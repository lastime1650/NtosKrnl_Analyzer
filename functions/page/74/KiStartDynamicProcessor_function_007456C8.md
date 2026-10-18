# KiStartDynamicProcessor

- RVA: `0x007456C8`–`0x00745D32` (길이 `1,642` bytes)
- VA: `0x00000001407456C8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C9DFC`
- 디코드: `408`개 명령, `1,642/1,642` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **60**; 고유 호출 대상: **54**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **12**

### Outgoing calls
- `0x00745720` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00745731` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00745745` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0074575E` → [KiInitializeProcessorStateInitializationParameters](../../text/5B/KiInitializeProcessorStateInitializationParameters_function_005B834C.md) (function, `0x005B834C`)
- `0x0074579F` → [HalRegisterDynamicProcessor](../../text/54/HalRegisterDynamicProcessor_function_00545E10.md) (function, `0x00545E10`)
- `0x007457C1` → [KiQueryProcessorNode](../../text/5B/KiQueryProcessorNode_function_005BCC70.md) (function, `0x005BCC70`)
- `0x007457EF` → [KiComputeProcessorDataSize](../../pagelk/B6/KiComputeProcessorDataSize_function_00B6B1A8.md) (function, `0x00B6B1A8`)
- `0x00745820` → [KiAllocateProcessorStateInitializationParameters](../../text/5B/KiAllocateProcessorStateInitializationParameters_function_005B6F24.md) (function, `0x005B6F24`)
- `0x00745837` → [ExCreatePoolTagTable](../7C/ExCreatePoolTagTable_function_007C76FC.md) (function, `0x007C76FC`)
- `0x00745886` → [KiInitializeProcessorState](KiInitializeProcessorState_function_00747390.md) (function, `0x00747390`)
- `0x007458A9` → [MmInitializeProcessor](../../pagelk/B7/MmInitializeProcessor_function_00B737F8.md) (function, `0x00B737F8`)
- `0x007458C4` → [KiInitializePrcbContext](../../pagelk/B6/KiInitializePrcbContext_function_00B66D70.md) (function, `0x00B66D70`)
- `0x007458D6` → [KeInitializeTimerTable](../A9/KeInitializeTimerTable_function_00A9471C.md) (function, `0x00A9471C`)
- `0x007458EA` → [ExInitializeProcessor](../../text/65/ExInitializeProcessor_function_00655844.md) (function, `0x00655844`)
- `0x007458FC` → [ObInitializeProcessor](ObInitializeProcessor_function_0074DA98.md) (function, `0x0074DA98`)
- `0x00745910` → [IoInitializeProcessor](../71/IoInitializeProcessor_function_0071A91C.md) (function, `0x0071A91C`)
- `0x00745922` → [CcInitializeProcessor](../71/CcInitializeProcessor_function_00710220.md) (function, `0x00710220`)
- `0x00745934` → [EtwInitializeProcessor](../7B/EtwInitializeProcessor_function_007B4EBC.md) (function, `0x007B4EBC`)
- `0x0074594D` → [EtwpInitializeActivityIdSeed](../7B/EtwpInitializeActivityIdSeed_function_007B69A4.md) (function, `0x007B69A4`)
- `0x00745957` → [WheaInitializeProcessor](../../pagelk/B7/WheaInitializeProcessor_function_00B732E4.md) (function, `0x00B732E4`)
- `0x00745971` → [HvlInitializeProcessor](../71/HvlInitializeProcessor_function_0071804C.md) (function, `0x0071804C`)
- `0x00745983` → [KiAllocatePrcbThreads](../../text/5B/KiAllocatePrcbThreads_function_005B6C2C.md) (function, `0x005B6C2C`)
- `0x00745995` → [KiAllocateLocalSharedReadyQueue](../../text/5B/KiAllocateLocalSharedReadyQueue_function_005B6BB0.md) (function, `0x005B6BB0`)
- `0x007459A7` → [KiAllocateStaticRescheduleContext](../../text/5B/KiAllocateStaticRescheduleContext_function_005B6F98.md) (function, `0x005B6F98`)
- `0x007459B9` → [KiAllocateIdleSearchStructures](../../text/5B/KiAllocateIdleSearchStructures_function_005B6A04.md) (function, `0x005B6A04`)
- `0x007459CB` → [KiInitializeThreadCycleTable](../../pagelk/B6/KiInitializeThreadCycleTable_function_00B66B10.md) (function, `0x00B66B10`)
- `0x007459DD` → [CmInitializeProcessorCallbacks](../7E/CmInitializeProcessorCallbacks_function_007E143C.md) (function, `0x007E143C`)
- `0x007459EF` → [KiAllocateForceParkingData](../../text/5C/KiAllocateForceParkingData_function_005C96C8.md) (function, `0x005C96C8`)
- `0x00745A01` → [VmInitializeProcessor](../../pagelk/B7/VmInitializeProcessor_function_00B7E858.md) (function, `0x00B7E858`)
- `0x00745A13` → [KiInitializeSingleDpcRuntimeHistoryHashTable](KiInitializeSingleDpcRuntimeHistoryHashTable_function_00747808.md) (function, `0x00747808`)
- `0x00745A33` → [KiAllocateProcessorHiberSwapShadowStacks](../../text/5B/KiAllocateProcessorHiberSwapShadowStacks_function_005BD754.md) (function, `0x005BD754`)
- `0x00745A5A` → [MmLockPagableSectionByHandle](../A4/MmLockPagableSectionByHandle_function_00A4D1E0.md) (function, `0x00A4D1E0`)
- `0x00745A62` → [KiAddProcessorToGroupSchedulingDatabase](../../pagelk/B6/KiAddProcessorToGroupSchedulingDatabase_function_00B6B1D8.md) (function, `0x00B6B1D8`)
- `0x00745AB5` → [KiDynamicProcessorAddNotification](../../text/5B/KiDynamicProcessorAddNotification_function_005BD928.md) (function, `0x005BD928`)
- `0x00745ACD` → [KiRcuProcessorInitialize](../../text/4D/KiRcuProcessorInitialize_function_004DF7E8.md) (function, `0x004DF7E8`)
- `0x00745AE7` → [HalStartDynamicProcessor](../../text/54/HalStartDynamicProcessor_function_00543300.md) (function, `0x00543300`)
- `0x00745B0D` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00745B3E` → [KiDynamicProcessorAddNotification](../../text/5B/KiDynamicProcessorAddNotification_function_005BD928.md) (function, `0x005BD928`)
- `0x00745B51` → [WheaInitializeProcessor](../../pagelk/B7/WheaInitializeProcessor_function_00B732E4.md) (function, `0x00B732E4`)
- `0x00745B59` → [CmInitializeProcessor](../7E/CmInitializeProcessor_function_007E4BAC.md) (function, `0x007E4BAC`)
- `0x00745B61` → [KiDynamicProcessorInitialization](../../text/5B/KiDynamicProcessorInitialization_function_005B7C6C.md) (function, `0x005B7C6C`)
- `0x00745B74` → [MmUnlockPagableImageSection](../../text/2A/MmUnlockPagableImageSection_function_002A39F0.md) (function, `0x002A39F0`)
- `0x00745B99` → [KiInitializeDynamicProcessor](../../pagelk/B6/KiInitializeDynamicProcessor_function_00B679C8.md) (function, `0x00B679C8`)
- `0x00745C53` → [KiRcuProcessorInitialize](../../text/4D/KiRcuProcessorInitialize_function_004DF7E8.md) (function, `0x004DF7E8`)
- `0x00745C5B` → [KiFreeForceParkingData](../../text/5C/KiFreeForceParkingData_function_005C99B8.md) (function, `0x005C99B8`)
- `0x00745C6E` → [KiAllocateProcessorHiberSwapShadowStacks](../../text/5B/KiAllocateProcessorHiberSwapShadowStacks_function_005BD754.md) (function, `0x005BD754`)
- `0x00745C76` → [KiFreeIdleSearchStructures](../../text/5B/KiFreeIdleSearchStructures_function_005B7E88.md) (function, `0x005B7E88`)
- `0x00745C7E` → [KiFreeStaticRescheduleContext](../../text/5B/KiFreeStaticRescheduleContext_function_005B8120.md) (function, `0x005B8120`)
- `0x00745C86` → [KiFreeLocalSharedReadyQueue](../../text/5B/KiFreeLocalSharedReadyQueue_function_005B7F0C.md) (function, `0x005B7F0C`)
- `0x00745C8E` → [KiFreePrcbThreads](../../text/5B/KiFreePrcbThreads_function_005B7F40.md) (function, `0x005B7F40`)
- `0x00745C96` → [KiFreeThreadCycleTable](../../pagelk/B6/KiFreeThreadCycleTable_function_00B66610.md) (function, `0x00B66610`)
- `0x00745C9E` → [HvlDeleteProcessor](../71/HvlDeleteProcessor_function_00717FA4.md) (function, `0x00717FA4`)
- `0x00745CA6` → [MmDeleteProcessor](../7F/MmDeleteProcessor_function_007F8FB4.md) (function, `0x007F8FB4`)
- `0x00745CAE` → [EtwDeleteProcessor](../7B/EtwDeleteProcessor_function_007B4CC0.md) (function, `0x007B4CC0`)
- `0x00745CC1` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00745CD0` → [KiUnassignProcessorNumberFromPrcb](../../text/5B/KiUnassignProcessorNumberFromPrcb_function_005BCEC8.md) (function, `0x005BCEC8`)
- `0x00745CDD` → [ExDeletePoolTagTable](../../text/65/ExDeletePoolTagTable_function_00655F88.md) (function, `0x00655F88`)
- `0x00745CF6` → [KiUnshadowProcessorAllocation](../../pagelk/B6/KiUnshadowProcessorAllocation_function_00B6B0E8.md) (function, `0x00B6B0E8`)
- `0x00745D00` → [KiFreeProcessorStateInitializationParameters](../../text/5B/KiFreeProcessorStateInitializationParameters_function_005B80A8.md) (function, `0x005B80A8`)
- `0x00745D11` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [KeStartDynamicProcessor](KeStartDynamicProcessor_function_00746730.md) at `0x00746794`

### Static image references
- `0x007456E7` → RVA `0x00E0A740` (`.data`; read)
- `0x00745763` → RVA `0x00FC6A80` (`ALMOSTRO`; read)
- `0x00745769` → RVA `0x00FCF6C0` (`CACHEALI`; read)
- `0x0074577B` → RVA `0x00FC6C94` (`ALMOSTRO`; read)
- `0x00745799` → RVA `0x00FC6C68` (`ALMOSTRO`; read)
- `0x007457D3` → RVA `0x00FC6AE8` (`ALMOSTRO`; read)
- `0x0074584E` → RVA `0x00FC6C50` (`ALMOSTRO`; write)
- `0x00745866` → RVA `0x00EF54C0` (`.data`; read)
- `0x00745A22` → RVA `0x00F230E4` (`.data`; read)
- `0x00745A42` → RVA `0x00FC6C00` (`ALMOSTRO`; read)
- `0x00745A67` → RVA `0x00FC6B20` (`ALMOSTRO`; read)
- `0x00745A88` → RVA `0x00FC6B20` (`ALMOSTRO`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **44**
  - `0x00745720` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00745731` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00745745` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x0074575E` → [KiInitializeProcessorStateInitializationParameters](../../text/5B/KiInitializeProcessorStateInitializationParameters_function_005B834C.md) (`PAGE` → `.text`)
  - `0x0074579F` → [HalRegisterDynamicProcessor](../../text/54/HalRegisterDynamicProcessor_function_00545E10.md) (`PAGE` → `.text`)
  - `0x007457C1` → [KiQueryProcessorNode](../../text/5B/KiQueryProcessorNode_function_005BCC70.md) (`PAGE` → `.text`)
  - `0x007457EF` → [KiComputeProcessorDataSize](../../pagelk/B6/KiComputeProcessorDataSize_function_00B6B1A8.md) (`PAGE` → `PAGELK`)
  - `0x00745820` → [KiAllocateProcessorStateInitializationParameters](../../text/5B/KiAllocateProcessorStateInitializationParameters_function_005B6F24.md) (`PAGE` → `.text`)
  - `0x007458A9` → [MmInitializeProcessor](../../pagelk/B7/MmInitializeProcessor_function_00B737F8.md) (`PAGE` → `PAGELK`)
  - `0x007458C4` → [KiInitializePrcbContext](../../pagelk/B6/KiInitializePrcbContext_function_00B66D70.md) (`PAGE` → `PAGELK`)
  - `0x007458EA` → [ExInitializeProcessor](../../text/65/ExInitializeProcessor_function_00655844.md) (`PAGE` → `.text`)
  - `0x00745957` → [WheaInitializeProcessor](../../pagelk/B7/WheaInitializeProcessor_function_00B732E4.md) (`PAGE` → `PAGELK`)
  - `0x00745983` → [KiAllocatePrcbThreads](../../text/5B/KiAllocatePrcbThreads_function_005B6C2C.md) (`PAGE` → `.text`)
  - `0x00745995` → [KiAllocateLocalSharedReadyQueue](../../text/5B/KiAllocateLocalSharedReadyQueue_function_005B6BB0.md) (`PAGE` → `.text`)
  - `0x007459A7` → [KiAllocateStaticRescheduleContext](../../text/5B/KiAllocateStaticRescheduleContext_function_005B6F98.md) (`PAGE` → `.text`)
  - `0x007459B9` → [KiAllocateIdleSearchStructures](../../text/5B/KiAllocateIdleSearchStructures_function_005B6A04.md) (`PAGE` → `.text`)
  - `0x007459CB` → [KiInitializeThreadCycleTable](../../pagelk/B6/KiInitializeThreadCycleTable_function_00B66B10.md) (`PAGE` → `PAGELK`)
  - `0x007459EF` → [KiAllocateForceParkingData](../../text/5C/KiAllocateForceParkingData_function_005C96C8.md) (`PAGE` → `.text`)
  - `0x00745A01` → [VmInitializeProcessor](../../pagelk/B7/VmInitializeProcessor_function_00B7E858.md) (`PAGE` → `PAGELK`)
  - `0x00745A33` → [KiAllocateProcessorHiberSwapShadowStacks](../../text/5B/KiAllocateProcessorHiberSwapShadowStacks_function_005BD754.md) (`PAGE` → `.text`)
  - `0x00745A62` → [KiAddProcessorToGroupSchedulingDatabase](../../pagelk/B6/KiAddProcessorToGroupSchedulingDatabase_function_00B6B1D8.md) (`PAGE` → `PAGELK`)
  - `0x00745AB5` → [KiDynamicProcessorAddNotification](../../text/5B/KiDynamicProcessorAddNotification_function_005BD928.md) (`PAGE` → `.text`)
  - `0x00745ACD` → [KiRcuProcessorInitialize](../../text/4D/KiRcuProcessorInitialize_function_004DF7E8.md) (`PAGE` → `.text`)
  - `0x00745AE7` → [HalStartDynamicProcessor](../../text/54/HalStartDynamicProcessor_function_00543300.md) (`PAGE` → `.text`)
  - `0x00745B0D` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x00745B3E` → [KiDynamicProcessorAddNotification](../../text/5B/KiDynamicProcessorAddNotification_function_005BD928.md) (`PAGE` → `.text`)
  - `0x00745B51` → [WheaInitializeProcessor](../../pagelk/B7/WheaInitializeProcessor_function_00B732E4.md) (`PAGE` → `PAGELK`)
  - `0x00745B61` → [KiDynamicProcessorInitialization](../../text/5B/KiDynamicProcessorInitialization_function_005B7C6C.md) (`PAGE` → `.text`)
  - `0x00745B74` → [MmUnlockPagableImageSection](../../text/2A/MmUnlockPagableImageSection_function_002A39F0.md) (`PAGE` → `.text`)
  - `0x00745B99` → [KiInitializeDynamicProcessor](../../pagelk/B6/KiInitializeDynamicProcessor_function_00B679C8.md) (`PAGE` → `PAGELK`)
  - `0x00745C53` → [KiRcuProcessorInitialize](../../text/4D/KiRcuProcessorInitialize_function_004DF7E8.md) (`PAGE` → `.text`)
  - `0x00745C5B` → [KiFreeForceParkingData](../../text/5C/KiFreeForceParkingData_function_005C99B8.md) (`PAGE` → `.text`)
  - `0x00745C6E` → [KiAllocateProcessorHiberSwapShadowStacks](../../text/5B/KiAllocateProcessorHiberSwapShadowStacks_function_005BD754.md) (`PAGE` → `.text`)
  - `0x00745C76` → [KiFreeIdleSearchStructures](../../text/5B/KiFreeIdleSearchStructures_function_005B7E88.md) (`PAGE` → `.text`)
  - `0x00745C7E` → [KiFreeStaticRescheduleContext](../../text/5B/KiFreeStaticRescheduleContext_function_005B8120.md) (`PAGE` → `.text`)
  - `0x00745C86` → [KiFreeLocalSharedReadyQueue](../../text/5B/KiFreeLocalSharedReadyQueue_function_005B7F0C.md) (`PAGE` → `.text`)
  - `0x00745C8E` → [KiFreePrcbThreads](../../text/5B/KiFreePrcbThreads_function_005B7F40.md) (`PAGE` → `.text`)
  - `0x00745C96` → [KiFreeThreadCycleTable](../../pagelk/B6/KiFreeThreadCycleTable_function_00B66610.md) (`PAGE` → `PAGELK`)
  - `0x00745CC1` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00745CD0` → [KiUnassignProcessorNumberFromPrcb](../../text/5B/KiUnassignProcessorNumberFromPrcb_function_005BCEC8.md) (`PAGE` → `.text`)
  - `0x00745CDD` → [ExDeletePoolTagTable](../../text/65/ExDeletePoolTagTable_function_00655F88.md) (`PAGE` → `.text`)
  - `0x00745CF6` → [KiUnshadowProcessorAllocation](../../pagelk/B6/KiUnshadowProcessorAllocation_function_00B6B0E8.md) (`PAGE` → `PAGELK`)
  - `0x00745D00` → [KiFreeProcessorStateInitializationParameters](../../text/5B/KiFreeProcessorStateInitializationParameters_function_005B80A8.md) (`PAGE` → `.text`)
  - `0x00745D11` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007456C8  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
