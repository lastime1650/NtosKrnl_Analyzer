# MiWalkEntireImage

- RVA: `0x00365D70`–`0x00367058` (길이 `4,840` bytes)
- VA: `0x0000000140365D70`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00079F88`
- 디코드: `1,164`개 명령, `4,840/4,840` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **89**; 고유 호출 대상: **67**
- 직접 호출자로 확인된 함수: **7**
- RIP 상대 이미지 참조: **10**

### Outgoing calls
- `0x00365DCD` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00365EE8` → [MiGetSectionStrongImageReference](../../page/93/MiGetSectionStrongImageReference_function_0093E9C0.md) (function, `0x0093E9C0`)
- `0x00365F0A` → [MiGetNextDirectFixupProto](../../page/70/MiGetNextDirectFixupProto_function_007049F0.md) (function, `0x007049F0`)
- `0x00365F54` → [MiAllocatePool](../35/MiAllocatePool_function_0035B540.md) (function, `0x0035B540`)
- `0x00365F86` → [MiUnlockProtoPoolPage](../24/MiUnlockProtoPoolPage_function_00246090.md) (function, `0x00246090`)
- `0x00366011` → [MiStartingOffset](../34/MiStartingOffset_function_003482E0.md) (function, `0x003482E0`)
- `0x00366065` → [MiLockLeafPage](MiLockLeafPage_function_003658C0.md) (function, `0x003658C0`)
- `0x0036617D` → [MiAddLockedPageCharge](../28/MiAddLockedPageCharge_function_0028B550.md) (function, `0x0028B550`)
- `0x003661C0` → [MiUnlockProtoPoolPage](../24/MiUnlockProtoPoolPage_function_00246090.md) (function, `0x00246090`)
- `0x0036623D` → [MiRelocateImagePfn](../../page/93/MiRelocateImagePfn_function_0093F2A8.md) (function, `0x0093F2A8`)
- `0x00366271` → [MiLockPageInline](../31/MiLockPageInline_function_0031A340.md) (function, `0x0031A340`)
- `0x003662D5` → [MiRemoveLockedPageCharge](../24/MiRemoveLockedPageCharge_function_00246950.md) (function, `0x00246950`)
- `0x003662F3` → [MiPfnReferenceCountIsZero](../2B/MiPfnReferenceCountIsZero_function_002B9E40.md) (function, `0x002B9E40`)
- `0x00366345` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x003663A6` → [MiCheckProtoPtePageState](../31/MiCheckProtoPtePageState_function_003183E0.md) (function, `0x003183E0`)
- `0x003663CB` → [MiGetPfnSlabType](../28/MiGetPfnSlabType_function_0028E2D0.md) (function, `0x0028E2D0`)
- `0x003663F0` → [MiUnlinkPageFromListEx](../28/MiUnlinkPageFromListEx_function_00287590.md) (function, `0x00287590`)
- `0x00366402` → [MiDiscardTransitionPteEx](../37/MiDiscardTransitionPteEx_function_00375954.md) (function, `0x00375954`)
- `0x0036647B` → [MiInsertProtectedStandbyPage](../45/MiInsertProtectedStandbyPage_function_004527D8.md) (function, `0x004527D8`)
- `0x00366487` → [MiUnlockPage](../31/MiUnlockPage_function_0031A3E0.md) (function, `0x0031A3E0`)
- `0x003664D5` → [VslApplySecureImageFixups](../48/VslApplySecureImageFixups_function_00489500.md) (function, `0x00489500`)
- `0x003664FC` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0036651B` → [MiUnlockProtoPoolPage](../24/MiUnlockProtoPoolPage_function_00246090.md) (function, `0x00246090`)
- `0x0036653C` → [MiReleasePageFileInfo](../28/MiReleasePageFileInfo_function_00283FD0.md) (function, `0x00283FD0`)
- `0x00366573` → [MiUnlockProtoPoolPage](../24/MiUnlockProtoPoolPage_function_00246090.md) (function, `0x00246090`)
- `0x00366595` → [MiDecayPfnFullyInitialized](../44/MiDecayPfnFullyInitialized_function_00447748.md) (function, `0x00447748`)
- `0x003665B5` → [MiFlushFileOnlyDeleteChain](../4F/MiFlushFileOnlyDeleteChain_function_004F5534.md) (function, `0x004F5534`)
- `0x003665C8` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x003665EB` → [MiReleaseFreshPage](../33/MiReleaseFreshPage_function_00334AE0.md) (function, `0x00334AE0`)
- `0x003665FD` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x0036661C` → [MiSetActivePfnHeat](../40/MiSetActivePfnHeat_function_00409E00.md) (function, `0x00409E00`)
- `0x00366629` → [MiCaptureDirtyBitToPfn](../37/MiCaptureDirtyBitToPfn_function_00370DD0.md) (function, `0x00370DD0`)
- `0x00366667` → [MiReleaseFreshPage](../33/MiReleaseFreshPage_function_00334AE0.md) (function, `0x00334AE0`)
- `0x003666B0` → [MiInitializePageColorBase](../32/MiInitializePageColorBase_function_00320410.md) (function, `0x00320410`)
- `0x003666FD` → [MiCreateDecayPfn](../2B/MiCreateDecayPfn_function_002B8764.md) (function, `0x002B8764`)
- `0x00366718` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x0036677E` → [MiPageHasRelocations](../../page/93/MiPageHasRelocations_function_0093EEC0.md) (function, `0x0093EEC0`)
- `0x003667A8` → [MiSplitDirectMapPage](../4D/MiSplitDirectMapPage_function_004DAAA0.md) (function, `0x004DAAA0`)
- `0x003667C4` → [MiLockPageInline](../31/MiLockPageInline_function_0031A340.md) (function, `0x0031A340`)
- `0x003667CE` → [MiRemoveLockedPageCharge](../24/MiRemoveLockedPageCharge_function_00246950.md) (function, `0x00246950`)
- `0x003667DD` → [MiPfnReferenceCountIsZero](../2B/MiPfnReferenceCountIsZero_function_002B9E40.md) (function, `0x002B9E40`)
- `0x003667E7` → [MiUnlockPage](../31/MiUnlockPage_function_0031A3E0.md) (function, `0x0031A3E0`)
- `0x003668B8` → [MiValidateImagePfn](../../page/93/MiValidateImagePfn_function_0093EA08.md) (function, `0x0093EA08`)
- `0x003668D6` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00366905` → [MiLockProtoPoolPage](../2B/MiLockProtoPoolPage_function_002B8B80.md) (function, `0x002B8B80`)
- `0x00366919` → [MmAccessFault](../27/MmAccessFault_function_0027EE80.md) (function, `0x0027EE80`)
- `0x00366969` → [KeAbPreAcquire](../21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00366988` → [ExfAcquirePushLockSharedEx](../21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)
- `0x003669B5` → [MiGetSharedProtos](../34/MiGetSharedProtos_function_00348D58.md) (function, `0x00348D58`)
- `0x00366A41` → [MI_NODE_FROM_PFN](../2B/MI_NODE_FROM_PFN_function_002B0F30.md) (function, `0x002B0F30`)
- `0x00366A5E` → [MiUseSlabAllocator](MiUseSlabAllocator_function_00365C68.md) (function, `0x00365C68`)
- `0x00366A78` → [MiGetPfnSlabType](../28/MiGetPfnSlabType_function_0028E2D0.md) (function, `0x0028E2D0`)
- `0x00366A8E` → [MiCheckSlabPage](../34/MiCheckSlabPage_function_00348AC8.md) (function, `0x00348AC8`)
- `0x00366AB2` → [MiWalkEntireImagePageNeedsProcessing](../4D/MiWalkEntireImagePageNeedsProcessing_function_004DC2BC.md) (function, `0x004DC2BC`)
- `0x00366AD6` → [MiAddPageToHeatList](../44/MiAddPageToHeatList_function_0044603C.md) (function, `0x0044603C`)
- `0x00366B70` → [MiUpdateImagePfnImportRelocations](../44/MiUpdateImagePfnImportRelocations_function_00449E84.md) (function, `0x00449E84`)
- `0x00366B88` → [MiGetPagingFileOffset](MiGetPagingFileOffset_function_0036F530.md) (function, `0x0036F530`)
- `0x00366B9E` → [MiUnlockProtoPoolPage](../24/MiUnlockProtoPoolPage_function_00246090.md) (function, `0x00246090`)
- `0x00366BC6` → [MiPageHasRelocations](../../page/93/MiPageHasRelocations_function_0093EEC0.md) (function, `0x0093EEC0`)
- `0x00366BE4` → [MiGetEffectivePagePriorityThread](MiGetEffectivePagePriorityThread_function_003626E0.md) (function, `0x003626E0`)
- `0x00366C16` → [MiPrefetchControlArea](../../page/93/MiPrefetchControlArea_function_0093E830.md) (function, `0x0093E830`)
- `0x00366C2D` → [KeDelayExecutionThread](../20/KeDelayExecutionThread_function_00209550.md) (function, `0x00209550`)
- `0x00366C62` → [MiInitializePageFaultPacket](../22/MiInitializePageFaultPacket_function_00228EB0.md) (function, `0x00228EB0`)
- `0x00366C75` → [MiObtainProtoReference](../31/MiObtainProtoReference_function_00318178.md) (function, `0x00318178`)
- `0x00366C97` → [MiWaitForCollidedFaultComplete](MiWaitForCollidedFaultComplete_function_00369EDC.md) (function, `0x00369EDC`)
- `0x00366CC3` → [MI_PAGE_TO_FULL_COLOR](../33/MI_PAGE_TO_FULL_COLOR_function_00337820.md) (function, `0x00337820`)
- `0x00366CE0` → [MiGetSlabPage](../37/MiGetSlabPage_function_00376FBC.md) (function, `0x00376FBC`)
- `0x00366D02` → [MiPfnReferenceCountIsZero](../2B/MiPfnReferenceCountIsZero_function_002B9E40.md) (function, `0x002B9E40`)
- `0x00366D42` → [VslApplySecureImageFixups](../48/VslApplySecureImageFixups_function_00489500.md) (function, `0x00489500`)
- `0x00366D69` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00366D86` → [MiTrimSharedPage](../29/MiTrimSharedPage_function_00297D14.md) (function, `0x00297D14`)
- `0x00366D8E` → [MiLockPageInline](../31/MiLockPageInline_function_0031A340.md) (function, `0x0031A340`)
- `0x00366DBB` → [KeAbPostRelease](../2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00366DDE` → [KiCheckForKernelApcDelivery](../2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (function, `0x002E2C80`)
- `0x00366E0F` → [MiApplyDebuggerPatches](../4F/MiApplyDebuggerPatches_function_004F7BE4.md) (function, `0x004F7BE4`)
- `0x00366E2F` → [MiInitializePageHeatList](../44/MiInitializePageHeatList_function_00446000.md) (function, `0x00446000`)
- `0x00366E6F` → [MiDeleteTransitionPte](../37/MiDeleteTransitionPte_function_00371B70.md) (function, `0x00371B70`)
- `0x00366E89` → [MiIssuePageHeatList](../44/MiIssuePageHeatList_function_0044615C.md) (function, `0x0044615C`)
- `0x00366EAE` → [KeAbPostRelease](../2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00366ED1` → [KiCheckForKernelApcDelivery](../2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (function, `0x002E2C80`)
- `0x00366F04` → [MiWalkEntireImage](MiWalkEntireImage_function_00365D70.md) (function, `0x00365D70`)
- `0x00366F27` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x00366F76` → [MiGetPfnSlabType](../28/MiGetPfnSlabType_function_0028E2D0.md) (function, `0x0028E2D0`)
- `0x00366F87` → [MiGetPfnSlabType](../28/MiGetPfnSlabType_function_0028E2D0.md) (function, `0x0028E2D0`)
- `0x00366F98` → [MiReplaceTransitionPage](../2B/MiReplaceTransitionPage_function_002B1120.md) (function, `0x002B1120`)
- `0x00366FC9` → [MiSetOriginalPtePfnFromFreeList](../28/MiSetOriginalPtePfnFromFreeList_function_0028A99C.md) (function, `0x0028A99C`)
- `0x00366FD1` → [MiReleaseFreshPageLocked](../44/MiReleaseFreshPageLocked_function_0044CDD8.md) (function, `0x0044CDD8`)
- `0x00366FDE` → [ExfReleasePushLockShared](../26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x00366FEB` → [ExfReleasePushLockShared](../26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)

### Direct callers
- [MiCheckControlArea](../28/MiCheckControlArea_function_002861B0.md) at `0x002862E4`
- [MiWalkEntireImage](MiWalkEntireImage_function_00365D70.md) at `0x00366F04`
- [MiValidateSectionCreate](../../page/94/MiValidateSectionCreate_function_00940190.md) at `0x00940A80`
- [MiSwitchBaseAddress](../../page/98/MiSwitchBaseAddress_function_00988CDC.md) at `0x00988D76`
- [MiApplyImportOptimizationToRuntimeDriver](../../page/A9/MiApplyImportOptimizationToRuntimeDriver_function_00A9F93C.md) at `0x00A9F9F3`
- [MiFreeRetpolineImportInfo](../../page/AA/MiFreeRetpolineImportInfo_function_00AAFF1C.md) at `0x00AAFFA8`
- [sub_00B2B6D0](../../page/B2/Unknown_function_00B2B6D0.md) at `0x00B2B7D6`
- [sub_00B2B6D0](../../page/B2/Unknown_function_00B2B6D0.md) at `0x00B2B7ED`

### Static image references
- `0x00365D8C` → RVA `0x00E0A740` (`.data`; read)
- `0x00365DF3` → RVA `0x00E30088` (`.data`; read)
- `0x00365E94` → RVA `0x00FC6A88` (`ALMOSTRO`; read)
- `0x003660CF` → RVA `0x00E2DC80` (`.data`; read)
- `0x00366195` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)
- `0x00366338` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x0036655B` → RVA `0x00E2D7F8` (`.data`; write)
- `0x003667FC` → RVA `0x00E2ECF8` (`.data`; read)
- `0x00366C22` → RVA `0x00010780` (`.rdata`; read)
- `0x00366FB2` → RVA `0x00010880` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **8**
  - `0x00365EE8` → [MiGetSectionStrongImageReference](../../page/93/MiGetSectionStrongImageReference_function_0093E9C0.md) (`.text` → `PAGE`)
  - `0x00365F0A` → [MiGetNextDirectFixupProto](../../page/70/MiGetNextDirectFixupProto_function_007049F0.md) (`.text` → `PAGE`)
  - `0x0036623D` → [MiRelocateImagePfn](../../page/93/MiRelocateImagePfn_function_0093F2A8.md) (`.text` → `PAGE`)
  - `0x003665C8` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x0036677E` → [MiPageHasRelocations](../../page/93/MiPageHasRelocations_function_0093EEC0.md) (`.text` → `PAGE`)
  - `0x003668B8` → [MiValidateImagePfn](../../page/93/MiValidateImagePfn_function_0093EA08.md) (`.text` → `PAGE`)
  - `0x00366BC6` → [MiPageHasRelocations](../../page/93/MiPageHasRelocations_function_0093EEC0.md) (`.text` → `PAGE`)
  - `0x00366C16` → [MiPrefetchControlArea](../../page/93/MiPrefetchControlArea_function_0093E830.md) (`.text` → `PAGE`)
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x00365FB0` → [sub_006E3418 + 0x80](../6E/Unknown_function_006E3418.md) (`tail-transfer`)
  - `0x0036609A` → [sub_006E3418](../6E/Unknown_function_006E3418.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00365D70  40 55                           push rbp
00365D72  53                              push rbx
00365D73  56                              push rsi
00365D74  57                              push rdi
00365D75  41 54                           push r12
00365D77  41 55                           push r13
00365D79  41 56                           push r14
00365D7B  41 57                           push r15
00365D7D  48 8D AC 24 58 FE FF FF         lea rbp, [rsp - 0x1a8]
00365D85  48 81 EC A8 02 00 00            sub rsp, 0x2a8
00365D8C  48 8B 05 AD 49 AA 00            mov rax, qword ptr [rip + 0xaa49ad]
00365D93  48 33 C4                        xor rax, rsp
00365D96  48 89 85 90 01 00 00            mov qword ptr [rbp + 0x190], rax
00365D9D  41 8B F0                        mov esi, r8d
00365DA0  44 89 44 24 70                  mov dword ptr [rsp + 0x70], r8d
00365DA5  48 89 55 D8                     mov qword ptr [rbp - 0x28], rdx
00365DA9  4C 8B E9                        mov r13, rcx
00365DAC  48 89 4D 20                     mov qword ptr [rbp + 0x20], rcx
00365DB0  33 C0                           xor eax, eax
00365DB2  0F 57 C0                        xorps xmm0, xmm0
00365DB5  89 45 D0                        mov dword ptr [rbp - 0x30], eax
00365DB8  33 D2                           xor edx, edx
00365DBA  44 89 4C 24 78                  mov dword ptr [rsp + 0x78], r9d
00365DBF  41 B8 90 00 00 00               mov r8d, 0x90
00365DC5  48 8D 4D 60                     lea rcx, [rbp + 0x60]
00365DC9  0F 11 45 48                     movups xmmword ptr [rbp + 0x48], xmm0
00365DCD  E8 6E 0E 36 00                  call 0x1406c6c40
00365DD2  49 8B 45 00                     mov rax, qword ptr [r13]
00365DD6  45 33 C9                        xor r9d, r9d
00365DD9  41 0F B7 4D 3C                  movzx ecx, word ptr [r13 + 0x3c]
00365DDE  44 8B F6                        mov r14d, esi
00365DE1  49 8B 55 60                     mov rdx, qword ptr [r13 + 0x60]
00365DE5  81 E1 FF 03 00 00               and ecx, 0x3ff
00365DEB  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
00365DEF  48 83 E2 F8                     and rdx, 0xfffffffffffffff8
00365DF3  48 8B 05 8E A2 AC 00            mov rax, qword ptr [rip + 0xaca28e]
00365DFA  45 8D 41 02                     lea r8d, [r9 + 2]
00365DFE  41 83 E6 04                     and r14d, 4
00365E02  48 89 55 C8                     mov qword ptr [rbp - 0x38], rdx
00365E06  41 8B F9                        mov edi, r9d
00365E09  44 89 75 88                     mov dword ptr [rbp - 0x78], r14d
00365E0D  48 8B 04 C8                     mov rax, qword ptr [rax + rcx*8]
00365E11  48 89 45 00                     mov qword ptr [rbp], rax
00365E15  41 8A 45 3E                     mov al, byte ptr [r13 + 0x3e]
00365E19  24 0C                           and al, 0xc
00365E1B  3C 04                           cmp al, 4
00365E1D  0F 84 AD 0B 00 00               je 0x1403669d0
00365E23  49 8D 4D 38                     lea rcx, [r13 + 0x38]
00365E27  F7 01 00 08 00 00               test dword ptr [rcx], 0x800
00365E2D  48 89 4D F8                     mov qword ptr [rbp - 8], rcx
00365E31  74 07                           je 0x140365e3a
00365E33  48 89 4D F8                     mov qword ptr [rbp - 8], rcx
00365E37  41 8B F8                        mov edi, r8d
00365E3A  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00365E43  48 8D 5D 60                     lea rbx, [rbp + 0x60]
00365E47  83 4D 64 FF                     or dword ptr [rbp + 0x64], 0xffffffff
00365E4B  0F 57 C0                        xorps xmm0, xmm0
00365E4E  48 89 45 A0                     mov qword ptr [rbp - 0x60], rax
00365E52  33 C0                           xor eax, eax
00365E54  48 89 45 40                     mov qword ptr [rbp + 0x40], rax
00365E58  8B C6                           mov eax, esi
00365E5A  83 E0 10                        and eax, 0x10
00365E5D  4C 89 4D E0                     mov qword ptr [rbp - 0x20], r9
00365E61  89 44 24 74                     mov dword ptr [rsp + 0x74], eax
00365E65  0F 11 45 30                     movups xmmword ptr [rbp + 0x30], xmm0
00365E69  48 89 5D 80                     mov qword ptr [rbp - 0x80], rbx
00365E6D  0F 85 89 09 00 00               jne 0x1403667fc
00365E73  45 85 F6                        test r14d, r14d
00365E76  0F 85 09 08 00 00               jne 0x140366685
00365E7C  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00365E85  49 8D 9D 80 00 00 00            lea rbx, [r13 + 0x80]
00365E8C  49 83 CF FF                     or r15, 0xffffffffffffffff
00365E90  48 89 5D A8                     mov qword ptr [rbp - 0x58], rbx
00365E94  48 F7 05 E9 0B C6 00 00 20 00 00  test qword ptr [rip + 0xc60be9], 0x2000
00365E9F  45 8B E1                        mov r12d, r9d
00365EA2  44 89 4D 8C                     mov dword ptr [rbp - 0x74], r9d
00365EA6  49 8B F1                        mov rsi, r9
00365EA9  48 8B 80 B8 00 00 00            mov rax, qword ptr [rax + 0xb8]
00365EB0  48 89 45 18                     mov qword ptr [rbp + 0x18], rax
00365EB4  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
00365EB8  48 89 45 10                     mov qword ptr [rbp + 0x10], rax
00365EBC  B8 11 00 00 00                  mov eax, 0x11
00365EC1  88 44 24 50                     mov byte ptr [rsp + 0x50], al
00365EC5  4C 89 4C 24 58                  mov qword ptr [rsp + 0x58], r9
00365ECA  4C 89 4D F0                     mov qword ptr [rbp - 0x10], r9
00365ECE  4C 89 7C 24 60                  mov qword ptr [rsp + 0x60], r15
00365ED3  74 26                           je 0x140365efb
00365ED5  41 F7 45 5C 00 00 0C 00         test dword ptr [r13 + 0x5c], 0xc0000
00365EDD  74 1C                           je 0x140365efb
00365EDF  4C 39 4A 40                     cmp qword ptr [rdx + 0x40], r9
00365EE3  75 16                           jne 0x140365efb
00365EE5  48 8B CA                        mov rcx, rdx
00365EE8  E8 D3 8A 5D 00                  call 0x14093e9c0
00365EED  45 33 C9                        xor r9d, r9d
00365EF0  44 8B E0                        mov r12d, eax
00365EF3  85 C0                           test eax, eax
00365EF5  0F 88 F8 06 00 00               js 0x1403665f3
00365EFB  44 89 4D E8                     mov dword ptr [rbp - 0x18], r9d
00365EFF  45 85 F6                        test r14d, r14d
00365F02  74 0F                           je 0x140365f13
00365F04  48 8B 4D D8                     mov rcx, qword ptr [rbp - 0x28]
00365F08  33 D2                           xor edx, edx
00365F0A  E8 E1 EA 39 00                  call 0x1407049f0
00365F0F  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
00365F13  83 7D 64 FF                     cmp dword ptr [rbp + 0x64], -1
00365F17  41 B8 01 00 00 00               mov r8d, 1
00365F1D  48 8B 55 C0                     mov rdx, qword ptr [rbp - 0x40]
00365F21  0F 84 A9 00 00 00               je 0x140365fd0
00365F27  8B 4A 08                        mov ecx, dword ptr [rdx + 8]
00365F2A  BB FF 01 00 00                  mov ebx, 0x1ff
00365F2F  3B CB                           cmp ecx, ebx
00365F31  0F 42 D9                        cmovb ebx, ecx
00365F34  8B 4D 60                        mov ecx, dword ptr [rbp + 0x60]
00365F37  C1 E9 03                        shr ecx, 3
00365F3A  3B D9                           cmp ebx, ecx
00365F3C  0F 86 B3 10 00 00               jbe 0x140366ff5
00365F42  41 8D 48 41                     lea ecx, [r8 + 0x41]
00365F46  41 B8 4D 69 68 6C               mov r8d, 0x6c68694d
00365F4C  48 8D 14 DD 10 00 00 00         lea rdx, [rbx*8 + 0x10]
00365F54  E8 E7 55 FF FF                  call 0x14035b540
00365F59  45 33 C9                        xor r9d, r9d
00365F5C  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
00365F60  48 85 C0                        test rax, rax
00365F63  0F 85 B0 0E 00 00               jne 0x140366e19
00365F69  48 8D 45 60                     lea rax, [rbp + 0x60]
00365F6D  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
00365F71  49 8D 9D 80 00 00 00            lea rbx, [r13 + 0x80]
00365F78  EB 4C                           jmp 0x140365fc6
00365F7A  48 85 F6                        test rsi, rsi
00365F7D  74 14                           je 0x140365f93
00365F7F  8A 54 24 50                     mov dl, byte ptr [rsp + 0x50]
00365F83  48 8B CE                        mov rcx, rsi
00365F86  E8 05 01 EE FF                  call 0x140246090
00365F8B  45 33 C9                        xor r9d, r9d
00365F8E  4C 89 4C 24 58                  mov qword ptr [rsp + 0x58], r9
00365F93  4C 8B 7C 24 60                  mov r15, qword ptr [rsp + 0x60]
00365F98  49 83 FF FF                     cmp r15, -1
00365F9C  0F 85 AD 06 00 00               jne 0x14036664f
00365FA2  4C 8B 75 A0                     mov r14, qword ptr [rbp - 0x60]
00365FA6  41 B8 01 00 00 00               mov r8d, 1
00365FAC  40 F6 C7 08                     test dil, 8
00365FB0  0F 85 E2 D4 37 00               jne 0x1406e3498
00365FB6  48 8B 5D 28                     mov rbx, qword ptr [rbp + 0x28]
00365FBA  48 8B 74 24 58                  mov rsi, qword ptr [rsp + 0x58]
00365FBF  48 89 5D A8                     mov qword ptr [rbp - 0x58], rbx
00365FC3  45 33 C9                        xor r9d, r9d
00365FC6  48 8B 55 C0                     mov rdx, qword ptr [rbp - 0x40]
00365FCA  41 B8 01 00 00 00               mov r8d, 1
00365FD0  48 85 DB                        test rbx, rbx
00365FD3  0F 84 AA 05 00 00               je 0x140366583
00365FD9  4C 8B 73 08                     mov r14, qword ptr [rbx + 8]
00365FDD  48 8B 43 10                     mov rax, qword ptr [rbx + 0x10]
00365FE1  4D 8B FE                        mov r15, r14
00365FE4  4C 2B 7D 10                     sub r15, qword ptr [rbp + 0x10]
00365FE8  49 C1 FF 03                     sar r15, 3
00365FEC  48 89 45 28                     mov qword ptr [rbp + 0x28], rax
00365FF0  8B 43 20                        mov eax, dword ptr [rbx + 0x20]
00365FF3  4C 89 75 B8                     mov qword ptr [rbp - 0x48], r14
00365FF7  4C 89 7C 24 68                  mov qword ptr [rsp + 0x68], r15
00365FFC  0F BA E0 11                     bt eax, 0x11
00366000  0F 82 24 09 00 00               jb 0x14036692a
00366006  44 8B 44 24 78                  mov r8d, dword ptr [rsp + 0x78]
0036600B  49 8B D6                        mov rdx, r14
0036600E  48 8B CB                        mov rcx, rbx
00366011  E8 CA 22 FE FF                  call 0x1403482e0
00366016  8B 4B 2C                        mov ecx, dword ptr [rbx + 0x2c]
00366019  45 33 C9                        xor r9d, r9d
0036601C  4C 8B 45 E0                     mov r8, qword ptr [rbp - 0x20]
00366020  48 8B D0                        mov rdx, rax
00366023  48 89 45 98                     mov qword ptr [rbp - 0x68], rax
00366027  49 8D 1C CE                     lea rbx, [r14 + rcx*8]
0036602B  48 89 5D B0                     mov qword ptr [rbp - 0x50], rbx
0036602F  4D 85 C0                        test r8, r8
00366032  0F 85 DF 07 00 00               jne 0x140366817
00366038  4C 89 4D 90                     mov qword ptr [rbp - 0x70], r9
0036603C  B8 02 00 00 00                  mov eax, 2
00366041  4C 3B F3                        cmp r14, rbx
00366044  0F 83 30 FF FF FF               jae 0x140365f7a
0036604A  49 F7 C6 FF 0F 00 00            test r14, 0xfff
00366051  0F 84 2E 03 00 00               je 0x140366385
00366057  48 85 F6                        test rsi, rsi
0036605A  0F 84 25 03 00 00               je 0x140366385
00366060  33 D2                           xor edx, edx
00366062  49 8B CE                        mov rcx, r14
00366065  E8 56 F8 FF FF                  call 0x1403658c0
0036606A  45 33 C9                        xor r9d, r9d
0036606D  48 8B F0                        mov rsi, rax
00366070  48 85 C0                        test rax, rax
00366073  75 49                           jne 0x1403660be
00366075  44 39 4D 88                     cmp dword ptr [rbp - 0x78], r9d
00366079  0F 85 74 0D 00 00               jne 0x140366df3
0036607F  8D 46 02                        lea eax, [rsi + 2]
00366082  40 84 F8                        test al, dil
00366085  0F 85 EF 0A 00 00               jne 0x140366b7a
0036608B  48 8B 74 24 58                  mov rsi, qword ptr [rsp + 0x58]
00366090  41 BA 01 00 00 00               mov r10d, 1
00366096  4C 39 4D E0                     cmp qword ptr [rbp - 0x20], r9
0036609A  0F 85 78 D3 37 00               jne 0x1406e3418
003660A0  48 8B 5D B0                     mov rbx, qword ptr [rbp - 0x50]
003660A4  49 83 C6 08                     add r14, 8
003660A8  45 03 FA                        add r15d, r10d
003660AB  4C 89 75 B8                     mov qword ptr [rbp - 0x48], r14
003660AF  48 81 45 98 00 10 00 00         add qword ptr [rbp - 0x68], 0x1000
003660B7  4C 89 7C 24 68                  mov qword ptr [rsp + 0x68], r15
003660BC  EB 83                           jmp 0x140366041
003660BE  49 8B 0E                        mov rcx, qword ptr [r14]
003660C1  41 BA 01 00 00 00               mov r10d, 1
003660C7  4C 8B F9                        mov r15, rcx
003660CA  41 84 CA                        test r10b, cl
003660CD  75 1E                           jne 0x1403660ed
003660CF  48 8B 05 AA 7B AC 00            mov rax, qword ptr [rip + 0xac7baa]
003660D6  48 85 C0                        test rax, rax
003660D9  74 12                           je 0x1403660ed
003660DB  F6 C1 10                        test cl, 0x10
003660DE  0F 85 46 04 00 00               jne 0x14036652a
003660E4  4C 8B F8                        mov r15, rax
003660E7  49 F7 D7                        not r15
003660EA  4C 23 F9                        and r15, rcx
003660ED  8B 5C 24 70                     mov ebx, dword ptr [rsp + 0x70]
003660F1  48 B8 FF FF FF FF FF 00 00 00   movabs rax, 0xffffffffff
003660FB  49 C1 EF 0C                     shr r15, 0xc
003660FF  4C 23 F8                        and r15, rax
00366102  41 84 DA                        test r10b, bl
00366105  0F 85 3E 07 00 00               jne 0x140366849
0036610B  8B 46 10                        mov eax, dword ptr [rsi + 0x10]
0036610E  48 0F BA E0 0A                  bt rax, 0xa
00366113  0F 83 F2 0E 00 00               jae 0x14036700b
00366119  8B 46 20                        mov eax, dword ptr [rsi + 0x20]
0036611C  8B 55 88                        mov edx, dword ptr [rbp - 0x78]
0036611F  C1 E8 18                        shr eax, 0x18
00366122  A8 40                           test al, 0x40
00366124  0F 85 B8 08 00 00               jne 0x1403669e2
0036612A  F6 46 23 10                     test byte ptr [rsi + 0x23], 0x10
0036612E  0F 85 15 04 00 00               jne 0x140366549
00366134  41 84 CA                        test r10b, cl
00366137  75 0A                           jne 0x140366143
00366139  F6 46 22 20                     test byte ptr [rsi + 0x22], 0x20
0036613D  0F 85 84 07 00 00               jne 0x1403668c7
00366143  44 39 4C 24 74                  cmp dword ptr [rsp + 0x74], r9d
00366148  0F 85 B5 08 00 00               jne 0x140366a03
0036614E  BB 08 00 00 00                  mov ebx, 8
00366153  89 5D D4                        mov dword ptr [rbp - 0x2c], ebx
00366156  41 84 CA                        test r10b, cl
00366159  0F 84 69 02 00 00               je 0x1403663c8
0036615F  44 8B 74 24 70                  mov r14d, dword ptr [rsp + 0x70]
00366164  41 8B C6                        mov eax, r14d
00366167  24 11                           and al, 0x11
00366169  41 3A C2                        cmp al, r10b
0036616C  0F 84 C2 08 00 00               je 0x140366a34
00366172  83 E7 EF                        and edi, 0xffffffef
00366175  BA 01 00 00 00                  mov edx, 1
0036617A  48 8B CE                        mov rcx, rsi
0036617D  E8 CE 53 F2 FF                  call 0x14028b550
00366182  45 33 C0                        xor r8d, r8d
00366185  44 39 44 24 74                  cmp dword ptr [rsp + 0x74], r8d
0036618A  0F 85 0E 03 00 00               jne 0x14036649e
00366190  40 84 FF                        test dil, dil
00366193  78 10                           js 0x1403661a5
00366195  F7 05 19 09 C6 00 00 00 20 00   test dword ptr [rip + 0xc60919], 0x200000
0036619F  0F 85 5B 09 00 00               jne 0x140366b00
003661A5  83 E7 DF                        and edi, 0xffffffdf
003661A8  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
003661B2  F0 48 21 46 18                  lock and qword ptr [rsi + 0x18], rax
003661B7  8A 54 24 50                     mov dl, byte ptr [rsp + 0x50]
003661BB  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
003661C0  E8 CB FE ED FF                  call 0x140246090
003661C5  33 D2                           xor edx, edx
003661C7  48 89 54 24 58                  mov qword ptr [rsp + 0x58], rdx
003661CC  40 F6 C7 20                     test dil, 0x20
003661D0  0F 85 CD 08 00 00               jne 0x140366aa3
003661D6  4C 8B 74 24 68                  mov r14, qword ptr [rsp + 0x68]
003661DB  48 8B 4E 28                     mov rcx, qword ptr [rsi + 0x28]
003661DF  41 B8 01 00 00 00               mov r8d, 1
003661E5  48 0F BA E1 35                  bt rcx, 0x35
003661EA  0F 82 7B 05 00 00               jb 0x14036676b
003661F0  83 E7 FE                        and edi, 0xfffffffe
003661F3  39 54 24 74                     cmp dword ptr [rsp + 0x74], edx
003661F7  0F 85 99 02 00 00               jne 0x140366496
003661FD  39 55 88                        cmp dword ptr [rbp - 0x78], edx
00366200  0F 85 6D 05 00 00               jne 0x140366773
00366206  8B 44 24 70                     mov eax, dword ptr [rsp + 0x70]
0036620A  A8 02                           test al, 2
0036620C  0F 84 67 06 00 00               je 0x140366879
00366212  48 F7 05 6B 08 C6 00 00 20 00 00  test qword ptr [rip + 0xc6086b], 0x2000
0036621D  0F 85 86 02 00 00               jne 0x1403664a9
00366223  C7 44 24 30 41 00 00 00         mov dword ptr [rsp + 0x30], 0x41
0036622B  4D 8B CF                        mov r9, r15
0036622E  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
00366233  45 8B C6                        mov r8d, r14d
00366236  48 8B 55 D8                     mov rdx, qword ptr [rbp - 0x28]
0036623A  49 8B CD                        mov rcx, r13
0036623D  E8 66 90 5D 00                  call 0x14093f2a8
00366242  33 D2                           xor edx, edx
00366244  44 8B E0                        mov r12d, eax
00366247  85 C0                           test eax, eax
00366249  0F 85 C3 0C 00 00               jne 0x140366f12
0036624F  83 CF 04                        or edi, 4
00366252  83 FB 08                        cmp ebx, 8
00366255  0F 85 71 04 00 00               jne 0x1403666cc
0036625B  45 33 F6                        xor r14d, r14d
0036625E  40 F6 C7 10                     test dil, 0x10
00366262  0F 85 4C 0A 00 00               jne 0x140366cb4
00366268  48 8B CE                        mov rcx, rsi
0036626B  4D 8B EE                        mov r13, r14
0036626E  49 8B DE                        mov rbx, r14
00366271  E8 CA 40 FB FF                  call 0x14031a340
00366276  48 8B 4E 18                     mov rcx, qword ptr [rsi + 0x18]
0036627A  48 0F BA E1 3E                  bt rcx, 0x3e
0036627F  88 44 24 50                     mov byte ptr [rsp + 0x50], al
00366283  0F 82 79 02 00 00               jb 0x140366502
00366289  40 F6 C7 40                     test dil, 0x40
0036628D  0F 85 84 03 00 00               jne 0x140366617
00366293  8A 46 23                        mov al, byte ptr [rsi + 0x23]
00366296  44 8B F7                        mov r14d, edi
00366299  41 83 E6 EF                     and r14d, 0xffffffef
0036629D  84 C0                           test al, al
0036629F  8B 44 24 70                     mov eax, dword ptr [rsp + 0x70]
003662A3  44 0F 49 F7                     cmovns r14d, edi
003662A7  A8 08                           test al, 8
003662A9  75 0B                           jne 0x1403662b6
003662AB  24 12                           and al, 0x12
003662AD  B9 02 00 00 00                  mov ecx, 2
003662B2  3A C1                           cmp al, cl
003662B4  75 0F                           jne 0x1403662c5
003662B6  48 8B 46 10                     mov rax, qword ptr [rsi + 0x10]
003662BA  48 0F BA E0 0A                  bt rax, 0xa
003662BF  0F 83 61 03 00 00               jae 0x140366626
003662C5  41 8B FE                        mov edi, r14d
003662C8  41 F6 C6 10                     test r14b, 0x10
003662CC  0F 85 9D 0A 00 00               jne 0x140366d6f
003662D2  48 8B CE                        mov rcx, rsi
003662D5  E8 76 06 EE FF                  call 0x140246950
003662DA  33 C9                           xor ecx, ecx
003662DC  44 8D 71 01                     lea r14d, [rcx + 1]
003662E0  85 C0                           test eax, eax
003662E2  74 16                           je 0x1403662fa
003662E4  41 84 FE                        test r14b, dil
003662E7  0F 84 4E 01 00 00               je 0x14036643b
003662ED  49 8B D7                        mov rdx, r15
003662F0  48 8B CE                        mov rcx, rsi
003662F3  E8 48 3B F5 FF                  call 0x1402b9e40
003662F8  33 C9                           xor ecx, ecx
003662FA  40 F6 C7 10                     test dil, 0x10
003662FE  0F 85 2D 0C 00 00               jne 0x140366f31
00366304  4C 8B 7C 24 60                  mov r15, qword ptr [rsp + 0x60]
00366309  80 7C 24 50 11                  cmp byte ptr [rsp + 0x50], 0x11
0036630E  74 0F                           je 0x14036631f
00366310  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
0036631A  F0 48 21 46 18                  lock and qword ptr [rsi + 0x18], rax
0036631F  45 33 C9                        xor r9d, r9d
00366322  48 85 DB                        test rbx, rbx
00366325  0F 85 08 02 00 00               jne 0x140366533
0036632B  8A 54 24 50                     mov dl, byte ptr [rsp + 0x50]
0036632F  BB 11 00 00 00                  mov ebx, 0x11
00366334  3A D3                           cmp dl, bl
00366336  74 22                           je 0x14036635a
00366338  44 39 0D E1 09 C6 00            cmp dword ptr [rip + 0xc609e1], r9d
0036633F  74 0C                           je 0x14036634d
00366341  44 0F 20 C1                     mov rcx, cr8
00366345  E8 4E F3 18 00                  call 0x1404f5698
0036634A  45 33 C9                        xor r9d, r9d
0036634D  0F B6 44 24 50                  movzx eax, byte ptr [rsp + 0x50]
00366352  44 0F 22 C0                     mov cr8, rax
00366356  88 5C 24 50                     mov byte ptr [rsp + 0x50], bl
0036635A  45 85 E4                        test r12d, r12d
0036635D  0F 88 82 07 00 00               js 0x140366ae5
00366363  4C 8B 75 B8                     mov r14, qword ptr [rbp - 0x48]
00366367  4C 8B 6D 20                     mov r13, qword ptr [rbp + 0x20]
0036636B  48 8B 74 24 58                  mov rsi, qword ptr [rsp + 0x58]
00366370  4C 8B 7C 24 68                  mov r15, qword ptr [rsp + 0x68]
00366375  41 BA 01 00 00 00               mov r10d, 1
0036637B  B8 02 00 00 00                  mov eax, 2
00366380  E9 11 FD FF FF                  jmp 0x140366096
00366385  48 85 F6                        test rsi, rsi
00366388  0F 85 86 01 00 00               jne 0x140366514
0036638E  8B DF                           mov ebx, edi
00366390  23 D8                           and ebx, eax
00366392  0F 85 65 05 00 00               jne 0x1403668fd
00366398  4C 8D 4C 24 50                  lea r9, [rsp + 0x50]
0036639D  45 33 C0                        xor r8d, r8d
003663A0  49 8B D6                        mov rdx, r14
003663A3  49 8B CD                        mov rcx, r13
003663A6  E8 35 20 FB FF                  call 0x1403183e0
003663AB  45 33 C9                        xor r9d, r9d
003663AE  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
003663B3  48 8B F0                        mov rsi, rax
003663B6  48 85 C0                        test rax, rax
003663B9  0F 84 6A 03 00 00               je 0x140366729
003663BF  48 8B 5D B0                     mov rbx, qword ptr [rbp - 0x50]
003663C3  E9 98 FC FF FF                  jmp 0x140366060
003663C8  48 8B CE                        mov rcx, rsi
003663CB  E8 00 7F F2 FF                  call 0x14028e2d0
003663D0  83 F8 09                        cmp eax, 9
003663D3  75 16                           jne 0x1403663eb
003663D5  8B 46 20                        mov eax, dword ptr [rsi + 0x20]
003663D8  C1 E8 18                        shr eax, 0x18
003663DB  84 C3                           test bl, al
003663DD  74 0C                           je 0x1403663eb
003663DF  8B 5E 20                        mov ebx, dword ptr [rsi + 0x20]
003663E2  C1 EB 18                        shr ebx, 0x18
003663E5  83 E3 07                        and ebx, 7
003663E8  89 5D D4                        mov dword ptr [rbp - 0x2c], ebx
003663EB  33 D2                           xor edx, edx
003663ED  48 8B CE                        mov rcx, rsi
003663F0  E8 9B 11 F2 FF                  call 0x140287590
003663F5  A8 03                           test al, 3
003663F7  0F 84 2C 0C 00 00               je 0x140367029
003663FD  33 D2                           xor edx, edx
003663FF  48 8B CE                        mov rcx, rsi
00366402  E8 4D F5 00 00                  call 0x140375954
00366407  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
00366411  F0 48 21 46 18                  lock and qword ptr [rsi + 0x18], rax
00366416  48 8B 74 24 58                  mov rsi, qword ptr [rsp + 0x58]
0036641B  B8 02 00 00 00                  mov eax, 2
00366420  4C 8B 7C 24 68                  mov r15, qword ptr [rsp + 0x68]
00366425  48 8B 5D B0                     mov rbx, qword ptr [rbp - 0x50]
00366429  44 8D 48 FE                     lea r9d, [rax - 2]
0036642D  40 84 F8                        test al, dil
00366430  0F 85 0B FC FF FF               jne 0x140366041
00366436  E9 55 FC FF FF                  jmp 0x140366090
0036643B  83 7D D4 08                     cmp dword ptr [rbp - 0x2c], 8
0036643F  0F 84 A8 FE FF FF               je 0x1403662ed
00366445  F6 46 22 10                     test byte ptr [rsi + 0x22], 0x10
00366449  0F 85 9E FE FF FF               jne 0x1403662ed
0036644F  48 8B 46 18                     mov rax, qword ptr [rsi + 0x18]
00366453  48 0F BA E0 3E                  bt rax, 0x3e
00366458  0F 82 8F FE FF FF               jb 0x1403662ed
0036645E  40 F6 C7 10                     test dil, 0x10
00366462  0F 85 85 FE FF FF               jne 0x1403662ed
00366468  48 8B 45 F0                     mov rax, qword ptr [rbp - 0x10]
0036646C  48 85 C0                        test rax, rax
0036646F  0F 84 87 08 00 00               je 0x140366cfc
00366475  48 8B D6                        mov rdx, rsi
00366478  48 8B C8                        mov rcx, rax
0036647B  E8 58 C3 0E 00                  call 0x1404527d8
00366480  8A 54 24 50                     mov dl, byte ptr [rsp + 0x50]
00366484  48 8B CE                        mov rcx, rsi
00366487  E8 54 3F FB FF                  call 0x14031a3e0
0036648C  C6 44 24 50 11                  mov byte ptr [rsp + 0x50], 0x11
00366491  E9 6E FE FF FF                  jmp 0x140366304
00366496  44 8B E2                        mov r12d, edx
00366499  E9 B4 FD FF FF                  jmp 0x140366252
0036649E  83 E7 BF                        and edi, 0xffffffbf
003664A1  83 CF 20                        or edi, 0x20
003664A4  E9 FF FC FF FF                  jmp 0x1403661a8
003664A9  41 F7 45 5C 00 00 0C 00         test dword ptr [r13 + 0x5c], 0xc0000
003664B1  0F 84 6C FD FF FF               je 0x140366223
003664B7  48 C1 E9 3C                     shr rcx, 0x3c
003664BB  80 E1 07                        and cl, 7
003664BE  80 F9 03                        cmp cl, 3
003664C1  0F 85 5C FD FF FF               jne 0x140366223
003664C7  48 8B 45 C8                     mov rax, qword ptr [rbp - 0x38]
003664CB  4D 8B C7                        mov r8, r15
003664CE  41 8B D6                        mov edx, r14d
003664D1  48 8B 48 40                     mov rcx, qword ptr [rax + 0x40]
003664D5  E8 26 30 12 00                  call 0x140489500
003664DA  33 D2                           xor edx, edx
003664DC  4C 63 E0                        movsxd r12, eax
003664DF  85 C0                           test eax, eax
003664E1  0F 89 6B FD FF FF               jns 0x140366252
003664E7  4D 8B C4                        mov r8, r12
003664EA  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
003664EF  4D 8B CF                        mov r9, r15
003664F2  BA 11 15 05 00                  mov edx, 0x51511
003664F7  B9 1A 00 00 00                  mov ecx, 0x1a
003664FC  E8 5F 71 19 00                  call 0x1404fd660
00366501  CC                              int3
00366502  40 F6 C7 10                     test dil, 0x10
00366506  0F 84 87 FD FF FF               je 0x140366293
0036650C  83 E7 EF                        and edi, 0xffffffef
0036650F  E9 7F FD FF FF                  jmp 0x140366293
00366514  8A 54 24 50                     mov dl, byte ptr [rsp + 0x50]
00366518  48 8B CE                        mov rcx, rsi
0036651B  E8 70 FB ED FF                  call 0x140246090
00366520  B8 02 00 00 00                  mov eax, 2
00366525  E9 64 FE FF FF                  jmp 0x14036638e
0036652A  49 83 E7 EF                     and r15, 0xffffffffffffffef
0036652E  E9 BA FB FF FF                  jmp 0x1403660ed
00366533  45 8B C6                        mov r8d, r14d
00366536  48 8B D3                        mov rdx, rbx
00366539  49 8B CD                        mov rcx, r13
0036653C  E8 8F DA F1 FF                  call 0x140283fd0
00366541  45 33 C9                        xor r9d, r9d
00366544  E9 E2 FD FF FF                  jmp 0x14036632b
00366549  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
00366553  85 D2                           test edx, edx
00366555  0F 84 0A 03 00 00               je 0x140366865
0036655B  C7 05 93 72 AC 00 7B 00 00 00   mov dword ptr [rip + 0xac7293], 0x7b
00366565  F0 48 21 46 18                  lock and qword ptr [rsi + 0x18], rax
0036656A  8A 54 24 50                     mov dl, byte ptr [rsp + 0x50]
0036656E  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00366573  E8 18 FB ED FF                  call 0x140246090
00366578  41 BC 09 07 00 C0               mov r12d, 0xc0000709
0036657E  4C 8B 7C 24 60                  mov r15, qword ptr [rsp + 0x60]
00366583  4C 8B 75 80                     mov r14, qword ptr [rbp - 0x80]
00366587  48 8B 45 F0                     mov rax, qword ptr [rbp - 0x10]
0036658B  48 85 C0                        test rax, rax
0036658E  74 0A                           je 0x14036659a
00366590  33 D2                           xor edx, edx
00366592  48 8B C8                        mov rcx, rax
00366595  E8 AE 11 0E 00                  call 0x140447748
0036659A  41 8B 46 04                     mov eax, dword ptr [r14 + 4]
0036659E  FF C8                           dec eax
003665A0  83 F8 FD                        cmp eax, -3
003665A3  0F 86 DD 08 00 00               jbe 0x140366e86
003665A9  33 C0                           xor eax, eax
003665AB  48 39 45 40                     cmp qword ptr [rbp + 0x40], rax
003665AF  74 09                           je 0x1403665ba
003665B1  48 8D 4D 30                     lea rcx, [rbp + 0x30]
003665B5  E8 7A EF 18 00                  call 0x1404f5534
003665BA  48 8D 45 60                     lea rax, [rbp + 0x60]
003665BE  4C 3B F0                        cmp r14, rax
003665C1  74 0A                           je 0x1403665cd
003665C3  33 D2                           xor edx, edx
003665C5  49 8B CE                        mov rcx, r14
003665C8  E8 A3 C2 81 00                  call 0x140b82870
003665CD  49 83 FF FF                     cmp r15, -1
003665D1  74 1D                           je 0x1403665f0
003665D3  4B 8D 0C 7F                     lea rcx, [r15 + r15*2]
003665D7  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
003665E1  48 C1 E1 04                     shl rcx, 4
003665E5  48 8B C0                        mov rax, rax
003665E8  48 03 C8                        add rcx, rax
003665EB  E8 F0 E4 FC FF                  call 0x140334ae0
003665F0  41 8B C4                        mov eax, r12d
003665F3  48 8B 8D 90 01 00 00            mov rcx, qword ptr [rbp + 0x190]
003665FA  48 33 CC                        xor rcx, rsp
003665FD  E8 3E 60 34 00                  call 0x1406ac640
00366602  48 81 C4 A8 02 00 00            add rsp, 0x2a8
00366609  41 5F                           pop r15
0036660B  41 5E                           pop r14
0036660D  41 5D                           pop r13
0036660F  41 5C                           pop r12
00366611  5F                              pop rdi
00366612  5E                              pop rsi
00366613  5B                              pop rbx
00366614  5D                              pop rbp
00366615  C3                              ret
00366616  CC                              int3
00366617  33 D2                           xor edx, edx
00366619  48 8B CE                        mov rcx, rsi
0036661C  E8 DF 37 0A 00                  call 0x140409e00
00366621  E9 6D FC FF FF                  jmp 0x140366293
00366626  48 8B CE                        mov rcx, rsi
00366629  E8 A2 A7 00 00                  call 0x140370dd0
0036662E  48 8B 4E 28                     mov rcx, qword ptr [rsi + 0x28]
00366632  48 8B D8                        mov rbx, rax
00366635  48 8B 05 4C 9A AC 00            mov rax, qword ptr [rip + 0xac9a4c]
0036663C  48 C1 E9 2B                     shr rcx, 0x2b
00366640  81 E1 FF 03 00 00               and ecx, 0x3ff
00366646  4C 8B 2C C8                     mov r13, qword ptr [rax + rcx*8]
0036664A  E9 76 FC FF FF                  jmp 0x1403662c5
0036664F  4B 8D 0C 7F                     lea rcx, [r15 + r15*2]
00366653  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
0036665D  48 C1 E1 04                     shl rcx, 4
00366661  48 8B C0                        mov rax, rax
00366664  48 03 C8                        add rcx, rax
00366667  E8 74 E4 FC FF                  call 0x140334ae0
0036666C  4C 8B 75 A0                     mov r14, qword ptr [rbp - 0x60]
00366670  49 83 CF FF                     or r15, 0xffffffffffffffff
00366674  4C 89 7C 24 60                  mov qword ptr [rsp + 0x60], r15
00366679  45 8D 47 02                     lea r8d, [r15 + 2]
0036667D  45 33 C9                        xor r9d, r9d
00366680  E9 27 F9 FF FF                  jmp 0x140365fac
00366685  44 8B 01                        mov r8d, dword ptr [rcx]
00366688  4C 8D 4D 48                     lea r9, [rbp + 0x48]
0036668C  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00366695  BA 03 00 00 00                  mov edx, 3
0036669A  41 C1 E8 14                     shr r8d, 0x14
0036669E  41 83 E0 7F                     and r8d, 0x7f
003666A2  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
003666A9  48 81 C1 00 04 00 00            add rcx, 0x400
003666B0  E8 5B 9D FB FF                  call 0x140320410
003666B5  48 8B 55 C8                     mov rdx, qword ptr [rbp - 0x38]
003666B9  45 33 C9                        xor r9d, r9d
003666BC  0F 11 45 60                     movups xmmword ptr [rbp + 0x60], xmm0
003666C0  C7 45 60 80 00 00 00            mov dword ptr [rbp + 0x60], 0x80
003666C7  E9 B0 F7 FF FF                  jmp 0x140365e7c
003666CC  48 39 55 F0                     cmp qword ptr [rbp - 0x10], rdx
003666D0  0F 85 85 FB FF FF               jne 0x14036625b
003666D6  B8 01 00 00 00                  mov eax, 1
003666DB  40 84 F8                        test al, dil
003666DE  0F 85 77 FB FF FF               jne 0x14036625b
003666E4  44 0F 20 C3                     mov rbx, cr8
003666E8  B8 02 00 00 00                  mov eax, 2
003666ED  44 0F 22 C0                     mov cr8, rax
003666F1  39 15 29 06 C6 00               cmp dword ptr [rip + 0xc60629], edx
003666F7  0F 85 26 08 00 00               jne 0x140366f23
003666FD  E8 62 20 F5 FF                  call 0x1402b8764
00366702  45 33 F6                        xor r14d, r14d
00366705  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
00366709  44 39 35 10 06 C6 00            cmp dword ptr [rip + 0xc60610], r14d
00366710  74 0B                           je 0x14036671d
00366712  44 0F 20 C1                     mov rcx, cr8
00366716  8A D3                           mov dl, bl
00366718  E8 7B EF 18 00                  call 0x1404f5698
0036671D  0F B6 CB                        movzx ecx, bl
00366720  44 0F 22 C1                     mov cr8, rcx
00366724  E9 35 FB FF FF                  jmp 0x14036625e
00366729  85 DB                           test ebx, ebx
0036672B  0F 85 DE 01 00 00               jne 0x14036690f
00366731  41 8B CE                        mov ecx, r14d
00366734  B8 00 10 00 00                  mov eax, 0x1000
00366739  81 E1 FF 0F 00 00               and ecx, 0xfff
0036673F  2B C1                           sub eax, ecx
00366741  8B C8                           mov ecx, eax
00366743  48 C1 E9 03                     shr rcx, 3
00366747  48 8B C1                        mov rax, rcx
0036674A  48 C1 E0 0C                     shl rax, 0xc
0036674E  48 01 45 98                     add qword ptr [rbp - 0x68], rax
00366752  44 03 F9                        add r15d, ecx
00366755  4D 8D 34 CE                     lea r14, [r14 + rcx*8]
00366759  4C 89 7C 24 68                  mov qword ptr [rsp + 0x68], r15
0036675E  4C 89 75 B8                     mov qword ptr [rbp - 0x48], r14
00366762  48 8B 5D B0                     mov rbx, qword ptr [rbp - 0x50]
00366766  E9 D1 F8 FF FF                  jmp 0x14036603c
0036676B  41 0B F8                        or edi, r8d
0036676E  E9 80 FA FF FF                  jmp 0x1403661f3
00366773  48 8B 45 C8                     mov rax, qword ptr [rbp - 0x38]
00366777  41 8B D6                        mov edx, r14d
0036677A  48 8B 48 20                     mov rcx, qword ptr [rax + 0x20]
0036677E  E8 3D 87 5D 00                  call 0x14093eec0
00366783  33 D2                           xor edx, edx
00366785  85 C0                           test eax, eax
00366787  0F 84 C5 FA FF FF               je 0x140366252
0036678D  4C 8B 75 80                     mov r14, qword ptr [rbp - 0x80]
00366791  48 8D 45 30                     lea rax, [rbp + 0x30]
00366795  48 8B 4D A8                     mov rcx, qword ptr [rbp - 0x58]
00366799  48 8D 55 48                     lea rdx, [rbp + 0x48]
0036679D  4D 8B CE                        mov r9, r14
003667A0  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
003667A5  4D 8B C7                        mov r8, r15
003667A8  E8 F3 42 17 00                  call 0x1404daaa0
003667AD  48 83 F8 FF                     cmp rax, -1
003667B1  0F 85 7B 03 00 00               jne 0x140366b32
003667B7  48 8B CE                        mov rcx, rsi
003667BA  C7 05 34 70 AC 00 78 00 00 00   mov dword ptr [rip + 0xac7034], 0x78
003667C4  E8 77 3B FB FF                  call 0x14031a340
003667C9  48 8B CE                        mov rcx, rsi
003667CC  8A D8                           mov bl, al
003667CE  E8 7D 01 EE FF                  call 0x140246950
003667D3  85 C0                           test eax, eax
003667D5  74 0B                           je 0x1403667e2
003667D7  49 8B D7                        mov rdx, r15
003667DA  48 8B CE                        mov rcx, rsi
003667DD  E8 5E 36 F5 FF                  call 0x1402b9e40
003667E2  8A D3                           mov dl, bl
003667E4  48 8B CE                        mov rcx, rsi
003667E7  E8 F4 3B FB FF                  call 0x14031a3e0
003667EC  4C 8B 7C 24 60                  mov r15, qword ptr [rsp + 0x60]
003667F1  41 BC 09 07 00 C0               mov r12d, 0xc0000709
003667F7  E9 8B FD FF FF                  jmp 0x140366587
003667FC  48 8B 05 F5 84 AC 00            mov rax, qword ptr [rip + 0xac84f5]
00366803  41 8B F9                        mov edi, r9d
00366806  48 89 45 68                     mov qword ptr [rbp + 0x68], rax
0036680A  48 C7 45 60 83 00 00 00         mov qword ptr [rbp + 0x60], 0x83
00366812  E9 65 F6 FF FF                  jmp 0x140365e7c
00366817  4C 3B C3                        cmp r8, rbx
0036681A  0F 83 EC 04 00 00               jae 0x140366d0c
00366820  49 8B C8                        mov rcx, r8
00366823  4C 89 45 B8                     mov qword ptr [rbp - 0x48], r8
00366827  49 2B CE                        sub rcx, r14
0036682A  4D 8B F0                        mov r14, r8
0036682D  48 C1 F9 03                     sar rcx, 3
00366831  44 03 F9                        add r15d, ecx
00366834  48 C1 E1 0C                     shl rcx, 0xc
00366838  48 03 D1                        add rdx, rcx
0036683B  4C 89 7C 24 68                  mov qword ptr [rsp + 0x68], r15
00366840  48 89 55 98                     mov qword ptr [rbp - 0x68], rdx
00366844  E9 EF F7 FF FF                  jmp 0x140366038
00366849  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
0036684D  48 C1 E8 3C                     shr rax, 0x3c
00366851  24 07                           and al, 7
00366853  3C 03                           cmp al, 3
00366855  0F 85 B0 F8 FF FF               jne 0x14036610b
0036685B  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
00366865  F0 48 21 46 18                  lock and qword ptr [rsi + 0x18], rax
0036686A  48 8B 74 24 58                  mov rsi, qword ptr [rsp + 0x58]
0036686F  4C 8B 7C 24 68                  mov r15, qword ptr [rsp + 0x68]
00366874  E9 02 FB FF FF                  jmp 0x14036637b
00366879  A8 08                           test al, 8
0036687B  0F 85 D1 02 00 00               jne 0x140366b52
00366881  49 8B CD                        mov rcx, r13
00366884  A8 20                           test al, 0x20
00366886  0F 85 76 05 00 00               jne 0x140366e02
0036688C  48 8B 45 A8                     mov rax, qword ptr [rbp - 0x58]
00366890  45 8B CE                        mov r9d, r14d
00366893  4C 8B 45 18                     mov r8, qword ptr [rbp + 0x18]
00366897  89 54 24 40                     mov dword ptr [rsp + 0x40], edx
0036689B  48 8B 55 98                     mov rdx, qword ptr [rbp - 0x68]
0036689F  8B 40 20                        mov eax, dword ptr [rax + 0x20]
003668A2  D1 E8                           shr eax, 1
003668A4  83 E0 1F                        and eax, 0x1f
003668A7  C7 44 24 38 00 00 00 04         mov dword ptr [rsp + 0x38], 0x4000000
003668AF  4C 89 7C 24 30                  mov qword ptr [rsp + 0x30], r15
003668B4  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
003668B8  E8 4B 81 5D 00                  call 0x14093ea08
003668BD  44 8B E0                        mov r12d, eax
003668C0  33 D2                           xor edx, edx
003668C2  E9 8B F9 FF FF                  jmp 0x140366252
003668C7  33 D2                           xor edx, edx
003668C9  48 8D 8D F0 00 00 00            lea rcx, [rbp + 0xf0]
003668D0  41 B8 98 00 00 00               mov r8d, 0x98
003668D6  E8 65 03 36 00                  call 0x1406c6c40
003668DB  45 33 C9                        xor r9d, r9d
003668DE  44 39 4C 24 74                  cmp dword ptr [rsp + 0x74], r9d
003668E3  0F 84 54 03 00 00               je 0x140366c3d
003668E9  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
003668F3  F0 48 21 46 18                  lock and qword ptr [rsi + 0x18], rax
003668F8  E9 6E FA FF FF                  jmp 0x14036636b
003668FD  48 8D 54 24 50                  lea rdx, [rsp + 0x50]
00366902  49 8B CE                        mov rcx, r14
00366905  E8 76 22 F5 FF                  call 0x1402b8b80
0036690A  E9 9C FA FF FF                  jmp 0x1403663ab
0036690F  45 33 C0                        xor r8d, r8d
00366912  49 8B D6                        mov rdx, r14
00366915  41 8D 48 02                     lea ecx, [r8 + 2]
00366919  E8 62 85 F1 FF                  call 0x14027ee80
0036691E  48 8B 5D B0                     mov rbx, qword ptr [rbp - 0x50]
00366922  45 33 C9                        xor r9d, r9d
00366925  E9 12 F7 FF FF                  jmp 0x14036603c
0036692A  8B 4C 24 70                     mov ecx, dword ptr [rsp + 0x70]
0036692E  41 84 C8                        test r8b, cl
00366931  0F 85 13 07 00 00               jne 0x14036704a
00366937  48 8B 45 F8                     mov rax, qword ptr [rbp - 8]
0036693B  F7 00 00 00 00 08               test dword ptr [rax], 0x8000000
00366941  0F 84 BF F6 FF FF               je 0x140366006
00366947  4C 8B 75 A0                     mov r14, qword ptr [rbp - 0x60]
0036694B  F6 C1 16                        test cl, 0x16
0036694E  0F 85 FA 06 00 00               jne 0x14036704e
00366954  66 45 29 86 E6 01 00 00         sub word ptr [r14 + 0x1e6], r8w
0036695C  48 8D 5A 28                     lea rbx, [rdx + 0x28]
00366960  48 8B CB                        mov rcx, rbx
00366963  45 33 C0                        xor r8d, r8d
00366966  33 D2                           xor edx, edx
00366968  90                              nop
00366969  E8 C2 98 EA FF                  call 0x140210230
0036696E  48 8B F0                        mov rsi, rax
00366971  33 C0                           xor eax, eax
00366973  8D 50 11                        lea edx, [rax + 0x11]
00366976  F0 48 0F B1 13                  lock cmpxchg qword ptr [rbx], rdx
0036697B  74 15                           je 0x140366992
0036697D  4C 8B CB                        mov r9, rbx
00366980  4C 8B C6                        mov r8, rsi
00366983  33 D2                           xor edx, edx
00366985  48 8B CB                        mov rcx, rbx
00366988  E8 BF 9A EA FF                  call 0x14021044c
0036698D  BA 11 00 00 00                  mov edx, 0x11
00366992  33 C9                           xor ecx, ecx
00366994  48 85 F6                        test rsi, rsi
00366997  74 04                           je 0x14036699d
00366999  C6 46 0A 01                     mov byte ptr [rsi + 0xa], 1
0036699D  48 8B 45 A8                     mov rax, qword ptr [rbp - 0x58]
003669A1  48 39 48 18                     cmp qword ptr [rax + 0x18], rcx
003669A5  0F 84 FF 03 00 00               je 0x140366daa
003669AB  8B 54 24 78                     mov edx, dword ptr [rsp + 0x78]
003669AF  4C 8B C0                        mov r8, rax
003669B2  49 8B CD                        mov rcx, r13
003669B5  E8 9E 23 FE FF                  call 0x140348d58
003669BA  33 C9                           xor ecx, ecx
003669BC  48 8B F0                        mov rsi, rax
003669BF  48 85 C0                        test rax, rax
003669C2  0F 85 CB 04 00 00               jne 0x140366e93
003669C8  8D 46 11                        lea eax, [rsi + 0x11]
003669CB  E9 DD 03 00 00                  jmp 0x140366dad
003669D0  45 85 F6                        test r14d, r14d
003669D3  0F 85 4A F4 FF FF               jne 0x140365e23
003669D9  49 8D 4D 38                     lea rcx, [r13 + 0x38]
003669DD  E9 51 F4 FF FF                  jmp 0x140365e33
003669E2  85 D2                           test edx, edx
003669E4  0F 84 40 F7 FF FF               je 0x14036612a
003669EA  C7 05 04 6E AC 00 7A 00 00 00   mov dword ptr [rip + 0xac6e04], 0x7a
003669F4  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
003669FE  E9 62 FB FF FF                  jmp 0x140366565
00366A03  41 84 CA                        test r10b, cl
00366A06  0F 85 4F FE FF FF               jne 0x14036685b
00366A0C  48 8B 46 10                     mov rax, qword ptr [rsi + 0x10]
00366A10  48 8B D0                        mov rdx, rax
00366A13  4C 8B C0                        mov r8, rax
00366A16  48 C1 EA 0B                     shr rdx, 0xb
00366A1A  48 C1 E8 03                     shr rax, 3
00366A1E  49 0F BA E0 0A                  bt r8, 0xa
00366A23  0F 42 C2                        cmovb eax, edx
00366A26  41 84 C2                        test r10b, al
00366A29  0F 85 1F F7 FF FF               jne 0x14036614e
00366A2F  E9 27 FE FF FF                  jmp 0x14036685b
00366A34  44 38 4E 23                     cmp byte ptr [rsi + 0x23], r9b
00366A38  0F 8C 34 F7 FF FF               jl 0x140366172
00366A3E  48 8B CE                        mov rcx, rsi
00366A41  E8 EA A4 F4 FF                  call 0x1402b0f30
00366A46  4C 8B 46 10                     mov r8, qword ptr [rsi + 0x10]
00366A4A  44 8B C8                        mov r9d, eax
00366A4D  48 8B 55 A8                     mov rdx, qword ptr [rbp - 0x58]
00366A51  48 8D 45 8C                     lea rax, [rbp - 0x74]
00366A55  48 8B 4D 00                     mov rcx, qword ptr [rbp]
00366A59  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00366A5E  E8 05 F2 FF FF                  call 0x140365c68
00366A63  85 C0                           test eax, eax
00366A65  0F 84 07 F7 FF FF               je 0x140366172
00366A6B  83 7D 8C 04                     cmp dword ptr [rbp - 0x74], 4
00366A6F  0F 87 FD F6 FF FF               ja 0x140366172
00366A75  48 8B CE                        mov rcx, rsi
00366A78  E8 53 78 F2 FF                  call 0x14028e2d0
00366A7D  83 F8 09                        cmp eax, 9
00366A80  74 19                           je 0x140366a9b
00366A82  8B 55 8C                        mov edx, dword ptr [rbp - 0x74]
00366A85  41 B8 04 00 00 00               mov r8d, 4
00366A8B  48 8B CE                        mov rcx, rsi
00366A8E  E8 35 20 FE FF                  call 0x140348ac8
00366A93  85 C0                           test eax, eax
00366A95  0F 85 D7 F6 FF FF               jne 0x140366172
00366A9B  83 CF 10                        or edi, 0x10
00366A9E  E9 D2 F6 FF FF                  jmp 0x140366175
00366AA3  48 8B 4D C8                     mov rcx, qword ptr [rbp - 0x38]
00366AA7  45 8B C6                        mov r8d, r14d
00366AAA  4C 8B 74 24 68                  mov r14, qword ptr [rsp + 0x68]
00366AAF  41 8B D6                        mov edx, r14d
00366AB2  E8 05 58 17 00                  call 0x1404dc2bc
00366AB7  33 D2                           xor edx, edx
00366AB9  85 C0                           test eax, eax
00366ABB  0F 84 1A F7 FF FF               je 0x1403661db
00366AC1  39 54 24 74                     cmp dword ptr [rsp + 0x74], edx
00366AC5  0F 84 24 04 00 00               je 0x140366eef
00366ACB  48 8B 4D 80                     mov rcx, qword ptr [rbp - 0x80]
00366ACF  44 8D 42 03                     lea r8d, [rdx + 3]
00366AD3  49 8B D7                        mov rdx, r15
00366AD6  E8 61 F5 0D 00                  call 0x14044603c
00366ADB  83 CF 40                        or edi, 0x40
00366ADE  33 D2                           xor edx, edx
00366AE0  E9 F6 F6 FF FF                  jmp 0x1403661db
00366AE5  41 81 FC 9A 00 00 C0            cmp r12d, 0xc000009a
00366AEC  41 8B C1                        mov eax, r9d
00366AEF  0F 95 C0                        setne al
00366AF2  83 C0 71                        add eax, 0x71
00366AF5  89 05 FD 6C AC 00               mov dword ptr [rip + 0xac6cfd], eax
00366AFB  E9 83 FA FF FF                  jmp 0x140366583
00366B00  48 8B 46 10                     mov rax, qword ptr [rsi + 0x10]
00366B04  41 B9 01 00 00 00               mov r9d, 1
00366B0A  48 8B D0                        mov rdx, rax
00366B0D  48 8B C8                        mov rcx, rax
00366B10  48 C1 E9 0B                     shr rcx, 0xb
00366B14  81 E2 00 04 00 00               and edx, 0x400
00366B1A  48 C1 E8 03                     shr rax, 3
00366B1E  48 85 D2                        test rdx, rdx
00366B21  0F 45 C1                        cmovne eax, ecx
00366B24  41 84 C1                        test r9b, al
00366B27  0F 85 74 F9 FF FF               jne 0x1403664a1
00366B2D  E9 73 F6 FF FF                  jmp 0x1403661a5
00366B32  48 8D 34 40                     lea rsi, [rax + rax*2]
00366B36  48 B9 00 00 00 00 00 DE FF FF   movabs rcx, 0xffffde0000000000
00366B40  48 C1 E6 04                     shl rsi, 4
00366B44  48 8B C9                        mov rcx, rcx
00366B47  48 03 F1                        add rsi, rcx
00366B4A  4C 8B F8                        mov r15, rax
00366B4D  E9 6E FD FF FF                  jmp 0x1403668c0
00366B52  48 F7 05 2B FF C5 00 00 20 00 00  test qword ptr [rip + 0xc5ff2b], 0x2000
00366B5D  0F 85 B3 01 00 00               jne 0x140366d16
00366B63  48 8B 55 D8                     mov rdx, qword ptr [rbp - 0x28]
00366B67  4D 8B CF                        mov r9, r15
00366B6A  45 8B C6                        mov r8d, r14d
00366B6D  49 8B CD                        mov rcx, r13
00366B70  E8 0F 33 0E 00                  call 0x140449e84
00366B75  E9 C8 F6 FF FF                  jmp 0x140366242
00366B7A  49 8B 0E                        mov rcx, qword ptr [r14]
00366B7D  48 0F BA E1 0A                  bt rcx, 0xa
00366B82  0F 82 79 04 00 00               jb 0x140367001
00366B88  E8 A3 89 00 00                  call 0x14036f530
00366B8D  85 C0                           test eax, eax
00366B8F  0F 84 6C 04 00 00               je 0x140367001
00366B95  8A 54 24 50                     mov dl, byte ptr [rsp + 0x50]
00366B99  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00366B9E  E8 ED F4 ED FF                  call 0x140246090
00366BA3  33 C0                           xor eax, eax
00366BA5  8B F0                           mov esi, eax
00366BA7  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
00366BAC  44 8D 48 02                     lea r9d, [rax + 2]
00366BB0  44 84 4C 24 70                  test byte ptr [rsp + 0x70], r9b
00366BB5  74 23                           je 0x140366bda
00366BB7  44 8D 40 01                     lea r8d, [rax + 1]
00366BBB  41 8B D7                        mov edx, r15d
00366BBE  48 8B 45 C8                     mov rax, qword ptr [rbp - 0x38]
00366BC2  48 8B 48 20                     mov rcx, qword ptr [rax + 0x20]
00366BC6  E8 F5 82 5D 00                  call 0x14093eec0
00366BCB  45 33 C9                        xor r9d, r9d
00366BCE  85 C0                           test eax, eax
00366BD0  0F 84 9F F7 FF FF               je 0x140366375
00366BD6  44 8D 4E 02                     lea r9d, [rsi + 2]
00366BDA  48 8B 4D A0                     mov rcx, qword ptr [rbp - 0x60]
00366BDE  41 8B D7                        mov edx, r15d
00366BE1  C1 E2 0C                        shl edx, 0xc
00366BE4  E8 F7 BA FF FF                  call 0x1403626e0
00366BE9  B9 05 00 00 00                  mov ecx, 5
00366BEE  3B C1                           cmp eax, ecx
00366BF0  0F 47 C1                        cmova eax, ecx
00366BF3  4C 3B 75 90                     cmp r14, qword ptr [rbp - 0x70]
00366BF7  0F 85 43 02 00 00               jne 0x140366e40
00366BFD  41 B8 00 10 00 00               mov r8d, 0x1000
00366C03  8B 4C 24 78                     mov ecx, dword ptr [rsp + 0x78]
00366C07  89 4C 24 28                     mov dword ptr [rsp + 0x28], ecx
00366C0B  49 8B CD                        mov rcx, r13
00366C0E  44 89 4C 24 20                  mov dword ptr [rsp + 0x20], r9d
00366C13  44 8B C8                        mov r9d, eax
00366C16  E8 15 7C 5D 00                  call 0x14093e830
00366C1B  45 33 C9                        xor r9d, r9d
00366C1E  85 C0                           test eax, eax
00366C20  79 13                           jns 0x140366c35
00366C22  4C 8D 05 57 9B CA FF            lea r8, [rip - 0x3564a9]
00366C29  33 D2                           xor edx, edx
00366C2B  33 C9                           xor ecx, ecx
00366C2D  E8 1E 29 EA FF                  call 0x140209550
00366C32  45 33 C9                        xor r9d, r9d
00366C35  45 8B E1                        mov r12d, r9d
00366C38  E9 FF F3 FF FF                  jmp 0x14036603c
00366C3D  B9 02 00 00 00                  mov ecx, 2
00366C42  84 D9                           test cl, bl
00366C44  0F 85 0D 02 00 00               jne 0x140366e57
00366C4A  48 8D 85 F0 00 00 00            lea rax, [rbp + 0xf0]
00366C51  45 33 C0                        xor r8d, r8d
00366C54  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00366C59  33 D2                           xor edx, edx
00366C5B  33 C9                           xor ecx, ecx
00366C5D  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
00366C62  E8 49 22 EC FF                  call 0x140228eb0
00366C67  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00366C6C  41 8D 40 01                     lea eax, [r8 + 1]
00366C70  8B D0                           mov edx, eax
00366C72  89 45 D0                        mov dword ptr [rbp - 0x30], eax
00366C75  E8 FE 14 FB FF                  call 0x140318178
00366C7A  44 8A 4C 24 50                  mov r9b, byte ptr [rsp + 0x50]
00366C7F  48 8D 45 D0                     lea rax, [rbp - 0x30]
00366C83  4C 8B 44 24 58                  mov r8, qword ptr [rsp + 0x58]
00366C88  48 8D 8D F0 00 00 00            lea rcx, [rbp + 0xf0]
00366C8F  48 8B D6                        mov rdx, rsi
00366C92  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00366C97  E8 40 32 00 00                  call 0x140369edc
00366C9C  4C 8B 7C 24 68                  mov r15, qword ptr [rsp + 0x68]
00366CA1  45 33 C9                        xor r9d, r9d
00366CA4  41 8B F1                        mov esi, r9d
00366CA7  4C 89 4C 24 58                  mov qword ptr [rsp + 0x58], r9
00366CAC  45 8B E1                        mov r12d, r9d
00366CAF  E9 AE FA FF FF                  jmp 0x140366762
00366CB4  48 83 7C 24 60 FF               cmp qword ptr [rsp + 0x60], -1
00366CBA  0F 85 A8 F5 FF FF               jne 0x140366268
00366CC0  49 8B CF                        mov rcx, r15
00366CC3  E8 58 0B FD FF                  call 0x140337820
00366CC8  8B 55 8C                        mov edx, dword ptr [rbp - 0x74]
00366CCB  45 33 C9                        xor r9d, r9d
00366CCE  48 8B 4D 00                     mov rcx, qword ptr [rbp]
00366CD2  44 8B C0                        mov r8d, eax
00366CD5  44 89 74 24 28                  mov dword ptr [rsp + 0x28], r14d
00366CDA  48 83 4C 24 20 FF               or qword ptr [rsp + 0x20], 0xffffffffffffffff
00366CE0  E8 D7 02 01 00                  call 0x140376fbc
00366CE5  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00366CEA  48 83 F8 FF                     cmp rax, -1
00366CEE  0F 85 74 F5 FF FF               jne 0x140366268
00366CF4  83 E7 EF                        and edi, 0xffffffef
00366CF7  E9 6C F5 FF FF                  jmp 0x140366268
00366CFC  49 8B D7                        mov rdx, r15
00366CFF  48 8B CE                        mov rcx, rsi
00366D02  E8 39 31 F5 FF                  call 0x1402b9e40
00366D07  E9 74 F7 FF FF                  jmp 0x140366480
00366D0C  4C 8B 7C 24 60                  mov r15, qword ptr [rsp + 0x60]
00366D11  E9 8C F2 FF FF                  jmp 0x140365fa2
00366D16  41 F7 45 5C 00 00 0C 00         test dword ptr [r13 + 0x5c], 0xc0000
00366D1E  0F 84 3F FE FF FF               je 0x140366b63
00366D24  48 C1 E9 3C                     shr rcx, 0x3c
00366D28  80 E1 07                        and cl, 7
00366D2B  80 F9 03                        cmp cl, 3
00366D2E  0F 85 2F FE FF FF               jne 0x140366b63
00366D34  48 8B 45 C8                     mov rax, qword ptr [rbp - 0x38]
00366D38  4D 8B C7                        mov r8, r15
00366D3B  41 8B D6                        mov edx, r14d
00366D3E  48 8B 48 40                     mov rcx, qword ptr [rax + 0x40]
00366D42  E8 B9 27 12 00                  call 0x140489500
00366D47  33 D2                           xor edx, edx
00366D49  4C 63 E0                        movsxd r12, eax
00366D4C  85 C0                           test eax, eax
00366D4E  0F 89 FE F4 FF FF               jns 0x140366252
00366D54  4D 8B C4                        mov r8, r12
00366D57  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
00366D5C  4D 8B CF                        mov r9, r15
00366D5F  BA 12 15 05 00                  mov edx, 0x51512
00366D64  B9 1A 00 00 00                  mov ecx, 0x1a
00366D69  E8 F2 68 19 00                  call 0x1404fd660
00366D6E  CC                              int3
00366D6F  8A 46 22                        mov al, byte ptr [rsi + 0x22]
00366D72  24 07                           and al, 7
00366D74  3C 06                           cmp al, 6
00366D76  0F 85 56 F5 FF FF               jne 0x1403662d2
00366D7C  8A 54 24 50                     mov dl, byte ptr [rsp + 0x50]
00366D80  45 33 C0                        xor r8d, r8d
00366D83  48 8B CE                        mov rcx, rsi
00366D86  E8 89 0F F3 FF                  call 0x140297d14
00366D8B  48 8B CE                        mov rcx, rsi
00366D8E  E8 AD 35 FB FF                  call 0x14031a340
00366D93  48 8B 46 18                     mov rax, qword ptr [rsi + 0x18]
00366D97  48 0F BA E0 3E                  bt rax, 0x3e
00366D9C  0F 83 30 F5 FF FF               jae 0x1403662d2
00366DA2  83 E7 EF                        and edi, 0xffffffef
00366DA5  E9 28 F5 FF FF                  jmp 0x1403662d2
00366DAA  48 8B C2                        mov rax, rdx
00366DAD  F0 48 0F B1 0B                  lock cmpxchg qword ptr [rbx], rcx
00366DB2  0F 85 23 02 00 00               jne 0x140366fdb
00366DB8  48 8B CB                        mov rcx, rbx
00366DBB  E8 40 A8 F7 FF                  call 0x1402e1600
00366DC0  41 B8 01 00 00 00               mov r8d, 1
00366DC6  90                              nop
00366DC7  66 45 01 86 E6 01 00 00         add word ptr [r14 + 0x1e6], r8w
00366DCF  75 18                           jne 0x140366de9
00366DD1  49 8D 86 98 00 00 00            lea rax, [r14 + 0x98]
00366DD8  90                              nop
00366DD9  48 39 00                        cmp qword ptr [rax], rax
00366DDC  74 0B                           je 0x140366de9
00366DDE  E8 9D BE F7 FF                  call 0x1402e2c80
00366DE3  41 B8 01 00 00 00               mov r8d, 1
00366DE9  4C 8B 7C 24 60                  mov r15, qword ptr [rsp + 0x60]
00366DEE  E9 8A F8 FF FF                  jmp 0x14036667d
00366DF3  C7 05 FB 69 AC 00 79 00 00 00   mov dword ptr [rip + 0xac69fb], 0x79
00366DFD  E9 68 F7 FF FF                  jmp 0x14036656a
00366E02  44 89 44 24 20                  mov dword ptr [rsp + 0x20], r8d
00366E07  4D 8B CF                        mov r9, r15
00366E0A  45 8B C6                        mov r8d, r14d
00366E0D  33 D2                           xor edx, edx
00366E0F  E8 D0 0D 19 00                  call 0x1404f7be4
00366E14  E9 A7 FA FF FF                  jmp 0x1403668c0
00366E19  8B 55 60                        mov edx, dword ptr [rbp + 0x60]
00366E1C  44 8B CB                        mov r9d, ebx
00366E1F  44 8B C2                        mov r8d, edx
00366E22  48 8B C8                        mov rcx, rax
00366E25  41 D1 E8                        shr r8d, 1
00366E28  83 E2 01                        and edx, 1
00366E2B  41 83 E0 03                     and r8d, 3
00366E2F  E8 CC F1 0D 00                  call 0x140446000
00366E34  49 8D 9D 80 00 00 00            lea rbx, [r13 + 0x80]
00366E3B  E9 83 F1 FF FF                  jmp 0x140365fc3
00366E40  4C 8B C3                        mov r8, rbx
00366E43  4C 89 75 90                     mov qword ptr [rbp - 0x70], r14
00366E47  4D 2B C6                        sub r8, r14
00366E4A  49 C1 F8 03                     sar r8, 3
00366E4E  49 C1 E0 0C                     shl r8, 0xc
00366E52  E9 AC FD FF FF                  jmp 0x140366c03
00366E57  41 8B 45 38                     mov eax, dword ptr [r13 + 0x38]
00366E5B  84 C1                           test cl, al
00366E5D  0F 85 E7 FD FF FF               jne 0x140366c4a
00366E63  41 B8 11 00 00 00               mov r8d, 0x11
00366E69  48 8B D6                        mov rdx, rsi
00366E6C  49 8B CE                        mov rcx, r14
00366E6F  E8 FC AC 00 00                  call 0x140371b70
00366E74  48 8B 74 24 58                  mov rsi, qword ptr [rsp + 0x58]
00366E79  45 33 C9                        xor r9d, r9d
00366E7C  4C 8B 7C 24 68                  mov r15, qword ptr [rsp + 0x68]
00366E81  E9 EF F4 FF FF                  jmp 0x140366375
00366E86  49 8B CE                        mov rcx, r14
00366E89  E8 CE F2 0D 00                  call 0x14044615c
00366E8E  E9 16 F7 FF FF                  jmp 0x1403665a9
00366E93  B8 01 00 00 00                  mov eax, 1
00366E98  01 46 50                        add dword ptr [rsi + 0x50], eax
00366E9B  B8 11 00 00 00                  mov eax, 0x11
00366EA0  F0 48 0F B1 0B                  lock cmpxchg qword ptr [rbx], rcx
00366EA5  0F 85 3D 01 00 00               jne 0x140366fe8
00366EAB  48 8B CB                        mov rcx, rbx
00366EAE  E8 4D A7 F7 FF                  call 0x1402e1600
00366EB3  41 B9 01 00 00 00               mov r9d, 1
00366EB9  90                              nop
00366EBA  66 45 01 8E E6 01 00 00         add word ptr [r14 + 0x1e6], r9w
00366EC2  75 12                           jne 0x140366ed6
00366EC4  49 8D 86 98 00 00 00            lea rax, [r14 + 0x98]
00366ECB  90                              nop
00366ECC  48 39 00                        cmp qword ptr [rax], rax
00366ECF  74 05                           je 0x140366ed6
00366ED1  E8 AA BD F7 FF                  call 0x1402e2c80
00366ED6  4C 8B 76 48                     mov r14, qword ptr [rsi + 0x48]
00366EDA  83 CF 08                        or edi, 8
00366EDD  48 8B 74 24 58                  mov rsi, qword ptr [rsp + 0x58]
00366EE2  48 8B 5D A8                     mov rbx, qword ptr [rbp - 0x58]
00366EE6  4C 89 75 B8                     mov qword ptr [rbp - 0x48], r14
00366EEA  E9 17 F1 FF FF                  jmp 0x140366006
00366EEF  44 8B 44 24 70                  mov r8d, dword ptr [rsp + 0x70]
00366EF4  49 8B CD                        mov rcx, r13
00366EF7  44 8B 4C 24 78                  mov r9d, dword ptr [rsp + 0x78]
00366EFC  41 83 C8 10                     or r8d, 0x10
00366F00  48 8B 55 D8                     mov rdx, qword ptr [rbp - 0x28]
00366F04  E8 67 EE FF FF                  call 0x140365d70
00366F09  0F BA EF 07                     bts edi, 7
00366F0D  E9 CC FB FF FF                  jmp 0x140366ade
00366F12  B8 01 00 00 00                  mov eax, 1
00366F17  44 3B E0                        cmp r12d, eax
00366F1A  44 0F 44 E2                     cmove r12d, edx
00366F1E  E9 2F F3 FF FF                  jmp 0x140366252
00366F23  8A D0                           mov dl, al
00366F25  8A CB                           mov cl, bl
00366F27  E8 D0 E7 18 00                  call 0x1404f56fc
00366F2C  E9 CC F7 FF FF                  jmp 0x1403666fd
00366F31  8A 46 22                        mov al, byte ptr [rsi + 0x22]
00366F34  24 07                           and al, 7
00366F36  2C 02                           sub al, 2
00366F38  41 3A C6                        cmp al, r14b
00366F3B  0F 87 C3 F3 FF FF               ja 0x140366304
00366F41  8B 46 20                        mov eax, dword ptr [rsi + 0x20]
00366F44  66 85 C0                        test ax, ax
00366F47  0F 85 B7 F3 FF FF               jne 0x140366304
00366F4D  38 4E 23                        cmp byte ptr [rsi + 0x23], cl
00366F50  0F 8C AE F3 FF FF               jl 0x140366304
00366F56  4C 8B 7C 24 60                  mov r15, qword ptr [rsp + 0x60]
00366F5B  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
00366F65  4F 8D 14 7F                     lea r10, [r15 + r15*2]
00366F69  49 C1 E2 04                     shl r10, 4
00366F6D  48 8B C0                        mov rax, rax
00366F70  4C 03 D0                        add r10, rax
00366F73  49 8B CA                        mov rcx, r10
00366F76  E8 55 73 F2 FF                  call 0x14028e2d0
00366F7B  83 F8 09                        cmp eax, 9
00366F7E  0F 84 85 F3 FF FF               je 0x140366309
00366F84  48 8B CE                        mov rcx, rsi
00366F87  E8 44 73 F2 FF                  call 0x14028e2d0
00366F8C  44 8B C0                        mov r8d, eax
00366F8F  49 8B D2                        mov rdx, r10
00366F92  48 8B CE                        mov rcx, rsi
00366F95  45 33 C9                        xor r9d, r9d
00366F98  E8 83 A1 F4 FF                  call 0x1402b1120
00366F9D  8B C8                           mov ecx, eax
00366F9F  C1 E1 04                        shl ecx, 4
00366FA2  33 CF                           xor ecx, edi
00366FA4  83 E1 10                        and ecx, 0x10
00366FA7  33 F9                           xor edi, ecx
00366FA9  41 84 C6                        test r14b, al
00366FAC  0F 84 57 F3 FF FF               je 0x140366309
00366FB2  48 8B 05 C7 98 CA FF            mov rax, qword ptr [rip - 0x356739]
00366FB9  48 8D 4E 10                     lea rcx, [rsi + 0x10]
00366FBD  49 83 CF FF                     or r15, 0xffffffffffffffff
00366FC1  48 89 01                        mov qword ptr [rcx], rax
00366FC4  4C 89 7C 24 60                  mov qword ptr [rsp + 0x60], r15
00366FC9  E8 CE 39 F2 FF                  call 0x14028a99c
00366FCE  48 8B CE                        mov rcx, rsi
00366FD1  E8 02 5E 0E 00                  call 0x14044cdd8
00366FD6  E9 2E F3 FF FF                  jmp 0x140366309
00366FDB  48 8B CB                        mov rcx, rbx
00366FDE  E8 5D C4 EF FF                  call 0x140263440
00366FE3  E9 D0 FD FF FF                  jmp 0x140366db8
00366FE8  48 8B CB                        mov rcx, rbx
00366FEB  E8 50 C4 EF FF                  call 0x140263440
00366FF0  E9 B6 FE FF FF                  jmp 0x140366eab
00366FF5  49 8D 9D 80 00 00 00            lea rbx, [r13 + 0x80]
00366FFC  E9 CF EF FF FF                  jmp 0x140365fd0
00367001  48 8B 74 24 58                  mov rsi, qword ptr [rsp + 0x58]
00367006  E9 6A F3 FF FF                  jmp 0x140366375
0036700B  F6 C3 10                        test bl, 0x10
0036700E  B8 02 00 00 00                  mov eax, 2
00367013  0F 94 C2                        sete dl
00367016  40 84 F8                        test al, dil
00367019  0F 94 C0                        sete al
0036701C  84 D0                           test al, dl
0036701E  0F 85 37 F8 FF FF               jne 0x14036685b
00367024  E9 F0 F0 FF FF                  jmp 0x140366119
00367029  48 8B 46 18                     mov rax, qword ptr [rsi + 0x18]
0036702D  48 B9 00 00 00 00 00 00 00 C0   movabs rcx, 0xc000000000000000
00367037  48 23 C1                        and rax, rcx
0036703A  45 33 C9                        xor r9d, r9d
0036703D  48 89 46 18                     mov qword ptr [rsi + 0x18], rax
00367041  45 8D 51 01                     lea r10d, [r9 + 1]
00367045  E9 15 F1 FF FF                  jmp 0x14036615f
0036704A  4C 8B 75 A0                     mov r14, qword ptr [rbp - 0x60]
0036704E  4C 8B 7C 24 60                  mov r15, qword ptr [rsp + 0x60]
00367053  E9 54 EF FF FF                  jmp 0x140365fac
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiWalkEntireImage(__int64 a1, __int64 a2, int a3, int a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m180;
    unsigned int v_stack_m184;
    unsigned __int64 v_stack_m188;
    unsigned __int64 v_stack_m1A0;
    unsigned __int64 v_stack_m1A8;
    unsigned __int64 v_stack_m1B8;
    unsigned __int64 v_stack_m1C0;
    unsigned __int64 v_stack_m1C8;
    unsigned __int64 v_stack_m1D0;
    unsigned __int64 v_stack_m1D8;
    unsigned __int64 v_stack_m1E8;
    unsigned __int64 v_stack_m1F0;
    unsigned __int64 v_stack_m1F8;
    unsigned int v_stack_m200;
    unsigned __int64 v_stack_m208;
    unsigned __int64 v_stack_m210;
    unsigned int v_stack_m214;
    unsigned int v_stack_m218;
    unsigned __int64 v_stack_m220;
    unsigned __int64 v_stack_m228;
    unsigned __int64 v_stack_m230;
    unsigned __int64 v_stack_m238;
    unsigned __int64 v_stack_m240;
    unsigned __int64 v_stack_m248;
    unsigned __int64 v_stack_m250;
    unsigned __int64 v_stack_m258;
    unsigned int v_stack_m25C;
    unsigned int v_stack_m260;
    unsigned __int64 v_stack_m268;
    unsigned int v_stack_m270;
    unsigned int v_stack_m274;
    unsigned int v_stack_m278;
    unsigned __int64 v_stack_m280;
    unsigned __int64 v_stack_m288;
    unsigned __int64 v_stack_m290;
    unsigned __int8 v_stack_m298;
    unsigned int v_stack_m2B8;
    unsigned __int64 v_stack_m2C8;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned int v_stack_p38;
    unsigned int v_stack_p40;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned int v_stack_p70;
    unsigned int v_stack_p74;
    unsigned int v_stack_p78;

    v_rsp = (v_rsp) - (680);
    result = (*(unsigned __int64 *)(v_rip + 11159981)) ^ (v_rsp);
    v_stack_m58 = result;
    v_stack_m278 = a3;
    v_stack_m210 = a2;
    v_stack_m1C8 = a1;
    result = 0;
    v_stack_m218 = 0;
    a2 = 0;
    v_stack_m270 = a4;
    v_stack_m1A0 = v_xmm0;
    result = memset(v_stack_m188, a2, 144, a4);
    a4 = 0;
    a1 = (unsigned int)((*(unsigned __int16 *)(a1 + 60)) & (0x3FFULL));
    v_stack_m228 = *(unsigned __int64 *)(a1);
    a2 = (*(unsigned __int64 *)(a1 + 96)) & (-8);
    v_r14 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a3)))) & (4));
    v_stack_m220 = a2;
    v_stack_m260 = (unsigned int)(v_r14);
    v_stack_m1E8 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11313806) + a1 * 8);
    result = (unsigned __int8)((*(unsigned __int8 *)(a1 + 62)) & (12));
    if (((unsigned __int8)(result)) == 4) goto loc_003669D0;
loc_00365E23:
    v_stack_m1F0 = a1 + 56;
    v_rdi = 0;
    if (((*(unsigned int *)(a1 + 56)) & (0x800ULL)) != 0) {
        v_stack_m1F0 = a1 + 56;
        v_rdi = (unsigned int)(a4 + 2);
    }
    v_stack_m248 = *(unsigned __int64 *)(gs_base + (0 + 392));
    result = 0;
    v_stack_m1A8 = 0;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a3)))) & (16));
    v_stack_m208 = 0;
    v_stack_m274 = (unsigned int)(result);
    v_stack_m1B8 = v_xmm0;
    v_stack_m268 = v_stack_m188;
    if (condition_is_not_equal) goto loc_003667FC;
    if ((unsigned int)(v_r14) != 0) goto loc_00366685;
loc_00365E7C:
    v_r15 = (v_r15) | (-1);
    v_stack_m240 = a1 + 128;
    v_stack_m25C = 0;
    v_stack_m1D0 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184);
    v_stack_m1D8 = *(unsigned __int64 *)(a1 + 128 + 8);
    v_stack_m298 = 17;
    v_stack_m290 = 0;
    v_stack_m1F8 = 0;
    v_stack_m288 = v_r15;
    if (((*(unsigned __int64 *)(v_rip + 12979177)) & (0x2000ULL)) == 0) goto loc_00365EFB;
    if (((*(unsigned int *)(a1 + 92)) & (0xC0000ULL)) == 0) goto loc_00365EFB;
    if ((*(unsigned __int64 *)(a2 + 64)) != 0) goto loc_00365EFB;
    result = MiGetSectionStrongImageReference(a2, a2, a4 + 2, a4);
    a4 = 0;
    if (sign_flag) goto loc_003665F3;
loc_00365EFB:
    v_stack_m200 = 0;
    if ((unsigned int)(v_r14) != 0) {
        a1 = v_stack_m210;
        a2 = 0;
        result = MiGetNextDirectFixupProto(a1, a2, a4 + 2, a4);
        v_stack_m208 = result;
    }
    if (v_stack_m184 == -1) goto loc_00365FD0;
    v_rbx = 511;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m228 + 8)))) < 511) { v_rbx = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m228 + 8))); }
    a1 = (unsigned int)(((unsigned int)(v_stack_m188)) >> (3));
    if (((unsigned int)(v_rbx)) <= ((unsigned int)(a1))) goto loc_00366FF5;
    result = MiAllocatePool(1 + 65, v_rbx * 8 + 16, (unsigned int)(0x6C68694DULL), a4);
    a4 = 0;
    v_stack_m268 = result;
    if (result != 0) goto loc_00366E19;
    v_stack_m268 = v_stack_m188;
    goto loc_00365FC6;
loc_00365F7A:
    result = v_stack_m188;
    if (0 != 0) {
        a2 = v_stack_m298;
        a1 = 0;
        result = MiUnlockProtoPoolPage(a1, a2, (unsigned int)(0x6C68694DULL), a4);
        a4 = 0;
        v_stack_m290 = 0;
    }
    if (v_stack_m288 != -1) goto loc_0036664F;
loc_00365FA2:
loc_00365FAC:
    v_stack_m240 = v_stack_m1C0;
loc_00365FC3:
    a4 = 0;
loc_00365FC6:
loc_00365FD0:
    if (v_stack_m1C0 == 0) goto loc_00366583;
    v_r15 = (*(unsigned __int64 *)(v_stack_m1C0 + 8)) - (v_stack_m1D8);
    v_r15 = (v_r15) >> (3);
    v_stack_m1C0 = *(unsigned __int64 *)(v_stack_m1C0 + 16);
    v_stack_m230 = *(unsigned __int64 *)(v_stack_m1C0 + 8);
    v_stack_m280 = v_r15;
    if (condition_is_below) goto loc_0036692A;
loc_00366006:
    result = MiStartingOffset(v_stack_m1C0, *(unsigned __int64 *)(v_stack_m1C0 + 8), (unsigned int)(v_stack_m270), a4);
    a4 = 0;
    v_stack_m250 = result;
    v_stack_m238 = *(unsigned __int64 *)(v_stack_m1C0 + 8) + (unsigned int)(*(unsigned int *)(v_stack_m1C0 + 44)) * 8;
    if (v_stack_m208 != 0) goto loc_00366817;
loc_00366038:
    v_stack_m258 = 0;
loc_0036603C:
loc_00366041:
    if ((*(unsigned __int64 *)(v_stack_m1C0 + 8)) >= (*(unsigned __int64 *)(v_stack_m1C0 + 8) + (unsigned int)(*(unsigned int *)(v_stack_m1C0 + 44)) * 8)) goto loc_00365F7A;
    if (((*(unsigned __int64 *)(v_stack_m1C0 + 8)) & (0xFFFULL)) == 0) goto loc_00366385;
    if (v_stack_m290 == 0) goto loc_00366385;
loc_00366060:
    a2 = 0;
    result = MiLockLeafPage(*(unsigned __int64 *)(v_stack_m1C0 + 8), a2, v_stack_m208, a4);
    a4 = 0;
    if (result != 0) goto loc_003660BE;
    if (v_stack_m260 != 0) goto loc_00366DF3;
    if ((((unsigned __int8)(result + 2)) & ((unsigned __int8)(v_rdi))) != 0) goto loc_00366B7A;
loc_00366090:
loc_00366096:
    v_r14 = (*(unsigned __int64 *)(v_stack_m1C0 + 8)) + (8);
    v_r15 = (unsigned int)((v_r15) + (1));
    v_stack_m230 = v_r14;
    v_stack_m280 = v_r15;
    goto loc_00366041;
loc_003660BE:
    if (((1) & ((unsigned __int8)(*(unsigned __int64 *)(v_r14)))) != 0) goto loc_003660ED;
    if (*(unsigned __int64 *)(v_rip + 11303850) == 0) goto loc_003660ED;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_r14))) & (16)) != 0) goto loc_0036652A;
    v_r15 = ~(*(unsigned __int64 *)(v_rip + 11303850));
    v_r15 = (v_r15) & (*(unsigned __int64 *)(v_r14));
loc_003660ED:
    v_r15 = (v_r15) >> (12);
    v_r15 = (v_r15) & (*(unsigned __int64 *)(v_rip + 11303850));
    if (((1) & ((unsigned __int8)((unsigned int)(v_stack_m278)))) != 0) goto loc_00366849;
loc_0036610B:
    if (condition_is_above_or_equal) goto loc_0036700B;
loc_00366119:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m290 + 32))) >> (24));
    if ((((unsigned __int8)(result)) & (64)) != 0) goto loc_003669E2;
loc_0036612A:
    if (((*(unsigned __int8 *)(v_stack_m290 + 35)) & (16)) != 0) goto loc_00366549;
    if (((1) & ((unsigned __int8)(*(unsigned __int64 *)(v_r14)))) != 0) goto loc_00366143;
    if (((*(unsigned __int8 *)(v_stack_m290 + 34)) & (32)) != 0) goto loc_003668C7;
loc_00366143:
    if (v_stack_m274 != 0) goto loc_00366A03;
loc_0036614E:
    v_stack_m214 = 8;
    if (((1) & ((unsigned __int8)(*(unsigned __int64 *)(v_r14)))) == 0) goto loc_003663C8;
loc_0036615F:
    result = (unsigned __int8)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m278)))) & (17));
    if (((unsigned __int8)(result)) == 1) goto loc_00366A34;
loc_00366172:
    v_rdi = (unsigned int)((v_rdi) & (0xFFFFFFEFULL));
loc_00366175:
    result = MiAddLockedPageCharge(v_stack_m290, 1, v_stack_m208, a4);
    a3 = 0;
    if (v_stack_m274 != 0) goto loc_0036649E;
    if (sign_flag) goto loc_003661A5;
    if (((*(unsigned int *)(v_rip + 12978457)) & (0x200000ULL)) != 0) goto loc_00366B00;
loc_003661A5:
    v_rdi = (unsigned int)((v_rdi) & (0xFFFFFFDFULL));
loc_003661A8:
    result = MiUnlockProtoPoolPage(v_stack_m290, v_stack_m298, a3, a4);
    a2 = 0;
    v_stack_m290 = 0;
    if ((((unsigned __int8)(v_rdi)) & (32)) != 0) goto loc_00366AA3;
loc_003661DB:
    if (condition_is_below) goto loc_0036676B;
    v_rdi = (unsigned int)((v_rdi) & (0xFFFFFFFEULL));
loc_003661F3:
    if (v_stack_m274 != 0) goto loc_00366496;
    if (v_stack_m260 != 0) goto loc_00366773;
    if ((((unsigned __int8)((unsigned int)(v_stack_m278))) & (2)) == 0) goto loc_00366879;
    if (((*(unsigned __int64 *)(v_rip + 12978283)) & (0x2000ULL)) != 0) goto loc_003664A9;
loc_00366223:
    v_stack_m2B8 = 65;
    v_stack_m2C8 = 0;
    result = MiRelocateImagePfn(a1, v_stack_m210, (unsigned int)((unsigned int)(v_stack_m280)), v_r15);
loc_00366242:
    a2 = 0;
    if ((unsigned int)(result) != 0) goto loc_00366F12;
    v_rdi = (unsigned int)((v_rdi) | (4));
loc_00366252:
    if (8 != 8) goto loc_003666CC;
loc_0036625B:
    v_r14 = 0;
loc_0036625E:
    if ((((unsigned __int8)(v_rdi)) & (16)) != 0) goto loc_00366CB4;
loc_00366268:
    result = MiLockPageInline(v_stack_m290, a2, (unsigned int)((unsigned int)(v_stack_m280)), v_r15);
    v_stack_m298 = (unsigned __int8)(result);
    if (condition_is_below) goto loc_00366502;
    if ((((unsigned __int8)(v_rdi)) & (64)) != 0) goto loc_00366617;
loc_00366293:
    v_r14 = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) & (0xFFFFFFEFULL));
    if (!sign_flag) { v_r14 = (unsigned int)(v_rdi); }
    if ((((unsigned __int8)((unsigned int)(v_stack_m278))) & (8)) != 0) goto loc_003662B6;
    result = (unsigned __int8)(((unsigned int)(v_stack_m278)) & (18));
    if (((unsigned __int8)(result)) != 2) goto loc_003662C5;
loc_003662B6:
    if (((unsigned __int8)(result)) >= 2) goto loc_00366626;
loc_003662C5:
    if ((((unsigned __int8)(v_r14)) & (16)) != 0) goto loc_00366D6F;
loc_003662D2:
    result = MiRemoveLockedPageCharge(v_stack_m290, a2, (unsigned int)((unsigned int)(v_stack_m280)), v_r15);
    a1 = 0;
    if ((unsigned int)(result) == 0) goto loc_003662FA;
    if ((((unsigned __int8)(a1 + 1)) & ((unsigned __int8)((unsigned int)((unsigned int)(v_r14))))) == 0) goto loc_0036643B;
loc_003662ED:
    result = MiPfnReferenceCountIsZero(v_stack_m290, v_r15, (unsigned int)((unsigned int)(v_stack_m280)), v_r15);
    a1 = 0;
loc_003662FA:
    if ((((unsigned __int8)((unsigned int)((unsigned int)(v_r14)))) & (16)) != 0) goto loc_00366F31;
loc_00366304:
loc_00366309:
    if (v_stack_m298 != 17) {
    }
    a4 = 0;
    if (0 != 0) goto loc_00366533;
loc_0036632B:
    if (((unsigned __int8)(v_stack_m298)) == 17) goto loc_0036635A;
    if ((*(unsigned int *)(v_rip + 12978657)) != 0) {
        a1 = v_cr8;
        result = KiLowerIrqlProcessIrqlFlags(a1, v_stack_m298, (unsigned int)((unsigned int)(v_stack_m280)), a4);
        a4 = 0;
    }
    v_stack_m298 = 17;
loc_0036635A:
    if (sign_flag) goto loc_00366AE5;
loc_0036636B:
loc_00366375:
loc_0036637B:
    goto loc_00366096;
loc_00366385:
    if (v_stack_m290 != 0) goto loc_00366514;
loc_0036638E:
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r14))))) & (2));
    if (condition_is_not_equal) goto loc_003668FD;
    a3 = 0;
    result = MiCheckProtoPtePageState(v_stack_m1C8, v_stack_m230, a3, v_stack_m298);
loc_003663AB:
    a4 = 0;
    v_stack_m290 = result;
    if (result == 0) goto loc_00366729;
    goto loc_00366060;
loc_003663C8:
    result = MiGetPfnSlabType(result, v_stack_m230, a3, a4);
    if (((unsigned int)(result)) != 9) goto loc_003663EB;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 32))) >> (24));
    v_rbx = v_stack_m238;
    if ((((unsigned __int8)(v_stack_m238)) & ((unsigned __int8)(result))) != 0) {
        v_rbx = *(unsigned int *)(result + 32);
        v_rbx = (unsigned int)((v_rbx) >> (24));
        v_rbx = (unsigned int)((v_rbx) & (7));
        v_stack_m214 = (unsigned int)(v_rbx);
    }
    a2 = 0;
    result = MiUnlinkPageFromListEx(result, a2, a3, a4);
    if ((((unsigned __int8)(result)) & (3)) == 0) goto loc_00367029;
    a2 = 0;
    result = MiDiscardTransitionPteEx(result, a2, a3, a4);
    if (((2) & ((unsigned __int8)((unsigned int)((unsigned int)(v_r14))))) != 0) goto loc_00366041;
    goto loc_00366090;
loc_0036643B:
    if (v_stack_m214 == 8) goto loc_003662ED;
    if (((*(unsigned __int8 *)(v_stack_m290 + 34)) & (16)) != 0) goto loc_003662ED;
    if (condition_is_below) goto loc_003662ED;
    if ((((unsigned __int8)((unsigned int)((unsigned int)(v_r14)))) & (16)) != 0) goto loc_003662ED;
    if (v_stack_m1F8 == 0) goto loc_00366CFC;
    result = MiInsertProtectedStandbyPage(v_stack_m1F8, v_stack_m290, a3, 2 - 2);
loc_00366480:
    result = MiUnlockPage(v_stack_m290, v_stack_m298, a3, 2 - 2);
    v_stack_m298 = 17;
    goto loc_00366304;
loc_00366496:
    goto loc_00366252;
loc_0036649E:
    v_rdi = (unsigned int)(((unsigned int)((unsigned int)(v_r14))) & (0xFFFFFFBFULL));
loc_003664A1:
    v_rdi = (unsigned int)((v_rdi) | (32));
    goto loc_003661A8;
loc_003664A9:
    if (((*(unsigned int *)(v_stack_m1C8 + 92)) & (0xC0000ULL)) == 0) goto loc_00366223;
    a1 = (v_stack_m290) >> (60);
    a1 = (unsigned __int8)((a1) & (7));
    if (((unsigned __int8)(a1)) != 3) goto loc_00366223;
    result = VslApplySecureImageFixups(*(unsigned __int64 *)(v_stack_m220 + 64), (unsigned int)((unsigned int)(v_stack_m230)), v_stack_m280, 2 - 2);
    a2 = 0;
    if (!sign_flag) goto loc_00366252;
    v_stack_m2C8 = v_stack_m1C8;
    result = KeBugCheckEx(26, (unsigned int)(0x51511ULL), (int)((unsigned int)(result)), v_stack_m280);
loc_00366502:
    if ((((unsigned __int8)(v_rdi)) & (16)) == 0) goto loc_00366293;
    v_rdi = (unsigned int)((v_rdi) & (0xFFFFFFEFULL));
    goto loc_00366293;
loc_00366514:
    result = MiUnlockProtoPoolPage(v_stack_m290, v_stack_m298, (int)((unsigned int)(result)), v_stack_m280);
    goto loc_0036638E;
loc_0036652A:
    v_r15 = (v_stack_m280) & (-17);
    goto loc_003660ED;
loc_00366533:
    result = MiReleasePageFileInfo(v_stack_m1C8, v_stack_m238, (unsigned int)((unsigned int)(v_stack_m230)), v_stack_m280);
    a4 = 0;
    goto loc_0036632B;
loc_00366549:
    if ((unsigned int)(v_stack_m238) == 0) goto loc_00366865;
    *(unsigned int *)(v_rip + 11301523) = 123;
loc_00366565:
loc_0036656A:
    result = MiUnlockProtoPoolPage(v_stack_m290, v_stack_m298, (unsigned int)((unsigned int)(v_stack_m230)), a4);
loc_00366583:
loc_00366587:
    result = v_stack_m1F8;
    if (v_stack_m1F8 != 0) {
        a2 = 0;
        a1 = v_stack_m1F8;
        result = MiDecayPfnFullyInitialized(a1, a2, (unsigned int)((unsigned int)(v_stack_m230)), a4);
    }
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m268 + 4))) - 1);
    if (((unsigned int)(result)) <= -3) goto loc_00366E86;
loc_003665A9:
    result = 0;
    if (v_stack_m1A8 != 0) {
        a1 = v_stack_m1B8;
        result = MiFlushFileOnlyDeleteChain(a1, a2, (unsigned int)((unsigned int)(v_stack_m230)), a4);
    }
    result = v_stack_m188;
    if (v_stack_m268 != v_stack_m188) {
        a2 = 0;
        a1 = v_stack_m268;
        result = ExFreePoolWithTag(a1, a2, (unsigned int)((unsigned int)(v_stack_m230)), a4);
    }
    if (v_stack_m288 != -1) {
        a1 = v_stack_m288 + v_stack_m288 * 2;
        a1 = (a1) << (4);
        result = result;
        a1 = (a1) + (result);
        result = MiReleaseFreshPage(a1, a2, (unsigned int)((unsigned int)(v_stack_m230)), a4);
    }
loc_003665F3:
    a1 = (v_stack_m58) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, (unsigned int)((unsigned int)(v_stack_m230)), a4);
    v_rsp = (v_rsp) + (680);
    return result;
loc_00366617:
    a2 = 0;
    result = MiSetActivePfnHeat(v_stack_m290, a2, (unsigned int)((unsigned int)(v_stack_m230)), a4);
    goto loc_00366293;
loc_00366626:
    result = MiCaptureDirtyBitToPfn(v_stack_m290, a2, (unsigned int)((unsigned int)(v_stack_m230)), a4);
    a1 = (*(unsigned __int64 *)(v_stack_m290 + 40)) >> (43);
    a1 = (unsigned int)((a1) & (0x3FFULL));
    goto loc_003662C5;
loc_0036664F:
    a1 = (v_stack_m288 + v_stack_m288 * 2) << (4);
    a1 = (a1) + (*(unsigned __int64 *)(v_rip + 11311692));
    result = MiReleaseFreshPage(a1, a2, (unsigned int)((unsigned int)(v_stack_m230)), a4);
    v_r15 = (v_stack_m288) | (-1);
    v_stack_p60 = v_r15;
loc_0036667D:
    a4 = 0;
    goto loc_00365FAC;
loc_00366685:
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1))) >> (20));
    a3 = (unsigned int)((a3) & (127));
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184)) + (0x400ULL);
    result = MiInitializePageColorBase(a1, 3, a3, v_stack_m1A0);
    a4 = 0;
    v_stack_m188 = v_xmm0;
    v_stack_m188 = 128;
    goto loc_00365E7C;
loc_003666CC:
    if (v_stack_m1F8 != v_stack_m220) goto loc_0036625B;
    if (((1) & ((unsigned __int8)(v_rdi))) != 0) goto loc_0036625B;
    if ((*(unsigned int *)(v_rip + 12977705)) != ((unsigned int)(v_stack_m220))) goto loc_00366F23;
loc_003666FD:
    result = MiCreateDecayPfn(a1, v_stack_m220, a3, a4);
    v_r14 = 0;
    v_stack_m1F8 = result;
    if ((*(unsigned int *)(v_rip + 12977680)) != 0) {
        a1 = 2;
        a2 = (unsigned __int8)(v_stack_m298);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, a3, a4);
    }
    goto loc_0036625E;
loc_00366729:
    if ((unsigned int)(v_stack_m298) != 0) goto loc_0036690F;
    a1 = (unsigned int)((0) & (0xFFFULL));
    result = (unsigned int)(((unsigned int)(0x1000ULL)) - ((unsigned int)(a1)));
    a1 = ((unsigned int)((unsigned int)(result))) >> (3);
    result = (a1) << (12);
    v_r15 = (unsigned int)((v_r15) + ((unsigned int)(a1)));
    v_stack_p68 = v_r15;
    v_stack_m230 = v_r14 + a1 * 8;
loc_00366762:
    goto loc_0036603C;
loc_0036676B:
    v_rdi = (unsigned int)((v_rdi) | (a3));
    goto loc_003661F3;
loc_00366773:
    result = MiPageHasRelocations(*(unsigned __int64 *)(v_stack_m220 + 32), (unsigned int)((unsigned int)(v_r14 + a1 * 8)), a3, a4);
    a2 = 0;
    if ((unsigned int)(result) == 0) goto loc_00366252;
    v_stack_p20 = v_stack_m1B8;
    result = MiSplitDirectMapPage(v_stack_m240, v_stack_m1A0, v_r15, v_stack_m268);
    if (result != -1) goto loc_00366B32;
    *(unsigned int *)(v_rip + 11300916) = 120;
    result = MiLockPageInline(v_stack_m290, v_stack_m1A0, v_r15, v_stack_m268);
    result = MiRemoveLockedPageCharge(v_stack_m290, v_stack_m1A0, v_r15, v_stack_m268);
    if ((unsigned int)(result) != 0) {
        a2 = v_r15;
        a1 = v_stack_m290;
        result = MiPfnReferenceCountIsZero(a1, a2, v_r15, v_stack_m268);
    }
    result = MiUnlockPage(v_stack_m290, (unsigned __int8)((unsigned __int8)(result)), v_r15, v_stack_m268);
    goto loc_00366587;
loc_003667FC:
    v_stack_m180 = *(unsigned __int64 *)(v_rip + 11306229);
    v_stack_m188 = 131;
    goto loc_00365E7C;
loc_00366817:
    if (v_r15 >= ((unsigned __int8)(result))) goto loc_00366D0C;
    v_stack_m230 = v_r15;
    a1 = (v_r15) - (v_stack_m268);
    a1 = (a1) >> (3);
    v_r15 = (unsigned int)((v_stack_p60) + ((unsigned int)(a1)));
    a1 = (a1) << (12);
    a2 = ((unsigned __int8)((unsigned __int8)(result))) + (a1);
    v_stack_p68 = v_r15;
    v_stack_m250 = a2;
    goto loc_00366038;
loc_00366849:
    result = (*(unsigned __int64 *)(v_stack_m290 + 40)) >> (60);
    result = (unsigned __int8)((result) & (7));
    if (((unsigned __int8)(result)) != 3) goto loc_0036610B;
loc_0036685B:
loc_00366865:
    goto loc_0036637B;
loc_00366879:
    if ((((unsigned __int8)(result)) & (8)) != 0) goto loc_00366B52;
    if ((((unsigned __int8)(result)) & (32)) != 0) goto loc_00366E02;
    v_stack_p40 = (unsigned int)(a2);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m240 + 32))) >> (1));
    result = (unsigned int)((result) & (31));
    v_stack_p38 = 0x4000000ULL;
    v_stack_p30 = v_stack_p68;
    v_stack_p28 = (unsigned int)(result);
    result = MiValidateImagePfn(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11311692) + a1 * 8), v_stack_m250, v_stack_m1D0, (unsigned int)((unsigned int)(v_r15)));
loc_003668C0:
    a2 = 0;
    goto loc_00366252;
loc_003668C7:
    a2 = 0;
    result = memset(v_stack_mF8, a2, 152, (unsigned int)((unsigned int)(v_r15)));
    a4 = 0;
    if (v_stack_p74 == 0) goto loc_00366C3D;
    goto loc_0036636B;
loc_003668FD:
    result = MiLockProtoPoolPage(v_r15, v_stack_p50, 152, a4);
    goto loc_003663AB;
loc_0036690F:
    a3 = 0;
    result = MmAccessFault(a3 + 2, v_r15, a3, a4);
    a4 = 0;
    goto loc_0036603C;
loc_0036692A:
    if (((0) & ((unsigned __int8)((unsigned int)(v_stack_p70)))) != 0) goto loc_0036704A;
    if (((*(unsigned int *)(v_stack_m1F0)) & (0x8000000ULL)) == 0) goto loc_00366006;
    if ((((unsigned __int8)((unsigned int)(v_stack_p70))) & (22)) != 0) goto loc_0036704E;
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_r15 + 40, a2, a3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = v_r15 + 40;
        a3 = 0;
        a2 = 0;
        a1 = v_r15 + 40;
        result = ExfAcquirePushLockSharedEx(a1, a2, a3, a4);
        a2 = 17;
    }
    a1 = 0;
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    if ((*(unsigned __int64 *)(v_stack_m240 + 24)) == 0) goto loc_00366DAA;
    result = MiGetSharedProtos(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11311692) + a1 * 8), (unsigned int)(v_stack_p78), v_stack_m240, a4);
    a1 = 0;
    if (result != 0) goto loc_00366E93;
    goto loc_00366DAD;
loc_003669D0:
    if ((unsigned int)(v_stack_m248) != 0) goto loc_00365E23;
    goto loc_00365E33;
loc_003669E2:
    if ((unsigned int)((unsigned int)(v_stack_p78)) == 0) goto loc_0036612A;
    *(unsigned int *)(v_rip + 11300356) = 122;
    goto loc_00366565;
loc_00366A03:
    if (((1) & ((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11311692) + a1 * 8) + 56))) != 0) goto loc_0036685B;
    a2 = (*(unsigned __int64 *)(result + 16)) >> (11);
    result = (*(unsigned __int64 *)(result + 16)) >> (3);
    if (condition_is_below) { result = (unsigned int)(a2); }
    if (((1) & ((unsigned __int8)(result))) != 0) goto loc_0036614E;
    goto loc_0036685B;
loc_00366A34:
    if ((*(unsigned __int8 *)(result + 35)) < ((unsigned __int8)(a4))) goto loc_00366172;
    result = MI_NODE_FROM_PFN(result, a2, *(unsigned __int64 *)(result + 16), a4);
    v_stack_p20 = v_stack_m25C;
    result = MiUseSlabAllocator(v_stack_m1E8, v_stack_m240, *(unsigned __int64 *)(result + 16), (unsigned int)((unsigned int)(result)));
    if ((unsigned int)(result) == 0) goto loc_00366172;
    if (v_stack_m25C > 4) goto loc_00366172;
    result = MiGetPfnSlabType(result, v_stack_m240, *(unsigned __int64 *)(result + 16), (unsigned int)((unsigned int)(result)));
    if (((unsigned int)(result)) == 9) goto loc_00366A9B;
    result = MiCheckSlabPage(result, (unsigned int)(v_stack_m25C), 4, (unsigned int)((unsigned int)(result)));
    if ((unsigned int)(result) != 0) goto loc_00366172;
loc_00366A9B:
    v_rdi = (unsigned int)(((unsigned int)((unsigned int)(v_stack_m268))) | (16));
    goto loc_00366175;
loc_00366AA3:
    result = MiWalkEntireImagePageNeedsProcessing(v_stack_m220, (unsigned int)((unsigned int)(v_stack_p68)), (unsigned int)((unsigned int)(v_stack_m248)), (unsigned int)((unsigned int)(result)));
    a2 = 0;
    if ((unsigned int)(result) == 0) goto loc_003661DB;
    if (v_stack_p74 == 0) goto loc_00366EEF;
    result = MiAddPageToHeatList(v_stack_m268, v_stack_p68, a2 + 3, (unsigned int)((unsigned int)(result)));
    v_rdi = (unsigned int)((v_rdi) | (64));
loc_00366ADE:
    a2 = 0;
    goto loc_003661DB;
loc_00366AE5:
    result = (((unsigned int)((unsigned int)((unsigned int)(result)))) != 0xC000009AULL) ? 1 : 0;
    result = (unsigned int)((result) + (113));
    *(unsigned int *)(v_rip + 11300093) = (unsigned int)(result);
    goto loc_00366583;
loc_00366B00:
    a1 = (*(unsigned __int64 *)(result + 16)) >> (11);
    a2 = (unsigned int)((*(unsigned __int64 *)(result + 16)) & (0x400ULL));
    result = (*(unsigned __int64 *)(result + 16)) >> (3);
    if (a2 != 0) { result = (unsigned int)(a1); }
    if (((1) & ((unsigned __int8)(result))) != 0) goto loc_003664A1;
    goto loc_003661A5;
loc_00366B32:
    v_rsi = (result + result * 2) << (4);
    v_rsi = (v_rsi) + (a1);
    goto loc_003668C0;
loc_00366B52:
    if (((*(unsigned __int64 *)(v_rip + 12975915)) & (0x2000ULL)) != 0) goto loc_00366D16;
loc_00366B63:
    result = MiUpdateImagePfnImportRelocations(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11311692) + a1 * 8), v_stack_m210, (unsigned int)((unsigned int)(v_stack_p68)), result);
    goto loc_00366242;
loc_00366B7A:
    if (condition_is_below) goto loc_00367001;
    result = MiGetPagingFileOffset(*(unsigned __int64 *)(v_stack_p68), v_stack_m210, (unsigned int)((unsigned int)(v_stack_p68)), result);
    if ((unsigned int)(result) == 0) goto loc_00367001;
    result = MiUnlockProtoPoolPage(v_stack_p58, v_stack_p50, (unsigned int)((unsigned int)(v_stack_p68)), result);
    result = 0;
    v_stack_p58 = 0;
    if (((v_stack_p70) & ((unsigned __int8)(result + 2))) == 0) goto loc_00366BDA;
    result = MiPageHasRelocations(*(unsigned __int64 *)(v_stack_m220 + 32), 0, result + 1, result + 2);
    a4 = 0;
    if ((unsigned int)(result) == 0) goto loc_00366375;
loc_00366BDA:
    a2 = (unsigned int)(((unsigned int)((unsigned int)(result))) << (12));
    result = MiGetEffectivePagePriorityThread(v_stack_m248, a2, result + 1, 0 + 2);
    if (((unsigned int)(result)) > 5) { result = 5; }
    if (v_stack_p68 != v_stack_m258) goto loc_00366E40;
loc_00366C03:
    v_stack_p28 = (unsigned int)((unsigned int)(v_stack_p78));
    v_stack_p20 = (unsigned int)(0 + 2);
    result = MiPrefetchControlArea(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11311692) + a1 * 8), a2, (unsigned int)(0x1000ULL), (unsigned int)((unsigned int)(result)));
    a4 = 0;
    if (sign_flag) {
        a3 = v_rip - 3499177;
        a2 = 0;
        a1 = 0;
        result = KeDelayExecutionThread(a1, a2, a3, a4);
        a4 = 0;
    }
    goto loc_0036603C;
loc_00366C3D:
    if (((2) & ((unsigned __int8)(v_r15 + 40))) != 0) goto loc_00366E57;
loc_00366C4A:
    a3 = 0;
    v_stack_p28 = v_stack_mF8;
    a2 = 0;
    a1 = 0;
    v_stack_p20 = 0;
    result = MiInitializePageFaultPacket(a1, a2, a3, a4);
    v_stack_m218 = (unsigned int)(a3 + 1);
    result = MiObtainProtoReference(v_stack_p58, (unsigned int)((unsigned int)(a3 + 1)), a3, a4);
    v_stack_p20 = v_stack_m218;
    result = MiWaitForCollidedFaultComplete(v_stack_mF8, 0, v_stack_p58, v_stack_p50);
    a4 = 0;
    v_stack_p58 = 0;
    goto loc_00366762;
loc_00366CB4:
    if (v_stack_p60 != -1) goto loc_00366268;
    result = MI_PAGE_TO_FULL_COLOR(v_stack_p68, 0, v_stack_p58, a4);
    a4 = 0;
    v_stack_p28 = (unsigned int)(v_stack_p68);
    result = MiGetSlabPage(v_stack_m1E8, (unsigned int)(v_stack_m25C), (unsigned int)((unsigned int)(result)), a4);
    v_stack_p60 = result;
    if (result != -1) goto loc_00366268;
    v_rdi = (unsigned int)((v_rdi) & (0xFFFFFFEFULL));
    goto loc_00366268;
loc_00366CFC:
    result = MiPfnReferenceCountIsZero(0, v_stack_p68, (unsigned int)((unsigned int)(result)), a4);
    goto loc_00366480;
loc_00366D0C:
    goto loc_00365FA2;
loc_00366D16:
    if (((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11311692) + a1 * 8) + 92)) & (0xC0000ULL)) == 0) goto loc_00366B63;
    a1 = (0) >> (60);
    a1 = (unsigned __int8)((a1) & (7));
    if (((unsigned __int8)(a1)) != 3) goto loc_00366B63;
    result = VslApplySecureImageFixups(*(unsigned __int64 *)(v_stack_m220 + 64), (unsigned int)((unsigned int)(v_stack_p68)), v_stack_p60, a4);
    a2 = 0;
    if (!sign_flag) goto loc_00366252;
    v_stack_p20 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11311692) + a1 * 8);
    result = KeBugCheckEx(26, (unsigned int)(0x51512ULL), (int)((unsigned int)(result)), v_stack_p60);
loc_00366D6F:
    result = (unsigned __int8)((*(unsigned __int8 *)(0 + 34)) & (7));
    if (((unsigned __int8)(result)) != 6) goto loc_003662D2;
    a3 = 0;
    result = MiTrimSharedPage(0, v_stack_p50, a3, v_stack_p60);
    result = MiLockPageInline(0, v_stack_p50, a3, v_stack_p60);
    if (condition_is_above_or_equal) goto loc_003662D2;
    v_rdi = (unsigned int)((v_rdi) & (0xFFFFFFEFULL));
    goto loc_003662D2;
loc_00366DAA:
loc_00366DAD:
    if (condition_is_not_equal) goto loc_00366FDB;
loc_00366DB8:
    result = KeAbPostRelease(v_r15 + 40, v_stack_p50, a3, v_stack_p60);
    if (condition_is_not_equal) goto loc_00366DE9;
    result = v_stack_p68 + 152;
    if ((*(unsigned __int64 *)(v_stack_p68 + 152)) != (v_stack_p68 + 152)) {
        result = KiCheckForKernelApcDelivery(v_r15 + 40, v_stack_p50, 1, v_stack_p60);
        a3 = 1;
    }
    goto loc_0036667D;
loc_00366DF3:
    *(unsigned int *)(v_rip + 11299323) = 121;
    goto loc_0036656A;
loc_00366E02:
    v_stack_p20 = a3;
    a2 = 0;
    result = MiApplyDebuggerPatches(v_r15 + 40, a2, (unsigned int)((unsigned int)(v_stack_p68)), v_stack_p60);
    goto loc_003668C0;
loc_00366E19:
    a3 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m188)))) >> (1));
    a2 = (unsigned int)(((unsigned int)(v_stack_m188)) & (1));
    a3 = (unsigned int)((a3) & (3));
    result = MiInitializePageHeatList(result, a2, a3, (unsigned int)((unsigned int)(v_r15 + 40)));
    goto loc_00365FC3;
loc_00366E40:
    v_stack_m258 = v_stack_p68;
    a3 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11311692) + a1 * 8) + 128) - (v_stack_p68);
    a3 = (a3) >> (3);
    a3 = (a3) << (12);
    goto loc_00366C03;
loc_00366E57:
    if ((((unsigned __int8)(result)) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11311692) + a1 * 8) + 56))))) != 0) goto loc_00366C4A;
    result = MiDeleteTransitionPte(v_stack_p68, 0, 17, (unsigned int)((unsigned int)(v_r15 + 40)));
    a4 = 0;
    goto loc_00366375;
loc_00366E86:
    result = MiIssuePageHeatList(v_stack_p68, 0, 17, a4);
    goto loc_003665A9;
loc_00366E93:
    if (condition_is_not_equal) goto loc_00366FE8;
loc_00366EAB:
    result = KeAbPostRelease(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11311692) + a1 * 8) + 128, 0, 17, a4);
    if (condition_is_not_equal) goto loc_00366ED6;
    result = v_stack_p68 + 152;
    if ((*(unsigned __int64 *)(v_stack_p68 + 152)) != (v_stack_p68 + 152)) {
        result = KiCheckForKernelApcDelivery(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11311692) + a1 * 8) + 128, 0, 17, 1);
    }
    v_rdi = (unsigned int)((v_rdi) | (8));
    v_stack_m230 = *(unsigned __int64 *)(v_stack_p58 + 72);
    goto loc_00366006;
loc_00366EEF:
    a3 = (unsigned int)(((unsigned int)(v_stack_p70)) | (16));
    result = MiWalkEntireImage(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11311692) + a1 * 8), v_stack_m210, a3, (unsigned int)(v_stack_p78));
    goto loc_00366ADE;
loc_00366F12:
    v_r12 = (int)((unsigned int)(result));
    if (((unsigned int)((int)((unsigned int)(result)))) == 1) { v_r12 = (unsigned int)(v_stack_m210); }
    goto loc_00366252;
loc_00366F23:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(v_stack_m240), 1, a3, (unsigned int)(v_stack_p78));
    goto loc_003666FD;
loc_00366F31:
    result = (unsigned __int8)((*(unsigned __int8 *)(v_stack_p58 + 34)) & (7));
    result = (unsigned __int8)((result) - (2));
    if (((unsigned __int8)(result)) > ((unsigned __int8)(*(unsigned __int64 *)(v_stack_p58 + 72)))) goto loc_00366304;
    if ((unsigned __int16)((unsigned int)(*(unsigned int *)(v_stack_p58 + 32))) != 0) goto loc_00366304;
    if ((*(unsigned __int8 *)(v_stack_p58 + 35)) < ((unsigned __int8)((unsigned __int8)(v_stack_m240)))) goto loc_00366304;
    v_r10 = (v_stack_p60 + v_stack_p60 * 2) << (4);
    v_r10 = (v_r10) + ((unsigned int)(*(unsigned int *)(v_stack_p58 + 32)));
    result = MiGetPfnSlabType(v_r10, 1, a3, (unsigned int)(v_stack_p78));
    if (((unsigned int)(result)) == 9) goto loc_00366309;
    result = MiGetPfnSlabType(v_stack_p58, 1, a3, (unsigned int)(v_stack_p78));
    a4 = 0;
    result = MiReplaceTransitionPage(v_stack_p58, v_r10, (unsigned int)((unsigned int)(result)), a4);
    a1 = (unsigned int)(((unsigned int)((unsigned int)(result))) << (4));
    a1 = (unsigned int)((a1) ^ ((unsigned int)(v_rdi)));
    a1 = (unsigned int)((a1) & (16));
    v_rdi = (unsigned int)((v_rdi) ^ ((unsigned int)(a1)));
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_p58 + 72))) & ((unsigned __int8)(result))) == 0) goto loc_00366309;
    v_r15 = (v_stack_p60) | (-1);
    *(unsigned __int64 *)(v_stack_p58 + 16) = *(unsigned __int64 *)(v_rip - 3499833);
    v_stack_p60 = v_r15;
    result = MiSetOriginalPtePfnFromFreeList(v_stack_p58 + 16, v_r10, (unsigned int)((unsigned int)(result)), a4);
    result = MiReleaseFreshPageLocked(v_stack_p58, v_r10, (unsigned int)((unsigned int)(result)), a4);
    goto loc_00366309;
loc_00366FDB:
    result = ExfReleasePushLockShared(v_stack_m240, v_r10, (unsigned int)((unsigned int)(result)), a4);
    goto loc_00366DB8;
loc_00366FE8:
    result = ExfReleasePushLockShared(v_stack_m240, v_r10, (unsigned int)((unsigned int)(result)), a4);
    goto loc_00366EAB;
loc_00366FF5:
    goto loc_00365FD0;
loc_00367001:
    goto loc_00366375;
loc_0036700B:
    a2 = ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11311692) + a1 * 8) + 128)) & (16)) == 0) ? 1 : 0;
    result = (((2) & ((unsigned __int8)(v_rdi))) == 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a2))) != 0) goto loc_0036685B;
    goto loc_00366119;
loc_00367029:
    result = (*(unsigned __int64 *)(v_stack_p58 + 24)) & (v_stack_m240);
    a4 = 0;
    *(unsigned __int64 *)(v_stack_p58 + 24) = result;
    goto loc_0036615F;
loc_0036704A:
loc_0036704E:
    goto loc_00365FAC;
}
```

## 5. (Beta) C Style

```c
int64_t MiWalkEntireImage(void *Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m180;
    uint32_t v_stack_m184;
    uint64_t v_stack_m188;
    uint64_t v_stack_m1A0;
    uint64_t v_stack_m1A8;
    uint64_t v_stack_m1B8;
    uint64_t v_stack_m1C0;
    uint64_t v_stack_m1C8;
    uint64_t v_stack_m1D0;
    uint64_t v_stack_m1D8;
    uint64_t v_stack_m1E8;
    uint64_t v_stack_m1F0;
    uint64_t v_stack_m1F8;
    uint32_t v_stack_m200;
    uint64_t v_stack_m208;
    uint64_t v_stack_m210;
    uint32_t v_stack_m214;
    uint32_t v_stack_m218;
    uint64_t v_stack_m220;
    uint64_t v_stack_m228;
    uint64_t v_stack_m230;
    uint64_t v_stack_m238;
    uint64_t v_stack_m240;
    uint64_t v_stack_m248;
    uint64_t v_stack_m250;
    uint64_t v_stack_m258;
    uint32_t v_stack_m25C;
    uint32_t v_stack_m260;
    uint64_t v_stack_m268;
    uint32_t v_stack_m270;
    uint32_t v_stack_m274;
    uint32_t v_stack_m278;
    uint64_t v_stack_m280;
    uint64_t v_stack_m288;
    uint64_t v_stack_m290;
    uint8_t v_stack_m298;
    uint32_t v_stack_m2B8;
    uint64_t v_stack_m2C8;
    uint64_t v_stack_m58;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p20;
    uint32_t v_stack_p28;
    uint64_t v_stack_p30;
    uint32_t v_stack_p38;
    uint32_t v_stack_p40;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_p60;
    uint64_t v_stack_p68;
    uint32_t v_stack_p70;
    uint32_t v_stack_p74;
    uint32_t v_stack_p78;

    local_rsp = (local_rsp) - (680);
    result = (*(uint64_t *)(v_rip + 0xAA49AD)) ^ (local_rsp);
    v_stack_m58 = result;
    v_stack_m278 = Arg3;
    v_stack_m210 = Arg2;
    v_stack_m1C8 = Arg1;
    result = 0;
    v_stack_m218 = 0;
    Arg2 = 0;
    v_stack_m270 = Arg4;
    v_stack_m1A0 = v_xmm0;
    result = memset(v_stack_m188, Arg2, 144, Arg4);
    Arg4 = 0;
    Arg1 = (uint32_t)((*(uint16_t *)(arg1 + 0x3C)) & (0x3FFULL));
    v_stack_m228 = *(uint64_t *)(arg1);
    Arg2 = (*(uint64_t *)(arg1 + 0x60)) & (-8);
    local_r14 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg3)))) & (4));
    v_stack_m220 = Arg2;
    v_stack_m260 = (uint32_t)(local_r14);
    v_stack_m1E8 = *(uint64_t *)(*(uint64_t *)(v_rip + 0xACA28E) + arg1 * 8);
    result = (uint8_t)((*(uint8_t *)(arg1 + 0x3E)) & (12));
    if (((uint8_t)(result)) == 4) goto loc_003669D0;
loc_00365E23:
    v_stack_m1F0 = Arg1 + 56;
    local_rdi = 0;
    if (((*(uint32_t *)(arg1 + 0x38)) & (0x800ULL)) != 0) {
        v_stack_m1F0 = Arg1 + 56;
        local_rdi = (uint32_t)(Arg4 + 2);
    }
    v_stack_m248 = *(uint64_t *)(gs_base + (0 + 0x188));
    result = 0;
    v_stack_m1A8 = 0;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg3)))) & (16));
    v_stack_m208 = 0;
    v_stack_m274 = (uint32_t)(result);
    v_stack_m1B8 = v_xmm0;
    v_stack_m268 = v_stack_m188;
    if (condition_is_not_equal) goto loc_003667FC;
    if ((uint32_t)(local_r14) != 0) goto loc_00366685;
loc_00365E7C:
    local_r15 = (local_r15) | (-1);
    v_stack_m240 = Arg1 + 128;
    v_stack_m25C = 0;
    v_stack_m1D0 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8);
    v_stack_m1D8 = *(uint64_t *)(arg1 + 0x80 + 0x8);
    v_stack_m298 = 17;
    v_stack_m290 = 0;
    v_stack_m1F8 = 0;
    v_stack_m288 = local_r15;
    if (((*(uint64_t *)(v_rip + 0xC60BE9)) & (0x2000ULL)) == 0) goto loc_00365EFB;
    if (((*(uint32_t *)(arg1 + 0x5C)) & (0xC0000ULL)) == 0) goto loc_00365EFB;
    if ((*(uint64_t *)(Arg2 + 0x40)) != 0) goto loc_00365EFB;
    result = MiGetSectionStrongImageReference(Arg2, Arg2, Arg4 + 2, Arg4);
    Arg4 = 0;
    if (sign_flag) goto loc_003665F3;
loc_00365EFB:
    v_stack_m200 = 0;
    if ((uint32_t)(local_r14) != 0) {
        Arg1 = v_stack_m210;
        Arg2 = 0;
        result = MiGetNextDirectFixupProto(Arg1, Arg2, Arg4 + 2, Arg4);
        v_stack_m208 = result;
    }
    if (v_stack_m184 == -1) goto loc_00365FD0;
    local_rbx = 511;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m228 + 0x8)))) < 511) { local_rbx = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m228 + 0x8))); }
    Arg1 = (uint32_t)(((uint32_t)(v_stack_m188)) >> (3));
    if (((uint32_t)(local_rbx)) <= ((uint32_t)(Arg1))) goto loc_00366FF5;
    result = MiAllocatePool(1 + 65, local_rbx * 8 + 16, (uint32_t)(0x6C68694DULL), Arg4);
    Arg4 = 0;
    v_stack_m268 = result;
    if (result != 0) goto loc_00366E19;
    v_stack_m268 = v_stack_m188;
    goto loc_00365FC6;
loc_00365F7A:
    result = v_stack_m188;
    if (0 != 0) {
        Arg2 = v_stack_m298;
        Arg1 = 0;
        result = MiUnlockProtoPoolPage(Arg1, Arg2, (uint32_t)(0x6C68694DULL), Arg4);
        Arg4 = 0;
        v_stack_m290 = 0;
    }
    if (v_stack_m288 != -1) goto loc_0036664F;
loc_00365FA2:
loc_00365FAC:
    v_stack_m240 = v_stack_m1C0;
loc_00365FC3:
    Arg4 = 0;
loc_00365FC6:
loc_00365FD0:
    if (v_stack_m1C0 == 0) goto loc_00366583;
    local_r15 = (*(uint64_t *)(v_stack_m1C0 + 0x8)) - (v_stack_m1D8);
    local_r15 = (local_r15) >> (3);
    v_stack_m1C0 = *(uint64_t *)(v_stack_m1C0 + 0x10);
    v_stack_m230 = *(uint64_t *)(v_stack_m1C0 + 0x8);
    v_stack_m280 = local_r15;
    if (condition_is_below) goto loc_0036692A;
loc_00366006:
    result = MiStartingOffset(v_stack_m1C0, *(uint64_t *)(v_stack_m1C0 + 0x8), (uint32_t)(v_stack_m270), Arg4);
    Arg4 = 0;
    v_stack_m250 = result;
    v_stack_m238 = *(uint64_t *)(v_stack_m1C0 + 0x8) + (uint32_t)(*(uint32_t *)(v_stack_m1C0 + 0x2C)) * 8;
    if (v_stack_m208 != 0) goto loc_00366817;
loc_00366038:
    v_stack_m258 = 0;
loc_0036603C:
loc_00366041:
    if ((*(uint64_t *)(v_stack_m1C0 + 0x8)) >= (*(uint64_t *)(v_stack_m1C0 + 0x8) + (uint32_t)(*(uint32_t *)(v_stack_m1C0 + 0x2C)) * 8)) goto loc_00365F7A;
    if (((*(uint64_t *)(v_stack_m1C0 + 0x8)) & (0xFFFULL)) == 0) goto loc_00366385;
    if (v_stack_m290 == 0) goto loc_00366385;
loc_00366060:
    Arg2 = 0;
    result = MiLockLeafPage(*(uint64_t *)(v_stack_m1C0 + 0x8), Arg2, v_stack_m208, Arg4);
    Arg4 = 0;
    if (result != 0) goto loc_003660BE;
    if (v_stack_m260 != 0) goto loc_00366DF3;
    if ((((uint8_t)(result + 2)) & ((uint8_t)(local_rdi))) != 0) goto loc_00366B7A;
loc_00366090:
loc_00366096:
    local_r14 = (*(uint64_t *)(v_stack_m1C0 + 0x8)) + (8);
    local_r15 = (uint32_t)((local_r15) + (1));
    v_stack_m230 = local_r14;
    v_stack_m280 = local_r15;
    goto loc_00366041;
loc_003660BE:
    if (((1) & ((uint8_t)(*(uint64_t *)(local_r14)))) != 0) goto loc_003660ED;
    if (*(uint64_t *)(v_rip + 0xAC7BAA) == 0) goto loc_003660ED;
    if ((((uint8_t)(*(uint64_t *)(local_r14))) & (16)) != 0) goto loc_0036652A;
    local_r15 = ~(*(uint64_t *)(v_rip + 0xAC7BAA));
    local_r15 = (local_r15) & (*(uint64_t *)(local_r14));
loc_003660ED:
    local_r15 = (local_r15) >> (12);
    local_r15 = (local_r15) & (*(uint64_t *)(v_rip + 0xAC7BAA));
    if (((1) & ((uint8_t)((uint32_t)(v_stack_m278)))) != 0) goto loc_00366849;
loc_0036610B:
    if (condition_is_above_or_equal) goto loc_0036700B;
loc_00366119:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m290 + 0x20))) >> (24));
    if ((((uint8_t)(result)) & (64)) != 0) goto loc_003669E2;
loc_0036612A:
    if (((*(uint8_t *)(v_stack_m290 + 0x23)) & (16)) != 0) goto loc_00366549;
    if (((1) & ((uint8_t)(*(uint64_t *)(local_r14)))) != 0) goto loc_00366143;
    if (((*(uint8_t *)(v_stack_m290 + 0x22)) & (32)) != 0) goto loc_003668C7;
loc_00366143:
    if (v_stack_m274 != 0) goto loc_00366A03;
loc_0036614E:
    v_stack_m214 = 8;
    if (((1) & ((uint8_t)(*(uint64_t *)(local_r14)))) == 0) goto loc_003663C8;
loc_0036615F:
    result = (uint8_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m278)))) & (17));
    if (((uint8_t)(result)) == 1) goto loc_00366A34;
loc_00366172:
    local_rdi = (uint32_t)((local_rdi) & (0xFFFFFFEFULL));
loc_00366175:
    result = MiAddLockedPageCharge(v_stack_m290, 1, v_stack_m208, Arg4);
    Arg3 = 0;
    if (v_stack_m274 != 0) goto loc_0036649E;
    if (sign_flag) goto loc_003661A5;
    if (((*(uint32_t *)(v_rip + 0xC60919)) & (0x200000ULL)) != 0) goto loc_00366B00;
loc_003661A5:
    local_rdi = (uint32_t)((local_rdi) & (0xFFFFFFDFULL));
loc_003661A8:
    result = MiUnlockProtoPoolPage(v_stack_m290, v_stack_m298, Arg3, Arg4);
    Arg2 = 0;
    v_stack_m290 = 0;
    if ((((uint8_t)(local_rdi)) & (32)) != 0) goto loc_00366AA3;
loc_003661DB:
    if (condition_is_below) goto loc_0036676B;
    local_rdi = (uint32_t)((local_rdi) & (0xFFFFFFFEULL));
loc_003661F3:
    if (v_stack_m274 != 0) goto loc_00366496;
    if (v_stack_m260 != 0) goto loc_00366773;
    if ((((uint8_t)((uint32_t)(v_stack_m278))) & (2)) == 0) goto loc_00366879;
    if (((*(uint64_t *)(v_rip + 0xC6086B)) & (0x2000ULL)) != 0) goto loc_003664A9;
loc_00366223:
    v_stack_m2B8 = 65;
    v_stack_m2C8 = 0;
    result = MiRelocateImagePfn(Arg1, v_stack_m210, (uint32_t)((uint32_t)(v_stack_m280)), local_r15);
loc_00366242:
    Arg2 = 0;
    if ((uint32_t)(result) != 0) goto loc_00366F12;
    local_rdi = (uint32_t)((local_rdi) | (4));
loc_00366252:
    if (8 != 8) goto loc_003666CC;
loc_0036625B:
    local_r14 = 0;
loc_0036625E:
    if ((((uint8_t)(local_rdi)) & (16)) != 0) goto loc_00366CB4;
loc_00366268:
    result = MiLockPageInline(v_stack_m290, Arg2, (uint32_t)((uint32_t)(v_stack_m280)), local_r15);
    v_stack_m298 = (uint8_t)(result);
    if (condition_is_below) goto loc_00366502;
    if ((((uint8_t)(local_rdi)) & (64)) != 0) goto loc_00366617;
loc_00366293:
    local_r14 = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) & (0xFFFFFFEFULL));
    if (!sign_flag) { local_r14 = (uint32_t)(local_rdi); }
    if ((((uint8_t)((uint32_t)(v_stack_m278))) & (8)) != 0) goto loc_003662B6;
    result = (uint8_t)(((uint32_t)(v_stack_m278)) & (18));
    if (((uint8_t)(result)) != 2) goto loc_003662C5;
loc_003662B6:
    if (((uint8_t)(result)) >= 2) goto loc_00366626;
loc_003662C5:
    if ((((uint8_t)(local_r14)) & (16)) != 0) goto loc_00366D6F;
loc_003662D2:
    result = MiRemoveLockedPageCharge(v_stack_m290, Arg2, (uint32_t)((uint32_t)(v_stack_m280)), local_r15);
    Arg1 = 0;
    if ((uint32_t)(result) == 0) goto loc_003662FA;
    if ((((uint8_t)(Arg1 + 1)) & ((uint8_t)((uint32_t)((uint32_t)(local_r14))))) == 0) goto loc_0036643B;
loc_003662ED:
    result = MiPfnReferenceCountIsZero(v_stack_m290, local_r15, (uint32_t)((uint32_t)(v_stack_m280)), local_r15);
    Arg1 = 0;
loc_003662FA:
    if ((((uint8_t)((uint32_t)((uint32_t)(local_r14)))) & (16)) != 0) goto loc_00366F31;
loc_00366304:
loc_00366309:
    if (v_stack_m298 != 17) {
    }
    Arg4 = 0;
    if (0 != 0) goto loc_00366533;
loc_0036632B:
    if (((uint8_t)(v_stack_m298)) == 17) goto loc_0036635A;
    if ((*(uint32_t *)(v_rip + 0xC609E1)) != 0) {
        Arg1 = v_cr8;
        result = KiLowerIrqlProcessIrqlFlags(Arg1, v_stack_m298, (uint32_t)((uint32_t)(v_stack_m280)), Arg4);
        Arg4 = 0;
    }
    v_stack_m298 = 17;
loc_0036635A:
    if (sign_flag) goto loc_00366AE5;
loc_0036636B:
loc_00366375:
loc_0036637B:
    goto loc_00366096;
loc_00366385:
    if (v_stack_m290 != 0) goto loc_00366514;
loc_0036638E:
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r14))))) & (2));
    if (condition_is_not_equal) goto loc_003668FD;
    Arg3 = 0;
    result = MiCheckProtoPtePageState(v_stack_m1C8, v_stack_m230, Arg3, v_stack_m298);
loc_003663AB:
    Arg4 = 0;
    v_stack_m290 = result;
    if (result == 0) goto loc_00366729;
    goto loc_00366060;
loc_003663C8:
    result = MiGetPfnSlabType(result, v_stack_m230, Arg3, Arg4);
    if (((uint32_t)(result)) != 9) goto loc_003663EB;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x20))) >> (24));
    local_rbx = v_stack_m238;
    if ((((uint8_t)(v_stack_m238)) & ((uint8_t)(result))) != 0) {
        local_rbx = *(uint32_t *)(result + 0x20);
        local_rbx = (uint32_t)((local_rbx) >> (24));
        local_rbx = (uint32_t)((local_rbx) & (7));
        v_stack_m214 = (uint32_t)(local_rbx);
    }
    Arg2 = 0;
    result = MiUnlinkPageFromListEx(result, Arg2, Arg3, Arg4);
    if ((((uint8_t)(result)) & (3)) == 0) goto loc_00367029;
    Arg2 = 0;
    result = MiDiscardTransitionPteEx(result, Arg2, Arg3, Arg4);
    if (((2) & ((uint8_t)((uint32_t)((uint32_t)(local_r14))))) != 0) goto loc_00366041;
    goto loc_00366090;
loc_0036643B:
    if (v_stack_m214 == 8) goto loc_003662ED;
    if (((*(uint8_t *)(v_stack_m290 + 0x22)) & (16)) != 0) goto loc_003662ED;
    if (condition_is_below) goto loc_003662ED;
    if ((((uint8_t)((uint32_t)((uint32_t)(local_r14)))) & (16)) != 0) goto loc_003662ED;
    if (v_stack_m1F8 == 0) goto loc_00366CFC;
    result = MiInsertProtectedStandbyPage(v_stack_m1F8, v_stack_m290, Arg3, 2 - 2);
loc_00366480:
    result = MiUnlockPage(v_stack_m290, v_stack_m298, Arg3, 2 - 2);
    v_stack_m298 = 17;
    goto loc_00366304;
loc_00366496:
    goto loc_00366252;
loc_0036649E:
    local_rdi = (uint32_t)(((uint32_t)((uint32_t)(local_r14))) & (0xFFFFFFBFULL));
loc_003664A1:
    local_rdi = (uint32_t)((local_rdi) | (32));
    goto loc_003661A8;
loc_003664A9:
    if (((*(uint32_t *)(v_stack_m1C8 + 0x5C)) & (0xC0000ULL)) == 0) goto loc_00366223;
    Arg1 = (v_stack_m290) >> (60);
    Arg1 = (uint8_t)((Arg1) & (7));
    if (((uint8_t)(Arg1)) != 3) goto loc_00366223;
    result = VslApplySecureImageFixups(*(uint64_t *)(v_stack_m220 + 0x40), (uint32_t)((uint32_t)(v_stack_m230)), v_stack_m280, 2 - 2);
    Arg2 = 0;
    if (!sign_flag) goto loc_00366252;
    v_stack_m2C8 = v_stack_m1C8;
    result = KeBugCheckEx(26, (uint32_t)(0x51511ULL), (int32_t)((uint32_t)(result)), v_stack_m280);
loc_00366502:
    if ((((uint8_t)(local_rdi)) & (16)) == 0) goto loc_00366293;
    local_rdi = (uint32_t)((local_rdi) & (0xFFFFFFEFULL));
    goto loc_00366293;
loc_00366514:
    result = MiUnlockProtoPoolPage(v_stack_m290, v_stack_m298, (int32_t)((uint32_t)(result)), v_stack_m280);
    goto loc_0036638E;
loc_0036652A:
    local_r15 = (v_stack_m280) & (-17);
    goto loc_003660ED;
loc_00366533:
    result = MiReleasePageFileInfo(v_stack_m1C8, v_stack_m238, (uint32_t)((uint32_t)(v_stack_m230)), v_stack_m280);
    Arg4 = 0;
    goto loc_0036632B;
loc_00366549:
    if ((uint32_t)(v_stack_m238) == 0) goto loc_00366865;
    *(uint32_t *)(v_rip + 0xAC7293) = 123;
loc_00366565:
loc_0036656A:
    result = MiUnlockProtoPoolPage(v_stack_m290, v_stack_m298, (uint32_t)((uint32_t)(v_stack_m230)), Arg4);
loc_00366583:
loc_00366587:
    result = v_stack_m1F8;
    if (v_stack_m1F8 != 0) {
        Arg2 = 0;
        Arg1 = v_stack_m1F8;
        result = MiDecayPfnFullyInitialized(Arg1, Arg2, (uint32_t)((uint32_t)(v_stack_m230)), Arg4);
    }
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m268 + 0x4))) - 1);
    if (((uint32_t)(result)) <= -3) goto loc_00366E86;
loc_003665A9:
    result = 0;
    if (v_stack_m1A8 != 0) {
        Arg1 = v_stack_m1B8;
        result = MiFlushFileOnlyDeleteChain(Arg1, Arg2, (uint32_t)((uint32_t)(v_stack_m230)), Arg4);
    }
    result = v_stack_m188;
    if (v_stack_m268 != v_stack_m188) {
        Arg2 = 0;
        Arg1 = v_stack_m268;
        result = ExFreePoolWithTag(Arg1, Arg2, (uint32_t)((uint32_t)(v_stack_m230)), Arg4);
    }
    if (v_stack_m288 != -1) {
        Arg1 = v_stack_m288 + v_stack_m288 * 2;
        Arg1 = (Arg1) << (4);
        result = result;
        Arg1 = (Arg1) + (result);
        result = MiReleaseFreshPage(Arg1, Arg2, (uint32_t)((uint32_t)(v_stack_m230)), Arg4);
    }
loc_003665F3:
    Arg1 = (v_stack_m58) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, (uint32_t)((uint32_t)(v_stack_m230)), Arg4);
    local_rsp = (local_rsp) + (680);
    return result;
loc_00366617:
    Arg2 = 0;
    result = MiSetActivePfnHeat(v_stack_m290, Arg2, (uint32_t)((uint32_t)(v_stack_m230)), Arg4);
    goto loc_00366293;
loc_00366626:
    result = MiCaptureDirtyBitToPfn(v_stack_m290, Arg2, (uint32_t)((uint32_t)(v_stack_m230)), Arg4);
    Arg1 = (*(uint64_t *)(v_stack_m290 + 0x28)) >> (43);
    Arg1 = (uint32_t)((Arg1) & (0x3FFULL));
    goto loc_003662C5;
loc_0036664F:
    Arg1 = (v_stack_m288 + v_stack_m288 * 2) << (4);
    Arg1 = (Arg1) + (*(uint64_t *)(v_rip + 0xAC9A4C));
    result = MiReleaseFreshPage(Arg1, Arg2, (uint32_t)((uint32_t)(v_stack_m230)), Arg4);
    local_r15 = (v_stack_m288) | (-1);
    v_stack_p60 = local_r15;
loc_0036667D:
    Arg4 = 0;
    goto loc_00365FAC;
loc_00366685:
    Arg3 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1))) >> (20));
    Arg3 = (uint32_t)((Arg3) & (127));
    Arg1 = (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8)) + (0x400ULL);
    result = MiInitializePageColorBase(Arg1, 3, Arg3, v_stack_m1A0);
    Arg4 = 0;
    v_stack_m188 = v_xmm0;
    v_stack_m188 = 128;
    goto loc_00365E7C;
loc_003666CC:
    if (v_stack_m1F8 != v_stack_m220) goto loc_0036625B;
    if (((1) & ((uint8_t)(local_rdi))) != 0) goto loc_0036625B;
    if ((*(uint32_t *)(v_rip + 0xC60629)) != ((uint32_t)(v_stack_m220))) goto loc_00366F23;
loc_003666FD:
    result = MiCreateDecayPfn(Arg1, v_stack_m220, Arg3, Arg4);
    local_r14 = 0;
    v_stack_m1F8 = result;
    if ((*(uint32_t *)(v_rip + 0xC60610)) != 0) {
        Arg1 = 2;
        Arg2 = (uint8_t)(v_stack_m298);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, Arg3, Arg4);
    }
    goto loc_0036625E;
loc_00366729:
    if ((uint32_t)(v_stack_m298) != 0) goto loc_0036690F;
    Arg1 = (uint32_t)((0) & (0xFFFULL));
    result = (uint32_t)(((uint32_t)(0x1000ULL)) - ((uint32_t)(Arg1)));
    Arg1 = ((uint32_t)((uint32_t)(result))) >> (3);
    result = (Arg1) << (12);
    local_r15 = (uint32_t)((local_r15) + ((uint32_t)(Arg1)));
    v_stack_p68 = local_r15;
    v_stack_m230 = local_r14 + Arg1 * 8;
loc_00366762:
    goto loc_0036603C;
loc_0036676B:
    local_rdi = (uint32_t)((local_rdi) | (Arg3));
    goto loc_003661F3;
loc_00366773:
    result = MiPageHasRelocations(*(uint64_t *)(v_stack_m220 + 0x20), (uint32_t)((uint32_t)(local_r14 + Arg1 * 8)), Arg3, Arg4);
    Arg2 = 0;
    if ((uint32_t)(result) == 0) goto loc_00366252;
    v_stack_p20 = v_stack_m1B8;
    result = MiSplitDirectMapPage(v_stack_m240, v_stack_m1A0, local_r15, v_stack_m268);
    if (result != -1) goto loc_00366B32;
    *(uint32_t *)(v_rip + 0xAC7034) = 120;
    result = MiLockPageInline(v_stack_m290, v_stack_m1A0, local_r15, v_stack_m268);
    result = MiRemoveLockedPageCharge(v_stack_m290, v_stack_m1A0, local_r15, v_stack_m268);
    if ((uint32_t)(result) != 0) {
        Arg2 = local_r15;
        Arg1 = v_stack_m290;
        result = MiPfnReferenceCountIsZero(Arg1, Arg2, local_r15, v_stack_m268);
    }
    result = MiUnlockPage(v_stack_m290, (uint8_t)((uint8_t)(result)), local_r15, v_stack_m268);
    goto loc_00366587;
loc_003667FC:
    v_stack_m180 = *(uint64_t *)(v_rip + 0xAC84F5);
    v_stack_m188 = 131;
    goto loc_00365E7C;
loc_00366817:
    if (local_r15 >= ((uint8_t)(result))) goto loc_00366D0C;
    v_stack_m230 = local_r15;
    Arg1 = (local_r15) - (v_stack_m268);
    Arg1 = (Arg1) >> (3);
    local_r15 = (uint32_t)((v_stack_p60) + ((uint32_t)(Arg1)));
    Arg1 = (Arg1) << (12);
    Arg2 = ((uint8_t)((uint8_t)(result))) + (Arg1);
    v_stack_p68 = local_r15;
    v_stack_m250 = Arg2;
    goto loc_00366038;
loc_00366849:
    result = (*(uint64_t *)(v_stack_m290 + 0x28)) >> (60);
    result = (uint8_t)((result) & (7));
    if (((uint8_t)(result)) != 3) goto loc_0036610B;
loc_0036685B:
loc_00366865:
    goto loc_0036637B;
loc_00366879:
    if ((((uint8_t)(result)) & (8)) != 0) goto loc_00366B52;
    if ((((uint8_t)(result)) & (32)) != 0) goto loc_00366E02;
    v_stack_p40 = (uint32_t)(Arg2);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m240 + 0x20))) >> (1));
    result = (uint32_t)((result) & (31));
    v_stack_p38 = 0x4000000ULL;
    v_stack_p30 = v_stack_p68;
    v_stack_p28 = (uint32_t)(result);
    result = MiValidateImagePfn(*(uint64_t *)(*(uint64_t *)(v_rip + 0xAC9A4C) + arg1 * 8), v_stack_m250, v_stack_m1D0, (uint32_t)((uint32_t)(local_r15)));
loc_003668C0:
    Arg2 = 0;
    goto loc_00366252;
loc_003668C7:
    Arg2 = 0;
    result = memset(v_stack_mF8, Arg2, 152, (uint32_t)((uint32_t)(local_r15)));
    Arg4 = 0;
    if (v_stack_p74 == 0) goto loc_00366C3D;
    goto loc_0036636B;
loc_003668FD:
    result = MiLockProtoPoolPage(local_r15, v_stack_p50, 152, Arg4);
    goto loc_003663AB;
loc_0036690F:
    Arg3 = 0;
    result = MmAccessFault(Arg3 + 2, local_r15, Arg3, Arg4);
    Arg4 = 0;
    goto loc_0036603C;
loc_0036692A:
    if (((0) & ((uint8_t)((uint32_t)(v_stack_p70)))) != 0) goto loc_0036704A;
    if (((*(uint32_t *)(v_stack_m1F0)) & (0x8000000ULL)) == 0) goto loc_00366006;
    if ((((uint8_t)((uint32_t)(v_stack_p70))) & (22)) != 0) goto loc_0036704E;
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(local_r15 + 40, Arg2, Arg3, Arg4);
    result = 0;
    if (!(condition_is_equal)) {
        Arg4 = local_r15 + 40;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = local_r15 + 40;
        result = ExfAcquirePushLockSharedEx(Arg1, Arg2, Arg3, Arg4);
        Arg2 = 17;
    }
    Arg1 = 0;
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    if ((*(uint64_t *)(v_stack_m240 + 0x18)) == 0) goto loc_00366DAA;
    result = MiGetSharedProtos(*(uint64_t *)(*(uint64_t *)(v_rip + 0xAC9A4C) + arg1 * 8), (uint32_t)(v_stack_p78), v_stack_m240, Arg4);
    Arg1 = 0;
    if (result != 0) goto loc_00366E93;
    goto loc_00366DAD;
loc_003669D0:
    if ((uint32_t)(v_stack_m248) != 0) goto loc_00365E23;
    goto loc_00365E33;
loc_003669E2:
    if ((uint32_t)((uint32_t)(v_stack_p78)) == 0) goto loc_0036612A;
    *(uint32_t *)(v_rip + 0xAC6E04) = 122;
    goto loc_00366565;
loc_00366A03:
    if (((1) & ((uint8_t)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xAC9A4C) + arg1 * 8) + 56))) != 0) goto loc_0036685B;
    Arg2 = (*(uint64_t *)(result + 0x10)) >> (11);
    result = (*(uint64_t *)(result + 0x10)) >> (3);
    if (condition_is_below) { result = (uint32_t)(Arg2); }
    if (((1) & ((uint8_t)(result))) != 0) goto loc_0036614E;
    goto loc_0036685B;
loc_00366A34:
    if ((*(uint8_t *)(result + 0x23)) < ((uint8_t)(Arg4))) goto loc_00366172;
    result = MI_NODE_FROM_PFN(result, Arg2, *(uint64_t *)(result + 0x10), Arg4);
    v_stack_p20 = v_stack_m25C;
    result = MiUseSlabAllocator(v_stack_m1E8, v_stack_m240, *(uint64_t *)(result + 0x10), (uint32_t)((uint32_t)(result)));
    if ((uint32_t)(result) == 0) goto loc_00366172;
    if (v_stack_m25C > 4) goto loc_00366172;
    result = MiGetPfnSlabType(result, v_stack_m240, *(uint64_t *)(result + 0x10), (uint32_t)((uint32_t)(result)));
    if (((uint32_t)(result)) == 9) goto loc_00366A9B;
    result = MiCheckSlabPage(result, (uint32_t)(v_stack_m25C), 4, (uint32_t)((uint32_t)(result)));
    if ((uint32_t)(result) != 0) goto loc_00366172;
loc_00366A9B:
    local_rdi = (uint32_t)(((uint32_t)((uint32_t)(v_stack_m268))) | (16));
    goto loc_00366175;
loc_00366AA3:
    result = MiWalkEntireImagePageNeedsProcessing(v_stack_m220, (uint32_t)((uint32_t)(v_stack_p68)), (uint32_t)((uint32_t)(v_stack_m248)), (uint32_t)((uint32_t)(result)));
    Arg2 = 0;
    if ((uint32_t)(result) == 0) goto loc_003661DB;
    if (v_stack_p74 == 0) goto loc_00366EEF;
    result = MiAddPageToHeatList(v_stack_m268, v_stack_p68, Arg2 + 3, (uint32_t)((uint32_t)(result)));
    local_rdi = (uint32_t)((local_rdi) | (64));
loc_00366ADE:
    Arg2 = 0;
    goto loc_003661DB;
loc_00366AE5:
    result = (((uint32_t)((uint32_t)((uint32_t)(result)))) != 0xC000009AULL) ? 1 : 0;
    result = (uint32_t)((result) + (113));
    *(uint32_t *)(v_rip + 0xAC6CFD) = (uint32_t)(result);
    goto loc_00366583;
loc_00366B00:
    Arg1 = (*(uint64_t *)(result + 0x10)) >> (11);
    Arg2 = (uint32_t)((*(uint64_t *)(result + 0x10)) & (0x400ULL));
    result = (*(uint64_t *)(result + 0x10)) >> (3);
    if (Arg2 != 0) { result = (uint32_t)(Arg1); }
    if (((1) & ((uint8_t)(result))) != 0) goto loc_003664A1;
    goto loc_003661A5;
loc_00366B32:
    local_rsi = (result + result * 2) << (4);
    local_rsi = (local_rsi) + (Arg1);
    goto loc_003668C0;
loc_00366B52:
    if (((*(uint64_t *)(v_rip + 0xC5FF2B)) & (0x2000ULL)) != 0) goto loc_00366D16;
loc_00366B63:
    result = MiUpdateImagePfnImportRelocations(*(uint64_t *)(*(uint64_t *)(v_rip + 0xAC9A4C) + arg1 * 8), v_stack_m210, (uint32_t)((uint32_t)(v_stack_p68)), result);
    goto loc_00366242;
loc_00366B7A:
    if (condition_is_below) goto loc_00367001;
    result = MiGetPagingFileOffset(*(uint64_t *)(v_stack_p68), v_stack_m210, (uint32_t)((uint32_t)(v_stack_p68)), result);
    if ((uint32_t)(result) == 0) goto loc_00367001;
    result = MiUnlockProtoPoolPage(v_stack_p58, v_stack_p50, (uint32_t)((uint32_t)(v_stack_p68)), result);
    result = 0;
    v_stack_p58 = 0;
    if (((v_stack_p70) & ((uint8_t)(result + 2))) == 0) goto loc_00366BDA;
    result = MiPageHasRelocations(*(uint64_t *)(v_stack_m220 + 0x20), 0, result + 1, result + 2);
    Arg4 = 0;
    if ((uint32_t)(result) == 0) goto loc_00366375;
loc_00366BDA:
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(result))) << (12));
    result = MiGetEffectivePagePriorityThread(v_stack_m248, Arg2, result + 1, 0 + 2);
    if (((uint32_t)(result)) > 5) { result = 5; }
    if (v_stack_p68 != v_stack_m258) goto loc_00366E40;
loc_00366C03:
    v_stack_p28 = (uint32_t)((uint32_t)(v_stack_p78));
    v_stack_p20 = (uint32_t)(0 + 2);
    result = MiPrefetchControlArea(*(uint64_t *)(*(uint64_t *)(v_rip + 0xAC9A4C) + arg1 * 8), Arg2, (uint32_t)(0x1000ULL), (uint32_t)((uint32_t)(result)));
    Arg4 = 0;
    if (sign_flag) {
        Arg3 = v_rip - 3499177;
        Arg2 = 0;
        Arg1 = 0;
        result = KeDelayExecutionThread(Arg1, Arg2, Arg3, Arg4);
        Arg4 = 0;
    }
    goto loc_0036603C;
loc_00366C3D:
    if (((2) & ((uint8_t)(local_r15 + 40))) != 0) goto loc_00366E57;
loc_00366C4A:
    Arg3 = 0;
    v_stack_p28 = v_stack_mF8;
    Arg2 = 0;
    Arg1 = 0;
    v_stack_p20 = 0;
    result = MiInitializePageFaultPacket(Arg1, Arg2, Arg3, Arg4);
    v_stack_m218 = (uint32_t)(Arg3 + 1);
    result = MiObtainProtoReference(v_stack_p58, (uint32_t)((uint32_t)(Arg3 + 1)), Arg3, Arg4);
    v_stack_p20 = v_stack_m218;
    result = MiWaitForCollidedFaultComplete(v_stack_mF8, 0, v_stack_p58, v_stack_p50);
    Arg4 = 0;
    v_stack_p58 = 0;
    goto loc_00366762;
loc_00366CB4:
    if (v_stack_p60 != -1) goto loc_00366268;
    result = MI_PAGE_TO_FULL_COLOR(v_stack_p68, 0, v_stack_p58, Arg4);
    Arg4 = 0;
    v_stack_p28 = (uint32_t)(v_stack_p68);
    result = MiGetSlabPage(v_stack_m1E8, (uint32_t)(v_stack_m25C), (uint32_t)((uint32_t)(result)), Arg4);
    v_stack_p60 = result;
    if (result != -1) goto loc_00366268;
    local_rdi = (uint32_t)((local_rdi) & (0xFFFFFFEFULL));
    goto loc_00366268;
loc_00366CFC:
    result = MiPfnReferenceCountIsZero(0, v_stack_p68, (uint32_t)((uint32_t)(result)), Arg4);
    goto loc_00366480;
loc_00366D0C:
    goto loc_00365FA2;
loc_00366D16:
    if (((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xAC9A4C) + arg1 * 8) + 0x5C)) & (0xC0000ULL)) == 0) goto loc_00366B63;
    Arg1 = (0) >> (60);
    Arg1 = (uint8_t)((Arg1) & (7));
    if (((uint8_t)(Arg1)) != 3) goto loc_00366B63;
    result = VslApplySecureImageFixups(*(uint64_t *)(v_stack_m220 + 0x40), (uint32_t)((uint32_t)(v_stack_p68)), v_stack_p60, Arg4);
    Arg2 = 0;
    if (!sign_flag) goto loc_00366252;
    v_stack_p20 = *(uint64_t *)(*(uint64_t *)(v_rip + 0xAC9A4C) + arg1 * 8);
    result = KeBugCheckEx(26, (uint32_t)(0x51512ULL), (int32_t)((uint32_t)(result)), v_stack_p60);
loc_00366D6F:
    result = (uint8_t)((*(uint8_t *)(0 + 0x22)) & (7));
    if (((uint8_t)(result)) != 6) goto loc_003662D2;
    Arg3 = 0;
    result = MiTrimSharedPage(0, v_stack_p50, Arg3, v_stack_p60);
    result = MiLockPageInline(0, v_stack_p50, Arg3, v_stack_p60);
    if (condition_is_above_or_equal) goto loc_003662D2;
    local_rdi = (uint32_t)((local_rdi) & (0xFFFFFFEFULL));
    goto loc_003662D2;
loc_00366DAA:
loc_00366DAD:
    if (condition_is_not_equal) goto loc_00366FDB;
loc_00366DB8:
    result = KeAbPostRelease(local_r15 + 40, v_stack_p50, Arg3, v_stack_p60);
    if (condition_is_not_equal) goto loc_00366DE9;
    result = v_stack_p68 + 152;
    if ((*(uint64_t *)(v_stack_p68 + 0x98)) != (v_stack_p68 + 152)) {
        result = KiCheckForKernelApcDelivery(local_r15 + 40, v_stack_p50, 1, v_stack_p60);
        Arg3 = 1;
    }
    goto loc_0036667D;
loc_00366DF3:
    *(uint32_t *)(v_rip + 0xAC69FB) = 121;
    goto loc_0036656A;
loc_00366E02:
    v_stack_p20 = Arg3;
    Arg2 = 0;
    result = MiApplyDebuggerPatches(local_r15 + 40, Arg2, (uint32_t)((uint32_t)(v_stack_p68)), v_stack_p60);
    goto loc_003668C0;
loc_00366E19:
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m188)))) >> (1));
    Arg2 = (uint32_t)(((uint32_t)(v_stack_m188)) & (1));
    Arg3 = (uint32_t)((Arg3) & (3));
    result = MiInitializePageHeatList(result, Arg2, Arg3, (uint32_t)((uint32_t)(local_r15 + 40)));
    goto loc_00365FC3;
loc_00366E40:
    v_stack_m258 = v_stack_p68;
    Arg3 = (*(uint64_t *)(*(uint64_t *)(v_rip + 0xAC9A4C) + arg1 * 8) + 128) - (v_stack_p68);
    Arg3 = (Arg3) >> (3);
    Arg3 = (Arg3) << (12);
    goto loc_00366C03;
loc_00366E57:
    if ((((uint8_t)(result)) & ((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xAC9A4C) + arg1 * 8) + 0x38))))) != 0) goto loc_00366C4A;
    result = MiDeleteTransitionPte(v_stack_p68, 0, 17, (uint32_t)((uint32_t)(local_r15 + 40)));
    Arg4 = 0;
    goto loc_00366375;
loc_00366E86:
    result = MiIssuePageHeatList(v_stack_p68, 0, 17, Arg4);
    goto loc_003665A9;
loc_00366E93:
    if (condition_is_not_equal) goto loc_00366FE8;
loc_00366EAB:
    result = KeAbPostRelease(*(uint64_t *)(*(uint64_t *)(v_rip + 0xAC9A4C) + arg1 * 8) + 128, 0, 17, Arg4);
    if (condition_is_not_equal) goto loc_00366ED6;
    result = v_stack_p68 + 152;
    if ((*(uint64_t *)(v_stack_p68 + 0x98)) != (v_stack_p68 + 152)) {
        result = KiCheckForKernelApcDelivery(*(uint64_t *)(*(uint64_t *)(v_rip + 0xAC9A4C) + arg1 * 8) + 128, 0, 17, 1);
    }
    local_rdi = (uint32_t)((local_rdi) | (8));
    v_stack_m230 = *(uint64_t *)(v_stack_p58 + 0x48);
    goto loc_00366006;
loc_00366EEF:
    Arg3 = (uint32_t)(((uint32_t)(v_stack_p70)) | (16));
    result = MiWalkEntireImage(*(uint64_t *)(*(uint64_t *)(v_rip + 0xAC9A4C) + arg1 * 8), v_stack_m210, Arg3, (uint32_t)(v_stack_p78));
    goto loc_00366ADE;
loc_00366F12:
    local_r12 = (int32_t)((uint32_t)(result));
    if (((uint32_t)((int32_t)((uint32_t)(result)))) == 1) { local_r12 = (uint32_t)(v_stack_m210); }
    goto loc_00366252;
loc_00366F23:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(v_stack_m240), 1, Arg3, (uint32_t)(v_stack_p78));
    goto loc_003666FD;
loc_00366F31:
    result = (uint8_t)((*(uint8_t *)(v_stack_p58 + 0x22)) & (7));
    result = (uint8_t)((result) - (2));
    if (((uint8_t)(result)) > ((uint8_t)(*(uint64_t *)(v_stack_p58 + 0x48)))) goto loc_00366304;
    if ((uint16_t)((uint32_t)(*(uint32_t *)(v_stack_p58 + 0x20))) != 0) goto loc_00366304;
    if ((*(uint8_t *)(v_stack_p58 + 0x23)) < ((uint8_t)((uint8_t)(v_stack_m240)))) goto loc_00366304;
    local_r10 = (v_stack_p60 + v_stack_p60 * 2) << (4);
    local_r10 = (local_r10) + ((uint32_t)(*(uint32_t *)(v_stack_p58 + 0x20)));
    result = MiGetPfnSlabType(local_r10, 1, Arg3, (uint32_t)(v_stack_p78));
    if (((uint32_t)(result)) == 9) goto loc_00366309;
    result = MiGetPfnSlabType(v_stack_p58, 1, Arg3, (uint32_t)(v_stack_p78));
    Arg4 = 0;
    result = MiReplaceTransitionPage(v_stack_p58, local_r10, (uint32_t)((uint32_t)(result)), Arg4);
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(result))) << (4));
    Arg1 = (uint32_t)((Arg1) ^ ((uint32_t)(local_rdi)));
    Arg1 = (uint32_t)((Arg1) & (16));
    local_rdi = (uint32_t)((local_rdi) ^ ((uint32_t)(Arg1)));
    if ((((uint8_t)(*(uint64_t *)(v_stack_p58 + 0x48))) & ((uint8_t)(result))) == 0) goto loc_00366309;
    local_r15 = (v_stack_p60) | (-1);
    *(uint64_t *)(v_stack_p58 + 0x10) = *(uint64_t *)(v_rip - 0x356739);
    v_stack_p60 = local_r15;
    result = MiSetOriginalPtePfnFromFreeList(v_stack_p58 + 16, local_r10, (uint32_t)((uint32_t)(result)), Arg4);
    result = MiReleaseFreshPageLocked(v_stack_p58, local_r10, (uint32_t)((uint32_t)(result)), Arg4);
    goto loc_00366309;
loc_00366FDB:
    result = ExfReleasePushLockShared(v_stack_m240, local_r10, (uint32_t)((uint32_t)(result)), Arg4);
    goto loc_00366DB8;
loc_00366FE8:
    result = ExfReleasePushLockShared(v_stack_m240, local_r10, (uint32_t)((uint32_t)(result)), Arg4);
    goto loc_00366EAB;
loc_00366FF5:
    goto loc_00365FD0;
loc_00367001:
    goto loc_00366375;
loc_0036700B:
    Arg2 = ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xAC9A4C) + arg1 * 8) + 128)) & (16)) == 0) ? 1 : 0;
    result = (((2) & ((uint8_t)(local_rdi))) == 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg2))) != 0) goto loc_0036685B;
    goto loc_00366119;
loc_00367029:
    result = (*(uint64_t *)(v_stack_p58 + 0x18)) & (v_stack_m240);
    Arg4 = 0;
    *(uint64_t *)(v_stack_p58 + 0x18) = result;
    goto loc_0036615F;
loc_0036704A:
loc_0036704E:
    goto loc_00365FAC;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x38` | `64` | `R` |
| `Arg1` | `+ 0x3C` | `16` | `R` |
| `Arg1` | `+ 0x3E` | `8` | `R` |
| `Arg1` | `+ 0x5C` | `32` | `R` |
| `Arg1` | `+ 0x60` | `64` | `R` |
| `Arg1` | `+ 0x80` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00365D70&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
