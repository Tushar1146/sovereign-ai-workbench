# Backend

FastAPI backend for the Sovereign AI Workbench.

Planned modules:

- `api/` — REST endpoints
- `agents/` — agent orchestration
- `rag/` — ingestion, embeddings and retrieval
- `tools/` — controlled local tools
- `models/` — Ollama/model routing
- `vision/` — OCR and local multimodal processing
- `security/` — privacy controls and telemetry
- `audit/` — audit event persistence

The current prototype keeps the first implementation in `main.py` and will be modularized as features are added.
