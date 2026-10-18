# KiUpdateTotalCyclesCurrentThread

- RVA: `0x0037DE40`–`0x0037E687` (길이 `2,119` bytes)
- VA: `0x000000014037DE40`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007B644`
- 디코드: `511`개 명령, `2,119/2,119` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **5**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **14**
- RIP 상대 이미지 참조: **11**

### Outgoing calls
- `0x0037DE8E` → [KeQueryPerformanceCounter](KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)
- `0x0037E18D` → [KiUpdateThreadHgsFeedback](KiUpdateThreadHgsFeedback_function_0037D790.md) (function, `0x0037D790`)
- `0x0037E1E0` → [KeQueryPerformanceCounter](KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)
- `0x0037E3AD` → [KiEndCounterAccumulation](KiEndCounterAccumulation_function_0037EEAC.md) (function, `0x0037EEAC`)
- `0x0037E5C4` → [HalRequestSoftwareInterrupt](../3F/HalRequestSoftwareInterrupt_function_003FADA0.md) (function, `0x003FADA0`)

### Direct callers
- [KeYieldExecution](../20/KeYieldExecution_function_00209FA0.md) at `0x0020A111`
- [sub_0021D7F8](../21/Unknown_function_0021D7F8.md) at `0x0021D863`
- [KeSetPriorityThread](../2C/KeSetPriorityThread_function_002C76E0.md) at `0x002C778B`
- [KiRemoveThreadFromSchedulingGroup](../35/KiRemoveThreadFromSchedulingGroup_function_00356514.md) at `0x00356697`
- [sub_00392F50](../39/Unknown_function_00392F50.md) at `0x00392F82`
- [sub_0039538C](../39/Unknown_function_0039538C.md) at `0x003953BC`
- [KeSetPriorityAndQuantumProcess](../3C/KeSetPriorityAndQuantumProcess_function_003C2EC0.md) at `0x003C30CE`
- [KeSetActualBasePriorityThread](../3C/KeSetActualBasePriorityThread_function_003C4370.md) at `0x003C44AF`
- [KeRemovePriQueue](../3C/KeRemovePriQueue_function_003C5090.md) at `0x003C558F`
- [KeSetBasePriorityThread](../3C/KeSetBasePriorityThread_function_003C6EB0.md) at `0x003C7046`
- [KiCompleteDirectSwitchThread](../3F/KiCompleteDirectSwitchThread_function_003FFE1C.md) at `0x003FFE53`
- [KeBoostPriorityThread](../4D/KeBoostPriorityThread_function_004D37F8.md) at `0x004D3937`
- [KiStartDebugAccumulation](../5C/KiStartDebugAccumulation_function_005C3460.md) at `0x005C3482`
- [sub_006E7EC2](../6E/Unknown_function_006E7EC2.md) at `0x006E7EEB`

### Static image references
- `0x0037DEC8` → RVA `0x00FC6A95` (`ALMOSTRO`; read)
- `0x0037DF16` → RVA `0x00FC6BC6` (`ALMOSTRO`; read)
- `0x0037DF2E` → RVA `0x00FC7318` (`ALMOSTRO`; read)
- `0x0037E0C2` → RVA `0x00F10A44` (`.data`; read)
- `0x0037E0EA` → RVA `0x00FC6D60` (`ALMOSTRO`; read)
- `0x0037E178` → RVA `0x00FC6ADE` (`ALMOSTRO`; read)
- `0x0037E192` → RVA `0x00FCFF00` (`CACHEALI`; read)
- `0x0037E311` → RVA `0x00E66908` (`.data`; read)
- `0x0037E31B` → RVA `0x00F10E80` (`.data`; read)
- `0x0037E608` → RVA `0x00FC537C` (`ALMOSTRO`; read)
- `0x0037E615` → RVA `0x00FC53E0` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0037DE40  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
0037DE45  53                              push rbx
0037DE46  55                              push rbp
0037DE47  56                              push rsi
0037DE48  57                              push rdi
0037DE49  41 54                           push r12
0037DE4B  41 55                           push r13
0037DE4D  41 56                           push r14
0037DE4F  41 57                           push r15
0037DE51  48 83 EC 58                     sub rsp, 0x58
0037DE55  33 FF                           xor edi, edi
0037DE57  C6 41 20 01                     mov byte ptr [rcx + 0x20], 1
0037DE5B  90                              nop
0037DE5C  48 8B F2                        mov rsi, rdx
0037DE5F  48 8B D9                        mov rbx, rcx
0037DE62  44 8B DF                        mov r11d, edi
0037DE65  44 8B FF                        mov r15d, edi
0037DE68  44 8B F7                        mov r14d, edi
0037DE6B  48 BD 00 03 00 00 80 F7 FF FF   movabs rbp, 0xfffff78000000300
0037DE75  49 BC 60 03 00 00 80 F7 FF FF   movabs r12, 0xfffff78000000360
0037DE7F  40 38 B9 DC 86 00 00            cmp byte ptr [rcx + 0x86dc], dil
0037DE86  0F 84 D3 00 00 00               je 0x14037df5f
0037DE8C  33 C9                           xor ecx, ecx
0037DE8E  E8 4D 09 00 00                  call 0x14037e7e0
0037DE93  0F B6 8B AC 00 00 00            movzx ecx, byte ptr [rbx + 0xac]
0037DE9A  4C 8B D8                        mov r11, rax
0037DE9D  48 8B 83 B0 00 00 00            mov rax, qword ptr [rbx + 0xb0]
0037DEA4  49 8B D3                        mov rdx, r11
0037DEA7  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
0037DEAC  84 C9                           test cl, cl
0037DEAE  74 03                           je 0x14037deb3
0037DEB0  48 D3 E2                        shl rdx, cl
0037DEB3  48 F7 E2                        mul rdx
0037DEB6  4C 8B F2                        mov r14, rdx
0037DEB9  48 89 54 24 38                  mov qword ptr [rsp + 0x38], rdx
0037DEBE  4C 2B B3 80 86 00 00            sub r14, qword ptr [rbx + 0x8680]
0037DEC5  4C 8B FA                        mov r15, rdx
0037DEC8  40 38 3D C6 8B C4 00            cmp byte ptr [rip + 0xc48bc6], dil
0037DECF  0F 84 8A 00 00 00               je 0x14037df5f
0037DED5  4C 8B 83 F8 86 00 00            mov r8, qword ptr [rbx + 0x86f8]
0037DEDC  48 39 7D 00                     cmp qword ptr [rbp], rdi
0037DEE0  74 7D                           je 0x14037df5f
0037DEE2  A0 69 03 00 00 80 F7 FF FF      movabs al, byte ptr [0xfffff78000000369]
0037DEEB  4D 8B 0C 24                     mov r9, qword ptr [r12]
0037DEEF  0F B6 C8                        movzx ecx, al
0037DEF2  84 C0                           test al, al
0037DEF4  48 89 BC 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rdi
0037DEFC  49 8B C1                        mov rax, r9
0037DEFF  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
0037DF04  0F 84 C4 06 00 00               je 0x14037e5ce
0037DF0A  49 D3 E0                        shl r8, cl
0037DF0D  49 F7 E0                        mul r8
0037DF10  4D 8B C3                        mov r8, r11
0037DF13  49 D3 E0                        shl r8, cl
0037DF16  0F BE 0D A9 8C C4 00            movsx ecx, byte ptr [rip + 0xc48ca9]
0037DF1D  4C 8B D2                        mov r10, rdx
0037DF20  48 89 94 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rdx
0037DF28  49 8B C1                        mov rax, r9
0037DF2B  49 F7 E0                        mul r8
0037DF2E  48 8B 05 E3 93 C4 00            mov rax, qword ptr [rip + 0xc493e3]
0037DF35  4C 8B CA                        mov r9, rdx
0037DF38  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
0037DF3D  49 F7 E2                        mul r10
0037DF40  48 8B 05 D1 93 C4 00            mov rax, qword ptr [rip + 0xc493d1]
0037DF47  4C 8B D2                        mov r10, rdx
0037DF4A  49 F7 E1                        mul r9
0037DF4D  49 D3 EA                        shr r10, cl
0037DF50  4C 8B C2                        mov r8, rdx
0037DF53  49 D3 E8                        shr r8, cl
0037DF56  45 2B C2                        sub r8d, r10d
0037DF59  0F 85 52 05 00 00               jne 0x14037e4b1
0037DF5F  4C 89 9B F8 86 00 00            mov qword ptr [rbx + 0x86f8], r11
0037DF66  4C 89 BB 80 86 00 00            mov qword ptr [rbx + 0x8680], r15
0037DF6D  48 8B 46 48                     mov rax, qword ptr [rsi + 0x48]
0037DF71  49 03 C6                        add rax, r14
0037DF74  48 89 46 48                     mov qword ptr [rsi + 0x48], rax
0037DF78  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0037DF7D  48 3B 73 18                     cmp rsi, qword ptr [rbx + 0x18]
0037DF81  74 23                           je 0x14037dfa6
0037DF83  8B 83 B8 86 00 00               mov eax, dword ptr [rbx + 0x86b8]
0037DF89  8B 4E 50                        mov ecx, dword ptr [rsi + 0x50]
0037DF8C  49 0F AF C6                     imul rax, r14
0037DF90  48 C1 E8 10                     shr rax, 0x10
0037DF94  48 03 C8                        add rcx, rax
0037DF97  B8 FF FF FF FF                  mov eax, 0xffffffff
0037DF9C  48 3B C8                        cmp rcx, rax
0037DF9F  48 0F 47 C8                     cmova rcx, rax
0037DFA3  89 4E 50                        mov dword ptr [rsi + 0x50], ecx
0037DFA6  0F B6 6E 02                     movzx ebp, byte ptr [rsi + 2]
0037DFAA  41 BD 01 00 00 00               mov r13d, 1
0037DFB0  45 8D 65 63                     lea r12d, [r13 + 0x63]
0037DFB4  40 F6 C5 BE                     test bpl, 0xbe
0037DFB8  0F 84 FB 01 00 00               je 0x14037e1b9
0037DFBE  40 84 ED                        test bpl, bpl
0037DFC1  79 57                           jns 0x14037e01a
0037DFC3  48 8B 86 20 02 00 00            mov rax, qword ptr [rsi + 0x220]
0037DFCA  41 8B D5                        mov edx, r13d
0037DFCD  4C 8B 83 B0 8B 00 00            mov r8, qword ptr [rbx + 0x8bb0]
0037DFD4  44 8B 88 90 01 00 00            mov r9d, dword ptr [rax + 0x190]
0037DFDB  41 8B C1                        mov eax, r9d
0037DFDE  C1 E8 0D                        shr eax, 0xd
0037DFE1  25 FF FF 03 00                  and eax, 0x3ffff
0037DFE6  49 C1 E9 04                     shr r9, 4
0037DFEA  0F BD C8                        bsr ecx, eax
0037DFED  41 81 E1 FF 01 00 00            and r9d, 0x1ff
0037DFF4  D3 E2                           shl edx, cl
0037DFF6  83 C1 FE                        add ecx, -2
0037DFF9  33 D0                           xor edx, eax
0037DFFB  89 8C 24 A0 00 00 00            mov dword ptr [rsp + 0xa0], ecx
0037E002  49 8B 0C C8                     mov rcx, qword ptr [r8 + rcx*8]
0037E006  48 8B 54 D1 08                  mov rdx, qword ptr [rcx + rdx*8 + 8]
0037E00B  4A 8B 04 CA                     mov rax, qword ptr [rdx + r9*8]
0037E00F  49 03 C6                        add rax, r14
0037E012  4A 89 04 CA                     mov qword ptr [rdx + r9*8], rax
0037E016  40 80 E5 7F                     and bpl, 0x7f
0037E01A  40 F6 C5 10                     test bpl, 0x10
0037E01E  0F 85 52 04 00 00               jne 0x14037e476
0037E024  40 F6 C5 20                     test bpl, 0x20
0037E028  0F 84 40 01 00 00               je 0x14037e16e
0037E02E  4C 8B 8E 88 06 00 00            mov r9, qword ptr [rsi + 0x688]
0037E035  4D 85 C9                        test r9, r9
0037E038  0F 84 2C 01 00 00               je 0x14037e16a
0037E03E  48 8B 8B B0 89 00 00            mov rcx, qword ptr [rbx + 0x89b0]
0037E045  48 8B 83 B8 89 00 00            mov rax, qword ptr [rbx + 0x89b8]
0037E04C  48 85 C9                        test rcx, rcx
0037E04F  0F 84 16 06 00 00               je 0x14037e66b
0037E055  48 85 C0                        test rax, rax
0037E058  0F 84 0D 06 00 00               je 0x14037e66b
0037E05E  40 38 78 70                     cmp byte ptr [rax + 0x70], dil
0037E062  75 11                           jne 0x14037e075
0037E064  8B 50 50                        mov edx, dword ptr [rax + 0x50]
0037E067  8B 81 10 02 00 00               mov eax, dword ptr [rcx + 0x210]
0037E06D  3B D0                           cmp edx, eax
0037E06F  72 0A                           jb 0x14037e07b
0037E071  8B D0                           mov edx, eax
0037E073  EB 06                           jmp 0x14037e07b
0037E075  8B 90 84 00 00 00               mov edx, dword ptr [rax + 0x84]
0037E07B  44 8B C7                        mov r8d, edi
0037E07E  48 8D 8B 6A 8A 00 00            lea rcx, [rbx + 0x8a6a]
0037E085  0F B7 01                        movzx eax, word ptr [rcx]
0037E088  3B D0                           cmp edx, eax
0037E08A  76 0D                           jbe 0x14037e099
0037E08C  41 FF C0                        inc r8d
0037E08F  48 83 C1 02                     add rcx, 2
0037E093  41 83 F8 03                     cmp r8d, 3
0037E097  72 EC                           jb 0x14037e085
0037E099  44 0F B6 93 08 8A 00 00         movzx r10d, byte ptr [rbx + 0x8a08]
0037E0A1  41 0F B6 C2                     movzx eax, r10b
0037E0A5  41 8B D0                        mov edx, r8d
0037E0A8  F6 D8                           neg al
0037E0AA  48 1B C9                        sbb rcx, rcx
0037E0AD  48 03 D2                        add rdx, rdx
0037E0B0  83 E1 08                        and ecx, 8
0037E0B3  49 8D 04 09                     lea rax, [r9 + rcx]
0037E0B7  48 8B 0C D0                     mov rcx, qword ptr [rax + rdx*8]
0037E0BB  49 03 CE                        add rcx, r14
0037E0BE  48 89 0C D0                     mov qword ptr [rax + rdx*8], rcx
0037E0C2  8B 05 7C 29 B9 00               mov eax, dword ptr [rip + 0xb9297c]
0037E0C8  41 8B 89 C0 00 00 00            mov ecx, dword ptr [r9 + 0xc0]
0037E0CF  3B C1                           cmp eax, ecx
0037E0D1  0F 87 A4 04 00 00               ja 0x14037e57b
0037E0D7  2B C8                           sub ecx, eax
0037E0D9  83 F9 20                        cmp ecx, 0x20
0037E0DC  73 0C                           jae 0x14037e0ea
0037E0DE  41 8B C5                        mov eax, r13d
0037E0E1  D3 E0                           shl eax, cl
0037E0E3  41 09 81 C4 00 00 00            or dword ptr [r9 + 0xc4], eax
0037E0EA  39 3D 70 8C C4 00               cmp dword ptr [rip + 0xc48c70], edi
0037E0F0  75 1E                           jne 0x14037e110
0037E0F2  0F B6 8E 04 02 00 00            movzx ecx, byte ptr [rsi + 0x204]
0037E0F9  8D 41 FE                        lea eax, [rcx - 2]
0037E0FC  A9 FB FF FF FF                  test eax, 0xfffffffb
0037E101  0F 84 57 03 00 00               je 0x14037e45e
0037E107  80 F9 05                        cmp cl, 5
0037E10A  0F 84 4E 03 00 00               je 0x14037e45e
0037E110  48 39 BE 50 06 00 00            cmp qword ptr [rsi + 0x650], rdi
0037E117  74 51                           je 0x14037e16a
0037E119  41 0F B6 C2                     movzx eax, r10b
0037E11D  41 8B C8                        mov ecx, r8d
0037E120  48 83 C1 08                     add rcx, 8
0037E124  48 03 C9                        add rcx, rcx
0037E127  F6 D8                           neg al
0037E129  48 1B D2                        sbb rdx, rdx
0037E12C  83 E2 08                        and edx, 8
0037E12F  49 8D 04 C9                     lea rax, [r9 + rcx*8]
0037E133  48 8B 0C 02                     mov rcx, qword ptr [rdx + rax]
0037E137  49 03 CE                        add rcx, r14
0037E13A  48 89 0C 02                     mov qword ptr [rdx + rax], rcx
0037E13E  45 84 D2                        test r10b, r10b
0037E141  48 8B 86 50 06 00 00            mov rax, qword ptr [rsi + 0x650]
0037E148  BA 48 00 00 00                  mov edx, 0x48
0037E14D  48 8B 88 88 06 00 00            mov rcx, qword ptr [rax + 0x688]
0037E154  B8 40 00 00 00                  mov eax, 0x40
0037E159  0F 45 C2                        cmovne eax, edx
0037E15C  41 8B D0                        mov edx, r8d
0037E15F  48 03 D2                        add rdx, rdx
0037E162  48 03 C1                        add rax, rcx
0037E165  F0 4C 01 34 D0                  lock add qword ptr [rax + rdx*8], r14
0037E16A  40 80 E5 DF                     and bpl, 0xdf
0037E16E  40 F6 C5 40                     test bpl, 0x40
0037E172  0F 85 20 03 00 00               jne 0x14037e498
0037E178  40 38 3D 5F 89 C4 00            cmp byte ptr [rip + 0xc4895f], dil
0037E17F  74 11                           je 0x14037e192
0037E181  45 33 C9                        xor r9d, r9d
0037E184  4D 8B C6                        mov r8, r14
0037E187  48 8B D6                        mov rdx, rsi
0037E18A  48 8B CB                        mov rcx, rbx
0037E18D  E8 FE F5 FF FF                  call 0x14037d790
0037E192  4C 8D 0D 67 1D C5 00            lea r9, [rip + 0xc51d67]
0037E199  48 39 BB B0 86 00 00            cmp qword ptr [rbx + 0x86b0], rdi
0037E1A0  74 0D                           je 0x14037e1af
0037E1A2  4C 39 8E 20 02 00 00            cmp qword ptr [rsi + 0x220], r9
0037E1A9  0F 85 32 04 00 00               jne 0x14037e5e1
0037E1AF  40 F6 C5 BE                     test bpl, 0xbe
0037E1B3  0F 85 B0 01 00 00               jne 0x14037e369
0037E1B9  48 8B 84 24 B0 00 00 00         mov rax, qword ptr [rsp + 0xb0]
0037E1C1  48 85 C0                        test rax, rax
0037E1C4  74 03                           je 0x14037e1c9
0037E1C6  4C 89 38                        mov qword ptr [rax], r15
0037E1C9  48 8B EF                        mov rbp, rdi
0037E1CC  4C 8B FF                        mov r15, rdi
0037E1CF  4C 8B F7                        mov r14, rdi
0037E1D2  4C 8B DF                        mov r11, rdi
0037E1D5  40 38 BB DC 86 00 00            cmp byte ptr [rbx + 0x86dc], dil
0037E1DC  74 56                           je 0x14037e234
0037E1DE  33 C9                           xor ecx, ecx
0037E1E0  E8 FB 05 00 00                  call 0x14037e7e0
0037E1E5  0F B6 8B AC 00 00 00            movzx ecx, byte ptr [rbx + 0xac]
0037E1EC  48 8B E8                        mov rbp, rax
0037E1EF  48 8B 83 B0 00 00 00            mov rax, qword ptr [rbx + 0xb0]
0037E1F6  48 8B D5                        mov rdx, rbp
0037E1F9  48 89 7C 24 40                  mov qword ptr [rsp + 0x40], rdi
0037E1FE  84 C9                           test cl, cl
0037E200  74 03                           je 0x14037e205
0037E202  48 D3 E2                        shl rdx, cl
0037E205  48 F7 E2                        mul rdx
0037E208  4C 8B F5                        mov r14, rbp
0037E20B  4C 8B FA                        mov r15, rdx
0037E20E  48 89 54 24 40                  mov qword ptr [rsp + 0x40], rdx
0037E213  48 8B 93 F8 86 00 00            mov rdx, qword ptr [rbx + 0x86f8]
0037E21A  4D 8B DF                        mov r11, r15
0037E21D  4C 2B 9B 80 86 00 00            sub r11, qword ptr [rbx + 0x8680]
0037E224  4C 2B F2                        sub r14, rdx
0037E227  40 38 3D 67 88 C4 00            cmp byte ptr [rip + 0xc48867], dil
0037E22E  0F 85 83 01 00 00               jne 0x14037e3b7
0037E234  48 8B 8B 00 87 00 00            mov rcx, qword ptr [rbx + 0x8700]
0037E23B  49 03 CE                        add rcx, r14
0037E23E  48 89 8B 00 87 00 00            mov qword ptr [rbx + 0x8700], rcx
0037E245  48 8B 8B 78 87 00 00            mov rcx, qword ptr [rbx + 0x8778]
0037E24C  49 03 CB                        add rcx, r11
0037E24F  48 89 8B 78 87 00 00            mov qword ptr [rbx + 0x8778], rcx
0037E256  F6 46 02 20                     test byte ptr [rsi + 2], 0x20
0037E25A  74 7B                           je 0x14037e2d7
0037E25C  48 8B 8B B0 89 00 00            mov rcx, qword ptr [rbx + 0x89b0]
0037E263  48 8B 83 B8 89 00 00            mov rax, qword ptr [rbx + 0x89b8]
0037E26A  48 85 C9                        test rcx, rcx
0037E26D  74 26                           je 0x14037e295
0037E26F  48 85 C0                        test rax, rax
0037E272  74 21                           je 0x14037e295
0037E274  40 38 78 70                     cmp byte ptr [rax + 0x70], dil
0037E278  75 14                           jne 0x14037e28e
0037E27A  44 8B 60 50                     mov r12d, dword ptr [rax + 0x50]
0037E27E  8B 81 10 02 00 00               mov eax, dword ptr [rcx + 0x210]
0037E284  44 3B E0                        cmp r12d, eax
0037E287  72 0C                           jb 0x14037e295
0037E289  44 8B E0                        mov r12d, eax
0037E28C  EB 07                           jmp 0x14037e295
0037E28E  44 8B A0 84 00 00 00            mov r12d, dword ptr [rax + 0x84]
0037E295  8B CF                           mov ecx, edi
0037E297  48 8D 93 6A 8A 00 00            lea rdx, [rbx + 0x8a6a]
0037E29E  0F B7 02                        movzx eax, word ptr [rdx]
0037E2A1  44 3B E0                        cmp r12d, eax
0037E2A4  76 0B                           jbe 0x14037e2b1
0037E2A6  FF C1                           inc ecx
0037E2A8  48 83 C2 02                     add rdx, 2
0037E2AC  83 F9 03                        cmp ecx, 3
0037E2AF  72 ED                           jb 0x14037e29e
0037E2B1  40 38 BB 08 8A 00 00            cmp byte ptr [rbx + 0x8a08], dil
0037E2B8  8B C1                           mov eax, ecx
0037E2BA  40 0F 95 C7                     setne dil
0037E2BE  48 81 C7 F0 10 00 00            add rdi, 0x10f0
0037E2C5  48 8D 04 47                     lea rax, [rdi + rax*2]
0037E2C9  48 8B 0C C3                     mov rcx, qword ptr [rbx + rax*8]
0037E2CD  48 8D 14 C3                     lea rdx, [rbx + rax*8]
0037E2D1  49 03 CB                        add rcx, r11
0037E2D4  48 89 0A                        mov qword ptr [rdx], rcx
0037E2D7  F6 46 02 40                     test byte ptr [rsi + 2], 0x40
0037E2DB  74 10                           je 0x14037e2ed
0037E2DD  48 8B 86 C8 03 00 00            mov rax, qword ptr [rsi + 0x3c8]
0037E2E4  48 85 C0                        test rax, rax
0037E2E7  74 04                           je 0x14037e2ed
0037E2E9  44 88 68 40                     mov byte ptr [rax + 0x40], r13b
0037E2ED  48 89 AB F8 86 00 00            mov qword ptr [rbx + 0x86f8], rbp
0037E2F4  4C 89 BB 80 86 00 00            mov qword ptr [rbx + 0x8680], r15
0037E2FB  F6 46 02 02                     test byte ptr [rsi + 2], 2
0037E2FF  74 42                           je 0x14037e343
0037E301  48 8B 86 68 01 00 00            mov rax, qword ptr [rsi + 0x168]
0037E308  4C 8B 40 20                     mov r8, qword ptr [rax + 0x20]
0037E30C  4D 85 C0                        test r8, r8
0037E30F  74 32                           je 0x14037e343
0037E311  8B 0D F1 85 AE 00               mov ecx, dword ptr [rip + 0xae85f1]
0037E317  85 C9                           test ecx, ecx
0037E319  74 28                           je 0x14037e343
0037E31B  4C 8D 0D 5E 2B B9 00            lea r9, [rip + 0xb92b5e]
0037E322  44 8B D9                        mov r11d, ecx
0037E325  4C 8D 50 30                     lea r10, [rax + 0x30]
0037E329  4D 85 C5                        test r13, r8
0037E32C  0F 85 41 03 00 00               jne 0x14037e673
0037E332  4D 03 ED                        add r13, r13
0037E335  49 83 C2 18                     add r10, 0x18
0037E339  49 83 C1 04                     add r9, 4
0037E33D  49 83 EB 01                     sub r11, 1
0037E341  75 E6                           jne 0x14037e329
0037E343  90                              nop
0037E344  80 7B 06 00                     cmp byte ptr [rbx + 6], 0
0037E348  C6 43 20 00                     mov byte ptr [rbx + 0x20], 0
0037E34C  0F 85 6C 02 00 00               jne 0x14037e5be
0037E352  48 8B 44 24 30                  mov rax, qword ptr [rsp + 0x30]
0037E357  48 83 C4 58                     add rsp, 0x58
0037E35B  41 5F                           pop r15
0037E35D  41 5E                           pop r14
0037E35F  41 5D                           pop r13
0037E361  41 5C                           pop r12
0037E363  5F                              pop rdi
0037E364  5E                              pop rsi
0037E365  5D                              pop rbp
0037E366  5B                              pop rbx
0037E367  C3                              ret
0037E368  CC                              int3
0037E369  48 8B 4E 68                     mov rcx, qword ptr [rsi + 0x68]
0037E36D  48 85 C9                        test rcx, rcx
0037E370  74 18                           je 0x14037e38a
0037E372  8B 83 D8 00 00 00               mov eax, dword ptr [rbx + 0xd8]
0037E378  48 03 C1                        add rax, rcx
0037E37B  4C 01 30                        add qword ptr [rax], r14
0037E37E  48 8B 80 A0 01 00 00            mov rax, qword ptr [rax + 0x1a0]
0037E385  48 85 C0                        test rax, rax
0037E388  75 F1                           jne 0x14037e37b
0037E38A  F6 46 02 08                     test byte ptr [rsi + 2], 8
0037E38E  74 0D                           je 0x14037e39d
0037E390  4C 39 8E 20 02 00 00            cmp qword ptr [rsi + 0x220], r9
0037E397  0F 85 91 02 00 00               jne 0x14037e62e
0037E39D  48 39 BE 68 01 00 00            cmp qword ptr [rsi + 0x168], rdi
0037E3A4  0F 84 0F FE FF FF               je 0x14037e1b9
0037E3AA  48 8B CE                        mov rcx, rsi
0037E3AD  E8 FA 0A 00 00                  call 0x14037eeac
0037E3B2  E9 02 FE FF FF                  jmp 0x14037e1b9
0037E3B7  48 B8 00 03 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000300
0037E3C1  48 39 38                        cmp qword ptr [rax], rdi
0037E3C4  0F 84 6A FE FF FF               je 0x14037e234
0037E3CA  A0 69 03 00 00 80 F7 FF FF      movabs al, byte ptr [0xfffff78000000369]
0037E3D3  49 B9 60 03 00 00 80 F7 FF FF   movabs r9, 0xfffff78000000360
0037E3DD  0F B6 C8                        movzx ecx, al
0037E3E0  48 89 BC 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rdi
0037E3E8  84 C0                           test al, al
0037E3EA  48 89 7C 24 28                  mov qword ptr [rsp + 0x28], rdi
0037E3EF  4C 8B C5                        mov r8, rbp
0037E3F2  4D 8B 09                        mov r9, qword ptr [r9]
0037E3F5  49 8B C1                        mov rax, r9
0037E3F8  0F 84 DB 01 00 00               je 0x14037e5d9
0037E3FE  48 D3 E2                        shl rdx, cl
0037E401  48 F7 E2                        mul rdx
0037E404  49 D3 E0                        shl r8, cl
0037E407  0F BE 0D B8 87 C4 00            movsx ecx, byte ptr [rip + 0xc487b8]
0037E40E  4C 8B D2                        mov r10, rdx
0037E411  48 89 94 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rdx
0037E419  49 8B C1                        mov rax, r9
0037E41C  49 F7 E0                        mul r8
0037E41F  48 8B 05 F2 8E C4 00            mov rax, qword ptr [rip + 0xc48ef2]
0037E426  4C 8B CA                        mov r9, rdx
0037E429  48 89 54 24 28                  mov qword ptr [rsp + 0x28], rdx
0037E42E  49 F7 E2                        mul r10
0037E431  48 8B 05 E0 8E C4 00            mov rax, qword ptr [rip + 0xc48ee0]
0037E438  4C 8B D2                        mov r10, rdx
0037E43B  49 F7 E1                        mul r9
0037E43E  49 D3 EA                        shr r10, cl
0037E441  48 D3 EA                        shr rdx, cl
0037E444  41 2B D2                        sub edx, r10d
0037E447  0F 84 E7 FD FF FF               je 0x14037e234
0037E44D  01 93 44 86 00 00               add dword ptr [rbx + 0x8644], edx
0037E453  01 93 50 86 00 00               add dword ptr [rbx + 0x8650], edx
0037E459  E9 D6 FD FF FF                  jmp 0x14037e234
0037E45E  41 8B D0                        mov edx, r8d
0037E461  48 03 D2                        add rdx, rdx
0037E464  49 8B 4C D1 08                  mov rcx, qword ptr [r9 + rdx*8 + 8]
0037E469  49 03 CE                        add rcx, r14
0037E46C  49 89 4C D1 08                  mov qword ptr [r9 + rdx*8 + 8], rcx
0037E471  E9 9A FC FF FF                  jmp 0x14037e110
0037E476  0F B6 46 7C                     movzx eax, byte ptr [rsi + 0x7c]
0037E47A  48 8D 14 C3                     lea rdx, [rbx + rax*8]
0037E47E  48 8B 8A 88 86 00 00            mov rcx, qword ptr [rdx + 0x8688]
0037E485  49 03 CE                        add rcx, r14
0037E488  48 89 8A 88 86 00 00            mov qword ptr [rdx + 0x8688], rcx
0037E48F  40 80 E5 EF                     and bpl, 0xef
0037E493  E9 8C FB FF FF                  jmp 0x14037e024
0037E498  48 8B 86 C8 03 00 00            mov rax, qword ptr [rsi + 0x3c8]
0037E49F  48 85 C0                        test rax, rax
0037E4A2  0F 84 D0 FC FF FF               je 0x14037e178
0037E4A8  40 88 78 40                     mov byte ptr [rax + 0x40], dil
0037E4AC  E9 C7 FC FF FF                  jmp 0x14037e178
0037E4B1  F7 46 74 00 04 00 00            test dword ptr [rsi + 0x74], 0x400
0037E4B8  75 29                           jne 0x14037e4e3
0037E4BA  8B 86 4C 04 00 00               mov eax, dword ptr [rsi + 0x44c]
0037E4C0  F3 48 0F B8 D0                  popcnt rdx, rax
0037E4C5  49 8B C3                        mov rax, r11
0037E4C8  48 C1 E8 04                     shr rax, 4
0037E4CC  83 E0 1F                        and eax, 0x1f
0037E4CF  3B C2                           cmp eax, edx
0037E4D1  73 10                           jae 0x14037e4e3
0037E4D3  44 01 83 48 86 00 00            add dword ptr [rbx + 0x8648], r8d
0037E4DA  44 01 86 DC 02 00 00            add dword ptr [rsi + 0x2dc], r8d
0037E4E1  EB 0E                           jmp 0x14037e4f1
0037E4E3  44 01 83 44 86 00 00            add dword ptr [rbx + 0x8644], r8d
0037E4EA  44 01 86 8C 02 00 00            add dword ptr [rsi + 0x28c], r8d
0037E4F1  48 3B 73 18                     cmp rsi, qword ptr [rbx + 0x18]
0037E4F5  0F 84 64 FA FF FF               je 0x14037df5f
0037E4FB  48 8D 96 C3 00 00 00            lea rdx, [rsi + 0xc3]
0037E502  80 3A 10                        cmp byte ptr [rdx], 0x10
0037E505  7D 5F                           jge 0x14037e566
0037E507  48 8B 46 68                     mov rax, qword ptr [rsi + 0x68]
0037E50B  48 85 C0                        test rax, rax
0037E50E  74 56                           je 0x14037e566
0037E510  48 8B 46 68                     mov rax, qword ptr [rsi + 0x68]
0037E514  48 85 C0                        test rax, rax
0037E517  74 4D                           je 0x14037e566
0037E519  8B 8B D8 00 00 00               mov ecx, dword ptr [rbx + 0xd8]
0037E51F  44 8B CF                        mov r9d, edi
0037E522  48 03 C8                        add rcx, rax
0037E525  80 3A 10                        cmp byte ptr [rdx], 0x10
0037E528  7D 35                           jge 0x14037e55f
0037E52A  F7 46 78 00 02 00 00            test dword ptr [rsi + 0x78], 0x200
0037E531  75 2C                           jne 0x14037e55f
0037E533  48 8B D1                        mov rdx, rcx
0037E536  F6 42 70 02                     test byte ptr [rdx + 0x70], 2
0037E53A  75 33                           jne 0x14037e56f
0037E53C  48 8B 92 A0 01 00 00            mov rdx, qword ptr [rdx + 0x1a0]
0037E543  48 85 D2                        test rdx, rdx
0037E546  75 EE                           jne 0x14037e536
0037E548  44 03 49 7C                     add r9d, dword ptr [rcx + 0x7c]
0037E54C  75 0C                           jne 0x14037e55a
0037E54E  48 8B 89 A0 01 00 00            mov rcx, qword ptr [rcx + 0x1a0]
0037E555  48 85 C9                        test rcx, rcx
0037E558  75 EE                           jne 0x14037e548
0037E55A  45 85 C9                        test r9d, r9d
0037E55D  75 10                           jne 0x14037e56f
0037E55F  48 8D 96 C3 00 00 00            lea rdx, [rsi + 0xc3]
0037E566  80 3A 08                        cmp byte ptr [rdx], 8
0037E569  0F 8D F0 F9 FF FF               jge 0x14037df5f
0037E56F  44 01 83 6C 86 00 00            add dword ptr [rbx + 0x866c], r8d
0037E576  E9 E4 F9 FF FF                  jmp 0x14037df5f
0037E57B  8B D0                           mov edx, eax
0037E57D  89 84 24 A8 00 00 00            mov dword ptr [rsp + 0xa8], eax
0037E584  2B D1                           sub edx, ecx
0037E586  83 FA 20                        cmp edx, 0x20
0037E589  73 29                           jae 0x14037e5b4
0037E58B  41 8B 81 C4 00 00 00            mov eax, dword ptr [r9 + 0xc4]
0037E592  8B CA                           mov ecx, edx
0037E594  D3 E0                           shl eax, cl
0037E596  41 0B C5                        or eax, r13d
0037E599  89 84 24 AC 00 00 00            mov dword ptr [rsp + 0xac], eax
0037E5A0  48 8B 84 24 A8 00 00 00         mov rax, qword ptr [rsp + 0xa8]
0037E5A8  49 89 81 C0 00 00 00            mov qword ptr [r9 + 0xc0], rax
0037E5AF  E9 36 FB FF FF                  jmp 0x14037e0ea
0037E5B4  44 89 AC 24 AC 00 00 00         mov dword ptr [rsp + 0xac], r13d
0037E5BC  EB E2                           jmp 0x14037e5a0
0037E5BE  B1 02                           mov cl, 2
0037E5C0  C6 43 06 00                     mov byte ptr [rbx + 6], 0
0037E5C4  E8 D7 C7 07 00                  call 0x1403fada0
0037E5C9  E9 84 FD FF FF                  jmp 0x14037e352
0037E5CE  49 F7 E0                        mul r8
0037E5D1  4D 8B C3                        mov r8, r11
0037E5D4  E9 3D F9 FF FF                  jmp 0x14037df16
0037E5D9  48 F7 E2                        mul rdx
0037E5DC  E9 26 FE FF FF                  jmp 0x14037e407
0037E5E1  0F B6 86 04 02 00 00            movzx eax, byte ptr [rsi + 0x204]
0037E5E8  44 8B C0                        mov r8d, eax
0037E5EB  83 F8 07                        cmp eax, 7
0037E5EE  0F 83 BB FB FF FF               jae 0x14037e1af
0037E5F4  8B 46 54                        mov eax, dword ptr [rsi + 0x54]
0037E5F7  8B CF                           mov ecx, edi
0037E5F9  8B 56 50                        mov edx, dword ptr [rsi + 0x50]
0037E5FC  3B D0                           cmp edx, eax
0037E5FE  0F 46 D0                        cmovbe edx, eax
0037E601  0F B6 86 05 02 00 00            movzx eax, byte ptr [rsi + 0x205]
0037E608  3B 15 6E 6D C4 00               cmp edx, dword ptr [rip + 0xc46d6e]
0037E60E  0F 93 C1                        setae cl
0037E611  42 8D 0C 41                     lea ecx, [rcx + r8*2]
0037E615  0F AF 0D C4 6D C4 00            imul ecx, dword ptr [rip + 0xc46dc4]
0037E61C  03 C8                           add ecx, eax
0037E61E  48 8B 83 B0 86 00 00            mov rax, qword ptr [rbx + 0x86b0]
0037E625  4C 01 34 C8                     add qword ptr [rax + rcx*8], r14
0037E629  E9 81 FB FF FF                  jmp 0x14037e1af
0037E62E  4C 8B 83 C0 00 00 00            mov r8, qword ptr [rbx + 0xc0]
0037E635  48 8B 86 40 02 00 00            mov rax, qword ptr [rsi + 0x240]
0037E63C  41 0F B7 88 88 00 00 00         movzx ecx, word ptr [r8 + 0x88]
0037E644  48 8B 54 C8 08                  mov rdx, qword ptr [rax + rcx*8 + 8]
0037E649  49 8B 88 80 00 00 00            mov rcx, qword ptr [r8 + 0x80]
0037E650  48 8B C1                        mov rax, rcx
0037E653  48 23 C2                        and rax, rdx
0037E656  48 3B C1                        cmp rax, rcx
0037E659  0F 84 3E FD FF FF               je 0x14037e39d
0037E65F  4C 01 B3 A8 86 00 00            add qword ptr [rbx + 0x86a8], r14
0037E666  E9 32 FD FF FF                  jmp 0x14037e39d
0037E66B  41 8B D4                        mov edx, r12d
0037E66E  E9 08 FA FF FF                  jmp 0x14037e07b
0037E673  41 8B 09                        mov ecx, dword ptr [r9]
0037E676  0F 33                           rdpmc
0037E678  48 C1 E2 20                     shl rdx, 0x20
0037E67C  48 0B C2                        or rax, rdx
0037E67F  49 89 02                        mov qword ptr [r10], rax
0037E682  E9 AB FC FF FF                  jmp 0x14037e332
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiUpdateTotalCyclesCurrentThread(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned int v_stack_p8;
    unsigned int v_stack_pA8;
    unsigned int v_stack_pAC;
    unsigned __int64 v_stack_pB0;

    v_stack_p18 = a3;
    v_rsp = (v_rsp) - (88);
    v_rdi = 0;
    *(unsigned __int8 *)(a1 + 32) = 1;
    if ((*(unsigned __int8 *)(a1 + 34524)) == 0) goto loc_0037DF5F;
    a1 = 0;
    result = KeQueryPerformanceCounter(a1, a2, a3, a4);
    v_stack_m60 = 0;
    if ((unsigned __int8)(*(unsigned __int8 *)(a1 + 172)) != 0) {
        a2 = (result) << ((unsigned __int8)(*(unsigned __int8 *)(a1 + 172)));
    }
    v_stack_m60 = a2;
    v_r14 = (a2) - (*(unsigned __int64 *)(a1 + 34432));
    if ((*(unsigned __int8 *)(v_rip + 12880838)) == 0) goto loc_0037DF5F;
    if ((*(unsigned __int64 *)(v_rbp)) == 0) goto loc_0037DF5F;
    v_stack_p20 = 0;
    v_stack_m78 = 0;
    if ((unsigned __int8)(*(unsigned __int64 *)(a1 + 176)) == 0) goto loc_0037E5CE;
    a3 = (*(unsigned __int64 *)(a1 + 34552)) << ((unsigned __int8)((unsigned __int8)(*(unsigned __int64 *)(a1 + 176))));
    a3 = (result) << ((unsigned __int8)((unsigned __int8)(*(unsigned __int64 *)(a1 + 176))));
loc_0037DF16:
    v_stack_p20 = a2;
    v_stack_m78 = a2;
    v_r10 = (a2) >> ((unsigned __int8)((__int8)(*(unsigned __int8 *)(v_rip + 12881065))));
    a3 = (a2) >> ((unsigned __int8)((__int8)(*(unsigned __int8 *)(v_rip + 12881065))));
    a3 = (unsigned int)((a3) - ((unsigned int)(v_r10)));
    if (condition_is_not_equal) goto loc_0037E4B1;
loc_0037DF5F:
    *(unsigned __int64 *)(a1 + 34552) = result;
    *(unsigned __int64 *)(a1 + 34432) = a2;
    result = (*(unsigned __int64 *)(a2 + 72)) + (v_r14);
    *(unsigned __int64 *)(a2 + 72) = result;
    v_stack_m68 = result;
    if (a2 != (*(unsigned __int64 *)(a1 + 24))) {
        result = *(unsigned int *)(a1 + 34488);
        a1 = *(unsigned int *)(a2 + 80);
        result = (result) * (v_r14);
        result = (result) >> (16);
        a1 = (a1) + (result);
        result = 0xFFFFFFFFULL;
        if (a1 > result) { a1 = result; }
        *(unsigned int *)(a2 + 80) = (unsigned int)(a1);
    }
    if ((((unsigned __int8)(*(unsigned __int8 *)(a2 + 2))) & (190)) == 0) goto loc_0037E1B9;
    v_rbp = *(unsigned __int8 *)(a2 + 2);
    if (sign_flag) {
        result = *(unsigned __int64 *)(a2 + 544);
        a2 = 1;
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
        v_stack_p8 = (unsigned int)(a1);
        a1 = *(unsigned __int64 *)(a3 + a1 * 8);
        a2 = *(unsigned __int64 *)(a1 + a2 * 8 + 8);
        result = *(unsigned __int64 *)(a2 + a4 * 8);
        result = (result) + (v_r14);
        *(unsigned __int64 *)(a2 + a4 * 8) = result;
        v_rbp = (unsigned __int8)((*(unsigned __int8 *)(a2 + 2)) & (127));
    }
    if ((((unsigned __int8)(v_rbp)) & (16)) != 0) goto loc_0037E476;
loc_0037E024:
    if ((((unsigned __int8)(v_rbp)) & (32)) == 0) goto loc_0037E16E;
    if (*(unsigned __int64 *)(a2 + 1672) == 0) goto loc_0037E16A;
    if (*(unsigned __int64 *)(a1 + 35248) == 0) goto loc_0037E66B;
    if (*(unsigned __int64 *)(a1 + 35256) == 0) goto loc_0037E66B;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 35256) + 112)) != 0) goto loc_0037E075;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 35256) + 80)))) < ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 35248) + 528))))) goto loc_0037E07B;
    goto loc_0037E07B;
loc_0037E075:
loc_0037E07B:
loc_0037E085:
    if (((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 35248) + 528)) + 132)))) <= ((unsigned int)(*(unsigned __int16 *)(a1 + 35434)))) goto loc_0037E099;
    a3 = (unsigned int)((0) + 1);
    a1 = (a1 + 35434) + (2);
    if (((unsigned int)(a3)) < 3) goto loc_0037E085;
loc_0037E099:
    result = (unsigned __int8)(-((unsigned __int8)(*(unsigned __int8 *)(a1 + 35336))));
    a2 = ((unsigned int)((unsigned int)(a3))) + ((unsigned int)((unsigned int)(a3)));
    a1 = (unsigned int)((a1) & (8));
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 1672) + a1 * 1 + a2 * 8)) + (v_r14);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 1672) + a1 * 1 + a2 * 8) = a1;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12134780)))) > ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 1672) + 192))))) goto loc_0037E57B;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 1672) + 192))) - ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12134780)))));
    result = (unsigned int)(*(unsigned int *)(v_rip + 12134780));
    if (((unsigned int)(a1)) < 32) {
        result = 1;
        result = (unsigned int)((result) << ((unsigned __int8)(a1)));
    }
    if ((*(unsigned int *)(v_rip + 12881008)) != 0) goto loc_0037E110;
    if ((((unsigned int)(*(unsigned __int8 *)(a2 + 516) - 2)) & (0xFFFFFFFBULL)) == 0) goto loc_0037E45E;
    if (((unsigned __int8)(*(unsigned __int8 *)(a2 + 516))) == 5) goto loc_0037E45E;
loc_0037E110:
    result = *(unsigned __int8 *)(a2 + 516) - 2;
    if ((*(unsigned __int64 *)(a2 + 1616)) != 0) {
        result = (unsigned __int8)(*(unsigned __int8 *)(a1 + 35336));
        a1 = (unsigned int)(a3);
        a1 = (a1) + (8);
        a1 = (a1) + (a1);
        result = (unsigned __int8)(-(result));
        a2 = (unsigned int)((a2) & (8));
        result = *(unsigned __int64 *)(a2 + 1672) + a1 * 8;
        a1 = *(unsigned __int64 *)(a2 + result * 1);
        a1 = (a1) + (v_r14);
        *(unsigned __int64 *)(a2 + result * 1) = a1;
        result = *(unsigned __int64 *)(a2 + 1616);
        a2 = 72;
        a1 = *(unsigned __int64 *)(result + 1672);
        result = 64;
        if ((unsigned __int8)(*(unsigned __int8 *)(a1 + 35336)) != 0) { result = (unsigned int)(a2); }
        a2 = (unsigned int)(a3);
        a2 = (a2) + (a2);
        result = (result) + (a1);
    }
    v_rbp = (unsigned __int8)((v_rbp) & (223));
loc_0037E16E:
    if ((((unsigned __int8)(v_rbp)) & (64)) != 0) goto loc_0037E498;
loc_0037E178:
    if ((*(unsigned __int8 *)(v_rip + 12880223)) != 0) {
        a4 = 0;
        a3 = v_r14;
        a2 = a2;
        a1 = a1;
        result = KiUpdateThreadHgsFeedback(a1, a2, a3, a4);
    }
    if ((*(unsigned __int64 *)(a1 + 34480)) == 0) goto loc_0037E1AF;
    if ((*(unsigned __int64 *)(a2 + 544)) != (v_rip + 12918119)) goto loc_0037E5E1;
loc_0037E1AF:
    if ((((unsigned __int8)(v_rbp)) & (190)) != 0) goto loc_0037E369;
loc_0037E1B9:
    if (v_stack_p18 != 0) {
        *(unsigned __int64 *)(v_stack_p18) = a2;
    }
    if ((*(unsigned __int8 *)(a1 + 34524)) == 0) goto loc_0037E234;
    a1 = 0;
    result = KeQueryPerformanceCounter(a1, a2, a3, v_rip + 12918119);
    v_stack_m58 = 0;
    if ((unsigned __int8)(*(unsigned __int8 *)(a1 + 172)) != 0) {
        a2 = (result) << ((unsigned __int8)(*(unsigned __int8 *)(a1 + 172)));
    }
    v_stack_m58 = a2;
    v_r11 = (a2) - (*(unsigned __int64 *)(a1 + 34432));
    v_r14 = (result) - (*(unsigned __int64 *)(a1 + 34552));
    if ((*(unsigned __int8 *)(v_rip + 12879975)) != 0) goto loc_0037E3B7;
loc_0037E234:
    a1 = (*(unsigned __int64 *)(a1 + 34560)) + (v_r14);
    *(unsigned __int64 *)(a1 + 34560) = a1;
    a1 = (*(unsigned __int64 *)(a1 + 34680)) + (v_r11);
    *(unsigned __int64 *)(a1 + 34680) = a1;
    if (((*(unsigned __int8 *)(a2 + 2)) & (32)) == 0) goto loc_0037E2D7;
    if (*(unsigned __int64 *)(a1 + 35248) == 0) goto loc_0037E295;
    if (*(unsigned __int64 *)(a1 + 35256) == 0) goto loc_0037E295;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 35256) + 112)) != 0) goto loc_0037E28E;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 35256) + 80)))) < ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 35248) + 528))))) goto loc_0037E295;
    goto loc_0037E295;
loc_0037E28E:
loc_0037E295:
loc_0037E29E:
    if (((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 35248) + 528)) + 132)))) <= ((unsigned int)(*(unsigned __int16 *)(a1 + 35434)))) goto loc_0037E2B1;
    a1 = (unsigned int)((0) + 1);
    a2 = (a1 + 35434) + (2);
    if (((unsigned int)(a1)) < 3) goto loc_0037E29E;
loc_0037E2B1:
    v_rdi = ((*(unsigned __int8 *)(a1 + 35336)) != 0) ? 1 : 0;
    v_rdi = (v_rdi) + (0x10F0ULL);
    a1 = (*(unsigned __int64 *)(a1 + v_rdi + (unsigned int)((unsigned int)(a1)) * 2 * 8)) + (v_r11);
    *(unsigned __int64 *)(a1 + v_rdi + (unsigned int)((unsigned int)(a1)) * 2 * 8) = a1;
loc_0037E2D7:
    if (((*(unsigned __int8 *)(a2 + 2)) & (64)) == 0) goto loc_0037E2ED;
    if (*(unsigned __int64 *)(a2 + 968) != 0) {
        *(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 968) + 64) = 1;
    }
    *(unsigned __int64 *)(a1 + 34552) = result;
    *(unsigned __int64 *)(a1 + 34432) = a2;
    if (((*(unsigned __int8 *)(a2 + 2)) & (2)) == 0) goto loc_0037E343;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 360) + 32) == 0) goto loc_0037E343;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11437553))) == 0) goto loc_0037E343;
loc_0037E329:
    if (((1) & (*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 360) + 32))) != 0) goto loc_0037E673;
loc_0037E332:
    v_r13 = (1) + (1);
    v_r10 = (*(unsigned __int64 *)(a2 + 360) + 48) + (24);
    a4 = (v_rip + 12135262) + (4);
    v_r11 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11437553))))) - (1);
    if (condition_is_not_equal) goto loc_0037E329;
loc_0037E343:
    *(unsigned __int8 *)(a1 + 32) = 0;
    if ((*(unsigned __int8 *)(a1 + 6)) != 0) goto loc_0037E5BE;
loc_0037E352:
    v_rsp = (v_rsp) + (88);
    return v_stack_m68;
loc_0037E369:
    if (*(unsigned __int64 *)(a2 + 104) == 0) goto loc_0037E38A;
    result = ((unsigned int)(*(unsigned int *)(a1 + 216))) + (*(unsigned __int64 *)(a2 + 104));
loc_0037E37B:
    if (*(unsigned __int64 *)(result + 416) != 0) goto loc_0037E37B;
loc_0037E38A:
    if (((*(unsigned __int8 *)(a2 + 2)) & (8)) == 0) goto loc_0037E39D;
    if ((*(unsigned __int64 *)(a2 + 544)) != a4) goto loc_0037E62E;
loc_0037E39D:
    if ((*(unsigned __int64 *)(a2 + 360)) == v_rdi) goto loc_0037E1B9;
    result = KiEndCounterAccumulation(a2, a1 + v_rdi + (unsigned int)((unsigned int)(a1)) * 2 * 8, *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 360) + 32), a4);
    goto loc_0037E1B9;
loc_0037E3B7:
    if ((*(unsigned __int64 *)(result)) == v_rdi) goto loc_0037E234;
    v_stack_pB0 = v_rdi;
    v_stack_p28 = v_rdi;
    if ((unsigned __int8)(result) == 0) goto loc_0037E5D9;
    a2 = (a1 + v_rdi + (unsigned int)((unsigned int)(a1)) * 2 * 8) << ((unsigned __int8)((unsigned __int8)(result)));
    a3 = (result) << ((unsigned __int8)((unsigned __int8)(result)));
loc_0037E407:
    v_stack_pB0 = a2;
    v_stack_p28 = a2;
    v_r10 = (a2) >> ((unsigned __int8)((__int8)(*(unsigned __int8 *)(v_rip + 12879800))));
    a2 = (a2) >> ((unsigned __int8)((__int8)(*(unsigned __int8 *)(v_rip + 12879800))));
    a2 = (unsigned int)((a2) - ((unsigned int)(v_r10)));
    if (condition_is_equal) goto loc_0037E234;
    goto loc_0037E234;
loc_0037E45E:
    a2 = ((unsigned int)((unsigned int)(a3))) + ((unsigned int)((unsigned int)(a3)));
    a1 = (*(unsigned __int64 *)(a2 + a2 * 8 + 8)) + (v_r14);
    *(unsigned __int64 *)(a2 + a2 * 8 + 8) = a1;
    goto loc_0037E110;
loc_0037E476:
    a1 = (*(unsigned __int64 *)(a1 + *(unsigned __int8 *)(a2 + 124) * 8 + 34440)) + (v_r14);
    *(unsigned __int64 *)(a1 + *(unsigned __int8 *)(a2 + 124) * 8 + 34440) = a1;
    v_rbp = (unsigned __int8)((result) & (239));
    goto loc_0037E024;
loc_0037E498:
    if (*(unsigned __int64 *)(a2 + 968) == 0) goto loc_0037E178;
    *(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 968) + 64) = (unsigned __int8)(v_rdi);
    goto loc_0037E178;
loc_0037E4B1:
    if (((*(unsigned int *)(a2 + 116)) & (0x400ULL)) != 0) goto loc_0037E4E3;
    result = (v_r11) >> (4);
    result = (unsigned int)((result) & (31));
    if (((unsigned int)(result)) >= ((unsigned int)(a1 + *(unsigned __int8 *)(a2 + 124) * 8))) goto loc_0037E4E3;
    goto loc_0037E4F1;
loc_0037E4E3:
loc_0037E4F1:
    if (a2 == (*(unsigned __int64 *)(a1 + 24))) goto loc_0037DF5F;
    if ((*(unsigned __int8 *)(a2 + 195)) >= 16) goto loc_0037E566;
    if (*(unsigned __int64 *)(a2 + 104) == 0) goto loc_0037E566;
    if (*(unsigned __int64 *)(a2 + 104) == 0) goto loc_0037E566;
    a1 = ((unsigned int)(*(unsigned int *)(a1 + 216))) + (*(unsigned __int64 *)(a2 + 104));
    if ((*(unsigned __int8 *)(a2 + 195)) >= 16) goto loc_0037E55F;
    if (((*(unsigned int *)(a2 + 120)) & (512)) != 0) goto loc_0037E55F;
loc_0037E536:
    if (((*(unsigned __int8 *)(a1 + 112)) & (2)) != 0) goto loc_0037E56F;
    if (*(unsigned __int64 *)(a1 + 416) != 0) goto loc_0037E536;
loc_0037E548:
    a4 = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) + (*(unsigned int *)(a1 + 124)));
    if (condition_is_not_equal) goto loc_0037E55A;
    if (*(unsigned __int64 *)(a1 + 416) != 0) goto loc_0037E548;
loc_0037E55A:
    if ((unsigned int)(a4) != 0) goto loc_0037E56F;
loc_0037E55F:
loc_0037E566:
    if ((*(unsigned __int8 *)(a2 + 195)) >= 8) goto loc_0037DF5F;
loc_0037E56F:
    goto loc_0037DF5F;
loc_0037E57B:
    v_stack_pA8 = (unsigned int)(*(unsigned __int64 *)(a2 + 104));
    a2 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int64 *)(a2 + 104)))) - ((unsigned int)(*(unsigned __int64 *)(a1 + 416))));
    if (((unsigned int)(a2)) >= 32) goto loc_0037E5B4;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a4 + 196))) << ((unsigned __int8)((unsigned int)((unsigned int)(a2)))));
    result = (unsigned int)((result) | ((unsigned int)(v_r13)));
    v_stack_pAC = (unsigned int)(result);
loc_0037E5A0:
    *(unsigned __int64 *)(a4 + 192) = v_stack_pA8;
    goto loc_0037E0EA;
loc_0037E5B4:
    v_stack_pAC = (unsigned int)(v_r13);
    goto loc_0037E5A0;
loc_0037E5BE:
    *(unsigned __int8 *)(a1 + 6) = 0;
    result = HalRequestSoftwareInterrupt(2, a2, a3, a4);
    goto loc_0037E352;
loc_0037E5CE:
    goto loc_0037DF16;
loc_0037E5D9:
    goto loc_0037E407;
loc_0037E5E1:
    if (((unsigned int)(*(unsigned __int8 *)(a2 + 516))) >= 7) goto loc_0037E1AF;
    a2 = (unsigned int)(*(unsigned int *)(a2 + 80));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 80)))) <= ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 84))))) { a2 = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 84))); }
    a1 = (((unsigned int)(a2)) >= (*(unsigned int *)(v_rip + 12873070))) ? 1 : 0;
    a1 = (unsigned int)((a1 + (unsigned int)((unsigned int)(*(unsigned __int8 *)(a2 + 516))) * 2) * (*(unsigned int *)(v_rip + 12873156)));
    a1 = (unsigned int)((a1) + ((unsigned int)(*(unsigned __int8 *)(a2 + 517))));
    goto loc_0037E1AF;
loc_0037E62E:
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 192) + 128)) & (*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 576) + *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 192) + 136) * 8 + 8));
    if (result == (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 192) + 128))) goto loc_0037E39D;
    goto loc_0037E39D;
loc_0037E66B:
    goto loc_0037E07B;
loc_0037E673:
    a2 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 35248) + 528)) + 132))))) << (32);
    result = (result) | (a2);
    *(unsigned __int64 *)(v_r10) = result;
    goto loc_0037E332;
}
```

