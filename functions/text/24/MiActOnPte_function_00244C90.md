# MiActOnPte

- RVA: `0x00244C90`–`0x002459CA` (길이 `3,386` bytes)
- VA: `0x0000000140244C90`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00061CEC`
- 디코드: `816`개 명령, `3,386/3,386` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **51**; 고유 호출 대상: **33**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x00244D0A` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x00244DDC` → [IS_PTE_NOT_DEMAND_ZERO](../22/IS_PTE_NOT_DEMAND_ZERO_function_0022F4D0.md) (function, `0x0022F4D0`)
- `0x00244E08` → [MiUpdatePageFileHighInPte](../36/MiUpdatePageFileHighInPte_function_0036D840.md) (function, `0x0036D840`)
- `0x00244E73` → [MiSwizzleInvalidPte](../28/MiSwizzleInvalidPte_function_0028F5E0.md) (function, `0x0028F5E0`)
- `0x00244E82` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x00244ECD` → [MiLockLeafPage](../36/MiLockLeafPage_function_003658C0.md) (function, `0x003658C0`)
- `0x00244F4F` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0024508C` → [MI_IS_RESET_PTE](../38/MI_IS_RESET_PTE_function_00383E80.md) (function, `0x00383E80`)
- `0x0024509C` → [MiClearResetPfn](../47/MiClearResetPfn_function_00473B3C.md) (function, `0x00473B3C`)
- `0x00245109` → [MiWriteValidPteNewProtection](../28/MiWriteValidPteNewProtection_function_00281810.md) (function, `0x00281810`)
- `0x0024512D` → [MiGetVaAge](MiGetVaAge_function_00240AC0.md) (function, `0x00240AC0`)
- `0x0024514B` → [MiSetVaAgeList](../29/MiSetVaAgeList_function_00290A20.md) (function, `0x00290A20`)
- `0x0024516A` → [MiUpdatePfnPriority](../2B/MiUpdatePfnPriority_function_002B8570.md) (function, `0x002B8570`)
- `0x0024518C` → [MiUpdateWsleAge](../28/MiUpdateWsleAge_function_0028F608.md) (function, `0x0028F608`)
- `0x002451D8` → [MiDemoteCombinedPte](../22/MiDemoteCombinedPte_function_0022ABAC.md) (function, `0x0022ABAC`)
- `0x00245212` → [MiClearPageFileReservation](../32/MiClearPageFileReservation_function_0032B68C.md) (function, `0x0032B68C`)
- `0x0024522E` → [MI_IS_RESET_PTE](../38/MI_IS_RESET_PTE_function_00383E80.md) (function, `0x00383E80`)
- `0x00245240` → [MI_CLEAR_RESET_PTE](../46/MI_CLEAR_RESET_PTE_function_00464460.md) (function, `0x00464460`)
- `0x0024525E` → [MiRotatedToFrameBuffer](../2C/MiRotatedToFrameBuffer_function_002C5FE4.md) (function, `0x002C5FE4`)
- `0x002452CE` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x002452E4` → [MiInvalidPteConforms](../37/MiInvalidPteConforms_function_00372A10.md) (function, `0x00372A10`)
- `0x00245374` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x0024544D` → [MiCapturePageFileInfoInline](../37/MiCapturePageFileInfoInline_function_00373A60.md) (function, `0x00373A60`)
- `0x00245495` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x002454A4` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x002454EA` → [MiCheckUserVirtualAddress](../48/MiCheckUserVirtualAddress_function_00488834.md) (function, `0x00488834`)
- `0x0024550B` → [MiUpdatePageTableUseCount](../3D/MiUpdatePageTableUseCount_function_003D34F0.md) (function, `0x003D34F0`)
- `0x0024551A` → [MiMakePageFilePte](../38/MiMakePageFilePte_function_003823C8.md) (function, `0x003823C8`)
- `0x0024556C` → [MiSharedVaToPartition](../2B/MiSharedVaToPartition_function_002B6700.md) (function, `0x002B6700`)
- `0x002455DF` → [MiUnlinkPageFromListEx](../28/MiUnlinkPageFromListEx_function_00287590.md) (function, `0x00287590`)
- `0x002455E9` → [MiSetPfnModified](../36/MiSetPfnModified_function_00362960.md) (function, `0x00362960`)
- `0x0024567C` → [MiUpdatePfnPriority](../2B/MiUpdatePfnPriority_function_002B8570.md) (function, `0x002B8570`)
- `0x00245692` → [MiLockLeafPage](../36/MiLockLeafPage_function_003658C0.md) (function, `0x003658C0`)
- `0x002456A8` → [MiReleasePageFileInfo](../28/MiReleasePageFileInfo_function_00283FD0.md) (function, `0x00283FD0`)
- `0x002456EB` → [MiUpdatePageFileHighInPte](../36/MiUpdatePageFileHighInPte_function_0036D840.md) (function, `0x0036D840`)
- `0x002456FA` → [MiClearPageFileReservation](../32/MiClearPageFileReservation_function_0032B68C.md) (function, `0x0032B68C`)
- `0x00245717` → [MiCanPfnOriginalPteBeLost](../37/MiCanPfnOriginalPteBeLost_function_00373D3C.md) (function, `0x00373D3C`)
- `0x00245757` → [MI_IS_RESET_PTE](../38/MI_IS_RESET_PTE_function_00383E80.md) (function, `0x00383E80`)
- `0x00245767` → [MiClearResetPfn](../47/MiClearResetPfn_function_00473B3C.md) (function, `0x00473B3C`)
- `0x0024577F` → [MiSetPfnModified](../36/MiSetPfnModified_function_00362960.md) (function, `0x00362960`)
- `0x00245796` → [MiUnlinkPageFromListEx](../28/MiUnlinkPageFromListEx_function_00287590.md) (function, `0x00287590`)
- `0x002457AB` → [MiInsertPageInList](../2B/MiInsertPageInList_function_002BA000.md) (function, `0x002BA000`)
- `0x002457DA` → [MiUpdatePageFileHighInPte](../36/MiUpdatePageFileHighInPte_function_0036D840.md) (function, `0x0036D840`)
- `0x002457E9` → [MiClearPageFileReservation](../32/MiClearPageFileReservation_function_0032B68C.md) (function, `0x0032B68C`)
- `0x0024580C` → [MiInsertPageInList](../2B/MiInsertPageInList_function_002BA000.md) (function, `0x002BA000`)
- `0x00245819` → [MiCanPfnOriginalPteBeLost](../37/MiCanPfnOriginalPteBeLost_function_00373D3C.md) (function, `0x00373D3C`)
- `0x00245868` → [MiLockSpecialPurposeMemoryCachedPage](../40/MiLockSpecialPurposeMemoryCachedPage_function_004049F0.md) (function, `0x004049F0`)
- `0x002458BB` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00245900` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00245910` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0024594F` → [MiDiscardTransitionPteEx](../37/MiDiscardTransitionPteEx_function_00375954.md) (function, `0x00375954`)

### Direct callers
- [MiWalkVaRange](MiWalkVaRange_function_00243BF0.md) at `0x00243F5C`

