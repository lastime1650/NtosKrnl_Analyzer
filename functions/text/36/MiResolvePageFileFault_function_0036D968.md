# MiResolvePageFileFault

- RVA: `0x0036D968`–`0x0036F0F3` (길이 `6,027` bytes)
- VA: `0x000000014036D968`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0007A640`
- 디코드: `1,389`개 명령, `6,027/6,027` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **71**; 고유 호출 대상: **43**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **8**

### Outgoing calls
- `0x0036D9BA` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x0036DA96` → [MiGetSystemRegionType](../28/MiGetSystemRegionType_function_0028EC80.md) (function, `0x0028EC80`)
- `0x0036DB82` → [MiComputeFaultNode](../2B/MiComputeFaultNode_function_002B60C0.md) (function, `0x002B60C0`)
- `0x0036DC62` → [MiLockVadTree](../27/MiLockVadTree_function_0027C0F0.md) (function, `0x0027C0F0`)
- `0x0036DC6B` → [MiLocateAddress](../31/MiLocateAddress_function_003168D0.md) (function, `0x003168D0`)
- `0x0036DC7C` → [MiUnlockVadTree](../29/MiUnlockVadTree_function_00297020.md) (function, `0x00297020`)
- `0x0036DD02` → [MiAllocateInPageSupport](MiAllocateInPageSupport_function_0036F100.md) (function, `0x0036F100`)
- `0x0036DD1A` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x0036DD66` → [MiObtainFaultCharges](../28/MiObtainFaultCharges_function_0028AEB0.md) (function, `0x0028AEB0`)
- `0x0036DDF7` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x0036DF24` → [MiLockSetPfnPriority](../29/MiLockSetPfnPriority_function_00294E10.md) (function, `0x00294E10`)
- `0x0036DF47` → [MiAdvanceFaultList](MiAdvanceFaultList_function_003637A0.md) (function, `0x003637A0`)
- `0x0036DFA6` → [MiSwizzleInvalidPte](../28/MiSwizzleInvalidPte_function_0028F5E0.md) (function, `0x0028F5E0`)
- `0x0036E07F` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x0036E0BB` → [MiInitializeReadInProgressPfn](../2B/MiInitializeReadInProgressPfn_function_002B6990.md) (function, `0x002B6990`)
- `0x0036E0DA` → [MiObtainProtoReference](../31/MiObtainProtoReference_function_00318178.md) (function, `0x00318178`)
- `0x0036E0E9` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x0036E11E` → [PsGetIoPriorityThread](../34/PsGetIoPriorityThread_function_00343930.md) (function, `0x00343930`)
- `0x0036E150` → [MiUnlockProtoPoolPage](../24/MiUnlockProtoPoolPage_function_00246090.md) (function, `0x00246090`)
- `0x0036E187` → [MiReleaseFreshPage](../33/MiReleaseFreshPage_function_00334AE0.md) (function, `0x00334AE0`)
- `0x0036E198` → [MiSufficientAvailablePages](MiSufficientAvailablePages_function_0036D0B0.md) (function, `0x0036D0B0`)
- `0x0036E212` → [MiGetPagingFileOffset](MiGetPagingFileOffset_function_0036F530.md) (function, `0x0036F530`)
- `0x0036E248` → [MI_CLEAR_PTE_BITS_FOR_READ_CLUSTER](MI_CLEAR_PTE_BITS_FOR_READ_CLUSTER_function_0036D890.md) (function, `0x0036D890`)
- `0x0036E26C` → [MiUpdatePageFileHighInPte](MiUpdatePageFileHighInPte_function_0036D840.md) (function, `0x0036D840`)
- `0x0036E277` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x0036E290` → [MI_CLEAR_PTE_BITS_FOR_READ_CLUSTER](MI_CLEAR_PTE_BITS_FOR_READ_CLUSTER_function_0036D890.md) (function, `0x0036D890`)
- `0x0036E2F2` → [MiGetPagingFileOffset](MiGetPagingFileOffset_function_0036F530.md) (function, `0x0036F530`)
- `0x0036E313` → [MI_CLEAR_PTE_BITS_FOR_READ_CLUSTER](MI_CLEAR_PTE_BITS_FOR_READ_CLUSTER_function_0036D890.md) (function, `0x0036D890`)
- `0x0036E337` → [MiUpdatePageFileHighInPte](MiUpdatePageFileHighInPte_function_0036D840.md) (function, `0x0036D840`)
- `0x0036E342` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x0036E357` → [MI_CLEAR_PTE_BITS_FOR_READ_CLUSTER](MI_CLEAR_PTE_BITS_FOR_READ_CLUSTER_function_0036D890.md) (function, `0x0036D890`)
- `0x0036E3E6` → [MiSwizzleInvalidPte](../28/MiSwizzleInvalidPte_function_0028F5E0.md) (function, `0x0028F5E0`)
- `0x0036E4CB` → [MiGetCurrentSlabIdentity](../3B/MiGetCurrentSlabIdentity_function_003BD020.md) (function, `0x003BD020`)
- `0x0036E505` → [MiProtectionToCacheAttribute](../2B/MiProtectionToCacheAttribute_function_002B8530.md) (function, `0x002B8530`)
- `0x0036E537` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0036E593` → [MiInitializePageChainPacket](../43/MiInitializePageChainPacket_function_004367C0.md) (function, `0x004367C0`)
- `0x0036E59C` → [MiGetPageChain](../33/MiGetPageChain_function_00330130.md) (function, `0x00330130`)
- `0x0036E730` → [MiGetAvailablePagesBelowPriority](../34/MiGetAvailablePagesBelowPriority_function_0034D340.md) (function, `0x0034D340`)
- `0x0036E76A` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x0036E772` → [MI_PROTO_FORMAT_COMBINED](../22/MI_PROTO_FORMAT_COMBINED_function_0022F720.md) (function, `0x0022F720`)
- `0x0036E7A4` → [MiIsPteInStore](MiIsPteInStore_function_00362460.md) (function, `0x00362460`)
- `0x0036E7BB` → [MiUnlockProtoPoolPage](../24/MiUnlockProtoPoolPage_function_00246090.md) (function, `0x00246090`)
- `0x0036E7DA` → [MiSetInPagePrefetchPriority](MiSetInPagePrefetchPriority_function_0036A974.md) (function, `0x0036A974`)
- `0x0036E826` → [MiComputeFaultCluster](MiComputeFaultCluster_function_003635B4.md) (function, `0x003635B4`)
- `0x0036E897` → [MiFreeInPageSupportBlock](../2B/MiFreeInPageSupportBlock_function_002B5900.md) (function, `0x002B5900`)
- `0x0036E8B4` → [MiReturnFaultCharges](MiReturnFaultCharges_function_0036D928.md) (function, `0x0036D928`)
- `0x0036E8E2` → [MiReturnFaultCharges](MiReturnFaultCharges_function_0036D928.md) (function, `0x0036D928`)
- `0x0036E8F4` → [MiGetPagingFileOffset](MiGetPagingFileOffset_function_0036F530.md) (function, `0x0036F530`)
- `0x0036EA01` → [MiSharedVaToPartition](../2B/MiSharedVaToPartition_function_002B6700.md) (function, `0x002B6700`)
- `0x0036EA1B` → [MiLockVadTree](../27/MiLockVadTree_function_0027C0F0.md) (function, `0x0027C0F0`)
- `0x0036EA27` → [MiLocateAddress](../31/MiLocateAddress_function_003168D0.md) (function, `0x003168D0`)
- `0x0036EA3A` → [MiUnlockVadTree](../29/MiUnlockVadTree_function_00297020.md) (function, `0x00297020`)
- `0x0036EA6A` → [MiGetProtoPteAddress](../32/MiGetProtoPteAddress_function_0032E970.md) (function, `0x0032E970`)
- `0x0036EAE0` → [MiIsStoreProcess](../2B/MiIsStoreProcess_function_002B62E0.md) (function, `0x002B62E0`)
- `0x0036EB79` → [MiGetPagingFileOffset](MiGetPagingFileOffset_function_0036F530.md) (function, `0x0036F530`)
- `0x0036EBE7` → [MiFlowThroughInsertNode](../4B/MiFlowThroughInsertNode_function_004B560C.md) (function, `0x004B560C`)
- `0x0036EBF8` → [MiReduceMdl](../44/MiReduceMdl_function_0044BA80.md) (function, `0x0044BA80`)
- `0x0036EC65` → [MiLockVadTree](../27/MiLockVadTree_function_0027C0F0.md) (function, `0x0027C0F0`)
- `0x0036EC6E` → [MiLocateAddress](../31/MiLocateAddress_function_003168D0.md) (function, `0x003168D0`)
- `0x0036EC81` → [MiUnlockVadTree](../29/MiUnlockVadTree_function_00297020.md) (function, `0x00297020`)
- `0x0036ECE5` → [MiReleaseFreshPageAtDpc](../33/MiReleaseFreshPageAtDpc_function_00334B50.md) (function, `0x00334B50`)
- `0x0036ED1D` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x0036ED6C` → [MiKernelStackVaToStackNode](../34/MiKernelStackVaToStackNode_function_00348A4C.md) (function, `0x00348A4C`)
- `0x0036EEB3` → [MiUnlockProtoPoolPage](../24/MiUnlockProtoPoolPage_function_00246090.md) (function, `0x00246090`)
- `0x0036EEC6` → [MiIsPteInStore](MiIsPteInStore_function_00362460.md) (function, `0x00362460`)
- `0x0036EF56` → [MiUnlockProtoPoolPage](../24/MiUnlockProtoPoolPage_function_00246090.md) (function, `0x00246090`)
- `0x0036EFA3` → [PsReferencePartitionSafe](../3B/PsReferencePartitionSafe_function_003BA6C0.md) (function, `0x003BA6C0`)
- `0x0036F036` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0036F053` → [PsDereferencePartition](../34/PsDereferencePartition_function_00342E70.md) (function, `0x00342E70`)
- `0x0036F073` → [MiUnlockProtoPoolPage](../24/MiUnlockProtoPoolPage_function_00246090.md) (function, `0x00246090`)
- `0x0036F0E9` → [MiReadFromMemoryPagefile](../4D/MiReadFromMemoryPagefile_function_004DB6B0.md) (function, `0x004DB6B0`)

### Direct callers
- [sub_00320866](../32/Unknown_function_00320866.md) at `0x00320C52`
- [MiResolveProtoPteFault](../32/MiResolveProtoPteFault_function_00321750.md) at `0x00322333`
- [MiIssueFlowThroughFault](MiIssueFlowThroughFault_function_00369D64.md) at `0x00369E22`

