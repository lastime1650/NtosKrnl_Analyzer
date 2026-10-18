# MiLockLowestValidPageTableEx

- RVA: `0x00280D10`–`0x00281803` (길이 `2,803` bytes)
- VA: `0x0000000140280D10`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000666F0`
- 디코드: `638`개 명령, `2,803/2,803` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **21**; 고유 호출 대상: **16**
- 직접 호출자로 확인된 함수: **20**
- RIP 상대 이미지 참조: **7**

### Outgoing calls
- `0x00280EF1` → [MiWriteValidPteNewProtection](MiWriteValidPteNewProtection_function_00281810.md) (function, `0x00281810`)
- `0x00280FB8` → [KxWaitForLockOwnerShip](../25/KxWaitForLockOwnerShip_function_00257EB0.md) (function, `0x00257EB0`)
- `0x0028128D` → [KxWaitForLockChainValid](../21/KxWaitForLockChainValid_function_00217AA0.md) (function, `0x00217AA0`)
- `0x002812BA` → [KeDisableInterrupts](../21/KeDisableInterrupts_function_00217BE0.md) (function, `0x00217BE0`)
- `0x002812CD` → [KiHaltOnAddressWakeEntireList](../21/KiHaltOnAddressWakeEntireList_function_00217AF4.md) (function, `0x00217AF4`)
- `0x002813C9` → [KiReleaseQueuedSpinLockInstrumented](../21/KiReleaseQueuedSpinLockInstrumented_function_002179F0.md) (function, `0x002179F0`)
- `0x00281491` → [KiAcquireQueuedSpinLockInstrumented](../27/KiAcquireQueuedSpinLockInstrumented_function_00275850.md) (function, `0x00275850`)
- `0x002814AC` → [KiAcquireQueuedSpinLockInstrumented](../27/KiAcquireQueuedSpinLockInstrumented_function_00275850.md) (function, `0x00275850`)
- `0x002815D4` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x002815E3` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00281617` → [KiRemoveSystemWorkPriorityKick](../26/KiRemoveSystemWorkPriorityKick_function_002631D0.md) (function, `0x002631D0`)
- `0x00281621` → [KxWaitForLockOwnerShip](../25/KxWaitForLockOwnerShip_function_00257EB0.md) (function, `0x00257EB0`)
- `0x00281672` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x002816AB` → [MiCheckLinearProtectedPteAccessedBit](../29/MiCheckLinearProtectedPteAccessedBit_function_00292D80.md) (function, `0x00292D80`)
- `0x002816C3` → [ExAcquireSpinLockExclusiveAtDpcLevel](../24/ExAcquireSpinLockExclusiveAtDpcLevel_function_00248E80.md) (function, `0x00248E80`)
- `0x002816E3` → [ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented](../2C/ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented_function_002C0F44.md) (function, `0x002C0F44`)
- `0x00281735` → [ExpReleaseSpinLockSharedFromDpcLevelInstrumented](../2F/ExpReleaseSpinLockSharedFromDpcLevelInstrumented_function_002F0F48.md) (function, `0x002F0F48`)
- `0x00281751` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0028175D` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00281781` → [ExAcquireSpinLockExclusiveAtDpcLevel](../24/ExAcquireSpinLockExclusiveAtDpcLevel_function_00248E80.md) (function, `0x00248E80`)
- `0x002817D3` → [ExReleaseSpinLockExclusiveFromDpcLevel](../24/ExReleaseSpinLockExclusiveFromDpcLevel_function_002497E0.md) (function, `0x002497E0`)

### Direct callers
- [MiTranslatePageForCopy](../22/MiTranslatePageForCopy_function_00228960.md) at `0x00228C1E`
- [sub_002434F4](../24/Unknown_function_002434F4.md) at `0x00243514`
- [MiSynchronizeSystemVa](MiSynchronizeSystemVa_function_0028ECB8.md) at `0x0028EF0A`
- [MiGetWorkingSetInfoList](../2A/MiGetWorkingSetInfoList_function_002AF770.md) at `0x002AFC44`
- [MiLockStealUserVm](../2B/MiLockStealUserVm_function_002B3EDC.md) at `0x002B43E2`
- [MiTrimSharedPageFromViews](../2E/MiTrimSharedPageFromViews_function_002E16F8.md) at `0x002E1E1F`
- [MiSharePages](../31/MiSharePages_function_00315110.md) at `0x0031577D`
- [MiLockPoolCommitPageTable](../32/MiLockPoolCommitPageTable_function_00328BAC.md) at `0x00328C9B`
- [MiRelockFaultState](../36/MiRelockFaultState_function_0036A230.md) at `0x0036A285`
- [MiDeprioritizeVirtualAddresses](../42/MiDeprioritizeVirtualAddresses_function_0042AD1C.md) at `0x0042ADBE`
- [MiConvertAndFlushWsleVas](../49/MiConvertAndFlushWsleVas_function_00492CB4.md) at `0x00492D1F`
- [MmUpdateUserShadowStackValue](../49/MmUpdateUserShadowStackValue_function_004935D8.md) at `0x00493804`
- [MiSetPagesModified](../49/MiSetPagesModified_function_0049DC2C.md) at `0x0049DEF6`
- [MiProtectAweRegion](../4C/MiProtectAweRegion_function_004CE62C.md) at `0x004CEA06`
- [NtUnlockVirtualMemory](../4E/NtUnlockVirtualMemory_function_004EE890.md) at `0x004EEB66`
- [NtUnlockVirtualMemory](../4E/NtUnlockVirtualMemory_function_004EE890.md) at `0x004EEE35`
- [MiSplitReducedCommitClonePage](../4F/MiSplitReducedCommitClonePage_function_004FA808.md) at `0x004FA8BC`
- [MiDeleteBootRange](../66/MiDeleteBootRange_function_0066E450.md) at `0x0066E557`
- [MiSetGraphicsPtes](../67/MiSetGraphicsPtes_function_00678554.md) at `0x00678637`
- [MiScrubLargeMappedPage](../69/MiScrubLargeMappedPage_function_00693E2C.md) at `0x00693F54`
- [MiComputeIdealLargePage](../69/MiComputeIdealLargePage_function_006987C0.md) at `0x006988E6`

