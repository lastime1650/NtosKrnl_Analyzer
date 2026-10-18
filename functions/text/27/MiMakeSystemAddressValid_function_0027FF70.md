# MiMakeSystemAddressValid

- RVA: `0x0027FF70`–`0x00280D0A` (길이 `3,482` bytes)
- VA: `0x000000014027FF70`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000666C4`
- 디코드: `795`개 명령, `3,482/3,482` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **32**; 고유 호출 대상: **25**
- 직접 호출자로 확인된 함수: **37**
- RIP 상대 이미지 참조: **10**

### Outgoing calls
- `0x002800B2` → [MmIsAddressValidEx](MmIsAddressValidEx_function_0027FDD0.md) (function, `0x0027FDD0`)
- `0x002800C6` → [MiUnlockWorkingSetExclusive](MiUnlockWorkingSetExclusive_function_0027EC70.md) (function, `0x0027EC70`)
- `0x002800D8` → [MmAccessFault](MmAccessFault_function_0027EE80.md) (function, `0x0027EE80`)
- `0x00280351` → [MiWriteValidPteNewProtection](../28/MiWriteValidPteNewProtection_function_00281810.md) (function, `0x00281810`)
- `0x00280444` → [KxWaitForLockOwnerShip](../25/KxWaitForLockOwnerShip_function_00257EB0.md) (function, `0x00257EB0`)
- `0x002804C6` → [MiFastLockLeafPageTable](MiFastLockLeafPageTable_function_00276340.md) (function, `0x00276340`)
- `0x0028066A` → [ExpAcquireSpinLockSharedAtDpcLevelInstrumented](ExpAcquireSpinLockSharedAtDpcLevelInstrumented_function_0027CD20.md) (function, `0x0027CD20`)
- `0x00280748` → [KxWaitForLockChainValid](../21/KxWaitForLockChainValid_function_00217AA0.md) (function, `0x00217AA0`)
- `0x0028076B` → [KeWakeAddressAll](../21/KeWakeAddressAll_function_00217C20.md) (function, `0x00217C20`)
- `0x00280865` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x00280888` → [KiReleaseQueuedSpinLockInstrumented](../21/KiReleaseQueuedSpinLockInstrumented_function_002179F0.md) (function, `0x002179F0`)
- `0x00280935` → [ExpWaitForSpinLockSharedAndAcquire](../36/ExpWaitForSpinLockSharedAndAcquire_function_00362380.md) (function, `0x00362380`)
- `0x00280965` → [KiAcquireQueuedSpinLockInstrumented](KiAcquireQueuedSpinLockInstrumented_function_00275850.md) (function, `0x00275850`)
- `0x0028097D` → [KiAcquireQueuedSpinLockInstrumented](KiAcquireQueuedSpinLockInstrumented_function_00275850.md) (function, `0x00275850`)
- `0x002809FA` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x00280A55` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x00280A65` → [MiUnlockWorkingSetShared](MiUnlockWorkingSetShared_function_0027D690.md) (function, `0x0027D690`)
- `0x00280B07` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00280B16` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00280B2D` → [KxWaitForLockOwnerShip](../25/KxWaitForLockOwnerShip_function_00257EB0.md) (function, `0x00257EB0`)
- `0x00280B54` → [MiLockWorkingSetExclusive](../32/MiLockWorkingSetExclusive_function_003238A0.md) (function, `0x003238A0`)
- `0x00280B7F` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00280BB8` → [MiCheckLinearProtectedPteAccessedBit](../29/MiCheckLinearProtectedPteAccessedBit_function_00292D80.md) (function, `0x00292D80`)
- `0x00280BD0` → [ExAcquireSpinLockExclusiveAtDpcLevel](../24/ExAcquireSpinLockExclusiveAtDpcLevel_function_00248E80.md) (function, `0x00248E80`)
- `0x00280C01` → [ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented](../2C/ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented_function_002C0F44.md) (function, `0x002C0F44`)
- `0x00280C48` → [ExpReleaseSpinLockSharedFromDpcLevelInstrumented](../2F/ExpReleaseSpinLockSharedFromDpcLevelInstrumented_function_002F0F48.md) (function, `0x002F0F48`)
- `0x00280C67` → [MiFlushAllFilesystemPages](../4E/MiFlushAllFilesystemPages_function_004E141C.md) (function, `0x004E141C`)
- `0x00280C80` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00280C90` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00280C9C` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00280CB2` → [ExAcquireSpinLockExclusiveAtDpcLevel](../24/ExAcquireSpinLockExclusiveAtDpcLevel_function_00248E80.md) (function, `0x00248E80`)
- `0x00280CEF` → [ExReleaseSpinLockExclusiveFromDpcLevel](../24/ExReleaseSpinLockExclusiveFromDpcLevel_function_002497E0.md) (function, `0x002497E0`)

### Direct callers
- [MiHandleForkTransitionPte](../22/MiHandleForkTransitionPte_function_0022D34C.md) at `0x0022DA16`
- [MiCloneVads](../22/MiCloneVads_function_0022DC1C.md) at `0x0022DFAC`
- [MiBuildForkPte](../22/MiBuildForkPte_function_0022E32C.md) at `0x0022F13E`
- [sub_002434A4](../24/Unknown_function_002434A4.md) at `0x002434CA`
- [MiCaptureDeleteHierarchy](MiCaptureDeleteHierarchy_function_0027F5F0.md) at `0x0027F731`
- [MiSetReadOnlyOnSectionView](../29/MiSetReadOnlyOnSectionView_function_00294538.md) at `0x002947AB`
- [MiInsertViewOfPhysicalSection](../2A/MiInsertViewOfPhysicalSection_function_002A57E0.md) at `0x002A58CA`
- [MiSplitPrivatePage](../2A/MiSplitPrivatePage_function_002A6210.md) at `0x002A63E1`
- [MiSplitPrivatePage](../2A/MiSplitPrivatePage_function_002A6210.md) at `0x002A6579`
- [MiMakeProtoLeafValid](../2A/MiMakeProtoLeafValid_function_002A6710.md) at `0x002A67F5`
- [MiMapLockedPagesInUserSpaceHelper](../2A/MiMapLockedPagesInUserSpaceHelper_function_002ADFE0.md) at `0x002AE1E2`
- [MiWorkingSetInfoCheckPageTable](../2A/MiWorkingSetInfoCheckPageTable_function_002AEFCC.md) at `0x002AF06E`
- [sub_002C3A7C](../2C/Unknown_function_002C3A7C.md) at `0x002C3C2F`
- [MiProtectPrivateMemory](../2C/MiProtectPrivateMemory_function_002C45B0.md) at `0x002C475B`
- [MiProtectPrivateMemory](../2C/MiProtectPrivateMemory_function_002C45B0.md) at `0x002C4C81`
- [MiCommitExistingVad](../32/MiCommitExistingVad_function_0032A860.md) at `0x0032AD56`
- [MiSoftFaultMappedView](../36/MiSoftFaultMappedView_function_00365364.md) at `0x00365729`
- [MiCommitEnclavePages](../36/MiCommitEnclavePages_function_00367CCC.md) at `0x00367E2A`
- [MiAddPagesToEnclave](../36/MiAddPagesToEnclave_function_00367EEC.md) at `0x0036809D`
- [MiWriteEnclavePte](../36/MiWriteEnclavePte_function_00368570.md) at `0x003685F7`
- [MiDecommitHardwareEnclavePages](../36/MiDecommitHardwareEnclavePages_function_003688D4.md) at `0x00368BAA`
- [MiCopyToUserVa](../3D/MiCopyToUserVa_function_003D1E68.md) at `0x003D1F31`
- [MiMapUserLargePages](../3D/MiMapUserLargePages_function_003D26F4.md) at `0x003D2B91`
- [NtLockVirtualMemory](../40/NtLockVirtualMemory_function_004088A0.md) at `0x00408F28`
- [MiFillHyperPtes](../46/MiFillHyperPtes_function_004644AC.md) at `0x004645C2`
- [MiLockPagedAddress](../48/MiLockPagedAddress_function_00484CDC.md) at `0x00484D51`
- [MiLockPageTableRange](../49/MiLockPageTableRange_function_0049A850.md) at `0x0049A91D`
- [MiBuildForkPageTable](../4A/MiBuildForkPageTable_function_004ACF5C.md) at `0x004AD042`
- [MiWriteAwePtes](../4C/MiWriteAwePtes_function_004C51E0.md) at `0x004C5740`
- [MiUpdatePrivateDemandZeroView](../4C/MiUpdatePrivateDemandZeroView_function_004CCC2C.md) at `0x004CCEA0`
- [MiProtectEnclavePages](../4D/MiProtectEnclavePages_function_004D5528.md) at `0x004D588A`
- [MiVadRangeIsIoSpace](../4D/MiVadRangeIsIoSpace_function_004D5CD4.md) at `0x004D5DA7`
- [MiQueryImageExtensionInformation](../4E/MiQueryImageExtensionInformation_function_004EE3C8.md) at `0x004EE566`
- [MiCommitHotPatchTable](../68/MiCommitHotPatchTable_function_00683420.md) at `0x00683578`
- [MiPrepareImagePagesForHotPatch](../68/MiPrepareImagePagesForHotPatch_function_00683800.md) at `0x0068395E`
- [MiQueryImageExtensionInformationOld](../68/MiQueryImageExtensionInformationOld_function_00687384.md) at `0x006874DE`
- [MiStoreDiscardPoisonedPage](../69/MiStoreDiscardPoisonedPage_function_00692858.md) at `0x00692B05`
- [MmStoreIsVirtualAddressPoisoned](../69/MmStoreIsVirtualAddressPoisoned_function_00693120.md) at `0x0069319B`
- [sub_006E362E](../6E/Unknown_function_006E362E.md) at `0x006E3886`

