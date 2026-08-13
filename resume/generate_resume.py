"""Generate one-page bilingual job-application resumes from resume_data.json."""

from __future__ import annotations

import json
import os
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    KeepTogether,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = Path(__file__).with_name("resume_data.json")
OUTPUT_DIR = ROOT / "output" / "pdf"

PAGE_WIDTH, PAGE_HEIGHT = A4
INK = colors.HexColor("#20252B")
MUTED = colors.HexColor("#626A73")
ACCENT = colors.HexColor("#C84A3A")
RULE = colors.HexColor("#AEB5BC")
PALE = colors.HexColor("#F5F6F7")


def _font_candidates():
    configured = os.environ.get("RESUME_FONT_DIR")
    roots = [Path(configured)] if configured else []
    roots.extend(
        [
            Path("/usr/share/fonts/opentype/noto"),
            Path("/usr/share/fonts/noto-cjk"),
            Path("/usr/share/fonts/truetype/noto"),
            Path("/usr/share/fonts/truetype/wqy"),
        ]
    )
    return roots


def register_fonts():
    regular_names = ("wqy-zenhei.ttc", "wqy-zenhei.ttf", "NotoSansCJK-Regular.ttc", "NotoSansCJKtc-Regular.otf")
    bold_names = ("wqy-zenhei.ttc", "wqy-zenhei.ttf", "NotoSansCJK-Bold.ttc", "NotoSansCJKtc-Bold.otf")
    regular = next((root / name for root in _font_candidates() for name in regular_names if (root / name).exists()), None)
    bold = next((root / name for root in _font_candidates() for name in bold_names if (root / name).exists()), None)
    if regular is None or bold is None:
        searched = ", ".join(str(root) for root in _font_candidates())
        raise FileNotFoundError(f"Noto Sans CJK fonts not found. Searched: {searched}")
    pdfmetrics.registerFont(TTFont("ResumeSans", str(regular), subfontIndex=0))
    pdfmetrics.registerFont(TTFont("ResumeSans-Bold", str(bold), subfontIndex=0))


def load_data():
    return json.loads(DATA_PATH.read_text(encoding="utf-8"))


def make_styles(lang):
    styles = getSampleStyleSheet()
    if lang == "en":
        body_size, body_leading = 8.35, 10.8
        summary_size, summary_leading = 8.45, 10.9
        bullet_indent = 10
    else:
        body_size, body_leading = 8.05, 10.5
        summary_size, summary_leading = 8.2, 10.6
        bullet_indent = 11

    return {
        "name": ParagraphStyle(
            "Name", parent=styles["Normal"], fontName="ResumeSans-Bold", fontSize=20,
            leading=21, textColor=INK, spaceAfter=1,
        ),
        "title": ParagraphStyle(
            "Title", parent=styles["Normal"], fontName="ResumeSans", fontSize=9.2,
            leading=11.5, textColor=ACCENT, spaceAfter=2,
        ),
        "contact": ParagraphStyle(
            "Contact", parent=styles["Normal"], fontName="ResumeSans", fontSize=6.9,
            leading=8.6, textColor=MUTED, alignment=TA_RIGHT,
        ),
        "section": ParagraphStyle(
            "Section", parent=styles["Normal"], fontName="ResumeSans-Bold", fontSize=11.1,
            leading=13.3, textColor=ACCENT, spaceBefore=4, spaceAfter=2.5,
        ),
        "summary": ParagraphStyle(
            "Summary", parent=styles["Normal"], fontName="ResumeSans", fontSize=summary_size,
            leading=summary_leading, textColor=INK, spaceAfter=1.5,
        ),
        "company": ParagraphStyle(
            "Company", parent=styles["Normal"], fontName="ResumeSans-Bold", fontSize=8.5,
            leading=10.3, textColor=INK,
        ),
        "role": ParagraphStyle(
            "Role", parent=styles["Normal"], fontName="ResumeSans", fontSize=7.2,
            leading=8.8, textColor=MUTED,
        ),
        "body": ParagraphStyle(
            "Body", parent=styles["Normal"], fontName="ResumeSans", fontSize=body_size,
            leading=body_leading, textColor=INK, leftIndent=bullet_indent,
            firstLineIndent=-bullet_indent, spaceAfter=1.35,
        ),
        "skill_label": ParagraphStyle(
            "SkillLabel", parent=styles["Normal"], fontName="ResumeSans-Bold", fontSize=7.7,
            leading=9.5, textColor=INK,
        ),
        "skill_items": ParagraphStyle(
            "SkillItems", parent=styles["Normal"], fontName="ResumeSans", fontSize=7.7,
            leading=9.5, textColor=INK,
        ),
        "project_title": ParagraphStyle(
            "ProjectTitle", parent=styles["Normal"], fontName="ResumeSans-Bold", fontSize=7.45,
            leading=9.0, textColor=INK,
        ),
        "project_detail": ParagraphStyle(
            "ProjectDetail", parent=styles["Normal"], fontName="ResumeSans", fontSize=7.35,
            leading=9.0, textColor=INK,
        ),
        "edu": ParagraphStyle(
            "Education", parent=styles["Normal"], fontName="ResumeSans", fontSize=7.7,
            leading=9.6, textColor=INK, leftIndent=9, firstLineIndent=-9, spaceAfter=1.1,
        ),
        "footer": ParagraphStyle(
            "Footer", parent=styles["Normal"], fontName="ResumeSans", fontSize=6.1,
            leading=7.5, textColor=MUTED,
        ),
    }