### Static image references
- `0x00280DDD` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x00280DFD` → RVA `0x00FC6B06` (`ALMOSTRO`; read)
- `0x00280FEA` → RVA `0x00FC6A88` (`ALMOSTRO`; read)
- `0x002813B0` → RVA `0x00F0DE58` (`.data`; read)
- `0x00281532` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x002815C6` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)
- `0x00281775` → RVA `0x00E374C0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x002817C7` → [sub_006DA166](../6D/Unknown_function_006DA166.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00280D10  44 89 4C 24 20                  mov dword ptr [rsp + 0x20], r9d
00280D15  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
00280D1A  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
00280D1F  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
00280D24  53                              push rbx
00280D25  55                              push rbp
00280D26  56                              push rsi
00280D27  57                              push rdi
00280D28  41 54                           push r12
00280D2A  41 55                           push r13
00280D2C  41 56                           push r14
00280D2E  41 57                           push r15
00280D30  48 83 EC 68                     sub rsp, 0x68
00280D34  45 8B D9                        mov r11d, r9d
00280D37  49 BC 00 00 00 00 80 F6 FF FF   movabs r12, 0xfffff68000000000
00280D41  4C 8B D2                        mov r10, rdx
00280D44  4C 8B C9                        mov r9, rcx
00280D47  49 C1 EA 09                     shr r10, 9
00280D4B  48 B9 F8 FF FF FF 7F 00 00 00   movabs rcx, 0x7ffffffff8
00280D55  33 FF                           xor edi, edi
00280D57  4C 23 D1                        and r10, rcx
00280D5A  49 89 38                        mov qword ptr [r8], rdi
00280D5D  49 8B C4                        mov rax, r12
00280D60  4C 03 D0                        add r10, rax
00280D63  4C 89 54 24 40                  mov qword ptr [rsp + 0x40], r10
00280D68  49 C1 EA 09                     shr r10, 9
00280D6C  4C 23 D1                        and r10, rcx
00280D6F  49 8B C4                        mov rax, r12
00280D72  4C 03 D0                        add r10, rax
00280D75  4C 89 54 24 48                  mov qword ptr [rsp + 0x48], r10
00280D7A  49 C1 EA 09                     shr r10, 9
00280D7E  4C 23 D1                        and r10, rcx
00280D81  49 8B C4                        mov rax, r12
00280D84  4C 03 D0                        add r10, rax
00280D87  4C 89 54 24 50                  mov qword ptr [rsp + 0x50], r10
00280D8C  49 C1 EA 09                     shr r10, 9
00280D90  4C 23 D1                        and r10, rcx
00280D93  49 8B C4                        mov rax, r12
00280D96  4C 03 D0                        add r10, rax
00280D99  48 BD 68 DF BE 7D FB F6 FF FF   movabs rbp, 0xfffff6fb7dbedf68
00280DA3  4C 89 54 24 58                  mov qword ptr [rsp + 0x58], r10
00280DA8  4C 8B ED                        mov r13, rbp
00280DAB  4C 89 6C 24 38                  mov qword ptr [rsp + 0x38], r13
00280DB0  45 85 DB                        test r11d, r11d
00280DB3  0F 85 97 08 00 00               jne 0x140281650
00280DB9  65 48 8B 14 25 20 00 00 00      mov rdx, qword ptr gs:[0x20]
00280DC2  41 8B 81 B8 00 00 00            mov eax, dword ptr [r9 + 0xb8]
00280DC9  24 0F                           and al, 0xf
00280DCB  0F 85 B4 05 00 00               jne 0x140281385
00280DD1  B9 02 00 00 00                  mov ecx, 2
00280DD6  4D 8D 81 B0 00 00 00            lea r8, [r9 + 0xb0]
00280DDD  4C 8D 3D 1C F2 D7 FF            lea r15, [rip - 0x280de4]
00280DE4  8B C1                           mov eax, ecx
00280DE6  48 8D 88 C4 09 00 00            lea rcx, [rax + 0x9c4]
00280DED  48 8D 0C 48                     lea rcx, [rax + rcx*2]
00280DF1  48 8D 0C CA                     lea rcx, [rdx + rcx*8]
00280DF5  4C 89 41 08                     mov qword ptr [rcx + 8], r8
00280DF9  48 89 39                        mov qword ptr [rcx], rdi
00280DFC  90                              nop
00280DFD  F6 05 02 5D D4 00 21            test byte ptr [rip + 0xd45d02], 0x21
00280E04  0F 85 91 06 00 00               jne 0x14028149b
00280E0A  48 8B D1                        mov rdx, rcx
00280E0D  49 87 10                        xchg qword ptr [r8], rdx
00280E10  48 85 D2                        test rdx, rdx
00280E13  0F 85 08 08 00 00               jne 0x140281621
00280E19  41 BE 02 00 00 00               mov r14d, 2
00280E1F  4A 8B 74 F4 40                  mov rsi, qword ptr [rsp + r14*8 + 0x40]
00280E24  48 B9 FF FF FF FF FF F6 FF FF   movabs rcx, 0xfffff6ffffffffff
00280E2E  49 BB FF DF BE 7D FB F6 FF FF   movabs r11, 0xfffff6fb7dbedfff
00280E38  49 BA F8 D7 BE 7D FB F6 FF FF   movabs r10, 0xfffff6fb7dbed7f8
00280E42  48 8B 1E                        mov rbx, qword ptr [rsi]
00280E45  49 B8 00 D0 BE 7D FB F6 FF FF   movabs r8, 0xfffff6fb7dbed000
00280E4F  4C 89 74 24 30                  mov qword ptr [rsp + 0x30], r14
00280E54  49 8B C0                        mov rax, r8
00280E57  48 3B F0                        cmp rsi, rax
00280E5A  72 2F                           jb 0x140280e8b
00280E5C  49 8B C2                        mov rax, r10
00280E5F  48 3B F0                        cmp rsi, rax
00280E62  77 27                           ja 0x140280e8b
00280E64  F6 C3 01                        test bl, 1
00280E67  0F 84 5D 01 00 00               je 0x140280fca
00280E6D  F6 C3 42                        test bl, 0x42
00280E70  0F 95 C1                        setne cl
00280E73  F6 C3 20                        test bl, 0x20
00280E76  0F 95 C0                        setne al
00280E79  84 C8                           test al, cl
00280E7B  0F 84 69 01 00 00               je 0x140280fea
00280E81  48 B9 FF FF FF FF FF F6 FF FF   movabs rcx, 0xfffff6ffffffffff
00280E8B  F6 C3 01                        test bl, 1
00280E8E  0F 84 36 01 00 00               je 0x140280fca
00280E94  84 DB                           test bl, bl
00280E96  0F 88 2E 01 00 00               js 0x140280fca
00280E9C  F6 C3 20                        test bl, 0x20
00280E9F  0F 85 8B 00 00 00               jne 0x140280f30
00280EA5  8B EF                           mov ebp, edi
00280EA7  48 8B FE                        mov rdi, rsi
00280EAA  48 C1 E7 19                     shl rdi, 0x19
00280EAE  49 8B C4                        mov rax, r12
00280EB1  48 C1 E0 19                     shl rax, 0x19
00280EB5  48 2B F8                        sub rdi, rax
00280EB8  41 8B 81 B8 00 00 00            mov eax, dword ptr [r9 + 0xb8]
00280EBF  48 C1 FF 10                     sar rdi, 0x10
00280EC3  A8 0F                           test al, 0xf
00280EC5  74 14                           je 0x140280edb
00280EC7  49 8B C0                        mov rax, r8
00280ECA  48 3B F0                        cmp rsi, rax
00280ECD  72 0C                           jb 0x140280edb
00280ECF  49 8B C3                        mov rax, r11
00280ED2  48 3B F0                        cmp rsi, rax
00280ED5  0F 86 9A 08 00 00               jbe 0x140281775
00280EDB  49 8B C4                        mov rax, r12
00280EDE  48 3B F8                        cmp rdi, rax
00280EE1  0F 83 D4 08 00 00               jae 0x1402817bb
00280EE7  48 83 CB 20                     or rbx, 0x20
00280EEB  48 8B CE                        mov rcx, rsi
00280EEE  48 8B D3                        mov rdx, rbx
00280EF1  E8 1A 09 00 00                  call 0x140281810
00280EF6  4C 8B 8C 24 B0 00 00 00         mov r9, qword ptr [rsp + 0xb0]
00280EFE  49 B8 00 D0 BE 7D FB F6 FF FF   movabs r8, 0xfffff6fb7dbed000
00280F08  49 BA F8 D7 BE 7D FB F6 FF FF   movabs r10, 0xfffff6fb7dbed7f8
00280F12  49 BB FF DF BE 7D FB F6 FF FF   movabs r11, 0xfffff6fb7dbedfff
00280F1C  85 ED                           test ebp, ebp
00280F1E  0F 85 A8 08 00 00               jne 0x1402817cc
00280F24  48 BD 68 DF BE 7D FB F6 FF FF   movabs rbp, 0xfffff6fb7dbedf68
00280F2E  33 FF                           xor edi, edi
00280F30  49 3B F5                        cmp rsi, r13
00280F33  75 1B                           jne 0x140280f50
00280F35  4D 85 F6                        test r14, r14
00280F38  0F 84 84 00 00 00               je 0x140280fc2
00280F3E  4C 8B 8C 24 B0 00 00 00         mov r9, qword ptr [rsp + 0xb0]
00280F46  49 FF CE                        dec r14
00280F49  33 FF                           xor edi, edi
00280F4B  E9 CF FE FF FF                  jmp 0x140280e1f
00280F50  48 8B C5                        mov rax, rbp
00280F53  48 3B F0                        cmp rsi, rax
00280F56  0F 85 F6 00 00 00               jne 0x140281052
00280F5C  65 4C 8B 04 25 20 00 00 00      mov r8, qword ptr gs:[0x20]
00280F65  41 8B 81 B8 00 00 00            mov eax, dword ptr [r9 + 0xb8]
00280F6C  24 0F                           and al, 0xf
00280F6E  0F 85 ED 03 00 00               jne 0x140281361
00280F74  B9 02 00 00 00                  mov ecx, 2
00280F79  49 8D 91 B0 00 00 00            lea rdx, [r9 + 0xb0]
00280F80  8B C1                           mov eax, ecx
00280F82  48 8D 88 C4 09 00 00            lea rcx, [rax + 0x9c4]
00280F89  48 8D 0C 48                     lea rcx, [rax + rcx*2]
00280F8D  49 8D 0C C8                     lea rcx, [r8 + rcx*8]
00280F91  48 89 51 08                     mov qword ptr [rcx + 8], rdx
00280F95  48 89 39                        mov qword ptr [rcx], rdi
00280F98  90                              nop
00280F99  F6 05 66 5B D4 00 21            test byte ptr [rip + 0xd45b66], 0x21
00280FA0  0F 85 DD 04 00 00               jne 0x140281483
00280FA6  48 8B C1                        mov rax, rcx
00280FA9  48 87 02                        xchg qword ptr [rdx], rax
00280FAC  48 85 C0                        test rax, rax
00280FAF  0F 84 9D 01 00 00               je 0x140281152
00280FB5  48 8B D0                        mov rdx, rax
00280FB8  E8 F3 6E FD FF                  call 0x140257eb0
00280FBD  E9 88 01 00 00                  jmp 0x14028114a
00280FC2  48 8B B4 24 B8 00 00 00         mov rsi, qword ptr [rsp + 0xb8]
00280FCA  48 8B 84 24 C0 00 00 00         mov rax, qword ptr [rsp + 0xc0]
00280FD2  48 89 30                        mov qword ptr [rax], rsi
00280FD5  49 8B C5                        mov rax, r13
00280FD8  48 83 C4 68                     add rsp, 0x68
00280FDC  41 5F                           pop r15
00280FDE  41 5E                           pop r14
00280FE0  41 5D                           pop r13
00280FE2  41 5C                           pop r12
00280FE4  5F                              pop rdi
00280FE5  5E                              pop rsi
00280FE6  5D                              pop rbp
00280FE7  5B                              pop rbx
00280FE8  C3                              ret
00280FE9  CC                              int3
00280FEA  48 F7 05 93 5A D4 00 00 00 60 00  test qword ptr [rip + 0xd45a93], 0x600000
00280FF5  0F 84 86 FE FF FF               je 0x140280e81
00280FFB  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00281004  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
0028100B  80 B9 60 01 00 00 01            cmp byte ptr [rcx + 0x160], 1
00281012  0F 84 69 FE FF FF               je 0x140280e81
00281018  48 8B 91 08 05 00 00            mov rdx, qword ptr [rcx + 0x508]
0028101F  48 85 D2                        test rdx, rdx
00281022  0F 84 59 FE FF FF               je 0x140280e81
00281028  48 8B C6                        mov rax, rsi
0028102B  48 C1 E8 03                     shr rax, 3
0028102F  25 FF 01 00 00                  and eax, 0x1ff
00281034  48 8B 04 C2                     mov rax, qword ptr [rdx + rax*8]
00281038  A8 20                           test al, 0x20
0028103A  74 04                           je 0x140281040
0028103C  48 83 CB 20                     or rbx, 0x20
00281040  48 8B CB                        mov rcx, rbx
00281043  48 83 CB 42                     or rbx, 0x42
00281047  A8 42                           test al, 0x42
00281049  48 0F 44 D9                     cmove rbx, rcx
0028104D  E9 2F FE FF FF                  jmp 0x140280e81
00281052  41 8B 81 B8 00 00 00            mov eax, dword ptr [r9 + 0xb8]
00281059  A8 0F                           test al, 0xf
0028105B  75 37                           jne 0x140281094
0028105D  49 8B C0                        mov rax, r8
00281060  48 3B F0                        cmp rsi, rax
00281063  72 2F                           jb 0x140281094
00281065  49 8B C3                        mov rax, r11
00281068  48 3B F0                        cmp rsi, rax
0028106B  77 27                           ja 0x140281094
0028106D  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00281076  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
0028107D  48 8B 81 10 04 00 00            mov rax, qword ptr [rcx + 0x410]
00281084  48 8B 88 68 05 00 00            mov rcx, qword ptr [rax + 0x568]
0028108B  48 85 C9                        test rcx, rcx
0028108E  0F 85 21 06 00 00               jne 0x1402816b5
00281094  41 8B 81 B8 00 00 00            mov eax, dword ptr [r9 + 0xb8]
0028109B  A8 0F                           test al, 0xf
0028109D  74 14                           je 0x1402810b3
0028109F  49 8B C0                        mov rax, r8
002810A2  48 3B F0                        cmp rsi, rax
002810A5  72 0C                           jb 0x1402810b3
002810A7  49 8B C3                        mov rax, r11
002810AA  48 3B F0                        cmp rsi, rax
002810AD  0F 86 9C 04 00 00               jbe 0x14028154f
002810B3  48 8B 1E                        mov rbx, qword ptr [rsi]
002810B6  8B EF                           mov ebp, edi
002810B8  49 8B C0                        mov rax, r8
002810BB  48 3B F0                        cmp rsi, rax
002810BE  72 21                           jb 0x1402810e1
002810C0  49 8B C2                        mov rax, r10
002810C3  48 3B F0                        cmp rsi, rax
002810C6  77 19                           ja 0x1402810e1
002810C8  F6 C3 01                        test bl, 1
002810CB  74 14                           je 0x1402810e1
002810CD  F6 C3 42                        test bl, 0x42
002810D0  0F 95 C1                        setne cl
002810D3  F6 C3 20                        test bl, 0x20
002810D6  0F 95 C0                        setne al
002810D9  84 C8                           test al, cl
002810DB  0F 84 1E 03 00 00               je 0x1402813ff
002810E1  49 BE FF FF FF FF FF FF FF DF   movabs r14, 0xdfffffffffffffff
002810EB  49 BF 20 00 00 00 00 00 00 10   movabs r15, 0x1000000000000020
002810F5  F6 C3 01                        test bl, 1
002810F8  74 35                           je 0x14028112f
002810FA  48 8B C3                        mov rax, rbx
002810FD  48 C1 E8 3C                     shr rax, 0x3c
00281101  A8 01                           test al, 1
00281103  0F 85 B5 03 00 00               jne 0x1402814be
00281109  48 8B CB                        mov rcx, rbx
0028110C  49 23 CE                        and rcx, r14
0028110F  49 0B CF                        or rcx, r15
00281112  48 F7 05 6B 59 D4 00 00 00 00 02  test qword ptr [rip + 0xd4596b], 0x2000000
0028111D  74 03                           je 0x140281122
0028111F  0F AE E8                        lfence
00281122  48 8B C3                        mov rax, rbx
00281125  F0 48 0F B1 0E                  lock cmpxchg qword ptr [rsi], rcx
0028112A  48 8B D8                        mov rbx, rax
0028112D  75 C6                           jne 0x1402810f5
0028112F  4C 8B 6C 24 38                  mov r13, qword ptr [rsp + 0x38]
00281134  4C 8B 74 24 30                  mov r14, qword ptr [rsp + 0x30]
00281139  4C 8D 3D C0 EE D7 FF            lea r15, [rip - 0x281140]
00281140  48 BD 68 DF BE 7D FB F6 FF FF   movabs rbp, 0xfffff6fb7dbedf68
0028114A  4C 8B 8C 24 B0 00 00 00         mov r9, qword ptr [rsp + 0xb0]
00281152  83 BC 24 C8 00 00 00 00         cmp dword ptr [rsp + 0xc8], 0
0028115A  0F 85 04 06 00 00               jne 0x140281764
00281160  48 8B C5                        mov rax, rbp
00281163  4C 3B E8                        cmp r13, rax
00281166  0F 84 CB 00 00 00               je 0x140281237
0028116C  41 8B 81 B8 00 00 00            mov eax, dword ptr [r9 + 0xb8]
00281173  49 B8 00 D0 BE 7D FB F6 FF FF   movabs r8, 0xfffff6fb7dbed000
0028117D  A8 0F                           test al, 0xf
0028117F  74 35                           je 0x1402811b6
00281181  48 BA FF DF BE 7D FB F6 FF FF   movabs rdx, 0xfffff6fb7dbedfff
0028118B  41 8B 81 B8 00 00 00            mov eax, dword ptr [r9 + 0xb8]
00281192  A8 0F                           test al, 0xf
00281194  0F 85 67 01 00 00               jne 0x140281301
0028119A  48 B8 FF FF FF FF FF FF FF CF   movabs rax, 0xcfffffffffffffff
002811A4  F0 49 21 45 00                  lock and qword ptr [r13], rax
002811A9  4C 8B EE                        mov r13, rsi
002811AC  48 89 74 24 38                  mov qword ptr [rsp + 0x38], rsi
002811B1  E9 7F FD FF FF                  jmp 0x140280f35
002811B6  49 8B C0                        mov rax, r8
002811B9  48 BA FF DF BE 7D FB F6 FF FF   movabs rdx, 0xfffff6fb7dbedfff
002811C3  4C 3B E8                        cmp r13, rax
002811C6  72 C3                           jb 0x14028118b
002811C8  48 8B C2                        mov rax, rdx
002811CB  4C 3B E8                        cmp r13, rax
002811CE  77 BB                           ja 0x14028118b
002811D0  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
002811D9  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
002811E0  48 8B 81 10 04 00 00            mov rax, qword ptr [rcx + 0x410]
002811E7  48 8B 88 68 05 00 00            mov rcx, qword ptr [rax + 0x568]
002811EE  48 85 C9                        test rcx, rcx
002811F1  74 98                           je 0x14028118b
002811F3  49 C1 ED 03                     shr r13, 3
002811F7  41 81 E5 FF 01 00 00            and r13d, 0x1ff
002811FE  42 8B 04 A9                     mov eax, dword ptr [rcx + r13*4]
00281202  4A 8D 0C A9                     lea rcx, [rcx + r13*4]
00281206  A9 FF FF FF 3F                  test eax, 0x3fffffff
0028120B  0F 85 CA 01 00 00               jne 0x1402813db
00281211  85 C0                           test eax, eax
00281213  0F 89 43 04 00 00               jns 0x14028165c
00281219  F6 05 E6 58 D4 00 01            test byte ptr [rip + 0xd458e6], 1
00281220  0F 85 A7 04 00 00               jne 0x1402816cd
00281226  33 FF                           xor edi, edi
00281228  48 89 74 24 38                  mov qword ptr [rsp + 0x38], rsi
0028122D  89 39                           mov dword ptr [rcx], edi
0028122F  4C 8B EE                        mov r13, rsi
00281232  E9 FE FC FF FF                  jmp 0x140280f35
00281237  65 48 8B 14 25 20 00 00 00      mov rdx, qword ptr gs:[0x20]
00281240  41 8B 81 B8 00 00 00            mov eax, dword ptr [r9 + 0xb8]
00281247  24 0F                           and al, 0xf
00281249  0F 85 18 02 00 00               jne 0x140281467
0028124F  B9 30 00 00 00                  mov ecx, 0x30
00281254  33 FF                           xor edi, edi
00281256  48 8D 9A 40 9C 00 00            lea rbx, [rdx + 0x9c40]
0028125D  48 03 D9                        add rbx, rcx
00281260  F6 05 9F 58 D4 00 01            test byte ptr [rip + 0xd4589f], 1
00281267  0F 85 43 01 00 00               jne 0x1402813b0
0028126D  0F 0D 0B                        prefetchw byte ptr [rbx]
00281270  48 8B 03                        mov rax, qword ptr [rbx]
00281273  48 85 C0                        test rax, rax
00281276  75 1A                           jne 0x140281292
00281278  48 8B 4B 08                     mov rcx, qword ptr [rbx + 8]
0028127C  48 8B C3                        mov rax, rbx
0028127F  F0 48 0F B1 39                  lock cmpxchg qword ptr [rcx], rdi
00281284  0F 84 1F FF FF FF               je 0x1402811a9
0028128A  48 8B CB                        mov rcx, rbx
0028128D  E8 0E 68 F9 FF                  call 0x140217aa0
00281292  4C 8D 40 08                     lea r8, [rax + 8]
00281296  48 89 3B                        mov qword ptr [rbx], rdi
00281299  48 8B 4B 08                     mov rcx, qword ptr [rbx + 8]
0028129D  48 8B C1                        mov rax, rcx
002812A0  49 87 00                        xchg qword ptr [r8], rax
002812A3  32 C1                           xor al, cl
002812A5  A8 04                           test al, 4
002812A7  0F 84 FC FE FF FF               je 0x1402811a9
002812AD  F0 83 0C 24 00                  lock or dword ptr [rsp], 0
002812B2  49 C1 E8 05                     shr r8, 5
002812B6  41 83 E0 7F                     and r8d, 0x7f
002812BA  E8 21 69 F9 FF                  call 0x140217be0
002812BF  48 8B D7                        mov rdx, rdi
002812C2  0F B6 D8                        movzx ebx, al
002812C5  4B 87 94 C7 20 1B F2 00         xchg qword ptr [r15 + r8*8 + 0xf21b20], rdx
002812CD  E8 22 68 F9 FF                  call 0x140217af4
002812D2  84 DB                           test bl, bl
002812D4  0F 84 CF FE FF FF               je 0x1402811a9
002812DA  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
002812E3  4C 8B 81 B8 8E 00 00            mov r8, qword ptr [rcx + 0x8eb8]
002812EA  4D 85 C0                        test r8, r8
002812ED  0F 85 06 03 00 00               jne 0x1402815f9
002812F3  FB                              sti
002812F4  4C 8B EE                        mov r13, rsi
002812F7  48 89 74 24 38                  mov qword ptr [rsp + 0x38], rsi
002812FC  E9 34 FC FF FF                  jmp 0x140280f35
00281301  49 8B C0                        mov rax, r8
00281304  4C 3B E8                        cmp r13, rax
00281307  0F 82 8D FE FF FF               jb 0x14028119a
0028130D  48 8B C2                        mov rax, rdx
00281310  4C 3B E8                        cmp r13, rax
00281313  0F 87 81 FE FF FF               ja 0x14028119a
00281319  49 8B C0                        mov rax, r8
0028131C  4C 2B E8                        sub r13, rax
0028131F  BA 02 00 00 00                  mov edx, 2
00281324  41 8B 81 B8 00 00 00            mov eax, dword ptr [r9 + 0xb8]
0028132B  49 C1 FD 03                     sar r13, 3
0028132F  46 8D 04 6D 00 00 00 00         lea r8d, [r13*2]
00281337  41 8B C8                        mov ecx, r8d
0028133A  41 8B C0                        mov eax, r8d
0028133D  83 E1 1F                        and ecx, 0x1f
00281340  D3 E2                           shl edx, cl
00281342  F7 D2                           not edx
00281344  0F B3 CA                        btr edx, ecx
00281347  48 C1 E8 05                     shr rax, 5
0028134B  F0 41 21 94 87 AC F1 E2 00      lock and dword ptr [r15 + rax*4 + 0xe2f1ac], edx
00281354  4C 8B EE                        mov r13, rsi
00281357  48 89 74 24 38                  mov qword ptr [rsp + 0x38], rsi
0028135C  E9 D4 FB FF FF                  jmp 0x140280f35
00281361  3C 07                           cmp al, 7
00281363  0F 84 9C 01 00 00               je 0x140281505
00281369  3C 05                           cmp al, 5
0028136B  B9 03 00 00 00                  mov ecx, 3
00281370  0F 44 CF                        cmove ecx, edi
00281373  8B C1                           mov eax, ecx
00281375  48 8D 14 C5 C0 FD E2 00         lea rdx, [rax*8 + 0xe2fdc0]
0028137D  49 03 D7                        add rdx, r15
00281380  E9 FB FB FF FF                  jmp 0x140280f80
00281385  3C 07                           cmp al, 7
00281387  0F 84 8F 01 00 00               je 0x14028151c
0028138D  3C 05                           cmp al, 5
0028138F  B9 03 00 00 00                  mov ecx, 3
00281394  0F 44 CF                        cmove ecx, edi
00281397  8B C1                           mov eax, ecx
00281399  4C 8D 3D 60 EC D7 FF            lea r15, [rip - 0x2813a0]
002813A0  4D 8D 87 C0 FD E2 00            lea r8, [r15 + 0xe2fdc0]
002813A7  4D 8D 04 C0                     lea r8, [r8 + rax*8]
002813AB  E9 34 FA FF FF                  jmp 0x140280de4
002813B0  8B 05 A2 CA C8 00               mov eax, dword ptr [rip + 0xc8caa2]
002813B6  85 C0                           test eax, eax
002813B8  0F 85 AF FE FF FF               jne 0x14028126d
002813BE  48 8B 94 24 A8 00 00 00         mov rdx, qword ptr [rsp + 0xa8]
002813C6  48 8B CB                        mov rcx, rbx
002813C9  E8 22 66 F9 FF                  call 0x1402179f0
002813CE  4C 8B EE                        mov r13, rsi
002813D1  48 89 74 24 38                  mov qword ptr [rsp + 0x38], rsi
002813D6  E9 5A FB FF FF                  jmp 0x140280f35
002813DB  F6 05 24 57 D4 00 01            test byte ptr [rip + 0xd45724], 1
002813E2  0F 85 37 03 00 00               jne 0x14028171f
002813E8  F0 81 21 FF FF FF BF            lock and dword ptr [rcx], 0xbfffffff
002813EF  F0 FF 09                        lock dec dword ptr [rcx]
002813F2  4C 8B EE                        mov r13, rsi
002813F5  48 89 74 24 38                  mov qword ptr [rsp + 0x38], rsi
002813FA  E9 36 FB FF FF                  jmp 0x140280f35
002813FF  48 F7 05 7E 56 D4 00 00 00 60 00  test qword ptr [rip + 0xd4567e], 0x600000
0028140A  0F 84 D1 FC FF FF               je 0x1402810e1
00281410  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00281419  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
00281420  80 B9 60 01 00 00 01            cmp byte ptr [rcx + 0x160], 1
00281427  0F 84 B4 FC FF FF               je 0x1402810e1
0028142D  48 8B 91 08 05 00 00            mov rdx, qword ptr [rcx + 0x508]
00281434  48 85 D2                        test rdx, rdx
00281437  0F 84 A4 FC FF FF               je 0x1402810e1
0028143D  48 8B C6                        mov rax, rsi
00281440  48 C1 E8 03                     shr rax, 3
00281444  25 FF 01 00 00                  and eax, 0x1ff
00281449  48 8B 04 C2                     mov rax, qword ptr [rdx + rax*8]
0028144D  A8 20                           test al, 0x20
0028144F  74 04                           je 0x140281455
00281451  48 83 CB 20                     or rbx, 0x20
00281455  48 8B CB                        mov rcx, rbx
00281458  48 83 CB 42                     or rbx, 0x42
0028145C  A8 42                           test al, 0x42
0028145E  48 0F 44 D9                     cmove rbx, rcx
00281462  E9 7A FC FF FF                  jmp 0x1402810e1
00281467  3C 07                           cmp al, 7
00281469  0F 84 7E 01 00 00               je 0x1402815ed
0028146F  3C 05                           cmp al, 5
00281471  B9 48 00 00 00                  mov ecx, 0x48
00281476  BF 00 00 00 00                  mov edi, 0
0028147B  0F 44 CF                        cmove ecx, edi
0028147E  E9 D3 FD FF FF                  jmp 0x140281256
00281483  8B 05 CF C9 C8 00               mov eax, dword ptr [rip + 0xc8c9cf]
00281489  85 C0                           test eax, eax
0028148B  0F 85 15 FB FF FF               jne 0x140280fa6
00281491  E8 BA 43 FF FF                  call 0x140275850
00281496  E9 AF FC FF FF                  jmp 0x14028114a
0028149B  8B 05 B7 C9 C8 00               mov eax, dword ptr [rip + 0xc8c9b7]
002814A1  85 C0                           test eax, eax
002814A3  0F 85 61 F9 FF FF               jne 0x140280e0a
002814A9  49 8B D0                        mov rdx, r8
002814AC  E8 9F 43 FF FF                  call 0x140275850
002814B1  4C 8B 8C 24 B0 00 00 00         mov r9, qword ptr [rsp + 0xb0]
002814B9  E9 5B F9 FF FF                  jmp 0x140280e19
002814BE  A8 02                           test al, 2
002814C0  75 6E                           jne 0x140281530
002814C2  48 8B FB                        mov rdi, rbx
002814C5  48 B8 00 00 00 00 00 00 00 20   movabs rax, 0x2000000000000000
002814CF  48 0B F8                        or rdi, rax
002814D2  48 F7 05 AB 55 D4 00 00 00 00 02  test qword ptr [rip + 0xd455ab], 0x2000000
002814DD  74 03                           je 0x1402814e2
002814DF  0F AE E8                        lfence
002814E2  48 0F BA 25 9D 55 D4 00 24      bt qword ptr [rip + 0xd4559d], 0x24
002814EB  0F 82 87 01 00 00               jb 0x140281678
002814F1  48 8B C3                        mov rax, rbx
002814F4  F0 48 0F B1 3E                  lock cmpxchg qword ptr [rsi], rdi
002814F9  48 8B D8                        mov rbx, rax
002814FC  48 0F 44 DF                     cmove rbx, rdi
00281500  E9 F0 FB FF FF                  jmp 0x1402810f5
00281505  B9 01 00 00 00                  mov ecx, 1
0028150A  8B C1                           mov eax, ecx
0028150C  48 8D 14 C5 C0 FD E2 00         lea rdx, [rax*8 + 0xe2fdc0]
00281514  49 03 D7                        add rdx, r15
00281517  E9 64 FA FF FF                  jmp 0x140280f80
0028151C  B9 01 00 00 00                  mov ecx, 1
00281521  E9 71 FE FF FF                  jmp 0x140281397
00281526  66 66 0F 1F 84 00 00 00 00 00   nop word ptr [rax + rax]
00281530  FF C5                           inc ebp
00281532  85 2D 74 3D D4 00               test dword ptr [rip + 0xd43d74], ebp
00281538  0F 84 88 00 00 00               je 0x1402815c6
0028153E  F3 90                           pause
00281540  48 8B 1E                        mov rbx, qword ptr [rsi]
00281543  48 0F BA E3 3C                  bt rbx, 0x3c
00281548  72 E6                           jb 0x140281530
0028154A  E9 A6 FB FF FF                  jmp 0x1402810f5
0028154F  44 8B E7                        mov r12d, edi
00281552  49 8B C0                        mov rax, r8
00281555  48 8B CE                        mov rcx, rsi
00281558  BD 01 00 00 00                  mov ebp, 1
0028155D  48 2B C8                        sub rcx, rax
00281560  41 8B 81 B8 00 00 00            mov eax, dword ptr [r9 + 0xb8]
00281567  48 C1 F9 03                     sar rcx, 3
0028156B  03 C9                           add ecx, ecx
0028156D  8B C1                           mov eax, ecx
0028156F  8B F9                           mov edi, ecx
00281571  48 C1 E8 05                     shr rax, 5
00281575  83 E7 1F                        and edi, 0x1f
00281578  8B CF                           mov ecx, edi
0028157A  D3 E5                           shl ebp, cl
0028157C  48 8D 1C 85 AC F1 E2 00         lea rbx, [rax*4 + 0xe2f1ac]
00281584  49 03 DF                        add rbx, r15
00281587  41 BF 02 00 00 00               mov r15d, 2
0028158D  41 D3 E7                        shl r15d, cl
00281590  45 8B F7                        mov r14d, r15d
00281593  41 F7 D6                        not r14d
00281596  8B 13                           mov edx, dword ptr [rbx]
00281598  8B CF                           mov ecx, edi
0028159A  8B C2                           mov eax, edx
0028159C  D3 E8                           shr eax, cl
0028159E  A8 01                           test al, 1
002815A0  0F 85 8D 00 00 00               jne 0x140281633
002815A6  8B CA                           mov ecx, edx
002815A8  8B C2                           mov eax, edx
002815AA  0B CD                           or ecx, ebp
002815AC  41 23 CE                        and ecx, r14d
002815AF  F0 0F B1 0B                     lock cmpxchg dword ptr [rbx], ecx
002815B3  8B D0                           mov edx, eax
002815B5  75 E1                           jne 0x140281598
002815B7  49 BC 00 00 00 00 80 F6 FF FF   movabs r12, 0xfffff68000000000
002815C1  E9 6E FB FF FF                  jmp 0x140281134
002815C6  8B 05 EC 54 D4 00               mov eax, dword ptr [rip + 0xd454ec]
002815CC  A8 40                           test al, 0x40
002815CE  0F 84 6A FF FF FF               je 0x14028153e
002815D4  E8 B7 DE 08 00                  call 0x14030f490
002815D9  84 C0                           test al, al
002815DB  0F 84 5D FF FF FF               je 0x14028153e
002815E1  8B CD                           mov ecx, ebp
002815E3  E8 78 DE 08 00                  call 0x14030f460
002815E8  E9 53 FF FF FF                  jmp 0x140281540
002815ED  B9 18 00 00 00                  mov ecx, 0x18
002815F2  33 FF                           xor edi, edi
002815F4  E9 5D FC FF FF                  jmp 0x140281256
002815F9  41 0F 0D 08                     prefetchw byte ptr [r8]
002815FD  41 8B 00                        mov eax, dword ptr [r8]
00281600  8B D0                           mov edx, eax
00281602  0F BA F2 15                     btr edx, 0x15
00281606  F0 41 0F B1 10                  lock cmpxchg dword ptr [r8], edx
0028160B  75 F3                           jne 0x140281600
0028160D  0F BA E0 15                     bt eax, 0x15
00281611  0F 83 DC FC FF FF               jae 0x1402812f3
00281617  E8 B4 1B FE FF                  call 0x1402631d0
0028161C  E9 D2 FC FF FF                  jmp 0x1402812f3
00281621  E8 8A 68 FD FF                  call 0x140257eb0
00281626  4C 8B 8C 24 B0 00 00 00         mov r9, qword ptr [rsp + 0xb0]
0028162E  E9 E6 F7 FF FF                  jmp 0x140280e19
00281633  A8 02                           test al, 2
00281635  0F 85 C5 00 00 00               jne 0x140281700
0028163B  8B CA                           mov ecx, edx
0028163D  8B C2                           mov eax, edx
0028163F  41 0B CF                        or ecx, r15d
00281642  F0 0F B1 0B                     lock cmpxchg dword ptr [rbx], ecx
00281646  8B D0                           mov edx, eax
00281648  0F 44 D1                        cmove edx, ecx
0028164B  E9 48 FF FF FF                  jmp 0x140281598
00281650  4C 8D 3D A9 E9 D7 FF            lea r15, [rip - 0x281657]
00281657  E9 BD F7 FF FF                  jmp 0x140280e19
0028165C  33 FF                           xor edi, edi
0028165E  48 8B D1                        mov rdx, rcx
00281661  45 33 C9                        xor r9d, r9d
00281664  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
00281669  41 B8 00 01 00 00               mov r8d, 0x100
0028166F  8D 4F 10                        lea ecx, [rdi + 0x10]
00281672  E8 E9 BF 27 00                  call 0x1404fd660
00281677  CC                              int3
00281678  40 0F B6 C7                     movzx eax, dil
0028167C  24 21                           and al, 0x21
0028167E  3C 01                           cmp al, 1
00281680  0F 85 6B FE FF FF               jne 0x1402814f1
00281686  49 8B C4                        mov rax, r12
00281689  48 B9 00 00 00 00 40 00 00 00   movabs rcx, 0x4000000000
00281693  48 03 C1                        add rax, rcx
00281696  48 3B F0                        cmp rsi, rax
00281699  0F 82 52 FE FF FF               jb 0x1402814f1
0028169F  41 B8 80 00 00 00               mov r8d, 0x80
002816A5  48 8B D7                        mov rdx, rdi
002816A8  48 8B CE                        mov rcx, rsi
002816AB  E8 D0 16 01 00                  call 0x140292d80
002816B0  E9 3C FE FF FF                  jmp 0x1402814f1
002816B5  8B C6                           mov eax, esi
002816B7  C1 E8 03                        shr eax, 3
002816BA  25 FF 01 00 00                  and eax, 0x1ff
002816BF  48 8D 0C 81                     lea rcx, [rcx + rax*4]
002816C3  E8 B8 77 FC FF                  call 0x140248e80
002816C8  E9 7D FA FF FF                  jmp 0x14028114a
002816CD  8B 05 85 C7 C8 00               mov eax, dword ptr [rip + 0xc8c785]
002816D3  85 C0                           test eax, eax
002816D5  0F 85 4B FB FF FF               jne 0x140281226
002816DB  48 8B 94 24 A8 00 00 00         mov rdx, qword ptr [rsp + 0xa8]
002816E3  E8 5C F8 03 00                  call 0x1402c0f44
002816E8  4C 8B EE                        mov r13, rsi
002816EB  48 89 74 24 38                  mov qword ptr [rsp + 0x38], rsi
002816F0  E9 40 F8 FF FF                  jmp 0x140280f35
002816F5  66 66 66 0F 1F 84 00 00 00 00 00  nop word ptr [rax + rax]
00281700  41 FF C4                        inc r12d
00281703  44 85 25 A2 3B D4 00            test dword ptr [rip + 0xd43ba2], r12d
0028170A  74 3B                           je 0x140281747
0028170C  F3 90                           pause
0028170E  8B 13                           mov edx, dword ptr [rbx]
00281710  8B CF                           mov ecx, edi
00281712  8B C2                           mov eax, edx
00281714  D3 E8                           shr eax, cl
00281716  A8 01                           test al, 1
00281718  75 E6                           jne 0x140281700
0028171A  E9 79 FE FF FF                  jmp 0x140281598
0028171F  8B 05 33 C7 C8 00               mov eax, dword ptr [rip + 0xc8c733]
00281725  85 C0                           test eax, eax
00281727  0F 85 BB FC FF FF               jne 0x1402813e8
0028172D  48 8B 94 24 A8 00 00 00         mov rdx, qword ptr [rsp + 0xa8]
00281735  E8 0E F8 06 00                  call 0x1402f0f48
0028173A  4C 8B EE                        mov r13, rsi
0028173D  48 89 74 24 38                  mov qword ptr [rsp + 0x38], rsi
00281742  E9 EE F7 FF FF                  jmp 0x140280f35
00281747  8B 05 6B 53 D4 00               mov eax, dword ptr [rip + 0xd4536b]
0028174D  A8 40                           test al, 0x40
0028174F  74 BB                           je 0x14028170c
00281751  E8 3A DD 08 00                  call 0x14030f490
00281756  84 C0                           test al, al
00281758  74 B2                           je 0x14028170c
0028175A  41 8B CC                        mov ecx, r12d
0028175D  E8 FE DC 08 00                  call 0x14030f460
00281762  EB AA                           jmp 0x14028170e
00281764  48 8B C5                        mov rax, rbp
00281767  4C 3B E8                        cmp r13, rax
0028176A  0F 84 39 FA FF FF               je 0x1402811a9
00281770  E9 EB F9 FF FF                  jmp 0x140281160
00281775  48 8D 0D 44 5D BB 00            lea rcx, [rip + 0xbb5d44]
0028177C  BD 01 00 00 00                  mov ebp, 1
00281781  E8 FA 76 FC FF                  call 0x140248e80
00281786  4C 8B 8C 24 B0 00 00 00         mov r9, qword ptr [rsp + 0xb0]
0028178E  49 B8 00 D0 BE 7D FB F6 FF FF   movabs r8, 0xfffff6fb7dbed000
00281798  49 BA F8 D7 BE 7D FB F6 FF FF   movabs r10, 0xfffff6fb7dbed7f8
002817A2  49 BB FF DF BE 7D FB F6 FF FF   movabs r11, 0xfffff6fb7dbedfff
002817AC  48 B9 FF FF FF FF FF F6 FF FF   movabs rcx, 0xfffff6ffffffffff
002817B6  E9 20 F7 FF FF                  jmp 0x140280edb
002817BB  48 8B C1                        mov rax, rcx
002817BE  48 3B F8                        cmp rdi, rax
002817C1  0F 87 20 F7 FF FF               ja 0x140280ee7
002817C7  E9 9A 89 45 00                  jmp 0x1406da166
002817CC  48 8D 0D ED 5C BB 00            lea rcx, [rip + 0xbb5ced]
002817D3  E8 08 80 FC FF                  call 0x1402497e0
002817D8  4C 8B 8C 24 B0 00 00 00         mov r9, qword ptr [rsp + 0xb0]
002817E0  49 B8 00 D0 BE 7D FB F6 FF FF   movabs r8, 0xfffff6fb7dbed000
002817EA  49 BA F8 D7 BE 7D FB F6 FF FF   movabs r10, 0xfffff6fb7dbed7f8
002817F4  49 BB FF DF BE 7D FB F6 FF FF   movabs r11, 0xfffff6fb7dbedfff
002817FE  E9 21 F7 FF FF                  jmp 0x140280f24
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiLockLowestValidPageTableEx(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned int v_stack_p0;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p8;
    unsigned __int64 v_stack_pA8;
    unsigned __int64 v_stack_pB0;
    unsigned int v_stack_pC8;

    v_stack_p20 = a4;
    v_stack_p18 = a3;
    v_stack_p10 = a2;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (104);
    v_r10 = (a2) >> (9);
    v_rdi = 0;
    v_r10 = (v_r10) & (a1);
    *(unsigned __int64 *)(a3) = 0;
    v_r10 = (v_r10) + (v_r12);
    v_stack_m68 = v_r10;
    v_r10 = (v_r10) >> (9);
    v_r10 = (v_r10) & (a1);
    v_r10 = (v_r10) + (v_r12);
    v_stack_m60 = v_r10;
    v_r10 = (v_r10) >> (9);
    v_r10 = (v_r10) & (a1);
    v_r10 = (v_r10) + (v_r12);
    v_stack_m58 = v_r10;
    v_r10 = (v_r10) >> (9);
    v_r10 = (v_r10) & (a1);
    v_r10 = (v_r10) + (v_r12);
    v_stack_m50 = v_r10;
    v_stack_m70 = v_rbp;
    if ((unsigned int)((unsigned int)(a4)) != 0) goto loc_00281650;
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(a1 + 184))) & (15));
    if (condition_is_not_equal) goto loc_00281385;
