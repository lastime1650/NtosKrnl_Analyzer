# MiReleasePageFileInfo

- RVA: `0x00283FD0`–`0x002845D3` (길이 `1,539` bytes)
- VA: `0x0000000140283FD0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00066918`
- 디코드: `378`개 명령, `1,539/1,539` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **17**; 고유 호출 대상: **14**
- 직접 호출자로 확인된 함수: **62**
- RIP 상대 이미지 참조: **12**

### Outgoing calls
- `0x0028406B` → [ExpWaitForSpinLockExclusiveAndAcquire](../32/ExpWaitForSpinLockExclusiveAndAcquire_function_003239A0.md) (function, `0x003239A0`)
- `0x00284209` → [KeSetEvent](../33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x00284233` → [ExpAcquireSpinLockExclusiveAtDpcLevelInstrumented](../32/ExpAcquireSpinLockExclusiveAtDpcLevelInstrumented_function_00323A70.md) (function, `0x00323A70`)
- `0x0028427F` → [MiCoalescePageFileBitmapsCache](../3E/MiCoalescePageFileBitmapsCache_function_003E4540.md) (function, `0x003E4540`)
- `0x002842B2` → [ExReleaseSpinLockExclusiveFromDpcLevel](../24/ExReleaseSpinLockExclusiveFromDpcLevel_function_002497E0.md) (function, `0x002497E0`)
- `0x002842D0` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x002843EA` → [MiSwizzleInvalidPte](MiSwizzleInvalidPte_function_0028F5E0.md) (function, `0x0028F5E0`)
- `0x00284413` → [MiFlushSingleTbEntry](MiFlushSingleTbEntry_function_0028E730.md) (function, `0x0028E730`)
- `0x00284424` → [ExpInterlockedPushEntrySList](../6B/ExpInterlockedPushEntrySList_function_006BA5B0.md) (function, `0x006BA5B0`)
- `0x0028444F` → [ExAcquireSpinLockExclusive](../24/ExAcquireSpinLockExclusive_function_00248690.md) (function, `0x00248690`)
- `0x0028447C` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0028448C` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x002844F7` → [MiSwizzleInvalidPte](MiSwizzleInvalidPte_function_0028F5E0.md) (function, `0x0028F5E0`)
- `0x00284510` → [KeSetEvent](../33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x00284530` → [ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented](../2C/ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented_function_002C0F44.md) (function, `0x002C0F44`)
- `0x00284575` → [MiPageHashBugCheck](../69/MiPageHashBugCheck_function_00697AC8.md) (function, `0x00697AC8`)
- `0x002845A8` → [MiPageHashBugCheck](../69/MiPageHashBugCheck_function_00697AC8.md) (function, `0x00697AC8`)

### Direct callers
- [MiCombineInitialInstance](../22/MiCombineInitialInstance_function_0022BC0C.md) at `0x0022CA8C`
- [MiResolveProtoCombine](../22/MiResolveProtoCombine_function_0022CD00.md) at `0x0022D08D`
- [MiBuildForkPte](../22/MiBuildForkPte_function_0022E32C.md) at `0x0022F04E`
- [MiBuildForkPte](../22/MiBuildForkPte_function_0022E32C.md) at `0x0022F2A7`
- [MmSetAddressRangeModifiedEx](../23/MmSetAddressRangeModifiedEx_function_00236F20.md) at `0x00237081`
- [sub_0023E278](../23/Unknown_function_0023E278.md) at `0x0023E553`
- [MiProbeUnlockPage](../24/MiProbeUnlockPage_function_00243860.md) at `0x00243B9B`
- [MiWalkVaRange](../24/MiWalkVaRange_function_00243BF0.md) at `0x0024478A`
- [MiActOnPte](../24/MiActOnPte_function_00244C90.md) at `0x002456A8`
- [sub_00245F6B](../24/Unknown_function_00245F6B.md) at `0x00245F71`
- [sub_002467FE](../24/Unknown_function_002467FE.md) at `0x00246804`
- [MmProtectPool](../26/MmProtectPool_function_002697AC.md) at `0x00269CDF`
- [MiResolveTransitionFault](MiResolveTransitionFault_function_00282940.md) at `0x00282D36`
- [MiWsleFree](MiWsleFree_function_00284600.md) at `0x00284C8A`
- [MiWsleFree](MiWsleFree_function_00284600.md) at `0x00285253`
- [MiWsleFree](MiWsleFree_function_00284600.md) at `0x00285263`
- [MiLockPageAndSetDirty](MiLockPageAndSetDirty_function_002857A0.md) at `0x00285873`
- [MiReleasePageFileSpace](MiReleasePageFileSpace_function_00285980.md) at `0x00285A21`
- [MiTrimUnusedPageFileRegionsWorker](../2A/MiTrimUnusedPageFileRegionsWorker_function_002AA320.md) at `0x002AA659`
- [MiStealPage](../2B/MiStealPage_function_002B28D0.md) at `0x002B3E33`
- [MiStoreWriteModifiedPages](../2B/MiStoreWriteModifiedPages_function_002B46C4.md) at `0x002B4F4F`
- [MiStoreWriteModifiedPages](../2B/MiStoreWriteModifiedPages_function_002B46C4.md) at `0x002B51D2`
- [MiStoreWriteModifiedPages](../2B/MiStoreWriteModifiedPages_function_002B46C4.md) at `0x002B527A`
- [MiPfnReferenceCountIsZero](../2B/MiPfnReferenceCountIsZero_function_002B9E40.md) at `0x002B9FF2`
- [sub_002C3A7C](../2C/Unknown_function_002C3A7C.md) at `0x002C4594`
- [MiPfnShareCountIsZero](../33/MiPfnShareCountIsZero_function_00330930.md) at `0x00330C12`
- [MiCompletePrivateZeroFault](../33/MiCompletePrivateZeroFault_function_00330CC0.md) at `0x00331B2E`
- [MiAllocateWsle](../33/MiAllocateWsle_function_003332C0.md) at `0x00333F52`
- [sub_003341DB](../33/Unknown_function_003341DB.md) at `0x003342C7`
- [MiCompleteProtoPteFault](../34/MiCompleteProtoPteFault_function_00345710.md) at `0x00345FD2`
- [MiDeleteClusterPage](../34/MiDeleteClusterPage_function_00346CB0.md) at `0x00347022`
- [MiMakeFaultPfnActive](../36/MiMakeFaultPfnActive_function_00361D00.md) at `0x00361DBA`
- [MiProcessWsInSwapFault](../36/MiProcessWsInSwapFault_function_00361EFC.md) at `0x00361F6A`
- [MiWalkEntireImage](../36/MiWalkEntireImage_function_00365D70.md) at `0x0036653C`
- [MiZeroCfgSystemWideBitmapWorker](../36/MiZeroCfgSystemWideBitmapWorker_function_00367060.md) at `0x003672F0`
- [MiInPageSingleKernelStack](../36/MiInPageSingleKernelStack_function_0036A3E8.md) at `0x0036A7CD`
- [MiDecommitPrivatePageTail](../36/MiDecommitPrivatePageTail_function_0036F564.md) at `0x0036F704`
- [MiLockCode](../36/MiLockCode_function_0036F91C.md) at `0x0037013F`
- [MiDecommitSharedPageTail](../37/MiDecommitSharedPageTail_function_00370240.md) at `0x0037085A`
- [sub_00370B5B](../37/Unknown_function_00370B5B.md) at `0x00370CC7`
- [MiDeleteMergedPte](../37/MiDeleteMergedPte_function_00371040.md) at `0x003710CF`
- [MiPurgeSubsection](../37/MiPurgeSubsection_function_003712F0.md) at `0x0037195E`
- [sub_00371ECD](../37/Unknown_function_00371ECD.md) at `0x00371EEE`
- [MiOutSwapWorkingSetPte](../37/MiOutSwapWorkingSetPte_function_00372190.md) at `0x00372849`
- [MiOutSwapWorkingSetPte](../37/MiOutSwapWorkingSetPte_function_00372190.md) at `0x003728CC`
- [MiUnlockStoreLockedPages](../37/MiUnlockStoreLockedPages_function_003735C0.md) at `0x003737B1`
- [MiDeleteSectionCluster](../37/MiDeleteSectionCluster_function_00373DF0.md) at `0x0037431C`
- [MiReservePageFileSpaceForPage](../38/MiReservePageFileSpaceForPage_function_0038377C.md) at `0x00383A3F`
- [MiReservePageFileSpace](../38/MiReservePageFileSpace_function_00383ED8.md) at `0x00384392`
- [MiSetSystemCodeProtection](../38/MiSetSystemCodeProtection_function_00384420.md) at `0x00384BB4`
- [MiWriteComplete](../40/MiWriteComplete_function_004069B0.md) at `0x00406EFB`
- [MiBuildReservationCluster](../40/MiBuildReservationCluster_function_004071A0.md) at `0x0040777E`
- [MiMakeOutswappedPageResident](../43/MiMakeOutswappedPageResident_function_00431AD0.md) at `0x00431FD8`
- [sub_00438F5D](../43/Unknown_function_00438F5D.md) at `0x0043900F`
- [MiUpdateImportRelocationsOnDriverPrivatePages](../44/MiUpdateImportRelocationsOnDriverPrivatePages_function_00449BCC.md) at `0x00449E61`
- [MiCompleteSecureProcessFault](../46/MiCompleteSecureProcessFault_function_0046710C.md) at `0x004673C6`
- [MiLockPagedAddress](../48/MiLockPagedAddress_function_00484CDC.md) at `0x00484EF0`
- [MmUpdateUserShadowStackValue](../49/MmUpdateUserShadowStackValue_function_004935D8.md) at `0x004938E7`
- [MiSetPagesModified](../49/MiSetPagesModified_function_0049DC2C.md) at `0x0049E0FC`
- [MiTrimSystemImagePages](../4B/MiTrimSystemImagePages_function_004B18FC.md) at `0x004B1B6E`
- [MiFreeModifiedReservations](../4F/MiFreeModifiedReservations_function_004FA318.md) at `0x004FA42B`
- [MiLockDriverPageRange](../67/MiLockDriverPageRange_function_00670160.md) at `0x00670467`
- [MiReplaceImportEntry](../67/MiReplaceImportEntry_function_00671440.md) at `0x006716CA`
- [MmDbgMarkPfnModifiedWorker](../68/MmDbgMarkPfnModifiedWorker_function_00686298.md) at `0x00686323`
- [sub_006D715C](../6D/Unknown_function_006D715C.md) at `0x006D7196`
- [sub_006DA4DA](../6D/Unknown_function_006DA4DA.md) at `0x006DA54F`
- [MiScanPagefileSpace](../../page/80/MiScanPagefileSpace_function_00800440.md) at `0x008005F2`
- [MiFreeReservationRun](../../page/A4/MiFreeReservationRun_function_00A4AB74.md) at `0x00A4ABB4`

### Static image references
- `0x00283FE1` → RVA `0x00E2DC80` (`.data`; read)
- `0x00284049` → RVA `0x00FC6B06` (`ALMOSTRO`; read)
- `0x00284094` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x0028417D` → RVA `0x00E2DCCC` (`.data`; read)
- `0x0028418B` → RVA `0x00FC5000` (`ALMOSTRO`; read)
- `0x00284220` → RVA `0x00F0DE58` (`.data`; read)
- `0x002842C0` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x0028430B` → RVA `0x00E3738C` (`.data`; read)
- `0x0028434E` → RVA `0x00E37390` (`.data`; read)
- `0x002843F7` → RVA `0x00010880` (`.rdata`; read)
- `0x0028446E` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)
- `0x00284556` → RVA `0x00E30254` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x00284550` → [sub_006DA1EE](../6D/Unknown_function_006DA1EE.md) (`tail-transfer`)
  - `0x0028455C` → [sub_006DA1EE](../6D/Unknown_function_006DA1EE.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00283FD0  40 53                           push rbx
00283FD2  55                              push rbp
00283FD3  56                              push rsi
00283FD4  57                              push rdi
00283FD5  41 54                           push r12
00283FD7  41 55                           push r13
00283FD9  41 56                           push r14
00283FDB  41 57                           push r15
00283FDD  48 83 EC 58                     sub rsp, 0x58
00283FE1  48 8B 05 98 9C BA 00            mov rax, qword ptr [rip + 0xba9c98]
00283FE8  45 8B F8                        mov r15d, r8d
00283FEB  48 8B DA                        mov rbx, rdx
00283FEE  4C 8B E9                        mov r13, rcx
00283FF1  48 8B FA                        mov rdi, rdx
00283FF4  48 85 C0                        test rax, rax
00283FF7  74 0E                           je 0x140284007
00283FF9  F6 C3 10                        test bl, 0x10
00283FFC  75 09                           jne 0x140284007
00283FFE  48 8B F8                        mov rdi, rax
00284001  48 F7 D7                        not rdi
00284004  48 23 FA                        and rdi, rdx
00284007  48 8B F3                        mov rsi, rbx
0028400A  48 C1 EF 20                     shr rdi, 0x20
0028400E  48 C1 EE 0C                     shr rsi, 0xc
00284012  48 8B EB                        mov rbp, rbx
00284015  83 E6 0F                        and esi, 0xf
00284018  48 D1 ED                        shr rbp, 1
0028401B  48 C1 EB 02                     shr rbx, 2
0028401F  45 33 E4                        xor r12d, r12d
00284022  83 E5 01                        and ebp, 1
00284025  44 89 A4 24 A0 00 00 00         mov dword ptr [rsp + 0xa0], r12d
0028402D  83 E3 01                        and ebx, 1
00284030  48 8B B4 F1 60 48 00 00         mov rsi, qword ptr [rcx + rsi*8 + 0x4860]
00284038  4C 8D B6 C8 00 00 00            lea r14, [rsi + 0xc8]
0028403F  41 F6 C7 01                     test r15b, 1
00284043  0F 84 03 04 00 00               je 0x14028444c
00284049  F6 05 B6 2A D4 00 21            test byte ptr [rip + 0xd42ab6], 0x21
00284050  C6 84 24 B0 00 00 00 11         mov byte ptr [rsp + 0xb0], 0x11
00284058  0F 85 C2 01 00 00               jne 0x140284220
0028405E  F0 41 0F BA 2E 1F               lock bts dword ptr [r14], 0x1f
00284064  73 0D                           jae 0x140284073
00284066  B2 FF                           mov dl, 0xff
00284068  49 8B CE                        mov rcx, r14
0028406B  E8 30 F9 09 00                  call 0x1403239a0
00284070  44 8B E0                        mov r12d, eax
00284073  41 8B 0E                        mov ecx, dword ptr [r14]
00284076  8B C1                           mov eax, ecx
00284078  0F BA F0 1E                     btr eax, 0x1e
0028407C  3D 00 00 00 80                  cmp eax, 0x80000000
00284081  74 30                           je 0x1402840b3
00284083  0F BA E1 1E                     bt ecx, 0x1e
00284087  72 08                           jb 0x140284091
00284089  F0 41 81 0E 00 00 00 40         lock or dword ptr [r14], 0x40000000
00284091  41 FF C4                        inc r12d
00284094  44 85 25 11 12 D4 00            test dword ptr [rip + 0xd41211], r12d
0028409B  0F 84 CD 03 00 00               je 0x14028446e
002840A1  F3 90                           pause
002840A3  41 8B 0E                        mov ecx, dword ptr [r14]
002840A6  8B C1                           mov eax, ecx
002840A8  0F BA F0 1E                     btr eax, 0x1e
002840AC  3D 00 00 00 80                  cmp eax, 0x80000000
002840B1  75 D0                           jne 0x140284083
002840B3  44 8B A4 24 A0 00 00 00         mov r12d, dword ptr [rsp + 0xa0]
002840BB  4C 8B 76 50                     mov r14, qword ptr [rsi + 0x50]
002840BF  85 ED                           test ebp, ebp
002840C1  74 20                           je 0x1402840e3
002840C3  48 8B D7                        mov rdx, rdi
002840C6  8B C7                           mov eax, edi
002840C8  83 E0 07                        and eax, 7
002840CB  48 C1 EA 03                     shr rdx, 3
002840CF  49 03 56 20                     add rdx, qword ptr [r14 + 0x20]
002840D3  0F BE 0A                        movsx ecx, byte ptr [rdx]
002840D6  0F B3 C1                        btr ecx, eax
002840D9  88 0A                           mov byte ptr [rdx], cl
002840DB  8B 46 14                        mov eax, dword ptr [rsi + 0x14]
002840DE  FF C0                           inc eax
002840E0  89 46 14                        mov dword ptr [rsi + 0x14], eax
002840E3  85 DB                           test ebx, ebx
002840E5  0F 84 80 01 00 00               je 0x14028426b
002840EB  41 BB 01 00 00 00               mov r11d, 1
002840F1  41 F6 C7 02                     test r15b, 2
002840F5  75 18                           jne 0x14028410f
002840F7  48 8B 8E B8 00 00 00            mov rcx, qword ptr [rsi + 0xb8]
002840FE  C7 44 24 44 00 00 00 00         mov dword ptr [rsp + 0x44], 0
00284106  48 85 C9                        test rcx, rcx
00284109  0F 85 EF 01 00 00               jne 0x1402842fe
0028410F  48 8B D7                        mov rdx, rdi
00284112  44 8B C7                        mov r8d, edi
00284115  48 C1 EA 03                     shr rdx, 3
00284119  41 83 E0 07                     and r8d, 7
0028411D  F6 86 AC 00 00 00 40            test byte ptr [rsi + 0xac], 0x40
00284124  0F 84 13 01 00 00               je 0x14028423d
0028412A  48 8B 46 50                     mov rax, qword ptr [rsi + 0x50]
0028412E  4C 8B 8E D8 00 00 00            mov r9, qword ptr [rsi + 0xd8]
00284135  48 8B 48 20                     mov rcx, qword ptr [rax + 0x20]
00284139  0F BE 04 0A                     movsx eax, byte ptr [rdx + rcx]
0028413D  44 0F B3 C0                     btr eax, r8d
00284141  88 04 0A                        mov byte ptr [rdx + rcx], al
00284144  3B 7E 68                        cmp edi, dword ptr [rsi + 0x68]
00284147  73 03                           jae 0x14028414c
00284149  89 7E 68                        mov dword ptr [rsi + 0x68], edi
0028414C  8B 8E A8 00 00 00               mov ecx, dword ptr [rsi + 0xa8]
00284152  8D 41 01                        lea eax, [rcx + 1]
00284155  89 86 A8 00 00 00               mov dword ptr [rsi + 0xa8], eax
0028415B  81 F9 FF 00 00 00               cmp ecx, 0xff
00284161  0F 84 9D 03 00 00               je 0x140284504
00284167  49 8B 91 00 49 00 00            mov rdx, qword ptr [r9 + 0x4900]
0028416E  48 81 FA A0 00 00 00            cmp rdx, 0xa0
00284175  73 5D                           jae 0x1402841d4
00284177  49 8B 69 10                     mov rbp, qword ptr [r9 + 0x10]
0028417B  33 C0                           xor eax, eax
0028417D  44 8B 35 48 9B BA 00            mov r14d, dword ptr [rip + 0xba9b48]
00284184  48 81 C5 60 3A 00 00            add rbp, 0x3a60
0028418B  0F B7 3D 6E 0E D4 00            movzx edi, word ptr [rip + 0xd40e6e]
00284192  3B C7                           cmp eax, edi
00284194  0F 83 6A 03 00 00               jae 0x140284504
0028419A  45 33 DB                        xor r11d, r11d
0028419D  48 8B DD                        mov rbx, rbp
002841A0  49 83 FB 01                     cmp r11, 1
002841A4  0F 8F F8 02 00 00               jg 0x1402844a2
002841AA  4C 8B 13                        mov r10, qword ptr [rbx]
002841AD  45 33 C0                        xor r8d, r8d
002841B0  45 3B C6                        cmp r8d, r14d
002841B3  0F 83 DD 02 00 00               jae 0x140284496
002841B9  41 8B C8                        mov ecx, r8d
002841BC  48 03 C9                        add rcx, rcx
002841BF  41 0F B7 0C CA                  movzx ecx, word ptr [r10 + rcx*8]
002841C4  48 03 D1                        add rdx, rcx
002841C7  48 81 FA A0 00 00 00            cmp rdx, 0xa0
002841CE  0F 82 0A 01 00 00               jb 0x1402842de
002841D4  48 8D 8E C8 00 00 00            lea rcx, [rsi + 0xc8]
002841DB  41 F6 C7 01                     test r15b, 1
002841DF  0F 84 C5 00 00 00               je 0x1402842aa
002841E5  F6 05 1A 29 D4 00 01            test byte ptr [rip + 0xd4291a], 1
002841EC  0F 85 28 03 00 00               jne 0x14028451a
002841F2  C7 01 00 00 00 00               mov dword ptr [rcx], 0
002841F8  45 85 E4                        test r12d, r12d
002841FB  74 11                           je 0x14028420e
002841FD  49 8D 8D A0 03 00 00            lea rcx, [r13 + 0x3a0]
00284204  45 33 C0                        xor r8d, r8d
00284207  33 D2                           xor edx, edx
00284209  E8 02 B1 0B 00                  call 0x14033f310
0028420E  48 83 C4 58                     add rsp, 0x58
00284212  41 5F                           pop r15
00284214  41 5E                           pop r14
00284216  41 5D                           pop r13
00284218  41 5C                           pop r12
0028421A  5F                              pop rdi
0028421B  5E                              pop rsi
0028421C  5D                              pop rbp
0028421D  5B                              pop rbx
0028421E  C3                              ret
0028421F  CC                              int3
00284220  8B 05 32 9C C8 00               mov eax, dword ptr [rip + 0xc89c32]
00284226  85 C0                           test eax, eax
00284228  0F 85 30 FE FF FF               jne 0x14028405e
0028422E  B2 FF                           mov dl, 0xff
00284230  49 8B CE                        mov rcx, r14
00284233  E8 38 F8 09 00                  call 0x140323a70
00284238  E9 7E FE FF FF                  jmp 0x1402840bb
0028423D  49 8B 4E 10                     mov rcx, qword ptr [r14 + 0x10]
00284241  0F BE 04 11                     movsx eax, byte ptr [rcx + rdx]
00284245  44 0F B3 C0                     btr eax, r8d
00284249  88 04 11                        mov byte ptr [rcx + rdx], al
0028424C  8B 4E 0C                        mov ecx, dword ptr [rsi + 0xc]
0028424F  8D 41 01                        lea eax, [rcx + 1]
00284252  89 46 0C                        mov dword ptr [rsi + 0xc], eax
00284255  8B 46 58                        mov eax, dword ptr [rsi + 0x58]
00284258  3B F8                           cmp edi, eax
0028425A  0F 82 5B 03 00 00               jb 0x1402845bb
00284260  FF 46 60                        inc dword ptr [rsi + 0x60]
00284263  85 C9                           test ecx, ecx
00284265  0F 84 58 03 00 00               je 0x1402845c3
0028426B  85 ED                           test ebp, ebp
0028426D  74 77                           je 0x1402842e6
0028426F  85 DB                           test ebx, ebx
00284271  0F 84 BD 01 00 00               je 0x140284434
00284277  44 8B C7                        mov r8d, edi
0028427A  8B D5                           mov edx, ebp
0028427C  48 8B CE                        mov rcx, rsi
0028427F  E8 BC 02 16 00                  call 0x1403e4540
00284284  48 8B 8E D8 00 00 00            mov rcx, qword ptr [rsi + 0xd8]
0028428B  8B 81 98 03 00 00               mov eax, dword ptr [rcx + 0x398]
00284291  25 00 FE FF FF                  and eax, 0xfffffe00
00284296  0F BA E8 09                     bts eax, 9
0028429A  05 00 04 00 00                  add eax, 0x400
0028429F  87 81 98 03 00 00               xchg dword ptr [rcx + 0x398], eax
002842A5  E9 2A FF FF FF                  jmp 0x1402841d4
002842AA  0F B6 9C 24 B0 00 00 00         movzx ebx, byte ptr [rsp + 0xb0]
002842B2  E8 29 55 FC FF                  call 0x1402497e0
002842B7  80 FB 11                        cmp bl, 0x11
002842BA  0F 84 38 FF FF FF               je 0x1402841f8
002842C0  83 3D 59 2A D4 00 00            cmp dword ptr [rip + 0xd42a59], 0
002842C7  74 0C                           je 0x1402842d5
002842C9  44 0F 20 C1                     mov rcx, cr8
002842CD  0F B6 D3                        movzx edx, bl
002842D0  E8 C3 13 27 00                  call 0x1404f5698
002842D5  44 0F 22 C3                     mov cr8, rbx
002842D9  E9 1A FF FF FF                  jmp 0x1402841f8
002842DE  41 FF C0                        inc r8d
002842E1  E9 CA FE FF FF                  jmp 0x1402841b0
002842E6  49 8B 46 20                     mov rax, qword ptr [r14 + 0x20]
002842EA  48 0F A3 38                     bt qword ptr [rax], rdi
002842EE  0F 92 C0                        setb al
002842F1  84 C0                           test al, al
002842F3  0F 85 DB FE FF FF               jne 0x1402841d4
002842F9  E9 71 FF FF FF                  jmp 0x14028426f
002842FE  44 8B D7                        mov r10d, edi
00284301  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
0028430B  44 0F AF 15 79 30 BB 00         imul r10d, dword ptr [rip + 0xbb3079]
00284313  4C 03 D1                        add r10, rcx
00284316  4D 8B CA                        mov r9, r10
00284319  49 C1 E9 09                     shr r9, 9
0028431D  4C 23 C8                        and r9, rax
00284320  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
0028432A  4C 03 C8                        add r9, rax
0028432D  49 8B 01                        mov rax, qword ptr [r9]
00284330  41 84 C3                        test r11b, al
00284333  0F 84 77 01 00 00               je 0x1402844b0
00284339  33 C9                           xor ecx, ecx
0028433B  44 89 5C 24 40                  mov dword ptr [rsp + 0x40], r11d
00284340  48 89 4C 24 48                  mov qword ptr [rsp + 0x48], rcx
00284345  45 39 1A                        cmp dword ptr [r10], r11d
00284348  0F 84 3B 02 00 00               je 0x140284589
0028434E  39 0D 3C 30 BB 00               cmp dword ptr [rip + 0xbb303c], ecx
00284354  0F 85 E6 01 00 00               jne 0x140284540
0028435A  8B 54 24 44                     mov edx, dword ptr [rsp + 0x44]
0028435E  45 89 1A                        mov dword ptr [r10], r11d
00284361  83 3D 28 30 BB 00 00            cmp dword ptr [rip + 0xbb3028], 0
00284368  0F 85 40 02 00 00               jne 0x1402845ae
0028436E  48 C1 E8 0C                     shr rax, 0xc
00284372  48 B9 FF FF FF FF FF 00 00 00   movabs rcx, 0xffffffffff
0028437C  48 23 C1                        and rax, rcx
0028437F  4C 8D 1C 40                     lea r11, [rax + rax*2]
00284383  49 C1 E3 04                     shl r11, 4
00284387  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
00284391  48 8B 0D E8 98 BA 00            mov rcx, qword ptr [rip + 0xba98e8]
00284398  4C 03 D8                        add r11, rax
0028439B  4C 89 9C 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], r11
002843A3  49 8B 43 10                     mov rax, qword ptr [r11 + 0x10]
002843A7  48 8B D0                        mov rdx, rax
002843AA  48 85 C9                        test rcx, rcx
002843AD  74 0D                           je 0x1402843bc
002843AF  A8 10                           test al, 0x10
002843B1  75 09                           jne 0x1402843bc
002843B3  48 8B D1                        mov rdx, rcx
002843B6  48 F7 D2                        not rdx
002843B9  48 23 D0                        and rdx, rax
002843BC  48 C1 EA 20                     shr rdx, 0x20
002843C0  FF CA                           dec edx
002843C2  48 85 C0                        test rax, rax
002843C5  0F 84 9E 00 00 00               je 0x140284469
002843CB  48 85 C9                        test rcx, rcx
002843CE  74 0E                           je 0x1402843de
002843D0  A8 10                           test al, 0x10
002843D2  0F 85 88 00 00 00               jne 0x140284460
002843D8  48 F7 D1                        not rcx
002843DB  48 23 C1                        and rax, rcx
002843DE  44 8B C0                        mov r8d, eax
002843E1  8B CA                           mov ecx, edx
002843E3  48 C1 E1 20                     shl rcx, 0x20
002843E7  49 0B C8                        or rcx, r8
002843EA  E8 F1 B1 00 00                  call 0x14028f5e0
002843EF  49 89 43 10                     mov qword ptr [r11 + 0x10], rax
002843F3  85 D2                           test edx, edx
002843F5  75 32                           jne 0x140284429
002843F7  48 8B 05 82 C4 D8 FF            mov rax, qword ptr [rip - 0x273b7e]
002843FE  BA 02 00 00 00                  mov edx, 2
00284403  FF 8E B0 00 00 00               dec dword ptr [rsi + 0xb0]
00284409  49 8B CA                        mov rcx, r10
0028440C  49 89 01                        mov qword ptr [r9], rax
0028440F  44 8D 42 FF                     lea r8d, [rdx - 1]
00284413  E8 18 A3 00 00                  call 0x14028e730
00284418  48 8B 94 24 A0 00 00 00         mov rdx, qword ptr [rsp + 0xa0]
00284420  48 8D 4E 30                     lea rcx, [rsi + 0x30]
00284424  E8 87 61 43 00                  call 0x1406ba5b0
00284429  41 BB 01 00 00 00               mov r11d, 1
0028442F  E9 DB FC FF FF                  jmp 0x14028410f
00284434  49 8B 46 10                     mov rax, qword ptr [r14 + 0x10]
00284438  48 0F A3 38                     bt qword ptr [rax], rdi
0028443C  0F 92 C0                        setb al
0028443F  84 C0                           test al, al
00284441  0F 84 30 FE FF FF               je 0x140284277
00284447  E9 88 FD FF FF                  jmp 0x1402841d4
0028444C  49 8B CE                        mov rcx, r14
0028444F  E8 3C 42 FC FF                  call 0x140248690
00284454  88 84 24 B0 00 00 00            mov byte ptr [rsp + 0xb0], al
0028445B  E9 5B FC FF FF                  jmp 0x1402840bb
00284460  48 83 E0 EF                     and rax, 0xffffffffffffffef
00284464  E9 75 FF FF FF                  jmp 0x1402843de
00284469  E9 70 FF FF FF                  jmp 0x1402843de
0028446E  8B 05 44 26 D4 00               mov eax, dword ptr [rip + 0xd42644]
00284474  A8 40                           test al, 0x40
00284476  0F 84 25 FC FF FF               je 0x1402840a1
0028447C  E8 0F B0 08 00                  call 0x14030f490
00284481  84 C0                           test al, al
00284483  0F 84 18 FC FF FF               je 0x1402840a1
00284489  41 8B CC                        mov ecx, r12d
0028448C  E8 CF AF 08 00                  call 0x14030f460
00284491  E9 0D FC FF FF                  jmp 0x1402840a3
00284496  49 FF C3                        inc r11
00284499  48 83 C3 08                     add rbx, 8
0028449D  E9 FE FC FF FF                  jmp 0x1402841a0
002844A2  48 81 C5 80 DF 00 00            add rbp, 0xdf80
002844A9  FF C0                           inc eax
002844AB  E9 E2 FC FF FF                  jmp 0x140284192
002844B0  48 8B 15 C9 97 BA 00            mov rdx, qword ptr [rip + 0xba97c9]
002844B7  48 8B C8                        mov rcx, rax
002844BA  48 85 D2                        test rdx, rdx
002844BD  74 0D                           je 0x1402844cc
002844BF  A8 10                           test al, 0x10
002844C1  75 77                           jne 0x14028453a
002844C3  48 8B CA                        mov rcx, rdx
002844C6  48 F7 D1                        not rcx
002844C9  48 23 C8                        and rcx, rax
002844CC  48 C1 E9 20                     shr rcx, 0x20
002844D0  FF C9                           dec ecx
002844D2  48 85 C0                        test rax, rax
002844D5  0F 84 A9 00 00 00               je 0x140284584
002844DB  48 85 D2                        test rdx, rdx
002844DE  74 0E                           je 0x1402844ee
002844E0  A8 10                           test al, 0x10
002844E2  0F 85 93 00 00 00               jne 0x14028457b
002844E8  48 F7 D2                        not rdx
002844EB  48 23 C2                        and rax, rdx
002844EE  48 C1 E1 20                     shl rcx, 0x20
002844F2  8B D0                           mov edx, eax
002844F4  48 0B CA                        or rcx, rdx
002844F7  E8 E4 B0 00 00                  call 0x14028f5e0
002844FC  49 89 01                        mov qword ptr [r9], rax
002844FF  E9 0B FC FF FF                  jmp 0x14028410f
00284504  49 8D 89 30 05 00 00            lea rcx, [r9 + 0x530]
0028450B  45 33 C0                        xor r8d, r8d
0028450E  33 D2                           xor edx, edx
00284510  E8 FB AD 0B 00                  call 0x14033f310
00284515  E9 BA FC FF FF                  jmp 0x1402841d4
0028451A  8B 05 38 99 C8 00               mov eax, dword ptr [rip + 0xc89938]
00284520  85 C0                           test eax, eax
00284522  0F 85 CA FC FF FF               jne 0x1402841f2
00284528  48 8B 94 24 98 00 00 00         mov rdx, qword ptr [rsp + 0x98]
00284530  E8 0F CA 03 00                  call 0x1402c0f44
00284535  E9 BE FC FF FF                  jmp 0x1402841f8
0028453A  48 83 E1 EF                     and rcx, 0xffffffffffffffef
0028453E  EB 8C                           jmp 0x1402844cc
00284540  49 8B 52 08                     mov rdx, qword ptr [r10 + 8]
00284544  48 85 D2                        test rdx, rdx
00284547  0F 84 0D FE FF FF               je 0x14028435a
0028454D  41 84 D3                        test r11b, dl
00284550  0F 85 98 5C 45 00               jne 0x1406da1ee
00284556  39 0D F8 BC BA 00               cmp dword ptr [rip + 0xbabcf8], ecx
0028455C  0F 85 8C 5C 45 00               jne 0x1406da1ee
00284562  89 4C 24 20                     mov dword ptr [rsp + 0x20], ecx
00284566  4C 8D 4C 24 40                  lea r9, [rsp + 0x40]
0028456B  B9 61 00 00 00                  mov ecx, 0x61
00284570  4D 8B C2                        mov r8, r10
00284573  8B D7                           mov edx, edi
00284575  E8 4E 35 41 00                  call 0x140697ac8
0028457A  CC                              int3
0028457B  48 83 E0 EF                     and rax, 0xffffffffffffffef
0028457F  E9 6A FF FF FF                  jmp 0x1402844ee
00284584  E9 65 FF FF FF                  jmp 0x1402844ee
00284589  39 0D C5 BC BA 00               cmp dword ptr [rip + 0xbabcc5], ecx
0028458F  0F 85 B9 FD FF FF               jne 0x14028434e
00284595  89 4C 24 20                     mov dword ptr [rsp + 0x20], ecx
00284599  4C 8D 4C 24 40                  lea r9, [rsp + 0x40]
0028459E  B9 62 00 00 00                  mov ecx, 0x62
002845A3  4D 8B C2                        mov r8, r10
002845A6  8B D7                           mov edx, edi
002845A8  E8 1B 35 41 00                  call 0x140697ac8
002845AD  CC                              int3
002845AE  49 89 4A 08                     mov qword ptr [r10 + 8], rcx
002845B2  41 89 52 04                     mov dword ptr [r10 + 4], edx
002845B6  E9 B3 FD FF FF                  jmp 0x14028436e
002845BB  89 7E 58                        mov dword ptr [rsi + 0x58], edi
002845BE  E9 9D FC FF FF                  jmp 0x140284260
002845C3  F6 86 AE 00 00 00 01            test byte ptr [rsi + 0xae], 1
002845CA  45 0F 45 E3                     cmovne r12d, r11d
002845CE  E9 98 FC FF FF                  jmp 0x14028426b
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiReleasePageFileInfo(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m54;
    unsigned __int8 v_stack_p18;
    unsigned int v_stack_p20;
    unsigned int v_stack_p40;
    unsigned int v_stack_p44;
    unsigned __int64 v_stack_p48;
    unsigned int v_stack_p8;
    unsigned __int64 v_stack_p98;
    unsigned __int64 v_stack_pA0;
    unsigned __int8 v_stack_pB0;

    v_rsp = (v_rsp) - (88);
    if (*(unsigned __int64 *)(v_rip + 12229784) == 0) goto loc_00284007;
    v_rdi = a2;
    if ((((unsigned __int8)(a2)) & (16)) == 0) {
        v_rdi = *(unsigned __int64 *)(v_rip + 12229784);
        v_rdi = ~(v_rdi);
        v_rdi = (v_rdi) & (a2);
    }
    v_rdi = (v_rdi) >> (32);
    v_rsi = (a2) >> (12);
    v_rsi = (unsigned int)((v_rsi) & (15));
    v_rbp = (a2) >> (1);
    v_rbx = (a2) >> (2);
    v_r12 = 0;
    v_rbp = (unsigned int)((v_rbp) & (1));
    v_stack_p8 = 0;
    v_rbx = (unsigned int)((v_rbx) & (1));
    if ((((unsigned __int8)((unsigned int)(a3))) & (1)) == 0) goto loc_0028444C;
    v_stack_p18 = 17;
    if (((*(unsigned __int8 *)(v_rip + 13904566)) & (33)) != 0) goto loc_00284220;
loc_0028405E:
    result = *(unsigned __int64 *)(v_rip + 12229784);
    if (!(condition_is_above_or_equal)) {
        a2 = 255;
        a1 = *(unsigned __int64 *)(a1 + v_rsi * 8 + 18528) + 200;
        result = ExpWaitForSpinLockExclusiveAndAcquire(a1, a2, a3, a4);
        v_r12 = (unsigned int)(result);
    }
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + v_rsi * 8 + 18528) + 200)))))) == 0x80000000ULL) goto loc_002840B3;
loc_00284083:
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + v_rsi * 8 + 18528) + 200)))))) >= 0x80000000ULL) {
    }
    v_r12 = (unsigned int)((v_r12) + 1);
    if (((*(unsigned int *)(v_rip + 13898257)) & ((unsigned int)(v_r12))) == 0) goto loc_0028446E;