def p(text, style):
    return Paragraph(text, style)


def section_heading(title, style, width):
    return Table(
        [[p(title, style)]],
        colWidths=[width],
        style=TableStyle([
            ("LINEBELOW", (0, 0), (-1, -1), 0.55, RULE),
            ("LEFTPADDING", (0, 0), (-1, -1), 0),
            ("RIGHTPADDING", (0, 0), (-1, -1), 0),
            ("TOPPADDING", (0, 0), (-1, -1), 2.7),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 2.2),
        ]),
    )


def header(data, lang, styles, width):
    contact = data["contact"]
    name = contact["name_en"] if lang == "en" else contact["name_zh"]
    title = contact["title_en"] if lang == "en" else contact["title_zh"]
    location = contact["location_en"] if lang == "en" else contact["location_zh"]
    left = [p(name, styles["name"]), p(title, styles["title"])]
    right = p(
        f"{contact['email']} | {contact['phone']}<br/>"
        f"{location} | {contact['website']}<br/>"
        f"{contact['github']} | {contact['linkedin']}",
        styles["contact"],
    )
    table = Table([[left, right]], colWidths=[width * 0.62, width * 0.38])
    table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
        ("LINEBELOW", (0, 0), (-1, -1), 1.0, INK),
    ]))
    return table


def experience_block(item, lang, styles, width):
    company = item[f"company_{lang}"]
    role = item[f"role_{lang}"]
    period = item[f"period_{lang}"]
    location = item[f"location_{lang}"]
    heading = Table(
        [[p(f"{company} | {role}", styles["company"]),
          p(f"{period} | {location}", ParagraphStyle(
              "ExperienceMeta", parent=styles["role"], alignment=TA_RIGHT))]],
        colWidths=[width * 0.67, width * 0.33],
        style=TableStyle([
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 0),
            ("RIGHTPADDING", (0, 0), (-1, -1), 0),
            ("TOPPADDING", (0, 0), (-1, -1), 2.1),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 0.8),
        ]),
    )
    bullets = [p(f"- {bullet}", styles["body"]) for bullet in item["bullets"][lang]]
    return KeepTogether([heading, *bullets, Spacer(1, 2.2 * mm)])


