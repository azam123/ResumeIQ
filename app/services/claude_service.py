import json
import logging

import httpx

from app.core.config import Settings

logger = logging.getLogger(__name__)


class ClaudeServiceError(Exception):
    pass


class ClaudeService:
    def __init__(self, settings: Settings) -> None:
        self._settings = settings

    async def generate_resume_analysis(self, resume_text: str, job_description: str) -> dict:
        prompt = self._build_prompt(resume_text=resume_text, job_description=job_description)
        payload = {
            "model": self._settings.anthropic_model,
            "max_tokens": 1500,
            "temperature": 0.2,
            "messages": [{"role": "user", "content": prompt}],
        }
        headers = {
            "x-api-key": self._settings.anthropic_api_key,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json",
        }

        try:
            async with httpx.AsyncClient(timeout=self._settings.request_timeout_seconds) as client:
                response = await client.post(
                    f"{self._settings.anthropic_base_url}/v1/messages",
                    headers=headers,
                    json=payload,
                )
                response.raise_for_status()
                data = response.json()
        except (httpx.HTTPError, ValueError) as exc:
            logger.exception("Anthropic API request failed")
            raise ClaudeServiceError("Failed to get response from Anthropic API") from exc

        return self._extract_json_block(data)

    @staticmethod
    def _build_prompt(resume_text: str, job_description: str) -> str:
        return (
            "You are an expert resume optimization assistant.\n"
            "Given a resume and a job description, return a JSON object with these keys only:\n"
            "optimized_resume, missing_skills, improvement_suggestions, ats_resume\n"
            "Where ats_resume has: header, summary, skills, experience, education, certifications.\n"
            "Ensure missing_skills and improvement_suggestions are arrays of strings.\n"
            "Return strict JSON with no markdown fences.\n\n"
            f"Resume:\n{resume_text}\n\n"
            f"Job Description:\n{job_description}"
        )

    @staticmethod
    def _extract_json_block(raw_response: dict) -> dict:
        try:
            text = "".join(
                chunk.get("text", "")
                for chunk in raw_response.get("content", [])
                if isinstance(chunk, dict)
            )
            return json.loads(text)
        except (json.JSONDecodeError, TypeError) as exc:
            logger.exception("Failed to parse Anthropic content as JSON")
            raise ClaudeServiceError("Anthropic response was not valid JSON") from exc