loc_002840A1:
loc_002840A3:
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + v_rsi * 8 + 18528) + 200)))))) != 0x80000000ULL) goto loc_00284083;
loc_002840B3:
loc_002840BB:
    result = (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + v_rsi * 8 + 18528) + 200))));
    if ((unsigned int)(v_rbp) != 0) {
        a2 = v_rdi;
        result = (unsigned int)(v_rdi);
        result = (unsigned int)((result) & (7));
        a2 = (a2) >> (3);
        a2 = (a2) + (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + v_rsi * 8 + 18528) + 80) + 32));
        a1 = (__int8)(*(unsigned __int8 *)(a2));
        *(unsigned __int8 *)(a2) = (unsigned __int8)(a1);
        result = *(unsigned int *)(*(unsigned __int64 *)(a1 + v_rsi * 8 + 18528) + 20);
        result = (unsigned int)((result) + 1);
        *(unsigned int *)(*(unsigned __int64 *)(a1 + v_rsi * 8 + 18528) + 20) = (unsigned int)(result);
    }
    if ((unsigned int)(v_rbx) == 0) goto loc_0028426B;
    if ((((unsigned __int8)((unsigned int)(a3))) & (2)) != 0) goto loc_0028410F;
    v_stack_m54 = 0;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + v_rsi * 8 + 18528) + 184) != 0) goto loc_002842FE;
