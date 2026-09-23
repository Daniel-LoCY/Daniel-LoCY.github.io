import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


class ResumeContentConsistencyTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.resume_data = json.loads(
            (ROOT / "resume" / "resume_data.json").read_text(encoding="utf-8")
        )

    def _experience_bullets(self, language):
        return self.resume_data["experience"][0]["bullets"][language]

    def _find_text(self, texts, marker, label):
        match = next((text for text in texts if marker in text), None)
        self.assertIsNotNone(match, f"Missing {label}: {marker}")
        return match

    def test_experience_separates_training_collection_from_perception(self):
        cases = {
            "en": {
                "collection_marker": "WebSocket",
                "collection_terms": ("script", "recording", "ROS 2", "WebSocket"),
                "forbidden_in_collection": ("YOLO OBB", "AprilTag", "OpenCV"),
                "insertion_terms": ("YOLO OBB", "OpenCV", "insertion"),
                "unplugging_terms": ("AprilTag", "OpenCV", "unplugging"),
            },
            "zh": {
                "collection_marker": "WebSocket",
                "collection_terms": ("腳本", "錄製系統", "ROS 2", "WebSocket"),
                "forbidden_in_collection": ("YOLO OBB", "AprilTag", "OpenCV"),
                "insertion_terms": ("YOLO OBB", "OpenCV", "插線"),
                "unplugging_terms": ("AprilTag", "OpenCV", "拔線"),
            },
        }

        for language, case in cases.items():
            bullets = self._experience_bullets(language)
            collection = self._find_text(
                bullets, case["collection_marker"], f"{language} training-data collection bullet"
            )
            for term in case["collection_terms"]:
                self.assertIn(term, collection)
            for term in case["forbidden_in_collection"]:
                self.assertNotIn(term, collection)

            insertion = self._find_text(bullets, "YOLO OBB", f"{language} insertion bullet")
            for term in case["insertion_terms"]:
                self.assertIn(term, insertion)

            unplugging = self._find_text(bullets, "AprilTag", f"{language} unplugging bullet")
            for term in case["unplugging_terms"]:
                self.assertIn(term, unplugging)

    def test_automated_collection_mentions_two_saved_operators(self):
        cases = {
            "en": ("two", "operator"),
            "zh": ("兩", "人力"),
        }

        for language, terms in cases.items():
            collection = self._find_text(
                self._experience_bullets(language),
                "WebSocket",
                f"{language} training-data collection bullet",
            )
            for term in terms:
                self.assertIn(term, collection)

    def test_project_summaries_preserve_the_same_task_mapping(self):
        cases = {
            "en": {
                "workflow": ("script", "recording", "ROS 2", "WebSocket", "two operators"),
                "vision": ("YOLO OBB", "OpenCV", "insertion", "AprilTag", "unplugging"),
            },
            "zh": {
                "workflow": ("腳本", "錄製系統", "ROS 2", "WebSocket", "兩名操作人力"),
                "vision": ("YOLO OBB", "OpenCV", "插線", "AprilTag", "拔線"),
            },
        }

        for language, expected in cases.items():
            projects = self.resume_data["projects"][language]
            workflow = self._find_text(
                [project["detail"] for project in projects],
                "WebSocket" if language == "en" else "WebSocket",
                f"{language} workflow project summary",
            )
            for term in expected["workflow"]:
                self.assertIn(term, workflow)
            self.assertNotIn("YOLO OBB", workflow)
            self.assertNotIn("AprilTag", workflow)
            self.assertNotIn("OpenCV", workflow)

            vision = self._find_text(
                [project["detail"] for project in projects],
                "YOLO OBB",
                f"{language} vision project summary",
            )
            for term in expected["vision"]:
                self.assertIn(term, vision)

    def test_public_workflow_pages_describe_two_components_without_perception_tools(self):
        page_paths = (
            ROOT / "content" / "zh-tw" / "engineering" / "robot-workflow-data-platform.md",
            ROOT / "content" / "en" / "engineering" / "robot-workflow-data-platform.md",
        )
        for path in page_paths:
            text = path.read_text(encoding="utf-8")
            self.assertIn("ROS 2", text)
            self.assertIn("WebSocket", text)
            self.assertRegex(text.lower(), r"script|腳本")
            self.assertRegex(text.lower(), r"record|錄製")
            self.assertRegex(text, r"兩名|two operators")
            self.assertNotIn("YOLO OBB", text)
            self.assertNotIn("AprilTag", text)
            self.assertNotIn("OpenCV", text)

    def test_homepage_experience_uses_the_same_task_mapping(self):
        cases = {
            ROOT / "content" / "zh-tw" / "experience.md": {
                "collection_terms": ("腳本", "資料錄製系統", "ROS 2", "WebSocket", "兩名操作人力"),
                "insertion_terms": ("YOLO OBB", "OpenCV", "插線"),
                "unplugging_terms": ("AprilTag", "OpenCV", "拔線"),
            },
            ROOT / "content" / "en" / "experience.md": {
                "collection_terms": ("scripts", "recording system", "ROS 2", "WebSocket", "two operators"),
                "insertion_terms": ("YOLO OBB", "OpenCV", "insertion"),
                "unplugging_terms": ("AprilTag", "OpenCV", "unplugging"),
            },
        }

        for path, expected in cases.items():
            lines = path.read_text(encoding="utf-8").splitlines()
            collection = self._find_text(lines, "WebSocket", f"{path.name} collection bullet")
            for term in expected["collection_terms"]:
                self.assertIn(term, collection)
            for term in ("YOLO OBB", "AprilTag", "OpenCV"):
                self.assertNotIn(term, collection)

            insertion = self._find_text(lines, "YOLO OBB", f"{path.name} insertion bullet")
            for term in expected["insertion_terms"]:
                self.assertIn(term, insertion)

            unplugging = self._find_text(lines, "AprilTag", f"{path.name} unplugging bullet")
            for term in expected["unplugging_terms"]:
                self.assertIn(term, unplugging)

    def test_104_copy_removes_the_old_mixed_workflow_sentence(self):
        text = (ROOT / "resume" / "104-resume-zh-tw.md").read_text(encoding="utf-8")
        self.assertIn("自動化腳本", text)
        self.assertIn("資料錄製系統", text)
        self.assertIn("ROS 2", text)
        self.assertIn("WebSocket", text)
        self.assertIn("節省兩名操作人力", text)
        self.assertIn("YOLO OBB＋OpenCV", text)
        self.assertIn("AprilTag＋OpenCV", text)
        self.assertNotIn("整合 RealSense、YOLO OBB、AprilTag、OpenCV 與 Quest 2 遙操作", text)

    def test_force_guided_insertion_is_explicit_and_positive(self):
        cases = {
            "en": (
                "six-axis force/torque",
                "force-guided contact search",
                "bounded spiral micro-search",
                "physical robot",
            ),
            "zh": (
                "六軸力／扭矩",
                "接觸搜尋",
                "螺旋微動",
                "真機",
            ),
        }

        for language, terms in cases.items():
            bullets = self._experience_bullets(language)
            insertion = self._find_text(
                bullets,
                "force-guided" if language == "en" else "六軸力",
                f"{language} force-guided insertion bullet",
            )
            for term in terms:
                self.assertIn(term, insertion)
            for forbidden in ("impedance", "admittance", "EtherCAT", "CANopen"):
                self.assertNotIn(forbidden.lower(), insertion.lower())

    def test_hdmi_project_pages_include_force_contact_search_and_verified_metric(self):
        paths = {
            "zh": ROOT / "content" / "zh-tw" / "engineering" / "yolo-obb-hdmi-insertion-system.md",
            "en": ROOT / "content" / "en" / "engineering" / "yolo-obb-hdmi-insertion-system.md",
        }
        for language, path in paths.items():
            text = path.read_text(encoding="utf-8")
            if language == "en":
                for term in ("six-axis force/torque", "force-guided contact search", "bounded spiral micro-search", "physical robot", "70%", "90%"):
                    self.assertIn(term, text)
            else:
                for term in ("六軸力／扭矩", "接觸搜尋", "螺旋微動", "真機", "70%", "90%"):
                    self.assertIn(term, text)

    def test_tsmc_profile_keeps_unverified_low_level_terms_out(self):
        path = ROOT / "resume" / "tsmc_profile.json"
        self.assertTrue(path.exists())
        text = path.read_text(encoding="utf-8")
        self.assertIn("force-guided", text)
        self.assertIn("力／扭矩", text)
        for forbidden in ("EtherCAT", "CANopen", "impedance", "admittance", "functional safety"):
            self.assertNotIn(forbidden.lower(), text.lower())

    def test_patchcore_is_present_with_implementation_details(self):
        source_text = (ROOT / "resume" / "resume_data.json").read_text(encoding="utf-8")
        software_text = (ROOT / "resume" / "software_profile.json").read_text(encoding="utf-8")
        copy_ready_text = "\n".join(
            (ROOT / "resume" / name).read_text(encoding="utf-8")
            for name in ("104-resume-zh-tw.md", "104-resume-software-zh-tw.md")
        )
        public_text = "\n".join(
            (ROOT / "content" / language / filename).read_text(encoding="utf-8")
            for language in ("zh-tw", "en")
            for filename in ("about.md", "experience.md", "skills.md", "technical.md")
        )
        project_text = "\n".join(
            (ROOT / "content" / language / "engineering" / "robot-vision-anomaly-detection.md").read_text(encoding="utf-8")
            for language in ("zh-tw", "en")
        )

        for text in (source_text, software_text, copy_ready_text, public_text, project_text):
            self.assertIn("PatchCore", text)
            self.assertRegex(text, r"ROI|異常分數|anomaly[- ]score")
        legacy_phrases = (
            "\u76ee\u524d\u70ba\u958b\u767c\u9a57\u8b49\u539f\u578b",
            "\u5c1a\u672a\u6574\u5408\u81f3\u6b63\u5f0f\u6aa2\u6e2c\u6216\u751f\u7522\u6d41\u7a0b",
            "remains a development prototype",
            "not deployed to a formal inspection or production flow",
        )
        for text in (source_text, software_text, copy_ready_text, public_text, project_text):
            for phrase in legacy_phrases:
                self.assertNotIn(phrase, text.lower())

    def test_current_profile_wording_uses_new_taipei_only(self):
        source_paths = [
            ROOT / "README.md",
            ROOT / "config.toml",
            ROOT / "resume" / "resume_data.json",
            ROOT / "resume" / "software_profile.json",
            ROOT / "resume" / "tsmc_profile.json",
            ROOT / "resume" / "104-resume-zh-tw.md",
            ROOT / "resume" / "104-resume-software-zh-tw.md",
            ROOT / "content" / "zh-tw" / "about.md",
            ROOT / "content" / "zh-tw" / "experience.md",
            ROOT / "content" / "zh-tw" / "skills.md",
            ROOT / "content" / "zh-tw" / "technical.md",
            ROOT / "content" / "zh-tw" / "engineering" / "yolo-obb-hdmi-insertion-system.md",
            ROOT / "content" / "en" / "about.md",
            ROOT / "content" / "en" / "experience.md",
            ROOT / "content" / "en" / "skills.md",
            ROOT / "content" / "en" / "engineering" / "yolo-obb-hdmi-insertion-system.md",
        ]
        text = "\n".join(path.read_text(encoding="utf-8") for path in source_paths)
        for forbidden in (
            "\u88dc\u6551",
            "\u65b0\u7af9",
            "Hsin" + "chu",
            "Open to " + "relo" + "cate",
            "relo" + "cate to " + "Hsin" + "chu",
            "insertion " + "reco" + "very",
            "contact " + "reco" + "very",
            "reco" + "ver insertion",
        ):
            self.assertNotIn(forbidden, text)


if __name__ == "__main__":
    unittest.main()