### Static image references
- `0x00280091` → RVA `0x00E2CB40` (`.data`; read)
- `0x00280112` → RVA `0x00E38840` (`.data`; read)
- `0x0028013F` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x0028014C` → RVA `0x00FC6B06` (`ALMOSTRO`; read)
- `0x00280155` → RVA `0x00F0DE58` (`.data`; read)
- `0x0028044E` → RVA `0x00FC6A88` (`ALMOSTRO`; read)
- `0x00280A32` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x00280AF9` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)
- `0x00280BDF` → RVA `0x00E380C0` (`.data`; read)
- `0x00280CA6` → RVA `0x00E374C0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00280CE3` → [sub_006DA136](../6D/Unknown_function_006DA136.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0027FF70  4C 8B DC                        mov r11, rsp
0027FF73  45 88 43 18                     mov byte ptr [r11 + 0x18], r8b
0027FF77  49 89 4B 08                     mov qword ptr [r11 + 8], rcx
0027FF7B  53                              push rbx
0027FF7C  55                              push rbp
0027FF7D  56                              push rsi
0027FF7E  57                              push rdi
0027FF7F  41 54                           push r12
0027FF81  41 55                           push r13
0027FF83  41 56                           push r14
0027FF85  41 57                           push r15
0027FF87  48 81 EC 18 01 00 00            sub rsp, 0x118
0027FF8E  0F 57 C0                        xorps xmm0, xmm0
0027FF91  41 8B D9                        mov ebx, r9d
0027FF94  0F 11 84 24 90 00 00 00         movups xmmword ptr [rsp + 0x90], xmm0
0027FF9C  33 C0                           xor eax, eax
0027FF9E  45 33 C9                        xor r9d, r9d
0027FFA1  41 0F B6 F0                     movzx esi, r8b
0027FFA5  48 8B F9                        mov rdi, rcx
0027FFA8  0F 11 84 24 A0 00 00 00         movups xmmword ptr [rsp + 0xa0], xmm0
0027FFB0  0F 11 84 24 B0 00 00 00         movups xmmword ptr [rsp + 0xb0], xmm0
0027FFB8  0F 11 84 24 C0 00 00 00         movups xmmword ptr [rsp + 0xc0], xmm0
0027FFC0  0F 11 84 24 D0 00 00 00         movups xmmword ptr [rsp + 0xd0], xmm0
0027FFC8  49 89 43 A8                     mov qword ptr [r11 - 0x58], rax
0027FFCC  41 0F 11 43 88                  movups xmmword ptr [r11 - 0x78], xmm0
0027FFD1  41 0F 11 43 98                  movups xmmword ptr [r11 - 0x68], xmm0
0027FFD6  F6 C3 04                        test bl, 4
0027FFD9  0F 85 FB 0B 00 00               jne 0x140280bda
0027FFDF  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0027FFE8  4C 8B 80 B8 00 00 00            mov r8, qword ptr [rax + 0xb8]
0027FFEF  4C 89 44 24 60                  mov qword ptr [rsp + 0x60], r8
0027FFF4  4D 8D B8 00 04 00 00            lea r15, [r8 + 0x400]
0027FFFB  44 8B F3                        mov r14d, ebx
0027FFFE  4C 89 7C 24 38                  mov qword ptr [rsp + 0x38], r15
00280003  41 83 E6 08                     and r14d, 8
00280007  89 94 24 B8 00 00 00            mov dword ptr [rsp + 0xb8], edx
0028000E  48 8D AC 24 90 00 00 00         lea rbp, [rsp + 0x90]
00280016  44 89 74 24 34                  mov dword ptr [rsp + 0x34], r14d
0028001B  0F 95 C0                        setne al
0028001E  49 BD 00 00 00 00 80 F6 FF FF   movabs r13, 0xfffff68000000000
00280028  04 07                           add al, 7
0028002A  48 83 CD 01                     or rbp, 1
0028002E  88 84 24 90 00 00 00            mov byte ptr [rsp + 0x90], al
00280035  48 89 6C 24 48                  mov qword ptr [rsp + 0x48], rbp
0028003A  4D 8B E5                        mov r12, r13
0028003D  49 C1 E4 19                     shl r12, 0x19
00280041  48 C1 E1 19                     shl rcx, 0x19
00280045  49 2B CC                        sub rcx, r12
00280048  4C 89 64 24 50                  mov qword ptr [rsp + 0x50], r12
0028004D  48 C1 F9 10                     sar rcx, 0x10
00280051  48 89 4C 24 68                  mov qword ptr [rsp + 0x68], rcx
00280056  49 8B C5                        mov rax, r13
00280059  48 BA FF FF FF FF FF F6 FF FF   movabs rdx, 0xfffff6ffffffffff
00280063  48 3B C8                        cmp rcx, rax
00280066  72 0D                           jb 0x140280075
00280068  48 8B C2                        mov rax, rdx
0028006B  48 3B C8                        cmp rcx, rax
0028006E  77 05                           ja 0x140280075
00280070  41 8B C1                        mov eax, r9d
00280073  EB 05                           jmp 0x14028007a
00280075  B8 01 00 00 00                  mov eax, 1
0028007A  83 E3 01                        and ebx, 1
0028007D  89 84 24 68 01 00 00            mov dword ptr [rsp + 0x168], eax
00280084  89 9C 24 78 01 00 00            mov dword ptr [rsp + 0x178], ebx
0028008B  41 BA 02 00 00 00               mov r10d, 2
00280091  4C 8D 1D A8 CA BA 00            lea r11, [rip + 0xbacaa8]
00280098  49 B8 F8 FF FF FF 7F 00 00 00   movabs r8, 0x7ffffffff8
002800A2  85 DB                           test ebx, ebx
002800A4  0F 84 28 01 00 00               je 0x1402801d2
002800AA  BA 01 00 00 00                  mov edx, 1
002800AF  48 8B CF                        mov rcx, rdi
002800B2  E8 19 FD FF FF                  call 0x14027fdd0
002800B7  84 C0                           test al, al
002800B9  0F 85 08 03 00 00               jne 0x1402803c7
002800BF  40 0F B6 D6                     movzx edx, sil
002800C3  49 8B CF                        mov rcx, r15
002800C6  E8 A5 EB FF FF                  call 0x14027ec70
002800CB  45 33 C0                        xor r8d, r8d
002800CE  4C 8B CD                        mov r9, rbp
002800D1  48 8B D7                        mov rdx, rdi
002800D4  41 8D 48 02                     lea ecx, [r8 + 2]
002800D8  E8 A3 ED FF FF                  call 0x14027ee80
002800DD  48 63 F0                        movsxd rsi, eax
002800E0  85 C0                           test eax, eax
002800E2  0F 88 72 0B 00 00               js 0x140280c5a
002800E8  85 DB                           test ebx, ebx
002800EA  0F 85 61 0A 00 00               jne 0x140280b51
002800F0  41 8B 87 B8 00 00 00            mov eax, dword ptr [r15 + 0xb8]
002800F7  24 0F                           and al, 0xf
002800F9  3C 06                           cmp al, 6
002800FB  0F 83 DA 08 00 00               jae 0x1402809db
00280101  41 8B 87 B8 00 00 00            mov eax, dword ptr [r15 + 0xb8]
00280108  24 0F                           and al, 0xf
0028010A  3C 01                           cmp al, 1
0028010C  0F 85 4C 0A 00 00               jne 0x140280b5e
00280112  48 8D 05 27 87 BB 00            lea rax, [rip + 0xbb8727]
00280119  65 8B 3C 25 A4 01 00 00         mov edi, dword ptr gs:[0x1a4]
00280121  48 8B 00                        mov rax, qword ptr [rax]
00280124  D1 EF                           shr edi, 1
00280126  83 E7 03                        and edi, 3
00280129  8B DF                           mov ebx, edi
0028012B  48 C1 E3 06                     shl rbx, 6
0028012F  48 03 D8                        add rbx, rax
00280132  44 0F 20 C5                     mov rbp, cr8
00280136  B8 02 00 00 00                  mov eax, 2
0028013B  44 0F 22 C0                     mov cr8, rax
0028013F  83 3D DA 6B D4 00 00            cmp dword ptr [rip + 0xd46bda], 0
00280146  0F 85 12 07 00 00               jne 0x14028085e
0028014C  F6 05 B3 69 D4 00 21            test byte ptr [rip + 0xd469b3], 0x21
00280153  74 0E                           je 0x140280163
00280155  8B 05 FD DC C8 00               mov eax, dword ptr [rip + 0xc8dcfd]
0028015B  85 C0                           test eax, eax
0028015D  0F 84 00 05 00 00               je 0x140280663
00280163  0F 0D 0B                        prefetchw byte ptr [rbx]
00280166  8B 03                           mov eax, dword ptr [rbx]
00280168  0F BA F0 1F                     btr eax, 0x1f
0028016C  8D 48 01                        lea ecx, [rax + 1]
0028016F  F0 0F B1 0B                     lock cmpxchg dword ptr [rbx], ecx
00280173  0F 85 AD 07 00 00               jne 0x140280926
00280179  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
00280182  8B 9C 24 78 01 00 00            mov ebx, dword ptr [rsp + 0x178]
00280189  48 8B 6C 24 48                  mov rbp, qword ptr [rsp + 0x48]
0028018E  48 8B 88 38 88 00 00            mov rcx, qword ptr [rax + 0x8838]
00280195  48 85 C9                        test rcx, rcx
00280198  74 06                           je 0x1402801a0
0028019A  89 B9 44 01 00 00               mov dword ptr [rcx + 0x144], edi
002801A0  48 8B BC 24 60 01 00 00         mov rdi, qword ptr [rsp + 0x160]
002801A8  41 BA 02 00 00 00               mov r10d, 2
002801AE  85 F6                           test esi, esi
002801B0  0F 88 00 03 00 00               js 0x1402804b6
002801B6  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
002801BB  45 33 C9                        xor r9d, r9d
002801BE  8B 84 24 68 01 00 00            mov eax, dword ptr [rsp + 0x168]
002801C5  0F B6 B4 24 70 01 00 00         movzx esi, byte ptr [rsp + 0x170]
002801CD  E9 BF FE FF FF                  jmp 0x140280091
002801D2  85 C0                           test eax, eax
002801D4  0F 85 E3 02 00 00               jne 0x1402804bd
002801DA  48 8B CF                        mov rcx, rdi
002801DD  48 C1 E9 09                     shr rcx, 9
002801E1  49 23 C8                        and rcx, r8
002801E4  49 8B C5                        mov rax, r13
002801E7  48 03 C8                        add rcx, rax
002801EA  48 89 4C 24 70                  mov qword ptr [rsp + 0x70], rcx
002801EF  48 C1 E9 09                     shr rcx, 9
002801F3  49 23 C8                        and rcx, r8
002801F6  49 8B C5                        mov rax, r13
002801F9  48 03 C8                        add rcx, rax
002801FC  48 89 4C 24 78                  mov qword ptr [rsp + 0x78], rcx
00280201  48 C1 E9 09                     shr rcx, 9
00280205  49 23 C8                        and rcx, r8
00280208  49 8B C5                        mov rax, r13
0028020B  48 03 C8                        add rcx, rax
0028020E  48 89 8C 24 80 00 00 00         mov qword ptr [rsp + 0x80], rcx
00280216  48 C1 E9 09                     shr rcx, 9
0028021A  49 23 C8                        and rcx, r8
0028021D  49 8B C5                        mov rax, r13
00280220  48 03 C8                        add rcx, rax
00280223  48 BF 68 DF BE 7D FB F6 FF FF   movabs rdi, 0xfffff6fb7dbedf68
0028022D  48 89 8C 24 88 00 00 00         mov qword ptr [rsp + 0x88], rcx
00280235  4C 8B EF                        mov r13, rdi
00280238  65 4C 8B 04 25 20 00 00 00      mov r8, qword ptr gs:[0x20]
00280241  41 8B 87 B8 00 00 00            mov eax, dword ptr [r15 + 0xb8]
00280248  4C 89 6C 24 58                  mov qword ptr [rsp + 0x58], r13
0028024D  24 0F                           and al, 0xf
0028024F  0F 85 E4 05 00 00               jne 0x140280839
00280255  41 8B CA                        mov ecx, r10d
00280258  49 8D 97 B0 00 00 00            lea rdx, [r15 + 0xb0]
0028025F  8B C1                           mov eax, ecx
00280261  48 8D 88 C4 09 00 00            lea rcx, [rax + 0x9c4]
00280268  48 8D 0C 48                     lea rcx, [rax + rcx*2]
0028026C  49 8D 0C C8                     lea rcx, [r8 + rcx*8]
00280270  48 89 51 08                     mov qword ptr [rcx + 8], rdx
00280274  4C 89 09                        mov qword ptr [rcx], r9
00280277  90                              nop
00280278  F6 05 87 68 D4 00 21            test byte ptr [rip + 0xd46887], 0x21
0028027F  0F 85 EA 06 00 00               jne 0x14028096f
00280285  48 8B C1                        mov rax, rcx
00280288  48 87 02                        xchg qword ptr [rdx], rax
0028028B  48 85 C0                        test rax, rax
0028028E  0F 85 96 08 00 00               jne 0x140280b2a
00280294  4D 8B F2                        mov r14, r10
00280297  4A 8B 74 F4 70                  mov rsi, qword ptr [rsp + r14*8 + 0x70]
0028029C  4C 89 74 24 40                  mov qword ptr [rsp + 0x40], r14
002802A1  49 B8 00 D0 BE 7D FB F6 FF FF   movabs r8, 0xfffff6fb7dbed000
002802AB  48 8B 1E                        mov rbx, qword ptr [rsi]
002802AE  49 8B C0                        mov rax, r8
002802B1  48 3B F0                        cmp rsi, rax
002802B4  72 2B                           jb 0x1402802e1
002802B6  48 B8 F8 D7 BE 7D FB F6 FF FF   movabs rax, 0xfffff6fb7dbed7f8
002802C0  48 8B C0                        mov rax, rax
002802C3  48 3B F0                        cmp rsi, rax
002802C6  77 19                           ja 0x1402802e1
002802C8  F6 C3 01                        test bl, 1
002802CB  74 14                           je 0x1402802e1
002802CD  F6 C3 42                        test bl, 0x42
002802D0  0F 95 C1                        setne cl
002802D3  F6 C3 20                        test bl, 0x20
002802D6  0F 95 C0                        setne al
002802D9  84 C8                           test al, cl
002802DB  0F 84 6D 01 00 00               je 0x14028044e
002802E1  0F B6 C3                        movzx eax, bl
002802E4  24 81                           and al, 0x81
002802E6  3C 01                           cmp al, 1
002802E8  0F 85 A4 00 00 00               jne 0x140280392
002802EE  F6 C3 20                        test bl, 0x20
002802F1  0F 85 82 00 00 00               jne 0x140280379
002802F7  41 8B 87 B8 00 00 00            mov eax, dword ptr [r15 + 0xb8]
002802FE  48 8B FE                        mov rdi, rsi
00280301  48 C1 E7 19                     shl rdi, 0x19
00280305  41 8B E9                        mov ebp, r9d
00280308  49 2B FC                        sub rdi, r12
0028030B  48 C1 FF 10                     sar rdi, 0x10
0028030F  A8 0F                           test al, 0xf
00280311  74 1E                           je 0x140280331
00280313  49 8B C0                        mov rax, r8
00280316  48 3B F0                        cmp rsi, rax
00280319  72 16                           jb 0x140280331
0028031B  48 B8 FF DF BE 7D FB F6 FF FF   movabs rax, 0xfffff6fb7dbedfff
00280325  48 8B C0                        mov rax, rax
00280328  48 3B F0                        cmp rsi, rax
0028032B  0F 86 75 09 00 00               jbe 0x140280ca6
00280331  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
0028033B  48 8B C0                        mov rax, rax
0028033E  48 3B F8                        cmp rdi, rax
00280341  0F 83 86 09 00 00               jae 0x140280ccd
00280347  48 83 CB 20                     or rbx, 0x20
0028034B  48 8B CE                        mov rcx, rsi
0028034E  48 8B D3                        mov rdx, rbx
00280351  E8 BA 14 00 00                  call 0x140281810
00280356  45 33 C9                        xor r9d, r9d
00280359  49 B8 00 D0 BE 7D FB F6 FF FF   movabs r8, 0xfffff6fb7dbed000
00280363  45 8D 51 02                     lea r10d, [r9 + 2]
00280367  85 ED                           test ebp, ebp
00280369  0F 85 79 09 00 00               jne 0x140280ce8
0028036F  48 BF 68 DF BE 7D FB F6 FF FF   movabs rdi, 0xfffff6fb7dbedf68
00280379  49 3B F5                        cmp rsi, r13
0028037C  75 60                           jne 0x1402803de
0028037E  4D 85 F6                        test r14, r14
00280381  74 0F                           je 0x140280392
00280383  49 FF CE                        dec r14
00280386  45 33 C9                        xor r9d, r9d
00280389  45 8D 51 02                     lea r10d, [r9 + 2]
0028038D  E9 05 FF FF FF                  jmp 0x140280297
00280392  48 8B BC 24 60 01 00 00         mov rdi, qword ptr [rsp + 0x160]
0028039A  48 BA F8 FF FF FF 7F 00 00 00   movabs rdx, 0x7ffffffff8
002803A4  48 8B CF                        mov rcx, rdi
002803A7  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
002803B1  48 C1 E9 09                     shr rcx, 9
002803B5  48 23 CA                        and rcx, rdx
002803B8  48 8B C0                        mov rax, rax
002803BB  48 03 C8                        add rcx, rax
002803BE  4C 3B E9                        cmp r13, rcx
002803C1  0F 85 88 06 00 00               jne 0x140280a4f
002803C7  33 C0                           xor eax, eax
002803C9  48 81 C4 18 01 00 00            add rsp, 0x118
002803D0  41 5F                           pop r15
002803D2  41 5E                           pop r14
002803D4  41 5D                           pop r13
002803D6  41 5C                           pop r12
002803D8  5F                              pop rdi
002803D9  5E                              pop rsi
002803DA  5D                              pop rbp
002803DB  5B                              pop rbx
002803DC  C3                              ret
002803DD  CC                              int3
002803DE  48 8B C7                        mov rax, rdi
002803E1  48 3B F0                        cmp rsi, rax
002803E4  0F 85 06 01 00 00               jne 0x1402804f0
002803EA  65 4C 8B 04 25 20 00 00 00      mov r8, qword ptr gs:[0x20]
002803F3  41 8B 87 B8 00 00 00            mov eax, dword ptr [r15 + 0xb8]
002803FA  24 0F                           and al, 0xf
002803FC  0F 85 E9 03 00 00               jne 0x1402807eb
00280402  41 8B CA                        mov ecx, r10d
00280405  49 8D 97 B0 00 00 00            lea rdx, [r15 + 0xb0]
0028040C  8B C1                           mov eax, ecx
0028040E  48 8D 88 C4 09 00 00            lea rcx, [rax + 0x9c4]
00280415  48 8D 0C 48                     lea rcx, [rax + rcx*2]
00280419  49 8D 0C C8                     lea rcx, [r8 + rcx*8]
0028041D  48 89 51 08                     mov qword ptr [rcx + 8], rdx
00280421  4C 89 09                        mov qword ptr [rcx], r9
00280424  90                              nop
00280425  F6 05 DA 66 D4 00 21            test byte ptr [rip + 0xd466da], 0x21
0028042C  0F 85 25 05 00 00               jne 0x140280957
00280432  48 8B C1                        mov rax, rcx
00280435  48 87 02                        xchg qword ptr [rdx], rax
00280438  48 85 C0                        test rax, rax
0028043B  0F 84 D6 01 00 00               je 0x140280617
00280441  48 8B D0                        mov rdx, rax
00280444  E8 67 7A FD FF                  call 0x140257eb0
00280449  E9 C6 01 00 00                  jmp 0x140280614
0028044E  48 F7 05 2F 66 D4 00 00 00 60 00  test qword ptr [rip + 0xd4662f], 0x600000
00280459  0F 84 82 FE FF FF               je 0x1402802e1
0028045F  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00280468  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
0028046F  80 B9 60 01 00 00 01            cmp byte ptr [rcx + 0x160], 1
00280476  0F 84 65 FE FF FF               je 0x1402802e1
0028047C  48 8B 91 08 05 00 00            mov rdx, qword ptr [rcx + 0x508]
00280483  48 85 D2                        test rdx, rdx
00280486  0F 84 55 FE FF FF               je 0x1402802e1
0028048C  48 8B C6                        mov rax, rsi
0028048F  48 C1 E8 03                     shr rax, 3
00280493  25 FF 01 00 00                  and eax, 0x1ff
00280498  48 8B 04 C2                     mov rax, qword ptr [rdx + rax*8]
0028049C  A8 20                           test al, 0x20
0028049E  74 04                           je 0x1402804a4
002804A0  48 83 CB 20                     or rbx, 0x20
002804A4  48 8B CB                        mov rcx, rbx
002804A7  48 83 CB 42                     or rbx, 0x42
002804AB  A8 42                           test al, 0x42
002804AD  48 0F 44 D9                     cmove rbx, rcx
002804B1  E9 2B FE FF FF                  jmp 0x1402802e1
002804B6  8B C6                           mov eax, esi
002804B8  E9 0C FF FF FF                  jmp 0x1402803c9
002804BD  48 8B D1                        mov rdx, rcx
002804C0  45 33 C0                        xor r8d, r8d
002804C3  49 8B CF                        mov rcx, r15
002804C6  E8 75 5E FF FF                  call 0x140276340
002804CB  85 C0                           test eax, eax
002804CD  0F 85 44 03 00 00               jne 0x140280817
002804D3  45 33 C9                        xor r9d, r9d
002804D6  44 8D 50 02                     lea r10d, [rax + 2]
002804DA  49 B8 F8 FF FF FF 7F 00 00 00   movabs r8, 0x7ffffffff8
002804E4  4C 8D 1D 55 C6 BA 00            lea r11, [rip + 0xbac655]
002804EB  E9 EA FC FF FF                  jmp 0x1402801da
002804F0  41 8B 87 B8 00 00 00            mov eax, dword ptr [r15 + 0xb8]
002804F7  A8 0F                           test al, 0xf
002804F9  75 41                           jne 0x14028053c
002804FB  49 8B C0                        mov rax, r8
002804FE  48 3B F0                        cmp rsi, rax
00280501  72 39                           jb 0x14028053c
00280503  48 B8 FF DF BE 7D FB F6 FF FF   movabs rax, 0xfffff6fb7dbedfff
0028050D  48 8B C0                        mov rax, rax
00280510  48 3B F0                        cmp rsi, rax
00280513  77 27                           ja 0x14028053c
00280515  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0028051E  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
00280525  48 8B 81 10 04 00 00            mov rax, qword ptr [rcx + 0x410]
0028052C  48 8B 88 68 05 00 00            mov rcx, qword ptr [rax + 0x568]
00280533  48 85 C9                        test rcx, rcx
00280536  0F 85 86 06 00 00               jne 0x140280bc2
0028053C  41 8B 87 B8 00 00 00            mov eax, dword ptr [r15 + 0xb8]
00280543  A8 0F                           test al, 0xf
00280545  74 1E                           je 0x140280565
00280547  49 8B C0                        mov rax, r8
0028054A  48 3B F0                        cmp rsi, rax
0028054D  72 16                           jb 0x140280565
0028054F  48 B8 FF DF BE 7D FB F6 FF FF   movabs rax, 0xfffff6fb7dbedfff
00280559  48 8B C0                        mov rax, rax
0028055C  48 3B F0                        cmp rsi, rax
0028055F  0F 86 25 05 00 00               jbe 0x140280a8a
00280565  48 8B 1E                        mov rbx, qword ptr [rsi]
00280568  41 8B E9                        mov ebp, r9d
0028056B  49 8B C0                        mov rax, r8
0028056E  48 3B F0                        cmp rsi, rax
00280571  72 2B                           jb 0x14028059e
00280573  48 B8 F8 D7 BE 7D FB F6 FF FF   movabs rax, 0xfffff6fb7dbed7f8
0028057D  48 8B C0                        mov rax, rax
00280580  48 3B F0                        cmp rsi, rax
00280583  77 19                           ja 0x14028059e
00280585  F6 C3 01                        test bl, 1
00280588  74 14                           je 0x14028059e
0028058A  F6 C3 42                        test bl, 0x42
0028058D  0F 95 C1                        setne cl
00280590  F6 C3 20                        test bl, 0x20
00280593  0F 95 C0                        setne al
00280596  84 C8                           test al, cl
00280598  0F 84 20 03 00 00               je 0x1402808be
0028059E  49 BC 00 00 00 00 80 F6 FF FF   movabs r12, 0xfffff68000000000
002805A8  49 BE FF FF FF FF FF FF FF DF   movabs r14, 0xdfffffffffffffff
002805B2  49 BF 20 00 00 00 00 00 00 10   movabs r15, 0x1000000000000020
002805BC  F6 C3 01                        test bl, 1
002805BF  74 35                           je 0x1402805f6
002805C1  48 8B C3                        mov rax, rbx
002805C4  48 C1 E8 3C                     shr rax, 0x3c
002805C8  A8 01                           test al, 1
002805CA  0F 85 C0 03 00 00               jne 0x140280990
002805D0  48 8B CB                        mov rcx, rbx
002805D3  49 23 CE                        and rcx, r14
002805D6  49 0B CF                        or rcx, r15
002805D9  48 F7 05 A4 64 D4 00 00 00 00 02  test qword ptr [rip + 0xd464a4], 0x2000000
002805E4  74 03                           je 0x1402805e9
002805E6  0F AE E8                        lfence
002805E9  48 8B C3                        mov rax, rbx
002805EC  F0 48 0F B1 0E                  lock cmpxchg qword ptr [rsi], rcx
002805F1  48 8B D8                        mov rbx, rax
002805F4  75 C6                           jne 0x1402805bc
002805F6  4C 8B 6C 24 58                  mov r13, qword ptr [rsp + 0x58]
002805FB  4C 8B 64 24 50                  mov r12, qword ptr [rsp + 0x50]
00280600  4C 8B 7C 24 38                  mov r15, qword ptr [rsp + 0x38]
00280605  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
0028060A  48 BF 68 DF BE 7D FB F6 FF FF   movabs rdi, 0xfffff6fb7dbedf68
00280614  45 33 C9                        xor r9d, r9d
00280617  48 8B C7                        mov rax, rdi
0028061A  4C 3B E8                        cmp r13, rax
0028061D  0F 84 D1 00 00 00               je 0x1402806f4
00280623  41 8B 87 B8 00 00 00            mov eax, dword ptr [r15 + 0xb8]
0028062A  49 B8 00 D0 BE 7D FB F6 FF FF   movabs r8, 0xfffff6fb7dbed000
00280634  A8 0F                           test al, 0xf
00280636  74 3C                           je 0x140280674
00280638  41 8B 87 B8 00 00 00            mov eax, dword ptr [r15 + 0xb8]
0028063F  A8 0F                           test al, 0xf
00280641  0F 85 36 01 00 00               jne 0x14028077d
00280647  48 B8 FF FF FF FF FF FF FF CF   movabs rax, 0xcfffffffffffffff
00280651  F0 49 21 45 00                  lock and qword ptr [r13], rax
00280656  4C 8B EE                        mov r13, rsi
00280659  48 89 74 24 58                  mov qword ptr [rsp + 0x58], rsi
0028065E  E9 1B FD FF FF                  jmp 0x14028037e
00280663  40 0F B6 D5                     movzx edx, bpl
00280667  48 8B CB                        mov rcx, rbx
0028066A  E8 B1 C6 FF FF                  call 0x14027cd20
0028066F  E9 05 FB FF FF                  jmp 0x140280179
00280674  49 8B C0                        mov rax, r8
00280677  4C 3B E8                        cmp r13, rax
0028067A  72 BC                           jb 0x140280638
0028067C  48 B8 FF DF BE 7D FB F6 FF FF   movabs rax, 0xfffff6fb7dbedfff
00280686  48 8B C0                        mov rax, rax
00280689  4C 3B E8                        cmp r13, rax
0028068C  77 AA                           ja 0x140280638
0028068E  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00280697  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
0028069E  48 8B 81 10 04 00 00            mov rax, qword ptr [rcx + 0x410]
002806A5  48 8B 88 68 05 00 00            mov rcx, qword ptr [rax + 0x568]
002806AC  48 85 C9                        test rcx, rcx
002806AF  74 87                           je 0x140280638
002806B1  41 C1 ED 03                     shr r13d, 3
002806B5  41 81 E5 FF 01 00 00            and r13d, 0x1ff
002806BC  42 8B 04 A9                     mov eax, dword ptr [rcx + r13*4]
002806C0  4A 8D 0C A9                     lea rcx, [rcx + r13*4]
002806C4  A9 FF FF FF 3F                  test eax, 0x3fffffff
002806C9  0F 85 CB 01 00 00               jne 0x14028089a
002806CF  85 C0                           test eax, eax
002806D1  0F 89 93 04 00 00               jns 0x140280b6a
002806D7  F6 05 28 64 D4 00 01            test byte ptr [rip + 0xd46428], 1
002806DE  0F 85 07 05 00 00               jne 0x140280beb
002806E4  44 89 09                        mov dword ptr [rcx], r9d
002806E7  4C 8B EE                        mov r13, rsi
002806EA  48 89 74 24 58                  mov qword ptr [rsp + 0x58], rsi
002806EF  E9 8A FC FF FF                  jmp 0x14028037e
002806F4  65 48 8B 14 25 20 00 00 00      mov rdx, qword ptr gs:[0x20]
002806FD  41 8B 87 B8 00 00 00            mov eax, dword ptr [r15 + 0xb8]
00280704  24 0F                           and al, 0xf
00280706  0F 85 33 02 00 00               jne 0x14028093f
0028070C  B9 30 00 00 00                  mov ecx, 0x30
00280711  48 8D 9A 40 9C 00 00            lea rbx, [rdx + 0x9c40]
00280718  48 03 D9                        add rbx, rcx
0028071B  F6 05 E4 63 D4 00 01            test byte ptr [rip + 0xd463e4], 1
00280722  0F 85 47 01 00 00               jne 0x14028086f
00280728  0F 0D 0B                        prefetchw byte ptr [rbx]
0028072B  48 8B 03                        mov rax, qword ptr [rbx]
0028072E  48 85 C0                        test rax, rax
00280731  75 1D                           jne 0x140280750
00280733  48 8B 4B 08                     mov rcx, qword ptr [rbx + 8]
00280737  48 8B C3                        mov rax, rbx
0028073A  F0 4C 0F B1 09                  lock cmpxchg qword ptr [rcx], r9
0028073F  0F 84 11 FF FF FF               je 0x140280656
00280745  48 8B CB                        mov rcx, rbx
00280748  E8 53 73 F9 FF                  call 0x140217aa0
0028074D  45 33 C9                        xor r9d, r9d
00280750  48 8D 48 08                     lea rcx, [rax + 8]
00280754  4C 89 0B                        mov qword ptr [rbx], r9
00280757  48 8B 53 08                     mov rdx, qword ptr [rbx + 8]
0028075B  48 8B C2                        mov rax, rdx
0028075E  48 87 01                        xchg qword ptr [rcx], rax
00280761  32 C2                           xor al, dl
00280763  A8 04                           test al, 4
00280765  0F 84 EB FE FF FF               je 0x140280656
0028076B  E8 B0 74 F9 FF                  call 0x140217c20
00280770  4C 8B EE                        mov r13, rsi
00280773  48 89 74 24 58                  mov qword ptr [rsp + 0x58], rsi
00280778  E9 01 FC FF FF                  jmp 0x14028037e
0028077D  49 8B C0                        mov rax, r8
00280780  4C 3B E8                        cmp r13, rax
00280783  0F 82 BE FE FF FF               jb 0x140280647
00280789  48 B8 FF DF BE 7D FB F6 FF FF   movabs rax, 0xfffff6fb7dbedfff
00280793  48 8B C0                        mov rax, rax
00280796  4C 3B E8                        cmp r13, rax
00280799  0F 87 A8 FE FF FF               ja 0x140280647
0028079F  49 8B C0                        mov rax, r8
002807A2  4C 2B E8                        sub r13, rax
002807A5  41 8B 87 B8 00 00 00            mov eax, dword ptr [r15 + 0xb8]
002807AC  49 C1 FD 03                     sar r13, 3
002807B0  42 8D 14 6D 00 00 00 00         lea edx, [r13*2]
002807B8  8B C2                           mov eax, edx
002807BA  8B CA                           mov ecx, edx
002807BC  48 C1 E8 05                     shr rax, 5
002807C0  48 8D 15 79 C3 BA 00            lea rdx, [rip + 0xbac379]
002807C7  83 E1 1F                        and ecx, 0x1f
002807CA  48 8D 14 82                     lea rdx, [rdx + rax*4]
002807CE  B8 03 00 00 00                  mov eax, 3
002807D3  D3 E0                           shl eax, cl
002807D5  F7 D0                           not eax
002807D7  F0 21 82 6C 26 00 00            lock and dword ptr [rdx + 0x266c], eax
002807DE  4C 8B EE                        mov r13, rsi
002807E1  48 89 74 24 58                  mov qword ptr [rsp + 0x58], rsi
002807E6  E9 93 FB FF FF                  jmp 0x14028037e
002807EB  3C 07                           cmp al, 7
002807ED  0F 84 11 02 00 00               je 0x140280a04
002807F3  3C 05                           cmp al, 5
002807F5  B9 03 00 00 00                  mov ecx, 3
002807FA  41 0F 44 C9                     cmove ecx, r9d
002807FE  8B C1                           mov eax, ecx
00280800  48 8D 15 39 C3 BA 00            lea rdx, [rip + 0xbac339]
00280807  48 8D 14 C2                     lea rdx, [rdx + rax*8]
0028080B  48 81 C2 80 32 00 00            add rdx, 0x3280
00280812  E9 F5 FB FF FF                  jmp 0x14028040c
00280817  83 F8 01                        cmp eax, 1
0028081A  0F 84 A7 FB FF FF               je 0x1402803c7
00280820  48 BA F8 FF FF FF 7F 00 00 00   movabs rdx, 0x7ffffffff8
0028082A  48 C1 EF 09                     shr rdi, 9
0028082E  48 23 FA                        and rdi, rdx
00280831  49 8B C5                        mov rax, r13
00280834  48 03 F8                        add rdi, rax
00280837  EB F1                           jmp 0x14028082a
00280839  3C 07                           cmp al, 7
0028083B  0F 84 CD 01 00 00               je 0x140280a0e
00280841  3C 05                           cmp al, 5
00280843  B9 03 00 00 00                  mov ecx, 3
00280848  41 0F 44 C9                     cmove ecx, r9d
0028084C  8B D1                           mov edx, ecx
0028084E  48 81 C2 50 06 00 00            add rdx, 0x650
00280855  49 8D 14 D3                     lea rdx, [r11 + rdx*8]
00280859  E9 01 FA FF FF                  jmp 0x14028025f
0028085E  0F B6 D0                        movzx edx, al
00280861  40 0F B6 CD                     movzx ecx, bpl
00280865  E8 92 4E 27 00                  call 0x1404f56fc
0028086A  E9 DD F8 FF FF                  jmp 0x14028014c
0028086F  8B 05 E3 D5 C8 00               mov eax, dword ptr [rip + 0xc8d5e3]
00280875  85 C0                           test eax, eax
00280877  0F 85 AB FE FF FF               jne 0x140280728
0028087D  48 8B 94 24 58 01 00 00         mov rdx, qword ptr [rsp + 0x158]
00280885  48 8B CB                        mov rcx, rbx
00280888  E8 63 71 F9 FF                  call 0x1402179f0
0028088D  4C 8B EE                        mov r13, rsi
00280890  48 89 74 24 58                  mov qword ptr [rsp + 0x58], rsi
00280895  E9 E4 FA FF FF                  jmp 0x14028037e
0028089A  F6 05 65 62 D4 00 01            test byte ptr [rip + 0xd46265], 1
002808A1  0F 85 8B 03 00 00               jne 0x140280c32
002808A7  F0 81 21 FF FF FF BF            lock and dword ptr [rcx], 0xbfffffff
002808AE  F0 FF 09                        lock dec dword ptr [rcx]
002808B1  4C 8B EE                        mov r13, rsi
002808B4  48 89 74 24 58                  mov qword ptr [rsp + 0x58], rsi
002808B9  E9 C0 FA FF FF                  jmp 0x14028037e
002808BE  48 F7 05 BF 61 D4 00 00 00 60 00  test qword ptr [rip + 0xd461bf], 0x600000
002808C9  0F 84 CF FC FF FF               je 0x14028059e
002808CF  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
002808D8  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
002808DF  80 B9 60 01 00 00 01            cmp byte ptr [rcx + 0x160], 1
002808E6  0F 84 B2 FC FF FF               je 0x14028059e
002808EC  48 8B 91 08 05 00 00            mov rdx, qword ptr [rcx + 0x508]
002808F3  48 85 D2                        test rdx, rdx
002808F6  0F 84 A2 FC FF FF               je 0x14028059e
002808FC  48 8B C6                        mov rax, rsi
002808FF  48 C1 E8 03                     shr rax, 3
00280903  25 FF 01 00 00                  and eax, 0x1ff
00280908  48 8B 04 C2                     mov rax, qword ptr [rdx + rax*8]
0028090C  A8 20                           test al, 0x20
0028090E  74 04                           je 0x140280914
00280910  48 83 CB 20                     or rbx, 0x20
00280914  48 8B CB                        mov rcx, rbx
00280917  48 83 CB 42                     or rbx, 0x42
0028091B  A8 42                           test al, 0x42
0028091D  48 0F 44 D9                     cmove rbx, rcx
00280921  E9 78 FC FF FF                  jmp 0x14028059e
00280926  85 C0                           test eax, eax
00280928  0F 89 3E F8 FF FF               jns 0x14028016c
0028092E  40 0F B6 D5                     movzx edx, bpl
00280932  48 8B CB                        mov rcx, rbx
00280935  E8 46 1A 0E 00                  call 0x140362380
0028093A  E9 3A F8 FF FF                  jmp 0x140280179
0028093F  3C 07                           cmp al, 7
00280941  0F 84 D9 01 00 00               je 0x140280b20
00280947  3C 05                           cmp al, 5
00280949  B9 48 00 00 00                  mov ecx, 0x48
0028094E  49 0F 44 C9                     cmove rcx, r9
00280952  E9 BA FD FF FF                  jmp 0x140280711
00280957  8B 05 FB D4 C8 00               mov eax, dword ptr [rip + 0xc8d4fb]
0028095D  85 C0                           test eax, eax
0028095F  0F 85 CD FA FF FF               jne 0x140280432
00280965  E8 E6 4E FF FF                  call 0x140275850
0028096A  E9 A5 FC FF FF                  jmp 0x140280614
0028096F  8B 05 E3 D4 C8 00               mov eax, dword ptr [rip + 0xc8d4e3]
00280975  85 C0                           test eax, eax
00280977  0F 85 08 F9 FF FF               jne 0x140280285
0028097D  E8 CE 4E FF FF                  call 0x140275850
00280982  41 BA 02 00 00 00               mov r10d, 2
00280988  45 33 C9                        xor r9d, r9d
0028098B  E9 04 F9 FF FF                  jmp 0x140280294
00280990  A8 02                           test al, 2
00280992  0F 85 98 00 00 00               jne 0x140280a30
00280998  48 8B FB                        mov rdi, rbx
0028099B  48 B8 00 00 00 00 00 00 00 20   movabs rax, 0x2000000000000000
002809A5  48 0B F8                        or rdi, rax
002809A8  48 F7 05 D5 60 D4 00 00 00 00 02  test qword ptr [rip + 0xd460d5], 0x2000000
002809B3  74 03                           je 0x1402809b8
002809B5  0F AE E8                        lfence
002809B8  48 0F BA 25 C7 60 D4 00 24      bt qword ptr [rip + 0xd460c7], 0x24
002809C1  0F 82 BE 01 00 00               jb 0x140280b85
002809C7  48 8B C3                        mov rax, rbx
002809CA  F0 48 0F B1 3E                  lock cmpxchg qword ptr [rsi], rdi
002809CF  48 8B D8                        mov rbx, rax
002809D2  48 0F 44 DF                     cmove rbx, rdi
002809D6  E9 E1 FB FF FF                  jmp 0x1402805bc
002809DB  44 0F 20 C1                     mov rcx, cr8
002809DF  41 BA 02 00 00 00               mov r10d, 2
002809E5  45 0F 22 C2                     mov cr8, r10
002809E9  83 3D 30 63 D4 00 00            cmp dword ptr [rip + 0xd46330], 0
002809F0  0F 84 B8 F7 FF FF               je 0x1402801ae
002809F6  41 0F B6 D2                     movzx edx, r10b
002809FA  E8 FD 4C 27 00                  call 0x1404f56fc
002809FF  E9 A4 F7 FF FF                  jmp 0x1402801a8
00280A04  B9 01 00 00 00                  mov ecx, 1
00280A09  E9 F0 FD FF FF                  jmp 0x1402807fe
00280A0E  B9 01 00 00 00                  mov ecx, 1
00280A13  8B D1                           mov edx, ecx
00280A15  48 81 C2 50 06 00 00            add rdx, 0x650
00280A1C  49 8D 14 D3                     lea rdx, [r11 + rdx*8]
00280A20  E9 3A F8 FF FF                  jmp 0x14028025f
00280A25  66 66 66 0F 1F 84 00 00 00 00 00  nop word ptr [rax + rax]
00280A30  FF C5                           inc ebp
00280A32  85 2D 74 48 D4 00               test dword ptr [rip + 0xd44874], ebp
00280A38  0F 84 BB 00 00 00               je 0x140280af9
00280A3E  F3 90                           pause
00280A40  48 8B 1E                        mov rbx, qword ptr [rsi]
00280A43  48 0F BA E3 3C                  bt rbx, 0x3c
00280A48  72 E6                           jb 0x140280a30
00280A4A  E9 6D FB FF FF                  jmp 0x1402805bc
00280A4F  49 8B D5                        mov rdx, r13
00280A52  49 8B CF                        mov rcx, r15
00280A55  E8 66 64 F9 FF                  call 0x140216ec0
00280A5A  0F B6 94 24 70 01 00 00         movzx edx, byte ptr [rsp + 0x170]
00280A62  49 8B CF                        mov rcx, r15
00280A65  E8 26 CC FF FF                  call 0x14027d690
00280A6A  8B 9C 24 78 01 00 00            mov ebx, dword ptr [rsp + 0x178]
00280A71  48 8B 6C 24 48                  mov rbp, qword ptr [rsp + 0x48]
00280A76  44 8B 74 24 34                  mov r14d, dword ptr [rsp + 0x34]
00280A7B  49 BD 00 00 00 00 80 F6 FF FF   movabs r13, 0xfffff68000000000
00280A85  E9 41 F6 FF FF                  jmp 0x1402800cb
00280A8A  45 8B E1                        mov r12d, r9d
00280A8D  49 8B C0                        mov rax, r8
00280A90  48 8B CE                        mov rcx, rsi
00280A93  BD 01 00 00 00                  mov ebp, 1
00280A98  48 2B C8                        sub rcx, rax
00280A9B  41 8B 87 B8 00 00 00            mov eax, dword ptr [r15 + 0xb8]
00280AA2  48 C1 F9 03                     sar rcx, 3
00280AA6  45 8B FA                        mov r15d, r10d
00280AA9  03 C9                           add ecx, ecx
00280AAB  8B F9                           mov edi, ecx
00280AAD  8B D9                           mov ebx, ecx
00280AAF  48 C1 EF 05                     shr rdi, 5
00280AB3  48 8D 0D 86 C0 BA 00            lea rcx, [rip + 0xbac086]
00280ABA  48 8D 89 6C 26 00 00            lea rcx, [rcx + 0x266c]
00280AC1  83 E3 1F                        and ebx, 0x1f
00280AC4  8B 14 B9                        mov edx, dword ptr [rcx + rdi*4]
00280AC7  48 8D 3C B9                     lea rdi, [rcx + rdi*4]
00280ACB  8B CB                           mov ecx, ebx
00280ACD  D3 E5                           shl ebp, cl
00280ACF  41 D3 E7                        shl r15d, cl
00280AD2  45 8B F7                        mov r14d, r15d
00280AD5  41 F7 D6                        not r14d
00280AD8  8B CB                           mov ecx, ebx
00280ADA  8B C2                           mov eax, edx
00280ADC  D3 E8                           shr eax, cl
00280ADE  A8 01                           test al, 1
00280AE0  75 55                           jne 0x140280b37
00280AE2  8B CA                           mov ecx, edx
00280AE4  8B C2                           mov eax, edx
00280AE6  0B CD                           or ecx, ebp
00280AE8  41 23 CE                        and ecx, r14d
00280AEB  F0 0F B1 0F                     lock cmpxchg dword ptr [rdi], ecx
00280AEF  8B D0                           mov edx, eax
00280AF1  0F 84 04 FB FF FF               je 0x1402805fb
00280AF7  EB DF                           jmp 0x140280ad8
00280AF9  8B 05 B9 5F D4 00               mov eax, dword ptr [rip + 0xd45fb9]
00280AFF  A8 40                           test al, 0x40
00280B01  0F 84 37 FF FF FF               je 0x140280a3e
00280B07  E8 84 E9 08 00                  call 0x14030f490
00280B0C  84 C0                           test al, al
00280B0E  0F 84 2A FF FF FF               je 0x140280a3e
00280B14  8B CD                           mov ecx, ebp
00280B16  E8 45 E9 08 00                  call 0x14030f460
00280B1B  E9 20 FF FF FF                  jmp 0x140280a40
00280B20  B9 18 00 00 00                  mov ecx, 0x18
00280B25  E9 E7 FB FF FF                  jmp 0x140280711
00280B2A  48 8B D0                        mov rdx, rax
00280B2D  E8 7E 73 FD FF                  call 0x140257eb0
00280B32  E9 4B FE FF FF                  jmp 0x140280982
00280B37  A8 02                           test al, 2
00280B39  0F 85 D4 00 00 00               jne 0x140280c13
00280B3F  8B CA                           mov ecx, edx
00280B41  8B C2                           mov eax, edx
00280B43  41 0B CF                        or ecx, r15d
00280B46  F0 0F B1 0F                     lock cmpxchg dword ptr [rdi], ecx
00280B4A  8B D0                           mov edx, eax
00280B4C  0F 44 D1                        cmove edx, ecx
00280B4F  EB 87                           jmp 0x140280ad8
00280B51  49 8B CF                        mov rcx, r15
00280B54  E8 47 2D 0A 00                  call 0x1403238a0
00280B59  E9 4A F6 FF FF                  jmp 0x1402801a8
00280B5E  49 8D 87 C0 00 00 00            lea rax, [r15 + 0xc0]
00280B65  E9 AF F5 FF FF                  jmp 0x140280119
00280B6A  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
00280B6F  48 8B D1                        mov rdx, rcx
00280B72  45 33 C9                        xor r9d, r9d
00280B75  41 B8 00 01 00 00               mov r8d, 0x100
00280B7B  41 8D 49 10                     lea ecx, [r9 + 0x10]
00280B7F  E8 DC CA 27 00                  call 0x1404fd660
00280B84  CC                              int3
00280B85  40 0F B6 C7                     movzx eax, dil
00280B89  24 21                           and al, 0x21
00280B8B  3C 01                           cmp al, 1
00280B8D  0F 85 34 FE FF FF               jne 0x1402809c7
00280B93  49 8B C4                        mov rax, r12
00280B96  48 B9 00 00 00 00 40 00 00 00   movabs rcx, 0x4000000000
00280BA0  48 03 C1                        add rax, rcx
00280BA3  48 3B F0                        cmp rsi, rax
00280BA6  0F 82 1B FE FF FF               jb 0x1402809c7
00280BAC  41 B8 80 00 00 00               mov r8d, 0x80
00280BB2  48 8B D7                        mov rdx, rdi
00280BB5  48 8B CE                        mov rcx, rsi
00280BB8  E8 C3 21 01 00                  call 0x140292d80
00280BBD  E9 05 FE FF FF                  jmp 0x1402809c7
00280BC2  8B C6                           mov eax, esi
00280BC4  C1 E8 03                        shr eax, 3
00280BC7  25 FF 01 00 00                  and eax, 0x1ff
00280BCC  48 8D 0C 81                     lea rcx, [rcx + rax*4]
00280BD0  E8 AB 82 FC FF                  call 0x140248e80
00280BD5  E9 3A FA FF FF                  jmp 0x140280614
00280BDA  4C 89 4C 24 60                  mov qword ptr [rsp + 0x60], r9
00280BDF  4C 8D 3D DA 74 BB 00            lea r15, [rip + 0xbb74da]
00280BE6  E9 10 F4 FF FF                  jmp 0x14027fffb
00280BEB  8B 05 67 D2 C8 00               mov eax, dword ptr [rip + 0xc8d267]
00280BF1  85 C0                           test eax, eax
00280BF3  0F 85 EB FA FF FF               jne 0x1402806e4
00280BF9  48 8B 94 24 58 01 00 00         mov rdx, qword ptr [rsp + 0x158]
00280C01  E8 3E 03 04 00                  call 0x1402c0f44
00280C06  4C 8B EE                        mov r13, rsi
00280C09  48 89 74 24 58                  mov qword ptr [rsp + 0x58], rsi
00280C0E  E9 6B F7 FF FF                  jmp 0x14028037e
00280C13  41 FF C4                        inc r12d
00280C16  44 85 25 8F 46 D4 00            test dword ptr [rip + 0xd4468f], r12d
00280C1D  74 67                           je 0x140280c86
00280C1F  F3 90                           pause
00280C21  8B 17                           mov edx, dword ptr [rdi]
00280C23  8B CB                           mov ecx, ebx
00280C25  8B C2                           mov eax, edx
00280C27  D3 E8                           shr eax, cl
00280C29  A8 01                           test al, 1
00280C2B  75 E6                           jne 0x140280c13
00280C2D  E9 A6 FE FF FF                  jmp 0x140280ad8
00280C32  8B 05 20 D2 C8 00               mov eax, dword ptr [rip + 0xc8d220]
00280C38  85 C0                           test eax, eax
00280C3A  0F 85 67 FC FF FF               jne 0x1402808a7
00280C40  48 8B 94 24 58 01 00 00         mov rdx, qword ptr [rsp + 0x158]
00280C48  E8 FB 02 07 00                  call 0x1402f0f48
00280C4D  4C 8B EE                        mov r13, rsi
00280C50  48 89 74 24 58                  mov qword ptr [rsp + 0x58], rsi
00280C55  E9 24 F7 FF FF                  jmp 0x14028037e
00280C5A  45 85 F6                        test r14d, r14d
00280C5D  0F 85 85 F4 FF FF               jne 0x1402800e8
00280C63  41 8D 4E 01                     lea ecx, [r14 + 1]
00280C67  E8 B0 07 26 00                  call 0x1404e141c
00280C6C  4C 8B 4C 24 60                  mov r9, qword ptr [rsp + 0x60]
00280C71  41 8D 56 01                     lea edx, [r14 + 1]
00280C75  4C 8B C6                        mov r8, rsi
00280C78  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
00280C7D  8D 4A 79                        lea ecx, [rdx + 0x79]
00280C80  E8 DB C9 27 00                  call 0x1404fd660
00280C85  CC                              int3
00280C86  8B 05 2C 5E D4 00               mov eax, dword ptr [rip + 0xd45e2c]
00280C8C  A8 40                           test al, 0x40
00280C8E  74 8F                           je 0x140280c1f
00280C90  E8 FB E7 08 00                  call 0x14030f490
00280C95  84 C0                           test al, al
00280C97  74 86                           je 0x140280c1f
00280C99  41 8B CC                        mov ecx, r12d
00280C9C  E8 BF E7 08 00                  call 0x14030f460
00280CA1  E9 7B FF FF FF                  jmp 0x140280c21
00280CA6  48 8D 0D 13 68 BB 00            lea rcx, [rip + 0xbb6813]
00280CAD  BD 01 00 00 00                  mov ebp, 1
00280CB2  E8 C9 81 FC FF                  call 0x140248e80
00280CB7  45 33 C9                        xor r9d, r9d
00280CBA  49 B8 00 D0 BE 7D FB F6 FF FF   movabs r8, 0xfffff6fb7dbed000
00280CC4  44 8D 55 01                     lea r10d, [rbp + 1]
00280CC8  E9 64 F6 FF FF                  jmp 0x140280331
00280CCD  48 B8 FF FF FF FF FF F6 FF FF   movabs rax, 0xfffff6ffffffffff
00280CD7  48 8B C0                        mov rax, rax
00280CDA  48 3B F8                        cmp rdi, rax
00280CDD  0F 87 64 F6 FF FF               ja 0x140280347
00280CE3  E9 4E 94 45 00                  jmp 0x1406da136
00280CE8  48 8D 0D D1 67 BB 00            lea rcx, [rip + 0xbb67d1]
00280CEF  E8 EC 8A FC FF                  call 0x1402497e0
00280CF4  45 33 C9                        xor r9d, r9d
00280CF7  49 B8 00 D0 BE 7D FB F6 FF FF   movabs r8, 0xfffff6fb7dbed000
00280D01  45 8D 51 02                     lea r10d, [r9 + 2]
00280D05  E9 65 F6 FF FF                  jmp 0x14028036f
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiMakeSystemAddressValid(__int64 a1, int a2, unsigned __int8 a3, int a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned int v_stack_m124;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m98;
    unsigned int v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB8;
    unsigned int v_stack_mC7;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned int v_stack_p10;
    unsigned __int64 v_stack_p158;
    unsigned __int8 v_stack_p170;
    unsigned int v_stack_p178;
    unsigned __int8 v_stack_p18;
    unsigned int v_stack_p20;
    unsigned int v_stack_p34;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p8;

    *(unsigned __int8 *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (280);
    v_stack_mC8 = v_xmm0;
    result = 0;
    a4 = 0;
    v_stack_mB8 = v_xmm0;
    v_stack_mA8 = v_xmm0;
    v_stack_m98 = v_xmm0;
    v_stack_m88 = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 88) = 0;
    *(unsigned __int64 *)(v_rsp - 120) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 104) = v_xmm0;
    if ((((unsigned __int8)((unsigned int)(a4))) & (4)) != 0) goto loc_00280BDA;
    v_stack_mF8 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184);
