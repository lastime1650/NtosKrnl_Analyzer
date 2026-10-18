# KeBugCheck2

- RVA: `0x005B27D0`–`0x005B37C2` (길이 `4,082` bytes)
- VA: `0x00000001405B27D0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C9C68`
- 디코드: `941`개 명령, `4,082/4,082` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **85**; 고유 호출 대상: **51**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **74**

### Outgoing calls
- `0x005B281B` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x005B28D2` → [IoNotifyDumpEx](../59/IoNotifyDumpEx_function_00592B78.md) (function, `0x00592B78`)
- `0x005B28E7` → [HvlNotifyRootCrashdump](../58/HvlNotifyRootCrashdump_function_00588EF8.md) (function, `0x00588EF8`)
- `0x005B2915` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x005B2980` → [KeQueryCurrentStackInformation](../2F/KeQueryCurrentStackInformation_function_002F7C80.md) (function, `0x002F7C80`)
- `0x005B29C2` → [IoNotifyDumpEx](../59/IoNotifyDumpEx_function_00592B78.md) (function, `0x00592B78`)
- `0x005B2A1A` → [MmIsAddressValidEx](../27/MmIsAddressValidEx_function_0027FDD0.md) (function, `0x0027FDD0`)
- `0x005B2A30` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x005B2A50` → [IoNotifyDumpEx](../59/IoNotifyDumpEx_function_00592B78.md) (function, `0x00592B78`)
- `0x005B2AC7` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x005B2AFD` → [DbgPrintEx](../35/DbgPrintEx_function_00359290.md) (function, `0x00359290`)
- `0x005B2B45` → [KeSaveSupervisorState](KeSaveSupervisorState_function_005B9CB4.md) (function, `0x005B9CB4`)
- `0x005B2B85` → [DbgPrintEx](../35/DbgPrintEx_function_00359290.md) (function, `0x00359290`)
- `0x005B2B9B` → [DbgPrintEx](../35/DbgPrintEx_function_00359290.md) (function, `0x00359290`)
- `0x005B2C47` → [VfNotifyVerifierOfEvent](../../pagevrfy/B9/VfNotifyVerifierOfEvent_function_00B92E90.md) (function, `0x00B92E90`)
- `0x005B2C57` → [KiScanBugCheckCallbackList](KiScanBugCheckCallbackList_function_005B5464.md) (function, `0x005B5464`)
- `0x005B2C65` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x005B2C6F` → [HalReturnToFirmware](../54/HalReturnToFirmware_function_00546550.md) (function, `0x00546550`)
- `0x005B2D06` → [KiBugCheckUnicodeToAnsi](KiBugCheckUnicodeToAnsi_function_005B4104.md) (function, `0x005B4104`)
- `0x005B2D9F` → [KiPcToFileHeader](KiPcToFileHeader_function_005B5268.md) (function, `0x005B5268`)
- `0x005B2DB5` → [MmLocateUnloadedDriver](../67/MmLocateUnloadedDriver_function_0067170C.md) (function, `0x0067170C`)
- `0x005B2E6B` → [KiPcToFileHeader](KiPcToFileHeader_function_005B5268.md) (function, `0x005B5268`)
- `0x005B2EA6` → [KiPcToFileHeader](KiPcToFileHeader_function_005B5268.md) (function, `0x005B5268`)
- `0x005B2EDC` → [MmLocateUnloadedDriver](../67/MmLocateUnloadedDriver_function_0067170C.md) (function, `0x0067170C`)
- `0x005B30A4` → [IoAddTriageDumpDataBlock](../42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x005B30D9` → [KiDumpParameterImages](KiDumpParameterImages_function_005B4CE0.md) (function, `0x005B4CE0`)
- `0x005B30E7` → [WheapSelLogSetNtSchedulerAvailabilityNoLock](../65/WheapSelLogSetNtSchedulerAvailabilityNoLock_function_0065DBB4.md) (function, `0x0065DBB4`)
- `0x005B30F3` → [IpmiHwContextInitialized](../6A/IpmiHwContextInitialized_function_006A64DC.md) (function, `0x006A64DC`)
- `0x005B30FC` → [IpmiLibAddSelBugcheckRecord](../6A/IpmiLibAddSelBugcheckRecord_function_006A6A40.md) (function, `0x006A6A40`)
- `0x005B3121` → [KiCollectTriageDumpDataBlocks](KiCollectTriageDumpDataBlocks_function_005B43F8.md) (function, `0x005B43F8`)
- `0x005B316F` → [KiAttemptBugcheckRecovery](../5C/KiAttemptBugcheckRecovery_function_005C6D24.md) (function, `0x005C6D24`)
- `0x005B3182` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x005B3196` → [IoSaveBugCheckProgress](../59/IoSaveBugCheckProgress_function_00592E10.md) (function, `0x00592E10`)
- `0x005B31A2` → [KeIsEmptyAffinityEx](../2D/KeIsEmptyAffinityEx_function_002D1580.md) (function, `0x002D1580`)
- `0x005B31B7` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x005B31C7` → [KiFilterBugCheckInfo](../50/KiFilterBugCheckInfo_function_00509EBC.md) (function, `0x00509EBC`)
- `0x005B320F` → [HvlLogGuestCrashInformation](../58/HvlLogGuestCrashInformation_function_00583C84.md) (function, `0x00583C84`)
- `0x005B3230` → [KiBugCheckShouldEnterPostBugCheckDebugger](KiBugCheckShouldEnterPostBugCheckDebugger_function_005B40A0.md) (function, `0x005B40A0`)
- `0x005B328D` → [DbgPrintEx](../35/DbgPrintEx_function_00359290.md) (function, `0x00359290`)
- `0x005B32AE` → [DbgPrintEx](../35/DbgPrintEx_function_00359290.md) (function, `0x00359290`)
- `0x005B32CB` → [DbgPrintEx](../35/DbgPrintEx_function_00359290.md) (function, `0x00359290`)
- `0x005B32DD` → [DbgPrintEx](../35/DbgPrintEx_function_00359290.md) (function, `0x00359290`)
- `0x005B32F9` → [KiBugCheckDebugBreak](KiBugCheckDebugBreak_function_005B3DC0.md) (function, `0x005B3DC0`)
- `0x005B3325` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x005B333B` → [KiHandleMultipleBugchecksDuringRecovery](../5C/KiHandleMultipleBugchecksDuringRecovery_function_005C7860.md) (function, `0x005C7860`)
- `0x005B336A` → [KiYieldWaitForDebugger](KiYieldWaitForDebugger_function_005B56DC.md) (function, `0x005B56DC`)
- `0x005B33B0` → [DbgPrintEx](../35/DbgPrintEx_function_00359290.md) (function, `0x00359290`)
- `0x005B33BA` → [IoSetBugCheckProgressFlag](../59/IoSetBugCheckProgressFlag_function_005931C0.md) (function, `0x005931C0`)
- `0x005B3452` → [IoRetryAsMiniDump](../59/IoRetryAsMiniDump_function_00592CA0.md) (function, `0x00592CA0`)
- `0x005B3478` → [DbgPrintEx](../35/DbgPrintEx_function_00359290.md) (function, `0x00359290`)
- `0x005B3481` → [KiBugCheckDebugBreak](KiBugCheckDebugBreak_function_005B3DC0.md) (function, `0x005B3DC0`)
- `0x005B349F` → [DbgPrintEx](../35/DbgPrintEx_function_00359290.md) (function, `0x00359290`)
- `0x005B34AB` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x005B34CF` → [KiSetDebuggerOwner](../4F/KiSetDebuggerOwner_function_004FCE94.md) (function, `0x004FCE94`)
- `0x005B34E8` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x005B34FC` → [KiCopyAffinityEx](../2C/KiCopyAffinityEx_function_002CE860.md) (function, `0x002CE860`)
- `0x005B3509` → [KeRemoveProcessorAffinityEx](../30/KeRemoveProcessorAffinityEx_function_00304E10.md) (function, `0x00304E10`)
- `0x005B3514` → [KiSendFreeze](../5C/KiSendFreeze_function_005C3364.md) (function, `0x005C3364`)
- `0x005B351E` → [KeStallExecutionProcessor](../44/KeStallExecutionProcessor_function_0044F620.md) (function, `0x0044F620`)
- `0x005B3530` → [IoSaveInitialBugCheckProgress](../59/IoSaveInitialBugCheckProgress_function_00593020.md) (function, `0x00593020`)
- `0x005B3538` → [IoSaveBugCheckProgress](../59/IoSaveBugCheckProgress_function_00592E10.md) (function, `0x00592E10`)
- `0x005B353F` → [KiBugCheckProgressCpusFrozen](KiBugCheckProgressCpusFrozen_function_005B3FE4.md) (function, `0x005B3FE4`)
- `0x005B355B` → [PpmHvSetVirtualProcessorQos](../5D/PpmHvSetVirtualProcessorQos_function_005DD0A0.md) (function, `0x005DD0A0`)
- `0x005B3596` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x005B35C7` → [KiDisplayBlueScreen](KiDisplayBlueScreen_function_005B494C.md) (function, `0x005B494C`)
- `0x005B35D6` → [HvlPrepareForRootCrashdump](../58/HvlPrepareForRootCrashdump_function_00588F84.md) (function, `0x00588F84`)
- `0x005B35E5` → [IoSaveBugCheckProgress](../59/IoSaveBugCheckProgress_function_00592E10.md) (function, `0x00592E10`)
- `0x005B35F2` → [KiInvokeBugCheckEntryCallbacks](KiInvokeBugCheckEntryCallbacks_function_005B51A0.md) (function, `0x005B51A0`)
- `0x005B35FF` → [KiInvokeBugCheckEntryCallbacks](KiInvokeBugCheckEntryCallbacks_function_005B51A0.md) (function, `0x005B51A0`)
- `0x005B360E` → [KiInvokeBugCheckEntryCallbacks](KiInvokeBugCheckEntryCallbacks_function_005B51A0.md) (function, `0x005B51A0`)
- `0x005B3616` → [IoSaveBugCheckProgress](../59/IoSaveBugCheckProgress_function_00592E10.md) (function, `0x00592E10`)
- `0x005B361B` → [KiInvokeBugCheckAddTriageDumpDataCallbacks](KiInvokeBugCheckAddTriageDumpDataCallbacks_function_005B4F88.md) (function, `0x005B4F88`)
- `0x005B363B` → [KdEnableDebuggerWithLock](KdEnableDebuggerWithLock_function_005B0A7C.md) (function, `0x005B0A7C`)
- `0x005B36C8` → [KdDecodeDataBlock](KdDecodeDataBlock_function_005B05A8.md) (function, `0x005B05A8`)
- `0x005B3711` → [KiBugCheckWriteCrashDump](KiBugCheckWriteCrashDump_function_005B4148.md) (function, `0x005B4148`)
- `0x005B3718` → [HvlResumeFromRootCrashdump](../58/HvlResumeFromRootCrashdump_function_005893E0.md) (function, `0x005893E0`)
- `0x005B3722` → [IoSaveBugCheckProgress](../59/IoSaveBugCheckProgress_function_00592E10.md) (function, `0x00592E10`)
- `0x005B372C` → [KiScanBugCheckCallbackList](KiScanBugCheckCallbackList_function_005B5464.md) (function, `0x005B5464`)
- `0x005B3738` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x005B3742` → [IoSaveBugCheckProgress](../59/IoSaveBugCheckProgress_function_00592E10.md) (function, `0x00592E10`)
- `0x005B3757` → [KiSendThawExecution](../4E/KiSendThawExecution_function_004E2800.md) (function, `0x004E2800`)
- `0x005B375C` → [KiBugcheckUnloadDebugSymbols](KiBugcheckUnloadDebugSymbols_function_005B41B4.md) (function, `0x005B41B4`)
- `0x005B376A` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x005B379E` → [HalReturnToFirmware](../54/HalReturnToFirmware_function_00546550.md) (function, `0x00546550`)
- `0x005B37A8` → [KiBugCheckDebugBreak](KiBugCheckDebugBreak_function_005B3DC0.md) (function, `0x005B3DC0`)

### Direct callers
- [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) at `0x004FD762`
- [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) at `0x004FD779`

