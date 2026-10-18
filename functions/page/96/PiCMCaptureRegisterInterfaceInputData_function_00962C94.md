# PiCMCaptureRegisterInterfaceInputData

- RVA: `0x00962C94`–`0x00963112` (길이 `1,150` bytes)
- VA: `0x0000000140962C94`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000934E0`
- 디코드: `298`개 명령, `1,150/1,150` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **10**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00962D04` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x00962DBD` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x00962E75` → [Feature_KernelPnP_ObjectNameUpdates__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_KernelPnP_ObjectNameUpdates__private_IsEnabledDeviceUsageNoInline_function_004F2E10.md) (function, `0x004F2E10`)
- `0x00962EBD` → [PiControlMakeUserModeCallersCopy](../8E/PiControlMakeUserModeCallersCopy_function_008E4630.md) (function, `0x008E4630`)
- `0x00962F14` → [PiControlFreeUserModeCallersBuffer](../../text/44/PiControlFreeUserModeCallersBuffer_function_00448990.md) (function, `0x00448990`)
- `0x00962F29` → [PiControlFreeUserModeCallersBuffer](../../text/44/PiControlFreeUserModeCallersBuffer_function_00448990.md) (function, `0x00448990`)
- `0x00962F94` → [PiControlMakeUserModeCallersCopy](../8E/PiControlMakeUserModeCallersCopy_function_008E4630.md) (function, `0x008E4630`)
- `0x00962FFA` → [Feature_KernelPnP_ObjectNameUpdates__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_KernelPnP_ObjectNameUpdates__private_IsEnabledDeviceUsageNoInline_function_004F2E10.md) (function, `0x004F2E10`)
- `0x00963034` → [PiControlMakeUserModeCallersCopy](../8E/PiControlMakeUserModeCallersCopy_function_008E4630.md) (function, `0x008E4630`)
- `0x00963098` → [PiControlMakeUserModeCallersCopy](../8E/PiControlMakeUserModeCallersCopy_function_008E4630.md) (function, `0x008E4630`)

