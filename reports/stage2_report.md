# 第二階段實際執行與驗證報告

- 日期：2026-11-23（臺灣時間）
- 專案基線：第一階段 `AI_Agents_Wiki_Stage1.zip` 的解壓縮副本。
- 改動範圍：`raw/S03–S05.md`、`wiki/S03–S05.md`、索引、術語表、簡報資料及 HTML、品質檢查程式、相關報告。

## 1. S03–S05 官方來源複核

| ID | 官方機構 | 查證章節 | 執行結果 |
|---|---|---|---|
| S03 | LangChain | Agents 頁首及 create_agent 介紹 | 查到舊網址重新導向，改用 https://docs.langchain.com/oss/python/langchain/agents；補充工具循環與 Harness 定義 |
| S04 | Google Cloud | Agent architecture overview、Agent tools、Agent memory、Agent design patterns | 核對組件、工具型式、短期／長期記憶及設計模式 |
| S05 | Microsoft Learn | Core architectural components、Orchestrators and language models | 核對協調器與模型職責、動態與確定性流程 |

本專案的 `raw/` 為原文查閱後改寫的摘要，並非官方網站全文或逐字鏡像。

## 2. 更新 HTML

- 共 12 頁，保留既有教學層次。
- 原第 8 頁改為「記憶與規劃」，加入「記憶並非每個 Agent 的必要功能」提醒。
- 第 4、6、7、10 頁加入簡易概念圖。
- 簡報所有 [S03] 來源連結改成官方現行文件網址。
- 每頁仍附 [S01]–[S05] 的對應來源。

## 3. 自動檢查與實際錯誤修正

- `python3 scripts/check.py`：**12/12 PASS**。
- `python3 scripts/check_final.py`：**18/18 PASS**（先有一次 **17/18 FAIL**，原因是 S01、S02 既有章節標題用「章節與可支持的主張」，與新檢查程式預期欄位格式不同；已調整檢查程式，**沒有篡改既有摘要**）。
- 檢查範圍：來源數、URL 格式與逐頁對應、HTML 頁數、互動程式、圖示節點、Wiki 索引、AGENTS.md Graph/Loop 條件。

## 4. 真正的無頭瀏覽器測試

在 Chromium + Playwright 中以 HTML 原始碼載入頁面（本環境直接開啟 file:// 網址會受到管理員限制，故改用 `page.set_content`，此替代方式仍可檢查排版與互動）：

| 視窗尺寸 | 投影片覆蓋 | DOM 文字／容器溢位檢查 | 左右鍵互動 |
|---|---|---|---|
| 桌面 1440×900 | 12/12 | 0 頁超出容器 | 下一頁正常 |
| 手機 390×844 | 12/12 | 0 頁超出容器 | 下一頁正常 |

`slide_preview.png` 是桌面版瀏覽器截圖。這是一次實際的自動化瀏覽器測試，但仍建議使用者自行開啟 Mac 的 Chrome/Safari 確認呈現。

## 5. 內容審查的界線

已人工對照 S03–S05 的主要描述與官方章節，並修正不精確的網址與記憶表述；沒有另啟獨立 AI 對話進行盲審，**不能聲稱已完成老師要求的獨立 AI 忠實度審查**。官方頁面可能更新，提交前可再次點擊來源確認。

## 6. 工作流程反思

最易出錯的節點是「引用連結與內容的對應」。本次實際發現 S03 的舊 URL 被重新導向，修正點是 Source 節點而不是重寫整份簡報。為防止錯誤再現，新增可執行的 URL 一致性檢查，並將其放進簡報交件關卡。局部修正後自動檢查全部通過。未宣稱實際運行過三輪 AI 自主修正或提交過 Git commit。
