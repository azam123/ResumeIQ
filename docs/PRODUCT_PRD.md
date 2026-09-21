# ResumeIQ Product Requirements Document

## 1. Vision
ResumeIQ is an evidence-first career intelligence platform that helps candidates understand job fit, improve application quality, discover verified opportunities, and plan career growth. Recruiter workflows must remain human-led and privacy-aware.

## 2. Personas
- Candidate: uploads resume, manages career evidence, matches jobs, tracks applications, and prepares for interviews.
- Recruiter: searches consented candidate profiles, reviews evidence, and manages requisitions.
- Admin/data steward: manages source connectors, freshness, abuse, privacy, and audit logs.

## 3. MVP scope
- Resume PDF/DOCX ingestion and structured extraction.
- Job-description parsing from pasted text and permitted URLs.
- Explainable match score with matched terms, missing evidence, and uncertainty labels.
- ATS parsing diagnostics; never present a score as a hiring probability.
- Evidence Vault with user confirmation and provenance.
- Candidate dashboard and application tracker.
- Source URL, last-verified timestamp, and stale/uncertain job status.
- Accessible responsive web UI and versioned REST API.

## 4. Expansion scope
- Official career-site connectors and licensed feeds.
- Career Twin and skill graph.
- Skill transferability and career path simulation.
- LinkedIn import only through approved permissions or user-provided exports.
- Interview story bank and evidence-grounded question generation.
- Recruiter organizations, roles, consent, and audit trails.
- Notifications, subscriptions, and analytics.

## 5. Non-functional requirements
- Python 3.11+, FastAPI, typed Pydantic contracts.
- PostgreSQL for transactional data; object storage for documents; optional vector search.
- Async workers for ingestion and verification.
- OAuth/OIDC, least privilege, encryption in transit and at rest.
- Tenant isolation, retention controls, deletion/export workflows.
- Structured logs, metrics, traces, rate limits, and idempotent jobs.
- Unit, integration, contract, security, and accessibility tests.
- WCAG-oriented keyboard navigation and readable contrast.

## 6. Core entities
User, Organization, CandidateProfile, Resume, ResumeVersion, EvidenceItem, Job, JobSource, JobVerification, MatchReport, Gap, Application, InterviewStory, ConsentRecord, AuditEvent, Subscription.

## 7. API outline
- `POST /api/v1/resume/analyze`
- `POST /api/v1/platform/match`
- `GET /api/v1/platform/jobs`
- `GET /api/v1/platform/dashboard`
- `POST /api/v1/platform/evidence`
Future endpoints must use authentication, authorization, pagination, validation, and audit logging.

## 8. Matching methodology
Use weighted, explainable features: required-skill coverage, preferred-skill coverage, experience alignment, responsibility evidence, location/authorization constraints, and data completeness. Missing resume evidence must not be treated as proof that a candidate lacks a skill. Scores require calibration and should not be used for automated employment rejection.

## 9. Job freshness
Every listing stores source URL, source identifier, fetched time, last verified time, status, and verification result. Connectors must respect source terms, robots directives where applicable, rate limits, and licensing. Closed or uncertain listings must not be presented as confirmed active.

## 10. AI safety and trust
- Never fabricate experience, achievements, employers, qualifications, or recruiter outcomes.
- Show citations/provenance where possible.
- Require user confirmation before publishing generated claims.
- Redact secrets and detect potentially confidential content.
- Provide explanations and uncertainty, not guaranteed ATS or hiring outcomes.
- Apply privacy, employment, and data-protection review before recruiter automation.

## 11. Success metrics
Activation, completed analyses, repeat usage, report usefulness, correction rate, verified job click-through, application tracking adoption, deletion request completion, latency, error rate, and customer willingness to pay. Do not use hiring outcomes as a sole quality metric.

## 12. Delivery phases
1. Foundation: contracts, auth, storage, parsing, tests.
2. Candidate MVP: matching, reports, evidence, dashboard.
3. Job intelligence: connectors, deduplication, freshness, alerts.
4. Career copilot: LinkedIn alternatives, interview stories, learning roadmap.
5. Recruiter product: organization permissions, search, auditability, human review.
