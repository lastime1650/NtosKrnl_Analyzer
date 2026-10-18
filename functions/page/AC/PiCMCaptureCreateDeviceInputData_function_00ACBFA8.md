# PiCMCaptureCreateDeviceInputData

- RVA: `0x00ACBFA8`–`0x00ACC40F` (길이 `1,127` bytes)
- VA: `0x0000000140ACBFA8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BE50C`
- 디코드: `293`개 명령, `1,127/1,127` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **10**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00ACC018` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x00ACC0C7` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x00ACC176` → [Feature_KernelPnP_ObjectNameUpdates__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_KernelPnP_ObjectNameUpdates__private_IsEnabledDeviceUsageNoInline_function_004F2E10.md) (function, `0x004F2E10`)
- `0x00ACC1BE` → [PiControlMakeUserModeCallersCopy](../8E/PiControlMakeUserModeCallersCopy_function_008E4630.md) (function, `0x008E4630`)
- `0x00ACC215` → [PiControlFreeUserModeCallersBuffer](../../text/44/PiControlFreeUserModeCallersBuffer_function_00448990.md) (function, `0x00448990`)
- `0x00ACC22A` → [PiControlFreeUserModeCallersBuffer](../../text/44/PiControlFreeUserModeCallersBuffer_function_00448990.md) (function, `0x00448990`)
- `0x00ACC291` → [PiControlMakeUserModeCallersCopy](../8E/PiControlMakeUserModeCallersCopy_function_008E4630.md) (function, `0x008E4630`)
- `0x00ACC2F7` → [Feature_KernelPnP_ObjectNameUpdates__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_KernelPnP_ObjectNameUpdates__private_IsEnabledDeviceUsageNoInline_function_004F2E10.md) (function, `0x004F2E10`)
- `0x00ACC331` → [PiControlMakeUserModeCallersCopy](../8E/PiControlMakeUserModeCallersCopy_function_008E4630.md) (function, `0x008E4630`)
- `0x00ACC395` → [PiControlMakeUserModeCallersCopy](../8E/PiControlMakeUserModeCallersCopy_function_008E4630.md) (function, `0x008E4630`)

### Direct callers
- [PiCMCreateDevice](PiCMCreateDevice_function_00ACB824.md) at `0x00ACB8BC`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **4**
  - `0x00ACC176` → [Feature_KernelPnP_ObjectNameUpdates__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_KernelPnP_ObjectNameUpdates__private_IsEnabledDeviceUsageNoInline_function_004F2E10.md) (`PAGE` → `.text`)
  - `0x00ACC215` → [PiControlFreeUserModeCallersBuffer](../../text/44/PiControlFreeUserModeCallersBuffer_function_00448990.md) (`PAGE` → `.text`)
  - `0x00ACC22A` → [PiControlFreeUserModeCallersBuffer](../../text/44/PiControlFreeUserModeCallersBuffer_function_00448990.md) (`PAGE` → `.text`)
  - `0x00ACC2F7` → [Feature_KernelPnP_ObjectNameUpdates__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_KernelPnP_ObjectNameUpdates__private_IsEnabledDeviceUsageNoInline_function_004F2E10.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00ACBFA8  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
00ACBFAD  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
00ACBFB2  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
00ACBFB7  57                              push rdi
00ACBFB8  41 54                           push r12
00ACBFBA  41 55                           push r13
00ACBFBC  41 56                           push r14
00ACBFBE  41 57                           push r15
00ACBFC0  48 83 EC 50                     sub rsp, 0x50
00ACBFC4  49 8B F1                        mov rsi, r9
00ACBFC7  4D 8B E1                        mov r12, r9
00ACBFCA  4C 89 4C 24 48                  mov qword ptr [rsp + 0x48], r9
00ACBFCF  33 DB                           xor ebx, ebx
00ACBFD1  89 5C 24 3C                     mov dword ptr [rsp + 0x3c], ebx
00ACBFD5  89 5C 24 34                     mov dword ptr [rsp + 0x34], ebx
00ACBFD9  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00ACBFE2  8A 80 32 02 00 00               mov al, byte ptr [rax + 0x232]
00ACBFE8  88 84 24 80 00 00 00            mov byte ptr [rsp + 0x80], al
00ACBFEF  88 44 24 30                     mov byte ptr [rsp + 0x30], al
00ACBFF3  8B FB                           mov edi, ebx
00ACBFF5  89 5C 24 38                     mov dword ptr [rsp + 0x38], ebx
00ACBFF9  48 85 C9                        test rcx, rcx
00ACBFFC  0F 84 00 04 00 00               je 0x140acc402
00ACC002  85 D2                           test edx, edx
00ACC004  0F 84 F8 03 00 00               je 0x140acc402
00ACC00A  45 85 C0                        test r8d, r8d
00ACC00D  0F 84 AF 00 00 00               je 0x140acc0c2
00ACC013  F6 C1 03                        test cl, 3
00ACC016  74 05                           je 0x140acc01d
00ACC018  E8 B3 DF DC FF                  call 0x140899fd0
00ACC01D  44 8B C2                        mov r8d, edx
00ACC020  4C 03 C1                        add r8, rcx
00ACC023  48 B8 00 00 FF FF FF 7F 00 00   movabs rax, 0x7fffffff0000
00ACC02D  4C 3B C0                        cmp r8, rax
00ACC030  77 05                           ja 0x140acc037
00ACC032  4C 3B C1                        cmp r8, rcx
00ACC035  73 06                           jae 0x140acc03d
00ACC037  8A 00                           mov al, byte ptr [rax]
00ACC039  8B 7C 24 38                     mov edi, dword ptr [rsp + 0x38]
00ACC03D  41 BE 0D 00 00 C0               mov r14d, 0xc000000d
00ACC043  83 FA 1C                        cmp edx, 0x1c
00ACC046  73 0A                           jae 0x140acc052
00ACC048  41 8B FE                        mov edi, r14d
00ACC04B  44 89 74 24 38                  mov dword ptr [rsp + 0x38], r14d
00ACC050  EB 36                           jmp 0x140acc088
00ACC052  83 39 1C                        cmp dword ptr [rcx], 0x1c
00ACC055  75 F1                           jne 0x140acc048
00ACC057  41 C7 01 28 00 00 00            mov dword ptr [r9], 0x28
00ACC05E  8B 41 04                        mov eax, dword ptr [rcx + 4]
00ACC061  41 89 41 04                     mov dword ptr [r9 + 4], eax
00ACC065  8B 41 08                        mov eax, dword ptr [rcx + 8]
00ACC068  49 89 41 08                     mov qword ptr [r9 + 8], rax
00ACC06C  8B 41 0C                        mov eax, dword ptr [rcx + 0xc]
00ACC06F  41 89 41 10                     mov dword ptr [r9 + 0x10], eax
00ACC073  8B 41 10                        mov eax, dword ptr [rcx + 0x10]
00ACC076  49 89 41 18                     mov qword ptr [r9 + 0x18], rax
00ACC07A  8B 41 14                        mov eax, dword ptr [rcx + 0x14]
00ACC07D  41 89 41 20                     mov dword ptr [r9 + 0x20], eax
00ACC081  8B 41 18                        mov eax, dword ptr [rcx + 0x18]
00ACC084  41 89 41 24                     mov dword ptr [r9 + 0x24], eax
00ACC088  8A 84 24 80 00 00 00            mov al, byte ptr [rsp + 0x80]
00ACC08F  EB 2C                           jmp 0x140acc0bd
00ACC091  8B F8                           mov edi, eax
00ACC093  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
00ACC097  33 DB                           xor ebx, ebx
00ACC099  41 BE 0D 00 00 C0               mov r14d, 0xc000000d
00ACC09F  48 8B B4 24 98 00 00 00         mov rsi, qword ptr [rsp + 0x98]
00ACC0A7  8B C3                           mov eax, ebx
00ACC0A9  89 5C 24 3C                     mov dword ptr [rsp + 0x3c], ebx
00ACC0AD  8A 44 24 30                     mov al, byte ptr [rsp + 0x30]
00ACC0B1  88 84 24 80 00 00 00            mov byte ptr [rsp + 0x80], al
00ACC0B8  4C 8B 64 24 48                  mov r12, qword ptr [rsp + 0x48]
00ACC0BD  E9 9B 00 00 00                  jmp 0x140acc15d
00ACC0C2  F6 C1 07                        test cl, 7
00ACC0C5  74 05                           je 0x140acc0cc
00ACC0C7  E8 04 DF DC FF                  call 0x140899fd0
00ACC0CC  44 8B C2                        mov r8d, edx
00ACC0CF  4C 03 C1                        add r8, rcx
00ACC0D2  48 B8 00 00 FF FF FF 7F 00 00   movabs rax, 0x7fffffff0000
00ACC0DC  4C 3B C0                        cmp r8, rax
00ACC0DF  77 05                           ja 0x140acc0e6
00ACC0E1  4C 3B C1                        cmp r8, rcx
00ACC0E4  73 06                           jae 0x140acc0ec
00ACC0E6  8A 00                           mov al, byte ptr [rax]
00ACC0E8  8B 7C 24 38                     mov edi, dword ptr [rsp + 0x38]
00ACC0EC  41 BE 0D 00 00 C0               mov r14d, 0xc000000d
00ACC0F2  83 FA 28                        cmp edx, 0x28
00ACC0F5  73 0A                           jae 0x140acc101
00ACC0F7  41 8B FE                        mov edi, r14d
00ACC0FA  44 89 74 24 38                  mov dword ptr [rsp + 0x38], r14d
00ACC0FF  EB 27                           jmp 0x140acc128
00ACC101  0F 10 01                        movups xmm0, xmmword ptr [rcx]
00ACC104  41 0F 11 01                     movups xmmword ptr [r9], xmm0
00ACC108  0F 10 49 10                     movups xmm1, xmmword ptr [rcx + 0x10]
00ACC10C  41 0F 11 49 10                  movups xmmword ptr [r9 + 0x10], xmm1
00ACC111  F2 0F 10 41 20                  movsd xmm0, qword ptr [rcx + 0x20]
00ACC116  F2 41 0F 11 41 20               movsd qword ptr [r9 + 0x20], xmm0
00ACC11C  41 83 39 28                     cmp dword ptr [r9], 0x28
00ACC120  41 0F 45 FE                     cmovne edi, r14d
00ACC124  89 7C 24 38                     mov dword ptr [rsp + 0x38], edi
00ACC128  8A 84 24 80 00 00 00            mov al, byte ptr [rsp + 0x80]
00ACC12F  EB 2C                           jmp 0x140acc15d
00ACC131  8B F8                           mov edi, eax
00ACC133  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
00ACC137  33 DB                           xor ebx, ebx
00ACC139  41 BE 0D 00 00 C0               mov r14d, 0xc000000d
00ACC13F  48 8B B4 24 98 00 00 00         mov rsi, qword ptr [rsp + 0x98]
00ACC147  8B C3                           mov eax, ebx
00ACC149  89 5C 24 3C                     mov dword ptr [rsp + 0x3c], ebx
00ACC14D  8A 44 24 30                     mov al, byte ptr [rsp + 0x30]
00ACC151  88 84 24 80 00 00 00            mov byte ptr [rsp + 0x80], al
00ACC158  4C 8B 64 24 48                  mov r12, qword ptr [rsp + 0x48]
00ACC15D  85 FF                           test edi, edi
00ACC15F  0F 88 9B 00 00 00               js 0x140acc200
00ACC165  4C 8D 6E 08                     lea r13, [rsi + 8]
00ACC169  4D 8B 7D 00                     mov r15, qword ptr [r13]
00ACC16D  4C 89 7C 24 40                  mov qword ptr [rsp + 0x40], r15
00ACC172  49 89 5D 00                     mov qword ptr [r13], rbx
00ACC176  E8 95 6C A2 FF                  call 0x1404f2e10
00ACC17B  85 C0                           test eax, eax
00ACC17D  0F 84 D9 00 00 00               je 0x140acc25c
00ACC183  8B 4E 10                        mov ecx, dword ptr [rsi + 0x10]
00ACC186  4D 85 FF                        test r15, r15
00ACC189  74 63                           je 0x140acc1ee
00ACC18B  8D 41 FE                        lea eax, [rcx - 2]
00ACC18E  3D 8E 01 00 00                  cmp eax, 0x18e
00ACC193  8A 84 24 80 00 00 00            mov al, byte ptr [rsp + 0x80]
00ACC19A  0F 87 BC 01 00 00               ja 0x140acc35c
00ACC1A0  41 BF 01 00 00 00               mov r15d, 1
00ACC1A6  44 89 7C 24 28                  mov dword ptr [rsp + 0x28], r15d
00ACC1AB  88 44 24 20                     mov byte ptr [rsp + 0x20], al
00ACC1AF  45 8D 4F 01                     lea r9d, [r15 + 1]
00ACC1B3  44 8B C1                        mov r8d, ecx
00ACC1B6  48 8B 54 24 40                  mov rdx, qword ptr [rsp + 0x40]
00ACC1BB  49 8B CD                        mov rcx, r13
00ACC1BE  E8 6D 84 E1 FF                  call 0x1408e4630
00ACC1C3  8B F8                           mov edi, eax
00ACC1C5  85 C0                           test eax, eax
00ACC1C7  78 19                           js 0x140acc1e2
00ACC1C9  44 89 7C 24 3C                  mov dword ptr [rsp + 0x3c], r15d
00ACC1CE  8B 56 10                        mov edx, dword ptr [rsi + 0x10]
00ACC1D1  48 D1 EA                        shr rdx, 1
00ACC1D4  49 8B 4D 00                     mov rcx, qword ptr [r13]
00ACC1D8  66 89 5C 51 FE                  mov word ptr [rcx + rdx*2 - 2], bx
00ACC1DD  E9 04 01 00 00                  jmp 0x140acc2e6
00ACC1E2  49 89 5D 00                     mov qword ptr [r13], rbx
00ACC1E6  89 5E 10                        mov dword ptr [rsi + 0x10], ebx
00ACC1E9  E9 F8 00 00 00                  jmp 0x140acc2e6
00ACC1EE  85 C9                           test ecx, ecx
00ACC1F0  0F 84 EA 00 00 00               je 0x140acc2e0
00ACC1F6  41 8B FE                        mov edi, r14d
00ACC1F9  8A 84 24 80 00 00 00            mov al, byte ptr [rsp + 0x80]
00ACC200  44 8B 74 24 34                  mov r14d, dword ptr [rsp + 0x34]
00ACC205  85 FF                           test edi, edi
00ACC207  79 36                           jns 0x140acc23f
00ACC209  39 5C 24 3C                     cmp dword ptr [rsp + 0x3c], ebx
00ACC20D  74 0B                           je 0x140acc21a
00ACC20F  48 8B 56 08                     mov rdx, qword ptr [rsi + 8]
00ACC213  8A C8                           mov cl, al
00ACC215  E8 76 C7 97 FF                  call 0x140448990
00ACC21A  45 85 F6                        test r14d, r14d
00ACC21D  74 10                           je 0x140acc22f
00ACC21F  48 8B 56 18                     mov rdx, qword ptr [rsi + 0x18]
00ACC223  8A 8C 24 80 00 00 00            mov cl, byte ptr [rsp + 0x80]
00ACC22A  E8 61 C7 97 FF                  call 0x140448990
00ACC22F  0F 57 C0                        xorps xmm0, xmm0
00ACC232  33 C0                           xor eax, eax
00ACC234  0F 11 06                        movups xmmword ptr [rsi], xmm0
00ACC237  0F 11 46 10                     movups xmmword ptr [rsi + 0x10], xmm0
00ACC23B  48 89 46 20                     mov qword ptr [rsi + 0x20], rax
00ACC23F  8B C7                           mov eax, edi
00ACC241  4C 8D 5C 24 50                  lea r11, [rsp + 0x50]
00ACC246  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
00ACC24A  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
00ACC24E  49 8B E3                        mov rsp, r11
00ACC251  41 5F                           pop r15
00ACC253  41 5E                           pop r14
00ACC255  41 5D                           pop r13
00ACC257  41 5C                           pop r12
00ACC259  5F                              pop rdi
00ACC25A  C3                              ret
00ACC25B  CC                              int3
00ACC25C  4D 85 FF                        test r15, r15
00ACC25F  74 5C                           je 0x140acc2bd
00ACC261  4C 8D 66 10                     lea r12, [rsi + 0x10]
00ACC265  45 8B 04 24                     mov r8d, dword ptr [r12]
00ACC269  41 83 F8 02                     cmp r8d, 2
00ACC26D  72 52                           jb 0x140acc2c1
00ACC26F  41 BF 01 00 00 00               mov r15d, 1
00ACC275  44 89 7C 24 28                  mov dword ptr [rsp + 0x28], r15d
00ACC27A  8A 84 24 80 00 00 00            mov al, byte ptr [rsp + 0x80]
00ACC281  88 44 24 20                     mov byte ptr [rsp + 0x20], al
00ACC285  45 8D 4F 01                     lea r9d, [r15 + 1]
00ACC289  48 8B 54 24 40                  mov rdx, qword ptr [rsp + 0x40]
00ACC28E  49 8B CD                        mov rcx, r13
00ACC291  E8 9A 83 E1 FF                  call 0x1408e4630
00ACC296  8B F8                           mov edi, eax
00ACC298  85 C0                           test eax, eax
00ACC29A  78 17                           js 0x140acc2b3
00ACC29C  44 89 7C 24 3C                  mov dword ptr [rsp + 0x3c], r15d
00ACC2A1  41 8B 0C 24                     mov ecx, dword ptr [r12]
00ACC2A5  48 D1 E9                        shr rcx, 1
00ACC2A8  49 8B 45 00                     mov rax, qword ptr [r13]
00ACC2AC  66 89 5C 48 FE                  mov word ptr [rax + rcx*2 - 2], bx
00ACC2B1  EB 33                           jmp 0x140acc2e6
00ACC2B3  49 89 5D 00                     mov qword ptr [r13], rbx
00ACC2B7  41 89 1C 24                     mov dword ptr [r12], ebx
00ACC2BB  EB 29                           jmp 0x140acc2e6
00ACC2BD  49 83 C4 10                     add r12, 0x10
00ACC2C1  4D 85 FF                        test r15, r15
00ACC2C4  75 0F                           jne 0x140acc2d5
00ACC2C6  41 39 1C 24                     cmp dword ptr [r12], ebx
00ACC2CA  0F 87 26 FF FF FF               ja 0x140acc1f6
00ACC2D0  4D 85 FF                        test r15, r15
00ACC2D3  74 0B                           je 0x140acc2e0
00ACC2D5  41 83 3C 24 02                  cmp dword ptr [r12], 2
00ACC2DA  0F 82 16 FF FF FF               jb 0x140acc1f6
00ACC2E0  41 BF 01 00 00 00               mov r15d, 1
00ACC2E6  4C 8D 6E 18                     lea r13, [rsi + 0x18]
00ACC2EA  4D 8B 65 00                     mov r12, qword ptr [r13]
00ACC2EE  4C 89 64 24 40                  mov qword ptr [rsp + 0x40], r12
00ACC2F3  49 89 5D 00                     mov qword ptr [r13], rbx
00ACC2F7  E8 14 6B A2 FF                  call 0x1404f2e10
00ACC2FC  85 C0                           test eax, eax
00ACC2FE  74 64                           je 0x140acc364
00ACC300  8B 4E 20                        mov ecx, dword ptr [rsi + 0x20]
00ACC303  4D 85 E4                        test r12, r12
00ACC306  74 45                           je 0x140acc34d
00ACC308  8D 41 FE                        lea eax, [rcx - 2]
00ACC30B  3D 8E 01 00 00                  cmp eax, 0x18e
00ACC310  8A 84 24 80 00 00 00            mov al, byte ptr [rsp + 0x80]
00ACC317  77 43                           ja 0x140acc35c
00ACC319  44 89 7C 24 28                  mov dword ptr [rsp + 0x28], r15d
00ACC31E  88 44 24 20                     mov byte ptr [rsp + 0x20], al
00ACC322  41 B9 02 00 00 00               mov r9d, 2
00ACC328  44 8B C1                        mov r8d, ecx
00ACC32B  49 8B D4                        mov rdx, r12
00ACC32E  49 8B CD                        mov rcx, r13
00ACC331  E8 FA 82 E1 FF                  call 0x1408e4630
00ACC336  8B F8                           mov edi, eax
00ACC338  85 C0                           test eax, eax
00ACC33A  78 05                           js 0x140acc341
00ACC33C  8B 4E 20                        mov ecx, dword ptr [rsi + 0x20]
00ACC33F  EB 63                           jmp 0x140acc3a4
00ACC341  49 89 5D 00                     mov qword ptr [r13], rbx
00ACC345  89 5E 20                        mov dword ptr [rsi + 0x20], ebx
00ACC348  E9 AC FE FF FF                  jmp 0x140acc1f9
00ACC34D  8A 84 24 80 00 00 00            mov al, byte ptr [rsp + 0x80]
00ACC354  85 C9                           test ecx, ecx
00ACC356  0F 84 A4 FE FF FF               je 0x140acc200
00ACC35C  41 8B FE                        mov edi, r14d
00ACC35F  E9 9C FE FF FF                  jmp 0x140acc200
00ACC364  4D 85 E4                        test r12, r12
00ACC367  74 63                           je 0x140acc3cc
00ACC369  4C 8D 66 20                     lea r12, [rsi + 0x20]
00ACC36D  45 8B 04 24                     mov r8d, dword ptr [r12]
00ACC371  41 83 F8 02                     cmp r8d, 2
00ACC375  72 5E                           jb 0x140acc3d5
00ACC377  44 89 7C 24 28                  mov dword ptr [rsp + 0x28], r15d
00ACC37C  8A 84 24 80 00 00 00            mov al, byte ptr [rsp + 0x80]
00ACC383  88 44 24 20                     mov byte ptr [rsp + 0x20], al
00ACC387  41 B9 02 00 00 00               mov r9d, 2
00ACC38D  48 8B 54 24 40                  mov rdx, qword ptr [rsp + 0x40]
00ACC392  49 8B CD                        mov rcx, r13
00ACC395  E8 96 82 E1 FF                  call 0x1408e4630
00ACC39A  8B F8                           mov edi, eax
00ACC39C  85 C0                           test eax, eax
00ACC39E  78 1F                           js 0x140acc3bf
00ACC3A0  41 8B 0C 24                     mov ecx, dword ptr [r12]
00ACC3A4  45 8B F7                        mov r14d, r15d
00ACC3A7  48 D1 E9                        shr rcx, 1
00ACC3AA  49 8B 45 00                     mov rax, qword ptr [r13]
00ACC3AE  66 89 5C 48 FE                  mov word ptr [rax + rcx*2 - 2], bx
00ACC3B3  8A 84 24 80 00 00 00            mov al, byte ptr [rsp + 0x80]
00ACC3BA  E9 46 FE FF FF                  jmp 0x140acc205
00ACC3BF  49 89 5D 00                     mov qword ptr [r13], rbx
00ACC3C3  41 89 1C 24                     mov dword ptr [r12], ebx
00ACC3C7  E9 2D FE FF FF                  jmp 0x140acc1f9
00ACC3CC  4C 8B 64 24 48                  mov r12, qword ptr [rsp + 0x48]
00ACC3D1  49 83 C4 20                     add r12, 0x20
00ACC3D5  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
00ACC3DA  48 85 C0                        test rax, rax
00ACC3DD  75 13                           jne 0x140acc3f2
00ACC3DF  41 39 1C 24                     cmp dword ptr [r12], ebx
00ACC3E3  0F 87 0D FE FF FF               ja 0x140acc1f6
00ACC3E9  48 85 C0                        test rax, rax
00ACC3EC  0F 84 07 FE FF FF               je 0x140acc1f9
00ACC3F2  41 83 3C 24 02                  cmp dword ptr [r12], 2
00ACC3F7  0F 83 FC FD FF FF               jae 0x140acc1f9
00ACC3FD  E9 F4 FD FF FF                  jmp 0x140acc1f6
00ACC402  BF 0D 00 00 C0                  mov edi, 0xc000000d
00ACC407  44 8B F3                        mov r14d, ebx
00ACC40A  E9 F6 FD FF FF                  jmp 0x140acc205
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PiCMCaptureCreateDeviceInputData(__int64 a1, int a2, int a3, __int64 a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned int v_stack_m14;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned int v_stack_m3C;
    unsigned int v_stack_m40;
    unsigned int v_stack_m44;
    unsigned __int8 v_stack_m48;
    unsigned int v_stack_m50;
    unsigned __int8 v_stack_m58;
    unsigned __int64 v_stack_m8;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int8 v_stack_p30;
    unsigned __int8 v_stack_p8;

    v_stack_p10 = v_rbx;
    v_stack_p18 = v_rsi;
    v_stack_p20 = a4;
    v_rsp = (v_rsp) - (80);
    v_stack_m30 = a4;
    v_rbx = 0;
    v_stack_m3C = 0;
    v_stack_m44 = 0;
    v_stack_p8 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    v_stack_m48 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    v_stack_m40 = 0;
    if (a1 == 0) goto loc_00ACC402;
    if (a2 == 0) goto loc_00ACC402;
    if (a3 == 0) goto loc_00ACC0C2;
    result = *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562);
    if ((((unsigned __int8)(a1)) & (3)) != 0) {
        result = ExRaiseDatatypeMisalignment(a1, a2, a3, a4);
    }
    a3 = ((unsigned int)(a2)) + (a1);
    if (a3 > result) goto loc_00ACC037;
    v_rdi = 0;
    if (a3 < a1) {
        result = *(unsigned __int8 *)(result);
        v_rdi = v_stack_m40;
    }
    if (a2 >= 28) goto loc_00ACC052;
loc_00ACC048:
    v_stack_m40 = (unsigned int)((unsigned int)(0xC000000DULL));
    goto loc_00ACC088;
loc_00ACC052:
    if ((*(unsigned int *)(a1)) != 28) goto loc_00ACC048;
    *(unsigned int *)(a4) = 40;
    *(unsigned int *)(a4 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4)));
    *(unsigned __int64 *)(a4 + 8) = (unsigned int)(*(unsigned int *)(a1 + 8));
    *(unsigned int *)(a4 + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 12)));
    *(unsigned __int64 *)(a4 + 24) = (unsigned int)(*(unsigned int *)(a1 + 16));
    *(unsigned int *)(a4 + 32) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 20)));
    *(unsigned int *)(a4 + 36) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 24)));
loc_00ACC088:
    goto loc_00ACC0BD;
loc_00ACC0BD:
    goto loc_00ACC15D;
loc_00ACC0C2:
    result = v_stack_p8;
    if ((((unsigned __int8)(a1)) & (7)) != 0) {
        result = ExRaiseDatatypeMisalignment(a1, a2, a3, a4);
    }
    a3 = ((unsigned int)(a2)) + (a1);
    if (a3 > result) goto loc_00ACC0E6;
    v_rdi = (unsigned int)((unsigned int)((unsigned int)(0xC000000DULL)));
    if (a3 < a1) {
        result = *(unsigned __int8 *)(result);
        v_rdi = v_stack_m40;
    }
    if (a2 >= 40) goto loc_00ACC101;
    v_stack_m40 = (unsigned int)((unsigned int)(0xC000000DULL));
    goto loc_00ACC128;
loc_00ACC101:
    *(unsigned __int64 *)(a4) = v_xmm0;
    *(unsigned __int64 *)(a4 + 16) = v_xmm1;
    *(unsigned __int64 *)(a4 + 32) = v_xmm0;
    v_rdi = (unsigned int)((unsigned int)((unsigned int)(0xC000000DULL)));
    if ((*(unsigned int *)(a4)) != 40) { v_rdi = (unsigned int)((unsigned int)(0xC000000DULL)); }
    v_stack_m40 = (unsigned int)(v_rdi);
loc_00ACC128:
    goto loc_00ACC15D;
loc_00ACC15D:
    if (sign_flag) goto loc_00ACC200;
    v_stack_m38 = *(unsigned __int64 *)(a4 + 8);
    *(unsigned __int64 *)(a4 + 8) = 0;
    result = Feature_KernelPnP_ObjectNameUpdates__private_IsEnabledDeviceUsageNoInline(a1, a2, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_00ACC25C;
    if (*(unsigned __int64 *)(a4 + 8) == 0) goto loc_00ACC1EE;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16)) - 2)) > 398) goto loc_00ACC35C;
    v_stack_m50 = 1;
    v_stack_m58 = (unsigned __int8)(v_stack_p8);
    result = PiControlMakeUserModeCallersCopy(a4 + 8, v_stack_m38, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16)))), 1 + 1);
    if (sign_flag) goto loc_00ACC1E2;
    v_stack_m3C = 1;
    a2 = ((unsigned int)(*(unsigned int *)(a4 + 16))) >> (1);
    *(unsigned __int16 *)(*(unsigned __int64 *)(a4 + 8) + a2 * 2 - 2) = 0;
    goto loc_00ACC2E6;
loc_00ACC1E2:
    *(unsigned __int64 *)(a4 + 8) = 0;
    *(unsigned int *)(a4 + 16) = 0;
    goto loc_00ACC2E6;
loc_00ACC1EE:
    if ((unsigned int)(*(unsigned __int64 *)(a4 + 8)) == 0) goto loc_00ACC2E0;
loc_00ACC1F6:
loc_00ACC1F9:
loc_00ACC200:
loc_00ACC205:
    if (!sign_flag) goto loc_00ACC23F;
    result = v_stack_p8;
    if (v_stack_m3C != 0) {
        a2 = *(unsigned __int64 *)(a4 + 8);
        a1 = (unsigned __int8)(v_stack_p8);
        result = PiControlFreeUserModeCallersBuffer(a1, a2, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16)))), 1 + 1);
    }
    if ((unsigned int)((unsigned int)(v_stack_m44)) != 0) {
        a2 = *(unsigned __int64 *)(a4 + 24);
        a1 = v_stack_p8;
        result = PiControlFreeUserModeCallersBuffer(a1, a2, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16)))), 1 + 1);
    }
    result = 0;
    *(unsigned __int64 *)(a4) = v_xmm0;
    *(unsigned __int64 *)(a4 + 16) = v_xmm0;
    *(unsigned __int64 *)(a4 + 32) = 0;
loc_00ACC23F:
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(0xC000000DULL)))));
loc_00ACC25C:
    if (1 == 0) goto loc_00ACC2BD;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 16)))) < 2) goto loc_00ACC2C1;
    v_stack_m28 = 1;
    v_stack_m30 = (unsigned __int8)(v_stack_p30);
    result = PiControlMakeUserModeCallersCopy(a4 + 8, v_stack_m10, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 16)), 1 + 1);
    if (sign_flag) goto loc_00ACC2B3;
    v_stack_m14 = 1;
    a1 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 16))) >> (1);
    *(unsigned __int16 *)(*(unsigned __int64 *)(a4 + 8) + a1 * 2 - 2) = (unsigned __int16)(*(unsigned __int64 *)(v_stack_m28 + 56));
    goto loc_00ACC2E6;
loc_00ACC2B3:
    *(unsigned __int64 *)(a4 + 8) = *(unsigned __int64 *)(v_stack_m28 + 56);
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 16) = (unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 56));
    goto loc_00ACC2E6;
loc_00ACC2BD:
    v_r12 = (*(unsigned __int64 *)(v_stack_m28 + 64) + 16) + (16);
loc_00ACC2C1:
    if (1 != 0) goto loc_00ACC2D5;
    if ((*(unsigned int *)(v_r12)) > ((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 56)))) goto loc_00ACC1F6;
    if (1 == 0) goto loc_00ACC2E0;
loc_00ACC2D5:
    if ((*(unsigned int *)(v_r12)) < 2) goto loc_00ACC1F6;
loc_00ACC2E0:
loc_00ACC2E6:
    v_stack_m10 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 24);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 24) = *(unsigned __int64 *)(v_stack_m28 + 56);
    result = Feature_KernelPnP_ObjectNameUpdates__private_IsEnabledDeviceUsageNoInline(a1, v_stack_m10, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 16)), 1 + 1);
    if ((unsigned int)(result) == 0) goto loc_00ACC364;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 24) == 0) goto loc_00ACC34D;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 32)) - 2)) > 398) goto loc_00ACC35C;
    v_stack_m28 = 1;
    v_stack_m30 = (unsigned __int8)(v_stack_p30);
    result = PiControlMakeUserModeCallersCopy(*(unsigned __int64 *)(v_stack_m28 + 64) + 24, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 24), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 32)))), 2);
    if (sign_flag) goto loc_00ACC341;
    goto loc_00ACC3A4;
loc_00ACC341:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 24) = *(unsigned __int64 *)(v_stack_m28 + 56);
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 32) = (unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 56));
    goto loc_00ACC1F9;
loc_00ACC34D:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 32))) == 0) goto loc_00ACC200;
loc_00ACC35C:
    goto loc_00ACC200;
loc_00ACC364:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 24) == 0) goto loc_00ACC3CC;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 32)))) < 2) goto loc_00ACC3D5;
    v_stack_m28 = 1;
    v_stack_m30 = (unsigned __int8)(v_stack_p30);
    result = PiControlMakeUserModeCallersCopy(*(unsigned __int64 *)(v_stack_m28 + 64) + 24, v_stack_m10, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 32)), 2);
    if (sign_flag) goto loc_00ACC3BF;
loc_00ACC3A4:
    a1 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 32))) >> (1);
    *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 24) + a1 * 2 - 2) = (unsigned __int16)(*(unsigned __int64 *)(v_stack_m28 + 56));
    goto loc_00ACC205;
loc_00ACC3BF:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 24) = *(unsigned __int64 *)(v_stack_m28 + 56);
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 32) = (unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 56));
    goto loc_00ACC1F9;
loc_00ACC3CC:
    v_r12 = (v_stack_m8) + (32);
loc_00ACC3D5:
    if (v_stack_m10 != 0) goto loc_00ACC3F2;
    if ((*(unsigned int *)(v_r12)) > ((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 56)))) goto loc_00ACC1F6;
    if (v_stack_m10 == 0) goto loc_00ACC1F9;
loc_00ACC3F2:
    if ((*(unsigned int *)(v_r12)) >= 2) goto loc_00ACC1F9;
    goto loc_00ACC1F6;
loc_00ACC402:
    goto loc_00ACC205;
}
```

