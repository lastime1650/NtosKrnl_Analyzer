# KeInitSystem

- RVA: `0x00C71660`–`0x00C71C73` (길이 `1,555` bytes)
- VA: `0x0000000140C71660`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BAF48`
- 디코드: `346`개 명령, `1,555/1,555` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **43**; 고유 호출 대상: **38**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **62**

### Outgoing calls
- `0x00C716E3` → [KiDetectTsx](../../text/4E/KiDetectTsx_function_004E34FC.md) (function, `0x004E34FC`)
- `0x00C716F1` → [KiRcuSystemInitialize](KiRcuSystemInitialize_function_00C733A8.md) (function, `0x00C733A8`)
- `0x00C7174F` → [KeInitializeCatRegisters](../../text/4F/KeInitializeCatRegisters_function_004FAE74.md) (function, `0x004FAE74`)
- `0x00C71757` → [KeInitializeTimerTable](../../page/A9/KeInitializeTimerTable_function_00A9471C.md) (function, `0x00A9471C`)
- `0x00C71772` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C71778` → [KiInitializeVelocity](../BE/KiInitializeVelocity_function_00BEEDB8.md) (function, `0x00BEEDB8`)
- `0x00C7177D` → [KiInitializeAntiStarvationPolicies](../../text/4F/KiInitializeAntiStarvationPolicies_function_004F5B5C.md) (function, `0x004F5B5C`)
- `0x00C71794` → [KiInitDynamicTraceSupport](../C3/KiInitDynamicTraceSupport_function_00C3A450.md) (function, `0x00C3A450`)
- `0x00C7179E` → [KeQueryActiveProcessorCountEx](../../text/24/KeQueryActiveProcessorCountEx_function_00249EF0.md) (function, `0x00249EF0`)
- `0x00C717D6` → [HviIsAnyHypervisorPresent](../../text/4A/HviIsAnyHypervisorPresent_function_004ADC50.md) (function, `0x004ADC50`)
- `0x00C71823` → [KeRelaxTimingConstraints](../../text/5B/KeRelaxTimingConstraints_function_005B59C8.md) (function, `0x005B59C8`)
- `0x00C71828` → [KiInitDpcThresholds](../C3/KiInitDpcThresholds_function_00C38318.md) (function, `0x00C38318`)
- `0x00C71857` → [KiApplyDpcVerificationScaleSettings](../../text/5B/KiApplyDpcVerificationScaleSettings_function_005B7014.md) (function, `0x005B7014`)
- `0x00C71874` → [KiInitializeProcessor](../../pagelk/B6/KiInitializeProcessor_function_00B66A0C.md) (function, `0x00B66A0C`)
- `0x00C71885` → [KiStartDpcThread](../../page/74/KiStartDpcThread_function_00745628.md) (function, `0x00745628`)
- `0x00C71896` → [KiComputeNumaCosts](../C3/KiComputeNumaCosts_function_00C37AD4.md) (function, `0x00C37AD4`)
- `0x00C718A3` → [KiComputeDispatchInterruptCost](../C3/KiComputeDispatchInterruptCost_function_00C377C0.md) (function, `0x00C377C0`)
- `0x00C718B0` → [KiInitializeDpcRuntimeHistoryHashTables](../C3/KiInitializeDpcRuntimeHistoryHashTables_function_00C3A398.md) (function, `0x00C3A398`)
- `0x00C718DB` → [SymCryptInitEnvWindowsKernelmodeWin8_1nLater](../../text/51/SymCryptInitEnvWindowsKernelmodeWin8_1nLater_function_0051C948.md) (function, `0x0051C948`)
- `0x00C718E2` → [KiIntSteerInit](../C3/KiIntSteerInit_function_00C3A1CC.md) (function, `0x00C3A1CC`)
- `0x00C718E7` → [KiInitSupervisorStateExtensionHost](../C3/KiInitSupervisorStateExtensionHost_function_00C389EC.md) (function, `0x00C389EC`)
- `0x00C718EC` → [KiInitMachineDependent](../../text/5C/KiInitMachineDependent_function_005C1880.md) (function, `0x005C1880`)
- `0x00C719F2` → [KdEncodeDataBlock](../../text/5B/KdEncodeDataBlock_function_005B06B0.md) (function, `0x005B06B0`)
- `0x00C719F7` → [KiVerifyScopes](../C3/KiVerifyScopes_function_00C3A5E8.md) (function, `0x00C3A5E8`)
- `0x00C719FC` → [KiInitializeIdealProcessorRebalancer](../../text/5C/KiInitializeIdealProcessorRebalancer_function_005C1BA0.md) (function, `0x005C1BA0`)
- `0x00C71A61` → [TraceLoggingRegisterEx_EtwRegister_EtwSetInformation](../../page/92/TraceLoggingRegisterEx_EtwRegister_EtwSetInformation_function_009208A0.md) (function, `0x009208A0`)
- `0x00C71A72` → [TraceLoggingRegisterEx_EtwRegister_EtwSetInformation](../../page/92/TraceLoggingRegisterEx_EtwRegister_EtwSetInformation_function_009208A0.md) (function, `0x009208A0`)
- `0x00C71A99` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (function, `0x0042EAA0`)
- `0x00C71AEC` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x00C71AF6` → [KiIntSteerInit](../C3/KiIntSteerInit_function_00C3A1CC.md) (function, `0x00C3A1CC`)
- `0x00C71AFB` → [Feature_PpmParkEx__private_IsEnabledNoReportingNoInline](../../text/4F/Feature_PpmParkEx__private_IsEnabledNoReportingNoInline_function_004F40E0.md) (function, `0x004F40E0`)
- `0x00C71B3B` → [KeGetTopologySiblingGroupAffinityForProcessor](../../text/39/KeGetTopologySiblingGroupAffinityForProcessor_function_0039EEE4.md) (function, `0x0039EEE4`)
- `0x00C71B67` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (function, `0x0042EAA0`)
- `0x00C71BD5` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x00C71BE1` → [KiInitializeReservedCpuSets](../C3/KiInitializeReservedCpuSets_function_00C39DAC.md) (function, `0x00C39DAC`)
- `0x00C71BEF` → [ExAcquireFastMutexUnsafe](../../text/3F/ExAcquireFastMutexUnsafe_function_003F3720.md) (function, `0x003F3720`)
- `0x00C71BF4` → [MmFreeLoaderBlock](../C5/MmFreeLoaderBlock_function_00C5F2F0.md) (function, `0x00C5F2F0`)
- `0x00C71C07` → [ExReleaseFastMutexUnsafe](../../text/25/ExReleaseFastMutexUnsafe_function_002503A0.md) (function, `0x002503A0`)
- `0x00C71C0C` → [KiInitializeNormalPriorityAntiStarvationPolicies](../../text/5B/KiInitializeNormalPriorityAntiStarvationPolicies_function_005B8178.md) (function, `0x005B8178`)
- `0x00C71C1A` → [HviIsAnyHypervisorPresent](../../text/4A/HviIsAnyHypervisorPresent_function_004ADC50.md) (function, `0x004ADC50`)
- `0x00C71C29` → [KiEpfInitialize](../C3/KiEpfInitialize_function_00C39FC0.md) (function, `0x00C39FC0`)
- `0x00C71C2E` → [KeFreeInitializationCode](../BE/KeFreeInitializationCode_function_00BEFB10.md) (function, `0x00BEFB10`)
- `0x00C71C4C` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [InitBootProcessor](../C1/InitBootProcessor_function_00C1B1C8.md) at `0x00C1B4A8`
- [Phase1InitializationDiscard](../C1/Phase1InitializationDiscard_function_00C1C728.md) at `0x00C1D22D`
- [IoInitSystemPreDrivers](../C2/IoInitSystemPreDrivers_function_00C2AC3C.md) at `0x00C2B719`
- [Phase1InitializationIoReady](Phase1InitializationIoReady_function_00C70458.md) at `0x00C705F3`
- [Phase1InitializationIoReady](Phase1InitializationIoReady_function_00C70458.md) at `0x00C707B1`

