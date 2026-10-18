# KiRetireDpcList

- RVA: `0x0021A0B0`–`0x0021B0FD` (길이 `4,173` bytes)
- VA: `0x000000014021A0B0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005EC8C`
- 디코드: `973`개 명령, `4,173/4,173` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **29**; 고유 호출 대상: **22**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **18**

### Outgoing calls
- `0x0021A0FB` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0021A15A` → [KeQueryPerformanceCounter](../37/KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)
- `0x0021A47E` → [KiUpdateThreadHgsFeedback](../37/KiUpdateThreadHgsFeedback_function_0037D790.md) (function, `0x0037D790`)
- `0x0021A4AE` → [KiRcuCheckQuiescent](KiRcuCheckQuiescent_function_0021B110.md) (function, `0x0021B110`)
- `0x0021A4F2` → [KiNormalPriorityReadyScan](KiNormalPriorityReadyScan_function_0021B400.md) (function, `0x0021B400`)
- `0x0021A505` → [KiExecuteAllDpcs](../25/KiExecuteAllDpcs_function_0025B740.md) (function, `0x0025B740`)
- `0x0021A5CC` → [KiTryUnwaitThread](../35/KiTryUnwaitThread_function_003506D0.md) (function, `0x003506D0`)
- `0x0021A5FE` → [KiExitDispatcher](../25/KiExitDispatcher_function_00251CF0.md) (function, `0x00251CF0`)
- `0x0021A622` → [KeQueryPerformanceCounter](../37/KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)
- `0x0021A808` → [RtlBackoff](../20/RtlBackoff_function_00208620.md) (function, `0x00208620`)
- `0x0021A845` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x0021A8B8` → [KiEndCounterAccumulation](../37/KiEndCounterAccumulation_function_0037EEAC.md) (function, `0x0037EEAC`)
- `0x0021A99D` → [KeQueryPerformanceCounter](../37/KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)
- `0x0021AA1A` → [PoGetFrequencyBucket](PoGetFrequencyBucket_function_0021B780.md) (function, `0x0021B780`)
- `0x0021ABAE` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x0021ABCC` → [KiInsertQueueInternal](KiInsertQueueInternal_function_00219B30.md) (function, `0x00219B30`)
- `0x0021AC3E` → [KiQueryEffectivePriorityThread](../25/KiQueryEffectivePriorityThread_function_00257BA0.md) (function, `0x00257BA0`)
- `0x0021AC87` → [KiSelectActiveTimerTable](../44/KiSelectActiveTimerTable_function_00446680.md) (function, `0x00446680`)
- `0x0021AD54` → [KiTimerExpiration](../23/KiTimerExpiration_function_00234840.md) (function, `0x00234840`)
- `0x0021AD76` → [KiTimer2Expiration](../3A/KiTimer2Expiration_function_003A1880.md) (function, `0x003A1880`)
- `0x0021ADD5` → [KiRemoveSystemWorkPriorityKick](../26/KiRemoveSystemWorkPriorityKick_function_002631D0.md) (function, `0x002631D0`)
- `0x0021AE10` → [KiRemoveSystemWorkPriorityKick](../26/KiRemoveSystemWorkPriorityKick_function_002631D0.md) (function, `0x002631D0`)
- `0x0021AEEB` → [KiRemoveSystemWorkPriorityKick](../26/KiRemoveSystemWorkPriorityKick_function_002631D0.md) (function, `0x002631D0`)
- `0x0021AF34` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0021AF44` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0021AF70` → [KiTryUnwaitThread](../35/KiTryUnwaitThread_function_003506D0.md) (function, `0x003506D0`)
- `0x0021AFAE` → [KiRemoveSystemWorkPriorityKick](../26/KiRemoveSystemWorkPriorityKick_function_002631D0.md) (function, `0x002631D0`)
- `0x0021AFE7` → [KiRemoveSystemWorkPriorityKick](../26/KiRemoveSystemWorkPriorityKick_function_002631D0.md) (function, `0x002631D0`)
- `0x0021B00E` → [KeInsertQueueDpc](../20/KeInsertQueueDpc_function_00207C50.md) (function, `0x00207C50`)

### Direct callers
- [KiExecuteSmtIsolationThread](../5C/KiExecuteSmtIsolationThread_function_005C4070.md) at `0x005C40B4`
- [KiExecuteDpcDelegate](../5C/KiExecuteDpcDelegate_function_005C8620.md) at `0x005C8659`
- [KiIdleLoop](../6B/KiIdleLoop_function_006B2910.md) at `0x006B29A9`
- [KxSwapStacksAndRetireDpcList](../6B/KxSwapStacksAndRetireDpcList_function_006B9720.md) at `0x006B9720`

### Static image references
- `0x0021A0D7` → RVA `0x00E0A740` (`.data`; read)
- `0x0021A199` → RVA `0x00FC6A95` (`ALMOSTRO`; read)
- `0x0021A1FF` → RVA `0x00FC6BC6` (`ALMOSTRO`; read)
- `0x0021A214` → RVA `0x00FC7318` (`ALMOSTRO`; read)
- `0x0021A3B5` → RVA `0x00F10A44` (`.data`; read)
- `0x0021A3DD` → RVA `0x00FC6D60` (`ALMOSTRO`; read)
- `0x0021A469` → RVA `0x00FC6ADE` (`ALMOSTRO`; read)
- `0x0021A48D` → RVA `0x00FCFF00` (`CACHEALI`; read)
- `0x0021A54A` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x0021A75A` → RVA `0x00E66908` (`.data`; read)
- `0x0021A767` → RVA `0x00F10E80` (`.data`; read)
- `0x0021ACAC` → RVA `0x00E668B0` (`.data`; read)
- `0x0021ACB3` → RVA `0x00E668A8` (`.data`; read)
- `0x0021ACD5` → RVA `0x00FC6C48` (`ALMOSTRO`; read)
- `0x0021AD93` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x0021AF26` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)
- `0x0021B04C` → RVA `0x00FC537C` (`ALMOSTRO`; read)
- `0x0021B059` → RVA `0x00FC53E0` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0021A0B0  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
0021A0B5  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
0021A0BA  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
0021A0BF  55                              push rbp
0021A0C0  41 54                           push r12
0021A0C2  41 55                           push r13
0021A0C4  41 56                           push r14
0021A0C6  41 57                           push r15
0021A0C8  48 8D AC 24 A0 FE FF FF         lea rbp, [rsp - 0x160]
0021A0D0  48 81 EC 60 02 00 00            sub rsp, 0x260
0021A0D7  48 8B 05 62 06 BF 00            mov rax, qword ptr [rip + 0xbf0662]
0021A0DE  48 33 C4                        xor rax, rsp
0021A0E1  48 89 85 50 01 00 00            mov qword ptr [rbp + 0x150], rax
0021A0E8  48 8B D9                        mov rbx, rcx
0021A0EB  48 89 4D B0                     mov qword ptr [rbp - 0x50], rcx
0021A0EF  48 8D 4D C4                     lea rcx, [rbp - 0x3c]
0021A0F3  33 D2                           xor edx, edx
0021A0F5  41 B8 8C 01 00 00               mov r8d, 0x18c
0021A0FB  E8 40 CB 4A 00                  call 0x1406c6c40
0021A100  48 8B 73 08                     mov rsi, qword ptr [rbx + 8]
0021A104  48 8D 83 F8 86 00 00            lea rax, [rbx + 0x86f8]
0021A10B  45 33 E4                        xor r12d, r12d
0021A10E  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0021A113  48 8D BB 80 86 00 00            lea rdi, [rbx + 0x8680]
0021A11A  44 89 65 C0                     mov dword ptr [rbp - 0x40], r12d
0021A11E  4C 8B F8                        mov r15, rax
0021A121  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
0021A126  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
0021A12B  45 8D 6C 24 01                  lea r13d, [r12 + 1]
0021A130  48 89 7C 24 50                  mov qword ptr [rsp + 0x50], rdi
0021A135  C6 43 20 01                     mov byte ptr [rbx + 0x20], 1
0021A139  41 BB 48 00 00 00               mov r11d, 0x48
0021A13F  90                              nop
0021A140  BA FF FF FF FF                  mov edx, 0xffffffff
0021A145  80 BB DC 86 00 00 00            cmp byte ptr [rbx + 0x86dc], 0
0021A14C  49 8B FC                        mov rdi, r12
0021A14F  4D 8B F4                        mov r14, r12
0021A152  0F 84 8C 09 00 00               je 0x14021aae4
0021A158  33 C9                           xor ecx, ecx
0021A15A  E8 81 46 16 00                  call 0x14037e7e0
0021A15F  0F B6 8B AC 00 00 00            movzx ecx, byte ptr [rbx + 0xac]
0021A166  45 33 D2                        xor r10d, r10d
0021A169  4C 89 55 98                     mov qword ptr [rbp - 0x68], r10
0021A16D  48 8B F8                        mov rdi, rax
0021A170  48 8B 83 B0 00 00 00            mov rax, qword ptr [rbx + 0xb0]
0021A177  48 8B D7                        mov rdx, rdi
0021A17A  84 C9                           test cl, cl
0021A17C  74 03                           je 0x14021a181
0021A17E  48 D3 E2                        shl rdx, cl
0021A181  4C 8B 5C 24 50                  mov r11, qword ptr [rsp + 0x50]
0021A186  48 F7 E2                        mul rdx
0021A189  49 8B C3                        mov rax, r11
0021A18C  4C 8B E2                        mov r12, rdx
0021A18F  48 89 55 98                     mov qword ptr [rbp - 0x68], rdx
0021A193  4D 2B 23                        sub r12, qword ptr [r11]
0021A196  4C 8B F2                        mov r14, rdx
0021A199  44 38 15 F5 C8 DA 00            cmp byte ptr [rip + 0xdac8f5], r10b
0021A1A0  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0021A1A5  0F 84 A3 0D 00 00               je 0x14021af4e
0021A1AB  49 8B 17                        mov rdx, qword ptr [r15]
0021A1AE  48 B8 00 03 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000300
0021A1B8  4C 39 10                        cmp qword ptr [rax], r10
0021A1BB  0F 84 EB 0E 00 00               je 0x14021b0ac
0021A1C1  48 B8 60 03 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000360
0021A1CB  4C 89 54 24 68                  mov qword ptr [rsp + 0x68], r10
0021A1D0  48 C7 44 24 70 00 00 00 00      mov qword ptr [rsp + 0x70], 0
0021A1D9  4C 8B C7                        mov r8, rdi
0021A1DC  4C 8B 08                        mov r9, qword ptr [rax]
0021A1DF  A0 69 03 00 00 80 F7 FF FF      movabs al, byte ptr [0xfffff78000000369]
0021A1E8  0F B6 C8                        movzx ecx, al
0021A1EB  84 C0                           test al, al
0021A1ED  49 8B C1                        mov rax, r9
0021A1F0  0F 84 C2 0D 00 00               je 0x14021afb8
0021A1F6  48 D3 E2                        shl rdx, cl
0021A1F9  48 F7 E2                        mul rdx
0021A1FC  49 D3 E0                        shl r8, cl
0021A1FF  0F BE 0D C0 C9 DA 00            movsx ecx, byte ptr [rip + 0xdac9c0]
0021A206  4C 8B D2                        mov r10, rdx
0021A209  48 89 54 24 68                  mov qword ptr [rsp + 0x68], rdx
0021A20E  49 8B C1                        mov rax, r9
0021A211  49 F7 E0                        mul r8
0021A214  48 8B 05 FD D0 DA 00            mov rax, qword ptr [rip + 0xdad0fd]
0021A21B  4C 8B 44 24 48                  mov r8, qword ptr [rsp + 0x48]
0021A220  4C 8B CA                        mov r9, rdx
0021A223  48 89 54 24 70                  mov qword ptr [rsp + 0x70], rdx
0021A228  49 F7 E2                        mul r10
0021A22B  48 8B 05 E6 D0 DA 00            mov rax, qword ptr [rip + 0xdad0e6]
0021A232  4C 8B D2                        mov r10, rdx
0021A235  49 F7 E1                        mul r9
0021A238  49 D3 EA                        shr r10, cl
0021A23B  49 8B C3                        mov rax, r11
0021A23E  4C 8B FA                        mov r15, rdx
0021A241  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0021A246  49 D3 EF                        shr r15, cl
0021A249  49 8B C8                        mov rcx, r8
0021A24C  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
0021A251  45 2B FA                        sub r15d, r10d
0021A254  0F 85 89 09 00 00               jne 0x14021abe3
0021A25A  45 33 D2                        xor r10d, r10d
0021A25D  41 BB 48 00 00 00               mov r11d, 0x48
0021A263  BA FF FF FF FF                  mov edx, 0xffffffff
0021A268  48 89 39                        mov qword ptr [rcx], rdi
0021A26B  4C 89 30                        mov qword ptr [rax], r14
0021A26E  48 8B 4E 48                     mov rcx, qword ptr [rsi + 0x48]
0021A272  49 03 CC                        add rcx, r12
0021A275  48 89 4E 48                     mov qword ptr [rsi + 0x48], rcx
0021A279  48 3B 73 18                     cmp rsi, qword ptr [rbx + 0x18]
0021A27D  74 1E                           je 0x14021a29d
0021A27F  8B 83 B8 86 00 00               mov eax, dword ptr [rbx + 0x86b8]
0021A285  8B 4E 50                        mov ecx, dword ptr [rsi + 0x50]
0021A288  49 0F AF C4                     imul rax, r12
0021A28C  48 C1 E8 10                     shr rax, 0x10
0021A290  48 03 C8                        add rcx, rax
0021A293  48 3B CA                        cmp rcx, rdx
0021A296  48 0F 47 CA                     cmova rcx, rdx
0021A29A  89 4E 50                        mov dword ptr [rsi + 0x50], ecx
0021A29D  0F B6 7E 02                     movzx edi, byte ptr [rsi + 2]
0021A2A1  40 F6 C7 BE                     test dil, 0xbe
0021A2A5  0F 84 00 02 00 00               je 0x14021a4ab
0021A2AB  40 84 FF                        test dil, dil
0021A2AE  79 54                           jns 0x14021a304
0021A2B0  48 8B 86 20 02 00 00            mov rax, qword ptr [rsi + 0x220]
0021A2B7  41 8B D5                        mov edx, r13d
0021A2BA  4C 8B 83 B0 8B 00 00            mov r8, qword ptr [rbx + 0x8bb0]
0021A2C1  44 8B 88 90 01 00 00            mov r9d, dword ptr [rax + 0x190]
0021A2C8  41 8B C1                        mov eax, r9d
0021A2CB  C1 E8 0D                        shr eax, 0xd
0021A2CE  25 FF FF 03 00                  and eax, 0x3ffff
0021A2D3  49 C1 E9 04                     shr r9, 4
0021A2D7  0F BD C8                        bsr ecx, eax
0021A2DA  41 81 E1 FF 01 00 00            and r9d, 0x1ff
0021A2E1  D3 E2                           shl edx, cl
0021A2E3  83 C1 FE                        add ecx, -2
0021A2E6  33 D0                           xor edx, eax
0021A2E8  89 4C 24 60                     mov dword ptr [rsp + 0x60], ecx
0021A2EC  49 8B 0C C8                     mov rcx, qword ptr [r8 + rcx*8]
0021A2F0  48 8B 54 D1 08                  mov rdx, qword ptr [rcx + rdx*8 + 8]
0021A2F5  4A 8B 04 CA                     mov rax, qword ptr [rdx + r9*8]
0021A2F9  49 03 C4                        add rax, r12
0021A2FC  4A 89 04 CA                     mov qword ptr [rdx + r9*8], rax
0021A300  40 80 E7 7F                     and dil, 0x7f
0021A304  40 F6 C7 10                     test dil, 0x10
0021A308  0F 85 B6 07 00 00               jne 0x14021aac4
0021A30E  40 F6 C7 20                     test dil, 0x20
0021A312  0F 84 47 01 00 00               je 0x14021a45f
0021A318  4C 8B 8E 88 06 00 00            mov r9, qword ptr [rsi + 0x688]
0021A31F  4D 85 C9                        test r9, r9
0021A322  0F 84 33 01 00 00               je 0x14021a45b
0021A328  48 8B 83 B0 89 00 00            mov rax, qword ptr [rbx + 0x89b0]
0021A32F  48 8B 93 B8 89 00 00            mov rdx, qword ptr [rbx + 0x89b8]
0021A336  48 85 C0                        test rax, rax
0021A339  0F 84 82 0D 00 00               je 0x14021b0c1
0021A33F  48 85 D2                        test rdx, rdx
0021A342  0F 84 79 0D 00 00               je 0x14021b0c1
0021A348  80 7A 70 00                     cmp byte ptr [rdx + 0x70], 0
0021A34C  75 11                           jne 0x14021a35f
0021A34E  8B 52 50                        mov edx, dword ptr [rdx + 0x50]
0021A351  8B 88 10 02 00 00               mov ecx, dword ptr [rax + 0x210]
0021A357  3B D1                           cmp edx, ecx
0021A359  72 0A                           jb 0x14021a365
0021A35B  8B D1                           mov edx, ecx
0021A35D  EB 06                           jmp 0x14021a365
0021A35F  8B 92 84 00 00 00               mov edx, dword ptr [rdx + 0x84]
0021A365  45 8B C2                        mov r8d, r10d
0021A368  48 8D 8B 6A 8A 00 00            lea rcx, [rbx + 0x8a6a]
0021A36F  0F B7 01                        movzx eax, word ptr [rcx]
0021A372  3B D0                           cmp edx, eax
0021A374  76 0D                           jbe 0x14021a383
0021A376  41 FF C0                        inc r8d
0021A379  48 83 C1 02                     add rcx, 2
0021A37D  41 83 F8 03                     cmp r8d, 3
0021A381  72 EC                           jb 0x14021a36f
0021A383  44 0F B6 93 08 8A 00 00         movzx r10d, byte ptr [rbx + 0x8a08]
0021A38B  41 0F B6 C2                     movzx eax, r10b
0021A38F  41 8B D0                        mov edx, r8d
0021A392  F6 D8                           neg al
0021A394  48 C7 44 24 58 00 00 00 00      mov qword ptr [rsp + 0x58], 0
0021A39D  48 1B C9                        sbb rcx, rcx
0021A3A0  48 03 D2                        add rdx, rdx
0021A3A3  83 E1 08                        and ecx, 8
0021A3A6  49 8D 04 09                     lea rax, [r9 + rcx]
0021A3AA  48 8B 0C D0                     mov rcx, qword ptr [rax + rdx*8]
0021A3AE  49 03 CC                        add rcx, r12
0021A3B1  48 89 0C D0                     mov qword ptr [rax + rdx*8], rcx
0021A3B5  8B 05 89 66 CF 00               mov eax, dword ptr [rip + 0xcf6689]
0021A3BB  41 8B 89 C0 00 00 00            mov ecx, dword ptr [r9 + 0xc0]
0021A3C2  3B C1                           cmp eax, ecx
0021A3C4  0F 87 96 0A 00 00               ja 0x14021ae60
0021A3CA  2B C8                           sub ecx, eax
0021A3CC  83 F9 20                        cmp ecx, 0x20
0021A3CF  73 0C                           jae 0x14021a3dd
0021A3D1  41 8B C5                        mov eax, r13d
0021A3D4  D3 E0                           shl eax, cl
0021A3D6  41 09 81 C4 00 00 00            or dword ptr [r9 + 0xc4], eax
0021A3DD  83 3D 7C C9 DA 00 00            cmp dword ptr [rip + 0xdac97c], 0
0021A3E4  75 1E                           jne 0x14021a404
0021A3E6  0F B6 8E 04 02 00 00            movzx ecx, byte ptr [rsi + 0x204]
0021A3ED  8D 41 FE                        lea eax, [rcx - 2]
0021A3F0  A9 FB FF FF FF                  test eax, 0xfffffffb
0021A3F5  0F 84 70 05 00 00               je 0x14021a96b
0021A3FB  80 F9 05                        cmp cl, 5
0021A3FE  0F 84 67 05 00 00               je 0x14021a96b
0021A404  48 83 BE 50 06 00 00 00         cmp qword ptr [rsi + 0x650], 0
0021A40C  74 4D                           je 0x14021a45b
0021A40E  41 0F B6 C2                     movzx eax, r10b
0021A412  41 8B C8                        mov ecx, r8d
0021A415  48 83 C1 08                     add rcx, 8
0021A419  48 03 C9                        add rcx, rcx
0021A41C  F6 D8                           neg al
0021A41E  48 1B D2                        sbb rdx, rdx
0021A421  83 E2 08                        and edx, 8
0021A424  49 8D 04 C9                     lea rax, [r9 + rcx*8]
0021A428  48 8B 0C 02                     mov rcx, qword ptr [rdx + rax]
0021A42C  49 03 CC                        add rcx, r12
0021A42F  48 89 0C 02                     mov qword ptr [rdx + rax], rcx
0021A433  45 84 D2                        test r10b, r10b
0021A436  48 8B 86 50 06 00 00            mov rax, qword ptr [rsi + 0x650]
0021A43D  41 8B D0                        mov edx, r8d
0021A440  48 8B 88 88 06 00 00            mov rcx, qword ptr [rax + 0x688]
0021A447  B8 40 00 00 00                  mov eax, 0x40
0021A44C  49 0F 45 C3                     cmovne rax, r11
0021A450  48 03 D2                        add rdx, rdx
0021A453  48 03 C1                        add rax, rcx
0021A456  F0 4C 01 24 D0                  lock add qword ptr [rax + rdx*8], r12
0021A45B  40 80 E7 DF                     and dil, 0xdf
0021A45F  40 F6 C7 40                     test dil, 0x40
0021A463  0F 85 8D 06 00 00               jne 0x14021aaf6
0021A469  80 3D 6E C6 DA 00 00            cmp byte ptr [rip + 0xdac66e], 0
0021A470  74 11                           je 0x14021a483
0021A472  45 33 C9                        xor r9d, r9d
0021A475  4D 8B C4                        mov r8, r12
0021A478  48 8B D6                        mov rdx, rsi
0021A47B  48 8B CB                        mov rcx, rbx
0021A47E  E8 0D 33 16 00                  call 0x14037d790
0021A483  48 83 BB B0 86 00 00 00         cmp qword ptr [rbx + 0x86b0], 0
0021A48B  74 14                           je 0x14021a4a1
0021A48D  48 8D 05 6C 5A DB 00            lea rax, [rip + 0xdb5a6c]
0021A494  48 39 86 20 02 00 00            cmp qword ptr [rsi + 0x220], rax
0021A49B  0F 85 84 0B 00 00               jne 0x14021b025
0021A4A1  40 F6 C7 BE                     test dil, 0xbe
0021A4A5  0F 85 C1 03 00 00               jne 0x14021a86c
0021A4AB  48 8B CB                        mov rcx, rbx
0021A4AE  E8 5D 0C 00 00                  call 0x14021b110
0021A4B3  41 8B FD                        mov edi, r13d
0021A4B6  66 87 BB BC 38 00 00            xchg word ptr [rbx + 0x38bc], di
0021A4BD  40 F6 C7 08                     test dil, 8
0021A4C1  0F 85 B3 07 00 00               jne 0x14021ac7a
0021A4C7  40 F6 C7 40                     test dil, 0x40
0021A4CB  74 2B                           je 0x14021a4f8
0021A4CD  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
0021A4D6  B8 BF FF 00 00                  mov eax, 0xffbf
0021A4DB  66 23 F8                        and di, ax
0021A4DE  4C 8B 81 B8 8E 00 00            mov r8, qword ptr [rcx + 0x8eb8]
0021A4E5  4D 85 C0                        test r8, r8
0021A4E8  0F 85 C9 08 00 00               jne 0x14021adb7
0021A4EE  FB                              sti
0021A4EF  48 8B CB                        mov rcx, rbx
0021A4F2  E8 09 0F 00 00                  call 0x14021b400
0021A4F7  FA                              cli
0021A4F8  45 33 C9                        xor r9d, r9d
0021A4FB  4C 8D 45 C0                     lea r8, [rbp - 0x40]
0021A4FF  48 8B D6                        mov rdx, rsi
0021A502  48 8B CB                        mov rcx, rbx
0021A505  E8 36 12 04 00                  call 0x14025b740
0021A50A  84 C0                           test al, al
0021A50C  0F 84 71 04 00 00               je 0x14021a983
0021A512  40 F6 C7 04                     test dil, 4
0021A516  0F 84 E8 00 00 00               je 0x14021a604
0021A51C  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
0021A525  4C 8B 81 B8 8E 00 00            mov r8, qword ptr [rcx + 0x8eb8]
0021A52C  4D 85 C0                        test r8, r8
0021A52F  0F 85 BD 08 00 00               jne 0x14021adf2
0021A535  FB                              sti
0021A536  48 8D BB 40 83 00 00            lea rdi, [rbx + 0x8340]
0021A53D  45 0F 20 C5                     mov r13, cr8
0021A541  B8 02 00 00 00                  mov eax, 2
0021A546  44 0F 22 C0                     mov cr8, rax
0021A54A  83 3D CF C7 DA 00 00            cmp dword ptr [rip + 0xdac7cf], 0
0021A551  0F 85 50 06 00 00               jne 0x14021aba7
0021A557  65 4C 8B 24 25 20 00 00 00      mov r12, qword ptr gs:[0x20]
0021A560  45 33 C0                        xor r8d, r8d
0021A563  F0 0F BA 2F 07                  lock bts dword ptr [rdi], 7
0021A568  45 8B F0                        mov r14d, r8d
0021A56B  0F 82 1F 08 00 00               jb 0x14021ad90
0021A571  83 7F 04 00                     cmp dword ptr [rdi + 4], 0
0021A575  75 6A                           jne 0x14021a5e1
0021A577  4C 8B 77 08                     mov r14, qword ptr [rdi + 8]
0021A57B  4C 8D 7F 08                     lea r15, [rdi + 8]
0021A57F  C7 47 04 01 00 00 00            mov dword ptr [rdi + 4], 1
0021A586  4D 3B F7                        cmp r14, r15
0021A589  74 56                           je 0x14021a5e1
0021A58B  49 8B 0E                        mov rcx, qword ptr [r14]
0021A58E  49 8B C6                        mov rax, r14
0021A591  4C 8B F1                        mov r14, rcx
0021A594  48 8B 50 08                     mov rdx, qword ptr [rax + 8]
0021A598  48 39 41 08                     cmp qword ptr [rcx + 8], rax
0021A59C  75 05                           jne 0x14021a5a3
0021A59E  48 39 02                        cmp qword ptr [rdx], rax
0021A5A1  74 07                           je 0x14021a5aa
0021A5A3  B9 03 00 00 00                  mov ecx, 3
0021A5A8  CD 29                           int 0x29
0021A5AA  48 89 0A                        mov qword ptr [rdx], rcx
0021A5AD  48 89 51 08                     mov qword ptr [rcx + 8], rdx
0021A5B1  0F B6 48 10                     movzx ecx, byte ptr [rax + 0x10]
0021A5B5  80 F9 01                        cmp cl, 1
0021A5B8  0F 85 FA 05 00 00               jne 0x14021abb8
0021A5BE  44 0F B7 40 12                  movzx r8d, word ptr [rax + 0x12]
0021A5C3  45 33 C9                        xor r9d, r9d
0021A5C6  48 8B D0                        mov rdx, rax
0021A5C9  49 8B CC                        mov rcx, r12
0021A5CC  E8 FF 60 13 00                  call 0x1403506d0
0021A5D1  41 B8 00 00 00 00               mov r8d, 0
0021A5D7  84 C0                           test al, al
0021A5D9  74 AB                           je 0x14021a586
0021A5DB  83 6F 04 01                     sub dword ptr [rdi + 4], 1
0021A5DF  75 A5                           jne 0x14021a586
0021A5E1  F0 81 27 7F FF FF FF            lock and dword ptr [rdi], 0xffffff7f
0021A5E8  44 88 6C 24 20                  mov byte ptr [rsp + 0x20], r13b
0021A5ED  45 33 C9                        xor r9d, r9d
0021A5F0  41 BD 01 00 00 00               mov r13d, 1
0021A5F6  33 D2                           xor edx, edx
0021A5F8  45 8B C5                        mov r8d, r13d
0021A5FB  49 8B CC                        mov rcx, r12
0021A5FE  E8 ED 76 03 00                  call 0x140251cf0
0021A603  FA                              cli
0021A604  45 33 E4                        xor r12d, r12d
0021A607  41 8B FC                        mov edi, r12d
0021A60A  45 8B FC                        mov r15d, r12d
0021A60D  45 8B DC                        mov r11d, r12d
0021A610  45 8B D4                        mov r10d, r12d
0021A613  44 38 A3 DC 86 00 00            cmp byte ptr [rbx + 0x86dc], r12b
0021A61A  0F 84 FA 07 00 00               je 0x14021ae1a
0021A620  33 C9                           xor ecx, ecx
0021A622  E8 B9 41 16 00                  call 0x14037e7e0
0021A627  0F B6 8B AC 00 00 00            movzx ecx, byte ptr [rbx + 0xac]
0021A62E  48 8B F8                        mov rdi, rax
0021A631  48 8B 83 B0 00 00 00            mov rax, qword ptr [rbx + 0xb0]
0021A638  48 8B D7                        mov rdx, rdi
0021A63B  4C 89 65 A0                     mov qword ptr [rbp - 0x60], r12
0021A63F  84 C9                           test cl, cl
0021A641  74 03                           je 0x14021a646
0021A643  48 D3 E2                        shl rdx, cl
0021A646  4C 8B 74 24 38                  mov r14, qword ptr [rsp + 0x38]
0021A64B  4C 8B DF                        mov r11, rdi
0021A64E  4C 8B 4C 24 30                  mov r9, qword ptr [rsp + 0x30]
0021A653  48 F7 E2                        mul rdx
0021A656  4D 8B 06                        mov r8, qword ptr [r14]
0021A659  4C 8B D2                        mov r10, rdx
0021A65C  48 89 55 A0                     mov qword ptr [rbp - 0x60], rdx
0021A660  4D 2B 11                        sub r10, qword ptr [r9]
0021A663  4D 2B D8                        sub r11, r8
0021A666  44 38 25 28 C4 DA 00            cmp byte ptr [rip + 0xdac428], r12b
0021A66D  4C 8B FA                        mov r15, rdx
0021A670  0F 85 4C 02 00 00               jne 0x14021a8c2
0021A676  48 8B 8B 00 87 00 00            mov rcx, qword ptr [rbx + 0x8700]
0021A67D  49 03 CB                        add rcx, r11
0021A680  48 89 8B 00 87 00 00            mov qword ptr [rbx + 0x8700], rcx
0021A687  48 8B 8B 78 87 00 00            mov rcx, qword ptr [rbx + 0x8778]
0021A68E  49 03 CA                        add rcx, r10
0021A691  48 89 8B 78 87 00 00            mov qword ptr [rbx + 0x8778], rcx
0021A698  F6 46 02 20                     test byte ptr [rsi + 2], 0x20
0021A69C  0F 84 86 00 00 00               je 0x14021a728
0021A6A2  48 8B 83 B0 89 00 00            mov rax, qword ptr [rbx + 0x89b0]
0021A6A9  4C 8B 83 B8 89 00 00            mov r8, qword ptr [rbx + 0x89b8]
0021A6B0  48 85 C0                        test rax, rax
0021A6B3  0F 84 12 0A 00 00               je 0x14021b0cb
0021A6B9  4D 85 C0                        test r8, r8
0021A6BC  0F 84 09 0A 00 00               je 0x14021b0cb
0021A6C2  45 38 60 70                     cmp byte ptr [r8 + 0x70], r12b
0021A6C6  75 14                           jne 0x14021a6dc
0021A6C8  45 8B 40 50                     mov r8d, dword ptr [r8 + 0x50]
0021A6CC  8B 88 10 02 00 00               mov ecx, dword ptr [rax + 0x210]
0021A6D2  44 3B C1                        cmp r8d, ecx
0021A6D5  72 0C                           jb 0x14021a6e3
0021A6D7  44 8B C1                        mov r8d, ecx
0021A6DA  EB 07                           jmp 0x14021a6e3
0021A6DC  45 8B 80 84 00 00 00            mov r8d, dword ptr [r8 + 0x84]
0021A6E3  41 8B D4                        mov edx, r12d
0021A6E6  48 8D 8B 6A 8A 00 00            lea rcx, [rbx + 0x8a6a]
0021A6ED  0F B7 01                        movzx eax, word ptr [rcx]
0021A6F0  44 3B C0                        cmp r8d, eax
0021A6F3  76 0B                           jbe 0x14021a700
0021A6F5  FF C2                           inc edx
0021A6F7  48 83 C1 02                     add rcx, 2
0021A6FB  83 FA 03                        cmp edx, 3
0021A6FE  72 ED                           jb 0x14021a6ed
0021A700  44 38 A3 08 8A 00 00            cmp byte ptr [rbx + 0x8a08], r12b
0021A707  49 8B C4                        mov rax, r12
0021A70A  8B CA                           mov ecx, edx
0021A70C  0F 95 C0                        setne al
0021A70F  48 8D 04 48                     lea rax, [rax + rcx*2]
0021A713  48 8D 80 F0 10 00 00            lea rax, [rax + 0x10f0]
0021A71A  48 8B 0C C3                     mov rcx, qword ptr [rbx + rax*8]
0021A71E  48 8D 14 C3                     lea rdx, [rbx + rax*8]
0021A722  49 03 CA                        add rcx, r10
0021A725  48 89 0A                        mov qword ptr [rdx], rcx
0021A728  F6 46 02 40                     test byte ptr [rsi + 2], 0x40
0021A72C  74 10                           je 0x14021a73e
0021A72E  48 8B 86 C8 03 00 00            mov rax, qword ptr [rsi + 0x3c8]
0021A735  48 85 C0                        test rax, rax
0021A738  74 04                           je 0x14021a73e
0021A73A  C6 40 40 01                     mov byte ptr [rax + 0x40], 1
0021A73E  49 89 3E                        mov qword ptr [r14], rdi
0021A741  4D 89 39                        mov qword ptr [r9], r15
0021A744  F6 46 02 02                     test byte ptr [rsi + 2], 2
0021A748  74 44                           je 0x14021a78e
0021A74A  48 8B 8E 68 01 00 00            mov rcx, qword ptr [rsi + 0x168]
0021A751  4C 8B 49 20                     mov r9, qword ptr [rcx + 0x20]
0021A755  4D 85 C9                        test r9, r9
0021A758  74 34                           je 0x14021a78e
0021A75A  8B 05 A8 C1 C4 00               mov eax, dword ptr [rip + 0xc4c1a8]
0021A760  4D 8B C5                        mov r8, r13
0021A763  85 C0                           test eax, eax
0021A765  74 27                           je 0x14021a78e
0021A767  4C 8D 15 12 67 CF 00            lea r10, [rip + 0xcf6712]
0021A76E  8B F8                           mov edi, eax
0021A770  4C 8D 59 30                     lea r11, [rcx + 0x30]
0021A774  4D 85 C8                        test r8, r9
0021A777  0F 85 59 09 00 00               jne 0x14021b0d6
0021A77D  4D 03 C0                        add r8, r8
0021A780  49 83 C3 18                     add r11, 0x18
0021A784  49 83 C2 04                     add r10, 4
0021A788  48 83 EF 01                     sub rdi, 1
0021A78C  75 E6                           jne 0x14021a774
0021A78E  90                              nop
0021A78F  44 88 63 20                     mov byte ptr [rbx + 0x20], r12b
0021A793  44 38 63 06                     cmp byte ptr [rbx + 6], r12b
0021A797  0F 85 EA 07 00 00               jne 0x14021af87
0021A79D  41 8B C5                        mov eax, r13d
0021A7A0  66 F0 44 0F B1 A3 BC 38 00 00   lock cmpxchg word ptr [rbx + 0x38bc], r12w
0021A7AA  66 83 F8 01                     cmp ax, 1
0021A7AE  0F 84 80 00 00 00               je 0x14021a834
0021A7B4  4C 8B 7C 24 48                  mov r15, qword ptr [rsp + 0x48]
0021A7B9  E9 77 F9 FF FF                  jmp 0x14021a135
0021A7BE  48 8B 5D B0                     mov rbx, qword ptr [rbp - 0x50]
0021A7C2  90                              nop
0021A7C3  80 7B 06 00                     cmp byte ptr [rbx + 6], 0
0021A7C7  C6 43 20 00                     mov byte ptr [rbx + 0x20], 0
0021A7CB  0F 85 EF 07 00 00               jne 0x14021afc0
0021A7D1  44 89 64 24 48                  mov dword ptr [rsp + 0x48], r12d
0021A7D6  0F 0D 8B BC 38 00 00            prefetchw byte ptr [rbx + 0x38bc]
0021A7DD  0F B7 83 BC 38 00 00            movzx eax, word ptr [rbx + 0x38bc]
0021A7E4  41 B9 80 00 00 00               mov r9d, 0x80
0021A7EA  0F B7 C8                        movzx ecx, ax
0021A7ED  66 0B CF                        or cx, di
0021A7F0  66 83 E1 FE                     and cx, 0xfffe
0021A7F4  66 41 0B C9                     or cx, r9w
0021A7F8  66 F0 0F B1 8B BC 38 00 00      lock cmpxchg word ptr [rbx + 0x38bc], cx
0021A801  74 31                           je 0x14021a834
0021A803  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
0021A808  E8 13 DE FE FF                  call 0x140208620
0021A80D  0F 0D 8B BC 38 00 00            prefetchw byte ptr [rbx + 0x38bc]
0021A814  0F B7 83 BC 38 00 00            movzx eax, word ptr [rbx + 0x38bc]
0021A81B  0F B7 C8                        movzx ecx, ax
0021A81E  66 0B CF                        or cx, di
0021A821  66 83 E1 FE                     and cx, 0xfffe
0021A825  66 41 0B C9                     or cx, r9w
0021A829  66 F0 0F B1 8B BC 38 00 00      lock cmpxchg word ptr [rbx + 0x38bc], cx
0021A832  75 CF                           jne 0x14021a803
0021A834  4C 89 A3 60 38 00 00            mov qword ptr [rbx + 0x3860], r12
0021A83B  48 8B 8D 50 01 00 00            mov rcx, qword ptr [rbp + 0x150]
0021A842  48 33 CC                        xor rcx, rsp
0021A845  E8 F6 1D 49 00                  call 0x1406ac640
0021A84A  4C 8D 9C 24 60 02 00 00         lea r11, [rsp + 0x260]
0021A852  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
0021A856  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
0021A85A  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
0021A85E  49 8B E3                        mov rsp, r11
0021A861  41 5F                           pop r15
0021A863  41 5E                           pop r14
0021A865  41 5D                           pop r13
0021A867  41 5C                           pop r12
0021A869  5D                              pop rbp
0021A86A  C3                              ret
0021A86B  CC                              int3
0021A86C  48 8B 4E 68                     mov rcx, qword ptr [rsi + 0x68]
0021A870  48 85 C9                        test rcx, rcx
0021A873  74 18                           je 0x14021a88d
0021A875  8B 83 D8 00 00 00               mov eax, dword ptr [rbx + 0xd8]
0021A87B  48 03 C1                        add rax, rcx
0021A87E  4C 01 20                        add qword ptr [rax], r12
0021A881  48 8B 80 A0 01 00 00            mov rax, qword ptr [rax + 0x1a0]
0021A888  48 85 C0                        test rax, rax
0021A88B  75 F1                           jne 0x14021a87e
0021A88D  F6 46 02 08                     test byte ptr [rsi + 2], 8
0021A891  74 14                           je 0x14021a8a7
0021A893  48 8D 05 66 56 DB 00            lea rax, [rip + 0xdb5666]
0021A89A  48 39 86 20 02 00 00            cmp qword ptr [rsi + 0x220], rax
0021A8A1  0F 85 CB 07 00 00               jne 0x14021b072
0021A8A7  48 83 BE 68 01 00 00 00         cmp qword ptr [rsi + 0x168], 0
0021A8AF  0F 84 F6 FB FF FF               je 0x14021a4ab
0021A8B5  48 8B CE                        mov rcx, rsi
0021A8B8  E8 EF 45 16 00                  call 0x14037eeac
0021A8BD  E9 E9 FB FF FF                  jmp 0x14021a4ab
0021A8C2  48 B8 00 03 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000300
0021A8CC  4C 39 20                        cmp qword ptr [rax], r12
0021A8CF  0F 84 A1 FD FF FF               je 0x14021a676
0021A8D5  48 B8 60 03 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000360
0021A8DF  4C 89 64 24 78                  mov qword ptr [rsp + 0x78], r12
0021A8E4  4C 89 65 80                     mov qword ptr [rbp - 0x80], r12
0021A8E8  4C 8B 08                        mov r9, qword ptr [rax]
0021A8EB  A0 69 03 00 00 80 F7 FF FF      movabs al, byte ptr [0xfffff78000000369]
0021A8F4  0F B6 C8                        movzx ecx, al
0021A8F7  84 C0                           test al, al
0021A8F9  49 8B C1                        mov rax, r9
0021A8FC  0F 84 EF 06 00 00               je 0x14021aff1
0021A902  49 D3 E0                        shl r8, cl
0021A905  49 F7 E0                        mul r8
0021A908  4C 8B C7                        mov r8, rdi
0021A90B  49 D3 E0                        shl r8, cl
0021A90E  0F BE 0D B1 C2 DA 00            movsx ecx, byte ptr [rip + 0xdac2b1]
0021A915  4C 8B F2                        mov r14, rdx
0021A918  48 89 54 24 78                  mov qword ptr [rsp + 0x78], rdx
0021A91D  49 8B C1                        mov rax, r9
0021A920  49 F7 E0                        mul r8
0021A923  48 8B 05 EE C9 DA 00            mov rax, qword ptr [rip + 0xdac9ee]
0021A92A  4C 8B C2                        mov r8, rdx
0021A92D  48 89 55 80                     mov qword ptr [rbp - 0x80], rdx
0021A931  49 F7 E6                        mul r14
0021A934  48 8B 05 DD C9 DA 00            mov rax, qword ptr [rip + 0xdac9dd]
0021A93B  4C 8B 74 24 38                  mov r14, qword ptr [rsp + 0x38]
0021A940  4C 8B CA                        mov r9, rdx
0021A943  49 F7 E0                        mul r8
0021A946  49 D3 E9                        shr r9, cl
0021A949  48 D3 EA                        shr rdx, cl
0021A94C  41 2B D1                        sub edx, r9d
0021A94F  4C 8B 4C 24 30                  mov r9, qword ptr [rsp + 0x30]
0021A954  0F 84 1C FD FF FF               je 0x14021a676
0021A95A  01 93 44 86 00 00               add dword ptr [rbx + 0x8644], edx
0021A960  01 93 4C 86 00 00               add dword ptr [rbx + 0x864c], edx
0021A966  E9 0B FD FF FF                  jmp 0x14021a676
0021A96B  41 8B D0                        mov edx, r8d
0021A96E  48 03 D2                        add rdx, rdx
0021A971  49 8B 4C D1 08                  mov rcx, qword ptr [r9 + rdx*8 + 8]
0021A976  49 03 CC                        add rcx, r12
0021A979  49 89 4C D1 08                  mov qword ptr [r9 + rdx*8 + 8], rcx
0021A97E  E9 81 FA FF FF                  jmp 0x14021a404
0021A983  45 33 E4                        xor r12d, r12d
0021A986  45 8B D4                        mov r10d, r12d
0021A989  45 8B FC                        mov r15d, r12d
0021A98C  45 8B F4                        mov r14d, r12d
0021A98F  45 8B DC                        mov r11d, r12d
0021A992  44 38 A3 DC 86 00 00            cmp byte ptr [rbx + 0x86dc], r12b
0021A999  74 54                           je 0x14021a9ef
0021A99B  33 C9                           xor ecx, ecx
0021A99D  E8 3E 3E 16 00                  call 0x14037e7e0
0021A9A2  0F B6 8B AC 00 00 00            movzx ecx, byte ptr [rbx + 0xac]
0021A9A9  4C 8B D0                        mov r10, rax
0021A9AC  48 8B 83 B0 00 00 00            mov rax, qword ptr [rbx + 0xb0]
0021A9B3  49 8B D2                        mov rdx, r10
0021A9B6  4C 89 65 A8                     mov qword ptr [rbp - 0x58], r12
0021A9BA  84 C9                           test cl, cl
0021A9BC  74 03                           je 0x14021a9c1
0021A9BE  48 D3 E2                        shl rdx, cl
0021A9C1  48 F7 E2                        mul rdx
0021A9C4  4D 8B F2                        mov r14, r10
0021A9C7  4C 8B FA                        mov r15, rdx
0021A9CA  48 89 55 A8                     mov qword ptr [rbp - 0x58], rdx
0021A9CE  48 8B 93 F8 86 00 00            mov rdx, qword ptr [rbx + 0x86f8]
0021A9D5  4D 8B DF                        mov r11, r15
0021A9D8  4C 2B 9B 80 86 00 00            sub r11, qword ptr [rbx + 0x8680]
0021A9DF  4C 2B F2                        sub r14, rdx
0021A9E2  44 38 25 AC C0 DA 00            cmp byte ptr [rip + 0xdac0ac], r12b
0021A9E9  0F 85 20 01 00 00               jne 0x14021ab0f
0021A9EF  48 8B 8B 00 87 00 00            mov rcx, qword ptr [rbx + 0x8700]
0021A9F6  49 03 CE                        add rcx, r14
0021A9F9  48 89 8B 00 87 00 00            mov qword ptr [rbx + 0x8700], rcx
0021AA00  48 8B 8B 78 87 00 00            mov rcx, qword ptr [rbx + 0x8778]
0021AA07  49 03 CB                        add rcx, r11
0021AA0A  48 89 8B 78 87 00 00            mov qword ptr [rbx + 0x8778], rcx
0021AA11  F6 46 02 20                     test byte ptr [rsi + 2], 0x20
0021AA15  74 30                           je 0x14021aa47
0021AA17  48 8B CB                        mov rcx, rbx
0021AA1A  E8 61 0D 00 00                  call 0x14021b780
0021AA1F  80 BB 08 8A 00 00 00            cmp byte ptr [rbx + 0x8a08], 0
0021AA26  49 8B CC                        mov rcx, r12
0021AA29  8B C0                           mov eax, eax
0021AA2B  0F 95 C1                        setne cl
0021AA2E  48 8D 0C 41                     lea rcx, [rcx + rax*2]
0021AA32  48 8D 89 F0 10 00 00            lea rcx, [rcx + 0x10f0]
0021AA39  48 8D 14 CB                     lea rdx, [rbx + rcx*8]
0021AA3D  48 8B 0C CB                     mov rcx, qword ptr [rbx + rcx*8]
0021AA41  49 03 CB                        add rcx, r11
0021AA44  48 89 0A                        mov qword ptr [rdx], rcx
0021AA47  F6 46 02 40                     test byte ptr [rsi + 2], 0x40
0021AA4B  74 10                           je 0x14021aa5d
0021AA4D  48 8B 86 C8 03 00 00            mov rax, qword ptr [rsi + 0x3c8]
0021AA54  48 85 C0                        test rax, rax
0021AA57  74 04                           je 0x14021aa5d
0021AA59  C6 40 40 01                     mov byte ptr [rax + 0x40], 1
0021AA5D  4C 89 93 F8 86 00 00            mov qword ptr [rbx + 0x86f8], r10
0021AA64  4C 89 BB 80 86 00 00            mov qword ptr [rbx + 0x8680], r15
0021AA6B  F6 46 02 02                     test byte ptr [rsi + 2], 2
0021AA6F  0F 84 4D FD FF FF               je 0x14021a7c2
0021AA75  48 8B 86 68 01 00 00            mov rax, qword ptr [rsi + 0x168]
0021AA7C  4C 8B 50 20                     mov r10, qword ptr [rax + 0x20]
0021AA80  4D 85 D2                        test r10, r10
0021AA83  0F 84 39 FD FF FF               je 0x14021a7c2
0021AA89  8B 0D 79 BE C4 00               mov ecx, dword ptr [rip + 0xc4be79]
0021AA8F  85 C9                           test ecx, ecx
0021AA91  0F 84 2B FD FF FF               je 0x14021a7c2
0021AA97  4C 8D 40 30                     lea r8, [rax + 0x30]
0021AA9B  44 8B C9                        mov r9d, ecx
0021AA9E  48 8D 1D DB 63 CF 00            lea rbx, [rip + 0xcf63db]
0021AAA5  4D 85 D5                        test r13, r10
0021AAA8  0F 85 3C 06 00 00               jne 0x14021b0ea
0021AAAE  4D 03 ED                        add r13, r13
0021AAB1  49 83 C0 18                     add r8, 0x18
0021AAB5  48 83 C3 04                     add rbx, 4
0021AAB9  49 83 E9 01                     sub r9, 1
0021AABD  75 E6                           jne 0x14021aaa5
0021AABF  E9 FA FC FF FF                  jmp 0x14021a7be
0021AAC4  0F B6 46 7C                     movzx eax, byte ptr [rsi + 0x7c]
0021AAC8  48 8D 14 C5 88 86 00 00         lea rdx, [rax*8 + 0x8688]
0021AAD0  48 8B 0C 13                     mov rcx, qword ptr [rbx + rdx]
0021AAD4  49 03 CC                        add rcx, r12
0021AAD7  48 89 0C 13                     mov qword ptr [rbx + rdx], rcx
0021AADB  40 80 E7 EF                     and dil, 0xef
0021AADF  E9 2A F8 FF FF                  jmp 0x14021a30e
0021AAE4  48 8B 44 24 30                  mov rax, qword ptr [rsp + 0x30]
0021AAE9  45 33 D2                        xor r10d, r10d
0021AAEC  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
0021AAF1  E9 72 F7 FF FF                  jmp 0x14021a268
0021AAF6  48 8B 86 C8 03 00 00            mov rax, qword ptr [rsi + 0x3c8]
0021AAFD  48 85 C0                        test rax, rax
0021AB00  0F 84 63 F9 FF FF               je 0x14021a469
0021AB06  C6 40 40 00                     mov byte ptr [rax + 0x40], 0
0021AB0A  E9 5A F9 FF FF                  jmp 0x14021a469
0021AB0F  48 B8 00 03 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000300
0021AB19  4C 39 20                        cmp qword ptr [rax], r12
0021AB1C  0F 84 CD FE FF FF               je 0x14021a9ef
0021AB22  48 B8 60 03 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000360
0021AB2C  4C 89 64 24 50                  mov qword ptr [rsp + 0x50], r12
0021AB31  4D 8B C2                        mov r8, r10
0021AB34  4C 8B 08                        mov r9, qword ptr [rax]
0021AB37  A0 69 03 00 00 80 F7 FF FF      movabs al, byte ptr [0xfffff78000000369]
0021AB40  0F B6 C8                        movzx ecx, al
0021AB43  84 C0                           test al, al
0021AB45  49 8B C1                        mov rax, r9
0021AB48  0F 84 CD 04 00 00               je 0x14021b01b
0021AB4E  48 D3 E2                        shl rdx, cl
0021AB51  48 F7 E2                        mul rdx
0021AB54  33 C0                           xor eax, eax
0021AB56  49 D3 E0                        shl r8, cl
0021AB59  0F BE 0D 66 C0 DA 00            movsx ecx, byte ptr [rip + 0xdac066]
0021AB60  4C 8B E2                        mov r12, rdx
0021AB63  48 89 45 88                     mov qword ptr [rbp - 0x78], rax
0021AB67  49 8B C1                        mov rax, r9
0021AB6A  48 89 54 24 50                  mov qword ptr [rsp + 0x50], rdx
0021AB6F  49 F7 E0                        mul r8
0021AB72  48 8B 05 9F C7 DA 00            mov rax, qword ptr [rip + 0xdac79f]
0021AB79  4C 8B C2                        mov r8, rdx
0021AB7C  48 89 55 88                     mov qword ptr [rbp - 0x78], rdx
0021AB80  49 F7 E4                        mul r12
0021AB83  48 8B 05 8E C7 DA 00            mov rax, qword ptr [rip + 0xdac78e]
0021AB8A  4C 8B CA                        mov r9, rdx
0021AB8D  49 F7 E0                        mul r8
0021AB90  49 D3 E9                        shr r9, cl
0021AB93  48 D3 EA                        shr rdx, cl
0021AB96  41 2B D1                        sub edx, r9d
0021AB99  0F 85 8A 02 00 00               jne 0x14021ae29
0021AB9F  45 33 E4                        xor r12d, r12d
0021ABA2  E9 48 FE FF FF                  jmp 0x14021a9ef
0021ABA7  0F B6 D0                        movzx edx, al
0021ABAA  41 0F B6 CD                     movzx ecx, r13b
0021ABAE  E8 49 AB 2D 00                  call 0x1404f56fc
0021ABB3  E9 9F F9 FF FF                  jmp 0x14021a557
0021ABB8  80 F9 02                        cmp cl, 2
0021ABBB  0F 85 97 03 00 00               jne 0x14021af58
0021ABC1  C6 40 11 05                     mov byte ptr [rax + 0x11], 5
0021ABC5  48 8B D0                        mov rdx, rax
0021ABC8  48 8B 48 18                     mov rcx, qword ptr [rax + 0x18]
0021ABCC  E8 5F EF FF FF                  call 0x140219b30
0021ABD1  83 6F 04 01                     sub dword ptr [rdi + 4], 1
0021ABD5  0F 84 06 FA FF FF               je 0x14021a5e1
0021ABDB  45 33 C0                        xor r8d, r8d
0021ABDE  E9 A3 F9 FF FF                  jmp 0x14021a586
0021ABE3  F7 46 74 00 04 00 00            test dword ptr [rsi + 0x74], 0x400
0021ABEA  75 1D                           jne 0x14021ac09
0021ABEC  8B 86 4C 04 00 00               mov eax, dword ptr [rsi + 0x44c]
0021ABF2  F3 48 0F B8 D0                  popcnt rdx, rax
0021ABF7  48 8B C7                        mov rax, rdi
0021ABFA  48 C1 E8 04                     shr rax, 4
0021ABFE  83 E0 1F                        and eax, 0x1f
0021AC01  3B C2                           cmp eax, edx
0021AC03  0F 82 D6 01 00 00               jb 0x14021addf
0021AC09  44 01 BB 44 86 00 00            add dword ptr [rbx + 0x8644], r15d
0021AC10  44 01 BE 8C 02 00 00            add dword ptr [rsi + 0x28c], r15d
0021AC17  49 8B C3                        mov rax, r11
0021AC1A  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
0021AC1F  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0021AC24  48 3B 73 18                     cmp rsi, qword ptr [rbx + 0x18]
0021AC28  0F 84 2C F6 FF FF               je 0x14021a25a
0021AC2E  48 8B D3                        mov rdx, rbx
0021AC31  4C 89 5C 24 30                  mov qword ptr [rsp + 0x30], r11
0021AC36  48 8B CE                        mov rcx, rsi
0021AC39  4C 89 44 24 38                  mov qword ptr [rsp + 0x38], r8
0021AC3E  E8 5D CF 03 00                  call 0x140257ba0
0021AC43  BA FF FF FF FF                  mov edx, 0xffffffff
0021AC48  41 BB 48 00 00 00               mov r11d, 0x48
0021AC4E  83 F8 08                        cmp eax, 8
0021AC51  0F 8D 8D FE FF FF               jge 0x14021aae4
0021AC57  44 01 BB 6C 86 00 00            add dword ptr [rbx + 0x866c], r15d
0021AC5E  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
0021AC63  45 33 D2                        xor r10d, r10d
0021AC66  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
0021AC6B  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0021AC70  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
0021AC75  E9 EE F5 FF FF                  jmp 0x14021a268
0021AC7A  B8 F7 FF 00 00                  mov eax, 0xfff7
0021AC7F  B2 01                           mov dl, 1
0021AC81  48 8B CB                        mov rcx, rbx
0021AC84  66 23 F8                        and di, ax
0021AC87  E8 F4 B9 22 00                  call 0x140446680
0021AC8C  48 8B D0                        mov rdx, rax
0021AC8F  48 85 C0                        test rax, rax
0021AC92  0F 84 5D 02 00 00               je 0x14021aef5
0021AC98  44 8B A8 10 42 00 00            mov r13d, dword ptr [rax + 0x4210]
0021AC9F  48 B8 08 00 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000008
0021ACA9  4C 8B 38                        mov r15, qword ptr [rax]
0021ACAC  4C 8B 15 FD BB C4 00            mov r10, qword ptr [rip + 0xc4bbfd]
0021ACB3  4C 8B 05 EE BB C4 00            mov r8, qword ptr [rip + 0xc4bbee]
0021ACBA  4C 8B 8A 00 42 00 00            mov r9, qword ptr [rdx + 0x4200]
0021ACC1  48 8B 8A 08 42 00 00            mov rcx, qword ptr [rdx + 0x4208]
0021ACC8  4D 3B C1                        cmp r8, r9
0021ACCB  41 0F 95 C4                     setne r12b
0021ACCF  4C 3B D1                        cmp r10, rcx
0021ACD2  0F 95 C0                        setne al
0021ACD5  83 3D 6C BF DA 00 00            cmp dword ptr [rip + 0xdabf6c], 0
0021ACDC  44 0F B6 F0                     movzx r14d, al
0021ACE0  41 0F B6 C4                     movzx eax, r12b
0021ACE4  44 0F 45 F0                     cmovne r14d, eax
0021ACE8  4D 3B C1                        cmp r8, r9
0021ACEB  74 14                           je 0x14021ad01
0021ACED  49 8B C7                        mov rax, r15
0021ACF0  4C 89 82 00 42 00 00            mov qword ptr [rdx + 0x4200], r8
0021ACF7  48 C1 E8 12                     shr rax, 0x12
0021ACFB  89 82 10 42 00 00               mov dword ptr [rdx + 0x4210], eax
0021AD01  45 84 F6                        test r14b, r14b
0021AD04  0F 85 30 01 00 00               jne 0x14021ae3a
0021AD0A  4D 3B C1                        cmp r8, r9
0021AD0D  0F 84 81 01 00 00               je 0x14021ae94
0021AD13  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
0021AD1C  4C 8B 81 B8 8E 00 00            mov r8, qword ptr [rcx + 0x8eb8]
0021AD23  4D 85 C0                        test r8, r8
0021AD26  0F 85 A1 01 00 00               jne 0x14021aecd
0021AD2C  FB                              sti
0021AD2D  48 B8 14 00 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000014
0021AD37  45 0F B6 CE                     movzx r9d, r14b
0021AD3B  4D 8B C7                        mov r8, r15
0021AD3E  41 8B D5                        mov edx, r13d
0021AD41  48 8B CB                        mov rcx, rbx
0021AD44  48 8B 00                        mov rax, qword ptr [rax]
0021AD47  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
0021AD4B  48 8D 45 C0                     lea rax, [rbp - 0x40]
0021AD4F  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0021AD54  E8 E7 9A 01 00                  call 0x140234840
0021AD59  80 7B 21 00                     cmp byte ptr [rbx + 0x21], 0
0021AD5D  74 1C                           je 0x14021ad7b
0021AD5F  48 8D 45 C0                     lea rax, [rbp - 0x40]
0021AD63  45 0F B6 CE                     movzx r9d, r14b
0021AD67  45 0F B6 C4                     movzx r8d, r12b
0021AD6B  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0021AD70  49 8B D7                        mov rdx, r15
0021AD73  48 8B CB                        mov rcx, rbx
0021AD76  E8 05 6B 18 00                  call 0x1403a1880
0021AD7B  41 BD 01 00 00 00               mov r13d, 1
0021AD81  FA                              cli
0021AD82  E9 40 F7 FF FF                  jmp 0x14021a4c7
0021AD87  66 0F 1F 84 00 00 00 00 00      nop word ptr [rax + rax]
0021AD90  41 FF C6                        inc r14d
0021AD93  44 85 35 12 A5 DA 00            test dword ptr [rip + 0xdaa512], r14d
0021AD9A  0F 84 86 01 00 00               je 0x14021af26
0021ADA0  F3 90                           pause
0021ADA2  8B 07                           mov eax, dword ptr [rdi]
0021ADA4  84 C0                           test al, al
0021ADA6  78 E8                           js 0x14021ad90
0021ADA8  F0 0F BA 2F 07                  lock bts dword ptr [rdi], 7
0021ADAD  72 E1                           jb 0x14021ad90
0021ADAF  45 33 C0                        xor r8d, r8d
0021ADB2  E9 BA F7 FF FF                  jmp 0x14021a571
0021ADB7  41 0F 0D 08                     prefetchw byte ptr [r8]
0021ADBB  41 8B 00                        mov eax, dword ptr [r8]
0021ADBE  8B D0                           mov edx, eax
0021ADC0  0F BA F2 15                     btr edx, 0x15
0021ADC4  F0 41 0F B1 10                  lock cmpxchg dword ptr [r8], edx
0021ADC9  75 F3                           jne 0x14021adbe
0021ADCB  0F BA E0 15                     bt eax, 0x15
0021ADCF  0F 83 19 F7 FF FF               jae 0x14021a4ee
0021ADD5  E8 F6 83 04 00                  call 0x1402631d0
0021ADDA  E9 0F F7 FF FF                  jmp 0x14021a4ee
0021ADDF  44 01 BB 48 86 00 00            add dword ptr [rbx + 0x8648], r15d
0021ADE6  44 01 BE DC 02 00 00            add dword ptr [rsi + 0x2dc], r15d
0021ADED  E9 25 FE FF FF                  jmp 0x14021ac17
0021ADF2  41 0F 0D 08                     prefetchw byte ptr [r8]
0021ADF6  41 8B 00                        mov eax, dword ptr [r8]
0021ADF9  8B D0                           mov edx, eax
0021ADFB  0F BA F2 15                     btr edx, 0x15
0021ADFF  F0 41 0F B1 10                  lock cmpxchg dword ptr [r8], edx
0021AE04  75 F3                           jne 0x14021adf9
0021AE06  0F BA E0 15                     bt eax, 0x15
0021AE0A  0F 83 25 F7 FF FF               jae 0x14021a535
0021AE10  E8 BB 83 04 00                  call 0x1402631d0
0021AE15  E9 1B F7 FF FF                  jmp 0x14021a535
0021AE1A  4C 8B 4C 24 30                  mov r9, qword ptr [rsp + 0x30]
0021AE1F  4C 8B 74 24 38                  mov r14, qword ptr [rsp + 0x38]
0021AE24  E9 4D F8 FF FF                  jmp 0x14021a676
0021AE29  01 93 44 86 00 00               add dword ptr [rbx + 0x8644], edx
0021AE2F  01 93 4C 86 00 00               add dword ptr [rbx + 0x864c], edx
0021AE35  E9 65 FD FF FF                  jmp 0x14021ab9f
0021AE3A  8B 82 14 42 00 00               mov eax, dword ptr [rdx + 0x4214]
0021AE40  44 3B E8                        cmp r13d, eax
0021AE43  4C 89 92 08 42 00 00            mov qword ptr [rdx + 0x4208], r10
0021AE4A  44 0F 43 E8                     cmovae r13d, eax
0021AE4E  49 8B C7                        mov rax, r15
0021AE51  48 C1 E8 12                     shr rax, 0x12
0021AE55  89 82 14 42 00 00               mov dword ptr [rdx + 0x4214], eax
0021AE5B  E9 AA FE FF FF                  jmp 0x14021ad0a
0021AE60  8B D0                           mov edx, eax
0021AE62  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
0021AE66  2B D1                           sub edx, ecx
0021AE68  83 FA 20                        cmp edx, 0x20
0021AE6B  0F 83 0C 01 00 00               jae 0x14021af7d
0021AE71  41 8B 81 C4 00 00 00            mov eax, dword ptr [r9 + 0xc4]
0021AE78  8B CA                           mov ecx, edx
0021AE7A  D3 E0                           shl eax, cl
0021AE7C  83 C8 01                        or eax, 1
0021AE7F  89 44 24 5C                     mov dword ptr [rsp + 0x5c], eax
0021AE83  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
0021AE88  49 89 81 C0 00 00 00            mov qword ptr [r9 + 0xc0], rax
0021AE8F  E9 49 F5 FF FF                  jmp 0x14021a3dd
0021AE94  45 84 F6                        test r14b, r14b
0021AE97  0F 85 76 FE FF FF               jne 0x14021ad13
0021AE9D  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
0021AEA6  4C 8B 81 B8 8E 00 00            mov r8, qword ptr [rcx + 0x8eb8]
0021AEAD  4D 85 C0                        test r8, r8
0021AEB0  0F 85 DA 00 00 00               jne 0x14021af90
0021AEB6  FB                              sti
0021AEB7  48 B8 14 00 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000014
0021AEC1  48 8B 00                        mov rax, qword ptr [rax]
0021AEC4  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
0021AEC8  E9 8C FE FF FF                  jmp 0x14021ad59
0021AECD  41 0F 0D 08                     prefetchw byte ptr [r8]
0021AED1  41 8B 00                        mov eax, dword ptr [r8]
0021AED4  8B D0                           mov edx, eax
0021AED6  0F BA F2 15                     btr edx, 0x15
0021AEDA  F0 41 0F B1 10                  lock cmpxchg dword ptr [r8], edx
0021AEDF  75 F3                           jne 0x14021aed4
0021AEE1  0F BA E0 15                     bt eax, 0x15
0021AEE5  0F 83 41 FE FF FF               jae 0x14021ad2c
0021AEEB  E8 E0 82 04 00                  call 0x1402631d0
0021AEF0  E9 37 FE FF FF                  jmp 0x14021ad2c
0021AEF5  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
0021AEFE  4C 8B 81 B8 8E 00 00            mov r8, qword ptr [rcx + 0x8eb8]
0021AF05  4D 85 C0                        test r8, r8
0021AF08  0F 85 BB 00 00 00               jne 0x14021afc9
0021AF0E  FB                              sti
0021AF0F  48 B8 14 00 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000014
0021AF19  48 8B 00                        mov rax, qword ptr [rax]
0021AF1C  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
0021AF20  FA                              cli
0021AF21  E9 A1 F5 FF FF                  jmp 0x14021a4c7
0021AF26  8B 05 8C BB DA 00               mov eax, dword ptr [rip + 0xdabb8c]
0021AF2C  A8 40                           test al, 0x40
0021AF2E  0F 84 6C FE FF FF               je 0x14021ada0
0021AF34  E8 57 45 0F 00                  call 0x14030f490
0021AF39  84 C0                           test al, al
0021AF3B  0F 84 5F FE FF FF               je 0x14021ada0
0021AF41  41 8B CE                        mov ecx, r14d
0021AF44  E8 17 45 0F 00                  call 0x14030f460
0021AF49  E9 54 FE FF FF                  jmp 0x14021ada2
0021AF4E  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
0021AF53  E9 05 F3 FF FF                  jmp 0x14021a25d
0021AF58  80 F9 04                        cmp cl, 4
0021AF5B  0F 84 9B 00 00 00               je 0x14021affc
0021AF61  45 33 C9                        xor r9d, r9d
0021AF64  41 B8 00 01 00 00               mov r8d, 0x100
0021AF6A  48 8B D0                        mov rdx, rax
0021AF6D  49 8B CC                        mov rcx, r12
0021AF70  E8 5B 57 13 00                  call 0x1403506d0
0021AF75  45 33 C0                        xor r8d, r8d
0021AF78  E9 09 F6 FF FF                  jmp 0x14021a586
0021AF7D  44 89 6C 24 5C                  mov dword ptr [rsp + 0x5c], r13d
0021AF82  E9 FC FE FF FF                  jmp 0x14021ae83
0021AF87  44 88 63 06                     mov byte ptr [rbx + 6], r12b
0021AF8B  E9 0D F8 FF FF                  jmp 0x14021a79d
0021AF90  41 0F 0D 08                     prefetchw byte ptr [r8]
0021AF94  41 8B 00                        mov eax, dword ptr [r8]
0021AF97  8B D0                           mov edx, eax
0021AF99  0F BA F2 15                     btr edx, 0x15
0021AF9D  F0 41 0F B1 10                  lock cmpxchg dword ptr [r8], edx
0021AFA2  75 F3                           jne 0x14021af97
0021AFA4  0F BA E0 15                     bt eax, 0x15
0021AFA8  0F 83 08 FF FF FF               jae 0x14021aeb6
0021AFAE  E8 1D 82 04 00                  call 0x1402631d0
0021AFB3  E9 FE FE FF FF                  jmp 0x14021aeb6
0021AFB8  48 F7 E2                        mul rdx
0021AFBB  E9 3F F2 FF FF                  jmp 0x14021a1ff
0021AFC0  C6 43 06 00                     mov byte ptr [rbx + 6], 0
0021AFC4  E9 08 F8 FF FF                  jmp 0x14021a7d1
0021AFC9  41 0F 0D 08                     prefetchw byte ptr [r8]
0021AFCD  41 8B 00                        mov eax, dword ptr [r8]
0021AFD0  8B D0                           mov edx, eax
0021AFD2  0F BA F2 15                     btr edx, 0x15
0021AFD6  F0 41 0F B1 10                  lock cmpxchg dword ptr [r8], edx
0021AFDB  75 F3                           jne 0x14021afd0
0021AFDD  0F BA E0 15                     bt eax, 0x15
0021AFE1  0F 83 27 FF FF FF               jae 0x14021af0e
0021AFE7  E8 E4 81 04 00                  call 0x1402631d0
0021AFEC  E9 1D FF FF FF                  jmp 0x14021af0e
0021AFF1  49 F7 E0                        mul r8
0021AFF4  4C 8B C7                        mov r8, rdi
0021AFF7  E9 12 F9 FF FF                  jmp 0x14021a90e
0021AFFC  C6 40 11 05                     mov byte ptr [rax + 0x11], 5
0021B000  48 8B D7                        mov rdx, rdi
0021B003  44 89 47 04                     mov dword ptr [rdi + 4], r8d
0021B007  4C 8B C0                        mov r8, rax
0021B00A  48 8B 48 18                     mov rcx, qword ptr [rax + 0x18]
0021B00E  E8 3D CC FE FF                  call 0x140207c50
0021B013  45 33 C0                        xor r8d, r8d
0021B016  E9 6B F5 FF FF                  jmp 0x14021a586
0021B01B  48 F7 E2                        mul rdx
0021B01E  33 C0                           xor eax, eax
0021B020  E9 34 FB FF FF                  jmp 0x14021ab59
0021B025  0F B6 86 04 02 00 00            movzx eax, byte ptr [rsi + 0x204]
0021B02C  44 8B C0                        mov r8d, eax
0021B02F  83 F8 07                        cmp eax, 7
0021B032  0F 83 69 F4 FF FF               jae 0x14021a4a1
0021B038  8B 46 54                        mov eax, dword ptr [rsi + 0x54]
0021B03B  8B 56 50                        mov edx, dword ptr [rsi + 0x50]
0021B03E  3B D0                           cmp edx, eax
0021B040  0F 46 D0                        cmovbe edx, eax
0021B043  0F B6 86 05 02 00 00            movzx eax, byte ptr [rsi + 0x205]
0021B04A  33 C9                           xor ecx, ecx
0021B04C  3B 15 2A A3 DA 00               cmp edx, dword ptr [rip + 0xdaa32a]
0021B052  0F 93 C1                        setae cl
0021B055  42 8D 0C 41                     lea ecx, [rcx + r8*2]
0021B059  0F AF 0D 80 A3 DA 00            imul ecx, dword ptr [rip + 0xdaa380]
0021B060  03 C8                           add ecx, eax
0021B062  48 8B 83 B0 86 00 00            mov rax, qword ptr [rbx + 0x86b0]
0021B069  4C 01 24 C8                     add qword ptr [rax + rcx*8], r12
0021B06D  E9 2F F4 FF FF                  jmp 0x14021a4a1
0021B072  4C 8B 83 C0 00 00 00            mov r8, qword ptr [rbx + 0xc0]
0021B079  48 8B 86 40 02 00 00            mov rax, qword ptr [rsi + 0x240]
0021B080  41 0F B7 88 88 00 00 00         movzx ecx, word ptr [r8 + 0x88]
0021B088  48 8B 54 C8 08                  mov rdx, qword ptr [rax + rcx*8 + 8]
0021B08D  49 8B 80 80 00 00 00            mov rax, qword ptr [r8 + 0x80]
0021B094  48 23 D0                        and rdx, rax
0021B097  48 3B D0                        cmp rdx, rax
0021B09A  0F 84 07 F8 FF FF               je 0x14021a8a7
0021B0A0  4C 01 A3 A8 86 00 00            add qword ptr [rbx + 0x86a8], r12
0021B0A7  E9 FB F7 FF FF                  jmp 0x14021a8a7
0021B0AC  49 8B C3                        mov rax, r11
0021B0AF  49 8B CF                        mov rcx, r15
0021B0B2  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0021B0B7  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
0021B0BC  E9 9C F1 FF FF                  jmp 0x14021a25d
0021B0C1  BA 64 00 00 00                  mov edx, 0x64
0021B0C6  E9 9A F2 FF FF                  jmp 0x14021a365
0021B0CB  41 B8 64 00 00 00               mov r8d, 0x64
0021B0D1  E9 0D F6 FF FF                  jmp 0x14021a6e3
0021B0D6  41 8B 0A                        mov ecx, dword ptr [r10]
0021B0D9  0F 33                           rdpmc
0021B0DB  48 C1 E2 20                     shl rdx, 0x20
0021B0DF  48 0B C2                        or rax, rdx
0021B0E2  49 89 03                        mov qword ptr [r11], rax
0021B0E5  E9 93 F6 FF FF                  jmp 0x14021a77d
0021B0EA  8B 0B                           mov ecx, dword ptr [rbx]
0021B0EC  0F 33                           rdpmc
0021B0EE  48 C1 E2 20                     shl rdx, 0x20
0021B0F2  48 0B C2                        or rax, rdx
0021B0F5  49 89 00                        mov qword ptr [r8], rax
0021B0F8  E9 B1 F9 FF FF                  jmp 0x14021aaae
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiRetireDpcList(__int64 a1, int a2)
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
    __int64 v_rsp;
    unsigned __int64 v_stack_m188;
    unsigned __int64 v_stack_m1C0;
    unsigned __int64 v_stack_m1C4;
    unsigned int v_stack_m1C8;
    unsigned __int64 v_stack_m1D8;
    unsigned __int64 v_stack_m1E0;
    unsigned __int64 v_stack_m1E8;
    unsigned __int64 v_stack_m1F0;
    unsigned __int64 v_stack_m200;
    unsigned int v_stack_m204;
    unsigned __int64 v_stack_m208;
    unsigned __int64 v_stack_m210;
    unsigned __int64 v_stack_m218;
    unsigned __int64 v_stack_m220;
    unsigned int v_stack_m228;
    unsigned __int64 v_stack_m230;
    unsigned __int64 v_stack_m238;
    unsigned __int64 v_stack_m240;
    unsigned __int64 v_stack_m250;
    unsigned __int64 v_stack_m258;
    unsigned __int8 v_stack_m268;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;

    v_stack_p10 = v_rbx;
    v_stack_p18 = v_rsi;
    v_stack_p20 = v_rdi;
    v_rsp = (v_rsp) - (608);
    result = (*(unsigned __int64 *)(v_rip + 12519010)) ^ (v_rsp);
    v_stack_m38 = result;
    v_stack_m1D8 = a1;
    a2 = 0;
    result = memset(v_stack_m1C4, a2, 396, a4);
    v_r12 = 0;
    v_stack_m250 = a1 + 34552;
    v_stack_m1C8 = 0;
    v_stack_m240 = a1 + 34552;
    v_stack_m258 = a1 + 34432;
    v_stack_m238 = a1 + 34432;
loc_0021A135:
    *(unsigned __int8 *)(a1 + 32) = 1;
    if ((*(unsigned __int8 *)(a1 + 34524)) == 0) goto loc_0021AAE4;
    a1 = 0;
    result = KeQueryPerformanceCounter(a1, (unsigned int)(0xFFFFFFFFULL), 396, a4);
    v_r10 = 0;
    v_stack_m1F0 = 0;
    if ((unsigned __int8)(*(unsigned __int8 *)(a1 + 172)) != 0) {
        a2 = (result) << ((unsigned __int8)(*(unsigned __int8 *)(a1 + 172)));
    }
    v_stack_m1F0 = a2;
    v_r12 = (a2) - (*(unsigned __int64 *)(v_stack_m238));
    v_stack_m258 = v_stack_m238;
    if ((*(unsigned __int8 *)(v_rip + 14338293)) == 0) goto loc_0021AF4E;
    if ((*(unsigned __int64 *)(v_stack_m238)) == 0) goto loc_0021B0AC;
    v_stack_m220 = 0;
    v_stack_m218 = 0;
    if ((unsigned __int8)(v_stack_m238) == 0) goto loc_0021AFB8;
    a2 = (*(unsigned __int64 *)(a1 + 34552)) << ((unsigned __int8)((unsigned __int8)(v_stack_m238)));
    a3 = (result) << ((unsigned __int8)((unsigned __int8)(v_stack_m238)));
loc_0021A1FF:
    v_stack_m220 = a2;
    v_stack_m218 = a2;
    v_r10 = (a2) >> ((unsigned __int8)((__int8)(*(unsigned __int8 *)(v_rip + 14338496))));
    v_stack_m258 = v_stack_m238;
    v_r15 = (a2) >> ((unsigned __int8)((__int8)(*(unsigned __int8 *)(v_rip + 14338496))));
    v_stack_m250 = v_stack_m240;
    v_r15 = (unsigned int)((v_r15) - ((unsigned int)(v_r10)));
    if (condition_is_not_equal) goto loc_0021ABE3;
loc_0021A25A:
    v_r10 = 0;
loc_0021A25D:
loc_0021A268:
    *(unsigned __int64 *)(v_stack_m240) = result;
    *(unsigned __int64 *)(v_stack_m238) = a2;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 72)) + (v_r12);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 72) = a1;
    result = v_stack_m238;
    if ((*(unsigned __int64 *)(a1 + 8)) != (*(unsigned __int64 *)(a1 + 24))) {
        result = *(unsigned int *)(a1 + 34488);
        a1 = *(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 80);
        result = (result) * (v_r12);
        result = (result) >> (16);
        a1 = (a1) + (result);
        if (a1 > ((unsigned int)(0xFFFFFFFFULL))) { a1 = (unsigned int)(0xFFFFFFFFULL); }
        *(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 80) = (unsigned int)(a1);
    }
    if ((((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 8) + 2))) & (190)) == 0) goto loc_0021A4AB;
    v_rdi = *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 8) + 2);
    if (sign_flag) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 544);
        a2 = (unsigned int)(v_r12 + 1);
        a3 = *(unsigned __int64 *)(a1 + 35760);
        a4 = *(unsigned int *)(result + 400);
        result = (unsigned int)(a4);
        result = (unsigned int)((result) >> (13));
        result = (unsigned int)((result) & (0x3FFFFULL));
        a4 = (a4) >> (4);
        a4 = (unsigned int)((a4) & (511));
        a2 = (unsigned int)((a2) << ((unsigned __int8)(a1)));
        a1 = (unsigned int)((a1) + (-2));
        a2 = (unsigned int)((a2) ^ ((unsigned int)(result)));
        v_stack_m228 = (unsigned int)(a1);
        a1 = *(unsigned __int64 *)(a3 + a1 * 8);
        a2 = *(unsigned __int64 *)(a1 + a2 * 8 + 8);
        result = *(unsigned __int64 *)(a2 + a4 * 8);
        result = (result) + (v_r12);
        *(unsigned __int64 *)(a2 + a4 * 8) = result;
        v_rdi = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 8) + 2)) & (127));
    }
    if ((((unsigned __int8)(v_rdi)) & (16)) != 0) goto loc_0021AAC4;
loc_0021A30E:
    if ((((unsigned __int8)(v_rdi)) & (32)) == 0) goto loc_0021A45F;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 1672) == 0) goto loc_0021A45B;
    if (*(unsigned __int64 *)(a1 + 35248) == 0) goto loc_0021B0C1;
    if (*(unsigned __int64 *)(a1 + 35256) == 0) goto loc_0021B0C1;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 35256) + 112)) != 0) goto loc_0021A35F;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 35256) + 80)))) < ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 35248) + 528))))) goto loc_0021A365;
    goto loc_0021A365;
loc_0021A35F:
loc_0021A365:
loc_0021A36F:
    if (((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 35248) + 528)))) + 132)))) <= ((unsigned int)(*(unsigned __int16 *)(a1 + 35434)))) goto loc_0021A383;
    a3 = (unsigned int)((0) + 1);
    a1 = (a1 + 35434) + (2);
    if (((unsigned int)(a3)) < 3) goto loc_0021A36F;
loc_0021A383:
    result = (unsigned __int8)(-((unsigned __int8)(*(unsigned __int8 *)(a1 + 35336))));
    v_stack_m230 = 0;
    a2 = ((unsigned int)((unsigned int)(a3))) + ((unsigned int)((unsigned int)(a3)));
    a1 = (unsigned int)((a1) & (8));
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 1672) + a1 * 1 + a2 * 8)) + (v_r12);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 1672) + a1 * 1 + a2 * 8) = a1;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13592201)))) > ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 1672) + 192))))) goto loc_0021AE60;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 1672) + 192))) - ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13592201)))));
    result = (unsigned int)(*(unsigned int *)(v_rip + 13592201));
    if (((unsigned int)(a1)) < 32) {
        result = (unsigned int)(v_r12 + 1);
        result = (unsigned int)((result) << ((unsigned __int8)(a1)));
    }
    if ((*(unsigned int *)(v_rip + 14338428)) != 0) goto loc_0021A404;
    if ((((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 8) + 516) - 2)) & (0xFFFFFFFBULL)) == 0) goto loc_0021A96B;
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 8) + 516))) == 5) goto loc_0021A96B;
loc_0021A404:
    result = *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 8) + 516) - 2;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 1616)) != 0) {
        result = (unsigned __int8)(*(unsigned __int8 *)(a1 + 35336));
        a1 = (unsigned int)(a3);
        a1 = (a1) + (8);
        a1 = (a1) + (a1);
        result = (unsigned __int8)(-(result));
        a2 = (unsigned int)((a2) & (8));
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 1672) + a1 * 8;
        a1 = *(unsigned __int64 *)(a2 + result * 1);
        a1 = (a1) + (v_r12);
        *(unsigned __int64 *)(a2 + result * 1) = a1;
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 1616);
        a2 = (unsigned int)(a3);
        a1 = *(unsigned __int64 *)(result + 1672);
        result = 64;
        if ((unsigned __int8)(*(unsigned __int8 *)(a1 + 35336)) != 0) { result = 72; }
        a2 = (a2) + (a2);
        result = (result) + (a1);
    }
    v_rdi = (unsigned __int8)((v_rdi) & (223));
loc_0021A45F:
    if ((((unsigned __int8)(v_rdi)) & (64)) != 0) goto loc_0021AAF6;
loc_0021A469:
    if ((*(unsigned __int8 *)(v_rip + 14337646)) != 0) {
        a4 = 0;
        a3 = v_r12;
        a2 = *(unsigned __int64 *)(a1 + 8);
        a1 = a1;
        result = KiUpdateThreadHgsFeedback(a1, a2, a3, a4);
    }
    if ((*(unsigned __int64 *)(a1 + 34480)) == 0) goto loc_0021A4A1;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 544)) != (v_rip + 14375532)) goto loc_0021B025;
loc_0021A4A1:
    if ((((unsigned __int8)(v_rdi)) & (190)) != 0) goto loc_0021A86C;
loc_0021A4AB:
    result = KiRcuCheckQuiescent(a1, a2, a3, a4);
    if ((((unsigned __int8)((unsigned int)((unsigned int)(v_r12 + 1)))) & (8)) != 0) goto loc_0021AC7A;
loc_0021A4C7:
    if ((((unsigned __int8)((unsigned int)((unsigned int)(v_r12 + 1)))) & (64)) == 0) goto loc_0021A4F8;
    v_rdi = (unsigned __int16)(((unsigned int)((unsigned int)(v_r12 + 1))) & ((unsigned __int16)((unsigned int)(0xFFBFULL))));
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536) != 0) goto loc_0021ADB7;
loc_0021A4EE:
    result = KiNormalPriorityReadyScan(a1, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), a4);
loc_0021A4F8:
    a4 = 0;
    result = KiExecuteAllDpcs(a1, *(unsigned __int64 *)(a1 + 8), v_stack_m1C8, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0021A983;
    if ((((unsigned __int8)(v_rdi)) & (4)) == 0) goto loc_0021A604;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536) != 0) goto loc_0021ADF2;
loc_0021A535:
    if ((*(unsigned int *)(v_rip + 14337999)) != 0) goto loc_0021ABA7;
loc_0021A557:
    a3 = 0;
    if (condition_is_below) goto loc_0021AD90;
loc_0021A571:
    if ((*(unsigned int *)(a1 + 33600 + 4)) != 0) goto loc_0021A5E1;
    *(unsigned int *)(a1 + 33600 + 4) = 1;
loc_0021A586:
    if ((*(unsigned __int64 *)(a1 + 33600 + 8)) == (a1 + 33600 + 8)) goto loc_0021A5E1;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 33600 + 8)) + 8)) != (*(unsigned __int64 *)(a1 + 33600 + 8))) goto loc_0021A5A3;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 33600 + 8) + 8))) != (*(unsigned __int64 *)(a1 + 33600 + 8))) {
        a1 = 3;
    }
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 33600 + 8) + 8)) = a1;
    *(unsigned __int64 *)(a1 + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 33600 + 8) + 8);
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 33600 + 8) + 16))) != 1) goto loc_0021ABB8;
    a4 = 0;
    result = KiTryUnwaitThread(*(unsigned __int64 *)(gs_base + (0 + 32)), *(unsigned __int64 *)(a1 + 33600 + 8), *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 33600 + 8) + 18), a4);
    if ((unsigned __int8)(result) == 0) goto loc_0021A586;
    if ((unsigned __int8)(result) != 0) goto loc_0021A586;
loc_0021A5E1:
    v_stack_m268 = (unsigned __int8)(v_cr8);
    a4 = 0;
    a2 = 0;
    result = KiExitDispatcher(*(unsigned __int64 *)(gs_base + (0 + 32)), a2, 1, a4);
loc_0021A604:
    v_r12 = 0;
    if ((*(unsigned __int8 *)(a1 + 34524)) == 0) goto loc_0021AE1A;
    a1 = 0;
    result = KeQueryPerformanceCounter(a1, a2, 1, a4);
    v_stack_m1E8 = 0;
    if ((unsigned __int8)(*(unsigned __int8 *)(a1 + 172)) != 0) {
        a2 = (result) << ((unsigned __int8)(*(unsigned __int8 *)(a1 + 172)));
    }
    v_stack_m1E8 = a2;
    v_r10 = (a2) - (*(unsigned __int64 *)(v_stack_m258));
    v_r11 = (result) - (*(unsigned __int64 *)(v_stack_m250));
    if ((*(unsigned __int8 *)(v_rip + 14337064)) != 0) goto loc_0021A8C2;
loc_0021A676:
    a1 = (*(unsigned __int64 *)(a1 + 34560)) + (v_r11);
    *(unsigned __int64 *)(a1 + 34560) = a1;
    a1 = (*(unsigned __int64 *)(a1 + 34680)) + (v_r10);
    *(unsigned __int64 *)(a1 + 34680) = a1;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 8) + 2)) & (32)) == 0) goto loc_0021A728;
    if (*(unsigned __int64 *)(a1 + 35248) == 0) goto loc_0021B0CB;
    if (*(unsigned __int64 *)(a1 + 35256) == 0) goto loc_0021B0CB;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 35256) + 112)) != 0) goto loc_0021A6DC;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 35256) + 80)))) < ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 35248) + 528))))) goto loc_0021A6E3;
    goto loc_0021A6E3;
loc_0021A6DC:
loc_0021A6E3:
loc_0021A6ED:
    if (((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 35248) + 528)))) + 132)))) <= ((unsigned int)(*(unsigned __int16 *)(a1 + 35434)))) goto loc_0021A700;
    a2 = (unsigned int)((0) + 1);
    a1 = (a1 + 35434) + (2);
    if (a2 < 3) goto loc_0021A6ED;
loc_0021A700:
    result = ((*(unsigned __int8 *)(a1 + 35336)) != 0) ? 1 : 0;
    a1 = (*(unsigned __int64 *)(a1 + result + (unsigned int)(a2) * 2 + 4336 * 8)) + (v_r10);
    *(unsigned __int64 *)(a1 + result + (unsigned int)(a2) * 2 + 4336 * 8) = a1;
loc_0021A728:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 8) + 2)) & (64)) == 0) goto loc_0021A73E;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 968) != 0) {
        *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 968) + 64) = 1;
    }
    *(unsigned __int64 *)(v_stack_m250) = result;
    *(unsigned __int64 *)(v_stack_m258) = a2;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 8) + 2)) & (2)) == 0) goto loc_0021A78E;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 360) + 32) == 0) goto loc_0021A78E;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12894632))) == 0) goto loc_0021A78E;
loc_0021A774:
    if (((1) & (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 360) + 32))) != 0) goto loc_0021B0D6;
loc_0021A77D:
    a3 = (1) + (1);
    v_r11 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 360) + 48) + (24);
    v_r10 = (v_rip + 13592338) + (4);
    v_rdi = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12894632))))) - (1);
    if (condition_is_not_equal) goto loc_0021A774;
loc_0021A78E:
    *(unsigned __int8 *)(a1 + 32) = 0;
    if ((*(unsigned __int8 *)(a1 + 6)) != 0) goto loc_0021AF87;
loc_0021A79D:
    if (1 == 1) goto loc_0021A834;
    goto loc_0021A135;
loc_0021A7BE:
loc_0021A7C2:
    *(unsigned __int8 *)(v_stack_m1D8 + 32) = 0;
    if ((*(unsigned __int8 *)(v_stack_m1D8 + 6)) != 0) goto loc_0021AFC0;
loc_0021A7D1:
    v_stack_m240 = 0;
    a1 = (unsigned __int16)(((unsigned __int16)(*(unsigned __int16 *)(v_stack_m1D8 + 14524))) | ((unsigned __int16)(v_rdi)));
    a1 = (unsigned __int16)((a1) & (0xFFFEULL));
    a1 = (unsigned __int16)((a1) | (128));
    if (condition_is_equal) goto loc_0021A834;
loc_0021A803:
    result = RtlBackoff(v_stack_m240, a1 + result + (unsigned int)(a2) * 2 + 4336 * 8, a3, 128);
    a1 = (unsigned __int16)(((unsigned __int16)(*(unsigned __int16 *)(v_stack_m1D8 + 14524))) | ((unsigned __int16)(v_rdi)));
    a1 = (unsigned __int16)((a1) & (0xFFFEULL));
    a1 = (unsigned __int16)((a1) | (128));
    if (condition_is_not_equal) goto loc_0021A803;
loc_0021A834:
    *(unsigned __int64 *)(v_stack_m1D8 + 14432) = 0;
    a1 = (v_stack_m38) ^ (v_rsp);
    result = _security_check_cookie(a1, a1 + result + (unsigned int)(a2) * 2 + 4336 * 8, a3, 128);
    return result;
loc_0021A86C:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 104) == 0) goto loc_0021A88D;
    result = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 216))) + (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 104));
loc_0021A87E:
    if (*(unsigned __int64 *)(result + 416) != 0) goto loc_0021A87E;
loc_0021A88D:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 2)) & (8)) == 0) goto loc_0021A8A7;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 544)) != (v_rip + 14374502)) goto loc_0021B072;
loc_0021A8A7:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 360)) == 0) goto loc_0021A4AB;
    result = KiEndCounterAccumulation(*(unsigned __int64 *)(v_stack_m28 + 64), a1 + result + (unsigned int)(a2) * 2 + 4336 * 8, a3, 128);
    goto loc_0021A4AB;
loc_0021A8C2:
    if ((*(unsigned __int64 *)(result)) == 0) goto loc_0021A676;
    v_stack_m1E8 = 0;
    v_stack_m208 = 0;
    if ((unsigned __int8)(result) == 0) goto loc_0021AFF1;
    a3 = (a3) << ((unsigned __int8)((unsigned __int8)(result)));
    a3 = (*(unsigned __int64 *)(v_stack_m28 + 72)) << ((unsigned __int8)((unsigned __int8)(result)));
loc_0021A90E:
    v_stack_m1E8 = a1 + result + (unsigned int)(a2) * 2 + 4336 * 8;
    v_stack_m208 = a1 + result + (unsigned int)(a2) * 2 + 4336 * 8;
    a4 = (a1 + result + (unsigned int)(a2) * 2 + 4336 * 8) >> ((unsigned __int8)((__int8)(*(unsigned __int8 *)(v_rip + 14336689))));
    a2 = (a1 + result + (unsigned int)(a2) * 2 + 4336 * 8) >> ((unsigned __int8)((__int8)(*(unsigned __int8 *)(v_rip + 14336689))));
    a2 = (unsigned int)((a2) - ((unsigned int)(a4)));
    if (condition_is_equal) goto loc_0021A676;
    goto loc_0021A676;
loc_0021A96B:
    a2 = ((unsigned int)((unsigned int)(a1 + result + (unsigned int)(a2) * 2 + 4336 * 8))) + ((unsigned int)((unsigned int)(a1 + result + (unsigned int)(a2) * 2 + 4336 * 8)));
    a1 = (*(unsigned __int64 *)(v_stack_m230 + a2 * 8 + 8)) + (0);
    *(unsigned __int64 *)(v_stack_m230 + a2 * 8 + 8) = a1;
    goto loc_0021A404;
loc_0021A983:
    v_r12 = 0;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 34524)) == 0) goto loc_0021A9EF;
    a1 = 0;
    result = KeQueryPerformanceCounter(a1, a2, a1 + result + (unsigned int)(a2) * 2 + 4336 * 8, v_stack_m230);
    v_stack_m1E0 = 0;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 172)) != 0) {
        a2 = (result) << ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 172)));
    }
    v_stack_m1E0 = a2;
    v_r11 = (a2) - (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 34432));
    v_r14 = (result) - (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 34552));
    if ((*(unsigned __int8 *)(v_rip + 14336172)) != 0) goto loc_0021AB0F;
loc_0021A9EF:
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 34560)) + (v_r14);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 34560) = a1;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 34680)) + (v_r11);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 34680) = a1;
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 176);
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 2)) & (32)) != 0) {
        a1 = *(unsigned __int64 *)(v_stack_m28 + 56);
        result = PoGetFrequencyBucket(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 34552), a1 + result + (unsigned int)(a2) * 2 + 4336 * 8, v_stack_m230);
        a1 = 0;
        result = (unsigned int)(result);
        a1 = ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 35336)) != 0) ? 1 : 0;
        a1 = a1 + result * 2;
        a1 = a1 + 4336;
        a2 = *(unsigned __int64 *)(v_stack_m28 + 56) + a1 * 8;
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + a1 * 8);
        a1 = (a1) + (v_r11);
        *(unsigned __int64 *)(a2) = a1;
    }
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 2)) & (64)) == 0) goto loc_0021AA5D;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 968) != 0) {
        *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 968) + 64) = 1;
    }
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 34552) = result;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 34432) = a2;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 2)) & (2)) == 0) goto loc_0021A7C2;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 360) + 32) == 0) goto loc_0021A7C2;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12893817))) == 0) goto loc_0021A7C2;
loc_0021AAA5:
    if (((1) & (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 360) + 32))) != 0) goto loc_0021B0EA;
loc_0021AAAE:
    v_r13 = (1) + (1);
    a3 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 360) + 48) + (24);
    v_rbx = (v_rip + 13591515) + (4);
    a4 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12893817))))) - (1);
    if (condition_is_not_equal) goto loc_0021AAA5;
    goto loc_0021A7BE;
loc_0021AAC4:
    a1 = (*(unsigned __int64 *)(v_rbx + *(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 124) * 8 + 34440 * 1)) + (0);
    *(unsigned __int64 *)(v_rbx + *(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 124) * 8 + 34440 * 1) = a1;
    v_rdi = (unsigned __int8)((*(unsigned __int64 *)(v_stack_m28 + 72)) & (239));
    goto loc_0021A30E;
loc_0021AAE4:
    v_r10 = 0;
    goto loc_0021A268;
loc_0021AAF6:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 968) == 0) goto loc_0021A469;
    *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 968) + 64) = 0;
    goto loc_0021A469;
loc_0021AB0F:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 968))) == 0) goto loc_0021A9EF;
    v_stack_m210 = 0;
    if ((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 968)) == 0) goto loc_0021B01B;
    a2 = (*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 124) * 8 + 34440) << ((unsigned __int8)((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 968))));
    result = 0;
    a3 = (0) << ((unsigned __int8)((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 968))));
loc_0021AB59:
    v_stack_m200 = 0;
    v_stack_m210 = a2;
    v_stack_m200 = a2;
    a4 = (a2) >> ((unsigned __int8)((__int8)(*(unsigned __int8 *)(v_rip + 14336102))));
    a2 = (a2) >> ((unsigned __int8)((__int8)(*(unsigned __int8 *)(v_rip + 14336102))));
    a2 = (unsigned int)((a2) - ((unsigned int)(a4)));
    if (condition_is_not_equal) goto loc_0021AE29;
loc_0021AB9F:
    v_r12 = 0;
    goto loc_0021A9EF;
loc_0021ABA7:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(v_r13), (unsigned __int8)(*(unsigned __int64 *)(v_rip + 14337934)), a2, a4);
    goto loc_0021A557;
loc_0021ABB8:
    if (((unsigned __int8)((unsigned __int8)(v_r13))) != 2) goto loc_0021AF58;
    *(unsigned __int8 *)(result + 17) = 5;
    result = KiInsertQueueInternal(*(unsigned __int64 *)(result + 24), result, a2, a4);
    if (((unsigned __int8)((unsigned __int8)(v_r13))) == 2) goto loc_0021A5E1;
    a3 = 0;
    goto loc_0021A586;
loc_0021ABE3:
    if (((*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 116)) & (0x400ULL)) != 0) goto loc_0021AC09;
    result = (v_rdi) >> (4);
    result = (unsigned int)((result) & (31));
    if (((unsigned int)(result)) < ((unsigned int)(result))) goto loc_0021ADDF;
loc_0021AC09:
loc_0021AC17:
    v_stack_m228 = *(unsigned __int64 *)(result + 24);
    v_stack_m230 = v_r11;
    if ((*(unsigned __int64 *)(v_stack_m28 + 64)) == (*(unsigned __int64 *)(v_rbx + 24))) goto loc_0021A25A;
    v_stack_m230 = v_r11;
    v_stack_m228 = 0;
    result = KiQueryEffectivePriorityThread(*(unsigned __int64 *)(v_stack_m28 + 64), v_rbx, a3, a4);
    if (((unsigned int)(result)) >= 8) goto loc_0021AAE4;
    v_r10 = 0;
    v_stack_m230 = v_stack_m210;
    v_stack_m228 = v_stack_m218;
    goto loc_0021A268;
loc_0021AC7A:
    v_rdi = (unsigned __int16)((v_rdi) & ((unsigned __int16)((unsigned int)(0xFFF7ULL))));
    result = KiSelectActiveTimerTable(v_rbx, 1, a3, a4);
    if (result == 0) goto loc_0021AEF5;
    v_r12 = ((*(unsigned __int64 *)(v_rip + 12893166)) != (*(unsigned __int64 *)(result + 16896))) ? 1 : 0;
    result = ((*(unsigned __int64 *)(v_rip + 12893181)) != (*(unsigned __int64 *)(result + 16904))) ? 1 : 0;
    v_r14 = (unsigned __int8)(result);
    if ((*(unsigned int *)(v_rip + 14335852)) != 0) { v_r14 = (unsigned int)((unsigned __int8)(v_r12)); }
    result = (unsigned __int8)(v_r12);
    if ((*(unsigned __int64 *)(v_rip + 12893166)) != (*(unsigned __int64 *)(result + 16896))) {
        result = *(unsigned __int64 *)(result);
        *(unsigned __int64 *)(result + 16896) = *(unsigned __int64 *)(v_rip + 12893166);
        result = (result) >> (18);
        *(unsigned int *)(result + 16912) = (unsigned int)(result);
    }
    if ((unsigned __int8)(v_r14) != 0) goto loc_0021AE3A;
loc_0021AD0A:
    if ((*(unsigned __int64 *)(v_rip + 12893166)) == (*(unsigned __int64 *)(result + 16896))) goto loc_0021AE94;
loc_0021AD13:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536) != 0) goto loc_0021AECD;
loc_0021AD2C:
    v_stack_m1C0 = *(unsigned __int64 *)(result);
    v_stack_m240 = v_stack_m1C8;
    result = KiTimerExpiration(v_rbx, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + 16912)))), *(unsigned __int64 *)(result), (unsigned __int8)(v_r14));
loc_0021AD59:
    if ((*(unsigned __int8 *)(v_rbx + 33)) != 0) {
        result = v_stack_m1C8;
        a4 = (unsigned __int8)(v_r14);
        a3 = (unsigned __int8)(v_r12);
        v_stack_m240 = result;
        a2 = *(unsigned __int64 *)(result);
        a1 = v_rbx;
        result = KiTimer2Expiration(a1, a2, a3, a4);
    }
    goto loc_0021A4C7;
loc_0021AD90:
    v_r14 = (unsigned int)((v_r14) + 1);
    if (((*(unsigned int *)(v_rip + 14329106)) & ((unsigned int)(v_r14))) == 0) goto loc_0021AF26;
loc_0021ADA0:
loc_0021ADA2:
    if (sign_flag) goto loc_0021AD90;
    if (condition_is_below) goto loc_0021AD90;
    a3 = 0;
    goto loc_0021A571;
loc_0021ADB7:
loc_0021ADBE:
    if (condition_is_not_equal) goto loc_0021ADBE;
    if (condition_is_above_or_equal) goto loc_0021A4EE;
    result = KiRemoveSystemWorkPriorityKick(a1, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a3)))), a3, a4);
    goto loc_0021A4EE;
loc_0021ADDF:
    goto loc_0021AC17;
loc_0021ADF2:
loc_0021ADF9:
    if (condition_is_not_equal) goto loc_0021ADF9;
    if (condition_is_above_or_equal) goto loc_0021A535;
    result = KiRemoveSystemWorkPriorityKick(a1, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a3)))), a3, a4);
    goto loc_0021A535;
loc_0021AE1A:
    goto loc_0021A676;
loc_0021AE29:
    goto loc_0021AB9F;
loc_0021AE3A:
    *(unsigned __int64 *)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a3)))) + 16904) = *(unsigned __int64 *)(v_rip + 12893181);
    v_r13 = 1;
    if (1 >= ((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a3)))) + 16916))))) { v_r13 = (unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a3)))) + 16916))); }
    result = (*(unsigned __int64 *)(result)) >> (18);
    *(unsigned int *)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a3)))) + 16916) = (unsigned int)(result);
    goto loc_0021AD0A;
loc_0021AE60:
    v_stack_m208 = (unsigned int)(result);
    a2 = (unsigned int)(((unsigned int)((unsigned int)(result))) - ((unsigned int)(a1)));
    if (a2 >= 32) goto loc_0021AF7D;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m230 + 196))) << ((unsigned __int8)((unsigned int)(a2))));
    result = (unsigned int)((result) | (1));
    v_stack_m204 = (unsigned int)(result);
loc_0021AE83:
    *(unsigned __int64 *)(v_stack_m230 + 192) = v_stack_m208;
    goto loc_0021A3DD;
loc_0021AE94:
    if ((unsigned __int8)(v_stack_m228) != 0) goto loc_0021AD13;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536) != 0) goto loc_0021AF90;
loc_0021AEB6:
    v_stack_m1C0 = *(unsigned __int64 *)(v_stack_m208);
    goto loc_0021AD59;
loc_0021AECD:
loc_0021AED4:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536) != 0) goto loc_0021AED4;
    if (condition_is_above_or_equal) goto loc_0021AD2C;
    result = KiRemoveSystemWorkPriorityKick(*(unsigned __int64 *)(gs_base + (0 + 32)), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536))))), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), v_stack_m230);
    goto loc_0021AD2C;
loc_0021AEF5:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536) != 0) goto loc_0021AFC9;
loc_0021AF0E:
    v_stack_m1C0 = *(unsigned __int64 *)(result);
    goto loc_0021A4C7;
loc_0021AF26:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14334860)))) & (64)) == 0) goto loc_0021ADA0;
    result = KiCheckVpBackingLongSpinWaitHypercall(*(unsigned __int64 *)(gs_base + (0 + 32)), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536))))), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), v_stack_m230);
    if ((unsigned __int8)(result) == 0) goto loc_0021ADA0;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_stack_m228)), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536))))), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), v_stack_m230);
    goto loc_0021ADA2;
loc_0021AF4E:
    goto loc_0021A25D;
loc_0021AF58:
    if (((unsigned __int8)(v_stack_m228)) == 4) goto loc_0021AFFC;
    a4 = 0;
    result = KiTryUnwaitThread(v_r12, result, 256, a4);
    a3 = 0;
    goto loc_0021A586;
loc_0021AF7D:
    v_stack_m204 = (unsigned int)(v_r13);
    goto loc_0021AE83;
loc_0021AF87:
    *(unsigned __int8 *)(v_rbx + 6) = (unsigned __int8)(v_r12);
    goto loc_0021A79D;
loc_0021AF90:
loc_0021AF97:
    if (condition_is_not_equal) goto loc_0021AF97;
    if (condition_is_above_or_equal) goto loc_0021AEB6;
    result = KiRemoveSystemWorkPriorityKick(v_r12, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a3)))), a3, a4);
    goto loc_0021AEB6;
loc_0021AFB8:
    goto loc_0021A1FF;
loc_0021AFC0:
    *(unsigned __int8 *)(v_rbx + 6) = 0;
    goto loc_0021A7D1;
loc_0021AFC9:
loc_0021AFD0:
    if (condition_is_not_equal) goto loc_0021AFD0;
    if (condition_is_above_or_equal) goto loc_0021AF0E;
    result = KiRemoveSystemWorkPriorityKick(v_r12, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a3)))), a3, a4);
    goto loc_0021AF0E;
loc_0021AFF1:
    goto loc_0021A90E;
loc_0021AFFC:
    *(unsigned __int8 *)(result + 17) = 5;
    *(unsigned int *)(v_rdi + 4) = (unsigned int)(v_rdi);
    result = KeInsertQueueDpc(*(unsigned __int64 *)(result + 24), v_rdi, result, a4);
    a3 = 0;
    goto loc_0021A586;
loc_0021B01B:
    result = 0;
    goto loc_0021AB59;
loc_0021B025:
    if (((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 516))) >= 7) goto loc_0021A4A1;
    a2 = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 80));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 80)))) <= ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 84))))) { a2 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 84))); }
    a1 = 0;
    a1 = (a2 >= (*(unsigned int *)(v_rip + 14328618))) ? 1 : 0;
    a1 = (unsigned int)((a1 + (unsigned int)((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 516))) * 2) * (*(unsigned int *)(v_rip + 14328704)));
    a1 = (unsigned int)((a1) + ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 517))));
    goto loc_0021A4A1;
loc_0021B072:
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 576) + *(unsigned __int16 *)(*(unsigned __int64 *)(v_rbx + 192) + 136) * 8 + 8)) & (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 192) + 128));
    if (a2 == (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 192) + 128))) goto loc_0021A8A7;
    goto loc_0021A8A7;
loc_0021B0AC:
    v_stack_m230 = 72;
    v_stack_m228 = *(unsigned __int64 *)(result);
    goto loc_0021A25D;
loc_0021B0C1:
    goto loc_0021A365;
loc_0021B0CB:
    goto loc_0021A6E3;
loc_0021B0D6:
    a2 = (100) << (32);
    result = (72) | (a2);
    *(unsigned __int64 *)(72) = result;
    goto loc_0021A77D;
loc_0021B0EA:
    a2 = (a2) << (32);
    result = (result) | (a2);
    *(unsigned __int64 *)(100) = result;
    goto loc_0021AAAE;
}
```

