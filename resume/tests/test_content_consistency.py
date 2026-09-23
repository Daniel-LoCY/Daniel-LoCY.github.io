import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]

PUBLIC_CONTENT_PATHS = tuple(
    ROOT / language / relative_path
    for language in ("content/zh-tw", "content/en")
    for relative_path in (
        "about.md",
        "experience.md",
        "skills.md",
        "technical.md",
        "engineering/isaac-groot-digital-twin-data-platform.md",
        "engineering/isaac-sim-manipulation-planning-platform.md",
        "engineering/robot-workflow-data-platform.md",
        "engineering/vr-imitation-learning-pipeline.md",
        "engineering/yolo-obb-hdmi-insertion-system.md",
        "engineering/robot-vision-anomaly-detection.md",
        "engineering/apriltag-cable-unplugging-system.md",
        "engineering/tm-ros2-web-control-monitoring.md",
    )
)

RESUME_SOURCE_PATHS = (
    ROOT / "resume" / "resume_data.json",
    ROOT / "resume" / "software_profile.json",
    ROOT / "resume" / "tsmc_profile.json",
    ROOT / "resume" / "104-resume-zh-tw.md",
    ROOT / "resume" / "104-resume-software-zh-tw.md",
)

LOW_LEVEL_MARKERS = (
    "pick-and-place",
    "60 hz",
    "30 fps",
    "rotation 6d",
    "timestamp",
    "6.82 mm",
    "0.40°",
    "alvr",
    "steamvr",
    "pyopenxr",
    "two operators",
    "兩名操作人力",
    "螺旋微動",
    "bounded spiral",
    "resize／crop／normalize／clip",
    "resize/crop/normalize/clip",
    "base／tool",
    "base/tool",
    "absolute／relative",
    "absolute/relative",
    "dry run",
        "timesteps",
        "time steps",
        "fps",
        "3～4 倍",
        "3–4×",
        "3-4x",
        "70%",
        "90%",
        "10 次",
        "10-trial",
        "robot state",
        "robot state/action",
        "hand-eye",
        "手眼標定",
        "contact-aware",
        "接觸式插接",
        "force-guided",
        "力導向",
        "roi",
)


class ResumeContentConsistencyTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.resume_data = json.loads(
            (ROOT / "resume" / "resume_data.json").read_text(encoding="utf-8")
        )

    def test_robotics_and_software_profiles_keep_distinct_positioning(self):
        software = json.loads(
            (ROOT / "resume" / "software_profile.json").read_text(encoding="utf-8")
        )
        tsmc = json.loads(
            (ROOT / "resume" / "tsmc_profile.json").read_text(encoding="utf-8")
        )

        self.assertIn("AI Robotics Engineer", self.resume_data["contact"]["title_en"])
        self.assertEqual(software["contact"]["title_en"], "AI Engineer | Backend & Systems Integration")
        self.assertEqual(software["contact"]["title_zh"], "AI 工程師｜後端與系統整合")
        self.assertNotIn("TSMC", software["version"])
        self.assertIn("TSMC", tsmc["version"])

    def test_positive_outcomes_and_patchcore_are_preserved(self):
        source_text = "\n".join(path.read_text(encoding="utf-8") for path in RESUME_SOURCE_PATHS)
        public_text = "\n".join(path.read_text(encoding="utf-8") for path in PUBLIC_CONTENT_PATHS)

        for text in (source_text, public_text):
            self.assertIn("PatchCore", text)
            self.assertRegex(text, r"AI 視覺|異常檢測|anomaly[- ]detection")

    def test_low_level_details_are_removed_from_public_sources(self):
        for path in (*RESUME_SOURCE_PATHS, *PUBLIC_CONTENT_PATHS):
            text = path.read_text(encoding="utf-8").lower()
            for marker in LOW_LEVEL_MARKERS:
                self.assertNotIn(marker.lower(), text, f"Unexpected detail {marker!r} in {path}")

    def test_workflow_pages_keep_the_system_boundary_and_result(self):
        for language, markers in {
            "zh-tw": ("ROS 2", "WebSocket", "自動化", "資料錄製", "AI／VLA"),
            "en": ("ROS 2", "WebSocket", "automated", "recording", "AI / VLA"),
        }.items():
            text = (
                ROOT / "content" / language / "engineering" / "robot-workflow-data-platform.md"
            ).read_text(encoding="utf-8")
            for marker in markers:
                self.assertIn(marker, text)

    def test_insertion_pages_keep_verified_outcome_without_calibration_parameters(self):
        for language, markers in {
            "zh-tw": ("YOLO OBB", "視覺對位", "真機", "OpenCV"),
            "en": ("YOLO OBB", "visual localization", "robot-control", "OpenCV"),
        }.items():
            text = (
                ROOT / "content" / language / "engineering" / "yolo-obb-hdmi-insertion-system.md"
            ).read_text(encoding="utf-8")
            for marker in markers:
                self.assertIn(marker, text)
            self.assertNotIn("6.82", text)
            self.assertNotIn("0.40", text)

    def test_copy_ready_resumes_keep_required_sections_and_current_location(self):
        for path in (
            ROOT / "resume" / "104-resume-zh-tw.md",
            ROOT / "resume" / "104-resume-software-zh-tw.md",
        ):
            text = path.read_text(encoding="utf-8")
            for marker in ("自我介紹", "工作經歷", "專長關鍵字", "精選專案", "學歷", "PatchCore", "目前所在地：新北，台灣"):
                self.assertIn(marker, text)

    def test_public_profile_wording_keeps_current_location_only(self):
        source_text = "\n".join(path.read_text(encoding="utf-8") for path in RESUME_SOURCE_PATHS)
        website_text = "\n".join(
            (ROOT / "content" / language / filename).read_text(encoding="utf-8")
            for language in ("zh-tw", "en")
            for filename in ("about.md", "experience.md", "skills.md", "technical.md")
        )

        self.assertIn("新北，台灣", source_text)
        self.assertIn("New Taipei, Taiwan", source_text)
        self.assertIn("新北，台灣", website_text)
        self.assertIn("New Taipei, Taiwan", website_text)
        for marker in ("新竹", "Hsinchu", "relocate", "relocation"):
            self.assertNotIn(marker.lower(), (source_text + website_text).lower())


if __name__ == "__main__":
    unittest.main()