### Direct callers
- [PiCMRegisterDeviceInterface](PiCMRegisterDeviceInterface_function_00962A94.md) at `0x00962AF6`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **4**
  - `0x00962E75` → [Feature_KernelPnP_ObjectNameUpdates__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_KernelPnP_ObjectNameUpdates__private_IsEnabledDeviceUsageNoInline_function_004F2E10.md) (`PAGE` → `.text`)
  - `0x00962F14` → [PiControlFreeUserModeCallersBuffer](../../text/44/PiControlFreeUserModeCallersBuffer_function_00448990.md) (`PAGE` → `.text`)
  - `0x00962F29` → [PiControlFreeUserModeCallersBuffer](../../text/44/PiControlFreeUserModeCallersBuffer_function_00448990.md) (`PAGE` → `.text`)
  - `0x00962FFA` → [Feature_KernelPnP_ObjectNameUpdates__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_KernelPnP_ObjectNameUpdates__private_IsEnabledDeviceUsageNoInline_function_004F2E10.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00962C94  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
00962C99  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
00962C9E  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
00962CA3  57                              push rdi
00962CA4  41 54                           push r12
00962CA6  41 55                           push r13
00962CA8  41 56                           push r14
00962CAA  41 57                           push r15
00962CAC  48 83 EC 50                     sub rsp, 0x50
00962CB0  49 8B F1                        mov rsi, r9
00962CB3  4D 8B E1                        mov r12, r9
00962CB6  4C 89 4C 24 48                  mov qword ptr [rsp + 0x48], r9
00962CBB  33 DB                           xor ebx, ebx
00962CBD  89 5C 24 3C                     mov dword ptr [rsp + 0x3c], ebx
00962CC1  89 5C 24 34                     mov dword ptr [rsp + 0x34], ebx
00962CC5  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00962CCE  8A 80 32 02 00 00               mov al, byte ptr [rax + 0x232]
00962CD4  88 84 24 80 00 00 00            mov byte ptr [rsp + 0x80], al
00962CDB  88 44 24 30                     mov byte ptr [rsp + 0x30], al
00962CDF  8B FB                           mov edi, ebx
00962CE1  89 5C 24 38                     mov dword ptr [rsp + 0x38], ebx
00962CE5  48 85 C9                        test rcx, rcx
00962CE8  0F 84 17 04 00 00               je 0x140963105
00962CEE  85 D2                           test edx, edx
00962CF0  0F 84 0F 04 00 00               je 0x140963105
00962CF6  45 85 C0                        test r8d, r8d
00962CF9  0F 84 B9 00 00 00               je 0x140962db8
00962CFF  F6 C1 03                        test cl, 3
00962D02  74 05                           je 0x140962d09
00962D04  E8 C7 72 F3 FF                  call 0x140899fd0
00962D09  44 8B C2                        mov r8d, edx
00962D0C  4C 03 C1                        add r8, rcx
00962D0F  48 B8 00 00 FF FF FF 7F 00 00   movabs rax, 0x7fffffff0000
00962D19  4C 3B C0                        cmp r8, rax
00962D1C  77 05                           ja 0x140962d23
00962D1E  4C 3B C1                        cmp r8, rcx
00962D21  73 06                           jae 0x140962d29
00962D23  8A 00                           mov al, byte ptr [rax]
00962D25  8B 7C 24 38                     mov edi, dword ptr [rsp + 0x38]
00962D29  41 BE 0D 00 00 C0               mov r14d, 0xc000000d
00962D2F  83 FA 2C                        cmp edx, 0x2c
00962D32  73 0A                           jae 0x140962d3e
00962D34  41 8B FE                        mov edi, r14d
00962D37  44 89 74 24 38                  mov dword ptr [rsp + 0x38], r14d
00962D3C  EB 40                           jmp 0x140962d7e
00962D3E  83 39 2C                        cmp dword ptr [rcx], 0x2c
00962D41  75 F1                           jne 0x140962d34
00962D43  41 C7 01 38 00 00 00            mov dword ptr [r9], 0x38
00962D4A  8B 41 04                        mov eax, dword ptr [rcx + 4]
00962D4D  41 89 41 04                     mov dword ptr [r9 + 4], eax
00962D51  0F 10 41 08                     movups xmm0, xmmword ptr [rcx + 8]
00962D55  F3 41 0F 7F 41 08               movdqu xmmword ptr [r9 + 8], xmm0
00962D5B  8B 41 18                        mov eax, dword ptr [rcx + 0x18]
00962D5E  49 89 41 18                     mov qword ptr [r9 + 0x18], rax
00962D62  8B 41 1C                        mov eax, dword ptr [rcx + 0x1c]
00962D65  41 89 41 20                     mov dword ptr [r9 + 0x20], eax
00962D69  8B 41 20                        mov eax, dword ptr [rcx + 0x20]
00962D6C  49 89 41 28                     mov qword ptr [r9 + 0x28], rax
00962D70  8B 41 24                        mov eax, dword ptr [rcx + 0x24]
00962D73  41 89 41 30                     mov dword ptr [r9 + 0x30], eax
00962D77  8B 41 28                        mov eax, dword ptr [rcx + 0x28]
00962D7A  41 89 41 34                     mov dword ptr [r9 + 0x34], eax
00962D7E  8A 84 24 80 00 00 00            mov al, byte ptr [rsp + 0x80]
00962D85  EB 2C                           jmp 0x140962db3
00962D87  8B F8                           mov edi, eax
00962D89  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
00962D8D  33 DB                           xor ebx, ebx
00962D8F  41 BE 0D 00 00 C0               mov r14d, 0xc000000d
00962D95  48 8B B4 24 98 00 00 00         mov rsi, qword ptr [rsp + 0x98]
00962D9D  8B C3                           mov eax, ebx
00962D9F  89 5C 24 3C                     mov dword ptr [rsp + 0x3c], ebx
00962DA3  8A 44 24 30                     mov al, byte ptr [rsp + 0x30]
00962DA7  88 84 24 80 00 00 00            mov byte ptr [rsp + 0x80], al
00962DAE  4C 8B 64 24 48                  mov r12, qword ptr [rsp + 0x48]
00962DB3  E9 A4 00 00 00                  jmp 0x140962e5c
00962DB8  F6 C1 07                        test cl, 7
00962DBB  74 05                           je 0x140962dc2
00962DBD  E8 0E 72 F3 FF                  call 0x140899fd0
00962DC2  44 8B C2                        mov r8d, edx
00962DC5  4C 03 C1                        add r8, rcx
00962DC8  48 B8 00 00 FF FF FF 7F 00 00   movabs rax, 0x7fffffff0000
00962DD2  4C 3B C0                        cmp r8, rax
00962DD5  77 05                           ja 0x140962ddc
00962DD7  4C 3B C1                        cmp r8, rcx
00962DDA  73 06                           jae 0x140962de2
00962DDC  8A 00                           mov al, byte ptr [rax]
00962DDE  8B 7C 24 38                     mov edi, dword ptr [rsp + 0x38]
00962DE2  41 BE 0D 00 00 C0               mov r14d, 0xc000000d
00962DE8  83 FA 38                        cmp edx, 0x38
00962DEB  73 0A                           jae 0x140962df7
00962DED  41 8B FE                        mov edi, r14d
00962DF0  44 89 74 24 38                  mov dword ptr [rsp + 0x38], r14d
00962DF5  EB 30                           jmp 0x140962e27
00962DF7  0F 10 01                        movups xmm0, xmmword ptr [rcx]
00962DFA  41 0F 11 01                     movups xmmword ptr [r9], xmm0
00962DFE  0F 10 49 10                     movups xmm1, xmmword ptr [rcx + 0x10]
00962E02  41 0F 11 49 10                  movups xmmword ptr [r9 + 0x10], xmm1
00962E07  0F 10 41 20                     movups xmm0, xmmword ptr [rcx + 0x20]
00962E0B  41 0F 11 41 20                  movups xmmword ptr [r9 + 0x20], xmm0
00962E10  F2 0F 10 49 30                  movsd xmm1, qword ptr [rcx + 0x30]
00962E15  F2 41 0F 11 49 30               movsd qword ptr [r9 + 0x30], xmm1
00962E1B  41 83 39 38                     cmp dword ptr [r9], 0x38
00962E1F  41 0F 45 FE                     cmovne edi, r14d
00962E23  89 7C 24 38                     mov dword ptr [rsp + 0x38], edi
00962E27  8A 84 24 80 00 00 00            mov al, byte ptr [rsp + 0x80]
00962E2E  EB 2C                           jmp 0x140962e5c
00962E30  8B F8                           mov edi, eax
00962E32  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
00962E36  33 DB                           xor ebx, ebx
00962E38  41 BE 0D 00 00 C0               mov r14d, 0xc000000d
00962E3E  48 8B B4 24 98 00 00 00         mov rsi, qword ptr [rsp + 0x98]
00962E46  8B C3                           mov eax, ebx
00962E48  89 5C 24 3C                     mov dword ptr [rsp + 0x3c], ebx
00962E4C  8A 44 24 30                     mov al, byte ptr [rsp + 0x30]
00962E50  88 84 24 80 00 00 00            mov byte ptr [rsp + 0x80], al
00962E57  4C 8B 64 24 48                  mov r12, qword ptr [rsp + 0x48]
00962E5C  85 FF                           test edi, edi
00962E5E  0F 88 9B 00 00 00               js 0x140962eff
00962E64  4C 8D 6E 18                     lea r13, [rsi + 0x18]
00962E68  4D 8B 7D 00                     mov r15, qword ptr [r13]
00962E6C  4C 89 7C 24 40                  mov qword ptr [rsp + 0x40], r15
00962E71  49 89 5D 00                     mov qword ptr [r13], rbx
00962E75  E8 96 FF B8 FF                  call 0x1404f2e10
00962E7A  85 C0                           test eax, eax
00962E7C  0F 84 DD 00 00 00               je 0x140962f5f
00962E82  8B 4E 20                        mov ecx, dword ptr [rsi + 0x20]
00962E85  4D 85 FF                        test r15, r15
00962E88  74 63                           je 0x140962eed
00962E8A  8D 41 FE                        lea eax, [rcx - 2]
00962E8D  3D 8E 01 00 00                  cmp eax, 0x18e
00962E92  8A 84 24 80 00 00 00            mov al, byte ptr [rsp + 0x80]
00962E99  0F 87 C0 01 00 00               ja 0x14096305f
00962E9F  41 BF 01 00 00 00               mov r15d, 1
00962EA5  44 89 7C 24 28                  mov dword ptr [rsp + 0x28], r15d
00962EAA  88 44 24 20                     mov byte ptr [rsp + 0x20], al
00962EAE  45 8D 4F 01                     lea r9d, [r15 + 1]
00962EB2  44 8B C1                        mov r8d, ecx
00962EB5  48 8B 54 24 40                  mov rdx, qword ptr [rsp + 0x40]
00962EBA  49 8B CD                        mov rcx, r13
00962EBD  E8 6E 17 F8 FF                  call 0x1408e4630
00962EC2  8B F8                           mov edi, eax
00962EC4  85 C0                           test eax, eax
00962EC6  78 19                           js 0x140962ee1
00962EC8  44 89 7C 24 3C                  mov dword ptr [rsp + 0x3c], r15d
00962ECD  8B 56 20                        mov edx, dword ptr [rsi + 0x20]
00962ED0  48 D1 EA                        shr rdx, 1
00962ED3  49 8B 4D 00                     mov rcx, qword ptr [r13]
00962ED7  66 89 5C 51 FE                  mov word ptr [rcx + rdx*2 - 2], bx
00962EDC  E9 08 01 00 00                  jmp 0x140962fe9
00962EE1  49 89 5D 00                     mov qword ptr [r13], rbx
00962EE5  89 5E 20                        mov dword ptr [rsi + 0x20], ebx
00962EE8  E9 FC 00 00 00                  jmp 0x140962fe9
00962EED  85 C9                           test ecx, ecx
00962EEF  0F 84 EE 00 00 00               je 0x140962fe3
00962EF5  41 8B FE                        mov edi, r14d
00962EF8  8A 84 24 80 00 00 00            mov al, byte ptr [rsp + 0x80]
00962EFF  44 8B 74 24 34                  mov r14d, dword ptr [rsp + 0x34]
00962F04  85 FF                           test edi, edi
00962F06  79 3A                           jns 0x140962f42
00962F08  39 5C 24 3C                     cmp dword ptr [rsp + 0x3c], ebx
00962F0C  74 0B                           je 0x140962f19
00962F0E  48 8B 56 18                     mov rdx, qword ptr [rsi + 0x18]
00962F12  8A C8                           mov cl, al
00962F14  E8 77 5A AE FF                  call 0x140448990
00962F19  45 85 F6                        test r14d, r14d
00962F1C  74 10                           je 0x140962f2e
00962F1E  48 8B 56 28                     mov rdx, qword ptr [rsi + 0x28]
00962F22  8A 8C 24 80 00 00 00            mov cl, byte ptr [rsp + 0x80]
00962F29  E8 62 5A AE FF                  call 0x140448990
00962F2E  0F 57 C0                        xorps xmm0, xmm0
00962F31  33 C0                           xor eax, eax
00962F33  0F 11 06                        movups xmmword ptr [rsi], xmm0
00962F36  0F 11 46 10                     movups xmmword ptr [rsi + 0x10], xmm0
00962F3A  0F 11 46 20                     movups xmmword ptr [rsi + 0x20], xmm0
00962F3E  48 89 46 30                     mov qword ptr [rsi + 0x30], rax
00962F42  8B C7                           mov eax, edi
00962F44  4C 8D 5C 24 50                  lea r11, [rsp + 0x50]
00962F49  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
00962F4D  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
00962F51  49 8B E3                        mov rsp, r11
00962F54  41 5F                           pop r15
00962F56  41 5E                           pop r14
00962F58  41 5D                           pop r13
00962F5A  41 5C                           pop r12
00962F5C  5F                              pop rdi
00962F5D  C3                              ret
00962F5E  CC                              int3
00962F5F  4D 85 FF                        test r15, r15
00962F62  74 5C                           je 0x140962fc0
00962F64  4C 8D 66 20                     lea r12, [rsi + 0x20]
00962F68  45 8B 04 24                     mov r8d, dword ptr [r12]
00962F6C  41 83 F8 02                     cmp r8d, 2
00962F70  72 52                           jb 0x140962fc4
00962F72  41 BF 01 00 00 00               mov r15d, 1
00962F78  44 89 7C 24 28                  mov dword ptr [rsp + 0x28], r15d
00962F7D  8A 84 24 80 00 00 00            mov al, byte ptr [rsp + 0x80]
00962F84  88 44 24 20                     mov byte ptr [rsp + 0x20], al
00962F88  45 8D 4F 01                     lea r9d, [r15 + 1]
00962F8C  48 8B 54 24 40                  mov rdx, qword ptr [rsp + 0x40]
00962F91  49 8B CD                        mov rcx, r13
00962F94  E8 97 16 F8 FF                  call 0x1408e4630
00962F99  8B F8                           mov edi, eax
00962F9B  85 C0                           test eax, eax
00962F9D  78 17                           js 0x140962fb6
00962F9F  44 89 7C 24 3C                  mov dword ptr [rsp + 0x3c], r15d
00962FA4  41 8B 0C 24                     mov ecx, dword ptr [r12]
00962FA8  48 D1 E9                        shr rcx, 1
00962FAB  49 8B 45 00                     mov rax, qword ptr [r13]
00962FAF  66 89 5C 48 FE                  mov word ptr [rax + rcx*2 - 2], bx
00962FB4  EB 33                           jmp 0x140962fe9
00962FB6  49 89 5D 00                     mov qword ptr [r13], rbx
00962FBA  41 89 1C 24                     mov dword ptr [r12], ebx
00962FBE  EB 29                           jmp 0x140962fe9
00962FC0  49 83 C4 20                     add r12, 0x20
00962FC4  4D 85 FF                        test r15, r15
00962FC7  75 0F                           jne 0x140962fd8
00962FC9  41 39 1C 24                     cmp dword ptr [r12], ebx
00962FCD  0F 87 22 FF FF FF               ja 0x140962ef5
00962FD3  4D 85 FF                        test r15, r15
00962FD6  74 0B                           je 0x140962fe3
00962FD8  41 83 3C 24 02                  cmp dword ptr [r12], 2
00962FDD  0F 82 12 FF FF FF               jb 0x140962ef5
00962FE3  41 BF 01 00 00 00               mov r15d, 1
00962FE9  4C 8D 66 28                     lea r12, [rsi + 0x28]
00962FED  4D 8B 2C 24                     mov r13, qword ptr [r12]
00962FF1  4C 89 6C 24 40                  mov qword ptr [rsp + 0x40], r13
00962FF6  49 89 1C 24                     mov qword ptr [r12], rbx
00962FFA  E8 11 FE B8 FF                  call 0x1404f2e10
00962FFF  85 C0                           test eax, eax
00963001  74 64                           je 0x140963067
00963003  8B 4E 30                        mov ecx, dword ptr [rsi + 0x30]
00963006  4D 85 ED                        test r13, r13
00963009  74 45                           je 0x140963050
0096300B  8D 41 FE                        lea eax, [rcx - 2]
0096300E  3D FD FF 00 00                  cmp eax, 0xfffd
00963013  8A 84 24 80 00 00 00            mov al, byte ptr [rsp + 0x80]
0096301A  77 43                           ja 0x14096305f
0096301C  44 89 7C 24 28                  mov dword ptr [rsp + 0x28], r15d
00963021  88 44 24 20                     mov byte ptr [rsp + 0x20], al
00963025  41 B9 02 00 00 00               mov r9d, 2
0096302B  44 8B C1                        mov r8d, ecx
0096302E  49 8B D5                        mov rdx, r13
00963031  49 8B CC                        mov rcx, r12
00963034  E8 F7 15 F8 FF                  call 0x1408e4630
00963039  8B F8                           mov edi, eax
0096303B  85 C0                           test eax, eax
0096303D  78 05                           js 0x140963044
0096303F  8B 4E 30                        mov ecx, dword ptr [rsi + 0x30]
00963042  EB 63                           jmp 0x1409630a7
00963044  49 89 1C 24                     mov qword ptr [r12], rbx
00963048  89 5E 30                        mov dword ptr [rsi + 0x30], ebx
0096304B  E9 A8 FE FF FF                  jmp 0x140962ef8
00963050  8A 84 24 80 00 00 00            mov al, byte ptr [rsp + 0x80]
00963057  85 C9                           test ecx, ecx
00963059  0F 84 A0 FE FF FF               je 0x140962eff
0096305F  41 8B FE                        mov edi, r14d
00963062  E9 98 FE FF FF                  jmp 0x140962eff
00963067  4D 85 ED                        test r13, r13
0096306A  74 63                           je 0x1409630cf
0096306C  4C 8D 6E 30                     lea r13, [rsi + 0x30]
00963070  45 8B 45 00                     mov r8d, dword ptr [r13]
00963074  41 83 F8 02                     cmp r8d, 2
00963078  72 5E                           jb 0x1409630d8
0096307A  44 89 7C 24 28                  mov dword ptr [rsp + 0x28], r15d
0096307F  8A 84 24 80 00 00 00            mov al, byte ptr [rsp + 0x80]
00963086  88 44 24 20                     mov byte ptr [rsp + 0x20], al
0096308A  41 B9 02 00 00 00               mov r9d, 2
00963090  48 8B 54 24 40                  mov rdx, qword ptr [rsp + 0x40]
00963095  49 8B CC                        mov rcx, r12
00963098  E8 93 15 F8 FF                  call 0x1408e4630
0096309D  8B F8                           mov edi, eax
0096309F  85 C0                           test eax, eax
009630A1  78 1F                           js 0x1409630c2
009630A3  41 8B 4D 00                     mov ecx, dword ptr [r13]
009630A7  45 8B F7                        mov r14d, r15d
009630AA  48 D1 E9                        shr rcx, 1
009630AD  49 8B 04 24                     mov rax, qword ptr [r12]
009630B1  66 89 5C 48 FE                  mov word ptr [rax + rcx*2 - 2], bx
009630B6  8A 84 24 80 00 00 00            mov al, byte ptr [rsp + 0x80]
009630BD  E9 42 FE FF FF                  jmp 0x140962f04
009630C2  49 89 1C 24                     mov qword ptr [r12], rbx
009630C6  41 89 5D 00                     mov dword ptr [r13], ebx
009630CA  E9 29 FE FF FF                  jmp 0x140962ef8
009630CF  4C 8B 6C 24 48                  mov r13, qword ptr [rsp + 0x48]
009630D4  49 83 C5 30                     add r13, 0x30
009630D8  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
009630DD  48 85 C0                        test rax, rax
009630E0  75 13                           jne 0x1409630f5
009630E2  41 39 5D 00                     cmp dword ptr [r13], ebx
009630E6  0F 87 09 FE FF FF               ja 0x140962ef5
009630EC  48 85 C0                        test rax, rax
009630EF  0F 84 03 FE FF FF               je 0x140962ef8
009630F5  41 83 7D 00 02                  cmp dword ptr [r13], 2
009630FA  0F 83 F8 FD FF FF               jae 0x140962ef8
00963100  E9 F0 FD FF FF                  jmp 0x140962ef5
00963105  BF 0D 00 00 C0                  mov edi, 0xc000000d
0096310A  44 8B F3                        mov r14d, ebx
0096310D  E9 F2 FD FF FF                  jmp 0x140962f04
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PiCMCaptureRegisterInterfaceInputData(__int64 a1, int a2, int a3, __int64 a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
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
    if (a1 == 0) goto loc_00963105;
    if (a2 == 0) goto loc_00963105;
    if (a3 == 0) goto loc_00962DB8;
    result = *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562);
    if ((((unsigned __int8)(a1)) & (3)) != 0) {
        result = ExRaiseDatatypeMisalignment(a1, a2, a3, a4);
    }
    a3 = ((unsigned int)(a2)) + (a1);
    if (a3 > result) goto loc_00962D23;
    v_rdi = 0;
    if (a3 < a1) {
        result = *(unsigned __int8 *)(result);
        v_rdi = v_stack_m40;
    }
    if (a2 >= 44) goto loc_00962D3E;
loc_00962D34:
    v_stack_m40 = (unsigned int)((unsigned int)(0xC000000DULL));
    goto loc_00962D7E;
loc_00962D3E:
    if ((*(unsigned int *)(a1)) != 44) goto loc_00962D34;
    *(unsigned int *)(a4) = 56;
    *(unsigned int *)(a4 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4)));
    *(unsigned __int64 *)(a4 + 8) = v_xmm0;
    *(unsigned __int64 *)(a4 + 24) = (unsigned int)(*(unsigned int *)(a1 + 24));
    *(unsigned int *)(a4 + 32) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 28)));
    *(unsigned __int64 *)(a4 + 40) = (unsigned int)(*(unsigned int *)(a1 + 32));
    *(unsigned int *)(a4 + 48) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 36)));
    *(unsigned int *)(a4 + 52) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 40)));
