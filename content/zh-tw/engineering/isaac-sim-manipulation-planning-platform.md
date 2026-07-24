---
title: "Isaac Sim 機器人抓取與路徑規劃平台"
description: "整合 Isaac Sim、ROS 2、MoveIt 2 與 cuMotion 的機器人模擬、避障與夾取平台。"
featured_image: "/images/projects/default-project.svg"
tags: ["Isaac Sim", "ROS 2", "MoveIt 2", "cuMotion", "OMPL", "TRAC-IK"]
weight: 3
---

這是一套以 Isaac Sim 為核心、串接 ROS 2 與 MoveIt 2／cuMotion 的機器人模擬與控制環境，用於驗證目標姿態、路徑規劃、碰撞處理及物件抓取流程。

## 我的工作

- 完成目標姿態控制、固定物件抓取／放置、碰撞場景與動態碰撞物更新。
- 實作 `Attach Object`，將抓取物件加入路徑規劃碰撞模型，避免後續規劃因夾爪與物件碰撞而失敗。
- 針對 Mesh 無法直接附加的限制，依物件實際姿態建立近似碰撞球體，完成可用的避障方案。
- 將 UR5 控制架構延伸至 TM5S，整合 Robotiq 2F-85／2F-140 與 Toyo CHY2B-S80 夾爪。
- 將機械手臂與夾爪參數由硬編碼改為設定檔讀取，降低更換硬體時的修改成本。

## 技術重點

使用 URDF／USD／XRDF、OMPL、TRAC-IK 與 KDL 處理機器人模型、運動學、路徑規劃與碰撞相關設定。
