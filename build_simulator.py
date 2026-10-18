#!/usr/bin/env python3
"""Bind the browser contract simulator to this exact PE / PDB analysis."""
from __future__ import annotations
import argparse
import bisect
import hashlib
import json
import shutil
import sys
from pathlib import Path

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root',type=Path,default=Path(__file__).resolve().parent)
    parser.add_argument('--exe',type=Path,default=Path('C:/Windows/System32/ntoskrnl.exe'))
    args=parser.parse_args()
    root=args.root.resolve()
    sys.path.insert(0,str(root/'tools'))
    from ntoskrnl_disassembler import PEImage
    import capstone
    from capstone.x86 import X86_OP_IMM
    pe=PEImage(args.exe)
    inventory=json.loads((root/'data/all_executable_functions.json').read_text(encoding='utf-8'))
    digest=hashlib.sha256(pe.data).hexdigest()
    expected=json.loads((root/'summary.json').read_text(encoding='utf-8')).get('image_sha256')
    if expected and expected!=digest:
        raise ValueError('PE hash does not match the function analysis. Analyze this version first.')
    records=inventory['functions']
    by_rva={int(r['rva']):r for r in records}
    index=json.loads((root/'function-index.json').read_text(encoding='utf-8'))
    names={int(r['rva']):r['name'] for r in index}
    reports={int(r['rva']):r['report'] for r in index}
    for r in inventory.get('additional_code_symbol_candidates',[]):
        names.setdefault(int(r['rva']),str(r.get('name') or (r.get('symbol_names') or [''])[0]))
    exports=[]
    for row in pe.exports():
        rva=int(str(row['rva']),16)
        section=pe.section_for_rva(rva)
        callable=bool(section and section.executable and not row['forwarder'])
        aliases=str(row['name']).split(';') if row['name'] else [f"ordinal_{row['ordinal']}"]
        for name in aliases:
            exports.append({'id':name,'name':name if row['name'] else f"#{row['ordinal']} · {names.get(rva,'Unknown')}", 'ordinal':row['ordinal'],'rva':f'0x{rva:08X}','callable':callable,'forwarder':row['forwarder'],'symbol':names.get(rva,''),'report':reports.get(rva,'')})
            names.setdefault(rva,name)
    md=capstone.Cs(capstone.CS_ARCH_X86,capstone.CS_MODE_64)
    md.detail=True
    starts=sorted(by_rva)
    calls={}
    pending={int(x['rva'],16) for x in exports if x['callable']}
    for depth in range(3):
        next_pending=set()
        for rva in sorted(pending):
            key=f'0x{rva:08X}'
            if key in calls: continue
            rec=by_rva.get(rva)
            size=min(int(rec['end_rva'])-rva,32768) if rec else 256
            section=pe.section_for_rva(rva)
            if not section or not section.executable:continue
            found=[]
            try:
                for ins in md.disasm(pe.bytes_at_rva(rva,size),pe.image_base+rva):
                    if not rec and ins.mnemonic in ('ret','int3'):break
                    if ins.mnemonic=='call':
                        direct=bool(ins.operands and ins.operands[0].type==X86_OP_IMM)
                        target=int(ins.operands[0].imm)-pe.image_base if direct else None
                        if direct:
                            target_section=pe.section_for_rva(target)
                            if target_section and target_section.executable:
                                next_pending.add(target)
                        found.append({'site':f'0x{ins.address-pe.image_base:08X}','target':f'0x{target:08X}' if target is not None else None,'name':names.get(target,f'sub_{target:08X}') if target is not None else ins.op_str,'kind':'direct' if direct else 'indirect','report':reports.get(target,'')})
                        if len(found)>=64:break
            except Exception as exc:
                found.append({'kind':'decode-limit','name':str(exc)})
            calls[key]=found
        pending=next_pending
    data={'schema':1,'image':str(args.exe),'sha256':digest,'pdb':inventory.get('pdb',{}),'architecture':inventory.get('architecture'),'exportCount':len(pe.exports()),'exports':exports,'calls':calls,'traceNote':'Direct call sites decoded from this exact PE. These are static candidates, not a recorded execution path. Indirect targets, CFG tail transfers and branch reachability are not resolved here.'}
    dest=root/'simulator'
    dest.mkdir(exist_ok=True)
    (dest/'catalog.js').write_text('window.KERNEL_CATALOG='+json.dumps(data,ensure_ascii=True,separators=(',',':')).replace('</','<\\/')+';\n',encoding='utf-8')
    from build_internal_graphs import build
    build(root)
    print(f'Simulator catalog: {len(exports)} export names, {len(calls)} static call maps; {digest}')

if __name__=='__main__':main()