loc_00962D7E:
    goto loc_00962DB3;
loc_00962DB3:
    goto loc_00962E5C;
loc_00962DB8:
    result = v_stack_p8;
    if ((((unsigned __int8)(a1)) & (7)) != 0) {
        result = ExRaiseDatatypeMisalignment(a1, a2, a3, a4);
    }
    a3 = ((unsigned int)(a2)) + (a1);
    if (a3 > result) goto loc_00962DDC;
    v_rdi = (unsigned int)((unsigned int)((unsigned int)(0xC000000DULL)));
    if (a3 < a1) {
        result = *(unsigned __int8 *)(result);
        v_rdi = v_stack_m40;
    }
    if (a2 >= 56) goto loc_00962DF7;
    v_stack_m40 = (unsigned int)((unsigned int)(0xC000000DULL));
    goto loc_00962E27;
loc_00962DF7:
    *(unsigned __int64 *)(a4) = v_xmm0;
    *(unsigned __int64 *)(a4 + 16) = v_xmm1;
    *(unsigned __int64 *)(a4 + 32) = v_xmm0;
    *(unsigned __int64 *)(a4 + 48) = v_xmm1;
    v_rdi = (unsigned int)((unsigned int)((unsigned int)(0xC000000DULL)));
    if ((*(unsigned int *)(a4)) != 56) { v_rdi = (unsigned int)((unsigned int)(0xC000000DULL)); }
    v_stack_m40 = (unsigned int)(v_rdi);