loc_0028410F:
    a2 = (v_rdi) >> (3);
    a3 = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) & (7));
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + v_rsi * 8 + 18528) + 172)) & (64)) == 0) goto loc_0028423D;
    *(unsigned __int8 *)(a2 + *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + v_rsi * 8 + 18528) + 80) + 32) * 1) = (unsigned __int8)((__int8)(*(unsigned __int8 *)(a2 + *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + v_rsi * 8 + 18528) + 80) + 32) * 1)));
    if (((unsigned int)(v_rdi)) < (*(unsigned int *)(*(unsigned __int64 *)(a1 + v_rsi * 8 + 18528) + 104))) {
        *(unsigned int *)(*(unsigned __int64 *)(a1 + v_rsi * 8 + 18528) + 104) = (unsigned int)(v_rdi);
    }
    *(unsigned int *)(*(unsigned __int64 *)(a1 + v_rsi * 8 + 18528) + 168) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + v_rsi * 8 + 18528) + 168)) + 1);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + v_rsi * 8 + 18528) + 168)))) == 255) goto loc_00284504;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + v_rsi * 8 + 18528) + 216) + 18688)) >= 160) goto loc_002841D4;
    result = 0;
    v_rbp = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + v_rsi * 8 + 18528) + 216) + 16)) + (0x3A60ULL);
