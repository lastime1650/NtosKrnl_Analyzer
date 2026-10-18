# MiGetPage

- RVA: `0x002884C0`–`0x002898DA` (길이 `5,146` bytes)
- VA: `0x00000001402884C0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00066E08`
- 디코드: `1,331`개 명령, `5,146/5,146` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **46**; 고유 호출 대상: **32**
- 직접 호출자로 확인된 함수: **39**
- RIP 상대 이미지 참조: **22**

### Outgoing calls
- `0x0028886B` → [ExpInterlockedPopEntrySList](../6B/ExpInterlockedPopEntrySList_function_006BA570.md) (function, `0x006BA570`)
- `0x002888B4` → [MiGetPerfectColorHeadPage](MiGetPerfectColorHeadPage_function_00289CA8.md) (function, `0x00289CA8`)
- `0x00288936` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0028896F` → [MiGetPerfectFreeOrZeroPage](MiGetPerfectFreeOrZeroPage_function_002898E0.md) (function, `0x002898E0`)
- `0x00288999` → [MiCheckZeroFreeRebalance](MiCheckZeroFreeRebalance_function_0028B1FC.md) (function, `0x0028B1FC`)
- `0x002889C0` → [MiCacheAttributeHasValue](MiCacheAttributeHasValue_function_0028A14C.md) (function, `0x0028A14C`)
- `0x002889E2` → [MiDemoteLocalLargePage](MiDemoteLocalLargePage_function_0028A4F0.md) (function, `0x0028A4F0`)
- `0x00288A3A` → [MiRemovePageAnyColor](MiRemovePageAnyColor_function_0028A9D8.md) (function, `0x0028A9D8`)
- `0x00288A81` → [MiRemovePageAnyColor](MiRemovePageAnyColor_function_0028A9D8.md) (function, `0x0028A9D8`)
- `0x00288AAF` → [MiPageAvailable](../2A/MiPageAvailable_function_002A3138.md) (function, `0x002A3138`)
- `0x00288C2D` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00288CB8` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00288F22` → [MiZeroPhysicalPage](../33/MiZeroPhysicalPage_function_00332590.md) (function, `0x00332590`)
- `0x00288F4B` → [MiChangePageAttribute](../33/MiChangePageAttribute_function_00332ECC.md) (function, `0x00332ECC`)
- `0x00288FB7` → [ExpInterlockedPopEntrySList](../6B/ExpInterlockedPopEntrySList_function_006BA570.md) (function, `0x006BA570`)
- `0x00288FE2` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x00289050` → [MiSetOriginalPtePfnFromFreeList](MiSetOriginalPtePfnFromFreeList_function_0028A99C.md) (function, `0x0028A99C`)
- `0x00289081` → [MiRemoveLowestPriorityStandbyPage](../33/MiRemoveLowestPriorityStandbyPage_function_00334600.md) (function, `0x00334600`)
- `0x002890C0` → [MiPageAvailable](../2A/MiPageAvailable_function_002A3138.md) (function, `0x002A3138`)
- `0x0028919D` → [MiPageToChannel](../2B/MiPageToChannel_function_002B9B48.md) (function, `0x002B9B48`)
- `0x002891DA` → [MiGetPageSlist](MiGetPageSlist_function_0028B79C.md) (function, `0x0028B79C`)
- `0x0028924A` → [MiCacheAttributeHasValue](MiCacheAttributeHasValue_function_0028A14C.md) (function, `0x0028A14C`)
- `0x00289271` → [MiDemoteLocalLargePage](MiDemoteLocalLargePage_function_0028A4F0.md) (function, `0x0028A4F0`)
- `0x002892A1` → [MiGetFreeOrZeroPageAnyColor](../43/MiGetFreeOrZeroPageAnyColor_function_004352D8.md) (function, `0x004352D8`)
- `0x002892C0` → [MiGetPageSlist](MiGetPageSlist_function_0028B79C.md) (function, `0x0028B79C`)
- `0x00289300` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x002893BE` → [MiRemovePageAnyColor](MiRemovePageAnyColor_function_0028A9D8.md) (function, `0x0028A9D8`)
- `0x00289407` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x0028944F` → [MiObtainedPageIsGood](../43/MiObtainedPageIsGood_function_00435448.md) (function, `0x00435448`)
- `0x00289468` → [MiObtainedPageIsGood](../43/MiObtainedPageIsGood_function_00435448.md) (function, `0x00435448`)
- `0x002895B0` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x002895CD` → [MiAssignDefaultChannel](../31/MiAssignDefaultChannel_function_0031E5B0.md) (function, `0x0031E5B0`)
- `0x002895DD` → [MiPfnBestZeroAttribute](../2C/MiPfnBestZeroAttribute_function_002C8600.md) (function, `0x002C8600`)
- `0x002895F6` → [MiChangePageAttribute](../33/MiChangePageAttribute_function_00332ECC.md) (function, `0x00332ECC`)
- `0x00289631` → [MiSwapNumaStandbyPage](../38/MiSwapNumaStandbyPage_function_00385144.md) (function, `0x00385144`)
- `0x0028965E` → [MiPageToNode](../33/MiPageToNode_function_00338CD0.md) (function, `0x00338CD0`)
- `0x0028966F` → [MiReleaseFreshPage](../33/MiReleaseFreshPage_function_00334AE0.md) (function, `0x00334AE0`)
- `0x002896A6` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x002896B6` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00289704` → [MiArePageContentsZero](../4D/MiArePageContentsZero_function_004D4278.md) (function, `0x004D4278`)
- `0x00289725` → [MiGetPfnChannel](../33/MiGetPfnChannel_function_0033BA90.md) (function, `0x0033BA90`)
- `0x002897AD` → [MiCheckNodeChannelStandbyCount](../4A/MiCheckNodeChannelStandbyCount_function_004A1108.md) (function, `0x004A1108`)
- `0x002897D1` → [MiAssignDefaultChannel](../31/MiAssignDefaultChannel_function_0031E5B0.md) (function, `0x0031E5B0`)
- `0x002898A3` → [MiPfnBestZeroAttribute](../2C/MiPfnBestZeroAttribute_function_002C8600.md) (function, `0x002C8600`)
- `0x002898B2` → [MiChangePageAttribute](../33/MiChangePageAttribute_function_00332ECC.md) (function, `0x00332ECC`)
- `0x002898D0` → [MiZeroLargePage](../2C/MiZeroLargePage_function_002C6914.md) (function, `0x002C6914`)

### Direct callers
- [MiHandleForkTransitionPte](../22/MiHandleForkTransitionPte_function_0022D34C.md) at `0x0022D9B1`
- [MiHandleForkTransitionPte](../22/MiHandleForkTransitionPte_function_0022D34C.md) at `0x0022DA26`
- [MiBuildForkPte](../22/MiBuildForkPte_function_0022E32C.md) at `0x0022EB0A`
- [MiGetUltraPage](MiGetUltraPage_function_002883D0.md) at `0x0028843E`
- [MiDemoteLocalLargePage](MiDemoteLocalLargePage_function_0028A4F0.md) at `0x0028A67A`
- [MiDemoteLocalLargePage](MiDemoteLocalLargePage_function_0028A4F0.md) at `0x0028A8CB`
- [MiTradeTransitionPage](MiTradeTransitionPage_function_0028B9AC.md) at `0x0028BB15`
- [MiMigratePfn](MiMigratePfn_function_0028DBB0.md) at `0x0028DD64`
- [MiSwapStackPage](../29/MiSwapStackPage_function_0029FDE0.md) at `0x0029FF1B`
- [MiAllocateKernelStackPages](../2A/MiAllocateKernelStackPages_function_002A1BEC.md) at `0x002A1D62`
- [MiGetSystemPage](../2A/MiGetSystemPage_function_002AB7E8.md) at `0x002AB840`
- [MiStealPage](../2B/MiStealPage_function_002B28D0.md) at `0x002B2B9C`
- [MiMakePageAvoidRead](../2B/MiMakePageAvoidRead_function_002B7DE0.md) at `0x002B7F90`
- [MmAllocateNonChargedSecurePages](../2C/MmAllocateNonChargedSecurePages_function_002C886C.md) at `0x002C89B5`
- [sub_002F6E32](../2F/Unknown_function_002F6E32.md) at `0x002F7217`
- [MiGetLargePage](../31/MiGetLargePage_function_0031E210.md) at `0x0031E377`
- [MiGetPageChain](../33/MiGetPageChain_function_00330130.md) at `0x0033027F`
- [MiGetPageChain](../33/MiGetPageChain_function_00330130.md) at `0x00330513`
- [MiGetPageChain](../33/MiGetPageChain_function_00330130.md) at `0x00330877`
- [MiRemoveLowestPriorityStandbyPage](../33/MiRemoveLowestPriorityStandbyPage_function_00334600.md) at `0x003347AE`
- [MiCopyOnWrite](../36/MiCopyOnWrite_function_00362A0C.md) at `0x00362CFE`
- [MiPrivateFixup](../36/MiPrivateFixup_function_003693E8.md) at `0x00369545`
- [MiResolveMappedFileFault](../36/MiResolveMappedFileFault_function_0036B640.md) at `0x0036B9DC`
- [MiGetPageTablePages](../37/MiGetPageTablePages_function_00376C3C.md) at `0x00376E17`
- [MiGetPageTablePages](../37/MiGetPageTablePages_function_00376C3C.md) at `0x00376E4D`
- [MiReplaceLockedPage](../38/MiReplaceLockedPage_function_0038351C.md) at `0x0038361B`
- [MiAllocateMdlPagesByLists](../3B/MiAllocateMdlPagesByLists_function_003B7898.md) at `0x003B79B1`
- [MiGetLargePageDemoteAsNeeded](../3B/MiGetLargePageDemoteAsNeeded_function_003B8440.md) at `0x003B850C`
- [MiPruneStandbyPages](../3B/MiPruneStandbyPages_function_003BC0E4.md) at `0x003BC32D`
- [MiMakeOutswappedPageResident](../43/MiMakeOutswappedPageResident_function_00431AD0.md) at `0x00431D4A`
- [MiMakeOutswappedPageResident](../43/MiMakeOutswappedPageResident_function_00431AD0.md) at `0x00431D6F`
- [MiHandleSpecialPurposeMemoryCachedFault](../44/MiHandleSpecialPurposeMemoryCachedFault_function_0044C740.md) at `0x0044C851`
- [MiHandleSpecialPurposeMemoryCachedFault](../44/MiHandleSpecialPurposeMemoryCachedFault_function_0044C740.md) at `0x0044C8A5`
- [MiGetFileHashPage](../49/MiGetFileHashPage_function_004926F4.md) at `0x0049272B`
- [MiSwitchToTransition](../4C/MiSwitchToTransition_function_004C0F5C.md) at `0x004C10F3`
- [MiSplitDirectMapPage](../4D/MiSplitDirectMapPage_function_004DAAA0.md) at `0x004DAB4E`
- [MiComputeCacheAttributeSpeeds](../69/MiComputeCacheAttributeSpeeds_function_006999E8.md) at `0x00699AFB`
- [sub_006E313A](../6E/Unknown_function_006E313A.md) at `0x006E31AA`
- [MiPfPrepareReadList](../../page/93/MiPfPrepareReadList_function_0093CD5C.md) at `0x0093D214`
- [MiAllocateTopLevelPage](../../page/A5/MiAllocateTopLevelPage_function_00A5F2EC.md) at `0x00A5F37D`
- [MiDoneWithThisPageGetAnother](../../page/A7/MiDoneWithThisPageGetAnother_function_00A7DDDC.md) at `0x00A7DE3F`
- [MmAllocateIndependentPagesEx](../../page/AA/MmAllocateIndependentPagesEx_function_00AA0CFC.md) at `0x00AA0EA5`
- [sub_00B42C66](../../page/B4/Unknown_function_00B42C66.md) at `0x00B42D0C`
- [MiAllocateDummyPage](../../init/C5/MiAllocateDummyPage_function_00C5F6E8.md) at `0x00C5F767`
- [MmInitializeImageViewExtensionCfg](../../init/C6/MmInitializeImageViewExtensionCfg_function_00C64FC4.md) at `0x00C650FF`
- [MiInitializeCacheFlushing](../../init/C6/MiInitializeCacheFlushing_function_00C6ACF8.md) at `0x00C6ADB3`

### Static image references
- `0x002884DC` → RVA `0x00E0A740` (`.data`; read)
- `0x00288521` → RVA `0x00FC5000` (`ALMOSTRO`; read)
- `0x0028855D` → RVA `0x00FC5002` (`ALMOSTRO`; read)
- `0x002885A7` → RVA `0x00E2DBD0` (`.data`; read)
- `0x002886E0` → RVA `0x00E2DCC0` (`.data`; read)
- `0x002887CB` → RVA `0x00010860` (`.rdata`; read)
- `0x002887D5` → RVA `0x00011038` (`.rdata`; read)
- `0x00288885` → RVA `0x00010880` (`.rdata`; read)
- `0x00288895` → RVA `0x00FC6A88` (`ALMOSTRO`; read)
- `0x00288B51` → RVA `0x00E2DBC0` (`.data`; read)
- `0x00288B58` → RVA `0x00E2DBC4` (`.data`; read)
- `0x00288B69` → RVA `0x00E2DC20` (`.data`; read)
- `0x00288BB4` → RVA `0x00E2DBC0` (`.data`; write)
- `0x00288BC4` → RVA `0x00E2DC28` (`.data`; read)
- `0x00288E7A` → RVA `0x00E2DCD8` (`.data`; reference)
- `0x00288FD2` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x002890F8` → RVA `0x00E2DCCC` (`.data`; read)
- `0x002894F3` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x00289698` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)
- `0x002896C0` → RVA `0x00E30270` (`.data`; read)
- `0x002896C8` → RVA `0x00FC5054` (`ALMOSTRO`; reference)
- `0x002896CE` → RVA `0x00E30270` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x00288C99` → [sub_006DA360](../6D/Unknown_function_006DA360.md) (`tail-transfer`)
  - `0x00288C9F` → [sub_006DA360 + 0x19](../6D/Unknown_function_006DA360.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002884C0  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
002884C5  55                              push rbp
002884C6  56                              push rsi
002884C7  57                              push rdi
002884C8  41 54                           push r12
002884CA  41 55                           push r13
002884CC  41 56                           push r14
002884CE  41 57                           push r15
002884D0  48 8D 6C 24 F0                  lea rbp, [rsp - 0x10]
002884D5  48 81 EC 10 01 00 00            sub rsp, 0x110
002884DC  48 8B 05 5D 22 B8 00            mov rax, qword ptr [rip + 0xb8225d]
002884E3  48 33 C4                        xor rax, rsp
002884E6  48 89 45 08                     mov qword ptr [rbp + 8], rax
002884EA  41 8B F8                        mov edi, r8d
002884ED  44 89 45 88                     mov dword ptr [rbp - 0x78], r8d
002884F1  45 33 C9                        xor r9d, r9d
002884F4  89 54 24 30                     mov dword ptr [rsp + 0x30], edx
002884F8  44 8B C2                        mov r8d, edx
002884FB  48 89 4D 90                     mov qword ptr [rbp - 0x70], rcx
002884FF  41 C1 E8 10                     shr r8d, 0x10
00288503  8B C7                           mov eax, edi
00288505  41 8B D8                        mov ebx, r8d
00288508  8B F2                           mov esi, edx
0028850A  83 E3 0C                        and ebx, 0xc
0028850D  45 8D 59 01                     lea r11d, [r9 + 1]
00288511  83 E0 02                        and eax, 2
00288514  45 8B E1                        mov r12d, r9d
00288517  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
0028851B  0F 85 FE 0F 00 00               jne 0x14028951f
00288521  0F B7 15 D8 CA D3 00            movzx edx, word ptr [rip + 0xd3cad8]
00288528  8B C3                           mov eax, ebx
0028852A  C1 E8 02                        shr eax, 2
0028852D  41 83 E0 03                     and r8d, 3
00288531  83 E0 03                        and eax, 3
00288534  0B D8                           or ebx, eax
00288536  0F BA E7 12                     bt edi, 0x12
0028853A  0F 82 0E 07 00 00               jb 0x140288c4e
00288540  F7 C7 40 10 00 00               test edi, 0x1040
00288546  41 0F 45 D3                     cmovne edx, r11d
0028854A  33 C0                           xor eax, eax
0028854C  89 54 24 78                     mov dword ptr [rsp + 0x78], edx
00288550  89 45 E0                        mov dword ptr [rbp - 0x20], eax
00288553  44 8B FE                        mov r15d, esi
00288556  66 89 45 E4                     mov word ptr [rbp - 0x1c], ax
0028855A  4D 8B E9                        mov r13, r9
0028855D  0F B6 05 9E CA D3 00            movzx eax, byte ptr [rip + 0xd3ca9e]
00288564  4D 8B D1                        mov r10, r9
00288567  8B C8                           mov ecx, eax
00288569  41 C1 EF 09                     shr r15d, 9
0028856D  41 83 E7 3F                     and r15d, 0x3f
00288571  4C 89 4D A8                     mov qword ptr [rbp - 0x58], r9
00288575  41 3A C3                        cmp al, r11b
00288578  44 89 7C 24 74                  mov dword ptr [rsp + 0x74], r15d
0028857D  8B C6                           mov eax, esi
0028857F  44 89 44 24 38                  mov dword ptr [rsp + 0x38], r8d
00288584  41 0F 46 CB                     cmovbe ecx, r11d
00288588  45 8B F1                        mov r14d, r9d
0028858B  C1 E8 08                        shr eax, 8
0028858E  41 22 C3                        and al, r11b
00288591  88 4D E3                        mov byte ptr [rbp - 0x1d], cl
00288594  88 45 E4                        mov byte ptr [rbp - 0x1c], al
00288597  44 3B F2                        cmp r14d, edx
0028859A  0F 83 59 05 00 00               jae 0x140288af9
002885A0  0F B7 0D 59 CA D3 00            movzx ecx, word ptr [rip + 0xd3ca59]
002885A7  48 8B 05 22 56 BA 00            mov rax, qword ptr [rip + 0xba5622]
002885AE  41 0F AF CF                     imul ecx, r15d
002885B2  41 03 CE                        add ecx, r14d
002885B5  8B 04 88                        mov eax, dword ptr [rax + rcx*4]
002885B8  48 8B 4D 90                     mov rcx, qword ptr [rbp - 0x70]
002885BC  4C 69 C8 80 DF 00 00            imul r9, rax, 0xdf80
002885C3  C1 E0 09                        shl eax, 9
002885C6  4C 03 49 10                     add r9, qword ptr [rcx + 0x10]
002885CA  33 C6                           xor eax, esi
002885CC  25 00 7E 00 00                  and eax, 0x7e00
002885D1  4C 89 4C 24 50                  mov qword ptr [rsp + 0x50], r9
002885D6  33 F0                           xor esi, eax
002885D8  89 74 24 30                     mov dword ptr [rsp + 0x30], esi
002885DC  49 8B 81 80 3A 00 00            mov rax, qword ptr [r9 + 0x3a80]
002885E3  48 85 C0                        test rax, rax
002885E6  0F 84 C3 0A 00 00               je 0x1402890af
002885EC  4D 85 C9                        test r9, r9
002885EF  0F 85 61 06 00 00               jne 0x140288c56
002885F5  33 C0                           xor eax, eax
002885F7  89 45 E0                        mov dword ptr [rbp - 0x20], eax
002885FA  66 89 45 E4                     mov word ptr [rbp - 0x1c], ax
002885FE  0F B6 05 FD C9 D3 00            movzx eax, byte ptr [rip + 0xd3c9fd]
00288605  3C 01                           cmp al, 1
00288607  8B C8                           mov ecx, eax
00288609  8B C6                           mov eax, esi
0028860B  41 0F 46 CB                     cmovbe ecx, r11d
0028860F  C1 E8 08                        shr eax, 8
00288612  24 01                           and al, 1
00288614  88 4D E3                        mov byte ptr [rbp - 0x1d], cl
00288617  88 45 E4                        mov byte ptr [rbp - 0x1c], al
0028861A  41 8B C6                        mov eax, r14d
0028861D  49 0F A3 C2                     bt r10, rax
00288621  72 22                           jb 0x140288645
00288623  41 83 F8 03                     cmp r8d, 3
00288627  B8 60 3B 00 00                  mov eax, 0x3b60
0028862C  41 BC 58 3B 00 00               mov r12d, 0x3b58
00288632  44 0F 45 E0                     cmovne r12d, eax
00288636  41 8B C6                        mov eax, r14d
00288639  49 0F AB C2                     bts r10, rax
0028863D  4C 89 55 A8                     mov qword ptr [rbp - 0x58], r10
00288641  4F 8B 24 0C                     mov r12, qword ptr [r12 + r9]
00288645  44 8B D3                        mov r10d, ebx
00288648  44 8B C6                        mov r8d, esi
0028864B  41 C1 E8 10                     shr r8d, 0x10
0028864F  41 83 E2 03                     and r10d, 3
00288653  41 83 E0 03                     and r8d, 3
00288657  4C 89 54 24 40                  mov qword ptr [rsp + 0x40], r10
0028865C  8B C6                           mov eax, esi
0028865E  BA 00 00 00 00                  mov edx, 0
00288663  C1 E8 0F                        shr eax, 0xf
00288666  83 E0 01                        and eax, 1
00288669  4B 8D 0C 80                     lea rcx, [r8 + r8*4]
0028866D  48 C1 E1 08                     shl rcx, 8
00288671  49 03 C9                        add rcx, r9
00288674  41 83 F8 03                     cmp r8d, 3
00288678  0F 44 C2                        cmove eax, edx
0028867B  49 8D 04 82                     lea rax, [r10 + rax*4]
0028867F  48 8B 4C C1 18                  mov rcx, qword ptr [rcx + rax*8 + 0x18]
00288684  48 85 C9                        test rcx, rcx
00288687  0F 85 F1 00 00 00               jne 0x14028877e
0028868D  49 8B 81 60 3B 00 00            mov rax, qword ptr [r9 + 0x3b60]
00288694  66 85 C0                        test ax, ax
00288697  0F 85 E1 00 00 00               jne 0x14028877e
0028869D  41 3B D0                        cmp edx, r8d
002886A0  77 2A                           ja 0x1402886cc
002886A2  8B C2                           mov eax, edx
002886A4  48 8D 0C 80                     lea rcx, [rax + rax*4]
002886A8  48 C1 E1 08                     shl rcx, 8
002886AC  4A 8B 44 09 08                  mov rax, qword ptr [rcx + r9 + 8]
002886B1  48 85 C0                        test rax, rax
002886B4  0F 85 C4 00 00 00               jne 0x14028877e
002886BA  4A 8B 44 09 10                  mov rax, qword ptr [rcx + r9 + 0x10]
002886BF  48 85 C0                        test rax, rax
002886C2  0F 85 B6 00 00 00               jne 0x14028877e
002886C8  FF C2                           inc edx
002886CA  EB D1                           jmp 0x14028869d
002886CC  41 83 FA 01                     cmp r10d, 1
002886D0  0F 85 ED 05 00 00               jne 0x140288cc3
002886D6  41 83 F8 03                     cmp r8d, 3
002886DA  0F 85 E3 05 00 00               jne 0x140288cc3
002886E0  48 8D 05 D9 55 BA 00            lea rax, [rip + 0xba55d9]
002886E7  33 C9                           xor ecx, ecx
002886E9  42 8B 04 80                     mov eax, dword ptr [rax + r8*4]
002886ED  44 8B D9                        mov r11d, ecx
002886F0  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
002886F4  41 83 FB 02                     cmp r11d, 2
002886F8  0F 83 C0 05 00 00               jae 0x140288cbe
002886FE  8B D0                           mov edx, eax
00288700  41 8B C3                        mov eax, r11d
00288703  48 05 A0 03 00 00               add rax, 0x3a0
00288709  48 03 C0                        add rax, rax
0028870C  49 8B 0C C1                     mov rcx, qword ptr [r9 + rax*8]
00288710  48 85 C9                        test rcx, rcx
00288713  74 64                           je 0x140288779
00288715  48 83 FA 01                     cmp rdx, 1
00288719  77 17                           ja 0x140288732
0028871B  75 5C                           jne 0x140288779
0028871D  49 8B 44 C1 08                  mov rax, qword ptr [r9 + rax*8 + 8]
00288722  48 0F BA 20 00                  bt qword ptr [rax], 0
00288727  72 50                           jb 0x140288779
00288729  8B 44 24 34                     mov eax, dword ptr [rsp + 0x34]
0028872D  41 FF C3                        inc r11d
00288730  EB C2                           jmp 0x1402886f4
00288732  48 3B CA                        cmp rcx, rdx
00288735  72 42                           jb 0x140288779
00288737  49 8B 4C C1 08                  mov rcx, qword ptr [r9 + rax*8 + 8]
0028873C  4C 8D 52 FF                     lea r10, [rdx - 1]
00288740  49 8B C2                        mov rax, r10
00288743  48 C1 E8 06                     shr rax, 6
00288747  4C 8D 04 C1                     lea r8, [rcx + rax*8]
0028874B  48 8B 01                        mov rax, qword ptr [rcx]
0028874E  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
00288753  49 3B C8                        cmp rcx, r8
00288756  0F 85 B5 0C 00 00               jne 0x140289411
0028875C  B9 40 00 00 00                  mov ecx, 0x40
00288761  48 C7 C0 FF FF FF FF            mov rax, 0xffffffffffffffff
00288768  2A CA                           sub cl, dl
0028876A  48 D3 E8                        shr rax, cl
0028876D  48 85 44 24 68                  test qword ptr [rsp + 0x68], rax
00288772  0F 94 C0                        sete al
00288775  84 C0                           test al, al
00288777  75 B0                           jne 0x140288729
00288779  4C 8B 54 24 40                  mov r10, qword ptr [rsp + 0x40]
0028877E  41 B8 01 00 00 00               mov r8d, 1
00288784  41 8B CA                        mov ecx, r10d
00288787  41 8B D0                        mov edx, r8d
0028878A  8B C3                           mov eax, ebx
0028878C  D3 E2                           shl edx, cl
0028878E  C1 E8 04                        shr eax, 4
00288791  23 D0                           and edx, eax
00288793  F6 C2 0F                        test dl, 0xf
00288796  0F 85 27 05 00 00               jne 0x140288cc3
0028879C  8B C3                           mov eax, ebx
0028879E  89 5C 24 40                     mov dword ptr [rsp + 0x40], ebx
002887A2  C1 E0 12                        shl eax, 0x12
002887A5  8B D7                           mov edx, edi
002887A7  33 C6                           xor eax, esi
002887A9  25 00 00 0C 00                  and eax, 0xc0000
002887AE  33 F0                           xor esi, eax
002887B0  8B C3                           mov eax, ebx
002887B2  83 E0 03                        and eax, 3
002887B5  83 E2 10                        and edx, 0x10
002887B8  89 45 A0                        mov dword ptr [rbp - 0x60], eax
002887BB  89 54 24 70                     mov dword ptr [rsp + 0x70], edx
002887BF  33 C9                           xor ecx, ecx
002887C1  44 89 45 C8                     mov dword ptr [rbp - 0x38], r8d
002887C5  85 D2                           test edx, edx
002887C7  48 89 4D B8                     mov qword ptr [rbp - 0x48], rcx
002887CB  48 8D 05 8E 80 D8 FF            lea rax, [rip - 0x277f72]
002887D2  89 4D D4                        mov dword ptr [rbp - 0x2c], ecx
002887D5  4C 8D 05 5C 88 D8 FF            lea r8, [rip - 0x2777a4]
002887DC  48 89 4D D8                     mov qword ptr [rbp - 0x28], rcx
002887E0  49 0F 44 C0                     cmove rax, r8
002887E4  89 74 24 30                     mov dword ptr [rsp + 0x30], esi
002887E8  0F 94 C1                        sete cl
002887EB  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
002887EF  8B C6                           mov eax, esi
002887F1  4C 89 4D B0                     mov qword ptr [rbp - 0x50], r9
002887F5  25 00 00 03 00                  and eax, 0x30000
002887FA  89 75 CC                        mov dword ptr [rbp - 0x34], esi
002887FD  89 7D D0                        mov dword ptr [rbp - 0x30], edi
00288800  89 4C 24 48                     mov dword ptr [rsp + 0x48], ecx
00288804  3D 00 00 03 00                  cmp eax, 0x30000
00288809  0F 85 A1 00 00 00               jne 0x1402888b0
0028880F  8B C6                           mov eax, esi
00288811  25 00 00 0C 00                  and eax, 0xc0000
00288816  3D 00 00 04 00                  cmp eax, 0x40000
0028881B  0F 85 8F 00 00 00               jne 0x1402888b0
00288821  40 0F B6 C6                     movzx eax, sil
00288825  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
00288829  44 8B C0                        mov r8d, eax
0028882C  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00288831  48 63 D1                        movsxd rdx, ecx
00288834  48 8D 82 A0 03 00 00            lea rax, [rdx + 0x3a0]
0028883B  48 C1 E0 04                     shl rax, 4
0028883F  49 03 C1                        add rax, r9
00288842  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
00288847  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0028884B  4C 0F A3 00                     bt qword ptr [rax], r8
0028884F  0F 83 A8 07 00 00               jae 0x140288ffd
00288855  49 8B 84 D1 60 3A 00 00         mov rax, qword ptr [r9 + rdx*8 + 0x3a60]
0028885D  49 8B C8                        mov rcx, r8
00288860  48 C1 E1 04                     shl rcx, 4
00288864  48 03 C8                        add rcx, rax
00288867  48 89 45 98                     mov qword ptr [rbp - 0x68], rax
0028886B  E8 00 1D 43 00                  call 0x1406ba570
00288870  4C 8B E8                        mov r13, rax
00288873  48 85 C0                        test rax, rax
00288876  0F 84 D9 06 00 00               je 0x140288f55
0028887C  83 7C 24 48 00                  cmp dword ptr [rsp + 0x48], 0
00288881  49 8D 4D 10                     lea rcx, [r13 + 0x10]
00288885  48 8B 05 F4 7F D8 FF            mov rax, qword ptr [rip - 0x27800c]
0028888C  48 89 01                        mov qword ptr [rcx], rax
0028888F  0F 85 BB 07 00 00               jne 0x140289050
00288895  0F B6 05 EC E1 D3 00            movzx eax, byte ptr [rip + 0xd3e1ec]
0028889C  84 C0                           test al, al
0028889E  0F 88 1C 0E 00 00               js 0x1402896c0
002888A4  45 33 C9                        xor r9d, r9d
002888A7  4D 89 4D 00                     mov qword ptr [r13], r9
002888AB  48 8B 01                        mov rax, qword ptr [rcx]
002888AE  EB 0F                           jmp 0x1402888bf
002888B0  48 8D 4D B0                     lea rcx, [rbp - 0x50]
002888B4  E8 EF 13 00 00                  call 0x140289ca8
002888B9  4C 8B E8                        mov r13, rax
002888BC  45 33 C9                        xor r9d, r9d
002888BF  49 83 FD 02                     cmp r13, 2
002888C3  0F 83 34 02 00 00               jae 0x140288afd
002888C9  4C 8B 6C 24 50                  mov r13, qword ptr [rsp + 0x50]
002888CE  8B C6                           mov eax, esi
002888D0  C1 E8 10                        shr eax, 0x10
002888D3  83 E0 03                        and eax, 3
002888D6  C1 EE 0F                        shr esi, 0xf
002888D9  83 E6 01                        and esi, 1
002888DC  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
002888E0  4C 8D 04 80                     lea r8, [rax + rax*4]
002888E4  49 C1 E0 08                     shl r8, 8
002888E8  4D 03 C5                        add r8, r13
002888EB  83 7C 24 70 00                  cmp dword ptr [rsp + 0x70], 0
002888F0  0F 84 E3 07 00 00               je 0x1402890d9
002888F6  40 F6 C7 20                     test dil, 0x20
002888FA  0F 84 DA 0A 00 00               je 0x1402893da
00288900  8B 45 A0                        mov eax, dword ptr [rbp - 0x60]
00288903  48 83 C0 04                     add rax, 4
00288907  48 8D 14 B0                     lea rdx, [rax + rsi*4]
0028890B  48 C1 E2 05                     shl rdx, 5
0028890F  49 03 D0                        add rdx, r8
00288912  8B F7                           mov esi, edi
00288914  83 E6 EF                        and esi, 0xffffffef
00288917  48 85 D2                        test rdx, rdx
0028891A  74 47                           je 0x140288963
0028891C  4C 8B 02                        mov r8, qword ptr [rdx]
0028891F  48 8D 4D E8                     lea rcx, [rbp - 0x18]
00288923  48 8B 52 08                     mov rdx, qword ptr [rdx + 8]
00288927  0F 57 C0                        xorps xmm0, xmm0
0028892A  49 C1 E8 03                     shr r8, 3
0028892E  0F 11 45 E8                     movups xmmword ptr [rbp - 0x18], xmm0
00288932  0F 11 45 F8                     movups xmmword ptr [rbp - 8], xmm0
00288936  E8 05 DF 43 00                  call 0x1406c6840
0028893B  33 C0                           xor eax, eax
0028893D  48 8D 4D E8                     lea rcx, [rbp - 0x18]
00288941  44 8B C0                        mov r8d, eax
00288944  8B D0                           mov edx, eax
00288946  F3 48 0F B8 01                  popcnt rax, qword ptr [rcx]
0028894B  44 03 C0                        add r8d, eax
0028894E  41 83 F8 08                     cmp r8d, 8
00288952  0F 83 55 0A 00 00               jae 0x1402893ad
00288958  FF C2                           inc edx
0028895A  48 83 C1 08                     add rcx, 8
0028895E  83 FA 04                        cmp edx, 4
00288961  72 E3                           jb 0x140288946
00288963  44 8B C6                        mov r8d, esi
00288966  49 8B CD                        mov rcx, r13
00288969  8B 74 24 30                     mov esi, dword ptr [rsp + 0x30]
0028896D  8B D6                           mov edx, esi
0028896F  E8 6C 0F 00 00                  call 0x1402898e0
00288974  4C 8B E8                        mov r13, rax
00288977  48 83 F8 02                     cmp rax, 2
0028897B  0F 83 75 01 00 00               jae 0x140288af6
00288981  83 7C 24 34 03                  cmp dword ptr [rsp + 0x34], 3
00288986  4C 8B 6C 24 50                  mov r13, qword ptr [rsp + 0x50]
0028898B  75 11                           jne 0x14028899e
0028898D  49 8B 8D 88 3A 00 00            mov rcx, qword ptr [r13 + 0x3a88]
00288994  44 8B C7                        mov r8d, edi
00288997  8B D6                           mov edx, esi
00288999  E8 5E 28 00 00                  call 0x14028b1fc
0028899E  8B C6                           mov eax, esi
002889A0  25 00 00 03 00                  and eax, 0x30000
002889A5  3D 00 00 03 00                  cmp eax, 0x30000
002889AA  0F 94 C1                        sete cl
002889AD  40 F6 C7 02                     test dil, 2
002889B1  0F 94 C0                        sete al
002889B4  84 C8                           test al, cl
002889B6  74 3B                           je 0x1402889f3
002889B8  8B CE                           mov ecx, esi
002889BA  C1 E9 12                        shr ecx, 0x12
002889BD  83 E1 03                        and ecx, 3
002889C0  E8 87 17 00 00                  call 0x14028a14c
002889C5  85 C0                           test eax, eax
002889C7  74 2A                           je 0x1402889f3
002889C9  49 8B 8D 88 3A 00 00            mov rcx, qword ptr [r13 + 0x3a88]
002889D0  8B D3                           mov edx, ebx
002889D2  C1 E2 10                        shl edx, 0x10
002889D5  44 8B C7                        mov r8d, edi
002889D8  33 D6                           xor edx, esi
002889DA  81 E2 00 00 0C 00               and edx, 0xc0000
002889E0  33 D6                           xor edx, esi
002889E2  E8 09 1B 00 00                  call 0x14028a4f0
002889E7  4C 8B E8                        mov r13, rax
002889EA  48 85 C0                        test rax, rax
002889ED  0F 85 55 0A 00 00               jne 0x140289448
002889F3  4C 8B 4C 24 50                  mov r9, qword ptr [rsp + 0x50]
002889F8  8B F7                           mov esi, edi
002889FA  8B 4C 24 30                     mov ecx, dword ptr [rsp + 0x30]
002889FE  49 8B 81 88 3A 00 00            mov rax, qword ptr [r9 + 0x3a88]
00288A05  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
00288A0A  8B C1                           mov eax, ecx
00288A0C  25 00 00 03 00                  and eax, 0x30000
00288A11  3D 00 00 03 00                  cmp eax, 0x30000
00288A16  75 12                           jne 0x140288a2a
00288A18  8B C1                           mov eax, ecx
00288A1A  25 00 00 0C 00                  and eax, 0xc0000
00288A1F  3D 00 00 04 00                  cmp eax, 0x40000
00288A24  0F 84 8E 08 00 00               je 0x1402892b8
00288A2A  8B D1                           mov edx, ecx
00288A2C  41 B9 01 00 00 00               mov r9d, 1
00288A32  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
00288A37  44 8B C7                        mov r8d, edi
00288A3A  E8 99 1F 00 00                  call 0x14028a9d8
00288A3F  4C 8B E8                        mov r13, rax
00288A42  48 83 F8 02                     cmp rax, 2
00288A46  0F 84 81 06 00 00               je 0x1402890cd
00288A4C  48 85 C0                        test rax, rax
00288A4F  0F 85 96 07 00 00               jne 0x1402891eb
00288A55  40 F6 C7 40                     test dil, 0x40
00288A59  0F 85 48 07 00 00               jne 0x1402891a7
00288A5F  0F BA E6 0A                     bt esi, 0xa
00288A63  0F 82 71 08 00 00               jb 0x1402892da
00288A69  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
00288A6E  0F BA EE 0A                     bts esi, 0xa
00288A72  44 8B C6                        mov r8d, esi
00288A75  41 B9 01 00 00 00               mov r9d, 1
00288A7B  8B 74 24 30                     mov esi, dword ptr [rsp + 0x30]
00288A7F  8B D6                           mov edx, esi
00288A81  E8 52 1F 00 00                  call 0x14028a9d8
00288A86  4C 8B E8                        mov r13, rax
00288A89  48 83 F8 02                     cmp rax, 2
00288A8D  0F 84 3A 06 00 00               je 0x1402890cd
00288A93  48 85 C0                        test rax, rax
00288A96  0F 85 53 07 00 00               jne 0x1402891ef
00288A9C  E9 58 07 00 00                  jmp 0x1402891f9
00288AA1  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
00288AA6  8B D7                           mov edx, edi
00288AA8  48 8B 88 88 3A 00 00            mov rcx, qword ptr [rax + 0x3a88]
00288AAF  E8 84 A6 01 00                  call 0x1402a3138
00288AB4  85 C0                           test eax, eax
00288AB6  0F 84 11 06 00 00               je 0x1402890cd
00288ABC  0F B6 45 E2                     movzx eax, byte ptr [rbp - 0x1e]
00288AC0  FE C0                           inc al
00288AC2  88 45 E2                        mov byte ptr [rbp - 0x1e], al
00288AC5  3A 45 E3                        cmp al, byte ptr [rbp - 0x1d]
00288AC8  0F 82 89 0C 00 00               jb 0x140289757
00288ACE  0F B6 45 E4                     movzx eax, byte ptr [rbp - 0x1c]
00288AD2  3C 02                           cmp al, 2
00288AD4  0F 84 EB 0A 00 00               je 0x1402895c5
00288ADA  0F B6 C0                        movzx eax, al
00288ADD  C1 E0 08                        shl eax, 8
00288AE0  33 C6                           xor eax, esi
00288AE2  25 00 01 00 00                  and eax, 0x100
00288AE7  33 F0                           xor esi, eax
00288AE9  89 74 24 30                     mov dword ptr [rsp + 0x30], esi
00288AED  4D 85 ED                        test r13, r13
00288AF0  0F 84 10 08 00 00               je 0x140289306
00288AF6  45 33 C9                        xor r9d, r9d
00288AF9  49 83 FD 02                     cmp r13, 2
00288AFD  0F 84 CA 05 00 00               je 0x1402890cd
00288B03  4D 85 ED                        test r13, r13
00288B06  0F 84 4E 05 00 00               je 0x14028905a
00288B0C  49 BC 00 00 00 00 00 DE FF FF   movabs r12, 0xffffde0000000000
00288B16  49 8B C4                        mov rax, r12
00288B19  49 8B F5                        mov rsi, r13
00288B1C  48 2B F0                        sub rsi, rax
00288B1F  48 B8 AB AA AA AA AA AA AA AA   movabs rax, 0xaaaaaaaaaaaaaaab
00288B29  48 C1 FE 04                     sar rsi, 4
00288B2D  48 0F AF F0                     imul rsi, rax
00288B31  4D 89 4D 00                     mov qword ptr [r13], r9
00288B35  41 8B C9                        mov ecx, r9d
00288B38  49 8B 45 28                     mov rax, qword ptr [r13 + 0x28]
00288B3C  48 0F BA E0 28                  bt rax, 0x28
00288B41  73 0A                           jae 0x140288b4d
00288B43  41 8B 4D 24                     mov ecx, dword ptr [r13 + 0x24]
00288B47  81 E1 00 00 00 18               and ecx, 0x18000000
00288B4D  41 89 4D 24                     mov dword ptr [r13 + 0x24], ecx
00288B51  48 63 0D 68 50 BA 00            movsxd rcx, dword ptr [rip + 0xba5068]
00288B58  8B 15 66 50 BA 00               mov edx, dword ptr [rip + 0xba5066]
00288B5E  3B CA                           cmp ecx, edx
00288B60  77 1D                           ja 0x140288b7f
00288B62  48 8B C1                        mov rax, rcx
00288B65  48 C1 E0 04                     shl rax, 4
00288B69  48 03 05 B0 50 BA 00            add rax, qword ptr [rip + 0xba50b0]
00288B70  48 3B 30                        cmp rsi, qword ptr [rax]
00288B73  72 0A                           jb 0x140288b7f
00288B75  3B CA                           cmp ecx, edx
00288B77  74 41                           je 0x140288bba
00288B79  48 3B 70 10                     cmp rsi, qword ptr [rax + 0x10]
00288B7D  72 3B                           jb 0x140288bba
00288B7F  45 8B C1                        mov r8d, r9d
00288B82  41 3B D0                        cmp edx, r8d
00288B85  0F 8C 19 01 00 00               jl 0x140288ca4
00288B8B  41 8D 0C 10                     lea ecx, [r8 + rdx]
00288B8F  D1 F9                           sar ecx, 1
00288B91  48 63 C1                        movsxd rax, ecx
00288B94  48 C1 E0 04                     shl rax, 4
00288B98  48 03 05 81 50 BA 00            add rax, qword ptr [rip + 0xba5081]
00288B9F  48 3B 30                        cmp rsi, qword ptr [rax]
00288BA2  0F 82 3B 07 00 00               jb 0x1402892e3
00288BA8  3B 0D 16 50 BA 00               cmp ecx, dword ptr [rip + 0xba5016]
00288BAE  0F 85 89 04 00 00               jne 0x14028903d
00288BB4  89 0D 06 50 BA 00               mov dword ptr [rip + 0xba5006], ecx
00288BBA  44 39 78 08                     cmp dword ptr [rax + 8], r15d
00288BBE  0F 85 41 0A 00 00               jne 0x140289605
00288BC4  48 83 3D 5C 50 BA 00 00         cmp qword ptr [rip + 0xba505c], 0
00288BCC  0F 85 B0 05 00 00               jne 0x140289182
00288BD2  32 C0                           xor al, al
00288BD4  44 0F B6 75 E4                  movzx r14d, byte ptr [rbp - 0x1c]
00288BD9  41 3A C6                        cmp al, r14b
00288BDC  0F 85 58 0B 00 00               jne 0x14028973a
00288BE2  40 F6 C7 20                     test dil, 0x20
00288BE6  74 31                           je 0x140288c19
00288BE8  49 8B 45 10                     mov rax, qword ptr [r13 + 0x10]
00288BEC  44 8B F3                        mov r14d, ebx
00288BEF  41 C1 EE 02                     shr r14d, 2
00288BF3  41 83 E6 03                     and r14d, 3
00288BF7  48 A9 E0 03 00 00               test rax, 0x3e0
00288BFD  0F 85 83 02 00 00               jne 0x140288e86
00288C03  41 8B 45 20                     mov eax, dword ptr [r13 + 0x20]
00288C07  C1 E8 10                        shr eax, 0x10
00288C0A  0F B6 C8                        movzx ecx, al
00288C0D  C1 E9 06                        shr ecx, 6
00288C10  41 3B CE                        cmp ecx, r14d
00288C13  0F 85 53 02 00 00               jne 0x140288e6c
00288C19  40 F6 C7 08                     test dil, 8
00288C1D  0F 84 F4 03 00 00               je 0x140289017
00288C23  48 8B C6                        mov rax, rsi
00288C26  48 8B 4D 08                     mov rcx, qword ptr [rbp + 8]
00288C2A  48 33 CC                        xor rcx, rsp
00288C2D  E8 0E 3A 42 00                  call 0x1406ac640
00288C32  48 8B 9C 24 68 01 00 00         mov rbx, qword ptr [rsp + 0x168]
00288C3A  48 81 C4 10 01 00 00            add rsp, 0x110
00288C41  41 5F                           pop r15
00288C43  41 5E                           pop r14
00288C45  41 5D                           pop r13
00288C47  41 5C                           pop r12
00288C49  5F                              pop rdi
00288C4A  5E                              pop rsi
00288C4B  5D                              pop rbp
00288C4C  C3                              ret
00288C4D  CC                              int3
00288C4E  41 8B D1                        mov edx, r9d
00288C51  E9 F4 F8 FF FF                  jmp 0x14028854a
00288C56  0F B6 4D E3                     movzx ecx, byte ptr [rbp - 0x1d]
00288C5A  C6 45 E2 00                     mov byte ptr [rbp - 0x1e], 0
00288C5E  80 F9 01                        cmp cl, 1
00288C61  0F 86 B3 F9 FF FF               jbe 0x14028861a
00288C67  41 0F B6 81 50 3B 00 00         movzx eax, byte ptr [r9 + 0x3b50]
00288C6F  F6 D0                           not al
00288C71  24 01                           and al, 1
00288C73  88 45 E5                        mov byte ptr [rbp - 0x1b], al
00288C76  41 0F B7 81 81 3B 00 00         movzx eax, word ptr [r9 + 0x3b81]
00288C7E  66 89 45 E0                     mov word ptr [rbp - 0x20], ax
00288C82  0F BA E7 0D                     bt edi, 0xd
00288C86  0F 83 8E F9 FF FF               jae 0x14028861a
00288C8C  44 0F B6 45 E4                  movzx r8d, byte ptr [rbp - 0x1c]
00288C91  48 8D 45 E0                     lea rax, [rbp - 0x20]
00288C95  32 D2                           xor dl, dl
00288C97  84 C9                           test cl, cl
00288C99  0F 85 C1 16 45 00               jne 0x1406da360
00288C9F  E9 D5 16 45 00                  jmp 0x1406da379
00288CA4  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
00288CA9  4C 8B C6                        mov r8, rsi
00288CAC  45 33 C9                        xor r9d, r9d
00288CAF  BA 80 51 00 00                  mov edx, 0x5180
00288CB4  41 8D 49 1A                     lea ecx, [r9 + 0x1a]
00288CB8  E8 A3 49 27 00                  call 0x1404fd660
00288CBD  CC                              int3
00288CBE  4C 8B 54 24 40                  mov r10, qword ptr [rsp + 0x40]
00288CC3  41 8B CA                        mov ecx, r10d
00288CC6  8B C3                           mov eax, ebx
00288CC8  44 8B D6                        mov r10d, esi
00288CCB  44 8B DE                        mov r11d, esi
00288CCE  25 0F F8 FF FF                  and eax, 0xfffff80f
00288CD3  41 C1 EA 10                     shr r10d, 0x10
00288CD7  41 C1 EB 0F                     shr r11d, 0xf
00288CDB  BA 10 00 00 00                  mov edx, 0x10
00288CE0  D3 E2                           shl edx, cl
00288CE2  41 83 E3 01                     and r11d, 1
00288CE6  0B D3                           or edx, ebx
00288CE8  44 89 5C 24 34                  mov dword ptr [rsp + 0x34], r11d
00288CED  81 E2 F0 00 00 00               and edx, 0xf0
00288CF3  41 83 E2 03                     and r10d, 3
00288CF7  8B DA                           mov ebx, edx
00288CF9  BE 01 00 00 00                  mov esi, 1
00288CFE  0B D8                           or ebx, eax
00288D00  33 FF                           xor edi, edi
00288D02  44 8B C3                        mov r8d, ebx
00288D05  8B D6                           mov edx, esi
00288D07  41 C1 E8 08                     shr r8d, 8
00288D0B  8B C3                           mov eax, ebx
00288D0D  41 83 E0 07                     and r8d, 7
00288D11  C1 E8 04                        shr eax, 4
00288D14  41 8B C8                        mov ecx, r8d
00288D17  D3 E2                           shl edx, cl
00288D19  23 D0                           and edx, eax
00288D1B  F6 C2 0F                        test dl, 0xf
00288D1E  0F 85 90 00 00 00               jne 0x140288db4
00288D24  41 8B C3                        mov eax, r11d
00288D27  4B 8D 14 92                     lea rdx, [r10 + r10*4]
00288D2B  48 C1 E2 08                     shl rdx, 8
00288D2F  49 03 D1                        add rdx, r9
00288D32  41 83 FA 03                     cmp r10d, 3
00288D36  0F 44 C7                        cmove eax, edi
00288D39  49 8D 0C 80                     lea rcx, [r8 + rax*4]
00288D3D  48 8B 44 CA 18                  mov rax, qword ptr [rdx + rcx*8 + 0x18]
00288D42  48 85 C0                        test rax, rax
00288D45  0F 85 8A 00 00 00               jne 0x140288dd5
00288D4B  49 8B 81 60 3B 00 00            mov rax, qword ptr [r9 + 0x3b60]
00288D52  66 85 C0                        test ax, ax
00288D55  75 7E                           jne 0x140288dd5
00288D57  8B D7                           mov edx, edi
00288D59  41 3B D2                        cmp edx, r10d
00288D5C  77 22                           ja 0x140288d80
00288D5E  8B C2                           mov eax, edx
00288D60  48 8D 0C 80                     lea rcx, [rax + rax*4]
00288D64  48 C1 E1 08                     shl rcx, 8
00288D68  4A 8B 44 09 08                  mov rax, qword ptr [rcx + r9 + 8]
00288D6D  48 85 C0                        test rax, rax
00288D70  75 63                           jne 0x140288dd5
00288D72  4A 8B 44 09 10                  mov rax, qword ptr [rcx + r9 + 0x10]
00288D77  48 85 C0                        test rax, rax
00288D7A  75 59                           jne 0x140288dd5
00288D7C  FF C2                           inc edx
00288D7E  EB D9                           jmp 0x140288d59
00288D80  41 83 FA 03                     cmp r10d, 3
00288D84  75 0C                           jne 0x140288d92
00288D86  45 22 C2                        and r8b, r10b
00288D89  44 3A C6                        cmp r8b, sil
00288D8C  0F 84 66 03 00 00               je 0x1402890f8
00288D92  8B CB                           mov ecx, ebx
00288D94  8B C3                           mov eax, ebx
00288D96  C1 E9 08                        shr ecx, 8
00288D99  BA 10 00 00 00                  mov edx, 0x10
00288D9E  83 E1 07                        and ecx, 7
00288DA1  25 0F FF FF FF                  and eax, 0xffffff0f
00288DA6  D3 E2                           shl edx, cl
00288DA8  0B D3                           or edx, ebx
00288DAA  81 E2 F0 00 00 00               and edx, 0xf0
00288DB0  8B DA                           mov ebx, edx
00288DB2  33 D8                           xor ebx, eax
00288DB4  8D 83 00 01 00 00               lea eax, [rbx + 0x100]
00288DBA  33 C3                           xor eax, ebx
00288DBC  25 00 07 00 00                  and eax, 0x700
00288DC1  33 D8                           xor ebx, eax
00288DC3  8B C3                           mov eax, ebx
00288DC5  25 00 07 00 00                  and eax, 0x700
00288DCA  3D 00 03 00 00                  cmp eax, 0x300
00288DCF  0F 86 2D FF FF FF               jbe 0x140288d02
00288DD5  8B 7D 88                        mov edi, dword ptr [rbp - 0x78]
00288DD8  8B C3                           mov eax, ebx
00288DDA  8B 74 24 30                     mov esi, dword ptr [rsp + 0x30]
00288DDE  25 F0 00 00 00                  and eax, 0xf0
00288DE3  3C F0                           cmp al, 0xf0
00288DE5  0F 85 53 05 00 00               jne 0x14028933e
00288DEB  44 8B 44 24 58                  mov r8d, dword ptr [rsp + 0x58]
00288DF0  8B D3                           mov edx, ebx
00288DF2  45 85 C0                        test r8d, r8d
00288DF5  75 3A                           jne 0x140288e31
00288DF7  83 7C 24 38 03                  cmp dword ptr [rsp + 0x38], 3
00288DFC  B9 60 3B 00 00                  mov ecx, 0x3b60
00288E01  B8 58 3B 00 00                  mov eax, 0x3b58
00288E06  0F 45 C1                        cmovne eax, ecx
00288E09  33 C9                           xor ecx, ecx
00288E0B  49 03 C1                        add rax, r9
00288E0E  48 89 45 98                     mov qword ptr [rbp - 0x68], rax
00288E12  48 8B 00                        mov rax, qword ptr [rax]
00288E15  66 85 C0                        test ax, ax
00288E18  0F 85 CB 06 00 00               jne 0x1402894e9
00288E1E  48 8B C8                        mov rcx, rax
00288E21  49 33 CC                        xor rcx, r12
00288E24  48 F7 C1 00 00 FF FF            test rcx, -0x10000
00288E2B  0F 85 1B 03 00 00               jne 0x14028914c
00288E31  8B C3                           mov eax, ebx
00288E33  C1 E8 02                        shr eax, 2
00288E36  33 C3                           xor eax, ebx
00288E38  83 E0 03                        and eax, 3
00288E3B  33 D8                           xor ebx, eax
00288E3D  45 85 C0                        test r8d, r8d
00288E40  0F 84 18 03 00 00               je 0x14028915e
00288E46  41 BB 01 00 00 00               mov r11d, 1
00288E4C  8B CB                           mov ecx, ebx
00288E4E  41 8B C3                        mov eax, r11d
00288E51  C1 E9 02                        shr ecx, 2
00288E54  83 E1 03                        and ecx, 3
00288E57  D3 E0                           shl eax, cl
00288E59  F7 D0                           not eax
00288E5B  C1 E0 04                        shl eax, 4
00288E5E  33 C3                           xor eax, ebx
00288E60  25 F0 00 00 00                  and eax, 0xf0
00288E65  33 D8                           xor ebx, eax
00288E67  E9 FE 02 00 00                  jmp 0x14028916a
00288E6C  B8 01 00 00 00                  mov eax, 1
00288E71  D2 E0                           shl al, cl
00288E73  0F B6 C0                        movzx eax, al
00288E76  44 0F AB F0                     bts eax, r14d
00288E7A  84 05 58 4E BA 00               test byte ptr [rip + 0xba4e58], al
00288E80  0F 84 93 FD FF FF               je 0x140288c19
00288E86  44 8B 7C 24 30                  mov r15d, dword ptr [rsp + 0x30]
00288E8B  8D 04 FD 00 00 00 00            lea eax, [rdi*8]
00288E92  41 C1 EF 10                     shr r15d, 0x10
00288E96  8B D8                           mov ebx, eax
00288E98  83 CB 01                        or ebx, 1
00288E9B  41 83 E7 03                     and r15d, 3
00288E9F  40 F6 C7 20                     test dil, 0x20
00288EA3  0F 44 D8                        cmove ebx, eax
00288EA6  49 8B C4                        mov rax, r12
00288EA9  49 8B FD                        mov rdi, r13
00288EAC  48 2B F8                        sub rdi, rax
00288EAF  48 B8 AB AA AA AA AA AA AA AA   movabs rax, 0xaaaaaaaaaaaaaaab
00288EB9  48 C1 FF 04                     sar rdi, 4
00288EBD  48 0F AF F8                     imul rdi, rax
00288EC1  8B C3                           mov eax, ebx
00288EC3  83 E0 08                        and eax, 8
00288EC6  83 C8 04                        or eax, 4
00288EC9  8D 14 00                        lea edx, [rax + rax]
00288ECC  41 8B 45 20                     mov eax, dword ptr [r13 + 0x20]
00288ED0  C1 E8 10                        shr eax, 0x10
00288ED3  24 C0                           and al, 0xc0
00288ED5  89 54 24 38                     mov dword ptr [rsp + 0x38], edx
00288ED9  3C C0                           cmp al, 0xc0
00288EDB  0F 84 BC 09 00 00               je 0x14028989d
00288EE1  41 8B 45 20                     mov eax, dword ptr [r13 + 0x20]
00288EE5  C1 E8 10                        shr eax, 0x10
00288EE8  0F B6 C8                        movzx ecx, al
00288EEB  33 C0                           xor eax, eax
00288EED  C1 E9 06                        shr ecx, 6
00288EF0  41 3B CE                        cmp ecx, r14d
00288EF3  0F 95 C0                        setne al
00288EF6  44 8B E0                        mov r12d, eax
00288EF9  F6 C3 01                        test bl, 1
00288EFC  74 3B                           je 0x140288f39
00288EFE  41 3B CE                        cmp ecx, r14d
00288F01  0F 85 D0 06 00 00               jne 0x1402895d7
00288F07  33 C9                           xor ecx, ecx
00288F09  45 8B CE                        mov r9d, r14d
00288F0C  41 83 FF 03                     cmp r15d, 3
00288F10  0F 85 AA 09 00 00               jne 0x1402898c0
00288F16  C1 EB 02                        shr ebx, 2
00288F19  48 8B D7                        mov rdx, rdi
00288F1C  83 E3 02                        and ebx, 2
00288F1F  44 8B C3                        mov r8d, ebx
00288F22  E8 69 96 0A 00                  call 0x140332590
00288F27  49 8B 45 10                     mov rax, qword ptr [r13 + 0x10]
00288F2B  8B 54 24 38                     mov edx, dword ptr [rsp + 0x38]
00288F2F  48 25 1F FC FF FF               and rax, 0xfffffffffffffc1f
00288F35  49 89 45 10                     mov qword ptr [r13 + 0x10], rax
00288F39  45 85 E4                        test r12d, r12d
00288F3C  0F 84 E1 FC FF FF               je 0x140288c23
00288F42  44 8B C2                        mov r8d, edx
00288F45  49 8B CD                        mov rcx, r13
00288F48  41 8B D6                        mov edx, r14d
00288F4B  E8 7C 9F 0A 00                  call 0x140332ecc
00288F50  E9 CE FC FF FF                  jmp 0x140288c23
00288F55  8B C7                           mov eax, edi
00288F57  D1 E8                           shr eax, 1
00288F59  0B C7                           or eax, edi
00288F5B  A8 01                           test al, 1
00288F5D  0F 84 7F 04 00 00               je 0x1402893e2
00288F63  C6 45 80 11                     mov byte ptr [rbp - 0x80], 0x11
00288F67  4C 8B 44 24 60                  mov r8, qword ptr [rsp + 0x60]
00288F6C  41 BB 01 00 00 00               mov r11d, 1
00288F72  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
00288F77  4D 8B C8                        mov r9, r8
00288F7A  41 83 E1 1F                     and r9d, 0x1f
00288F7E  49 8B C8                        mov rcx, r8
00288F81  48 C1 E9 05                     shr rcx, 5
00288F85  41 8B D3                        mov edx, r11d
00288F88  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00288F8C  4C 8D 14 88                     lea r10, [rax + rcx*4]
00288F90  49 8D 41 01                     lea rax, [r9 + 1]
00288F94  48 83 F8 20                     cmp rax, 0x20
00288F98  0F 87 EA 04 00 00               ja 0x140289488
00288F9E  41 8B C9                        mov ecx, r9d
00288FA1  41 8B C3                        mov eax, r11d
00288FA4  D3 E0                           shl eax, cl
00288FA6  F7 D0                           not eax
00288FA8  F0 41 21 02                     lock and dword ptr [r10], eax
00288FAC  49 8B C8                        mov rcx, r8
00288FAF  48 C1 E1 04                     shl rcx, 4
00288FB3  48 03 4D 98                     add rcx, qword ptr [rbp - 0x68]
00288FB7  E8 B4 15 43 00                  call 0x1406ba570
00288FBC  4C 8B E8                        mov r13, rax
00288FBF  48 85 C0                        test rax, rax
00288FC2  0F 85 8A 05 00 00               jne 0x140289552
00288FC8  4C 8B 6D 80                     mov r13, qword ptr [rbp - 0x80]
00288FCC  41 80 FD 11                     cmp r13b, 0x11
00288FD0  74 1D                           je 0x140288fef
00288FD2  39 05 48 DD D3 00               cmp dword ptr [rip + 0xd3dd48], eax
00288FD8  74 0D                           je 0x140288fe7
00288FDA  44 0F 20 C1                     mov rcx, cr8
00288FDE  41 0F B6 D5                     movzx edx, r13b
00288FE2  E8 B1 C6 26 00                  call 0x1404f5698
00288FE7  41 0F B6 C5                     movzx eax, r13b
00288FEB  44 0F 22 C0                     mov cr8, rax
00288FEF  4C 8B 44 24 60                  mov r8, qword ptr [rsp + 0x60]
00288FF4  4C 8B 4C 24 50                  mov r9, qword ptr [rsp + 0x50]
00288FF9  8B 4C 24 48                     mov ecx, dword ptr [rsp + 0x48]
00288FFD  48 8B 45 C0                     mov rax, qword ptr [rbp - 0x40]
00289001  8B 50 04                        mov edx, dword ptr [rax + 4]
00289004  3B CA                           cmp ecx, edx
00289006  0F 84 A4 F8 FF FF               je 0x1402888b0
0028900C  8B CA                           mov ecx, edx
0028900E  89 54 24 48                     mov dword ptr [rsp + 0x48], edx
00289012  E9 1A F8 FF FF                  jmp 0x140288831
00289017  41 8B 45 20                     mov eax, dword ptr [r13 + 0x20]
0028901B  44 8B F3                        mov r14d, ebx
0028901E  C1 E8 10                        shr eax, 0x10
00289021  41 C1 EE 02                     shr r14d, 2
00289025  0F B6 C0                        movzx eax, al
00289028  41 83 E6 03                     and r14d, 3
0028902C  C1 E8 06                        shr eax, 6
0028902F  41 3B C6                        cmp eax, r14d
00289032  0F 84 EB FB FF FF               je 0x140288c23
00289038  E9 49 FE FF FF                  jmp 0x140288e86
0028903D  48 3B 70 10                     cmp rsi, qword ptr [rax + 0x10]
00289041  0F 82 6D FB FF FF               jb 0x140288bb4
00289047  44 8D 41 01                     lea r8d, [rcx + 1]
0028904B  E9 32 FB FF FF                  jmp 0x140288b82
00289050  E8 47 19 00 00                  call 0x14028a99c
00289055  E9 4A F8 FF FF                  jmp 0x1402888a4
0028905A  40 F6 C7 02                     test dil, 2
0028905E  75 6D                           jne 0x1402890cd
00289060  0F BA E7 10                     bt edi, 0x10
00289064  72 67                           jb 0x1402890cd
00289066  48 8B 75 90                     mov rsi, qword ptr [rbp - 0x70]
0028906A  F7 C7 00 30 00 00               test edi, 0x3000
00289070  0F 85 2C 07 00 00               jne 0x1402897a2
00289076  44 8B C7                        mov r8d, edi
00289079  BA 08 00 00 00                  mov edx, 8
0028907E  48 8B CE                        mov rcx, rsi
00289081  E8 7A B5 0A 00                  call 0x140334600
00289086  48 8B F0                        mov rsi, rax
00289089  48 83 F8 FF                     cmp rax, -1
0028908D  74 3E                           je 0x1402890cd
0028908F  4C 8D 2C 40                     lea r13, [rax + rax*2]
00289093  49 BC 00 00 00 00 00 DE FF FF   movabs r12, 0xffffde0000000000
0028909D  49 C1 E5 04                     shl r13, 4
002890A1  49 8B CC                        mov rcx, r12
002890A4  4C 03 E9                        add r13, rcx
002890A7  45 33 C9                        xor r9d, r9d
002890AA  E9 82 FA FF FF                  jmp 0x140288b31
002890AF  48 8B 05 D2 D9 D3 00            mov rax, qword ptr [rip + 0xd3d9d2]
002890B6  A8 30                           test al, 0x30
002890B8  0F 84 2E F5 FF FF               je 0x1402885ec
002890BE  8B D7                           mov edx, edi
002890C0  E8 73 A0 01 00                  call 0x1402a3138
002890C5  85 C0                           test eax, eax
002890C7  0F 85 B9 06 00 00               jne 0x140289786
002890CD  48 C7 C0 FF FF FF FF            mov rax, 0xffffffffffffffff
002890D4  E9 4D FB FF FF                  jmp 0x140288c26
002890D9  8B 45 A0                        mov eax, dword ptr [rbp - 0x60]
002890DC  48 8D 14 B0                     lea rdx, [rax + rsi*4]
002890E0  8B F7                           mov esi, edi
002890E2  48 C1 E2 05                     shl rdx, 5
002890E6  48 81 C2 90 00 00 00            add rdx, 0x90
002890ED  49 03 D0                        add rdx, r8
002890F0  83 CE 10                        or esi, 0x10
002890F3  E9 1F F8 FF FF                  jmp 0x140288917
002890F8  44 8B 1D CD 4B BA 00            mov r11d, dword ptr [rip + 0xba4bcd]
002890FF  44 8B C7                        mov r8d, edi
00289102  41 83 F8 02                     cmp r8d, 2
00289106  0F 83 B3 06 00 00               jae 0x1402897bf
0028910C  41 8B C0                        mov eax, r8d
0028910F  49 8B D3                        mov rdx, r11
00289112  48 05 A0 03 00 00               add rax, 0x3a0
00289118  48 03 C0                        add rax, rax
0028911B  49 8B 0C C1                     mov rcx, qword ptr [r9 + rax*8]
0028911F  48 85 C9                        test rcx, rcx
00289122  0F 84 AD FC FF FF               je 0x140288dd5
00289128  48 3B D6                        cmp rdx, rsi
0028912B  0F 87 24 02 00 00               ja 0x140289355
00289131  0F 85 9E FC FF FF               jne 0x140288dd5
00289137  49 8B 44 C1 08                  mov rax, qword ptr [r9 + rax*8 + 8]
0028913C  48 0F BA 20 00                  bt qword ptr [rax], 0
00289141  0F 82 8E FC FF FF               jb 0x140288dd5
00289147  41 FF C0                        inc r8d
0028914A  EB B6                           jmp 0x140289102
0028914C  8B DA                           mov ebx, edx
0028914E  41 FF CE                        dec r14d
00289151  C1 EB 02                        shr ebx, 2
00289154  4C 8B E0                        mov r12, rax
00289157  33 DA                           xor ebx, edx
00289159  83 E3 03                        and ebx, 3
0028915C  33 DA                           xor ebx, edx
0028915E  41 BB 01 00 00 00               mov r11d, 1
00289164  81 E3 0F FF FF FF               and ebx, 0xffffff0f
0028916A  8B 54 24 78                     mov edx, dword ptr [rsp + 0x78]
0028916E  41 FF C6                        inc r14d
00289171  44 8B 44 24 38                  mov r8d, dword ptr [rsp + 0x38]
00289176  45 33 C9                        xor r9d, r9d
00289179  4C 8B 55 A8                     mov r10, qword ptr [rbp - 0x58]
0028917D  E9 15 F4 FF FF                  jmp 0x140288597
00289182  49 8B C4                        mov rax, r12
00289185  49 8B CD                        mov rcx, r13
00289188  48 2B C8                        sub rcx, rax
0028918B  48 B8 AB AA AA AA AA AA AA AA   movabs rax, 0xaaaaaaaaaaaaaaab
00289195  48 C1 F9 04                     sar rcx, 4
00289199  48 0F AF C8                     imul rcx, rax
0028919D  E8 A6 09 03 00                  call 0x1402b9b48
002891A2  E9 2D FA FF FF                  jmp 0x140288bd4
002891A7  8B 54 24 30                     mov edx, dword ptr [rsp + 0x30]
002891AB  83 E6 BF                        and esi, 0xffffffbf
002891AE  8B C2                           mov eax, edx
002891B0  25 00 00 03 00                  and eax, 0x30000
002891B5  3D 00 00 03 00                  cmp eax, 0x30000
002891BA  0F 85 9F F8 FF FF               jne 0x140288a5f
002891C0  8B C2                           mov eax, edx
002891C2  25 00 00 0C 00                  and eax, 0xc0000
002891C7  3D 00 00 04 00                  cmp eax, 0x40000
002891CC  0F 85 8D F8 FF FF               jne 0x140288a5f
002891D2  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
002891D7  44 8B C6                        mov r8d, esi
002891DA  E8 BD 25 00 00                  call 0x14028b79c
002891DF  4C 8B E8                        mov r13, rax
002891E2  48 85 C0                        test rax, rax
002891E5  0F 84 74 F8 FF FF               je 0x140288a5f
002891EB  8B 74 24 30                     mov esi, dword ptr [rsp + 0x30]
002891EF  49 83 FD 02                     cmp r13, 2
002891F3  0F 83 FD F8 FF FF               jae 0x140288af6
002891F9  8B C7                           mov eax, edi
002891FB  8B CF                           mov ecx, edi
002891FD  83 C8 10                        or eax, 0x10
00289200  83 E1 EF                        and ecx, 0xffffffef
00289203  83 7C 24 70 00                  cmp dword ptr [rsp + 0x70], 0
00289208  0F 44 C8                        cmove ecx, eax
0028920B  33 C0                           xor eax, eax
0028920D  44 8B C8                        mov r9d, eax
00289210  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
00289214  8B C6                           mov eax, esi
00289216  89 4C 24 48                     mov dword ptr [rsp + 0x48], ecx
0028921A  25 00 00 03 00                  and eax, 0x30000
0028921F  3D 00 00 03 00                  cmp eax, 0x30000
00289224  0F 94 C1                        sete cl
00289227  40 F6 C7 02                     test dil, 2
0028922B  0F 94 C0                        sete al
0028922E  84 C8                           test al, cl
00289230  0F 84 FA 01 00 00               je 0x140289430
00289236  8B CE                           mov ecx, esi
00289238  C1 E9 12                        shr ecx, 0x12
0028923B  83 E1 03                        and ecx, 3
0028923E  8D 41 FF                        lea eax, [rcx - 1]
00289241  83 F8 01                        cmp eax, 1
00289244  0F 87 E6 01 00 00               ja 0x140289430
0028924A  E8 FD 0E 00 00                  call 0x14028a14c
0028924F  85 C0                           test eax, eax
00289251  74 2F                           je 0x140289282
00289253  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
00289258  8B D3                           mov edx, ebx
0028925A  C1 E2 10                        shl edx, 0x10
0028925D  44 8B C7                        mov r8d, edi
00289260  33 D6                           xor edx, esi
00289262  81 E2 00 00 0C 00               and edx, 0xc0000
00289268  48 8B 88 88 3A 00 00            mov rcx, qword ptr [rax + 0x3a88]
0028926F  33 D6                           xor edx, esi
00289271  E8 7A 12 00 00                  call 0x14028a4f0
00289276  4C 8B E8                        mov r13, rax
00289279  48 85 C0                        test rax, rax
0028927C  0F 85 DF 01 00 00               jne 0x140289461
00289282  8B 44 24 34                     mov eax, dword ptr [rsp + 0x34]
00289286  44 8B CB                        mov r9d, ebx
00289289  44 8B 44 24 48                  mov r8d, dword ptr [rsp + 0x48]
0028928E  8B D6                           mov edx, esi
00289290  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
00289295  41 C1 E9 02                     shr r9d, 2
00289299  41 83 E1 03                     and r9d, 3
0028929D  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
002892A1  E8 32 C0 1A 00                  call 0x1404352d8
002892A6  4C 8B E8                        mov r13, rax
002892A9  48 83 F8 02                     cmp rax, 2
002892AD  0F 83 43 F8 FF FF               jae 0x140288af6
002892B3  E9 E9 F7 FF FF                  jmp 0x140288aa1
002892B8  8B D1                           mov edx, ecx
002892BA  44 8B C7                        mov r8d, edi
002892BD  49 8B C9                        mov rcx, r9
002892C0  E8 D7 24 00 00                  call 0x14028b79c
002892C5  4C 8B E8                        mov r13, rax
002892C8  48 85 C0                        test rax, rax
002892CB  0F 85 1A FF FF FF               jne 0x1402891eb
002892D1  8B 4C 24 30                     mov ecx, dword ptr [rsp + 0x30]
002892D5  E9 50 F7 FF FF                  jmp 0x140288a2a
002892DA  8B 74 24 30                     mov esi, dword ptr [rsp + 0x30]
002892DE  E9 16 FF FF FF                  jmp 0x1402891f9
002892E3  85 C9                           test ecx, ecx
002892E5  0F 85 AA 05 00 00               jne 0x140289895
002892EB  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
002892F0  4C 8B C6                        mov r8, rsi
002892F3  4C 8B C8                        mov r9, rax
002892F6  BA 80 51 00 00                  mov edx, 0x5180
002892FB  B9 1A 00 00 00                  mov ecx, 0x1a
00289300  E8 5B 43 27 00                  call 0x1404fd660
00289305  CC                              int3
00289306  8B CB                           mov ecx, ebx
00289308  B8 10 00 00 00                  mov eax, 0x10
0028930D  83 E1 03                        and ecx, 3
00289310  D3 E0                           shl eax, cl
00289312  0B D8                           or ebx, eax
00289314  8B 44 24 40                     mov eax, dword ptr [rsp + 0x40]
00289318  25 0F FF FF FF                  and eax, 0xffffff0f
0028931D  81 E3 F0 00 00 00               and ebx, 0xf0
00289323  33 D8                           xor ebx, eax
00289325  8B C3                           mov eax, ebx
00289327  25 F0 00 00 00                  and eax, 0xf0
0028932C  3C F0                           cmp al, 0xf0
0028932E  0F 85 46 01 00 00               jne 0x14028947a
00289334  4C 8B 4C 24 50                  mov r9, qword ptr [rsp + 0x50]
00289339  E9 AD FA FF FF                  jmp 0x140288deb
0028933E  8B C3                           mov eax, ebx
00289340  41 B8 01 00 00 00               mov r8d, 1
00289346  C1 E8 08                        shr eax, 8
00289349  33 C3                           xor eax, ebx
0028934B  83 E0 03                        and eax, 3
0028934E  33 D8                           xor ebx, eax
00289350  E9 47 F4 FF FF                  jmp 0x14028879c
00289355  48 3B CA                        cmp rcx, rdx
00289358  0F 82 77 FA FF FF               jb 0x140288dd5
0028935E  49 8B 4C C1 08                  mov rcx, qword ptr [r9 + rax*8 + 8]
00289363  49 8D 43 FF                     lea rax, [r11 - 1]
00289367  48 C1 E8 06                     shr rax, 6
0028936B  48 8D 04 C1                     lea rax, [rcx + rax*8]
0028936F  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00289374  48 8B 01                        mov rax, qword ptr [rcx]
00289377  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
0028937C  48 3B 4C 24 60                  cmp rcx, qword ptr [rsp + 0x60]
00289381  0F 85 19 01 00 00               jne 0x1402894a0
00289387  B9 40 00 00 00                  mov ecx, 0x40
0028938C  48 C7 C0 FF FF FF FF            mov rax, 0xffffffffffffffff
00289393  2A CA                           sub cl, dl
00289395  48 D3 E8                        shr rax, cl
00289398  48 85 44 24 68                  test qword ptr [rsp + 0x68], rax
0028939D  0F 94 C0                        sete al
002893A0  84 C0                           test al, al
002893A2  0F 84 2D FA FF FF               je 0x140288dd5
002893A8  E9 9A FD FF FF                  jmp 0x140289147
002893AD  8B 54 24 30                     mov edx, dword ptr [rsp + 0x30]
002893B1  45 33 C9                        xor r9d, r9d
002893B4  49 8B 8D 88 3A 00 00            mov rcx, qword ptr [r13 + 0x3a88]
002893BB  44 8B C7                        mov r8d, edi
002893BE  E8 15 16 00 00                  call 0x14028a9d8
002893C3  4C 8B E8                        mov r13, rax
002893C6  48 83 F8 02                     cmp rax, 2
002893CA  0F 83 26 F7 FF FF               jae 0x140288af6
002893D0  4C 8B 6C 24 50                  mov r13, qword ptr [rsp + 0x50]
002893D5  E9 89 F5 FF FF                  jmp 0x140288963
002893DA  49 8B D1                        mov rdx, r9
002893DD  E9 30 F5 FF FF                  jmp 0x140288912
002893E2  45 0F 20 C3                     mov r11, cr8
002893E6  4C 89 5D 80                     mov qword ptr [rbp - 0x80], r11
002893EA  B8 02 00 00 00                  mov eax, 2
002893EF  44 0F 22 C0                     mov cr8, rax
002893F3  83 3D 26 D9 D3 00 00            cmp dword ptr [rip + 0xd3d926], 0
002893FA  0F 84 67 FB FF FF               je 0x140288f67
00289400  0F B6 D0                        movzx edx, al
00289403  41 0F B6 CB                     movzx ecx, r11b
00289407  E8 F0 C2 26 00                  call 0x1404f56fc
0028940C  E9 56 FB FF FF                  jmp 0x140288f67
00289411  48 85 C0                        test rax, rax
00289414  0F 85 5F F3 FF FF               jne 0x140288779
0028941A  48 8B 51 08                     mov rdx, qword ptr [rcx + 8]
0028941E  48 83 C1 08                     add rcx, 8
00289422  49 3B C8                        cmp rcx, r8
00289425  0F 84 A6 00 00 00               je 0x1402894d1
0028942B  48 85 D2                        test rdx, rdx
0028942E  EB E4                           jmp 0x140289414
00289430  44 39 4C 24 58                  cmp dword ptr [rsp + 0x58], r9d
00289435  B8 01 00 00 00                  mov eax, 1
0028943A  44 0F 44 C8                     cmove r9d, eax
0028943E  44 89 4C 24 34                  mov dword ptr [rsp + 0x34], r9d
00289443  E9 3A FE FF FF                  jmp 0x140289282
00289448  48 8B 40 10                     mov rax, qword ptr [rax + 0x10]
0028944C  49 8B CD                        mov rcx, r13
0028944F  E8 F4 BF 1A 00                  call 0x140435448
00289454  85 C0                           test eax, eax
00289456  0F 85 9A F6 FF FF               jne 0x140288af6
0028945C  E9 92 F5 FF FF                  jmp 0x1402889f3
00289461  48 8B 40 10                     mov rax, qword ptr [rax + 0x10]
00289465  49 8B CD                        mov rcx, r13
00289468  E8 DB BF 1A 00                  call 0x140435448
0028946D  85 C0                           test eax, eax
0028946F  0F 85 81 F6 FF FF               jne 0x140288af6
00289475  E9 08 FE FF FF                  jmp 0x140289282
0028947A  41 FF CE                        dec r14d
0028947D  41 BB 01 00 00 00               mov r11d, 1
00289483  E9 E2 FC FF FF                  jmp 0x14028916a
00289488  4D 85 C9                        test r9, r9
0028948B  0F 85 47 03 00 00               jne 0x1402897d8
00289491  48 8B CA                        mov rcx, rdx
00289494  B8 FF FF FF FF                  mov eax, 0xffffffff
00289499  D3 E0                           shl eax, cl
0028949B  E9 08 FB FF FF                  jmp 0x140288fa8
002894A0  48 85 C0                        test rax, rax
002894A3  0F 85 2C F9 FF FF               jne 0x140288dd5
002894A9  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
002894AE  4C 8B 79 08                     mov r15, qword ptr [rcx + 8]
002894B2  48 83 C1 08                     add rcx, 8
002894B6  4C 89 7C 24 60                  mov qword ptr [rsp + 0x60], r15
002894BB  44 8B 7C 24 74                  mov r15d, dword ptr [rsp + 0x74]
002894C0  48 3B C8                        cmp rcx, rax
002894C3  74 73                           je 0x140289538
002894C5  48 39 7C 24 60                  cmp qword ptr [rsp + 0x60], rdi
002894CA  74 E2                           je 0x1402894ae
002894CC  E9 04 F9 FF FF                  jmp 0x140288dd5
002894D1  41 0F B6 CA                     movzx ecx, r10b
002894D5  48 C7 C0 FF FF FF FF            mov rax, 0xffffffffffffffff
002894DC  F6 D1                           not cl
002894DE  48 D3 E8                        shr rax, cl
002894E1  48 85 D0                        test rax, rdx
002894E4  E9 89 F2 FF FF                  jmp 0x140288772
002894E9  48 8B 75 98                     mov rsi, qword ptr [rbp - 0x68]
002894ED  44 8B F9                        mov r15d, ecx
002894F0  41 FF C7                        inc r15d
002894F3  44 85 3D B2 BD D3 00            test dword ptr [rip + 0xd3bdb2], r15d
002894FA  0F 84 98 01 00 00               je 0x140289698
00289500  F3 90                           pause
00289502  48 8B 06                        mov rax, qword ptr [rsi]
00289505  66 85 C0                        test ax, ax
00289508  75 E6                           jne 0x1402894f0
0028950A  44 8B 7C 24 74                  mov r15d, dword ptr [rsp + 0x74]
0028950F  8B D3                           mov edx, ebx
00289511  8B 74 24 30                     mov esi, dword ptr [rsp + 0x30]
00289515  44 8B 44 24 58                  mov r8d, dword ptr [rsp + 0x58]
0028951A  E9 FF F8 FF FF                  jmp 0x140288e1e
0028951F  8B CB                           mov ecx, ebx
00289521  41 8B C3                        mov eax, r11d
00289524  C1 E9 02                        shr ecx, 2
00289527  D3 E0                           shl eax, cl
00289529  F7 D0                           not eax
0028952B  83 E0 0F                        and eax, 0xf
0028952E  C1 E0 04                        shl eax, 4
00289531  0B D8                           or ebx, eax
00289533  E9 E9 EF FF FF                  jmp 0x140288521
00289538  49 8D 4B FF                     lea rcx, [r11 - 1]
0028953C  48 C7 C0 FF FF FF FF            mov rax, 0xffffffffffffffff
00289543  F6 D1                           not cl
00289545  48 D3 E8                        shr rax, cl
00289548  48 85 44 24 60                  test qword ptr [rsp + 0x60], rax
0028954D  E9 4B FE FF FF                  jmp 0x14028939d
00289552  44 8B 44 24 34                  mov r8d, dword ptr [rsp + 0x34]
00289557  41 BB 01 00 00 00               mov r11d, 1
0028955D  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
00289562  41 8B C8                        mov ecx, r8d
00289565  48 C1 E9 05                     shr rcx, 5
00289569  41 8B D3                        mov edx, r11d
0028956C  45 8B D0                        mov r10d, r8d
0028956F  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00289573  4C 8D 0C 88                     lea r9, [rax + rcx*4]
00289577  41 8B C8                        mov ecx, r8d
0028957A  83 E1 1F                        and ecx, 0x1f
0028957D  48 8D 41 01                     lea rax, [rcx + 1]
00289581  48 83 F8 20                     cmp rax, 0x20
00289585  0F 87 F5 00 00 00               ja 0x140289680
0028958B  41 8B C3                        mov eax, r11d
0028958E  D3 E0                           shl eax, cl
00289590  F0 41 09 01                     lock or dword ptr [r9], eax
00289594  48 8B 45 80                     mov rax, qword ptr [rbp - 0x80]
00289598  3C 11                           cmp al, 0x11
0028959A  0F 84 DC F2 FF FF               je 0x14028887c
002895A0  83 3D 79 D7 D3 00 00            cmp dword ptr [rip + 0xd3d779], 0
002895A7  74 10                           je 0x1402895b9
002895A9  44 0F 20 C1                     mov rcx, cr8
002895AD  0F B6 D0                        movzx edx, al
002895B0  E8 E3 C0 26 00                  call 0x1404f5698
002895B5  48 8B 45 80                     mov rax, qword ptr [rbp - 0x80]
002895B9  0F B6 C0                        movzx eax, al
002895BC  44 0F 22 C0                     mov cr8, rax
002895C0  E9 B7 F2 FF FF                  jmp 0x14028887c
002895C5  8B CE                           mov ecx, esi
002895C7  C1 E9 09                        shr ecx, 9
002895CA  83 E1 3F                        and ecx, 0x3f
002895CD  E8 DE 4F 09 00                  call 0x14031e5b0
002895D2  E9 03 F5 FF FF                  jmp 0x140288ada
002895D7  41 8B D6                        mov edx, r14d
002895DA  49 8B CD                        mov rcx, r13
002895DD  E8 1E F0 03 00                  call 0x1402c8600
002895E2  41 3B C6                        cmp eax, r14d
002895E5  0F 85 1C F9 FF FF               jne 0x140288f07
002895EB  44 8B 44 24 38                  mov r8d, dword ptr [rsp + 0x38]
002895F0  41 8B D6                        mov edx, r14d
002895F3  49 8B CD                        mov rcx, r13
002895F6  E8 D1 98 0A 00                  call 0x140332ecc
002895FB  33 C0                           xor eax, eax
002895FD  44 8B E0                        mov r12d, eax
00289600  E9 02 F9 FF FF                  jmp 0x140288f07
00289605  44 0F B6 65 E5                  movzx r12d, byte ptr [rbp - 0x1b]
0028960A  44 0F B6 75 E4                  movzx r14d, byte ptr [rbp - 0x1c]
0028960F  40 F6 C7 02                     test dil, 2
00289613  0F 85 2F 01 00 00               jne 0x140289748
00289619  0F BA E7 11                     bt edi, 0x11
0028961D  72 32                           jb 0x140289651
0028961F  44 8B CF                        mov r9d, edi
00289622  45 0F B6 C6                     movzx r8d, r14b
00289626  41 0F BA E9 0C                  bts r9d, 0xc
0028962B  41 8B D7                        mov edx, r15d
0028962E  48 8B CE                        mov rcx, rsi
00289631  E8 0E BB 0F 00                  call 0x140385144
00289636  48 8B F0                        mov rsi, rax
00289639  4C 8D 2C 40                     lea r13, [rax + rax*2]
0028963D  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
00289647  49 C1 E5 04                     shl r13, 4
0028964B  48 8B C0                        mov rax, rax
0028964E  4C 03 E8                        add r13, rax
00289651  0F BA E7 0C                     bt edi, 0xc
00289655  0F 83 C1 00 00 00               jae 0x14028971c
0028965B  48 8B CE                        mov rcx, rsi
0028965E  E8 6D F6 0A 00                  call 0x140338cd0
00289663  41 3B C7                        cmp eax, r15d
00289666  0F 84 B0 00 00 00               je 0x14028971c
0028966C  49 8B CD                        mov rcx, r13
0028966F  E8 6C B4 0A 00                  call 0x140334ae0
00289674  48 C7 C0 FF FF FF FF            mov rax, 0xffffffffffffffff
0028967B  E9 A6 F5 FF FF                  jmp 0x140288c26
00289680  48 85 C9                        test rcx, rcx
00289683  0F 85 AC 01 00 00               jne 0x140289835
00289689  48 8B CA                        mov rcx, rdx
0028968C  41 8B C3                        mov eax, r11d
0028968F  D3 E0                           shl eax, cl
00289691  FF C8                           dec eax
00289693  E9 F8 FE FF FF                  jmp 0x140289590
00289698  8B 05 1A D4 D3 00               mov eax, dword ptr [rip + 0xd3d41a]
0028969E  A8 40                           test al, 0x40
002896A0  0F 84 5A FE FF FF               je 0x140289500
002896A6  E8 E5 5D 08 00                  call 0x14030f490
002896AB  84 C0                           test al, al
002896AD  0F 84 4D FE FF FF               je 0x140289500
002896B3  41 8B CF                        mov ecx, r15d
002896B6  E8 A5 5D 08 00                  call 0x14030f460
002896BB  E9 42 FE FF FF                  jmp 0x140289502
002896C0  8B 05 AA 6B BA 00               mov eax, dword ptr [rip + 0xba6baa]
002896C6  FF C0                           inc eax
002896C8  85 05 86 B9 D3 00               test dword ptr [rip + 0xd3b986], eax
002896CE  89 05 9C 6B BA 00               mov dword ptr [rip + 0xba6b9c], eax
002896D4  0F 85 CA F1 FF FF               jne 0x1402888a4
002896DA  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
002896E4  48 8B C0                        mov rax, rax
002896E7  49 8B CD                        mov rcx, r13
002896EA  BA 01 00 00 00                  mov edx, 1
002896EF  48 2B C8                        sub rcx, rax
002896F2  48 B8 AB AA AA AA AA AA AA AA   movabs rax, 0xaaaaaaaaaaaaaaab
002896FC  48 C1 F9 04                     sar rcx, 4
00289700  48 0F AF C8                     imul rcx, rax
00289704  E8 6F AB 24 00                  call 0x1404d4278
00289709  45 33 C9                        xor r9d, r9d
0028970C  49 8D 4D 10                     lea rcx, [r13 + 0x10]
00289710  4D 89 4D 00                     mov qword ptr [r13], r9
00289714  48 8B 01                        mov rax, qword ptr [rcx]
00289717  E9 A3 F1 FF FF                  jmp 0x1402888bf
0028971C  0F BA E7 0D                     bt edi, 0xd
00289720  73 26                           jae 0x140289748
00289722  49 8B CD                        mov rcx, r13
00289725  E8 66 23 0B 00                  call 0x14033ba90
0028972A  41 3A C6                        cmp al, r14b
0028972D  74 19                           je 0x140289748
0028972F  45 84 E4                        test r12b, r12b
00289732  0F 84 34 FF FF FF               je 0x14028966c
00289738  EB 0E                           jmp 0x140289748
0028973A  44 0F B6 65 E5                  movzx r12d, byte ptr [rbp - 0x1b]
0028973F  45 84 E4                        test r12b, r12b
00289742  0F 84 C7 FE FF FF               je 0x14028960f
00289748  49 BC 00 00 00 00 00 DE FF FF   movabs r12, 0xffffde0000000000
00289752  E9 8B F4 FF FF                  jmp 0x140288be2
00289757  0F B6 C0                        movzx eax, al
0028975A  0F B6 44 05 E0                  movzx eax, byte ptr [rbp + rax - 0x20]
0028975F  3C 02                           cmp al, 2
00289761  74 66                           je 0x1402897c9
00289763  4C 8B 4C 24 50                  mov r9, qword ptr [rsp + 0x50]
00289768  41 B8 01 00 00 00               mov r8d, 1
0028976E  8B 54 24 70                     mov edx, dword ptr [rsp + 0x70]
00289772  0F B6 C0                        movzx eax, al
00289775  C1 E0 08                        shl eax, 8
00289778  33 C6                           xor eax, esi
0028977A  25 00 01 00 00                  and eax, 0x100
0028977F  33 F0                           xor esi, eax
00289781  E9 39 F0 FF FF                  jmp 0x1402887bf
00289786  8B C3                           mov eax, ebx
00289788  C1 E8 02                        shr eax, 2
0028978B  33 C3                           xor eax, ebx
0028978D  83 E0 03                        and eax, 3
00289790  33 D8                           xor ebx, eax
00289792  83 7C 24 58 00                  cmp dword ptr [rsp + 0x58], 0
00289797  0F 84 C7 F9 FF FF               je 0x140289164
0028979D  E9 AA F6 FF FF                  jmp 0x140288e4c
002897A2  44 0F B6 45 E4                  movzx r8d, byte ptr [rbp - 0x1c]
002897A7  41 8B D7                        mov edx, r15d
002897AA  48 8B CE                        mov rcx, rsi
002897AD  E8 56 79 21 00                  call 0x1404a1108
002897B2  85 C0                           test eax, eax
002897B4  0F 85 BC F8 FF FF               jne 0x140289076
002897BA  E9 0E F9 FF FF                  jmp 0x1402890cd
002897BF  44 8B 5C 24 34                  mov r11d, dword ptr [rsp + 0x34]
002897C4  E9 C9 F5 FF FF                  jmp 0x140288d92
002897C9  8B CE                           mov ecx, esi
002897CB  C1 E9 09                        shr ecx, 9
002897CE  83 E1 3F                        and ecx, 0x3f
002897D1  E8 DA 4D 09 00                  call 0x14031e5b0
002897D6  EB 8B                           jmp 0x140289763
002897D8  41 8B C0                        mov eax, r8d
002897DB  BA 20 00 00 00                  mov edx, 0x20
002897E0  83 E0 1F                        and eax, 0x1f
002897E3  2B D0                           sub edx, eax
002897E5  41 8B C3                        mov eax, r11d
002897E8  8B CA                           mov ecx, edx
002897EA  D3 E0                           shl eax, cl
002897EC  49 8B C9                        mov rcx, r9
002897EF  FF C8                           dec eax
002897F1  D3 E0                           shl eax, cl
002897F3  F7 D0                           not eax
002897F5  F0 41 21 02                     lock and dword ptr [r10], eax
002897F9  8B C2                           mov eax, edx
002897FB  49 83 C2 04                     add r10, 4
002897FF  49 8B D3                        mov rdx, r11
00289802  48 2B D0                        sub rdx, rax
00289805  48 83 FA 20                     cmp rdx, 0x20
00289809  72 1C                           jb 0x140289827
0028980B  48 8B CA                        mov rcx, rdx
0028980E  48 C1 E9 05                     shr rcx, 5
00289812  48 6B C1 E0                     imul rax, rcx, -0x20
00289816  48 03 D0                        add rdx, rax
00289819  33 C0                           xor eax, eax
0028981B  41 89 02                        mov dword ptr [r10], eax
0028981E  49 83 C2 04                     add r10, 4
00289822  49 2B CB                        sub rcx, r11
00289825  75 F4                           jne 0x14028981b
00289827  48 85 D2                        test rdx, rdx
0028982A  0F 84 7C F7 FF FF               je 0x140288fac
00289830  E9 5C FC FF FF                  jmp 0x140289491
00289835  41 83 E0 1F                     and r8d, 0x1f
00289839  BA 20 00 00 00                  mov edx, 0x20
0028983E  41 2B D0                        sub edx, r8d
00289841  41 8B C3                        mov eax, r11d
00289844  8B CA                           mov ecx, edx
00289846  D3 E0                           shl eax, cl
00289848  41 0F B6 CA                     movzx ecx, r10b
0028984C  80 E1 1F                        and cl, 0x1f
0028984F  FF C8                           dec eax
00289851  D3 E0                           shl eax, cl
00289853  F0 41 09 01                     lock or dword ptr [r9], eax
00289857  8B C2                           mov eax, edx
00289859  49 83 C1 04                     add r9, 4
0028985D  49 8B D3                        mov rdx, r11
00289860  48 2B D0                        sub rdx, rax
00289863  48 83 FA 20                     cmp rdx, 0x20
00289867  72 1E                           jb 0x140289887
00289869  48 8B CA                        mov rcx, rdx
0028986C  48 C1 E9 05                     shr rcx, 5
00289870  48 6B C1 E0                     imul rax, rcx, -0x20
00289874  48 03 D0                        add rdx, rax
00289877  41 C7 01 FF FF FF FF            mov dword ptr [r9], 0xffffffff
0028987E  49 83 C1 04                     add r9, 4
00289882  49 2B CB                        sub rcx, r11
00289885  75 F0                           jne 0x140289877
00289887  48 85 D2                        test rdx, rdx
0028988A  0F 84 04 FD FF FF               je 0x140289594
00289890  E9 F4 FD FF FF                  jmp 0x140289689
00289895  8D 51 FF                        lea edx, [rcx - 1]
00289898  E9 E5 F2 FF FF                  jmp 0x140288b82
0028989D  41 8B D6                        mov edx, r14d
002898A0  49 8B CD                        mov rcx, r13
002898A3  E8 58 ED 03 00                  call 0x1402c8600
002898A8  44 8B 44 24 38                  mov r8d, dword ptr [rsp + 0x38]
002898AD  8B D0                           mov edx, eax
002898AF  49 8B CD                        mov rcx, r13
002898B2  E8 15 96 0A 00                  call 0x140332ecc
002898B7  8B 54 24 38                     mov edx, dword ptr [rsp + 0x38]
002898BB  E9 21 F6 FF FF                  jmp 0x140288ee1
002898C0  C1 EB 03                        shr ebx, 3
002898C3  45 8B C7                        mov r8d, r15d
002898C6  83 E3 01                        and ebx, 1
002898C9  49 8B D5                        mov rdx, r13
002898CC  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
002898D0  E8 3F D0 03 00                  call 0x1402c6914
002898D5  E9 4D F6 FF FF                  jmp 0x140288f27
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiGetPage(__int64 a1, int a2, int a3, int a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned int v_stack_m110;
    unsigned int v_stack_m114;
    unsigned int v_stack_m118;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m60;
    unsigned __int8 v_stack_m63;
    unsigned __int16 v_stack_m64;
    unsigned __int8 v_stack_m65;
    unsigned __int8 v_stack_m66;
    unsigned int v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned int v_stack_m74;
    unsigned int v_stack_m78;
    unsigned int v_stack_m7C;
    unsigned int v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned int v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned int v_stack_mC0;
    unsigned __int8 v_stack_mC8;
    unsigned int v_stack_mD0;
    unsigned int v_stack_mD4;
    unsigned int v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned int v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p30;
    unsigned int v_stack_p34;
    unsigned int v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned int v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned int v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned int v_stack_p70;
    unsigned int v_stack_p74;
    unsigned int v_stack_p78;

    v_stack_p20 = v_rbx;
    v_rsp = (v_rsp) - (272);
    result = (*(unsigned __int64 *)(v_rip + 12067421)) ^ (v_rsp);
    v_stack_m40 = result;
    v_stack_mC0 = a3;
    a4 = 0;
    v_stack_m118 = a2;
    v_stack_mB8 = a1;
    a3 = (unsigned int)(((unsigned int)(a2)) >> (16));
    v_rbx = (unsigned int)(((unsigned int)(a3)) & (12));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a3)))) & (2));
    v_stack_mF0 = (unsigned int)(result);
    if (condition_is_not_equal) goto loc_0028951F;