loc_00962E27:
    goto loc_00962E5C;
loc_00962E5C:
    if (sign_flag) goto loc_00962EFF;
    v_stack_m38 = *(unsigned __int64 *)(a4 + 24);
    *(unsigned __int64 *)(a4 + 24) = 0;
    result = Feature_KernelPnP_ObjectNameUpdates__private_IsEnabledDeviceUsageNoInline(a1, a2, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_00962F5F;
    if (*(unsigned __int64 *)(a4 + 24) == 0) goto loc_00962EED;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 32)) - 2)) > 398) goto loc_0096305F;
    v_stack_m50 = 1;
    v_stack_m58 = (unsigned __int8)(v_stack_p8);
    result = PiControlMakeUserModeCallersCopy(a4 + 24, v_stack_m38, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 32)))), 1 + 1);
    if (sign_flag) goto loc_00962EE1;
    v_stack_m3C = 1;
    a2 = ((unsigned int)(*(unsigned int *)(a4 + 32))) >> (1);
    *(unsigned __int16 *)(*(unsigned __int64 *)(a4 + 24) + a2 * 2 - 2) = 0;
    goto loc_00962FE9;
loc_00962EE1:
    *(unsigned __int64 *)(a4 + 24) = 0;
    *(unsigned int *)(a4 + 32) = 0;
    goto loc_00962FE9;