loc_00284192:
    if (0 >= ((unsigned int)(*(unsigned __int16 *)(v_rip + 13897326)))) goto loc_00284504;
    v_r11 = 0;
loc_002841A0:
    if (0 > 1) goto loc_002844A2;
    a3 = 0;
loc_002841B0:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12229448))))) goto loc_00284496;
    a1 = (0) + (0);
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + v_rsi * 8 + 18528) + 216) + 18688)) + (*(unsigned __int16 *)(*(unsigned __int64 *)(v_rbp) + a1 * 8));
    if (a2 < 160) goto loc_002842DE;
loc_002841D4:
    if ((((unsigned __int8)((unsigned int)(a3))) & (1)) == 0) goto loc_002842AA;
    if (((*(unsigned __int8 *)(v_rip + 13904154)) & (1)) != 0) goto loc_0028451A;
loc_002841F2:
    *(unsigned int *)(*(unsigned __int64 *)(a1 + v_rsi * 8 + 18528) + 200) = 0;
loc_002841F8:
    if ((unsigned int)((unsigned int)(v_stack_p8)) != 0) {
        a1 = a1 + 928;
        a3 = 0;
        a2 = 0;
        result = KeSetEvent(a1, a2, a3, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + v_rsi * 8 + 18528) + 216));
    }
    v_rsp = (v_rsp) + (88);
    return result;