007456CD  55                              push rbp
007456CE  56                              push rsi
007456CF  57                              push rdi
007456D0  41 54                           push r12
007456D2  41 55                           push r13
007456D4  41 56                           push r14
007456D6  41 57                           push r15
007456D8  48 8D AC 24 80 F8 FF FF         lea rbp, [rsp - 0x780]
007456E0  48 81 EC 80 08 00 00            sub rsp, 0x880
007456E7  48 8B 05 52 50 6C 00            mov rax, qword ptr [rip + 0x6c5052]
007456EE  48 33 C4                        xor rax, rsp
007456F1  48 89 85 70 07 00 00            mov qword ptr [rbp + 0x770], rax
007456F8  45 0F B7 F8                     movzx r15d, r8w
007456FC  89 54 24 38                     mov dword ptr [rsp + 0x38], edx
00745700  33 DB                           xor ebx, ebx
00745702  45 8B F1                        mov r14d, r9d
00745705  33 C0                           xor eax, eax
00745707  89 5C 24 40                     mov dword ptr [rsp + 0x40], ebx
0074570B  33 D2                           xor edx, edx
0074570D  89 5C 24 44                     mov dword ptr [rsp + 0x44], ebx
00745711  41 B8 E4 00 00 00               mov r8d, 0xe4
00745717  89 44 24 54                     mov dword ptr [rsp + 0x54], eax
0074571B  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
00745720  E8 1B 15 F8 FF                  call 0x1406c6c40
00745725  33 D2                           xor edx, edx
00745727  48 8D 4D 40                     lea rcx, [rbp + 0x40]
0074572B  41 B8 70 01 00 00               mov r8d, 0x170
00745731  E8 0A 15 F8 FF                  call 0x1406c6c40
00745736  33 D2                           xor edx, edx
00745738  48 8D 8D B0 01 00 00            lea rcx, [rbp + 0x1b0]
0074573F  41 B8 C0 05 00 00               mov r8d, 0x5c0
00745745  E8 F6 14 F8 FF                  call 0x1406c6c40
0074574A  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
0074574F  66 89 5C 24 30                  mov word ptr [rsp + 0x30], bx
00745754  44 8B E3                        mov r12d, ebx
00745757  44 8B EB                        mov r13d, ebx
0074575A  8B F3                           mov esi, ebx
0074575C  8B FB                           mov edi, ebx
0074575E  E8 E9 2B E7 FF                  call 0x1405b834c
00745763  8B 05 17 13 88 00               mov eax, dword ptr [rip + 0x881317]
00745769  4C 8D 05 50 9F 88 00            lea r8, [rip + 0x889f50]
00745770  3D 00 08 00 00                  cmp eax, 0x800
00745775  0F 83 2E 04 00 00               jae 0x140745ba9
0074577B  39 1D 13 15 88 00               cmp dword ptr [rip + 0x881513], ebx
00745781  74 12                           je 0x140745795
00745783  8B 05 F7 12 88 00               mov eax, dword ptr [rip + 0x8812f7]
00745789  3B 05 05 15 88 00               cmp eax, dword ptr [rip + 0x881505]
0074578F  0F 83 14 04 00 00               jae 0x140745ba9
00745795  8B 54 24 38                     mov edx, dword ptr [rsp + 0x38]
00745799  8B 0D C9 14 88 00               mov ecx, dword ptr [rip + 0x8814c9]
0074579F  E8 6C 06 E0 FF                  call 0x140545e10
007457A4  8B D8                           mov ebx, eax
007457A6  85 C0                           test eax, eax
007457A8  0F 88 05 04 00 00               js 0x140745bb3
007457AE  4C 8D 44 24 30                  lea r8, [rsp + 0x30]
007457B3  66 44 89 7C 24 30               mov word ptr [rsp + 0x30], r15w
007457B9  48 8D 54 24 38                  lea rdx, [rsp + 0x38]
007457BE  41 8B CE                        mov ecx, r14d
007457C1  E8 AA 74 E7 FF                  call 0x1405bcc70
007457C6  45 33 FF                        xor r15d, r15d
007457C9  8B D8                           mov ebx, eax
007457CB  85 C0                           test eax, eax
007457CD  0F 85 AB 03 00 00               jne 0x140745b7e
007457D3  44 8B 0D 0E 13 88 00            mov r9d, dword ptr [rip + 0x88130e]
007457DA  4C 8D 44 24 44                  lea r8, [rsp + 0x44]
007457DF  41 8B C9                        mov ecx, r9d
007457E2  C7 44 24 50 01 00 00 00         mov dword ptr [rsp + 0x50], 1
007457EA  48 8D 54 24 40                  lea rdx, [rsp + 0x40]
007457EF  E8 B4 59 42 00                  call 0x140b6b1a8
007457F4  0F B7 54 24 30                  movzx edx, word ptr [rsp + 0x30]
007457F9  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
007457FE  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
00745802  8B 44 24 40                     mov eax, dword ptr [rsp + 0x40]
00745806  89 44 24 74                     mov dword ptr [rsp + 0x74], eax
0074580A  8B 44 24 44                     mov eax, dword ptr [rsp + 0x44]
0074580E  89 44 24 78                     mov dword ptr [rsp + 0x78], eax
00745812  89 54 24 64                     mov dword ptr [rsp + 0x64], edx
00745816  44 89 74 24 68                  mov dword ptr [rsp + 0x68], r14d
0074581B  44 89 4C 24 6C                  mov dword ptr [rsp + 0x6c], r9d
00745820  E8 FF 16 E7 FF                  call 0x1405b6f24
00745825  8B D8                           mov ebx, eax
00745827  85 C0                           test eax, eax
00745829  0F 88 87 03 00 00               js 0x140745bb6
0074582F  0F B7 54 24 30                  movzx edx, word ptr [rsp + 0x30]
00745834  41 8B CE                        mov ecx, r14d
00745837  E8 C0 1E 08 00                  call 0x1407c76fc
0074583C  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00745841  4C 8B E0                        mov r12, rax
00745844  48 85 C0                        test rax, rax
00745847  75 11                           jne 0x14074585a
00745849  BB 9A 00 00 C0                  mov ebx, 0xc000009a
0074584E  44 89 3D FB 13 88 00            mov dword ptr [rip + 0x8813fb], r15d
00745855  E9 A1 04 00 00                  jmp 0x140745cfb
0074585A  0F B7 44 24 30                  movzx eax, word ptr [rsp + 0x30]
0074585F  48 8D 1D 5A 9E 88 00            lea rbx, [rip + 0x889e5a]
00745866  0F 10 05 53 FC 7A 00            movups xmm0, xmmword ptr [rip + 0x7afc53]
0074586D  4C 8D 44 24 50                  lea r8, [rsp + 0x50]
00745872  48 8D 55 40                     lea rdx, [rbp + 0x40]
00745876  4C 8B 2C C3                     mov r13, qword ptr [rbx + rax*8]
0074587A  48 8D 8D B0 01 00 00            lea rcx, [rbp + 0x1b0]
00745881  F3 0F 7F 45 50                  movdqu xmmword ptr [rbp + 0x50], xmm0
00745886  E8 05 1B 00 00                  call 0x140747390
0074588B  48 8B F8                        mov rdi, rax
0074588E  48 85 C0                        test rax, rax
00745891  75 0A                           jne 0x14074589d
00745893  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00745898  E9 19 03 00 00                  jmp 0x140745bb6
0074589D  0F B7 44 24 30                  movzx eax, word ptr [rsp + 0x30]
007458A2  48 8B CF                        mov rcx, rdi
007458A5  48 8B 34 C3                     mov rsi, qword ptr [rbx + rax*8]
007458A9  E8 4A DF 42 00                  call 0x140b737f8
007458AE  85 C0                           test eax, eax
007458B0  75 0A                           jne 0x1407458bc
007458B2  BB 01 00 00 C0                  mov ebx, 0xc0000001
007458B7  E9 FA 02 00 00                  jmp 0x140745bb6
007458BC  0F B7 54 24 30                  movzx edx, word ptr [rsp + 0x30]
007458C1  48 8B CF                        mov rcx, rdi
007458C4  E8 A7 14 42 00                  call 0x140b66d70
007458C9  8B D8                           mov ebx, eax
007458CB  85 C0                           test eax, eax
007458CD  0F 88 E3 02 00 00               js 0x140745bb6
007458D3  48 8B CF                        mov rcx, rdi
007458D6  E8 41 EE 34 00                  call 0x140a9471c
007458DB  8B D8                           mov ebx, eax
007458DD  85 C0                           test eax, eax
007458DF  0F 88 D1 02 00 00               js 0x140745bb6
007458E5  B2 01                           mov dl, 1
007458E7  48 8B CF                        mov rcx, rdi
007458EA  E8 55 FF F0 FF                  call 0x140655844
007458EF  8B D8                           mov ebx, eax
007458F1  85 C0                           test eax, eax
007458F3  0F 88 BD 02 00 00               js 0x140745bb6
007458F9  48 8B CF                        mov rcx, rdi
007458FC  E8 97 81 00 00                  call 0x14074da98
00745901  8B D8                           mov ebx, eax
00745903  85 C0                           test eax, eax
00745905  0F 88 AB 02 00 00               js 0x140745bb6
0074590B  33 D2                           xor edx, edx
0074590D  48 8B CF                        mov rcx, rdi
00745910  E8 07 50 FD FF                  call 0x14071a91c
00745915  8B D8                           mov ebx, eax
00745917  85 C0                           test eax, eax
00745919  0F 88 97 02 00 00               js 0x140745bb6
0074591F  48 8B CF                        mov rcx, rdi
00745922  E8 F9 A8 FC FF                  call 0x140710220
00745927  8B D8                           mov ebx, eax
00745929  85 C0                           test eax, eax
0074592B  0F 88 85 02 00 00               js 0x140745bb6
00745931  48 8B CF                        mov rcx, rdi
00745934  E8 83 F5 06 00                  call 0x1407b4ebc
00745939  8B D8                           mov ebx, eax
0074593B  85 C0                           test eax, eax
0074593D  0F 88 73 02 00 00               js 0x140745bb6
00745943  8B 57 24                        mov edx, dword ptr [rdi + 0x24]
00745946  48 8B 8F A8 8B 00 00            mov rcx, qword ptr [rdi + 0x8ba8]
0074594D  E8 52 10 07 00                  call 0x1407b69a4
00745952  33 D2                           xor edx, edx
00745954  48 8B CF                        mov rcx, rdi
00745957  E8 88 D9 42 00                  call 0x140b732e4
0074595C  8B D8                           mov ebx, eax
0074595E  85 C0                           test eax, eax
00745960  0F 88 50 02 00 00               js 0x140745bb6
00745966  44 8B 44 24 38                  mov r8d, dword ptr [rsp + 0x38]
0074596B  41 8B D6                        mov edx, r14d
0074596E  48 8B CF                        mov rcx, rdi
00745971  E8 D6 26 FD FF                  call 0x14071804c
00745976  8B D8                           mov ebx, eax
00745978  85 C0                           test eax, eax
0074597A  0F 88 36 02 00 00               js 0x140745bb6
00745980  48 8B CF                        mov rcx, rdi
00745983  E8 A4 12 E7 FF                  call 0x1405b6c2c
00745988  8B D8                           mov ebx, eax
0074598A  85 C0                           test eax, eax
0074598C  0F 88 24 02 00 00               js 0x140745bb6
00745992  48 8B CF                        mov rcx, rdi
00745995  E8 16 12 E7 FF                  call 0x1405b6bb0
0074599A  8B D8                           mov ebx, eax
0074599C  85 C0                           test eax, eax
0074599E  0F 88 12 02 00 00               js 0x140745bb6
007459A4  48 8B CF                        mov rcx, rdi
007459A7  E8 EC 15 E7 FF                  call 0x1405b6f98
007459AC  8B D8                           mov ebx, eax
007459AE  85 C0                           test eax, eax
007459B0  0F 88 00 02 00 00               js 0x140745bb6
007459B6  48 8B CF                        mov rcx, rdi
007459B9  E8 46 10 E7 FF                  call 0x1405b6a04
007459BE  8B D8                           mov ebx, eax
007459C0  85 C0                           test eax, eax
007459C2  0F 88 EE 01 00 00               js 0x140745bb6
007459C8  48 8B CF                        mov rcx, rdi
007459CB  E8 40 11 42 00                  call 0x140b66b10
007459D0  8B D8                           mov ebx, eax
007459D2  85 C0                           test eax, eax
007459D4  0F 88 DC 01 00 00               js 0x140745bb6
007459DA  48 8B CF                        mov rcx, rdi
007459DD  E8 5A BA 09 00                  call 0x1407e143c
007459E2  8B D8                           mov ebx, eax
007459E4  85 C0                           test eax, eax
007459E6  0F 88 CA 01 00 00               js 0x140745bb6
007459EC  48 8B CF                        mov rcx, rdi
007459EF  E8 D4 3C E8 FF                  call 0x1405c96c8
007459F4  8B D8                           mov ebx, eax
007459F6  85 C0                           test eax, eax
007459F8  0F 88 B8 01 00 00               js 0x140745bb6
007459FE  48 8B CF                        mov rcx, rdi
00745A01  E8 52 8E 43 00                  call 0x140b7e858
00745A06  8B D8                           mov ebx, eax
00745A08  85 C0                           test eax, eax
00745A0A  0F 88 A6 01 00 00               js 0x140745bb6
00745A10  48 8B CF                        mov rcx, rdi
00745A13  E8 F0 1D 00 00                  call 0x140747808
00745A18  8B D8                           mov ebx, eax
00745A1A  85 C0                           test eax, eax
00745A1C  0F 88 94 01 00 00               js 0x140745bb6
00745A22  44 39 3D BB D6 7D 00            cmp dword ptr [rip + 0x7dd6bb], r15d
00745A29  74 17                           je 0x140745a42
00745A2B  BA 01 00 00 00                  mov edx, 1
00745A30  48 8B CF                        mov rcx, rdi
00745A33  E8 1C 7D E7 FF                  call 0x1405bd754
00745A38  8B D8                           mov ebx, eax
00745A3A  85 C0                           test eax, eax
00745A3C  0F 88 74 01 00 00               js 0x140745bb6
00745A42  48 8B 0D B7 11 88 00            mov rcx, qword ptr [rip + 0x8811b7]
00745A49  48 8D 87 A0 8E 00 00            lea rax, [rdi + 0x8ea0]
00745A50  48 89 00                        mov qword ptr [rax], rax
00745A53  4C 89 BF 98 8E 00 00            mov qword ptr [rdi + 0x8e98], r15
00745A5A  E8 81 77 30 00                  call 0x140a4d1e0
00745A5F  48 8B CF                        mov rcx, rdi
00745A62  E8 71 57 42 00                  call 0x140b6b1d8
00745A67  4C 8B 25 B2 10 88 00            mov r12, qword ptr [rip + 0x8810b2]
00745A6E  C7 05 D8 11 88 00 01 00 00 00   mov dword ptr [rip + 0x8811d8], 1
00745A78  4D 85 E4                        test r12, r12
00745A7B  75 17                           jne 0x140745a94
00745A7D  0F 10 05 3C FA 7A 00            movups xmm0, xmmword ptr [rip + 0x7afa3c]
00745A84  48 8D 45 40                     lea rax, [rbp + 0x40]
00745A88  48 89 05 91 10 88 00            mov qword ptr [rip + 0x881091], rax
00745A8F  F3 0F 7F 45 50                  movdqu xmmword ptr [rbp + 0x50], xmm0
00745A94  8B 44 24 38                     mov eax, dword ptr [rsp + 0x38]
00745A98  33 C9                           xor ecx, ecx
00745A9A  44 0F B6 87 D0 00 00 00         movzx r8d, byte ptr [rdi + 0xd0]
00745AA2  44 8A 8F D1 00 00 00            mov r9b, byte ptr [rdi + 0xd1]
00745AA9  8B 57 24                        mov edx, dword ptr [rdi + 0x24]
00745AAC  44 89 7C 24 28                  mov dword ptr [rsp + 0x28], r15d
00745AB1  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00745AB5  E8 6E 7E E7 FF                  call 0x1405bd928
00745ABA  8B D8                           mov ebx, eax
00745ABC  41 BF 02 00 00 00               mov r15d, 2
00745AC2  85 C0                           test eax, eax
00745AC4  78 57                           js 0x140745b1d
00745AC6  41 8D 57 FF                     lea edx, [r15 - 1]
00745ACA  48 8B CF                        mov rcx, rdi
00745ACD  E8 16 9D D9 FF                  call 0x1404df7e8
00745AD2  44 0F B7 4C 24 30               movzx r9d, word ptr [rsp + 0x30]
00745AD8  48 8D 8D B0 01 00 00            lea rcx, [rbp + 0x1b0]
00745ADF  44 8B 44 24 38                  mov r8d, dword ptr [rsp + 0x38]
00745AE4  41 8B D6                        mov edx, r14d
00745AE7  E8 14 D8 DF FF                  call 0x140543300
00745AEC  45 8D 47 01                     lea r8d, [r15 + 1]
00745AF0  41 3B C0                        cmp eax, r8d
00745AF3  75 1E                           jne 0x140745b13
00745AF5  8B 44 24 38                     mov eax, dword ptr [rsp + 0x38]
00745AF9  48 8D 95 B0 01 00 00            lea rdx, [rbp + 0x1b0]
00745B00  4D 8B CE                        mov r9, r14
00745B03  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00745B08  B9 DF 01 00 00                  mov ecx, 0x1df
00745B0D  E8 4E 7B DB FF                  call 0x1404fd660
00745B12  CC                              int3
00745B13  41 3B C7                        cmp eax, r15d
00745B16  75 72                           jne 0x140745b8a
00745B18  BB 01 00 00 C0                  mov ebx, 0xc0000001
00745B1D  8B 44 24 38                     mov eax, dword ptr [rsp + 0x38]
00745B21  41 8B CF                        mov ecx, r15d
00745B24  44 0F B6 87 D0 00 00 00         movzx r8d, byte ptr [rdi + 0xd0]
00745B2C  44 8A 8F D1 00 00 00            mov r9b, byte ptr [rdi + 0xd1]
00745B33  8B 57 24                        mov edx, dword ptr [rdi + 0x24]
00745B36  89 5C 24 28                     mov dword ptr [rsp + 0x28], ebx
00745B3A  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00745B3E  E8 E5 7D E7 FF                  call 0x1405bd928
00745B43  45 33 FF                        xor r15d, r15d
00745B46  85 DB                           test ebx, ebx
00745B48  78 1C                           js 0x140745b66
00745B4A  41 8D 57 01                     lea edx, [r15 + 1]
00745B4E  48 8B CF                        mov rcx, rdi
00745B51  E8 8E D7 42 00                  call 0x140b732e4
00745B56  48 8B CF                        mov rcx, rdi
00745B59  E8 4E F0 09 00                  call 0x1407e4bac
00745B5E  48 8B CF                        mov rcx, rdi
00745B61  E8 06 21 E7 FF                  call 0x1405b7c6c
00745B66  48 8B 0D 93 10 88 00            mov rcx, qword ptr [rip + 0x881093]
00745B6D  4C 89 25 AC 0F 88 00            mov qword ptr [rip + 0x880fac], r12
00745B74  E8 77 DE B5 FF                  call 0x1402a39f0
00745B79  4C 8B 64 24 48                  mov r12, qword ptr [rsp + 0x48]
00745B7E  85 DB                           test ebx, ebx
00745B80  0F 89 7F 01 00 00               jns 0x140745d05
00745B86  EB 2E                           jmp 0x140745bb6
00745B88  F3 90                           pause
00745B8A  48 8B 85 C8 00 00 00            mov rax, qword ptr [rbp + 0xc8]
00745B91  48 85 C0                        test rax, rax
00745B94  75 F2                           jne 0x140745b88
00745B96  48 8B CF                        mov rcx, rdi
00745B99  E8 2A 1E 42 00                  call 0x140b679c8
00745B9E  41 BF 01 00 00 00               mov r15d, 1
00745BA4  E9 74 FF FF FF                  jmp 0x140745b1d
00745BA9  BB 59 02 00 C0                  mov ebx, 0xc0000259
00745BAE  45 33 FF                        xor r15d, r15d
00745BB1  EB 0A                           jmp 0x140745bbd
00745BB3  45 33 FF                        xor r15d, r15d
00745BB6  4C 8D 05 03 9B 88 00            lea r8, [rip + 0x889b03]
00745BBD  44 89 3D 8C 10 88 00            mov dword ptr [rip + 0x88108c], r15d
00745BC4  4D 85 ED                        test r13, r13
00745BC7  74 7C                           je 0x140745c45
00745BC9  B8 06 00 00 00                  mov eax, 6
00745BCE  49 8B CD                        mov rcx, r13
00745BD1  8D 50 7A                        lea edx, [rax + 0x7a]
00745BD4  0F 10 06                        movups xmm0, xmmword ptr [rsi]
00745BD7  0F 11 01                        movups xmmword ptr [rcx], xmm0
00745BDA  0F 10 4E 10                     movups xmm1, xmmword ptr [rsi + 0x10]
00745BDE  0F 11 49 10                     movups xmmword ptr [rcx + 0x10], xmm1
00745BE2  0F 10 46 20                     movups xmm0, xmmword ptr [rsi + 0x20]
00745BE6  0F 11 41 20                     movups xmmword ptr [rcx + 0x20], xmm0
00745BEA  0F 10 4E 30                     movups xmm1, xmmword ptr [rsi + 0x30]
00745BEE  0F 11 49 30                     movups xmmword ptr [rcx + 0x30], xmm1
00745BF2  0F 10 46 40                     movups xmm0, xmmword ptr [rsi + 0x40]
00745BF6  0F 11 41 40                     movups xmmword ptr [rcx + 0x40], xmm0
00745BFA  0F 10 4E 50                     movups xmm1, xmmword ptr [rsi + 0x50]
00745BFE  0F 11 49 50                     movups xmmword ptr [rcx + 0x50], xmm1
00745C02  0F 10 46 60                     movups xmm0, xmmword ptr [rsi + 0x60]
00745C06  0F 11 41 60                     movups xmmword ptr [rcx + 0x60], xmm0
00745C0A  48 03 CA                        add rcx, rdx
00745C0D  0F 10 4E 70                     movups xmm1, xmmword ptr [rsi + 0x70]
00745C11  48 03 F2                        add rsi, rdx
00745C14  0F 11 49 F0                     movups xmmword ptr [rcx - 0x10], xmm1
00745C18  48 83 E8 01                     sub rax, 1
00745C1C  75 B6                           jne 0x140745bd4
00745C1E  0F 10 06                        movups xmm0, xmmword ptr [rsi]
00745C21  0F 11 01                        movups xmmword ptr [rcx], xmm0
00745C24  0F 10 4E 10                     movups xmm1, xmmword ptr [rsi + 0x10]
00745C28  0F 11 49 10                     movups xmmword ptr [rcx + 0x10], xmm1
00745C2C  0F 10 46 20                     movups xmm0, xmmword ptr [rsi + 0x20]
00745C30  0F 11 41 20                     movups xmmword ptr [rcx + 0x20], xmm0
00745C34  48 8B 46 30                     mov rax, qword ptr [rsi + 0x30]
00745C38  48 89 41 30                     mov qword ptr [rcx + 0x30], rax
00745C3C  0F B7 44 24 30                  movzx eax, word ptr [rsp + 0x30]
00745C41  4D 89 2C C0                     mov qword ptr [r8 + rax*8], r13
00745C45  48 85 FF                        test rdi, rdi
00745C48  0F 84 87 00 00 00               je 0x140745cd5
00745C4E  33 D2                           xor edx, edx
00745C50  48 8B CF                        mov rcx, rdi
00745C53  E8 90 9B D9 FF                  call 0x1404df7e8
00745C58  48 8B CF                        mov rcx, rdi
00745C5B  E8 58 3D E8 FF                  call 0x1405c99b8
00745C60  44 39 3D 7D D4 7D 00            cmp dword ptr [rip + 0x7dd47d], r15d
00745C67  74 0A                           je 0x140745c73
00745C69  33 D2                           xor edx, edx
00745C6B  48 8B CF                        mov rcx, rdi
00745C6E  E8 E1 7A E7 FF                  call 0x1405bd754
00745C73  48 8B CF                        mov rcx, rdi
00745C76  E8 0D 22 E7 FF                  call 0x1405b7e88
00745C7B  48 8B CF                        mov rcx, rdi
00745C7E  E8 9D 24 E7 FF                  call 0x1405b8120
00745C83  48 8B CF                        mov rcx, rdi
00745C86  E8 81 22 E7 FF                  call 0x1405b7f0c
00745C8B  48 8B CF                        mov rcx, rdi
00745C8E  E8 AD 22 E7 FF                  call 0x1405b7f40
00745C93  48 8B CF                        mov rcx, rdi
00745C96  E8 75 09 42 00                  call 0x140b66610
00745C9B  48 8B CF                        mov rcx, rdi
00745C9E  E8 01 23 FD FF                  call 0x140717fa4
00745CA3  48 8B CF                        mov rcx, rdi
00745CA6  E8 09 33 0B 00                  call 0x1407f8fb4
00745CAB  48 8B CF                        mov rcx, rdi
00745CAE  E8 0D F0 06 00                  call 0x1407b4cc0
00745CB3  48 8B 8F 50 8B 00 00            mov rcx, qword ptr [rdi + 0x8b50]
00745CBA  48 85 C9                        test rcx, rcx
00745CBD  74 0E                           je 0x140745ccd
00745CBF  33 D2                           xor edx, edx
00745CC1  E8 AA CB 43 00                  call 0x140b82870
00745CC6  4C 89 BF 50 8B 00 00            mov qword ptr [rdi + 0x8b50], r15
00745CCD  48 8B CF                        mov rcx, rdi
00745CD0  E8 F3 71 E7 FF                  call 0x1405bcec8
00745CD5  4D 85 E4                        test r12, r12
00745CD8  74 08                           je 0x140745ce2
00745CDA  41 8B CE                        mov ecx, r14d
00745CDD  E8 A6 02 F1 FF                  call 0x140655f88
00745CE2  48 85 FF                        test rdi, rdi
00745CE5  74 14                           je 0x140745cfb
00745CE7  4C 8D 44 24 50                  lea r8, [rsp + 0x50]
00745CEC  48 8B CF                        mov rcx, rdi
00745CEF  48 8D 95 B0 01 00 00            lea rdx, [rbp + 0x1b0]
00745CF6  E8 ED 53 42 00                  call 0x140b6b0e8
00745CFB  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
00745D00  E8 A3 23 E7 FF                  call 0x1405b80a8
00745D05  8B C3                           mov eax, ebx
00745D07  48 8B 8D 70 07 00 00            mov rcx, qword ptr [rbp + 0x770]
00745D0E  48 33 CC                        xor rcx, rsp
00745D11  E8 2A 69 F6 FF                  call 0x1406ac640
00745D16  48 8B 9C 24 C0 08 00 00         mov rbx, qword ptr [rsp + 0x8c0]
00745D1E  48 81 C4 80 08 00 00            add rsp, 0x880
00745D25  41 5F                           pop r15
00745D27  41 5E                           pop r14
00745D29  41 5D                           pop r13
00745D2B  41 5C                           pop r12
00745D2D  5F                              pop rdi
00745D2E  5E                              pop rsi
00745D2F  5D                              pop rbp
00745D30  C3                              ret
00745D31  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiStartDynamicProcessor(__int64 a1, int a2, unsigned __int16 a3, int a4)
{
    __int64 result;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m608;
    unsigned __int64 v_stack_m6F0;
    unsigned __int64 v_stack_m768;
    unsigned __int64 v_stack_m778;
    unsigned __int64 v_stack_m7B8;
    unsigned int v_stack_m840;
    unsigned int v_stack_m844;
    unsigned int v_stack_m84C;
    unsigned int v_stack_m850;
    unsigned int v_stack_m854;
    unsigned int v_stack_m858;
    unsigned int v_stack_m864;
    unsigned __int64 v_stack_m868;
    unsigned __int64 v_stack_m870;
    unsigned int v_stack_m874;
    unsigned int v_stack_m878;
    unsigned int v_stack_m880;
    unsigned __int16 v_stack_m888;
    unsigned int v_stack_m890;
    unsigned int v_stack_m898;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (0x880ULL);
    result = (*(unsigned __int64 *)(v_rip + 7098450)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m880 = a2;
    v_rbx = 0;
    result = 0;
    v_stack_m878 = 0;
    a2 = 0;
    v_stack_m874 = 0;
    v_stack_m864 = 0;
    result = memset(v_stack_m868, a2, 228, a4);
    a2 = 0;
    result = memset(v_stack_m778, a2, 368, a4);
    a2 = 0;
    result = memset(v_stack_m608, a2, (unsigned int)(0x5C0ULL), a4);
    v_stack_m888 = 0;
    result = KiInitializeProcessorStateInitializationParameters(v_stack_m868, a2, (unsigned int)(0x5C0ULL), a4);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 8917783)))) >= 0x800ULL) goto loc_00745BA9;
    if ((*(unsigned int *)(v_rip + 8918291)) == 0) goto loc_00745795;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 8917751)))) >= (*(unsigned int *)(v_rip + 8918277))) goto loc_00745BA9;
