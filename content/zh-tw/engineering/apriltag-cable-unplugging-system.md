---
title: "AprilTag HDMI／電源線拔線系統"
description: "以 AprilTag 與 OpenCV 定位接頭，整合 TM5S、夾爪、TM API 與 ROS 2，支援多種拔線方向與機種。"
featured_image: "/images/projects/default-project.svg"
tags: ["TM5S", "TM Flow", "TM API", "ROS 2", "AprilTag", "OpenCV", "PyQt"]
weight: 8
---

這是一套針對 HDMI 與電源線接頭的實機拔線流程，從影像辨識、姿態估計、手臂接近、夾取到錯誤處理，建立可調整機種與線材設定的控制介面。

## 我的工作

- 使用 AprilTag 辨識接頭位置與姿態，並以 OpenCV 處理影像與座標轉換，控制手臂移動至目標並執行拔線。
- 支援背插、側插、下插、電源線及不同機種，單次測試最多辨識 4 個 AprilTag。
- 量測手臂內建相機的穩定辨識範圍，測試極限約為 50 cm、80 pixels。
- 依機台與接頭方向設定手臂姿態及夾取位置，降低手臂撞擊機台的風險。
- 將卡榫／夾取位置移離接頭，改善背插機台無法垂直接近時的拔線限制。

## 系統介面

規劃 PyQt／PyQt6 UI，集中管理機種／線材設定、Tag ID、影像顯示、流程狀態、錯誤處理與機械手臂控制，並將視覺、PLC、夾爪、ROS 2 與流程執行模組分開。