def skills_block(data, lang, styles, width):
    rows = []
    for skill in data["skills"][lang]:
        rows.append([p(skill["label"], styles["skill_label"]), p(skill["items"], styles["skill_items"])])
    table = Table(rows, colWidths=[width * 0.27, width * 0.73], hAlign="LEFT")
    table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("BACKGROUND", (0, 0), (-1, -1), PALE),
        ("BOX", (0, 0), (-1, -1), 0.35, RULE),
        ("INNERGRID", (0, 0), (-1, -1), 0.25, colors.HexColor("#D8DCE0")),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 3.2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3.2),
    ]))
    return table


def projects_block(data, lang, styles, width):
    rows = []
    for project in data["projects"][lang]:
        rows.append([
            p(project["title"], styles["project_title"]),
            p(project["detail"], styles["project_detail"]),
        ])
    table = Table(rows, colWidths=[width * 0.30, width * 0.70], hAlign="LEFT")
    table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("BACKGROUND", (0, 0), (-1, -1), colors.white),
        ("LINEBELOW", (0, 0), (-1, -2), 0.25, colors.HexColor("#D8DCE0")),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 1.6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 1.6),
    ]))
    return table


def footer(canvas, doc, data, lang):
    canvas.saveState()
    canvas.setStrokeColor(RULE)
    canvas.setLineWidth(0.35)
    canvas.line(doc.leftMargin, 14 * mm, PAGE_WIDTH - doc.rightMargin, 14 * mm)
    canvas.setFont("ResumeSans", 6.1)
    canvas.setFillColor(MUTED)
    footer_name = data["contact"]["name_en"] if lang == "en" else data["contact"]["name_zh"]
    canvas.drawString(doc.leftMargin, 9.5 * mm, f"{footer_name} | {data['contact']['website']}")
    canvas.drawRightString(PAGE_WIDTH - doc.rightMargin, 9.5 * mm, data["version"])
    canvas.restoreState()


def build_resume(data, lang, output_path):
    styles = make_styles(lang)
    doc = SimpleDocTemplate(
        str(output_path), pagesize=A4,
        leftMargin=16 * mm, rightMargin=16 * mm,
        topMargin=12 * mm, bottomMargin=18 * mm,
        title=(data["contact"]["name_en"] if lang == "en" else data["contact"]["name_zh"]),
        author="Daniel Lo",
    )
    width = doc.width
    story = [
        header(data, lang, styles, width),
        Spacer(1, 2.5 * mm),
        section_heading("Summary" if lang == "en" else "個人簡介", styles["section"], width),
        p(data["summary"][lang], styles["summary"]),
        section_heading("Experience" if lang == "en" else "工作經歷", styles["section"], width),
    ]
    for item in data["experience"]:
        story.append(experience_block(item, lang, styles, width))
    story.extend([
        section_heading("Selected Projects" if lang == "en" else "精選專案", styles["section"], width),
        projects_block(data, lang, styles, width),
        Spacer(1, 1.4 * mm),
        section_heading("Skills" if lang == "en" else "核心技能", styles["section"], width),
        skills_block(data, lang, styles, width),
        Spacer(1, 2 * mm),
        section_heading("Education & Honors" if lang == "en" else "學歷與榮譽", styles["section"], width),
    ])
    story.extend(p(f"- {item}", styles["edu"]) for item in data["education"][lang])
    story.append(Spacer(1, 1 * mm))
    doc.build(
        story,
        onFirstPage=lambda canvas, doc: footer(canvas, doc, data, lang),
        onLaterPages=lambda canvas, doc: footer(canvas, doc, data, lang),
    )


def main():
    register_fonts()
    data = load_data()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    build_resume(data, "en", OUTPUT_DIR / "daniel-lo-resume-en.pdf")
    build_resume(data, "zh", OUTPUT_DIR / "daniel-lo-resume-zh-tw.pdf")
    print(f"Generated {OUTPUT_DIR / 'daniel-lo-resume-en.pdf'}")
    print(f"Generated {OUTPUT_DIR / 'daniel-lo-resume-zh-tw.pdf'}")


if __name__ == "__main__":
    main()