loc_00280DE4:
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2 + 2 + 2500 * 2 * 8 + 8) = a1 + 176;
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2 + 2 + 2500 * 2 * 8) = 0;
    if (((*(unsigned __int8 *)(v_rip + 13917442)) & (33)) != 0) goto loc_0028149B;
loc_00280E0A:
    if (*(unsigned __int64 *)(gs_base + (0 + 32)) + 2 + 2 + 2500 * 2 * 8 != 0) goto loc_00281621;
loc_00280E19:
loc_00280E1F:
    v_stack_m78 = 2;
    if ((*(unsigned __int64 *)(v_rsp + 2 * 8 + 64)) < (a1 + 176)) goto loc_00280E8B;
    if ((*(unsigned __int64 *)(v_rsp + 2 * 8 + 64)) > v_r10) goto loc_00280E8B;
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp + 2 * 8 + 64)))) & (1)) == 0) goto loc_00280FCA;
    a1 = ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp + 2 * 8 + 64)))) & (66)) != 0) ? 1 : 0;
    result = ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp + 2 * 8 + 64)))) & (32)) != 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) == 0) goto loc_00280FEA;
loc_00280E81:
loc_00280E8B:
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp + 2 * 8 + 64)))) & (1)) == 0) goto loc_00280FCA;
    if (sign_flag) goto loc_00280FCA;
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp + 2 * 8 + 64)))) & (32)) != 0) goto loc_00280F30;
    v_rdi = (*(unsigned __int64 *)(v_rsp + 2 * 8 + 64)) << (25);
    result = (v_r12) << (25);
    v_rdi = (v_rdi) - (result);
    v_rdi = (v_rdi) >> (16);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 184)))) & (15)) == 0) goto loc_00280EDB;
    if ((*(unsigned __int64 *)(v_rsp + 2 * 8 + 64)) < (a1 + 176)) goto loc_00280EDB;
    if ((*(unsigned __int64 *)(v_rsp + 2 * 8 + 64)) <= ((unsigned int)(a4))) goto loc_00281775;
