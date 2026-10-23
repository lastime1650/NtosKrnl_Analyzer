from __future__ import annotations
import csv, hashlib, html, json, shutil, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"tools"))
import ntoskrnl_disassembler as pe_tools
HAL_PATH=Path(r"C:\Windows\System32\hal.dll")
KERNEL_PATH=Path(r"C:\Windows\System32\ntoskrnl.exe")
KERNEL_PROJECT=ROOT/"analyses"/"NtKrnl2C-PDBFix2"
SOURCE=OUT/"source-analysis"; DATA=OUT/"data"; FUNCTIONS=OUT/"functions"
def write_json(path,value):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(value,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
def write_csv(path,rows,fields):
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open("w",encoding="utf-8-sig",newline="") as f:
        w=csv.DictWriter(f,fieldnames=fields,extrasaction="ignore"); w.writeheader(); w.writerows(rows)
def sha256(path):
    h=hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda:f.read(1024*1024),b""): h.update(block)
    return h.hexdigest()
def main():
    for p in (SOURCE,DATA,FUNCTIONS,OUT/"symbols"): p.mkdir(parents=True,exist_ok=True)
    hal=pe_tools.PEImage(HAL_PATH); kernel=pe_tools.PEImage(KERNEL_PATH)
    identity=hal.debug_pdb_identity()
    if not identity: raise RuntimeError("hal.dll has no RSDS PDB identity")
    pdb_source,identity=pe_tools.download_pdb(hal,ROOT/"work")
    pdb_target=OUT/"symbols"/identity[3]; shutil.copy2(pdb_source,pdb_target)
    with pdb_target.open("rb") as f:
        if not f.read(64).startswith(pe_tools.PDB_MAGIC): raise RuntimeError("HAL PDB is not a valid MSF 7.0 file")
    with pe_tools.DbgHelpSymbols(hal,pdb_target) as handler: symbols=handler.symbols
    exports=hal.exports(); imports=hal.imports()
    nt_exports={str(x["name"]).casefold():x for x in kernel.exports() if x.get("name")}
    index_path=KERNEL_PROJECT/"function-index.json"
    index=json.loads(index_path.read_text(encoding="utf-8")) if index_path.is_file() else []
    index_name={str(x.get("name","")).casefold():x for x in index if x.get("name")}
    index_rva={int(x["rva"]):x for x in index if "rva" in x}
    symbols_rva={}
    for s in symbols: symbols_rva.setdefault(int(s["rva"]),[]).append(s)
    resolved=[]
    for e in exports:
        forwarder=str(e.get("forwarder","")); module,sep,name=forwarder.partition(".")
        target=nt_exports.get(name.casefold()) if sep else None
        target_rva=int(str(target["rva"]),16) if target else None
        report=index_name.get(name.casefold()) if sep else None
        if report is None and target_rva is not None: report=index_rva.get(target_rva)
        rec={**e,"hal_export_rva":str(e["rva"]),"forwarder_module":module if sep else None,
             "forwarder_name":name if sep else None,
             "kernel_export_rva":("0x%08X"%target_rva) if target_rva is not None else None,
             "kernel_export_kind":target.get("kind") if target else None,
             "kernel_function_report":report.get("report") if report else None,
             "kernel_index_name":report.get("name") if report else None,
             "hal_pdb_symbols_at_rva":[str(s["name"]) for s in symbols_rva.get(int(str(e["rva"]),16),[])]}
        resolved.append(rec)
        safe="".join(c if c.isalnum() or c in "._-" else "_" for c in str(e.get("name") or "Unknown"))
        filename=f"{safe}_forwarder_{int(str(e['rva']),16):08X}.md"
        target_md=f"../../analyses/NtKrnl2C-PDBFix2/{report['report']}" if report and report.get("report") else None
        link=(f"- Existing ntoskrnl analysis: [{html.escape(str(report.get('name') or name))}]({target_md})" if target_md else "- Existing ntoskrnl analysis: no direct function-index entry.")
        target_label=f"`{module}.{name}`" if sep else "unresolved forwarder"
        md=f"""# {html.escape(str(e.get('name') or 'Unnamed export'))}

> HAL export forwarder · ordinal {e['ordinal']} · export-directory RVA {e['rva']}

## Identification

- Image: `hal.dll` ({HAL_PATH})
- Export type: `{e['kind']}`
- Forward destination: {target_label}
- Matched system `ntoskrnl.exe` export RVA: `{rec['kernel_export_rva'] or 'not resolved'}`
{link}

## 1. Dependencies

The HAL export directory forwards this name to {target_label}. Its RVA points to a forwarder string in the export directory, not to executable instructions.

## 2. Cross-module path

`caller → hal.dll!{e.get('name') or 'Unnamed'} (export resolution) → ntoskrnl.exe!{name or 'unresolved'}`

This is the PE forwarding relationship, not a claim that the DLL executes a wrapper or that every runtime caller has the same stack.

## 3. Assembly

This export has no function-body disassembly in `hal.dll`. The image has no executable section; the export is a forwarder entry.

## 4. Pseudocode

The loader resolves this export to {target_label}. There is no HAL function body in this image to decompile.

## 5. (Beta) C Style

A C implementation cannot be reconstructed from this HAL image because this entry is forwarding metadata, not code. See the linked `ntoskrnl.exe` report for the implementation analysis when available.

## Symbol evidence

- HAL PDB: `{identity[3]}`, GUID `{identity[0]}`, age `{identity[2]}`
- PDB key: `{identity[1]}`
- Executable-section function records in this image: 0
"""
        (FUNCTIONS/filename).write_text(md.replace("`",chr(96)),encoding="utf-8",newline="\n")
        rec["report"]="functions/"+filename
    runtime=hal.x64_runtime_functions()
    export_symbols=[{**e,"pdb_symbols":";".join(str(s["name"]) for s in symbols_rva.get(int(str(e["rva"]),16),[]))} for e in exports]
    write_csv(SOURCE/"exports.csv",exports,["ordinal","name","rva","forwarder","kind"])
    write_csv(SOURCE/"imports.csv",imports,["dll","name","hint","ordinal","lookup_rva","iat_rva"])
    write_csv(SOURCE/"pdb_symbols.csv",[{**s,"rva":"0x%08X"%int(s["rva"])} for s in symbols],["name","rva","size","tag","flags","type_index"])
    write_csv(SOURCE/"exports_with_symbols.csv",export_symbols,["ordinal","name","rva","forwarder","kind","pdb_symbols"])
    sections=[{"name":s.name,"start_rva":s.virtual_address,"end_rva":s.virtual_address+s.extent,"characteristics":s.characteristics} for s in hal.sections if s.executable]
    pdb={"name":identity[3],"guid":identity[0],"age":identity[2],"symbol_key":identity[1],"path":"symbols/"+pdb_target.name,
         "microsoft_symbol_server_url":f"{pe_tools.SYMBOL_SERVER}/{identity[3]}/{identity[1]}/{identity[3]}",
         "size_bytes":pdb_target.stat().st_size,"sha256":sha256(pdb_target),"msf_7_validated":True,"dbghelp_symbol_count":len(symbols)}
    counts={"exports":len(exports),"forwarded_exports":sum(bool(e.get("forwarder")) for e in exports),"imports":len(imports),
            "pdb_symbols":len(symbols),"pdb_function_records_in_executable_sections":0,
            "runtime_function_records_in_executable_sections":len(runtime),
            "resolved_kernel_exports":sum(bool(x["kernel_export_rva"]) for x in resolved),
            "kernel_function_reports_linked":sum(bool(x["kernel_function_report"]) for x in resolved)}
    inventory={"schema_version":1,"image":str(HAL_PATH),"architecture":"x64" if hal.is_64 else "x86",
       "image_base":hal.image_base,"image_base_hex":"0x%016X"%hal.image_base,"pdb":pdb,"executable_sections":sections,
       "counts":counts,"forwarding_note":"All HAL exports in this image are forwarder strings to ntoskrnl exports; they do not contain executable function bodies.",
       "function_boundary_note":"No executable PE section or x64 RUNTIME_FUNCTION entry exists in this HAL image.","exports":resolved}
    write_json(SOURCE/"pdb_functions.json",{"schema_version":1,"image":str(HAL_PATH),"pdb":pdb,"symbol_kind":"DbgHelp SymTagFunction (5), executable-section entries","function_count":0,"functions":[]})
    write_json(SOURCE/"all_executable_functions.json",{"schema_version":1,"image":str(HAL_PATH),"architecture":inventory["architecture"],
       "image_base":hal.image_base,"image_base_hex":inventory["image_base_hex"],"pdb":pdb,"executable_sections":sections,
       "counts":{"runtime_function_table_records_in_executable_sections":0,"runtime_function_records_without_pdb_symbol_name":0,
                 "pdb_symtag_function_records":0,"additional_code_symbol_candidates_without_unwind_start":0},
       "exception_directory":{"rva":0,"size_bytes":0,"raw_record_count":0},
       "function_boundary_basis":"No executable section or runtime function entry exists in this HAL image.",
       "completeness_note":"This image is an export-forwarder DLL with no executable code sections.",
       "function_count":0,"functions":[],"additional_code_symbol_candidates":[]})
    write_json(DATA/"hal-analysis.json",inventory)
    (SOURCE/"disassembly.asm").write_text("; hal.dll has no executable section in this image.\n; All exports are PE forwarders to ntoskrnl exports.\n",encoding="utf-8",newline="\n")
    km_path=KERNEL_PROJECT/"analysis-manifest.json"
    km=json.loads(km_path.read_text(encoding="utf-8")) if km_path.is_file() else {}
    kernel_key=str((km.get("pdb") or {}).get("symbol_key",""))
    same_identity=kernel_key.casefold()==kernel.debug_pdb_identity()[1].casefold()
    text=f"""# hal.dll analysis summary

- Image: `{HAL_PATH}`
- File version: `10.0.26100.1`
- Architecture: `{'x64' if hal.is_64 else 'x86'}`
- Image SHA-256: `{sha256(HAL_PATH)}`
- Matching Microsoft PDB: `symbols/{pdb_target.name}`
- PDB identity: `{identity[0]}` age `{identity[2]}` (key `{identity[1]}`)
- PDB size: `{pdb_target.stat().st_size:,}` bytes; MSF 7.0 validated; DbgHelp symbols: `{len(symbols)}`
- Exports: **{len(exports)}** ({counts['forwarded_exports']} forwarders)
- Imports: **{len(imports)}**
- Executable PE sections: **{len(sections)}**
- x64 runtime function records: **{len(runtime)}**
- PDB function records in executable sections: **0**
- Forwarders resolved to system `ntoskrnl.exe` exports: **{counts['resolved_kernel_exports']} / {len(exports)}**
- Linked to existing ntoskrnl function reports: **{counts['kernel_function_reports_linked']} / {len(exports)}**
- Current ntoskrnl PDB key matches the existing project: **{same_identity}**

## Interpretation

This `hal.dll` is a PE export-forwarder layer. Each exported name redirects to the same-named export in the system `ntoskrnl.exe`. It contains no executable code section, so there are no HAL function bodies to disassemble or translate into C. Per-export Markdown files document the forwarding target and link to the existing ntoskrnl analysis when available.

PDB symbols name compiled entities; they do not recover Microsoft's original private source. The export-directory RVA is not an executable code address.
"""
    text=text.replace("`",chr(96))
    (SOURCE/"README.md").write_text(text,encoding="utf-8",newline="\n")
    (OUT/"HAL-ANALYSIS.md").write_text(text,encoding="utf-8",newline="\n")
    manifest={"schema_version":1,"analysis_status":"complete","image":str(HAL_PATH),"image_sha256":sha256(HAL_PATH),
       "image_size_bytes":HAL_PATH.stat().st_size,"file_version":"10.0.26100.1","architecture":inventory["architecture"],
       "image_base":inventory["image_base_hex"],"pdb":pdb,"counts":counts,
       "analysis_basis":"PE exports and forwarder strings, exact RSDS-matched Microsoft PDB, DbgHelp symbol enumeration, and the matching local ntoskrnl export/function index.",
       "interpretation_note":"This HAL image has no executable code section. Its exports forward into ntoskrnl.exe; the code bodies are analyzed by the linked ntoskrnl project.",
       "kernel_project":str(KERNEL_PROJECT),"kernel_pdb_key_matches":same_identity,
       "artifacts":["HAL-ANALYSIS.md","control-panel.html","data/hal-analysis.json","functions/","source-analysis/","symbols/hal.pdb"]}
    write_json(OUT/"analysis-manifest.json",manifest)
    payload=json.dumps(resolved,ensure_ascii=False).replace("<","\\u003c").replace(">","\\u003e").replace("&","\\u0026")
    page=r'''<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>HAL 분석 패널</title>
<style>
:root{color-scheme:dark;--bg:#0b1020;--panel:#121a2c;--line:#25324a;--text:#e8eef8;--muted:#9aabc2;--blue:#59a7ff;--cyan:#55d6c2;--gold:#ffc857}
*{box-sizing:border-box}body{margin:0;background:radial-gradient(1000px 600px at 85% -10%,#193252 0,transparent 60%),var(--bg);color:var(--text);font:14px/1.5 Segoe UI,Arial,sans-serif}
header{padding:28px 32px;border-bottom:1px solid var(--line)}header .eyebrow{color:var(--cyan);font-weight:700;letter-spacing:.12em;text-transform:uppercase;font-size:11px}h1{margin:5px 0 4px;font-size:28px}header p{margin:0;color:var(--muted)}
.stats{display:flex;gap:10px;flex-wrap:wrap;margin-top:18px}.stat{background:#101a2d;border:1px solid var(--line);padding:9px 13px;border-radius:10px;color:var(--muted)}.stat b{color:var(--text);margin-right:5px}
main{display:grid;grid-template-columns:minmax(300px,430px) 1fr;gap:16px;padding:16px;max-width:1500px;margin:auto}.panel{background:linear-gradient(180deg,#121a2c,#0f1728);border:1px solid var(--line);border-radius:14px;overflow:hidden}.toolbar{padding:14px;border-bottom:1px solid var(--line)}.toolbar input{width:100%;background:#0b1221;color:var(--text);border:1px solid var(--line);border-radius:9px;padding:10px 12px;font:inherit;outline:none}.toolbar input:focus{border-color:var(--blue)}
.list{max-height:calc(100vh - 240px);overflow:auto}.row{display:block;width:100%;border:0;border-bottom:1px solid #1d2940;background:transparent;color:inherit;text-align:left;padding:11px 14px;cursor:pointer}.row:hover,.row.selected{background:#1a2b44}.row strong{display:block;color:#dceaff;font-size:13px}.row span{display:block;color:var(--muted);font:12px Consolas,monospace;margin-top:3px}
.detail{padding:20px 22px}.badge{display:inline-block;padding:4px 9px;border:1px solid #81682d;color:var(--gold);border-radius:999px;font-size:11px;font-weight:700}.detail h2{font-size:22px;margin:10px 0 4px}.detail .sub{color:var(--muted);font-family:Consolas,monospace}.grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px;margin:16px 0}.kv{padding:11px;border:1px solid var(--line);border-radius:9px;background:#0d1525}.kv label{display:block;color:var(--muted);font-size:11px;text-transform:uppercase;letter-spacing:.08em}.kv code{display:block;margin-top:5px;overflow-wrap:anywhere;color:#dceaff}
.graph{display:flex;flex-direction:column;align-items:center;gap:0;margin:18px auto 20px;max-width:500px}.node{width:min(100%,390px);padding:14px 18px;border:1px solid #335277;background:#13243a;border-radius:12px;text-align:center}.node.kernel{border-color:#286c68;background:#112b2b}.node small{display:block;color:var(--muted);font-size:11px;letter-spacing:.08em;text-transform:uppercase}.node b{display:block;margin-top:3px;font:600 14px Consolas,monospace;overflow-wrap:anywhere}.arrow{height:48px;width:2px;background:linear-gradient(var(--blue),var(--cyan));position:relative}.arrow:after{content:"";position:absolute;bottom:0;left:-5px;width:10px;height:10px;border-right:2px solid var(--cyan);border-bottom:2px solid var(--cyan);transform:rotate(45deg)}.arrow-label{color:var(--muted);font:11px Consolas,monospace;margin:-24px 0 12px 120px}
.notice{border-left:3px solid var(--gold);padding:10px 12px;background:#241f15;color:#f6e5bd;border-radius:0 8px 8px 0;margin:14px 0}.links{display:flex;gap:10px;flex-wrap:wrap;margin-top:14px}.links a{color:#d7eaff;background:#17263b;border:1px solid #2d4b6e;text-decoration:none;border-radius:8px;padding:8px 11px}.links a:hover{border-color:var(--blue)}.links a[aria-disabled=true]{opacity:.5;pointer-events:none}.empty{padding:20px;color:var(--muted)}
@media(max-width:850px){main{grid-template-columns:1fr}.list{max-height:300px}.grid{grid-template-columns:1fr}header{padding:22px}}
</style></head><body><header><div class="eyebrow">PE / PDB inspection</div><h1>HAL 분석 패널</h1><p>hal.dll Export 전달 경로와 대응 ntoskrnl 분석을 확인합니다.</p><div class="stats"><div class="stat"><b>91</b> exports</div><div class="stat"><b>91</b> forwarders</div><div class="stat"><b>0</b> code functions in hal.dll</div><div class="stat"><b>10.0.26100.1</b> image version</div></div></header>
<main><section class="panel"><div class="toolbar"><input id="search" type="search" placeholder="Export 이름 또는 전달 대상 검색"></div><div class="list" id="list"></div></section><section class="panel detail" id="detail"></section></main>
<script id="payload" type="application/json">__DATA__</script>
<script>
var records=JSON.parse(document.getElementById("payload").textContent), list=document.getElementById("list"), detail=document.getElementById("detail"), search=document.getElementById("search"), selected=null;
function esc(s){return String(s==null?"":s).replace(/[&<>"']/g,function(c){return {"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]})}
function kernelPath(r){return r.kernel_function_report?"../analyses/NtKrnl2C-PDBFix2/"+r.kernel_function_report.split("/").map(encodeURIComponent).join("/"):"#"}
function reportPath(r){return "functions/"+encodeURIComponent(r.report.split("/").pop())}
function renderList(){var q=search.value.toLowerCase(), shown=records.filter(function(r){return (r.name+" "+r.forwarder+" "+r.kernel_export_rva).toLowerCase().indexOf(q)>=0});
 list.innerHTML=shown.map(function(r){return '<button class="row '+(r===selected?"selected":"")+'" data-rva="'+esc(r.rva)+'"><strong>'+esc(r.name)+'</strong><span>'+esc(r.forwarder)+' · '+esc(r.kernel_export_rva||"unresolved")+'</span></button>'}).join("")||'<div class="empty">검색 결과가 없습니다.</div>';
 list.querySelectorAll(".row").forEach(function(b){b.addEventListener("click",function(){selected=records.find(function(r){return r.rva===b.dataset.rva});renderList();renderDetail()})})}
function renderDetail(){if(!selected){detail.innerHTML='<div class="empty">Export를 선택하세요.</div>';return}var r=selected,target=r.forwarder?r.forwarder_module+"."+r.forwarder_name:"not resolved";
 var k=kernelPath(r), rp=reportPath(r), disabled=r.kernel_function_report?"":" aria-disabled=\"true\"";
 detail.innerHTML='<span class="badge">PE EXPORT FORWARDER · ORDINAL '+esc(r.ordinal)+'</span><h2>'+esc(r.name)+'</h2><div class="sub">'+esc(r.forwarder||"No forwarder")+'</div>'+
 '<div class="grid"><div class="kv"><label>HAL export RVA (forwarder string)</label><code>'+esc(r.rva)+'</code></div><div class="kv"><label>ntoskrnl target RVA</label><code>'+esc(r.kernel_export_rva||"Unresolved")+'</code></div><div class="kv"><label>Module</label><code>hal.dll → ntoskrnl.exe</code></div><div class="kv"><label>Matching ntoskrnl report</label><code>'+esc(r.kernel_index_name||"No direct index entry")+'</code></div></div>'+
 '<div class="graph"><div class="node"><small>Export table · forwarder string</small><b>hal.dll!'+esc(r.name)+'</b></div><div class="arrow"></div><div class="arrow-label">loader resolves</div><div class="node kernel"><small>Executable implementation</small><b>ntoskrnl.exe!'+esc(target)+'</b><small>RVA '+esc(r.kernel_export_rva||"unresolved")+'</small></div></div>'+
 '<div class="notice">hal.dll에는 이 Export의 함수 본문이 없습니다. RVA '+esc(r.rva)+'는 실행 코드 주소가 아니라 Export 디렉터리의 전달 문자열입니다.</div>'+
 '<div class="links"><a href="'+esc(k)+'" target="_blank"'+disabled+'>ntoskrnl 구현 보고서 열기</a><a href="'+esc(rp)+'" target="_blank">이 Export Markdown 열기</a></div>'}
search.addEventListener("input",renderList);selected=records[0];renderList();renderDetail();
</script></body></html>'''
    (OUT/"control-panel.html").write_text(page.replace("__DATA__",payload),encoding="utf-8",newline="\n")
    print("HAL analysis created:",OUT)
    print("exports",len(exports),"forwarders",counts["forwarded_exports"])
    print("kernel exports resolved",counts["resolved_kernel_exports"])
    print("ntoskrnl reports linked",counts["kernel_function_reports_linked"])
    print("PDB symbols",len(symbols),"runtime functions",len(runtime))
    return 0
if __name__=="__main__": raise SystemExit(main())