### Static image references
- `0x0036DA02` → RVA `0x00E2DC80` (`.data`; read)
- `0x0036DA4D` → RVA `0x00E30088` (`.data`; read)
- `0x0036DCB8` → RVA `0x00E37398` (`.data`; read)
- `0x0036E6D8` → RVA `0x00014578` (`.rdata`; read)
- `0x0036E6FB` → RVA `0x00E37438` (`.data`; read)
- `0x0036E9ED` → RVA `0x00E37398` (`.data`; write)
- `0x0036ED48` → RVA `0x00FC5200` (`ALMOSTRO`; read)
- `0x0036ED7A` → RVA `0x00E38D00` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **14**
  - `0x0036EEBC` → [sub_006E3BD0](../6E/Unknown_function_006E3BD0.md) (`tail-transfer`)
  - `0x0036EED3` → [sub_006E3BD0](../6E/Unknown_function_006E3BD0.md) (`tail-transfer`)
  - `0x0036EF3A` → [sub_006E3BD0 + 0x21](../6E/Unknown_function_006E3BD0.md) (`tail-transfer`)
  - `0x0036EF4E` → [sub_006E3BD0 + 0x19](../6E/Unknown_function_006E3BD0.md) (`tail-transfer`)
  - `0x0036EF5C` → [sub_006E3BD0 + 0x19](../6E/Unknown_function_006E3BD0.md) (`tail-transfer`)
  - `0x0036EF7F` → [sub_006E3BD0 + 0x3F](../6E/Unknown_function_006E3BD0.md) (`tail-transfer`)
  - `0x0036EF88` → [sub_006E3BD0 + 0x3F](../6E/Unknown_function_006E3BD0.md) (`tail-transfer`)
  - `0x0036EF97` → [sub_006E3BD0 + 0x3F](../6E/Unknown_function_006E3BD0.md) (`tail-transfer`)
  - `0x0036EFAA` → [sub_006E3BD0 + 0x89](../6E/Unknown_function_006E3BD0.md) (`tail-transfer`)
  - `0x0036F01B` → [sub_006E3BD0 + 0x90](../6E/Unknown_function_006E3BD0.md) (`tail-transfer`)
  - `0x0036F03F` → [sub_006E3BD0 + 0x90](../6E/Unknown_function_006E3BD0.md) (`tail-transfer`)
  - `0x0036F0AE` → [sub_006E3BD0 + 0xAE](../6E/Unknown_function_006E3BD0.md) (`tail-transfer`)
  - `0x0036F0B6` → [sub_006E3BD0 + 0xAE](../6E/Unknown_function_006E3BD0.md) (`tail-transfer`)
  - `0x0036F0C5` → [sub_006E3BD0 + 0xAE](../6E/Unknown_function_006E3BD0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0036D968  48 8B C4                        mov rax, rsp
0036D96B  4C 89 48 20                     mov qword ptr [rax + 0x20], r9
0036D96F  4C 89 40 18                     mov qword ptr [rax + 0x18], r8
0036D973  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
0036D977  48 89 48 08                     mov qword ptr [rax + 8], rcx
0036D97B  55                              push rbp
0036D97C  53                              push rbx
0036D97D  56                              push rsi
0036D97E  57                              push rdi
0036D97F  41 54                           push r12
0036D981  41 55                           push r13
0036D983  41 56                           push r14
0036D985  41 57                           push r15
0036D987  48 8D A8 08 FF FF FF            lea rbp, [rax - 0xf8]
0036D98E  48 81 EC B8 01 00 00            sub rsp, 0x1b8
0036D995  4C 8B 21                        mov r12, qword ptr [rcx]
0036D998  33 FF                           xor edi, edi
0036D99A  4C 8B 69 38                     mov r13, qword ptr [rcx + 0x38]
0036D99E  8B F7                           mov esi, edi
0036D9A0  4C 8B 79 10                     mov r15, qword ptr [rcx + 0x10]
0036D9A4  4C 8B F2                        mov r14, rdx
0036D9A7  48 8B CA                        mov rcx, rdx
0036D9AA  48 89 7D 10                     mov qword ptr [rbp + 0x10], rdi
0036D9AE  48 89 7D 28                     mov qword ptr [rbp + 0x28], rdi
0036D9B2  4C 89 65 B0                     mov qword ptr [rbp - 0x50], r12
0036D9B6  4C 89 6D 08                     mov qword ptr [rbp + 8], r13
0036D9BA  E8 E1 4E F1 FF                  call 0x1402828a0
0036D9BF  48 8B D8                        mov rbx, rax
0036D9C2  48 89 45 00                     mov qword ptr [rbp], rax
0036D9C6  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0036D9CF  48 89 45 20                     mov qword ptr [rbp + 0x20], rax
0036D9D3  F6 80 A8 05 00 00 04            test byte ptr [rax + 0x5a8], 4
0036D9DA  0F 85 80 14 00 00               jne 0x14036ee60
0036D9E0  BA 00 08 00 00                  mov edx, 0x800
0036D9E5  49 B8 00 00 00 00 00 DE FF FF   movabs r8, 0xffffde0000000000
0036D9EF  49 B9 FF FF FF FF FF 00 00 00   movabs r9, 0xffffffffff
0036D9F9  48 85 DA                        test rdx, rbx
0036D9FC  0F 84 E8 01 00 00               je 0x14036dbea
0036DA02  48 8B 0D 77 02 AC 00            mov rcx, qword ptr [rip + 0xac0277]
0036DA09  48 8B C3                        mov rax, rbx
0036DA0C  48 85 C9                        test rcx, rcx
0036DA0F  74 12                           je 0x14036da23
0036DA11  F6 C3 10                        test bl, 0x10
0036DA14  0F 85 2F 02 00 00               jne 0x14036dc49
0036DA1A  48 8B C1                        mov rax, rcx
0036DA1D  48 F7 D0                        not rax
0036DA20  48 23 C3                        and rax, rbx
0036DA23  48 C1 E8 0C                     shr rax, 0xc
0036DA27  49 23 C1                        and rax, r9
0036DA2A  48 8D 14 40                     lea rdx, [rax + rax*2]
0036DA2E  48 C1 E2 04                     shl rdx, 4
0036DA32  49 8B C0                        mov rax, r8
0036DA35  48 03 D0                        add rdx, rax
0036DA38  BE 10 00 00 00                  mov esi, 0x10
0036DA3D  48 89 55 C8                     mov qword ptr [rbp - 0x38], rdx
0036DA41  48 8B 42 10                     mov rax, qword ptr [rdx + 0x10]
0036DA45  48 89 45 88                     mov qword ptr [rbp - 0x78], rax
0036DA49  48 8B 42 28                     mov rax, qword ptr [rdx + 0x28]
0036DA4D  48 8B 0D 34 26 AC 00            mov rcx, qword ptr [rip + 0xac2634]
0036DA54  48 8B BD 10 01 00 00            mov rdi, qword ptr [rbp + 0x110]
0036DA5B  48 C1 E8 2B                     shr rax, 0x2b
0036DA5F  25 FF 03 00 00                  and eax, 0x3ff
0036DA64  48 8B 0C C1                     mov rcx, qword ptr [rcx + rax*8]
0036DA68  BA 00 08 00 00                  mov edx, 0x800
0036DA6D  45 33 ED                        xor r13d, r13d
0036DA70  48 89 4C 24 78                  mov qword ptr [rsp + 0x78], rcx
0036DA75  4C 21 6D F0                     and qword ptr [rbp - 0x10], r13
0036DA79  4C 89 6D A0                     mov qword ptr [rbp - 0x60], r13
0036DA7D  45 8D 75 01                     lea r14d, [r13 + 1]
0036DA81  45 8D 65 02                     lea r12d, [r13 + 2]
0036DA85  44 89 65 B8                     mov dword ptr [rbp - 0x48], r12d
0036DA89  45 84 FE                        test r14b, r15b
0036DA8C  0F 85 B0 10 00 00               jne 0x14036eb42
0036DA92  48 8B 4D B0                     mov rcx, qword ptr [rbp - 0x50]
0036DA96  E8 E5 11 F2 FF                  call 0x14028ec80
0036DA9B  8B C8                           mov ecx, eax
0036DA9D  45 84 FE                        test r14b, r15b
0036DAA0  0F 84 74 01 00 00               je 0x14036dc1a
0036DAA6  49 83 E7 FE                     and r15, 0xfffffffffffffffe
0036DAAA  41 80 3F 04                     cmp byte ptr [r15], 4
0036DAAE  0F 85 66 01 00 00               jne 0x14036dc1a
0036DAB4  49 8B 47 30                     mov rax, qword ptr [r15 + 0x30]
0036DAB8  41 83 CC 08                     or r12d, 8
0036DABC  41 BE 81 00 00 00               mov r14d, 0x81
0036DAC2  4C 89 7D A0                     mov qword ptr [rbp - 0x60], r15
0036DAC6  4D 8B EF                        mov r13, r15
0036DAC9  44 89 65 B8                     mov dword ptr [rbp - 0x48], r12d
0036DACD  48 8B 88 20 02 00 00            mov rcx, qword ptr [rax + 0x220]
0036DAD4  48 8B 05 AD 25 AC 00            mov rax, qword ptr [rip + 0xac25ad]
0036DADB  0F B7 91 AE 04 00 00            movzx edx, word ptr [rcx + 0x4ae]
0036DAE2  48 8B 0C D0                     mov rcx, qword ptr [rax + rdx*8]
0036DAE6  48 89 4C 24 78                  mov qword ptr [rsp + 0x78], rcx
0036DAEB  4C 8B 7D B0                     mov r15, qword ptr [rbp - 0x50]
0036DAEF  40 F6 C6 20                     test sil, 0x20
0036DAF3  0F 85 9A 0C 00 00               jne 0x14036e793
0036DAF9  4C 8B 65 20                     mov r12, qword ptr [rbp + 0x20]
0036DAFD  41 BD 01 00 00 00               mov r13d, 1
0036DB03  48 8B 8D 08 01 00 00            mov rcx, qword ptr [rbp + 0x108]
0036DB0A  83 65 D0 00                     and dword ptr [rbp - 0x30], 0
0036DB0E  44 89 6D 80                     mov dword ptr [rbp - 0x80], r13d
0036DB12  4D 8B A4 24 B8 00 00 00         mov r12, qword ptr [r12 + 0xb8]
0036DB1A  48 89 4D 90                     mov qword ptr [rbp - 0x70], rcx
0036DB1E  C7 45 A8 02 00 00 00            mov dword ptr [rbp - 0x58], 2
0036DB25  C7 45 98 10 00 00 00            mov dword ptr [rbp - 0x68], 0x10
0036DB2C  49 B8 00 00 00 00 80 F6 FF FF   movabs r8, 0xfffff68000000000
0036DB36  49 8B C0                        mov rax, r8
0036DB39  48 BA FF FF FF FF FF F6 FF FF   movabs rdx, 0xfffff6ffffffffff
0036DB43  48 3B C8                        cmp rcx, rax
0036DB46  0F 82 FF 0B 00 00               jb 0x14036e74b
0036DB4C  48 8B C2                        mov rax, rdx
0036DB4F  48 3B C8                        cmp rcx, rax
0036DB52  0F 87 F3 0B 00 00               ja 0x14036e74b
0036DB58  8A 4D D0                        mov cl, byte ptr [rbp - 0x30]
0036DB5B  88 4C 24 70                     mov byte ptr [rsp + 0x70], cl
0036DB5F  48 8B 8D 00 01 00 00            mov rcx, qword ptr [rbp + 0x100]
0036DB66  4C 8D 45 C0                     lea r8, [rbp - 0x40]
0036DB6A  48 8B C3                        mov rax, rbx
0036DB6D  33 D2                           xor edx, edx
0036DB6F  48 C1 E8 05                     shr rax, 5
0036DB73  83 E0 1F                        and eax, 0x1f
0036DB76  48 89 45 30                     mov qword ptr [rbp + 0x30], rax
0036DB7A  48 8B 41 58                     mov rax, qword ptr [rcx + 0x58]
0036DB7E  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
0036DB82  E8 39 85 F4 FF                  call 0x1402b60c0
0036DB87  4C 8B 6D C0                     mov r13, qword ptr [rbp - 0x40]
0036DB8B  44 8B F8                        mov r15d, eax
0036DB8E  89 45 AC                        mov dword ptr [rbp - 0x54], eax
0036DB91  4D 85 ED                        test r13, r13
0036DB94  0F 84 DC 12 00 00               je 0x14036ee76
0036DB9A  41 8B 4D 34                     mov ecx, dword ptr [r13 + 0x34]
0036DB9E  48 8B 45 C0                     mov rax, qword ptr [rbp - 0x40]
0036DBA2  4C 8B 4D B0                     mov r9, qword ptr [rbp - 0x50]
0036DBA6  0F B6 50 22                     movzx edx, byte ptr [rax + 0x22]
0036DBAA  48 B8 FE FF FF FF 07 00 00 00   movabs rax, 0x7fffffffe
0036DBB4  48 C1 E2 20                     shl rdx, 0x20
0036DBB8  48 0B D1                        or rdx, rcx
0036DBBB  48 3B D0                        cmp rdx, rax
0036DBBE  0F 85 6E 0F 00 00               jne 0x14036eb32
0036DBC4  44 8A 44 24 70                  mov r8b, byte ptr [rsp + 0x70]
0036DBC9  B8 07 00 00 00                  mov eax, 7
0036DBCE  48 8B BD 10 01 00 00            mov rdi, qword ptr [rbp + 0x110]
0036DBD5  41 80 C8 80                     or r8b, 0x80
0036DBD9  4C 8B 6D C0                     mov r13, qword ptr [rbp - 0x40]
0036DBDD  44 88 44 24 70                  mov byte ptr [rsp + 0x70], r8b
0036DBE2  89 45 A8                        mov dword ptr [rbp - 0x58], eax
0036DBE5  E9 AC 00 00 00                  jmp 0x14036dc96
0036DBEA  48 89 7D C8                     mov qword ptr [rbp - 0x38], rdi
0036DBEE  48 8B BD 10 01 00 00            mov rdi, qword ptr [rbp + 0x110]
0036DBF5  48 89 5D 88                     mov qword ptr [rbp - 0x78], rbx
0036DBF9  48 85 FF                        test rdi, rdi
0036DBFC  0F 85 F6 0D 00 00               jne 0x14036e9f8
0036DC02  41 0F B7 8D AE 00 00 00         movzx ecx, word ptr [r13 + 0xae]
0036DC0A  48 8B 05 77 24 AC 00            mov rax, qword ptr [rip + 0xac2477]
0036DC11  48 8B 0C C8                     mov rcx, qword ptr [rax + rcx*8]
0036DC15  E9 53 FE FF FF                  jmp 0x14036da6d
0036DC1A  48 8B C3                        mov rax, rbx
0036DC1D  48 C1 E8 05                     shr rax, 5
0036DC21  83 E0 1F                        and eax, 0x1f
0036DC24  3C 1F                           cmp al, 0x1f
0036DC26  0F 84 30 11 00 00               je 0x14036ed5c
0036DC2C  41 8B C6                        mov eax, r14d
0036DC2F  83 F9 0B                        cmp ecx, 0xb
0036DC32  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
0036DC37  41 BE 81 00 00 00               mov r14d, 0x81
0036DC3D  41 0F 44 C6                     cmove eax, r14d
0036DC41  44 8B F0                        mov r14d, eax
0036DC44  E9 A2 FE FF FF                  jmp 0x14036daeb
0036DC49  48 83 E0 EF                     and rax, 0xffffffffffffffef
0036DC4D  E9 D1 FD FF FF                  jmp 0x14036da23
0036DC52  48 8B BD 10 01 00 00            mov rdi, qword ptr [rbp + 0x110]
0036DC59  41 BC 01 00 00 00               mov r12d, 1
0036DC5F  41 8B CC                        mov ecx, r12d
0036DC62  E8 89 E4 F0 FF                  call 0x14027c0f0
0036DC67  48 8B 4D B0                     mov rcx, qword ptr [rbp - 0x50]
0036DC6B  E8 60 8C FA FF                  call 0x1403168d0
0036DC70  B2 11                           mov dl, 0x11
0036DC72  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
0036DC76  41 8B CC                        mov ecx, r12d
0036DC79  4C 8B E8                        mov r13, rax
0036DC7C  E8 9F 93 F2 FF                  call 0x140297020
0036DC81  4D 85 ED                        test r13, r13
0036DC84  0F 85 10 FF FF FF               jne 0x14036db9a
0036DC8A  4C 8B 4D B0                     mov r9, qword ptr [rbp - 0x50]
0036DC8E  8B 45 A8                        mov eax, dword ptr [rbp - 0x58]
0036DC91  44 8A 44 24 70                  mov r8b, byte ptr [rsp + 0x70]
0036DC96  48 0F BA E3 0B                  bt rbx, 0xb
0036DC9B  41 BA 01 00 00 00               mov r10d, 1
0036DCA1  0F 82 7F 12 00 00               jb 0x14036ef26
0036DCA7  8A 45 88                        mov al, byte ptr [rbp - 0x78]
0036DCAA  33 D2                           xor edx, edx
0036DCAC  C0 E8 02                        shr al, 2
0036DCAF  41 84 C2                        test r10b, al
0036DCB2  0F 85 35 09 00 00               jne 0x14036e5ed
0036DCB8  8B 05 DA 96 AC 00               mov eax, dword ptr [rip + 0xac96da]
0036DCBE  0B F2                           or esi, edx
0036DCC0  44 39 55 98                     cmp dword ptr [rbp - 0x68], r10d
0036DCC4  0F 85 69 07 00 00               jne 0x14036e433
0036DCCA  4C 8B 64 24 78                  mov r12, qword ptr [rsp + 0x78]
0036DCCF  41 84 F2                        test r10b, sil
0036DCD2  0F 85 7B 09 00 00               jne 0x14036e653
0036DCD8  8B 55 B8                        mov edx, dword ptr [rbp - 0x48]
0036DCDB  48 8D 85 10 01 00 00            lea rax, [rbp + 0x110]
0036DCE2  48 F7 DF                        neg rdi
0036DCE5  4C 8D 45 98                     lea r8, [rbp - 0x68]
0036DCE9  48 8B BD 08 01 00 00            mov rdi, qword ptr [rbp + 0x108]
0036DCF0  4D 1B C9                        sbb r9, r9
0036DCF3  48 8B CF                        mov rcx, rdi
0036DCF6  4C 23 C8                        and r9, rax
0036DCF9  48 8B 45 F0                     mov rax, qword ptr [rbp - 0x10]
0036DCFD  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0036DD02  E8 F9 13 00 00                  call 0x14036f100
0036DD07  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
0036DD0B  4C 8B E0                        mov r12, rax
0036DD0E  48 85 C0                        test rax, rax
0036DD11  0F 84 1E 12 00 00               je 0x14036ef35
0036DD17  48 8B CF                        mov rcx, rdi
0036DD1A  E8 81 4B F1 FF                  call 0x1402828a0
0036DD1F  48 3B C3                        cmp rax, rbx
0036DD22  0F 85 17 12 00 00               jne 0x14036ef3f
0036DD28  48 0F BA E3 0B                  bt rbx, 0xb
0036DD2D  0F 82 C9 10 00 00               jb 0x14036edfc
0036DD33  48 8B 45 A0                     mov rax, qword ptr [rbp - 0x60]
0036DD37  48 85 C0                        test rax, rax
0036DD3A  0F 85 87 0A 00 00               jne 0x14036e7c7
0036DD40  8B 7D 98                        mov edi, dword ptr [rbp - 0x68]
0036DD43  B8 01 00 00 00                  mov eax, 1
0036DD48  3B F8                           cmp edi, eax
0036DD4A  0F 87 3E 04 00 00               ja 0x14036e18e
0036DD50  48 8B 7D 90                     mov rdi, qword ptr [rbp - 0x70]
0036DD54  4C 8B 6D A0                     mov r13, qword ptr [rbp - 0x60]
0036DD58  8B 5D 80                        mov ebx, dword ptr [rbp - 0x80]
0036DD5B  44 8B 45 A8                     mov r8d, dword ptr [rbp - 0x58]
0036DD5F  8B D3                           mov edx, ebx
0036DD61  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
0036DD66  E8 45 D1 F1 FF                  call 0x14028aeb0
0036DD6B  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
0036DD6F  4C 8B C8                        mov r9, rax
0036DD72  48 3B D8                        cmp rbx, rax
0036DD75  0F 87 F3 11 00 00               ja 0x14036ef6e
0036DD7B  44 8B 55 80                     mov r10d, dword ptr [rbp - 0x80]
0036DD7F  45 33 C9                        xor r9d, r9d
0036DD82  0F 57 C0                        xorps xmm0, xmm0
0036DD85  4C 89 4D E8                     mov qword ptr [rbp - 0x18], r9
0036DD89  0F 11 45 D8                     movups xmmword ptr [rbp - 0x28], xmm0
0036DD8D  4D 85 ED                        test r13, r13
0036DD90  0F 85 77 09 00 00               jne 0x14036e70d
0036DD96  4C 8B 6C 24 78                  mov r13, qword ptr [rsp + 0x78]
0036DD9B  41 8B FA                        mov edi, r10d
0036DD9E  41 BB 06 00 00 00               mov r11d, 6
0036DDA4  48 85 FF                        test rdi, rdi
0036DDA7  0F 85 F7 06 00 00               jne 0x14036e4a4
0036DDAD  4D 85 C9                        test r9, r9
0036DDB0  0F 84 CE 0A 00 00               je 0x14036e884
0036DDB6  41 8B CA                        mov ecx, r10d
0036DDB9  48 3B F9                        cmp rdi, rcx
0036DDBC  0F 85 7E 10 00 00               jne 0x14036ee40
0036DDC2  45 8B B4 24 C0 00 00 00         mov r14d, dword ptr [r12 + 0xc0]
0036DDCA  4D 8D AC 24 40 01 00 00         lea r13, [r12 + 0x140]
0036DDD2  41 C1 EE 0B                     shr r14d, 0xb
0036DDD6  4D 8D BC 24 10 01 00 00         lea r15, [r12 + 0x110]
0036DDDE  41 83 E6 07                     and r14d, 7
0036DDE2  33 FF                           xor edi, edi
0036DDE4  33 C0                           xor eax, eax
0036DDE6  49 8B DD                        mov rbx, r13
0036DDE9  89 85 00 01 00 00               mov dword ptr [rbp + 0x100], eax
0036DDEF  48 8B 4D 90                     mov rcx, qword ptr [rbp - 0x70]
0036DDF3  44 89 55 80                     mov dword ptr [rbp - 0x80], r10d
0036DDF7  E8 A4 4A F1 FF                  call 0x1402828a0
0036DDFC  40 F6 C6 10                     test sil, 0x10
0036DE00  0F 85 A3 08 00 00               jne 0x14036e6a9
0036DE06  48 A9 01 0C 00 00               test rax, 0xc01
0036DE0C  0F 85 15 08 00 00               jne 0x14036e627
0036DE12  48 8B 0D 67 FE AB 00            mov rcx, qword ptr [rip + 0xabfe67]
0036DE19  48 8B D0                        mov rdx, rax
0036DE1C  48 85 C9                        test rcx, rcx
0036DE1F  0F 84 78 08 00 00               je 0x14036e69d
0036DE25  4C 8B 45 88                     mov r8, qword ptr [rbp - 0x78]
0036DE29  A8 10                           test al, 0x10
0036DE2B  0F 85 52 08 00 00               jne 0x14036e683
0036DE31  48 8B D1                        mov rdx, rcx
0036DE34  48 F7 D2                        not rdx
0036DE37  48 23 D0                        and rdx, rax
0036DE3A  41 F6 C0 10                     test r8b, 0x10
0036DE3E  0F 85 48 08 00 00               jne 0x14036e68c
0036DE44  48 F7 D1                        not rcx
0036DE47  49 23 C8                        and rcx, r8
0036DE4A  48 33 CA                        xor rcx, rdx
0036DE4D  41 BB 01 00 00 00               mov r11d, 1
0036DE53  48 BA 00 00 00 00 FF FF FF FF   movabs rdx, 0xffffffff00000000
0036DE5D  48 85 CA                        test rdx, rcx
0036DE60  0F 85 C7 07 00 00               jne 0x14036e62d
0036DE66  8A C8                           mov cl, al
0036DE68  C0 E9 02                        shr cl, 2
0036DE6B  41 84 CB                        test r11b, cl
0036DE6E  0F 84 B9 07 00 00               je 0x14036e62d
0036DE74  48 C1 E8 0C                     shr rax, 0xc
0036DE78  49 C1 E8 0C                     shr r8, 0xc
0036DE7C  44 32 C0                        xor r8b, al
0036DE7F  41 F6 C0 0F                     test r8b, 0xf
0036DE83  0F 85 A4 07 00 00               jne 0x14036e62d
0036DE89  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
0036DE8E  83 E0 0F                        and eax, 0xf
0036DE91  33 D2                           xor edx, edx
0036DE93  8B 89 B4 04 00 00               mov ecx, dword ptr [rcx + 0x4b4]
0036DE99  3B C1                           cmp eax, ecx
0036DE9B  8B C6                           mov eax, esi
0036DE9D  0F 94 C2                        sete dl
0036DEA0  41 23 C3                        and eax, r11d
0036DEA3  3B D0                           cmp edx, eax
0036DEA5  0F 85 82 07 00 00               jne 0x14036e62d
0036DEAB  4C 8B 45 D8                     mov r8, qword ptr [rbp - 0x28]
0036DEAF  4D 85 C0                        test r8, r8
0036DEB2  74 1F                           je 0x14036ded3
0036DEB4  49 8B C0                        mov rax, r8
0036DEB7  48 8B 08                        mov rcx, qword ptr [rax]
0036DEBA  48 8B 45 E8                     mov rax, qword ptr [rbp - 0x18]
0036DEBE  49 2B C3                        sub rax, r11
0036DEC1  48 89 4D D8                     mov qword ptr [rbp - 0x28], rcx
0036DEC5  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
0036DEC9  48 F7 D8                        neg rax
0036DECC  48 1B C0                        sbb rax, rax
0036DECF  48 21 45 E0                     and qword ptr [rbp - 0x20], rax
0036DED3  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
0036DEDD  48 8B C0                        mov rax, rax
0036DEE0  44 01 9D 00 01 00 00            add dword ptr [rbp + 0x100], r11d
0036DEE7  49 8B D0                        mov rdx, r8
0036DEEA  48 2B D0                        sub rdx, rax
0036DEED  49 8B C8                        mov rcx, r8
0036DEF0  48 C1 FA 04                     sar rdx, 4
0036DEF4  48 B8 AB AA AA AA AA AA AA AA   movabs rax, 0xaaaaaaaaaaaaaaab
0036DEFE  48 0F AF D0                     imul rdx, rax
0036DF02  48 8B 85 08 01 00 00            mov rax, qword ptr [rbp + 0x108]
0036DF09  48 89 13                        mov qword ptr [rbx], rdx
0036DF0C  48 39 45 90                     cmp qword ptr [rbp - 0x70], rax
0036DF10  0F 84 55 07 00 00               je 0x14036e66b
0036DF16  41 8B 94 24 C0 00 00 00         mov edx, dword ptr [r12 + 0xc0]
0036DF1E  C1 EA 0E                        shr edx, 0xe
0036DF21  83 E2 07                        and edx, 7
0036DF24  E8 E7 6E F2 FF                  call 0x140294e10
0036DF29  48 8B 45 A0                     mov rax, qword ptr [rbp - 0x60]
0036DF2D  48 83 C3 08                     add rbx, 8
0036DF31  44 8B 8D 00 01 00 00            mov r9d, dword ptr [rbp + 0x100]
0036DF38  44 89 8D 00 01 00 00            mov dword ptr [rbp + 0x100], r9d
0036DF3F  48 85 C0                        test rax, rax
0036DF42  74 08                           je 0x14036df4c
0036DF44  48 8B C8                        mov rcx, rax
0036DF47  E8 54 58 FF FF                  call 0x1403637a0
0036DF4C  48 8B 55 88                     mov rdx, qword ptr [rbp - 0x78]
0036DF50  48 83 45 90 08                  add qword ptr [rbp - 0x70], 8
0036DF55  48 8B C2                        mov rax, rdx
0036DF58  48 8B 0D 21 FD AB 00            mov rcx, qword ptr [rip + 0xabfd21]
0036DF5F  4C 8B C2                        mov r8, rdx
0036DF62  48 85 C9                        test rcx, rcx
0036DF65  74 0D                           je 0x14036df74
0036DF67  A8 10                           test al, 0x10
0036DF69  75 09                           jne 0x14036df74
0036DF6B  48 8B D1                        mov rdx, rcx
0036DF6E  48 F7 D2                        not rdx
0036DF71  48 23 D0                        and rdx, rax
0036DF74  48 C1 EA 20                     shr rdx, 0x20
0036DF78  41 BB 01 00 00 00               mov r11d, 1
0036DF7E  49 03 D3                        add rdx, r11
0036DF81  4D 85 C0                        test r8, r8
0036DF84  0F 84 44 07 00 00               je 0x14036e6ce
0036DF8A  48 85 C9                        test rcx, rcx
0036DF8D  74 0E                           je 0x14036df9d
0036DF8F  A8 10                           test al, 0x10
0036DF91  0F 85 FD 06 00 00               jne 0x14036e694
0036DF97  48 F7 D1                        not rcx
0036DF9A  48 23 C1                        and rax, rcx
0036DF9D  8B C8                           mov ecx, eax
0036DF9F  48 C1 E2 20                     shl rdx, 0x20
0036DFA3  48 0B CA                        or rcx, rdx
0036DFA6  E8 35 16 F2 FF                  call 0x14028f5e0
0036DFAB  44 8B 55 80                     mov r10d, dword ptr [rbp - 0x80]
0036DFAF  41 03 FB                        add edi, r11d
0036DFB2  48 89 45 88                     mov qword ptr [rbp - 0x78], rax
0036DFB6  41 3B FA                        cmp edi, r10d
0036DFB9  0F 82 30 FE FF FF               jb 0x14036ddef
0036DFBF  48 8B 4D 90                     mov rcx, qword ptr [rbp - 0x70]
0036DFC3  49 8D BC 24 40 01 00 00         lea rdi, [r12 + 0x140]
0036DFCB  8A 5C 24 70                     mov bl, byte ptr [rsp + 0x70]
0036DFCF  41 8B C2                        mov eax, r10d
0036DFD2  48 F7 D8                        neg rax
0036DFD5  C0 EB 04                        shr bl, 4
0036DFD8  4C 8D 34 C1                     lea r14, [rcx + rax*8]
0036DFDC  48 8B 85 08 01 00 00            mov rax, qword ptr [rbp + 0x108]
0036DFE3  49 2B C6                        sub rax, r14
0036DFE6  48 C1 F8 03                     sar rax, 3
0036DFEA  4C 8B 2C C7                     mov r13, qword ptr [rdi + rax*8]
0036DFEE  41 22 DB                        and bl, r11b
0036DFF1  0F 85 CF 06 00 00               jne 0x14036e6c6
0036DFF7  4D 8B CE                        mov r9, r14
0036DFFA  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
0036E004  49 C1 E1 19                     shl r9, 0x19
0036E008  48 8B C0                        mov rax, rax
0036E00B  48 C1 E0 19                     shl rax, 0x19
0036E00F  4C 2B C8                        sub r9, rax
0036E012  49 C1 F9 10                     sar r9, 0x10
0036E016  49 83 27 00                     and qword ptr [r15], 0
0036E01A  45 8B C2                        mov r8d, r10d
0036E01D  41 C1 E0 0C                     shl r8d, 0xc
0036E021  41 8B D1                        mov edx, r9d
0036E024  8B C2                           mov eax, edx
0036E026  45 89 47 28                     mov dword ptr [r15 + 0x28], r8d
0036E02A  41 BA FF 0F 00 00               mov r10d, 0xfff
0036E030  66 41 C7 47 0A 42 00            mov word ptr [r15 + 0xa], 0x42
0036E037  49 23 C2                        and rax, r10
0036E03A  49 81 E1 00 F0 FF FF            and r9, 0xfffffffffffff000
0036E041  41 23 D2                        and edx, r10d
0036E044  4D 89 4F 20                     mov qword ptr [r15 + 0x20], r9
0036E048  49 8D 88 FF 0F 00 00            lea rcx, [r8 + 0xfff]
0036E04F  41 89 57 2C                     mov dword ptr [r15 + 0x2c], edx
0036E053  48 03 C8                        add rcx, rax
0036E056  48 C1 E9 0C                     shr rcx, 0xc
0036E05A  66 83 C1 06                     add cx, 6
0036E05E  66 C1 E1 03                     shl cx, 3
0036E062  66 41 89 4F 08                  mov word ptr [r15 + 8], cx
0036E067  40 F6 C6 02                     test sil, 2
0036E06B  0F 85 84 0B 00 00               jne 0x14036ebf5
0036E071  66 41 C7 47 0A 42 40            mov word ptr [r15 + 0xa], 0x4042
0036E078  44 8B 7D 80                     mov r15d, dword ptr [rbp - 0x80]
0036E07C  49 8B CE                        mov rcx, r14
0036E07F  E8 1C 48 F1 FF                  call 0x1402828a0
0036E084  48 8B D8                        mov rbx, rax
0036E087  B8 01 00 00 00                  mov eax, 1
0036E08C  44 3B F8                        cmp r15d, eax
0036E08F  8A 44 24 70                     mov al, byte ptr [rsp + 0x70]
0036E093  0F 84 79 03 00 00               je 0x14036e412
0036E099  24 DF                           and al, 0xdf
0036E09B  88 44 24 70                     mov byte ptr [rsp + 0x70], al
0036E09F  88 45 D0                        mov byte ptr [rbp - 0x30], al
0036E0A2  8B 45 D0                        mov eax, dword ptr [rbp - 0x30]
0036E0A5  4D 8B CE                        mov r9, r14
0036E0A8  48 8B 4D B0                     mov rcx, qword ptr [rbp - 0x50]
0036E0AC  45 8B C7                        mov r8d, r15d
0036E0AF  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
0036E0B3  48 8B D7                        mov rdx, rdi
0036E0B6  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
0036E0BB  E8 D0 88 F4 FF                  call 0x1402b6990
0036E0C0  40 F6 C6 10                     test sil, 0x10
0036E0C4  0F 85 D3 0A 00 00               jne 0x14036eb9d
0036E0CA  F6 44 24 70 10                  test byte ptr [rsp + 0x70], 0x10
0036E0CF  74 0E                           je 0x14036e0df
0036E0D1  48 8B 8D 10 01 00 00            mov rcx, qword ptr [rbp + 0x110]
0036E0D8  33 D2                           xor edx, edx
0036E0DA  E8 99 A0 FA FF                  call 0x140318178
0036E0DF  48 8B BD 08 01 00 00            mov rdi, qword ptr [rbp + 0x108]
0036E0E6  48 8B CF                        mov rcx, rdi
0036E0E9  E8 B2 47 F1 FF                  call 0x1402828a0
0036E0EE  4C 8B 7D A0                     mov r15, qword ptr [rbp - 0x60]
0036E0F2  49 89 84 24 A8 00 00 00         mov qword ptr [r12 + 0xa8], rax
0036E0FA  49 89 BC 24 E8 00 00 00         mov qword ptr [r12 + 0xe8], rdi
0036E102  45 8B 8C 24 C0 00 00 00         mov r9d, dword ptr [r12 + 0xc0]
0036E10A  41 8B D1                        mov edx, r9d
0036E10D  48 89 45 88                     mov qword ptr [rbp - 0x78], rax
0036E111  4D 85 FF                        test r15, r15
0036E114  0F 85 32 07 00 00               jne 0x14036e84c
0036E11A  48 8B 4D 20                     mov rcx, qword ptr [rbp + 0x20]
0036E11E  E8 0D 58 FD FF                  call 0x140343930
0036E123  83 F8 02                        cmp eax, 2
0036E126  7D 05                           jge 0x14036e12d
0036E128  41 0F BA E9 09                  bts r9d, 9
0036E12D  48 8B 45 C0                     mov rax, qword ptr [rbp - 0x40]
0036E131  48 85 C0                        test rax, rax
0036E134  0F 85 9B 05 00 00               jne 0x14036e6d5
0036E13A  48 8B 8D 10 01 00 00            mov rcx, qword ptr [rbp + 0x110]
0036E141  45 89 8C 24 C0 00 00 00         mov dword ptr [r12 + 0xc0], r9d
0036E149  48 85 C9                        test rcx, rcx
0036E14C  74 07                           je 0x14036e155
0036E14E  B2 11                           mov dl, 0x11
0036E150  E8 3B 7F ED FF                  call 0x140246090
0036E155  48 8B 7D D8                     mov rdi, qword ptr [rbp - 0x28]
0036E159  41 BF 01 00 00 00               mov r15d, 1
0036E15F  48 8B CF                        mov rcx, rdi
0036E162  48 85 FF                        test rdi, rdi
0036E165  0F 84 58 07 00 00               je 0x14036e8c3
0036E16B  48 8B 3F                        mov rdi, qword ptr [rdi]
0036E16E  48 8B 45 E8                     mov rax, qword ptr [rbp - 0x18]
0036E172  49 2B C7                        sub rax, r15
0036E175  48 89 7D D8                     mov qword ptr [rbp - 0x28], rdi
0036E179  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
0036E17D  48 F7 D8                        neg rax
0036E180  48 1B C0                        sbb rax, rax
0036E183  48 21 45 E0                     and qword ptr [rbp - 0x20], rax
0036E187  E8 54 69 FC FF                  call 0x140334ae0
0036E18C  EB D1                           jmp 0x14036e15f
0036E18E  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
0036E193  BA 40 01 00 00                  mov edx, 0x140
0036E198  E8 13 EF FF FF                  call 0x14036d0b0
0036E19D  85 C0                           test eax, eax
0036E19F  0F 84 AB FB FF FF               je 0x14036dd50
0036E1A5  48 8B 95 08 01 00 00            mov rdx, qword ptr [rbp + 0x108]
0036E1AC  41 BC FF 01 00 00               mov r12d, 0x1ff
0036E1B2  44 8B D2                        mov r10d, edx
0036E1B5  41 C1 EA 03                     shr r10d, 3
0036E1B9  45 23 D4                        and r10d, r12d
0036E1BC  45 2B E2                        sub r12d, r10d
0036E1BF  44 89 55 B8                     mov dword ptr [rbp - 0x48], r10d
0036E1C3  F6 44 24 70 10                  test byte ptr [rsp + 0x70], 0x10
0036E1C8  0F 85 40 08 00 00               jne 0x14036ea0e
0036E1CE  41 B8 01 00 00 00               mov r8d, 1
0036E1D4  4C 8B 6D A0                     mov r13, qword ptr [rbp - 0x60]
0036E1D8  4D 85 ED                        test r13, r13
0036E1DB  0F 85 03 06 00 00               jne 0x14036e7e4
0036E1E1  40 F6 C6 04                     test sil, 4
0036E1E5  0F 85 F9 05 00 00               jne 0x14036e7e4
0036E1EB  41 3B F8                        cmp edi, r8d
0036E1EE  0F 86 6D 0D 00 00               jbe 0x14036ef61
0036E1F4  44 8D 5F FF                     lea r11d, [rdi - 1]
0036E1F8  48 89 5D 88                     mov qword ptr [rbp - 0x78], rbx
0036E1FC  48 8D 42 08                     lea rax, [rdx + 8]
0036E200  44 89 5D 80                     mov dword ptr [rbp - 0x80], r11d
0036E204  45 3B E3                        cmp r12d, r11d
0036E207  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
0036E20B  48 8B CB                        mov rcx, rbx
0036E20E  45 0F 47 E3                     cmova r12d, r11d
0036E212  E8 19 13 00 00                  call 0x14036f530
0036E217  8B D0                           mov edx, eax
0036E219  41 BD FD FF FF FF               mov r13d, 0xfffffffd
0036E21F  44 2B EA                        sub r13d, edx
0036E222  41 8B C4                        mov eax, r12d
0036E225  48 03 C2                        add rax, rdx
0036E228  48 89 55 98                     mov qword ptr [rbp - 0x68], rdx
0036E22C  B9 FE FF FF FF                  mov ecx, 0xfffffffe
0036E231  48 3B C1                        cmp rax, rcx
0036E234  45 0F 42 EC                     cmovb r13d, r12d
0036E238  41 84 F0                        test r8b, sil
0036E23B  0F 84 32 04 00 00               je 0x14036e673
0036E241  83 CE 08                        or esi, 8
0036E244  48 8D 4D 88                     lea rcx, [rbp - 0x78]
0036E248  E8 43 F6 FF FF                  call 0x14036d890
0036E24D  45 85 ED                        test r13d, r13d
0036E250  74 6B                           je 0x14036e2bd
0036E252  48 8B 7D 88                     mov rdi, qword ptr [rbp - 0x78]
0036E256  BB 01 00 00 00                  mov ebx, 1
0036E25B  4C 8B 65 C8                     mov r12, qword ptr [rbp - 0x38]
0036E25F  4C 8B 7D 98                     mov r15, qword ptr [rbp - 0x68]
0036E263  4C 03 FB                        add r15, rbx
0036E266  48 8B CF                        mov rcx, rdi
0036E269  49 8B D7                        mov rdx, r15
0036E26C  E8 CF F5 FF FF                  call 0x14036d840
0036E271  49 8B CC                        mov rcx, r12
0036E274  48 8B F8                        mov rdi, rax
0036E277  E8 24 46 F1 FF                  call 0x1402828a0
0036E27C  48 89 45 F8                     mov qword ptr [rbp - 8], rax
0036E280  48 A9 E0 03 00 00               test rax, 0x3e0
0036E286  0F 84 8C 03 00 00               je 0x14036e618
0036E28C  48 8D 4D F8                     lea rcx, [rbp - 8]
0036E290  E8 FB F5 FF FF                  call 0x14036d890
0036E295  48 39 7D F8                     cmp qword ptr [rbp - 8], rdi
0036E299  0F 85 79 03 00 00               jne 0x14036e618
0036E29F  4C 89 65 90                     mov qword ptr [rbp - 0x70], r12
0036E2A3  49 83 C4 08                     add r12, 8
0036E2A7  41 83 C5 FF                     add r13d, -1
0036E2AB  75 B6                           jne 0x14036e263
0036E2AD  48 8B 5D 00                     mov rbx, qword ptr [rbp]
0036E2B1  44 8B 7D AC                     mov r15d, dword ptr [rbp - 0x54]
0036E2B5  44 8B 55 B8                     mov r10d, dword ptr [rbp - 0x48]
0036E2B9  44 8B 5D 80                     mov r11d, dword ptr [rbp - 0x80]
0036E2BD  48 8B 85 08 01 00 00            mov rax, qword ptr [rbp + 0x108]
0036E2C4  48 8B CB                        mov rcx, rbx
0036E2C7  48 8B 7D 90                     mov rdi, qword ptr [rbp - 0x70]
0036E2CB  4C 8B E0                        mov r12, rax
0036E2CE  48 2B F8                        sub rdi, rax
0036E2D1  48 89 5D 88                     mov qword ptr [rbp - 0x78], rbx
0036E2D5  48 C1 FF 03                     sar rdi, 3
0036E2D9  44 2B DF                        sub r11d, edi
0036E2DC  48 89 7D 90                     mov qword ptr [rbp - 0x70], rdi
0036E2E0  45 3B D3                        cmp r10d, r11d
0036E2E3  44 89 5D 98                     mov dword ptr [rbp - 0x68], r11d
0036E2E7  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
0036E2EB  45 0F 47 D3                     cmova r10d, r11d
0036E2EF  4C 8B D8                        mov r11, rax
0036E2F2  E8 39 12 00 00                  call 0x14036f530
0036E2F7  44 8B E8                        mov r13d, eax
0036E2FA  4C 89 6D B8                     mov qword ptr [rbp - 0x48], r13
0036E2FE  41 8B C2                        mov eax, r10d
0036E301  49 8D 4D FF                     lea rcx, [r13 - 1]
0036E305  41 FF CD                        dec r13d
0036E308  48 3B C1                        cmp rax, rcx
0036E30B  48 8D 4D 88                     lea rcx, [rbp - 0x78]
0036E30F  45 0F 46 EA                     cmovbe r13d, r10d
0036E313  E8 78 F5 FF FF                  call 0x14036d890
0036E318  45 85 ED                        test r13d, r13d
0036E31B  74 67                           je 0x14036e384
0036E31D  48 8B 7D 88                     mov rdi, qword ptr [rbp - 0x78]
0036E321  BB 01 00 00 00                  mov ebx, 1
0036E326  4C 8B 7D B8                     mov r15, qword ptr [rbp - 0x48]
0036E32A  4C 2B FB                        sub r15, rbx
0036E32D  48 8B CF                        mov rcx, rdi
0036E330  49 8B D7                        mov rdx, r15
0036E333  49 83 EC 08                     sub r12, 8
0036E337  E8 04 F5 FF FF                  call 0x14036d840
0036E33C  49 8B CC                        mov rcx, r12
0036E33F  48 8B F8                        mov rdi, rax
0036E342  E8 59 45 F1 FF                  call 0x1402828a0
0036E347  48 89 45 F8                     mov qword ptr [rbp - 8], rax
0036E34B  48 A9 E0 03 00 00               test rax, 0x3e0
0036E351  74 0F                           je 0x14036e362
0036E353  48 8D 4D F8                     lea rcx, [rbp - 8]
0036E357  E8 34 F5 FF FF                  call 0x14036d890
0036E35C  48 39 7D F8                     cmp qword ptr [rbp - 8], rdi
0036E360  74 08                           je 0x14036e36a
0036E362  40 F6 C6 08                     test sil, 8
0036E366  74 06                           je 0x14036e36e
0036E368  EB 0A                           jmp 0x14036e374
0036E36A  4C 89 65 C8                     mov qword ptr [rbp - 0x38], r12
0036E36E  41 83 C5 FF                     add r13d, -1
0036E372  75 B6                           jne 0x14036e32a
0036E374  48 8B 5D 00                     mov rbx, qword ptr [rbp]
0036E378  44 8B 7D AC                     mov r15d, dword ptr [rbp - 0x54]
0036E37C  4C 8B 5D C8                     mov r11, qword ptr [rbp - 0x38]
0036E380  48 8B 7D 90                     mov rdi, qword ptr [rbp - 0x70]
0036E384  4C 8B 8D 08 01 00 00            mov r9, qword ptr [rbp + 0x108]
0036E38B  48 8B C3                        mov rax, rbx
0036E38E  48 8B 0D EB F8 AB 00            mov rcx, qword ptr [rip + 0xabf8eb]
0036E395  49 8B D1                        mov rdx, r9
0036E398  49 2B D3                        sub rdx, r11
0036E39B  48 C1 FA 03                     sar rdx, 3
0036E39F  48 85 C9                        test rcx, rcx
0036E3A2  74 12                           je 0x14036e3b6
0036E3A4  F6 C3 10                        test bl, 0x10
0036E3A7  0F 85 07 03 00 00               jne 0x14036e6b4
0036E3AD  48 8B C1                        mov rax, rcx
0036E3B0  48 F7 D0                        not rax
0036E3B3  48 23 C3                        and rax, rbx
0036E3B6  48 C1 E8 20                     shr rax, 0x20
0036E3BA  44 8B C2                        mov r8d, edx
0036E3BD  49 2B C0                        sub rax, r8
0036E3C0  48 85 DB                        test rbx, rbx
0036E3C3  0F 84 70 04 00 00               je 0x14036e839
0036E3C9  48 85 C9                        test rcx, rcx
0036E3CC  74 0F                           je 0x14036e3dd
0036E3CE  F6 C3 10                        test bl, 0x10
0036E3D1  0F 85 E6 02 00 00               jne 0x14036e6bd
0036E3D7  48 F7 D1                        not rcx
0036E3DA  48 23 D9                        and rbx, rcx
0036E3DD  48 C1 E0 20                     shl rax, 0x20
0036E3E1  8B CB                           mov ecx, ebx
0036E3E3  48 0B C8                        or rcx, rax
0036E3E6  E8 F5 11 F2 FF                  call 0x14028f5e0
0036E3EB  4C 8B 65 F0                     mov r12, qword ptr [rbp - 0x10]
0036E3EF  48 89 45 88                     mov qword ptr [rbp - 0x78], rax
0036E3F3  8D 47 01                        lea eax, [rdi + 1]
0036E3F6  03 C2                           add eax, edx
0036E3F8  49 8B F9                        mov rdi, r9
0036E3FB  89 45 80                        mov dword ptr [rbp - 0x80], eax
0036E3FE  4A 8D 04 C5 00 00 00 00         lea rax, [r8*8]
0036E406  48 2B F8                        sub rdi, rax
0036E409  48 89 7D 90                     mov qword ptr [rbp - 0x70], rdi
0036E40D  E9 42 F9 FF FF                  jmp 0x14036dd54
0036E412  41 8B 8C 24 C0 00 00 00         mov ecx, dword ptr [r12 + 0xc0]
0036E41A  24 F8                           and al, 0xf8
0036E41C  C1 E9 0B                        shr ecx, 0xb
0036E41F  80 E1 07                        and cl, 7
0036E422  0A C8                           or cl, al
0036E424  80 C9 08                        or cl, 8
0036E427  88 4C 24 70                     mov byte ptr [rsp + 0x70], cl
0036E42B  88 4D D0                        mov byte ptr [rbp - 0x30], cl
0036E42E  E9 6F FC FF FF                  jmp 0x14036e0a2
0036E433  85 C0                           test eax, eax
0036E435  0F 85 AC 05 00 00               jne 0x14036e9e7
0036E43B  4C 8B 65 A0                     mov r12, qword ptr [rbp - 0x60]
0036E43F  4D 85 E4                        test r12, r12
0036E442  0F 85 B2 03 00 00               jne 0x14036e7fa
0036E448  48 8B 4D B0                     mov rcx, qword ptr [rbp - 0x50]
0036E44C  48 B8 FF FF FE FF FF 7F 00 00   movabs rax, 0x7ffffffeffff
0036E456  48 3B C8                        cmp rcx, rax
0036E459  0F 86 6B F8 FF FF               jbe 0x14036dcca
0036E45F  44 89 55 98                     mov dword ptr [rbp - 0x68], r10d
0036E463  41 F6 C0 10                     test r8b, 0x10
0036E467  0F 85 5D F8 FF FF               jne 0x14036dcca
0036E46D  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
0036E477  48 8B C0                        mov rax, rax
0036E47A  48 3B C8                        cmp rcx, rax
0036E47D  72 16                           jb 0x14036e495
0036E47F  48 B8 FF FF FF FF FF F6 FF FF   movabs rax, 0xfffff6ffffffffff
0036E489  48 8B C0                        mov rax, rax
0036E48C  48 3B C8                        cmp rcx, rax
0036E48F  0F 86 35 F8 FF FF               jbe 0x14036dcca
0036E495  83 CE 04                        or esi, 4
0036E498  C7 45 98 10 00 00 00            mov dword ptr [rbp - 0x68], 0x10
0036E49F  E9 26 F8 FF FF                  jmp 0x14036dcca
0036E4A4  40 84 F6                        test sil, sil
0036E4A7  0F 88 EF 0A 00 00               js 0x14036ef9c
0036E4AD  48 8B 45 08                     mov rax, qword ptr [rbp + 8]
0036E4B1  8B 80 B8 00 00 00               mov eax, dword ptr [rax + 0xb8]
0036E4B7  4C 8B 85 10 01 00 00            mov r8, qword ptr [rbp + 0x110]
0036E4BE  A8 0F                           test al, 0xf
0036E4C0  75 16                           jne 0x14036e4d8
0036E4C2  4D 85 C0                        test r8, r8
0036E4C5  75 11                           jne 0x14036e4d8
0036E4C7  48 8B 4D 20                     mov rcx, qword ptr [rbp + 0x20]
0036E4CB  E8 50 EB 04 00                  call 0x1403bd020
0036E4D0  3C FF                           cmp al, 0xff
0036E4D2  0F 85 3B 07 00 00               jne 0x14036ec13
0036E4D8  40 F6 C6 40                     test sil, 0x40
0036E4DC  0F 85 E7 0A 00 00               jne 0x14036efc9
0036E4E2  F6 44 24 70 20                  test byte ptr [rsp + 0x70], 0x20
0036E4E7  BB 09 00 00 00                  mov ebx, 9
0036E4EC  41 0F 45 DB                     cmovne ebx, r11d
0036E4F0  4C 39 4D E8                     cmp qword ptr [rbp - 0x18], r9
0036E4F4  0F 85 BC F8 FF FF               jne 0x14036ddb6
0036E4FA  8B 4D 30                        mov ecx, dword ptr [rbp + 0x30]
0036E4FD  4C 21 4D 18                     and qword ptr [rbp + 0x18], r9
0036E501  48 89 7D 00                     mov qword ptr [rbp], rdi
0036E505  E8 26 A0 F4 FF                  call 0x1402b8530
0036E50A  4C 8B 6D 90                     mov r13, qword ptr [rbp - 0x70]
0036E50E  89 45 AC                        mov dword ptr [rbp - 0x54], eax
0036E511  49 C1 E5 19                     shl r13, 0x19
0036E515  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
0036E51F  48 8B C8                        mov rcx, rax
0036E522  48 C1 E1 19                     shl rcx, 0x19
0036E526  4C 2B E9                        sub r13, rcx
0036E529  49 C1 FD 10                     sar r13, 0x10
0036E52D  33 D2                           xor edx, edx
0036E52F  48 8D 4D 40                     lea rcx, [rbp + 0x40]
0036E533  44 8D 42 70                     lea r8d, [rdx + 0x70]
0036E537  E8 04 87 35 00                  call 0x1406c6c40
0036E53C  48 8B 85 00 01 00 00            mov rax, qword ptr [rbp + 0x100]
0036E543  48 8D 4D 40                     lea rcx, [rbp + 0x40]
0036E547  48 8B 55 08                     mov rdx, qword ptr [rbp + 8]
0036E54B  4D 8B CD                        mov r9, r13
0036E54E  48 89 4C 24 60                  mov qword ptr [rsp + 0x60], rcx
0036E553  48 8D 4D 18                     lea rcx, [rbp + 0x18]
0036E557  48 89 7C 24 58                  mov qword ptr [rsp + 0x58], rdi
0036E55C  44 0F B6 40 45                  movzx r8d, byte ptr [rax + 0x45]
0036E561  48 8B 40 60                     mov rax, qword ptr [rax + 0x60]
0036E565  41 83 E0 01                     and r8d, 1
0036E569  48 89 4C 24 50                  mov qword ptr [rsp + 0x50], rcx
0036E56E  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
0036E573  89 5C 24 48                     mov dword ptr [rsp + 0x48], ebx
0036E577  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
0036E57C  48 83 4C 24 38 FF               or qword ptr [rsp + 0x38], 0xffffffffffffffff
0036E582  8B 45 AC                        mov eax, dword ptr [rbp - 0x54]
0036E585  44 89 74 24 30                  mov dword ptr [rsp + 0x30], r14d
0036E58A  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
0036E58E  44 89 7C 24 20                  mov dword ptr [rsp + 0x20], r15d
0036E593  E8 28 82 0C 00                  call 0x1404367c0
0036E598  48 8D 4D 40                     lea rcx, [rbp + 0x40]
0036E59C  E8 8F 1B FC FF                  call 0x140330130
0036E5A1  48 8B BD A8 00 00 00            mov rdi, qword ptr [rbp + 0xa8]
0036E5A8  48 85 FF                        test rdi, rdi
0036E5AB  0F 84 0F 08 00 00               je 0x14036edc0
0036E5B1  48 83 7D D8 00                  cmp qword ptr [rbp - 0x28], 0
0036E5B6  0F 85 D5 06 00 00               jne 0x14036ec91
0036E5BC  0F 10 85 98 00 00 00            movups xmm0, xmmword ptr [rbp + 0x98]
0036E5C3  F2 0F 10 8D A8 00 00 00         movsd xmm1, qword ptr [rbp + 0xa8]
0036E5CB  0F 11 45 D8                     movups xmmword ptr [rbp - 0x28], xmm0
0036E5CF  F2 0F 11 4D E8                  movsd qword ptr [rbp - 0x18], xmm1
0036E5D4  4C 8B 6C 24 78                  mov r13, qword ptr [rsp + 0x78]
0036E5D9  48 83 7D E8 00                  cmp qword ptr [rbp - 0x18], 0
0036E5DE  0F 84 97 02 00 00               je 0x14036e87b
0036E5E4  44 8B 55 80                     mov r10d, dword ptr [rbp - 0x80]
0036E5E8  E9 C9 F7 FF FF                  jmp 0x14036ddb6
0036E5ED  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
0036E5F2  8B 88 B4 04 00 00               mov ecx, dword ptr [rax + 0x4b4]
0036E5F8  48 8B 45 88                     mov rax, qword ptr [rbp - 0x78]
0036E5FC  48 8B BD 10 01 00 00            mov rdi, qword ptr [rbp + 0x110]
0036E603  4C 8B 6D C0                     mov r13, qword ptr [rbp - 0x40]
0036E607  48 C1 E8 0C                     shr rax, 0xc
0036E60B  83 E0 0F                        and eax, 0xf
0036E60E  3B C1                           cmp eax, ecx
0036E610  0F 94 C2                        sete dl
0036E613  E9 A0 F6 FF FF                  jmp 0x14036dcb8
0036E618  40 F6 C6 08                     test sil, 8
0036E61C  0F 84 81 FC FF FF               je 0x14036e2a3
0036E622  E9 86 FC FF FF                  jmp 0x14036e2ad
0036E627  41 BB 01 00 00 00               mov r11d, 1
0036E62D  40 F6 C6 08                     test sil, 8
0036E631  0F 84 C4 00 00 00               je 0x14036e6fb
0036E637  48 8B 85 08 01 00 00            mov rax, qword ptr [rbp + 0x108]
0036E63E  48 39 45 90                     cmp qword ptr [rbp - 0x70], rax
0036E642  0F 86 6B 06 00 00               jbe 0x14036ecb3
0036E648  44 8B D7                        mov r10d, edi
0036E64B  89 7D 80                        mov dword ptr [rbp - 0x80], edi
0036E64E  E9 6C F9 FF FF                  jmp 0x14036dfbf
0036E653  8B 45 98                        mov eax, dword ptr [rbp - 0x68]
0036E656  41 8B 8C 24 B8 04 00 00         mov ecx, dword ptr [r12 + 0x4b8]
0036E65E  3B C1                           cmp eax, ecx
0036E660  0F 47 C1                        cmova eax, ecx
0036E663  89 45 98                        mov dword ptr [rbp - 0x68], eax
0036E666  E9 6D F6 FF FF                  jmp 0x14036dcd8
0036E66B  41 8B D6                        mov edx, r14d
0036E66E  E9 B1 F8 FF FF                  jmp 0x14036df24
0036E673  48 83 7D A0 00                  cmp qword ptr [rbp - 0x60], 0
0036E678  0F 84 C6 FB FF FF               je 0x14036e244
0036E67E  E9 BE FB FF FF                  jmp 0x14036e241
0036E683  48 83 E2 EF                     and rdx, 0xffffffffffffffef
0036E687  E9 AE F7 FF FF                  jmp 0x14036de3a
0036E68C  49 8B C8                        mov rcx, r8
0036E68F  E9 B6 F7 FF FF                  jmp 0x14036de4a
0036E694  48 83 E0 EF                     and rax, 0xffffffffffffffef
0036E698  E9 00 F9 FF FF                  jmp 0x14036df9d
0036E69D  48 8B 4D 88                     mov rcx, qword ptr [rbp - 0x78]
0036E6A1  4C 8B C1                        mov r8, rcx
0036E6A4  E9 A1 F7 FF FF                  jmp 0x14036de4a
0036E6A9  41 BB 01 00 00 00               mov r11d, 1
0036E6AF  E9 F7 F7 FF FF                  jmp 0x14036deab
0036E6B4  48 83 E0 EF                     and rax, 0xffffffffffffffef
0036E6B8  E9 F9 FC FF FF                  jmp 0x14036e3b6
0036E6BD  48 83 E3 EF                     and rbx, 0xffffffffffffffef
0036E6C1  E9 17 FD FF FF                  jmp 0x14036e3dd
0036E6C6  45 33 C9                        xor r9d, r9d
0036E6C9  E9 48 F9 FF FF                  jmp 0x14036e016
0036E6CE  33 C0                           xor eax, eax
0036E6D0  E9 C8 F8 FF FF                  jmp 0x14036df9d
0036E6D5  8B 40 30                        mov eax, dword ptr [rax + 0x30]
0036E6D8  48 8D 0D 99 5E CA FF            lea rcx, [rip - 0x35a167]
0036E6DF  48 C1 E8 13                     shr rax, 0x13
0036E6E3  83 E0 03                        and eax, 3
0036E6E6  48 83 3C C1 10                  cmp qword ptr [rcx + rax*8], 0x10
0036E6EB  0F 85 49 FA FF FF               jne 0x14036e13a
0036E6F1  41 0F BA E9 15                  bts r9d, 0x15
0036E6F6  E9 3F FA FF FF                  jmp 0x14036e13a
0036E6FB  48 8B 05 36 8D AC 00            mov rax, qword ptr [rip + 0xac8d36]
0036E702  83 CE 02                        or esi, 2
0036E705  48 89 03                        mov qword ptr [rbx], rax
0036E708  E9 1C F8 FF FF                  jmp 0x14036df29
0036E70D  B8 01 00 00 00                  mov eax, 1
0036E712  41 38 45 00                     cmp byte ptr [r13], al
0036E716  0F 85 7A F6 FF FF               jne 0x14036dd96
0036E71C  41 8B 55 50                     mov edx, dword ptr [r13 + 0x50]
0036E720  4C 8B 6C 24 78                  mov r13, qword ptr [rsp + 0x78]
0036E725  C1 EA 03                        shr edx, 3
0036E728  49 8B CD                        mov rcx, r13
0036E72B  83 E2 07                        and edx, 7
0036E72E  03 D0                           add edx, eax
0036E730  E8 0B EC FD FF                  call 0x14034d340
0036E735  48 8B F8                        mov rdi, rax
0036E738  41 8B C2                        mov eax, r10d
0036E73B  48 3B F8                        cmp rdi, rax
0036E73E  0F 86 5A F6 FF FF               jbe 0x14036dd9e
0036E744  8B F8                           mov edi, eax
0036E746  E9 53 F6 FF FF                  jmp 0x14036dd9e
0036E74B  49 8B CF                        mov rcx, r15
0036E74E  C6 44 24 70 10                  mov byte ptr [rsp + 0x70], 0x10
0036E753  48 C1 E9 09                     shr rcx, 9
0036E757  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
0036E761  48 23 C8                        and rcx, rax
0036E764  49 8B C0                        mov rax, r8
0036E767  48 03 C8                        add rcx, rax
0036E76A  E8 31 41 F1 FF                  call 0x1402828a0
0036E76F  48 8B C8                        mov rcx, rax
0036E772  E8 A9 0F EC FF                  call 0x14022f720
0036E777  84 C0                           test al, al
0036E779  0F 85 BF 00 00 00               jne 0x14036e83e
0036E77F  49 83 BC 24 80 02 00 00 00      cmp qword ptr [r12 + 0x280], 0
0036E788  0F 84 D1 F3 FF FF               je 0x14036db5f
0036E78E  E9 B0 00 00 00                  jmp 0x14036e843
0036E793  41 F7 45 50 00 02 00 00         test dword ptr [r13 + 0x50], 0x200
0036E79B  0F 84 58 F3 FF FF               je 0x14036daf9
0036E7A1  48 8B D3                        mov rdx, rbx
0036E7A4  E8 B7 3C FF FF                  call 0x140362460
0036E7A9  85 C0                           test eax, eax
0036E7AB  0F 84 48 F3 FF FF               je 0x14036daf9
0036E7B1  48 85 FF                        test rdi, rdi
0036E7B4  74 0A                           je 0x14036e7c0
0036E7B6  B2 11                           mov dl, 0x11
0036E7B8  48 8B CF                        mov rcx, rdi
0036E7BB  E8 D0 78 ED FF                  call 0x140246090
0036E7C0  33 C0                           xor eax, eax
0036E7C2  E9 E3 01 00 00                  jmp 0x14036e9aa
0036E7C7  B9 01 00 00 00                  mov ecx, 1
0036E7CC  38 08                           cmp byte ptr [rax], cl
0036E7CE  0F 85 6C F5 FF FF               jne 0x14036dd40
0036E7D4  49 8B D4                        mov rdx, r12
0036E7D7  48 8B C8                        mov rcx, rax
0036E7DA  E8 95 C1 FF FF                  call 0x14036a974
0036E7DF  E9 5C F5 FF FF                  jmp 0x14036dd40
0036E7E4  45 33 D2                        xor r10d, r10d
0036E7E7  45 85 E4                        test r12d, r12d
0036E7EA  44 89 55 B8                     mov dword ptr [rbp - 0x48], r10d
0036E7EE  41 0F 44 F8                     cmove edi, r8d
0036E7F2  89 7D 98                        mov dword ptr [rbp - 0x68], edi
0036E7F5  E9 F1 F9 FF FF                  jmp 0x14036e1eb
0036E7FA  4D 85 ED                        test r13, r13
0036E7FD  0F 84 4C 04 00 00               je 0x14036ec4f
0036E803  8B D6                           mov edx, esi
0036E805  4D 8B C5                        mov r8, r13
0036E808  41 23 D2                        and edx, r10d
0036E80B  44 8B CA                        mov r9d, edx
0036E80E  41 83 C9 02                     or r9d, 2
0036E812  F6 44 24 70 10                  test byte ptr [rsp + 0x70], 0x10
0036E817  44 0F 44 CA                     cmove r9d, edx
0036E81B  49 8B D4                        mov rdx, r12
0036E81E  4C 8B 64 24 78                  mov r12, qword ptr [rsp + 0x78]
0036E823  49 8B CC                        mov rcx, r12
0036E826  E8 89 4D FF FF                  call 0x1403635b4
0036E82B  89 45 98                        mov dword ptr [rbp - 0x68], eax
0036E82E  41 BA 01 00 00 00               mov r10d, 1
0036E834  E9 96 F4 FF FF                  jmp 0x14036dccf
0036E839  E9 9F FB FF FF                  jmp 0x14036e3dd
0036E83E  C6 44 24 70 30                  mov byte ptr [rsp + 0x70], 0x30
0036E843  44 89 6D 98                     mov dword ptr [rbp - 0x68], r13d
0036E847  E9 13 F3 FF FF                  jmp 0x14036db5f
0036E84C  B8 01 00 00 00                  mov eax, 1
0036E851  41 38 07                        cmp byte ptr [r15], al
0036E854  0F 85 C0 F8 FF FF               jne 0x14036e11a
0036E85A  41 83 C9 20                     or r9d, 0x20
0036E85E  41 F7 47 50 00 20 00 00         test dword ptr [r15 + 0x50], 0x2000
0036E866  0F 84 AE F8 FF FF               je 0x14036e11a
0036E86C  44 8B CA                        mov r9d, edx
0036E86F  41 81 C9 A0 00 00 00            or r9d, 0xa0
0036E876  E9 9F F8 FF FF                  jmp 0x14036e11a
0036E87B  40 84 F6                        test sil, sil
0036E87E  0F 88 C0 07 00 00               js 0x14036f044
0036E884  48 8B 8D 10 01 00 00            mov rcx, qword ptr [rbp + 0x110]
0036E88B  48 85 C9                        test rcx, rcx
0036E88E  0F 85 DD 07 00 00               jne 0x14036f071
0036E894  49 8B CC                        mov rcx, r12
0036E897  E8 64 70 F4 FF                  call 0x1402b5900
0036E89C  4C 8B 65 A0                     mov r12, qword ptr [rbp - 0x60]
0036E8A0  4D 85 E4                        test r12, r12
0036E8A3  0F 85 D4 07 00 00               jne 0x14036f07d
0036E8A9  44 8B 45 A8                     mov r8d, dword ptr [rbp - 0x58]
0036E8AD  49 8B CD                        mov rcx, r13
0036E8B0  48 8B 55 C8                     mov rdx, qword ptr [rbp - 0x38]
0036E8B4  E8 6F F0 FF FF                  call 0x14036d928
0036E8B9  B8 17 00 00 C0                  mov eax, 0xc0000017
0036E8BE  E9 E7 00 00 00                  jmp 0x14036e9aa
0036E8C3  8B 85 00 01 00 00               mov eax, dword ptr [rbp + 0x100]
0036E8C9  48 8B 55 C8                     mov rdx, qword ptr [rbp - 0x38]
0036E8CD  4C 8B 7D A0                     mov r15, qword ptr [rbp - 0x60]
0036E8D1  48 3B C2                        cmp rax, rdx
0036E8D4  74 11                           je 0x14036e8e7
0036E8D6  44 8B 45 A8                     mov r8d, dword ptr [rbp - 0x58]
0036E8DA  48 2B D0                        sub rdx, rax
0036E8DD  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
0036E8E2  E8 41 F0 FF FF                  call 0x14036d928
0036E8E7  48 8B 85 18 01 00 00            mov rax, qword ptr [rbp + 0x118]
0036E8EE  48 8B CB                        mov rcx, rbx
0036E8F1  4C 89 20                        mov qword ptr [rax], r12
0036E8F4  E8 37 0C 00 00                  call 0x14036f530
0036E8F9  48 C1 EB 0C                     shr rbx, 0xc
0036E8FD  8B D0                           mov edx, eax
0036E8FF  83 E3 0F                        and ebx, 0xf
0036E902  F6 44 24 70 10                  test byte ptr [rsp + 0x70], 0x10
0036E907  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
0036E90C  89 55 28                        mov dword ptr [rbp + 0x28], edx
0036E90F  4C 8B 84 D8 60 48 00 00         mov r8, qword ptr [rax + rbx*8 + 0x4860]
0036E917  74 0F                           je 0x14036e928
0036E919  48 8B 8D 10 01 00 00            mov rcx, qword ptr [rbp + 0x110]
0036E920  49 89 8C 24 A0 00 00 00         mov qword ptr [r12 + 0xa0], rcx
0036E928  41 8B 84 24 C0 00 00 00         mov eax, dword ptr [r12 + 0xc0]
0036E930  41 B9 01 00 00 00               mov r9d, 1
0036E936  41 84 F1                        test r9b, sil
0036E939  0F 84 80 00 00 00               je 0x14036e9bf
0036E93F  49 89 54 24 60                  mov qword ptr [r12 + 0x60], rdx
0036E944  0F BA E8 0A                     bts eax, 0xa
0036E948  0F BA E8 16                     bts eax, 0x16
0036E94C  4D 89 84 24 C8 00 00 00         mov qword ptr [r12 + 0xc8], r8
0036E954  49 83 B8 B8 00 00 00 00         cmp qword ptr [r8 + 0xb8], 0
0036E95C  75 77                           jne 0x14036e9d5
0036E95E  41 89 84 24 C0 00 00 00         mov dword ptr [r12 + 0xc0], eax
0036E966  4A 8D 14 6D 00 00 00 00         lea rdx, [r13*2]
0036E96E  49 03 D5                        add rdx, r13
0036E971  4D 89 B4 24 F0 00 00 00         mov qword ptr [r12 + 0xf0], r14
0036E979  48 C1 E2 04                     shl rdx, 4
0036E97D  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
0036E987  48 8B C0                        mov rax, rax
0036E98A  48 03 D0                        add rdx, rax
0036E98D  49 89 94 24 F8 00 00 00         mov qword ptr [r12 + 0xf8], rdx
0036E995  66 41 0F BA A0 AC 00 00 00 0B   bt word ptr [r8 + 0xac], 0xb
0036E99F  0F 82 3E 07 00 00               jb 0x14036f0e3
0036E9A5  B8 33 33 03 C0                  mov eax, 0xc0033333
0036E9AA  48 81 C4 B8 01 00 00            add rsp, 0x1b8
0036E9B1  41 5F                           pop r15
0036E9B3  41 5E                           pop r14
0036E9B5  41 5D                           pop r13
0036E9B7  41 5C                           pop r12
0036E9B9  5F                              pop rdi
0036E9BA  5E                              pop rsi
0036E9BB  5B                              pop rbx
0036E9BC  5D                              pop rbp
0036E9BD  C3                              ret
0036E9BE  CC                              int3
0036E9BF  83 65 2C 00                     and dword ptr [rbp + 0x2c], 0
0036E9C3  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
0036E9C7  48 C1 E1 0C                     shl rcx, 0xc
0036E9CB  49 89 4C 24 60                  mov qword ptr [r12 + 0x60], rcx
0036E9D0  E9 73 FF FF FF                  jmp 0x14036e948
0036E9D5  4D 85 FF                        test r15, r15
0036E9D8  0F 85 53 03 00 00               jne 0x14036ed31
0036E9DE  0F BA E8 17                     bts eax, 0x17
0036E9E2  E9 77 FF FF FF                  jmp 0x14036e95e
0036E9E7  FF C8                           dec eax
0036E9E9  44 89 55 98                     mov dword ptr [rbp - 0x68], r10d
0036E9ED  89 05 A5 89 AC 00               mov dword ptr [rip + 0xac89a5], eax
0036E9F3  E9 D2 F2 FF FF                  jmp 0x14036dcca
0036E9F8  4D 8B C6                        mov r8, r14
0036E9FB  49 8B D4                        mov rdx, r12
0036E9FE  49 8B CD                        mov rcx, r13
0036EA01  E8 FA 7C F4 FF                  call 0x1402b6700
0036EA06  48 8B C8                        mov rcx, rax
0036EA09  E9 5A F0 FF FF                  jmp 0x14036da68
0036EA0E  4D 85 ED                        test r13, r13
0036EA11  0F 85 7F 03 00 00               jne 0x14036ed96
0036EA17  41 8D 4D 01                     lea ecx, [r13 + 1]
0036EA1B  E8 D0 D6 F0 FF                  call 0x14027c0f0
0036EA20  48 8B 7D B0                     mov rdi, qword ptr [rbp - 0x50]
0036EA24  48 8B CF                        mov rcx, rdi
0036EA27  E8 A4 7E FA FF                  call 0x1403168d0
0036EA2C  B2 11                           mov dl, 0x11
0036EA2E  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
0036EA32  B9 01 00 00 00                  mov ecx, 1
0036EA37  4C 8B E8                        mov r13, rax
0036EA3A  E8 E1 85 F2 FF                  call 0x140297020
0036EA3F  4D 85 ED                        test r13, r13
0036EA42  0F 84 D5 01 00 00               je 0x14036ec1d
0036EA48  41 F7 45 30 00 00 20 00         test dword ptr [r13 + 0x30], 0x200000
0036EA50  0F 85 C7 01 00 00               jne 0x14036ec1d
0036EA56  48 8B D7                        mov rdx, rdi
0036EA59  4C 8D 4D 10                     lea r9, [rbp + 0x10]
0036EA5D  48 C1 EA 0C                     shr rdx, 0xc
0036EA61  41 B8 0C 00 00 00               mov r8d, 0xc
0036EA67  49 8B CD                        mov rcx, r13
0036EA6A  E8 01 FF FB FF                  call 0x14032e970
0036EA6F  48 8B 45 10                     mov rax, qword ptr [rbp + 0x10]
0036EA73  48 85 C0                        test rax, rax
0036EA76  0F 84 A1 01 00 00               je 0x14036ec1d
0036EA7C  8B 40 20                        mov eax, dword ptr [rax + 0x20]
0036EA7F  0F BA E0 11                     bt eax, 0x11
0036EA83  0F 82 94 01 00 00               jb 0x14036ec1d
0036EA89  48 8B 45 10                     mov rax, qword ptr [rbp + 0x10]
0036EA8D  41 B8 01 00 00 00               mov r8d, 1
0036EA93  48 8B 95 08 01 00 00            mov rdx, qword ptr [rbp + 0x108]
0036EA9A  44 8B 55 B8                     mov r10d, dword ptr [rbp - 0x48]
0036EA9E  8B 7D 98                        mov edi, dword ptr [rbp - 0x68]
0036EAA1  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
0036EAA5  8B 40 2C                        mov eax, dword ptr [rax + 0x2c]
0036EAA8  48 C1 E0 03                     shl rax, 3
0036EAAC  48 2B C2                        sub rax, rdx
0036EAAF  48 03 C1                        add rax, rcx
0036EAB2  48 C1 F8 03                     sar rax, 3
0036EAB6  FF C8                           dec eax
0036EAB8  41 3B C4                        cmp eax, r12d
0036EABB  44 0F 42 E0                     cmovb r12d, eax
0036EABF  48 8B C2                        mov rax, rdx
0036EAC2  48 2B C1                        sub rax, rcx
0036EAC5  48 C1 F8 03                     sar rax, 3
0036EAC9  41 3B C2                        cmp eax, r10d
0036EACC  0F 83 02 F7 FF FF               jae 0x14036e1d4
0036EAD2  44 8B D0                        mov r10d, eax
0036EAD5  89 45 B8                        mov dword ptr [rbp - 0x48], eax
0036EAD8  E9 F7 F6 FF FF                  jmp 0x14036e1d4
0036EADD  49 8B CC                        mov rcx, r12
0036EAE0  E8 FB 77 F4 FF                  call 0x1402b62e0
0036EAE5  85 C0                           test eax, eax
0036EAE7  0F 85 6C F1 FF FF               jne 0x14036dc59
0036EAED  48 8B 45 08                     mov rax, qword ptr [rbp + 8]
0036EAF1  4C 8B 4D B0                     mov r9, qword ptr [rbp - 0x50]
0036EAF5  8B 80 B8 00 00 00               mov eax, dword ptr [rax + 0xb8]
0036EAFB  A8 0F                           test al, 0xf
0036EAFD  75 33                           jne 0x14036eb32
0036EAFF  48 B8 00 00 00 00 00 80 FF FF   movabs rax, 0xffff800000000000
0036EB09  4C 3B C8                        cmp r9, rax
0036EB0C  73 24                           jae 0x14036eb32
0036EB0E  49 8B 84 24 10 04 00 00         mov rax, qword ptr [r12 + 0x410]
0036EB16  48 83 B8 90 04 00 00 00         cmp qword ptr [rax + 0x490], 0
0036EB1E  0F 85 2E F1 FF FF               jne 0x14036dc52
0036EB24  48 83 B8 98 04 00 00 00         cmp qword ptr [rax + 0x498], 0
0036EB2C  0F 85 20 F1 FF FF               jne 0x14036dc52
0036EB32  48 8B BD 10 01 00 00            mov rdi, qword ptr [rbp + 0x110]
0036EB39  4C 8B 6D C0                     mov r13, qword ptr [rbp - 0x40]
0036EB3D  E9 4C F1 FF FF                  jmp 0x14036dc8e
0036EB42  4D 8B CF                        mov r9, r15
0036EB45  49 83 E1 FE                     and r9, 0xfffffffffffffffe
0036EB49  41 8A 01                        mov al, byte ptr [r9]
0036EB4C  3C 05                           cmp al, 5
0036EB4E  0F 84 4B 02 00 00               je 0x14036ed9f
0036EB54  41 3A C4                        cmp al, r12b
0036EB57  0F 84 DD 00 00 00               je 0x14036ec3a
0036EB5D  41 3A C6                        cmp al, r14b
0036EB60  0F 85 2C EF FF FF               jne 0x14036da92
0036EB66  4C 89 4D A0                     mov qword ptr [rbp - 0x60], r9
0036EB6A  4D 8B E9                        mov r13, r9
0036EB6D  48 85 DA                        test rdx, rbx
0036EB70  0F 85 4A FC FF FF               jne 0x14036e7c0
0036EB76  48 8B CB                        mov rcx, rbx
0036EB79  E8 B2 09 00 00                  call 0x14036f530
0036EB7E  85 C0                           test eax, eax
0036EB80  0F 84 3A FC FF FF               je 0x14036e7c0
0036EB86  49 8B 41 70                     mov rax, qword ptr [r9 + 0x70]
0036EB8A  45 33 E4                        xor r12d, r12d
0036EB8D  44 89 65 B8                     mov dword ptr [rbp - 0x48], r12d
0036EB91  83 CE 20                        or esi, 0x20
0036EB94  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
0036EB98  E9 F5 EE FF FF                  jmp 0x14036da92
0036EB9D  48 8B 05 DC F0 AB 00            mov rax, qword ptr [rip + 0xabf0dc]
0036EBA4  48 85 C0                        test rax, rax
0036EBA7  74 0F                           je 0x14036ebb8
0036EBA9  F6 C3 10                        test bl, 0x10
0036EBAC  0F 85 94 00 00 00               jne 0x14036ec46
0036EBB2  48 F7 D0                        not rax
0036EBB5  48 23 D8                        and rbx, rax
0036EBB8  48 C1 EB 0C                     shr rbx, 0xc
0036EBBC  48 B8 FF FF FF FF FF 00 00 00   movabs rax, 0xffffffffff
0036EBC6  48 23 D8                        and rbx, rax
0036EBC9  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
0036EBD3  48 8D 1C 5B                     lea rbx, [rbx + rbx*2]
0036EBD7  48 C1 E3 04                     shl rbx, 4
0036EBDB  48 8B C0                        mov rax, rax
0036EBDE  48 03 D8                        add rbx, rax
0036EBE1  49 8B CC                        mov rcx, r12
0036EBE4  48 8B D3                        mov rdx, rbx
0036EBE7  E8 20 6A 14 00                  call 0x1404b560c
0036EBEC  48 8B 5B 10                     mov rbx, qword ptr [rbx + 0x10]
0036EBF0  E9 D5 F4 FF FF                  jmp 0x14036e0ca
0036EBF5  49 8B CF                        mov rcx, r15
0036EBF8  E8 83 CE 0D 00                  call 0x14044ba80
0036EBFD  48 85 C0                        test rax, rax
0036EC00  0F 85 C4 04 00 00               jne 0x14036f0ca
0036EC06  45 8B 7F 28                     mov r15d, dword ptr [r15 + 0x28]
0036EC0A  41 C1 EF 0C                     shr r15d, 0xc
0036EC0E  E9 69 F4 FF FF                  jmp 0x14036e07c
0036EC13  BB 08 00 00 00                  mov ebx, 8
0036EC18  E9 D3 F8 FF FF                  jmp 0x14036e4f0
0036EC1D  44 8B 55 B8                     mov r10d, dword ptr [rbp - 0x48]
0036EC21  41 B8 01 00 00 00               mov r8d, 1
0036EC27  48 8B 95 08 01 00 00            mov rdx, qword ptr [rbp + 0x108]
0036EC2E  41 8B F8                        mov edi, r8d
0036EC31  44 89 45 98                     mov dword ptr [rbp - 0x68], r8d
0036EC35  E9 9A F5 FF FF                  jmp 0x14036e1d4
0036EC3A  4D 8B E9                        mov r13, r9
0036EC3D  4C 89 4D A0                     mov qword ptr [rbp - 0x60], r9
0036EC41  E9 4C EE FF FF                  jmp 0x14036da92
0036EC46  48 83 E3 EF                     and rbx, 0xffffffffffffffef
0036EC4A  E9 69 FF FF FF                  jmp 0x14036ebb8
0036EC4F  48 B8 FF FF FE FF FF 7F 00 00   movabs rax, 0x7ffffffeffff
0036EC59  4C 3B C8                        cmp r9, rax
0036EC5C  0F 87 A1 FB FF FF               ja 0x14036e803
0036EC62  41 8B CA                        mov ecx, r10d
0036EC65  E8 86 D4 F0 FF                  call 0x14027c0f0
0036EC6A  48 8B 4D B0                     mov rcx, qword ptr [rbp - 0x50]
0036EC6E  E8 5D 7C FA FF                  call 0x1403168d0
0036EC73  B2 11                           mov dl, 0x11
0036EC75  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
0036EC79  B9 01 00 00 00                  mov ecx, 1
0036EC7E  4C 8B E8                        mov r13, rax
0036EC81  E8 9A 83 F2 FF                  call 0x140297020
0036EC86  41 BA 01 00 00 00               mov r10d, 1
0036EC8C  E9 72 FB FF FF                  jmp 0x14036e803
0036EC91  48 8B 4D E0                     mov rcx, qword ptr [rbp - 0x20]
0036EC95  48 8B 85 98 00 00 00            mov rax, qword ptr [rbp + 0x98]
0036EC9C  48 01 7D E8                     add qword ptr [rbp - 0x18], rdi
0036ECA0  48 89 01                        mov qword ptr [rcx], rax
0036ECA3  48 8B 85 A0 00 00 00            mov rax, qword ptr [rbp + 0xa0]
0036ECAA  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
0036ECAE  E9 21 F9 FF FF                  jmp 0x14036e5d4
0036ECB3  49 8B DD                        mov rbx, r13
0036ECB6  85 FF                           test edi, edi
0036ECB8  74 56                           je 0x14036ed10
0036ECBA  44 8B BD 00 01 00 00            mov r15d, dword ptr [rbp + 0x100]
0036ECC1  49 BC 00 00 00 00 00 DE FF FF   movabs r12, 0xffffde0000000000
0036ECCB  48 8B 03                        mov rax, qword ptr [rbx]
0036ECCE  48 3B 05 63 87 AC 00            cmp rax, qword ptr [rip + 0xac8763]
0036ECD5  74 16                           je 0x14036eced
0036ECD7  48 8D 0C 40                     lea rcx, [rax + rax*2]
0036ECDB  48 C1 E1 04                     shl rcx, 4
0036ECDF  49 8B C4                        mov rax, r12
0036ECE2  48 03 C8                        add rcx, rax
0036ECE5  E8 66 5E FC FF                  call 0x140334b50
0036ECEA  41 FF CF                        dec r15d
0036ECED  48 83 C3 08                     add rbx, 8
0036ECF1  83 C7 FF                        add edi, -1
0036ECF4  75 D5                           jne 0x14036eccb
0036ECF6  4C 8B 65 F0                     mov r12, qword ptr [rbp - 0x10]
0036ECFA  48 8B 85 08 01 00 00            mov rax, qword ptr [rbp + 0x108]
0036ED01  44 89 BD 00 01 00 00            mov dword ptr [rbp + 0x100], r15d
0036ED08  4D 8D BC 24 10 01 00 00         lea r15, [r12 + 0x110]
0036ED10  83 E6 FD                        and esi, 0xfffffffd
0036ED13  48 89 45 90                     mov qword ptr [rbp - 0x70], rax
0036ED17  48 8B C8                        mov rcx, rax
0036ED1A  49 8B DD                        mov rbx, r13
0036ED1D  E8 7E 3B F1 FF                  call 0x1402828a0
0036ED22  48 89 45 88                     mov qword ptr [rbp - 0x78], rax
0036ED26  41 BA 01 00 00 00               mov r10d, 1
0036ED2C  E9 BE F0 FF FF                  jmp 0x14036ddef
0036ED31  45 38 0F                        cmp byte ptr [r15], r9b
0036ED34  0F 85 A4 FC FF FF               jne 0x14036e9de
0036ED3A  41 F7 47 50 00 10 00 00         test dword ptr [r15 + 0x50], 0x1000
0036ED42  0F 84 96 FC FF FF               je 0x14036e9de
0036ED48  8B 0D B2 64 C5 00               mov ecx, dword ptr [rip + 0xc564b2]
0036ED4E  41 84 C9                        test r9b, cl
0036ED51  0F 84 07 FC FF FF               je 0x14036e95e
0036ED57  E9 82 FC FF FF                  jmp 0x14036e9de
0036ED5C  4C 8B 7D B0                     mov r15, qword ptr [rbp - 0x50]
0036ED60  49 8B D6                        mov rdx, r14
0036ED63  49 8B CF                        mov rcx, r15
0036ED66  41 BE 81 00 00 00               mov r14d, 0x81
0036ED6C  E8 DB 9C FD FF                  call 0x140348a4c
0036ED71  48 85 C0                        test rax, rax
0036ED74  0F 85 66 01 00 00               jne 0x14036eee0
0036ED7A  48 8D 05 7F 9F AC 00            lea rax, [rip + 0xac9f7f]
0036ED81  48 8B C8                        mov rcx, rax
0036ED84  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
0036ED89  41 83 CC 08                     or r12d, 8
0036ED8D  44 89 65 B8                     mov dword ptr [rbp - 0x48], r12d
0036ED91  E9 59 ED FF FF                  jmp 0x14036daef
0036ED96  48 8B 7D B0                     mov rdi, qword ptr [rbp - 0x50]
0036ED9A  E9 A9 FC FF FF                  jmp 0x14036ea48
0036ED9F  41 8B 41 38                     mov eax, dword ptr [r9 + 0x38]
0036EDA3  A8 04                           test al, 4
0036EDA5  0F 85 0F 01 00 00               jne 0x14036eeba
0036EDAB  41 8B 41 38                     mov eax, dword ptr [r9 + 0x38]
0036EDAF  A8 20                           test al, 0x20
0036EDB1  0F 85 21 01 00 00               jne 0x14036eed8
0036EDB7  4C 89 6D A0                     mov qword ptr [rbp - 0x60], r13
0036EDBB  E9 D2 EC FF FF                  jmp 0x14036da92
0036EDC0  83 FB 09                        cmp ebx, 9
0036EDC3  0F 84 0B F8 FF FF               je 0x14036e5d4
0036EDC9  48 8B 55 18                     mov rdx, qword ptr [rbp + 0x18]
0036EDCD  48 85 D2                        test rdx, rdx
0036EDD0  0F 85 2A 02 00 00               jne 0x14036f000
0036EDD6  83 FB 06                        cmp ebx, 6
0036EDD9  0F 85 08 02 00 00               jne 0x14036efe7
0036EDDF  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
0036EDE4  8D 4A 01                        lea ecx, [rdx + 1]
0036EDE7  F0 01 88 E4 43 00 00            lock add dword ptr [rax + 0x43e4], ecx
0036EDEE  48 8B 7D 00                     mov rdi, qword ptr [rbp]
0036EDF2  BB 09 00 00 00                  mov ebx, 9
0036EDF7  E9 31 F7 FF FF                  jmp 0x14036e52d
0036EDFC  48 8B 55 C8                     mov rdx, qword ptr [rbp - 0x38]
0036EE00  8A 4A 22                        mov cl, byte ptr [rdx + 0x22]
0036EE03  8A C1                           mov al, cl
0036EE05  24 28                           and al, 0x28
0036EE07  3C 28                           cmp al, 0x28
0036EE09  0F 84 30 01 00 00               je 0x14036ef3f
0036EE0F  F6 C1 20                        test cl, 0x20
0036EE12  0F 84 27 01 00 00               je 0x14036ef3f
0036EE18  48 8B 42 10                     mov rax, qword ptr [rdx + 0x10]
0036EE1C  48 39 45 88                     cmp qword ptr [rbp - 0x78], rax
0036EE20  0F 85 19 01 00 00               jne 0x14036ef3f
0036EE26  48 8B 02                        mov rax, qword ptr [rdx]
0036EE29  8B 80 A0 00 00 00               mov eax, dword ptr [rax + 0xa0]
0036EE2F  84 C0                           test al, al
0036EE31  0F 88 08 01 00 00               js 0x14036ef3f
0036EE37  4C 8B 6D C0                     mov r13, qword ptr [rbp - 0x40]
0036EE3B  E9 F3 EE FF FF                  jmp 0x14036dd33
0036EE40  4C 8B 4D 90                     mov r9, qword ptr [rbp - 0x70]
0036EE44  4C 8B 95 08 01 00 00            mov r10, qword ptr [rbp + 0x108]
0036EE4B  49 8D 04 F9                     lea rax, [r9 + rdi*8]
0036EE4F  49 3B C2                        cmp rax, r10
0036EE52  0F 86 45 02 00 00               jbe 0x14036f09d
0036EE58  44 8B D7                        mov r10d, edi
0036EE5B  E9 62 EF FF FF                  jmp 0x14036ddc2
0036EE60  48 8B 8D 10 01 00 00            mov rcx, qword ptr [rbp + 0x110]
0036EE67  48 85 C9                        test rcx, rcx
0036EE6A  75 45                           jne 0x14036eeb1
0036EE6C  B8 A1 00 00 C0                  mov eax, 0xc00000a1
0036EE71  E9 34 FB FF FF                  jmp 0x14036e9aa
0036EE76  48 BA 00 00 00 00 80 F6 FF FF   movabs rdx, 0xfffff68000000000
0036EE80  48 8B C2                        mov rax, rdx
0036EE83  48 B9 78 FF FF FF 3F 00 00 00   movabs rcx, 0x3fffffff78
0036EE8D  48 03 C1                        add rax, rcx
0036EE90  48 8B 8D 08 01 00 00            mov rcx, qword ptr [rbp + 0x108]
0036EE97  48 3B C8                        cmp rcx, rax
0036EE9A  0F 87 4D FC FF FF               ja 0x14036eaed
0036EEA0  48 8B C2                        mov rax, rdx
0036EEA3  48 3B C8                        cmp rcx, rax
0036EEA6  0F 83 31 FC FF FF               jae 0x14036eadd
0036EEAC  E9 3C FC FF FF                  jmp 0x14036eaed
0036EEB1  B2 11                           mov dl, 0x11
0036EEB3  E8 D8 71 ED FF                  call 0x140246090
0036EEB8  EB B2                           jmp 0x14036ee6c
0036EEBA  A8 10                           test al, 0x10
0036EEBC  0F 85 0E 4D 37 00               jne 0x1406e3bd0
0036EEC2  48 8B 55 88                     mov rdx, qword ptr [rbp - 0x78]
0036EEC6  E8 95 35 FF FF                  call 0x140362460
0036EECB  85 C0                           test eax, eax
0036EECD  0F 85 D8 FE FF FF               jne 0x14036edab
0036EED3  E9 F8 4C 37 00                  jmp 0x1406e3bd0
0036EED8  83 CE 40                        or esi, 0x40
0036EEDB  E9 D7 FE FF FF                  jmp 0x14036edb7
0036EEE0  0F B7 48 28                     movzx ecx, word ptr [rax + 0x28]
0036EEE4  48 8B 05 9D 11 AC 00            mov rax, qword ptr [rip + 0xac119d]
0036EEEB  48 8B 0C C8                     mov rcx, qword ptr [rax + rcx*8]
0036EEEF  48 8D 05 0A 9E AC 00            lea rax, [rip + 0xac9e0a]
0036EEF6  48 89 4C 24 78                  mov qword ptr [rsp + 0x78], rcx
0036EEFB  48 3B C8                        cmp rcx, rax
0036EEFE  0F 84 85 FE FF FF               je 0x14036ed89
0036EF04  40 F6 C6 20                     test sil, 0x20
0036EF08  0F 84 7B FE FF FF               je 0x14036ed89
0036EF0E  B8 01 00 00 00                  mov eax, 1
0036EF13  41 38 45 00                     cmp byte ptr [r13], al
0036EF17  0F 85 6C FE FF FF               jne 0x14036ed89
0036EF1D  0F BA EE 07                     bts esi, 7
0036EF21  E9 63 FE FF FF                  jmp 0x14036ed89
0036EF26  41 0B C2                        or eax, r10d
0036EF29  44 89 55 98                     mov dword ptr [rbp - 0x68], r10d
0036EF2D  89 45 A8                        mov dword ptr [rbp - 0x58], eax
0036EF30  E9 72 ED FF FF                  jmp 0x14036dca7
0036EF35  BB 9A 00 00 C0                  mov ebx, 0xc000009a
0036EF3A  E9 B2 4C 37 00                  jmp 0x1406e3bf1
0036EF3F  48 8B 8D 10 01 00 00            mov rcx, qword ptr [rbp + 0x110]
0036EF46  BB 34 04 00 C0                  mov ebx, 0xc0000434
0036EF4B  48 85 C9                        test rcx, rcx
0036EF4E  0F 84 95 4C 37 00               je 0x1406e3be9
0036EF54  B2 11                           mov dl, 0x11
0036EF56  E8 35 71 ED FF                  call 0x140246090
0036EF5B  90                              nop
0036EF5C  E9 88 4C 37 00                  jmp 0x1406e3be9
0036EF61  4C 8B 65 F0                     mov r12, qword ptr [rbp - 0x10]
0036EF65  48 8B 7D 90                     mov rdi, qword ptr [rbp - 0x70]
0036EF69  E9 EA ED FF FF                  jmp 0x14036dd58
0036EF6E  4C 8B 05 0B ED AB 00            mov r8, qword ptr [rip + 0xabed0b]
0036EF75  48 8B 55 88                     mov rdx, qword ptr [rbp - 0x78]
0036EF79  48 8B CA                        mov rcx, rdx
0036EF7C  4D 85 C0                        test r8, r8
0036EF7F  0F 84 8A 4C 37 00               je 0x1406e3c0f
0036EF85  F6 C1 10                        test cl, 0x10
0036EF88  0F 85 81 4C 37 00               jne 0x1406e3c0f
0036EF8E  49 8B D0                        mov rdx, r8
0036EF91  48 F7 D2                        not rdx
0036EF94  48 23 D1                        and rdx, rcx
0036EF97  E9 73 4C 37 00                  jmp 0x1406e3c0f
0036EF9C  49 8B 8D B8 00 00 00            mov rcx, qword ptr [r13 + 0xb8]
0036EFA3  E8 18 B7 04 00                  call 0x1403ba6c0
0036EFA8  84 C0                           test al, al
0036EFAA  0F 84 A9 4C 37 00               je 0x1406e3c59
0036EFB0  41 8B 84 24 C0 00 00 00         mov eax, dword ptr [r12 + 0xc0]
0036EFB8  0F BA E8 1A                     bts eax, 0x1a
0036EFBC  41 89 84 24 C0 00 00 00         mov dword ptr [r12 + 0xc0], eax
0036EFC4  E9 E4 F4 FF FF                  jmp 0x14036e4ad
0036EFC9  4D 85 C0                        test r8, r8
0036EFCC  0F 85 10 F5 FF FF               jne 0x14036e4e2
0036EFD2  41 8B 45 04                     mov eax, dword ptr [r13 + 4]
0036EFD6  A8 08                           test al, 8
0036EFD8  0F 84 04 F5 FF FF               je 0x14036e4e2
0036EFDE  41 8D 58 02                     lea ebx, [r8 + 2]
0036EFE2  E9 09 F5 FF FF                  jmp 0x14036e4f0
0036EFE7  83 FB 08                        cmp ebx, 8
0036EFEA  0F 85 FE FD FF FF               jne 0x14036edee
0036EFF0  48 8B 85 00 01 00 00            mov rax, qword ptr [rbp + 0x100]
0036EFF7  83 48 50 10                     or dword ptr [rax + 0x50], 0x10
0036EFFB  E9 EE FD FF FF                  jmp 0x14036edee
0036F000  48 8B 45 08                     mov rax, qword ptr [rbp + 8]
0036F004  4C 8B 6C 24 78                  mov r13, qword ptr [rsp + 0x78]
0036F009  0F B7 88 AE 00 00 00            movzx ecx, word ptr [rax + 0xae]
0036F010  48 8B 05 71 10 AC 00            mov rax, qword ptr [rip + 0xac1071]
0036F017  4C 3B 2C C8                     cmp r13, qword ptr [rax + rcx*8]
0036F01B  0F 84 3F 4C 37 00               je 0x1406e3c60
0036F021  48 8B 85 00 01 00 00            mov rax, qword ptr [rbp + 0x100]
0036F028  49 8D 8D C8 47 00 00            lea rcx, [r13 + 0x47c8]
0036F02F  4C 89 A8 88 00 00 00            mov qword ptr [rax + 0x88], r13
0036F036  E8 E5 75 EA FF                  call 0x140216620
0036F03B  48 8B 55 18                     mov rdx, qword ptr [rbp + 0x18]
0036F03F  E9 1C 4C 37 00                  jmp 0x1406e3c60
0036F044  41 8B 9C 24 C0 00 00 00         mov ebx, dword ptr [r12 + 0xc0]
0036F04C  49 8B 8D B8 00 00 00            mov rcx, qword ptr [r13 + 0xb8]
0036F053  E8 18 3E FD FF                  call 0x140342e70
0036F058  4C 8B 4D E8                     mov r9, qword ptr [rbp - 0x18]
0036F05C  0F BA F3 1A                     btr ebx, 0x1a
0036F060  44 8B 55 80                     mov r10d, dword ptr [rbp - 0x80]
0036F064  41 89 9C 24 C0 00 00 00         mov dword ptr [r12 + 0xc0], ebx
0036F06C  E9 3C ED FF FF                  jmp 0x14036ddad
0036F071  B2 11                           mov dl, 0x11
0036F073  E8 18 70 ED FF                  call 0x140246090
0036F078  E9 17 F8 FF FF                  jmp 0x14036e894
0036F07D  48 8B 85 00 01 00 00            mov rax, qword ptr [rbp + 0x100]
0036F084  48 8B 80 80 00 00 00            mov rax, qword ptr [rax + 0x80]
0036F08B  48 F7 D8                        neg rax
0036F08E  1A C9                           sbb cl, cl
0036F090  80 C1 02                        add cl, 2
0036F093  41 88 4C 24 01                  mov byte ptr [r12 + 1], cl
0036F098  E9 0C F8 FF FF                  jmp 0x14036e8a9
0036F09D  4C 8B 05 DC EB AB 00            mov r8, qword ptr [rip + 0xabebdc]
0036F0A4  48 8B 55 88                     mov rdx, qword ptr [rbp - 0x78]
0036F0A8  48 8B C2                        mov rax, rdx
0036F0AB  4D 85 C0                        test r8, r8
0036F0AE  0F 84 CA 4B 37 00               je 0x1406e3c7e
0036F0B4  A8 10                           test al, 0x10
0036F0B6  0F 85 C2 4B 37 00               jne 0x1406e3c7e
0036F0BC  49 8B D0                        mov rdx, r8
0036F0BF  48 F7 D2                        not rdx
0036F0C2  48 23 D0                        and rdx, rax
0036F0C5  E9 B4 4B 37 00                  jmp 0x1406e3c7e
0036F0CA  4D 8D 34 C6                     lea r14, [r14 + rax*8]
0036F0CE  84 DB                           test bl, bl
0036F0D0  0F 85 30 FB FF FF               jne 0x14036ec06
0036F0D6  48 C1 E0 0C                     shl rax, 0xc
0036F0DA  49 01 47 20                     add qword ptr [r15 + 0x20], rax
0036F0DE  E9 23 FB FF FF                  jmp 0x14036ec06
0036F0E3  49 8B D4                        mov rdx, r12
0036F0E6  49 8B C8                        mov rcx, r8
0036F0E9  E8 C2 C5 16 00                  call 0x1404db6b0
0036F0EE  E9 B2 F8 FF FF                  jmp 0x14036e9a5
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiResolvePageFileFault(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
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
    unsigned __int64 v_stack_m180;
    unsigned __int8 v_stack_m188;
    unsigned __int64 v_stack_m198;
    unsigned __int64 v_stack_m1A0;
    unsigned __int64 v_stack_m1A8;
    unsigned int v_stack_m1B0;
    unsigned __int64 v_stack_m1B8;
    unsigned __int64 v_stack_m1C0;
    unsigned int v_stack_m1C8;
    unsigned int v_stack_m1D0;
    unsigned __int64 v_stack_m1D8;
    unsigned __int64 v_stack_p78;

    *(unsigned __int64 *)(v_rsp + 32) = a4;
    *(unsigned __int64 *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (440);
    v_rdi = 0;
    *(unsigned __int64 *)(v_rsp - 248 + 16) = 0;
    *(unsigned __int64 *)(v_rsp - 248 + 40) = 0;
    *(unsigned __int64 *)(v_rsp - 248 - 80) = *(unsigned __int64 *)(a1);
    *(unsigned __int64 *)(v_rsp - 248 + 8) = *(unsigned __int64 *)(a1 + 56);
    result = MI_READ_PTE_LOCK_FREE(a2, a2, a3, a4);
    *(unsigned __int64 *)(v_rsp - 248) = result;
    *(unsigned __int64 *)(v_rsp - 248 + 32) = *(unsigned __int64 *)(gs_base + (0 + 392));
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1448)) & (4)) != 0) goto loc_0036EE60;
    if ((((unsigned int)(0x800ULL)) & (result)) == 0) goto loc_0036DBEA;
    if (*(unsigned __int64 *)(v_rip + 11272823) == 0) goto loc_0036DA23;
    if ((((unsigned __int8)(result)) & (16)) != 0) goto loc_0036DC49;
    result = ~(*(unsigned __int64 *)(v_rip + 11272823));
    result = (result) & (result);
