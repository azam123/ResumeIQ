from functools import lru_cache

from app.agents.resume_agent import ResumeAgent
from app.core.config import get_settings
from app.exporters.docx_exporter import DocxExporter
from app.exporters.pdf_exporter import PdfExporter
from app.scoring.engine import ResumeScoringEngine
from app.services.claude_service import ClaudeService
from app.services.parsing_service import ParsingService


@lru_cache(maxsize=1)
def get_resume_agent() -> ResumeAgent:
    settings = get_settings()
    return ResumeAgent(
        parsing_service=ParsingService(),
        claude_service=ClaudeService(settings=settings),
        scoring_engine=ResumeScoringEngine(),
        pdf_exporter=PdfExporter(),
        docx_exporter=DocxExporter(),
    )