loc_00745795:
    result = HalRegisterDynamicProcessor((unsigned int)(*(unsigned int *)(v_rip + 8918217)), (unsigned int)(v_stack_m880), v_rip + 8953680, a4);
    if (sign_flag) goto loc_00745BB3;
    v_stack_m888 = a3;
    result = KiQueryProcessorNode((unsigned int)((unsigned int)((unsigned int)(a4))), v_stack_m880, v_stack_m888, a4);
    v_r15 = 0;
    if ((unsigned int)(result) != 0) goto loc_00745B7E;
    v_stack_m868 = 1;
    result = KiComputeProcessorDataSize((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 8917774)))), v_stack_m878, v_stack_m874, (unsigned int)(*(unsigned int *)(v_rip + 8917774)));
    v_stack_m858 = (unsigned int)(result);
    v_stack_m844 = (unsigned int)((unsigned int)(v_stack_m878));
    v_stack_m840 = (unsigned int)((unsigned int)(v_stack_m874));
    v_stack_m854 = (unsigned int)(v_stack_m888);
    v_stack_m850 = (unsigned int)((unsigned int)(a4));
    v_stack_m84C = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 8917774)));
    result = KiAllocateProcessorStateInitializationParameters(v_stack_m868, v_stack_m888, v_stack_m874, (unsigned int)(*(unsigned int *)(v_rip + 8917774)));
    if (sign_flag) goto loc_00745BB6;
    result = ExCreatePoolTagTable((unsigned int)((unsigned int)((unsigned int)(a4))), v_stack_m888, v_stack_m874, (unsigned int)(*(unsigned int *)(v_rip + 8917774)));
    v_stack_m870 = result;
    if (result != 0) goto loc_0074585A;
    *(unsigned int *)(v_rip + 8918011) = 0;
    goto loc_00745CFB;
