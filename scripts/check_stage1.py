from pathlib import Path
import re, sys
root=Path(__file__).resolve().parents[1]
checks=[]
def check(name, cond):checks.append((name,bool(cond)))
for sid in ('S01','S02'):
    raw=(root/'raw'/f'{sid}.md').read_text(encoding='utf-8')
    wiki=(root/'wiki'/f'{sid}.md').read_text(encoding='utf-8')
    check(f'{sid} raw 與 Wiki 存在',bool(raw and wiki))
    check(f'{sid} raw 有官方 HTTPS 網址',bool(re.search(r'https://(?:openai\.com|www\.anthropic\.com)/',raw)))
    check(f'{sid} raw 有章節與引用標示','來源位置：' in raw and f'[{sid}]' in raw)
    check(f'{sid} wiki 可連回 raw',f'../raw/{sid}.md' in wiki)
    check(f'{sid} wiki 主張帶來源代碼',wiki.count(f'[{sid}]')>=4)
a=(root/'AGENTS.md').read_text(encoding='utf-8')
check('AGENTS.md 含 Graph、Loop 和三輪停止條件',all(x in a for x in ['Graph','Loop','3 輪','停止']))
check('第一階段索引包含兩篇',all(x in (root/'wiki'/'stage1_index.md').read_text(encoding='utf-8') for x in ['S01','S02']))
check('術語表已建立',(root/'wiki'/'glossary.md').exists())
check('HTML 檔案保留',(root/'slides'/'ai_agents_intro.html').exists())
for name,ok in checks:print(('PASS' if ok else 'FAIL')+' '+name)
print(f'{sum(ok for _,ok in checks)}/{len(checks)} passed')
sys.exit(0 if all(ok for _,ok in checks) else 1)
