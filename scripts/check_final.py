from pathlib import Path
from html.parser import HTMLParser
import json,re,sys
ROOT=Path(__file__).resolve().parents[1]
IDS=[f'S{i:02d}' for i in range(1,6)]
raw=ROOT/'raw';wiki=ROOT/'wiki';slides=ROOT/'slides';reports=ROOT/'reports'
arr=json.loads((slides/'slide_data.json').read_text(encoding='utf-8'))
page=(slides/'ai_agents_intro.html').read_text(encoding='utf-8')
class H(HTMLParser):
 def __init__(self):super().__init__();self.sections=0;self.links=[];self.script=0;self.visual=0
 def handle_starttag(self,t,a):
  a=dict(a);cl=a.get('class','').split()
  if t=='section' and 'slide' in cl:self.sections+=1
  if t=='a' and 'source' in cl:self.links.append(a.get('href'))
  if t=='script':self.script+=1
  if 'visual' in cl:self.visual+=1
h=H();h.feed(page)
links={x:re.search(r'https://[^)\s]+', (raw/f'{x}.md').read_text(encoding='utf-8')).group(0) for x in IDS}
checks=[
 ('五篇 raw 來源存在',all((raw/f'{x}.md').is_file() for x in IDS)),
 ('五篇 wiki 條目存在',all((wiki/f'{x}.md').is_file() for x in IDS)),
 ('每份 raw 都有官方來源網址和章節',all('查閱章節' in (raw/f'{x}.md').read_text(encoding='utf-8') or '來源章節' in (raw/f'{x}.md').read_text(encoding='utf-8') or '原文章節' in (raw/f'{x}.md').read_text(encoding='utf-8') or '章節與可支持的主張' in (raw/f'{x}.md').read_text(encoding='utf-8') for x in IDS)),
 ('所有 Wiki 皆註明來源代碼',all(f'[{x}]' in (wiki/f'{x}.md').read_text(encoding='utf-8') for x in IDS)),
 ('S03 使用現行 LangChain 官方連結',links['S03']=='https://docs.langchain.com/oss/python/langchain/agents'),
 ('來源 URL 為 https',all(v.startswith('https://') for v in links.values())),
 ('Wiki index 提及五篇',all(x in (wiki/'index.md').read_text(encoding='utf-8') for x in IDS)),
 ('術語表存在', (wiki/'glossary.md').is_file()),
 ('逐頁來源矩陣存在', (wiki/'slide_source_matrix.md').is_file()),
 ('HTML 共 12 頁',h.sections==12==len(arr)),
 ('每頁具有效來源',all(s.get('refs') and set(s['refs'])<=set(IDS) for s in arr)),
 ('簡報連結數與引用總數一致',len(h.links)==sum(len(s['refs']) for s in arr)),
 ('簡報全部引用正確官方網址',all(h.links[i]==links[r] for i,r in enumerate(x for s in arr for x in s['refs']))),
 ('具互動操作與 4 個圖示區塊', h.script>=1 and 'keydown' in page and h.visual>=4),
 ('每頁文字長度控制',all(len(s['body'])<170 and len(s['note'])<110 for s in arr)),
 ('HTML 有 lang 與手機 viewport','lang="zh-Hant"' in page and 'name="viewport"' in page),
 ('Graph / Loop 規則完整',all(term in (ROOT/'AGENTS.md').read_text(encoding='utf-8') for term in ['Graph','Loop','最多 3 輪','人工'])),
 ('提交與反思檔案存在',(reports/'submission.md').is_file() and (reports/'workflow.md').is_file()),
]
result='\n'.join(('PASS' if ok else 'FAIL')+' - '+n for n,ok in checks)
summary=f'{sum(ok for _,ok in checks)}/{len(checks)} checks passed'
print(result+'\n'+summary)
(reports/'final_static_checks.md').write_text('# 最終靜態檢查\n\n```text\n'+result+'\n'+summary+'\n```\n\n上述程式檢查只驗證結構、網址一致性與文本長度，不等同於語義忠實度或瀏覽器無溢位。\n',encoding='utf-8')
sys.exit(0 if all(ok for _,ok in checks) else 1)
