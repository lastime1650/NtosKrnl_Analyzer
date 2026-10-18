# MiInsertPageInList

- RVA: `0x002BA000`–`0x002BAAEF` (길이 `2,799` bytes)
- VA: `0x00000001402BA000`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0006DD34`
- 디코드: `640`개 명령, `2,799/2,799` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **38**; 고유 호출 대상: **26**
- 직접 호출자로 확인된 함수: **32**
- RIP 상대 이미지 참조: **14**

### Outgoing calls
- `0x002BA084` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x002BA1B9` → [MiDetermineModifiedPageListHead](MiDetermineModifiedPageListHead_function_002BAB00.md) (function, `0x002BAB00`)
- `0x002BA1D0` → [MiLockPageListAndLastPage](../41/MiLockPageListAndLastPage_function_00411BA0.md) (function, `0x00411BA0`)
- `0x002BA439` → [MiUpdateLargePageCandidateValue](../33/MiUpdateLargePageCandidateValue_function_0033EF80.md) (function, `0x0033EF80`)
- `0x002BA45B` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x002BA491` → [MiInsertDecayClusterTimer](MiInsertDecayClusterTimer_function_002BADF4.md) (function, `0x002BADF4`)
- `0x002BA4C7` → [MiGetPfnPriority](../32/MiGetPfnPriority_function_003226F0.md) (function, `0x003226F0`)
- `0x002BA593` → [MiSynchronizeFastPageInsert](MiSynchronizeFastPageInsert_function_002BAE80.md) (function, `0x002BAE80`)
- `0x002BA5BA` → [MiRebuildStandbyLookasideList](../3D/MiRebuildStandbyLookasideList_function_003D50E0.md) (function, `0x003D50E0`)
- `0x002BA5EF` → [MiInsertSecondaryListStandbyPage](../33/MiInsertSecondaryListStandbyPage_function_0033BEE0.md) (function, `0x0033BEE0`)
- `0x002BA6A8` → [ExAcquireSpinLockExclusiveAtDpcLevel](../24/ExAcquireSpinLockExclusiveAtDpcLevel_function_00248E80.md) (function, `0x00248E80`)
- `0x002BA6B1` → [ExAcquireSpinLockExclusiveAtDpcLevel](../24/ExAcquireSpinLockExclusiveAtDpcLevel_function_00248E80.md) (function, `0x00248E80`)
- `0x002BA6C5` → [ExReleaseSpinLockExclusiveFromDpcLevel](../24/ExReleaseSpinLockExclusiveFromDpcLevel_function_002497E0.md) (function, `0x002497E0`)
- `0x002BA6CF` → [ExReleaseSpinLockExclusiveFromDpcLevel](../24/ExReleaseSpinLockExclusiveFromDpcLevel_function_002497E0.md) (function, `0x002497E0`)
- `0x002BA6E6` → [MiLockPageListAndLastPage](../41/MiLockPageListAndLastPage_function_00411BA0.md) (function, `0x00411BA0`)
- `0x002BA729` → [MI_NODE_FROM_PFN](MI_NODE_FROM_PFN_function_002B0F30.md) (function, `0x002B0F30`)
- `0x002BA755` → [MiGetSlabRepurposedStandbyListWorker](../2A/MiGetSlabRepurposedStandbyListWorker_function_002AF534.md) (function, `0x002AF534`)
- `0x002BA76C` → [MiRestoreTransitionPte](../33/MiRestoreTransitionPte_function_0033DD90.md) (function, `0x0033DD90`)
- `0x002BA779` → [MiInsertPageInFreeOrZeroedList](../33/MiInsertPageInFreeOrZeroedList_function_00334D20.md) (function, `0x00334D20`)
- `0x002BA7F3` → [MiInsertSecondaryListStandbyPage](../33/MiInsertSecondaryListStandbyPage_function_0033BEE0.md) (function, `0x0033BEE0`)
- `0x002BA81A` → [MiLockPageListAndLastPage](../41/MiLockPageListAndLastPage_function_00411BA0.md) (function, `0x00411BA0`)
- `0x002BA88B` → [ExReleaseSpinLockExclusiveFromDpcLevel](../24/ExReleaseSpinLockExclusiveFromDpcLevel_function_002497E0.md) (function, `0x002497E0`)
- `0x002BA8A1` → [KeSetEvent](../33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x002BA8B9` → [MiRestoreTransitionPte](../33/MiRestoreTransitionPte_function_0033DD90.md) (function, `0x0033DD90`)
- `0x002BA8E6` → [ExpReleaseSpinLockSharedFromDpcLevelInstrumented](../2F/ExpReleaseSpinLockSharedFromDpcLevelInstrumented_function_002F0F48.md) (function, `0x002F0F48`)
- `0x002BA90A` → [MiWakeModifiedPageWriter](../3B/MiWakeModifiedPageWriter_function_003BCB18.md) (function, `0x003BCB18`)
- `0x002BA92F` → [KeSetEvent](../33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x002BA979` → [MiWakeFileOnlyReaper](../4D/MiWakeFileOnlyReaper_function_004D1D00.md) (function, `0x004D1D00`)
- `0x002BA9B1` → [MiSlabDemotionLowMemoryConditionUpdate](../3B/MiSlabDemotionLowMemoryConditionUpdate_function_003BB7E0.md) (function, `0x003BB7E0`)
- `0x002BA9C1` → [MiGetEnclavePageList](../4A/MiGetEnclavePageList_function_004AEE58.md) (function, `0x004AEE58`)
- `0x002BA9FF` → [ExAcquireSpinLockExclusiveAtDpcLevel](../24/ExAcquireSpinLockExclusiveAtDpcLevel_function_00248E80.md) (function, `0x00248E80`)
- `0x002BAA10` → [KeSetEvent](../33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x002BAA22` → [ExReleaseSpinLockExclusiveFromDpcLevel](../24/ExReleaseSpinLockExclusiveFromDpcLevel_function_002497E0.md) (function, `0x002497E0`)
- `0x002BAA33` → [MiUpdateAvailableEventsAtDpc](../3B/MiUpdateAvailableEventsAtDpc_function_003BC804.md) (function, `0x003BC804`)
- `0x002BAA69` → [MiSetPfnModified](../36/MiSetPfnModified_function_00362960.md) (function, `0x00362960`)
- `0x002BAAC6` → [MiSetPfnRemovalRequested](../67/MiSetPfnRemovalRequested_function_0067A4D0.md) (function, `0x0067A4D0`)
- `0x002BAAD5` → [ExReleaseSpinLockExclusiveFromDpcLevel](../24/ExReleaseSpinLockExclusiveFromDpcLevel_function_002497E0.md) (function, `0x002497E0`)
- `0x002BAAE5` → [MiBadPageInserted](../4D/MiBadPageInserted_function_004DD9A0.md) (function, `0x004DD9A0`)

### Direct callers
- [MiActOnPte](../24/MiActOnPte_function_00244C90.md) at `0x002457AB`
- [MiActOnPte](../24/MiActOnPte_function_00244C90.md) at `0x0024580C`
- [sub_00245BBB](../24/Unknown_function_00245BBB.md) at `0x00245CB4`
- [sub_00245D8C](../24/Unknown_function_00245D8C.md) at `0x00245D91`
- [sub_002463DF](../24/Unknown_function_002463DF.md) at `0x002464FE`
- [sub_002465D3](../24/Unknown_function_002465D3.md) at `0x002465D8`
- [MiWsleFree](../28/MiWsleFree_function_00284600.md) at `0x00284FE8`
- [MiWsleFree](../28/MiWsleFree_function_00284600.md) at `0x0028503F`
- [MiWsleFree](../28/MiWsleFree_function_00284600.md) at `0x0028509C`
- [MiWsleFree](../28/MiWsleFree_function_00284600.md) at `0x002850CB`
- [MiReplaceTransitionPage](MiReplaceTransitionPage_function_002B1120.md) at `0x002B1B1E`
- [MiCreateDecayPfn](MiCreateDecayPfn_function_002B8764.md) at `0x002B89E0`
- [MiRelinkStandbyPage](MiRelinkStandbyPage_function_002B9D30.md) at `0x002B9D81`
- [MiPfnReferenceCountIsZero](MiPfnReferenceCountIsZero_function_002B9E40.md) at `0x002B9EDB`
- [MiPfnShareCountIsZero](../33/MiPfnShareCountIsZero_function_00330930.md) at `0x00330B97`
- [MiCompletePrivateZeroFault](../33/MiCompletePrivateZeroFault_function_00330CC0.md) at `0x00331802`
- [MiCompletePrivateZeroFault](../33/MiCompletePrivateZeroFault_function_00330CC0.md) at `0x00331A36`
- [sub_003341DB](../33/Unknown_function_003341DB.md) at `0x0033424F`
- [MiRemoveLowestPriorityStandbyPage](../33/MiRemoveLowestPriorityStandbyPage_function_00334600.md) at `0x003349FC`
- [sub_00336291](../33/Unknown_function_00336291.md) at `0x003362F0`
- [MiZeroCfgSystemWideBitmapWorker](../36/MiZeroCfgSystemWideBitmapWorker_function_00367060.md) at `0x003675E4`
- [sub_00370B5B](../37/Unknown_function_00370B5B.md) at `0x00370BDA`
- [MiOutSwapWorkingSetPte](../37/MiOutSwapWorkingSetPte_function_00372190.md) at `0x00372567`
- [MiReservePageFileSpaceForPage](../38/MiReservePageFileSpaceForPage_function_0038377C.md) at `0x00383B5E`
- [MiGatherMappedPages](../40/MiGatherMappedPages_function_00404E80.md) at `0x0040530D`
- [MiBuildReservationCluster](../40/MiBuildReservationCluster_function_004071A0.md) at `0x00407765`
- [MiHandleSpecialPurposeMemoryCachedFault](../44/MiHandleSpecialPurposeMemoryCachedFault_function_0044C740.md) at `0x0044CA4C`
- [MiRelinkTransitionSlabPages](../44/MiRelinkTransitionSlabPages_function_0044D060.md) at `0x0044D0DF`
- [MiFreeModifiedReservations](../4F/MiFreeModifiedReservations_function_004FA318.md) at `0x004FA409`
- [MiReturnBadPagesToBadList](../67/MiReturnBadPagesToBadList_function_0067A374.md) at `0x0067A42F`
- [MmMarkPhysicalMemoryAsBad](../67/MmMarkPhysicalMemoryAsBad_function_0067AA50.md) at `0x0067AEAE`
- [MiMarkFileOnlyPfnBad](../68/MiMarkFileOnlyPfnBad_function_006815C4.md) at `0x0068170A`
- [MiRepointPteAtExtendedStandby](../68/MiRepointPteAtExtendedStandby_function_0068B6F4.md) at `0x0068B7E3`
- [MiMoveBadPagePartition](../69/MiMoveBadPagePartition_function_00691924.md) at `0x006919C2`
- [MiMoveModifiedPagesToCompressList](../69/MiMoveModifiedPagesToCompressList_function_006925D8.md) at `0x0069265F`
- [sub_006D715C](../6D/Unknown_function_006D715C.md) at `0x006D717A`
- [sub_006E1F48](../6E/Unknown_function_006E1F48.md) at `0x006E1F93`

### Static image references
- `0x002BA01A` → RVA `0x00E0A740` (`.data`; read)
- `0x002BA063` → RVA `0x00E30088` (`.data`; read)
- `0x002BA0A0` → RVA `0x00E35C00` (`.data`; read)
- `0x002BA0BB` → RVA `0x00E3CBE6` (`.data`; read)
- `0x002BA0C4` → RVA `0x00E3D240` (`.data`; read)
- `0x002BA136` → RVA `0x00FCF080` (`CACHEALI`; read)
- `0x002BA213` → RVA `0x00E2DCCC` (`.data`; read)
- `0x002BA21D` → RVA `0x00FC5000` (`ALMOSTRO`; read)
- `0x002BA339` → RVA `0x00E2D650` (`.data`; read)
- `0x002BA3F7` → RVA `0x00FC6B06` (`ALMOSTRO`; read)
- `0x002BA4AE` → RVA `0x00FC5200` (`ALMOSTRO`; read)
- `0x002BA65B` → RVA `0x00E2DC80` (`.data`; read)
- `0x002BA8CC` → RVA `0x00F0DE58` (`.data`; read)
- `0x002BAA4D` → RVA `0x00E2DC40` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **6**
  - `0x002BA4B6` → [sub_006DBBC0 + 0x2B](../6D/Unknown_function_006DBBC0.md) (`tail-transfer`)
  - `0x002BAA88` → [sub_006DBBC0](../6D/Unknown_function_006DBBC0.md) (`tail-transfer`)
  - `0x002BAA96` → [sub_006DBBC0](../6D/Unknown_function_006DBBC0.md) (`tail-transfer`)
  - `0x002BAAA5` → [sub_006DBBC0 + 0xC6](../6D/Unknown_function_006DBBC0.md) (`tail-transfer`)
  - `0x002BAAB4` → [sub_006DBBC0 + 0xBF](../6D/Unknown_function_006DBBC0.md) (`tail-transfer`)
  - `0x002BAACC` → [sub_006DBBC0 + 0xBF](../6D/Unknown_function_006DBBC0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002BA000  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
002BA005  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
002BA00A  57                              push rdi
002BA00B  41 54                           push r12
002BA00D  41 55                           push r13
002BA00F  41 56                           push r14
002BA011  41 57                           push r15
002BA013  48 81 EC E0 00 00 00            sub rsp, 0xe0
002BA01A  48 8B 05 1F 07 B5 00            mov rax, qword ptr [rip + 0xb5071f]
002BA021  48 33 C4                        xor rax, rsp
002BA024  48 89 84 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], rax
002BA02C  8B FA                           mov edi, edx
002BA02E  89 54 24 38                     mov dword ptr [rsp + 0x38], edx
002BA032  4C 8B F1                        mov r14, rcx
002BA035  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
002BA03F  48 8B C0                        mov rax, rax
002BA042  4C 8B E1                        mov r12, rcx
002BA045  4C 2B E0                        sub r12, rax
002BA048  48 B8 AB AA AA AA AA AA AA AA   movabs rax, 0xaaaaaaaaaaaaaaab
002BA052  49 C1 FC 04                     sar r12, 4
002BA056  4C 0F AF E0                     imul r12, rax
002BA05A  49 8B 46 28                     mov rax, qword ptr [r14 + 0x28]
002BA05E  BE 01 00 00 00                  mov esi, 1
002BA063  48 8B 0D 1E 60 B7 00            mov rcx, qword ptr [rip + 0xb7601e]
002BA06A  33 D2                           xor edx, edx
002BA06C  48 C1 E8 2B                     shr rax, 0x2b
002BA070  33 DB                           xor ebx, ebx
002BA072  25 FF 03 00 00                  and eax, 0x3ff
002BA077  44 8D 46 67                     lea r8d, [rsi + 0x67]
002BA07B  4C 8B 2C C1                     mov r13, qword ptr [rcx + rax*8]
002BA07F  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
002BA084  E8 B7 CB 40 00                  call 0x1406c6c40
002BA089  49 0F BA 66 28 35               bt qword ptr [r14 + 0x28], 0x35
002BA08F  41 BF 09 00 00 00               mov r15d, 9
002BA095  44 89 7C 24 34                  mov dword ptr [rsp + 0x34], r15d
002BA09A  0F 82 E7 03 00 00               jb 0x1402ba487
002BA0A0  48 8B 05 59 BB B7 00            mov rax, qword ptr [rip + 0xb7bb59]
002BA0A7  4C 3B E0                        cmp r12, rax
002BA0AA  72 0F                           jb 0x1402ba0bb
002BA0AC  48 05 00 08 00 00               add rax, 0x800
002BA0B2  4C 3B E0                        cmp r12, rax
002BA0B5  0F 82 EF 06 00 00               jb 0x1402ba7aa
002BA0BB  80 3D 24 2B B8 00 00            cmp byte ptr [rip + 0xb82b24], 0
002BA0C2  74 1A                           je 0x1402ba0de
002BA0C4  48 8B 05 75 31 B8 00            mov rax, qword ptr [rip + 0xb83175]
002BA0CB  49 8B CC                        mov rcx, r12
002BA0CE  48 C1 E9 09                     shr rcx, 9
002BA0D2  0F B6 14 48                     movzx edx, byte ptr [rax + rcx*2]
002BA0D6  85 D2                           test edx, edx
002BA0D8  0F 85 46 07 00 00               jne 0x1402ba824
002BA0DE  44 89 7C 24 34                  mov dword ptr [rsp + 0x34], r15d
002BA0E3  40 F6 C7 08                     test dil, 8
002BA0E7  0F 85 57 09 00 00               jne 0x1402baa44
002BA0ED  40 F6 C7 04                     test dil, 4
002BA0F1  75 13                           jne 0x1402ba106
002BA0F3  40 F6 C7 08                     test dil, 8
002BA0F7  0F 84 F3 05 00 00               je 0x1402ba6f0
002BA0FD  4D 8D BD C0 4B 00 00            lea r15, [r13 + 0x4bc0]
002BA104  EB 07                           jmp 0x1402ba10d
002BA106  4D 8D BD 40 0C 00 00            lea r15, [r13 + 0xc40]
002BA10D  8B F3                           mov esi, ebx
002BA10F  83 E6 01                        and esi, 1
002BA112  0F 85 67 09 00 00               jne 0x1402baa7f
002BA118  41 8B 7F 0C                     mov edi, dword ptr [r15 + 0xc]
002BA11C  89 7C 24 30                     mov dword ptr [rsp + 0x30], edi
002BA120  4C 89 7C 24 40                  mov qword ptr [rsp + 0x40], r15
002BA125  48 C7 44 24 48 00 00 00 00      mov qword ptr [rsp + 0x48], 0
002BA12E  85 F6                           test esi, esi
002BA130  75 2C                           jne 0x1402ba15e
002BA132  F0 09 34 24                     lock or dword ptr [rsp], esi
002BA136  8B 15 44 4F D1 00               mov edx, dword ptr [rip + 0xd14f44]
002BA13C  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
002BA140  48 C1 E2 3B                     shl rdx, 0x3b
002BA144  48 8B CA                        mov rcx, rdx
002BA147  48 33 C8                        xor rcx, rax
002BA14A  48 B8 FF FF FF FF FF FF FF C7   movabs rax, 0xc7ffffffffffffff
002BA154  48 23 C8                        and rcx, rax
002BA157  48 33 CA                        xor rcx, rdx
002BA15A  49 89 4E 18                     mov qword ptr [r14 + 0x18], rcx
002BA15E  83 FF 02                        cmp edi, 2
002BA161  0F 84 34 03 00 00               je 0x1402ba49b
002BA167  83 FF 03                        cmp edi, 3
002BA16A  0F 85 E2 04 00 00               jne 0x1402ba652
002BA170  49 8B 46 28                     mov rax, qword ptr [r14 + 0x28]
002BA174  48 85 C0                        test rax, rax
002BA177  0F 89 C8 04 00 00               jns 0x1402ba645
002BA17D  F0 49 FF 85 40 1C 00 00         lock inc qword ptr [r13 + 0x1c40]
002BA185  F0 49 FF 85 C0 4B 00 00         lock inc qword ptr [r13 + 0x4bc0]
002BA18D  8B 4C 24 38                     mov ecx, dword ptr [rsp + 0x38]
002BA191  41 8B 46 10                     mov eax, dword ptr [r14 + 0x10]
002BA195  81 E1 80 00 00 00               and ecx, 0x80
002BA19B  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
002BA19F  48 0F BA E0 0A                  bt rax, 0xa
002BA1A4  0F 82 53 04 00 00               jb 0x1402ba5fd
002BA1AA  45 33 C0                        xor r8d, r8d
002BA1AD  49 8B D5                        mov rdx, r13
002BA1B0  85 C9                           test ecx, ecx
002BA1B2  49 8B CE                        mov rcx, r14
002BA1B5  41 0F 94 C0                     sete r8b
002BA1B9  E8 42 09 00 00                  call 0x1402bab00
002BA1BE  83 7C 24 30 00                  cmp dword ptr [rsp + 0x30], 0
002BA1C3  4C 8B F8                        mov r15, rax
002BA1C6  75 0D                           jne 0x1402ba1d5
002BA1C8  48 8D 54 24 60                  lea rdx, [rsp + 0x60]
002BA1CD  48 8B C8                        mov rcx, rax
002BA1D0  E8 CB 79 15 00                  call 0x140411ba0
002BA1D5  49 8B 07                        mov rax, qword ptr [r15]
002BA1D8  48 85 C0                        test rax, rax
002BA1DB  0F 84 4C 06 00 00               je 0x1402ba82d
002BA1E1  4D 8D 85 A0 4C 00 00            lea r8, [r13 + 0x4ca0]
002BA1E8  F0 49 FF 00                     lock inc qword ptr [r8]
002BA1EC  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
002BA1F5  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
002BA1FC  F0 FF 81 50 05 00 00            lock inc dword ptr [rcx + 0x550]
002BA203  49 8B 95 00 49 00 00            mov rdx, qword ptr [r13 + 0x4900]
002BA20A  48 81 FA 20 04 00 00            cmp rdx, 0x420
002BA211  73 70                           jae 0x1402ba283
002BA213  8B 05 B3 3A B7 00               mov eax, dword ptr [rip + 0xb73ab3]
002BA219  49 8B 4D 10                     mov rcx, qword ptr [r13 + 0x10]
002BA21D  44 0F B7 0D DB AD D0 00         movzx r9d, word ptr [rip + 0xd0addb]
002BA225  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
002BA229  33 C0                           xor eax, eax
002BA22B  48 81 C1 60 3A 00 00            add rcx, 0x3a60
002BA232  44 89 4C 24 40                  mov dword ptr [rsp + 0x40], r9d
002BA237  48 89 4C 24 48                  mov qword ptr [rsp + 0x48], rcx
002BA23C  41 3B C1                        cmp eax, r9d
002BA23F  0F 83 B2 06 00 00               jae 0x1402ba8f7
002BA245  45 33 C9                        xor r9d, r9d
002BA248  48 8B F1                        mov rsi, rcx
002BA24B  8B 4C 24 30                     mov ecx, dword ptr [rsp + 0x30]
002BA24F  45 8B D9                        mov r11d, r9d
002BA252  49 83 FB 01                     cmp r11, 1
002BA256  0F 8F 06 06 00 00               jg 0x1402ba862
002BA25C  4C 8B 16                        mov r10, qword ptr [rsi]
002BA25F  44 3B C9                        cmp r9d, ecx
002BA262  0F 83 EB 05 00 00               jae 0x1402ba853
002BA268  41 8B C9                        mov ecx, r9d
002BA26B  48 03 C9                        add rcx, rcx
002BA26E  41 0F B7 0C CA                  movzx ecx, word ptr [r10 + rcx*8]
002BA273  48 03 D1                        add rdx, rcx
002BA276  48 81 FA 20 04 00 00            cmp rdx, 0x420
002BA27D  0F 82 B6 03 00 00               jb 0x1402ba639
002BA283  48 C7 44 24 48 00 00 00 00      mov qword ptr [rsp + 0x48], 0
002BA28C  4C 89 7C 24 40                  mov qword ptr [rsp + 0x40], r15
002BA291  8B F3                           mov esi, ebx
002BA293  83 E6 04                        and esi, 4
002BA296  0F 85 F2 01 00 00               jne 0x1402ba48e
002BA29C  83 7C 24 34 09                  cmp dword ptr [rsp + 0x34], 9
002BA2A1  0F 85 0D 05 00 00               jne 0x1402ba7b4
002BA2A7  F0 49 FF 07                     lock inc qword ptr [r15]
002BA2AB  80 7C 24 60 00                  cmp byte ptr [rsp + 0x60], 0
002BA2B0  49 BB FF FF FF FF 3F 00 00 00   movabs r11, 0x3fffffffff
002BA2BA  0F 84 C3 04 00 00               je 0x1402ba783
002BA2C0  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
002BA2C5  48 8B 54 24 70                  mov rdx, qword ptr [rsp + 0x70]
002BA2CA  4C 8B 84 24 80 00 00 00         mov r8, qword ptr [rsp + 0x80]
002BA2D2  4C 8B 8C 24 88 00 00 00         mov r9, qword ptr [rsp + 0x88]
002BA2DA  49 BA 00 00 00 00 00 FF FF FF   movabs r10, 0xffffff0000000000
002BA2E4  49 3B CB                        cmp rcx, r11
002BA2E7  0F 84 14 05 00 00               je 0x1402ba801
002BA2ED  48 8B 02                        mov rax, qword ptr [rdx]
002BA2F0  49 33 C4                        xor rax, r12
002BA2F3  49 23 C2                        and rax, r10
002BA2F6  49 33 C4                        xor rax, r12
002BA2F9  48 89 02                        mov qword ptr [rdx], rax
002BA2FC  49 8B 06                        mov rax, qword ptr [r14]
002BA2FF  49 33 C0                        xor rax, r8
002BA302  49 23 C2                        and rax, r10
002BA305  49 33 C0                        xor rax, r8
002BA308  49 89 06                        mov qword ptr [r14], rax
002BA30B  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
002BA30F  48 33 C1                        xor rax, rcx
002BA312  49 23 C2                        and rax, r10
002BA315  48 33 C1                        xor rax, rcx
002BA318  49 89 46 18                     mov qword ptr [r14 + 0x18], rax
002BA31C  4D 3B C3                        cmp r8, r11
002BA31F  0F 84 59 01 00 00               je 0x1402ba47e
002BA325  49 8B 41 18                     mov rax, qword ptr [r9 + 0x18]
002BA329  49 8B CC                        mov rcx, r12
002BA32C  48 33 C8                        xor rcx, rax
002BA32F  49 23 CA                        and rcx, r10
002BA332  49 33 CC                        xor rcx, r12
002BA335  49 89 49 18                     mov qword ptr [r9 + 0x18], rcx
002BA339  48 8D 05 10 33 B7 00            lea rax, [rip + 0xb73310]
002BA340  4C 3B F8                        cmp r15, rax
002BA343  0F 84 FC 05 00 00               je 0x1402ba945
002BA349  41 8B 4E 20                     mov ecx, dword ptr [r14 + 0x20]
002BA34D  40 0F B6 C7                     movzx eax, dil
002BA351  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
002BA355  C1 E9 10                        shr ecx, 0x10
002BA358  32 C1                           xor al, cl
002BA35A  24 07                           and al, 7
002BA35C  32 C1                           xor al, cl
002BA35E  88 44 24 32                     mov byte ptr [rsp + 0x32], al
002BA362  8B 44 24 30                     mov eax, dword ptr [rsp + 0x30]
002BA366  41 89 46 20                     mov dword ptr [r14 + 0x20], eax
002BA36A  44 8B 7C 24 34                  mov r15d, dword ptr [rsp + 0x34]
002BA36F  83 FF 02                        cmp edi, 2
002BA372  0F 84 4C 02 00 00               je 0x1402ba5c4
002BA378  8B 4C 24 38                     mov ecx, dword ptr [rsp + 0x38]
002BA37C  33 F6                           xor esi, esi
002BA37E  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
002BA383  48 85 C0                        test rax, rax
002BA386  0F 85 45 07 00 00               jne 0x1402baad1
002BA38C  80 7C 24 60 00                  cmp byte ptr [rsp + 0x60], 0
002BA391  0F 84 E3 04 00 00               je 0x1402ba87a
002BA397  80 7C 24 78 00                  cmp byte ptr [rsp + 0x78], 0
002BA39C  48 B9 FF FF FF FF FF FF FF 7F   movabs rcx, 0x7fffffffffffffff
002BA3A6  74 0A                           je 0x1402ba3b2
002BA3A8  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
002BA3AD  F0 48 21 48 18                  lock and qword ptr [rax + 0x18], rcx
002BA3B2  80 BC 24 90 00 00 00 00         cmp byte ptr [rsp + 0x90], 0
002BA3BA  74 0D                           je 0x1402ba3c9
002BA3BC  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
002BA3C4  F0 48 21 48 18                  lock and qword ptr [rax + 0x18], rcx
002BA3C9  80 BC 24 A8 00 00 00 00         cmp byte ptr [rsp + 0xa8], 0
002BA3D1  74 0D                           je 0x1402ba3e0
002BA3D3  48 8B 84 24 A0 00 00 00         mov rax, qword ptr [rsp + 0xa0]
002BA3DB  F0 48 21 48 18                  lock and qword ptr [rax + 0x18], rcx
002BA3E0  80 BC 24 C0 00 00 00 00         cmp byte ptr [rsp + 0xc0], 0
002BA3E8  74 0D                           je 0x1402ba3f7
002BA3EA  48 8B 84 24 B8 00 00 00         mov rax, qword ptr [rsp + 0xb8]
002BA3F2  F0 48 21 48 18                  lock and qword ptr [rax + 0x18], rcx
002BA3F7  F6 05 08 C7 D0 00 01            test byte ptr [rip + 0xd0c708], 1
002BA3FE  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
002BA403  0F 85 C3 04 00 00               jne 0x1402ba8cc
002BA409  F0 81 60 20 FF FF FF BF         lock and dword ptr [rax + 0x20], 0xbfffffff
002BA411  F0 FF 48 20                     lock dec dword ptr [rax + 0x20]
002BA415  83 FF 04                        cmp edi, 4
002BA418  7F 24                           jg 0x1402ba43e
002BA41A  41 83 FF 09                     cmp r15d, 9
002BA41E  75 1E                           jne 0x1402ba43e
002BA420  F6 C3 05                        test bl, 5
002BA423  75 19                           jne 0x1402ba43e
002BA425  41 B9 03 00 00 00               mov r9d, 3
002BA42B  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
002BA430  45 8B C1                        mov r8d, r9d
002BA433  49 8B D4                        mov rdx, r12
002BA436  49 8B CD                        mov rcx, r13
002BA439  E8 42 4B 08 00                  call 0x14033ef80
002BA43E  F6 C3 02                        test bl, 2
002BA441  0F 85 4E 04 00 00               jne 0x1402ba895
002BA447  83 FB 08                        cmp ebx, 8
002BA44A  0F 83 93 06 00 00               jae 0x1402baae3
002BA450  48 8B 8C 24 D0 00 00 00         mov rcx, qword ptr [rsp + 0xd0]
002BA458  48 33 CC                        xor rcx, rsp
002BA45B  E8 E0 21 3F 00                  call 0x1406ac640
002BA460  4C 8D 9C 24 E0 00 00 00         lea r11, [rsp + 0xe0]
002BA468  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
002BA46C  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
002BA470  49 8B E3                        mov rsp, r11
002BA473  41 5F                           pop r15
002BA475  41 5E                           pop r14
002BA477  41 5D                           pop r13
002BA479  41 5C                           pop r12
002BA47B  5F                              pop rdi
002BA47C  C3                              ret
002BA47D  CC                              int3
002BA47E  4D 89 67 18                     mov qword ptr [r15 + 0x18], r12
002BA482  E9 B2 FE FF FF                  jmp 0x1402ba339
002BA487  8B DE                           mov ebx, esi
002BA489  E9 55 FC FF FF                  jmp 0x1402ba0e3
002BA48E  49 8B CE                        mov rcx, r14
002BA491  E8 5E 09 00 00                  call 0x1402badf4
002BA496  E9 10 FE FF FF                  jmp 0x1402ba2ab
002BA49B  41 8B 46 20                     mov eax, dword ptr [r14 + 0x20]
002BA49F  8B 4C 24 34                     mov ecx, dword ptr [rsp + 0x34]
002BA4A3  C1 E8 18                        shr eax, 0x18
002BA4A6  A8 40                           test al, 0x40
002BA4A8  0F 85 FD 03 00 00               jne 0x1402ba8ab
002BA4AE  8B 05 4C AD D0 00               mov eax, dword ptr [rip + 0xd0ad4c]
002BA4B4  A8 02                           test al, 2
002BA4B6  0F 85 2F 17 42 00               jne 0x1406dbbeb
002BA4BC  85 F6                           test esi, esi
002BA4BE  0F 85 0A 05 00 00               jne 0x1402ba9ce
002BA4C4  49 8B CE                        mov rcx, r14
002BA4C7  E8 24 82 06 00                  call 0x1403226f0
002BA4CC  8B 4C 24 34                     mov ecx, dword ptr [rsp + 0x34]
002BA4D0  44 8B D0                        mov r10d, eax
002BA4D3  8B 44 24 38                     mov eax, dword ptr [rsp + 0x38]
002BA4D7  25 00 08 00 00                  and eax, 0x800
002BA4DC  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
002BA4E0  75 79                           jne 0x1402ba55b
002BA4E2  4D 6B FA 58                     imul r15, r10, 0x58
002BA4E6  49 81 C7 C0 0C 00 00            add r15, 0xcc0
002BA4ED  4D 03 FD                        add r15, r13
002BA4F0  83 FB 04                        cmp ebx, 4
002BA4F3  73 66                           jae 0x1402ba55b
002BA4F5  83 F9 09                        cmp ecx, 9
002BA4F8  75 61                           jne 0x1402ba55b
002BA4FA  49 8B 46 28                     mov rax, qword ptr [r14 + 0x28]
002BA4FE  B9 40 1C 00 00                  mov ecx, 0x1c40
002BA503  48 C1 E8 3F                     shr rax, 0x3f
002BA507  BA C0 3F 00 00                  mov edx, 0x3fc0
002BA50C  84 C0                           test al, al
002BA50E  0F 44 CA                        cmove ecx, edx
002BA511  F0 4A FF 04 29                  lock inc qword ptr [rcx + r13]
002BA516  B8 01 00 00 00                  mov eax, 1
002BA51B  8B F0                           mov esi, eax
002BA51D  F0 49 0F C1 B5 00 49 00 00      lock xadd qword ptr [r13 + 0x4900], rsi
002BA526  48 FF C6                        inc rsi
002BA529  48 81 FE 20 04 00 00            cmp rsi, 0x420
002BA530  0F 86 4D 04 00 00               jbe 0x1402ba983
002BA536  48 FF CE                        dec rsi
002BA539  49 3B B5 00 41 00 00            cmp rsi, qword ptr [r13 + 0x4100]
002BA540  0F 84 EA 04 00 00               je 0x1402baa30
002BA546  49 3B B5 08 41 00 00            cmp rsi, qword ptr [r13 + 0x4108]
002BA54D  0F 84 DD 04 00 00               je 0x1402baa30
002BA553  8B 4C 24 34                     mov ecx, dword ptr [rsp + 0x34]
002BA557  8B 44 24 40                     mov eax, dword ptr [rsp + 0x40]
002BA55B  F6 44 24 38 80                  test byte ptr [rsp + 0x38], 0x80
002BA560  4C 89 7C 24 40                  mov qword ptr [rsp + 0x40], r15
002BA565  0F 85 26 FD FF FF               jne 0x1402ba291
002BA56B  83 F9 09                        cmp ecx, 9
002BA56E  0F 8C 96 02 00 00               jl 0x1402ba80a
002BA574  48 8D 44 24 60                  lea rax, [rsp + 0x60]
002BA579  44 8B C9                        mov r9d, ecx
002BA57C  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
002BA581  4D 8B C6                        mov r8, r14
002BA584  49 8B D7                        mov rdx, r15
002BA587  48 C7 44 24 20 00 00 00 00      mov qword ptr [rsp + 0x20], 0
002BA590  49 8B CD                        mov rcx, r13
002BA593  E8 E8 08 00 00                  call 0x1402bae80
002BA598  80 7C 24 60 00                  cmp byte ptr [rsp + 0x60], 0
002BA59D  0F 85 EE FC FF FF               jne 0x1402ba291
002BA5A3  0F B6 54 24 62                  movzx edx, byte ptr [rsp + 0x62]
002BA5A8  83 FA 03                        cmp edx, 3
002BA5AB  0F 84 E0 FC FF FF               je 0x1402ba291
002BA5B1  44 0F B6 44 24 61               movzx r8d, byte ptr [rsp + 0x61]
002BA5B7  49 8B CE                        mov rcx, r14
002BA5BA  E8 21 AB 11 00                  call 0x1403d50e0
002BA5BF  E9 CD FC FF FF                  jmp 0x1402ba291
002BA5C4  41 83 FF 09                     cmp r15d, 9
002BA5C8  0F 8C 02 02 00 00               jl 0x1402ba7d0
002BA5CE  85 F6                           test esi, esi
002BA5D0  0F 85 1A 03 00 00               jne 0x1402ba8f0
002BA5D6  40 38 74 24 60                  cmp byte ptr [rsp + 0x60], sil
002BA5DB  4C 8D 44 24 60                  lea r8, [rsp + 0x60]
002BA5E0  BE 00 00 00 00                  mov esi, 0
002BA5E5  49 8B CE                        mov rcx, r14
002BA5E8  4C 0F 44 C6                     cmove r8, rsi
002BA5EC  8D 56 09                        lea edx, [rsi + 9]
002BA5EF  E8 EC 18 08 00                  call 0x14033bee0
002BA5F4  8B 4C 24 38                     mov ecx, dword ptr [rsp + 0x38]
002BA5F8  E9 81 FD FF FF                  jmp 0x1402ba37e
002BA5FD  49 8B 85 C0 44 00 00            mov rax, qword ptr [r13 + 0x44c0]
002BA604  8B 70 18                        mov esi, dword ptr [rax + 0x18]
002BA607  48 8D 46 40                     lea rax, [rsi + 0x40]
002BA60B  4C 6B F8 58                     imul r15, rax, 0x58
002BA60F  4D 03 FD                        add r15, r13
002BA612  85 C9                           test ecx, ecx
002BA614  0F 84 C4 00 00 00               je 0x1402ba6de
002BA61A  41 0F B6 46 24                  movzx eax, byte ptr [r14 + 0x24]
002BA61F  4D 8D 85 A0 4C 00 00            lea r8, [r13 + 0x4ca0]
002BA626  40 32 F0                        xor sil, al
002BA629  40 80 E6 0F                     and sil, 0xf
002BA62D  40 32 F0                        xor sil, al
002BA630  41 88 76 24                     mov byte ptr [r14 + 0x24], sil
002BA634  E9 B3 FB FF FF                  jmp 0x1402ba1ec
002BA639  8B 4C 24 30                     mov ecx, dword ptr [rsp + 0x30]
002BA63D  41 FF C1                        inc r9d
002BA640  E9 1A FC FF FF                  jmp 0x1402ba25f
002BA645  F0 49 FF 85 C0 3F 00 00         lock inc qword ptr [r13 + 0x3fc0]
002BA64D  E9 33 FB FF FF                  jmp 0x1402ba185
002BA652  83 FF 04                        cmp edi, 4
002BA655  0F 85 40 04 00 00               jne 0x1402baa9b
002BA65B  48 8B 0D 1E 36 B7 00            mov rcx, qword ptr [rip + 0xb7361e]
002BA662  49 8B 46 10                     mov rax, qword ptr [r14 + 0x10]
002BA666  48 85 C9                        test rcx, rcx
002BA669  74 0A                           je 0x1402ba675
002BA66B  A8 10                           test al, 0x10
002BA66D  75 06                           jne 0x1402ba675
002BA66F  48 F7 D1                        not rcx
002BA672  48 23 C1                        and rax, rcx
002BA675  48 C1 F8 10                     sar rax, 0x10
002BA679  48 8B 30                        mov rsi, qword ptr [rax]
002BA67C  49 8B 46 28                     mov rax, qword ptr [r14 + 0x28]
002BA680  48 85 C0                        test rax, rax
002BA683  48 89 74 24 48                  mov qword ptr [rsp + 0x48], rsi
002BA688  49 8D 85 C0 3F 00 00            lea rax, [r13 + 0x3fc0]
002BA68F  79 07                           jns 0x1402ba698
002BA691  49 8D 85 40 1C 00 00            lea rax, [r13 + 0x1c40]
002BA698  F0 48 FF 00                     lock inc qword ptr [rax]
002BA69C  49 8D 47 20                     lea rax, [r15 + 0x20]
002BA6A0  48 8B C8                        mov rcx, rax
002BA6A3  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
002BA6A8  E8 D3 E7 F8 FF                  call 0x140248e80
002BA6AD  48 8D 4E 48                     lea rcx, [rsi + 0x48]
002BA6B1  E8 CA E7 F8 FF                  call 0x140248e80
002BA6B6  8B 46 38                        mov eax, dword ptr [rsi + 0x38]
002BA6B9  A8 08                           test al, 8
002BA6BB  0F 85 D0 FB FF FF               jne 0x1402ba291
002BA6C1  48 8D 4E 48                     lea rcx, [rsi + 0x48]
002BA6C5  E8 16 F1 F8 FF                  call 0x1402497e0
002BA6CA  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
002BA6CF  E8 0C F1 F8 FF                  call 0x1402497e0
002BA6D4  BF 03 00 00 00                  mov edi, 3
002BA6D9  E9 A7 FA FF FF                  jmp 0x1402ba185
002BA6DE  48 8D 54 24 60                  lea rdx, [rsp + 0x60]
002BA6E3  49 8B CF                        mov rcx, r15
002BA6E6  E8 B5 74 15 00                  call 0x140411ba0
002BA6EB  E9 2A FF FF FF                  jmp 0x1402ba61a
002BA6F0  40 F6 C7 10                     test dil, 0x10
002BA6F4  0F 85 3F 02 00 00               jne 0x1402ba939
002BA6FA  0F BA E7 08                     bt edi, 8
002BA6FE  0F 82 B7 02 00 00               jb 0x1402ba9bb
002BA704  0F BA E7 0B                     bt edi, 0xb
002BA708  0F 83 65 03 00 00               jae 0x1402baa73
002BA70E  49 8B 46 28                     mov rax, qword ptr [r14 + 0x28]
002BA712  48 8B 0D 6F 59 B7 00            mov rcx, qword ptr [rip + 0xb7596f]
002BA719  48 C1 E8 2B                     shr rax, 0x2b
002BA71D  25 FF 03 00 00                  and eax, 0x3ff
002BA722  48 8B 3C C1                     mov rdi, qword ptr [rcx + rax*8]
002BA726  49 8B CE                        mov rcx, r14
002BA729  E8 02 68 FF FF                  call 0x1402b0f30
002BA72E  8B C8                           mov ecx, eax
002BA730  48 69 D1 80 DF 00 00            imul rdx, rcx, 0xdf80
002BA737  49 63 C7                        movsxd rax, r15d
002BA73A  48 69 C8 E8 00 00 00            imul rcx, rax, 0xe8
002BA741  48 03 D1                        add rdx, rcx
002BA744  48 8B 4F 10                     mov rcx, qword ptr [rdi + 0x10]
002BA748  48 81 C1 50 3D 00 00            add rcx, 0x3d50
002BA74F  48 03 CA                        add rcx, rdx
002BA752  49 8B D6                        mov rdx, r14
002BA755  E8 DA 4D FF FF                  call 0x1402af534
002BA75A  4C 8B F8                        mov r15, rax
002BA75D  48 83 F8 FF                     cmp rax, -1
002BA761  0F 85 A6 F9 FF FF               jne 0x1402ba10d
002BA767  33 D2                           xor edx, edx
002BA769  49 8B CE                        mov rcx, r14
002BA76C  E8 1F 36 08 00                  call 0x14033dd90
002BA771  BA 02 00 00 00                  mov edx, 2
002BA776  49 8B CC                        mov rcx, r12
002BA779  E8 A2 A5 07 00                  call 0x140334d20
002BA77E  E9 CD FC FF FF                  jmp 0x1402ba450
002BA783  49 8B 4F 18                     mov rcx, qword ptr [r15 + 0x18]
002BA787  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
002BA791  48 8D 14 49                     lea rdx, [rcx + rcx*2]
002BA795  48 C1 E2 04                     shl rdx, 4
002BA799  48 8B C0                        mov rax, rax
002BA79C  48 03 D0                        add rdx, rax
002BA79F  4D 8B C3                        mov r8, r11
002BA7A2  45 33 C9                        xor r9d, r9d
002BA7A5  E9 30 FB FF FF                  jmp 0x1402ba2da
002BA7AA  BB 04 00 00 00                  mov ebx, 4
002BA7AF  E9 2F F9 FF FF                  jmp 0x1402ba0e3
002BA7B4  F7 44 24 38 00 08 00 00         test dword ptr [rsp + 0x38], 0x800
002BA7BC  0F 85 E5 FA FF FF               jne 0x1402ba2a7
002BA7C2  83 FF 02                        cmp edi, 2
002BA7C5  0F 85 DC FA FF FF               jne 0x1402ba2a7
002BA7CB  E9 DB FA FF FF                  jmp 0x1402ba2ab
002BA7D0  8B 4C 24 38                     mov ecx, dword ptr [rsp + 0x38]
002BA7D4  0F BA E1 0B                     bt ecx, 0xb
002BA7D8  72 5B                           jb 0x1402ba835
002BA7DA  80 7C 24 60 00                  cmp byte ptr [rsp + 0x60], 0
002BA7DF  4C 8D 44 24 60                  lea r8, [rsp + 0x60]
002BA7E4  BE 00 00 00 00                  mov esi, 0
002BA7E9  41 8B D7                        mov edx, r15d
002BA7EC  4C 0F 44 C6                     cmove r8, rsi
002BA7F0  49 8B CE                        mov rcx, r14
002BA7F3  E8 E8 16 08 00                  call 0x14033bee0
002BA7F8  8B 4C 24 38                     mov ecx, dword ptr [rsp + 0x38]
002BA7FC  E9 7D FB FF FF                  jmp 0x1402ba37e
002BA801  4D 89 67 10                     mov qword ptr [r15 + 0x10], r12
002BA805  E9 F2 FA FF FF                  jmp 0x1402ba2fc
002BA80A  85 C0                           test eax, eax
002BA80C  0F 84 62 FD FF FF               je 0x1402ba574
002BA812  48 8D 54 24 60                  lea rdx, [rsp + 0x60]
002BA817  49 8B CF                        mov rcx, r15
002BA81A  E8 81 73 15 00                  call 0x140411ba0
002BA81F  E9 6D FA FF FF                  jmp 0x1402ba291
002BA824  44 8D 7A FF                     lea r15d, [rdx - 1]
002BA828  E9 B1 F8 FF FF                  jmp 0x1402ba0de
002BA82D  83 CB 02                        or ebx, 2
002BA830  E9 AC F9 FF FF                  jmp 0x1402ba1e1
002BA835  41 8B 46 20                     mov eax, dword ptr [r14 + 0x20]
002BA839  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
002BA83D  C1 E8 18                        shr eax, 0x18
002BA840  0C 08                           or al, 8
002BA842  88 44 24 33                     mov byte ptr [rsp + 0x33], al
002BA846  8B 44 24 30                     mov eax, dword ptr [rsp + 0x30]
002BA84A  41 89 46 20                     mov dword ptr [r14 + 0x20], eax
002BA84E  E9 29 FB FF FF                  jmp 0x1402ba37c
002BA853  49 FF C3                        inc r11
002BA856  48 83 C6 08                     add rsi, 8
002BA85A  45 33 C9                        xor r9d, r9d
002BA85D  E9 F0 F9 FF FF                  jmp 0x1402ba252
002BA862  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
002BA867  44 8B 4C 24 40                  mov r9d, dword ptr [rsp + 0x40]
002BA86C  48 81 C1 80 DF 00 00            add rcx, 0xdf80
002BA873  FF C0                           inc eax
002BA875  E9 BD F9 FF FF                  jmp 0x1402ba237
002BA87A  84 C9                           test cl, cl
002BA87C  0F 88 93 FB FF FF               js 0x1402ba415
002BA882  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
002BA887  48 83 C1 20                     add rcx, 0x20
002BA88B  E8 50 EF F8 FF                  call 0x1402497e0
002BA890  E9 80 FB FF FF                  jmp 0x1402ba415
002BA895  49 8D 8D A0 03 00 00            lea rcx, [r13 + 0x3a0]
002BA89C  45 33 C0                        xor r8d, r8d
002BA89F  33 D2                           xor edx, edx
002BA8A1  E8 6A 4A 08 00                  call 0x14033f310
002BA8A6  E9 9C FB FF FF                  jmp 0x1402ba447
002BA8AB  83 F9 09                        cmp ecx, 9
002BA8AE  0F 85 FA FB FF FF               jne 0x1402ba4ae
002BA8B4  33 D2                           xor edx, edx
002BA8B6  49 8B CE                        mov rcx, r14
002BA8B9  E8 D2 34 08 00                  call 0x14033dd90
002BA8BE  BF 20 00 00 00                  mov edi, 0x20
002BA8C3  89 7C 24 38                     mov dword ptr [rsp + 0x38], edi
002BA8C7  E9 8E F7 FF FF                  jmp 0x1402ba05a
002BA8CC  8B 0D 86 35 C5 00               mov ecx, dword ptr [rip + 0xc53586]
002BA8D2  85 C9                           test ecx, ecx
002BA8D4  0F 85 2F FB FF FF               jne 0x1402ba409
002BA8DA  48 8B 94 24 08 01 00 00         mov rdx, qword ptr [rsp + 0x108]
002BA8E2  48 8D 48 20                     lea rcx, [rax + 0x20]
002BA8E6  E8 5D 66 03 00                  call 0x1402f0f48
002BA8EB  E9 25 FB FF FF                  jmp 0x1402ba415
002BA8F0  33 F6                           xor esi, esi
002BA8F2  E9 FD FC FF FF                  jmp 0x1402ba5f4
002BA8F7  49 8B 30                        mov rsi, qword ptr [r8]
002BA8FA  48 83 FE 10                     cmp rsi, 0x10
002BA8FE  72 0F                           jb 0x1402ba90f
002BA900  48 C7 C2 FF FF FF FF            mov rdx, 0xffffffffffffffff
002BA907  49 8B CD                        mov rcx, r13
002BA90A  E8 09 22 10 00                  call 0x1403bcb18
002BA90F  49 8B 85 C0 4B 00 00            mov rax, qword ptr [r13 + 0x4bc0]
002BA916  48 2B C6                        sub rax, rsi
002BA919  48 83 F8 10                     cmp rax, 0x10
002BA91D  0F 82 60 F9 FF FF               jb 0x1402ba283
002BA923  49 8D 8D 48 03 00 00            lea rcx, [r13 + 0x348]
002BA92A  45 33 C0                        xor r8d, r8d
002BA92D  33 D2                           xor edx, edx
002BA92F  E8 DC 49 08 00                  call 0x14033f310
002BA934  E9 4A F9 FF FF                  jmp 0x1402ba283
002BA939  4D 8D BD 40 4C 00 00            lea r15, [r13 + 0x4c40]
002BA940  E9 C8 F7 FF FF                  jmp 0x1402ba10d
002BA945  41 8B 46 20                     mov eax, dword ptr [r14 + 0x20]
002BA949  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
002BA94D  C1 E8 10                        shr eax, 0x10
002BA950  24 FA                           and al, 0xfa
002BA952  0C 02                           or al, 2
002BA954  88 44 24 32                     mov byte ptr [rsp + 0x32], al
002BA958  8B 44 24 30                     mov eax, dword ptr [rsp + 0x30]
002BA95C  41 89 46 20                     mov dword ptr [r14 + 0x20], eax
002BA960  41 8B 46 20                     mov eax, dword ptr [r14 + 0x20]
002BA964  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
002BA968  C1 E8 18                        shr eax, 0x18
002BA96B  0C 10                           or al, 0x10
002BA96D  88 44 24 33                     mov byte ptr [rsp + 0x33], al
002BA971  8B 44 24 30                     mov eax, dword ptr [rsp + 0x30]
002BA975  41 89 46 20                     mov dword ptr [r14 + 0x20], eax
002BA979  E8 82 73 21 00                  call 0x1404d1d00
002BA97E  E9 E7 F9 FF FF                  jmp 0x1402ba36a
002BA983  48 81 FE A0 00 00 00            cmp rsi, 0xa0
002BA98A  74 64                           je 0x1402ba9f0
002BA98C  48 81 FE 20 04 00 00            cmp rsi, 0x420
002BA993  0F 84 A4 00 00 00               je 0x1402baa3d
002BA999  48 83 FE 22                     cmp rsi, 0x22
002BA99D  74 4F                           je 0x1402ba9ee
002BA99F  48 81 FE 20 01 00 00            cmp rsi, 0x120
002BA9A6  0F 85 8A FB FF FF               jne 0x1402ba536
002BA9AC  8B D0                           mov edx, eax
002BA9AE  49 8B CD                        mov rcx, r13
002BA9B1  E8 2A 0E 10 00                  call 0x1403bb7e0
002BA9B6  E9 7B FB FF FF                  jmp 0x1402ba536
002BA9BB  49 8B D4                        mov rdx, r12
002BA9BE  49 8B CD                        mov rcx, r13
002BA9C1  E8 92 44 1F 00                  call 0x1404aee58
002BA9C6  4C 8B F8                        mov r15, rax
002BA9C9  E9 3F F7 FF FF                  jmp 0x1402ba10d
002BA9CE  41 8B 46 20                     mov eax, dword ptr [r14 + 0x20]
002BA9D2  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
002BA9D6  C1 E8 10                        shr eax, 0x10
002BA9D9  24 FA                           and al, 0xfa
002BA9DB  0C 02                           or al, 2
002BA9DD  88 44 24 42                     mov byte ptr [rsp + 0x42], al
002BA9E1  8B 44 24 40                     mov eax, dword ptr [rsp + 0x40]
002BA9E5  41 89 46 20                     mov dword ptr [r14 + 0x20], eax
002BA9E9  E9 62 FA FF FF                  jmp 0x1402ba450
002BA9EE  33 C0                           xor eax, eax
002BA9F0  48 C1 E0 05                     shl rax, 5
002BA9F4  49 8D 8D 40 3F 00 00            lea rcx, [r13 + 0x3f40]
002BA9FB  4A 8D 3C 28                     lea rdi, [rax + r13]
002BA9FF  E8 7C E4 F8 FF                  call 0x140248e80
002BAA04  45 33 C0                        xor r8d, r8d
002BAA07  48 8D 8F 48 3F 00 00            lea rcx, [rdi + 0x3f48]
002BAA0E  33 D2                           xor edx, edx
002BAA10  E8 FB 48 08 00                  call 0x14033f310
002BAA15  FF 87 60 3F 00 00               inc dword ptr [rdi + 0x3f60]
002BAA1B  49 8D 8D 40 3F 00 00            lea rcx, [r13 + 0x3f40]
002BAA22  E8 B9 ED F8 FF                  call 0x1402497e0
002BAA27  8B 7C 24 30                     mov edi, dword ptr [rsp + 0x30]
002BAA2B  E9 06 FB FF FF                  jmp 0x1402ba536
002BAA30  49 8B CD                        mov rcx, r13
002BAA33  E8 CC 1D 10 00                  call 0x1403bc804
002BAA38  E9 16 FB FF FF                  jmp 0x1402ba553
002BAA3D  B8 02 00 00 00                  mov eax, 2
002BAA42  EB AC                           jmp 0x1402ba9f0
002BAA44  F6 C3 01                        test bl, 1
002BAA47  0F 84 A0 F6 FF FF               je 0x1402ba0ed
002BAA4D  80 3D EC 31 B7 00 00            cmp byte ptr [rip + 0xb731ec], 0
002BAA54  0F 84 93 F6 FF FF               je 0x1402ba0ed
002BAA5A  83 E7 F7                        and edi, 0xfffffff7
002BAA5D  33 D2                           xor edx, edx
002BAA5F  83 CF 04                        or edi, 4
002BAA62  49 8B CE                        mov rcx, r14
002BAA65  89 7C 24 38                     mov dword ptr [rsp + 0x38], edi
002BAA69  E8 F2 7E 0A 00                  call 0x140362960
002BAA6E  E9 7A F6 FF FF                  jmp 0x1402ba0ed
002BAA73  4D 8D BD 80 1B 00 00            lea r15, [r13 + 0x1b80]
002BAA7A  E9 8E F6 FF FF                  jmp 0x1402ba10d
002BAA7F  41 8B 46 20                     mov eax, dword ptr [r14 + 0x20]
002BAA83  C1 E8 18                        shr eax, 0x18
002BAA86  A8 40                           test al, 0x40
002BAA88  0F 85 32 11 42 00               jne 0x1406dbbc0
002BAA8E  A8 10                           test al, 0x10
002BAA90  0F 84 82 F6 FF FF               je 0x1402ba118
002BAA96  E9 25 11 42 00                  jmp 0x1406dbbc0
002BAA9B  48 8D 05 AE 2B B7 00            lea rax, [rip + 0xb72bae]
002BAAA2  4C 3B F8                        cmp r15, rax
002BAAA5  0F 84 DB 11 42 00               je 0x1406dbc86
002BAAAB  41 8B 46 20                     mov eax, dword ptr [r14 + 0x20]
002BAAAF  C1 E8 18                        shr eax, 0x18
002BAAB2  A8 40                           test al, 0x40
002BAAB4  0F 84 C5 11 42 00               je 0x1406dbc7f
002BAABA  45 33 C9                        xor r9d, r9d
002BAABD  33 D2                           xor edx, edx
002BAABF  49 8B CE                        mov rcx, r14
002BAAC2  45 8D 41 01                     lea r8d, [r9 + 1]
002BAAC6  E8 05 FA 3B 00                  call 0x14067a4d0
002BAACB  90                              nop
002BAACC  E9 AE 11 42 00                  jmp 0x1406dbc7f
002BAAD1  48 8D 48 48                     lea rcx, [rax + 0x48]
002BAAD5  E8 06 ED F8 FF                  call 0x1402497e0
002BAADA  8B 4C 24 38                     mov ecx, dword ptr [rsp + 0x38]
002BAADE  E9 A9 F8 FF FF                  jmp 0x1402ba38c
002BAAE3  33 C9                           xor ecx, ecx
002BAAE5  E8 B6 2E 22 00                  call 0x1404dd9a0
002BAAEA  E9 61 F9 FF FF                  jmp 0x1402ba450
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiInsertPageInList(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m108;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned __int8 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int8 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int8 v_stack_m78;
    unsigned __int8 v_stack_m7E;
    unsigned __int8 v_stack_m7F;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int8 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int8 v_stack_m9E;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned int v_stack_mAC;
    unsigned __int8 v_stack_mAD;
    unsigned __int8 v_stack_mAE;
    unsigned int v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned int v_stack_mD0;
    unsigned int v_stack_mD4;
    unsigned __int8 v_stack_mD6;
    unsigned int v_stack_mD8;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p28;

    v_stack_p10 = v_rbx;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (224);
    result = (*(unsigned __int64 *)(v_rip + 11863839)) ^ (v_rsp);
    v_stack_m38 = result;
    v_stack_mD0 = a2;
    v_r12 = (a1) - (result);
    v_r12 = (v_r12) >> (4);
    v_r12 = (v_r12) * (result);
loc_002BA05A:
    a2 = 0;
    result = (*(unsigned __int64 *)(a1 + 40)) >> (43);
    v_rbx = 0;
    result = (unsigned int)((result) & (0x3FFULL));
    result = memset(v_stack_mA8, a2, 1 + 103, a4);
    v_stack_mD4 = 9;
    if (condition_is_below) goto loc_002BA487;
    if (v_r12 < (*(unsigned __int64 *)(v_rip + 12041049))) goto loc_002BA0BB;
    result = (*(unsigned __int64 *)(v_rip + 12041049)) + (0x800ULL);
    if (v_r12 < result) goto loc_002BA7AA;
loc_002BA0BB:
    if ((*(unsigned __int8 *)(v_rip + 12069668)) == 0) goto loc_002BA0DE;
    a1 = (v_r12) >> (9);
    if ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 12071285) + a1 * 2)) != 0) goto loc_002BA824;
