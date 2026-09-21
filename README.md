# ResumeIQ — AI Career Intelligence Platform

<p align="center">
  <strong>Your career, backed by evidence.</strong><br />
  Explainable resume intelligence, job matching, career insights, and evidence-first workflows.
</p>

<p align="center">
  <a href="https://github.com/azam123/ResumeIQ/actions"><img src="https://img.shields.io/github/actions/workflow/status/azam123/ResumeIQ/ci.yml?branch=main&label=CI&logo=github" alt="CI status" /></a>
  <a href="https://github.com/azam123/ResumeIQ"><img src="https://img.shields.io/github/stars/azam123/ResumeIQ?style=flat&logo=github" alt="GitHub stars" /></a>
  <a href="https://github.com/azam123/ResumeIQ/issues"><img src="https://img.shields.io/github/issues/azam123/ResumeIQ" alt="GitHub issues" /></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.11%2B-3776AB?logo=python&logoColor=white" alt="Python 3.11+" /></a>
  <a href="https://fastapi.tiangolo.com/"><img src="https://img.shields.io/badge/FastAPI-API-009688?logo=fastapi&logoColor=white" alt="FastAPI" /></a>
  <a href="https://pytest.org/"><img src="https://img.shields.io/badge/Tests-pytest-0A9EDC?logo=pytest&logoColor=white" alt="pytest" /></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-green.svg" alt="MIT License" /></a>
</p>

<p align="center">
  <a href="#-features">Features</a> •
  <a href="#-local-development">Local Development</a> •
  <a href="#-cloud-deployment">Cloud Deployment</a> •
  <a href="#-api-endpoints">API</a> •
  <a href="#-roadmap">Roadmap</a>
</p>

---

## 🚀 Overview

**ResumeIQ** is an evidence-first career intelligence platform for candidates and recruiters. It is designed to combine resume analysis, explainable job matching, ATS diagnostics, career gap analysis, professional evidence, and job-source freshness workflows.

> ⚠️ **Important:** Scores are diagnostic signals, not hiring probabilities. Missing resume evidence is not proof that a candidate lacks a skill.

## ✨ Features

### 👤 Candidate Workspace

- 📄 Resume parsing and AI-assisted analysis
- 🎯 Explainable resume-to-job matching
- 🧩 ATS parsing and content diagnostics
- 🗂️ Evidence Vault for achievements, projects, and architecture work
- 🧭 Career Twin and skill graph roadmap *(planned)*
- 📊 Career gap and transferable-skill analysis *(planned)*
- 🔎 Job discovery with source URL and verification metadata
- 📝 Application tracking and interview story bank *(planned)*
- 🔗 LinkedIn analysis through approved permissions or user-provided data *(planned)*

### 🧑‍💼 Recruiter Workspace

- 🏢 Organization-aware candidate workspaces *(planned)*
- 🔐 Consent-based candidate evidence review *(planned)*
- 📌 Requisition and requirement parsing *(planned)*
- 👥 Human-led shortlist workflows *(planned)*
- 🧾 Audit logs, access controls, and fairness review *(planned)*

### ⚙️ Platform Capabilities

- 🐍 Modular FastAPI backend
- ✅ Typed Pydantic contracts
- 🔍 Deterministic, explainable matching baseline
- 📱 Responsive frontend prototype
- 📚 Product requirements in `docs/PRODUCT_PRD.md`

## 🏷️ Technology Tags

`Python` `FastAPI` `Pydantic` `AI` `Generative AI` `RAG` `Resume Analysis` `ATS` `Job Matching` `Career Intelligence` `Explainable AI` `Career Copilot` `LinkedIn Optimization` `Skill Gap Analysis` `Evidence Vault` `REST API` `Responsive UI`