loc_0027FFFB:
    v_stack_m120 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1024;
    v_r14 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a4)))) & (8));
    v_stack_mA0 = a2;
    v_stack_m124 = (unsigned int)(v_r14);
    result = (condition_is_not_equal) ? 1 : 0;
    result = (unsigned __int8)((result) + (7));
    v_rbp = (v_stack_mC8) | (1);
    v_stack_mC8 = (unsigned __int8)(result);
    v_stack_m110 = v_rbp;
    v_r12 = (v_r13) << (25);
    a1 = (a1) << (25);
    a1 = (a1) - (v_r12);
    v_stack_m108 = v_r12;
    a1 = (a1) >> (16);
    v_stack_mF0 = a1;
    if (a1 < v_r13) goto loc_00280075;
    if (a1 > a2) goto loc_00280075;
    goto loc_0028007A;
loc_00280075:
loc_0028007A:
    v_rbx = (unsigned int)(((unsigned int)(a4)) & (1));
    v_stack_p10 = 1;
    v_stack_p20 = (unsigned int)(v_rbx);
loc_00280091:
    if ((unsigned int)(v_rbx) == 0) goto loc_002801D2;
    result = MmIsAddressValidEx(a1, 1, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), a4);
    if ((unsigned __int8)(result) != 0) goto loc_002803C7;
    result = MiUnlockWorkingSetExclusive(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1024, a3, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), a4);