loc_002BA0DE:
    v_stack_mD4 = 9;
loc_002BA0E3:
    if ((((unsigned __int8)((unsigned int)(a2))) & (8)) != 0) goto loc_002BAA44;
loc_002BA0ED:
    if ((((unsigned __int8)((unsigned int)(a2))) & (4)) != 0) goto loc_002BA106;
    if ((((unsigned __int8)((unsigned int)(a2))) & (8)) == 0) goto loc_002BA6F0;
    goto loc_002BA10D;
loc_002BA106:
loc_002BA10D:
    v_rsi = (unsigned int)((0) & (1));
    if (condition_is_not_equal) goto loc_002BAA7F;
loc_002BA118:
    v_stack_mD8 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12017694) + result * 8) + 3136 + 12)));
    v_stack_mC8 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12017694) + result * 8) + 3136;
    v_stack_mC0 = 0;
    result = *(unsigned __int64 *)(v_rip + 12071285);
    if ((unsigned int)(v_rsi) == 0) {
        a2 = *(unsigned int *)(v_rip + 13717316);
        result = *(unsigned __int64 *)(a1 + 24);
        a2 = (a2) << (59);
        a1 = a2;
        a1 = (a1) ^ (result);
        a1 = (a1) & (result);
        a1 = (a1) ^ (a2);
        *(unsigned __int64 *)(a1 + 24) = a1;
    }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12017694) + result * 8) + 3136 + 12)))) == 2) goto loc_002BA49B;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12017694) + result * 8) + 3136 + 12)))) != 3) goto loc_002BA652;
    if (!sign_flag) goto loc_002BA645;