loc_0036DA23:
    result = (result) >> (12);
    result = (result) & (a4);
    a2 = (result + result * 2) << (4);
    a2 = (a2) + (a3);
    *(unsigned __int64 *)(v_rsp - 248 - 56) = a2;
    *(unsigned __int64 *)(v_rsp - 248 - 120) = *(unsigned __int64 *)(a2 + 16);
    result = (*(unsigned __int64 *)(a2 + 40)) >> (43);
    result = (unsigned int)((result) & (0x3FFULL));
loc_0036DA68:
loc_0036DA6D:
    v_r13 = 0;
    v_stack_m180 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11281972) + result * 8);
    *(unsigned __int64 *)(v_rsp - 248 - 96) = 0;
    *(unsigned int *)(v_rsp - 248 - 72) = (unsigned int)(v_r13 + 2);
    if ((((unsigned __int8)(v_r13 + 1)) & ((unsigned __int8)(*(unsigned __int64 *)(a1 + 16)))) != 0) goto loc_0036EB42;
loc_0036DA92:
    result = MiGetSystemRegionType(*(unsigned __int64 *)(v_rsp - 248 - 80), (unsigned int)(0x800ULL), a3, a4);
    if ((((unsigned __int8)(v_r13 + 1)) & ((unsigned __int8)(*(unsigned __int64 *)(a1 + 16)))) == 0) goto loc_0036DC1A;
    v_r15 = (*(unsigned __int64 *)(a1 + 16)) & (-2);
    if ((*(unsigned __int8 *)(v_r15)) != 4) goto loc_0036DC1A;
    v_r12 = (unsigned int)((v_r13 + 2) | (8));
    *(unsigned __int64 *)(v_rsp - 248 - 96) = v_r15;
    *(unsigned int *)(v_rsp - 248 - 72) = (unsigned int)(v_r12);
    v_stack_m180 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11281837) + *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 48) + 544) + 1198) * 8);
