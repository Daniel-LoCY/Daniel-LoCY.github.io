---
title: "虛擬與真實機械手臂 VR 遙操作與 Digital Twin 資料流程"
description: "以 VR Teleoperation 與 Digital Twin 支援虛擬／真實機械手臂操作與 GR00T／VLA 資料收集。"
featured_image: "/images/projects/default-project.svg"
tags: ["VR Teleoperation", "Digital Twin", "NVIDIA Isaac GR00T", "ROS 2"]
weight: 2
---

這是一套 VR 遙操作與 Digital Twin 資料流程，可分別驅動 Isaac Sim 虛擬機器人與真實機械手臂，再串接資料錄製平台，建立模仿學習或 NVIDIA Isaac GR00T 所需的示範資料。

## 控制流程

- 將 VR 控制輸入轉成機器人操作目標。
- 串接 Isaac Sim 與真實機械手臂，支援虛擬與實體環境驗證。

## 資料錄製整合

- 將遙操作資料與相機影像整合到資料錄製平台。
- 支援虛擬與真實環境的示範資料，作為模仿學習與 GR00T／VLA 訓練輸入。
- 建立可重複的多來源資料錄製流程。

## 驗證狀態

系統已在虛擬與真實環境完成驗證，支援可重複的資料收集與分析。
