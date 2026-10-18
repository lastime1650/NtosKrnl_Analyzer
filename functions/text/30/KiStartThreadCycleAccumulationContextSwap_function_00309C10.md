# KiStartThreadCycleAccumulationContextSwap

- RVA: `0x00309C10`–`0x0030A62A` (길이 `2,586` bytes)
- VA: `0x0000000140309C10`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00073BCC`
- 디코드: `616`개 명령, `2,586/2,586` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **19**; 고유 호출 대상: **9**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **16**

### Outgoing calls
- `0x0030A0D3` → [KiRemoveSystemWorkPriorityKick](../26/KiRemoveSystemWorkPriorityKick_function_002631D0.md) (function, `0x002631D0`)
- `0x0030A0E6` → [KiInsertDeferredPreemptionApc](KiInsertDeferredPreemptionApc_function_0030A8E8.md) (function, `0x0030A8E8`)
- `0x0030A119` → [HalpDisableInterrupts](../25/HalpDisableInterrupts_function_002521A0.md) (function, `0x002521A0`)
- `0x0030A173` → [HalpInterruptSendIpi](../25/HalpInterruptSendIpi_function_00252310.md) (function, `0x00252310`)
- `0x0030A19B` → [KiRemoveSystemWorkPriorityKick](../26/KiRemoveSystemWorkPriorityKick_function_002631D0.md) (function, `0x002631D0`)
- `0x0030A1BE` → [HalpTimerGetInternalData](../20/HalpTimerGetInternalData_function_00209500.md) (function, `0x00209500`)
- `0x0030A282` → [HalpTimerScaleCounter](../37/HalpTimerScaleCounter_function_0037B354.md) (function, `0x0037B354`)
- `0x0030A2B3` → [HalpTimerScaleCounter](../37/HalpTimerScaleCounter_function_0037B354.md) (function, `0x0037B354`)
- `0x0030A2DC` → [HalpTimerGetInternalData](../20/HalpTimerGetInternalData_function_00209500.md) (function, `0x00209500`)
- `0x0030A2F1` → [HalpHpetQueryCounter](../37/HalpHpetQueryCounter_function_00379660.md) (function, `0x00379660`)
- `0x0030A418` → [HvlpGetRegister64](../37/HvlpGetRegister64_function_00379050.md) (function, `0x00379050`)
- `0x0030A46C` → [HalpTimerGetInternalData](../20/HalpTimerGetInternalData_function_00209500.md) (function, `0x00209500`)
- `0x0030A481` → [HalpHpetQueryCounter](../37/HalpHpetQueryCounter_function_00379660.md) (function, `0x00379660`)
- `0x0030A542` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0030A58B` → [HvlpGetRegister64](../37/HvlpGetRegister64_function_00379050.md) (function, `0x00379050`)
- `0x0030A5AB` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0030A5BB` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0030A5C9` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0030A5DF` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [SwapContext](../6B/SwapContext_function_006B9820.md) at `0x006B9866`

### Static image references
- `0x00309C4A` → RVA `0x00FC3FD0` (`.data`; read)
- `0x00309C65` → RVA `0x00FC40E0` (`.data`; read)
- `0x00309C8E` → RVA `0x0041FD10` (`HalpTscQueryCounterOrdered`; read)
- `0x00309CD0` → RVA `0x00FC3FC8` (`.data`; read)
- `0x00309D20` → RVA `0x00FC6A95` (`ALMOSTRO`; read)
- `0x00309D74` → RVA `0x00FC6BC6` (`ALMOSTRO`; read)
- `0x00309D88` → RVA `0x00FC7318` (`ALMOSTRO`; read)
- `0x00309EB2` → RVA `0x00E66908` (`.data`; read)
- `0x00309EBC` → RVA `0x00F10E80` (`.data`; read)
- `0x00309F10` → RVA `0x00FC6ADE` (`ALMOSTRO`; read)
- `0x00309FEE` → RVA `0x00378F50` (`HalpHvCounterQueryCounter`; read)
- `0x00309FFE` → RVA `0x00E11760` (`.data`; read)
- `0x0030A00E` → RVA `0x002DDBC0` (`HvlGetReferenceTimeUsingTscPage`; read)
- `0x0030A02F` → RVA `0x00FC6D88` (`ALMOSTRO`; read)
- `0x0030A103` → RVA `0x00FC6BC5` (`ALMOSTRO`; read)
- `0x0030A2CB` → RVA `0x00379660` (`HalpHpetQueryCounter`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00309C10  40 55                           push rbp
00309C12  53                              push rbx
00309C13  56                              push rsi
00309C14  57                              push rdi
00309C15  41 54                           push r12
00309C17  41 55                           push r13
00309C19  41 56                           push r14
00309C1B  41 57                           push r15
00309C1D  48 8B EC                        mov rbp, rsp
00309C20  48 83 EC 68                     sub rsp, 0x68
00309C24  45 33 ED                        xor r13d, r13d
00309C27  4C 8B F2                        mov r14, rdx
00309C2A  48 8B F1                        mov rsi, rcx
00309C2D  41 8B FD                        mov edi, r13d
00309C30  41 8B DD                        mov ebx, r13d
00309C33  45 8B E5                        mov r12d, r13d
00309C36  45 8B DD                        mov r11d, r13d
00309C39  45 8D 7D 01                     lea r15d, [r13 + 1]
00309C3D  44 38 A9 DC 86 00 00            cmp byte ptr [rcx + 0x86dc], r13b
00309C44  0F 84 6B 01 00 00               je 0x140309db5
00309C4A  4C 8B 2D 7F A3 CB 00            mov r13, qword ptr [rip + 0xcba37f]
00309C51  41 B9 80 96 98 00               mov r9d, 0x989680
00309C57  41 83 BD E4 00 00 00 05         cmp dword ptr [r13 + 0xe4], 5
00309C5F  0F 85 5B 03 00 00               jne 0x140309fc0
00309C65  4C 39 1D 74 A4 CB 00            cmp qword ptr [rip + 0xcba474], r11
00309C6C  41 8B D9                        mov ebx, r9d
00309C6F  0F 84 38 05 00 00               je 0x14030a1ad
00309C75  41 F7 85 E0 00 00 00 00 00 01 00  test dword ptr [r13 + 0xe0], 0x10000
00309C80  0F 85 C4 06 00 00               jne 0x14030a34a
00309C86  49 8B 4D 48                     mov rcx, qword ptr [r13 + 0x48]
00309C8A  49 8B 45 70                     mov rax, qword ptr [r13 + 0x70]
00309C8E  48 8D 15 7B 60 11 00            lea rdx, [rip + 0x11607b]
00309C95  48 3B C2                        cmp rax, rdx
00309C98  0F 85 2B 09 00 00               jne 0x14030a5c9
00309C9E  89 7D 50                        mov dword ptr [rbp + 0x50], edi
00309CA1  0F 01 F9                        rdtscp
00309CA4  4C 8D 45 50                     lea r8, [rbp + 0x50]
00309CA8  48 C1 E2 20                     shl rdx, 0x20
00309CAC  41 89 08                        mov dword ptr [r8], ecx
00309CAF  48 0B D0                        or rdx, rax
00309CB2  48 8B 05 27 A4 CB 00            mov rax, qword ptr [rip + 0xcba427]
00309CB9  48 B9 B8 03 00 00 80 F7 FF FF   movabs rcx, 0xfffff780000003b8
00309CC3  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00309CC7  48 8B 39                        mov rdi, qword ptr [rcx]
00309CCA  48 F7 E2                        mul rdx
00309CCD  48 03 FA                        add rdi, rdx
00309CD0  48 8B 05 F1 A2 CB 00            mov rax, qword ptr [rip + 0xcba2f1]
00309CD7  4C 3B E8                        cmp r13, rax
00309CDA  0F 85 B2 05 00 00               jne 0x14030a292
00309CE0  0F B6 8E AC 00 00 00            movzx ecx, byte ptr [rsi + 0xac]
00309CE7  45 33 ED                        xor r13d, r13d
00309CEA  48 8B 86 B0 00 00 00            mov rax, qword ptr [rsi + 0xb0]
00309CF1  48 8B D7                        mov rdx, rdi
00309CF4  4C 89 6D D8                     mov qword ptr [rbp - 0x28], r13
00309CF8  84 C9                           test cl, cl
00309CFA  74 03                           je 0x140309cff
00309CFC  48 D3 E2                        shl rdx, cl
00309CFF  48 F7 E2                        mul rdx
00309D02  4C 8B E7                        mov r12, rdi
00309D05  48 8B DA                        mov rbx, rdx
00309D08  48 89 55 D8                     mov qword ptr [rbp - 0x28], rdx
00309D0C  48 8B 96 F8 86 00 00            mov rdx, qword ptr [rsi + 0x86f8]
00309D13  4C 8B DB                        mov r11, rbx
00309D16  4C 2B 9E 80 86 00 00            sub r11, qword ptr [rsi + 0x8680]
00309D1D  4C 2B E2                        sub r12, rdx
00309D20  44 38 2D 6E CD CB 00            cmp byte ptr [rip + 0xcbcd6e], r13b
00309D27  0F 84 88 00 00 00               je 0x140309db5
00309D2D  48 B8 00 03 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000300
00309D37  4C 39 28                        cmp qword ptr [rax], r13
00309D3A  74 79                           je 0x140309db5
00309D3C  A0 69 03 00 00 80 F7 FF FF      movabs al, byte ptr [0xfffff78000000369]
00309D45  49 B9 60 03 00 00 80 F7 FF FF   movabs r9, 0xfffff78000000360
00309D4F  0F B6 C8                        movzx ecx, al
00309D52  4C 89 6D C0                     mov qword ptr [rbp - 0x40], r13
00309D56  84 C0                           test al, al
00309D58  4C 89 6D C8                     mov qword ptr [rbp - 0x38], r13
00309D5C  4C 8B C7                        mov r8, rdi
00309D5F  4D 8B 09                        mov r9, qword ptr [r9]
00309D62  49 8B C1                        mov rax, r9
00309D65  0F 84 3A 04 00 00               je 0x14030a1a5
00309D6B  48 D3 E2                        shl rdx, cl
00309D6E  48 F7 E2                        mul rdx
00309D71  49 D3 E0                        shl r8, cl
00309D74  0F BE 0D 4B CE CB 00            movsx ecx, byte ptr [rip + 0xcbce4b]
00309D7B  4C 8B D2                        mov r10, rdx
00309D7E  48 89 55 C0                     mov qword ptr [rbp - 0x40], rdx
00309D82  49 8B C1                        mov rax, r9
00309D85  49 F7 E0                        mul r8
00309D88  48 8B 05 89 D5 CB 00            mov rax, qword ptr [rip + 0xcbd589]
00309D8F  4C 8B CA                        mov r9, rdx
00309D92  48 89 55 C8                     mov qword ptr [rbp - 0x38], rdx
00309D96  49 F7 E2                        mul r10
00309D99  48 8B 05 78 D5 CB 00            mov rax, qword ptr [rip + 0xcbd578]
00309DA0  4C 8B D2                        mov r10, rdx
00309DA3  49 F7 E1                        mul r9
00309DA6  49 D3 EA                        shr r10, cl
00309DA9  48 D3 EA                        shr rdx, cl
00309DAC  41 2B D2                        sub edx, r10d
00309DAF  0F 85 EF 02 00 00               jne 0x14030a0a4
00309DB5  48 8B 86 00 87 00 00            mov rax, qword ptr [rsi + 0x8700]
00309DBC  49 03 C4                        add rax, r12
00309DBF  48 89 86 00 87 00 00            mov qword ptr [rsi + 0x8700], rax
00309DC6  48 8B 86 78 87 00 00            mov rax, qword ptr [rsi + 0x8778]
00309DCD  49 03 C3                        add rax, r11
00309DD0  48 89 86 78 87 00 00            mov qword ptr [rsi + 0x8778], rax
00309DD7  48 89 BE F8 86 00 00            mov qword ptr [rsi + 0x86f8], rdi
00309DDE  48 89 9E 80 86 00 00            mov qword ptr [rsi + 0x8680], rbx
00309DE5  45 0F B6 4E 02                  movzx r9d, byte ptr [r14 + 2]
00309DEA  41 F6 C1 B6                     test r9b, 0xb6
00309DEE  0F 84 A9 01 00 00               je 0x140309f9d
00309DF4  41 F6 C1 20                     test r9b, 0x20
00309DF8  0F 84 85 00 00 00               je 0x140309e83
00309DFE  48 8B 86 B0 89 00 00            mov rax, qword ptr [rsi + 0x89b0]
00309E05  4C 8B 86 B8 89 00 00            mov r8, qword ptr [rsi + 0x89b8]
00309E0C  48 85 C0                        test rax, rax
00309E0F  0F 84 DB 07 00 00               je 0x14030a5f0
00309E15  4D 85 C0                        test r8, r8
00309E18  0F 84 D2 07 00 00               je 0x14030a5f0
00309E1E  41 80 78 70 00                  cmp byte ptr [r8 + 0x70], 0
00309E23  75 14                           jne 0x140309e39
00309E25  45 8B 40 50                     mov r8d, dword ptr [r8 + 0x50]
00309E29  8B 88 10 02 00 00               mov ecx, dword ptr [rax + 0x210]
00309E2F  44 3B C1                        cmp r8d, ecx
00309E32  72 0C                           jb 0x140309e40
00309E34  44 8B C1                        mov r8d, ecx
00309E37  EB 07                           jmp 0x140309e40
00309E39  45 8B 80 84 00 00 00            mov r8d, dword ptr [r8 + 0x84]
00309E40  41 8B CD                        mov ecx, r13d
00309E43  48 8D 96 6A 8A 00 00            lea rdx, [rsi + 0x8a6a]
00309E4A  0F B7 02                        movzx eax, word ptr [rdx]
00309E4D  44 3B C0                        cmp r8d, eax
00309E50  76 0B                           jbe 0x140309e5d
00309E52  FF C1                           inc ecx
00309E54  48 83 C2 02                     add rdx, 2
00309E58  83 F9 03                        cmp ecx, 3
00309E5B  72 ED                           jb 0x140309e4a
00309E5D  80 BE 08 8A 00 00 00            cmp byte ptr [rsi + 0x8a08], 0
00309E64  49 8B C5                        mov rax, r13
00309E67  0F 95 C0                        setne al
00309E6A  48 8D 04 48                     lea rax, [rax + rcx*2]
00309E6E  48 8D 80 F0 10 00 00            lea rax, [rax + 0x10f0]
00309E75  48 8B 0C C6                     mov rcx, qword ptr [rsi + rax*8]
00309E79  48 8D 14 C6                     lea rdx, [rsi + rax*8]
00309E7D  49 03 CB                        add rcx, r11
00309E80  48 89 0A                        mov qword ptr [rdx], rcx
00309E83  41 F6 C1 40                     test r9b, 0x40
00309E87  74 10                           je 0x140309e99
00309E89  49 8B 86 C8 03 00 00            mov rax, qword ptr [r14 + 0x3c8]
00309E90  48 85 C0                        test rax, rax
00309E93  74 04                           je 0x140309e99
00309E95  44 88 78 40                     mov byte ptr [rax + 0x40], r15b
00309E99  C6 46 20 00                     mov byte ptr [rsi + 0x20], 0
00309E9D  4D 8B 86 68 01 00 00            mov r8, qword ptr [r14 + 0x168]
00309EA4  4D 85 C0                        test r8, r8
00309EA7  74 46                           je 0x140309eef
00309EA9  4D 8B 48 20                     mov r9, qword ptr [r8 + 0x20]
00309EAD  4D 85 C9                        test r9, r9
00309EB0  74 31                           je 0x140309ee3
00309EB2  8B 05 50 CA B5 00               mov eax, dword ptr [rip + 0xb5ca50]
00309EB8  85 C0                           test eax, eax
00309EBA  74 27                           je 0x140309ee3
00309EBC  4C 8D 15 BD 6F C0 00            lea r10, [rip + 0xc06fbd]
00309EC3  8B D8                           mov ebx, eax
00309EC5  4D 8D 58 30                     lea r11, [r8 + 0x30]
00309EC9  4D 85 CF                        test r15, r9
00309ECC  0F 85 29 07 00 00               jne 0x14030a5fb
00309ED2  4D 03 FF                        add r15, r15
00309ED5  49 83 C3 18                     add r11, 0x18
00309ED9  49 83 C2 04                     add r10, 4
00309EDD  48 83 EB 01                     sub rbx, 1
00309EE1  75 E6                           jne 0x140309ec9
00309EE3  41 8B 40 10                     mov eax, dword ptr [r8 + 0x10]
00309EE7  A8 01                           test al, 1
00309EE9  0F 85 20 07 00 00               jne 0x14030a60f
00309EEF  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
00309EF8  4C 8B 81 B8 8E 00 00            mov r8, qword ptr [rcx + 0x8eb8]
00309EFF  4D 85 C0                        test r8, r8
00309F02  0F 85 AD 01 00 00               jne 0x14030a0b5
00309F08  FB                              sti
00309F09  41 F6 46 02 04                  test byte ptr [r14 + 2], 4
00309F0E  75 3C                           jne 0x140309f4c
00309F10  80 3D C7 CB CB 00 00            cmp byte ptr [rip + 0xcbcbc7], 0
00309F17  74 17                           je 0x140309f30
00309F19  0F 31                           rdtsc
00309F1B  48 C1 E2 20                     shl rdx, 0x20
00309F1F  48 0B C2                        or rax, rdx
00309F22  4D 89 AE 38 04 00 00            mov qword ptr [r14 + 0x438], r13
00309F29  49 89 86 30 04 00 00            mov qword ptr [r14 + 0x430], rax
00309F30  80 7E 06 00                     cmp byte ptr [rsi + 6], 0
00309F34  0F 85 B6 01 00 00               jne 0x14030a0f0
00309F3A  48 83 C4 68                     add rsp, 0x68
00309F3E  41 5F                           pop r15
00309F40  41 5E                           pop r14
00309F42  41 5D                           pop r13
00309F44  41 5C                           pop r12
00309F46  5F                              pop rdi
00309F47  5E                              pop rsi
00309F48  5B                              pop rbx
00309F49  5D                              pop rbp
00309F4A  C3                              ret
00309F4B  CC                              int3
00309F4C  41 8B 46 78                     mov eax, dword ptr [r14 + 0x78]
00309F50  0F BA E0 0B                     bt eax, 0xb
00309F54  0F 82 83 01 00 00               jb 0x14030a0dd
00309F5A  0F BA E0 0A                     bt eax, 0xa
00309F5E  72 B0                           jb 0x140309f10
00309F60  41 80 BE C3 00 00 00 10         cmp byte ptr [r14 + 0xc3], 0x10
00309F68  7D A6                           jge 0x140309f10
00309F6A  0F BA E0 09                     bt eax, 9
00309F6E  72 A0                           jb 0x140309f10
00309F70  49 8B 46 68                     mov rax, qword ptr [r14 + 0x68]
00309F74  48 85 C0                        test rax, rax
00309F77  74 97                           je 0x140309f10
00309F79  8B 8E D8 00 00 00               mov ecx, dword ptr [rsi + 0xd8]
00309F7F  48 03 C8                        add rcx, rax
00309F82  F6 41 70 02                     test byte ptr [rcx + 0x70], 2
00309F86  0F 85 51 01 00 00               jne 0x14030a0dd
00309F8C  48 8B 89 A0 01 00 00            mov rcx, qword ptr [rcx + 0x1a0]
00309F93  48 85 C9                        test rcx, rcx
00309F96  75 EA                           jne 0x140309f82
00309F98  E9 73 FF FF FF                  jmp 0x140309f10
00309F9D  90                              nop
00309F9E  FE 4E 20                        dec byte ptr [rsi + 0x20]
00309FA1  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
00309FAA  4C 8B 81 B8 8E 00 00            mov r8, qword ptr [rcx + 0x8eb8]
00309FB1  4D 85 C0                        test r8, r8
00309FB4  0F 85 C3 01 00 00               jne 0x14030a17d
00309FBA  FB                              sti
00309FBB  E9 70 FF FF FF                  jmp 0x140309f30
00309FC0  41 83 BD DC 00 00 00 40         cmp dword ptr [r13 + 0xdc], 0x40
00309FC8  49 8B 9D C0 00 00 00            mov rbx, qword ptr [r13 + 0xc0]
00309FCF  0F 85 EB 02 00 00               jne 0x14030a2c0
00309FD5  41 F7 85 E0 00 00 00 00 00 01 00  test dword ptr [r13 + 0xe0], 0x10000
00309FE0  0F 85 F5 03 00 00               jne 0x14030a3db
00309FE6  49 8B 4D 48                     mov rcx, qword ptr [r13 + 0x48]
00309FEA  49 8B 55 70                     mov rdx, qword ptr [r13 + 0x70]
00309FEE  48 8D 05 5B EF 06 00            lea rax, [rip + 0x6ef5b]
00309FF5  48 3B D0                        cmp rdx, rax
00309FF8  0F 85 41 05 00 00               jne 0x14030a53f
00309FFE  48 8B 05 5B 77 B0 00            mov rax, qword ptr [rip + 0xb0775b]
0030A005  48 85 C0                        test rax, rax
0030A008  0F 84 2B 04 00 00               je 0x14030a439
0030A00E  48 8D 0D AB 3B FD FF            lea rcx, [rip - 0x2c455]
0030A015  48 3B C1                        cmp rax, rcx
0030A018  0F 85 CB 05 00 00               jne 0x14030a5e9
0030A01E  48 89 7D B8                     mov qword ptr [rbp - 0x48], rdi
0030A022  49 BA 94 02 00 00 80 F7 FF FF   movabs r10, 0xfffff78000000294
0030A02C  89 7D 58                        mov dword ptr [rbp + 0x58], edi
0030A02F  48 8B 05 52 CD CB 00            mov rax, qword ptr [rip + 0xcbcd52]
0030A036  44 8B 08                        mov r9d, dword ptr [rax]
0030A039  45 85 C9                        test r9d, r9d
0030A03C  0F 84 CD 03 00 00               je 0x14030a40f
0030A042  41 38 3A                        cmp byte ptr [r10], dil
0030A045  0F 84 A8 03 00 00               je 0x14030a3f3
0030A04B  0F 01 F9                        rdtscp
0030A04E  4C 8D 45 58                     lea r8, [rbp + 0x58]
0030A052  41 89 08                        mov dword ptr [r8], ecx
0030A055  48 C1 E2 20                     shl rdx, 0x20
0030A059  48 0B D0                        or rdx, rax
0030A05C  48 8B 05 25 CD CB 00            mov rax, qword ptr [rip + 0xcbcd25]
0030A063  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0030A067  48 8B 0D 1A CD CB 00            mov rcx, qword ptr [rip + 0xcbcd1a]
0030A06E  48 F7 E2                        mul rdx
0030A071  4C 8B 41 10                     mov r8, qword ptr [rcx + 0x10]
0030A075  48 8B 05 0C CD CB 00            mov rax, qword ptr [rip + 0xcbcd0c]
0030A07C  49 03 D0                        add rdx, r8
0030A07F  48 89 55 B8                     mov qword ptr [rbp - 0x48], rdx
0030A083  8B 08                           mov ecx, dword ptr [rax]
0030A085  41 3B C9                        cmp ecx, r9d
0030A088  75 A5                           jne 0x14030a02f
0030A08A  48 8B 55 B8                     mov rdx, qword ptr [rbp - 0x48]
0030A08E  4D 8B A5 D0 00 00 00            mov r12, qword ptr [r13 + 0xd0]
0030A095  41 B9 80 96 98 00               mov r9d, 0x989680
0030A09B  49 8D 3C 14                     lea rdi, [r12 + rdx]
0030A09F  E9 2C FC FF FF                  jmp 0x140309cd0
0030A0A4  01 96 44 86 00 00               add dword ptr [rsi + 0x8644], edx
0030A0AA  01 96 50 86 00 00               add dword ptr [rsi + 0x8650], edx
0030A0B0  E9 00 FD FF FF                  jmp 0x140309db5
0030A0B5  41 0F 0D 08                     prefetchw byte ptr [r8]
0030A0B9  41 8B 00                        mov eax, dword ptr [r8]
0030A0BC  8B D0                           mov edx, eax
0030A0BE  0F BA F2 15                     btr edx, 0x15
0030A0C2  F0 41 0F B1 10                  lock cmpxchg dword ptr [r8], edx
0030A0C7  75 F3                           jne 0x14030a0bc
0030A0C9  0F BA E0 15                     bt eax, 0x15
0030A0CD  0F 83 35 FE FF FF               jae 0x140309f08
0030A0D3  E8 F8 90 F5 FF                  call 0x1402631d0
0030A0D8  E9 2B FE FF FF                  jmp 0x140309f08
0030A0DD  41 B0 01                        mov r8b, 1
0030A0E0  49 8B D6                        mov rdx, r14
0030A0E3  48 8B CE                        mov rcx, rsi
0030A0E6  E8 FD 07 00 00                  call 0x14030a8e8
0030A0EB  E9 20 FE FF FF                  jmp 0x140309f10
0030A0F0  C6 46 06 00                     mov byte ptr [rsi + 6], 0
0030A0F4  4C 3B 76 18                     cmp r14, qword ptr [rsi + 0x18]
0030A0F8  0F 84 3C FE FF FF               je 0x140309f3a
0030A0FE  33 C0                           xor eax, eax
0030A100  0F 57 C0                        xorps xmm0, xmm0
0030A103  38 05 BC CA CB 00               cmp byte ptr [rip + 0xcbcabc], al
0030A109  F3 0F 7F 45 E4                  movdqu xmmword ptr [rbp - 0x1c], xmm0
0030A10E  74 53                           je 0x14030a163
0030A110  65 4C 8B 04 25 20 00 00 00      mov r8, qword ptr gs:[0x20]
0030A119  E8 82 80 F4 FF                  call 0x1402521a0
0030A11E  41 8B 90 A8 00 00 00            mov edx, dword ptr [r8 + 0xa8]
0030A125  44 0F B6 C8                     movzx r9d, al
0030A129  8B CA                           mov ecx, edx
0030A12B  83 C9 04                        or ecx, 4
0030A12E  41 89 88 A8 00 00 00            mov dword ptr [r8 + 0xa8], ecx
0030A135  85 D2                           test edx, edx
0030A137  75 24                           jne 0x14030a15d
0030A139  B9 15 00 01 C0                  mov ecx, 0xc0010015
0030A13E  0F 32                           rdmsr
0030A140  48 C1 E2 20                     shl rdx, 0x20
0030A144  48 0B C2                        or rax, rdx
0030A147  48 BA 00 00 00 00 01 00 00 00   movabs rdx, 0x100000000
0030A151  48 0B C2                        or rax, rdx
0030A154  48 8B D0                        mov rdx, rax
0030A157  48 C1 EA 20                     shr rdx, 0x20
0030A15B  0F 30                           wrmsr
0030A15D  45 84 C9                        test r9b, r9b
0030A160  74 01                           je 0x14030a163
0030A162  FB                              sti
0030A163  BA 2F 00 00 00                  mov edx, 0x2f
0030A168  C7 45 E0 05 00 00 00            mov dword ptr [rbp - 0x20], 5
0030A16F  48 8D 4D E0                     lea rcx, [rbp - 0x20]
0030A173  E8 98 81 F4 FF                  call 0x140252310
0030A178  E9 BD FD FF FF                  jmp 0x140309f3a
0030A17D  41 0F 0D 08                     prefetchw byte ptr [r8]
0030A181  41 8B 00                        mov eax, dword ptr [r8]
0030A184  8B D0                           mov edx, eax
0030A186  0F BA F2 15                     btr edx, 0x15
0030A18A  F0 41 0F B1 10                  lock cmpxchg dword ptr [r8], edx
0030A18F  75 F3                           jne 0x14030a184
0030A191  0F BA E0 15                     bt eax, 0x15
0030A195  0F 83 1F FE FF FF               jae 0x140309fba
0030A19B  E8 30 90 F5 FF                  call 0x1402631d0
0030A1A0  E9 15 FE FF FF                  jmp 0x140309fba
0030A1A5  48 F7 E2                        mul rdx
0030A1A8  E9 C7 FB FF FF                  jmp 0x140309d74
0030A1AD  41 83 BD DC 00 00 00 40         cmp dword ptr [r13 + 0xdc], 0x40
0030A1B5  0F 85 95 02 00 00               jne 0x14030a450
0030A1BB  49 8B CD                        mov rcx, r13
0030A1BE  E8 3D F3 EF FF                  call 0x140209500
0030A1C3  49 8B 55 70                     mov rdx, qword ptr [r13 + 0x70]
0030A1C7  48 8B C8                        mov rcx, rax
0030A1CA  48 8D 05 7F ED 06 00            lea rax, [rip + 0x6ed7f]
0030A1D1  48 3B D0                        cmp rdx, rax
0030A1D4  0F 85 CE 03 00 00               jne 0x14030a5a8
0030A1DA  48 8B 05 7F 75 B0 00            mov rax, qword ptr [rip + 0xb0757f]
0030A1E1  48 85 C0                        test rax, rax
0030A1E4  0F 84 AB 03 00 00               je 0x14030a595
0030A1EA  48 8D 0D CF 39 FD FF            lea rcx, [rip - 0x2c631]
0030A1F1  48 3B C1                        cmp rax, rcx
0030A1F4  0F 85 CB 03 00 00               jne 0x14030a5c5
0030A1FA  48 89 7D 60                     mov qword ptr [rbp + 0x60], rdi
0030A1FE  49 BA 94 02 00 00 80 F7 FF FF   movabs r10, 0xfffff78000000294
0030A208  89 7D 48                        mov dword ptr [rbp + 0x48], edi
0030A20B  48 8B 05 76 CB CB 00            mov rax, qword ptr [rip + 0xcbcb76]
0030A212  44 8B 08                        mov r9d, dword ptr [rax]
0030A215  45 85 C9                        test r9d, r9d
0030A218  0F 84 64 03 00 00               je 0x14030a582
0030A21E  41 38 3A                        cmp byte ptr [r10], dil
0030A221  0F 84 28 03 00 00               je 0x14030a54f
0030A227  0F 01 F9                        rdtscp
0030A22A  4C 8D 45 48                     lea r8, [rbp + 0x48]
0030A22E  41 89 08                        mov dword ptr [r8], ecx
0030A231  48 C1 E2 20                     shl rdx, 0x20
0030A235  48 0B D0                        or rdx, rax
0030A238  48 8B 05 49 CB CB 00            mov rax, qword ptr [rip + 0xcbcb49]
0030A23F  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
0030A243  48 8B 05 3E CB CB 00            mov rax, qword ptr [rip + 0xcbcb3e]
0030A24A  4C 8B 40 10                     mov r8, qword ptr [rax + 0x10]
0030A24E  48 8B C1                        mov rax, rcx
0030A251  48 F7 E2                        mul rdx
0030A254  48 8B 05 2D CB CB 00            mov rax, qword ptr [rip + 0xcbcb2d]
0030A25B  49 03 D0                        add rdx, r8
0030A25E  48 89 55 60                     mov qword ptr [rbp + 0x60], rdx
0030A262  8B 08                           mov ecx, dword ptr [rax]
0030A264  41 3B C9                        cmp ecx, r9d
0030A267  75 A2                           jne 0x14030a20b
0030A269  48 8B 55 60                     mov rdx, qword ptr [rbp + 0x60]
0030A26D  4D 8B A5 D0 00 00 00            mov r12, qword ptr [r13 + 0xd0]
0030A274  49 8D 0C 14                     lea rcx, [r12 + rdx]
0030A278  4C 8B C3                        mov r8, rbx
0030A27B  49 8B 95 C0 00 00 00            mov rdx, qword ptr [r13 + 0xc0]
0030A282  E8 CD 10 07 00                  call 0x14037b354
0030A287  48 8B F8                        mov rdi, rax
0030A28A  4C 8B CB                        mov r9, rbx
0030A28D  E9 3E FA FF FF                  jmp 0x140309cd0
0030A292  48 85 C0                        test rax, rax
0030A295  0F 84 45 FA FF FF               je 0x140309ce0
0030A29B  83 B8 E4 00 00 00 05            cmp dword ptr [rax + 0xe4], 5
0030A2A2  48 8B D3                        mov rdx, rbx
0030A2A5  4C 8B 80 C0 00 00 00            mov r8, qword ptr [rax + 0xc0]
0030A2AC  48 8B CF                        mov rcx, rdi
0030A2AF  4D 0F 44 C1                     cmove r8, r9
0030A2B3  E8 9C 10 07 00                  call 0x14037b354
0030A2B8  48 8B F8                        mov rdi, rax
0030A2BB  E9 20 FA FF FF                  jmp 0x140309ce0
0030A2C0  4D 8B A5 D0 00 00 00            mov r12, qword ptr [r13 + 0xd0]
0030A2C7  4C 89 65 D0                     mov qword ptr [rbp - 0x30], r12
0030A2CB  4C 8D 25 8E F3 06 00            lea r12, [rip + 0x6f38e]
0030A2D2  49 8B BD C8 00 00 00            mov rdi, qword ptr [r13 + 0xc8]
0030A2D9  49 8B CD                        mov rcx, r13
0030A2DC  E8 1F F2 EF FF                  call 0x140209500
0030A2E1  49 8B 55 70                     mov rdx, qword ptr [r13 + 0x70]
0030A2E5  48 8B C8                        mov rcx, rax
0030A2E8  49 3B D4                        cmp rdx, r12
0030A2EB  0F 85 EB 02 00 00               jne 0x14030a5dc
0030A2F1  E8 6A F3 06 00                  call 0x140379660
0030A2F6  4C 8B D0                        mov r10, rax
0030A2F9  F0 83 0C 24 00                  lock or dword ptr [rsp], 0
0030A2FE  49 8B 85 C8 00 00 00            mov rax, qword ptr [r13 + 0xc8]
0030A305  48 3B F8                        cmp rdi, rax
0030A308  75 C8                           jne 0x14030a2d2
0030A30A  49 8B 8D D0 00 00 00            mov rcx, qword ptr [r13 + 0xd0]
0030A311  4C 8B 65 D0                     mov r12, qword ptr [rbp - 0x30]
0030A315  4C 3B E1                        cmp r12, rcx
0030A318  75 A6                           jne 0x14030a2c0
0030A31A  45 8B 8D DC 00 00 00            mov r9d, dword ptr [r13 + 0xdc]
0030A321  49 8B D7                        mov rdx, r15
0030A324  41 8D 49 FF                     lea ecx, [r9 - 1]
0030A328  48 D3 E2                        shl rdx, cl
0030A32B  49 8B CA                        mov rcx, r10
0030A32E  48 33 CF                        xor rcx, rdi
0030A331  48 85 CA                        test rdx, rcx
0030A334  75 2C                           jne 0x14030a362
0030A336  41 83 F9 40                     cmp r9d, 0x40
0030A33A  74 72                           je 0x14030a3ae
0030A33C  41 8B C9                        mov ecx, r9d
0030A33F  49 8B D7                        mov rdx, r15
0030A342  48 D3 E2                        shl rdx, cl
0030A345  48 FF CA                        dec rdx
0030A348  EB 6B                           jmp 0x14030a3b5
0030A34A  65 8B 04 25 A4 01 00 00         mov eax, dword ptr gs:[0x1a4]
0030A352  41 0F AF 45 50                  imul eax, dword ptr [r13 + 0x50]
0030A357  8B C8                           mov ecx, eax
0030A359  49 03 4D 48                     add rcx, qword ptr [r13 + 0x48]
0030A35D  E9 28 F9 FF FF                  jmp 0x140309c8a
0030A362  41 83 F9 40                     cmp r9d, 0x40
0030A366  75 65                           jne 0x14030a3cd
0030A368  49 C7 C0 FF FF FF FF            mov r8, 0xffffffffffffffff
0030A36F  41 8B C9                        mov ecx, r9d
0030A372  49 8B D7                        mov rdx, r15
0030A375  48 D3 E2                        shl rdx, cl
0030A378  33 C9                           xor ecx, ecx
0030A37A  41 83 F9 40                     cmp r9d, 0x40
0030A37E  48 0F 45 CA                     cmovne rcx, rdx
0030A382  4C 23 C7                        and r8, rdi
0030A385  49 8B D0                        mov rdx, r8
0030A388  48 33 D7                        xor rdx, rdi
0030A38B  49 0B D2                        or rdx, r10
0030A38E  4D 3B D0                        cmp r10, r8
0030A391  73 03                           jae 0x14030a396
0030A393  48 03 D1                        add rdx, rcx
0030A396  F0 49 0F B1 95 C8 00 00 00      lock cmpxchg qword ptr [r13 + 0xc8], rdx
0030A39F  49 8D 3C 14                     lea rdi, [r12 + rdx]
0030A3A3  41 B9 80 96 98 00               mov r9d, 0x989680
0030A3A9  E9 22 F9 FF FF                  jmp 0x140309cd0
0030A3AE  48 C7 C2 FF FF FF FF            mov rdx, 0xffffffffffffffff
0030A3B5  48 F7 D2                        not rdx
0030A3B8  41 B9 80 96 98 00               mov r9d, 0x989680
0030A3BE  48 23 D7                        and rdx, rdi
0030A3C1  49 0B D2                        or rdx, r10
0030A3C4  49 8D 3C 14                     lea rdi, [r12 + rdx]
0030A3C8  E9 03 F9 FF FF                  jmp 0x140309cd0
0030A3CD  41 8B C9                        mov ecx, r9d
0030A3D0  4D 8B C7                        mov r8, r15
0030A3D3  49 D3 E0                        shl r8, cl
0030A3D6  49 FF C8                        dec r8
0030A3D9  EB 94                           jmp 0x14030a36f
0030A3DB  65 8B 04 25 A4 01 00 00         mov eax, dword ptr gs:[0x1a4]
0030A3E3  41 0F AF 45 50                  imul eax, dword ptr [r13 + 0x50]
0030A3E8  8B C8                           mov ecx, eax
0030A3EA  49 03 4D 48                     add rcx, qword ptr [r13 + 0x48]
0030A3EE  E9 F7 FB FF FF                  jmp 0x140309fea
0030A3F3  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
0030A3FC  80 B8 8D 00 00 00 02            cmp byte ptr [rax + 0x8d], 2
0030A403  75 1D                           jne 0x14030a422
0030A405  0F AE E8                        lfence
0030A408  0F 31                           rdtsc
0030A40A  E9 46 FC FF FF                  jmp 0x14030a055
0030A40F  48 8D 55 B8                     lea rdx, [rbp - 0x48]
0030A413  B9 04 00 09 00                  mov ecx, 0x90004
0030A418  E8 33 EC 06 00                  call 0x140379050
0030A41D  E9 68 FC FF FF                  jmp 0x14030a08a
0030A422  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
0030A42B  44 38 B8 8D 00 00 00            cmp byte ptr [rax + 0x8d], r15b
0030A432  75 D4                           jne 0x14030a408
0030A434  0F AE F0                        mfence
0030A437  EB CF                           jmp 0x14030a408
0030A439  B9 20 00 00 40                  mov ecx, 0x40000020
0030A43E  0F 32                           rdmsr
0030A440  48 C1 E2 20                     shl rdx, 0x20
0030A444  48 0B D0                        or rdx, rax
0030A447  E9 42 FC FF FF                  jmp 0x14030a08e
0030A44C  0F 1F 40 00                     nop dword ptr [rax]
0030A450  4D 8B A5 D0 00 00 00            mov r12, qword ptr [r13 + 0xd0]
0030A457  4C 89 65 D0                     mov qword ptr [rbp - 0x30], r12
0030A45B  4C 8D 25 FE F1 06 00            lea r12, [rip + 0x6f1fe]
0030A462  49 8B BD C8 00 00 00            mov rdi, qword ptr [r13 + 0xc8]
0030A469  49 8B CD                        mov rcx, r13
0030A46C  E8 8F F0 EF FF                  call 0x140209500
0030A471  49 8B 55 70                     mov rdx, qword ptr [r13 + 0x70]
0030A475  48 8B C8                        mov rcx, rax
0030A478  49 3B D4                        cmp rdx, r12
0030A47B  0F 85 37 01 00 00               jne 0x14030a5b8
0030A481  E8 DA F1 06 00                  call 0x140379660
0030A486  4C 8B D0                        mov r10, rax
0030A489  F0 83 0C 24 00                  lock or dword ptr [rsp], 0
0030A48E  49 8B 85 C8 00 00 00            mov rax, qword ptr [r13 + 0xc8]
0030A495  48 3B F8                        cmp rdi, rax
0030A498  75 C8                           jne 0x14030a462
0030A49A  49 8B 8D D0 00 00 00            mov rcx, qword ptr [r13 + 0xd0]
0030A4A1  4C 8B 65 D0                     mov r12, qword ptr [rbp - 0x30]
0030A4A5  4C 3B E1                        cmp r12, rcx
0030A4A8  75 A6                           jne 0x14030a450
0030A4AA  45 8B 8D DC 00 00 00            mov r9d, dword ptr [r13 + 0xdc]
0030A4B1  49 8B D7                        mov rdx, r15
0030A4B4  41 8D 49 FF                     lea ecx, [r9 - 1]
0030A4B8  48 D3 E2                        shl rdx, cl
0030A4BB  49 8B CA                        mov rcx, r10
0030A4BE  48 33 CF                        xor rcx, rdi
0030A4C1  48 85 CA                        test rdx, rcx
0030A4C4  75 1B                           jne 0x14030a4e1
0030A4C6  41 83 F9 40                     cmp r9d, 0x40
0030A4CA  75 65                           jne 0x14030a531
0030A4CC  48 C7 C2 FF FF FF FF            mov rdx, 0xffffffffffffffff
0030A4D3  48 F7 D2                        not rdx
0030A4D6  48 23 D7                        and rdx, rdi
0030A4D9  49 0B D2                        or rdx, r10
0030A4DC  E9 93 FD FF FF                  jmp 0x14030a274
0030A4E1  41 83 F9 40                     cmp r9d, 0x40
0030A4E5  75 3C                           jne 0x14030a523
0030A4E7  49 C7 C0 FF FF FF FF            mov r8, 0xffffffffffffffff
0030A4EE  41 8B C9                        mov ecx, r9d
0030A4F1  49 8B D7                        mov rdx, r15
0030A4F4  48 D3 E2                        shl rdx, cl
0030A4F7  33 C9                           xor ecx, ecx
0030A4F9  41 83 F9 40                     cmp r9d, 0x40
0030A4FD  48 0F 45 CA                     cmovne rcx, rdx
0030A501  4C 23 C7                        and r8, rdi
0030A504  49 8B D0                        mov rdx, r8
0030A507  48 33 D7                        xor rdx, rdi
0030A50A  49 0B D2                        or rdx, r10
0030A50D  4D 3B D0                        cmp r10, r8
0030A510  73 03                           jae 0x14030a515
0030A512  48 03 D1                        add rdx, rcx
0030A515  F0 49 0F B1 95 C8 00 00 00      lock cmpxchg qword ptr [r13 + 0xc8], rdx
0030A51E  E9 51 FD FF FF                  jmp 0x14030a274
0030A523  41 8B C9                        mov ecx, r9d
0030A526  4D 8B C7                        mov r8, r15
0030A529  49 D3 E0                        shl r8, cl
0030A52C  49 FF C8                        dec r8
0030A52F  EB BD                           jmp 0x14030a4ee
0030A531  41 8B C9                        mov ecx, r9d
0030A534  49 8B D7                        mov rdx, r15
0030A537  48 D3 E2                        shl rdx, cl
0030A53A  48 FF CA                        dec rdx
0030A53D  EB 94                           jmp 0x14030a4d3
0030A53F  48 8B C2                        mov rax, rdx
0030A542  E8 89 05 3B 00                  call 0x1406baad0
0030A547  48 8B D0                        mov rdx, rax
0030A54A  E9 3F FB FF FF                  jmp 0x14030a08e
0030A54F  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
0030A558  80 B8 8D 00 00 00 02            cmp byte ptr [rax + 0x8d], 2
0030A55F  75 0A                           jne 0x14030a56b
0030A561  0F AE E8                        lfence
0030A564  0F 31                           rdtsc
0030A566  E9 C6 FC FF FF                  jmp 0x14030a231
0030A56B  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
0030A574  44 38 B8 8D 00 00 00            cmp byte ptr [rax + 0x8d], r15b
0030A57B  75 E7                           jne 0x14030a564
0030A57D  0F AE F0                        mfence
0030A580  EB E2                           jmp 0x14030a564
0030A582  48 8D 55 60                     lea rdx, [rbp + 0x60]
0030A586  B9 04 00 09 00                  mov ecx, 0x90004
0030A58B  E8 C0 EA 06 00                  call 0x140379050
0030A590  E9 D4 FC FF FF                  jmp 0x14030a269
0030A595  B9 20 00 00 40                  mov ecx, 0x40000020
0030A59A  0F 32                           rdmsr
0030A59C  48 C1 E2 20                     shl rdx, 0x20
0030A5A0  48 0B D0                        or rdx, rax
0030A5A3  E9 C5 FC FF FF                  jmp 0x14030a26d
0030A5A8  48 8B C2                        mov rax, rdx
0030A5AB  E8 20 05 3B 00                  call 0x1406baad0
0030A5B0  48 8B D0                        mov rdx, rax
0030A5B3  E9 B5 FC FF FF                  jmp 0x14030a26d
0030A5B8  48 8B C2                        mov rax, rdx
0030A5BB  E8 10 05 3B 00                  call 0x1406baad0
0030A5C0  E9 C1 FE FF FF                  jmp 0x14030a486
0030A5C5  33 C9                           xor ecx, ecx
0030A5C7  EB E2                           jmp 0x14030a5ab
0030A5C9  E8 02 05 3B 00                  call 0x1406baad0
0030A5CE  48 8B D0                        mov rdx, rax
0030A5D1  41 B9 80 96 98 00               mov r9d, 0x989680
0030A5D7  E9 D6 F6 FF FF                  jmp 0x140309cb2
0030A5DC  48 8B C2                        mov rax, rdx
0030A5DF  E8 EC 04 3B 00                  call 0x1406baad0
0030A5E4  E9 0D FD FF FF                  jmp 0x14030a2f6
0030A5E9  33 C9                           xor ecx, ecx
0030A5EB  E9 52 FF FF FF                  jmp 0x14030a542
0030A5F0  41 B8 64 00 00 00               mov r8d, 0x64
0030A5F6  E9 45 F8 FF FF                  jmp 0x140309e40
0030A5FB  41 8B 0A                        mov ecx, dword ptr [r10]
0030A5FE  0F 33                           rdpmc
0030A600  48 C1 E2 20                     shl rdx, 0x20
0030A604  48 0B C2                        or rax, rdx
0030A607  49 89 03                        mov qword ptr [r11], rax
0030A60A  E9 C3 F8 FF FF                  jmp 0x140309ed2
0030A60F  41 FF 40 14                     inc dword ptr [r8 + 0x14]
0030A613  41 0F B6 86 83 02 00 00         movzx eax, byte ptr [r14 + 0x283]
0030A61B  49 8B 08                        mov rcx, qword ptr [r8]
0030A61E  48 0F AB C1                     bts rcx, rax
0030A622  49 89 08                        mov qword ptr [r8], rcx
0030A625  E9 C5 F8 FF FF                  jmp 0x140309eef
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiStartThreadCycleAccumulationContextSwap(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m5C;
    unsigned int v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned int v_stack_p0;
    unsigned int v_stack_p10;
    unsigned int v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p8;

    v_rsp = (v_rsp) - (104);
    v_r13 = 0;
    if ((*(unsigned __int8 *)(a1 + 34524)) == 0) goto loc_00309DB5;
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rip + 13345663) + 228)) != 5) goto loc_00309FC0;
    if ((*(unsigned __int64 *)(v_rip + 13345908)) == 0) goto loc_0030A1AD;
    if (((*(unsigned int *)(*(unsigned __int64 *)(v_rip + 13345663) + 224)) & (0x10000ULL)) != 0) goto loc_0030A34A;
loc_00309C8A:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 13345663) + 112)) != (v_rip + 1138811)) goto loc_0030A5C9;
    v_stack_p10 = 0;
    a2 = (v_rip + 1138811) << (32);
    *(unsigned int *)(v_stack_p10) = (unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 13345663) + 72));
    a2 = (a2) | (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 13345663) + 112));
loc_00309CB2:
    v_rdi = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 13345663) + 72))) + (a2);
loc_00309CD0:
    if ((*(unsigned __int64 *)(v_rip + 13345663)) != (*(unsigned __int64 *)(v_rip + 13345521))) goto loc_0030A292;
loc_00309CE0:
    v_r13 = 0;
    v_stack_m68 = 0;
    if ((unsigned __int8)(*(unsigned __int8 *)(a1 + 172)) != 0) {
        a2 = (v_rdi) << ((unsigned __int8)(*(unsigned __int8 *)(a1 + 172)));
    }
    v_stack_m68 = a2;
    v_r11 = (a2) - (*(unsigned __int64 *)(a1 + 34432));
    v_r12 = (v_rdi) - (*(unsigned __int64 *)(a1 + 34552));
    if ((*(unsigned __int8 *)(v_rip + 13356398)) == 0) goto loc_00309DB5;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 176))) == 0) goto loc_00309DB5;
    v_stack_m80 = 0;
    v_stack_m78 = 0;
    if ((unsigned __int8)(*(unsigned __int64 *)(a1 + 176)) == 0) goto loc_0030A1A5;
    a2 = (*(unsigned __int64 *)(a1 + 34552)) << ((unsigned __int8)((unsigned __int8)(*(unsigned __int64 *)(a1 + 176))));
    a3 = (v_rdi) << ((unsigned __int8)((unsigned __int8)(*(unsigned __int64 *)(a1 + 176))));
loc_00309D74:
    v_stack_m80 = a2;
    v_stack_m78 = a2;
    v_r10 = (a2) >> ((unsigned __int8)((__int8)(*(unsigned __int8 *)(v_rip + 13356619))));
    a2 = (a2) >> ((unsigned __int8)((__int8)(*(unsigned __int8 *)(v_rip + 13356619))));
    a2 = (unsigned int)((a2) - ((unsigned int)(v_r10)));
    if (condition_is_not_equal) goto loc_0030A0A4;
loc_00309DB5:
    result = (*(unsigned __int64 *)(a1 + 34560)) + (v_r12);
    *(unsigned __int64 *)(a1 + 34560) = result;
    result = (*(unsigned __int64 *)(a1 + 34680)) + (v_r11);
    *(unsigned __int64 *)(a1 + 34680) = result;
    *(unsigned __int64 *)(a1 + 34552) = v_rdi;
    *(unsigned __int64 *)(a1 + 34432) = a2;
    if ((((unsigned __int8)(*(unsigned __int8 *)(a2 + 2))) & (182)) == 0) goto loc_00309F9D;
    if ((((unsigned __int8)(*(unsigned __int8 *)(a2 + 2))) & (32)) == 0) goto loc_00309E83;
    if (*(unsigned __int64 *)(a1 + 35248) == 0) goto loc_0030A5F0;
    if (*(unsigned __int64 *)(a1 + 35256) == 0) goto loc_0030A5F0;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 35256) + 112)) != 0) goto loc_00309E39;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 35256) + 80)))) < ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 35248) + 528))))) goto loc_00309E40;
    goto loc_00309E40;
loc_00309E39:
loc_00309E40:
loc_00309E4A:
    if (((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 35248) + 528)))) + 132)))) <= ((unsigned int)(*(unsigned __int16 *)(a1 + 35434)))) goto loc_00309E5D;
    a1 = (unsigned int)((0) + 1);
    a2 = (a1 + 35434) + (2);
    if (((unsigned int)(a1)) < 3) goto loc_00309E4A;
loc_00309E5D:
    result = ((*(unsigned __int8 *)(a1 + 35336)) != 0) ? 1 : 0;
    a1 = (*(unsigned __int64 *)(a1 + result + a1 * 2 + 4336 * 8)) + (v_r11);
    *(unsigned __int64 *)(a1 + result + a1 * 2 + 4336 * 8) = a1;
loc_00309E83:
    if ((((unsigned __int8)(*(unsigned __int8 *)(a2 + 2))) & (64)) == 0) goto loc_00309E99;
    if (*(unsigned __int64 *)(a2 + 968) != 0) {
        *(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 968) + 64) = (unsigned __int8)(v_r13 + 1);
    }
    *(unsigned __int8 *)(a1 + 32) = 0;
    if (*(unsigned __int64 *)(a2 + 360) == 0) goto loc_00309EEF;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 360) + 32) == 0) goto loc_00309EE3;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11913808))) == 0) goto loc_00309EE3;
loc_00309EC9:
    if (((v_r13 + 1) & (*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 360) + 32))) != 0) goto loc_0030A5FB;
loc_00309ED2:
    v_r15 = (v_r13 + 1) + (v_r13 + 1);
    v_r11 = (*(unsigned __int64 *)(a2 + 360) + 48) + (24);
    v_r10 = (v_rip + 12611517) + (4);
    v_rbx = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11913808))))) - (1);
    if (condition_is_not_equal) goto loc_00309EC9;
loc_00309EE3:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 360) + 16)))) & (1)) != 0) goto loc_0030A60F;
loc_00309EEF:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536) != 0) goto loc_0030A0B5;
loc_00309F08:
    if (((*(unsigned __int8 *)(a2 + 2)) & (4)) != 0) goto loc_00309F4C;
loc_00309F10:
    result = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 360) + 16));
    if ((*(unsigned __int8 *)(v_rip + 13355975)) != 0) {
        a2 = (a1 + result + a1 * 2 + 4336 * 8) << (32);
        result = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 360) + 16))) | (a2);
        *(unsigned __int64 *)(a2 + 1080) = 0;
        *(unsigned __int64 *)(a2 + 1072) = result;
    }
    if ((*(unsigned __int8 *)(a1 + 6)) != 0) goto loc_0030A0F0;
loc_00309F3A:
    v_rsp = (v_rsp) + (104);
    return result;
loc_00309F4C:
    if (condition_is_below) goto loc_0030A0DD;
    if (condition_is_below) goto loc_00309F10;
    if ((*(unsigned __int8 *)(a2 + 195)) >= 16) goto loc_00309F10;
    if ((*(unsigned __int8 *)(a2 + 195)) < 16) goto loc_00309F10;
    if (*(unsigned __int64 *)(a2 + 104) == 0) goto loc_00309F10;
    a1 = ((unsigned int)(*(unsigned int *)(a1 + 216))) + (*(unsigned __int64 *)(a2 + 104));
loc_00309F82:
    if (((*(unsigned __int8 *)(a1 + 112)) & (2)) != 0) goto loc_0030A0DD;
    if (*(unsigned __int64 *)(a1 + 416) != 0) goto loc_00309F82;
    goto loc_00309F10;
loc_00309F9D:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536) != 0) goto loc_0030A17D;
loc_00309FBA:
    goto loc_00309F30;
loc_00309FC0:
    if ((*(unsigned int *)(v_r13 + 220)) != 64) goto loc_0030A2C0;
    if (((*(unsigned int *)(v_r13 + 224)) & (0x10000ULL)) != 0) goto loc_0030A3DB;
loc_00309FEA:
    if ((*(unsigned __int64 *)(v_r13 + 112)) != (v_rip + 454491)) goto loc_0030A53F;
    if (*(unsigned __int64 *)(v_rip + 11564891) == 0) goto loc_0030A439;
    if ((*(unsigned __int64 *)(v_rip + 11564891)) != (v_rip - 181333)) goto loc_0030A5E9;
    v_stack_m88 = v_rdi;
    v_stack_p18 = (unsigned int)(v_rdi);
loc_0030A02F:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 13356370)))) == 0) goto loc_0030A40F;
    if ((*(unsigned __int8 *)(v_r10)) == ((unsigned __int8)(v_rdi))) goto loc_0030A3F3;
    *(unsigned int *)(v_stack_p18) = (unsigned int)(v_rip - 181333);
loc_0030A055:
    a2 = (*(unsigned __int64 *)(v_r13 + 112)) << (32);
    a2 = (a2) | (*(unsigned __int64 *)(v_rip + 13356370));
    a2 = (a2) + (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 13356314) + 16));
    v_stack_m88 = a2;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 13356300))))) != ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 13356370)))))) goto loc_0030A02F;
loc_0030A08A:
loc_0030A08E:
    goto loc_00309CD0;
loc_0030A0A4:
    goto loc_00309DB5;
loc_0030A0B5:
loc_0030A0BC:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 13356300))))) != ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 13356370)))))) goto loc_0030A0BC;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 13356300))))) >= ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 13356370)))))) goto loc_00309F08;
    result = KiRemoveSystemWorkPriorityKick((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 13356300))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 13356314) + 16))))), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 13356314) + 16), (unsigned int)(0x989680ULL));
    goto loc_00309F08;
loc_0030A0DD:
    result = KiInsertDeferredPreemptionApc(a1, a2, 1, (unsigned int)(0x989680ULL));
    goto loc_00309F10;
loc_0030A0F0:
    *(unsigned __int8 *)(a1 + 6) = 0;
    if (a2 == (*(unsigned __int64 *)(a1 + 24))) goto loc_00309F3A;
    result = 0;
    v_stack_m5C = v_xmm0;
    if ((*(unsigned __int8 *)(v_rip + 13355708)) == 0) goto loc_0030A163;
    result = HalpDisableInterrupts(a1, a2, *(unsigned __int64 *)(gs_base + (0 + 32)), (unsigned int)(0x989680ULL));
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 168))))) | (4));
    *(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 168) = (unsigned int)(a1);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 168))) == 0) {
        a1 = 0xC0010015ULL;
        a2 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 168))) << (32);
        result = (result) | (a2);
        result = (result) | (a2);
        a2 = result;
        a2 = (a2) >> (32);
    }
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
    }
    v_stack_m60 = 5;
    result = HalpInterruptSendIpi(v_stack_m60, 47, *(unsigned __int64 *)(gs_base + (0 + 32)), (unsigned __int8)(result));
    goto loc_00309F3A;
loc_0030A17D:
loc_0030A184:
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) goto loc_0030A184;
    if (condition_is_above_or_equal) goto loc_00309FBA;
    result = KiRemoveSystemWorkPriorityKick(v_stack_m60, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)))))), *(unsigned __int64 *)(gs_base + (0 + 32)), (unsigned __int8)(result));
    goto loc_00309FBA;
loc_0030A1A5:
    goto loc_00309D74;
loc_0030A1AD:
    if ((*(unsigned int *)(v_r13 + 220)) != 64) goto loc_0030A450;
    result = HalpTimerGetInternalData(0, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)))))), *(unsigned __int64 *)(gs_base + (0 + 32)), (unsigned __int8)(result));
    if ((*(unsigned __int64 *)(v_r13 + 112)) != (v_rip + 454015)) goto loc_0030A5A8;
    if (*(unsigned __int64 *)(v_rip + 11564415) == 0) goto loc_0030A595;
    if ((*(unsigned __int64 *)(v_rip + 11564415)) != (v_rip - 181809)) goto loc_0030A5C5;
    v_stack_p20 = *(unsigned __int64 *)(v_r13 + 208) + v_stack_m88 * 1;
    v_stack_p8 = (unsigned int)(*(unsigned __int64 *)(v_r13 + 208) + v_stack_m88 * 1);
loc_0030A20B:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 13355894)))) == 0) goto loc_0030A582;
    if ((*(unsigned __int8 *)(v_r10)) == ((unsigned __int8)(*(unsigned __int64 *)(v_r13 + 208) + v_stack_m88 * 1))) goto loc_0030A54F;
    *(unsigned int *)(v_stack_p8) = (unsigned int)(v_rip - 181809);
loc_0030A231:
    a2 = (*(unsigned __int64 *)(v_r13 + 112)) << (32);
    a2 = (a2) | (*(unsigned __int64 *)(v_rip + 13355894));
    a2 = (a2) + (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 13355838) + 16));
    v_stack_p20 = a2;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 13355821))))) != ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 13355894)))))) goto loc_0030A20B;
loc_0030A269:
loc_0030A26D:
loc_0030A274:
    result = HalpTimerScaleCounter(*(unsigned __int64 *)(v_r13 + 208) + v_stack_p20 * 1, *(unsigned __int64 *)(v_r13 + 192), *(unsigned __int64 *)(v_r13 + 192), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 13355894))));
    goto loc_00309CD0;
loc_0030A292:
    if (result == 0) goto loc_00309CE0;
    a3 = *(unsigned __int64 *)(result + 192);
    if ((*(unsigned int *)(result + 228)) == 5) { a3 = *(unsigned __int64 *)(v_r13 + 192); }
    result = HalpTimerScaleCounter(result, *(unsigned __int64 *)(v_r13 + 192), a3, *(unsigned __int64 *)(v_r13 + 192));
    goto loc_00309CE0;
loc_0030A2C0:
    v_stack_m70 = *(unsigned __int64 *)(v_r13 + 208);
loc_0030A2D2:
    result = HalpTimerGetInternalData(0, *(unsigned __int64 *)(v_r13 + 192), a3, *(unsigned __int64 *)(v_r13 + 192));
    if ((*(unsigned __int64 *)(v_r13 + 112)) != (v_rip + 455566)) goto loc_0030A5DC;
    result = HalpHpetQueryCounter(result, *(unsigned __int64 *)(v_r13 + 112), a3, *(unsigned __int64 *)(v_r13 + 192));
loc_0030A2F6:
    if ((*(unsigned __int64 *)(v_r13 + 200)) != (*(unsigned __int64 *)(v_r13 + 200))) goto loc_0030A2D2;
    if (v_stack_m70 != (*(unsigned __int64 *)(v_r13 + 208))) goto loc_0030A2C0;
    a2 = (v_r15) << ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_r13 + 220)) - 1));
    a1 = (result) ^ (*(unsigned __int64 *)(v_r13 + 200));
    if (((a2) & (a1)) != 0) goto loc_0030A362;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_r13 + 220)))) == 64) goto loc_0030A3AE;
    a2 = (v_r15) << ((unsigned __int8)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_r13 + 220))))));
    a2 = (a2) - 1;
    goto loc_0030A3B5;
loc_0030A34A:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(gs_base + (0 + 420)))) * (*(unsigned int *)(v_r13 + 80)));
    a1 = ((unsigned int)((unsigned int)(result))) + (*(unsigned __int64 *)(v_r13 + 72));
    goto loc_00309C8A;
loc_0030A362:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_r13 + 220)))) != 64) goto loc_0030A3CD;
loc_0030A36F:
    a2 = (v_r15) << ((unsigned __int8)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_r13 + 220))))));
    a1 = 0;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_r13 + 220)))) != 64) { a1 = a2; }
    a3 = (-1) & (*(unsigned __int64 *)(v_r13 + 200));
    a2 = (a3) ^ (*(unsigned __int64 *)(v_r13 + 200));
    a2 = (a2) | (result);
    if (result < a3) {
        a2 = (a2) + (a1);
    }
    goto loc_00309CD0;
loc_0030A3AE:
loc_0030A3B5:
    a2 = ~(-1);
    a2 = (a2) & (v_stack_m70 + a2 * 1);
    a2 = (a2) | (result);
    goto loc_00309CD0;
loc_0030A3CD:
    a3 = (v_r15) << ((unsigned __int8)((unsigned int)((unsigned int)((unsigned int)(0x989680ULL)))));
    a3 = (a3) - 1;
    goto loc_0030A36F;
loc_0030A3DB:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(gs_base + (0 + 420)))) * (*(unsigned int *)(v_r13 + 80)));
    a1 = ((unsigned int)((unsigned int)(result))) + (*(unsigned __int64 *)(v_r13 + 72));
    goto loc_00309FEA;
loc_0030A3F3:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 141)) != 2) goto loc_0030A422;
loc_0030A408:
    goto loc_0030A055;
loc_0030A40F:
    result = HvlpGetRegister64((unsigned int)(0x90004ULL), v_stack_m88, a3, (unsigned int)(0x989680ULL));
    goto loc_0030A08A;
loc_0030A422:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 141)) != ((unsigned __int8)(v_r15))) goto loc_0030A408;
    goto loc_0030A408;
loc_0030A439:
    a2 = (v_stack_m88) << (32);
    a2 = (a2) | (*(unsigned __int64 *)(gs_base + (0 + 32)));
    goto loc_0030A08E;
loc_0030A450:
    v_stack_m70 = *(unsigned __int64 *)(v_r13 + 208);
loc_0030A462:
    result = HalpTimerGetInternalData(0, a2, a3, (unsigned int)(0x989680ULL));
    if ((*(unsigned __int64 *)(v_r13 + 112)) != (v_rip + 455166)) goto loc_0030A5B8;
    result = HalpHpetQueryCounter(result, *(unsigned __int64 *)(v_r13 + 112), a3, (unsigned int)(0x989680ULL));
loc_0030A486:
    if ((*(unsigned __int64 *)(v_r13 + 200)) != (*(unsigned __int64 *)(v_r13 + 200))) goto loc_0030A462;
    if (v_stack_m70 != (*(unsigned __int64 *)(v_r13 + 208))) goto loc_0030A450;
    a2 = (v_r15) << ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_r13 + 220)) - 1));
    a1 = (result) ^ (*(unsigned __int64 *)(v_r13 + 200));
    if (((a2) & (a1)) != 0) goto loc_0030A4E1;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_r13 + 220)))) != 64) goto loc_0030A531;
loc_0030A4D3:
    a2 = ~(-1);
    a2 = (a2) & (*(unsigned __int64 *)(v_r13 + 200));
    a2 = (a2) | (result);
    goto loc_0030A274;
loc_0030A4E1:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_r13 + 220)))) != 64) goto loc_0030A523;
loc_0030A4EE:
    a2 = (v_r15) << ((unsigned __int8)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_r13 + 220))))));
    a1 = 0;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_r13 + 220)))) != 64) { a1 = a2; }
    a3 = (-1) & (*(unsigned __int64 *)(v_r13 + 200));
    a2 = (a3) ^ (*(unsigned __int64 *)(v_r13 + 200));
    a2 = (a2) | (result);
    if (result < a3) {
        a2 = (a2) + (a1);
    }
    goto loc_0030A274;
loc_0030A523:
    a3 = (v_r15) << ((unsigned __int8)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_r13 + 220))))));
    a3 = (a3) - 1;
    goto loc_0030A4EE;
loc_0030A531:
    a2 = (v_r15) << ((unsigned __int8)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_r13 + 220))))));
    a2 = (a2) - 1;
    goto loc_0030A4D3;
loc_0030A53F:
loc_0030A542:
    result = guard_dispatch_icall((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_r13 + 220)))), a2, a3, (unsigned int)(*(unsigned int *)(v_r13 + 220)));
    goto loc_0030A08E;
loc_0030A54F:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 141)) != 2) goto loc_0030A56B;
loc_0030A564:
    goto loc_0030A231;
loc_0030A56B:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 141)) != ((unsigned __int8)(v_r15))) goto loc_0030A564;
    goto loc_0030A564;
loc_0030A582:
    result = HvlpGetRegister64((unsigned int)(0x90004ULL), v_stack_p20, a3, (unsigned int)(*(unsigned int *)(v_r13 + 220)));
    goto loc_0030A269;
loc_0030A595:
    a2 = (v_stack_p20) << (32);
    a2 = (a2) | (result);
    goto loc_0030A26D;
loc_0030A5A8:
loc_0030A5AB:
    result = guard_dispatch_icall((unsigned int)(0x40000020ULL), a2, a3, (unsigned int)(*(unsigned int *)(v_r13 + 220)));
    goto loc_0030A26D;
loc_0030A5B8:
    result = guard_dispatch_icall((unsigned int)(0x40000020ULL), result, a3, (unsigned int)(*(unsigned int *)(v_r13 + 220)));
    goto loc_0030A486;
loc_0030A5C5:
    a1 = 0;
    goto loc_0030A5AB;
loc_0030A5C9:
    result = guard_dispatch_icall(a1, result, a3, (unsigned int)(*(unsigned int *)(v_r13 + 220)));
    goto loc_00309CB2;
loc_0030A5DC:
    result = guard_dispatch_icall(a1, result, a3, (unsigned int)(0x989680ULL));
    goto loc_0030A2F6;
loc_0030A5E9:
    a1 = 0;
    goto loc_0030A542;
loc_0030A5F0:
    goto loc_00309E40;
loc_0030A5FB:
    a2 = (result) << (32);
    result = (result) | (a2);
    *(unsigned __int64 *)(v_r11) = result;
    goto loc_00309ED2;
loc_0030A60F:
    *(unsigned __int64 *)(100) = *(unsigned __int64 *)(100);
    goto loc_00309EEF;
}
```

