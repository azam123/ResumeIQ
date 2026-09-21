from dataclasses import dataclass
import re

COMMON_SKILLS = {
    "python",
    "fastapi",
    "sql",
    "postgresql",
    "aws",
    "docker",
    "kubernetes",
    "redis",
    "git",
    "ci/cd",
    "terraform",
    "microservices",
    "rest",
    "graphql",
    "pandas",
    "numpy",
    "machine learning",
    "nlp",
    "llm",
    "prompt engineering",
    "data modeling",
    "linux",
}


@dataclass
class ParsedContent:
    cleaned_text: str
    extracted_skills: set[str]


class ParsingService:
    @staticmethod
    def clean_text(raw_text: str) -> str:
        text = re.sub(r"\s+", " ", raw_text).strip()
        return text

    def extract_skills(self, text: str) -> set[str]:
        lowered = text.lower()
        return {skill for skill in COMMON_SKILLS if skill in lowered}

    def parse(self, raw_text: str) -> ParsedContent:
        cleaned = self.clean_text(raw_text)
        skills = self.extract_skills(cleaned)
        return ParsedContent(cleaned_text=cleaned, extracted_skills=skills)