loc_00288521:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) >> (2));
    a3 = (unsigned int)((a3) & (3));
    result = (unsigned int)((result) & (3));
    v_rbx = (unsigned int)((v_rbx) | ((unsigned int)(result)));
    if (condition_is_below) goto loc_00288C4E;
    a2 = *(unsigned __int16 *)(v_rip + 13880024);
    if ((((unsigned int)((unsigned int)(a3))) & (0x1040ULL)) != 0) { a2 = (unsigned int)(a4 + 1); }
loc_0028854A:
    result = 0;
    v_stack_mD0 = a2;
    v_stack_m68 = 0;
    v_stack_m64 = 0;
    v_r15 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a2)))) >> (9));
    v_r15 = (unsigned int)((v_r15) & (63));
    v_stack_mA0 = 0;
    v_stack_mD4 = (unsigned int)(v_r15);
    v_stack_m110 = a3;
    a1 = (unsigned int)((unsigned int)(*(unsigned __int8 *)(v_rip + 13879966)));
    if (((unsigned __int8)(*(unsigned __int8 *)(v_rip + 13879966))) <= ((unsigned __int8)(a4 + 1))) { a1 = (unsigned int)(a4 + 1); }
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a2)))) >> (8));
    result = (unsigned __int8)((result) & ((unsigned __int8)(a4 + 1)));
    v_stack_m65 = (unsigned __int8)(a1);
    v_stack_m64 = (unsigned __int8)(result);
