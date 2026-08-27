---
title: "Robot Workflow 自動化與資料錄製整合平台"
description: "由自動化腳本控制與資料錄製系統組成，透過 ROS 2、WebSocket 等介面完成模仿學習／GR00T／VLA 訓練資料的全自動蒐集；相同時間內資料量達人工操作的 3～4 倍，並節省兩名操作人力。"
featured_image: "/images/projects/default-project.svg"
tags: ["Robot Workflow", "ROS 2", "WebSocket", "React Flow", "FastAPI", "Docker"]
weight: 5
---

此流程由兩個相互協作的部分組成：一套執行自動化腳本、控制機械手臂與任務流程的 Workflow 系統，以及一套記錄動作、影像、Robot State／Action 與 Timestamp 的資料錄製系統。兩者透過 ROS 2、WebSocket 等介面交換控制、狀態與錄製事件，完成多筆模仿學習／GR00T／VLA 訓練資料的全自動錄製；與另一套著重即時操作的 Web 控制／監控平台用途不同。

## 專案責任與規模

- 由我獨立從零開發，約 4 週完成第一版可用系統。
- 負責需求分析、架構、前後端、Robot Control 串接、Docker 部署、測試與後續維護。
- 資料錄製平台是既有的外部系統；我協助其開發，並負責自動化 Workflow、機器人控制、錄製狀態與跨系統介面的整合。

## 系統設計

- 自動化控制側以 Next.js、React Flow 建立圖形化編排介面，執行腳本並將動作、條件、等待、重試與場景重置組成任務配置。
- 資料錄製側記錄動作、影像、Robot State／Action 與 Timestamp，提供可用於模仿學習／GR00T／VLA 的多筆 Episode 資料。
- 透過 ROS 2、FastAPI、WebSocket 等介面交換機器人控制、流程狀態與錄製事件；完成一次配置後即可全自動執行。
- 執行期間可暫停、停止與重試，介面會同步顯示目前節點、狀態、錯誤與已儲存資料數量。

## 實際任務與成果

- 已串接四種 Pick-and-Place 任務變體，以及錄製前後的場景重置流程。
- 完成一次任務配置後，後續可全自動執行，不需持續人工介入。
- 在相同時間內，平均資料蒐集量約為人工操作的 3～4 倍，並節省兩名操作人力。
- 錄製資料包含 30 FPS 影像與 60 Hz Robot State／Action；Episode 長度依任務約為 100～600 個時間步。

目前未以任務成功率或累積執行次數作為公開指標；上述效益只使用已實際觀察並確認的資料蒐集倍率。