loc_00284220:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13147186))) != 0) goto loc_0028405E;
    result = ExpAcquireSpinLockExclusiveAtDpcLevelInstrumented((unsigned int)(*(unsigned int *)(v_rip + 12229448)), 255, a3, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + v_rsi * 8 + 18528) + 216));
    goto loc_002840BB;
loc_0028423D:
    *(unsigned __int8 *)(*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(v_rip + 12229448)) + 16) + 255 * 1) = (unsigned __int8)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(v_rip + 12229448)) + 16) + 255 * 1)));
    *(unsigned int *)(*(unsigned __int64 *)(a1 + v_rsi * 8 + 18528) + 12) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + v_rsi * 8 + 18528) + 12)) + 1);
    if (((unsigned int)(*(unsigned __int16 *)(v_rip + 13897326))) < ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + v_rsi * 8 + 18528) + 88))))) goto loc_002845BB;
loc_00284260:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + v_rsi * 8 + 18528) + 12))) == 0) goto loc_002845C3;
loc_0028426B:
    if ((unsigned int)(v_rbp) == 0) goto loc_002842E6;
loc_0028426F:
    if ((unsigned int)(v_rbp) == 0) goto loc_00284434;
loc_00284277:
    result = MiCoalescePageFileBitmapsCache(*(unsigned __int64 *)(a1 + v_rsi * 8 + 18528), (unsigned int)((unsigned int)(v_rbp)), (unsigned int)((unsigned int)(*(unsigned __int16 *)(v_rip + 13897326))), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + v_rsi * 8 + 18528) + 216));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + v_rsi * 8 + 18528) + 216) + 920))) & (0xFFFFFE00ULL));
    result = (unsigned int)((result) + (0x400ULL));
    goto loc_002841D4;