loc_0074585A:
    v_stack_m768 = v_xmm0;
    result = KiInitializeProcessorState(v_stack_m608, v_stack_m778, v_stack_m868, (unsigned int)(*(unsigned int *)(v_rip + 8917774)));
    if (result != 0) goto loc_0074589D;
    goto loc_00745BB6;
loc_0074589D:
    result = MmInitializeProcessor(result, v_stack_m778, v_stack_m868, (unsigned int)(*(unsigned int *)(v_rip + 8917774)));
    if ((unsigned int)(result) != 0) goto loc_007458BC;
    goto loc_00745BB6;
loc_007458BC:
    result = KiInitializePrcbContext(result, v_stack_m888, v_stack_m868, (unsigned int)(*(unsigned int *)(v_rip + 8917774)));
    if (sign_flag) goto loc_00745BB6;
    result = KeInitializeTimerTable(result, v_stack_m888, v_stack_m868, (unsigned int)(*(unsigned int *)(v_rip + 8917774)));
    if (sign_flag) goto loc_00745BB6;
    result = ExInitializeProcessor(result, 1, v_stack_m868, (unsigned int)(*(unsigned int *)(v_rip + 8917774)));
    if (sign_flag) goto loc_00745BB6;
    result = ObInitializeProcessor(result, 1, v_stack_m868, (unsigned int)(*(unsigned int *)(v_rip + 8917774)));
    if (sign_flag) goto loc_00745BB6;
    a2 = 0;
    result = IoInitializeProcessor(result, a2, v_stack_m868, (unsigned int)(*(unsigned int *)(v_rip + 8917774)));
    if (sign_flag) goto loc_00745BB6;
    result = CcInitializeProcessor(result, a2, v_stack_m868, (unsigned int)(*(unsigned int *)(v_rip + 8917774)));
    if (sign_flag) goto loc_00745BB6;
    result = EtwInitializeProcessor(result, a2, v_stack_m868, (unsigned int)(*(unsigned int *)(v_rip + 8917774)));
    if (sign_flag) goto loc_00745BB6;
    result = EtwpInitializeActivityIdSeed(*(unsigned __int64 *)(result + 35752), (unsigned int)(*(unsigned int *)(result + 36)), v_stack_m868, (unsigned int)(*(unsigned int *)(v_rip + 8917774)));
    a2 = 0;
    result = WheaInitializeProcessor(result, a2, v_stack_m868, (unsigned int)(*(unsigned int *)(v_rip + 8917774)));
    if (sign_flag) goto loc_00745BB6;
    result = HvlInitializeProcessor(result, (unsigned int)((unsigned int)((unsigned int)(a4))), (unsigned int)(v_stack_m880), (unsigned int)(*(unsigned int *)(v_rip + 8917774)));
    if (sign_flag) goto loc_00745BB6;
    result = KiAllocatePrcbThreads(result, (unsigned int)((unsigned int)((unsigned int)(a4))), (unsigned int)(v_stack_m880), (unsigned int)(*(unsigned int *)(v_rip + 8917774)));
    if (sign_flag) goto loc_00745BB6;
    result = KiAllocateLocalSharedReadyQueue(result, (unsigned int)((unsigned int)((unsigned int)(a4))), (unsigned int)(v_stack_m880), (unsigned int)(*(unsigned int *)(v_rip + 8917774)));
    if (sign_flag) goto loc_00745BB6;
    result = KiAllocateStaticRescheduleContext(result, (unsigned int)((unsigned int)((unsigned int)(a4))), (unsigned int)(v_stack_m880), (unsigned int)(*(unsigned int *)(v_rip + 8917774)));
    if (sign_flag) goto loc_00745BB6;
    result = KiAllocateIdleSearchStructures(result, (unsigned int)((unsigned int)((unsigned int)(a4))), (unsigned int)(v_stack_m880), (unsigned int)(*(unsigned int *)(v_rip + 8917774)));
    if (sign_flag) goto loc_00745BB6;
    result = KiInitializeThreadCycleTable(result, (unsigned int)((unsigned int)((unsigned int)(a4))), (unsigned int)(v_stack_m880), (unsigned int)(*(unsigned int *)(v_rip + 8917774)));
    if (sign_flag) goto loc_00745BB6;
    result = CmInitializeProcessorCallbacks(result, (unsigned int)((unsigned int)((unsigned int)(a4))), (unsigned int)(v_stack_m880), (unsigned int)(*(unsigned int *)(v_rip + 8917774)));
    if (sign_flag) goto loc_00745BB6;
    result = KiAllocateForceParkingData(result, (unsigned int)((unsigned int)((unsigned int)(a4))), (unsigned int)(v_stack_m880), (unsigned int)(*(unsigned int *)(v_rip + 8917774)));
    if (sign_flag) goto loc_00745BB6;
    result = VmInitializeProcessor(result, (unsigned int)((unsigned int)((unsigned int)(a4))), (unsigned int)(v_stack_m880), (unsigned int)(*(unsigned int *)(v_rip + 8917774)));
    if (sign_flag) goto loc_00745BB6;
    result = KiInitializeSingleDpcRuntimeHistoryHashTable(result, (unsigned int)((unsigned int)((unsigned int)(a4))), (unsigned int)(v_stack_m880), (unsigned int)(*(unsigned int *)(v_rip + 8917774)));
    if (sign_flag) goto loc_00745BB6;
    if ((*(unsigned int *)(v_rip + 8246971)) == 0) goto loc_00745A42;
    result = KiAllocateProcessorHiberSwapShadowStacks(result, 1, (unsigned int)(v_stack_m880), (unsigned int)(*(unsigned int *)(v_rip + 8917774)));
    if (sign_flag) goto loc_00745BB6;