## 5. (Beta) C Style

```c
int64_t KiRetireDpcList(void *Arg1, int32_t Arg2)
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
    int64_t local_rsp;
    uint64_t v_stack_m188;
    uint64_t v_stack_m1C0;
    uint64_t v_stack_m1C4;
    uint32_t v_stack_m1C8;
    uint64_t v_stack_m1D8;
    uint64_t v_stack_m1E0;
    uint64_t v_stack_m1E8;
    uint64_t v_stack_m1F0;
    uint64_t v_stack_m200;
    uint32_t v_stack_m204;
    uint64_t v_stack_m208;
    uint64_t v_stack_m210;
    uint64_t v_stack_m218;
    uint64_t v_stack_m220;
    uint32_t v_stack_m228;
    uint64_t v_stack_m230;
    uint64_t v_stack_m238;
    uint64_t v_stack_m240;
    uint64_t v_stack_m250;
    uint64_t v_stack_m258;
    uint8_t v_stack_m268;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;

    v_stack_p10 = local_rbx;
    v_stack_p18 = local_rsi;
    v_stack_p20 = local_rdi;
    local_rsp = (local_rsp) - (608);
    result = (*(uint64_t *)(v_rip + 0xBF0662)) ^ (local_rsp);
    v_stack_m38 = result;
    v_stack_m1D8 = Arg1;
    Arg2 = 0;
    result = memset(v_stack_m1C4, Arg2, 396, a4);
    local_r12 = 0;
    v_stack_m250 = Arg1 + 34552;
    v_stack_m1C8 = 0;
    v_stack_m240 = Arg1 + 34552;
    v_stack_m258 = Arg1 + 34432;
    v_stack_m238 = Arg1 + 34432;
loc_0021A135:
    *(uint8_t *)(arg1 + 0x20) = 1;
    if ((*(uint8_t *)(arg1 + 0x86DC)) == 0) goto loc_0021AAE4;
    Arg1 = 0;
    result = KeQueryPerformanceCounter(Arg1, (uint32_t)(0xFFFFFFFFULL), 396, a4);
    local_r10 = 0;
    v_stack_m1F0 = 0;
    if ((uint8_t)(*(uint8_t *)(arg1 + 0xAC)) != 0) {
        Arg2 = (result) << ((uint8_t)(*(uint8_t *)(arg1 + 0xAC)));
    }
    v_stack_m1F0 = Arg2;
    local_r12 = (Arg2) - (*(uint64_t *)(v_stack_m238));
    v_stack_m258 = v_stack_m238;
    if ((*(uint8_t *)(v_rip + 0xDAC8F5)) == 0) goto loc_0021AF4E;
    if ((*(uint64_t *)(v_stack_m238)) == 0) goto loc_0021B0AC;
    v_stack_m220 = 0;
    v_stack_m218 = 0;
    if ((uint8_t)(v_stack_m238) == 0) goto loc_0021AFB8;
    Arg2 = (*(uint64_t *)(arg1 + 0x86F8)) << ((uint8_t)((uint8_t)(v_stack_m238)));
    a3 = (result) << ((uint8_t)((uint8_t)(v_stack_m238)));
loc_0021A1FF:
    v_stack_m220 = Arg2;
    v_stack_m218 = Arg2;
    local_r10 = (Arg2) >> ((uint8_t)((int8_t)(*(uint8_t *)(v_rip + 0xDAC9C0))));
    v_stack_m258 = v_stack_m238;
    local_r15 = (Arg2) >> ((uint8_t)((int8_t)(*(uint8_t *)(v_rip + 0xDAC9C0))));
    v_stack_m250 = v_stack_m240;
    local_r15 = (uint32_t)((local_r15) - ((uint32_t)(local_r10)));
    if (condition_is_not_equal) goto loc_0021ABE3;
loc_0021A25A:
    local_r10 = 0;
loc_0021A25D:
loc_0021A268:
    *(uint64_t *)(v_stack_m240) = result;
    *(uint64_t *)(v_stack_m238) = Arg2;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x48)) + (local_r12);
    *(void **)(*(uint64_t *)(arg1 + 0x8) + 0x48) = Arg1;
    result = v_stack_m238;
    if ((*(uint64_t *)(arg1 + 0x8)) != (*(uint64_t *)(arg1 + 0x18))) {
        result = *(uint32_t *)(arg1 + 0x86B8);
        Arg1 = *(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x50);
        result = (result) * (local_r12);
        result = (result) >> (16);
        Arg1 = (Arg1) + (result);
        if (Arg1 > ((uint32_t)(0xFFFFFFFFULL))) { Arg1 = (uint32_t)(0xFFFFFFFFULL); }
        *(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x50) = (uint32_t)(Arg1);
    }
    if ((((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x8) + 0x2))) & (190)) == 0) goto loc_0021A4AB;
    local_rdi = *(uint8_t *)(*(uint64_t *)(arg1 + 0x8) + 0x2);
    if (sign_flag) {
        result = *(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x220);
        Arg2 = (uint32_t)(local_r12 + 1);
        a3 = *(uint64_t *)(arg1 + 0x8BB0);
        a4 = *(uint32_t *)(result + 0x190);
        result = (uint32_t)(a4);
        result = (uint32_t)((result) >> (13));
        result = (uint32_t)((result) & (0x3FFFFULL));
        a4 = (a4) >> (4);
        a4 = (uint32_t)((a4) & (511));
        Arg2 = (uint32_t)((Arg2) << ((uint8_t)(Arg1)));
        Arg1 = (uint32_t)((Arg1) + (-2));
        Arg2 = (uint32_t)((Arg2) ^ ((uint32_t)(result)));
        v_stack_m228 = (uint32_t)(Arg1);
        Arg1 = *(uint64_t *)(a3 + arg1 * 8);
        Arg2 = *(uint64_t *)(arg1 + Arg2 * 8 + 0x8);
        result = *(uint64_t *)(Arg2 + a4 * 8);
        result = (result) + (local_r12);
        *(uint64_t *)(Arg2 + a4 * 8) = result;
        local_rdi = (uint8_t)((*(uint8_t *)(*(uint64_t *)(arg1 + 0x8) + 0x2)) & (127));
    }
    if ((((uint8_t)(local_rdi)) & (16)) != 0) goto loc_0021AAC4;
loc_0021A30E:
    if ((((uint8_t)(local_rdi)) & (32)) == 0) goto loc_0021A45F;
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x688) == 0) goto loc_0021A45B;
    if (*(uint64_t *)(arg1 + 0x89B0) == 0) goto loc_0021B0C1;
    if (*(uint64_t *)(arg1 + 0x89B8) == 0) goto loc_0021B0C1;
    if ((*(uint8_t *)(*(uint64_t *)(arg1 + 0x89B8) + 0x70)) != 0) goto loc_0021A35F;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x89B8) + 0x50)))) < ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x89B0) + 0x210))))) goto loc_0021A365;
    goto loc_0021A365;
loc_0021A35F:
loc_0021A365:
loc_0021A36F:
    if (((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x89B0) + 0x210)))) + 0x84)))) <= ((uint32_t)(*(uint16_t *)(arg1 + 0x8A6A)))) goto loc_0021A383;
    a3 = (uint32_t)((0) + 1);
    Arg1 = (Arg1 + 35434) + (2);
    if (((uint32_t)(a3)) < 3) goto loc_0021A36F;
loc_0021A383:
    result = (uint8_t)(-((uint8_t)(*(uint8_t *)(arg1 + 0x8A08))));
    v_stack_m230 = 0;
    Arg2 = ((uint32_t)((uint32_t)(a3))) + ((uint32_t)((uint32_t)(a3)));
    Arg1 = (uint32_t)((Arg1) & (8));
    Arg1 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x688) + arg1 * 1 + Arg2 * 8)) + (local_r12);
    *(void **)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x688) + arg1 * 1 + Arg2 * 8) = Arg1;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCF6689)))) > ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x688) + 0xC0))))) goto loc_0021AE60;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x688) + 0xC0))) - ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCF6689)))));
    result = (uint32_t)(*(uint32_t *)(v_rip + 0xCF6689));
    if (((uint32_t)(Arg1)) < 32) {
        result = (uint32_t)(local_r12 + 1);
        result = (uint32_t)((result) << ((uint8_t)(Arg1)));
    }
    if ((*(uint32_t *)(v_rip + 0xDAC97C)) != 0) goto loc_0021A404;
    if ((((uint32_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x8) + 0x204) - 2)) & (0xFFFFFFFBULL)) == 0) goto loc_0021A96B;
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x8) + 0x204))) == 5) goto loc_0021A96B;
loc_0021A404:
    result = *(uint8_t *)(*(uint64_t *)(arg1 + 0x8) + 0x204) - 2;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x650)) != 0) {
        result = (uint8_t)(*(uint8_t *)(arg1 + 0x8A08));
        Arg1 = (uint32_t)(a3);
        Arg1 = (Arg1) + (8);
        Arg1 = (Arg1) + (Arg1);
        result = (uint8_t)(-(result));
        Arg2 = (uint32_t)((Arg2) & (8));
        result = *(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x688) + Arg1 * 8;
        Arg1 = *(uint64_t *)(Arg2 + result * 1);
        Arg1 = (Arg1) + (local_r12);
        *(void **)(Arg2 + result * 1) = Arg1;
        result = *(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x650);
        Arg2 = (uint32_t)(a3);
        Arg1 = *(uint64_t *)(result + 0x688);
        result = 64;
        if ((uint8_t)(*(uint8_t *)(arg1 + 0x8A08)) != 0) { result = 72; }
        Arg2 = (Arg2) + (Arg2);
        result = (result) + (Arg1);
    }
    local_rdi = (uint8_t)((local_rdi) & (223));
loc_0021A45F:
    if ((((uint8_t)(local_rdi)) & (64)) != 0) goto loc_0021AAF6;
loc_0021A469:
    if ((*(uint8_t *)(v_rip + 0xDAC66E)) != 0) {
        a4 = 0;
        a3 = local_r12;
        Arg2 = *(uint64_t *)(arg1 + 0x8);
        Arg1 = Arg1;
        result = KiUpdateThreadHgsFeedback(Arg1, Arg2, a3, a4);
    }
    if ((*(uint64_t *)(arg1 + 0x86B0)) == 0) goto loc_0021A4A1;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x220)) != (v_rip + 14375532)) goto loc_0021B025;
loc_0021A4A1:
    if ((((uint8_t)(local_rdi)) & (190)) != 0) goto loc_0021A86C;
loc_0021A4AB:
    result = KiRcuCheckQuiescent(Arg1, Arg2, a3, a4);
    if ((((uint8_t)((uint32_t)((uint32_t)(local_r12 + 1)))) & (8)) != 0) goto loc_0021AC7A;
loc_0021A4C7:
    if ((((uint8_t)((uint32_t)((uint32_t)(local_r12 + 1)))) & (64)) == 0) goto loc_0021A4F8;
    local_rdi = (uint16_t)(((uint32_t)((uint32_t)(local_r12 + 1))) & ((uint16_t)((uint32_t)(0xFFBFULL))));
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8) != 0) goto loc_0021ADB7;
loc_0021A4EE:
    result = KiNormalPriorityReadyScan(Arg1, Arg2, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), a4);
loc_0021A4F8:
    a4 = 0;
    result = KiExecuteAllDpcs(Arg1, *(uint64_t *)(arg1 + 0x8), v_stack_m1C8, a4);
    if ((uint8_t)(result) == 0) goto loc_0021A983;
    if ((((uint8_t)(local_rdi)) & (4)) == 0) goto loc_0021A604;
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8) != 0) goto loc_0021ADF2;
loc_0021A535:
    if ((*(uint32_t *)(v_rip + 0xDAC7CF)) != 0) goto loc_0021ABA7;
loc_0021A557:
    a3 = 0;
    if (condition_is_below) goto loc_0021AD90;
loc_0021A571:
    if ((*(uint32_t *)(arg1 + 0x8340 + 0x4)) != 0) goto loc_0021A5E1;
    *(uint32_t *)(arg1 + 0x8340 + 0x4) = 1;
loc_0021A586:
    if ((*(uint64_t *)(arg1 + 0x8340 + 0x8)) == (Arg1 + 33600 + 8)) goto loc_0021A5E1;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8340 + 0x8)) + 0x8)) != (*(uint64_t *)(arg1 + 0x8340 + 0x8))) goto loc_0021A5A3;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8340 + 0x8) + 0x8))) != (*(uint64_t *)(arg1 + 0x8340 + 0x8))) {
        Arg1 = 3;
    }
    *(void **)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8340 + 0x8) + 0x8)) = Arg1;
    *(uint64_t *)(arg1 + 0x8) = *(uint64_t *)(*(uint64_t *)(arg1 + 0x8340 + 0x8) + 0x8);
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x8340 + 0x8) + 0x10))) != 1) goto loc_0021ABB8;
    a4 = 0;
    result = KiTryUnwaitThread(*(uint64_t *)(gs_base + (0 + 0x20)), *(uint64_t *)(arg1 + 0x8340 + 0x8), *(uint16_t *)(*(uint64_t *)(arg1 + 0x8340 + 0x8) + 0x12), a4);
    if ((uint8_t)(result) == 0) goto loc_0021A586;
    if ((uint8_t)(result) != 0) goto loc_0021A586;
loc_0021A5E1:
    v_stack_m268 = (uint8_t)(v_cr8);
    a4 = 0;
    Arg2 = 0;
    result = KiExitDispatcher(*(uint64_t *)(gs_base + (0 + 0x20)), Arg2, 1, a4);
loc_0021A604:
    local_r12 = 0;
    if ((*(uint8_t *)(arg1 + 0x86DC)) == 0) goto loc_0021AE1A;
    Arg1 = 0;
    result = KeQueryPerformanceCounter(Arg1, Arg2, 1, a4);
    v_stack_m1E8 = 0;
    if ((uint8_t)(*(uint8_t *)(arg1 + 0xAC)) != 0) {
        Arg2 = (result) << ((uint8_t)(*(uint8_t *)(arg1 + 0xAC)));
    }
    v_stack_m1E8 = Arg2;
    local_r10 = (Arg2) - (*(uint64_t *)(v_stack_m258));
    local_r11 = (result) - (*(uint64_t *)(v_stack_m250));
    if ((*(uint8_t *)(v_rip + 0xDAC428)) != 0) goto loc_0021A8C2;
loc_0021A676:
    Arg1 = (*(uint64_t *)(arg1 + 0x8700)) + (local_r11);
    *(void **)(arg1 + 0x8700) = Arg1;
    Arg1 = (*(uint64_t *)(arg1 + 0x8778)) + (local_r10);
    *(void **)(arg1 + 0x8778) = Arg1;
    if (((*(uint8_t *)(*(uint64_t *)(arg1 + 0x8) + 0x2)) & (32)) == 0) goto loc_0021A728;
    if (*(uint64_t *)(arg1 + 0x89B0) == 0) goto loc_0021B0CB;
    if (*(uint64_t *)(arg1 + 0x89B8) == 0) goto loc_0021B0CB;
    if ((*(uint8_t *)(*(uint64_t *)(arg1 + 0x89B8) + 0x70)) != 0) goto loc_0021A6DC;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x89B8) + 0x50)))) < ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x89B0) + 0x210))))) goto loc_0021A6E3;
    goto loc_0021A6E3;
loc_0021A6DC:
loc_0021A6E3:
loc_0021A6ED:
    if (((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x89B0) + 0x210)))) + 0x84)))) <= ((uint32_t)(*(uint16_t *)(arg1 + 0x8A6A)))) goto loc_0021A700;
    Arg2 = (uint32_t)((0) + 1);
    Arg1 = (Arg1 + 35434) + (2);
    if (Arg2 < 3) goto loc_0021A6ED;
loc_0021A700:
    result = ((*(uint8_t *)(arg1 + 0x8A08)) != 0) ? 1 : 0;
    Arg1 = (*(uint64_t *)(arg1 + result + (uint32_t)(Arg2) * 2 + 0x10F0 * 8)) + (local_r10);
    *(void **)(arg1 + result + (uint32_t)(Arg2) * 2 + 0x10F0 * 8) = Arg1;
loc_0021A728:
    if (((*(uint8_t *)(*(uint64_t *)(arg1 + 0x8) + 0x2)) & (64)) == 0) goto loc_0021A73E;
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x3C8) != 0) {
        *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x3C8) + 0x40) = 1;
    }
    *(uint64_t *)(v_stack_m250) = result;
    *(uint64_t *)(v_stack_m258) = Arg2;
    if (((*(uint8_t *)(*(uint64_t *)(arg1 + 0x8) + 0x2)) & (2)) == 0) goto loc_0021A78E;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x168) + 0x20) == 0) goto loc_0021A78E;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC4C1A8))) == 0) goto loc_0021A78E;
loc_0021A774:
    if (((1) & (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x168) + 0x20))) != 0) goto loc_0021B0D6;
loc_0021A77D:
    a3 = (1) + (1);
    local_r11 = (*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x168) + 48) + (24);
    local_r10 = (v_rip + 13592338) + (4);
    local_rdi = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC4C1A8))))) - (1);
    if (condition_is_not_equal) goto loc_0021A774;
loc_0021A78E:
    *(uint8_t *)(arg1 + 0x20) = 0;
    if ((*(uint8_t *)(arg1 + 0x6)) != 0) goto loc_0021AF87;
loc_0021A79D:
    if (1 == 1) goto loc_0021A834;
    goto loc_0021A135;
loc_0021A7BE:
loc_0021A7C2:
    *(uint8_t *)(v_stack_m1D8 + 0x20) = 0;
    if ((*(uint8_t *)(v_stack_m1D8 + 0x6)) != 0) goto loc_0021AFC0;
loc_0021A7D1:
    v_stack_m240 = 0;
    Arg1 = (uint16_t)(((uint16_t)(*(uint16_t *)(v_stack_m1D8 + 0x38BC))) | ((uint16_t)(local_rdi)));
    Arg1 = (uint16_t)((Arg1) & (0xFFFEULL));
    Arg1 = (uint16_t)((Arg1) | (128));
    if (condition_is_equal) goto loc_0021A834;
loc_0021A803:
    result = RtlBackoff(v_stack_m240, Arg1 + result + (uint32_t)(Arg2) * 2 + 4336 * 8, a3, 128);
    Arg1 = (uint16_t)(((uint16_t)(*(uint16_t *)(v_stack_m1D8 + 0x38BC))) | ((uint16_t)(local_rdi)));
    Arg1 = (uint16_t)((Arg1) & (0xFFFEULL));
    Arg1 = (uint16_t)((Arg1) | (128));
    if (condition_is_not_equal) goto loc_0021A803;
loc_0021A834:
    *(uint64_t *)(v_stack_m1D8 + 0x3860) = 0;
    Arg1 = (v_stack_m38) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg1 + result + (uint32_t)(Arg2) * 2 + 4336 * 8, a3, 128);
    return result;
loc_0021A86C:
    if (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x68) == 0) goto loc_0021A88D;
    result = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0xD8))) + (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x68));
loc_0021A87E:
    if (*(uint64_t *)(result + 0x1A0) != 0) goto loc_0021A87E;
loc_0021A88D:
    if (((*(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x2)) & (8)) == 0) goto loc_0021A8A7;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x220)) != (v_rip + 14374502)) goto loc_0021B072;
loc_0021A8A7:
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x168)) == 0) goto loc_0021A4AB;
    result = KiEndCounterAccumulation(*(uint64_t *)(v_stack_m28 + 0x40), Arg1 + result + (uint32_t)(Arg2) * 2 + 4336 * 8, a3, 128);
    goto loc_0021A4AB;
loc_0021A8C2:
    if ((*(uint64_t *)(result)) == 0) goto loc_0021A676;
    v_stack_m1E8 = 0;
    v_stack_m208 = 0;
    if ((uint8_t)(result) == 0) goto loc_0021AFF1;
    a3 = (a3) << ((uint8_t)((uint8_t)(result)));
    a3 = (*(uint64_t *)(v_stack_m28 + 0x48)) << ((uint8_t)((uint8_t)(result)));
loc_0021A90E:
    v_stack_m1E8 = Arg1 + result + (uint32_t)(Arg2) * 2 + 4336 * 8;
    v_stack_m208 = Arg1 + result + (uint32_t)(Arg2) * 2 + 4336 * 8;
    a4 = (Arg1 + result + (uint32_t)(Arg2) * 2 + 4336 * 8) >> ((uint8_t)((int8_t)(*(uint8_t *)(v_rip + 0xDAC2B1))));
    Arg2 = (Arg1 + result + (uint32_t)(Arg2) * 2 + 4336 * 8) >> ((uint8_t)((int8_t)(*(uint8_t *)(v_rip + 0xDAC2B1))));
    Arg2 = (uint32_t)((Arg2) - ((uint32_t)(a4)));
    if (condition_is_equal) goto loc_0021A676;
    goto loc_0021A676;
loc_0021A96B:
    Arg2 = ((uint32_t)((uint32_t)(Arg1 + result + (uint32_t)(Arg2) * 2 + 4336 * 8))) + ((uint32_t)((uint32_t)(Arg1 + result + (uint32_t)(Arg2) * 2 + 4336 * 8)));
    Arg1 = (*(uint64_t *)(v_stack_m230 + Arg2 * 8 + 0x8)) + (0);
    *(void **)(v_stack_m230 + Arg2 * 8 + 0x8) = Arg1;
    goto loc_0021A404;
loc_0021A983:
    local_r12 = 0;
    if ((*(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x86DC)) == 0) goto loc_0021A9EF;
    Arg1 = 0;
    result = KeQueryPerformanceCounter(Arg1, Arg2, Arg1 + result + (uint32_t)(Arg2) * 2 + 4336 * 8, v_stack_m230);
    v_stack_m1E0 = 0;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0xAC)) != 0) {
        Arg2 = (result) << ((uint8_t)(*(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0xAC)));
    }
    v_stack_m1E0 = Arg2;
    local_r11 = (Arg2) - (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x8680));
    local_r14 = (result) - (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x86F8));
    if ((*(uint8_t *)(v_rip + 0xDAC0AC)) != 0) goto loc_0021AB0F;
loc_0021A9EF:
    Arg1 = (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x8700)) + (local_r14);
    *(void **)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x8700) = Arg1;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x8778)) + (local_r11);
    *(void **)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x8778) = Arg1;
    result = *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0xB0);
    if (((*(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x2)) & (32)) != 0) {
        Arg1 = *(uint64_t *)(v_stack_m28 + 0x38);
        result = PoGetFrequencyBucket(Arg1, *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x86F8), Arg1 + result + (uint32_t)(Arg2) * 2 + 4336 * 8, v_stack_m230);
        Arg1 = 0;
        result = (uint32_t)(result);
        Arg1 = ((*(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x8A08)) != 0) ? 1 : 0;
        Arg1 = Arg1 + result * 2;
        Arg1 = Arg1 + 4336;
        Arg2 = *(uint64_t *)(v_stack_m28 + 0x38) + Arg1 * 8;
        Arg1 = *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + arg1 * 8);
        Arg1 = (Arg1) + (local_r11);
        *(void **)(Arg2) = Arg1;
    }
    if (((*(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x2)) & (64)) == 0) goto loc_0021AA5D;
    if (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x3C8) != 0) {
        *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x3C8) + 0x40) = 1;
    }
    *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x86F8) = result;
    *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x8680) = Arg2;
    if (((*(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x2)) & (2)) == 0) goto loc_0021A7C2;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x168) + 0x20) == 0) goto loc_0021A7C2;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC4BE79))) == 0) goto loc_0021A7C2;
loc_0021AAA5:
    if (((1) & (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x168) + 0x20))) != 0) goto loc_0021B0EA;
loc_0021AAAE:
    local_r13 = (1) + (1);
    a3 = (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x168) + 48) + (24);
    local_rbx = (v_rip + 13591515) + (4);
    a4 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC4BE79))))) - (1);
    if (condition_is_not_equal) goto loc_0021AAA5;
    goto loc_0021A7BE;
loc_0021AAC4:
    Arg1 = (*(uint64_t *)(local_rbx + *(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x7C) * 8 + 0x8688 * 1)) + (0);
    *(void **)(local_rbx + *(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x7C) * 8 + 0x8688 * 1) = Arg1;
    local_rdi = (uint8_t)((*(uint64_t *)(v_stack_m28 + 0x48)) & (239));
    goto loc_0021A30E;
loc_0021AAE4:
    local_r10 = 0;
    goto loc_0021A268;
loc_0021AAF6:
    if (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x3C8) == 0) goto loc_0021A469;
    *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x3C8) + 0x40) = 0;
    goto loc_0021A469;
loc_0021AB0F:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x3C8))) == 0) goto loc_0021A9EF;
    v_stack_m210 = 0;
    if ((uint8_t)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x3C8)) == 0) goto loc_0021B01B;
    Arg2 = (*(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x7C) * 8 + 34440) << ((uint8_t)((uint8_t)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x3C8))));
    result = 0;
    a3 = (0) << ((uint8_t)((uint8_t)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x3C8))));
loc_0021AB59:
    v_stack_m200 = 0;
    v_stack_m210 = Arg2;
    v_stack_m200 = Arg2;
    a4 = (Arg2) >> ((uint8_t)((int8_t)(*(uint8_t *)(v_rip + 0xDAC066))));
    Arg2 = (Arg2) >> ((uint8_t)((int8_t)(*(uint8_t *)(v_rip + 0xDAC066))));
    Arg2 = (uint32_t)((Arg2) - ((uint32_t)(a4)));
    if (condition_is_not_equal) goto loc_0021AE29;
loc_0021AB9F:
    local_r12 = 0;
    goto loc_0021A9EF;
loc_0021ABA7:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(local_r13), (uint8_t)(*(uint64_t *)(v_rip + 0xDAC78E)), Arg2, a4);
    goto loc_0021A557;
loc_0021ABB8:
    if (((uint8_t)((uint8_t)(local_r13))) != 2) goto loc_0021AF58;
    *(uint8_t *)(result + 0x11) = 5;
    result = KiInsertQueueInternal(*(uint64_t *)(result + 0x18), result, Arg2, a4);
    if (((uint8_t)((uint8_t)(local_r13))) == 2) goto loc_0021A5E1;
    a3 = 0;
    goto loc_0021A586;
loc_0021ABE3:
    if (((*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x74)) & (0x400ULL)) != 0) goto loc_0021AC09;
    result = (local_rdi) >> (4);
    result = (uint32_t)((result) & (31));
    if (((uint32_t)(result)) < ((uint32_t)(result))) goto loc_0021ADDF;
loc_0021AC09:
loc_0021AC17:
    v_stack_m228 = *(uint64_t *)(result + 0x18);
    v_stack_m230 = local_r11;
    if ((*(uint64_t *)(v_stack_m28 + 0x40)) == (*(uint64_t *)(local_rbx + 0x18))) goto loc_0021A25A;
    v_stack_m230 = local_r11;
    v_stack_m228 = 0;
    result = KiQueryEffectivePriorityThread(*(uint64_t *)(v_stack_m28 + 0x40), local_rbx, a3, a4);
    if (((uint32_t)(result)) >= 8) goto loc_0021AAE4;
    local_r10 = 0;
    v_stack_m230 = v_stack_m210;
    v_stack_m228 = v_stack_m218;
    goto loc_0021A268;
loc_0021AC7A:
    local_rdi = (uint16_t)((local_rdi) & ((uint16_t)((uint32_t)(0xFFF7ULL))));
    result = KiSelectActiveTimerTable(local_rbx, 1, a3, a4);
    if (result == 0) goto loc_0021AEF5;
    local_r12 = ((*(uint64_t *)(v_rip + 0xC4BBEE)) != (*(uint64_t *)(result + 0x4200))) ? 1 : 0;
    result = ((*(uint64_t *)(v_rip + 0xC4BBFD)) != (*(uint64_t *)(result + 0x4208))) ? 1 : 0;
    local_r14 = (uint8_t)(result);
    if ((*(uint32_t *)(v_rip + 0xDABF6C)) != 0) { local_r14 = (uint32_t)((uint8_t)(local_r12)); }
    result = (uint8_t)(local_r12);
    if ((*(uint64_t *)(v_rip + 0xC4BBEE)) != (*(uint64_t *)(result + 0x4200))) {
        result = *(uint64_t *)(result);
        *(uint64_t *)(result + 0x4200) = *(uint64_t *)(v_rip + 0xC4BBEE);
        result = (result) >> (18);
        *(uint32_t *)(result + 0x4210) = (uint32_t)(result);
    }
    if ((uint8_t)(local_r14) != 0) goto loc_0021AE3A;
loc_0021AD0A:
    if ((*(uint64_t *)(v_rip + 0xC4BBEE)) == (*(uint64_t *)(result + 0x4200))) goto loc_0021AE94;
loc_0021AD13:
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8) != 0) goto loc_0021AECD;
loc_0021AD2C:
    v_stack_m1C0 = *(uint64_t *)(result);
    v_stack_m240 = v_stack_m1C8;
    result = KiTimerExpiration(local_rbx, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x4210)))), *(uint64_t *)(result), (uint8_t)(local_r14));
loc_0021AD59:
    if ((*(uint8_t *)(local_rbx + 0x21)) != 0) {
        result = v_stack_m1C8;
        a4 = (uint8_t)(local_r14);
        a3 = (uint8_t)(local_r12);
        v_stack_m240 = result;
        Arg2 = *(uint64_t *)(result);
        Arg1 = local_rbx;
        result = KiTimer2Expiration(Arg1, Arg2, a3, a4);
    }
    goto loc_0021A4C7;
loc_0021AD90:
    local_r14 = (uint32_t)((local_r14) + 1);
    if (((*(uint32_t *)(v_rip + 0xDAA512)) & ((uint32_t)(local_r14))) == 0) goto loc_0021AF26;
loc_0021ADA0:
loc_0021ADA2:
    if (sign_flag) goto loc_0021AD90;
    if (condition_is_below) goto loc_0021AD90;
    a3 = 0;
    goto loc_0021A571;
loc_0021ADB7:
loc_0021ADBE:
    if (condition_is_not_equal) goto loc_0021ADBE;
    if (condition_is_above_or_equal) goto loc_0021A4EE;
    result = KiRemoveSystemWorkPriorityKick(Arg1, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(a3)))), a3, a4);
    goto loc_0021A4EE;
loc_0021ADDF:
    goto loc_0021AC17;
loc_0021ADF2:
loc_0021ADF9:
    if (condition_is_not_equal) goto loc_0021ADF9;
    if (condition_is_above_or_equal) goto loc_0021A535;
    result = KiRemoveSystemWorkPriorityKick(Arg1, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(a3)))), a3, a4);
    goto loc_0021A535;
loc_0021AE1A:
    goto loc_0021A676;
loc_0021AE29:
    goto loc_0021AB9F;
loc_0021AE3A:
    *(uint64_t *)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(a3)))) + 0x4208) = *(uint64_t *)(v_rip + 0xC4BBFD);
    local_r13 = 1;
    if (1 >= ((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(a3)))) + 0x4214))))) { local_r13 = (uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(a3)))) + 0x4214))); }
    result = (*(uint64_t *)(result)) >> (18);
    *(uint32_t *)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(a3)))) + 0x4214) = (uint32_t)(result);
    goto loc_0021AD0A;
loc_0021AE60:
    v_stack_m208 = (uint32_t)(result);
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(result))) - ((uint32_t)(Arg1)));
    if (Arg2 >= 32) goto loc_0021AF7D;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m230 + 0xC4))) << ((uint8_t)((uint32_t)(Arg2))));
    result = (uint32_t)((result) | (1));
    v_stack_m204 = (uint32_t)(result);
loc_0021AE83:
    *(uint64_t *)(v_stack_m230 + 0xC0) = v_stack_m208;
    goto loc_0021A3DD;
loc_0021AE94:
    if ((uint8_t)(v_stack_m228) != 0) goto loc_0021AD13;
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8) != 0) goto loc_0021AF90;
loc_0021AEB6:
    v_stack_m1C0 = *(uint64_t *)(v_stack_m208);
    goto loc_0021AD59;
loc_0021AECD:
loc_0021AED4:
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8) != 0) goto loc_0021AED4;
    if (condition_is_above_or_equal) goto loc_0021AD2C;
    result = KiRemoveSystemWorkPriorityKick(*(uint64_t *)(gs_base + (0 + 0x20)), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8))))), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), v_stack_m230);
    goto loc_0021AD2C;
loc_0021AEF5:
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8) != 0) goto loc_0021AFC9;
loc_0021AF0E:
    v_stack_m1C0 = *(uint64_t *)(result);
    goto loc_0021A4C7;
loc_0021AF26:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xDABB8C)))) & (64)) == 0) goto loc_0021ADA0;
    result = KiCheckVpBackingLongSpinWaitHypercall(*(uint64_t *)(gs_base + (0 + 0x20)), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8))))), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), v_stack_m230);
    if ((uint8_t)(result) == 0) goto loc_0021ADA0;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(v_stack_m228)), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8))))), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), v_stack_m230);
    goto loc_0021ADA2;
loc_0021AF4E:
    goto loc_0021A25D;
loc_0021AF58:
    if (((uint8_t)(v_stack_m228)) == 4) goto loc_0021AFFC;
    a4 = 0;
    result = KiTryUnwaitThread(local_r12, result, 256, a4);
    a3 = 0;
    goto loc_0021A586;
loc_0021AF7D:
    v_stack_m204 = (uint32_t)(local_r13);
    goto loc_0021AE83;
loc_0021AF87:
    *(uint8_t *)(local_rbx + 0x6) = (uint8_t)(local_r12);
    goto loc_0021A79D;
loc_0021AF90:
loc_0021AF97:
    if (condition_is_not_equal) goto loc_0021AF97;
    if (condition_is_above_or_equal) goto loc_0021AEB6;
    result = KiRemoveSystemWorkPriorityKick(local_r12, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(a3)))), a3, a4);
    goto loc_0021AEB6;
loc_0021AFB8:
    goto loc_0021A1FF;
loc_0021AFC0:
    *(uint8_t *)(local_rbx + 0x6) = 0;
    goto loc_0021A7D1;
loc_0021AFC9:
loc_0021AFD0:
    if (condition_is_not_equal) goto loc_0021AFD0;
    if (condition_is_above_or_equal) goto loc_0021AF0E;
    result = KiRemoveSystemWorkPriorityKick(local_r12, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(a3)))), a3, a4);
    goto loc_0021AF0E;
loc_0021AFF1:
    goto loc_0021A90E;
loc_0021AFFC:
    *(uint8_t *)(result + 0x11) = 5;
    *(uint32_t *)(local_rdi + 0x4) = (uint32_t)(local_rdi);
    result = KeInsertQueueDpc(*(uint64_t *)(result + 0x18), local_rdi, result, a4);
    a3 = 0;
    goto loc_0021A586;
loc_0021B01B:
    result = 0;
    goto loc_0021AB59;
loc_0021B025:
    if (((uint32_t)(*(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x204))) >= 7) goto loc_0021A4A1;
    Arg2 = (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x50));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x50)))) <= ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x54))))) { Arg2 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x54))); }
    Arg1 = 0;
    Arg1 = (Arg2 >= (*(uint32_t *)(v_rip + 0xDAA32A))) ? 1 : 0;
    Arg1 = (uint32_t)((Arg1 + (uint32_t)((uint32_t)(*(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x204))) * 2) * (*(uint32_t *)(v_rip + 0xDAA380)));
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(*(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x205))));
    goto loc_0021A4A1;
loc_0021B072:
    Arg2 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x240) + *(uint16_t *)(*(uint64_t *)(local_rbx + 0xC0) + 0x88) * 8 + 0x8)) & (*(uint64_t *)(*(uint64_t *)(local_rbx + 0xC0) + 0x80));
    if (Arg2 == (*(uint64_t *)(*(uint64_t *)(local_rbx + 0xC0) + 0x80))) goto loc_0021A8A7;
    goto loc_0021A8A7;
loc_0021B0AC:
    v_stack_m230 = 72;
    v_stack_m228 = *(uint64_t *)(result);
    goto loc_0021A25D;
loc_0021B0C1:
    goto loc_0021A365;
loc_0021B0CB:
    goto loc_0021A6E3;
loc_0021B0D6:
    Arg2 = (100) << (32);
    result = (72) | (Arg2);
    *(uint64_t *)(72) = result;
    goto loc_0021A77D;
loc_0021B0EA:
    Arg2 = (Arg2) << (32);
    result = (result) | (Arg2);
    *(uint64_t *)(100) = result;
    goto loc_0021AAAE;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `16` | `R` |
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x0` | `32` | `R/W` |
| `Arg1` | `+ 0x0` | `64` | `W` |
| `Arg1` | `+ 0x0 + rax*8` | `64` | `R` |
| `Arg1` | `+ 0x0 + rcx*8` | `64` | `R` |
| `Arg1` | `+ 0x0 + rdx*1` | `64` | `R` |
| `Arg1` | `+ 0x0 + rdx*1` | `64` | `W` |
| `Arg1` | `+ 0x4` | `32` | `R` |
| `Arg1` | `+ 0x4` | `32` | `R/W` |
| `Arg1` | `+ 0x4` | `32` | `W` |
| `Arg1` | `+ 0x6` | `8` | `R` |
| `Arg1` | `+ 0x6` | `8` | `W` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x20` | `8` | `W` |
| `Arg1` | `+ 0x21` | `8` | `R` |
| `Arg1` | `+ 0xAC` | `8` | `R` |
| `Arg1` | `+ 0xB0` | `64` | `R` |
| `Arg1` | `+ 0xC0` | `64` | `R` |
| `Arg1` | `+ 0xD8` | `32` | `R` |
| `Arg1` | `+ 0x38BC` | `16` | `R` |
| `Arg1` | `+ 0x38BC` | `16` | `R/W` |
| `Arg1` | `+ 0x8340` | `64` | `R` |
| `Arg1` | `+ 0x8644` | `32` | `R/W` |
| `Arg1` | `+ 0x8648` | `32` | `R/W` |
| `Arg1` | `+ 0x864C` | `32` | `R/W` |
| `Arg1` | `+ 0x866C` | `32` | `R/W` |
| `Arg1` | `+ 0x8680` | `64` | `R` |
| `Arg1` | `+ 0x8680` | `64` | `W` |
| `Arg1` | `+ 0x86A8` | `64` | `R/W` |
| `Arg1` | `+ 0x86B0` | `64` | `R` |

추가 오프셋 13개는 표에서 생략했습니다.

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0021A0B0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