loc_002800CB:
    a3 = 0;
    result = MmAccessFault(a3 + 2, a1, a3, v_rbp);
    if (sign_flag) goto loc_00280C5A;
loc_002800E8:
    if ((unsigned int)(v_rbx) != 0) goto loc_00280B51;
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1024 + 184))) & (15));
    if (((unsigned __int8)(result)) >= 6) goto loc_002809DB;
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1024 + 184))) & (15));
    if (((unsigned __int8)(result)) != 1) goto loc_00280B5E;
loc_00280119:
    v_rdi = (unsigned int)(((unsigned int)(*(unsigned int *)(gs_base + (0 + 420)))) >> (1));
    v_rdi = (unsigned int)((v_rdi) & (3));
    v_rbx = ((unsigned int)((unsigned int)(v_rdi))) << (6);
    v_rbx = (v_rbx) + (*(unsigned __int64 *)(v_rip + 12289831));
    if ((*(unsigned int *)(v_rip + 13921242)) != 0) goto loc_0028085E;
loc_0028014C:
    if (((*(unsigned __int8 *)(v_rip + 13920691)) & (33)) == 0) goto loc_00280163;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13163773))) == 0) goto loc_00280663;
loc_00280163:
loc_0028016C:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13163773))) != 0) goto loc_00280926;
loc_00280179:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34872) != 0) {
        *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34872) + 324) = (unsigned int)(v_rdi);
    }
