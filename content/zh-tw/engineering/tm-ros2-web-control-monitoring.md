---
title: "TM5S Web 遠端控制與即時監控平台"
description: "以 ROS 2、FastAPI 與 WebSocket 整合 TM5S 操作、Robot Feedback、相機畫面與 MoveIt 軌跡。"
featured_image: "/images/projects/default-project.svg"
tags: ["TM5S", "ROS 2", "FastAPI", "React", "WebSocket"]
weight: 6
---

此平台的目標是降低 TM5S 即時操作與狀態查看的門檻，讓使用者能從瀏覽器遠端控制機械手臂並監看即時資訊。它處理「控制與監控」，不負責另一套 Workflow 平台的自動腳本編排。

## 專案責任與架構

- 由我獨立從零開發，約 1 週完成第一版，並實際連接 1 台 TM5S 使用。
- 前端採 React、TypeScript、Vite 與 Material UI；後端以 FastAPI、`rclpy` 與 WebSocket 串接 ROS 2。
- 使用 Docker 與 Nginx 整理服務邊界與部署方式，將瀏覽器介面和機器人控制程序分開。

## 控制能力

- 關節角度與笛卡兒目標控制。
- TM Script、I/O、事件與常用姿態／動作預設。
- MoveIt 軌跡規劃與執行，並支援直接送出需要的 TM 控制指令。

## 即時監控

- Robot Feedback、關節狀態、Tool Pose、控制與連線狀態。
- 相機串流、FPS、解析度與影像來源資訊。
- ROS 2 節點／Topic 等執行資訊，協助確認控制與資料鏈路是否正常。

平台的核心價值是以較簡單的方式提供遠端控制與監控。目前主要由我本人操作，尚未正式量測控制延遲、節省時間或長時間穩定運行數據，因此不使用推測數字包裝成效。
