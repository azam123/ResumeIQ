from pathlib import Path

from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer

from app.models.schemas import ATSResume


class PdfExporter:
    def export(self, ats_resume: ATSResume, output_path: Path) -> Path:
        output_path.parent.mkdir(parents=True, exist_ok=True)

        doc = SimpleDocTemplate(str(output_path), pagesize=LETTER)
        styles = getSampleStyleSheet()
        story = []

        name = ats_resume.header.get("name", "Candidate")
        story.append(Paragraph(f"<b>{name}</b>", styles["Title"]))
        story.append(Spacer(1, 12))

        for key in ("email", "phone", "location", "linkedin"):
            value = ats_resume.header.get(key)
            if value:
                story.append(Paragraph(f"<b>{key.title()}:</b> {value}", styles["Normal"]))

        story.append(Spacer(1, 10))
        story.append(Paragraph("<b>Summary</b>", styles["Heading2"]))
        story.append(Paragraph(ats_resume.summary or "N/A", styles["Normal"]))

        story.append(Paragraph("<b>Skills</b>", styles["Heading2"]))
        story.append(Paragraph(", ".join(ats_resume.skills) if ats_resume.skills else "N/A", styles["Normal"]))

        story.append(Paragraph("<b>Experience</b>", styles["Heading2"]))
        for exp in ats_resume.experience:
            title = exp.get("title", "")
            company = exp.get("company", "")
            story.append(Paragraph(f"{title} - {company}", styles["Normal"]))
            for bullet in exp.get("bullets", []):
                story.append(Paragraph(f"• {bullet}", styles["Normal"]))

        story.append(Paragraph("<b>Education</b>", styles["Heading2"]))
        for edu in ats_resume.education:
            story.append(
                Paragraph(f"{edu.get('degree', '')} - {edu.get('institution', '')}", styles["Normal"])
            )

        if ats_resume.certifications:
            story.append(Paragraph("<b>Certifications</b>", styles["Heading2"]))
            for cert in ats_resume.certifications:
                story.append(Paragraph(cert, styles["Normal"]))

        doc.build(story)
        return output_path
