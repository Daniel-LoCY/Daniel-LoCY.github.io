---
title: "虛擬與真實機械手臂 VR 遙操作與 Digital Twin 資料流程"
description: "以 Quest 2 分別控制 Isaac Sim 與真實機械手臂，並串接 Robot State、影像與 Action 錄製，建立 GR00T／VLA 示範資料。"
featured_image: "/images/projects/default-project.svg"
tags: ["VR Teleoperation", "Digital Twin", "NVIDIA Isaac GR00T", "ROS 2"]
weight: 2
---

這是一套 VR 遙操作與 Digital Twin 資料流程，可分別驅動 Isaac Sim 虛擬機器人與真實機械手臂，再串接資料錄製平台，建立模仿學習或 NVIDIA Isaac GR00T 所需的示範資料。

## 控制流程

- 取得 VR 控制輸入並轉成機器人操作目標，加入速度、工作範圍與操作狀態限制。
- 同一套遙操作概念已串接 Isaac Sim 與真實機械手臂，支援虛擬與實體環境驗證。

## 資料錄製整合

- 將控制 Action 與相機影像、Robot State、末端位姿與夾爪狀態整合到資料錄製平台。
- 支援分別來自虛擬與真實環境的示範資料，作為模仿學習與 GR00T／VLA 訓練輸入。
- 建立可重複的多來源資料錄製與分析流程。

## 驗證狀態

系統已在虛擬與真實環境完成驗證；流程記錄影像、Robot State／Action、末端位姿與夾爪狀態，支援可重複的資料分析。
