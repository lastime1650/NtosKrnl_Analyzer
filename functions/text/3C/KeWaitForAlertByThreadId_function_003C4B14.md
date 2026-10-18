# KeWaitForAlertByThreadId

- RVA: `0x003C4B14`–`0x003C4F50` (길이 `1,084` bytes)
- VA: `0x00000001403C4B14`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008E428`
- 디코드: `254`개 명령, `1,084/1,084` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **14**; 고유 호출 대상: **13**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x003C4BB9` → [KiCheckWaitNext](KiCheckWaitNext_function_003C5FC0.md) (function, `0x003C5FC0`)
- `0x003C4CCB` → [KiCommitThreadWait](../20/KiCommitThreadWait_function_0020DFE0.md) (function, `0x0020DFE0`)
- `0x003C4CF2` → [KiAbUmPostWait](KiAbUmPostWait_function_003C4F58.md) (function, `0x003C4F58`)
- `0x003C4E1B` → [KiFastExitThreadWait](../22/KiFastExitThreadWait_function_00220BB0.md) (function, `0x00220BB0`)
- `0x003C4E2A` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x003C4E42` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x003C4E52` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x003C4E7A` → [KiRemoveSystemWorkPriorityKick](../26/KiRemoveSystemWorkPriorityKick_function_002631D0.md) (function, `0x002631D0`)
- `0x003C4EA1` → [KiReleaseThreadLockLowerIrql](KiReleaseThreadLockLowerIrql_function_003C65D0.md) (function, `0x003C65D0`)
- `0x003C4EAD` → [KiDeliverApc](../25/KiDeliverApc_function_00250F20.md) (function, `0x00250F20`)
- `0x003C4EDC` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x003C4EFF` → [KiPerformWaitDeferredWork](../22/KiPerformWaitDeferredWork_function_00220480.md) (function, `0x00220480`)
- `0x003C4F1C` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x003C4F3F` → [KiProcessDeferredReadyList](../25/KiProcessDeferredReadyList_function_00250800.md) (function, `0x00250800`)

### Direct callers
- [sub_006F88AE](../6F/Unknown_function_006F88AE.md) at `0x006F89B3`
- [RtlpRunOnceWaitForInit](../../page/79/RtlpRunOnceWaitForInit_function_00794AF8.md) at `0x00794B5D`
- [NtWaitForAlertByThreadId](../../page/9E/NtWaitForAlertByThreadId_function_009E98F0.md) at `0x009E991F`

### Static image references
- `0x003C4BF2` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x003C4D1F` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x003C4E34` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003C4B14  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
003C4B19  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
003C4B1E  55                              push rbp
003C4B1F  56                              push rsi
003C4B20  57                              push rdi
003C4B21  41 54                           push r12
003C4B23  41 55                           push r13
003C4B25  41 56                           push r14
003C4B27  41 57                           push r15
003C4B29  48 8B EC                        mov rbp, rsp
003C4B2C  48 83 EC 50                     sub rsp, 0x50
003C4B30  65 48 8B 3C 25 88 01 00 00      mov rdi, qword ptr gs:[0x188]
003C4B39  45 33 D2                        xor r10d, r10d
003C4B3C  4C 89 55 E8                     mov qword ptr [rbp - 0x18], r10
003C4B40  4D 8B F8                        mov r15, r8
003C4B43  44 89 55 58                     mov dword ptr [rbp + 0x58], r10d
003C4B47  48 8B DA                        mov rbx, rdx
003C4B4A  44 8A E9                        mov r13b, cl
003C4B4D  44 89 55 E0                     mov dword ptr [rbp - 0x20], r10d
003C4B51  F0 0F BA 77 78 04               lock btr dword ptr [rdi + 0x78], 4
003C4B57  0F 82 72 03 00 00               jb 0x1403c4ecf
003C4B5D  48 85 D2                        test rdx, rdx
003C4B60  0F 85 76 02 00 00               jne 0x1403c4ddc
003C4B66  BE 01 00 00 00                  mov esi, 1
003C4B6B  4D 85 FF                        test r15, r15
003C4B6E  74 33                           je 0x1403c4ba3
003C4B70  44 3A EE                        cmp r13b, sil
003C4B73  75 2E                           jne 0x1403c4ba3
003C4B75  FA                              cli
003C4B76  48 8B 97 20 03 00 00            mov rdx, qword ptr [rdi + 0x320]
003C4B7D  48 85 D2                        test rdx, rdx
003C4B80  0F 85 29 02 00 00               jne 0x1403c4daf
003C4B86  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
003C4B8F  4C 8B 81 B8 8E 00 00            mov r8, qword ptr [rcx + 0x8eb8]
003C4B96  4D 85 C0                        test r8, r8
003C4B99  0F 85 BD 02 00 00               jne 0x1403c4e5c
003C4B9F  FB                              sti
003C4BA0  89 75 E0                        mov dword ptr [rbp - 0x20], esi
003C4BA3  48 8D 4D 58                     lea rcx, [rbp + 0x58]
003C4BA7  45 33 C0                        xor r8d, r8d
003C4BAA  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
003C4BAF  4C 8D 4D E8                     lea r9, [rbp - 0x18]
003C4BB3  48 8B CF                        mov rcx, rdi
003C4BB6  48 8B D3                        mov rdx, rbx
003C4BB9  E8 02 14 00 00                  call 0x1403c5fc0
003C4BBE  8B D8                           mov ebx, eax
003C4BC0  0F B6 B7 86 01 00 00            movzx esi, byte ptr [rdi + 0x186]
003C4BC7  45 33 FF                        xor r15d, r15d
003C4BCA  4C 89 7D F0                     mov qword ptr [rbp - 0x10], r15
003C4BCE  41 BC 02 00 00 00               mov r12d, 2
003C4BD4  83 67 74 EF                     and dword ptr [rdi + 0x74], 0xffffffef
003C4BD8  45 8B F7                        mov r14d, r15d
003C4BDB  44 88 7F 70                     mov byte ptr [rdi + 0x70], r15b
003C4BDF  44 88 AF 87 01 00 00            mov byte ptr [rdi + 0x187], r13b
003C4BE6  F0 48 0F BA 6F 40 00            lock bts qword ptr [rdi + 0x40], 0
003C4BED  73 1D                           jae 0x1403c4c0c
003C4BEF  41 FF C6                        inc r14d
003C4BF2  44 85 35 B3 06 C0 00            test dword ptr [rip + 0xc006b3], r14d
003C4BF9  0F 84 35 02 00 00               je 0x1403c4e34
003C4BFF  F3 90                           pause
003C4C01  48 8B 47 40                     mov rax, qword ptr [rdi + 0x40]
003C4C05  48 85 C0                        test rax, rax
003C4C08  74 DC                           je 0x1403c4be6
003C4C0A  EB E3                           jmp 0x1403c4bef
003C4C0C  44 38 BF C1 00 00 00            cmp byte ptr [rdi + 0xc1], r15b
003C4C13  0F 85 6B 02 00 00               jne 0x1403c4e84
003C4C19  44 84 A7 C2 00 00 00            test byte ptr [rdi + 0xc2], r12b
003C4C20  44 8B 65 E0                     mov r12d, dword ptr [rbp - 0x20]
003C4C24  4C 8B 7D 50                     mov r15, qword ptr [rbp + 0x50]
003C4C28  0F 85 B5 02 00 00               jne 0x1403c4ee3
003C4C2E  45 33 F6                        xor r14d, r14d
003C4C31  C6 87 84 01 00 00 05            mov byte ptr [rdi + 0x184], 5
003C4C38  48 B8 20 03 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000320
003C4C42  C6 87 83 02 00 00 25            mov byte ptr [rdi + 0x283], 0x25
003C4C49  8B 00                           mov eax, dword ptr [rax]
003C4C4B  89 87 B4 01 00 00               mov dword ptr [rdi + 0x1b4], eax
003C4C51  4C 89 77 40                     mov qword ptr [rdi + 0x40], r14
003C4C55  F0 0F BA 77 78 04               lock btr dword ptr [rdi + 0x78], 4
003C4C5B  0F 82 9F 01 00 00               jb 0x1403c4e00
003C4C61  4C 8B 4D E8                     mov r9, qword ptr [rbp - 0x18]
003C4C65  44 8B 45 58                     mov r8d, dword ptr [rbp + 0x58]
003C4C69  49 8B C1                        mov rax, r9
003C4C6C  41 83 F8 02                     cmp r8d, 2
003C4C70  0F 84 C2 00 00 00               je 0x1403c4d38
003C4C76  45 85 C0                        test r8d, r8d
003C4C79  74 27                           je 0x1403c4ca2
003C4C7B  48 85 C0                        test rax, rax
003C4C7E  0F 84 C2 02 00 00               je 0x1403c4f46
003C4C84  48 B9 14 00 00 00 80 F7 FF FF   movabs rcx, 0xfffff78000000014
003C4C8E  48 8B 09                        mov rcx, qword ptr [rcx]
003C4C91  4C 8B 4D E8                     mov r9, qword ptr [rbp - 0x18]
003C4C95  48 3B C8                        cmp rcx, rax
003C4C98  0F 87 A8 02 00 00               ja 0x1403c4f46
003C4C9E  44 8B 45 58                     mov r8d, dword ptr [rbp + 0x58]
003C4CA2  4C 8D B7 40 01 00 00            lea r14, [rdi + 0x140]
003C4CA9  45 33 D2                        xor r10d, r10d
003C4CAC  4D 89 7E 20                     mov qword ptr [r14 + 0x20], r15
003C4CB0  49 8B D6                        mov rdx, r14
003C4CB3  41 C6 46 11 05                  mov byte ptr [r14 + 0x11], 5
003C4CB8  48 8B CF                        mov rcx, rdi
003C4CBB  4C 89 54 24 28                  mov qword ptr [rsp + 0x28], r10
003C4CC0  C6 87 4B 02 00 00 01            mov byte ptr [rdi + 0x24b], 1
003C4CC7  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
003C4CCB  E8 10 93 E4 FF                  call 0x14020dfe0
003C4CD0  45 33 F6                        xor r14d, r14d
003C4CD3  48 8B F0                        mov rsi, rax
003C4CD6  44 88 B7 83 02 00 00            mov byte ptr [rdi + 0x283], r14b
003C4CDD  41 8B DE                        mov ebx, r14d
003C4CE0  3D 00 01 00 00                  cmp eax, 0x100
003C4CE5  74 2B                           je 0x1403c4d12
003C4CE7  45 85 E4                        test r12d, r12d
003C4CEA  74 0B                           je 0x1403c4cf7
003C4CEC  49 8B D7                        mov rdx, r15
003C4CEF  48 8B CF                        mov rcx, rdi
003C4CF2  E8 61 02 00 00                  call 0x1403c4f58
003C4CF7  48 8B 9C 24 90 00 00 00         mov rbx, qword ptr [rsp + 0x90]
003C4CFF  8B C6                           mov eax, esi
003C4D01  48 83 C4 50                     add rsp, 0x50
003C4D05  41 5F                           pop r15
003C4D07  41 5E                           pop r14
003C4D09  41 5D                           pop r13
003C4D0B  41 5C                           pop r12
003C4D0D  5F                              pop rdi
003C4D0E  5E                              pop rsi
003C4D0F  5D                              pop rbp
003C4D10  C3                              ret
003C4D11  CC                              int3
003C4D12  44 0F 20 C6                     mov rsi, cr8
003C4D16  B8 02 00 00 00                  mov eax, 2
003C4D1B  44 0F 22 C0                     mov cr8, rax
003C4D1F  44 39 35 FA 1F C0 00            cmp dword ptr [rip + 0xc01ffa], r14d
003C4D26  0F 85 F9 00 00 00               jne 0x1403c4e25
003C4D2C  40 88 B7 86 01 00 00            mov byte ptr [rdi + 0x186], sil
003C4D33  E9 88 FE FF FF                  jmp 0x1403c4bc0
003C4D38  48 B8 B0 03 00 00 80 F7 FF FF   movabs rax, 0xfffff780000003b0
003C4D42  48 B9 08 00 00 00 80 F7 FF FF   movabs rcx, 0xfffff78000000008
003C4D4C  48 8B 00                        mov rax, qword ptr [rax]
003C4D4F  48 8B 09                        mov rcx, qword ptr [rcx]
003C4D52  48 2B 8F F8 00 00 00            sub rcx, qword ptr [rdi + 0xf8]
003C4D59  8B 97 B8 03 00 00               mov edx, dword ptr [rdi + 0x3b8]
003C4D5F  48 2B C8                        sub rcx, rax
003C4D62  48 8B 45 E8                     mov rax, qword ptr [rbp - 0x18]
003C4D66  4C 8B 4D E8                     mov r9, qword ptr [rbp - 0x18]
003C4D6A  44 38 B7 87 01 00 00            cmp byte ptr [rdi + 0x187], r14b
003C4D71  0F 84 1E FF FF FF               je 0x1403c4c95
003C4D77  44 39 B7 E4 01 00 00            cmp dword ptr [rdi + 0x1e4], r14d
003C4D7E  0F 85 11 FF FF FF               jne 0x1403c4c95
003C4D84  44 38 B7 86 01 00 00            cmp byte ptr [rdi + 0x186], r14b
003C4D8B  0F 85 04 FF FF FF               jne 0x1403c4c95
003C4D91  44 38 B7 C0 00 00 00            cmp byte ptr [rdi + 0xc0], r14b
003C4D98  0F 85 F7 FE FF FF               jne 0x1403c4c95
003C4D9E  85 D2                           test edx, edx
003C4DA0  0F 84 EF FE FF FF               je 0x1403c4c95
003C4DA6  49 8D 04 11                     lea rax, [r9 + rdx]
003C4DAA  E9 E6 FE FF FF                  jmp 0x1403c4c95
003C4DAF  41 8B CA                        mov ecx, r10d
003C4DB2  83 F9 08                        cmp ecx, 8
003C4DB5  0F 83 CB FD FF FF               jae 0x1403c4b86
003C4DBB  44 8B C1                        mov r8d, ecx
003C4DBE  49 B9 FC FF FF FF FF FF FF 7F   movabs r9, 0x7ffffffffffffffc
003C4DC8  4A 8B 04 C2                     mov rax, qword ptr [rdx + r8*8]
003C4DCC  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
003C4DD0  49 23 C1                        and rax, r9
003C4DD3  49 3B C7                        cmp rax, r15
003C4DD6  74 17                           je 0x1403c4def
003C4DD8  03 CE                           add ecx, esi
003C4DDA  EB D6                           jmp 0x1403c4db2
003C4DDC  4C 39 12                        cmp qword ptr [rdx], r10
003C4DDF  0F 85 81 FD FF FF               jne 0x1403c4b66
003C4DE5  BE 02 01 00 00                  mov esi, 0x102
003C4DEA  E9 08 FF FF FF                  jmp 0x1403c4cf7
003C4DEF  40 08 75 E0                     or byte ptr [rbp - 0x20], sil
003C4DF3  48 8B 45 E0                     mov rax, qword ptr [rbp - 0x20]
003C4DF7  4A 89 04 C2                     mov qword ptr [rdx + r8*8], rax
003C4DFB  E9 86 FD FF FF                  jmp 0x1403c4b86
003C4E00  BE 01 01 00 00                  mov esi, 0x101
003C4E05  44 88 B7 83 02 00 00            mov byte ptr [rdi + 0x283], r14b
003C4E0C  44 8B C3                        mov r8d, ebx
003C4E0F  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
003C4E18  48 8B D7                        mov rdx, rdi
003C4E1B  E8 90 BD E5 FF                  call 0x140220bb0
003C4E20  E9 C2 FE FF FF                  jmp 0x1403c4ce7
003C4E25  8A D0                           mov dl, al
003C4E27  40 8A CE                        mov cl, sil
003C4E2A  E8 CD 08 13 00                  call 0x1404f56fc
003C4E2F  E9 F8 FE FF FF                  jmp 0x1403c4d2c
003C4E34  8B 05 7E 1C C0 00               mov eax, dword ptr [rip + 0xc01c7e]
003C4E3A  A8 40                           test al, 0x40
003C4E3C  0F 84 BD FD FF FF               je 0x1403c4bff
003C4E42  E8 49 A6 F4 FF                  call 0x14030f490
003C4E47  84 C0                           test al, al
003C4E49  0F 84 B0 FD FF FF               je 0x1403c4bff
003C4E4F  41 8B CE                        mov ecx, r14d
003C4E52  E8 09 A6 F4 FF                  call 0x14030f460
003C4E57  E9 A5 FD FF FF                  jmp 0x1403c4c01
003C4E5C  41 0F 0D 08                     prefetchw byte ptr [r8]
003C4E60  41 8B 00                        mov eax, dword ptr [r8]
003C4E63  8B D0                           mov edx, eax
003C4E65  0F BA F2 15                     btr edx, 0x15
003C4E69  F0 41 0F B1 10                  lock cmpxchg dword ptr [r8], edx
003C4E6E  75 F3                           jne 0x1403c4e63
003C4E70  0F BA E0 15                     bt eax, 0x15
003C4E74  0F 83 25 FD FF FF               jae 0x1403c4b9f
003C4E7A  E8 51 E3 E9 FF                  call 0x1402631d0
003C4E7F  E9 1B FD FF FF                  jmp 0x1403c4b9f
003C4E84  66 44 39 BF E6 01 00 00         cmp word ptr [rdi + 0x1e6], r15w
003C4E8C  0F 85 87 FD FF FF               jne 0x1403c4c19
003C4E92  40 80 FE 01                     cmp sil, 1
003C4E96  0F 83 7D FD FF FF               jae 0x1403c4c19
003C4E9C  B2 01                           mov dl, 1
003C4E9E  48 8B CF                        mov rcx, rdi
003C4EA1  E8 2A 17 00 00                  call 0x1403c65d0
003C4EA6  45 33 C0                        xor r8d, r8d
003C4EA9  33 D2                           xor edx, edx
003C4EAB  33 C9                           xor ecx, ecx
003C4EAD  E8 6E C0 E8 FF                  call 0x140250f20
003C4EB2  44 0F 20 C1                     mov rcx, cr8
003C4EB6  45 0F 22 C4                     mov cr8, r12
003C4EBA  44 39 3D 5F 1E C0 00            cmp dword ptr [rip + 0xc01e5f], r15d
003C4EC1  75 16                           jne 0x1403c4ed9
003C4EC3  40 88 B7 86 01 00 00            mov byte ptr [rdi + 0x186], sil
003C4ECA  E9 05 FD FF FF                  jmp 0x1403c4bd4
003C4ECF  BE 01 01 00 00                  mov esi, 0x101
003C4ED4  E9 1E FE FF FF                  jmp 0x1403c4cf7
003C4ED9  41 8A D4                        mov dl, r12b
003C4EDC  E8 1B 08 13 00                  call 0x1404f56fc
003C4EE1  EB E0                           jmp 0x1403c4ec3
003C4EE3  45 33 F6                        xor r14d, r14d
003C4EE6  45 84 ED                        test r13b, r13b
003C4EE9  0F 84 42 FD FF FF               je 0x1403c4c31
003C4EEF  4C 8D 4D F0                     lea r9, [rbp - 0x10]
003C4EF3  4C 89 75 F0                     mov qword ptr [rbp - 0x10], r14
003C4EF7  41 B0 01                        mov r8b, 1
003C4EFA  8B D3                           mov edx, ebx
003C4EFC  48 8B CF                        mov rcx, rdi
003C4EFF  E8 7C B5 E5 FF                  call 0x140220480
003C4F04  4C 89 77 40                     mov qword ptr [rdi + 0x40], r14
003C4F08  85 C0                           test eax, eax
003C4F0A  75 23                           jne 0x1403c4f2f
003C4F0C  44 39 35 0D 1E C0 00            cmp dword ptr [rip + 0xc01e0d], r14d
003C4F13  74 0C                           je 0x1403c4f21
003C4F15  44 0F 20 C1                     mov rcx, cr8
003C4F19  40 8A D6                        mov dl, sil
003C4F1C  E8 77 07 13 00                  call 0x1404f5698
003C4F21  44 0F 22 C6                     mov cr8, rsi
003C4F25  BE C0 00 00 00                  mov esi, 0xc0
003C4F2A  E9 B8 FD FF FF                  jmp 0x1403c4ce7
003C4F2F  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
003C4F38  48 8D 55 F0                     lea rdx, [rbp - 0x10]
003C4F3C  44 8A C6                        mov r8b, sil
003C4F3F  E8 BC B8 E8 FF                  call 0x140250800
003C4F44  EB DF                           jmp 0x1403c4f25
003C4F46  BE 02 01 00 00                  mov esi, 0x102
003C4F4B  E9 B5 FE FF FF                  jmp 0x1403c4e05
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KeWaitForAlertByThreadId(unsigned __int8 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned int v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p18 = a3;
    v_rsp = (v_rsp) - (80);
    v_r10 = 0;
    v_stack_m50 = 0;
    v_stack_p20 = 0;
    v_stack_m58 = 0;
    if (condition_is_below) goto loc_003C4ECF;
    if (a2 != 0) goto loc_003C4DDC;
loc_003C4B66:
    if (a3 == 0) goto loc_003C4BA3;
    if (a1 != 1) goto loc_003C4BA3;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 800) != 0) goto loc_003C4DAF;
loc_003C4B86:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536) != 0) goto loc_003C4E5C;
loc_003C4B9F:
    v_stack_m58 = 1;
loc_003C4BA3:
    a3 = 0;
    v_stack_m68 = v_stack_p20;
    result = KiCheckWaitNext(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, a3, v_stack_m50);
loc_003C4BC0:
    v_r15 = 0;
    v_stack_m48 = 0;
loc_003C4BD4:
    *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 112) = 0;
    *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 391) = a1;
loc_003C4BE6:
    if (condition_is_above_or_equal) goto loc_003C4C0C;
loc_003C4BEF:
    v_r14 = (unsigned int)((0) + 1);
    if (((*(unsigned int *)(v_rip + 12584627)) & ((unsigned int)(v_r14))) == 0) goto loc_003C4E34;
loc_003C4BFF:
loc_003C4C01:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 64) == 0) goto loc_003C4BE6;
    goto loc_003C4BEF;
loc_003C4C0C:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 193)) != 0) goto loc_003C4E84;
loc_003C4C19:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 194)) & (2)) != 0) goto loc_003C4EE3;
    v_r14 = 0;
loc_003C4C31:
    *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 388) = 5;
    *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 643) = 37;
    *(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 436) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 64))));
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 64) = 0;
    if (condition_is_below) goto loc_003C4E00;
    if (((unsigned int)((unsigned int)(v_stack_p20))) == 2) goto loc_003C4D38;
    if ((unsigned int)((unsigned int)(v_stack_p20)) == 0) goto loc_003C4CA2;
    if (v_stack_m50 == 0) goto loc_003C4F46;
loc_003C4C95:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)))) > v_stack_m50) goto loc_003C4F46;
loc_003C4CA2:
    v_r10 = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 320 + 32) = v_stack_p18;
    *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 320 + 17) = 5;
    v_stack_m60 = 0;
    *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 587) = 1;
    v_stack_m68 = (unsigned int)((unsigned int)((unsigned int)(result)));
    result = KiCommitThreadWait(*(unsigned __int64 *)(gs_base + (0 + 392)), *(unsigned __int64 *)(gs_base + (0 + 392)) + 320, (unsigned int)(v_stack_p20), v_stack_m50);
    v_r14 = 0;
    *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 643) = 0;
    if (((unsigned int)(result)) == 256) goto loc_003C4D12;
loc_003C4CE7:
    if ((unsigned int)((unsigned int)(v_stack_m58)) != 0) {
        a2 = v_stack_p18;
        a1 = *(unsigned __int64 *)(gs_base + (0 + 392));
        result = KiAbUmPostWait(a1, a2, (unsigned int)(v_stack_p20), v_stack_m50);
    }
    v_rsp = (v_rsp) + (80);
    return (unsigned int)((unsigned int)(result));
loc_003C4D12:
    if ((*(unsigned int *)(v_rip + 12591098)) != 0) goto loc_003C4E25;
loc_003C4D2C:
    *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) = (unsigned __int8)(v_cr8);
    goto loc_003C4BC0;
loc_003C4D38:
    a1 = (*(unsigned __int64 *)(a1)) - (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 248));
    a1 = (a1) - (*(unsigned __int64 *)(2));
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 391)) == 0) goto loc_003C4C95;
    if ((*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 484)) != 0) goto loc_003C4C95;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390)) != 0) goto loc_003C4C95;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 192)) != 0) goto loc_003C4C95;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 952))) == 0) goto loc_003C4C95;
    goto loc_003C4C95;
loc_003C4DAF:
loc_003C4DB2:
    if (0 >= 8) goto loc_003C4B86;
    v_stack_m58 = *(unsigned __int64 *)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 952)) + 0 * 8);
    result = (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 952)) + 0 * 8)) & (v_stack_m50);
    if (result == v_stack_p18) goto loc_003C4DEF;
    a1 = (unsigned int)((0) + ((unsigned int)(v_cr8)));
    goto loc_003C4DB2;
loc_003C4DDC:
    if ((*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 952)))) != 0) goto loc_003C4B66;
    goto loc_003C4CF7;
loc_003C4DEF:
    *(unsigned __int64 *)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 952)) + 0 * 8) = v_stack_m58;
    goto loc_003C4B86;
loc_003C4E00:
loc_003C4E05:
    *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 643) = 0;
    result = KiFastExitThreadWait(*(unsigned __int64 *)(gs_base + (0 + 32)), *(unsigned __int64 *)(gs_base + (0 + 392)), (unsigned int)((unsigned int)(v_stack_p8)), v_stack_m50);
    goto loc_003C4CE7;
loc_003C4E25:
    result = KiRaiseIrqlProcessIrqlFlags(257, (unsigned __int8)(result), (unsigned int)((unsigned int)(v_stack_p8)), v_stack_m50);
    goto loc_003C4D2C;
loc_003C4E34:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 12590206)))) & (64)) == 0) goto loc_003C4BFF;
    result = KiCheckVpBackingLongSpinWaitHypercall(257, (unsigned __int8)(result), (unsigned int)((unsigned int)(v_stack_p8)), v_stack_m50);
    if ((unsigned __int8)(result) == 0) goto loc_003C4BFF;
    result = HvlNotifyLongSpinWait(0, (unsigned __int8)(result), (unsigned int)((unsigned int)(v_stack_p8)), v_stack_m50);
    goto loc_003C4C01;
loc_003C4E5C:
loc_003C4E63:
    if ((unsigned __int8)(result) != 0) goto loc_003C4E63;
    if (condition_is_above_or_equal) goto loc_003C4B9F;
    result = KiRemoveSystemWorkPriorityKick(0, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)(v_stack_p8)))))), (unsigned int)((unsigned int)(v_stack_p8)), v_stack_m50);
    goto loc_003C4B9F;
loc_003C4E84:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 486)) != ((unsigned __int16)(v_stack_p18))) goto loc_003C4C19;
    if (257 >= 1) goto loc_003C4C19;
    result = KiReleaseThreadLockLowerIrql(*(unsigned __int64 *)(gs_base + (0 + 392)), 1, (unsigned int)((unsigned int)(v_stack_p8)), v_stack_m50);
    a3 = 0;
    a2 = 0;
    a1 = 0;
    result = KiDeliverApc(a1, a2, a3, v_stack_m50);
    if ((*(unsigned int *)(v_rip + 12590687)) != ((unsigned int)(v_stack_p18))) goto loc_003C4ED9;
loc_003C4EC3:
    *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) = 257;
    goto loc_003C4BD4;
loc_003C4ECF:
    goto loc_003C4CF7;
loc_003C4ED9:
    result = KiRaiseIrqlProcessIrqlFlags(2, (unsigned __int8)((unsigned int)(v_stack_m58)), a3, v_stack_m50);
    goto loc_003C4EC3;
loc_003C4EE3:
    v_r14 = 0;
    if (0 == 0) goto loc_003C4C31;
    v_stack_m48 = 0;
    result = KiPerformWaitDeferredWork(*(unsigned __int64 *)(gs_base + (0 + 392)), (unsigned int)((unsigned int)(v_stack_p8)), 1, v_stack_m48);
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 64) = 0;
    if ((unsigned int)(result) != 0) goto loc_003C4F2F;
    if ((*(unsigned int *)(v_rip + 12590605)) != 0) {
        a1 = (unsigned int)(v_stack_m58);
        a2 = 257;
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, 1, v_stack_m48);
    }
loc_003C4F25:
    goto loc_003C4CE7;
loc_003C4F2F:
    result = KiProcessDeferredReadyList(*(unsigned __int64 *)(gs_base + (0 + 32)), v_stack_m48, 192, v_stack_m48);
    goto loc_003C4F25;
loc_003C4F46:
    goto loc_003C4E05;
}
```

