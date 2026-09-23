---
title: "YOLO OBB 視覺導引 HDMI 插線系統"
description: "以 YOLO OBB 與視覺伺服控制 TM5S，完成 HDMI 孔定位、姿態對位與自動插線。"
featured_image: "/images/projects/default-project.svg"
tags: ["TM5S", "TM Flow", "TM API", "ROS 2", "YOLO OBB", "OpenCV"]
weight: 4
---

這是一套將物件辨識、OpenCV 相機影像處理、相機幾何與機械手臂控制整合在一起的 HDMI 插線流程，重點在於讓末端相機能根據 YOLO OBB 影像結果逐步完成對位，再執行穩定的插線動作。

## 我的工作

- 使用 YOLO OBB 辨識 HDMI 孔中心位置與旋轉姿態，並以 OpenCV 處理影像、相機內參與座標幾何。
- 控制 TM5S 末端相機進行平移、旋轉與多軸同步對位。
- 依相機內參、主點偏移、焦距、辨識框尺寸與 HDMI 實際尺寸估算相對距離。
- 調整移動距離與旋轉誤差範圍，降低重複調整並改善插線流程。

## 技術重點

- 讀取 EIH Camera API 的焦距、影像尺寸、內參矩陣與畸變係數。
- 將視覺辨識結果轉換為機械手臂可執行的控制目標。
- 串接 TM Flow、TM API 與 ROS 2，完成視覺、控制與流程狀態整合。

## 接觸式插接定位

- 在 HDMI 插線最後接觸階段整合視覺伺服與接觸式定位策略。
- 已於真機驗證，完成最後插接定位流程的整合。

## 實機驗證

- 整體插線流程在 10 次測試中由 70% 基準達到 90% 成功率。
