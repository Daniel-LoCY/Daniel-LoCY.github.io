---
title: "Home Assistant／ESPHome IoT 自架 Stack"
description: "以 Docker 部署 Home Assistant、ESPHome、MQTT 與設定一致性工具的 IoT 平台。"
featured_image: "/images/projects/default-project.svg"
tags: ["Docker", "Home Assistant", "ESPHome", "MQTT", "ESP32", "Python"]
weight: 36
---

這是一套以 Docker 管理的智慧家庭與 IoT 環境，將 Home Assistant、ESPHome 與 Mosquitto MQTT Broker 組成可持續運行的服務 Stack。

## 系統組成

- Home Assistant 負責裝置整合、自動化與狀態管理。
- ESPHome 負責 ESP 裝置的設定、編譯與管理。
- Mosquitto 提供 MQTT 訊息交換，銜接感測器與自動化流程。
- Compose 使用持久化 bind mount 保存 HA、ESPHome 與 MQTT 的設定、資料及 log。

## 穩定性設計

- 以 host network 支援區域網路探索與需要同網段通訊的 IoT 情境。
- 撰寫 `ha_esphome_config_guard.py`，持續檢查 Home Assistant 的 ESPHome config entry。
- 發現裝置 host／port 漂移時，自動校正設定，並以 restart cooldown 降低反覆重啟風險。
- 將設定備份、容器啟動、語法檢查與常見排錯流程整理成可重建的操作文件。

## 我的工程重點

- 處理容器、區域網路、裝置服務與持久化設定之間的邊界。
- 將實際運行中可能發生的 IP／port 漂移轉成可觀測、可恢復的檢查流程。
- 讓 IoT 自動化不只停留在單次展示，而是具備重建與維運能力。

## 展示範圍

這是私有硬體與家庭服務環境，網站僅展示系統設計與工程方法，不公開裝置識別資訊、內網位址、憑證或自動化中的個人資料。