loc_00280EDB:
    if (v_rdi >= v_r12) goto loc_002817BB;
loc_00280EE7:
    v_rbx = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp + 2 * 8 + 64))) | (32);
    result = MiWriteValidPteNewProtection(*(unsigned __int64 *)(v_rsp + 2 * 8 + 64), v_rbx, a1 + 176, a1);
    if (0 != 0) goto loc_002817CC;
loc_00280F24:
    v_rdi = 0;
loc_00280F30:
    if ((*(unsigned __int64 *)(v_rsp + 2 * 8 + 64)) != v_rbp) goto loc_00280F50;
loc_00280F35:
    if (2 == 0) goto loc_00280FC2;
    v_r14 = (2) - 1;
    v_rdi = 0;
    goto loc_00280E1F;
loc_00280F50:
    if ((*(unsigned __int64 *)(v_rsp + 2 * 8 + 64)) != 0) goto loc_00281052;
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(v_stack_p8 + 184))) & (15));
    if (condition_is_not_equal) goto loc_00281361;
loc_00280F80:
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2 + 2 + 2500 * 2 * 8 + 8) = v_stack_p8 + 176;
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2 + 2 + 2500 * 2 * 8) = 0;
    if (((*(unsigned __int8 *)(v_rip + 13917030)) & (33)) != 0) goto loc_00281483;
