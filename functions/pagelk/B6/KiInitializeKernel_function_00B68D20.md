# KiInitializeKernel

- RVA: `0x00B68D20`–`0x00B69640` (길이 `2,336` bytes)
- VA: `0x0000000140B68D20`
- 실행 섹션: `PAGELK`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CA860`
- 디코드: `522`개 명령, `2,336/2,336` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **46**; 고유 호출 대상: **41**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **31**

### Outgoing calls
- `0x00B68D8A` → [HvlPhase0Initialize](../../page/71/HvlPhase0Initialize_function_00717AC8.md) (function, `0x00717AC8`)
- `0x00B68DED` → [KiSetHardwareSpeculationControlFeatures](../../text/5C/KiSetHardwareSpeculationControlFeatures_function_005C03A8.md) (function, `0x005C03A8`)
- `0x00B68DF5` → [KiCheckMicrocode](../B7/KiCheckMicrocode_function_00B7E648.md) (function, `0x00B7E648`)
- `0x00B68E0A` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00B68E20` → [KiDetectFpuLeakage](../B5/KiDetectFpuLeakage_function_00B5B6A0.md) (function, `0x00B5B6A0`)
- `0x00B68E66` → [KiSetUserTbFlushPending](../../text/6B/KiSetUserTbFlushPending_function_006B20C0.md) (function, `0x006B20C0`)
- `0x00B68E8F` → [KiSetPageAttributesTable](../B7/KiSetPageAttributesTable_function_00B7D7FC.md) (function, `0x00B7D7FC`)
- `0x00B68EFB` → [KiSetUserTbFlushPending](../../text/6B/KiSetUserTbFlushPending_function_006B20C0.md) (function, `0x006B20C0`)
- `0x00B68F27` → [KiConfigureProcessorBlock](KiConfigureProcessorBlock_function_00B663E8.md) (function, `0x00B663E8`)
- `0x00B68F2F` → [KiInitializeTopologyStructures](KiInitializeTopologyStructures_function_00B69708.md) (function, `0x00B69708`)
- `0x00B68F77` → [KeCompactServiceTable](../../text/5B/KeCompactServiceTable_function_005B61AC.md) (function, `0x005B61AC`)
- `0x00B68F96` → [KiSetPageAttributesTable](../B7/KiSetPageAttributesTable_function_00B7D7FC.md) (function, `0x00B7D7FC`)
- `0x00B68F9E` → [KiInitializeTopologyStructures](KiInitializeTopologyStructures_function_00B69708.md) (function, `0x00B69708`)
- `0x00B68FC1` → [KiInitializeCoreControlBlock](../../text/5B/KiInitializeCoreControlBlock_function_005BCB34.md) (function, `0x005BCB34`)
- `0x00B68FCC` → [KiAddProcessorToCoreControlBlock](../../text/5B/KiAddProcessorToCoreControlBlock_function_005BBECC.md) (function, `0x005BBECC`)
- `0x00B68FD1` → [KiSetCacheInformation](KiSetCacheInformation_function_00B69B78.md) (function, `0x00B69B78`)
- `0x00B68FD9` → [PoInitializePrcb](../B7/PoInitializePrcb_function_00B715E4.md) (function, `0x00B715E4`)
- `0x00B6900F` → [RtlGetXSaveFeatureFlags](../../text/5E/RtlGetXSaveFeatureFlags_function_005E6CE0.md) (function, `0x005E6CE0`)
- `0x00B6905F` → [KiSetControlEnforcement](KiSetControlEnforcement_function_00B69F68.md) (function, `0x00B69F68`)
- `0x00B6906C` → [KiCheckEnqueueStoreFeaturePresence](KiCheckEnqueueStoreFeaturePresence_function_00B682E8.md) (function, `0x00B682E8`)
- `0x00B690B9` → [KiLowerIrqlProcessIrqlFlags](../../text/4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x00B690CF` → [KiInitSystem](../../init/C3/KiInitSystem_function_00C38480.md) (function, `0x00C38480`)
- `0x00B6911D` → [HviGetHypervisorFeatures](../../text/66/HviGetHypervisorFeatures_function_00666630.md) (function, `0x00666630`)
- `0x00B69135` → [KiIsKernelCfgActive](../../init/C3/KiIsKernelCfgActive_function_00C36E54.md) (function, `0x00C36E54`)
- `0x00B69142` → [RtlInitKernelModeSpecialMachineFrameEntries](../../init/C4/RtlInitKernelModeSpecialMachineFrameEntries_function_00C4763C.md) (function, `0x00C4763C`)
- `0x00B691BC` → [KeGetTopologyIdForProcessor](../../text/5B/KeGetTopologyIdForProcessor_function_005BBCFC.md) (function, `0x005BBCFC`)
- `0x00B691DF` → [KeGetTopologyIdForProcessor](../../text/5B/KeGetTopologyIdForProcessor_function_005BBCFC.md) (function, `0x005BBCFC`)
- `0x00B69277` → [KiLowerIrqlProcessIrqlFlags](../../text/4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x00B69287` → [HvlEnlightenProcessor](../../text/4D/HvlEnlightenProcessor_function_004DCD9C.md) (function, `0x004DCD9C`)
- `0x00B692A5` → [KiEnableXSave](../B5/KiEnableXSave_function_00B5B128.md) (function, `0x00B5B128`)
- `0x00B694A1` → [Feature_Test57481295__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_Test57481295__private_IsEnabledDeviceUsageNoInline_function_004F7B90.md) (function, `0x004F7B90`)
- `0x00B694EF` → [KiInitializeAndStartInitialThread](../../text/5C/KiInitializeAndStartInitialThread_function_005C42A4.md) (function, `0x005C42A4`)
- `0x00B694FE` → [KiStartIdleThread](../../text/5C/KiStartIdleThread_function_005C46B0.md) (function, `0x005C46B0`)
- `0x00B69510` → [KiStartPrcbThreads](../../text/5B/KiStartPrcbThreads_function_005B8648.md) (function, `0x005B8648`)
- `0x00B6951E` → [InitBootProcessor](../../init/C1/InitBootProcessor_function_00C1B1C8.md) (function, `0x00C1B1C8`)
- `0x00B69529` → [HalInitSystem](../B5/HalInitSystem_function_00B5B6E0.md) (function, `0x00B5B6E0`)
- `0x00B69537` → [KeBugCheck](../../text/4F/KeBugCheck_function_004FD640.md) (function, `0x004FD640`)
- `0x00B6956B` → [KiConfigureAmdTprLowerInterruptDelayWorkaround](KiConfigureAmdTprLowerInterruptDelayWorkaround_function_00B68374.md) (function, `0x00B68374`)
- `0x00B69579` → [KiCompleteKernelInit](KiCompleteKernelInit_function_00B66090.md) (function, `0x00B66090`)
- `0x00B695A5` → [KiCheckVpBackingLongSpinWaitHypercall](../../text/30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00B695C4` → [KeHaltOnAddress](../../text/4B/KeHaltOnAddress_function_004BD8DC.md) (function, `0x004BD8DC`)
- `0x00B695CD` → [HvlNotifyLongSpinWait](../../text/30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00B695EC` → [KiInitializeProcessorCycleAccumulation](../../text/5B/KiInitializeProcessorCycleAccumulation_function_005B2014.md) (function, `0x005B2014`)
- `0x00B69602` → [KeInitializeClockOtherProcessors](KeInitializeClockOtherProcessors_function_00B678FC.md) (function, `0x00B678FC`)
- `0x00B69612` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00B6963A` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)

### Direct callers
- [KiSystemStartup](../B5/KiSystemStartup_function_00B5B3C0.md) at `0x00B5B63E`

### Static image references
- `0x00B68D32` → RVA `0x00E0A740` (`.data`; read)
- `0x00B68D93` → RVA `0x0100815C` (`INITDATA`; read)
- `0x00B68D9B` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)
- `0x00B68DA7` → RVA `0x00FC5008` (`ALMOSTRO`; read)
- `0x00B68E25` → RVA `0x00FC6E58` (`ALMOSTRO`; write)
- `0x00B68E3E` → RVA `0x00FC6A87` (`ALMOSTRO`; read)
- `0x00B68F4D` → RVA `0x00FC5114` (`ALMOSTRO`; write)
- `0x00B68F53` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x00B68F62` → RVA `0x000DBEC8` (`.rdata`; read)
- `0x00B68F69` → RVA `0x000DBECC` (`.rdata`; read)
- `0x00B68F70` → RVA `0x000DB720` (`.rdata`; read)
- `0x00B68F7E` → RVA `0x00FC6E58` (`ALMOSTRO`; read)
- `0x00B69083` → RVA `0x00FC5078` (`ALMOSTRO`; write)
- `0x00B6908F` → RVA `0x00FC6BE8` (`ALMOSTRO`; write)
- `0x00B6909B` → RVA `0x00FC6BF4` (`ALMOSTRO`; write)
- `0x00B690A2` → RVA `0x00FC6B30` (`ALMOSTRO`; write)
- `0x00B690A9` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x00B690C2` → RVA `0x00FCF2C0` (`CACHEALI`; read/write)
- `0x00B690EF` → RVA `0x00FC6F78` (`ALMOSTRO`; write)
- `0x00B69111` → RVA `0x00FC7250` (`ALMOSTRO`; write)
- `0x00B6912F` → RVA `0x00FC6DC0` (`ALMOSTRO`; write)
- `0x00B6915D` → RVA `0x00FC6B30` (`ALMOSTRO`; read)
- `0x00B691C7` → RVA `0x00FC6A80` (`ALMOSTRO`; read)
- `0x00B6921D` → RVA `0x00FC5114` (`ALMOSTRO`; read)
- `0x00B69231` → RVA `0x00FC8C40` (`ALMOSTRO`; read)
- `0x00B6928C` → RVA `0x00FC6DC0` (`ALMOSTRO`; read)
- `0x00B694BF` → RVA `0x00E66920` (`.data`; read)
- `0x00B6957E` → RVA `0x00FC6E74` (`ALMOSTRO`; read)
- `0x00B69593` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x00B695BD` → RVA `0x00FC6C50` (`ALMOSTRO`; read)
- `0x00B695F1` → RVA `0x00FC6A85` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **30**
  - `0x00B68D8A` → [HvlPhase0Initialize](../../page/71/HvlPhase0Initialize_function_00717AC8.md) (`PAGELK` → `PAGE`)
  - `0x00B68DED` → [KiSetHardwareSpeculationControlFeatures](../../text/5C/KiSetHardwareSpeculationControlFeatures_function_005C03A8.md) (`PAGELK` → `.text`)
  - `0x00B68E0A` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGELK` → `.text`)
  - `0x00B68E66` → [KiSetUserTbFlushPending](../../text/6B/KiSetUserTbFlushPending_function_006B20C0.md) (`PAGELK` → `.text`)
  - `0x00B68EFB` → [KiSetUserTbFlushPending](../../text/6B/KiSetUserTbFlushPending_function_006B20C0.md) (`PAGELK` → `.text`)
  - `0x00B68F77` → [KeCompactServiceTable](../../text/5B/KeCompactServiceTable_function_005B61AC.md) (`PAGELK` → `.text`)
  - `0x00B68FC1` → [KiInitializeCoreControlBlock](../../text/5B/KiInitializeCoreControlBlock_function_005BCB34.md) (`PAGELK` → `.text`)
  - `0x00B68FCC` → [KiAddProcessorToCoreControlBlock](../../text/5B/KiAddProcessorToCoreControlBlock_function_005BBECC.md) (`PAGELK` → `.text`)
  - `0x00B6900F` → [RtlGetXSaveFeatureFlags](../../text/5E/RtlGetXSaveFeatureFlags_function_005E6CE0.md) (`PAGELK` → `.text`)
  - `0x00B690B9` → [KiLowerIrqlProcessIrqlFlags](../../text/4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (`PAGELK` → `.text`)
  - `0x00B690CF` → [KiInitSystem](../../init/C3/KiInitSystem_function_00C38480.md) (`PAGELK` → `INIT`)
  - `0x00B6911D` → [HviGetHypervisorFeatures](../../text/66/HviGetHypervisorFeatures_function_00666630.md) (`PAGELK` → `.text`)
  - `0x00B69135` → [KiIsKernelCfgActive](../../init/C3/KiIsKernelCfgActive_function_00C36E54.md) (`PAGELK` → `INIT`)
  - `0x00B69142` → [RtlInitKernelModeSpecialMachineFrameEntries](../../init/C4/RtlInitKernelModeSpecialMachineFrameEntries_function_00C4763C.md) (`PAGELK` → `INIT`)
  - `0x00B691BC` → [KeGetTopologyIdForProcessor](../../text/5B/KeGetTopologyIdForProcessor_function_005BBCFC.md) (`PAGELK` → `.text`)
  - `0x00B691DF` → [KeGetTopologyIdForProcessor](../../text/5B/KeGetTopologyIdForProcessor_function_005BBCFC.md) (`PAGELK` → `.text`)
  - `0x00B69277` → [KiLowerIrqlProcessIrqlFlags](../../text/4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (`PAGELK` → `.text`)
  - `0x00B69287` → [HvlEnlightenProcessor](../../text/4D/HvlEnlightenProcessor_function_004DCD9C.md) (`PAGELK` → `.text`)
  - `0x00B694A1` → [Feature_Test57481295__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_Test57481295__private_IsEnabledDeviceUsageNoInline_function_004F7B90.md) (`PAGELK` → `.text`)
  - `0x00B694EF` → [KiInitializeAndStartInitialThread](../../text/5C/KiInitializeAndStartInitialThread_function_005C42A4.md) (`PAGELK` → `.text`)
  - `0x00B694FE` → [KiStartIdleThread](../../text/5C/KiStartIdleThread_function_005C46B0.md) (`PAGELK` → `.text`)
  - `0x00B69510` → [KiStartPrcbThreads](../../text/5B/KiStartPrcbThreads_function_005B8648.md) (`PAGELK` → `.text`)
  - `0x00B6951E` → [InitBootProcessor](../../init/C1/InitBootProcessor_function_00C1B1C8.md) (`PAGELK` → `INIT`)
  - `0x00B69537` → [KeBugCheck](../../text/4F/KeBugCheck_function_004FD640.md) (`PAGELK` → `.text`)
  - `0x00B695A5` → [KiCheckVpBackingLongSpinWaitHypercall](../../text/30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (`PAGELK` → `.text`)
  - `0x00B695C4` → [KeHaltOnAddress](../../text/4B/KeHaltOnAddress_function_004BD8DC.md) (`PAGELK` → `.text`)
  - `0x00B695CD` → [HvlNotifyLongSpinWait](../../text/30/HvlNotifyLongSpinWait_function_0030F460.md) (`PAGELK` → `.text`)
  - `0x00B695EC` → [KiInitializeProcessorCycleAccumulation](../../text/5B/KiInitializeProcessorCycleAccumulation_function_005B2014.md) (`PAGELK` → `.text`)
  - `0x00B69612` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGELK` → `.text`)
  - `0x00B6963A` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGELK` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B68D20  40 53                           push rbx
00B68D22  56                              push rsi
00B68D23  41 54                           push r12
00B68D25  41 55                           push r13
00B68D27  41 56                           push r14
00B68D29  41 57                           push r15
00B68D2B  48 81 EC A8 02 00 00            sub rsp, 0x2a8
00B68D32  48 8B 05 07 1A 2A 00            mov rax, qword ptr [rip + 0x2a1a07]
00B68D39  48 33 C4                        xor rax, rsp
00B68D3C  48 89 84 24 90 02 00 00         mov qword ptr [rsp + 0x290], rax
00B68D44  4D 8B F1                        mov r14, r9
00B68D47  4C 89 44 24 38                  mov qword ptr [rsp + 0x38], r8
00B68D4C  48 89 54 24 40                  mov qword ptr [rsp + 0x40], rdx
00B68D51  48 89 4C 24 58                  mov qword ptr [rsp + 0x58], rcx
00B68D56  48 89 54 24 60                  mov qword ptr [rsp + 0x60], rdx
00B68D5B  4C 89 4C 24 68                  mov qword ptr [rsp + 0x68], r9
00B68D60  48 8B 84 24 08 03 00 00         mov rax, qword ptr [rsp + 0x308]
00B68D68  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00B68D6D  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
00B68D72  0F 57 C0                        xorps xmm0, xmm0
00B68D75  0F 11 44 24 78                  movups xmmword ptr [rsp + 0x78], xmm0
00B68D7A  44 8B BC 24 00 03 00 00         mov r15d, dword ptr [rsp + 0x300]
00B68D82  45 85 FF                        test r15d, r15d
00B68D85  75 2F                           jne 0x140b68db6
00B68D87  48 8B C8                        mov rcx, rax
00B68D8A  E8 39 ED BA FF                  call 0x140717ac8
00B68D8F  41 8D 77 01                     lea esi, [r15 + 1]
00B68D93  39 35 C3 F3 49 00               cmp dword ptr [rip + 0x49f3c3], esi
00B68D99  75 20                           jne 0x140b68dbb
00B68D9B  F7 05 13 DD 45 00 00 00 08 00   test dword ptr [rip + 0x45dd13], 0x80000
00B68DA5  74 14                           je 0x140b68dbb
00B68DA7  48 8B 05 5A C2 45 00            mov rax, qword ptr [rip + 0x45c25a]
00B68DAE  89 B0 08 03 00 00               mov dword ptr [rax + 0x308], esi
00B68DB4  EB 05                           jmp 0x140b68dbb
00B68DB6  BE 01 00 00 00                  mov esi, 1
00B68DBB  49 8B 86 A0 8F 00 00            mov rax, qword ptr [r14 + 0x8fa0]
00B68DC2  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00B68DC7  49 8D 86 8D 00 00 00            lea rax, [r14 + 0x8d]
00B68DCE  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00B68DD3  8A 00                           mov al, byte ptr [rax]
00B68DD5  B9 02 00 00 00                  mov ecx, 2
00B68DDA  3A C1                           cmp al, cl
00B68DDC  74 07                           je 0x140b68de5
00B68DDE  40 2A C6                        sub al, sil
00B68DE1  A8 FD                           test al, 0xfd
00B68DE3  75 0D                           jne 0x140b68df2
00B68DE5  48 8B 54 24 30                  mov rdx, qword ptr [rsp + 0x30]
00B68DEA  49 8B CE                        mov rcx, r14
00B68DED  E8 B6 75 A5 FF                  call 0x1405c03a8
00B68DF2  49 8B CE                        mov rcx, r14
00B68DF5  E8 4E 58 01 00                  call 0x140b7e648
00B68DFA  33 D2                           xor edx, edx
00B68DFC  41 B8 00 02 00 00               mov r8d, 0x200
00B68E02  48 8D 8C 24 90 00 00 00         lea rcx, [rsp + 0x90]
00B68E0A  E8 31 DE B5 FF                  call 0x1406c6c40
00B68E0F  0F AE 84 24 90 00 00 00         fxsave [rsp + 0x90]
00B68E17  45 85 FF                        test r15d, r15d
00B68E1A  0F 85 5E 01 00 00               jne 0x140b68f7e
00B68E20  E8 7B 28 FF FF                  call 0x140b5b6a0
00B68E25  89 05 2D E0 45 00               mov dword ptr [rip + 0x45e02d], eax
00B68E2B  85 C0                           test eax, eax
00B68E2D  74 0F                           je 0x140b68e3e
00B68E2F  48 B8 00 00 00 00 00 02 00 00   movabs rax, 0x20000000000
00B68E39  48 09 44 24 30                  or qword ptr [rsp + 0x30], rax
00B68E3E  80 3D 42 DC 45 00 00            cmp byte ptr [rip + 0x45dc42], 0
00B68E45  74 26                           je 0x140b68e6d
00B68E47  0F 20 D8                        mov rax, cr3
00B68E4A  0F 22 D8                        mov cr3, rax
00B68E4D  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00B68E56  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
00B68E5D  80 B9 60 01 00 00 00            cmp byte ptr [rcx + 0x160], 0
00B68E64  75 29                           jne 0x140b68e8f
00B68E66  E8 55 92 B4 FF                  call 0x1406b20c0
00B68E6B  EB 22                           jmp 0x140b68e8f
00B68E6D  0F 20 E1                        mov rcx, cr4
00B68E70  48 F7 C1 80 00 02 00            test rcx, 0x20080
00B68E77  74 10                           je 0x140b68e89
00B68E79  48 8B C1                        mov rax, rcx
00B68E7C  48 0F BA F8 07                  btc rax, 7
00B68E81  0F 22 E0                        mov cr4, rax
00B68E84  0F 22 E1                        mov cr4, rcx
00B68E87  EB 06                           jmp 0x140b68e8f
00B68E89  0F 20 D8                        mov rax, cr3
00B68E8C  0F 22 D8                        mov cr3, rax
00B68E8F  E8 68 49 01 00                  call 0x140b7d7fc
00B68E94  48 B8 80 02 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000280
00B68E9E  80 38 00                        cmp byte ptr [rax], 0
00B68EA1  48 8B 44 24 30                  mov rax, qword ptr [rsp + 0x30]
00B68EA6  74 0A                           je 0x140b68eb2
00B68EA8  B9 00 00 00 80                  mov ecx, 0x80000000
00B68EAD  48 0B C1                        or rax, rcx
00B68EB0  EB 12                           jmp 0x140b68ec4
00B68EB2  48 B9 FF FF FF 7F FF FF FF FF   movabs rcx, 0xffffffff7fffffff
00B68EBC  48 23 C1                        and rax, rcx
00B68EBF  48 0F BA E8 1E                  bts rax, 0x1e
00B68EC4  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00B68EC9  0F 20 E0                        mov rax, cr4
00B68ECC  48 83 C8 18                     or rax, 0x18
00B68ED0  0F 22 E0                        mov cr4, rax
00B68ED3  80 3D AD DB 45 00 00            cmp byte ptr [rip + 0x45dbad], 0
00B68EDA  74 26                           je 0x140b68f02
00B68EDC  0F 20 D8                        mov rax, cr3
00B68EDF  0F 22 D8                        mov cr3, rax
00B68EE2  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00B68EEB  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
00B68EF2  80 B9 60 01 00 00 00            cmp byte ptr [rcx + 0x160], 0
00B68EF9  75 29                           jne 0x140b68f24
00B68EFB  E8 C0 91 B4 FF                  call 0x1406b20c0
00B68F00  EB 22                           jmp 0x140b68f24
00B68F02  0F 20 E1                        mov rcx, cr4
00B68F05  48 F7 C1 80 00 02 00            test rcx, 0x20080
00B68F0C  74 10                           je 0x140b68f1e
00B68F0E  48 8B C1                        mov rax, rcx
00B68F11  48 0F BA F8 07                  btc rax, 7
00B68F16  0F 22 E0                        mov cr4, rax
00B68F19  0F 22 E1                        mov cr4, rcx
00B68F1C  EB 06                           jmp 0x140b68f24
00B68F1E  0F 20 D8                        mov rax, cr3
00B68F21  0F 22 D8                        mov cr3, rax
00B68F24  49 8B CE                        mov rcx, r14
00B68F27  E8 BC D4 FF FF                  call 0x140b663e8
00B68F2C  49 8B CE                        mov rcx, r14
00B68F2F  E8 D4 07 00 00                  call 0x140b69708
00B68F34  41 BC BF FF 00 00               mov r12d, 0xffbf
00B68F3A  41 8B C4                        mov eax, r12d
00B68F3D  83 BC 24 AC 00 00 00 00         cmp dword ptr [rsp + 0xac], 0
00B68F45  0F 45 84 24 AC 00 00 00         cmovne eax, dword ptr [rsp + 0xac]
00B68F4D  89 05 C1 C1 45 00               mov dword ptr [rip + 0x45c1c1], eax
00B68F53  4C 8D 2D A6 70 49 FF            lea r13, [rip - 0xb68f5a]
00B68F5A  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
00B68F5F  45 33 C9                        xor r9d, r9d
00B68F62  44 8B 05 5F 2F 57 FF            mov r8d, dword ptr [rip - 0xa8d0a1]
00B68F69  48 8D 15 5C 2F 57 FF            lea rdx, [rip - 0xa8d0a4]
00B68F70  48 8D 0D A9 27 57 FF            lea rcx, [rip - 0xa8d857]
00B68F77  E8 30 D2 A4 FF                  call 0x1405b61ac
00B68F7C  EB 32                           jmp 0x140b68fb0
00B68F7E  83 3D D3 DE 45 00 00            cmp dword ptr [rip + 0x45ded3], 0
00B68F85  74 0F                           je 0x140b68f96
00B68F87  48 B8 00 00 00 00 00 02 00 00   movabs rax, 0x20000000000
00B68F91  48 09 44 24 30                  or qword ptr [rsp + 0x30], rax
00B68F96  E8 61 48 01 00                  call 0x140b7d7fc
00B68F9B  49 8B CE                        mov rcx, r14
00B68F9E  E8 65 07 00 00                  call 0x140b69708
00B68FA3  41 BC BF FF 00 00               mov r12d, 0xffbf
00B68FA9  4C 8D 2D 50 70 49 FF            lea r13, [rip - 0xb68fb0]
00B68FB0  49 8D 9E 18 A1 00 00            lea rbx, [r14 + 0xa118]
00B68FB7  49 8D 96 C0 AE 00 00            lea rdx, [r14 + 0xaec0]
00B68FBE  48 8B CB                        mov rcx, rbx
00B68FC1  E8 6E 3B A5 FF                  call 0x1405bcb34
00B68FC6  49 8B D6                        mov rdx, r14
00B68FC9  48 8B CB                        mov rcx, rbx
00B68FCC  E8 FB 2E A5 FF                  call 0x1405bbecc
00B68FD1  E8 A2 0B 00 00                  call 0x140b69b78
00B68FD6  49 8B CE                        mov rcx, r14
00B68FD9  E8 06 86 00 00                  call 0x140b715e4
00B68FDE  49 83 A6 98 8E 00 00 00         and qword ptr [r14 + 0x8e98], 0
00B68FE6  49 8D 86 A0 8E 00 00            lea rax, [r14 + 0x8ea0]
00B68FED  48 89 00                        mov qword ptr [rax], rax
00B68FF0  48 B8 D8 03 00 00 80 F7 FF FF   movabs rax, 0xfffff780000003d8
00B68FFA  48 83 38 00                     cmp qword ptr [rax], 0
00B68FFE  74 57                           je 0x140b69057
00B69000  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00B69005  48 0F BA EB 17                  bts rbx, 0x17
00B6900A  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
00B6900F  E8 CC DC A7 FF                  call 0x1405e6ce0
00B69014  48 8B CB                        mov rcx, rbx
00B69017  A8 08                           test al, 8
00B69019  74 0D                           je 0x140b69028
00B6901B  48 0F BA EB 0F                  bts rbx, 0xf
00B69020  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
00B69025  48 8B CB                        mov rcx, rbx
00B69028  A8 10                           test al, 0x10
00B6902A  74 15                           je 0x140b69041
00B6902C  48 BA 00 00 00 00 40 00 00 00   movabs rdx, 0x4000000000
00B69036  48 8B CB                        mov rcx, rbx
00B69039  48 0B CA                        or rcx, rdx
00B6903C  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
00B69041  A8 40                           test al, 0x40
00B69043  74 12                           je 0x140b69057
00B69045  48 B8 00 00 00 00 00 00 80 00   movabs rax, 0x80000000000000
00B6904F  48 0B C8                        or rcx, rax
00B69052  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
00B69057  48 8D 54 24 30                  lea rdx, [rsp + 0x30]
00B6905C  49 8B CE                        mov rcx, r14
00B6905F  E8 04 0F 00 00                  call 0x140b69f68
00B69064  48 8D 54 24 30                  lea rdx, [rsp + 0x30]
00B69069  49 8B CE                        mov rcx, r14
00B6906C  E8 77 F2 FF FF                  call 0x140b682e8
00B69071  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00B69076  45 85 FF                        test r15d, r15d
00B69079  0F 85 CD 00 00 00               jne 0x140b6914c
00B6907F  41 8D 47 09                     lea eax, [r15 + 9]
00B69083  66 89 05 EE BF 45 00            mov word ptr [rip + 0x45bfee], ax
00B6908A  41 0F BE 46 40                  movsx eax, byte ptr [r14 + 0x40]
00B6908F  66 89 05 52 DB 45 00            mov word ptr [rip + 0x45db52], ax
00B69096  41 0F B7 46 42                  movzx eax, word ptr [r14 + 0x42]
00B6909B  66 89 05 52 DB 45 00            mov word ptr [rip + 0x45db52], ax
00B690A2  48 89 1D 87 DA 45 00            mov qword ptr [rip + 0x45da87], rbx
00B690A9  44 39 3D 70 DC 45 00            cmp dword ptr [rip + 0x45dc70], r15d
00B690B0  74 0C                           je 0x140b690be
00B690B2  44 0F 20 C1                     mov rcx, cr8
00B690B6  40 8A D6                        mov dl, sil
00B690B9  E8 DA C5 98 FF                  call 0x1404f5698
00B690BE  44 0F 22 C6                     mov cr8, rsi
00B690C2  48 83 25 F6 61 46 00 00         and qword ptr [rip + 0x4661f6], 0
00B690CA  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00B690CF  E8 AC F3 0C 00                  call 0x140c38480
00B690D4  0F 31                           rdtsc
00B690D6  48 C1 E2 20                     shl rdx, 0x20
00B690DA  48 0B C2                        or rax, rdx
00B690DD  8B C8                           mov ecx, eax
00B690DF  83 E1 0F                        and ecx, 0xf
00B690E2  48 8B D0                        mov rdx, rax
00B690E5  48 C1 C2 2B                     rol rdx, 0x2b
00B690E9  48 33 D0                        xor rdx, rax
00B690EC  48 D3 CA                        ror rdx, cl
00B690EF  48 89 15 82 DE 45 00            mov qword ptr [rip + 0x45de82], rdx
00B690F6  0F 31                           rdtsc
00B690F8  48 C1 E2 20                     shl rdx, 0x20
00B690FC  48 0B C2                        or rax, rdx
00B690FF  8B C8                           mov ecx, eax
00B69101  83 E1 0F                        and ecx, 0xf
00B69104  48 8B D0                        mov rdx, rax
00B69107  48 C1 CA 2F                     ror rdx, 0x2f
00B6910B  48 33 C2                        xor rax, rdx
00B6910E  48 D3 C0                        rol rax, cl
00B69111  48 89 05 38 E1 45 00            mov qword ptr [rip + 0x45e138], rax
00B69118  48 8D 4C 24 78                  lea rcx, [rsp + 0x78]
00B6911D  E8 0E D5 AF FF                  call 0x140666630
00B69122  F7 84 24 84 00 00 00 00 10 00 00  test dword ptr [rsp + 0x84], 0x1000
00B6912D  74 06                           je 0x140b69135
00B6912F  89 35 8B DC 45 00               mov dword ptr [rip + 0x45dc8b], esi
00B69135  E8 1A DD 0C 00                  call 0x140c36e54
00B6913A  85 C0                           test eax, eax
00B6913C  0F 84 4A 01 00 00               je 0x140b6928c
00B69142  E8 F5 E4 0D 00                  call 0x140c4763c
00B69147  E9 40 01 00 00                  jmp 0x140b6928c
00B6914C  83 BC 24 AC 00 00 00 00         cmp dword ptr [rsp + 0xac], 0
00B69154  44 0F 45 A4 24 AC 00 00 00      cmovne r12d, dword ptr [rsp + 0xac]
00B6915D  4C 8B 05 CC D9 45 00            mov r8, qword ptr [rip + 0x45d9cc]
00B69164  48 B8 FF FF FF 3F FF FF FF FF   movabs rax, 0xffffffff3fffffff
00B6916E  4C 23 C0                        and r8, rax
00B69171  48 8B CB                        mov rcx, rbx
00B69174  81 E1 00 00 00 08               and ecx, 0x8000000
00B6917A  49 8B C0                        mov rax, r8
00B6917D  48 0F BA F0 1B                  btr rax, 0x1b
00B69182  49 0F BA E8 1B                  bts r8, 0x1b
00B69187  48 85 C9                        test rcx, rcx
00B6918A  4C 0F 44 C0                     cmove r8, rax
00B6918E  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
00B69193  BA 02 00 00 00                  mov edx, 2
00B69198  38 10                           cmp byte ptr [rax], dl
00B6919A  75 78                           jne 0x140b69214
00B6919C  41 80 7E 40 06                  cmp byte ptr [r14 + 0x40], 6
00B691A1  75 71                           jne 0x140b69214
00B691A3  41 80 7E 43 17                  cmp byte ptr [r14 + 0x43], 0x17
00B691A8  75 6A                           jne 0x140b69214
00B691AA  41 80 7E 42 0A                  cmp byte ptr [r14 + 0x42], 0xa
00B691AF  75 63                           jne 0x140b69214
00B691B1  4D 8B D6                        mov r10, r14
00B691B4  BA 04 00 00 00                  mov edx, 4
00B691B9  49 8B CE                        mov rcx, r14
00B691BC  E8 3B 2B A5 FF                  call 0x1405bbcfc
00B691C1  44 8B D8                        mov r11d, eax
00B691C4  45 33 C9                        xor r9d, r9d
00B691C7  8B 0D B3 D8 45 00               mov ecx, dword ptr [rip + 0x45d8b3]
00B691CD  44 3B C9                        cmp r9d, ecx
00B691D0  73 1F                           jae 0x140b691f1
00B691D2  4B 8B 8C CD 40 8C FC 00         mov rcx, qword ptr [r13 + r9*8 + 0xfc8c40]
00B691DA  BA 04 00 00 00                  mov edx, 4
00B691DF  E8 18 2B A5 FF                  call 0x1405bbcfc
00B691E4  44 3B D8                        cmp r11d, eax
00B691E7  74 05                           je 0x140b691ee
00B691E9  44 03 CE                        add r9d, esi
00B691EC  EB D9                           jmp 0x140b691c7
00B691EE  4C 8B D1                        mov r10, rcx
00B691F1  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00B691F6  48 0F BA F3 14                  btr rbx, 0x14
00B691FB  41 8B 82 A0 8F 00 00            mov eax, dword ptr [r10 + 0x8fa0]
00B69202  B9 00 00 10 00                  mov ecx, 0x100000
00B69207  BA 02 00 00 00                  mov edx, 2
00B6920C  48 85 C1                        test rcx, rax
00B6920F  74 03                           je 0x140b69214
00B69211  48 0B D9                        or rbx, rcx
00B69214  49 3B D8                        cmp rbx, r8
00B69217  0F 85 0D 04 00 00               jne 0x140b6962a
00B6921D  44 3B 25 F0 BE 45 00            cmp r12d, dword ptr [rip + 0x45bef0]
00B69224  0F 85 00 04 00 00               jne 0x140b6962a
00B6922A  41 8B 86 E8 00 00 00            mov eax, dword ptr [r14 + 0xe8]
00B69231  48 8B 0D 08 FA 45 00            mov rcx, qword ptr [rip + 0x45fa08]
00B69238  39 81 E8 00 00 00               cmp dword ptr [rcx + 0xe8], eax
00B6923E  0F 85 E6 03 00 00               jne 0x140b6962a
00B69244  41 8B 86 A0 00 00 00            mov eax, dword ptr [r14 + 0xa0]
00B6924B  39 81 A0 00 00 00               cmp dword ptr [rcx + 0xa0], eax
00B69251  0F 85 D3 03 00 00               jne 0x140b6962a
00B69257  41 8B 86 A4 00 00 00            mov eax, dword ptr [r14 + 0xa4]
00B6925E  39 81 A4 00 00 00               cmp dword ptr [rcx + 0xa4], eax
00B69264  0F 85 C0 03 00 00               jne 0x140b6962a
00B6926A  83 3D AF DA 45 00 00            cmp dword ptr [rip + 0x45daaf], 0
00B69271  74 09                           je 0x140b6927c
00B69273  44 0F 20 C1                     mov rcx, cr8
00B69277  E8 1C C4 98 FF                  call 0x1404f5698
00B6927C  B8 02 00 00 00                  mov eax, 2
00B69281  44 0F 22 C0                     mov cr8, rax
00B69285  33 C9                           xor ecx, ecx
00B69287  E8 10 3B 97 FF                  call 0x1404dcd9c
00B6928C  83 3D 2D DB 45 00 00            cmp dword ptr [rip + 0x45db2d], 0
00B69293  74 0E                           je 0x140b692a3
00B69295  B8 0F 00 00 00                  mov eax, 0xf
00B6929A  33 D2                           xor edx, edx
00B6929C  B9 40 00 00 40                  mov ecx, 0x40000040
00B692A1  0F 30                           wrmsr
00B692A3  33 C9                           xor ecx, ecx
00B692A5  E8 7E 1E FF FF                  call 0x140b5b128
00B692AA  4C 8B 0D 57 BD 45 00            mov r9, qword ptr [rip + 0x45bd57]
00B692B1  49 C7 81 F8 02 00 00 C3 00 00 00  mov qword ptr [r9 + 0x2f8], 0xc3
00B692BC  48 8B 05 45 BD 45 00            mov rax, qword ptr [rip + 0x45bd45]
00B692C3  40 88 B0 76 02 00 00            mov byte ptr [rax + 0x276], sil
00B692CA  48 8B 05 37 BD 45 00            mov rax, qword ptr [rip + 0x45bd37]
00B692D1  40 88 B0 77 02 00 00            mov byte ptr [rax + 0x277], sil
00B692D8  48 8B 05 29 BD 45 00            mov rax, qword ptr [rip + 0x45bd29]
00B692DF  40 88 B0 7A 02 00 00            mov byte ptr [rax + 0x27a], sil
00B692E6  48 8B 05 1B BD 45 00            mov rax, qword ptr [rip + 0x45bd1b]
00B692ED  40 88 B0 7C 02 00 00            mov byte ptr [rax + 0x27c], sil
00B692F4  48 8B 05 0D BD 45 00            mov rax, qword ptr [rip + 0x45bd0d]
00B692FB  40 88 B0 7D 02 00 00            mov byte ptr [rax + 0x27d], sil
00B69302  48 8B 05 FF BC 45 00            mov rax, qword ptr [rip + 0x45bcff]
00B69309  40 88 B0 7E 02 00 00            mov byte ptr [rax + 0x27e], sil
00B69310  48 8B 05 F1 BC 45 00            mov rax, qword ptr [rip + 0x45bcf1]
00B69317  40 88 B0 82 02 00 00            mov byte ptr [rax + 0x282], sil
00B6931E  48 0F BA E3 13                  bt rbx, 0x13
00B69323  73 0E                           jae 0x140b69333
00B69325  48 8B 05 DC BC 45 00            mov rax, qword ptr [rip + 0x45bcdc]
00B6932C  40 88 B0 81 02 00 00            mov byte ptr [rax + 0x281], sil
00B69333  48 0F BA E3 0E                  bt rbx, 0xe
00B69338  73 0E                           jae 0x140b69348
00B6933A  48 8B 05 C7 BC 45 00            mov rax, qword ptr [rip + 0x45bcc7]
00B69341  40 88 B0 7B 02 00 00            mov byte ptr [rax + 0x27b], sil
00B69348  48 0F BA E3 17                  bt rbx, 0x17
00B6934D  73 0E                           jae 0x140b6935d
00B6934F  48 8B 05 B2 BC 45 00            mov rax, qword ptr [rip + 0x45bcb2]
00B69356  40 88 B0 85 02 00 00            mov byte ptr [rax + 0x285], sil
00B6935D  48 0F BA E3 1C                  bt rbx, 0x1c
00B69362  73 0E                           jae 0x140b69372
00B69364  48 8B 05 9D BC 45 00            mov rax, qword ptr [rip + 0x45bc9d]
00B6936B  40 88 B0 8A 02 00 00            mov byte ptr [rax + 0x28a], sil
00B69372  48 0F BA E3 1A                  bt rbx, 0x1a
00B69377  73 0E                           jae 0x140b69387
00B69379  48 8B 05 88 BC 45 00            mov rax, qword ptr [rip + 0x45bc88]
00B69380  40 88 B0 88 02 00 00            mov byte ptr [rax + 0x288], sil
00B69387  48 0F BA E3 1B                  bt rbx, 0x1b
00B6938C  73 0E                           jae 0x140b6939c
00B6938E  48 8B 05 73 BC 45 00            mov rax, qword ptr [rip + 0x45bc73]
00B69395  40 88 B0 89 02 00 00            mov byte ptr [rax + 0x289], sil
00B6939C  48 0F BA E3 20                  bt rbx, 0x20
00B693A1  73 0E                           jae 0x140b693b1
00B693A3  48 8B 05 5E BC 45 00            mov rax, qword ptr [rip + 0x45bc5e]
00B693AA  40 88 B0 90 02 00 00            mov byte ptr [rax + 0x290], sil
00B693B1  48 0F BA E3 22                  bt rbx, 0x22
00B693B6  73 0E                           jae 0x140b693c6
00B693B8  48 8B 05 49 BC 45 00            mov rax, qword ptr [rip + 0x45bc49]
00B693BF  40 88 B0 94 02 00 00            mov byte ptr [rax + 0x294], sil
00B693C6  48 0F BA E3 2F                  bt rbx, 0x2f
00B693CB  73 0E                           jae 0x140b693db
00B693CD  48 8B 05 34 BC 45 00            mov rax, qword ptr [rip + 0x45bc34]
00B693D4  40 88 B0 98 02 00 00            mov byte ptr [rax + 0x298], sil
00B693DB  48 0F BA E3 30                  bt rbx, 0x30
00B693E0  73 0E                           jae 0x140b693f0
00B693E2  48 8B 05 1F BC 45 00            mov rax, qword ptr [rip + 0x45bc1f]
00B693E9  40 88 B0 99 02 00 00            mov byte ptr [rax + 0x299], sil
00B693F0  48 0F BA E3 31                  bt rbx, 0x31
00B693F5  73 0E                           jae 0x140b69405
00B693F7  48 8B 05 0A BC 45 00            mov rax, qword ptr [rip + 0x45bc0a]
00B693FE  40 88 B0 9A 02 00 00            mov byte ptr [rax + 0x29a], sil
00B69405  48 BA D8 03 00 00 80 F7 FF FF   movabs rdx, 0xfffff780000003d8
00B6940F  F6 02 04                        test byte ptr [rdx], 4
00B69412  0F 95 C1                        setne cl
00B69415  48 0F BA E3 32                  bt rbx, 0x32
00B6941A  0F 92 C0                        setb al
00B6941D  84 C8                           test al, cl
00B6941F  74 0E                           je 0x140b6942f
00B69421  48 8B 05 E0 BB 45 00            mov rax, qword ptr [rip + 0x45bbe0]
00B69428  40 88 B0 9B 02 00 00            mov byte ptr [rax + 0x29b], sil
00B6942F  F6 02 04                        test byte ptr [rdx], 4
00B69432  0F 95 C1                        setne cl
00B69435  48 0F BA E3 33                  bt rbx, 0x33
00B6943A  0F 92 C0                        setb al
00B6943D  84 C8                           test al, cl
00B6943F  74 0E                           je 0x140b6944f
00B69441  48 8B 05 C0 BB 45 00            mov rax, qword ptr [rip + 0x45bbc0]
00B69448  40 88 B0 9C 02 00 00            mov byte ptr [rax + 0x29c], sil
00B6944F  A0 D8 03 00 00 80 F7 FF FF      movabs al, byte ptr [0xfffff780000003d8]
00B69458  A8 E0                           test al, 0xe0
00B6945A  0F 95 C1                        setne cl
00B6945D  48 0F BA E3 34                  bt rbx, 0x34
00B69462  0F 92 C0                        setb al
00B69465  84 C8                           test al, cl
00B69467  74 0E                           je 0x140b69477
00B69469  48 8B 05 98 BB 45 00            mov rax, qword ptr [rip + 0x45bb98]
00B69470  40 88 B0 9D 02 00 00            mov byte ptr [rax + 0x29d], sil
00B69477  48 0F BA E3 36                  bt rbx, 0x36
00B6947C  73 0E                           jae 0x140b6948c
00B6947E  48 8B 05 83 BB 45 00            mov rax, qword ptr [rip + 0x45bb83]
00B69485  40 88 B0 9E 02 00 00            mov byte ptr [rax + 0x29e], sil
00B6948C  48 0F BA E3 39                  bt rbx, 0x39
00B69491  73 0E                           jae 0x140b694a1
00B69493  48 8B 05 6E BB 45 00            mov rax, qword ptr [rip + 0x45bb6e]
00B6949A  40 88 B0 B0 02 00 00            mov byte ptr [rax + 0x2b0], sil
00B694A1  E8 EA E6 98 FF                  call 0x1404f7b90
00B694A6  85 C0                           test eax, eax
00B694A8  74 15                           je 0x140b694bf
00B694AA  48 0F BA E3 3A                  bt rbx, 0x3a
00B694AF  73 0E                           jae 0x140b694bf
00B694B1  48 8B 05 50 BB 45 00            mov rax, qword ptr [rip + 0x45bb50]
00B694B8  40 88 B0 B1 02 00 00            mov byte ptr [rax + 0x2b1], sil
00B694BF  8A 0D 5B D4 2F 00               mov cl, byte ptr [rip + 0x2fd45b]
00B694C5  48 8B 05 3C BB 45 00            mov rax, qword ptr [rip + 0x45bb3c]
00B694CC  88 88 ED 02 00 00               mov byte ptr [rax + 0x2ed], cl
00B694D2  4C 8B 64 24 40                  mov r12, qword ptr [rsp + 0x40]
00B694D7  49 8B CC                        mov rcx, r12
00B694DA  45 85 FF                        test r15d, r15d
00B694DD  75 17                           jne 0x140b694f6
00B694DF  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
00B694E4  4C 8B CB                        mov r9, rbx
00B694E7  4D 8B C6                        mov r8, r14
00B694EA  48 8B 54 24 38                  mov rdx, qword ptr [rsp + 0x38]
00B694EF  E8 B0 AD A5 FF                  call 0x1405c42a4
00B694F4  EB 12                           jmp 0x140b69508
00B694F6  4C 8B 44 24 38                  mov r8, qword ptr [rsp + 0x38]
00B694FB  49 8B D6                        mov rdx, r14
00B694FE  E8 AD B1 A5 FF                  call 0x1405c46b0
00B69503  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
00B69508  45 85 FF                        test r15d, r15d
00B6950B  74 09                           je 0x140b69516
00B6950D  49 8B CE                        mov rcx, r14
00B69510  E8 33 F1 A4 FF                  call 0x1405b8648
00B69515  90                              nop
00B69516  45 85 FF                        test r15d, r15d
00B69519  75 0A                           jne 0x140b69525
00B6951B  48 8B CB                        mov rcx, rbx
00B6951E  E8 A5 1C 0B 00                  call 0x140c1b1c8
00B69523  EB 18                           jmp 0x140b6953d
00B69525  33 D2                           xor edx, edx
00B69527  8B CE                           mov ecx, esi
00B69529  E8 B2 21 FF FF                  call 0x140b5b6e0
00B6952E  84 C0                           test al, al
00B69530  75 0B                           jne 0x140b6953d
00B69532  B9 5C 00 00 00                  mov ecx, 0x5c
00B69537  E8 04 41 99 FF                  call 0x1404fd640
00B6953C  CC                              int3
00B6953D  EB 1C                           jmp 0x140b6955b
00B6953F  BE 01 00 00 00                  mov esi, 1
00B69544  44 8B BC 24 00 03 00 00         mov r15d, dword ptr [rsp + 0x300]
00B6954C  4C 8B 64 24 60                  mov r12, qword ptr [rsp + 0x60]
00B69551  4C 8B 74 24 68                  mov r14, qword ptr [rsp + 0x68]
00B69556  48 8B 5C 24 70                  mov rbx, qword ptr [rsp + 0x70]
00B6955B  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
00B69560  40 38 30                        cmp byte ptr [rax], sil
00B69563  75 0B                           jne 0x140b69570
00B69565  41 8B D7                        mov edx, r15d
00B69568  49 8B CE                        mov rcx, r14
00B6956B  E8 04 EE FF FF                  call 0x140b68374
00B69570  45 8B C7                        mov r8d, r15d
00B69573  49 8B D4                        mov rdx, r12
00B69576  49 8B CE                        mov rcx, r14
00B69579  E8 12 CB FF FF                  call 0x140b66090
00B6957E  44 8B 25 EF D8 45 00            mov r12d, dword ptr [rip + 0x45d8ef]
00B69585  48 83 A3 88 00 00 00 00         and qword ptr [rbx + 0x88], 0
00B6958D  33 DB                           xor ebx, ebx
00B6958F  EB 45                           jmp 0x140b695d6
00B69591  03 DE                           add ebx, esi
00B69593  85 1D 13 BD 45 00               test dword ptr [rip + 0x45bd13], ebx
00B69599  75 39                           jne 0x140b695d4
00B6959B  8B 05 17 D5 45 00               mov eax, dword ptr [rip + 0x45d517]
00B695A1  A8 40                           test al, 0x40
00B695A3  74 2F                           je 0x140b695d4
00B695A5  E8 E6 5E 7A FF                  call 0x14030f490
00B695AA  84 C0                           test al, al
00B695AC  74 26                           je 0x140b695d4
00B695AE  45 85 E4                        test r12d, r12d
00B695B1  75 18                           jne 0x140b695cb
00B695B3  45 8D 44 24 04                  lea r8d, [r12 + 4]
00B695B8  48 8D 54 24 38                  lea rdx, [rsp + 0x38]
00B695BD  48 8D 0D 8C D6 45 00            lea rcx, [rip + 0x45d68c]
00B695C4  E8 13 43 95 FF                  call 0x1404bd8dc
00B695C9  EB 0B                           jmp 0x140b695d6
00B695CB  8B CB                           mov ecx, ebx
00B695CD  E8 8E 5E 7A FF                  call 0x14030f460
00B695D2  EB 02                           jmp 0x140b695d6
00B695D4  F3 90                           pause
00B695D6  8B 05 74 D6 45 00               mov eax, dword ptr [rip + 0x45d674]
00B695DC  85 C0                           test eax, eax
00B695DE  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
00B695E2  75 AD                           jne 0x140b69591
00B695E4  45 85 FF                        test r15d, r15d
00B695E7  74 08                           je 0x140b695f1
00B695E9  49 8B CE                        mov rcx, r14
00B695EC  E8 23 8A A4 FF                  call 0x1405b2014
00B695F1  80 3D 8D D4 45 00 00            cmp byte ptr [rip + 0x45d48d], 0
00B695F8  74 0D                           je 0x140b69607
00B695FA  45 85 FF                        test r15d, r15d
00B695FD  74 08                           je 0x140b69607
00B695FF  49 8B CE                        mov rcx, r14
00B69602  E8 F5 E2 FF FF                  call 0x140b678fc
00B69607  48 8B 8C 24 90 02 00 00         mov rcx, qword ptr [rsp + 0x290]
00B6960F  48 33 CC                        xor rcx, rsp
00B69612  E8 29 30 B4 FF                  call 0x1406ac640
00B69617  48 81 C4 A8 02 00 00            add rsp, 0x2a8
00B6961E  41 5F                           pop r15
00B69620  41 5E                           pop r14
00B69622  41 5D                           pop r13
00B69624  41 5C                           pop r12
00B69626  5E                              pop rsi
00B69627  5B                              pop rbx
00B69628  C3                              ret
00B69629  CC                              int3
00B6962A  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
00B69630  45 33 C9                        xor r9d, r9d
00B69633  48 8B D3                        mov rdx, rbx
00B69636  41 8D 49 3E                     lea ecx, [r9 + 0x3e]
00B6963A  E8 21 40 99 FF                  call 0x1404fd660
00B6963F  90                              nop
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiInitializeKernel(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned int a5, __int64 a6)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned int v_stack_m22C;
    unsigned __int64 v_stack_m248;
    unsigned int v_stack_m254;
    unsigned __int64 v_stack_m260;
    unsigned __int64 v_stack_m268;
    unsigned __int64 v_stack_m270;
    unsigned __int64 v_stack_m278;
    unsigned __int64 v_stack_m280;
    unsigned __int64 v_stack_m288;
    unsigned __int64 v_stack_m290;
    unsigned __int64 v_stack_m298;
    unsigned __int64 v_stack_m2A0;
    unsigned __int64 v_stack_m2A8;
    unsigned __int64 v_stack_m2B8;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p28;

    v_rsp = (v_rsp) - (680);
    result = (*(unsigned __int64 *)(v_rip + 2759175)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m2A0 = a3;
    v_stack_m298 = a2;
    v_stack_m280 = a1;
    v_stack_m278 = a2;
    v_stack_m270 = a4;
    v_stack_m290 = a6;
    v_stack_m268 = a6;
    v_stack_m260 = v_xmm0;
    if ((unsigned int)((unsigned int)(a5)) != 0) goto loc_00B68DB6;
    result = HvlPhase0Initialize(a6, a2, a3, a4);
    if ((*(unsigned int *)(v_rip + 4846531)) != ((unsigned int)((unsigned int)(a5) + 1))) goto loc_00B68DBB;
    if (((*(unsigned int *)(v_rip + 4578579)) & (0x80000ULL)) == 0) goto loc_00B68DBB;
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 4571738) + 776) = (unsigned int)((unsigned int)(a5) + 1);
    goto loc_00B68DBB;
loc_00B68DB6:
loc_00B68DBB:
    v_stack_m2A8 = *(unsigned __int64 *)(a4 + 36768);
    v_stack_m288 = a4 + 141;
    if (((unsigned __int8)(*(unsigned __int8 *)(a4 + 141))) == 2) goto loc_00B68DE5;
    result = (unsigned __int8)((*(unsigned __int8 *)(a4 + 141)) - (1));
    if ((((unsigned __int8)(result)) & (253)) == 0) {
        a2 = v_stack_m2A8;
        a1 = a4;
        result = KiSetHardwareSpeculationControlFeatures(a1, a2, a3, a4);
    }
    result = KiCheckMicrocode(a4, a2, a3, a4);
    a2 = 0;
    result = memset(v_stack_m248, a2, 512, a4);
    if ((unsigned int)((unsigned int)(a5)) != 0) goto loc_00B68F7E;
    result = KiDetectFpuLeakage(v_stack_m248, a2, 512, a4);
    *(unsigned int *)(v_rip + 4579373) = (unsigned int)(result);
    if ((unsigned int)(result) != 0) {
    }
    if ((*(unsigned __int8 *)(v_rip + 4578370)) == 0) goto loc_00B68E6D;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 352)) != 0) goto loc_00B68E8F;
    result = KiSetUserTbFlushPending(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), a2, 512, a4);
    goto loc_00B68E8F;
loc_00B68E6D:
    if (((v_cr4) & (0x20080ULL)) == 0) goto loc_00B68E89;
    goto loc_00B68E8F;
loc_00B68E89:
loc_00B68E8F:
    result = KiSetPageAttributesTable(v_cr4, a2, 512, a4);
    if ((*(unsigned __int8 *)(result)) == 0) goto loc_00B68EB2;
    result = (v_stack_m2A8) | ((unsigned int)(0x80000000ULL));
    goto loc_00B68EC4;
loc_00B68EB2:
    result = (result) & ((unsigned int)(0x80000000ULL));
loc_00B68EC4:
    v_stack_m2A8 = result;
    result = (v_cr4) | (24);
    if ((*(unsigned __int8 *)(v_rip + 4578221)) == 0) goto loc_00B68F02;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 352)) != 0) goto loc_00B68F24;
    result = KiSetUserTbFlushPending(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), a2, 512, a4);
    goto loc_00B68F24;
loc_00B68F02:
    if (((result) & (0x20080ULL)) == 0) goto loc_00B68F1E;
    goto loc_00B68F24;
loc_00B68F1E:
loc_00B68F24:
    result = KiConfigureProcessorBlock(a4, a2, 512, a4);
    result = KiInitializeTopologyStructures(a4, a2, 512, a4);
    result = (unsigned int)((unsigned int)((unsigned int)(0xFFBFULL)));
    if (v_stack_m22C != 0) { result = v_stack_m22C; }
    *(unsigned int *)(v_rip + 4571585) = (unsigned int)(result);
    v_stack_m2B8 = v_rip - 11964250;
    a4 = 0;
    result = KeCompactServiceTable(v_rip - 11065431, v_rip - 11063460, (unsigned int)(*(unsigned int *)(v_rip - 11063457)), a4);
    goto loc_00B68FB0;
loc_00B68F7E:
    if ((*(unsigned int *)(v_rip + 4579027)) != 0) {
    }
    result = KiSetPageAttributesTable(v_rip - 11065431, v_rip - 11063460, (unsigned int)(*(unsigned int *)(v_rip - 11063457)), a4);
    result = KiInitializeTopologyStructures(0, v_rip - 11063460, (unsigned int)(*(unsigned int *)(v_rip - 11063457)), a4);
loc_00B68FB0:
    result = KiInitializeCoreControlBlock(a4 + 41240, a4 + 44736, (unsigned int)(*(unsigned int *)(v_rip - 11063457)), a4);
    result = KiAddProcessorToCoreControlBlock(a4 + 41240, 0, (unsigned int)(*(unsigned int *)(v_rip - 11063457)), a4);
    result = KiSetCacheInformation(a4 + 41240, 0, (unsigned int)(*(unsigned int *)(v_rip - 11063457)), a4);
    result = PoInitializePrcb(0, 0, (unsigned int)(*(unsigned int *)(v_rip - 11063457)), a4);
    *(unsigned __int64 *)(a4 + 36512) = a4 + 36512;
    if ((*(unsigned __int64 *)(a4 + 36512)) == 0) goto loc_00B69057;
    v_stack_m2A8 = v_stack_m2A8;
    result = RtlGetXSaveFeatureFlags(0, 0, (unsigned int)(*(unsigned int *)(v_rip - 11063457)), a4);
    if ((((unsigned __int8)(result)) & (8)) != 0) {
        v_stack_m2A8 = v_stack_m2A8;
        a1 = v_stack_m2A8;
    }
    if ((((unsigned __int8)(result)) & (16)) != 0) {
        a1 = v_stack_m2A8;
        a1 = (a1) | (0);
        v_stack_m2A8 = a1;
    }
    if ((((unsigned __int8)(result)) & (64)) != 0) {
        a1 = (a1) | (result);
        v_stack_m2A8 = a1;
    }
    result = KiSetControlEnforcement(0, v_stack_m2A8, (unsigned int)(*(unsigned int *)(v_rip - 11063457)), a4);
    result = KiCheckEnqueueStoreFeaturePresence(0, v_stack_m2A8, (unsigned int)(*(unsigned int *)(v_rip - 11063457)), a4);
    if ((unsigned int)((unsigned int)(a5)) != 0) goto loc_00B6914C;
    *(unsigned __int16 *)(v_rip + 4571118) = (unsigned __int16)((unsigned int)(a5) + 9);
    *(unsigned __int16 *)(v_rip + 4578130) = (unsigned __int16)((__int8)(*(unsigned __int8 *)(a4 + 64)));
    *(unsigned __int16 *)(v_rip + 4578130) = (unsigned __int16)(*(unsigned __int16 *)(a4 + 66));
    *(unsigned __int64 *)(v_rip + 4577927) = v_stack_m2A8;
    result = *(unsigned __int16 *)(a4 + 66);
    if ((*(unsigned int *)(v_rip + 4578416)) != ((unsigned int)((unsigned int)(a5)))) {
        a1 = v_cr8;
        a2 = 1;
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, (unsigned int)(*(unsigned int *)(v_rip - 11063457)), a4);
    }
    result = KiInitSystem(v_stack_m280, a2, (unsigned int)(*(unsigned int *)(v_rip - 11063457)), a4);
    a2 = (a2) << (32);
    result = (result) | (a2);
    a1 = (unsigned int)(((unsigned int)((unsigned int)(result))) & (15));
    a2 = (result) ^ (result);
    *(unsigned __int64 *)(v_rip + 4578946) = a2;
    a2 = (a2) << (32);
    result = (result) | (a2);
    a1 = (unsigned int)(((unsigned int)((unsigned int)(result))) & (15));
    result = (result) ^ (result);
    *(unsigned __int64 *)(v_rip + 4579640) = result;
    result = HviGetHypervisorFeatures(v_stack_m260, result, (unsigned int)(*(unsigned int *)(v_rip - 11063457)), a4);
    if (((v_stack_m254) & (0x1000ULL)) != 0) {
        *(unsigned int *)(v_rip + 4578443) = 1;
    }
    result = KiIsKernelCfgActive(v_stack_m260, result, (unsigned int)(*(unsigned int *)(v_rip - 11063457)), a4);
    if ((unsigned int)(result) == 0) goto loc_00B6928C;
    result = RtlInitKernelModeSpecialMachineFrameEntries(v_stack_m260, result, (unsigned int)(*(unsigned int *)(v_rip - 11063457)), a4);
    goto loc_00B6928C;
loc_00B6914C:
    v_r12 = (unsigned int)(0xFFBFULL);
    if (v_stack_m22C != 0) { v_r12 = v_stack_m22C; }
    a3 = (*(unsigned __int64 *)(v_rip + 4577740)) & (result);
    a1 = (unsigned int)((v_stack_m2A8) & (0x8000000ULL));
    if (a1 == 0) { a3 = a3; }
    if ((*(unsigned __int8 *)(v_stack_m288)) != 2) goto loc_00B69214;
    if ((*(unsigned __int8 *)(a4 + 64)) != 6) goto loc_00B69214;
    if ((*(unsigned __int8 *)(a4 + 67)) != 23) goto loc_00B69214;
    if ((*(unsigned __int8 *)(a4 + 66)) != 10) goto loc_00B69214;
    result = KeGetTopologyIdForProcessor(0, 4, a3, a4);
    a4 = 0;
loc_00B691C7:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4577459))))) goto loc_00B691F1;
    result = KeGetTopologyIdForProcessor(*(unsigned __int64 *)(v_rip - 11964336 + a4 * 8 + 16550976), 4, a3, a4);
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == ((unsigned int)(result))) goto loc_00B691EE;
    a4 = (unsigned int)((a4) + (1));
    goto loc_00B691C7;
loc_00B691EE:
loc_00B691F1:
    v_rbx = v_stack_m2A8;
    if ((((unsigned int)(0x100000ULL)) & ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip - 11964336 + a4 * 8 + 16550976) + 36768)))) != 0) {
        v_rbx = (v_stack_m2A8) | ((unsigned int)(0x100000ULL));
    }
    if (v_rbx != a3) goto loc_00B6962A;
    if (((unsigned int)(v_r12)) != (*(unsigned int *)(v_rip + 4570864))) goto loc_00B6962A;
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rip + 4585992) + 232)) != ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 232))))) goto loc_00B6962A;
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rip + 4585992) + 160)) != ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 160))))) goto loc_00B6962A;
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rip + 4585992) + 164)) != ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 164))))) goto loc_00B6962A;
    result = (unsigned int)(*(unsigned int *)(a4 + 164));
    if ((*(unsigned int *)(v_rip + 4577967)) != 0) {
        a1 = 1;
        result = KiLowerIrqlProcessIrqlFlags(a1, 2, a3, a4);
    }
    a1 = 0;
    result = HvlEnlightenProcessor(a1, 2, a3, a4);
loc_00B6928C:
    if ((*(unsigned int *)(v_rip + 4578093)) != 0) {
        result = 15;
        a2 = 0;
        a1 = 0x40000040ULL;
    }
    a1 = 0;
    result = KiEnableXSave(a1, a2, a3, a4);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4570455) + 760) = 195;
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 4570437) + 630) = 1;
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 4570423) + 631) = 1;
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 4570409) + 634) = 1;
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 4570395) + 636) = 1;
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 4570381) + 637) = 1;
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 4570367) + 638) = 1;
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 4570353) + 642) = 1;
    result = *(unsigned __int64 *)(v_rip + 4570353);
    if (!(condition_is_above_or_equal)) {
        result = *(unsigned __int64 *)(v_rip + 4570332);
        *(unsigned __int8 *)(result + 641) = 1;
    }
    if (!(condition_is_above_or_equal)) {
        result = *(unsigned __int64 *)(v_rip + 4570311);
        *(unsigned __int8 *)(result + 635) = 1;
    }
    if (!(condition_is_above_or_equal)) {
        result = *(unsigned __int64 *)(v_rip + 4570290);
        *(unsigned __int8 *)(result + 645) = 1;
    }
    if (!(condition_is_above_or_equal)) {
        result = *(unsigned __int64 *)(v_rip + 4570269);
        *(unsigned __int8 *)(result + 650) = 1;
    }
    if (!(condition_is_above_or_equal)) {
        result = *(unsigned __int64 *)(v_rip + 4570248);
        *(unsigned __int8 *)(result + 648) = 1;
    }
    if (!(condition_is_above_or_equal)) {
        result = *(unsigned __int64 *)(v_rip + 4570227);
        *(unsigned __int8 *)(result + 649) = 1;
    }
    if (!(condition_is_above_or_equal)) {
        result = *(unsigned __int64 *)(v_rip + 4570206);
        *(unsigned __int8 *)(result + 656) = 1;
    }
    if (!(condition_is_above_or_equal)) {
        result = *(unsigned __int64 *)(v_rip + 4570185);
        *(unsigned __int8 *)(result + 660) = 1;
    }
    if (!(condition_is_above_or_equal)) {
        result = *(unsigned __int64 *)(v_rip + 4570164);
        *(unsigned __int8 *)(result + 664) = 1;
    }
    if (!(condition_is_above_or_equal)) {
        result = *(unsigned __int64 *)(v_rip + 4570143);
        *(unsigned __int8 *)(result + 665) = 1;
    }
    if (!(condition_is_above_or_equal)) {
        result = *(unsigned __int64 *)(v_rip + 4570122);
        *(unsigned __int8 *)(result + 666) = 1;
    }
    a1 = (((*(unsigned __int8 *)(a2)) & (4)) != 0) ? 1 : 0;
    result = (condition_is_below) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) != 0) {
        result = *(unsigned __int64 *)(v_rip + 4570080);
        *(unsigned __int8 *)(result + 667) = 1;
    }
    a1 = (((*(unsigned __int8 *)(a2)) & (4)) != 0) ? 1 : 0;
    result = (condition_is_below) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) != 0) {
        result = *(unsigned __int64 *)(v_rip + 4570048);
        *(unsigned __int8 *)(result + 668) = 1;
    }
    a1 = ((((unsigned __int8)(result)) & (224)) != 0) ? 1 : 0;
    result = (condition_is_below) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) != 0) {
        result = *(unsigned __int64 *)(v_rip + 4570008);
        *(unsigned __int8 *)(result + 669) = 1;
    }
    if (!(condition_is_above_or_equal)) {
        result = *(unsigned __int64 *)(v_rip + 4569987);
        *(unsigned __int8 *)(result + 670) = 1;
    }
    if (!(condition_is_above_or_equal)) {
        result = *(unsigned __int64 *)(v_rip + 4569966);
        *(unsigned __int8 *)(result + 688) = 1;
    }
    result = Feature_Test57481295__private_IsEnabledDeviceUsageNoInline(a1, a2, a3, *(unsigned __int64 *)(v_rip + 4570455));
    if ((unsigned int)(result) == 0) goto loc_00B694BF;
    if (!(condition_is_above_or_equal)) {
        result = *(unsigned __int64 *)(v_rip + 4569936);
        *(unsigned __int8 *)(result + 689) = 1;
    }
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 4569916) + 749) = (unsigned __int8)(*(unsigned __int8 *)(v_rip + 3134555));
    if ((unsigned int)((unsigned int)(a5)) != 0) goto loc_00B694F6;
    result = KiInitializeAndStartInitialThread(v_stack_m298, v_stack_m2A0, a4, v_stack_m290);
    goto loc_00B69508;
loc_00B694F6:
    result = KiStartIdleThread(v_stack_m298, a4, v_stack_m2A0, v_stack_m290);
loc_00B69508:
    if ((unsigned int)((unsigned int)(a5)) != 0) {
        a1 = a4;
        result = KiStartPrcbThreads(a1, a4, v_stack_m2A0, v_stack_m290);
    }
    if ((unsigned int)((unsigned int)(a5)) != 0) goto loc_00B69525;
    result = InitBootProcessor(v_stack_m290, a4, v_stack_m2A0, v_stack_m290);
    goto loc_00B6953D;
loc_00B69525:
    a2 = 0;
    result = HalInitSystem(1, a2, v_stack_m2A0, v_stack_m290);
    if ((unsigned __int8)(result) == 0) {
        a1 = 92;
        result = KeBugCheck(a1, a2, v_stack_m2A0, v_stack_m290);
    }
    goto loc_00B6955B;
loc_00B6955B:
    result = v_stack_m288;
    if ((*(unsigned __int8 *)(v_stack_m288)) == 1) {
        a2 = (unsigned int)((unsigned int)(a5));
        a1 = a4;
        result = KiConfigureAmdTprLowerInterruptDelayWorkaround(a1, a2, v_stack_m2A0, v_stack_m290);
    }
    result = KiCompleteKernelInit(a4, v_stack_m298, (unsigned int)((unsigned int)((unsigned int)(a5))), v_stack_m290);
    v_rbx = 0;
    goto loc_00B695D6;
loc_00B69591:
    v_rbx = (unsigned int)((v_rbx) + (1));
    if (((*(unsigned int *)(v_rip + 4570387)) & ((unsigned int)(v_rbx))) != 0) goto loc_00B695D4;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 4576535)))) & (64)) == 0) goto loc_00B695D4;
    result = KiCheckVpBackingLongSpinWaitHypercall(a4, v_stack_m298, (unsigned int)((unsigned int)((unsigned int)(a5))), v_stack_m290);
    if ((unsigned __int8)(result) == 0) goto loc_00B695D4;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4577519))) != 0) goto loc_00B695CB;
    result = KeHaltOnAddress(v_rip + 4576908, v_stack_m2A0, (unsigned int)(*(unsigned int *)(v_rip + 4577519)) + 4, v_stack_m290);
    goto loc_00B695D6;
loc_00B695CB:
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rbx)), v_stack_m2A0, (unsigned int)(*(unsigned int *)(v_rip + 4577519)) + 4, v_stack_m290);
    goto loc_00B695D6;
loc_00B695D4:
loc_00B695D6:
    v_stack_m2A0 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4576884)));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4576884))) != 0) goto loc_00B69591;
    result = (unsigned int)(*(unsigned int *)(v_rip + 4576884));
    if ((unsigned int)((unsigned int)(a5)) != 0) {
        a1 = a4;
        result = KiInitializeProcessorCycleAccumulation(a1, v_stack_m2A0, (unsigned int)(*(unsigned int *)(v_rip + 4577519)) + 4, v_stack_m290);
    }
    if ((*(unsigned __int8 *)(v_rip + 4576397)) == 0) goto loc_00B69607;
    if ((unsigned int)((unsigned int)(a5)) != 0) {
        a1 = a4;
        result = KeInitializeClockOtherProcessors(a1, v_stack_m2A0, (unsigned int)(*(unsigned int *)(v_rip + 4577519)) + 4, v_stack_m290);
    }
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, v_stack_m2A0, (unsigned int)(*(unsigned int *)(v_rip + 4577519)) + 4, v_stack_m290);
    v_rsp = (v_rsp) + (680);
    return result;
loc_00B6962A:
    a4 = 0;
    result = KeBugCheckEx(a4 + 62, v_rbx, (unsigned int)(*(unsigned int *)(v_rip + 4577519)) + 4, a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KiInitializeKernel(int64_t Arg1, int64_t Arg2, int64_t Arg3, void *Arg4, uint32_t Arg5, int64_t Arg6)
{
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r12;
    int64_t local_rbx;
    int64_t local_rsp;
    uint32_t v_stack_m22C;
    uint64_t v_stack_m248;
    uint32_t v_stack_m254;
    uint64_t v_stack_m260;
    uint64_t v_stack_m268;
    uint64_t v_stack_m270;
    uint64_t v_stack_m278;
    uint64_t v_stack_m280;
    uint64_t v_stack_m288;
    uint64_t v_stack_m290;
    uint64_t v_stack_m298;
    uint64_t v_stack_m2A0;
    uint64_t v_stack_m2A8;
    uint64_t v_stack_m2B8;
    uint64_t v_stack_m48;
    uint64_t v_stack_p20;
    uint32_t v_stack_p28;

    local_rsp = (local_rsp) - (680);
    result = (*(uint64_t *)(v_rip + 0x2A1A07)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m2A0 = Arg3;
    v_stack_m298 = Arg2;
    v_stack_m280 = Arg1;
    v_stack_m278 = Arg2;
    v_stack_m270 = Arg4;
    v_stack_m290 = Arg6;
    v_stack_m268 = Arg6;
    v_stack_m260 = v_xmm0;
    if ((uint32_t)((uint32_t)(Arg5)) != 0) goto loc_00B68DB6;
    result = HvlPhase0Initialize(Arg6, Arg2, Arg3, Arg4);
    if ((*(uint32_t *)(v_rip + 0x49F3C3)) != ((uint32_t)((uint32_t)(Arg5) + 1))) goto loc_00B68DBB;
    if (((*(uint32_t *)(v_rip + 0x45DD13)) & (0x80000ULL)) == 0) goto loc_00B68DBB;
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x45C25A) + 0x308) = (uint32_t)((uint32_t)(Arg5) + 1);
    goto loc_00B68DBB;
loc_00B68DB6:
loc_00B68DBB:
    v_stack_m2A8 = *(uint64_t *)(arg4 + 0x8FA0);
    v_stack_m288 = Arg4 + 141;
    if (((uint8_t)(*(uint8_t *)(arg4 + 0x8D))) == 2) goto loc_00B68DE5;
    result = (uint8_t)((*(uint8_t *)(arg4 + 0x8D)) - (1));
    if ((((uint8_t)(result)) & (253)) == 0) {
        Arg2 = v_stack_m2A8;
        Arg1 = Arg4;
        result = KiSetHardwareSpeculationControlFeatures(Arg1, Arg2, Arg3, Arg4);
    }
    result = KiCheckMicrocode(Arg4, Arg2, Arg3, Arg4);
    Arg2 = 0;
    result = memset(v_stack_m248, Arg2, 512, Arg4);
    if ((uint32_t)((uint32_t)(Arg5)) != 0) goto loc_00B68F7E;
    result = KiDetectFpuLeakage(v_stack_m248, Arg2, 512, Arg4);
    *(uint32_t *)(v_rip + 0x45E02D) = (uint32_t)(result);
    if ((uint32_t)(result) != 0) {
    }
    if ((*(uint8_t *)(v_rip + 0x45DC42)) == 0) goto loc_00B68E6D;
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x160)) != 0) goto loc_00B68E8F;
    result = KiSetUserTbFlushPending(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), Arg2, 512, Arg4);
    goto loc_00B68E8F;
loc_00B68E6D:
    if (((v_cr4) & (0x20080ULL)) == 0) goto loc_00B68E89;
    goto loc_00B68E8F;
loc_00B68E89:
loc_00B68E8F:
    result = KiSetPageAttributesTable(v_cr4, Arg2, 512, Arg4);
    if ((*(uint8_t *)(result)) == 0) goto loc_00B68EB2;
    result = (v_stack_m2A8) | ((uint32_t)(0x80000000ULL));
    goto loc_00B68EC4;
loc_00B68EB2:
    result = (result) & ((uint32_t)(0x80000000ULL));
loc_00B68EC4:
    v_stack_m2A8 = result;
    result = (v_cr4) | (24);
    if ((*(uint8_t *)(v_rip + 0x45DBAD)) == 0) goto loc_00B68F02;
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x160)) != 0) goto loc_00B68F24;
    result = KiSetUserTbFlushPending(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), Arg2, 512, Arg4);
    goto loc_00B68F24;
loc_00B68F02:
    if (((result) & (0x20080ULL)) == 0) goto loc_00B68F1E;
    goto loc_00B68F24;
loc_00B68F1E:
loc_00B68F24:
    result = KiConfigureProcessorBlock(Arg4, Arg2, 512, Arg4);
    result = KiInitializeTopologyStructures(Arg4, Arg2, 512, Arg4);
    result = (uint32_t)((uint32_t)((uint32_t)(0xFFBFULL)));
    if (v_stack_m22C != 0) { result = v_stack_m22C; }
    *(uint32_t *)(v_rip + 0x45C1C1) = (uint32_t)(result);
    v_stack_m2B8 = v_rip - 11964250;
    Arg4 = 0;
    result = KeCompactServiceTable(v_rip - 11065431, v_rip - 11063460, (uint32_t)(*(uint32_t *)(v_rip - 0xA8D0A1)), Arg4);
    goto loc_00B68FB0;
loc_00B68F7E:
    if ((*(uint32_t *)(v_rip + 0x45DED3)) != 0) {
    }
    result = KiSetPageAttributesTable(v_rip - 11065431, v_rip - 11063460, (uint32_t)(*(uint32_t *)(v_rip - 0xA8D0A1)), Arg4);
    result = KiInitializeTopologyStructures(0, v_rip - 11063460, (uint32_t)(*(uint32_t *)(v_rip - 0xA8D0A1)), Arg4);
loc_00B68FB0:
    result = KiInitializeCoreControlBlock(Arg4 + 41240, Arg4 + 44736, (uint32_t)(*(uint32_t *)(v_rip - 0xA8D0A1)), Arg4);
    result = KiAddProcessorToCoreControlBlock(Arg4 + 41240, 0, (uint32_t)(*(uint32_t *)(v_rip - 0xA8D0A1)), Arg4);
    result = KiSetCacheInformation(Arg4 + 41240, 0, (uint32_t)(*(uint32_t *)(v_rip - 0xA8D0A1)), Arg4);
    result = PoInitializePrcb(0, 0, (uint32_t)(*(uint32_t *)(v_rip - 0xA8D0A1)), Arg4);
    *(void **)(arg4 + 0x8EA0) = Arg4 + 36512;
    if ((*(uint64_t *)(arg4 + 0x8EA0)) == 0) goto loc_00B69057;
    v_stack_m2A8 = v_stack_m2A8;
    result = RtlGetXSaveFeatureFlags(0, 0, (uint32_t)(*(uint32_t *)(v_rip - 0xA8D0A1)), Arg4);
    if ((((uint8_t)(result)) & (8)) != 0) {
        v_stack_m2A8 = v_stack_m2A8;
        Arg1 = v_stack_m2A8;
    }
    if ((((uint8_t)(result)) & (16)) != 0) {
        Arg1 = v_stack_m2A8;
        Arg1 = (Arg1) | (0);
        v_stack_m2A8 = Arg1;
    }
    if ((((uint8_t)(result)) & (64)) != 0) {
        Arg1 = (Arg1) | (result);
        v_stack_m2A8 = Arg1;
    }
    result = KiSetControlEnforcement(0, v_stack_m2A8, (uint32_t)(*(uint32_t *)(v_rip - 0xA8D0A1)), Arg4);
    result = KiCheckEnqueueStoreFeaturePresence(0, v_stack_m2A8, (uint32_t)(*(uint32_t *)(v_rip - 0xA8D0A1)), Arg4);
    if ((uint32_t)((uint32_t)(Arg5)) != 0) goto loc_00B6914C;
    *(uint16_t *)(v_rip + 0x45BFEE) = (uint16_t)((uint32_t)(Arg5) + 9);
    *(uint16_t *)(v_rip + 0x45DB52) = (uint16_t)((int8_t)(*(uint8_t *)(arg4 + 0x40)));
    *(uint16_t *)(v_rip + 0x45DB52) = (uint16_t)(*(uint16_t *)(arg4 + 0x42));
    *(uint64_t *)(v_rip + 0x45DA87) = v_stack_m2A8;
    result = *(uint16_t *)(arg4 + 0x42);
    if ((*(uint32_t *)(v_rip + 0x45DC70)) != ((uint32_t)((uint32_t)(Arg5)))) {
        Arg1 = v_cr8;
        Arg2 = 1;
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, (uint32_t)(*(uint32_t *)(v_rip - 0xA8D0A1)), Arg4);
    }
    result = KiInitSystem(v_stack_m280, Arg2, (uint32_t)(*(uint32_t *)(v_rip - 0xA8D0A1)), Arg4);
    Arg2 = (Arg2) << (32);
    result = (result) | (Arg2);
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(result))) & (15));
    Arg2 = (result) ^ (result);
    *(uint64_t *)(v_rip + 0x45DE82) = Arg2;
    Arg2 = (Arg2) << (32);
    result = (result) | (Arg2);
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(result))) & (15));
    result = (result) ^ (result);
    *(uint64_t *)(v_rip + 0x45E138) = result;
    result = HviGetHypervisorFeatures(v_stack_m260, result, (uint32_t)(*(uint32_t *)(v_rip - 0xA8D0A1)), Arg4);
    if (((v_stack_m254) & (0x1000ULL)) != 0) {
        *(uint32_t *)(v_rip + 0x45DC8B) = 1;
    }
    result = KiIsKernelCfgActive(v_stack_m260, result, (uint32_t)(*(uint32_t *)(v_rip - 0xA8D0A1)), Arg4);
    if ((uint32_t)(result) == 0) goto loc_00B6928C;
    result = RtlInitKernelModeSpecialMachineFrameEntries(v_stack_m260, result, (uint32_t)(*(uint32_t *)(v_rip - 0xA8D0A1)), Arg4);
    goto loc_00B6928C;
loc_00B6914C:
    local_r12 = (uint32_t)(0xFFBFULL);
    if (v_stack_m22C != 0) { local_r12 = v_stack_m22C; }
    Arg3 = (*(uint64_t *)(v_rip + 0x45D9CC)) & (result);
    Arg1 = (uint32_t)((v_stack_m2A8) & (0x8000000ULL));
    if (Arg1 == 0) { Arg3 = Arg3; }
    if ((*(uint8_t *)(v_stack_m288)) != 2) goto loc_00B69214;
    if ((*(uint8_t *)(arg4 + 0x40)) != 6) goto loc_00B69214;
    if ((*(uint8_t *)(arg4 + 0x43)) != 23) goto loc_00B69214;
    if ((*(uint8_t *)(arg4 + 0x42)) != 10) goto loc_00B69214;
    result = KeGetTopologyIdForProcessor(0, 4, Arg3, Arg4);
    Arg4 = 0;
loc_00B691C7:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x45D8B3))))) goto loc_00B691F1;
    result = KeGetTopologyIdForProcessor(*(uint64_t *)(v_rip - 0xB68FB0 + arg4 * 8 + 0xFC8C40), 4, Arg3, Arg4);
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == ((uint32_t)(result))) goto loc_00B691EE;
    Arg4 = (uint32_t)((Arg4) + (1));
    goto loc_00B691C7;
loc_00B691EE:
loc_00B691F1:
    local_rbx = v_stack_m2A8;
    if ((((uint32_t)(0x100000ULL)) & ((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip - 0xB68FB0 + arg4 * 8 + 0xFC8C40) + 0x8FA0)))) != 0) {
        local_rbx = (v_stack_m2A8) | ((uint32_t)(0x100000ULL));
    }
    if (local_rbx != Arg3) goto loc_00B6962A;
    if (((uint32_t)(local_r12)) != (*(uint32_t *)(v_rip + 0x45BEF0))) goto loc_00B6962A;
    if ((*(uint32_t *)(*(uint64_t *)(v_rip + 0x45FA08) + 0xE8)) != ((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0xE8))))) goto loc_00B6962A;
    if ((*(uint32_t *)(*(uint64_t *)(v_rip + 0x45FA08) + 0xA0)) != ((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0xA0))))) goto loc_00B6962A;
    if ((*(uint32_t *)(*(uint64_t *)(v_rip + 0x45FA08) + 0xA4)) != ((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0xA4))))) goto loc_00B6962A;
    result = (uint32_t)(*(uint32_t *)(arg4 + 0xA4));
    if ((*(uint32_t *)(v_rip + 0x45DAAF)) != 0) {
        Arg1 = 1;
        result = KiLowerIrqlProcessIrqlFlags(Arg1, 2, Arg3, Arg4);
    }
    Arg1 = 0;
    result = HvlEnlightenProcessor(Arg1, 2, Arg3, Arg4);
loc_00B6928C:
    if ((*(uint32_t *)(v_rip + 0x45DB2D)) != 0) {
        result = 15;
        Arg2 = 0;
        Arg1 = 0x40000040ULL;
    }
    Arg1 = 0;
    result = KiEnableXSave(Arg1, Arg2, Arg3, Arg4);
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x45BD57) + 0x2F8) = 195;
    *(uint8_t *)(*(uint64_t *)(v_rip + 0x45BD45) + 0x276) = 1;
    *(uint8_t *)(*(uint64_t *)(v_rip + 0x45BD37) + 0x277) = 1;
    *(uint8_t *)(*(uint64_t *)(v_rip + 0x45BD29) + 0x27A) = 1;
    *(uint8_t *)(*(uint64_t *)(v_rip + 0x45BD1B) + 0x27C) = 1;
    *(uint8_t *)(*(uint64_t *)(v_rip + 0x45BD0D) + 0x27D) = 1;
    *(uint8_t *)(*(uint64_t *)(v_rip + 0x45BCFF) + 0x27E) = 1;
    *(uint8_t *)(*(uint64_t *)(v_rip + 0x45BCF1) + 0x282) = 1;
    result = *(uint64_t *)(v_rip + 0x45BCF1);
    if (!(condition_is_above_or_equal)) {
        result = *(uint64_t *)(v_rip + 0x45BCDC);
        *(uint8_t *)(result + 0x281) = 1;
    }
    if (!(condition_is_above_or_equal)) {
        result = *(uint64_t *)(v_rip + 0x45BCC7);
        *(uint8_t *)(result + 0x27B) = 1;
    }
    if (!(condition_is_above_or_equal)) {
        result = *(uint64_t *)(v_rip + 0x45BCB2);
        *(uint8_t *)(result + 0x285) = 1;
    }
    if (!(condition_is_above_or_equal)) {
        result = *(uint64_t *)(v_rip + 0x45BC9D);
        *(uint8_t *)(result + 0x28A) = 1;
    }
    if (!(condition_is_above_or_equal)) {
        result = *(uint64_t *)(v_rip + 0x45BC88);
        *(uint8_t *)(result + 0x288) = 1;
    }
    if (!(condition_is_above_or_equal)) {
        result = *(uint64_t *)(v_rip + 0x45BC73);
        *(uint8_t *)(result + 0x289) = 1;
    }
    if (!(condition_is_above_or_equal)) {
        result = *(uint64_t *)(v_rip + 0x45BC5E);
        *(uint8_t *)(result + 0x290) = 1;
    }
    if (!(condition_is_above_or_equal)) {
        result = *(uint64_t *)(v_rip + 0x45BC49);
        *(uint8_t *)(result + 0x294) = 1;
    }
    if (!(condition_is_above_or_equal)) {
        result = *(uint64_t *)(v_rip + 0x45BC34);
        *(uint8_t *)(result + 0x298) = 1;
    }
    if (!(condition_is_above_or_equal)) {
        result = *(uint64_t *)(v_rip + 0x45BC1F);
        *(uint8_t *)(result + 0x299) = 1;
    }
    if (!(condition_is_above_or_equal)) {
        result = *(uint64_t *)(v_rip + 0x45BC0A);
        *(uint8_t *)(result + 0x29A) = 1;
    }
    Arg1 = (((*(uint8_t *)(Arg2)) & (4)) != 0) ? 1 : 0;
    result = (condition_is_below) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) != 0) {
        result = *(uint64_t *)(v_rip + 0x45BBE0);
        *(uint8_t *)(result + 0x29B) = 1;
    }
    Arg1 = (((*(uint8_t *)(Arg2)) & (4)) != 0) ? 1 : 0;
    result = (condition_is_below) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) != 0) {
        result = *(uint64_t *)(v_rip + 0x45BBC0);
        *(uint8_t *)(result + 0x29C) = 1;
    }
    Arg1 = ((((uint8_t)(result)) & (224)) != 0) ? 1 : 0;
    result = (condition_is_below) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) != 0) {
        result = *(uint64_t *)(v_rip + 0x45BB98);
        *(uint8_t *)(result + 0x29D) = 1;
    }
    if (!(condition_is_above_or_equal)) {
        result = *(uint64_t *)(v_rip + 0x45BB83);
        *(uint8_t *)(result + 0x29E) = 1;
    }
    if (!(condition_is_above_or_equal)) {
        result = *(uint64_t *)(v_rip + 0x45BB6E);
        *(uint8_t *)(result + 0x2B0) = 1;
    }
    result = Feature_Test57481295__private_IsEnabledDeviceUsageNoInline(Arg1, Arg2, Arg3, *(uint64_t *)(v_rip + 0x45BD57));
    if ((uint32_t)(result) == 0) goto loc_00B694BF;
    if (!(condition_is_above_or_equal)) {
        result = *(uint64_t *)(v_rip + 0x45BB50);
        *(uint8_t *)(result + 0x2B1) = 1;
    }
    *(uint8_t *)(*(uint64_t *)(v_rip + 0x45BB3C) + 0x2ED) = (uint8_t)(*(uint8_t *)(v_rip + 0x2FD45B));
    if ((uint32_t)((uint32_t)(Arg5)) != 0) goto loc_00B694F6;
    result = KiInitializeAndStartInitialThread(v_stack_m298, v_stack_m2A0, Arg4, v_stack_m290);
    goto loc_00B69508;
loc_00B694F6:
    result = KiStartIdleThread(v_stack_m298, Arg4, v_stack_m2A0, v_stack_m290);
loc_00B69508:
    if ((uint32_t)((uint32_t)(Arg5)) != 0) {
        Arg1 = Arg4;
        result = KiStartPrcbThreads(Arg1, Arg4, v_stack_m2A0, v_stack_m290);
    }
    if ((uint32_t)((uint32_t)(Arg5)) != 0) goto loc_00B69525;
    result = InitBootProcessor(v_stack_m290, Arg4, v_stack_m2A0, v_stack_m290);
    goto loc_00B6953D;
loc_00B69525:
    Arg2 = 0;
    result = HalInitSystem(1, Arg2, v_stack_m2A0, v_stack_m290);
    if ((uint8_t)(result) == 0) {
        Arg1 = 92;
        result = KeBugCheck(Arg1, Arg2, v_stack_m2A0, v_stack_m290);
    }
    goto loc_00B6955B;
loc_00B6955B:
    result = v_stack_m288;
    if ((*(uint8_t *)(v_stack_m288)) == 1) {
        Arg2 = (uint32_t)((uint32_t)(Arg5));
        Arg1 = Arg4;
        result = KiConfigureAmdTprLowerInterruptDelayWorkaround(Arg1, Arg2, v_stack_m2A0, v_stack_m290);
    }
    result = KiCompleteKernelInit(Arg4, v_stack_m298, (uint32_t)((uint32_t)((uint32_t)(Arg5))), v_stack_m290);
    local_rbx = 0;
    goto loc_00B695D6;
loc_00B69591:
    local_rbx = (uint32_t)((local_rbx) + (1));
    if (((*(uint32_t *)(v_rip + 0x45BD13)) & ((uint32_t)(local_rbx))) != 0) goto loc_00B695D4;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x45D517)))) & (64)) == 0) goto loc_00B695D4;
    result = KiCheckVpBackingLongSpinWaitHypercall(Arg4, v_stack_m298, (uint32_t)((uint32_t)((uint32_t)(Arg5))), v_stack_m290);
    if ((uint8_t)(result) == 0) goto loc_00B695D4;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x45D8EF))) != 0) goto loc_00B695CB;
    result = KeHaltOnAddress(v_rip + 4576908, v_stack_m2A0, (uint32_t)(*(uint32_t *)(v_rip + 0x45D8EF)) + 4, v_stack_m290);
    goto loc_00B695D6;
loc_00B695CB:
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rbx)), v_stack_m2A0, (uint32_t)(*(uint32_t *)(v_rip + 0x45D8EF)) + 4, v_stack_m290);
    goto loc_00B695D6;
loc_00B695D4:
loc_00B695D6:
    v_stack_m2A0 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x45D674)));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x45D674))) != 0) goto loc_00B69591;
    result = (uint32_t)(*(uint32_t *)(v_rip + 0x45D674));
    if ((uint32_t)((uint32_t)(Arg5)) != 0) {
        Arg1 = Arg4;
        result = KiInitializeProcessorCycleAccumulation(Arg1, v_stack_m2A0, (uint32_t)(*(uint32_t *)(v_rip + 0x45D8EF)) + 4, v_stack_m290);
    }
    if ((*(uint8_t *)(v_rip + 0x45D48D)) == 0) goto loc_00B69607;
    if ((uint32_t)((uint32_t)(Arg5)) != 0) {
        Arg1 = Arg4;
        result = KeInitializeClockOtherProcessors(Arg1, v_stack_m2A0, (uint32_t)(*(uint32_t *)(v_rip + 0x45D8EF)) + 4, v_stack_m290);
    }
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_stack_m2A0, (uint32_t)(*(uint32_t *)(v_rip + 0x45D8EF)) + 4, v_stack_m290);
    local_rsp = (local_rsp) + (680);
    return result;
loc_00B6962A:
    Arg4 = 0;
    result = KeBugCheckEx(Arg4 + 62, local_rbx, (uint32_t)(*(uint32_t *)(v_rip + 0x45D8EF)) + 4, Arg4);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg4` | `+ 0x0` | `8` | `R` |
| `Arg4` | `+ 0x0` | `64` | `W` |
| `Arg4` | `+ 0x40` | `8` | `R` |
| `Arg4` | `+ 0x42` | `8` | `R` |
| `Arg4` | `+ 0x42` | `16` | `R` |
| `Arg4` | `+ 0x43` | `8` | `R` |
| `Arg4` | `+ 0x8D` | `64` | `R` |
| `Arg4` | `+ 0xA0` | `32` | `R` |
| `Arg4` | `+ 0xA4` | `32` | `R` |
| `Arg4` | `+ 0xE8` | `32` | `R` |
| `Arg4` | `+ 0x8E98` | `64` | `R/W` |
| `Arg4` | `+ 0x8EA0` | `64` | `R` |
| `Arg4` | `+ 0x8FA0` | `64` | `R` |
| `Arg4` | `+ 0xA118` | `64` | `R` |
| `Arg4` | `+ 0xAEC0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagelk&rva=0x00B68D20&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
