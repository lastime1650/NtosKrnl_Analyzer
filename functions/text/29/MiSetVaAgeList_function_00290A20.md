# MiSetVaAgeList

- RVA: `0x00290A20`–`0x002918A9` (길이 `3,721` bytes)
- VA: `0x0000000140290A20`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00067438`
- 디코드: `862`개 명령, `3,721/3,721` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **34**; 고유 호출 대상: **16**
- 직접 호출자로 확인된 함수: **9**
- RIP 상대 이미지 참조: **6**

### Outgoing calls
- `0x00290B84` → [ExpAcquireSpinLockSharedAtDpcLevelInstrumented](../27/ExpAcquireSpinLockSharedAtDpcLevelInstrumented_function_0027CD20.md) (function, `0x0027CD20`)
- `0x00290EA4` → [MiRemoveActivePageTableLinks](MiRemoveActivePageTableLinks_function_00291FA8.md) (function, `0x00291FA8`)
- `0x00290F34` → [MiRemoveActivePageTableLinks](MiRemoveActivePageTableLinks_function_00291FA8.md) (function, `0x00291FA8`)
- `0x00290F6A` → [MiInsertActivePageTableLinksTail](MiInsertActivePageTableLinksTail_function_00291D98.md) (function, `0x00291D98`)
- `0x00291061` → [MiRemoveActivePageTableLinks](MiRemoveActivePageTableLinks_function_00291FA8.md) (function, `0x00291FA8`)
- `0x00291134` → [MiRemoveActivePageTableLinks](MiRemoveActivePageTableLinks_function_00291FA8.md) (function, `0x00291FA8`)
- `0x0029116A` → [MiInsertActivePageTableLinksTail](MiInsertActivePageTableLinksTail_function_00291D98.md) (function, `0x00291D98`)
- `0x0029120A` → [ExAcquireSpinLockExclusiveAtDpcLevel](../24/ExAcquireSpinLockExclusiveAtDpcLevel_function_00248E80.md) (function, `0x00248E80`)
- `0x0029123F` → [MiPteHasShadow](../32/MiPteHasShadow_function_0032B998.md) (function, `0x0032B998`)
- `0x00291287` → [MiPteHasShadow](../32/MiPteHasShadow_function_0032B998.md) (function, `0x0032B998`)
- `0x0029131D` → [ExAcquireSpinLockExclusiveAtDpcLevel](../24/ExAcquireSpinLockExclusiveAtDpcLevel_function_00248E80.md) (function, `0x00248E80`)
- `0x00291378` → [ExReleaseSpinLockExclusiveFromDpcLevel](../24/ExReleaseSpinLockExclusiveFromDpcLevel_function_002497E0.md) (function, `0x002497E0`)
- `0x00291382` → [MiPteHasShadow](../32/MiPteHasShadow_function_0032B998.md) (function, `0x0032B998`)
- `0x002913C9` → [MiPteHasShadow](../32/MiPteHasShadow_function_0032B998.md) (function, `0x0032B998`)
- `0x00291420` → [MiLockWorkingSetCoreExclusive](../2C/MiLockWorkingSetCoreExclusive_function_002C0CFC.md) (function, `0x002C0CFC`)
- `0x00291442` → [MiUnlockWorkingSetCoreExclusive](../2C/MiUnlockWorkingSetCoreExclusive_function_002C0DC4.md) (function, `0x002C0DC4`)
- `0x00291452` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x0029145E` → [MiPteHasShadow](../32/MiPteHasShadow_function_0032B998.md) (function, `0x0032B998`)
- `0x002914AA` → [MiPteHasShadow](../32/MiPteHasShadow_function_0032B998.md) (function, `0x0032B998`)
- `0x00291534` → [ExpWaitForSpinLockSharedAndAcquire](../36/ExpWaitForSpinLockSharedAndAcquire_function_00362380.md) (function, `0x00362380`)
- `0x00291566` → [MiCheckLinearProtectedPteAccessedBit](MiCheckLinearProtectedPteAccessedBit_function_00292D80.md) (function, `0x00292D80`)
- `0x002915E6` → [ExAcquireSpinLockExclusiveAtDpcLevel](../24/ExAcquireSpinLockExclusiveAtDpcLevel_function_00248E80.md) (function, `0x00248E80`)
- `0x00291645` → [ExReleaseSpinLockExclusiveFromDpcLevel](../24/ExReleaseSpinLockExclusiveFromDpcLevel_function_002497E0.md) (function, `0x002497E0`)
- `0x00291652` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x002916A6` → [MiLockNestedPageTable](../23/MiLockNestedPageTable_function_0023E890.md) (function, `0x0023E890`)
- `0x002916CC` → [MiLockWorkingSetCoreExclusive](../2C/MiLockWorkingSetCoreExclusive_function_002C0CFC.md) (function, `0x002C0CFC`)
- `0x002916D9` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x00291766` → [MiGetPagePrivilege](../28/MiGetPagePrivilege_function_00285420.md) (function, `0x00285420`)
- `0x00291781` → [MiRebuildPageTableAges](../40/MiRebuildPageTableAges_function_0040D4E0.md) (function, `0x0040D4E0`)
- `0x002917D6` → [ExReleaseSpinLockExclusiveFromDpcLevel](../24/ExReleaseSpinLockExclusiveFromDpcLevel_function_002497E0.md) (function, `0x002497E0`)
- `0x002917E3` → [MiUnlockWorkingSetCoreExclusive](../2C/MiUnlockWorkingSetCoreExclusive_function_002C0DC4.md) (function, `0x002C0DC4`)
- `0x002917F8` → [ExReleaseSpinLockExclusiveFromDpcLevel](../24/ExReleaseSpinLockExclusiveFromDpcLevel_function_002497E0.md) (function, `0x002497E0`)
- `0x0029180D` → [ExReleaseSpinLockExclusiveFromDpcLevel](../24/ExReleaseSpinLockExclusiveFromDpcLevel_function_002497E0.md) (function, `0x002497E0`)
- `0x0029184E` → [ExpReleaseSpinLockSharedFromDpcLevelInstrumented](../2F/ExpReleaseSpinLockSharedFromDpcLevelInstrumented_function_002F0F48.md) (function, `0x002F0F48`)

### Direct callers
- [MiResetAccessBitPteWorker](../22/MiResetAccessBitPteWorker_function_0022A6B8.md) at `0x0022A79A`
- [MiActOnPte](../24/MiActOnPte_function_00244C90.md) at `0x0024514B`
- [MiUpdateWsleAge](../28/MiUpdateWsleAge_function_0028F608.md) at `0x0028F6A4`
- [sub_0028FDDD](../28/Unknown_function_0028FDDD.md) at `0x0028FE09`
- [sub_0028FDDD](../28/Unknown_function_0028FDDD.md) at `0x0028FE2B`
- [MiClearPteAccessed](MiClearPteAccessed_function_00290630.md) at `0x002907A6`
- [MiProcessWsInSwapFault](../36/MiProcessWsInSwapFault_function_00361EFC.md) at `0x00361FE3`
- [MiTrimWorkingSetBuildup](../3E/MiTrimWorkingSetBuildup_function_003E03FC.md) at `0x003E069A`
- [MiUnlockWsle](../40/MiUnlockWsle_function_00407F84.md) at `0x0040800B`
- [NtLockVirtualMemory](../40/NtLockVirtualMemory_function_004088A0.md) at `0x00408C89`

