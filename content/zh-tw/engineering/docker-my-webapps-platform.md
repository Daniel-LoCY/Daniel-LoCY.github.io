---
title: "Docker 化個人多功能工作台"
description: "以 React、FastAPI 與 Docker 建置的私有影音與工作流程平台。"
featured_image: "/images/projects/default-project.svg"
tags: ["Docker", "React", "FastAPI", "FFmpeg", "yt-dlp", "SQLite"]
weight: 35
---

這是一套以 Docker Compose 部署的個人多功能工作台，將影音下載、媒體處理、文件轉換、資產管理與私有資料功能整合在同一個 Web 入口。

## 系統組成

- 以 React 建立支援深色／淺色主題的 Web UI 與 PWA 入口。
- 以 FastAPI 提供帳號、權限、工作佇列與各功能 API。
- 以 yt-dlp 負責影音來源解析，以 FFmpeg 執行轉檔與媒體處理。
- 以 Docker Compose 拆分前端、後端與檔案瀏覽服務，並支援 dev／prod 兩種啟動模式。

## 功能重點

- 影片下載、播放清單處理、格式轉換、裁切、合併、抽幀、縮圖與速度調整。
- 即時畫面調整與輸出，包含色溫、亮度、對比、飽和、模糊、銳利、去背與浮水印。
- 支援 HLS／DASH 輸出、RTMP／SRT／UDP 推流，以及背景工作佇列與 callback。
- 整合 MarkItDown 文件轉 Markdown、GitHub 圖片資產管理與每帳號 SQLite 財務資料隔離。

## 我的工程重點

- 以帳號 scope 隔離影片工作區與資料，並在 API 邊界處理驗證、權限與一致的錯誤回應。
- 透過服務狀態檢查讓首頁能辨識其他自架服務是否可用。
- 將大型媒體處理放入背景任務，讓 Web API 回應與實際工作執行分離。

## 展示範圍

這是私有自架平台，網站僅展示架構、技術選擇與可公開的功能摘要，不公開內部網址、帳號、檔案或個人財務資料。
