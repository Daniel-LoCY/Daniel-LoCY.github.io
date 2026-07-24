---
title: "高鐵自動訂票機器人"
description: "透過 Selenium 模擬使用者行為的自動訂票工具。"
featured_image: "/images/projects/default-project.svg"
tags: ["Python", "Selenium", "Browser Automation"]
weight: 100
---

這是一個將重複訂票流程自動化的瀏覽器控制專案。

## 重點

- 自動完成登入與訂票流程。
- 使用 Selenium 模擬使用者操作。
- 著重於自動化流程的穩定與順序控制。

## Docker 化部署補充

- 以 Docker Compose 將原始訂票專案包裝成可獨立啟動的 Web service。
- 以唯讀掛載保留原始程式，設定檔與瀏覽器擴充套件則分開管理。
- 預設支援 Headless 與 AutoVerify 驗證流程，並提供 `/status.json` 回報最新工作與訂票結果。
