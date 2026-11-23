# 作業繳交說明｜把你的工作拆成 AI 能做的流程

**學校：**［請填］　**學號：**［請填］　**系級：**［請填］　**姓名：**［請填］

## 1. 主題與簡介
「AI Agents 是什麼？」：用官方文件整理成 LLM Wiki，對用過 ChatGPT 的大學生介紹 Agent 定義、組件、Workflow 差異、工具、記憶、應用與風險。

## 2. Wiki 成果
本機 Wiki 索引：[`wiki/index.md`](../wiki/index.md)。五篇官方來源整理：[`raw/`](../raw/)；五篇主題條目：[`wiki/`](../wiki/)；逐頁來源對照：[`wiki/slide_source_matrix.md`](../wiki/slide_source_matrix.md)。**未公開部署，不應冒稱有公開網址**。

## 3. HTML 教學簡報
[`slides/ai_agents_intro.html`](../slides/ai_agents_intro.html)，共 12 頁，左右鍵／按鈕切換、每頁引用來源、部分頁有概念圖。

## 4. Graph / Loop 設計
[`reports/workflow.md`](workflow.md)；[`AGENTS.md`](../AGENTS.md)。包含關卡分工、錯誤退回最近節點、最多三輪與資料不足停止。

## 5. 實際執行與檢查紀錄
- 第一階段：[`reports/stage1_report.md`](stage1_report.md)，S01–S02 補強與檢查。
- 第二階段：[`reports/stage2_report.md`](stage2_report.md)，S03–S05 來源查核、更新、靜態／瀏覽器驗證。
- 靜態檢查：[`reports/final_static_checks.md`](final_static_checks.md)，可用 `python3 scripts/check_final.py` 重跑。

## 6. 反思
**最容易出錯的節點：**來源連結及頁面主張對應。S03 的舊文件網址已重新導向，若不先查驗來源，簡報仍能開啟，但引用將不精確。

**檢查往前移到哪裡：**先查原文與章節，再寫 Wiki；生成簡報前先建立逐頁引用表；最後程式檢查 HTML 網址是否等於 raw 的來源。

**是否修正 Graph：**修正，將「來源網址一致性關卡」移到簡報產生之前，並在最後加入雙向對照檢查。原先發現錯誤可能重做整份 HTML，現在只需要修改 S03 的來源與相關引用頁。

## 尚需本人完成
請在電腦開啟簡報確認投影顯示與互動；填寫個人欄位，若老師要求公開網址請自行部署 GitHub Pages；若老師要求真正的「獨立 AI 審查」，須使用新的獨立對話提供資料和簡報再保留審查紀錄。未在此環境中產生 Git commit。