loc_0036DAEB:
loc_0036DAEF:
    if (((16) & (32)) != 0) goto loc_0036E793;
loc_0036DAF9:
    *(unsigned int *)(v_rsp - 248 - 128) = 1;
    *(unsigned __int64 *)(v_rsp - 248 - 112) = *(unsigned __int64 *)(v_rsp - 248 + 264);
    *(unsigned int *)(v_rsp - 248 - 88) = 2;
    *(unsigned int *)(v_rsp - 248 - 104) = 16;
    if ((*(unsigned __int64 *)(v_rsp - 248 + 264)) < a3) goto loc_0036E74B;
    if ((*(unsigned __int64 *)(v_rsp - 248 + 264)) > (*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 48) + 544) + 1198))) goto loc_0036E74B;
    v_stack_m188 = (unsigned __int8)(*(unsigned __int8 *)(v_rsp - 248 - 48));
loc_0036DB5F:
    a2 = 0;
    result = (result) >> (5);
    result = (unsigned int)((result) & (31));
    *(unsigned __int64 *)(v_rsp - 248 + 48) = result;
    *(unsigned __int64 *)(v_rsp - 248 - 64) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 248 + 256) + 88);
    result = MiComputeFaultNode(*(unsigned __int64 *)(v_rsp - 248 + 256), a2, v_rsp - 248 - 64, a4);
    *(unsigned int *)(v_rsp - 248 - 84) = (unsigned int)(result);
    if (*(unsigned __int64 *)(v_rsp - 248 - 64) == 0) goto loc_0036EE76;
loc_0036DB9A:
    a2 = (*(unsigned __int8 *)(*(unsigned __int64 *)(v_rsp - 248 - 64) + 34)) << (32);
    a2 = (a2) | ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 248 - 64) + 52)));
    if (a2 != (*(unsigned __int64 *)(v_rsp - 248 - 64))) goto loc_0036EB32;
    a3 = (unsigned __int8)((v_stack_m188) | (128));
    v_stack_m188 = (unsigned __int8)(a3);
    *(unsigned int *)(v_rsp - 248 - 88) = 7;
    goto loc_0036DC96;
loc_0036DBEA:
    *(unsigned __int64 *)(v_rsp - 248 - 56) = *(unsigned __int64 *)(v_rsp - 248 + 272);
    *(unsigned __int64 *)(v_rsp - 248 - 120) = result;
    if (*(unsigned __int64 *)(v_rsp - 248 + 272) != 0) goto loc_0036E9F8;
    goto loc_0036DA6D;
loc_0036DC1A:
    result = (result) >> (5);
    result = (unsigned int)((result) & (31));
    if (((unsigned __int8)(result)) == 31) goto loc_0036ED5C;
    result = 129;
    if (((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11281527) + *(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 248 - 64) + 174) * 8))) == 11) { result = 129; }
    goto loc_0036DAEB;
loc_0036DC49:
    result = (result) & (-17);
    goto loc_0036DA23;
loc_0036DC52:
loc_0036DC59:
    result = MiLockVadTree(1, a2, a3, *(unsigned __int64 *)(v_rsp - 248 - 80));
    result = MiLocateAddress(*(unsigned __int64 *)(v_rsp - 248 - 80), a2, a3, *(unsigned __int64 *)(v_rsp - 248 - 80));
    *(unsigned __int64 *)(v_rsp - 248 - 64) = result;
    result = MiUnlockVadTree(1, 17, a3, *(unsigned __int64 *)(v_rsp - 248 - 80));
    if (result != 0) goto loc_0036DB9A;
loc_0036DC8E:
loc_0036DC96:
    if (condition_is_below) goto loc_0036EF26;
loc_0036DCA7:
    a2 = 0;
    result = (unsigned __int8)((*(unsigned __int8 *)(v_rsp - 248 - 120)) >> (2));
    if (((1) & ((unsigned __int8)(result))) != 0) goto loc_0036E5ED;
loc_0036DCB8:
    v_rsi = (unsigned int)((16) | (0));
    if ((*(unsigned int *)(v_rsp - 248 - 104)) != 1) goto loc_0036E433;
loc_0036DCCA:
loc_0036DCCF:
    if (((1) & ((unsigned __int8)(v_rsi))) != 0) goto loc_0036E653;