loc_00962EED:
    if ((unsigned int)(*(unsigned __int64 *)(a4 + 24)) == 0) goto loc_00962FE3;
loc_00962EF5:
loc_00962EF8:
loc_00962EFF:
loc_00962F04:
    if (!sign_flag) goto loc_00962F42;
    result = v_stack_p8;
    if (v_stack_m3C != 0) {
        a2 = *(unsigned __int64 *)(a4 + 24);
        a1 = (unsigned __int8)(v_stack_p8);
        result = PiControlFreeUserModeCallersBuffer(a1, a2, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 32)))), 1 + 1);
    }
    if ((unsigned int)((unsigned int)(v_stack_m44)) != 0) {
        a2 = *(unsigned __int64 *)(a4 + 40);
        a1 = v_stack_p8;
        result = PiControlFreeUserModeCallersBuffer(a1, a2, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 32)))), 1 + 1);
    }
    result = 0;
    *(unsigned __int64 *)(a4) = v_xmm0;
    *(unsigned __int64 *)(a4 + 16) = v_xmm0;
    *(unsigned __int64 *)(a4 + 32) = v_xmm0;
    *(unsigned __int64 *)(a4 + 48) = 0;
loc_00962F42:
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(0xC000000DULL)))));
loc_00962F5F:
    if (1 == 0) goto loc_00962FC0;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 32)))) < 2) goto loc_00962FC4;
    v_stack_m28 = 1;
    v_stack_m30 = (unsigned __int8)(v_stack_p30);
    result = PiControlMakeUserModeCallersCopy(a4 + 24, v_stack_m10, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 32)), 1 + 1);
    if (sign_flag) goto loc_00962FB6;
    v_stack_m14 = 1;
    a1 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 32))) >> (1);
    *(unsigned __int16 *)(*(unsigned __int64 *)(a4 + 24) + a1 * 2 - 2) = (unsigned __int16)(*(unsigned __int64 *)(v_stack_m28 + 56));
    goto loc_00962FE9;
