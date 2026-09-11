from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from pathlib import Path
import re
import requests

BASE = Path(__file__).resolve().parent.parent
DATA = BASE / "data"
DATA.mkdir(exist_ok=True)

app = FastAPI(title="Sovereign AI Workbench")
app.mount("/static", StaticFiles(directory=str(BASE / "frontend")), name="static")

OLLAMA_URL = "http://127.0.0.1:11434/api/generate"
MODEL = "llama3.2:3b"

class ChatRequest(BaseModel):
    message: str

def local_docs():
    docs = []
    for p in DATA.glob("*"):
        if p.is_file():
            try:
                text = p.read_text(encoding="utf-8", errors="ignore")
            except Exception:
                continue
            docs.append({"name": p.name, "text": text})
    return docs

def retrieve(query, limit=3):
    terms = [x.lower() for x in re.findall(r"[A-Za-z0-9]{3,}", query)]
    scored = []
    for d in local_docs():
        low = d["text"].lower()
        score = sum(low.count(t) for t in terms)
        if score:
            scored.append((score, d))
    scored.sort(key=lambda x: x[0], reverse=True)
    return [d for _, d in scored[:limit]]

def demo_answer(message, docs):
    if docs:
        names = ", ".join(d["name"] for d in docs)
        return (
            "Demo-mode local assistant response.\n\n"
            f"I searched the local knowledge base and found relevant information in: {names}.\n\n"
            "In the full version, a local LLM would use these retrieved passages to "
            "produce a grounded answer with page/section citations. No external AI API is used."
        )
    return (
        "Demo-mode local assistant response.\n\n"
        "No matching local documents were found. Upload a company document and ask a question "
        "about it. In the full version, the local LLM would answer using the company's private knowledge base."
    )

def ollama_available():
    try:
        r = requests.get("http://127.0.0.1:11434/api/tags", timeout=1.5)
        return r.ok
    except Exception:
        return False

@app.get("/", response_class=HTMLResponse)
def home():
    return (BASE / "frontend" / "index.html").read_text(encoding="utf-8")

@app.get("/api/status")
def status():
    return {
        "privacy": True,
        "external_ai_calls": 0,
        "ollama": ollama_available(),
        "model": MODEL if ollama_available() else "Demo Local Mode",
        "documents": len(local_docs())
    }

@app.get("/api/documents")
def documents():
    return [{"name": d["name"], "size": len(d["text"])} for d in local_docs()]

@app.post("/api/upload")
async def upload(file: UploadFile = File(...)):
    data = await file.read()
    suffix = Path(file.filename).suffix.lower()
    if suffix == ".pdf":
        try:
            from pypdf import PdfReader
            import io
            reader = PdfReader(io.BytesIO(data))
            text = "\n".join(page.extract_text() or "" for page in reader.pages)
        except Exception as e:
            return {"ok": False, "error": f"PDF extraction failed: {e}"}
    else:
        text = data.decode("utf-8", errors="ignore")
    safe = re.sub(r"[^A-Za-z0-9._-]", "_", file.filename)
    (DATA / safe).write_text(text, encoding="utf-8")
    return {"ok": True, "name": safe, "characters": len(text)}

@app.post("/api/chat")
def chat(req: ChatRequest):
    docs = retrieve(req.message)
    context = "\n\n".join(
        f"[SOURCE: {d['name']}]\n{d['text'][:6000]}" for d in docs
    )

    if ollama_available():
        prompt = f"""You are a private enterprise AI assistant.
All processing is local. Use only the provided local context when it is relevant.
If the context is insufficient, say so clearly. Cite source filenames.

LOCAL CONTEXT:
{context or 'No relevant local documents found.'}

USER:
{req.message}

Answer concisely and include a Sources section if sources were used."""
        try:
            r = requests.post(
                OLLAMA_URL,
                json={"model": MODEL, "prompt": prompt, "stream": False},
                timeout=120,
            )
            if r.ok:
                return {
                    "answer": r.json().get("response", "").strip(),
                    "sources": [d["name"] for d in docs],
                    "mode": "local-llm"
                }
        except Exception:
            pass

    return {
        "answer": demo_answer(req.message, docs),
        "sources": [d["name"] for d in docs],
        "mode": "demo"
    }