### Static image references
- `0x005B2838` → RVA `0x00E660B8` (`.data`; read)
- `0x005B2843` → RVA `0x005B3E90` (`KiBugCheckProgress`; read)
- `0x005B2864` → RVA `0x00E667F4` (`.data`; read/write)
- `0x005B28A6` → RVA `0x00F47580` (`.data`; write)
- `0x005B28AD` → RVA `0x00F47588` (`.data`; write)
- `0x005B28B4` → RVA `0x00F47590` (`.data`; write)
- `0x005B28BB` → RVA `0x00F47598` (`.data`; write)
- `0x005B28C2` → RVA `0x00F475A0` (`.data`; write)
- `0x005B28D7` → RVA `0x00FC6A90` (`ALMOSTRO`; read)
- `0x005B2909` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x005B2937` → RVA `0x00F4754C` (`.data`; read)
- `0x005B2A01` → RVA `0x00F23540` (`.data`; read)
- `0x005B2A5C` → RVA `0x01201841` (`CFGRO`; read)
- `0x005B2AB6` → RVA `0x00FC80C0` (`ALMOSTRO`; read)
- `0x005B2AF3` → RVA `0x006CB6B0` (` ?? ::FNODOBFM::`string'`; read)
- `0x005B2B07` → RVA `0x00F1090C` (`.data`; read)
- `0x005B2B11` → RVA `0x00F47548` (`.data`; write)
- `0x005B2B18` → RVA `0x00FC6BF0` (`ALMOSTRO`; read)
- `0x005B2B2D` → RVA `0x00FC6C60` (`ALMOSTRO`; read)
- `0x005B2B4A` → RVA `0x00F0BD90` (`.data`; read)
- `0x005B2B5E` → RVA `0x00F0C2E0` (`.data`; read)
- `0x005B2B67` → RVA `0x00F0BD20` (`.data`; write)
- `0x005B2B7B` → RVA `0x006CBF70` (` ?? ::FNODOBFM::`string'`; read)
- `0x005B2B8F` → RVA `0x006CC030` (` ?? ::FNODOBFM::`string'`; read)
- `0x005B2C3C` → RVA `0x00F04984` (`.data`; read)
- `0x005B2C5C` → RVA `0x00E00B08` (`.data`; read)
- `0x005B2CEF` → RVA `0x00E667E0` (`.data`; read)
- `0x005B2DC7` → RVA `0x00E667F0` (`.data`; write)
- `0x005B2DCE` → RVA `0x00E667E0` (`.data`; write)
- `0x005B2DEA` → RVA `0x00F47588` (`.data`; read)
- `0x005B2DF9` → RVA `0x00F475A8` (`.data`; read)
- `0x005B2E36` → RVA `0x00EF5498` (`.data`; read)
- `0x005B2E43` → RVA `0x00EF54A0` (`.data`; read)
- `0x005B30DE` → RVA `0x00EF9F00` (`.data`; read)
- `0x005B30EC` → RVA `0x00EFA080` (`.data`; read)
- `0x005B3101` → RVA `0x00F47580` (`.data`; read)
- `0x005B3113` → RVA `0x00E65ED4` (`.data`; write)
- `0x005B3131` → RVA `0x00E0A9B4` (`.data`; read)
- `0x005B3142` → RVA `0x00F23508` (`.data`; write)
- `0x005B3149` → RVA `0x00F23500` (`.data`; write)
- `0x005B3154` → RVA `0x00F23510` (`.data`; write)
- `0x005B315B` → RVA `0x00F23518` (`.data`; write)
- `0x005B3162` → RVA `0x00F23520` (`.data`; write)
- `0x005B3168` → RVA `0x00F23521` (`.data`; write)
- `0x005B3174` → RVA `0x00E00B28` (`.data`; read)
- `0x005B3187` → RVA `0x00FC6AB8` (`ALMOSTRO`; read/write)
- `0x005B319B` → RVA `0x00E0AA60` (`.data`; read)
- `0x005B31AD` → RVA `0x00E008F8` (`.data`; read)
- `0x005B31CC` → RVA `0x00E66050` (`.data`; read)
- `0x005B31E1` → RVA `0x00F47598` (`.data`; read)
- `0x005B31E8` → RVA `0x00F47590` (`.data`; read)
- `0x005B3203` → RVA `0x00F475A0` (`.data`; read)
- `0x005B3214` → RVA `0x00E0AA1C` (`.data`; read)
- `0x005B3224` → RVA `0x00E01088` (`.data`; write)
- `0x005B3251` → RVA `0x006CB730` (` ?? ::FNODOBFM::`string'`; read)
- `0x005B32A4` → RVA `0x006CB710` (` ?? ::FNODOBFM::`string'`; read)
- `0x005B32E2` → RVA `0x00F475F8` (`.data`; read)
- `0x005B32EB` → RVA `0x00F475DC` (`.data`; read)
- `0x005B3370` → RVA `0x00E667E8` (`.data`; read)
- `0x005B3392` → RVA `0x006CB5D0` (` ?? ::FNODOBFM::`string'`; read)
- `0x005B33BF` → RVA `0x00F4754C` (`.data`; read/write)
- `0x005B346B` → RVA `0x006CB590` (` ?? ::FNODOBFM::`string'`; read)
- `0x005B3495` → RVA `0x006CB690` (` ?? ::FNODOBFM::`string'`; read)
- `0x005B34A4` → RVA `0x00E00838` (`.data`; read)
- `0x005B34B8` → RVA `0x00FC6A80` (`ALMOSTRO`; read)
- `0x005B34F1` → RVA `0x00FC7120` (`ALMOSTRO`; read)
- `0x005B354D` → RVA `0x00FC6AED` (`ALMOSTRO`; read)
- `0x005B3562` → RVA `0x00FC6ADC` (`ALMOSTRO`; read)
- `0x005B36EE` → RVA `0x00F23500` (`.data`; read)
- `0x005B3731` → RVA `0x00E00B18` (`.data`; read)
- `0x005B3750` → RVA `0x00E66890` (`.data`; write)
- `0x005B376F` → RVA `0x00F0BD20` (`.data`; read)
- `0x005B3778` → RVA `0x00F0BD21` (`.data`; read)
- `0x005B3781` → RVA `0x00F0BD22` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x005B2C47` → [VfNotifyVerifierOfEvent](../../pagevrfy/B9/VfNotifyVerifierOfEvent_function_00B92E90.md) (`.text` → `PAGEVRFY`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005B27D0  40 55                           push rbp
005B27D2  53                              push rbx
005B27D3  56                              push rsi
005B27D4  57                              push rdi
005B27D5  41 54                           push r12
005B27D7  41 55                           push r13
005B27D9  41 56                           push r14
005B27DB  41 57                           push r15
005B27DD  48 8D AC 24 B8 F9 FF FF         lea rbp, [rsp - 0x648]
005B27E5  48 81 EC 48 07 00 00            sub rsp, 0x748
005B27EC  48 8B 85 B8 06 00 00            mov rax, qword ptr [rbp + 0x6b8]
005B27F3  49 8B F8                        mov rdi, r8
005B27F6  4C 8B AD B0 06 00 00            mov r13, qword ptr [rbp + 0x6b0]
005B27FD  4C 8B FA                        mov r15, rdx
005B2800  4C 89 45 B8                     mov qword ptr [rbp - 0x48], r8
005B2804  33 D2                           xor edx, edx
005B2806  89 4D 80                        mov dword ptr [rbp - 0x80], ecx
005B2809  41 B8 08 01 00 00               mov r8d, 0x108
005B280F  48 8D 4D E0                     lea rcx, [rbp - 0x20]
005B2813  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
005B2818  4D 8B E1                        mov r12, r9
005B281B  E8 20 44 11 00                  call 0x1406c6c40
005B2820  45 33 F6                        xor r14d, r14d
005B2823  C6 44 24 59 01                  mov byte ptr [rsp + 0x59], 1
005B2828  44 88 B5 C0 05 00 00            mov byte ptr [rbp + 0x5c0], r14b
005B282F  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
005B2838  44 39 35 79 38 8B 00            cmp dword ptr [rip + 0x8b3879], r14d
005B283F  48 89 45 A0                     mov qword ptr [rbp - 0x60], rax
005B2843  48 8D 05 46 16 00 00            lea rax, [rip + 0x1646]
005B284A  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
005B284E  0F 95 44 24 68                  setne byte ptr [rsp + 0x68]
005B2853  41 8D 46 01                     lea eax, [r14 + 1]
005B2857  4C 89 75 98                     mov qword ptr [rbp - 0x68], r14
005B285B  44 88 74 24 5A                  mov byte ptr [rsp + 0x5a], r14b
005B2860  4C 89 75 88                     mov qword ptr [rbp - 0x78], r14
005B2864  87 05 8A 3F 8B 00               xchg dword ptr [rip + 0x8b3f8a], eax
005B286A  44 88 74 24 54                  mov byte ptr [rsp + 0x54], r14b
005B286F  44 88 74 24 78                  mov byte ptr [rsp + 0x78], r14b
005B2874  44 88 74 24 7A                  mov byte ptr [rsp + 0x7a], r14b
005B2879  4C 89 75 D0                     mov qword ptr [rbp - 0x30], r14
005B287D  4C 89 74 24 70                  mov qword ptr [rsp + 0x70], r14
005B2882  C6 44 24 50 01                  mov byte ptr [rsp + 0x50], 1
005B2887  44 88 74 24 79                  mov byte ptr [rsp + 0x79], r14b
005B288C  44 89 75 90                     mov dword ptr [rbp - 0x70], r14d
005B2890  85 C0                           test eax, eax
005B2892  75 35                           jne 0x1405b28c9
005B2894  8B 45 80                        mov eax, dword ptr [rbp - 0x80]
005B2897  3D D1 02 00 C0                  cmp eax, 0xc00002d1
005B289C  75 08                           jne 0x1405b28a6
005B289E  B8 C3 00 00 00                  mov eax, 0xc3
005B28A3  89 45 80                        mov dword ptr [rbp - 0x80], eax
005B28A6  48 89 05 D3 4C 99 00            mov qword ptr [rip + 0x994cd3], rax
005B28AD  4C 89 3D D4 4C 99 00            mov qword ptr [rip + 0x994cd4], r15
005B28B4  48 89 3D D5 4C 99 00            mov qword ptr [rip + 0x994cd5], rdi
005B28BB  4C 89 25 D6 4C 99 00            mov qword ptr [rip + 0x994cd6], r12
005B28C2  4C 89 2D D7 4C 99 00            mov qword ptr [rip + 0x994cd7], r13
005B28C9  45 33 C0                        xor r8d, r8d
005B28CC  41 8D 58 04                     lea ebx, [r8 + 4]
005B28D0  8B CB                           mov ecx, ebx
005B28D2  E8 A1 02 FE FF                  call 0x140592b78
005B28D7  8B 05 B3 41 A1 00               mov eax, dword ptr [rip + 0xa141b3]
005B28DD  8D 73 FE                        lea esi, [rbx - 2]
005B28E0  40 84 C6                        test sil, al
005B28E3  74 07                           je 0x1405b28ec
005B28E5  8B CB                           mov ecx, ebx
005B28E7  E8 0C 66 FD FF                  call 0x140588ef8
005B28EC  4C 89 75 C0                     mov qword ptr [rbp - 0x40], r14
005B28F0  4C 89 75 C8                     mov qword ptr [rbp - 0x38], r14
005B28F4  44 89 75 A8                     mov dword ptr [rbp - 0x58], r14d
005B28F8  44 0F 20 C0                     mov rax, cr8
005B28FC  40 3A C6                        cmp al, sil
005B28FF  73 19                           jae 0x1405b291a
005B2901  44 0F 20 C1                     mov rcx, cr8
005B2905  44 0F 22 C6                     mov cr8, rsi
005B2909  44 39 35 10 44 A1 00            cmp dword ptr [rip + 0xa14410], r14d
005B2910  74 08                           je 0x1405b291a
005B2912  40 8A D6                        mov dl, sil
005B2915  E8 E2 2D F4 FF                  call 0x1404f56fc
005B291A  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
005B2923  BB 00 01 00 00                  mov ebx, 0x100
005B2928  4C 39 70 28                     cmp qword ptr [rax + 0x28], r14
005B292C  75 46                           jne 0x1405b2974
005B292E  65 48 8B 14 25 20 00 00 00      mov rdx, qword ptr gs:[0x20]
005B2937  8B 05 0F 4C 99 00               mov eax, dword ptr [rip + 0x994c0f]
005B293D  8B 52 24                        mov edx, dword ptr [rdx + 0x24]
005B2940  C1 E2 04                        shl edx, 4
005B2943  83 CA 03                        or edx, 3
005B2946  8B C8                           mov ecx, eax
005B2948  83 E1 03                        and ecx, 3
005B294B  80 F9 03                        cmp cl, 3
005B294E  74 15                           je 0x1405b2965
005B2950  8B C8                           mov ecx, eax
005B2952  F0 0F B1 15 F2 4B 99 00         lock cmpxchg dword ptr [rip + 0x994bf2], edx
005B295A  3B C1                           cmp eax, ecx
005B295C  75 E8                           jne 0x1405b2946
005B295E  C6 44 24 58 01                  mov byte ptr [rsp + 0x58], 1
005B2963  EB 05                           jmp 0x1405b296a
005B2965  44 88 74 24 58                  mov byte ptr [rsp + 0x58], r14b
005B296A  40 8A 74 24 58                  mov sil, byte ptr [rsp + 0x58]
005B296F  E9 76 01 00 00                  jmp 0x1405b2aea
005B2974  4C 8D 45 C0                     lea r8, [rbp - 0x40]
005B2978  48 8D 55 C8                     lea rdx, [rbp - 0x38]
005B297C  48 8D 4D A8                     lea rcx, [rbp - 0x58]
005B2980  E8 FB 52 D4 FF                  call 0x1402f7c80
005B2985  65 48 8B 14 25 20 00 00 00      mov rdx, qword ptr gs:[0x20]
005B298E  8A D8                           mov bl, al
005B2990  8B 05 B6 4B 99 00               mov eax, dword ptr [rip + 0x994bb6]
005B2996  8B 52 24                        mov edx, dword ptr [rdx + 0x24]
005B2999  C1 E2 04                        shl edx, 4
005B299C  83 CA 03                        or edx, 3
005B299F  8B C8                           mov ecx, eax
005B29A1  83 E1 03                        and ecx, 3
005B29A4  80 F9 03                        cmp cl, 3
005B29A7  0F 84 30 01 00 00               je 0x1405b2add
005B29AD  8B C8                           mov ecx, eax
005B29AF  F0 0F B1 15 95 4B 99 00         lock cmpxchg dword ptr [rip + 0x994b95], edx
005B29B7  3B C1                           cmp eax, ecx
005B29B9  75 E4                           jne 0x1405b299f
005B29BB  45 33 C0                        xor r8d, r8d
005B29BE  41 8D 48 06                     lea ecx, [r8 + 6]
005B29C2  E8 B1 01 FE FF                  call 0x140592b78
005B29C7  84 DB                           test bl, bl
005B29C9  0F 84 8D 00 00 00               je 0x1405b2a5c
005B29CF  8B 45 A8                        mov eax, dword ptr [rbp - 0x58]
005B29D2  83 F8 09                        cmp eax, 9
005B29D5  77 0A                           ja 0x1405b29e1
005B29D7  B9 A1 03 00 00                  mov ecx, 0x3a1
005B29DC  0F A3 C1                        bt ecx, eax
005B29DF  72 7B                           jb 0x1405b2a5c
005B29E1  48 8B 45 C0                     mov rax, qword ptr [rbp - 0x40]
005B29E5  BF 00 40 02 00                  mov edi, 0x24000
005B29EA  48 8B 5D C8                     mov rbx, qword ptr [rbp - 0x38]
005B29EE  41 B6 01                        mov r14b, 1
005B29F1  48 2B C3                        sub rax, rbx
005B29F4  48 3B C7                        cmp rax, rdi
005B29F7  77 08                           ja 0x1405b2a01
005B29F9  48 8B F8                        mov rdi, rax
005B29FC  48 85 C0                        test rax, rax
005B29FF  74 46                           je 0x1405b2a47
005B2A01  48 8D 35 38 0B 97 00            lea rsi, [rip + 0x970b38]
005B2A08  48 2B F3                        sub rsi, rbx
005B2A0B  48 FF CF                        dec rdi
005B2A0E  48 C1 EF 0C                     shr rdi, 0xc
005B2A12  48 FF C7                        inc rdi
005B2A15  33 D2                           xor edx, edx
005B2A17  48 8B CB                        mov rcx, rbx
005B2A1A  E8 B1 D3 CC FF                  call 0x14027fdd0
005B2A1F  84 C0                           test al, al
005B2A21  74 14                           je 0x1405b2a37
005B2A23  48 8D 0C 33                     lea rcx, [rbx + rsi]
005B2A27  41 B8 00 10 00 00               mov r8d, 0x1000
005B2A2D  48 8B D3                        mov rdx, rbx
005B2A30  E8 0B 3E 11 00                  call 0x1406c6840
005B2A35  EB 03                           jmp 0x1405b2a3a
005B2A37  45 32 F6                        xor r14b, r14b
005B2A3A  48 81 C3 00 10 00 00            add rbx, 0x1000
005B2A41  48 83 EF 01                     sub rdi, 1
005B2A45  75 CE                           jne 0x1405b2a15
005B2A47  45 0F B6 C6                     movzx r8d, r14b
005B2A4B  B9 07 00 00 00                  mov ecx, 7
005B2A50  E8 23 01 FE FF                  call 0x140592b78
005B2A55  48 8B 7D B8                     mov rdi, qword ptr [rbp - 0x48]
005B2A59  45 33 F6                        xor r14d, r14d
005B2A5C  44 38 35 DE ED C4 00            cmp byte ptr [rip + 0xc4edde], r14b
005B2A63  74 69                           je 0x1405b2ace
005B2A65  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
005B2A6E  45 33 C0                        xor r8d, r8d
005B2A71  F3 49 0F 1E C8                  rdsspq r8
005B2A76  48 8B 88 20 04 00 00            mov rcx, qword ptr [rax + 0x420]
005B2A7D  48 8B 90 18 04 00 00            mov rdx, qword ptr [rax + 0x418]
005B2A84  48 81 E1 00 F0 FF FF            and rcx, 0xfffffffffffff000
005B2A8B  48 81 C1 00 10 00 00            add rcx, 0x1000
005B2A92  48 81 EA 00 10 00 00            sub rdx, 0x1000
005B2A99  4C 3B C1                        cmp r8, rcx
005B2A9C  76 30                           jbe 0x1405b2ace
005B2A9E  BB 00 01 00 00                  mov ebx, 0x100
005B2AA3  4C 3B C2                        cmp r8, rdx
005B2AA6  73 2B                           jae 0x1405b2ad3
005B2AA8  49 8D 90 00 FF FF FF            lea rdx, [r8 - 0x100]
005B2AAF  48 3B D1                        cmp rdx, rcx
005B2AB2  48 0F 42 D1                     cmovb rdx, rcx
005B2AB6  48 8D 0D 03 56 A1 00            lea rcx, [rip + 0xa15603]
005B2ABD  4C 2B C2                        sub r8, rdx
005B2AC0  4C 3B C3                        cmp r8, rbx
005B2AC3  4C 0F 47 C3                     cmova r8, rbx
005B2AC7  E8 74 3D 11 00                  call 0x1406c6840
005B2ACC  EB 05                           jmp 0x1405b2ad3
005B2ACE  BB 00 01 00 00                  mov ebx, 0x100
005B2AD3  40 B6 01                        mov sil, 1
005B2AD6  40 88 74 24 58                  mov byte ptr [rsp + 0x58], sil
005B2ADB  EB 0D                           jmp 0x1405b2aea
005B2ADD  41 8A F6                        mov sil, r14b
005B2AE0  44 88 74 24 58                  mov byte ptr [rsp + 0x58], r14b
005B2AE5  BB 00 01 00 00                  mov ebx, 0x100
005B2AEA  BA 02 00 00 00                  mov edx, 2
005B2AEF  44 0F B6 CE                     movzx r9d, sil
005B2AF3  4C 8D 05 B6 8B 11 00            lea r8, [rip + 0x118bb6]
005B2AFA  8D 4A 03                        lea ecx, [rdx + 3]
005B2AFD  E8 8E 67 DA FF                  call 0x140359290
005B2B02  40 84 F6                        test sil, sil
005B2B05  74 11                           je 0x1405b2b18
005B2B07  8B 05 FF DD 95 00               mov eax, dword ptr [rip + 0x95ddff]
005B2B0D  85 C0                           test eax, eax
005B2B0F  7F 07                           jg 0x1405b2b18
005B2B11  C6 05 30 4A 99 00 01            mov byte ptr [rip + 0x994a30], 1
005B2B18  44 39 35 D1 40 A1 00            cmp dword ptr [rip + 0xa140d1], r14d
005B2B1F  74 03                           je 0x1405b2b24
005B2B21  0F 01 CB                        stac
005B2B24  65 4C 8B 34 25 20 00 00 00      mov r14, qword ptr gs:[0x20]
005B2B2D  48 8B 15 2C 41 A1 00            mov rdx, qword ptr [rip + 0xa1412c]
005B2B34  48 0B D3                        or rdx, rbx
005B2B37  41 8B 46 24                     mov eax, dword ptr [r14 + 0x24]
005B2B3B  49 8B 8E C0 06 00 00            mov rcx, qword ptr [r14 + 0x6c0]
005B2B42  89 45 B8                        mov dword ptr [rbp - 0x48], eax
005B2B45  E8 6A 71 00 00                  call 0x1405b9cb4
005B2B4A  48 8B 05 3F 92 95 00            mov rax, qword ptr [rip + 0x95923f]
005B2B51  8B 5D 80                        mov ebx, dword ptr [rbp - 0x80]
005B2B54  48 85 C0                        test rax, rax
005B2B57  75 05                           jne 0x1405b2b5e
005B2B59  40 32 F6                        xor sil, sil
005B2B5C  EB 4D                           jmp 0x1405b2bab
005B2B5E  83 3D 7B 97 95 00 00            cmp dword ptr [rip + 0x95977b], 0
005B2B65  74 07                           je 0x1405b2b6e
005B2B67  C6 05 B2 91 95 00 00            mov byte ptr [rip + 0x9591b2], 0
005B2B6E  80 78 02 00                     cmp byte ptr [rax + 2], 0
005B2B72  74 E5                           je 0x1405b2b59
005B2B74  40 84 F6                        test sil, sil
005B2B77  74 2A                           je 0x1405b2ba3
005B2B79  33 D2                           xor edx, edx
005B2B7B  4C 8D 05 EE 93 11 00            lea r8, [rip + 0x1193ee]
005B2B82  8D 4A 65                        lea ecx, [rdx + 0x65]
005B2B85  E8 06 67 DA FF                  call 0x140359290
005B2B8A  83 FB 0A                        cmp ebx, 0xa
005B2B8D  75 11                           jne 0x1405b2ba0
005B2B8F  4C 8D 05 9A 94 11 00            lea r8, [rip + 0x11949a]
005B2B96  33 D2                           xor edx, edx
005B2B98  8D 4B 5B                        lea ecx, [rbx + 0x5b]
005B2B9B  E8 F0 66 DA FF                  call 0x140359290
005B2BA0  8B 5D 80                        mov ebx, dword ptr [rbp - 0x80]
005B2BA3  48 83 65 B0 00                  and qword ptr [rbp - 0x50], 0
005B2BA8  40 B6 01                        mov sil, 1
005B2BAB  49 8B 86 C0 8F 00 00            mov rax, qword ptr [r14 + 0x8fc0]
005B2BB2  48 8D 8D F0 00 00 00            lea rcx, [rbp + 0xf0]
005B2BB9  BA 09 00 00 00                  mov edx, 9
005B2BBE  44 8D 42 77                     lea r8d, [rdx + 0x77]
005B2BC2  0F 10 00                        movups xmm0, xmmword ptr [rax]
005B2BC5  0F 11 01                        movups xmmword ptr [rcx], xmm0
005B2BC8  0F 10 48 10                     movups xmm1, xmmword ptr [rax + 0x10]
005B2BCC  0F 11 49 10                     movups xmmword ptr [rcx + 0x10], xmm1
005B2BD0  0F 10 40 20                     movups xmm0, xmmword ptr [rax + 0x20]
005B2BD4  0F 11 41 20                     movups xmmword ptr [rcx + 0x20], xmm0
005B2BD8  0F 10 48 30                     movups xmm1, xmmword ptr [rax + 0x30]
005B2BDC  0F 11 49 30                     movups xmmword ptr [rcx + 0x30], xmm1
005B2BE0  0F 10 40 40                     movups xmm0, xmmword ptr [rax + 0x40]
005B2BE4  0F 11 41 40                     movups xmmword ptr [rcx + 0x40], xmm0
005B2BE8  0F 10 48 50                     movups xmm1, xmmword ptr [rax + 0x50]
005B2BEC  0F 11 49 50                     movups xmmword ptr [rcx + 0x50], xmm1
005B2BF0  0F 10 40 60                     movups xmm0, xmmword ptr [rax + 0x60]
005B2BF4  0F 11 41 60                     movups xmmword ptr [rcx + 0x60], xmm0
005B2BF8  49 03 C8                        add rcx, r8
005B2BFB  0F 10 48 70                     movups xmm1, xmmword ptr [rax + 0x70]
005B2BFF  49 03 C0                        add rax, r8
005B2C02  0F 11 49 F0                     movups xmmword ptr [rcx - 0x10], xmm1
005B2C06  48 83 EA 01                     sub rdx, 1
005B2C0A  75 B6                           jne 0x1405b2bc2
005B2C0C  0F 10 00                        movups xmm0, xmmword ptr [rax]
005B2C0F  0F 11 01                        movups xmmword ptr [rcx], xmm0
005B2C12  0F 10 48 10                     movups xmm1, xmmword ptr [rax + 0x10]
005B2C16  0F 11 49 10                     movups xmmword ptr [rcx + 0x10], xmm1
005B2C1A  0F 10 40 20                     movups xmm0, xmmword ptr [rax + 0x20]
005B2C1E  0F 11 41 20                     movups xmmword ptr [rcx + 0x20], xmm0
005B2C22  0F 10 48 30                     movups xmm1, xmmword ptr [rax + 0x30]
005B2C26  0F 11 49 30                     movups xmmword ptr [rcx + 0x30], xmm1
005B2C2A  0F 10 40 40                     movups xmm0, xmmword ptr [rax + 0x40]
005B2C2E  0F 11 41 40                     movups xmmword ptr [rcx + 0x40], xmm0
005B2C32  38 54 24 58                     cmp byte ptr [rsp + 0x58], dl
005B2C36  0F 84 C4 06 00 00               je 0x1405b3300
005B2C3C  39 15 42 1D 95 00               cmp dword ptr [rip + 0x951d42], edx
005B2C42  74 0B                           je 0x1405b2c4f
005B2C44  8D 4A 02                        lea ecx, [rdx + 2]
005B2C47  E8 44 02 5E 00                  call 0x140b92e90
005B2C4C  8B 5D 80                        mov ebx, dword ptr [rbp - 0x80]
005B2C4F  81 FB E5 00 00 00               cmp ebx, 0xe5
005B2C55  75 20                           jne 0x1405b2c77
005B2C57  E8 08 28 00 00                  call 0x1405b5464
005B2C5C  48 8B 05 A5 DE 84 00            mov rax, qword ptr [rip + 0x84dea5]
005B2C63  33 C9                           xor ecx, ecx
005B2C65  E8 66 7E 10 00                  call 0x1406baad0
005B2C6A  B9 03 00 00 00                  mov ecx, 3
005B2C6F  E8 DC 38 F9 FF                  call 0x140546550
005B2C74  8B 5D 80                        mov ebx, dword ptr [rbp - 0x80]
005B2C77  81 FB D1 00 00 00               cmp ebx, 0xd1
005B2C7D  0F 87 D7 02 00 00               ja 0x1405b2f5a
005B2C83  0F 84 AD 01 00 00               je 0x1405b2e36
005B2C89  8B C3                           mov eax, ebx
005B2C8B  83 E8 0A                        sub eax, 0xa
005B2C8E  0F 84 A2 01 00 00               je 0x1405b2e36
005B2C94  83 E8 31                        sub eax, 0x31
005B2C97  0F 84 90 01 00 00               je 0x1405b2e2d
005B2C9D  83 E8 11                        sub eax, 0x11
005B2CA0  0F 84 3F 01 00 00               je 0x1405b2de5
005B2CA6  83 E8 04                        sub eax, 4
005B2CA9  0F 84 BA 00 00 00               je 0x1405b2d69
005B2CAF  83 E8 2B                        sub eax, 0x2b
005B2CB2  0F 84 8E 00 00 00               je 0x1405b2d46
005B2CB8  83 E8 13                        sub eax, 0x13
005B2CBB  0F 84 92 03 00 00               je 0x1405b3053
005B2CC1  83 E8 12                        sub eax, 0x12
005B2CC4  74 4A                           je 0x1405b2d10
005B2CC6  83 E8 1E                        sub eax, 0x1e
005B2CC9  0F 84 84 03 00 00               je 0x1405b3053
005B2CCF  83 F8 0D                        cmp eax, 0xd
005B2CD2  0F 85 CB 02 00 00               jne 0x1405b2fa3
005B2CD8  4C 89 7D 88                     mov qword ptr [rbp - 0x78], r15
005B2CDC  48 8B 7C 24 60                  mov rdi, qword ptr [rsp + 0x60]
005B2CE1  8B 5C 24 54                     mov ebx, dword ptr [rsp + 0x54]
005B2CE5  44 8A 7C 24 50                  mov r15b, byte ptr [rsp + 0x50]
005B2CEA  4C 8B 6C 24 70                  mov r13, qword ptr [rsp + 0x70]
005B2CEF  48 8B 0D EA 3A 8B 00            mov rcx, qword ptr [rip + 0x8b3aea]
005B2CF6  48 85 C9                        test rcx, rcx
005B2CF9  0F 84 BF 03 00 00               je 0x1405b30be
005B2CFF  48 8D 95 C0 05 00 00            lea rdx, [rbp + 0x5c0]
005B2D06  E8 F9 13 00 00                  call 0x1405b4104
005B2D0B  E9 CE 03 00 00                  jmp 0x1405b30de
005B2D10  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
005B2D19  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
005B2D20  F7 81 FC 05 00 00 00 10 00 00   test dword ptr [rcx + 0x5fc], 0x1000
005B2D2A  75 B0                           jne 0x1405b2cdc
005B2D2C  48 8B 7C 24 60                  mov rdi, qword ptr [rsp + 0x60]
005B2D31  49 8D 87 10 FF FF FF            lea rax, [r15 - 0xf0]
005B2D38  48 83 F8 01                     cmp rax, 1
005B2D3C  77 A3                           ja 0x1405b2ce1
005B2D3E  B3 01                           mov bl, 1
005B2D40  89 5C 24 54                     mov dword ptr [rsp + 0x54], ebx
005B2D44  EB 9F                           jmp 0x1405b2ce5
005B2D46  48 8B 7C 24 60                  mov rdi, qword ptr [rsp + 0x60]
005B2D4B  41 8A C4                        mov al, r12b
005B2D4E  8B 5C 24 54                     mov ebx, dword ptr [rsp + 0x54]
005B2D52  45 8A FC                        mov r15b, r12b
005B2D55  41 D0 EF                        shr r15b, 1
005B2D58  F6 D0                           not al
005B2D5A  24 01                           and al, 1
005B2D5C  41 F6 D7                        not r15b
005B2D5F  88 44 24 59                     mov byte ptr [rsp + 0x59], al
005B2D63  41 80 E7 01                     and r15b, 1
005B2D67  EB 81                           jmp 0x1405b2cea
005B2D69  48 8B 7C 24 60                  mov rdi, qword ptr [rsp + 0x60]
005B2D6E  48 85 FF                        test rdi, rdi
005B2D71  75 0E                           jne 0x1405b2d81
005B2D73  4D 85 E4                        test r12, r12
005B2D76  74 3A                           je 0x1405b2db2
005B2D78  41 F6 C4 03                     test r12b, 3
005B2D7C  75 34                           jne 0x1405b2db2
005B2D7E  49 8B FC                        mov rdi, r12
005B2D81  48 8B 8F 68 01 00 00            mov rcx, qword ptr [rdi + 0x168]
005B2D88  4C 8D 4C 24 5A                  lea r9, [rsp + 0x5a]
005B2D8D  45 33 C0                        xor r8d, r8d
005B2D90  48 89 4D 88                     mov qword ptr [rbp - 0x78], rcx
005B2D94  48 8D 55 98                     lea rdx, [rbp - 0x68]
005B2D98  48 89 0D F9 47 99 00            mov qword ptr [rip + 0x9947f9], rcx
005B2D9F  E8 C4 24 00 00                  call 0x1405b5268
005B2DA4  48 89 7C 24 60                  mov qword ptr [rsp + 0x60], rdi
005B2DA9  48 85 C0                        test rax, rax
005B2DAC  0F 85 2F FF FF FF               jne 0x1405b2ce1
005B2DB2  49 8B CF                        mov rcx, r15
005B2DB5  E8 52 E9 0B 00                  call 0x14067170c
005B2DBA  48 85 C0                        test rax, rax
005B2DBD  0F 84 1E FF FF FF               je 0x1405b2ce1
005B2DC3  44 2B 78 10                     sub r15d, dword ptr [rax + 0x10]
005B2DC7  44 89 3D 22 3A 8B 00            mov dword ptr [rip + 0x8b3a22], r15d
005B2DCE  48 89 05 0B 3A 8B 00            mov qword ptr [rip + 0x8b3a0b], rax
005B2DD5  48 C7 05 A0 47 99 00 CE 00 00 00  mov qword ptr [rip + 0x9947a0], 0xce
005B2DE0  E9 FC FE FF FF                  jmp 0x1405b2ce1
005B2DE5  B3 01                           mov bl, 1
005B2DE7  41 8B C7                        mov eax, r15d
005B2DEA  48 8D 0D 97 47 99 00            lea rcx, [rip + 0x994797]
005B2DF1  89 5C 24 54                     mov dword ptr [rsp + 0x54], ebx
005B2DF5  88 5C 24 78                     mov byte ptr [rsp + 0x78], bl
005B2DF9  48 8D 15 A8 47 99 00            lea rdx, [rip + 0x9947a8]
005B2E00  48 89 05 79 47 99 00            mov qword ptr [rip + 0x994779], rax
005B2E07  48 2B F9                        sub rdi, rcx
005B2E0A  4C 89 65 D0                     mov qword ptr [rbp - 0x30], r12
005B2E0E  48 8B 04 0F                     mov rax, qword ptr [rdi + rcx]
005B2E12  48 89 01                        mov qword ptr [rcx], rax
005B2E15  48 83 C1 08                     add rcx, 8
005B2E19  48 3B CA                        cmp rcx, rdx
005B2E1C  7C F0                           jl 0x1405b2e0e
005B2E1E  48 8B 7C 24 60                  mov rdi, qword ptr [rsp + 0x60]
005B2E23  44 8A 7C 24 50                  mov r15b, byte ptr [rsp + 0x50]
005B2E28  E9 C2 FE FF FF                  jmp 0x1405b2cef
005B2E2D  4C 89 6D 88                     mov qword ptr [rbp - 0x78], r13
005B2E31  E9 A6 FE FF FF                  jmp 0x1405b2cdc
005B2E36  4C 3B 2D 5B 26 94 00            cmp r13, qword ptr [rip + 0x94265b]
005B2E3D  4C 89 6D 88                     mov qword ptr [rbp - 0x78], r13
005B2E41  72 19                           jb 0x1405b2e5c
005B2E43  4C 3B 2D 56 26 94 00            cmp r13, qword ptr [rip + 0x942656]
005B2E4A  73 10                           jae 0x1405b2e5c
005B2E4C  48 C7 05 29 47 99 00 C5 00 00 00  mov qword ptr [rip + 0x994729], 0xc5
005B2E57  E9 80 FE FF FF                  jmp 0x1405b2cdc
005B2E5C  4C 8D 4C 24 5A                  lea r9, [rsp + 0x5a]
005B2E61  45 33 C0                        xor r8d, r8d
005B2E64  48 8D 55 98                     lea rdx, [rbp - 0x68]
005B2E68  49 8B CD                        mov rcx, r13
005B2E6B  E8 F8 23 00 00                  call 0x1405b5268
005B2E70  80 7C 24 5A 01                  cmp byte ptr [rsp + 0x5a], 1
005B2E75  0F 85 9F 00 00 00               jne 0x1405b2f1a
005B2E7B  44 2B E8                        sub r13d, eax
005B2E7E  4C 8D 4C 24 5A                  lea r9, [rsp + 0x5a]
005B2E83  48 8B 45 98                     mov rax, qword ptr [rbp - 0x68]
005B2E87  48 8D 55 98                     lea rdx, [rbp - 0x68]
005B2E8B  48 83 C0 58                     add rax, 0x58
005B2E8F  44 89 2D 5A 39 8B 00            mov dword ptr [rip + 0x8b395a], r13d
005B2E96  41 B8 01 00 00 00               mov r8d, 1
005B2E9C  48 89 05 3D 39 8B 00            mov qword ptr [rip + 0x8b393d], rax
005B2EA3  49 8B CF                        mov rcx, r15
005B2EA6  E8 BD 23 00 00                  call 0x1405b5268
005B2EAB  48 85 C0                        test rax, rax
005B2EAE  74 29                           je 0x1405b2ed9
005B2EB0  44 2B F8                        sub r15d, eax
005B2EB3  48 C7 05 C2 46 99 00 D3 00 00 00  mov qword ptr [rip + 0x9946c2], 0xd3
005B2EBE  48 8B 45 98                     mov rax, qword ptr [rbp - 0x68]
005B2EC2  48 83 C0 58                     add rax, 0x58
005B2EC6  44 89 3D 23 39 8B 00            mov dword ptr [rip + 0x8b3923], r15d
005B2ECD  48 89 05 0C 39 8B 00            mov qword ptr [rip + 0x8b390c], rax
005B2ED4  E9 03 FE FF FF                  jmp 0x1405b2cdc
005B2ED9  49 8B CF                        mov rcx, r15
005B2EDC  E8 2B E8 0B 00                  call 0x14067170c
005B2EE1  48 8B 7C 24 60                  mov rdi, qword ptr [rsp + 0x60]
005B2EE6  8B 5C 24 54                     mov ebx, dword ptr [rsp + 0x54]
005B2EEA  4C 8B 6C 24 70                  mov r13, qword ptr [rsp + 0x70]
005B2EEF  48 85 C0                        test rax, rax
005B2EF2  0F 84 2B FF FF FF               je 0x1405b2e23
005B2EF8  44 2B 78 10                     sub r15d, dword ptr [rax + 0x10]
005B2EFC  44 89 3D ED 38 8B 00            mov dword ptr [rip + 0x8b38ed], r15d
005B2F03  48 89 05 D6 38 8B 00            mov qword ptr [rip + 0x8b38d6], rax
005B2F0A  48 C7 05 6B 46 99 00 D4 00 00 00  mov qword ptr [rip + 0x99466b], 0xd4
005B2F15  E9 09 FF FF FF                  jmp 0x1405b2e23
005B2F1A  48 8B 7C 24 60                  mov rdi, qword ptr [rsp + 0x60]
005B2F1F  8B 5C 24 54                     mov ebx, dword ptr [rsp + 0x54]
005B2F23  44 8A 7C 24 50                  mov r15b, byte ptr [rsp + 0x50]
005B2F28  48 C7 05 4D 46 99 00 D1 00 00 00  mov qword ptr [rip + 0x99464d], 0xd1
005B2F33  48 85 C0                        test rax, rax
005B2F36  0F 84 AE FD FF FF               je 0x1405b2cea
005B2F3C  44 2B E8                        sub r13d, eax
005B2F3F  48 8B 45 98                     mov rax, qword ptr [rbp - 0x68]
005B2F43  48 83 C0 58                     add rax, 0x58
005B2F47  44 89 2D A2 38 8B 00            mov dword ptr [rip + 0x8b38a2], r13d
005B2F4E  48 89 05 8B 38 8B 00            mov qword ptr [rip + 0x8b388b], rax
005B2F55  E9 90 FD FF FF                  jmp 0x1405b2cea
005B2F5A  8B C3                           mov eax, ebx
005B2F5C  2D D8 00 00 00                  sub eax, 0xd8
005B2F61  0F 84 47 01 00 00               je 0x1405b30ae
005B2F67  83 E8 0E                        sub eax, 0xe
005B2F6A  0F 84 23 01 00 00               je 0x1405b3093
005B2F70  83 E8 04                        sub eax, 4
005B2F73  0F 84 0E 01 00 00               je 0x1405b3087
005B2F79  83 E8 05                        sub eax, 5
005B2F7C  0F 84 01 01 00 00               je 0x1405b3083
005B2F82  83 E8 0D                        sub eax, 0xd
005B2F85  0F 84 C8 00 00 00               je 0x1405b3053
005B2F8B  83 E8 3D                        sub eax, 0x3d
005B2F8E  0F 84 90 00 00 00               je 0x1405b3024
005B2F94  83 E8 04                        sub eax, 4
005B2F97  74 7F                           je 0x1405b3018
005B2F99  83 E8 12                        sub eax, 0x12
005B2F9C  74 2D                           je 0x1405b2fcb
005B2F9E  83 F8 79                        cmp eax, 0x79
005B2FA1  74 1E                           je 0x1405b2fc1
005B2FA3  48 8B 7C 24 60                  mov rdi, qword ptr [rsp + 0x60]
005B2FA8  48 85 FF                        test rdi, rdi
005B2FAB  0F 84 30 FD FF FF               je 0x1405b2ce1
005B2FB1  48 8B 87 68 01 00 00            mov rax, qword ptr [rdi + 0x168]
005B2FB8  48 89 45 88                     mov qword ptr [rbp - 0x78], rax
005B2FBC  E9 20 FD FF FF                  jmp 0x1405b2ce1
005B2FC1  C6 44 24 7A 01                  mov byte ptr [rsp + 0x7a], 1
005B2FC6  E9 11 FD FF FF                  jmp 0x1405b2cdc
005B2FCB  48 81 FF 00 01 00 00            cmp rdi, 0x100
005B2FD2  73 18                           jae 0x1405b2fec
005B2FD4  4D 85 ED                        test r13, r13
005B2FD7  74 13                           je 0x1405b2fec
005B2FD9  49 8B 45 08                     mov rax, qword ptr [r13 + 8]
005B2FDD  48 8B 4D A0                     mov rcx, qword ptr [rbp - 0x60]
005B2FE1  48 85 C0                        test rax, rax
005B2FE4  48 0F 45 C8                     cmovne rcx, rax
005B2FE8  48 89 4D A0                     mov qword ptr [rbp - 0x60], rcx
005B2FEC  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
005B2FF5  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
005B2FFC  8B 99 FC 05 00 00               mov ebx, dword ptr [rcx + 0x5fc]
005B3002  C1 EB 0C                        shr ebx, 0xc
005B3005  F6 D3                           not bl
005B3007  80 E3 01                        and bl, 1
005B300A  89 5C 24 54                     mov dword ptr [rsp + 0x54], ebx
005B300E  48 8B 7C 24 60                  mov rdi, qword ptr [rsp + 0x60]
005B3013  E9 CD FC FF FF                  jmp 0x1405b2ce5
005B3018  C7 45 90 08 00 00 00            mov dword ptr [rbp - 0x70], 8
005B301F  E9 B8 FC FF FF                  jmp 0x1405b2cdc
005B3024  48 83 7C 24 60 00               cmp qword ptr [rsp + 0x60], 0
005B302A  8B 5C 24 54                     mov ebx, dword ptr [rsp + 0x54]
005B302E  74 15                           je 0x1405b3045
005B3030  48 8B 7C 24 60                  mov rdi, qword ptr [rsp + 0x60]
005B3035  48 8B 87 68 01 00 00            mov rax, qword ptr [rdi + 0x168]
005B303C  48 89 45 88                     mov qword ptr [rbp - 0x78], rax
005B3040  E9 A0 FC FF FF                  jmp 0x1405b2ce5
005B3045  49 83 FF 0A                     cmp r15, 0xa
005B3049  49 0F 44 FD                     cmove rdi, r13
005B304D  48 89 7D 88                     mov qword ptr [rbp - 0x78], rdi
005B3051  EB BB                           jmp 0x1405b300e
005B3053  48 8B 7C 24 60                  mov rdi, qword ptr [rsp + 0x60]
005B3058  48 85 FF                        test rdi, rdi
005B305B  75 1B                           jne 0x1405b3078
005B305D  4D 85 E4                        test r12, r12
005B3060  0F 84 7B FC FF FF               je 0x1405b2ce1
005B3066  41 F6 C4 03                     test r12b, 3
005B306A  0F 85 71 FC FF FF               jne 0x1405b2ce1
005B3070  49 8B FC                        mov rdi, r12
005B3073  4C 89 64 24 60                  mov qword ptr [rsp + 0x60], r12
005B3078  81 FB 8E 00 00 00               cmp ebx, 0x8e
005B307E  E9 28 FF FF FF                  jmp 0x1405b2fab
005B3083  B3 01                           mov bl, 1
005B3085  EB 83                           jmp 0x1405b300a
005B3087  4C 89 25 52 37 8B 00            mov qword ptr [rip + 0x8b3752], r12
005B308E  E9 49 FC FF FF                  jmp 0x1405b2cdc
005B3093  41 83 FF 27                     cmp r15d, 0x27
005B3097  0F 85 3F FC FF FF               jne 0x1405b2cdc
005B309D  41 8D 57 E1                     lea edx, [r15 - 0x1f]
005B30A1  48 8B CF                        mov rcx, rdi
005B30A4  E8 CB 52 E7 FF                  call 0x140428374
005B30A9  E9 2E FC FF FF                  jmp 0x1405b2cdc
005B30AE  49 8D 47 58                     lea rax, [r15 + 0x58]
005B30B2  48 89 05 27 37 8B 00            mov qword ptr [rip + 0x8b3727], rax
005B30B9  E9 1E FC FF FF                  jmp 0x1405b2cdc
005B30BE  48 83 7D 88 00                  cmp qword ptr [rbp - 0x78], 0
005B30C3  74 19                           je 0x1405b30de
005B30C5  41 B1 01                        mov r9b, 1
005B30C8  48 8D 55 88                     lea rdx, [rbp - 0x78]
005B30CC  41 B8 01 00 00 00               mov r8d, 1
005B30D2  48 8D 8D C0 05 00 00            lea rcx, [rbp + 0x5c0]
005B30D9  E8 02 1C 00 00                  call 0x1405b4ce0
005B30DE  83 3D 1B 6E 94 00 00            cmp dword ptr [rip + 0x946e1b], 0
005B30E5  75 1A                           jne 0x1405b3101
005B30E7  E8 C8 AA 0A 00                  call 0x14065dbb4
005B30EC  48 8D 0D 8D 6F 94 00            lea rcx, [rip + 0x946f8d]
005B30F3  E8 E4 33 0F 00                  call 0x1406a64dc
005B30F8  84 C0                           test al, al
005B30FA  74 05                           je 0x1405b3101
005B30FC  E8 3F 39 0F 00                  call 0x1406a6a40
005B3101  48 8B 0D 78 44 99 00            mov rcx, qword ptr [rip + 0x994478]
005B3108  33 C0                           xor eax, eax
005B310A  81 F9 09 01 00 00               cmp ecx, 0x109
005B3110  0F 95 C0                        setne al
005B3113  89 05 BB 2D 8B 00               mov dword ptr [rip + 0x8b2dbb], eax
005B3119  45 84 FF                        test r15b, r15b
005B311C  74 08                           je 0x1405b3126
005B311E  40 8A D6                        mov dl, sil
005B3121  E8 D2 12 00 00                  call 0x1405b43f8
005B3126  80 7C 24 68 00                  cmp byte ptr [rsp + 0x68], 0
005B312B  4C 8B 65 A0                     mov r12, qword ptr [rbp - 0x60]
005B312F  74 43                           je 0x1405b3174
005B3131  8B 05 7D 78 85 00               mov eax, dword ptr [rip + 0x85787d]
005B3137  A8 04                           test al, 4
005B3139  74 39                           je 0x1405b3174
005B313B  48 8D 85 F0 00 00 00            lea rax, [rbp + 0xf0]
005B3142  4C 89 25 BF 03 97 00            mov qword ptr [rip + 0x9703bf], r12
005B3149  48 89 05 B0 03 97 00            mov qword ptr [rip + 0x9703b0], rax
005B3150  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
005B3154  48 89 05 B5 03 97 00            mov qword ptr [rip + 0x9703b5], rax
005B315B  48 89 3D B6 03 97 00            mov qword ptr [rip + 0x9703b6], rdi
005B3162  88 1D B8 03 97 00               mov byte ptr [rip + 0x9703b8], bl
005B3168  40 88 35 B2 03 97 00            mov byte ptr [rip + 0x9703b2], sil
005B316F  E8 B0 3B 01 00                  call 0x1405c6d24
005B3174  48 8B 05 AD D9 84 00            mov rax, qword ptr [rip + 0x84d9ad]
005B317B  C6 05 C6 43 99 00 01            mov byte ptr [rip + 0x9943c6], 1
005B3182  E8 49 79 10 00                  call 0x1406baad0
005B3187  81 25 27 39 A1 00 00 20 00 00   and dword ptr [rip + 0xa13927], 0x2000
005B3191  B9 60 00 00 00                  mov ecx, 0x60
005B3196  E8 75 FC FD FF                  call 0x140592e10
005B319B  48 8D 0D BE 78 85 00            lea rcx, [rip + 0x8578be]
005B31A2  E8 D9 E3 D1 FF                  call 0x1402d1580
005B31A7  33 FF                           xor edi, edi
005B31A9  85 C0                           test eax, eax
005B31AB  8B CF                           mov ecx, edi
005B31AD  48 8B 05 44 D7 84 00            mov rax, qword ptr [rip + 0x84d744]
005B31B4  0F 94 C1                        sete cl
005B31B7  E8 14 79 10 00                  call 0x1406baad0
005B31BC  48 8D 15 BD 43 99 00            lea rdx, [rip + 0x9943bd]
005B31C3  48 8D 4D 80                     lea rcx, [rbp - 0x80]
005B31C7  E8 F0 6C F5 FF                  call 0x140509ebc
005B31CC  48 39 3D 7D 2E 8B 00            cmp qword ptr [rip + 0x8b2e7d], rdi
005B31D3  74 05                           je 0x1405b31da
005B31D5  45 84 FF                        test r15b, r15b
005B31D8  75 04                           jne 0x1405b31de
005B31DA  B3 01                           mov bl, 1
005B31DC  EB 03                           jmp 0x1405b31e1
005B31DE  40 8A DF                        mov bl, dil
005B31E1  4C 8B 0D B0 43 99 00            mov r9, qword ptr [rip + 0x9943b0]
005B31E8  4C 8B 05 A1 43 99 00            mov r8, qword ptr [rip + 0x9943a1]
005B31EF  48 8B 15 92 43 99 00            mov rdx, qword ptr [rip + 0x994392]
005B31F6  8B 0D 84 43 99 00               mov ecx, dword ptr [rip + 0x994384]
005B31FC  0F B6 C3                        movzx eax, bl
005B31FF  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
005B3203  48 8B 05 96 43 99 00            mov rax, qword ptr [rip + 0x994396]
005B320A  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
005B320F  E8 70 0A FD FF                  call 0x140583c84
005B3214  40 38 3D 01 78 85 00            cmp byte ptr [rip + 0x857801], dil
005B321B  75 0E                           jne 0x1405b322b
005B321D  48 8D 85 F0 00 00 00            lea rax, [rbp + 0xf0]
005B3224  48 89 05 5D DE 84 00            mov qword ptr [rip + 0x84de5d], rax
005B322B  8B 4D 80                        mov ecx, dword ptr [rbp - 0x80]
005B322E  33 D2                           xor edx, edx
005B3230  E8 6B 0E 00 00                  call 0x1405b40a0
005B3235  84 C0                           test al, al
005B3237  0F 84 D2 00 00 00               je 0x1405b330f
005B323D  41 38 BE A6 83 00 00            cmp byte ptr [r14 + 0x83a6], dil
005B3244  0F 85 98 00 00 00               jne 0x1405b32e2
005B324A  48 8B 05 4F 43 99 00            mov rax, qword ptr [rip + 0x99434f]
005B3251  4C 8D 05 D8 84 11 00            lea r8, [rip + 0x1184d8]
005B3258  44 8B 0D 21 43 99 00            mov r9d, dword ptr [rip + 0x994321]
005B325F  33 D2                           xor edx, edx
005B3261  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
005B3266  48 8B 05 2B 43 99 00            mov rax, qword ptr [rip + 0x99432b]
005B326D  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
005B3272  48 8B 05 17 43 99 00            mov rax, qword ptr [rip + 0x994317]
005B3279  8D 4A 65                        lea ecx, [rdx + 0x65]
005B327C  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
005B3281  48 8B 05 00 43 99 00            mov rax, qword ptr [rip + 0x994300]
005B3288  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
005B328D  E8 FE 5F DA FF                  call 0x140359290
005B3292  48 39 3D 47 35 8B 00            cmp qword ptr [rip + 0x8b3547], rdi
005B3299  74 18                           je 0x1405b32b3
005B329B  33 D2                           xor edx, edx
005B329D  4C 8D 8D C0 05 00 00            lea r9, [rbp + 0x5c0]
005B32A4  4C 8D 05 65 84 11 00            lea r8, [rip + 0x118465]
005B32AB  8D 4A 65                        lea ecx, [rdx + 0x65]
005B32AE  E8 DD 5F DA FF                  call 0x140359290
005B32B3  40 38 7C 24 78                  cmp byte ptr [rsp + 0x78], dil
005B32B8  74 28                           je 0x1405b32e2
005B32BA  48 8B 45 D0                     mov rax, qword ptr [rbp - 0x30]
005B32BE  48 85 C0                        test rax, rax
005B32C1  74 0D                           je 0x1405b32d0
005B32C3  33 D2                           xor edx, edx
005B32C5  4C 8B C0                        mov r8, rax
005B32C8  8D 4A 65                        lea ecx, [rdx + 0x65]
005B32CB  E8 C0 5F DA FF                  call 0x140359290
005B32D0  4D 85 ED                        test r13, r13
005B32D3  74 0D                           je 0x1405b32e2
005B32D5  33 D2                           xor edx, edx
005B32D7  4D 8B C5                        mov r8, r13
005B32DA  8D 4A 65                        lea ecx, [rdx + 0x65]
005B32DD  E8 AE 5F DA FF                  call 0x140359290
005B32E2  40 38 3D 0F 43 99 00            cmp byte ptr [rip + 0x99430f], dil
005B32E9  74 24                           je 0x1405b330f
005B32EB  40 38 3D EA 42 99 00            cmp byte ptr [rip + 0x9942ea], dil
005B32F2  75 1B                           jne 0x1405b330f
005B32F4  B9 03 00 00 00                  mov ecx, 3
005B32F9  E8 C2 0A 00 00                  call 0x1405b3dc0
005B32FE  EB 0F                           jmp 0x1405b330f
005B3300  44 8A 7C 24 50                  mov r15b, byte ptr [rsp + 0x50]
005B3305  33 FF                           xor edi, edi
005B3307  4C 8B 65 A0                     mov r12, qword ptr [rbp - 0x60]
005B330B  8A 5C 24 79                     mov bl, byte ptr [rsp + 0x79]
005B330F  FA                              cli
005B3310  44 0F 20 C1                     mov rcx, cr8
005B3314  BA 0F 00 00 00                  mov edx, 0xf
005B3319  44 0F 22 C2                     mov cr8, rdx
005B331D  39 3D FD 39 A1 00               cmp dword ptr [rip + 0xa139fd], edi
005B3323  74 05                           je 0x1405b332a
005B3325  E8 D2 23 F4 FF                  call 0x1404f56fc
005B332A  40 38 7C 24 58                  cmp byte ptr [rsp + 0x58], dil
005B332F  0F 85 7D 01 00 00               jne 0x1405b34b2
005B3335  8B 0D 11 42 99 00               mov ecx, dword ptr [rip + 0x994211]
005B333B  E8 20 45 01 00                  call 0x1405c7860
005B3340  84 C0                           test al, al
005B3342  74 12                           je 0x1405b3356
005B3344  41 BD 01 00 00 00               mov r13d, 1
005B334A  44 88 2D F7 41 99 00            mov byte ptr [rip + 0x9941f7], r13b
005B3351  E9 62 01 00 00                  jmp 0x1405b34b8
005B3356  8B 05 F0 41 99 00               mov eax, dword ptr [rip + 0x9941f0]
005B335C  8B C8                           mov ecx, eax
005B335E  44 8B 4D B8                     mov r9d, dword ptr [rbp - 0x48]
005B3362  C1 E9 04                        shr ecx, 4
005B3365  44 3B C9                        cmp r9d, ecx
005B3368  74 06                           je 0x1405b3370
005B336A  E8 6D 23 00 00                  call 0x1405b56dc
005B336F  CC                              int3
005B3370  40 38 3D 71 34 8B 00            cmp byte ptr [rip + 0x8b3471], dil
005B3377  0F 85 13 01 00 00               jne 0x1405b3490
005B337D  8B D8                           mov ebx, eax
005B337F  C1 EB 02                        shr ebx, 2
005B3382  83 E3 03                        and ebx, 3
005B3385  83 FB 02                        cmp ebx, 2
005B3388  0F 83 02 01 00 00               jae 0x1405b3490
005B338E  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
005B3392  4C 8D 05 37 82 11 00            lea r8, [rip + 0x118237]
005B3399  BA 02 00 00 00                  mov edx, 2
005B339E  89 5C 24 28                     mov dword ptr [rsp + 0x28], ebx
005B33A2  83 E0 03                        and eax, 3
005B33A5  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
005B33A9  44 8D 72 03                     lea r14d, [rdx + 3]
005B33AD  41 8B CE                        mov ecx, r14d
005B33B0  E8 DB 5E DA FF                  call 0x140359290
005B33B5  B9 00 00 02 00                  mov ecx, 0x20000
005B33BA  E8 01 FE FD FF                  call 0x1405931c0
005B33BF  F0 83 05 85 41 99 00 04         lock add dword ptr [rip + 0x994185], 4
005B33C7  85 DB                           test ebx, ebx
005B33C9  0F 85 96 00 00 00               jne 0x1405b3465
005B33CF  8B 4C 24 54                     mov ecx, dword ptr [rsp + 0x54]
005B33D3  48 8D 85 F0 00 00 00            lea rax, [rbp + 0xf0]
005B33DA  48 8B 55 B0                     mov rdx, qword ptr [rbp - 0x50]
005B33DE  4C 8B 0D B3 41 99 00            mov r9, qword ptr [rip + 0x9941b3]
005B33E5  4C 8B 05 A4 41 99 00            mov r8, qword ptr [rip + 0x9941a4]
005B33EC  48 89 05 0D 01 97 00            mov qword ptr [rip + 0x97010d], rax
005B33F3  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
005B33F8  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
005B33FD  88 4C 24 40                     mov byte ptr [rsp + 0x40], cl
005B3401  48 89 54 24 38                  mov qword ptr [rsp + 0x38], rdx
005B3406  48 89 05 0B 01 97 00            mov qword ptr [rip + 0x97010b], rax
005B340D  48 8D 85 F0 00 00 00            lea rax, [rbp + 0xf0]
005B3414  4C 89 64 24 30                  mov qword ptr [rsp + 0x30], r12
005B3419  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
005B341E  48 8B 05 7B 41 99 00            mov rax, qword ptr [rip + 0x99417b]
005B3425  48 89 15 E4 00 97 00            mov qword ptr [rip + 0x9700e4], rdx
005B342C  48 8B 15 55 41 99 00            mov rdx, qword ptr [rip + 0x994155]
005B3433  88 0D E7 00 97 00               mov byte ptr [rip + 0x9700e7], cl
005B3439  8B 0D 41 41 99 00               mov ecx, dword ptr [rip + 0x994141]
005B343F  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
005B3444  4C 89 25 BD 00 97 00            mov qword ptr [rip + 0x9700bd], r12
005B344B  40 88 35 CF 00 97 00            mov byte ptr [rip + 0x9700cf], sil
005B3452  E8 49 F8 FD FF                  call 0x140592ca0
005B3457  40 8A 7C 24 59                  mov dil, byte ptr [rsp + 0x59]
005B345C  45 8D 6E FC                     lea r13d, [r14 - 4]
005B3460  E9 B1 02 00 00                  jmp 0x1405b3716
005B3465  41 BD 01 00 00 00               mov r13d, 1
005B346B  4C 8D 05 1E 81 11 00            lea r8, [rip + 0x11811e]
005B3472  41 8B D5                        mov edx, r13d
005B3475  41 8B CE                        mov ecx, r14d
005B3478  E8 13 5E DA FF                  call 0x140359290
005B347D  41 8D 4D 03                     lea ecx, [r13 + 3]
005B3481  E8 3A 09 00 00                  call 0x1405b3dc0
005B3486  40 8A 7C 24 59                  mov dil, byte ptr [rsp + 0x59]
005B348B  E9 86 02 00 00                  jmp 0x1405b3716
005B3490  BA 01 00 00 00                  mov edx, 1
005B3495  4C 8D 05 F4 81 11 00            lea r8, [rip + 0x1181f4]
005B349C  8D 4A 04                        lea ecx, [rdx + 4]
005B349F  E8 EC 5D DA FF                  call 0x140359290
005B34A4  48 8B 05 8D D3 84 00            mov rax, qword ptr [rip + 0x84d38d]
005B34AB  E8 20 76 10 00                  call 0x1406baad0
005B34B0  EB F2                           jmp 0x1405b34a4
005B34B2  41 BD 01 00 00 00               mov r13d, 1
005B34B8  8B 05 C2 35 A1 00               mov eax, dword ptr [rip + 0xa135c2]
005B34BE  41 3B C5                        cmp eax, r13d
005B34C1  76 60                           jbe 0x1405b3523
005B34C3  40 38 3D 1E 33 8B 00            cmp byte ptr [rip + 0x8b331e], dil
005B34CA  75 57                           jne 0x1405b3523
005B34CC  49 8B CE                        mov rcx, r14
005B34CF  E8 C0 99 F4 FF                  call 0x1404fce94
005B34D4  33 D2                           xor edx, edx
005B34D6  48 C7 45 E0 01 00 20 00         mov qword ptr [rbp - 0x20], 0x200001
005B34DE  48 8D 4D E8                     lea rcx, [rbp - 0x18]
005B34E2  41 B8 00 01 00 00               mov r8d, 0x100
005B34E8  E8 53 37 11 00                  call 0x1406c6c40
005B34ED  0F B7 55 E2                     movzx edx, word ptr [rbp - 0x1e]
005B34F1  4C 8D 05 28 3C A1 00            lea r8, [rip + 0xa13c28]
005B34F8  48 8D 4D E0                     lea rcx, [rbp - 0x20]
005B34FC  E8 5F B3 D1 FF                  call 0x1402ce860
005B3501  41 8B 56 24                     mov edx, dword ptr [r14 + 0x24]
005B3505  48 8D 4D E0                     lea rcx, [rbp - 0x20]
005B3509  E8 02 19 D5 FF                  call 0x140304e10
005B350E  33 D2                           xor edx, edx
005B3510  48 8D 4D E0                     lea rcx, [rbp - 0x20]
005B3514  E8 4B FE 00 00                  call 0x1405c3364
005B3519  B9 40 42 0F 00                  mov ecx, 0xf4240
005B351E  E8 FD C0 E9 FF                  call 0x14044f620
005B3523  48 8B 15 5E 40 99 00            mov rdx, qword ptr [rip + 0x99405e]
005B352A  8B 0D 50 40 99 00               mov ecx, dword ptr [rip + 0x994050]
005B3530  E8 EB FA FD FF                  call 0x140593020
005B3535  41 8B CD                        mov ecx, r13d
005B3538  E8 D3 F8 FD FF                  call 0x140592e10
005B353D  8A CB                           mov cl, bl
005B353F  E8 A0 0A 00 00                  call 0x1405b3fe4
005B3544  41 39 BE 44 8A 00 00            cmp dword ptr [r14 + 0x8a44], edi
005B354B  74 4E                           je 0x1405b359b
005B354D  40 38 3D 99 35 A1 00            cmp byte ptr [rip + 0xa13599], dil
005B3554  74 0C                           je 0x1405b3562
005B3556  33 D2                           xor edx, edx
005B3558  49 8B CE                        mov rcx, r14
005B355B  E8 40 9B 02 00                  call 0x1405dd0a0
005B3560  EB 39                           jmp 0x1405b359b
005B3562  40 38 3D 73 35 A1 00            cmp byte ptr [rip + 0xa13573], dil
005B3569  74 30                           je 0x1405b359b
005B356B  49 8B 86 B0 89 00 00            mov rax, qword ptr [r14 + 0x89b0]
005B3572  48 85 C0                        test rax, rax
005B3575  74 24                           je 0x1405b359b
005B3577  49 8B 8E B8 89 00 00            mov rcx, qword ptr [r14 + 0x89b8]
005B357E  48 8D 90 28 03 00 00            lea rdx, [rax + 0x328]
005B3585  48 8B 80 88 01 00 00            mov rax, qword ptr [rax + 0x188]
005B358C  45 8A CD                        mov r9b, r13b
005B358F  45 8A C5                        mov r8b, r13b
005B3592  48 8B 49 08                     mov rcx, qword ptr [rcx + 8]
005B3596  E8 35 75 10 00                  call 0x1406baad0
005B359B  40 84 F6                        test sil, sil
005B359E  75 2E                           jne 0x1405b35ce
005B35A0  8B 4D 90                        mov ecx, dword ptr [rbp - 0x70]
005B35A3  84 DB                           test bl, bl
005B35A5  74 03                           je 0x1405b35aa
005B35A7  83 C9 04                        or ecx, 4
005B35AA  8B C1                           mov eax, ecx
005B35AC  83 C8 02                        or eax, 2
005B35AF  40 38 7C 24 68                  cmp byte ptr [rsp + 0x68], dil
005B35B4  40 8A 7C 24 59                  mov dil, byte ptr [rsp + 0x59]
005B35B9  0F 45 C1                        cmovne eax, ecx
005B35BC  8B C8                           mov ecx, eax
005B35BE  41 0B CD                        or ecx, r13d
005B35C1  40 84 FF                        test dil, dil
005B35C4  0F 45 C8                        cmovne ecx, eax
005B35C7  E8 80 13 00 00                  call 0x1405b494c
005B35CC  EB 05                           jmp 0x1405b35d3
005B35CE  40 8A 7C 24 59                  mov dil, byte ptr [rsp + 0x59]
005B35D3  41 8A CD                        mov cl, r13b
005B35D6  E8 A9 59 FD FF                  call 0x140588f84
005B35DB  40 84 F6                        test sil, sil
005B35DE  75 42                           jne 0x1405b3622
005B35E0  B9 02 00 00 00                  mov ecx, 2
005B35E5  E8 26 F8 FD FF                  call 0x140592e10
005B35EA  45 33 C0                        xor r8d, r8d
005B35ED  33 D2                           xor edx, edx
005B35EF  41 8B CD                        mov ecx, r13d
005B35F2  E8 A9 1B 00 00                  call 0x1405b51a0
005B35F7  33 D2                           xor edx, edx
005B35F9  45 33 C0                        xor r8d, r8d
005B35FC  8D 4A 08                        lea ecx, [rdx + 8]
005B35FF  E8 9C 1B 00 00                  call 0x1405b51a0
005B3604  33 D2                           xor edx, edx
005B3606  45 33 C0                        xor r8d, r8d
005B3609  8D 5A 09                        lea ebx, [rdx + 9]
005B360C  8B CB                           mov ecx, ebx
005B360E  E8 8D 1B 00 00                  call 0x1405b51a0
005B3613  8D 4B FC                        lea ecx, [rbx - 4]
005B3616  E8 F5 F7 FD FF                  call 0x140592e10
005B361B  E8 68 19 00 00                  call 0x1405b4f88
005B3620  EB 05                           jmp 0x1405b3627
005B3622  BB 09 00 00 00                  mov ebx, 9
005B3627  80 3D CA 3F 99 00 00            cmp byte ptr [rip + 0x993fca], 0
005B362E  75 10                           jne 0x1405b3640
005B3630  80 3D E5 73 85 00 00            cmp byte ptr [rip + 0x8573e5], 0
005B3637  75 07                           jne 0x1405b3640
005B3639  33 C9                           xor ecx, ecx
005B363B  E8 3C D4 FF FF                  call 0x1405b0a7c
005B3640  49 8B 86 C0 8F 00 00            mov rax, qword ptr [r14 + 0x8fc0]
005B3647  48 8D 8D F0 00 00 00            lea rcx, [rbp + 0xf0]
005B364E  BA 80 00 00 00                  mov edx, 0x80
005B3653  0F 10 01                        movups xmm0, xmmword ptr [rcx]
005B3656  0F 11 00                        movups xmmword ptr [rax], xmm0
005B3659  0F 10 49 10                     movups xmm1, xmmword ptr [rcx + 0x10]
005B365D  0F 11 48 10                     movups xmmword ptr [rax + 0x10], xmm1
005B3661  0F 10 41 20                     movups xmm0, xmmword ptr [rcx + 0x20]
005B3665  0F 11 40 20                     movups xmmword ptr [rax + 0x20], xmm0
005B3669  0F 10 49 30                     movups xmm1, xmmword ptr [rcx + 0x30]
005B366D  0F 11 48 30                     movups xmmword ptr [rax + 0x30], xmm1
005B3671  0F 10 41 40                     movups xmm0, xmmword ptr [rcx + 0x40]
005B3675  0F 11 40 40                     movups xmmword ptr [rax + 0x40], xmm0
005B3679  0F 10 49 50                     movups xmm1, xmmword ptr [rcx + 0x50]
005B367D  0F 11 48 50                     movups xmmword ptr [rax + 0x50], xmm1
005B3681  0F 10 41 60                     movups xmm0, xmmword ptr [rcx + 0x60]
005B3685  0F 11 40 60                     movups xmmword ptr [rax + 0x60], xmm0
005B3689  48 03 C2                        add rax, rdx
005B368C  0F 10 49 70                     movups xmm1, xmmword ptr [rcx + 0x70]
005B3690  48 03 CA                        add rcx, rdx
005B3693  0F 11 48 F0                     movups xmmword ptr [rax - 0x10], xmm1
005B3697  48 83 EB 01                     sub rbx, 1
005B369B  75 B6                           jne 0x1405b3653
005B369D  0F 10 01                        movups xmm0, xmmword ptr [rcx]
005B36A0  0F 11 00                        movups xmmword ptr [rax], xmm0
005B36A3  0F 10 49 10                     movups xmm1, xmmword ptr [rcx + 0x10]
005B36A7  0F 11 48 10                     movups xmmword ptr [rax + 0x10], xmm1
005B36AB  0F 10 41 20                     movups xmm0, xmmword ptr [rcx + 0x20]
005B36AF  0F 11 40 20                     movups xmmword ptr [rax + 0x20], xmm0
005B36B3  0F 10 49 30                     movups xmm1, xmmword ptr [rcx + 0x30]
005B36B7  0F 11 48 30                     movups xmmword ptr [rax + 0x30], xmm1
005B36BB  0F 10 41 40                     movups xmm0, xmmword ptr [rcx + 0x40]
005B36BF  0F 11 40 40                     movups xmmword ptr [rax + 0x40], xmm0
005B36C3  45 84 FF                        test r15b, r15b
005B36C6  74 4E                           je 0x1405b3716
005B36C8  E8 DB CE FF FF                  call 0x1405b05a8
005B36CD  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
005B36D1  4C 8D 95 F0 00 00 00            lea r10, [rbp + 0xf0]
005B36D8  8B 4C 24 54                     mov ecx, dword ptr [rsp + 0x54]
005B36DC  48 89 05 2D FE 96 00            mov qword ptr [rip + 0x96fe2d], rax
005B36E3  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
005B36E8  88 0D 32 FE 96 00               mov byte ptr [rip + 0x96fe32], cl
005B36EE  48 8D 0D 0B FE 96 00            lea rcx, [rip + 0x96fe0b]
005B36F5  48 89 05 1C FE 96 00            mov qword ptr [rip + 0x96fe1c], rax
005B36FC  4C 89 15 FD FD 96 00            mov qword ptr [rip + 0x96fdfd], r10
005B3703  4C 89 25 FE FD 96 00            mov qword ptr [rip + 0x96fdfe], r12
005B370A  40 88 35 10 FE 96 00            mov byte ptr [rip + 0x96fe10], sil
005B3711  E8 32 0A 00 00                  call 0x1405b4148
005B3716  33 C9                           xor ecx, ecx
005B3718  E8 C3 5C FD FF                  call 0x1405893e0
005B371D  B9 63 00 00 00                  mov ecx, 0x63
005B3722  E8 E9 F6 FD FF                  call 0x140592e10
005B3727  40 84 F6                        test sil, sil
005B372A  75 05                           jne 0x1405b3731
005B372C  E8 33 1D 00 00                  call 0x1405b5464
005B3731  48 8B 05 E0 D3 84 00            mov rax, qword ptr [rip + 0x84d3e0]
005B3738  E8 93 73 10 00                  call 0x1406baad0
005B373D  B9 04 00 00 00                  mov ecx, 4
005B3742  E8 C9 F6 FD FF                  call 0x140592e10
005B3747  80 7C 24 68 00                  cmp byte ptr [rsp + 0x68], 0
005B374C  74 55                           je 0x1405b37a3
005B374E  33 C9                           xor ecx, ecx
005B3750  44 88 2D 39 31 8B 00            mov byte ptr [rip + 0x8b3139], r13b
005B3757  E8 A4 F0 F2 FF                  call 0x1404e2800
005B375C  E8 53 0A 00 00                  call 0x1405b41b4
005B3761  48 8B 05 A0 D3 84 00            mov rax, qword ptr [rip + 0x84d3a0]
005B3768  33 C9                           xor ecx, ecx
005B376A  E8 61 73 10 00                  call 0x1406baad0
005B376F  80 3D AA 85 95 00 00            cmp byte ptr [rip + 0x9585aa], 0
005B3776  74 09                           je 0x1405b3781
005B3778  80 3D A2 85 95 00 00            cmp byte ptr [rip + 0x9585a2], 0
005B377F  74 1A                           je 0x1405b379b
005B3781  80 3D 9A 85 95 00 00            cmp byte ptr [rip + 0x95859a], 0
005B3788  75 11                           jne 0x1405b379b
005B378A  80 7C 24 7A 00                  cmp byte ptr [rsp + 0x7a], 0
005B378F  75 0A                           jne 0x1405b379b
005B3791  B9 03 00 00 00                  mov ecx, 3
005B3796  40 84 FF                        test dil, dil
005B3799  75 03                           jne 0x1405b379e
005B379B  41 8B CD                        mov ecx, r13d
005B379E  E8 AD 2D F9 FF                  call 0x140546550
005B37A3  B9 04 00 00 00                  mov ecx, 4
005B37A8  E8 13 06 00 00                  call 0x1405b3dc0
005B37AD  48 81 C4 48 07 00 00            add rsp, 0x748
005B37B4  41 5F                           pop r15
005B37B6  41 5E                           pop r14
005B37B8  41 5D                           pop r13
005B37BA  41 5C                           pop r12
005B37BC  5F                              pop rdi
005B37BD  5E                              pop rsi
005B37BE  5B                              pop rbx
005B37BF  5D                              pop rbp
005B37C0  C3                              ret
005B37C1  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KeBugCheck2(int a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m598;
    unsigned __int64 v_stack_m688;
    unsigned __int64 v_stack_m6A0;
    unsigned __int16 v_stack_m6A6;
    unsigned __int64 v_stack_m6A8;
    unsigned __int64 v_stack_m6B8;
    unsigned __int64 v_stack_m6C0;
    unsigned __int64 v_stack_m6C8;
    unsigned __int64 v_stack_m6D0;
    unsigned __int64 v_stack_m6D8;
    unsigned int v_stack_m6E0;
    unsigned __int64 v_stack_m6E8;
    unsigned __int64 v_stack_m6F0;
    unsigned int v_stack_m6F8;
    unsigned __int64 v_stack_m700;
    unsigned int v_stack_m708;
    unsigned __int8 v_stack_m70E;
    unsigned __int8 v_stack_m70F;
    unsigned __int8 v_stack_m710;
    unsigned __int64 v_stack_m718;
    unsigned __int8 v_stack_m720;
    unsigned __int64 v_stack_m728;
    unsigned __int8 v_stack_m72E;
    unsigned __int8 v_stack_m72F;
    unsigned __int8 v_stack_m730;
    unsigned __int8 v_stack_m734;
    unsigned __int8 v_stack_m738;
    unsigned __int64 v_stack_m740;
    unsigned __int8 v_stack_m748;
    unsigned __int64 v_stack_m750;
    unsigned __int64 v_stack_m758;
    unsigned int v_stack_m760;
    unsigned __int64 v_stack_m768;
    unsigned __int8 v_stack_mC8;

    v_rsp = (v_rsp) - (0x748ULL);
    v_stack_m6D0 = a3;
    a2 = 0;
    v_stack_m708 = a1;
    v_stack_m728 = a6;
    result = memset(v_stack_m6A8, a2, 264, a4);
    v_r14 = 0;
    v_stack_m72F = 1;
    v_stack_mC8 = 0;
    v_stack_m6E8 = *(unsigned __int64 *)(gs_base + (0 + 392));
    v_stack_m6D8 = v_rip + 5702;
    v_stack_m6F0 = 0;
    v_stack_m72E = 0;
    v_stack_m700 = 0;
    v_stack_m734 = 0;
    v_stack_m710 = 0;
    v_stack_m70E = 0;
    v_stack_m6B8 = 0;
    v_stack_m718 = 0;
    v_stack_m738 = 1;
    v_stack_m70F = 0;
    v_stack_m6F8 = 0;
    if ((unsigned int)(v_r14 + 1) != 0) goto loc_005B28C9;
    result = (unsigned int)(v_stack_m708);
    if (((unsigned int)((unsigned int)(v_stack_m708))) == 0xC00002D1ULL) {
        result = 195;
        v_stack_m708 = (unsigned int)(result);
    }
    *(unsigned __int64 *)(v_rip + 10046675) = result;
    *(unsigned __int64 *)(v_rip + 10046676) = 0;
    *(unsigned __int64 *)(v_rip + 10046677) = a3;
    *(unsigned __int64 *)(v_rip + 10046678) = a4;
    *(unsigned __int64 *)(v_rip + 10046679) = a5;
loc_005B28C9:
    a3 = 0;
    result = IoNotifyDumpEx((unsigned int)((unsigned int)(a3 + 4)), a2, a3, a4);
    result = (unsigned int)(*(unsigned int *)(v_rip + 10568115));
    if ((((unsigned __int8)(a3 + 4 - 2)) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 10568115))))) != 0) {
        a1 = (unsigned int)(a3 + 4);
        result = HvlNotifyRootCrashdump(a1, a2, a3, a4);
    }
    v_stack_m6C8 = 0;
    v_stack_m6C0 = 0;
    v_stack_m6E0 = 0;
    if (((unsigned __int8)(v_cr8)) >= ((unsigned __int8)(a3 + 4 - 2))) goto loc_005B291A;
    result = v_cr8;
    if ((*(unsigned int *)(v_rip + 10568720)) != 0) {
        a2 = (unsigned __int8)(a3 + 4 - 2);
        result = KiRaiseIrqlProcessIrqlFlags(v_cr8, a2, a3, a4);
    }
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 40)) != 0) goto loc_005B2974;
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36))) << (4));
    a2 = (unsigned int)((a2) | (3));
loc_005B2946:
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10046479))))) & (3));
    if (((unsigned __int8)(a1)) == 3) goto loc_005B2965;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10046479)))) != ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10046479))))))) goto loc_005B2946;
    v_stack_m730 = 1;
    goto loc_005B296A;
loc_005B2965:
    v_stack_m730 = 0;
loc_005B296A:
    goto loc_005B2AEA;
loc_005B2974:
    result = KeQueryCurrentStackInformation(v_stack_m6E0, v_stack_m6C0, v_stack_m6C8, a4);
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36))) << (4));
    a2 = (unsigned int)((a2) | (3));
loc_005B299F:
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10046390))))) & (3));
    if (((unsigned __int8)(a1)) == 3) goto loc_005B2ADD;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10046390)))) != ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10046390))))))) goto loc_005B299F;
    a3 = 0;
    result = IoNotifyDumpEx(a3 + 6, a2, a3, a4);
    if ((unsigned __int8)((unsigned __int8)(result)) == 0) goto loc_005B2A5C;
    if (((unsigned int)((unsigned int)(v_stack_m6E0))) > 9) goto loc_005B29E1;
    if (((unsigned int)((unsigned int)(v_stack_m6E0))) < 9) goto loc_005B2A5C;
loc_005B29E1:
    result = (v_stack_m6C8) - (v_stack_m6C0);
    if (result > ((unsigned int)(0x24000ULL))) goto loc_005B2A01;
    if (result == 0) goto loc_005B2A47;
loc_005B2A01:
    v_rsi = (v_rip + 9898808) - (v_stack_m6C0);
    v_rdi = (result) - 1;
    v_rdi = (v_rdi) >> (12);
    v_rdi = (v_rdi) + 1;
loc_005B2A15:
    a2 = 0;
    result = MmIsAddressValidEx(v_stack_m6C0, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_005B2A37;
    result = memcpy(v_stack_m6C0 + v_rsi * 1, v_stack_m6C0, (unsigned int)(0x1000ULL), a4);
    goto loc_005B2A3A;
loc_005B2A37:
    v_r14 = 0;
loc_005B2A3A:
    v_rbx = (v_stack_m6C0) + (0x1000ULL);
    v_rdi = (v_rdi) - (1);
    if (condition_is_not_equal) goto loc_005B2A15;
loc_005B2A47:
    result = IoNotifyDumpEx(7, v_stack_m6C0, 0, a4);
    v_r14 = 0;
loc_005B2A5C:
    if ((*(unsigned __int8 *)(v_rip + 12905950)) == 0) goto loc_005B2ACE;
    a3 = 0;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1056)) & (0xFFFFFFFFFFFFF000ULL);
    a1 = (a1) + (0x1000ULL);
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1048)) - (0x1000ULL);
    if (0 <= a1) goto loc_005B2ACE;
    if (0 >= a2) goto loc_005B2AD3;
    a2 = a3 - 256;
    if ((a3 - 256) < a1) { a2 = a1; }
    a3 = (a3) - (a2);
    if (a3 > 256) { a3 = 256; }
    result = memcpy(v_rip + 10573315, a2, a3, a4);
    goto loc_005B2AD3;
loc_005B2ACE:
loc_005B2AD3:
    v_stack_m730 = 1;
    goto loc_005B2AEA;
loc_005B2ADD:
    v_stack_m730 = 0;
loc_005B2AEA:
    result = DbgPrintEx(2 + 3, 2, v_rip + 1149878, 0);
    if (0 == 0) goto loc_005B2B18;
    if (!(condition_is_greater)) {
        *(unsigned __int8 *)(v_rip + 10046000) = 1;
    }
    if ((*(unsigned int *)(v_rip + 10567889)) != 0) {
    }
    a2 = (*(unsigned __int64 *)(v_rip + 10567980)) | (256);
    v_stack_m6D0 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36)));
    result = KeSaveSupervisorState(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 1728), a2, v_rip + 1149878, 0);
    if (*(unsigned __int64 *)(v_rip + 9802303) != 0) goto loc_005B2B5E;
loc_005B2B59:
    v_rsi = 0;
    goto loc_005B2BAB;
loc_005B2B5E:
    if ((*(unsigned int *)(v_rip + 9803643)) != 0) {
        *(unsigned __int8 *)(v_rip + 9802162) = 0;
    }
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 9802303) + 2)) == 0) goto loc_005B2B59;
    if (0 == 0) goto loc_005B2BA3;
    a2 = 0;
    result = DbgPrintEx(a2 + 101, a2, v_rip + 1151982, 0);
    if (((unsigned int)((unsigned int)(v_stack_m708))) == 10) {
        a3 = v_rip + 1152154;
        a2 = 0;
        a1 = (unsigned int)(v_stack_m708) + 91;
        result = DbgPrintEx(a1, a2, a3, 0);
    }
loc_005B2BA3:
loc_005B2BAB:
loc_005B2BC2:
    *(unsigned __int64 *)(v_stack_m598) = v_xmm0;
    *(unsigned __int64 *)(v_stack_m598 + 16) = v_xmm1;
    *(unsigned __int64 *)(v_stack_m598 + 32) = v_xmm0;
    *(unsigned __int64 *)(v_stack_m598 + 48) = v_xmm1;
    *(unsigned __int64 *)(v_stack_m598 + 64) = v_xmm0;
    *(unsigned __int64 *)(v_stack_m598 + 80) = v_xmm1;
    *(unsigned __int64 *)(v_stack_m598 + 96) = v_xmm0;
    a1 = (v_stack_m598) + (9 + 119);
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36800)) + (9 + 119);
    *(unsigned __int64 *)(a1 - 16) = v_xmm1;
    a2 = (9) - (1);
    if (condition_is_not_equal) goto loc_005B2BC2;
    *(unsigned __int64 *)(a1) = v_xmm0;
    *(unsigned __int64 *)(a1 + 16) = v_xmm1;
    *(unsigned __int64 *)(a1 + 32) = v_xmm0;
    *(unsigned __int64 *)(a1 + 48) = v_xmm1;
    *(unsigned __int64 *)(a1 + 64) = v_xmm0;
    if (v_stack_m730 == ((unsigned __int8)(a2))) goto loc_005B3300;
    v_rbx = (unsigned int)(v_stack_m708);
    if ((*(unsigned int *)(v_rip + 9772354)) != ((unsigned int)(a2))) {
        a1 = a2 + 2;
        result = VfNotifyVerifierOfEvent(a1, a2, 9 + 119, 0);
        v_rbx = v_stack_m708;
    }
    if (((unsigned int)(v_rbx)) == 229) {
        result = KiScanBugCheckCallbackList(a1, a2, 9 + 119, 0);
        result = *(unsigned __int64 *)(v_rip + 8707749);
        a1 = 0;
        result = guard_dispatch_icall(a1, a2, 9 + 119, 0);
        a1 = 3;
        result = HalReturnToFirmware(a1, a2, 9 + 119, 0);
        v_rbx = v_stack_m708;
    }
    if (((unsigned int)(v_rbx)) > 209) goto loc_005B2F5A;
    if (((unsigned int)(v_rbx)) == 209) goto loc_005B2E36;
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) - (10));
    if (condition_is_equal) goto loc_005B2E36;
    result = (unsigned int)((result) - (49));
    if (condition_is_equal) goto loc_005B2E2D;
    result = (unsigned int)((result) - (17));
    if (condition_is_equal) goto loc_005B2DE5;
    result = (unsigned int)((result) - (4));
    if (condition_is_equal) goto loc_005B2D69;
    result = (unsigned int)((result) - (43));
    if (condition_is_equal) goto loc_005B2D46;
    result = (unsigned int)((result) - (19));
    if (condition_is_equal) goto loc_005B3053;
    result = (unsigned int)((result) - (18));
    if (condition_is_equal) goto loc_005B2D10;
    result = (unsigned int)((result) - (30));
    if (condition_is_equal) goto loc_005B3053;
    if (((unsigned int)(result)) != 13) goto loc_005B2FA3;
    v_stack_m700 = a2;
loc_005B2CDC:
loc_005B2CE1:
loc_005B2CE5:
loc_005B2CEA:
loc_005B2CEF:
    if (*(unsigned __int64 *)(v_rip + 9124586) == 0) goto loc_005B30BE;
    result = KiBugCheckUnicodeToAnsi(*(unsigned __int64 *)(v_rip + 9124586), v_stack_mC8, 9 + 119, 0);
    goto loc_005B30DE;
loc_005B2D10:
    if (((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1532)) & (0x1000ULL)) != 0) goto loc_005B2CDC;
    if ((v_stack_m738 - 240) > 1) goto loc_005B2CE1;
    v_stack_m734 = 1;
    goto loc_005B2CE5;
loc_005B2D46:
    v_r15 = (unsigned __int8)(((unsigned __int8)(a4)) >> (1));
    result = (unsigned __int8)(~((unsigned __int8)(a4)));
    result = (unsigned __int8)((result) & (1));
    v_r15 = (unsigned __int8)(~(v_r15));
    v_stack_m72F = (unsigned __int8)(result);
    v_r15 = (unsigned __int8)((v_r15) & (1));
    goto loc_005B2CEA;
loc_005B2D69:
    if (v_stack_m728 != 0) goto loc_005B2D81;
    if (a4 == 0) goto loc_005B2DB2;
    if ((((unsigned __int8)(a4)) & (3)) != 0) goto loc_005B2DB2;
loc_005B2D81:
    a3 = 0;
    v_stack_m700 = *(unsigned __int64 *)(a4 + 360);
    *(unsigned __int64 *)(v_rip + 10045433) = *(unsigned __int64 *)(a4 + 360);
    result = KiPcToFileHeader(*(unsigned __int64 *)(a4 + 360), v_stack_m6F0, a3, v_stack_m72E);
    v_stack_m728 = a4;
    if (result != 0) goto loc_005B2CE1;
loc_005B2DB2:
    result = MmLocateUnloadedDriver(v_r15, v_stack_m6F0, a3, v_stack_m72E);
    if (result == 0) goto loc_005B2CE1;
    v_r15 = (unsigned int)((v_r15) - (*(unsigned int *)(result + 16)));
    *(unsigned int *)(v_rip + 9124386) = (unsigned int)(v_r15);
    *(unsigned __int64 *)(v_rip + 9124363) = result;
    *(unsigned __int64 *)(v_rip + 10045344) = 206;
    goto loc_005B2CE1;
loc_005B2DE5:
    v_stack_m734 = 1;
    v_stack_m710 = 1;
    *(unsigned __int64 *)(v_rip + 10045305) = (unsigned int)((unsigned int)(v_r15));
    v_rdi = (a4) - (v_rip + 10045335);
    v_stack_m6B8 = a4;
loc_005B2E0E:
    *(unsigned __int64 *)(v_rip + 10045335) = *(unsigned __int64 *)(v_rdi + v_rip + 10045335 * 1);
    a1 = (v_rip + 10045335) + (8);
    if (a1 < (v_rip + 10045352)) goto loc_005B2E0E;
loc_005B2E23:
    goto loc_005B2CEF;
loc_005B2E2D:
    v_stack_m700 = v_stack_m718;
    goto loc_005B2CDC;
loc_005B2E36:
    v_stack_m700 = v_stack_m718;
    if (v_stack_m718 < (*(unsigned __int64 *)(v_rip + 9709147))) goto loc_005B2E5C;
    if (v_stack_m718 >= (*(unsigned __int64 *)(v_rip + 9709142))) goto loc_005B2E5C;
    *(unsigned __int64 *)(v_rip + 10045225) = 197;
    goto loc_005B2CDC;
loc_005B2E5C:
    a3 = 0;
    result = KiPcToFileHeader(v_stack_m718, v_stack_m6F0, a3, v_stack_m72E);
    if (v_stack_m72E != 1) goto loc_005B2F1A;
    v_r13 = (unsigned int)((v_stack_m718) - ((unsigned int)(result)));
    result = (v_stack_m6F0) + (88);
    *(unsigned int *)(v_rip + 9124186) = (unsigned int)(v_r13);
    *(unsigned __int64 *)(v_rip + 9124157) = result;
    result = KiPcToFileHeader(v_stack_m738, v_stack_m6F0, 1, v_stack_m72E);
    if (result == 0) goto loc_005B2ED9;
    v_r15 = (unsigned int)((v_stack_m738) - ((unsigned int)(result)));
    *(unsigned __int64 *)(v_rip + 10045122) = 211;
    result = (v_stack_m6F0) + (88);
    *(unsigned int *)(v_rip + 9124131) = (unsigned int)(v_r15);
    *(unsigned __int64 *)(v_rip + 9124108) = result;
    goto loc_005B2CDC;
loc_005B2ED9:
    result = MmLocateUnloadedDriver(v_r15, v_stack_m6F0, 1, v_stack_m72E);
    if (result == 0) goto loc_005B2E23;
    v_r15 = (unsigned int)((v_r15) - (*(unsigned int *)(result + 16)));
    *(unsigned int *)(v_rip + 9124077) = (unsigned int)(v_r15);
    *(unsigned __int64 *)(v_rip + 9124054) = result;
    *(unsigned __int64 *)(v_rip + 10045035) = 212;
    goto loc_005B2E23;
loc_005B2F1A:
    *(unsigned __int64 *)(v_rip + 10045005) = 209;
    if (result == 0) goto loc_005B2CEA;
    v_r13 = (unsigned int)((v_stack_m718) - ((unsigned int)(result)));
    result = (v_stack_m6F0) + (88);
    *(unsigned int *)(v_rip + 9124002) = (unsigned int)(v_r13);
    *(unsigned __int64 *)(v_rip + 9123979) = result;
    goto loc_005B2CEA;
loc_005B2F5A:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m734)))) - (216));
    if (condition_is_equal) goto loc_005B30AE;
    result = (unsigned int)((result) - (14));
    if (condition_is_equal) goto loc_005B3093;
    result = (unsigned int)((result) - (4));
    if (condition_is_equal) goto loc_005B3087;
    result = (unsigned int)((result) - (5));
    if (condition_is_equal) goto loc_005B3083;
    result = (unsigned int)((result) - (13));
    if (condition_is_equal) goto loc_005B3053;
    result = (unsigned int)((result) - (61));
    if (condition_is_equal) goto loc_005B3024;
    result = (unsigned int)((result) - (4));
    if (condition_is_equal) goto loc_005B3018;
    result = (unsigned int)((result) - (18));
    if (condition_is_equal) goto loc_005B2FCB;
    if (((unsigned int)(result)) == 121) goto loc_005B2FC1;
loc_005B2FA3:
loc_005B2FAB:
    if (v_stack_m728 == 0) goto loc_005B2CE1;
    v_stack_m700 = *(unsigned __int64 *)(v_stack_m728 + 360);
    goto loc_005B2CE1;
loc_005B2FC1:
    v_stack_m70E = 1;
    goto loc_005B2CDC;
loc_005B2FCB:
    if (v_stack_m728 >= 256) goto loc_005B2FEC;
    result = *(unsigned __int64 *)(v_stack_m728 + 360);
    if (v_r13 != 0) {
        result = *(unsigned __int64 *)(v_r13 + 8);
        a1 = v_stack_m6E8;
        if (result != 0) { a1 = result; }
        v_stack_m6E8 = a1;
    }
    v_rbx = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1532))) >> (12));
    v_rbx = (unsigned __int8)(~(v_rbx));
    v_rbx = (unsigned __int8)((v_rbx) & (1));
loc_005B300A:
    v_stack_m734 = (unsigned int)(v_rbx);
loc_005B300E:
    goto loc_005B2CE5;
loc_005B3018:
    v_stack_m6F8 = 8;
    goto loc_005B2CDC;
loc_005B3024:
    if (v_stack_m728 == 0) goto loc_005B3045;
    v_stack_m700 = *(unsigned __int64 *)(v_stack_m728 + 360);
    goto loc_005B2CE5;
loc_005B3045:
    v_rdi = v_stack_m728;
    if (v_stack_m738 == 10) { v_rdi = v_r13; }
    v_stack_m700 = v_rdi;
    goto loc_005B300E;
loc_005B3053:
    if (v_stack_m728 != 0) goto loc_005B3078;
    if (a4 == 0) goto loc_005B2CE1;
    if ((((unsigned __int8)(a4)) & (3)) != 0) goto loc_005B2CE1;
    v_stack_m728 = a4;
loc_005B3078:
    goto loc_005B2FAB;
loc_005B3083:
    goto loc_005B300A;
loc_005B3087:
    *(unsigned __int64 *)(v_rip + 9123666) = a4;
    goto loc_005B2CDC;
loc_005B3093:
    if (((unsigned int)(v_stack_m738)) != 39) goto loc_005B2CDC;
    result = IoAddTriageDumpDataBlock(a4, v_stack_m738 - 31, 1, v_stack_m72E);
    goto loc_005B2CDC;
loc_005B30AE:
    *(unsigned __int64 *)(v_rip + 9123623) = v_stack_m738 + 88;
    goto loc_005B2CDC;
loc_005B30BE:
    result = v_stack_m738 + 88;
    if (v_stack_m700 != 0) {
        a4 = 1;
        a2 = v_stack_m700;
        a3 = 1;
        a1 = v_stack_mC8;
        result = KiDumpParameterImages(a1, a2, a3, a4);
    }
    if ((*(unsigned int *)(v_rip + 9727515)) != 0) goto loc_005B3101;
    result = WheapSelLogSetNtSchedulerAvailabilityNoLock(a1, a2, a3, a4);
    result = IpmiHwContextInitialized(v_rip + 9727885, a2, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        result = IpmiLibAddSelBugcheckRecord(v_rip + 9727885, a2, a3, a4);
    }
    result = 0;
    result = (((unsigned int)(*(unsigned __int64 *)(v_rip + 10044536))) != 265) ? 1 : 0;
    *(unsigned int *)(v_rip + 9121211) = (unsigned int)(result);
    if ((unsigned __int8)(v_stack_m738) != 0) {
        a2 = 1;
        result = KiCollectTriageDumpDataBlocks(*(unsigned __int64 *)(v_rip + 10044536), a2, a3, a4);
    }
    if (v_stack_m720 == 0) goto loc_005B3174;
    result = (unsigned int)(*(unsigned int *)(v_rip + 8747133));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 8747133)))) & (4)) != 0) {
        result = v_stack_m598;
        *(unsigned __int64 *)(v_rip + 9896895) = v_stack_m6E8;
        *(unsigned __int64 *)(v_rip + 9896880) = result;
        result = v_stack_m6D8;
        *(unsigned __int64 *)(v_rip + 9896885) = result;
        *(unsigned __int64 *)(v_rip + 9896886) = a4;
        *(unsigned __int8 *)(v_rip + 9896888) = 1;
        *(unsigned __int8 *)(v_rip + 9896882) = 1;
        result = KiAttemptBugcheckRecovery(*(unsigned __int64 *)(v_rip + 10044536), a2, a3, a4);
    }
    *(unsigned __int8 *)(v_rip + 10044358) = 1;
    result = guard_dispatch_icall(*(unsigned __int64 *)(v_rip + 10044536), a2, a3, a4);
    result = IoSaveBugCheckProgress(96, a2, a3, a4);
    result = KeIsEmptyAffinityEx(v_rip + 8747198, a2, a3, a4);
    v_rdi = 0;
    a1 = ((unsigned int)(result) == 0) ? 1 : 0;
    result = guard_dispatch_icall(a1, a2, a3, a4);
    result = KiFilterBugCheckInfo(v_stack_m708, v_rip + 10044349, a3, a4);
    if ((*(unsigned __int64 *)(v_rip + 9121405)) == 0) goto loc_005B31DA;
    if ((unsigned __int8)(v_stack_m738) != 0) goto loc_005B31DE;
loc_005B31DA:
    goto loc_005B31E1;
loc_005B31DE:
loc_005B31E1:
    v_stack_m760 = 0;
    v_stack_m768 = *(unsigned __int64 *)(v_rip + 10044310);
    result = HvlLogGuestCrashInformation((unsigned int)(*(unsigned int *)(v_rip + 10044292)), *(unsigned __int64 *)(v_rip + 10044306), *(unsigned __int64 *)(v_rip + 10044321), *(unsigned __int64 *)(v_rip + 10044336));
    if ((*(unsigned __int8 *)(v_rip + 8747009)) == 0) {
        result = v_stack_m598;
        *(unsigned __int64 *)(v_rip + 8707677) = result;
    }
    a2 = 0;
    result = KiBugCheckShouldEnterPostBugCheckDebugger((unsigned int)(v_stack_m708), a2, *(unsigned __int64 *)(v_rip + 10044321), *(unsigned __int64 *)(v_rip + 10044336));
    if ((unsigned __int8)(result) == 0) goto loc_005B330F;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 33702)) != 0) goto loc_005B32E2;
    a2 = 0;
    v_stack_m750 = *(unsigned __int64 *)(v_rip + 10044239);
    v_stack_m758 = *(unsigned __int64 *)(v_rip + 10044203);
    v_stack_m760 = *(unsigned __int64 *)(v_rip + 10044183);
    v_stack_m768 = *(unsigned __int64 *)(v_rip + 10044160);
    result = DbgPrintEx(a2 + 101, a2, v_rip + 1148120, (unsigned int)(*(unsigned int *)(v_rip + 10044193)));
    if ((*(unsigned __int64 *)(v_rip + 9123143)) != 0) {
        a2 = 0;
        a4 = v_stack_mC8;
        a3 = v_rip + 1148005;
        a1 = a2 + 101;
        result = DbgPrintEx(a1, a2, a3, a4);
    }
    if (v_stack_m710 == 0) goto loc_005B32E2;
    result = v_stack_m6B8;
    if (v_stack_m6B8 != 0) {
        a2 = 0;
        a3 = v_stack_m6B8;
        a1 = a2 + 101;
        result = DbgPrintEx(a1, a2, a3, a4);
    }
    if (v_r13 != 0) {
        a2 = 0;
        a3 = v_r13;
        a1 = a2 + 101;
        result = DbgPrintEx(a1, a2, a3, a4);
    }
    if ((*(unsigned __int8 *)(v_rip + 10044175)) == 0) goto loc_005B330F;
    if ((*(unsigned __int8 *)(v_rip + 10044138)) != 0) goto loc_005B330F;
    result = KiBugCheckDebugBreak(3, a2, a3, a4);
    goto loc_005B330F;
loc_005B3300:
    v_rdi = 0;
loc_005B330F:
    if ((*(unsigned int *)(v_rip + 10566141)) != 0) {
        result = KiRaiseIrqlProcessIrqlFlags(a3 + 4 - 2, 15, a3, a4);
    }
    if (v_stack_m730 != 0) goto loc_005B34B2;
    result = KiHandleMultipleBugchecksDuringRecovery((unsigned int)(*(unsigned int *)(v_rip + 10043921)), 15, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_005B3356;
    *(unsigned __int8 *)(v_rip + 10043895) = 1;
    goto loc_005B34B8;
loc_005B3356:
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10043888))))) >> (4));
    result = (unsigned int)(*(unsigned int *)(v_rip + 10043888));
    if (((unsigned int)((unsigned int)(v_stack_m6D0))) != a1) {
        result = KiYieldWaitForDebugger(a1, 15, a3, (unsigned int)(v_stack_m6D0));
    }
    if ((*(unsigned __int8 *)(v_rip + 9122929)) != 0) goto loc_005B3490;
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)(result))) >> (2));
    v_rbx = (unsigned int)((v_rbx) & (3));
    if (((unsigned int)(v_rbx)) >= 2) goto loc_005B3490;
    v_stack_m758 = a1;
    v_stack_m760 = (unsigned int)(v_rbx);
    result = (unsigned int)((result) & (3));
    v_stack_m768 = (unsigned int)(result);
    result = DbgPrintEx((unsigned int)((unsigned int)(2 + 3)), 2, v_rip + 1147447, (unsigned int)(v_stack_m6D0));
    result = IoSetBugCheckProgressFlag((unsigned int)(0x20000ULL), 2, v_rip + 1147447, (unsigned int)(v_stack_m6D0));
    if ((unsigned int)(v_rbx) != 0) goto loc_005B3465;
    *(unsigned __int64 *)(v_rip + 9896205) = v_stack_m598;
    v_stack_m740 = v_stack_m728;
    v_stack_m748 = (unsigned __int8)((unsigned int)(v_stack_m734));
    v_stack_m750 = v_stack_m6D8;
    *(unsigned __int64 *)(v_rip + 9896203) = v_stack_m728;
    v_stack_m758 = v_stack_m6E8;
    v_stack_m760 = v_stack_m598;
    *(unsigned __int64 *)(v_rip + 9896164) = v_stack_m6D8;
    *(unsigned __int8 *)(v_rip + 9896167) = (unsigned __int8)((unsigned int)(v_stack_m734));
    v_stack_m768 = *(unsigned __int64 *)(v_rip + 10043771);
    *(unsigned __int64 *)(v_rip + 9896125) = v_stack_m6E8;
    *(unsigned __int8 *)(v_rip + 9896143) = 1;
    result = IoRetryAsMiniDump((unsigned int)(*(unsigned int *)(v_rip + 10043713)), *(unsigned __int64 *)(v_rip + 10043733), *(unsigned __int64 *)(v_rip + 10043812), *(unsigned __int64 *)(v_rip + 10043827));
    goto loc_005B3716;
loc_005B3465:
    result = DbgPrintEx((unsigned int)((unsigned int)(2 + 3)), 1, v_rip + 1147166, *(unsigned __int64 *)(v_rip + 10043827));
    result = KiBugCheckDebugBreak(1 + 3, 1, v_rip + 1147166, *(unsigned __int64 *)(v_rip + 10043827));
    goto loc_005B3716;
loc_005B3490:
    result = DbgPrintEx(1 + 4, 1, v_rip + 1147380, *(unsigned __int64 *)(v_rip + 10043827));
loc_005B34A4:
    result = guard_dispatch_icall(1 + 4, 1, v_rip + 1147380, *(unsigned __int64 *)(v_rip + 10043827));
    goto loc_005B34A4;
loc_005B34B2:
loc_005B34B8:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10565058)))) <= 1) goto loc_005B3523;
    result = (unsigned int)(*(unsigned int *)(v_rip + 10565058));
    if ((*(unsigned __int8 *)(v_rip + 9122590)) == ((unsigned __int8)(v_stack_m72F))) {
        a1 = 2 + 3;
        result = KiSetDebuggerOwner(a1, 1, v_rip + 1147380, *(unsigned __int64 *)(v_rip + 10043827));
        a2 = 0;
        v_stack_m6A8 = 0x200001ULL;
        a1 = v_stack_m6A0;
        a3 = 256;
        result = memset(a1, a2, a3, *(unsigned __int64 *)(v_rip + 10043827));
        a2 = v_stack_m6A6;
        a3 = v_rip + 10566696;
        a1 = v_stack_m6A8;
        result = KiCopyAffinityEx(a1, a2, a3, *(unsigned __int64 *)(v_rip + 10043827));
        a2 = *(unsigned int *)(2 + 3 + 36);
        a1 = v_stack_m6A8;
        result = KeRemoveProcessorAffinityEx(a1, a2, a3, *(unsigned __int64 *)(v_rip + 10043827));
        a2 = 0;
        a1 = v_stack_m6A8;
        result = KiSendFreeze(a1, a2, a3, *(unsigned __int64 *)(v_rip + 10043827));
        a1 = 0xF4240ULL;
        result = KeStallExecutionProcessor(a1, a2, a3, *(unsigned __int64 *)(v_rip + 10043827));
    }
    result = IoSaveInitialBugCheckProgress((unsigned int)(*(unsigned int *)(v_rip + 10043472)), *(unsigned __int64 *)(v_rip + 10043486), a3, *(unsigned __int64 *)(v_rip + 10043827));
    result = IoSaveBugCheckProgress(1, *(unsigned __int64 *)(v_rip + 10043486), a3, *(unsigned __int64 *)(v_rip + 10043827));
    result = KiBugCheckProgressCpusFrozen((unsigned __int8)(v_rbx), *(unsigned __int64 *)(v_rip + 10043486), a3, *(unsigned __int64 *)(v_rip + 10043827));
    if ((*(unsigned int *)(2 + 3 + 35396)) == ((unsigned int)(v_stack_m72F))) goto loc_005B359B;
    if ((*(unsigned __int8 *)(v_rip + 10565017)) == ((unsigned __int8)(v_stack_m72F))) goto loc_005B3562;
    a2 = 0;
    result = PpmHvSetVirtualProcessorQos(2 + 3, a2, a3, *(unsigned __int64 *)(v_rip + 10043827));
    goto loc_005B359B;
loc_005B3562:
    if ((*(unsigned __int8 *)(v_rip + 10564979)) == ((unsigned __int8)(v_stack_m72F))) goto loc_005B359B;
    result = *(unsigned __int64 *)(2 + 3 + 35248);
    if (*(unsigned __int64 *)(2 + 3 + 35248) != 0) {
        a1 = *(unsigned __int64 *)(2 + 3 + 35256);
        a2 = *(unsigned __int64 *)(2 + 3 + 35248) + 808;
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(2 + 3 + 35248) + 392);
        a4 = 1;
        a3 = 1;
        a1 = *(unsigned __int64 *)(a1 + 8);
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
    if (1 != 0) goto loc_005B35CE;
    if ((unsigned __int8)(v_rbx) != 0) {
        a1 = (unsigned int)(((unsigned int)(v_stack_m6F8)) | (4));
    }
    result = (unsigned int)(((unsigned int)(a1)) | (2));
    if (v_stack_m720 != ((unsigned __int8)(v_stack_m72F))) { result = a1; }
    a1 = (unsigned int)(((unsigned int)((unsigned int)(result))) | (1));
    if ((unsigned __int8)(v_stack_m72F) != 0) { a1 = (unsigned int)(result); }
    result = KiDisplayBlueScreen(a1, a2, a3, a4);
    goto loc_005B35D3;
loc_005B35CE:
loc_005B35D3:
    result = HvlPrepareForRootCrashdump(1, a2, a3, a4);
    if (1 != 0) goto loc_005B3622;
    result = IoSaveBugCheckProgress(2, a2, a3, a4);
    a3 = 0;
    a2 = 0;
    result = KiInvokeBugCheckEntryCallbacks(1, a2, a3, a4);
    a2 = 0;
    a3 = 0;
    result = KiInvokeBugCheckEntryCallbacks(a2 + 8, a2, a3, a4);
    a2 = 0;
    a3 = 0;
    result = KiInvokeBugCheckEntryCallbacks((unsigned int)((unsigned int)(a2 + 9)), a2, a3, a4);
    result = IoSaveBugCheckProgress(a2 + 9 - 4, a2, a3, a4);
    result = KiInvokeBugCheckAddTriageDumpDataCallbacks(a2 + 9 - 4, a2, a3, a4);
    goto loc_005B3627;
loc_005B3622:
loc_005B3627:
    if ((*(unsigned __int8 *)(v_rip + 10043338)) != 0) goto loc_005B3640;
    if ((*(unsigned __int8 *)(v_rip + 8745957)) == 0) {
        a1 = 0;
        result = KdEnableDebuggerWithLock(a1, a2, a3, a4);
    }
loc_005B3653:
    *(unsigned __int64 *)(*(unsigned __int64 *)(2 + 3 + 36800)) = v_xmm0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(2 + 3 + 36800) + 16) = v_xmm1;
    *(unsigned __int64 *)(*(unsigned __int64 *)(2 + 3 + 36800) + 32) = v_xmm0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(2 + 3 + 36800) + 48) = v_xmm1;
    *(unsigned __int64 *)(*(unsigned __int64 *)(2 + 3 + 36800) + 64) = v_xmm0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(2 + 3 + 36800) + 80) = v_xmm1;
    *(unsigned __int64 *)(*(unsigned __int64 *)(2 + 3 + 36800) + 96) = v_xmm0;
    result = (*(unsigned __int64 *)(2 + 3 + 36800)) + (128);
    a1 = (v_stack_m598) + (128);
    *(unsigned __int64 *)(result - 16) = v_xmm1;
    v_rbx = (9) - (1);
    if (condition_is_not_equal) goto loc_005B3653;
    *(unsigned __int64 *)(result) = v_xmm0;
    *(unsigned __int64 *)(result + 16) = v_xmm1;
    *(unsigned __int64 *)(result + 32) = v_xmm0;
    *(unsigned __int64 *)(result + 48) = v_xmm1;
    *(unsigned __int64 *)(result + 64) = v_xmm0;
    if ((unsigned __int8)(v_stack_m738) != 0) {
        result = KdDecodeDataBlock(a1, 128, a3, a4);
        result = v_stack_m6D8;
        v_r10 = v_stack_m598;
        a1 = v_stack_m734;
        *(unsigned __int64 *)(v_rip + 9895469) = result;
        result = v_stack_m728;
        *(unsigned __int8 *)(v_rip + 9895474) = (unsigned __int8)(a1);
        a1 = v_rip + 9895435;
        *(unsigned __int64 *)(v_rip + 9895452) = result;
        *(unsigned __int64 *)(v_rip + 9895421) = v_r10;
        *(unsigned __int64 *)(v_rip + 9895422) = v_stack_m6E8;
        *(unsigned __int8 *)(v_rip + 9895440) = 1;
        result = KiBugCheckWriteCrashDump(a1, 128, a3, a4);
    }
    a1 = 0;
    result = HvlResumeFromRootCrashdump(a1, 128, a3, a4);
    result = IoSaveBugCheckProgress(99, 128, a3, a4);
    if (1 == 0) {
        result = KiScanBugCheckCallbackList(99, 128, a3, a4);
    }
    result = guard_dispatch_icall(99, 128, a3, a4);
    result = IoSaveBugCheckProgress(4, 128, a3, a4);
    if (v_stack_m720 == 0) goto loc_005B37A3;
    a1 = 0;
    *(unsigned __int8 *)(v_rip + 9122105) = 1;
    result = KiSendThawExecution(a1, 128, a3, a4);
    result = KiBugcheckUnloadDebugSymbols(a1, 128, a3, a4);
    a1 = 0;
    result = guard_dispatch_icall(a1, 128, a3, a4);
    if ((*(unsigned __int8 *)(v_rip + 9799082)) == 0) goto loc_005B3781;
    if ((*(unsigned __int8 *)(v_rip + 9799074)) == 0) goto loc_005B379B;
loc_005B3781:
    if ((*(unsigned __int8 *)(v_rip + 9799066)) != 0) goto loc_005B379B;
    if (v_stack_m70E != 0) goto loc_005B379B;
    if ((unsigned __int8)(v_stack_m72F) == 0) {
        a1 = 1;
    }
    result = HalReturnToFirmware(a1, 128, a3, a4);
loc_005B37A3:
    result = KiBugCheckDebugBreak(4, 128, a3, a4);
    v_rsp = (v_rsp) + (0x748ULL);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KeBugCheck2(int32_t Arg1, void *Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5, int64_t Arg6)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r10;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m598;
    uint64_t v_stack_m688;
    uint64_t v_stack_m6A0;
    uint16_t v_stack_m6A6;
    uint64_t v_stack_m6A8;
    uint64_t v_stack_m6B8;
    uint64_t v_stack_m6C0;
    uint64_t v_stack_m6C8;
    uint64_t v_stack_m6D0;
    uint64_t v_stack_m6D8;
    uint32_t v_stack_m6E0;
    uint64_t v_stack_m6E8;
    uint64_t v_stack_m6F0;
    uint32_t v_stack_m6F8;
    uint64_t v_stack_m700;
    uint32_t v_stack_m708;
    uint8_t v_stack_m70E;
    uint8_t v_stack_m70F;
    uint8_t v_stack_m710;
    uint64_t v_stack_m718;
    uint8_t v_stack_m720;
    uint64_t v_stack_m728;
    uint8_t v_stack_m72E;
    uint8_t v_stack_m72F;
    uint8_t v_stack_m730;
    uint8_t v_stack_m734;
    uint8_t v_stack_m738;
    uint64_t v_stack_m740;
    uint8_t v_stack_m748;
    uint64_t v_stack_m750;
    uint64_t v_stack_m758;
    uint32_t v_stack_m760;
    uint64_t v_stack_m768;
    uint8_t v_stack_mC8;

    local_rsp = (local_rsp) - (0x748ULL);
    v_stack_m6D0 = Arg3;
    Arg2 = 0;
    v_stack_m708 = Arg1;
    v_stack_m728 = Arg6;
    result = memset(v_stack_m6A8, Arg2, 264, Arg4);
    local_r14 = 0;
    v_stack_m72F = 1;
    v_stack_mC8 = 0;
    v_stack_m6E8 = *(uint64_t *)(gs_base + (0 + 0x188));
    v_stack_m6D8 = v_rip + 5702;
    v_stack_m6F0 = 0;
    v_stack_m72E = 0;
    v_stack_m700 = 0;
    v_stack_m734 = 0;
    v_stack_m710 = 0;
    v_stack_m70E = 0;
    v_stack_m6B8 = 0;
    v_stack_m718 = 0;
    v_stack_m738 = 1;
    v_stack_m70F = 0;
    v_stack_m6F8 = 0;
    if ((uint32_t)(local_r14 + 1) != 0) goto loc_005B28C9;
    result = (uint32_t)(v_stack_m708);
    if (((uint32_t)((uint32_t)(v_stack_m708))) == 0xC00002D1ULL) {
        result = 195;
        v_stack_m708 = (uint32_t)(result);
    }
    *(uint64_t *)(v_rip + 0x994CD3) = result;
    *(uint64_t *)(v_rip + 0x994CD4) = 0;
    *(uint64_t *)(v_rip + 0x994CD5) = Arg3;
    *(uint64_t *)(v_rip + 0x994CD6) = Arg4;
    *(uint64_t *)(v_rip + 0x994CD7) = Arg5;
loc_005B28C9:
    Arg3 = 0;
    result = IoNotifyDumpEx((uint32_t)((uint32_t)(Arg3 + 4)), Arg2, Arg3, Arg4);
    result = (uint32_t)(*(uint32_t *)(v_rip + 0xA141B3));
    if ((((uint8_t)(Arg3 + 4 - 2)) & ((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA141B3))))) != 0) {
        Arg1 = (uint32_t)(Arg3 + 4);
        result = HvlNotifyRootCrashdump(Arg1, Arg2, Arg3, Arg4);
    }
    v_stack_m6C8 = 0;
    v_stack_m6C0 = 0;
    v_stack_m6E0 = 0;
    if (((uint8_t)(v_cr8)) >= ((uint8_t)(Arg3 + 4 - 2))) goto loc_005B291A;
    result = v_cr8;
    if ((*(uint32_t *)(v_rip + 0xA14410)) != 0) {
        Arg2 = (uint8_t)(Arg3 + 4 - 2);
        result = KiRaiseIrqlProcessIrqlFlags(v_cr8, Arg2, Arg3, Arg4);
    }
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x28)) != 0) goto loc_005B2974;
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x24))) << (4));
    Arg2 = (uint32_t)((Arg2) | (3));
loc_005B2946:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x994C0F))))) & (3));
    if (((uint8_t)(Arg1)) == 3) goto loc_005B2965;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x994C0F)))) != ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x994C0F))))))) goto loc_005B2946;
    v_stack_m730 = 1;
    goto loc_005B296A;
loc_005B2965:
    v_stack_m730 = 0;
loc_005B296A:
    goto loc_005B2AEA;
loc_005B2974:
    result = KeQueryCurrentStackInformation(v_stack_m6E0, v_stack_m6C0, v_stack_m6C8, Arg4);
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x24))) << (4));
    Arg2 = (uint32_t)((Arg2) | (3));
loc_005B299F:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x994BB6))))) & (3));
    if (((uint8_t)(Arg1)) == 3) goto loc_005B2ADD;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x994BB6)))) != ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x994BB6))))))) goto loc_005B299F;
    Arg3 = 0;
    result = IoNotifyDumpEx(Arg3 + 6, Arg2, Arg3, Arg4);
    if ((uint8_t)((uint8_t)(result)) == 0) goto loc_005B2A5C;
    if (((uint32_t)((uint32_t)(v_stack_m6E0))) > 9) goto loc_005B29E1;
    if (((uint32_t)((uint32_t)(v_stack_m6E0))) < 9) goto loc_005B2A5C;
loc_005B29E1:
    result = (v_stack_m6C8) - (v_stack_m6C0);
    if (result > ((uint32_t)(0x24000ULL))) goto loc_005B2A01;
    if (result == 0) goto loc_005B2A47;
loc_005B2A01:
    local_rsi = (v_rip + 9898808) - (v_stack_m6C0);
    local_rdi = (result) - 1;
    local_rdi = (local_rdi) >> (12);
    local_rdi = (local_rdi) + 1;
loc_005B2A15:
    Arg2 = 0;
    result = MmIsAddressValidEx(v_stack_m6C0, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_005B2A37;
    result = memcpy(v_stack_m6C0 + local_rsi * 1, v_stack_m6C0, (uint32_t)(0x1000ULL), Arg4);
    goto loc_005B2A3A;
loc_005B2A37:
    local_r14 = 0;
loc_005B2A3A:
    local_rbx = (v_stack_m6C0) + (0x1000ULL);
    local_rdi = (local_rdi) - (1);
    if (condition_is_not_equal) goto loc_005B2A15;
loc_005B2A47:
    result = IoNotifyDumpEx(7, v_stack_m6C0, 0, Arg4);
    local_r14 = 0;
loc_005B2A5C:
    if ((*(uint8_t *)(v_rip + 0xC4EDDE)) == 0) goto loc_005B2ACE;
    Arg3 = 0;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x420)) & (0xFFFFFFFFFFFFF000ULL);
    Arg1 = (Arg1) + (0x1000ULL);
    Arg2 = (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x418)) - (0x1000ULL);
    if (0 <= Arg1) goto loc_005B2ACE;
    if (0 >= Arg2) goto loc_005B2AD3;
    Arg2 = Arg3 - 256;
    if ((Arg3 - 256) < Arg1) { Arg2 = Arg1; }
    Arg3 = (Arg3) - (Arg2);
    if (Arg3 > 256) { Arg3 = 256; }
    result = memcpy(v_rip + 10573315, Arg2, Arg3, Arg4);
    goto loc_005B2AD3;
loc_005B2ACE:
loc_005B2AD3:
    v_stack_m730 = 1;
    goto loc_005B2AEA;
loc_005B2ADD:
    v_stack_m730 = 0;
loc_005B2AEA:
    result = DbgPrintEx(2 + 3, 2, v_rip + 1149878, 0);
    if (0 == 0) goto loc_005B2B18;
    if (!(condition_is_greater)) {
        *(uint8_t *)(v_rip + 0x994A30) = 1;
    }
    if ((*(uint32_t *)(v_rip + 0xA140D1)) != 0) {
    }
    Arg2 = (*(uint64_t *)(v_rip + 0xA1412C)) | (256);
    v_stack_m6D0 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x24)));
    result = KeSaveSupervisorState(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x6C0), Arg2, v_rip + 1149878, 0);
    if (*(uint64_t *)(v_rip + 0x95923F) != 0) goto loc_005B2B5E;
loc_005B2B59:
    local_rsi = 0;
    goto loc_005B2BAB;
loc_005B2B5E:
    if ((*(uint32_t *)(v_rip + 0x95977B)) != 0) {
        *(uint8_t *)(v_rip + 0x9591B2) = 0;
    }
    if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0x95923F) + 0x2)) == 0) goto loc_005B2B59;
    if (0 == 0) goto loc_005B2BA3;
    Arg2 = 0;
    result = DbgPrintEx(Arg2 + 101, Arg2, v_rip + 1151982, 0);
    if (((uint32_t)((uint32_t)(v_stack_m708))) == 10) {
        Arg3 = v_rip + 1152154;
        Arg2 = 0;
        Arg1 = (uint32_t)(v_stack_m708) + 91;
        result = DbgPrintEx(Arg1, Arg2, Arg3, 0);
    }
loc_005B2BA3:
loc_005B2BAB:
loc_005B2BC2:
    *(uint64_t *)(v_stack_m598) = v_xmm0;
    *(uint64_t *)(v_stack_m598 + 0x10) = v_xmm1;
    *(uint64_t *)(v_stack_m598 + 0x20) = v_xmm0;
    *(uint64_t *)(v_stack_m598 + 0x30) = v_xmm1;
    *(uint64_t *)(v_stack_m598 + 0x40) = v_xmm0;
    *(uint64_t *)(v_stack_m598 + 0x50) = v_xmm1;
    *(uint64_t *)(v_stack_m598 + 0x60) = v_xmm0;
    Arg1 = (v_stack_m598) + (9 + 119);
    result = (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8FC0)) + (9 + 119);
    *(uint64_t *)(Arg1 - 0x10) = v_xmm1;
    Arg2 = (9) - (1);
    if (condition_is_not_equal) goto loc_005B2BC2;
    *(uint64_t *)(Arg1) = v_xmm0;
    *(uint64_t *)(Arg1 + 0x10) = v_xmm1;
    *(uint64_t *)(Arg1 + 0x20) = v_xmm0;
    *(uint64_t *)(Arg1 + 0x30) = v_xmm1;
    *(uint64_t *)(Arg1 + 0x40) = v_xmm0;
    if (v_stack_m730 == ((uint8_t)(Arg2))) goto loc_005B3300;
    local_rbx = (uint32_t)(v_stack_m708);
    if ((*(uint32_t *)(v_rip + 0x951D42)) != ((uint32_t)(Arg2))) {
        Arg1 = Arg2 + 2;
        result = VfNotifyVerifierOfEvent(Arg1, Arg2, 9 + 119, 0);
        local_rbx = v_stack_m708;
    }
    if (((uint32_t)(local_rbx)) == 229) {
        result = KiScanBugCheckCallbackList(Arg1, Arg2, 9 + 119, 0);
        result = *(uint64_t *)(v_rip + 0x84DEA5);
        Arg1 = 0;
        result = guard_dispatch_icall(Arg1, Arg2, 9 + 119, 0);
        Arg1 = 3;
        result = HalReturnToFirmware(Arg1, Arg2, 9 + 119, 0);
        local_rbx = v_stack_m708;
    }
    if (((uint32_t)(local_rbx)) > 209) goto loc_005B2F5A;
    if (((uint32_t)(local_rbx)) == 209) goto loc_005B2E36;
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) - (10));
    if (condition_is_equal) goto loc_005B2E36;
    result = (uint32_t)((result) - (49));
    if (condition_is_equal) goto loc_005B2E2D;
    result = (uint32_t)((result) - (17));
    if (condition_is_equal) goto loc_005B2DE5;
    result = (uint32_t)((result) - (4));
    if (condition_is_equal) goto loc_005B2D69;
    result = (uint32_t)((result) - (43));
    if (condition_is_equal) goto loc_005B2D46;
    result = (uint32_t)((result) - (19));
    if (condition_is_equal) goto loc_005B3053;
    result = (uint32_t)((result) - (18));
    if (condition_is_equal) goto loc_005B2D10;
    result = (uint32_t)((result) - (30));
    if (condition_is_equal) goto loc_005B3053;
    if (((uint32_t)(result)) != 13) goto loc_005B2FA3;
    v_stack_m700 = Arg2;
loc_005B2CDC:
loc_005B2CE1:
loc_005B2CE5:
loc_005B2CEA:
loc_005B2CEF:
    if (*(uint64_t *)(v_rip + 0x8B3AEA) == 0) goto loc_005B30BE;
    result = KiBugCheckUnicodeToAnsi(*(uint64_t *)(v_rip + 0x8B3AEA), v_stack_mC8, 9 + 119, 0);
    goto loc_005B30DE;
loc_005B2D10:
    if (((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x5FC)) & (0x1000ULL)) != 0) goto loc_005B2CDC;
    if ((v_stack_m738 - 240) > 1) goto loc_005B2CE1;
    v_stack_m734 = 1;
    goto loc_005B2CE5;
loc_005B2D46:
    local_r15 = (uint8_t)(((uint8_t)(Arg4)) >> (1));
    result = (uint8_t)(~((uint8_t)(Arg4)));
    result = (uint8_t)((result) & (1));
    local_r15 = (uint8_t)(~(local_r15));
    v_stack_m72F = (uint8_t)(result);
    local_r15 = (uint8_t)((local_r15) & (1));
    goto loc_005B2CEA;
loc_005B2D69:
    if (v_stack_m728 != 0) goto loc_005B2D81;
    if (Arg4 == 0) goto loc_005B2DB2;
    if ((((uint8_t)(Arg4)) & (3)) != 0) goto loc_005B2DB2;
loc_005B2D81:
    Arg3 = 0;
    v_stack_m700 = *(uint64_t *)(Arg4 + 0x168);
    *(uint64_t *)(v_rip + 0x9947F9) = *(uint64_t *)(Arg4 + 0x168);
    result = KiPcToFileHeader(*(uint64_t *)(Arg4 + 0x168), v_stack_m6F0, Arg3, v_stack_m72E);
    v_stack_m728 = Arg4;
    if (result != 0) goto loc_005B2CE1;
loc_005B2DB2:
    result = MmLocateUnloadedDriver(local_r15, v_stack_m6F0, Arg3, v_stack_m72E);
    if (result == 0) goto loc_005B2CE1;
    local_r15 = (uint32_t)((local_r15) - (*(uint32_t *)(result + 0x10)));
    *(uint32_t *)(v_rip + 0x8B3A22) = (uint32_t)(local_r15);
    *(uint64_t *)(v_rip + 0x8B3A0B) = result;
    *(uint64_t *)(v_rip + 0x9947A0) = 206;
    goto loc_005B2CE1;
loc_005B2DE5:
    v_stack_m734 = 1;
    v_stack_m710 = 1;
    *(uint64_t *)(v_rip + 0x994779) = (uint32_t)((uint32_t)(local_r15));
    local_rdi = (Arg4) - (v_rip + 10045335);
    v_stack_m6B8 = Arg4;
loc_005B2E0E:
    *(uint64_t *)(v_rip + 0x994797) = *(uint64_t *)(local_rdi + v_rip + 0x994797 * 1);
    Arg1 = (v_rip + 10045335) + (8);
    if (Arg1 < (v_rip + 10045352)) goto loc_005B2E0E;
loc_005B2E23:
    goto loc_005B2CEF;
loc_005B2E2D:
    v_stack_m700 = v_stack_m718;
    goto loc_005B2CDC;
loc_005B2E36:
    v_stack_m700 = v_stack_m718;
    if (v_stack_m718 < (*(uint64_t *)(v_rip + 0x94265B))) goto loc_005B2E5C;
    if (v_stack_m718 >= (*(uint64_t *)(v_rip + 0x942656))) goto loc_005B2E5C;
    *(uint64_t *)(v_rip + 0x994729) = 197;
    goto loc_005B2CDC;
loc_005B2E5C:
    Arg3 = 0;
    result = KiPcToFileHeader(v_stack_m718, v_stack_m6F0, Arg3, v_stack_m72E);
    if (v_stack_m72E != 1) goto loc_005B2F1A;
    local_r13 = (uint32_t)((v_stack_m718) - ((uint32_t)(result)));
    result = (v_stack_m6F0) + (88);
    *(uint32_t *)(v_rip + 0x8B395A) = (uint32_t)(local_r13);
    *(uint64_t *)(v_rip + 0x8B393D) = result;
    result = KiPcToFileHeader(v_stack_m738, v_stack_m6F0, 1, v_stack_m72E);
    if (result == 0) goto loc_005B2ED9;
    local_r15 = (uint32_t)((v_stack_m738) - ((uint32_t)(result)));
    *(uint64_t *)(v_rip + 0x9946C2) = 211;
    result = (v_stack_m6F0) + (88);
    *(uint32_t *)(v_rip + 0x8B3923) = (uint32_t)(local_r15);
    *(uint64_t *)(v_rip + 0x8B390C) = result;
    goto loc_005B2CDC;
loc_005B2ED9:
    result = MmLocateUnloadedDriver(local_r15, v_stack_m6F0, 1, v_stack_m72E);
    if (result == 0) goto loc_005B2E23;
    local_r15 = (uint32_t)((local_r15) - (*(uint32_t *)(result + 0x10)));
    *(uint32_t *)(v_rip + 0x8B38ED) = (uint32_t)(local_r15);
    *(uint64_t *)(v_rip + 0x8B38D6) = result;
    *(uint64_t *)(v_rip + 0x99466B) = 212;
    goto loc_005B2E23;
loc_005B2F1A:
    *(uint64_t *)(v_rip + 0x99464D) = 209;
    if (result == 0) goto loc_005B2CEA;
    local_r13 = (uint32_t)((v_stack_m718) - ((uint32_t)(result)));
    result = (v_stack_m6F0) + (88);
    *(uint32_t *)(v_rip + 0x8B38A2) = (uint32_t)(local_r13);
    *(uint64_t *)(v_rip + 0x8B388B) = result;
    goto loc_005B2CEA;
loc_005B2F5A:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m734)))) - (216));
    if (condition_is_equal) goto loc_005B30AE;
    result = (uint32_t)((result) - (14));
    if (condition_is_equal) goto loc_005B3093;
    result = (uint32_t)((result) - (4));
    if (condition_is_equal) goto loc_005B3087;
    result = (uint32_t)((result) - (5));
    if (condition_is_equal) goto loc_005B3083;
    result = (uint32_t)((result) - (13));
    if (condition_is_equal) goto loc_005B3053;
    result = (uint32_t)((result) - (61));
    if (condition_is_equal) goto loc_005B3024;
    result = (uint32_t)((result) - (4));
    if (condition_is_equal) goto loc_005B3018;
    result = (uint32_t)((result) - (18));
    if (condition_is_equal) goto loc_005B2FCB;
    if (((uint32_t)(result)) == 121) goto loc_005B2FC1;
loc_005B2FA3:
loc_005B2FAB:
    if (v_stack_m728 == 0) goto loc_005B2CE1;
    v_stack_m700 = *(uint64_t *)(v_stack_m728 + 0x168);
    goto loc_005B2CE1;
loc_005B2FC1:
    v_stack_m70E = 1;
    goto loc_005B2CDC;
loc_005B2FCB:
    if (v_stack_m728 >= 256) goto loc_005B2FEC;
    result = *(uint64_t *)(v_stack_m728 + 0x168);
    if (local_r13 != 0) {
        result = *(uint64_t *)(local_r13 + 0x8);
        Arg1 = v_stack_m6E8;
        if (result != 0) { Arg1 = result; }
        v_stack_m6E8 = Arg1;
    }
    local_rbx = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x5FC))) >> (12));
    local_rbx = (uint8_t)(~(local_rbx));
    local_rbx = (uint8_t)((local_rbx) & (1));
loc_005B300A:
    v_stack_m734 = (uint32_t)(local_rbx);
loc_005B300E:
    goto loc_005B2CE5;
loc_005B3018:
    v_stack_m6F8 = 8;
    goto loc_005B2CDC;
loc_005B3024:
    if (v_stack_m728 == 0) goto loc_005B3045;
    v_stack_m700 = *(uint64_t *)(v_stack_m728 + 0x168);
    goto loc_005B2CE5;
loc_005B3045:
    local_rdi = v_stack_m728;
    if (v_stack_m738 == 10) { local_rdi = local_r13; }
    v_stack_m700 = local_rdi;
    goto loc_005B300E;
loc_005B3053:
    if (v_stack_m728 != 0) goto loc_005B3078;
    if (Arg4 == 0) goto loc_005B2CE1;
    if ((((uint8_t)(Arg4)) & (3)) != 0) goto loc_005B2CE1;
    v_stack_m728 = Arg4;
loc_005B3078:
    goto loc_005B2FAB;
loc_005B3083:
    goto loc_005B300A;
loc_005B3087:
    *(uint64_t *)(v_rip + 0x8B3752) = Arg4;
    goto loc_005B2CDC;
loc_005B3093:
    if (((uint32_t)(v_stack_m738)) != 39) goto loc_005B2CDC;
    result = IoAddTriageDumpDataBlock(Arg4, v_stack_m738 - 31, 1, v_stack_m72E);
    goto loc_005B2CDC;
loc_005B30AE:
    *(uint64_t *)(v_rip + 0x8B3727) = v_stack_m738 + 88;
    goto loc_005B2CDC;
loc_005B30BE:
    result = v_stack_m738 + 88;
    if (v_stack_m700 != 0) {
        Arg4 = 1;
        Arg2 = v_stack_m700;
        Arg3 = 1;
        Arg1 = v_stack_mC8;
        result = KiDumpParameterImages(Arg1, Arg2, Arg3, Arg4);
    }
    if ((*(uint32_t *)(v_rip + 0x946E1B)) != 0) goto loc_005B3101;
    result = WheapSelLogSetNtSchedulerAvailabilityNoLock(Arg1, Arg2, Arg3, Arg4);
    result = IpmiHwContextInitialized(v_rip + 9727885, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        result = IpmiLibAddSelBugcheckRecord(v_rip + 9727885, Arg2, Arg3, Arg4);
    }
    result = 0;
    result = (((uint32_t)(*(uint64_t *)(v_rip + 0x994478))) != 265) ? 1 : 0;
    *(uint32_t *)(v_rip + 0x8B2DBB) = (uint32_t)(result);
    if ((uint8_t)(v_stack_m738) != 0) {
        Arg2 = 1;
        result = KiCollectTriageDumpDataBlocks(*(uint64_t *)(v_rip + 0x994478), Arg2, Arg3, Arg4);
    }
    if (v_stack_m720 == 0) goto loc_005B3174;
    result = (uint32_t)(*(uint32_t *)(v_rip + 0x85787D));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x85787D)))) & (4)) != 0) {
        result = v_stack_m598;
        *(uint64_t *)(v_rip + 0x9703BF) = v_stack_m6E8;
        *(uint64_t *)(v_rip + 0x9703B0) = result;
        result = v_stack_m6D8;
        *(uint64_t *)(v_rip + 0x9703B5) = result;
        *(uint64_t *)(v_rip + 0x9703B6) = Arg4;
        *(uint8_t *)(v_rip + 0x9703B8) = 1;
        *(uint8_t *)(v_rip + 0x9703B2) = 1;
        result = KiAttemptBugcheckRecovery(*(uint64_t *)(v_rip + 0x994478), Arg2, Arg3, Arg4);
    }
    *(uint8_t *)(v_rip + 0x9943C6) = 1;
    result = guard_dispatch_icall(*(uint64_t *)(v_rip + 0x994478), Arg2, Arg3, Arg4);
    result = IoSaveBugCheckProgress(96, Arg2, Arg3, Arg4);
    result = KeIsEmptyAffinityEx(v_rip + 8747198, Arg2, Arg3, Arg4);
    local_rdi = 0;
    Arg1 = ((uint32_t)(result) == 0) ? 1 : 0;
    result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    result = KiFilterBugCheckInfo(v_stack_m708, v_rip + 10044349, Arg3, Arg4);
    if ((*(uint64_t *)(v_rip + 0x8B2E7D)) == 0) goto loc_005B31DA;
    if ((uint8_t)(v_stack_m738) != 0) goto loc_005B31DE;
loc_005B31DA:
    goto loc_005B31E1;
loc_005B31DE:
loc_005B31E1:
    v_stack_m760 = 0;
    v_stack_m768 = *(uint64_t *)(v_rip + 0x994396);
    result = HvlLogGuestCrashInformation((uint32_t)(*(uint32_t *)(v_rip + 0x994384)), *(uint64_t *)(v_rip + 0x994392), *(uint64_t *)(v_rip + 0x9943A1), *(uint64_t *)(v_rip + 0x9943B0));
    if ((*(uint8_t *)(v_rip + 0x857801)) == 0) {
        result = v_stack_m598;
        *(uint64_t *)(v_rip + 0x84DE5D) = result;
    }
    Arg2 = 0;
    result = KiBugCheckShouldEnterPostBugCheckDebugger((uint32_t)(v_stack_m708), Arg2, *(uint64_t *)(v_rip + 0x9943A1), *(uint64_t *)(v_rip + 0x9943B0));
    if ((uint8_t)(result) == 0) goto loc_005B330F;
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x83A6)) != 0) goto loc_005B32E2;
    Arg2 = 0;
    v_stack_m750 = *(uint64_t *)(v_rip + 0x99434F);
    v_stack_m758 = *(uint64_t *)(v_rip + 0x99432B);
    v_stack_m760 = *(uint64_t *)(v_rip + 0x994317);
    v_stack_m768 = *(uint64_t *)(v_rip + 0x994300);
    result = DbgPrintEx(Arg2 + 101, Arg2, v_rip + 1148120, (uint32_t)(*(uint32_t *)(v_rip + 0x994321)));
    if ((*(uint64_t *)(v_rip + 0x8B3547)) != 0) {
        Arg2 = 0;
        Arg4 = v_stack_mC8;
        Arg3 = v_rip + 1148005;
        Arg1 = Arg2 + 101;
        result = DbgPrintEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (v_stack_m710 == 0) goto loc_005B32E2;
    result = v_stack_m6B8;
    if (v_stack_m6B8 != 0) {
        Arg2 = 0;
        Arg3 = v_stack_m6B8;
        Arg1 = Arg2 + 101;
        result = DbgPrintEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (local_r13 != 0) {
        Arg2 = 0;
        Arg3 = local_r13;
        Arg1 = Arg2 + 101;
        result = DbgPrintEx(Arg1, Arg2, Arg3, Arg4);
    }
    if ((*(uint8_t *)(v_rip + 0x99430F)) == 0) goto loc_005B330F;
    if ((*(uint8_t *)(v_rip + 0x9942EA)) != 0) goto loc_005B330F;
    result = KiBugCheckDebugBreak(3, Arg2, Arg3, Arg4);
    goto loc_005B330F;
loc_005B3300:
    local_rdi = 0;
loc_005B330F:
    if ((*(uint32_t *)(v_rip + 0xA139FD)) != 0) {
        result = KiRaiseIrqlProcessIrqlFlags(Arg3 + 4 - 2, 15, Arg3, Arg4);
    }
    if (v_stack_m730 != 0) goto loc_005B34B2;
    result = KiHandleMultipleBugchecksDuringRecovery((uint32_t)(*(uint32_t *)(v_rip + 0x994211)), 15, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_005B3356;
    *(uint8_t *)(v_rip + 0x9941F7) = 1;
    goto loc_005B34B8;
loc_005B3356:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x9941F0))))) >> (4));
    result = (uint32_t)(*(uint32_t *)(v_rip + 0x9941F0));
    if (((uint32_t)((uint32_t)(v_stack_m6D0))) != Arg1) {
        result = KiYieldWaitForDebugger(Arg1, 15, Arg3, (uint32_t)(v_stack_m6D0));
    }
    if ((*(uint8_t *)(v_rip + 0x8B3471)) != 0) goto loc_005B3490;
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)(result))) >> (2));
    local_rbx = (uint32_t)((local_rbx) & (3));
    if (((uint32_t)(local_rbx)) >= 2) goto loc_005B3490;
    v_stack_m758 = Arg1;
    v_stack_m760 = (uint32_t)(local_rbx);
    result = (uint32_t)((result) & (3));
    v_stack_m768 = (uint32_t)(result);
    result = DbgPrintEx((uint32_t)((uint32_t)(2 + 3)), 2, v_rip + 1147447, (uint32_t)(v_stack_m6D0));
    result = IoSetBugCheckProgressFlag((uint32_t)(0x20000ULL), 2, v_rip + 1147447, (uint32_t)(v_stack_m6D0));
    if ((uint32_t)(local_rbx) != 0) goto loc_005B3465;
    *(uint64_t *)(v_rip + 0x97010D) = v_stack_m598;
    v_stack_m740 = v_stack_m728;
    v_stack_m748 = (uint8_t)((uint32_t)(v_stack_m734));
    v_stack_m750 = v_stack_m6D8;
    *(uint64_t *)(v_rip + 0x97010B) = v_stack_m728;
    v_stack_m758 = v_stack_m6E8;
    v_stack_m760 = v_stack_m598;
    *(uint64_t *)(v_rip + 0x9700E4) = v_stack_m6D8;
    *(uint8_t *)(v_rip + 0x9700E7) = (uint8_t)((uint32_t)(v_stack_m734));
    v_stack_m768 = *(uint64_t *)(v_rip + 0x99417B);
    *(uint64_t *)(v_rip + 0x9700BD) = v_stack_m6E8;
    *(uint8_t *)(v_rip + 0x9700CF) = 1;
    result = IoRetryAsMiniDump((uint32_t)(*(uint32_t *)(v_rip + 0x994141)), *(uint64_t *)(v_rip + 0x994155), *(uint64_t *)(v_rip + 0x9941A4), *(uint64_t *)(v_rip + 0x9941B3));
    goto loc_005B3716;
loc_005B3465:
    result = DbgPrintEx((uint32_t)((uint32_t)(2 + 3)), 1, v_rip + 1147166, *(uint64_t *)(v_rip + 0x9941B3));
    result = KiBugCheckDebugBreak(1 + 3, 1, v_rip + 1147166, *(uint64_t *)(v_rip + 0x9941B3));
    goto loc_005B3716;
loc_005B3490:
    result = DbgPrintEx(1 + 4, 1, v_rip + 1147380, *(uint64_t *)(v_rip + 0x9941B3));
loc_005B34A4:
    result = guard_dispatch_icall(1 + 4, 1, v_rip + 1147380, *(uint64_t *)(v_rip + 0x9941B3));
    goto loc_005B34A4;
loc_005B34B2:
loc_005B34B8:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA135C2)))) <= 1) goto loc_005B3523;
    result = (uint32_t)(*(uint32_t *)(v_rip + 0xA135C2));
    if ((*(uint8_t *)(v_rip + 0x8B331E)) == ((uint8_t)(v_stack_m72F))) {
        Arg1 = 2 + 3;
        result = KiSetDebuggerOwner(Arg1, 1, v_rip + 1147380, *(uint64_t *)(v_rip + 0x9941B3));
        Arg2 = 0;
        v_stack_m6A8 = 0x200001ULL;
        Arg1 = v_stack_m6A0;
        Arg3 = 256;
        result = memset(Arg1, Arg2, Arg3, *(uint64_t *)(v_rip + 0x9941B3));
        Arg2 = v_stack_m6A6;
        Arg3 = v_rip + 10566696;
        Arg1 = v_stack_m6A8;
        result = KiCopyAffinityEx(Arg1, Arg2, Arg3, *(uint64_t *)(v_rip + 0x9941B3));
        Arg2 = *(uint32_t *)(2 + 0x3 + 0x24);
        Arg1 = v_stack_m6A8;
        result = KeRemoveProcessorAffinityEx(Arg1, Arg2, Arg3, *(uint64_t *)(v_rip + 0x9941B3));
        Arg2 = 0;
        Arg1 = v_stack_m6A8;
        result = KiSendFreeze(Arg1, Arg2, Arg3, *(uint64_t *)(v_rip + 0x9941B3));
        Arg1 = 0xF4240ULL;
        result = KeStallExecutionProcessor(Arg1, Arg2, Arg3, *(uint64_t *)(v_rip + 0x9941B3));
    }
    result = IoSaveInitialBugCheckProgress((uint32_t)(*(uint32_t *)(v_rip + 0x994050)), *(uint64_t *)(v_rip + 0x99405E), Arg3, *(uint64_t *)(v_rip + 0x9941B3));
    result = IoSaveBugCheckProgress(1, *(uint64_t *)(v_rip + 0x99405E), Arg3, *(uint64_t *)(v_rip + 0x9941B3));
    result = KiBugCheckProgressCpusFrozen((uint8_t)(local_rbx), *(uint64_t *)(v_rip + 0x99405E), Arg3, *(uint64_t *)(v_rip + 0x9941B3));
    if ((*(uint32_t *)(2 + 0x3 + 0x8A44)) == ((uint32_t)(v_stack_m72F))) goto loc_005B359B;
    if ((*(uint8_t *)(v_rip + 0xA13599)) == ((uint8_t)(v_stack_m72F))) goto loc_005B3562;
    Arg2 = 0;
    result = PpmHvSetVirtualProcessorQos(2 + 3, Arg2, Arg3, *(uint64_t *)(v_rip + 0x9941B3));
    goto loc_005B359B;
loc_005B3562:
    if ((*(uint8_t *)(v_rip + 0xA13573)) == ((uint8_t)(v_stack_m72F))) goto loc_005B359B;
    result = *(uint64_t *)(2 + 0x3 + 0x89B0);
    if (*(uint64_t *)(2 + 0x3 + 0x89B0) != 0) {
        Arg1 = *(uint64_t *)(2 + 0x3 + 0x89B8);
        Arg2 = *(uint64_t *)(2 + 0x3 + 0x89B0) + 808;
        result = *(uint64_t *)(*(uint64_t *)(2 + 0x3 + 0x89B0) + 0x188);
        Arg4 = 1;
        Arg3 = 1;
        Arg1 = *(uint64_t *)(Arg1 + 0x8);
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
    if (1 != 0) goto loc_005B35CE;
    if ((uint8_t)(local_rbx) != 0) {
        Arg1 = (uint32_t)(((uint32_t)(v_stack_m6F8)) | (4));
    }
    result = (uint32_t)(((uint32_t)(Arg1)) | (2));
    if (v_stack_m720 != ((uint8_t)(v_stack_m72F))) { result = Arg1; }
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(result))) | (1));
    if ((uint8_t)(v_stack_m72F) != 0) { Arg1 = (uint32_t)(result); }
    result = KiDisplayBlueScreen(Arg1, Arg2, Arg3, Arg4);
    goto loc_005B35D3;
loc_005B35CE:
loc_005B35D3:
    result = HvlPrepareForRootCrashdump(1, Arg2, Arg3, Arg4);
    if (1 != 0) goto loc_005B3622;
    result = IoSaveBugCheckProgress(2, Arg2, Arg3, Arg4);
    Arg3 = 0;
    Arg2 = 0;
    result = KiInvokeBugCheckEntryCallbacks(1, Arg2, Arg3, Arg4);
    Arg2 = 0;
    Arg3 = 0;
    result = KiInvokeBugCheckEntryCallbacks(Arg2 + 8, Arg2, Arg3, Arg4);
    Arg2 = 0;
    Arg3 = 0;
    result = KiInvokeBugCheckEntryCallbacks((uint32_t)((uint32_t)(Arg2 + 9)), Arg2, Arg3, Arg4);
    result = IoSaveBugCheckProgress(Arg2 + 9 - 4, Arg2, Arg3, Arg4);
    result = KiInvokeBugCheckAddTriageDumpDataCallbacks(Arg2 + 9 - 4, Arg2, Arg3, Arg4);
    goto loc_005B3627;
loc_005B3622:
loc_005B3627:
    if ((*(uint8_t *)(v_rip + 0x993FCA)) != 0) goto loc_005B3640;
    if ((*(uint8_t *)(v_rip + 0x8573E5)) == 0) {
        Arg1 = 0;
        result = KdEnableDebuggerWithLock(Arg1, Arg2, Arg3, Arg4);
    }
loc_005B3653:
    *(uint64_t *)(*(uint64_t *)(2 + 0x3 + 0x8FC0)) = v_xmm0;
    *(uint64_t *)(*(uint64_t *)(2 + 0x3 + 0x8FC0) + 0x10) = v_xmm1;
    *(uint64_t *)(*(uint64_t *)(2 + 0x3 + 0x8FC0) + 0x20) = v_xmm0;
    *(uint64_t *)(*(uint64_t *)(2 + 0x3 + 0x8FC0) + 0x30) = v_xmm1;
    *(uint64_t *)(*(uint64_t *)(2 + 0x3 + 0x8FC0) + 0x40) = v_xmm0;
    *(uint64_t *)(*(uint64_t *)(2 + 0x3 + 0x8FC0) + 0x50) = v_xmm1;
    *(uint64_t *)(*(uint64_t *)(2 + 0x3 + 0x8FC0) + 0x60) = v_xmm0;
    result = (*(uint64_t *)(2 + 0x3 + 0x8FC0)) + (128);
    Arg1 = (v_stack_m598) + (128);
    *(uint64_t *)(result - 0x10) = v_xmm1;
    local_rbx = (9) - (1);
    if (condition_is_not_equal) goto loc_005B3653;
    *(uint64_t *)(result) = v_xmm0;
    *(uint64_t *)(result + 0x10) = v_xmm1;
    *(uint64_t *)(result + 0x20) = v_xmm0;
    *(uint64_t *)(result + 0x30) = v_xmm1;
    *(uint64_t *)(result + 0x40) = v_xmm0;
    if ((uint8_t)(v_stack_m738) != 0) {
        result = KdDecodeDataBlock(Arg1, 128, Arg3, Arg4);
        result = v_stack_m6D8;
        local_r10 = v_stack_m598;
        Arg1 = v_stack_m734;
        *(uint64_t *)(v_rip + 0x96FE2D) = result;
        result = v_stack_m728;
        *(uint8_t *)(v_rip + 0x96FE32) = (uint8_t)(Arg1);
        Arg1 = v_rip + 9895435;
        *(uint64_t *)(v_rip + 0x96FE1C) = result;
        *(uint64_t *)(v_rip + 0x96FDFD) = local_r10;
        *(uint64_t *)(v_rip + 0x96FDFE) = v_stack_m6E8;
        *(uint8_t *)(v_rip + 0x96FE10) = 1;
        result = KiBugCheckWriteCrashDump(Arg1, 128, Arg3, Arg4);
    }
    Arg1 = 0;
    result = HvlResumeFromRootCrashdump(Arg1, 128, Arg3, Arg4);
    result = IoSaveBugCheckProgress(99, 128, Arg3, Arg4);
    if (1 == 0) {
        result = KiScanBugCheckCallbackList(99, 128, Arg3, Arg4);
    }
    result = guard_dispatch_icall(99, 128, Arg3, Arg4);
    result = IoSaveBugCheckProgress(4, 128, Arg3, Arg4);
    if (v_stack_m720 == 0) goto loc_005B37A3;
    Arg1 = 0;
    *(uint8_t *)(v_rip + 0x8B3139) = 1;
    result = KiSendThawExecution(Arg1, 128, Arg3, Arg4);
    result = KiBugcheckUnloadDebugSymbols(Arg1, 128, Arg3, Arg4);
    Arg1 = 0;
    result = guard_dispatch_icall(Arg1, 128, Arg3, Arg4);
    if ((*(uint8_t *)(v_rip + 0x9585AA)) == 0) goto loc_005B3781;
    if ((*(uint8_t *)(v_rip + 0x9585A2)) == 0) goto loc_005B379B;
loc_005B3781:
    if ((*(uint8_t *)(v_rip + 0x95859A)) != 0) goto loc_005B379B;
    if (v_stack_m70E != 0) goto loc_005B379B;
    if ((uint8_t)(v_stack_m72F) == 0) {
        Arg1 = 1;
    }
    result = HalReturnToFirmware(Arg1, 128, Arg3, Arg4);
loc_005B37A3:
    result = KiBugCheckDebugBreak(4, 128, Arg3, Arg4);
    local_rsp = (local_rsp) + (0x748ULL);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `- 0xF0` | `64` | `R` |
| `Arg2` | `+ 0x58` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005B27D0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