loc_00288597:
    if (0 >= a2) goto loc_00288AF9;
    a1 = (unsigned int)((*(unsigned __int16 *)(v_rip + 13879897)) * ((unsigned int)(v_r15)));
    a1 = (unsigned int)((a1) + (0));
    a4 = (a4) * ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12211746) + a1 * 4)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12211746) + a1 * 4))) << (9));
    a4 = (a4) + (*(unsigned __int64 *)(v_stack_mB8 + 16));
    result = (unsigned int)((result) ^ ((unsigned int)((unsigned int)(a2))));
    result = (unsigned int)((result) & (0x7E00ULL));
    v_stack_mF8 = a4;
    v_rsi = (unsigned int)(((unsigned int)(a2)) ^ ((unsigned int)(result)));
    v_stack_m118 = (unsigned int)(v_rsi);
    if (*(unsigned __int64 *)(a4 + 14976) == 0) goto loc_002890AF;
loc_002885EC:
    if (a4 != 0) goto loc_00288C56;
    result = 0;
    v_stack_m68 = 0;
    v_stack_m64 = 0;
    a1 = (unsigned int)((unsigned int)(*(unsigned __int8 *)(v_rip + 13879805)));
    if (((unsigned __int8)(*(unsigned __int8 *)(v_rip + 13879805))) <= 1) { a1 = (unsigned int)(a4 + 1); }
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rsi))) >> (8));
    result = (unsigned __int8)((result) & (1));
    v_stack_m65 = (unsigned __int8)(a1);
    v_stack_m64 = (unsigned __int8)(result);