loc_00280FA6:
    if (*(unsigned __int64 *)(gs_base + (0 + 32)) + 2 + 2 + 2500 * 2 * 8 == 0) goto loc_00281152;
    result = KxWaitForLockOwnerShip(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2 + 2 + 2500 * 2 * 8, *(unsigned __int64 *)(gs_base + (0 + 32)) + 2 + 2 + 2500 * 2 * 8, *(unsigned __int64 *)(gs_base + (0 + 32)), v_stack_p8);
    goto loc_0028114A;
loc_00280FC2:
loc_00280FCA:
    *(unsigned __int64 *)(v_stack_p18) = v_stack_p10;
    v_rsp = (v_rsp) + (104);
    return v_rbp;
loc_00280FEA:
    if (((*(unsigned __int64 *)(v_rip + 13916819)) & (0x600000ULL)) == 0) goto loc_00280E81;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 352)) == 1) goto loc_00280E81;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) == 0) goto loc_00280E81;
    result = (v_stack_p10) >> (3);
    result = (unsigned int)((result) & (511));
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + result * 8))) & (32)) != 0) {
        v_rbx = (v_rbx) | (32);
    }
    v_rbx = (v_rbx) | (66);
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + result * 8))) & (66)) == 0) { v_rbx = v_rbx; }
    goto loc_00280E81;
loc_00281052:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p8 + 184)))) & (15)) != 0) goto loc_00281094;
    if (v_stack_p10 < (*(unsigned __int64 *)(gs_base + (0 + 32)))) goto loc_00281094;
    if (v_stack_p10 > ((unsigned int)(a4))) goto loc_00281094;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1040) + 1384) != 0) goto loc_002816B5;
loc_00281094:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p8 + 184)))) & (15)) == 0) goto loc_002810B3;
    if (v_stack_p10 < (*(unsigned __int64 *)(gs_base + (0 + 32)))) goto loc_002810B3;
    if (v_stack_p10 <= ((unsigned int)(a4))) goto loc_0028154F;
loc_002810B3:
    if (v_stack_p10 < (*(unsigned __int64 *)(gs_base + (0 + 32)))) goto loc_002810E1;
    if (v_stack_p10 > v_r10) goto loc_002810E1;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_p10))) & (1)) == 0) goto loc_002810E1;
    a1 = ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_p10))) & (66)) != 0) ? 1 : 0;
    result = ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_p10))) & (32)) != 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) == 0) goto loc_002813FF;
loc_002810E1:
loc_002810F5:
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_p10))) & (1)) == 0) goto loc_0028112F;
    result = (*(unsigned __int64 *)(v_stack_p10)) >> (60);
    if ((((unsigned __int8)(result)) & (1)) != 0) goto loc_002814BE;
    a1 = (*(unsigned __int64 *)(v_stack_p10)) & (v_r14);
    a1 = (a1) | (v_rip - 2624996);
    if (((*(unsigned __int64 *)(v_rip + 13916523)) & (0x2000000ULL)) != 0) {
    }
    if (((*(unsigned __int64 *)(v_rip + 13916523)) & (0x2000000ULL)) != 0) goto loc_002810F5;
loc_0028112F:
loc_00281134:
loc_0028114A:
loc_00281152:
    if (v_stack_pC8 != 0) goto loc_00281764;
loc_00281160:
    if (v_stack_p38 == 0) goto loc_00281237;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_pB0 + 184)))) & (15)) == 0) goto loc_002811B6;
loc_0028118B:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_pB0 + 184)))) & (15)) != 0) goto loc_00281301;
loc_0028119A:
loc_002811A9:
    v_stack_p38 = v_stack_p10;
    goto loc_00280F35;
loc_002811B6:
    if (v_stack_p10 < (*(unsigned __int64 *)(gs_base + (0 + 32)))) goto loc_0028118B;
    if (v_stack_p10 > (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288))) goto loc_0028118B;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1040) + 1384) == 0) goto loc_0028118B;
    v_r13 = (v_stack_p10) >> (3);
    v_r13 = (unsigned int)((v_r13) & (511));
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1040) + 1384) + v_r13 * 4)))) & (0x3FFFFFFFULL)) != 0) goto loc_002813DB;
    if (!sign_flag) goto loc_0028165C;
    if (((*(unsigned __int8 *)(v_rip + 13916390)) & (1)) != 0) goto loc_002816CD;
