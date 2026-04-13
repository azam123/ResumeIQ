# ResumeIQ

ResumeIQ is a production-style FastAPI backend that uses an AI-agent orchestration flow (powered by Claude via Anthropic API) to:

- Compare a resume against a job description
- Produce a match score (0-100)
- Rewrite and optimize resume content
- Return missing skills and suggestions
- Export ATS-structured output to PDF and DOCX

## Architecture (Layered)

1. **API Layer** (`app/api`)  
   FastAPI endpoints, request validation, HTTP error mapping.
2. **Agent Layer** (`app/agents`)  
   Orchestrates parse -> AI optimize -> deterministic+AI scoring -> export.
3. **Service Layer** (`app/services`)  
   Claude integration and parsing/skill extraction logic.
4. **Scoring Engine** (`app/scoring`)  
   Hybrid deterministic + AI-aware scoring.
5. **Export Layer** (`app/exporters`)  
   ATS resume export to PDF/DOCX.
6. **Core Layer** (`app/core`)  
   Configuration, environment management, and logging.

## Project Structure

```text
ResumeIQ/
├── app/
│   ├── agents/
│   │   └── resume_agent.py
│   ├── api/
│   │   ├── deps.py
│   │   └── v1/resume.py
│   ├── core/
│   │   ├── config.py
│   │   └── logging.py
│   ├── exporters/
│   │   ├── docx_exporter.py
│   │   └── pdf_exporter.py
│   ├── models/
│   │   └── schemas.py
│   ├── scoring/
│   │   └── engine.py
│   ├── services/
│   │   ├── claude_service.py
│   │   └── parsing_service.py
│   └── main.py
├── tests/
│   └── test_scoring_engine.py
├── pyproject.toml
└── README.md
```

## Setup

### 1) Create environment

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

### 2) Configure environment variables

Create `.env`:

```bash
ANTHROPIC_API_KEY=your_api_key_here
ANTHROPIC_MODEL=claude-3-7-sonnet-20250219
ANTHROPIC_BASE_URL=https://api.anthropic.com
APP_NAME=ResumeIQ
ENV=development
```

### 3) Run API

```bash
uvicorn app.main:app --reload
```

## API

### `POST /api/v1/resume/analyze`

Request:

```json
{
  "resume_text": "...",
  "job_description": "..."
}
```

Response includes:

- `optimized_resume`
- `match_score`
- `missing_skills`
- `improvement_suggestions`
- `ats_resume`
- `pdf_path`
- `docx_path`

## Notes

- Uses async HTTP client (`httpx.AsyncClient`) for Anthropic API calls.
- Handles upstream AI errors with 502 and unknown errors with 500.
- Uses pydantic models and settings for strong typing and config safety.
