# Architecture

## High-Level Flow

```text
User
  ↓
React/Vite Workbench
  ↓
FastAPI Backend
  ↓
Orchestrator
  ├── Model Router ─────→ Local Ollama Models
  ├── RAG Engine ───────→ Local Vector Store
  ├── Agent ─────────────→ Controlled Tool Registry
  ├── Data Tools ───────→ Pandas / OpenPyXL
  ├── Document Tools ────→ PyMuPDF / pypdf
  ├── Vision/OCR ────────→ Local Models / OCR
  ├── Deliverables ──────→ DOCX / XLSX / PPTX / PDF
  └── Audit + Security ──→ SQLite / Local Logs
```

## Design Principles

1. **Local-first:** core AI inference and sensitive processing happen locally.
2. **Evidence-first:** important conclusions should reference retrieved evidence.
3. **Tool-controlled agents:** agents use an allow-listed tool registry instead of unrestricted system access.
4. **Model flexibility:** the workbench should support multiple local open-weight models.
5. **Observable security:** model status, external API activity and audit events should be visible.
6. **Synthetic demo data:** public development uses synthetic industrial data only.

## Example Workflow

```text
Task: Analyze Pump P-102
        ↓
Task classification / model routing
        ↓
Retrieve relevant maintenance + inspection evidence
        ↓
Analyze sensor CSV
        ↓
Analyze image if a local vision model is available
        ↓
Cross-check against maintenance guidance
        ↓
Generate evidence-backed recommendation
        ↓
Create maintenance report
        ↓
Write audit events
```