## 5. (Beta) C Style

```c
int64_t PiCMCaptureCreateDeviceInputData(int64_t Arg1, int32_t Arg2, int32_t Arg3, void *Arg4)
{
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r12;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint32_t v_stack_m14;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;
    uint32_t v_stack_m3C;
    uint32_t v_stack_m40;
    uint32_t v_stack_m44;
    uint8_t v_stack_m48;
    uint32_t v_stack_m50;
    uint8_t v_stack_m58;
    uint64_t v_stack_m8;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint8_t v_stack_p30;
    uint8_t v_stack_p8;

    v_stack_p10 = local_rbx;
    v_stack_p18 = local_rsi;
    v_stack_p20 = Arg4;
    local_rsp = (local_rsp) - (80);
    v_stack_m30 = Arg4;
    local_rbx = 0;
    v_stack_m3C = 0;
    v_stack_m44 = 0;
    v_stack_p8 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    v_stack_m48 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    v_stack_m40 = 0;
    if (Arg1 == 0) goto loc_00ACC402;
    if (Arg2 == 0) goto loc_00ACC402;
    if (Arg3 == 0) goto loc_00ACC0C2;
    result = *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232);
    if ((((uint8_t)(Arg1)) & (3)) != 0) {
        result = ExRaiseDatatypeMisalignment(Arg1, Arg2, Arg3, Arg4);
    }
    Arg3 = ((uint32_t)(Arg2)) + (Arg1);
    if (Arg3 > result) goto loc_00ACC037;
    local_rdi = 0;
    if (Arg3 < Arg1) {
        result = *(uint8_t *)(result);
        local_rdi = v_stack_m40;
    }
    if (Arg2 >= 28) goto loc_00ACC052;
loc_00ACC048:
    v_stack_m40 = (uint32_t)((uint32_t)(0xC000000DULL));
    goto loc_00ACC088;
loc_00ACC052:
    if ((*(uint32_t *)(Arg1)) != 28) goto loc_00ACC048;
    *(uint32_t *)(arg4) = 40;
    *(uint32_t *)(arg4 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x4)));
    *(uint64_t *)(arg4 + 0x8) = (uint32_t)(*(uint32_t *)(Arg1 + 0x8));
    *(uint32_t *)(arg4 + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + 0xC)));
    *(uint64_t *)(arg4 + 0x18) = (uint32_t)(*(uint32_t *)(Arg1 + 0x10));
    *(uint32_t *)(arg4 + 0x20) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x14)));
    *(uint32_t *)(arg4 + 0x24) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x18)));
loc_00ACC088:
    goto loc_00ACC0BD;
loc_00ACC0BD:
    goto loc_00ACC15D;
loc_00ACC0C2:
    result = v_stack_p8;
    if ((((uint8_t)(Arg1)) & (7)) != 0) {
        result = ExRaiseDatatypeMisalignment(Arg1, Arg2, Arg3, Arg4);
    }
    Arg3 = ((uint32_t)(Arg2)) + (Arg1);
    if (Arg3 > result) goto loc_00ACC0E6;
    local_rdi = (uint32_t)((uint32_t)((uint32_t)(0xC000000DULL)));
    if (Arg3 < Arg1) {
        result = *(uint8_t *)(result);
        local_rdi = v_stack_m40;
    }
    if (Arg2 >= 40) goto loc_00ACC101;
    v_stack_m40 = (uint32_t)((uint32_t)(0xC000000DULL));
    goto loc_00ACC128;
loc_00ACC101:
    *(uint64_t *)(arg4) = v_xmm0;
    *(uint64_t *)(arg4 + 0x10) = v_xmm1;
    *(uint64_t *)(arg4 + 0x20) = v_xmm0;
    local_rdi = (uint32_t)((uint32_t)((uint32_t)(0xC000000DULL)));
    if ((*(uint32_t *)(arg4)) != 40) { local_rdi = (uint32_t)((uint32_t)(0xC000000DULL)); }
    v_stack_m40 = (uint32_t)(local_rdi);
loc_00ACC128:
    goto loc_00ACC15D;
loc_00ACC15D:
    if (sign_flag) goto loc_00ACC200;
    v_stack_m38 = *(uint64_t *)(arg4 + 0x8);
    *(uint64_t *)(arg4 + 0x8) = 0;
    result = Feature_KernelPnP_ObjectNameUpdates__private_IsEnabledDeviceUsageNoInline(Arg1, Arg2, Arg3, Arg4);
    if ((uint32_t)(result) == 0) goto loc_00ACC25C;
    if (*(uint64_t *)(arg4 + 0x8) == 0) goto loc_00ACC1EE;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x10)) - 2)) > 398) goto loc_00ACC35C;
    v_stack_m50 = 1;
    v_stack_m58 = (uint8_t)(v_stack_p8);
    result = PiControlMakeUserModeCallersCopy(Arg4 + 8, v_stack_m38, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x10)))), 1 + 1);
    if (sign_flag) goto loc_00ACC1E2;
    v_stack_m3C = 1;
    Arg2 = ((uint32_t)(*(uint32_t *)(arg4 + 0x10))) >> (1);
    *(uint16_t *)(*(uint64_t *)(arg4 + 0x8) + Arg2 * 2 - 0x2) = 0;
    goto loc_00ACC2E6;
loc_00ACC1E2:
    *(uint64_t *)(arg4 + 0x8) = 0;
    *(uint32_t *)(arg4 + 0x10) = 0;
    goto loc_00ACC2E6;
loc_00ACC1EE:
    if ((uint32_t)(*(uint64_t *)(arg4 + 0x8)) == 0) goto loc_00ACC2E0;
loc_00ACC1F6:
loc_00ACC1F9:
loc_00ACC200:
loc_00ACC205:
    if (!sign_flag) goto loc_00ACC23F;
    result = v_stack_p8;
    if (v_stack_m3C != 0) {
        Arg2 = *(uint64_t *)(arg4 + 0x8);
        Arg1 = (uint8_t)(v_stack_p8);
        result = PiControlFreeUserModeCallersBuffer(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x10)))), 1 + 1);
    }
    if ((uint32_t)((uint32_t)(v_stack_m44)) != 0) {
        Arg2 = *(uint64_t *)(arg4 + 0x18);
        Arg1 = v_stack_p8;
        result = PiControlFreeUserModeCallersBuffer(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x10)))), 1 + 1);
    }
    result = 0;
    *(uint64_t *)(arg4) = v_xmm0;
    *(uint64_t *)(arg4 + 0x10) = v_xmm0;
    *(uint64_t *)(arg4 + 0x20) = 0;
loc_00ACC23F:
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(0xC000000DULL)))));
loc_00ACC25C:
    if (1 == 0) goto loc_00ACC2BD;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x10)))) < 2) goto loc_00ACC2C1;
    v_stack_m28 = 1;
    v_stack_m30 = (uint8_t)(v_stack_p30);
    result = PiControlMakeUserModeCallersCopy(Arg4 + 8, v_stack_m10, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x10)), 1 + 1);
    if (sign_flag) goto loc_00ACC2B3;
    v_stack_m14 = 1;
    Arg1 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x10))) >> (1);
    *(uint16_t *)(*(uint64_t *)(arg4 + 0x8) + Arg1 * 2 - 0x2) = (uint16_t)(*(uint64_t *)(v_stack_m28 + 0x38));
    goto loc_00ACC2E6;
loc_00ACC2B3:
    *(uint64_t *)(arg4 + 0x8) = *(uint64_t *)(v_stack_m28 + 0x38);
    *(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x10) = (uint32_t)(*(uint64_t *)(v_stack_m28 + 0x38));
    goto loc_00ACC2E6;
loc_00ACC2BD:
    local_r12 = (*(uint64_t *)(v_stack_m28 + 0x40) + 16) + (16);
loc_00ACC2C1:
    if (1 != 0) goto loc_00ACC2D5;
    if ((*(uint32_t *)(local_r12)) > ((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x38)))) goto loc_00ACC1F6;
    if (1 == 0) goto loc_00ACC2E0;
loc_00ACC2D5:
    if ((*(uint32_t *)(local_r12)) < 2) goto loc_00ACC1F6;
loc_00ACC2E0:
loc_00ACC2E6:
    v_stack_m10 = *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x18);
    *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x18) = *(uint64_t *)(v_stack_m28 + 0x38);
    result = Feature_KernelPnP_ObjectNameUpdates__private_IsEnabledDeviceUsageNoInline(Arg1, v_stack_m10, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x10)), 1 + 1);
    if ((uint32_t)(result) == 0) goto loc_00ACC364;
    if (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x18) == 0) goto loc_00ACC34D;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x20)) - 2)) > 398) goto loc_00ACC35C;
    v_stack_m28 = 1;
    v_stack_m30 = (uint8_t)(v_stack_p30);
    result = PiControlMakeUserModeCallersCopy(*(uint64_t *)(v_stack_m28 + 0x40) + 24, *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x18), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x20)))), 2);
    if (sign_flag) goto loc_00ACC341;
    goto loc_00ACC3A4;
loc_00ACC341:
    *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x18) = *(uint64_t *)(v_stack_m28 + 0x38);
    *(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x20) = (uint32_t)(*(uint64_t *)(v_stack_m28 + 0x38));
    goto loc_00ACC1F9;
loc_00ACC34D:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x20))) == 0) goto loc_00ACC200;
loc_00ACC35C:
    goto loc_00ACC200;
loc_00ACC364:
    if (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x18) == 0) goto loc_00ACC3CC;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x20)))) < 2) goto loc_00ACC3D5;
    v_stack_m28 = 1;
    v_stack_m30 = (uint8_t)(v_stack_p30);
    result = PiControlMakeUserModeCallersCopy(*(uint64_t *)(v_stack_m28 + 0x40) + 24, v_stack_m10, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x20)), 2);
    if (sign_flag) goto loc_00ACC3BF;
loc_00ACC3A4:
    Arg1 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x20))) >> (1);
    *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x18) + Arg1 * 2 - 0x2) = (uint16_t)(*(uint64_t *)(v_stack_m28 + 0x38));
    goto loc_00ACC205;
loc_00ACC3BF:
    *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x18) = *(uint64_t *)(v_stack_m28 + 0x38);
    *(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x20) = (uint32_t)(*(uint64_t *)(v_stack_m28 + 0x38));
    goto loc_00ACC1F9;
loc_00ACC3CC:
    local_r12 = (v_stack_m8) + (32);
loc_00ACC3D5:
    if (v_stack_m10 != 0) goto loc_00ACC3F2;
    if ((*(uint32_t *)(local_r12)) > ((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x38)))) goto loc_00ACC1F6;
    if (v_stack_m10 == 0) goto loc_00ACC1F9;
loc_00ACC3F2:
    if ((*(uint32_t *)(local_r12)) >= 2) goto loc_00ACC1F9;
    goto loc_00ACC1F6;
loc_00ACC402:
    goto loc_00ACC205;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg4` | `+ 0x0` | `32` | `R` |
| `Arg4` | `+ 0x0` | `32` | `W` |
| `Arg4` | `+ 0x0` | `64` | `R` |
| `Arg4` | `+ 0x0` | `64` | `W` |
| `Arg4` | `+ 0x0` | `128` | `R` |
| `Arg4` | `+ 0x8` | `64` | `R` |
| `Arg4` | `+ 0x10` | `32` | `R` |
| `Arg4` | `+ 0x10` | `32` | `W` |
| `Arg4` | `+ 0x10` | `64` | `R` |
| `Arg4` | `+ 0x10` | `128` | `R` |
| `Arg4` | `+ 0x18` | `64` | `R` |
| `Arg4` | `+ 0x20` | `32` | `R` |
| `Arg4` | `+ 0x20` | `32` | `W` |
| `Arg4` | `+ 0x20` | `64` | `R` |
| `Arg4` | `+ 0x20` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00ACBFA8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