loc_00745A42:
    *(unsigned __int64 *)(result + 36512) = result + 36512;
    *(unsigned __int64 *)(result + 36504) = 0;
    result = MmLockPagableSectionByHandle(*(unsigned __int64 *)(v_rip + 8917431), 1, (unsigned int)(v_stack_m880), (unsigned int)(*(unsigned int *)(v_rip + 8917774)));
    result = KiAddProcessorToGroupSchedulingDatabase(result, 1, (unsigned int)(v_stack_m880), (unsigned int)(*(unsigned int *)(v_rip + 8917774)));
    *(unsigned int *)(v_rip + 8917464) = 1;
    if (*(unsigned __int64 *)(v_rip + 8917170) == 0) {
        result = v_stack_m778;
        *(unsigned __int64 *)(v_rip + 8917137) = result;
        v_stack_m768 = v_xmm0;
    }
    a1 = 0;
    v_stack_m890 = 0;
    v_stack_m898 = (unsigned int)((unsigned int)(v_stack_m880));
    result = KiDynamicProcessorAddNotification(a1, (unsigned int)(*(unsigned int *)(result + 36)), *(unsigned __int8 *)(result + 208), *(unsigned __int8 *)(result + 209));
    if (sign_flag) goto loc_00745B1D;
    result = KiRcuProcessorInitialize(result, 2 - 1, *(unsigned __int8 *)(result + 208), *(unsigned __int8 *)(result + 209));
    result = HalStartDynamicProcessor(v_stack_m608, (unsigned int)((unsigned int)((unsigned int)(a4))), (unsigned int)(v_stack_m880), v_stack_m888);
    if (((unsigned int)(result)) == ((unsigned int)(2 + 1))) {
        result = v_stack_m880;
        a2 = v_stack_m608;
        a4 = (unsigned int)(a4);
        v_stack_m898 = result;
        a1 = 479;
        result = KeBugCheckEx(a1, a2, 2 + 1, a4);
    }
    if (((unsigned int)(result)) != 2) goto loc_00745B8A;
