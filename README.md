# 駱忠湧 Daniel Lo 個人網站

這是駱忠湧的雙語個人作品集網站，主要呈現 Robot Control、NVIDIA Isaac GR00T／VLA、Digital Twin 資料流程、Robot Data、機器人軟體與 AI 機器人系統整合經驗。

## 2026-09-23 雙軌通用履歷與 PatchCore 同步

- 建立兩條不針對特定公司或職缺的主要履歷：`AI 機器人工程師｜機器人軟體與系統整合` 與 `AI 工程師｜後端與系統整合`，各產出繁中兩頁與英文一頁 PDF。
- 在 `resume/software_profile.json` 與 104 copy-ready 來源中補上後端 API、即時 WebSocket、Docker、AI／電腦視覺與 PatchCore 原型內容。
- 中英文網站的 About、Experience、Skills 與 Core Tech Stack 同步補上 PatchCore、PyQt、ROI 前處理與原型限制；既有 PatchCore 專案頁保留為完整技術說明。
- PatchCore 僅描述開發驗證原型，不宣稱已導入正式檢測或生產流程，也不公開未量測的 AUROC、F1 或推論時間。
- 兩份 104 履歷、LinkedIn 與網站採機器人優先的公開定位；軟體版本使用 `AI 工程師｜後端與系統整合` 作為獨立求職方向。

## 內容結構

- `content/zh-tw/`：繁體中文首頁、經歷、技術棧與專案作品。
- `content/en/`：英文首頁、經歷、技術棧與專案作品。
- `content/*/engineering/`：專案作品詳細頁，包含近期機器人工作專案與既有軟體／互動系統專案。
- `themes/careercanvas/`：網站使用的 CareerCanvas Hugo theme。

## 2026-08-13 履歷定位更新

- 將首頁 Hero、About、Skills、Experience、Tech Stack 與 Contact 統一調整為機器人控制、GR00T／VLA、Digital Twin 資料流程與虛擬／真實環境驗證的職涯定位。
- 將網站頭像與社群分享預覽圖統一使用 `profile-about.jpg`。
- 未設定 Pexels 背景時不再顯示照片來源標籤，避免與個人頭像產生錯誤對應。
- 將 Hero 核心定位改為常駐文字，避免 typewriter 動畫延遲第一眼資訊；並修正 Hugo 渲染後失效的電話連結。
- 修正專案索引在 900px 以下因搜尋欄 flex basis 造成的大面積垂直空白。
- 補上聯絡表單姓名與 Email 欄位的 `autocomplete` 語意，消除 Chrome 表單改善提示。
- 現職經歷改以端到端責任呈現：需求分析、架構、開發、Docker 部署、測試、現場整合與維護。
- 新增並前置 NVIDIA Isaac GR00T N1.7 VLA 訓練／真實機器人推論、Quest 2 遙操作，以及 Robot Control 虛擬／真實環境驗證三個核心專案。
- 新增 Robot Workflow 自動化資料錄製平台與 Web Robot Control 遠端控制／監控平台的中英文詳細頁，明確區分兩者用途。
- 保留 YOLO OBB、AprilTag、PatchCore、後端與 Docker 作品於完整專案索引，作為支援機器人整合能力的補充，而非首頁主定位。
- 明確標示 DOPE 僅使用官方資料於 Isaac Sim 驗證，避免與已完成的真機視覺伺服成果混淆。
- 移除未經歷的 UR5 → TM5S 延伸敘述；量化成果只保留已有依據的模仿學習／GR00T／VLA 訓練資料蒐集 3～4 倍與線材插接 70% → 90%（10 次測試）。

## 2026-08-14 個人網站定位同步

- 將中英文首頁 Hero、About、Skills 與 Contact 收斂為 `AI Robotics Engineer｜Embodied AI`，並保留 Robot Control、VLA／Robot Learning、Perception 與 Digital Twin Data 關鍵字。
- 將中英文 Experience 現職內容由七段長敘述收斂為四項重點，直接呈現交付範圍、控制與模擬、GR00T 真機驗證，以及模仿學習／GR00T／VLA 訓練資料蒐集與線材插接成果。
- 保留已驗證數據：相同時間內模仿學習／GR00T／VLA 訓練資料蒐集量達人工操作的 3～4 倍、線材插接成功率由 70% 提升至 90%（10 次測試）。
- 使用 Hugo Extended 0.152.1 建置成功（繁中 37 頁、英文 35 頁），並以 Chrome 實際檢查本機繁中／英文首頁與 Experience 區塊的渲染結果。
- Docker `hugomods/hugo:exts-0.152.1` 驗證因目前 macOS keychain credential helper 無法在非互動工作階段讀取而未能啟動；本次改以既有版本的本機 Hugo 0.152.1 fallback 驗證，未修改 Docker 設定。
- 中文首頁「查看履歷」指向中文兩頁 v2 PDF；英文首頁「View CV」指向英文一頁 PDF；中英文 Experience 區均提供中英文履歷下載。

