const esc=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
export class InternalView{
 constructor(canvas,catalog,apis,fmt){
  Object.assign(this,{canvas,catalog,apis,fmt,active:false,tab:'model',trail:[],cache:new Map(),request:0});
  this.layer=document.createElement('section');this.layer.className='internal-view';this.layer.hidden=true;this.layer.setAttribute('aria-label','읽기 전용 커널 내부 그래프');canvas.append(this.layer);
  this.layer.addEventListener('pointerdown',e=>e.stopPropagation());this.layer.addEventListener('wheel',e=>e.stopPropagation());this.layer.addEventListener('contextmenu',e=>{e.preventDefault();e.stopPropagation()});
  this.layer.addEventListener('dragstart',e=>e.preventDefault());
 }
 close(){this.request++;this.active=false;this.layer.hidden=true;this.canvas.classList.remove('viewing-internals');}
 open(e){if(!e.stage)return;this.e=e;this.root=e.node(e.current);this.active=true;this.tab='model';this.trail=[];this.layer.hidden=false;this.canvas.classList.add('viewing-internals');this.render();}
 sync(e){this.e=e;if(!this.active)return;if(!e.stage||e.node(e.current)?.id!==this.root.id){this.close();return}this.render();}
 async loadIndex(){if(!this.index){const response=await fetch('internal-index.json');if(!response.ok)throw Error('내부 CFG 인덱스가 없습니다. 프로젝트 분석을 다시 생성하세요.');const value=await response.json();if(value.sha256!==this.catalog.sha256)throw Error('다른 커널 이미지의 내부 그래프입니다.');this.index=value.functions;}return this.index;}
 async load(rva){if(!this.cache.has(rva)){const index=await this.loadIndex(),entry=index[rva];if(!entry)throw Error('이 호출 대상의 CFG는 현재 분석 결과에 없습니다.');const response=await fetch('internal-graphs/'+entry.file);if(!response.ok)throw Error('내부 CFG 읽기 실패');const data=await response.json();if(data.sha256!==this.catalog.sha256||data.rva!==rva||data.readonly!==true)throw Error('내부 CFG 이미지 / RVA 검증 실패');this.cache.set(rva,data);}return this.cache.get(rva);}
 render(){
  const scroll=this.layer.querySelector('.internal-scroll'),top=scroll?.scrollTop||0,left=scroll?.scrollLeft||0;
  const e=this.e,n=this.root,api=this.apis[n.api],liveArgs=e.stage?.args||{},entry=this.catalog.exports.find(x=>x.id===n.api);
  this.layer.innerHTML=`<header class="internal-toolbar"><b>🔒 nt!${esc(n.api)}</b><span>READ ONLY</span><button data-internal-close>드라이버 그래프로 복귀</button></header><nav class="internal-tabs"><button data-internal-tab="model" class="${this.tab==='model'?'active':''}">실행 모델 노드</button><button data-internal-tab="binary" class="${this.tab==='binary'?'active':''}">바이너리 CFG / ASM</button></nav><div class="internal-caption">${this.tab==='model'?(api.phaseRun?'API 계약의 단계별 실행입니다. 검사 → 예약 → 초기화의 메모리 변화를 Step Into로 확인하세요.':'API 계약 단계 표시입니다. 이 API의 검증과 메모리 변경은 마지막 모델 단계에서 함께 적용합니다.'):'동일 PE/PDB의 정적 기본 블록 / 호출 후보입니다. 이 CFG의 분기는 현재 CPU 실행 기록이 아닙니다.'}</div><div class="internal-call-values" aria-label="현재 내부 호출 인자">${Object.entries(liveArgs).map(([k,v])=>'<span>'+esc(k)+' <code>'+esc(this.fmt(v))+'</code></span>').join('')}${e.stage?.poolPointer?'<span>예약 포인터 <code>'+esc(this.fmt(e.stage.poolPointer))+'</code></span>':''}</div><div class="internal-scroll"></div>`;
  this.layer.querySelector('[data-internal-close]').onclick=()=>this.close();
  this.layer.querySelectorAll('[data-internal-tab]').forEach(b=>b.onclick=()=>{this.tab=b.dataset.internalTab;if(!this.trail.length&&entry)this.trail=[entry.rva];this.render()});
  const target=this.layer.querySelector('.internal-scroll');
  if(this.tab==='model'){
   const args=e.stage?.args||{},index=e.stage?.index||0,fault=e.error?.node===n.id,active=fault?index:index+1,items=[{name:'EXPORT 진입 · '+n.api,detail:entry?.rva||''},...api.phases.map(name=>({name,detail:api.phaseRun?'단계별 계약 실행 · 비공개 nt 함수 이름을 가정하지 않음':'계약 단계 표시 · 실제 변경은 마지막 단계에서 적용'})),{name:'호출자에게 복귀',detail:e.stage?.result!==undefined?'Return = '+this.fmt(e.stage.result):'반환값 계산 대기'}];
   target.innerHTML=`<div class="internal-model-graph">${items.map((item,i)=>`<article class="internal-model-node ${i===active?(fault?'fault':'next'):''} ${i<active?'done':''}" aria-label="내부 단계 ${i}: ${esc(item.name)}"><small>${i===active?(fault?'■ 오류 중단 · ':'▶ 다음 실행 · '):i<active?'✓ 완료 · ':''}READ ONLY</small><b>${esc(item.name)}</b><p>${esc(item.detail)}</p></article>`).join('<div class="internal-flow-arrow">↓</div>')}</div>`;
  }else{
   target.innerHTML='<p class="internal-loading">바이너리 CFG를 읽는 중…</p>';
   const token=++this.request,rva=this.trail.at(-1)||entry?.rva;
   this.load(rva).then(graph=>{if(token!==this.request||!this.active||this.tab!=='binary')return;this.renderBinary(target,graph);target.scrollTop=top;target.scrollLeft=left}).catch(error=>{if(token===this.request)target.textContent=error.message});
  }
  target.scrollTop=top;target.scrollLeft=left;if(this.tab==='model'){const current=target.querySelector('.internal-model-node.next,.internal-model-node.fault');if(current)target.scrollTop+=current.getBoundingClientRect().top-target.getBoundingClientRect().top-8;}
 }
 renderBinary(target,graph){
  const nodes=graph.nodes.slice(0,600),ids=new Map(nodes.map((n,i)=>[n.id,i])),edges=graph.edges.filter(e=>ids.has(e.source)&&ids.has(e.target)),width=760,height=Math.max(360,nodes.length*158+60);
  const paths=edges.map((edge,i)=>{const from=ids.get(edge.source),to=ids.get(edge.target),y=from*158+118,y2=to*158+35,lane=590+(i%18)*8;return `<path d="M570 ${y} H${lane} V${y2} H570" class="binary-edge ${esc(edge.kind)}"><title>${esc(edge.kind+' · '+edge.source+' → '+edge.target)}</title></path>`}).join('');
  target.innerHTML=`<div class="internal-breadcrumb"><button data-binary-root>EXPORT CFG</button>${this.trail.length>1?'<button data-binary-back>← 이전 호출 대상</button>':''}<b>${esc(graph.name)} · ${esc(graph.rva)}</b></div><p class="internal-static-note"><a href="${esc(graph.report)}" target="_blank" rel="noopener">분석 보고서 ↗</a> · ${graph.blocks} 기본 블록 · ${graph.calls} 정적 호출 지점 · 주소 순서 배치 · 간접 호출 대상은 확정하지 않습니다.${graph.nodes.length>600?' 큰 그래프: 앞 600개 노드 표시. 전체는 분석 보고서를 확인하세요.':''}</p><div class="binary-graph" style="width:${width}px;height:${height}px"><svg width="${width}" height="${height}" aria-label="내부 정적 연결">${paths}</svg>${nodes.map((node,i)=>{const match=/0x[0-9A-Fa-f]{8}/.exec(node.label||''),rva=node.kind==='call'?match?.[0]?.toUpperCase().replace('0X','0x'):null;return `<article class="binary-node ${esc(node.kind)}" style="top:${i*158+12}px" aria-label="${esc(node.label)}"><b>${esc(node.label)}</b><pre>${esc((node.detail||'').split('\n').slice(0,3).join('\n'))}</pre><button data-binary-detail="${esc(node.id)}">ASM / 상세</button>${rva?`<button data-binary-call="${esc(rva)}">호출 대상 CFG 열기 →</button>`:''}</article>`}).join('')}</div><dialog class="internal-asm-dialog"><button data-asm-close>닫기</button><pre></pre></dialog>`;
  target.querySelector('[data-binary-root]').onclick=()=>{target.scrollTop=0;this.trail=this.trail.slice(0,1);this.render()};
  if(target.querySelector('[data-binary-back]'))target.querySelector('[data-binary-back]').onclick=()=>{target.scrollTop=0;this.trail.pop();this.render()};
  target.querySelectorAll('[data-binary-call]').forEach(b=>b.onclick=()=>{target.scrollTop=0;this.trail.push(b.dataset.binaryCall);this.render()});
  const dialog=target.querySelector('dialog');target.querySelector('[data-asm-close]').onclick=()=>dialog.close();
  target.querySelectorAll('[data-binary-detail]').forEach(b=>b.onclick=()=>{dialog.querySelector('pre').textContent=graph.nodes.find(n=>n.id===b.dataset.binaryDetail)?.detail||'';dialog.showModal()});
 }
}
