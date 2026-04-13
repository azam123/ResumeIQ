from app.scoring.engine import ResumeScoringEngine


def test_score_with_overlap() -> None:
    engine = ResumeScoringEngine()
    result = engine.calculate_score(
        resume_skills={"python", "fastapi", "sql"},
        job_skills={"python", "fastapi", "aws", "docker"},
        ai_missing_skills=["aws"],
        ai_suggestions=["Add measurable impact bullets"],
    )

    assert 0 <= result.final_score <= 100
    assert result.deterministic_score == 40