loc_002BA185:
    a1 = (unsigned int)(((unsigned int)(v_stack_mD0)) & (128));
    v_stack_mD8 = (unsigned int)(a1);
    if (condition_is_below) goto loc_002BA5FD;
    a3 = 0;
    a3 = ((unsigned int)(a1) == 0) ? 1 : 0;
    result = MiDetermineModifiedPageListHead(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12017694) + result * 8), a3, a4);
    if (v_stack_mD8 == 0) {
        a2 = v_stack_mA8;
        a1 = result;
        result = MiLockPageListAndLastPage(a1, a2, a3, a4);
    }
    if (*(unsigned __int64 *)(result) == 0) goto loc_002BA82D;
loc_002BA1E1:
loc_002BA1EC:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12017694) + result * 8) + 18688)) >= 0x420ULL) goto loc_002BA283;
    v_stack_mD8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12008115)));
    result = 0;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12017694) + result * 8) + 16)) + (0x3A60ULL);
    v_stack_mC8 = (unsigned int)(*(unsigned __int16 *)(v_rip + 13675995));
loc_002BA237:
    v_stack_mC0 = a1;
    if (0 >= ((unsigned int)(*(unsigned __int16 *)(v_rip + 13675995)))) goto loc_002BA8F7;
    a4 = 0;