### Static image references
- `0x00244D46` → RVA `0x00E2DCE0` (`.data`; read)
- `0x00244DC5` → RVA `0x00E30088` (`.data`; read)
- `0x00244E48` → RVA `0x00E2DC80` (`.data`; read)
- `0x002450C2` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x00245487` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00244C90  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
00244C95  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
00244C9A  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
00244C9F  55                              push rbp
00244CA0  56                              push rsi
00244CA1  57                              push rdi
00244CA2  41 54                           push r12
00244CA4  41 55                           push r13
00244CA6  41 56                           push r14
00244CA8  41 57                           push r15
00244CAA  48 8D 6C 24 F9                  lea rbp, [rsp - 7]
00244CAF  48 81 EC D0 00 00 00            sub rsp, 0xd0
00244CB6  48 8B 5D 7F                     mov rbx, qword ptr [rbp + 0x7f]
00244CBA  33 FF                           xor edi, edi
00244CBC  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00244CC5  4D 8B E9                        mov r13, r9
00244CC8  4D 8B F8                        mov r15, r8
00244CCB  48 89 7C 24 40                  mov qword ptr [rsp + 0x40], rdi
00244CD0  44 8B E2                        mov r12d, edx
00244CD3  89 7C 24 38                     mov dword ptr [rsp + 0x38], edi
00244CD7  48 89 3B                        mov qword ptr [rbx], rdi
00244CDA  48 8B 5D 77                     mov rbx, qword ptr [rbp + 0x77]
00244CDE  48 8B B0 B8 00 00 00            mov rsi, qword ptr [rax + 0xb8]
00244CE5  48 89 3B                        mov qword ptr [rbx], rdi
00244CE8  48 BB FF FF FF FF FF FF FF 7F   movabs rbx, 0x7fffffffffffffff
00244CF2  4C 8D 9E 00 04 00 00            lea r11, [rsi + 0x400]
00244CF9  4C 89 5C 24 48                  mov qword ptr [rsp + 0x48], r11
00244CFE  4D 85 ED                        test r13, r13
00244D01  0F 85 4C 09 00 00               jne 0x140245653
00244D07  49 8B CF                        mov rcx, r15
00244D0A  E8 91 DB 03 00                  call 0x1402828a0
00244D0F  4C 8B C0                        mov r8, rax
00244D12  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00244D17  48 8B C8                        mov rcx, rax
00244D1A  48 8B D0                        mov rdx, rax
00244D1D  4C 8B D0                        mov r10, rax
00244D20  4C 8B C8                        mov r9, rax
00244D23  F6 C1 01                        test cl, 1
00244D26  74 6B                           je 0x140244d93
00244D28  44 8B 7D 67                     mov r15d, dword ptr [rbp + 0x67]
00244D2C  4D 85 ED                        test r13, r13
00244D2F  0F 85 93 01 00 00               jne 0x140244ec8
00244D35  48 C1 E8 0C                     shr rax, 0xc
00244D39  48 B9 FF FF FF FF FF 00 00 00   movabs rcx, 0xffffffffff
00244D43  48 23 C1                        and rax, rcx
00244D46  48 3B 05 93 8F BE 00            cmp rax, qword ptr [rip + 0xbe8f93]
00244D4D  77 23                           ja 0x140244d72
00244D4F  48 8D 0C 40                     lea rcx, [rax + rax*2]
00244D53  48 B8 28 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000028
00244D5D  48 03 C9                        add rcx, rcx
00244D60  48 8B C0                        mov rax, rax
00244D63  48 8B 04 C8                     mov rax, qword ptr [rax + rcx*8]
00244D67  48 0F BA E0 36                  bt rax, 0x36
00244D6C  0F 82 91 01 00 00               jb 0x140244f03
00244D72  B8 34 04 00 C0                  mov eax, 0xc0000434
00244D77  48 8B 9C 24 18 01 00 00         mov rbx, qword ptr [rsp + 0x118]
00244D7F  48 81 C4 D0 00 00 00            add rsp, 0xd0
00244D86  41 5F                           pop r15
00244D88  41 5E                           pop r14
00244D8A  41 5D                           pop r13
00244D8C  41 5C                           pop r12
00244D8E  5F                              pop rdi
00244D8F  5E                              pop rsi
00244D90  5D                              pop rbp
00244D91  C3                              ret
00244D92  CC                              int3
00244D93  48 0F BA E2 0A                  bt rdx, 0xa
00244D98  0F 82 1D 01 00 00               jb 0x140244ebb
00244D9E  49 0F BA E2 0B                  bt r10, 0xb
00244DA3  0F 82 19 05 00 00               jb 0x1402452c2
00244DA9  8B 5D 67                        mov ebx, dword ptr [rbp + 0x67]
00244DAC  83 FB 02                        cmp ebx, 2
00244DAF  0F 84 06 01 00 00               je 0x140244ebb
00244DB5  4D 85 C9                        test r9, r9
00244DB8  0F 84 F0 06 00 00               je 0x1402454ae
00244DBE  0F B7 86 AE 04 00 00            movzx eax, word ptr [rsi + 0x4ae]
00244DC5  48 8B 15 BC B2 BE 00            mov rdx, qword ptr [rip + 0xbeb2bc]
00244DCC  4C 8B 14 C2                     mov r10, qword ptr [rdx + rax*8]
00244DD0  4D 85 ED                        test r13, r13
00244DD3  0F 85 A6 04 00 00               jne 0x14024527f
00244DD9  49 8B C8                        mov rcx, r8
00244DDC  E8 EF A6 FE FF                  call 0x14022f4d0
00244DE1  85 C0                           test eax, eax
00244DE3  0F 85 4F 06 00 00               jne 0x140245438
00244DE9  83 FB 01                        cmp ebx, 1
00244DEC  0F 84 39 04 00 00               je 0x14024522b
00244DF2  41 0F B6 C0                     movzx eax, r8b
00244DF6  D0 E8                           shr al, 1
00244DF8  A8 01                           test al, 1
00244DFA  0F 85 E2 03 00 00               jne 0x1402451e2
00244E00  BA 01 00 00 00                  mov edx, 1
00244E05  49 8B C8                        mov rcx, r8
00244E08  E8 33 8A 12 00                  call 0x14036d840
00244E0D  4D 85 ED                        test r13, r13
00244E10  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00244E15  4D 0F 45 FD                     cmovne r15, r13
00244E19  49 89 07                        mov qword ptr [r15], rax
00244E1C  33 C0                           xor eax, eax
00244E1E  E9 54 FF FF FF                  jmp 0x140244d77
00244E23  49 8B 46 10                     mov rax, qword ptr [r14 + 0x10]
00244E27  48 83 E0 FB                     and rax, 0xfffffffffffffffb
00244E2B  49 89 46 10                     mov qword ptr [r14 + 0x10], rax
00244E2F  48 8B 55 7F                     mov rdx, qword ptr [rbp + 0x7f]
00244E33  48 89 0A                        mov qword ptr [rdx], rcx
00244E36  48 85 C9                        test rcx, rcx
00244E39  0F 85 DA 07 00 00               jne 0x140245619
00244E3F  49 8B 46 10                     mov rax, qword ptr [r14 + 0x10]
00244E43  48 85 C0                        test rax, rax
00244E46  74 1C                           je 0x140244e64
00244E48  48 8B 0D 31 8E BE 00            mov rcx, qword ptr [rip + 0xbe8e31]
00244E4F  48 8B F8                        mov rdi, rax
00244E52  48 85 C9                        test rcx, rcx
00244E55  74 0D                           je 0x140244e64
00244E57  A8 10                           test al, 0x10
00244E59  75 67                           jne 0x140244ec2
00244E5B  48 8B F9                        mov rdi, rcx
00244E5E  48 F7 D7                        not rdi
00244E61  48 23 F8                        and rdi, rax
00244E64  48 B8 00 00 00 00 01 00 00 00   movabs rax, 0x100000000
00244E6E  8B CF                           mov ecx, edi
00244E70  48 0B C8                        or rcx, rax
00244E73  E8 68 A7 04 00                  call 0x14028f5e0
00244E78  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
00244E7D  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00244E82  E8 19 DA 03 00                  call 0x1402828a0
00244E87  48 83 E0 FD                     and rax, 0xfffffffffffffffd
00244E8B  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00244E90  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
00244E95  49 89 46 10                     mov qword ptr [r14 + 0x10], rax
00244E99  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
00244EA3  F0 49 21 46 18                  lock and qword ptr [r14 + 0x18], rax
00244EA8  4D 85 ED                        test r13, r13
00244EAB  75 0E                           jne 0x140244ebb
00244EAD  48 8B 54 24 30                  mov rdx, qword ptr [rsp + 0x30]
00244EB2  F6 C2 42                        test dl, 0x42
00244EB5  0F 85 42 02 00 00               jne 0x1402450fd
00244EBB  33 C0                           xor eax, eax
00244EBD  E9 B5 FE FF FF                  jmp 0x140244d77
00244EC2  48 83 E7 EF                     and rdi, 0xffffffffffffffef
00244EC6  EB 9C                           jmp 0x140244e64
00244EC8  33 D2                           xor edx, edx
00244ECA  49 8B CD                        mov rcx, r13
00244ECD  E8 EE 09 12 00                  call 0x1403658c0
00244ED2  4C 8B F0                        mov r14, rax
00244ED5  48 85 C0                        test rax, rax
00244ED8  0F 84 7C 09 00 00               je 0x14024585a
00244EDE  49 8B 4D 00                     mov rcx, qword ptr [r13]
00244EE2  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
00244EE7  F6 C1 01                        test cl, 1
00244EEA  0F 84 65 09 00 00               je 0x140245855
00244EF0  48 8B 75 57                     mov rsi, qword ptr [rbp + 0x57]
00244EF4  49 BC 00 00 00 00 00 01 00 00   movabs r12, 0x10000000000
00244EFE  E9 C1 00 00 00                  jmp 0x140244fc4
00244F03  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
00244F0D  48 8B C0                        mov rax, rax
00244F10  4C 8D 34 C8                     lea r14, [rax + rcx*8]
00244F14  49 BC 00 00 00 00 00 01 00 00   movabs r12, 0x10000000000
00244F1E  49 8B 46 28                     mov rax, qword ptr [r14 + 0x28]
00244F22  49 85 C4                        test r12, rax
00244F25  75 0D                           jne 0x140244f34
00244F27  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
00244F2B  48 85 C0                        test rax, rax
00244F2E  0F 89 E6 09 00 00               jns 0x14024591a
00244F34  49 8B 5E 08                     mov rbx, qword ptr [r14 + 8]
00244F38  48 8D 4D 97                     lea rcx, [rbp - 0x69]
00244F3C  33 D2                           xor edx, edx
00244F3E  48 B8 00 00 00 00 00 00 00 80   movabs rax, 0x8000000000000000
00244F48  48 0B D8                        or rbx, rax
00244F4B  44 8D 42 70                     lea r8d, [rdx + 0x70]
00244F4F  E8 EC 1C 48 00                  call 0x1406c6c40
00244F54  48 8B 86 80 02 00 00            mov rax, qword ptr [rsi + 0x280]
00244F5B  48 85 C0                        test rax, rax
00244F5E  74 31                           je 0x140244f91
00244F60  48 89 5D AF                     mov qword ptr [rbp - 0x51], rbx
00244F64  48 89 5D B7                     mov qword ptr [rbp - 0x49], rbx
00244F68  0F 1F 84 00 00 00 00 00         nop dword ptr [rax + rax]
00244F70  48 3B 58 20                     cmp rbx, qword ptr [rax + 0x20]
00244F74  0F 87 CA 09 00 00               ja 0x140245944
00244F7A  48 3B 58 18                     cmp rbx, qword ptr [rax + 0x18]
00244F7E  73 08                           jae 0x140244f88
00244F80  48 8B 00                        mov rax, qword ptr [rax]
00244F83  48 85 C0                        test rax, rax
00244F86  75 E8                           jne 0x140244f70
00244F88  48 85 C0                        test rax, rax
00244F8B  0F 85 5D 01 00 00               jne 0x1402450ee
00244F91  8B DF                           mov ebx, edi
00244F93  F0 49 0F BA 6E 18 3F            lock bts qword ptr [r14 + 0x18], 0x3f
00244F9A  0F 82 20 01 00 00               jb 0x1402450c0
00244FA0  48 8B 55 47                     mov rdx, qword ptr [rbp + 0x47]
00244FA4  48 8B 75 57                     mov rsi, qword ptr [rbp + 0x57]
00244FA8  8B 42 30                        mov eax, dword ptr [rdx + 0x30]
00244FAB  24 70                           and al, 0x70
00244FAD  3C 40                           cmp al, 0x40
00244FAF  0F 84 A6 02 00 00               je 0x14024525b
00244FB5  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
00244FBA  48 BB FF FF FF FF FF FF FF 7F   movabs rbx, 0x7fffffffffffffff
00244FC4  41 83 FF 02                     cmp r15d, 2
00244FC8  0F 84 8C 01 00 00               je 0x14024515a
00244FCE  41 0F B6 46 22                  movzx eax, byte ptr [r14 + 0x22]
00244FD3  A8 08                           test al, 8
00244FD5  0F 85 04 01 00 00               jne 0x1402450df
00244FDB  0F B6 D0                        movzx edx, al
00244FDE  80 E2 10                        and dl, 0x10
00244FE1  41 83 FF 01                     cmp r15d, 1
00244FE5  74 56                           je 0x14024503d
00244FE7  84 D2                           test dl, dl
00244FE9  74 27                           je 0x140245012
00244FEB  45 8B 5E 20                     mov r11d, dword ptr [r14 + 0x20]
00244FEF  44 89 5D 5F                     mov dword ptr [rbp + 0x5f], r11d
00244FF3  41 C1 EB 10                     shr r11d, 0x10
00244FF7  41 0F B6 DB                     movzx ebx, r11b
00244FFB  41 F6 C3 08                     test r11b, 8
00244FFF  0F 85 0F 07 00 00               jne 0x140245714
00245005  80 E3 EF                        and bl, 0xef
00245008  88 5D 61                        mov byte ptr [rbp + 0x61], bl
0024500B  8B 45 5F                        mov eax, dword ptr [rbp + 0x5f]
0024500E  41 89 46 20                     mov dword ptr [r14 + 0x20], eax
00245012  49 8B 4E 10                     mov rcx, qword ptr [r14 + 0x10]
00245016  0F B6 C1                        movzx eax, cl
00245019  C0 E8 02                        shr al, 2
0024501C  A8 01                           test al, 1
0024501E  0F 85 FF FD FF FF               jne 0x140244e23
00245024  0F B6 C1                        movzx eax, cl
00245027  D0 E8                           shr al, 1
00245029  A8 01                           test al, 1
0024502B  0F 85 FE FD FF FF               jne 0x140244e2f
00245031  48 8B 55 7F                     mov rdx, qword ptr [rbp + 0x7f]
00245035  48 89 3A                        mov qword ptr [rdx], rdi
00245038  E9 02 FE FF FF                  jmp 0x140244e3f
0024503D  84 D2                           test dl, dl
0024503F  0F 85 3C 08 00 00               jne 0x140245881
00245045  4D 85 ED                        test r13, r13
00245048  75 09                           jne 0x140245053
0024504A  F6 C1 42                        test cl, 0x42
0024504D  0F 85 2E 08 00 00               jne 0x140245881
00245053  41 8B 46 10                     mov eax, dword ptr [r14 + 0x10]
00245057  C0 E8 02                        shr al, 2
0024505A  A8 01                           test al, 1
0024505C  75 2A                           jne 0x140245088
0024505E  45 8B 5E 20                     mov r11d, dword ptr [r14 + 0x20]
00245062  44 89 5D 7F                     mov dword ptr [rbp + 0x7f], r11d
00245066  41 C1 EB 10                     shr r11d, 0x10
0024506A  41 0F B6 DB                     movzx ebx, r11b
0024506E  41 F6 C3 08                     test r11b, 8
00245072  0F 85 9E 07 00 00               jne 0x140245816
00245078  80 CB 10                        or bl, 0x10
0024507B  88 9D 81 00 00 00               mov byte ptr [rbp + 0x81], bl
00245081  8B 45 7F                        mov eax, dword ptr [rbp + 0x7f]
00245084  41 89 46 20                     mov dword ptr [r14 + 0x20], eax
00245088  49 8B 4E 10                     mov rcx, qword ptr [r14 + 0x10]
0024508C  E8 EF ED 13 00                  call 0x140383e80
00245091  85 C0                           test eax, eax
00245093  0F 84 88 01 00 00               je 0x140245221
00245099  49 8B CE                        mov rcx, r14
0024509C  E8 9B EA 22 00                  call 0x140473b3c
002450A1  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
002450AB  F0 49 21 46 18                  lock and qword ptr [r14 + 0x18], rax
002450B0  8B C7                           mov eax, edi
002450B2  E9 C0 FC FF FF                  jmp 0x140244d77
002450B7  66 0F 1F 84 00 00 00 00 00      nop word ptr [rax + rax]
002450C0  FF C3                           inc ebx
002450C2  85 1D E4 01 D8 00               test dword ptr [rip + 0xd801e4], ebx
002450C8  0F 84 B9 03 00 00               je 0x140245487
002450CE  F3 90                           pause
002450D0  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
002450D4  48 85 C0                        test rax, rax
002450D7  0F 89 B6 FE FF FF               jns 0x140244f93
002450DD  EB E1                           jmp 0x1402450c0
002450DF  F0 49 21 5E 18                  lock and qword ptr [r14 + 0x18], rbx
002450E4  B8 34 04 00 C0                  mov eax, 0xc0000434
002450E9  E9 89 FC FF FF                  jmp 0x140244d77
002450EE  48 39 78 30                     cmp qword ptr [rax + 0x30], rdi
002450F2  0F 84 99 FE FF FF               je 0x140244f91
002450F8  E9 75 FC FF FF                  jmp 0x140244d72
002450FD  48 83 E2 9D                     and rdx, 0xffffffffffffff9d
00245101  48 8B CE                        mov rcx, rsi
00245104  48 89 54 24 30                  mov qword ptr [rsp + 0x30], rdx
00245109  E8 02 C7 03 00                  call 0x140281810
0024510E  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
00245118  48 C1 E6 19                     shl rsi, 0x19
0024511C  48 8B C0                        mov rax, rax
0024511F  48 C1 E0 19                     shl rax, 0x19
00245123  48 2B F0                        sub rsi, rax
00245126  48 C1 FE 10                     sar rsi, 0x10
0024512A  48 8B D6                        mov rdx, rsi
0024512D  E8 8E B9 FF FF                  call 0x140240ac0
00245132  3C 01                           cmp al, 1
00245134  74 1A                           je 0x140245150
00245136  3C 07                           cmp al, 7
00245138  73 16                           jae 0x140245150
0024513A  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
0024513F  41 B1 01                        mov r9b, 1
00245142  41 B8 01 00 00 00               mov r8d, 1
00245148  48 8B D6                        mov rdx, rsi
0024514B  E8 D0 B8 04 00                  call 0x140290a20
00245150  B8 21 00 00 C0                  mov eax, 0xc0000021
00245155  E9 1D FC FF FF                  jmp 0x140244d77
0024515A  8B 55 6F                        mov edx, dword ptr [rbp + 0x6f]
0024515D  4D 85 ED                        test r13, r13
00245160  49 8B CE                        mov rcx, r14
00245163  40 0F 94 C7                     sete dil
00245167  44 8B C7                        mov r8d, edi
0024516A  E8 01 34 07 00                  call 0x1402b8570
0024516F  F0 49 21 5E 18                  lock and qword ptr [r14 + 0x18], rbx
00245174  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
00245179  3C FF                           cmp al, 0xff
0024517B  74 14                           je 0x140245191
0024517D  4D 85 ED                        test r13, r13
00245180  75 0F                           jne 0x140245191
00245182  44 0F B6 C0                     movzx r8d, al
00245186  48 8B D6                        mov rdx, rsi
00245189  48 8B CB                        mov rcx, rbx
0024518C  E8 77 A4 04 00                  call 0x14028f608
00245191  49 8B 46 28                     mov rax, qword ptr [r14 + 0x28]
00245195  49 85 C4                        test r12, rax
00245198  0F 85 1D FD FF FF               jne 0x140244ebb
0024519E  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
002451A2  48 85 C0                        test rax, rax
002451A5  0F 88 10 FD FF FF               js 0x140244ebb
002451AB  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
002451AF  48 85 C0                        test rax, rax
002451B2  0F 84 03 FD FF FF               je 0x140244ebb
002451B8  4D 85 ED                        test r13, r13
002451BB  0F 85 FA FC FF FF               jne 0x140244ebb
002451C1  4D 8B 46 08                     mov r8, qword ptr [r14 + 8]
002451C5  48 B8 00 00 00 00 00 00 00 80   movabs rax, 0x8000000000000000
002451CF  4C 0B C0                        or r8, rax
002451D2  48 8B D6                        mov rdx, rsi
002451D5  48 8B CB                        mov rcx, rbx
002451D8  E8 CF 59 FE FF                  call 0x14022abac
002451DD  E9 D9 FC FF FF                  jmp 0x140244ebb
002451E2  4C 89 45 77                     mov qword ptr [rbp + 0x77], r8
002451E6  49 0F BA E0 0A                  bt r8, 0xa
002451EB  72 20                           jb 0x14024520d
002451ED  48 8B 55 77                     mov rdx, qword ptr [rbp + 0x77]
002451F1  0F B6 C2                        movzx eax, dl
002451F4  C0 E8 02                        shr al, 2
002451F7  A8 01                           test al, 1
002451F9  75 09                           jne 0x140245204
002451FB  0F B6 C2                        movzx eax, dl
002451FE  D0 E8                           shr al, 1
00245200  A8 01                           test al, 1
00245202  74 09                           je 0x14024520d
00245204  48 85 D2                        test rdx, rdx
00245207  0F 85 92 04 00 00               jne 0x14024569f
0024520D  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
00245212  E8 75 64 0E 00                  call 0x14032b68c
00245217  4C 8B 44 24 30                  mov r8, qword ptr [rsp + 0x30]
0024521C  E9 DF FB FF FF                  jmp 0x140244e00
00245221  BF 34 04 00 C0                  mov edi, 0xc0000434
00245226  E9 76 FE FF FF                  jmp 0x1402450a1
0024522B  49 8B C8                        mov rcx, r8
0024522E  E8 4D EC 13 00                  call 0x140383e80
00245233  85 C0                           test eax, eax
00245235  0F 84 37 FB FF FF               je 0x140244d72
0024523B  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
00245240  E8 1B F2 21 00                  call 0x140464460
00245245  48 8B 44 24 30                  mov rax, qword ptr [rsp + 0x30]
0024524A  4D 85 ED                        test r13, r13
0024524D  4D 0F 45 FD                     cmovne r15, r13
00245251  49 89 07                        mov qword ptr [r15], rax
00245254  33 C0                           xor eax, eax
00245256  E9 1C FB FF FF                  jmp 0x140244d77
0024525B  48 8B CE                        mov rcx, rsi
0024525E  E8 81 0D 08 00                  call 0x1402c5fe4
00245263  85 C0                           test eax, eax
00245265  0F 84 4A FD FF FF               je 0x140244fb5
0024526B  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
00245275  F0 49 21 46 18                  lock and qword ptr [r14 + 0x18], rax
0024527A  E9 F3 FA FF FF                  jmp 0x140244d72
0024527F  45 85 E4                        test r12d, r12d
00245282  0F 85 BB 02 00 00               jne 0x140245543
00245288  4C 8B 5D 47                     mov r11, qword ptr [rbp + 0x47]
0024528C  41 F7 43 30 00 00 20 00         test dword ptr [r11 + 0x30], 0x200000
00245294  0F 85 3F FB FF FF               jne 0x140244dd9
0024529A  49 8B 43 48                     mov rax, qword ptr [r11 + 0x48]
0024529E  48 85 C0                        test rax, rax
002452A1  0F 84 32 FB FF FF               je 0x140244dd9
002452A7  48 8B 00                        mov rax, qword ptr [rax]
002452AA  0F B7 48 3C                     movzx ecx, word ptr [rax + 0x3c]
002452AE  B8 FF 03 00 00                  mov eax, 0x3ff
002452B3  66 23 C8                        and cx, ax
002452B6  0F B7 C1                        movzx eax, cx
002452B9  4C 8B 14 C2                     mov r10, qword ptr [rdx + rax*8]
002452BD  E9 17 FB FF FF                  jmp 0x140244dd9
002452C2  4D 85 ED                        test r13, r13
002452C5  0F 85 C2 03 00 00               jne 0x14024568d
002452CB  49 8B CF                        mov rcx, r15
002452CE  E8 CD D5 03 00                  call 0x1402828a0
002452D3  48 8B D8                        mov rbx, rax
002452D6  48 0F BA E0 0B                  bt rax, 0xb
002452DB  0F 83 98 05 00 00               jae 0x140245879
002452E1  48 8B C8                        mov rcx, rax
002452E4  E8 27 D7 12 00                  call 0x140372a10
002452E9  85 C0                           test eax, eax
002452EB  74 DE                           je 0x1402452cb
002452ED  48 8B 05 8C 89 BE 00            mov rax, qword ptr [rip + 0xbe898c]
002452F4  48 85 C0                        test rax, rax
002452F7  74 12                           je 0x14024530b
002452F9  F6 C3 10                        test bl, 0x10
002452FC  0F 85 38 02 00 00               jne 0x14024553a
00245302  48 8B C8                        mov rcx, rax
00245305  48 F7 D1                        not rcx
00245308  48 23 CB                        and rcx, rbx
0024530B  48 B8 FF FF FF FF FF 00 00 00   movabs rax, 0xffffffffff
00245315  48 C1 E9 0C                     shr rcx, 0xc
00245319  48 23 C8                        and rcx, rax
0024531C  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
00245326  48 8D 14 49                     lea rdx, [rcx + rcx*2]
0024532A  48 03 D2                        add rdx, rdx
0024532D  48 8B C0                        mov rax, rax
00245330  48 3B 0D A9 89 BE 00            cmp rcx, qword ptr [rip + 0xbe89a9]
00245337  4C 8D 34 D0                     lea r14, [rax + rdx*8]
0024533B  77 8E                           ja 0x1402452cb
0024533D  48 B8 28 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000028
00245347  48 8B C0                        mov rax, rax
0024534A  48 8B 04 D0                     mov rax, qword ptr [rax + rdx*8]
0024534E  48 0F BA E0 36                  bt rax, 0x36
00245353  0F 83 72 FF FF FF               jae 0x1402452cb
00245359  44 8B FF                        mov r15d, edi
0024535C  0F 1F 40 00                     nop dword ptr [rax]
00245360  F0 49 0F BA 6E 18 3F            lock bts qword ptr [r14 + 0x18], 0x3f
00245367  0F 82 13 02 00 00               jb 0x140245580
0024536D  4C 8B 7D 57                     mov r15, qword ptr [rbp + 0x57]
00245371  49 8B CF                        mov rcx, r15
00245374  E8 27 D5 03 00                  call 0x1402828a0
00245379  48 3B C3                        cmp rax, rbx
0024537C  0F 85 30 03 00 00               jne 0x1402456b2
00245382  49 8B 46 28                     mov rax, qword ptr [r14 + 0x28]
00245386  48 8B 0D FB AC BE 00            mov rcx, qword ptr [rip + 0xbeacfb]
0024538D  48 C1 E8 2B                     shr rax, 0x2b
00245391  25 FF 03 00 00                  and eax, 0x3ff
00245396  48 8B 04 C1                     mov rax, qword ptr [rcx + rax*8]
0024539A  8B 40 04                        mov eax, dword ptr [rax + 4]
0024539D  84 C0                           test al, al
0024539F  0F 88 BE 04 00 00               js 0x140245863
002453A5  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
002453A9  48 B9 00 00 00 00 00 00 00 80   movabs rcx, 0x8000000000000000
002453B3  48 0B C1                        or rax, rcx
002453B6  49 3B C7                        cmp rax, r15
002453B9  0F 85 D4 04 00 00               jne 0x140245893
002453BF  48 BB FF FF FF FF FF FF FF 7F   movabs rbx, 0x7fffffffffffffff
002453C9  4D 85 F6                        test r14, r14
002453CC  0F 84 2C F9 FF FF               je 0x140244cfe
002453D2  4D 85 ED                        test r13, r13
002453D5  0F 85 62 02 00 00               jne 0x14024563d
002453DB  8B 45 67                        mov eax, dword ptr [rbp + 0x67]
002453DE  83 F8 02                        cmp eax, 2
002453E1  0F 84 89 02 00 00               je 0x140245670
002453E7  41 0F B6 4E 22                  movzx ecx, byte ptr [r14 + 0x22]
002453EC  0F B6 D1                        movzx edx, cl
002453EF  80 E2 07                        and dl, 7
002453F2  80 FA 02                        cmp dl, 2
002453F5  0F 85 A6 01 00 00               jne 0x1402455a1
002453FB  83 F8 01                        cmp eax, 1
002453FE  0F 84 4F 03 00 00               je 0x140245753
00245404  F6 C1 28                        test cl, 0x28
00245407  0F 85 FB 02 00 00               jne 0x140245708
0024540D  49 8B 4E 10                     mov rcx, qword ptr [r14 + 0x10]
00245411  0F B6 C1                        movzx eax, cl
00245414  C0 E8 02                        shr al, 2
00245417  A8 01                           test al, 1
00245419  0F 85 A7 02 00 00               jne 0x1402456c6
0024541F  0F B6 C1                        movzx eax, cl
00245422  D0 E8                           shr al, 1
00245424  A8 01                           test al, 1
00245426  0F 85 A6 02 00 00               jne 0x1402456d2
0024542C  48 8B 55 7F                     mov rdx, qword ptr [rbp + 0x7f]
00245430  48 89 3A                        mov qword ptr [rdx], rdi
00245433  E9 AA 02 00 00                  jmp 0x1402456e2
00245438  83 FB 01                        cmp ebx, 1
0024543B  0F 84 31 F9 FF FF               je 0x140244d72
00245441  45 33 C0                        xor r8d, r8d
00245444  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
00245449  41 8D 50 01                     lea edx, [r8 + 1]
0024544D  E8 0E E6 12 00                  call 0x140373a60
00245452  48 8B 55 7F                     mov rdx, qword ptr [rbp + 0x7f]
00245456  48 89 02                        mov qword ptr [rdx], rax
00245459  48 85 C0                        test rax, rax
0024545C  0F 84 59 FA FF FF               je 0x140244ebb
00245462  48 8B 45 77                     mov rax, qword ptr [rbp + 0x77]
00245466  4C 89 10                        mov qword ptr [rax], r10
00245469  4D 85 ED                        test r13, r13
0024546C  75 0B                           jne 0x140245479
0024546E  F0 48 FF 8E 88 02 00 00         lock dec qword ptr [rsi + 0x288]
00245476  4D 8B EF                        mov r13, r15
00245479  48 8B 44 24 30                  mov rax, qword ptr [rsp + 0x30]
0024547E  49 89 45 00                     mov qword ptr [r13], rax
00245482  E9 34 FA FF FF                  jmp 0x140244ebb
00245487  8B 05 2B 16 D8 00               mov eax, dword ptr [rip + 0xd8162b]
0024548D  A8 40                           test al, 0x40
0024548F  0F 84 39 FC FF FF               je 0x1402450ce
00245495  E8 F6 9F 0C 00                  call 0x14030f490
0024549A  84 C0                           test al, al
0024549C  0F 84 2C FC FF FF               je 0x1402450ce
002454A2  8B CB                           mov ecx, ebx
002454A4  E8 B7 9F 0C 00                  call 0x14030f460
002454A9  E9 22 FC FF FF                  jmp 0x1402450d0
002454AE  4D 85 ED                        test r13, r13
002454B1  0F 85 BB F8 FF FF               jne 0x140244d72
002454B7  85 DB                           test ebx, ebx
002454B9  0F 85 B3 F8 FF FF               jne 0x140244d72
002454BF  49 8B DF                        mov rbx, r15
002454C2  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
002454CC  48 C1 E3 19                     shl rbx, 0x19
002454D0  48 8B C0                        mov rax, rax
002454D3  48 8B 55 47                     mov rdx, qword ptr [rbp + 0x47]
002454D7  4C 8D 4C 24 38                  lea r9, [rsp + 0x38]
002454DC  48 C1 E0 19                     shl rax, 0x19
002454E0  48 2B D8                        sub rbx, rax
002454E3  48 C1 FB 10                     sar rbx, 0x10
002454E7  48 8B CB                        mov rcx, rbx
002454EA  E8 45 33 24 00                  call 0x140488834
002454EF  48 85 C0                        test rax, rax
002454F2  0F 85 7A F8 FF FF               jne 0x140244d72
002454F8  8B 7C 24 38                     mov edi, dword ptr [rsp + 0x38]
002454FC  83 FF 18                        cmp edi, 0x18
002454FF  0F 84 6D F8 FF FF               je 0x140244d72
00245505  8D 50 01                        lea edx, [rax + 1]
00245508  48 8B CB                        mov rcx, rbx
0024550B  E8 E0 DF 18 00                  call 0x1403d34f0
00245510  8B D7                           mov edx, edi
00245512  41 8D 4D 01                     lea ecx, [r13 + 1]
00245516  48 C1 E2 05                     shl rdx, 5
0024551A  E8 A9 CE 13 00                  call 0x1403823c8
0024551F  48 33 C2                        xor rax, rdx
00245522  48 25 1F FC FF FF               and rax, 0xfffffffffffffc1f
00245528  48 33 C2                        xor rax, rdx
0024552B  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00245530  49 89 07                        mov qword ptr [r15], rax
00245533  33 C0                           xor eax, eax
00245535  E9 3D F8 FF FF                  jmp 0x140244d77
0024553A  48 83 E1 EF                     and rcx, 0xffffffffffffffef
0024553E  E9 C8 FD FF FF                  jmp 0x14024530b
00245543  49 8B D7                        mov rdx, r15
00245546  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
00245550  48 C1 E2 19                     shl rdx, 0x19
00245554  48 8B C0                        mov rax, rax
00245557  48 C1 E0 19                     shl rax, 0x19
0024555B  48 8D 8E 00 04 00 00            lea rcx, [rsi + 0x400]
00245562  48 2B D0                        sub rdx, rax
00245565  4D 8B C5                        mov r8, r13
00245568  48 C1 FA 10                     sar rdx, 0x10
0024556C  E8 8F 11 07 00                  call 0x1402b6700
00245571  4C 8B 44 24 30                  mov r8, qword ptr [rsp + 0x30]
00245576  4C 8B D0                        mov r10, rax
00245579  E9 5B F8 FF FF                  jmp 0x140244dd9
0024557E  66 90                           nop
00245580  41 FF C7                        inc r15d
00245583  44 85 3D 22 FD D7 00            test dword ptr [rip + 0xd7fd22], r15d
0024558A  0F 84 62 03 00 00               je 0x1402458f2
00245590  F3 90                           pause
00245592  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
00245596  48 85 C0                        test rax, rax
00245599  0F 89 C1 FD FF FF               jns 0x140245360
0024559F  EB DF                           jmp 0x140245580
002455A1  80 FA 03                        cmp dl, 3
002455A4  0F 85 5E 01 00 00               jne 0x140245708
002455AA  83 F8 01                        cmp eax, 1
002455AD  0F 84 A1 03 00 00               je 0x140245954
002455B3  F6 C1 08                        test cl, 8
002455B6  0F 85 4C 01 00 00               jne 0x140245708
002455BC  85 C0                           test eax, eax
002455BE  0F 85 44 01 00 00               jne 0x140245708
002455C4  F6 C1 20                        test cl, 0x20
002455C7  0F 85 3B 01 00 00               jne 0x140245708
002455CD  41 8B 46 20                     mov eax, dword ptr [r14 + 0x20]
002455D1  66 85 C0                        test ax, ax
002455D4  0F 85 AF 03 00 00               jne 0x140245989
002455DA  33 D2                           xor edx, edx
002455DC  49 8B CE                        mov rcx, r14
002455DF  E8 AC 1F 04 00                  call 0x140287590
002455E4  33 D2                           xor edx, edx
002455E6  49 8B CE                        mov rcx, r14
002455E9  E8 72 D3 11 00                  call 0x140362960
002455EE  49 8B 4E 10                     mov rcx, qword ptr [r14 + 0x10]
002455F2  0F B6 C1                        movzx eax, cl
002455F5  C0 E8 02                        shr al, 2
002455F8  A8 01                           test al, 1
002455FA  0F 85 B5 01 00 00               jne 0x1402457b5
00245600  0F B6 C1                        movzx eax, cl
00245603  D0 E8                           shr al, 1
00245605  A8 01                           test al, 1
00245607  0F 85 B4 01 00 00               jne 0x1402457c1
0024560D  48 8B 55 7F                     mov rdx, qword ptr [rbp + 0x7f]
00245611  48 89 3A                        mov qword ptr [rdx], rdi
00245614  E9 B8 01 00 00                  jmp 0x1402457d1
00245619  49 8B 46 28                     mov rax, qword ptr [r14 + 0x28]
0024561D  48 8B 0D 64 AA BE 00            mov rcx, qword ptr [rip + 0xbeaa64]
00245624  48 C1 E8 2B                     shr rax, 0x2b
00245628  25 FF 03 00 00                  and eax, 0x3ff
0024562D  48 8B 14 C1                     mov rdx, qword ptr [rcx + rax*8]
00245631  48 8B 45 77                     mov rax, qword ptr [rbp + 0x77]
00245635  48 89 10                        mov qword ptr [rax], rdx
00245638  E9 02 F8 FF FF                  jmp 0x140244e3f
0024563D  49 8B 45 00                     mov rax, qword ptr [r13]
00245641  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00245646  A8 01                           test al, 1
00245648  0F 84 8D FD FF FF               je 0x1402453db
0024564E  F0 49 21 5E 18                  lock and qword ptr [r14 + 0x18], rbx
00245653  4D 8B 45 00                     mov r8, qword ptr [r13]
00245657  49 8B C8                        mov rcx, r8
0024565A  4C 89 44 24 30                  mov qword ptr [rsp + 0x30], r8
0024565F  49 8B D0                        mov rdx, r8
00245662  4D 8B D0                        mov r10, r8
00245665  49 8B C0                        mov rax, r8
00245668  4D 8B C8                        mov r9, r8
0024566B  E9 B3 F6 FF FF                  jmp 0x140244d23
00245670  8B 55 6F                        mov edx, dword ptr [rbp + 0x6f]
00245673  41 B8 01 00 00 00               mov r8d, 1
00245679  49 8B CE                        mov rcx, r14
0024567C  E8 EF 2E 07 00                  call 0x1402b8570
00245681  F0 49 21 5E 18                  lock and qword ptr [r14 + 0x18], rbx
00245686  33 C0                           xor eax, eax
00245688  E9 EA F6 FF FF                  jmp 0x140244d77
0024568D  33 D2                           xor edx, edx
0024568F  49 8B CD                        mov rcx, r13
00245692  E8 29 02 12 00                  call 0x1403658c0
00245697  4C 8B F0                        mov r14, rax
0024569A  E9 2A FD FF FF                  jmp 0x1402453c9
0024569F  41 B8 01 00 00 00               mov r8d, 1
002456A5  49 8B CA                        mov rcx, r10
002456A8  E8 23 E9 03 00                  call 0x140283fd0
002456AD  E9 5B FB FF FF                  jmp 0x14024520d
002456B2  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
002456BC  F0 49 21 46 18                  lock and qword ptr [r14 + 0x18], rax
002456C1  E9 05 FC FF FF                  jmp 0x1402452cb
002456C6  49 8B 46 10                     mov rax, qword ptr [r14 + 0x10]
002456CA  48 83 E0 FB                     and rax, 0xfffffffffffffffb
002456CE  49 89 46 10                     mov qword ptr [r14 + 0x10], rax
002456D2  48 8B 55 7F                     mov rdx, qword ptr [rbp + 0x7f]
002456D6  48 89 0A                        mov qword ptr [rdx], rcx
002456D9  48 85 C9                        test rcx, rcx
002456DC  0F 85 83 02 00 00               jne 0x140245965
002456E2  49 8B 4E 10                     mov rcx, qword ptr [r14 + 0x10]
002456E6  BA 01 00 00 00                  mov edx, 1
002456EB  E8 50 81 12 00                  call 0x14036d840
002456F0  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
002456F5  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
002456FA  E8 8D 5F 0E 00                  call 0x14032b68c
002456FF  4C 8B 54 24 30                  mov r10, qword ptr [rsp + 0x30]
00245704  4D 89 56 10                     mov qword ptr [r14 + 0x10], r10
00245708  F0 49 21 5E 18                  lock and qword ptr [r14 + 0x18], rbx
0024570D  8B C7                           mov eax, edi
0024570F  E9 63 F6 FF FF                  jmp 0x140244d77
00245714  49 8B CE                        mov rcx, r14
00245717  E8 20 E6 12 00                  call 0x140373d3c
0024571C  85 C0                           test eax, eax
0024571E  0F 84 E1 F8 FF FF               je 0x140245005
00245724  49 8B 46 10                     mov rax, qword ptr [r14 + 0x10]
00245728  41 0F B6 4E 22                  movzx ecx, byte ptr [r14 + 0x22]
0024572D  C0 E9 04                        shr cl, 4
00245730  A8 04                           test al, 4
00245732  F6 D1                           not cl
00245734  0F 95 C0                        setne al
00245737  22 C8                           and cl, al
00245739  F6 C1 01                        test cl, 1
0024573C  0F 84 C3 F8 FF FF               je 0x140245005
00245742  49 8B 46 10                     mov rax, qword ptr [r14 + 0x10]
00245746  48 83 E0 FB                     and rax, 0xfffffffffffffffb
0024574A  49 89 46 10                     mov qword ptr [r14 + 0x10], rax
0024574E  E9 B2 F8 FF FF                  jmp 0x140245005
00245753  49 8B 4E 10                     mov rcx, qword ptr [r14 + 0x10]
00245757  E8 24 E7 13 00                  call 0x140383e80
0024575C  85 C0                           test eax, eax
0024575E  0F 84 5D 01 00 00               je 0x1402458c1
00245764  49 8B CE                        mov rcx, r14
00245767  E8 D0 E3 22 00                  call 0x140473b3c
0024576C  41 8B 46 10                     mov eax, dword ptr [r14 + 0x10]
00245770  C0 E8 02                        shr al, 2
00245773  A8 01                           test al, 1
00245775  75 91                           jne 0x140245708
00245777  BA 01 00 00 00                  mov edx, 1
0024577C  49 8B CE                        mov rcx, r14
0024577F  E8 DC D1 11 00                  call 0x140362960
00245784  41 8B 46 20                     mov eax, dword ptr [r14 + 0x20]
00245788  66 85 C0                        test ax, ax
0024578B  0F 85 3A 01 00 00               jne 0x1402458cb
00245791  33 D2                           xor edx, edx
00245793  49 8B CE                        mov rcx, r14
00245796  E8 F5 1D 04 00                  call 0x140287590
0024579B  49 8B CE                        mov rcx, r14
0024579E  A8 03                           test al, 3
002457A0  0F 85 A7 01 00 00               jne 0x14024594d
002457A6  BA 08 00 00 00                  mov edx, 8
002457AB  E8 50 48 07 00                  call 0x1402ba000
002457B0  E9 53 FF FF FF                  jmp 0x140245708
002457B5  49 8B 46 10                     mov rax, qword ptr [r14 + 0x10]
002457B9  48 83 E0 FB                     and rax, 0xfffffffffffffffb
002457BD  49 89 46 10                     mov qword ptr [r14 + 0x10], rax
002457C1  48 8B 55 7F                     mov rdx, qword ptr [rbp + 0x7f]
002457C5  48 89 0A                        mov qword ptr [rdx], rcx
002457C8  48 85 C9                        test rcx, rcx
002457CB  0F 85 D5 01 00 00               jne 0x1402459a6
002457D1  49 8B 4E 10                     mov rcx, qword ptr [r14 + 0x10]
002457D5  BA 01 00 00 00                  mov edx, 1
002457DA  E8 61 80 12 00                  call 0x14036d840
002457DF  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
002457E4  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
002457E9  E8 9E 5E 0E 00                  call 0x14032b68c
002457EE  4C 8B 54 24 30                  mov r10, qword ptr [rsp + 0x30]
002457F3  4D 89 56 10                     mov qword ptr [r14 + 0x10], r10
002457F7  41 8B 46 20                     mov eax, dword ptr [r14 + 0x20]
002457FB  66 85 C0                        test ax, ax
002457FE  0F 85 04 FF FF FF               jne 0x140245708
00245804  BA 04 00 00 00                  mov edx, 4
00245809  49 8B CE                        mov rcx, r14
0024580C  E8 EF 47 07 00                  call 0x1402ba000
00245811  E9 F2 FE FF FF                  jmp 0x140245708
00245816  49 8B CE                        mov rcx, r14
00245819  E8 1E E5 12 00                  call 0x140373d3c
0024581E  85 C0                           test eax, eax
00245820  0F 84 52 F8 FF FF               je 0x140245078
00245826  49 8B 46 10                     mov rax, qword ptr [r14 + 0x10]
0024582A  41 0F B6 4E 22                  movzx ecx, byte ptr [r14 + 0x22]
0024582F  C0 E9 04                        shr cl, 4
00245832  A8 04                           test al, 4
00245834  F6 D1                           not cl
00245836  0F 95 C0                        setne al
00245839  22 C8                           and cl, al
0024583B  F6 C1 01                        test cl, 1
0024583E  0F 84 34 F8 FF FF               je 0x140245078
00245844  49 8B 46 10                     mov rax, qword ptr [r14 + 0x10]
00245848  48 83 E0 FB                     and rax, 0xfffffffffffffffb
0024584C  49 89 46 10                     mov qword ptr [r14 + 0x10], rax
00245850  E9 23 F8 FF FF                  jmp 0x140245078
00245855  F0 48 21 58 18                  lock and qword ptr [rax + 0x18], rbx
0024585A  4C 8B 7D 57                     mov r15, qword ptr [rbp + 0x57]
0024585E  E9 F0 FD FF FF                  jmp 0x140245653
00245863  33 D2                           xor edx, edx
00245865  49 8B CE                        mov rcx, r14
00245868  E8 83 F1 1B 00                  call 0x1404049f0
0024586D  4C 8B F0                        mov r14, rax
00245870  48 85 C0                        test rax, rax
00245873  0F 85 2C FB FF FF               jne 0x1402453a5
00245879  4C 8B F7                        mov r14, rdi
0024587C  E9 3E FB FF FF                  jmp 0x1402453bf
00245881  BF 34 04 00 C0                  mov edi, 0xc0000434
00245886  A8 10                           test al, 0x10
00245888  0F 84 C5 F7 FF FF               je 0x140245053
0024588E  E9 F5 F7 FF FF                  jmp 0x140245088
00245893  49 8B 46 28                     mov rax, qword ptr [r14 + 0x28]
00245897  48 0F BA E0 28                  bt rax, 0x28
0024589C  0F 82 1D FB FF FF               jb 0x1402453bf
002458A2  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
002458A6  4C 8B CB                        mov r9, rbx
002458A9  4D 8B C7                        mov r8, r15
002458AC  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
002458B1  BA 11 04 00 00                  mov edx, 0x411
002458B6  B9 1A 00 00 00                  mov ecx, 0x1a
002458BB  E8 A0 7D 2B 00                  call 0x1404fd660
002458C0  CC                              int3
002458C1  BF 34 04 00 C0                  mov edi, 0xc0000434
002458C6  E9 A1 FE FF FF                  jmp 0x14024576c
002458CB  41 8B 46 20                     mov eax, dword ptr [r14 + 0x20]
002458CF  89 45 7F                        mov dword ptr [rbp + 0x7f], eax
002458D2  C1 E8 10                        shr eax, 0x10
002458D5  24 FB                           and al, 0xfb
002458D7  0C 03                           or al, 3
002458D9  88 85 81 00 00 00               mov byte ptr [rbp + 0x81], al
002458DF  8B 45 7F                        mov eax, dword ptr [rbp + 0x7f]
002458E2  41 89 46 20                     mov dword ptr [r14 + 0x20], eax
002458E6  F0 49 21 5E 18                  lock and qword ptr [r14 + 0x18], rbx
002458EB  8B C7                           mov eax, edi
002458ED  E9 85 F4 FF FF                  jmp 0x140244d77
002458F2  8B 05 C0 11 D8 00               mov eax, dword ptr [rip + 0xd811c0]
002458F8  A8 40                           test al, 0x40
002458FA  0F 84 90 FC FF FF               je 0x140245590
00245900  E8 8B 9B 0C 00                  call 0x14030f490
00245905  84 C0                           test al, al
00245907  0F 84 83 FC FF FF               je 0x140245590
0024590D  41 8B CF                        mov ecx, r15d
00245910  E8 4B 9B 0C 00                  call 0x14030f460
00245915  E9 78 FC FF FF                  jmp 0x140245592
0024591A  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
0024591E  48 85 C0                        test rax, rax
00245921  0F 84 0D F6 FF FF               je 0x140244f34
00245927  41 83 FF 01                     cmp r15d, 1
0024592B  0F 84 41 F4 FF FF               je 0x140244d72
00245931  45 85 FF                        test r15d, r15d
00245934  0F 85 57 F6 FF FF               jne 0x140244f91
0024593A  B8 12 01 00 00                  mov eax, 0x112
0024593F  E9 33 F4 FF FF                  jmp 0x140244d77
00245944  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00245948  E9 36 F6 FF FF                  jmp 0x140244f83
0024594D  33 D2                           xor edx, edx
0024594F  E8 00 00 13 00                  call 0x140375954
00245954  BF 34 04 00 C0                  mov edi, 0xc0000434
00245959  F0 49 21 5E 18                  lock and qword ptr [r14 + 0x18], rbx
0024595E  8B C7                           mov eax, edi
00245960  E9 12 F4 FF FF                  jmp 0x140244d77
00245965  49 8B 46 28                     mov rax, qword ptr [r14 + 0x28]
00245969  48 8B 0D 18 A7 BE 00            mov rcx, qword ptr [rip + 0xbea718]
00245970  48 C1 E8 2B                     shr rax, 0x2b
00245974  25 FF 03 00 00                  and eax, 0x3ff
00245979  48 8B 14 C1                     mov rdx, qword ptr [rcx + rax*8]
0024597D  48 8B 45 77                     mov rax, qword ptr [rbp + 0x77]
00245981  48 89 10                        mov qword ptr [rax], rdx
00245984  E9 59 FD FF FF                  jmp 0x1402456e2
00245989  41 8B 46 20                     mov eax, dword ptr [r14 + 0x20]
0024598D  89 45 5F                        mov dword ptr [rbp + 0x5f], eax
00245990  C1 E8 10                        shr eax, 0x10
00245993  24 FA                           and al, 0xfa
00245995  0C 02                           or al, 2
00245997  88 45 61                        mov byte ptr [rbp + 0x61], al
0024599A  8B 45 5F                        mov eax, dword ptr [rbp + 0x5f]
0024599D  41 89 46 20                     mov dword ptr [r14 + 0x20], eax
002459A1  E9 3E FC FF FF                  jmp 0x1402455e4
002459A6  49 8B 46 28                     mov rax, qword ptr [r14 + 0x28]
002459AA  48 8B 0D D7 A6 BE 00            mov rcx, qword ptr [rip + 0xbea6d7]
002459B1  48 C1 E8 2B                     shr rax, 0x2b
002459B5  25 FF 03 00 00                  and eax, 0x3ff
002459BA  48 8B 14 C1                     mov rdx, qword ptr [rcx + rax*8]
002459BE  48 8B 45 77                     mov rax, qword ptr [rbp + 0x77]
002459C2  48 89 10                        mov qword ptr [rax], rdx
002459C5  E9 07 FE FF FF                  jmp 0x1402457d1
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiActOnPte(__int64 a1, int a2, __int64 a3, __int64 a4, unsigned int a5, unsigned int a6, __int64 a7, unsigned int a8)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m3F;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned int v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int8 v_stack_p22;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int8 v_stack_p42;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p8;

    v_stack_p10 = v_rbx;
    v_stack_p18 = a3;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (208);
    v_rdi = 0;
    v_stack_mC8 = 0;
    v_stack_mD0 = 0;
    *(unsigned __int64 *)(a8) = 0;
    *(unsigned __int64 *)(a7) = 0;
    v_stack_mC0 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1024;
loc_00244CFE:
    if (a4 != 0) goto loc_00245653;
    result = MI_READ_PTE_LOCK_FREE(a3, a2, a3, a4);
    v_stack_mD8 = result;
loc_00244D23:
    if ((((unsigned __int8)(result)) & (1)) == 0) goto loc_00244D93;
    if (a4 != 0) goto loc_00244EC8;
    result = (result) >> (12);
    result = (result) & (result);
    if (result > (*(unsigned __int64 *)(v_rip + 12488595))) goto loc_00244D72;
    a1 = (result + result * 2) + (result + result * 2);
    if (condition_is_below) goto loc_00244F03;
loc_00244D72:
loc_00244D77:
    v_rsp = (v_rsp) + (208);
    return (unsigned int)(0xC0000434ULL);
loc_00244D93:
    if (condition_is_below) goto loc_00244EBB;
    if (condition_is_below) goto loc_002452C2;
    if (((unsigned int)((unsigned int)(a5))) == 2) goto loc_00244EBB;
    if (result == 0) goto loc_002454AE;
    if (a4 != 0) goto loc_0024527F;
loc_00244DD9:
    result = IS_PTE_NOT_DEMAND_ZERO(result, *(unsigned __int64 *)(v_rip + 12497596), result, result);
    if ((unsigned int)(result) != 0) goto loc_00245438;
    if (((unsigned int)((unsigned int)(a5))) == 1) goto loc_0024522B;
    result = (unsigned __int8)(((unsigned __int8)(result)) >> (1));
    if ((((unsigned __int8)(result)) & (1)) != 0) goto loc_002451E2;
loc_00244E00:
    result = MiUpdatePageFileHighInPte(result, 1, result, result);
    v_stack_p30 = result;
    v_r15 = (unsigned int)(a5);
    if (a4 != 0) { v_r15 = a4; }
    *(unsigned __int64 *)(v_r15) = result;
    result = 0;
    goto loc_00244D77;
loc_00244E23:
    result = (*(unsigned __int64 *)(v_r14 + 16)) & (-5);
    *(unsigned __int64 *)(v_r14 + 16) = result;
loc_00244E2F:
    *(unsigned __int64 *)(a8) = result;
    if (result != 0) goto loc_00245619;
loc_00244E3F:
    if (*(unsigned __int64 *)(v_r14 + 16) == 0) goto loc_00244E64;
    if (*(unsigned __int64 *)(v_rip + 12488241) == 0) goto loc_00244E64;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_r14 + 16))) & (16)) != 0) goto loc_00244EC2;
    v_rdi = ~(*(unsigned __int64 *)(v_rip + 12488241));
    v_rdi = (v_rdi) & (*(unsigned __int64 *)(v_r14 + 16));
loc_00244E64:
    a1 = ((unsigned int)((unsigned int)(v_rdi))) | (*(unsigned __int64 *)(v_r14 + 16));
    result = MiSwizzleInvalidPte(a1, a8, result, result);
    v_stack_p40 = result;
    result = MI_READ_PTE_LOCK_FREE(v_stack_p40, a8, result, result);
    result = (result) & (-3);
    v_stack_p40 = result;
    *(unsigned __int64 *)(v_r14 + 16) = v_stack_p40;
    if (a4 != 0) goto loc_00244EBB;
    if ((((unsigned __int8)(v_stack_p30)) & (66)) != 0) goto loc_002450FD;
loc_00244EBB:
    result = 0;
    goto loc_00244D77;
loc_00244EC2:
    v_rdi = (v_rdi) & (-17);
    goto loc_00244E64;
loc_00244EC8:
    a2 = 0;
    result = MiLockLeafPage(a4, a2, result, result);
    if (result == 0) goto loc_0024585A;
    v_stack_p30 = *(unsigned __int64 *)(a4);
    if ((((unsigned __int8)(*(unsigned __int64 *)(a4))) & (1)) == 0) goto loc_00245855;
    goto loc_00244FC4;
loc_00244F03:
    if ((((unsigned int)(a2)) & (*(unsigned __int64 *)(result + *(unsigned __int64 *)(a4) * 8 + 40))) != 0) goto loc_00244F34;
    if (!sign_flag) goto loc_0024591A;
loc_00244F34:
    a2 = 0;
    v_rbx = (*(unsigned __int64 *)(result + *(unsigned __int64 *)(a4) * 8 + 8)) | (*(unsigned __int64 *)(result + *(unsigned __int64 *)(a4) * 8 + 8));
    result = memset(v_stack_mA8, a2, a2 + 112, result);
    if (*(unsigned __int64 *)(v_stack_p18 + 640) == 0) goto loc_00244F91;
    v_stack_m90 = v_rbx;
    v_stack_m88 = v_rbx;
loc_00244F70:
    if (v_rbx > (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p18 + 640) + 32))) goto loc_00245944;
    if (v_rbx >= (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p18 + 640) + 24))) goto loc_00244F88;
loc_00244F83:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p18 + 640)) != 0) goto loc_00244F70;
loc_00244F88:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p18 + 640)) != 0) goto loc_002450EE;
loc_00244F91:
loc_00244F93:
    if (condition_is_below) goto loc_002450C0;
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(v_stack_p8 + 48))) & (112));
    if (((unsigned __int8)(result)) == 64) goto loc_0024525B;
loc_00244FB5:
loc_00244FC4:
    if (((unsigned int)(v_r15)) == 2) goto loc_0024515A;
    if ((((unsigned __int8)(*(unsigned __int8 *)(result + *(unsigned __int64 *)(a4) * 8 + 34))) & (8)) != 0) goto loc_002450DF;
    a2 = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(result + *(unsigned __int64 *)(a4) * 8 + 34))) & (16));
    if (((unsigned int)(v_r15)) == 1) goto loc_0024503D;
    if ((unsigned __int8)(a2) == 0) goto loc_00245012;
    v_stack_p20 = (unsigned int)((unsigned int)(*(unsigned int *)(result + *(unsigned __int64 *)(a4) * 8 + 32)));
    v_r11 = (unsigned int)(((unsigned int)(*(unsigned int *)(result + *(unsigned __int64 *)(a4) * 8 + 32))) >> (16));
    if ((((unsigned __int8)(v_r11)) & (8)) != 0) goto loc_00245714;
loc_00245005:
    v_rbx = (unsigned __int8)(((unsigned __int8)(v_r11)) & (239));
    v_stack_p22 = (unsigned __int8)(v_rbx);
    *(unsigned int *)(result + *(unsigned __int64 *)(a4) * 8 + 32) = (unsigned int)((unsigned int)(v_stack_p20));
loc_00245012:
    result = (unsigned __int8)(((unsigned __int8)(*(unsigned __int64 *)(result + *(unsigned __int64 *)(a4) * 8 + 16))) >> (2));
    if ((((unsigned __int8)(result)) & (1)) != 0) goto loc_00244E23;
    result = (unsigned __int8)(((unsigned __int8)(*(unsigned __int64 *)(result + *(unsigned __int64 *)(a4) * 8 + 16))) >> (1));
    if ((((unsigned __int8)(result)) & (1)) != 0) goto loc_00244E2F;
    *(unsigned __int64 *)(a8) = v_rdi;
    goto loc_00244E3F;
loc_0024503D:
    if ((unsigned __int8)(a8) != 0) goto loc_00245881;
    if (a4 != 0) goto loc_00245053;
    if ((((unsigned __int8)(*(unsigned __int64 *)(result + *(unsigned __int64 *)(a4) * 8 + 16))) & (66)) != 0) goto loc_00245881;
loc_00245053:
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(result + *(unsigned __int64 *)(a4) * 8 + 16))) >> (2));
    if ((((unsigned __int8)(result)) & (1)) != 0) goto loc_00245088;
    v_stack_p40 = (unsigned int)((unsigned int)(*(unsigned int *)(result + *(unsigned __int64 *)(a4) * 8 + 32)));
    v_r11 = (unsigned int)(((unsigned int)(*(unsigned int *)(result + *(unsigned __int64 *)(a4) * 8 + 32))) >> (16));
    if ((((unsigned __int8)(v_r11)) & (8)) != 0) goto loc_00245816;
loc_00245078:
    v_rbx = (unsigned __int8)(((unsigned __int8)(v_r11)) | (16));
    v_stack_p42 = (unsigned __int8)(v_rbx);
    *(unsigned int *)(result + *(unsigned __int64 *)(a4) * 8 + 32) = (unsigned int)((unsigned int)(a8));
loc_00245088:
    result = MI_IS_RESET_PTE(*(unsigned __int64 *)(result + *(unsigned __int64 *)(a4) * 8 + 16), a8, a2 + 112, result);
    if ((unsigned int)(result) == 0) goto loc_00245221;
    result = MiClearResetPfn(result + *(unsigned __int64 *)(a4) * 8, a8, a2 + 112, result);
loc_002450A1:
    goto loc_00244D77;
loc_002450C0:
    v_rbx = (unsigned int)((v_rbx) + 1);
    if (((*(unsigned int *)(v_rip + 14156260)) & ((unsigned int)(v_rbx))) == 0) goto loc_00245487;
loc_002450CE:
loc_002450D0:
    if (!sign_flag) goto loc_00244F93;
    goto loc_002450C0;
loc_002450DF:
    goto loc_00244D77;
loc_002450EE:
    if ((*(unsigned __int64 *)((unsigned int)(0xC0000434ULL) + 48)) == v_rdi) goto loc_00244F91;
    goto loc_00244D72;
loc_002450FD:
    a2 = (a8) & (-99);
    v_stack_p30 = a2;
    result = MiWriteValidPteNewProtection(v_stack_p18, a2, a2 + 112, result);
    v_rsi = (v_stack_p18) << (25);
    result = (result) << (25);
    v_rsi = (v_rsi) - (result);
    v_rsi = (v_rsi) >> (16);
    result = MiGetVaAge(v_stack_p18, v_rsi, a2 + 112, result);
    if (((unsigned __int8)(result)) == 1) goto loc_00245150;
    if (((unsigned __int8)(result)) < 7) {
        a1 = v_stack_p48;
        a4 = 1;
        a3 = 1;
        a2 = v_rsi;
        result = MiSetVaAgeList(a1, a2, a3, a4);
    }
    goto loc_00244D77;
loc_0024515A:
    v_rdi = (a4 == 0) ? 1 : 0;
    result = MiUpdatePfnPriority(result + *(unsigned __int64 *)(a4) * 8, (unsigned int)(a6), (unsigned int)((unsigned int)(v_rdi)), a4);
    if (((unsigned __int8)(result)) == 255) goto loc_00245191;
    if (a4 == 0) {
        a3 = (unsigned __int8)(result);
        a2 = v_rsi;
        a1 = v_stack_p48;
        result = MiUpdateWsleAge(a1, a2, a3, a4);
    }
    if ((((unsigned int)(a2)) & (*(unsigned __int64 *)(result + *(unsigned __int64 *)(a4) * 8 + 40))) != 0) goto loc_00244EBB;
    if (sign_flag) goto loc_00244EBB;
    if (*(unsigned __int64 *)(result + *(unsigned __int64 *)(a4) * 8 + 8) == 0) goto loc_00244EBB;
    if (a4 != 0) goto loc_00244EBB;
    a3 = (*(unsigned __int64 *)(result + *(unsigned __int64 *)(a4) * 8 + 8)) | (*(unsigned __int64 *)(result + *(unsigned __int64 *)(a4) * 8 + 8));
    result = MiDemoteCombinedPte(v_stack_p48, v_rsi, a3, a4);
    goto loc_00244EBB;
loc_002451E2:
    v_stack_p38 = a3;
    if (condition_is_below) goto loc_0024520D;
    result = (unsigned __int8)(((unsigned __int8)(a7)) >> (2));
    if ((((unsigned __int8)(result)) & (1)) != 0) goto loc_00245204;
    result = (unsigned __int8)(((unsigned __int8)(a7)) >> (1));
    if ((((unsigned __int8)(result)) & (1)) == 0) goto loc_0024520D;
loc_00245204:
    if (a7 != 0) goto loc_0024569F;
loc_0024520D:
    result = MiClearPageFileReservation(v_stack_p30, a7, a3, a4);
    goto loc_00244E00;
loc_00245221:
    goto loc_002450A1;
loc_0024522B:
    result = MI_IS_RESET_PTE(v_stack_p30, a7, v_stack_p30, a4);
    if ((unsigned int)(result) == 0) goto loc_00244D72;
    result = MI_CLEAR_RESET_PTE(v_stack_p30, a7, v_stack_p30, a4);
    if (a4 != 0) { v_r15 = a4; }
    *(unsigned __int64 *)(v_r15) = v_stack_p30;
    result = 0;
    goto loc_00244D77;
loc_0024525B:
    result = MiRotatedToFrameBuffer(v_rsi, a7, v_stack_p30, a4);
    if ((unsigned int)(result) == 0) goto loc_00244FB5;
    goto loc_00244D72;
loc_0024527F:
    if ((unsigned int)((unsigned int)(a2)) != 0) goto loc_00245543;
    if (((*(unsigned int *)(v_stack_p8 + 48)) & (0x200000ULL)) != 0) goto loc_00244DD9;
    if (*(unsigned __int64 *)(v_stack_p8 + 72) == 0) goto loc_00244DD9;
    a1 = (unsigned __int16)((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + 72)) + 60)) & ((unsigned __int16)((unsigned int)(0x3FFULL))));
    goto loc_00244DD9;
loc_002452C2:
    if (a4 != 0) goto loc_0024568D;
loc_002452CB:
    result = MI_READ_PTE_LOCK_FREE(v_r15, a7, v_stack_p30, a4);
    if (condition_is_above_or_equal) goto loc_00245879;
    result = MiInvalidPteConforms(result, a7, v_stack_p30, a4);
    if ((unsigned int)(result) == 0) goto loc_002452CB;
    if (*(unsigned __int64 *)(v_rip + 12487052) == 0) goto loc_0024530B;
    if ((((unsigned __int8)(result)) & (16)) != 0) goto loc_0024553A;
    a1 = ~(*(unsigned __int64 *)(v_rip + 12487052));
    a1 = (a1) & (result);
loc_0024530B:
    a1 = (a1) >> (12);
    a1 = (a1) & (*(unsigned __int64 *)(v_rip + 12487052));
    a2 = (a1 + a1 * 2) + (a1 + a1 * 2);
    if (a1 > (*(unsigned __int64 *)(v_rip + 12487081))) goto loc_002452CB;
    if (a1 >= (*(unsigned __int64 *)(v_rip + 12487081))) goto loc_002452CB;
loc_00245360:
    if (a1 < (*(unsigned __int64 *)(v_rip + 12487081))) goto loc_00245580;
    result = MI_READ_PTE_LOCK_FREE(v_stack_p18, a2, v_stack_p30, a4);
    if (result != result) goto loc_002456B2;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12487052) + a2 * 8 + 40)) >> (43);
    result = (unsigned int)((result) & (0x3FFULL));
    if (sign_flag) goto loc_00245863;
loc_002453A5:
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12487052) + a2 * 8 + 8)) | (*(unsigned __int64 *)(v_rip + 12496123));
    if (result != v_stack_p18) goto loc_00245893;
loc_002453BF:
loc_002453C9:
    if (*(unsigned __int64 *)(v_rip + 12487052) + a2 * 8 == 0) goto loc_00244CFE;
    if (a4 != 0) goto loc_0024563D;
loc_002453DB:
    if (((unsigned int)((unsigned int)(a5))) == 2) goto loc_00245670;
    a2 = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 12487052) + a2 * 8 + 34))) & (7));
    if (((unsigned __int8)(a2)) != 2) goto loc_002455A1;
    if (((unsigned int)((unsigned int)(a5))) == 1) goto loc_00245753;
    if ((((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 12487052) + a2 * 8 + 34))) & (40)) != 0) goto loc_00245708;
    result = (unsigned __int8)(((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12487052) + a2 * 8 + 16))) >> (2));
    if ((((unsigned __int8)(result)) & (1)) != 0) goto loc_002456C6;
    result = (unsigned __int8)(((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12487052) + a2 * 8 + 16))) >> (1));
    if ((((unsigned __int8)(result)) & (1)) != 0) goto loc_002456D2;
    *(unsigned __int64 *)(a8) = (unsigned int)(0xC0000434ULL);
    goto loc_002456E2;
loc_00245438:
    if (((unsigned int)(result)) == 1) goto loc_00244D72;
    a3 = 0;
    result = MiCapturePageFileInfoInline(v_stack_p30, a3 + 1, a3, a4);
    *(unsigned __int64 *)(a8) = result;
    if (result == 0) goto loc_00244EBB;
    *(unsigned __int64 *)(a7) = *(unsigned __int64 *)(a7 + (unsigned __int16)(a1) * 8);
    v_r13 = a4;
    if (a4 == 0) {
        v_r13 = v_stack_p18;
    }
    *(unsigned __int64 *)(v_r13) = v_stack_p30;
    goto loc_00244EBB;
loc_00245487:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14161451)))) & (64)) == 0) goto loc_002450CE;
    result = KiCheckVpBackingLongSpinWaitHypercall(v_stack_p30, a8, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_002450CE;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(result)), a8, a3, a4);
    goto loc_002450D0;
loc_002454AE:
    if (v_r13 != 0) goto loc_00244D72;
    if ((unsigned int)(result) != 0) goto loc_00244D72;
    v_rbx = (v_stack_p18) << (25);
    result = (result) << (25);
    v_rbx = (v_rbx) - (result);
    v_rbx = (v_rbx) >> (16);
    result = MiCheckUserVirtualAddress(v_rbx, v_stack_p8, a3, v_stack_p38);
    if (result != 0) goto loc_00244D72;
    if (((unsigned int)((unsigned int)(v_stack_p38))) == 24) goto loc_00244D72;
    result = MiUpdatePageTableUseCount(v_rbx, result + 1, a3, v_stack_p38);
    a2 = ((unsigned int)((unsigned int)((unsigned int)(v_stack_p38)))) << (5);
    result = MiMakePageFilePte(v_r13 + 1, a2, a3, v_stack_p38);
    result = (result) ^ (a2);
    result = (result) & (-993);
    result = (result) ^ (a2);
    v_stack_p30 = result;
    *(unsigned __int64 *)(v_stack_p18) = result;
    result = 0;
    goto loc_00244D77;
loc_0024553A:
    a1 = (v_r13 + 1) & (-17);
    goto loc_0024530B;
loc_00245543:
    a2 = (v_stack_p18) << (25);
    result = (0) << (25);
    a2 = (a2) - (result);
    a2 = (a2) >> (16);
    result = MiSharedVaToPartition(v_rsi + 1024, a2, v_r13, v_stack_p38);
    goto loc_00244DD9;
loc_00245580:
    v_r15 = (unsigned int)((v_stack_p18) + 1);
    if (((*(unsigned int *)(v_rip + 14155042)) & ((unsigned int)(v_r15))) == 0) goto loc_002458F2;
loc_00245590:
loc_00245592:
    if (!sign_flag) goto loc_00245360;
    goto loc_00245580;
loc_002455A1:
    if (((unsigned __int8)(a2)) != 3) goto loc_00245708;
    if (((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12487052) + a2 * 8 + 24))) == 1) goto loc_00245954;
    if ((((unsigned __int8)(v_rsi + 1024)) & (8)) != 0) goto loc_00245708;
    if ((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12487052) + a2 * 8 + 24)) != 0) goto loc_00245708;
    if ((((unsigned __int8)(v_rsi + 1024)) & (32)) != 0) goto loc_00245708;
    if ((unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12487052) + a2 * 8 + 32))) != 0) goto loc_00245989;
    a2 = 0;
    result = MiUnlinkPageFromListEx(*(unsigned __int64 *)(v_rip + 12487052) + a2 * 8, a2, v_stack_p30, v_stack_p38);
loc_002455E4:
    a2 = 0;
    result = MiSetPfnModified(*(unsigned __int64 *)(v_rip + 12487052) + a2 * 8, a2, v_stack_p30, v_stack_p38);
    result = (unsigned __int8)(((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12487052) + a2 * 8 + 16))) >> (2));
    if ((((unsigned __int8)(result)) & (1)) != 0) goto loc_002457B5;
    result = (unsigned __int8)(((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12487052) + a2 * 8 + 16))) >> (1));
    if ((((unsigned __int8)(result)) & (1)) != 0) goto loc_002457C1;
    *(unsigned __int64 *)(a8) = (unsigned int)(v_stack_p38);
    goto loc_002457D1;
loc_00245619:
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12487052) + a2 * 8 + 40)) >> (43);
    result = (unsigned int)((result) & (0x3FFULL));
    *(unsigned __int64 *)(a7) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12495460) + result * 8);
    goto loc_00244E3F;
loc_0024563D:
    v_stack_p30 = *(unsigned __int64 *)(v_r13);
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_r13))) & (1)) == 0) goto loc_002453DB;
loc_00245653:
    v_stack_p30 = *(unsigned __int64 *)(v_r13);
    goto loc_00244D23;
loc_00245670:
    result = MiUpdatePfnPriority(*(unsigned __int64 *)(v_rip + 12487052) + a2 * 8, (unsigned int)(a6), 1, *(unsigned __int64 *)(v_r13));
    result = 0;
    goto loc_00244D77;
loc_0024568D:
    a2 = 0;
    result = MiLockLeafPage(v_r13, a2, 1, *(unsigned __int64 *)(v_r13));
    goto loc_002453C9;
loc_0024569F:
    result = MiReleasePageFileInfo(*(unsigned __int64 *)(v_r13), a2, 1, *(unsigned __int64 *)(v_r13));
    goto loc_0024520D;
loc_002456B2:
    goto loc_002452CB;
loc_002456C6:
    result = (*(unsigned __int64 *)(result + 16)) & (-5);
    *(unsigned __int64 *)(result + 16) = result;
loc_002456D2:
    *(unsigned __int64 *)(a8) = *(unsigned __int64 *)(v_r13);
    if (*(unsigned __int64 *)(v_r13) != 0) goto loc_00245965;
loc_002456E2:
    result = MiUpdatePageFileHighInPte(*(unsigned __int64 *)(result + 16), 1, 1, *(unsigned __int64 *)(v_r13));
    v_stack_p30 = result;
    result = MiClearPageFileReservation(v_stack_p30, 1, 1, *(unsigned __int64 *)(v_r13));
    *(unsigned __int64 *)(result + 16) = v_stack_p30;
loc_00245708:
    goto loc_00244D77;
loc_00245714:
    result = MiCanPfnOriginalPteBeLost(result, 1, 1, *(unsigned __int64 *)(v_r13));
    if ((unsigned int)(result) == 0) goto loc_00245005;
    a1 = (unsigned __int8)((*(unsigned __int8 *)(result + 34)) >> (4));
    a1 = (unsigned __int8)(~(a1));
    result = ((((unsigned __int8)(*(unsigned __int64 *)(result + 16))) & (4)) != 0) ? 1 : 0;
    a1 = (unsigned __int8)((a1) & ((unsigned __int8)(result)));
    if ((((unsigned __int8)(a1)) & (1)) == 0) goto loc_00245005;
    result = (*(unsigned __int64 *)(result + 16)) & (-5);
    *(unsigned __int64 *)(result + 16) = result;
    goto loc_00245005;
loc_00245753:
    result = MI_IS_RESET_PTE(*(unsigned __int64 *)(result + 16), 1, 1, *(unsigned __int64 *)(v_r13));
    if ((unsigned int)(result) == 0) goto loc_002458C1;
    result = MiClearResetPfn(result, 1, 1, *(unsigned __int64 *)(v_r13));
loc_0024576C:
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(result + 16))) >> (2));
    if ((((unsigned __int8)(result)) & (1)) != 0) goto loc_00245708;
    result = MiSetPfnModified(result, 1, 1, *(unsigned __int64 *)(v_r13));
    if ((unsigned __int16)((unsigned int)(*(unsigned int *)(result + 32))) != 0) goto loc_002458CB;
    a2 = 0;
    result = MiUnlinkPageFromListEx(result, a2, 1, *(unsigned __int64 *)(v_r13));
    if ((((unsigned __int8)(result)) & (3)) != 0) goto loc_0024594D;
    result = MiInsertPageInList(result, 8, 1, *(unsigned __int64 *)(v_r13));
    goto loc_00245708;
loc_002457B5:
    result = (*(unsigned __int64 *)(result + 16)) & (-5);
    *(unsigned __int64 *)(result + 16) = result;
loc_002457C1:
    *(unsigned __int64 *)(a8) = result;
    if (result != 0) goto loc_002459A6;
loc_002457D1:
    result = MiUpdatePageFileHighInPte(*(unsigned __int64 *)(result + 16), 1, 1, *(unsigned __int64 *)(v_r13));
    v_stack_p30 = result;
    result = MiClearPageFileReservation(v_stack_p30, 1, 1, *(unsigned __int64 *)(v_r13));
    *(unsigned __int64 *)(result + 16) = v_stack_p30;
    if ((unsigned __int16)((unsigned int)(*(unsigned int *)(result + 32))) != 0) goto loc_00245708;
    result = MiInsertPageInList(result, 4, 1, *(unsigned __int64 *)(v_r13));
    goto loc_00245708;
loc_00245816:
    result = MiCanPfnOriginalPteBeLost(result, 4, 1, *(unsigned __int64 *)(v_r13));
    if ((unsigned int)(result) == 0) goto loc_00245078;
    a1 = (unsigned __int8)((*(unsigned __int8 *)(result + 34)) >> (4));
    a1 = (unsigned __int8)(~(a1));
    result = ((((unsigned __int8)(*(unsigned __int64 *)(result + 16))) & (4)) != 0) ? 1 : 0;
    a1 = (unsigned __int8)((a1) & ((unsigned __int8)(result)));
    if ((((unsigned __int8)(a1)) & (1)) == 0) goto loc_00245078;
    result = (*(unsigned __int64 *)(result + 16)) & (-5);
    *(unsigned __int64 *)(result + 16) = result;
    goto loc_00245078;
loc_00245855:
loc_0024585A:
    goto loc_00245653;
loc_00245863:
    a2 = 0;
    result = MiLockSpecialPurposeMemoryCachedPage(result, a2, 1, *(unsigned __int64 *)(v_r13));
    if (result != 0) goto loc_002453A5;
loc_00245879:
    goto loc_002453BF;
loc_00245881:
    if ((((unsigned __int8)(result)) & (16)) == 0) goto loc_00245053;
    goto loc_00245088;
loc_00245893:
    if (condition_is_below) goto loc_002453BF;
    v_stack_p20 = *(unsigned __int64 *)((unsigned int)(v_stack_p38) + 8);
    result = KeBugCheckEx(26, (unsigned int)(0x411ULL), v_stack_p18, v_rbx);
loc_002458C1:
    goto loc_0024576C;
loc_002458CB:
    v_stack_p40 = (unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(v_stack_p38) + 32)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)((unsigned int)(v_stack_p38) + 32))) >> (16));
    result = (unsigned __int8)((result) & (251));
    result = (unsigned __int8)((result) | (3));
    v_stack_p42 = (unsigned __int8)(result);
    *(unsigned int *)((unsigned int)(v_stack_p38) + 32) = (unsigned int)((unsigned int)(a8));
    goto loc_00244D77;
loc_002458F2:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14160320)))) & (64)) == 0) goto loc_00245590;
    result = KiCheckVpBackingLongSpinWaitHypercall(26, (unsigned int)(0x411ULL), v_stack_p18, v_rbx);
    if ((unsigned __int8)(result) == 0) goto loc_00245590;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_stack_p18)), (unsigned int)(0x411ULL), v_stack_p18, v_rbx);
    goto loc_00245592;
loc_0024591A:
    if (*(unsigned __int64 *)((unsigned int)(v_stack_p38) + 8) == 0) goto loc_00244F34;
    if (((unsigned int)(v_stack_p18)) == 1) goto loc_00244D72;
    if ((unsigned int)(v_stack_p18) != 0) goto loc_00244F91;
    goto loc_00244D77;
loc_00245944:
    goto loc_00244F83;
loc_0024594D:
    a2 = 0;
    result = MiDiscardTransitionPteEx((unsigned int)((unsigned int)(v_stack_p18)), a2, v_stack_p18, v_rbx);
loc_00245954:
    goto loc_00244D77;
loc_00245965:
    result = (*(unsigned __int64 *)((unsigned int)(v_stack_p38) + 40)) >> (43);
    result = (unsigned int)((result) & (0x3FFULL));
    *(unsigned __int64 *)(a7) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12494616) + result * 8);
    goto loc_002456E2;
loc_00245989:
    v_stack_p20 = (unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(v_stack_p38) + 32)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)((unsigned int)(v_stack_p38) + 32))) >> (16));
    result = (unsigned __int8)((result) & (250));
    result = (unsigned __int8)((result) | (2));
    v_stack_p22 = (unsigned __int8)(result);
    *(unsigned int *)((unsigned int)(v_stack_p38) + 32) = (unsigned int)((unsigned int)(v_stack_p20));
    goto loc_002455E4;
loc_002459A6:
    result = (*(unsigned __int64 *)((unsigned int)(v_stack_p38) + 40)) >> (43);
    result = (unsigned int)((result) & (0x3FFULL));
    *(unsigned __int64 *)(a7) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12494551) + result * 8);
    goto loc_002457D1;
}
```

