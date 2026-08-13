import unittest
from pathlib import Path

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[2]
PDF_DIR = ROOT / "output" / "pdf"


class ResumeOutputTest(unittest.TestCase):
    def _read_pdf(self, filename):
        path = PDF_DIR / filename
        self.assertTrue(path.exists(), f"Missing generated PDF: {path}")
        reader = PdfReader(str(path))
        self.assertEqual(len(reader.pages), 1, f"{filename} must be one page")
        return "\n".join(page.extract_text() or "" for page in reader.pages)

    def test_english_resume_is_one_page_and_job_focused(self):
        text = self._read_pdf("daniel-lo-resume-en.pdf")
        for marker in (
            "Daniel Lo",
            "AI Robotics Engineer",
            "Summary",
            "Key Results",
            "Experience",
            "Skills",
            "Education & Honors",
            "Isaac GR00T",
            "3-4x",
            "ROS 2",
            "daniel-locy.github.io",
        ):
            self.assertIn(marker, text)
        for removed_detail in ("Selected Projects", "Robot Workflow", "Verification snapshot", "Evidence:"):
            self.assertNotIn(removed_detail, text)

    def test_traditional_chinese_resume_is_one_page_and_job_focused(self):
        text = self._read_pdf("daniel-lo-resume-zh-tw.pdf")
        for marker in (
            "駱忠湧",
            "AI 機器人工程師",
            "個人簡介",
            "核心成果",
            "工作經歷",
            "核心技能",
            "學歷與榮譽",
            "Isaac GR00T",
            "3～4 倍",
            "ROS 2",
            "daniel-locy.github.io",
        ):
            self.assertIn(marker, text)
        for removed_detail in ("精選專案", "機器人自動化工作流程", "代表專案", "工程驗證摘要", "Evidence:"):
            self.assertNotIn(removed_detail, text)

    def test_104_resume_contains_copy_ready_sections(self):
        path = ROOT / "resume" / "104-resume-zh-tw.md"
        self.assertTrue(path.exists())
        text = path.read_text(encoding="utf-8")
        for marker in ("自我介紹", "工作經歷", "專長關鍵字", "精選專案", "學歷", "作品集", "Isaac GR00T"):
            self.assertIn(marker, text)


if __name__ == "__main__":
    unittest.main()
