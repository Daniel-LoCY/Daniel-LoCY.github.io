---
title: "機器人視覺與 PatchCore 異常檢測"
description: "在 Isaac Sim 驗證 DOPE，另完成 RealSense／AprilTag 真機感知流程與尚未導入正式檢測的 PatchCore 原型。"
featured_image: "/images/projects/default-project.svg"
tags: ["RealSense", "DOPE", "OpenCV", "AprilTag", "PatchCore", "ROS 2"]
weight: 9
---

此專案涵蓋機器人抓取所需的 3D 視覺，以及用於品質檢查的影像異常檢測，重點是將模型輸出轉成可追蹤、可測試、可整合的工程流程。

## 機器人視覺

- 使用官方資料在 Isaac Sim 驗證 DOPE 物件姿態預測與 ROS 2 流程，完成影像輸入、姿態輸出與 TF 轉換測試；未將此項寫成真機成果。
- 建立 Eye-in-Hand 與 Eye-to-Hand 手眼標定流程。
- 使用 Checkerboard 與 OpenCV 演算法測試不同標定板，分析平移與旋轉誤差來源。
- 以 RealSense 與 OpenCV 支援影像取得與前處理，並以 AprilTag 定位拔線接頭及進行座標轉換。

## 異常檢測

- 開發 PatchCore API Server 與 PyQt 介面。
- 加入 ROI 擷取、Resize、Crop、Normalize、Clip、模板替換與異常分數判斷。
- 比較正常圖片、反光、小瑕疵及不同場景資料，找出模型誤判情境並調整前處理流程。

PatchCore 目前為開發驗證原型，尚未整合至正式檢測或生產流程，也不公開尚未完成統計的 AUROC、F1 或單張推論時間。
