# Sovereign AI Workbench

> **SIH26117 — Sovereign On-Premise Agentic AI Workbench using Open-Weight Multimodal LLMs for Confidential Industrial Work**

A private, on-premise AI workbench for confidential industrial workflows. The project combines local open-weight LLMs, private RAG, agentic tool execution, multimodal understanding, evidence-backed answers, data analysis, and local deliverable generation.

## Problem

Industrial organizations work with sensitive maintenance manuals, inspection reports, engineering documents, sensor data, correspondence, drawings, scanned documents, and equipment images. Using external AI services for these workflows can create data-leakage, security, compliance, and connectivity concerns.

## Proposed Solution

Sovereign AI Workbench provides a private AI environment where:

- Open-weight AI models run locally/on-premise.
- Company documents are indexed into a local knowledge base.
- RAG retrieves relevant private evidence before generation.
- Agents perform multi-step tasks using controlled local tools.
- CSV/XLSX sensor data can be analyzed locally.
- Images and scanned documents can be processed using local vision/OCR components.
- Answers can show supporting evidence and source references.
- Reports, approval notes, Excel analysis and presentations can be generated locally.
- Audit logs and security telemetry make system activity visible.

## Reference Industrial Demo

### Pump P-102 Analysis

Demo inputs:

- `Inspection_Report_P102.pdf`
- `Pump_Maintenance_Manual.pdf`
- `Sensor_Data_P102.csv`
- `Pump_P102_Image.jpg`

Example request:

> Analyze Pump P-102 using the available documents, sensor data and image. Identify abnormalities, compare findings with the maintenance manual, provide an evidence-backed recommendation and prepare a maintenance report.

Agent flow:

```text
Plan → Retrieve → Analyze → Cross-check → Recommend → Generate
```

## Architecture

```text
User
  ↓
Web Workbench
  ↓
Local API / Orchestrator
  ├── Model Router
  ├── RAG / Knowledge Base
  ├── Agent / Tool Registry
  ├── Data Analysis
  ├── Vision / OCR
  ├── Deliverable Generator
  └── Audit + Security
  ↓
Local Open-Weight Models / Ollama
  ↓
Local Evidence + Results + Reports
```

## Core Features

- 🔒 Local / on-premise AI inference
- 📚 Private RAG knowledge base
- 🤖 Agentic multi-step workflows
- 📊 CSV/XLSX analysis and anomaly detection
- 👁️ Multimodal document/image analysis
- 🔀 Automatic local model routing
- 📑 Evidence-first answers with source attribution
- 📄 Local report/document generation
- 📝 Audit logs
- 🛡️ Security and privacy telemetry

## Technology Direction

| Layer | Technology |
|---|---|
| Frontend | React / Vite / Tailwind |
| Backend | Python / FastAPI |
| Local model runtime | Ollama |
| RAG | Local embeddings + FAISS/Chroma |
| Documents | PyMuPDF / pypdf / python-docx |
| Data | Pandas / OpenPyXL |
| Agents | LangGraph or modular tool registry |
| Database | SQLite |
| Sandbox | Controlled local execution environment |

## Repository Structure

```text
frontend/             # Web application
backend/              # API, agents, RAG, tools and model routing
knowledge_base/       # Runtime KB storage; confidential data is not committed
sample_data/          # Synthetic demo assets only
tests/                # Automated tests
docs/                 # Architecture, security and demo documentation
```

## Local-Only Principle

The project is designed so that core inference and document processing do not require external AI APIs. Air-gapped operation depends on the deployment environment and its network policy.

**Important:** This public repository must contain only source code and synthetic/demo data. Never commit real industrial documents, credentials, API keys, `.env` secrets, audit logs containing sensitive data, or model weight files.

## Development Roadmap

- [x] Initial enterprise workbench UI
- [ ] Knowledge Base ingestion
- [ ] Local RAG retrieval and citations
- [ ] Agent execution workflow
- [ ] Sensor analytics
- [ ] Multimodal/vision pipeline
- [ ] Automatic model router
- [ ] Deliverable generation
- [ ] Security telemetry
- [ ] Audit logging
- [ ] End-to-end Pump P-102 demo

## Smart India Hackathon 2026

- **Problem Statement ID:** SIH26117
- **Organization:** Mangalore Refinery and Petrochemicals Limited (MRPL)
- **Theme:** Smart Automation
- **Category:** Software

## License

This project is developed as an SIH 2026 prototype. Add the team's preferred open-source license before public production use.
