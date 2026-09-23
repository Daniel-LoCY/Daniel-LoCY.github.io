---
title: "機器人視覺與 PatchCore 異常檢測"
description: "在 Isaac Sim 驗證 DOPE，另完成 RealSense／AprilTag 真機感知流程與 PatchCore 異常檢測 API／PyQt 介面。"
featured_image: "/images/projects/default-project.svg"
tags: ["RealSense", "DOPE", "OpenCV", "AprilTag", "PatchCore", "ROS 2"]
weight: 9
---

此專案涵蓋機器人抓取所需的 3D 視覺，以及用於品質檢查的影像異常檢測，重點是將模型輸出轉成可追蹤、可測試、可整合的工程流程。

## 機器人視覺

- 使用官方資料在 Isaac Sim 驗證 DOPE 物件姿態預測與 ROS 2 流程，完成影像輸入、姿態輸出與 TF 轉換測試。
- 建立 Eye-in-Hand 與 Eye-to-Hand 手眼標定流程。
- 使用 Checkerboard 與 OpenCV 演算法測試不同標定板，分析平移與旋轉誤差來源。
- 以 RealSense 與 OpenCV 支援影像取得與前處理，並以 AprilTag 定位拔線接頭及進行座標轉換。

## 異常檢測

- 開發 PatchCore API Server 與 PyQt 介面。
- 加入 ROI、影像前處理、模板替換與異常分數分析。
- 比較正常圖片、反光、小瑕疵及不同場景資料，找出模型誤判情境並調整前處理流程。

PatchCore 實作涵蓋 API Server、PyQt 操作介面、ROI 前處理、模板替換與異常分數分析，形成可追蹤的影像異常檢測流程。