loc_0028861A:
    result = 0;
    v_r12 = 0;
    if (!(condition_is_below)) {
        result = 0x3B60ULL;
        v_r12 = 0x3B58ULL;
        if (a3 != 3) { v_r12 = (unsigned int)(result); }
        result = 0;
        v_stack_mA0 = 0;
        v_r12 = *(unsigned __int64 *)(v_r12 + a4 * 1);
    }
    a3 = (unsigned int)(((unsigned int)((unsigned int)(v_rsi))) >> (16));
    v_r10 = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) & (3));
    a3 = (unsigned int)((a3) & (3));
    v_stack_m108 = v_r10;
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rsi))) >> (15));
    result = (unsigned int)((result) & (1));
    a1 = (a3 + a3 * 4) << (8);
    a1 = (a1) + (a4);
    if (a3 == 3) { result = 0; }
    if (*(unsigned __int64 *)(a1 + v_r10 + result * 4 * 8 + 24) != 0) goto loc_0028877E;
    if ((unsigned __int16)(*(unsigned __int64 *)(a4 + 15200)) != 0) goto loc_0028877E;
loc_0028869D:
    if (0 > a3) goto loc_002886CC;
    a1 = (0 + 0 * 4) << (8);
    if (*(unsigned __int64 *)(a1 + a4 * 1 + 8) != 0) goto loc_0028877E;
    if (*(unsigned __int64 *)(a1 + a4 * 1 + 16) != 0) goto loc_0028877E;
    a2 = (unsigned int)((0) + 1);
    goto loc_0028869D;