loc_002801A8:
loc_002801AE:
    if (sign_flag) goto loc_002804B6;
    a4 = 0;
    goto loc_00280091;
loc_002801D2:
    if ((unsigned int)((unsigned int)(v_stack_p10)) != 0) goto loc_002804BD;
loc_002801DA:
    a1 = (v_stack_p8) >> (9);
    a1 = (a1) & (0);
    a1 = (a1) + (v_r13);
    v_stack_mE8 = a1;
    a1 = (a1) >> (9);
    a1 = (a1) & (0);
    a1 = (a1) + (v_r13);
    v_stack_mE0 = a1;
    a1 = (a1) >> (9);
    a1 = (a1) & (0);
    a1 = (a1) + (v_r13);
    v_stack_mD8 = a1;
    a1 = (a1) >> (9);
    a1 = (a1) & (0);
    a1 = (a1) + (v_r13);
    v_stack_mD0 = a1;
    v_stack_m100 = v_stack_p8;
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1024 + 184))) & (15));
    if (condition_is_not_equal) goto loc_00280839;
loc_0028025F:
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2 + 2 + 2500 * 2 * 8 + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1024 + 176;
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2 + 2 + 2500 * 2 * 8) = 0;
    if (((*(unsigned __int8 *)(v_rip + 13920391)) & (33)) != 0) goto loc_0028096F;
loc_00280285:
    if (*(unsigned __int64 *)(gs_base + (0 + 32)) + 2 + 2 + 2500 * 2 * 8 != 0) goto loc_00280B2A;
loc_00280294:
loc_00280297:
    v_stack_m118 = 2;
    if ((*(unsigned __int64 *)(v_rsp + 2 * 8 + 112)) < (*(unsigned __int64 *)(gs_base + (0 + 32)))) goto loc_002802E1;
    if ((*(unsigned __int64 *)(v_rsp + 2 * 8 + 112)) > (*(unsigned __int64 *)(gs_base + (0 + 32)))) goto loc_002802E1;
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp + 2 * 8 + 112)))) & (1)) == 0) goto loc_002802E1;
    a1 = ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp + 2 * 8 + 112)))) & (66)) != 0) ? 1 : 0;
    result = ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp + 2 * 8 + 112)))) & (32)) != 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) == 0) goto loc_0028044E;
loc_002802E1:
    result = (unsigned __int8)(((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp + 2 * 8 + 112)))) & (129));
    if (((unsigned __int8)(result)) != 1) goto loc_00280392;
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp + 2 * 8 + 112)))) & (32)) != 0) goto loc_00280379;
    v_rdi = (*(unsigned __int64 *)(v_rsp + 2 * 8 + 112)) << (25);
    v_rdi = (v_rdi) - (v_r12);
    v_rdi = (v_rdi) >> (16);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1024 + 184)))) & (15)) == 0) goto loc_00280331;
    if ((*(unsigned __int64 *)(v_rsp + 2 * 8 + 112)) < (*(unsigned __int64 *)(gs_base + (0 + 32)))) goto loc_00280331;
    if ((*(unsigned __int64 *)(v_rsp + 2 * 8 + 112)) <= (*(unsigned __int64 *)(gs_base + (0 + 32)))) goto loc_00280CA6;
loc_00280331:
    if (v_rdi >= (*(unsigned __int64 *)(gs_base + (0 + 32)))) goto loc_00280CCD;
loc_00280347:
    v_rbx = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp + 2 * 8 + 112))) | (32);
    result = MiWriteValidPteNewProtection(*(unsigned __int64 *)(v_rsp + 2 * 8 + 112), v_rbx, *(unsigned __int64 *)(gs_base + (0 + 32)), a4);
    a4 = 0;
    if (0 != 0) goto loc_00280CE8;
loc_0028036F:
loc_00280379:
    if ((*(unsigned __int64 *)(v_rsp + 2 * 8 + 112)) != v_stack_p8) goto loc_002803DE;
loc_0028037E:
    if (2 == 0) goto loc_00280392;
    v_r14 = (2) - 1;
    a4 = 0;
    goto loc_00280297;
loc_00280392:
    a1 = (v_stack_p8) >> (9);
    a1 = (a1) & (v_rbx);
    a1 = (a1) + (result);
    if (v_stack_p8 != a1) goto loc_00280A4F;
loc_002803C7:
    result = 0;
loc_002803C9:
    v_rsp = (v_rsp) + (280);
    return result;
loc_002803DE:
    if ((*(unsigned __int64 *)(v_rsp + 2 * 8 + 112)) != v_stack_p8) goto loc_002804F0;
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1024 + 184))) & (15));
    if (condition_is_not_equal) goto loc_002807EB;
loc_0028040C:
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(a4 + 2)))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(a4 + 2)))) + 2500 * 2 * 8 + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1024 + 176;
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(a4 + 2)))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(a4 + 2)))) + 2500 * 2 * 8) = 0;
    if (((*(unsigned __int8 *)(v_rip + 13919962)) & (33)) != 0) goto loc_00280957;
loc_00280432:
    if (*(unsigned __int64 *)(gs_base + (0 + 32)) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(a4 + 2)))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(a4 + 2)))) + 2500 * 2 * 8 == 0) goto loc_00280617;
    result = KxWaitForLockOwnerShip(*(unsigned __int64 *)(gs_base + (0 + 32)) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(a4 + 2)))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(a4 + 2)))) + 2500 * 2 * 8, *(unsigned __int64 *)(gs_base + (0 + 32)) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(a4 + 2)))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(a4 + 2)))) + 2500 * 2 * 8, *(unsigned __int64 *)(gs_base + (0 + 32)), a4);
    goto loc_00280614;
loc_0028044E:
    if (((*(unsigned __int64 *)(v_rip + 13919791)) & (0x600000ULL)) == 0) goto loc_002802E1;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 352)) == 1) goto loc_002802E1;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) == 0) goto loc_002802E1;
    result = (*(unsigned __int64 *)(v_rsp + 2 * 8 + 112)) >> (3);
    result = (unsigned int)((result) & (511));
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + result * 8))) & (32)) != 0) {
        v_rbx = (v_rbx) | (32);
    }
    v_rbx = (v_rbx) | (66);
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + result * 8))) & (66)) == 0) { v_rbx = v_rbx; }
    goto loc_002802E1;
loc_002804B6:
    goto loc_002803C9;
loc_002804BD:
    a3 = 0;
    result = MiFastLockLeafPageTable(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1024, v_rbx, a3, a4);
    if ((unsigned int)(result) != 0) goto loc_00280817;
    a4 = 0;
    goto loc_002801DA;
loc_002804F0:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1024 + 184)))) & (15)) != 0) goto loc_0028053C;
    if ((*(unsigned __int64 *)(v_rsp + 2 * 8 + 112)) < 0) goto loc_0028053C;
    if ((*(unsigned __int64 *)(v_rsp + 2 * 8 + 112)) > 0) goto loc_0028053C;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1040) + 1384) != 0) goto loc_00280BC2;
loc_0028053C:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1024 + 184)))) & (15)) == 0) goto loc_00280565;
    if ((*(unsigned __int64 *)(v_rsp + 2 * 8 + 112)) < 0) goto loc_00280565;
    if ((*(unsigned __int64 *)(v_rsp + 2 * 8 + 112)) <= 0) goto loc_00280A8A;
loc_00280565:
    if ((*(unsigned __int64 *)(v_rsp + 2 * 8 + 112)) < 0) goto loc_0028059E;
    if ((*(unsigned __int64 *)(v_rsp + 2 * 8 + 112)) > 0) goto loc_0028059E;
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp + 2 * 8 + 112)))) & (1)) == 0) goto loc_0028059E;
    a1 = ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp + 2 * 8 + 112)))) & (66)) != 0) ? 1 : 0;
    result = ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp + 2 * 8 + 112)))) & (32)) != 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) == 0) goto loc_002808BE;
