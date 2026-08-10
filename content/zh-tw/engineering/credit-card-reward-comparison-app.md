---
title: "卡片指南：信用卡回饋比較工具"
description: "以 Flutter、FastAPI 與 PostgreSQL 建置並實際上線的台灣信用卡回饋比較 PWA。"
featured_image: "/images/projects/default-project.svg"
tags: ["Flutter", "Dart", "FastAPI", "PostgreSQL", "PWA", "Docker"]
weight: 25
---

這是一個已實際上線的台灣信用卡回饋比較工具，讓使用者輸入消費金額、店家與支付條件後，依當天日期、卡片、活動規則與官方來源計算預估回饋並排序。

## 線上 Demo

[開啟卡片指南](https://card.lolo-lab.com/)

## 系統組成

- 以 Flutter 共用 Android、iOS 與 Web 介面，Web 版本支援 PWA manifest、service worker、standalone 顯示模式與安裝提示。
- 以 FastAPI 模組化單體後端拆分銀行、信用卡、店家、支付方式、回饋規則、推薦與使用者回報等 domain router。
- 以 PostgreSQL、SQLAlchemy 與 Alembic 管理資料模型、migration 與官方資料同步結果。
- 以 Docker Compose 管理資料庫、API 與 Flutter Web；Web 由 Nginx 以同源 `/api` 代理 backend，正式環境再透過 Cloudflare Tunnel 對外提供服務。

## 產品功能

- 依消費金額、店家、銀行、卡片與支付方式篩選可用回饋。
- 計算基本回饋與具備門檻、期限、登錄或方案條件的活動回饋，並保留現金、點數、哩程等原始回饋單位。
- 卡片與店家活動清單會合併相同活動，同時保留不同卡別的適用條件與官方來源連結。
- 「我的卡片」與「方案設定」使用 `shared_preferences` 保存在目前裝置／瀏覽器，不需要建立帳號。
- 提供關於／回報頁，讓使用者回報資料問題；後端只保存問題描述與非個人化的資料筆數快照。

## 資料可靠性設計

- 資料同步流程要求 HTTPS 官方來源、固定 JSON schema、日期與條件欄位驗證，以及銀行／卡片／支付方式／店家對應檢查。
- LLM Collector 只作為來源擷取與固定格式驗證邊界，不直接把未驗證模型輸出發布成公開回饋。
- 活動詳情與推薦結果都提供官方來源 URL，讓使用者可以回到發卡行或活動主辦方頁面確認條款。

## 我的工程重點

- 在 Flutter 跨平台 UI、FastAPI API contract、PostgreSQL schema 與 Docker production 部署之間維持一致資料流。
- 以模組化單體保留清楚 domain 邊界，同時避免 MVP 過早拆成多個微服務。
- 實作同源 API proxy、PWA、資料來源揭露與免責說明，讓工具可以真的被公開使用而不只停留在 demo。

## 可驗證工程證據

- 2026/08/08 驗證快照：Flutter `analyze`、22 項 Flutter tests、Web release build、SEO contract verifier、Nginx 設定檢查與 HTTP smoke test 通過；backend pytest 40 passed。
- 2026/07/21 資料同步快照：151 張 active 卡片、413 筆 active 官方活動規則，涵蓋 24 家銀行；這是驗證當日的資料快照，不代表目前即時筆數。
- Web 入口具備 canonical、Open Graph、JSON-LD、可索引的產品說明頁、資料來源頁與隱私說明頁，並以 Docker 重建驗證部署結果。

## 產品限制

這個工具提供的是快速回饋估算，不代表銀行最終入帳；活動可能有名額、已使用額度、MCC 判定或最新條款差異。工具不要求登入、不收集卡號與消費紀錄，網站只展示公開產品功能與工程設計。
