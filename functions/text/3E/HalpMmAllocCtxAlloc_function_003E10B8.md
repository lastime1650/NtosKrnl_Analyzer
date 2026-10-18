# HalpMmAllocCtxAlloc

- RVA: `0x003E10B8`–`0x003E1606` (길이 `1,358` bytes)
- VA: `0x00000001403E10B8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000949E8`
- 디코드: `353`개 명령, `1,358/1,358` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **7**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **68**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x003E110E` → [KeAcquireSpinLockRaiseToDpc](../20/KeAcquireSpinLockRaiseToDpc_function_00208470.md) (function, `0x00208470`)
- `0x003E1272` → [RtlSetBits](RtlSetBits_function_003E1610.md) (function, `0x003E1610`)
- `0x003E12BD` → [KeReleaseSpinLock](../39/KeReleaseSpinLock_function_00392BA0.md) (function, `0x00392BA0`)
- `0x003E12C7` → [HalpMmAllocCtxAllocBuffer](HalpMmAllocCtxAllocBuffer_function_003E16B8.md) (function, `0x003E16B8`)
- `0x003E12E2` → [KeAcquireSpinLockRaiseToDpc](../20/KeAcquireSpinLockRaiseToDpc_function_00208470.md) (function, `0x00208470`)
- `0x003E13A0` → [KeReleaseSpinLock](../39/KeReleaseSpinLock_function_00392BA0.md) (function, `0x00392BA0`)
- `0x003E15E8` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)

### Direct callers
- [HalpDmaAllocateMapRegisters](../3D/HalpDmaAllocateMapRegisters_function_003DDA0C.md) at `0x003DDBFC`
- [HalpDmaAllocateMapRegisters](../3D/HalpDmaAllocateMapRegisters_function_003DDA0C.md) at `0x003DDCF2`
- [HalpBuddyAllocatorSplitNode](HalpBuddyAllocatorSplitNode_function_003E0BD0.md) at `0x003E0BEF`
- [HalpBuddyAllocatorSplitNode](HalpBuddyAllocatorSplitNode_function_003E0BD0.md) at `0x003E0C08`
- [HalpAllocateCommonBufferVectorInternal](HalpAllocateCommonBufferVectorInternal_function_003E848C.md) at `0x003E851F`
- [HalpAllocateCommonBufferVectorInternal](HalpAllocateCommonBufferVectorInternal_function_003E848C.md) at `0x003E8553`
- [HalpIommuAllocateAndZeroPageTable](../3F/HalpIommuAllocateAndZeroPageTable_function_003F8B30.md) at `0x003F8BE5`
- [HalpCmciInitializeErrorPacket](../48/HalpCmciInitializeErrorPacket_function_00487010.md) at `0x00487041`
- [HalpDmaAllocateNewTranslationBuffer](../49/HalpDmaAllocateNewTranslationBuffer_function_0049ACD8.md) at `0x0049AD09`
- [HalpDmaAllocateNewTranslationBuffer](../49/HalpDmaAllocateNewTranslationBuffer_function_0049ACD8.md) at `0x0049AD69`
- [HalpDmaAllocateNewTranslationBuffer](../49/HalpDmaAllocateNewTranslationBuffer_function_0049ACD8.md) at `0x0049ADBC`
- [HalpAllocatePmcCounterSetEx](../4C/HalpAllocatePmcCounterSetEx_function_004C5E70.md) at `0x004C5F3F`
- [HalpIommuGetHardwareDomain](../4D/HalpIommuGetHardwareDomain_function_004D7BCC.md) at `0x004D7C52`
- [HalpHvInitMcaPcrContext](../4D/HalpHvInitMcaPcrContext_function_004D7D88.md) at `0x004D7DF0`
- [HalpIommuCloneDeviceId](../4E/HalpIommuCloneDeviceId_function_004E4228.md) at `0x004E4251`
- [HalpTimerInitSystem](../53/HalpTimerInitSystem_function_0053CB70.md) at `0x0053CD9F`
- [HalInitializeBios](../53/HalInitializeBios_function_0053D9A0.md) at `0x0053DBDC`
- [HalpAcpiAllocateMemory](../53/HalpAcpiAllocateMemory_function_0053ECE0.md) at `0x0053ED46`
- [HalDmaAllocateCrashDumpRegistersEx](../53/HalDmaAllocateCrashDumpRegistersEx_function_0053F6D0.md) at `0x0053F872`
- [HalpInterruptSetLineSpecificOverride](../54/HalpInterruptSetLineSpecificOverride_function_0054468C.md) at `0x005446B5`
- [HalpTscReserveResources](../54/HalpTscReserveResources_function_0054AE20.md) at `0x0054AE9F`
- [HalpHvInitMcaStatusMsrCache](../54/HalpHvInitMcaStatusMsrCache_function_0054C170.md) at `0x0054C1BC`
- [HalpHvInitMcaStatusMsrCache](../54/HalpHvInitMcaStatusMsrCache_function_0054C170.md) at `0x0054C263`
- [HalpIommuCreateDevice](../54/HalpIommuCreateDevice_function_0054ED60.md) at `0x0054F02F`
- [HalpIommuCreateDevice](../54/HalpIommuCreateDevice_function_0054ED60.md) at `0x0054F07D`
- [IommupPasidDeviceCreate](../54/IommupPasidDeviceCreate_function_0054FEEC.md) at `0x0054FF1A`
- [HalpDmaAllocateMapRegisterFrame](../55/HalpDmaAllocateMapRegisterFrame_function_005506BC.md) at `0x005506D4`
- [HalpDmaAllocateDomain](../55/HalpDmaAllocateDomain_function_00551C10.md) at `0x00551C4D`
- [HalpDmaGetReservedRegionsForDeviceResources](../55/HalpDmaGetReservedRegionsForDeviceResources_function_00552018.md) at `0x005520B6`
- [HalpDmaGetReservedRegionsForDeviceResources](../55/HalpDmaGetReservedRegionsForDeviceResources_function_00552018.md) at `0x0055212F`
- [HalpDmaGetReservedRegionsForHybridPassthroughDomain](../55/HalpDmaGetReservedRegionsForHybridPassthroughDomain_function_005522A4.md) at `0x005522BB`
- [HalpDmaGetReservedRegionsForTranslateDomain](../55/HalpDmaGetReservedRegionsForTranslateDomain_function_0055232C.md) at `0x00552387`
- [HalpDmaInitializeControllers](../55/HalpDmaInitializeControllers_function_005531E8.md) at `0x00553280`
- [HalpIommuGetDeviceId](../55/HalpIommuGetDeviceId_function_005536C0.md) at `0x00553785`
- [HalpIommuAllocateDmaDomain](../55/HalpIommuAllocateDmaDomain_function_00554904.md) at `0x00554952`
- [HalpIommuCreateIncreaseAliasTrack](../55/HalpIommuCreateIncreaseAliasTrack_function_00554CB0.md) at `0x00554D1E`
- [HalpNumaAddRangeProximity](../55/HalpNumaAddRangeProximity_function_00558EC0.md) at `0x005590CC`
- [HalpInterruptAllocateCacheDomainTable](../55/HalpInterruptAllocateCacheDomainTable_function_0055A41C.md) at `0x0055A44B`
- [EmonAddProfileSource](../55/EmonAddProfileSource_function_0055BEA0.md) at `0x0055BEE9`
- [EmonAddProfileSource](../55/EmonAddProfileSource_function_0055BEA0.md) at `0x0055BF19`
- [EmonAllocateResources](../55/EmonAllocateResources_function_0055C40C.md) at `0x0055C489`
- [ExtEnvAllocateMemory](../56/ExtEnvAllocateMemory_function_005610B0.md) at `0x005610E4`
- [ExtEnvAllocatePhysicalMemory](../56/ExtEnvAllocatePhysicalMemory_function_00561124.md) at `0x00561264`
- [HalpRegisterUsbController](../56/HalpRegisterUsbController_function_00563758.md) at `0x0056377B`
- [IommuEnableDevicePasid](../56/IommuEnableDevicePasid_function_00565150.md) at `0x0056519E`
- [IommuEnableDevicePasid](../56/IommuEnableDevicePasid_function_00565150.md) at `0x00565213`
- [IommuGetLibraryContext](../56/IommuGetLibraryContext_function_00565990.md) at `0x005659CC`
- [IommuGetLibraryContext](../56/IommuGetLibraryContext_function_00565990.md) at `0x005659E5`
- [IommupGetSystemContext](../56/IommupGetSystemContext_function_00566310.md) at `0x00566392`
- [IommupMapDeviceInternal](../56/IommupMapDeviceInternal_function_00566478.md) at `0x0056656C`
- [IommupMapDeviceInternal](../56/IommupMapDeviceInternal_function_00566478.md) at `0x0056660E`
- [IommupMapDeviceInternal](../56/IommupMapDeviceInternal_function_00566478.md) at `0x00566630`
- [IommuDomainAttachDevice](../56/IommuDomainAttachDevice_function_00567960.md) at `0x00567A3C`
- [IommuDomainAttachDeviceEx](../56/IommuDomainAttachDeviceEx_function_00567B60.md) at `0x00567C3E`
- [IommuRegisterInterfaceStateChangeCallback](../56/IommuRegisterInterfaceStateChangeCallback_function_00568200.md) at `0x0056823D`
- [IommuReserveLogicalAddressRange](../56/IommuReserveLogicalAddressRange_function_00568400.md) at `0x00568464`
- [HalpIommuCreateDmarPageTable](../56/HalpIommuCreateDmarPageTable_function_00568C4C.md) at `0x00568C8B`
- [Amd64AddProfileSource](../56/Amd64AddProfileSource_function_0056B720.md) at `0x0056B799`
- [Amd64AddProfileSource](../56/Amd64AddProfileSource_function_0056B720.md) at `0x0056B7C9`
- [Amd64InitializeCacheStatusEnhanced](../56/Amd64InitializeCacheStatusEnhanced_function_0056C804.md) at `0x0056C905`
- [Amd64InitializeCacheStatusOriginal](../56/Amd64InitializeCacheStatusOriginal_function_0056CA40.md) at `0x0056CB43`
- [Amd64InitializeDataFabricStatusEnhanced](../56/Amd64InitializeDataFabricStatusEnhanced_function_0056CC3C.md) at `0x0056CCBB`
- [Amd64InitializeDataFabricStatusOriginal](../56/Amd64InitializeDataFabricStatusOriginal_function_0056CDCC.md) at `0x0056CE4F`
- [Amd64InitializeUncoreStatusEnhanced](../56/Amd64InitializeUncoreStatusEnhanced_function_0056D178.md) at `0x0056D1A2`
- [Amd64InitializeUncoreStatusOriginal](../56/Amd64InitializeUncoreStatusOriginal_function_0056D214.md) at `0x0056D23E`
- [HalpBuddyAllocatorCreateAllocator](../57/HalpBuddyAllocatorCreateAllocator_function_00575B4C.md) at `0x00575B84`
- [HalpBuddyAllocatorCreateAllocator](../57/HalpBuddyAllocatorCreateAllocator_function_00575B4C.md) at `0x00575BA0`
- [HalpBuddyAllocatorCreateAllocator](../57/HalpBuddyAllocatorCreateAllocator_function_00575B4C.md) at `0x00575BC2`
- [HalpDmaAllocateLocalContiguousPool](../../page/70/HalpDmaAllocateLocalContiguousPool_function_00708EE4.md) at `0x00708F1D`
- [HalpDmaAllocateLocalContiguousPool](../../page/70/HalpDmaAllocateLocalContiguousPool_function_00708EE4.md) at `0x00708FAF`
- [HalpDmaAllocateLocalContiguousPool](../../page/70/HalpDmaAllocateLocalContiguousPool_function_00708EE4.md) at `0x00708FD0`
- [HalpDmaAllocateLocalContiguousPool](../../page/70/HalpDmaAllocateLocalContiguousPool_function_00708EE4.md) at `0x007090E4`
- [HalpDmaAllocateLocalScatterPool](../../page/70/HalpDmaAllocateLocalScatterPool_function_007091D4.md) at `0x00709219`
- [HalpDmaAllocateLocalScatterPool](../../page/70/HalpDmaAllocateLocalScatterPool_function_007091D4.md) at `0x00709236`
- [HalpMcaInitializePcrContext](../../pagelk/B5/HalpMcaInitializePcrContext_function_00B5BDD0.md) at `0x00B5BE08`
- [HalpInitMemoryCachingRequirementsTable](../../pagelk/B5/HalpInitMemoryCachingRequirementsTable_function_00B5C1C4.md) at `0x00B5C1FB`
- [HalpBuildResumeStructures](../../pagelk/B5/HalpBuildResumeStructures_function_00B5D0F0.md) at `0x00B5D10C`
- [HalpMapCR3Ex](../../pagelk/B5/HalpMapCR3Ex_function_00B5E95C.md) at `0x00B5E9B2`
- [HalpMapNvsArea](../../pagelk/B7/HalpMapNvsArea_function_00B7D180.md) at `0x00B7D1A7`
- [HalpMceInitializeErrorPacket](../../pagelk/B7/HalpMceInitializeErrorPacket_function_00B7D4BC.md) at `0x00B7D4D6`
- [HalpAcpiDetectPiix4](../../init/C1/HalpAcpiDetectPiix4_function_00C1F9E0.md) at `0x00C1FA14`
- [HalpAcpiPopulateTableCache](../../init/C1/HalpAcpiPopulateTableCache_function_00C1FA88.md) at `0x00C1FABC`
- [HalpDmaAllocateEmergencyResources](../../init/C2/HalpDmaAllocateEmergencyResources_function_00C2075C.md) at `0x00C20772`
- [HalpDmaAllocateEmergencyResources](../../init/C2/HalpDmaAllocateEmergencyResources_function_00C2075C.md) at `0x00C20792`
- [HalpDmaAllocateMappingResources](../../init/C2/HalpDmaAllocateMappingResources_function_00C2087C.md) at `0x00C208AE`
- [HalpDmaAllocateMappingResources](../../init/C2/HalpDmaAllocateMappingResources_function_00C2087C.md) at `0x00C208D0`
- [HalpDmaAllocateMappingResources](../../init/C2/HalpDmaAllocateMappingResources_function_00C2087C.md) at `0x00C20944`
- [HalpDmaAllocateReservedMapping](../../init/C2/HalpDmaAllocateReservedMapping_function_00C20A18.md) at `0x00C20A23`
- [HalpDmaAllocateReservedMappingArray](../../init/C2/HalpDmaAllocateReservedMappingArray_function_00C20A74.md) at `0x00C20ABA`
- [HalpDmaAllocateTranslationBuffer](../../init/C2/HalpDmaAllocateTranslationBuffer_function_00C20B48.md) at `0x00C20B5F`
- [HalpDmaAllocateTranslationBuffer](../../init/C2/HalpDmaAllocateTranslationBuffer_function_00C20B48.md) at `0x00C20B75`
- [HalpDmaInitializeMasterAdapter](../../init/C2/HalpDmaInitializeMasterAdapter_function_00C21278.md) at `0x00C212FA`
- [HalpDmaInitializeMasterAdapter](../../init/C2/HalpDmaInitializeMasterAdapter_function_00C21278.md) at `0x00C21310`

### Static image references
- `0x003E10CD` → RVA `0x00FC2CA0` (`.data`; read)
- `0x003E1107` → RVA `0x00FC2CB0` (`.data`; read)
- `0x003E1399` → RVA `0x00FC2CA0` (`.data`; write)
- `0x003E15CB` → RVA `0x00023C60` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003E10B8  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
003E10BD  53                              push rbx
003E10BE  55                              push rbp
003E10BF  56                              push rsi
003E10C0  57                              push rdi
003E10C1  41 54                           push r12
003E10C3  41 55                           push r13
003E10C5  41 56                           push r14
003E10C7  48 83 EC 50                     sub rsp, 0x50
003E10CB  33 DB                           xor ebx, ebx
003E10CD  4C 8D 25 CC 1B BE 00            lea r12, [rip + 0xbe1bcc]
003E10D4  48 85 D2                        test rdx, rdx
003E10D7  0F 84 EE 04 00 00               je 0x1403e15cb
003E10DD  48 8D 42 0F                     lea rax, [rdx + 0xf]
003E10E1  48 83 E0 F0                     and rax, 0xfffffffffffffff0
003E10E5  48 3D 00 10 00 00               cmp rax, 0x1000
003E10EB  48 8D 68 10                     lea rbp, [rax + 0x10]
003E10EF  48 0F 43 E8                     cmovae rbp, rax
003E10F3  4C 8B F5                        mov r14, rbp
003E10F6  49 C1 EE 04                     shr r14, 4
003E10FA  48 81 FD 00 10 00 00            cmp rbp, 0x1000
003E1101  0F 83 68 02 00 00               jae 0x1403e136f
003E1107  48 8D 0D A2 1B BE 00            lea rcx, [rip + 0xbe1ba2]
003E110E  E8 5D 73 E2 FF                  call 0x140208470
003E1113  48 8B 3D 86 1B BE 00            mov rdi, qword ptr [rip + 0xbe1b86]
003E111A  41 BD FF FF FF FF               mov r13d, 0xffffffff
003E1120  88 84 24 90 00 00 00            mov byte ptr [rsp + 0x90], al
003E1127  49 3B FC                        cmp rdi, r12
003E112A  0F 84 7F 01 00 00               je 0x1403e12af
003E1130  44 8B 47 20                     mov r8d, dword ptr [rdi + 0x20]
003E1134  8B 77 18                        mov esi, dword ptr [rdi + 0x18]
003E1137  41 3B F0                        cmp esi, r8d
003E113A  4C 8B 67 28                     mov r12, qword ptr [rdi + 0x28]
003E113E  1B D2                           sbb edx, edx
003E1140  89 B4 24 A0 00 00 00            mov dword ptr [rsp + 0xa0], esi
003E1147  23 D6                           and edx, esi
003E1149  44 89 84 24 98 00 00 00         mov dword ptr [rsp + 0x98], r8d
003E1151  4C 89 64 24 40                  mov qword ptr [rsp + 0x40], r12
003E1156  41 8D 48 FF                     lea ecx, [r8 - 1]
003E115A  45 85 F6                        test r14d, r14d
003E115D  0F 84 1E 04 00 00               je 0x1403e1581
003E1163  4D 8B CC                        mov r9, r12
003E1166  41 83 E1 04                     and r9d, 4
003E116A  41 8B C1                        mov eax, r9d
003E116D  4C 89 4C 24 38                  mov qword ptr [rsp + 0x38], r9
003E1172  48 F7 D8                        neg rax
003E1175  8B C2                           mov eax, edx
003E1177  45 1B DB                        sbb r11d, r11d
003E117A  41 83 E3 20                     and r11d, 0x20
003E117E  44 89 5C 24 30                  mov dword ptr [rsp + 0x30], r11d
003E1183  89 84 24 A8 00 00 00            mov dword ptr [rsp + 0xa8], eax
003E118A  41 8D 14 03                     lea edx, [r11 + rax]
003E118E  45 8D 14 0B                     lea r10d, [r11 + rcx]
003E1192  49 8B C1                        mov rax, r9
003E1195  48 F7 D8                        neg rax
003E1198  41 8B C2                        mov eax, r10d
003E119B  48 1B C9                        sbb rcx, rcx
003E119E  2B C2                           sub eax, edx
003E11A0  83 E1 04                        and ecx, 4
003E11A3  FF C0                           inc eax
003E11A5  4C 2B E1                        sub r12, rcx
003E11A8  41 3B C6                        cmp eax, r14d
003E11AB  0F 82 3D 04 00 00               jb 0x1403e15ee
003E11B1  45 8B EA                        mov r13d, r10d
003E11B4  8B CA                           mov ecx, edx
003E11B6  45 2B EE                        sub r13d, r14d
003E11B9  80 E1 3F                        and cl, 0x3f
003E11BC  41 FF C5                        inc r13d
003E11BF  41 B9 01 00 00 00               mov r9d, 1
003E11C5  49 D3 E1                        shl r9, cl
003E11C8  49 FF C9                        dec r9
003E11CB  41 8B C5                        mov eax, r13d
003E11CE  48 C1 E8 06                     shr rax, 6
003E11D2  49 8D 34 C4                     lea rsi, [r12 + rax*8]
003E11D6  8B C2                           mov eax, edx
003E11D8  48 C1 E8 06                     shr rax, 6
003E11DC  4D 8D 04 C4                     lea r8, [r12 + rax*8]
003E11E0  4D 0B 08                        or r9, qword ptr [r8]
003E11E3  41 83 FE 7F                     cmp r14d, 0x7f
003E11E7  0F 87 8F 02 00 00               ja 0x1403e147c
003E11ED  B9 40 00 00 00                  mov ecx, 0x40
003E11F2  44 3B F1                        cmp r14d, ecx
003E11F5  0F 83 45 02 00 00               jae 0x1403e1440
003E11FB  41 83 FE 01                     cmp r14d, 1
003E11FF  0F 87 CF 01 00 00               ja 0x1403e13d4
003E1205  49 83 F9 FF                     cmp r9, -1
003E1209  75 12                           jne 0x1403e121d
003E120B  49 83 C0 08                     add r8, 8
003E120F  4C 3B C6                        cmp r8, rsi
003E1212  0F 87 0E 01 00 00               ja 0x1403e1326
003E1218  4D 8B 08                        mov r9, qword ptr [r8]
003E121B  EB E8                           jmp 0x1403e1205
003E121D  4D 2B C4                        sub r8, r12
003E1220  49 F7 D1                        not r9
003E1223  49 C1 F8 03                     sar r8, 3
003E1227  49 0F BC C1                     bsf rax, r9
003E122B  41 C1 E0 06                     shl r8d, 6
003E122F  44 03 C0                        add r8d, eax
003E1232  41 8B D0                        mov edx, r8d
003E1235  45 3B C5                        cmp r8d, r13d
003E1238  0F 87 E8 00 00 00               ja 0x1403e1326
003E123E  41 BD FF FF FF FF               mov r13d, 0xffffffff
003E1244  41 3B D5                        cmp edx, r13d
003E1247  0F 84 E2 00 00 00               je 0x1403e132f
003E124D  41 2B D3                        sub edx, r11d
003E1250  8B F2                           mov esi, edx
003E1252  4C 8D 25 47 1A BE 00            lea r12, [rip + 0xbe1a47]
003E1259  49 3B F5                        cmp rsi, r13
003E125C  0F 84 8C 00 00 00               je 0x1403e12ee
003E1262  8A 9C 24 90 00 00 00            mov bl, byte ptr [rsp + 0x90]
003E1269  48 8D 4F 20                     lea rcx, [rdi + 0x20]
003E126D  45 8B C6                        mov r8d, r14d
003E1270  8B D6                           mov edx, esi
003E1272  E8 99 03 00 00                  call 0x1403e1610
003E1277  41 8D 04 36                     lea eax, [r14 + rsi]
003E127B  89 47 18                        mov dword ptr [rdi + 0x18], eax
003E127E  48 8B 17                        mov rdx, qword ptr [rdi]
003E1281  48 39 7A 08                     cmp qword ptr [rdx + 8], rdi
003E1285  75 21                           jne 0x1403e12a8
003E1287  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
003E128B  48 39 38                        cmp qword ptr [rax], rdi
003E128E  75 18                           jne 0x1403e12a8
003E1290  48 89 10                        mov qword ptr [rax], rdx
003E1293  48 89 42 08                     mov qword ptr [rdx + 8], rax
003E1297  48 8B 05 02 1A BE 00            mov rax, qword ptr [rip + 0xbe1a02]
003E129E  4C 39 60 08                     cmp qword ptr [rax + 8], r12
003E12A2  0F 84 DD 00 00 00               je 0x1403e1385
003E12A8  B9 03 00 00 00                  mov ecx, 3
003E12AD  CD 29                           int 0x29
003E12AF  8A 94 24 90 00 00 00            mov dl, byte ptr [rsp + 0x90]
003E12B6  48 8D 0D F3 19 BE 00            lea rcx, [rip + 0xbe19f3]
003E12BD  E8 DE 18 FB FF                  call 0x140392ba0
003E12C2  BA 00 40 00 00                  mov edx, 0x4000
003E12C7  E8 EC 03 00 00                  call 0x1403e16b8
003E12CC  48 8B F8                        mov rdi, rax
003E12CF  48 85 C0                        test rax, rax
003E12D2  0F 84 E9 00 00 00               je 0x1403e13c1
003E12D8  48 8D 0D D1 19 BE 00            lea rcx, [rip + 0xbe19d1]
003E12DF  48 8B F3                        mov rsi, rbx
003E12E2  E8 89 71 E2 FF                  call 0x140208470
003E12E7  8A D8                           mov bl, al
003E12E9  E9 7B FF FF FF                  jmp 0x1403e1269
003E12EE  48 8B 3F                        mov rdi, qword ptr [rdi]
003E12F1  E9 31 FE FF FF                  jmp 0x1403e1127
003E12F6  49 0F BD C1                     bsr rax, r9
003E12FA  0F 84 9A 02 00 00               je 0x1403e159a
003E1300  41 B9 3F 00 00 00               mov r9d, 0x3f
003E1306  44 2B C8                        sub r9d, eax
003E1309  49 8B C0                        mov rax, r8
003E130C  49 2B C4                        sub rax, r12
003E130F  48 C1 F8 03                     sar rax, 3
003E1313  FF C0                           inc eax
003E1315  C1 E0 06                        shl eax, 6
003E1318  41 2B C1                        sub eax, r9d
003E131B  8B D0                           mov edx, eax
003E131D  41 3B C5                        cmp eax, r13d
003E1320  0F 86 C1 01 00 00               jbe 0x1403e14e7
003E1326  41 BD FF FF FF FF               mov r13d, 0xffffffff
003E132C  41 8B D5                        mov edx, r13d
003E132F  8B B4 24 A0 00 00 00            mov esi, dword ptr [rsp + 0xa0]
003E1336  4C 8B 4C 24 38                  mov r9, qword ptr [rsp + 0x38]
003E133B  44 8B 84 24 98 00 00 00         mov r8d, dword ptr [rsp + 0x98]
003E1343  39 9C 24 A8 00 00 00            cmp dword ptr [rsp + 0xa8], ebx
003E134A  0F 84 00 FF FF FF               je 0x1403e1250
003E1350  44 8B 5C 24 30                  mov r11d, dword ptr [rsp + 0x30]
003E1355  41 8D 0C 36                     lea ecx, [r14 + rsi]
003E1359  4C 8B 64 24 40                  mov r12, qword ptr [rsp + 0x40]
003E135E  41 3B C8                        cmp ecx, r8d
003E1361  8B C3                           mov eax, ebx
003E1363  41 0F 47 C8                     cmova ecx, r8d
003E1367  41 03 CD                        add ecx, r13d
003E136A  E9 14 FE FF FF                  jmp 0x1403e1183
003E136F  48 81 C5 FF 0F 00 00            add rbp, 0xfff
003E1376  48 81 E5 00 F0 FF FF            and rbp, 0xfffffffffffff000
003E137D  48 8B D5                        mov rdx, rbp
003E1380  E9 42 FF FF FF                  jmp 0x1403e12c7
003E1385  48 89 07                        mov qword ptr [rdi], rax
003E1388  48 8D 0D 21 19 BE 00            lea rcx, [rip + 0xbe1921]
003E138F  4C 89 67 08                     mov qword ptr [rdi + 8], r12
003E1393  8A D3                           mov dl, bl
003E1395  48 89 78 08                     mov qword ptr [rax + 8], rdi
003E1399  48 89 3D 00 19 BE 00            mov qword ptr [rip + 0xbe1900], rdi
003E13A0  E8 FB 17 FB FF                  call 0x140392ba0
003E13A5  48 8B DE                        mov rbx, rsi
003E13A8  48 C1 E3 04                     shl rbx, 4
003E13AC  48 03 5F 10                     add rbx, qword ptr [rdi + 0x10]
003E13B0  48 81 FD 00 10 00 00            cmp rbp, 0x1000
003E13B7  0F 82 39 02 00 00               jb 0x1403e15f6
003E13BD  44 89 77 1C                     mov dword ptr [rdi + 0x1c], r14d
003E13C1  48 8B C3                        mov rax, rbx
003E13C4  48 83 C4 50                     add rsp, 0x50
003E13C8  41 5E                           pop r14
003E13CA  41 5D                           pop r13
003E13CC  41 5C                           pop r12
003E13CE  5F                              pop rdi
003E13CF  5E                              pop rsi
003E13D0  5D                              pop rbp
003E13D1  5B                              pop rbx
003E13D2  C3                              ret
003E13D3  CC                              int3
003E13D4  41 8B C2                        mov eax, r10d
003E13D7  8B D3                           mov edx, ebx
003E13D9  48 C1 E8 06                     shr rax, 6
003E13DD  4D 8D 1C C4                     lea r11, [r12 + rax*8]
003E13E1  49 83 F9 FF                     cmp r9, -1
003E13E5  74 78                           je 0x1403e145f
003E13E7  49 0F BC C1                     bsf rax, r9
003E13EB  0F 44 C1                        cmove eax, ecx
003E13EE  03 C2                           add eax, edx
003E13F0  41 3B C6                        cmp eax, r14d
003E13F3  73 66                           jae 0x1403e145b
003E13F5  49 8B D1                        mov rdx, r9
003E13F8  45 8B D6                        mov r10d, r14d
003E13FB  48 F7 D2                        not rdx
003E13FE  48 8B C2                        mov rax, rdx
003E1401  41 8B CA                        mov ecx, r10d
003E1404  D1 E9                           shr ecx, 1
003E1406  48 D3 E8                        shr rax, cl
003E1409  48 23 D0                        and rdx, rax
003E140C  0F 84 90 01 00 00               je 0x1403e15a2
003E1412  44 2B D1                        sub r10d, ecx
003E1415  41 83 FA 01                     cmp r10d, 1
003E1419  77 E3                           ja 0x1403e13fe
003E141B  48 0F BC D2                     bsf rdx, rdx
003E141F  4D 2B C4                        sub r8, r12
003E1422  49 C1 F8 03                     sar r8, 3
003E1426  41 C1 E0 06                     shl r8d, 6
003E142A  41 03 D0                        add edx, r8d
003E142D  41 3B D5                        cmp edx, r13d
003E1430  0F 87 F0 FE FF FF               ja 0x1403e1326
003E1436  44 8B 5C 24 30                  mov r11d, dword ptr [rsp + 0x30]
003E143B  E9 FE FD FF FF                  jmp 0x1403e123e
003E1440  4D 85 C9                        test r9, r9
003E1443  0F 89 AD FE FF FF               jns 0x1403e12f6
003E1449  49 83 C0 08                     add r8, 8
003E144D  4C 3B C6                        cmp r8, rsi
003E1450  0F 87 D0 FE FF FF               ja 0x1403e1326
003E1456  4D 8B 08                        mov r9, qword ptr [r8]
003E1459  EB E5                           jmp 0x1403e1440
003E145B  F7 DA                           neg edx
003E145D  EB C0                           jmp 0x1403e141f
003E145F  49 83 C0 08                     add r8, 8
003E1463  4C 3B C6                        cmp r8, rsi
003E1466  0F 87 BA FE FF FF               ja 0x1403e1326
003E146C  4D 8B 08                        mov r9, qword ptr [r8]
003E146F  49 83 F9 FF                     cmp r9, -1
003E1473  74 EA                           je 0x1403e145f
003E1475  8B D3                           mov edx, ebx
003E1477  E9 6B FF FF FF                  jmp 0x1403e13e7
003E147C  41 F6 C5 3F                     test r13b, 0x3f
003E1480  4C 8D 56 08                     lea r10, [rsi + 8]
003E1484  4C 0F 44 D6                     cmove r10, rsi
003E1488  4D 85 C9                        test r9, r9
003E148B  0F 84 F8 00 00 00               je 0x1403e1589
003E1491  49 83 C0 08                     add r8, 8
003E1495  49 39 18                        cmp qword ptr [r8], rbx
003E1498  0F 85 B9 00 00 00               jne 0x1403e1557
003E149E  49 0F BD C1                     bsr rax, r9
003E14A2  0F 84 E8 00 00 00               je 0x1403e1590
003E14A8  B9 3F 00 00 00                  mov ecx, 0x3f
003E14AD  2B C8                           sub ecx, eax
003E14AF  49 8B D0                        mov rdx, r8
003E14B2  49 2B D4                        sub rdx, r12
003E14B5  48 C1 FA 03                     sar rdx, 3
003E14B9  C1 E2 06                        shl edx, 6
003E14BC  2B D1                           sub edx, ecx
003E14BE  41 3B D5                        cmp edx, r13d
003E14C1  0F 87 5F FE FF FF               ja 0x1403e1326
003E14C7  41 8B C6                        mov eax, r14d
003E14CA  2B C1                           sub eax, ecx
003E14CC  44 8B C8                        mov r9d, eax
003E14CF  48 C1 E8 06                     shr rax, 6
003E14D3  49 8D 0C C0                     lea rcx, [r8 + rax*8]
003E14D7  49 83 C0 08                     add r8, 8
003E14DB  4C 3B C1                        cmp r8, rcx
003E14DE  74 55                           je 0x1403e1535
003E14E0  49 39 18                        cmp qword ptr [r8], rbx
003E14E3  74 F2                           je 0x1403e14d7
003E14E5  EB 70                           jmp 0x1403e1557
003E14E7  41 8B CE                        mov ecx, r14d
003E14EA  41 2B C9                        sub ecx, r9d
003E14ED  0F 84 4B FD FF FF               je 0x1403e123e
003E14F3  49 83 C0 08                     add r8, 8
003E14F7  41 BA 40 00 00 00               mov r10d, 0x40
003E14FD  49 8B 00                        mov rax, qword ptr [r8]
003E1500  4C 8B C8                        mov r9, rax
003E1503  41 3B CA                        cmp ecx, r10d
003E1506  72 15                           jb 0x1403e151d
003E1508  48 85 C0                        test rax, rax
003E150B  75 20                           jne 0x1403e152d
003E150D  83 C1 C0                        add ecx, -0x40
003E1510  0F 84 28 FD FF FF               je 0x1403e123e
003E1516  49 83 C0 08                     add r8, 8
003E151A  4D 8B 08                        mov r9, qword ptr [r8]
003E151D  49 0F BC C1                     bsf rax, r9
003E1521  41 0F 44 C2                     cmove eax, r10d
003E1525  3B C1                           cmp eax, ecx
003E1527  0F 83 11 FD FF FF               jae 0x1403e123e
003E152D  41 8B CA                        mov ecx, r10d
003E1530  E9 0B FF FF FF                  jmp 0x1403e1440
003E1535  41 83 E1 3F                     and r9d, 0x3f
003E1539  0F 84 FF FC FF FF               je 0x1403e123e
003E153F  49 8B 00                        mov rax, qword ptr [r8]
003E1542  48 0F BC C8                     bsf rcx, rax
003E1546  B8 40 00 00 00                  mov eax, 0x40
003E154B  0F 44 C8                        cmove ecx, eax
003E154E  41 3B C9                        cmp ecx, r9d
003E1551  0F 83 E7 FC FF FF               jae 0x1403e123e
003E1557  49 8B C0                        mov rax, r8
003E155A  4D 3B C2                        cmp r8, r10
003E155D  0F 87 C3 FD FF FF               ja 0x1403e1326
003E1563  49 83 C0 08                     add r8, 8
003E1567  49 39 18                        cmp qword ptr [r8], rbx
003E156A  75 EB                           jne 0x1403e1557
003E156C  48 8B 00                        mov rax, qword ptr [rax]
003E156F  48 0F BD D0                     bsr rdx, rax
003E1573  74 1B                           je 0x1403e1590
003E1575  B9 3F 00 00 00                  mov ecx, 0x3f
003E157A  2B CA                           sub ecx, edx
003E157C  E9 2E FF FF FF                  jmp 0x1403e14af
003E1581  83 E2 F8                        and edx, 0xfffffff8
003E1584  E9 C7 FC FF FF                  jmp 0x1403e1250
003E1589  8B CB                           mov ecx, ebx
003E158B  E9 1F FF FF FF                  jmp 0x1403e14af
003E1590  B9 40 00 00 00                  mov ecx, 0x40
003E1595  E9 15 FF FF FF                  jmp 0x1403e14af
003E159A  44 8B C9                        mov r9d, ecx
003E159D  E9 67 FD FF FF                  jmp 0x1403e1309
003E15A2  4D 3B C3                        cmp r8, r11
003E15A5  0F 84 7B FD FF FF               je 0x1403e1326
003E15AB  49 0F BD C1                     bsr rax, r9
003E15AF  B9 40 00 00 00                  mov ecx, 0x40
003E15B4  74 11                           je 0x1403e15c7
003E15B6  8D 51 FF                        lea edx, [rcx - 1]
003E15B9  2B D0                           sub edx, eax
003E15BB  49 83 C0 08                     add r8, 8
003E15BF  4D 8B 08                        mov r9, qword ptr [r8]
003E15C2  E9 1A FE FF FF                  jmp 0x1403e13e1
003E15C7  8B D1                           mov edx, ecx
003E15C9  EB F0                           jmp 0x1403e15bb
003E15CB  4C 8D 0D 8E 26 C4 FF            lea r9, [rip - 0x3bd972]
003E15D2  48 C7 44 24 20 DC 0B 00 00      mov qword ptr [rsp + 0x20], 0xbdc
003E15DB  33 D2                           xor edx, edx
003E15DD  B9 AC 00 00 00                  mov ecx, 0xac
003E15E2  41 B8 A0 A0 00 00               mov r8d, 0xa0a0
003E15E8  E8 73 C0 11 00                  call 0x1404fd660
003E15ED  CC                              int3
003E15EE  41 8B D5                        mov edx, r13d
003E15F1  E9 4D FD FF FF                  jmp 0x1403e1343
003E15F6  48 89 3B                        mov qword ptr [rbx], rdi
003E15F9  44 89 73 08                     mov dword ptr [rbx + 8], r14d
003E15FD  48 83 C3 10                     add rbx, 0x10
003E1601  E9 BB FD FF FF                  jmp 0x1403e13c1
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpMmAllocCtxAlloc(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned int v_stack_m58;
    unsigned int v_stack_p10;
    unsigned int v_stack_p18;
    unsigned int v_stack_p20;
    unsigned int v_stack_p30;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (80);
    v_rbx = 0;
    if (a2 == 0) goto loc_003E15CB;
    result = (a2 + 15) & (-16);
    v_rbp = result + 16;
    if (result >= 0x1000ULL) { v_rbp = result; }
    v_r14 = (v_rbp) >> (4);
    if (v_rbp >= 0x1000ULL) goto loc_003E136F;
    result = KeAcquireSpinLockRaiseToDpc(v_rip + 12458914, a2, a3, a4);
    v_stack_p8 = (unsigned __int8)(result);
loc_003E1127:
    if ((*(unsigned __int64 *)(v_rip + 12458886)) == (v_rip + 12458956)) goto loc_003E12AF;
    v_stack_p18 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12458886) + 24)));
    a2 = (unsigned int)((a2) & ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12458886) + 24)))));
    v_stack_p10 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12458886) + 32)));
    v_stack_m48 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12458886) + 40);
    if ((unsigned int)(v_r14) == 0) goto loc_003E1581;
    a4 = (unsigned int)((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12458886) + 40)) & (4));
    v_stack_m50 = a4;
    result = -((unsigned int)((unsigned int)(a4)));
    v_r11 = (unsigned int)((v_r11) & (32));
    v_stack_m58 = (unsigned int)(v_r11);
loc_003E1183:
    v_stack_p20 = (unsigned int)((unsigned int)((unsigned int)(a2)));
    result = -(a4);
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r11 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12458886) + 32)) - 1 * 1))) - ((unsigned int)(v_r11 + (unsigned int)((unsigned int)(a2)) * 1)));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12458886) + 32)) - 1) & (4));
    result = (unsigned int)((result) + 1);
    v_r12 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12458886) + 40)) - (a1);
    if (((unsigned int)(result)) < ((unsigned int)(v_r14))) goto loc_003E15EE;
    v_r13 = (unsigned int)(((unsigned int)((unsigned int)(v_r11 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12458886) + 32)) - 1 * 1))) - ((unsigned int)(v_r14)));
    a1 = (unsigned __int8)(((unsigned int)((unsigned int)(v_r11 + (unsigned int)((unsigned int)(a2)) * 1))) & (63));
    v_r13 = (unsigned int)((v_r13) + 1);
    a4 = (1) << ((unsigned __int8)(a1));
    a4 = (a4) - 1;
    result = ((unsigned int)((unsigned int)(v_r13))) >> (6);
    result = ((unsigned int)((unsigned int)(v_r11 + (unsigned int)((unsigned int)(a2)) * 1))) >> (6);
    a4 = (a4) | (*(unsigned __int64 *)(v_r12 + result * 8));
    if (((unsigned int)(v_r14)) > 127) goto loc_003E147C;
    if (((unsigned int)(v_r14)) >= 64) goto loc_003E1440;
    if (((unsigned int)(v_r14)) > 1) goto loc_003E13D4;
loc_003E1205:
    if (a4 != -1) goto loc_003E121D;
    a3 = (v_r12 + result * 8) + (8);
    if (a3 > (v_r12 + result * 8)) goto loc_003E1326;
    goto loc_003E1205;
loc_003E121D:
    a3 = (a3) - (v_r12);
    a4 = ~(*(unsigned __int64 *)(a3));
    a3 = (a3) >> (3);
    a3 = (unsigned int)((a3) << (6));
    a3 = (unsigned int)((a3) + ((unsigned int)(result)));
    if (((unsigned int)(a3)) > ((unsigned int)(v_r13))) goto loc_003E1326;
loc_003E123E:
    if (((unsigned int)((unsigned int)((unsigned int)(a3)))) == ((unsigned int)((unsigned int)(0xFFFFFFFFULL)))) goto loc_003E132F;
    a2 = (unsigned int)(((unsigned int)((unsigned int)(a3))) - ((unsigned int)(v_r11)));
loc_003E1250:
    if (((unsigned int)((unsigned int)(a2))) == ((unsigned int)(0xFFFFFFFFULL))) goto loc_003E12EE;
loc_003E1269:
    result = RtlSetBits(*(unsigned __int64 *)(v_rip + 12458886) + 32, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(a2)))), (unsigned int)((unsigned int)(v_r14)), a4);
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 12458886) + 24) = (unsigned int)(v_r14 + (unsigned int)((unsigned int)(a2)) * 1);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12458886)) + 8)) != (*(unsigned __int64 *)(v_rip + 12458886))) goto loc_003E12A8;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12458886) + 8))) != (*(unsigned __int64 *)(v_rip + 12458886))) goto loc_003E12A8;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12458886) + 8)) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12458886));
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12458886)) + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12458886) + 8);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12458498) + 8)) == (v_rip + 12458567)) goto loc_003E1385;
loc_003E12A8:
loc_003E12AF:
    result = KeReleaseSpinLock(v_rip + 12458483, v_stack_p8, (unsigned int)((unsigned int)(v_r14)), a4);
loc_003E12C7:
    result = HalpMmAllocCtxAllocBuffer(v_rip + 12458483, (unsigned int)(0x4000ULL), (unsigned int)((unsigned int)(v_r14)), a4);
    if (result == 0) goto loc_003E13C1;
    result = KeAcquireSpinLockRaiseToDpc(v_rip + 12458449, (unsigned int)(0x4000ULL), (unsigned int)((unsigned int)(v_r14)), a4);
    goto loc_003E1269;
loc_003E12EE:
    goto loc_003E1127;
loc_003E12F6:
    if (result == 0) goto loc_003E159A;
    a4 = (unsigned int)((63) - ((unsigned int)(result)));
loc_003E1309:
    result = ((unsigned int)((unsigned int)(v_r14))) - (v_rip + 12458567);
    result = (result) >> (3);
    result = (unsigned int)((result) + 1);
    result = (unsigned int)((result) << (6));
    result = (unsigned int)((result) - ((unsigned int)(a4)));
    if (((unsigned int)(result)) <= ((unsigned int)((unsigned int)(0xFFFFFFFFULL)))) goto loc_003E14E7;
loc_003E1326:
loc_003E132F:
loc_003E1343:
    if (v_stack_p20 == ((unsigned int)((unsigned __int8)(result)))) goto loc_003E1250;
    a1 = v_r14 + (unsigned int)(v_stack_p18) * 1;
    if (((unsigned int)(v_r14 + (unsigned int)(v_stack_p18) * 1)) > ((unsigned int)((unsigned int)(v_stack_p10)))) { a1 = (unsigned int)((unsigned int)(v_stack_p10)); }
    a1 = (unsigned int)((a1) + ((unsigned int)((unsigned int)(0xFFFFFFFFULL))));
    goto loc_003E1183;
loc_003E136F:
    v_rbp = (v_rbp) + (0xFFFULL);
    v_rbp = (v_rbp) & (0xFFFFFFFFFFFFF000ULL);
    goto loc_003E12C7;
loc_003E1385:
    *(unsigned __int64 *)(*(unsigned __int64 *)(result)) = (unsigned int)((unsigned int)((unsigned __int8)(result)));
    *(unsigned __int64 *)(*(unsigned __int64 *)(result) + 8) = v_stack_m48;
    *(unsigned __int64 *)((unsigned int)((unsigned int)((unsigned __int8)(result))) + 8) = *(unsigned __int64 *)(result);
    *(unsigned __int64 *)(v_rip + 12458240) = *(unsigned __int64 *)(result);
    result = KeReleaseSpinLock(v_rip + 12458273, (unsigned __int8)((unsigned __int8)(result)), (unsigned int)(v_stack_p10), v_stack_m50);
    v_rbx = ((unsigned int)(v_stack_p18)) << (4);
    v_rbx = (v_rbx) + (*(unsigned __int64 *)(*(unsigned __int64 *)(result) + 16));
    if (v_rbp < 0x1000ULL) goto loc_003E15F6;
    *(unsigned int *)(*(unsigned __int64 *)(result) + 28) = (unsigned int)(v_r14);
loc_003E13C1:
    v_rsp = (v_rsp) + (80);
    return v_rbx;
loc_003E13D4:
    result = ((unsigned int)((unsigned int)(v_r11 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12458886) + 32)) - 1 * 1))) >> (6);
loc_003E13E1:
    if (v_stack_m50 == -1) goto loc_003E145F;
loc_003E13E7:
    if (v_stack_m50 == -1) { result = (unsigned int)(v_rip + 12458273); }
    result = (unsigned int)((result) + ((unsigned int)((unsigned int)((unsigned int)(v_rbx)))));
    if (((unsigned int)(result)) >= ((unsigned int)(v_r14))) goto loc_003E145B;
    a2 = ~(v_stack_m50);
loc_003E13FE:
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r14))))) >> (1));
    result = (a2) >> ((unsigned __int8)(a1));
    a2 = (a2) & (result);
    if (condition_is_equal) goto loc_003E15A2;
    v_r10 = (unsigned int)(((unsigned int)((unsigned int)(v_r14))) - ((unsigned int)(a1)));
    if (((unsigned int)(v_r10)) > 1) goto loc_003E13FE;
loc_003E141F:
    a3 = ((unsigned int)(v_stack_p10)) - (v_stack_m48);
    a3 = (a3) >> (3);
    a3 = (unsigned int)((a3) << (6));
    a2 = (unsigned int)((a2) + ((unsigned int)(a3)));
    if (((unsigned int)(a2)) > ((unsigned int)((unsigned int)(0xFFFFFFFFULL)))) goto loc_003E1326;
    goto loc_003E123E;
loc_003E1440:
    if (!sign_flag) goto loc_003E12F6;
    a3 = (a3) + (8);
    if (a3 > ((unsigned int)(v_stack_p18))) goto loc_003E1326;
    goto loc_003E1440;
loc_003E145B:
    a2 = (unsigned int)(-(a2));
    goto loc_003E141F;
loc_003E145F:
    a3 = (a3) + (8);
    if (a3 > ((unsigned int)(v_stack_p18))) goto loc_003E1326;
    if ((*(unsigned __int64 *)(a3)) == -1) goto loc_003E145F;
    goto loc_003E13E7;
loc_003E147C:
    v_r10 = (unsigned int)(v_stack_p18) + 8;
    if ((((unsigned __int8)((unsigned int)(0xFFFFFFFFULL))) & (63)) == 0) { v_r10 = (unsigned int)(v_stack_p18); }
    if (*(unsigned __int64 *)(a3) == 0) goto loc_003E1589;
    a3 = (a3) + (8);
    if ((*(unsigned __int64 *)(a3)) != v_rbx) goto loc_003E1557;
    if ((*(unsigned __int64 *)(a3)) == v_rbx) goto loc_003E1590;
    a1 = (unsigned int)((63) - ((unsigned int)(result)));
loc_003E14AF:
    a2 = (a3) - (v_stack_m48);
    a2 = (a2) >> (3);
    a2 = (unsigned int)((a2) << (6));
    a2 = (unsigned int)((a2) - ((unsigned int)(a1)));
    if (((unsigned int)(a2)) > ((unsigned int)((unsigned int)(0xFFFFFFFFULL)))) goto loc_003E1326;
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r14))) - ((unsigned int)(a1)));
    result = (result) >> (6);
loc_003E14D7:
    a3 = (a3) + (8);
    if (a3 == (a3 + result * 8)) goto loc_003E1535;
    if ((*(unsigned __int64 *)(a3)) == v_rbx) goto loc_003E14D7;
    goto loc_003E1557;
loc_003E14E7:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_r14))) - ((unsigned int)((unsigned int)((unsigned int)(result)))));
    if (condition_is_equal) goto loc_003E123E;
    a3 = (a3) + (8);
    if (((unsigned int)(a1)) < 64) goto loc_003E151D;
    if (*(unsigned __int64 *)(a3) != 0) goto loc_003E152D;
    a1 = (unsigned int)((a1) + (-64));
    if (condition_is_equal) goto loc_003E123E;
    a3 = (a3) + (8);
loc_003E151D:
    result = *(unsigned __int64 *)(a3);
    if (condition_is_equal) { result = 64; }
    if (((unsigned int)(result)) >= ((unsigned int)(a1))) goto loc_003E123E;
loc_003E152D:
    goto loc_003E1440;
loc_003E1535:
    a4 = (unsigned int)((*(unsigned __int64 *)(a3)) & (63));
    if (condition_is_equal) goto loc_003E123E;
    a1 = 64;
    if (condition_is_equal) { a1 = 64; }
    if (((unsigned int)(a1)) >= ((unsigned int)(a4))) goto loc_003E123E;
loc_003E1557:
    if (a3 > 64) goto loc_003E1326;
    a3 = (a3) + (8);
    if ((*(unsigned __int64 *)(a3)) != v_rbx) goto loc_003E1557;
    if ((*(unsigned __int64 *)(a3)) == v_rbx) goto loc_003E1590;
    a1 = (unsigned int)((63) - ((unsigned int)(a2)));
    goto loc_003E14AF;
loc_003E1581:
    a2 = (unsigned int)((a2) & (0xFFFFFFF8ULL));
    goto loc_003E1250;
loc_003E1589:
    goto loc_003E14AF;
loc_003E1590:
    goto loc_003E14AF;
loc_003E159A:
    goto loc_003E1309;
loc_003E15A2:
    if (a3 == ((unsigned int)(v_stack_p30))) goto loc_003E1326;
    if (a3 == ((unsigned int)(v_stack_p30))) goto loc_003E15C7;
    a2 = (unsigned int)((64 - 1) - ((unsigned int)(*(unsigned __int64 *)(a3))));
loc_003E15BB:
    a3 = (a3) + (8);
    goto loc_003E13E1;
loc_003E15C7:
    goto loc_003E15BB;
loc_003E15CB:
    v_stack_p20 = 0xBDCULL;
    a2 = 0;
    result = KeBugCheckEx(172, a2, (unsigned int)(0xA0A0ULL), v_rip - 3922290);
loc_003E15EE:
    goto loc_003E1343;
loc_003E15F6:
    *(unsigned __int64 *)(v_rbx) = *(unsigned __int64 *)(result);
    *(unsigned int *)(v_rbx + 8) = (unsigned int)(v_r14);
    v_rbx = (v_rbx) + (16);
    goto loc_003E13C1;
}
```

