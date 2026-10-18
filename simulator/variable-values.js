export const isStringType=(type,types)=>!!types[type]?.string;
export const isNumericType=(type,types)=>!!types[type]?.scalar;
const key=p=>'0x'+BigInt(p).toString(16).toUpperCase();
export function installVariableTypes(types){
 const signed={CHAR:1,SHORT:2,INT:4,INT32:4,INT64:8,LONGLONG:8,LONG_PTR:8,SSIZE_T:8};
 const unsigned={BYTE:1,WORD:2,DWORD:4,UINT:4,UINT32:4,UINT64:8,ULONGLONG:8,UINT_PTR:8,BOOLEAN:1};
 for(const [name,size]of Object.entries(signed))types[name]??={size,scalar:true,signed:true};
 for(const [name,size]of Object.entries(unsigned))types[name]??={size,scalar:true};
 types.PVOID.pointerTo='VOID';
 for(const name of Object.keys(types))if(!types[name].pointerTo)types['P'+name]??={size:8,scalar:true,pointerTo:name};
 for(const [name,target]of Object.entries({PCSTR:'ANSI',PSTR:'ANSI',PCHAR:'ANSI',PCSZ:'ANSI',PCWSTR:'WCHAR',PWSTR:'WCHAR',PWCHAR:'WCHAR',PCUNICODE_STRING:'UNICODE_STRING',PCANSI_STRING:'ANSI_STRING',PPVOID:'PVOID'}))types[name]={size:8,scalar:true,pointerTo:target};
}
export function initialObject(initial){if(initial===undefined||initial===''||initial==='0'||initial===0)return {};const value=typeof initial==='string'?JSON.parse(initial):initial;if(!value||Array.isArray(value)||typeof value!=='object')throw Error('구조체 초기값은 JSON 객체 또는 0이어야 합니다.');return value;}
export function valueFields(type,types,config={}){
 const t=types[type];if(!t)return [];
 if(t.custom){let fields=config.customFields??{Field0:{offset:0,width:4,value:'0'}};if(typeof fields==='string')fields=JSON.parse(fields);if(!fields||typeof fields!=='object'||Array.isArray(fields)||Object.keys(fields).length>64)throw Error('사용자 필드 정의는 최대 64개의 JSON 객체입니다.');return Object.entries(fields).map(([name,f])=>{if(!/^[A-Za-z_][A-Za-z0-9_]{0,79}$/.test(name)||!f||![1,2,4,8].includes(f.width)||!Number.isInteger(f.offset)||f.offset<0)throw Error('사용자 필드는 이름 / offset / width(1,2,4,8)가 필요합니다.');return {name,offset:f.offset,size:f.width,type:f.type||({1:'UCHAR',2:'USHORT',4:'ULONG32',8:'ULONG64'}[f.width]),initial:f.value??'0'}})}
 return Object.entries(t.fields||{}).map(([name,[fieldType,offset]])=>({name,type:fieldType,offset,size:types[fieldType]?.size||8,initial:t.defaults?.[name]??'0'}));
}
export function valueLayout(type,initial,types,config={}){
 const t=types[type];if(!t)throw Error('알 수 없는 자료형: '+type);
 if(t.scalar)return {size:t.size,alignment:Math.min(t.size,8),fields:[]};
 if(t.string){const wide=t.string==='wide'||t.string==='unicode',unit=wide?2:1,limit=wide?32767:65535,text=String(initial??'');const capacity=config.capacity===undefined?Math.max(256,text.length+1):Number(config.capacity);if(!Number.isInteger(capacity)||capacity<1||capacity>limit)throw Error('문자열 용량은 1–'+limit+' '+(wide?'UTF-16 단위':'바이트')+'입니다.');if(text.length>=capacity)throw Error('문자열 초기값과 종료 문자가 버퍼 용량을 초과했습니다.');if(!wide&&[...text].some(c=>c.charCodeAt(0)>255))throw Error('ANSI는 단일 바이트 문자입니다. 한글은 WCHAR / UNICODE_STRING을 선택하세요.');return {size:t.size||capacity*unit,alignment:t.size?8:unit,capacity,unit,fields:valueFields(type,types,config)}}
 const size=t.custom?Number(config.customSize??64):t.size,fields=valueFields(type,types,config);if(!Number.isInteger(size)||size<1||size>1048576)throw Error('객체 크기는 1–1048576 바이트입니다.');
 const used=[];for(const f of fields){if(!types[f.type]?.scalar||types[f.type].size!==f.size||f.offset+f.size>size||used.some(x=>f.offset<x[1]&&f.offset+f.size>x[0]))throw Error('필드 크기 / 오프셋 / 겹침을 확인하세요.');used.push([f.offset,f.offset+f.size])}
 return {size,alignment:Math.min(8,Math.max(t.opaque?8:1,...fields.map(f=>Math.min(f.size,8)))),fields,...(t.custom?{customSize:size,customFields:config.customFields??{Field0:{offset:0,width:4,value:'0'}}}:{})};
}
export function validateInitial(type,initial,types,literal,config={}){
 const t=types[type];valueLayout(type,initial,types,config);
 if(t.scalar){if(typeof literal(initial??0)!=='bigint')throw Error('정수 / 상수 / 포인터 초기값이 필요합니다.');return;}
 if(t.string)return;
 const obj=initialObject(initial);if(t.opaque&&Object.keys(obj).length)throw Error('opaque 커널 객체는 0으로 만들고 전용 API로 초기화하세요.');
 const fields=valueFields(type,types,config),names=new Set(fields.map(f=>f.name));for(const name of Object.keys(obj))if(!names.has(name))throw Error('정의되지 않은 구조체 필드: '+name);
 for(const f of fields)if(typeof literal(obj[f.name]??f.initial)!=='bigint')throw Error('구조체 필드 초기값은 정수 / 상수 / 포인터입니다.');
}
function stringBytes(text,wide){const bytes=new Uint8Array(text.length*(wide?2:1));for(let i=0;i<text.length;i++){const value=text.charCodeAt(i);if(!wide&&value>255)throw Error('ANSI에 표현할 수 없는 문자입니다.');bytes[i*(wide?2:1)]=value&255;if(wide)bytes[i*2+1]=value>>8}return bytes;}
function decode(bytes,wide){let text='';for(let i=0;i+(wide?1:0)<bytes.length;i+=wide?2:1)text+=String.fromCharCode(bytes[i]|(wide?bytes[i+1]<<8:0));return text;}
function stringValue(e,c,address,types,preview=false){
 const t=types[c.type],wide=t.string==='wide'||t.string==='unicode';
 if(t.size){const length=Number(e.mem.num(address,2)),maximum=Number(e.mem.num(address+2n,2)),buffer=e.mem.num(address+8n);if(length>maximum||wide&&length%2)throw Error('문자열 Length / MaximumLength가 올바르지 않습니다.');if(preview&&buffer&&buffer<e.mem.base)return {Text:'(유저 버퍼: 실행 시 주소 공간 검사)',Length:BigInt(length),MaximumLength:BigInt(maximum),Buffer:buffer};const text=length?decode(e.mem.read(buffer,length),wide):'';return {Text:text,Length:BigInt(length),MaximumLength:BigInt(maximum),Buffer:buffer};}
 const bytes=e.mem.read(address,c.size);let end=0;for(;end+(wide?1:0)<bytes.length;end+=wide?2:1)if(!bytes[end]&&(!wide||!bytes[end+1]))break;return decode(bytes.slice(0,end),wide);
}
export function readCell(e,c,address,types,coerce,preview=false){
 const t=types[c.type];if(t.scalar)return coerce(e.mem.num(address,c.size),c.type);
 if(t.string)return stringValue(e,c,address,types,preview);
 if(t.opaque){const o=e.mem.obj(address,c.type);return {Type:c.type,Initialized:!!o.initialized,...structuredClone(o.fields)}}
 return Object.fromEntries(c.fields.map(f=>[f.name,coerce(e.mem.num(address+BigInt(f.offset),f.size),f.type)]));
}
export function initializeCell(e,c,address,types,coerce,owned){
 const t=types[c.type];if(t.scalar){e.mem.put(address,coerce(e.literal(c.initial??0),c.type),c.size);return;}
 e.mem.objects.set(key(address),{type:c.type,fields:{},initialized:!t.opaque,address});
 if(t.string){if(t.size){c.buffer=e.mem.object('VARIABLE_STRING_BUFFER',{},c.capacity*c.unit);owned.add(e.mem.block(c.buffer).id);}writeText(e,c,address,types,String(c.initial??''));return;}
 const obj=initialObject(c.initial);for(const f of c.fields)e.mem.put(address+BigInt(f.offset),e.literal(obj[f.name]??f.initial),f.size);
 if(!t.opaque)e.mem.obj(address).fields=readCell(e,c,address,types,coerce);
}
function writeText(e,c,address,types,text){
 const t=types[c.type],bytes=stringBytes(text,c.unit===2),capacity=c.capacity*c.unit;
 if(bytes.length+c.unit>capacity)throw Error('문자열 쓰기가 용량을 초과했습니다: '+bytes.length+' bytes / '+capacity+' bytes');
 const data=new Uint8Array(capacity);data.set(bytes);const buffer=t.size?c.buffer:address;e.mem.write(buffer,data);
 if(t.size){e.mem.put(address,bytes.length,2);e.mem.put(address+2n,capacity,2);e.mem.put(address+8n,buffer);e.mem.obj(address).fields={Length:BigInt(bytes.length),MaximumLength:BigInt(capacity),Buffer:buffer};}
}
export function assignCell(e,c,address,types,coerce,source){
 const t=types[c.type];if(t.scalar){e.mem.put(address,coerce(source,c.type),c.size);return;}
 if(t.opaque)throw Error('활성 커널 객체를 값으로 복사할 수 없습니다. Address / Value 핀을 전용 초기화 API에 연결하세요.');
 if(t.string){const value=source?(t.size?stringValue(e,c,BigInt(source),types):e.mem.cstring(BigInt(source),c.unit===2)):'';writeText(e,c,address,types,typeof value==='string'?value:value.Text);return;}
 const bytes=source?e.mem.read(BigInt(source),c.size):new Uint8Array(c.size);e.mem.write(address,bytes);if(!t.opaque)e.mem.obj(address).fields=readCell(e,c,address,types,coerce);
}
