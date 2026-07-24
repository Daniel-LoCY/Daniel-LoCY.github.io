# 駱忠湧 Daniel Lo 個人網站

這是駱忠湧的雙語個人作品集網站，內容聚焦於 AI 機器人、電腦視覺、後端系統與跨域整合。

## 內容結構

- `content/zh-tw/`：繁體中文首頁、經歷、技術棧與專案作品。
- `content/en/`：英文首頁、經歷、技術棧與專案作品。
- `content/*/engineering/`：專案作品詳細頁，包含近期機器人工作專案與既有軟體／互動系統專案。
- `themes/careercanvas/`：網站使用的 CareerCanvas Hugo theme。

## 本次內容更新

- 更新 2025/05 至今的 AI 機器人工程工作經歷，整理 Isaac Sim、ROS 2、TM5S、電腦視覺、VR 控制與 GR00T 資料流程。
- 新增 6 個工作代表專案的中英文詳細頁：HDMI 插線、HDMI／電源線拔線、Isaac Sim 路徑規劃、機器人視覺與異常檢測、VR 模仿學習、Isaac GR00T 數位孿生資料平台。
- 新增 3 個 Docker 工作區代表專案的中英文詳細頁：影音與工作流程平台、Home Assistant／ESPHome IoT Stack、多 Stack 自架服務與安全入口；並補充高鐵訂票工具的 Docker 化部署內容。
- 同步補充中英文技術棧中的機器人、視覺與模仿學習工具。

## 預覽與建置

本專案使用 Hugo Extended 0.152.1。可在專案根目錄執行：

```bash
hugo server
```

正式建置：

```bash
hugo --gc --minify
```

GitHub Actions 會在推送至 `main` 後執行建置並部署至 GitHub Pages。
