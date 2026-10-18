# KeStartAllProcessors

- RVA: `0x00C36F78`–`0x00C377BA` (길이 `2,114` bytes)
- VA: `0x0000000140C36F78`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C9FB8`
- 디코드: `494`개 명령, `2,114/2,114` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **60**; 고유 호출 대상: **52**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **29**

### Outgoing calls
- `0x00C36FC8` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00C36FEA` → [KiCompleteBootProcessorContextInitialization](../../text/5B/KiCompleteBootProcessorContextInitialization_function_005B7634.md) (function, `0x005B7634`)
- `0x00C37025` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C37047` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00C3707B` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00C3708F` → [KiComputeEstimatedMaximumProcessors](../../text/5B/KiComputeEstimatedMaximumProcessors_function_005B7800.md) (function, `0x005B7800`)
- `0x00C3709A` → [KiAllocateProcessorLookupStructures](../../text/5B/KiAllocateProcessorLookupStructures_function_005B6C8C.md) (function, `0x005B6C8C`)
- `0x00C370D3` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C37116` → [KiCreateCpuSetForProcessor](../../pagelk/B6/KiCreateCpuSetForProcessor_function_00B681A0.md) (function, `0x00B681A0`)
- `0x00C37129` → [KiComputeProcessorDataSize](../../pagelk/B6/KiComputeProcessorDataSize_function_00B6B1A8.md) (function, `0x00B6B1A8`)
- `0x00C37143` → [HvlStartBootLogicalProcessors](../../text/58/HvlStartBootLogicalProcessors_function_00584E18.md) (function, `0x00584E18`)
- `0x00C37198` → [KiQueryProcessorNode](../../text/5B/KiQueryProcessorNode_function_005BCC70.md) (function, `0x005BCC70`)
- `0x00C371B6` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00C371C2` → [ExCreatePoolTagTable](../../page/7C/ExCreatePoolTagTable_function_007C76FC.md) (function, `0x007C76FC`)
- `0x00C371E3` → [MmAllocateIndependentPagesEx](../../page/AA/MmAllocateIndependentPagesEx_function_00AA0CFC.md) (function, `0x00AA0CFC`)
- `0x00C3721F` → [KiAllocateProcessorStateInitializationParameters](../../text/5B/KiAllocateProcessorStateInitializationParameters_function_005B6F24.md) (function, `0x005B6F24`)
- `0x00C3724C` → [KiInitializeProcessorState](../../page/74/KiInitializeProcessorState_function_00747390.md) (function, `0x00747390`)
- `0x00C37279` → [KiRcuProcessorInitialize](../../text/4D/KiRcuProcessorInitialize_function_004DF7E8.md) (function, `0x004DF7E8`)
- `0x00C37288` → [HvlInitializeProcessor](../../page/71/HvlInitializeProcessor_function_0071804C.md) (function, `0x0071804C`)
- `0x00C37298` → [MmInitializeProcessor](../../pagelk/B7/MmInitializeProcessor_function_00B737F8.md) (function, `0x00B737F8`)
- `0x00C372AD` → [KiInitializePrcbContext](../../pagelk/B6/KiInitializePrcbContext_function_00B66D70.md) (function, `0x00B66D70`)
- `0x00C372BD` → [KeInitializeTimerTable](../../page/A9/KeInitializeTimerTable_function_00A9471C.md) (function, `0x00A9471C`)
- `0x00C372CD` → [EtwInitializeProcessor](../../page/7B/EtwInitializeProcessor_function_007B4EBC.md) (function, `0x007B4EBC`)
- `0x00C372DD` → [KiAllocatePrcbThreads](../../text/5B/KiAllocatePrcbThreads_function_005B6C2C.md) (function, `0x005B6C2C`)
- `0x00C372ED` → [KiAllocateLocalSharedReadyQueue](../../text/5B/KiAllocateLocalSharedReadyQueue_function_005B6BB0.md) (function, `0x005B6BB0`)
- `0x00C372FD` → [KiAllocateStaticRescheduleContext](../../text/5B/KiAllocateStaticRescheduleContext_function_005B6F98.md) (function, `0x005B6F98`)
- `0x00C3730D` → [KiAllocateIdleSearchStructures](../../text/5B/KiAllocateIdleSearchStructures_function_005B6A04.md) (function, `0x005B6A04`)
- `0x00C3731D` → [KiAllocateForceParkingData](../../text/5C/KiAllocateForceParkingData_function_005C96C8.md) (function, `0x005C96C8`)
- `0x00C3732D` → [VmInitializeProcessor](../../pagelk/B7/VmInitializeProcessor_function_00B7E858.md) (function, `0x00B7E858`)
- `0x00C37348` → [HalStartNextProcessor](../../text/54/HalStartNextProcessor_function_005479B0.md) (function, `0x005479B0`)
- `0x00C37368` → [KeYieldProcessorEx](../../text/3F/KeYieldProcessorEx_function_003FBD00.md) (function, `0x003FBD00`)
- `0x00C37383` → [KiConfigureProcessorBlock](../../pagelk/B6/KiConfigureProcessorBlock_function_00B663E8.md) (function, `0x00B663E8`)
- `0x00C37391` → [KiUpdateProcessorCount](../../pagelk/B6/KiUpdateProcessorCount_function_00B65D18.md) (function, `0x00B65D18`)
- `0x00C3742E` → [KiRcuProcessorInitialize](../../text/4D/KiRcuProcessorInitialize_function_004DF7E8.md) (function, `0x004DF7E8`)
- `0x00C37436` → [KiFreeForceParkingData](../../text/5C/KiFreeForceParkingData_function_005C99B8.md) (function, `0x005C99B8`)
- `0x00C3743E` → [KiFreeIdleSearchStructures](../../text/5B/KiFreeIdleSearchStructures_function_005B7E88.md) (function, `0x005B7E88`)
- `0x00C37446` → [KiFreeStaticRescheduleContext](../../text/5B/KiFreeStaticRescheduleContext_function_005B8120.md) (function, `0x005B8120`)
- `0x00C3744E` → [KiFreeLocalSharedReadyQueue](../../text/5B/KiFreeLocalSharedReadyQueue_function_005B7F0C.md) (function, `0x005B7F0C`)
- `0x00C37456` → [KiFreePrcbThreads](../../text/5B/KiFreePrcbThreads_function_005B7F40.md) (function, `0x005B7F40`)
- `0x00C3745E` → [HvlDeleteProcessor](../../page/71/HvlDeleteProcessor_function_00717FA4.md) (function, `0x00717FA4`)
- `0x00C37466` → [MmDeleteProcessor](../../page/7F/MmDeleteProcessor_function_007F8FB4.md) (function, `0x007F8FB4`)
- `0x00C3746E` → [EtwDeleteProcessor](../../page/7B/EtwDeleteProcessor_function_007B4CC0.md) (function, `0x007B4CC0`)
- `0x00C37475` → [ExDeletePoolTagTable](../../text/65/ExDeletePoolTagTable_function_00655F88.md) (function, `0x00655F88`)
- `0x00C37489` → [KiUnshadowProcessorAllocation](../../pagelk/B6/KiUnshadowProcessorAllocation_function_00B6B0E8.md) (function, `0x00B6B0E8`)
- `0x00C374CB` → [KiFreeProcessorStateInitializationParameters](../../text/5B/KiFreeProcessorStateInitializationParameters_function_005B80A8.md) (function, `0x005B80A8`)
- `0x00C374F4` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C37553` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C37603` → [KeInitializeSchedulerSubNodeEnumerationContext](../../text/41/KeInitializeSchedulerSubNodeEnumerationContext_function_0041E4B0.md) (function, `0x0041E4B0`)
- `0x00C37626` → [KeEnumerateNextSchedulerSubNodeInNode](../../text/25/KeEnumerateNextSchedulerSubNodeInNode_function_002566D8.md) (function, `0x002566D8`)
- `0x00C37664` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00C376DE` → [PoInitHeteroDetection](PoInitHeteroDetection_function_00C3D244.md) (function, `0x00C3D244`)
- `0x00C376EC` → [KeBugCheck](../../text/4F/KeBugCheck_function_004FD640.md) (function, `0x004FD640`)
- `0x00C37708` → [KiInitializeThreadCycleTable](../../pagelk/B6/KiInitializeThreadCycleTable_function_00B66B10.md) (function, `0x00B66B10`)
- `0x00C37729` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C3772F` → [KiConfigureAllSchedulingInformation](KiConfigureAllSchedulingInformation_function_00C380D0.md) (function, `0x00C380D0`)
- `0x00C37740` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00C37751` → [KeQueryActiveProcessorCountEx](../../text/24/KeQueryActiveProcessorCountEx_function_00249EF0.md) (function, `0x00249EF0`)
- `0x00C37769` → [KeWakeAddressAll](../../text/21/KeWakeAddressAll_function_00217C20.md) (function, `0x00217C20`)
- `0x00C37778` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00C377B4` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)

### Direct callers
- [Phase1InitializationDiscard](../C1/Phase1InitializationDiscard_function_00C1C728.md) at `0x00C1D047`

### Static image references
- `0x00C36F9E` → RVA `0x00E0A740` (`.data`; read)
- `0x00C3701F` → RVA `0x00E66960` (`.data`; write)
- `0x00C3702A` → RVA `0x00FD9EA8` (`PAGEDATA`; write)
- `0x00C3703A` → RVA `0x00E66960` (`.data`; read)
- `0x00C37051` → RVA `0x00FC6C68` (`ALMOSTRO`; read)
- `0x00C37059` → RVA `0x00FC6C68` (`ALMOSTRO`; write)
- `0x00C3706E` → RVA `0x00FC6C50` (`ALMOSTRO`; write)
- `0x00C370A7` → RVA `0x00FC6AE8` (`ALMOSTRO`; write)
- `0x00C370AD` → RVA `0x00FC5014` (`ALMOSTRO`; read)
- `0x00C370E1` → RVA `0x00FC8C40` (`ALMOSTRO`; read)
- `0x00C370E8` → RVA `0x00FC6E18` (`ALMOSTRO`; write)
- `0x00C370F8` → RVA `0x00FC6E20` (`ALMOSTRO`; write)
- `0x00C37102` → RVA `0x00FC72F8` (`ALMOSTRO`; write)
- `0x00C37110` → RVA `0x00FC6FD4` (`ALMOSTRO`; write)
- `0x00C37155` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x00C3716E` → RVA `0x00FC6A80` (`ALMOSTRO`; read)
- `0x00C37236` → RVA `0x00FC6B20` (`ALMOSTRO`; read)
- `0x00C3748E` → RVA `0x00F231B0` (`.data`; read)
- `0x00C374AE` → RVA `0x00F231B8` (`.data`; read)
- `0x00C37507` → RVA `0x00FC5000` (`ALMOSTRO`; read)
- `0x00C375E4` → RVA `0x00FCF6C0` (`CACHEALI`; read)
- `0x00C37669` → RVA `0x00FC6E5C` (`ALMOSTRO`; read)
- `0x00C3767D` → RVA `0x00FC6AA4` (`ALMOSTRO`; read)
- `0x00C376D0` → RVA `0x00FC5018` (`ALMOSTRO`; read)
- `0x00C376D7` → RVA `0x00FC5014` (`ALMOSTRO`; write)
- `0x00C37734` → RVA `0x00E00910` (`.data`; read)
- `0x00C3774A` → RVA `0x00FC6E74` (`ALMOSTRO`; write)
- `0x00C37756` → RVA `0x00FC6FDC` (`ALMOSTRO`; write)
- `0x00C3775C` → RVA `0x00FC6C50` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **58**
  - `0x00C36FC8` → [memset](../../text/6C/memset_function_006C6C40.md) (`INIT` → `.text`)
  - `0x00C36FEA` → [KiCompleteBootProcessorContextInitialization](../../text/5B/KiCompleteBootProcessorContextInitialization_function_005B7634.md) (`INIT` → `.text`)
  - `0x00C37025` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C37047` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`INIT` → `.text`)
  - `0x00C3707B` → [memset](../../text/6C/memset_function_006C6C40.md) (`INIT` → `.text`)
  - `0x00C3708F` → [KiComputeEstimatedMaximumProcessors](../../text/5B/KiComputeEstimatedMaximumProcessors_function_005B7800.md) (`INIT` → `.text`)
  - `0x00C3709A` → [KiAllocateProcessorLookupStructures](../../text/5B/KiAllocateProcessorLookupStructures_function_005B6C8C.md) (`INIT` → `.text`)
  - `0x00C370D3` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C37116` → [KiCreateCpuSetForProcessor](../../pagelk/B6/KiCreateCpuSetForProcessor_function_00B681A0.md) (`INIT` → `PAGELK`)
  - `0x00C37129` → [KiComputeProcessorDataSize](../../pagelk/B6/KiComputeProcessorDataSize_function_00B6B1A8.md) (`INIT` → `PAGELK`)
  - `0x00C37143` → [HvlStartBootLogicalProcessors](../../text/58/HvlStartBootLogicalProcessors_function_00584E18.md) (`INIT` → `.text`)
  - `0x00C37198` → [KiQueryProcessorNode](../../text/5B/KiQueryProcessorNode_function_005BCC70.md) (`INIT` → `.text`)
  - `0x00C371B6` → [memset](../../text/6C/memset_function_006C6C40.md) (`INIT` → `.text`)
  - `0x00C371C2` → [ExCreatePoolTagTable](../../page/7C/ExCreatePoolTagTable_function_007C76FC.md) (`INIT` → `PAGE`)
  - `0x00C371E3` → [MmAllocateIndependentPagesEx](../../page/AA/MmAllocateIndependentPagesEx_function_00AA0CFC.md) (`INIT` → `PAGE`)
  - `0x00C3721F` → [KiAllocateProcessorStateInitializationParameters](../../text/5B/KiAllocateProcessorStateInitializationParameters_function_005B6F24.md) (`INIT` → `.text`)
  - `0x00C3724C` → [KiInitializeProcessorState](../../page/74/KiInitializeProcessorState_function_00747390.md) (`INIT` → `PAGE`)
  - `0x00C37279` → [KiRcuProcessorInitialize](../../text/4D/KiRcuProcessorInitialize_function_004DF7E8.md) (`INIT` → `.text`)
  - `0x00C37288` → [HvlInitializeProcessor](../../page/71/HvlInitializeProcessor_function_0071804C.md) (`INIT` → `PAGE`)
  - `0x00C37298` → [MmInitializeProcessor](../../pagelk/B7/MmInitializeProcessor_function_00B737F8.md) (`INIT` → `PAGELK`)
  - `0x00C372AD` → [KiInitializePrcbContext](../../pagelk/B6/KiInitializePrcbContext_function_00B66D70.md) (`INIT` → `PAGELK`)
  - `0x00C372BD` → [KeInitializeTimerTable](../../page/A9/KeInitializeTimerTable_function_00A9471C.md) (`INIT` → `PAGE`)
  - `0x00C372CD` → [EtwInitializeProcessor](../../page/7B/EtwInitializeProcessor_function_007B4EBC.md) (`INIT` → `PAGE`)
  - `0x00C372DD` → [KiAllocatePrcbThreads](../../text/5B/KiAllocatePrcbThreads_function_005B6C2C.md) (`INIT` → `.text`)
  - `0x00C372ED` → [KiAllocateLocalSharedReadyQueue](../../text/5B/KiAllocateLocalSharedReadyQueue_function_005B6BB0.md) (`INIT` → `.text`)
  - `0x00C372FD` → [KiAllocateStaticRescheduleContext](../../text/5B/KiAllocateStaticRescheduleContext_function_005B6F98.md) (`INIT` → `.text`)
  - `0x00C3730D` → [KiAllocateIdleSearchStructures](../../text/5B/KiAllocateIdleSearchStructures_function_005B6A04.md) (`INIT` → `.text`)
  - `0x00C3731D` → [KiAllocateForceParkingData](../../text/5C/KiAllocateForceParkingData_function_005C96C8.md) (`INIT` → `.text`)
  - `0x00C3732D` → [VmInitializeProcessor](../../pagelk/B7/VmInitializeProcessor_function_00B7E858.md) (`INIT` → `PAGELK`)
  - `0x00C37348` → [HalStartNextProcessor](../../text/54/HalStartNextProcessor_function_005479B0.md) (`INIT` → `.text`)
  - `0x00C37368` → [KeYieldProcessorEx](../../text/3F/KeYieldProcessorEx_function_003FBD00.md) (`INIT` → `.text`)
  - `0x00C37383` → [KiConfigureProcessorBlock](../../pagelk/B6/KiConfigureProcessorBlock_function_00B663E8.md) (`INIT` → `PAGELK`)
  - `0x00C37391` → [KiUpdateProcessorCount](../../pagelk/B6/KiUpdateProcessorCount_function_00B65D18.md) (`INIT` → `PAGELK`)
  - `0x00C3742E` → [KiRcuProcessorInitialize](../../text/4D/KiRcuProcessorInitialize_function_004DF7E8.md) (`INIT` → `.text`)
  - `0x00C37436` → [KiFreeForceParkingData](../../text/5C/KiFreeForceParkingData_function_005C99B8.md) (`INIT` → `.text`)
  - `0x00C3743E` → [KiFreeIdleSearchStructures](../../text/5B/KiFreeIdleSearchStructures_function_005B7E88.md) (`INIT` → `.text`)
  - `0x00C37446` → [KiFreeStaticRescheduleContext](../../text/5B/KiFreeStaticRescheduleContext_function_005B8120.md) (`INIT` → `.text`)
  - `0x00C3744E` → [KiFreeLocalSharedReadyQueue](../../text/5B/KiFreeLocalSharedReadyQueue_function_005B7F0C.md) (`INIT` → `.text`)
  - `0x00C37456` → [KiFreePrcbThreads](../../text/5B/KiFreePrcbThreads_function_005B7F40.md) (`INIT` → `.text`)
  - `0x00C3745E` → [HvlDeleteProcessor](../../page/71/HvlDeleteProcessor_function_00717FA4.md) (`INIT` → `PAGE`)
  - `0x00C37466` → [MmDeleteProcessor](../../page/7F/MmDeleteProcessor_function_007F8FB4.md) (`INIT` → `PAGE`)
  - `0x00C3746E` → [EtwDeleteProcessor](../../page/7B/EtwDeleteProcessor_function_007B4CC0.md) (`INIT` → `PAGE`)
  - `0x00C37475` → [ExDeletePoolTagTable](../../text/65/ExDeletePoolTagTable_function_00655F88.md) (`INIT` → `.text`)
  - `0x00C37489` → [KiUnshadowProcessorAllocation](../../pagelk/B6/KiUnshadowProcessorAllocation_function_00B6B0E8.md) (`INIT` → `PAGELK`)
  - `0x00C374CB` → [KiFreeProcessorStateInitializationParameters](../../text/5B/KiFreeProcessorStateInitializationParameters_function_005B80A8.md) (`INIT` → `.text`)
  - `0x00C374F4` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C37553` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C37603` → [KeInitializeSchedulerSubNodeEnumerationContext](../../text/41/KeInitializeSchedulerSubNodeEnumerationContext_function_0041E4B0.md) (`INIT` → `.text`)
  - `0x00C37626` → [KeEnumerateNextSchedulerSubNodeInNode](../../text/25/KeEnumerateNextSchedulerSubNodeInNode_function_002566D8.md) (`INIT` → `.text`)
  - `0x00C37664` → [memset](../../text/6C/memset_function_006C6C40.md) (`INIT` → `.text`)
  - `0x00C376EC` → [KeBugCheck](../../text/4F/KeBugCheck_function_004FD640.md) (`INIT` → `.text`)
  - `0x00C37708` → [KiInitializeThreadCycleTable](../../pagelk/B6/KiInitializeThreadCycleTable_function_00B66B10.md) (`INIT` → `PAGELK`)
  - `0x00C37729` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C37740` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`INIT` → `.text`)
  - `0x00C37751` → [KeQueryActiveProcessorCountEx](../../text/24/KeQueryActiveProcessorCountEx_function_00249EF0.md) (`INIT` → `.text`)
  - `0x00C37769` → [KeWakeAddressAll](../../text/21/KeWakeAddressAll_function_00217C20.md) (`INIT` → `.text`)
  - `0x00C37778` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`INIT` → `.text`)
  - `0x00C377B4` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C36F78  48 8B C4                        mov rax, rsp
00C36F7B  48 89 58 08                     mov qword ptr [rax + 8], rbx
00C36F7F  48 89 70 10                     mov qword ptr [rax + 0x10], rsi
00C36F83  48 89 78 18                     mov qword ptr [rax + 0x18], rdi
00C36F87  55                              push rbp
00C36F88  41 54                           push r12
00C36F8A  41 55                           push r13
00C36F8C  41 56                           push r14
00C36F8E  41 57                           push r15
00C36F90  48 8D A8 88 F9 FF FF            lea rbp, [rax - 0x678]
00C36F97  48 81 EC 50 07 00 00            sub rsp, 0x750
00C36F9E  48 8B 05 9B 37 1D 00            mov rax, qword ptr [rip + 0x1d379b]
00C36FA5  48 33 C4                        xor rax, rsp
00C36FA8  48 89 85 40 06 00 00            mov qword ptr [rbp + 0x640], rax
00C36FAF  33 C0                           xor eax, eax
00C36FB1  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
00C36FB6  33 FF                           xor edi, edi
00C36FB8  89 44 24 74                     mov dword ptr [rsp + 0x74], eax
00C36FBC  33 D2                           xor edx, edx
00C36FBE  89 7C 24 38                     mov dword ptr [rsp + 0x38], edi
00C36FC2  41 B8 E4 00 00 00               mov r8d, 0xe4
00C36FC8  E8 73 FC A8 FF                  call 0x1406c6c40
00C36FCD  89 7C 24 48                     mov dword ptr [rsp + 0x48], edi
00C36FD1  89 7C 24 3C                     mov dword ptr [rsp + 0x3c], edi
00C36FD5  66 89 7C 24 30                  mov word ptr [rsp + 0x30], di
00C36FDA  89 7C 24 34                     mov dword ptr [rsp + 0x34], edi
00C36FDE  89 7C 24 4C                     mov dword ptr [rsp + 0x4c], edi
00C36FE2  89 7C 24 40                     mov dword ptr [rsp + 0x40], edi
00C36FE6  89 7C 24 44                     mov dword ptr [rsp + 0x44], edi
00C36FEA  E8 45 06 98 FF                  call 0x1405b7634
00C36FEF  85 C0                           test eax, eax
00C36FF1  0F 88 AA 07 00 00               js 0x140c377a1
00C36FF7  65 48 8B 04 25 18 00 00 00      mov rax, qword ptr gs:[0x18]
00C37000  BE 4B 65 20 20                  mov esi, 0x2020654b
00C37005  44 8B C6                        mov r8d, esi
00C37008  B9 00 01 00 00                  mov ecx, 0x100
00C3700D  48 8B 98 E8 02 00 00            mov rbx, qword ptr [rax + 0x2e8]
00C37014  0F B7 80 E6 02 00 00            movzx eax, word ptr [rax + 0x2e6]
00C3701B  FF C0                           inc eax
00C3701D  8B D0                           mov edx, eax
00C3701F  89 05 3B F9 22 00               mov dword ptr [rip + 0x22f93b], eax
00C37025  E8 C6 B0 F4 FF                  call 0x140b820f0
00C3702A  48 89 05 77 2E 3A 00            mov qword ptr [rip + 0x3a2e77], rax
00C37031  48 85 C0                        test rax, rax
00C37034  0F 84 67 07 00 00               je 0x140c377a1
00C3703A  44 8B 05 1F F9 22 00            mov r8d, dword ptr [rip + 0x22f91f]
00C37041  48 8B D3                        mov rdx, rbx
00C37044  48 8B C8                        mov rcx, rax
00C37047  E8 F4 F7 A8 FF                  call 0x1406c6840
00C3704C  B8 00 08 00 00                  mov eax, 0x800
00C37051  39 05 11 FC 38 00               cmp dword ptr [rip + 0x38fc11], eax
00C37057  76 06                           jbe 0x140c3705f
00C37059  89 05 09 FC 38 00               mov dword ptr [rip + 0x38fc09], eax
00C3705F  41 BD 01 00 00 00               mov r13d, 1
00C37065  48 8D 8D 80 00 00 00            lea rcx, [rbp + 0x80]
00C3706C  33 D2                           xor edx, edx
00C3706E  44 89 2D DB FB 38 00            mov dword ptr [rip + 0x38fbdb], r13d
00C37075  41 B8 C0 05 00 00               mov r8d, 0x5c0
00C3707B  E8 C0 FB A8 FF                  call 0x1406c6c40
00C37080  4C 8D 44 24 3C                  lea r8, [rsp + 0x3c]
00C37085  48 8D 54 24 38                  lea rdx, [rsp + 0x38]
00C3708A  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
00C3708F  E8 6C 07 98 FF                  call 0x1405b7800
00C37094  8B 5C 24 3C                     mov ebx, dword ptr [rsp + 0x3c]
00C37098  8B CB                           mov ecx, ebx
00C3709A  E8 ED FB 97 FF                  call 0x1405b6c8c
00C3709F  85 C0                           test eax, eax
00C370A1  0F 88 FA 06 00 00               js 0x140c377a1
00C370A7  89 1D 3B FA 38 00               mov dword ptr [rip + 0x38fa3b], ebx
00C370AD  0F B7 1D 60 DF 38 00            movzx ebx, word ptr [rip + 0x38df60]
00C370B4  41 3B DD                        cmp ebx, r13d
00C370B7  75 06                           jne 0x140c370bf
00C370B9  8B 5C 24 38                     mov ebx, dword ptr [rsp + 0x38]
00C370BD  EB 03                           jmp 0x140c370c2
00C370BF  C1 E3 06                        shl ebx, 6
00C370C2  8B D3                           mov edx, ebx
00C370C4  41 BE 40 00 00 00               mov r14d, 0x40
00C370CA  C1 E2 05                        shl edx, 5
00C370CD  41 8B CE                        mov ecx, r14d
00C370D0  44 8B C6                        mov r8d, esi
00C370D3  E8 18 B0 F4 FF                  call 0x140b820f0
00C370D8  48 85 C0                        test rax, rax
00C370DB  0F 84 C0 06 00 00               je 0x140c377a1
00C370E1  48 8B 0D 58 1B 39 00            mov rcx, qword ptr [rip + 0x391b58]
00C370E8  48 89 05 29 FD 38 00            mov qword ptr [rip + 0x38fd29], rax
00C370EF  8B D3                           mov edx, ebx
00C370F1  48 C1 E2 03                     shl rdx, 3
00C370F5  48 03 C2                        add rax, rdx
00C370F8  48 89 05 21 FD 38 00            mov qword ptr [rip + 0x38fd21], rax
00C370FF  48 03 C2                        add rax, rdx
00C37102  48 89 05 EF 01 39 00            mov qword ptr [rip + 0x3901ef], rax
00C37109  8D 04 DD 00 00 00 00            lea eax, [rbx*8]
00C37110  89 05 BE FE 38 00               mov dword ptr [rip + 0x38febe], eax
00C37116  E8 85 10 F3 FF                  call 0x140b681a0
00C3711B  8B 4C 24 38                     mov ecx, dword ptr [rsp + 0x38]
00C3711F  4C 8D 44 24 44                  lea r8, [rsp + 0x44]
00C37124  48 8D 54 24 40                  lea rdx, [rsp + 0x40]
00C37129  E8 7A 40 F3 FF                  call 0x140b6b1a8
00C3712E  8B 4C 24 40                     mov ecx, dword ptr [rsp + 0x40]
00C37132  48 89 4C 24 58                  mov qword ptr [rsp + 0x58], rcx
00C37137  8B 4C 24 44                     mov ecx, dword ptr [rsp + 0x44]
00C3713B  48 89 4C 24 60                  mov qword ptr [rsp + 0x60], rcx
00C37140  44 8B E0                        mov r12d, eax
00C37143  E8 D0 DC 94 FF                  call 0x140584e18
00C37148  85 C0                           test eax, eax
00C3714A  0F 88 51 06 00 00               js 0x140c377a1
00C37150  44 8B FF                        mov r15d, edi
00C37153  8B F7                           mov esi, edi
00C37155  48 8D 1D A4 8E 3C FF            lea rbx, [rip - 0xc3715c]
00C3715C  B9 FF FF 00 00                  mov ecx, 0xffff
00C37161  41 81 FF FF 07 00 00            cmp r15d, 0x7ff
00C37168  0F 83 8C 03 00 00               jae 0x140c374fa
00C3716E  8B 05 0C F9 38 00               mov eax, dword ptr [rip + 0x38f90c]
00C37174  3B 44 24 48                     cmp eax, dword ptr [rsp + 0x48]
00C37178  0F 83 7C 03 00 00               jae 0x140c374fa
00C3717E  83 4C 24 34 FF                  or dword ptr [rsp + 0x34], 0xffffffff
00C37183  4C 8D 44 24 30                  lea r8, [rsp + 0x30]
00C37188  66 89 4C 24 30                  mov word ptr [rsp + 0x30], cx
00C3718D  48 8D 54 24 34                  lea rdx, [rsp + 0x34]
00C37192  45 03 FD                        add r15d, r13d
00C37195  41 8B CF                        mov ecx, r15d
00C37198  E8 D3 5A 98 FF                  call 0x1405bcc70
00C3719D  B9 FF FF 00 00                  mov ecx, 0xffff
00C371A2  85 C0                           test eax, eax
00C371A4  75 BB                           jne 0x140c37161
00C371A6  33 D2                           xor edx, edx
00C371A8  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
00C371AD  41 B8 E8 00 00 00               mov r8d, 0xe8
00C371B3  41 03 F5                        add esi, r13d
00C371B6  E8 85 FA A8 FF                  call 0x1406c6c40
00C371BB  0F B7 54 24 30                  movzx edx, word ptr [rsp + 0x30]
00C371C0  8B CE                           mov ecx, esi
00C371C2  E8 35 05 B9 FF                  call 0x1407c76fc
00C371C7  48 85 C0                        test rax, rax
00C371CA  0F 84 D1 05 00 00               je 0x140c377a1
00C371D0  0F B7 54 24 30                  movzx edx, word ptr [rsp + 0x30]
00C371D5  4C 8D 44 24 58                  lea r8, [rsp + 0x58]
00C371DA  49 8B CC                        mov rcx, r12
00C371DD  41 B9 02 00 00 00               mov r9d, 2
00C371E3  E8 14 9B E6 FF                  call 0x140aa0cfc
00C371E8  48 85 C0                        test rax, rax
00C371EB  0F 84 B0 05 00 00               je 0x140c377a1
00C371F1  0F B7 54 24 30                  movzx edx, word ptr [rsp + 0x30]
00C371F6  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
00C371FB  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
00C37200  8B 44 24 38                     mov eax, dword ptr [rsp + 0x38]
00C37204  89 45 8C                        mov dword ptr [rbp - 0x74], eax
00C37207  8B 44 24 40                     mov eax, dword ptr [rsp + 0x40]
00C3720B  89 45 94                        mov dword ptr [rbp - 0x6c], eax
00C3720E  8B 44 24 44                     mov eax, dword ptr [rsp + 0x44]
00C37212  89 45 98                        mov dword ptr [rbp - 0x68], eax
00C37215  44 89 65 80                     mov dword ptr [rbp - 0x80], r12d
00C37219  89 55 84                        mov dword ptr [rbp - 0x7c], edx
00C3721C  89 75 88                        mov dword ptr [rbp - 0x78], esi
00C3721F  E8 00 FD 97 FF                  call 0x1405b6f24
00C37224  85 C0                           test eax, eax
00C37226  0F 88 75 05 00 00               js 0x140c377a1
00C3722C  0F B7 44 24 30                  movzx eax, word ptr [rsp + 0x30]
00C37231  4C 8D 44 24 70                  lea r8, [rsp + 0x70]
00C37236  48 8B 15 E3 F8 38 00            mov rdx, qword ptr [rip + 0x38f8e3]
00C3723D  48 8D 8D 80 00 00 00            lea rcx, [rbp + 0x80]
00C37244  4C 8B AC C3 C0 F6 FC 00         mov r13, qword ptr [rbx + rax*8 + 0xfcf6c0]
00C3724C  E8 3F 01 B1 FF                  call 0x140747390
00C37251  48 8B D8                        mov rbx, rax
00C37254  48 85 C0                        test rax, rax
00C37257  0F 84 44 05 00 00               je 0x140c377a1
00C3725D  0F B7 4C 24 30                  movzx ecx, word ptr [rsp + 0x30]
00C37262  48 8D 3D 97 8D 3C FF            lea rdi, [rip - 0xc37269]
00C37269  BA 01 00 00 00                  mov edx, 1
00C3726E  48 8B BC CF C0 F6 FC 00         mov rdi, qword ptr [rdi + rcx*8 + 0xfcf6c0]
00C37276  48 8B C8                        mov rcx, rax
00C37279  E8 6A 85 8A FF                  call 0x1404df7e8
00C3727E  44 8B 44 24 34                  mov r8d, dword ptr [rsp + 0x34]
00C37283  8B D6                           mov edx, esi
00C37285  48 8B CB                        mov rcx, rbx
00C37288  E8 BF 0D AE FF                  call 0x14071804c
00C3728D  85 C0                           test eax, eax
00C3728F  0F 85 0A 05 00 00               jne 0x140c3779f
00C37295  48 8B CB                        mov rcx, rbx
00C37298  E8 5B C5 F3 FF                  call 0x140b737f8
00C3729D  85 C0                           test eax, eax
00C3729F  0F 84 FA 04 00 00               je 0x140c3779f
00C372A5  0F B7 54 24 30                  movzx edx, word ptr [rsp + 0x30]
00C372AA  48 8B CB                        mov rcx, rbx
00C372AD  E8 BE FA F2 FF                  call 0x140b66d70
00C372B2  85 C0                           test eax, eax
00C372B4  0F 88 E5 04 00 00               js 0x140c3779f
00C372BA  48 8B CB                        mov rcx, rbx
00C372BD  E8 5A D4 E5 FF                  call 0x140a9471c
00C372C2  85 C0                           test eax, eax
00C372C4  0F 88 D5 04 00 00               js 0x140c3779f
00C372CA  48 8B CB                        mov rcx, rbx
00C372CD  E8 EA DB B7 FF                  call 0x1407b4ebc
00C372D2  85 C0                           test eax, eax
00C372D4  0F 88 C5 04 00 00               js 0x140c3779f
00C372DA  48 8B CB                        mov rcx, rbx
00C372DD  E8 4A F9 97 FF                  call 0x1405b6c2c
00C372E2  85 C0                           test eax, eax
00C372E4  0F 88 B5 04 00 00               js 0x140c3779f
00C372EA  48 8B CB                        mov rcx, rbx
00C372ED  E8 BE F8 97 FF                  call 0x1405b6bb0
00C372F2  85 C0                           test eax, eax
00C372F4  0F 88 A5 04 00 00               js 0x140c3779f
00C372FA  48 8B CB                        mov rcx, rbx
00C372FD  E8 96 FC 97 FF                  call 0x1405b6f98
00C37302  85 C0                           test eax, eax
00C37304  0F 88 95 04 00 00               js 0x140c3779f
00C3730A  48 8B CB                        mov rcx, rbx
00C3730D  E8 F2 F6 97 FF                  call 0x1405b6a04
00C37312  85 C0                           test eax, eax
00C37314  0F 88 85 04 00 00               js 0x140c3779f
00C3731A  48 8B CB                        mov rcx, rbx
00C3731D  E8 A6 23 99 FF                  call 0x1405c96c8
00C37322  85 C0                           test eax, eax
00C37324  0F 88 75 04 00 00               js 0x140c3779f
00C3732A  48 8B CB                        mov rcx, rbx
00C3732D  E8 26 75 F4 FF                  call 0x140b7e858
00C37332  85 C0                           test eax, eax
00C37334  0F 88 65 04 00 00               js 0x140c3779f
00C3733A  44 8B 44 24 34                  mov r8d, dword ptr [rsp + 0x34]
00C3733F  48 8D 8D 80 00 00 00            lea rcx, [rbp + 0x80]
00C37346  8B D6                           mov edx, esi
00C37348  E8 63 06 91 FF                  call 0x1405479b0
00C3734D  83 F8 03                        cmp eax, 3
00C37350  0F 84 80 01 00 00               je 0x140c374d6
00C37356  83 F8 04                        cmp eax, 4
00C37359  75 46                           jne 0x140c373a1
00C3735B  33 FF                           xor edi, edi
00C3735D  89 7C 24 4C                     mov dword ptr [rsp + 0x4c], edi
00C37361  EB 0A                           jmp 0x140c3736d
00C37363  48 8D 4C 24 4C                  lea rcx, [rsp + 0x4c]
00C37368  E8 93 49 7C FF                  call 0x1403fbd00
00C3736D  48 8B 05 AC F7 38 00            mov rax, qword ptr [rip + 0x38f7ac]
00C37374  48 8B 80 88 00 00 00            mov rax, qword ptr [rax + 0x88]
00C3737B  48 85 C0                        test rax, rax
00C3737E  75 E3                           jne 0x140c37363
00C37380  48 8B CB                        mov rcx, rbx
00C37383  E8 60 F0 F2 FF                  call 0x140b663e8
00C37388  0F B6 93 D0 00 00 00            movzx edx, byte ptr [rbx + 0xd0]
00C3738F  8B CE                           mov ecx, esi
00C37391  E8 82 E9 F2 FF                  call 0x140b65d18
00C37396  41 BD 01 00 00 00               mov r13d, 1
00C3739C  E9 B4 FD FF FF                  jmp 0x140c37155
00C373A1  B8 06 00 00 00                  mov eax, 6
00C373A6  49 8B CD                        mov rcx, r13
00C373A9  44 8D 60 7A                     lea r12d, [rax + 0x7a]
00C373AD  0F 10 07                        movups xmm0, xmmword ptr [rdi]
00C373B0  0F 11 01                        movups xmmword ptr [rcx], xmm0
00C373B3  0F 10 4F 10                     movups xmm1, xmmword ptr [rdi + 0x10]
00C373B7  0F 11 49 10                     movups xmmword ptr [rcx + 0x10], xmm1
00C373BB  0F 10 47 20                     movups xmm0, xmmword ptr [rdi + 0x20]
00C373BF  0F 11 41 20                     movups xmmword ptr [rcx + 0x20], xmm0
00C373C3  0F 10 4F 30                     movups xmm1, xmmword ptr [rdi + 0x30]
00C373C7  0F 11 49 30                     movups xmmword ptr [rcx + 0x30], xmm1
00C373CB  0F 10 47 40                     movups xmm0, xmmword ptr [rdi + 0x40]
00C373CF  0F 11 41 40                     movups xmmword ptr [rcx + 0x40], xmm0
00C373D3  0F 10 4F 50                     movups xmm1, xmmword ptr [rdi + 0x50]
00C373D7  0F 11 49 50                     movups xmmword ptr [rcx + 0x50], xmm1
00C373DB  0F 10 47 60                     movups xmm0, xmmword ptr [rdi + 0x60]
00C373DF  0F 11 41 60                     movups xmmword ptr [rcx + 0x60], xmm0
00C373E3  49 03 CC                        add rcx, r12
00C373E6  0F 10 4F 70                     movups xmm1, xmmword ptr [rdi + 0x70]
00C373EA  49 03 FC                        add rdi, r12
00C373ED  0F 11 49 F0                     movups xmmword ptr [rcx - 0x10], xmm1
00C373F1  48 83 E8 01                     sub rax, 1
00C373F5  75 B6                           jne 0x140c373ad
00C373F7  0F 10 07                        movups xmm0, xmmword ptr [rdi]
00C373FA  4C 8D 3D FF 8B 3C FF            lea r15, [rip - 0xc37401]
00C37401  33 D2                           xor edx, edx
00C37403  0F 11 01                        movups xmmword ptr [rcx], xmm0
00C37406  0F 10 4F 10                     movups xmm1, xmmword ptr [rdi + 0x10]
00C3740A  0F 11 49 10                     movups xmmword ptr [rcx + 0x10], xmm1
00C3740E  0F 10 47 20                     movups xmm0, xmmword ptr [rdi + 0x20]
00C37412  0F 11 41 20                     movups xmmword ptr [rcx + 0x20], xmm0
00C37416  48 8B 47 30                     mov rax, qword ptr [rdi + 0x30]
00C3741A  48 89 41 30                     mov qword ptr [rcx + 0x30], rax
00C3741E  48 8B CB                        mov rcx, rbx
00C37421  0F B7 44 24 30                  movzx eax, word ptr [rsp + 0x30]
00C37426  4D 89 AC C7 C0 F6 FC 00         mov qword ptr [r15 + rax*8 + 0xfcf6c0], r13
00C3742E  E8 B5 83 8A FF                  call 0x1404df7e8
00C37433  48 8B CB                        mov rcx, rbx
00C37436  E8 7D 25 99 FF                  call 0x1405c99b8
00C3743B  48 8B CB                        mov rcx, rbx
00C3743E  E8 45 0A 98 FF                  call 0x1405b7e88
00C37443  48 8B CB                        mov rcx, rbx
00C37446  E8 D5 0C 98 FF                  call 0x1405b8120
00C3744B  48 8B CB                        mov rcx, rbx
00C3744E  E8 B9 0A 98 FF                  call 0x1405b7f0c
00C37453  48 8B CB                        mov rcx, rbx
00C37456  E8 E5 0A 98 FF                  call 0x1405b7f40
00C3745B  48 8B CB                        mov rcx, rbx
00C3745E  E8 41 0B AE FF                  call 0x140717fa4
00C37463  48 8B CB                        mov rcx, rbx
00C37466  E8 49 1B BC FF                  call 0x1407f8fb4
00C3746B  48 8B CB                        mov rcx, rbx
00C3746E  E8 4D D8 B7 FF                  call 0x1407b4cc0
00C37473  8B CE                           mov ecx, esi
00C37475  E8 0E EB A1 FF                  call 0x140655f88
00C3747A  4C 8D 44 24 70                  lea r8, [rsp + 0x70]
00C3747F  48 8B CB                        mov rcx, rbx
00C37482  48 8D 95 80 00 00 00            lea rdx, [rbp + 0x80]
00C37489  E8 5A 3C F3 FF                  call 0x140b6b0e8
00C3748E  48 8B 05 1B BD 2E 00            mov rax, qword ptr [rip + 0x2ebd1b]
00C37495  33 FF                           xor edi, edi
00C37497  8B 4B 24                        mov ecx, dword ptr [rbx + 0x24]
00C3749A  44 0F B6 83 D1 00 00 00         movzx r8d, byte ptr [rbx + 0xd1]
00C374A2  0F B6 93 D0 00 00 00            movzx edx, byte ptr [rbx + 0xd0]
00C374A9  89 3C 88                        mov dword ptr [rax + rcx*4], edi
00C374AC  8B CA                           mov ecx, edx
00C374AE  48 8B 05 03 BD 2E 00            mov rax, qword ptr [rip + 0x2ebd03]
00C374B5  48 C1 E1 06                     shl rcx, 6
00C374B9  49 03 C8                        add rcx, r8
00C374BC  89 3C 88                        mov dword ptr [rax + rcx*4], edi
00C374BF  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
00C374C4  48 89 BB C0 00 00 00            mov qword ptr [rbx + 0xc0], rdi
00C374CB  E8 D8 0B 98 FF                  call 0x1405b80a8
00C374D0  44 8D 6F 01                     lea r13d, [rdi + 1]
00C374D4  EB 31                           jmp 0x140c37507
00C374D6  8B 44 24 34                     mov eax, dword ptr [rsp + 0x34]
00C374DA  48 8D 95 80 00 00 00            lea rdx, [rbp + 0x80]
00C374E1  44 8B CE                        mov r9d, esi
00C374E4  41 B8 03 00 00 00               mov r8d, 3
00C374EA  B9 DF 01 00 00                  mov ecx, 0x1df
00C374EF  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00C374F4  E8 67 61 8C FF                  call 0x1404fd660
00C374F9  CC                              int3
00C374FA  41 BC 80 00 00 00               mov r12d, 0x80
00C37500  4C 8D 3D F9 8A 3C FF            lea r15, [rip - 0xc37507]
00C37507  66 44 39 2D F1 DA 38 00         cmp word ptr [rip + 0x38daf1], r13w
00C3750F  0F 86 CF 00 00 00               jbe 0x140c375e4
00C37515  0F B7 05 E4 DA 38 00            movzx eax, word ptr [rip + 0x38dae4]
00C3751C  3B F8                           cmp edi, eax
00C3751E  0F 83 1B 01 00 00               jae 0x140c3763f
00C37524  8B F7                           mov esi, edi
00C37526  48 69 C6 38 03 00 00            imul rax, rsi, 0x338
00C3752D  48 8D 98 C0 AE FD 00            lea rbx, [rax + 0xfdaec0]
00C37534  49 03 DF                        add rbx, r15
00C37537  49 39 9C F7 C0 F6 FC 00         cmp qword ptr [r15 + rsi*8 + 0xfcf6c0], rbx
00C3753F  0F 85 97 00 00 00               jne 0x140c375dc
00C37545  BA 80 03 00 00                  mov edx, 0x380
00C3754A  41 B8 4B 65 20 20               mov r8d, 0x2020654b
00C37550  49 8B CE                        mov rcx, r14
00C37553  E8 98 AB F4 FF                  call 0x140b820f0
00C37558  48 8B D0                        mov rdx, rax
00C3755B  48 85 C0                        test rax, rax
00C3755E  0F 84 3B 02 00 00               je 0x140c3779f
00C37564  48 8B C8                        mov rcx, rax
00C37567  B8 06 00 00 00                  mov eax, 6
00C3756C  0F 10 03                        movups xmm0, xmmword ptr [rbx]
00C3756F  0F 11 01                        movups xmmword ptr [rcx], xmm0
00C37572  0F 10 4B 10                     movups xmm1, xmmword ptr [rbx + 0x10]
00C37576  0F 11 49 10                     movups xmmword ptr [rcx + 0x10], xmm1
00C3757A  0F 10 43 20                     movups xmm0, xmmword ptr [rbx + 0x20]
00C3757E  0F 11 41 20                     movups xmmword ptr [rcx + 0x20], xmm0
00C37582  0F 10 4B 30                     movups xmm1, xmmword ptr [rbx + 0x30]
00C37586  0F 11 49 30                     movups xmmword ptr [rcx + 0x30], xmm1
00C3758A  0F 10 43 40                     movups xmm0, xmmword ptr [rbx + 0x40]
00C3758E  0F 11 41 40                     movups xmmword ptr [rcx + 0x40], xmm0
00C37592  0F 10 4B 50                     movups xmm1, xmmword ptr [rbx + 0x50]
00C37596  0F 11 49 50                     movups xmmword ptr [rcx + 0x50], xmm1
00C3759A  0F 10 43 60                     movups xmm0, xmmword ptr [rbx + 0x60]
00C3759E  0F 11 41 60                     movups xmmword ptr [rcx + 0x60], xmm0
00C375A2  49 03 CC                        add rcx, r12
00C375A5  0F 10 4B 70                     movups xmm1, xmmword ptr [rbx + 0x70]
00C375A9  49 03 DC                        add rbx, r12
00C375AC  0F 11 49 F0                     movups xmmword ptr [rcx - 0x10], xmm1
00C375B0  48 83 E8 01                     sub rax, 1
00C375B4  75 B6                           jne 0x140c3756c
00C375B6  0F 10 03                        movups xmm0, xmmword ptr [rbx]
00C375B9  49 89 94 F7 C0 F6 FC 00         mov qword ptr [r15 + rsi*8 + 0xfcf6c0], rdx
00C375C1  0F 11 01                        movups xmmword ptr [rcx], xmm0
00C375C4  0F 10 4B 10                     movups xmm1, xmmword ptr [rbx + 0x10]
00C375C8  0F 11 49 10                     movups xmmword ptr [rcx + 0x10], xmm1
00C375CC  0F 10 43 20                     movups xmm0, xmmword ptr [rbx + 0x20]
00C375D0  0F 11 41 20                     movups xmmword ptr [rcx + 0x20], xmm0
00C375D4  48 8B 43 30                     mov rax, qword ptr [rbx + 0x30]
00C375D8  48 89 41 30                     mov qword ptr [rcx + 0x30], rax
00C375DC  41 03 FD                        add edi, r13d
00C375DF  E9 31 FF FF FF                  jmp 0x140c37515
00C375E4  48 8B 15 D5 80 39 00            mov rdx, qword ptr [rip + 0x3980d5]
00C375EB  48 8D 4D 60                     lea rcx, [rbp + 0x60]
00C375EF  0F 57 C0                        xorps xmm0, xmm0
00C375F2  48 89 7C 24 50                  mov qword ptr [rsp + 0x50], rdi
00C375F7  33 C0                           xor eax, eax
00C375F9  8B DF                           mov ebx, edi
00C375FB  0F 11 45 60                     movups xmmword ptr [rbp + 0x60], xmm0
00C375FF  48 89 45 70                     mov qword ptr [rbp + 0x70], rax
00C37603  E8 A8 6E 7E FF                  call 0x14041e4b0
00C37608  EB 13                           jmp 0x140c3761d
00C3760A  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
00C3760F  48 8B 88 80 00 00 00            mov rcx, qword ptr [rax + 0x80]
00C37616  F3 48 0F B8 C1                  popcnt rax, rcx
00C3761B  03 D8                           add ebx, eax
00C3761D  48 8D 54 24 50                  lea rdx, [rsp + 0x50]
00C37622  48 8D 4D 60                     lea rcx, [rbp + 0x60]
00C37626  E8 AD F0 61 FF                  call 0x1402566d8
00C3762B  85 C0                           test eax, eax
00C3762D  74 DB                           je 0x140c3760a
00C3762F  8B 05 4B F4 38 00               mov eax, dword ptr [rip + 0x38f44b]
00C37635  3B D8                           cmp ebx, eax
00C37637  0F 85 64 01 00 00               jne 0x140c377a1
00C3763D  EB 02                           jmp 0x140c37641
00C3763F  33 FF                           xor edi, edi
00C37641  0F B7 15 B8 D9 38 00            movzx edx, word ptr [rip + 0x38d9b8]
00C37648  41 3B D6                        cmp edx, r14d
00C3764B  73 1C                           jae 0x140c37669
00C3764D  44 2B F2                        sub r14d, edx
00C37650  48 8D 0C D5 C0 F6 FC 00         lea rcx, [rdx*8 + 0xfcf6c0]
00C37658  45 8B C6                        mov r8d, r14d
00C3765B  49 03 CF                        add rcx, r15
00C3765E  49 C1 E0 03                     shl r8, 3
00C37662  33 D2                           xor edx, edx
00C37664  E8 D7 F5 A8 FF                  call 0x1406c6c40
00C37669  39 3D ED F7 38 00               cmp dword ptr [rip + 0x38f7ed], edi
00C3766F  74 0C                           je 0x140c3767d
00C37671  C7 05 6D F4 38 00 00 08 00 00   mov dword ptr [rip + 0x38f46d], 0x800
00C3767B  EB 4A                           jmp 0x140c376c7
00C3767D  40 38 3D 20 F4 38 00            cmp byte ptr [rip + 0x38f420], dil
00C37684  75 0E                           jne 0x140c37694
00C37686  8B 05 F4 F3 38 00               mov eax, dword ptr [rip + 0x38f3f4]
00C3768C  89 05 56 F4 38 00               mov dword ptr [rip + 0x38f456], eax
00C37692  EB 33                           jmp 0x140c376c7
00C37694  8B 44 24 3C                     mov eax, dword ptr [rsp + 0x3c]
00C37698  89 05 4A F4 38 00               mov dword ptr [rip + 0x38f44a], eax
00C3769E  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
00C376A7  8B 88 A4 00 00 00               mov ecx, dword ptr [rax + 0xa4]
00C376AD  0F AF 88 A0 00 00 00            imul ecx, dword ptr [rax + 0xa0]
00C376B4  0F AF 0D AD F5 38 00            imul ecx, dword ptr [rip + 0x38f5ad]
00C376BB  39 4C 24 3C                     cmp dword ptr [rsp + 0x3c], ecx
00C376BF  76 06                           jbe 0x140c376c7
00C376C1  89 0D 21 F4 38 00               mov dword ptr [rip + 0x38f421], ecx
00C376C7  40 38 3D D6 F3 38 00            cmp byte ptr [rip + 0x38f3d6], dil
00C376CE  75 0E                           jne 0x140c376de
00C376D0  0F B7 05 41 D9 38 00            movzx eax, word ptr [rip + 0x38d941]
00C376D7  66 89 05 36 D9 38 00            mov word ptr [rip + 0x38d936], ax
00C376DE  E8 61 5B 00 00                  call 0x140c3d244
00C376E3  84 C0                           test al, al
00C376E5  75 0B                           jne 0x140c376f2
00C376E7  B9 A0 00 00 00                  mov ecx, 0xa0
00C376EC  E8 4F 5F 8C FF                  call 0x1404fd640
00C376F1  CC                              int3
00C376F2  8B DF                           mov ebx, edi
00C376F4  8B 05 86 F3 38 00               mov eax, dword ptr [rip + 0x38f386]
00C376FA  3B D8                           cmp ebx, eax
00C376FC  73 31                           jae 0x140c3772f
00C376FE  8B CB                           mov ecx, ebx
00C37700  49 8B 8C CF 40 8C FC 00         mov rcx, qword ptr [r15 + rcx*8 + 0xfc8c40]
00C37708  E8 03 F4 F2 FF                  call 0x140b66b10
00C3770D  85 C0                           test eax, eax
00C3770F  78 05                           js 0x140c37716
00C37711  41 03 DD                        add ebx, r13d
00C37714  EB DE                           jmp 0x140c376f4
00C37716  45 33 C9                        xor r9d, r9d
00C37719  48 63 D0                        movsxd rdx, eax
00C3771C  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
00C37721  41 8D 49 32                     lea ecx, [r9 + 0x32]
00C37725  45 8D 41 0C                     lea r8d, [r9 + 0xc]
00C37729  E8 32 5F 8C FF                  call 0x1404fd660
00C3772E  CC                              int3
00C3772F  E8 9C 09 00 00                  call 0x140c380d0
00C37734  48 8B 05 D5 91 1C 00            mov rax, qword ptr [rip + 0x1c91d5]
00C3773B  33 D2                           xor edx, edx
00C3773D  41 8A CD                        mov cl, r13b
00C37740  E8 8B 33 A8 FF                  call 0x1406baad0
00C37745  B9 FF FF 00 00                  mov ecx, 0xffff
00C3774A  44 89 2D 23 F7 38 00            mov dword ptr [rip + 0x38f723], r13d
00C37751  E8 9A 27 61 FF                  call 0x140249ef0
00C37756  89 05 80 F8 38 00               mov dword ptr [rip + 0x38f880], eax
00C3775C  48 8D 0D ED F4 38 00            lea rcx, [rip + 0x38f4ed]
00C37763  89 3D E7 F4 38 00               mov dword ptr [rip + 0x38f4e7], edi
00C37769  E8 B2 04 5E FF                  call 0x140217c20
00C3776E  48 8B 8D 40 06 00 00            mov rcx, qword ptr [rbp + 0x640]
00C37775  48 33 CC                        xor rcx, rsp
00C37778  E8 C3 4E A7 FF                  call 0x1406ac640
00C3777D  4C 8D 9C 24 50 07 00 00         lea r11, [rsp + 0x750]
00C37785  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
00C37789  49 8B 73 38                     mov rsi, qword ptr [r11 + 0x38]
00C3778D  49 8B 7B 40                     mov rdi, qword ptr [r11 + 0x40]
00C37791  49 8B E3                        mov rsp, r11
00C37794  41 5F                           pop r15
00C37796  41 5E                           pop r14
00C37798  41 5D                           pop r13
00C3779A  41 5C                           pop r12
00C3779C  5D                              pop rbp
00C3779D  C3                              ret
00C3779E  CC                              int3
00C3779F  33 FF                           xor edi, edi
00C377A1  33 D2                           xor edx, edx
00C377A3  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
00C377A8  41 B9 14 00 00 00               mov r9d, 0x14
00C377AE  45 33 C0                        xor r8d, r8d
00C377B1  8D 4A 32                        lea ecx, [rdx + 0x32]
00C377B4  E8 A7 5E 8C FF                  call 0x1404fd660
00C377B9  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KeStartAllProcessors(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m700;
    unsigned int v_stack_m704;
    unsigned __int64 v_stack_m708;
    unsigned __int64 v_stack_m718;
    unsigned __int64 v_stack_m720;
    unsigned __int64 v_stack_m728;
    unsigned int v_stack_m72C;
    unsigned int v_stack_m730;
    unsigned int v_stack_m734;
    unsigned int v_stack_m738;
    unsigned int v_stack_m73C;
    unsigned int v_stack_m740;
    unsigned int v_stack_m744;
    unsigned __int16 v_stack_m748;
    unsigned __int64 v_stack_m758;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 24) = v_rdi;
    v_rsp = (v_rsp) - (0x750ULL);
    result = (*(unsigned __int64 *)(v_rip + 1914779)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 1656 + 1600) = result;
    result = 0;
    v_rdi = 0;
    v_stack_m704 = 0;
    a2 = 0;
    v_stack_m740 = 0;
    result = memset(v_stack_m708, a2, 228, a4);
    v_stack_m730 = 0;
    v_stack_m73C = 0;
    v_stack_m748 = 0;
    v_stack_m744 = 0;
    v_stack_m72C = 0;
    v_stack_m738 = 0;
    v_stack_m734 = 0;
    result = KiCompleteBootProcessorContextInitialization(v_stack_m708, a2, 228, a4);
    if (sign_flag) goto loc_00C377A1;
    result = (unsigned int)((*(unsigned __int16 *)(*(unsigned __int64 *)(gs_base + (0 + 24)) + 742)) + 1);
    *(unsigned int *)(v_rip + 2292027) = (unsigned int)(result);
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(result)), (unsigned int)((unsigned int)((unsigned int)(0x2020654BULL))), a4);
    *(unsigned __int64 *)(v_rip + 3812983) = result;
    if (result == 0) goto loc_00C377A1;
    result = memcpy(result, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 24)) + 744), (unsigned int)(*(unsigned int *)(v_rip + 2291999)), a4);
    if ((*(unsigned int *)(v_rip + 3734545)) >= = ((unsigned int)((unsigned int)(0x800ULL)))) {
        *(unsigned int *)(v_rip + 3734537) = (unsigned int)((unsigned int)(0x800ULL));
    }
    a2 = 0;
    *(unsigned int *)(v_rip + 3734491) = 1;
    result = memset(v_rsp - 1656 + 128, a2, (unsigned int)(0x5C0ULL), a4);
    result = KiComputeEstimatedMaximumProcessors(v_stack_m730, v_stack_m740, v_stack_m73C, a4);
    result = KiAllocateProcessorLookupStructures((unsigned int)((unsigned int)((unsigned int)(v_stack_m73C))), v_stack_m740, v_stack_m73C, a4);
    if (sign_flag) goto loc_00C377A1;
    *(unsigned int *)(v_rip + 3734075) = (unsigned int)((unsigned int)(v_stack_m73C));
    if (((unsigned int)(*(unsigned __int16 *)(v_rip + 3727200))) != 1) goto loc_00C370BF;
    goto loc_00C370C2;
loc_00C370BF:
    v_rbx = (unsigned int)(((unsigned int)(v_stack_m740)) << (6));
loc_00C370C2:
    a2 = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) << (5));
    result = ExAllocatePool2(64, a2, (unsigned int)((unsigned int)((unsigned int)(0x2020654BULL))), a4);
    if (result == 0) goto loc_00C377A1;
    *(unsigned __int64 *)(v_rip + 3734825) = result;
    a2 = ((unsigned int)((unsigned int)(v_rbx))) << (3);
    result = (result) + (a2);
    *(unsigned __int64 *)(v_rip + 3734817) = result;
    result = (result) + (a2);
    *(unsigned __int64 *)(v_rip + 3736047) = result;
    *(unsigned int *)(v_rip + 3735230) = (unsigned int)(v_rbx * 8);
    result = KiCreateCpuSetForProcessor(*(unsigned __int64 *)(v_rip + 3742552), a2, (unsigned int)((unsigned int)((unsigned int)(0x2020654BULL))), a4);
    result = KiComputeProcessorDataSize((unsigned int)(v_stack_m740), v_stack_m738, v_stack_m734, a4);
    v_stack_m720 = (unsigned int)(v_stack_m738);
    v_stack_m718 = (unsigned int)(v_stack_m734);
    result = HvlStartBootLogicalProcessors((unsigned int)(v_stack_m734), v_stack_m738, v_stack_m734, a4);
    if (sign_flag) goto loc_00C377A1;
loc_00C37155:
loc_00C37161:
    if (0 >= 0x7FFULL) goto loc_00C374FA;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3733772)))) >= v_stack_m730) goto loc_00C374FA;
    v_stack_m748 = (unsigned __int16)((unsigned int)(0xFFFFULL));
    v_r15 = (unsigned int)((0) + (1));
    result = KiQueryProcessorNode((unsigned int)((unsigned int)(v_r15)), v_stack_m744, v_stack_m748, a4);
    if ((unsigned int)(result) != 0) goto loc_00C37161;
    a2 = 0;
    v_rsi = (unsigned int)((0) + (1));
    result = memset(v_stack_m708, a2, 232, a4);
    result = ExCreatePoolTagTable((unsigned int)((unsigned int)(v_rsi)), v_stack_m748, 232, a4);
    if (result == 0) goto loc_00C377A1;
    result = MmAllocateIndependentPagesEx((unsigned int)((unsigned int)(result)), v_stack_m748, v_stack_m720, 2);
    if (result == 0) goto loc_00C377A1;
    v_stack_m700 = result;
    *(unsigned int *)(v_rsp - 1656 - 116) = (unsigned int)((unsigned int)(v_stack_m740));
    *(unsigned int *)(v_rsp - 1656 - 108) = (unsigned int)((unsigned int)(v_stack_m738));
    *(unsigned int *)(v_rsp - 1656 - 104) = (unsigned int)((unsigned int)(v_stack_m734));
    *(unsigned int *)(v_rsp - 1656 - 128) = (unsigned int)((unsigned int)((unsigned int)(result)));
    *(unsigned int *)(v_rsp - 1656 - 124) = (unsigned int)(v_stack_m748);
    *(unsigned int *)(v_rsp - 1656 - 120) = (unsigned int)(v_rsi);
    result = KiAllocateProcessorStateInitializationParameters(v_stack_m708, v_stack_m748, v_stack_m720, 2);
    if (sign_flag) goto loc_00C377A1;
    result = KiInitializeProcessorState(v_rsp - 1656 + 128, *(unsigned __int64 *)(v_rip + 3733731), v_stack_m708, 2);
    if (result == 0) goto loc_00C377A1;
    result = KiRcuProcessorInitialize(result, 1, v_stack_m708, 2);
    result = HvlInitializeProcessor(result, (unsigned int)((unsigned int)(v_rsi)), (unsigned int)(v_stack_m744), 2);
    if ((unsigned int)(result) != 0) goto loc_00C3779F;
    result = MmInitializeProcessor(result, (unsigned int)((unsigned int)(v_rsi)), (unsigned int)(v_stack_m744), 2);
    if ((unsigned int)(result) == 0) goto loc_00C3779F;
    result = KiInitializePrcbContext(result, v_stack_m748, (unsigned int)(v_stack_m744), 2);
    if (sign_flag) goto loc_00C3779F;
    result = KeInitializeTimerTable(result, v_stack_m748, (unsigned int)(v_stack_m744), 2);
    if (sign_flag) goto loc_00C3779F;
    result = EtwInitializeProcessor(result, v_stack_m748, (unsigned int)(v_stack_m744), 2);
    if (sign_flag) goto loc_00C3779F;
    result = KiAllocatePrcbThreads(result, v_stack_m748, (unsigned int)(v_stack_m744), 2);
    if (sign_flag) goto loc_00C3779F;
    result = KiAllocateLocalSharedReadyQueue(result, v_stack_m748, (unsigned int)(v_stack_m744), 2);
    if (sign_flag) goto loc_00C3779F;
    result = KiAllocateStaticRescheduleContext(result, v_stack_m748, (unsigned int)(v_stack_m744), 2);
    if (sign_flag) goto loc_00C3779F;
    result = KiAllocateIdleSearchStructures(result, v_stack_m748, (unsigned int)(v_stack_m744), 2);
    if (sign_flag) goto loc_00C3779F;
    result = KiAllocateForceParkingData(result, v_stack_m748, (unsigned int)(v_stack_m744), 2);
    if (sign_flag) goto loc_00C3779F;
    result = VmInitializeProcessor(result, v_stack_m748, (unsigned int)(v_stack_m744), 2);
    if (sign_flag) goto loc_00C3779F;
    result = HalStartNextProcessor(v_rsp - 1656 + 128, (unsigned int)((unsigned int)(v_rsi)), (unsigned int)(v_stack_m744), 2);
    if (((unsigned int)(result)) == 3) goto loc_00C374D6;
    if (((unsigned int)(result)) != 4) goto loc_00C373A1;
    v_rdi = 0;
    v_stack_m72C = 0;
    goto loc_00C3736D;
loc_00C37363:
    result = KeYieldProcessorEx(v_stack_m72C, (unsigned int)((unsigned int)(v_rsi)), (unsigned int)(v_stack_m744), 2);
loc_00C3736D:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3733420) + 136) != 0) goto loc_00C37363;
    result = KiConfigureProcessorBlock(result, (unsigned int)((unsigned int)(v_rsi)), (unsigned int)(v_stack_m744), 2);
    result = KiUpdateProcessorCount((unsigned int)((unsigned int)(v_rsi)), *(unsigned __int8 *)(result + 208), (unsigned int)(v_stack_m744), 2);
    goto loc_00C37155;
loc_00C373A1:
loc_00C373AD:
    *(unsigned __int64 *)(1) = v_xmm0;
    *(unsigned __int64 *)(1 + 16) = v_xmm1;
    *(unsigned __int64 *)(1 + 32) = v_xmm0;
    *(unsigned __int64 *)(1 + 48) = v_xmm1;
    *(unsigned __int64 *)(1 + 64) = v_xmm0;
    *(unsigned __int64 *)(1 + 80) = v_xmm1;
    *(unsigned __int64 *)(1 + 96) = v_xmm0;
    a1 = (1) + (6 + 122);
    v_rdi = (v_rdi) + (6 + 122);
    *(unsigned __int64 *)(a1 - 16) = v_xmm1;
    result = (6) - (1);
    if (condition_is_not_equal) goto loc_00C373AD;
    a2 = 0;
    *(unsigned __int64 *)(a1) = v_xmm0;
    *(unsigned __int64 *)(a1 + 16) = v_xmm1;
    *(unsigned __int64 *)(a1 + 32) = v_xmm0;
    *(unsigned __int64 *)(a1 + 48) = *(unsigned __int64 *)(v_rdi + 48);
    *(unsigned __int64 *)(v_rip - 12809217 + v_stack_m748 * 8 + 16578240) = 1;
    result = KiRcuProcessorInitialize(result, a2, (unsigned int)(v_stack_m744), 2);
    result = KiFreeForceParkingData(result, a2, (unsigned int)(v_stack_m744), 2);
    result = KiFreeIdleSearchStructures(result, a2, (unsigned int)(v_stack_m744), 2);
    result = KiFreeStaticRescheduleContext(result, a2, (unsigned int)(v_stack_m744), 2);
    result = KiFreeLocalSharedReadyQueue(result, a2, (unsigned int)(v_stack_m744), 2);
    result = KiFreePrcbThreads(result, a2, (unsigned int)(v_stack_m744), 2);
    result = HvlDeleteProcessor(result, a2, (unsigned int)(v_stack_m744), 2);
    result = MmDeleteProcessor(result, a2, (unsigned int)(v_stack_m744), 2);
    result = EtwDeleteProcessor(result, a2, (unsigned int)(v_stack_m744), 2);
    result = ExDeletePoolTagTable((unsigned int)((unsigned int)(v_rsi)), a2, (unsigned int)(v_stack_m744), 2);
    result = KiUnshadowProcessorAllocation(result, v_rsp - 1656 + 128, v_stack_m708, 2);
    v_rdi = 0;
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 3063067) + (unsigned int)(*(unsigned int *)(result + 36)) * 4) = 0;
    a1 = ((unsigned int)((unsigned int)(*(unsigned __int8 *)(result + 208)))) << (6);
    a1 = (a1) + (*(unsigned __int8 *)(result + 209));
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 3063043) + a1 * 4) = 0;
    *(unsigned __int64 *)(result + 192) = 0;
    result = KiFreeProcessorStateInitializationParameters(v_stack_m708, *(unsigned __int8 *)(result + 208), *(unsigned __int8 *)(result + 209), 2);
    goto loc_00C37507;
loc_00C374D6:
    v_stack_m758 = (unsigned int)(v_stack_m744);
    result = KeBugCheckEx(479, v_rsp - 1656 + 128, 3, (unsigned int)((unsigned int)(v_rsi)));
loc_00C374FA:
loc_00C37507:
    if ((*(unsigned __int16 *)(v_rip + 3726065)) <= ((unsigned __int16)(v_rdi + 1))) goto loc_00C375E4;
loc_00C37515:
    if (0 >= ((unsigned int)(*(unsigned __int16 *)(v_rip + 3726052)))) goto loc_00C3763F;
    result = (*(unsigned __int16 *)(v_rip + 3726052)) * (0);
    v_rbx = (result + 16625344) + (v_rip - 12809479);
    if ((*(unsigned __int64 *)(v_rip - 12809479 + 0 * 8 + 16578240)) != v_rbx) goto loc_00C375DC;
    result = ExAllocatePool2(64, 896, (unsigned int)(0x2020654BULL), (unsigned int)((unsigned int)(v_rsi)));
    if (result == 0) goto loc_00C3779F;
loc_00C3756C:
    *(unsigned __int64 *)(result) = v_xmm0;
    *(unsigned __int64 *)(result + 16) = v_xmm1;
    *(unsigned __int64 *)(result + 32) = v_xmm0;
    *(unsigned __int64 *)(result + 48) = v_xmm1;
    *(unsigned __int64 *)(result + 64) = v_xmm0;
    *(unsigned __int64 *)(result + 80) = v_xmm1;
    *(unsigned __int64 *)(result + 96) = v_xmm0;
    a1 = (result) + (128);
    v_rbx = (v_rbx) + (128);
    *(unsigned __int64 *)(a1 - 16) = v_xmm1;
    result = (6) - (1);
    if (condition_is_not_equal) goto loc_00C3756C;
    *(unsigned __int64 *)(v_rip - 12809479 + 0 * 8 + 16578240) = result;
    *(unsigned __int64 *)(a1) = v_xmm0;
    *(unsigned __int64 *)(a1 + 16) = v_xmm1;
    *(unsigned __int64 *)(a1 + 32) = v_xmm0;
    *(unsigned __int64 *)(a1 + 48) = *(unsigned __int64 *)(v_rbx + 48);
loc_00C375DC:
    v_rdi = (unsigned int)((v_rdi) + ((unsigned int)(v_rdi + 1)));
    goto loc_00C37515;
loc_00C375E4:
    v_stack_m728 = v_rdi;
    result = 0;
    *(unsigned __int64 *)(v_rsp - 1656 + 96) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 1656 + 112) = 0;
    result = KeInitializeSchedulerSubNodeEnumerationContext(v_rsp - 1656 + 96, *(unsigned __int64 *)(v_rip + 3768533), (unsigned int)(0x2020654BULL), (unsigned int)((unsigned int)(v_rsi)));
    goto loc_00C3761D;
loc_00C3760A:
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) + ((unsigned int)(v_stack_m728)));
loc_00C3761D:
    result = KeEnumerateNextSchedulerSubNodeInNode(v_rsp - 1656 + 96, v_stack_m728, (unsigned int)(0x2020654BULL), (unsigned int)((unsigned int)(v_rsi)));
    if ((unsigned int)(result) == 0) goto loc_00C3760A;
    if (((unsigned int)(v_rbx)) != ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3732555))))) goto loc_00C377A1;
    goto loc_00C37641;
loc_00C3763F:
    v_rdi = 0;
loc_00C37641:
    result = (unsigned int)(*(unsigned int *)(v_rip + 3732555));
    v_r14 = 64;
    if (((unsigned int)(*(unsigned __int16 *)(v_rip + 3725752))) < 64) {
        v_r14 = (unsigned int)((64) - ((unsigned int)(*(unsigned __int16 *)(v_rip + 3725752))));
        a1 = *(unsigned __int16 *)(v_rip + 3725752) * 8 + 16578240;
        a3 = (unsigned int)(v_r14);
        a1 = (a1) + (v_rip - 12809479);
        a3 = (a3) << (3);
        a2 = 0;
        result = memset(a1, a2, a3, (unsigned int)((unsigned int)(v_rsi)));
    }
    if ((*(unsigned int *)(v_rip + 3733485)) == 0) goto loc_00C3767D;
    *(unsigned int *)(v_rip + 3732589) = 0x800ULL;
    goto loc_00C376C7;
loc_00C3767D:
    if ((*(unsigned __int8 *)(v_rip + 3732512)) != 0) goto loc_00C37694;
    *(unsigned int *)(v_rip + 3732566) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3732468)));
    goto loc_00C376C7;
loc_00C37694:
    *(unsigned int *)(v_rip + 3732554) = (unsigned int)((unsigned int)(v_stack_m73C));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 164))) * (*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 160)));
    a1 = (unsigned int)((a1) * (*(unsigned int *)(v_rip + 3732909)));
    if (v_stack_m73C >= = ((unsigned int)(a1))) {
        *(unsigned int *)(v_rip + 3732513) = (unsigned int)(a1);
    }
    result = *(unsigned __int64 *)(gs_base + (0 + 32));
    if ((*(unsigned __int8 *)(v_rip + 3732438)) == 0) {
        result = *(unsigned __int16 *)(v_rip + 3725633);
        *(unsigned __int16 *)(v_rip + 3725622) = (unsigned __int16)(result);
    }
    result = PoInitHeteroDetection(a1, a2, a3, (unsigned int)((unsigned int)(v_rsi)));
    if ((unsigned __int8)(result) == 0) {
        a1 = 160;
        result = KeBugCheck(a1, a2, a3, (unsigned int)((unsigned int)(v_rsi)));
    }
loc_00C376F4:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3732358))))) goto loc_00C3772F;
    result = KiInitializeThreadCycleTable(*(unsigned __int64 *)(v_rip - 12809479 + 0 * 8 + 16550976), a2, a3, (unsigned int)((unsigned int)(v_rsi)));
    if (sign_flag) goto loc_00C37716;
    v_rbx = (unsigned int)((0) + ((unsigned int)(v_rdi + 1)));
    goto loc_00C376F4;
loc_00C37716:
    a4 = 0;
    v_stack_m758 = 0;
    result = KeBugCheckEx(a4 + 50, (int)((unsigned int)(result)), a4 + 12, a4);
loc_00C3772F:
    result = KiConfigureAllSchedulingInformation(a4 + 50, (int)((unsigned int)(result)), a4 + 12, a4);
    a2 = 0;
    result = guard_dispatch_icall((unsigned __int8)(v_rdi + 1), a2, a4 + 12, a4);
    *(unsigned int *)(v_rip + 3733283) = (unsigned int)(v_rdi + 1);
    result = KeQueryActiveProcessorCountEx((unsigned int)(0xFFFFULL), a2, a4 + 12, a4);
    *(unsigned int *)(v_rip + 3733632) = (unsigned int)(result);
    *(unsigned int *)(v_rip + 3732711) = 0;
    result = KeWakeAddressAll(v_rip + 3732717, a2, a4 + 12, a4);
    a1 = (*(unsigned __int64 *)(v_rsp - 1656 + 1600)) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a4 + 12, a4);
    return result;
loc_00C3779F:
    v_rdi = 0;
loc_00C377A1:
    a2 = 0;
    v_stack_m730 = 0;
    a3 = 0;
    result = KeBugCheckEx(a2 + 50, a2, a3, 20);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KeStartAllProcessors(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m700;
    uint32_t v_stack_m704;
    uint64_t v_stack_m708;
    uint64_t v_stack_m718;
    uint64_t v_stack_m720;
    uint64_t v_stack_m728;
    uint32_t v_stack_m72C;
    uint32_t v_stack_m730;
    uint32_t v_stack_m734;
    uint32_t v_stack_m738;
    uint32_t v_stack_m73C;
    uint32_t v_stack_m740;
    uint32_t v_stack_m744;
    uint16_t v_stack_m748;
    uint64_t v_stack_m758;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rsi;
    *(uint64_t *)(local_rsp + 0x18) = local_rdi;
    local_rsp = (local_rsp) - (0x750ULL);
    result = (*(uint64_t *)(v_rip + 0x1D379B)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x678 + 0x640) = result;
    result = 0;
    local_rdi = 0;
    v_stack_m704 = 0;
    Arg2 = 0;
    v_stack_m740 = 0;
    result = memset(v_stack_m708, Arg2, 228, a4);
    v_stack_m730 = 0;
    v_stack_m73C = 0;
    v_stack_m748 = 0;
    v_stack_m744 = 0;
    v_stack_m72C = 0;
    v_stack_m738 = 0;
    v_stack_m734 = 0;
    result = KiCompleteBootProcessorContextInitialization(v_stack_m708, Arg2, 228, a4);
    if (sign_flag) goto loc_00C377A1;
    result = (uint32_t)((*(uint16_t *)(*(uint64_t *)(gs_base + (0 + 0x18)) + 0x2E6)) + 1);
    *(uint32_t *)(v_rip + 0x22F93B) = (uint32_t)(result);
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(result)), (uint32_t)((uint32_t)((uint32_t)(0x2020654BULL))), a4);
    *(uint64_t *)(v_rip + 0x3A2E77) = result;
    if (result == 0) goto loc_00C377A1;
    result = memcpy(result, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x18)) + 0x2E8), (uint32_t)(*(uint32_t *)(v_rip + 0x22F91F)), a4);
    if ((*(uint32_t *)(v_rip + 0x38FC11)) >= = ((uint32_t)((uint32_t)(0x800ULL)))) {
        *(uint32_t *)(v_rip + 0x38FC09) = (uint32_t)((uint32_t)(0x800ULL));
    }
    Arg2 = 0;
    *(uint32_t *)(v_rip + 0x38FBDB) = 1;
    result = memset(local_rsp - 1656 + 128, Arg2, (uint32_t)(0x5C0ULL), a4);
    result = KiComputeEstimatedMaximumProcessors(v_stack_m730, v_stack_m740, v_stack_m73C, a4);
    result = KiAllocateProcessorLookupStructures((uint32_t)((uint32_t)((uint32_t)(v_stack_m73C))), v_stack_m740, v_stack_m73C, a4);
    if (sign_flag) goto loc_00C377A1;
    *(uint32_t *)(v_rip + 0x38FA3B) = (uint32_t)((uint32_t)(v_stack_m73C));
    if (((uint32_t)(*(uint16_t *)(v_rip + 0x38DF60))) != 1) goto loc_00C370BF;
    goto loc_00C370C2;
loc_00C370BF:
    local_rbx = (uint32_t)(((uint32_t)(v_stack_m740)) << (6));
loc_00C370C2:
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) << (5));
    result = ExAllocatePool2(64, Arg2, (uint32_t)((uint32_t)((uint32_t)(0x2020654BULL))), a4);
    if (result == 0) goto loc_00C377A1;
    *(uint64_t *)(v_rip + 0x38FD29) = result;
    Arg2 = ((uint32_t)((uint32_t)(local_rbx))) << (3);
    result = (result) + (Arg2);
    *(uint64_t *)(v_rip + 0x38FD21) = result;
    result = (result) + (Arg2);
    *(uint64_t *)(v_rip + 0x3901EF) = result;
    *(uint32_t *)(v_rip + 0x38FEBE) = (uint32_t)(local_rbx * 8);
    result = KiCreateCpuSetForProcessor(*(uint64_t *)(v_rip + 0x391B58), Arg2, (uint32_t)((uint32_t)((uint32_t)(0x2020654BULL))), a4);
    result = KiComputeProcessorDataSize((uint32_t)(v_stack_m740), v_stack_m738, v_stack_m734, a4);
    v_stack_m720 = (uint32_t)(v_stack_m738);
    v_stack_m718 = (uint32_t)(v_stack_m734);
    result = HvlStartBootLogicalProcessors((uint32_t)(v_stack_m734), v_stack_m738, v_stack_m734, a4);
    if (sign_flag) goto loc_00C377A1;
loc_00C37155:
loc_00C37161:
    if (0 >= 0x7FFULL) goto loc_00C374FA;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x38F90C)))) >= v_stack_m730) goto loc_00C374FA;
    v_stack_m748 = (uint16_t)((uint32_t)(0xFFFFULL));
    local_r15 = (uint32_t)((0) + (1));
    result = KiQueryProcessorNode((uint32_t)((uint32_t)(local_r15)), v_stack_m744, v_stack_m748, a4);
    if ((uint32_t)(result) != 0) goto loc_00C37161;
    Arg2 = 0;
    local_rsi = (uint32_t)((0) + (1));
    result = memset(v_stack_m708, Arg2, 232, a4);
    result = ExCreatePoolTagTable((uint32_t)((uint32_t)(local_rsi)), v_stack_m748, 232, a4);
    if (result == 0) goto loc_00C377A1;
    result = MmAllocateIndependentPagesEx((uint32_t)((uint32_t)(result)), v_stack_m748, v_stack_m720, 2);
    if (result == 0) goto loc_00C377A1;
    v_stack_m700 = result;
    *(uint32_t *)(local_rsp - 0x678 - 0x74) = (uint32_t)((uint32_t)(v_stack_m740));
    *(uint32_t *)(local_rsp - 0x678 - 0x6C) = (uint32_t)((uint32_t)(v_stack_m738));
    *(uint32_t *)(local_rsp - 0x678 - 0x68) = (uint32_t)((uint32_t)(v_stack_m734));
    *(uint32_t *)(local_rsp - 0x678 - 0x80) = (uint32_t)((uint32_t)((uint32_t)(result)));
    *(uint32_t *)(local_rsp - 0x678 - 0x7C) = (uint32_t)(v_stack_m748);
    *(uint32_t *)(local_rsp - 0x678 - 0x78) = (uint32_t)(local_rsi);
    result = KiAllocateProcessorStateInitializationParameters(v_stack_m708, v_stack_m748, v_stack_m720, 2);
    if (sign_flag) goto loc_00C377A1;
    result = KiInitializeProcessorState(local_rsp - 1656 + 128, *(uint64_t *)(v_rip + 0x38F8E3), v_stack_m708, 2);
    if (result == 0) goto loc_00C377A1;
    result = KiRcuProcessorInitialize(result, 1, v_stack_m708, 2);
    result = HvlInitializeProcessor(result, (uint32_t)((uint32_t)(local_rsi)), (uint32_t)(v_stack_m744), 2);
    if ((uint32_t)(result) != 0) goto loc_00C3779F;
    result = MmInitializeProcessor(result, (uint32_t)((uint32_t)(local_rsi)), (uint32_t)(v_stack_m744), 2);
    if ((uint32_t)(result) == 0) goto loc_00C3779F;
    result = KiInitializePrcbContext(result, v_stack_m748, (uint32_t)(v_stack_m744), 2);
    if (sign_flag) goto loc_00C3779F;
    result = KeInitializeTimerTable(result, v_stack_m748, (uint32_t)(v_stack_m744), 2);
    if (sign_flag) goto loc_00C3779F;
    result = EtwInitializeProcessor(result, v_stack_m748, (uint32_t)(v_stack_m744), 2);
    if (sign_flag) goto loc_00C3779F;
    result = KiAllocatePrcbThreads(result, v_stack_m748, (uint32_t)(v_stack_m744), 2);
    if (sign_flag) goto loc_00C3779F;
    result = KiAllocateLocalSharedReadyQueue(result, v_stack_m748, (uint32_t)(v_stack_m744), 2);
    if (sign_flag) goto loc_00C3779F;
    result = KiAllocateStaticRescheduleContext(result, v_stack_m748, (uint32_t)(v_stack_m744), 2);
    if (sign_flag) goto loc_00C3779F;
    result = KiAllocateIdleSearchStructures(result, v_stack_m748, (uint32_t)(v_stack_m744), 2);
    if (sign_flag) goto loc_00C3779F;
    result = KiAllocateForceParkingData(result, v_stack_m748, (uint32_t)(v_stack_m744), 2);
    if (sign_flag) goto loc_00C3779F;
    result = VmInitializeProcessor(result, v_stack_m748, (uint32_t)(v_stack_m744), 2);
    if (sign_flag) goto loc_00C3779F;
    result = HalStartNextProcessor(local_rsp - 1656 + 128, (uint32_t)((uint32_t)(local_rsi)), (uint32_t)(v_stack_m744), 2);
    if (((uint32_t)(result)) == 3) goto loc_00C374D6;
    if (((uint32_t)(result)) != 4) goto loc_00C373A1;
    local_rdi = 0;
    v_stack_m72C = 0;
    goto loc_00C3736D;
loc_00C37363:
    result = KeYieldProcessorEx(v_stack_m72C, (uint32_t)((uint32_t)(local_rsi)), (uint32_t)(v_stack_m744), 2);
loc_00C3736D:
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0x38F7AC) + 0x88) != 0) goto loc_00C37363;
    result = KiConfigureProcessorBlock(result, (uint32_t)((uint32_t)(local_rsi)), (uint32_t)(v_stack_m744), 2);
    result = KiUpdateProcessorCount((uint32_t)((uint32_t)(local_rsi)), *(uint8_t *)(result + 0xD0), (uint32_t)(v_stack_m744), 2);
    goto loc_00C37155;
loc_00C373A1:
loc_00C373AD:
    *(uint64_t *)(1) = v_xmm0;
    *(uint64_t *)(1 + 0x10) = v_xmm1;
    *(uint64_t *)(1 + 0x20) = v_xmm0;
    *(uint64_t *)(1 + 0x30) = v_xmm1;
    *(uint64_t *)(1 + 0x40) = v_xmm0;
    *(uint64_t *)(1 + 0x50) = v_xmm1;
    *(uint64_t *)(1 + 0x60) = v_xmm0;
    Arg1 = (1) + (6 + 122);
    local_rdi = (local_rdi) + (6 + 122);
    *(uint64_t *)(Arg1 - 0x10) = v_xmm1;
    result = (6) - (1);
    if (condition_is_not_equal) goto loc_00C373AD;
    Arg2 = 0;
    *(uint64_t *)(Arg1) = v_xmm0;
    *(uint64_t *)(Arg1 + 0x10) = v_xmm1;
    *(uint64_t *)(Arg1 + 0x20) = v_xmm0;
    *(uint64_t *)(Arg1 + 0x30) = *(uint64_t *)(local_rdi + 0x30);
    *(uint64_t *)(v_rip - 0xC37401 + v_stack_m748 * 8 + 0xFCF6C0) = 1;
    result = KiRcuProcessorInitialize(result, Arg2, (uint32_t)(v_stack_m744), 2);
    result = KiFreeForceParkingData(result, Arg2, (uint32_t)(v_stack_m744), 2);
    result = KiFreeIdleSearchStructures(result, Arg2, (uint32_t)(v_stack_m744), 2);
    result = KiFreeStaticRescheduleContext(result, Arg2, (uint32_t)(v_stack_m744), 2);
    result = KiFreeLocalSharedReadyQueue(result, Arg2, (uint32_t)(v_stack_m744), 2);
    result = KiFreePrcbThreads(result, Arg2, (uint32_t)(v_stack_m744), 2);
    result = HvlDeleteProcessor(result, Arg2, (uint32_t)(v_stack_m744), 2);
    result = MmDeleteProcessor(result, Arg2, (uint32_t)(v_stack_m744), 2);
    result = EtwDeleteProcessor(result, Arg2, (uint32_t)(v_stack_m744), 2);
    result = ExDeletePoolTagTable((uint32_t)((uint32_t)(local_rsi)), Arg2, (uint32_t)(v_stack_m744), 2);
    result = KiUnshadowProcessorAllocation(result, local_rsp - 1656 + 128, v_stack_m708, 2);
    local_rdi = 0;
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x2EBD1B) + (uint32_t)(*(uint32_t *)(result + 0x24)) * 4) = 0;
    Arg1 = ((uint32_t)((uint32_t)(*(uint8_t *)(result + 0xD0)))) << (6);
    Arg1 = (Arg1) + (*(uint8_t *)(result + 0xD1));
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x2EBD03) + Arg1 * 4) = 0;
    *(uint64_t *)(result + 0xC0) = 0;
    result = KiFreeProcessorStateInitializationParameters(v_stack_m708, *(uint8_t *)(result + 0xD0), *(uint8_t *)(result + 0xD1), 2);
    goto loc_00C37507;
loc_00C374D6:
    v_stack_m758 = (uint32_t)(v_stack_m744);
    result = KeBugCheckEx(479, local_rsp - 1656 + 128, 3, (uint32_t)((uint32_t)(local_rsi)));
loc_00C374FA:
loc_00C37507:
    if ((*(uint16_t *)(v_rip + 0x38DAF1)) <= ((uint16_t)(local_rdi + 1))) goto loc_00C375E4;
loc_00C37515:
    if (0 >= ((uint32_t)(*(uint16_t *)(v_rip + 0x38DAE4)))) goto loc_00C3763F;
    result = (*(uint16_t *)(v_rip + 0x38DAE4)) * (0);
    local_rbx = (result + 16625344) + (v_rip - 12809479);
    if ((*(uint64_t *)(v_rip - 0xC37507 + 0x0 * 8 + 0xFCF6C0)) != local_rbx) goto loc_00C375DC;
    result = ExAllocatePool2(64, 896, (uint32_t)(0x2020654BULL), (uint32_t)((uint32_t)(local_rsi)));
    if (result == 0) goto loc_00C3779F;
loc_00C3756C:
    *(uint64_t *)(result) = v_xmm0;
    *(uint64_t *)(result + 0x10) = v_xmm1;
    *(uint64_t *)(result + 0x20) = v_xmm0;
    *(uint64_t *)(result + 0x30) = v_xmm1;
    *(uint64_t *)(result + 0x40) = v_xmm0;
    *(uint64_t *)(result + 0x50) = v_xmm1;
    *(uint64_t *)(result + 0x60) = v_xmm0;
    Arg1 = (result) + (128);
    local_rbx = (local_rbx) + (128);
    *(uint64_t *)(Arg1 - 0x10) = v_xmm1;
    result = (6) - (1);
    if (condition_is_not_equal) goto loc_00C3756C;
    *(uint64_t *)(v_rip - 0xC37507 + 0x0 * 8 + 0xFCF6C0) = result;
    *(uint64_t *)(Arg1) = v_xmm0;
    *(uint64_t *)(Arg1 + 0x10) = v_xmm1;
    *(uint64_t *)(Arg1 + 0x20) = v_xmm0;
    *(uint64_t *)(Arg1 + 0x30) = *(uint64_t *)(local_rbx + 0x30);
loc_00C375DC:
    local_rdi = (uint32_t)((local_rdi) + ((uint32_t)(local_rdi + 1)));
    goto loc_00C37515;
loc_00C375E4:
    v_stack_m728 = local_rdi;
    result = 0;
    *(uint64_t *)(local_rsp - 0x678 + 0x60) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x678 + 0x70) = 0;
    result = KeInitializeSchedulerSubNodeEnumerationContext(local_rsp - 1656 + 96, *(uint64_t *)(v_rip + 0x3980D5), (uint32_t)(0x2020654BULL), (uint32_t)((uint32_t)(local_rsi)));
    goto loc_00C3761D;
loc_00C3760A:
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) + ((uint32_t)(v_stack_m728)));
loc_00C3761D:
    result = KeEnumerateNextSchedulerSubNodeInNode(local_rsp - 1656 + 96, v_stack_m728, (uint32_t)(0x2020654BULL), (uint32_t)((uint32_t)(local_rsi)));
    if ((uint32_t)(result) == 0) goto loc_00C3760A;
    if (((uint32_t)(local_rbx)) != ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x38F44B))))) goto loc_00C377A1;
    goto loc_00C37641;
loc_00C3763F:
    local_rdi = 0;
loc_00C37641:
    result = (uint32_t)(*(uint32_t *)(v_rip + 0x38F44B));
    local_r14 = 64;
    if (((uint32_t)(*(uint16_t *)(v_rip + 0x38D9B8))) < 64) {
        local_r14 = (uint32_t)((64) - ((uint32_t)(*(uint16_t *)(v_rip + 0x38D9B8))));
        Arg1 = *(uint16_t *)(v_rip + 0x38D9B8) * 8 + 16578240;
        a3 = (uint32_t)(local_r14);
        Arg1 = (Arg1) + (v_rip - 12809479);
        a3 = (a3) << (3);
        Arg2 = 0;
        result = memset(Arg1, Arg2, a3, (uint32_t)((uint32_t)(local_rsi)));
    }
    if ((*(uint32_t *)(v_rip + 0x38F7ED)) == 0) goto loc_00C3767D;
    *(uint32_t *)(v_rip + 0x38F46D) = 0x800ULL;
    goto loc_00C376C7;
loc_00C3767D:
    if ((*(uint8_t *)(v_rip + 0x38F420)) != 0) goto loc_00C37694;
    *(uint32_t *)(v_rip + 0x38F456) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x38F3F4)));
    goto loc_00C376C7;
loc_00C37694:
    *(uint32_t *)(v_rip + 0x38F44A) = (uint32_t)((uint32_t)(v_stack_m73C));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xA4))) * (*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xA0)));
    Arg1 = (uint32_t)((Arg1) * (*(uint32_t *)(v_rip + 0x38F5AD)));
    if (v_stack_m73C >= = ((uint32_t)(Arg1))) {
        *(uint32_t *)(v_rip + 0x38F421) = (uint32_t)(Arg1);
    }
    result = *(uint64_t *)(gs_base + (0 + 0x20));
    if ((*(uint8_t *)(v_rip + 0x38F3D6)) == 0) {
        result = *(uint16_t *)(v_rip + 0x38D941);
        *(uint16_t *)(v_rip + 0x38D936) = (uint16_t)(result);
    }
    result = PoInitHeteroDetection(Arg1, Arg2, a3, (uint32_t)((uint32_t)(local_rsi)));
    if ((uint8_t)(result) == 0) {
        Arg1 = 160;
        result = KeBugCheck(Arg1, Arg2, a3, (uint32_t)((uint32_t)(local_rsi)));
    }
loc_00C376F4:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x38F386))))) goto loc_00C3772F;
    result = KiInitializeThreadCycleTable(*(uint64_t *)(v_rip - 0xC37507 + 0x0 * 8 + 0xFC8C40), Arg2, a3, (uint32_t)((uint32_t)(local_rsi)));
    if (sign_flag) goto loc_00C37716;
    local_rbx = (uint32_t)((0) + ((uint32_t)(local_rdi + 1)));
    goto loc_00C376F4;
loc_00C37716:
    a4 = 0;
    v_stack_m758 = 0;
    result = KeBugCheckEx(a4 + 50, (int32_t)((uint32_t)(result)), a4 + 12, a4);
loc_00C3772F:
    result = KiConfigureAllSchedulingInformation(a4 + 50, (int32_t)((uint32_t)(result)), a4 + 12, a4);
    Arg2 = 0;
    result = guard_dispatch_icall((uint8_t)(local_rdi + 1), Arg2, a4 + 12, a4);
    *(uint32_t *)(v_rip + 0x38F723) = (uint32_t)(local_rdi + 1);
    result = KeQueryActiveProcessorCountEx((uint32_t)(0xFFFFULL), Arg2, a4 + 12, a4);
    *(uint32_t *)(v_rip + 0x38F880) = (uint32_t)(result);
    *(uint32_t *)(v_rip + 0x38F4E7) = 0;
    result = KeWakeAddressAll(v_rip + 3732717, Arg2, a4 + 12, a4);
    Arg1 = (*(uint64_t *)(local_rsp - 0x678 + 0x640)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, a4 + 12, a4);
    return result;
loc_00C3779F:
    local_rdi = 0;
loc_00C377A1:
    Arg2 = 0;
    v_stack_m730 = 0;
    a3 = 0;
    result = KeBugCheckEx(Arg2 + 50, Arg2, a3, 20);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C36F78&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