loc_0028059E:
loc_002805BC:
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp + 2 * 8 + 112)))) & (1)) == 0) goto loc_002805F6;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp + 2 * 8 + 112))) >> (60);
    if ((((unsigned __int8)(result)) & (1)) != 0) goto loc_00280990;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp + 2 * 8 + 112))) & (v_r14);
    a1 = (a1) | (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1024);
    if (((*(unsigned __int64 *)(v_rip + 13919396)) & (0x2000000ULL)) != 0) {
    }
    if (((*(unsigned __int64 *)(v_rip + 13919396)) & (0x2000000ULL)) != 0) goto loc_002805BC;
loc_002805F6:
loc_002805FB:
loc_00280614:
    a4 = 0;
loc_00280617:
    if (v_stack_p58 == v_stack_p8) goto loc_002806F4;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p38 + 184)))) & (15)) == 0) goto loc_00280674;
loc_00280638:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p38 + 184)))) & (15)) != 0) goto loc_0028077D;
loc_00280647:
loc_00280656:
    v_stack_p58 = *(unsigned __int64 *)(v_rsp + 2 * 8 + 112);
    goto loc_0028037E;
loc_00280663:
    result = ExpAcquireSpinLockSharedAtDpcLevelInstrumented(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp + 2 * 8 + 112)), 0, a3, a4);
    goto loc_00280179;
loc_00280674:
    if ((*(unsigned __int64 *)(v_rsp + 2 * 8 + 112)) < 0) goto loc_00280638;
    if ((*(unsigned __int64 *)(v_rsp + 2 * 8 + 112)) > 0) goto loc_00280638;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1040) + 1384) == 0) goto loc_00280638;
    v_r13 = (unsigned int)((*(unsigned __int64 *)(v_rsp + 2 * 8 + 112)) >> (3));
    v_r13 = (unsigned int)((v_r13) & (511));
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1040) + 1384) + v_r13 * 4)))) & (0x3FFFFFFFULL)) != 0) goto loc_0028089A;
    if (!sign_flag) goto loc_00280B6A;
    if (((*(unsigned __int8 *)(v_rip + 13919272)) & (1)) != 0) goto loc_00280BEB;
loc_002806E4:
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1040) + 1384) + v_r13 * 4) = 0;
    v_stack_p58 = *(unsigned __int64 *)(v_rsp + 2 * 8 + 112);
    goto loc_0028037E;
loc_002806F4:
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(v_stack_p38 + 184))) & (15));
    if (condition_is_not_equal) goto loc_0028093F;
loc_00280711:
    v_rbx = (*(unsigned __int64 *)(gs_base + (0 + 32)) + 40000) + (48);
    if (((*(unsigned __int8 *)(v_rip + 13919204)) & (1)) != 0) goto loc_0028086F;
loc_00280728:
    if (*(unsigned __int64 *)(v_rbx) != 0) goto loc_00280750;
    if (*(unsigned __int64 *)(v_rbx) == 0) goto loc_00280656;
    result = KxWaitForLockChainValid(v_rbx, *(unsigned __int64 *)(gs_base + (0 + 32)), a3, a4);
    a4 = 0;
loc_00280750:
    *(unsigned __int64 *)(v_rbx) = 0;
    result = (unsigned __int8)((*(unsigned __int64 *)(v_rbx + 8)) ^ ((unsigned __int8)(*(unsigned __int64 *)(v_rbx + 8))));
    if ((((unsigned __int8)(result)) & (4)) == 0) goto loc_00280656;
    result = KeWakeAddressAll(result + 8, *(unsigned __int64 *)(v_rbx + 8), a3, a4);
    v_stack_p58 = *(unsigned __int64 *)(v_rsp + 2 * 8 + 112);
    goto loc_0028037E;
loc_0028077D:
    if ((*(unsigned __int64 *)(v_rsp + 2 * 8 + 112)) < 0) goto loc_00280647;
    if ((*(unsigned __int64 *)(v_rsp + 2 * 8 + 112)) > 0) goto loc_00280647;
    v_r13 = (*(unsigned __int64 *)(v_rsp + 2 * 8 + 112)) - (0);
    v_r13 = (v_r13) >> (3);
    result = ((unsigned int)((unsigned int)(v_r13 * 2))) >> (5);
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_r13 * 2))) & (31));
    result = (unsigned int)((3) << ((unsigned __int8)(a1)));
    result = (unsigned int)(~(result));
    v_stack_p58 = *(unsigned __int64 *)(v_rsp + 2 * 8 + 112);
    goto loc_0028037E;
loc_002807EB:
    if (((unsigned __int8)(result)) == 7) goto loc_00280A04;
    a1 = 3;
    if (((unsigned __int8)(result)) == 5) { a1 = 0; }
loc_002807FE:
    a2 = (v_rip + 12239673 + (unsigned int)((unsigned int)(a1)) * 8) + (0x3280ULL);
    goto loc_0028040C;
loc_00280817:
    if (((unsigned int)((unsigned int)((unsigned int)(a1)))) == 1) goto loc_002803C7;
loc_0028082A:
    v_rdi = (v_stack_p8) >> (9);
    v_rdi = (v_rdi) & (a2);
    v_rdi = (v_rdi) + (*(unsigned __int64 *)(v_rsp + 2 * 8 + 112));
    goto loc_0028082A;
loc_00280839:
    if (((unsigned __int8)(*(unsigned __int64 *)(v_rsp + 2 * 8 + 112))) == 7) goto loc_00280A0E;
    a1 = 3;
    if (((unsigned __int8)(*(unsigned __int64 *)(v_rsp + 2 * 8 + 112))) == 5) { a1 = 0; }
    a2 = ((unsigned int)((unsigned int)(a1))) + (0x650ULL);
    goto loc_0028025F;
loc_0028085E:
    result = KiRaiseIrqlProcessIrqlFlags(0, (unsigned __int8)(*(unsigned __int64 *)(v_rsp + 2 * 8 + 112)), a3, a4);
    goto loc_0028014C;
loc_0028086F:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13161955))) != 0) goto loc_00280728;
    result = KiReleaseQueuedSpinLockInstrumented(v_rbx, v_stack_p158, a3, a4);
    v_stack_p58 = *(unsigned __int64 *)(v_rsp + 2 * 8 + 112);
    goto loc_0028037E;
loc_0028089A:
    if (((*(unsigned __int8 *)(v_rip + 13918821)) & (1)) != 0) goto loc_00280C32;
loc_002808A7:
    v_stack_p58 = *(unsigned __int64 *)(v_rsp + 2 * 8 + 112);
    goto loc_0028037E;
loc_002808BE:
    if (((*(unsigned __int64 *)(v_rip + 13918655)) & (0x600000ULL)) == 0) goto loc_0028059E;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 352)) == 1) goto loc_0028059E;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) == 0) goto loc_0028059E;
    result = (*(unsigned __int64 *)(v_rsp + 2 * 8 + 112)) >> (3);
    result = (unsigned int)((result) & (511));
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + result * 8))) & (32)) != 0) {
        v_rbx = (v_rbx) | (32);
    }
    v_rbx = (v_rbx) | (66);
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + result * 8))) & (66)) == 0) { v_rbx = v_rbx; }
    goto loc_0028059E;
loc_00280926:
    if (!sign_flag) goto loc_0028016C;
    result = ExpWaitForSpinLockSharedAndAcquire(v_rbx, 0, a3, a4);
    goto loc_00280179;
loc_0028093F:
    if (((unsigned __int8)(result)) == 7) goto loc_00280B20;
    a1 = 72;
    if (((unsigned __int8)(result)) == 5) { a1 = 0; }
    goto loc_00280711;
loc_00280957:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13161723))) != 0) goto loc_00280432;
    result = KiAcquireQueuedSpinLockInstrumented(a1, 0, a3, a4);
    goto loc_00280614;
loc_0028096F:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13161699))) != 0) goto loc_00280285;
    result = KiAcquireQueuedSpinLockInstrumented(a1, 0, a3, a4);
loc_00280982:
    a4 = 0;
    goto loc_00280294;
loc_00280990:
    if ((((unsigned __int8)(result)) & (2)) != 0) goto loc_00280A30;
    v_rdi = (v_rbx) | (result);
    if (((*(unsigned __int64 *)(v_rip + 13918421)) & (0x2000000ULL)) != 0) {
    }
    if (condition_is_below) goto loc_00280B85;
loc_002809C7:
    if (((*(unsigned __int64 *)(v_rip + 13918421)) & (0x2000000ULL)) == 0) { v_rbx = v_rdi; }
    goto loc_002805BC;
loc_002809DB:
    if ((*(unsigned int *)(v_rip + 13919024)) == 0) goto loc_002801AE;
    result = KiRaiseIrqlProcessIrqlFlags(2, 2, a3, a4);
    goto loc_002801A8;
loc_00280A04:
    goto loc_002807FE;
loc_00280A0E:
    a2 = (1) + (0x650ULL);
    goto loc_0028025F;
loc_00280A30:
    v_rbp = (unsigned int)((0) + 1);
    if (((*(unsigned int *)(v_rip + 13912180)) & ((unsigned int)(v_rbp))) == 0) goto loc_00280AF9;
loc_00280A3E:
loc_00280A40:
    if (condition_is_below) goto loc_00280A30;
    goto loc_002805BC;
loc_00280A4F:
    result = MiUnlockPageTable(v_stack_p38, *(unsigned __int64 *)(v_rsp + 2 * 8 + 112), a3, a4);
    result = MiUnlockWorkingSetShared(v_stack_p38, v_stack_p170, a3, a4);
    goto loc_002800CB;
loc_00280A8A:
    a1 = (*(unsigned __int64 *)(v_rsp + 2 * 8 + 112)) - (0);
    a1 = (a1) >> (3);
    a1 = (unsigned int)((a1) + ((unsigned int)(a1)));
    v_rdi = ((unsigned int)((unsigned int)(a1))) >> (5);
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)(a1))) & (31));
    v_rbp = (unsigned int)((1) << ((unsigned __int8)((unsigned int)((unsigned int)(v_rbx)))));
    v_r15 = (unsigned int)((2) << ((unsigned __int8)((unsigned int)((unsigned int)(v_rbx)))));
    v_r14 = (unsigned int)(~((unsigned int)((unsigned int)(v_r15))));
loc_00280AD8:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12238982 + 9836 + v_rdi * 4))))) >> ((unsigned __int8)((unsigned int)((unsigned int)(v_rbx)))));
    if ((((unsigned __int8)(result)) & (1)) != 0) goto loc_00280B37;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12238982 + 9836 + v_rdi * 4))))) | ((unsigned int)(v_rbp)));
    a1 = (unsigned int)((a1) & ((unsigned int)(v_r14)));
    if (condition_is_equal) goto loc_002805FB;
    goto loc_00280AD8;
loc_00280AF9:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13918137)))) & (64)) == 0) goto loc_00280A3E;
    result = KiCheckVpBackingLongSpinWaitHypercall(a1, (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12238982 + 9836 + v_rdi * 4)))))), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00280A3E;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rbp)), (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12238982 + 9836 + v_rdi * 4)))))), a3, a4);
    goto loc_00280A40;
loc_00280B20:
    goto loc_00280711;
loc_00280B2A:
    result = KxWaitForLockOwnerShip(24, result, a3, a4);
    goto loc_00280982;
loc_00280B37:
    if ((((unsigned __int8)(result)) & (2)) != 0) goto loc_00280C13;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(result))) | ((unsigned int)(v_r15)));
    a2 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
    if (condition_is_equal) { a2 = (unsigned int)(a1); }
    goto loc_00280AD8;
loc_00280B51:
    result = MiLockWorkingSetExclusive(v_r15, a2, a3, a4);
    goto loc_002801A8;
loc_00280B5E:
    goto loc_00280119;
loc_00280B6A:
    v_stack_p20 = 0;
    a4 = 0;
    result = KeBugCheckEx(a4 + 16, v_r15, 256, a4);
loc_00280B85:
    result = (unsigned __int8)(((unsigned __int8)(v_rip + 12238982 + 9836 + v_rdi * 4)) & (33));
    if (((unsigned __int8)(result)) != 1) goto loc_002809C7;
    result = (0) + (a4 + 16);
    if ((*(unsigned __int64 *)(v_rsp + 2 * 8 + 112)) < result) goto loc_002809C7;
    result = MiCheckLinearProtectedPteAccessedBit(*(unsigned __int64 *)(v_rsp + 2 * 8 + 112), v_rip + 12238982 + 9836 + v_rdi * 4, 128, a4);
    goto loc_002809C7;
loc_00280BC2:
    result = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rsp + 2 * 8 + 112)))) >> (3));
    result = (unsigned int)((result) & (511));
    result = ExAcquireSpinLockExclusiveAtDpcLevel(*(unsigned __int64 *)(v_rsp + 2 * 8 + 112) + result * 4, v_rip + 12238982 + 9836 + v_rdi * 4, 128, a4);
    goto loc_00280614;
loc_00280BDA:
    v_stack_p60 = 0;
    goto loc_0027FFFB;
loc_00280BEB:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13161063))) != 0) goto loc_002806E4;
    result = ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented(*(unsigned __int64 *)(v_rsp + 2 * 8 + 112) + result * 4, v_stack_p158, 128, a4);
    v_stack_p58 = *(unsigned __int64 *)(v_rsp + 2 * 8 + 112);
    goto loc_0028037E;
loc_00280C13:
    v_r12 = (unsigned int)((0) + 1);
    if (((*(unsigned int *)(v_rip + 13911695)) & ((unsigned int)(v_r12))) == 0) goto loc_00280C86;
loc_00280C1F:
loc_00280C21:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12238982 + 9836 + v_rdi * 4))))) >> ((unsigned __int8)((unsigned int)((unsigned int)(v_rbx)))));
    if ((((unsigned __int8)(result)) & (1)) != 0) goto loc_00280C13;
    goto loc_00280AD8;
loc_00280C32:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13160992))) != 0) goto loc_002808A7;
    result = ExpReleaseSpinLockSharedFromDpcLevelInstrumented((unsigned int)((unsigned int)(v_rbx)), v_stack_p158, 128, a4);
    v_stack_p58 = *(unsigned __int64 *)(v_rsp + 2 * 8 + 112);
    goto loc_0028037E;
loc_00280C5A:
    if ((unsigned int)(v_r14) != 0) goto loc_002800E8;
    result = MiFlushAllFilesystemPages(v_r14 + 1, v_stack_p158, 128, a4);
    v_stack_p20 = v_rip + 12238982 + 9836 + v_rdi * 4;
    result = KeBugCheckEx(v_r14 + 1 + 121, v_r14 + 1, *(unsigned __int64 *)(v_rsp + 2 * 8 + 112), v_stack_p60);