loc_002BA252:
    if (0 > 1) goto loc_002BA862;
loc_002BA25F:
    if (0 >= ((unsigned int)((unsigned int)(v_stack_mD8)))) goto loc_002BA853;
    a1 = (0) + (0);
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12017694) + result * 8) + 18688)) + (*(unsigned __int16 *)(*(unsigned __int64 *)(a1) + a1 * 8));
    if (a2 < 0x420ULL) goto loc_002BA639;
loc_002BA283:
    v_stack_mC0 = 0;
    v_stack_mC8 = 0;
loc_002BA291:
    v_rsi = (unsigned int)((0) & (4));
    if (condition_is_not_equal) goto loc_002BA48E;
    if (v_stack_mD4 != 9) goto loc_002BA7B4;
loc_002BA2A7:
loc_002BA2AB:
    if (v_stack_mA8 == 0) goto loc_002BA783;
loc_002BA2DA:
    if (v_stack_mA0 == 0) goto loc_002BA801;
    result = (*(unsigned __int64 *)(v_stack_m98)) ^ (v_r12);
    result = (result) & (*(unsigned __int64 *)(a1));
    result = (result) ^ (v_r12);
    *(unsigned __int64 *)(v_stack_m98) = result;
loc_002BA2FC:
    result = (*(unsigned __int64 *)(a1)) ^ (v_stack_m88);
    result = (result) & (*(unsigned __int64 *)(a1));
    result = (result) ^ (v_stack_m88);
    *(unsigned __int64 *)(a1) = result;
    result = (*(unsigned __int64 *)(a1 + 24)) ^ (v_stack_mA0);
    result = (result) & (*(unsigned __int64 *)(a1));
    result = (result) ^ (v_stack_mA0);
    *(unsigned __int64 *)(a1 + 24) = result;
    if (v_stack_m88 == 0) goto loc_002BA47E;
    a1 = (v_r12) ^ (*(unsigned __int64 *)(v_stack_m80 + 24));
    a1 = (a1) & (*(unsigned __int64 *)(a1));
    a1 = (a1) ^ (v_r12);
    *(unsigned __int64 *)(v_stack_m80 + 24) = a1;