loc_00745B1D:
    v_stack_m890 = (unsigned int)((unsigned int)(0xC0000001ULL));
    v_stack_m898 = (unsigned int)((unsigned int)(v_stack_m880));
    result = KiDynamicProcessorAddNotification(2, (unsigned int)(*(unsigned int *)(result + 36)), *(unsigned __int8 *)(result + 208), *(unsigned __int8 *)(result + 209));
    v_r15 = 0;
    if (!(sign_flag)) {
        a2 = v_r15 + 1;
        a1 = result;
        result = WheaInitializeProcessor(a1, a2, *(unsigned __int8 *)(result + 208), *(unsigned __int8 *)(result + 209));
        a1 = result;
        result = CmInitializeProcessor(a1, a2, *(unsigned __int8 *)(result + 208), *(unsigned __int8 *)(result + 209));
        a1 = result;
        result = KiDynamicProcessorInitialization(a1, a2, *(unsigned __int8 *)(result + 208), *(unsigned __int8 *)(result + 209));
    }
    *(unsigned __int64 *)(v_rip + 8916908) = *(unsigned __int64 *)(v_rip + 8917170);
    result = MmUnlockPagableImageSection(*(unsigned __int64 *)(v_rip + 8917139), a2, *(unsigned __int8 *)(result + 208), *(unsigned __int8 *)(result + 209));
loc_00745B7E:
    if (!sign_flag) goto loc_00745D05;
    goto loc_00745BB6;
loc_00745B88:
loc_00745B8A:
    if (v_stack_m6F0 != 0) goto loc_00745B88;
    result = KiInitializeDynamicProcessor(result, a2, *(unsigned __int8 *)(result + 208), *(unsigned __int8 *)(result + 209));
    goto loc_00745B1D;
loc_00745BA9:
    v_r15 = 0;
    goto loc_00745BBD;
loc_00745BB3:
    v_r15 = 0;
loc_00745BB6:
loc_00745BBD:
    *(unsigned int *)(v_rip + 8917132) = 0;
    if (*(unsigned __int64 *)(v_rip + 8953434 + v_stack_m888 * 8) == 0) goto loc_00745C45;
loc_00745BD4:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 8953434 + v_stack_m888 * 8)) = v_xmm0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 8953434 + v_stack_m888 * 8) + 16) = v_xmm1;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 8953434 + v_stack_m888 * 8) + 32) = v_xmm0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 8953434 + v_stack_m888 * 8) + 48) = v_xmm1;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 8953434 + v_stack_m888 * 8) + 64) = v_xmm0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 8953434 + v_stack_m888 * 8) + 80) = v_xmm1;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 8953434 + v_stack_m888 * 8) + 96) = v_xmm0;
    a1 = (*(unsigned __int64 *)(v_rip + 8953434 + v_stack_m888 * 8)) + (6 + 122);
    v_rsi = (*(unsigned __int64 *)((unsigned int)(0xC000009AULL) + v_stack_m888 * 8)) + (6 + 122);
    *(unsigned __int64 *)(a1 - 16) = v_xmm1;
    result = (6) - (1);
    if (condition_is_not_equal) goto loc_00745BD4;
    *(unsigned __int64 *)(a1) = v_xmm0;
    *(unsigned __int64 *)(a1 + 16) = v_xmm1;
    *(unsigned __int64 *)(a1 + 32) = v_xmm0;
    *(unsigned __int64 *)(a1 + 48) = *(unsigned __int64 *)(v_rsi + 48);
    *(unsigned __int64 *)(v_rip + 8952579 + v_stack_m888 * 8) = *(unsigned __int64 *)(v_rip + 8953434 + v_stack_m888 * 8);
