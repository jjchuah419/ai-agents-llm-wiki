# AI Agents 是什麼？｜LLM Wiki 知識索引

**讀者：**用過 ChatGPT、尚不熟悉 AI Agent 的大學生。**語言：**繁體中文（術語首次出現附英文）。

> 五筆來源皆為官方網站的人工整理摘要；raw/ 並非逐字抓取的原文。2026-11-23 重新查核了 S03–S05，第一階段另核對 S01–S02。

## 五篇來源與條目

| 代碼 | 官方資料 | 知識焦點 | Wiki | 摘要 |
|---|---|---|---|---|
| S01 | [OpenAI：A practical guide to building agents](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/) | Agent 基本組件、工具、指示與安全邊界 | [S01](S01.md) | [raw/S01](../raw/S01.md) |
| S02 | [Anthropic：Building effective agents](https://www.anthropic.com/research/building-effective-agents) | Workflow、Agent、簡單優先與評估 | [S02](S02.md) | [raw/S02](../raw/S02.md) |
| S03 | [LangChain：Agents — Docs by LangChain](https://docs.langchain.com/oss/python/langchain/agents) | 模型、工具、執行循環與 harness | [S03](S03.md) | [raw/S03](../raw/S03.md) |
| S04 | [Google Cloud：Choose your agentic AI architecture components](https://docs.cloud.google.com/architecture/choose-agentic-ai-architecture-components) | 代理架構、工具、記憶與設計模式 | [S04](S04.md) | [raw/S04](../raw/S04.md) |
| S05 | [Microsoft Learn：Agent architecture components](https://learn.microsoft.com/en-us/agents/architecture/components-of-agent-architecture) | 客戶端、基礎設施、協調層、模型與工具 | [S05](S05.md) | [raw/S05](../raw/S05.md) |

## 建議閱讀路徑
1. **認識 Agent 的基本概念**：[S01](S01.md)，以模型、指示與工具理解執行任務的系統。
2. **理解 Workflow vs Agent**：[S02](S02.md)，區分固定流程和動態決策。
3. **理解模型／工具循環**：[S03](S03.md)，觀察工具回傳後如何繼續執行。
4. **認識進階架構與記憶**：[S04](S04.md)，了解哪些組件需要額外設計。
5. **掌握協調器及不同子系統的職責**：[S05](S05.md)。

## 專題對應
- 定義和工具：[S01]、[S03]；組件：[S01]、[S04]、[S05]。
- 工作流程與代理：[S02]、[S03]；記憶：[S04]。
- 應用風險及人工審核：[S01]、[S04]、[S05]。
- 中英術語：[glossary.md](glossary.md)；逐頁引文：[slide_source_matrix.md](slide_source_matrix.md)。

## 資料品質規則
所有實質事實陳述應附代碼。不同文件的定義如果偏向不同抽象層級，保留原意並註明情境；無法判定就標記「待查證」，不能自行補造數據。示意案例不是官方真實案例。