loc_00280C86:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13917740)))) & (64)) == 0) goto loc_00280C1F;
    result = KiCheckVpBackingLongSpinWaitHypercall(v_r14 + 1 + 121, v_r14 + 1, *(unsigned __int64 *)(v_rsp + 2 * 8 + 112), v_stack_p60);
    if ((unsigned __int8)(result) == 0) goto loc_00280C1F;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_r12)), v_r14 + 1, *(unsigned __int64 *)(v_rsp + 2 * 8 + 112), v_stack_p60);
    goto loc_00280C21;
loc_00280CA6:
    result = ExAcquireSpinLockExclusiveAtDpcLevel(v_rip + 12281875, v_r14 + 1, *(unsigned __int64 *)(v_rsp + 2 * 8 + 112), v_stack_p60);
    a4 = 0;
    goto loc_00280331;
loc_00280CCD:
    if ((v_rip + 12238982 + 9836 + v_rdi * 4) > result) goto loc_00280347;
loc_00280CE8:
    result = ExReleaseSpinLockExclusiveFromDpcLevel(v_rip + 12281809, v_r14 + 1, *(unsigned __int64 *)(v_rsp + 2 * 8 + 112), a4);
    a4 = 0;
    goto loc_0028036F;
}
```

## 5. (Beta) C Style

```c
int64_t MiMakeSystemAddressValid(int64_t Arg1, int32_t Arg2, uint8_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint32_t v_stack_m124;
    uint64_t v_stack_m88;
    uint64_t v_stack_m98;
    uint32_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB8;
    uint32_t v_stack_mC7;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint32_t v_stack_p10;
    uint64_t v_stack_p158;
    uint8_t v_stack_p170;
    uint32_t v_stack_p178;
    uint8_t v_stack_p18;
    uint32_t v_stack_p20;
    uint32_t v_stack_p34;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_p60;
    uint64_t v_stack_p8;

    *(uint8_t *)(local_rsp + 0x18) = Arg3;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (280);
    v_stack_mC8 = v_xmm0;
    result = 0;
    Arg4 = 0;
    v_stack_mB8 = v_xmm0;
    v_stack_mA8 = v_xmm0;
    v_stack_m98 = v_xmm0;
    v_stack_m88 = v_xmm0;
    *(uint64_t *)(local_rsp - 0x58) = 0;
    *(uint64_t *)(local_rsp - 0x78) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x68) = v_xmm0;
    if ((((uint8_t)((uint32_t)(Arg4))) & (4)) != 0) goto loc_00280BDA;
    v_stack_mF8 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8);
loc_0027FFFB:
    v_stack_m120 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 1024;
    local_r14 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg4)))) & (8));
    v_stack_mA0 = Arg2;
    v_stack_m124 = (uint32_t)(local_r14);
    result = (condition_is_not_equal) ? 1 : 0;
    result = (uint8_t)((result) + (7));
    local_rbp = (v_stack_mC8) | (1);
    v_stack_mC8 = (uint8_t)(result);
    v_stack_m110 = local_rbp;
    local_r12 = (local_r13) << (25);
    Arg1 = (Arg1) << (25);
    Arg1 = (Arg1) - (local_r12);
    v_stack_m108 = local_r12;
    Arg1 = (Arg1) >> (16);
    v_stack_mF0 = Arg1;
    if (Arg1 < local_r13) goto loc_00280075;
    if (Arg1 > Arg2) goto loc_00280075;
    goto loc_0028007A;
loc_00280075:
loc_0028007A:
    local_rbx = (uint32_t)(((uint32_t)(Arg4)) & (1));
    v_stack_p10 = 1;
    v_stack_p20 = (uint32_t)(local_rbx);
loc_00280091:
    if ((uint32_t)(local_rbx) == 0) goto loc_002801D2;
    result = MmIsAddressValidEx(Arg1, 1, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), Arg4);
    if ((uint8_t)(result) != 0) goto loc_002803C7;
    result = MiUnlockWorkingSetExclusive(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 1024, Arg3, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), Arg4);
loc_002800CB:
    Arg3 = 0;
    result = MmAccessFault(Arg3 + 2, Arg1, Arg3, local_rbp);
    if (sign_flag) goto loc_00280C5A;
loc_002800E8:
    if ((uint32_t)(local_rbx) != 0) goto loc_00280B51;
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x400 + 0xB8))) & (15));
    if (((uint8_t)(result)) >= 6) goto loc_002809DB;
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x400 + 0xB8))) & (15));
    if (((uint8_t)(result)) != 1) goto loc_00280B5E;
loc_00280119:
    local_rdi = (uint32_t)(((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4)))) >> (1));
    local_rdi = (uint32_t)((local_rdi) & (3));
    local_rbx = ((uint32_t)((uint32_t)(local_rdi))) << (6);
    local_rbx = (local_rbx) + (*(uint64_t *)(v_rip + 0xBB8727));
    if ((*(uint32_t *)(v_rip + 0xD46BDA)) != 0) goto loc_0028085E;
loc_0028014C:
    if (((*(uint8_t *)(v_rip + 0xD469B3)) & (33)) == 0) goto loc_00280163;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC8DCFD))) == 0) goto loc_00280663;
loc_00280163:
loc_0028016C:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC8DCFD))) != 0) goto loc_00280926;
loc_00280179:
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8838) != 0) {
        *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8838) + 0x144) = (uint32_t)(local_rdi);
    }
loc_002801A8:
loc_002801AE:
    if (sign_flag) goto loc_002804B6;
    Arg4 = 0;
    goto loc_00280091;
loc_002801D2:
    if ((uint32_t)((uint32_t)(v_stack_p10)) != 0) goto loc_002804BD;
loc_002801DA:
    Arg1 = (v_stack_p8) >> (9);
    Arg1 = (Arg1) & (0);
    Arg1 = (Arg1) + (local_r13);
    v_stack_mE8 = Arg1;
    Arg1 = (Arg1) >> (9);
    Arg1 = (Arg1) & (0);
    Arg1 = (Arg1) + (local_r13);
    v_stack_mE0 = Arg1;
    Arg1 = (Arg1) >> (9);
    Arg1 = (Arg1) & (0);
    Arg1 = (Arg1) + (local_r13);
    v_stack_mD8 = Arg1;
    Arg1 = (Arg1) >> (9);
    Arg1 = (Arg1) & (0);
    Arg1 = (Arg1) + (local_r13);
    v_stack_mD0 = Arg1;
    v_stack_m100 = v_stack_p8;
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x400 + 0xB8))) & (15));
    if (condition_is_not_equal) goto loc_00280839;
loc_0028025F:
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x2 + 0x2 + 0x9C4 * 2 * 8 + 0x8) = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 1024 + 176;
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x2 + 0x2 + 0x9C4 * 2 * 8) = 0;
    if (((*(uint8_t *)(v_rip + 0xD46887)) & (33)) != 0) goto loc_0028096F;
loc_00280285:
    if (*(uint64_t *)(gs_base + (0 + 0x20)) + 2 + 2 + 2500 * 2 * 8 != 0) goto loc_00280B2A;
loc_00280294:
loc_00280297:
    v_stack_m118 = 2;
    if ((*(uint64_t *)(local_rsp + 0x2 * 8 + 0x70)) < (*(uint64_t *)(gs_base + (0 + 0x20)))) goto loc_002802E1;
    if ((*(uint64_t *)(local_rsp + 0x2 * 8 + 0x70)) > (*(uint64_t *)(gs_base + (0 + 0x20)))) goto loc_002802E1;
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(local_rsp + 0x2 * 8 + 0x70)))) & (1)) == 0) goto loc_002802E1;
    Arg1 = ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(local_rsp + 0x2 * 8 + 0x70)))) & (66)) != 0) ? 1 : 0;
    result = ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(local_rsp + 0x2 * 8 + 0x70)))) & (32)) != 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) == 0) goto loc_0028044E;
loc_002802E1:
    result = (uint8_t)(((uint8_t)(*(uint64_t *)(*(uint64_t *)(local_rsp + 0x2 * 8 + 0x70)))) & (129));
    if (((uint8_t)(result)) != 1) goto loc_00280392;
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(local_rsp + 0x2 * 8 + 0x70)))) & (32)) != 0) goto loc_00280379;
    local_rdi = (*(uint64_t *)(local_rsp + 0x2 * 8 + 0x70)) << (25);
    local_rdi = (local_rdi) - (local_r12);
    local_rdi = (local_rdi) >> (16);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x400 + 0xB8)))) & (15)) == 0) goto loc_00280331;
    if ((*(uint64_t *)(local_rsp + 0x2 * 8 + 0x70)) < (*(uint64_t *)(gs_base + (0 + 0x20)))) goto loc_00280331;
    if ((*(uint64_t *)(local_rsp + 0x2 * 8 + 0x70)) <= (*(uint64_t *)(gs_base + (0 + 0x20)))) goto loc_00280CA6;
loc_00280331:
    if (local_rdi >= (*(uint64_t *)(gs_base + (0 + 0x20)))) goto loc_00280CCD;
loc_00280347:
    local_rbx = (*(uint64_t *)(*(uint64_t *)(local_rsp + 0x2 * 8 + 0x70))) | (32);
    result = MiWriteValidPteNewProtection(*(uint64_t *)(local_rsp + 0x2 * 8 + 0x70), local_rbx, *(uint64_t *)(gs_base + (0 + 0x20)), Arg4);
    Arg4 = 0;
    if (0 != 0) goto loc_00280CE8;
loc_0028036F:
loc_00280379:
    if ((*(uint64_t *)(local_rsp + 0x2 * 8 + 0x70)) != v_stack_p8) goto loc_002803DE;
loc_0028037E:
    if (2 == 0) goto loc_00280392;
    local_r14 = (2) - 1;
    Arg4 = 0;
    goto loc_00280297;
loc_00280392:
    Arg1 = (v_stack_p8) >> (9);
    Arg1 = (Arg1) & (local_rbx);
    Arg1 = (Arg1) + (result);
    if (v_stack_p8 != Arg1) goto loc_00280A4F;
loc_002803C7:
    result = 0;
loc_002803C9:
    local_rsp = (local_rsp) + (280);
    return result;
loc_002803DE:
    if ((*(uint64_t *)(local_rsp + 0x2 * 8 + 0x70)) != v_stack_p8) goto loc_002804F0;
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x400 + 0xB8))) & (15));
    if (condition_is_not_equal) goto loc_002807EB;
loc_0028040C:
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg4 + 0x2)))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg4 + 0x2)))) + 0x9C4 * 2 * 8 + 0x8) = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 1024 + 176;
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg4 + 0x2)))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg4 + 0x2)))) + 0x9C4 * 2 * 8) = 0;
    if (((*(uint8_t *)(v_rip + 0xD466DA)) & (33)) != 0) goto loc_00280957;
loc_00280432:
    if (*(uint64_t *)(gs_base + (0 + 0x20)) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg4 + 2)))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg4 + 2)))) + 2500 * 2 * 8 == 0) goto loc_00280617;
    result = KxWaitForLockOwnerShip(*(uint64_t *)(gs_base + (0 + 0x20)) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg4 + 2)))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg4 + 2)))) + 2500 * 2 * 8, *(uint64_t *)(gs_base + (0 + 0x20)) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg4 + 2)))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg4 + 2)))) + 2500 * 2 * 8, *(uint64_t *)(gs_base + (0 + 0x20)), Arg4);
    goto loc_00280614;
loc_0028044E:
    if (((*(uint64_t *)(v_rip + 0xD4662F)) & (0x600000ULL)) == 0) goto loc_002802E1;
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x160)) == 1) goto loc_002802E1;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) == 0) goto loc_002802E1;
    result = (*(uint64_t *)(local_rsp + 0x2 * 8 + 0x70)) >> (3);
    result = (uint32_t)((result) & (511));
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + result * 8))) & (32)) != 0) {
        local_rbx = (local_rbx) | (32);
    }
    local_rbx = (local_rbx) | (66);
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + result * 8))) & (66)) == 0) { local_rbx = local_rbx; }
    goto loc_002802E1;
loc_002804B6:
    goto loc_002803C9;
loc_002804BD:
    Arg3 = 0;
    result = MiFastLockLeafPageTable(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 1024, local_rbx, Arg3, Arg4);
    if ((uint32_t)(result) != 0) goto loc_00280817;
    Arg4 = 0;
    goto loc_002801DA;
loc_002804F0:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x400 + 0xB8)))) & (15)) != 0) goto loc_0028053C;
    if ((*(uint64_t *)(local_rsp + 0x2 * 8 + 0x70)) < 0) goto loc_0028053C;
    if ((*(uint64_t *)(local_rsp + 0x2 * 8 + 0x70)) > 0) goto loc_0028053C;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x410) + 0x568) != 0) goto loc_00280BC2;
loc_0028053C:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x400 + 0xB8)))) & (15)) == 0) goto loc_00280565;
    if ((*(uint64_t *)(local_rsp + 0x2 * 8 + 0x70)) < 0) goto loc_00280565;
    if ((*(uint64_t *)(local_rsp + 0x2 * 8 + 0x70)) <= 0) goto loc_00280A8A;
loc_00280565:
    if ((*(uint64_t *)(local_rsp + 0x2 * 8 + 0x70)) < 0) goto loc_0028059E;
    if ((*(uint64_t *)(local_rsp + 0x2 * 8 + 0x70)) > 0) goto loc_0028059E;
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(local_rsp + 0x2 * 8 + 0x70)))) & (1)) == 0) goto loc_0028059E;
    Arg1 = ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(local_rsp + 0x2 * 8 + 0x70)))) & (66)) != 0) ? 1 : 0;
    result = ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(local_rsp + 0x2 * 8 + 0x70)))) & (32)) != 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) == 0) goto loc_002808BE;
loc_0028059E:
loc_002805BC:
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(local_rsp + 0x2 * 8 + 0x70)))) & (1)) == 0) goto loc_002805F6;
    result = (*(uint64_t *)(*(uint64_t *)(local_rsp + 0x2 * 8 + 0x70))) >> (60);
    if ((((uint8_t)(result)) & (1)) != 0) goto loc_00280990;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(local_rsp + 0x2 * 8 + 0x70))) & (local_r14);
    Arg1 = (Arg1) | (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 1024);
    if (((*(uint64_t *)(v_rip + 0xD464A4)) & (0x2000000ULL)) != 0) {
    }
    if (((*(uint64_t *)(v_rip + 0xD464A4)) & (0x2000000ULL)) != 0) goto loc_002805BC;
loc_002805F6:
loc_002805FB:
loc_00280614:
    Arg4 = 0;
loc_00280617:
    if (v_stack_p58 == v_stack_p8) goto loc_002806F4;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p38 + 0xB8)))) & (15)) == 0) goto loc_00280674;
loc_00280638:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p38 + 0xB8)))) & (15)) != 0) goto loc_0028077D;
loc_00280647:
loc_00280656:
    v_stack_p58 = *(uint64_t *)(local_rsp + 0x2 * 8 + 0x70);
    goto loc_0028037E;
loc_00280663:
    result = ExpAcquireSpinLockSharedAtDpcLevelInstrumented(*(uint64_t *)(*(uint64_t *)(local_rsp + 0x2 * 8 + 0x70)), 0, Arg3, Arg4);
    goto loc_00280179;
