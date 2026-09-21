"""Product APIs for ResumeIQ's career intelligence workspace.

The first release intentionally uses deterministic, explainable heuristics.
Provider-backed AI, persistence, and source connectors can be added behind
these stable contracts without changing the client application.
"""
from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from fastapi import APIRouter
from pydantic import BaseModel, Field

router = APIRouter(prefix="/platform", tags=["platform"])


class MatchRequest(BaseModel):
    resume_text: str = Field(min_length=20)
    job_description: str = Field(min_length=20)


class MatchResponse(BaseModel):
    score: int
    matched_terms: list[str]
    missing_terms: list[str]
    evidence_warnings: list[str]
    generated_at: str


class JobRecord(BaseModel):
    id: str
    title: str
    company: str
    location: str
    source_url: str
    status: str
    last_verified_at: str
    tags: list[str]


class EvidenceItem(BaseModel):
    title: str
    description: str
    evidence_type: str
    verified_by_user: bool = False


COMMON_SKILLS = {
    "python", "java", "c#", ".net", "azure", "aws", "gcp", "kubernetes",
    "docker", "sql", "postgresql", "microservices", "kafka", "ai", "genai",
    "llm", "rag", "fastapi", "react", "typescript", "system design",
}


def _terms(text: str) -> set[str]:
    normalized = text.lower().replace("/", " ")
    return {skill for skill in COMMON_SKILLS if skill in normalized}


@router.post("/match", response_model=MatchResponse)
async def match_resume(payload: MatchRequest) -> MatchResponse:
    resume_terms = _terms(payload.resume_text)
    job_terms = _terms(payload.job_description)
    matched = sorted(resume_terms & job_terms)
    missing = sorted(job_terms - resume_terms)
    score = 100 if not job_terms else round(len(matched) / len(job_terms) * 100)
    warnings = []
    if not resume_terms:
        warnings.append("No supported skills were detected; review the extracted profile.")
    if missing:
        warnings.append("Missing terms indicate absent resume evidence, not confirmed skill gaps.")
    return MatchResponse(
        score=score,
        matched_terms=matched,
        missing_terms=missing,
        evidence_warnings=warnings,
        generated_at=datetime.now(timezone.utc).isoformat(),
    )


@router.get("/jobs", response_model=list[JobRecord])
async def list_jobs() -> list[JobRecord]:
    """Return demo records; production connectors must verify official sources."""
    now = datetime.now(timezone.utc).isoformat()
    return [
        JobRecord(
            id="demo-001", title="Principal Software Engineer", company="Example Cloud",
            location="Remote / India", source_url="https://example.com/careers",
            status="demo", last_verified_at=now, tags=["azure", "distributed-systems"],
        )
    ]


@router.get("/dashboard")
async def dashboard() -> dict[str, Any]:
    return {
        "candidate": {"profile_completion": 62, "evidence_items": 0},
        "applications": {"saved": 0, "in_progress": 0, "submitted": 0},
        "insights": ["Upload a resume and add a target job to begin."],
    }


@router.post("/evidence", response_model=EvidenceItem)
async def add_evidence(item: EvidenceItem) -> EvidenceItem:
    """Validate the contract; persistence is intentionally injected later."""
    return item