loc_00962FB6:
    *(unsigned __int64 *)(a4 + 24) = *(unsigned __int64 *)(v_stack_m28 + 56);
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 32) = (unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 56));
    goto loc_00962FE9;
loc_00962FC0:
    v_r12 = (*(unsigned __int64 *)(v_stack_m28 + 64) + 32) + (32);
loc_00962FC4:
    if (1 != 0) goto loc_00962FD8;
    if ((*(unsigned int *)(v_r12)) > ((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 56)))) goto loc_00962EF5;
    if (1 == 0) goto loc_00962FE3;
loc_00962FD8:
    if ((*(unsigned int *)(v_r12)) < 2) goto loc_00962EF5;
loc_00962FE3:
loc_00962FE9:
    v_stack_m10 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 40);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 40) = *(unsigned __int64 *)(v_stack_m28 + 56);
    result = Feature_KernelPnP_ObjectNameUpdates__private_IsEnabledDeviceUsageNoInline(a1, v_stack_m10, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 32)), 1 + 1);
    if ((unsigned int)(result) == 0) goto loc_00963067;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 40) == 0) goto loc_00963050;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 48)) - 2)) > 0xFFFDULL) goto loc_0096305F;
    v_stack_m28 = 1;
    v_stack_m30 = (unsigned __int8)(v_stack_p30);
    result = PiControlMakeUserModeCallersCopy(*(unsigned __int64 *)(v_stack_m28 + 64) + 40, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 40), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 48)))), 2);
    if (sign_flag) goto loc_00963044;
    goto loc_009630A7;
loc_00963044:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 40) = *(unsigned __int64 *)(v_stack_m28 + 56);
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 48) = (unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 56));
    goto loc_00962EF8;
loc_00963050:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 48))) == 0) goto loc_00962EFF;
loc_0096305F:
    goto loc_00962EFF;
loc_00963067:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 40) == 0) goto loc_009630CF;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 48)))) < 2) goto loc_009630D8;
    v_stack_m28 = 1;
    v_stack_m30 = (unsigned __int8)(v_stack_p30);
    result = PiControlMakeUserModeCallersCopy(*(unsigned __int64 *)(v_stack_m28 + 64) + 40, v_stack_m10, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 48)), 2);
    if (sign_flag) goto loc_009630C2;
loc_009630A7:
    a1 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 48))) >> (1);
    *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 40) + a1 * 2 - 2) = (unsigned __int16)(*(unsigned __int64 *)(v_stack_m28 + 56));
    goto loc_00962F04;
loc_009630C2:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 40) = *(unsigned __int64 *)(v_stack_m28 + 56);
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 48) = (unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 56));
    goto loc_00962EF8;
loc_009630CF:
    v_r13 = (v_stack_m8) + (48);
loc_009630D8:
    if (v_stack_m10 != 0) goto loc_009630F5;
    if ((*(unsigned int *)(v_r13)) > ((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 56)))) goto loc_00962EF5;
    if (v_stack_m10 == 0) goto loc_00962EF8;