loc_002842AA:
    result = ExReleaseSpinLockExclusiveFromDpcLevel(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + v_rsi * 8 + 18528) + 216), (unsigned int)((unsigned int)(v_rbp)), (unsigned int)((unsigned int)(*(unsigned __int16 *)(v_rip + 13897326))), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + v_rsi * 8 + 18528) + 216));
    if (((unsigned __int8)(v_stack_pB0)) == 17) goto loc_002841F8;
    if ((*(unsigned int *)(v_rip + 13904473)) != 0) {
        a1 = v_cr8;
        a2 = (unsigned __int8)(v_stack_pB0);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, (unsigned int)((unsigned int)(*(unsigned __int16 *)(v_rip + 13897326))), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + v_rsi * 8 + 18528) + 216));
    }
    goto loc_002841F8;
loc_002842DE:
    a3 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_rip + 13897326)))) + 1);
    goto loc_002841B0;
loc_002842E6:
    result = ((*(unsigned int *)(v_rip + 13904473)) < 0) ? 1 : 0;
    if ((unsigned __int8)(result) != 0) goto loc_002841D4;
    goto loc_0028426F;
loc_002842FE:
    v_r10 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_rip + 13897326)))) * (*(unsigned int *)(v_rip + 12267641)));
    v_r10 = (v_r10) + (a1);
    a4 = (v_r10) >> (9);
    a4 = (a4) & (result);
    a4 = (a4) + (result);
    if (((0) & ((unsigned __int8)(*(unsigned __int64 *)(a4)))) == 0) goto loc_002844B0;
    a1 = 0;
    v_stack_p40 = 0;
    v_stack_p48 = 0;
    if ((*(unsigned int *)(v_r10)) == 0) goto loc_00284589;
loc_0028434E:
    if ((*(unsigned int *)(v_rip + 12267580)) != 0) goto loc_00284540;
loc_0028435A:
    *(unsigned int *)(v_r10) = 0;
    if ((*(unsigned int *)(v_rip + 12267560)) != 0) goto loc_002845AE;
loc_0028436E:
    result = (*(unsigned __int64 *)(a4)) >> (12);
    result = (result) & (0);
    v_r11 = (result + result * 2) << (4);
    v_r11 = (v_r11) + (result);
    v_stack_pA0 = v_r11;
    if (*(unsigned __int64 *)(v_rip + 12228840) == 0) goto loc_002843BC;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_r11 + 16))) & (16)) == 0) {
        a2 = *(unsigned __int64 *)(v_rip + 12228840);
        a2 = ~(a2);
        a2 = (a2) & (*(unsigned __int64 *)(v_r11 + 16));
    }
    a2 = (a2) >> (32);
    a2 = (unsigned int)((a2) - 1);
    if (*(unsigned __int64 *)(v_r11 + 16) == 0) goto loc_00284469;
    if (*(unsigned __int64 *)(v_rip + 12228840) == 0) goto loc_002843DE;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_r11 + 16))) & (16)) != 0) goto loc_00284460;
    a1 = ~(*(unsigned __int64 *)(v_rip + 12228840));
    result = (*(unsigned __int64 *)(v_r11 + 16)) & (a1);
loc_002843DE:
    a1 = ((unsigned int)((unsigned int)(a2))) << (32);
    a1 = (a1) | ((unsigned int)((unsigned int)(result)));
    result = MiSwizzleInvalidPte(a1, a2, (unsigned int)((unsigned int)(result)), a4);
    *(unsigned __int64 *)(v_r11 + 16) = result;
    if ((unsigned int)(a2) == 0) {
        result = *(unsigned __int64 *)(v_rip - 2571134);
        a2 = 2;
        a1 = v_r10;
        *(unsigned __int64 *)(a4) = result;
        a3 = a2 - 1;
        result = MiFlushSingleTbEntry(a1, a2, a3, a4);
        a2 = v_stack_pA0;
        a1 = *(unsigned __int64 *)(a1 + v_rsi * 8 + 18528) + 48;
        result = ExpInterlockedPushEntrySList(a1, a2, a3, a4);
    }
    goto loc_0028410F;
loc_00284434:
    result = (condition_is_below) ? 1 : 0;
    if ((unsigned __int8)(result) == 0) goto loc_00284277;
    goto loc_002841D4;
loc_0028444C:
    result = ExAcquireSpinLockExclusive((unsigned int)(*(unsigned int *)(v_rip + 12229448)), a2, a3, a4);
    v_stack_pB0 = (unsigned __int8)(result);
    goto loc_002840BB;
loc_00284460:
    result = (result) & (-17);
    goto loc_002843DE;
loc_00284469:
    goto loc_002843DE;
loc_0028446E:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13903428)))) & (64)) == 0) goto loc_002840A1;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned int)(*(unsigned int *)(v_rip + 12229448)), a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_002840A1;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)((unsigned int)(v_stack_p8))), a2, a3, a4);
    goto loc_002840A3;
loc_00284496:
    v_r11 = (1) + 1;
    v_rbx = (v_stack_pB0) + (8);
    goto loc_002841A0;
loc_002844A2:
    v_rbp = (v_rbp) + (0xDF80ULL);
    result = (unsigned int)((result) + 1);
    goto loc_00284192;
loc_002844B0:
    if (*(unsigned __int64 *)(v_rip + 12228553) == 0) goto loc_002844CC;
    if ((((unsigned __int8)(result)) & (16)) != 0) goto loc_0028453A;
    a1 = ~(*(unsigned __int64 *)(v_rip + 12228553));
    a1 = (a1) & (result);
loc_002844CC:
    a1 = (a1) >> (32);
    a1 = (unsigned int)((a1) - 1);
    if (result == 0) goto loc_00284584;
    if (*(unsigned __int64 *)(v_rip + 12228553) == 0) goto loc_002844EE;
    if ((((unsigned __int8)(result)) & (16)) != 0) goto loc_0028457B;
    a2 = ~(*(unsigned __int64 *)(v_rip + 12228553));
    result = (result) & (a2);
loc_002844EE:
    a1 = (a1) << (32);
    a1 = (a1) | ((unsigned int)((unsigned int)(result)));
    result = MiSwizzleInvalidPte(a1, (unsigned int)((unsigned int)(result)), a3, a4);
    *(unsigned __int64 *)(a4) = result;
    goto loc_0028410F;
loc_00284504:
    a3 = 0;
    a2 = 0;
    result = KeSetEvent(a4 + 1328, a2, a3, a4);
    goto loc_002841D4;
loc_0028451A:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13146424))) != 0) goto loc_002841F2;
    result = ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented(a4 + 1328, v_stack_p98, a3, a4);
    goto loc_002841F8;
loc_0028453A:
    a1 = (a4 + 1328) & (-17);
    goto loc_002844CC;
loc_00284540:
    if (*(unsigned __int64 *)(v_r10 + 8) == 0) goto loc_0028435A;
    v_stack_p20 = (unsigned int)(a1);
    result = MiPageHashBugCheck(97, (unsigned int)((unsigned int)(*(unsigned __int16 *)(v_rip + 13897326))), v_r10, v_stack_p40);
loc_0028457B:
    result = (result) & (-17);
    goto loc_002844EE;
loc_00284584:
    goto loc_002844EE;
loc_00284589:
    if ((*(unsigned int *)(v_rip + 12238021)) != 97) goto loc_0028434E;
    v_stack_p20 = 97;
    result = MiPageHashBugCheck(98, (unsigned int)((unsigned int)(*(unsigned __int16 *)(v_rip + 13897326))), v_r10, v_stack_p40);
loc_002845AE:
    *(unsigned __int64 *)(v_r10 + 8) = 98;
    *(unsigned int *)(v_r10 + 4) = (unsigned int)((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_rip + 13897326))));
    goto loc_0028436E;
loc_002845BB:
    *(unsigned int *)(*(unsigned __int64 *)(a1 + v_rsi * 8 + 18528) + 88) = (unsigned int)(*(unsigned __int16 *)(v_rip + 13897326));
    goto loc_00284260;
