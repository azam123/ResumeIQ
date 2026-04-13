import logging

from fastapi import APIRouter, Depends, HTTPException, status

from app.agents.resume_agent import ResumeAgent
from app.api.deps import get_resume_agent
from app.models.schemas import AnalyzeResumeRequest, AnalyzeResumeResponse
from app.services.claude_service import ClaudeServiceError

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/resume", tags=["resume"])


@router.post("/analyze", response_model=AnalyzeResumeResponse, status_code=status.HTTP_200_OK)
async def analyze_resume(
    payload: AnalyzeResumeRequest,
    agent: ResumeAgent = Depends(get_resume_agent),
) -> AnalyzeResumeResponse:
    try:
        result = await agent.run(
            resume_text=payload.resume_text,
            job_description=payload.job_description,
        )
        return AnalyzeResumeResponse.model_validate(result)
    except ClaudeServiceError as exc:
        logger.exception("Claude service failure")
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail="Upstream AI provider failed",
        ) from exc
    except Exception as exc:  # noqa: BLE001
        logger.exception("Unexpected error during resume analysis")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        ) from exc