loc_002BA339:
    if (result == (v_rip + 12006160)) goto loc_002BA945;
    v_stack_mD8 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 32)));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 32))) >> (16));
    result = (unsigned __int8)(((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12017694) + result * 8) + 3136 + 12)))) ^ ((unsigned __int8)(a1)));
    result = (unsigned __int8)((result) & (7));
    result = (unsigned __int8)((result) ^ ((unsigned __int8)(a1)));
    v_stack_mD6 = (unsigned __int8)(result);
    *(unsigned int *)(a1 + 32) = (unsigned int)((unsigned int)(v_stack_mD8));
loc_002BA36A:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12017694) + result * 8) + 3136 + 12)))) == 2) goto loc_002BA5C4;
loc_002BA37C:
    v_rsi = 0;
loc_002BA37E:
    if (v_stack_mC0 != 0) goto loc_002BAAD1;
loc_002BA38C:
    if (v_stack_mA8 == 0) goto loc_002BA87A;
    result = v_stack_mC0;
    if (v_stack_m90 != 0) {
        result = v_stack_m98;
    }
    if (v_stack_m78 != 0) {
        result = v_stack_m80;
    }
    if (v_stack_m60 != 0) {
        result = v_stack_m68;
    }
    if (v_stack_m48 != 0) {
        result = v_stack_m50;
    }
    if (((*(unsigned __int8 *)(v_rip + 13682440)) & (1)) != 0) goto loc_002BA8CC;
loc_002BA409:
loc_002BA415:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12017694) + result * 8) + 3136 + 12)))) > 4) goto loc_002BA43E;
    if (((unsigned int)((unsigned int)(v_stack_mD4))) != 9) goto loc_002BA43E;
    result = v_stack_mC8;
    if (((0) & (5)) == 0) {
        a4 = 3;
        v_stack_mE8 = 0;
        a3 = (unsigned int)(a4);
        a2 = v_r12;
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12017694) + result * 8);
        result = MiUpdateLargePageCandidateValue(a1, a2, a3, a4);
    }
    if (((0) & (2)) != 0) goto loc_002BA895;
loc_002BA447:
    if (0 >= 8) goto loc_002BAAE3;
loc_002BA450:
    a1 = (v_stack_m38) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    return result;
loc_002BA47E:
    *(unsigned __int64 *)((unsigned int)(v_stack_mD4) + 24) = v_r12;
    goto loc_002BA339;
loc_002BA487:
    goto loc_002BA0E3;
loc_002BA48E:
    result = MiInsertDecayClusterTimer(a1, a2, a3, a4);
    goto loc_002BA2AB;
loc_002BA49B:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 32))) >> (24));
    if ((((unsigned __int8)(result)) & (64)) != 0) goto loc_002BA8AB;
loc_002BA4AE:
    if ((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 64)) != 0) goto loc_002BA9CE;
    result = MiGetPfnPriority(a1, a2, a3, a4);
    result = (unsigned int)(((unsigned int)(v_stack_mA8)) & (0x800ULL));
    v_stack_mA0 = (unsigned int)(result);
    if (condition_is_not_equal) goto loc_002BA55B;
    v_r15 = ((unsigned int)(v_stack_mD4)) * ((unsigned int)((unsigned int)(result)));
    v_r15 = (v_r15) + (0xCC0ULL);
    v_r15 = (v_r15) + (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12017694) + result * 8));
    if (((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 64))))) >= 4) goto loc_002BA55B;
    if (((unsigned int)((unsigned int)(v_stack_mAC))) != 9) goto loc_002BA55B;
    result = (*(unsigned __int64 *)(a1 + 40)) >> (63);
    a1 = (unsigned int)(0x1C40ULL);
    if ((unsigned __int8)(result) == 0) { a1 = (unsigned int)((unsigned int)(0x3FC0ULL)); }
    v_rsi = (1) + 1;
    if (v_rsi <= 0x420ULL) goto loc_002BA983;
