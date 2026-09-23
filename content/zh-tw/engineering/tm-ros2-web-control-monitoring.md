---
title: "TM5S Web 遠端控制與即時監控平台"
description: "以 ROS 2、FastAPI、React 與 WebSocket 建置 TM5S Web 遠端控制與即時監控平台。"
featured_image: "/images/projects/default-project.svg"
tags: ["TM5S", "ROS 2", "FastAPI", "React", "WebSocket"]
weight: 6
---

此平台讓使用者能從瀏覽器遠端控制 TM5S 並查看即時資訊，聚焦於機器人控制、影像與系統監控；自動腳本編排由另一套 Workflow 平台負責。

## 專案責任與架構

- 由我獨立開發並實際連接 TM5S 使用。
- 前端採 React、TypeScript、Vite 與 Material UI；後端以 FastAPI、`rclpy` 與 WebSocket 串接 ROS 2。
- 使用 Docker 與 Nginx 整理服務邊界與部署方式。

## 控制能力

- 支援機械手臂控制、常用動作與控制命令。
- 整合 MoveIt 軌跡規劃與執行流程。

## 即時監控

- 顯示機器人回饋、控制與連線狀態。
- 整合相機串流與 ROS 2 執行資訊，支援日常操作與問題確認。

這套平台將控制命令、相機串流、機器人回饋與 ROS 2 執行資訊整合在同一個操作介面。
