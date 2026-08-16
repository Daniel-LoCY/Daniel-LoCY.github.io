---
title: "Robot Control 與模擬／真實環境驗證平台"
description: "整合 Isaac Sim／Isaac Lab、ROS 2、MoveIt 2 與 cuMotion 的控制、規劃與真實環境驗證流程。"
featured_image: "/images/projects/default-project.svg"
tags: ["Isaac Sim", "ROS 2", "MoveIt 2", "cuMotion", "OMPL", "TRAC-IK"]
weight: 3
---

這是一套串接 Isaac Sim／Isaac Lab、ROS 2、MoveIt 2 與 cuMotion 的機器人控制與模擬／真實環境驗證流程，用於驗證目標姿態、路徑規劃、碰撞處理、物件操作與真機任務。

## 我的工作

- 完成目標姿態控制、固定物件抓取／放置、碰撞場景與動態碰撞物更新。
- 實作 `Attach Object`，將抓取物件加入路徑規劃碰撞模型，避免後續規劃因夾爪與物件碰撞而失敗。
- 針對 Mesh 無法直接附加的限制，依物件實際姿態建立近似碰撞球體，完成可用的避障方案。
- 建立虛擬與真實機械手臂間的控制與座標轉換流程，完成 Pick-and-Place、線材插拔及 GR00T 相關任務的系統整合。
- 將機械手臂與夾爪參數由硬編碼改為設定檔讀取，降低控制、規劃與實機環境間的重複設定。

## 技術重點

使用 URDF／USD／XRDF、OMPL、TRAC-IK 與 KDL 處理機器人模型、運動學、路徑規劃與碰撞設定；MoveIt 2 與 cuMotion 作為既有規劃工具，主要貢獻在控制層與整體任務流程的整合。
