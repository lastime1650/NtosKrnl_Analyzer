# sub_0027475D

- RVA: `0x0027475D`–`0x0027572C` (길이 `4,047` bytes)
- VA: `0x000000014027475D`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00065E1C`
- 디코드: `946`개 명령, `4,047/4,047` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **57**; 고유 호출 대상: **23**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **11**

### Outgoing calls
- `0x00274833` → [ObpPushStackInfo](../21/ObpPushStackInfo_function_002109E4.md) (function, `0x002109E4`)
- `0x002748FF` → [KxWaitForLockChainValid](../21/KxWaitForLockChainValid_function_00217AA0.md) (function, `0x00217AA0`)
- `0x00274935` → [KeDisableInterrupts](../21/KeDisableInterrupts_function_00217BE0.md) (function, `0x00217BE0`)
- `0x00274948` → [KiHaltOnAddressWakeEntireList](../21/KiHaltOnAddressWakeEntireList_function_00217AF4.md) (function, `0x00217AF4`)
- `0x00274985` → [KiReleaseQueuedSpinLockInstrumented](../21/KiReleaseQueuedSpinLockInstrumented_function_002179F0.md) (function, `0x002179F0`)
- `0x002749A0` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x00274A0E` → [KiReleaseQueuedSpinLockInstrumented](../21/KiReleaseQueuedSpinLockInstrumented_function_002179F0.md) (function, `0x002179F0`)
- `0x00274A29` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x00274AE2` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00274B1B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00274C53` → [KxWaitForLockChainValid](../21/KxWaitForLockChainValid_function_00217AA0.md) (function, `0x00217AA0`)
- `0x00274C8A` → [KeDisableInterrupts](../21/KeDisableInterrupts_function_00217BE0.md) (function, `0x00217BE0`)
- `0x00274C9D` → [KiHaltOnAddressWakeEntireList](../21/KiHaltOnAddressWakeEntireList_function_00217AF4.md) (function, `0x00217AF4`)
- `0x00274D05` → [KiTryUnwaitThread](../35/KiTryUnwaitThread_function_003506D0.md) (function, `0x003506D0`)
- `0x00274D52` → [KiRemoveBoostThread](../21/KiRemoveBoostThread_function_00219128.md) (function, `0x00219128`)
- `0x00274D7E` → [KiExitDispatcher](../25/KiExitDispatcher_function_00251CF0.md) (function, `0x00251CF0`)
- `0x00274DD3` → [KiRemoveSystemWorkPriorityKick](../26/KiRemoveSystemWorkPriorityKick_function_002631D0.md) (function, `0x002631D0`)
- `0x00274E27` → [KiAcquireKobjectLockSafe](../25/KiAcquireKobjectLockSafe_function_00251C90.md) (function, `0x00251C90`)
- `0x00274E8C` → [KiTryUnwaitThread](../35/KiTryUnwaitThread_function_003506D0.md) (function, `0x003506D0`)
- `0x00274EC8` → [KiRemoveBoostThread](../21/KiRemoveBoostThread_function_00219128.md) (function, `0x00219128`)
- `0x00274EF3` → [KiExitDispatcher](../25/KiExitDispatcher_function_00251CF0.md) (function, `0x00251CF0`)
- `0x00274F28` → [KiRemoveSystemWorkPriorityKick](../26/KiRemoveSystemWorkPriorityKick_function_002631D0.md) (function, `0x002631D0`)
- `0x00274F5D` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x00274F7B` → [KiInsertQueueInternal](../21/KiInsertQueueInternal_function_00219B30.md) (function, `0x00219B30`)
- `0x00274FBB` → [KiRemoveSystemWorkPriorityKick](../26/KiRemoveSystemWorkPriorityKick_function_002631D0.md) (function, `0x002631D0`)
- `0x00274FFF` → [RtlRemoveHeadCircularList](../43/RtlRemoveHeadCircularList_function_00432D70.md) (function, `0x00432D70`)
- `0x0027504A` → [KiRemoveSystemWorkPriorityKick](../26/KiRemoveSystemWorkPriorityKick_function_002631D0.md) (function, `0x002631D0`)
- `0x002750DF` → [EtwTraceKernelEvent](../23/EtwTraceKernelEvent_function_00235350.md) (function, `0x00235350`)
- `0x002750EF` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x0027510D` → [KiInsertQueueInternal](../21/KiInsertQueueInternal_function_00219B30.md) (function, `0x00219B30`)
- `0x002751D4` → [EtwTraceKernelEvent](../23/EtwTraceKernelEvent_function_00235350.md) (function, `0x00235350`)
- `0x00275223` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00275250` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00275270` → [KiTryUnwaitThread](../35/KiTryUnwaitThread_function_003506D0.md) (function, `0x003506D0`)
- `0x002752C5` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x002752E5` → [KiTryUnwaitThread](../35/KiTryUnwaitThread_function_003506D0.md) (function, `0x003506D0`)
- `0x0027532C` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00275359` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00275374` → [RtlCaptureStackBackTrace](../2F/RtlCaptureStackBackTrace_function_002F9FF0.md) (function, `0x002F9FF0`)
- `0x00275393` → [KeAcquireSpinLockRaiseToDpc](../20/KeAcquireSpinLockRaiseToDpc_function_00208470.md) (function, `0x00208470`)
- `0x002753B7` → [KeInsertQueueDpc](../20/KeInsertQueueDpc_function_00207C50.md) (function, `0x00207C50`)
- `0x002753E0` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x002753FB` → [RtlCaptureStackBackTrace](../2F/RtlCaptureStackBackTrace_function_002F9FF0.md) (function, `0x002F9FF0`)
- `0x0027541C` → [KeAcquireSpinLockRaiseToDpc](../20/KeAcquireSpinLockRaiseToDpc_function_00208470.md) (function, `0x00208470`)
- `0x0027543E` → [KeInsertQueueDpc](../20/KeInsertQueueDpc_function_00207C50.md) (function, `0x00207C50`)
- `0x0027544C` → [ObpDeferObjectDeletion](../3A/ObpDeferObjectDeletion_function_003A2394.md) (function, `0x003A2394`)
- `0x0027545A` → [ObpDeferObjectDeletion](../3A/ObpDeferObjectDeletion_function_003A2394.md) (function, `0x003A2394`)
- `0x00275493` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x002754B3` → [KiReleaseSpinLockInstrumented](../39/KiReleaseSpinLockInstrumented_function_00392EF0.md) (function, `0x00392EF0`)
- `0x002754E9` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x00275509` → [KiReleaseSpinLockInstrumented](../39/KiReleaseSpinLockInstrumented_function_00392EF0.md) (function, `0x00392EF0`)
- `0x00275556` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x002755A0` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x002755CA` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00275619` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00275663` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0027568D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x002747C5` → RVA `0x00FC6F88` (`ALMOSTRO`; read)
- `0x0027481B` → RVA `0x00FC5010` (`ALMOSTRO`; read)
- `0x002748BE` → RVA `0x00FC6B06` (`ALMOSTRO`; read)
- `0x0027492A` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x0027496E` → RVA `0x00F0DE58` (`.data`; read)
- `0x0027498A` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x00274AC8` → RVA `0x00E68468` (`.data`; read)
- `0x00274BFD` → RVA `0x00E0EB10` (`.data`; read)
- `0x00275064` → RVA `0x00E0EB18` (`.data`; read)
- `0x002752B3` → RVA `0x00FC6E4C` (`ALMOSTRO`; read)
- `0x0027546D` → RVA `0x00FC6B06` (`ALMOSTRO`; reference)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **10**
  - `0x00274AE2` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
  - `0x00274B1B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x00275359` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
  - `0x002753E0` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
  - `0x00275556` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x002755A0` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x002755CA` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x00275619` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x00275663` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x0027568D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **47**
  - `0x00274A3D` → [sub_002746E8 + 0x4E](Unknown_function_002746E8.md) (`tail-transfer`)
  - `0x00274A99` → [sub_002746E8 + 0x4E](Unknown_function_002746E8.md) (`tail-transfer`)
  - `0x00274ABB` → [sub_002746E8 + 0x4E](Unknown_function_002746E8.md) (`tail-transfer`)
  - `0x00274AED` → [sub_002746E8 + 0x4E](Unknown_function_002746E8.md) (`tail-transfer`)
  - `0x00274B8D` → [sub_002746E8 + 0x4E](Unknown_function_002746E8.md) (`tail-transfer`)
  - `0x00274C0F` → [sub_002746E8 + 0x4E](Unknown_function_002746E8.md) (`tail-transfer`)
  - `0x00274D1A` → [sub_00274581 + 0xFF](Unknown_function_00274581.md) (`tail-transfer`)
  - `0x00274D28` → [sub_00274581 + 0xFF](Unknown_function_00274581.md) (`tail-transfer`)
  - `0x00274D83` → [sub_00273F95 + 0x24D](Unknown_function_00273F95.md) (`tail-transfer`)
  - `0x00274DB0` → [sub_00273F95 + 0x110](Unknown_function_00273F95.md) (`tail-transfer`)
  - `0x00274DCD` → [sub_00273F95 + 0x5BD](Unknown_function_00273F95.md) (`tail-transfer`)
  - `0x00274DD8` → [sub_00273F95 + 0x5BD](Unknown_function_00273F95.md) (`tail-transfer`)
  - `0x00274E59` → [sub_00274581 + 0x126](Unknown_function_00274581.md) (`tail-transfer`)
  - `0x00274E62` → [sub_00274581 + 0x126](Unknown_function_00274581.md) (`tail-transfer`)
  - `0x00274F05` → [sub_00273F95 + 0x288](Unknown_function_00273F95.md) (`tail-transfer`)
  - `0x00274F22` → [sub_00273F95 + 0x1F0](Unknown_function_00273F95.md) (`tail-transfer`)
  - `0x00274F2D` → [sub_00273F95 + 0x1F0](Unknown_function_00273F95.md) (`tail-transfer`)
  - `0x00274F39` → [sub_002746E8 + 0x4E](Unknown_function_002746E8.md) (`tail-transfer`)
  - `0x00274F46` → [sub_002746E8 + 0x4E](Unknown_function_002746E8.md) (`tail-transfer`)
  - `0x00274F62` → [sub_00274581 + 0xC6](Unknown_function_00274581.md) (`tail-transfer`)
  - `0x00274F98` → [sub_00274581 + 0xFF](Unknown_function_00274581.md) (`tail-transfer`)
  - `0x00274FCB` → [sub_00274581 + 0xDD](Unknown_function_00274581.md) (`tail-transfer`)
  - `0x00274FD7` → [sub_00274581 + 0x9F](Unknown_function_00274581.md) (`tail-transfer`)
  - `0x00274FF6` → [sub_00273F95 + 0x110](Unknown_function_00273F95.md) (`tail-transfer`)
  - `0x0027506C` → [sub_002746E8 + 0x1B](Unknown_function_002746E8.md) (`tail-transfer`)
  - `0x002750E4` → [sub_002746E8 + 0x4A](Unknown_function_002746E8.md) (`tail-transfer`)
  - `0x00275283` → [sub_00274581 + 0xFF](Unknown_function_00274581.md) (`tail-transfer`)
  - `0x0027539C` → [sub_00273F95 + 0x65](Unknown_function_00273F95.md) (`tail-transfer`)
  - `0x002753CA` → [sub_00274581 + 0xFF](Unknown_function_00274581.md) (`tail-transfer`)
  - `0x00275451` → [sub_00273F95 + 0xD6](Unknown_function_00273F95.md) (`tail-transfer`)
  - `0x00275467` → [sub_00273F95 + 0x82](Unknown_function_00273F95.md) (`tail-transfer`)
  - `0x002754A0` → [sub_00273F95 + 0x82](Unknown_function_00273F95.md) (`tail-transfer`)
  - `0x00275530` → [sub_00274581 + 0x9F](Unknown_function_00274581.md) (`tail-transfer`)
  - `0x00275584` → [sub_00274581 + 0x9F](Unknown_function_00274581.md) (`tail-transfer`)
  - `0x0027558E` → [sub_00274581 + 0x9F](Unknown_function_00274581.md) (`tail-transfer`)
  - `0x002755AE` → [sub_00274581 + 0x9F](Unknown_function_00274581.md) (`tail-transfer`)
  - `0x002755B8` → [sub_00274581 + 0x9F](Unknown_function_00274581.md) (`tail-transfer`)
  - `0x002755F1` → [sub_00274581 + 0x9F](Unknown_function_00274581.md) (`tail-transfer`)
  - `0x00275647` → [sub_00274581 + 0x9F](Unknown_function_00274581.md) (`tail-transfer`)
  - `0x00275651` → [sub_00274581 + 0x9F](Unknown_function_00274581.md) (`tail-transfer`)
  - `0x00275671` → [sub_00274581 + 0x9F](Unknown_function_00274581.md) (`tail-transfer`)
  - `0x0027567B` → [sub_00274581 + 0x9F](Unknown_function_00274581.md) (`tail-transfer`)
  - `0x00275698` → [sub_00273F95 + 0x4DC](Unknown_function_00273F95.md) (`tail-transfer`)
  - `0x002756A6` → [sub_002746E8 + 0xE](Unknown_function_002746E8.md) (`tail-transfer`)
  - `0x002756B4` → [sub_002746E8 + 0xE](Unknown_function_002746E8.md) (`tail-transfer`)
  - `0x002756C2` → [sub_002746E8 + 0x11](Unknown_function_002746E8.md) (`tail-transfer`)
  - `0x002756DC` → [sub_002746E8 + 0x2C](Unknown_function_002746E8.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0027475D  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00274766  8B C7                           mov eax, edi
00274768  2B 43 10                        sub eax, dword ptr [rbx + 0x10]
0027476B  48 C1 F8 04                     sar rax, 4
0027476F  88 81 60 04 00 00               mov byte ptr [rcx + 0x460], al
00274775  8B 4F 08                        mov ecx, dword ptr [rdi + 8]
00274778  41 BC 01 00 00 00               mov r12d, 1
0027477E  8B C1                           mov eax, ecx
00274780  83 E1 07                        and ecx, 7
00274783  C1 E8 03                        shr eax, 3
00274786  8D 04 C5 F8 FF FF FF            lea eax, [rax*8 - 8]
0027478D  0B C1                           or eax, ecx
0027478F  8B F0                           mov esi, eax
00274791  89 47 08                        mov dword ptr [rdi + 8], eax
00274794  C1 EE 03                        shr esi, 3
00274797  89 74 24 38                     mov dword ptr [rsp + 0x38], esi
0027479B  85 F6                           test esi, esi
0027479D  0F 85 35 02 00 00               jne 0x1402749d8
002747A3  48 8B 37                        mov rsi, qword ptr [rdi]
002747A6  A8 02                           test al, 2
002747A8  0F 84 1C 05 00 00               je 0x140274cca
002747AE  48 83 E6 FC                     and rsi, 0xfffffffffffffffc
002747B2  48 85 F6                        test rsi, rsi
002747B5  0F 84 98 00 00 00               je 0x140274853
002747BB  41 84 C4                        test r12b, al
002747BE  74 43                           je 0x140274803
002747C0  33 C0                           xor eax, eax
002747C2  45 32 F6                        xor r14b, r14b
002747C5  39 05 BD 27 D5 00               cmp dword ptr [rip + 0xd527bd], eax
002747CB  44 8B E0                        mov r12d, eax
002747CE  0F 85 FB 0B 00 00               jne 0x1402753cf
002747D4  83 BE E0 05 00 00 00            cmp dword ptr [rsi + 0x5e0], 0
002747DB  0F 84 D9 0C 00 00               je 0x1402754ba
002747E1  F0 FF 8E E0 05 00 00            lock dec dword ptr [rsi + 0x5e0]
002747E8  45 84 F6                        test r14b, r14b
002747EB  0F 85 E0 0D 00 00               jne 0x1402755d1
002747F1  8B 47 08                        mov eax, dword ptr [rdi + 8]
002747F4  41 BC 01 00 00 00               mov r12d, 1
002747FA  83 E0 FE                        and eax, 0xfffffffe
002747FD  89 47 08                        mov dword ptr [rdi + 8], eax
00274800  45 33 FF                        xor r15d, r15d
00274803  A8 04                           test al, 4
00274805  74 10                           je 0x140274817
00274807  F0 FF 8E E4 05 00 00            lock dec dword ptr [rsi + 0x5e4]
0027480E  8B 47 08                        mov eax, dword ptr [rdi + 8]
00274811  83 E0 FB                        and eax, 0xfffffffb
00274814  89 47 08                        mov dword ptr [rdi + 8], eax
00274817  A8 02                           test al, 2
00274819  74 38                           je 0x140274853
0027481B  83 3D EE 07 D5 00 00            cmp dword ptr [rip + 0xd507ee], 0
00274822  74 14                           je 0x140274838
00274824  41 B9 44 66 6C 74               mov r9d, 0x746c6644
0027482A  48 8D 4E D0                     lea rcx, [rsi - 0x30]
0027482E  45 8B C4                        mov r8d, r12d
00274831  33 D2                           xor edx, edx
00274833  E8 AC C1 F9 FF                  call 0x1402109e4
00274838  48 C7 C0 FF FF FF FF            mov rax, 0xffffffffffffffff
0027483F  F0 48 0F C1 46 D0               lock xadd qword ptr [rsi - 0x30], rax
00274845  48 83 E8 01                     sub rax, 1
00274849  0F 8E DA 09 00 00               jle 0x140275229
0027484F  83 67 08 FD                     and dword ptr [rdi + 8], 0xfffffffd
00274853  4C 89 3F                        mov qword ptr [rdi], r15
00274856  49 8B F7                        mov rsi, r15
00274859  83 7B 40 01                     cmp dword ptr [rbx + 0x40], 1
0027485D  8B 43 44                        mov eax, dword ptr [rbx + 0x44]
00274860  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
00274864  77 15                           ja 0x14027487b
00274866  83 7B 4C 00                     cmp dword ptr [rbx + 0x4c], 0
0027486A  0F 85 8B 07 00 00               jne 0x140274ffb
00274870  8B 4B 48                        mov ecx, dword ptr [rbx + 0x48]
00274873  85 C9                           test ecx, ecx
00274875  0F 85 B7 0A 00 00               jne 0x140275332
0027487B  41 8B CF                        mov ecx, r15d
0027487E  8B 43 40                        mov eax, dword ptr [rbx + 0x40]
00274881  FF C8                           dec eax
00274883  03 C8                           add ecx, eax
00274885  89 4B 40                        mov dword ptr [rbx + 0x40], ecx
00274888  75 05                           jne 0x14027488f
0027488A  66 44 89 7B 18                  mov word ptr [rbx + 0x18], r15w
0027488F  83 7B 4C 00                     cmp dword ptr [rbx + 0x4c], 0
00274893  75 0F                           jne 0x1402748a4
00274895  83 7B 48 00                     cmp dword ptr [rbx + 0x48], 0
00274899  75 09                           jne 0x1402748a4
0027489B  B9 F9 00 00 00                  mov ecx, 0xf9
002748A0  66 21 4B 1A                     and word ptr [rbx + 0x1a], cx
002748A4  44 0F B6 7B 1B                  movzx r15d, byte ptr [rbx + 0x1b]
002748A9  48 85 F6                        test rsi, rsi
002748AC  74 10                           je 0x1402748be
002748AE  8B 43 38                        mov eax, dword ptr [rbx + 0x38]
002748B1  83 E0 07                        and eax, 7
002748B4  48 89 73 30                     mov qword ptr [rbx + 0x30], rsi
002748B8  83 C8 08                        or eax, 8
002748BB  89 43 38                        mov dword ptr [rbx + 0x38], eax
002748BE  F6 05 41 22 D5 00 01            test byte ptr [rip + 0xd52241], 1
002748C5  0F 85 A3 00 00 00               jne 0x14027496e
002748CB  0F 0D 4C 24 48                  prefetchw byte ptr [rsp + 0x48]
002748D0  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
002748D5  48 85 C0                        test rax, rax
002748D8  75 2A                           jne 0x140274904
002748DA  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
002748DF  48 8D 44 24 48                  lea rax, [rsp + 0x48]
002748E4  45 33 C9                        xor r9d, r9d
002748E7  F0 4C 0F B1 09                  lock cmpxchg qword ptr [rcx], r9
002748EC  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
002748F1  48 3B C1                        cmp rax, rcx
002748F4  0F 84 90 00 00 00               je 0x14027498a
002748FA  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
002748FF  E8 9C 31 FA FF                  call 0x140217aa0
00274904  4C 8D 40 08                     lea r8, [rax + 8]
00274908  45 33 C9                        xor r9d, r9d
0027490B  4C 89 4C 24 48                  mov qword ptr [rsp + 0x48], r9
00274910  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
00274915  48 8B C1                        mov rax, rcx
00274918  49 87 00                        xchg qword ptr [r8], rax
0027491B  32 C1                           xor al, cl
0027491D  A8 04                           test al, 4
0027491F  74 69                           je 0x14027498a
00274921  F0 44 09 0C 24                  lock or dword ptr [rsp], r9d
00274926  49 C1 E8 05                     shr r8, 5
0027492A  4C 8D 15 CF B6 D8 FF            lea r10, [rip - 0x274931]
00274931  41 83 E0 7F                     and r8d, 0x7f
00274935  E8 A6 32 FA FF                  call 0x140217be0
0027493A  41 8B D1                        mov edx, r9d
0027493D  0F B6 F8                        movzx edi, al
00274940  4B 87 94 C2 20 1B F2 00         xchg qword ptr [r10 + r8*8 + 0xf21b20], rdx
00274948  E8 A7 31 FA FF                  call 0x140217af4
0027494D  40 84 FF                        test dil, dil
00274950  74 38                           je 0x14027498a
00274952  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
0027495B  4C 8B 81 B8 8E 00 00            mov r8, qword ptr [rcx + 0x8eb8]
00274962  4D 85 C0                        test r8, r8
00274965  0F 85 C1 06 00 00               jne 0x14027502c
0027496B  FB                              sti
0027496C  EB 1C                           jmp 0x14027498a
0027496E  8B 05 E4 94 C9 00               mov eax, dword ptr [rip + 0xc994e4]
00274974  85 C0                           test eax, eax
00274976  0F 85 4F FF FF FF               jne 0x1402748cb
0027497C  48 8B 55 48                     mov rdx, qword ptr [rbp + 0x48]
00274980  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
00274985  E8 66 30 FA FF                  call 0x1402179f0
0027498A  83 3D 8F 23 D5 00 00            cmp dword ptr [rip + 0xd5238f], 0
00274991  0F B6 7C 24 58                  movzx edi, byte ptr [rsp + 0x58]
00274996  74 0D                           je 0x1402749a5
00274998  44 0F 20 C1                     mov rcx, cr8
0027499C  40 0F B6 D7                     movzx edx, dil
002749A0  E8 F3 0C 28 00                  call 0x1404f5698
002749A5  44 0F 22 C7                     mov cr8, rdi
002749A9  48 85 F6                        test rsi, rsi
002749AC  41 BE 03 00 00 00               mov r14d, 3
002749B2  41 8B FC                        mov edi, r12d
002749B5  41 8B F4                        mov esi, r12d
002749B8  41 0F 45 FE                     cmovne edi, r14d
002749BC  48 83 7D 80 00                  cmp qword ptr [rbp - 0x80], 0
002749C1  0F 85 16 04 00 00               jne 0x140274ddd
002749C7  BE 42 00 01 00                  mov esi, 0x10042
002749CC  33 C0                           xor eax, eax
002749CE  89 74 24 60                     mov dword ptr [rsp + 0x60], esi
002749D2  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
002749D6  EB 5A                           jmp 0x140274a32
002749D8  F6 05 27 21 D5 00 01            test byte ptr [rip + 0xd52127], 1
002749DF  BE 52 00 01 00                  mov esi, 0x10052
002749E4  44 8B 63 44                     mov r12d, dword ptr [rbx + 0x44]
002749E8  89 74 24 60                     mov dword ptr [rsp + 0x60], esi
002749EC  44 89 64 24 44                  mov dword ptr [rsp + 0x44], r12d
002749F1  0F 84 2B 02 00 00               je 0x140274c22
002749F7  8B 05 5B 94 C9 00               mov eax, dword ptr [rip + 0xc9945b]
002749FD  85 C0                           test eax, eax
002749FF  0F 85 1D 02 00 00               jne 0x140274c22
00274A05  48 8B 55 48                     mov rdx, qword ptr [rbp + 0x48]
00274A09  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
00274A0E  E8 DD 2F FA FF                  call 0x1402179f0
00274A13  44 39 3D 06 23 D5 00            cmp dword ptr [rip + 0xd52306], r15d
00274A1A  0F B6 7C 24 58                  movzx edi, byte ptr [rsp + 0x58]
00274A1F  74 0D                           je 0x140274a2e
00274A21  44 0F 20 C1                     mov rcx, cr8
00274A25  40 0F B6 D7                     movzx edx, dil
00274A29  E8 6A 0C 28 00                  call 0x1404f5698
00274A2E  44 0F 22 C7                     mov cr8, rdi
00274A32  65 FF 04 25 70 90 00 00         inc dword ptr gs:[0x9070]
00274A3A  45 85 ED                        test r13d, r13d
00274A3D  0F 84 F3 FC FF FF               je 0x140274736
00274A43  0F 57 C0                        xorps xmm0, xmm0
00274A46  0F 11 45 C8                     movups xmmword ptr [rbp - 0x38], xmm0
00274A4A  0F 11 45 D8                     movups xmmword ptr [rbp - 0x28], xmm0
00274A4E  0F 11 45 E8                     movups xmmword ptr [rbp - 0x18], xmm0
00274A52  0F 31                           rdtsc
00274A54  65 4C 8B 34 25 20 00 00 00      mov r14, qword ptr gs:[0x20]
00274A5D  48 C1 E2 20                     shl rdx, 0x20
00274A61  48 0B C2                        or rax, rdx
00274A64  48 89 45 90                     mov qword ptr [rbp - 0x70], rax
00274A68  41 FF 86 70 8F 00 00            inc dword ptr [r14 + 0x8f70]
00274A6F  41 0F B6 86 D0 00 00 00         movzx eax, byte ptr [r14 + 0xd0]
00274A77  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00274A80  66 89 44 24 40                  mov word ptr [rsp + 0x40], ax
00274A85  41 0F B6 86 D1 00 00 00         movzx eax, byte ptr [r14 + 0xd1]
00274A8D  88 44 24 30                     mov byte ptr [rsp + 0x30], al
00274A91  48 83 B9 20 06 00 00 00         cmp qword ptr [rcx + 0x620], 0
00274A99  0F 84 97 FC FF FF               je 0x140274736
00274A9F  65 4C 8B 3C 25 88 01 00 00      mov r15, qword ptr gs:[0x188]
00274AA8  44 8B E6                        mov r12d, esi
00274AAB  41 81 E4 00 00 FF FF            and r12d, 0xffff0000
00274AB2  41 8B 87 A0 05 00 00            mov eax, dword ptr [r15 + 0x5a0]
00274AB9  A8 01                           test al, 1
00274ABB  0F 85 75 FC FF FF               jne 0x140274736
00274AC1  49 8B B7 20 06 00 00            mov rsi, qword ptr [r15 + 0x620]
00274AC8  44 8B 2D 99 39 BF 00            mov r13d, dword ptr [rip + 0xbf3999]
00274ACF  48 85 F6                        test rsi, rsi
00274AD2  75 4C                           jne 0x140274b20
00274AD4  BA 00 02 00 00                  mov edx, 0x200
00274AD9  8D 4E 48                        lea ecx, [rsi + 0x48]
00274ADC  41 B8 52 65 54 72               mov r8d, 0x72546552
00274AE2  E8 09 D6 90 00                  call 0x140b820f0
00274AE7  48 8B F8                        mov rdi, rax
00274AEA  48 85 C0                        test rax, rax
00274AED  0F 84 43 FC FF FF               je 0x140274736
00274AF3  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
00274AF7  44 89 60 1C                     mov dword ptr [rax + 0x1c], r12d
00274AFB  33 C0                           xor eax, eax
00274AFD  89 47 20                        mov dword ptr [rdi + 0x20], eax
00274B00  44 89 6F 28                     mov dword ptr [rdi + 0x28], r13d
00274B04  F0 49 0F B1 BF 20 06 00 00      lock cmpxchg qword ptr [r15 + 0x620], rdi
00274B0D  48 8B F0                        mov rsi, rax
00274B10  0F 84 C3 01 00 00               je 0x140274cd9
00274B16  33 D2                           xor edx, edx
00274B18  48 8B CF                        mov rcx, rdi
00274B1B  E8 50 DD 90 00                  call 0x140b82870
00274B20  45 33 FF                        xor r15d, r15d
00274B23  41 8B C7                        mov eax, r15d
00274B26  41 8B CF                        mov ecx, r15d
00274B29  83 F9 08                        cmp ecx, 8
00274B2C  73 32                           jae 0x140274b60
00274B2E  8B 56 1C                        mov edx, dword ptr [rsi + 0x1c]
00274B31  41 3B D4                        cmp edx, r12d
00274B34  75 0C                           jne 0x140274b42
00274B36  48 39 5E 10                     cmp qword ptr [rsi + 0x10], rbx
00274B3A  75 06                           jne 0x140274b42
00274B3C  44 39 6E 28                     cmp dword ptr [rsi + 0x28], r13d
00274B40  74 45                           je 0x140274b87
00274B42  48 85 C0                        test rax, rax
00274B45  0F 85 CC 00 00 00               jne 0x140274c17
00274B4B  85 D2                           test edx, edx
00274B4D  0F 84 C1 00 00 00               je 0x140274c14
00274B53  44 39 6E 28                     cmp dword ptr [rsi + 0x28], r13d
00274B57  0F 8D BA 00 00 00               jge 0x140274c17
00274B5D  48 8B C6                        mov rax, rsi
00274B60  48 8B F0                        mov rsi, rax
00274B63  48 85 C0                        test rax, rax
00274B66  74 1F                           je 0x140274b87
00274B68  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
00274B6C  44 89 60 1C                     mov dword ptr [rax + 0x1c], r12d
00274B70  4C 89 78 20                     mov qword ptr [rax + 0x20], r15
00274B74  4C 89 38                        mov qword ptr [rax], r15
00274B77  4C 89 78 08                     mov qword ptr [rax + 8], r15
00274B7B  44 89 78 18                     mov dword ptr [rax + 0x18], r15d
00274B7F  44 89 68 28                     mov dword ptr [rax + 0x28], r13d
00274B83  44 89 78 2C                     mov dword ptr [rax + 0x2c], r15d
00274B87  48 8B FE                        mov rdi, rsi
00274B8A  48 85 F6                        test rsi, rsi
00274B8D  0F 84 A3 FB FF FF               je 0x140274736
00274B93  83 7F 20 00                     cmp dword ptr [rdi + 0x20], 0
00274B97  74 72                           je 0x140274c0b
00274B99  41 FF 86 74 8F 00 00            inc dword ptr [r14 + 0x8f74]
00274BA0  8B 44 24 38                     mov eax, dword ptr [rsp + 0x38]
00274BA4  FF C0                           inc eax
00274BA6  39 47 24                        cmp dword ptr [rdi + 0x24], eax
00274BA9  0F 82 32 0B 00 00               jb 0x1402756e1
00274BAF  44 8B 44 24 60                  mov r8d, dword ptr [rsp + 0x60]
00274BB4  41 81 F8 42 00 01 00            cmp r8d, 0x10042
00274BBB  0F 85 71 03 00 00               jne 0x140274f32
00274BC1  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
00274BC5  48 83 F8 02                     cmp rax, 2
00274BC9  0F 87 1A 0B 00 00               ja 0x1402756e9
00274BCF  4D 8B CF                        mov r9, r15
00274BD2  48 83 3F 01                     cmp qword ptr [rdi], 1
00274BD6  0F 87 6D 05 00 00               ja 0x140275149
00274BDC  8B 4F 2C                        mov ecx, dword ptr [rdi + 0x2c]
00274BDF  44 8B 54 24 44                  mov r10d, dword ptr [rsp + 0x44]
00274BE4  44 3B D1                        cmp r10d, ecx
00274BE7  0F 87 25 0B 00 00               ja 0x140275712
00274BED  41 8B 86 F0 8E 00 00            mov eax, dword ptr [r14 + 0x8ef0]
00274BF4  33 D2                           xor edx, edx
00274BF6  41 03 86 EC 8E 00 00            add eax, dword ptr [r14 + 0x8eec]
00274BFD  F7 35 0D 9F B9 00               div dword ptr [rip + 0xb99f0d]
00274C03  85 D2                           test edx, edx
00274C05  0F 84 61 05 00 00               je 0x14027516c
00274C0B  44 89 7F 1C                     mov dword ptr [rdi + 0x1c], r15d
00274C0F  E9 22 FB FF FF                  jmp 0x140274736
00274C14  48 8B C6                        mov rax, rsi
00274C17  48 83 C6 40                     add rsi, 0x40
00274C1B  FF C1                           inc ecx
00274C1D  E9 07 FF FF FF                  jmp 0x140274b29
00274C22  0F 0D 4C 24 48                  prefetchw byte ptr [rsp + 0x48]
00274C27  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
00274C2C  48 85 C0                        test rax, rax
00274C2F  75 27                           jne 0x140274c58
00274C31  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
00274C36  48 8D 44 24 48                  lea rax, [rsp + 0x48]
00274C3B  F0 4C 0F B1 39                  lock cmpxchg qword ptr [rcx], r15
00274C40  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
00274C45  48 3B C1                        cmp rax, rcx
00274C48  0F 84 C5 FD FF FF               je 0x140274a13
00274C4E  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
00274C53  E8 48 2E FA FF                  call 0x140217aa0
00274C58  4C 8D 40 08                     lea r8, [rax + 8]
00274C5C  4C 89 7C 24 48                  mov qword ptr [rsp + 0x48], r15
00274C61  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
00274C66  48 8B C1                        mov rax, rcx
00274C69  49 87 00                        xchg qword ptr [r8], rax
00274C6C  32 C1                           xor al, cl
00274C6E  A8 04                           test al, 4
00274C70  0F 84 9D FD FF FF               je 0x140274a13
00274C76  F0 44 09 3C 24                  lock or dword ptr [rsp], r15d
00274C7B  49 C1 E8 05                     shr r8, 5
00274C7F  4C 8D 15 7A B3 D8 FF            lea r10, [rip - 0x274c86]
00274C86  41 83 E0 7F                     and r8d, 0x7f
00274C8A  E8 51 2F FA FF                  call 0x140217be0
00274C8F  49 8B D7                        mov rdx, r15
00274C92  0F B6 F8                        movzx edi, al
00274C95  4B 87 94 C2 20 1B F2 00         xchg qword ptr [r10 + r8*8 + 0xf21b20], rdx
00274C9D  E8 52 2E FA FF                  call 0x140217af4
00274CA2  40 84 FF                        test dil, dil
00274CA5  0F 84 68 FD FF FF               je 0x140274a13
00274CAB  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
00274CB4  4C 8B 81 B8 8E 00 00            mov r8, qword ptr [rcx + 0x8eb8]
00274CBB  4D 85 C0                        test r8, r8
00274CBE  0F 85 D9 02 00 00               jne 0x140274f9d
00274CC4  FB                              sti
00274CC5  E9 49 FD FF FF                  jmp 0x140274a13
00274CCA  40 F6 C6 03                     test sil, 3
00274CCE  0F 85 7F FB FF FF               jne 0x140274853
00274CD4  E9 D9 FA FF FF                  jmp 0x1402747b2
00274CD9  45 33 FF                        xor r15d, r15d
00274CDC  E9 B2 FE FF FF                  jmp 0x140274b93
00274CE1  48 89 11                        mov qword ptr [rcx], rdx
00274CE4  48 89 4A 08                     mov qword ptr [rdx + 8], rcx
00274CE8  0F B6 48 10                     movzx ecx, byte ptr [rax + 0x10]
00274CEC  40 3A CE                        cmp cl, sil
00274CEF  0F 85 72 02 00 00               jne 0x140274f67
00274CF5  44 0F B7 40 12                  movzx r8d, word ptr [rax + 0x12]
00274CFA  45 33 C9                        xor r9d, r9d
00274CFD  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
00274D02  48 8B D0                        mov rdx, rax
00274D05  E8 C6 B9 0D 00                  call 0x1403506d0
00274D0A  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
00274D0F  4D 8D 4D 18                     lea r9, [r13 + 0x18]
00274D13  84 C0                           test al, al
00274D15  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
00274D1A  0F 84 60 F9 FF FF               je 0x140274680
00274D20  41 29 75 1C                     sub dword ptr [r13 + 0x1c], esi
00274D24  4D 8D 4D 18                     lea r9, [r13 + 0x18]
00274D28  0F 85 52 F9 FF FF               jne 0x140274680
00274D2E  F0 41 81 65 18 7F FF FF FF      lock and dword ptr [r13 + 0x18], 0xffffff7f
00274D37  48 8B 45 88                     mov rax, qword ptr [rbp - 0x78]
00274D3B  48 3B 44 24 70                  cmp rax, qword ptr [rsp + 0x70]
00274D40  0F 85 7F 02 00 00               jne 0x140274fc5
00274D46  4C 8B 74 24 68                  mov r14, qword ptr [rsp + 0x68]
00274D4B  49 8B CE                        mov rcx, r14
00274D4E  49 8B 56 08                     mov rdx, qword ptr [r14 + 8]
00274D52  E8 D1 43 FA FF                  call 0x140219128
00274D57  45 85 FF                        test r15d, r15d
00274D5A  0F 85 D8 03 00 00               jne 0x140275138
00274D60  40 F6 C7 02                     test dil, 2
00274D64  0F 85 B2 03 00 00               jne 0x14027511c
00274D6A  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
00274D6F  45 8B CF                        mov r9d, r15d
00274D72  44 8B C6                        mov r8d, esi
00274D75  88 44 24 20                     mov byte ptr [rsp + 0x20], al
00274D79  33 D2                           xor edx, edx
00274D7B  49 8B CE                        mov rcx, r14
00274D7E  E8 6D CF FD FF                  call 0x140251cf0
00274D83  E9 5A F4 FF FF                  jmp 0x1402741e2
00274D88  4C 89 73 28                     mov qword ptr [rbx + 0x28], r14
00274D8C  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
00274D91  48 8B 71 10                     mov rsi, qword ptr [rcx + 0x10]
00274D95  48 85 C0                        test rax, rax
00274D98  0F 85 32 02 00 00               jne 0x140274fd0
00274D9E  48 89 49 08                     mov qword ptr [rcx + 8], rcx
00274DA2  48 89 09                        mov qword ptr [rcx], rcx
00274DA5  48 89 4C 24 70                  mov qword ptr [rsp + 0x70], rcx
00274DAA  FF 4B 4C                        dec dword ptr [rbx + 0x4c]
00274DAD  41 8B CD                        mov ecx, r13d
00274DB0  E9 F0 F2 FF FF                  jmp 0x1402740a5
00274DB5  41 0F 0D 08                     prefetchw byte ptr [r8]
00274DB9  41 8B 00                        mov eax, dword ptr [r8]
00274DBC  8B D0                           mov edx, eax
00274DBE  0F BA F2 15                     btr edx, 0x15
00274DC2  F0 41 0F B1 10                  lock cmpxchg dword ptr [r8], edx
00274DC7  75 F3                           jne 0x140274dbc
00274DC9  0F BA E0 15                     bt eax, 0x15
00274DCD  0F 83 7F F7 FF FF               jae 0x140274552
00274DD3  E8 F8 E3 FE FF                  call 0x1402631d0
00274DD8  E9 75 F7 FF FF                  jmp 0x140274552
00274DDD  44 0F 20 C0                     mov rax, cr8
00274DE1  48 89 45 90                     mov qword ptr [rbp - 0x70], rax
00274DE5  B9 02 00 00 00                  mov ecx, 2
00274DEA  44 0F 22 C1                     mov cr8, rcx
00274DEE  83 3D 2B 1F D5 00 00            cmp dword ptr [rip + 0xd51f2b], 0
00274DF5  0F 85 EE 02 00 00               jne 0x1402750e9
00274DFB  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
00274E04  4C 8B 65 80                     mov r12, qword ptr [rbp - 0x80]
00274E08  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
00274E0D  49 8B 04 24                     mov rax, qword ptr [r12]
00274E11  4D 8D 6C 24 18                  lea r13, [r12 + 0x18]
00274E16  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
00274E1B  49 8B CD                        mov rcx, r13
00274E1E  4C 89 65 88                     mov qword ptr [rbp - 0x78], r12
00274E22  4C 89 6C 24 38                  mov qword ptr [rsp + 0x38], r13
00274E27  E8 64 CE FD FF                  call 0x140251c90
00274E2C  49 83 C5 08                     add r13, 8
00274E30  41 C7 44 24 1C 01 00 00 00      mov dword ptr [r12 + 0x1c], 1
00274E39  4D 8B 65 00                     mov r12, qword ptr [r13]
00274E3D  4C 8B 4C 24 38                  mov r9, qword ptr [rsp + 0x38]
00274E42  4D 3B E5                        cmp r12, r13
00274E45  74 5A                           je 0x140274ea1
00274E47  49 8B 14 24                     mov rdx, qword ptr [r12]
00274E4B  49 8B C4                        mov rax, r12
00274E4E  4C 8B E2                        mov r12, rdx
00274E51  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
00274E55  48 39 42 08                     cmp qword ptr [rdx + 8], rax
00274E59  0F 85 48 F8 FF FF               jne 0x1402746a7
00274E5F  48 39 01                        cmp qword ptr [rcx], rax
00274E62  0F 85 3F F8 FF FF               jne 0x1402746a7
00274E68  48 89 11                        mov qword ptr [rcx], rdx
00274E6B  48 89 4A 08                     mov qword ptr [rdx + 8], rcx
00274E6F  0F B6 48 10                     movzx ecx, byte ptr [rax + 0x10]
00274E73  80 F9 01                        cmp cl, 1
00274E76  0F 85 7D 02 00 00               jne 0x1402750f9
00274E7C  44 0F B7 40 12                  movzx r8d, word ptr [rax + 0x12]
00274E81  45 33 C9                        xor r9d, r9d
00274E84  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
00274E89  48 8B D0                        mov rdx, rax
00274E8C  E8 3F B8 0D 00                  call 0x1403506d0
00274E91  4C 8B 4C 24 38                  mov r9, qword ptr [rsp + 0x38]
00274E96  84 C0                           test al, al
00274E98  74 A8                           je 0x140274e42
00274E9A  41 83 69 04 01                  sub dword ptr [r9 + 4], 1
00274E9F  75 A1                           jne 0x140274e42
00274EA1  48 8B 45 88                     mov rax, qword ptr [rbp - 0x78]
00274EA5  F0 81 60 18 7F FF FF FF         lock and dword ptr [rax + 0x18], 0xffffff7f
00274EAD  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
00274EB2  48 3B 45 80                     cmp rax, qword ptr [rbp - 0x80]
00274EB6  0F 85 71 02 00 00               jne 0x14027512d
00274EBC  4C 8B 74 24 68                  mov r14, qword ptr [rsp + 0x68]
00274EC1  49 8B CE                        mov rcx, r14
00274EC4  49 8B 56 08                     mov rdx, qword ptr [r14 + 8]
00274EC8  E8 5B 42 FA FF                  call 0x140219128
00274ECD  45 85 FF                        test r15d, r15d
00274ED0  0F 85 19 03 00 00               jne 0x1402751ef
00274ED6  40 F6 C7 02                     test dil, 2
00274EDA  0F 85 FE 02 00 00               jne 0x1402751de
00274EE0  48 8B 45 90                     mov rax, qword ptr [rbp - 0x70]
00274EE4  45 8B CF                        mov r9d, r15d
00274EE7  44 8B C6                        mov r8d, esi
00274EEA  88 44 24 20                     mov byte ptr [rsp + 0x20], al
00274EEE  33 D2                           xor edx, edx
00274EF0  49 8B CE                        mov rcx, r14
00274EF3  E8 F8 CD FD FF                  call 0x140251cf0
00274EF8  44 8B 6C 24 60                  mov r13d, dword ptr [rsp + 0x60]
00274EFD  E9 C5 FA FF FF                  jmp 0x1402749c7
00274F02  41 8B C7                        mov eax, r15d
00274F05  E9 13 F3 FF FF                  jmp 0x14027421d
00274F0A  41 0F 0D 08                     prefetchw byte ptr [r8]
00274F0E  41 8B 00                        mov eax, dword ptr [r8]
00274F11  8B D0                           mov edx, eax
00274F13  0F BA F2 15                     btr edx, 0x15
00274F17  F0 41 0F B1 10                  lock cmpxchg dword ptr [r8], edx
00274F1C  75 F3                           jne 0x140274f11
00274F1E  0F BA E0 15                     bt eax, 0x15
00274F22  0F 83 5D F2 FF FF               jae 0x140274185
00274F28  E8 A3 E2 FE FF                  call 0x1402631d0
00274F2D  E9 53 F2 FF FF                  jmp 0x140274185
00274F32  41 81 F8 52 00 01 00            cmp r8d, 0x10052
00274F39  0F 85 F7 F7 FF FF               jne 0x140274736
00274F3F  C7 47 20 02 00 00 00            mov dword ptr [rdi + 0x20], 2
00274F46  E9 EB F7 FF FF                  jmp 0x140274736
00274F4B  48 89 10                        mov qword ptr [rax], rdx
00274F4E  48 89 42 08                     mov qword ptr [rdx + 8], rax
00274F52  E9 35 FE FF FF                  jmp 0x140274d8c
00274F57  0F B6 D1                        movzx edx, cl
00274F5A  0F B6 C8                        movzx ecx, al
00274F5D  E8 9A 07 28 00                  call 0x1404f56fc
00274F62  E9 E0 F6 FF FF                  jmp 0x140274647
00274F67  80 F9 02                        cmp cl, 2
00274F6A  0F 85 E6 02 00 00               jne 0x140275256
00274F70  C6 40 11 05                     mov byte ptr [rax + 0x11], 5
00274F74  48 8B D0                        mov rdx, rax
00274F77  48 8B 48 18                     mov rcx, qword ptr [rax + 0x18]
00274F7B  E8 B0 4B FA FF                  call 0x140219b30
00274F80  41 29 75 1C                     sub dword ptr [r13 + 0x1c], esi
00274F84  4D 8D 4D 18                     lea r9, [r13 + 0x18]
00274F88  0F 84 A0 FD FF FF               je 0x140274d2e
00274F8E  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
00274F93  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
00274F98  E9 E3 F6 FF FF                  jmp 0x140274680
00274F9D  41 0F 0D 08                     prefetchw byte ptr [r8]
00274FA1  41 8B 00                        mov eax, dword ptr [r8]
00274FA4  8B D0                           mov edx, eax
00274FA6  0F BA F2 15                     btr edx, 0x15
00274FAA  F0 41 0F B1 10                  lock cmpxchg dword ptr [r8], edx
00274FAF  75 F3                           jne 0x140274fa4
00274FB1  0F BA E0 15                     bt eax, 0x15
00274FB5  0F 83 09 FD FF FF               jae 0x140274cc4
00274FBB  E8 10 E2 FE FF                  call 0x1402631d0
00274FC0  E9 FF FC FF FF                  jmp 0x140274cc4
00274FC5  4C 8B E8                        mov r13, rax
00274FC8  48 8B 00                        mov rax, qword ptr [rax]
00274FCB  E9 8E F6 FF FF                  jmp 0x14027465e
00274FD0  48 8B 50 08                     mov rdx, qword ptr [rax + 8]
00274FD4  48 39 02                        cmp qword ptr [rdx], rax
00274FD7  0F 85 43 F6 FF FF               jne 0x140274620
00274FDD  48 89 01                        mov qword ptr [rcx], rax
00274FE0  48 89 51 08                     mov qword ptr [rcx + 8], rdx
00274FE4  48 89 0A                        mov qword ptr [rdx], rcx
00274FE7  48 89 48 08                     mov qword ptr [rax + 8], rcx
00274FEB  FF 4B 4C                        dec dword ptr [rbx + 0x4c]
00274FEE  48 89 4C 24 70                  mov qword ptr [rsp + 0x70], rcx
00274FF3  41 8B CD                        mov ecx, r13d
00274FF6  E9 AA F0 FF FF                  jmp 0x1402740a5
00274FFB  48 8D 4B 28                     lea rcx, [rbx + 0x28]
00274FFF  E8 6C DD 1B 00                  call 0x140432d70
00275004  48 85 C0                        test rax, rax
00275007  74 0F                           je 0x140275018
00275009  48 8B 70 10                     mov rsi, qword ptr [rax + 0x10]
0027500D  48 89 40 08                     mov qword ptr [rax + 8], rax
00275011  48 89 00                        mov qword ptr [rax], rax
00275014  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
00275018  FF 4B 4C                        dec dword ptr [rbx + 0x4c]
0027501B  B8 80 00 00 00                  mov eax, 0x80
00275020  66 09 43 1A                     or word ptr [rbx + 0x1a], ax
00275024  41 8B CC                        mov ecx, r12d
00275027  E9 52 F8 FF FF                  jmp 0x14027487e
0027502C  41 0F 0D 08                     prefetchw byte ptr [r8]
00275030  41 8B 00                        mov eax, dword ptr [r8]
00275033  8B D0                           mov edx, eax
00275035  0F BA F2 15                     btr edx, 0x15
00275039  F0 41 0F B1 10                  lock cmpxchg dword ptr [r8], edx
0027503E  75 F3                           jne 0x140275033
00275040  0F BA E0 15                     bt eax, 0x15
00275044  0F 83 21 F9 FF FF               jae 0x14027496b
0027504A  E8 81 E1 FE FF                  call 0x1402631d0
0027504F  E9 17 F9 FF FF                  jmp 0x14027496b
00275054  41 8B 86 F0 8E 00 00            mov eax, dword ptr [r14 + 0x8ef0]
0027505B  33 D2                           xor edx, edx
0027505D  41 03 86 EC 8E 00 00            add eax, dword ptr [r14 + 0x8eec]
00275064  F7 35 AE 9A B9 00               div dword ptr [rip + 0xb99aae]
0027506A  85 D2                           test edx, edx
0027506C  0F 85 91 F6 FF FF               jne 0x140274703
00275072  44 8B 54 24 44                  mov r10d, dword ptr [rsp + 0x44]
00275077  44 89 45 C0                     mov dword ptr [rbp - 0x40], r8d
0027507B  BA 01 00 00 00                  mov edx, 1
00275080  48 89 5D B8                     mov qword ptr [rbp - 0x48], rbx
00275084  41 B8 00 00 02 20               mov r8d, 0x20020000
0027508A  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
0027508E  48 89 45 98                     mov qword ptr [rbp - 0x68], rax
00275092  8B 47 24                        mov eax, dword ptr [rdi + 0x24]
00275095  89 45 B0                        mov dword ptr [rbp - 0x50], eax
00275098  4C 89 4D A0                     mov qword ptr [rbp - 0x60], r9
0027509C  41 B9 2B 05 00 00               mov r9d, 0x52b
002750A2  48 8B 07                        mov rax, qword ptr [rdi]
002750A5  48 89 45 A8                     mov qword ptr [rbp - 0x58], rax
002750A9  44 2B 57 2C                     sub r10d, dword ptr [rdi + 0x2c]
002750AD  44 89 55 C4                     mov dword ptr [rbp - 0x3c], r10d
002750B1  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
002750BA  48 C7 45 00 30 00 00 00         mov qword ptr [rbp], 0x30
002750C2  C7 44 24 20 02 18 60 01         mov dword ptr [rsp + 0x20], 0x1601802
002750CA  8B 88 10 05 00 00               mov ecx, dword ptr [rax + 0x510]
002750D0  48 8D 45 98                     lea rax, [rbp - 0x68]
002750D4  89 4D B4                        mov dword ptr [rbp - 0x4c], ecx
002750D7  48 8D 4D F8                     lea rcx, [rbp - 8]
002750DB  48 89 45 F8                     mov qword ptr [rbp - 8], rax
002750DF  E8 6C 02 FC FF                  call 0x140235350
002750E4  E9 49 F6 FF FF                  jmp 0x140274732
002750E9  0F B6 D1                        movzx edx, cl
002750EC  0F B6 C8                        movzx ecx, al
002750EF  E8 08 06 28 00                  call 0x1404f56fc
002750F4  E9 02 FD FF FF                  jmp 0x140274dfb
002750F9  80 F9 02                        cmp cl, 2
002750FC  0F 85 C9 01 00 00               jne 0x1402752cb
00275102  C6 40 11 05                     mov byte ptr [rax + 0x11], 5
00275106  48 8B D0                        mov rdx, rax
00275109  48 8B 48 18                     mov rcx, qword ptr [rax + 0x18]
0027510D  E8 1E 4A FA FF                  call 0x140219b30
00275112  4C 8B 4C 24 38                  mov r9, qword ptr [rsp + 0x38]
00275117  E9 7E FD FF FF                  jmp 0x140274e9a
0027511C  83 FE 01                        cmp esi, 1
0027511F  B8 01 00 00 00                  mov eax, 1
00275124  44 0F 44 F8                     cmove r15d, eax
00275128  E9 3D FC FF FF                  jmp 0x140274d6a
0027512D  4C 8B E0                        mov r12, rax
00275130  48 8B 00                        mov rax, qword ptr [rax]
00275133  E9 D9 FC FF FF                  jmp 0x140274e11
00275138  41 3B C7                        cmp eax, r15d
0027513B  BE 02 00 00 00                  mov esi, 2
00275140  44 0F 4F F8                     cmovg r15d, eax
00275144  E9 17 FC FF FF                  jmp 0x140274d60
00275149  41 8B 86 F0 8E 00 00            mov eax, dword ptr [r14 + 0x8ef0]
00275150  33 D2                           xor edx, edx
00275152  41 03 86 EC 8E 00 00            add eax, dword ptr [r14 + 0x8eec]
00275159  F7 35 B9 99 B9 00               div dword ptr [rip + 0xb999b9]
0027515F  85 D2                           test edx, edx
00275161  0F 85 75 FA FF FF               jne 0x140274bdc
00275167  44 8B 54 24 44                  mov r10d, dword ptr [rsp + 0x44]
0027516C  44 89 45 F0                     mov dword ptr [rbp - 0x10], r8d
00275170  BA 01 00 00 00                  mov edx, 1
00275175  48 89 5D E8                     mov qword ptr [rbp - 0x18], rbx
00275179  41 B8 00 00 02 20               mov r8d, 0x20020000
0027517F  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
00275183  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
00275187  8B 47 24                        mov eax, dword ptr [rdi + 0x24]
0027518A  89 45 E0                        mov dword ptr [rbp - 0x20], eax
0027518D  4C 89 4D D0                     mov qword ptr [rbp - 0x30], r9
00275191  41 B9 2B 05 00 00               mov r9d, 0x52b
00275197  48 8B 07                        mov rax, qword ptr [rdi]
0027519A  48 89 45 D8                     mov qword ptr [rbp - 0x28], rax
0027519E  44 2B 57 2C                     sub r10d, dword ptr [rdi + 0x2c]
002751A2  44 89 55 F4                     mov dword ptr [rbp - 0xc], r10d
002751A6  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
002751AF  48 C7 45 00 30 00 00 00         mov qword ptr [rbp], 0x30
002751B7  C7 44 24 20 02 18 60 01         mov dword ptr [rsp + 0x20], 0x1601802
002751BF  8B 88 10 05 00 00               mov ecx, dword ptr [rax + 0x510]
002751C5  48 8D 45 C8                     lea rax, [rbp - 0x38]
002751C9  89 4D E4                        mov dword ptr [rbp - 0x1c], ecx
002751CC  48 8D 4D F8                     lea rcx, [rbp - 8]
002751D0  48 89 45 F8                     mov qword ptr [rbp - 8], rax
002751D4  E8 77 01 FC FF                  call 0x140235350
002751D9  E9 2D FA FF FF                  jmp 0x140274c0b
002751DE  83 FE 01                        cmp esi, 1
002751E1  B8 01 00 00 00                  mov eax, 1
002751E6  44 0F 44 F8                     cmove r15d, eax
002751EA  E9 F1 FC FF FF                  jmp 0x140274ee0
002751EF  41 3B C7                        cmp eax, r15d
002751F2  BE 02 00 00 00                  mov esi, 2
002751F7  44 0F 4F F8                     cmovg r15d, eax
002751FB  E9 D6 FC FF FF                  jmp 0x140274ed6
00275200  48 8B 4F D8                     mov rcx, qword ptr [rdi - 0x28]
00275204  48 85 C9                        test rcx, rcx
00275207  75 7F                           jne 0x140275288
00275209  48 85 C0                        test rax, rax
0027520C  0F 89 36 02 00 00               jns 0x140275448
00275212  33 D2                           xor edx, edx
00275214  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00275219  44 8D 49 04                     lea r9d, [rcx + 4]
0027521D  4C 8B C7                        mov r8, rdi
00275220  8D 4A 18                        lea ecx, [rdx + 0x18]
00275223  E8 38 84 28 00                  call 0x1404fd660
00275228  CC                              int3
00275229  48 8B 4E D8                     mov rcx, qword ptr [rsi - 0x28]
0027522D  48 85 C9                        test rcx, rcx
00275230  0F 85 B9 00 00 00               jne 0x1402752ef
00275236  48 85 C0                        test rax, rax
00275239  0F 89 17 02 00 00               jns 0x140275456
0027523F  33 D2                           xor edx, edx
00275241  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00275246  44 8D 49 04                     lea r9d, [rcx + 4]
0027524A  4C 8B C6                        mov r8, rsi
0027524D  8D 4A 18                        lea ecx, [rdx + 0x18]
00275250  E8 0B 84 28 00                  call 0x1404fd660
00275255  CC                              int3
00275256  80 F9 04                        cmp cl, 4
00275259  0F 84 42 01 00 00               je 0x1402753a1
0027525F  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
00275264  45 33 C9                        xor r9d, r9d
00275267  41 B8 00 01 00 00               mov r8d, 0x100
0027526D  48 8B D0                        mov rdx, rax
00275270  E8 5B B4 0D 00                  call 0x1403506d0
00275275  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
0027527A  4D 8D 4D 18                     lea r9, [r13 + 0x18]
0027527E  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
00275283  E9 F8 F3 FF FF                  jmp 0x140274680
00275288  41 B9 03 00 00 00               mov r9d, 3
0027528E  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00275293  4C 8D 15 66 AD D8 FF            lea r10, [rip - 0x27529a]
0027529A  4C 8B C7                        mov r8, rdi
0027529D  48 8D 47 D0                     lea rax, [rdi - 0x30]
002752A1  48 C1 E8 08                     shr rax, 8
002752A5  0F B6 D0                        movzx edx, al
002752A8  41 8D 49 15                     lea ecx, [r9 + 0x15]
002752AC  0F B6 47 E8                     movzx eax, byte ptr [rdi - 0x18]
002752B0  48 33 D0                        xor rdx, rax
002752B3  0F B6 05 92 1B D5 00            movzx eax, byte ptr [rip + 0xd51b92]
002752BA  48 33 D0                        xor rdx, rax
002752BD  49 8B 94 D2 00 78 FC 00         mov rdx, qword ptr [r10 + rdx*8 + 0xfc7800]
002752C5  E8 96 83 28 00                  call 0x1404fd660
002752CA  CC                              int3
002752CB  80 F9 04                        cmp cl, 4
002752CE  0F 84 56 01 00 00               je 0x14027542a
002752D4  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
002752D9  45 33 C9                        xor r9d, r9d
002752DC  41 B8 00 01 00 00               mov r8d, 0x100
002752E2  48 8B D0                        mov rdx, rax
002752E5  E8 E6 B3 0D 00                  call 0x1403506d0
002752EA  E9 4E FB FF FF                  jmp 0x140274e3d
002752EF  41 B9 03 00 00 00               mov r9d, 3
002752F5  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
002752FA  4C 8D 15 FF AC D8 FF            lea r10, [rip - 0x275301]
00275301  4C 8B C6                        mov r8, rsi
00275304  48 8D 46 D0                     lea rax, [rsi - 0x30]
00275308  48 C1 E8 08                     shr rax, 8
0027530C  0F B6 D0                        movzx edx, al
0027530F  41 8D 49 15                     lea ecx, [r9 + 0x15]
00275313  0F B6 46 E8                     movzx eax, byte ptr [rsi - 0x18]
00275317  48 33 D0                        xor rdx, rax
0027531A  0F B6 05 2B 1B D5 00            movzx eax, byte ptr [rip + 0xd51b2b]
00275321  48 33 D0                        xor rdx, rax
00275324  49 8B 94 D2 00 78 FC 00         mov rdx, qword ptr [r10 + rdx*8 + 0xfc7800]
0027532C  E8 2F 83 28 00                  call 0x1404fd660
00275331  CC                              int3
00275332  48 8B 43 20                     mov rax, qword ptr [rbx + 0x20]
00275336  4C 89 7B 20                     mov qword ptr [rbx + 0x20], r15
0027533A  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
0027533E  44 89 7B 48                     mov dword ptr [rbx + 0x48], r15d
00275342  E9 37 F5 FF FF                  jmp 0x14027487e
00275347  BA 70 00 00 00                  mov edx, 0x70
0027534C  41 B8 42 6F 6F 73               mov r8d, 0x736f6f42
00275352  41 0F B6 F5                     movzx esi, r13b
00275356  8D 4A D0                        lea ecx, [rdx - 0x30]
00275359  E8 92 CD 90 00                  call 0x140b820f0
0027535E  4C 8B F8                        mov r15, rax
00275361  48 85 C0                        test rax, rax
00275364  74 26                           je 0x14027538c
00275366  45 33 C9                        xor r9d, r9d
00275369  4C 8D 40 10                     lea r8, [rax + 0x10]
0027536D  41 8B CD                        mov ecx, r13d
00275370  41 8D 51 0A                     lea edx, [r9 + 0xa]
00275374  E8 77 4C 08 00                  call 0x1402f9ff0
00275379  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00275382  33 C0                           xor eax, eax
00275384  49 89 4F 60                     mov qword ptr [r15 + 0x60], rcx
00275388  49 89 47 68                     mov qword ptr [r15 + 0x68], rax
0027538C  48 8D 8F 10 06 00 00            lea rcx, [rdi + 0x610]
00275393  E8 D8 30 F9 FF                  call 0x140208470
00275398  44 0F B6 F0                     movzx r14d, al
0027539C  E9 59 EC FF FF                  jmp 0x140273ffa
002753A1  C6 40 11 05                     mov byte ptr [rax + 0x11], 5
002753A5  4C 8B C0                        mov r8, rax
002753A8  41 C7 41 04 00 00 00 00         mov dword ptr [r9 + 4], 0
002753B0  49 8B D1                        mov rdx, r9
002753B3  48 8B 48 18                     mov rcx, qword ptr [rax + 0x18]
002753B7  E8 94 28 F9 FF                  call 0x140207c50
002753BC  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
002753C1  4D 8D 4D 18                     lea r9, [r13 + 0x18]
002753C5  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
002753CA  E9 B1 F2 FF FF                  jmp 0x140274680
002753CF  BA 70 00 00 00                  mov edx, 0x70
002753D4  41 B8 42 6F 6F 73               mov r8d, 0x736f6f42
002753DA  41 B6 01                        mov r14b, 1
002753DD  8D 4A D0                        lea ecx, [rdx - 0x30]
002753E0  E8 0B CD 90 00                  call 0x140b820f0
002753E5  4C 8B E0                        mov r12, rax
002753E8  48 85 C0                        test rax, rax
002753EB  74 28                           je 0x140275415
002753ED  45 33 C9                        xor r9d, r9d
002753F0  4C 8D 40 10                     lea r8, [rax + 0x10]
002753F4  41 8D 51 0A                     lea edx, [r9 + 0xa]
002753F8  8D 4A F7                        lea ecx, [rdx - 9]
002753FB  E8 F0 4B 08 00                  call 0x1402f9ff0
00275400  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00275409  33 C0                           xor eax, eax
0027540B  49 89 4C 24 60                  mov qword ptr [r12 + 0x60], rcx
00275410  49 89 44 24 68                  mov qword ptr [r12 + 0x68], rax
00275415  48 8D 8E 10 06 00 00            lea rcx, [rsi + 0x610]
0027541C  E8 4F 30 F9 FF                  call 0x140208470
00275421  44 0F B6 F8                     movzx r15d, al
00275425  E9 AA F3 FF FF                  jmp 0x1402747d4
0027542A  33 C9                           xor ecx, ecx
0027542C  C6 40 11 05                     mov byte ptr [rax + 0x11], 5
00275430  41 89 49 04                     mov dword ptr [r9 + 4], ecx
00275434  4C 8B C0                        mov r8, rax
00275437  48 8B 48 18                     mov rcx, qword ptr [rax + 0x18]
0027543B  49 8B D1                        mov rdx, r9
0027543E  E8 0D 28 F9 FF                  call 0x140207c50
00275443  E9 F5 F9 FF FF                  jmp 0x140274e3d
00275448  48 8D 4F D0                     lea rcx, [rdi - 0x30]
0027544C  E8 43 CF 12 00                  call 0x1403a2394
00275451  E9 15 EC FF FF                  jmp 0x14027406b
00275456  48 8D 4E D0                     lea rcx, [rsi - 0x30]
0027545A  E8 35 CF 12 00                  call 0x1403a2394
0027545F  E9 EB F3 FF FF                  jmp 0x14027484f
00275464  40 84 F6                        test sil, sil
00275467  0F 84 AA EB FF FF               je 0x140274017
0027546D  44 84 2D 92 16 D5 00            test byte ptr [rip + 0xd51692], r13b
00275474  48 8D 8F 10 06 00 00            lea rcx, [rdi + 0x610]
0027547B  75 28                           jne 0x1402754a5
0027547D  F0 48 83 21 00                  lock and qword ptr [rcx], 0
00275482  83 3D 97 18 D5 00 00            cmp dword ptr [rip + 0xd51897], 0
00275489  74 0D                           je 0x140275498
0027548B  44 0F 20 C1                     mov rcx, cr8
0027548F  41 0F B6 D6                     movzx edx, r14b
00275493  E8 00 02 28 00                  call 0x1404f5698
00275498  41 0F B6 C6                     movzx eax, r14b
0027549C  44 0F 22 C0                     mov cr8, rax
002754A0  E9 72 EB FF FF                  jmp 0x140274017
002754A5  8B 05 AD 89 C9 00               mov eax, dword ptr [rip + 0xc989ad]
002754AB  85 C0                           test eax, eax
002754AD  75 CE                           jne 0x14027547d
002754AF  48 8B 55 48                     mov rdx, qword ptr [rbp + 0x48]
002754B3  E8 38 DA 11 00                  call 0x140392ef0
002754B8  EB C8                           jmp 0x140275482
002754BA  45 84 F6                        test r14b, r14b
002754BD  0F 84 2E F3 FF FF               je 0x1402747f1
002754C3  F6 05 3C 16 D5 00 01            test byte ptr [rip + 0xd5163c], 1
002754CA  48 8D 8E 10 06 00 00            lea rcx, [rsi + 0x610]
002754D1  75 28                           jne 0x1402754fb
002754D3  F0 48 83 21 00                  lock and qword ptr [rcx], 0
002754D8  83 3D 41 18 D5 00 00            cmp dword ptr [rip + 0xd51841], 0
002754DF  74 0D                           je 0x1402754ee
002754E1  44 0F 20 C1                     mov rcx, cr8
002754E5  41 0F B6 D7                     movzx edx, r15b
002754E9  E8 AA 01 28 00                  call 0x1404f5698
002754EE  41 0F B6 C7                     movzx eax, r15b
002754F2  44 0F 22 C0                     mov cr8, rax
002754F6  E9 F6 F2 FF FF                  jmp 0x1402747f1
002754FB  8B 05 57 89 C9 00               mov eax, dword ptr [rip + 0xc98957]
00275501  85 C0                           test eax, eax
00275503  75 CE                           jne 0x1402754d3
00275505  48 8B 55 48                     mov rdx, qword ptr [rbp + 0x48]
00275509  E8 E2 D9 11 00                  call 0x140392ef0
0027550E  EB C8                           jmp 0x1402754d8
00275510  83 BF E0 05 00 00 00            cmp dword ptr [rdi + 0x5e0], 0
00275517  74 30                           je 0x140275549
00275519  4D 85 FF                        test r15, r15
0027551C  0F 84 4B FF FF FF               je 0x14027546d
00275522  48 8D 87 00 06 00 00            lea rax, [rdi + 0x600]
00275529  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
0027552D  48 39 01                        cmp qword ptr [rcx], rax
00275530  0F 85 EA F0 FF FF               jne 0x140274620
00275536  49 89 07                        mov qword ptr [r15], rax
00275539  49 89 4F 08                     mov qword ptr [r15 + 8], rcx
0027553D  4C 89 39                        mov qword ptr [rcx], r15
00275540  4C 89 78 08                     mov qword ptr [rax + 8], r15
00275544  E9 24 FF FF FF                  jmp 0x14027546d
00275549  4D 85 FF                        test r15, r15
0027554C  74 0D                           je 0x14027555b
0027554E  BA 42 6F 6F 73                  mov edx, 0x736f6f42
00275553  49 8B CF                        mov rcx, r15
00275556  E8 15 D3 90 00                  call 0x140b82870
0027555B  48 8D B7 F0 05 00 00            lea rsi, [rdi + 0x5f0]
00275562  48 8B 0E                        mov rcx, qword ptr [rsi]
00275565  48 3B CE                        cmp rcx, rsi
00275568  75 3D                           jne 0x1402755a7
0027556A  48 8D B7 00 06 00 00            lea rsi, [rdi + 0x600]
00275571  48 8B 0E                        mov rcx, qword ptr [rsi]
00275574  48 3B CE                        cmp rcx, rsi
00275577  0F 84 F0 FE FF FF               je 0x14027546d
0027557D  48 8B 01                        mov rax, qword ptr [rcx]
00275580  48 39 71 08                     cmp qword ptr [rcx + 8], rsi
00275584  0F 85 96 F0 FF FF               jne 0x140274620
0027558A  48 39 48 08                     cmp qword ptr [rax + 8], rcx
0027558E  0F 85 8C F0 FF FF               jne 0x140274620
00275594  48 89 06                        mov qword ptr [rsi], rax
00275597  BA 42 6F 6F 73                  mov edx, 0x736f6f42
0027559C  48 89 70 08                     mov qword ptr [rax + 8], rsi
002755A0  E8 CB D2 90 00                  call 0x140b82870
002755A5  EB CA                           jmp 0x140275571
002755A7  48 8B 01                        mov rax, qword ptr [rcx]
002755AA  48 39 71 08                     cmp qword ptr [rcx + 8], rsi
002755AE  0F 85 6C F0 FF FF               jne 0x140274620
002755B4  48 39 48 08                     cmp qword ptr [rax + 8], rcx
002755B8  0F 85 62 F0 FF FF               jne 0x140274620
002755BE  48 89 06                        mov qword ptr [rsi], rax
002755C1  BA 42 6F 6F 73                  mov edx, 0x736f6f42
002755C6  48 89 70 08                     mov qword ptr [rax + 8], rsi
002755CA  E8 A1 D2 90 00                  call 0x140b82870
002755CF  EB 91                           jmp 0x140275562
002755D1  83 BE E0 05 00 00 00            cmp dword ptr [rsi + 0x5e0], 0
002755D8  74 32                           je 0x14027560c
002755DA  4D 85 E4                        test r12, r12
002755DD  0F 84 E0 FE FF FF               je 0x1402754c3
002755E3  48 8D 86 00 06 00 00            lea rax, [rsi + 0x600]
002755EA  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
002755EE  48 39 01                        cmp qword ptr [rcx], rax
002755F1  0F 85 29 F0 FF FF               jne 0x140274620
002755F7  49 89 04 24                     mov qword ptr [r12], rax
002755FB  49 89 4C 24 08                  mov qword ptr [r12 + 8], rcx
00275600  4C 89 21                        mov qword ptr [rcx], r12
00275603  4C 89 60 08                     mov qword ptr [rax + 8], r12
00275607  E9 B7 FE FF FF                  jmp 0x1402754c3
0027560C  4D 85 E4                        test r12, r12
0027560F  74 0D                           je 0x14027561e
00275611  BA 42 6F 6F 73                  mov edx, 0x736f6f42
00275616  49 8B CC                        mov rcx, r12
00275619  E8 52 D2 90 00                  call 0x140b82870
0027561E  4C 8D B6 F0 05 00 00            lea r14, [rsi + 0x5f0]
00275625  49 8B 0E                        mov rcx, qword ptr [r14]
00275628  49 3B CE                        cmp rcx, r14
0027562B  75 3D                           jne 0x14027566a
0027562D  4C 8D B6 00 06 00 00            lea r14, [rsi + 0x600]
00275634  49 8B 0E                        mov rcx, qword ptr [r14]
00275637  49 3B CE                        cmp rcx, r14
0027563A  0F 84 83 FE FF FF               je 0x1402754c3
00275640  48 8B 01                        mov rax, qword ptr [rcx]
00275643  4C 39 71 08                     cmp qword ptr [rcx + 8], r14
00275647  0F 85 D3 EF FF FF               jne 0x140274620
0027564D  48 39 48 08                     cmp qword ptr [rax + 8], rcx
00275651  0F 85 C9 EF FF FF               jne 0x140274620
00275657  49 89 06                        mov qword ptr [r14], rax
0027565A  BA 42 6F 6F 73                  mov edx, 0x736f6f42
0027565F  4C 89 70 08                     mov qword ptr [rax + 8], r14
00275663  E8 08 D2 90 00                  call 0x140b82870
00275668  EB CA                           jmp 0x140275634
0027566A  48 8B 01                        mov rax, qword ptr [rcx]
0027566D  4C 39 71 08                     cmp qword ptr [rcx + 8], r14
00275671  0F 85 A9 EF FF FF               jne 0x140274620
00275677  48 39 48 08                     cmp qword ptr [rax + 8], rcx
0027567B  0F 85 9F EF FF FF               jne 0x140274620
00275681  49 89 06                        mov qword ptr [r14], rax
00275684  BA 42 6F 6F 73                  mov edx, 0x736f6f42
00275689  4C 89 70 08                     mov qword ptr [rax + 8], r14
0027568D  E8 DE D1 90 00                  call 0x140b82870
00275692  EB 91                           jmp 0x140275625
00275694  44 89 7F 24                     mov dword ptr [rdi + 0x24], r15d
00275698  E9 D4 ED FF FF                  jmp 0x140274471
0027569D  0F B7 4C 24 40                  movzx ecx, word ptr [rsp + 0x40]
002756A2  66 39 4F 18                     cmp word ptr [rdi + 0x18], cx
002756A6  0F 85 4A F0 FF FF               jne 0x1402746f6
002756AC  0F B6 4C 24 30                  movzx ecx, byte ptr [rsp + 0x30]
002756B1  38 4F 1A                        cmp byte ptr [rdi + 0x1a], cl
002756B4  0F 85 3C F0 FF FF               jne 0x1402746f6
002756BA  4C 8B 4C 24 78                  mov r9, qword ptr [rsp + 0x78]
002756BF  4C 2B C8                        sub r9, rax
002756C2  E9 32 F0 FF FF                  jmp 0x1402746f9
002756C7  33 D2                           xor edx, edx
002756C9  41 8B C2                        mov eax, r10d
002756CC  2B C1                           sub eax, ecx
002756CE  F7 35 44 94 B9 00               div dword ptr [rip + 0xb99444]
002756D4  85 D2                           test edx, edx
002756D6  0F 84 9B F9 FF FF               je 0x140275077
002756DC  E9 33 F0 FF FF                  jmp 0x140274714
002756E1  89 47 24                        mov dword ptr [rdi + 0x24], eax
002756E4  E9 C6 F4 FF FF                  jmp 0x140274baf
002756E9  0F B7 4C 24 40                  movzx ecx, word ptr [rsp + 0x40]
002756EE  66 39 4F 18                     cmp word ptr [rdi + 0x18], cx
002756F2  0F 85 D7 F4 FF FF               jne 0x140274bcf
002756F8  0F B6 4C 24 30                  movzx ecx, byte ptr [rsp + 0x30]
002756FD  38 4F 1A                        cmp byte ptr [rdi + 0x1a], cl
00275700  0F 85 C9 F4 FF FF               jne 0x140274bcf
00275706  4C 8B 4D 90                     mov r9, qword ptr [rbp - 0x70]
0027570A  4C 2B C8                        sub r9, rax
0027570D  E9 C0 F4 FF FF                  jmp 0x140274bd2
00275712  33 D2                           xor edx, edx
00275714  41 8B C2                        mov eax, r10d
00275717  2B C1                           sub eax, ecx
00275719  F7 35 F9 93 B9 00               div dword ptr [rip + 0xb993f9]
0027571F  85 D2                           test edx, edx
00275721  0F 84 45 FA FF FF               je 0x14027516c
00275727  E9 C1 F4 FF FF                  jmp 0x140274bed
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0027475D(__int64 a1, int a2, __int64 a3, __int64 a4, __int64 a5, unsigned __int8 a6, unsigned int a7, unsigned __int16 a8, unsigned __int8 a9, __int64 a10, unsigned __int8 a11, unsigned int a12, __int64 a13, __int64 a14, __int64 a15)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rdi;
    __int64 v_rsi;
    unsigned int v_stack_p0;
    unsigned __int8 v_stack_p20;
    unsigned __int8 v_stack_p30;
    unsigned int v_stack_p38;
    unsigned __int16 v_stack_p40;
    unsigned int v_stack_p44;
    unsigned __int64 v_stack_p48;
    unsigned int v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p78;

    result = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) - (*(unsigned int *)(v_rbx + 16)));
    result = (result) >> (4);
    *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1120) = (unsigned __int8)(result);
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rdi + 8))) & (7));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 8))))) >> (3));
    result = (unsigned int)((result * 8 - 8) | ((unsigned int)(a1)));
    *(unsigned int *)(v_rdi + 8) = (unsigned int)(result);
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)(result))) >> (3));
    v_stack_p38 = (unsigned int)(v_rsi);
    if ((unsigned int)(v_rsi) != 0) goto loc_002749D8;
    if ((((unsigned __int8)(result)) & (2)) == 0) goto loc_00274CCA;
    v_rsi = (*(unsigned __int64 *)(v_rdi)) & (-4);
loc_002747B2:
    if (v_rsi == 0) goto loc_00274853;
    if (((1) & ((unsigned __int8)(result))) == 0) goto loc_00274803;
    result = 0;
    v_r14 = 0;
    if ((*(unsigned int *)(v_rip + 13969341)) != 0) goto loc_002753CF;
loc_002747D4:
    if ((*(unsigned int *)(v_rsi + 1504)) == 0) goto loc_002754BA;
    if (0 != 0) goto loc_002755D1;
loc_002747F1:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rdi + 8))) & (0xFFFFFFFEULL));
    *(unsigned int *)(v_rdi + 8) = (unsigned int)(result);
    v_r15 = 0;
loc_00274803:
    if ((((unsigned __int8)(result)) & (4)) != 0) {
        result = *(unsigned int *)(v_rdi + 8);
        result = (unsigned int)((result) & (0xFFFFFFFBULL));
        *(unsigned int *)(v_rdi + 8) = (unsigned int)(result);
    }
    if ((((unsigned __int8)(result)) & (2)) == 0) goto loc_00274853;
    if ((*(unsigned int *)(v_rip + 13961198)) != 0) {
        a4 = 0x746C6644ULL;
        a1 = v_rsi - 48;
        a3 = 1;
        a2 = 0;
        result = ObpPushStackInfo(a1, a2, a3, a4);
    }
    result = (-1) - (1);
    if (condition_is_less_or_equal) goto loc_00275229;
loc_0027484F:
loc_00274853:
    *(unsigned __int64 *)(v_rdi) = 0;
    v_stack_p44 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 68)));
    if ((*(unsigned int *)(v_rbx + 64)) > 1) goto loc_0027487B;
    if ((*(unsigned int *)(v_rbx + 76)) != 0) goto loc_00274FFB;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 72))) != 0) goto loc_00275332;
loc_0027487B:
loc_0027487E:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbx + 64))) - 1);
    a1 = (unsigned int)((0) + ((unsigned int)(result)));
    *(unsigned int *)(v_rbx + 64) = (unsigned int)(a1);
    if (!(condition_is_not_equal)) {
        *(unsigned __int16 *)(v_rbx + 24) = 0;
    }
    if ((*(unsigned int *)(v_rbx + 76)) != 0) goto loc_002748A4;
    if ((*(unsigned int *)(v_rbx + 72)) == 0) {
        a1 = 249;
    }
    if (0 != 0) {
        result = *(unsigned int *)(v_rbx + 56);
        result = (unsigned int)((result) & (7));
        *(unsigned __int64 *)(v_rbx + 48) = 0;
        result = (unsigned int)((result) | (8));
        *(unsigned int *)(v_rbx + 56) = (unsigned int)(result);
    }
    if (((*(unsigned __int8 *)(v_rip + 13967937)) & (1)) != 0) goto loc_0027496E;
loc_002748CB:
    if (a9 != 0) goto loc_00274904;
    a4 = 0;
    if (a9 == a9) goto loc_0027498A;
    result = KxWaitForLockChainValid(a9, a2, a3, a4);
loc_00274904:
    a4 = 0;
    v_stack_p48 = 0;
    result = (unsigned __int8)((a10) ^ ((unsigned __int8)(a10)));
    if ((((unsigned __int8)(result)) & (4)) == 0) goto loc_0027498A;
    a3 = (result + 8) >> (5);
    a3 = (unsigned int)((a3) & (127));
    result = KeDisableInterrupts(a10, a2, a3, a4);
    result = KiHaltOnAddressWakeEntireList(a10, 0, a3, a4);
    if ((unsigned __int8)((unsigned __int8)(result)) == 0) goto loc_0027498A;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536) != 0) goto loc_0027502C;
loc_0027496B:
    goto loc_0027498A;
loc_0027496E:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13210852))) != 0) goto loc_002748CB;
    result = KiReleaseQueuedSpinLockInstrumented(a9, *(unsigned __int64 *)(v_rbp + 72), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), a4);
loc_0027498A:
    if ((*(unsigned int *)(v_rip + 13968271)) != 0) {
        a1 = v_cr8;
        a2 = a11;
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), a4);
    }
    v_rdi = 1;
    if (0 != 0) { v_rdi = 3; }
    if ((*(unsigned __int64 *)(v_rbp - 128)) != 0) goto loc_00274DDD;
loc_002749C7:
    result = 0;
    v_stack_p60 = (unsigned int)((unsigned int)(0x10042ULL));
    v_stack_p38 = 0;
    goto loc_00274A32;
loc_002749D8:
    v_stack_p60 = (unsigned int)((unsigned int)(0x10052ULL));
    v_stack_p44 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 68)));
    if (((*(unsigned __int8 *)(v_rip + 13967655)) & (1)) == 0) goto loc_00274C22;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13210715))) != 0) goto loc_00274C22;
    result = KiReleaseQueuedSpinLockInstrumented(a9, *(unsigned __int64 *)(v_rbp + 72), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), a4);
loc_00274A13:
    if ((*(unsigned int *)(v_rip + 13968134)) != ((unsigned int)(*(unsigned __int8 *)(v_rbx + 27)))) {
        a1 = a11;
        a2 = a11;
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), a4);
    }
loc_00274A32:
    *(unsigned __int64 *)(v_rbp - 56) = v_xmm0;
    *(unsigned __int64 *)(v_rbp - 40) = v_xmm0;
    *(unsigned __int64 *)(v_rbp - 24) = v_xmm0;
    a2 = (a2) << (32);
    result = (result) | (a2);
    *(unsigned __int64 *)(v_rbp - 112) = result;
    v_stack_p40 = (unsigned __int16)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 208));
    v_stack_p30 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 209));
    v_r12 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(0x10052ULL)))) & (0xFFFF0000ULL));
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1568) != 0) goto loc_00274B20;
    result = ExAllocatePool2(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1568) + 72, 512, (unsigned int)(0x72546552ULL), a4);
    *(unsigned __int64 *)(result + 16) = v_rbx;
    *(unsigned int *)(result + 28) = (unsigned int)(v_r12);
    result = 0;
    *(unsigned int *)(result + 32) = 0;
    *(unsigned int *)(result + 40) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12532121)));
    if (condition_is_equal) goto loc_00274CD9;
    a2 = 0;
    result = ExFreePoolWithTag(0, a2, (unsigned int)(0x72546552ULL), a4);
loc_00274B20:
    v_r15 = 0;
loc_00274B29:
    if (0 >= 8) goto loc_00274B60;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(0 + 28)))) != ((unsigned int)(v_r12))) goto loc_00274B42;
    if ((*(unsigned __int64 *)(0 + 16)) != v_rbx) goto loc_00274B42;
    if ((*(unsigned int *)(0 + 40)) == ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12532121))))) goto loc_00274B87;
loc_00274B42:
    if (0 != 0) goto loc_00274C17;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(0 + 28))) == 0) goto loc_00274C14;
    if ((*(unsigned int *)(0 + 40)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12532121))))) goto loc_00274C17;
loc_00274B60:
    if (0 != 0) {
        *(unsigned __int64 *)(0 + 16) = v_rbx;
        *(unsigned int *)(0 + 28) = (unsigned int)(v_r12);
        *(unsigned __int64 *)(0 + 32) = 0;
        *(unsigned __int64 *)(0) = 0;
        *(unsigned __int64 *)(0 + 8) = 0;
        *(unsigned int *)(0 + 24) = 0;
        *(unsigned int *)(0 + 40) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12532121)));
        *(unsigned int *)(0 + 44) = 0;
    }
loc_00274B93:
    if ((*(unsigned int *)(0 + 32)) == 0) goto loc_00274C0B;
    result = (unsigned int)(((unsigned int)(a7)) + 1);
    if ((*(unsigned int *)(0 + 36)) < ((unsigned int)(result))) goto loc_002756E1;
loc_00274BAF:
    if (((unsigned int)((unsigned int)(a12))) != 0x10042ULL) goto loc_00274F32;
    if ((*(unsigned __int64 *)(0 + 8)) > 2) goto loc_002756E9;
loc_00274BCF:
loc_00274BD2:
    if ((*(unsigned __int64 *)(0)) > 1) goto loc_00275149;
loc_00274BDC:
    if (((unsigned int)((unsigned int)(v_stack_p44))) > ((unsigned int)((unsigned int)(*(unsigned int *)(0 + 44))))) goto loc_00275712;
loc_00274BED:
    a2 = 0;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36592))) + (*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36588)));
    if (0 == 0) goto loc_0027516C;
loc_00274C0B:
    *(unsigned int *)(0 + 28) = 0;
loc_00274C14:
loc_00274C17:
    v_rsi = (0) + (64);
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(0 + 44))) + 1);
    goto loc_00274B29;
loc_00274C22:
    if (a9 != 0) goto loc_00274C58;
    if (a9 == a9) goto loc_00274A13;
    result = KxWaitForLockChainValid(a9, a2, (unsigned int)(a12), 0);
loc_00274C58:
    v_stack_p48 = 0;
    result = (unsigned __int8)((a10) ^ ((unsigned __int8)(a10)));
    if ((((unsigned __int8)(result)) & (4)) == 0) goto loc_00274A13;
    a3 = (result + 8) >> (5);
    a3 = (unsigned int)((a3) & (127));
    result = KeDisableInterrupts(a10, a2, a3, 0);
    result = KiHaltOnAddressWakeEntireList(a10, 0, a3, 0);
    if ((unsigned __int8)((unsigned __int8)(result)) == 0) goto loc_00274A13;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536) != 0) goto loc_00274F9D;
loc_00274CC4:
    goto loc_00274A13;
loc_00274CCA:
    if ((((unsigned __int8)(v_rsi)) & (3)) != 0) goto loc_00274853;
    goto loc_002747B2;
loc_00274CD9:
    v_r15 = 0;
    goto loc_00274B93;
loc_00274DDD:
    *(unsigned __int64 *)(v_rbp - 112) = a11;
    if ((*(unsigned int *)(v_rip + 13967147)) != 0) goto loc_002750E9;
loc_00274DFB:
    v_stack_p68 = *(unsigned __int64 *)(gs_base + (0 + 32));
loc_00274E11:
    v_stack_p78 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 128));
    *(unsigned __int64 *)(v_rbp - 120) = *(unsigned __int64 *)(v_rbp - 128);
    v_stack_p38 = *(unsigned __int64 *)(v_rbp - 128) + 24;
    result = KiAcquireKobjectLockSafe(*(unsigned __int64 *)(v_rbp - 128) + 24, 0, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), 0);
    v_r13 = (*(unsigned __int64 *)(v_rbp - 128) + 24) + (8);
    *(unsigned int *)(*(unsigned __int64 *)(v_rbp - 128) + 28) = 1;
loc_00274E3D:
loc_00274E42:
    if ((*(unsigned __int64 *)(v_r13)) == v_r13) goto loc_00274EA1;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r13) + 8)) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_r13));
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r13)) + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_r13) + 8);
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_r13) + 16))) != 1) goto loc_002750F9;
    a4 = 0;
    result = KiTryUnwaitThread(a13, *(unsigned __int64 *)(v_r13), *(unsigned __int16 *)(*(unsigned __int64 *)(v_r13) + 18), a4);
    if ((unsigned __int8)(result) == 0) goto loc_00274E42;
loc_00274E9A:
    if ((unsigned __int8)(result) != 0) goto loc_00274E42;
loc_00274EA1:
    if (a15 != (*(unsigned __int64 *)(v_rbp - 128))) goto loc_0027512D;
    result = KiRemoveBoostThread(a13, *(unsigned __int64 *)(a13 + 8), *(unsigned __int16 *)(*(unsigned __int64 *)(v_r13) + 18), a7);
    if (0 != 0) goto loc_002751EF;
loc_00274ED6:
    if ((((unsigned __int8)((unsigned __int8)(result))) & (2)) != 0) goto loc_002751DE;
loc_00274EE0:
    v_stack_p20 = (unsigned __int8)(*(unsigned __int64 *)(v_rbp - 112));
    a2 = 0;
    result = KiExitDispatcher(a13, a2, (unsigned int)((unsigned int)(v_rsi)), 0);
    goto loc_002749C7;
loc_00274F32:
    *(unsigned int *)((unsigned __int8)(result) + 32) = 2;
loc_00274F9D:
loc_00274FA4:
    if (((unsigned int)((unsigned int)((unsigned int)(v_rsi)))) != 0x10052ULL) goto loc_00274FA4;
    if (((unsigned int)((unsigned int)((unsigned int)(v_rsi)))) >= 0x10052ULL) goto loc_00274CC4;
    result = KiRemoveSystemWorkPriorityKick(a13, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)(v_rsi)))))), (unsigned int)((unsigned int)(v_rsi)), 0);
    goto loc_00274CC4;
loc_00274FFB:
    result = RtlRemoveHeadCircularList(v_rbx + 40, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)(v_rsi)))))), (unsigned int)((unsigned int)(v_rsi)), 0);
    if (result != 0) {
        v_rsi = *(unsigned __int64 *)(result + 16);
        *(unsigned __int64 *)(result + 8) = result;
        *(unsigned __int64 *)(result) = result;
        *(unsigned __int64 *)(v_rbp - 128) = result;
    }
    goto loc_0027487E;
loc_0027502C:
loc_00275033:
    if (result != 0) goto loc_00275033;
    if (condition_is_above_or_equal) goto loc_0027496B;
    result = KiRemoveSystemWorkPriorityKick((unsigned int)((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r13)))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)(v_rsi)))))), (unsigned int)((unsigned int)(v_rsi)), 0);
    goto loc_0027496B;
loc_002750E9:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(result), (unsigned __int8)((unsigned int)((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r13))))), (unsigned int)((unsigned int)(v_rsi)), 0);
    goto loc_00274DFB;
loc_002750F9:
    if (((unsigned __int8)((unsigned __int8)(result))) != 2) goto loc_002752CB;
    *(unsigned __int8 *)(result + 17) = 5;
    result = KiInsertQueueInternal(*(unsigned __int64 *)(result + 24), result, (unsigned int)((unsigned int)(v_rsi)), 0);
    goto loc_00274E9A;
loc_0027512D:
    goto loc_00274E11;
loc_00275149:
    a2 = 0;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a13 + 36592))) + (*(unsigned int *)(a13 + 36588)));
    if (0 != 0) goto loc_00274BDC;
loc_0027516C:
    *(unsigned int *)(v_rbp - 16) = (unsigned int)((unsigned int)((unsigned int)(v_rsi)));
    *(unsigned __int64 *)(v_rbp - 24) = v_rbx;
    *(unsigned __int64 *)(v_rbp - 56) = *(unsigned __int64 *)((unsigned __int8)(result) + 8);
    *(unsigned int *)(v_rbp - 32) = (unsigned int)((unsigned int)(*(unsigned int *)((unsigned __int8)(result) + 36)));
    *(unsigned __int64 *)(v_rbp - 48) = a7;
    *(unsigned __int64 *)(v_rbp - 40) = *(unsigned __int64 *)((unsigned __int8)(result));
    v_r10 = (unsigned int)(((unsigned int)(v_stack_p44)) - (*(unsigned int *)((unsigned __int8)(result) + 44)));
    *(unsigned int *)(v_rbp - 12) = (unsigned int)(v_r10);
    *(unsigned __int64 *)(v_rbp) = 48;
    v_stack_p20 = 0x1601802ULL;
    *(unsigned int *)(v_rbp - 28) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1296)));
    *(unsigned __int64 *)(v_rbp - 8) = v_rbp - 56;
    result = EtwTraceKernelEvent(v_rbp - 8, 1, (unsigned int)(0x20020000ULL), (unsigned int)(0x52BULL));
    goto loc_00274C0B;
loc_002751DE:
    if (((unsigned int)(v_rsi)) == 1) { v_r15 = 1; }
    goto loc_00274EE0;
loc_002751EF:
    if (1 > ((unsigned int)(v_r15))) { v_r15 = 1; }
    goto loc_00274ED6;
loc_00275229:
    if (*(unsigned __int64 *)(2 - 40) != 0) goto loc_002752EF;
    if (!sign_flag) goto loc_00275456;
    a2 = 0;
    v_stack_p20 = 1;
    result = KeBugCheckEx(a2 + 24, a2, 2, *(unsigned __int64 *)(2 - 40) + 4);
loc_00275256:
    if (((unsigned __int8)(a2 + 24)) == 4) goto loc_002753A1;
    a4 = 0;
    result = KiTryUnwaitThread(a13, result, 256, a4);
loc_002752CB:
    if (((unsigned __int8)(a7)) == 4) goto loc_0027542A;
    a4 = 0;
    result = KiTryUnwaitThread(a13, a12, 256, a4);
    goto loc_00274E3D;
loc_002752EF:
    v_stack_p20 = a13;
    result = (2 - 48) >> (8);
    a2 = ((unsigned __int8)(result)) ^ (*(unsigned __int8 *)(2 - 24));
    a2 = (a2) ^ (*(unsigned __int8 *)(v_rip + 13966123));
    result = KeBugCheckEx(3 + 21, *(unsigned __int64 *)(v_rip - 2577153 + a2 * 8 + 16545792), 2, 3);
loc_00275332:
    *(unsigned __int64 *)(v_rbx + 32) = v_r15;
    *(unsigned __int64 *)(v_rbp - 128) = *(unsigned __int64 *)(v_rbx + 32);
    *(unsigned int *)(v_rbx + 72) = (unsigned int)(v_r15);
    goto loc_0027487E;
loc_002753A1:
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_rbx + 32) + 17) = 5;
    *(unsigned int *)(3 + 4) = 0;
    result = KeInsertQueueDpc(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 32) + 24), 3, *(unsigned __int64 *)(v_rbx + 32), 3);
loc_002753CF:
    result = ExAllocatePool2(112 - 48, 112, (unsigned int)(0x736F6F42ULL), (unsigned int)(a12) + 24);
    if (result != 0) {
        a4 = 0;
        a3 = result + 16;
        a2 = a4 + 10;
        a1 = a2 - 9;
        result = RtlCaptureStackBackTrace(a1, a2, a3, a4);
        a1 = *(unsigned __int64 *)(gs_base + (0 + 392));
        result = 0;
        *(unsigned __int64 *)(result + 96) = a1;
        *(unsigned __int64 *)(result + 104) = 0;
    }
    result = KeAcquireSpinLockRaiseToDpc(2 + 1552, a2, a3, a4);
    goto loc_002747D4;
loc_0027542A:
    a1 = 0;
    *(unsigned __int8 *)(result + 17) = 5;
    *(unsigned int *)(a4 + 4) = 0;
    result = KeInsertQueueDpc(*(unsigned __int64 *)(result + 24), 0, result, a4);
    goto loc_00274E3D;
loc_00275456:
    result = ObpDeferObjectDeletion(2 - 48, 0, result, a4);
    goto loc_0027484F;
loc_002754BA:
    if (1 == 0) goto loc_002747F1;
loc_002754C3:
    if (((*(unsigned __int8 *)(v_rip + 13964860)) & (1)) != 0) goto loc_002754FB;
loc_002754D3:
loc_002754D8:
    if ((*(unsigned int *)(v_rip + 13965377)) != 0) {
        a1 = 2;
        a2 = (unsigned __int8)((unsigned __int8)(result));
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, result, a4);
    }
    goto loc_002747F1;
loc_002754FB:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13207895))) != 0) goto loc_002754D3;
    result = KiReleaseSpinLockInstrumented(a1, *(unsigned __int64 *)(v_rbp + 72), result, a4);
    goto loc_002754D8;
loc_002755D1:
    if ((*(unsigned int *)(2 + 1504)) == 0) goto loc_0027560C;
    if (result == 0) goto loc_002754C3;
    *(unsigned __int64 *)(result) = 2 + 1536;
    *(unsigned __int64 *)(result + 8) = *(unsigned __int64 *)(2 + 1536 + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(2 + 1536 + 8)) = result;
    *(unsigned __int64 *)(2 + 1536 + 8) = result;
    goto loc_002754C3;
loc_0027560C:
    result = 2 + 1536;
    if (result != 0) {
        a2 = 0x736F6F42ULL;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, result, a4);
    }
loc_00275625:
    if ((*(unsigned __int64 *)(2 + 1520)) != (2 + 1520)) goto loc_0027566A;
loc_00275634:
    if ((*(unsigned __int64 *)(2 + 1536)) == (2 + 1536)) goto loc_002754C3;
    *(unsigned __int64 *)(2 + 1536) = *(unsigned __int64 *)(*(unsigned __int64 *)(2 + 1536));
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(2 + 1536)) + 8) = 2 + 1536;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(2 + 1536), (unsigned int)(0x736F6F42ULL), result, a4);
    goto loc_00275634;
loc_0027566A:
    *(unsigned __int64 *)(2 + 1536) = *(unsigned __int64 *)(*(unsigned __int64 *)(2 + 1536));
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(2 + 1536)) + 8) = 2 + 1536;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(2 + 1536), (unsigned int)(0x736F6F42ULL), result, a4);
    goto loc_00275625;
loc_002756E1:
    *(unsigned int *)((unsigned __int8)(result) + 36) = (unsigned int)(result);
    goto loc_00274BAF;
loc_002756E9:
    if ((*(unsigned __int16 *)((unsigned __int8)(result) + 24)) != a8) goto loc_00274BCF;
    if ((*(unsigned __int8 *)((unsigned __int8)(result) + 26)) != a6) goto loc_00274BCF;
    a4 = (*(unsigned __int64 *)(v_rbp - 112)) - (result);
    goto loc_00274BD2;
loc_00275712:
    a2 = 0;
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rip - 2577153))) - (a6));
    if (0 == 0) goto loc_0027516C;
    goto loc_00274BED;
}
```