loc_00281226:
    v_rdi = 0;
    v_stack_p38 = v_stack_p10;
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1040) + 1384) + v_r13 * 4) = 0;
    goto loc_00280F35;
loc_00281237:
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(v_stack_pB0 + 184))) & (15));
    if (condition_is_not_equal) goto loc_00281467;
    v_rdi = 0;
loc_00281256:
    v_rbx = (*(unsigned __int64 *)(gs_base + (0 + 32)) + 40000) + (48);
    if (((*(unsigned __int8 *)(v_rip + 13916319)) & (1)) != 0) goto loc_002813B0;
loc_0028126D:
    if (*(unsigned __int64 *)(v_rbx) != 0) goto loc_00281292;
    if (*(unsigned __int64 *)(v_rbx) == 0) goto loc_002811A9;
    result = KxWaitForLockChainValid(v_rbx, *(unsigned __int64 *)(gs_base + (0 + 32)), *(unsigned __int64 *)(gs_base + (0 + 32)), v_stack_pB0);
loc_00281292:
    *(unsigned __int64 *)(v_rbx) = 0;
    result = (unsigned __int8)((*(unsigned __int64 *)(v_rbx + 8)) ^ ((unsigned __int8)(*(unsigned __int64 *)(v_rbx + 8))));
    if ((((unsigned __int8)(result)) & (4)) == 0) goto loc_002811A9;
    a3 = (result + 8) >> (5);
    a3 = (unsigned int)((a3) & (127));
    result = KeDisableInterrupts(*(unsigned __int64 *)(v_rbx + 8), *(unsigned __int64 *)(gs_base + (0 + 32)), a3, v_stack_pB0);
    result = KiHaltOnAddressWakeEntireList(*(unsigned __int64 *)(v_rbx + 8), 0, a3, v_stack_pB0);
    if ((unsigned __int8)((unsigned __int8)(result)) == 0) goto loc_002811A9;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536) != 0) goto loc_002815F9;
loc_002812F3:
    v_stack_p38 = v_stack_p10;
    goto loc_00280F35;
loc_00281301:
    if (v_stack_p10 < (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536))) goto loc_0028119A;
    if (v_stack_p10 > 0) goto loc_0028119A;
    v_r13 = (v_stack_p10) - (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536));
    v_r13 = (v_r13) >> (3);
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_r13 * 2))) & (31));
    a2 = (unsigned int)((2) << ((unsigned __int8)(a1)));
    a2 = (unsigned int)(~(a2));
    result = ((unsigned int)((unsigned int)(v_r13 * 2))) >> (5);
    v_stack_p38 = v_stack_p10;
    goto loc_00280F35;
loc_00281361:
    if (((unsigned __int8)(result)) == 7) goto loc_00281505;
    a1 = 3;
    if (((unsigned __int8)(result)) == 5) { a1 = 0; }
    a2 = ((unsigned int)((unsigned int)(a1)) * 8 + 14876096) + (v_rip - 2625856);
    goto loc_00280F80;
loc_00281385:
    if (((unsigned __int8)((unsigned int)((unsigned int)(a1)))) == 7) goto loc_0028151C;
    a1 = 3;
    if (((unsigned __int8)((unsigned int)((unsigned int)(a1)))) == 5) { a1 = 0; }
loc_00281397:
    goto loc_00280DE4;
loc_002813B0:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13159074))) != 0) goto loc_0028126D;
    result = KiReleaseQueuedSpinLockInstrumented((unsigned __int8)(result), v_stack_pA8, v_rip - 2626464 + 14876096 + (unsigned int)((unsigned int)(a1)) * 8, v_stack_pB0);
    v_stack_p38 = v_stack_p10;
    goto loc_00280F35;
loc_002813DB:
    if (((*(unsigned __int8 *)(v_rip + 13915940)) & (1)) != 0) goto loc_0028171F;
loc_002813E8:
    v_stack_p38 = v_stack_p10;
    goto loc_00280F35;
loc_002813FF:
    if (((*(unsigned __int64 *)(v_rip + 13915774)) & (0x600000ULL)) == 0) goto loc_002810E1;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 352)) == 1) goto loc_002810E1;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) == 0) goto loc_002810E1;
    result = (v_stack_p10) >> (3);
    result = (unsigned int)((result) & (511));
    v_rbx = (unsigned __int8)(result);
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + result * 8))) & (32)) != 0) {
        v_rbx = ((unsigned __int8)(result)) | (32);
    }
    v_rbx = (v_rbx) | (66);
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + result * 8))) & (66)) == 0) { v_rbx = v_rbx; }
    goto loc_002810E1;
loc_00281467:
    if (((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + result * 8))) == 7) goto loc_002815ED;
    a1 = 72;
    if (((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + result * 8))) == 5) { a1 = 0; }
    goto loc_00281256;
loc_00281483:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13158863))) != 0) goto loc_00280FA6;
    result = KiAcquireQueuedSpinLockInstrumented(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288), v_rip - 2626464 + 14876096 + (unsigned int)((unsigned int)(a1)) * 8, v_stack_pB0);
    goto loc_0028114A;
loc_0028149B:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13158839))) != 0) goto loc_00280E0A;
    result = KiAcquireQueuedSpinLockInstrumented(a1, v_rip - 2626464 + 14876096 + (unsigned int)((unsigned int)(a1)) * 8, v_rip - 2626464 + 14876096 + (unsigned int)((unsigned int)(a1)) * 8, v_stack_pB0);
    goto loc_00280E19;
loc_002814BE:
    if ((((unsigned __int8)(result)) & (2)) != 0) goto loc_00281530;
    v_rdi = (v_rbx) | (result);
    if (((*(unsigned __int64 *)(v_rip + 13915563)) & (0x2000000ULL)) != 0) {
    }
    if (condition_is_below) goto loc_00281678;
loc_002814F1:
    if (((*(unsigned __int64 *)(v_rip + 13915563)) & (0x2000000ULL)) == 0) { v_rbx = v_rdi; }
    goto loc_002810F5;
loc_00281505:
    a2 = (1 * 8 + 14876096) + (v_rip - 2626464);
    goto loc_00280F80;
loc_0028151C:
    goto loc_00281397;
loc_00281530:
    v_rbp = (unsigned int)((0) + 1);
    if (((*(unsigned int *)(v_rip + 13909364)) & ((unsigned int)(v_rbp))) == 0) goto loc_002815C6;
loc_0028153E:
loc_00281540:
    if (condition_is_below) goto loc_00281530;
    goto loc_002810F5;
loc_0028154F:
    a1 = (v_stack_p10) - (v_rip - 2626464 + 14876096 + (unsigned int)((unsigned int)(a1)) * 8);
    a1 = (a1) >> (3);
    a1 = (unsigned int)((a1) + ((unsigned int)(a1)));
    result = ((unsigned int)((unsigned int)(a1))) >> (5);
    v_rdi = (unsigned int)(((unsigned int)((unsigned int)(a1))) & (31));
    v_rbp = (unsigned int)((1) << ((unsigned __int8)((unsigned int)((unsigned int)(v_rdi)))));
    v_rbx = (result * 4 + 14873004) + (v_rip - 2626464);
    v_r15 = (unsigned int)((2) << ((unsigned __int8)((unsigned int)((unsigned int)(v_rdi)))));
    v_r14 = (unsigned int)(~((unsigned int)((unsigned int)(v_r15))));
loc_00281598:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx))))) >> ((unsigned __int8)((unsigned int)((unsigned int)(v_rdi)))));
    if ((((unsigned __int8)(result)) & (1)) != 0) goto loc_00281633;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx))))) | ((unsigned int)(v_rbp)));
    a1 = (unsigned int)((a1) & ((unsigned int)(v_r14)));
    if (condition_is_not_equal) goto loc_00281598;
    goto loc_00281134;
loc_002815C6:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13915372)))) & (64)) == 0) goto loc_0028153E;
    result = KiCheckVpBackingLongSpinWaitHypercall(a1, (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx)))))), v_rip - 2626464 + 14876096 + (unsigned int)((unsigned int)(a1)) * 8, v_stack_pB0);
    if ((unsigned __int8)(result) == 0) goto loc_0028153E;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rbp)), (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx)))))), v_rip - 2626464 + 14876096 + (unsigned int)((unsigned int)(a1)) * 8, v_stack_pB0);
    goto loc_00281540;
loc_002815ED:
    v_rdi = 0;
    goto loc_00281256;
loc_002815F9:
loc_00281600:
    if (condition_is_not_equal) goto loc_00281600;
    if (condition_is_above_or_equal) goto loc_002812F3;
    result = KiRemoveSystemWorkPriorityKick(24, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 2626464 + 14876096 + (unsigned int)((unsigned int)(a1)) * 8)))), v_rip - 2626464 + 14876096 + (unsigned int)((unsigned int)(a1)) * 8, v_stack_pB0);
    goto loc_002812F3;
loc_00281621:
    result = KxWaitForLockOwnerShip(24, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 2626464 + 14876096 + (unsigned int)((unsigned int)(a1)) * 8)))), v_rip - 2626464 + 14876096 + (unsigned int)((unsigned int)(a1)) * 8, v_stack_pB0);
    goto loc_00280E19;
loc_00281633:
    if ((((unsigned __int8)(result)) & (2)) != 0) goto loc_00281700;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 2626464 + 14876096 + (unsigned int)((unsigned int)(a1)) * 8))))))) | ((unsigned int)(v_r15)));
    a2 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 2626464 + 14876096 + (unsigned int)((unsigned int)(a1)) * 8))))))));
    if (condition_is_equal) { a2 = (unsigned int)(a1); }
    goto loc_00281598;
loc_00281650:
    goto loc_00280E19;
loc_0028165C:
    v_rdi = 0;
    a4 = 0;
    v_stack_p20 = 0;
    result = KeBugCheckEx(v_rdi + 16, a1, 256, a4);
loc_00281678:
    result = (unsigned __int8)((0) & (33));
    if (((unsigned __int8)(result)) != 1) goto loc_002814F1;
    result = ((unsigned int)((unsigned int)(v_rdi))) + (v_rdi + 16);
    if (v_stack_p10 < result) goto loc_002814F1;
    result = MiCheckLinearProtectedPteAccessedBit(v_stack_p10, 0, 128, a4);
    goto loc_002814F1;
loc_002816B5:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_stack_p10))) >> (3));
    result = (unsigned int)((result) & (511));
    result = ExAcquireSpinLockExclusiveAtDpcLevel(v_stack_p10 + result * 4, 0, 128, a4);
    goto loc_0028114A;
loc_002816CD:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13158277))) != 0) goto loc_00281226;
    result = ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented(v_stack_p10 + result * 4, v_stack_pA8, 128, a4);
    v_stack_p38 = v_stack_p10;
    goto loc_00280F35;
loc_00281700:
    v_r12 = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) + 1);
    if (((*(unsigned int *)(v_rip + 13908898)) & ((unsigned int)(v_r12))) == 0) goto loc_00281747;
loc_0028170C:
loc_0028170E:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx))))) >> (0));
    if ((((unsigned __int8)(result)) & (1)) != 0) goto loc_00281700;
    goto loc_00281598;
loc_0028171F:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13158195))) != 0) goto loc_002813E8;
    result = ExpReleaseSpinLockSharedFromDpcLevelInstrumented(0, v_stack_pA8, 128, a4);
    v_stack_p38 = v_stack_p10;
    goto loc_00280F35;