### Static image references
- `0x00C71683` → RVA `0x00E0A740` (`.data`; read)
- `0x00C716A5` → RVA `0x00FC6B60` (`ALMOSTRO`; read)
- `0x00C716B2` → RVA `0x00FC6DD0` (`ALMOSTRO`; read)
- `0x00C716EB` → RVA `0x00FC6E7C` (`ALMOSTRO`; write)
- `0x00C71707` → RVA `0x00FC6E88` (`ALMOSTRO`; read)
- `0x00C7171A` → RVA `0x00FC6DC4` (`ALMOSTRO`; write)
- `0x00C7172D` → RVA `0x00FC504C` (`ALMOSTRO`; read)
- `0x00C7173A` → RVA `0x00FC504C` (`ALMOSTRO`; write)
- `0x00C71749` → RVA `0x00FC6D20` (`ALMOSTRO`; read/write)
- `0x00C717A3` → RVA `0x00FC6AA0` (`ALMOSTRO`; read)
- `0x00C717AE` → RVA `0x00F234F8` (`.data`; write)
- `0x00C717C7` → RVA `0x00FC6E94` (`ALMOSTRO`; read)
- `0x00C717CE` → RVA `0x00FC5006` (`ALMOSTRO`; write)
- `0x00C717DF` → RVA `0x00FC6A97` (`ALMOSTRO`; read)
- `0x00C717E8` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)
- `0x00C717F9` → RVA `0x00FC502C` (`ALMOSTRO`; write)
- `0x00C71800` → RVA `0x00FC5034` (`ALMOSTRO`; write)
- `0x00C71807` → RVA `0x00FC5040` (`ALMOSTRO`; write)
- `0x00C7180E` → RVA `0x00FC503C` (`ALMOSTRO`; write)
- `0x00C71815` → RVA `0x00FC5024` (`ALMOSTRO`; write)
- `0x00C7181C` → RVA `0x00FC5028` (`ALMOSTRO`; write)
- `0x00C7182D` → RVA `0x00F04984` (`.data`; read)
- `0x00C71836` → RVA `0x00FC5058` (`ALMOSTRO`; read)
- `0x00C71842` → RVA `0x00FC5058` (`ALMOSTRO`; write)
- `0x00C7185F` → RVA `0x00FC8C40` (`ALMOSTRO`; read)
- `0x00C71879` → RVA `0x00FC519C` (`ALMOSTRO`; read)
- `0x00C718BD` → RVA `0x01201841` (`CFGRO`; read)
- `0x00C718C6` → RVA `0x00FC80A0` (`ALMOSTRO`; write)
- `0x00C718CC` → RVA `0x00FC80A8` (`ALMOSTRO`; write)
- `0x00C7193D` → RVA `0x00FC6DBC` (`ALMOSTRO`; write)
- `0x00C71949` → RVA `0x00FC6B38` (`ALMOSTRO`; read)
- `0x00C71953` → RVA `0x00FC5098` (`ALMOSTRO`; write)
- `0x00C71959` → RVA `0x00FC6DB4` (`ALMOSTRO`; write)
- `0x00C71962` → RVA `0x00FC6C4C` (`ALMOSTRO`; write)
- `0x00C71983` → RVA `0x00FC51CC` (`ALMOSTRO`; read)
- `0x00C71994` → RVA `0x00FC6FE4` (`ALMOSTRO`; write)
- `0x00C719A4` → RVA `0x00FC51CC` (`ALMOSTRO`; write)
- `0x00C719AA` → RVA `0x00FC51D0` (`ALMOSTRO`; read)
- `0x00C719B3` → RVA `0x00FC51D0` (`ALMOSTRO`; write)
- `0x00C719C6` → RVA `0x00FC6FF8` (`ALMOSTRO`; write)
- `0x00C719CC` → RVA `0x00FC53E4` (`ALMOSTRO`; read)
- `0x00C719D6` → RVA `0x00FC53F0` (`ALMOSTRO`; read)
- `0x00C719DC` → RVA `0x00FC53E8` (`ALMOSTRO`; write)
- `0x00C719EB` → RVA `0x00FC53F8` (`ALMOSTRO`; write)
- `0x00C71A01` → RVA `0x005C7A70` (`KiPristineTriageDumpAllocationWorker`; read)
- `0x00C71A08` → RVA `0x00F108A0` (`.data`; write)
- `0x00C71A12` → RVA `0x00F108D8` (`.data`; write)
- `0x00C71A19` → RVA `0x00F108C0` (`.data`; write)
- `0x00C71A23` → RVA `0x00F108E0` (`.data`; write)
- `0x00C71A2A` → RVA `0x00F108F8` (`.data`; write)
- `0x00C71A31` → RVA `0x00F108D0` (`.data`; write)
- `0x00C71A4D` → RVA `0x00E070A0` (`.data`; read)
- `0x00C71A57` → RVA `0x006FF9C0` (`KiTraceLogControlCallback`; read)
- `0x00C71A69` → RVA `0x00E070D8` (`.data`; read)
- `0x00C71A77` → RVA `0x00FC6DCC` (`ALMOSTRO`; read)
- `0x00C71AB7` → RVA `0x0005AE12` (`.rdata`; read)
- `0x00C71B12` → RVA `0x00FC6A80` (`ALMOSTRO`; read)
- `0x00C71B80` → RVA `0x0005ADC4` (`.rdata`; read)
- `0x00C71BE8` → RVA `0x00F22B80` (`.data`; read)
- `0x00C71C00` → RVA `0x00FC6B20` (`ALMOSTRO`; write)
- `0x00C71C23` → RVA `0x00FC6AF3` (`ALMOSTRO`; write)
- `0x00C71C3D` → RVA `0x0100870C` (`INITDATA`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **28**
  - `0x00C716E3` → [KiDetectTsx](../../text/4E/KiDetectTsx_function_004E34FC.md) (`INIT` → `.text`)
  - `0x00C7174F` → [KeInitializeCatRegisters](../../text/4F/KeInitializeCatRegisters_function_004FAE74.md) (`INIT` → `.text`)
  - `0x00C71757` → [KeInitializeTimerTable](../../page/A9/KeInitializeTimerTable_function_00A9471C.md) (`INIT` → `PAGE`)
  - `0x00C71772` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C7177D` → [KiInitializeAntiStarvationPolicies](../../text/4F/KiInitializeAntiStarvationPolicies_function_004F5B5C.md) (`INIT` → `.text`)
  - `0x00C7179E` → [KeQueryActiveProcessorCountEx](../../text/24/KeQueryActiveProcessorCountEx_function_00249EF0.md) (`INIT` → `.text`)
  - `0x00C717D6` → [HviIsAnyHypervisorPresent](../../text/4A/HviIsAnyHypervisorPresent_function_004ADC50.md) (`INIT` → `.text`)
  - `0x00C71823` → [KeRelaxTimingConstraints](../../text/5B/KeRelaxTimingConstraints_function_005B59C8.md) (`INIT` → `.text`)
  - `0x00C71857` → [KiApplyDpcVerificationScaleSettings](../../text/5B/KiApplyDpcVerificationScaleSettings_function_005B7014.md) (`INIT` → `.text`)
  - `0x00C71874` → [KiInitializeProcessor](../../pagelk/B6/KiInitializeProcessor_function_00B66A0C.md) (`INIT` → `PAGELK`)
  - `0x00C71885` → [KiStartDpcThread](../../page/74/KiStartDpcThread_function_00745628.md) (`INIT` → `PAGE`)
  - `0x00C718DB` → [SymCryptInitEnvWindowsKernelmodeWin8_1nLater](../../text/51/SymCryptInitEnvWindowsKernelmodeWin8_1nLater_function_0051C948.md) (`INIT` → `.text`)
  - `0x00C718EC` → [KiInitMachineDependent](../../text/5C/KiInitMachineDependent_function_005C1880.md) (`INIT` → `.text`)
  - `0x00C719F2` → [KdEncodeDataBlock](../../text/5B/KdEncodeDataBlock_function_005B06B0.md) (`INIT` → `.text`)
  - `0x00C719FC` → [KiInitializeIdealProcessorRebalancer](../../text/5C/KiInitializeIdealProcessorRebalancer_function_005C1BA0.md) (`INIT` → `.text`)
  - `0x00C71A61` → [TraceLoggingRegisterEx_EtwRegister_EtwSetInformation](../../page/92/TraceLoggingRegisterEx_EtwRegister_EtwSetInformation_function_009208A0.md) (`INIT` → `PAGE`)
  - `0x00C71A72` → [TraceLoggingRegisterEx_EtwRegister_EtwSetInformation](../../page/92/TraceLoggingRegisterEx_EtwRegister_EtwSetInformation_function_009208A0.md) (`INIT` → `PAGE`)
  - `0x00C71A99` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (`INIT` → `.text`)
  - `0x00C71AEC` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (`INIT` → `.text`)
  - `0x00C71AFB` → [Feature_PpmParkEx__private_IsEnabledNoReportingNoInline](../../text/4F/Feature_PpmParkEx__private_IsEnabledNoReportingNoInline_function_004F40E0.md) (`INIT` → `.text`)
  - `0x00C71B3B` → [KeGetTopologySiblingGroupAffinityForProcessor](../../text/39/KeGetTopologySiblingGroupAffinityForProcessor_function_0039EEE4.md) (`INIT` → `.text`)
  - `0x00C71B67` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (`INIT` → `.text`)
  - `0x00C71BD5` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (`INIT` → `.text`)
  - `0x00C71BEF` → [ExAcquireFastMutexUnsafe](../../text/3F/ExAcquireFastMutexUnsafe_function_003F3720.md) (`INIT` → `.text`)
  - `0x00C71C07` → [ExReleaseFastMutexUnsafe](../../text/25/ExReleaseFastMutexUnsafe_function_002503A0.md) (`INIT` → `.text`)
  - `0x00C71C0C` → [KiInitializeNormalPriorityAntiStarvationPolicies](../../text/5B/KiInitializeNormalPriorityAntiStarvationPolicies_function_005B8178.md) (`INIT` → `.text`)
  - `0x00C71C1A` → [HviIsAnyHypervisorPresent](../../text/4A/HviIsAnyHypervisorPresent_function_004ADC50.md) (`INIT` → `.text`)
  - `0x00C71C4C` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`INIT` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C71660  48 8B C4                        mov rax, rsp
00C71663  48 89 58 08                     mov qword ptr [rax + 8], rbx
00C71667  48 89 70 10                     mov qword ptr [rax + 0x10], rsi
00C7166B  48 89 78 18                     mov qword ptr [rax + 0x18], rdi
00C7166F  4C 89 60 20                     mov qword ptr [rax + 0x20], r12
00C71673  55                              push rbp
00C71674  41 56                           push r14
00C71676  41 57                           push r15
00C71678  48 8D 68 A1                     lea rbp, [rax - 0x5f]
00C7167C  48 81 EC B0 00 00 00            sub rsp, 0xb0
00C71683  48 8B 05 B6 90 19 00            mov rax, qword ptr [rip + 0x1990b6]
00C7168A  48 33 C4                        xor rax, rsp
00C7168D  48 89 45 37                     mov qword ptr [rbp + 0x37], rax
00C71691  45 33 E4                        xor r12d, r12d
00C71694  85 C9                           test ecx, ecx
00C71696  0F 85 EB 00 00 00               jne 0x140c71787
00C7169C  65 48 8B 3C 25 20 00 00 00      mov rdi, qword ptr gs:[0x20]
00C716A5  48 F7 05 B0 54 35 00 00 80 00 00  test qword ptr [rip + 0x3554b0], 0x8000
00C716B0  74 31                           je 0x140c716e3
00C716B2  44 39 25 17 57 35 00            cmp dword ptr [rip + 0x355717], r12d
00C716B9  74 28                           je 0x140c716e3
00C716BB  48 8B 97 00 2D 00 00            mov rdx, qword ptr [rdi + 0x2d00]
00C716C2  8A C2                           mov al, dl
00C716C4  24 03                           and al, 3
00C716C6  3C 03                           cmp al, 3
00C716C8  74 19                           je 0x140c716e3
00C716CA  48 83 CA 03                     or rdx, 3
00C716CE  B9 22 01 00 00                  mov ecx, 0x122
00C716D3  48 89 97 00 2D 00 00            mov qword ptr [rdi + 0x2d00], rdx
00C716DA  48 8B C2                        mov rax, rdx
00C716DD  48 C1 EA 20                     shr rdx, 0x20
00C716E1  0F 30                           wrmsr
00C716E3  E8 14 1E 87 FF                  call 0x1404e34fc
00C716E8  48 8B CF                        mov rcx, rdi
00C716EB  89 05 8B 57 35 00               mov dword ptr [rip + 0x35578b], eax
00C716F1  E8 B2 1C 00 00                  call 0x140c733a8
00C716F6  41 8B C4                        mov eax, r12d
00C716F9  BB 01 00 00 00                  mov ebx, 1
00C716FE  4C 39 A7 B8 8E 00 00            cmp qword ptr [rdi + 0x8eb8], r12
00C71705  74 13                           je 0x140c7171a
00C71707  8B 0D 7B 57 35 00               mov ecx, dword ptr [rip + 0x35577b]
00C7170D  8B C3                           mov eax, ebx
00C7170F  3B CB                           cmp ecx, ebx
00C71711  74 07                           je 0x140c7171a
00C71713  83 F9 02                        cmp ecx, 2
00C71716  41 0F 44 C4                     cmove eax, r12d
00C7171A  89 05 A4 56 35 00               mov dword ptr [rip + 0x3556a4], eax
00C71720  85 C0                           test eax, eax
00C71722  74 09                           je 0x140c7172d
00C71724  48 8B 47 18                     mov rax, qword ptr [rdi + 0x18]
00C71728  F0 0F BA 28 16                  lock bts dword ptr [rax], 0x16
00C7172D  8B 05 19 39 35 00               mov eax, dword ptr [rip + 0x353919]
00C71733  FF C8                           dec eax
00C71735  83 F8 1E                        cmp eax, 0x1e
00C71738  76 06                           jbe 0x140c71740
00C7173A  89 1D 0C 39 35 00               mov dword ptr [rip + 0x35390c], ebx
00C71740  4C 39 A7 B8 8E 00 00            cmp qword ptr [rdi + 0x8eb8], r12
00C71747  74 06                           je 0x140c7174f
00C71749  09 1D D1 55 35 00               or dword ptr [rip + 0x3555d1], ebx
00C7174F  E8 20 97 88 FF                  call 0x1404fae74
00C71754  48 8B CF                        mov rcx, rdi
00C71757  E8 C0 2F E2 FF                  call 0x140a9471c
00C7175C  85 C0                           test eax, eax
00C7175E  79 18                           jns 0x140c71778
00C71760  45 33 C9                        xor r9d, r9d
00C71763  48 63 D0                        movsxd rdx, eax
00C71766  4C 8B C3                        mov r8, rbx
00C71769  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
00C7176E  41 8D 49 31                     lea ecx, [r9 + 0x31]
00C71772  E8 E9 BE 88 FF                  call 0x1404fd660
00C71777  CC                              int3
00C71778  E8 3B D6 F7 FF                  call 0x140beedb8
00C7177D  E8 DA 43 88 FF                  call 0x1404f5b5c
00C71782  E9 BC 04 00 00                  jmp 0x140c71c43
00C71787  BB 01 00 00 00                  mov ebx, 1
00C7178C  3B CB                           cmp ecx, ebx
00C7178E  0F 85 B0 02 00 00               jne 0x140c71a44
00C71794  E8 B7 8C FC FF                  call 0x140c3a450
00C71799  B9 FF FF 00 00                  mov ecx, 0xffff
00C7179E  E8 4D 87 5D FF                  call 0x140249ef0
00C717A3  8B 0D F7 52 35 00               mov ecx, dword ptr [rip + 0x3552f7]
00C717A9  44 8B F8                        mov r15d, eax
00C717AC  33 D2                           xor edx, edx
00C717AE  4C 89 25 43 1D 2B 00            mov qword ptr [rip + 0x2b1d43], r12
00C717B5  8D 81 7F C3 C9 01               lea eax, [rcx + 0x1c9c37f]
00C717BB  F7 F1                           div ecx
00C717BD  33 D2                           xor edx, edx
00C717BF  FF C8                           dec eax
00C717C1  41 03 C7                        add eax, r15d
00C717C4  41 F7 F7                        div r15d
00C717C7  44 39 25 C6 56 35 00            cmp dword ptr [rip + 0x3556c6], r12d
00C717CE  88 05 32 38 35 00               mov byte ptr [rip + 0x353832], al
00C717D4  75 52                           jne 0x140c71828
00C717D6  E8 75 C4 83 FF                  call 0x1404adc50
00C717DB  84 C0                           test al, al
00C717DD  74 49                           je 0x140c71828
00C717DF  44 38 25 B1 52 35 00            cmp byte ptr [rip + 0x3552b1], r12b
00C717E6  74 0F                           je 0x140c717f7
00C717E8  8B 05 CA 52 35 00               mov eax, dword ptr [rip + 0x3552ca]
00C717EE  A8 20                           test al, 0x20
00C717F0  75 05                           jne 0x140c717f7
00C717F2  41 8B CC                        mov ecx, r12d
00C717F5  EB 2C                           jmp 0x140c71823
00C717F7  8B CB                           mov ecx, ebx
00C717F9  44 89 25 2C 38 35 00            mov dword ptr [rip + 0x35382c], r12d
00C71800  44 89 25 2D 38 35 00            mov dword ptr [rip + 0x35382d], r12d
00C71807  44 89 25 32 38 35 00            mov dword ptr [rip + 0x353832], r12d
00C7180E  44 89 25 27 38 35 00            mov dword ptr [rip + 0x353827], r12d
00C71815  44 89 25 08 38 35 00            mov dword ptr [rip + 0x353808], r12d
00C7181C  44 89 25 05 38 35 00            mov dword ptr [rip + 0x353805], r12d
00C71823  E8 A0 41 94 FF                  call 0x1405b59c8
00C71828  E8 EB 6A FC FF                  call 0x140c38318
00C7182D  44 39 25 50 31 29 00            cmp dword ptr [rip + 0x293150], r12d
00C71834  74 26                           je 0x140c7185c
00C71836  8B 05 1C 38 35 00               mov eax, dword ptr [rip + 0x35381c]
00C7183C  3B C3                           cmp eax, ebx
00C7183E  73 08                           jae 0x140c71848
00C71840  8B C3                           mov eax, ebx
00C71842  89 1D 10 38 35 00               mov dword ptr [rip + 0x353810], ebx
00C71848  83 F8 64                        cmp eax, 0x64
00C7184B  76 0A                           jbe 0x140c71857
00C7184D  C7 05 01 38 35 00 64 00 00 00   mov dword ptr [rip + 0x353801], 0x64
00C71857  E8 B8 57 94 FF                  call 0x1405b7014
00C7185C  41 8B FC                        mov edi, r12d
00C7185F  48 8D 35 DA 73 35 00            lea rsi, [rip + 0x3573da]
00C71866  41 3B FF                        cmp edi, r15d
00C71869  73 2B                           jae 0x140c71896
00C7186B  8B C7                           mov eax, edi
00C7186D  4C 8B 34 C6                     mov r14, qword ptr [rsi + rax*8]
00C71871  49 8B CE                        mov rcx, r14
00C71874  E8 93 51 EF FF                  call 0x140b66a0c
00C71879  44 39 25 1C 39 35 00            cmp dword ptr [rip + 0x35391c], r12d
00C71880  74 10                           je 0x140c71892
00C71882  49 8B CE                        mov rcx, r14
00C71885  E8 9E 3D AD FF                  call 0x140745628
00C7188A  85 C0                           test eax, eax
00C7188C  0F 88 AB 01 00 00               js 0x140c71a3d
00C71892  03 FB                           add edi, ebx
00C71894  EB D0                           jmp 0x140c71866
00C71896  E8 39 62 FC FF                  call 0x140c37ad4
00C7189B  84 C0                           test al, al
00C7189D  0F 84 9A 01 00 00               je 0x140c71a3d
00C718A3  E8 18 5F FC FF                  call 0x140c377c0
00C718A8  85 C0                           test eax, eax
00C718AA  0F 88 8D 01 00 00               js 0x140c71a3d
00C718B0  E8 E3 8A FC FF                  call 0x140c3a398
00C718B5  85 C0                           test eax, eax
00C718B7  0F 88 80 01 00 00               js 0x140c71a3d
00C718BD  44 38 25 7D FF 58 00            cmp byte ptr [rip + 0x58ff7d], r12b
00C718C4  74 10                           je 0x140c718d6
00C718C6  88 1D D4 67 35 00               mov byte ptr [rip + 0x3567d4], bl
00C718CC  C7 05 D2 67 35 00 0A 00 00 00   mov dword ptr [rip + 0x3567d2], 0xa
00C718D6  B9 0C 00 67 00                  mov ecx, 0x67000c
00C718DB  E8 68 B0 8A FF                  call 0x14051c948
00C718E0  8B CB                           mov ecx, ebx
00C718E2  E8 E5 88 FC FF                  call 0x140c3a1cc
00C718E7  E8 00 71 FC FF                  call 0x140c389ec
00C718EC  E8 8F FF 94 FF                  call 0x1405c1880
00C718F1  84 C0                           test al, al
00C718F3  0F 84 44 01 00 00               je 0x140c71a3d
00C718F9  4C 8B 05 40 73 35 00            mov r8, qword ptr [rip + 0x357340]
00C71900  48 B8 CD CC CC CC CC CC CC CC   movabs rax, 0xcccccccccccccccd
00C7190A  8B 0D 90 51 35 00               mov ecx, dword ptr [rip + 0x355190]
00C71910  45 8B 48 44                     mov r9d, dword ptr [r8 + 0x44]
00C71914  49 0F AF C9                     imul rcx, r9
00C71918  48 F7 E1                        mul rcx
00C7191B  48 B8 89 88 88 88 88 88 88 88   movabs rax, 0x8888888888888889
00C71925  48 8B CA                        mov rcx, rdx
00C71928  48 C1 E9 03                     shr rcx, 3
00C7192C  48 F7 E1                        mul rcx
00C7192F  48 B8 AB AA AA AA AA AA AA AA   movabs rax, 0xaaaaaaaaaaaaaaab
00C71939  48 C1 EA 07                     shr rdx, 7
00C7193D  89 15 79 54 35 00               mov dword ptr [rip + 0x355479], edx
00C71943  48 F7 E1                        mul rcx
00C71946  48 D1 EA                        shr rdx, 1
00C71949  F7 05 E5 51 35 00 00 00 04 00   test dword ptr [rip + 0x3551e5], 0x40000
00C71953  89 15 3F 37 35 00               mov dword ptr [rip + 0x35373f], edx
00C71959  89 15 55 54 35 00               mov dword ptr [rip + 0x355455], edx
00C7195F  8D 04 52                        lea eax, [rdx + rdx*2]
00C71962  89 05 E4 52 35 00               mov dword ptr [rip + 0x3552e4], eax
00C71968  74 19                           je 0x140c71983
00C7196A  B8 AB AA AA AA                  mov eax, 0xaaaaaaab
00C7196F  F7 E2                           mul edx
00C71971  C1 EA 02                        shr edx, 2
00C71974  89 15 1E 37 35 00               mov dword ptr [rip + 0x35371e], edx
00C7197A  8D 04 12                        lea eax, [rdx + rdx]
00C7197D  89 05 C9 52 35 00               mov dword ptr [rip + 0x3552c9], eax
00C71983  8B 15 43 38 35 00               mov edx, dword ptr [rip + 0x353843]
00C71989  49 69 C1 80 8D 5B 00            imul rax, r9, 0x5b8d80
00C71990  48 0F BD C8                     bsr rcx, rax
00C71994  89 0D 4A 56 35 00               mov dword ptr [rip + 0x35564a], ecx
00C7199A  83 FA 32                        cmp edx, 0x32
00C7199D  73 0B                           jae 0x140c719aa
00C7199F  BA 32 00 00 00                  mov edx, 0x32
00C719A4  89 15 22 38 35 00               mov dword ptr [rip + 0x353822], edx
00C719AA  83 3D 1F 38 35 00 02            cmp dword ptr [rip + 0x35381f], 2
00C719B1  73 0A                           jae 0x140c719bd
00C719B3  C7 05 13 38 35 00 02 00 00 00   mov dword ptr [rip + 0x353813], 2
00C719BD  41 8B 48 44                     mov ecx, dword ptr [r8 + 0x44]
00C719C1  8B C1                           mov eax, ecx
00C719C3  0F AF C2                        imul eax, edx
00C719C6  89 05 2C 56 35 00               mov dword ptr [rip + 0x35562c], eax
00C719CC  8B 05 12 3A 35 00               mov eax, dword ptr [rip + 0x353a12]
00C719D2  48 0F AF C1                     imul rax, rcx
00C719D6  8B 0D 14 3A 35 00               mov ecx, dword ptr [rip + 0x353a14]
00C719DC  48 89 05 05 3A 35 00            mov qword ptr [rip + 0x353a05], rax
00C719E3  41 8B 40 44                     mov eax, dword ptr [r8 + 0x44]
00C719E7  48 0F AF C8                     imul rcx, rax
00C719EB  48 89 0D 06 3A 35 00            mov qword ptr [rip + 0x353a06], rcx
00C719F2  E8 B9 EC 93 FF                  call 0x1405b06b0
00C719F7  E8 EC 8B FC FF                  call 0x140c3a5e8
00C719FC  E8 9F 01 95 FF                  call 0x1405c1ba0
00C71A01  48 8D 05 68 60 95 FF            lea rax, [rip - 0x6a9f98]
00C71A08  C7 05 8E EE 29 00 00 18 04 00   mov dword ptr [rip + 0x29ee8e], 0x41800
00C71A12  48 89 05 BF EE 29 00            mov qword ptr [rip + 0x29eebf], rax
00C71A19  C7 05 9D EE 29 00 13 01 00 00   mov dword ptr [rip + 0x29ee9d], 0x113
00C71A23  4C 89 25 B6 EE 29 00            mov qword ptr [rip + 0x29eeb6], r12
00C71A2A  4C 89 25 C7 EE 29 00            mov qword ptr [rip + 0x29eec7], r12
00C71A31  4C 89 25 98 EE 29 00            mov qword ptr [rip + 0x29ee98], r12
00C71A38  E9 06 02 00 00                  jmp 0x140c71c43
00C71A3D  32 C0                           xor al, al
00C71A3F  E9 01 02 00 00                  jmp 0x140c71c45
00C71A44  83 F9 02                        cmp ecx, 2
00C71A47  0F 85 8F 01 00 00               jne 0x140c71bdc
00C71A4D  4C 8D 3D 4C 56 19 00            lea r15, [rip + 0x19564c]
00C71A54  4D 8B C7                        mov r8, r15
00C71A57  48 8D 15 62 DF A8 FF            lea rdx, [rip - 0x57209e]
00C71A5E  49 8B CF                        mov rcx, r15
00C71A61  E8 3A EE CA FF                  call 0x1409208a0
00C71A66  45 33 C0                        xor r8d, r8d
00C71A69  48 8D 0D 68 56 19 00            lea rcx, [rip + 0x195668]
00C71A70  33 D2                           xor edx, edx
00C71A72  E8 29 EE CA FF                  call 0x1409208a0
00C71A77  44 8B 05 4E 53 35 00            mov r8d, dword ptr [rip + 0x35534e]
00C71A7E  45 85 C0                        test r8d, r8d
00C71A81  74 6E                           je 0x140c71af1
00C71A83  83 3D 16 56 19 00 05            cmp dword ptr [rip + 0x195616], 5
00C71A8A  76 65                           jbe 0x140c71af1
00C71A8C  48 BA 00 00 00 00 00 40 00 00   movabs rdx, 0x400000000000
00C71A96  49 8B CF                        mov rcx, r15
00C71A99  E8 02 D0 7B FF                  call 0x14042eaa0
00C71A9E  84 C0                           test al, al
00C71AA0  74 4F                           je 0x140c71af1
00C71AA2  B9 04 00 00 00                  mov ecx, 4
00C71AA7  44 89 45 C7                     mov dword ptr [rbp - 0x39], r8d
00C71AAB  48 8D 45 C7                     lea rax, [rbp - 0x39]
00C71AAF  48 89 4D 0F                     mov qword ptr [rbp + 0xf], rcx
00C71AB3  48 89 45 07                     mov qword ptr [rbp + 7], rax
00C71AB7  48 8D 15 54 93 3E FF            lea rdx, [rip - 0xc16cac]
00C71ABE  48 8D 45 CF                     lea rax, [rbp - 0x31]
00C71AC2  48 C7 45 CF 00 00 00 01         mov qword ptr [rbp - 0x31], 0x1000000
00C71ACA  48 89 45 17                     mov qword ptr [rbp + 0x17], rax
00C71ACE  45 33 C9                        xor r9d, r9d
00C71AD1  48 8D 45 E7                     lea rax, [rbp - 0x19]
00C71AD5  48 C7 45 1F 08 00 00 00         mov qword ptr [rbp + 0x1f], 8
00C71ADD  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00C71AE2  45 33 C0                        xor r8d, r8d
00C71AE5  89 4C 24 20                     mov dword ptr [rsp + 0x20], ecx
00C71AE9  49 8B CF                        mov rcx, r15
00C71AEC  E8 EF 45 7B FF                  call 0x1404260e0
00C71AF1  B9 02 00 00 00                  mov ecx, 2
00C71AF6  E8 D1 86 FC FF                  call 0x140c3a1cc
00C71AFB  E8 E0 25 88 FF                  call 0x1404f40e0
00C71B00  85 C0                           test eax, eax
00C71B02  0F 84 3B 01 00 00               je 0x140c71c43
00C71B08  41 8B FC                        mov edi, r12d
00C71B0B  48 8D 35 2E 71 35 00            lea rsi, [rip + 0x35712e]
00C71B12  3B 3D 68 4F 35 00               cmp edi, dword ptr [rip + 0x354f68]
00C71B18  0F 83 25 01 00 00               jae 0x140c71c43
00C71B1E  8B C7                           mov eax, edi
00C71B20  4C 8D 45 D7                     lea r8, [rbp - 0x29]
00C71B24  0F 57 C0                        xorps xmm0, xmm0
00C71B27  BA 05 00 00 00                  mov edx, 5
00C71B2C  0F 11 45 D7                     movups xmmword ptr [rbp - 0x29], xmm0
00C71B30  48 8B 0C C6                     mov rcx, qword ptr [rsi + rax*8]
00C71B34  4C 8B B1 70 8E 00 00            mov r14, qword ptr [rcx + 0x8e70]
00C71B3B  E8 A4 D3 72 FF                  call 0x14039eee4
00C71B40  4C 8B 45 D7                     mov r8, qword ptr [rbp - 0x29]
00C71B44  4D 3B F0                        cmp r14, r8
00C71B47  75 04                           jne 0x140c71b4d
00C71B49  03 FB                           add edi, ebx
00C71B4B  EB C5                           jmp 0x140c71b12
00C71B4D  83 3D 4C 55 19 00 05            cmp dword ptr [rip + 0x19554c], 5
00C71B54  0F 86 E9 00 00 00               jbe 0x140c71c43
00C71B5A  48 BA 00 00 00 00 00 40 00 00   movabs rdx, 0x400000000000
00C71B64  49 8B CF                        mov rcx, r15
00C71B67  E8 34 CF 7B FF                  call 0x14042eaa0
00C71B6C  84 C0                           test al, al
00C71B6E  0F 84 CF 00 00 00               je 0x140c71c43
00C71B74  48 8D 45 CF                     lea rax, [rbp - 0x31]
00C71B78  4C 89 45 CF                     mov qword ptr [rbp - 0x31], r8
00C71B7C  48 89 45 07                     mov qword ptr [rbp + 7], rax
00C71B80  48 8D 15 3D 92 3E FF            lea rdx, [rip - 0xc16dc3]
00C71B87  48 8D 45 C7                     lea rax, [rbp - 0x39]
00C71B8B  48 C7 45 0F 08 00 00 00         mov qword ptr [rbp + 0xf], 8
00C71B93  48 89 45 17                     mov qword ptr [rbp + 0x17], rax
00C71B97  45 33 C9                        xor r9d, r9d
00C71B9A  48 8D 45 D7                     lea rax, [rbp - 0x29]
00C71B9E  4C 89 75 C7                     mov qword ptr [rbp - 0x39], r14
00C71BA2  48 89 45 27                     mov qword ptr [rbp + 0x27], rax
00C71BA6  45 33 C0                        xor r8d, r8d
00C71BA9  48 8D 45 E7                     lea rax, [rbp - 0x19]
00C71BAD  48 C7 45 1F 08 00 00 00         mov qword ptr [rbp + 0x1f], 8
00C71BB5  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00C71BBA  49 8B CF                        mov rcx, r15
00C71BBD  C7 44 24 20 05 00 00 00         mov dword ptr [rsp + 0x20], 5
00C71BC5  48 C7 45 D7 00 00 00 01         mov qword ptr [rbp - 0x29], 0x1000000
00C71BCD  48 C7 45 2F 08 00 00 00         mov qword ptr [rbp + 0x2f], 8
00C71BD5  E8 06 45 7B FF                  call 0x1404260e0
00C71BDA  EB 67                           jmp 0x140c71c43
00C71BDC  83 F9 03                        cmp ecx, 3
00C71BDF  75 07                           jne 0x140c71be8
00C71BE1  E8 C6 81 FC FF                  call 0x140c39dac
00C71BE6  EB 5B                           jmp 0x140c71c43
00C71BE8  48 8D 0D 91 0F 2B 00            lea rcx, [rip + 0x2b0f91]
00C71BEF  E8 2C 1B 78 FF                  call 0x1403f3720
00C71BF4  E8 F7 D6 FE FF                  call 0x140c5f2f0
00C71BF9  48 8D 0D 80 0F 2B 00            lea rcx, [rip + 0x2b0f80]
00C71C00  4C 89 25 19 4F 35 00            mov qword ptr [rip + 0x354f19], r12
00C71C07  E8 94 E7 5D FF                  call 0x1402503a0
00C71C0C  E8 67 65 94 FF                  call 0x1405b8178
00C71C11  44 39 25 7C 52 35 00            cmp dword ptr [rip + 0x35527c], r12d
00C71C18  75 09                           jne 0x140c71c23
00C71C1A  E8 31 C0 83 FF                  call 0x1404adc50
00C71C1F  84 C0                           test al, al
00C71C21  75 06                           jne 0x140c71c29
00C71C23  88 1D CA 4E 35 00               mov byte ptr [rip + 0x354eca], bl
00C71C29  E8 92 83 FC FF                  call 0x140c39fc0
00C71C2E  E8 DD DE F7 FF                  call 0x140befb10
00C71C33  48 B8 EB EB EB EB EB EB EB EB   movabs rax, 0xebebebebebebebeb
00C71C3D  89 05 C9 6A 39 00               mov dword ptr [rip + 0x396ac9], eax
00C71C43  8A C3                           mov al, bl
00C71C45  48 8B 4D 37                     mov rcx, qword ptr [rbp + 0x37]
00C71C49  48 33 CC                        xor rcx, rsp
00C71C4C  E8 EF A9 A3 FF                  call 0x1406ac640
00C71C51  4C 8D 9C 24 B0 00 00 00         lea r11, [rsp + 0xb0]
00C71C59  49 8B 5B 20                     mov rbx, qword ptr [r11 + 0x20]
00C71C5D  49 8B 73 28                     mov rsi, qword ptr [r11 + 0x28]
00C71C61  49 8B 7B 30                     mov rdi, qword ptr [r11 + 0x30]
00C71C65  4D 8B 63 38                     mov r12, qword ptr [r11 + 0x38]
00C71C69  49 8B E3                        mov rsp, r11
00C71C6C  41 5F                           pop r15
00C71C6E  41 5E                           pop r14
00C71C70  5D                              pop rbp
00C71C71  C3                              ret
00C71C72  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KeInitSystem(int a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 24) = v_rdi;
    *(unsigned __int64 *)(v_rsp + 32) = v_r12;
    v_rsp = (v_rsp) - (176);
    result = (*(unsigned __int64 *)(v_rip + 1675446)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 95 + 55) = result;
    v_r12 = 0;
    if (a1 != 0) goto loc_00C71787;
    if (((*(unsigned __int64 *)(v_rip + 3495088)) & (0x8000ULL)) == 0) goto loc_00C716E3;
    if ((*(unsigned int *)(v_rip + 3495703)) == 0) goto loc_00C716E3;
    result = (unsigned __int8)(((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 11520))) & (3));
    if (((unsigned __int8)(result)) != 3) {
        a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 11520)) | (3);
        a1 = 290;
        *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 11520) = a2;
        result = a2;
        a2 = (a2) >> (32);
    }
    result = KiDetectTsx(a1, a2, a3, a4);
    *(unsigned int *)(v_rip + 3495819) = (unsigned int)(result);
    result = KiRcuSystemInitialize(*(unsigned __int64 *)(gs_base + (0 + 32)), a2, a3, a4);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536)) == 0) goto loc_00C7171A;
    result = 1;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3495803)))) != 1) {
        result = 1;
        if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3495803)))) == 2) { result = 0; }
    }
    *(unsigned int *)(v_rip + 3495588) = (unsigned int)(result);
    if ((unsigned int)(result) != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 24);
    }
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 3488025))) - 1);
    if (((unsigned int)(result)) >= = 30) {
        *(unsigned int *)(v_rip + 3488012) = 1;
    }
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536)) != 0) {
    }
    result = KeInitializeCatRegisters((unsigned int)(*(unsigned int *)(v_rip + 3495803)), a2, a3, a4);
    result = KeInitializeTimerTable(*(unsigned __int64 *)(gs_base + (0 + 32)), a2, a3, a4);
    if (sign_flag) {
        a4 = 0;
        a2 = (int)((unsigned int)(result));
        a3 = 1;
        v_stack_mA8 = 0;
        a1 = a4 + 49;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    result = KiInitializeVelocity(a1, a2, a3, a4);
    result = KiInitializeAntiStarvationPolicies(a1, a2, a3, a4);
    goto loc_00C71C43;
loc_00C71787:
    if (a1 != 1) goto loc_00C71A44;
    result = KiInitDynamicTraceSupport(a1, a2, a3, a4);
    result = KeQueryActiveProcessorCountEx((unsigned int)(0xFFFFULL), a2, a3, a4);
    a2 = 0;
    *(unsigned __int64 *)(v_rip + 2825539) = 0;
    a2 = 0;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 3494647)) + 29999999) - 1);
    result = (unsigned int)((result) + ((unsigned int)((unsigned int)((unsigned int)(result)))));
    *(unsigned __int8 *)(v_rip + 3487794) = (unsigned __int8)(result);
    if ((*(unsigned int *)(v_rip + 3495622)) != 0) goto loc_00C71828;
    result = HviIsAnyHypervisorPresent((unsigned int)(*(unsigned int *)(v_rip + 3494647)), a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00C71828;
    if ((*(unsigned __int8 *)(v_rip + 3494577)) == 0) goto loc_00C717F7;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 3494602)))) & (32)) != 0) goto loc_00C717F7;
    goto loc_00C71823;
loc_00C717F7:
    *(unsigned int *)(v_rip + 3487788) = 0;
    *(unsigned int *)(v_rip + 3487789) = 0;
    *(unsigned int *)(v_rip + 3487794) = 0;
    *(unsigned int *)(v_rip + 3487783) = 0;
    *(unsigned int *)(v_rip + 3487752) = 0;
    *(unsigned int *)(v_rip + 3487749) = 0;
loc_00C71823:
    result = KeRelaxTimingConstraints(1, a2, a3, a4);
loc_00C71828:
    result = KiInitDpcThresholds(1, a2, a3, a4);
    if ((*(unsigned int *)(v_rip + 2699600)) == 0) goto loc_00C7185C;
    result = (unsigned int)(*(unsigned int *)(v_rip + 3487772));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3487772)))) < 1) {
        result = 1;
        *(unsigned int *)(v_rip + 3487760) = 1;
    }
    if (((unsigned int)(result)) >= = 100) {
        *(unsigned int *)(v_rip + 3487745) = 100;
    }
    result = KiApplyDpcVerificationScaleSettings(1, a2, a3, a4);
loc_00C7185C:
loc_00C71866:
    if (0 >= ((unsigned int)((unsigned int)((unsigned int)(result))))) goto loc_00C71896;
    result = KiInitializeProcessor(*(unsigned __int64 *)(v_rip + 3503066 + 0 * 8), a2, a3, a4);
    if ((*(unsigned int *)(v_rip + 3488028)) == 0) goto loc_00C71892;
    result = KiStartDpcThread(*(unsigned __int64 *)(v_rip + 3503066 + 0 * 8), a2, a3, a4);
    if (sign_flag) goto loc_00C71A3D;
loc_00C71892:
    v_rdi = (unsigned int)((0) + (1));
    goto loc_00C71866;
loc_00C71896:
    result = KiComputeNumaCosts(*(unsigned __int64 *)(v_rip + 3503066 + 0 * 8), a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00C71A3D;
    result = KiComputeDispatchInterruptCost(*(unsigned __int64 *)(v_rip + 3503066 + 0 * 8), a2, a3, a4);
    if (sign_flag) goto loc_00C71A3D;
    result = KiInitializeDpcRuntimeHistoryHashTables(*(unsigned __int64 *)(v_rip + 3503066 + 0 * 8), a2, a3, a4);
    if (sign_flag) goto loc_00C71A3D;
    if ((*(unsigned __int8 *)(v_rip + 5832573)) != 0) {
        *(unsigned __int8 *)(v_rip + 3499988) = 1;
        *(unsigned int *)(v_rip + 3499986) = 10;
    }
    result = SymCryptInitEnvWindowsKernelmodeWin8_1nLater((unsigned int)(0x67000CULL), a2, a3, a4);
    result = KiIntSteerInit(1, a2, a3, a4);
    result = KiInitSupervisorStateExtensionHost(1, a2, a3, a4);
    result = KiInitMachineDependent(1, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00C71A3D;
    a1 = ((unsigned int)(*(unsigned int *)(v_rip + 3494288))) * ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 3502912) + 68)));
    a1 = (0) >> (3);
    a2 = (a2) >> (7);
    *(unsigned int *)(v_rip + 3495033) = (unsigned int)(a2);
    a2 = (a2) >> (1);
    *(unsigned int *)(v_rip + 3487551) = (unsigned int)(a2);
    *(unsigned int *)(v_rip + 3494997) = (unsigned int)(a2);
    *(unsigned int *)(v_rip + 3494628) = (unsigned int)(a2 + a2 * 2);
    result = a2 + a2 * 2;
    if (((*(unsigned int *)(v_rip + 3494373)) & (0x40000ULL)) != 0) {
        result = 0xAAAAAAABULL;
        a2 = (unsigned int)((a2) >> (2));
        *(unsigned int *)(v_rip + 3487518) = (unsigned int)(a2);
        result = a2 + a2 * 1;
        *(unsigned int *)(v_rip + 3494601) = (unsigned int)(result);
    }
    result = (result) * ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 3502912) + 68)));
    *(unsigned int *)(v_rip + 3495498) = a1;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3487811)))) < 50) {
        a2 = 50;
        *(unsigned int *)(v_rip + 3487778) = (unsigned int)(a2);
    }
    if ((*(unsigned int *)(v_rip + 3487775)) < 2) {
        *(unsigned int *)(v_rip + 3487763) = 2;
    }
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 3502912) + 68))))) * ((unsigned int)(a2)));
    *(unsigned int *)(v_rip + 3495468) = (unsigned int)(result);
    result = ((unsigned int)(*(unsigned int *)(v_rip + 3488274))) * ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 3502912) + 68)));
    *(unsigned __int64 *)(v_rip + 3488261) = result;
    a1 = ((unsigned int)(*(unsigned int *)(v_rip + 3488276))) * ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 3502912) + 68)));
    *(unsigned __int64 *)(v_rip + 3488262) = a1;
    result = KdEncodeDataBlock(a1, a2, *(unsigned __int64 *)(v_rip + 3502912), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 3502912) + 68)));
    result = KiVerifyScopes(a1, a2, *(unsigned __int64 *)(v_rip + 3502912), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 3502912) + 68)));
    result = KiInitializeIdealProcessorRebalancer(a1, a2, *(unsigned __int64 *)(v_rip + 3502912), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 3502912) + 68)));
    *(unsigned int *)(v_rip + 2748046) = 0x41800ULL;
    *(unsigned __int64 *)(v_rip + 2748095) = v_rip - 6987672;
    *(unsigned int *)(v_rip + 2748061) = 275;
    *(unsigned __int64 *)(v_rip + 2748086) = 0;
    *(unsigned __int64 *)(v_rip + 2748103) = 0;
    *(unsigned __int64 *)(v_rip + 2748056) = 0;
    goto loc_00C71C43;
loc_00C71A3D:
    result = 0;
    goto loc_00C71C45;
loc_00C71A44:
    if (a1 != 2) goto loc_00C71BDC;
    result = TraceLoggingRegisterEx_EtwRegister_EtwSetInformation(v_rip + 1660492, v_rip - 5709982, v_rip + 1660492, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 3502912) + 68)));
    a3 = 0;
    a2 = 0;
    result = TraceLoggingRegisterEx_EtwRegister_EtwSetInformation(v_rip + 1660520, a2, a3, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 3502912) + 68)));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3494734))) == 0) goto loc_00C71AF1;
    if ((*(unsigned int *)(v_rip + 1660438)) <= 5) goto loc_00C71AF1;
    result = tlgKeywordOn(v_rip + 1660492, a2, (unsigned int)(*(unsigned int *)(v_rip + 3494734)), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 3502912) + 68)));
    if ((unsigned __int8)(result) != 0) {
        a1 = 4;
        *(unsigned int *)(v_rsp - 95 - 57) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3494734)));
        result = v_rsp - 95 - 57;
        *(unsigned __int64 *)(v_rsp - 95 + 15) = a1;
        *(unsigned __int64 *)(v_rsp - 95 + 7) = result;
        a2 = v_rip - 12676268;
        result = v_rsp - 95 - 49;
        *(unsigned __int64 *)(v_rsp - 95 - 49) = 0x1000000ULL;
        *(unsigned __int64 *)(v_rsp - 95 + 23) = result;
        a4 = 0;
        result = v_rsp - 95 - 25;
        *(unsigned __int64 *)(v_rsp - 95 + 31) = 8;
        v_stack_mA0 = result;
        a3 = 0;
        v_stack_mA8 = a1;
        a1 = v_rip + 1660492;
        result = tlgWriteTransfer_EtwWriteTransfer(a1, a2, a3, a4);
    }
    result = KiIntSteerInit(2, a2, a3, a4);
    result = Feature_PpmParkEx__private_IsEnabledNoReportingNoInline(2, a2, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_00C71C43;
loc_00C71B12:
    if (0 >= (*(unsigned int *)(v_rip + 3493736))) goto loc_00C71C43;
    *(unsigned __int64 *)(v_rsp - 95 - 41) = v_xmm0;
    result = KeGetTopologySiblingGroupAffinityForProcessor(*(unsigned __int64 *)(v_rip + 3502382 + 0 * 8), 5, v_rsp - 95 - 41, a4);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3502382 + 0 * 8) + 36464)) != (*(unsigned __int64 *)(v_rsp - 95 - 41))) goto loc_00C71B4D;
    v_rdi = (unsigned int)((0) + (1));
    goto loc_00C71B12;
loc_00C71B4D:
    if ((*(unsigned int *)(v_rip + 1660236)) <= 5) goto loc_00C71C43;
    result = tlgKeywordOn(v_rip + 1660492, 5, *(unsigned __int64 *)(v_rsp - 95 - 41), a4);
    if ((unsigned __int8)(result) == 0) goto loc_00C71C43;
    *(unsigned __int64 *)(v_rsp - 95 - 49) = *(unsigned __int64 *)(v_rsp - 95 - 41);
    *(unsigned __int64 *)(v_rsp - 95 + 7) = v_rsp - 95 - 49;
    *(unsigned __int64 *)(v_rsp - 95 + 15) = 8;
    *(unsigned __int64 *)(v_rsp - 95 + 23) = v_rsp - 95 - 57;
    a4 = 0;
    *(unsigned __int64 *)(v_rsp - 95 - 57) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3502382 + 0 * 8) + 36464);
    *(unsigned __int64 *)(v_rsp - 95 + 39) = v_rsp - 95 - 41;
    a3 = 0;
    *(unsigned __int64 *)(v_rsp - 95 + 31) = 8;
    v_stack_mA0 = v_rsp - 95 - 25;
    v_stack_mA8 = 5;
    *(unsigned __int64 *)(v_rsp - 95 - 41) = 0x1000000ULL;
    *(unsigned __int64 *)(v_rsp - 95 + 47) = 8;
    result = tlgWriteTransfer_EtwWriteTransfer(v_rip + 1660492, v_rip - 12676547, a3, a4);
    goto loc_00C71C43;
loc_00C71BDC:
    if (((unsigned int)(v_rip + 1660492)) != 3) goto loc_00C71BE8;
    result = KiInitializeReservedCpuSets(v_rip + 1660492, v_rip - 12676547, a3, a4);
    goto loc_00C71C43;
loc_00C71BE8:
    result = ExAcquireFastMutexUnsafe(v_rip + 2822033, v_rip - 12676547, a3, a4);
    result = MmFreeLoaderBlock(v_rip + 2822033, v_rip - 12676547, a3, a4);
    *(unsigned __int64 *)(v_rip + 3493657) = 0;
    result = ExReleaseFastMutexUnsafe(v_rip + 2822016, v_rip - 12676547, a3, a4);
    result = KiInitializeNormalPriorityAntiStarvationPolicies(v_rip + 2822016, v_rip - 12676547, a3, a4);
    if ((*(unsigned int *)(v_rip + 3494524)) != 0) goto loc_00C71C23;
    result = HviIsAnyHypervisorPresent(v_rip + 2822016, v_rip - 12676547, a3, a4);
    if ((unsigned __int8)(result) == 0) {
        *(unsigned __int8 *)(v_rip + 3493578) = 1;
    }
    result = KiEpfInitialize(v_rip + 2822016, v_rip - 12676547, a3, a4);
    result = KeFreeInitializationCode(v_rip + 2822016, v_rip - 12676547, a3, a4);
    *(unsigned int *)(v_rip + 3762889) = (unsigned int)(result);
loc_00C71C43:
loc_00C71C45:
    a1 = (*(unsigned __int64 *)(v_rsp - 95 + 55)) ^ (v_rsp);
    result = _security_check_cookie(a1, v_rip - 12676547, a3, a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KeInitSystem(int32_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_r12;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rsi;
    *(uint64_t *)(local_rsp + 0x18) = local_rdi;
    *(uint64_t *)(local_rsp + 0x20) = local_r12;
    local_rsp = (local_rsp) - (176);
    result = (*(uint64_t *)(v_rip + 0x1990B6)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x5F + 0x37) = result;
    local_r12 = 0;
    if (Arg1 != 0) goto loc_00C71787;
    if (((*(uint64_t *)(v_rip + 0x3554B0)) & (0x8000ULL)) == 0) goto loc_00C716E3;
    if ((*(uint32_t *)(v_rip + 0x355717)) == 0) goto loc_00C716E3;
    result = (uint8_t)(((uint8_t)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x2D00))) & (3));
    if (((uint8_t)(result)) != 3) {
        Arg2 = (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x2D00)) | (3);
        Arg1 = 290;
        *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x2D00) = Arg2;
        result = Arg2;
        Arg2 = (Arg2) >> (32);
    }
    result = KiDetectTsx(Arg1, Arg2, Arg3, Arg4);
    *(uint32_t *)(v_rip + 0x35578B) = (uint32_t)(result);
    result = KiRcuSystemInitialize(*(uint64_t *)(gs_base + (0 + 0x20)), Arg2, Arg3, Arg4);
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8)) == 0) goto loc_00C7171A;
    result = 1;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x35577B)))) != 1) {
        result = 1;
        if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x35577B)))) == 2) { result = 0; }
    }
    *(uint32_t *)(v_rip + 0x3556A4) = (uint32_t)(result);
    if ((uint32_t)(result) != 0) {
        result = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x18);
    }
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x353919))) - 1);
    if (((uint32_t)(result)) >= = 30) {
        *(uint32_t *)(v_rip + 0x35390C) = 1;
    }
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8)) != 0) {
    }
    result = KeInitializeCatRegisters((uint32_t)(*(uint32_t *)(v_rip + 0x35577B)), Arg2, Arg3, Arg4);
    result = KeInitializeTimerTable(*(uint64_t *)(gs_base + (0 + 0x20)), Arg2, Arg3, Arg4);
    if (sign_flag) {
        Arg4 = 0;
        Arg2 = (int32_t)((uint32_t)(result));
        Arg3 = 1;
        v_stack_mA8 = 0;
        Arg1 = Arg4 + 49;
        result = KeBugCheckEx(Arg1, Arg2, Arg3, Arg4);
    }
    result = KiInitializeVelocity(Arg1, Arg2, Arg3, Arg4);
    result = KiInitializeAntiStarvationPolicies(Arg1, Arg2, Arg3, Arg4);
    goto loc_00C71C43;
loc_00C71787:
    if (Arg1 != 1) goto loc_00C71A44;
    result = KiInitDynamicTraceSupport(Arg1, Arg2, Arg3, Arg4);
    result = KeQueryActiveProcessorCountEx((uint32_t)(0xFFFFULL), Arg2, Arg3, Arg4);
    Arg2 = 0;
    *(uint64_t *)(v_rip + 0x2B1D43) = 0;
    Arg2 = 0;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x3552F7)) + 29999999) - 1);
    result = (uint32_t)((result) + ((uint32_t)((uint32_t)((uint32_t)(result)))));
    *(uint8_t *)(v_rip + 0x353832) = (uint8_t)(result);
    if ((*(uint32_t *)(v_rip + 0x3556C6)) != 0) goto loc_00C71828;
    result = HviIsAnyHypervisorPresent((uint32_t)(*(uint32_t *)(v_rip + 0x3552F7)), Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00C71828;
    if ((*(uint8_t *)(v_rip + 0x3552B1)) == 0) goto loc_00C717F7;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x3552CA)))) & (32)) != 0) goto loc_00C717F7;
    goto loc_00C71823;
loc_00C717F7:
    *(uint32_t *)(v_rip + 0x35382C) = 0;
    *(uint32_t *)(v_rip + 0x35382D) = 0;
    *(uint32_t *)(v_rip + 0x353832) = 0;
    *(uint32_t *)(v_rip + 0x353827) = 0;
    *(uint32_t *)(v_rip + 0x353808) = 0;
    *(uint32_t *)(v_rip + 0x353805) = 0;
loc_00C71823:
    result = KeRelaxTimingConstraints(1, Arg2, Arg3, Arg4);
loc_00C71828:
    result = KiInitDpcThresholds(1, Arg2, Arg3, Arg4);
    if ((*(uint32_t *)(v_rip + 0x293150)) == 0) goto loc_00C7185C;
    result = (uint32_t)(*(uint32_t *)(v_rip + 0x35381C));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x35381C)))) < 1) {
        result = 1;
        *(uint32_t *)(v_rip + 0x353810) = 1;
    }
    if (((uint32_t)(result)) >= = 100) {
        *(uint32_t *)(v_rip + 0x353801) = 100;
    }
    result = KiApplyDpcVerificationScaleSettings(1, Arg2, Arg3, Arg4);
loc_00C7185C:
loc_00C71866:
    if (0 >= ((uint32_t)((uint32_t)((uint32_t)(result))))) goto loc_00C71896;
    result = KiInitializeProcessor(*(uint64_t *)(v_rip + 0x3573DA + 0x0 * 8), Arg2, Arg3, Arg4);
    if ((*(uint32_t *)(v_rip + 0x35391C)) == 0) goto loc_00C71892;
    result = KiStartDpcThread(*(uint64_t *)(v_rip + 0x3573DA + 0x0 * 8), Arg2, Arg3, Arg4);
    if (sign_flag) goto loc_00C71A3D;
loc_00C71892:
    local_rdi = (uint32_t)((0) + (1));
    goto loc_00C71866;
loc_00C71896:
    result = KiComputeNumaCosts(*(uint64_t *)(v_rip + 0x3573DA + 0x0 * 8), Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00C71A3D;
    result = KiComputeDispatchInterruptCost(*(uint64_t *)(v_rip + 0x3573DA + 0x0 * 8), Arg2, Arg3, Arg4);
    if (sign_flag) goto loc_00C71A3D;
    result = KiInitializeDpcRuntimeHistoryHashTables(*(uint64_t *)(v_rip + 0x3573DA + 0x0 * 8), Arg2, Arg3, Arg4);
    if (sign_flag) goto loc_00C71A3D;
    if ((*(uint8_t *)(v_rip + 0x58FF7D)) != 0) {
        *(uint8_t *)(v_rip + 0x3567D4) = 1;
        *(uint32_t *)(v_rip + 0x3567D2) = 10;
    }
    result = SymCryptInitEnvWindowsKernelmodeWin8_1nLater((uint32_t)(0x67000CULL), Arg2, Arg3, Arg4);
    result = KiIntSteerInit(1, Arg2, Arg3, Arg4);
    result = KiInitSupervisorStateExtensionHost(1, Arg2, Arg3, Arg4);
    result = KiInitMachineDependent(1, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00C71A3D;
    Arg1 = ((uint32_t)(*(uint32_t *)(v_rip + 0x355190))) * ((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x357340) + 0x44)));
    Arg1 = (0) >> (3);
    Arg2 = (Arg2) >> (7);
    *(uint32_t *)(v_rip + 0x355479) = (uint32_t)(Arg2);
    Arg2 = (Arg2) >> (1);
    *(uint32_t *)(v_rip + 0x35373F) = (uint32_t)(Arg2);
    *(uint32_t *)(v_rip + 0x355455) = (uint32_t)(Arg2);
    *(uint32_t *)(v_rip + 0x3552E4) = (uint32_t)(Arg2 + Arg2 * 2);
    result = Arg2 + Arg2 * 2;
    if (((*(uint32_t *)(v_rip + 0x3551E5)) & (0x40000ULL)) != 0) {
        result = 0xAAAAAAABULL;
        Arg2 = (uint32_t)((Arg2) >> (2));
        *(uint32_t *)(v_rip + 0x35371E) = (uint32_t)(Arg2);
        result = Arg2 + Arg2 * 1;
        *(uint32_t *)(v_rip + 0x3552C9) = (uint32_t)(result);
    }
    result = (result) * ((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x357340) + 0x44)));
    *(uint32_t *)(v_rip + 0x35564A) = Arg1;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x353843)))) < 50) {
        Arg2 = 50;
        *(uint32_t *)(v_rip + 0x353822) = (uint32_t)(Arg2);
    }
    if ((*(uint32_t *)(v_rip + 0x35381F)) < 2) {
        *(uint32_t *)(v_rip + 0x353813) = 2;
    }
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x357340) + 0x44))))) * ((uint32_t)(Arg2)));
    *(uint32_t *)(v_rip + 0x35562C) = (uint32_t)(result);
    result = ((uint32_t)(*(uint32_t *)(v_rip + 0x353A12))) * ((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x357340) + 0x44)));
    *(uint64_t *)(v_rip + 0x353A05) = result;
    Arg1 = ((uint32_t)(*(uint32_t *)(v_rip + 0x353A14))) * ((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x357340) + 0x44)));
    *(uint64_t *)(v_rip + 0x353A06) = Arg1;
    result = KdEncodeDataBlock(Arg1, Arg2, *(uint64_t *)(v_rip + 0x357340), (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x357340) + 0x44)));
    result = KiVerifyScopes(Arg1, Arg2, *(uint64_t *)(v_rip + 0x357340), (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x357340) + 0x44)));
    result = KiInitializeIdealProcessorRebalancer(Arg1, Arg2, *(uint64_t *)(v_rip + 0x357340), (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x357340) + 0x44)));
    *(uint32_t *)(v_rip + 0x29EE8E) = 0x41800ULL;
    *(uint64_t *)(v_rip + 0x29EEBF) = v_rip - 6987672;
    *(uint32_t *)(v_rip + 0x29EE9D) = 275;
    *(uint64_t *)(v_rip + 0x29EEB6) = 0;
    *(uint64_t *)(v_rip + 0x29EEC7) = 0;
    *(uint64_t *)(v_rip + 0x29EE98) = 0;
    goto loc_00C71C43;
loc_00C71A3D:
    result = 0;
    goto loc_00C71C45;
loc_00C71A44:
    if (Arg1 != 2) goto loc_00C71BDC;
    result = TraceLoggingRegisterEx_EtwRegister_EtwSetInformation(v_rip + 1660492, v_rip - 5709982, v_rip + 1660492, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x357340) + 0x44)));
    Arg3 = 0;
    Arg2 = 0;
    result = TraceLoggingRegisterEx_EtwRegister_EtwSetInformation(v_rip + 1660520, Arg2, Arg3, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x357340) + 0x44)));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x35534E))) == 0) goto loc_00C71AF1;
    if ((*(uint32_t *)(v_rip + 0x195616)) <= 5) goto loc_00C71AF1;
    result = tlgKeywordOn(v_rip + 1660492, Arg2, (uint32_t)(*(uint32_t *)(v_rip + 0x35534E)), (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x357340) + 0x44)));
    if ((uint8_t)(result) != 0) {
        Arg1 = 4;
        *(uint32_t *)(local_rsp - 0x5F - 0x39) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x35534E)));
        result = local_rsp - 95 - 57;
        *(uint64_t *)(local_rsp - 0x5F + 0xF) = Arg1;
        *(uint64_t *)(local_rsp - 0x5F + 0x7) = result;
        Arg2 = v_rip - 12676268;
        result = local_rsp - 95 - 49;
        *(uint64_t *)(local_rsp - 0x5F - 0x31) = 0x1000000ULL;
        *(uint64_t *)(local_rsp - 0x5F + 0x17) = result;
        Arg4 = 0;
        result = local_rsp - 95 - 25;
        *(uint64_t *)(local_rsp - 0x5F + 0x1F) = 8;
        v_stack_mA0 = result;
        Arg3 = 0;
        v_stack_mA8 = Arg1;
        Arg1 = v_rip + 1660492;
        result = tlgWriteTransfer_EtwWriteTransfer(Arg1, Arg2, Arg3, Arg4);
    }
    result = KiIntSteerInit(2, Arg2, Arg3, Arg4);
    result = Feature_PpmParkEx__private_IsEnabledNoReportingNoInline(2, Arg2, Arg3, Arg4);
    if ((uint32_t)(result) == 0) goto loc_00C71C43;
loc_00C71B12:
    if (0 >= (*(uint32_t *)(v_rip + 0x354F68))) goto loc_00C71C43;
    *(uint64_t *)(local_rsp - 0x5F - 0x29) = v_xmm0;
    result = KeGetTopologySiblingGroupAffinityForProcessor(*(uint64_t *)(v_rip + 0x35712E + 0x0 * 8), 5, local_rsp - 95 - 41, Arg4);
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0x35712E + 0x0 * 8) + 0x8E70)) != (*(uint64_t *)(local_rsp - 0x5F - 0x29))) goto loc_00C71B4D;
    local_rdi = (uint32_t)((0) + (1));
    goto loc_00C71B12;
loc_00C71B4D:
    if ((*(uint32_t *)(v_rip + 0x19554C)) <= 5) goto loc_00C71C43;
    result = tlgKeywordOn(v_rip + 1660492, 5, *(uint64_t *)(local_rsp - 0x5F - 0x29), Arg4);
    if ((uint8_t)(result) == 0) goto loc_00C71C43;
    *(uint64_t *)(local_rsp - 0x5F - 0x31) = *(uint64_t *)(local_rsp - 0x5F - 0x29);
    *(uint64_t *)(local_rsp - 0x5F + 0x7) = local_rsp - 95 - 49;
    *(uint64_t *)(local_rsp - 0x5F + 0xF) = 8;
    *(uint64_t *)(local_rsp - 0x5F + 0x17) = local_rsp - 95 - 57;
    Arg4 = 0;
    *(uint64_t *)(local_rsp - 0x5F - 0x39) = *(uint64_t *)(*(uint64_t *)(v_rip + 0x35712E + 0x0 * 8) + 0x8E70);
    *(uint64_t *)(local_rsp - 0x5F + 0x27) = local_rsp - 95 - 41;
    Arg3 = 0;
    *(uint64_t *)(local_rsp - 0x5F + 0x1F) = 8;
    v_stack_mA0 = local_rsp - 95 - 25;
    v_stack_mA8 = 5;
    *(uint64_t *)(local_rsp - 0x5F - 0x29) = 0x1000000ULL;
    *(uint64_t *)(local_rsp - 0x5F + 0x2F) = 8;
    result = tlgWriteTransfer_EtwWriteTransfer(v_rip + 1660492, v_rip - 12676547, Arg3, Arg4);
    goto loc_00C71C43;
loc_00C71BDC:
    if (((uint32_t)(v_rip + 1660492)) != 3) goto loc_00C71BE8;
    result = KiInitializeReservedCpuSets(v_rip + 1660492, v_rip - 12676547, Arg3, Arg4);
    goto loc_00C71C43;
loc_00C71BE8:
    result = ExAcquireFastMutexUnsafe(v_rip + 2822033, v_rip - 12676547, Arg3, Arg4);
    result = MmFreeLoaderBlock(v_rip + 2822033, v_rip - 12676547, Arg3, Arg4);
    *(uint64_t *)(v_rip + 0x354F19) = 0;
    result = ExReleaseFastMutexUnsafe(v_rip + 2822016, v_rip - 12676547, Arg3, Arg4);
    result = KiInitializeNormalPriorityAntiStarvationPolicies(v_rip + 2822016, v_rip - 12676547, Arg3, Arg4);
    if ((*(uint32_t *)(v_rip + 0x35527C)) != 0) goto loc_00C71C23;
    result = HviIsAnyHypervisorPresent(v_rip + 2822016, v_rip - 12676547, Arg3, Arg4);
    if ((uint8_t)(result) == 0) {
        *(uint8_t *)(v_rip + 0x354ECA) = 1;
    }
    result = KiEpfInitialize(v_rip + 2822016, v_rip - 12676547, Arg3, Arg4);
    result = KeFreeInitializationCode(v_rip + 2822016, v_rip - 12676547, Arg3, Arg4);
    *(uint32_t *)(v_rip + 0x396AC9) = (uint32_t)(result);
loc_00C71C43:
loc_00C71C45:
    Arg1 = (*(uint64_t *)(local_rsp - 0x5F + 0x37)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_rip - 12676547, Arg3, Arg4);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C71660&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