loc_002886CC:
    if (((unsigned int)(v_r10)) != 1) goto loc_00288CC3;
    if (a3 != 3) goto loc_00288CC3;
    a1 = 0;
    v_stack_m114 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12211673 + a3 * 4)));
loc_002886F4:
    if (0 >= 2) goto loc_00288CBE;
    result = (0) + (928);
    result = (result) + (result);
    if (*(unsigned __int64 *)(a4 + result * 8) == 0) goto loc_00288779;
    if (((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12211673 + a3 * 4))))) > 1) goto loc_00288732;
    if (((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12211673 + a3 * 4))))) != 1) goto loc_00288779;
    if (((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12211673 + a3 * 4))))) < 1) goto loc_00288779;
loc_00288729:
    v_r11 = (unsigned int)((0) + 1);
    goto loc_002886F4;
loc_00288732:
    if ((*(unsigned __int64 *)(a4 + result * 8)) < ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12211673 + a3 * 4)))))) goto loc_00288779;
    result = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12211673 + a3 * 4)))) - 1) >> (6);
    v_stack_mE0 = *(unsigned __int64 *)(*(unsigned __int64 *)(a4 + (unsigned int)(v_stack_m114) * 8 + 8));
    if ((*(unsigned __int64 *)(a4 + (unsigned int)(v_stack_m114) * 8 + 8)) != (*(unsigned __int64 *)(a4 + (unsigned int)(v_stack_m114) * 8 + 8) + result * 8)) goto loc_00289411;
    a1 = (unsigned __int8)((64) - ((unsigned __int8)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12211673 + a3 * 4)))))));
    result = (-1) >> ((unsigned __int8)(a1));
loc_00288772:
    result = (((v_stack_mE0) & (result)) == 0) ? 1 : 0;
    if ((unsigned __int8)(result) != 0) goto loc_00288729;
loc_00288779:
loc_0028877E:
    a2 = (unsigned int)((1) << ((unsigned __int8)((unsigned int)((unsigned int)(v_stack_m108)))));
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) >> (4));
    a2 = (unsigned int)((a2) & ((unsigned int)(result)));
    if ((((unsigned __int8)(a2)) & (15)) != 0) goto loc_00288CC3;
loc_0028879C:
    v_stack_m108 = (unsigned int)(v_rbx);
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) << (18));
    result = (unsigned int)((result) ^ ((unsigned int)(v_rsi)));
    result = (unsigned int)((result) & (0xC0000ULL));
    v_rsi = (unsigned int)((v_rsi) ^ ((unsigned int)(result)));
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) & (3));
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a3)))) & (16));
    v_stack_mA8 = (unsigned int)(result);
    v_stack_mD8 = a2;
loc_002887BF:
    a1 = 0;
    v_stack_m80 = 1;
    v_stack_m90 = 0;
    v_stack_m74 = 0;
    v_stack_m70 = 0;
    result = v_rip - 2588530;
    if (a2 == 0) { result = v_rip - 2586532; }
    v_stack_m118 = (unsigned int)(v_rsi);
    a1 = (a2 == 0) ? 1 : 0;
    v_stack_m88 = result;
    v_stack_m98 = a4;
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rsi))) & (0x30000ULL));
    v_stack_m7C = (unsigned int)(v_rsi);
    v_stack_m78 = (unsigned int)((unsigned int)(a3));
    v_stack_m100 = (unsigned int)(a1);
    if (((unsigned int)(result)) != 0x30000ULL) goto loc_002888B0;
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rsi))) & (0xC0000ULL));
    if (((unsigned int)(result)) != 0x40000ULL) goto loc_002888B0;
    v_stack_m114 = (unsigned int)((unsigned __int8)(v_rsi));
    v_stack_mE8 = (unsigned __int8)(v_rsi);
loc_00288831:
    result = ((int)((unsigned int)(a1)) + 928) << (4);
    result = (result) + (a4);
    v_stack_mE0 = result;
    if (condition_is_above_or_equal) goto loc_00288FFD;
    a1 = ((unsigned int)((unsigned int)((unsigned __int8)(v_rsi)))) << (4);
    a1 = (a1) + (*(unsigned __int64 *)(a4 + (int)((unsigned int)(a1)) * 8 + 14944));
    v_stack_mB0 = *(unsigned __int64 *)(a4 + (int)((unsigned int)(a1)) * 8 + 14944);
    result = ExpInterlockedPopEntrySList(a1, (int)((unsigned int)(a1)), (unsigned int)((unsigned int)((unsigned __int8)(v_rsi))), a4);
    if (result == 0) goto loc_00288F55;
loc_0028887C:
    *(unsigned __int64 *)(result + 16) = *(unsigned __int64 *)(v_rip - 2588684);
    if (v_stack_m100 != 0) goto loc_00289050;
    if (sign_flag) goto loc_002896C0;
loc_002888A4:
    a4 = 0;
    *(unsigned __int64 *)(result) = 0;
    goto loc_002888BF;
loc_002888B0:
    result = MiGetPerfectColorHeadPage(v_stack_m98, (int)((unsigned int)(a1)), (unsigned int)((unsigned int)((unsigned __int8)(v_rsi))), a4);
    a4 = 0;
loc_002888BF:
    if (result >= 2) goto loc_00288AFD;
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rsi))) >> (16));
    result = (unsigned int)((result) & (3));
    v_rsi = (unsigned int)((v_rsi) >> (15));
    v_rsi = (unsigned int)((v_rsi) & (1));
    v_stack_m114 = (unsigned int)(result);
    a3 = (result + result * 4) << (8);
    a3 = (a3) + (v_stack_mF8);
    if (v_stack_mD8 == 0) goto loc_002890D9;
    if ((((unsigned __int8)((unsigned int)(a3))) & (32)) == 0) goto loc_002893DA;
    result = ((unsigned int)(v_stack_mA8)) + (4);
    a2 = (result + v_rsi * 4) << (5);
    a2 = (a2) + (a3);
loc_00288912:
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a3)))) & (0xFFFFFFEFULL));
loc_00288917:
    if (a2 == 0) goto loc_00288963;
    a3 = (*(unsigned __int64 *)(a2)) >> (3);
    v_stack_m60 = v_xmm0;
    v_stack_m50 = v_xmm0;
    result = memcpy(v_stack_m60, *(unsigned __int64 *)(a2 + 8), a3, a4);
    result = 0;
loc_00288946:
    a3 = (unsigned int)((0) + (0));
    if (a3 >= 8) goto loc_002893AD;
    a2 = (unsigned int)((0) + 1);
    a1 = (v_stack_m60) + (8);
    if (a2 < 4) goto loc_00288946;
loc_00288963:
    result = MiGetPerfectFreeOrZeroPage(v_stack_mF8, (unsigned int)((unsigned int)((unsigned int)(v_stack_m118))), (unsigned int)((unsigned int)(v_rsi)), a4);
    if (result >= 2) goto loc_00288AF6;
    if (v_stack_m114 == 3) {
        a1 = *(unsigned __int64 *)(v_stack_mF8 + 14984);
        a3 = (unsigned int)((unsigned int)(a3));
        a2 = (unsigned int)((unsigned int)(v_stack_m118));
        result = MiCheckZeroFreeRebalance(a1, a2, a3, a4);
    }
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m118)))) & (0x30000ULL));
    a1 = (((unsigned int)(result)) == 0x30000ULL) ? 1 : 0;
    result = ((((unsigned __int8)((unsigned int)(a3))) & (2)) == 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) == 0) goto loc_002889F3;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m118)))) >> (18));
    a1 = (unsigned int)((a1) & (3));
    result = MiCacheAttributeHasValue(a1, a2, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_002889F3;
    a2 = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) << (16));
    a2 = (unsigned int)((a2) ^ ((unsigned int)((unsigned int)(v_stack_m118))));
    a2 = (unsigned int)((a2) & (0xC0000ULL));
    a2 = (unsigned int)((a2) ^ ((unsigned int)((unsigned int)(v_stack_m118))));
    result = MiDemoteLocalLargePage(*(unsigned __int64 *)(v_stack_mF8 + 14984), a2, (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    if (result != 0) goto loc_00289448;
loc_002889F3:
    v_stack_mE0 = *(unsigned __int64 *)(v_stack_mF8 + 14984);
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m118)))) & (0x30000ULL));
    if (((unsigned int)(result)) != 0x30000ULL) goto loc_00288A2A;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m118)))) & (0xC0000ULL));
    if (((unsigned int)(result)) == 0x40000ULL) goto loc_002892B8;
loc_00288A2A:
    result = MiRemovePageAnyColor(v_stack_mE0, (unsigned int)((unsigned int)((unsigned int)(v_stack_m118))), (unsigned int)((unsigned int)((unsigned int)(a3))), 1);
    if (result == 2) goto loc_002890CD;
    if (result != 0) goto loc_002891EB;
    if ((((unsigned __int8)((unsigned int)(a3))) & (64)) != 0) goto loc_002891A7;
loc_00288A5F:
    if (condition_is_below) goto loc_002892DA;
    result = MiRemovePageAnyColor(v_stack_mE0, (unsigned int)((unsigned int)((unsigned int)(v_stack_m118))), (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a3))))), 1);
    if (result == 2) goto loc_002890CD;
    if (result != 0) goto loc_002891EF;
    goto loc_002891F9;
loc_00288AA1:
    result = MiPageAvailable(*(unsigned __int64 *)(v_stack_mF8 + 14984), (unsigned int)((unsigned int)((unsigned int)(a3))), (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a3))))), 1);
    if ((unsigned int)(result) == 0) goto loc_002890CD;
    result = (unsigned __int8)((v_stack_m66) + 1);
    v_stack_m66 = (unsigned __int8)(result);
    if (((unsigned __int8)(result)) < v_stack_m65) goto loc_00289757;
    if (((unsigned __int8)(v_stack_m64)) == 2) goto loc_002895C5;
loc_00288ADA:
    result = (unsigned int)(((unsigned __int8)(v_stack_m64)) << (8));
    result = (unsigned int)((result) ^ ((unsigned int)((unsigned int)(v_stack_m118))));
    result = (unsigned int)((result) & (256));
    v_rsi = (unsigned int)(((unsigned int)(v_stack_m118)) ^ ((unsigned int)(result)));
    v_stack_m118 = (unsigned int)(v_rsi);
    if (result == 0) goto loc_00289306;
loc_00288AF6:
    a4 = 0;
loc_00288AF9:
loc_00288AFD:
    if (result == 2) goto loc_002890CD;
    if (result == 0) goto loc_0028905A;
    v_rsi = (result) - (v_r12);
    v_rsi = (v_rsi) >> (4);
    v_rsi = (v_rsi) * (v_r12);
loc_00288B31:
    *(unsigned __int64 *)(result) = 0;
    if (!(condition_is_above_or_equal)) {
        a1 = *(unsigned int *)(result + 36);
        a1 = (unsigned int)((a1) & (0x18000000ULL));
    }
    *(unsigned int *)(result + 36) = (unsigned int)(a1);
    if (((unsigned int)((int)(*(unsigned int *)(v_rip + 12210280)))) > ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12210278))))) goto loc_00288B7F;
    result = ((int)(*(unsigned int *)(v_rip + 12210280))) << (4);
    result = (result) + (*(unsigned __int64 *)(v_rip + 12210352));
    if (v_rsi < (*(unsigned __int64 *)(result))) goto loc_00288B7F;
    if (((unsigned int)((int)(*(unsigned int *)(v_rip + 12210280)))) == ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12210278))))) goto loc_00288BBA;
    if (v_rsi < (*(unsigned __int64 *)(result + 16))) goto loc_00288BBA;
loc_00288B7F:
loc_00288B82:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12210278)))) < 0) goto loc_00288CA4;
    a1 = (unsigned int)((0 + (unsigned int)(*(unsigned int *)(v_rip + 12210278)) * 1) >> (1));
    result = ((int)((unsigned int)(a1))) << (4);
    result = (result) + (*(unsigned __int64 *)(v_rip + 12210305));
    if (v_rsi < (*(unsigned __int64 *)(result))) goto loc_002892E3;
    if (((unsigned int)(a1)) != (*(unsigned int *)(v_rip + 12210198))) goto loc_0028903D;
loc_00288BB4:
    *(unsigned int *)(v_rip + 12210182) = (unsigned int)(a1);
loc_00288BBA:
    if ((*(unsigned int *)(result + 8)) != ((unsigned int)(v_r15))) goto loc_00289605;
    if ((*(unsigned __int64 *)(v_rip + 12210268)) != 0) goto loc_00289182;
    result = 0;
loc_00288BD4:
    if (0 != ((unsigned __int8)(v_stack_m64))) goto loc_0028973A;
loc_00288BE2:
    if ((((unsigned __int8)((unsigned int)(a3))) & (32)) == 0) goto loc_00288C19;
    v_r14 = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) >> (2));
    v_r14 = (unsigned int)((v_r14) & (3));
    if (((*(unsigned __int64 *)(result + 16)) & (992)) != 0) goto loc_00288E86;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 32))) >> (16));
    a1 = (unsigned int)(((unsigned __int8)(result)) >> (6));
    if (((unsigned int)(a1)) != ((unsigned int)(v_r14))) goto loc_00288E6C;
loc_00288C19:
    if ((((unsigned __int8)((unsigned int)(a3))) & (8)) == 0) goto loc_00289017;
loc_00288C23:
loc_00288C26:
    a1 = (v_stack_m40) ^ (v_rsp);
    result = _security_check_cookie(a1, (unsigned int)(*(unsigned int *)(v_rip + 12210278)), 0, a4);
    v_rsp = (v_rsp) + (272);
    return result;
loc_00288C4E:
    goto loc_0028854A;
loc_00288C56:
    v_stack_m66 = 0;
    if (((unsigned __int8)(v_stack_m65)) <= 1) goto loc_0028861A;
    result = (unsigned __int8)(~(*(unsigned __int8 *)(a4 + 15184)));
    result = (unsigned __int8)((result) & (1));
    v_stack_m63 = (unsigned __int8)(result);
    v_stack_m68 = (unsigned __int16)(*(unsigned __int16 *)(a4 + 15233));
    if (condition_is_above_or_equal) goto loc_0028861A;
    a2 = 0;
loc_00288CA4:
    v_stack_p20 = 0;
    a4 = 0;
    result = KeBugCheckEx(a4 + 26, (unsigned int)(0x5180ULL), v_rsi, a4);
loc_00288CBE:
loc_00288CC3:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_stack_p20))) & (0xFFFFF80FULL));
    v_r10 = (unsigned int)(((unsigned int)((unsigned int)(v_rsi))) >> (16));
    v_r11 = (unsigned int)(((unsigned int)((unsigned int)(v_rsi))) >> (15));
    a2 = (unsigned int)((16) << ((unsigned __int8)((unsigned int)((unsigned int)(v_stack_p40)))));
    v_r11 = (unsigned int)((v_r11) & (1));
    a2 = (unsigned int)((a2) | ((unsigned int)(v_stack_p20)));
    v_stack_p34 = (unsigned int)(v_r11);
    a2 = (unsigned int)((a2) & (240));
    v_r10 = (unsigned int)((v_r10) & (3));
    v_rbx = (unsigned int)(((unsigned int)(a2)) | ((unsigned int)(result)));
    v_rdi = 0;
loc_00288D02:
    a3 = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) >> (8));
    a3 = (unsigned int)((a3) & (7));
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) >> (4));
    a2 = (unsigned int)((1) << ((unsigned __int8)((unsigned int)(a3))));
    a2 = (unsigned int)((a2) & ((unsigned int)(result)));
    if ((((unsigned __int8)(a2)) & (15)) != 0) goto loc_00288DB4;
    a2 = (v_r10 + v_r10 * 4) << (8);
    a2 = (a2) + (0);
    result = (unsigned int)((unsigned int)(v_r11));
    if (((unsigned int)(v_r10)) == 3) { result = 0; }
    if (*(unsigned __int64 *)(a2 + a3 + result * 4 * 8 + 24) != 0) goto loc_00288DD5;
    if ((unsigned __int16)(*(unsigned __int64 *)(a4 + 15200)) != 0) goto loc_00288DD5;
loc_00288D59:
    if (0 > ((unsigned int)(v_r10))) goto loc_00288D80;
    a1 = (0 + 0 * 4) << (8);
    if (*(unsigned __int64 *)(a1 + a4 * 1 + 8) != 0) goto loc_00288DD5;
    if (*(unsigned __int64 *)(a1 + a4 * 1 + 16) != 0) goto loc_00288DD5;
    a2 = (unsigned int)((0) + 1);
    goto loc_00288D59;
loc_00288D80:
    if (((unsigned int)(v_r10)) != 3) goto loc_00288D92;
    a3 = (unsigned __int8)((a3) & ((unsigned __int8)(v_r10)));
    if (((unsigned __int8)(a3)) == 1) goto loc_002890F8;
loc_00288D92:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) >> (8));
    a1 = (unsigned int)((a1) & (7));
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) & (0xFFFFFF0FULL));
    a2 = (unsigned int)((16) << ((unsigned __int8)(a1)));
    a2 = (unsigned int)((a2) | ((unsigned int)(v_rbx)));
    a2 = (unsigned int)((a2) & (240));
    v_rbx = (unsigned int)(((unsigned int)(a2)) ^ ((unsigned int)(result)));
loc_00288DB4:
    result = (unsigned int)((v_rbx + 256) ^ ((unsigned int)(v_rbx)));
    result = (unsigned int)((result) & (0x700ULL));
    v_rbx = (unsigned int)((v_rbx) ^ ((unsigned int)(result)));
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) & (0x700ULL));
    if (((unsigned int)(result)) <= 768) goto loc_00288D02;
loc_00288DD5:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) & (240));
    if (((unsigned __int8)(result)) != 240) goto loc_0028933E;
loc_00288DEB:
    if ((unsigned int)((unsigned int)(v_stack_p58)) != 0) goto loc_00288E31;
    result = (unsigned int)(0x3B58ULL);
    if (v_stack_p38 != 3) { result = (unsigned int)((unsigned int)(0x3B60ULL)); }
    a1 = 0;
    result = (result) + (0);
    v_stack_mB0 = result;
    if ((unsigned __int16)(*(unsigned __int64 *)(result)) != 0) goto loc_002894E9;
loc_00288E1E:
    a1 = (*(unsigned __int64 *)(result)) ^ (v_r12);
    if (((a1) & (0xFFFFFFFFFFFF0000ULL)) != 0) goto loc_0028914C;
loc_00288E31:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) >> (2));
    result = (unsigned int)((result) ^ ((unsigned int)(v_rbx)));
    result = (unsigned int)((result) & (3));
    v_rbx = (unsigned int)((v_rbx) ^ ((unsigned int)(result)));
    if ((unsigned int)((unsigned int)(v_stack_p58)) == 0) goto loc_0028915E;
loc_00288E4C:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) >> (2));
    a1 = (unsigned int)((a1) & (3));
    result = (unsigned int)((1) << ((unsigned __int8)(a1)));
    result = (unsigned int)(~(result));
    result = (unsigned int)((result) << (4));
    result = (unsigned int)((result) ^ ((unsigned int)(v_rbx)));
    result = (unsigned int)((result) & (240));
    v_rbx = (unsigned int)((v_rbx) ^ ((unsigned int)(result)));
    goto loc_0028916A;
loc_00288E6C:
    result = (unsigned __int8)((1) << ((unsigned __int8)(a1)));
    if (((*(unsigned __int8 *)(v_rip + 12209752)) & ((unsigned __int8)((unsigned __int8)(result)))) == 0) goto loc_00288C19;
loc_00288E86:
    v_r15 = (unsigned int)(((unsigned int)(v_stack_p30)) >> (16));
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_mC0) * 8))) | (1));
    v_r15 = (unsigned int)((v_r15) & (3));
    if ((((unsigned __int8)((unsigned int)(v_stack_mC0))) & (32)) == 0) { v_rbx = (unsigned int)((unsigned int)(v_stack_mC0) * 8); }
    v_rdi = (result) - (v_r12);
    v_rdi = (v_rdi) >> (4);
    v_rdi = (v_rdi) * (v_r12);
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) & (8));
    result = (unsigned int)((result) | (4));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 32))) >> (16));
    result = (unsigned __int8)((result) & (192));
    v_stack_p38 = (unsigned int)(result + result * 1);
    if (((unsigned __int8)(result)) == 192) goto loc_0028989D;
loc_00288EE1:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 32))) >> (16));
    result = 0;
    a1 = (unsigned int)(((unsigned __int8)(result)) >> (6));
    result = (((unsigned int)(a1)) != ((unsigned int)(v_r14))) ? 1 : 0;
    if ((((unsigned __int8)(v_rbx)) & (1)) == 0) goto loc_00288F39;
    if (((unsigned int)(a1)) != ((unsigned int)(v_r14))) goto loc_002895D7;
loc_00288F07:
    a1 = 0;
    if (((unsigned int)(v_r15)) != 3) goto loc_002898C0;
    v_rbx = (unsigned int)((v_rbx) >> (2));
    v_rbx = (unsigned int)((v_rbx) & (2));
    result = MiZeroPhysicalPage(a1, v_rdi, (unsigned int)((unsigned int)(v_rbx)), (unsigned int)((unsigned int)(v_r14)));
loc_00288F27:
    result = (*(unsigned __int64 *)(result + 16)) & (-993);
    *(unsigned __int64 *)(result + 16) = result;
loc_00288F39:
    if ((unsigned int)((unsigned int)((unsigned int)(result))) == 0) goto loc_00288C23;
    result = MiChangePageAttribute(result, (unsigned int)((unsigned int)(v_r14)), (unsigned int)((unsigned int)((unsigned int)(v_stack_p38))), (unsigned int)((unsigned int)(v_r14)));
    goto loc_00288C23;
loc_00288F55:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) >> (1));
    result = (unsigned int)((result) | ((unsigned int)(v_rdi)));
    if ((((unsigned __int8)(result)) & (1)) == 0) goto loc_002893E2;
    v_stack_mC8 = 17;