loc_002845C3:
    v_r12 = (unsigned int)(v_stack_p8);
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + v_rsi * 8 + 18528) + 174)) & (1)) != 0) { v_r12 = (unsigned int)(v_r11); }
    goto loc_0028426B;
}
```

## 5. (Beta) C Style

```c
int64_t MiReleasePageFileInfo(void *Arg1, int64_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m54;
    uint8_t v_stack_p18;
    uint32_t v_stack_p20;
    uint32_t v_stack_p40;
    uint32_t v_stack_p44;
    uint64_t v_stack_p48;
    uint32_t v_stack_p8;
    uint64_t v_stack_p98;
    uint64_t v_stack_pA0;
    uint8_t v_stack_pB0;

    local_rsp = (local_rsp) - (88);
    if (*(uint64_t *)(v_rip + 0xBA9C98) == 0) goto loc_00284007;
    local_rdi = Arg2;
    if ((((uint8_t)(Arg2)) & (16)) == 0) {
        local_rdi = *(uint64_t *)(v_rip + 0xBA9C98);
        local_rdi = ~(local_rdi);
        local_rdi = (local_rdi) & (Arg2);
    }
    local_rdi = (local_rdi) >> (32);
    local_rsi = (Arg2) >> (12);
    local_rsi = (uint32_t)((local_rsi) & (15));
    local_rbp = (Arg2) >> (1);
    local_rbx = (Arg2) >> (2);
    local_r12 = 0;
    local_rbp = (uint32_t)((local_rbp) & (1));
    v_stack_p8 = 0;
    local_rbx = (uint32_t)((local_rbx) & (1));
    if ((((uint8_t)((uint32_t)(Arg3))) & (1)) == 0) goto loc_0028444C;
    v_stack_p18 = 17;
    if (((*(uint8_t *)(v_rip + 0xD42AB6)) & (33)) != 0) goto loc_00284220;
loc_0028405E:
    result = *(uint64_t *)(v_rip + 0xBA9C98);
    if (!(condition_is_above_or_equal)) {
        Arg2 = 255;
        Arg1 = *(uint64_t *)(arg1 + local_rsi * 8 + 0x4860) + 200;
        result = ExpWaitForSpinLockExclusiveAndAcquire(Arg1, Arg2, Arg3, a4);
        local_r12 = (uint32_t)(result);
    }
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + local_rsi * 8 + 0x4860) + 0xC8)))))) == 0x80000000ULL) goto loc_002840B3;
loc_00284083:
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + local_rsi * 8 + 0x4860) + 0xC8)))))) >= 0x80000000ULL) {
    }
    local_r12 = (uint32_t)((local_r12) + 1);
    if (((*(uint32_t *)(v_rip + 0xD41211)) & ((uint32_t)(local_r12))) == 0) goto loc_0028446E;
loc_002840A1:
loc_002840A3:
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + local_rsi * 8 + 0x4860) + 0xC8)))))) != 0x80000000ULL) goto loc_00284083;
loc_002840B3:
loc_002840BB:
    result = (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + local_rsi * 8 + 0x4860) + 0xC8))));
    if ((uint32_t)(local_rbp) != 0) {
        Arg2 = local_rdi;
        result = (uint32_t)(local_rdi);
        result = (uint32_t)((result) & (7));
        Arg2 = (Arg2) >> (3);
        Arg2 = (Arg2) + (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + local_rsi * 8 + 0x4860) + 0x50) + 0x20));
        Arg1 = (int8_t)(*(uint8_t *)(Arg2));
        *(uint8_t *)(Arg2) = (uint8_t)(Arg1);
        result = *(uint32_t *)(*(uint64_t *)(arg1 + local_rsi * 8 + 0x4860) + 0x14);
        result = (uint32_t)((result) + 1);
        *(uint32_t *)(*(uint64_t *)(arg1 + local_rsi * 8 + 0x4860) + 0x14) = (uint32_t)(result);
    }
    if ((uint32_t)(local_rbx) == 0) goto loc_0028426B;
    if ((((uint8_t)((uint32_t)(Arg3))) & (2)) != 0) goto loc_0028410F;
    v_stack_m54 = 0;
    if (*(uint64_t *)(*(uint64_t *)(arg1 + local_rsi * 8 + 0x4860) + 0xB8) != 0) goto loc_002842FE;
loc_0028410F:
    Arg2 = (local_rdi) >> (3);
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) & (7));
    if (((*(uint8_t *)(*(uint64_t *)(arg1 + local_rsi * 8 + 0x4860) + 0xAC)) & (64)) == 0) goto loc_0028423D;
    *(uint8_t *)(Arg2 + *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + local_rsi * 8 + 0x4860) + 0x50) + 0x20) * 1) = (uint8_t)((int8_t)(*(uint8_t *)(Arg2 + *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + local_rsi * 8 + 0x4860) + 0x50) + 0x20) * 1)));
    if (((uint32_t)(local_rdi)) < (*(uint32_t *)(*(uint64_t *)(arg1 + local_rsi * 8 + 0x4860) + 0x68))) {
        *(uint32_t *)(*(uint64_t *)(arg1 + local_rsi * 8 + 0x4860) + 0x68) = (uint32_t)(local_rdi);
    }
    *(uint32_t *)(*(uint64_t *)(arg1 + local_rsi * 8 + 0x4860) + 0xA8) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + local_rsi * 8 + 0x4860) + 0xA8)) + 1);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + local_rsi * 8 + 0x4860) + 0xA8)))) == 255) goto loc_00284504;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + local_rsi * 8 + 0x4860) + 0xD8) + 0x4900)) >= 160) goto loc_002841D4;
    result = 0;
    local_rbp = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + local_rsi * 8 + 0x4860) + 0xD8) + 0x10)) + (0x3A60ULL);
loc_00284192:
    if (0 >= ((uint32_t)(*(uint16_t *)(v_rip + 0xD40E6E)))) goto loc_00284504;
    local_r11 = 0;
loc_002841A0:
    if (0 > 1) goto loc_002844A2;
    Arg3 = 0;
loc_002841B0:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBA9B48))))) goto loc_00284496;
    Arg1 = (0) + (0);
    Arg2 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + local_rsi * 8 + 0x4860) + 0xD8) + 0x4900)) + (*(uint16_t *)(*(uint64_t *)(local_rbp) + arg1 * 8));
    if (Arg2 < 160) goto loc_002842DE;
loc_002841D4:
    if ((((uint8_t)((uint32_t)(Arg3))) & (1)) == 0) goto loc_002842AA;
    if (((*(uint8_t *)(v_rip + 0xD4291A)) & (1)) != 0) goto loc_0028451A;
loc_002841F2:
    *(uint32_t *)(*(uint64_t *)(arg1 + local_rsi * 8 + 0x4860) + 0xC8) = 0;
loc_002841F8:
    if ((uint32_t)((uint32_t)(v_stack_p8)) != 0) {
        Arg1 = Arg1 + 928;
        Arg3 = 0;
        Arg2 = 0;
        result = KeSetEvent(Arg1, Arg2, Arg3, *(uint64_t *)(*(uint64_t *)(arg1 + local_rsi * 8 + 0x4860) + 0xD8));
    }
    local_rsp = (local_rsp) + (88);
    return result;
loc_00284220:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC89C32))) != 0) goto loc_0028405E;
    result = ExpAcquireSpinLockExclusiveAtDpcLevelInstrumented((uint32_t)(*(uint32_t *)(v_rip + 0xBA9B48)), 255, Arg3, *(uint64_t *)(*(uint64_t *)(arg1 + local_rsi * 8 + 0x4860) + 0xD8));
    goto loc_002840BB;
loc_0028423D:
    *(uint8_t *)(*(uint64_t *)((uint32_t)(*(uint32_t *)(v_rip + 0xBA9B48)) + 0x10) + 0xFF * 1) = (uint8_t)((int8_t)(*(uint8_t *)(*(uint64_t *)((uint32_t)(*(uint32_t *)(v_rip + 0xBA9B48)) + 0x10) + 0xFF * 1)));
    *(uint32_t *)(*(uint64_t *)(arg1 + local_rsi * 8 + 0x4860) + 0xC) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + local_rsi * 8 + 0x4860) + 0xC)) + 1);
    if (((uint32_t)(*(uint16_t *)(v_rip + 0xD40E6E))) < ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + local_rsi * 8 + 0x4860) + 0x58))))) goto loc_002845BB;
loc_00284260:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + local_rsi * 8 + 0x4860) + 0xC))) == 0) goto loc_002845C3;
loc_0028426B:
    if ((uint32_t)(local_rbp) == 0) goto loc_002842E6;
loc_0028426F:
    if ((uint32_t)(local_rbp) == 0) goto loc_00284434;
loc_00284277:
    result = MiCoalescePageFileBitmapsCache(*(uint64_t *)(arg1 + local_rsi * 8 + 0x4860), (uint32_t)((uint32_t)(local_rbp)), (uint32_t)((uint32_t)(*(uint16_t *)(v_rip + 0xD40E6E))), *(uint64_t *)(*(uint64_t *)(arg1 + local_rsi * 8 + 0x4860) + 0xD8));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + local_rsi * 8 + 0x4860) + 0xD8) + 0x398))) & (0xFFFFFE00ULL));
    result = (uint32_t)((result) + (0x400ULL));
    goto loc_002841D4;