## 5. (Beta) C Style

```c
int64_t KiStartThreadCycleAccumulationContextSwap(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m5C;
    uint32_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint32_t v_stack_p0;
    uint32_t v_stack_p10;
    uint32_t v_stack_p18;
    uint64_t v_stack_p20;
    uint32_t v_stack_p8;

    local_rsp = (local_rsp) - (104);
    local_r13 = 0;
    if ((*(uint8_t *)(arg1 + 0x86DC)) == 0) goto loc_00309DB5;
    if ((*(uint32_t *)(*(uint64_t *)(v_rip + 0xCBA37F) + 0xE4)) != 5) goto loc_00309FC0;
    if ((*(uint64_t *)(v_rip + 0xCBA474)) == 0) goto loc_0030A1AD;
    if (((*(uint32_t *)(*(uint64_t *)(v_rip + 0xCBA37F) + 0xE0)) & (0x10000ULL)) != 0) goto loc_0030A34A;
loc_00309C8A:
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xCBA37F) + 0x70)) != (v_rip + 1138811)) goto loc_0030A5C9;
    v_stack_p10 = 0;
    Arg2 = (v_rip + 1138811) << (32);
    *(uint32_t *)(v_stack_p10) = (uint32_t)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xCBA37F) + 0x48));
    Arg2 = (Arg2) | (*(uint64_t *)(*(uint64_t *)(v_rip + 0xCBA37F) + 0x70));
loc_00309CB2:
    local_rdi = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xCBA37F) + 0x48))) + (Arg2);
loc_00309CD0:
    if ((*(uint64_t *)(v_rip + 0xCBA37F)) != (*(uint64_t *)(v_rip + 0xCBA2F1))) goto loc_0030A292;
loc_00309CE0:
    local_r13 = 0;
    v_stack_m68 = 0;
    if ((uint8_t)(*(uint8_t *)(arg1 + 0xAC)) != 0) {
        Arg2 = (local_rdi) << ((uint8_t)(*(uint8_t *)(arg1 + 0xAC)));
    }
    v_stack_m68 = Arg2;
    local_r11 = (Arg2) - (*(uint64_t *)(arg1 + 0x8680));
    local_r12 = (local_rdi) - (*(uint64_t *)(arg1 + 0x86F8));
    if ((*(uint8_t *)(v_rip + 0xCBCD6E)) == 0) goto loc_00309DB5;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0xB0))) == 0) goto loc_00309DB5;
    v_stack_m80 = 0;
    v_stack_m78 = 0;
    if ((uint8_t)(*(uint64_t *)(arg1 + 0xB0)) == 0) goto loc_0030A1A5;
    Arg2 = (*(uint64_t *)(arg1 + 0x86F8)) << ((uint8_t)((uint8_t)(*(uint64_t *)(arg1 + 0xB0))));
    a3 = (local_rdi) << ((uint8_t)((uint8_t)(*(uint64_t *)(arg1 + 0xB0))));
loc_00309D74:
    v_stack_m80 = Arg2;
    v_stack_m78 = Arg2;
    local_r10 = (Arg2) >> ((uint8_t)((int8_t)(*(uint8_t *)(v_rip + 0xCBCE4B))));
    Arg2 = (Arg2) >> ((uint8_t)((int8_t)(*(uint8_t *)(v_rip + 0xCBCE4B))));
    Arg2 = (uint32_t)((Arg2) - ((uint32_t)(local_r10)));
    if (condition_is_not_equal) goto loc_0030A0A4;
loc_00309DB5:
    result = (*(uint64_t *)(arg1 + 0x8700)) + (local_r12);
    *(uint64_t *)(arg1 + 0x8700) = result;
    result = (*(uint64_t *)(arg1 + 0x8778)) + (local_r11);
    *(uint64_t *)(arg1 + 0x8778) = result;
    *(uint64_t *)(arg1 + 0x86F8) = local_rdi;
    *(void **)(arg1 + 0x8680) = Arg2;
    if ((((uint8_t)(*(uint8_t *)(arg2 + 0x2))) & (182)) == 0) goto loc_00309F9D;
    if ((((uint8_t)(*(uint8_t *)(arg2 + 0x2))) & (32)) == 0) goto loc_00309E83;
    if (*(uint64_t *)(arg1 + 0x89B0) == 0) goto loc_0030A5F0;
    if (*(uint64_t *)(arg1 + 0x89B8) == 0) goto loc_0030A5F0;
    if ((*(uint8_t *)(*(uint64_t *)(arg1 + 0x89B8) + 0x70)) != 0) goto loc_00309E39;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x89B8) + 0x50)))) < ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x89B0) + 0x210))))) goto loc_00309E40;
    goto loc_00309E40;
loc_00309E39:
loc_00309E40:
loc_00309E4A:
    if (((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x89B0) + 0x210)))) + 0x84)))) <= ((uint32_t)(*(uint16_t *)(arg1 + 0x8A6A)))) goto loc_00309E5D;
    Arg1 = (uint32_t)((0) + 1);
    Arg2 = (Arg1 + 35434) + (2);
    if (((uint32_t)(Arg1)) < 3) goto loc_00309E4A;
loc_00309E5D:
    result = ((*(uint8_t *)(arg1 + 0x8A08)) != 0) ? 1 : 0;
    Arg1 = (*(uint64_t *)(arg1 + result + arg1 * 2 + 0x10F0 * 8)) + (local_r11);
    *(void **)(arg1 + result + arg1 * 2 + 0x10F0 * 8) = Arg1;
loc_00309E83:
    if ((((uint8_t)(*(uint8_t *)(arg2 + 0x2))) & (64)) == 0) goto loc_00309E99;
    if (*(uint64_t *)(arg2 + 0x3C8) != 0) {
        *(uint8_t *)(*(uint64_t *)(arg2 + 0x3C8) + 0x40) = (uint8_t)(local_r13 + 1);
    }
    *(uint8_t *)(arg1 + 0x20) = 0;
    if (*(uint64_t *)(arg2 + 0x168) == 0) goto loc_00309EEF;
    if (*(uint64_t *)(*(uint64_t *)(arg2 + 0x168) + 0x20) == 0) goto loc_00309EE3;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB5CA50))) == 0) goto loc_00309EE3;
loc_00309EC9:
    if (((local_r13 + 1) & (*(uint64_t *)(*(uint64_t *)(arg2 + 0x168) + 0x20))) != 0) goto loc_0030A5FB;
loc_00309ED2:
    local_r15 = (local_r13 + 1) + (local_r13 + 1);
    local_r11 = (*(uint64_t *)(arg2 + 0x168) + 48) + (24);
    local_r10 = (v_rip + 12611517) + (4);
    local_rbx = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB5CA50))))) - (1);
    if (condition_is_not_equal) goto loc_00309EC9;
loc_00309EE3:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x168) + 0x10)))) & (1)) != 0) goto loc_0030A60F;
loc_00309EEF:
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8) != 0) goto loc_0030A0B5;
loc_00309F08:
    if (((*(uint8_t *)(arg2 + 0x2)) & (4)) != 0) goto loc_00309F4C;
loc_00309F10:
    result = (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x168) + 0x10));
    if ((*(uint8_t *)(v_rip + 0xCBCBC7)) != 0) {
        Arg2 = (Arg1 + result + Arg1 * 2 + 4336 * 8) << (32);
        result = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x168) + 0x10))) | (Arg2);
        *(uint64_t *)(arg2 + 0x438) = 0;
        *(uint64_t *)(arg2 + 0x430) = result;
    }
    if ((*(uint8_t *)(arg1 + 0x6)) != 0) goto loc_0030A0F0;
loc_00309F3A:
    local_rsp = (local_rsp) + (104);
    return result;
loc_00309F4C:
    if (condition_is_below) goto loc_0030A0DD;
    if (condition_is_below) goto loc_00309F10;
    if ((*(uint8_t *)(arg2 + 0xC3)) >= 16) goto loc_00309F10;
    if ((*(uint8_t *)(arg2 + 0xC3)) < 16) goto loc_00309F10;
    if (*(uint64_t *)(arg2 + 0x68) == 0) goto loc_00309F10;
    Arg1 = ((uint32_t)(*(uint32_t *)(arg1 + 0xD8))) + (*(uint64_t *)(arg2 + 0x68));
loc_00309F82:
    if (((*(uint8_t *)(arg1 + 0x70)) & (2)) != 0) goto loc_0030A0DD;
    if (*(uint64_t *)(arg1 + 0x1A0) != 0) goto loc_00309F82;
    goto loc_00309F10;
loc_00309F9D:
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8) != 0) goto loc_0030A17D;
loc_00309FBA:
    goto loc_00309F30;
loc_00309FC0:
    if ((*(uint32_t *)(local_r13 + 0xDC)) != 64) goto loc_0030A2C0;
    if (((*(uint32_t *)(local_r13 + 0xE0)) & (0x10000ULL)) != 0) goto loc_0030A3DB;
loc_00309FEA:
    if ((*(uint64_t *)(local_r13 + 0x70)) != (v_rip + 454491)) goto loc_0030A53F;
    if (*(uint64_t *)(v_rip + 0xB0775B) == 0) goto loc_0030A439;
    if ((*(uint64_t *)(v_rip + 0xB0775B)) != (v_rip - 181333)) goto loc_0030A5E9;
    v_stack_m88 = local_rdi;
    v_stack_p18 = (uint32_t)(local_rdi);
loc_0030A02F:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xCBCD52)))) == 0) goto loc_0030A40F;
    if ((*(uint8_t *)(local_r10)) == ((uint8_t)(local_rdi))) goto loc_0030A3F3;
    *(uint32_t *)(v_stack_p18) = (uint32_t)(v_rip - 181333);
loc_0030A055:
    Arg2 = (*(uint64_t *)(local_r13 + 0x70)) << (32);
    Arg2 = (Arg2) | (*(uint64_t *)(v_rip + 0xCBCD52));
    Arg2 = (Arg2) + (*(uint64_t *)(*(uint64_t *)(v_rip + 0xCBCD1A) + 0x10));
    v_stack_m88 = Arg2;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xCBCD0C))))) != ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xCBCD52)))))) goto loc_0030A02F;
loc_0030A08A:
loc_0030A08E:
    goto loc_00309CD0;
loc_0030A0A4:
    goto loc_00309DB5;
loc_0030A0B5:
loc_0030A0BC:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xCBCD0C))))) != ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xCBCD52)))))) goto loc_0030A0BC;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xCBCD0C))))) >= ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xCBCD52)))))) goto loc_00309F08;
    result = KiRemoveSystemWorkPriorityKick((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xCBCD0C))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xCBCD1A) + 0x10))))), *(uint64_t *)(*(uint64_t *)(v_rip + 0xCBCD1A) + 0x10), (uint32_t)(0x989680ULL));
    goto loc_00309F08;
loc_0030A0DD:
    result = KiInsertDeferredPreemptionApc(Arg1, Arg2, 1, (uint32_t)(0x989680ULL));
    goto loc_00309F10;
loc_0030A0F0:
    *(uint8_t *)(arg1 + 0x6) = 0;
    if (Arg2 == (*(uint64_t *)(arg1 + 0x18))) goto loc_00309F3A;
    result = 0;
    v_stack_m5C = v_xmm0;
    if ((*(uint8_t *)(v_rip + 0xCBCABC)) == 0) goto loc_0030A163;
    result = HalpDisableInterrupts(Arg1, Arg2, *(uint64_t *)(gs_base + (0 + 0x20)), (uint32_t)(0x989680ULL));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xA8))))) | (4));
    *(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xA8) = (uint32_t)(Arg1);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xA8))) == 0) {
        Arg1 = 0xC0010015ULL;
        Arg2 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xA8))) << (32);
        result = (result) | (Arg2);
        result = (result) | (Arg2);
        Arg2 = result;
        Arg2 = (Arg2) >> (32);
    }
    if ((uint8_t)((uint8_t)(result)) != 0) {
    }
    v_stack_m60 = 5;
    result = HalpInterruptSendIpi(v_stack_m60, 47, *(uint64_t *)(gs_base + (0 + 0x20)), (uint8_t)(result));
    goto loc_00309F3A;
loc_0030A17D:
loc_0030A184:
    if ((uint8_t)((uint8_t)(result)) != 0) goto loc_0030A184;
    if (condition_is_above_or_equal) goto loc_00309FBA;
    result = KiRemoveSystemWorkPriorityKick(v_stack_m60, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)))))), *(uint64_t *)(gs_base + (0 + 0x20)), (uint8_t)(result));
    goto loc_00309FBA;
loc_0030A1A5:
    goto loc_00309D74;
loc_0030A1AD:
    if ((*(uint32_t *)(local_r13 + 0xDC)) != 64) goto loc_0030A450;
    result = HalpTimerGetInternalData(0, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)))))), *(uint64_t *)(gs_base + (0 + 0x20)), (uint8_t)(result));
    if ((*(uint64_t *)(local_r13 + 0x70)) != (v_rip + 454015)) goto loc_0030A5A8;
    if (*(uint64_t *)(v_rip + 0xB0757F) == 0) goto loc_0030A595;
    if ((*(uint64_t *)(v_rip + 0xB0757F)) != (v_rip - 181809)) goto loc_0030A5C5;
    v_stack_p20 = *(uint64_t *)(local_r13 + 0xD0) + v_stack_m88 * 1;
    v_stack_p8 = (uint32_t)(*(uint64_t *)(local_r13 + 0xD0) + v_stack_m88 * 1);
loc_0030A20B:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xCBCB76)))) == 0) goto loc_0030A582;
    if ((*(uint8_t *)(local_r10)) == ((uint8_t)(*(uint64_t *)(local_r13 + 0xD0) + v_stack_m88 * 1))) goto loc_0030A54F;
    *(uint32_t *)(v_stack_p8) = (uint32_t)(v_rip - 181809);
loc_0030A231:
    Arg2 = (*(uint64_t *)(local_r13 + 0x70)) << (32);
    Arg2 = (Arg2) | (*(uint64_t *)(v_rip + 0xCBCB76));
    Arg2 = (Arg2) + (*(uint64_t *)(*(uint64_t *)(v_rip + 0xCBCB3E) + 0x10));
    v_stack_p20 = Arg2;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xCBCB2D))))) != ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xCBCB76)))))) goto loc_0030A20B;
loc_0030A269:
loc_0030A26D:
loc_0030A274:
    result = HalpTimerScaleCounter(*(uint64_t *)(local_r13 + 0xD0) + v_stack_p20 * 1, *(uint64_t *)(local_r13 + 0xC0), *(uint64_t *)(local_r13 + 0xC0), (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xCBCB76))));
    goto loc_00309CD0;
loc_0030A292:
    if (result == 0) goto loc_00309CE0;
    a3 = *(uint64_t *)(result + 0xC0);
    if ((*(uint32_t *)(result + 0xE4)) == 5) { a3 = *(uint64_t *)(local_r13 + 0xC0); }
    result = HalpTimerScaleCounter(result, *(uint64_t *)(local_r13 + 0xC0), a3, *(uint64_t *)(local_r13 + 0xC0));
    goto loc_00309CE0;
loc_0030A2C0:
    v_stack_m70 = *(uint64_t *)(local_r13 + 0xD0);
loc_0030A2D2:
    result = HalpTimerGetInternalData(0, *(uint64_t *)(local_r13 + 0xC0), a3, *(uint64_t *)(local_r13 + 0xC0));
    if ((*(uint64_t *)(local_r13 + 0x70)) != (v_rip + 455566)) goto loc_0030A5DC;
    result = HalpHpetQueryCounter(result, *(uint64_t *)(local_r13 + 0x70), a3, *(uint64_t *)(local_r13 + 0xC0));
loc_0030A2F6:
    if ((*(uint64_t *)(local_r13 + 0xC8)) != (*(uint64_t *)(local_r13 + 0xC8))) goto loc_0030A2D2;
    if (v_stack_m70 != (*(uint64_t *)(local_r13 + 0xD0))) goto loc_0030A2C0;
    Arg2 = (local_r15) << ((uint8_t)((uint32_t)(*(uint32_t *)(local_r13 + 0xDC)) - 1));
    Arg1 = (result) ^ (*(uint64_t *)(local_r13 + 0xC8));
    if (((Arg2) & (Arg1)) != 0) goto loc_0030A362;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_r13 + 0xDC)))) == 64) goto loc_0030A3AE;
    Arg2 = (local_r15) << ((uint8_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_r13 + 0xDC))))));
    Arg2 = (Arg2) - 1;
    goto loc_0030A3B5;
loc_0030A34A:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4)))) * (*(uint32_t *)(local_r13 + 0x50)));
    Arg1 = ((uint32_t)((uint32_t)(result))) + (*(uint64_t *)(local_r13 + 0x48));
    goto loc_00309C8A;
loc_0030A362:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_r13 + 0xDC)))) != 64) goto loc_0030A3CD;
loc_0030A36F:
    Arg2 = (local_r15) << ((uint8_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_r13 + 0xDC))))));
    Arg1 = 0;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_r13 + 0xDC)))) != 64) { Arg1 = Arg2; }
    a3 = (-1) & (*(uint64_t *)(local_r13 + 0xC8));
    Arg2 = (a3) ^ (*(uint64_t *)(local_r13 + 0xC8));
    Arg2 = (Arg2) | (result);
    if (result < a3) {
        Arg2 = (Arg2) + (Arg1);
    }
    goto loc_00309CD0;
loc_0030A3AE:
loc_0030A3B5:
    Arg2 = ~(-1);
    Arg2 = (Arg2) & (v_stack_m70 + Arg2 * 1);
    Arg2 = (Arg2) | (result);
    goto loc_00309CD0;
loc_0030A3CD:
    a3 = (local_r15) << ((uint8_t)((uint32_t)((uint32_t)((uint32_t)(0x989680ULL)))));
    a3 = (a3) - 1;
    goto loc_0030A36F;
loc_0030A3DB:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4)))) * (*(uint32_t *)(local_r13 + 0x50)));
    Arg1 = ((uint32_t)((uint32_t)(result))) + (*(uint64_t *)(local_r13 + 0x48));
    goto loc_00309FEA;
loc_0030A3F3:
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8D)) != 2) goto loc_0030A422;
loc_0030A408:
    goto loc_0030A055;
loc_0030A40F:
    result = HvlpGetRegister64((uint32_t)(0x90004ULL), v_stack_m88, a3, (uint32_t)(0x989680ULL));
    goto loc_0030A08A;
loc_0030A422:
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8D)) != ((uint8_t)(local_r15))) goto loc_0030A408;
    goto loc_0030A408;
loc_0030A439:
    Arg2 = (v_stack_m88) << (32);
    Arg2 = (Arg2) | (*(uint64_t *)(gs_base + (0 + 0x20)));
    goto loc_0030A08E;
loc_0030A450:
    v_stack_m70 = *(uint64_t *)(local_r13 + 0xD0);
loc_0030A462:
    result = HalpTimerGetInternalData(0, Arg2, a3, (uint32_t)(0x989680ULL));
    if ((*(uint64_t *)(local_r13 + 0x70)) != (v_rip + 455166)) goto loc_0030A5B8;
    result = HalpHpetQueryCounter(result, *(uint64_t *)(local_r13 + 0x70), a3, (uint32_t)(0x989680ULL));
loc_0030A486:
    if ((*(uint64_t *)(local_r13 + 0xC8)) != (*(uint64_t *)(local_r13 + 0xC8))) goto loc_0030A462;
    if (v_stack_m70 != (*(uint64_t *)(local_r13 + 0xD0))) goto loc_0030A450;
    Arg2 = (local_r15) << ((uint8_t)((uint32_t)(*(uint32_t *)(local_r13 + 0xDC)) - 1));
    Arg1 = (result) ^ (*(uint64_t *)(local_r13 + 0xC8));
    if (((Arg2) & (Arg1)) != 0) goto loc_0030A4E1;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_r13 + 0xDC)))) != 64) goto loc_0030A531;
loc_0030A4D3:
    Arg2 = ~(-1);
    Arg2 = (Arg2) & (*(uint64_t *)(local_r13 + 0xC8));
    Arg2 = (Arg2) | (result);
    goto loc_0030A274;
loc_0030A4E1:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_r13 + 0xDC)))) != 64) goto loc_0030A523;
loc_0030A4EE:
    Arg2 = (local_r15) << ((uint8_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_r13 + 0xDC))))));
    Arg1 = 0;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_r13 + 0xDC)))) != 64) { Arg1 = Arg2; }
    a3 = (-1) & (*(uint64_t *)(local_r13 + 0xC8));
    Arg2 = (a3) ^ (*(uint64_t *)(local_r13 + 0xC8));
    Arg2 = (Arg2) | (result);
    if (result < a3) {
        Arg2 = (Arg2) + (Arg1);
    }
    goto loc_0030A274;
loc_0030A523:
    a3 = (local_r15) << ((uint8_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_r13 + 0xDC))))));
    a3 = (a3) - 1;
    goto loc_0030A4EE;
loc_0030A531:
    Arg2 = (local_r15) << ((uint8_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_r13 + 0xDC))))));
    Arg2 = (Arg2) - 1;
    goto loc_0030A4D3;
loc_0030A53F:
loc_0030A542:
    result = guard_dispatch_icall((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_r13 + 0xDC)))), Arg2, a3, (uint32_t)(*(uint32_t *)(local_r13 + 0xDC)));
    goto loc_0030A08E;
loc_0030A54F:
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8D)) != 2) goto loc_0030A56B;
loc_0030A564:
    goto loc_0030A231;
loc_0030A56B:
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8D)) != ((uint8_t)(local_r15))) goto loc_0030A564;
    goto loc_0030A564;
loc_0030A582:
    result = HvlpGetRegister64((uint32_t)(0x90004ULL), v_stack_p20, a3, (uint32_t)(*(uint32_t *)(local_r13 + 0xDC)));
    goto loc_0030A269;
loc_0030A595:
    Arg2 = (v_stack_p20) << (32);
    Arg2 = (Arg2) | (result);
    goto loc_0030A26D;
loc_0030A5A8:
loc_0030A5AB:
    result = guard_dispatch_icall((uint32_t)(0x40000020ULL), Arg2, a3, (uint32_t)(*(uint32_t *)(local_r13 + 0xDC)));
    goto loc_0030A26D;
loc_0030A5B8:
    result = guard_dispatch_icall((uint32_t)(0x40000020ULL), result, a3, (uint32_t)(*(uint32_t *)(local_r13 + 0xDC)));
    goto loc_0030A486;
loc_0030A5C5:
    Arg1 = 0;
    goto loc_0030A5AB;
loc_0030A5C9:
    result = guard_dispatch_icall(Arg1, result, a3, (uint32_t)(*(uint32_t *)(local_r13 + 0xDC)));
    goto loc_00309CB2;
loc_0030A5DC:
    result = guard_dispatch_icall(Arg1, result, a3, (uint32_t)(0x989680ULL));
    goto loc_0030A2F6;
loc_0030A5E9:
    Arg1 = 0;
    goto loc_0030A542;
loc_0030A5F0:
    goto loc_00309E40;
loc_0030A5FB:
    Arg2 = (result) << (32);
    result = (result) | (Arg2);
    *(uint64_t *)(local_r11) = result;
    goto loc_00309ED2;
loc_0030A60F:
    *(uint64_t *)(100) = *(uint64_t *)(100);
    goto loc_00309EEF;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `16` | `R` |
| `Arg1` | `+ 0x0` | `64` | `W` |
| `Arg1` | `+ 0x0 + rax*8` | `64` | `R` |
| `Arg1` | `+ 0x6` | `8` | `R` |
| `Arg1` | `+ 0x6` | `8` | `W` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x20` | `8` | `R/W` |
| `Arg1` | `+ 0x20` | `8` | `W` |
| `Arg1` | `+ 0xAC` | `8` | `R` |
| `Arg1` | `+ 0xB0` | `64` | `R` |
| `Arg1` | `+ 0xD8` | `32` | `R` |
| `Arg1` | `+ 0x8644` | `32` | `R/W` |
| `Arg1` | `+ 0x8650` | `32` | `R/W` |
| `Arg1` | `+ 0x8680` | `64` | `R` |
| `Arg1` | `+ 0x8680` | `64` | `W` |
| `Arg1` | `+ 0x86DC` | `8` | `R` |
| `Arg1` | `+ 0x86F8` | `64` | `R` |
| `Arg1` | `+ 0x86F8` | `64` | `W` |
| `Arg1` | `+ 0x8700` | `64` | `R` |
| `Arg1` | `+ 0x8700` | `64` | `W` |
| `Arg1` | `+ 0x8778` | `64` | `R` |
| `Arg1` | `+ 0x8778` | `64` | `W` |
| `Arg1` | `+ 0x89B0` | `64` | `R` |
| `Arg1` | `+ 0x89B8` | `64` | `R` |
| `Arg1` | `+ 0x8A08` | `8` | `R` |
| `Arg1` | `+ 0x8A6A` | `64` | `R` |
| `Arg2` | `+ 0x2` | `8` | `R` |
| `Arg2` | `+ 0x68` | `64` | `R` |
| `Arg2` | `+ 0x78` | `32` | `R` |
| `Arg2` | `+ 0xC3` | `8` | `R` |
| `Arg2` | `+ 0x168` | `64` | `R` |
| `Arg2` | `+ 0x283` | `8` | `R` |

추가 오프셋 3개는 표에서 생략했습니다.

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00309C10&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
