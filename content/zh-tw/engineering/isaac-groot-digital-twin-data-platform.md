---
title: "NVIDIA Isaac GR00T N1.7：VLA Policy 訓練與真實機器人推論"
description: "完成 Robot Data 轉換、GR00T N1.7 模型訓練、Policy Inference 與真實機器人控制整合。"
featured_image: "/images/projects/default-project.svg"
tags: ["NVIDIA Isaac GR00T", "VLA", "Digital Twin Data", "Robot Data", "Policy Inference"]
weight: 1
---

此專案將虛擬與真實環境的 Robot Data 串接到 NVIDIA Isaac GR00T N1.7 的資料轉換、模型訓練、Policy Inference 與真實機器人執行流程。我主要負責機械手臂控制與整體系統整合。

## 專案範圍與責任

- 完成資料轉換、模型訓練、模型推論與真實機器人測試的端到端流程。
- 主要負責 Robot Control、Policy Service 串接與整體推論流程整合。
- 透過 ROS 2、WebSocket 與資料錄製系統整合機器人控制與自動化工作流程。

## 端到端資料與推論流程

1. 整理虛擬與真實環境的 Robot Data，建立可用於訓練與推論的資料流程。
2. 將 Robot Data 轉成 GR00T N1.7 訓練格式，再進行模型訓練與 Policy Inference。
3. 由 Policy Service 串接模型輸出與機器人控制，完成真實機器人測試。

## 工程重點

- 建立資料、模型服務與控制命令之間清楚的介面，支援跨系統整合。
- 將模型推論與實機輸出拆成可檢查的服務邊界，完成虛擬與真實環境的驗證流程。
