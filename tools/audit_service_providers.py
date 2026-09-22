"""Read-only provider inventory: baseline + active MO2 config overlay, with provenance.

This is a static audit, not an XRay interpreter. Runtime DXML/script-generated jobs
and ambiguous DLTX ordering remain explicitly outside the inventory's guarantee.
"""
from pathlib import Path, PurePosixPath
import argparse, csv, html, json, re

ROLES = {'trader':'trader','mechanic':'tech','tech':'tech','medic':'medic','barman':'barman','guider':'guide','guide':'guide'}
DIALOG_ROLES = {'dm_init_trader':'trader','dm_init_mechanic':'tech','dm_init_medic':'medic','dm_medic_general':'medic','dm_init_batender':'barman'}

def read(p):
    b=p.read_bytes()
    try: return b.decode('utf-8-sig')
    except UnicodeDecodeError: return b.decode('cp1251',errors='replace')

def overlay(root,label,files):
    root=root.resolve()
    if root.is_dir():
        for p in root.rglob('*'):
            if p.is_file() and p.suffix.lower() in ('.ltx','.xml'):
                files[p.relative_to(root).as_posix().lower()]=(p,label)

class Corpus:
    def __init__(self,files):
        self.files,self.cache,self.warnings=files,{},[]
        self.patches={}
        bases=[k for k in files if k.endswith('.ltx') and not PurePosixPath(k).name.startswith('mod_')]
        bydir={}
        for k in bases: bydir.setdefault(str(PurePosixPath(k).parent),[]).append(k)
        for k in files:
            p=PurePosixPath(k)
            if p.suffix!='.ltx' or not p.name.startswith('mod_'): continue
            matches=[b for b in bydir.get(str(p.parent),[]) if p.stem.startswith('mod_'+PurePosixPath(b).stem+'_')]
            if matches:
                target=max(matches,key=len); self.patches.setdefault(target,[]).append(k)

    def include(self,key,parent):
        key=key.replace('\\','/').lower()
        relative=str(PurePosixPath(parent).parent/key)
        return key if key in self.files else relative if relative in self.files else None

    def ltx(self,key,stack=()):
        if key in self.cache: return self.cache[key]
        if key not in self.files or key in stack: return {}
        sections={}
        def apply(path):
            current=None
            for line_no,line in enumerate(read(self.files[path][0]).splitlines(),1):
                line=line.split(';',1)[0].strip()
                inc=re.match(r'#include\s+"([^"]+)"',line)
                if inc:
                    child=self.include(inc[1],path)
                    if child:
                        for name,data in self.ltx(child,stack+(key,)).items():
                            dst=sections.setdefault(name,{'values':{},'parents':[]})
                            dst['values'].update(data['values']); dst['parents']=data['parents'][:]
                    elif '*' not in inc[1]: self.warnings.append(f'missing include: {path}:{line_no}: {inc[1]}')
                    continue
                m=re.match(r'(!?)\[(!?)([^]]+)\]\s*(?::\s*(.*))?',line)
                if m:
                    current=m[3]
                    if m[2]: sections.pop(current,None); current=None; continue
                    dst=sections.setdefault(current,{'values':{},'parents':[]})
                    if m[4]: dst['parents']=[v.strip() for v in m[4].split(',') if v.strip()]
                    continue
                if not current: continue
                if '=' in line:
                    field,value=line.split('=',1)
                    field,value=field.strip(),value.strip()
                    if field.startswith('!'):
                        sections[current]['values'].pop(field[1:],None); continue
                    if field.startswith(('>','<')):
                        op,field=field[0],field[1:]
                        old=sections[current]['values'].get(field,{}).get('value','')
                        items=[v.strip() for v in old.split(',') if v.strip()]
                        change=[v.strip() for v in value.split(',') if v.strip()]
                        items=items+[v for v in change if v not in items] if op=='>' else [v for v in items if v not in change]
                        value=', '.join(items)
                    sections[current]['values'][field]={'value':value,'file':path,'line':line_no}
                elif line.startswith('!'): sections[current]['values'].pop(line[1:].strip(),None)
        apply(key)
        for patch in sorted(self.patches.get(key,[])): apply(patch)
        self.cache[key]=sections
        return sections

    def fields(self,key,section,seen=()):
        if section in seen: return {}
        data=self.ltx(key).get(section)
        if not data: return {}
        values={}
        for parent in data['parents']: values.update(self.fields(key,parent,seen+(section,)))
        values.update(data['values']); return values

    def text(self,key,stack=()):
        if key not in self.files or key in stack: return ''
        def replace(m):
            child=self.include(m[1],key)
            return self.text(child,stack+(key,)) if child else ''
        return re.sub(r'#include\s+"([^"]+)"',replace,read(self.files[key][0]))

    def analyze(self):
        names={}
        for k in self.files:
            if k.startswith('text/rus/') and k.endswith('.xml'):
                for ident,body in re.findall(r'<string\s+id="([^"]+)"[^>]*>(.*?)</string>',read(self.files[k][0]),re.S):
                    m=re.search(r'<text>(.*?)</text>',body,re.S)
                    if m: names[ident]=html.unescape(m[1].strip())
        dialog_roles={k:{v} for k,v in DIALOG_ROLES.items()}
        for k in self.files:
            if not (k.startswith('gameplay/') and k.endswith('.xml')): continue
            xml=re.sub(r'<!--.*?-->','',read(self.files[k][0]),flags=re.S)
            for ident,body in re.findall(r'<dialog\b[^>]*\bid="([^"]+)"[^>]*>(.*?)</dialog>',xml,re.S):
                roles=dialog_roles.setdefault(ident,set())
                if re.search(r'<action>\s*dialogs\.heal_actor_',body): roles.add('medic')
                if re.search(r'<action>\s*dialogs\.npc_is_trader\s*</action>',body): roles.add('trader')
                if re.search(r'<action>\s*dialogs\.upgrade\s*</action>',body): roles.add('tech')
        profiles={}
        registered=self.fields('system.ltx','profiles').get('specific_characters_files',{}).get('value','')
        profile_files={'gameplay/'+name.strip()+'.xml' for name in registered.split(',') if name.strip()}
        for k in self.files:
            if not (k.startswith('gameplay/') and k.endswith('.xml')): continue
            text=re.sub(r'<!--.*?-->','',read(self.files[k][0]),flags=re.S)
            for ident,body in re.findall(r'<specific_character\b[^>]*\bid="([^"]+)"[^>]*>(.*?)</specific_character>',text,re.S):
                dialogs=re.findall(r'<actor_dialog>(.*?)</actor_dialog>',body,re.S)
                roles=set().union(*(dialog_roles.get(d.strip(),set()) for d in dialogs))
                def tag(n):
                    m=re.search('<'+n+r'>(.*?)</'+n+'>',body,re.S); return m[1].strip() if m else ''
                pname=tag('name')
                if ident in profiles: self.warnings.append(f'duplicate profile definition: {ident}: {k}')
                profiles[ident]=dict(character=ident,name=names.get(pname,pname),roles=';'.join(sorted(roles)),
                    community=tag('community'),source=str(self.files[k][0]),provider=self.files[k][1],
                    dialogs=';'.join(d.strip() for d in dialogs),generic=ident.startswith('sim_default_'),
                    registration='declared' if k in profile_files else 'include_or_runtime_unverified')
        profile_by_id=profiles
        def character(n):
            return self.fields('system.ltx',n).get('character_profile',{}).get('value',n)
        jobs=[]
        for k in self.files:
            if '/smart/' not in k or not k.endswith('.ltx') or PurePosixPath(k).name.startswith('mod_'): continue
            smart=PurePosixPath(k).stem
            entries=self.fields(k,'exclusive').copy()
            entries.update({n:v for n,v in self.fields(k,'smart_terrain').items() if re.fullmatch(r'work\d+',n)})
            for work,entry in entries.items():
                path='scripts/'+entry['value'].replace('\\','/').lower()
                section='logic@'+work
                f=self.fields(path,section)
                if not f:
                    self.warnings.append(f'missing job: {k} {section} -> {path}'); continue
                v=lambda name:f.get(name,{}).get('value','')
                suitable,trade,spot=v('suitable'),v('trade'),v('level_spot')
                role=None
                for key,r in [('trader','trader'),('mechanic','tech'),('medic','medic'),('barman','barman')]:
                    if 'check_npc_'+key in suitable: role=r; break
                role=role or ROLES.get(spot)
                tail=re.search(r'([a-z]+)$',section.lower())
                role=role or (ROLES.get(tail[1]) if tail else None)
                npc_names=re.findall(r'check_npc_name\s*\(([^)]+)\)',suitable)
                npc_names=[n for group in npc_names for n in re.split(r'[: ,]+',group) if n]
                if not role and trade:
                    for token,r in [('mechanic','tech'),('tech','tech'),('medic','medic'),('barman','barman'),('trader','trader')]:
                        if token in section: role=r; break
                if not role:
                    for n in npc_names:
                        pr=profile_by_id.get(character(n))
                        if pr:
                            rr=pr['roles'].split(';'); role=next((r for r in ('tech','medic','barman','trader') if r in rr),None)
                if not role or 'beh_trade_job' in section or 'beh_tech_job' in section: continue
                active=v('active'); af=self.fields(path,active)
                flags=[]
                if active in ('','nil'): flags.append('disabled_or_missing_active')
                if not trade: flags.append('no_trade_config')
                if not npc_names: flags.append('no_named_original')
                if any(c in suitable for c in '+-!'): flags.append('conditional_suitable')
                if '%' in suitable: flags.append('suitable_effects')
                if 'target_squad_name' in suitable: flags.append('squad_identity_gate')
                if 'bodyguard' in section: flags.append('support_job_not_provider')
                av=lambda key:af.get(key,{}).get('value','')
                inv=av('invulnerable')
                if inv and inv!='false': flags.append('invulnerable_logic')
                if any('teleport' in x['value'] for x in af.values()): flags.append('teleport_entry')
                if active.split('@')[0] not in ('animpoint','walker','beh','sleeper'): flags.append('special_active_scheme')
                origin=f.get('suitable') or f.get('trade') or next(iter(f.values()))
                jobs.append(dict(smart=smart,level=PurePosixPath(k).parts[1],role=role,npc=';'.join(npc_names),
                    name=';'.join(profile_by_id.get(character(n),{}).get('name',n) for n in npc_names),
                    job=section,active=active,trade=trade,suitable=suitable,invulnerable=inv,
                    task_section=v('task_section') or ';'.join(npc_names),flags=';'.join(flags),
                    smart_config=k,job_config=path,source=str(self.files.get(origin['file'],self.files[k])[0]),
                    line=origin['line'],provider=self.files.get(origin['file'],self.files[k])[1]))
        for row in profiles.values():
            matched=[j for j in jobs if row['character'] in [character(n) for n in j['npc'].split(';')]]
            roles=set(filter(None,row['roles'].split(';')))
            roles.update(j['role'] for j in matched if j['role']!='guide' and 'support_job_not_provider' not in j['flags'])
            row['roles']=';'.join(sorted(roles))
            row['smarts']=';'.join(sorted({j['smart'] for j in matched}))
            row['flags']='generic_archetype' if row['generic'] else '' if matched else 'no_static_smart_job_match'
        return [p for p in profiles.values() if p['roles']],jobs

