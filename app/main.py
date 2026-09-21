from fastapi import FastAPI

from app.api.v1.platform import router as platform_router
from app.api.v1.resume import router as resume_router
from app.core.config import get_settings
from app.core.logging import configure_logging

configure_logging()
settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    version="0.2.0",
    description="ResumeIQ career intelligence APIs with explainable matching and evidence-first workflows.",
)
app.include_router(resume_router, prefix=settings.api_v1_prefix)
app.include_router(platform_router, prefix=settings.api_v1_prefix)


@app.get("/health", tags=["system"])
async def health() -> dict[str, str]:
    return {"status": "ok", "service": "resumeiq-api"}