## 5. (Beta) C Style

```c
int64_t KiUpdateTotalCyclesCurrentThread(void *Arg1, void *Arg2, int64_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m78;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint32_t v_stack_p8;
    uint32_t v_stack_pA8;
    uint32_t v_stack_pAC;
    uint64_t v_stack_pB0;

    v_stack_p18 = Arg3;
    local_rsp = (local_rsp) - (88);
    local_rdi = 0;
    *(uint8_t *)(arg1 + 0x20) = 1;
    if ((*(uint8_t *)(arg1 + 0x86DC)) == 0) goto loc_0037DF5F;
    Arg1 = 0;
    result = KeQueryPerformanceCounter(Arg1, Arg2, Arg3, a4);
    v_stack_m60 = 0;
    if ((uint8_t)(*(uint8_t *)(arg1 + 0xAC)) != 0) {
        Arg2 = (result) << ((uint8_t)(*(uint8_t *)(arg1 + 0xAC)));
    }
    v_stack_m60 = Arg2;
    local_r14 = (Arg2) - (*(uint64_t *)(arg1 + 0x8680));
    if ((*(uint8_t *)(v_rip + 0xC48BC6)) == 0) goto loc_0037DF5F;
    if ((*(uint64_t *)(local_rbp)) == 0) goto loc_0037DF5F;
    v_stack_p20 = 0;
    v_stack_m78 = 0;
    if ((uint8_t)(*(uint64_t *)(arg1 + 0xB0)) == 0) goto loc_0037E5CE;
    Arg3 = (*(uint64_t *)(arg1 + 0x86F8)) << ((uint8_t)((uint8_t)(*(uint64_t *)(arg1 + 0xB0))));
    Arg3 = (result) << ((uint8_t)((uint8_t)(*(uint64_t *)(arg1 + 0xB0))));
loc_0037DF16:
    v_stack_p20 = Arg2;
    v_stack_m78 = Arg2;
    local_r10 = (Arg2) >> ((uint8_t)((int8_t)(*(uint8_t *)(v_rip + 0xC48CA9))));
    Arg3 = (Arg2) >> ((uint8_t)((int8_t)(*(uint8_t *)(v_rip + 0xC48CA9))));
    Arg3 = (uint32_t)((Arg3) - ((uint32_t)(local_r10)));
    if (condition_is_not_equal) goto loc_0037E4B1;
loc_0037DF5F:
    *(uint64_t *)(arg1 + 0x86F8) = result;
    *(void **)(arg1 + 0x8680) = Arg2;
    result = (*(uint64_t *)(arg2 + 0x48)) + (local_r14);
    *(uint64_t *)(arg2 + 0x48) = result;
    v_stack_m68 = result;
    if (Arg2 != (*(uint64_t *)(arg1 + 0x18))) {
        result = *(uint32_t *)(arg1 + 0x86B8);
        Arg1 = *(uint32_t *)(arg2 + 0x50);
        result = (result) * (local_r14);
        result = (result) >> (16);
        Arg1 = (Arg1) + (result);
        result = 0xFFFFFFFFULL;
        if (Arg1 > result) { Arg1 = result; }
        *(uint32_t *)(arg2 + 0x50) = (uint32_t)(Arg1);
    }
    if ((((uint8_t)(*(uint8_t *)(arg2 + 0x2))) & (190)) == 0) goto loc_0037E1B9;
    local_rbp = *(uint8_t *)(arg2 + 0x2);
    if (sign_flag) {
        result = *(uint64_t *)(arg2 + 0x220);
        Arg2 = 1;
        Arg3 = *(uint64_t *)(arg1 + 0x8BB0);
        a4 = *(uint32_t *)(result + 0x190);
        result = (uint32_t)(a4);
        result = (uint32_t)((result) >> (13));
        result = (uint32_t)((result) & (0x3FFFFULL));
        a4 = (a4) >> (4);
        a4 = (uint32_t)((a4) & (511));
        Arg2 = (uint32_t)((Arg2) << ((uint8_t)(Arg1)));
        Arg1 = (uint32_t)((Arg1) + (-2));
        Arg2 = (uint32_t)((Arg2) ^ ((uint32_t)(result)));
        v_stack_p8 = (uint32_t)(Arg1);
        Arg1 = *(uint64_t *)(Arg3 + arg1 * 8);
        Arg2 = *(uint64_t *)(arg1 + arg2 * 8 + 0x8);
        result = *(uint64_t *)(arg2 + a4 * 8);
        result = (result) + (local_r14);
        *(uint64_t *)(arg2 + a4 * 8) = result;
        local_rbp = (uint8_t)((*(uint8_t *)(arg2 + 0x2)) & (127));
    }
    if ((((uint8_t)(local_rbp)) & (16)) != 0) goto loc_0037E476;
loc_0037E024:
    if ((((uint8_t)(local_rbp)) & (32)) == 0) goto loc_0037E16E;
    if (*(uint64_t *)(arg2 + 0x688) == 0) goto loc_0037E16A;
    if (*(uint64_t *)(arg1 + 0x89B0) == 0) goto loc_0037E66B;
    if (*(uint64_t *)(arg1 + 0x89B8) == 0) goto loc_0037E66B;
    if ((*(uint8_t *)(*(uint64_t *)(arg1 + 0x89B8) + 0x70)) != 0) goto loc_0037E075;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x89B8) + 0x50)))) < ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x89B0) + 0x210))))) goto loc_0037E07B;
    goto loc_0037E07B;
loc_0037E075:
loc_0037E07B:
loc_0037E085:
    if (((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x89B0) + 0x210)) + 0x84)))) <= ((uint32_t)(*(uint16_t *)(arg1 + 0x8A6A)))) goto loc_0037E099;
    Arg3 = (uint32_t)((0) + 1);
    Arg1 = (Arg1 + 35434) + (2);
    if (((uint32_t)(Arg3)) < 3) goto loc_0037E085;
loc_0037E099:
    result = (uint8_t)(-((uint8_t)(*(uint8_t *)(arg1 + 0x8A08))));
    Arg2 = ((uint32_t)((uint32_t)(Arg3))) + ((uint32_t)((uint32_t)(Arg3)));
    Arg1 = (uint32_t)((Arg1) & (8));
    Arg1 = (*(uint64_t *)(*(uint64_t *)(arg2 + 0x688) + arg1 * 1 + arg2 * 8)) + (local_r14);
    *(void **)(*(uint64_t *)(arg2 + 0x688) + arg1 * 1 + arg2 * 8) = Arg1;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB9297C)))) > ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x688) + 0xC0))))) goto loc_0037E57B;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x688) + 0xC0))) - ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB9297C)))));
    result = (uint32_t)(*(uint32_t *)(v_rip + 0xB9297C));
    if (((uint32_t)(Arg1)) < 32) {
        result = 1;
        result = (uint32_t)((result) << ((uint8_t)(Arg1)));
    }
    if ((*(uint32_t *)(v_rip + 0xC48C70)) != 0) goto loc_0037E110;
    if ((((uint32_t)(*(uint8_t *)(arg2 + 0x204) - 2)) & (0xFFFFFFFBULL)) == 0) goto loc_0037E45E;
    if (((uint8_t)(*(uint8_t *)(arg2 + 0x204))) == 5) goto loc_0037E45E;
loc_0037E110:
    result = *(uint8_t *)(arg2 + 0x204) - 2;
    if ((*(uint64_t *)(arg2 + 0x650)) != 0) {
        result = (uint8_t)(*(uint8_t *)(arg1 + 0x8A08));
        Arg1 = (uint32_t)(Arg3);
        Arg1 = (Arg1) + (8);
        Arg1 = (Arg1) + (Arg1);
        result = (uint8_t)(-(result));
        Arg2 = (uint32_t)((Arg2) & (8));
        result = *(uint64_t *)(arg2 + 0x688) + Arg1 * 8;
        Arg1 = *(uint64_t *)(arg2 + result * 1);
        Arg1 = (Arg1) + (local_r14);
        *(void **)(arg2 + result * 1) = Arg1;
        result = *(uint64_t *)(arg2 + 0x650);
        Arg2 = 72;
        Arg1 = *(uint64_t *)(result + 0x688);
        result = 64;
        if ((uint8_t)(*(uint8_t *)(arg1 + 0x8A08)) != 0) { result = (uint32_t)(Arg2); }
        Arg2 = (uint32_t)(Arg3);
        Arg2 = (Arg2) + (Arg2);
        result = (result) + (Arg1);
    }
    local_rbp = (uint8_t)((local_rbp) & (223));
loc_0037E16E:
    if ((((uint8_t)(local_rbp)) & (64)) != 0) goto loc_0037E498;
loc_0037E178:
    if ((*(uint8_t *)(v_rip + 0xC4895F)) != 0) {
        a4 = 0;
        Arg3 = local_r14;
        Arg2 = Arg2;
        Arg1 = Arg1;
        result = KiUpdateThreadHgsFeedback(Arg1, Arg2, Arg3, a4);
    }
    if ((*(uint64_t *)(arg1 + 0x86B0)) == 0) goto loc_0037E1AF;
    if ((*(uint64_t *)(arg2 + 0x220)) != (v_rip + 12918119)) goto loc_0037E5E1;
loc_0037E1AF:
    if ((((uint8_t)(local_rbp)) & (190)) != 0) goto loc_0037E369;
loc_0037E1B9:
    if (v_stack_p18 != 0) {
        *(void **)(v_stack_p18) = Arg2;
    }
    if ((*(uint8_t *)(arg1 + 0x86DC)) == 0) goto loc_0037E234;
    Arg1 = 0;
    result = KeQueryPerformanceCounter(Arg1, Arg2, Arg3, v_rip + 12918119);
    v_stack_m58 = 0;
    if ((uint8_t)(*(uint8_t *)(arg1 + 0xAC)) != 0) {
        Arg2 = (result) << ((uint8_t)(*(uint8_t *)(arg1 + 0xAC)));
    }
    v_stack_m58 = Arg2;
    local_r11 = (Arg2) - (*(uint64_t *)(arg1 + 0x8680));
    local_r14 = (result) - (*(uint64_t *)(arg1 + 0x86F8));
    if ((*(uint8_t *)(v_rip + 0xC48867)) != 0) goto loc_0037E3B7;
loc_0037E234:
    Arg1 = (*(uint64_t *)(arg1 + 0x8700)) + (local_r14);
    *(void **)(arg1 + 0x8700) = Arg1;
    Arg1 = (*(uint64_t *)(arg1 + 0x8778)) + (local_r11);
    *(void **)(arg1 + 0x8778) = Arg1;
    if (((*(uint8_t *)(arg2 + 0x2)) & (32)) == 0) goto loc_0037E2D7;
    if (*(uint64_t *)(arg1 + 0x89B0) == 0) goto loc_0037E295;
    if (*(uint64_t *)(arg1 + 0x89B8) == 0) goto loc_0037E295;
    if ((*(uint8_t *)(*(uint64_t *)(arg1 + 0x89B8) + 0x70)) != 0) goto loc_0037E28E;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x89B8) + 0x50)))) < ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x89B0) + 0x210))))) goto loc_0037E295;
    goto loc_0037E295;
loc_0037E28E:
loc_0037E295:
loc_0037E29E:
    if (((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x89B0) + 0x210)) + 0x84)))) <= ((uint32_t)(*(uint16_t *)(arg1 + 0x8A6A)))) goto loc_0037E2B1;
    Arg1 = (uint32_t)((0) + 1);
    Arg2 = (Arg1 + 35434) + (2);
    if (((uint32_t)(Arg1)) < 3) goto loc_0037E29E;
loc_0037E2B1:
    local_rdi = ((*(uint8_t *)(arg1 + 0x8A08)) != 0) ? 1 : 0;
    local_rdi = (local_rdi) + (0x10F0ULL);
    Arg1 = (*(uint64_t *)(arg1 + local_rdi + (uint32_t)((uint32_t)(arg1)) * 2 * 8)) + (local_r11);
    *(void **)(arg1 + local_rdi + (uint32_t)((uint32_t)(arg1)) * 2 * 8) = Arg1;
loc_0037E2D7:
    if (((*(uint8_t *)(arg2 + 0x2)) & (64)) == 0) goto loc_0037E2ED;
    if (*(uint64_t *)(arg2 + 0x3C8) != 0) {
        *(uint8_t *)(*(uint64_t *)(arg2 + 0x3C8) + 0x40) = 1;
    }
    *(uint64_t *)(arg1 + 0x86F8) = result;
    *(void **)(arg1 + 0x8680) = Arg2;
    if (((*(uint8_t *)(arg2 + 0x2)) & (2)) == 0) goto loc_0037E343;
    if (*(uint64_t *)(*(uint64_t *)(arg2 + 0x168) + 0x20) == 0) goto loc_0037E343;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xAE85F1))) == 0) goto loc_0037E343;
loc_0037E329:
    if (((1) & (*(uint64_t *)(*(uint64_t *)(arg2 + 0x168) + 0x20))) != 0) goto loc_0037E673;
loc_0037E332:
    local_r13 = (1) + (1);
    local_r10 = (*(uint64_t *)(arg2 + 0x168) + 48) + (24);
    a4 = (v_rip + 12135262) + (4);
    local_r11 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xAE85F1))))) - (1);
    if (condition_is_not_equal) goto loc_0037E329;
loc_0037E343:
    *(uint8_t *)(arg1 + 0x20) = 0;
    if ((*(uint8_t *)(arg1 + 0x6)) != 0) goto loc_0037E5BE;
loc_0037E352:
    local_rsp = (local_rsp) + (88);
    return v_stack_m68;
loc_0037E369:
    if (*(uint64_t *)(arg2 + 0x68) == 0) goto loc_0037E38A;
    result = ((uint32_t)(*(uint32_t *)(arg1 + 0xD8))) + (*(uint64_t *)(arg2 + 0x68));
loc_0037E37B:
    if (*(uint64_t *)(result + 0x1A0) != 0) goto loc_0037E37B;
loc_0037E38A:
    if (((*(uint8_t *)(arg2 + 0x2)) & (8)) == 0) goto loc_0037E39D;
    if ((*(uint64_t *)(arg2 + 0x220)) != a4) goto loc_0037E62E;
loc_0037E39D:
    if ((*(uint64_t *)(arg2 + 0x168)) == local_rdi) goto loc_0037E1B9;
    result = KiEndCounterAccumulation(Arg2, Arg1 + local_rdi + (uint32_t)((uint32_t)(Arg1)) * 2 * 8, *(uint64_t *)(*(uint64_t *)(arg2 + 0x168) + 0x20), a4);
    goto loc_0037E1B9;
loc_0037E3B7:
    if ((*(uint64_t *)(result)) == local_rdi) goto loc_0037E234;
    v_stack_pB0 = local_rdi;
    v_stack_p28 = local_rdi;
    if ((uint8_t)(result) == 0) goto loc_0037E5D9;
    Arg2 = (Arg1 + local_rdi + (uint32_t)((uint32_t)(Arg1)) * 2 * 8) << ((uint8_t)((uint8_t)(result)));
    Arg3 = (result) << ((uint8_t)((uint8_t)(result)));
loc_0037E407:
    v_stack_pB0 = Arg2;
    v_stack_p28 = Arg2;
    local_r10 = (Arg2) >> ((uint8_t)((int8_t)(*(uint8_t *)(v_rip + 0xC487B8))));
    Arg2 = (Arg2) >> ((uint8_t)((int8_t)(*(uint8_t *)(v_rip + 0xC487B8))));
    Arg2 = (uint32_t)((Arg2) - ((uint32_t)(local_r10)));
    if (condition_is_equal) goto loc_0037E234;
    goto loc_0037E234;
loc_0037E45E:
    Arg2 = ((uint32_t)((uint32_t)(Arg3))) + ((uint32_t)((uint32_t)(Arg3)));
    Arg1 = (*(uint64_t *)(arg2 + arg2 * 8 + 0x8)) + (local_r14);
    *(void **)(arg2 + arg2 * 8 + 0x8) = Arg1;
    goto loc_0037E110;
loc_0037E476:
    Arg1 = (*(uint64_t *)(arg1 + *(uint8_t *)(arg2 + 0x7C) * 8 + 0x8688)) + (local_r14);
    *(void **)(arg1 + *(uint8_t *)(arg2 + 0x7C) * 8 + 0x8688) = Arg1;
    local_rbp = (uint8_t)((result) & (239));
    goto loc_0037E024;
loc_0037E498:
    if (*(uint64_t *)(arg2 + 0x3C8) == 0) goto loc_0037E178;
    *(uint8_t *)(*(uint64_t *)(arg2 + 0x3C8) + 0x40) = (uint8_t)(local_rdi);
    goto loc_0037E178;
loc_0037E4B1:
    if (((*(uint32_t *)(arg2 + 0x74)) & (0x400ULL)) != 0) goto loc_0037E4E3;
    result = (local_r11) >> (4);
    result = (uint32_t)((result) & (31));
    if (((uint32_t)(result)) >= ((uint32_t)(Arg1 + *(uint8_t *)(arg2 + 0x7C) * 8))) goto loc_0037E4E3;
    goto loc_0037E4F1;
loc_0037E4E3:
loc_0037E4F1:
    if (Arg2 == (*(uint64_t *)(arg1 + 0x18))) goto loc_0037DF5F;
    if ((*(uint8_t *)(arg2 + 0xC3)) >= 16) goto loc_0037E566;
    if (*(uint64_t *)(arg2 + 0x68) == 0) goto loc_0037E566;
    if (*(uint64_t *)(arg2 + 0x68) == 0) goto loc_0037E566;
    Arg1 = ((uint32_t)(*(uint32_t *)(arg1 + 0xD8))) + (*(uint64_t *)(arg2 + 0x68));
    if ((*(uint8_t *)(arg2 + 0xC3)) >= 16) goto loc_0037E55F;
    if (((*(uint32_t *)(arg2 + 0x78)) & (512)) != 0) goto loc_0037E55F;
loc_0037E536:
    if (((*(uint8_t *)(arg1 + 0x70)) & (2)) != 0) goto loc_0037E56F;
    if (*(uint64_t *)(arg1 + 0x1A0) != 0) goto loc_0037E536;
loc_0037E548:
    a4 = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) + (*(uint32_t *)(arg1 + 0x7C)));
    if (condition_is_not_equal) goto loc_0037E55A;
    if (*(uint64_t *)(arg1 + 0x1A0) != 0) goto loc_0037E548;
loc_0037E55A:
    if ((uint32_t)(a4) != 0) goto loc_0037E56F;
loc_0037E55F:
loc_0037E566:
    if ((*(uint8_t *)(arg2 + 0xC3)) >= 8) goto loc_0037DF5F;
loc_0037E56F:
    goto loc_0037DF5F;
loc_0037E57B:
    v_stack_pA8 = (uint32_t)(*(uint64_t *)(arg2 + 0x68));
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(*(uint64_t *)(arg2 + 0x68)))) - ((uint32_t)(*(uint64_t *)(arg1 + 0x1A0))));
    if (((uint32_t)(Arg2)) >= 32) goto loc_0037E5B4;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(a4 + 0xC4))) << ((uint8_t)((uint32_t)((uint32_t)(Arg2)))));
    result = (uint32_t)((result) | ((uint32_t)(local_r13)));
    v_stack_pAC = (uint32_t)(result);
loc_0037E5A0:
    *(uint64_t *)(a4 + 0xC0) = v_stack_pA8;
    goto loc_0037E0EA;
loc_0037E5B4:
    v_stack_pAC = (uint32_t)(local_r13);
    goto loc_0037E5A0;
loc_0037E5BE:
    *(uint8_t *)(arg1 + 0x6) = 0;
    result = HalRequestSoftwareInterrupt(2, Arg2, Arg3, a4);
    goto loc_0037E352;
loc_0037E5CE:
    goto loc_0037DF16;
loc_0037E5D9:
    goto loc_0037E407;
loc_0037E5E1:
    if (((uint32_t)(*(uint8_t *)(arg2 + 0x204))) >= 7) goto loc_0037E1AF;
    Arg2 = (uint32_t)(*(uint32_t *)(arg2 + 0x50));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x50)))) <= ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x54))))) { Arg2 = (uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x54))); }
    Arg1 = (((uint32_t)(Arg2)) >= (*(uint32_t *)(v_rip + 0xC46D6E))) ? 1 : 0;
    Arg1 = (uint32_t)((Arg1 + (uint32_t)((uint32_t)(*(uint8_t *)(arg2 + 0x204))) * 2) * (*(uint32_t *)(v_rip + 0xC46DC4)));
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(*(uint8_t *)(arg2 + 0x205))));
    goto loc_0037E1AF;
loc_0037E62E:
    result = (*(uint64_t *)(*(uint64_t *)(arg1 + 0xC0) + 0x80)) & (*(uint64_t *)(*(uint64_t *)(arg2 + 0x240) + *(uint16_t *)(*(uint64_t *)(arg1 + 0xC0) + 0x88) * 8 + 0x8));
    if (result == (*(uint64_t *)(*(uint64_t *)(arg1 + 0xC0) + 0x80))) goto loc_0037E39D;
    goto loc_0037E39D;
loc_0037E66B:
    goto loc_0037E07B;
loc_0037E673:
    Arg2 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x89B0) + 0x210)) + 0x84))))) << (32);
    result = (result) | (Arg2);
    *(uint64_t *)(local_r10) = result;
    goto loc_0037E332;
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
| `Arg1` | `+ 0x20` | `8` | `W` |
| `Arg1` | `+ 0xAC` | `8` | `R` |
| `Arg1` | `+ 0xB0` | `64` | `R` |
| `Arg1` | `+ 0xC0` | `64` | `R` |
| `Arg1` | `+ 0xD8` | `32` | `R` |
| `Arg1` | `+ 0x8644` | `32` | `R/W` |
| `Arg1` | `+ 0x8648` | `32` | `R/W` |
| `Arg1` | `+ 0x8650` | `32` | `R/W` |
| `Arg1` | `+ 0x866C` | `32` | `R/W` |
| `Arg1` | `+ 0x8680` | `64` | `R` |
| `Arg1` | `+ 0x8680` | `64` | `W` |
| `Arg1` | `+ 0x8688` | `64` | `R` |
| `Arg1` | `+ 0x8688` | `64` | `W` |
| `Arg1` | `+ 0x86A8` | `64` | `R/W` |
| `Arg1` | `+ 0x86B0` | `64` | `R` |
| `Arg1` | `+ 0x86B8` | `32` | `R` |
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

추가 오프셋 6개는 표에서 생략했습니다.

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0037DE40&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