## 5. (Beta) C Style

```c
int64_t HalpMmAllocCtxAlloc(int64_t Arg1, int64_t Arg2)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint32_t v_stack_m58;
    uint32_t v_stack_p10;
    uint32_t v_stack_p18;
    uint32_t v_stack_p20;
    uint32_t v_stack_p30;
    uint64_t v_stack_p8;

    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (80);
    local_rbx = 0;
    if (Arg2 == 0) goto loc_003E15CB;
    result = (Arg2 + 15) & (-16);
    local_rbp = result + 16;
    if (result >= 0x1000ULL) { local_rbp = result; }
    local_r14 = (local_rbp) >> (4);
    if (local_rbp >= 0x1000ULL) goto loc_003E136F;
    result = KeAcquireSpinLockRaiseToDpc(v_rip + 12458914, Arg2, a3, a4);
    v_stack_p8 = (uint8_t)(result);
loc_003E1127:
    if ((*(uint64_t *)(v_rip + 0xBE1B86)) == (v_rip + 12458956)) goto loc_003E12AF;
    v_stack_p18 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xBE1B86) + 0x18)));
    Arg2 = (uint32_t)((Arg2) & ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xBE1B86) + 0x18)))));
    v_stack_p10 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xBE1B86) + 0x20)));
    v_stack_m48 = *(uint64_t *)(*(uint64_t *)(v_rip + 0xBE1B86) + 0x28);
    if ((uint32_t)(local_r14) == 0) goto loc_003E1581;
    a4 = (uint32_t)((*(uint64_t *)(*(uint64_t *)(v_rip + 0xBE1B86) + 0x28)) & (4));
    v_stack_m50 = a4;
    result = -((uint32_t)((uint32_t)(a4)));
    local_r11 = (uint32_t)((local_r11) & (32));
    v_stack_m58 = (uint32_t)(local_r11);
loc_003E1183:
    v_stack_p20 = (uint32_t)((uint32_t)((uint32_t)(Arg2)));
    result = -(a4);
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r11 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xBE1B86) + 0x20)) - 1 * 1))) - ((uint32_t)(local_r11 + (uint32_t)((uint32_t)(Arg2)) * 1)));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xBE1B86) + 0x20)) - 1) & (4));
    result = (uint32_t)((result) + 1);
    local_r12 = (*(uint64_t *)(*(uint64_t *)(v_rip + 0xBE1B86) + 0x28)) - (Arg1);
    if (((uint32_t)(result)) < ((uint32_t)(local_r14))) goto loc_003E15EE;
    local_r13 = (uint32_t)(((uint32_t)((uint32_t)(local_r11 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xBE1B86) + 0x20)) - 1 * 1))) - ((uint32_t)(local_r14)));
    Arg1 = (uint8_t)(((uint32_t)((uint32_t)(local_r11 + (uint32_t)((uint32_t)(Arg2)) * 1))) & (63));
    local_r13 = (uint32_t)((local_r13) + 1);
    a4 = (1) << ((uint8_t)(Arg1));
    a4 = (a4) - 1;
    result = ((uint32_t)((uint32_t)(local_r13))) >> (6);
    result = ((uint32_t)((uint32_t)(local_r11 + (uint32_t)((uint32_t)(Arg2)) * 1))) >> (6);
    a4 = (a4) | (*(uint64_t *)(local_r12 + result * 8));
    if (((uint32_t)(local_r14)) > 127) goto loc_003E147C;
    if (((uint32_t)(local_r14)) >= 64) goto loc_003E1440;
    if (((uint32_t)(local_r14)) > 1) goto loc_003E13D4;
loc_003E1205:
    if (a4 != -1) goto loc_003E121D;
    a3 = (local_r12 + result * 8) + (8);
    if (a3 > (local_r12 + result * 8)) goto loc_003E1326;
    goto loc_003E1205;
loc_003E121D:
    a3 = (a3) - (local_r12);
    a4 = ~(*(uint64_t *)(a3));
    a3 = (a3) >> (3);
    a3 = (uint32_t)((a3) << (6));
    a3 = (uint32_t)((a3) + ((uint32_t)(result)));
    if (((uint32_t)(a3)) > ((uint32_t)(local_r13))) goto loc_003E1326;
loc_003E123E:
    if (((uint32_t)((uint32_t)((uint32_t)(a3)))) == ((uint32_t)((uint32_t)(0xFFFFFFFFULL)))) goto loc_003E132F;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(a3))) - ((uint32_t)(local_r11)));
loc_003E1250:
    if (((uint32_t)((uint32_t)(Arg2))) == ((uint32_t)(0xFFFFFFFFULL))) goto loc_003E12EE;
loc_003E1269:
    result = RtlSetBits(*(uint64_t *)(v_rip + 0xBE1B86) + 32, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg2)))), (uint32_t)((uint32_t)(local_r14)), a4);
    *(uint32_t *)(*(uint64_t *)(v_rip + 0xBE1B86) + 0x18) = (uint32_t)(local_r14 + (uint32_t)((uint32_t)(Arg2)) * 1);
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xBE1B86)) + 0x8)) != (*(uint64_t *)(v_rip + 0xBE1B86))) goto loc_003E12A8;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xBE1B86) + 0x8))) != (*(uint64_t *)(v_rip + 0xBE1B86))) goto loc_003E12A8;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xBE1B86) + 0x8)) = *(uint64_t *)(*(uint64_t *)(v_rip + 0xBE1B86));
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xBE1B86)) + 0x8) = *(uint64_t *)(*(uint64_t *)(v_rip + 0xBE1B86) + 0x8);
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xBE1A02) + 0x8)) == (v_rip + 12458567)) goto loc_003E1385;
loc_003E12A8:
loc_003E12AF:
    result = KeReleaseSpinLock(v_rip + 12458483, v_stack_p8, (uint32_t)((uint32_t)(local_r14)), a4);
loc_003E12C7:
    result = HalpMmAllocCtxAllocBuffer(v_rip + 12458483, (uint32_t)(0x4000ULL), (uint32_t)((uint32_t)(local_r14)), a4);
    if (result == 0) goto loc_003E13C1;
    result = KeAcquireSpinLockRaiseToDpc(v_rip + 12458449, (uint32_t)(0x4000ULL), (uint32_t)((uint32_t)(local_r14)), a4);
    goto loc_003E1269;
loc_003E12EE:
    goto loc_003E1127;
loc_003E12F6:
    if (result == 0) goto loc_003E159A;
    a4 = (uint32_t)((63) - ((uint32_t)(result)));
loc_003E1309:
    result = ((uint32_t)((uint32_t)(local_r14))) - (v_rip + 12458567);
    result = (result) >> (3);
    result = (uint32_t)((result) + 1);
    result = (uint32_t)((result) << (6));
    result = (uint32_t)((result) - ((uint32_t)(a4)));
    if (((uint32_t)(result)) <= ((uint32_t)((uint32_t)(0xFFFFFFFFULL)))) goto loc_003E14E7;
loc_003E1326:
loc_003E132F:
loc_003E1343:
    if (v_stack_p20 == ((uint32_t)((uint8_t)(result)))) goto loc_003E1250;
    Arg1 = local_r14 + (uint32_t)(v_stack_p18) * 1;
    if (((uint32_t)(local_r14 + (uint32_t)(v_stack_p18) * 1)) > ((uint32_t)((uint32_t)(v_stack_p10)))) { Arg1 = (uint32_t)((uint32_t)(v_stack_p10)); }
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)((uint32_t)(0xFFFFFFFFULL))));
    goto loc_003E1183;
loc_003E136F:
    local_rbp = (local_rbp) + (0xFFFULL);
    local_rbp = (local_rbp) & (0xFFFFFFFFFFFFF000ULL);
    goto loc_003E12C7;
loc_003E1385:
    *(uint64_t *)(*(uint64_t *)(result)) = (uint32_t)((uint32_t)((uint8_t)(result)));
    *(uint64_t *)(*(uint64_t *)(result) + 0x8) = v_stack_m48;
    *(uint64_t *)((uint32_t)((uint32_t)((uint8_t)(result))) + 0x8) = *(uint64_t *)(result);
    *(uint64_t *)(v_rip + 0xBE1900) = *(uint64_t *)(result);
    result = KeReleaseSpinLock(v_rip + 12458273, (uint8_t)((uint8_t)(result)), (uint32_t)(v_stack_p10), v_stack_m50);
    local_rbx = ((uint32_t)(v_stack_p18)) << (4);
    local_rbx = (local_rbx) + (*(uint64_t *)(*(uint64_t *)(result) + 0x10));
    if (local_rbp < 0x1000ULL) goto loc_003E15F6;
    *(uint32_t *)(*(uint64_t *)(result) + 0x1C) = (uint32_t)(local_r14);
loc_003E13C1:
    local_rsp = (local_rsp) + (80);
    return local_rbx;
loc_003E13D4:
    result = ((uint32_t)((uint32_t)(local_r11 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xBE1B86) + 0x20)) - 1 * 1))) >> (6);
loc_003E13E1:
    if (v_stack_m50 == -1) goto loc_003E145F;
loc_003E13E7:
    if (v_stack_m50 == -1) { result = (uint32_t)(v_rip + 12458273); }
    result = (uint32_t)((result) + ((uint32_t)((uint32_t)((uint32_t)(local_rbx)))));
    if (((uint32_t)(result)) >= ((uint32_t)(local_r14))) goto loc_003E145B;
    Arg2 = ~(v_stack_m50);
loc_003E13FE:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r14))))) >> (1));
    result = (Arg2) >> ((uint8_t)(Arg1));
    Arg2 = (Arg2) & (result);
    if (condition_is_equal) goto loc_003E15A2;
    local_r10 = (uint32_t)(((uint32_t)((uint32_t)(local_r14))) - ((uint32_t)(Arg1)));
    if (((uint32_t)(local_r10)) > 1) goto loc_003E13FE;
loc_003E141F:
    a3 = ((uint32_t)(v_stack_p10)) - (v_stack_m48);
    a3 = (a3) >> (3);
    a3 = (uint32_t)((a3) << (6));
    Arg2 = (uint32_t)((Arg2) + ((uint32_t)(a3)));
    if (((uint32_t)(Arg2)) > ((uint32_t)((uint32_t)(0xFFFFFFFFULL)))) goto loc_003E1326;
    goto loc_003E123E;
loc_003E1440:
    if (!sign_flag) goto loc_003E12F6;
    a3 = (a3) + (8);
    if (a3 > ((uint32_t)(v_stack_p18))) goto loc_003E1326;
    goto loc_003E1440;
loc_003E145B:
    Arg2 = (uint32_t)(-(Arg2));
    goto loc_003E141F;
loc_003E145F:
    a3 = (a3) + (8);
    if (a3 > ((uint32_t)(v_stack_p18))) goto loc_003E1326;
    if ((*(uint64_t *)(a3)) == -1) goto loc_003E145F;
    goto loc_003E13E7;
loc_003E147C:
    local_r10 = (uint32_t)(v_stack_p18) + 8;
    if ((((uint8_t)((uint32_t)(0xFFFFFFFFULL))) & (63)) == 0) { local_r10 = (uint32_t)(v_stack_p18); }
    if (*(uint64_t *)(a3) == 0) goto loc_003E1589;
    a3 = (a3) + (8);
    if ((*(uint64_t *)(a3)) != local_rbx) goto loc_003E1557;
    if ((*(uint64_t *)(a3)) == local_rbx) goto loc_003E1590;
    Arg1 = (uint32_t)((63) - ((uint32_t)(result)));
loc_003E14AF:
    Arg2 = (a3) - (v_stack_m48);
    Arg2 = (Arg2) >> (3);
    Arg2 = (uint32_t)((Arg2) << (6));
    Arg2 = (uint32_t)((Arg2) - ((uint32_t)(Arg1)));
    if (((uint32_t)(Arg2)) > ((uint32_t)((uint32_t)(0xFFFFFFFFULL)))) goto loc_003E1326;
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r14))) - ((uint32_t)(Arg1)));
    result = (result) >> (6);
loc_003E14D7:
    a3 = (a3) + (8);
    if (a3 == (a3 + result * 8)) goto loc_003E1535;
    if ((*(uint64_t *)(a3)) == local_rbx) goto loc_003E14D7;
    goto loc_003E1557;
loc_003E14E7:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_r14))) - ((uint32_t)((uint32_t)((uint32_t)(result)))));
    if (condition_is_equal) goto loc_003E123E;
    a3 = (a3) + (8);
    if (((uint32_t)(Arg1)) < 64) goto loc_003E151D;
    if (*(uint64_t *)(a3) != 0) goto loc_003E152D;
    Arg1 = (uint32_t)((Arg1) + (-64));
    if (condition_is_equal) goto loc_003E123E;
    a3 = (a3) + (8);
loc_003E151D:
    result = *(uint64_t *)(a3);
    if (condition_is_equal) { result = 64; }
    if (((uint32_t)(result)) >= ((uint32_t)(Arg1))) goto loc_003E123E;
loc_003E152D:
    goto loc_003E1440;
loc_003E1535:
    a4 = (uint32_t)((*(uint64_t *)(a3)) & (63));
    if (condition_is_equal) goto loc_003E123E;
    Arg1 = 64;
    if (condition_is_equal) { Arg1 = 64; }
    if (((uint32_t)(Arg1)) >= ((uint32_t)(a4))) goto loc_003E123E;
loc_003E1557:
    if (a3 > 64) goto loc_003E1326;
    a3 = (a3) + (8);
    if ((*(uint64_t *)(a3)) != local_rbx) goto loc_003E1557;
    if ((*(uint64_t *)(a3)) == local_rbx) goto loc_003E1590;
    Arg1 = (uint32_t)((63) - ((uint32_t)(Arg2)));
    goto loc_003E14AF;
loc_003E1581:
    Arg2 = (uint32_t)((Arg2) & (0xFFFFFFF8ULL));
    goto loc_003E1250;
loc_003E1589:
    goto loc_003E14AF;
loc_003E1590:
    goto loc_003E14AF;
loc_003E159A:
    goto loc_003E1309;
loc_003E15A2:
    if (a3 == ((uint32_t)(v_stack_p30))) goto loc_003E1326;
    if (a3 == ((uint32_t)(v_stack_p30))) goto loc_003E15C7;
    Arg2 = (uint32_t)((64 - 1) - ((uint32_t)(*(uint64_t *)(a3))));
loc_003E15BB:
    a3 = (a3) + (8);
    goto loc_003E13E1;
loc_003E15C7:
    goto loc_003E15BB;
loc_003E15CB:
    v_stack_p20 = 0xBDCULL;
    Arg2 = 0;
    result = KeBugCheckEx(172, Arg2, (uint32_t)(0xA0A0ULL), v_rip - 3922290);
loc_003E15EE:
    goto loc_003E1343;
loc_003E15F6:
    *(uint64_t *)(local_rbx) = *(uint64_t *)(result);
    *(uint32_t *)(local_rbx + 0x8) = (uint32_t)(local_r14);
    local_rbx = (local_rbx) + (16);
    goto loc_003E13C1;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003E10B8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