loc_00281747:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13914987)))) & (64)) == 0) goto loc_0028170C;
    result = KiCheckVpBackingLongSpinWaitHypercall(0, v_stack_pA8, 128, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0028170C;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_r12)), v_stack_pA8, 128, a4);
    goto loc_0028170E;
loc_00281764:
    if (v_stack_p10 == v_rbp) goto loc_002811A9;
    goto loc_00281160;
loc_00281775:
    result = ExAcquireSpinLockExclusiveAtDpcLevel(v_rip + 12279108, v_stack_pA8, 128, a4);
    goto loc_00280EDB;
loc_002817BB:
    if (0 > (v_rip + 12279108)) goto loc_00280EE7;
loc_002817CC:
    result = ExReleaseSpinLockExclusiveFromDpcLevel(v_rip + 12279021, v_stack_pA8, 128, v_stack_pB0);
    goto loc_00280F24;
}
```

## 5. (Beta) C Style

```c
int64_t MiLockLowestValidPageTableEx(void *Arg1, int64_t Arg2, void *Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint32_t v_stack_p0;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint32_t v_stack_p20;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p8;
    uint64_t v_stack_pA8;
    uint64_t v_stack_pB0;
    uint32_t v_stack_pC8;

    v_stack_p20 = Arg4;
    v_stack_p18 = Arg3;
    v_stack_p10 = Arg2;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (104);
    local_r10 = (Arg2) >> (9);
    local_rdi = 0;
    local_r10 = (local_r10) & (Arg1);
    *(uint64_t *)(arg3) = 0;
    local_r10 = (local_r10) + (local_r12);
    v_stack_m68 = local_r10;
    local_r10 = (local_r10) >> (9);
    local_r10 = (local_r10) & (Arg1);
    local_r10 = (local_r10) + (local_r12);
    v_stack_m60 = local_r10;
    local_r10 = (local_r10) >> (9);
    local_r10 = (local_r10) & (Arg1);
    local_r10 = (local_r10) + (local_r12);
    v_stack_m58 = local_r10;
    local_r10 = (local_r10) >> (9);
    local_r10 = (local_r10) & (Arg1);
    local_r10 = (local_r10) + (local_r12);
    v_stack_m50 = local_r10;
    v_stack_m70 = local_rbp;
    if ((uint32_t)((uint32_t)(Arg4)) != 0) goto loc_00281650;
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(arg1 + 0xB8))) & (15));
    if (condition_is_not_equal) goto loc_00281385;
loc_00280DE4:
    *(void **)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x2 + 0x2 + 0x9C4 * 2 * 8 + 0x8) = Arg1 + 176;
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x2 + 0x2 + 0x9C4 * 2 * 8) = 0;
    if (((*(uint8_t *)(v_rip + 0xD45D02)) & (33)) != 0) goto loc_0028149B;
loc_00280E0A:
    if (*(uint64_t *)(gs_base + (0 + 0x20)) + 2 + 2 + 2500 * 2 * 8 != 0) goto loc_00281621;
loc_00280E19:
loc_00280E1F:
    v_stack_m78 = 2;
    if ((*(uint64_t *)(local_rsp + 0x2 * 8 + 0x40)) < (Arg1 + 176)) goto loc_00280E8B;
    if ((*(uint64_t *)(local_rsp + 0x2 * 8 + 0x40)) > local_r10) goto loc_00280E8B;
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(local_rsp + 0x2 * 8 + 0x40)))) & (1)) == 0) goto loc_00280FCA;
    Arg1 = ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(local_rsp + 0x2 * 8 + 0x40)))) & (66)) != 0) ? 1 : 0;
    result = ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(local_rsp + 0x2 * 8 + 0x40)))) & (32)) != 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) == 0) goto loc_00280FEA;
loc_00280E81:
loc_00280E8B:
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(local_rsp + 0x2 * 8 + 0x40)))) & (1)) == 0) goto loc_00280FCA;
    if (sign_flag) goto loc_00280FCA;
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(local_rsp + 0x2 * 8 + 0x40)))) & (32)) != 0) goto loc_00280F30;
    local_rdi = (*(uint64_t *)(local_rsp + 0x2 * 8 + 0x40)) << (25);
    result = (local_r12) << (25);
    local_rdi = (local_rdi) - (result);
    local_rdi = (local_rdi) >> (16);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0xB8)))) & (15)) == 0) goto loc_00280EDB;
    if ((*(uint64_t *)(local_rsp + 0x2 * 8 + 0x40)) < (Arg1 + 176)) goto loc_00280EDB;
    if ((*(uint64_t *)(local_rsp + 0x2 * 8 + 0x40)) <= ((uint32_t)(Arg4))) goto loc_00281775;
loc_00280EDB:
    if (local_rdi >= local_r12) goto loc_002817BB;
loc_00280EE7:
    local_rbx = (*(uint64_t *)(*(uint64_t *)(local_rsp + 0x2 * 8 + 0x40))) | (32);
    result = MiWriteValidPteNewProtection(*(uint64_t *)(local_rsp + 0x2 * 8 + 0x40), local_rbx, Arg1 + 176, Arg1);
    if (0 != 0) goto loc_002817CC;
loc_00280F24:
    local_rdi = 0;
loc_00280F30:
    if ((*(uint64_t *)(local_rsp + 0x2 * 8 + 0x40)) != local_rbp) goto loc_00280F50;
loc_00280F35:
    if (2 == 0) goto loc_00280FC2;
    local_r14 = (2) - 1;
    local_rdi = 0;
    goto loc_00280E1F;
loc_00280F50:
    if ((*(uint64_t *)(local_rsp + 0x2 * 8 + 0x40)) != 0) goto loc_00281052;
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(v_stack_p8 + 0xB8))) & (15));
    if (condition_is_not_equal) goto loc_00281361;
loc_00280F80:
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x2 + 0x2 + 0x9C4 * 2 * 8 + 0x8) = v_stack_p8 + 176;
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x2 + 0x2 + 0x9C4 * 2 * 8) = 0;
    if (((*(uint8_t *)(v_rip + 0xD45B66)) & (33)) != 0) goto loc_00281483;
loc_00280FA6:
    if (*(uint64_t *)(gs_base + (0 + 0x20)) + 2 + 2 + 2500 * 2 * 8 == 0) goto loc_00281152;
    result = KxWaitForLockOwnerShip(*(uint64_t *)(gs_base + (0 + 0x20)) + 2 + 2 + 2500 * 2 * 8, *(uint64_t *)(gs_base + (0 + 0x20)) + 2 + 2 + 2500 * 2 * 8, *(uint64_t *)(gs_base + (0 + 0x20)), v_stack_p8);
    goto loc_0028114A;
loc_00280FC2:
loc_00280FCA:
    *(uint64_t *)(v_stack_p18) = v_stack_p10;
    local_rsp = (local_rsp) + (104);
    return local_rbp;
loc_00280FEA:
    if (((*(uint64_t *)(v_rip + 0xD45A93)) & (0x600000ULL)) == 0) goto loc_00280E81;
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x160)) == 1) goto loc_00280E81;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) == 0) goto loc_00280E81;
    result = (v_stack_p10) >> (3);
    result = (uint32_t)((result) & (511));
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + result * 8))) & (32)) != 0) {
        local_rbx = (local_rbx) | (32);
    }
    local_rbx = (local_rbx) | (66);
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + result * 8))) & (66)) == 0) { local_rbx = local_rbx; }
    goto loc_00280E81;
loc_00281052:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0xB8)))) & (15)) != 0) goto loc_00281094;
    if (v_stack_p10 < (*(uint64_t *)(gs_base + (0 + 0x20)))) goto loc_00281094;
    if (v_stack_p10 > ((uint32_t)(Arg4))) goto loc_00281094;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x410) + 0x568) != 0) goto loc_002816B5;
loc_00281094:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0xB8)))) & (15)) == 0) goto loc_002810B3;
    if (v_stack_p10 < (*(uint64_t *)(gs_base + (0 + 0x20)))) goto loc_002810B3;
    if (v_stack_p10 <= ((uint32_t)(Arg4))) goto loc_0028154F;
loc_002810B3:
    if (v_stack_p10 < (*(uint64_t *)(gs_base + (0 + 0x20)))) goto loc_002810E1;
    if (v_stack_p10 > local_r10) goto loc_002810E1;
    if ((((uint8_t)(*(uint64_t *)(v_stack_p10))) & (1)) == 0) goto loc_002810E1;
    Arg1 = ((((uint8_t)(*(uint64_t *)(v_stack_p10))) & (66)) != 0) ? 1 : 0;
    result = ((((uint8_t)(*(uint64_t *)(v_stack_p10))) & (32)) != 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) == 0) goto loc_002813FF;
loc_002810E1:
loc_002810F5:
    if ((((uint8_t)(*(uint64_t *)(v_stack_p10))) & (1)) == 0) goto loc_0028112F;
    result = (*(uint64_t *)(v_stack_p10)) >> (60);
    if ((((uint8_t)(result)) & (1)) != 0) goto loc_002814BE;
    Arg1 = (*(uint64_t *)(v_stack_p10)) & (local_r14);
    Arg1 = (Arg1) | (v_rip - 2624996);
    if (((*(uint64_t *)(v_rip + 0xD4596B)) & (0x2000000ULL)) != 0) {
    }
    if (((*(uint64_t *)(v_rip + 0xD4596B)) & (0x2000000ULL)) != 0) goto loc_002810F5;
loc_0028112F:
loc_00281134:
loc_0028114A:
loc_00281152:
    if (v_stack_pC8 != 0) goto loc_00281764;
loc_00281160:
    if (v_stack_p38 == 0) goto loc_00281237;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_pB0 + 0xB8)))) & (15)) == 0) goto loc_002811B6;
loc_0028118B:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_pB0 + 0xB8)))) & (15)) != 0) goto loc_00281301;
loc_0028119A:
loc_002811A9:
    v_stack_p38 = v_stack_p10;
    goto loc_00280F35;
loc_002811B6:
    if (v_stack_p10 < (*(uint64_t *)(gs_base + (0 + 0x20)))) goto loc_0028118B;
    if (v_stack_p10 > (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508))) goto loc_0028118B;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x410) + 0x568) == 0) goto loc_0028118B;
    local_r13 = (v_stack_p10) >> (3);
    local_r13 = (uint32_t)((local_r13) & (511));
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x410) + 0x568) + local_r13 * 4)))) & (0x3FFFFFFFULL)) != 0) goto loc_002813DB;
    if (!sign_flag) goto loc_0028165C;
    if (((*(uint8_t *)(v_rip + 0xD458E6)) & (1)) != 0) goto loc_002816CD;
loc_00281226:
    local_rdi = 0;
    v_stack_p38 = v_stack_p10;
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x410) + 0x568) + local_r13 * 4) = 0;
    goto loc_00280F35;
loc_00281237:
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(v_stack_pB0 + 0xB8))) & (15));
    if (condition_is_not_equal) goto loc_00281467;
    local_rdi = 0;
loc_00281256:
    local_rbx = (*(uint64_t *)(gs_base + (0 + 0x20)) + 40000) + (48);
    if (((*(uint8_t *)(v_rip + 0xD4589F)) & (1)) != 0) goto loc_002813B0;
loc_0028126D:
    if (*(uint64_t *)(local_rbx) != 0) goto loc_00281292;
    if (*(uint64_t *)(local_rbx) == 0) goto loc_002811A9;
    result = KxWaitForLockChainValid(local_rbx, *(uint64_t *)(gs_base + (0 + 0x20)), *(uint64_t *)(gs_base + (0 + 0x20)), v_stack_pB0);
