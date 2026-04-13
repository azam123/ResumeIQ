from dataclasses import dataclass


@dataclass
class ScoreBreakdown:
    deterministic_score: int
    ai_alignment_bonus: int
    final_score: int


class ResumeScoringEngine:
    def calculate_score(
        self,
        resume_skills: set[str],
        job_skills: set[str],
        ai_missing_skills: list[str],
        ai_suggestions: list[str],
    ) -> ScoreBreakdown:
        if not job_skills:
            deterministic_score = 50
        else:
            overlap = len(resume_skills & job_skills)
            deterministic_score = int((overlap / len(job_skills)) * 80)

        penalty = min(len(ai_missing_skills) * 3, 20)
        suggestion_bonus = min(len(ai_suggestions), 5)
        ai_alignment_bonus = max(0, 20 - penalty + suggestion_bonus)

        final = max(0, min(100, deterministic_score + ai_alignment_bonus))
        return ScoreBreakdown(
            deterministic_score=deterministic_score,
            ai_alignment_bonus=ai_alignment_bonus,
            final_score=final,
        )