## 5. (Beta) C Style

```c
int64_t KeWaitForAlertByThreadId(uint8_t Arg1, int64_t Arg2, int64_t Arg3)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint32_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_p18;
    uint32_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p18 = Arg3;
    local_rsp = (local_rsp) - (80);
    local_r10 = 0;
    v_stack_m50 = 0;
    v_stack_p20 = 0;
    v_stack_m58 = 0;
    if (condition_is_below) goto loc_003C4ECF;
    if (Arg2 != 0) goto loc_003C4DDC;
loc_003C4B66:
    if (Arg3 == 0) goto loc_003C4BA3;
    if (Arg1 != 1) goto loc_003C4BA3;
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x320) != 0) goto loc_003C4DAF;
loc_003C4B86:
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8) != 0) goto loc_003C4E5C;
loc_003C4B9F:
    v_stack_m58 = 1;
loc_003C4BA3:
    Arg3 = 0;
    v_stack_m68 = v_stack_p20;
    result = KiCheckWaitNext(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, Arg3, v_stack_m50);
loc_003C4BC0:
    local_r15 = 0;
    v_stack_m48 = 0;
loc_003C4BD4:
    *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x70) = 0;
    *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x187) = Arg1;
loc_003C4BE6:
    if (condition_is_above_or_equal) goto loc_003C4C0C;
loc_003C4BEF:
    local_r14 = (uint32_t)((0) + 1);
    if (((*(uint32_t *)(v_rip + 0xC006B3)) & ((uint32_t)(local_r14))) == 0) goto loc_003C4E34;
loc_003C4BFF:
loc_003C4C01:
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x40) == 0) goto loc_003C4BE6;
    goto loc_003C4BEF;
loc_003C4C0C:
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xC1)) != 0) goto loc_003C4E84;
loc_003C4C19:
    if (((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xC2)) & (2)) != 0) goto loc_003C4EE3;
    local_r14 = 0;
loc_003C4C31:
    *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x184) = 5;
    *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x283) = 37;
    *(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x1B4) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x40))));
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x40) = 0;
    if (condition_is_below) goto loc_003C4E00;
    if (((uint32_t)((uint32_t)(v_stack_p20))) == 2) goto loc_003C4D38;
    if ((uint32_t)((uint32_t)(v_stack_p20)) == 0) goto loc_003C4CA2;
    if (v_stack_m50 == 0) goto loc_003C4F46;
loc_003C4C95:
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)))) > v_stack_m50) goto loc_003C4F46;
loc_003C4CA2:
    local_r10 = 0;
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x140 + 0x20) = v_stack_p18;
    *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x140 + 0x11) = 5;
    v_stack_m60 = 0;
    *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x24B) = 1;
    v_stack_m68 = (uint32_t)((uint32_t)((uint32_t)(result)));
    result = KiCommitThreadWait(*(uint64_t *)(gs_base + (0 + 0x188)), *(uint64_t *)(gs_base + (0 + 0x188)) + 320, (uint32_t)(v_stack_p20), v_stack_m50);
    local_r14 = 0;
    *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x283) = 0;
    if (((uint32_t)(result)) == 256) goto loc_003C4D12;
loc_003C4CE7:
    if ((uint32_t)((uint32_t)(v_stack_m58)) != 0) {
        Arg2 = v_stack_p18;
        Arg1 = *(uint64_t *)(gs_base + (0 + 0x188));
        result = KiAbUmPostWait(Arg1, Arg2, (uint32_t)(v_stack_p20), v_stack_m50);
    }
    local_rsp = (local_rsp) + (80);
    return (uint32_t)((uint32_t)(result));
loc_003C4D12:
    if ((*(uint32_t *)(v_rip + 0xC01FFA)) != 0) goto loc_003C4E25;
loc_003C4D2C:
    *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) = (uint8_t)(v_cr8);
    goto loc_003C4BC0;
loc_003C4D38:
    Arg1 = (*(uint64_t *)(Arg1)) - (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xF8));
    Arg1 = (Arg1) - (*(uint64_t *)(2));
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x187)) == 0) goto loc_003C4C95;
    if ((*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x1E4)) != 0) goto loc_003C4C95;
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186)) != 0) goto loc_003C4C95;
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xC0)) != 0) goto loc_003C4C95;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x3B8))) == 0) goto loc_003C4C95;
    goto loc_003C4C95;
loc_003C4DAF:
loc_003C4DB2:
    if (0 >= 8) goto loc_003C4B86;
    v_stack_m58 = *(uint64_t *)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x3B8)) + 0x0 * 8);
    result = (*(uint64_t *)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x3B8)) + 0x0 * 8)) & (v_stack_m50);
    if (result == v_stack_p18) goto loc_003C4DEF;
    Arg1 = (uint32_t)((0) + ((uint32_t)(v_cr8)));
    goto loc_003C4DB2;
loc_003C4DDC:
    if ((*(uint64_t *)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x3B8)))) != 0) goto loc_003C4B66;
    goto loc_003C4CF7;
loc_003C4DEF:
    *(uint64_t *)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x3B8)) + 0x0 * 8) = v_stack_m58;
    goto loc_003C4B86;
loc_003C4E00:
loc_003C4E05:
    *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x283) = 0;
    result = KiFastExitThreadWait(*(uint64_t *)(gs_base + (0 + 0x20)), *(uint64_t *)(gs_base + (0 + 0x188)), (uint32_t)((uint32_t)(v_stack_p8)), v_stack_m50);
    goto loc_003C4CE7;
loc_003C4E25:
    result = KiRaiseIrqlProcessIrqlFlags(257, (uint8_t)(result), (uint32_t)((uint32_t)(v_stack_p8)), v_stack_m50);
    goto loc_003C4D2C;
loc_003C4E34:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC01C7E)))) & (64)) == 0) goto loc_003C4BFF;
    result = KiCheckVpBackingLongSpinWaitHypercall(257, (uint8_t)(result), (uint32_t)((uint32_t)(v_stack_p8)), v_stack_m50);
    if ((uint8_t)(result) == 0) goto loc_003C4BFF;
    result = HvlNotifyLongSpinWait(0, (uint8_t)(result), (uint32_t)((uint32_t)(v_stack_p8)), v_stack_m50);
    goto loc_003C4C01;
loc_003C4E5C:
loc_003C4E63:
    if ((uint8_t)(result) != 0) goto loc_003C4E63;
    if (condition_is_above_or_equal) goto loc_003C4B9F;
    result = KiRemoveSystemWorkPriorityKick(0, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)(v_stack_p8)))))), (uint32_t)((uint32_t)(v_stack_p8)), v_stack_m50);
    goto loc_003C4B9F;
loc_003C4E84:
    if ((*(uint16_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x1E6)) != ((uint16_t)(v_stack_p18))) goto loc_003C4C19;
    if (257 >= 1) goto loc_003C4C19;
    result = KiReleaseThreadLockLowerIrql(*(uint64_t *)(gs_base + (0 + 0x188)), 1, (uint32_t)((uint32_t)(v_stack_p8)), v_stack_m50);
    Arg3 = 0;
    Arg2 = 0;
    Arg1 = 0;
    result = KiDeliverApc(Arg1, Arg2, Arg3, v_stack_m50);
    if ((*(uint32_t *)(v_rip + 0xC01E5F)) != ((uint32_t)(v_stack_p18))) goto loc_003C4ED9;
loc_003C4EC3:
    *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) = 257;
    goto loc_003C4BD4;
loc_003C4ECF:
    goto loc_003C4CF7;
loc_003C4ED9:
    result = KiRaiseIrqlProcessIrqlFlags(2, (uint8_t)((uint32_t)(v_stack_m58)), Arg3, v_stack_m50);
    goto loc_003C4EC3;
loc_003C4EE3:
    local_r14 = 0;
    if (0 == 0) goto loc_003C4C31;
    v_stack_m48 = 0;
    result = KiPerformWaitDeferredWork(*(uint64_t *)(gs_base + (0 + 0x188)), (uint32_t)((uint32_t)(v_stack_p8)), 1, v_stack_m48);
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x40) = 0;
    if ((uint32_t)(result) != 0) goto loc_003C4F2F;
    if ((*(uint32_t *)(v_rip + 0xC01E0D)) != 0) {
        Arg1 = (uint32_t)(v_stack_m58);
        Arg2 = 257;
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, 1, v_stack_m48);
    }
loc_003C4F25:
    goto loc_003C4CE7;
loc_003C4F2F:
    result = KiProcessDeferredReadyList(*(uint64_t *)(gs_base + (0 + 0x20)), v_stack_m48, 192, v_stack_m48);
    goto loc_003C4F25;
loc_003C4F46:
    goto loc_003C4E05;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003C4B14&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