loc_002842AA:
    result = ExReleaseSpinLockExclusiveFromDpcLevel(*(uint64_t *)(*(uint64_t *)(arg1 + local_rsi * 8 + 0x4860) + 0xD8), (uint32_t)((uint32_t)(local_rbp)), (uint32_t)((uint32_t)(*(uint16_t *)(v_rip + 0xD40E6E))), *(uint64_t *)(*(uint64_t *)(arg1 + local_rsi * 8 + 0x4860) + 0xD8));
    if (((uint8_t)(v_stack_pB0)) == 17) goto loc_002841F8;
    if ((*(uint32_t *)(v_rip + 0xD42A59)) != 0) {
        Arg1 = v_cr8;
        Arg2 = (uint8_t)(v_stack_pB0);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, (uint32_t)((uint32_t)(*(uint16_t *)(v_rip + 0xD40E6E))), *(uint64_t *)(*(uint64_t *)(arg1 + local_rsi * 8 + 0x4860) + 0xD8));
    }
    goto loc_002841F8;
loc_002842DE:
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(v_rip + 0xD40E6E)))) + 1);
    goto loc_002841B0;
loc_002842E6:
    result = ((*(uint32_t *)(v_rip + 0xD42A59)) < 0) ? 1 : 0;
    if ((uint8_t)(result) != 0) goto loc_002841D4;
    goto loc_0028426F;
loc_002842FE:
    local_r10 = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(v_rip + 0xD40E6E)))) * (*(uint32_t *)(v_rip + 0xBB3079)));
    local_r10 = (local_r10) + (Arg1);
    a4 = (local_r10) >> (9);
    a4 = (a4) & (result);
    a4 = (a4) + (result);
    if (((0) & ((uint8_t)(*(uint64_t *)(a4)))) == 0) goto loc_002844B0;
    Arg1 = 0;
    v_stack_p40 = 0;
    v_stack_p48 = 0;
    if ((*(uint32_t *)(local_r10)) == 0) goto loc_00284589;
loc_0028434E:
    if ((*(uint32_t *)(v_rip + 0xBB303C)) != 0) goto loc_00284540;
loc_0028435A:
    *(uint32_t *)(local_r10) = 0;
    if ((*(uint32_t *)(v_rip + 0xBB3028)) != 0) goto loc_002845AE;
loc_0028436E:
    result = (*(uint64_t *)(a4)) >> (12);
    result = (result) & (0);
    local_r11 = (result + result * 2) << (4);
    local_r11 = (local_r11) + (result);
    v_stack_pA0 = local_r11;
    if (*(uint64_t *)(v_rip + 0xBA98E8) == 0) goto loc_002843BC;
    if ((((uint8_t)(*(uint64_t *)(local_r11 + 0x10))) & (16)) == 0) {
        Arg2 = *(uint64_t *)(v_rip + 0xBA98E8);
        Arg2 = ~(Arg2);
        Arg2 = (Arg2) & (*(uint64_t *)(local_r11 + 0x10));
    }
    Arg2 = (Arg2) >> (32);
    Arg2 = (uint32_t)((Arg2) - 1);
    if (*(uint64_t *)(local_r11 + 0x10) == 0) goto loc_00284469;
    if (*(uint64_t *)(v_rip + 0xBA98E8) == 0) goto loc_002843DE;
    if ((((uint8_t)(*(uint64_t *)(local_r11 + 0x10))) & (16)) != 0) goto loc_00284460;
    Arg1 = ~(*(uint64_t *)(v_rip + 0xBA98E8));
    result = (*(uint64_t *)(local_r11 + 0x10)) & (Arg1);
loc_002843DE:
    Arg1 = ((uint32_t)((uint32_t)(Arg2))) << (32);
    Arg1 = (Arg1) | ((uint32_t)((uint32_t)(result)));
    result = MiSwizzleInvalidPte(Arg1, Arg2, (uint32_t)((uint32_t)(result)), a4);
    *(uint64_t *)(local_r11 + 0x10) = result;
    if ((uint32_t)(Arg2) == 0) {
        result = *(uint64_t *)(v_rip - 0x273B7E);
        Arg2 = 2;
        Arg1 = local_r10;
        *(uint64_t *)(a4) = result;
        Arg3 = Arg2 - 1;
        result = MiFlushSingleTbEntry(Arg1, Arg2, Arg3, a4);
        Arg2 = v_stack_pA0;
        Arg1 = *(uint64_t *)(arg1 + local_rsi * 8 + 0x4860) + 48;
        result = ExpInterlockedPushEntrySList(Arg1, Arg2, Arg3, a4);
    }
    goto loc_0028410F;
loc_00284434:
    result = (condition_is_below) ? 1 : 0;
    if ((uint8_t)(result) == 0) goto loc_00284277;
    goto loc_002841D4;
loc_0028444C:
    result = ExAcquireSpinLockExclusive((uint32_t)(*(uint32_t *)(v_rip + 0xBA9B48)), Arg2, Arg3, a4);
    v_stack_pB0 = (uint8_t)(result);
    goto loc_002840BB;
loc_00284460:
    result = (result) & (-17);
    goto loc_002843DE;
loc_00284469:
    goto loc_002843DE;
loc_0028446E:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD42644)))) & (64)) == 0) goto loc_002840A1;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint32_t)(*(uint32_t *)(v_rip + 0xBA9B48)), Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_002840A1;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)((uint32_t)(v_stack_p8))), Arg2, Arg3, a4);
    goto loc_002840A3;
loc_00284496:
    local_r11 = (1) + 1;
    local_rbx = (v_stack_pB0) + (8);
    goto loc_002841A0;
loc_002844A2:
    local_rbp = (local_rbp) + (0xDF80ULL);
    result = (uint32_t)((result) + 1);
    goto loc_00284192;
loc_002844B0:
    if (*(uint64_t *)(v_rip + 0xBA97C9) == 0) goto loc_002844CC;
    if ((((uint8_t)(result)) & (16)) != 0) goto loc_0028453A;
    Arg1 = ~(*(uint64_t *)(v_rip + 0xBA97C9));
    Arg1 = (Arg1) & (result);
loc_002844CC:
    Arg1 = (Arg1) >> (32);
    Arg1 = (uint32_t)((Arg1) - 1);
    if (result == 0) goto loc_00284584;
    if (*(uint64_t *)(v_rip + 0xBA97C9) == 0) goto loc_002844EE;
    if ((((uint8_t)(result)) & (16)) != 0) goto loc_0028457B;
    Arg2 = ~(*(uint64_t *)(v_rip + 0xBA97C9));
    result = (result) & (Arg2);
loc_002844EE:
    Arg1 = (Arg1) << (32);
    Arg1 = (Arg1) | ((uint32_t)((uint32_t)(result)));
    result = MiSwizzleInvalidPte(Arg1, (uint32_t)((uint32_t)(result)), Arg3, a4);
    *(uint64_t *)(a4) = result;
    goto loc_0028410F;
loc_00284504:
    Arg3 = 0;
    Arg2 = 0;
    result = KeSetEvent(a4 + 1328, Arg2, Arg3, a4);
    goto loc_002841D4;
loc_0028451A:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC89938))) != 0) goto loc_002841F2;
    result = ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented(a4 + 1328, v_stack_p98, Arg3, a4);
    goto loc_002841F8;
loc_0028453A:
    Arg1 = (a4 + 1328) & (-17);
    goto loc_002844CC;
loc_00284540:
    if (*(uint64_t *)(local_r10 + 0x8) == 0) goto loc_0028435A;
    v_stack_p20 = (uint32_t)(Arg1);
    result = MiPageHashBugCheck(97, (uint32_t)((uint32_t)(*(uint16_t *)(v_rip + 0xD40E6E))), local_r10, v_stack_p40);
loc_0028457B:
    result = (result) & (-17);
    goto loc_002844EE;
loc_00284584:
    goto loc_002844EE;
loc_00284589:
    if ((*(uint32_t *)(v_rip + 0xBABCC5)) != 97) goto loc_0028434E;
    v_stack_p20 = 97;
    result = MiPageHashBugCheck(98, (uint32_t)((uint32_t)(*(uint16_t *)(v_rip + 0xD40E6E))), local_r10, v_stack_p40);
loc_002845AE:
    *(uint64_t *)(local_r10 + 0x8) = 98;
    *(uint32_t *)(local_r10 + 0x4) = (uint32_t)((uint32_t)((uint32_t)(*(uint16_t *)(v_rip + 0xD40E6E))));
    goto loc_0028436E;
loc_002845BB:
    *(uint32_t *)(*(uint64_t *)(arg1 + local_rsi * 8 + 0x4860) + 0x58) = (uint32_t)(*(uint16_t *)(v_rip + 0xD40E6E));
    goto loc_00284260;
loc_002845C3:
    local_r12 = (uint32_t)(v_stack_p8);
    if (((*(uint8_t *)(*(uint64_t *)(arg1 + local_rsi * 8 + 0x4860) + 0xAE)) & (1)) != 0) { local_r12 = (uint32_t)(local_r11); }
    goto loc_0028426B;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x3A0` | `64` | `R` |
| `Arg1` | `+ 0x4860 + rsi*8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00283FD0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