loc_0036DCD8:
    v_rdi = -(*(unsigned __int64 *)(v_rsp - 248 + 272));
    a4 = (*(unsigned __int64 *)(v_rsp - 248 - 80)) & (v_rsp - 248 + 272);
    v_stack_m1D8 = *(unsigned __int64 *)(v_rsp - 248 - 16);
    result = MiAllocateInPageSupport(*(unsigned __int64 *)(v_rsp - 248 + 264), (unsigned int)(*(unsigned int *)(v_rsp - 248 - 72)), v_rsp - 248 - 104, a4);
    *(unsigned __int64 *)(v_rsp - 248 - 16) = result;
    if (result == 0) goto loc_0036EF35;
    result = MI_READ_PTE_LOCK_FREE(*(unsigned __int64 *)(v_rsp - 248 + 264), (unsigned int)(*(unsigned int *)(v_rsp - 248 - 72)), v_rsp - 248 - 104, a4);
    if (result != result) goto loc_0036EF3F;
    if (result < result) goto loc_0036EDFC;
loc_0036DD33:
    if (*(unsigned __int64 *)(v_rsp - 248 - 96) != 0) goto loc_0036E7C7;
loc_0036DD40:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 248 - 104)))) > 1) goto loc_0036E18E;
loc_0036DD50:
loc_0036DD54:
loc_0036DD58:
    result = MiObtainFaultCharges(v_stack_m180, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 248 - 128)))), (unsigned int)(*(unsigned int *)(v_rsp - 248 - 88)), a4);
    *(unsigned __int64 *)(v_rsp - 248 - 56) = result;
    if (((unsigned int)(*(unsigned int *)(v_rsp - 248 - 128))) > result) goto loc_0036EF6E;
    a4 = 0;
    *(unsigned __int64 *)(v_rsp - 248 - 24) = 0;
    *(unsigned __int64 *)(v_rsp - 248 - 40) = v_xmm0;
    if (*(unsigned __int64 *)(v_rsp - 248 - 96) != 0) goto loc_0036E70D;
loc_0036DD96:
loc_0036DD9E:
    if ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 248 - 128)))) != 0) goto loc_0036E4A4;
loc_0036DDAD:
    if (0 == 0) goto loc_0036E884;
loc_0036DDB6:
    if (((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 248 - 128))))) != ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 248 - 128)))))) goto loc_0036EE40;
loc_0036DDC2:
    v_r14 = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 192))) >> (11));
    v_r14 = (unsigned int)((v_r14) & (7));
    v_rdi = 0;
    result = 0;
    *(unsigned int *)(v_rsp - 248 + 256) = 0;
loc_0036DDEF:
    *(unsigned int *)(v_rsp - 248 - 128) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 248 - 128)));
    result = MI_READ_PTE_LOCK_FREE(*(unsigned __int64 *)(v_rsp - 248 - 112), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 248 - 128)))), (unsigned int)(*(unsigned int *)(v_rsp - 248 - 88)), a4);
    if ((((unsigned __int8)(v_rsi)) & (16)) != 0) goto loc_0036E6A9;
    if (((result) & (0xC01ULL)) != 0) goto loc_0036E627;
    if (*(unsigned __int64 *)(v_rip + 11271783) == 0) goto loc_0036E69D;
    if ((((unsigned __int8)(result)) & (16)) != 0) goto loc_0036E683;
    a2 = ~(*(unsigned __int64 *)(v_rip + 11271783));
    a2 = (a2) & (result);
loc_0036DE3A:
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rsp - 248 - 120))) & (16)) != 0) goto loc_0036E68C;
    a1 = ~(*(unsigned __int64 *)(v_rip + 11271783));
    a1 = (a1) & (*(unsigned __int64 *)(v_rsp - 248 - 120));
loc_0036DE4A:
    a1 = (a1) ^ (a2);
    if (((a2) & (a1)) != 0) goto loc_0036E62D;
    a1 = (unsigned __int8)(((unsigned __int8)(result)) >> (2));
    if (((1) & ((unsigned __int8)(a1))) == 0) goto loc_0036E62D;
    result = (result) >> (12);
    a3 = (*(unsigned __int64 *)(v_rsp - 248 - 120)) >> (12);
    a3 = (unsigned __int8)((a3) ^ ((unsigned __int8)(result)));
    if ((((unsigned __int8)(a3)) & (15)) != 0) goto loc_0036E62D;
    result = (unsigned int)((result) & (15));
    a2 = 0;
    a2 = (((unsigned int)(result)) == ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m180 + 1204))))) ? 1 : 0;
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rsi))) & (1));
    if (((unsigned int)(a2)) != ((unsigned int)(result))) goto loc_0036E62D;
loc_0036DEAB:
    if (*(unsigned __int64 *)(v_rsp - 248 - 40) != 0) {
        result = *(unsigned __int64 *)(v_rsp - 248 - 40);
        a1 = *(unsigned __int64 *)(result);
        result = *(unsigned __int64 *)(v_rsp - 248 - 24);
        result = (result) - (1);
        *(unsigned __int64 *)(v_rsp - 248 - 40) = a1;
        *(unsigned __int64 *)(v_rsp - 248 - 24) = result;
        result = -(result);
    }
    a2 = (*(unsigned __int64 *)(v_rsp - 248 - 40)) - (result);
    a2 = (a2) >> (4);
    a2 = (a2) * (result);
    *(unsigned __int64 *)(result + 320) = a2;
    if ((*(unsigned __int64 *)(v_rsp - 248 - 112)) == (*(unsigned __int64 *)(v_rsp - 248 + 264))) goto loc_0036E66B;
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 192))) >> (14));
    a2 = (unsigned int)((a2) & (7));
loc_0036DF24:
    result = MiLockSetPfnPriority(*(unsigned __int64 *)(v_rsp - 248 - 40), a2, *(unsigned __int64 *)(v_rsp - 248 - 40), a4);
loc_0036DF29:
    v_rbx = (result + 320) + (8);
    *(unsigned int *)(v_rsp - 248 + 256) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 248 + 256)));
    result = *(unsigned __int64 *)(v_rsp - 248 - 96);
    if (*(unsigned __int64 *)(v_rsp - 248 - 96) != 0) {
        a1 = *(unsigned __int64 *)(v_rsp - 248 - 96);
        result = MiAdvanceFaultList(a1, a2, *(unsigned __int64 *)(v_rsp - 248 - 40), (unsigned int)(*(unsigned int *)(v_rsp - 248 + 256)));
    }
    if (*(unsigned __int64 *)(v_rip + 11271457) == 0) goto loc_0036DF74;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rsp - 248 - 120))) & (16)) == 0) {
        a2 = *(unsigned __int64 *)(v_rip + 11271457);
        a2 = ~(a2);
        a2 = (a2) & (*(unsigned __int64 *)(v_rsp - 248 - 120));
    }
    a2 = (a2) >> (32);
    a2 = (a2) + (1);
    if (*(unsigned __int64 *)(v_rsp - 248 - 120) == 0) goto loc_0036E6CE;
    if (*(unsigned __int64 *)(v_rip + 11271457) == 0) goto loc_0036DF9D;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rsp - 248 - 120))) & (16)) != 0) goto loc_0036E694;
    a1 = ~(*(unsigned __int64 *)(v_rip + 11271457));
    result = (*(unsigned __int64 *)(v_rsp - 248 - 120)) & (a1);
loc_0036DF9D:
    a2 = (a2) << (32);
    a1 = ((unsigned int)((unsigned int)(result))) | (a2);
    result = MiSwizzleInvalidPte(a1, a2, *(unsigned __int64 *)(v_rsp - 248 - 120), (unsigned int)(*(unsigned int *)(v_rsp - 248 + 256)));
    v_rdi = (unsigned int)((v_rdi) + (1));
    *(unsigned __int64 *)(v_rsp - 248 - 120) = result;
    if (((unsigned int)(v_rdi)) < ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 248 - 128))))) goto loc_0036DDEF;
loc_0036DFBF:
    result = -((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 248 - 128)))));
    v_rbx = (unsigned __int8)((v_stack_m188) >> (4));
    result = (*(unsigned __int64 *)(v_rsp - 248 + 264)) - (*(unsigned __int64 *)(v_rsp - 248 - 112) + result * 8);
    result = (result) >> (3);
    v_rbx = (unsigned __int8)((v_rbx) & (1));
    if (condition_is_not_equal) goto loc_0036E6C6;
    a4 = (*(unsigned __int64 *)(v_rsp - 248 - 112) + result * 8) << (25);
    result = (result) << (25);
    a4 = (a4) - (result);
    a4 = (a4) >> (16);
loc_0036E016:
    a3 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 248 - 128))))) << (12));
    *(unsigned int *)(result + 272 + 40) = (unsigned int)(a3);
    *(unsigned __int16 *)(result + 272 + 10) = 66;
    result = ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a4))))) & ((unsigned int)(0xFFFULL));
    a4 = (a4) & (0xFFFFFFFFFFFFF000ULL);
    a2 = (unsigned int)(((unsigned int)((unsigned int)(a4))) & ((unsigned int)((unsigned int)(0xFFFULL))));
    *(unsigned __int64 *)(result + 272 + 32) = a4;
    *(unsigned int *)(result + 272 + 44) = (unsigned int)(a2);
    a1 = (a3 + 4095) + (result);
    a1 = (a1) >> (12);
    a1 = (unsigned __int16)((a1) + (6));
    a1 = (unsigned __int16)((a1) << (3));
    *(unsigned __int16 *)(result + 272 + 8) = (unsigned __int16)(a1);
    if ((((unsigned __int8)(v_rsi)) & (2)) != 0) goto loc_0036EBF5;
    *(unsigned __int16 *)(result + 272 + 10) = 0x4042ULL;
loc_0036E07C:
    result = MI_READ_PTE_LOCK_FREE(*(unsigned __int64 *)(v_rsp - 248 - 112) + result * 8, a2, a3, a4);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 248 - 128)))) == 1) goto loc_0036E412;
    result = (unsigned __int8)((v_stack_m188) & (223));
    v_stack_m188 = (unsigned __int8)(result);
    *(unsigned __int8 *)(v_rsp - 248 - 48) = (unsigned __int8)(result);
loc_0036E0A2:
    v_stack_m1D0 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 248 - 48)));
    v_stack_m1D8 = result;
    result = MiInitializeReadInProgressPfn(*(unsigned __int64 *)(v_rsp - 248 - 80), result + 320, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 248 - 128)))), *(unsigned __int64 *)(v_rsp - 248 - 112) + result * 8);
    if ((((unsigned __int8)(v_rsi)) & (16)) != 0) goto loc_0036EB9D;
loc_0036E0CA:
    if (((v_stack_m188) & (16)) != 0) {
        a1 = *(unsigned __int64 *)(v_rsp - 248 + 272);
        a2 = 0;
        result = MiObtainProtoReference(a1, a2, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 248 - 128)))), *(unsigned __int64 *)(v_rsp - 248 - 112) + result * 8);
    }
    result = MI_READ_PTE_LOCK_FREE(*(unsigned __int64 *)(v_rsp - 248 + 264), a2, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 248 - 128)))), *(unsigned __int64 *)(v_rsp - 248 - 112) + result * 8);
    *(unsigned __int64 *)(result + 168) = result;
    *(unsigned __int64 *)(result + 232) = *(unsigned __int64 *)(v_rsp - 248 + 264);
    *(unsigned __int64 *)(v_rsp - 248 - 120) = result;
    if (*(unsigned __int64 *)(v_rsp - 248 - 96) != 0) goto loc_0036E84C;
loc_0036E11A:
    result = PsGetIoPriorityThread(*(unsigned __int64 *)(v_rsp - 248 + 32), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + 192)))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 248 - 128)))), (unsigned int)(*(unsigned int *)(result + 192)));
    if (((unsigned int)(result)) < 2) {
    }
    if (*(unsigned __int64 *)(v_rsp - 248 - 64) != 0) goto loc_0036E6D5;
loc_0036E13A:
    *(unsigned int *)(result + 192) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 192)));
    result = *(unsigned __int64 *)(v_rsp - 248 - 64);
    if (*(unsigned __int64 *)(v_rsp - 248 + 272) != 0) {
        a2 = 17;
        result = MiUnlockProtoPoolPage(*(unsigned __int64 *)(v_rsp - 248 + 272), a2, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 248 - 128)))), (unsigned int)(*(unsigned int *)(result + 192)));
    }
loc_0036E15F:
    if (*(unsigned __int64 *)(v_rsp - 248 - 40) == 0) goto loc_0036E8C3;
    result = (*(unsigned __int64 *)(v_rsp - 248 - 24)) - (1);
    *(unsigned __int64 *)(v_rsp - 248 - 40) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 248 - 40));
    *(unsigned __int64 *)(v_rsp - 248 - 24) = result;
    result = -(result);
    result = MiReleaseFreshPage(*(unsigned __int64 *)(v_rsp - 248 - 40), a2, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 248 - 128)))), (unsigned int)(*(unsigned int *)(result + 192)));
    goto loc_0036E15F;
loc_0036E18E:
    result = MiSufficientAvailablePages(v_stack_m180, 320, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 248 - 128)))), (unsigned int)(*(unsigned int *)(result + 192)));
    if ((unsigned int)(result) == 0) goto loc_0036DD50;
    v_r10 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rsp - 248 + 264)))) >> (3));
    v_r10 = (unsigned int)((v_r10) & (511));
    v_r12 = (unsigned int)((511) - ((unsigned int)(v_r10)));
    *(unsigned int *)(v_rsp - 248 - 72) = (unsigned int)(v_r10);
    if (((v_stack_m188) & (16)) != 0) goto loc_0036EA0E;
loc_0036E1D4:
    if (*(unsigned __int64 *)(v_rsp - 248 - 96) != 0) goto loc_0036E7E4;
    if ((((unsigned __int8)(v_rsi)) & (4)) != 0) goto loc_0036E7E4;
loc_0036E1EB:
    if (((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 248 - 40)))) <= 1) goto loc_0036EF61;
    *(unsigned __int64 *)(v_rsp - 248 - 120) = result;
    *(unsigned int *)(v_rsp - 248 - 128) = (unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 248 - 40)) - 1);
    *(unsigned __int64 *)(v_rsp - 248 - 56) = *(unsigned __int64 *)(v_rsp - 248 + 264) + 8;
    if (((unsigned int)(v_r12)) > ((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 248 - 40)) - 1))) { v_r12 = (unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 248 - 40)) - 1); }
    result = MiGetPagingFileOffset(result, *(unsigned __int64 *)(v_rsp - 248 + 264), 1, (unsigned int)(*(unsigned int *)(result + 192)));
    v_r13 = (unsigned int)(((unsigned int)(0xFFFFFFFDULL)) - ((unsigned int)((unsigned int)((unsigned int)(result)))));
    result = ((unsigned int)((unsigned int)(v_r12))) + ((unsigned int)((unsigned int)(result)));
    *(unsigned __int64 *)(v_rsp - 248 - 104) = (unsigned int)((unsigned int)(result));
    if (result < ((unsigned int)(0xFFFFFFFEULL))) { v_r13 = (unsigned int)(v_r12); }
    if (((1) & ((unsigned __int8)(v_rsi))) == 0) goto loc_0036E673;
loc_0036E241:
    v_rsi = (unsigned int)((v_rsi) | (8));
loc_0036E244:
    result = MI_CLEAR_PTE_BITS_FOR_READ_CLUSTER(v_rsp - 248 - 120, (unsigned int)((unsigned int)(result)), 1, (unsigned int)(*(unsigned int *)(result + 192)));
    if ((unsigned int)(v_r13) == 0) goto loc_0036E2BD;
loc_0036E263:
    v_r15 = (*(unsigned __int64 *)(v_rsp - 248 - 104)) + (1);
    result = MiUpdatePageFileHighInPte(*(unsigned __int64 *)(v_rsp - 248 - 120), v_r15, 1, (unsigned int)(*(unsigned int *)(result + 192)));
    result = MI_READ_PTE_LOCK_FREE(*(unsigned __int64 *)(v_rsp - 248 - 56), v_r15, 1, (unsigned int)(*(unsigned int *)(result + 192)));
    *(unsigned __int64 *)(v_rsp - 248 - 8) = result;
    if (((result) & (992)) == 0) goto loc_0036E618;
    result = MI_CLEAR_PTE_BITS_FOR_READ_CLUSTER(v_rsp - 248 - 8, v_r15, 1, (unsigned int)(*(unsigned int *)(result + 192)));
    if ((*(unsigned __int64 *)(v_rsp - 248 - 8)) != result) goto loc_0036E618;
    *(unsigned __int64 *)(v_rsp - 248 - 112) = *(unsigned __int64 *)(v_rsp - 248 - 56);
loc_0036E2A3:
    v_r12 = (*(unsigned __int64 *)(v_rsp - 248 - 56)) + (8);
    v_r13 = (unsigned int)((v_r13) + (-1));
    if (condition_is_not_equal) goto loc_0036E263;
loc_0036E2AD:
loc_0036E2BD:
    v_rdi = (*(unsigned __int64 *)(v_rsp - 248 - 112)) - (*(unsigned __int64 *)(v_rsp - 248 + 264));
    *(unsigned __int64 *)(v_rsp - 248 - 120) = *(unsigned __int64 *)(v_rsp - 248);
    v_rdi = (v_rdi) >> (3);
    v_r11 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 248 - 128))) - ((unsigned int)(v_rdi)));
    *(unsigned __int64 *)(v_rsp - 248 - 112) = v_rdi;
    *(unsigned int *)(v_rsp - 248 - 104) = (unsigned int)(v_r11);
    *(unsigned __int64 *)(v_rsp - 248 - 56) = *(unsigned __int64 *)(v_rsp - 248 + 264);
    v_r10 = (unsigned int)(*(unsigned int *)(v_rsp - 248 - 72));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 248 - 72)))) > ((unsigned int)(v_r11))) { v_r10 = (unsigned int)(v_r11); }
    result = MiGetPagingFileOffset(*(unsigned __int64 *)(v_rsp - 248), v_r15, 1, (unsigned int)(*(unsigned int *)(result + 192)));
    *(unsigned __int64 *)(v_rsp - 248 - 72) = (unsigned int)((unsigned int)(result));
    v_r13 = (unsigned int)(((unsigned int)((unsigned int)(result))) - 1);
    if (((unsigned int)((unsigned int)(v_r10))) <= ((unsigned int)((unsigned int)(result)) - 1)) { v_r13 = (unsigned int)(v_r10); }
    result = MI_CLEAR_PTE_BITS_FOR_READ_CLUSTER(v_rsp - 248 - 120, v_r15, 1, (unsigned int)(*(unsigned int *)(result + 192)));
    if ((unsigned int)(v_r13) == 0) goto loc_0036E384;
loc_0036E32A:
    v_r15 = (*(unsigned __int64 *)(v_rsp - 248 - 72)) - (1);
    v_r12 = (*(unsigned __int64 *)(v_rsp - 248 + 264)) - (8);
    result = MiUpdatePageFileHighInPte(*(unsigned __int64 *)(v_rsp - 248 - 120), v_r15, 1, (unsigned int)(*(unsigned int *)(result + 192)));
    result = MI_READ_PTE_LOCK_FREE(v_r12, v_r15, 1, (unsigned int)(*(unsigned int *)(result + 192)));
    *(unsigned __int64 *)(v_rsp - 248 - 8) = result;
    if (((result) & (992)) == 0) goto loc_0036E362;
    result = MI_CLEAR_PTE_BITS_FOR_READ_CLUSTER(v_rsp - 248 - 8, v_r15, 1, (unsigned int)(*(unsigned int *)(result + 192)));
    if ((*(unsigned __int64 *)(v_rsp - 248 - 8)) == result) goto loc_0036E36A;
loc_0036E362:
    if ((((unsigned __int8)(v_rsi)) & (8)) == 0) goto loc_0036E36E;
    goto loc_0036E374;
loc_0036E36A:
    *(unsigned __int64 *)(v_rsp - 248 - 56) = v_r12;
loc_0036E36E:
    v_r13 = (unsigned int)((v_r13) + (-1));
    if (condition_is_not_equal) goto loc_0036E32A;
loc_0036E374:
loc_0036E384:
    a2 = (*(unsigned __int64 *)(v_rsp - 248 + 264)) - (*(unsigned __int64 *)(v_rsp - 248 - 56));
    a2 = (a2) >> (3);
    if (*(unsigned __int64 *)(v_rip + 11270379) == 0) goto loc_0036E3B6;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rsp - 248))) & (16)) != 0) goto loc_0036E6B4;
    result = ~(*(unsigned __int64 *)(v_rip + 11270379));
    result = (result) & (*(unsigned __int64 *)(v_rsp - 248));
loc_0036E3B6:
    result = (result) >> (32);
    result = (result) - ((unsigned int)((unsigned int)(a2)));
    if (*(unsigned __int64 *)(v_rsp - 248) == 0) goto loc_0036E839;
    if (*(unsigned __int64 *)(v_rip + 11270379) == 0) goto loc_0036E3DD;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rsp - 248))) & (16)) != 0) goto loc_0036E6BD;
    a1 = ~(*(unsigned __int64 *)(v_rip + 11270379));
    v_rbx = (*(unsigned __int64 *)(v_rsp - 248)) & (a1);
loc_0036E3DD:
    result = (result) << (32);
    a1 = ((unsigned int)((unsigned int)(v_rbx))) | (result);
    result = MiSwizzleInvalidPte(a1, a2, (unsigned int)((unsigned int)(a2)), *(unsigned __int64 *)(v_rsp - 248 + 264));
    *(unsigned __int64 *)(v_rsp - 248 - 120) = result;
    result = (unsigned int)((*(unsigned __int64 *)(v_rsp - 248 - 112) + 1) + ((unsigned int)(a2)));
    *(unsigned int *)(v_rsp - 248 - 128) = (unsigned int)(result);
    v_rdi = (*(unsigned __int64 *)(v_rsp - 248 + 264)) - ((unsigned int)((unsigned int)(a2)) * 8);
    *(unsigned __int64 *)(v_rsp - 248 - 112) = v_rdi;
    goto loc_0036DD54;
loc_0036E412:
    result = (unsigned __int8)(((unsigned int)((unsigned int)(a2)) * 8) & (248));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 248 - 16) + 192))) >> (11));
    a1 = (unsigned __int8)((a1) & (7));
    a1 = (unsigned __int8)((a1) | ((unsigned __int8)(result)));
    a1 = (unsigned __int8)((a1) | (8));
    v_stack_m188 = (unsigned __int8)(a1);
    *(unsigned __int8 *)(v_rsp - 248 - 48) = (unsigned __int8)(a1);
    goto loc_0036E0A2;
loc_0036E433:
    if ((unsigned int)(result) != 0) goto loc_0036E9E7;
    if (*(unsigned __int64 *)(v_rsp - 248 - 96) != 0) goto loc_0036E7FA;
    if ((*(unsigned __int64 *)(v_rsp - 248 - 80)) <= result) goto loc_0036DCCA;
    *(unsigned int *)(v_rsp - 248 - 104) = (unsigned int)(v_r10);
    if ((((unsigned __int8)((unsigned int)((unsigned int)(a2)))) & (16)) != 0) goto loc_0036DCCA;
    if ((*(unsigned __int64 *)(v_rsp - 248 - 80)) < result) goto loc_0036E495;
    if ((*(unsigned __int64 *)(v_rsp - 248 - 80)) <= result) goto loc_0036DCCA;
loc_0036E495:
    v_rsi = (unsigned int)((v_rsi) | (4));
    *(unsigned int *)(v_rsp - 248 - 104) = 16;
    goto loc_0036DCCA;
loc_0036E4A4:
    if (sign_flag) goto loc_0036EF9C;
loc_0036E4AD:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 248 + 8) + 184)))) & (15)) != 0) goto loc_0036E4D8;
    if (*(unsigned __int64 *)(v_rsp - 248 + 272) != 0) goto loc_0036E4D8;
    result = MiGetCurrentSlabIdentity(*(unsigned __int64 *)(v_rsp - 248 + 32), a2, *(unsigned __int64 *)(v_rsp - 248 + 272), *(unsigned __int64 *)(v_rsp - 248 + 264));
    if (((unsigned __int8)(result)) != 255) goto loc_0036EC13;
loc_0036E4D8:
    if ((((unsigned __int8)(v_rsi)) & (64)) != 0) goto loc_0036EFC9;
loc_0036E4E2:
    v_rbx = 9;
    if (((v_stack_m188) & (32)) != 0) { v_rbx = (unsigned int)(*(unsigned __int64 *)(v_rsp - 248 - 56)); }
loc_0036E4F0:
    if ((*(unsigned __int64 *)(v_rsp - 248 - 24)) != (*(unsigned __int64 *)(v_rsp - 248 + 264))) goto loc_0036DDB6;
    *(unsigned __int64 *)(v_rsp - 248) = v_rdi;
    result = MiProtectionToCacheAttribute((unsigned int)(*(unsigned int *)(v_rsp - 248 + 48)), a2, *(unsigned __int64 *)(v_rsp - 248 + 272), *(unsigned __int64 *)(v_rsp - 248 + 264));
    *(unsigned int *)(v_rsp - 248 - 84) = (unsigned int)(result);
    v_r13 = (*(unsigned __int64 *)(v_rsp - 248 - 112)) << (25);
    a1 = (result) << (25);
    v_r13 = (v_r13) - (a1);
    v_r13 = (v_r13) >> (16);
loc_0036E52D:
    a2 = 0;
    result = memset(v_rsp - 248 + 64, a2, a2 + 112, *(unsigned __int64 *)(v_rsp - 248 + 264));
    v_stack_m198 = v_rsp - 248 + 64;
    v_stack_m1A0 = v_rdi;
    a3 = (unsigned int)((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rsp - 248 + 256) + 69)) & (1));
    v_stack_m1A8 = v_rsp - 248 + 24;
    v_stack_m1B0 = (unsigned int)(v_rbx);
    v_stack_m1B8 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 248 + 256) + 96);
    v_stack_m1C8 = (unsigned int)(*(unsigned __int64 *)(v_rsp - 248 - 112) + result * 8);
    v_stack_m1D0 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 248 - 84)));
    v_stack_m1D8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 248 - 84)));
    result = MiInitializePageChainPacket(v_stack_m180, *(unsigned __int64 *)(v_rsp - 248 + 8), a3, v_r13);
    result = MiGetPageChain(v_rsp - 248 + 64, *(unsigned __int64 *)(v_rsp - 248 + 8), a3, v_r13);
    if (*(unsigned __int64 *)(v_rsp - 248 + 168) == 0) goto loc_0036EDC0;
    if ((*(unsigned __int64 *)(v_rsp - 248 - 40)) != 0) goto loc_0036EC91;
    *(unsigned __int64 *)(v_rsp - 248 - 40) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 248 - 24) = v_xmm1;
loc_0036E5D4:
    if ((*(unsigned __int64 *)(v_rsp - 248 - 24)) == 0) goto loc_0036E87B;
    goto loc_0036DDB6;
loc_0036E5ED:
    result = (*(unsigned __int64 *)(v_rsp - 248 - 120)) >> (12);
    result = (unsigned int)((result) & (15));
    a2 = (((unsigned int)(result)) == ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m180 + 1204))))) ? 1 : 0;
    goto loc_0036DCB8;
loc_0036E618:
    if ((((unsigned __int8)(v_rsi)) & (8)) == 0) goto loc_0036E2A3;
    goto loc_0036E2AD;
loc_0036E627:
loc_0036E62D:
    if ((((unsigned __int8)(v_rsi)) & (8)) == 0) goto loc_0036E6FB;
    if ((*(unsigned __int64 *)(v_rsp - 248 - 112)) <= (*(unsigned __int64 *)(v_rsp - 248 + 264))) goto loc_0036ECB3;
    *(unsigned int *)(v_rsp - 248 - 128) = (unsigned int)(*(unsigned __int64 *)(v_rsp - 248 + 272));
    goto loc_0036DFBF;
loc_0036E653:
    result = (unsigned int)(*(unsigned int *)(v_rsp - 248 - 104));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 248 - 104)))) > ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 248 - 96) + 1208))))) { result = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 248 - 96) + 1208))); }
    *(unsigned int *)(v_rsp - 248 - 104) = (unsigned int)(result);
    goto loc_0036DCD8;
loc_0036E66B:
    goto loc_0036DF24;
loc_0036E673:
    if ((*(unsigned __int64 *)(v_rsp - 248 - 96)) == 0) goto loc_0036E244;
    goto loc_0036E241;
loc_0036E683:
    a2 = ((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rsp - 248 - 112) + result * 8))) & (-17);
    goto loc_0036DE3A;
loc_0036E68C:
    goto loc_0036DE4A;
loc_0036E694:
    result = (result) & (-17);
    goto loc_0036DF9D;
loc_0036E69D:
    goto loc_0036DE4A;
loc_0036E6A9:
    goto loc_0036DEAB;
loc_0036E6B4:
    result = (result) & (-17);
    goto loc_0036E3B6;
loc_0036E6BD:
    v_rbx = (v_rbx) & (-17);
    goto loc_0036E3DD;
loc_0036E6C6:
    a4 = 0;
    goto loc_0036E016;
loc_0036E6CE:
    result = 0;
    goto loc_0036DF9D;
loc_0036E6D5:
    result = ((unsigned int)(*(unsigned int *)(result + 48))) >> (19);
    result = (unsigned int)((result) & (3));
    if ((*(unsigned __int64 *)(v_rip - 3514727 + result * 8)) != 16) goto loc_0036E13A;
    goto loc_0036E13A;
loc_0036E6FB:
    v_rsi = (unsigned int)((v_rsi) | (2));
    *(unsigned __int64 *)(v_rbx) = *(unsigned __int64 *)(v_rip + 11308342);
    goto loc_0036DF29;
loc_0036E70D:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rsp - 248 - 64))) != 1) goto loc_0036DD96;
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 248 - 64) + 80))) >> (3));
    a2 = (unsigned int)((a2) & (7));
    a2 = (unsigned int)((a2) + (1));
    result = MiGetAvailablePagesBelowPriority(v_stack_m180, a2, *(unsigned __int64 *)(v_rsp - 248 - 120), a4);
    if (result <= ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rsp - 248 + 272))))))) goto loc_0036DD9E;
    goto loc_0036DD9E;
loc_0036E74B:
    v_stack_m188 = 16;
    a1 = ((unsigned int)(*(unsigned int *)(v_rsp - 248 - 84))) >> (9);
    a1 = (a1) & ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rsp - 248 + 272))))));
    a1 = (a1) + (*(unsigned __int64 *)(v_rsp - 248 - 120));
    result = MI_READ_PTE_LOCK_FREE(a1, a2, *(unsigned __int64 *)(v_rsp - 248 - 120), a4);
    result = MI_PROTO_FORMAT_COMBINED(result, a2, *(unsigned __int64 *)(v_rsp - 248 - 120), a4);
    if ((unsigned __int8)(result) != 0) goto loc_0036E83E;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 248 - 96) + 640)) == 0) goto loc_0036DB5F;
    goto loc_0036E843;