loc_00745C45:
    if (result == 0) goto loc_00745CD5;
    a2 = 0;
    result = KiRcuProcessorInitialize(result, a2, v_rip + 8952579, *(unsigned __int8 *)(result + 209));
    result = KiFreeForceParkingData(result, a2, v_rip + 8952579, *(unsigned __int8 *)(result + 209));
    if ((*(unsigned int *)(v_rip + 8246397)) != 0) {
        a2 = 0;
        a1 = result;
        result = KiAllocateProcessorHiberSwapShadowStacks(a1, a2, v_rip + 8952579, *(unsigned __int8 *)(result + 209));
    }
    result = KiFreeIdleSearchStructures(result, a2, v_rip + 8952579, *(unsigned __int8 *)(result + 209));
    result = KiFreeStaticRescheduleContext(result, a2, v_rip + 8952579, *(unsigned __int8 *)(result + 209));
    result = KiFreeLocalSharedReadyQueue(result, a2, v_rip + 8952579, *(unsigned __int8 *)(result + 209));
    result = KiFreePrcbThreads(result, a2, v_rip + 8952579, *(unsigned __int8 *)(result + 209));
    result = KiFreeThreadCycleTable(result, a2, v_rip + 8952579, *(unsigned __int8 *)(result + 209));
    result = HvlDeleteProcessor(result, a2, v_rip + 8952579, *(unsigned __int8 *)(result + 209));
    result = MmDeleteProcessor(result, a2, v_rip + 8952579, *(unsigned __int8 *)(result + 209));
    result = EtwDeleteProcessor(result, a2, v_rip + 8952579, *(unsigned __int8 *)(result + 209));
    if (*(unsigned __int64 *)(result + 35664) != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(result + 35664), a2, v_rip + 8952579, *(unsigned __int8 *)(result + 209));
        *(unsigned __int64 *)(result + 35664) = 0;
    }
    result = KiUnassignProcessorNumberFromPrcb(result, a2, v_rip + 8952579, *(unsigned __int8 *)(result + 209));
loc_00745CD5:
    if (v_stack_m870 != 0) {
        a1 = (unsigned int)((unsigned int)(a4));
        result = ExDeletePoolTagTable(a1, a2, v_rip + 8952579, *(unsigned __int8 *)(result + 209));
    }
    if (result != 0) {
        a3 = v_stack_m868;
        a1 = result;
        a2 = v_stack_m608;
        result = KiUnshadowProcessorAllocation(a1, a2, a3, *(unsigned __int8 *)(result + 209));
    }
    result = KiFreeProcessorStateInitializationParameters(v_stack_m868, a2, a3, *(unsigned __int8 *)(result + 209));
loc_00745D05:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, *(unsigned __int8 *)(result + 209));
    v_rsp = (v_rsp) + (0x880ULL);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KiStartDynamicProcessor(int64_t Arg1, int32_t Arg2, uint16_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m608;
    uint64_t v_stack_m6F0;
    uint64_t v_stack_m768;
    uint64_t v_stack_m778;
    uint64_t v_stack_m7B8;
    uint32_t v_stack_m840;
    uint32_t v_stack_m844;
    uint32_t v_stack_m84C;
    uint32_t v_stack_m850;
    uint32_t v_stack_m854;
    uint32_t v_stack_m858;
    uint32_t v_stack_m864;
    uint64_t v_stack_m868;
    uint64_t v_stack_m870;
    uint32_t v_stack_m874;
    uint32_t v_stack_m878;
    uint32_t v_stack_m880;
    uint16_t v_stack_m888;
    uint32_t v_stack_m890;
    uint32_t v_stack_m898;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (0x880ULL);
    result = (*(uint64_t *)(v_rip + 0x6C5052)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m880 = Arg2;
    local_rbx = 0;
    result = 0;
    v_stack_m878 = 0;
    Arg2 = 0;
    v_stack_m874 = 0;
    v_stack_m864 = 0;
    result = memset(v_stack_m868, Arg2, 228, Arg4);
    Arg2 = 0;
    result = memset(v_stack_m778, Arg2, 368, Arg4);
    Arg2 = 0;
    result = memset(v_stack_m608, Arg2, (uint32_t)(0x5C0ULL), Arg4);
    v_stack_m888 = 0;
    result = KiInitializeProcessorStateInitializationParameters(v_stack_m868, Arg2, (uint32_t)(0x5C0ULL), Arg4);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x881317)))) >= 0x800ULL) goto loc_00745BA9;
    if ((*(uint32_t *)(v_rip + 0x881513)) == 0) goto loc_00745795;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x8812F7)))) >= (*(uint32_t *)(v_rip + 0x881505))) goto loc_00745BA9;
loc_00745795:
    result = HalRegisterDynamicProcessor((uint32_t)(*(uint32_t *)(v_rip + 0x8814C9)), (uint32_t)(v_stack_m880), v_rip + 8953680, Arg4);
    if (sign_flag) goto loc_00745BB3;
    v_stack_m888 = Arg3;
    result = KiQueryProcessorNode((uint32_t)((uint32_t)((uint32_t)(Arg4))), v_stack_m880, v_stack_m888, Arg4);
    local_r15 = 0;
    if ((uint32_t)(result) != 0) goto loc_00745B7E;
    v_stack_m868 = 1;
    result = KiComputeProcessorDataSize((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x88130E)))), v_stack_m878, v_stack_m874, (uint32_t)(*(uint32_t *)(v_rip + 0x88130E)));
    v_stack_m858 = (uint32_t)(result);
    v_stack_m844 = (uint32_t)((uint32_t)(v_stack_m878));
    v_stack_m840 = (uint32_t)((uint32_t)(v_stack_m874));
    v_stack_m854 = (uint32_t)(v_stack_m888);
    v_stack_m850 = (uint32_t)((uint32_t)(Arg4));
    v_stack_m84C = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x88130E)));
    result = KiAllocateProcessorStateInitializationParameters(v_stack_m868, v_stack_m888, v_stack_m874, (uint32_t)(*(uint32_t *)(v_rip + 0x88130E)));
    if (sign_flag) goto loc_00745BB6;
    result = ExCreatePoolTagTable((uint32_t)((uint32_t)((uint32_t)(Arg4))), v_stack_m888, v_stack_m874, (uint32_t)(*(uint32_t *)(v_rip + 0x88130E)));
    v_stack_m870 = result;
    if (result != 0) goto loc_0074585A;
    *(uint32_t *)(v_rip + 0x8813FB) = 0;
    goto loc_00745CFB;
loc_0074585A:
    v_stack_m768 = v_xmm0;
    result = KiInitializeProcessorState(v_stack_m608, v_stack_m778, v_stack_m868, (uint32_t)(*(uint32_t *)(v_rip + 0x88130E)));
    if (result != 0) goto loc_0074589D;
    goto loc_00745BB6;
loc_0074589D:
    result = MmInitializeProcessor(result, v_stack_m778, v_stack_m868, (uint32_t)(*(uint32_t *)(v_rip + 0x88130E)));
    if ((uint32_t)(result) != 0) goto loc_007458BC;
    goto loc_00745BB6;
loc_007458BC:
    result = KiInitializePrcbContext(result, v_stack_m888, v_stack_m868, (uint32_t)(*(uint32_t *)(v_rip + 0x88130E)));
    if (sign_flag) goto loc_00745BB6;
    result = KeInitializeTimerTable(result, v_stack_m888, v_stack_m868, (uint32_t)(*(uint32_t *)(v_rip + 0x88130E)));
    if (sign_flag) goto loc_00745BB6;
    result = ExInitializeProcessor(result, 1, v_stack_m868, (uint32_t)(*(uint32_t *)(v_rip + 0x88130E)));
    if (sign_flag) goto loc_00745BB6;
    result = ObInitializeProcessor(result, 1, v_stack_m868, (uint32_t)(*(uint32_t *)(v_rip + 0x88130E)));
    if (sign_flag) goto loc_00745BB6;
    Arg2 = 0;
    result = IoInitializeProcessor(result, Arg2, v_stack_m868, (uint32_t)(*(uint32_t *)(v_rip + 0x88130E)));
    if (sign_flag) goto loc_00745BB6;
    result = CcInitializeProcessor(result, Arg2, v_stack_m868, (uint32_t)(*(uint32_t *)(v_rip + 0x88130E)));
    if (sign_flag) goto loc_00745BB6;
    result = EtwInitializeProcessor(result, Arg2, v_stack_m868, (uint32_t)(*(uint32_t *)(v_rip + 0x88130E)));
    if (sign_flag) goto loc_00745BB6;
    result = EtwpInitializeActivityIdSeed(*(uint64_t *)(result + 0x8BA8), (uint32_t)(*(uint32_t *)(result + 0x24)), v_stack_m868, (uint32_t)(*(uint32_t *)(v_rip + 0x88130E)));
    Arg2 = 0;
    result = WheaInitializeProcessor(result, Arg2, v_stack_m868, (uint32_t)(*(uint32_t *)(v_rip + 0x88130E)));
    if (sign_flag) goto loc_00745BB6;
    result = HvlInitializeProcessor(result, (uint32_t)((uint32_t)((uint32_t)(Arg4))), (uint32_t)(v_stack_m880), (uint32_t)(*(uint32_t *)(v_rip + 0x88130E)));
    if (sign_flag) goto loc_00745BB6;
    result = KiAllocatePrcbThreads(result, (uint32_t)((uint32_t)((uint32_t)(Arg4))), (uint32_t)(v_stack_m880), (uint32_t)(*(uint32_t *)(v_rip + 0x88130E)));
    if (sign_flag) goto loc_00745BB6;
    result = KiAllocateLocalSharedReadyQueue(result, (uint32_t)((uint32_t)((uint32_t)(Arg4))), (uint32_t)(v_stack_m880), (uint32_t)(*(uint32_t *)(v_rip + 0x88130E)));
    if (sign_flag) goto loc_00745BB6;
    result = KiAllocateStaticRescheduleContext(result, (uint32_t)((uint32_t)((uint32_t)(Arg4))), (uint32_t)(v_stack_m880), (uint32_t)(*(uint32_t *)(v_rip + 0x88130E)));
    if (sign_flag) goto loc_00745BB6;
    result = KiAllocateIdleSearchStructures(result, (uint32_t)((uint32_t)((uint32_t)(Arg4))), (uint32_t)(v_stack_m880), (uint32_t)(*(uint32_t *)(v_rip + 0x88130E)));
    if (sign_flag) goto loc_00745BB6;
    result = KiInitializeThreadCycleTable(result, (uint32_t)((uint32_t)((uint32_t)(Arg4))), (uint32_t)(v_stack_m880), (uint32_t)(*(uint32_t *)(v_rip + 0x88130E)));
    if (sign_flag) goto loc_00745BB6;
    result = CmInitializeProcessorCallbacks(result, (uint32_t)((uint32_t)((uint32_t)(Arg4))), (uint32_t)(v_stack_m880), (uint32_t)(*(uint32_t *)(v_rip + 0x88130E)));
    if (sign_flag) goto loc_00745BB6;
    result = KiAllocateForceParkingData(result, (uint32_t)((uint32_t)((uint32_t)(Arg4))), (uint32_t)(v_stack_m880), (uint32_t)(*(uint32_t *)(v_rip + 0x88130E)));
    if (sign_flag) goto loc_00745BB6;
    result = VmInitializeProcessor(result, (uint32_t)((uint32_t)((uint32_t)(Arg4))), (uint32_t)(v_stack_m880), (uint32_t)(*(uint32_t *)(v_rip + 0x88130E)));
    if (sign_flag) goto loc_00745BB6;
    result = KiInitializeSingleDpcRuntimeHistoryHashTable(result, (uint32_t)((uint32_t)((uint32_t)(Arg4))), (uint32_t)(v_stack_m880), (uint32_t)(*(uint32_t *)(v_rip + 0x88130E)));
    if (sign_flag) goto loc_00745BB6;
    if ((*(uint32_t *)(v_rip + 0x7DD6BB)) == 0) goto loc_00745A42;
    result = KiAllocateProcessorHiberSwapShadowStacks(result, 1, (uint32_t)(v_stack_m880), (uint32_t)(*(uint32_t *)(v_rip + 0x88130E)));
    if (sign_flag) goto loc_00745BB6;