## 5. (Beta) C Style

```c
int64_t MiActOnPte(int64_t Arg1, int32_t Arg2, int64_t Arg3, int64_t Arg4, uint32_t Arg5, uint32_t Arg6, void *Arg7, void *Arg8)
{
    uint8_t *arg7 = (uint8_t *)Arg7;
    uint8_t *arg8 = (uint8_t *)Arg8;

    int64_t result;
    int64_t local_r11;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m3F;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint32_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint32_t v_stack_p20;
    uint8_t v_stack_p22;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint8_t v_stack_p42;
    uint64_t v_stack_p48;
    uint64_t v_stack_p8;

    v_stack_p10 = local_rbx;
    v_stack_p18 = Arg3;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (208);
    local_rdi = 0;
    v_stack_mC8 = 0;
    v_stack_mD0 = 0;
    *(uint64_t *)(arg8) = 0;
    *(uint64_t *)(arg7) = 0;
    v_stack_mC0 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 1024;
loc_00244CFE:
    if (Arg4 != 0) goto loc_00245653;
    result = MI_READ_PTE_LOCK_FREE(Arg3, Arg2, Arg3, Arg4);
    v_stack_mD8 = result;
loc_00244D23:
    if ((((uint8_t)(result)) & (1)) == 0) goto loc_00244D93;
    if (Arg4 != 0) goto loc_00244EC8;
    result = (result) >> (12);
    result = (result) & (result);
    if (result > (*(uint64_t *)(v_rip + 0xBE8F93))) goto loc_00244D72;
    Arg1 = (result + result * 2) + (result + result * 2);
    if (condition_is_below) goto loc_00244F03;
loc_00244D72:
loc_00244D77:
    local_rsp = (local_rsp) + (208);
    return (uint32_t)(0xC0000434ULL);
loc_00244D93:
    if (condition_is_below) goto loc_00244EBB;
    if (condition_is_below) goto loc_002452C2;
    if (((uint32_t)((uint32_t)(Arg5))) == 2) goto loc_00244EBB;
    if (result == 0) goto loc_002454AE;
    if (Arg4 != 0) goto loc_0024527F;
loc_00244DD9:
    result = IS_PTE_NOT_DEMAND_ZERO(result, *(uint64_t *)(v_rip + 0xBEB2BC), result, result);
    if ((uint32_t)(result) != 0) goto loc_00245438;
    if (((uint32_t)((uint32_t)(Arg5))) == 1) goto loc_0024522B;
    result = (uint8_t)(((uint8_t)(result)) >> (1));
    if ((((uint8_t)(result)) & (1)) != 0) goto loc_002451E2;
loc_00244E00:
    result = MiUpdatePageFileHighInPte(result, 1, result, result);
    v_stack_p30 = result;
    local_r15 = (uint32_t)(Arg5);
    if (Arg4 != 0) { local_r15 = Arg4; }
    *(uint64_t *)(local_r15) = result;
    result = 0;
    goto loc_00244D77;
loc_00244E23:
    result = (*(uint64_t *)(local_r14 + 0x10)) & (-5);
    *(uint64_t *)(local_r14 + 0x10) = result;
loc_00244E2F:
    *(uint64_t *)(arg8) = result;
    if (result != 0) goto loc_00245619;
loc_00244E3F:
    if (*(uint64_t *)(local_r14 + 0x10) == 0) goto loc_00244E64;
    if (*(uint64_t *)(v_rip + 0xBE8E31) == 0) goto loc_00244E64;
    if ((((uint8_t)(*(uint64_t *)(local_r14 + 0x10))) & (16)) != 0) goto loc_00244EC2;
    local_rdi = ~(*(uint64_t *)(v_rip + 0xBE8E31));
    local_rdi = (local_rdi) & (*(uint64_t *)(local_r14 + 0x10));
loc_00244E64:
    Arg1 = ((uint32_t)((uint32_t)(local_rdi))) | (*(uint64_t *)(local_r14 + 0x10));
    result = MiSwizzleInvalidPte(Arg1, Arg8, result, result);
    v_stack_p40 = result;
    result = MI_READ_PTE_LOCK_FREE(v_stack_p40, Arg8, result, result);
    result = (result) & (-3);
    v_stack_p40 = result;
    *(uint64_t *)(local_r14 + 0x10) = v_stack_p40;
    if (Arg4 != 0) goto loc_00244EBB;
    if ((((uint8_t)(v_stack_p30)) & (66)) != 0) goto loc_002450FD;
loc_00244EBB:
    result = 0;
    goto loc_00244D77;
loc_00244EC2:
    local_rdi = (local_rdi) & (-17);
    goto loc_00244E64;
loc_00244EC8:
    Arg2 = 0;
    result = MiLockLeafPage(Arg4, Arg2, result, result);
    if (result == 0) goto loc_0024585A;
    v_stack_p30 = *(uint64_t *)(Arg4);
    if ((((uint8_t)(*(uint64_t *)(Arg4))) & (1)) == 0) goto loc_00245855;
    goto loc_00244FC4;
loc_00244F03:
    if ((((uint32_t)(Arg2)) & (*(uint64_t *)(result + *(uint64_t *)(Arg4) * 8 + 0x28))) != 0) goto loc_00244F34;
    if (!sign_flag) goto loc_0024591A;
loc_00244F34:
    Arg2 = 0;
    local_rbx = (*(uint64_t *)(result + *(uint64_t *)(Arg4) * 8 + 0x8)) | (*(uint64_t *)(result + *(uint64_t *)(Arg4) * 8 + 0x8));
    result = memset(v_stack_mA8, Arg2, Arg2 + 112, result);
    if (*(uint64_t *)(v_stack_p18 + 0x280) == 0) goto loc_00244F91;
    v_stack_m90 = local_rbx;
    v_stack_m88 = local_rbx;
loc_00244F70:
    if (local_rbx > (*(uint64_t *)(*(uint64_t *)(v_stack_p18 + 0x280) + 0x20))) goto loc_00245944;
    if (local_rbx >= (*(uint64_t *)(*(uint64_t *)(v_stack_p18 + 0x280) + 0x18))) goto loc_00244F88;
loc_00244F83:
    if (*(uint64_t *)(*(uint64_t *)(v_stack_p18 + 0x280)) != 0) goto loc_00244F70;
loc_00244F88:
    if (*(uint64_t *)(*(uint64_t *)(v_stack_p18 + 0x280)) != 0) goto loc_002450EE;
loc_00244F91:
loc_00244F93:
    if (condition_is_below) goto loc_002450C0;
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x30))) & (112));
    if (((uint8_t)(result)) == 64) goto loc_0024525B;
loc_00244FB5:
loc_00244FC4:
    if (((uint32_t)(local_r15)) == 2) goto loc_0024515A;
    if ((((uint8_t)(*(uint8_t *)(result + *(uint64_t *)(Arg4) * 8 + 0x22))) & (8)) != 0) goto loc_002450DF;
    Arg2 = (uint8_t)(((uint8_t)(*(uint8_t *)(result + *(uint64_t *)(Arg4) * 8 + 0x22))) & (16));
    if (((uint32_t)(local_r15)) == 1) goto loc_0024503D;
    if ((uint8_t)(Arg2) == 0) goto loc_00245012;
    v_stack_p20 = (uint32_t)((uint32_t)(*(uint32_t *)(result + *(uint64_t *)(Arg4) * 8 + 0x20)));
    local_r11 = (uint32_t)(((uint32_t)(*(uint32_t *)(result + *(uint64_t *)(Arg4) * 8 + 0x20))) >> (16));
    if ((((uint8_t)(local_r11)) & (8)) != 0) goto loc_00245714;
loc_00245005:
    local_rbx = (uint8_t)(((uint8_t)(local_r11)) & (239));
    v_stack_p22 = (uint8_t)(local_rbx);
    *(uint32_t *)(result + *(uint64_t *)(Arg4) * 8 + 0x20) = (uint32_t)((uint32_t)(v_stack_p20));
loc_00245012:
    result = (uint8_t)(((uint8_t)(*(uint64_t *)(result + *(uint64_t *)(Arg4) * 8 + 0x10))) >> (2));
    if ((((uint8_t)(result)) & (1)) != 0) goto loc_00244E23;
    result = (uint8_t)(((uint8_t)(*(uint64_t *)(result + *(uint64_t *)(Arg4) * 8 + 0x10))) >> (1));
    if ((((uint8_t)(result)) & (1)) != 0) goto loc_00244E2F;
    *(uint64_t *)(arg8) = local_rdi;
    goto loc_00244E3F;
loc_0024503D:
    if ((uint8_t)(Arg8) != 0) goto loc_00245881;
    if (Arg4 != 0) goto loc_00245053;
    if ((((uint8_t)(*(uint64_t *)(result + *(uint64_t *)(Arg4) * 8 + 0x10))) & (66)) != 0) goto loc_00245881;
loc_00245053:
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(result + *(uint64_t *)(Arg4) * 8 + 0x10))) >> (2));
    if ((((uint8_t)(result)) & (1)) != 0) goto loc_00245088;
    v_stack_p40 = (uint32_t)((uint32_t)(*(uint32_t *)(result + *(uint64_t *)(Arg4) * 8 + 0x20)));
    local_r11 = (uint32_t)(((uint32_t)(*(uint32_t *)(result + *(uint64_t *)(Arg4) * 8 + 0x20))) >> (16));
    if ((((uint8_t)(local_r11)) & (8)) != 0) goto loc_00245816;
loc_00245078:
    local_rbx = (uint8_t)(((uint8_t)(local_r11)) | (16));
    v_stack_p42 = (uint8_t)(local_rbx);
    *(uint32_t *)(result + *(uint64_t *)(Arg4) * 8 + 0x20) = (uint32_t)((uint32_t)(Arg8));
loc_00245088:
    result = MI_IS_RESET_PTE(*(uint64_t *)(result + *(uint64_t *)(Arg4) * 8 + 0x10), Arg8, Arg2 + 112, result);
    if ((uint32_t)(result) == 0) goto loc_00245221;
    result = MiClearResetPfn(result + *(uint64_t *)(Arg4) * 8, Arg8, Arg2 + 112, result);
loc_002450A1:
    goto loc_00244D77;
loc_002450C0:
    local_rbx = (uint32_t)((local_rbx) + 1);
    if (((*(uint32_t *)(v_rip + 0xD801E4)) & ((uint32_t)(local_rbx))) == 0) goto loc_00245487;
loc_002450CE:
loc_002450D0:
    if (!sign_flag) goto loc_00244F93;
    goto loc_002450C0;
loc_002450DF:
    goto loc_00244D77;
loc_002450EE:
    if ((*(uint64_t *)((uint32_t)(0xC0000434ULL) + 0x30)) == local_rdi) goto loc_00244F91;
    goto loc_00244D72;
loc_002450FD:
    Arg2 = (Arg8) & (-99);
    v_stack_p30 = Arg2;
    result = MiWriteValidPteNewProtection(v_stack_p18, Arg2, Arg2 + 112, result);
    local_rsi = (v_stack_p18) << (25);
    result = (result) << (25);
    local_rsi = (local_rsi) - (result);
    local_rsi = (local_rsi) >> (16);
    result = MiGetVaAge(v_stack_p18, local_rsi, Arg2 + 112, result);
    if (((uint8_t)(result)) == 1) goto loc_00245150;
    if (((uint8_t)(result)) < 7) {
        Arg1 = v_stack_p48;
        Arg4 = 1;
        Arg3 = 1;
        Arg2 = local_rsi;
        result = MiSetVaAgeList(Arg1, Arg2, Arg3, Arg4);
    }
    goto loc_00244D77;
loc_0024515A:
    local_rdi = (Arg4 == 0) ? 1 : 0;
    result = MiUpdatePfnPriority(result + *(uint64_t *)(Arg4) * 8, (uint32_t)(Arg6), (uint32_t)((uint32_t)(local_rdi)), Arg4);
    if (((uint8_t)(result)) == 255) goto loc_00245191;
    if (Arg4 == 0) {
        Arg3 = (uint8_t)(result);
        Arg2 = local_rsi;
        Arg1 = v_stack_p48;
        result = MiUpdateWsleAge(Arg1, Arg2, Arg3, Arg4);
    }
    if ((((uint32_t)(Arg2)) & (*(uint64_t *)(result + *(uint64_t *)(Arg4) * 8 + 0x28))) != 0) goto loc_00244EBB;
    if (sign_flag) goto loc_00244EBB;
    if (*(uint64_t *)(result + *(uint64_t *)(Arg4) * 8 + 0x8) == 0) goto loc_00244EBB;
    if (Arg4 != 0) goto loc_00244EBB;
    Arg3 = (*(uint64_t *)(result + *(uint64_t *)(Arg4) * 8 + 0x8)) | (*(uint64_t *)(result + *(uint64_t *)(Arg4) * 8 + 0x8));
    result = MiDemoteCombinedPte(v_stack_p48, local_rsi, Arg3, Arg4);
    goto loc_00244EBB;
loc_002451E2:
    v_stack_p38 = Arg3;
    if (condition_is_below) goto loc_0024520D;
    result = (uint8_t)(((uint8_t)(Arg7)) >> (2));
    if ((((uint8_t)(result)) & (1)) != 0) goto loc_00245204;
    result = (uint8_t)(((uint8_t)(Arg7)) >> (1));
    if ((((uint8_t)(result)) & (1)) == 0) goto loc_0024520D;
loc_00245204:
    if (Arg7 != NULL) goto loc_0024569F;
loc_0024520D:
    result = MiClearPageFileReservation(v_stack_p30, Arg7, Arg3, Arg4);
    goto loc_00244E00;
loc_00245221:
    goto loc_002450A1;
loc_0024522B:
    result = MI_IS_RESET_PTE(v_stack_p30, Arg7, v_stack_p30, Arg4);
    if ((uint32_t)(result) == 0) goto loc_00244D72;
    result = MI_CLEAR_RESET_PTE(v_stack_p30, Arg7, v_stack_p30, Arg4);
    if (Arg4 != 0) { local_r15 = Arg4; }
    *(uint64_t *)(local_r15) = v_stack_p30;
    result = 0;
    goto loc_00244D77;
loc_0024525B:
    result = MiRotatedToFrameBuffer(local_rsi, Arg7, v_stack_p30, Arg4);
    if ((uint32_t)(result) == 0) goto loc_00244FB5;
    goto loc_00244D72;
loc_0024527F:
    if ((uint32_t)((uint32_t)(Arg2)) != 0) goto loc_00245543;
    if (((*(uint32_t *)(v_stack_p8 + 0x30)) & (0x200000ULL)) != 0) goto loc_00244DD9;
    if (*(uint64_t *)(v_stack_p8 + 0x48) == 0) goto loc_00244DD9;
    Arg1 = (uint16_t)((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p8 + 0x48)) + 0x3C)) & ((uint16_t)((uint32_t)(0x3FFULL))));
    goto loc_00244DD9;
loc_002452C2:
    if (Arg4 != 0) goto loc_0024568D;
loc_002452CB:
    result = MI_READ_PTE_LOCK_FREE(local_r15, Arg7, v_stack_p30, Arg4);
    if (condition_is_above_or_equal) goto loc_00245879;
    result = MiInvalidPteConforms(result, Arg7, v_stack_p30, Arg4);
    if ((uint32_t)(result) == 0) goto loc_002452CB;
    if (*(uint64_t *)(v_rip + 0xBE898C) == 0) goto loc_0024530B;
    if ((((uint8_t)(result)) & (16)) != 0) goto loc_0024553A;
    Arg1 = ~(*(uint64_t *)(v_rip + 0xBE898C));
    Arg1 = (Arg1) & (result);
loc_0024530B:
    Arg1 = (Arg1) >> (12);
    Arg1 = (Arg1) & (*(uint64_t *)(v_rip + 0xBE898C));
    Arg2 = (Arg1 + Arg1 * 2) + (Arg1 + Arg1 * 2);
    if (Arg1 > (*(uint64_t *)(v_rip + 0xBE89A9))) goto loc_002452CB;
    if (Arg1 >= (*(uint64_t *)(v_rip + 0xBE89A9))) goto loc_002452CB;
loc_00245360:
    if (Arg1 < (*(uint64_t *)(v_rip + 0xBE89A9))) goto loc_00245580;
    result = MI_READ_PTE_LOCK_FREE(v_stack_p18, Arg2, v_stack_p30, Arg4);
    if (result != result) goto loc_002456B2;
    result = (*(uint64_t *)(*(uint64_t *)(v_rip + 0xBE898C) + Arg2 * 8 + 0x28)) >> (43);
    result = (uint32_t)((result) & (0x3FFULL));
    if (sign_flag) goto loc_00245863;
loc_002453A5:
    result = (*(uint64_t *)(*(uint64_t *)(v_rip + 0xBE898C) + Arg2 * 8 + 0x8)) | (*(uint64_t *)(v_rip + 0xBEACFB));
    if (result != v_stack_p18) goto loc_00245893;
loc_002453BF:
loc_002453C9:
    if (*(uint64_t *)(v_rip + 0xBE898C) + Arg2 * 8 == 0) goto loc_00244CFE;
    if (Arg4 != 0) goto loc_0024563D;
loc_002453DB:
    if (((uint32_t)((uint32_t)(Arg5))) == 2) goto loc_00245670;
    Arg2 = (uint8_t)(((uint8_t)(*(uint8_t *)(*(uint64_t *)(v_rip + 0xBE898C) + Arg2 * 8 + 0x22))) & (7));
    if (((uint8_t)(Arg2)) != 2) goto loc_002455A1;
    if (((uint32_t)((uint32_t)(Arg5))) == 1) goto loc_00245753;
    if ((((uint8_t)(*(uint8_t *)(*(uint64_t *)(v_rip + 0xBE898C) + Arg2 * 8 + 0x22))) & (40)) != 0) goto loc_00245708;
    result = (uint8_t)(((uint8_t)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xBE898C) + Arg2 * 8 + 0x10))) >> (2));
    if ((((uint8_t)(result)) & (1)) != 0) goto loc_002456C6;
    result = (uint8_t)(((uint8_t)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xBE898C) + Arg2 * 8 + 0x10))) >> (1));
    if ((((uint8_t)(result)) & (1)) != 0) goto loc_002456D2;
    *(uint64_t *)(arg8) = (uint32_t)(0xC0000434ULL);
    goto loc_002456E2;
loc_00245438:
    if (((uint32_t)(result)) == 1) goto loc_00244D72;
    Arg3 = 0;
    result = MiCapturePageFileInfoInline(v_stack_p30, Arg3 + 1, Arg3, Arg4);
    *(uint64_t *)(arg8) = result;
    if (result == 0) goto loc_00244EBB;
    *(uint64_t *)(arg7) = *(uint64_t *)(arg7 + (uint16_t)(Arg1) * 8);
    local_r13 = Arg4;
    if (Arg4 == 0) {
        local_r13 = v_stack_p18;
    }
    *(uint64_t *)(local_r13) = v_stack_p30;
    goto loc_00244EBB;
loc_00245487:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD8162B)))) & (64)) == 0) goto loc_002450CE;
    result = KiCheckVpBackingLongSpinWaitHypercall(v_stack_p30, Arg8, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_002450CE;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(result)), Arg8, Arg3, Arg4);
    goto loc_002450D0;
loc_002454AE:
    if (local_r13 != 0) goto loc_00244D72;
    if ((uint32_t)(result) != 0) goto loc_00244D72;
    local_rbx = (v_stack_p18) << (25);
    result = (result) << (25);
    local_rbx = (local_rbx) - (result);
    local_rbx = (local_rbx) >> (16);
    result = MiCheckUserVirtualAddress(local_rbx, v_stack_p8, Arg3, v_stack_p38);
    if (result != 0) goto loc_00244D72;
    if (((uint32_t)((uint32_t)(v_stack_p38))) == 24) goto loc_00244D72;
    result = MiUpdatePageTableUseCount(local_rbx, result + 1, Arg3, v_stack_p38);
    Arg2 = ((uint32_t)((uint32_t)((uint32_t)(v_stack_p38)))) << (5);
    result = MiMakePageFilePte(local_r13 + 1, Arg2, Arg3, v_stack_p38);
    result = (result) ^ (Arg2);
    result = (result) & (-993);
    result = (result) ^ (Arg2);
    v_stack_p30 = result;
    *(uint64_t *)(v_stack_p18) = result;
    result = 0;
    goto loc_00244D77;
loc_0024553A:
    Arg1 = (local_r13 + 1) & (-17);
    goto loc_0024530B;
loc_00245543:
    Arg2 = (v_stack_p18) << (25);
    result = (0) << (25);
    Arg2 = (Arg2) - (result);
    Arg2 = (Arg2) >> (16);
    result = MiSharedVaToPartition(local_rsi + 1024, Arg2, local_r13, v_stack_p38);
    goto loc_00244DD9;
loc_00245580:
    local_r15 = (uint32_t)((v_stack_p18) + 1);
    if (((*(uint32_t *)(v_rip + 0xD7FD22)) & ((uint32_t)(local_r15))) == 0) goto loc_002458F2;
loc_00245590:
loc_00245592:
    if (!sign_flag) goto loc_00245360;
    goto loc_00245580;
loc_002455A1:
    if (((uint8_t)(Arg2)) != 3) goto loc_00245708;
    if (((uint32_t)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xBE898C) + Arg2 * 8 + 0x18))) == 1) goto loc_00245954;
    if ((((uint8_t)(local_rsi + 1024)) & (8)) != 0) goto loc_00245708;
    if ((uint32_t)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xBE898C) + Arg2 * 8 + 0x18)) != 0) goto loc_00245708;
    if ((((uint8_t)(local_rsi + 1024)) & (32)) != 0) goto loc_00245708;
    if ((uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xBE898C) + Arg2 * 8 + 0x20))) != 0) goto loc_00245989;
    Arg2 = 0;
    result = MiUnlinkPageFromListEx(*(uint64_t *)(v_rip + 0xBE898C) + Arg2 * 8, Arg2, v_stack_p30, v_stack_p38);
loc_002455E4:
    Arg2 = 0;
    result = MiSetPfnModified(*(uint64_t *)(v_rip + 0xBE898C) + Arg2 * 8, Arg2, v_stack_p30, v_stack_p38);
    result = (uint8_t)(((uint8_t)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xBE898C) + Arg2 * 8 + 0x10))) >> (2));
    if ((((uint8_t)(result)) & (1)) != 0) goto loc_002457B5;
    result = (uint8_t)(((uint8_t)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xBE898C) + Arg2 * 8 + 0x10))) >> (1));
    if ((((uint8_t)(result)) & (1)) != 0) goto loc_002457C1;
    *(uint64_t *)(arg8) = (uint32_t)(v_stack_p38);
    goto loc_002457D1;
loc_00245619:
    result = (*(uint64_t *)(*(uint64_t *)(v_rip + 0xBE898C) + Arg2 * 8 + 0x28)) >> (43);
    result = (uint32_t)((result) & (0x3FFULL));
    *(uint64_t *)(arg7) = *(uint64_t *)(*(uint64_t *)(v_rip + 0xBEAA64) + result * 8);
    goto loc_00244E3F;
loc_0024563D:
    v_stack_p30 = *(uint64_t *)(local_r13);
    if ((((uint8_t)(*(uint64_t *)(local_r13))) & (1)) == 0) goto loc_002453DB;
loc_00245653:
    v_stack_p30 = *(uint64_t *)(local_r13);
    goto loc_00244D23;
loc_00245670:
    result = MiUpdatePfnPriority(*(uint64_t *)(v_rip + 0xBE898C) + Arg2 * 8, (uint32_t)(Arg6), 1, *(uint64_t *)(local_r13));
    result = 0;
    goto loc_00244D77;
loc_0024568D:
    Arg2 = 0;
    result = MiLockLeafPage(local_r13, Arg2, 1, *(uint64_t *)(local_r13));
    goto loc_002453C9;
loc_0024569F:
    result = MiReleasePageFileInfo(*(uint64_t *)(local_r13), Arg2, 1, *(uint64_t *)(local_r13));
    goto loc_0024520D;
loc_002456B2:
    goto loc_002452CB;
loc_002456C6:
    result = (*(uint64_t *)(result + 0x10)) & (-5);
    *(uint64_t *)(result + 0x10) = result;
loc_002456D2:
    *(uint64_t *)(arg8) = *(uint64_t *)(local_r13);
    if (*(uint64_t *)(local_r13) != 0) goto loc_00245965;
loc_002456E2:
    result = MiUpdatePageFileHighInPte(*(uint64_t *)(result + 0x10), 1, 1, *(uint64_t *)(local_r13));
    v_stack_p30 = result;
    result = MiClearPageFileReservation(v_stack_p30, 1, 1, *(uint64_t *)(local_r13));
    *(uint64_t *)(result + 0x10) = v_stack_p30;
loc_00245708:
    goto loc_00244D77;
loc_00245714:
    result = MiCanPfnOriginalPteBeLost(result, 1, 1, *(uint64_t *)(local_r13));
    if ((uint32_t)(result) == 0) goto loc_00245005;
    Arg1 = (uint8_t)((*(uint8_t *)(result + 0x22)) >> (4));
    Arg1 = (uint8_t)(~(Arg1));
    result = ((((uint8_t)(*(uint64_t *)(result + 0x10))) & (4)) != 0) ? 1 : 0;
    Arg1 = (uint8_t)((Arg1) & ((uint8_t)(result)));
    if ((((uint8_t)(Arg1)) & (1)) == 0) goto loc_00245005;
    result = (*(uint64_t *)(result + 0x10)) & (-5);
    *(uint64_t *)(result + 0x10) = result;
    goto loc_00245005;
loc_00245753:
    result = MI_IS_RESET_PTE(*(uint64_t *)(result + 0x10), 1, 1, *(uint64_t *)(local_r13));
    if ((uint32_t)(result) == 0) goto loc_002458C1;
    result = MiClearResetPfn(result, 1, 1, *(uint64_t *)(local_r13));
loc_0024576C:
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(result + 0x10))) >> (2));
    if ((((uint8_t)(result)) & (1)) != 0) goto loc_00245708;
    result = MiSetPfnModified(result, 1, 1, *(uint64_t *)(local_r13));
    if ((uint16_t)((uint32_t)(*(uint32_t *)(result + 0x20))) != 0) goto loc_002458CB;
    Arg2 = 0;
    result = MiUnlinkPageFromListEx(result, Arg2, 1, *(uint64_t *)(local_r13));
    if ((((uint8_t)(result)) & (3)) != 0) goto loc_0024594D;
    result = MiInsertPageInList(result, 8, 1, *(uint64_t *)(local_r13));
    goto loc_00245708;
loc_002457B5:
    result = (*(uint64_t *)(result + 0x10)) & (-5);
    *(uint64_t *)(result + 0x10) = result;
loc_002457C1:
    *(uint64_t *)(arg8) = result;
    if (result != 0) goto loc_002459A6;
loc_002457D1:
    result = MiUpdatePageFileHighInPte(*(uint64_t *)(result + 0x10), 1, 1, *(uint64_t *)(local_r13));
    v_stack_p30 = result;
    result = MiClearPageFileReservation(v_stack_p30, 1, 1, *(uint64_t *)(local_r13));
    *(uint64_t *)(result + 0x10) = v_stack_p30;
    if ((uint16_t)((uint32_t)(*(uint32_t *)(result + 0x20))) != 0) goto loc_00245708;
    result = MiInsertPageInList(result, 4, 1, *(uint64_t *)(local_r13));
    goto loc_00245708;
loc_00245816:
    result = MiCanPfnOriginalPteBeLost(result, 4, 1, *(uint64_t *)(local_r13));
    if ((uint32_t)(result) == 0) goto loc_00245078;
    Arg1 = (uint8_t)((*(uint8_t *)(result + 0x22)) >> (4));
    Arg1 = (uint8_t)(~(Arg1));
    result = ((((uint8_t)(*(uint64_t *)(result + 0x10))) & (4)) != 0) ? 1 : 0;
    Arg1 = (uint8_t)((Arg1) & ((uint8_t)(result)));
    if ((((uint8_t)(Arg1)) & (1)) == 0) goto loc_00245078;
    result = (*(uint64_t *)(result + 0x10)) & (-5);
    *(uint64_t *)(result + 0x10) = result;
    goto loc_00245078;
loc_00245855:
loc_0024585A:
    goto loc_00245653;
loc_00245863:
    Arg2 = 0;
    result = MiLockSpecialPurposeMemoryCachedPage(result, Arg2, 1, *(uint64_t *)(local_r13));
    if (result != 0) goto loc_002453A5;
loc_00245879:
    goto loc_002453BF;
loc_00245881:
    if ((((uint8_t)(result)) & (16)) == 0) goto loc_00245053;
    goto loc_00245088;
loc_00245893:
    if (condition_is_below) goto loc_002453BF;
    v_stack_p20 = *(uint64_t *)((uint32_t)(v_stack_p38) + 0x8);
    result = KeBugCheckEx(26, (uint32_t)(0x411ULL), v_stack_p18, local_rbx);
loc_002458C1:
    goto loc_0024576C;
loc_002458CB:
    v_stack_p40 = (uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(v_stack_p38) + 0x20)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)((uint32_t)(v_stack_p38) + 0x20))) >> (16));
    result = (uint8_t)((result) & (251));
    result = (uint8_t)((result) | (3));
    v_stack_p42 = (uint8_t)(result);
    *(uint32_t *)((uint32_t)(v_stack_p38) + 0x20) = (uint32_t)((uint32_t)(Arg8));
    goto loc_00244D77;
loc_002458F2:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD811C0)))) & (64)) == 0) goto loc_00245590;
    result = KiCheckVpBackingLongSpinWaitHypercall(26, (uint32_t)(0x411ULL), v_stack_p18, local_rbx);
    if ((uint8_t)(result) == 0) goto loc_00245590;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(v_stack_p18)), (uint32_t)(0x411ULL), v_stack_p18, local_rbx);
    goto loc_00245592;
loc_0024591A:
    if (*(uint64_t *)((uint32_t)(v_stack_p38) + 0x8) == 0) goto loc_00244F34;
    if (((uint32_t)(v_stack_p18)) == 1) goto loc_00244D72;
    if ((uint32_t)(v_stack_p18) != 0) goto loc_00244F91;
    goto loc_00244D77;
loc_00245944:
    goto loc_00244F83;
loc_0024594D:
    Arg2 = 0;
    result = MiDiscardTransitionPteEx((uint32_t)((uint32_t)(v_stack_p18)), Arg2, v_stack_p18, local_rbx);
loc_00245954:
    goto loc_00244D77;
loc_00245965:
    result = (*(uint64_t *)((uint32_t)(v_stack_p38) + 0x28)) >> (43);
    result = (uint32_t)((result) & (0x3FFULL));
    *(uint64_t *)(arg7) = *(uint64_t *)(*(uint64_t *)(v_rip + 0xBEA718) + result * 8);
    goto loc_002456E2;
loc_00245989:
    v_stack_p20 = (uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(v_stack_p38) + 0x20)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)((uint32_t)(v_stack_p38) + 0x20))) >> (16));
    result = (uint8_t)((result) & (250));
    result = (uint8_t)((result) | (2));
    v_stack_p22 = (uint8_t)(result);
    *(uint32_t *)((uint32_t)(v_stack_p38) + 0x20) = (uint32_t)((uint32_t)(v_stack_p20));
    goto loc_002455E4;
loc_002459A6:
    result = (*(uint64_t *)((uint32_t)(v_stack_p38) + 0x28)) >> (43);
    result = (uint32_t)((result) & (0x3FFULL));
    *(uint64_t *)(arg7) = *(uint64_t *)(*(uint64_t *)(v_rip + 0xBEA6D7) + result * 8);
    goto loc_002457D1;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg7` | `+ 0x0` | `64` | `W` |
| `Arg8` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00244C90&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