loc_0036E793:
    if (((*(unsigned int *)(v_stack_m180 + 80)) & (512)) == 0) goto loc_0036DAF9;
    result = MiIsPteInStore(result, v_rbx, *(unsigned __int64 *)(v_rsp - 248 - 120), a4);
    if ((unsigned int)(result) == 0) goto loc_0036DAF9;
    if ((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rsp - 248 + 272))))))) != 0) {
        a2 = 17;
        a1 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rsp - 248 + 272)))))));
        result = MiUnlockProtoPoolPage(a1, a2, *(unsigned __int64 *)(v_rsp - 248 - 120), a4);
    }
    result = 0;
    goto loc_0036E9AA;
loc_0036E7C7:
    if ((*(unsigned __int8 *)(result)) != 1) goto loc_0036DD40;
    result = MiSetInPagePrefetchPriority(0, *(unsigned __int64 *)(v_rsp - 248 - 96), *(unsigned __int64 *)(v_rsp - 248 - 120), a4);
    goto loc_0036DD40;
loc_0036E7E4:
    v_r10 = 0;
    *(unsigned int *)(v_rsp - 248 - 72) = 0;
    v_rdi = (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rsp - 248 + 272)))))));
    if ((unsigned int)(*(unsigned __int64 *)(v_rsp - 248 - 96)) == 0) { v_rdi = (unsigned int)(*(unsigned __int64 *)(v_rsp - 248 - 120)); }
    *(unsigned int *)(v_rsp - 248 - 104) = (unsigned int)(v_rdi);
    goto loc_0036E1EB;
loc_0036E7FA:
    if (v_stack_m180 == 0) goto loc_0036EC4F;
loc_0036E803:
    a2 = (unsigned int)(((unsigned int)((unsigned int)(v_rsi))) & (0));
    a4 = (unsigned int)(((unsigned int)((unsigned int)(a2))) | (2));
    if (((v_stack_m188) & (16)) == 0) { a4 = (unsigned int)(a2); }
    result = MiComputeFaultCluster(v_stack_m180, *(unsigned __int64 *)(v_rsp - 248 - 96), v_stack_m180, a4);
    *(unsigned int *)(v_rsp - 248 - 104) = (unsigned int)(result);
    goto loc_0036DCCF;
loc_0036E839:
    goto loc_0036E3DD;
loc_0036E83E:
    v_stack_m188 = 48;
loc_0036E843:
    *(unsigned int *)(v_rsp - 248 - 104) = (unsigned int)(v_stack_m180);
    goto loc_0036DB5F;
loc_0036E84C:
    if ((*(unsigned __int8 *)((unsigned int)(*(unsigned int *)(v_rsp - 248 - 84)))) != 1) goto loc_0036E11A;
    a4 = (unsigned int)((a4) | (32));
    if (((*(unsigned int *)((unsigned int)(*(unsigned int *)(v_rsp - 248 - 84)) + 80)) & (0x2000ULL)) == 0) goto loc_0036E11A;
    a4 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rsp - 248 - 96)))) | (160));
    goto loc_0036E11A;
loc_0036E87B:
    if (sign_flag) goto loc_0036F044;
loc_0036E884:
    if (*(unsigned __int64 *)(v_rsp - 248 + 272) != 0) goto loc_0036F071;
loc_0036E894:
    result = MiFreeInPageSupportBlock(v_stack_m180, *(unsigned __int64 *)(v_rsp - 248 - 96), v_stack_m180, a4);
    if (*(unsigned __int64 *)(v_rsp - 248 - 96) != 0) goto loc_0036F07D;
loc_0036E8A9:
    result = MiReturnFaultCharges(v_stack_m180, *(unsigned __int64 *)(v_rsp - 248 - 56), (unsigned int)(*(unsigned int *)(v_rsp - 248 - 88)), a4);
    goto loc_0036E9AA;
loc_0036E8C3:
    result = (unsigned int)(*(unsigned int *)(v_rsp - 248 + 256));
    if (((unsigned int)(*(unsigned int *)(v_rsp - 248 + 256))) != (*(unsigned __int64 *)(v_rsp - 248 - 56))) {
        a3 = *(unsigned int *)(v_rsp - 248 - 88);
        a2 = (*(unsigned __int64 *)(v_rsp - 248 - 56)) - ((unsigned int)(*(unsigned int *)(v_rsp - 248 + 256)));
        a1 = v_stack_m180;
        result = MiReturnFaultCharges(a1, a2, a3, a4);
    }
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 248 + 280)) = *(unsigned __int64 *)(v_rsp - 248 - 96);
    result = MiGetPagingFileOffset(v_rbx, a2, a3, a4);
    v_rbx = (v_rbx) >> (12);
    v_rbx = (unsigned int)((v_rbx) & (15));
    *(unsigned int *)(v_rsp - 248 + 40) = (unsigned int)((unsigned int)((unsigned int)(result)));
    if (((v_stack_m188) & (16)) != 0) {
        a1 = *(unsigned __int64 *)(v_rsp - 248 + 272);
        *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 248 - 96) + 160) = a1;
    }
    if (((1) & ((unsigned __int8)(v_rsi))) == 0) goto loc_0036E9BF;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 248 - 96) + 96) = (unsigned int)((unsigned int)(result));
loc_0036E948:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 248 - 96) + 200) = *(unsigned __int64 *)(v_stack_m180 + v_rbx * 8 + 18528);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m180 + v_rbx * 8 + 18528) + 184)) != 0) goto loc_0036E9D5;
loc_0036E95E:
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 248 - 96) + 192) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 248 - 96) + 192)));
    a2 = (v_stack_m180 * 2) + (v_stack_m180);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 248 - 96) + 240) = *(unsigned __int64 *)(v_rsp - 248 - 112) + result * 8;
    a2 = (a2) << (4);
    a2 = (a2) + ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 248 - 96) + 192)));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 248 - 96) + 248) = a2;
    if (condition_is_below) goto loc_0036F0E3;
loc_0036E9A5:
loc_0036E9AA:
    v_rsp = (v_rsp) + (440);
    return (unsigned int)(0xC0033333ULL);
loc_0036E9BF:
    a1 = (*(unsigned __int64 *)(v_rsp - 248 + 40)) << (12);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 248 - 96) + 96) = a1;
    goto loc_0036E948;
loc_0036E9D5:
    if (*(unsigned __int64 *)(v_rsp - 248 - 96) != 0) goto loc_0036ED31;
loc_0036E9DE:
    goto loc_0036E95E;
loc_0036E9E7:
    result = (unsigned int)(((unsigned int)(0xC0033333ULL)) - 1);
    *(unsigned int *)(v_rsp - 248 - 104) = 1;
    *(unsigned int *)(v_rip + 11307429) = (unsigned int)(result);
    goto loc_0036DCCA;
loc_0036E9F8:
    result = MiSharedVaToPartition(v_stack_m180, *(unsigned __int64 *)(v_rsp - 248 - 96), *(unsigned __int64 *)(v_rsp - 248 - 112) + result * 8, 1);
    goto loc_0036DA68;
loc_0036EA0E:
    if (v_stack_m180 != 0) goto loc_0036ED96;
    result = MiLockVadTree(v_stack_m180 + 1, *(unsigned __int64 *)(v_rsp - 248 - 96), *(unsigned __int64 *)(v_rsp - 248 - 112) + result * 8, 1);
    result = MiLocateAddress(*(unsigned __int64 *)(v_rsp - 248 - 80), *(unsigned __int64 *)(v_rsp - 248 - 96), *(unsigned __int64 *)(v_rsp - 248 - 112) + result * 8, 1);
    *(unsigned __int64 *)(v_rsp - 248 - 64) = result;
    result = MiUnlockVadTree(1, 17, *(unsigned __int64 *)(v_rsp - 248 - 112) + result * 8, 1);
    if (result == 0) goto loc_0036EC1D;
loc_0036EA48:
    if (((*(unsigned int *)(result + 48)) & (0x200000ULL)) != 0) goto loc_0036EC1D;
    a2 = (*(unsigned __int64 *)(v_rsp - 248 - 80)) >> (12);
    result = MiGetProtoPteAddress(result, a2, 12, v_rsp - 248 + 16);
    if (*(unsigned __int64 *)(v_rsp - 248 + 16) == 0) goto loc_0036EC1D;
    if (condition_is_below) goto loc_0036EC1D;
    result = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 248 + 16) + 44))) << (3);
    result = (result) - (*(unsigned __int64 *)(v_rsp - 248 + 264));
    result = (result) + (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 248 + 16) + 8));
    result = (result) >> (3);
    result = (unsigned int)((result) - 1);
    v_r12 = *(unsigned __int64 *)(v_rsp - 248 - 96);
    if (((unsigned int)(result)) < ((unsigned int)(*(unsigned __int64 *)(v_rsp - 248 - 96)))) { v_r12 = (unsigned int)(result); }
    result = (*(unsigned __int64 *)(v_rsp - 248 + 264)) - (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 248 + 16) + 8));
    result = (result) >> (3);
    if (((unsigned int)(result)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 248 - 72))))) goto loc_0036E1D4;
    *(unsigned int *)(v_rsp - 248 - 72) = (unsigned int)(result);
    goto loc_0036E1D4;
loc_0036EADD:
    result = MiIsStoreProcess(v_r12, *(unsigned __int64 *)(v_rsp - 248 + 264), 1, v_rsp - 248 + 16);
    if ((unsigned int)(result) != 0) goto loc_0036DC59;
loc_0036EAED:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 248 + 8) + 184)))) & (15)) != 0) goto loc_0036EB32;
    if ((*(unsigned __int64 *)(v_rsp - 248 - 80)) >= ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 248 + 8) + 184)))) goto loc_0036EB32;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_r12 + 1040) + 1168)) != 0) goto loc_0036DC52;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_r12 + 1040) + 1176)) != 0) goto loc_0036DC52;
loc_0036EB32:
    goto loc_0036DC8E;
loc_0036EB42:
    a4 = (*(unsigned __int64 *)(v_rsp - 248 - 96)) & (-2);
    if (((unsigned __int8)(*(unsigned __int8 *)(a4))) == 5) goto loc_0036ED9F;
    if (((unsigned __int8)(*(unsigned __int8 *)(a4))) == ((unsigned __int8)(v_r12))) goto loc_0036EC3A;
    if (((unsigned __int8)(*(unsigned __int8 *)(a4))) != ((unsigned __int8)(*(unsigned __int64 *)(v_rsp - 248 - 112) + result * 8))) goto loc_0036DA92;
    *(unsigned __int64 *)(v_rsp - 248 - 96) = a4;
    if (((*(unsigned __int64 *)(v_rsp - 248 + 264)) & (v_rbx)) != 0) goto loc_0036E7C0;
    result = MiGetPagingFileOffset(v_rbx, *(unsigned __int64 *)(v_rsp - 248 + 264), 1, a4);
    if ((unsigned int)(result) == 0) goto loc_0036E7C0;
    v_r12 = 0;
    *(unsigned int *)(v_rsp - 248 - 72) = 0;
    v_rsi = (unsigned int)((v_rsi) | (32));
    *(unsigned __int64 *)(v_rsp - 248 - 16) = *(unsigned __int64 *)(a4 + 112);
    goto loc_0036DA92;
loc_0036EB9D:
    if (*(unsigned __int64 *)(v_rip + 11268316) == 0) goto loc_0036EBB8;
    if ((((unsigned __int8)(v_rbx)) & (16)) != 0) goto loc_0036EC46;
    result = ~(*(unsigned __int64 *)(v_rip + 11268316));
    v_rbx = (v_rbx) & (result);
loc_0036EBB8:
    v_rbx = (v_rbx) >> (12);
    v_rbx = (v_rbx) & (result);
    v_rbx = (v_rbx + v_rbx * 2) << (4);
    v_rbx = (v_rbx) + (result);
    result = MiFlowThroughInsertNode(0, v_rbx, 1, a4);
    goto loc_0036E0CA;
loc_0036EBF5:
    result = MiReduceMdl(*(unsigned __int64 *)(v_rsp - 248 - 96), v_rbx, 1, a4);
    if (result != 0) goto loc_0036F0CA;
loc_0036EC06:
    v_r15 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 248 - 96) + 40))) >> (12));
    goto loc_0036E07C;
loc_0036EC13:
    goto loc_0036E4F0;
loc_0036EC1D:
    *(unsigned int *)(v_rsp - 248 - 104) = 1;
    goto loc_0036E1D4;
loc_0036EC3A:
    *(unsigned __int64 *)(v_rsp - 248 - 96) = a4;
    goto loc_0036DA92;
loc_0036EC46:
    v_rbx = (8) & (-17);
    goto loc_0036EBB8;
loc_0036EC4F:
    if (a4 > result) goto loc_0036E803;
    result = MiLockVadTree((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 248 - 72)))), *(unsigned __int64 *)(v_rsp - 248 + 264), 1, a4);
    result = MiLocateAddress(*(unsigned __int64 *)(v_rsp - 248 - 80), *(unsigned __int64 *)(v_rsp - 248 + 264), 1, a4);
    *(unsigned __int64 *)(v_rsp - 248 - 64) = result;
    result = MiUnlockVadTree(1, 17, 1, a4);
    goto loc_0036E803;
loc_0036EC91:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 248 - 32)) = *(unsigned __int64 *)(v_rsp - 248 + 152);
    *(unsigned __int64 *)(v_rsp - 248 - 32) = *(unsigned __int64 *)(v_rsp - 248 + 160);
    goto loc_0036E5D4;
loc_0036ECB3:
    if (1 == 0) goto loc_0036ED10;
loc_0036ECCB:
    result = *(unsigned __int64 *)(result);
    v_r15 = (unsigned int)(*(unsigned int *)(v_rsp - 248 + 256));
    if ((*(unsigned __int64 *)(result)) != (*(unsigned __int64 *)(v_rip + 11306851))) {
        a1 = *(unsigned __int64 *)(result) + *(unsigned __int64 *)(result) * 2;
        a1 = (a1) << (4);
        result = 0;
        a1 = (a1) + (result);
        result = MiReleaseFreshPageAtDpc(a1, 17, 1, a4);
        v_r15 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 248 + 256))) - 1);
    }
    v_rbx = (result) + (8);
    v_rdi = (unsigned int)((1) + (-1));
    if (condition_is_not_equal) goto loc_0036ECCB;
    *(unsigned int *)(v_rsp - 248 + 256) = (unsigned int)(v_r15);
loc_0036ED10:
    v_rsi = (unsigned int)((v_rsi) & (0xFFFFFFFDULL));
    *(unsigned __int64 *)(v_rsp - 248 - 112) = *(unsigned __int64 *)(v_rsp - 248 + 264);
    result = MI_READ_PTE_LOCK_FREE(*(unsigned __int64 *)(v_rsp - 248 + 264), 17, 1, a4);
    *(unsigned __int64 *)(v_rsp - 248 - 120) = result;
    goto loc_0036DDEF;
loc_0036ED31:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rsp - 248 - 16) + 272)) != ((unsigned __int8)(a4))) goto loc_0036E9DE;
    if (((*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 248 - 16) + 272 + 80)) & (0x1000ULL)) == 0) goto loc_0036E9DE;
    if ((((unsigned __int8)(a4)) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 12936370))))) == 0) goto loc_0036E95E;
    goto loc_0036E9DE;
loc_0036ED5C:
    result = MiKernelStackVaToStackNode(*(unsigned __int64 *)(v_rsp - 248 - 80), *(unsigned __int64 *)(v_rsp - 248 - 112) + result * 8, 1, a4);
    if (result != 0) goto loc_0036EEE0;
    v_stack_p78 = v_rip + 11313023;
loc_0036ED89:
    v_r12 = (unsigned int)((*(unsigned __int64 *)(v_rsp - 248 - 16)) | (8));
    *(unsigned int *)(v_rsp - 248 - 72) = (unsigned int)(v_r12);
    goto loc_0036DAEF;
loc_0036ED96:
    goto loc_0036EA48;
loc_0036ED9F:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a4 + 56)))) & (4)) != 0) goto loc_0036EEBA;
loc_0036EDAB:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a4 + 56)))) & (32)) != 0) goto loc_0036EED8;
loc_0036EDB7:
    *(unsigned __int64 *)(v_rsp - 248 - 96) = result;
    goto loc_0036DA92;
loc_0036EDC0:
    if (((unsigned int)(result)) == 9) goto loc_0036E5D4;
    if (*(unsigned __int64 *)(v_rsp - 248 + 24) != 0) goto loc_0036F000;
    if (((unsigned int)(result)) != 6) goto loc_0036EFE7;
loc_0036EDEE:
    goto loc_0036E52D;
loc_0036EDFC:
    result = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rsp - 248 - 56) + 34))) & (40));
    if (((unsigned __int8)(result)) == 40) goto loc_0036EF3F;
    if ((((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rsp - 248 - 56) + 34))) & (32)) == 0) goto loc_0036EF3F;
    if ((*(unsigned __int64 *)(v_rsp - 248 - 120)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 248 - 56) + 16))) goto loc_0036EF3F;
    if (sign_flag) goto loc_0036EF3F;
    goto loc_0036DD33;
loc_0036EE40:
    if ((*(unsigned __int64 *)(v_rsp - 248 - 112) + *(unsigned __int64 *)(v_rsp - 248) * 8) <= (*(unsigned __int64 *)(v_rsp - 248 + 264))) goto loc_0036F09D;
    goto loc_0036DDC2;
loc_0036EE60:
    if (*(unsigned __int64 *)(v_rsp - 248 + 272) != 0) goto loc_0036EEB1;
loc_0036EE6C:
    goto loc_0036E9AA;
loc_0036EE76:
    result = (*(unsigned __int64 *)(v_rsp - 248 - 56)) + (*(unsigned __int64 *)(v_rsp - 248 + 272));
    if ((*(unsigned __int64 *)(v_rsp - 248 + 264)) > result) goto loc_0036EAED;
    if ((*(unsigned __int64 *)(v_rsp - 248 + 264)) >= (*(unsigned __int64 *)(v_rsp - 248 - 56))) goto loc_0036EADD;
    goto loc_0036EAED;
loc_0036EEB1:
    result = MiUnlockProtoPoolPage(*(unsigned __int64 *)(v_rsp - 248 + 264), 17, 1, *(unsigned __int64 *)(v_rsp - 248 - 112));
    goto loc_0036EE6C;
loc_0036EEBA:
    result = MiIsPteInStore(*(unsigned __int64 *)(v_rsp - 248 + 264), *(unsigned __int64 *)(v_rsp - 248 - 120), 1, *(unsigned __int64 *)(v_rsp - 248 - 112));
    if ((unsigned int)(result) != 0) goto loc_0036EDAB;
loc_0036EED8:
    v_rsi = (unsigned int)((v_rsi) | (64));
    goto loc_0036EDB7;
loc_0036EEE0:
    v_stack_p78 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11276701) + *(unsigned __int16 *)(result + 40) * 8);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11276701) + *(unsigned __int16 *)(result + 40) * 8)) == (v_rip + 11312650)) goto loc_0036ED89;
    if ((((unsigned __int8)(v_rsi)) & (32)) == 0) goto loc_0036ED89;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rsp - 248 - 64))) != 1) goto loc_0036ED89;
    goto loc_0036ED89;
loc_0036EF26:
    result = (unsigned int)((1) | ((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rsp - 248))))));
    *(unsigned int *)(v_rsp - 248 - 104) = (unsigned int)((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rsp - 248))));
    *(unsigned int *)(v_rsp - 248 - 88) = (unsigned int)(result);
    goto loc_0036DCA7;
loc_0036EF35:
loc_0036EF3F:
    result = MiUnlockProtoPoolPage(*(unsigned __int64 *)(v_rsp - 248 + 272), 17, 1, *(unsigned __int64 *)(v_rsp - 248 - 112));
loc_0036EF61:
    goto loc_0036DD58;
loc_0036EF6E:
    a2 = ~(*(unsigned __int64 *)(v_rip + 11267339));
    a2 = (a2) & (*(unsigned __int64 *)(v_rsp - 248 - 120));
loc_0036EF9C:
    result = PsReferencePartitionSafe(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 248 - 64) + 184), a2, *(unsigned __int64 *)(v_rip + 11267339), *(unsigned __int64 *)(v_rsp - 248 - 112));
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 248 - 16) + 192) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 248 - 16) + 192)));
    goto loc_0036E4AD;
loc_0036EFC9:
    if (*(unsigned __int64 *)(v_rip + 11267339) != 0) goto loc_0036E4E2;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 248 - 64) + 4)))) & (8)) == 0) goto loc_0036E4E2;
    goto loc_0036E4F0;
loc_0036EFE7:
    if (((unsigned int)(*(unsigned __int64 *)(v_rip + 11267339) + 2)) != 8) goto loc_0036EDEE;
    goto loc_0036EDEE;
loc_0036F000:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 248 + 256) + 136) = v_stack_p78;
    result = ExAcquireRundownProtection(v_stack_p78 + 18376, a2, *(unsigned __int64 *)(v_rip + 11267339), *(unsigned __int64 *)(v_rsp - 248 - 112));
loc_0036F044:
    result = PsDereferencePartition(*(unsigned __int64 *)(v_stack_p78 + 184), *(unsigned __int64 *)(v_rsp - 248 + 24), *(unsigned __int64 *)(v_rip + 11267339), *(unsigned __int64 *)(v_rsp - 248 - 112));
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 248 - 16) + 192) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 248 - 16) + 192)));
    goto loc_0036DDAD;
loc_0036F071:
    result = MiUnlockProtoPoolPage(*(unsigned __int64 *)(v_stack_p78 + 184), 17, *(unsigned __int64 *)(v_rip + 11267339), *(unsigned __int64 *)(v_rsp - 248 - 24));
    goto loc_0036E894;
loc_0036F07D:
    result = -(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 248 + 256) + 128));
    a1 = (unsigned __int8)((*(unsigned __int64 *)(v_stack_p78 + 184)) + (2));
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_rsp - 248 - 16) + 1) = (unsigned __int8)(a1);
    goto loc_0036E8A9;
loc_0036F09D:
    a2 = ~(*(unsigned __int64 *)(v_rip + 11267036));
    a2 = (a2) & (*(unsigned __int64 *)(v_rsp - 248 - 120));
loc_0036F0CA:
    if ((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 248 - 16) + 192))) != 0) goto loc_0036EC06;
    result = (*(unsigned __int64 *)(v_rsp - 248 - 120)) << (12);
    goto loc_0036EC06;
loc_0036F0E3:
    result = MiReadFromMemoryPagefile(*(unsigned __int64 *)(v_rip + 11267036), *(unsigned __int64 *)(v_rsp - 248 - 16), *(unsigned __int64 *)(v_rip + 11267036), *(unsigned __int64 *)(v_rsp - 248 - 24));
    goto loc_0036E9A5;
}
```

## 5. (Beta) C Style

```c
int64_t MiResolvePageFileFault(void *Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

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
    uint64_t v_stack_m180;
    uint8_t v_stack_m188;
    uint64_t v_stack_m198;
    uint64_t v_stack_m1A0;
    uint64_t v_stack_m1A8;
    uint32_t v_stack_m1B0;
    uint64_t v_stack_m1B8;
    uint64_t v_stack_m1C0;
    uint32_t v_stack_m1C8;
    uint32_t v_stack_m1D0;
    uint64_t v_stack_m1D8;
    uint64_t v_stack_p78;

    *(uint64_t *)(local_rsp + 0x20) = Arg4;
    *(uint64_t *)(local_rsp + 0x18) = Arg3;
    *(uint64_t *)(local_rsp + 0x10) = Arg2;
    *(void **)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (440);
    local_rdi = 0;
    *(uint64_t *)(local_rsp - 0xF8 + 0x10) = 0;
    *(uint64_t *)(local_rsp - 0xF8 + 0x28) = 0;
    *(uint64_t *)(local_rsp - 0xF8 - 0x50) = *(uint64_t *)(arg1);
    *(uint64_t *)(local_rsp - 0xF8 + 0x8) = *(uint64_t *)(arg1 + 0x38);
    result = MI_READ_PTE_LOCK_FREE(Arg2, Arg2, Arg3, Arg4);
    *(uint64_t *)(local_rsp - 0xF8) = result;
    *(uint64_t *)(local_rsp - 0xF8 + 0x20) = *(uint64_t *)(gs_base + (0 + 0x188));
    if (((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5A8)) & (4)) != 0) goto loc_0036EE60;
    if ((((uint32_t)(0x800ULL)) & (result)) == 0) goto loc_0036DBEA;
    if (*(uint64_t *)(v_rip + 0xAC0277) == 0) goto loc_0036DA23;
    if ((((uint8_t)(result)) & (16)) != 0) goto loc_0036DC49;
    result = ~(*(uint64_t *)(v_rip + 0xAC0277));
    result = (result) & (result);
loc_0036DA23:
    result = (result) >> (12);
    result = (result) & (Arg4);
    Arg2 = (result + result * 2) << (4);
    Arg2 = (Arg2) + (Arg3);
    *(uint64_t *)(local_rsp - 0xF8 - 0x38) = Arg2;
    *(uint64_t *)(local_rsp - 0xF8 - 0x78) = *(uint64_t *)(Arg2 + 0x10);
    result = (*(uint64_t *)(Arg2 + 0x28)) >> (43);
    result = (uint32_t)((result) & (0x3FFULL));
loc_0036DA68:
loc_0036DA6D:
    local_r13 = 0;
    v_stack_m180 = *(uint64_t *)(*(uint64_t *)(v_rip + 0xAC2634) + result * 8);
    *(uint64_t *)(local_rsp - 0xF8 - 0x60) = 0;
    *(uint32_t *)(local_rsp - 0xF8 - 0x48) = (uint32_t)(local_r13 + 2);
    if ((((uint8_t)(local_r13 + 1)) & ((uint8_t)(*(uint64_t *)(arg1 + 0x10)))) != 0) goto loc_0036EB42;
loc_0036DA92:
    result = MiGetSystemRegionType(*(uint64_t *)(local_rsp - 0xF8 - 0x50), (uint32_t)(0x800ULL), Arg3, Arg4);
    if ((((uint8_t)(local_r13 + 1)) & ((uint8_t)(*(uint64_t *)(arg1 + 0x10)))) == 0) goto loc_0036DC1A;
    local_r15 = (*(uint64_t *)(arg1 + 0x10)) & (-2);
    if ((*(uint8_t *)(local_r15)) != 4) goto loc_0036DC1A;
    local_r12 = (uint32_t)((local_r13 + 2) | (8));
    *(uint64_t *)(local_rsp - 0xF8 - 0x60) = local_r15;
    *(uint32_t *)(local_rsp - 0xF8 - 0x48) = (uint32_t)(local_r12);
    v_stack_m180 = *(uint64_t *)(*(uint64_t *)(v_rip + 0xAC25AD) + *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(local_r15 + 0x30) + 0x220) + 0x4AE) * 8);
loc_0036DAEB:
loc_0036DAEF:
    if (((16) & (32)) != 0) goto loc_0036E793;
loc_0036DAF9:
    *(uint32_t *)(local_rsp - 0xF8 - 0x80) = 1;
    *(uint64_t *)(local_rsp - 0xF8 - 0x70) = *(uint64_t *)(local_rsp - 0xF8 + 0x108);
    *(uint32_t *)(local_rsp - 0xF8 - 0x58) = 2;
    *(uint32_t *)(local_rsp - 0xF8 - 0x68) = 16;
    if ((*(uint64_t *)(local_rsp - 0xF8 + 0x108)) < Arg3) goto loc_0036E74B;
    if ((*(uint64_t *)(local_rsp - 0xF8 + 0x108)) > (*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(local_r15 + 0x30) + 0x220) + 0x4AE))) goto loc_0036E74B;
    v_stack_m188 = (uint8_t)(*(uint8_t *)(local_rsp - 0xF8 - 0x30));
loc_0036DB5F:
    Arg2 = 0;
    result = (result) >> (5);
    result = (uint32_t)((result) & (31));
    *(uint64_t *)(local_rsp - 0xF8 + 0x30) = result;
    *(uint64_t *)(local_rsp - 0xF8 - 0x40) = *(uint64_t *)(*(uint64_t *)(local_rsp - 0xF8 + 0x100) + 0x58);
    result = MiComputeFaultNode(*(uint64_t *)(local_rsp - 0xF8 + 0x100), Arg2, local_rsp - 248 - 64, Arg4);
    *(uint32_t *)(local_rsp - 0xF8 - 0x54) = (uint32_t)(result);
    if (*(uint64_t *)(local_rsp - 0xF8 - 0x40) == 0) goto loc_0036EE76;
loc_0036DB9A:
    Arg2 = (*(uint8_t *)(*(uint64_t *)(local_rsp - 0xF8 - 0x40) + 0x22)) << (32);
    Arg2 = (Arg2) | ((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0xF8 - 0x40) + 0x34)));
    if (Arg2 != (*(uint64_t *)(local_rsp - 0xF8 - 0x40))) goto loc_0036EB32;
    Arg3 = (uint8_t)((v_stack_m188) | (128));
    v_stack_m188 = (uint8_t)(Arg3);
    *(uint32_t *)(local_rsp - 0xF8 - 0x58) = 7;
    goto loc_0036DC96;
loc_0036DBEA:
    *(uint64_t *)(local_rsp - 0xF8 - 0x38) = *(uint64_t *)(local_rsp - 0xF8 + 0x110);
    *(uint64_t *)(local_rsp - 0xF8 - 0x78) = result;
    if (*(uint64_t *)(local_rsp - 0xF8 + 0x110) != 0) goto loc_0036E9F8;
    goto loc_0036DA6D;
loc_0036DC1A:
    result = (result) >> (5);
    result = (uint32_t)((result) & (31));
    if (((uint8_t)(result)) == 31) goto loc_0036ED5C;
    result = 129;
    if (((uint32_t)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xAC2477) + *(uint16_t *)(*(uint64_t *)(local_rsp - 0xF8 - 0x40) + 0xAE) * 8))) == 11) { result = 129; }
    goto loc_0036DAEB;
loc_0036DC49:
    result = (result) & (-17);
    goto loc_0036DA23;
