// Build a read-only evaluator. In particular, hovering must never materialize a
// new data allocation or update expression caches in the running engine.
export function inspectValue(e,value,type,source){
 const info={value,type,source};
 if(typeof value!=='bigint'||!['ANSI','PCSTR','WCHAR','PCWSTR','UNICODE_STRING','PUNICODE_STRING'].includes(type))return info;
 try{
  let pointer=e.mem.resolve(value),length=null,wide=['WCHAR','PCWSTR','UNICODE_STRING','PUNICODE_STRING'].includes(type);
  if(['UNICODE_STRING','PUNICODE_STRING'].includes(type)){
   const object=e.mem.block(pointer);if(!object||object.freed||pointer+16n>object.address+BigInt(object.size))return info;
   length=Number(e.mem.num(pointer,2));pointer=e.mem.resolve(e.mem.num(pointer+8n));
  }
  const block=e.mem.block(pointer);if(!block||block.freed)return info;
  const offset=Number(pointer-block.address),available=Math.min(block.size-offset,length??Infinity,320),start=block.start+offset;
  let text='';for(let i=0;i+(wide?1:0)<available;i+=wide?2:1){const v=e.mem.bytes[start+i]|(wide?e.mem.bytes[start+i+1]<<8:0);if(!v&&length===null)break;text+=String.fromCharCode(v)}
  info.preview=text;
 }catch{}return info;
}
export function inspectArgument(e,n,name,{ports,TYPES,coerce,graphOf}){
 if(!e||e.state!=='paused')return {error:'일시정지 / 중단점에서 값을 확인할 수 있습니다.'};
 if(graphOf(n)!==e.activeGraph)return {error:'현재 활성 함수 호출의 인자만 조회할 수 있습니다.'};
 const spec=ports(n,e.program).inputs.find(p=>p.name===name);if(!spec)return {error:'입력 인자가 아닙니다.'};
 const edge=e.program.edges.find(x=>x.kind==='data'&&x.to===n.id&&x.in===name);
 const source=edge?edge.from+'.'+edge.out:'직접 입력';
 try{
  if(e.current===n.id&&e.stage&&Object.hasOwn(e.stage.args,name))return inspectValue(e,e.stage.args[name],spec.type,'호출 시 캡처 · '+source);
  const peek=Object.create(e);peek.outputs=new Map(e.outputs);peek.materialized=new Map(e.materialized);
  peek.variables=Object.assign(Object.create(Object.getPrototypeOf(e.variables)),e.variables,{e:peek});
  const baseValue=e.value;
  peek.value=function(id,port='Value',seen=new Set()){
   const node=this.node(id);
   if(node?.kind==='data'&&!this.materialized.has(id)){
    if(TYPES[node.type]?.scalar&&port==='Value')return coerce(this.literal(node.value??0),node.type);
    throw Error('아직 가상 메모리에 배치되지 않은 자료형입니다. 설정값: '+String(node.value??node.type));
   }
   if(node?.kind==='data')return this.dataValue(node,port);
   return baseValue.call(this,id,port,seen);
  };
  return inspectValue(e,peek.input(n,name),spec.type,source);
 }catch(error){return {error:error.message,type:spec.type,source}}
}
