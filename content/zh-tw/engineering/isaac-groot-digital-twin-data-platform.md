---
title: "NVIDIA Isaac GR00T N1.7：VLA Policy 訓練與真實機器人推論"
description: "完成 Robot Data 轉換、GR00T N1.7 模型訓練、Policy Inference 與真實機器人控制整合。"
featured_image: "/images/projects/default-project.svg"
tags: ["NVIDIA Isaac GR00T", "VLA", "Digital Twin Data", "Robot Data", "Policy Inference"]
weight: 1
---

此專案將分別來自虛擬與真實環境的 Robot Data，串接到 NVIDIA Isaac GR00T N1.7 的資料轉換、模型訓練、Policy Inference 與真實機器人執行流程。我主要負責機械手臂控制與整體系統整合，不只處理單一資料格式或模型步驟。

本專案分別驗證兩條流程：以虛擬環境資料訓練後在真實環境進行推論，以及以真實環境資料訓練並於真實環境進行推論；兩者不是同步混合資料訓練。

## 專案範圍與責任

- 完成資料轉換、模型訓練、模型推論與真實機器人測試的端到端流程。
- 主要負責 Robot Control、Policy Service 串接、Action 映射與真機推論執行。
- 訓練資料蒐集流程由自動化腳本控制側與資料錄製系統組成；資料錄製平台由其他系統負責，我協助其開發，並透過 ROS 2、WebSocket 等介面將機器人控制與自動化工作流程整合進錄製流程。

## 端到端資料與推論流程

1. 從雙相機影像、Robot State、夾爪狀態與控制 Action 建立 Episode 資料。
2. 影像以 30 FPS 錄製，Robot State／Action 以 60 Hz 取樣，並以 Timestamp 對齊；單一 Episode 約 100～600 個時間步。
3. 將位置、姿態、Rotation 6D 與 Action 定義轉成 GR00T N1.7 訓練格式，再進行訓練與 Checkpoint 推論。
4. 由 Policy Service 接收觀測、回傳模型 Action，經控制層映射成真實機器人可執行指令並完成真機測試。

## 工程重點

- 明確區分影像、Robot State、Action 與時間戳的資料 contract，處理多來源頻率不同造成的同步問題。
- 對齊 ABSOLUTE／RELATIVE Action、Base／Tool Frame 與 Rotation 6D 表示，避免訓練資料和真機控制語意漂移。
- 將模型推論與實機輸出拆成可檢查的服務邊界，保留不送出動作的測試模式，再切換到真機控制。
- 已完成 Pick-and-Place 類型任務的完整串接；目前持續進行 GR00T 相關任務與穩定性驗證，尚未以未統計的成功率作為成果宣稱。
