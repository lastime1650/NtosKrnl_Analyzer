export const debugScope=e=>e.functionFrames.length?'function:'+e.functionFrames.at(-1).id:e.localScope||'root';
const terminal=e=>['completed','stopped','crashed','unsupported'].includes(e.state);
function scopes(e){return [debugScope(e),e.localScope,...e.functionFrames.map(f=>'function:'+f.id),...e.contexts.flatMap(c=>[c.restore?.localScope,...(c.restore?.functionFrames||[]).map(f=>'function:'+f.id)])]}
export class DebugStepper{
 constructor(e,onUpdate=()=>{}){this.e=e;this.onUpdate=onUpdate;this.busy=false;this.generation=0;this.reason='';}
 cancel(){this.generation++;this.busy=false;this.reason='cancelled';}
 canOut(){const e=this.e;return e.state==='paused'&&!!(e.stage||e.current);}
 async command(mode='into'){
  if(this.busy)return;const e=this.e;if(terminal(e))return;
  this.busy=true;const token=++this.generation;this.reason='';
  try{
   if(e.state==='idle'){e.start();e.pause();this.reason='entry';return;}
   e.pause();
   const origin=e.current,scope=debugScope(e),stage=e.stage,visit=e.executionSerial||0;
   const initial=e.node(origin),isCall=initial?.kind==='userCall',isApi=initial?.kind==='api';
   // A stepping command intentionally executes the node at the current stop.
   // Subsequent breakpoints (including a recursive call to the same graph) stop it.
   if(initial?.breakpoint&&!stage)e.breakSkip=origin;
   let executed=false,actions=0,stagnant=0,last='';
   const done=()=>{
    const recent=e.debugLast;if(recent?.seq>visit&&recent.node===origin&&recent.scope===scope)executed=true;
    if(mode==='into'||mode==='over'&&!origin)return actions>0;
    if(mode==='out'){
     if(stage)return ![e.stage,...e.contexts.map(c=>c.restore?.stage)].includes(stage);
     return !scopes(e).includes(scope)||!e.variables.scopes.get(scope)?.active;
    }
    if(!executed)return false;
    if(isCall)return debugScope(e)===scope||!scopes(e).includes(scope);
    if(isApi)return debugScope(e)===scope&&!e.stage||!scopes(e).includes(scope);
    return true;
   };
   while(token===this.generation&&!terminal(e)){
    for(let i=0;i<16&&token===this.generation&&!terminal(e);i++){
     const seq=e.sequence,notify=e.notify;e.notify=()=>{};
     try{e.step()}finally{e.notify=notify}
     actions++;
     if(e.events.some(v=>v.seq>seq&&v.kind==='breakpoint')){this.reason='breakpoint';return;}
     if(done()){this.reason='step-'+mode;return;}
     const signature=[e.current,debugScope(e),e.stage?.index,e.steps,e.time,e.queue.length,e.wait?.waitUntil].join('|');
     stagnant=signature===last?stagnant+1:0;last=signature;
     if(stagnant>=2){this.reason='waiting';return;}
     if(actions>=e.settings.maxSteps*8+100){this.reason='step-limit';return;}
    }
    this.onUpdate(e);await new Promise(resolve=>setTimeout(resolve,0));
   }
  }finally{if(token===this.generation){this.busy=false;if(!terminal(e))e.state='paused';this.onUpdate(e)}}
 }
}