## 5. (Beta) C Style

```c
int64_t sub_0027475D(int64_t Arg1, int32_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint8_t Arg6, void *Arg7, uint16_t Arg8, uint8_t Arg9, void *Arg10, uint8_t Arg11, uint32_t Arg12, void *Arg13, uint64_t Arg14, int64_t Arg15)
{
    uint8_t *arg7 = (uint8_t *)Arg7;
    uint8_t *arg10 = (uint8_t *)Arg10;
    uint8_t *arg13 = (uint8_t *)Arg13;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rdi;
    int64_t local_rsi;
    uint32_t v_stack_p0;
    uint8_t v_stack_p20;
    uint8_t v_stack_p30;
    uint32_t v_stack_p38;
    uint16_t v_stack_p40;
    uint32_t v_stack_p44;
    uint64_t v_stack_p48;
    uint32_t v_stack_p60;
    uint64_t v_stack_p68;
    uint64_t v_stack_p70;
    uint64_t v_stack_p78;

    result = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) - (*(uint32_t *)(local_rbx + 0x10)));
    result = (result) >> (4);
    *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x460) = (uint8_t)(result);
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rdi + 0x8))) & (7));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x8))))) >> (3));
    result = (uint32_t)((result * 8 - 8) | ((uint32_t)(Arg1)));
    *(uint32_t *)(local_rdi + 0x8) = (uint32_t)(result);
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)(result))) >> (3));
    v_stack_p38 = (uint32_t)(local_rsi);
    if ((uint32_t)(local_rsi) != 0) goto loc_002749D8;
    if ((((uint8_t)(result)) & (2)) == 0) goto loc_00274CCA;
    local_rsi = (*(uint64_t *)(local_rdi)) & (-4);
loc_002747B2:
    if (local_rsi == 0) goto loc_00274853;
    if (((1) & ((uint8_t)(result))) == 0) goto loc_00274803;
    result = 0;
    local_r14 = 0;
    if ((*(uint32_t *)(v_rip + 0xD527BD)) != 0) goto loc_002753CF;
loc_002747D4:
    if ((*(uint32_t *)(local_rsi + 0x5E0)) == 0) goto loc_002754BA;
    if (0 != 0) goto loc_002755D1;
loc_002747F1:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rdi + 0x8))) & (0xFFFFFFFEULL));
    *(uint32_t *)(local_rdi + 0x8) = (uint32_t)(result);
    local_r15 = 0;
loc_00274803:
    if ((((uint8_t)(result)) & (4)) != 0) {
        result = *(uint32_t *)(local_rdi + 0x8);
        result = (uint32_t)((result) & (0xFFFFFFFBULL));
        *(uint32_t *)(local_rdi + 0x8) = (uint32_t)(result);
    }
    if ((((uint8_t)(result)) & (2)) == 0) goto loc_00274853;
    if ((*(uint32_t *)(v_rip + 0xD507EE)) != 0) {
        Arg4 = 0x746C6644ULL;
        Arg1 = local_rsi - 48;
        Arg3 = 1;
        Arg2 = 0;
        result = ObpPushStackInfo(Arg1, Arg2, Arg3, Arg4);
    }
    result = (-1) - (1);
    if (condition_is_less_or_equal) goto loc_00275229;
loc_0027484F:
loc_00274853:
    *(uint64_t *)(local_rdi) = 0;
    v_stack_p44 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x44)));
    if ((*(uint32_t *)(local_rbx + 0x40)) > 1) goto loc_0027487B;
    if ((*(uint32_t *)(local_rbx + 0x4C)) != 0) goto loc_00274FFB;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x48))) != 0) goto loc_00275332;
loc_0027487B:
loc_0027487E:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbx + 0x40))) - 1);
    Arg1 = (uint32_t)((0) + ((uint32_t)(result)));
    *(uint32_t *)(local_rbx + 0x40) = (uint32_t)(Arg1);
    if (!(condition_is_not_equal)) {
        *(uint16_t *)(local_rbx + 0x18) = 0;
    }
    if ((*(uint32_t *)(local_rbx + 0x4C)) != 0) goto loc_002748A4;
    if ((*(uint32_t *)(local_rbx + 0x48)) == 0) {
        Arg1 = 249;
    }
    if (0 != 0) {
        result = *(uint32_t *)(local_rbx + 0x38);
        result = (uint32_t)((result) & (7));
        *(uint64_t *)(local_rbx + 0x30) = 0;
        result = (uint32_t)((result) | (8));
        *(uint32_t *)(local_rbx + 0x38) = (uint32_t)(result);
    }
    if (((*(uint8_t *)(v_rip + 0xD52241)) & (1)) != 0) goto loc_0027496E;
loc_002748CB:
    if (Arg9 != 0) goto loc_00274904;
    Arg4 = 0;
    if (Arg9 == Arg9) goto loc_0027498A;
    result = KxWaitForLockChainValid(Arg9, Arg2, Arg3, Arg4);
loc_00274904:
    Arg4 = 0;
    v_stack_p48 = 0;
    result = (uint8_t)((Arg10) ^ ((uint8_t)(Arg10)));
    if ((((uint8_t)(result)) & (4)) == 0) goto loc_0027498A;
    Arg3 = (result + 8) >> (5);
    Arg3 = (uint32_t)((Arg3) & (127));
    result = KeDisableInterrupts(Arg10, Arg2, Arg3, Arg4);
    result = KiHaltOnAddressWakeEntireList(Arg10, 0, Arg3, Arg4);
    if ((uint8_t)((uint8_t)(result)) == 0) goto loc_0027498A;
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8) != 0) goto loc_0027502C;
loc_0027496B:
    goto loc_0027498A;
loc_0027496E:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC994E4))) != 0) goto loc_002748CB;
    result = KiReleaseQueuedSpinLockInstrumented(Arg9, *(uint64_t *)(local_rbp + 0x48), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), Arg4);
loc_0027498A:
    if ((*(uint32_t *)(v_rip + 0xD5238F)) != 0) {
        Arg1 = v_cr8;
        Arg2 = Arg11;
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), Arg4);
    }
    local_rdi = 1;
    if (0 != 0) { local_rdi = 3; }
    if ((*(uint64_t *)(local_rbp - 0x80)) != 0) goto loc_00274DDD;
loc_002749C7:
    result = 0;
    v_stack_p60 = (uint32_t)((uint32_t)(0x10042ULL));
    v_stack_p38 = 0;
    goto loc_00274A32;
loc_002749D8:
    v_stack_p60 = (uint32_t)((uint32_t)(0x10052ULL));
    v_stack_p44 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x44)));
    if (((*(uint8_t *)(v_rip + 0xD52127)) & (1)) == 0) goto loc_00274C22;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC9945B))) != 0) goto loc_00274C22;
    result = KiReleaseQueuedSpinLockInstrumented(Arg9, *(uint64_t *)(local_rbp + 0x48), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), Arg4);
loc_00274A13:
    if ((*(uint32_t *)(v_rip + 0xD52306)) != ((uint32_t)(*(uint8_t *)(local_rbx + 0x1B)))) {
        Arg1 = Arg11;
        Arg2 = Arg11;
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), Arg4);
    }
loc_00274A32:
    *(uint64_t *)(local_rbp - 0x38) = v_xmm0;
    *(uint64_t *)(local_rbp - 0x28) = v_xmm0;
    *(uint64_t *)(local_rbp - 0x18) = v_xmm0;
    Arg2 = (Arg2) << (32);
    result = (result) | (Arg2);
    *(uint64_t *)(local_rbp - 0x70) = result;
    v_stack_p40 = (uint16_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xD0));
    v_stack_p30 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xD1));
    local_r12 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(0x10052ULL)))) & (0xFFFF0000ULL));
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x620) != 0) goto loc_00274B20;
    result = ExAllocatePool2(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x620) + 72, 512, (uint32_t)(0x72546552ULL), Arg4);
    *(uint64_t *)(result + 0x10) = local_rbx;
    *(uint32_t *)(result + 0x1C) = (uint32_t)(local_r12);
    result = 0;
    *(uint32_t *)(result + 0x20) = 0;
    *(uint32_t *)(result + 0x28) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBF3999)));
    if (condition_is_equal) goto loc_00274CD9;
    Arg2 = 0;
    result = ExFreePoolWithTag(0, Arg2, (uint32_t)(0x72546552ULL), Arg4);
loc_00274B20:
    local_r15 = 0;
loc_00274B29:
    if (0 >= 8) goto loc_00274B60;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x1C)))) != ((uint32_t)(local_r12))) goto loc_00274B42;
    if ((*(uint64_t *)(0 + 0x10)) != local_rbx) goto loc_00274B42;
    if ((*(uint32_t *)(0 + 0x28)) == ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBF3999))))) goto loc_00274B87;
loc_00274B42:
    if (0 != 0) goto loc_00274C17;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x1C))) == 0) goto loc_00274C14;
    if ((*(uint32_t *)(0 + 0x28)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBF3999))))) goto loc_00274C17;
loc_00274B60:
    if (0 != 0) {
        *(uint64_t *)(0 + 0x10) = local_rbx;
        *(uint32_t *)(0 + 0x1C) = (uint32_t)(local_r12);
        *(uint64_t *)(0 + 0x20) = 0;
        *(uint64_t *)(0) = 0;
        *(uint64_t *)(0 + 0x8) = 0;
        *(uint32_t *)(0 + 0x18) = 0;
        *(uint32_t *)(0 + 0x28) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBF3999)));
        *(uint32_t *)(0 + 0x2C) = 0;
    }
loc_00274B93:
    if ((*(uint32_t *)(0 + 0x20)) == 0) goto loc_00274C0B;
    result = (uint32_t)(((uint32_t)(Arg7)) + 1);
    if ((*(uint32_t *)(0 + 0x24)) < ((uint32_t)(result))) goto loc_002756E1;
loc_00274BAF:
    if (((uint32_t)((uint32_t)(Arg12))) != 0x10042ULL) goto loc_00274F32;
    if ((*(uint64_t *)(0 + 0x8)) > 2) goto loc_002756E9;
loc_00274BCF:
loc_00274BD2:
    if ((*(uint64_t *)(0)) > 1) goto loc_00275149;
loc_00274BDC:
    if (((uint32_t)((uint32_t)(v_stack_p44))) > ((uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x2C))))) goto loc_00275712;
loc_00274BED:
    Arg2 = 0;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EF0))) + (*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EEC)));
    if (0 == 0) goto loc_0027516C;
loc_00274C0B:
    *(uint32_t *)(0 + 0x1C) = 0;
loc_00274C14:
loc_00274C17:
    local_rsi = (0) + (64);
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(0 + 0x2C))) + 1);
    goto loc_00274B29;
loc_00274C22:
    if (Arg9 != 0) goto loc_00274C58;
    if (Arg9 == Arg9) goto loc_00274A13;
    result = KxWaitForLockChainValid(Arg9, Arg2, (uint32_t)(Arg12), 0);
loc_00274C58:
    v_stack_p48 = 0;
    result = (uint8_t)((Arg10) ^ ((uint8_t)(Arg10)));
    if ((((uint8_t)(result)) & (4)) == 0) goto loc_00274A13;
    Arg3 = (result + 8) >> (5);
    Arg3 = (uint32_t)((Arg3) & (127));
    result = KeDisableInterrupts(Arg10, Arg2, Arg3, 0);
    result = KiHaltOnAddressWakeEntireList(Arg10, 0, Arg3, 0);
    if ((uint8_t)((uint8_t)(result)) == 0) goto loc_00274A13;
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8) != 0) goto loc_00274F9D;
loc_00274CC4:
    goto loc_00274A13;
loc_00274CCA:
    if ((((uint8_t)(local_rsi)) & (3)) != 0) goto loc_00274853;
    goto loc_002747B2;
loc_00274CD9:
    local_r15 = 0;
    goto loc_00274B93;
loc_00274DDD:
    *(uint64_t *)(local_rbp - 0x70) = Arg11;
    if ((*(uint32_t *)(v_rip + 0xD51F2B)) != 0) goto loc_002750E9;
loc_00274DFB:
    v_stack_p68 = *(uint64_t *)(gs_base + (0 + 0x20));
loc_00274E11:
    v_stack_p78 = *(uint64_t *)(*(uint64_t *)(local_rbp - 0x80));
    *(uint64_t *)(local_rbp - 0x78) = *(uint64_t *)(local_rbp - 0x80);
    v_stack_p38 = *(uint64_t *)(local_rbp - 0x80) + 24;
    result = KiAcquireKobjectLockSafe(*(uint64_t *)(local_rbp - 0x80) + 24, 0, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), 0);
    local_r13 = (*(uint64_t *)(local_rbp - 0x80) + 24) + (8);
    *(uint32_t *)(*(uint64_t *)(local_rbp - 0x80) + 0x1C) = 1;
loc_00274E3D:
loc_00274E42:
    if ((*(uint64_t *)(local_r13)) == local_r13) goto loc_00274EA1;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_r13) + 0x8)) = *(uint64_t *)(*(uint64_t *)(local_r13));
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_r13)) + 0x8) = *(uint64_t *)(*(uint64_t *)(local_r13) + 0x8);
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(local_r13) + 0x10))) != 1) goto loc_002750F9;
    Arg4 = 0;
    result = KiTryUnwaitThread(Arg13, *(uint64_t *)(local_r13), *(uint16_t *)(*(uint64_t *)(local_r13) + 0x12), Arg4);
    if ((uint8_t)(result) == 0) goto loc_00274E42;
loc_00274E9A:
    if ((uint8_t)(result) != 0) goto loc_00274E42;
loc_00274EA1:
    if (Arg15 != (*(uint64_t *)(local_rbp - 0x80))) goto loc_0027512D;
    result = KiRemoveBoostThread(Arg13, *(uint64_t *)(arg13 + 0x8), *(uint16_t *)(*(uint64_t *)(local_r13) + 0x12), Arg7);
    if (0 != 0) goto loc_002751EF;
loc_00274ED6:
    if ((((uint8_t)((uint8_t)(result))) & (2)) != 0) goto loc_002751DE;
loc_00274EE0:
    v_stack_p20 = (uint8_t)(*(uint64_t *)(local_rbp - 0x70));
    Arg2 = 0;
    result = KiExitDispatcher(Arg13, Arg2, (uint32_t)((uint32_t)(local_rsi)), 0);
    goto loc_002749C7;
loc_00274F32:
    *(uint32_t *)((uint8_t)(result) + 0x20) = 2;
loc_00274F9D:
loc_00274FA4:
    if (((uint32_t)((uint32_t)((uint32_t)(local_rsi)))) != 0x10052ULL) goto loc_00274FA4;
    if (((uint32_t)((uint32_t)((uint32_t)(local_rsi)))) >= 0x10052ULL) goto loc_00274CC4;
    result = KiRemoveSystemWorkPriorityKick(Arg13, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)(local_rsi)))))), (uint32_t)((uint32_t)(local_rsi)), 0);
    goto loc_00274CC4;
loc_00274FFB:
    result = RtlRemoveHeadCircularList(local_rbx + 40, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)(local_rsi)))))), (uint32_t)((uint32_t)(local_rsi)), 0);
    if (result != 0) {
        local_rsi = *(uint64_t *)(result + 0x10);
        *(uint64_t *)(result + 0x8) = result;
        *(uint64_t *)(result) = result;
        *(uint64_t *)(local_rbp - 0x80) = result;
    }
    goto loc_0027487E;
loc_0027502C:
loc_00275033:
    if (result != 0) goto loc_00275033;
    if (condition_is_above_or_equal) goto loc_0027496B;
    result = KiRemoveSystemWorkPriorityKick((uint32_t)((uint32_t)(*(uint64_t *)(*(uint64_t *)(local_r13)))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)(local_rsi)))))), (uint32_t)((uint32_t)(local_rsi)), 0);
    goto loc_0027496B;
loc_002750E9:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(result), (uint8_t)((uint32_t)((uint32_t)(*(uint64_t *)(*(uint64_t *)(local_r13))))), (uint32_t)((uint32_t)(local_rsi)), 0);
    goto loc_00274DFB;
loc_002750F9:
    if (((uint8_t)((uint8_t)(result))) != 2) goto loc_002752CB;
    *(uint8_t *)(result + 0x11) = 5;
    result = KiInsertQueueInternal(*(uint64_t *)(result + 0x18), result, (uint32_t)((uint32_t)(local_rsi)), 0);
    goto loc_00274E9A;
loc_0027512D:
    goto loc_00274E11;
loc_00275149:
    Arg2 = 0;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg13 + 0x8EF0))) + (*(uint32_t *)(arg13 + 0x8EEC)));
    if (0 != 0) goto loc_00274BDC;
loc_0027516C:
    *(uint32_t *)(local_rbp - 0x10) = (uint32_t)((uint32_t)((uint32_t)(local_rsi)));
    *(uint64_t *)(local_rbp - 0x18) = local_rbx;
    *(uint64_t *)(local_rbp - 0x38) = *(uint64_t *)((uint8_t)(result) + 0x8);
    *(uint32_t *)(local_rbp - 0x20) = (uint32_t)((uint32_t)(*(uint32_t *)((uint8_t)(result) + 0x24)));
    *(void **)(local_rbp - 0x30) = Arg7;
    *(uint64_t *)(local_rbp - 0x28) = *(uint64_t *)((uint8_t)(result));
    local_r10 = (uint32_t)(((uint32_t)(v_stack_p44)) - (*(uint32_t *)((uint8_t)(result) + 0x2C)));
    *(uint32_t *)(local_rbp - 0xC) = (uint32_t)(local_r10);
    *(uint64_t *)(local_rbp) = 48;
    v_stack_p20 = 0x1601802ULL;
    *(uint32_t *)(local_rbp - 0x1C) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x510)));
    *(uint64_t *)(local_rbp - 0x8) = local_rbp - 56;
    result = EtwTraceKernelEvent(local_rbp - 8, 1, (uint32_t)(0x20020000ULL), (uint32_t)(0x52BULL));
    goto loc_00274C0B;
loc_002751DE:
    if (((uint32_t)(local_rsi)) == 1) { local_r15 = 1; }
    goto loc_00274EE0;
loc_002751EF:
    if (1 > ((uint32_t)(local_r15))) { local_r15 = 1; }
    goto loc_00274ED6;
loc_00275229:
    if (*(uint64_t *)(2 - 0x28) != 0) goto loc_002752EF;
    if (!sign_flag) goto loc_00275456;
    Arg2 = 0;
    v_stack_p20 = 1;
    result = KeBugCheckEx(Arg2 + 24, Arg2, 2, *(uint64_t *)(2 - 0x28) + 4);
loc_00275256:
    if (((uint8_t)(Arg2 + 24)) == 4) goto loc_002753A1;
    Arg4 = 0;
    result = KiTryUnwaitThread(Arg13, result, 256, Arg4);
loc_002752CB:
    if (((uint8_t)(Arg7)) == 4) goto loc_0027542A;
    Arg4 = 0;
    result = KiTryUnwaitThread(Arg13, Arg12, 256, Arg4);
    goto loc_00274E3D;
loc_002752EF:
    v_stack_p20 = Arg13;
    result = (2 - 48) >> (8);
    Arg2 = ((uint8_t)(result)) ^ (*(uint8_t *)(2 - 0x18));
    Arg2 = (Arg2) ^ (*(uint8_t *)(v_rip + 0xD51B2B));
    result = KeBugCheckEx(3 + 21, *(uint64_t *)(v_rip - 0x275301 + Arg2 * 8 + 0xFC7800), 2, 3);
loc_00275332:
    *(uint64_t *)(local_rbx + 0x20) = local_r15;
    *(uint64_t *)(local_rbp - 0x80) = *(uint64_t *)(local_rbx + 0x20);
    *(uint32_t *)(local_rbx + 0x48) = (uint32_t)(local_r15);
    goto loc_0027487E;
loc_002753A1:
    *(uint8_t *)(*(uint64_t *)(local_rbx + 0x20) + 0x11) = 5;
    *(uint32_t *)(3 + 0x4) = 0;
    result = KeInsertQueueDpc(*(uint64_t *)(*(uint64_t *)(local_rbx + 0x20) + 0x18), 3, *(uint64_t *)(local_rbx + 0x20), 3);
loc_002753CF:
    result = ExAllocatePool2(112 - 48, 112, (uint32_t)(0x736F6F42ULL), (uint32_t)(Arg12) + 24);
    if (result != 0) {
        Arg4 = 0;
        Arg3 = result + 16;
        Arg2 = Arg4 + 10;
        Arg1 = Arg2 - 9;
        result = RtlCaptureStackBackTrace(Arg1, Arg2, Arg3, Arg4);
        Arg1 = *(uint64_t *)(gs_base + (0 + 0x188));
        result = 0;
        *(uint64_t *)(result + 0x60) = Arg1;
        *(uint64_t *)(result + 0x68) = 0;
    }
    result = KeAcquireSpinLockRaiseToDpc(2 + 1552, Arg2, Arg3, Arg4);
    goto loc_002747D4;
loc_0027542A:
    Arg1 = 0;
    *(uint8_t *)(result + 0x11) = 5;
    *(uint32_t *)(Arg4 + 0x4) = 0;
    result = KeInsertQueueDpc(*(uint64_t *)(result + 0x18), 0, result, Arg4);
    goto loc_00274E3D;
loc_00275456:
    result = ObpDeferObjectDeletion(2 - 48, 0, result, Arg4);
    goto loc_0027484F;
loc_002754BA:
    if (1 == 0) goto loc_002747F1;
loc_002754C3:
    if (((*(uint8_t *)(v_rip + 0xD5163C)) & (1)) != 0) goto loc_002754FB;
loc_002754D3:
loc_002754D8:
    if ((*(uint32_t *)(v_rip + 0xD51841)) != 0) {
        Arg1 = 2;
        Arg2 = (uint8_t)((uint8_t)(result));
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, result, Arg4);
    }
    goto loc_002747F1;
loc_002754FB:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC98957))) != 0) goto loc_002754D3;
    result = KiReleaseSpinLockInstrumented(Arg1, *(uint64_t *)(local_rbp + 0x48), result, Arg4);
    goto loc_002754D8;
loc_002755D1:
    if ((*(uint32_t *)(2 + 0x5E0)) == 0) goto loc_0027560C;
    if (result == 0) goto loc_002754C3;
    *(uint64_t *)(result) = 2 + 1536;
    *(uint64_t *)(result + 0x8) = *(uint64_t *)(2 + 0x600 + 0x8);
    *(uint64_t *)(*(uint64_t *)(2 + 0x600 + 0x8)) = result;
    *(uint64_t *)(2 + 0x600 + 0x8) = result;
    goto loc_002754C3;
loc_0027560C:
    result = 2 + 1536;
    if (result != 0) {
        Arg2 = 0x736F6F42ULL;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, result, Arg4);
    }
loc_00275625:
    if ((*(uint64_t *)(2 + 0x5F0)) != (2 + 1520)) goto loc_0027566A;
loc_00275634:
    if ((*(uint64_t *)(2 + 0x600)) == (2 + 1536)) goto loc_002754C3;
    *(uint64_t *)(2 + 0x600) = *(uint64_t *)(*(uint64_t *)(2 + 0x600));
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(2 + 0x600)) + 0x8) = 2 + 1536;
    result = ExFreePoolWithTag(*(uint64_t *)(2 + 0x600), (uint32_t)(0x736F6F42ULL), result, Arg4);
    goto loc_00275634;
loc_0027566A:
    *(uint64_t *)(2 + 0x600) = *(uint64_t *)(*(uint64_t *)(2 + 0x600));
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(2 + 0x600)) + 0x8) = 2 + 1536;
    result = ExFreePoolWithTag(*(uint64_t *)(2 + 0x600), (uint32_t)(0x736F6F42ULL), result, Arg4);
    goto loc_00275625;
loc_002756E1:
    *(uint32_t *)((uint8_t)(result) + 0x24) = (uint32_t)(result);
    goto loc_00274BAF;
loc_002756E9:
    if ((*(uint16_t *)((uint8_t)(result) + 0x18)) != Arg8) goto loc_00274BCF;
    if ((*(uint8_t *)((uint8_t)(result) + 0x1A)) != Arg6) goto loc_00274BCF;
    Arg4 = (*(uint64_t *)(local_rbp - 0x70)) - (result);
    goto loc_00274BD2;
loc_00275712:
    Arg2 = 0;
    result = (uint32_t)(((uint32_t)((uint32_t)(v_rip - 2577153))) - (Arg6));
    if (0 == 0) goto loc_0027516C;
    goto loc_00274BED;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg7` | `+ 0x4` | `32` | `R/W` |
| `Arg7` | `+ 0x4` | `32` | `W` |
| `Arg10` | `+ 0x0` | `64` | `R` |
| `Arg13` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0027475D&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
