# sub_002142F9

- RVA: `0x002142F9`–`0x00214DD7` (길이 `2,782` bytes)
- VA: `0x00000001402142F9`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005E128`
- 디코드: `653`개 명령, `2,782/2,782` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **62**; 고유 호출 대상: **29**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **14**

### Outgoing calls
- `0x0021431D` → [KiAcquireQueuedSpinLockInstrumented](../27/KiAcquireQueuedSpinLockInstrumented_function_00275850.md) (function, `0x00275850`)
- `0x0021433D` → [KiReleaseQueuedSpinLockInstrumented](KiReleaseQueuedSpinLockInstrumented_function_002179F0.md) (function, `0x002179F0`)
- `0x00214357` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x00214374` → [IoBoostThreadIoPriority](IoBoostThreadIoPriority_function_00216110.md) (function, `0x00216110`)
- `0x00214398` → [ExAcquireRundownProtection](ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00214480` → [KiSetPriorityBoost](../39/KiSetPriorityBoost_function_00398A40.md) (function, `0x00398A40`)
- `0x002144BC` → [KiDeferredReadySingleThread](../25/KiDeferredReadySingleThread_function_00252FE0.md) (function, `0x00252FE0`)
- `0x002144E1` → [KiFlushSoftwareInterruptBatch](../25/KiFlushSoftwareInterruptBatch_function_00252200.md) (function, `0x00252200`)
- `0x00214505` → [KiAcquireQueuedSpinLockInstrumented](../27/KiAcquireQueuedSpinLockInstrumented_function_00275850.md) (function, `0x00275850`)
- `0x00214516` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x0021464C` → [ObfReferenceObjectWithTag](ObfReferenceObjectWithTag_function_00210710.md) (function, `0x00210710`)
- `0x00214655` → [KeReleaseInStackQueuedSpinLock](../34/KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)
- `0x0021466E` → [IoBoostThreadIoPriority](IoBoostThreadIoPriority_function_00216110.md) (function, `0x00216110`)
- `0x0021467C` → [PsBoostThreadOutstandingIoQoS](PsBoostThreadOutstandingIoQoS_function_00215C54.md) (function, `0x00215C54`)
- `0x0021474B` → [KiSetPriorityBoost](../39/KiSetPriorityBoost_function_00398A40.md) (function, `0x00398A40`)
- `0x00214789` → [KiDeferredReadySingleThread](../25/KiDeferredReadySingleThread_function_00252FE0.md) (function, `0x00252FE0`)
- `0x002147AF` → [KiFlushSoftwareInterruptBatch](../25/KiFlushSoftwareInterruptBatch_function_00252200.md) (function, `0x00252200`)
- `0x002147C8` → [KiFlushSoftwareInterruptBatch](../25/KiFlushSoftwareInterruptBatch_function_00252200.md) (function, `0x00252200`)
- `0x002147D4` → [KiCheckForThreadDispatch](../25/KiCheckForThreadDispatch_function_00250648.md) (function, `0x00250648`)
- `0x002147F5` → [ObpPushStackInfo](ObpPushStackInfo_function_002109E4.md) (function, `0x002109E4`)
- `0x002148A8` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x002148B9` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x002148DA` → [KiAcquireQueuedSpinLockInstrumented](../27/KiAcquireQueuedSpinLockInstrumented_function_00275850.md) (function, `0x00275850`)
- `0x00214901` → [KxWaitForLockOwnerShip](../25/KxWaitForLockOwnerShip_function_00257EB0.md) (function, `0x00257EB0`)
- `0x00214920` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x00214940` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0021494F` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00214960` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x00214975` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x00214983` → [KxWaitForLockOwnerShip](../25/KxWaitForLockOwnerShip_function_00257EB0.md) (function, `0x00257EB0`)
- `0x002149A2` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x002149C2` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x002149D2` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x002149E0` → [KxWaitForLockOwnerShip](../25/KxWaitForLockOwnerShip_function_00257EB0.md) (function, `0x00257EB0`)
- `0x00214A11` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00214A3E` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00214A78` → [KiAbThreadInsertList](KiAbThreadInsertList_function_0021F0E0.md) (function, `0x0021F0E0`)
- `0x00214A84` → [KiAbQueueAutoBoostDpc](../20/KiAbQueueAutoBoostDpc_function_002074D0.md) (function, `0x002074D0`)
- `0x00214A9A` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x00214AE9` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00214B23` → [KiAbThreadInsertList](KiAbThreadInsertList_function_0021F0E0.md) (function, `0x0021F0E0`)
- `0x00214B2F` → [KiAbQueueAutoBoostDpc](../20/KiAbQueueAutoBoostDpc_function_002074D0.md) (function, `0x002074D0`)
- `0x00214B45` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x00214B95` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00214BA2` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x00214BBA` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00214BD5` → [RtlCaptureStackBackTrace](../2F/RtlCaptureStackBackTrace_function_002F9FF0.md) (function, `0x002F9FF0`)
- `0x00214BF6` → [KeAcquireSpinLockRaiseToDpc](../20/KeAcquireSpinLockRaiseToDpc_function_00208470.md) (function, `0x00208470`)
- `0x00214C39` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x00214C51` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00214C70` → [RtlCaptureStackBackTrace](../2F/RtlCaptureStackBackTrace_function_002F9FF0.md) (function, `0x002F9FF0`)
- `0x00214C91` → [KeAcquireSpinLockRaiseToDpc](../20/KeAcquireSpinLockRaiseToDpc_function_00208470.md) (function, `0x00208470`)
- `0x00214CDE` → [KxReleaseSpinLock](../20/KxReleaseSpinLock_function_00206670.md) (function, `0x00206670`)
- `0x00214CF4` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x00214D0A` → [ObpDeferObjectDeletion](../3A/ObpDeferObjectDeletion_function_003A2394.md) (function, `0x003A2394`)
- `0x00214D18` → [ObpDeferObjectDeletion](../3A/ObpDeferObjectDeletion_function_003A2394.md) (function, `0x003A2394`)
- `0x00214D58` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x00214D78` → [KiReleaseSpinLockInstrumented](../39/KiReleaseSpinLockInstrumented_function_00392EF0.md) (function, `0x00392EF0`)
- `0x00214D86` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00214DAF` → [ExfReleaseRundownProtection](../34/ExfReleaseRundownProtection_function_00349EB0.md) (function, `0x00349EB0`)
- `0x00214DBE` → [KeAbProcessEffectiveIoPriorityChange](../41/KeAbProcessEffectiveIoPriorityChange_function_0041FC60.md) (function, `0x0041FC60`)
- `0x00214DCD` → [KeAbProcessEffectiveIoPriorityChange](../41/KeAbProcessEffectiveIoPriorityChange_function_0041FC60.md) (function, `0x0041FC60`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00214308` → RVA `0x00F0DE58` (`.data`; read)
- `0x00214342` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x00214366` → RVA `0x00E685AC` (`.data`; read/write)
- `0x00214388` → RVA `0x00F8D130` (`.data`; read)
- `0x002143C3` → RVA `0x00FCFF00` (`CACHEALI`; read)
- `0x0021443B` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x00214464` → RVA `0x00FC6C4C` (`ALMOSTRO`; read)
- `0x002145AB` → RVA `0x00FC6F88` (`ALMOSTRO`; read)
- `0x00214660` → RVA `0x00E685B0` (`.data`; read/write)
- `0x002147DC` → RVA `0x00FC5010` (`ALMOSTRO`; read)
- `0x0021483B` → RVA `0x00FC6B06` (`ALMOSTRO`; read)
- `0x00214932` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)
- `0x00214AD4` → RVA `0x00FC6E4C` (`ALMOSTRO`; read)
- `0x00214ADE` → RVA `0x00FC7800` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00214BBA` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
  - `0x00214C51` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **26**
  - `0x002142FD` → [sub_00213F4F + 0x2E3](Unknown_function_00213F4F.md) (`tail-transfer`)
  - `0x00214303` → [sub_00213F4F + 0xFC](Unknown_function_00213F4F.md) (`tail-transfer`)
  - `0x00214310` → [sub_00213F4F + 0x97](Unknown_function_00213F4F.md) (`tail-transfer`)
  - `0x00214322` → [sub_00213F4F + 0xA7](Unknown_function_00213F4F.md) (`tail-transfer`)
  - `0x0021432F` → [sub_00213F4F + 0x1E8](Unknown_function_00213F4F.md) (`tail-transfer`)
  - `0x002143B5` → [sub_00213F4F + 0x25C](Unknown_function_00213F4F.md) (`tail-transfer`)
  - `0x002143D6` → [sub_00213F4F + 0x25C](Unknown_function_00213F4F.md) (`tail-transfer`)
  - `0x0021449E` → [sub_00213F4F + 0x240](Unknown_function_00213F4F.md) (`tail-transfer`)
  - `0x002144EB` → [sub_00213F4F + 0x240](Unknown_function_00213F4F.md) (`tail-transfer`)
  - `0x002144F8` → [sub_00213F4F + 0x2CF](Unknown_function_00213F4F.md) (`tail-transfer`)
  - `0x0021450A` → [sub_00213F4F + 0x2DF](Unknown_function_00213F4F.md) (`tail-transfer`)
  - `0x0021451B` → [sub_00213F4F + 0x86](Unknown_function_00213F4F.md) (`tail-transfer`)
  - `0x00214527` → [sub_00213F4F + 0x2F0](Unknown_function_00213F4F.md) (`tail-transfer`)
  - `0x0021453A` → [sub_00213F4F + 0x2F0](Unknown_function_00213F4F.md) (`tail-transfer`)
  - `0x0021485F` → [sub_00213F4F + 0x2F3](Unknown_function_00213F4F.md) (`tail-transfer`)
  - `0x00214871` → [sub_00213F4F + 0x2F3](Unknown_function_00213F4F.md) (`tail-transfer`)
  - `0x002148AD` → [sub_00213F4F + 0x2BE](Unknown_function_00213F4F.md) (`tail-transfer`)
  - `0x002148F0` → [sub_00213F4F + 0x43](Unknown_function_00213F4F.md) (`tail-transfer`)
  - `0x002148F8` → [sub_00213F4F + 0x41](Unknown_function_00213F4F.md) (`tail-transfer`)
  - `0x00214906` → [sub_00213F4F + 0xA7](Unknown_function_00213F4F.md) (`tail-transfer`)
  - `0x0021492D` → [sub_00213F4F + 0x258](Unknown_function_00213F4F.md) (`tail-transfer`)
  - `0x00214988` → [sub_00213F4F + 0x2DF](Unknown_function_00213F4F.md) (`tail-transfer`)
  - `0x00214AAB` → [sub_00213F4F + 0x1A5](Unknown_function_00213F4F.md) (`tail-transfer`)
  - `0x00214D0F` → [sub_00213F4F + 0x297](Unknown_function_00213F4F.md) (`tail-transfer`)
  - `0x00214D65` → [sub_00213F4F + 0x15F](Unknown_function_00213F4F.md) (`tail-transfer`)
  - `0x00214DC3` → [sub_00213F4F + 0x168](Unknown_function_00213F4F.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002142F9  40 F6 C7 03                     test dil, 3
002142FD  0F 85 2F FF FF FF               jne 0x140214232
00214303  E9 43 FD FF FF                  jmp 0x14021404b
00214308  8B 05 4A 9B CF 00               mov eax, dword ptr [rip + 0xcf9b4a]
0021430E  85 C0                           test eax, eax
00214310  0F 85 D0 FC FF FF               jne 0x140213fe6
00214316  48 8B D7                        mov rdx, rdi
00214319  48 8D 4D D7                     lea rcx, [rbp - 0x29]
0021431D  E8 2E 15 06 00                  call 0x140275850
00214322  E9 CF FC FF FF                  jmp 0x140213ff6
00214327  8B 05 2B 9B CF 00               mov eax, dword ptr [rip + 0xcf9b2b]
0021432D  85 C0                           test eax, eax
0021432F  0F 85 02 FE FF FF               jne 0x140214137
00214335  48 8B 55 5F                     mov rdx, qword ptr [rbp + 0x5f]
00214339  48 8D 4D D7                     lea rcx, [rbp - 0x29]
0021433D  E8 AE 36 00 00                  call 0x1402179f0
00214342  83 3D D7 29 DB 00 00            cmp dword ptr [rip + 0xdb29d7], 0
00214349  0F B6 75 E7                     movzx esi, byte ptr [rbp - 0x19]
0021434D  74 0D                           je 0x14021435c
0021434F  44 0F 20 C1                     mov rcx, cr8
00214353  40 0F B6 D6                     movzx edx, sil
00214357  E8 3C 13 2E 00                  call 0x1404f5698
0021435C  44 0F 22 C6                     mov cr8, rsi
00214360  41 F6 C5 04                     test r13b, 4
00214364  74 13                           je 0x140214379
00214366  FF 05 40 42 C5 00               inc dword ptr [rip + 0xc54240]
0021436C  45 33 C0                        xor r8d, r8d
0021436F  8B D3                           mov edx, ebx
00214371  48 8B CF                        mov rcx, rdi
00214374  E8 97 1D 00 00                  call 0x140216110
00214379  41 F6 C5 02                     test r13b, 2
0021437D  74 2F                           je 0x1402143ae
0021437F  83 BF E8 05 00 00 00            cmp dword ptr [rdi + 0x5e8], 0
00214386  74 26                           je 0x1402143ae
00214388  48 8B 35 A1 8D D7 00            mov rsi, qword ptr [rip + 0xd78da1]
0021438F  48 85 F6                        test rsi, rsi
00214392  74 1A                           je 0x1402143ae
00214394  48 8D 4E 58                     lea rcx, [rsi + 0x58]
00214398  E8 83 22 00 00                  call 0x140216620
0021439D  84 C0                           test al, al
0021439F  74 0D                           je 0x1402143ae
002143A1  48 8B 46 60                     mov rax, qword ptr [rsi + 0x60]
002143A5  48 85 C0                        test rax, rax
002143A8  0F 85 D1 09 00 00               jne 0x140214d7f
002143AE  41 F7 C5 00 FF 00 00            test r13d, 0xff00
002143B5  0F 84 F0 FD FF FF               je 0x1402141ab
002143BB  65 FF 04 25 E8 90 00 00         inc dword ptr gs:[0x90e8]
002143C3  48 8D 05 36 BB DB 00            lea rax, [rip + 0xdbbb36]
002143CA  45 0F B6 7E 1B                  movzx r15d, byte ptr [r14 + 0x1b]
002143CF  48 39 87 20 02 00 00            cmp qword ptr [rdi + 0x220], rax
002143D6  0F 84 CF FD FF FF               je 0x1402141ab
002143DC  33 D2                           xor edx, edx
002143DE  48 89 55 F7                     mov qword ptr [rbp - 9], rdx
002143E2  45 32 E4                        xor r12b, r12b
002143E5  44 0F 20 C6                     mov rsi, cr8
002143E9  48 89 75 7F                     mov qword ptr [rbp + 0x7f], rsi
002143ED  B8 02 00 00 00                  mov eax, 2
002143F2  44 0F 22 C0                     mov cr8, rax
002143F6  39 15 24 29 DB 00               cmp dword ptr [rip + 0xdb2924], edx
002143FC  0F 85 B0 04 00 00               jne 0x1402148b2
00214402  65 4C 8B 2C 25 20 00 00 00      mov r13, qword ptr gs:[0x20]
0021440B  0F BE 87 C3 00 00 00            movsx eax, byte ptr [rdi + 0xc3]
00214412  84 C0                           test al, al
00214414  0F 8E F5 04 00 00               jle 0x14021490f
0021441A  41 3B C7                        cmp eax, r15d
0021441D  0F 8D EC 04 00 00               jge 0x14021490f
00214423  48 8B 4F 48                     mov rcx, qword ptr [rdi + 0x48]
00214427  8B F2                           mov esi, edx
00214429  48 89 4D 07                     mov qword ptr [rbp + 7], rcx
0021442D  0F 1F 00                        nop dword ptr [rax]
00214430  F0 48 0F BA 6F 40 00            lock bts qword ptr [rdi + 0x40], 0
00214437  73 1B                           jae 0x140214454
00214439  FF C6                           inc esi
0021443B  85 35 6B 0E DB 00               test dword ptr [rip + 0xdb0e6b], esi
00214441  0F 84 EB 04 00 00               je 0x140214932
00214447  F3 90                           pause
00214449  48 8B 47 40                     mov rax, qword ptr [rdi + 0x40]
0021444D  48 85 C0                        test rax, rax
00214450  74 DE                           je 0x140214430
00214452  EB E5                           jmp 0x140214439
00214454  0F BE 87 C3 00 00 00            movsx eax, byte ptr [rdi + 0xc3]
0021445B  84 C0                           test al, al
0021445D  7E 26                           jle 0x140214485
0021445F  41 3B C7                        cmp eax, r15d
00214462  7D 21                           jge 0x140214485
00214464  8B 05 E2 27 DB 00               mov eax, dword ptr [rip + 0xdb27e2]
0021446A  48 8D 4D F7                     lea rcx, [rbp - 9]
0021446E  4C 8B 4D 07                     mov r9, qword ptr [rbp + 7]
00214472  48 8B D7                        mov rdx, rdi
00214475  45 0F BE C7                     movsx r8d, r15b
00214479  41 B4 01                        mov r12b, 1
0021447C  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00214480  E8 BB 45 18 00                  call 0x140398a40
00214485  33 D2                           xor edx, edx
00214487  48 89 57 40                     mov qword ptr [rdi + 0x40], rdx
0021448B  45 84 E4                        test r12b, r12b
0021448E  0F 84 77 04 00 00               je 0x14021490b
00214494  48 8B 75 F7                     mov rsi, qword ptr [rbp - 9]
00214498  44 8B FA                        mov r15d, edx
0021449B  48 85 F6                        test rsi, rsi
0021449E  0F 84 EB FC FF FF               je 0x14021418f
002144A4  48 8B 06                        mov rax, qword ptr [rsi]
002144A7  48 89 45 F7                     mov qword ptr [rbp - 9], rax
002144AB  48 8D 96 28 FF FF FF            lea rdx, [rsi - 0xd8]
002144B2  45 33 C9                        xor r9d, r9d
002144B5  4C 8D 45 F7                     lea r8, [rbp - 9]
002144B9  49 8B CD                        mov rcx, r13
002144BC  E8 1F EB 03 00                  call 0x140252fe0
002144C1  48 8B 75 F7                     mov rsi, qword ptr [rbp - 9]
002144C5  41 FF C7                        inc r15d
002144C8  48 85 F6                        test rsi, rsi
002144CB  74 07                           je 0x1402144d4
002144CD  48 8B 06                        mov rax, qword ptr [rsi]
002144D0  48 89 45 F7                     mov qword ptr [rbp - 9], rax
002144D4  41 F6 C7 0F                     test r15b, 0xf
002144D8  75 0C                           jne 0x1402144e6
002144DA  49 8D 8D D8 35 00 00            lea rcx, [r13 + 0x35d8]
002144E1  E8 1A DD 03 00                  call 0x140252200
002144E6  48 85 F6                        test rsi, rsi
002144E9  75 C0                           jne 0x1402144ab
002144EB  E9 9F FC FF FF                  jmp 0x14021418f
002144F0  8B 05 62 99 CF 00               mov eax, dword ptr [rip + 0xcf9962]
002144F6  85 C0                           test eax, eax
002144F8  0F 85 20 FD FF FF               jne 0x14021421e
002144FE  48 8B D7                        mov rdx, rdi
00214501  48 8D 4D D7                     lea rcx, [rbp - 0x29]
00214505  E8 46 13 06 00                  call 0x140275850
0021450A  E9 1F FD FF FF                  jmp 0x14021422e
0021450F  0F B6 D1                        movzx edx, cl
00214512  41 0F B6 CF                     movzx ecx, r15b
00214516  E8 E1 11 2E 00                  call 0x1404f56fc
0021451B  E9 B5 FA FF FF                  jmp 0x140213fd5
00214520  49 8B 7E 10                     mov rdi, qword ptr [r14 + 0x10]
00214524  48 85 FF                        test rdi, rdi
00214527  0F 84 12 FD FF FF               je 0x14021423f
0021452D  8B 47 08                        mov eax, dword ptr [rdi + 8]
00214530  BE 01 00 00 00                  mov esi, 1
00214535  89 45 0F                        mov dword ptr [rbp + 0xf], eax
00214538  3B F0                           cmp esi, eax
0021453A  0F 83 FF FC FF FF               jae 0x14021423f
00214540  8B 47 18                        mov eax, dword ptr [rdi + 0x18]
00214543  48 83 C7 10                     add rdi, 0x10
00214547  4C 8B 3F                        mov r15, qword ptr [rdi]
0021454A  A8 02                           test al, 2
0021454C  74 18                           je 0x140214566
0021454E  49 83 E7 FC                     and r15, 0xfffffffffffffffc
00214552  4D 85 FF                        test r15, r15
00214555  75 17                           jne 0x14021456e
00214557  8B 45 0F                        mov eax, dword ptr [rbp + 0xf]
0021455A  FF C6                           inc esi
0021455C  44 8B 65 6F                     mov r12d, dword ptr [rbp + 0x6f]
00214560  44 8B 45 EF                     mov r8d, dword ptr [rbp - 0x11]
00214564  EB D2                           jmp 0x140214538
00214566  41 F6 C7 03                     test r15b, 3
0021456A  75 EB                           jne 0x140214557
0021456C  EB E4                           jmp 0x140214552
0021456E  45 85 C0                        test r8d, r8d
00214571  74 6D                           je 0x1402145e0
00214573  A8 01                           test al, 1
00214575  75 69                           jne 0x1402145e0
00214577  49 8B 87 20 02 00 00            mov rax, qword ptr [r15 + 0x220]
0021457E  41 8B 8F A0 05 00 00            mov ecx, dword ptr [r15 + 0x5a0]
00214585  C1 E9 09                        shr ecx, 9
00214588  83 E1 07                        and ecx, 7
0021458B  48 8B 80 A0 02 00 00            mov rax, qword ptr [rax + 0x2a0]
00214592  48 85 C0                        test rax, rax
00214595  74 0B                           je 0x1402145a2
00214597  8B 80 3C 04 00 00               mov eax, dword ptr [rax + 0x43c]
0021459D  3B C8                           cmp ecx, eax
0021459F  0F 4D C8                        cmovge ecx, eax
002145A2  83 F9 02                        cmp ecx, 2
002145A5  73 39                           jae 0x1402145e0
002145A7  41 83 CD 04                     or r13d, 4
002145AB  83 3D D6 29 DB 00 00            cmp dword ptr [rip + 0xdb29d6], 0
002145B2  44 89 6D 7F                     mov dword ptr [rbp + 0x7f], r13d
002145B6  0F 85 87 06 00 00               jne 0x140214c43
002145BC  41 BC 01 00 00 00               mov r12d, 1
002145C2  F0 45 0F C1 A7 E0 05 00 00      lock xadd dword ptr [r15 + 0x5e0], r12d
002145CB  41 FF C4                        inc r12d
002145CE  41 83 FC 01                     cmp r12d, 1
002145D2  0F 84 F0 07 00 00               je 0x140214dc8
002145D8  83 4F 08 01                     or dword ptr [rdi + 8], 1
002145DC  44 8B 65 6F                     mov r12d, dword ptr [rbp + 0x6f]
002145E0  45 85 E4                        test r12d, r12d
002145E3  74 38                           je 0x14021461d
002145E5  8B 47 08                        mov eax, dword ptr [rdi + 8]
002145E8  A8 04                           test al, 4
002145EA  75 31                           jne 0x14021461d
002145EC  41 83 CD 02                     or r13d, 2
002145F0  B8 01 00 00 00                  mov eax, 1
002145F5  44 89 6D 7F                     mov dword ptr [rbp + 0x7f], r13d
002145F9  F0 41 0F C1 87 E4 05 00 00      lock xadd dword ptr [r15 + 0x5e4], eax
00214602  FF C0                           inc eax
00214604  83 F8 01                        cmp eax, 1
00214607  75 10                           jne 0x140214619
00214609  41 0F B6 87 18 03 00 00         movzx eax, byte ptr [r15 + 0x318]
00214611  84 C0                           test al, al
00214613  0F 85 D6 04 00 00               jne 0x140214aef
00214619  83 4F 08 04                     or dword ptr [rdi + 8], 4
0021461D  83 7D F3 00                     cmp dword ptr [rbp - 0xd], 0
00214621  74 18                           je 0x14021463b
00214623  41 0F BE 8F C3 00 00 00         movsx ecx, byte ptr [r15 + 0xc3]
0021462B  41 0F B6 46 1B                  movzx eax, byte ptr [r14 + 0x1b]
00214630  3B C1                           cmp eax, ecx
00214632  7E 07                           jle 0x14021463b
00214634  41 81 CD 00 FF 00 00            or r13d, 0xff00
0021463B  45 85 ED                        test r13d, r13d
0021463E  0F 84 13 FF FF FF               je 0x140214557
00214644  BA 44 66 6C 74                  mov edx, 0x746c6644
00214649  49 8B CF                        mov rcx, r15
0021464C  E8 BF C0 FF FF                  call 0x140210710
00214651  48 8D 4D D7                     lea rcx, [rbp - 0x29]
00214655  E8 86 E6 12 00                  call 0x140342ce0
0021465A  41 F6 C5 04                     test r13b, 4
0021465E  74 13                           je 0x140214673
00214660  FF 05 4A 3F C5 00               inc dword ptr [rip + 0xc53f4a]
00214666  45 33 C0                        xor r8d, r8d
00214669  8B D3                           mov edx, ebx
0021466B  49 8B CF                        mov rcx, r15
0021466E  E8 9D 1A 00 00                  call 0x140216110
00214673  41 F6 C5 02                     test r13b, 2
00214677  74 08                           je 0x140214681
00214679  49 8B CF                        mov rcx, r15
0021467C  E8 D3 15 00 00                  call 0x140215c54
00214681  45 33 E4                        xor r12d, r12d
00214684  41 F7 C5 00 FF 00 00            test r13d, 0xff00
0021468B  0F 84 4B 01 00 00               je 0x1402147dc
00214691  65 FF 04 25 EC 90 00 00         inc dword ptr gs:[0x90ec]
00214699  48 8D 05 60 B8 DB 00            lea rax, [rip + 0xdbb860]
002146A0  45 0F B6 6E 1B                  movzx r13d, byte ptr [r14 + 0x1b]
002146A5  4C 89 65 FF                     mov qword ptr [rbp - 1], r12
002146A9  49 39 87 20 02 00 00            cmp qword ptr [r15 + 0x220], rax
002146B0  0F 84 26 01 00 00               je 0x1402147dc
002146B6  44 88 65 7F                     mov byte ptr [rbp + 0x7f], r12b
002146BA  45 0F 20 C4                     mov r12, cr8
002146BE  4C 89 65 07                     mov qword ptr [rbp + 7], r12
002146C2  B8 02 00 00 00                  mov eax, 2
002146C7  44 0F 22 C0                     mov cr8, rax
002146CB  83 3D 4E 26 DB 00 00            cmp dword ptr [rip + 0xdb264e], 0
002146D2  0F 85 96 02 00 00               jne 0x14021496e
002146D8  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
002146E1  48 89 45 17                     mov qword ptr [rbp + 0x17], rax
002146E5  41 0F BE 87 C3 00 00 00         movsx eax, byte ptr [r15 + 0xc3]
002146ED  84 C0                           test al, al
002146EF  0F 8E 9C 02 00 00               jle 0x140214991
002146F5  41 3B C5                        cmp eax, r13d
002146F8  0F 8D 93 02 00 00               jge 0x140214991
002146FE  49 8B 4F 48                     mov rcx, qword ptr [r15 + 0x48]
00214702  33 C0                           xor eax, eax
00214704  48 89 4D 1F                     mov qword ptr [rbp + 0x1f], rcx
00214708  44 8B E0                        mov r12d, eax
0021470B  0F 1F 44 00 00                  nop dword ptr [rax + rax]
00214710  F0 49 0F BA 6F 40 00            lock bts qword ptr [r15 + 0x40], 0
00214717  0F 82 63 01 00 00               jb 0x140214880
0021471D  41 0F BE 87 C3 00 00 00         movsx eax, byte ptr [r15 + 0xc3]
00214725  84 C0                           test al, al
00214727  7E 27                           jle 0x140214750
00214729  41 3B C5                        cmp eax, r13d
0021472C  7D 22                           jge 0x140214750
0021472E  8B 05 18 25 DB 00               mov eax, dword ptr [rip + 0xdb2518]
00214734  48 8D 4D FF                     lea rcx, [rbp - 1]
00214738  4C 8B 4D 1F                     mov r9, qword ptr [rbp + 0x1f]
0021473C  49 8B D7                        mov rdx, r15
0021473F  45 0F BE C5                     movsx r8d, r13b
00214743  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00214747  C6 45 7F 01                     mov byte ptr [rbp + 0x7f], 1
0021474B  E8 F0 42 18 00                  call 0x140398a40
00214750  33 C0                           xor eax, eax
00214752  49 89 47 40                     mov qword ptr [r15 + 0x40], rax
00214756  38 45 7F                        cmp byte ptr [rbp + 0x7f], al
00214759  0F 84 2E 02 00 00               je 0x14021498d
0021475F  4C 8B 65 FF                     mov r12, qword ptr [rbp - 1]
00214763  44 8B E8                        mov r13d, eax
00214766  4D 85 E4                        test r12, r12
00214769  74 52                           je 0x1402147bd
0021476B  49 8B 04 24                     mov rax, qword ptr [r12]
0021476F  4C 8B 75 17                     mov r14, qword ptr [rbp + 0x17]
00214773  48 89 45 FF                     mov qword ptr [rbp - 1], rax
00214777  49 8D 94 24 28 FF FF FF         lea rdx, [r12 - 0xd8]
0021477F  45 33 C9                        xor r9d, r9d
00214782  4C 8D 45 FF                     lea r8, [rbp - 1]
00214786  49 8B CE                        mov rcx, r14
00214789  E8 52 E8 03 00                  call 0x140252fe0
0021478E  4C 8B 65 FF                     mov r12, qword ptr [rbp - 1]
00214792  41 FF C5                        inc r13d
00214795  4D 85 E4                        test r12, r12
00214798  74 08                           je 0x1402147a2
0021479A  49 8B 04 24                     mov rax, qword ptr [r12]
0021479E  48 89 45 FF                     mov qword ptr [rbp - 1], rax
002147A2  41 F6 C5 0F                     test r13b, 0xf
002147A6  75 0C                           jne 0x1402147b4
002147A8  49 8D 8E D8 35 00 00            lea rcx, [r14 + 0x35d8]
002147AF  E8 4C DA 03 00                  call 0x140252200
002147B4  4D 85 E4                        test r12, r12
002147B7  75 BE                           jne 0x140214777
002147B9  4C 8B 75 67                     mov r14, qword ptr [rbp + 0x67]
002147BD  4C 8B 6D 17                     mov r13, qword ptr [rbp + 0x17]
002147C1  49 8D 8D D8 35 00 00            lea rcx, [r13 + 0x35d8]
002147C8  E8 33 DA 03 00                  call 0x140252200
002147CD  0F B6 55 07                     movzx edx, byte ptr [rbp + 7]
002147D1  49 8B CD                        mov rcx, r13
002147D4  E8 6F BE 03 00                  call 0x140250648
002147D9  45 33 E4                        xor r12d, r12d
002147DC  83 3D 2D 08 DB 00 00            cmp dword ptr [rip + 0xdb082d], 0
002147E3  74 15                           je 0x1402147fa
002147E5  33 D2                           xor edx, edx
002147E7  49 8D 4F D0                     lea rcx, [r15 - 0x30]
002147EB  41 B9 44 66 6C 74               mov r9d, 0x746c6644
002147F1  44 8D 42 01                     lea r8d, [rdx + 1]
002147F5  E8 EA C1 FF FF                  call 0x1402109e4
002147FA  48 C7 C0 FF FF FF FF            mov rax, 0xffffffffffffffff
00214801  F0 49 0F C1 47 D0               lock xadd qword ptr [r15 - 0x30], rax
00214807  48 83 E8 01                     sub rax, 1
0021480B  0F 8E 06 02 00 00               jle 0x140214a17
00214811  49 8D 4E 60                     lea rcx, [r14 + 0x60]
00214815  4C 89 65 D7                     mov qword ptr [rbp - 0x29], r12
00214819  48 89 4D DF                     mov qword ptr [rbp - 0x21], rcx
0021481D  45 8B EC                        mov r13d, r12d
00214820  90                              nop
00214821  45 0F 20 C7                     mov r15, cr8
00214825  B8 02 00 00 00                  mov eax, 2
0021482A  44 0F 22 C0                     mov cr8, rax
0021482E  83 3D EB 24 DB 00 00            cmp dword ptr [rip + 0xdb24eb], 0
00214835  0F 85 1E 01 00 00               jne 0x140214959
0021483B  F6 05 C4 22 DB 00 21            test byte ptr [rip + 0xdb22c4], 0x21
00214842  44 88 7D E7                     mov byte ptr [rbp - 0x19], r15b
00214846  75 7D                           jne 0x1402148c5
00214848  48 8D 55 D7                     lea rdx, [rbp - 0x29]
0021484C  48 87 11                        xchg qword ptr [rcx], rdx
0021484F  48 85 D2                        test rdx, rdx
00214852  0F 85 84 01 00 00               jne 0x1402149dc
00214858  49 8B 46 10                     mov rax, qword ptr [r14 + 0x10]
0021485C  48 85 C0                        test rax, rax
0021485F  0F 84 DD F9 FF FF               je 0x140214242
00214865  8B 4D 0F                        mov ecx, dword ptr [rbp + 0xf]
00214868  39 48 08                        cmp dword ptr [rax + 8], ecx
0021486B  0F 84 E6 FC FF FF               je 0x140214557
00214871  E9 CC F9 FF FF                  jmp 0x140214242
00214876  66 66 0F 1F 84 00 00 00 00 00   nop word ptr [rax + rax]
00214880  41 FF C4                        inc r12d
00214883  44 85 25 22 0A DB 00            test dword ptr [rip + 0xdb0a22], r12d
0021488A  0F 84 24 01 00 00               je 0x1402149b4
00214890  F3 90                           pause
00214892  49 8B 47 40                     mov rax, qword ptr [r15 + 0x40]
00214896  48 85 C0                        test rax, rax
00214899  0F 84 71 FE FF FF               je 0x140214710
0021489F  EB DF                           jmp 0x140214880
002148A1  0F B6 D0                        movzx edx, al
002148A4  40 0F B6 CE                     movzx ecx, sil
002148A8  E8 4F 0E 2E 00                  call 0x1404f56fc
002148AD  E9 5B F9 FF FF                  jmp 0x14021420d
002148B2  0F B6 D0                        movzx edx, al
002148B5  40 0F B6 CE                     movzx ecx, sil
002148B9  E8 3E 0E 2E 00                  call 0x1404f56fc
002148BE  33 D2                           xor edx, edx
002148C0  E9 3D FB FF FF                  jmp 0x140214402
002148C5  8B 05 8D 95 CF 00               mov eax, dword ptr [rip + 0xcf958d]
002148CB  85 C0                           test eax, eax
002148CD  0F 85 75 FF FF FF               jne 0x140214848
002148D3  48 8B D1                        mov rdx, rcx
002148D6  48 8D 4D D7                     lea rcx, [rbp - 0x29]
002148DA  E8 71 0F 06 00                  call 0x140275850
002148DF  E9 74 FF FF FF                  jmp 0x140214858
002148E4  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
002148ED  48 3B F0                        cmp rsi, rax
002148F0  0F 84 9C F6 FF FF               je 0x140213f92
002148F6  3B D9                           cmp ebx, ecx
002148F8  E9 93 F6 FF FF                  jmp 0x140213f90
002148FD  48 8D 4D D7                     lea rcx, [rbp - 0x29]
00214901  E8 AA 35 04 00                  call 0x140257eb0
00214906  E9 EB F6 FF FF                  jmp 0x140213ff6
0021490B  48 8B 75 7F                     mov rsi, qword ptr [rbp + 0x7f]
0021490F  83 3D 0A 24 DB 00 00            cmp dword ptr [rip + 0xdb240a], 0
00214916  74 0D                           je 0x140214925
00214918  44 0F 20 C1                     mov rcx, cr8
0021491C  40 0F B6 D6                     movzx edx, sil
00214920  E8 73 0D 2E 00                  call 0x1404f5698
00214925  40 0F B6 C6                     movzx eax, sil
00214929  44 0F 22 C0                     mov cr8, rax
0021492D  E9 75 F8 FF FF                  jmp 0x1402141a7
00214932  8B 05 80 21 DB 00               mov eax, dword ptr [rip + 0xdb2180]
00214938  A8 40                           test al, 0x40
0021493A  0F 84 07 FB FF FF               je 0x140214447
00214940  E8 4B AB 0F 00                  call 0x14030f490
00214945  84 C0                           test al, al
00214947  0F 84 FA FA FF FF               je 0x140214447
0021494D  8B CE                           mov ecx, esi
0021494F  E8 0C AB 0F 00                  call 0x14030f460
00214954  E9 F0 FA FF FF                  jmp 0x140214449
00214959  0F B6 D0                        movzx edx, al
0021495C  41 0F B6 CF                     movzx ecx, r15b
00214960  E8 97 0D 2E 00                  call 0x1404f56fc
00214965  49 8D 4E 60                     lea rcx, [r14 + 0x60]
00214969  E9 CD FE FF FF                  jmp 0x14021483b
0021496E  0F B6 D0                        movzx edx, al
00214971  41 0F B6 CC                     movzx ecx, r12b
00214975  E8 82 0D 2E 00                  call 0x1404f56fc
0021497A  E9 59 FD FF FF                  jmp 0x1402146d8
0021497F  48 8D 4D D7                     lea rcx, [rbp - 0x29]
00214983  E8 28 35 04 00                  call 0x140257eb0
00214988  E9 A1 F8 FF FF                  jmp 0x14021422e
0021498D  4C 8B 65 07                     mov r12, qword ptr [rbp + 7]
00214991  83 3D 88 23 DB 00 00            cmp dword ptr [rip + 0xdb2388], 0
00214998  74 0D                           je 0x1402149a7
0021499A  44 0F 20 C1                     mov rcx, cr8
0021499E  41 0F B6 D4                     movzx edx, r12b
002149A2  E8 F1 0C 2E 00                  call 0x1404f5698
002149A7  41 0F B6 C4                     movzx eax, r12b
002149AB  44 0F 22 C0                     mov cr8, rax
002149AF  E9 25 FE FF FF                  jmp 0x1402147d9
002149B4  8B 05 FE 20 DB 00               mov eax, dword ptr [rip + 0xdb20fe]
002149BA  A8 40                           test al, 0x40
002149BC  0F 84 CE FE FF FF               je 0x140214890
002149C2  E8 C9 AA 0F 00                  call 0x14030f490
002149C7  84 C0                           test al, al
002149C9  0F 84 C1 FE FF FF               je 0x140214890
002149CF  41 8B CC                        mov ecx, r12d
002149D2  E8 89 AA 0F 00                  call 0x14030f460
002149D7  E9 B6 FE FF FF                  jmp 0x140214892
002149DC  48 8D 4D D7                     lea rcx, [rbp - 0x29]
002149E0  E8 CB 34 04 00                  call 0x140257eb0
002149E5  E9 6E FE FF FF                  jmp 0x140214858
002149EA  48 8B 4F D8                     mov rcx, qword ptr [rdi - 0x28]
002149EE  48 85 C9                        test rcx, rcx
002149F1  0F 85 B9 00 00 00               jne 0x140214ab0
002149F7  48 85 C0                        test rax, rax
002149FA  0F 89 06 03 00 00               jns 0x140214d06
00214A00  33 D2                           xor edx, edx
00214A02  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00214A07  44 8D 49 04                     lea r9d, [rcx + 4]
00214A0B  4C 8B C7                        mov r8, rdi
00214A0E  8D 4A 18                        lea ecx, [rdx + 0x18]
00214A11  E8 4A 8C 2E 00                  call 0x1404fd660
00214A16  CC                              int3
00214A17  49 8B 4F D8                     mov rcx, qword ptr [r15 - 0x28]
00214A1B  48 85 C9                        test rcx, rcx
00214A1E  0F 85 37 01 00 00               jne 0x140214b5b
00214A24  48 85 C0                        test rax, rax
00214A27  0F 89 E7 02 00 00               jns 0x140214d14
00214A2D  33 D2                           xor edx, edx
00214A2F  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00214A34  44 8D 49 04                     lea r9d, [rcx + 4]
00214A38  4D 8B C7                        mov r8, r15
00214A3B  8D 4A 18                        lea ecx, [rdx + 0x18]
00214A3E  E8 1D 8C 2E 00                  call 0x1404fd660
00214A43  CC                              int3
00214A44  44 0F 20 C6                     mov rsi, cr8
00214A48  B8 02 00 00 00                  mov eax, 2
00214A4D  44 0F 22 C0                     mov cr8, rax
00214A51  83 3D C8 22 DB 00 00            cmp dword ptr [rip + 0xdb22c8], 0
00214A58  0F 85 3D 01 00 00               jne 0x140214b9b
00214A5E  65 4C 8B 3C 25 20 00 00 00      mov r15, qword ptr gs:[0x20]
00214A67  4C 8D 87 28 03 00 00            lea r8, [rdi + 0x328]
00214A6E  48 8B CF                        mov rcx, rdi
00214A71  49 8D 97 78 91 00 00            lea rdx, [r15 + 0x9178]
00214A78  E8 63 A6 00 00                  call 0x14021f0e0
00214A7D  85 C0                           test eax, eax
00214A7F  74 08                           je 0x140214a89
00214A81  49 8B CF                        mov rcx, r15
00214A84  E8 47 2A FF FF                  call 0x1402074d0
00214A89  83 3D 90 22 DB 00 00            cmp dword ptr [rip + 0xdb2290], 0
00214A90  74 0D                           je 0x140214a9f
00214A92  44 0F 20 C1                     mov rcx, cr8
00214A96  40 0F B6 D6                     movzx edx, sil
00214A9A  E8 F9 0B 2E 00                  call 0x1404f5698
00214A9F  40 0F B6 C6                     movzx eax, sil
00214AA3  44 0F 22 C0                     mov cr8, rax
00214AA7  49 8D 4E 38                     lea rcx, [r14 + 0x38]
00214AAB  E9 44 F6 FF FF                  jmp 0x1402140f4
00214AB0  41 B9 03 00 00 00               mov r9d, 3
00214AB6  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00214ABB  48 8D 47 D0                     lea rax, [rdi - 0x30]
00214ABF  4C 8B C7                        mov r8, rdi
00214AC2  48 C1 E8 08                     shr rax, 8
00214AC6  0F B6 D0                        movzx edx, al
00214AC9  0F B6 47 E8                     movzx eax, byte ptr [rdi - 0x18]
00214ACD  41 8D 49 15                     lea ecx, [r9 + 0x15]
00214AD1  48 33 D0                        xor rdx, rax
00214AD4  0F B6 05 71 23 DB 00            movzx eax, byte ptr [rip + 0xdb2371]
00214ADB  48 33 D0                        xor rdx, rax
00214ADE  48 8D 05 1B 2D DB 00            lea rax, [rip + 0xdb2d1b]
00214AE5  48 8B 14 D0                     mov rdx, qword ptr [rax + rdx*8]
00214AE9  E8 72 8B 2E 00                  call 0x1404fd660
00214AEE  CC                              int3
00214AEF  45 0F 20 C4                     mov r12, cr8
00214AF3  B8 02 00 00 00                  mov eax, 2
00214AF8  44 0F 22 C0                     mov cr8, rax
00214AFC  83 3D 1D 22 DB 00 00            cmp dword ptr [rip + 0xdb221d], 0
00214B03  0F 85 29 01 00 00               jne 0x140214c32
00214B09  65 4C 8B 2C 25 20 00 00 00      mov r13, qword ptr gs:[0x20]
00214B12  4D 8D 87 28 03 00 00            lea r8, [r15 + 0x328]
00214B19  49 8B CF                        mov rcx, r15
00214B1C  49 8D 95 78 91 00 00            lea rdx, [r13 + 0x9178]
00214B23  E8 B8 A5 00 00                  call 0x14021f0e0
00214B28  85 C0                           test eax, eax
00214B2A  74 08                           je 0x140214b34
00214B2C  49 8B CD                        mov rcx, r13
00214B2F  E8 9C 29 FF FF                  call 0x1402074d0
00214B34  83 3D E5 21 DB 00 00            cmp dword ptr [rip + 0xdb21e5], 0
00214B3B  74 0D                           je 0x140214b4a
00214B3D  44 0F 20 C1                     mov rcx, cr8
00214B41  41 0F B6 D4                     movzx edx, r12b
00214B45  E8 4E 0B 2E 00                  call 0x1404f5698
00214B4A  41 0F B6 C4                     movzx eax, r12b
00214B4E  44 0F 22 C0                     mov cr8, rax
00214B52  44 8B 6D 7F                     mov r13d, dword ptr [rbp + 0x7f]
00214B56  E9 BE FA FF FF                  jmp 0x140214619
00214B5B  41 B9 03 00 00 00               mov r9d, 3
00214B61  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00214B66  49 8D 47 D0                     lea rax, [r15 - 0x30]
00214B6A  4D 8B C7                        mov r8, r15
00214B6D  48 C1 E8 08                     shr rax, 8
00214B71  0F B6 D0                        movzx edx, al
00214B74  41 0F B6 47 E8                  movzx eax, byte ptr [r15 - 0x18]
00214B79  41 8D 49 15                     lea ecx, [r9 + 0x15]
00214B7D  48 33 D0                        xor rdx, rax
00214B80  0F B6 05 C5 22 DB 00            movzx eax, byte ptr [rip + 0xdb22c5]
00214B87  48 33 D0                        xor rdx, rax
00214B8A  48 8D 05 6F 2C DB 00            lea rax, [rip + 0xdb2c6f]
00214B91  48 8B 14 D0                     mov rdx, qword ptr [rax + rdx*8]
00214B95  E8 C6 8A 2E 00                  call 0x1404fd660
00214B9A  CC                              int3
00214B9B  0F B6 D0                        movzx edx, al
00214B9E  40 0F B6 CE                     movzx ecx, sil
00214BA2  E8 55 0B 2E 00                  call 0x1404f56fc
00214BA7  E9 B2 FE FF FF                  jmp 0x140214a5e
00214BAC  BA 70 00 00 00                  mov edx, 0x70
00214BB1  41 B8 42 6F 6F 73               mov r8d, 0x736f6f42
00214BB7  8D 4A D0                        lea ecx, [rdx - 0x30]
00214BBA  E8 31 D5 96 00                  call 0x140b820f0
00214BBF  4C 8B E0                        mov r12, rax
00214BC2  48 85 C0                        test rax, rax
00214BC5  74 28                           je 0x140214bef
00214BC7  45 33 C9                        xor r9d, r9d
00214BCA  4C 8D 40 10                     lea r8, [rax + 0x10]
00214BCE  41 8D 51 0A                     lea edx, [r9 + 0xa]
00214BD2  8D 4A F7                        lea ecx, [rdx - 9]
00214BD5  E8 16 54 0E 00                  call 0x1402f9ff0
00214BDA  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00214BE3  33 C0                           xor eax, eax
00214BE5  49 89 4C 24 60                  mov qword ptr [r12 + 0x60], rcx
00214BEA  49 89 44 24 68                  mov qword ptr [r12 + 0x68], rax
00214BEF  48 8D 8F 10 06 00 00            lea rcx, [rdi + 0x610]
00214BF6  E8 75 38 FF FF                  call 0x140208470
00214BFB  44 0F B6 F8                     movzx r15d, al
00214BFF  BE 01 00 00 00                  mov esi, 1
00214C04  F0 0F C1 B7 E0 05 00 00         lock xadd dword ptr [rdi + 0x5e0], esi
00214C0C  FF C6                           inc esi
00214C0E  4D 85 E4                        test r12, r12
00214C11  0F 84 1B 01 00 00               je 0x140214d32
00214C17  48 8D 87 F0 05 00 00            lea rax, [rdi + 0x5f0]
00214C1E  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
00214C22  48 39 01                        cmp qword ptr [rcx], rax
00214C25  0F 84 F7 00 00 00               je 0x140214d22
00214C2B  B9 03 00 00 00                  mov ecx, 3
00214C30  CD 29                           int 0x29
00214C32  0F B6 D0                        movzx edx, al
00214C35  41 0F B6 CC                     movzx ecx, r12b
00214C39  E8 BE 0A 2E 00                  call 0x1404f56fc
00214C3E  E9 C6 FE FF FF                  jmp 0x140214b09
00214C43  BA 70 00 00 00                  mov edx, 0x70
00214C48  41 B8 42 6F 6F 73               mov r8d, 0x736f6f42
00214C4E  8D 4A D0                        lea ecx, [rdx - 0x30]
00214C51  E8 9A D4 96 00                  call 0x140b820f0
00214C56  48 89 45 07                     mov qword ptr [rbp + 7], rax
00214C5A  4C 8B E0                        mov r12, rax
00214C5D  48 85 C0                        test rax, rax
00214C60  74 28                           je 0x140214c8a
00214C62  45 33 C9                        xor r9d, r9d
00214C65  4C 8D 40 10                     lea r8, [rax + 0x10]
00214C69  41 8D 51 0A                     lea edx, [r9 + 0xa]
00214C6D  8D 4A F7                        lea ecx, [rdx - 9]
00214C70  E8 7B 53 0E 00                  call 0x1402f9ff0
00214C75  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00214C7E  33 C0                           xor eax, eax
00214C80  49 89 4C 24 60                  mov qword ptr [r12 + 0x60], rcx
00214C85  49 89 44 24 68                  mov qword ptr [r12 + 0x68], rax
00214C8A  49 8D 8F 10 06 00 00            lea rcx, [r15 + 0x610]
00214C91  E8 DA 37 FF FF                  call 0x140208470
00214C96  44 0F B6 E8                     movzx r13d, al
00214C9A  41 BC 01 00 00 00               mov r12d, 1
00214CA0  F0 45 0F C1 A7 E0 05 00 00      lock xadd dword ptr [r15 + 0x5e0], r12d
00214CA9  48 8B 45 07                     mov rax, qword ptr [rbp + 7]
00214CAD  41 FF C4                        inc r12d
00214CB0  48 85 C0                        test rax, rax
00214CB3  74 22                           je 0x140214cd7
00214CB5  49 8D 8F F0 05 00 00            lea rcx, [r15 + 0x5f0]
00214CBC  48 8B 51 08                     mov rdx, qword ptr [rcx + 8]
00214CC0  48 39 0A                        cmp qword ptr [rdx], rcx
00214CC3  0F 85 62 FF FF FF               jne 0x140214c2b
00214CC9  48 89 08                        mov qword ptr [rax], rcx
00214CCC  48 89 50 08                     mov qword ptr [rax + 8], rdx
00214CD0  48 89 02                        mov qword ptr [rdx], rax
00214CD3  48 89 41 08                     mov qword ptr [rcx + 8], rax
00214CD7  49 8D 8F 10 06 00 00            lea rcx, [r15 + 0x610]
00214CDE  E8 8D 19 FF FF                  call 0x140206670
00214CE3  83 3D 36 20 DB 00 00            cmp dword ptr [rip + 0xdb2036], 0
00214CEA  74 0D                           je 0x140214cf9
00214CEC  44 0F 20 C1                     mov rcx, cr8
00214CF0  41 0F B6 D5                     movzx edx, r13b
00214CF4  E8 9F 09 2E 00                  call 0x1404f5698
00214CF9  45 0F 22 C5                     mov cr8, r13
00214CFD  44 8B 6D 7F                     mov r13d, dword ptr [rbp + 0x7f]
00214D01  E9 C8 F8 FF FF                  jmp 0x1402145ce
00214D06  48 8D 4F D0                     lea rcx, [rdi - 0x30]
00214D0A  E8 85 D6 18 00                  call 0x1403a2394
00214D0F  E9 D2 F4 FF FF                  jmp 0x1402141e6
00214D14  49 8D 4F D0                     lea rcx, [r15 - 0x30]
00214D18  E8 77 D6 18 00                  call 0x1403a2394
00214D1D  E9 EF FA FF FF                  jmp 0x140214811
00214D22  49 89 04 24                     mov qword ptr [r12], rax
00214D26  49 89 4C 24 08                  mov qword ptr [r12 + 8], rcx
00214D2B  4C 89 21                        mov qword ptr [rcx], r12
00214D2E  4C 89 60 08                     mov qword ptr [rax + 8], r12
00214D32  F6 05 CD 1D DB 00 01            test byte ptr [rip + 0xdb1dcd], 1
00214D39  48 8D 8F 10 06 00 00            lea rcx, [rdi + 0x610]
00214D40  75 28                           jne 0x140214d6a
00214D42  F0 48 83 21 00                  lock and qword ptr [rcx], 0
00214D47  83 3D D2 1F DB 00 00            cmp dword ptr [rip + 0xdb1fd2], 0
00214D4E  74 0D                           je 0x140214d5d
00214D50  44 0F 20 C1                     mov rcx, cr8
00214D54  41 0F B6 D7                     movzx edx, r15b
00214D58  E8 3B 09 2E 00                  call 0x1404f5698
00214D5D  45 0F 22 C7                     mov cr8, r15
00214D61  44 8B 65 6F                     mov r12d, dword ptr [rbp + 0x6f]
00214D65  E9 44 F3 FF FF                  jmp 0x1402140ae
00214D6A  8B 05 E8 90 CF 00               mov eax, dword ptr [rip + 0xcf90e8]
00214D70  85 C0                           test eax, eax
00214D72  75 CE                           jne 0x140214d42
00214D74  48 8B 55 5F                     mov rdx, qword ptr [rbp + 0x5f]
00214D78  E8 73 E1 17 00                  call 0x140392ef0
00214D7D  EB C8                           jmp 0x140214d47
00214D7F  48 8B 40 10                     mov rax, qword ptr [rax + 0x10]
00214D83  48 8B CF                        mov rcx, rdi
00214D86  E8 45 5D 4A 00                  call 0x1406baad0
00214D8B  48 8B 0D 9E 83 D7 00            mov rcx, qword ptr [rip + 0xd7839e]
00214D92  48 83 C1 58                     add rcx, 0x58
00214D96  0F 0D 09                        prefetchw byte ptr [rcx]
00214D99  48 8B 01                        mov rax, qword ptr [rcx]
00214D9C  48 83 E0 FE                     and rax, 0xfffffffffffffffe
00214DA0  48 8D 50 FE                     lea rdx, [rax - 2]
00214DA4  F0 48 0F B1 11                  lock cmpxchg qword ptr [rcx], rdx
00214DA9  0F 84 FF F5 FF FF               je 0x1402143ae
00214DAF  E8 FC 50 13 00                  call 0x140349eb0
00214DB4  E9 F5 F5 FF FF                  jmp 0x1402143ae
00214DB9  33 D2                           xor edx, edx
00214DBB  48 8B CF                        mov rcx, rdi
00214DBE  E8 9D AE 20 00                  call 0x14041fc60
00214DC3  E9 EF F2 FF FF                  jmp 0x1402140b7
00214DC8  33 D2                           xor edx, edx
00214DCA  49 8B CF                        mov rcx, r15
00214DCD  E8 8E AE 20 00                  call 0x14041fc60
00214DD2  E9 01 F8 FF FF                  jmp 0x1402145d8
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_002142F9(__int64 a1, __int64 a2, int a3)
{
    unsigned int v_stack_p20;
}
```

## 5. (Beta) C Style

```c
int64_t sub_002142F9(int64_t Arg1, int64_t Arg2, int32_t Arg3)
{
    uint32_t v_stack_p20;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002142F9&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