loc_00288F67:
    a4 = (unsigned int)((v_stack_p60) & (31));
    a1 = (v_stack_p60) >> (5);
    if ((a4 + 1) > 32) goto loc_00289488;
    result = (unsigned int)((1) << ((unsigned __int8)((unsigned int)(a4))));
    result = (unsigned int)(~(result));
loc_00288FA8:
loc_00288FAC:
    a1 = (v_stack_p60) << (4);
    a1 = (a1) + (v_stack_mB0);
    result = ExpInterlockedPopEntrySList(a1, 1, v_stack_p60, a4);
    if (result != 0) goto loc_00289552;
    if (((unsigned __int8)(v_stack_mC8)) == 17) goto loc_00288FEF;
    if ((*(unsigned int *)(v_rip + 13884744)) != ((unsigned int)(result))) {
        a1 = v_cr8;
        a2 = (unsigned __int8)(v_stack_mC8);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, v_stack_p60, a4);
    }
loc_00288FEF:
loc_00288FFD:
    if (((unsigned int)((unsigned int)(v_stack_p48))) == ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m88 + 4))))) goto loc_002888B0;
    v_stack_p48 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m88 + 4)));
    goto loc_00288831;
loc_00289017:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_mC8 + 32))) >> (16));
    v_r14 = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) >> (2));
    v_r14 = (unsigned int)((v_r14) & (3));
    result = (unsigned int)(((unsigned __int8)(result)) >> (6));
    if (((unsigned int)(result)) == ((unsigned int)(v_r14))) goto loc_00288C23;
    goto loc_00288E86;
loc_0028903D:
    if (((unsigned int)(v_stack_p30)) < (*(unsigned __int64 *)(result + 16))) goto loc_00288BB4;
    goto loc_00288B82;
loc_00289050:
    result = MiSetOriginalPtePfnFromFreeList((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m88 + 4)))), (unsigned int)(*(unsigned int *)(v_stack_m88 + 4)), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m88 + 4)))) + 1, v_stack_p50);
    goto loc_002888A4;
loc_0028905A:
    if ((((unsigned __int8)(v_rdi)) & (2)) != 0) goto loc_002890CD;
    if (condition_is_below) goto loc_002890CD;
    if ((((unsigned int)(v_rdi)) & (0x3000ULL)) != 0) goto loc_002897A2;
loc_00289076:
    result = MiRemoveLowestPriorityStandbyPage(v_stack_mB8, 8, (unsigned int)((unsigned int)(v_rdi)), v_stack_p50);
    if (result == -1) goto loc_002890CD;
    v_r13 = (result + result * 2) << (4);
    v_r13 = (v_r13) + ((unsigned int)((unsigned int)(result)));
    a4 = 0;
    goto loc_00288B31;
loc_002890AF:
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rip + 13883858))) & (48)) == 0) goto loc_002885EC;
    result = MiPageAvailable((unsigned int)((unsigned int)(result)), (unsigned int)((unsigned int)(v_rdi)), (unsigned int)((unsigned int)(v_rdi)), a4);
    if ((unsigned int)(result) != 0) goto loc_00289786;
loc_002890CD:
    goto loc_00288C26;
loc_002890D9:
    a2 = ((unsigned int)(v_stack_mA8) + result * 4) << (5);
    a2 = (a2) + (144);
    a2 = (a2) + ((unsigned int)((unsigned int)(v_rdi)));
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) | (16));
    goto loc_00288917;
loc_002890F8:
loc_00289102:
    if (((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) >= 2) goto loc_002897BF;
    result = ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi))))) + (928);
    result = (result) + (result);
    if (*(unsigned __int64 *)(a4 + result * 8) == 0) goto loc_00288DD5;
    if (((unsigned int)(*(unsigned int *)(v_rip + 12209101))) > v_rsi) goto loc_00289355;
    if (((unsigned int)(*(unsigned int *)(v_rip + 12209101))) != v_rsi) goto loc_00288DD5;
    if (((unsigned int)(*(unsigned int *)(v_rip + 12209101))) < v_rsi) goto loc_00288DD5;
loc_00289147:
    a3 = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) + 1);
    goto loc_00289102;
loc_0028914C:
    v_r14 = (unsigned int)((v_r14) - 1);
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12209101))))) >> (2));
    v_rbx = (unsigned int)((v_rbx) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12209101)))));
    v_rbx = (unsigned int)((v_rbx) & (3));
    v_rbx = (unsigned int)((v_rbx) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12209101)))));
loc_0028915E:
loc_00289164:
    v_rbx = (unsigned int)((v_rbx) & (0xFFFFFF0FULL));
loc_0028916A:
    v_r14 = (unsigned int)((v_r14) + 1);
    a4 = 0;
    goto loc_00288597;
loc_00289182:
    a1 = (v_r13) - (*(unsigned __int64 *)(a4 + result * 8 + 8));
    a1 = (a1) >> (4);
    a1 = (a1) * (*(unsigned __int64 *)(a4 + result * 8 + 8));
    result = MiPageToChannel(a1, (unsigned int)(v_stack_p78), (unsigned int)(v_stack_p38), a4);
    goto loc_00288BD4;
loc_002891A7:
    v_rsi = (unsigned int)((v_rsi) & (0xFFFFFFBFULL));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_p30)))) & (0x30000ULL));
    if (((unsigned int)(result)) != 0x30000ULL) goto loc_00288A5F;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_p30)))) & (0xC0000ULL));
    if (((unsigned int)(result)) != 0x40000ULL) goto loc_00288A5F;
    result = MiGetPageSlist(v_stack_p50, (unsigned int)(v_stack_p30), (unsigned int)((unsigned int)(v_rsi)), a4);
    if (result == 0) goto loc_00288A5F;
loc_002891EB:
loc_002891EF:
    if (result >= 2) goto loc_00288AF6;
loc_002891F9:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) | (16));
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) & (0xFFFFFFEFULL));
    if (v_stack_p70 == 0) { a1 = (unsigned int)(result); }
    result = 0;
    v_stack_p34 = 0;
    v_stack_p48 = (unsigned int)(a1);
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_p30)))) & (0x30000ULL));
    a1 = (((unsigned int)(result)) == 0x30000ULL) ? 1 : 0;
    result = ((((unsigned __int8)(v_rdi)) & (2)) == 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) == 0) goto loc_00289430;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_p30)))) >> (18));
    a1 = (unsigned int)((a1) & (3));
    if (((unsigned int)(a1 - 1)) > 1) goto loc_00289430;
    result = MiCacheAttributeHasValue(a1, (unsigned int)(v_stack_p30), (unsigned int)((unsigned int)(v_rsi)), 0);
    if ((unsigned int)(result) == 0) goto loc_00289282;
    a2 = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) << (16));
    a2 = (unsigned int)((a2) ^ ((unsigned int)((unsigned int)(v_stack_p30))));
    a2 = (unsigned int)((a2) & (0xC0000ULL));
    a2 = (unsigned int)((a2) ^ ((unsigned int)((unsigned int)(v_stack_p30))));
    result = MiDemoteLocalLargePage(*(unsigned __int64 *)(v_stack_p50 + 14984), a2, (unsigned int)((unsigned int)(v_rdi)), 0);
    if (result != 0) goto loc_00289461;
loc_00289282:
    a4 = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) >> (2));
    a4 = (unsigned int)((a4) & (3));
    v_stack_p20 = (unsigned int)((unsigned int)(v_stack_p34));
    result = MiGetFreeOrZeroPageAnyColor(v_stack_p50, (unsigned int)((unsigned int)((unsigned int)(v_stack_p30))), (unsigned int)(v_stack_p48), a4);
    if (result >= 2) goto loc_00288AF6;
    goto loc_00288AA1;
loc_002892B8:
    result = MiGetPageSlist(a4, (unsigned int)((unsigned int)(v_stack_p50)), (unsigned int)((unsigned int)(v_rdi)), a4);
    if (result != 0) goto loc_002891EB;
    goto loc_00288A2A;
loc_002892DA:
    goto loc_002891F9;
loc_002892E3:
    if ((unsigned int)((unsigned int)(v_stack_p30)) != 0) goto loc_00289895;
    v_stack_p20 = a4;
    result = KeBugCheckEx(26, (unsigned int)(0x5180ULL), (unsigned int)(v_stack_p30), result);
loc_00289306:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) & (3));
    result = (unsigned int)((16) << ((unsigned __int8)(a1)));
    v_rbx = (unsigned int)((v_rbx) | ((unsigned int)(result)));
    result = (unsigned int)(((unsigned int)(v_stack_p40)) & (0xFFFFFF0FULL));
    v_rbx = (unsigned int)((v_rbx) & (240));
    v_rbx = (unsigned int)((v_rbx) ^ ((unsigned int)(result)));
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) & (240));
    if (((unsigned __int8)(result)) != 240) goto loc_0028947A;
    goto loc_00288DEB;
loc_0028933E:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) >> (8));
    result = (unsigned int)((result) ^ ((unsigned int)(v_rbx)));
    result = (unsigned int)((result) & (3));
    v_rbx = (unsigned int)((v_rbx) ^ ((unsigned int)(result)));
    goto loc_0028879C;
loc_00289355:
    if (a1 < ((unsigned int)(0x5180ULL))) goto loc_00288DD5;
    result = (1 - 1) >> (6);
    v_stack_p60 = *(unsigned __int64 *)(v_stack_p50 + result * 8 + 8) + result * 8;
    v_stack_p68 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p50 + result * 8 + 8));
    if ((*(unsigned __int64 *)(v_stack_p50 + result * 8 + 8)) != v_stack_p60) goto loc_002894A0;
    a1 = (unsigned __int8)((64) - ((unsigned __int8)((unsigned int)(0x5180ULL))));
    result = (-1) >> ((unsigned __int8)(a1));
loc_0028939D:
    result = (((v_stack_p68) & (result)) == 0) ? 1 : 0;
    if ((unsigned __int8)(result) == 0) goto loc_00288DD5;
    goto loc_00289147;
loc_002893AD:
    a4 = 0;
    result = MiRemovePageAnyColor(*(unsigned __int64 *)(result + 14984), (unsigned int)(v_stack_p30), (unsigned int)((unsigned int)(v_rdi)), a4);
    if (result >= 2) goto loc_00288AF6;
    goto loc_00288963;
loc_002893DA:
    goto loc_00288912;
loc_002893E2:
    v_stack_mC8 = (unsigned __int8)(v_stack_mC8);
    if ((*(unsigned int *)(v_rip + 13883686)) == 0) goto loc_00288F67;
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)((unsigned __int8)(v_stack_mC8)), 2, (unsigned int)((unsigned int)(v_rdi)), a4);
    goto loc_00288F67;
loc_00289411:
loc_00289414:
    if (result != 0) goto loc_00288779;
    a1 = ((unsigned __int8)((unsigned __int8)(v_stack_mC8))) + (8);
    if (a1 == ((unsigned int)((unsigned int)(v_rdi)))) goto loc_002894D1;
    goto loc_00289414;
loc_00289430:
    if (v_stack_p58 == 0) { a4 = 1; }
    v_stack_p34 = a4;
    goto loc_00289282;
loc_00289448:
    result = MiObtainedPageIsGood(v_stack_p50, *(unsigned __int64 *)((unsigned __int8)((unsigned __int8)(v_stack_mC8)) + 8), (unsigned int)((unsigned int)(v_rdi)), a4);
    if ((unsigned int)(result) != 0) goto loc_00288AF6;
    goto loc_002889F3;
loc_00289461:
    result = MiObtainedPageIsGood(v_stack_p50, *(unsigned __int64 *)((unsigned __int8)((unsigned __int8)(v_stack_mC8)) + 8), (unsigned int)((unsigned int)(v_rdi)), a4);
    if ((unsigned int)(result) != 0) goto loc_00288AF6;
    goto loc_00289282;
loc_0028947A:
    v_r14 = (unsigned int)((v_r14) - 1);
    goto loc_0028916A;
loc_00289488:
    if (a4 != 0) goto loc_002897D8;
loc_00289491:
    result = (unsigned int)(((unsigned int)(0xFFFFFFFFULL)) << ((unsigned __int8)(*(unsigned __int64 *)((unsigned __int8)((unsigned __int8)(v_stack_mC8)) + 8))));
    goto loc_00288FA8;
loc_002894A0:
    if (result != 0) goto loc_00288DD5;
loc_002894AE:
    a1 = (*(unsigned __int64 *)((unsigned __int8)((unsigned __int8)(v_stack_mC8)) + 8)) + (8);
    v_stack_p60 = *(unsigned __int64 *)(*(unsigned __int64 *)((unsigned __int8)((unsigned __int8)(v_stack_mC8)) + 8) + 8);
    if (a1 == v_stack_p60) goto loc_00289538;
    if (v_stack_p60 == v_rdi) goto loc_002894AE;
    goto loc_00288DD5;
loc_002894D1:
    a1 = (unsigned __int8)(~((unsigned __int8)(v_stack_mA0)));
    result = (-1) >> ((unsigned __int8)(a1));
    goto loc_00288772;
loc_002894E9:
loc_002894F0:
    v_r15 = (unsigned int)(((unsigned int)((unsigned int)(a1))) + 1);
    if (((*(unsigned int *)(v_rip + 13876658)) & ((unsigned int)(v_r15))) == 0) goto loc_00289698;
loc_00289500:
loc_00289502:
    if ((unsigned __int16)(*(unsigned __int64 *)(v_stack_mB0)) != 0) goto loc_002894F0;
    goto loc_00288E1E;
loc_0028951F:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) >> (2));
    result = (unsigned int)((1) << ((unsigned __int8)(a1)));
    result = (unsigned int)(~(result));
    result = (unsigned int)((result) & (15));
    result = (unsigned int)((result) << (4));
    v_rbx = (unsigned int)((v_rbx) | ((unsigned int)(result)));
    goto loc_00288521;
loc_00289538:
    a1 = (unsigned __int8)(~(1 - 1));
    result = (-1) >> ((unsigned __int8)(a1));
    goto loc_0028939D;
loc_00289552:
    a1 = ((unsigned int)((unsigned int)((unsigned int)(v_stack_p34)))) >> (5);
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_p34)))) & (31));
    if ((a1 + 1) > 32) goto loc_00289680;
    result = (unsigned int)((1) << ((unsigned __int8)(a1)));
loc_00289590:
loc_00289594:
    if (((unsigned __int8)(v_stack_mC8)) == 17) goto loc_0028887C;
    result = v_stack_mC8;
    if ((*(unsigned int *)(v_rip + 13883257)) != 0) {
        a1 = 2;
        a2 = (unsigned __int8)(v_stack_mC8);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, (unsigned int)(v_stack_p34), *(unsigned __int64 *)(v_stack_p68 + 8) + a1 * 4);
        result = v_stack_mC8;
    }
    goto loc_0028887C;
loc_002895C5:
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_p30)))) >> (9));
    a1 = (unsigned int)((a1) & (63));
    result = MiAssignDefaultChannel(a1, a2, (unsigned int)(v_stack_p34), *(unsigned __int64 *)(v_stack_p68 + 8) + a1 * 4);
    goto loc_00288ADA;
loc_002895D7:
    result = MiPfnBestZeroAttribute(v_stack_p50, (unsigned int)((unsigned int)(v_r14)), (unsigned int)(v_stack_p34), *(unsigned __int64 *)(v_stack_p68 + 8) + a1 * 4);
    if (((unsigned int)(result)) != ((unsigned int)(v_r14))) goto loc_00288F07;
    result = MiChangePageAttribute(v_stack_p50, (unsigned int)((unsigned int)(v_r14)), (unsigned int)(v_stack_p38), *(unsigned __int64 *)(v_stack_p68 + 8) + a1 * 4);
    result = 0;
    goto loc_00288F07;
loc_00289605:
loc_0028960F:
    if ((((unsigned __int8)(v_rdi)) & (2)) != 0) goto loc_00289748;
    v_rsi = (unsigned int)(v_stack_p30);
    v_r13 = v_stack_p50;
    if (!(condition_is_below)) {
        a4 = (unsigned int)(v_rdi);
        a3 = (unsigned __int8)(v_stack_m64);
        a2 = (unsigned int)((unsigned int)(v_stack_p74));
        a1 = (unsigned int)(v_stack_p30);
        result = MiSwapNumaStandbyPage(a1, a2, a3, a4);
        v_rsi = result;
        v_r13 = result + result * 2;
        v_r13 = (v_r13) << (4);
        result = result;
        v_r13 = (v_r13) + (result);
    }
    if (condition_is_above_or_equal) goto loc_0028971C;
    result = MiPageToNode(v_rsi, a2, a3, a4);
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(v_stack_p74)))) goto loc_0028971C;
loc_0028966C:
    result = MiReleaseFreshPage(v_r13, a2, a3, a4);
    goto loc_00288C26;
loc_00289680:
    if (v_r13 != 0) goto loc_00289835;
loc_00289689:
    result = (unsigned int)((1) << ((unsigned __int8)(a2)));
    result = (unsigned int)((result) - 1);
    goto loc_00289590;
loc_00289698:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13882394)))) & (64)) == 0) goto loc_00289500;
    result = KiCheckVpBackingLongSpinWaitHypercall(a2, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00289500;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)((unsigned int)(v_stack_p74))), a2, a3, a4);
    goto loc_00289502;
loc_002896C0:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 12217258))) + 1);
    *(unsigned int *)(v_rip + 12217244) = (unsigned int)(result);
    if (((*(unsigned int *)(v_rip + 13875590)) & ((unsigned int)(result))) != 0) goto loc_002888A4;
    a1 = (v_r13) - (result);
    a1 = (a1) >> (4);
    a1 = (a1) * (result);
    result = MiArePageContentsZero(a1, 1, a3, a4);
    a4 = 0;
    *(unsigned __int64 *)(v_r13) = 0;
    goto loc_002888BF;
loc_0028971C:
    if (condition_is_above_or_equal) goto loc_00289748;
    result = MiGetPfnChannel(v_r13, 1, a3, a4);
    if (((unsigned __int8)(result)) == ((unsigned __int8)(v_stack_m64))) goto loc_00289748;
    if ((unsigned __int8)(v_stack_m63) == 0) goto loc_0028966C;
    goto loc_00289748;
loc_0028973A:
    if ((unsigned __int8)(v_stack_m63) == 0) goto loc_0028960F;
loc_00289748:
    goto loc_00288BE2;
loc_00289757:
    if (((unsigned __int8)(*(unsigned __int8 *)(v_stack_m48 + (unsigned __int8)(result) * 1 - 32))) == 2) goto loc_002897C9;
loc_00289763:
    result = (unsigned int)(((unsigned __int8)(*(unsigned __int8 *)(v_stack_m48 + (unsigned __int8)(result) * 1 - 32))) << (8));
    result = (unsigned int)((result) ^ ((unsigned int)(v_rsi)));
    result = (unsigned int)((result) & (256));
    v_rsi = (unsigned int)((v_rsi) ^ ((unsigned int)(result)));
    goto loc_002887BF;
loc_00289786:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) >> (2));
    result = (unsigned int)((result) ^ ((unsigned int)(v_rbx)));
    result = (unsigned int)((result) & (3));
    v_rbx = (unsigned int)((v_rbx) ^ ((unsigned int)(result)));
    if (v_stack_p58 == 0) goto loc_00289164;
    goto loc_00288E4C;
loc_002897A2:
    result = MiCheckNodeChannelStandbyCount(v_rsi, (unsigned int)((unsigned int)((unsigned int)(v_stack_p74))), v_stack_m64, v_stack_p50);
    if ((unsigned int)(result) != 0) goto loc_00289076;
    goto loc_002890CD;
loc_002897BF:
    goto loc_00288D92;
loc_002897C9:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_rsi))) >> (9));
    a1 = (unsigned int)((a1) & (63));
    result = MiAssignDefaultChannel(a1, (unsigned int)((unsigned int)((unsigned int)(v_stack_p74))), v_stack_m64, v_stack_p50);
    goto loc_00289763;
loc_002897D8:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_stack_m64))) & (31));
    a2 = (unsigned int)((32) - ((unsigned int)(result)));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_p34)))) << ((unsigned __int8)((unsigned int)(a2))));
    result = (unsigned int)((result) - 1);
    result = (unsigned int)((result) << ((unsigned __int8)(v_stack_p50)));
    result = (unsigned int)(~(result));
    v_r10 = ((unsigned int)((unsigned int)((unsigned int)(v_stack_p34)))) + (4);
    a2 = ((unsigned int)(v_stack_p34)) - ((unsigned int)(a2));
    if (a2 < 32) goto loc_00289827;
    a1 = (a2) >> (5);
    result = ((unsigned int)(a2)) * (a1);
    a2 = (a2) + (result);
    result = 0;
loc_0028981B:
    *(unsigned int *)(v_r10) = 0;
    v_r10 = (v_r10) + (4);
    a1 = (a1) - ((unsigned int)(v_stack_p34));
    if (condition_is_not_equal) goto loc_0028981B;
loc_00289827:
    if (a2 == 0) goto loc_00288FAC;
    goto loc_00289491;
loc_00289835:
    a3 = (unsigned int)((v_stack_m64) & (31));
    a2 = (unsigned int)((32) - (a3));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_p34)))) << ((unsigned __int8)((unsigned int)(a2))));
    a1 = (unsigned __int8)(((unsigned __int8)(v_r10)) & (31));
    result = (unsigned int)((result) - 1);
    result = (unsigned int)((result) << ((unsigned __int8)(a1)));
    a4 = (v_stack_p50) + (4);
    a2 = ((unsigned int)(v_stack_p34)) - ((unsigned int)(a2));
    if (a2 < 32) goto loc_00289887;
    a1 = (a2) >> (5);
    result = ((unsigned int)(a2)) * (a1);
    a2 = (a2) + (result);
loc_00289877:
    *(unsigned int *)(a4) = 0xFFFFFFFFULL;
    a4 = (a4) + (4);
    a1 = (a1) - ((unsigned int)(v_stack_p34));
    if (condition_is_not_equal) goto loc_00289877;
loc_00289887:
    if (a2 == 0) goto loc_00289594;
    goto loc_00289689;
loc_00289895:
    goto loc_00288B82;
loc_0028989D:
    result = MiPfnBestZeroAttribute(v_r13, (unsigned int)((unsigned int)(v_stack_m64)), a3, a4);
    result = MiChangePageAttribute(v_r13, (unsigned int)((unsigned int)(result)), (unsigned int)(v_stack_p38), a4);
    goto loc_00288EE1;
loc_002898C0:
    v_rbx = (unsigned int)((v_rbx) >> (3));
    v_rbx = (unsigned int)((v_rbx) & (1));
    v_stack_p20 = (unsigned int)(v_rbx);
    result = MiZeroLargePage(v_r13, v_r13, (unsigned int)((unsigned int)((unsigned int)(v_stack_p74))), a4);
    goto loc_00288F27;
}
```

## 5. (Beta) C Style

```c
int64_t MiGetPage(int64_t Arg1, int32_t Arg2, int32_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m100;
    uint64_t v_stack_m108;
    uint32_t v_stack_m110;
    uint32_t v_stack_m114;
    uint32_t v_stack_m118;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m60;
    uint8_t v_stack_m63;
    uint16_t v_stack_m64;
    uint8_t v_stack_m65;
    uint8_t v_stack_m66;
    uint32_t v_stack_m68;
    uint64_t v_stack_m70;
    uint32_t v_stack_m74;
    uint32_t v_stack_m78;
    uint32_t v_stack_m7C;
    uint32_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint32_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint32_t v_stack_mC0;
    uint8_t v_stack_mC8;
    uint32_t v_stack_mD0;
    uint32_t v_stack_mD4;
    uint32_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint32_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p20;
    uint32_t v_stack_p30;
    uint32_t v_stack_p34;
    uint32_t v_stack_p38;
    uint64_t v_stack_p40;
    uint32_t v_stack_p48;
    uint64_t v_stack_p50;
    uint32_t v_stack_p58;
    uint64_t v_stack_p60;
    uint64_t v_stack_p68;
    uint32_t v_stack_p70;
    uint32_t v_stack_p74;
    uint32_t v_stack_p78;

    v_stack_p20 = local_rbx;
    local_rsp = (local_rsp) - (272);
    result = (*(uint64_t *)(v_rip + 0xB8225D)) ^ (local_rsp);
    v_stack_m40 = result;
    v_stack_mC0 = Arg3;
    Arg4 = 0;
    v_stack_m118 = Arg2;
    v_stack_mB8 = Arg1;
    Arg3 = (uint32_t)(((uint32_t)(Arg2)) >> (16));
    local_rbx = (uint32_t)(((uint32_t)(Arg3)) & (12));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg3)))) & (2));
    v_stack_mF0 = (uint32_t)(result);
    if (condition_is_not_equal) goto loc_0028951F;
loc_00288521:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) >> (2));
    Arg3 = (uint32_t)((Arg3) & (3));
    result = (uint32_t)((result) & (3));
    local_rbx = (uint32_t)((local_rbx) | ((uint32_t)(result)));
    if (condition_is_below) goto loc_00288C4E;
    Arg2 = *(uint16_t *)(v_rip + 0xD3CAD8);
    if ((((uint32_t)((uint32_t)(Arg3))) & (0x1040ULL)) != 0) { Arg2 = (uint32_t)(Arg4 + 1); }