loc_0036DC52:
loc_0036DC59:
    result = MiLockVadTree(1, Arg2, Arg3, *(uint64_t *)(local_rsp - 0xF8 - 0x50));
    result = MiLocateAddress(*(uint64_t *)(local_rsp - 0xF8 - 0x50), Arg2, Arg3, *(uint64_t *)(local_rsp - 0xF8 - 0x50));
    *(uint64_t *)(local_rsp - 0xF8 - 0x40) = result;
    result = MiUnlockVadTree(1, 17, Arg3, *(uint64_t *)(local_rsp - 0xF8 - 0x50));
    if (result != 0) goto loc_0036DB9A;
loc_0036DC8E:
loc_0036DC96:
    if (condition_is_below) goto loc_0036EF26;
loc_0036DCA7:
    Arg2 = 0;
    result = (uint8_t)((*(uint8_t *)(local_rsp - 0xF8 - 0x78)) >> (2));
    if (((1) & ((uint8_t)(result))) != 0) goto loc_0036E5ED;
loc_0036DCB8:
    local_rsi = (uint32_t)((16) | (0));
    if ((*(uint32_t *)(local_rsp - 0xF8 - 0x68)) != 1) goto loc_0036E433;
loc_0036DCCA:
loc_0036DCCF:
    if (((1) & ((uint8_t)(local_rsi))) != 0) goto loc_0036E653;
loc_0036DCD8:
    local_rdi = -(*(uint64_t *)(local_rsp - 0xF8 + 0x110));
    Arg4 = (*(uint64_t *)(local_rsp - 0xF8 - 0x50)) & (local_rsp - 248 + 272);
    v_stack_m1D8 = *(uint64_t *)(local_rsp - 0xF8 - 0x10);
    result = MiAllocateInPageSupport(*(uint64_t *)(local_rsp - 0xF8 + 0x108), (uint32_t)(*(uint32_t *)(local_rsp - 0xF8 - 0x48)), local_rsp - 248 - 104, Arg4);
    *(uint64_t *)(local_rsp - 0xF8 - 0x10) = result;
    if (result == 0) goto loc_0036EF35;
    result = MI_READ_PTE_LOCK_FREE(*(uint64_t *)(local_rsp - 0xF8 + 0x108), (uint32_t)(*(uint32_t *)(local_rsp - 0xF8 - 0x48)), local_rsp - 248 - 104, Arg4);
    if (result != result) goto loc_0036EF3F;
    if (result < result) goto loc_0036EDFC;
loc_0036DD33:
    if (*(uint64_t *)(local_rsp - 0xF8 - 0x60) != 0) goto loc_0036E7C7;
loc_0036DD40:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0xF8 - 0x68)))) > 1) goto loc_0036E18E;
loc_0036DD50:
loc_0036DD54:
loc_0036DD58:
    result = MiObtainFaultCharges(v_stack_m180, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0xF8 - 0x80)))), (uint32_t)(*(uint32_t *)(local_rsp - 0xF8 - 0x58)), Arg4);
    *(uint64_t *)(local_rsp - 0xF8 - 0x38) = result;
    if (((uint32_t)(*(uint32_t *)(local_rsp - 0xF8 - 0x80))) > result) goto loc_0036EF6E;
    Arg4 = 0;
    *(uint64_t *)(local_rsp - 0xF8 - 0x18) = 0;
    *(uint64_t *)(local_rsp - 0xF8 - 0x28) = v_xmm0;
    if (*(uint64_t *)(local_rsp - 0xF8 - 0x60) != 0) goto loc_0036E70D;
loc_0036DD96:
loc_0036DD9E:
    if ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0xF8 - 0x80)))) != 0) goto loc_0036E4A4;
loc_0036DDAD:
    if (0 == 0) goto loc_0036E884;
loc_0036DDB6:
    if (((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0xF8 - 0x80))))) != ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0xF8 - 0x80)))))) goto loc_0036EE40;
loc_0036DDC2:
    local_r14 = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0xC0))) >> (11));
    local_r14 = (uint32_t)((local_r14) & (7));
    local_rdi = 0;
    result = 0;
    *(uint32_t *)(local_rsp - 0xF8 + 0x100) = 0;
loc_0036DDEF:
    *(uint32_t *)(local_rsp - 0xF8 - 0x80) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0xF8 - 0x80)));
    result = MI_READ_PTE_LOCK_FREE(*(uint64_t *)(local_rsp - 0xF8 - 0x70), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0xF8 - 0x80)))), (uint32_t)(*(uint32_t *)(local_rsp - 0xF8 - 0x58)), Arg4);
    if ((((uint8_t)(local_rsi)) & (16)) != 0) goto loc_0036E6A9;
    if (((result) & (0xC01ULL)) != 0) goto loc_0036E627;
    if (*(uint64_t *)(v_rip + 0xABFE67) == 0) goto loc_0036E69D;
    if ((((uint8_t)(result)) & (16)) != 0) goto loc_0036E683;
    Arg2 = ~(*(uint64_t *)(v_rip + 0xABFE67));
    Arg2 = (Arg2) & (result);
loc_0036DE3A:
    if ((((uint8_t)(*(uint64_t *)(local_rsp - 0xF8 - 0x78))) & (16)) != 0) goto loc_0036E68C;
    Arg1 = ~(*(uint64_t *)(v_rip + 0xABFE67));
    Arg1 = (Arg1) & (*(uint64_t *)(local_rsp - 0xF8 - 0x78));
loc_0036DE4A:
    Arg1 = (Arg1) ^ (Arg2);
    if (((Arg2) & (Arg1)) != 0) goto loc_0036E62D;
    Arg1 = (uint8_t)(((uint8_t)(result)) >> (2));
    if (((1) & ((uint8_t)(Arg1))) == 0) goto loc_0036E62D;
    result = (result) >> (12);
    Arg3 = (*(uint64_t *)(local_rsp - 0xF8 - 0x78)) >> (12);
    Arg3 = (uint8_t)((Arg3) ^ ((uint8_t)(result)));
    if ((((uint8_t)(Arg3)) & (15)) != 0) goto loc_0036E62D;
    result = (uint32_t)((result) & (15));
    Arg2 = 0;
    Arg2 = (((uint32_t)(result)) == ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m180 + 0x4B4))))) ? 1 : 0;
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rsi))) & (1));
    if (((uint32_t)(Arg2)) != ((uint32_t)(result))) goto loc_0036E62D;
loc_0036DEAB:
    if (*(uint64_t *)(local_rsp - 0xF8 - 0x28) != 0) {
        result = *(uint64_t *)(local_rsp - 0xF8 - 0x28);
        Arg1 = *(uint64_t *)(result);
        result = *(uint64_t *)(local_rsp - 0xF8 - 0x18);
        result = (result) - (1);
        *(void **)(local_rsp - 0xF8 - 0x28) = Arg1;
        *(uint64_t *)(local_rsp - 0xF8 - 0x18) = result;
        result = -(result);
    }
    Arg2 = (*(uint64_t *)(local_rsp - 0xF8 - 0x28)) - (result);
    Arg2 = (Arg2) >> (4);
    Arg2 = (Arg2) * (result);
    *(uint64_t *)(result + 0x140) = Arg2;
    if ((*(uint64_t *)(local_rsp - 0xF8 - 0x70)) == (*(uint64_t *)(local_rsp - 0xF8 + 0x108))) goto loc_0036E66B;
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0xC0))) >> (14));
    Arg2 = (uint32_t)((Arg2) & (7));
loc_0036DF24:
    result = MiLockSetPfnPriority(*(uint64_t *)(local_rsp - 0xF8 - 0x28), Arg2, *(uint64_t *)(local_rsp - 0xF8 - 0x28), Arg4);
loc_0036DF29:
    local_rbx = (result + 320) + (8);
    *(uint32_t *)(local_rsp - 0xF8 + 0x100) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0xF8 + 0x100)));
    result = *(uint64_t *)(local_rsp - 0xF8 - 0x60);
    if (*(uint64_t *)(local_rsp - 0xF8 - 0x60) != 0) {
        Arg1 = *(uint64_t *)(local_rsp - 0xF8 - 0x60);
        result = MiAdvanceFaultList(Arg1, Arg2, *(uint64_t *)(local_rsp - 0xF8 - 0x28), (uint32_t)(*(uint32_t *)(local_rsp - 0xF8 + 0x100)));
    }
    if (*(uint64_t *)(v_rip + 0xABFD21) == 0) goto loc_0036DF74;
    if ((((uint8_t)(*(uint64_t *)(local_rsp - 0xF8 - 0x78))) & (16)) == 0) {
        Arg2 = *(uint64_t *)(v_rip + 0xABFD21);
        Arg2 = ~(Arg2);
        Arg2 = (Arg2) & (*(uint64_t *)(local_rsp - 0xF8 - 0x78));
    }
    Arg2 = (Arg2) >> (32);
    Arg2 = (Arg2) + (1);
    if (*(uint64_t *)(local_rsp - 0xF8 - 0x78) == 0) goto loc_0036E6CE;
    if (*(uint64_t *)(v_rip + 0xABFD21) == 0) goto loc_0036DF9D;
    if ((((uint8_t)(*(uint64_t *)(local_rsp - 0xF8 - 0x78))) & (16)) != 0) goto loc_0036E694;
    Arg1 = ~(*(uint64_t *)(v_rip + 0xABFD21));
    result = (*(uint64_t *)(local_rsp - 0xF8 - 0x78)) & (Arg1);
loc_0036DF9D:
    Arg2 = (Arg2) << (32);
    Arg1 = ((uint32_t)((uint32_t)(result))) | (Arg2);
    result = MiSwizzleInvalidPte(Arg1, Arg2, *(uint64_t *)(local_rsp - 0xF8 - 0x78), (uint32_t)(*(uint32_t *)(local_rsp - 0xF8 + 0x100)));
    local_rdi = (uint32_t)((local_rdi) + (1));
    *(uint64_t *)(local_rsp - 0xF8 - 0x78) = result;
    if (((uint32_t)(local_rdi)) < ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0xF8 - 0x80))))) goto loc_0036DDEF;
loc_0036DFBF:
    result = -((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0xF8 - 0x80)))));
    local_rbx = (uint8_t)((v_stack_m188) >> (4));
    result = (*(uint64_t *)(local_rsp - 0xF8 + 0x108)) - (*(uint64_t *)(local_rsp - 0xF8 - 0x70) + result * 8);
    result = (result) >> (3);
    local_rbx = (uint8_t)((local_rbx) & (1));
    if (condition_is_not_equal) goto loc_0036E6C6;
    Arg4 = (*(uint64_t *)(local_rsp - 0xF8 - 0x70) + result * 8) << (25);
    result = (result) << (25);
    Arg4 = (Arg4) - (result);
    Arg4 = (Arg4) >> (16);
loc_0036E016:
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0xF8 - 0x80))))) << (12));
    *(uint32_t *)(result + 0x110 + 0x28) = (uint32_t)(Arg3);
    *(uint16_t *)(result + 0x110 + 0xA) = 66;
    result = ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg4))))) & ((uint32_t)(0xFFFULL));
    Arg4 = (Arg4) & (0xFFFFFFFFFFFFF000ULL);
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(Arg4))) & ((uint32_t)((uint32_t)(0xFFFULL))));
    *(uint64_t *)(result + 0x110 + 0x20) = Arg4;
    *(uint32_t *)(result + 0x110 + 0x2C) = (uint32_t)(Arg2);
    Arg1 = (Arg3 + 4095) + (result);
    Arg1 = (Arg1) >> (12);
    Arg1 = (uint16_t)((Arg1) + (6));
    Arg1 = (uint16_t)((Arg1) << (3));
    *(uint16_t *)(result + 0x110 + 0x8) = (uint16_t)(Arg1);
    if ((((uint8_t)(local_rsi)) & (2)) != 0) goto loc_0036EBF5;
    *(uint16_t *)(result + 0x110 + 0xA) = 0x4042ULL;
loc_0036E07C:
    result = MI_READ_PTE_LOCK_FREE(*(uint64_t *)(local_rsp - 0xF8 - 0x70) + result * 8, Arg2, Arg3, Arg4);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0xF8 - 0x80)))) == 1) goto loc_0036E412;
    result = (uint8_t)((v_stack_m188) & (223));
    v_stack_m188 = (uint8_t)(result);
    *(uint8_t *)(local_rsp - 0xF8 - 0x30) = (uint8_t)(result);
loc_0036E0A2:
    v_stack_m1D0 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0xF8 - 0x30)));
    v_stack_m1D8 = result;
    result = MiInitializeReadInProgressPfn(*(uint64_t *)(local_rsp - 0xF8 - 0x50), result + 320, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0xF8 - 0x80)))), *(uint64_t *)(local_rsp - 0xF8 - 0x70) + result * 8);
    if ((((uint8_t)(local_rsi)) & (16)) != 0) goto loc_0036EB9D;
loc_0036E0CA:
    if (((v_stack_m188) & (16)) != 0) {
        Arg1 = *(uint64_t *)(local_rsp - 0xF8 + 0x110);
        Arg2 = 0;
        result = MiObtainProtoReference(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0xF8 - 0x80)))), *(uint64_t *)(local_rsp - 0xF8 - 0x70) + result * 8);
    }
    result = MI_READ_PTE_LOCK_FREE(*(uint64_t *)(local_rsp - 0xF8 + 0x108), Arg2, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0xF8 - 0x80)))), *(uint64_t *)(local_rsp - 0xF8 - 0x70) + result * 8);
    *(uint64_t *)(result + 0xA8) = result;
    *(uint64_t *)(result + 0xE8) = *(uint64_t *)(local_rsp - 0xF8 + 0x108);
    *(uint64_t *)(local_rsp - 0xF8 - 0x78) = result;
    if (*(uint64_t *)(local_rsp - 0xF8 - 0x60) != 0) goto loc_0036E84C;
loc_0036E11A:
    result = PsGetIoPriorityThread(*(uint64_t *)(local_rsp - 0xF8 + 0x20), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + 0xC0)))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0xF8 - 0x80)))), (uint32_t)(*(uint32_t *)(result + 0xC0)));
    if (((uint32_t)(result)) < 2) {
    }
    if (*(uint64_t *)(local_rsp - 0xF8 - 0x40) != 0) goto loc_0036E6D5;
loc_0036E13A:
    *(uint32_t *)(result + 0xC0) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0xC0)));
    result = *(uint64_t *)(local_rsp - 0xF8 - 0x40);
    if (*(uint64_t *)(local_rsp - 0xF8 + 0x110) != 0) {
        Arg2 = 17;
        result = MiUnlockProtoPoolPage(*(uint64_t *)(local_rsp - 0xF8 + 0x110), Arg2, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0xF8 - 0x80)))), (uint32_t)(*(uint32_t *)(result + 0xC0)));
    }
loc_0036E15F:
    if (*(uint64_t *)(local_rsp - 0xF8 - 0x28) == 0) goto loc_0036E8C3;
    result = (*(uint64_t *)(local_rsp - 0xF8 - 0x18)) - (1);
    *(uint64_t *)(local_rsp - 0xF8 - 0x28) = *(uint64_t *)(*(uint64_t *)(local_rsp - 0xF8 - 0x28));
    *(uint64_t *)(local_rsp - 0xF8 - 0x18) = result;
    result = -(result);
    result = MiReleaseFreshPage(*(uint64_t *)(local_rsp - 0xF8 - 0x28), Arg2, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0xF8 - 0x80)))), (uint32_t)(*(uint32_t *)(result + 0xC0)));
    goto loc_0036E15F;
loc_0036E18E:
    result = MiSufficientAvailablePages(v_stack_m180, 320, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0xF8 - 0x80)))), (uint32_t)(*(uint32_t *)(result + 0xC0)));
    if ((uint32_t)(result) == 0) goto loc_0036DD50;
    local_r10 = (uint32_t)(((uint32_t)((uint32_t)(*(uint64_t *)(local_rsp - 0xF8 + 0x108)))) >> (3));
    local_r10 = (uint32_t)((local_r10) & (511));
    local_r12 = (uint32_t)((511) - ((uint32_t)(local_r10)));
    *(uint32_t *)(local_rsp - 0xF8 - 0x48) = (uint32_t)(local_r10);
    if (((v_stack_m188) & (16)) != 0) goto loc_0036EA0E;
loc_0036E1D4:
    if (*(uint64_t *)(local_rsp - 0xF8 - 0x60) != 0) goto loc_0036E7E4;
    if ((((uint8_t)(local_rsi)) & (4)) != 0) goto loc_0036E7E4;
loc_0036E1EB:
    if (((uint32_t)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0xF8 - 0x28)))) <= 1) goto loc_0036EF61;
    *(uint64_t *)(local_rsp - 0xF8 - 0x78) = result;
    *(uint32_t *)(local_rsp - 0xF8 - 0x80) = (uint32_t)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0xF8 - 0x28)) - 1);
    *(uint64_t *)(local_rsp - 0xF8 - 0x38) = *(uint64_t *)(local_rsp - 0xF8 + 0x108) + 8;
    if (((uint32_t)(local_r12)) > ((uint32_t)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0xF8 - 0x28)) - 1))) { local_r12 = (uint32_t)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0xF8 - 0x28)) - 1); }
    result = MiGetPagingFileOffset(result, *(uint64_t *)(local_rsp - 0xF8 + 0x108), 1, (uint32_t)(*(uint32_t *)(result + 0xC0)));
    local_r13 = (uint32_t)(((uint32_t)(0xFFFFFFFDULL)) - ((uint32_t)((uint32_t)((uint32_t)(result)))));
    result = ((uint32_t)((uint32_t)(local_r12))) + ((uint32_t)((uint32_t)(result)));
    *(uint64_t *)(local_rsp - 0xF8 - 0x68) = (uint32_t)((uint32_t)(result));
    if (result < ((uint32_t)(0xFFFFFFFEULL))) { local_r13 = (uint32_t)(local_r12); }
    if (((1) & ((uint8_t)(local_rsi))) == 0) goto loc_0036E673;
loc_0036E241:
    local_rsi = (uint32_t)((local_rsi) | (8));
loc_0036E244:
    result = MI_CLEAR_PTE_BITS_FOR_READ_CLUSTER(local_rsp - 248 - 120, (uint32_t)((uint32_t)(result)), 1, (uint32_t)(*(uint32_t *)(result + 0xC0)));
    if ((uint32_t)(local_r13) == 0) goto loc_0036E2BD;
loc_0036E263:
    local_r15 = (*(uint64_t *)(local_rsp - 0xF8 - 0x68)) + (1);
    result = MiUpdatePageFileHighInPte(*(uint64_t *)(local_rsp - 0xF8 - 0x78), local_r15, 1, (uint32_t)(*(uint32_t *)(result + 0xC0)));
    result = MI_READ_PTE_LOCK_FREE(*(uint64_t *)(local_rsp - 0xF8 - 0x38), local_r15, 1, (uint32_t)(*(uint32_t *)(result + 0xC0)));
    *(uint64_t *)(local_rsp - 0xF8 - 0x8) = result;
    if (((result) & (992)) == 0) goto loc_0036E618;
    result = MI_CLEAR_PTE_BITS_FOR_READ_CLUSTER(local_rsp - 248 - 8, local_r15, 1, (uint32_t)(*(uint32_t *)(result + 0xC0)));
    if ((*(uint64_t *)(local_rsp - 0xF8 - 0x8)) != result) goto loc_0036E618;
    *(uint64_t *)(local_rsp - 0xF8 - 0x70) = *(uint64_t *)(local_rsp - 0xF8 - 0x38);
loc_0036E2A3:
    local_r12 = (*(uint64_t *)(local_rsp - 0xF8 - 0x38)) + (8);
    local_r13 = (uint32_t)((local_r13) + (-1));
    if (condition_is_not_equal) goto loc_0036E263;
loc_0036E2AD:
loc_0036E2BD:
    local_rdi = (*(uint64_t *)(local_rsp - 0xF8 - 0x70)) - (*(uint64_t *)(local_rsp - 0xF8 + 0x108));
    *(uint64_t *)(local_rsp - 0xF8 - 0x78) = *(uint64_t *)(local_rsp - 0xF8);
    local_rdi = (local_rdi) >> (3);
    local_r11 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0xF8 - 0x80))) - ((uint32_t)(local_rdi)));
    *(uint64_t *)(local_rsp - 0xF8 - 0x70) = local_rdi;
    *(uint32_t *)(local_rsp - 0xF8 - 0x68) = (uint32_t)(local_r11);
    *(uint64_t *)(local_rsp - 0xF8 - 0x38) = *(uint64_t *)(local_rsp - 0xF8 + 0x108);
    local_r10 = (uint32_t)(*(uint32_t *)(local_rsp - 0xF8 - 0x48));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0xF8 - 0x48)))) > ((uint32_t)(local_r11))) { local_r10 = (uint32_t)(local_r11); }
    result = MiGetPagingFileOffset(*(uint64_t *)(local_rsp - 0xF8), local_r15, 1, (uint32_t)(*(uint32_t *)(result + 0xC0)));
    *(uint64_t *)(local_rsp - 0xF8 - 0x48) = (uint32_t)((uint32_t)(result));
    local_r13 = (uint32_t)(((uint32_t)((uint32_t)(result))) - 1);
    if (((uint32_t)((uint32_t)(local_r10))) <= ((uint32_t)((uint32_t)(result)) - 1)) { local_r13 = (uint32_t)(local_r10); }
    result = MI_CLEAR_PTE_BITS_FOR_READ_CLUSTER(local_rsp - 248 - 120, local_r15, 1, (uint32_t)(*(uint32_t *)(result + 0xC0)));
    if ((uint32_t)(local_r13) == 0) goto loc_0036E384;
loc_0036E32A:
    local_r15 = (*(uint64_t *)(local_rsp - 0xF8 - 0x48)) - (1);
    local_r12 = (*(uint64_t *)(local_rsp - 0xF8 + 0x108)) - (8);
    result = MiUpdatePageFileHighInPte(*(uint64_t *)(local_rsp - 0xF8 - 0x78), local_r15, 1, (uint32_t)(*(uint32_t *)(result + 0xC0)));
    result = MI_READ_PTE_LOCK_FREE(local_r12, local_r15, 1, (uint32_t)(*(uint32_t *)(result + 0xC0)));
    *(uint64_t *)(local_rsp - 0xF8 - 0x8) = result;
    if (((result) & (992)) == 0) goto loc_0036E362;
    result = MI_CLEAR_PTE_BITS_FOR_READ_CLUSTER(local_rsp - 248 - 8, local_r15, 1, (uint32_t)(*(uint32_t *)(result + 0xC0)));
    if ((*(uint64_t *)(local_rsp - 0xF8 - 0x8)) == result) goto loc_0036E36A;
loc_0036E362:
    if ((((uint8_t)(local_rsi)) & (8)) == 0) goto loc_0036E36E;
    goto loc_0036E374;
loc_0036E36A:
    *(uint64_t *)(local_rsp - 0xF8 - 0x38) = local_r12;
loc_0036E36E:
    local_r13 = (uint32_t)((local_r13) + (-1));
    if (condition_is_not_equal) goto loc_0036E32A;
loc_0036E374:
loc_0036E384:
    Arg2 = (*(uint64_t *)(local_rsp - 0xF8 + 0x108)) - (*(uint64_t *)(local_rsp - 0xF8 - 0x38));
    Arg2 = (Arg2) >> (3);
    if (*(uint64_t *)(v_rip + 0xABF8EB) == 0) goto loc_0036E3B6;
    if ((((uint8_t)(*(uint64_t *)(local_rsp - 0xF8))) & (16)) != 0) goto loc_0036E6B4;
    result = ~(*(uint64_t *)(v_rip + 0xABF8EB));
    result = (result) & (*(uint64_t *)(local_rsp - 0xF8));
loc_0036E3B6:
    result = (result) >> (32);
    result = (result) - ((uint32_t)((uint32_t)(Arg2)));
    if (*(uint64_t *)(local_rsp - 0xF8) == 0) goto loc_0036E839;
    if (*(uint64_t *)(v_rip + 0xABF8EB) == 0) goto loc_0036E3DD;
    if ((((uint8_t)(*(uint64_t *)(local_rsp - 0xF8))) & (16)) != 0) goto loc_0036E6BD;
    Arg1 = ~(*(uint64_t *)(v_rip + 0xABF8EB));
    local_rbx = (*(uint64_t *)(local_rsp - 0xF8)) & (Arg1);
loc_0036E3DD:
    result = (result) << (32);
    Arg1 = ((uint32_t)((uint32_t)(local_rbx))) | (result);
    result = MiSwizzleInvalidPte(Arg1, Arg2, (uint32_t)((uint32_t)(Arg2)), *(uint64_t *)(local_rsp - 0xF8 + 0x108));
    *(uint64_t *)(local_rsp - 0xF8 - 0x78) = result;
    result = (uint32_t)((*(uint64_t *)(local_rsp - 0xF8 - 0x70) + 1) + ((uint32_t)(Arg2)));
    *(uint32_t *)(local_rsp - 0xF8 - 0x80) = (uint32_t)(result);
    local_rdi = (*(uint64_t *)(local_rsp - 0xF8 + 0x108)) - ((uint32_t)((uint32_t)(Arg2)) * 8);
    *(uint64_t *)(local_rsp - 0xF8 - 0x70) = local_rdi;
    goto loc_0036DD54;
loc_0036E412:
    result = (uint8_t)(((uint32_t)((uint32_t)(Arg2)) * 8) & (248));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0xF8 - 0x10) + 0xC0))) >> (11));
    Arg1 = (uint8_t)((Arg1) & (7));
    Arg1 = (uint8_t)((Arg1) | ((uint8_t)(result)));
    Arg1 = (uint8_t)((Arg1) | (8));
    v_stack_m188 = (uint8_t)(Arg1);
    *(uint8_t *)(local_rsp - 0xF8 - 0x30) = (uint8_t)(Arg1);
    goto loc_0036E0A2;
loc_0036E433:
    if ((uint32_t)(result) != 0) goto loc_0036E9E7;
    if (*(uint64_t *)(local_rsp - 0xF8 - 0x60) != 0) goto loc_0036E7FA;
    if ((*(uint64_t *)(local_rsp - 0xF8 - 0x50)) <= result) goto loc_0036DCCA;
    *(uint32_t *)(local_rsp - 0xF8 - 0x68) = (uint32_t)(local_r10);
    if ((((uint8_t)((uint32_t)((uint32_t)(Arg2)))) & (16)) != 0) goto loc_0036DCCA;
    if ((*(uint64_t *)(local_rsp - 0xF8 - 0x50)) < result) goto loc_0036E495;
    if ((*(uint64_t *)(local_rsp - 0xF8 - 0x50)) <= result) goto loc_0036DCCA;
loc_0036E495:
    local_rsi = (uint32_t)((local_rsi) | (4));
    *(uint32_t *)(local_rsp - 0xF8 - 0x68) = 16;
    goto loc_0036DCCA;
loc_0036E4A4:
    if (sign_flag) goto loc_0036EF9C;
loc_0036E4AD:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0xF8 + 0x8) + 0xB8)))) & (15)) != 0) goto loc_0036E4D8;
    if (*(uint64_t *)(local_rsp - 0xF8 + 0x110) != 0) goto loc_0036E4D8;
    result = MiGetCurrentSlabIdentity(*(uint64_t *)(local_rsp - 0xF8 + 0x20), Arg2, *(uint64_t *)(local_rsp - 0xF8 + 0x110), *(uint64_t *)(local_rsp - 0xF8 + 0x108));
    if (((uint8_t)(result)) != 255) goto loc_0036EC13;
loc_0036E4D8:
    if ((((uint8_t)(local_rsi)) & (64)) != 0) goto loc_0036EFC9;
loc_0036E4E2:
    local_rbx = 9;
    if (((v_stack_m188) & (32)) != 0) { local_rbx = (uint32_t)(*(uint64_t *)(local_rsp - 0xF8 - 0x38)); }
loc_0036E4F0:
    if ((*(uint64_t *)(local_rsp - 0xF8 - 0x18)) != (*(uint64_t *)(local_rsp - 0xF8 + 0x108))) goto loc_0036DDB6;
    *(uint64_t *)(local_rsp - 0xF8) = local_rdi;
    result = MiProtectionToCacheAttribute((uint32_t)(*(uint32_t *)(local_rsp - 0xF8 + 0x30)), Arg2, *(uint64_t *)(local_rsp - 0xF8 + 0x110), *(uint64_t *)(local_rsp - 0xF8 + 0x108));
    *(uint32_t *)(local_rsp - 0xF8 - 0x54) = (uint32_t)(result);
    local_r13 = (*(uint64_t *)(local_rsp - 0xF8 - 0x70)) << (25);
    Arg1 = (result) << (25);
    local_r13 = (local_r13) - (Arg1);
    local_r13 = (local_r13) >> (16);
loc_0036E52D:
    Arg2 = 0;
    result = memset(local_rsp - 248 + 64, Arg2, Arg2 + 112, *(uint64_t *)(local_rsp - 0xF8 + 0x108));
    v_stack_m198 = local_rsp - 248 + 64;
    v_stack_m1A0 = local_rdi;
    Arg3 = (uint32_t)((*(uint8_t *)(*(uint64_t *)(local_rsp - 0xF8 + 0x100) + 0x45)) & (1));
    v_stack_m1A8 = local_rsp - 248 + 24;
    v_stack_m1B0 = (uint32_t)(local_rbx);
    v_stack_m1B8 = *(uint64_t *)(*(uint64_t *)(local_rsp - 0xF8 + 0x100) + 0x60);
    v_stack_m1C8 = (uint32_t)(*(uint64_t *)(local_rsp - 0xF8 - 0x70) + result * 8);
    v_stack_m1D0 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0xF8 - 0x54)));
    v_stack_m1D8 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0xF8 - 0x54)));
    result = MiInitializePageChainPacket(v_stack_m180, *(uint64_t *)(local_rsp - 0xF8 + 0x8), Arg3, local_r13);
    result = MiGetPageChain(local_rsp - 248 + 64, *(uint64_t *)(local_rsp - 0xF8 + 0x8), Arg3, local_r13);
    if (*(uint64_t *)(local_rsp - 0xF8 + 0xA8) == 0) goto loc_0036EDC0;
    if ((*(uint64_t *)(local_rsp - 0xF8 - 0x28)) != 0) goto loc_0036EC91;
    *(uint64_t *)(local_rsp - 0xF8 - 0x28) = v_xmm0;
    *(uint64_t *)(local_rsp - 0xF8 - 0x18) = v_xmm1;
