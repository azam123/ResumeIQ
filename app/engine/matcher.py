"""Deterministic, explainable baseline matcher.

This module deliberately separates evidence-backed matching from optional LLM
reasoning. Scores are diagnostic signals and must not be treated as hiring
probabilities.
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class MatchReport:
    overall_score: float
    skill_score: float
    responsibility_score: float
    leadership_score: float
    matched_keywords: list[str]
    missing_keywords: list[str]
    improvements: list[str]
    leadership_guidelines: list[str]


class ResumeMatchEngine:
    """Build an explainable resume/JD report using normalized lexical evidence."""

    DEFAULT_LEADERSHIP_TERMS = {
        "technical strategy", "architecture", "cross-functional", "mentoring",
        "influence", "roadmap", "design review", "stakeholder", "scalability",
        "reliability", "ownership", "technical direction", "trade-off",
    }

    def __init__(self, leadership_terms: Iterable[str] | None = None) -> None:
        self.leadership_terms = {
            self._normalize(term) for term in (leadership_terms or self.DEFAULT_LEADERSHIP_TERMS)
        }

    @staticmethod
    def _normalize(value: str) -> str:
        return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9+#.\-/ ]", " ", value.lower())).strip()

    @staticmethod
    def _terms(text: str) -> set[str]:
        normalized = ResumeMatchEngine._normalize(text)
        return {token for token in normalized.split() if len(token) > 2}

    def analyze(self, resume_text: str, job_description: str) -> MatchReport:
        resume = self._normalize(resume_text)
        job = self._normalize(job_description)
        resume_terms, job_terms = self._terms(resume), self._terms(job)
        matched = sorted(resume_terms & job_terms)
        missing = sorted(job_terms - resume_terms)

        skill_terms = {t for t in job_terms if any(x in t for x in ("python", "java", "c#", "azure", "aws", "sql", "kubernetes", "docker", "api", "microservice", "architecture", "ai", "rag"))}
        responsibility_terms = job_terms - skill_terms
        leadership_in_jd = {t for t in self.leadership_terms if t in job}
        leadership_matched = {t for t in leadership_in_jd if t in resume}

        skill_score = self._ratio(skill_terms, resume_terms)
        responsibility_score = self._ratio(responsibility_terms, resume_terms)
        leadership_score = self._ratio(leadership_in_jd, resume_terms) if leadership_in_jd else 0.0
        overall = round(skill_score * 0.45 + responsibility_score * 0.35 + leadership_score * 0.20, 2)

        improvements = []
        if missing: improvements.append("Add missing requirements only when supported by genuine experience.")
        if leadership_in_jd - leadership_matched: improvements.append("Add evidence of leadership scope, influence, architecture decisions, and mentoring where applicable.")
        if not re.search(r"\b(\d+%|\d+\s+(users|requests|services|teams|documents|ms|hours))\b", resume): improvements.append("Add defensible metrics, baselines, and outcomes to major achievements.")
        if not re.search(r"\b(designed|architected|led|optimized|implemented|migrated|automated)\b", resume): improvements.append("Rewrite responsibility statements with clear action and contribution verbs.")

        leadership_guidelines = [
            "Show cross-team influence and technical decision ownership.",
            "Describe system scale, complexity, reliability, and trade-offs.",
            "Demonstrate mentoring, stakeholder alignment, and technical direction.",
            "Separate personal contributions from team-level outcomes.",
            "Use measurable evidence without inventing metrics.",
            "Treat missing resume evidence as an evidence gap, not proof of missing capability.",
        ]
        return MatchReport(overall, skill_score, responsibility_score, leadership_score, matched, missing, improvements, leadership_guidelines)

    @staticmethod
    def _ratio(required: set[str], available: set[str]) -> float:
        return round((len(required & available) / len(required) * 100) if required else 100.0, 2)
