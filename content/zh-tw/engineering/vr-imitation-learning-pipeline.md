---
title: "Quest 2 遙操作與 VLA 模仿學習資料流程"
description: "以 Quest 2 控制 Isaac Sim 與 TM5S，並串接 Robot State、影像與 Action 錄製，建立 GR00T／VLA 示範資料。"
featured_image: "/images/projects/default-project.svg"
tags: ["Quest 2", "PyOpenXR", "Rotation 6D", "NVIDIA Isaac GR00T", "ROS 2"]
weight: 2
---

這是一套用 Quest 2 VR 手把遙操作機械手臂的控制系統，可驅動 Isaac Sim 虛擬機器人與 TM5S 真機，再串接外部資料錄製平台，建立模仿學習或 NVIDIA Isaac GR00T 所需的示範資料。

## 控制流程

- 以 Quest 2、ALVR、SteamVR 與 PyOpenXR 取得手把姿態和按鍵狀態。
- 將 VR 座標轉成機器人末端目標，以 60 Hz 更新控制，並加入速度、工作範圍與操作狀態限制。
- 同一套遙操作概念已實際串接 Isaac Sim 與 TM5S，完成 Pick-and-Place 測試。

## 資料錄製整合

- 將控制 Action 與相機影像、Robot State、末端位姿、夾爪狀態整合到資料錄製平台。
- 支援虛擬與真實環境的示範資料，作為模仿學習與 GR00T／VLA 訓練輸入。
- 影像錄製為 30 FPS，Robot State／Action 為 60 Hz，使用 Timestamp 進行多來源資料對齊。

## 驗證狀態

系統已由約 5 人實際操作或測試，並在虛擬與真實環境完成 Pick-and-Place；尚未進行正式延遲與任務成功率統計，因此不將主觀操作感受寫成量化結果。
