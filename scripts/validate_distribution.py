from pathlib import Path
import sys, yaml, re
root=Path('.')
errors=[]
manifest=root/'distribution.yaml'
if not manifest.exists(): errors.append('missing distribution.yaml')
else:
    data=yaml.safe_load(manifest.read_text()) or {}
    for k in ['name','version','description','hermes_requires','author','license']:
        if not data.get(k): errors.append(f'missing {k}')
    for p in data.get('distribution_owned',[]):
        if not (root/p).exists(): errors.append(f'distribution_owned path missing: {p}')
    for item in data.get('env_requires',[]):
        for k in ['name','description','required']:
            if k not in item: errors.append(f'env_requires item missing {k}: {item}')
blocked={'.env','auth.json','channel_directory.json'}
blocked_dirs={'memories','sessions','logs','workspace','plans','home','local','mcp-tokens'}
for p in root.rglob('*'):
    rel=p.relative_to(root)
    parts=set(rel.parts)
    if '.git' in parts:
        continue
    if p.name in blocked or parts & blocked_dirs or re.match(r'state\.db',p.name) or p.name.endswith('_cache'):
        errors.append(f'blocked user/private artifact committed: {rel}')
if not (root/'SOUL.md').exists(): errors.append('missing SOUL.md')
for skill in (root/'skills').rglob('SKILL.md') if (root/'skills').exists() else []:
    txt=skill.read_text()
    if not txt.startswith('---') or '\n---\n' not in txt[3:]: errors.append(f'invalid skill frontmatter: {skill}')
if errors:
    print('\n'.join(errors)); sys.exit(1)
print('OK')
