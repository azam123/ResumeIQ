# ResumeIQ — AI Career Intelligence Platform

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-async-green)](https://fastapi.tiangolo.com/)
[![Tests](https://img.shields.io/badge/tests-pytest-orange)](https://pytest.org/)
[![License](https://img.shields.io/badge/license-MIT-lightgrey)](LICENSE)

**ResumeIQ** is an evidence-first career intelligence platform for candidates and recruiters. It combines resume analysis, explainable job matching, ATS diagnostics, career gap analysis, professional evidence, and job-source freshness workflows.

> Scores are diagnostic signals, not hiring probabilities. Missing resume evidence is not proof that a candidate lacks a skill.

## Product capabilities

### Candidate
- Resume parsing and AI-assisted analysis
- Explainable resume-to-job matching
- ATS parsing and content diagnostics
- Evidence Vault for verified achievements and projects
- Career Twin and skill graph roadmap (planned)
- Career gap and transferable-skill analysis (planned)
- Job discovery with source URL and last-verified metadata
- Application tracking and interview story bank (planned)
- LinkedIn import through approved permissions or user-provided data (planned)

### Recruiter
- Organization-aware candidate workspaces (planned)
- Consent-based candidate evidence review (planned)
- Requisition and requirement parsing (planned)
- Human-led shortlist workflows (planned)
- Audit logs, access controls, and fairness review (planned)

### Platform
- Modular FastAPI backend
- Typed Pydantic contracts
- Deterministic explainable matching baseline
- Responsive frontend prototype
- PRD in `docs/PRODUCT_PRD.md`

## Current repository structure

```text
ResumeIQ/
├── app/
│   ├── agents/              # AI orchestration
│   ├── api/v1/              # Resume and platform APIs
│   ├── core/                # Configuration and logging
│   ├── exporters/           # PDF/DOCX exports
│   ├── models/              # Typed schemas
│   ├── scoring/             # Deterministic scoring
│   └── services/            # Parsing and provider integrations
├── frontend/index.html      # Candidate/recruiter UI prototype
├── docs/PRODUCT_PRD.md      # Product requirements
├── tests/
├── pyproject.toml
└── README.md
```

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
uvicorn app.main:app --reload
```

Open the API documentation at `http://localhost:8000/docs`.

The static frontend can be served with:

```bash
python -m http.server 5173 --directory frontend
```

Configure the frontend API base URL or reverse proxy it through the FastAPI host for local integrated use.

## API endpoints

| Endpoint | Purpose |
|---|---|
| `GET /health` | Service health |
| `POST /api/v1/resume/analyze` | AI resume analysis |
| `POST /api/v1/platform/match` | Explainable matching baseline |
| `GET /api/v1/platform/jobs` | Demo job contract |
| `GET /api/v1/platform/dashboard` | Candidate dashboard summary |
| `POST /api/v1/platform/evidence` | Evidence contract |

## Production roadmap

1. Add authentication and role-based access control.
2. Add PostgreSQL persistence, migrations, object storage, and tenant isolation.
3. Add permitted official career-site connectors and freshness verification.
4. Add robust document extraction, evaluation datasets, and provider abstraction.
5. Add candidate consent, deletion/export, audit logging, and encryption controls.
6. Add recruiter workflows only after privacy, fairness, and employment compliance review.
7. Add CI/CD, containerization, observability, security scanning, and load testing.

## Search keywords

`AI resume analyzer`, `resume ATS score`, `job matching`, `career intelligence`, `career copilot`, `resume optimization`, `LinkedIn optimization`, `skill gap analysis`, `job discovery`, `job verification`, `candidate dashboard`, `recruiter dashboard`, `FastAPI`, `Python`, `LLM`, `RAG`, `career twin`, `evidence vault`, `explainable AI`.

## Disclaimer

ResumeIQ is an assistive career tool. It does not guarantee ATS passage, recruiter attention, interviews, employment, job authenticity, or hiring outcomes. Integrations must respect provider terms, permissions, privacy requirements, and applicable law.
