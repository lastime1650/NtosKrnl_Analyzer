const frame=document.getElementById('app'),button=document.getElementById('run'),result=document.getElementById('result'),list=document.getElementById('results');
frame.onload=()=>{button.disabled=false;result.textContent='준비됨'};
button.onclick=async()=>{
 button.disabled=true;list.replaceChildren();const rows=[];
 const w=frame.contentWindow,d=w.document,canvas=d.getElementById('canvas');
 const saved=new Map(Object.keys(localStorage).filter(k=>k.startsWith('ntoskrnl-simulator-v1:')).map(k=>[k,localStorage.getItem(k)]));
 const pointer=(target,type,opts={})=>{const e=new w.PointerEvent(type,{bubbles:true,cancelable:true,pointerId:7,pointerType:'mouse',isPrimary:true,button:0,buttons:type==='pointerup'?0:1,clientX:400,clientY:200,...opts});target.dispatchEvent(e);return e};
 const check=(ok,message)=>{if(!ok)throw Error(message)};
 const eventErrors=[],onEventError=e=>eventErrors.push(e.message);w.addEventListener('error',onEventError);
 const test=(name,fn)=>{const before=eventErrors.length;try{fn();rows.push({name,pass:true})}catch(e){rows.push({name,pass:false,error:e.message})}finally{w.dispatchEvent(new w.Event('blur'));w.dispatchEvent(new w.KeyboardEvent('keydown',{key:'Escape'}));if(eventErrors.length!==before){rows.at(-1).pass=false;rows.at(-1).error=eventErrors.slice(before).join('; ')}}};
 const pos=el=>[el.style.left,el.style.top],same=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
 try{
  const node=d.querySelector('[data-node]'),header=node.querySelector('[data-drag]');
  test('느린 노드 드래그 → 해제 후 이동 중단',()=>{pointer(header,'pointerdown');for(let i=1;i<=20;i++)pointer(w,'pointermove',{clientX:400+i,clientY:200+i});pointer(w,'pointerup',{clientX:420,clientY:220});const after=pos(node);pointer(w,'pointermove',{clientX:600,clientY:300,buttons:0});check(same(after,pos(node)),'해제 후 노드 이동');check(!canvas.classList.contains('graph-dragging'),'드래그 잔류')});
  test('드래그 시작 시 브라우저 기본 동작 차단',()=>{check(pointer(header,'pointerdown').defaultPrevented,'pointerdown 기본 동작 허용')});
  test('pointerup 누락 시 buttons=0으로 복구',()=>{pointer(header,'pointerdown');const before=pos(node);pointer(w,'pointermove',{clientX:800,buttons:0});check(same(before,pos(node)),'버튼 해제 상태에서 이동');check(!canvas.classList.contains('graph-dragging'),'드래그 잔류')});
  for(const reason of ['pointercancel','lostpointercapture','blur'])test(reason+' 이후 드래그 종료',()=>{pointer(header,'pointerdown');pointer(w,'pointermove',{clientX:425});if(reason==='blur')w.dispatchEvent(new w.Event('blur'));else pointer(reason==='lostpointercapture'?canvas:w,reason);const after=pos(node);pointer(w,'pointermove',{clientX:600});check(same(after,pos(node)),'취소 이후 이동');check(!canvas.classList.contains('graph-dragging'),'드래그 잔류')});
  test('캔버스 밖에서 버튼 해제',()=>{pointer(header,'pointerdown');pointer(w,'pointermove',{clientX:-50});pointer(w,'pointerup',{clientX:-50});const after=pos(node);pointer(w,'pointermove',{clientX:700});check(same(after,pos(node)),'밖에서 해제 후 이동')});
  test('빈 공간 패닝 후 버튼 해제',()=>{pointer(canvas,'pointerdown');pointer(w,'pointermove',{clientX:430});pointer(w,'pointerup',{clientX:430});const before=d.getElementById('scene').style.transform;pointer(w,'pointermove',{clientX:700,buttons:0});check(before===d.getElementById('scene').style.transform,'해제 후 카메라 이동')});
  test('그래프 텍스트 선택 / 기본 이미지 드래그 차단',()=>{for(const type of ['selectstart','dragstart']){const e=new w.Event(type,{bubbles:true,cancelable:true});header.dispatchEvent(e);check(e.defaultPrevented,type+' 허용')}});
  test('캔버스 스크롤 / 선택 방지 스타일',()=>{check(w.getComputedStyle(canvas).userSelect==='none','user-select');check(w.getComputedStyle(canvas).overscrollBehavior==='none','overscroll');check(canvas.scrollTop===0&&canvas.scrollLeft===0,'캔버스 스크롤 잔류')});
  test('핀 클릭 연결 모드 유지',()=>{const pin=d.querySelector('[data-pin]');pointer(pin,'pointerdown');pointer(w,'pointerup');pin.click();check(!d.getElementById('connectionHint').hidden,'핀 클릭이 연결 모드를 열지 않음')});
  test('핀 드래그 후 빈 공간에 놓으면 연결 취소',()=>{const pin=d.querySelector('[data-pin]');pointer(pin,'pointerdown');pointer(w,'pointermove',{clientX:440});pointer(w,'pointerup',{clientX:0,clientY:0});check(d.getElementById('connectionHint').hidden,'연결 드래그 잔류');check(!canvas.classList.contains('graph-dragging'),'활성 상태 잔류')});
  test('Escape로 드래그 종료',()=>{pointer(header,'pointerdown');w.dispatchEvent(new w.KeyboardEvent('keydown',{key:'Escape'}));const before=pos(node);pointer(w,'pointermove',{clientX:800});check(same(before,pos(node)),'Escape 이후 이동')});
  test('노드 입력란의 편집 동작 유지',()=>{const input=d.querySelector('.node input,.node select,.node textarea');check(input,'검사할 입력란 없음');check(!pointer(input,'pointerdown').defaultPrevented,'입력란 기본 동작 차단')});
 }finally{
  for(const k of Object.keys(localStorage))if(k.startsWith('ntoskrnl-simulator-v1:')&&!saved.has(k))localStorage.removeItem(k);
  for(const [k,v]of saved)localStorage.setItem(k,v);
 }
 w.removeEventListener('error',onEventError);
 for(const row of rows){const li=document.createElement('li');li.className=row.pass?'pass':'fail';li.textContent=(row.pass?'PASS · ':'FAIL · ')+row.name+(row.error?' — '+row.error:'');list.append(li)}
 result.textContent=` ${rows.filter(r=>r.pass).length}/${rows.length} PASS`;
 button.disabled=false;
};