## 🗂️ Repository Structure

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
├── frontend/
│   └── index.html           # Candidate/recruiter UI prototype
├── docs/
│   └── PRODUCT_PRD.md       # Product requirements
├── tests/                   # Automated tests
├── pyproject.toml           # Python project configuration
└── README.md
```

# 💻 Local Development

## 1️⃣ Prerequisites

Install the following tools before starting:

- **Python 3.11 or newer** — [Download Python](https://www.python.org/downloads/)
- **Git** — [Install Git](https://git-scm.com/downloads)
- Optional: **Docker** for containerized development

Check your installed versions:

```bash
python --version
python -m pip --version
git --version
```

## 2️⃣ Clone the Repository

```bash
git clone https://github.com/azam123/ResumeIQ.git
cd ResumeIQ
```

## 3️⃣ Create and Activate a Virtual Environment

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Windows PowerShell

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

## 4️⃣ Install Dependencies

Install the project and development dependencies:

```bash
python -m pip install --upgrade pip
pip install -e ".[dev]"
```

If your shell does not support the quoted extra syntax, run:

```bash
pip install -e .
pip install pytest pytest-cov ruff
```

## 5️⃣ Configure Environment Variables

Create a local environment file if your configuration supports environment-based settings:

```bash
cp .env.example .env
```

On Windows, copy the file manually:

```powershell
Copy-Item .env.example .env
```

Never commit secrets, API keys, OAuth credentials, or production connection strings to Git.

## 6️⃣ Start the FastAPI Backend

Run the API in development mode:

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The backend will be available at:

| Resource | URL |
|---|---|
| Health check | `http://localhost:8000/health` |
| Swagger UI | `http://localhost:8000/docs` |
| ReDoc | `http://localhost:8000/redoc` |
| OpenAPI schema | `http://localhost:8000/openapi.json` |

## 7️⃣ Start the Frontend

Open a second terminal from the project root and serve the static frontend:

```bash
python -m http.server 5173 --directory frontend
```

Open the UI at:

```text
http://localhost:5173
```

The frontend uses the backend API endpoints listed below. For integrated development, configure a reverse proxy or set the API base URL according to the frontend implementation.

### 🔌 Frontend API Base URL

The frontend can use a configurable API base value such as:

```javascript
window.RESUMEIQ_API_BASE = "http://localhost:8000";
```

For production, prefer serving the frontend and API behind the same domain or configure CORS and a secure reverse proxy explicitly.

## 🧪 Run Tests and Quality Checks

Run the test suite:

```bash
pytest -q
```

Run tests with coverage:

```bash
pytest --cov=app --cov-report=term-missing
```

Run linting and formatting checks when configured:

```bash
ruff check .
ruff format --check .
```

## 🐳 Optional: Run with Docker

A production Docker setup should include a dedicated `Dockerfile`, environment configuration, health checks, and a secure process configuration. If Docker files are added to the repository, a typical local command will be:

```bash
docker build -t resumeiq-api .
docker run --rm -p 8000:8000 --env-file .env resumeiq-api
```

> ℹ️ Do not use this example until the repository contains a validated Dockerfile and the required runtime configuration.

# ☁️ Cloud Deployment

ResumeIQ currently contains a FastAPI backend and a static frontend prototype. The deployment options below describe a practical architecture; production readiness requires authentication, persistence, monitoring, security controls, and validation of all integrations.

## Recommended Cloud Architecture

```text
                    ┌────────────────────────┐
                    │  Browser / User         │
                    └────────────┬───────────┘
                                 │ HTTPS
                    ┌────────────▼───────────┐
                    │ Static Frontend / CDN  │
                    └────────────┬───────────┘
                                 │ HTTPS API
                    ┌────────────▼───────────┐
                    │ FastAPI Application    │
                    │ Container / App Service│
                    └───────┬─────────┬──────┘
                            │         │
              ┌─────────────▼─┐   ┌───▼─────────────┐
              │ PostgreSQL     │   │ Object Storage  │
              │ Database       │   │ Resumes / Files │
              └───────────────┘   └─────────────────┘
```

## ☁️ Option A: Microsoft Azure

A suitable Azure deployment can use:

- **Azure Static Web Apps** or **Azure Storage Static Website** for the frontend
- **Azure App Service** or **Azure Container Apps** for FastAPI
- **Azure Database for PostgreSQL** for application data
- **Azure Blob Storage** for resume and evidence files
- **Azure Key Vault** for secrets
- **Application Insights** for monitoring and diagnostics
- **Azure Front Door** or an equivalent secure entry point for routing and protection

### Azure deployment flow

1. Create an Azure resource group.
2. Provision the API hosting service.
3. Configure Python runtime or deploy a validated container.
4. Configure environment variables and secrets through managed configuration or Key Vault.
5. Deploy the frontend to Static Web Apps or a storage-backed static website.
6. Configure the frontend API base URL to point to the HTTPS API endpoint.
7. Configure CORS to allow only approved frontend origins.
8. Add health checks, application logging, alerts, and deployment rollback procedures.
9. Validate authentication, authorization, file upload limits, and data retention before accepting real user data.

