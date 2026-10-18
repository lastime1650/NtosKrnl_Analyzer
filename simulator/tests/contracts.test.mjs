import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {Engine,APIS,STATUS,KernelFault,TYPES} from '../engine.js';
const raw=readFileSync(new URL('../catalog.js',import.meta.url),'utf8'),catalog=JSON.parse(raw.slice(raw.indexOf('=')+1).trim().replace(/;$/,''));
const enabled=Object.keys(APIS).filter(n=>catalog.exports.some(x=>x.id===n&&x.callable));
function fixture(){const nodes=[{id:'entry',kind:'entry'},{id:'dpcRoutine',kind:'callback'},...['process','processEx','thread','image','registry'].map(t=>({id:'handler_'+t,kind:'handler',handlerType:t}))];const e=new Engine({nodes,edges:[]},catalog,{memoryMB:4,userMemoryMB:4});e.start();const object=(t)=>e.mem.object(t),slot=(v=0n,type='LARGE_INTEGER')=>{const p=object(type);e.mem.put(p,v,TYPES[type]?.size||8);return p},string=(s,wide=false)=>e.mem.string(s,wide),unicode=s=>e.makeData({type:'UNICODE_STRING',value:s});const p=e.world.create({id:'p',initialImage:false},false),timer=object('KTIMER'),dpc=object('KDPC'),event=object('KEVENT'),spin=object('KSPIN_LOCK'),buffer=e.mem.alloc(256,'Contract'),other=e.mem.alloc(256,'Other'),out=slot(),size=slot(4096n);APIS.KeInitializeTimer.run(e,{Timer:timer});APIS.KeInitializeDpc.run(e,{Dpc:dpc,DeferredRoutine:'callback:dpcRoutine',DeferredContext:0n});APIS.KeInitializeEvent.run(e,{Event:event,Type:0n,State:0n});APIS.KeInitializeSpinLock.run(e,{SpinLock:spin});return {e,object,slot,string,unicode,p,timer,dpc,event,spin,buffer,other,out,size};}
for(const name of enabled)test('EXPORT contract: '+name,()=>{const f=fixture(),{e,object,slot,string,unicode,p,timer,dpc,event,spin,buffer,other,out,size}=f;let args={},check=()=>{};
 switch(name){
 case 'ExAllocatePool2':args={Flags:0x40n,NumberOfBytes:128n,Tag:0x41424344n};check=r=>{assert(r);assert.equal(e.mem.block(r).size,128);assert.equal(e.mem.num(r,4),0n)};break;
 case 'ExAllocatePoolWithTag':args={PoolType:512n,NumberOfBytes:128n,Tag:0x41424344n};check=r=>assert.equal(e.mem.block(r).size,128);break;
 case 'ExFreePool':args={P:buffer};check=()=>assert.equal(e.mem.block(buffer).freed,true);break;
 case 'ExFreePoolWithTag':args={P:buffer,Tag:0x4142n};e.mem.block(buffer).tag='0x4142';check=()=>assert.equal(e.mem.block(buffer).freed,true);break;
 case 'RtlZeroMemory':e.mem.put(buffer,0xFFFFFFFFn,4);args={Destination:buffer,Length:16n};check=()=>assert.equal(e.mem.num(buffer,4),0n);break;
 case 'RtlFillMemory':args={Destination:buffer,Length:16n,Fill:0x41n};check=()=>assert.equal(e.mem.num(buffer,4),0x41414141n);break;
 case 'RtlCopyMemory':case 'RtlMoveMemory':e.mem.put(other,0xABCDn,4);args={Destination:buffer,Source:other,Length:16n};check=()=>assert.equal(e.mem.num(buffer,4),0xABCDn);break;
 case 'RtlCompareMemory':args={Source1:buffer,Source2:other,Length:16n};check=r=>assert.equal(r,16n);break;
 case 'RtlInitUnicodeString':args={DestinationString:object('UNICODE_STRING'),SourceString:string('ABC',true)};check=()=>assert.equal(e.mem.num(args.DestinationString,2),6n);break;
 case 'RtlInitAnsiString':case 'RtlInitString':args={DestinationString:object('ANSI_STRING'),SourceString:string('ABC')};check=()=>assert.equal(e.mem.num(args.DestinationString,2),3n);break;
 case 'RtlEqualUnicodeString':args={String1:unicode('AbC'),String2:unicode('abc'),CaseInSensitive:1n};check=r=>assert.equal(r,1n);break;
 case 'KeGetCurrentIrql':check=r=>assert.equal(r,0n);break;
 case 'KfRaiseIrql':args={NewIrql:2n};check=r=>{assert.equal(r,0n);assert.equal(e.irql,2)};break;
 case 'KeLowerIrql':e.irql=2;args={NewIrql:0n};check=()=>assert.equal(e.irql,0);break;
 case 'KeInitializeSpinLock':args={SpinLock:spin};check=()=>assert.equal(e.mem.obj(spin).fields.locked,false);break;
 case 'KeAcquireSpinLockRaiseToDpc':args={SpinLock:spin};check=r=>{assert.equal(r,0n);assert.equal(e.irql,2);assert.equal(e.mem.obj(spin).fields.locked,true)};break;
 case 'KeReleaseSpinLock':APIS.KeAcquireSpinLockRaiseToDpc.run(e,{SpinLock:spin});args={SpinLock:spin,NewIrql:0n};check=()=>{assert.equal(e.irql,0);assert.equal(e.mem.obj(spin).fields.locked,false)};break;
 case 'KeInitializeTimer':case 'KeInitializeTimerEx':args={Timer:timer,Type:1n};check=()=>assert.equal(e.mem.obj(timer).initialized,true);break;
 case 'KeSetTimer':case 'KeSetTimerEx':args={Timer:timer,DueTime:-10000000n,Period:name.endsWith('Ex')?1000n:0n,Dpc:0n};check=r=>{assert.equal(r,0n);assert.equal(e.mem.obj(timer).fields.pending,true);assert.equal(e.queue[0].at,1000)};break;
 case 'KeCancelTimer':APIS.KeSetTimer.run(e,{Timer:timer,DueTime:-10000000n,Dpc:0n});args={Timer:timer};check=r=>{assert.equal(r,1n);assert.equal(e.mem.obj(timer).fields.pending,false)};break;
 case 'KeReadStateTimer':args={Timer:timer};check=r=>assert.equal(r,0n);break;
 case 'KeInitializeDpc':args={Dpc:dpc,DeferredRoutine:'callback:dpcRoutine',DeferredContext:0n};check=()=>assert.equal(e.mem.obj(dpc).initialized,true);break;
 case 'KeInsertQueueDpc':args={Dpc:dpc,SystemArgument1:1n,SystemArgument2:2n};check=r=>{assert.equal(r,1n);assert.equal(e.mem.obj(dpc).fields.queued,true)};break;
 case 'KeRemoveQueueDpc':APIS.KeInsertQueueDpc.run(e,{Dpc:dpc,SystemArgument1:0n,SystemArgument2:0n});args={Dpc:dpc};check=r=>{assert.equal(r,1n);assert.equal(e.mem.obj(dpc).fields.queued,false)};break;
 case 'KeInitializeEvent':args={Event:event,Type:0n,State:1n};check=()=>assert.equal(e.mem.obj(event).fields.signaled,true);break;
 case 'KeSetEvent':args={Event:event,Increment:0n,Wait:0n};check=r=>{assert.equal(r,0n);assert.equal(e.mem.obj(event).fields.signaled,true)};break;
 case 'KeResetEvent':case 'KeClearEvent':APIS.KeSetEvent.run(e,{Event:event,Increment:0n,Wait:0n});args={Event:event};check=()=>assert.equal(e.mem.obj(event).fields.signaled,false);break;
 case 'KeReadStateEvent':args={Event:event};check=r=>assert.equal(r,0n);break;
 case 'KeWaitForSingleObject':args={Object:event,WaitReason:0n,WaitMode:0n,Alertable:0n,Timeout:slot()};check=r=>assert.equal(r,STATUS.STATUS_TIMEOUT);break;
 case 'KeDelayExecutionThread':args={WaitMode:0n,Alertable:0n,Interval:slot(-10000000n)};check=r=>{assert.equal(r.waitUntil,1000);assert.equal(r.result,0n)};break;
 case 'DbgPrint':args={Format:string('contract debug output')};check=()=>assert(e.events.some(ev=>ev.kind==='debug'&&ev.message==='contract debug output'));break;
 case 'DbgBreakPoint':check=()=>assert.equal(e.breakAfter,true);break;
 case 'KeBugCheckEx':args={BugCheckCode:0xDEADn,BugCheckParameter1:1n,BugCheckParameter2:2n,BugCheckParameter3:3n,BugCheckParameter4:4n};assert.throws(()=>APIS[name].run(e,args),error=>error instanceof KernelFault&&error.code===0xDEAD);return;
 case 'KeQueryTimeIncrement':check=r=>assert(r>0n);break;
 case 'KeQueryPerformanceCounter':e.time=1234;args={PerformanceFrequency:out};check=r=>{assert.equal(r,12340000n);assert.equal(e.mem.num(out),10000000n)};break;
 case 'KeQuerySystemTimePrecise':args={CurrentTime:out};check=()=>assert.equal(e.mem.num(out),e.epoch);break;
 case 'MmMapIoSpace':case 'MmMapIoSpaceEx':args={PhysicalAddress:0xF0000000n,NumberOfBytes:4096n,Protect:4n,CacheType:0n};check=r=>assert.equal(e.hardware.mappings[0].pointer,r);break;
 case 'MmUnmapIoSpace':args={BaseAddress:APIS.MmMapIoSpaceEx.run(e,{PhysicalAddress:0xF0000000n,NumberOfBytes:4096n,Protect:4n}),NumberOfBytes:4096n};check=()=>assert.equal(e.hardware.mappings.length,0);break;
 case 'MmIsAddressValid':args={VirtualAddress:buffer};check=r=>assert.equal(r,1n);break;
 case 'IoCreateDevice':args={DriverObject:e.entryAlias,DeviceExtensionSize:64n,DeviceName:0n,DeviceType:0x22n,DeviceCharacteristics:0n,Exclusive:0n,DeviceObject:out};check=r=>{assert.equal(r,0n);assert.equal(e.mem.obj(e.mem.num(out)).type,'DEVICE_OBJECT')};break;
 case 'IoDeleteDevice':APIS.IoCreateDevice.run(e,{DriverObject:e.entryAlias,DeviceExtensionSize:64n,DeviceName:0n,DeviceType:0x22n,DeviceCharacteristics:0n,Exclusive:0n,DeviceObject:out});args={DeviceObject:e.mem.num(out)};check=()=>assert.equal(e.devices.length,0);break;
 case 'IoCreateSymbolicLink':args={SymbolicLinkName:unicode('\\DosDevices\\Demo'),DeviceName:unicode('\\Device\\Demo')};check=r=>{assert.equal(r,0n);assert.equal(e.links.get('\\DosDevices\\Demo'),'\\Device\\Demo')};break;
 case 'IoDeleteSymbolicLink':e.links.set('\\DosDevices\\Demo','\\Device\\Demo');args={SymbolicLinkName:unicode('\\DosDevices\\Demo')};check=r=>{assert.equal(r,0n);assert.equal(e.links.size,0)};break;
 case 'KeStackAttachProcess':args={PROCESS:p.pointer,ApcState:object('KAPC_STATE')};check=()=>assert.equal(e.world.currentPid,p.pid);break;
 case 'KeUnstackDetachProcess':args={ApcState:object('KAPC_STATE')};APIS.KeStackAttachProcess.run(e,{PROCESS:p.pointer,...args});check=()=>assert.equal(e.world.currentPid,4n);break;
 case 'PsGetCurrentProcess':check=r=>assert.equal(r,e.world.processes.get(4n).pointer);break;
 case 'PsGetCurrentProcessId':check=r=>assert.equal(r,4n);break;
 case 'PsGetProcessId':args={Process:p.pointer};check=r=>assert.equal(r,p.pid);break;
 case 'PsLookupProcessByProcessId':args={ProcessId:p.pid,Process:out};check=r=>{assert.equal(r,0n);assert.equal(e.mem.num(out),p.pointer);assert.equal(p.lookupRefs,1)};break;
 case 'ObfDereferenceObject':APIS.PsLookupProcessByProcessId.run(e,{ProcessId:p.pid,Process:out});args={Object:p.pointer};check=()=>assert.equal(p.lookupRefs,0);break;
 case 'ZwOpenProcess':{const oa=object('OBJECT_ATTRIBUTES'),cid=object('CLIENT_ID');e.mem.put(oa,48,4);e.mem.put(oa+24n,0x200,4);e.mem.put(cid,p.pid);args={ProcessHandle:out,DesiredAccess:8n,ObjectAttributes:oa,ClientId:cid};check=r=>{assert.equal(r,0n);assert.equal(e.world.fromHandle(e.mem.num(out)).pid,p.pid)};break;}
 case 'ZwClose':args={Handle:e.world.open(p)};check=r=>{assert.equal(r,0n);assert.equal(e.world.handles.get(args.Handle).closed,true)};break;
 case 'ZwAllocateVirtualMemory':args={ProcessHandle:p.handle,BaseAddress:out,ZeroBits:0n,RegionSize:size,AllocationType:0x3000n,Protect:4n};check=r=>{assert.equal(r,0n);assert.equal(p.vm.committed,4096)};break;
 case 'ZwFreeVirtualMemory':case 'ZwProtectVirtualMemory':{APIS.ZwAllocateVirtualMemory.run(e,{ProcessHandle:p.handle,BaseAddress:out,ZeroBits:0n,RegionSize:size,AllocationType:0x3000n,Protect:4n});if(name==='ZwFreeVirtualMemory'){e.mem.put(size,0n);args={ProcessHandle:p.handle,BaseAddress:out,RegionSize:size,FreeType:0x8000n};check=r=>{assert.equal(r,0n);assert.equal(p.vm.reservations.length,0)}}else{args={ProcessHandle:p.handle,BaseAddress:out,RegionSize:size,NewProtection:2n,OldProtection:slot(0n,'ULONG32')};check=r=>{assert.equal(r,0n);assert.equal(e.mem.num(args.OldProtection,4),4n)}}break;}
 case 'PsSetCreateProcessNotifyRoutine':case 'PsSetCreateProcessNotifyRoutineEx':case 'PsSetCreateThreadNotifyRoutine':case 'PsSetLoadImageNotifyRoutine':{const type=name==='PsSetCreateProcessNotifyRoutine'?'process':name.endsWith('Ex')?'processEx':name.includes('Thread')?'thread':'image';args={NotifyRoutine:'callback:handler_'+type,Remove:0n};check=r=>{assert.equal(r,0n);assert(e.world.registrations.some(v=>v.type===type&&v.active))};break;}
 case 'PsRemoveCreateThreadNotifyRoutine':case 'PsRemoveLoadImageNotifyRoutine':{const type=name.includes('Thread')?'thread':'image';e.world.register(type,'callback:handler_'+type);args={NotifyRoutine:'callback:handler_'+type};check=r=>{assert.equal(r,0n);assert.equal(e.world.registrations[0].active,false)};break;}
 case 'CmRegisterCallback':case 'CmRegisterCallbackEx':args={Function:'callback:handler_registry',Altitude:unicode('385200.1'),Driver:e.entryAlias,Context:0x1234n,Cookie:out,Reserved:0n};check=r=>{assert.equal(r,0n);assert.equal(e.mem.num(out),1n)};break;
 case 'CmUnRegisterCallback':args={Cookie:e.world.register('registry','callback:handler_registry')};check=r=>{assert.equal(r,0n);assert.equal(e.world.registrations[0].active,false)};break;
 default:assert.fail('No independent contract fixture for '+name);
 }
 const result=APIS[name].run(e,args);check(result);
});