loc_002BA536:
    v_rsi = (v_rsi) - 1;
    if (v_rsi == (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12017694) + result * 8) + 16640))) goto loc_002BAA30;
    if (v_rsi == (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12017694) + result * 8) + 16648))) goto loc_002BAA30;
loc_002BA553:
loc_002BA55B:
    v_stack_mA0 = v_r15;
    if (((v_stack_mA8) & (128)) != 0) goto loc_002BA291;
    if (((unsigned int)((unsigned int)(v_stack_mAC))) < 9) goto loc_002BA80A;
loc_002BA574:
    v_stack_mB8 = v_stack_m80;
    v_stack_mC0 = 0;
    result = MiSynchronizeFastPageInsert(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12017694) + result * 8), v_r15, a1, (unsigned int)((unsigned int)((unsigned int)(v_stack_mAC))));
    if (v_stack_m80 != 0) goto loc_002BA291;
    if (((unsigned int)(v_stack_m7E)) == 3) goto loc_002BA291;
    result = MiRebuildStandbyLookasideList(a1, v_stack_m7E, v_stack_m7F, (unsigned int)((unsigned int)((unsigned int)(v_stack_mAC))));
    goto loc_002BA291;
loc_002BA5C4:
    if (((unsigned int)(v_r15)) < 9) goto loc_002BA7D0;
    if ((unsigned int)(v_rsi) != 0) goto loc_002BA8F0;
    a3 = v_stack_m80;
    if (v_stack_m80 == ((unsigned __int8)(v_rsi))) { a3 = 0; }
    result = MiInsertSecondaryListStandbyPage(a1, 0 + 9, a3, (unsigned int)((unsigned int)((unsigned int)(v_stack_mAC))));
loc_002BA5F4:
    goto loc_002BA37E;
loc_002BA5FD:
    v_r15 = (v_r15) * ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12017694) + result * 8) + 17600) + 24)) + 64);
    v_r15 = (v_r15) + (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12017694) + result * 8));
    if ((unsigned int)((unsigned int)(v_stack_mA8)) == 0) goto loc_002BA6DE;
loc_002BA61A:
    v_rsi = (unsigned __int8)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12017694) + result * 8) + 17600) + 24))) ^ ((unsigned __int8)(*(unsigned __int8 *)(a1 + 36))));
    v_rsi = (unsigned __int8)((v_rsi) & (15));
    v_rsi = (unsigned __int8)((v_rsi) ^ ((unsigned __int8)(*(unsigned __int8 *)(a1 + 36))));
    *(unsigned __int8 *)(a1 + 36) = (unsigned __int8)(v_rsi);
    goto loc_002BA1EC;
loc_002BA639:
    a4 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_mAC)))) + 1);
    goto loc_002BA25F;
loc_002BA645:
    goto loc_002BA185;
loc_002BA652:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12017694) + result * 8) + 3136 + 12)))) != 4) goto loc_002BAA9B;
    if (*(unsigned __int64 *)(v_rip + 12006942) == 0) goto loc_002BA675;
    result = *(unsigned __int64 *)(a1 + 16);
    if ((((unsigned __int8)(*(unsigned __int64 *)(a1 + 16))) & (16)) == 0) {
        a1 = ~(*(unsigned __int64 *)(v_rip + 12006942));
        result = (*(unsigned __int64 *)(a1 + 16)) & (a1);
    }
    result = (result) >> (16);
    v_stack_m98 = *(unsigned __int64 *)(result);
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12017694) + result * 8) + 16320;
    if (sign_flag) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12017694) + result * 8) + 7232;
    }
    v_stack_m90 = v_r15 + 32;
    result = ExAcquireSpinLockExclusiveAtDpcLevel(v_r15 + 32, 0 + 9, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12017694) + result * 8) + 19616, a4);
    result = ExAcquireSpinLockExclusiveAtDpcLevel(*(unsigned __int64 *)(result) + 72, 0 + 9, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12017694) + result * 8) + 19616, a4);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result) + 56)))) & (8)) != 0) goto loc_002BA291;
    result = ExReleaseSpinLockExclusiveFromDpcLevel(*(unsigned __int64 *)(result) + 72, 0 + 9, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12017694) + result * 8) + 19616, a4);
    result = ExReleaseSpinLockExclusiveFromDpcLevel(v_stack_m90, 0 + 9, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12017694) + result * 8) + 19616, a4);
    goto loc_002BA185;
loc_002BA6DE:
    result = MiLockPageListAndLastPage(v_r15, v_stack_m80, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12017694) + result * 8) + 19616, a4);
    goto loc_002BA61A;
loc_002BA6F0:
    if (((3) & (16)) != 0) goto loc_002BA939;
    if (condition_is_below) goto loc_002BA9BB;
    if (condition_is_above_or_equal) goto loc_002BAA73;
    result = (*(unsigned __int64 *)(a1 + 40)) >> (43);
    result = (unsigned int)((result) & (0x3FFULL));
    result = MI_NODE_FROM_PFN(a1, v_stack_m80, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12017694) + result * 8) + 19616, a4);
    a2 = (v_stack_m80) * ((unsigned int)((unsigned int)(result)));
    a1 = ((unsigned int)((unsigned int)(result))) * ((int)((unsigned int)(v_r15)));
    a2 = (a2) + (a1);
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12015983) + result * 8) + 16)) + (0x3D50ULL);
    a1 = (a1) + (a2);
    result = MiGetSlabRepurposedStandbyListWorker(a1, a1, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12017694) + result * 8) + 19616, a4);
    if (result != -1) goto loc_002BA10D;
    a2 = 0;
    result = MiRestoreTransitionPte(a1, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12017694) + result * 8) + 19616, a4);
    result = MiInsertPageInFreeOrZeroedList(v_r12, 2, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12017694) + result * 8) + 19616, a4);
    goto loc_002BA450;
loc_002BA783:
    a2 = (*(unsigned __int64 *)(result + 24) + *(unsigned __int64 *)(result + 24) * 2) << (4);
    a2 = (a2) + (result);
    a4 = 0;
    goto loc_002BA2DA;
loc_002BA7AA:
    goto loc_002BA0E3;
loc_002BA7B4:
    if (((v_stack_mA8) & (0x800ULL)) != 0) goto loc_002BA2A7;
    if (((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12015983) + result * 8))) != 2) goto loc_002BA2A7;
    goto loc_002BA2AB;
loc_002BA7D0:
    if (((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12015983) + result * 8))) < 2) goto loc_002BA835;
    a3 = v_stack_m80;
    if (v_stack_m80 == 0) { a3 = 0; }
    result = MiInsertSecondaryListStandbyPage(a1, (unsigned int)((unsigned int)(result)), a3, a4);
    goto loc_002BA37E;
loc_002BA801:
    *(unsigned __int64 *)(result + 16) = v_r12;
    goto loc_002BA2FC;
loc_002BA80A:
    if ((unsigned int)(result) == 0) goto loc_002BA574;
    result = MiLockPageListAndLastPage(result, v_stack_m80, a3, a4);
    goto loc_002BA291;
loc_002BA824:
    goto loc_002BA0DE;
loc_002BA82D:
    v_rbx = (unsigned int)((4) | (2));
    goto loc_002BA1E1;
loc_002BA835:
    v_stack_mB0 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 32)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 32))) >> (24));
    result = (unsigned __int8)((result) | (8));
    v_stack_mAD = (unsigned __int8)(result);
    *(unsigned int *)(a1 + 32) = (unsigned int)((unsigned int)(v_stack_mB0));
    goto loc_002BA37C;
loc_002BA853:
    v_r11 = (v_stack_m28) + 1;
    v_rsi = (0) + (8);
    a4 = 0;
    goto loc_002BA252;
loc_002BA862:
    a1 = (v_stack_m98) + (0xDF80ULL);
    result = (unsigned int)(((unsigned int)(v_stack_mB0)) + 1);
    goto loc_002BA237;
loc_002BA87A:
    if (sign_flag) goto loc_002BA415;
    a1 = (v_stack_mA0) + (32);
    result = ExReleaseSpinLockExclusiveFromDpcLevel(a1, v_stack_m80, a3, (unsigned int)(v_stack_mA0));
    goto loc_002BA415;
loc_002BA895:
    a3 = 0;
    a2 = 0;
    result = KeSetEvent(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12017694) + result * 8) + 928, a2, a3, (unsigned int)(v_stack_mA0));
    goto loc_002BA447;
loc_002BA8AB:
    if (((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12017694) + result * 8) + 928)) != 9) goto loc_002BA4AE;
    a2 = 0;
    result = MiRestoreTransitionPte(a1, a2, a3, (unsigned int)(v_stack_mA0));
    v_stack_mA8 = 32;
    goto loc_002BA05A;
loc_002BA8CC:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12924294))) != 0) goto loc_002BA409;
    result = ExpReleaseSpinLockSharedFromDpcLevelInstrumented(result + 32, v_stack_p28, a3, (unsigned int)(v_stack_mA0));
    goto loc_002BA415;
loc_002BA8F0:
    v_rsi = 0;
    goto loc_002BA5F4;
loc_002BA8F7:
    if ((*(unsigned __int64 *)(a3)) >= 16) {
        a2 = -1;
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12017694) + result * 8);
        result = MiWakeModifiedPageWriter(a1, a2, a3, (unsigned int)(v_stack_mA0));
    }
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12017694) + result * 8) + 19392)) - (*(unsigned __int64 *)(a3));
    if (result < 16) goto loc_002BA283;
    a3 = 0;
    a2 = 0;
    result = KeSetEvent(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12017694) + result * 8) + 840, a2, a3, (unsigned int)(v_stack_mA0));
    goto loc_002BA283;
loc_002BA939:
    goto loc_002BA10D;
loc_002BA945:
    v_stack_mB0 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 32)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 32))) >> (16));
    result = (unsigned __int8)((result) & (250));
    result = (unsigned __int8)((result) | (2));
    v_stack_mAE = (unsigned __int8)(result);
    *(unsigned int *)(a1 + 32) = (unsigned int)((unsigned int)(v_stack_mB0));
    v_stack_mB0 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 32)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 32))) >> (24));
    result = (unsigned __int8)((result) | (16));
    v_stack_mAD = (unsigned __int8)(result);
    *(unsigned int *)(a1 + 32) = (unsigned int)((unsigned int)(v_stack_mB0));
    result = MiWakeFileOnlyReaper(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12017694) + result * 8) + 840, a2, a3, (unsigned int)(v_stack_mA0));
    goto loc_002BA36A;
loc_002BA983:
    if ((*(unsigned __int64 *)(a3)) == 160) goto loc_002BA9F0;
    if ((*(unsigned __int64 *)(a3)) == 0x420ULL) goto loc_002BAA3D;
    if ((*(unsigned __int64 *)(a3)) == 34) goto loc_002BA9EE;
    if ((*(unsigned __int64 *)(a3)) != 288) goto loc_002BA536;
    result = MiSlabDemotionLowMemoryConditionUpdate(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12017694) + result * 8), (unsigned int)((unsigned int)(result)), a3, (unsigned int)(v_stack_mA0));
    goto loc_002BA536;
loc_002BA9BB:
    result = MiGetEnclavePageList(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12017694) + result * 8), v_r12, a3, (unsigned int)(v_stack_mA0));
    goto loc_002BA10D;
loc_002BA9CE:
    v_stack_mA0 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 32)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 32))) >> (16));
    result = (unsigned __int8)((result) & (250));
    result = (unsigned __int8)((result) | (2));
    v_stack_m9E = (unsigned __int8)(result);
    *(unsigned int *)(a1 + 32) = (unsigned int)((unsigned int)(v_stack_mA0));
    goto loc_002BA450;
loc_002BA9EE:
    result = 0;
loc_002BA9F0:
    result = (result) << (5);
    result = ExAcquireSpinLockExclusiveAtDpcLevel(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12017694) + result * 8) + 16192, v_r12, a3, (unsigned int)(v_stack_mA0));
    a3 = 0;
    a2 = 0;
    result = KeSetEvent(result + *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12017694) + result * 8) * 1 + 16200, a2, a3, (unsigned int)(v_stack_mA0));
    result = ExReleaseSpinLockExclusiveFromDpcLevel(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12017694) + result * 8) + 16192, a2, a3, (unsigned int)(v_stack_mA0));
    goto loc_002BA536;
loc_002BAA30:
    result = MiUpdateAvailableEventsAtDpc(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12017694) + result * 8), a2, a3, (unsigned int)(v_stack_mA0));
    goto loc_002BA553;
loc_002BAA3D:
    goto loc_002BA9F0;
loc_002BAA44:
    if ((((unsigned __int8)(v_rbx)) & (1)) == 0) goto loc_002BA0ED;
    if ((*(unsigned __int8 *)(v_rip + 12005868)) == 0) goto loc_002BA0ED;
    v_rdi = (unsigned int)(((unsigned int)(v_stack_mB0)) & (0xFFFFFFF7ULL));
    a2 = 0;
    v_rdi = (unsigned int)((v_rdi) | (4));
    v_stack_mA8 = (unsigned int)(v_rdi);
    result = MiSetPfnModified(a1, a2, a3, (unsigned int)(v_stack_mA0));
    goto loc_002BA0ED;
loc_002BAA73:
    goto loc_002BA10D;
loc_002BAA7F:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 32))) >> (24));
    if ((((unsigned __int8)(result)) & (16)) == 0) goto loc_002BA118;
