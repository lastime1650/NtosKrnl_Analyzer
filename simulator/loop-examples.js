// Portable graph fixtures used by the UI, browser regression and engine tests.
export const LOOP_EXAMPLES={for:'for · 조건과 증감값 연결',while:'while · 메모리 변수 갱신','loop-control':'for · break / continue','nested-loops':'중첩 반복문'};
export function makeLoopExample(name){
 const nodes=[],edges=[];const add=(id,kind,extra={},x=500,y=250)=>{const n={id:'demo_'+id,kind,params:{},x,y,...extra};nodes.push(n);return n;};
 const link=(a,out,b,input,kind='data')=>edges.push({id:'link_'+edges.length,kind,from:a.id,out,to:b.id,in:input});const flow=(a,b,out='then',input='exec')=>link(a,out,b,input,'exec');
 const entry=add('entry','entry',{},500,30),ret=add('return','return',{params:{Status:'STATUS_SUCCESS'}},1100,250);
 const scalar=(id,value,y)=>add(id,'data',{type:'LARGE_INTEGER',value:String(value)},30,y);
 const start=scalar('start',0,240),limit=scalar('limit',name==='loop-control'?10:name==='nested-loops'?3:5,470),step=scalar('step',1,700),variable=scalar('variable',0,930);
 const loop=add('loop',name==='while'?'while':'for',{op:'<',conditionMode:'compare',params:{Start:'0',Limit:'5',Step:'1',Left:'0',Right:'5',Condition:'TRUE',MaxIterations:'1000'}},500,250);
 flow(entry,loop);flow(loop,ret,'after');
 const write=add('write','write',{width:8,params:{Address:'0',Offset:'0',Value:'0'}},500,1080);link(variable,'Address',write,'Address');
 if(name==='while'){
  const compare=add('condition','compare',{op:'<',params:{Left:'0',Right:'5'}},30,1230),calc=add('increment','calculate',{op:'+',params:{Left:'0',Right:'1'}},30,1500);
  link(variable,'Value',loop,'Left');link(limit,'Value',loop,'Right');link(variable,'Value',compare,'Left');link(limit,'Value',compare,'Right');link(compare,'Value',loop,'Condition');link(variable,'Value',calc,'Left');link(step,'Value',calc,'Right');link(calc,'Value',write,'Value');flow(loop,write,'body');flow(write,loop,'then','repeat');
 }else{
  link(start,'Value',loop,'Start');link(limit,'Value',loop,'Limit');link(step,'Value',loop,'Step');
  if(name==='for'){
   const compare=add('condition','compare',{op:'<',params:{Left:'0',Right:'5'}},30,1230);link(loop,'Index',compare,'Left');link(limit,'Value',compare,'Right');link(compare,'Value',loop,'Condition');link(loop,'Index',write,'Value');flow(loop,write,'body');flow(write,loop,'then','repeat');
  }else if(name==='loop-control'){
   const branch=add('branch','branch',{op:'==',elseOp:'==',params:{Left:'0',Right:'2',ElseLeft:'0',ElseRight:'5'}},500,1030),skip=add('continue','continue',{},960,1080),stop=add('break','break',{},960,1330);write.y=1690;link(loop,'Index',branch,'Left');link(loop,'Index',branch,'ElseLeft');flow(loop,branch,'body');flow(branch,skip,'if');flow(branch,stop,'elseIf');flow(branch,write,'else');link(loop,'Index',write,'Value');flow(write,loop,'then','repeat');
  }else if(name==='nested-loops'){
   const inner=add('inner','for',{op:'<',params:{Start:'0',Limit:'5',Step:'1',Condition:'TRUE',MaxIterations:'1000'}},500,1030),branch=add('branch','branch',{op:'==',elseOp:'==',params:{Left:'0',Right:'1',ElseLeft:'0',ElseRight:'3'}},500,1840),skip=add('continue','continue',{},1000,1810),stop=add('break','break',{},1000,2090),multiply=add('multiply','calculate',{op:'*',params:{Left:'0',Right:'10'}},30,1830),sum=add('sum','calculate',{op:'+',params:{Left:'0',Right:'0'}},30,2110);write.y=2470;flow(loop,inner,'body');flow(inner,loop,'after','repeat');flow(inner,branch,'body');link(inner,'Index',branch,'Left');link(inner,'Index',branch,'ElseLeft');flow(branch,skip,'if');flow(branch,stop,'elseIf');flow(branch,write,'else');link(loop,'Index',multiply,'Left');link(multiply,'Value',sum,'Left');link(inner,'Index',sum,'Right');link(sum,'Value',write,'Value');flow(write,inner,'then','repeat');
  }
 }
 return {schema:1,nodes,edges};
}
