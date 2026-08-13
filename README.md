# 駱忠湧 Daniel Lo 個人網站

這是駱忠湧的雙語個人作品集網站，主要呈現 Robot Control、NVIDIA Isaac GR00T／VLA、Sim-to-Real、Robot Data 與 AI 機器人系統整合經驗。

## 內容結構

- `content/zh-tw/`：繁體中文首頁、經歷、技術棧與專案作品。
- `content/en/`：英文首頁、經歷、技術棧與專案作品。
- `content/*/engineering/`：專案作品詳細頁，包含近期機器人工作專案與既有軟體／互動系統專案。
- `themes/careercanvas/`：網站使用的 CareerCanvas Hugo theme。

## 2026-08-13 履歷定位更新

- 將首頁 Hero、About、Skills、Experience、Tech Stack 與 Contact 統一調整為機器人控制、GR00T／VLA 與 Sim-to-Real 的職涯定位。
- 將網站頭像與社群分享預覽圖統一使用 `profile-about.jpg`。
- 未設定 Pexels 背景時不再顯示照片來源標籤，避免與個人頭像產生錯誤對應。
- 將 Hero 核心定位改為常駐文字，避免 typewriter 動畫延遲第一眼資訊；並修正 Hugo 渲染後失效的電話連結。
- 修正專案索引在 900px 以下因搜尋欄 flex basis 造成的大面積垂直空白。
- 補上聯絡表單姓名與 Email 欄位的 `autocomplete` 語意，消除 Chrome 表單改善提示。
- 現職經歷改以端到端責任呈現：需求分析、架構、開發、Docker 部署、測試、現場整合與維護。
- 新增並前置 NVIDIA Isaac GR00T N1.7 VLA 訓練／TM5S 真機推論、Quest 2 遙操作，以及 TM5S Sim-to-Real 三個核心專案。
- 新增 Robot Workflow 自動化資料錄製平台與 TM5S Web 遠端控制／監控平台的中英文詳細頁，明確區分兩者用途。
- 保留 YOLO OBB、AprilTag、PatchCore、後端與 Docker 作品於完整專案索引，作為支援機器人整合能力的補充，而非首頁主定位。
- 明確標示 DOPE 僅使用官方資料於 Isaac Sim 驗證，避免與已完成的真機視覺伺服成果混淆。
- 移除未經歷的 UR5 → TM5S 延伸敘述；量化成果只保留已有依據的資料蒐集 3～4 倍與線材插接 70% → 90%（10 次測試）。

## 標準求職履歷

PDF 履歷採一頁式標準求職格式，保留職涯定位、工作經歷、核心技能、學歷與榮譽；完整專案細節、Demo、截圖與驗證資料則保留在個人網站。
版面使用較大的內文字級與較寬鬆的行距，優先維持紙本閱讀性，同時保持中英文 PDF 都是一頁 A4。

- `resume/resume_data.json`：中英文履歷的唯一內容來源。
- `resume/generate_resume.py`：使用 ReportLab 產生中英文 PDF。
- `resume/104-resume-zh-tw.md`：可直接整理至 104 履歷的中文版本。
- `output/pdf/daniel-lo-resume-zh-tw.pdf`：中文一頁履歷。
- `output/pdf/daniel-lo-resume-en.pdf`：英文一頁履歷。

重新產生與測試 PDF：

```bash
./resume/build.sh
```

建置與測試固定在 Docker container 中執行，會檢查兩份 PDF 是否為單頁、必要欄位是否存在，以及作品集型內容是否已移出 PDF。

## 已知限制

- GR00T 與遙操作任務仍在持續穩定性驗證，尚未公開未正式統計的成功率、延遲或長時間運行數字。
- 工作專案圖片可能包含公司內部資訊，公開前需另外完成敏感資訊檢查與裁切；目前使用通用專案圖，避免意外揭露。

## 預覽與建置

本專案固定使用 Hugo Extended 0.152.1，開發與測試優先在 Docker 中執行。

本機預覽：

```bash
docker run --rm -p 1313:1313 \
  -v "$PWD:/src" -w /src \
  hugomods/hugo:exts-0.152.1 \
  server --bind 0.0.0.0 --baseURL http://localhost:1313
```

正式建置：

```bash
docker run --rm \
  -v "$PWD:/src" -w /src \
  hugomods/hugo:exts-0.152.1 \
  --gc --minify
```

GitHub Actions 會在推送至 `main` 後執行建置並部署至 GitHub Pages。

中英文 PDF 履歷來源檔案：

- `output/pdf/daniel-lo-resume-zh-tw.pdf`
- `output/pdf/daniel-lo-resume-en.pdf`