loc_00745A42:
    *(uint64_t *)(result + 0x8EA0) = result + 36512;
    *(uint64_t *)(result + 0x8E98) = 0;
    result = MmLockPagableSectionByHandle(*(uint64_t *)(v_rip + 0x8811B7), 1, (uint32_t)(v_stack_m880), (uint32_t)(*(uint32_t *)(v_rip + 0x88130E)));
    result = KiAddProcessorToGroupSchedulingDatabase(result, 1, (uint32_t)(v_stack_m880), (uint32_t)(*(uint32_t *)(v_rip + 0x88130E)));
    *(uint32_t *)(v_rip + 0x8811D8) = 1;
    if (*(uint64_t *)(v_rip + 0x8810B2) == 0) {
        result = v_stack_m778;
        *(uint64_t *)(v_rip + 0x881091) = result;
        v_stack_m768 = v_xmm0;
    }
    Arg1 = 0;
    v_stack_m890 = 0;
    v_stack_m898 = (uint32_t)((uint32_t)(v_stack_m880));
    result = KiDynamicProcessorAddNotification(Arg1, (uint32_t)(*(uint32_t *)(result + 0x24)), *(uint8_t *)(result + 0xD0), *(uint8_t *)(result + 0xD1));
    if (sign_flag) goto loc_00745B1D;
    result = KiRcuProcessorInitialize(result, 2 - 1, *(uint8_t *)(result + 0xD0), *(uint8_t *)(result + 0xD1));
    result = HalStartDynamicProcessor(v_stack_m608, (uint32_t)((uint32_t)((uint32_t)(Arg4))), (uint32_t)(v_stack_m880), v_stack_m888);
    if (((uint32_t)(result)) == ((uint32_t)(2 + 1))) {
        result = v_stack_m880;
        Arg2 = v_stack_m608;
        Arg4 = (uint32_t)(Arg4);
        v_stack_m898 = result;
        Arg1 = 479;
        result = KeBugCheckEx(Arg1, Arg2, 2 + 1, Arg4);
    }
    if (((uint32_t)(result)) != 2) goto loc_00745B8A;
loc_00745B1D:
    v_stack_m890 = (uint32_t)((uint32_t)(0xC0000001ULL));
    v_stack_m898 = (uint32_t)((uint32_t)(v_stack_m880));
    result = KiDynamicProcessorAddNotification(2, (uint32_t)(*(uint32_t *)(result + 0x24)), *(uint8_t *)(result + 0xD0), *(uint8_t *)(result + 0xD1));
    local_r15 = 0;
    if (!(sign_flag)) {
        Arg2 = local_r15 + 1;
        Arg1 = result;
        result = WheaInitializeProcessor(Arg1, Arg2, *(uint8_t *)(result + 0xD0), *(uint8_t *)(result + 0xD1));
        Arg1 = result;
        result = CmInitializeProcessor(Arg1, Arg2, *(uint8_t *)(result + 0xD0), *(uint8_t *)(result + 0xD1));
        Arg1 = result;
        result = KiDynamicProcessorInitialization(Arg1, Arg2, *(uint8_t *)(result + 0xD0), *(uint8_t *)(result + 0xD1));
    }
    *(uint64_t *)(v_rip + 0x880FAC) = *(uint64_t *)(v_rip + 0x8810B2);
    result = MmUnlockPagableImageSection(*(uint64_t *)(v_rip + 0x881093), Arg2, *(uint8_t *)(result + 0xD0), *(uint8_t *)(result + 0xD1));
loc_00745B7E:
    if (!sign_flag) goto loc_00745D05;
    goto loc_00745BB6;
loc_00745B88:
loc_00745B8A:
    if (v_stack_m6F0 != 0) goto loc_00745B88;
    result = KiInitializeDynamicProcessor(result, Arg2, *(uint8_t *)(result + 0xD0), *(uint8_t *)(result + 0xD1));
    goto loc_00745B1D;
loc_00745BA9:
    local_r15 = 0;
    goto loc_00745BBD;
loc_00745BB3:
    local_r15 = 0;
loc_00745BB6:
loc_00745BBD:
    *(uint32_t *)(v_rip + 0x88108C) = 0;
    if (*(uint64_t *)(v_rip + 0x889E5A + v_stack_m888 * 8) == 0) goto loc_00745C45;
loc_00745BD4:
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x889E5A + v_stack_m888 * 8)) = v_xmm0;
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x889E5A + v_stack_m888 * 8) + 0x10) = v_xmm1;
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x889E5A + v_stack_m888 * 8) + 0x20) = v_xmm0;
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x889E5A + v_stack_m888 * 8) + 0x30) = v_xmm1;
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x889E5A + v_stack_m888 * 8) + 0x40) = v_xmm0;
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x889E5A + v_stack_m888 * 8) + 0x50) = v_xmm1;
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x889E5A + v_stack_m888 * 8) + 0x60) = v_xmm0;
    Arg1 = (*(uint64_t *)(v_rip + 0x889E5A + v_stack_m888 * 8)) + (6 + 122);
    local_rsi = (*(uint64_t *)((uint32_t)(0xC000009AULL) + v_stack_m888 * 8)) + (6 + 122);
    *(uint64_t *)(Arg1 - 0x10) = v_xmm1;
    result = (6) - (1);
    if (condition_is_not_equal) goto loc_00745BD4;
    *(uint64_t *)(Arg1) = v_xmm0;
    *(uint64_t *)(Arg1 + 0x10) = v_xmm1;
    *(uint64_t *)(Arg1 + 0x20) = v_xmm0;
    *(uint64_t *)(Arg1 + 0x30) = *(uint64_t *)(local_rsi + 0x30);
    *(uint64_t *)(v_rip + 0x889B03 + v_stack_m888 * 8) = *(uint64_t *)(v_rip + 0x889E5A + v_stack_m888 * 8);
loc_00745C45:
    if (result == 0) goto loc_00745CD5;
    Arg2 = 0;
    result = KiRcuProcessorInitialize(result, Arg2, v_rip + 8952579, *(uint8_t *)(result + 0xD1));
    result = KiFreeForceParkingData(result, Arg2, v_rip + 8952579, *(uint8_t *)(result + 0xD1));
    if ((*(uint32_t *)(v_rip + 0x7DD47D)) != 0) {
        Arg2 = 0;
        Arg1 = result;
        result = KiAllocateProcessorHiberSwapShadowStacks(Arg1, Arg2, v_rip + 8952579, *(uint8_t *)(result + 0xD1));
    }
    result = KiFreeIdleSearchStructures(result, Arg2, v_rip + 8952579, *(uint8_t *)(result + 0xD1));
    result = KiFreeStaticRescheduleContext(result, Arg2, v_rip + 8952579, *(uint8_t *)(result + 0xD1));
    result = KiFreeLocalSharedReadyQueue(result, Arg2, v_rip + 8952579, *(uint8_t *)(result + 0xD1));
    result = KiFreePrcbThreads(result, Arg2, v_rip + 8952579, *(uint8_t *)(result + 0xD1));
    result = KiFreeThreadCycleTable(result, Arg2, v_rip + 8952579, *(uint8_t *)(result + 0xD1));
    result = HvlDeleteProcessor(result, Arg2, v_rip + 8952579, *(uint8_t *)(result + 0xD1));
    result = MmDeleteProcessor(result, Arg2, v_rip + 8952579, *(uint8_t *)(result + 0xD1));
    result = EtwDeleteProcessor(result, Arg2, v_rip + 8952579, *(uint8_t *)(result + 0xD1));
    if (*(uint64_t *)(result + 0x8B50) != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(*(uint64_t *)(result + 0x8B50), Arg2, v_rip + 8952579, *(uint8_t *)(result + 0xD1));
        *(uint64_t *)(result + 0x8B50) = 0;
    }
    result = KiUnassignProcessorNumberFromPrcb(result, Arg2, v_rip + 8952579, *(uint8_t *)(result + 0xD1));
loc_00745CD5:
    if (v_stack_m870 != 0) {
        Arg1 = (uint32_t)((uint32_t)(Arg4));
        result = ExDeletePoolTagTable(Arg1, Arg2, v_rip + 8952579, *(uint8_t *)(result + 0xD1));
    }
    if (result != 0) {
        Arg3 = v_stack_m868;
        Arg1 = result;
        Arg2 = v_stack_m608;
        result = KiUnshadowProcessorAllocation(Arg1, Arg2, Arg3, *(uint8_t *)(result + 0xD1));
    }
    result = KiFreeProcessorStateInitializationParameters(v_stack_m868, Arg2, Arg3, *(uint8_t *)(result + 0xD1));
loc_00745D05:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, *(uint8_t *)(result + 0xD1));
    local_rsp = (local_rsp) + (0x880ULL);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007456C8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
