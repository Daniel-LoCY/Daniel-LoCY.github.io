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
    PageBreak,
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
        body_size, body_leading = 9.0, 12.0
        summary_size, summary_leading = 9.2, 12.2
        bullet_indent = 11
    else:
        body_size, body_leading = 8.8, 11.8
        summary_size, summary_leading = 9.0, 12.0
        bullet_indent = 12

    return {
        "name": ParagraphStyle(
            "Name", parent=styles["Normal"], fontName="ResumeSans-Bold", fontSize=21.5,
            leading=23, textColor=INK, spaceAfter=1,
        ),
        "title": ParagraphStyle(
            "Title", parent=styles["Normal"], fontName="ResumeSans", fontSize=9.8,
            leading=12.2, textColor=ACCENT, spaceAfter=2,
        ),
        "contact": ParagraphStyle(
            "Contact", parent=styles["Normal"], fontName="ResumeSans", fontSize=7.1,
            leading=9.0, textColor=MUTED, alignment=TA_RIGHT,
        ),
        "section": ParagraphStyle(
            "Section", parent=styles["Normal"], fontName="ResumeSans-Bold", fontSize=12.0,
            leading=14.5, textColor=ACCENT, spaceBefore=5, spaceAfter=3,
        ),
        "summary": ParagraphStyle(
            "Summary", parent=styles["Normal"], fontName="ResumeSans", fontSize=summary_size,
            leading=summary_leading, textColor=INK, spaceAfter=1.5,
        ),
        "company": ParagraphStyle(
            "Company", parent=styles["Normal"], fontName="ResumeSans-Bold", fontSize=9.0,
            leading=11.0, textColor=INK,
        ),
        "role": ParagraphStyle(
            "Role", parent=styles["Normal"], fontName="ResumeSans", fontSize=7.7,
            leading=9.4, textColor=MUTED,
        ),
        "body": ParagraphStyle(
            "Body", parent=styles["Normal"], fontName="ResumeSans", fontSize=body_size,
            leading=body_leading, textColor=INK, leftIndent=bullet_indent,
            firstLineIndent=-bullet_indent, spaceAfter=1.35,
        ),
        "skill_label": ParagraphStyle(
            "SkillLabel", parent=styles["Normal"], fontName="ResumeSans-Bold", fontSize=8.4,
            leading=10.5, textColor=INK,
        ),
        "skill_items": ParagraphStyle(
            "SkillItems", parent=styles["Normal"], fontName="ResumeSans", fontSize=8.4,
            leading=10.5, textColor=INK,
        ),
        "edu": ParagraphStyle(
            "Education", parent=styles["Normal"], fontName="ResumeSans", fontSize=8.4,
            leading=10.5, textColor=INK, leftIndent=10, firstLineIndent=-10, spaceAfter=1.5,
        ),
        "highlight_metric": ParagraphStyle(
            "HighlightMetric", parent=styles["Normal"], fontName="ResumeSans-Bold", fontSize=14.2,
            leading=16.5, textColor=ACCENT,
        ),
        "highlight_label": ParagraphStyle(
            "HighlightLabel", parent=styles["Normal"], fontName="ResumeSans", fontSize=7.8,
            leading=9.6, textColor=MUTED,
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
            ("TOPPADDING", (0, 0), (-1, -1), 4.0),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 3.0),
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
            ("TOPPADDING", (0, 0), (-1, -1), 2.8),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 1.0),
        ]),
    )
    bullets = [p(f"- {bullet}", styles["body"]) for bullet in item["bullets"][lang]]
    return KeepTogether([heading, *bullets, Spacer(1, 3.0 * mm)])


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
        ("TOPPADDING", (0, 0), (-1, -1), 4.3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4.3),
    ]))
    return table


