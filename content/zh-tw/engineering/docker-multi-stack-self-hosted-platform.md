---
title: "多 Stack Docker 自架服務與安全入口"
description: "以部署腳本、Nginx、Authelia 與 Tailscale 整合多個私有服務的自架平台。"
featured_image: "/images/projects/default-project.svg"
tags: ["Docker", "Nginx", "Authelia", "Tailscale", "n8n", "Portainer"]
weight: 37
---

這個 Docker 工作區把多個自架服務整理成可維運的多 Stack 平台，透過統一部署入口、反向代理與權限檢查，管理從工作流程自動化到個人 Web 工具的服務。

## 平台組成

- 根目錄 `deploy.sh` 與 `Makefile` 統一處理 up、down、restart、build、logs 與 ps。
- Authelia 與 Nginx 組成受保護的服務入口，依路由將請求導向 n8n、Portainer、OXWU、THSRC 與其他內部服務。
- 以 route registry 與產生器集中管理 Nginx 路由，降低多份手寫設定漂移。
- Tailscale 分離公開 Funnel gateway 與私有 Serve listeners，保留不同服務的存取邊界。

## 維運與可靠性

- 支援 dev／prod 模式與指定 Stack／service 的局部操作。
- 啟動前檢查 host port，若預設 port 被占用會自動尋找可用 port，並留下 runtime 設定供後續 compose 使用。
- 部署完成後輸出實際入口與服務狀態，並保留單一 Stack 的 log、restart 與 rollback 操作路徑。
- 將 Home Assistant、影片平台、訂票 Web UI、Portainer、n8n 與 OXWU 等服務納入同一套管理習慣。

## 我的工程重點

- 把容器生命週期、網路入口、驗證、路由與服務狀態拆成可追蹤的責任邊界。
- 以設定檔與腳本降低手動部署錯誤，同時避免把敏感設定硬編碼進公開內容。
- 針對內部服務的公開性、Tailnet 存取與認證流程保留清楚的 fallback 與驗證點。

## 展示範圍

這是私有自架基礎設施，網站展示的是架構與維運能力，不公開實際 hostname、內部 port、帳號、token 或服務資料。