loc_002BAA9B:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 32))) >> (24));
    a4 = 0;
    a2 = 0;
    result = MiSetPfnRemovalRequested(a1, a2, a4 + 1, a4);
loc_002BAAD1:
    result = ExReleaseSpinLockExclusiveFromDpcLevel(result + 72, a2, a4 + 1, a4);
    goto loc_002BA38C;
loc_002BAAE3:
    a1 = 0;
    result = MiBadPageInserted(a1, a2, a4 + 1, a4);
    goto loc_002BA450;
}
```

## 5. (Beta) C Style

```c
int64_t MiInsertPageInList(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m108;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint8_t v_stack_m48;
    uint64_t v_stack_m50;
    uint8_t v_stack_m60;
    uint64_t v_stack_m68;
    uint8_t v_stack_m78;
    uint8_t v_stack_m7E;
    uint8_t v_stack_m7F;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint8_t v_stack_m90;
    uint64_t v_stack_m98;
    uint8_t v_stack_m9E;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint32_t v_stack_mAC;
    uint8_t v_stack_mAD;
    uint8_t v_stack_mAE;
    uint32_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint32_t v_stack_mD0;
    uint32_t v_stack_mD4;
    uint8_t v_stack_mD6;
    uint32_t v_stack_mD8;
    uint64_t v_stack_mE8;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p28;

    v_stack_p10 = local_rbx;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (224);
    result = (*(uint64_t *)(v_rip + 0xB5071F)) ^ (local_rsp);
    v_stack_m38 = result;
    v_stack_mD0 = Arg2;
    local_r12 = (Arg1) - (result);
    local_r12 = (local_r12) >> (4);
    local_r12 = (local_r12) * (result);
loc_002BA05A:
    Arg2 = 0;
    result = (*(uint64_t *)(arg1 + 0x28)) >> (43);
    local_rbx = 0;
    result = (uint32_t)((result) & (0x3FFULL));
    result = memset(v_stack_mA8, Arg2, 1 + 103, a4);
    v_stack_mD4 = 9;
    if (condition_is_below) goto loc_002BA487;
    if (local_r12 < (*(uint64_t *)(v_rip + 0xB7BB59))) goto loc_002BA0BB;
    result = (*(uint64_t *)(v_rip + 0xB7BB59)) + (0x800ULL);
    if (local_r12 < result) goto loc_002BA7AA;
loc_002BA0BB:
    if ((*(uint8_t *)(v_rip + 0xB82B24)) == 0) goto loc_002BA0DE;
    Arg1 = (local_r12) >> (9);
    if ((uint32_t)(*(uint8_t *)(*(uint64_t *)(v_rip + 0xB83175) + arg1 * 2)) != 0) goto loc_002BA824;
loc_002BA0DE:
    v_stack_mD4 = 9;
loc_002BA0E3:
    if ((((uint8_t)((uint32_t)(Arg2))) & (8)) != 0) goto loc_002BAA44;
loc_002BA0ED:
    if ((((uint8_t)((uint32_t)(Arg2))) & (4)) != 0) goto loc_002BA106;
    if ((((uint8_t)((uint32_t)(Arg2))) & (8)) == 0) goto loc_002BA6F0;
    goto loc_002BA10D;
loc_002BA106:
loc_002BA10D:
    local_rsi = (uint32_t)((0) & (1));
    if (condition_is_not_equal) goto loc_002BAA7F;
loc_002BA118:
    v_stack_mD8 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB7601E) + result * 8) + 0xC40 + 0xC)));
    v_stack_mC8 = *(uint64_t *)(*(uint64_t *)(v_rip + 0xB7601E) + result * 8) + 3136;
    v_stack_mC0 = 0;
    result = *(uint64_t *)(v_rip + 0xB83175);
    if ((uint32_t)(local_rsi) == 0) {
        Arg2 = *(uint32_t *)(v_rip + 0xD14F44);
        result = *(uint64_t *)(arg1 + 0x18);
        Arg2 = (Arg2) << (59);
        Arg1 = Arg2;
        Arg1 = (Arg1) ^ (result);
        Arg1 = (Arg1) & (result);
        Arg1 = (Arg1) ^ (Arg2);
        *(void **)(arg1 + 0x18) = Arg1;
    }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB7601E) + result * 8) + 0xC40 + 0xC)))) == 2) goto loc_002BA49B;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB7601E) + result * 8) + 0xC40 + 0xC)))) != 3) goto loc_002BA652;
    if (!sign_flag) goto loc_002BA645;
loc_002BA185:
    Arg1 = (uint32_t)(((uint32_t)(v_stack_mD0)) & (128));
    v_stack_mD8 = (uint32_t)(Arg1);
    if (condition_is_below) goto loc_002BA5FD;
    a3 = 0;
    a3 = ((uint32_t)(Arg1) == 0) ? 1 : 0;
    result = MiDetermineModifiedPageListHead(Arg1, *(uint64_t *)(*(uint64_t *)(v_rip + 0xB7601E) + result * 8), a3, a4);
    if (v_stack_mD8 == 0) {
        Arg2 = v_stack_mA8;
        Arg1 = result;
        result = MiLockPageListAndLastPage(Arg1, Arg2, a3, a4);
    }
    if (*(uint64_t *)(result) == 0) goto loc_002BA82D;
loc_002BA1E1:
loc_002BA1EC:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB7601E) + result * 8) + 0x4900)) >= 0x420ULL) goto loc_002BA283;
    v_stack_mD8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB73AB3)));
    result = 0;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB7601E) + result * 8) + 0x10)) + (0x3A60ULL);
    v_stack_mC8 = (uint32_t)(*(uint16_t *)(v_rip + 0xD0ADDB));
loc_002BA237:
    v_stack_mC0 = Arg1;
    if (0 >= ((uint32_t)(*(uint16_t *)(v_rip + 0xD0ADDB)))) goto loc_002BA8F7;
    a4 = 0;
loc_002BA252:
    if (0 > 1) goto loc_002BA862;
loc_002BA25F:
    if (0 >= ((uint32_t)((uint32_t)(v_stack_mD8)))) goto loc_002BA853;
    Arg1 = (0) + (0);
    Arg2 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB7601E) + result * 8) + 0x4900)) + (*(uint16_t *)(*(uint64_t *)(arg1) + arg1 * 8));
    if (Arg2 < 0x420ULL) goto loc_002BA639;
loc_002BA283:
    v_stack_mC0 = 0;
    v_stack_mC8 = 0;
loc_002BA291:
    local_rsi = (uint32_t)((0) & (4));
    if (condition_is_not_equal) goto loc_002BA48E;
    if (v_stack_mD4 != 9) goto loc_002BA7B4;
loc_002BA2A7:
loc_002BA2AB:
    if (v_stack_mA8 == 0) goto loc_002BA783;
loc_002BA2DA:
    if (v_stack_mA0 == 0) goto loc_002BA801;
    result = (*(uint64_t *)(v_stack_m98)) ^ (local_r12);
    result = (result) & (*(uint64_t *)(arg1));
    result = (result) ^ (local_r12);
    *(uint64_t *)(v_stack_m98) = result;
loc_002BA2FC:
    result = (*(uint64_t *)(arg1)) ^ (v_stack_m88);
    result = (result) & (*(uint64_t *)(arg1));
    result = (result) ^ (v_stack_m88);
    *(uint64_t *)(arg1) = result;
    result = (*(uint64_t *)(arg1 + 0x18)) ^ (v_stack_mA0);
    result = (result) & (*(uint64_t *)(arg1));
    result = (result) ^ (v_stack_mA0);
    *(uint64_t *)(arg1 + 0x18) = result;
    if (v_stack_m88 == 0) goto loc_002BA47E;
    Arg1 = (local_r12) ^ (*(uint64_t *)(v_stack_m80 + 0x18));
    Arg1 = (Arg1) & (*(uint64_t *)(arg1));
    Arg1 = (Arg1) ^ (local_r12);
    *(void **)(v_stack_m80 + 0x18) = Arg1;
loc_002BA339:
    if (result == (v_rip + 12006160)) goto loc_002BA945;
    v_stack_mD8 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20)));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x20))) >> (16));
    result = (uint8_t)(((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB7601E) + result * 8) + 0xC40 + 0xC)))) ^ ((uint8_t)(Arg1)));
    result = (uint8_t)((result) & (7));
    result = (uint8_t)((result) ^ ((uint8_t)(Arg1)));
    v_stack_mD6 = (uint8_t)(result);
    *(uint32_t *)(arg1 + 0x20) = (uint32_t)((uint32_t)(v_stack_mD8));
loc_002BA36A:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB7601E) + result * 8) + 0xC40 + 0xC)))) == 2) goto loc_002BA5C4;
loc_002BA37C:
    local_rsi = 0;
loc_002BA37E:
    if (v_stack_mC0 != 0) goto loc_002BAAD1;
loc_002BA38C:
    if (v_stack_mA8 == 0) goto loc_002BA87A;
    result = v_stack_mC0;
    if (v_stack_m90 != 0) {
        result = v_stack_m98;
    }
    if (v_stack_m78 != 0) {
        result = v_stack_m80;
    }
    if (v_stack_m60 != 0) {
        result = v_stack_m68;
    }
    if (v_stack_m48 != 0) {
        result = v_stack_m50;
    }
    if (((*(uint8_t *)(v_rip + 0xD0C708)) & (1)) != 0) goto loc_002BA8CC;
loc_002BA409:
loc_002BA415:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB7601E) + result * 8) + 0xC40 + 0xC)))) > 4) goto loc_002BA43E;
    if (((uint32_t)((uint32_t)(v_stack_mD4))) != 9) goto loc_002BA43E;
    result = v_stack_mC8;
    if (((0) & (5)) == 0) {
        a4 = 3;
        v_stack_mE8 = 0;
        a3 = (uint32_t)(a4);
        Arg2 = local_r12;
        Arg1 = *(uint64_t *)(*(uint64_t *)(v_rip + 0xB7601E) + result * 8);
        result = MiUpdateLargePageCandidateValue(Arg1, Arg2, a3, a4);
    }
    if (((0) & (2)) != 0) goto loc_002BA895;
loc_002BA447:
    if (0 >= 8) goto loc_002BAAE3;
loc_002BA450:
    Arg1 = (v_stack_m38) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, a3, a4);
    return result;
loc_002BA47E:
    *(uint64_t *)((uint32_t)(v_stack_mD4) + 0x18) = local_r12;
    goto loc_002BA339;
loc_002BA487:
    goto loc_002BA0E3;
loc_002BA48E:
    result = MiInsertDecayClusterTimer(Arg1, Arg2, a3, a4);
    goto loc_002BA2AB;
loc_002BA49B:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x20))) >> (24));
    if ((((uint8_t)(result)) & (64)) != 0) goto loc_002BA8AB;
loc_002BA4AE:
    if ((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x40)) != 0) goto loc_002BA9CE;
    result = MiGetPfnPriority(Arg1, Arg2, a3, a4);
    result = (uint32_t)(((uint32_t)(v_stack_mA8)) & (0x800ULL));
    v_stack_mA0 = (uint32_t)(result);
    if (condition_is_not_equal) goto loc_002BA55B;
    local_r15 = ((uint32_t)(v_stack_mD4)) * ((uint32_t)((uint32_t)(result)));
    local_r15 = (local_r15) + (0xCC0ULL);
    local_r15 = (local_r15) + (*(uint64_t *)(*(uint64_t *)(v_rip + 0xB7601E) + result * 8));
    if (((uint32_t)((uint32_t)((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x40))))) >= 4) goto loc_002BA55B;
    if (((uint32_t)((uint32_t)(v_stack_mAC))) != 9) goto loc_002BA55B;
    result = (*(uint64_t *)(arg1 + 0x28)) >> (63);
    Arg1 = (uint32_t)(0x1C40ULL);
    if ((uint8_t)(result) == 0) { Arg1 = (uint32_t)((uint32_t)(0x3FC0ULL)); }
    local_rsi = (1) + 1;
    if (local_rsi <= 0x420ULL) goto loc_002BA983;
loc_002BA536:
    local_rsi = (local_rsi) - 1;
    if (local_rsi == (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB7601E) + result * 8) + 0x4100))) goto loc_002BAA30;
    if (local_rsi == (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB7601E) + result * 8) + 0x4108))) goto loc_002BAA30;
loc_002BA553:
loc_002BA55B:
    v_stack_mA0 = local_r15;
    if (((v_stack_mA8) & (128)) != 0) goto loc_002BA291;
    if (((uint32_t)((uint32_t)(v_stack_mAC))) < 9) goto loc_002BA80A;
loc_002BA574:
    v_stack_mB8 = v_stack_m80;
    v_stack_mC0 = 0;
    result = MiSynchronizeFastPageInsert(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB7601E) + result * 8), local_r15, Arg1, (uint32_t)((uint32_t)((uint32_t)(v_stack_mAC))));
    if (v_stack_m80 != 0) goto loc_002BA291;
    if (((uint32_t)(v_stack_m7E)) == 3) goto loc_002BA291;
    result = MiRebuildStandbyLookasideList(Arg1, v_stack_m7E, v_stack_m7F, (uint32_t)((uint32_t)((uint32_t)(v_stack_mAC))));
    goto loc_002BA291;
loc_002BA5C4:
    if (((uint32_t)(local_r15)) < 9) goto loc_002BA7D0;
    if ((uint32_t)(local_rsi) != 0) goto loc_002BA8F0;
    a3 = v_stack_m80;
    if (v_stack_m80 == ((uint8_t)(local_rsi))) { a3 = 0; }
    result = MiInsertSecondaryListStandbyPage(Arg1, 0 + 9, a3, (uint32_t)((uint32_t)((uint32_t)(v_stack_mAC))));
loc_002BA5F4:
    goto loc_002BA37E;