def highlights_block(data, lang, styles, width):
    cells = []
    for item in data["highlights"][lang]:
        cells.append([
            p(item["metric"], styles["highlight_metric"]),
            p(item["label"], styles["highlight_label"]),
        ])
    table = Table([cells], colWidths=[width * 0.5, width * 0.5], hAlign="LEFT")
    table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("BACKGROUND", (0, 0), (-1, -1), PALE),
        ("BOX", (0, 0), (-1, -1), 0.35, RULE),
        ("INNERGRID", (0, 0), (-1, -1), 0.25, colors.HexColor("#D8DCE0")),
        ("LEFTPADDING", (0, 0), (-1, -1), 7),
        ("RIGHTPADDING", (0, 0), (-1, -1), 7),
        ("TOPPADDING", (0, 0), (-1, -1), 4.5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4.5),
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
        leftMargin=17 * mm, rightMargin=17 * mm,
        topMargin=14 * mm, bottomMargin=18 * mm,
        title=(data["contact"]["name_en"] if lang == "en" else data["contact"]["name_zh"]),
        author="Daniel Lo",
    )
    width = doc.width
    story = [
        header(data, lang, styles, width),
        Spacer(1, 3.5 * mm),
        section_heading("Summary" if lang == "en" else "個人簡介", styles["section"], width),
        p(data["summary"][lang], styles["summary"]),
        section_heading("Key Results" if lang == "en" else "核心成果", styles["section"], width),
        highlights_block(data, lang, styles, width),
        section_heading("Experience" if lang == "en" else "工作經歷", styles["section"], width),
    ]
    for item in data["experience"]:
        story.append(experience_block(item, lang, styles, width))
    story.extend([
        section_heading("Skills" if lang == "en" else "核心技能", styles["section"], width),
        skills_block(data, lang, styles, width),
        Spacer(1, 3 * mm),
        section_heading("Education & Honors" if lang == "en" else "學歷與榮譽", styles["section"], width),
    ])
    story.extend(p(f"- {item}", styles["edu"]) for item in data["education"][lang])
    story.append(Spacer(1, 1 * mm))
    doc.build(
        story,
        onFirstPage=lambda canvas, doc: footer(canvas, doc, data, lang),
        onLaterPages=lambda canvas, doc: footer(canvas, doc, data, lang),
    )


def make_v2_styles():
    styles = make_styles("zh")
    styles.update({
        "summary": ParagraphStyle(
            "V2Summary", parent=styles["summary"], fontSize=9.2, leading=12.2,
        ),
        "body": ParagraphStyle(
            "V2Body", parent=styles["body"], fontSize=8.25, leading=10.4,
            leftIndent=11, firstLineIndent=-11, spaceAfter=1.2,
        ),
        "company": ParagraphStyle(
            "V2Company", parent=styles["company"], fontSize=9.2, leading=11.2,
        ),
        "project_title": ParagraphStyle(
            "V2ProjectTitle", parent=styles["company"], fontSize=9.0, leading=11.0,
        ),
        "project_meta": ParagraphStyle(
            "V2ProjectMeta", parent=styles["role"], fontSize=7.5, leading=9.0,
            alignment=TA_RIGHT,
        ),
        "project_body": ParagraphStyle(
            "V2ProjectBody", parent=styles["body"], fontSize=8.0, leading=9.8,
            leftIndent=10, firstLineIndent=-10, spaceAfter=1.0,
        ),
        "skill_label": ParagraphStyle(
            "V2SkillLabel", parent=styles["skill_label"], fontSize=8.0, leading=9.8,
        ),
        "skill_items": ParagraphStyle(
            "V2SkillItems", parent=styles["skill_items"], fontSize=8.0, leading=9.8,
        ),
        "edu": ParagraphStyle(
            "V2Education", parent=styles["edu"], fontSize=8.2, leading=10.0,
        ),
        "small": ParagraphStyle(
            "V2Small", parent=styles["role"], fontSize=8.0, leading=10.0,
            textColor=INK,
        ),
    })
    return styles


def highlights_block_v2(items, styles, width):
    cells = []
    for item in items:
        cells.append([
            p(item["metric"], styles["highlight_metric"]),
            p(item["label"], styles["highlight_label"]),
        ])
    table = Table([cells], colWidths=[width / len(cells)] * len(cells), hAlign="LEFT")
    table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("BACKGROUND", (0, 0), (-1, -1), PALE),
        ("BOX", (0, 0), (-1, -1), 0.35, RULE),
        ("INNERGRID", (0, 0), (-1, -1), 0.25, colors.HexColor("#D8DCE0")),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 4.2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4.2),
    ]))
    return table


def experience_block_v2(item, styles, width):
    heading = Table(
        [[p(f"{item['company']} | {item['role']}", styles["company"]),
          p(f"{item['period']} | {item['location']}", styles["project_meta"])]],
        colWidths=[width * 0.67, width * 0.33],
        style=TableStyle([
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 0),
            ("RIGHTPADDING", (0, 0), (-1, -1), 0),
            ("TOPPADDING", (0, 0), (-1, -1), 2.5),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 1.0),
        ]),
    )
    bullets = [p(f"- {bullet}", styles["body"]) for bullet in item["bullets"]]
    return KeepTogether([heading, *bullets, Spacer(1, 2.5 * mm)])