loc_009630F5:
    if ((*(unsigned int *)(v_r13)) >= 2) goto loc_00962EF8;
    goto loc_00962EF5;
loc_00963105:
    goto loc_00962F04;
}
```

## 5. (Beta) C Style

```c
int64_t PiCMCaptureRegisterInterfaceInputData(int64_t Arg1, int32_t Arg2, int32_t Arg3, void *Arg4)
{
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
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
    if (Arg1 == 0) goto loc_00963105;
    if (Arg2 == 0) goto loc_00963105;
    if (Arg3 == 0) goto loc_00962DB8;
    result = *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232);
    if ((((uint8_t)(Arg1)) & (3)) != 0) {
        result = ExRaiseDatatypeMisalignment(Arg1, Arg2, Arg3, Arg4);
    }
    Arg3 = ((uint32_t)(Arg2)) + (Arg1);
    if (Arg3 > result) goto loc_00962D23;
    local_rdi = 0;
    if (Arg3 < Arg1) {
        result = *(uint8_t *)(result);
        local_rdi = v_stack_m40;
    }
    if (Arg2 >= 44) goto loc_00962D3E;
loc_00962D34:
    v_stack_m40 = (uint32_t)((uint32_t)(0xC000000DULL));
    goto loc_00962D7E;
loc_00962D3E:
    if ((*(uint32_t *)(Arg1)) != 44) goto loc_00962D34;
    *(uint32_t *)(arg4) = 56;
    *(uint32_t *)(arg4 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x4)));
    *(uint64_t *)(arg4 + 0x8) = v_xmm0;
    *(uint64_t *)(arg4 + 0x18) = (uint32_t)(*(uint32_t *)(Arg1 + 0x18));
    *(uint32_t *)(arg4 + 0x20) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x1C)));
    *(uint64_t *)(arg4 + 0x28) = (uint32_t)(*(uint32_t *)(Arg1 + 0x20));
    *(uint32_t *)(arg4 + 0x30) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x24)));
    *(uint32_t *)(arg4 + 0x34) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x28)));
loc_00962D7E:
    goto loc_00962DB3;
loc_00962DB3:
    goto loc_00962E5C;
loc_00962DB8:
    result = v_stack_p8;
    if ((((uint8_t)(Arg1)) & (7)) != 0) {
        result = ExRaiseDatatypeMisalignment(Arg1, Arg2, Arg3, Arg4);
    }
    Arg3 = ((uint32_t)(Arg2)) + (Arg1);
    if (Arg3 > result) goto loc_00962DDC;
    local_rdi = (uint32_t)((uint32_t)((uint32_t)(0xC000000DULL)));
    if (Arg3 < Arg1) {
        result = *(uint8_t *)(result);
        local_rdi = v_stack_m40;
    }
    if (Arg2 >= 56) goto loc_00962DF7;
    v_stack_m40 = (uint32_t)((uint32_t)(0xC000000DULL));
    goto loc_00962E27;
loc_00962DF7:
    *(uint64_t *)(arg4) = v_xmm0;
    *(uint64_t *)(arg4 + 0x10) = v_xmm1;
    *(uint64_t *)(arg4 + 0x20) = v_xmm0;
    *(uint64_t *)(arg4 + 0x30) = v_xmm1;
    local_rdi = (uint32_t)((uint32_t)((uint32_t)(0xC000000DULL)));
    if ((*(uint32_t *)(arg4)) != 56) { local_rdi = (uint32_t)((uint32_t)(0xC000000DULL)); }
    v_stack_m40 = (uint32_t)(local_rdi);
loc_00962E27:
    goto loc_00962E5C;
loc_00962E5C:
    if (sign_flag) goto loc_00962EFF;
    v_stack_m38 = *(uint64_t *)(arg4 + 0x18);
    *(uint64_t *)(arg4 + 0x18) = 0;
    result = Feature_KernelPnP_ObjectNameUpdates__private_IsEnabledDeviceUsageNoInline(Arg1, Arg2, Arg3, Arg4);
    if ((uint32_t)(result) == 0) goto loc_00962F5F;
    if (*(uint64_t *)(arg4 + 0x18) == 0) goto loc_00962EED;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x20)) - 2)) > 398) goto loc_0096305F;
    v_stack_m50 = 1;
    v_stack_m58 = (uint8_t)(v_stack_p8);
    result = PiControlMakeUserModeCallersCopy(Arg4 + 24, v_stack_m38, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x20)))), 1 + 1);
    if (sign_flag) goto loc_00962EE1;
    v_stack_m3C = 1;
    Arg2 = ((uint32_t)(*(uint32_t *)(arg4 + 0x20))) >> (1);
    *(uint16_t *)(*(uint64_t *)(arg4 + 0x18) + Arg2 * 2 - 0x2) = 0;
    goto loc_00962FE9;
loc_00962EE1:
    *(uint64_t *)(arg4 + 0x18) = 0;
    *(uint32_t *)(arg4 + 0x20) = 0;
    goto loc_00962FE9;
loc_00962EED:
    if ((uint32_t)(*(uint64_t *)(arg4 + 0x18)) == 0) goto loc_00962FE3;