loc_0028854A:
    result = 0;
    v_stack_mD0 = Arg2;
    v_stack_m68 = 0;
    v_stack_m64 = 0;
    local_r15 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg2)))) >> (9));
    local_r15 = (uint32_t)((local_r15) & (63));
    v_stack_mA0 = 0;
    v_stack_mD4 = (uint32_t)(local_r15);
    v_stack_m110 = Arg3;
    Arg1 = (uint32_t)((uint32_t)(*(uint8_t *)(v_rip + 0xD3CA9E)));
    if (((uint8_t)(*(uint8_t *)(v_rip + 0xD3CA9E))) <= ((uint8_t)(Arg4 + 1))) { Arg1 = (uint32_t)(Arg4 + 1); }
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg2)))) >> (8));
    result = (uint8_t)((result) & ((uint8_t)(Arg4 + 1)));
    v_stack_m65 = (uint8_t)(Arg1);
    v_stack_m64 = (uint8_t)(result);
loc_00288597:
    if (0 >= Arg2) goto loc_00288AF9;
    Arg1 = (uint32_t)((*(uint16_t *)(v_rip + 0xD3CA59)) * ((uint32_t)(local_r15)));
    Arg1 = (uint32_t)((Arg1) + (0));
    Arg4 = (Arg4) * ((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xBA5622) + Arg1 * 4)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xBA5622) + Arg1 * 4))) << (9));
    Arg4 = (Arg4) + (*(uint64_t *)(v_stack_mB8 + 0x10));
    result = (uint32_t)((result) ^ ((uint32_t)((uint32_t)(Arg2))));
    result = (uint32_t)((result) & (0x7E00ULL));
    v_stack_mF8 = Arg4;
    local_rsi = (uint32_t)(((uint32_t)(Arg2)) ^ ((uint32_t)(result)));
    v_stack_m118 = (uint32_t)(local_rsi);
    if (*(uint64_t *)(Arg4 + 0x3A80) == 0) goto loc_002890AF;
loc_002885EC:
    if (Arg4 != 0) goto loc_00288C56;
    result = 0;
    v_stack_m68 = 0;
    v_stack_m64 = 0;
    Arg1 = (uint32_t)((uint32_t)(*(uint8_t *)(v_rip + 0xD3C9FD)));
    if (((uint8_t)(*(uint8_t *)(v_rip + 0xD3C9FD))) <= 1) { Arg1 = (uint32_t)(Arg4 + 1); }
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rsi))) >> (8));
    result = (uint8_t)((result) & (1));
    v_stack_m65 = (uint8_t)(Arg1);
    v_stack_m64 = (uint8_t)(result);
loc_0028861A:
    result = 0;
    local_r12 = 0;
    if (!(condition_is_below)) {
        result = 0x3B60ULL;
        local_r12 = 0x3B58ULL;
        if (Arg3 != 3) { local_r12 = (uint32_t)(result); }
        result = 0;
        v_stack_mA0 = 0;
        local_r12 = *(uint64_t *)(local_r12 + Arg4 * 1);
    }
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(local_rsi))) >> (16));
    local_r10 = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) & (3));
    Arg3 = (uint32_t)((Arg3) & (3));
    v_stack_m108 = local_r10;
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rsi))) >> (15));
    result = (uint32_t)((result) & (1));
    Arg1 = (Arg3 + Arg3 * 4) << (8);
    Arg1 = (Arg1) + (Arg4);
    if (Arg3 == 3) { result = 0; }
    if (*(uint64_t *)(Arg1 + local_r10 + result * 4 * 8 + 0x18) != 0) goto loc_0028877E;
    if ((uint16_t)(*(uint64_t *)(Arg4 + 0x3B60)) != 0) goto loc_0028877E;
loc_0028869D:
    if (0 > Arg3) goto loc_002886CC;
    Arg1 = (0 + 0 * 4) << (8);
    if (*(uint64_t *)(Arg1 + Arg4 * 1 + 0x8) != 0) goto loc_0028877E;
    if (*(uint64_t *)(Arg1 + Arg4 * 1 + 0x10) != 0) goto loc_0028877E;
    Arg2 = (uint32_t)((0) + 1);
    goto loc_0028869D;
loc_002886CC:
    if (((uint32_t)(local_r10)) != 1) goto loc_00288CC3;
    if (Arg3 != 3) goto loc_00288CC3;
    Arg1 = 0;
    v_stack_m114 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBA55D9 + Arg3 * 4)));
loc_002886F4:
    if (0 >= 2) goto loc_00288CBE;
    result = (0) + (928);
    result = (result) + (result);
    if (*(uint64_t *)(Arg4 + result * 8) == 0) goto loc_00288779;
    if (((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBA55D9 + Arg3 * 4))))) > 1) goto loc_00288732;
    if (((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBA55D9 + Arg3 * 4))))) != 1) goto loc_00288779;
    if (((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBA55D9 + Arg3 * 4))))) < 1) goto loc_00288779;
loc_00288729:
    local_r11 = (uint32_t)((0) + 1);
    goto loc_002886F4;
loc_00288732:
    if ((*(uint64_t *)(Arg4 + result * 8)) < ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBA55D9 + Arg3 * 4)))))) goto loc_00288779;
    result = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBA55D9 + Arg3 * 4)))) - 1) >> (6);
    v_stack_mE0 = *(uint64_t *)(*(uint64_t *)(Arg4 + (uint32_t)(v_stack_m114) * 8 + 0x8));
    if ((*(uint64_t *)(Arg4 + (uint32_t)(v_stack_m114) * 8 + 0x8)) != (*(uint64_t *)(Arg4 + (uint32_t)(v_stack_m114) * 8 + 0x8) + result * 8)) goto loc_00289411;
    Arg1 = (uint8_t)((64) - ((uint8_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBA55D9 + Arg3 * 4)))))));
    result = (-1) >> ((uint8_t)(Arg1));
loc_00288772:
    result = (((v_stack_mE0) & (result)) == 0) ? 1 : 0;
    if ((uint8_t)(result) != 0) goto loc_00288729;
loc_00288779:
loc_0028877E:
    Arg2 = (uint32_t)((1) << ((uint8_t)((uint32_t)((uint32_t)(v_stack_m108)))));
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) >> (4));
    Arg2 = (uint32_t)((Arg2) & ((uint32_t)(result)));
    if ((((uint8_t)(Arg2)) & (15)) != 0) goto loc_00288CC3;
loc_0028879C:
    v_stack_m108 = (uint32_t)(local_rbx);
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) << (18));
    result = (uint32_t)((result) ^ ((uint32_t)(local_rsi)));
    result = (uint32_t)((result) & (0xC0000ULL));
    local_rsi = (uint32_t)((local_rsi) ^ ((uint32_t)(result)));
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) & (3));
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg3)))) & (16));
    v_stack_mA8 = (uint32_t)(result);
    v_stack_mD8 = Arg2;
loc_002887BF:
    Arg1 = 0;
    v_stack_m80 = 1;
    v_stack_m90 = 0;
    v_stack_m74 = 0;
    v_stack_m70 = 0;
    result = v_rip - 2588530;
    if (Arg2 == 0) { result = v_rip - 2586532; }
    v_stack_m118 = (uint32_t)(local_rsi);
    Arg1 = (Arg2 == 0) ? 1 : 0;
    v_stack_m88 = result;
    v_stack_m98 = Arg4;
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rsi))) & (0x30000ULL));
    v_stack_m7C = (uint32_t)(local_rsi);
    v_stack_m78 = (uint32_t)((uint32_t)(Arg3));
    v_stack_m100 = (uint32_t)(Arg1);
    if (((uint32_t)(result)) != 0x30000ULL) goto loc_002888B0;
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rsi))) & (0xC0000ULL));
    if (((uint32_t)(result)) != 0x40000ULL) goto loc_002888B0;
    v_stack_m114 = (uint32_t)((uint8_t)(local_rsi));
    v_stack_mE8 = (uint8_t)(local_rsi);
loc_00288831:
    result = ((int32_t)((uint32_t)(Arg1)) + 928) << (4);
    result = (result) + (Arg4);
    v_stack_mE0 = result;
    if (condition_is_above_or_equal) goto loc_00288FFD;
    Arg1 = ((uint32_t)((uint32_t)((uint8_t)(local_rsi)))) << (4);
    Arg1 = (Arg1) + (*(uint64_t *)(Arg4 + (int32_t)((uint32_t)(Arg1)) * 8 + 0x3A60));
    v_stack_mB0 = *(uint64_t *)(Arg4 + (int32_t)((uint32_t)(Arg1)) * 8 + 0x3A60);
    result = ExpInterlockedPopEntrySList(Arg1, (int32_t)((uint32_t)(Arg1)), (uint32_t)((uint32_t)((uint8_t)(local_rsi))), Arg4);
    if (result == 0) goto loc_00288F55;
loc_0028887C:
    *(uint64_t *)(result + 0x10) = *(uint64_t *)(v_rip - 0x27800C);
    if (v_stack_m100 != 0) goto loc_00289050;
    if (sign_flag) goto loc_002896C0;
loc_002888A4:
    Arg4 = 0;
    *(uint64_t *)(result) = 0;
    goto loc_002888BF;
loc_002888B0:
    result = MiGetPerfectColorHeadPage(v_stack_m98, (int32_t)((uint32_t)(Arg1)), (uint32_t)((uint32_t)((uint8_t)(local_rsi))), Arg4);
    Arg4 = 0;
loc_002888BF:
    if (result >= 2) goto loc_00288AFD;
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rsi))) >> (16));
    result = (uint32_t)((result) & (3));
    local_rsi = (uint32_t)((local_rsi) >> (15));
    local_rsi = (uint32_t)((local_rsi) & (1));
    v_stack_m114 = (uint32_t)(result);
    Arg3 = (result + result * 4) << (8);
    Arg3 = (Arg3) + (v_stack_mF8);
    if (v_stack_mD8 == 0) goto loc_002890D9;
    if ((((uint8_t)((uint32_t)(Arg3))) & (32)) == 0) goto loc_002893DA;
    result = ((uint32_t)(v_stack_mA8)) + (4);
    Arg2 = (result + local_rsi * 4) << (5);
    Arg2 = (Arg2) + (Arg3);
loc_00288912:
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg3)))) & (0xFFFFFFEFULL));
loc_00288917:
    if (Arg2 == 0) goto loc_00288963;
    Arg3 = (*(uint64_t *)(Arg2)) >> (3);
    v_stack_m60 = v_xmm0;
    v_stack_m50 = v_xmm0;
    result = memcpy(v_stack_m60, *(uint64_t *)(Arg2 + 0x8), Arg3, Arg4);
    result = 0;
loc_00288946:
    Arg3 = (uint32_t)((0) + (0));
    if (Arg3 >= 8) goto loc_002893AD;
    Arg2 = (uint32_t)((0) + 1);
    Arg1 = (v_stack_m60) + (8);
    if (Arg2 < 4) goto loc_00288946;
loc_00288963:
    result = MiGetPerfectFreeOrZeroPage(v_stack_mF8, (uint32_t)((uint32_t)((uint32_t)(v_stack_m118))), (uint32_t)((uint32_t)(local_rsi)), Arg4);
    if (result >= 2) goto loc_00288AF6;
    if (v_stack_m114 == 3) {
        Arg1 = *(uint64_t *)(v_stack_mF8 + 0x3A88);
        Arg3 = (uint32_t)((uint32_t)(Arg3));
        Arg2 = (uint32_t)((uint32_t)(v_stack_m118));
        result = MiCheckZeroFreeRebalance(Arg1, Arg2, Arg3, Arg4);
    }
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m118)))) & (0x30000ULL));
    Arg1 = (((uint32_t)(result)) == 0x30000ULL) ? 1 : 0;
    result = ((((uint8_t)((uint32_t)(Arg3))) & (2)) == 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) == 0) goto loc_002889F3;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m118)))) >> (18));
    Arg1 = (uint32_t)((Arg1) & (3));
    result = MiCacheAttributeHasValue(Arg1, Arg2, Arg3, Arg4);
    if ((uint32_t)(result) == 0) goto loc_002889F3;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) << (16));
    Arg2 = (uint32_t)((Arg2) ^ ((uint32_t)((uint32_t)(v_stack_m118))));
    Arg2 = (uint32_t)((Arg2) & (0xC0000ULL));
    Arg2 = (uint32_t)((Arg2) ^ ((uint32_t)((uint32_t)(v_stack_m118))));
    result = MiDemoteLocalLargePage(*(uint64_t *)(v_stack_mF8 + 0x3A88), Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg4);
    if (result != 0) goto loc_00289448;
loc_002889F3:
    v_stack_mE0 = *(uint64_t *)(v_stack_mF8 + 0x3A88);
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m118)))) & (0x30000ULL));
    if (((uint32_t)(result)) != 0x30000ULL) goto loc_00288A2A;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m118)))) & (0xC0000ULL));
    if (((uint32_t)(result)) == 0x40000ULL) goto loc_002892B8;
loc_00288A2A:
    result = MiRemovePageAnyColor(v_stack_mE0, (uint32_t)((uint32_t)((uint32_t)(v_stack_m118))), (uint32_t)((uint32_t)((uint32_t)(Arg3))), 1);
    if (result == 2) goto loc_002890CD;
    if (result != 0) goto loc_002891EB;
    if ((((uint8_t)((uint32_t)(Arg3))) & (64)) != 0) goto loc_002891A7;
loc_00288A5F:
    if (condition_is_below) goto loc_002892DA;
    result = MiRemovePageAnyColor(v_stack_mE0, (uint32_t)((uint32_t)((uint32_t)(v_stack_m118))), (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg3))))), 1);
    if (result == 2) goto loc_002890CD;
    if (result != 0) goto loc_002891EF;
    goto loc_002891F9;
loc_00288AA1:
    result = MiPageAvailable(*(uint64_t *)(v_stack_mF8 + 0x3A88), (uint32_t)((uint32_t)((uint32_t)(Arg3))), (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg3))))), 1);
    if ((uint32_t)(result) == 0) goto loc_002890CD;
    result = (uint8_t)((v_stack_m66) + 1);
    v_stack_m66 = (uint8_t)(result);
    if (((uint8_t)(result)) < v_stack_m65) goto loc_00289757;
    if (((uint8_t)(v_stack_m64)) == 2) goto loc_002895C5;
loc_00288ADA:
    result = (uint32_t)(((uint8_t)(v_stack_m64)) << (8));
    result = (uint32_t)((result) ^ ((uint32_t)((uint32_t)(v_stack_m118))));
    result = (uint32_t)((result) & (256));
    local_rsi = (uint32_t)(((uint32_t)(v_stack_m118)) ^ ((uint32_t)(result)));
    v_stack_m118 = (uint32_t)(local_rsi);
    if (result == 0) goto loc_00289306;
loc_00288AF6:
    Arg4 = 0;
loc_00288AF9:
loc_00288AFD:
    if (result == 2) goto loc_002890CD;
    if (result == 0) goto loc_0028905A;
    local_rsi = (result) - (local_r12);
    local_rsi = (local_rsi) >> (4);
    local_rsi = (local_rsi) * (local_r12);
loc_00288B31:
    *(uint64_t *)(result) = 0;
    if (!(condition_is_above_or_equal)) {
        Arg1 = *(uint32_t *)(result + 0x24);
        Arg1 = (uint32_t)((Arg1) & (0x18000000ULL));
    }
    *(uint32_t *)(result + 0x24) = (uint32_t)(Arg1);
    if (((uint32_t)((int32_t)(*(uint32_t *)(v_rip + 0xBA5068)))) > ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBA5066))))) goto loc_00288B7F;
    result = ((int32_t)(*(uint32_t *)(v_rip + 0xBA5068))) << (4);
    result = (result) + (*(uint64_t *)(v_rip + 0xBA50B0));
    if (local_rsi < (*(uint64_t *)(result))) goto loc_00288B7F;
    if (((uint32_t)((int32_t)(*(uint32_t *)(v_rip + 0xBA5068)))) == ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBA5066))))) goto loc_00288BBA;
    if (local_rsi < (*(uint64_t *)(result + 0x10))) goto loc_00288BBA;
loc_00288B7F:
loc_00288B82:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBA5066)))) < 0) goto loc_00288CA4;
    Arg1 = (uint32_t)((0 + (uint32_t)(*(uint32_t *)(v_rip + 0xBA5066)) * 1) >> (1));
    result = ((int32_t)((uint32_t)(Arg1))) << (4);
    result = (result) + (*(uint64_t *)(v_rip + 0xBA5081));
    if (local_rsi < (*(uint64_t *)(result))) goto loc_002892E3;
    if (((uint32_t)(Arg1)) != (*(uint32_t *)(v_rip + 0xBA5016))) goto loc_0028903D;
loc_00288BB4:
    *(uint32_t *)(v_rip + 0xBA5006) = (uint32_t)(Arg1);
loc_00288BBA:
    if ((*(uint32_t *)(result + 0x8)) != ((uint32_t)(local_r15))) goto loc_00289605;
    if ((*(uint64_t *)(v_rip + 0xBA505C)) != 0) goto loc_00289182;
    result = 0;
loc_00288BD4:
    if (0 != ((uint8_t)(v_stack_m64))) goto loc_0028973A;
loc_00288BE2:
    if ((((uint8_t)((uint32_t)(Arg3))) & (32)) == 0) goto loc_00288C19;
    local_r14 = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) >> (2));
    local_r14 = (uint32_t)((local_r14) & (3));
    if (((*(uint64_t *)(result + 0x10)) & (992)) != 0) goto loc_00288E86;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x20))) >> (16));
    Arg1 = (uint32_t)(((uint8_t)(result)) >> (6));
    if (((uint32_t)(Arg1)) != ((uint32_t)(local_r14))) goto loc_00288E6C;
loc_00288C19:
    if ((((uint8_t)((uint32_t)(Arg3))) & (8)) == 0) goto loc_00289017;
loc_00288C23:
loc_00288C26:
    Arg1 = (v_stack_m40) ^ (local_rsp);
    result = _security_check_cookie(Arg1, (uint32_t)(*(uint32_t *)(v_rip + 0xBA5066)), 0, Arg4);
    local_rsp = (local_rsp) + (272);
    return result;
loc_00288C4E:
    goto loc_0028854A;
loc_00288C56:
    v_stack_m66 = 0;
    if (((uint8_t)(v_stack_m65)) <= 1) goto loc_0028861A;
    result = (uint8_t)(~(*(uint8_t *)(Arg4 + 0x3B50)));
    result = (uint8_t)((result) & (1));
    v_stack_m63 = (uint8_t)(result);
    v_stack_m68 = (uint16_t)(*(uint16_t *)(Arg4 + 0x3B81));
    if (condition_is_above_or_equal) goto loc_0028861A;
    Arg2 = 0;
loc_00288CA4:
    v_stack_p20 = 0;
    Arg4 = 0;
    result = KeBugCheckEx(Arg4 + 26, (uint32_t)(0x5180ULL), local_rsi, Arg4);
loc_00288CBE:
loc_00288CC3:
    result = (uint32_t)(((uint32_t)((uint32_t)(v_stack_p20))) & (0xFFFFF80FULL));
    local_r10 = (uint32_t)(((uint32_t)((uint32_t)(local_rsi))) >> (16));
    local_r11 = (uint32_t)(((uint32_t)((uint32_t)(local_rsi))) >> (15));
    Arg2 = (uint32_t)((16) << ((uint8_t)((uint32_t)((uint32_t)(v_stack_p40)))));
    local_r11 = (uint32_t)((local_r11) & (1));
    Arg2 = (uint32_t)((Arg2) | ((uint32_t)(v_stack_p20)));
    v_stack_p34 = (uint32_t)(local_r11);
    Arg2 = (uint32_t)((Arg2) & (240));
    local_r10 = (uint32_t)((local_r10) & (3));
    local_rbx = (uint32_t)(((uint32_t)(Arg2)) | ((uint32_t)(result)));
    local_rdi = 0;
loc_00288D02:
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) >> (8));
    Arg3 = (uint32_t)((Arg3) & (7));
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) >> (4));
    Arg2 = (uint32_t)((1) << ((uint8_t)((uint32_t)(Arg3))));
    Arg2 = (uint32_t)((Arg2) & ((uint32_t)(result)));
    if ((((uint8_t)(Arg2)) & (15)) != 0) goto loc_00288DB4;
    Arg2 = (local_r10 + local_r10 * 4) << (8);
    Arg2 = (Arg2) + (0);
    result = (uint32_t)((uint32_t)(local_r11));
    if (((uint32_t)(local_r10)) == 3) { result = 0; }
    if (*(uint64_t *)(Arg2 + Arg3 + result * 4 * 8 + 0x18) != 0) goto loc_00288DD5;
    if ((uint16_t)(*(uint64_t *)(Arg4 + 0x3B60)) != 0) goto loc_00288DD5;
loc_00288D59:
    if (0 > ((uint32_t)(local_r10))) goto loc_00288D80;
    Arg1 = (0 + 0 * 4) << (8);
    if (*(uint64_t *)(Arg1 + Arg4 * 1 + 0x8) != 0) goto loc_00288DD5;
    if (*(uint64_t *)(Arg1 + Arg4 * 1 + 0x10) != 0) goto loc_00288DD5;
    Arg2 = (uint32_t)((0) + 1);
    goto loc_00288D59;
loc_00288D80:
    if (((uint32_t)(local_r10)) != 3) goto loc_00288D92;
    Arg3 = (uint8_t)((Arg3) & ((uint8_t)(local_r10)));
    if (((uint8_t)(Arg3)) == 1) goto loc_002890F8;
loc_00288D92:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) >> (8));
    Arg1 = (uint32_t)((Arg1) & (7));
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) & (0xFFFFFF0FULL));
    Arg2 = (uint32_t)((16) << ((uint8_t)(Arg1)));
    Arg2 = (uint32_t)((Arg2) | ((uint32_t)(local_rbx)));
    Arg2 = (uint32_t)((Arg2) & (240));
    local_rbx = (uint32_t)(((uint32_t)(Arg2)) ^ ((uint32_t)(result)));
loc_00288DB4:
    result = (uint32_t)((local_rbx + 256) ^ ((uint32_t)(local_rbx)));
    result = (uint32_t)((result) & (0x700ULL));
    local_rbx = (uint32_t)((local_rbx) ^ ((uint32_t)(result)));
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) & (0x700ULL));
    if (((uint32_t)(result)) <= 768) goto loc_00288D02;
loc_00288DD5:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) & (240));
    if (((uint8_t)(result)) != 240) goto loc_0028933E;
loc_00288DEB:
    if ((uint32_t)((uint32_t)(v_stack_p58)) != 0) goto loc_00288E31;
    result = (uint32_t)(0x3B58ULL);
    if (v_stack_p38 != 3) { result = (uint32_t)((uint32_t)(0x3B60ULL)); }
    Arg1 = 0;
    result = (result) + (0);
    v_stack_mB0 = result;
    if ((uint16_t)(*(uint64_t *)(result)) != 0) goto loc_002894E9;
loc_00288E1E:
    Arg1 = (*(uint64_t *)(result)) ^ (local_r12);
    if (((Arg1) & (0xFFFFFFFFFFFF0000ULL)) != 0) goto loc_0028914C;
loc_00288E31:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) >> (2));
    result = (uint32_t)((result) ^ ((uint32_t)(local_rbx)));
    result = (uint32_t)((result) & (3));
    local_rbx = (uint32_t)((local_rbx) ^ ((uint32_t)(result)));
    if ((uint32_t)((uint32_t)(v_stack_p58)) == 0) goto loc_0028915E;
loc_00288E4C:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) >> (2));
    Arg1 = (uint32_t)((Arg1) & (3));
    result = (uint32_t)((1) << ((uint8_t)(Arg1)));
    result = (uint32_t)(~(result));
    result = (uint32_t)((result) << (4));
    result = (uint32_t)((result) ^ ((uint32_t)(local_rbx)));
    result = (uint32_t)((result) & (240));
    local_rbx = (uint32_t)((local_rbx) ^ ((uint32_t)(result)));
    goto loc_0028916A;
loc_00288E6C:
    result = (uint8_t)((1) << ((uint8_t)(Arg1)));
    if (((*(uint8_t *)(v_rip + 0xBA4E58)) & ((uint8_t)((uint8_t)(result)))) == 0) goto loc_00288C19;
loc_00288E86:
    local_r15 = (uint32_t)(((uint32_t)(v_stack_p30)) >> (16));
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_mC0) * 8))) | (1));
    local_r15 = (uint32_t)((local_r15) & (3));
    if ((((uint8_t)((uint32_t)(v_stack_mC0))) & (32)) == 0) { local_rbx = (uint32_t)((uint32_t)(v_stack_mC0) * 8); }
    local_rdi = (result) - (local_r12);
    local_rdi = (local_rdi) >> (4);
    local_rdi = (local_rdi) * (local_r12);
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) & (8));
    result = (uint32_t)((result) | (4));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x20))) >> (16));
    result = (uint8_t)((result) & (192));
    v_stack_p38 = (uint32_t)(result + result * 1);
    if (((uint8_t)(result)) == 192) goto loc_0028989D;