def write_csv(path,rows):
    with path.open('w',encoding='utf-8-sig',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]) if rows else ['empty']); writer.writeheader(); writer.writerows(rows)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--workspace',type=Path,default=Path('../..'))
    ap.add_argument('--mo2',type=Path,required=True); ap.add_argument('--game',type=Path,required=True)
    ap.add_argument('--profile',default='My Gamma'); ap.add_argument('--out',type=Path,default=Path('ai-docs/service-audit'))
    a=ap.parse_args(); a.out.mkdir(parents=True,exist_ok=True)
    base={}; overlay(a.workspace/'ai_workspace/vanilla scripts/gamedata/configs','vanilla',base)
    combined=base.copy(); overlay(a.game/'gamedata/configs','game_loose',combined)
    enabled=[s[1:] for s in read(a.mo2/'profiles'/a.profile/'modlist.txt').splitlines() if s.startswith('+')]
    for name in reversed(enabled): overlay(a.mo2/'mods'/name/'gamedata/configs',name,combined)
    summary={'profile':a.profile,'enabled_mods':len(enabled),'limits':['static config inventory; runtime DXML and script-created NPCs require in-game snapshot','DLTX matched by target filename; conditional/order-sensitive patch combinations need runtime verification']}
    datasets={}
    for label,files in [('vanilla',base),('active',combined)]:
        corpus=Corpus(files); profiles,jobs=corpus.analyze()
        datasets[label]=(profiles,jobs)
        write_csv(a.out/(label+'_providers.csv'),profiles); write_csv(a.out/(label+'_jobs.csv'),jobs)
        summary[label]={'profiles':len(profiles),'jobs':len(jobs),'smarts':len({j['smart'] for j in jobs}),
            'warnings':sorted(set(corpus.warnings)),'patch_files':sum(map(len,corpus.patches.values()))}
        summary[label]['named_profiles']=sum(not p['generic'] for p in profiles)
        summary[label]['generic_profiles']=sum(p['generic'] for p in profiles)
    original={p['character']:p for p in datasets['vanilla'][0]}
    added=[]
    for p in datasets['active'][0]:
        before=original.get(p['character'])
        status='added' if before is None else 'changed' if any(p[k]!=before[k] for k in ('roles','dialogs','community','smarts')) else 'same_service_contract'
        if status!='same_service_contract': added.append(dict(change=status,**p))
    write_csv(a.out/'modded_provider_changes.csv',added)
    summary['modded_changes']={'added':sum(p['change']=='added' for p in added),'changed':sum(p['change']=='changed' for p in added)}
    report=['# Каталог сервисников: статический срез', '',
        'Роли — доступные услуги; medic/tech/barman могут также иметь торговый диалог. Это профили и рабочие места, не число живых NPC.',
        'Привязка к смарту берётся из его exclusive/workN. Пустая привязка требует отдельной проверки; профиль может относиться к старому/неактивному NPC.', '',
        '## Штатные именные/специальные профили', '', '| Профиль | Имя | Услуги | Смарт |', '|---|---|---|---|']
    for p in sorted(datasets['vanilla'][0],key=lambda p:p['character']):
        if not p['generic']: report.append('| '+' | '.join(p[k] or '—' for k in ('character','name','roles','smarts'))+' |')
    report += ['', '## Дополнительные профили активной сборки', '', '| Профиль | Имя | Услуги | Смарт |', '|---|---|---|---|']
    for p in sorted(added,key=lambda p:p['character']):
        if p['change']=='added': report.append('| '+' | '.join(p[k] or '—' for k in ('character','name','roles','smarts'))+' |')
    report += ['', '## Сервисные смарты активной сборки', '', '| Локация | Смарт | Работы (без проводников) |', '|---|---|---|']
    for smart in sorted({j['smart'] for j in datasets['active'][1]}):
        jobs=[j for j in datasets['active'][1] if j['smart']==smart and j['role']!='guide']
        if jobs: report.append('| '+jobs[0]['level']+' | '+smart+' | '+'; '.join(j['role']+': '+j['job'] for j in jobs)+' |')
    (a.out/'INVENTORY.md').write_text('\n'.join(report)+'\n',encoding='utf-8')
    (a.out/'summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in summary.items() if k not in ('vanilla','active')},ensure_ascii=False))
    for label in ('vanilla','active'): print(label,{k:v for k,v in summary[label].items() if k!='warnings'},'warnings',len(summary[label]['warnings']))

if __name__=='__main__': main()
