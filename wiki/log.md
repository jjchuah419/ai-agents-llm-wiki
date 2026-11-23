# Wiki ingest 紀錄（2026-11-23）

1. 定義讀者、輸出、引用標準與停止條件，形成 `AGENTS.md`。
2. 第一批匯入 S01、S02，建立來源摘要與 Wiki 條目。
3. 檢視涵蓋範圍：基本定義、workflow/agent 差別已具備，但組件與工具執行不足。
4. 補入 S03（循環）、S04（架構）、S05（組件），總計 **5 篇**。
5. 生成 `wiki/index.md` 與 12 張 HTML 教學投影片。
6. 靜態程式檢查結果見 `reports/check_log.md`；網頁視覺溢出仍建議於實際瀏覽器檢視。

提醒：`raw/` 存的是可追溯的改寫摘要及原文連結，不是下載的完整原始網頁。

## 2026-11-23 新增第一階段複核（九題訪談後）
- 原 ZIP 原本已經有五篇摘要與條目；本階段不是新的第一次五篇 ingest。
- 本次查證 S01、S02 官方原文，補強 raw 與 wiki 的兩篇條目；執行 `scripts/check_stage1.py`。
- 詳情及未完成事項見 `reports/stage1_report.md`。

## 2026-11-23 第二階段
- S03 原網址重新導向，改採官方現行 Agents 文件網址，修訂 raw、Wiki 與 HTML 引用。
- S04 核對 Agent architecture overview、Agent tools、Agent memory、Agent design patterns。
- S05 核對 Core architectural components、Orchestrators and language models。
- 補充各段落定位、術語表、逐頁引文對照，重新生成 12 頁 HTML。
- 未擅自宣稱本階段有真實 Git commit 或運行外部模型 API。
