---
title: "Isaac GR00T N1.7 數位孿生資料處理平台"
description: "整合機器人、相機、夾爪與 Action 資料，輸出可用於 Isaac GR00T N1.7 的訓練資料。"
featured_image: "/images/projects/default-project.svg"
tags: ["Isaac Sim", "ROS 2", "HDF5", "RGB / Depth", "Robot State", "Action"]
weight: 6
---

此平台負責整理虛擬／真實機器人任務中的多源資料，將資料同步、品質檢查、任務分段與格式轉換串成可重複執行的處理流程，作為 Isaac GR00T N1.7 訓練與推論測試的資料基礎。

## 資料內容

- 機器人關節狀態、末端位置與姿態。
- 夾爪狀態、相機 RGB／Depth 影像與控制 Action。
- 虛擬與真實環境的任務、場景及錄製資訊。

## 我的工作

- 建立資料同步、品質檢查、任務分段、影像前處理與 HDF5 輸出流程。
- 將資料格式與 Action 定義對齊 Isaac GR00T N1.7 Model 的訓練需求。
- 處理 Rotation 6D、ABSOLUTE／RELATIVE Action 及 Base／Tool Frame 差異。
- 支援不同任務與場景的資料蒐集，銜接後續模型訓練、推論測試與虛實環境驗證。