Example API startup command for a managed Linux host:

```bash
gunicorn app.main:app \
  -k uvicorn.workers.UvicornWorker \
  --bind 0.0.0.0:${PORT:-8000} \
  --workers 2
```

Tune worker count based on workload, memory, concurrency, and the selected hosting service.

## ☁️ Option B: AWS

A comparable AWS architecture can use:

- **S3 + CloudFront** for the static frontend
- **ECS Fargate** or **App Runner** for the FastAPI service
- **RDS PostgreSQL** for relational persistence
- **S3** for resume and evidence storage
- **Secrets Manager** or **Systems Manager Parameter Store** for secrets
- **CloudWatch** for logs, metrics, and alerts
- **Application Load Balancer** for HTTPS routing

### AWS deployment flow

1. Build and test the API locally.
2. Create a secure container image for the FastAPI service.
3. Push the image to Amazon ECR.
4. Deploy the image using ECS Fargate, App Runner, or another supported service.
5. Configure the service environment and secrets.
6. Deploy the frontend assets to S3 and distribute them through CloudFront.
7. Configure HTTPS, CORS, health checks, and logging.
8. Add database migrations and backup policies before production use.

## ☁️ Option C: Container Platform

The API can also be hosted on a container platform such as:

- Google Cloud Run
- Azure Container Apps
- AWS App Runner
- Kubernetes
- A managed virtual machine with a reverse proxy

For production, use:

- 🔒 HTTPS and secure headers
- 🛡️ Authentication and role-based authorization
- 🧾 Structured logging and audit events
- 📈 Metrics and distributed tracing
- 🔄 Automated deployment and rollback
- 💾 Database backups and migration controls
- 🧪 Security and load testing
- 🗑️ User data deletion and export workflows

# 🔌 API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| `GET` | `/health` | Service health check |
| `POST` | `/api/v1/resume/analyze` | Resume analysis |
| `POST` | `/api/v1/platform/match` | Explainable matching baseline |
| `GET` | `/api/v1/platform/jobs` | Job contract / demo jobs |
| `GET` | `/api/v1/platform/dashboard` | Candidate dashboard summary |
| `POST` | `/api/v1/platform/evidence` | Evidence contract |

Use Swagger UI at `http://localhost:8000/docs` to inspect request and response schemas.

# 🛡️ Security and Privacy Checklist

Before using ResumeIQ with real candidate data:

- [ ] Add authentication and role-based access control.
- [ ] Encrypt data in transit and at rest.
- [ ] Add tenant isolation and authorization checks.
- [ ] Validate uploaded file types, sizes, and content.
- [ ] Store secrets in a managed secret store.
- [ ] Add consent, deletion, and data export workflows.
- [ ] Avoid collecting unnecessary personal information.
- [ ] Add audit logs for sensitive operations.
- [ ] Review third-party API terms and privacy requirements.
- [ ] Evaluate fairness and explainability of candidate-facing outputs.
- [ ] Do not represent diagnostic scores as hiring probabilities.

# 🧭 Roadmap

1. Authentication and role-based access control.
2. PostgreSQL persistence, migrations, object storage, and tenant isolation.
3. Official career-site connectors with source and freshness verification.
4. Robust document extraction and evaluation datasets.
5. Provider abstraction for LLM and embedding services.
6. Candidate consent, deletion/export, audit logging, and encryption controls.
7. Recruiter workflows with privacy, fairness, and employment compliance review.
8. CI/CD, containerization, observability, security scanning, and load testing.
9. Career Twin, skill transferability, interview evidence generation, and career simulation.

# 🤝 Contributing

1. Fork the repository.
2. Create a feature branch:

   ```bash
   git checkout -b feature/your-feature
   ```

3. Make your changes and add tests.
4. Run quality checks locally.
5. Commit using a clear message:

   ```bash
   git commit -m "feat: describe your change"
   ```

6. Push your branch and open a pull request.

# 📄 License

This project is licensed under the MIT License. See `LICENSE` for details.

# ⚠️ Disclaimer

ResumeIQ is an assistive career tool. It does not guarantee ATS passage, recruiter attention, interviews, employment, job authenticity, or hiring outcomes. Integrations must respect provider terms, permissions, privacy requirements, and applicable law.