loc_00288EE1:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x20))) >> (16));
    result = 0;
    Arg1 = (uint32_t)(((uint8_t)(result)) >> (6));
    result = (((uint32_t)(Arg1)) != ((uint32_t)(local_r14))) ? 1 : 0;
    if ((((uint8_t)(local_rbx)) & (1)) == 0) goto loc_00288F39;
    if (((uint32_t)(Arg1)) != ((uint32_t)(local_r14))) goto loc_002895D7;
loc_00288F07:
    Arg1 = 0;
    if (((uint32_t)(local_r15)) != 3) goto loc_002898C0;
    local_rbx = (uint32_t)((local_rbx) >> (2));
    local_rbx = (uint32_t)((local_rbx) & (2));
    result = MiZeroPhysicalPage(Arg1, local_rdi, (uint32_t)((uint32_t)(local_rbx)), (uint32_t)((uint32_t)(local_r14)));
loc_00288F27:
    result = (*(uint64_t *)(result + 0x10)) & (-993);
    *(uint64_t *)(result + 0x10) = result;
loc_00288F39:
    if ((uint32_t)((uint32_t)((uint32_t)(result))) == 0) goto loc_00288C23;
    result = MiChangePageAttribute(result, (uint32_t)((uint32_t)(local_r14)), (uint32_t)((uint32_t)((uint32_t)(v_stack_p38))), (uint32_t)((uint32_t)(local_r14)));
    goto loc_00288C23;
loc_00288F55:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) >> (1));
    result = (uint32_t)((result) | ((uint32_t)(local_rdi)));
    if ((((uint8_t)(result)) & (1)) == 0) goto loc_002893E2;
    v_stack_mC8 = 17;
loc_00288F67:
    Arg4 = (uint32_t)((v_stack_p60) & (31));
    Arg1 = (v_stack_p60) >> (5);
    if ((Arg4 + 1) > 32) goto loc_00289488;
    result = (uint32_t)((1) << ((uint8_t)((uint32_t)(Arg4))));
    result = (uint32_t)(~(result));
loc_00288FA8:
loc_00288FAC:
    Arg1 = (v_stack_p60) << (4);
    Arg1 = (Arg1) + (v_stack_mB0);
    result = ExpInterlockedPopEntrySList(Arg1, 1, v_stack_p60, Arg4);
    if (result != 0) goto loc_00289552;
    if (((uint8_t)(v_stack_mC8)) == 17) goto loc_00288FEF;
    if ((*(uint32_t *)(v_rip + 0xD3DD48)) != ((uint32_t)(result))) {
        Arg1 = v_cr8;
        Arg2 = (uint8_t)(v_stack_mC8);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, v_stack_p60, Arg4);
    }
loc_00288FEF:
loc_00288FFD:
    if (((uint32_t)((uint32_t)(v_stack_p48))) == ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m88 + 0x4))))) goto loc_002888B0;
    v_stack_p48 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m88 + 0x4)));
    goto loc_00288831;
loc_00289017:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_mC8 + 0x20))) >> (16));
    local_r14 = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) >> (2));
    local_r14 = (uint32_t)((local_r14) & (3));
    result = (uint32_t)(((uint8_t)(result)) >> (6));
    if (((uint32_t)(result)) == ((uint32_t)(local_r14))) goto loc_00288C23;
    goto loc_00288E86;
loc_0028903D:
    if (((uint32_t)(v_stack_p30)) < (*(uint64_t *)(result + 0x10))) goto loc_00288BB4;
    goto loc_00288B82;
loc_00289050:
    result = MiSetOriginalPtePfnFromFreeList((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m88 + 0x4)))), (uint32_t)(*(uint32_t *)(v_stack_m88 + 0x4)), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m88 + 0x4)))) + 1, v_stack_p50);
    goto loc_002888A4;
loc_0028905A:
    if ((((uint8_t)(local_rdi)) & (2)) != 0) goto loc_002890CD;
    if (condition_is_below) goto loc_002890CD;
    if ((((uint32_t)(local_rdi)) & (0x3000ULL)) != 0) goto loc_002897A2;
loc_00289076:
    result = MiRemoveLowestPriorityStandbyPage(v_stack_mB8, 8, (uint32_t)((uint32_t)(local_rdi)), v_stack_p50);
    if (result == -1) goto loc_002890CD;
    local_r13 = (result + result * 2) << (4);
    local_r13 = (local_r13) + ((uint32_t)((uint32_t)(result)));
    Arg4 = 0;
    goto loc_00288B31;
loc_002890AF:
    if ((((uint8_t)(*(uint64_t *)(v_rip + 0xD3D9D2))) & (48)) == 0) goto loc_002885EC;
    result = MiPageAvailable((uint32_t)((uint32_t)(result)), (uint32_t)((uint32_t)(local_rdi)), (uint32_t)((uint32_t)(local_rdi)), Arg4);
    if ((uint32_t)(result) != 0) goto loc_00289786;
loc_002890CD:
    goto loc_00288C26;
loc_002890D9:
    Arg2 = ((uint32_t)(v_stack_mA8) + result * 4) << (5);
    Arg2 = (Arg2) + (144);
    Arg2 = (Arg2) + ((uint32_t)((uint32_t)(local_rdi)));
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) | (16));
    goto loc_00288917;
loc_002890F8:
loc_00289102:
    if (((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) >= 2) goto loc_002897BF;
    result = ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi))))) + (928);
    result = (result) + (result);
    if (*(uint64_t *)(Arg4 + result * 8) == 0) goto loc_00288DD5;
    if (((uint32_t)(*(uint32_t *)(v_rip + 0xBA4BCD))) > local_rsi) goto loc_00289355;
    if (((uint32_t)(*(uint32_t *)(v_rip + 0xBA4BCD))) != local_rsi) goto loc_00288DD5;
    if (((uint32_t)(*(uint32_t *)(v_rip + 0xBA4BCD))) < local_rsi) goto loc_00288DD5;
loc_00289147:
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) + 1);
    goto loc_00289102;
loc_0028914C:
    local_r14 = (uint32_t)((local_r14) - 1);
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBA4BCD))))) >> (2));
    local_rbx = (uint32_t)((local_rbx) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBA4BCD)))));
    local_rbx = (uint32_t)((local_rbx) & (3));
    local_rbx = (uint32_t)((local_rbx) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBA4BCD)))));
loc_0028915E:
loc_00289164:
    local_rbx = (uint32_t)((local_rbx) & (0xFFFFFF0FULL));
loc_0028916A:
    local_r14 = (uint32_t)((local_r14) + 1);
    Arg4 = 0;
    goto loc_00288597;
loc_00289182:
    Arg1 = (local_r13) - (*(uint64_t *)(Arg4 + result * 8 + 0x8));
    Arg1 = (Arg1) >> (4);
    Arg1 = (Arg1) * (*(uint64_t *)(Arg4 + result * 8 + 0x8));
    result = MiPageToChannel(Arg1, (uint32_t)(v_stack_p78), (uint32_t)(v_stack_p38), Arg4);
    goto loc_00288BD4;
loc_002891A7:
    local_rsi = (uint32_t)((local_rsi) & (0xFFFFFFBFULL));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_p30)))) & (0x30000ULL));
    if (((uint32_t)(result)) != 0x30000ULL) goto loc_00288A5F;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_p30)))) & (0xC0000ULL));
    if (((uint32_t)(result)) != 0x40000ULL) goto loc_00288A5F;
    result = MiGetPageSlist(v_stack_p50, (uint32_t)(v_stack_p30), (uint32_t)((uint32_t)(local_rsi)), Arg4);
    if (result == 0) goto loc_00288A5F;
loc_002891EB:
loc_002891EF:
    if (result >= 2) goto loc_00288AF6;
loc_002891F9:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) | (16));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) & (0xFFFFFFEFULL));
    if (v_stack_p70 == 0) { Arg1 = (uint32_t)(result); }
    result = 0;
    v_stack_p34 = 0;
    v_stack_p48 = (uint32_t)(Arg1);
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_p30)))) & (0x30000ULL));
    Arg1 = (((uint32_t)(result)) == 0x30000ULL) ? 1 : 0;
    result = ((((uint8_t)(local_rdi)) & (2)) == 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) == 0) goto loc_00289430;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_p30)))) >> (18));
    Arg1 = (uint32_t)((Arg1) & (3));
    if (((uint32_t)(Arg1 - 1)) > 1) goto loc_00289430;
    result = MiCacheAttributeHasValue(Arg1, (uint32_t)(v_stack_p30), (uint32_t)((uint32_t)(local_rsi)), 0);
    if ((uint32_t)(result) == 0) goto loc_00289282;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) << (16));
    Arg2 = (uint32_t)((Arg2) ^ ((uint32_t)((uint32_t)(v_stack_p30))));
    Arg2 = (uint32_t)((Arg2) & (0xC0000ULL));
    Arg2 = (uint32_t)((Arg2) ^ ((uint32_t)((uint32_t)(v_stack_p30))));
    result = MiDemoteLocalLargePage(*(uint64_t *)(v_stack_p50 + 0x3A88), Arg2, (uint32_t)((uint32_t)(local_rdi)), 0);
    if (result != 0) goto loc_00289461;
loc_00289282:
    Arg4 = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) >> (2));
    Arg4 = (uint32_t)((Arg4) & (3));
    v_stack_p20 = (uint32_t)((uint32_t)(v_stack_p34));
    result = MiGetFreeOrZeroPageAnyColor(v_stack_p50, (uint32_t)((uint32_t)((uint32_t)(v_stack_p30))), (uint32_t)(v_stack_p48), Arg4);
    if (result >= 2) goto loc_00288AF6;
    goto loc_00288AA1;
loc_002892B8:
    result = MiGetPageSlist(Arg4, (uint32_t)((uint32_t)(v_stack_p50)), (uint32_t)((uint32_t)(local_rdi)), Arg4);
    if (result != 0) goto loc_002891EB;
    goto loc_00288A2A;
loc_002892DA:
    goto loc_002891F9;
loc_002892E3:
    if ((uint32_t)((uint32_t)(v_stack_p30)) != 0) goto loc_00289895;
    v_stack_p20 = Arg4;
    result = KeBugCheckEx(26, (uint32_t)(0x5180ULL), (uint32_t)(v_stack_p30), result);
loc_00289306:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) & (3));
    result = (uint32_t)((16) << ((uint8_t)(Arg1)));
    local_rbx = (uint32_t)((local_rbx) | ((uint32_t)(result)));
    result = (uint32_t)(((uint32_t)(v_stack_p40)) & (0xFFFFFF0FULL));
    local_rbx = (uint32_t)((local_rbx) & (240));
    local_rbx = (uint32_t)((local_rbx) ^ ((uint32_t)(result)));
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) & (240));
    if (((uint8_t)(result)) != 240) goto loc_0028947A;
    goto loc_00288DEB;
loc_0028933E:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) >> (8));
    result = (uint32_t)((result) ^ ((uint32_t)(local_rbx)));
    result = (uint32_t)((result) & (3));
    local_rbx = (uint32_t)((local_rbx) ^ ((uint32_t)(result)));
    goto loc_0028879C;
loc_00289355:
    if (Arg1 < ((uint32_t)(0x5180ULL))) goto loc_00288DD5;
    result = (1 - 1) >> (6);
    v_stack_p60 = *(uint64_t *)(v_stack_p50 + result * 8 + 0x8) + result * 8;
    v_stack_p68 = *(uint64_t *)(*(uint64_t *)(v_stack_p50 + result * 8 + 0x8));
    if ((*(uint64_t *)(v_stack_p50 + result * 8 + 0x8)) != v_stack_p60) goto loc_002894A0;
    Arg1 = (uint8_t)((64) - ((uint8_t)((uint32_t)(0x5180ULL))));
    result = (-1) >> ((uint8_t)(Arg1));
loc_0028939D:
    result = (((v_stack_p68) & (result)) == 0) ? 1 : 0;
    if ((uint8_t)(result) == 0) goto loc_00288DD5;
    goto loc_00289147;
loc_002893AD:
    Arg4 = 0;
    result = MiRemovePageAnyColor(*(uint64_t *)(result + 0x3A88), (uint32_t)(v_stack_p30), (uint32_t)((uint32_t)(local_rdi)), Arg4);
    if (result >= 2) goto loc_00288AF6;
    goto loc_00288963;
loc_002893DA:
    goto loc_00288912;
loc_002893E2:
    v_stack_mC8 = (uint8_t)(v_stack_mC8);
    if ((*(uint32_t *)(v_rip + 0xD3D926)) == 0) goto loc_00288F67;
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)((uint8_t)(v_stack_mC8)), 2, (uint32_t)((uint32_t)(local_rdi)), Arg4);
    goto loc_00288F67;
loc_00289411:
loc_00289414:
    if (result != 0) goto loc_00288779;
    Arg1 = ((uint8_t)((uint8_t)(v_stack_mC8))) + (8);
    if (Arg1 == ((uint32_t)((uint32_t)(local_rdi)))) goto loc_002894D1;
    goto loc_00289414;
loc_00289430:
    if (v_stack_p58 == 0) { Arg4 = 1; }
    v_stack_p34 = Arg4;
    goto loc_00289282;
loc_00289448:
    result = MiObtainedPageIsGood(v_stack_p50, *(uint64_t *)((uint8_t)((uint8_t)(v_stack_mC8)) + 0x8), (uint32_t)((uint32_t)(local_rdi)), Arg4);
    if ((uint32_t)(result) != 0) goto loc_00288AF6;
    goto loc_002889F3;
loc_00289461:
    result = MiObtainedPageIsGood(v_stack_p50, *(uint64_t *)((uint8_t)((uint8_t)(v_stack_mC8)) + 0x8), (uint32_t)((uint32_t)(local_rdi)), Arg4);
    if ((uint32_t)(result) != 0) goto loc_00288AF6;
    goto loc_00289282;
loc_0028947A:
    local_r14 = (uint32_t)((local_r14) - 1);
    goto loc_0028916A;
loc_00289488:
    if (Arg4 != 0) goto loc_002897D8;
loc_00289491:
    result = (uint32_t)(((uint32_t)(0xFFFFFFFFULL)) << ((uint8_t)(*(uint64_t *)((uint8_t)((uint8_t)(v_stack_mC8)) + 0x8))));
    goto loc_00288FA8;
loc_002894A0:
    if (result != 0) goto loc_00288DD5;
loc_002894AE:
    Arg1 = (*(uint64_t *)((uint8_t)((uint8_t)(v_stack_mC8)) + 0x8)) + (8);
    v_stack_p60 = *(uint64_t *)(*(uint64_t *)((uint8_t)((uint8_t)(v_stack_mC8)) + 0x8) + 0x8);
    if (Arg1 == v_stack_p60) goto loc_00289538;
    if (v_stack_p60 == local_rdi) goto loc_002894AE;
    goto loc_00288DD5;
loc_002894D1:
    Arg1 = (uint8_t)(~((uint8_t)(v_stack_mA0)));
    result = (-1) >> ((uint8_t)(Arg1));
    goto loc_00288772;
loc_002894E9:
loc_002894F0:
    local_r15 = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) + 1);
    if (((*(uint32_t *)(v_rip + 0xD3BDB2)) & ((uint32_t)(local_r15))) == 0) goto loc_00289698;
loc_00289500:
loc_00289502:
    if ((uint16_t)(*(uint64_t *)(v_stack_mB0)) != 0) goto loc_002894F0;
    goto loc_00288E1E;
loc_0028951F:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) >> (2));
    result = (uint32_t)((1) << ((uint8_t)(Arg1)));
    result = (uint32_t)(~(result));
    result = (uint32_t)((result) & (15));
    result = (uint32_t)((result) << (4));
    local_rbx = (uint32_t)((local_rbx) | ((uint32_t)(result)));
    goto loc_00288521;
loc_00289538:
    Arg1 = (uint8_t)(~(1 - 1));
    result = (-1) >> ((uint8_t)(Arg1));
    goto loc_0028939D;
loc_00289552:
    Arg1 = ((uint32_t)((uint32_t)((uint32_t)(v_stack_p34)))) >> (5);
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_p34)))) & (31));
    if ((Arg1 + 1) > 32) goto loc_00289680;
    result = (uint32_t)((1) << ((uint8_t)(Arg1)));
loc_00289590:
loc_00289594:
    if (((uint8_t)(v_stack_mC8)) == 17) goto loc_0028887C;
    result = v_stack_mC8;
    if ((*(uint32_t *)(v_rip + 0xD3D779)) != 0) {
        Arg1 = 2;
        Arg2 = (uint8_t)(v_stack_mC8);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, (uint32_t)(v_stack_p34), *(uint64_t *)(v_stack_p68 + 0x8) + Arg1 * 4);
        result = v_stack_mC8;
    }
    goto loc_0028887C;
loc_002895C5:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_p30)))) >> (9));
    Arg1 = (uint32_t)((Arg1) & (63));
    result = MiAssignDefaultChannel(Arg1, Arg2, (uint32_t)(v_stack_p34), *(uint64_t *)(v_stack_p68 + 0x8) + Arg1 * 4);
    goto loc_00288ADA;
loc_002895D7:
    result = MiPfnBestZeroAttribute(v_stack_p50, (uint32_t)((uint32_t)(local_r14)), (uint32_t)(v_stack_p34), *(uint64_t *)(v_stack_p68 + 0x8) + Arg1 * 4);
    if (((uint32_t)(result)) != ((uint32_t)(local_r14))) goto loc_00288F07;
    result = MiChangePageAttribute(v_stack_p50, (uint32_t)((uint32_t)(local_r14)), (uint32_t)(v_stack_p38), *(uint64_t *)(v_stack_p68 + 0x8) + Arg1 * 4);
    result = 0;
    goto loc_00288F07;
loc_00289605:
loc_0028960F:
    if ((((uint8_t)(local_rdi)) & (2)) != 0) goto loc_00289748;
    local_rsi = (uint32_t)(v_stack_p30);
    local_r13 = v_stack_p50;
    if (!(condition_is_below)) {
        Arg4 = (uint32_t)(local_rdi);
        Arg3 = (uint8_t)(v_stack_m64);
        Arg2 = (uint32_t)((uint32_t)(v_stack_p74));
        Arg1 = (uint32_t)(v_stack_p30);
        result = MiSwapNumaStandbyPage(Arg1, Arg2, Arg3, Arg4);
        local_rsi = result;
        local_r13 = result + result * 2;
        local_r13 = (local_r13) << (4);
        result = result;
        local_r13 = (local_r13) + (result);
    }
    if (condition_is_above_or_equal) goto loc_0028971C;
    result = MiPageToNode(local_rsi, Arg2, Arg3, Arg4);
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(v_stack_p74)))) goto loc_0028971C;
loc_0028966C:
    result = MiReleaseFreshPage(local_r13, Arg2, Arg3, Arg4);
    goto loc_00288C26;
loc_00289680:
    if (local_r13 != 0) goto loc_00289835;
loc_00289689:
    result = (uint32_t)((1) << ((uint8_t)(Arg2)));
    result = (uint32_t)((result) - 1);
    goto loc_00289590;
loc_00289698:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD3D41A)))) & (64)) == 0) goto loc_00289500;
    result = KiCheckVpBackingLongSpinWaitHypercall(Arg2, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00289500;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)((uint32_t)(v_stack_p74))), Arg2, Arg3, Arg4);
    goto loc_00289502;
loc_002896C0:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xBA6BAA))) + 1);
    *(uint32_t *)(v_rip + 0xBA6B9C) = (uint32_t)(result);
    if (((*(uint32_t *)(v_rip + 0xD3B986)) & ((uint32_t)(result))) != 0) goto loc_002888A4;
    Arg1 = (local_r13) - (result);
    Arg1 = (Arg1) >> (4);
    Arg1 = (Arg1) * (result);
    result = MiArePageContentsZero(Arg1, 1, Arg3, Arg4);
    Arg4 = 0;
    *(uint64_t *)(local_r13) = 0;
    goto loc_002888BF;
loc_0028971C:
    if (condition_is_above_or_equal) goto loc_00289748;
    result = MiGetPfnChannel(local_r13, 1, Arg3, Arg4);
    if (((uint8_t)(result)) == ((uint8_t)(v_stack_m64))) goto loc_00289748;
    if ((uint8_t)(v_stack_m63) == 0) goto loc_0028966C;
    goto loc_00289748;
loc_0028973A:
    if ((uint8_t)(v_stack_m63) == 0) goto loc_0028960F;
loc_00289748:
    goto loc_00288BE2;
loc_00289757:
    if (((uint8_t)(*(uint8_t *)(v_stack_m48 + (uint8_t)(result) * 1 - 0x20))) == 2) goto loc_002897C9;
loc_00289763:
    result = (uint32_t)(((uint8_t)(*(uint8_t *)(v_stack_m48 + (uint8_t)(result) * 1 - 0x20))) << (8));
    result = (uint32_t)((result) ^ ((uint32_t)(local_rsi)));
    result = (uint32_t)((result) & (256));
    local_rsi = (uint32_t)((local_rsi) ^ ((uint32_t)(result)));
    goto loc_002887BF;
loc_00289786:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) >> (2));
    result = (uint32_t)((result) ^ ((uint32_t)(local_rbx)));
    result = (uint32_t)((result) & (3));
    local_rbx = (uint32_t)((local_rbx) ^ ((uint32_t)(result)));
    if (v_stack_p58 == 0) goto loc_00289164;
    goto loc_00288E4C;
loc_002897A2:
    result = MiCheckNodeChannelStandbyCount(local_rsi, (uint32_t)((uint32_t)((uint32_t)(v_stack_p74))), v_stack_m64, v_stack_p50);
    if ((uint32_t)(result) != 0) goto loc_00289076;
    goto loc_002890CD;
loc_002897BF:
    goto loc_00288D92;
loc_002897C9:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_rsi))) >> (9));
    Arg1 = (uint32_t)((Arg1) & (63));
    result = MiAssignDefaultChannel(Arg1, (uint32_t)((uint32_t)((uint32_t)(v_stack_p74))), v_stack_m64, v_stack_p50);
    goto loc_00289763;
loc_002897D8:
    result = (uint32_t)(((uint32_t)((uint32_t)(v_stack_m64))) & (31));
    Arg2 = (uint32_t)((32) - ((uint32_t)(result)));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_p34)))) << ((uint8_t)((uint32_t)(Arg2))));
    result = (uint32_t)((result) - 1);
    result = (uint32_t)((result) << ((uint8_t)(v_stack_p50)));
    result = (uint32_t)(~(result));
    local_r10 = ((uint32_t)((uint32_t)((uint32_t)(v_stack_p34)))) + (4);
    Arg2 = ((uint32_t)(v_stack_p34)) - ((uint32_t)(Arg2));
    if (Arg2 < 32) goto loc_00289827;
    Arg1 = (Arg2) >> (5);
    result = ((uint32_t)(Arg2)) * (Arg1);
    Arg2 = (Arg2) + (result);
    result = 0;
loc_0028981B:
    *(uint32_t *)(local_r10) = 0;
    local_r10 = (local_r10) + (4);
    Arg1 = (Arg1) - ((uint32_t)(v_stack_p34));
    if (condition_is_not_equal) goto loc_0028981B;
loc_00289827:
    if (Arg2 == 0) goto loc_00288FAC;
    goto loc_00289491;
loc_00289835:
    Arg3 = (uint32_t)((v_stack_m64) & (31));
    Arg2 = (uint32_t)((32) - (Arg3));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_p34)))) << ((uint8_t)((uint32_t)(Arg2))));
    Arg1 = (uint8_t)(((uint8_t)(local_r10)) & (31));
    result = (uint32_t)((result) - 1);
    result = (uint32_t)((result) << ((uint8_t)(Arg1)));
    Arg4 = (v_stack_p50) + (4);
    Arg2 = ((uint32_t)(v_stack_p34)) - ((uint32_t)(Arg2));
    if (Arg2 < 32) goto loc_00289887;
    Arg1 = (Arg2) >> (5);
    result = ((uint32_t)(Arg2)) * (Arg1);
    Arg2 = (Arg2) + (result);
loc_00289877:
    *(uint32_t *)(Arg4) = 0xFFFFFFFFULL;
    Arg4 = (Arg4) + (4);
    Arg1 = (Arg1) - ((uint32_t)(v_stack_p34));
    if (condition_is_not_equal) goto loc_00289877;
loc_00289887:
    if (Arg2 == 0) goto loc_00289594;
    goto loc_00289689;
loc_00289895:
    goto loc_00288B82;
loc_0028989D:
    result = MiPfnBestZeroAttribute(local_r13, (uint32_t)((uint32_t)(v_stack_m64)), Arg3, Arg4);
    result = MiChangePageAttribute(local_r13, (uint32_t)((uint32_t)(result)), (uint32_t)(v_stack_p38), Arg4);
    goto loc_00288EE1;
loc_002898C0:
    local_rbx = (uint32_t)((local_rbx) >> (3));
    local_rbx = (uint32_t)((local_rbx) & (1));
    v_stack_p20 = (uint32_t)(local_rbx);
    result = MiZeroLargePage(local_r13, local_r13, (uint32_t)((uint32_t)((uint32_t)(v_stack_p74))), Arg4);
    goto loc_00288F27;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002884C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
