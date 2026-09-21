from pathlib import Path
from uuid import uuid4

import logging

from app.exporters.docx_exporter import DocxExporter
from app.exporters.pdf_exporter import PdfExporter
from app.models.schemas import ATSResume
from app.scoring.engine import ResumeScoringEngine
from app.services.claude_service import ClaudeService
from app.services.parsing_service import ParsingService

logger = logging.getLogger(__name__)


class ResumeAgent:
    def __init__(
        self,
        parsing_service: ParsingService,
        claude_service: ClaudeService,
        scoring_engine: ResumeScoringEngine,
        pdf_exporter: PdfExporter,
        docx_exporter: DocxExporter,
        output_dir: Path = Path("artifacts"),
    ) -> None:
        self._parsing_service = parsing_service
        self._claude_service = claude_service
        self._scoring_engine = scoring_engine
        self._pdf_exporter = pdf_exporter
        self._docx_exporter = docx_exporter
        self._output_dir = output_dir

    async def run(self, resume_text: str, job_description: str) -> dict:
        resume = self._parsing_service.parse(resume_text)
        jd = self._parsing_service.parse(job_description)

        ai_payload = await self._claude_service.generate_resume_analysis(
            resume_text=resume.cleaned_text,
            job_description=jd.cleaned_text,
        )

        optimized_resume = str(ai_payload.get("optimized_resume", resume.cleaned_text))
        missing_skills = [str(skill) for skill in ai_payload.get("missing_skills", [])]
        suggestions = [str(item) for item in ai_payload.get("improvement_suggestions", [])]
        ats_resume = ATSResume.model_validate(ai_payload.get("ats_resume", {}))

        score = self._scoring_engine.calculate_score(
            resume_skills=resume.extracted_skills,
            job_skills=jd.extracted_skills,
            ai_missing_skills=missing_skills,
            ai_suggestions=suggestions,
        )

        file_id = str(uuid4())
        pdf_path = self._pdf_exporter.export(ats_resume, self._output_dir / f"resume_{file_id}.pdf")
        docx_path = self._docx_exporter.export(ats_resume, self._output_dir / f"resume_{file_id}.docx")

        logger.info("Resume analysis completed with score=%s", score.final_score)

        return {
            "optimized_resume": optimized_resume,
            "match_score": score.final_score,
            "missing_skills": missing_skills,
            "improvement_suggestions": suggestions,
            "ats_resume": ats_resume,
            "pdf_path": str(pdf_path),
            "docx_path": str(docx_path),
        }
