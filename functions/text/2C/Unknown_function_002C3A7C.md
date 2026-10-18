# sub_002C3A7C

- RVA: `0x002C3A7C`–`0x002C459E` (길이 `2,850` bytes)
- VA: `0x00000001402C3A7C`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006EA44`
- 디코드: `678`개 명령, `2,850/2,850` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **68**; 고유 호출 대상: **41**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x002C3A85` → [MiCountSharedPages](MiCountSharedPages_function_002C30A4.md) (function, `0x002C30A4`)
- `0x002C3AB0` → [MiChargeFullProcessCommitment](../../page/88/MiChargeFullProcessCommitment_function_00887630.md) (function, `0x00887630`)
- `0x002C3ACB` → [MiReturnFullProcessCommitment](../../page/9E/MiReturnFullProcessCommitment_function_009E5D58.md) (function, `0x009E5D58`)
- `0x002C3AE5` → [LOCK_PAGE_TABLE_COMMITMENT](../2A/LOCK_PAGE_TABLE_COMMITMENT_function_002A6090.md) (function, `0x002A6090`)
- `0x002C3AF3` → [MiCommitPageTablesForVad](../../page/88/MiCommitPageTablesForVad_function_00886D50.md) (function, `0x00886D50`)
- `0x002C3B09` → [UNLOCK_PAGE_TABLE_COMMITMENT](../2E/UNLOCK_PAGE_TABLE_COMMITMENT_function_002E27D0.md) (function, `0x002E27D0`)
- `0x002C3B24` → [MiReturnFullProcessCommitment](../../page/9E/MiReturnFullProcessCommitment_function_009E5D58.md) (function, `0x009E5D58`)
- `0x002C3BE2` → [MiUnlockWorkingSetShared](../27/MiUnlockWorkingSetShared_function_0027D690.md) (function, `0x0027D690`)
- `0x002C3BEA` → [MiLockWorkingSetShared](../27/MiLockWorkingSetShared_function_0027CBF0.md) (function, `0x0027CBF0`)
- `0x002C3BF1` → [KeShouldYieldProcessor](../27/KeShouldYieldProcessor_function_002773E0.md) (function, `0x002773E0`)
- `0x002C3C2F` → [MiMakeSystemAddressValid](../27/MiMakeSystemAddressValid_function_0027FF70.md) (function, `0x0027FF70`)
- `0x002C3CCA` → [MiUpdatePfnProtection](MiUpdatePfnProtection_function_002C5AD0.md) (function, `0x002C5AD0`)
- `0x002C3CDF` → [MiGetProcessorFlushList](../24/MiGetProcessorFlushList_function_00242C90.md) (function, `0x00242C90`)
- `0x002C3D7D` → [MiRevertValidPte](MiRevertValidPte_function_002C5160.md) (function, `0x002C5160`)
- `0x002C3DC7` → [MiFlushTbList](../31/MiFlushTbList_function_00311FC0.md) (function, `0x00311FC0`)
- `0x002C3DCC` → [MiReleaseProcessorFlushList](../31/MiReleaseProcessorFlushList_function_00313C70.md) (function, `0x00313C70`)
- `0x002C3DDC` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x002C3E45` → [MiIncreaseUsedPtes](../24/MiIncreaseUsedPtes_function_00243630.md) (function, `0x00243630`)
- `0x002C3E6B` → [MiSanitizePfnProtection](../36/MiSanitizePfnProtection_function_0036C040.md) (function, `0x0036C040`)
- `0x002C3E72` → [MiMakePrototypePteVadLookup](MiMakePrototypePteVadLookup_function_002C3480.md) (function, `0x002C3480`)
- `0x002C3E98` → [MiGetProtoPteAddress](../32/MiGetProtoPteAddress_function_0032E970.md) (function, `0x0032E970`)
- `0x002C3ED9` → [MiGetPfnProtection](../32/MiGetPfnProtection_function_0032A650.md) (function, `0x0032A650`)
- `0x002C3EEB` → [MiSanitizePfnProtection](../36/MiSanitizePfnProtection_function_0036C040.md) (function, `0x0036C040`)
- `0x002C3EF8` → [MiSetWsleProtection](../29/MiSetWsleProtection_function_002939D8.md) (function, `0x002939D8`)
- `0x002C3F0D` → [MiPteNeedsCommitCharge](MiPteNeedsCommitCharge_function_002C13B0.md) (function, `0x002C13B0`)
- `0x002C3F47` → [MiLocateCloneAddress](../3D/MiLocateCloneAddress_function_003D26B4.md) (function, `0x003D26B4`)
- `0x002C3F89` → [MiCopyOnWrite](../36/MiCopyOnWrite_function_00362A0C.md) (function, `0x00362A0C`)
- `0x002C3FA4` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x002C3FB1` → [MiUnlockWorkingSetShared](../27/MiUnlockWorkingSetShared_function_0027D690.md) (function, `0x0027D690`)
- `0x002C3FBF` → [MiCopyOnWriteCheckConditions](../2A/MiCopyOnWriteCheckConditions_function_002A750C.md) (function, `0x002A750C`)
- `0x002C3FD9` → [MiLockWorkingSetShared](../27/MiLockWorkingSetShared_function_0027CBF0.md) (function, `0x0027CBF0`)
- `0x002C3FF9` → [MiSanitizePfnProtection](../36/MiSanitizePfnProtection_function_0036C040.md) (function, `0x0036C040`)
- `0x002C403A` → [MiSetProtectionOnTransitionPte](MiSetProtectionOnTransitionPte_function_002C586C.md) (function, `0x002C586C`)
- `0x002C4052` → [MiReturnCommit](../24/MiReturnCommit_function_00248410.md) (function, `0x00248410`)
- `0x002C405F` → [MiIsPrototypePteVadLookup](../32/MiIsPrototypePteVadLookup_function_00328B70.md) (function, `0x00328B70`)
- `0x002C4076` → [MiIsPrototypePteVadLookup](../32/MiIsPrototypePteVadLookup_function_00328B70.md) (function, `0x00328B70`)
- `0x002C4090` → [MiIsPrototypePteVadLookup](../32/MiIsPrototypePteVadLookup_function_00328B70.md) (function, `0x00328B70`)
- `0x002C40B1` → [MiSanitizePfnProtection](../36/MiSanitizePfnProtection_function_0036C040.md) (function, `0x0036C040`)
- `0x002C40B8` → [MiMakePrototypePteVadLookup](MiMakePrototypePteVadLookup_function_002C3480.md) (function, `0x002C3480`)
- `0x002C40C8` → [MiReturnFullProcessCommitment](../../page/9E/MiReturnFullProcessCommitment_function_009E5D58.md) (function, `0x009E5D58`)
- `0x002C4116` → [MiGetProcessorFlushList](../24/MiGetProcessorFlushList_function_00242C90.md) (function, `0x00242C90`)
- `0x002C413E` → [MiInitializeTbFlushList](../29/MiInitializeTbFlushList_function_00294F00.md) (function, `0x00294F00`)
- `0x002C41AB` → [MiGetWsleContents](../31/MiGetWsleContents_function_00316540.md) (function, `0x00316540`)
- `0x002C41C7` → [MiInsertTbFlushEntry](../29/MiInsertTbFlushEntry_function_00293670.md) (function, `0x00293670`)
- `0x002C4218` → [MiFreeWsleList](../24/MiFreeWsleList_function_00241168.md) (function, `0x00241168`)
- `0x002C4227` → [MiReleaseProcessorFlushList](../31/MiReleaseProcessorFlushList_function_00313C70.md) (function, `0x00313C70`)
- `0x002C4274` → [MiLockWorkingSetShared](../27/MiLockWorkingSetShared_function_0027CBF0.md) (function, `0x0027CBF0`)
- `0x002C429D` → [MiComputePageCommitment](MiComputePageCommitment_function_002C5C34.md) (function, `0x002C5C34`)
- `0x002C42A8` → [MiUnlockWorkingSetShared](../27/MiUnlockWorkingSetShared_function_0027D690.md) (function, `0x0027D690`)
- `0x002C42BD` → [MiChargeFullProcessCommitment](../../page/88/MiChargeFullProcessCommitment_function_00887630.md) (function, `0x00887630`)
- `0x002C42D6` → [MiTryDeleteTransitionPte](../37/MiTryDeleteTransitionPte_function_003710DC.md) (function, `0x003710DC`)
- `0x002C42EE` → [MiFlushTbList](../31/MiFlushTbList_function_00311FC0.md) (function, `0x00311FC0`)
- `0x002C42F8` → [MiReleaseProcessorFlushList](../31/MiReleaseProcessorFlushList_function_00313C70.md) (function, `0x00313C70`)
- `0x002C4360` → [MiDecreaseUsedPtes](../37/MiDecreaseUsedPtes_function_00378080.md) (function, `0x00378080`)
- `0x002C439D` → [IS_PTE_NOT_DEMAND_ZERO](../22/IS_PTE_NOT_DEMAND_ZERO_function_0022F4D0.md) (function, `0x0022F4D0`)
- `0x002C43B9` → [MiFlushTbList](../31/MiFlushTbList_function_00311FC0.md) (function, `0x00311FC0`)
- `0x002C43C3` → [MiReleaseProcessorFlushList](../31/MiReleaseProcessorFlushList_function_00313C70.md) (function, `0x00313C70`)
- `0x002C43D2` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x002C4400` → [MiChargeCommit](../28/MiChargeCommit_function_00286EB0.md) (function, `0x00286EB0`)
- `0x002C441D` → [MiReturnFullProcessCommitment](../../page/9E/MiReturnFullProcessCommitment_function_009E5D58.md) (function, `0x009E5D58`)
- `0x002C447B` → [MiGetProtoPteAddress](../32/MiGetProtoPteAddress_function_0032E970.md) (function, `0x0032E970`)
- `0x002C449A` → [MiFlushTbList](../31/MiFlushTbList_function_00311FC0.md) (function, `0x00311FC0`)
- `0x002C44A7` → [MiReleaseProcessorFlushList](../31/MiReleaseProcessorFlushList_function_00313C70.md) (function, `0x00313C70`)
- `0x002C44BE` → [MiMakeProtoLeafValid](../2A/MiMakeProtoLeafValid_function_002A6710.md) (function, `0x002A6710`)
- `0x002C451B` → [MiFreeWsleList](../24/MiFreeWsleList_function_00241168.md) (function, `0x00241168`)
- `0x002C4535` → [MiUnlockVa](../40/MiUnlockVa_function_00407F24.md) (function, `0x00407F24`)
- `0x002C4569` → [MiReturnCommit](../24/MiReturnCommit_function_00248410.md) (function, `0x00248410`)
- `0x002C4594` → [MiReleasePageFileInfo](../28/MiReleasePageFileInfo_function_00283FD0.md) (function, `0x00283FD0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x002C3BA6` → RVA `0x00E38840` (`.data`; read)
- `0x002C432C` → RVA `0x00010880` (`.rdata`; read)
- `0x002C4446` → RVA `0x00E2DC80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **7**
  - `0x002C3AB0` → [MiChargeFullProcessCommitment](../../page/88/MiChargeFullProcessCommitment_function_00887630.md) (`.text` → `PAGE`)
  - `0x002C3ACB` → [MiReturnFullProcessCommitment](../../page/9E/MiReturnFullProcessCommitment_function_009E5D58.md) (`.text` → `PAGE`)
  - `0x002C3AF3` → [MiCommitPageTablesForVad](../../page/88/MiCommitPageTablesForVad_function_00886D50.md) (`.text` → `PAGE`)
  - `0x002C3B24` → [MiReturnFullProcessCommitment](../../page/9E/MiReturnFullProcessCommitment_function_009E5D58.md) (`.text` → `PAGE`)
  - `0x002C40C8` → [MiReturnFullProcessCommitment](../../page/9E/MiReturnFullProcessCommitment_function_009E5D58.md) (`.text` → `PAGE`)
  - `0x002C42BD` → [MiChargeFullProcessCommitment](../../page/88/MiChargeFullProcessCommitment_function_00887630.md) (`.text` → `PAGE`)
  - `0x002C441D` → [MiReturnFullProcessCommitment](../../page/9E/MiReturnFullProcessCommitment_function_009E5D58.md) (`.text` → `PAGE`)
