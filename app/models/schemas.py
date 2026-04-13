from typing import Any

from pydantic import BaseModel, Field


class AnalyzeResumeRequest(BaseModel):
    resume_text: str = Field(..., min_length=50)
    job_description: str = Field(..., min_length=50)


class ATSResume(BaseModel):
    header: dict[str, str] = Field(default_factory=dict)
    summary: str = ""
    skills: list[str] = Field(default_factory=list)
    experience: list[dict[str, Any]] = Field(default_factory=list)
    education: list[dict[str, Any]] = Field(default_factory=list)
    certifications: list[str] = Field(default_factory=list)


class AnalyzeResumeResponse(BaseModel):
    optimized_resume: str
    match_score: int = Field(..., ge=0, le=100)
    missing_skills: list[str]
    improvement_suggestions: list[str]
    ats_resume: ATSResume
    pdf_path: str
    docx_path: str