loc_00280674:
    if ((*(uint64_t *)(local_rsp + 0x2 * 8 + 0x70)) < 0) goto loc_00280638;
    if ((*(uint64_t *)(local_rsp + 0x2 * 8 + 0x70)) > 0) goto loc_00280638;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x410) + 0x568) == 0) goto loc_00280638;
    local_r13 = (uint32_t)((*(uint64_t *)(local_rsp + 0x2 * 8 + 0x70)) >> (3));
    local_r13 = (uint32_t)((local_r13) & (511));
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x410) + 0x568) + local_r13 * 4)))) & (0x3FFFFFFFULL)) != 0) goto loc_0028089A;
    if (!sign_flag) goto loc_00280B6A;
    if (((*(uint8_t *)(v_rip + 0xD46428)) & (1)) != 0) goto loc_00280BEB;
loc_002806E4:
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x410) + 0x568) + local_r13 * 4) = 0;
    v_stack_p58 = *(uint64_t *)(local_rsp + 0x2 * 8 + 0x70);
    goto loc_0028037E;
loc_002806F4:
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(v_stack_p38 + 0xB8))) & (15));
    if (condition_is_not_equal) goto loc_0028093F;
loc_00280711:
    local_rbx = (*(uint64_t *)(gs_base + (0 + 0x20)) + 40000) + (48);
    if (((*(uint8_t *)(v_rip + 0xD463E4)) & (1)) != 0) goto loc_0028086F;
loc_00280728:
    if (*(uint64_t *)(local_rbx) != 0) goto loc_00280750;
    if (*(uint64_t *)(local_rbx) == 0) goto loc_00280656;
    result = KxWaitForLockChainValid(local_rbx, *(uint64_t *)(gs_base + (0 + 0x20)), Arg3, Arg4);
    Arg4 = 0;
loc_00280750:
    *(uint64_t *)(local_rbx) = 0;
    result = (uint8_t)((*(uint64_t *)(local_rbx + 0x8)) ^ ((uint8_t)(*(uint64_t *)(local_rbx + 0x8))));
    if ((((uint8_t)(result)) & (4)) == 0) goto loc_00280656;
    result = KeWakeAddressAll(result + 8, *(uint64_t *)(local_rbx + 0x8), Arg3, Arg4);
    v_stack_p58 = *(uint64_t *)(local_rsp + 0x2 * 8 + 0x70);
    goto loc_0028037E;
loc_0028077D:
    if ((*(uint64_t *)(local_rsp + 0x2 * 8 + 0x70)) < 0) goto loc_00280647;
    if ((*(uint64_t *)(local_rsp + 0x2 * 8 + 0x70)) > 0) goto loc_00280647;
    local_r13 = (*(uint64_t *)(local_rsp + 0x2 * 8 + 0x70)) - (0);
    local_r13 = (local_r13) >> (3);
    result = ((uint32_t)((uint32_t)(local_r13 * 2))) >> (5);
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_r13 * 2))) & (31));
    result = (uint32_t)((3) << ((uint8_t)(Arg1)));
    result = (uint32_t)(~(result));
    v_stack_p58 = *(uint64_t *)(local_rsp + 0x2 * 8 + 0x70);
    goto loc_0028037E;
loc_002807EB:
    if (((uint8_t)(result)) == 7) goto loc_00280A04;
    Arg1 = 3;
    if (((uint8_t)(result)) == 5) { Arg1 = 0; }
loc_002807FE:
    Arg2 = (v_rip + 12239673 + (uint32_t)((uint32_t)(Arg1)) * 8) + (0x3280ULL);
    goto loc_0028040C;
loc_00280817:
    if (((uint32_t)((uint32_t)((uint32_t)(Arg1)))) == 1) goto loc_002803C7;
loc_0028082A:
    local_rdi = (v_stack_p8) >> (9);
    local_rdi = (local_rdi) & (Arg2);
    local_rdi = (local_rdi) + (*(uint64_t *)(local_rsp + 0x2 * 8 + 0x70));
    goto loc_0028082A;
loc_00280839:
    if (((uint8_t)(*(uint64_t *)(local_rsp + 0x2 * 8 + 0x70))) == 7) goto loc_00280A0E;
    Arg1 = 3;
    if (((uint8_t)(*(uint64_t *)(local_rsp + 0x2 * 8 + 0x70))) == 5) { Arg1 = 0; }
    Arg2 = ((uint32_t)((uint32_t)(Arg1))) + (0x650ULL);
    goto loc_0028025F;
loc_0028085E:
    result = KiRaiseIrqlProcessIrqlFlags(0, (uint8_t)(*(uint64_t *)(local_rsp + 0x2 * 8 + 0x70)), Arg3, Arg4);
    goto loc_0028014C;
loc_0028086F:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC8D5E3))) != 0) goto loc_00280728;
    result = KiReleaseQueuedSpinLockInstrumented(local_rbx, v_stack_p158, Arg3, Arg4);
    v_stack_p58 = *(uint64_t *)(local_rsp + 0x2 * 8 + 0x70);
    goto loc_0028037E;
loc_0028089A:
    if (((*(uint8_t *)(v_rip + 0xD46265)) & (1)) != 0) goto loc_00280C32;
loc_002808A7:
    v_stack_p58 = *(uint64_t *)(local_rsp + 0x2 * 8 + 0x70);
    goto loc_0028037E;
loc_002808BE:
    if (((*(uint64_t *)(v_rip + 0xD461BF)) & (0x600000ULL)) == 0) goto loc_0028059E;
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x160)) == 1) goto loc_0028059E;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) == 0) goto loc_0028059E;
    result = (*(uint64_t *)(local_rsp + 0x2 * 8 + 0x70)) >> (3);
    result = (uint32_t)((result) & (511));
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + result * 8))) & (32)) != 0) {
        local_rbx = (local_rbx) | (32);
    }
    local_rbx = (local_rbx) | (66);
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + result * 8))) & (66)) == 0) { local_rbx = local_rbx; }
    goto loc_0028059E;
loc_00280926:
    if (!sign_flag) goto loc_0028016C;
    result = ExpWaitForSpinLockSharedAndAcquire(local_rbx, 0, Arg3, Arg4);
    goto loc_00280179;
loc_0028093F:
    if (((uint8_t)(result)) == 7) goto loc_00280B20;
    Arg1 = 72;
    if (((uint8_t)(result)) == 5) { Arg1 = 0; }
    goto loc_00280711;
loc_00280957:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC8D4FB))) != 0) goto loc_00280432;
    result = KiAcquireQueuedSpinLockInstrumented(Arg1, 0, Arg3, Arg4);
    goto loc_00280614;
loc_0028096F:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC8D4E3))) != 0) goto loc_00280285;
    result = KiAcquireQueuedSpinLockInstrumented(Arg1, 0, Arg3, Arg4);
loc_00280982:
    Arg4 = 0;
    goto loc_00280294;
loc_00280990:
    if ((((uint8_t)(result)) & (2)) != 0) goto loc_00280A30;
    local_rdi = (local_rbx) | (result);
    if (((*(uint64_t *)(v_rip + 0xD460D5)) & (0x2000000ULL)) != 0) {
    }
    if (condition_is_below) goto loc_00280B85;
loc_002809C7:
    if (((*(uint64_t *)(v_rip + 0xD460D5)) & (0x2000000ULL)) == 0) { local_rbx = local_rdi; }
    goto loc_002805BC;
loc_002809DB:
    if ((*(uint32_t *)(v_rip + 0xD46330)) == 0) goto loc_002801AE;
    result = KiRaiseIrqlProcessIrqlFlags(2, 2, Arg3, Arg4);
    goto loc_002801A8;
loc_00280A04:
    goto loc_002807FE;
loc_00280A0E:
    Arg2 = (1) + (0x650ULL);
    goto loc_0028025F;
loc_00280A30:
    local_rbp = (uint32_t)((0) + 1);
    if (((*(uint32_t *)(v_rip + 0xD44874)) & ((uint32_t)(local_rbp))) == 0) goto loc_00280AF9;
loc_00280A3E:
loc_00280A40:
    if (condition_is_below) goto loc_00280A30;
    goto loc_002805BC;
loc_00280A4F:
    result = MiUnlockPageTable(v_stack_p38, *(uint64_t *)(local_rsp + 0x2 * 8 + 0x70), Arg3, Arg4);
    result = MiUnlockWorkingSetShared(v_stack_p38, v_stack_p170, Arg3, Arg4);
    goto loc_002800CB;
loc_00280A8A:
    Arg1 = (*(uint64_t *)(local_rsp + 0x2 * 8 + 0x70)) - (0);
    Arg1 = (Arg1) >> (3);
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(Arg1)));
    local_rdi = ((uint32_t)((uint32_t)(Arg1))) >> (5);
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) & (31));
    local_rbp = (uint32_t)((1) << ((uint8_t)((uint32_t)((uint32_t)(local_rbx)))));
    local_r15 = (uint32_t)((2) << ((uint8_t)((uint32_t)((uint32_t)(local_rbx)))));
    local_r14 = (uint32_t)(~((uint32_t)((uint32_t)(local_r15))));
loc_00280AD8:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBAC086 + 0x266C + local_rdi * 4))))) >> ((uint8_t)((uint32_t)((uint32_t)(local_rbx)))));
    if ((((uint8_t)(result)) & (1)) != 0) goto loc_00280B37;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBAC086 + 0x266C + local_rdi * 4))))) | ((uint32_t)(local_rbp)));
    Arg1 = (uint32_t)((Arg1) & ((uint32_t)(local_r14)));
    if (condition_is_equal) goto loc_002805FB;
    goto loc_00280AD8;
loc_00280AF9:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD45FB9)))) & (64)) == 0) goto loc_00280A3E;
    result = KiCheckVpBackingLongSpinWaitHypercall(Arg1, (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBAC086 + 0x266C + local_rdi * 4)))))), Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00280A3E;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rbp)), (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBAC086 + 0x266C + local_rdi * 4)))))), Arg3, Arg4);
    goto loc_00280A40;
loc_00280B20:
    goto loc_00280711;
loc_00280B2A:
    result = KxWaitForLockOwnerShip(24, result, Arg3, Arg4);
    goto loc_00280982;
loc_00280B37:
    if ((((uint8_t)(result)) & (2)) != 0) goto loc_00280C13;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(result))) | ((uint32_t)(local_r15)));
    Arg2 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
    if (condition_is_equal) { Arg2 = (uint32_t)(Arg1); }
    goto loc_00280AD8;
loc_00280B51:
    result = MiLockWorkingSetExclusive(local_r15, Arg2, Arg3, Arg4);
    goto loc_002801A8;
loc_00280B5E:
    goto loc_00280119;
loc_00280B6A:
    v_stack_p20 = 0;
    Arg4 = 0;
    result = KeBugCheckEx(Arg4 + 16, local_r15, 256, Arg4);
loc_00280B85:
    result = (uint8_t)(((uint8_t)(v_rip + 12238982 + 9836 + local_rdi * 4)) & (33));
    if (((uint8_t)(result)) != 1) goto loc_002809C7;
    result = (0) + (Arg4 + 16);
    if ((*(uint64_t *)(local_rsp + 0x2 * 8 + 0x70)) < result) goto loc_002809C7;
    result = MiCheckLinearProtectedPteAccessedBit(*(uint64_t *)(local_rsp + 0x2 * 8 + 0x70), v_rip + 12238982 + 9836 + local_rdi * 4, 128, Arg4);
    goto loc_002809C7;
loc_00280BC2:
    result = (uint32_t)(((uint32_t)((uint32_t)(*(uint64_t *)(local_rsp + 0x2 * 8 + 0x70)))) >> (3));
    result = (uint32_t)((result) & (511));
    result = ExAcquireSpinLockExclusiveAtDpcLevel(*(uint64_t *)(local_rsp + 0x2 * 8 + 0x70) + result * 4, v_rip + 12238982 + 9836 + local_rdi * 4, 128, Arg4);
    goto loc_00280614;
loc_00280BDA:
    v_stack_p60 = 0;
    goto loc_0027FFFB;
loc_00280BEB:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC8D267))) != 0) goto loc_002806E4;
    result = ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented(*(uint64_t *)(local_rsp + 0x2 * 8 + 0x70) + result * 4, v_stack_p158, 128, Arg4);
    v_stack_p58 = *(uint64_t *)(local_rsp + 0x2 * 8 + 0x70);
    goto loc_0028037E;
loc_00280C13:
    local_r12 = (uint32_t)((0) + 1);
    if (((*(uint32_t *)(v_rip + 0xD4468F)) & ((uint32_t)(local_r12))) == 0) goto loc_00280C86;
loc_00280C1F:
loc_00280C21:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBAC086 + 0x266C + local_rdi * 4))))) >> ((uint8_t)((uint32_t)((uint32_t)(local_rbx)))));
    if ((((uint8_t)(result)) & (1)) != 0) goto loc_00280C13;
    goto loc_00280AD8;
loc_00280C32:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC8D220))) != 0) goto loc_002808A7;
    result = ExpReleaseSpinLockSharedFromDpcLevelInstrumented((uint32_t)((uint32_t)(local_rbx)), v_stack_p158, 128, Arg4);
    v_stack_p58 = *(uint64_t *)(local_rsp + 0x2 * 8 + 0x70);
    goto loc_0028037E;
loc_00280C5A:
    if ((uint32_t)(local_r14) != 0) goto loc_002800E8;
    result = MiFlushAllFilesystemPages(local_r14 + 1, v_stack_p158, 128, Arg4);
    v_stack_p20 = v_rip + 12238982 + 9836 + local_rdi * 4;
    result = KeBugCheckEx(local_r14 + 1 + 121, local_r14 + 1, *(uint64_t *)(local_rsp + 0x2 * 8 + 0x70), v_stack_p60);
loc_00280C86:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD45E2C)))) & (64)) == 0) goto loc_00280C1F;
    result = KiCheckVpBackingLongSpinWaitHypercall(local_r14 + 1 + 121, local_r14 + 1, *(uint64_t *)(local_rsp + 0x2 * 8 + 0x70), v_stack_p60);
    if ((uint8_t)(result) == 0) goto loc_00280C1F;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_r12)), local_r14 + 1, *(uint64_t *)(local_rsp + 0x2 * 8 + 0x70), v_stack_p60);
    goto loc_00280C21;
loc_00280CA6:
    result = ExAcquireSpinLockExclusiveAtDpcLevel(v_rip + 12281875, local_r14 + 1, *(uint64_t *)(local_rsp + 0x2 * 8 + 0x70), v_stack_p60);
    Arg4 = 0;
    goto loc_00280331;
loc_00280CCD:
    if ((v_rip + 12238982 + 9836 + local_rdi * 4) > result) goto loc_00280347;
loc_00280CE8:
    result = ExReleaseSpinLockExclusiveFromDpcLevel(v_rip + 12281809, local_r14 + 1, *(uint64_t *)(local_rsp + 0x2 * 8 + 0x70), Arg4);
    Arg4 = 0;
    goto loc_0028036F;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0027FF70&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