loc_00281292:
    *(uint64_t *)(local_rbx) = 0;
    result = (uint8_t)((*(uint64_t *)(local_rbx + 0x8)) ^ ((uint8_t)(*(uint64_t *)(local_rbx + 0x8))));
    if ((((uint8_t)(result)) & (4)) == 0) goto loc_002811A9;
    Arg3 = (result + 8) >> (5);
    Arg3 = (uint32_t)((Arg3) & (127));
    result = KeDisableInterrupts(*(uint64_t *)(local_rbx + 0x8), *(uint64_t *)(gs_base + (0 + 0x20)), Arg3, v_stack_pB0);
    result = KiHaltOnAddressWakeEntireList(*(uint64_t *)(local_rbx + 0x8), 0, Arg3, v_stack_pB0);
    if ((uint8_t)((uint8_t)(result)) == 0) goto loc_002811A9;
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8) != 0) goto loc_002815F9;
loc_002812F3:
    v_stack_p38 = v_stack_p10;
    goto loc_00280F35;
loc_00281301:
    if (v_stack_p10 < (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8))) goto loc_0028119A;
    if (v_stack_p10 > 0) goto loc_0028119A;
    local_r13 = (v_stack_p10) - (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8));
    local_r13 = (local_r13) >> (3);
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_r13 * 2))) & (31));
    Arg2 = (uint32_t)((2) << ((uint8_t)(Arg1)));
    Arg2 = (uint32_t)(~(Arg2));
    result = ((uint32_t)((uint32_t)(local_r13 * 2))) >> (5);
    v_stack_p38 = v_stack_p10;
    goto loc_00280F35;
loc_00281361:
    if (((uint8_t)(result)) == 7) goto loc_00281505;
    Arg1 = 3;
    if (((uint8_t)(result)) == 5) { Arg1 = 0; }
    Arg2 = ((uint32_t)((uint32_t)(Arg1)) * 8 + 14876096) + (v_rip - 2625856);
    goto loc_00280F80;
loc_00281385:
    if (((uint8_t)((uint32_t)((uint32_t)(Arg1)))) == 7) goto loc_0028151C;
    Arg1 = 3;
    if (((uint8_t)((uint32_t)((uint32_t)(Arg1)))) == 5) { Arg1 = 0; }
loc_00281397:
    goto loc_00280DE4;
loc_002813B0:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC8CAA2))) != 0) goto loc_0028126D;
    result = KiReleaseQueuedSpinLockInstrumented((uint8_t)(result), v_stack_pA8, v_rip - 2626464 + 14876096 + (uint32_t)((uint32_t)(Arg1)) * 8, v_stack_pB0);
    v_stack_p38 = v_stack_p10;
    goto loc_00280F35;
loc_002813DB:
    if (((*(uint8_t *)(v_rip + 0xD45724)) & (1)) != 0) goto loc_0028171F;
loc_002813E8:
    v_stack_p38 = v_stack_p10;
    goto loc_00280F35;
loc_002813FF:
    if (((*(uint64_t *)(v_rip + 0xD4567E)) & (0x600000ULL)) == 0) goto loc_002810E1;
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x160)) == 1) goto loc_002810E1;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) == 0) goto loc_002810E1;
    result = (v_stack_p10) >> (3);
    result = (uint32_t)((result) & (511));
    local_rbx = (uint8_t)(result);
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + result * 8))) & (32)) != 0) {
        local_rbx = ((uint8_t)(result)) | (32);
    }
    local_rbx = (local_rbx) | (66);
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + result * 8))) & (66)) == 0) { local_rbx = local_rbx; }
    goto loc_002810E1;
loc_00281467:
    if (((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + result * 8))) == 7) goto loc_002815ED;
    Arg1 = 72;
    if (((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + result * 8))) == 5) { Arg1 = 0; }
    goto loc_00281256;
loc_00281483:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC8C9CF))) != 0) goto loc_00280FA6;
    result = KiAcquireQueuedSpinLockInstrumented(Arg1, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508), v_rip - 2626464 + 14876096 + (uint32_t)((uint32_t)(Arg1)) * 8, v_stack_pB0);
    goto loc_0028114A;
loc_0028149B:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC8C9B7))) != 0) goto loc_00280E0A;
    result = KiAcquireQueuedSpinLockInstrumented(Arg1, v_rip - 2626464 + 14876096 + (uint32_t)((uint32_t)(Arg1)) * 8, v_rip - 2626464 + 14876096 + (uint32_t)((uint32_t)(Arg1)) * 8, v_stack_pB0);
    goto loc_00280E19;
loc_002814BE:
    if ((((uint8_t)(result)) & (2)) != 0) goto loc_00281530;
    local_rdi = (local_rbx) | (result);
    if (((*(uint64_t *)(v_rip + 0xD455AB)) & (0x2000000ULL)) != 0) {
    }
    if (condition_is_below) goto loc_00281678;
loc_002814F1:
    if (((*(uint64_t *)(v_rip + 0xD455AB)) & (0x2000000ULL)) == 0) { local_rbx = local_rdi; }
    goto loc_002810F5;
loc_00281505:
    Arg2 = (1 * 8 + 14876096) + (v_rip - 2626464);
    goto loc_00280F80;
loc_0028151C:
    goto loc_00281397;
loc_00281530:
    local_rbp = (uint32_t)((0) + 1);
    if (((*(uint32_t *)(v_rip + 0xD43D74)) & ((uint32_t)(local_rbp))) == 0) goto loc_002815C6;
loc_0028153E:
loc_00281540:
    if (condition_is_below) goto loc_00281530;
    goto loc_002810F5;
loc_0028154F:
    Arg1 = (v_stack_p10) - (v_rip - 2626464 + 14876096 + (uint32_t)((uint32_t)(Arg1)) * 8);
    Arg1 = (Arg1) >> (3);
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(Arg1)));
    result = ((uint32_t)((uint32_t)(Arg1))) >> (5);
    local_rdi = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) & (31));
    local_rbp = (uint32_t)((1) << ((uint8_t)((uint32_t)((uint32_t)(local_rdi)))));
    local_rbx = (result * 4 + 14873004) + (v_rip - 2626464);
    local_r15 = (uint32_t)((2) << ((uint8_t)((uint32_t)((uint32_t)(local_rdi)))));
    local_r14 = (uint32_t)(~((uint32_t)((uint32_t)(local_r15))));
loc_00281598:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx))))) >> ((uint8_t)((uint32_t)((uint32_t)(local_rdi)))));
    if ((((uint8_t)(result)) & (1)) != 0) goto loc_00281633;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx))))) | ((uint32_t)(local_rbp)));
    Arg1 = (uint32_t)((Arg1) & ((uint32_t)(local_r14)));
    if (condition_is_not_equal) goto loc_00281598;
    goto loc_00281134;
loc_002815C6:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD454EC)))) & (64)) == 0) goto loc_0028153E;
    result = KiCheckVpBackingLongSpinWaitHypercall(Arg1, (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx)))))), v_rip - 2626464 + 14876096 + (uint32_t)((uint32_t)(Arg1)) * 8, v_stack_pB0);
    if ((uint8_t)(result) == 0) goto loc_0028153E;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rbp)), (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx)))))), v_rip - 2626464 + 14876096 + (uint32_t)((uint32_t)(Arg1)) * 8, v_stack_pB0);
    goto loc_00281540;
loc_002815ED:
    local_rdi = 0;
    goto loc_00281256;
loc_002815F9:
loc_00281600:
    if (condition_is_not_equal) goto loc_00281600;
    if (condition_is_above_or_equal) goto loc_002812F3;
    result = KiRemoveSystemWorkPriorityKick(24, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0x2813A0 + 0xE2FDC0 + (uint32_t)((uint32_t)(arg1)) * 8)))), v_rip - 2626464 + 14876096 + (uint32_t)((uint32_t)(Arg1)) * 8, v_stack_pB0);
    goto loc_002812F3;
loc_00281621:
    result = KxWaitForLockOwnerShip(24, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0x2813A0 + 0xE2FDC0 + (uint32_t)((uint32_t)(arg1)) * 8)))), v_rip - 2626464 + 14876096 + (uint32_t)((uint32_t)(Arg1)) * 8, v_stack_pB0);
    goto loc_00280E19;
loc_00281633:
    if ((((uint8_t)(result)) & (2)) != 0) goto loc_00281700;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0x2813A0 + 0xE2FDC0 + (uint32_t)((uint32_t)(arg1)) * 8))))))) | ((uint32_t)(local_r15)));
    Arg2 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0x2813A0 + 0xE2FDC0 + (uint32_t)((uint32_t)(arg1)) * 8))))))));
    if (condition_is_equal) { Arg2 = (uint32_t)(Arg1); }
    goto loc_00281598;
loc_00281650:
    goto loc_00280E19;
loc_0028165C:
    local_rdi = 0;
    Arg4 = 0;
    v_stack_p20 = 0;
    result = KeBugCheckEx(local_rdi + 16, Arg1, 256, Arg4);
loc_00281678:
    result = (uint8_t)((0) & (33));
    if (((uint8_t)(result)) != 1) goto loc_002814F1;
    result = ((uint32_t)((uint32_t)(local_rdi))) + (local_rdi + 16);
    if (v_stack_p10 < result) goto loc_002814F1;
    result = MiCheckLinearProtectedPteAccessedBit(v_stack_p10, 0, 128, Arg4);
    goto loc_002814F1;
loc_002816B5:
    result = (uint32_t)(((uint32_t)((uint32_t)(v_stack_p10))) >> (3));
    result = (uint32_t)((result) & (511));
    result = ExAcquireSpinLockExclusiveAtDpcLevel(v_stack_p10 + result * 4, 0, 128, Arg4);
    goto loc_0028114A;
loc_002816CD:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC8C785))) != 0) goto loc_00281226;
    result = ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented(v_stack_p10 + result * 4, v_stack_pA8, 128, Arg4);
    v_stack_p38 = v_stack_p10;
    goto loc_00280F35;
loc_00281700:
    local_r12 = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) + 1);
    if (((*(uint32_t *)(v_rip + 0xD43BA2)) & ((uint32_t)(local_r12))) == 0) goto loc_00281747;
loc_0028170C:
loc_0028170E:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx))))) >> (0));
    if ((((uint8_t)(result)) & (1)) != 0) goto loc_00281700;
    goto loc_00281598;
loc_0028171F:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC8C733))) != 0) goto loc_002813E8;
    result = ExpReleaseSpinLockSharedFromDpcLevelInstrumented(0, v_stack_pA8, 128, Arg4);
    v_stack_p38 = v_stack_p10;
    goto loc_00280F35;
loc_00281747:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD4536B)))) & (64)) == 0) goto loc_0028170C;
    result = KiCheckVpBackingLongSpinWaitHypercall(0, v_stack_pA8, 128, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0028170C;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_r12)), v_stack_pA8, 128, Arg4);
    goto loc_0028170E;
loc_00281764:
    if (v_stack_p10 == local_rbp) goto loc_002811A9;
    goto loc_00281160;
loc_00281775:
    result = ExAcquireSpinLockExclusiveAtDpcLevel(v_rip + 12279108, v_stack_pA8, 128, Arg4);
    goto loc_00280EDB;
loc_002817BB:
    if (0 > (v_rip + 12279108)) goto loc_00280EE7;
loc_002817CC:
    result = ExReleaseSpinLockExclusiveFromDpcLevel(v_rip + 12279021, v_stack_pA8, 128, v_stack_pB0);
    goto loc_00280F24;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xB0` | `64` | `R` |
| `Arg1` | `+ 0xB8` | `32` | `R` |
| `Arg3` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00280D10&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