## 2026-08-17 公開履歷內容一致化

- 高層級頁面移除 `Sim-to-Real` 與過度集中的特定機器人廠商名稱，改用虛擬／真實環境驗證與 Digital Twin 資料流程描述。
- 明確區分虛擬資料訓練後的真實環境推論，以及真實資料訓練與推論兩條獨立流程。
- 技能區補上 Frontend、Backend、Embedded 與 IoT，並同步更新 104 文案來源與 PDF 履歷。

## 2026-08-18 軟體工程職涯定位擴充

- 中英文首頁 Hero、About、Experience 與 Contact 同步加入 Robotics Software、Systems Integration 與 frontend/backend platform 關鍵字。
- 104 copy-ready 履歷新增機器人軟體工程師、系統整合開發工程師與軟體工程師等目標職稱，並補上全端與後端職類。
- 中英文 PDF 履歷同步更新標題、摘要與 Software & System Integration 技能，現職正式職稱維持 AI Robotics Engineer。

## 2026-08-27 技術歸屬與資料流程說明修正

- 明確區分 YOLO OBB＋OpenCV 的 HDMI 插線，以及 AprilTag＋OpenCV 的 HDMI／電源線拔線。
- 補充模仿學習／GR00T／VLA 訓練資料蒐集由自動化腳本控制與資料錄製系統組成，透過 ROS 2／WebSocket 完成多筆資料全自動錄製，並節省兩名操作人力；不將上述感知技術歸入該流程。
- 同步中英文網站、104、履歷 PDF 與履歷整理草稿。

## 2026-09-22 台積電 Robotics 客製履歷與力導向接觸搜尋

- 在中英文履歷、104 copy-ready 內容與個人網站同步補上已於實體機器人驗證的腕部六軸力／扭矩感測、接觸搜尋與受限範圍螺旋微動，用於處理 HDMI 插線最後接觸階段的殘餘視覺對位誤差。
- 將整體插線流程的 70% → 90%（10 次測試）作為整體結果，不歸因於單一二次定位或力導向階段；力導向階段不宣稱尚未量化的額外成功率，也未加入未確認的低階通訊、阻抗或安全功能經驗。
- 新增 `resume/tsmc_profile.json` 與客製 PDF 生成流程，產生一頁英文與兩頁中文的 TSMC Robotics 版本；共用履歷 PDF 與客製 PDF 均以 Docker 生成並通過 16 項內容、頁數與關鍵字測試。
- 中英文 Hugo 網站同步更新 Experience、About、Skills、Core Tech Stack 與 HDMI 插線專案頁，公開定位只顯示目前所在地「新北，台灣」／「New Taipei, Taiwan」。Hugo Extended 0.152.1 Docker 建置確認中文 37 頁、英文 35 頁。

## 通用求職履歷

機器人版與軟體版各自保留最新的中文兩頁 v2 與英文一頁 PDF。中文版本呈現完整專案脈絡；英文版本維持一頁，方便快速篩選。台積電 Robotics 版本位於 `output/pdf/tsmc/`，與兩條通用履歷分開管理。

- `resume/resume_data.json`：機器人版與網站共用的核心內容來源。
- `resume/software_profile.json`：AI 後端／系統整合版的差異化內容來源。
- `resume/generate_resume.py`：使用 ReportLab 產生兩條通用版本與 TSMC 客製版本。
- `resume/104-resume-zh-tw.md`：104 機器人版 copy-ready 來源。
- `resume/104-resume-software-zh-tw.md`：104 AI 後端／系統整合版 copy-ready 來源。
- `output/pdf/robotics/daniel-lo-resume-robotics-zh-tw-v2.pdf`：機器人版中文兩頁履歷。
- `output/pdf/robotics/daniel-lo-resume-robotics-en.pdf`：機器人版英文一頁履歷。
- `output/pdf/software/daniel-lo-resume-software-zh-tw-v2.pdf`：AI 後端／系統整合版中文兩頁履歷。
- `output/pdf/software/daniel-lo-resume-software-en.pdf`：AI 後端／系統整合版英文一頁履歷。
- `output/pdf/tsmc/daniel-lo-resume-tsmc-zh-tw-v2.pdf`：台積電 Robotics 客製中文兩頁履歷。
- `output/pdf/tsmc/daniel-lo-resume-tsmc-en.pdf`：台積電 Robotics 客製英文一頁履歷。

重新產生與測試 PDF：

```bash
./resume/build.sh
```

建置與測試固定在 Docker container 中執行，會檢查兩條通用履歷與 TSMC 客製履歷的頁數、必要欄位、PatchCore 原型限制與核心成果是否存在，以及低相關舊活動是否未混入 v2。

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

- `output/pdf/robotics/daniel-lo-resume-robotics-zh-tw-v2.pdf`
- `output/pdf/robotics/daniel-lo-resume-robotics-en.pdf`
- `output/pdf/software/daniel-lo-resume-software-zh-tw-v2.pdf`
- `output/pdf/software/daniel-lo-resume-software-en.pdf`
