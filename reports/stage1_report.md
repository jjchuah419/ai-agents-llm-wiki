# 第一階段：AGENTS.md 對照與 S01–S02 核對報告

執行日期：2026-11-23

## 專案狀態與真實操作
- 初始 ZIP 已存在 S01–S05 的 raw 摘要、Wiki 條目及 12 頁 HTML。本次**不是從空專案首次 ingest**。
- 本次依使用者已確認九題需求，重寫 `AGENTS.md` 作為新的代理規範；原始 ZIP 保留未動。
- 實際開啟兩篇官方原文：OpenAI「A practical guide to building agents」、Anthropic「Building effective agents」，並核對相應章節。
- 依官方資料重新整理 `raw/S01.md`、`raw/S02.md`，補強 `wiki/S01.md`、`wiki/S02.md`，新增本階段索引與術語表。
- 其他三篇原有 Wiki、12 頁 HTML 暫時保留；其官方原文與簡報語義忠實度**尚未在本階段重新查證**。

## 官方來源定位
- S01： https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/ 章節：What is an agent?、Agent design foundations、When should you build an agent?、Defining tools。
- S02： https://www.anthropic.com/research/building-effective-agents 章節：What are agents?、When (and when not) to use agents、Building blocks, workflows, and agents、Workflow: Prompt chaining。
- Anthropic 文件發表於 2024-12-19，官網有部分工具生態已變更提示；本階段只採用已核對的概念性敘述。

## AGENTS.md 與九項需求差異處理
- 讀者改為「用過 ChatGPT，但不理解 AI Agents 的大學生」。
- 原文核對與章節定位、逐段來源代碼、待查證標示、繁體中文術語表、兩篇→三篇階段化 ingest、10–12 頁、獨立審查與瀏覽器檢查，均納入規範。
- Graph 與局部 Loop 定義完成；最多三輪，來源不足／需人為決定須停下。

## 實際自動檢查（本次重新執行）
執行：`python3 scripts/check_stage1.py`

```text
PASS S01 raw 與 Wiki 存在
PASS S01 raw 有官方 HTTPS 網址
PASS S01 raw 有章節與引用標示
PASS S01 wiki 可連回 raw
PASS S01 wiki 主張帶來源代碼
PASS S02 raw 與 Wiki 存在
PASS S02 raw 有官方 HTTPS 網址
PASS S02 raw 有章節與引用標示
PASS S02 wiki 可連回 raw
PASS S02 wiki 主張帶來源代碼
PASS AGENTS.md 含 Graph、Loop 和三輪停止條件
PASS 第一階段索引包含兩篇
PASS 術語表已建立
PASS HTML 檔案保留
14/14 passed
```

## 檢查限制與後續門檻
- 靜態檢查只證明文件存在、連結及引用格式合理，**不等於完整語義審查**。
- 官方網址已在研究階段開啟，但腳本沒有重新測試遠端連線。
- 簡報仍是既有 12 頁，尚未完成逐頁內容忠實度與人工版面復查。
- 沒有執行獨立 AI 審查、Git commit 或自動三輪 Loop；不能記作 PASS。
- 第二階段：核對 S03–S05，更新整體索引，驗證投影片引用及人工檢視，才可作完整交件判斷。
