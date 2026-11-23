from pathlib import Path
from html.parser import HTMLParser
import json,re,sys
ROOT=Path(__file__).resolve().parents[1]
wiki=ROOT/'wiki'; raw=ROOT/'raw'; slides=ROOT/'slides'; report=ROOT/'reports'
data=json.loads((slides/'slide_data.json').read_text(encoding='utf-8'))
source_ids={f'S{i:02d}' for i in range(1,6)}
class Parser(HTMLParser):
    def __init__(self): super().__init__(); self.sections=0; self.refs=[]; self.links=[]; self.has_script=False
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='section' and 'slide' in a.get('class','').split(): self.sections+=1
        if tag=='a' and 'source' in a.get('class','').split(): self.links.append(a.get('href',''))
        if tag=='script': self.has_script=True
parser=Parser(); page=(slides/'ai_agents_intro.html').read_text(encoding='utf-8'); parser.feed(page)
checks=[
('來源摘要共 5 篇',len(list(raw.glob('S*.md')))==5),
('Wiki 條目共 5 篇',len(list(wiki.glob('S*.md')))==5),
('來源代碼與 Wiki 互相對應',all((raw/f'{x}.md').exists() and (wiki/f'{x}.md').exists() for x in source_ids)),
('簡報在 8–15 頁之間',8<=len(data)<=15),
('HTML 實際頁數符合資料',parser.sections==len(data)),
('每頁至少一筆有效引用',all(s['refs'] and set(s['refs'])<=source_ids for s in data)),
('HTML 可點擊的來源數量一致',len(parser.links)==sum(len(s['refs']) for s in data)),
('出處連結為 https',all(url.startswith('https://') for url in parser.links)),
('未使用無來源百分比',not bool(re.search(r'\d+%', ''.join(s['body']+s['note'] for s in data)))),
('每頁內容長度適合教學',all(len(s['body'])<=130 and len(s['note'])<=100 for s in data)),
('HTML 具有互動程式',parser.has_script and 'keydown' in page and 'next' in page),
('Graph、規則與反思檔存在',all((ROOT/n).exists() for n in ['AGENTS.md','reports/workflow.md','reports/submission.md'])),
]
output='# 自動檢查紀錄\n\n- 日期：2026-11-23\n- 檢查方式：執行 `python3 scripts/check.py`，檢查本機 Wiki 與 HTML。\n- 檢查範圍：檔案完整性、來源代碼、來源連結、頁數、內容長度、HTML 元素。\n\n| 項目 | 結果 |\n|---|---|\n'
for name,ok in checks: output+=f'| {name} | {"PASS" if ok else "FAIL"} |\n'
output+=f'\n**統計：{sum(ok for _,ok in checks)}/{len(checks)} 項通過。**\n\n## 檢查侷限\n- 程式只能驗證連結格式與引用代碼存在，不能保證網頁連結未來持續可連。\n- 僅以字元數近似檢查溢位；CSS 響應式設計仍需用實際瀏覽器測試。\n- 內容忠實度是依來源摘要人工整理，並未執行獨立模型審查。\n- 無證據顯示已執行多次 AI 自動修正，因此不能宣稱跑過三輪。\n'
(report/'check_log.md').write_text(output,encoding='utf-8')
for name,ok in checks: print(('PASS' if ok else 'FAIL'),name)
print(f'{sum(ok for _,ok in checks)}/{len(checks)} passed')
sys.exit(0 if all(ok for _,ok in checks) else 1)