loc_002BA5FD:
    local_r15 = (local_r15) * ((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB7601E) + result * 8) + 0x44C0) + 0x18)) + 64);
    local_r15 = (local_r15) + (*(uint64_t *)(*(uint64_t *)(v_rip + 0xB7601E) + result * 8));
    if ((uint32_t)((uint32_t)(v_stack_mA8)) == 0) goto loc_002BA6DE;
loc_002BA61A:
    local_rsi = (uint8_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB7601E) + result * 8) + 0x44C0) + 0x18))) ^ ((uint8_t)(*(uint8_t *)(arg1 + 0x24))));
    local_rsi = (uint8_t)((local_rsi) & (15));
    local_rsi = (uint8_t)((local_rsi) ^ ((uint8_t)(*(uint8_t *)(arg1 + 0x24))));
    *(uint8_t *)(arg1 + 0x24) = (uint8_t)(local_rsi);
    goto loc_002BA1EC;
loc_002BA639:
    a4 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_mAC)))) + 1);
    goto loc_002BA25F;
loc_002BA645:
    goto loc_002BA185;
loc_002BA652:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB7601E) + result * 8) + 0xC40 + 0xC)))) != 4) goto loc_002BAA9B;
    if (*(uint64_t *)(v_rip + 0xB7361E) == 0) goto loc_002BA675;
    result = *(uint64_t *)(arg1 + 0x10);
    if ((((uint8_t)(*(uint64_t *)(arg1 + 0x10))) & (16)) == 0) {
        Arg1 = ~(*(uint64_t *)(v_rip + 0xB7361E));
        result = (*(uint64_t *)(arg1 + 0x10)) & (Arg1);
    }
    result = (result) >> (16);
    v_stack_m98 = *(uint64_t *)(result);
    result = *(uint64_t *)(*(uint64_t *)(v_rip + 0xB7601E) + result * 8) + 16320;
    if (sign_flag) {
        result = *(uint64_t *)(*(uint64_t *)(v_rip + 0xB7601E) + result * 8) + 7232;
    }
    v_stack_m90 = local_r15 + 32;
    result = ExAcquireSpinLockExclusiveAtDpcLevel(local_r15 + 32, 0 + 9, *(uint64_t *)(*(uint64_t *)(v_rip + 0xB7601E) + result * 8) + 19616, a4);
    result = ExAcquireSpinLockExclusiveAtDpcLevel(*(uint64_t *)(result) + 72, 0 + 9, *(uint64_t *)(*(uint64_t *)(v_rip + 0xB7601E) + result * 8) + 19616, a4);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(result) + 0x38)))) & (8)) != 0) goto loc_002BA291;
    result = ExReleaseSpinLockExclusiveFromDpcLevel(*(uint64_t *)(result) + 72, 0 + 9, *(uint64_t *)(*(uint64_t *)(v_rip + 0xB7601E) + result * 8) + 19616, a4);
    result = ExReleaseSpinLockExclusiveFromDpcLevel(v_stack_m90, 0 + 9, *(uint64_t *)(*(uint64_t *)(v_rip + 0xB7601E) + result * 8) + 19616, a4);
    goto loc_002BA185;
loc_002BA6DE:
    result = MiLockPageListAndLastPage(local_r15, v_stack_m80, *(uint64_t *)(*(uint64_t *)(v_rip + 0xB7601E) + result * 8) + 19616, a4);
    goto loc_002BA61A;
loc_002BA6F0:
    if (((3) & (16)) != 0) goto loc_002BA939;
    if (condition_is_below) goto loc_002BA9BB;
    if (condition_is_above_or_equal) goto loc_002BAA73;
    result = (*(uint64_t *)(arg1 + 0x28)) >> (43);
    result = (uint32_t)((result) & (0x3FFULL));
    result = MI_NODE_FROM_PFN(Arg1, v_stack_m80, *(uint64_t *)(*(uint64_t *)(v_rip + 0xB7601E) + result * 8) + 19616, a4);
    Arg2 = (v_stack_m80) * ((uint32_t)((uint32_t)(result)));
    Arg1 = ((uint32_t)((uint32_t)(result))) * ((int32_t)((uint32_t)(local_r15)));
    Arg2 = (Arg2) + (Arg1);
    Arg1 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB7596F) + result * 8) + 0x10)) + (0x3D50ULL);
    Arg1 = (Arg1) + (Arg2);
    result = MiGetSlabRepurposedStandbyListWorker(Arg1, Arg1, *(uint64_t *)(*(uint64_t *)(v_rip + 0xB7601E) + result * 8) + 19616, a4);
    if (result != -1) goto loc_002BA10D;
    Arg2 = 0;
    result = MiRestoreTransitionPte(Arg1, Arg2, *(uint64_t *)(*(uint64_t *)(v_rip + 0xB7601E) + result * 8) + 19616, a4);
    result = MiInsertPageInFreeOrZeroedList(local_r12, 2, *(uint64_t *)(*(uint64_t *)(v_rip + 0xB7601E) + result * 8) + 19616, a4);
    goto loc_002BA450;
loc_002BA783:
    Arg2 = (*(uint64_t *)(result + 0x18) + *(uint64_t *)(result + 0x18) * 2) << (4);
    Arg2 = (Arg2) + (result);
    a4 = 0;
    goto loc_002BA2DA;
loc_002BA7AA:
    goto loc_002BA0E3;
loc_002BA7B4:
    if (((v_stack_mA8) & (0x800ULL)) != 0) goto loc_002BA2A7;
    if (((uint32_t)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB7596F) + result * 8))) != 2) goto loc_002BA2A7;
    goto loc_002BA2AB;
loc_002BA7D0:
    if (((uint32_t)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB7596F) + result * 8))) < 2) goto loc_002BA835;
    a3 = v_stack_m80;
    if (v_stack_m80 == 0) { a3 = 0; }
    result = MiInsertSecondaryListStandbyPage(Arg1, (uint32_t)((uint32_t)(result)), a3, a4);
    goto loc_002BA37E;
loc_002BA801:
    *(uint64_t *)(result + 0x10) = local_r12;
    goto loc_002BA2FC;
loc_002BA80A:
    if ((uint32_t)(result) == 0) goto loc_002BA574;
    result = MiLockPageListAndLastPage(result, v_stack_m80, a3, a4);
    goto loc_002BA291;
loc_002BA824:
    goto loc_002BA0DE;
loc_002BA82D:
    local_rbx = (uint32_t)((4) | (2));
    goto loc_002BA1E1;
loc_002BA835:
    v_stack_mB0 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x20))) >> (24));
    result = (uint8_t)((result) | (8));
    v_stack_mAD = (uint8_t)(result);
    *(uint32_t *)(arg1 + 0x20) = (uint32_t)((uint32_t)(v_stack_mB0));
    goto loc_002BA37C;
loc_002BA853:
    local_r11 = (v_stack_m28) + 1;
    local_rsi = (0) + (8);
    a4 = 0;
    goto loc_002BA252;
loc_002BA862:
    Arg1 = (v_stack_m98) + (0xDF80ULL);
    result = (uint32_t)(((uint32_t)(v_stack_mB0)) + 1);
    goto loc_002BA237;
loc_002BA87A:
    if (sign_flag) goto loc_002BA415;
    Arg1 = (v_stack_mA0) + (32);
    result = ExReleaseSpinLockExclusiveFromDpcLevel(Arg1, v_stack_m80, a3, (uint32_t)(v_stack_mA0));
    goto loc_002BA415;
loc_002BA895:
    a3 = 0;
    Arg2 = 0;
    result = KeSetEvent(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB7601E) + result * 8) + 928, Arg2, a3, (uint32_t)(v_stack_mA0));
    goto loc_002BA447;
loc_002BA8AB:
    if (((uint32_t)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB7601E) + result * 8) + 928)) != 9) goto loc_002BA4AE;
    Arg2 = 0;
    result = MiRestoreTransitionPte(Arg1, Arg2, a3, (uint32_t)(v_stack_mA0));
    v_stack_mA8 = 32;
    goto loc_002BA05A;
loc_002BA8CC:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC53586))) != 0) goto loc_002BA409;
    result = ExpReleaseSpinLockSharedFromDpcLevelInstrumented(result + 32, v_stack_p28, a3, (uint32_t)(v_stack_mA0));
    goto loc_002BA415;
loc_002BA8F0:
    local_rsi = 0;
    goto loc_002BA5F4;
loc_002BA8F7:
    if ((*(uint64_t *)(a3)) >= 16) {
        Arg2 = -1;
        Arg1 = *(uint64_t *)(*(uint64_t *)(v_rip + 0xB7601E) + result * 8);
        result = MiWakeModifiedPageWriter(Arg1, Arg2, a3, (uint32_t)(v_stack_mA0));
    }
    result = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB7601E) + result * 8) + 0x4BC0)) - (*(uint64_t *)(a3));
    if (result < 16) goto loc_002BA283;
    a3 = 0;
    Arg2 = 0;
    result = KeSetEvent(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB7601E) + result * 8) + 840, Arg2, a3, (uint32_t)(v_stack_mA0));
    goto loc_002BA283;
loc_002BA939:
    goto loc_002BA10D;
loc_002BA945:
    v_stack_mB0 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x20))) >> (16));
    result = (uint8_t)((result) & (250));
    result = (uint8_t)((result) | (2));
    v_stack_mAE = (uint8_t)(result);
    *(uint32_t *)(arg1 + 0x20) = (uint32_t)((uint32_t)(v_stack_mB0));
    v_stack_mB0 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x20))) >> (24));
    result = (uint8_t)((result) | (16));
    v_stack_mAD = (uint8_t)(result);
    *(uint32_t *)(arg1 + 0x20) = (uint32_t)((uint32_t)(v_stack_mB0));
    result = MiWakeFileOnlyReaper(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB7601E) + result * 8) + 840, Arg2, a3, (uint32_t)(v_stack_mA0));
    goto loc_002BA36A;
loc_002BA983:
    if ((*(uint64_t *)(a3)) == 160) goto loc_002BA9F0;
    if ((*(uint64_t *)(a3)) == 0x420ULL) goto loc_002BAA3D;
    if ((*(uint64_t *)(a3)) == 34) goto loc_002BA9EE;
    if ((*(uint64_t *)(a3)) != 288) goto loc_002BA536;
    result = MiSlabDemotionLowMemoryConditionUpdate(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB7601E) + result * 8), (uint32_t)((uint32_t)(result)), a3, (uint32_t)(v_stack_mA0));
    goto loc_002BA536;
loc_002BA9BB:
    result = MiGetEnclavePageList(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB7601E) + result * 8), local_r12, a3, (uint32_t)(v_stack_mA0));
    goto loc_002BA10D;
loc_002BA9CE:
    v_stack_mA0 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x20))) >> (16));
    result = (uint8_t)((result) & (250));
    result = (uint8_t)((result) | (2));
    v_stack_m9E = (uint8_t)(result);
    *(uint32_t *)(arg1 + 0x20) = (uint32_t)((uint32_t)(v_stack_mA0));
    goto loc_002BA450;
loc_002BA9EE:
    result = 0;
loc_002BA9F0:
    result = (result) << (5);
    result = ExAcquireSpinLockExclusiveAtDpcLevel(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB7601E) + result * 8) + 16192, local_r12, a3, (uint32_t)(v_stack_mA0));
    a3 = 0;
    Arg2 = 0;
    result = KeSetEvent(result + *(uint64_t *)(*(uint64_t *)(v_rip + 0xB7601E) + result * 8) * 1 + 16200, Arg2, a3, (uint32_t)(v_stack_mA0));
    result = ExReleaseSpinLockExclusiveFromDpcLevel(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB7601E) + result * 8) + 16192, Arg2, a3, (uint32_t)(v_stack_mA0));
    goto loc_002BA536;
loc_002BAA30:
    result = MiUpdateAvailableEventsAtDpc(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB7601E) + result * 8), Arg2, a3, (uint32_t)(v_stack_mA0));
    goto loc_002BA553;
loc_002BAA3D:
    goto loc_002BA9F0;
loc_002BAA44:
    if ((((uint8_t)(local_rbx)) & (1)) == 0) goto loc_002BA0ED;
    if ((*(uint8_t *)(v_rip + 0xB731EC)) == 0) goto loc_002BA0ED;
    local_rdi = (uint32_t)(((uint32_t)(v_stack_mB0)) & (0xFFFFFFF7ULL));
    Arg2 = 0;
    local_rdi = (uint32_t)((local_rdi) | (4));
    v_stack_mA8 = (uint32_t)(local_rdi);
    result = MiSetPfnModified(Arg1, Arg2, a3, (uint32_t)(v_stack_mA0));
    goto loc_002BA0ED;
loc_002BAA73:
    goto loc_002BA10D;
loc_002BAA7F:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x20))) >> (24));
    if ((((uint8_t)(result)) & (16)) == 0) goto loc_002BA118;
loc_002BAA9B:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x20))) >> (24));
    a4 = 0;
    Arg2 = 0;
    result = MiSetPfnRemovalRequested(Arg1, Arg2, a4 + 1, a4);
loc_002BAAD1:
    result = ExReleaseSpinLockExclusiveFromDpcLevel(result + 72, Arg2, a4 + 1, a4);
    goto loc_002BA38C;
loc_002BAAE3:
    Arg1 = 0;
    result = MiBadPageInserted(Arg1, Arg2, a4 + 1, a4);
    goto loc_002BA450;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x0` | `64` | `W` |
| `Arg1` | `+ 0x10` | `32` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x18` | `64` | `W` |
| `Arg1` | `+ 0x20` | `32` | `R` |
| `Arg1` | `+ 0x20` | `32` | `W` |
| `Arg1` | `+ 0x24` | `8` | `R` |
| `Arg1` | `+ 0x24` | `8` | `W` |
| `Arg1` | `+ 0x28` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002BA000&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
