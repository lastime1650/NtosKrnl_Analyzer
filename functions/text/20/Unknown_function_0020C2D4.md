# sub_0020C2D4

- RVA: `0x0020C2D4`–`0x0020CEA5` (길이 `3,025` bytes)
- VA: `0x000000014020C2D4`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005D8D0`
- 디코드: `681`개 명령, `3,025/3,025` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **44**; 고유 호출 대상: **20**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **6**

### Outgoing calls
- `0x0020C325` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0020C334` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0020C3AE` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0020C3F1` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x0020C401` → [KiDeliverApc](../25/KiDeliverApc_function_00250F20.md) (function, `0x00250F20`)
- `0x0020C489` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0020C49D` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0020C4AC` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0020C5C1` → [KiCommitThreadWait](KiCommitThreadWait_function_0020DFE0.md) (function, `0x0020DFE0`)
- `0x0020C63A` → [KiAcquireKobjectLockSafe](../25/KiAcquireKobjectLockSafe_function_00251C90.md) (function, `0x00251C90`)
- `0x0020C651` → [KiAttemptFastRemoveQueue](../41/KiAttemptFastRemoveQueue_function_00419900.md) (function, `0x00419900`)
- `0x0020C672` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x0020C75B` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0020C789` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x0020C81C` → [KiProcessThreadWaitList](../25/KiProcessThreadWaitList_function_00252CC0.md) (function, `0x00252CC0`)
- `0x0020C82A` → [KiFastExitThreadWait](../22/KiFastExitThreadWait_function_00220BB0.md) (function, `0x00220BB0`)
- `0x0020C844` → [EtwTraceDequeueWork](../4B/EtwTraceDequeueWork_function_004BDBFC.md) (function, `0x004BDBFC`)
- `0x0020C854` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x0020C888` → [KiProcessDeferredReadyList](../25/KiProcessDeferredReadyList_function_00250800.md) (function, `0x00250800`)
- `0x0020C8C9` → [Feature_StackingDecayBoosts__private_IsEnabledNoReportingNoInline](../4E/Feature_StackingDecayBoosts__private_IsEnabledNoReportingNoInline_function_004EF7C0.md) (function, `0x004EF7C0`)
- `0x0020C94C` → [KiSetPriorityThread](../22/KiSetPriorityThread_function_00220E78.md) (function, `0x00220E78`)
- `0x0020C96A` → [KiComputeThreadPriorityNonStacking](../5C/KiComputeThreadPriorityNonStacking_function_005CA81C.md) (function, `0x005CA81C`)
- `0x0020C99A` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0020C9A9` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0020C9C1` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0020C9D0` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0020C9E8` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0020C9F7` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0020CA4F` → [Feature_StackingDecayBoosts__private_IsEnabledNoReportingNoInline](../4E/Feature_StackingDecayBoosts__private_IsEnabledNoReportingNoInline_function_004EF7C0.md) (function, `0x004EF7C0`)
- `0x0020CAD2` → [KiSetPriorityThread](../22/KiSetPriorityThread_function_00220E78.md) (function, `0x00220E78`)
- `0x0020CAF0` → [KiComputeThreadPriorityNonStacking](../5C/KiComputeThreadPriorityNonStacking_function_005CA81C.md) (function, `0x005CA81C`)
- `0x0020CB20` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0020CB2F` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0020CB4F` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x0020CB6B` → [KiProcessDeferredReadyList](../25/KiProcessDeferredReadyList_function_00250800.md) (function, `0x00250800`)
- `0x0020CB75` → [KeDisableInterrupts](../21/KeDisableInterrupts_function_00217BE0.md) (function, `0x00217BE0`)
- `0x0020CBE3` → [KiProcessDeferredReadyList](../25/KiProcessDeferredReadyList_function_00250800.md) (function, `0x00250800`)
- `0x0020CC3E` → [KeDisableInterrupts](../21/KeDisableInterrupts_function_00217BE0.md) (function, `0x00217BE0`)
- `0x0020CD1F` → [KeDisableInterrupts](../21/KeDisableInterrupts_function_00217BE0.md) (function, `0x00217BE0`)
- `0x0020CD6E` → [KiRemoveSystemWorkPriorityKick](../26/KiRemoveSystemWorkPriorityKick_function_002631D0.md) (function, `0x002631D0`)
- `0x0020CDBB` → [KiRemoveSystemWorkPriorityKick](../26/KiRemoveSystemWorkPriorityKick_function_002631D0.md) (function, `0x002631D0`)
- `0x0020CDE0` → [KiRemoveSystemWorkPriorityKick](../26/KiRemoveSystemWorkPriorityKick_function_002631D0.md) (function, `0x002631D0`)
- `0x0020CE48` → [KiSrcuReportQuiescent](../5C/KiSrcuReportQuiescent_function_005C2C08.md) (function, `0x005C2C08`)
- `0x0020CE59` → [KiSrcuFlushCompleted](../5C/KiSrcuFlushCompleted_function_005C22B4.md) (function, `0x005C22B4`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0020C2F2` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x0020C317` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)
- `0x0020C3E0` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x0020C74A` → RVA `0x00EFAAB8` (`.data`; read)
- `0x0020C82F` → RVA `0x00FC6B04` (`ALMOSTRO`; read)
- `0x0020CE7C` → RVA `0x00F210E8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **49**
  - `0x0020C2E4` → [sub_0020BDAA + 0x37B](Unknown_function_0020BDAA.md) (`tail-transfer`)
  - `0x0020C312` → [sub_0020BDAA + 0x24F](Unknown_function_0020BDAA.md) (`tail-transfer`)
  - `0x0020C31F` → [sub_0020BDAA + 0xFD](Unknown_function_0020BDAA.md) (`tail-transfer`)
  - `0x0020C32C` → [sub_0020BDAA + 0xFD](Unknown_function_0020BDAA.md) (`tail-transfer`)
  - `0x0020C339` → [sub_0020BDAA + 0xFF](Unknown_function_0020BDAA.md) (`tail-transfer`)
  - `0x0020C34D` → [sub_0020BDAA + 0x354](Unknown_function_0020BDAA.md) (`tail-transfer`)
  - `0x0020C3BC` → [sub_0020BDAA + 0xA1](Unknown_function_0020BDAA.md) (`tail-transfer`)
  - `0x0020C3C9` → [sub_0020BDAA + 0x117](Unknown_function_0020BDAA.md) (`tail-transfer`)
  - `0x0020C3D2` → [sub_0020BDAA + 0x117](Unknown_function_0020BDAA.md) (`tail-transfer`)
  - `0x0020C425` → [sub_0020BDAA + 0xC5](Unknown_function_0020BDAA.md) (`tail-transfer`)
  - `0x0020C497` → [sub_0020BDAA + 0x313](Unknown_function_0020BDAA.md) (`tail-transfer`)
  - `0x0020C4A4` → [sub_0020BDAA + 0x313](Unknown_function_0020BDAA.md) (`tail-transfer`)
  - `0x0020C4B1` → [sub_0020BDAA + 0x315](Unknown_function_0020BDAA.md) (`tail-transfer`)
  - `0x0020C4BD` → [sub_0020BDAA + 0x359](Unknown_function_0020BDAA.md) (`tail-transfer`)
  - `0x0020C4C6` → [sub_0020BDAA + 0x359](Unknown_function_0020BDAA.md) (`tail-transfer`)
  - `0x0020C4DB` → [sub_0020BDAA + 0x37B](Unknown_function_0020BDAA.md) (`tail-transfer`)
  - `0x0020C589` → [sub_0020BDAA + 0x22B](Unknown_function_0020BDAA.md) (`tail-transfer`)
  - `0x0020C5E4` → [sub_0020BDAA + 0x3AD](Unknown_function_0020BDAA.md) (`tail-transfer`)
  - `0x0020C5F2` → [sub_0020BDAA + 0x3AD](Unknown_function_0020BDAA.md) (`tail-transfer`)
  - `0x0020C5FE` → [sub_0020BDAA + 0x3AD](Unknown_function_0020BDAA.md) (`tail-transfer`)
  - `0x0020C60D` → [sub_0020BDAA + 0x3AD](Unknown_function_0020BDAA.md) (`tail-transfer`)
  - `0x0020C617` → [sub_0020BDAA + 0x3AD](Unknown_function_0020BDAA.md) (`tail-transfer`)
  - `0x0020C67E` → [sub_0020BDAA + 0x3AD](Unknown_function_0020BDAA.md) (`tail-transfer`)
  - `0x0020C77D` → [sub_0020BDAA + 0xA1](Unknown_function_0020BDAA.md) (`tail-transfer`)
  - `0x0020C7A4` → [sub_0020BDAA + 0x1AD](Unknown_function_0020BDAA.md) (`tail-transfer`)
  - `0x0020C7B1` → [sub_0020BDAA + 0x22B](Unknown_function_0020BDAA.md) (`tail-transfer`)
  - `0x0020C7BA` → [sub_0020BDAA + 0x22B](Unknown_function_0020BDAA.md) (`tail-transfer`)
  - `0x0020C84B` → [sub_0020BDAA + 0x3CA](Unknown_function_0020BDAA.md) (`tail-transfer`)
  - `0x0020C88D` → [sub_0020C222 + 0x7C](Unknown_function_0020C222.md) (`tail-transfer`)
  - `0x0020C960` → [sub_0020C222 + 0x53](Unknown_function_0020C222.md) (`tail-transfer`)
  - `0x0020CA0E` → [sub_0020BDAA + 0x354](Unknown_function_0020BDAA.md) (`tail-transfer`)
  - `0x0020CAE6` → [sub_0020BDAA + 0x384](Unknown_function_0020BDAA.md) (`tail-transfer`)
  - `0x0020CB44` → [sub_0020BDAA + 0x3AD](Unknown_function_0020BDAA.md) (`tail-transfer`)
  - `0x0020CB70` → [sub_0020BDAA + 0x18C](Unknown_function_0020BDAA.md) (`tail-transfer`)
  - `0x0020CBB5` → [sub_0020BDAA + 0x22B](Unknown_function_0020BDAA.md) (`tail-transfer`)
  - `0x0020CBBE` → [sub_0020BDAA + 0x22B](Unknown_function_0020BDAA.md) (`tail-transfer`)
  - `0x0020CBE8` → [sub_0020BDAA + 0x3AD](Unknown_function_0020BDAA.md) (`tail-transfer`)
  - `0x0020CBFA` → [sub_0020BDAA + 0x1AD](Unknown_function_0020BDAA.md) (`tail-transfer`)
  - `0x0020CC65` → [sub_0020BDAA + 0x22B](Unknown_function_0020BDAA.md) (`tail-transfer`)
  - `0x0020CC94` → [sub_0020BDAA + 0x1C](Unknown_function_0020BDAA.md) (`tail-transfer`)
  - `0x0020CCB7` → [sub_0020BDAA + 0x22B](Unknown_function_0020BDAA.md) (`tail-transfer`)
  - `0x0020CCC0` → [sub_0020BDAA + 0x22B](Unknown_function_0020BDAA.md) (`tail-transfer`)
  - `0x0020CD0D` → [sub_0020BDAA + 0x354](Unknown_function_0020BDAA.md) (`tail-transfer`)
  - `0x0020CD19` → [sub_0020BDAA + 0x29](Unknown_function_0020BDAA.md) (`tail-transfer`)
  - `0x0020CD33` → [sub_0020BDAA + 0x29](Unknown_function_0020BDAA.md) (`tail-transfer`)
  - `0x0020CD4F` → [sub_0020BDAA + 0x29](Unknown_function_0020BDAA.md) (`tail-transfer`)
  - `0x0020CD9C` → [sub_0020BDAA + 0x1C](Unknown_function_0020BDAA.md) (`tail-transfer`)
  - `0x0020CE06` → [sub_006D66EC + 0x18](../6D/Unknown_function_006D66EC.md) (`tail-transfer`)
  - `0x0020CE13` → [sub_006D66EC](../6D/Unknown_function_006D66EC.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0020C2D4  4C 8B BC 24 C0 00 00 00         mov r15, qword ptr [rsp + 0xc0]
0020C2DC  B9 80 00 00 00                  mov ecx, 0x80
0020C2E1  49 89 0F                        mov qword ptr [r15], rcx
0020C2E4  E9 3C FE FF FF                  jmp 0x14020c125
0020C2E9  0F 1F 80 00 00 00 00            nop dword ptr [rax]
0020C2F0  FF C6                           inc esi
0020C2F2  85 35 B4 8F DB 00               test dword ptr [rip + 0xdb8fb4], esi
0020C2F8  0F 84 DC 06 00 00               je 0x14020c9da
0020C2FE  F3 90                           pause
0020C300  41 8B 06                        mov eax, dword ptr [r14]
0020C303  84 C0                           test al, al
0020C305  78 E9                           js 0x14020c2f0
0020C307  F0 41 0F BA 2E 07               lock bts dword ptr [r14], 7
0020C30D  72 E1                           jb 0x14020c2f0
0020C30F  45 33 C9                        xor r9d, r9d
0020C312  E9 E2 FC FF FF                  jmp 0x14020bff9
0020C317  8B 05 9B A7 DB 00               mov eax, dword ptr [rip + 0xdba79b]
0020C31D  A8 40                           test al, 0x40
0020C31F  0F 84 82 FB FF FF               je 0x14020bea7
0020C325  E8 66 31 10 00                  call 0x14030f490
0020C32A  84 C0                           test al, al
0020C32C  0F 84 75 FB FF FF               je 0x14020bea7
0020C332  8B CE                           mov ecx, esi
0020C334  E8 27 31 10 00                  call 0x14030f460
0020C339  E9 6B FB FF FF                  jmp 0x14020bea9
0020C33E  80 8F C2 00 00 00 02            or byte ptr [rdi + 0xc2], 2
0020C345  B8 C0 00 00 00                  mov eax, 0xc0
0020C34A  45 33 C9                        xor r9d, r9d
0020C34D  E9 AC FD FF FF                  jmp 0x14020c0fe
0020C352  41 8B E9                        mov ebp, r9d
0020C355  F0 48 0F BA 6F 40 00            lock bts qword ptr [rdi + 0x40], 0
0020C35C  73 1B                           jae 0x14020c379
0020C35E  FF C5                           inc ebp
0020C360  85 2D 46 8F DB 00               test dword ptr [rip + 0xdb8f46], ebp
0020C366  0F 84 20 06 00 00               je 0x14020c98c
0020C36C  F3 90                           pause
0020C36E  48 8B 47 40                     mov rax, qword ptr [rdi + 0x40]
0020C372  48 85 C0                        test rax, rax
0020C375  74 DE                           je 0x14020c355
0020C377  EB E5                           jmp 0x14020c35e
0020C379  48 0F BE 8F 1B 03 00 00         movsx rcx, byte ptr [rdi + 0x31b]
0020C381  4C 8B C1                        mov r8, rcx
0020C384  48 8D 14 39                     lea rdx, [rcx + rdi]
0020C388  0F B6 82 38 03 00 00            movzx eax, byte ptr [rdx + 0x338]
0020C38F  84 C0                           test al, al
0020C391  0F 85 FB 04 00 00               jne 0x14020c892
0020C397  41 B9 02 00 00 00               mov r9d, 2
0020C39D  48 C7 44 24 20 00 00 00 00      mov qword ptr [rsp + 0x20], 0
0020C3A6  48 8B D7                        mov rdx, rdi
0020C3A9  B9 57 01 00 00                  mov ecx, 0x157
0020C3AE  E8 AD 12 2F 00                  call 0x1404fd660
0020C3B3  CC                              int3
0020C3B4  F0 41 81 26 7F FF FF FF         lock and dword ptr [r14], 0xffffff7f
0020C3BC  E9 8A FA FF FF                  jmp 0x14020be4b
0020C3C1  66 83 BF E6 01 00 00 00         cmp word ptr [rdi + 0x1e6], 0
0020C3C9  0F 85 F2 FA FF FF               jne 0x14020bec1
0020C3CF  41 3A EC                        cmp bpl, r12b
0020C3D2  0F 83 E9 FA FF FF               jae 0x14020bec1
0020C3D8  48 C7 47 40 00 00 00 00         mov qword ptr [rdi + 0x40], 0
0020C3E0  83 3D 39 A9 DB 00 00            cmp dword ptr [rip + 0xdba939], 0
0020C3E7  74 0D                           je 0x14020c3f6
0020C3E9  44 0F 20 C1                     mov rcx, cr8
0020C3ED  41 0F B6 D4                     movzx edx, r12b
0020C3F1  E8 A2 92 2E 00                  call 0x1404f5698
0020C3F6  45 0F 22 C4                     mov cr8, r12
0020C3FA  45 33 C0                        xor r8d, r8d
0020C3FD  33 D2                           xor edx, edx
0020C3FF  33 C9                           xor ecx, ecx
0020C401  E8 1A 4B 04 00                  call 0x140250f20
0020C406  44 0F 20 C1                     mov rcx, cr8
0020C40A  45 0F 22 C6                     mov cr8, r14
0020C40E  83 3D 0B A9 DB 00 00            cmp dword ptr [rip + 0xdba90b], 0
0020C415  0F 85 35 04 00 00               jne 0x14020c850
0020C41B  40 88 AF 86 01 00 00            mov byte ptr [rdi + 0x186], bpl
0020C422  45 33 C9                        xor r9d, r9d
0020C425  E9 45 FA FF FF                  jmp 0x14020be6f
0020C42A  41 8B F1                        mov esi, r9d
0020C42D  0F 1F 00                        nop dword ptr [rax]
0020C430  F0 48 0F BA 6F 40 00            lock bts qword ptr [rdi + 0x40], 0
0020C437  73 1B                           jae 0x14020c454
0020C439  FF C6                           inc esi
0020C43B  85 35 6B 8E DB 00               test dword ptr [rip + 0xdb8e6b], esi
0020C441  0F 84 CB 06 00 00               je 0x14020cb12
0020C447  F3 90                           pause
0020C449  48 8B 47 40                     mov rax, qword ptr [rdi + 0x40]
0020C44D  48 85 C0                        test rax, rax
0020C450  74 DE                           je 0x14020c430
0020C452  EB E5                           jmp 0x14020c439
0020C454  4C 0F BE 8F 1B 03 00 00         movsx r9, byte ptr [rdi + 0x31b]
0020C45C  4D 8B C1                        mov r8, r9
0020C45F  49 8D 0C 39                     lea rcx, [r9 + rdi]
0020C463  0F B6 81 38 03 00 00            movzx eax, byte ptr [rcx + 0x338]
0020C46A  84 C0                           test al, al
0020C46C  0F 85 A1 05 00 00               jne 0x14020ca13
0020C472  41 B9 02 00 00 00               mov r9d, 2
0020C478  48 C7 44 24 20 00 00 00 00      mov qword ptr [rsp + 0x20], 0
0020C481  48 8B D7                        mov rdx, rdi
0020C484  B9 57 01 00 00                  mov ecx, 0x157
0020C489  E8 D2 11 2F 00                  call 0x1404fd660
0020C48E  CC                              int3
0020C48F  8B 05 23 A6 DB 00               mov eax, dword ptr [rip + 0xdba623]
0020C495  A8 40                           test al, 0x40
0020C497  0F 84 20 FC FF FF               je 0x14020c0bd
0020C49D  E8 EE 2F 10 00                  call 0x14030f490
0020C4A2  84 C0                           test al, al
0020C4A4  0F 84 13 FC FF FF               je 0x14020c0bd
0020C4AA  8B CE                           mov ecx, esi
0020C4AC  E8 AF 2F 10 00                  call 0x14030f460
0020C4B1  E9 09 FC FF FF                  jmp 0x14020c0bf
0020C4B6  F6 87 C2 00 00 00 02            test byte ptr [rdi + 0xc2], 2
0020C4BD  0F 84 40 FC FF FF               je 0x14020c103
0020C4C3  40 84 ED                        test bpl, bpl
0020C4C6  0F 84 37 FC FF FF               je 0x14020c103
0020C4CC  4C 8B BC 24 C0 00 00 00         mov r15, qword ptr [rsp + 0xc0]
0020C4D4  49 C7 07 C0 00 00 00            mov qword ptr [r15], 0xc0
0020C4DB  E9 45 FC FF FF                  jmp 0x14020c125
0020C4E0  48 89 06                        mov qword ptr [rsi], rax
0020C4E3  48 89 4E 08                     mov qword ptr [rsi + 8], rcx
0020C4E7  48 89 31                        mov qword ptr [rcx], rsi
0020C4EA  48 89 70 08                     mov qword ptr [rax + 8], rsi
0020C4EE  F0 41 81 26 7F FF FF FF         lock and dword ptr [r14], 0xffffff7f
0020C4F6  45 33 C9                        xor r9d, r9d
0020C4F9  4C 8D 97 40 01 00 00            lea r10, [rdi + 0x140]
0020C500  41 8B F1                        mov esi, r9d
0020C503  41 C6 42 10 03                  mov byte ptr [r10 + 0x10], 3
0020C508  41 C6 42 11 04                  mov byte ptr [r10 + 0x11], 4
0020C50D  66 41 C7 42 12 80 00            mov word ptr [r10 + 0x12], 0x80
0020C514  4D 89 72 20                     mov qword ptr [r10 + 0x20], r14
0020C518  F0 41 0F BA 2E 07               lock bts dword ptr [r14], 7
0020C51E  0F 82 CC 01 00 00               jb 0x14020c6f0
0020C524  41 83 7E 04 00                  cmp dword ptr [r14 + 4], 0
0020C529  4C 8B BC 24 C0 00 00 00         mov r15, qword ptr [rsp + 0xc0]
0020C531  0F 85 E7 01 00 00               jne 0x14020c71e
0020C537  45 84 66 01                     test byte ptr [r14 + 1], r12b
0020C53B  0F 85 58 07 00 00               jne 0x14020cc99
0020C541  4C 8B 44 24 58                  mov r8, qword ptr [rsp + 0x58]
0020C546  8B 54 24 30                     mov edx, dword ptr [rsp + 0x30]
0020C54A  49 8B C0                        mov rax, r8
0020C54D  83 FA 02                        cmp edx, 2
0020C550  0F 84 2D 01 00 00               je 0x14020c683
0020C556  85 D2                           test edx, edx
0020C558  74 1F                           je 0x14020c579
0020C55A  4D 85 C0                        test r8, r8
0020C55D  0F 84 FB 02 00 00               je 0x14020c85e
0020C563  48 B9 14 00 00 00 80 F7 FF FF   movabs rcx, 0xfffff78000000014
0020C56D  48 8B 09                        mov rcx, qword ptr [rcx]
0020C570  48 3B C8                        cmp rcx, rax
0020C573  0F 87 E5 02 00 00               ja 0x14020c85e
0020C579  F0 41 FF 4E 28                  lock dec dword ptr [r14 + 0x28]
0020C57E  49 8D 46 08                     lea rax, [r14 + 8]
0020C582  48 8B 08                        mov rcx, qword ptr [rax]
0020C585  48 39 41 08                     cmp qword ptr [rcx + 8], rax
0020C589  0F 85 46 FA FF FF               jne 0x14020bfd5
0020C58F  49 89 0A                        mov qword ptr [r10], rcx
0020C592  49 89 42 08                     mov qword ptr [r10 + 8], rax
0020C596  4C 89 51 08                     mov qword ptr [rcx + 8], r10
0020C59A  4C 89 10                        mov qword ptr [rax], r10
0020C59D  F0 41 81 26 7F FF FF FF         lock and dword ptr [r14], 0xffffff7f
0020C5A5  4C 89 4C 24 28                  mov qword ptr [rsp + 0x28], r9
0020C5AA  48 8B CF                        mov rcx, rdi
0020C5AD  4D 8B C8                        mov r9, r8
0020C5B0  44 88 A7 4B 02 00 00            mov byte ptr [rdi + 0x24b], r12b
0020C5B7  44 8B C2                        mov r8d, edx
0020C5BA  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
0020C5BE  49 8B D2                        mov rdx, r10
0020C5C1  E8 1A 1A 00 00                  call 0x14020dfe0
0020C5C6  45 33 C9                        xor r9d, r9d
0020C5C9  41 8B D9                        mov ebx, r9d
0020C5CC  88 9F 83 02 00 00               mov byte ptr [rdi + 0x283], bl
0020C5D2  48 3D 00 01 00 00               cmp rax, 0x100
0020C5D8  0F 84 83 01 00 00               je 0x14020c761
0020C5DE  49 89 07                        mov qword ptr [r15], rax
0020C5E1  45 3B EC                        cmp r13d, r12d
0020C5E4  0F 86 6D FB FF FF               jbe 0x14020c157
0020C5EA  B9 80 00 00 00                  mov ecx, 0x80
0020C5EF  48 3B C1                        cmp rax, rcx
0020C5F2  0F 84 5F FB FF FF               je 0x14020c157
0020C5F8  48 3D C0 00 00 00               cmp rax, 0xc0
0020C5FE  0F 84 53 FB FF FF               je 0x14020c157
0020C604  48 05 FF FE FF FF               add rax, -0x101
0020C60A  49 3B C4                        cmp rax, r12
0020C60D  0F 86 44 FB FF FF               jbe 0x14020c157
0020C613  41 39 5E 04                     cmp dword ptr [r14 + 4], ebx
0020C617  0F 84 3A FB FF FF               je 0x14020c157
0020C61D  44 0F 20 C3                     mov rbx, cr8
0020C621  B8 02 00 00 00                  mov eax, 2
0020C626  44 0F 22 C0                     mov cr8, rax
0020C62A  44 39 0D EF A6 DB 00            cmp dword ptr [rip + 0xdba6ef], r9d
0020C631  0F 85 12 05 00 00               jne 0x14020cb49
0020C637  49 8B CE                        mov rcx, r14
0020C63A  E8 51 56 04 00                  call 0x140251c90
0020C63F  41 83 7E 04 00                  cmp dword ptr [r14 + 4], 0
0020C644  74 14                           je 0x14020c65a
0020C646  45 8D 45 FF                     lea r8d, [r13 - 1]
0020C64A  49 8B CE                        mov rcx, r14
0020C64D  49 8D 57 08                     lea rdx, [r15 + 8]
0020C651  E8 AA D2 20 00                  call 0x140419900
0020C656  44 8D 60 01                     lea r12d, [rax + 1]
0020C65A  F0 41 81 26 7F FF FF FF         lock and dword ptr [r14], 0xffffff7f
0020C662  83 3D B7 A6 DB 00 00            cmp dword ptr [rip + 0xdba6b7], 0
0020C669  74 0C                           je 0x14020c677
0020C66B  44 0F 20 C1                     mov rcx, cr8
0020C66F  0F B6 D3                        movzx edx, bl
0020C672  E8 21 90 2E 00                  call 0x1404f5698
0020C677  0F B6 C3                        movzx eax, bl
0020C67A  44 0F 22 C0                     mov cr8, rax
0020C67E  E9 D4 FA FF FF                  jmp 0x14020c157
0020C683  48 B8 B0 03 00 00 80 F7 FF FF   movabs rax, 0xfffff780000003b0
0020C68D  48 B9 08 00 00 00 80 F7 FF FF   movabs rcx, 0xfffff78000000008
0020C697  48 8B 00                        mov rax, qword ptr [rax]
0020C69A  48 8B 09                        mov rcx, qword ptr [rcx]
0020C69D  48 2B 8F F8 00 00 00            sub rcx, qword ptr [rdi + 0xf8]
0020C6A4  8B 97 B8 03 00 00               mov edx, dword ptr [rdi + 0x3b8]
0020C6AA  48 2B C8                        sub rcx, rax
0020C6AD  80 BF 87 01 00 00 00            cmp byte ptr [rdi + 0x187], 0
0020C6B4  49 8B C0                        mov rax, r8
0020C6B7  74 23                           je 0x14020c6dc
0020C6B9  83 BF E4 01 00 00 00            cmp dword ptr [rdi + 0x1e4], 0
0020C6C0  75 1A                           jne 0x14020c6dc
0020C6C2  80 BF 86 01 00 00 00            cmp byte ptr [rdi + 0x186], 0
0020C6C9  75 11                           jne 0x14020c6dc
0020C6CB  80 BF C0 00 00 00 00            cmp byte ptr [rdi + 0xc0], 0
0020C6D2  75 08                           jne 0x14020c6dc
0020C6D4  85 D2                           test edx, edx
0020C6D6  74 04                           je 0x14020c6dc
0020C6D8  49 8D 04 10                     lea rax, [r8 + rdx]
0020C6DC  8B 54 24 30                     mov edx, dword ptr [rsp + 0x30]
0020C6E0  E9 8B FE FF FF                  jmp 0x14020c570
0020C6E5  66 66 66 0F 1F 84 00 00 00 00 00  nop word ptr [rax + rax]
0020C6F0  FF C6                           inc esi
0020C6F2  85 35 B4 8B DB 00               test dword ptr [rip + 0xdb8bb4], esi
0020C6F8  0F 84 B5 02 00 00               je 0x14020c9b3
0020C6FE  F3 90                           pause
0020C700  41 8B 06                        mov eax, dword ptr [r14]
0020C703  84 C0                           test al, al
0020C705  78 E9                           js 0x14020c6f0
0020C707  F0 41 0F BA 2E 07               lock bts dword ptr [r14], 7
0020C70D  72 E1                           jb 0x14020c6f0
0020C70F  4C 8D 97 40 01 00 00            lea r10, [rdi + 0x140]
0020C716  45 33 C9                        xor r9d, r9d
0020C719  E9 06 FE FF FF                  jmp 0x14020c524
0020C71E  41 8B 46 28                     mov eax, dword ptr [r14 + 0x28]
0020C722  41 3B 46 2C                     cmp eax, dword ptr [r14 + 0x2c]
0020C726  0F 87 0B FE FF FF               ja 0x14020c537
0020C72C  49 8B 56 18                     mov rdx, qword ptr [r14 + 0x18]
0020C730  49 8D 4E 18                     lea rcx, [r14 + 0x18]
0020C734  41 8B E9                        mov ebp, r9d
0020C737  41 FF 4E 04                     dec dword ptr [r14 + 4]
0020C73B  48 8B 02                        mov rax, qword ptr [rdx]
0020C73E  48 85 C0                        test rax, rax
0020C741  75 66                           jne 0x14020c7a9
0020C743  48 8B 42 10                     mov rax, qword ptr [rdx + 0x10]
0020C747  4D 8B C6                        mov r8, r14
0020C74A  4C 8B 0D 67 E3 CE 00            mov r9, qword ptr [rip + 0xcee367]
0020C751  B9 96 00 00 00                  mov ecx, 0x96
0020C756  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0020C75B  E8 00 0F 2F 00                  call 0x1404fd660
0020C760  CC                              int3
0020C761  44 0F 20 C6                     mov rsi, cr8
0020C765  B8 02 00 00 00                  mov eax, 2
0020C76A  44 0F 22 C0                     mov cr8, rax
0020C76E  39 1D AC A5 DB 00               cmp dword ptr [rip + 0xdba5ac], ebx
0020C774  75 0C                           jne 0x14020c782
0020C776  40 88 B7 86 01 00 00            mov byte ptr [rdi + 0x186], sil
0020C77D  E9 C9 F6 FF FF                  jmp 0x14020be4b
0020C782  0F B6 D0                        movzx edx, al
0020C785  40 0F B6 CE                     movzx ecx, sil
0020C789  E8 6E 8F 2E 00                  call 0x1404f56fc
0020C78E  45 33 C9                        xor r9d, r9d
0020C791  EB E3                           jmp 0x14020c776
0020C793  C6 44 39 72 00                  mov byte ptr [rcx + rdi + 0x72], 0
0020C798  45 33 C9                        xor r9d, r9d
0020C79B  B9 01 01 00 00                  mov ecx, 0x101
0020C7A0  8B C1                           mov eax, ecx
0020C7A2  8B F1                           mov esi, ecx
0020C7A4  E9 AE F7 FF FF                  jmp 0x14020bf57
0020C7A9  4C 8B 42 08                     mov r8, qword ptr [rdx + 8]
0020C7AD  48 39 50 08                     cmp qword ptr [rax + 8], rdx
0020C7B1  0F 85 1E F8 FF FF               jne 0x14020bfd5
0020C7B7  49 39 10                        cmp qword ptr [r8], rdx
0020C7BA  0F 85 15 F8 FF FF               jne 0x14020bfd5
0020C7C0  49 89 00                        mov qword ptr [r8], rax
0020C7C3  4C 89 40 08                     mov qword ptr [rax + 8], r8
0020C7C7  8B C5                           mov eax, ebp
0020C7C9  FF C5                           inc ebp
0020C7CB  4C 89 0A                        mov qword ptr [rdx], r9
0020C7CE  49 89 14 C7                     mov qword ptr [r15 + rax*8], rdx
0020C7D2  48 8B 11                        mov rdx, qword ptr [rcx]
0020C7D5  48 3B D1                        cmp rdx, rcx
0020C7D8  74 09                           je 0x14020c7e3
0020C7DA  41 3B ED                        cmp ebp, r13d
0020C7DD  0F 82 54 FF FF FF               jb 0x14020c737
0020C7E3  85 ED                           test ebp, ebp
0020C7E5  0F 84 4C FD FF FF               je 0x14020c537
0020C7EB  F0 41 81 26 7F FF FF FF         lock and dword ptr [r14], 0xffffff7f
0020C7F3  C6 87 83 02 00 00 00            mov byte ptr [rdi + 0x283], 0
0020C7FA  65 48 8B 34 25 20 00 00 00      mov rsi, qword ptr gs:[0x20]
0020C803  48 83 BE 08 2D 00 00 00         cmp qword ptr [rsi + 0x2d08], 0
0020C80B  74 14                           je 0x14020c821
0020C80D  41 B9 02 00 00 00               mov r9d, 2
0020C813  45 33 C0                        xor r8d, r8d
0020C816  41 8B D4                        mov edx, r12d
0020C819  48 8B CE                        mov rcx, rsi
0020C81C  E8 9F 64 04 00                  call 0x140252cc0
0020C821  44 8B C3                        mov r8d, ebx
0020C824  48 8B D7                        mov rdx, rdi
0020C827  48 8B CE                        mov rcx, rsi
0020C82A  E8 81 43 01 00                  call 0x140220bb0
0020C82F  F7 05 CB A2 DB 00 00 00 00 01   test dword ptr [rip + 0xdba2cb], 0x1000000
0020C839  74 0E                           je 0x14020c849
0020C83B  44 8B C5                        mov r8d, ebp
0020C83E  49 8B D7                        mov rdx, r15
0020C841  48 8B CF                        mov rcx, rdi
0020C844  E8 B3 13 2B 00                  call 0x1404bdbfc
0020C849  8B C5                           mov eax, ebp
0020C84B  E9 24 F9 FF FF                  jmp 0x14020c174
0020C850  41 0F B6 D6                     movzx edx, r14b
0020C854  E8 A3 8E 2E 00                  call 0x1404f56fc
0020C859  E9 BD FB FF FF                  jmp 0x14020c41b
0020C85E  F0 41 81 26 7F FF FF FF         lock and dword ptr [r14], 0xffffff7f
0020C866  49 C7 07 02 01 00 00            mov qword ptr [r15], 0x102
0020C86D  41 8B EC                        mov ebp, r12d
0020C870  EB 81                           jmp 0x14020c7f3
0020C872  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
0020C87B  48 8D 54 24 48                  lea rdx, [rsp + 0x48]
0020C880  44 0F B6 87 86 01 00 00         movzx r8d, byte ptr [rdi + 0x186]
0020C888  E8 73 3F 04 00                  call 0x140250800
0020C88D  E9 0C FA FF FF                  jmp 0x14020c29e
0020C892  41 2A C4                        sub al, r12b
0020C895  88 82 38 03 00 00               mov byte ptr [rdx + 0x338], al
0020C89B  0F 85 B0 00 00 00               jne 0x14020c951
0020C8A1  8B 87 58 03 00 00               mov eax, dword ptr [rdi + 0x358]
0020C8A7  0F BB C8                        btc eax, ecx
0020C8AA  41 D3 E4                        shl r12d, cl
0020C8AD  89 87 58 03 00 00               mov dword ptr [rdi + 0x358], eax
0020C8B3  41 3B C4                        cmp eax, r12d
0020C8B6  0F 83 95 00 00 00               jae 0x14020c951
0020C8BC  80 BF C3 00 00 00 1F            cmp byte ptr [rdi + 0xc3], 0x1f
0020C8C3  0F 8F 88 00 00 00               jg 0x14020c951
0020C8C9  E8 F2 2E 2E 00                  call 0x1404ef7c0
0020C8CE  85 C0                           test eax, eax
0020C8D0  0F 84 8F 00 00 00               je 0x14020c965
0020C8D6  44 0F BE 87 33 02 00 00         movsx r8d, byte ptr [rdi + 0x233]
0020C8DE  45 8B D0                        mov r10d, r8d
0020C8E1  45 8B C8                        mov r9d, r8d
0020C8E4  41 83 F8 10                     cmp r8d, 0x10
0020C8E8  7D 44                           jge 0x14020c92e
0020C8EA  0F B6 8F 66 03 00 00            movzx ecx, byte ptr [rdi + 0x366]
0020C8F1  0F B7 97 06 02 00 00            movzx edx, word ptr [rdi + 0x206]
0020C8F8  8B C2                           mov eax, edx
0020C8FA  83 E0 0F                        and eax, 0xf
0020C8FD  41 03 C0                        add eax, r8d
0020C900  41 3B C1                        cmp eax, r9d
0020C903  44 8B C0                        mov r8d, eax
0020C906  45 0F 4E C1                     cmovle r8d, r9d
0020C90A  33 C0                           xor eax, eax
0020C90C  84 C9                           test cl, cl
0020C90E  0F 4F C1                        cmovg eax, ecx
0020C911  0F BE C0                        movsx eax, al
0020C914  44 03 C0                        add r8d, eax
0020C917  41 83 F8 10                     cmp r8d, 0x10
0020C91B  0F 8D 6E 05 00 00               jge 0x14020ce8f
0020C921  C1 EA 04                        shr edx, 4
0020C924  0F B6 C2                        movzx eax, dl
0020C927  41 3B C0                        cmp eax, r8d
0020C92A  44 0F 4F C0                     cmovg r8d, eax
0020C92E  8B 87 58 03 00 00               mov eax, dword ptr [rdi + 0x358]
0020C934  85 C0                           test eax, eax
0020C936  75 3C                           jne 0x14020c974
0020C938  0F BE 87 C3 00 00 00            movsx eax, byte ptr [rdi + 0xc3]
0020C93F  44 3B C0                        cmp r8d, eax
0020C942  7D 0D                           jge 0x14020c951
0020C944  48 8D 54 24 48                  lea rdx, [rsp + 0x48]
0020C949  48 8B CF                        mov rcx, rdi
0020C94C  E8 27 45 01 00                  call 0x140220e78
0020C951  C6 87 1B 03 00 00 20            mov byte ptr [rdi + 0x31b], 0x20
0020C958  48 C7 47 40 00 00 00 00         mov qword ptr [rdi + 0x40], 0
0020C960  E9 10 F9 FF FF                  jmp 0x14020c275
0020C965  33 D2                           xor edx, edx
0020C967  48 8B CF                        mov rcx, rdi
0020C96A  E8 AD DE 3B 00                  call 0x1405ca81c
0020C96F  44 8B C0                        mov r8d, eax
0020C972  EB C4                           jmp 0x14020c938
0020C974  0F BD C0                        bsr eax, eax
0020C977  C7 44 24 34 00 00 00 00         mov dword ptr [rsp + 0x34], 0
0020C97F  44 3B C0                        cmp r8d, eax
0020C982  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
0020C986  44 0F 4C C0                     cmovl r8d, eax
0020C98A  EB AC                           jmp 0x14020c938
0020C98C  8B 05 26 A1 DB 00               mov eax, dword ptr [rip + 0xdba126]
0020C992  A8 40                           test al, 0x40
0020C994  0F 84 D2 F9 FF FF               je 0x14020c36c
0020C99A  E8 F1 2A 10 00                  call 0x14030f490
0020C99F  84 C0                           test al, al
0020C9A1  0F 84 C5 F9 FF FF               je 0x14020c36c
0020C9A7  8B CD                           mov ecx, ebp
0020C9A9  E8 B2 2A 10 00                  call 0x14030f460
0020C9AE  E9 BB F9 FF FF                  jmp 0x14020c36e
0020C9B3  8B 05 FF A0 DB 00               mov eax, dword ptr [rip + 0xdba0ff]
0020C9B9  A8 40                           test al, 0x40
0020C9BB  0F 84 3D FD FF FF               je 0x14020c6fe
0020C9C1  E8 CA 2A 10 00                  call 0x14030f490
0020C9C6  84 C0                           test al, al
0020C9C8  0F 84 30 FD FF FF               je 0x14020c6fe
0020C9CE  8B CE                           mov ecx, esi
0020C9D0  E8 8B 2A 10 00                  call 0x14030f460
0020C9D5  E9 26 FD FF FF                  jmp 0x14020c700
0020C9DA  8B 05 D8 A0 DB 00               mov eax, dword ptr [rip + 0xdba0d8]
0020C9E0  A8 40                           test al, 0x40
0020C9E2  0F 84 16 F9 FF FF               je 0x14020c2fe
0020C9E8  E8 A3 2A 10 00                  call 0x14030f490
0020C9ED  84 C0                           test al, al
0020C9EF  0F 84 09 F9 FF FF               je 0x14020c2fe
0020C9F5  8B CE                           mov ecx, esi
0020C9F7  E8 64 2A 10 00                  call 0x14030f460
0020C9FC  E9 FF F8 FF FF                  jmp 0x14020c300
0020CA01  C6 44 38 72 00                  mov byte ptr [rax + rdi + 0x72], 0
0020CA06  45 33 C9                        xor r9d, r9d
0020CA09  B8 01 01 00 00                  mov eax, 0x101
0020CA0E  E9 EB F6 FF FF                  jmp 0x14020c0fe
0020CA13  41 2A C4                        sub al, r12b
0020CA16  88 81 38 03 00 00               mov byte ptr [rcx + 0x338], al
0020CA1C  0F 85 B5 00 00 00               jne 0x14020cad7
0020CA22  8B 97 58 03 00 00               mov edx, dword ptr [rdi + 0x358]
0020CA28  41 8B C9                        mov ecx, r9d
0020CA2B  44 0F BB CA                     btc edx, r9d
0020CA2F  41 8B C4                        mov eax, r12d
0020CA32  D3 E0                           shl eax, cl
0020CA34  89 97 58 03 00 00               mov dword ptr [rdi + 0x358], edx
0020CA3A  3B D0                           cmp edx, eax
0020CA3C  0F 83 95 00 00 00               jae 0x14020cad7
0020CA42  80 BF C3 00 00 00 1F            cmp byte ptr [rdi + 0xc3], 0x1f
0020CA49  0F 8F 88 00 00 00               jg 0x14020cad7
0020CA4F  E8 6C 2D 2E 00                  call 0x1404ef7c0
0020CA54  85 C0                           test eax, eax
0020CA56  0F 84 8F 00 00 00               je 0x14020caeb
0020CA5C  44 0F BE 87 33 02 00 00         movsx r8d, byte ptr [rdi + 0x233]
0020CA64  45 8B D0                        mov r10d, r8d
0020CA67  45 8B C8                        mov r9d, r8d
0020CA6A  41 83 F8 10                     cmp r8d, 0x10
0020CA6E  7D 44                           jge 0x14020cab4
0020CA70  0F B6 8F 66 03 00 00            movzx ecx, byte ptr [rdi + 0x366]
0020CA77  0F B7 97 06 02 00 00            movzx edx, word ptr [rdi + 0x206]
0020CA7E  8B C2                           mov eax, edx
0020CA80  83 E0 0F                        and eax, 0xf
0020CA83  41 03 C0                        add eax, r8d
0020CA86  41 3B C1                        cmp eax, r9d
0020CA89  44 8B C0                        mov r8d, eax
0020CA8C  45 0F 4E C1                     cmovle r8d, r9d
0020CA90  33 C0                           xor eax, eax
0020CA92  84 C9                           test cl, cl
0020CA94  0F 4F C1                        cmovg eax, ecx
0020CA97  0F BE C0                        movsx eax, al
0020CA9A  44 03 C0                        add r8d, eax
0020CA9D  41 83 F8 10                     cmp r8d, 0x10
0020CAA1  0F 8D F3 03 00 00               jge 0x14020ce9a
0020CAA7  C1 EA 04                        shr edx, 4
0020CAAA  0F B6 C2                        movzx eax, dl
0020CAAD  41 3B C0                        cmp eax, r8d
0020CAB0  44 0F 4F C0                     cmovg r8d, eax
0020CAB4  8B 87 58 03 00 00               mov eax, dword ptr [rdi + 0x358]
0020CABA  85 C0                           test eax, eax
0020CABC  75 3C                           jne 0x14020cafa
0020CABE  0F BE 87 C3 00 00 00            movsx eax, byte ptr [rdi + 0xc3]
0020CAC5  44 3B C0                        cmp r8d, eax
0020CAC8  7D 0D                           jge 0x14020cad7
0020CACA  48 8D 54 24 48                  lea rdx, [rsp + 0x48]
0020CACF  48 8B CF                        mov rcx, rdi
0020CAD2  E8 A1 43 01 00                  call 0x140220e78
0020CAD7  C6 87 1B 03 00 00 20            mov byte ptr [rdi + 0x31b], 0x20
0020CADE  48 C7 47 40 00 00 00 00         mov qword ptr [rdi + 0x40], 0
0020CAE6  E9 43 F6 FF FF                  jmp 0x14020c12e
0020CAEB  33 D2                           xor edx, edx
0020CAED  48 8B CF                        mov rcx, rdi
0020CAF0  E8 27 DD 3B 00                  call 0x1405ca81c
0020CAF5  44 8B C0                        mov r8d, eax
0020CAF8  EB C4                           jmp 0x14020cabe
0020CAFA  0F BD C0                        bsr eax, eax
0020CAFD  C7 44 24 38 00 00 00 00         mov dword ptr [rsp + 0x38], 0
0020CB05  44 3B C0                        cmp r8d, eax
0020CB08  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
0020CB0C  44 0F 4C C0                     cmovl r8d, eax
0020CB10  EB AC                           jmp 0x14020cabe
0020CB12  8B 05 A0 9F DB 00               mov eax, dword ptr [rip + 0xdb9fa0]
0020CB18  A8 40                           test al, 0x40
0020CB1A  0F 84 27 F9 FF FF               je 0x14020c447
0020CB20  E8 6B 29 10 00                  call 0x14030f490
0020CB25  84 C0                           test al, al
0020CB27  0F 84 1A F9 FF FF               je 0x14020c447
0020CB2D  8B CE                           mov ecx, esi
0020CB2F  E8 2C 29 10 00                  call 0x14030f460
0020CB34  E9 10 F9 FF FF                  jmp 0x14020c449
0020CB39  4C 8B BC 24 C0 00 00 00         mov r15, qword ptr [rsp + 0xc0]
0020CB41  49 89 37                        mov qword ptr [r15], rsi
0020CB44  E9 0E F6 FF FF                  jmp 0x14020c157
0020CB49  0F B6 D0                        movzx edx, al
0020CB4C  0F B6 CB                        movzx ecx, bl
0020CB4F  E8 A8 8B 2E 00                  call 0x1404f56fc
0020CB54  E9 DE FA FF FF                  jmp 0x14020c637
0020CB59  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
0020CB62  48 8D 54 24 50                  lea rdx, [rsp + 0x50]
0020CB67  44 0F B6 C5                     movzx r8d, bpl
0020CB6B  E8 90 3C 04 00                  call 0x140250800
0020CB70  E9 C1 F3 FF FF                  jmp 0x14020bf36
0020CB75  E8 66 B0 00 00                  call 0x140217be0
0020CB7A  48 8B AE F8 38 00 00            mov rbp, qword ptr [rsi + 0x38f8]
0020CB81  44 0F B6 C0                     movzx r8d, al
0020CB85  48 85 ED                        test rbp, rbp
0020CB88  0F 84 5C 02 00 00               je 0x14020cdea
0020CB8E  48 83 7D F8 00                  cmp qword ptr [rbp - 8], 0
0020CB93  48 8B 45 00                     mov rax, qword ptr [rbp]
0020CB97  0F 85 7B 02 00 00               jne 0x14020ce18
0020CB9D  48 3B C5                        cmp rax, rbp
0020CBA0  74 5D                           je 0x14020cbff
0020CBA2  48 89 86 F8 38 00 00            mov qword ptr [rsi + 0x38f8], rax
0020CBA9  48 8B 4D 00                     mov rcx, qword ptr [rbp]
0020CBAD  48 8B 45 08                     mov rax, qword ptr [rbp + 8]
0020CBB1  48 39 69 08                     cmp qword ptr [rcx + 8], rbp
0020CBB5  0F 85 1A F4 FF FF               jne 0x14020bfd5
0020CBBB  48 39 28                        cmp qword ptr [rax], rbp
0020CBBE  0F 85 11 F4 FF FF               jne 0x14020bfd5
0020CBC4  48 89 08                        mov qword ptr [rax], rcx
0020CBC7  48 89 41 08                     mov qword ptr [rcx + 8], rax
0020CBCB  EB 39                           jmp 0x14020cc06
0020CBCD  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
0020CBD6  48 8D 54 24 48                  lea rdx, [rsp + 0x48]
0020CBDB  44 0F B6 87 86 01 00 00         movzx r8d, byte ptr [rdi + 0x186]
0020CBE3  E8 18 3C 04 00                  call 0x140250800
0020CBE8  E9 6A F5 FF FF                  jmp 0x14020c157
0020CBED  B9 01 01 00 00                  mov ecx, 0x101
0020CBF2  C6 47 72 00                     mov byte ptr [rdi + 0x72], 0
0020CBF6  8B C1                           mov eax, ecx
0020CBF8  8B F1                           mov esi, ecx
0020CBFA  E9 58 F3 FF FF                  jmp 0x14020bf57
0020CBFF  4C 89 8E F8 38 00 00            mov qword ptr [rsi + 0x38f8], r9
0020CC06  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
0020CC0A  4C 89 4D 00                     mov qword ptr [rbp], r9
0020CC0E  48 8B 40 38                     mov rax, qword ptr [rax + 0x38]
0020CC12  48 89 45 10                     mov qword ptr [rbp + 0x10], rax
0020CC16  45 84 C0                        test r8b, r8b
0020CC19  0F 85 CA 00 00 00               jne 0x14020cce9
0020CC1F  4C 8B 45 10                     mov r8, qword ptr [rbp + 0x10]
0020CC23  4C 3B 45 18                     cmp r8, qword ptr [rbp + 0x18]
0020CC27  74 5A                           je 0x14020cc83
0020CC29  48 8B 45 28                     mov rax, qword ptr [rbp + 0x28]
0020CC2D  48 8B 55 20                     mov rdx, qword ptr [rbp + 0x20]
0020CC31  48 8B 08                        mov rcx, qword ptr [rax]
0020CC34  48 85 4A 28                     test qword ptr [rdx + 0x28], rcx
0020CC38  0F 84 03 02 00 00               je 0x14020ce41
0020CC3E  E8 9D AF 00 00                  call 0x140217be0
0020CC43  48 83 7D 00 00                  cmp qword ptr [rbp], 0
0020CC48  44 0F B6 C0                     movzx r8d, al
0020CC4C  75 2C                           jne 0x14020cc7a
0020CC4E  48 8B 8E F8 38 00 00            mov rcx, qword ptr [rsi + 0x38f8]
0020CC55  48 85 C9                        test rcx, rcx
0020CC58  0F 84 CF 01 00 00               je 0x14020ce2d
0020CC5E  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
0020CC62  48 39 08                        cmp qword ptr [rax], rcx
0020CC65  0F 85 6A F3 FF FF               jne 0x14020bfd5
0020CC6B  48 89 4D 00                     mov qword ptr [rbp], rcx
0020CC6F  48 89 45 08                     mov qword ptr [rbp + 8], rax
0020CC73  48 89 28                        mov qword ptr [rax], rbp
0020CC76  48 89 69 08                     mov qword ptr [rcx + 8], rbp
0020CC7A  45 84 C0                        test r8b, r8b
0020CC7D  0F 85 F2 00 00 00               jne 0x14020cd75
0020CC83  44 0F B6 AC 24 B0 00 00 00      movzx r13d, byte ptr [rsp + 0xb0]
0020CC8C  0F B6 AC 24 A8 00 00 00         movzx ebp, byte ptr [rsp + 0xa8]
0020CC94  E9 2D F1 FF FF                  jmp 0x14020bdc6
0020CC99  48 8B 87 E8 00 00 00            mov rax, qword ptr [rdi + 0xe8]
0020CCA0  48 85 C0                        test rax, rax
0020CCA3  74 2F                           je 0x14020ccd4
0020CCA5  48 8D 87 08 02 00 00            lea rax, [rdi + 0x208]
0020CCAC  48 8B 10                        mov rdx, qword ptr [rax]
0020CCAF  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
0020CCB3  48 39 42 08                     cmp qword ptr [rdx + 8], rax
0020CCB7  0F 85 18 F3 FF FF               jne 0x14020bfd5
0020CCBD  48 39 01                        cmp qword ptr [rcx], rax
0020CCC0  0F 85 0F F3 FF FF               jne 0x14020bfd5
0020CCC6  48 89 11                        mov qword ptr [rcx], rdx
0020CCC9  48 89 4A 08                     mov qword ptr [rdx + 8], rcx
0020CCCD  4C 89 8F E8 00 00 00            mov qword ptr [rdi + 0xe8], r9
0020CCD4  F0 41 81 26 7F FF FF FF         lock and dword ptr [r14], 0xffffff7f
0020CCDC  B9 80 00 00 00                  mov ecx, 0x80
0020CCE1  49 89 0F                        mov qword ptr [r15], rcx
0020CCE4  E9 84 FB FF FF                  jmp 0x14020c86d
0020CCE9  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
0020CCF2  4C 8B 81 B8 8E 00 00            mov r8, qword ptr [rcx + 0x8eb8]
0020CCF9  4D 85 C0                        test r8, r8
0020CCFC  75 56                           jne 0x14020cd54
0020CCFE  FB                              sti
0020CCFF  E9 1B FF FF FF                  jmp 0x14020cc1f
0020CD04  C6 47 72 00                     mov byte ptr [rdi + 0x72], 0
0020CD08  B8 01 01 00 00                  mov eax, 0x101
0020CD0D  E9 EC F3 FF FF                  jmp 0x14020c0fe
0020CD12  83 BE E0 38 00 00 00            cmp dword ptr [rsi + 0x38e0], 0
0020CD19  0F 85 B4 F0 FF FF               jne 0x14020bdd3
0020CD1F  E8 BC AE 00 00                  call 0x140217be0
0020CD24  80 BE E5 38 00 00 00            cmp byte ptr [rsi + 0x38e5], 0
0020CD2B  0F 85 32 01 00 00               jne 0x14020ce63
0020CD31  84 C0                           test al, al
0020CD33  0F 84 9A F0 FF FF               je 0x14020bdd3
0020CD39  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
0020CD42  4C 8B 81 B8 8E 00 00            mov r8, qword ptr [rcx + 0x8eb8]
0020CD49  4D 85 C0                        test r8, r8
0020CD4C  75 74                           jne 0x14020cdc2
0020CD4E  FB                              sti
0020CD4F  E9 7F F0 FF FF                  jmp 0x14020bdd3
0020CD54  41 0F 0D 08                     prefetchw byte ptr [r8]
0020CD58  41 8B 00                        mov eax, dword ptr [r8]
0020CD5B  8B D0                           mov edx, eax
0020CD5D  0F BA F2 15                     btr edx, 0x15
0020CD61  F0 41 0F B1 10                  lock cmpxchg dword ptr [r8], edx
0020CD66  75 F3                           jne 0x14020cd5b
0020CD68  0F BA E0 15                     bt eax, 0x15
0020CD6C  73 90                           jae 0x14020ccfe
0020CD6E  E8 5D 64 05 00                  call 0x1402631d0
0020CD73  EB 89                           jmp 0x14020ccfe
0020CD75  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
0020CD7E  4C 8B 81 B8 8E 00 00            mov r8, qword ptr [rcx + 0x8eb8]
0020CD85  4D 85 C0                        test r8, r8
0020CD88  75 17                           jne 0x14020cda1
0020CD8A  FB                              sti
0020CD8B  44 0F B6 AC 24 B0 00 00 00      movzx r13d, byte ptr [rsp + 0xb0]
0020CD94  0F B6 AC 24 A8 00 00 00         movzx ebp, byte ptr [rsp + 0xa8]
0020CD9C  E9 25 F0 FF FF                  jmp 0x14020bdc6
0020CDA1  41 0F 0D 08                     prefetchw byte ptr [r8]
0020CDA5  41 8B 00                        mov eax, dword ptr [r8]
0020CDA8  8B D0                           mov edx, eax
0020CDAA  0F BA F2 15                     btr edx, 0x15
0020CDAE  F0 41 0F B1 10                  lock cmpxchg dword ptr [r8], edx
0020CDB3  75 F3                           jne 0x14020cda8
0020CDB5  0F BA E0 15                     bt eax, 0x15
0020CDB9  73 CF                           jae 0x14020cd8a
0020CDBB  E8 10 64 05 00                  call 0x1402631d0
0020CDC0  EB C8                           jmp 0x14020cd8a
0020CDC2  41 0F 0D 08                     prefetchw byte ptr [r8]
0020CDC6  41 8B 00                        mov eax, dword ptr [r8]
0020CDC9  8B D0                           mov edx, eax
0020CDCB  0F BA F2 15                     btr edx, 0x15
0020CDCF  F0 41 0F B1 10                  lock cmpxchg dword ptr [r8], edx
0020CDD4  75 F3                           jne 0x14020cdc9
0020CDD6  0F BA E0 15                     bt eax, 0x15
0020CDDA  0F 83 6E FF FF FF               jae 0x14020cd4e
0020CDE0  E8 EB 63 05 00                  call 0x1402631d0
0020CDE5  E9 64 FF FF FF                  jmp 0x14020cd4e
0020CDEA  45 84 C0                        test r8b, r8b
0020CDED  0F 84 99 FE FF FF               je 0x14020cc8c
0020CDF3  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
0020CDFC  4C 8B 81 B8 8E 00 00            mov r8, qword ptr [rcx + 0x8eb8]
0020CE03  4D 85 C0                        test r8, r8
0020CE06  0F 84 F8 98 4C 00               je 0x1406d6704
0020CE0C  41 0F 0D 08                     prefetchw byte ptr [r8]
0020CE10  41 8B 00                        mov eax, dword ptr [r8]
0020CE13  E9 D4 98 4C 00                  jmp 0x1406d66ec
0020CE18  48 3B E8                        cmp rbp, rax
0020CE1B  0F 84 F5 FD FF FF               je 0x14020cc16
0020CE21  48 89 86 F8 38 00 00            mov qword ptr [rsi + 0x38f8], rax
0020CE28  E9 E9 FD FF FF                  jmp 0x14020cc16
0020CE2D  48 89 6D 08                     mov qword ptr [rbp + 8], rbp
0020CE31  48 89 6D 00                     mov qword ptr [rbp], rbp
0020CE35  48 89 AE F8 38 00 00            mov qword ptr [rsi + 0x38f8], rbp
0020CE3C  E9 39 FE FF FF                  jmp 0x14020cc7a
0020CE41  49 8B D0                        mov rdx, r8
0020CE44  48 8D 4D F8                     lea rcx, [rbp - 8]
0020CE48  E8 BB 5D 3B 00                  call 0x1405c2c08
0020CE4D  85 C0                           test eax, eax
0020CE4F  0F 84 2E FE FF FF               je 0x14020cc83
0020CE55  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
0020CE59  E8 56 54 3B 00                  call 0x1405c22b4
0020CE5E  E9 20 FE FF FF                  jmp 0x14020cc83
0020CE63  83 BE E0 38 00 00 00            cmp dword ptr [rsi + 0x38e0], 0
0020CE6A  0F 85 C1 FE FF FF               jne 0x14020cd31
0020CE70  C6 86 E5 38 00 00 00            mov byte ptr [rsi + 0x38e5], 0
0020CE77  F0 83 0C 24 00                  lock or dword ptr [rsp], 0
0020CE7C  48 8B 0D 65 42 D1 00            mov rcx, qword ptr [rip + 0xd14265]
0020CE83  48 89 8E E8 38 00 00            mov qword ptr [rsi + 0x38e8], rcx
0020CE8A  E9 A2 FE FF FF                  jmp 0x14020cd31
0020CE8F  41 B8 0F 00 00 00               mov r8d, 0xf
0020CE95  E9 87 FA FF FF                  jmp 0x14020c921
0020CE9A  41 B8 0F 00 00 00               mov r8d, 0xf
0020CEA0  E9 02 FC FF FF                  jmp 0x14020caa7
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0020C2D4(__int64 a1, __int64 a2, __int64 a3, int a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, __int64 a12, __int64 a13, __int64 a14, __int64 a15, __int64 a16, __int64 a17, __int64 a18, __int64 a19, __int64 a20, __int64 a21, __int64 a22, __int64 a23, __int64 a24)
{
    unsigned int v_stack_p0;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned int v_stack_p30;
    unsigned int v_stack_p34;
    unsigned int v_stack_p38;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int8 v_stack_pA8;
    unsigned __int8 v_stack_pB0;
    unsigned __int64 v_stack_pC0;

    *(unsigned __int64 *)(a24) = 128;
}
```

## 5. (Beta) C Style

```c
int64_t sub_0020C2D4(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, uint64_t Arg8, uint64_t Arg9, uint64_t Arg10, uint64_t Arg11, uint64_t Arg12, uint64_t Arg13, uint64_t Arg14, uint64_t Arg15, uint64_t Arg16, uint64_t Arg17, uint64_t Arg18, uint64_t Arg19, uint64_t Arg20, uint64_t Arg21, uint64_t Arg22, uint64_t Arg23, void *Arg24)
{
    uint8_t *arg24 = (uint8_t *)Arg24;

    uint32_t v_stack_p0;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint32_t v_stack_p30;
    uint32_t v_stack_p34;
    uint32_t v_stack_p38;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint8_t v_stack_pA8;
    uint8_t v_stack_pB0;
    uint64_t v_stack_pC0;

    *(uint64_t *)(arg24) = 128;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg24` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0020C2D4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