loc_00962EF5:
loc_00962EF8:
loc_00962EFF:
loc_00962F04:
    if (!sign_flag) goto loc_00962F42;
    result = v_stack_p8;
    if (v_stack_m3C != 0) {
        Arg2 = *(uint64_t *)(arg4 + 0x18);
        Arg1 = (uint8_t)(v_stack_p8);
        result = PiControlFreeUserModeCallersBuffer(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x20)))), 1 + 1);
    }
    if ((uint32_t)((uint32_t)(v_stack_m44)) != 0) {
        Arg2 = *(uint64_t *)(arg4 + 0x28);
        Arg1 = v_stack_p8;
        result = PiControlFreeUserModeCallersBuffer(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x20)))), 1 + 1);
    }
    result = 0;
    *(uint64_t *)(arg4) = v_xmm0;
    *(uint64_t *)(arg4 + 0x10) = v_xmm0;
    *(uint64_t *)(arg4 + 0x20) = v_xmm0;
    *(uint64_t *)(arg4 + 0x30) = 0;
loc_00962F42:
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(0xC000000DULL)))));
loc_00962F5F:
    if (1 == 0) goto loc_00962FC0;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x20)))) < 2) goto loc_00962FC4;
    v_stack_m28 = 1;
    v_stack_m30 = (uint8_t)(v_stack_p30);
    result = PiControlMakeUserModeCallersCopy(Arg4 + 24, v_stack_m10, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x20)), 1 + 1);
    if (sign_flag) goto loc_00962FB6;
    v_stack_m14 = 1;
    Arg1 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x20))) >> (1);
    *(uint16_t *)(*(uint64_t *)(arg4 + 0x18) + Arg1 * 2 - 0x2) = (uint16_t)(*(uint64_t *)(v_stack_m28 + 0x38));
    goto loc_00962FE9;
loc_00962FB6:
    *(uint64_t *)(arg4 + 0x18) = *(uint64_t *)(v_stack_m28 + 0x38);
    *(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x20) = (uint32_t)(*(uint64_t *)(v_stack_m28 + 0x38));
    goto loc_00962FE9;
loc_00962FC0:
    local_r12 = (*(uint64_t *)(v_stack_m28 + 0x40) + 32) + (32);
loc_00962FC4:
    if (1 != 0) goto loc_00962FD8;
    if ((*(uint32_t *)(local_r12)) > ((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x38)))) goto loc_00962EF5;
    if (1 == 0) goto loc_00962FE3;
loc_00962FD8:
    if ((*(uint32_t *)(local_r12)) < 2) goto loc_00962EF5;
loc_00962FE3:
loc_00962FE9:
    v_stack_m10 = *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x28);
    *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x28) = *(uint64_t *)(v_stack_m28 + 0x38);
    result = Feature_KernelPnP_ObjectNameUpdates__private_IsEnabledDeviceUsageNoInline(Arg1, v_stack_m10, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x20)), 1 + 1);
    if ((uint32_t)(result) == 0) goto loc_00963067;
    if (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x28) == 0) goto loc_00963050;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x30)) - 2)) > 0xFFFDULL) goto loc_0096305F;
    v_stack_m28 = 1;
    v_stack_m30 = (uint8_t)(v_stack_p30);
    result = PiControlMakeUserModeCallersCopy(*(uint64_t *)(v_stack_m28 + 0x40) + 40, *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x28), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x30)))), 2);
    if (sign_flag) goto loc_00963044;
    goto loc_009630A7;
loc_00963044:
    *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x28) = *(uint64_t *)(v_stack_m28 + 0x38);
    *(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x30) = (uint32_t)(*(uint64_t *)(v_stack_m28 + 0x38));
    goto loc_00962EF8;
loc_00963050:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x30))) == 0) goto loc_00962EFF;
loc_0096305F:
    goto loc_00962EFF;
loc_00963067:
    if (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x28) == 0) goto loc_009630CF;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x30)))) < 2) goto loc_009630D8;
    v_stack_m28 = 1;
    v_stack_m30 = (uint8_t)(v_stack_p30);
    result = PiControlMakeUserModeCallersCopy(*(uint64_t *)(v_stack_m28 + 0x40) + 40, v_stack_m10, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x30)), 2);
    if (sign_flag) goto loc_009630C2;
loc_009630A7:
    Arg1 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x30))) >> (1);
    *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x28) + Arg1 * 2 - 0x2) = (uint16_t)(*(uint64_t *)(v_stack_m28 + 0x38));
    goto loc_00962F04;
loc_009630C2:
    *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x28) = *(uint64_t *)(v_stack_m28 + 0x38);
    *(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x30) = (uint32_t)(*(uint64_t *)(v_stack_m28 + 0x38));
    goto loc_00962EF8;
loc_009630CF:
    local_r13 = (v_stack_m8) + (48);
loc_009630D8:
    if (v_stack_m10 != 0) goto loc_009630F5;
    if ((*(uint32_t *)(local_r13)) > ((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x38)))) goto loc_00962EF5;
    if (v_stack_m10 == 0) goto loc_00962EF8;
loc_009630F5:
    if ((*(uint32_t *)(local_r13)) >= 2) goto loc_00962EF8;
    goto loc_00962EF5;
loc_00963105:
    goto loc_00962F04;
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
| `Arg4` | `+ 0x10` | `128` | `R` |
| `Arg4` | `+ 0x18` | `64` | `R` |
| `Arg4` | `+ 0x20` | `32` | `R` |
| `Arg4` | `+ 0x20` | `32` | `W` |
| `Arg4` | `+ 0x20` | `64` | `R` |
| `Arg4` | `+ 0x20` | `128` | `R` |
| `Arg4` | `+ 0x28` | `64` | `R` |
| `Arg4` | `+ 0x30` | `32` | `R` |
| `Arg4` | `+ 0x30` | `32` | `W` |
| `Arg4` | `+ 0x30` | `64` | `R` |
| `Arg4` | `+ 0x30` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00962C94&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