### Static image references
- `0x00290AA9` → RVA `0x00E38880` (`.data`; read)
- `0x00290B6F` → RVA `0x00FC6B06` (`ALMOSTRO`; read)
- `0x00290B78` → RVA `0x00F0DE58` (`.data`; read)
- `0x00290D93` → RVA `0x00FC6A88` (`ALMOSTRO`; read)
- `0x002911CB` → RVA `0x00E30088` (`.data`; read)
- `0x00291203` → RVA `0x00E374C0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00290A20  44 88 4C 24 20                  mov byte ptr [rsp + 0x20], r9b
00290A25  44 89 44 24 18                  mov dword ptr [rsp + 0x18], r8d
00290A2A  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
00290A2F  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
00290A34  53                              push rbx
00290A35  55                              push rbp
00290A36  56                              push rsi
00290A37  57                              push rdi
00290A38  41 54                           push r12
00290A3A  41 55                           push r13
00290A3C  41 56                           push r14
00290A3E  41 57                           push r15
00290A40  48 83 EC 58                     sub rsp, 0x58
00290A44  48 8B FA                        mov rdi, rdx
00290A47  45 8B E0                        mov r12d, r8d
00290A4A  48 C1 EF 09                     shr rdi, 9
00290A4E  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
00290A58  4C 8B E9                        mov r13, rcx
00290A5B  48 23 F8                        and rdi, rax
00290A5E  40 32 F6                        xor sil, sil
00290A61  48 B9 00 00 00 00 80 F6 FF FF   movabs rcx, 0xfffff68000000000
00290A6B  48 8B C1                        mov rax, rcx
00290A6E  48 03 F8                        add rdi, rax
00290A71  33 DB                           xor ebx, ebx
00290A73  49 8B 45 10                     mov rax, qword ptr [r13 + 0x10]
00290A77  45 33 FF                        xor r15d, r15d
00290A7A  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00290A7F  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
00290A84  48 89 5C 24 40                  mov qword ptr [rsp + 0x40], rbx
00290A89  89 5C 24 2C                     mov dword ptr [rsp + 0x2c], ebx
00290A8D  44 89 7C 24 24                  mov dword ptr [rsp + 0x24], r15d
00290A92  48 8B C1                        mov rax, rcx
00290A95  48 3B D0                        cmp rdx, rax
00290A98  0F 83 D8 0B 00 00               jae 0x140291676
00290A9E  41 BE 01 00 00 00               mov r14d, 1
00290AA4  44 89 74 24 28                  mov dword ptr [rsp + 0x28], r14d
00290AA9  48 8D 2D D0 7D BA 00            lea rbp, [rip + 0xba7dd0]
00290AB0  41 80 F9 08                     cmp r9b, 8
00290AB4  0F 84 5B 09 00 00               je 0x140291415
00290ABA  33 DB                           xor ebx, ebx
00290ABC  45 85 E4                        test r12d, r12d
00290ABF  0F 84 8D 00 00 00               je 0x140290b52
00290AC5  49 BF F8 D7 BE 7D FB F6 FF FF   movabs r15, 0xfffff6fb7dbed7f8
00290ACF  49 BD 00 D0 BE 7D FB F6 FF FF   movabs r13, 0xfffff6fb7dbed000
00290AD9  48 BD 00 00 00 00 00 DE FF FF   movabs rbp, 0xffffde0000000000
00290AE3  45 85 F6                        test r14d, r14d
00290AE6  0F 84 EA 0B 00 00               je 0x1402916d6
00290AEC  48 8B 37                        mov rsi, qword ptr [rdi]
00290AEF  49 8B C5                        mov rax, r13
00290AF2  48 3B F8                        cmp rdi, rax
00290AF5  72 24                           jb 0x140290b1b
00290AF7  49 8B C7                        mov rax, r15
00290AFA  48 3B F8                        cmp rdi, rax
00290AFD  77 1C                           ja 0x140290b1b
00290AFF  40 F6 C6 01                     test sil, 1
00290B03  74 16                           je 0x140290b1b
00290B05  40 F6 C6 42                     test sil, 0x42
00290B09  0F 95 C1                        setne cl
00290B0C  40 F6 C6 20                     test sil, 0x20
00290B10  0F 95 C0                        setne al
00290B13  84 C8                           test al, cl
00290B15  0F 84 24 07 00 00               je 0x14029123f
00290B1B  48 8B C6                        mov rax, rsi
00290B1E  48 C1 EE 3C                     shr rsi, 0x3c
00290B22  40 80 E6 07                     and sil, 7
00290B26  48 C1 E8 38                     shr rax, 0x38
00290B2A  40 C0 E6 04                     shl sil, 4
00290B2E  24 0F                           and al, 0xf
00290B30  40 0A F0                        or sil, al
00290B33  3C 08                           cmp al, 8
00290B35  74 07                           je 0x140290b3e
00290B37  FF C3                           inc ebx
00290B39  41 3B DC                        cmp ebx, r12d
00290B3C  72 A5                           jb 0x140290ae3
00290B3E  4C 8B AC 24 A0 00 00 00         mov r13, qword ptr [rsp + 0xa0]
00290B46  48 8D 2D 33 7D BA 00            lea rbp, [rip + 0xba7d33]
00290B4D  44 8B 7C 24 24                  mov r15d, dword ptr [rsp + 0x24]
00290B52  41 3B DC                        cmp ebx, r12d
00290B55  0F 85 66 0B 00 00               jne 0x1402916c1
00290B5B  41 8B 85 B8 00 00 00            mov eax, dword ptr [r13 + 0xb8]
00290B62  24 0F                           and al, 0xf
00290B64  3C 01                           cmp al, 1
00290B66  0F 85 B7 0C 00 00               jne 0x140291823
00290B6C  48 8B CD                        mov rcx, rbp
00290B6F  F6 05 90 5F D3 00 21            test byte ptr [rip + 0xd35f90], 0x21
00290B76  74 13                           je 0x140290b8b
00290B78  8B 05 DA D2 C7 00               mov eax, dword ptr [rip + 0xc7d2da]
00290B7E  85 C0                           test eax, eax
00290B80  75 09                           jne 0x140290b8b
00290B82  B2 FF                           mov dl, 0xff
00290B84  E8 97 C1 FE FF                  call 0x14027cd20
00290B89  EB 16                           jmp 0x140290ba1
00290B8B  0F 0D 09                        prefetchw byte ptr [rcx]
00290B8E  8B 01                           mov eax, dword ptr [rcx]
00290B90  0F BA F0 1F                     btr eax, 0x1f
00290B94  8D 50 01                        lea edx, [rax + 1]
00290B97  F0 0F B1 11                     lock cmpxchg dword ptr [rcx], edx
00290B9B  0F 85 89 09 00 00               jne 0x14029152a
00290BA1  4C 8B 4C 24 30                  mov r9, qword ptr [rsp + 0x30]
00290BA6  45 85 E4                        test r12d, r12d
00290BA9  0F 84 E4 04 00 00               je 0x140291093
00290BAF  48 8B 17                        mov rdx, qword ptr [rdi]
00290BB2  49 BA 00 00 00 00 10 00 00 00   movabs r10, 0x1000000000
00290BBC  48 BB 00 D0 BE 7D FB F6 FF FF   movabs rbx, 0xfffff6fb7dbed000
00290BC6  48 8B C3                        mov rax, rbx
00290BC9  49 BB F8 D7 BE 7D FB F6 FF FF   movabs r11, 0xfffff6fb7dbed7f8
00290BD3  48 3B F8                        cmp rdi, rax
00290BD6  72 21                           jb 0x140290bf9
00290BD8  49 8B C3                        mov rax, r11
00290BDB  48 3B F8                        cmp rdi, rax
00290BDE  77 19                           ja 0x140290bf9
00290BE0  F6 C2 01                        test dl, 1
00290BE3  74 14                           je 0x140290bf9
00290BE5  F6 C2 42                        test dl, 0x42
00290BE8  0F 95 C1                        setne cl
00290BEB  F6 C2 20                        test dl, 0x20
00290BEE  0F 95 C0                        setne al
00290BF1  84 C8                           test al, cl
00290BF3  0F 84 8E 06 00 00               je 0x140291287
00290BF9  48 B8 FF FF FF FF FF 00 00 00   movabs rax, 0xffffffffff
00290C03  48 C1 EA 0C                     shr rdx, 0xc
00290C07  48 23 D0                        and rdx, rax
00290C0A  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
00290C14  48 8D 3C 52                     lea rdi, [rdx + rdx*2]
00290C18  48 C1 E7 04                     shl rdi, 4
00290C1C  48 8B C0                        mov rax, rax
00290C1F  48 03 F8                        add rdi, rax
00290C22  45 85 F6                        test r14d, r14d
00290C25  4C 8B B4 24 A8 00 00 00         mov r14, qword ptr [rsp + 0xa8]
00290C2D  0F 84 80 00 00 00               je 0x140290cb3
00290C33  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
00290C3D  4D 8B C6                        mov r8, r14
00290C40  49 C1 E8 09                     shr r8, 9
00290C44  4C 23 C0                        and r8, rax
00290C47  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
00290C51  48 8B C0                        mov rax, rax
00290C54  4C 03 C0                        add r8, rax
00290C57  49 8B 10                        mov rdx, qword ptr [r8]
00290C5A  48 8B C3                        mov rax, rbx
00290C5D  4C 3B C0                        cmp r8, rax
00290C60  72 21                           jb 0x140290c83
00290C62  49 8B C3                        mov rax, r11
00290C65  4C 3B C0                        cmp r8, rax
00290C68  77 19                           ja 0x140290c83
00290C6A  F6 C2 01                        test dl, 1
00290C6D  74 14                           je 0x140290c83
00290C6F  F6 C2 42                        test dl, 0x42
00290C72  0F 95 C1                        setne cl
00290C75  F6 C2 20                        test dl, 0x20
00290C78  0F 95 C0                        setne al
00290C7B  84 C8                           test al, cl
00290C7D  0F 84 FF 06 00 00               je 0x140291382
00290C83  48 8B C2                        mov rax, rdx
00290C86  48 C1 EA 3C                     shr rdx, 0x3c
00290C8A  80 E2 07                        and dl, 7
00290C8D  48 C1 E8 38                     shr rax, 0x38
00290C91  24 0F                           and al, 0xf
00290C93  C0 E2 04                        shl dl, 4
00290C96  0A D0                           or dl, al
00290C98  0F B6 E8                        movzx ebp, al
00290C9B  0F B6 F2                        movzx esi, dl
00290C9E  0F B6 DA                        movzx ebx, dl
00290CA1  3C 08                           cmp al, 8
00290CA3  0F 84 E8 0A 00 00               je 0x140291791
00290CA9  45 33 FF                        xor r15d, r15d
00290CAC  44 89 7C 24 24                  mov dword ptr [rsp + 0x24], r15d
00290CB1  EB 19                           jmp 0x140290ccc
00290CB3  48 8B 2F                        mov rbp, qword ptr [rdi]
00290CB6  40 0F B6 DE                     movzx ebx, sil
00290CBA  48 C1 ED 2A                     shr rbp, 0x2a
00290CBE  40 80 E5 07                     and bpl, 7
00290CC2  40 80 FD 08                     cmp bpl, 8
00290CC6  0F 84 D0 0A 00 00               je 0x14029179c
00290CCC  0F B6 84 24 B8 00 00 00         movzx eax, byte ptr [rsp + 0xb8]
00290CD4  44 0F B6 E0                     movzx r12d, al
00290CD8  88 44 24 20                     mov byte ptr [rsp + 0x20], al
00290CDC  FE C8                           dec al
00290CDE  3C 05                           cmp al, 5
00290CE0  77 44                           ja 0x140290d26
00290CE2  4C 8B 44 24 38                  mov r8, qword ptr [rsp + 0x38]
00290CE7  48 B8 00 D0 BE 7D FB F6 FF FF   movabs rax, 0xfffff6fb7dbed000
00290CF1  49 8B 10                        mov rdx, qword ptr [r8]
00290CF4  48 8B C0                        mov rax, rax
00290CF7  4C 3B C0                        cmp r8, rax
00290CFA  72 21                           jb 0x140290d1d
00290CFC  49 8B C3                        mov rax, r11
00290CFF  4C 3B C0                        cmp r8, rax
00290D02  77 19                           ja 0x140290d1d
00290D04  F6 C2 01                        test dl, 1
00290D07  74 14                           je 0x140290d1d
00290D09  F6 C2 42                        test dl, 0x42
00290D0C  0F 95 C1                        setne cl
00290D0F  F6 C2 20                        test dl, 0x20
00290D12  0F 95 C0                        setne al
00290D15  84 C8                           test al, cl
00290D17  0F 84 8D 07 00 00               je 0x1402914aa
00290D1D  F6 C2 20                        test dl, 0x20
00290D20  0F 85 D1 07 00 00               jne 0x1402914f7
00290D26  83 7C 24 28 00                  cmp dword ptr [rsp + 0x28], 0
00290D2B  0F 84 37 0B 00 00               je 0x140291868
00290D31  0F B6 F3                        movzx esi, bl
00290D34  49 C1 EE 09                     shr r14, 9
00290D38  41 32 F4                        xor sil, r12b
00290D3B  48 BA 00 00 00 00 80 F6 FF FF   movabs rdx, 0xfffff68000000000
00290D45  40 80 E6 0F                     and sil, 0xf
00290D49  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
00290D53  40 32 F3                        xor sil, bl
00290D56  4C 23 F0                        and r14, rax
00290D59  48 8B C2                        mov rax, rdx
00290D5C  4C 03 F0                        add r14, rax
00290D5F  44 0F B6 FE                     movzx r15d, sil
00290D63  48 B9 FF FF FF FF FF FF FF 80   movabs rcx, 0x80ffffffffffffff
00290D6D  49 BC 00 00 00 00 40 00 00 00   movabs r12, 0x4000000000
00290D77  49 8B 3E                        mov rdi, qword ptr [r14]
00290D7A  66 0F 1F 44 00 00               nop word ptr [rax + rax]
00290D80  49 8B C7                        mov rax, r15
00290D83  48 8B DF                        mov rbx, rdi
00290D86  48 C1 E0 38                     shl rax, 0x38
00290D8A  48 33 D8                        xor rbx, rax
00290D8D  48 23 D9                        and rbx, rcx
00290D90  48 33 D8                        xor rbx, rax
00290D93  48 F7 05 EA 5C D3 00 00 00 00 02  test qword ptr [rip + 0xd35cea], 0x2000000
00290D9E  74 03                           je 0x140290da3
00290DA0  0F AE E8                        lfence
00290DA3  48 0F BA 25 DC 5C D3 00 24      bt qword ptr [rip + 0xd35cdc], 0x24
00290DAC  0F 82 8C 07 00 00               jb 0x14029153e
00290DB2  48 8B C7                        mov rax, rdi
00290DB5  F0 49 0F B1 1E                  lock cmpxchg qword ptr [r14], rbx
00290DBA  48 8B F8                        mov rdi, rax
00290DBD  75 C1                           jne 0x140290d80
00290DBF  44 0F B6 64 24 20               movzx r12d, byte ptr [rsp + 0x20]
00290DC5  4C 8B AC 24 A0 00 00 00         mov r13, qword ptr [rsp + 0xa0]
00290DCD  44 8B 54 24 24                  mov r10d, dword ptr [rsp + 0x24]
00290DD2  45 33 FF                        xor r15d, r15d
00290DD5  45 85 D2                        test r10d, r10d
00290DD8  0F 85 AA 01 00 00               jne 0x140290f88
00290DDE  4C 8B 8C 24 A8 00 00 00         mov r9, qword ptr [rsp + 0xa8]
00290DE6  4D 8B C1                        mov r8, r9
00290DE9  48 B8 00 00 00 40 FB F6 FF FF   movabs rax, 0xfffff6fb40000000
00290DF3  49 C1 E8 12                     shr r8, 0x12
00290DF7  41 81 E0 F8 FF FF 3F            and r8d, 0x3ffffff8
00290DFE  48 8B C0                        mov rax, rax
00290E01  4C 03 C0                        add r8, rax
00290E04  48 B8 00 D0 BE 7D FB F6 FF FF   movabs rax, 0xfffff6fb7dbed000
00290E0E  49 8B 10                        mov rdx, qword ptr [r8]
00290E11  48 8B C0                        mov rax, rax
00290E14  4C 3B C0                        cmp r8, rax
00290E17  72 2B                           jb 0x140290e44
00290E19  48 B8 F8 D7 BE 7D FB F6 FF FF   movabs rax, 0xfffff6fb7dbed7f8
00290E23  48 8B C0                        mov rax, rax
00290E26  4C 3B C0                        cmp r8, rax
00290E29  77 19                           ja 0x140290e44
00290E2B  F6 C2 01                        test dl, 1
00290E2E  74 14                           je 0x140290e44
00290E30  F6 C2 42                        test dl, 0x42
00290E33  0F 95 C1                        setne cl
00290E36  F6 C2 20                        test dl, 0x20
00290E39  0F 95 C0                        setne al
00290E3C  84 C8                           test al, cl
00290E3E  0F 84 85 05 00 00               je 0x1402913c9
00290E44  48 B8 FF FF FF FF FF 00 00 00   movabs rax, 0xffffffffff
00290E4E  48 C1 EA 0C                     shr rdx, 0xc
00290E52  48 23 D0                        and rdx, rax
00290E55  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
00290E5F  48 8D 3C 52                     lea rdi, [rdx + rdx*2]
00290E63  48 C1 E7 04                     shl rdi, 4
00290E67  48 8B C0                        mov rax, rax
00290E6A  48 03 F8                        add rdi, rax
00290E6D  48 8B 07                        mov rax, qword ptr [rdi]
00290E70  4C 8B 07                        mov r8, qword ptr [rdi]
00290E73  49 C1 E8 2D                     shr r8, 0x2d
00290E77  48 C1 E8 37                     shr rax, 0x37
00290E7B  41 81 E0 FF 03 00 00            and r8d, 0x3ff
00290E82  24 07                           and al, 7
00290E84  40 3A E8                        cmp bpl, al
00290E87  74 53                           je 0x140290edc
00290E89  0F 86 E0 00 00 00               jbe 0x140290f6f
00290E8F  48 8B 1F                        mov rbx, qword ptr [rdi]
00290E92  8B 47 24                        mov eax, dword ptr [rdi + 0x24]
00290E95  0F BA E0 1A                     bt eax, 0x1a
00290E99  73 0E                           jae 0x140290ea9
00290E9B  45 33 C0                        xor r8d, r8d
00290E9E  48 8B D7                        mov rdx, rdi
00290EA1  49 8B CD                        mov rcx, r13
00290EA4  E8 FF 10 00 00                  call 0x140291fa8
00290EA9  40 0F B6 C5                     movzx eax, bpl
00290EAD  48 BA FF FF FF FF FF FF 7F FC   movabs rdx, 0xfc7fffffffffffff
00290EB7  48 C1 E0 37                     shl rax, 0x37
00290EBB  48 8B C8                        mov rcx, rax
00290EBE  48 33 CB                        xor rcx, rbx
00290EC1  48 23 CA                        and rcx, rdx
00290EC4  48 33 C8                        xor rcx, rax
00290EC7  48 B8 00 00 00 00 00 E0 7F 00   movabs rax, 0x7fe00000000000
00290ED1  48 0B C8                        or rcx, rax
00290ED4  48 89 0F                        mov qword ptr [rdi], rcx
00290ED7  E9 81 00 00 00                  jmp 0x140290f5d
00290EDC  48 8B 07                        mov rax, qword ptr [rdi]
00290EDF  41 8D 48 FF                     lea ecx, [r8 - 1]
00290EE3  8B D1                           mov edx, ecx
00290EE5  48 C1 E2 2D                     shl rdx, 0x2d
00290EE9  48 33 C2                        xor rax, rdx
00290EEC  44 8B F1                        mov r14d, ecx
00290EEF  48 B9 FF FF FF FF FF 1F 80 FF   movabs rcx, 0xff801fffffffffff
00290EF9  41 81 E6 FF 03 00 00            and r14d, 0x3ff
00290F00  48 23 C1                        and rax, rcx
00290F03  48 33 C2                        xor rax, rdx
00290F06  48 89 07                        mov qword ptr [rdi], rax
00290F09  49 8D 40 FF                     lea rax, [r8 - 1]
00290F0D  48 85 C0                        test rax, rax
00290F10  0F 84 62 08 00 00               je 0x140291778
00290F16  8B 47 24                        mov eax, dword ptr [rdi + 0x24]
00290F19  0F BA E0 1A                     bt eax, 0x1a
00290F1D  72 50                           jb 0x140290f6f
00290F1F  48 8B 1F                        mov rbx, qword ptr [rdi]
00290F22  8B 47 24                        mov eax, dword ptr [rdi + 0x24]
00290F25  0F BA E0 1A                     bt eax, 0x1a
00290F29  73 0E                           jae 0x140290f39
00290F2B  45 33 C0                        xor r8d, r8d
00290F2E  48 8B D7                        mov rdx, rdi
00290F31  49 8B CD                        mov rcx, r13
00290F34  E8 6F 10 00 00                  call 0x140291fa8
00290F39  48 8B C5                        mov rax, rbp
00290F3C  48 B9 FF FF FF FF FF 1F 00 FC   movabs rcx, 0xfc001fffffffffff
00290F46  83 E0 07                        and eax, 7
00290F49  48 23 D9                        and rbx, rcx
00290F4C  48 C1 E0 0A                     shl rax, 0xa
00290F50  49 0B C6                        or rax, r14
00290F53  48 C1 E0 2D                     shl rax, 0x2d
00290F57  48 0B C3                        or rax, rbx
00290F5A  48 89 07                        mov qword ptr [rdi], rax
00290F5D  45 33 C9                        xor r9d, r9d
00290F60  44 0F B6 C5                     movzx r8d, bpl
00290F64  48 8B D7                        mov rdx, rdi
00290F67  49 8B CD                        mov rcx, r13
00290F6A  E8 29 0E 00 00                  call 0x140291d98
00290F6F  40 0F B6 C5                     movzx eax, bpl
00290F73  F0 49 FF 4C C5 28               lock dec qword ptr [r13 + rax*8 + 0x28]
00290F79  40 80 FD 07                     cmp bpl, 7
00290F7D  0F 84 3C 02 00 00               je 0x1402911bf
00290F83  44 8B 54 24 24                  mov r10d, dword ptr [rsp + 0x24]
00290F88  41 80 FC 08                     cmp r12b, 8
00290F8C  0F 83 CA 06 00 00               jae 0x14029165c
00290F92  45 85 FF                        test r15d, r15d
00290F95  0F 85 E9 05 00 00               jne 0x140291584
00290F9B  4C 8B 84 24 A8 00 00 00         mov r8, qword ptr [rsp + 0xa8]
00290FA3  49 C1 E8 12                     shr r8, 0x12
00290FA7  41 81 E0 F8 FF FF 3F            and r8d, 0x3ffffff8
00290FAE  48 B8 00 00 00 40 FB F6 FF FF   movabs rax, 0xfffff6fb40000000
00290FB8  48 8B C0                        mov rax, rax
00290FBB  4C 03 C0                        add r8, rax
00290FBE  48 B8 00 D0 BE 7D FB F6 FF FF   movabs rax, 0xfffff6fb7dbed000
00290FC8  49 8B 10                        mov rdx, qword ptr [r8]
00290FCB  48 8B C0                        mov rax, rax
00290FCE  4C 3B C0                        cmp r8, rax
00290FD1  72 2B                           jb 0x140290ffe
00290FD3  48 B8 F8 D7 BE 7D FB F6 FF FF   movabs rax, 0xfffff6fb7dbed7f8
00290FDD  48 8B C0                        mov rax, rax
00290FE0  4C 3B C0                        cmp r8, rax
00290FE3  77 19                           ja 0x140290ffe
00290FE5  F6 C2 01                        test dl, 1
00290FE8  74 14                           je 0x140290ffe
00290FEA  F6 C2 42                        test dl, 0x42
00290FED  0F 95 C1                        setne cl
00290FF0  F6 C2 20                        test dl, 0x20
00290FF3  0F 95 C0                        setne al
00290FF6  84 C8                           test al, cl
00290FF8  0F 84 60 04 00 00               je 0x14029145e
00290FFE  48 B8 FF FF FF FF FF 00 00 00   movabs rax, 0xffffffffff
00291008  48 C1 EA 0C                     shr rdx, 0xc
0029100C  48 23 D0                        and rdx, rax
0029100F  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
00291019  48 8D 3C 52                     lea rdi, [rdx + rdx*2]
0029101D  48 C1 E7 04                     shl rdi, 4
00291021  48 8B C0                        mov rax, rax
00291024  48 03 F8                        add rdi, rax
00291027  48 8B 07                        mov rax, qword ptr [rdi]
0029102A  48 8B 0F                        mov rcx, qword ptr [rdi]
0029102D  48 C1 E9 2D                     shr rcx, 0x2d
00291031  48 C1 E8 37                     shr rax, 0x37
00291035  81 E1 FF 03 00 00               and ecx, 0x3ff
0029103B  24 07                           and al, 7
0029103D  44 3A E0                        cmp r12b, al
00291040  0F 84 A7 00 00 00               je 0x1402910ed
00291046  0F 86 23 01 00 00               jbe 0x14029116f
0029104C  48 8B 1F                        mov rbx, qword ptr [rdi]
0029104F  8B 47 24                        mov eax, dword ptr [rdi + 0x24]
00291052  0F BA E0 1A                     bt eax, 0x1a
00291056  73 0E                           jae 0x140291066
00291058  45 33 C0                        xor r8d, r8d
0029105B  48 8B D7                        mov rdx, rdi
0029105E  49 8B CD                        mov rcx, r13
00291061  E8 42 0F 00 00                  call 0x140291fa8
00291066  49 8B C4                        mov rax, r12
00291069  48 B9 00 00 00 00 00 20 00 00   movabs rcx, 0x200000000000
00291073  83 E0 07                        and eax, 7
00291076  48 C1 E0 37                     shl rax, 0x37
0029107A  48 0B C1                        or rax, rcx
0029107D  48 B9 FF FF FF FF FF 3F 00 FC   movabs rcx, 0xfc003fffffffffff
00291087  E9 C8 00 00 00                  jmp 0x140291154
0029108C  48 8D 2D ED 77 BA 00            lea rbp, [rip + 0xba77ed]
00291093  83 7C 24 2C 00                  cmp dword ptr [rsp + 0x2c], 0
00291098  0F 85 42 07 00 00               jne 0x1402917e0
0029109E  41 8B 85 B8 00 00 00            mov eax, dword ptr [r13 + 0xb8]
002910A5  24 0F                           and al, 0xf
002910A7  3C 01                           cmp al, 1
002910A9  0F 85 68 07 00 00               jne 0x140291817
002910AF  F6 05 50 5A D3 00 01            test byte ptr [rip + 0xd35a50], 1
002910B6  0F 85 79 07 00 00               jne 0x140291835
002910BC  F0 81 65 00 FF FF FF BF         lock and dword ptr [rbp], 0xbfffffff
002910C4  F0 FF 4D 00                     lock dec dword ptr [rbp]
002910C8  48 8B 54 24 40                  mov rdx, qword ptr [rsp + 0x40]
002910CD  48 85 D2                        test rdx, rdx
002910D0  0F 85 79 05 00 00               jne 0x14029164f
002910D6  B8 01 00 00 00                  mov eax, 1
002910DB  48 83 C4 58                     add rsp, 0x58
002910DF  41 5F                           pop r15
002910E1  41 5E                           pop r14
002910E3  41 5D                           pop r13
002910E5  41 5C                           pop r12
002910E7  5F                              pop rdi
002910E8  5E                              pop rsi
002910E9  5D                              pop rbp
002910EA  5B                              pop rbx
002910EB  C3                              ret
002910EC  CC                              int3
002910ED  48 8B 07                        mov rax, qword ptr [rdi]
002910F0  FF C1                           inc ecx
002910F2  8B D1                           mov edx, ecx
002910F4  48 C1 E2 2D                     shl rdx, 0x2d
002910F8  48 33 C2                        xor rax, rdx
002910FB  8B E9                           mov ebp, ecx
002910FD  48 B9 FF FF FF FF FF 1F 80 FF   movabs rcx, 0xff801fffffffffff
00291107  81 E5 FF 03 00 00               and ebp, 0x3ff
0029110D  48 23 C1                        and rax, rcx
00291110  48 33 C2                        xor rax, rdx
00291113  48 89 07                        mov qword ptr [rdi], rax
00291116  8B 47 24                        mov eax, dword ptr [rdi + 0x24]
00291119  0F BA E0 1A                     bt eax, 0x1a
0029111D  72 50                           jb 0x14029116f
0029111F  48 8B 1F                        mov rbx, qword ptr [rdi]
00291122  8B 47 24                        mov eax, dword ptr [rdi + 0x24]
00291125  0F BA E0 1A                     bt eax, 0x1a
00291129  73 0E                           jae 0x140291139
0029112B  45 33 C0                        xor r8d, r8d
0029112E  48 8B D7                        mov rdx, rdi
00291131  49 8B CD                        mov rcx, r13
00291134  E8 6F 0E 00 00                  call 0x140291fa8
00291139  49 8B C4                        mov rax, r12
0029113C  48 B9 FF FF FF FF FF 1F 00 FC   movabs rcx, 0xfc001fffffffffff
00291146  83 E0 07                        and eax, 7
00291149  48 C1 E0 0A                     shl rax, 0xa
0029114D  48 0B C5                        or rax, rbp
00291150  48 C1 E0 2D                     shl rax, 0x2d
00291154  48 23 D9                        and rbx, rcx
00291157  45 33 C9                        xor r9d, r9d
0029115A  48 0B C3                        or rax, rbx
0029115D  45 0F B6 C4                     movzx r8d, r12b
00291161  48 8B D7                        mov rdx, rdi
00291164  48 89 07                        mov qword ptr [rdi], rax
00291167  49 8B CD                        mov rcx, r13
0029116A  E8 29 0C 00 00                  call 0x140291d98
0029116F  41 0F B6 C4                     movzx eax, r12b
00291173  F0 49 FF 44 C5 28               lock inc qword ptr [r13 + rax*8 + 0x28]
00291179  41 80 FC 07                     cmp r12b, 7
0029117D  0F 84 4C 01 00 00               je 0x1402912cf
00291183  44 8B 7C 24 24                  mov r15d, dword ptr [rsp + 0x24]
00291188  4C 8B 4C 24 30                  mov r9, qword ptr [rsp + 0x30]
0029118D  48 8B 7C 24 38                  mov rdi, qword ptr [rsp + 0x38]
00291192  48 81 84 24 A8 00 00 00 00 10 00 00  add qword ptr [rsp + 0xa8], 0x1000
0029119E  48 83 C7 08                     add rdi, 8
002911A2  83 84 24 B0 00 00 00 FF         add dword ptr [rsp + 0xb0], -1
002911AA  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
002911AF  0F 84 D7 FE FF FF               je 0x14029108c
002911B5  44 8B 74 24 28                  mov r14d, dword ptr [rsp + 0x28]
002911BA  E9 F0 F9 FF FF                  jmp 0x140290baf
002911BF  49 8B 55 60                     mov rdx, qword ptr [r13 + 0x60]
002911C3  41 0F B7 8D AE 00 00 00         movzx ecx, word ptr [r13 + 0xae]
002911CB  48 8B 05 B6 EE B9 00            mov rax, qword ptr [rip + 0xb9eeb6]
002911D2  48 8B 1C C8                     mov rbx, qword ptr [rax + rcx*8]
002911D6  48 8B BB C0 44 00 00            mov rdi, qword ptr [rbx + 0x44c0]
002911DD  48 3B 57 38                     cmp rdx, qword ptr [rdi + 0x38]
002911E1  0F 83 9C FD FF FF               jae 0x140290f83
002911E7  49 83 7D 18 00                  cmp qword ptr [r13 + 0x18], 0
002911EC  4D 8D 75 18                     lea r14, [r13 + 0x18]
002911F0  0F 84 8D FD FF FF               je 0x140290f83
002911F6  4C 39 B3 D0 44 00 00            cmp qword ptr [rbx + 0x44d0], r14
002911FD  0F 84 80 FD FF FF               je 0x140290f83
00291203  48 8D 0D B6 62 BA 00            lea rcx, [rip + 0xba62b6]
0029120A  E8 71 7C FB FF                  call 0x140248e80
0029120F  80 7F 35 00                     cmp byte ptr [rdi + 0x35], 0
00291213  0F 85 D4 05 00 00               jne 0x1402917ed
00291219  49 8B 06                        mov rax, qword ptr [r14]
0029121C  48 85 C0                        test rax, rax
0029121F  0F 84 C8 05 00 00               je 0x1402917ed
00291225  49 8B 4E 08                     mov rcx, qword ptr [r14 + 8]
00291229  4C 39 70 08                     cmp qword ptr [rax + 8], r14
0029122D  75 09                           jne 0x140291238
0029122F  4C 39 31                        cmp qword ptr [rcx], r14
00291232  0F 84 6E 05 00 00               je 0x1402917a6
00291238  B9 03 00 00 00                  mov ecx, 3
0029123D  CD 29                           int 0x29
0029123F  E8 54 A7 09 00                  call 0x14032b998
00291244  48 85 C0                        test rax, rax
00291247  0F 84 CE F8 FF FF               je 0x140290b1b
0029124D  48 8B 88 08 05 00 00            mov rcx, qword ptr [rax + 0x508]
00291254  48 85 C9                        test rcx, rcx
00291257  0F 84 BE F8 FF FF               je 0x140290b1b
0029125D  48 8B C7                        mov rax, rdi
00291260  48 C1 E8 03                     shr rax, 3
00291264  25 FF 01 00 00                  and eax, 0x1ff
00291269  48 8B 04 C1                     mov rax, qword ptr [rcx + rax*8]
0029126D  A8 20                           test al, 0x20
0029126F  74 04                           je 0x140291275
00291271  48 83 CE 20                     or rsi, 0x20
00291275  48 8B CE                        mov rcx, rsi
00291278  48 83 CE 42                     or rsi, 0x42
0029127C  A8 42                           test al, 0x42
0029127E  48 0F 44 F1                     cmove rsi, rcx
00291282  E9 94 F8 FF FF                  jmp 0x140290b1b
00291287  E8 0C A7 09 00                  call 0x14032b998
0029128C  48 85 C0                        test rax, rax
0029128F  0F 84 64 F9 FF FF               je 0x140290bf9
00291295  48 8B 88 08 05 00 00            mov rcx, qword ptr [rax + 0x508]
0029129C  48 85 C9                        test rcx, rcx
0029129F  0F 84 54 F9 FF FF               je 0x140290bf9
002912A5  48 8B C7                        mov rax, rdi
002912A8  48 C1 E8 03                     shr rax, 3
002912AC  25 FF 01 00 00                  and eax, 0x1ff
002912B1  48 8B 04 C1                     mov rax, qword ptr [rcx + rax*8]
002912B5  A8 20                           test al, 0x20
002912B7  74 04                           je 0x1402912bd
002912B9  48 83 CA 20                     or rdx, 0x20
002912BD  48 8B CA                        mov rcx, rdx
002912C0  48 83 CA 42                     or rdx, 0x42
002912C4  A8 42                           test al, 0x42
002912C6  48 0F 44 D1                     cmove rdx, rcx
002912CA  E9 2A F9 FF FF                  jmp 0x140290bf9
002912CF  49 8B 55 60                     mov rdx, qword ptr [r13 + 0x60]
002912D3  41 0F B7 8D AE 00 00 00         movzx ecx, word ptr [r13 + 0xae]
002912DB  48 8B 05 A6 ED B9 00            mov rax, qword ptr [rip + 0xb9eda6]
002912E2  4C 8B 04 C8                     mov r8, qword ptr [rax + rcx*8]
002912E6  49 8B B8 C0 44 00 00            mov rdi, qword ptr [r8 + 0x44c0]
002912ED  48 3B 57 38                     cmp rdx, qword ptr [rdi + 0x38]
002912F1  0F 82 8C FE FF FF               jb 0x140291183
002912F7  49 83 7D 18 00                  cmp qword ptr [r13 + 0x18], 0
002912FC  4D 8D 75 18                     lea r14, [r13 + 0x18]
00291300  0F 84 7D FE FF FF               je 0x140291183
00291306  49 8D 98 C8 44 00 00            lea rbx, [r8 + 0x44c8]
0029130D  4C 39 33                        cmp qword ptr [rbx], r14
00291310  0F 84 6D FE FF FF               je 0x140291183
00291316  48 8D 0D A3 61 BA 00            lea rcx, [rip + 0xba61a3]
0029131D  E8 5E 7B FB FF                  call 0x140248e80
00291322  80 7F 35 00                     cmp byte ptr [rdi + 0x35], 0
00291326  0F 85 D6 04 00 00               jne 0x140291802
0029132C  49 8B 06                        mov rax, qword ptr [r14]
0029132F  48 85 C0                        test rax, rax
00291332  0F 84 CA 04 00 00               je 0x140291802
00291338  49 8B 4E 08                     mov rcx, qword ptr [r14 + 8]
0029133C  4C 39 70 08                     cmp qword ptr [rax + 8], r14
00291340  0F 85 F2 FE FF FF               jne 0x140291238
00291346  4C 39 31                        cmp qword ptr [rcx], r14
00291349  0F 85 E9 FE FF FF               jne 0x140291238
0029134F  48 89 01                        mov qword ptr [rcx], rax
00291352  48 89 48 08                     mov qword ptr [rax + 8], rcx
00291356  48 8B 03                        mov rax, qword ptr [rbx]
00291359  48 39 58 08                     cmp qword ptr [rax + 8], rbx
0029135D  0F 85 D5 FE FF FF               jne 0x140291238
00291363  49 89 06                        mov qword ptr [r14], rax
00291366  48 8D 0D 53 61 BA 00            lea rcx, [rip + 0xba6153]
0029136D  49 89 5E 08                     mov qword ptr [r14 + 8], rbx
00291371  4C 89 70 08                     mov qword ptr [rax + 8], r14
00291375  4C 89 33                        mov qword ptr [rbx], r14
00291378  E8 63 84 FB FF                  call 0x1402497e0
0029137D  E9 01 FE FF FF                  jmp 0x140291183
00291382  E8 11 A6 09 00                  call 0x14032b998
00291387  48 85 C0                        test rax, rax
0029138A  0F 84 F3 F8 FF FF               je 0x140290c83
00291390  48 8B 80 08 05 00 00            mov rax, qword ptr [rax + 0x508]
00291397  48 85 C0                        test rax, rax
0029139A  0F 84 E3 F8 FF FF               je 0x140290c83
002913A0  49 C1 E8 03                     shr r8, 3
002913A4  41 81 E0 FF 01 00 00            and r8d, 0x1ff
002913AB  4A 8B 04 C0                     mov rax, qword ptr [rax + r8*8]
002913AF  A8 20                           test al, 0x20
002913B1  74 04                           je 0x1402913b7
002913B3  48 83 CA 20                     or rdx, 0x20
002913B7  48 8B CA                        mov rcx, rdx
002913BA  48 83 CA 42                     or rdx, 0x42
002913BE  A8 42                           test al, 0x42
002913C0  48 0F 44 D1                     cmove rdx, rcx
002913C4  E9 BA F8 FF FF                  jmp 0x140290c83
002913C9  E8 CA A5 09 00                  call 0x14032b998
002913CE  48 85 C0                        test rax, rax
002913D1  0F 84 6D FA FF FF               je 0x140290e44
002913D7  48 8B 80 08 05 00 00            mov rax, qword ptr [rax + 0x508]
002913DE  48 85 C0                        test rax, rax
002913E1  0F 84 5D FA FF FF               je 0x140290e44
002913E7  49 C1 E8 03                     shr r8, 3
002913EB  41 81 E0 FF 01 00 00            and r8d, 0x1ff
002913F2  4A 8B 04 C0                     mov rax, qword ptr [rax + r8*8]
002913F6  A8 20                           test al, 0x20
002913F8  74 04                           je 0x1402913fe
002913FA  48 83 CA 20                     or rdx, 0x20
002913FE  48 8B CA                        mov rcx, rdx
00291401  44 89 54 24 24                  mov dword ptr [rsp + 0x24], r10d
00291406  48 83 CA 42                     or rdx, 0x42
0029140A  A8 42                           test al, 0x42
0029140C  48 0F 44 D1                     cmove rdx, rcx
00291410  E9 2F FA FF FF                  jmp 0x140290e44
00291415  49 8B CD                        mov rcx, r13
00291418  C7 44 24 2C 01 00 00 00         mov dword ptr [rsp + 0x2c], 1
00291420  E8 D7 F8 02 00                  call 0x1402c0cfc
00291425  4C 8B 4C 24 30                  mov r9, qword ptr [rsp + 0x30]
0029142A  49 8B 49 20                     mov rcx, qword ptr [r9 + 0x20]
0029142E  48 83 C1 06                     add rcx, 6
00291432  49 03 CC                        add rcx, r12
00291435  49 39 4D 70                     cmp qword ptr [r13 + 0x70], rcx
00291439  0F 83 67 F7 FF FF               jae 0x140290ba6
0029143F  49 8B CD                        mov rcx, r13
00291442  E8 7D F9 02 00                  call 0x1402c0dc4
00291447  48 85 DB                        test rbx, rbx
0029144A  74 0B                           je 0x140291457
0029144C  48 8B D3                        mov rdx, rbx
0029144F  49 8B CD                        mov rcx, r13
00291452  E8 69 5A F8 FF                  call 0x140216ec0
00291457  33 C0                           xor eax, eax
00291459  E9 7D FC FF FF                  jmp 0x1402910db
0029145E  E8 35 A5 09 00                  call 0x14032b998
00291463  48 85 C0                        test rax, rax
00291466  0F 84 92 FB FF FF               je 0x140290ffe
0029146C  48 8B 80 08 05 00 00            mov rax, qword ptr [rax + 0x508]
00291473  48 85 C0                        test rax, rax
00291476  0F 84 82 FB FF FF               je 0x140290ffe
0029147C  49 C1 E8 03                     shr r8, 3
00291480  41 81 E0 FF 01 00 00            and r8d, 0x1ff
00291487  4A 8B 04 C0                     mov rax, qword ptr [rax + r8*8]
0029148B  A8 20                           test al, 0x20
0029148D  74 04                           je 0x140291493
0029148F  48 83 CA 20                     or rdx, 0x20
00291493  48 8B CA                        mov rcx, rdx
00291496  44 89 54 24 24                  mov dword ptr [rsp + 0x24], r10d
0029149B  48 83 CA 42                     or rdx, 0x42
0029149F  A8 42                           test al, 0x42
002914A1  48 0F 44 D1                     cmove rdx, rcx
002914A5  E9 54 FB FF FF                  jmp 0x140290ffe
002914AA  E8 E9 A4 09 00                  call 0x14032b998
002914AF  48 85 C0                        test rax, rax
002914B2  0F 84 65 F8 FF FF               je 0x140290d1d
002914B8  48 8B 88 08 05 00 00            mov rcx, qword ptr [rax + 0x508]
002914BF  48 85 C9                        test rcx, rcx
002914C2  0F 84 55 F8 FF FF               je 0x140290d1d
002914C8  49 8B C0                        mov rax, r8
002914CB  48 C1 E8 03                     shr rax, 3
002914CF  25 FF 01 00 00                  and eax, 0x1ff
002914D4  48 8B 04 C1                     mov rax, qword ptr [rcx + rax*8]
002914D8  A8 20                           test al, 0x20
002914DA  74 04                           je 0x1402914e0
002914DC  48 83 CA 20                     or rdx, 0x20
002914E0  48 8B CA                        mov rcx, rdx
002914E3  44 89 7C 24 24                  mov dword ptr [rsp + 0x24], r15d
002914E8  48 83 CA 42                     or rdx, 0x42
002914EC  A8 42                           test al, 0x42
002914EE  48 0F 44 D1                     cmove rdx, rcx
002914F2  E9 26 F8 FF FF                  jmp 0x140290d1d
002914F7  41 8B 85 B8 00 00 00            mov eax, dword ptr [r13 + 0xb8]
002914FE  A8 0F                           test al, 0xf
00291500  0F 85 02 02 00 00               jne 0x140291708
00291506  49 83 BD 70 02 00 00 00         cmp qword ptr [r13 + 0x270], 0
0029150E  0F 85 13 02 00 00               jne 0x140291727
00291514  40 84 ED                        test bpl, bpl
00291517  0F 84 6B FC FF FF               je 0x140291188
0029151D  45 32 E4                        xor r12b, r12b
00291520  44 88 64 24 20                  mov byte ptr [rsp + 0x20], r12b
00291525  E9 FC F7 FF FF                  jmp 0x140290d26
0029152A  85 C0                           test eax, eax
0029152C  0F 89 62 F6 FF FF               jns 0x140290b94
00291532  B2 FF                           mov dl, 0xff
00291534  E8 47 0E 0D 00                  call 0x140362380
00291539  E9 63 F6 FF FF                  jmp 0x140290ba1
0029153E  0F B6 C3                        movzx eax, bl
00291541  24 21                           and al, 0x21
00291543  3C 01                           cmp al, 1
00291545  0F 85 67 F8 FF FF               jne 0x140290db2
0029154B  48 8B C2                        mov rax, rdx
0029154E  49 03 C4                        add rax, r12
00291551  4C 3B F0                        cmp r14, rax
00291554  0F 82 58 F8 FF FF               jb 0x140290db2
0029155A  41 B8 80 00 00 00               mov r8d, 0x80
00291560  48 8B D3                        mov rdx, rbx
00291563  49 8B CE                        mov rcx, r14
00291566  E8 15 18 00 00                  call 0x140292d80
0029156B  48 B9 FF FF FF FF FF FF FF 80   movabs rcx, 0x80ffffffffffffff
00291575  48 BA 00 00 00 00 80 F6 FF FF   movabs rdx, 0xfffff68000000000
0029157F  E9 2E F8 FF FF                  jmp 0x140290db2
00291584  41 0F B6 C4                     movzx eax, r12b
00291588  F0 49 FF 44 C5 28               lock inc qword ptr [r13 + rax*8 + 0x28]
0029158E  41 80 FC 07                     cmp r12b, 7
00291592  0F 85 EB FB FF FF               jne 0x140291183
00291598  49 8B 55 60                     mov rdx, qword ptr [r13 + 0x60]
0029159C  41 0F B7 8D AE 00 00 00         movzx ecx, word ptr [r13 + 0xae]
002915A4  48 8B 05 DD EA B9 00            mov rax, qword ptr [rip + 0xb9eadd]
002915AB  4C 8B 04 C8                     mov r8, qword ptr [rax + rcx*8]
002915AF  49 8B 98 C0 44 00 00            mov rbx, qword ptr [r8 + 0x44c0]
002915B6  48 3B 53 38                     cmp rdx, qword ptr [rbx + 0x38]
002915BA  0F 82 C3 FB FF FF               jb 0x140291183
002915C0  49 83 7D 18 00                  cmp qword ptr [r13 + 0x18], 0
002915C5  49 8D 7D 18                     lea rdi, [r13 + 0x18]
002915C9  0F 84 B4 FB FF FF               je 0x140291183
002915CF  4D 8D B0 C8 44 00 00            lea r14, [r8 + 0x44c8]
002915D6  49 39 3E                        cmp qword ptr [r14], rdi
002915D9  0F 84 A4 FB FF FF               je 0x140291183
002915DF  48 8D 0D DA 5E BA 00            lea rcx, [rip + 0xba5eda]
002915E6  E8 95 78 FB FF                  call 0x140248e80
002915EB  80 7B 35 00                     cmp byte ptr [rbx + 0x35], 0
002915EF  0F 85 3A 02 00 00               jne 0x14029182f
002915F5  48 8B 07                        mov rax, qword ptr [rdi]
002915F8  48 85 C0                        test rax, rax
002915FB  0F 84 2E 02 00 00               je 0x14029182f
00291601  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
00291605  48 39 78 08                     cmp qword ptr [rax + 8], rdi
00291609  0F 85 29 FC FF FF               jne 0x140291238
0029160F  48 39 39                        cmp qword ptr [rcx], rdi
00291612  0F 85 20 FC FF FF               jne 0x140291238
00291618  48 89 01                        mov qword ptr [rcx], rax
0029161B  48 89 48 08                     mov qword ptr [rax + 8], rcx
0029161F  49 8D 4D 18                     lea rcx, [r13 + 0x18]
00291623  49 8B 06                        mov rax, qword ptr [r14]
00291626  4C 39 70 08                     cmp qword ptr [rax + 8], r14
0029162A  0F 85 08 FC FF FF               jne 0x140291238
00291630  48 89 01                        mov qword ptr [rcx], rax
00291633  4C 89 77 08                     mov qword ptr [rdi + 8], r14
00291637  48 89 48 08                     mov qword ptr [rax + 8], rcx
0029163B  49 89 0E                        mov qword ptr [r14], rcx
0029163E  48 8D 0D 7B 5E BA 00            lea rcx, [rip + 0xba5e7b]
00291645  E8 96 81 FB FF                  call 0x1402497e0
0029164A  E9 34 FB FF FF                  jmp 0x140291183
0029164F  49 8B CD                        mov rcx, r13
00291652  E8 69 58 F8 FF                  call 0x140216ec0
00291657  E9 7A FA FF FF                  jmp 0x1402910d6
0029165C  4C 8B 4C 24 30                  mov r9, qword ptr [rsp + 0x30]
00291661  44 8B 7C 24 24                  mov r15d, dword ptr [rsp + 0x24]
00291666  0F 85 21 FB FF FF               jne 0x14029118d
0029166C  F0 49 FF 41 20                  lock inc qword ptr [r9 + 0x20]
00291671  E9 17 FB FF FF                  jmp 0x14029118d
00291676  48 B8 FF FF FF FF FF F6 FF FF   movabs rax, 0xfffff6ffffffffff
00291680  48 3B D0                        cmp rdx, rax
00291683  0F 87 15 F4 FF FF               ja 0x140290a9e
00291689  41 8B 85 B8 00 00 00            mov eax, dword ptr [r13 + 0xb8]
00291690  45 33 F6                        xor r14d, r14d
00291693  44 89 74 24 28                  mov dword ptr [rsp + 0x28], r14d
00291698  A8 0F                           test al, 0xf
0029169A  0F 85 B8 01 00 00               jne 0x140291858
002916A0  48 8B D7                        mov rdx, rdi
002916A3  49 8B CD                        mov rcx, r13
002916A6  E8 E5 D1 FA FF                  call 0x14023e890
002916AB  44 0F B6 8C 24 B8 00 00 00      movzx r9d, byte ptr [rsp + 0xb8]
002916B4  48 8B DF                        mov rbx, rdi
002916B7  48 89 5C 24 40                  mov qword ptr [rsp + 0x40], rbx
002916BC  E9 E8 F3 FF FF                  jmp 0x140290aa9
002916C1  49 8B CD                        mov rcx, r13
002916C4  C7 44 24 2C 01 00 00 00         mov dword ptr [rsp + 0x2c], 1
002916CC  E8 2B F6 02 00                  call 0x1402c0cfc
002916D1  E9 CB F4 FF FF                  jmp 0x140290ba1
002916D6  48 8B CF                        mov rcx, rdi
002916D9  E8 C2 11 FF FF                  call 0x1402828a0
002916DE  48 B9 FF FF FF FF FF 00 00 00   movabs rcx, 0xffffffffff
002916E8  48 C1 E8 0C                     shr rax, 0xc
002916EC  48 23 C1                        and rax, rcx
002916EF  48 8D 0C 40                     lea rcx, [rax + rax*2]
002916F3  48 03 C9                        add rcx, rcx
002916F6  48 8B C5                        mov rax, rbp
002916F9  48 8B 04 C8                     mov rax, qword ptr [rax + rcx*8]
002916FD  48 C1 E8 2A                     shr rax, 0x2a
00291701  24 07                           and al, 7
00291703  E9 2B F4 FF FF                  jmp 0x140290b33
00291708  4C 85 15 79 53 D3 00            test qword ptr [rip + 0xd35379], r10
0029170F  0F 84 FF FD FF FF               je 0x140291514
00291715  41 8B 85 B8 00 00 00            mov eax, dword ptr [r13 + 0xb8]
0029171C  C1 E8 08                        shr eax, 8
0029171F  A8 08                           test al, 8
00291721  0F 84 ED FD FF FF               je 0x140291514
00291727  41 8B 85 B8 00 00 00            mov eax, dword ptr [r13 + 0xb8]
0029172E  A8 0F                           test al, 0xf
00291730  0F 84 5B 01 00 00               je 0x140291891
00291736  48 B8 FF FF FF FF FF 00 00 00   movabs rax, 0xffffffffff
00291740  48 C1 EA 0C                     shr rdx, 0xc
00291744  48 23 D0                        and rdx, rax
00291747  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
00291751  48 8D 0C 52                     lea rcx, [rdx + rdx*2]
00291755  48 C1 E1 04                     shl rcx, 4
00291759  48 8B C0                        mov rax, rax
0029175C  45 33 C0                        xor r8d, r8d
0029175F  48 03 C8                        add rcx, rax
00291762  41 8D 50 02                     lea edx, [r8 + 2]
00291766  E8 B5 3C FF FF                  call 0x140285420
0029176B  A8 41                           test al, 0x41
0029176D  0F 85 B3 F5 FF FF               jne 0x140290d26
00291773  E9 9C FD FF FF                  jmp 0x140291514
00291778  45 33 C0                        xor r8d, r8d
0029177B  49 8B D1                        mov rdx, r9
0029177E  49 8B CD                        mov rcx, r13
00291781  E8 5A BD 17 00                  call 0x14040d4e0
00291786  41 BF 01 00 00 00               mov r15d, 1
0029178C  E9 DE F7 FF FF                  jmp 0x140290f6f
00291791  41 BF 01 00 00 00               mov r15d, 1
00291797  44 89 7C 24 24                  mov dword ptr [rsp + 0x24], r15d
0029179C  F0 49 FF 49 20                  lock dec qword ptr [r9 + 0x20]
002917A1  E9 26 F5 FF FF                  jmp 0x140290ccc
002917A6  48 89 01                        mov qword ptr [rcx], rax
002917A9  48 81 C3 C8 44 00 00            add rbx, 0x44c8
002917B0  48 89 48 08                     mov qword ptr [rax + 8], rcx
002917B4  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
002917B8  48 39 18                        cmp qword ptr [rax], rbx
002917BB  0F 85 77 FA FF FF               jne 0x140291238
002917C1  49 89 1E                        mov qword ptr [r14], rbx
002917C4  48 8D 0D F5 5C BA 00            lea rcx, [rip + 0xba5cf5]
002917CB  49 89 46 08                     mov qword ptr [r14 + 8], rax
002917CF  4C 89 30                        mov qword ptr [rax], r14
002917D2  4C 89 73 08                     mov qword ptr [rbx + 8], r14
002917D6  E8 05 80 FB FF                  call 0x1402497e0
002917DB  E9 A3 F7 FF FF                  jmp 0x140290f83
002917E0  49 8B CD                        mov rcx, r13
002917E3  E8 DC F5 02 00                  call 0x1402c0dc4
002917E8  E9 DB F8 FF FF                  jmp 0x1402910c8
002917ED  48 8D 0D CC 5C BA 00            lea rcx, [rip + 0xba5ccc]
002917F4  C6 47 36 01                     mov byte ptr [rdi + 0x36], 1
002917F8  E8 E3 7F FB FF                  call 0x1402497e0
002917FD  E9 81 F7 FF FF                  jmp 0x140290f83
00291802  C6 47 36 01                     mov byte ptr [rdi + 0x36], 1
00291806  48 8D 0D B3 5C BA 00            lea rcx, [rip + 0xba5cb3]
0029180D  E8 CE 7F FB FF                  call 0x1402497e0
00291812  E9 6C F9 FF FF                  jmp 0x140291183
00291817  49 8D AD 00 01 00 00            lea rbp, [r13 + 0x100]
0029181E  E9 8C F8 FF FF                  jmp 0x1402910af
00291823  49 8D 8D 00 01 00 00            lea rcx, [r13 + 0x100]
0029182A  E9 40 F3 FF FF                  jmp 0x140290b6f
0029182F  C6 43 36 01                     mov byte ptr [rbx + 0x36], 1
00291833  EB D1                           jmp 0x140291806
00291835  8B 05 1D C6 C7 00               mov eax, dword ptr [rip + 0xc7c61d]
0029183B  85 C0                           test eax, eax
0029183D  0F 85 79 F8 FF FF               jne 0x1402910bc
00291843  48 8B 94 24 98 00 00 00         mov rdx, qword ptr [rsp + 0x98]
0029184B  48 8B CD                        mov rcx, rbp
0029184E  E8 F5 F6 05 00                  call 0x1402f0f48
00291853  E9 70 F8 FF FF                  jmp 0x1402910c8
00291858  41 BF 01 00 00 00               mov r15d, 1
0029185E  44 89 7C 24 24                  mov dword ptr [rsp + 0x24], r15d
00291863  E9 41 F2 FF FF                  jmp 0x140290aa9
00291868  48 8B 07                        mov rax, qword ptr [rdi]
0029186B  41 0F B6 D4                     movzx edx, r12b
0029186F  48 C1 E2 2A                     shl rdx, 0x2a
00291873  48 8B CA                        mov rcx, rdx
00291876  48 33 C8                        xor rcx, rax
00291879  48 B8 FF FF FF FF FF E3 FF FF   movabs rax, 0xffffe3ffffffffff
00291883  48 23 C8                        and rcx, rax
00291886  48 33 CA                        xor rcx, rdx
00291889  48 89 0F                        mov qword ptr [rdi], rcx
0029188C  E9 3C F5 FF FF                  jmp 0x140290dcd
00291891  48 B8 FF FF FE FF FF 7F 00 00   movabs rax, 0x7ffffffeffff
0029189B  4C 3B F0                        cmp r14, rax
0029189E  0F 87 70 FC FF FF               ja 0x140291514
002918A4  E9 7D F4 FF FF                  jmp 0x140290d26
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiSetVaAgeList(__int64 a1, __int64 a2, int a3, unsigned __int8 a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned int v_stack_m6C;
    unsigned int v_stack_m70;
    unsigned int v_stack_m74;
    unsigned __int8 v_stack_m78;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p18;
    unsigned __int8 v_stack_p20;
    unsigned int v_stack_p24;
    unsigned int v_stack_p28;
    unsigned int v_stack_p2C;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p8;
    unsigned __int64 v_stack_p98;
    unsigned __int64 v_stack_pA8;
    unsigned int v_stack_pB0;
    unsigned __int8 v_stack_pB8;

    v_stack_p20 = a4;
    v_stack_p18 = a3;
    v_stack_p10 = a2;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (88);
    v_rdi = (a2) >> (9);
    v_rdi = (v_rdi) & (result);
    v_rsi = 0;
    v_rdi = (v_rdi) + (a1);
    v_rbx = 0;
    v_r15 = 0;
    v_stack_m68 = *(unsigned __int64 *)(a1 + 16);
    v_stack_m60 = v_rdi;
    v_stack_m58 = 0;
    v_stack_m6C = 0;
    v_stack_m74 = 0;
    if (a2 >= a1) goto loc_00291676;
loc_00290A9E:
    v_stack_m70 = 1;
loc_00290AA9:
    if (a4 == 8) goto loc_00291415;
    v_rbx = 0;
    if ((unsigned int)((unsigned int)(a3)) == 0) goto loc_00290B52;
loc_00290AE3:
    if (1 == 0) goto loc_002916D6;
    if (v_rdi < a1) goto loc_00290B1B;
    if (v_rdi > 0) goto loc_00290B1B;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rdi))) & (1)) == 0) goto loc_00290B1B;
    a1 = ((((unsigned __int8)(*(unsigned __int64 *)(v_rdi))) & (66)) != 0) ? 1 : 0;
    result = ((((unsigned __int8)(*(unsigned __int64 *)(v_rdi))) & (32)) != 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) == 0) goto loc_0029123F;
loc_00290B1B:
    v_rsi = (*(unsigned __int64 *)(v_rdi)) >> (60);
    v_rsi = (unsigned __int8)((v_rsi) & (7));
    result = (*(unsigned __int64 *)(v_rdi)) >> (56);
    v_rsi = (unsigned __int8)((v_rsi) << (4));
    result = (unsigned __int8)((result) & (15));
    v_rsi = (unsigned __int8)((v_rsi) | ((unsigned __int8)(result)));
loc_00290B33:
    if (((unsigned __int8)(result)) == 8) goto loc_00290B3E;
    v_rbx = (unsigned int)((v_rbx) + 1);
    if (((unsigned int)(v_rbx)) < ((unsigned int)((unsigned int)(a3)))) goto loc_00290AE3;
loc_00290B3E:
loc_00290B52:
    if (((unsigned int)(v_rbx)) != ((unsigned int)((unsigned int)(a3)))) goto loc_002916C1;
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(v_stack_p8 + 184))) & (15));
    if (((unsigned __int8)(result)) != 1) goto loc_00291823;
loc_00290B6F:
    if (((*(unsigned __int8 *)(v_rip + 13852560)) & (33)) == 0) goto loc_00290B8B;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13095642))) != 0) goto loc_00290B8B;
    result = ExpAcquireSpinLockSharedAtDpcLevelInstrumented(v_rip + 12221747, 255, a3, a4);
    goto loc_00290BA1;
loc_00290B8B:
loc_00290B94:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13095642))) != 0) goto loc_0029152A;
loc_00290BA1:
loc_00290BA6:
    if ((unsigned int)((unsigned int)(a3)) == 0) goto loc_00291093;
loc_00290BAF:
    if (v_rdi < v_rbx) goto loc_00290BF9;
    if (v_rdi > v_r11) goto loc_00290BF9;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rdi))) & (1)) == 0) goto loc_00290BF9;
    a1 = ((((unsigned __int8)(*(unsigned __int64 *)(v_rdi))) & (66)) != 0) ? 1 : 0;
    result = ((((unsigned __int8)(*(unsigned __int64 *)(v_rdi))) & (32)) != 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) == 0) goto loc_00291287;
loc_00290BF9:
    a2 = (*(unsigned __int64 *)(v_rdi)) >> (12);
    a2 = (a2) & (result);
    v_rdi = (a2 + a2 * 2) << (4);
    v_rdi = (v_rdi) + (result);
    if (1 == 0) goto loc_00290CB3;
    a3 = (v_stack_p10) >> (9);
    a3 = (a3) & (result);
    a3 = (a3) + (result);
    if (a3 < v_rbx) goto loc_00290C83;
    if (a3 > v_r11) goto loc_00290C83;
    if ((((unsigned __int8)(*(unsigned __int64 *)(a3))) & (1)) == 0) goto loc_00290C83;
    a1 = ((((unsigned __int8)(*(unsigned __int64 *)(a3))) & (66)) != 0) ? 1 : 0;
    result = ((((unsigned __int8)(*(unsigned __int64 *)(a3))) & (32)) != 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) == 0) goto loc_00291382;
loc_00290C83:
    a2 = (*(unsigned __int64 *)(a3)) >> (60);
    a2 = (unsigned __int8)((a2) & (7));
    result = (*(unsigned __int64 *)(a3)) >> (56);
    result = (unsigned __int8)((result) & (15));
    a2 = (unsigned __int8)((a2) << (4));
    a2 = (unsigned __int8)((a2) | ((unsigned __int8)(result)));
    if (((unsigned __int8)(result)) == 8) goto loc_00291791;
    v_r15 = 0;
    v_stack_m74 = 0;
    goto loc_00290CCC;
loc_00290CB3:
    v_rbp = (*(unsigned __int64 *)(v_rdi)) >> (42);
    v_rbp = (unsigned __int8)((v_rbp) & (7));
    if (((unsigned __int8)(v_rbp)) == 8) goto loc_0029179C;
loc_00290CCC:
    v_stack_m78 = (unsigned __int8)(v_stack_p20);
    result = (unsigned __int8)((v_stack_p20) - 1);
    if (((unsigned __int8)(result)) > 5) goto loc_00290D26;
    if (v_stack_m60 < result) goto loc_00290D1D;
    if (v_stack_m60 > v_r11) goto loc_00290D1D;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_m60))) & (1)) == 0) goto loc_00290D1D;
    a1 = ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_m60))) & (66)) != 0) ? 1 : 0;
    result = ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_m60))) & (32)) != 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) == 0) goto loc_002914AA;
loc_00290D1D:
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_m60))) & (32)) != 0) goto loc_002914F7;
loc_00290D26:
    if (v_stack_m70 == 0) goto loc_00291868;
    v_r14 = (v_stack_p10) >> (9);
    v_rsi = (unsigned __int8)(((unsigned __int8)((unsigned __int8)((unsigned __int8)(a2)))) ^ ((unsigned __int8)((unsigned __int8)(v_stack_p20))));
    v_rsi = (unsigned __int8)((v_rsi) & (15));
    v_rsi = (unsigned __int8)((v_rsi) ^ ((unsigned __int8)((unsigned __int8)((unsigned __int8)(a2)))));
    v_r14 = (v_r14) & (result);
    v_r14 = (v_r14) + (*(unsigned __int64 *)(v_stack_m60));
loc_00290D80:
    result = ((unsigned __int8)(v_rsi)) << (56);
    v_rbx = (*(unsigned __int64 *)(v_r14)) ^ (result);
    v_rbx = (v_rbx) & (a1);
    v_rbx = (v_rbx) ^ (result);
    if (((*(unsigned __int64 *)(v_rip + 13851882)) & (0x2000000ULL)) != 0) {
    }
    if (condition_is_below) goto loc_0029153E;
loc_00290DB2:
    if (((*(unsigned __int64 *)(v_rip + 13851882)) & (0x2000000ULL)) != 0) goto loc_00290D80;
loc_00290DCD:
    v_r15 = 0;
    if ((unsigned int)((unsigned int)(v_stack_m74)) != 0) goto loc_00290F88;
    a3 = (v_stack_p10) >> (18);
    a3 = (unsigned int)((a3) & (0x3FFFFFF8ULL));
    a3 = (a3) + (*(unsigned __int64 *)(v_r14));
    if (a3 < (*(unsigned __int64 *)(v_r14))) goto loc_00290E44;
    if (a3 > (*(unsigned __int64 *)(v_r14))) goto loc_00290E44;
    if ((((unsigned __int8)(*(unsigned __int64 *)(a3))) & (1)) == 0) goto loc_00290E44;
    a1 = ((((unsigned __int8)(*(unsigned __int64 *)(a3))) & (66)) != 0) ? 1 : 0;
    result = ((((unsigned __int8)(*(unsigned __int64 *)(a3))) & (32)) != 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) == 0) goto loc_002913C9;
loc_00290E44:
    a2 = (*(unsigned __int64 *)(a3)) >> (12);
    a2 = (a2) & (result);
    v_rdi = (a2 + a2 * 2) << (4);
    v_rdi = (v_rdi) + (result);
    a3 = (*(unsigned __int64 *)(v_rdi)) >> (45);
    result = (*(unsigned __int64 *)(v_rdi)) >> (55);
    a3 = (unsigned int)((a3) & (0x3FFULL));
    result = (unsigned __int8)((result) & (7));
    if (((unsigned __int8)(v_rbp)) == ((unsigned __int8)(result))) goto loc_00290EDC;
    if (((unsigned __int8)(v_rbp)) <= ((unsigned __int8)(result))) goto loc_00290F6F;
    result = (unsigned int)(*(unsigned int *)(v_rdi + 36));
    if (((unsigned __int8)(v_rbp)) < ((unsigned __int8)(result))) {
        a3 = 0;
        a2 = v_rdi;
        a1 = v_stack_p8;
        result = MiRemoveActivePageTableLinks(a1, a2, a3, v_stack_p10);
    }
    result = ((unsigned __int8)(v_rbp)) << (55);
    a1 = (result) ^ (*(unsigned __int64 *)(v_rdi));
    a1 = (a1) & (a2);
    a1 = (a1) ^ (result);
    a1 = (a1) | (result);
    *(unsigned __int64 *)(v_rdi) = a1;
    goto loc_00290F5D;
loc_00290EDC:
    a2 = ((unsigned int)((unsigned int)(a3 - 1))) << (45);
    result = (*(unsigned __int64 *)(v_rdi)) ^ (a2);
    v_r14 = (unsigned int)(((unsigned int)((unsigned int)(a3 - 1))) & (0x3FFULL));
    result = (result) & (a3 - 1);
    result = (result) ^ (a2);
    *(unsigned __int64 *)(v_rdi) = result;
    if (a3 - 1 == 0) goto loc_00291778;
    if (condition_is_below) goto loc_00290F6F;
    result = (unsigned int)(*(unsigned int *)(v_rdi + 36));
    if (!(condition_is_above_or_equal)) {
        a3 = 0;
        a2 = v_rdi;
        a1 = v_stack_p8;
        result = MiRemoveActivePageTableLinks(a1, a2, a3, v_stack_p10);
    }
    result = (unsigned int)((v_rbp) & (7));
    v_rbx = (*(unsigned __int64 *)(v_rdi)) & (a1);
    result = (result) << (10);
    result = (result) | (v_r14);
    result = (result) << (45);
    result = (result) | (v_rbx);
    *(unsigned __int64 *)(v_rdi) = result;
loc_00290F5D:
    a4 = 0;
    result = MiInsertActivePageTableLinksTail(v_stack_p8, v_rdi, (unsigned __int8)(v_rbp), a4);
loc_00290F6F:
    if (((unsigned __int8)(v_rbp)) == 7) goto loc_002911BF;
loc_00290F83:
loc_00290F88:
    if (((unsigned __int8)(v_stack_m78)) >= 8) goto loc_0029165C;
    if (0 != 0) goto loc_00291584;
    a3 = (v_stack_p10) >> (18);
    a3 = (unsigned int)((a3) & (0x3FFFFFF8ULL));
    a3 = (a3) + ((unsigned __int8)(v_rbp));
    if (a3 < ((unsigned __int8)(v_rbp))) goto loc_00290FFE;
    if (a3 > ((unsigned __int8)(v_rbp))) goto loc_00290FFE;
    if ((((unsigned __int8)(*(unsigned __int64 *)(a3))) & (1)) == 0) goto loc_00290FFE;
    a1 = ((((unsigned __int8)(*(unsigned __int64 *)(a3))) & (66)) != 0) ? 1 : 0;
    result = ((((unsigned __int8)(*(unsigned __int64 *)(a3))) & (32)) != 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) == 0) goto loc_0029145E;
loc_00290FFE:
    a2 = (*(unsigned __int64 *)(a3)) >> (12);
    a2 = (a2) & (result);
    v_rdi = (a2 + a2 * 2) << (4);
    v_rdi = (v_rdi) + (result);
    a1 = (*(unsigned __int64 *)(v_rdi)) >> (45);
    result = (*(unsigned __int64 *)(v_rdi)) >> (55);
    a1 = (unsigned int)((a1) & (0x3FFULL));
    result = (unsigned __int8)((result) & (7));
    if (((unsigned __int8)(v_stack_m78)) == ((unsigned __int8)(result))) goto loc_002910ED;
    if (((unsigned __int8)(v_stack_m78)) <= ((unsigned __int8)(result))) goto loc_0029116F;
    result = (unsigned int)(*(unsigned int *)(v_rdi + 36));
    if (((unsigned __int8)(v_stack_m78)) < ((unsigned __int8)(result))) {
        a3 = 0;
        a2 = v_rdi;
        a1 = v_stack_p8;
        result = MiRemoveActivePageTableLinks(a1, a2, a3, a4);
    }
    result = (unsigned int)((v_stack_m78) & (7));
    result = (result) << (55);
    result = (result) | (a1);
    goto loc_00291154;
loc_0029108C:
loc_00291093:
    if (v_stack_m6C != 0) goto loc_002917E0;
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(v_stack_p8 + 184))) & (15));
    if (((unsigned __int8)(result)) != 1) goto loc_00291817;
loc_002910AF:
    if (((*(unsigned __int8 *)(v_rip + 13851216)) & (1)) != 0) goto loc_00291835;
loc_002910BC:
loc_002910C8:
    if (v_stack_m58 != 0) goto loc_0029164F;
loc_002910D6:
loc_002910DB:
    v_rsp = (v_rsp) + (88);
    return 1;
loc_002910ED:
    a1 = (unsigned int)((a1) + 1);
    a2 = ((unsigned int)((unsigned int)(a1))) << (45);
    result = (*(unsigned __int64 *)(v_rdi)) ^ (a2);
    v_rbp = (unsigned int)(((unsigned int)((unsigned int)(a1))) & (0x3FFULL));
    result = (result) & (a1);
    result = (result) ^ (a2);
    *(unsigned __int64 *)(v_rdi) = result;
    if (condition_is_below) goto loc_0029116F;
    result = (unsigned int)(*(unsigned int *)(v_rdi + 36));
    if (!(condition_is_above_or_equal)) {
        a3 = 0;
        a2 = v_rdi;
        a1 = v_stack_p8;
        result = MiRemoveActivePageTableLinks(a1, a2, a3, a4);
    }
    result = (unsigned int)((v_stack_m78) & (7));
    result = (result) << (10);
    result = (result) | (v_rbp);
    result = (result) << (45);
loc_00291154:
    v_rbx = (*(unsigned __int64 *)(v_rdi)) & (a1);
    a4 = 0;
    result = (result) | (v_rbx);
    *(unsigned __int64 *)(v_rdi) = result;
    result = MiInsertActivePageTableLinksTail(v_stack_p8, v_rdi, (unsigned __int8)(v_stack_m78), a4);
loc_0029116F:
    if (((unsigned __int8)(v_stack_m78)) == 7) goto loc_002912CF;
loc_00291183:
loc_00291188:
loc_0029118D:
    v_rdi = (v_stack_p38) + (8);
    v_stack_p38 = v_rdi;
    if (condition_is_equal) goto loc_0029108C;
    goto loc_00290BAF;
loc_002911BF:
    if ((*(unsigned __int64 *)(v_stack_p8 + 96)) >= (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12185270) + *(unsigned __int16 *)(v_stack_p8 + 174) * 8) + 17600) + 56))) goto loc_00290F83;
    if ((*(unsigned __int64 *)(v_stack_p8 + 24)) == 0) goto loc_00290F83;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12185270) + *(unsigned __int16 *)(v_stack_p8 + 174) * 8) + 17616)) == (v_stack_p8 + 24)) goto loc_00290F83;
    result = ExAcquireSpinLockExclusiveAtDpcLevel(v_rip + 12214966, *(unsigned __int64 *)(v_stack_p8 + 96), (unsigned __int8)(v_stack_m78), v_stack_p30);
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12185270) + *(unsigned __int16 *)(v_stack_p8 + 174) * 8) + 17600) + 53)) != 0) goto loc_002917ED;
    if (*(unsigned __int64 *)(v_stack_p8 + 24) == 0) goto loc_002917ED;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + 24) + 8)) != (v_stack_p8 + 24)) goto loc_00291238;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + 24 + 8))) == (v_stack_p8 + 24)) goto loc_002917A6;
loc_00291238:
loc_0029123F:
    result = MiPteHasShadow(3, *(unsigned __int64 *)(v_stack_p8 + 96), (unsigned __int8)(v_stack_m78), v_stack_p30);
    if (result == 0) goto loc_00290B1B;
    if (*(unsigned __int64 *)(result + 1288) == 0) goto loc_00290B1B;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12185270) + *(unsigned __int16 *)(v_stack_p8 + 174) * 8) + 17600)) >> (3);
    result = (unsigned int)((result) & (511));
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 1288) + result * 8))) & (32)) != 0) {
        v_rsi = (v_rsi) | (32);
    }
    v_rsi = (v_rsi) | (66);
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 1288) + result * 8))) & (66)) == 0) { v_rsi = v_rsi; }
    goto loc_00290B1B;
loc_00291287:
    result = MiPteHasShadow(v_rsi, *(unsigned __int64 *)(v_stack_p8 + 96), (unsigned __int8)(v_stack_m78), v_stack_p30);
    if (result == 0) goto loc_00290BF9;
    if (*(unsigned __int64 *)(result + 1288) == 0) goto loc_00290BF9;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12185270) + *(unsigned __int16 *)(v_stack_p8 + 174) * 8) + 17600)) >> (3);
    result = (unsigned int)((result) & (511));
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 1288) + result * 8))) & (32)) != 0) {
        a2 = (*(unsigned __int64 *)(v_stack_p8 + 96)) | (32);
    }
    a2 = (a2) | (66);
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 1288) + result * 8))) & (66)) == 0) { a2 = a2; }
    goto loc_00290BF9;
loc_002912CF:
    if ((*(unsigned __int64 *)(v_stack_p8 + 96)) < (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12184998) + *(unsigned __int16 *)(v_stack_p8 + 174) * 8) + 17600) + 56))) goto loc_00291183;
    if ((*(unsigned __int64 *)(v_stack_p8 + 24)) == 0) goto loc_00291183;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12184998) + *(unsigned __int16 *)(v_stack_p8 + 174) * 8) + 17608)) == (v_stack_p8 + 24)) goto loc_00291183;
    result = ExAcquireSpinLockExclusiveAtDpcLevel(v_rip + 12214691, *(unsigned __int64 *)(v_stack_p8 + 96), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12184998) + *(unsigned __int16 *)(v_stack_p8 + 174) * 8), v_stack_p30);
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12184998) + *(unsigned __int16 *)(v_stack_p8 + 174) * 8) + 17600) + 53)) != 0) goto loc_00291802;
    if (*(unsigned __int64 *)(v_stack_p8 + 24) == 0) goto loc_00291802;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + 24) + 8)) != (v_stack_p8 + 24)) goto loc_00291238;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + 24 + 8))) != (v_stack_p8 + 24)) goto loc_00291238;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + 24 + 8)) = *(unsigned __int64 *)(v_stack_p8 + 24);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + 24) + 8) = *(unsigned __int64 *)(v_stack_p8 + 24 + 8);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12184998) + *(unsigned __int16 *)(v_stack_p8 + 174) * 8) + 17608) + 8)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12184998) + *(unsigned __int16 *)(v_stack_p8 + 174) * 8) + 17608)) goto loc_00291238;
    *(unsigned __int64 *)(v_stack_p8 + 24) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12184998) + *(unsigned __int16 *)(v_stack_p8 + 174) * 8) + 17608);
    *(unsigned __int64 *)(v_stack_p8 + 24 + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12184998) + *(unsigned __int16 *)(v_stack_p8 + 174) * 8) + 17608;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12184998) + *(unsigned __int16 *)(v_stack_p8 + 174) * 8) + 17608) + 8) = v_stack_p8 + 24;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12184998) + *(unsigned __int16 *)(v_stack_p8 + 174) * 8) + 17608) = v_stack_p8 + 24;
    result = ExReleaseSpinLockExclusiveFromDpcLevel(v_rip + 12214611, *(unsigned __int64 *)(v_stack_p8 + 96), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12184998) + *(unsigned __int16 *)(v_stack_p8 + 174) * 8), v_stack_p30);
    goto loc_00291183;
loc_00291382:
    result = MiPteHasShadow(v_rip + 12214611, *(unsigned __int64 *)(v_stack_p8 + 96), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12184998) + *(unsigned __int16 *)(v_stack_p8 + 174) * 8), v_stack_p30);
    if (result == 0) goto loc_00290C83;
    if (*(unsigned __int64 *)(result + 1288) == 0) goto loc_00290C83;
    a3 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12184998) + *(unsigned __int16 *)(v_stack_p8 + 174) * 8)) >> (3);
    a3 = (unsigned int)((a3) & (511));
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 1288) + a3 * 8))) & (32)) != 0) {
        a2 = (*(unsigned __int64 *)(v_stack_p8 + 96)) | (32);
    }
    a2 = (a2) | (66);
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 1288) + a3 * 8))) & (66)) == 0) { a2 = a2; }
    goto loc_00290C83;
loc_002913C9:
    result = MiPteHasShadow(a2, a2, a3, v_stack_p30);
    if (result == 0) goto loc_00290E44;
    if (*(unsigned __int64 *)(result + 1288) == 0) goto loc_00290E44;
    a3 = (a3) >> (3);
    a3 = (unsigned int)((a3) & (511));
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 1288) + a3 * 8))) & (32)) != 0) {
        a2 = (a2) | (32);
    }
    v_stack_p24 = (unsigned int)((unsigned int)(v_stack_m74));
    a2 = (a2) | (66);
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 1288) + a3 * 8))) & (66)) == 0) { a2 = a2; }
    goto loc_00290E44;
loc_00291415:
    v_stack_p2C = 1;
    result = MiLockWorkingSetCoreExclusive(v_stack_p8, a2, a3, v_stack_p30);
    a1 = (*(unsigned __int64 *)(v_stack_p30 + 32)) + (6);
    a1 = (a1) + (v_stack_m78);
    if ((*(unsigned __int64 *)(v_stack_p8 + 112)) >= a1) goto loc_00290BA6;
    result = MiUnlockWorkingSetCoreExclusive(v_stack_p8, a2, a3, v_stack_p30);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12184998) + *(unsigned __int16 *)(v_stack_p8 + 174) * 8) + 17608 != 0) {
        a2 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12184998) + *(unsigned __int16 *)(v_stack_p8 + 174) * 8) + 17608;
        a1 = v_stack_p8;
        result = MiUnlockPageTable(a1, a2, a3, v_stack_p30);
    }
    result = 0;
    goto loc_002910DB;
loc_0029145E:
    result = MiPteHasShadow(a1, a2, a3, v_stack_p30);
    if (result == 0) goto loc_00290FFE;
    if (*(unsigned __int64 *)(result + 1288) == 0) goto loc_00290FFE;
    a3 = (a3) >> (3);
    a3 = (unsigned int)((a3) & (511));
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 1288) + a3 * 8))) & (32)) != 0) {
        a2 = (a2) | (32);
    }
    v_stack_p24 = (unsigned int)((unsigned int)(v_stack_m74));
    a2 = (a2) | (66);
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 1288) + a3 * 8))) & (66)) == 0) { a2 = a2; }
    goto loc_00290FFE;
loc_002914AA:
    result = MiPteHasShadow(a2, a2, a3, v_stack_p30);
    if (result == 0) goto loc_00290D1D;
    if (*(unsigned __int64 *)(result + 1288) == 0) goto loc_00290D1D;
    result = (a3) >> (3);
    result = (unsigned int)((result) & (511));
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 1288) + result * 8))) & (32)) != 0) {
        a2 = (a2) | (32);
    }
    v_stack_p24 = (unsigned int)((unsigned int)(v_stack_p24));
    a2 = (a2) | (66);
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 1288) + result * 8))) & (66)) == 0) { a2 = a2; }
    goto loc_00290D1D;
loc_002914F7:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p8 + 184)))) & (15)) != 0) goto loc_00291708;
    if ((*(unsigned __int64 *)(v_stack_p8 + 624)) != 0) goto loc_00291727;
loc_00291514:
    if ((unsigned __int8)(v_rbp) == 0) goto loc_00291188;
    v_r12 = 0;
    v_stack_p20 = 0;
    goto loc_00290D26;
loc_0029152A:
    if (!sign_flag) goto loc_00290B94;
    result = ExpWaitForSpinLockSharedAndAcquire(a2, 255, a3, v_stack_p30);
    goto loc_00290BA1;
loc_0029153E:
    result = (unsigned __int8)(((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12184998) + *(unsigned __int16 *)(v_stack_p8 + 174) * 8) + 17608)) & (33));
    if (((unsigned __int8)(result)) != 1) goto loc_00290DB2;
    result = (255) + (0);
    if ((v_stack_p8 + 24) < result) goto loc_00290DB2;
    result = MiCheckLinearProtectedPteAccessedBit(v_stack_p8 + 24, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12184998) + *(unsigned __int16 *)(v_stack_p8 + 174) * 8) + 17608, 128, v_stack_p30);
    goto loc_00290DB2;
loc_00291584:
    if (0 != 7) goto loc_00291183;
    if ((*(unsigned __int64 *)(v_stack_p8 + 96)) < (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12184285) + *(unsigned __int16 *)(v_stack_p8 + 174) * 8) + 17600) + 56))) goto loc_00291183;
    if ((*(unsigned __int64 *)(v_stack_p8 + 24)) == 0) goto loc_00291183;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12184285) + *(unsigned __int16 *)(v_stack_p8 + 174) * 8) + 17608)) == (v_stack_p8 + 24)) goto loc_00291183;
    result = ExAcquireSpinLockExclusiveAtDpcLevel(v_rip + 12213978, *(unsigned __int64 *)(v_stack_p8 + 96), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12184285) + *(unsigned __int16 *)(v_stack_p8 + 174) * 8), v_stack_p30);
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12184285) + *(unsigned __int16 *)(v_stack_p8 + 174) * 8) + 17600) + 53)) != 0) goto loc_0029182F;
    if (*(unsigned __int64 *)(v_stack_p8 + 24) == 0) goto loc_0029182F;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + 24) + 8)) != (v_stack_p8 + 24)) goto loc_00291238;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + 24 + 8))) != (v_stack_p8 + 24)) goto loc_00291238;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + 24 + 8)) = *(unsigned __int64 *)(v_stack_p8 + 24);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + 24) + 8) = *(unsigned __int64 *)(v_stack_p8 + 24 + 8);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12184285) + *(unsigned __int16 *)(v_stack_p8 + 174) * 8) + 17608) + 8)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12184285) + *(unsigned __int16 *)(v_stack_p8 + 174) * 8) + 17608)) goto loc_00291238;
    *(unsigned __int64 *)(v_stack_p8 + 24) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12184285) + *(unsigned __int16 *)(v_stack_p8 + 174) * 8) + 17608);
    *(unsigned __int64 *)(v_stack_p8 + 24 + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12184285) + *(unsigned __int16 *)(v_stack_p8 + 174) * 8) + 17608;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12184285) + *(unsigned __int16 *)(v_stack_p8 + 174) * 8) + 17608) + 8) = v_stack_p8 + 24;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12184285) + *(unsigned __int16 *)(v_stack_p8 + 174) * 8) + 17608) = v_stack_p8 + 24;
    result = ExReleaseSpinLockExclusiveFromDpcLevel(v_rip + 12213883, *(unsigned __int64 *)(v_stack_p8 + 96), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12184285) + *(unsigned __int16 *)(v_stack_p8 + 174) * 8), v_stack_p30);
    goto loc_00291183;
loc_0029164F:
    result = MiUnlockPageTable(v_stack_p8, *(unsigned __int64 *)(v_stack_p8 + 96), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12184285) + *(unsigned __int16 *)(v_stack_p8 + 174) * 8), v_stack_p30);
    goto loc_002910D6;
loc_0029165C:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12184285) + *(unsigned __int16 *)(v_stack_p8 + 174) * 8) + 17608) + 8)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12184285) + *(unsigned __int16 *)(v_stack_p8 + 174) * 8) + 17608)) goto loc_0029118D;
    goto loc_0029118D;
loc_00291676:
    if ((*(unsigned __int64 *)(v_stack_p8 + 96)) > result) goto loc_00290A9E;
    v_r14 = 0;
    v_stack_p28 = 0;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p8 + 184)))) & (15)) != 0) goto loc_00291858;
    result = MiLockNestedPageTable(v_stack_p8, v_stack_p8 + 24, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12184285) + *(unsigned __int16 *)(v_stack_p8 + 174) * 8), v_stack_p30);
    v_stack_p40 = v_stack_p8 + 24;
    goto loc_00290AA9;
loc_002916C1:
    v_stack_p2C = 1;
    result = MiLockWorkingSetCoreExclusive(v_stack_p8, v_stack_p8 + 24, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12184285) + *(unsigned __int16 *)(v_stack_p8 + 174) * 8), v_stack_pB8);
    goto loc_00290BA1;
loc_002916D6:
    result = MI_READ_PTE_LOCK_FREE(v_stack_p8 + 24, v_stack_p8 + 24, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12184285) + *(unsigned __int16 *)(v_stack_p8 + 174) * 8), v_stack_pB8);
    result = (result) >> (12);
    result = (result) & (v_stack_p8 + 24);
    a1 = (result + result * 2) + (result + result * 2);
    result = (*(unsigned __int64 *)(v_rbp + a1 * 8)) >> (42);
    result = (unsigned __int8)((result) & (7));
    goto loc_00290B33;
loc_00291708:
    if (((*(unsigned __int64 *)(v_rip + 13849465)) & ((unsigned int)(v_stack_m74))) == 0) goto loc_00291514;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p8 + 184))) >> (8));
    if ((((unsigned __int8)(result)) & (8)) == 0) goto loc_00291514;
loc_00291727:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p8 + 184)))) & (15)) == 0) goto loc_00291891;
    a2 = (v_stack_p8 + 24) >> (12);
    a2 = (a2) & ((unsigned int)(*(unsigned int *)(v_stack_p8 + 184)));
    a1 = (a2 + a2 * 2) << (4);
    a3 = 0;
    a1 = (a1) + ((unsigned int)(*(unsigned int *)(v_stack_p8 + 184)));
    result = MiGetPagePrivilege(a1, a3 + 2, a3, v_stack_pB8);
    if ((((unsigned __int8)(result)) & (65)) != 0) goto loc_00290D26;
    goto loc_00291514;
loc_00291778:
    a3 = 0;
    result = MiRebuildPageTableAges(v_stack_p8, v_stack_pB8, a3, v_stack_pB8);
    goto loc_00290F6F;
loc_00291791:
    v_stack_p24 = 1;
loc_0029179C:
    goto loc_00290CCC;
loc_002917A6:
    *(unsigned __int64 *)(v_stack_p8) = result;
    v_rbx = (v_stack_p8 + 24) + (0x44C8ULL);
    *(unsigned __int64 *)(result + 8) = v_stack_p8;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 8))) != v_rbx) goto loc_00291238;
    *(unsigned __int64 *)(v_r14) = v_rbx;
    *(unsigned __int64 *)(v_r14 + 8) = *(unsigned __int64 *)(v_rbx + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 8)) = 0;
    *(unsigned __int64 *)(v_rbx + 8) = 0;
    result = ExReleaseSpinLockExclusiveFromDpcLevel(v_rip + 12213493, v_stack_pB8, a3, v_stack_pB8);
    goto loc_00290F83;
loc_002917E0:
    result = MiUnlockWorkingSetCoreExclusive(v_stack_p8, v_stack_pB8, a3, v_stack_pB8);
    goto loc_002910C8;
loc_002917ED:
    *(unsigned __int8 *)(v_stack_p8 + 24 + 54) = 1;
    result = ExReleaseSpinLockExclusiveFromDpcLevel(v_rip + 12213452, v_stack_pB8, a3, v_stack_pB8);
    goto loc_00290F83;
loc_00291802:
    *(unsigned __int8 *)(v_stack_p8 + 24 + 54) = 1;
loc_00291806:
    result = ExReleaseSpinLockExclusiveFromDpcLevel(v_rip + 12213427, v_stack_pB8, a3, v_stack_pB8);
    goto loc_00291183;
loc_00291817:
    goto loc_002910AF;
loc_00291823:
    goto loc_00290B6F;
loc_0029182F:
    *(unsigned __int8 *)(v_rbx + 54) = 1;
    goto loc_00291806;
loc_00291835:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13092381))) != 0) goto loc_002910BC;
    result = ExpReleaseSpinLockSharedFromDpcLevelInstrumented(v_stack_p8 + 256, v_stack_p98, a3, v_stack_pB8);
    goto loc_002910C8;
loc_00291858:
    v_stack_p24 = 1;
    goto loc_00290AA9;
loc_00291868:
    a2 = (0) << (42);
    a1 = (a2) ^ (*(unsigned __int64 *)(v_stack_p8 + 24));
    a1 = (a1) & (*(unsigned __int64 *)(v_stack_p8 + 24));
    a1 = (a1) ^ (a2);
    *(unsigned __int64 *)(v_stack_p8 + 24) = a1;
    goto loc_00290DCD;
loc_00291891:
    if (0 > (*(unsigned __int64 *)(v_stack_p8 + 24))) goto loc_00291514;
    goto loc_00290D26;
}
```

