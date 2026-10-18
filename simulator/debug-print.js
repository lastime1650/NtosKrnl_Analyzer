export const PRINT_TYPES=['LARGE_INTEGER','ULONG32','ULONG64','LONG','PVOID','ANSI','WCHAR','UNICODE_STRING','BOOLEAN'];
export function printArguments(n){
 const args=Array.isArray(n.formatArgs)?n.formatArgs:[];
 if(args.length>32)throw Error('DbgPrint 인자는 최대 32개입니다.');
 const seen=new Set(['Format']);
 return args.map(a=>{if(!a||!/^([A-Za-z_][A-Za-z0-9_]*|[0-9]+)$/.test(a.name)||seen.has(a.name)||!PRINT_TYPES.includes(a.type))throw Error('DbgPrint 인자 이름 / 자료형이 잘못되었습니다.');seen.add(a.name);return {name:a.name,type:a.type,default:'0'}});
}
export function syncPrintArguments(n){
 const old=new Map((n.formatArgs||[]).map(a=>[a.name,a]));
 const names=[...String(n.formatText||'').matchAll(/{{|}}|{([A-Za-z_][A-Za-z0-9_]*|[0-9]+)(?::[xXdp])?}/g)].filter(m=>m[1]!==undefined).map(m=>m[1]);
 n.formatArgs=[...new Set(names)].map(name=>old.get(name)||{name,type:'LARGE_INTEGER'});
 printArguments(n);
}
export function formatDebug(template,definitions,values,{readString,readUnicode,irql=0,style='named'}={}){
 const unicode=()=>{if(irql!==0)throw Error('Unicode 디버그 출력은 PASSIVE_LEVEL에서만 지원합니다.');};
 const number=(value,kind,width=0)=>{let v=BigInt(value),s;if(kind==='d')s=v.toString();else if(kind==='p')s='0x'+BigInt.asUintN(64,v).toString(16).toUpperCase().padStart(16,'0');else{s=BigInt.asUintN(64,v).toString(kind.toLowerCase()==='x'?16:10);if(kind==='X')s=s.toUpperCase()}return s.padStart(Math.min(128,width),'0')};
 const text=(def,value)=>{if(def.type==='ANSI')return readString(value,false);if(['WCHAR','UNICODE_STRING'].includes(def.type)){unicode();return def.type==='UNICODE_STRING'?readUnicode(value):readString(value,true)}return def.type==='PVOID'?number(value,'p'):String(value)};
 if(style==='named')return String(template).replace(/{{|}}|{([^{}]+)}|[{}]/g,(token,key)=>{
  if(token==='{{')return '{';if(token==='}}')return '}';if(!key)throw Error('포맷 중괄호가 올바르지 않습니다.');
  const [name,kind,...rest]=key.split(':'),def=definitions.find(a=>a.name===name);
  if(!def||!Object.hasOwn(values,name))throw Error('포맷 인자가 없습니다: '+name);
  if(rest.length||kind&&!['x','X','d','p'].includes(kind))throw Error('지원하지 않는 포맷: '+key);
  return kind?number(values[name],kind):text(def,values[name]);
 });
 let index=0;
 return String(template).replace(/%%|%([0]?)(\d{0,3})(I64|ll|l|w)?([diuUxXpcsSZ])|%/g,(token,pad,width,length,kind)=>{
  if(token==='%%')return '%';if(token==='%')throw Error('지원하지 않는 printf 포맷입니다.');
  const def=definitions[index++];if(!def||!Object.hasOwn(values,def.name))throw Error('printf 인자가 부족합니다.');
  const v=values[def.name];
  if(kind==='s'||kind==='S'||kind==='Z'){const wide=length==='l'||length==='w'||kind==='S';if(wide)unicode();if(kind==='Z'){if(length!=='w')throw Error('%wZ만 지원합니다.');return readUnicode(v)}return readString(v,wide)}
  if(kind==='c')return String.fromCharCode(Number(BigInt(v)&255n));
  const bits=length==='I64'||length==='ll'?64:32;
  return number(kind==='d'||kind==='i'?BigInt.asIntN(bits,BigInt(v)):kind==='p'?v:BigInt.asUintN(bits,BigInt(v)),kind==='i'?'d':kind==='U'?'u':kind,pad?Number(width):0);
 });
}
export function executeDebugPrint(e,a,Gap){
 const n=e.node(e.current),defs=printArguments(n),template=a.Format?e.mem.cstring(a.Format):String(n.formatText||'');
 let message;try{message=formatDebug(template,defs,a,{style:n.formatStyle||'printf',irql:e.irql,readString:(p,wide)=>e.mem.cstring(p,wide),readUnicode:p=>e.unicode(p)})}catch(error){if(error.status)throw error;throw new Gap(error.message)}
 // This simulator stores Unicode UI text in UTF-8; cap the recorded message by
 // encoded bytes, without splitting a character. No host debugger is called.
 let clipped='',bytes=0;for(const ch of message){const size=new TextEncoder().encode(ch).length;if(bytes+size>512)break;clipped+=ch;bytes+=size}
 e.log('debug',clipped);e.debugOutput.push({seq:e.sequence,time:e.time,node:n.id,message:clipped,truncated:clipped!==message});if(e.debugOutput.length>2000)e.debugOutput.shift();return 0n;
}