- call이 아닌 외부 분기/꼬리 이동: **14**
  - `0x002C3A9D` → [sub_002C37D9 + 0xDF](Unknown_function_002C37D9.md) (`tail-transfer`)
  - `0x002C3AB9` → [sub_002C37D9 + 0xE6](Unknown_function_002C37D9.md) (`tail-transfer`)
  - `0x002C3AD2` → [sub_002C37D9 + 0x244](Unknown_function_002C37D9.md) (`tail-transfer`)
  - `0x002C3AFC` → [sub_002C37D9 + 0xF6](Unknown_function_002C37D9.md) (`tail-transfer`)
  - `0x002C3DE6` → [sub_002C37D9 + 0x1B3](Unknown_function_002C37D9.md) (`tail-transfer`)
  - `0x002C4057` → [sub_002C37D9 + 0x1F5](Unknown_function_002C37D9.md) (`tail-transfer`)
  - `0x002C40CD` → [sub_002C37D9 + 0x242](Unknown_function_002C37D9.md) (`tail-transfer`)
  - `0x002C4256` → [sub_002C37D9 + 0xDF](Unknown_function_002C37D9.md) (`tail-transfer`)
  - `0x002C426B` → [sub_002C37D9 + 0xBC](Unknown_function_002C37D9.md) (`tail-transfer`)
  - `0x002C42C4` → [sub_002C37D9 + 0x244](Unknown_function_002C37D9.md) (`tail-transfer`)
  - `0x002C42CE` → [sub_002C37D9 + 0xBC](Unknown_function_002C37D9.md) (`tail-transfer`)
  - `0x002C4427` → [sub_002C37D9 + 0x244](Unknown_function_002C37D9.md) (`tail-transfer`)
  - `0x002C4578` → [sub_002C37D9 + 0x1E8](Unknown_function_002C37D9.md) (`tail-transfer`)
  - `0x002C4585` → [sub_002C37D9 + 0x1E8](Unknown_function_002C37D9.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002C3A7C  4C 8B C3                        mov r8, rbx
002C3A7F  49 8B D6                        mov rdx, r14
002C3A82  49 8B CD                        mov rcx, r13
002C3A85  E8 1A F6 FF FF                  call 0x1402c30a4
002C3A8A  83 BD A8 00 00 00 00            cmp dword ptr [rbp + 0xa8], 0
002C3A91  48 8B F8                        mov rdi, rax
002C3A94  0F 85 9D 07 00 00               jne 0x1402c4237
002C3A9A  48 85 C0                        test rax, rax
002C3A9D  0F 84 15 FE FF FF               je 0x1402c38b8
002C3AA3  4C 8B A5 80 00 00 00            mov r12, qword ptr [rbp + 0x80]
002C3AAA  48 8B D0                        mov rdx, rax
002C3AAD  49 8B CC                        mov rcx, r12
002C3AB0  E8 7B 3B 5C 00                  call 0x140887630
002C3AB5  8B D8                           mov ebx, eax
002C3AB7  85 C0                           test eax, eax
002C3AB9  0F 89 00 FE FF FF               jns 0x1402c38bf
002C3ABF  48 8B 55 80                     mov rdx, qword ptr [rbp - 0x80]
002C3AC3  48 85 D2                        test rdx, rdx
002C3AC6  74 08                           je 0x1402c3ad0
002C3AC8  49 8B CC                        mov rcx, r12
002C3ACB  E8 88 22 72 00                  call 0x1409e5d58
002C3AD0  8B C3                           mov eax, ebx
002C3AD2  E9 46 FF FF FF                  jmp 0x1402c3a1d
002C3AD7  48 8B 4D E0                     mov rcx, qword ptr [rbp - 0x20]
002C3ADB  49 8B D4                        mov rdx, r12
002C3ADE  C7 45 A4 01 00 00 00            mov dword ptr [rbp - 0x5c], 1
002C3AE5  E8 A6 25 FE FF                  call 0x1402a6090
002C3AEA  4D 8B C7                        mov r8, r15
002C3AED  48 8B D6                        mov rdx, rsi
002C3AF0  49 8B CD                        mov rcx, r13
002C3AF3  E8 58 32 5C 00                  call 0x140886d50
002C3AF8  8B D8                           mov ebx, eax
002C3AFA  85 C0                           test eax, eax
002C3AFC  0F 89 CD FD FF FF               jns 0x1402c38cf
002C3B02  48 8B 4D E0                     mov rcx, qword ptr [rbp - 0x20]
002C3B06  49 8B D4                        mov rdx, r12
002C3B09  E8 C2 EC 01 00                  call 0x1402e27d0
002C3B0E  48 83 7D B0 00                  cmp qword ptr [rbp - 0x50], 0
002C3B13  0F 85 46 0A 00 00               jne 0x1402c455f
002C3B19  48 85 FF                        test rdi, rdi
002C3B1C  74 A1                           je 0x1402c3abf
002C3B1E  48 8B D7                        mov rdx, rdi
002C3B21  49 8B CC                        mov rcx, r12
002C3B24  E8 2F 22 72 00                  call 0x1409e5d58
002C3B29  EB 94                           jmp 0x1402c3abf
002C3B2B  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
002C3B35  48 8B C0                        mov rax, rax
002C3B38  48 C1 E0 19                     shl rax, 0x19
002C3B3C  48 B9 FF FF FF FF FF 00 00 00   movabs rcx, 0xffffffffff
002C3B46  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
002C3B4A  48 BA 00 00 00 00 00 DE FF FF   movabs rdx, 0xffffde0000000000
002C3B54  EB 0F                           jmp 0x1402c3b65
002C3B56  66 66 0F 1F 84 00 00 00 00 00   nop word ptr [rax + rax]
002C3B60  4C 8B 64 24 68                  mov r12, qword ptr [rsp + 0x68]
002C3B65  49 F7 C6 FF 0F 00 00            test r14, 0xfff
002C3B6C  74 0B                           je 0x1402c3b79
002C3B6E  83 7C 24 70 00                  cmp dword ptr [rsp + 0x70], 0
002C3B73  0F 84 D3 00 00 00               je 0x1402c3c4c
002C3B79  45 33 FF                        xor r15d, r15d
002C3B7C  44 89 7C 24 70                  mov dword ptr [rsp + 0x70], r15d
002C3B81  4D 85 E4                        test r12, r12
002C3B84  0F 85 22 08 00 00               jne 0x1402c43ac
002C3B8A  8B 87 B8 00 00 00               mov eax, dword ptr [rdi + 0xb8]
002C3B90  24 0F                           and al, 0xf
002C3B92  3C 05                           cmp al, 5
002C3B94  77 5B                           ja 0x1402c3bf1
002C3B96  8B 87 B8 00 00 00               mov eax, dword ptr [rdi + 0xb8]
002C3B9C  24 0F                           and al, 0xf
002C3B9E  3C 01                           cmp al, 1
002C3BA0  0F 85 86 08 00 00               jne 0x1402c442c
002C3BA6  48 8D 0D 93 4C B7 00            lea rcx, [rip + 0xb74c93]
002C3BAD  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
002C3BB6  48 8B 09                        mov rcx, qword ptr [rcx]
002C3BB9  48 8B 90 38 88 00 00            mov rdx, qword ptr [rax + 0x8838]
002C3BC0  48 85 D2                        test rdx, rdx
002C3BC3  0F 84 EF 02 00 00               je 0x1402c3eb8
002C3BC9  8B 82 44 01 00 00               mov eax, dword ptr [rdx + 0x144]
002C3BCF  48 C1 E0 06                     shl rax, 6
002C3BD3  8B 04 01                        mov eax, dword ptr [rcx + rax]
002C3BD6  0F BA E0 1E                     bt eax, 0x1e
002C3BDA  73 15                           jae 0x1402c3bf1
002C3BDC  0F B6 D3                        movzx edx, bl
002C3BDF  48 8B CF                        mov rcx, rdi
002C3BE2  E8 A9 9A FB FF                  call 0x14027d690
002C3BE7  48 8B CF                        mov rcx, rdi
002C3BEA  E8 01 90 FB FF                  call 0x14027cbf0
002C3BEF  EB 09                           jmp 0x1402c3bfa
002C3BF1  E8 EA 37 FB FF                  call 0x1402773e0
002C3BF6  85 C0                           test eax, eax
002C3BF8  75 E2                           jne 0x1402c3bdc
002C3BFA  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
002C3C04  4D 8B E6                        mov r12, r14
002C3C07  49 C1 EC 09                     shr r12, 9
002C3C0B  4C 23 E0                        and r12, rax
002C3C0E  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
002C3C18  48 8B C0                        mov rax, rax
002C3C1B  4C 03 E0                        add r12, rax
002C3C1E  45 33 C9                        xor r9d, r9d
002C3C21  44 0F B6 C3                     movzx r8d, bl
002C3C25  4C 89 64 24 68                  mov qword ptr [rsp + 0x68], r12
002C3C2A  8B D6                           mov edx, esi
002C3C2C  49 8B CE                        mov rcx, r14
002C3C2F  E8 3C C3 FB FF                  call 0x14027ff70
002C3C34  48 8B 45 F0                     mov rax, qword ptr [rbp - 0x10]
002C3C38  48 B9 FF FF FF FF FF 00 00 00   movabs rcx, 0xffffffffff
002C3C42  48 BA 00 00 00 00 00 DE FF FF   movabs rdx, 0xffffde0000000000
002C3C4C  49 8B 1E                        mov rbx, qword ptr [r14]
002C3C4F  4D 8B FE                        mov r15, r14
002C3C52  49 C1 E7 19                     shl r15, 0x19
002C3C56  4C 2B F8                        sub r15, rax
002C3C59  49 C1 FF 10                     sar r15, 0x10
002C3C5D  F6 C3 01                        test bl, 1
002C3C60  0F 84 85 01 00 00               je 0x1402c3deb
002C3C66  48 8B C3                        mov rax, rbx
002C3C69  48 C1 E8 0C                     shr rax, 0xc
002C3C6D  48 23 C1                        and rax, rcx
002C3C70  48 89 45 B8                     mov qword ptr [rbp - 0x48], rax
002C3C74  4C 8D 24 40                     lea r12, [rax + rax*2]
002C3C78  49 C1 E4 04                     shl r12, 4
002C3C7C  48 8B C2                        mov rax, rdx
002C3C7F  4C 03 E0                        add r12, rax
002C3C82  49 8B 44 24 28                  mov rax, qword ptr [r12 + 0x28]
002C3C87  48 85 C0                        test rax, rax
002C3C8A  0F 88 EF 01 00 00               js 0x1402c3e7f
002C3C90  8B 85 A0 00 00 00               mov eax, dword ptr [rbp + 0xa0]
002C3C96  25 01 01 00 00                  and eax, 0x101
002C3C9B  89 45 CC                        mov dword ptr [rbp - 0x34], eax
002C3C9E  0F 85 2E 04 00 00               jne 0x1402c40d2
002C3CA4  83 BD A8 00 00 00 00            cmp dword ptr [rbp + 0xa8], 0
002C3CAB  0F 85 55 06 00 00               jne 0x1402c4306
002C3CB1  49 8B 44 24 28                  mov rax, qword ptr [r12 + 0x28]
002C3CB6  48 85 C0                        test rax, rax
002C3CB9  0F 88 01 02 00 00               js 0x1402c3ec0
002C3CBF  44 8B 44 24 74                  mov r8d, dword ptr [rsp + 0x74]
002C3CC4  49 8B D4                        mov rdx, r12
002C3CC7  49 8B CD                        mov rcx, r13
002C3CCA  E8 01 1E 00 00                  call 0x1402c5ad0
002C3CCF  8B D8                           mov ebx, eax
002C3CD1  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
002C3CD6  48 85 C0                        test rax, rax
002C3CD9  0F 85 8C 00 00 00               jne 0x1402c3d6b
002C3CDF  E8 AC EF F7 FF                  call 0x140242c90
002C3CE4  45 33 C0                        xor r8d, r8d
002C3CE7  48 89 45 90                     mov qword ptr [rbp - 0x70], rax
002C3CEB  48 8B D0                        mov rdx, rax
002C3CEE  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
002C3CF3  44 89 40 10                     mov dword ptr [rax + 0x10], r8d
002C3CF7  C7 40 14 20 00 00 00            mov dword ptr [rax + 0x14], 0x20
002C3CFE  48 89 38                        mov qword ptr [rax], rdi
002C3D01  8B 8F B8 00 00 00               mov ecx, dword ptr [rdi + 0xb8]
002C3D07  C1 E9 08                        shr ecx, 8
002C3D0A  C0 E9 03                        shr cl, 3
002C3D0D  80 E1 01                        and cl, 1
002C3D10  88 48 18                        mov byte ptr [rax + 0x18], cl
002C3D13  8B 87 B8 00 00 00               mov eax, dword ptr [rdi + 0xb8]
002C3D19  A8 0F                           test al, 0xf
002C3D1B  75 20                           jne 0x1402c3d3d
002C3D1D  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
002C3D26  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
002C3D2D  48 81 C1 00 04 00 00            add rcx, 0x400
002C3D34  48 3B F9                        cmp rdi, rcx
002C3D37  0F 85 A4 06 00 00               jne 0x1402c43e1
002C3D3D  8B 87 B8 00 00 00               mov eax, dword ptr [rdi + 0xb8]
002C3D43  A8 0F                           test al, 0xf
002C3D45  0F 85 9A 06 00 00               jne 0x1402c43e5
002C3D4B  B8 01 00 00 00                  mov eax, 1
002C3D50  83 62 10 DB                     and dword ptr [rdx + 0x10], 0xffffffdb
002C3D54  89 42 08                        mov dword ptr [rdx + 8], eax
002C3D57  48 8B C2                        mov rax, rdx
002C3D5A  66 44 89 42 19                  mov word ptr [rdx + 0x19], r8w
002C3D5F  44 89 42 1C                     mov dword ptr [rdx + 0x1c], r8d
002C3D63  4C 89 42 20                     mov qword ptr [rdx + 0x20], r8
002C3D67  4C 89 42 28                     mov qword ptr [rdx + 0x28], r8
002C3D6B  4C 8B 4D B8                     mov r9, qword ptr [rbp - 0x48]
002C3D6F  44 8B C3                        mov r8d, ebx
002C3D72  49 8B D6                        mov rdx, r14
002C3D75  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
002C3D7A  49 8B CD                        mov rcx, r13
002C3D7D  E8 DE 13 00 00                  call 0x1402c5160
002C3D82  49 83 C6 08                     add r14, 8
002C3D86  4C 89 75 D8                     mov qword ptr [rbp - 0x28], r14
002C3D8A  4C 8B 7C 24 68                  mov r15, qword ptr [rsp + 0x68]
002C3D8F  48 B9 FF FF FF FF FF 00 00 00   movabs rcx, 0xffffffffff
002C3D99  48 8B 7D 98                     mov rdi, qword ptr [rbp - 0x68]
002C3D9D  0F B6 5C 24 50                  movzx ebx, byte ptr [rsp + 0x50]
002C3DA2  48 8B 45 F0                     mov rax, qword ptr [rbp - 0x10]
002C3DA6  48 BA 00 00 00 00 00 DE FF FF   movabs rdx, 0xffffde0000000000
002C3DB0  4C 3B 75 A8                     cmp r14, qword ptr [rbp - 0x58]
002C3DB4  0F 86 A6 FD FF FF               jbe 0x1402c3b60
002C3DBA  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
002C3DBF  48 85 C0                        test rax, rax
002C3DC2  74 0D                           je 0x1402c3dd1
002C3DC4  48 8B C8                        mov rcx, rax
002C3DC7  E8 F4 E1 04 00                  call 0x140311fc0
002C3DCC  E8 9F FE 04 00                  call 0x140313c70
002C3DD1  4D 85 FF                        test r15, r15
002C3DD4  74 0B                           je 0x1402c3de1
002C3DD6  49 8B D7                        mov rdx, r15
002C3DD9  48 8B CF                        mov rcx, rdi
002C3DDC  E8 DF 30 F5 FF                  call 0x140216ec0
002C3DE1  4C 8B 7C 24 78                  mov r15, qword ptr [rsp + 0x78]
002C3DE6  E9 A1 FB FF FF                  jmp 0x1402c398c
002C3DEB  48 0F BA E3 0A                  bt rbx, 0xa
002C3DF0  0F 82 66 02 00 00               jb 0x1402c405c
002C3DF6  48 0F BA E3 0B                  bt rbx, 0xb
002C3DFB  0F 82 1B 02 00 00               jb 0x1402c401c
002C3E01  40 32 FF                        xor dil, dil
002C3E04  83 BD A8 00 00 00 00            cmp dword ptr [rbp + 0xa8], 0
002C3E0B  0F 85 5C 05 00 00               jne 0x1402c436d
002C3E11  48 85 DB                        test rbx, rbx
002C3E14  0F 85 C9 01 00 00               jne 0x1402c3fe3
002C3E1A  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
002C3E24  49 8B D6                        mov rdx, r14
002C3E27  48 C1 EA 09                     shr rdx, 9
002C3E2B  48 23 D0                        and rdx, rax
002C3E2E  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
002C3E38  48 8B C0                        mov rax, rax
002C3E3B  45 33 C9                        xor r9d, r9d
002C3E3E  48 03 D0                        add rdx, rax
002C3E41  45 8D 41 01                     lea r8d, [r9 + 1]
002C3E45  E8 E6 F7 F7 FF                  call 0x140243630
002C3E4A  83 7C 24 58 05                  cmp dword ptr [rsp + 0x58], 5
002C3E4F  0F 85 AD 00 00 00               jne 0x1402c3f02
002C3E55  49 8B 45 48                     mov rax, qword ptr [r13 + 0x48]
002C3E59  33 C9                           xor ecx, ecx
002C3E5B  44 8B 45 8C                     mov r8d, dword ptr [rbp - 0x74]
002C3E5F  8B 50 20                        mov edx, dword ptr [rax + 0x20]
002C3E62  D1 EA                           shr edx, 1
002C3E64  83 E2 1F                        and edx, 0x1f
002C3E67  89 54 24 54                     mov dword ptr [rsp + 0x54], edx
002C3E6B  E8 D0 81 0A 00                  call 0x14036c040
002C3E70  8B C8                           mov ecx, eax
002C3E72  E8 09 F6 FF FF                  call 0x1402c3480
002C3E77  49 89 06                        mov qword ptr [r14], rax
002C3E7A  E9 03 FF FF FF                  jmp 0x1402c3d82
002C3E7F  49 8B 7C 24 08                  mov rdi, qword ptr [r12 + 8]
002C3E84  4C 8D 4D 00                     lea r9, [rbp]
002C3E88  49 8B D7                        mov rdx, r15
002C3E8B  41 B8 08 00 00 00               mov r8d, 8
002C3E91  48 C1 EA 0C                     shr rdx, 0xc
002C3E95  49 8B CD                        mov rcx, r13
002C3E98  E8 D3 AA 06 00                  call 0x14032e970
002C3E9D  49 B8 00 00 00 00 00 00 00 80   movabs r8, 0x8000000000000000
002C3EA7  49 0B F8                        or rdi, r8
002C3EAA  48 3B F8                        cmp rdi, rax
002C3EAD  75 75                           jne 0x1402c3f24
002C3EAF  48 8B 7D 98                     mov rdi, qword ptr [rbp - 0x68]
002C3EB3  E9 D8 FD FF FF                  jmp 0x1402c3c90
002C3EB8  41 8B C7                        mov eax, r15d
002C3EBB  E9 0F FD FF FF                  jmp 0x1402c3bcf
002C3EC0  83 7C 24 58 05                  cmp dword ptr [rsp + 0x58], 5
002C3EC5  74 0C                           je 0x1402c3ed3
002C3EC7  48 0F BA E3 09                  bt rbx, 9
002C3ECC  73 05                           jae 0x1402c3ed3
002C3ECE  48 FF 44 24 78                  inc qword ptr [rsp + 0x78]
002C3ED3  4D 8B C4                        mov r8, r12
002C3ED6  49 8B D7                        mov rdx, r15
002C3ED9  E8 72 67 06 00                  call 0x14032a650
002C3EDE  44 8B 45 8C                     mov r8d, dword ptr [rbp - 0x74]
002C3EE2  8B D0                           mov edx, eax
002C3EE4  49 8B CD                        mov rcx, r13
002C3EE7  89 44 24 54                     mov dword ptr [rsp + 0x54], eax
002C3EEB  E8 50 81 0A 00                  call 0x14036c040
002C3EF0  44 8B C0                        mov r8d, eax
002C3EF3  49 8B D7                        mov rdx, r15
002C3EF6  8B D8                           mov ebx, eax
002C3EF8  E8 DB FA FC FF                  call 0x1402939d8
002C3EFD  E9 CF FD FF FF                  jmp 0x1402c3cd1
002C3F02  40 84 FF                        test dil, dil
002C3F05  75 13                           jne 0x1402c3f1a
002C3F07  49 8B D6                        mov rdx, r14
002C3F0A  49 8B CD                        mov rcx, r13
002C3F0D  E8 9E D4 FF FF                  call 0x1402c13b0
002C3F12  85 C0                           test eax, eax
002C3F14  0F 85 3B FF FF FF               jne 0x1402c3e55
002C3F1A  48 FF 44 24 78                  inc qword ptr [rsp + 0x78]
002C3F1F  E9 31 FF FF FF                  jmp 0x1402c3e55
002C3F24  49 8B 44 24 28                  mov rax, qword ptr [r12 + 0x28]
002C3F29  33 DB                           xor ebx, ebx
002C3F2B  48 0F BA E0 28                  bt rax, 0x28
002C3F30  8B FB                           mov edi, ebx
002C3F32  0F 83 A4 05 00 00               jae 0x1402c44dc
002C3F38  49 8B 54 24 08                  mov rdx, qword ptr [r12 + 8]
002C3F3D  48 8B 8D 80 00 00 00            mov rcx, qword ptr [rbp + 0x80]
002C3F44  49 0B D0                        or rdx, r8
002C3F47  E8 68 E7 10 00                  call 0x1403d26b4
002C3F4C  48 8B 91 10 04 00 00            mov rdx, qword ptr [rcx + 0x410]
002C3F53  48 8B F8                        mov rdi, rax
002C3F56  48 8B 48 60                     mov rcx, qword ptr [rax + 0x60]
002C3F5A  48 39 8A 28 04 00 00            cmp qword ptr [rdx + 0x428], rcx
002C3F61  48 0F 46 FB                     cmovbe rdi, rbx
002C3F65  4C 8B 64 24 60                  mov r12, qword ptr [rsp + 0x60]
002C3F6A  4D 85 E4                        test r12, r12
002C3F6D  0F 85 78 03 00 00               jne 0x1402c42eb
002C3F73  45 33 C9                        xor r9d, r9d
002C3F76  48 8D 45 F8                     lea rax, [rbp - 8]
002C3F7A  49 8B D6                        mov rdx, r14
002C3F7D  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
002C3F82  49 8B CF                        mov rcx, r15
002C3F85  4D 8D 41 FF                     lea r8, [r9 - 1]
002C3F89  E8 7E EA 09 00                  call 0x140362a0c
002C3F8E  8B D8                           mov ebx, eax
002C3F90  85 C0                           test eax, eax
002C3F92  0F 89 AC 05 00 00               jns 0x1402c4544
002C3F98  4C 8B 65 98                     mov r12, qword ptr [rbp - 0x68]
002C3F9C  48 8B 54 24 68                  mov rdx, qword ptr [rsp + 0x68]
002C3FA1  49 8B CC                        mov rcx, r12
002C3FA4  E8 17 2F F5 FF                  call 0x140216ec0
002C3FA9  0F B6 54 24 50                  movzx edx, byte ptr [rsp + 0x50]
002C3FAE  49 8B CC                        mov rcx, r12
002C3FB1  E8 DA 96 FB FF                  call 0x14027d690
002C3FB6  4C 8B 45 F8                     mov r8, qword ptr [rbp - 8]
002C3FBA  8B D3                           mov edx, ebx
002C3FBC  49 8B CC                        mov rcx, r12
002C3FBF  E8 48 35 FE FF                  call 0x1402a750c
002C3FC4  33 C0                           xor eax, eax
002C3FC6  C7 44 24 70 01 00 00 00         mov dword ptr [rsp + 0x70], 1
002C3FCE  49 8B CC                        mov rcx, r12
002C3FD1  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
002C3FD6  44 8B F8                        mov r15d, eax
002C3FD9  E8 12 8C FB FF                  call 0x14027cbf0
002C3FDE  E9 AC FD FF FF                  jmp 0x1402c3d8f
002C3FE3  44 8B 44 24 74                  mov r8d, dword ptr [rsp + 0x74]
002C3FE8  48 8B D3                        mov rdx, rbx
002C3FEB  48 C1 EA 05                     shr rdx, 5
002C3FEF  49 8B CD                        mov rcx, r13
002C3FF2  83 E2 1F                        and edx, 0x1f
002C3FF5  89 54 24 54                     mov dword ptr [rsp + 0x54], edx
002C3FF9  E8 42 80 0A 00                  call 0x14036c040
002C3FFE  8B C8                           mov ecx, eax
002C4000  89 44 24 74                     mov dword ptr [rsp + 0x74], eax
002C4004  48 C1 E1 05                     shl rcx, 5
002C4008  48 8B C1                        mov rax, rcx
002C400B  48 33 C3                        xor rax, rbx
002C400E  48 25 1F FC FF FF               and rax, 0xfffffffffffffc1f
002C4014  48 33 C1                        xor rax, rcx
002C4017  E9 5B FE FF FF                  jmp 0x1402c3e77
002C401C  83 BD A8 00 00 00 00            cmp dword ptr [rbp + 0xa8], 0
002C4023  0F 85 AA 02 00 00               jne 0x1402c42d3
002C4029  44 8B 44 24 74                  mov r8d, dword ptr [rsp + 0x74]
002C402E  41 B9 01 00 00 00               mov r9d, 1
002C4034  49 8B D6                        mov rdx, r14
002C4037  49 8B CD                        mov rcx, r13
002C403A  E8 2D 18 00 00                  call 0x1402c586c
002C403F  85 C0                           test eax, eax
002C4041  0F 85 43 FD FF FF               jne 0x1402c3d8a
002C4047  E9 36 FD FF FF                  jmp 0x1402c3d82
002C404C  45 33 C0                        xor r8d, r8d
002C404F  48 8B CE                        mov rcx, rsi
002C4052  E8 B9 43 F8 FF                  call 0x140248410
002C4057  E9 72 F9 FF FF                  jmp 0x1402c39ce
002C405C  48 8B CB                        mov rcx, rbx
002C405F  E8 0C 4B 06 00                  call 0x140328b70
002C4064  85 C0                           test eax, eax
002C4066  0F 84 DA 03 00 00               je 0x1402c4446
002C406C  83 7C 24 58 05                  cmp dword ptr [rsp + 0x58], 5
002C4071  74 1A                           je 0x1402c408d
002C4073  48 8B CB                        mov rcx, rbx
002C4076  E8 F5 4A 06 00                  call 0x140328b70
002C407B  85 C0                           test eax, eax
002C407D  74 0E                           je 0x1402c408d
002C407F  0F B6 C3                        movzx eax, bl
002C4082  24 A0                           and al, 0xa0
002C4084  3C A0                           cmp al, 0xa0
002C4086  75 05                           jne 0x1402c408d
002C4088  48 FF 44 24 78                  inc qword ptr [rsp + 0x78]
002C408D  48 8B CB                        mov rcx, rbx
002C4090  E8 DB 4A 06 00                  call 0x140328b70
002C4095  85 C0                           test eax, eax
002C4097  0F 84 9B 03 00 00               je 0x1402c4438
002C409D  48 C1 EB 05                     shr rbx, 5
002C40A1  44 8B 45 8C                     mov r8d, dword ptr [rbp - 0x74]
002C40A5  83 E3 1F                        and ebx, 0x1f
002C40A8  8B D3                           mov edx, ebx
002C40AA  89 5C 24 54                     mov dword ptr [rsp + 0x54], ebx
002C40AE  49 8B CD                        mov rcx, r13
002C40B1  E8 8A 7F 0A 00                  call 0x14036c040
002C40B6  8B C8                           mov ecx, eax
002C40B8  E8 C3 F3 FF FF                  call 0x1402c3480
002C40BD  49 89 06                        mov qword ptr [r14], rax
002C40C0  E9 BD FC FF FF                  jmp 0x1402c3d82
002C40C5  48 8B CB                        mov rcx, rbx
002C40C8  E8 8B 1C 72 00                  call 0x1409e5d58
002C40CD  E9 49 F9 FF FF                  jmp 0x1402c3a1b
002C40D2  48 8B 45 A8                     mov rax, qword ptr [rbp - 0x58]
002C40D6  49 8B CE                        mov rcx, r14
002C40D9  48 89 45 B8                     mov qword ptr [rbp - 0x48], rax
002C40DD  48 81 E1 00 F0 FF FF            and rcx, 0xfffffffffffff000
002C40E4  48 25 00 F0 FF FF               and rax, 0xfffffffffffff000
002C40EA  48 3B C8                        cmp rcx, rax
002C40ED  74 0B                           je 0x1402c40fa
002C40EF  48 8D 81 F8 0F 00 00            lea rax, [rcx + 0xff8]
002C40F6  48 89 45 B8                     mov qword ptr [rbp - 0x48], rax
002C40FA  48 8B 45 90                     mov rax, qword ptr [rbp - 0x70]
002C40FE  45 32 DB                        xor r11b, r11b
002C4101  44 88 5C 24 51                  mov byte ptr [rsp + 0x51], r11b
002C4106  48 85 C0                        test rax, rax
002C4109  0F 85 DE 02 00 00               jne 0x1402c43ed
002C410F  C7 45 A0 01 00 00 00            mov dword ptr [rbp - 0x60], 1
002C4116  E8 75 EB F7 FF                  call 0x140242c90
002C411B  48 89 45 90                     mov qword ptr [rbp - 0x70], rax
002C411F  48 8D 98 28 10 00 00            lea rbx, [rax + 0x1028]
002C4126  C7 44 24 20 01 00 00 00         mov dword ptr [rsp + 0x20], 1
002C412E  44 8B 43 0C                     mov r8d, dword ptr [rbx + 0xc]
002C4132  48 8B CB                        mov rcx, rbx
002C4135  41 B9 02 00 00 00               mov r9d, 2
002C413B  48 8B D7                        mov rdx, rdi
002C413E  E8 BD 0D FD FF                  call 0x140294f00
002C4143  4D 8B E6                        mov r12, r14
002C4146  4C 3B 75 B8                     cmp r14, qword ptr [rbp - 0x48]
002C414A  0F 87 B9 00 00 00               ja 0x1402c4209
002C4150  8B 75 CC                        mov esi, dword ptr [rbp - 0x34]
002C4153  4C 8B 6D B8                     mov r13, qword ptr [rbp - 0x48]
002C4157  4C 8B B5 B8 00 00 00            mov r14, qword ptr [rbp + 0xb8]
002C415E  49 8B 04 24                     mov rax, qword ptr [r12]
002C4162  A8 01                           test al, 1
002C4164  0F 84 91 00 00 00               je 0x1402c41fb
002C416A  85 F6                           test esi, esi
002C416C  75 3A                           jne 0x1402c41a8
002C416E  39 B5 A8 00 00 00               cmp dword ptr [rbp + 0xa8], esi
002C4174  0F 84 81 00 00 00               je 0x1402c41fb
002C417A  48 C1 E8 0C                     shr rax, 0xc
002C417E  48 B9 FF FF FF FF FF 00 00 00   movabs rcx, 0xffffffffff
002C4188  48 23 C1                        and rax, rcx
002C418B  48 8D 0C 40                     lea rcx, [rax + rax*2]
002C418F  48 B8 28 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000028
002C4199  48 03 C9                        add rcx, rcx
002C419C  48 8B C0                        mov rax, rax
002C419F  48 8B 04 C8                     mov rax, qword ptr [rax + rcx*8]
002C41A3  48 85 C0                        test rax, rax
002C41A6  78 53                           js 0x1402c41fb
002C41A8  49 8B D7                        mov rdx, r15
002C41AB  E8 90 23 05 00                  call 0x140316540
002C41B0  24 0F                           and al, 0xf
002C41B2  3C 08                           cmp al, 8
002C41B4  0F 84 43 03 00 00               je 0x1402c44fd
002C41BA  45 33 C9                        xor r9d, r9d
002C41BD  49 8B D7                        mov rdx, r15
002C41C0  48 8B CB                        mov rcx, rbx
002C41C3  45 8D 41 01                     lea r8d, [r9 + 1]
002C41C7  E8 A4 F4 FC FF                  call 0x140293670
002C41CC  44 0F B6 5C 24 51               movzx r11d, byte ptr [rsp + 0x51]
002C41D2  45 84 DB                        test r11b, r11b
002C41D5  0F 85 31 03 00 00               jne 0x1402c450c
002C41DB  8B 43 0C                        mov eax, dword ptr [rbx + 0xc]
002C41DE  39 43 1C                        cmp dword ptr [rbx + 0x1c], eax
002C41E1  0F 84 25 03 00 00               je 0x1402c450c
002C41E7  49 83 C4 08                     add r12, 8
002C41EB  49 81 C7 00 10 00 00            add r15, 0x1000
002C41F2  4D 3B E5                        cmp r12, r13
002C41F5  0F 86 63 FF FF FF               jbe 0x1402c415e
002C41FB  8B 75 D0                        mov esi, dword ptr [rbp - 0x30]
002C41FE  4C 8B 75 D8                     mov r14, qword ptr [rbp - 0x28]
002C4202  4C 8B AD 88 00 00 00            mov r13, qword ptr [rbp + 0x88]
002C4209  83 7B 1C 00                     cmp dword ptr [rbx + 0x1c], 0
002C420D  74 0E                           je 0x1402c421d
002C420F  45 33 C0                        xor r8d, r8d
002C4212  48 8B D3                        mov rdx, rbx
002C4215  48 8B CF                        mov rcx, rdi
002C4218  E8 4B CF F7 FF                  call 0x140241168
002C421D  83 7D A0 00                     cmp dword ptr [rbp - 0x60], 0
002C4221  0F 84 63 FB FF FF               je 0x1402c3d8a
002C4227  E8 44 FA 04 00                  call 0x140313c70
002C422C  33 C0                           xor eax, eax
002C422E  48 89 45 90                     mov qword ptr [rbp - 0x70], rax
002C4232  E9 53 FB FF FF                  jmp 0x1402c3d8a
002C4237  48 8B C3                        mov rax, rbx
002C423A  49 2B C6                        sub rax, r14
002C423D  48 C1 F8 03                     sar rax, 3
002C4241  48 2B C7                        sub rax, rdi
002C4244  48 83 C0 01                     add rax, 1
002C4248  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
002C424C  0F 85 A5 01 00 00               jne 0x1402c43f7
002C4252  33 C0                           xor eax, eax
002C4254  8B F8                           mov edi, eax
002C4256  E9 5D F6 FF FF                  jmp 0x1402c38b8
002C425B  41 8B 45 34                     mov eax, dword ptr [r13 + 0x34]
002C425F  41 0F B6 4D 22                  movzx ecx, byte ptr [r13 + 0x22]
002C4264  48 C1 E1 20                     shl rcx, 0x20
002C4268  48 0B C8                        or rcx, rax
002C426B  0F 84 24 F6 FF FF               je 0x1402c3895
002C4271  49 8B CC                        mov rcx, r12
002C4274  E8 77 89 FB FF                  call 0x14027cbf0
002C4279  33 C9                           xor ecx, ecx
002C427B  0F B6 D8                        movzx ebx, al
002C427E  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
002C4283  48 8D 45 80                     lea rax, [rbp - 0x80]
002C4287  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
002C428C  44 0F B6 CB                     movzx r9d, bl
002C4290  89 4C 24 20                     mov dword ptr [rsp + 0x20], ecx
002C4294  4D 8B C5                        mov r8, r13
002C4297  48 8B CE                        mov rcx, rsi
002C429A  49 8B D7                        mov rdx, r15
002C429D  E8 92 19 00 00                  call 0x1402c5c34
002C42A2  0F B6 D3                        movzx edx, bl
002C42A5  49 8B CC                        mov rcx, r12
002C42A8  E8 E3 93 FB FF                  call 0x14027d690
002C42AD  48 8B 55 80                     mov rdx, qword ptr [rbp - 0x80]
002C42B1  48 85 D2                        test rdx, rdx
002C42B4  74 14                           je 0x1402c42ca
002C42B6  48 8B 8D 80 00 00 00            mov rcx, qword ptr [rbp + 0x80]
002C42BD  E8 6E 33 5C 00                  call 0x140887630
002C42C2  85 C0                           test eax, eax
002C42C4  0F 88 53 F7 FF FF               js 0x1402c3a1d
002C42CA  48 8B 5D A8                     mov rbx, qword ptr [rbp - 0x58]
002C42CE  E9 C2 F5 FF FF                  jmp 0x1402c3895
002C42D3  49 8B CE                        mov rcx, r14
002C42D6  E8 01 CE 0A 00                  call 0x1403710dc
002C42DB  83 F8 03                        cmp eax, 3
002C42DE  74 39                           je 0x1402c4319
002C42E0  83 F8 01                        cmp eax, 1
002C42E3  0F 84 A1 FA FF FF               je 0x1402c3d8a
002C42E9  EB 32                           jmp 0x1402c431d
002C42EB  49 8B CC                        mov rcx, r12
002C42EE  E8 CD DC 04 00                  call 0x140311fc0
002C42F3  48 89 5C 24 60                  mov qword ptr [rsp + 0x60], rbx
002C42F8  E8 73 F9 04 00                  call 0x140313c70
002C42FD  48 89 5D 90                     mov qword ptr [rbp - 0x70], rbx
002C4301  E9 6D FC FF FF                  jmp 0x1402c3f73
002C4306  49 8B 44 24 28                  mov rax, qword ptr [r12 + 0x28]
002C430B  48 85 C0                        test rax, rax
002C430E  0F 88 9D F9 FF FF               js 0x1402c3cb1
002C4314  E9 B9 FD FF FF                  jmp 0x1402c40d2
002C4319  48 FF 45 E8                     inc qword ptr [rbp - 0x18]
002C431D  48 8B 85 80 00 00 00            mov rax, qword ptr [rbp + 0x80]
002C4324  F0 48 FF 88 88 02 00 00         lock dec qword ptr [rax + 0x288]
002C432C  48 8B 05 4D C5 D4 FF            mov rax, qword ptr [rip - 0x2b3ab3]
002C4333  49 8B D6                        mov rdx, r14
002C4336  49 89 06                        mov qword ptr [r14], rax
002C4339  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
002C4343  48 C1 EA 09                     shr rdx, 9
002C4347  48 23 D0                        and rdx, rax
002C434A  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
002C4354  48 8B C0                        mov rax, rax
002C4357  48 03 D0                        add rdx, rax
002C435A  41 B8 01 00 00 00               mov r8d, 1
002C4360  E8 1B 3D 0B 00                  call 0x140378080
002C4365  40 B7 01                        mov dil, 1
002C4368  E9 AD FA FF FF                  jmp 0x1402c3e1a
002C436D  48 85 DB                        test rbx, rbx
002C4370  0F 84 A4 FA FF FF               je 0x1402c3e1a
002C4376  48 89 5D 10                     mov qword ptr [rbp + 0x10], rbx
002C437A  48 8B 55 10                     mov rdx, qword ptr [rbp + 0x10]
002C437E  0F B6 C2                        movzx eax, dl
002C4381  C0 E8 02                        shr al, 2
002C4384  A8 01                           test al, 1
002C4386  75 09                           jne 0x1402c4391
002C4388  0F B6 C2                        movzx eax, dl
002C438B  D0 E8                           shr al, 1
002C438D  A8 01                           test al, 1
002C438F  74 09                           je 0x1402c439a
002C4391  48 85 D2                        test rdx, rdx
002C4394  0F 85 F0 01 00 00               jne 0x1402c458a
002C439A  48 8B CB                        mov rcx, rbx
002C439D  E8 2E B1 F6 FF                  call 0x14022f4d0
002C43A2  85 C0                           test eax, eax
002C43A4  0F 85 73 FF FF FF               jne 0x1402c431d
002C43AA  EB 80                           jmp 0x1402c432c
002C43AC  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
002C43B1  48 85 DB                        test rbx, rbx
002C43B4  74 16                           je 0x1402c43cc
002C43B6  48 8B CB                        mov rcx, rbx
002C43B9  E8 02 DC 04 00                  call 0x140311fc0
002C43BE  4C 89 7C 24 60                  mov qword ptr [rsp + 0x60], r15
002C43C3  E8 A8 F8 04 00                  call 0x140313c70
002C43C8  4C 89 7D 90                     mov qword ptr [rbp - 0x70], r15
002C43CC  49 8B D4                        mov rdx, r12
002C43CF  48 8B CF                        mov rcx, rdi
002C43D2  E8 E9 2A F5 FF                  call 0x140216ec0
002C43D7  0F B6 5C 24 50                  movzx ebx, byte ptr [rsp + 0x50]
002C43DC  E9 A9 F7 FF FF                  jmp 0x1402c3b8a
002C43E1  83 4A 10 09                     or dword ptr [rdx + 0x10], 9
002C43E5  41 8B C0                        mov eax, r8d
002C43E8  E9 63 F9 FF FF                  jmp 0x1402c3d50
002C43ED  33 C9                           xor ecx, ecx
002C43EF  89 4D A0                        mov dword ptr [rbp - 0x60], ecx
002C43F2  E9 28 FD FF FF                  jmp 0x1402c411f
002C43F7  45 33 C0                        xor r8d, r8d
002C43FA  48 8B D0                        mov rdx, rax
002C43FD  49 8B CC                        mov rcx, r12
002C4400  E8 AB 2A FC FF                  call 0x140286eb0
002C4405  85 C0                           test eax, eax
002C4407  0F 85 45 FE FF FF               jne 0x1402c4252
002C440D  48 8B 55 80                     mov rdx, qword ptr [rbp - 0x80]
002C4411  48 85 D2                        test rdx, rdx
002C4414  74 0C                           je 0x1402c4422
002C4416  48 8B 8D 80 00 00 00            mov rcx, qword ptr [rbp + 0x80]
002C441D  E8 36 19 72 00                  call 0x1409e5d58
002C4422  B8 2D 01 00 C0                  mov eax, 0xc000012d
002C4427  E9 F1 F5 FF FF                  jmp 0x1402c3a1d
002C442C  48 8D 8F C0 00 00 00            lea rcx, [rdi + 0xc0]
002C4433  E9 75 F7 FF FF                  jmp 0x1402c3bad
002C4438  49 8B 45 48                     mov rax, qword ptr [r13 + 0x48]
002C443C  8B 58 20                        mov ebx, dword ptr [rax + 0x20]
002C443F  D1 EB                           shr ebx, 1
002C4441  E9 5B FC FF FF                  jmp 0x1402c40a1
002C4446  48 8B 05 33 98 B6 00            mov rax, qword ptr [rip + 0xb69833]
002C444D  48 8B FB                        mov rdi, rbx
002C4450  48 85 C0                        test rax, rax
002C4453  74 12                           je 0x1402c4467
002C4455  F6 C3 10                        test bl, 0x10
002C4458  0F 85 F8 00 00 00               jne 0x1402c4556
002C445E  48 8B F8                        mov rdi, rax
002C4461  48 F7 D7                        not rdi
002C4464  48 23 FB                        and rdi, rbx
002C4467  49 C1 EF 0C                     shr r15, 0xc
002C446B  4C 8D 4D 00                     lea r9, [rbp]
002C446F  49 8B D7                        mov rdx, r15
002C4472  41 B8 08 00 00 00               mov r8d, 8
002C4478  49 8B CD                        mov rcx, r13
002C447B  E8 F0 A4 06 00                  call 0x14032e970
002C4480  48 C1 FF 10                     sar rdi, 0x10
002C4484  48 3B F8                        cmp rdi, rax
002C4487  0F 84 DF FB FF FF               je 0x1402c406c
002C448D  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
002C4492  48 85 DB                        test rbx, rbx
002C4495  74 19                           je 0x1402c44b0
002C4497  48 8B CB                        mov rcx, rbx
002C449A  E8 21 DB 04 00                  call 0x140311fc0
002C449F  45 33 C0                        xor r8d, r8d
002C44A2  4C 89 44 24 60                  mov qword ptr [rsp + 0x60], r8
002C44A7  E8 C4 F7 04 00                  call 0x140313c70
002C44AC  4C 89 45 90                     mov qword ptr [rbp - 0x70], r8
002C44B0  44 0F B6 44 24 50               movzx r8d, byte ptr [rsp + 0x50]
002C44B6  BA 01 00 00 00                  mov edx, 1
002C44BB  49 8B CE                        mov rcx, r14
002C44BE  E8 4D 22 FE FF                  call 0x1402a6710
002C44C3  85 C0                           test eax, eax
002C44C5  79 08                           jns 0x1402c44cf
002C44C7  49 83 C6 08                     add r14, 8
002C44CB  4C 89 75 D8                     mov qword ptr [rbp - 0x28], r14
002C44CF  C7 44 24 70 01 00 00 00         mov dword ptr [rsp + 0x70], 1
002C44D7  E9 AE F8 FF FF                  jmp 0x1402c3d8a
002C44DC  49 8B 44 24 08                  mov rax, qword ptr [r12 + 8]
002C44E1  48 85 C0                        test rax, rax
002C44E4  0F 88 4E FA FF FF               js 0x1402c3f38
002C44EA  49 8B 44 24 08                  mov rax, qword ptr [r12 + 8]
002C44EF  48 85 C0                        test rax, rax
002C44F2  0F 85 6D FA FF FF               jne 0x1402c3f65
002C44F8  E9 3B FA FF FF                  jmp 0x1402c3f38
002C44FD  41 B3 01                        mov r11b, 1
002C4500  41 C7 06 01 00 00 00            mov dword ptr [r14], 1
002C4507  44 88 5C 24 51                  mov byte ptr [rsp + 0x51], r11b
002C450C  83 7B 1C 00                     cmp dword ptr [rbx + 0x1c], 0
002C4510  74 14                           je 0x1402c4526
002C4512  45 33 C0                        xor r8d, r8d
002C4515  48 8B D3                        mov rdx, rbx
002C4518  48 8B CF                        mov rcx, rdi
002C451B  E8 48 CC F7 FF                  call 0x140241168
002C4520  44 0F B6 5C 24 51               movzx r11d, byte ptr [rsp + 0x51]
002C4526  45 84 DB                        test r11b, r11b
002C4529  0F 84 B8 FC FF FF               je 0x1402c41e7
002C452F  49 8B D7                        mov rdx, r15
002C4532  48 8B CF                        mov rcx, rdi
002C4535  E8 EA 39 14 00                  call 0x140407f24
002C453A  C6 44 24 51 00                  mov byte ptr [rsp + 0x51], 0
002C453F  E9 A3 FC FF FF                  jmp 0x1402c41e7
002C4544  48 85 FF                        test rdi, rdi
002C4547  0F 84 3D F8 FF FF               je 0x1402c3d8a
002C454D  48 FF 4D 80                     dec qword ptr [rbp - 0x80]
002C4551  E9 34 F8 FF FF                  jmp 0x1402c3d8a
002C4556  48 83 E7 EF                     and rdi, 0xffffffffffffffef
002C455A  E9 08 FF FF FF                  jmp 0x1402c4467
002C455F  48 8B 4D C0                     mov rcx, qword ptr [rbp - 0x40]
002C4563  45 33 C0                        xor r8d, r8d
002C4566  48 8B D7                        mov rdx, rdi
002C4569  E8 A2 3E F8 FF                  call 0x140248410
002C456E  E9 4C F5 FF FF                  jmp 0x1402c3abf
002C4573  83 7C 24 58 05                  cmp dword ptr [rsp + 0x58], 5
002C4578  0F 85 43 F4 FF FF               jne 0x1402c39c1
002C457E  48 2B D7                        sub rdx, rdi
002C4581  33 C0                           xor eax, eax
002C4583  8B F8                           mov edi, eax
002C4585  E9 37 F4 FF FF                  jmp 0x1402c39c1
002C458A  48 8B 4D C0                     mov rcx, qword ptr [rbp - 0x40]
002C458E  41 B8 01 00 00 00               mov r8d, 1
002C4594  E8 37 FA FB FF                  call 0x140283fd0
002C4599  E9 FC FD FF FF                  jmp 0x1402c439a
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_002C3A7C(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int8 v_stack_p50;
    unsigned __int8 v_stack_p51;
    unsigned int v_stack_p54;
    unsigned int v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned int v_stack_p70;
    unsigned int v_stack_p74;
    unsigned __int64 v_stack_p78;

    result = MiCountSharedPages(v_r13, v_r14, v_rbx, a4);
    if ((*(unsigned int *)(v_rbp + 168)) != 0) goto loc_002C4237;
    result = MiChargeFullProcessCommitment(*(unsigned __int64 *)(v_rbp + 128), result, v_rbx, a4);
loc_002C3ABF:
    if (*(unsigned __int64 *)(v_rbp - 128) != 0) {
        a1 = *(unsigned __int64 *)(v_rbp + 128);
        result = MiReturnFullProcessCommitment(a1, *(unsigned __int64 *)(v_rbp - 128), v_rbx, a4);
    }
loc_002C4237:
    result = ((unsigned int)((unsigned int)(result))) - (v_r14);
    result = (result) >> (3);
    result = (result) - (result);
    result = (result) + (1);
    *(unsigned __int64 *)(v_rbp - 80) = result;
    if (condition_is_not_equal) goto loc_002C43F7;
loc_002C4252:
    result = 0;
loc_002C43F7:
    a3 = 0;
    result = MiChargeCommit(*(unsigned __int64 *)(v_rbp + 128), 0, a3, a4);
    if ((unsigned int)(result) != 0) goto loc_002C4252;
    if (*(unsigned __int64 *)(v_rbp - 128) != 0) {
        a1 = *(unsigned __int64 *)(v_rbp + 128);
        result = MiReturnFullProcessCommitment(a1, *(unsigned __int64 *)(v_rbp - 128), a3, a4);
    }
}
```

## 5. (Beta) C Style

```c
int64_t sub_002C3A7C(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint8_t v_stack_p50;
    uint8_t v_stack_p51;
    uint32_t v_stack_p54;
    uint32_t v_stack_p58;
    uint64_t v_stack_p60;
    uint64_t v_stack_p68;
    uint32_t v_stack_p70;
    uint32_t v_stack_p74;
    uint64_t v_stack_p78;

    result = MiCountSharedPages(local_r13, local_r14, local_rbx, Arg4);
    if ((*(uint32_t *)(local_rbp + 0xA8)) != 0) goto loc_002C4237;
    result = MiChargeFullProcessCommitment(*(uint64_t *)(local_rbp + 0x80), result, local_rbx, Arg4);
loc_002C3ABF:
    if (*(uint64_t *)(local_rbp - 0x80) != 0) {
        Arg1 = *(uint64_t *)(local_rbp + 0x80);
        result = MiReturnFullProcessCommitment(Arg1, *(uint64_t *)(local_rbp - 0x80), local_rbx, Arg4);
    }
loc_002C4237:
    result = ((uint32_t)((uint32_t)(result))) - (local_r14);
    result = (result) >> (3);
    result = (result) - (result);
    result = (result) + (1);
    *(uint64_t *)(local_rbp - 0x50) = result;
    if (condition_is_not_equal) goto loc_002C43F7;
loc_002C4252:
    result = 0;
loc_002C43F7:
    Arg3 = 0;
    result = MiChargeCommit(*(uint64_t *)(local_rbp + 0x80), 0, Arg3, Arg4);
    if ((uint32_t)(result) != 0) goto loc_002C4252;
    if (*(uint64_t *)(local_rbp - 0x80) != 0) {
        Arg1 = *(uint64_t *)(local_rbp + 0x80);
        result = MiReturnFullProcessCommitment(Arg1, *(uint64_t *)(local_rbp - 0x80), Arg3, Arg4);
    }
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002C3A7C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