## 5. (Beta) C Style

```c
int64_t MiSetVaAgeList(void *Arg1, int64_t Arg2, int32_t Arg3, uint8_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint32_t v_stack_m6C;
    uint32_t v_stack_m70;
    uint32_t v_stack_m74;
    uint8_t v_stack_m78;
    uint64_t v_stack_p10;
    uint32_t v_stack_p18;
    uint8_t v_stack_p20;
    uint32_t v_stack_p24;
    uint32_t v_stack_p28;
    uint32_t v_stack_p2C;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint64_t v_stack_p8;
    uint64_t v_stack_p98;
    uint64_t v_stack_pA8;
    uint32_t v_stack_pB0;
    uint8_t v_stack_pB8;

    v_stack_p20 = Arg4;
    v_stack_p18 = Arg3;
    v_stack_p10 = Arg2;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (88);
    local_rdi = (Arg2) >> (9);
    local_rdi = (local_rdi) & (result);
    local_rsi = 0;
    local_rdi = (local_rdi) + (Arg1);
    local_rbx = 0;
    local_r15 = 0;
    v_stack_m68 = *(uint64_t *)(arg1 + 0x10);
    v_stack_m60 = local_rdi;
    v_stack_m58 = 0;
    v_stack_m6C = 0;
    v_stack_m74 = 0;
    if (Arg2 >= Arg1) goto loc_00291676;
loc_00290A9E:
    v_stack_m70 = 1;
loc_00290AA9:
    if (Arg4 == 8) goto loc_00291415;
    local_rbx = 0;
    if ((uint32_t)((uint32_t)(Arg3)) == 0) goto loc_00290B52;
loc_00290AE3:
    if (1 == 0) goto loc_002916D6;
    if (local_rdi < Arg1) goto loc_00290B1B;
    if (local_rdi > 0) goto loc_00290B1B;
    if ((((uint8_t)(*(uint64_t *)(local_rdi))) & (1)) == 0) goto loc_00290B1B;
    Arg1 = ((((uint8_t)(*(uint64_t *)(local_rdi))) & (66)) != 0) ? 1 : 0;
    result = ((((uint8_t)(*(uint64_t *)(local_rdi))) & (32)) != 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) == 0) goto loc_0029123F;
loc_00290B1B:
    local_rsi = (*(uint64_t *)(local_rdi)) >> (60);
    local_rsi = (uint8_t)((local_rsi) & (7));
    result = (*(uint64_t *)(local_rdi)) >> (56);
    local_rsi = (uint8_t)((local_rsi) << (4));
    result = (uint8_t)((result) & (15));
    local_rsi = (uint8_t)((local_rsi) | ((uint8_t)(result)));
loc_00290B33:
    if (((uint8_t)(result)) == 8) goto loc_00290B3E;
    local_rbx = (uint32_t)((local_rbx) + 1);
    if (((uint32_t)(local_rbx)) < ((uint32_t)((uint32_t)(Arg3)))) goto loc_00290AE3;
loc_00290B3E:
loc_00290B52:
    if (((uint32_t)(local_rbx)) != ((uint32_t)((uint32_t)(Arg3)))) goto loc_002916C1;
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(v_stack_p8 + 0xB8))) & (15));
    if (((uint8_t)(result)) != 1) goto loc_00291823;
loc_00290B6F:
    if (((*(uint8_t *)(v_rip + 0xD35F90)) & (33)) == 0) goto loc_00290B8B;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC7D2DA))) != 0) goto loc_00290B8B;
    result = ExpAcquireSpinLockSharedAtDpcLevelInstrumented(v_rip + 12221747, 255, Arg3, Arg4);
    goto loc_00290BA1;
loc_00290B8B:
loc_00290B94:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC7D2DA))) != 0) goto loc_0029152A;
loc_00290BA1:
loc_00290BA6:
    if ((uint32_t)((uint32_t)(Arg3)) == 0) goto loc_00291093;
loc_00290BAF:
    if (local_rdi < local_rbx) goto loc_00290BF9;
    if (local_rdi > local_r11) goto loc_00290BF9;
    if ((((uint8_t)(*(uint64_t *)(local_rdi))) & (1)) == 0) goto loc_00290BF9;
    Arg1 = ((((uint8_t)(*(uint64_t *)(local_rdi))) & (66)) != 0) ? 1 : 0;
    result = ((((uint8_t)(*(uint64_t *)(local_rdi))) & (32)) != 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) == 0) goto loc_00291287;
loc_00290BF9:
    Arg2 = (*(uint64_t *)(local_rdi)) >> (12);
    Arg2 = (Arg2) & (result);
    local_rdi = (Arg2 + Arg2 * 2) << (4);
    local_rdi = (local_rdi) + (result);
    if (1 == 0) goto loc_00290CB3;
    Arg3 = (v_stack_p10) >> (9);
    Arg3 = (Arg3) & (result);
    Arg3 = (Arg3) + (result);
    if (Arg3 < local_rbx) goto loc_00290C83;
    if (Arg3 > local_r11) goto loc_00290C83;
    if ((((uint8_t)(*(uint64_t *)(Arg3))) & (1)) == 0) goto loc_00290C83;
    Arg1 = ((((uint8_t)(*(uint64_t *)(Arg3))) & (66)) != 0) ? 1 : 0;
    result = ((((uint8_t)(*(uint64_t *)(Arg3))) & (32)) != 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) == 0) goto loc_00291382;
loc_00290C83:
    Arg2 = (*(uint64_t *)(Arg3)) >> (60);
    Arg2 = (uint8_t)((Arg2) & (7));
    result = (*(uint64_t *)(Arg3)) >> (56);
    result = (uint8_t)((result) & (15));
    Arg2 = (uint8_t)((Arg2) << (4));
    Arg2 = (uint8_t)((Arg2) | ((uint8_t)(result)));
    if (((uint8_t)(result)) == 8) goto loc_00291791;
    local_r15 = 0;
    v_stack_m74 = 0;
    goto loc_00290CCC;
loc_00290CB3:
    local_rbp = (*(uint64_t *)(local_rdi)) >> (42);
    local_rbp = (uint8_t)((local_rbp) & (7));
    if (((uint8_t)(local_rbp)) == 8) goto loc_0029179C;
loc_00290CCC:
    v_stack_m78 = (uint8_t)(v_stack_p20);
    result = (uint8_t)((v_stack_p20) - 1);
    if (((uint8_t)(result)) > 5) goto loc_00290D26;
    if (v_stack_m60 < result) goto loc_00290D1D;
    if (v_stack_m60 > local_r11) goto loc_00290D1D;
    if ((((uint8_t)(*(uint64_t *)(v_stack_m60))) & (1)) == 0) goto loc_00290D1D;
    Arg1 = ((((uint8_t)(*(uint64_t *)(v_stack_m60))) & (66)) != 0) ? 1 : 0;
    result = ((((uint8_t)(*(uint64_t *)(v_stack_m60))) & (32)) != 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) == 0) goto loc_002914AA;
loc_00290D1D:
    if ((((uint8_t)(*(uint64_t *)(v_stack_m60))) & (32)) != 0) goto loc_002914F7;
loc_00290D26:
    if (v_stack_m70 == 0) goto loc_00291868;
    local_r14 = (v_stack_p10) >> (9);
    local_rsi = (uint8_t)(((uint8_t)((uint8_t)((uint8_t)(Arg2)))) ^ ((uint8_t)((uint8_t)(v_stack_p20))));
    local_rsi = (uint8_t)((local_rsi) & (15));
    local_rsi = (uint8_t)((local_rsi) ^ ((uint8_t)((uint8_t)((uint8_t)(Arg2)))));
    local_r14 = (local_r14) & (result);
    local_r14 = (local_r14) + (*(uint64_t *)(v_stack_m60));
loc_00290D80:
    result = ((uint8_t)(local_rsi)) << (56);
    local_rbx = (*(uint64_t *)(local_r14)) ^ (result);
    local_rbx = (local_rbx) & (Arg1);
    local_rbx = (local_rbx) ^ (result);
    if (((*(uint64_t *)(v_rip + 0xD35CEA)) & (0x2000000ULL)) != 0) {
    }
    if (condition_is_below) goto loc_0029153E;
loc_00290DB2:
    if (((*(uint64_t *)(v_rip + 0xD35CEA)) & (0x2000000ULL)) != 0) goto loc_00290D80;
loc_00290DCD:
    local_r15 = 0;
    if ((uint32_t)((uint32_t)(v_stack_m74)) != 0) goto loc_00290F88;
    Arg3 = (v_stack_p10) >> (18);
    Arg3 = (uint32_t)((Arg3) & (0x3FFFFFF8ULL));
    Arg3 = (Arg3) + (*(uint64_t *)(local_r14));
    if (Arg3 < (*(uint64_t *)(local_r14))) goto loc_00290E44;
    if (Arg3 > (*(uint64_t *)(local_r14))) goto loc_00290E44;
    if ((((uint8_t)(*(uint64_t *)(Arg3))) & (1)) == 0) goto loc_00290E44;
    Arg1 = ((((uint8_t)(*(uint64_t *)(Arg3))) & (66)) != 0) ? 1 : 0;
    result = ((((uint8_t)(*(uint64_t *)(Arg3))) & (32)) != 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) == 0) goto loc_002913C9;
loc_00290E44:
    Arg2 = (*(uint64_t *)(Arg3)) >> (12);
    Arg2 = (Arg2) & (result);
    local_rdi = (Arg2 + Arg2 * 2) << (4);
    local_rdi = (local_rdi) + (result);
    Arg3 = (*(uint64_t *)(local_rdi)) >> (45);
    result = (*(uint64_t *)(local_rdi)) >> (55);
    Arg3 = (uint32_t)((Arg3) & (0x3FFULL));
    result = (uint8_t)((result) & (7));
    if (((uint8_t)(local_rbp)) == ((uint8_t)(result))) goto loc_00290EDC;
    if (((uint8_t)(local_rbp)) <= ((uint8_t)(result))) goto loc_00290F6F;
    result = (uint32_t)(*(uint32_t *)(local_rdi + 0x24));
    if (((uint8_t)(local_rbp)) < ((uint8_t)(result))) {
        Arg3 = 0;
        Arg2 = local_rdi;
        Arg1 = v_stack_p8;
        result = MiRemoveActivePageTableLinks(Arg1, Arg2, Arg3, v_stack_p10);
    }
    result = ((uint8_t)(local_rbp)) << (55);
    Arg1 = (result) ^ (*(uint64_t *)(local_rdi));
    Arg1 = (Arg1) & (Arg2);
    Arg1 = (Arg1) ^ (result);
    Arg1 = (Arg1) | (result);
    *(void **)(local_rdi) = Arg1;
    goto loc_00290F5D;
loc_00290EDC:
    Arg2 = ((uint32_t)((uint32_t)(Arg3 - 1))) << (45);
    result = (*(uint64_t *)(local_rdi)) ^ (Arg2);
    local_r14 = (uint32_t)(((uint32_t)((uint32_t)(Arg3 - 1))) & (0x3FFULL));
    result = (result) & (Arg3 - 1);
    result = (result) ^ (Arg2);
    *(uint64_t *)(local_rdi) = result;
    if (Arg3 - 1 == 0) goto loc_00291778;
    if (condition_is_below) goto loc_00290F6F;
    result = (uint32_t)(*(uint32_t *)(local_rdi + 0x24));
    if (!(condition_is_above_or_equal)) {
        Arg3 = 0;
        Arg2 = local_rdi;
        Arg1 = v_stack_p8;
        result = MiRemoveActivePageTableLinks(Arg1, Arg2, Arg3, v_stack_p10);
    }
    result = (uint32_t)((local_rbp) & (7));
    local_rbx = (*(uint64_t *)(local_rdi)) & (Arg1);
    result = (result) << (10);
    result = (result) | (local_r14);
    result = (result) << (45);
    result = (result) | (local_rbx);
    *(uint64_t *)(local_rdi) = result;
loc_00290F5D:
    Arg4 = 0;
    result = MiInsertActivePageTableLinksTail(v_stack_p8, local_rdi, (uint8_t)(local_rbp), Arg4);
loc_00290F6F:
    if (((uint8_t)(local_rbp)) == 7) goto loc_002911BF;
loc_00290F83:
loc_00290F88:
    if (((uint8_t)(v_stack_m78)) >= 8) goto loc_0029165C;
    if (0 != 0) goto loc_00291584;
    Arg3 = (v_stack_p10) >> (18);
    Arg3 = (uint32_t)((Arg3) & (0x3FFFFFF8ULL));
    Arg3 = (Arg3) + ((uint8_t)(local_rbp));
    if (Arg3 < ((uint8_t)(local_rbp))) goto loc_00290FFE;
    if (Arg3 > ((uint8_t)(local_rbp))) goto loc_00290FFE;
    if ((((uint8_t)(*(uint64_t *)(Arg3))) & (1)) == 0) goto loc_00290FFE;
    Arg1 = ((((uint8_t)(*(uint64_t *)(Arg3))) & (66)) != 0) ? 1 : 0;
    result = ((((uint8_t)(*(uint64_t *)(Arg3))) & (32)) != 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) == 0) goto loc_0029145E;
loc_00290FFE:
    Arg2 = (*(uint64_t *)(Arg3)) >> (12);
    Arg2 = (Arg2) & (result);
    local_rdi = (Arg2 + Arg2 * 2) << (4);
    local_rdi = (local_rdi) + (result);
    Arg1 = (*(uint64_t *)(local_rdi)) >> (45);
    result = (*(uint64_t *)(local_rdi)) >> (55);
    Arg1 = (uint32_t)((Arg1) & (0x3FFULL));
    result = (uint8_t)((result) & (7));
    if (((uint8_t)(v_stack_m78)) == ((uint8_t)(result))) goto loc_002910ED;
    if (((uint8_t)(v_stack_m78)) <= ((uint8_t)(result))) goto loc_0029116F;
    result = (uint32_t)(*(uint32_t *)(local_rdi + 0x24));
    if (((uint8_t)(v_stack_m78)) < ((uint8_t)(result))) {
        Arg3 = 0;
        Arg2 = local_rdi;
        Arg1 = v_stack_p8;
        result = MiRemoveActivePageTableLinks(Arg1, Arg2, Arg3, Arg4);
    }
    result = (uint32_t)((v_stack_m78) & (7));
    result = (result) << (55);
    result = (result) | (Arg1);
    goto loc_00291154;
loc_0029108C:
loc_00291093:
    if (v_stack_m6C != 0) goto loc_002917E0;
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(v_stack_p8 + 0xB8))) & (15));
    if (((uint8_t)(result)) != 1) goto loc_00291817;
loc_002910AF:
    if (((*(uint8_t *)(v_rip + 0xD35A50)) & (1)) != 0) goto loc_00291835;
loc_002910BC:
loc_002910C8:
    if (v_stack_m58 != 0) goto loc_0029164F;
loc_002910D6:
loc_002910DB:
    local_rsp = (local_rsp) + (88);
    return 1;
loc_002910ED:
    Arg1 = (uint32_t)((Arg1) + 1);
    Arg2 = ((uint32_t)((uint32_t)(Arg1))) << (45);
    result = (*(uint64_t *)(local_rdi)) ^ (Arg2);
    local_rbp = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) & (0x3FFULL));
    result = (result) & (Arg1);
    result = (result) ^ (Arg2);
    *(uint64_t *)(local_rdi) = result;
    if (condition_is_below) goto loc_0029116F;
    result = (uint32_t)(*(uint32_t *)(local_rdi + 0x24));
    if (!(condition_is_above_or_equal)) {
        Arg3 = 0;
        Arg2 = local_rdi;
        Arg1 = v_stack_p8;
        result = MiRemoveActivePageTableLinks(Arg1, Arg2, Arg3, Arg4);
    }
    result = (uint32_t)((v_stack_m78) & (7));
    result = (result) << (10);
    result = (result) | (local_rbp);
    result = (result) << (45);
loc_00291154:
    local_rbx = (*(uint64_t *)(local_rdi)) & (Arg1);
    Arg4 = 0;
    result = (result) | (local_rbx);
    *(uint64_t *)(local_rdi) = result;
    result = MiInsertActivePageTableLinksTail(v_stack_p8, local_rdi, (uint8_t)(v_stack_m78), Arg4);
loc_0029116F:
    if (((uint8_t)(v_stack_m78)) == 7) goto loc_002912CF;
loc_00291183:
loc_00291188:
loc_0029118D:
    local_rdi = (v_stack_p38) + (8);
    v_stack_p38 = local_rdi;
    if (condition_is_equal) goto loc_0029108C;
    goto loc_00290BAF;
loc_002911BF:
    if ((*(uint64_t *)(v_stack_p8 + 0x60)) >= (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB9EEB6) + *(uint16_t *)(v_stack_p8 + 0xAE) * 8) + 0x44C0) + 0x38))) goto loc_00290F83;
    if ((*(uint64_t *)(v_stack_p8 + 0x18)) == 0) goto loc_00290F83;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB9EEB6) + *(uint16_t *)(v_stack_p8 + 0xAE) * 8) + 0x44D0)) == (v_stack_p8 + 24)) goto loc_00290F83;
    result = ExAcquireSpinLockExclusiveAtDpcLevel(v_rip + 12214966, *(uint64_t *)(v_stack_p8 + 0x60), (uint8_t)(v_stack_m78), v_stack_p30);
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB9EEB6) + *(uint16_t *)(v_stack_p8 + 0xAE) * 8) + 0x44C0) + 0x35)) != 0) goto loc_002917ED;
    if (*(uint64_t *)(v_stack_p8 + 0x18) == 0) goto loc_002917ED;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_p8 + 0x18) + 0x8)) != (v_stack_p8 + 24)) goto loc_00291238;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_p8 + 0x18 + 0x8))) == (v_stack_p8 + 24)) goto loc_002917A6;
loc_00291238:
loc_0029123F:
    result = MiPteHasShadow(3, *(uint64_t *)(v_stack_p8 + 0x60), (uint8_t)(v_stack_m78), v_stack_p30);
    if (result == 0) goto loc_00290B1B;
    if (*(uint64_t *)(result + 0x508) == 0) goto loc_00290B1B;
    result = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB9EEB6) + *(uint16_t *)(v_stack_p8 + 0xAE) * 8) + 0x44C0)) >> (3);
    result = (uint32_t)((result) & (511));
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(result + 0x508) + result * 8))) & (32)) != 0) {
        local_rsi = (local_rsi) | (32);
    }
    local_rsi = (local_rsi) | (66);
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(result + 0x508) + result * 8))) & (66)) == 0) { local_rsi = local_rsi; }
    goto loc_00290B1B;
loc_00291287:
    result = MiPteHasShadow(local_rsi, *(uint64_t *)(v_stack_p8 + 0x60), (uint8_t)(v_stack_m78), v_stack_p30);
    if (result == 0) goto loc_00290BF9;
    if (*(uint64_t *)(result + 0x508) == 0) goto loc_00290BF9;
    result = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB9EEB6) + *(uint16_t *)(v_stack_p8 + 0xAE) * 8) + 0x44C0)) >> (3);
    result = (uint32_t)((result) & (511));
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(result + 0x508) + result * 8))) & (32)) != 0) {
        Arg2 = (*(uint64_t *)(v_stack_p8 + 0x60)) | (32);
    }
    Arg2 = (Arg2) | (66);
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(result + 0x508) + result * 8))) & (66)) == 0) { Arg2 = Arg2; }
    goto loc_00290BF9;
loc_002912CF:
    if ((*(uint64_t *)(v_stack_p8 + 0x60)) < (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB9EDA6) + *(uint16_t *)(v_stack_p8 + 0xAE) * 8) + 0x44C0) + 0x38))) goto loc_00291183;
    if ((*(uint64_t *)(v_stack_p8 + 0x18)) == 0) goto loc_00291183;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB9EDA6) + *(uint16_t *)(v_stack_p8 + 0xAE) * 8) + 0x44C8)) == (v_stack_p8 + 24)) goto loc_00291183;
    result = ExAcquireSpinLockExclusiveAtDpcLevel(v_rip + 12214691, *(uint64_t *)(v_stack_p8 + 0x60), *(uint64_t *)(*(uint64_t *)(v_rip + 0xB9EDA6) + *(uint16_t *)(v_stack_p8 + 0xAE) * 8), v_stack_p30);
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB9EDA6) + *(uint16_t *)(v_stack_p8 + 0xAE) * 8) + 0x44C0) + 0x35)) != 0) goto loc_00291802;
    if (*(uint64_t *)(v_stack_p8 + 0x18) == 0) goto loc_00291802;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_p8 + 0x18) + 0x8)) != (v_stack_p8 + 24)) goto loc_00291238;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_p8 + 0x18 + 0x8))) != (v_stack_p8 + 24)) goto loc_00291238;
    *(uint64_t *)(*(uint64_t *)(v_stack_p8 + 0x18 + 0x8)) = *(uint64_t *)(v_stack_p8 + 0x18);
    *(uint64_t *)(*(uint64_t *)(v_stack_p8 + 0x18) + 0x8) = *(uint64_t *)(v_stack_p8 + 0x18 + 0x8);
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB9EDA6) + *(uint16_t *)(v_stack_p8 + 0xAE) * 8) + 0x44C8) + 0x8)) != (*(uint64_t *)(*(uint64_t *)(v_rip + 0xB9EDA6) + *(uint16_t *)(v_stack_p8 + 0xAE) * 8) + 17608)) goto loc_00291238;
    *(uint64_t *)(v_stack_p8 + 0x18) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB9EDA6) + *(uint16_t *)(v_stack_p8 + 0xAE) * 8) + 0x44C8);
    *(uint64_t *)(v_stack_p8 + 0x18 + 0x8) = *(uint64_t *)(*(uint64_t *)(v_rip + 0xB9EDA6) + *(uint16_t *)(v_stack_p8 + 0xAE) * 8) + 17608;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB9EDA6) + *(uint16_t *)(v_stack_p8 + 0xAE) * 8) + 0x44C8) + 0x8) = v_stack_p8 + 24;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB9EDA6) + *(uint16_t *)(v_stack_p8 + 0xAE) * 8) + 0x44C8) = v_stack_p8 + 24;
    result = ExReleaseSpinLockExclusiveFromDpcLevel(v_rip + 12214611, *(uint64_t *)(v_stack_p8 + 0x60), *(uint64_t *)(*(uint64_t *)(v_rip + 0xB9EDA6) + *(uint16_t *)(v_stack_p8 + 0xAE) * 8), v_stack_p30);
    goto loc_00291183;
loc_00291382:
    result = MiPteHasShadow(v_rip + 12214611, *(uint64_t *)(v_stack_p8 + 0x60), *(uint64_t *)(*(uint64_t *)(v_rip + 0xB9EDA6) + *(uint16_t *)(v_stack_p8 + 0xAE) * 8), v_stack_p30);
    if (result == 0) goto loc_00290C83;
    if (*(uint64_t *)(result + 0x508) == 0) goto loc_00290C83;
    Arg3 = (*(uint64_t *)(*(uint64_t *)(v_rip + 0xB9EDA6) + *(uint16_t *)(v_stack_p8 + 0xAE) * 8)) >> (3);
    Arg3 = (uint32_t)((Arg3) & (511));
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(result + 0x508) + Arg3 * 8))) & (32)) != 0) {
        Arg2 = (*(uint64_t *)(v_stack_p8 + 0x60)) | (32);
    }
    Arg2 = (Arg2) | (66);
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(result + 0x508) + Arg3 * 8))) & (66)) == 0) { Arg2 = Arg2; }
    goto loc_00290C83;
loc_002913C9:
    result = MiPteHasShadow(Arg2, Arg2, Arg3, v_stack_p30);
    if (result == 0) goto loc_00290E44;
    if (*(uint64_t *)(result + 0x508) == 0) goto loc_00290E44;
    Arg3 = (Arg3) >> (3);
    Arg3 = (uint32_t)((Arg3) & (511));
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(result + 0x508) + Arg3 * 8))) & (32)) != 0) {
        Arg2 = (Arg2) | (32);
    }
    v_stack_p24 = (uint32_t)((uint32_t)(v_stack_m74));
    Arg2 = (Arg2) | (66);
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(result + 0x508) + Arg3 * 8))) & (66)) == 0) { Arg2 = Arg2; }
    goto loc_00290E44;
loc_00291415:
    v_stack_p2C = 1;
    result = MiLockWorkingSetCoreExclusive(v_stack_p8, Arg2, Arg3, v_stack_p30);
    Arg1 = (*(uint64_t *)(v_stack_p30 + 0x20)) + (6);
    Arg1 = (Arg1) + (v_stack_m78);
    if ((*(uint64_t *)(v_stack_p8 + 0x70)) >= Arg1) goto loc_00290BA6;
    result = MiUnlockWorkingSetCoreExclusive(v_stack_p8, Arg2, Arg3, v_stack_p30);
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0xB9EDA6) + *(uint16_t *)(v_stack_p8 + 0xAE) * 8) + 17608 != 0) {
        Arg2 = *(uint64_t *)(*(uint64_t *)(v_rip + 0xB9EDA6) + *(uint16_t *)(v_stack_p8 + 0xAE) * 8) + 17608;
        Arg1 = v_stack_p8;
        result = MiUnlockPageTable(Arg1, Arg2, Arg3, v_stack_p30);
    }
    result = 0;
    goto loc_002910DB;
loc_0029145E:
    result = MiPteHasShadow(Arg1, Arg2, Arg3, v_stack_p30);
    if (result == 0) goto loc_00290FFE;
    if (*(uint64_t *)(result + 0x508) == 0) goto loc_00290FFE;
    Arg3 = (Arg3) >> (3);
    Arg3 = (uint32_t)((Arg3) & (511));
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(result + 0x508) + Arg3 * 8))) & (32)) != 0) {
        Arg2 = (Arg2) | (32);
    }
    v_stack_p24 = (uint32_t)((uint32_t)(v_stack_m74));
    Arg2 = (Arg2) | (66);
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(result + 0x508) + Arg3 * 8))) & (66)) == 0) { Arg2 = Arg2; }
    goto loc_00290FFE;
loc_002914AA:
    result = MiPteHasShadow(Arg2, Arg2, Arg3, v_stack_p30);
    if (result == 0) goto loc_00290D1D;
    if (*(uint64_t *)(result + 0x508) == 0) goto loc_00290D1D;
    result = (Arg3) >> (3);
    result = (uint32_t)((result) & (511));
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(result + 0x508) + result * 8))) & (32)) != 0) {
        Arg2 = (Arg2) | (32);
    }
    v_stack_p24 = (uint32_t)((uint32_t)(v_stack_p24));
    Arg2 = (Arg2) | (66);
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(result + 0x508) + result * 8))) & (66)) == 0) { Arg2 = Arg2; }
    goto loc_00290D1D;
loc_002914F7:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0xB8)))) & (15)) != 0) goto loc_00291708;
    if ((*(uint64_t *)(v_stack_p8 + 0x270)) != 0) goto loc_00291727;
loc_00291514:
    if ((uint8_t)(local_rbp) == 0) goto loc_00291188;
    local_r12 = 0;
    v_stack_p20 = 0;
    goto loc_00290D26;
loc_0029152A:
    if (!sign_flag) goto loc_00290B94;
    result = ExpWaitForSpinLockSharedAndAcquire(Arg2, 255, Arg3, v_stack_p30);
    goto loc_00290BA1;
loc_0029153E:
    result = (uint8_t)(((uint8_t)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB9EDA6) + *(uint16_t *)(v_stack_p8 + 0xAE) * 8) + 17608)) & (33));
    if (((uint8_t)(result)) != 1) goto loc_00290DB2;
    result = (255) + (0);
    if ((v_stack_p8 + 24) < result) goto loc_00290DB2;
    result = MiCheckLinearProtectedPteAccessedBit(v_stack_p8 + 24, *(uint64_t *)(*(uint64_t *)(v_rip + 0xB9EDA6) + *(uint16_t *)(v_stack_p8 + 0xAE) * 8) + 17608, 128, v_stack_p30);
    goto loc_00290DB2;
loc_00291584:
    if (0 != 7) goto loc_00291183;
    if ((*(uint64_t *)(v_stack_p8 + 0x60)) < (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB9EADD) + *(uint16_t *)(v_stack_p8 + 0xAE) * 8) + 0x44C0) + 0x38))) goto loc_00291183;
    if ((*(uint64_t *)(v_stack_p8 + 0x18)) == 0) goto loc_00291183;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB9EADD) + *(uint16_t *)(v_stack_p8 + 0xAE) * 8) + 0x44C8)) == (v_stack_p8 + 24)) goto loc_00291183;
    result = ExAcquireSpinLockExclusiveAtDpcLevel(v_rip + 12213978, *(uint64_t *)(v_stack_p8 + 0x60), *(uint64_t *)(*(uint64_t *)(v_rip + 0xB9EADD) + *(uint16_t *)(v_stack_p8 + 0xAE) * 8), v_stack_p30);
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB9EADD) + *(uint16_t *)(v_stack_p8 + 0xAE) * 8) + 0x44C0) + 0x35)) != 0) goto loc_0029182F;
    if (*(uint64_t *)(v_stack_p8 + 0x18) == 0) goto loc_0029182F;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_p8 + 0x18) + 0x8)) != (v_stack_p8 + 24)) goto loc_00291238;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_p8 + 0x18 + 0x8))) != (v_stack_p8 + 24)) goto loc_00291238;
    *(uint64_t *)(*(uint64_t *)(v_stack_p8 + 0x18 + 0x8)) = *(uint64_t *)(v_stack_p8 + 0x18);
    *(uint64_t *)(*(uint64_t *)(v_stack_p8 + 0x18) + 0x8) = *(uint64_t *)(v_stack_p8 + 0x18 + 0x8);
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB9EADD) + *(uint16_t *)(v_stack_p8 + 0xAE) * 8) + 0x44C8) + 0x8)) != (*(uint64_t *)(*(uint64_t *)(v_rip + 0xB9EADD) + *(uint16_t *)(v_stack_p8 + 0xAE) * 8) + 17608)) goto loc_00291238;
    *(uint64_t *)(v_stack_p8 + 0x18) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB9EADD) + *(uint16_t *)(v_stack_p8 + 0xAE) * 8) + 0x44C8);
    *(uint64_t *)(v_stack_p8 + 0x18 + 0x8) = *(uint64_t *)(*(uint64_t *)(v_rip + 0xB9EADD) + *(uint16_t *)(v_stack_p8 + 0xAE) * 8) + 17608;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB9EADD) + *(uint16_t *)(v_stack_p8 + 0xAE) * 8) + 0x44C8) + 0x8) = v_stack_p8 + 24;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB9EADD) + *(uint16_t *)(v_stack_p8 + 0xAE) * 8) + 0x44C8) = v_stack_p8 + 24;
    result = ExReleaseSpinLockExclusiveFromDpcLevel(v_rip + 12213883, *(uint64_t *)(v_stack_p8 + 0x60), *(uint64_t *)(*(uint64_t *)(v_rip + 0xB9EADD) + *(uint16_t *)(v_stack_p8 + 0xAE) * 8), v_stack_p30);
    goto loc_00291183;
loc_0029164F:
    result = MiUnlockPageTable(v_stack_p8, *(uint64_t *)(v_stack_p8 + 0x60), *(uint64_t *)(*(uint64_t *)(v_rip + 0xB9EADD) + *(uint16_t *)(v_stack_p8 + 0xAE) * 8), v_stack_p30);
    goto loc_002910D6;
loc_0029165C:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB9EADD) + *(uint16_t *)(v_stack_p8 + 0xAE) * 8) + 0x44C8) + 0x8)) != (*(uint64_t *)(*(uint64_t *)(v_rip + 0xB9EADD) + *(uint16_t *)(v_stack_p8 + 0xAE) * 8) + 17608)) goto loc_0029118D;
    goto loc_0029118D;
loc_00291676:
    if ((*(uint64_t *)(v_stack_p8 + 0x60)) > result) goto loc_00290A9E;
    local_r14 = 0;
    v_stack_p28 = 0;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0xB8)))) & (15)) != 0) goto loc_00291858;
    result = MiLockNestedPageTable(v_stack_p8, v_stack_p8 + 24, *(uint64_t *)(*(uint64_t *)(v_rip + 0xB9EADD) + *(uint16_t *)(v_stack_p8 + 0xAE) * 8), v_stack_p30);
    v_stack_p40 = v_stack_p8 + 24;
    goto loc_00290AA9;
loc_002916C1:
    v_stack_p2C = 1;
    result = MiLockWorkingSetCoreExclusive(v_stack_p8, v_stack_p8 + 24, *(uint64_t *)(*(uint64_t *)(v_rip + 0xB9EADD) + *(uint16_t *)(v_stack_p8 + 0xAE) * 8), v_stack_pB8);
    goto loc_00290BA1;
loc_002916D6:
    result = MI_READ_PTE_LOCK_FREE(v_stack_p8 + 24, v_stack_p8 + 24, *(uint64_t *)(*(uint64_t *)(v_rip + 0xB9EADD) + *(uint16_t *)(v_stack_p8 + 0xAE) * 8), v_stack_pB8);
    result = (result) >> (12);
    result = (result) & (v_stack_p8 + 24);
    Arg1 = (result + result * 2) + (result + result * 2);
    result = (*(uint64_t *)(local_rbp + arg1 * 8)) >> (42);
    result = (uint8_t)((result) & (7));
    goto loc_00290B33;
loc_00291708:
    if (((*(uint64_t *)(v_rip + 0xD35379)) & ((uint32_t)(v_stack_m74))) == 0) goto loc_00291514;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p8 + 0xB8))) >> (8));
    if ((((uint8_t)(result)) & (8)) == 0) goto loc_00291514;
loc_00291727:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0xB8)))) & (15)) == 0) goto loc_00291891;
    Arg2 = (v_stack_p8 + 24) >> (12);
    Arg2 = (Arg2) & ((uint32_t)(*(uint32_t *)(v_stack_p8 + 0xB8)));
    Arg1 = (Arg2 + Arg2 * 2) << (4);
    Arg3 = 0;
    Arg1 = (Arg1) + ((uint32_t)(*(uint32_t *)(v_stack_p8 + 0xB8)));
    result = MiGetPagePrivilege(Arg1, Arg3 + 2, Arg3, v_stack_pB8);
    if ((((uint8_t)(result)) & (65)) != 0) goto loc_00290D26;
    goto loc_00291514;
loc_00291778:
    Arg3 = 0;
    result = MiRebuildPageTableAges(v_stack_p8, v_stack_pB8, Arg3, v_stack_pB8);
    goto loc_00290F6F;
loc_00291791:
    v_stack_p24 = 1;
loc_0029179C:
    goto loc_00290CCC;
loc_002917A6:
    *(uint64_t *)(v_stack_p8) = result;
    local_rbx = (v_stack_p8 + 24) + (0x44C8ULL);
    *(uint64_t *)(result + 0x8) = v_stack_p8;
    if ((*(uint64_t *)(*(uint64_t *)(local_rbx + 0x8))) != local_rbx) goto loc_00291238;
    *(uint64_t *)(local_r14) = local_rbx;
    *(uint64_t *)(local_r14 + 0x8) = *(uint64_t *)(local_rbx + 0x8);
    *(uint64_t *)(*(uint64_t *)(local_rbx + 0x8)) = 0;
    *(uint64_t *)(local_rbx + 0x8) = 0;
    result = ExReleaseSpinLockExclusiveFromDpcLevel(v_rip + 12213493, v_stack_pB8, Arg3, v_stack_pB8);
    goto loc_00290F83;
loc_002917E0:
    result = MiUnlockWorkingSetCoreExclusive(v_stack_p8, v_stack_pB8, Arg3, v_stack_pB8);
    goto loc_002910C8;
loc_002917ED:
    *(uint8_t *)(v_stack_p8 + 0x18 + 0x36) = 1;
    result = ExReleaseSpinLockExclusiveFromDpcLevel(v_rip + 12213452, v_stack_pB8, Arg3, v_stack_pB8);
    goto loc_00290F83;
loc_00291802:
    *(uint8_t *)(v_stack_p8 + 0x18 + 0x36) = 1;
loc_00291806:
    result = ExReleaseSpinLockExclusiveFromDpcLevel(v_rip + 12213427, v_stack_pB8, Arg3, v_stack_pB8);
    goto loc_00291183;
loc_00291817:
    goto loc_002910AF;
loc_00291823:
    goto loc_00290B6F;
loc_0029182F:
    *(uint8_t *)(local_rbx + 0x36) = 1;
    goto loc_00291806;
loc_00291835:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC7C61D))) != 0) goto loc_002910BC;
    result = ExpReleaseSpinLockSharedFromDpcLevelInstrumented(v_stack_p8 + 256, v_stack_p98, Arg3, v_stack_pB8);
    goto loc_002910C8;
loc_00291858:
    v_stack_p24 = 1;
    goto loc_00290AA9;
loc_00291868:
    Arg2 = (0) << (42);
    Arg1 = (Arg2) ^ (*(uint64_t *)(v_stack_p8 + 0x18));
    Arg1 = (Arg1) & (*(uint64_t *)(v_stack_p8 + 0x18));
    Arg1 = (Arg1) ^ (Arg2);
    *(void **)(v_stack_p8 + 0x18) = Arg1;
    goto loc_00290DCD;
loc_00291891:
    if (0 > (*(uint64_t *)(v_stack_p8 + 0x18))) goto loc_00291514;
    goto loc_00290D26;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x70` | `64` | `R` |
| `Arg1` | `+ 0xB8` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00290A20&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
