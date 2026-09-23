---
title: "AprilTag HDMI／電源線拔線系統"
description: "以 AprilTag、OpenCV、TM5S 與 ROS 2 建置可配置的接頭定位與機器人任務流程。"
featured_image: "/images/projects/default-project.svg"
tags: ["TM5S", "TM Flow", "TM API", "ROS 2", "AprilTag", "OpenCV", "PyQt"]
weight: 8
---

這是一套針對線材接頭的實機機器人流程，從影像辨識、定位、機器人控制到錯誤處理，建立可調整的任務介面。

## 我的工作

- 使用 AprilTag 與 OpenCV 完成接頭定位、影像處理與座標轉換，並串接機器人控制流程。
- 支援不同機種與線材設定，建立可重複的任務執行與錯誤處理流程。

## 系統介面

以 PyQt／PyQt6 UI 管理機種／線材設定、影像顯示、流程狀態、錯誤處理與機械手臂控制，並將視覺、PLC、夾爪、ROS 2 與流程執行模組分開。
