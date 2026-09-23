import json
import unittest
from pathlib import Path

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[2]
PDF_DIR = ROOT / "output" / "pdf"


class ResumeOutputTest(unittest.TestCase):
    def _read_pdf(self, filename, expected_pages=1):
        path = PDF_DIR / filename
        self.assertTrue(path.exists(), f"Missing generated PDF: {path}")
        reader = PdfReader(str(path))
        self.assertEqual(len(reader.pages), expected_pages, f"{filename} page count mismatch")
        return "\n".join(page.extract_text() or "" for page in reader.pages)

    def test_english_resume_is_one_page_and_job_focused(self):
        text = self._read_pdf("robotics/daniel-lo-resume-robotics-en.pdf")
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

    def test_software_english_resume_is_one_page_and_backend_focused(self):
        text = self._read_pdf("software/daniel-lo-resume-software-en.pdf")
        for marker in (
            "Daniel Lo",
            "AI Engineer | Backend & Systems Integration",
            "FastAPI",
            "WebSocket",
            "Docker",
            "PatchCore",
            "PyQt",
        ):
            self.assertIn(marker, text)
        self.assertIn("anomaly-score evaluation", " ".join(text.split()))

    def test_104_resume_contains_copy_ready_sections(self):
        path = ROOT / "resume" / "104-resume-zh-tw.md"
        self.assertTrue(path.exists())
        text = path.read_text(encoding="utf-8")
        for marker in ("自我介紹", "工作經歷", "專長關鍵字", "精選專案", "學歷", "作品集", "LinkedIn", "Isaac GR00T", "Digital Twin", "PatchCore"):
            self.assertIn(marker, text)

    def test_software_104_resume_is_copy_ready(self):
        path = ROOT / "resume" / "104-resume-software-zh-tw.md"
        self.assertTrue(path.exists())
        text = path.read_text(encoding="utf-8")
        for marker in (
            "AI 工程師｜後端與系統整合",
            "自我介紹",
            "工作經歷",
            "後端 API",
            "FastAPI",
            "Docker",
            "PatchCore",
            "異常分數分析流程",
        ):
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
        self.assertEqual(experience.count("\n- "), 5)
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

    def test_generic_profile_titles_are_distinct_from_targeted_profile(self):
        software = json.loads((ROOT / "resume" / "software_profile.json").read_text(encoding="utf-8"))
        tsmc = json.loads((ROOT / "resume" / "tsmc_profile.json").read_text(encoding="utf-8"))
        self.assertEqual(software["contact"]["title_en"], "AI Engineer | Backend & Systems Integration")
        self.assertEqual(software["contact"]["title_zh"], "AI 工程師｜後端與系統整合")
        self.assertNotIn("TSMC", software["version"])
        self.assertIn("TSMC", tsmc["version"])

    def test_traditional_chinese_resume_v2_is_two_pages_and_job_focused(self):
        text = self._read_pdf("robotics/daniel-lo-resume-robotics-zh-tw-v2.pdf", expected_pages=2)
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
            "PatchCore",
            "daniel-locy.github.io",
        ):
            self.assertIn(marker, text)
        for removed_detail in ("日本教育旅行", "偏鄉教育", "激發創意"):
            self.assertNotIn(removed_detail, text)

    def test_software_traditional_chinese_resume_v2_is_two_pages(self):
        text = self._read_pdf("software/daniel-lo-resume-software-zh-tw-v2.pdf", expected_pages=2)
        for marker in (
            "駱忠湧",
            "AI 工程師｜後端與系統整合",
            "FastAPI",
            "WebSocket",
            "Docker",
            "PatchCore",
            "PyQt",
            "ROI",
            "異常分數判斷",
        ):
            self.assertIn(marker, text)

    def test_generated_resumes_use_current_location_wording(self):
        output_paths = (
            "robotics/daniel-lo-resume-robotics-en.pdf",
            "robotics/daniel-lo-resume-robotics-zh-tw-v2.pdf",
            "software/daniel-lo-resume-software-en.pdf",
            "software/daniel-lo-resume-software-zh-tw-v2.pdf",
            "tsmc/daniel-lo-resume-tsmc-en.pdf",
            "tsmc/daniel-lo-resume-tsmc-zh-tw-v2.pdf",
        )
        for output_path in output_paths:
            text = self._read_pdf(output_path, expected_pages=2 if "zh-tw" in output_path else 1)
            for forbidden in ("\u88dc\u6551", "\u65b0\u7af9", "Hsin" + "chu", "relo" + "cate", "reco" + "very"):
                self.assertNotIn(forbidden.lower(), text.lower(), output_path)

    def test_only_latest_chinese_resume_is_generated(self):
        self.assertEqual({path.name for path in PDF_DIR.glob("*.pdf")}, set())
        self.assertEqual(
            {path.relative_to(PDF_DIR).as_posix() for path in PDF_DIR.glob("*/*.pdf")},
            {
                "robotics/daniel-lo-resume-robotics-en.pdf",
                "robotics/daniel-lo-resume-robotics-zh-tw-v2.pdf",
                "software/daniel-lo-resume-software-en.pdf",
                "software/daniel-lo-resume-software-zh-tw-v2.pdf",
                "tsmc/daniel-lo-resume-tsmc-en.pdf",
                "tsmc/daniel-lo-resume-tsmc-zh-tw-v2.pdf",
            },
        )

    def test_tsmc_targeted_resumes_are_generated_and_job_focused(self):
        targeted_dir = PDF_DIR / "tsmc"
        english_path = targeted_dir / "daniel-lo-resume-tsmc-en.pdf"
        chinese_path = targeted_dir / "daniel-lo-resume-tsmc-zh-tw-v2.pdf"
        self.assertTrue(english_path.exists(), f"Missing targeted English resume: {english_path}")
        self.assertTrue(chinese_path.exists(), f"Missing targeted Chinese resume: {chinese_path}")

        english_reader = PdfReader(str(english_path))
        chinese_reader = PdfReader(str(chinese_path))
        self.assertEqual(len(english_reader.pages), 1)
        self.assertEqual(len(chinese_reader.pages), 2)

        english_text = "\n".join(page.extract_text() or "" for page in english_reader.pages)
        chinese_text = "\n".join(page.extract_text() or "" for page in chinese_reader.pages)
        for marker in ("force-guided", "six-axis", "GR00T", "Visual Servoing"):
            self.assertIn(marker, english_text)
        for marker in ("力／扭矩", "六軸", "GR00T", "視覺伺服"):
            self.assertIn(marker, chinese_text)


if __name__ == "__main__":
    unittest.main()
