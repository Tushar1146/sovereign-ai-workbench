# Local Setup

## Prerequisites

- Python 3.10+
- Git
- Optional: Ollama for local LLM inference

## Install

```bash
git clone https://github.com/Tushar1146/sovereign-ai-workbench.git
cd sovereign-ai-workbench
python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
pip install -r requirements.txt
```

### Linux/macOS

```bash
source .venv/bin/activate
pip install -r requirements.txt
```

## Run the backend

```bash
uvicorn backend.main:app --reload
```

Open `http://127.0.0.1:8000` in a browser.

## Optional: Ollama

Install Ollama locally and pull a model, for example:

```bash
ollama pull llama3.2:3b
```

Then start the application. The backend checks the local Ollama endpoint and uses it when available.

## Current prototype limitations

The initial prototype uses simple local keyword retrieval. Production development should replace this with a real local embedding/vector pipeline, structured agent execution, stronger security controls, multimodal processing, evidence attribution and deliverable generation.