loc_0036E5D4:
    if ((*(uint64_t *)(local_rsp - 0xF8 - 0x18)) == 0) goto loc_0036E87B;
    goto loc_0036DDB6;
loc_0036E5ED:
    result = (*(uint64_t *)(local_rsp - 0xF8 - 0x78)) >> (12);
    result = (uint32_t)((result) & (15));
    Arg2 = (((uint32_t)(result)) == ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m180 + 0x4B4))))) ? 1 : 0;
    goto loc_0036DCB8;
loc_0036E618:
    if ((((uint8_t)(local_rsi)) & (8)) == 0) goto loc_0036E2A3;
    goto loc_0036E2AD;
loc_0036E627:
loc_0036E62D:
    if ((((uint8_t)(local_rsi)) & (8)) == 0) goto loc_0036E6FB;
    if ((*(uint64_t *)(local_rsp - 0xF8 - 0x70)) <= (*(uint64_t *)(local_rsp - 0xF8 + 0x108))) goto loc_0036ECB3;
    *(uint32_t *)(local_rsp - 0xF8 - 0x80) = (uint32_t)(*(uint64_t *)(local_rsp - 0xF8 + 0x110));
    goto loc_0036DFBF;
loc_0036E653:
    result = (uint32_t)(*(uint32_t *)(local_rsp - 0xF8 - 0x68));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0xF8 - 0x68)))) > ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0xF8 - 0x60) + 0x4B8))))) { result = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0xF8 - 0x60) + 0x4B8))); }
    *(uint32_t *)(local_rsp - 0xF8 - 0x68) = (uint32_t)(result);
    goto loc_0036DCD8;
loc_0036E66B:
    goto loc_0036DF24;
loc_0036E673:
    if ((*(uint64_t *)(local_rsp - 0xF8 - 0x60)) == 0) goto loc_0036E244;
    goto loc_0036E241;
loc_0036E683:
    Arg2 = ((uint32_t)((uint32_t)(*(uint64_t *)(local_rsp - 0xF8 - 0x70) + result * 8))) & (-17);
    goto loc_0036DE3A;
loc_0036E68C:
    goto loc_0036DE4A;
loc_0036E694:
    result = (result) & (-17);
    goto loc_0036DF9D;
loc_0036E69D:
    goto loc_0036DE4A;
loc_0036E6A9:
    goto loc_0036DEAB;
loc_0036E6B4:
    result = (result) & (-17);
    goto loc_0036E3B6;
loc_0036E6BD:
    local_rbx = (local_rbx) & (-17);
    goto loc_0036E3DD;
loc_0036E6C6:
    Arg4 = 0;
    goto loc_0036E016;
loc_0036E6CE:
    result = 0;
    goto loc_0036DF9D;
loc_0036E6D5:
    result = ((uint32_t)(*(uint32_t *)(result + 0x30))) >> (19);
    result = (uint32_t)((result) & (3));
    if ((*(uint64_t *)(v_rip - 0x35A167 + result * 8)) != 16) goto loc_0036E13A;
    goto loc_0036E13A;
loc_0036E6FB:
    local_rsi = (uint32_t)((local_rsi) | (2));
    *(uint64_t *)(local_rbx) = *(uint64_t *)(v_rip + 0xAC8D36);
    goto loc_0036DF29;
loc_0036E70D:
    if ((*(uint8_t *)(*(uint64_t *)(local_rsp - 0xF8 - 0x40))) != 1) goto loc_0036DD96;
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0xF8 - 0x40) + 0x50))) >> (3));
    Arg2 = (uint32_t)((Arg2) & (7));
    Arg2 = (uint32_t)((Arg2) + (1));
    result = MiGetAvailablePagesBelowPriority(v_stack_m180, Arg2, *(uint64_t *)(local_rsp - 0xF8 - 0x78), Arg4);
    if (result <= ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint64_t *)(local_rsp - 0xF8 + 0x110))))))) goto loc_0036DD9E;
    goto loc_0036DD9E;
loc_0036E74B:
    v_stack_m188 = 16;
    Arg1 = ((uint32_t)(*(uint32_t *)(local_rsp - 0xF8 - 0x54))) >> (9);
    Arg1 = (Arg1) & ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint64_t *)(local_rsp - 0xF8 + 0x110))))));
    Arg1 = (Arg1) + (*(uint64_t *)(local_rsp - 0xF8 - 0x78));
    result = MI_READ_PTE_LOCK_FREE(Arg1, Arg2, *(uint64_t *)(local_rsp - 0xF8 - 0x78), Arg4);
    result = MI_PROTO_FORMAT_COMBINED(result, Arg2, *(uint64_t *)(local_rsp - 0xF8 - 0x78), Arg4);
    if ((uint8_t)(result) != 0) goto loc_0036E83E;
    if ((*(uint64_t *)(*(uint64_t *)(local_rsp - 0xF8 - 0x60) + 0x280)) == 0) goto loc_0036DB5F;
    goto loc_0036E843;
loc_0036E793:
    if (((*(uint32_t *)(v_stack_m180 + 0x50)) & (512)) == 0) goto loc_0036DAF9;
    result = MiIsPteInStore(result, local_rbx, *(uint64_t *)(local_rsp - 0xF8 - 0x78), Arg4);
    if ((uint32_t)(result) == 0) goto loc_0036DAF9;
    if ((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint64_t *)(local_rsp - 0xF8 + 0x110))))))) != 0) {
        Arg2 = 17;
        Arg1 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint64_t *)(local_rsp - 0xF8 + 0x110)))))));
        result = MiUnlockProtoPoolPage(Arg1, Arg2, *(uint64_t *)(local_rsp - 0xF8 - 0x78), Arg4);
    }
    result = 0;
    goto loc_0036E9AA;
loc_0036E7C7:
    if ((*(uint8_t *)(result)) != 1) goto loc_0036DD40;
    result = MiSetInPagePrefetchPriority(0, *(uint64_t *)(local_rsp - 0xF8 - 0x60), *(uint64_t *)(local_rsp - 0xF8 - 0x78), Arg4);
    goto loc_0036DD40;
loc_0036E7E4:
    local_r10 = 0;
    *(uint32_t *)(local_rsp - 0xF8 - 0x48) = 0;
    local_rdi = (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint64_t *)(local_rsp - 0xF8 + 0x110)))))));
    if ((uint32_t)(*(uint64_t *)(local_rsp - 0xF8 - 0x60)) == 0) { local_rdi = (uint32_t)(*(uint64_t *)(local_rsp - 0xF8 - 0x78)); }
    *(uint32_t *)(local_rsp - 0xF8 - 0x68) = (uint32_t)(local_rdi);
    goto loc_0036E1EB;
loc_0036E7FA:
    if (v_stack_m180 == 0) goto loc_0036EC4F;
loc_0036E803:
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(local_rsi))) & (0));
    Arg4 = (uint32_t)(((uint32_t)((uint32_t)(Arg2))) | (2));
    if (((v_stack_m188) & (16)) == 0) { Arg4 = (uint32_t)(Arg2); }
    result = MiComputeFaultCluster(v_stack_m180, *(uint64_t *)(local_rsp - 0xF8 - 0x60), v_stack_m180, Arg4);
    *(uint32_t *)(local_rsp - 0xF8 - 0x68) = (uint32_t)(result);
    goto loc_0036DCCF;
loc_0036E839:
    goto loc_0036E3DD;
loc_0036E83E:
    v_stack_m188 = 48;
loc_0036E843:
    *(uint32_t *)(local_rsp - 0xF8 - 0x68) = (uint32_t)(v_stack_m180);
    goto loc_0036DB5F;
loc_0036E84C:
    if ((*(uint8_t *)((uint32_t)(*(uint32_t *)(local_rsp - 0xF8 - 0x54)))) != 1) goto loc_0036E11A;
    Arg4 = (uint32_t)((Arg4) | (32));
    if (((*(uint32_t *)((uint32_t)(*(uint32_t *)(local_rsp - 0xF8 - 0x54)) + 0x50)) & (0x2000ULL)) == 0) goto loc_0036E11A;
    Arg4 = (uint32_t)(((uint32_t)((uint32_t)(*(uint64_t *)(local_rsp - 0xF8 - 0x60)))) | (160));
    goto loc_0036E11A;
loc_0036E87B:
    if (sign_flag) goto loc_0036F044;
loc_0036E884:
    if (*(uint64_t *)(local_rsp - 0xF8 + 0x110) != 0) goto loc_0036F071;
loc_0036E894:
    result = MiFreeInPageSupportBlock(v_stack_m180, *(uint64_t *)(local_rsp - 0xF8 - 0x60), v_stack_m180, Arg4);
    if (*(uint64_t *)(local_rsp - 0xF8 - 0x60) != 0) goto loc_0036F07D;
loc_0036E8A9:
    result = MiReturnFaultCharges(v_stack_m180, *(uint64_t *)(local_rsp - 0xF8 - 0x38), (uint32_t)(*(uint32_t *)(local_rsp - 0xF8 - 0x58)), Arg4);
    goto loc_0036E9AA;
loc_0036E8C3:
    result = (uint32_t)(*(uint32_t *)(local_rsp - 0xF8 + 0x100));
    if (((uint32_t)(*(uint32_t *)(local_rsp - 0xF8 + 0x100))) != (*(uint64_t *)(local_rsp - 0xF8 - 0x38))) {
        Arg3 = *(uint32_t *)(local_rsp - 0xF8 - 0x58);
        Arg2 = (*(uint64_t *)(local_rsp - 0xF8 - 0x38)) - ((uint32_t)(*(uint32_t *)(local_rsp - 0xF8 + 0x100)));
        Arg1 = v_stack_m180;
        result = MiReturnFaultCharges(Arg1, Arg2, Arg3, Arg4);
    }
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0xF8 + 0x118)) = *(uint64_t *)(local_rsp - 0xF8 - 0x60);
    result = MiGetPagingFileOffset(local_rbx, Arg2, Arg3, Arg4);
    local_rbx = (local_rbx) >> (12);
    local_rbx = (uint32_t)((local_rbx) & (15));
    *(uint32_t *)(local_rsp - 0xF8 + 0x28) = (uint32_t)((uint32_t)((uint32_t)(result)));
    if (((v_stack_m188) & (16)) != 0) {
        Arg1 = *(uint64_t *)(local_rsp - 0xF8 + 0x110);
        *(void **)(*(uint64_t *)(local_rsp - 0xF8 - 0x60) + 0xA0) = Arg1;
    }
    if (((1) & ((uint8_t)(local_rsi))) == 0) goto loc_0036E9BF;
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0xF8 - 0x60) + 0x60) = (uint32_t)((uint32_t)(result));
loc_0036E948:
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0xF8 - 0x60) + 0xC8) = *(uint64_t *)(v_stack_m180 + local_rbx * 8 + 0x4860);
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m180 + local_rbx * 8 + 0x4860) + 0xB8)) != 0) goto loc_0036E9D5;
loc_0036E95E:
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0xF8 - 0x60) + 0xC0) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0xF8 - 0x60) + 0xC0)));
    Arg2 = (v_stack_m180 * 2) + (v_stack_m180);
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0xF8 - 0x60) + 0xF0) = *(uint64_t *)(local_rsp - 0xF8 - 0x70) + result * 8;
    Arg2 = (Arg2) << (4);
    Arg2 = (Arg2) + ((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0xF8 - 0x60) + 0xC0)));
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0xF8 - 0x60) + 0xF8) = Arg2;
    if (condition_is_below) goto loc_0036F0E3;
loc_0036E9A5:
loc_0036E9AA:
    local_rsp = (local_rsp) + (440);
    return (uint32_t)(0xC0033333ULL);
loc_0036E9BF:
    Arg1 = (*(uint64_t *)(local_rsp - 0xF8 + 0x28)) << (12);
    *(void **)(*(uint64_t *)(local_rsp - 0xF8 - 0x60) + 0x60) = Arg1;
    goto loc_0036E948;
loc_0036E9D5:
    if (*(uint64_t *)(local_rsp - 0xF8 - 0x60) != 0) goto loc_0036ED31;
loc_0036E9DE:
    goto loc_0036E95E;
loc_0036E9E7:
    result = (uint32_t)(((uint32_t)(0xC0033333ULL)) - 1);
    *(uint32_t *)(local_rsp - 0xF8 - 0x68) = 1;
    *(uint32_t *)(v_rip + 0xAC89A5) = (uint32_t)(result);
    goto loc_0036DCCA;
loc_0036E9F8:
    result = MiSharedVaToPartition(v_stack_m180, *(uint64_t *)(local_rsp - 0xF8 - 0x60), *(uint64_t *)(local_rsp - 0xF8 - 0x70) + result * 8, 1);
    goto loc_0036DA68;
loc_0036EA0E:
    if (v_stack_m180 != 0) goto loc_0036ED96;
    result = MiLockVadTree(v_stack_m180 + 1, *(uint64_t *)(local_rsp - 0xF8 - 0x60), *(uint64_t *)(local_rsp - 0xF8 - 0x70) + result * 8, 1);
    result = MiLocateAddress(*(uint64_t *)(local_rsp - 0xF8 - 0x50), *(uint64_t *)(local_rsp - 0xF8 - 0x60), *(uint64_t *)(local_rsp - 0xF8 - 0x70) + result * 8, 1);
    *(uint64_t *)(local_rsp - 0xF8 - 0x40) = result;
    result = MiUnlockVadTree(1, 17, *(uint64_t *)(local_rsp - 0xF8 - 0x70) + result * 8, 1);
    if (result == 0) goto loc_0036EC1D;
loc_0036EA48:
    if (((*(uint32_t *)(result + 0x30)) & (0x200000ULL)) != 0) goto loc_0036EC1D;
    Arg2 = (*(uint64_t *)(local_rsp - 0xF8 - 0x50)) >> (12);
    result = MiGetProtoPteAddress(result, Arg2, 12, local_rsp - 248 + 16);
    if (*(uint64_t *)(local_rsp - 0xF8 + 0x10) == 0) goto loc_0036EC1D;
    if (condition_is_below) goto loc_0036EC1D;
    result = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0xF8 + 0x10) + 0x2C))) << (3);
    result = (result) - (*(uint64_t *)(local_rsp - 0xF8 + 0x108));
    result = (result) + (*(uint64_t *)(*(uint64_t *)(local_rsp - 0xF8 + 0x10) + 0x8));
    result = (result) >> (3);
    result = (uint32_t)((result) - 1);
    local_r12 = *(uint64_t *)(local_rsp - 0xF8 - 0x60);
    if (((uint32_t)(result)) < ((uint32_t)(*(uint64_t *)(local_rsp - 0xF8 - 0x60)))) { local_r12 = (uint32_t)(result); }
    result = (*(uint64_t *)(local_rsp - 0xF8 + 0x108)) - (*(uint64_t *)(*(uint64_t *)(local_rsp - 0xF8 + 0x10) + 0x8));
    result = (result) >> (3);
    if (((uint32_t)(result)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0xF8 - 0x48))))) goto loc_0036E1D4;
    *(uint32_t *)(local_rsp - 0xF8 - 0x48) = (uint32_t)(result);
    goto loc_0036E1D4;
loc_0036EADD:
    result = MiIsStoreProcess(local_r12, *(uint64_t *)(local_rsp - 0xF8 + 0x108), 1, local_rsp - 248 + 16);
    if ((uint32_t)(result) != 0) goto loc_0036DC59;
loc_0036EAED:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0xF8 + 0x8) + 0xB8)))) & (15)) != 0) goto loc_0036EB32;
    if ((*(uint64_t *)(local_rsp - 0xF8 - 0x50)) >= ((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0xF8 + 0x8) + 0xB8)))) goto loc_0036EB32;
    if ((*(uint64_t *)(*(uint64_t *)(local_r12 + 0x410) + 0x490)) != 0) goto loc_0036DC52;
    if ((*(uint64_t *)(*(uint64_t *)(local_r12 + 0x410) + 0x498)) != 0) goto loc_0036DC52;
loc_0036EB32:
    goto loc_0036DC8E;
loc_0036EB42:
    Arg4 = (*(uint64_t *)(local_rsp - 0xF8 - 0x60)) & (-2);
    if (((uint8_t)(*(uint8_t *)(Arg4))) == 5) goto loc_0036ED9F;
    if (((uint8_t)(*(uint8_t *)(Arg4))) == ((uint8_t)(local_r12))) goto loc_0036EC3A;
    if (((uint8_t)(*(uint8_t *)(Arg4))) != ((uint8_t)(*(uint64_t *)(local_rsp - 0xF8 - 0x70) + result * 8))) goto loc_0036DA92;
    *(uint64_t *)(local_rsp - 0xF8 - 0x60) = Arg4;
    if (((*(uint64_t *)(local_rsp - 0xF8 + 0x108)) & (local_rbx)) != 0) goto loc_0036E7C0;
    result = MiGetPagingFileOffset(local_rbx, *(uint64_t *)(local_rsp - 0xF8 + 0x108), 1, Arg4);
    if ((uint32_t)(result) == 0) goto loc_0036E7C0;
    local_r12 = 0;
    *(uint32_t *)(local_rsp - 0xF8 - 0x48) = 0;
    local_rsi = (uint32_t)((local_rsi) | (32));
    *(uint64_t *)(local_rsp - 0xF8 - 0x10) = *(uint64_t *)(Arg4 + 0x70);
    goto loc_0036DA92;
loc_0036EB9D:
    if (*(uint64_t *)(v_rip + 0xABF0DC) == 0) goto loc_0036EBB8;
    if ((((uint8_t)(local_rbx)) & (16)) != 0) goto loc_0036EC46;
    result = ~(*(uint64_t *)(v_rip + 0xABF0DC));
    local_rbx = (local_rbx) & (result);
loc_0036EBB8:
    local_rbx = (local_rbx) >> (12);
    local_rbx = (local_rbx) & (result);
    local_rbx = (local_rbx + local_rbx * 2) << (4);
    local_rbx = (local_rbx) + (result);
    result = MiFlowThroughInsertNode(0, local_rbx, 1, Arg4);
    goto loc_0036E0CA;
loc_0036EBF5:
    result = MiReduceMdl(*(uint64_t *)(local_rsp - 0xF8 - 0x60), local_rbx, 1, Arg4);
    if (result != 0) goto loc_0036F0CA;
loc_0036EC06:
    local_r15 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0xF8 - 0x60) + 0x28))) >> (12));
    goto loc_0036E07C;
loc_0036EC13:
    goto loc_0036E4F0;
loc_0036EC1D:
    *(uint32_t *)(local_rsp - 0xF8 - 0x68) = 1;
    goto loc_0036E1D4;
loc_0036EC3A:
    *(uint64_t *)(local_rsp - 0xF8 - 0x60) = Arg4;
    goto loc_0036DA92;
loc_0036EC46:
    local_rbx = (8) & (-17);
    goto loc_0036EBB8;
loc_0036EC4F:
    if (Arg4 > result) goto loc_0036E803;
    result = MiLockVadTree((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0xF8 - 0x48)))), *(uint64_t *)(local_rsp - 0xF8 + 0x108), 1, Arg4);
    result = MiLocateAddress(*(uint64_t *)(local_rsp - 0xF8 - 0x50), *(uint64_t *)(local_rsp - 0xF8 + 0x108), 1, Arg4);
    *(uint64_t *)(local_rsp - 0xF8 - 0x40) = result;
    result = MiUnlockVadTree(1, 17, 1, Arg4);
    goto loc_0036E803;
loc_0036EC91:
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0xF8 - 0x20)) = *(uint64_t *)(local_rsp - 0xF8 + 0x98);
    *(uint64_t *)(local_rsp - 0xF8 - 0x20) = *(uint64_t *)(local_rsp - 0xF8 + 0xA0);
    goto loc_0036E5D4;
loc_0036ECB3:
    if (1 == 0) goto loc_0036ED10;
loc_0036ECCB:
    result = *(uint64_t *)(result);
    local_r15 = (uint32_t)(*(uint32_t *)(local_rsp - 0xF8 + 0x100));
    if ((*(uint64_t *)(result)) != (*(uint64_t *)(v_rip + 0xAC8763))) {
        Arg1 = *(uint64_t *)(result) + *(uint64_t *)(result) * 2;
        Arg1 = (Arg1) << (4);
        result = 0;
        Arg1 = (Arg1) + (result);
        result = MiReleaseFreshPageAtDpc(Arg1, 17, 1, Arg4);
        local_r15 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0xF8 + 0x100))) - 1);
    }
    local_rbx = (result) + (8);
    local_rdi = (uint32_t)((1) + (-1));
    if (condition_is_not_equal) goto loc_0036ECCB;
    *(uint32_t *)(local_rsp - 0xF8 + 0x100) = (uint32_t)(local_r15);
loc_0036ED10:
    local_rsi = (uint32_t)((local_rsi) & (0xFFFFFFFDULL));
    *(uint64_t *)(local_rsp - 0xF8 - 0x70) = *(uint64_t *)(local_rsp - 0xF8 + 0x108);
    result = MI_READ_PTE_LOCK_FREE(*(uint64_t *)(local_rsp - 0xF8 + 0x108), 17, 1, Arg4);
    *(uint64_t *)(local_rsp - 0xF8 - 0x78) = result;
    goto loc_0036DDEF;
loc_0036ED31:
    if ((*(uint8_t *)(*(uint64_t *)(local_rsp - 0xF8 - 0x10) + 0x110)) != ((uint8_t)(Arg4))) goto loc_0036E9DE;
    if (((*(uint32_t *)(*(uint64_t *)(local_rsp - 0xF8 - 0x10) + 0x110 + 0x50)) & (0x1000ULL)) == 0) goto loc_0036E9DE;
    if ((((uint8_t)(Arg4)) & ((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC564B2))))) == 0) goto loc_0036E95E;
    goto loc_0036E9DE;
loc_0036ED5C:
    result = MiKernelStackVaToStackNode(*(uint64_t *)(local_rsp - 0xF8 - 0x50), *(uint64_t *)(local_rsp - 0xF8 - 0x70) + result * 8, 1, Arg4);
    if (result != 0) goto loc_0036EEE0;
    v_stack_p78 = v_rip + 11313023;
loc_0036ED89:
    local_r12 = (uint32_t)((*(uint64_t *)(local_rsp - 0xF8 - 0x10)) | (8));
    *(uint32_t *)(local_rsp - 0xF8 - 0x48) = (uint32_t)(local_r12);
    goto loc_0036DAEF;
loc_0036ED96:
    goto loc_0036EA48;
loc_0036ED9F:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x38)))) & (4)) != 0) goto loc_0036EEBA;
loc_0036EDAB:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x38)))) & (32)) != 0) goto loc_0036EED8;
loc_0036EDB7:
    *(uint64_t *)(local_rsp - 0xF8 - 0x60) = result;
    goto loc_0036DA92;
loc_0036EDC0:
    if (((uint32_t)(result)) == 9) goto loc_0036E5D4;
    if (*(uint64_t *)(local_rsp - 0xF8 + 0x18) != 0) goto loc_0036F000;
    if (((uint32_t)(result)) != 6) goto loc_0036EFE7;
loc_0036EDEE:
    goto loc_0036E52D;
loc_0036EDFC:
    result = (uint8_t)(((uint8_t)(*(uint8_t *)(*(uint64_t *)(local_rsp - 0xF8 - 0x38) + 0x22))) & (40));
    if (((uint8_t)(result)) == 40) goto loc_0036EF3F;
    if ((((uint8_t)(*(uint8_t *)(*(uint64_t *)(local_rsp - 0xF8 - 0x38) + 0x22))) & (32)) == 0) goto loc_0036EF3F;
    if ((*(uint64_t *)(local_rsp - 0xF8 - 0x78)) != (*(uint64_t *)(*(uint64_t *)(local_rsp - 0xF8 - 0x38) + 0x10))) goto loc_0036EF3F;
    if (sign_flag) goto loc_0036EF3F;
    goto loc_0036DD33;
loc_0036EE40:
    if ((*(uint64_t *)(local_rsp - 0xF8 - 0x70) + *(uint64_t *)(local_rsp - 0xF8) * 8) <= (*(uint64_t *)(local_rsp - 0xF8 + 0x108))) goto loc_0036F09D;
    goto loc_0036DDC2;
loc_0036EE60:
    if (*(uint64_t *)(local_rsp - 0xF8 + 0x110) != 0) goto loc_0036EEB1;
loc_0036EE6C:
    goto loc_0036E9AA;
loc_0036EE76:
    result = (*(uint64_t *)(local_rsp - 0xF8 - 0x38)) + (*(uint64_t *)(local_rsp - 0xF8 + 0x110));
    if ((*(uint64_t *)(local_rsp - 0xF8 + 0x108)) > result) goto loc_0036EAED;
    if ((*(uint64_t *)(local_rsp - 0xF8 + 0x108)) >= (*(uint64_t *)(local_rsp - 0xF8 - 0x38))) goto loc_0036EADD;
    goto loc_0036EAED;
loc_0036EEB1:
    result = MiUnlockProtoPoolPage(*(uint64_t *)(local_rsp - 0xF8 + 0x108), 17, 1, *(uint64_t *)(local_rsp - 0xF8 - 0x70));
    goto loc_0036EE6C;
loc_0036EEBA:
    result = MiIsPteInStore(*(uint64_t *)(local_rsp - 0xF8 + 0x108), *(uint64_t *)(local_rsp - 0xF8 - 0x78), 1, *(uint64_t *)(local_rsp - 0xF8 - 0x70));
    if ((uint32_t)(result) != 0) goto loc_0036EDAB;
loc_0036EED8:
    local_rsi = (uint32_t)((local_rsi) | (64));
    goto loc_0036EDB7;
loc_0036EEE0:
    v_stack_p78 = *(uint64_t *)(*(uint64_t *)(v_rip + 0xAC119D) + *(uint16_t *)(result + 0x28) * 8);
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xAC119D) + *(uint16_t *)(result + 0x28) * 8)) == (v_rip + 11312650)) goto loc_0036ED89;
    if ((((uint8_t)(local_rsi)) & (32)) == 0) goto loc_0036ED89;
    if ((*(uint8_t *)(*(uint64_t *)(local_rsp - 0xF8 - 0x40))) != 1) goto loc_0036ED89;
    goto loc_0036ED89;
loc_0036EF26:
    result = (uint32_t)((1) | ((uint32_t)((uint32_t)((uint32_t)(*(uint64_t *)(local_rsp - 0xF8))))));
    *(uint32_t *)(local_rsp - 0xF8 - 0x68) = (uint32_t)((uint32_t)((uint32_t)(*(uint64_t *)(local_rsp - 0xF8))));
    *(uint32_t *)(local_rsp - 0xF8 - 0x58) = (uint32_t)(result);
    goto loc_0036DCA7;
loc_0036EF35:
loc_0036EF3F:
    result = MiUnlockProtoPoolPage(*(uint64_t *)(local_rsp - 0xF8 + 0x110), 17, 1, *(uint64_t *)(local_rsp - 0xF8 - 0x70));
loc_0036EF61:
    goto loc_0036DD58;
loc_0036EF6E:
    Arg2 = ~(*(uint64_t *)(v_rip + 0xABED0B));
    Arg2 = (Arg2) & (*(uint64_t *)(local_rsp - 0xF8 - 0x78));
loc_0036EF9C:
    result = PsReferencePartitionSafe(*(uint64_t *)(*(uint64_t *)(local_rsp - 0xF8 - 0x40) + 0xB8), Arg2, *(uint64_t *)(v_rip + 0xABED0B), *(uint64_t *)(local_rsp - 0xF8 - 0x70));
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0xF8 - 0x10) + 0xC0) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0xF8 - 0x10) + 0xC0)));
    goto loc_0036E4AD;
loc_0036EFC9:
    if (*(uint64_t *)(v_rip + 0xABED0B) != 0) goto loc_0036E4E2;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0xF8 - 0x40) + 0x4)))) & (8)) == 0) goto loc_0036E4E2;
    goto loc_0036E4F0;
loc_0036EFE7:
    if (((uint32_t)(*(uint64_t *)(v_rip + 0xABED0B) + 2)) != 8) goto loc_0036EDEE;
    goto loc_0036EDEE;
loc_0036F000:
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0xF8 + 0x100) + 0x88) = v_stack_p78;
    result = ExAcquireRundownProtection(v_stack_p78 + 18376, Arg2, *(uint64_t *)(v_rip + 0xABED0B), *(uint64_t *)(local_rsp - 0xF8 - 0x70));
loc_0036F044:
    result = PsDereferencePartition(*(uint64_t *)(v_stack_p78 + 0xB8), *(uint64_t *)(local_rsp - 0xF8 + 0x18), *(uint64_t *)(v_rip + 0xABED0B), *(uint64_t *)(local_rsp - 0xF8 - 0x70));
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0xF8 - 0x10) + 0xC0) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0xF8 - 0x10) + 0xC0)));
    goto loc_0036DDAD;
loc_0036F071:
    result = MiUnlockProtoPoolPage(*(uint64_t *)(v_stack_p78 + 0xB8), 17, *(uint64_t *)(v_rip + 0xABED0B), *(uint64_t *)(local_rsp - 0xF8 - 0x18));
    goto loc_0036E894;
loc_0036F07D:
    result = -(*(uint64_t *)(*(uint64_t *)(local_rsp - 0xF8 + 0x100) + 0x80));
    Arg1 = (uint8_t)((*(uint64_t *)(v_stack_p78 + 0xB8)) + (2));
    *(uint8_t *)(*(uint64_t *)(local_rsp - 0xF8 - 0x10) + 0x1) = (uint8_t)(Arg1);
    goto loc_0036E8A9;
loc_0036F09D:
    Arg2 = ~(*(uint64_t *)(v_rip + 0xABEBDC));
    Arg2 = (Arg2) & (*(uint64_t *)(local_rsp - 0xF8 - 0x78));
loc_0036F0CA:
    if ((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0xF8 - 0x10) + 0xC0))) != 0) goto loc_0036EC06;
    result = (*(uint64_t *)(local_rsp - 0xF8 - 0x78)) << (12);
    goto loc_0036EC06;
loc_0036F0E3:
    result = MiReadFromMemoryPagefile(*(uint64_t *)(v_rip + 0xABEBDC), *(uint64_t *)(local_rsp - 0xF8 - 0x10), *(uint64_t *)(v_rip + 0xABEBDC), *(uint64_t *)(local_rsp - 0xF8 - 0x18));
    goto loc_0036E9A5;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x38` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0036D968&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
