import json
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
        for marker in ("自我介紹", "工作經歷", "專長關鍵字", "精選專案", "學歷", "作品集", "LinkedIn", "Isaac GR00T", "Digital Twin"):
            self.assertIn(marker, text)

    def test_104_resume_is_concise_for_hr_screening(self):
        path = ROOT / "resume" / "104-resume-zh-tw.md"
        text = path.read_text(encoding="utf-8")
        self.assertIn(
            "目標職稱：AI 機器人工程師、機器人軟體工程師、機器人控制工程師、"
            "Embodied AI 工程師、系統整合開發工程師、軟體工程師",
            text,
        )
        self.assertIn(
            "目標職類：AI 工程師、軟體工程師、演算法工程師、全端工程師、後端工程師",
            text,
        )

        introduction = text.split("## 自我介紹", 1)[1].split("## 自傳", 1)[0].strip()
        autobiography = text.split("## 自傳", 1)[1].split("## 工作經歷", 1)[0].strip()
        self.assertEqual(len([part for part in introduction.split("\n\n") if part]), 1)
        self.assertEqual(len([part for part in autobiography.split("\n\n") if part]), 1)
        self.assertLessEqual(len(introduction), 180)
        self.assertLessEqual(len(autobiography), 220)

        experience = text.split("### 瑞軒科技股份有限公司", 1)[1].split("### 采威國際", 1)[0]
        self.assertEqual(experience.count("\n- "), 4)
        skills = text.split("## 專長關鍵字", 1)[1].split("## 精選專案", 1)[0]
        self.assertEqual(skills.count("\n- "), 6)
        self.assertIn("Frontend Development", skills)
        self.assertIn("Frontend, Backend & System Integration", skills)
        self.assertIn("Embedded & IoT Development", skills)
        self.assertNotIn("Sim-to-Real", text)

    def test_resume_data_uses_shared_software_positioning(self):
        path = ROOT / "resume" / "resume_data.json"
        data = json.loads(path.read_text(encoding="utf-8"))

        self.assertIn("Robotics Software", data["contact"]["title_en"])
        self.assertIn("機器人軟體", data["contact"]["title_zh"])
        self.assertIn("frontend/backend", data["summary"]["en"])
        self.assertIn("前後端", data["summary"]["zh"])
        self.assertIn("系統整合開發工程師", data["second_zh"]["target"])
        self.assertIn("軟體工程師", data["second_zh"]["target"])

    def test_traditional_chinese_resume_v2_is_two_pages_and_job_focused(self):
        path = PDF_DIR / "daniel-lo-resume-zh-tw-v2.pdf"
        self.assertTrue(path.exists(), f"Missing generated PDF: {path}")
        reader = PdfReader(str(path))
        self.assertEqual(len(reader.pages), 2, "v2 Chinese resume must be two pages")
        text = "\n".join(page.extract_text() or "" for page in reader.pages)
        for marker in (
            "駱忠湧",
            "個人簡介",
            "核心成果",
            "工作經歷",
            "精選專案",
            "核心技能",
            "學歷與榮譽",
            "NVIDIA Isaac GR00T",
            "模仿學習／GR00T／VLA 訓練資料蒐集量",
            "3～4 倍",
            "daniel-locy.github.io",
        ):
            self.assertIn(marker, text)
        for removed_detail in ("日本教育旅行", "偏鄉教育", "激發創意"):
            self.assertNotIn(removed_detail, text)


if __name__ == "__main__":
    unittest.main()