def project_block_v2(item, styles, width):
    heading = Table(
        [[p(item["title"], styles["project_title"]),
          p(item["stack"], styles["project_meta"])]],
        colWidths=[width * 0.52, width * 0.48],
        style=TableStyle([
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 0),
            ("RIGHTPADDING", (0, 0), (-1, -1), 0),
            ("TOPPADDING", (0, 0), (-1, -1), 2.0),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 0.6),
        ]),
    )
    bullets = [p(f"- {bullet}", styles["project_body"]) for bullet in item["bullets"]]
    return KeepTogether([heading, *bullets, Spacer(1, 1.9 * mm)])


def skills_block_v2(items, styles, width):
    rows = [[p(item["label"], styles["skill_label"]), p(item["items"], styles["skill_items"])] for item in items]
    table = Table(rows, colWidths=[width * 0.28, width * 0.72], hAlign="LEFT")
    table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("BACKGROUND", (0, 0), (-1, -1), PALE),
        ("BOX", (0, 0), (-1, -1), 0.35, RULE),
        ("INNERGRID", (0, 0), (-1, -1), 0.25, colors.HexColor("#D8DCE0")),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 3.5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3.5),
    ]))
    return table


def footer_v2(canvas, doc, data):
    footer(canvas, doc, data, "zh")


def build_resume_v2(data, output_path):
    spec = data["second_zh"]
    styles = make_v2_styles()
    doc = SimpleDocTemplate(
        str(output_path), pagesize=A4,
        leftMargin=16 * mm, rightMargin=16 * mm,
        topMargin=13 * mm, bottomMargin=18 * mm,
        title=f"{data['contact']['name_zh']} | 中文履歷 v2",
        author="Daniel Lo",
    )
    width = doc.width
    story = [
        header(data, "zh", styles, width),
        Spacer(1, 3.0 * mm),
        section_heading("個人簡介", styles["section"], width),
        p(spec["summary"], styles["summary"]),
        section_heading("核心成果", styles["section"], width),
        highlights_block_v2(spec["highlights"], styles, width),
        section_heading("工作經歷", styles["section"], width),
    ]
    for item in spec["experience"]:
        story.append(experience_block_v2(item, styles, width))
    story.append(section_heading("精選專案", styles["section"], width))
    for item in spec["projects"][:3]:
        story.append(project_block_v2(item, styles, width))
    story.extend([
        PageBreak(),
        section_heading("專案補充", styles["section"], width),
    ])
    for item in spec["projects"][3:]:
        story.append(project_block_v2(item, styles, width))
    story.extend([
        section_heading("核心技能", styles["section"], width),
        skills_block_v2(spec["skills"], styles, width),
        section_heading("學歷與榮譽", styles["section"], width),
    ])
    story.extend(p(f"- {item}", styles["edu"]) for item in spec["education"])
    story.extend([
        p(f"- 榮譽：{spec['honors']}", styles["edu"]),
        section_heading("資格、語言與求職方向", styles["section"], width),
        p(f"- 資格：{spec['certifications']}", styles["small"]),
        p(f"- 語言：{spec['language']}", styles["small"]),
        p(f"- {spec['target']}", styles["small"]),
        p(f"- 作品集：{data['contact']['website']}", styles["small"]),
    ])
    doc.build(
        story,
        onFirstPage=lambda canvas, doc: footer_v2(canvas, doc, data),
        onLaterPages=lambda canvas, doc: footer_v2(canvas, doc, data),
    )


def main():
    register_fonts()
    data = load_data()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    build_resume(data, "en", OUTPUT_DIR / "daniel-lo-resume-en.pdf")
    build_resume(data, "zh", OUTPUT_DIR / "daniel-lo-resume-zh-tw.pdf")
    build_resume_v2(data, OUTPUT_DIR / "daniel-lo-resume-zh-tw-v2.pdf")
    print(f"Generated {OUTPUT_DIR / 'daniel-lo-resume-en.pdf'}")
    print(f"Generated {OUTPUT_DIR / 'daniel-lo-resume-zh-tw.pdf'}")
    print(f"Generated {OUTPUT_DIR / 'daniel-lo-resume-zh-tw-v2.pdf'}")


if __name__ == "__main__":
    main()
