# NtCreateTokenEx

- RVA: `0x009C7C80`–`0x009C86BA` (길이 `2,618` bytes)
- VA: `0x00000001409C7C80`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A0850`
- 디코드: `551`개 명령, `2,618/2,618` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **32**; 고유 호출 대상: **15**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x009C7E58` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x009C7EA6` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x009C803B` → [SeCaptureSecurityQos](../8B/SeCaptureSecurityQos_function_008B71B8.md) (function, `0x008B71B8`)
- `0x009C80B0` → [SeCaptureSidAndAttributesArray](SeCaptureSidAndAttributesArray_function_009C9D70.md) (function, `0x009C9D70`)
- `0x009C80FE` → [SeCaptureSidAndAttributesArray](SeCaptureSidAndAttributesArray_function_009C9D70.md) (function, `0x009C9D70`)
- `0x009C816A` → [SeCaptureLuidAndAttributesArray](SeCaptureLuidAndAttributesArray_function_009C8D18.md) (function, `0x009C8D18`)
- `0x009C81A7` → [SeCaptureSid](../92/SeCaptureSid_function_009276D4.md) (function, `0x009276D4`)
- `0x009C81EC` → [SeCaptureAcl](SeCaptureAcl_function_009C6A58.md) (function, `0x009C6A58`)
- `0x009C8274` → [SeCaptureSid](../92/SeCaptureSid_function_009276D4.md) (function, `0x009276D4`)
- `0x009C82BD` → [SeCaptureSidAndAttributesArray](SeCaptureSidAndAttributesArray_function_009C9D70.md) (function, `0x009C9D70`)
- `0x009C82FD` → [SepCaptureTokenSecurityAttributesInformation](../97/SepCaptureTokenSecurityAttributesInformation_function_00971FB8.md) (function, `0x00971FB8`)
- `0x009C833D` → [SepCaptureTokenSecurityAttributesInformation](../97/SepCaptureTokenSecurityAttributesInformation_function_00971FB8.md) (function, `0x00971FB8`)
- `0x009C836D` → [SeReleaseLuidAndAttributesArray](SeReleaseLuidAndAttributesArray_function_009C7C40.md) (function, `0x009C7C40`)
- `0x009C8381` → [SeReleaseLuidAndAttributesArray](SeReleaseLuidAndAttributesArray_function_009C7C40.md) (function, `0x009C7C40`)
- `0x009C8395` → [SeReleaseLuidAndAttributesArray](SeReleaseLuidAndAttributesArray_function_009C7C40.md) (function, `0x009C7C40`)
- `0x009C83AC` → [SeReleaseSid](../A2/SeReleaseSid_function_00A2EF50.md) (function, `0x00A2EF50`)
- `0x009C83C3` → [SeReleaseSid](../A2/SeReleaseSid_function_00A2EF50.md) (function, `0x00A2EF50`)
- `0x009C83D7` → [SeReleaseAcl](SeReleaseAcl_function_009C7C64.md) (function, `0x009C7C64`)
- `0x009C83EB` → [SeReleaseLuidAndAttributesArray](SeReleaseLuidAndAttributesArray_function_009C7C40.md) (function, `0x009C7C40`)
- `0x009C83FD` → [SepFreeCapturedTokenSecurityAttributesInformation](../A4/SepFreeCapturedTokenSecurityAttributesInformation_function_00A4D124.md) (function, `0x00A4D124`)
- `0x009C840F` → [SepFreeCapturedTokenSecurityAttributesInformation](../A4/SepFreeCapturedTokenSecurityAttributesInformation_function_00A4D124.md) (function, `0x00A4D124`)
- `0x009C8433` → [SeReleaseLuidAndAttributesArray](SeReleaseLuidAndAttributesArray_function_009C7C40.md) (function, `0x009C7C40`)
- `0x009C8448` → [SeReleaseLuidAndAttributesArray](SeReleaseLuidAndAttributesArray_function_009C7C40.md) (function, `0x009C7C40`)
- `0x009C845D` → [SeReleaseLuidAndAttributesArray](SeReleaseLuidAndAttributesArray_function_009C7C40.md) (function, `0x009C7C40`)
- `0x009C849C` → [SeReleaseAcl](SeReleaseAcl_function_009C7C64.md) (function, `0x009C7C64`)
- `0x009C84E9` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x009C8504` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x009C850D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x009C865C` → [SepCreateTokenEx](../../text/4E/SepCreateTokenEx_function_004E9CD0.md) (function, `0x004E9CD0`)
- `0x009C8692` → [SeReleaseLuidAndAttributesArray](SeReleaseLuidAndAttributesArray_function_009C7C40.md) (function, `0x009C7C40`)
- `0x009C869C` → [SepFreeCapturedTokenSecurityAttributesInformation](../A4/SepFreeCapturedTokenSecurityAttributesInformation_function_00A4D124.md) (function, `0x00A4D124`)
- `0x009C86A6` → [SepFreeCapturedTokenSecurityAttributesInformation](../A4/SepFreeCapturedTokenSecurityAttributesInformation_function_00A4D124.md) (function, `0x00A4D124`)

### Direct callers
- [NtCreateToken](../7A/NtCreateToken_function_007A0720.md) at `0x007A07A8`

### Static image references
- `0x009C7C95` → RVA `0x00E0A740` (`.data`; read)
- `0x009C7E51` → RVA `0x00FD9B80` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **4**
  - `0x009C84E9` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x009C8504` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x009C850D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x009C865C` → [SepCreateTokenEx](../../text/4E/SepCreateTokenEx_function_004E9CD0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009C7C80  4C 8B DC                        mov r11, rsp
009C7C83  53                              push rbx
009C7C84  56                              push rsi
009C7C85  57                              push rdi
009C7C86  41 54                           push r12
009C7C88  41 55                           push r13
009C7C8A  41 56                           push r14
009C7C8C  41 57                           push r15
009C7C8E  48 81 EC E0 01 00 00            sub rsp, 0x1e0
009C7C95  48 8B 05 A4 2A 44 00            mov rax, qword ptr [rip + 0x442aa4]
009C7C9C  48 33 C4                        xor rax, rsp
009C7C9F  48 89 84 24 D8 01 00 00         mov qword ptr [rsp + 0x1d8], rax
009C7CA7  44 89 8C 24 E0 00 00 00         mov dword ptr [rsp + 0xe0], r9d
009C7CAF  4C 89 84 24 88 01 00 00         mov qword ptr [rsp + 0x188], r8
009C7CB7  89 94 24 40 01 00 00            mov dword ptr [rsp + 0x140], edx
009C7CBE  48 89 8C 24 98 01 00 00         mov qword ptr [rsp + 0x198], rcx
009C7CC6  4C 8B BC 24 68 02 00 00         mov r15, qword ptr [rsp + 0x268]
009C7CCE  4C 8B A4 24 70 02 00 00         mov r12, qword ptr [rsp + 0x270]
009C7CD6  4C 8B B4 24 78 02 00 00         mov r14, qword ptr [rsp + 0x278]
009C7CDE  48 8B BC 24 80 02 00 00         mov rdi, qword ptr [rsp + 0x280]
009C7CE6  48 89 BC 24 C0 01 00 00         mov qword ptr [rsp + 0x1c0], rdi
009C7CEE  48 8B 84 24 40 02 00 00         mov rax, qword ptr [rsp + 0x240]
009C7CF6  48 89 84 24 48 01 00 00         mov qword ptr [rsp + 0x148], rax
009C7CFE  4C 8B AC 24 98 02 00 00         mov r13, qword ptr [rsp + 0x298]
009C7D06  48 8B 84 24 90 02 00 00         mov rax, qword ptr [rsp + 0x290]
009C7D0E  48 89 84 24 68 01 00 00         mov qword ptr [rsp + 0x168], rax
009C7D16  48 8B 9C 24 88 02 00 00         mov rbx, qword ptr [rsp + 0x288]
009C7D1E  48 89 9C 24 B8 01 00 00         mov qword ptr [rsp + 0x1b8], rbx
009C7D26  48 8B 84 24 A0 02 00 00         mov rax, qword ptr [rsp + 0x2a0]
009C7D2E  48 89 84 24 70 01 00 00         mov qword ptr [rsp + 0x170], rax
009C7D36  48 8B 84 24 60 02 00 00         mov rax, qword ptr [rsp + 0x260]
009C7D3E  48 89 84 24 60 01 00 00         mov qword ptr [rsp + 0x160], rax
009C7D46  48 8B 84 24 58 02 00 00         mov rax, qword ptr [rsp + 0x258]
009C7D4E  48 89 84 24 58 01 00 00         mov qword ptr [rsp + 0x158], rax
009C7D56  48 8B 84 24 48 02 00 00         mov rax, qword ptr [rsp + 0x248]
009C7D5E  48 89 84 24 50 01 00 00         mov qword ptr [rsp + 0x150], rax
009C7D66  48 8B 84 24 50 02 00 00         mov rax, qword ptr [rsp + 0x250]
009C7D6E  48 89 84 24 B0 01 00 00         mov qword ptr [rsp + 0x1b0], rax
009C7D76  33 C9                           xor ecx, ecx
009C7D78  89 8C 24 38 01 00 00            mov dword ptr [rsp + 0x138], ecx
009C7D7F  49 89 8B 78 FF FF FF            mov qword ptr [r11 - 0x88], rcx
009C7D86  88 8C 24 C0 00 00 00            mov byte ptr [rsp + 0xc0], cl
009C7D8D  33 C0                           xor eax, eax
009C7D8F  49 89 43 88                     mov qword ptr [r11 - 0x78], rax
009C7D93  41 89 43 90                     mov dword ptr [r11 - 0x70], eax
009C7D97  49 89 8B 68 FF FF FF            mov qword ptr [r11 - 0x98], rcx
009C7D9E  49 89 8B 60 FF FF FF            mov qword ptr [r11 - 0xa0], rcx
009C7DA5  49 89 8B F8 FE FF FF            mov qword ptr [r11 - 0x108], rcx
009C7DAC  89 8C 24 30 01 00 00            mov dword ptr [rsp + 0x130], ecx
009C7DB3  89 8C 24 DC 00 00 00            mov dword ptr [rsp + 0xdc], ecx
009C7DBA  49 89 8B 00 FF FF FF            mov qword ptr [r11 - 0x100], rcx
009C7DC1  89 8C 24 C8 00 00 00            mov dword ptr [rsp + 0xc8], ecx
009C7DC8  89 8C 24 D8 00 00 00            mov dword ptr [rsp + 0xd8], ecx
009C7DCF  49 89 8B 08 FF FF FF            mov qword ptr [r11 - 0xf8], rcx
009C7DD6  89 8C 24 34 01 00 00            mov dword ptr [rsp + 0x134], ecx
009C7DDD  49 89 8B 10 FF FF FF            mov qword ptr [r11 - 0xf0], rcx
009C7DE4  49 89 8B D0 FE FF FF            mov qword ptr [r11 - 0x130], rcx
009C7DEB  49 89 8B D8 FE FF FF            mov qword ptr [r11 - 0x128], rcx
009C7DF2  0F 57 C0                        xorps xmm0, xmm0
009C7DF5  41 0F 11 43 B0                  movups xmmword ptr [r11 - 0x50], xmm0
009C7DFA  89 8C 24 D0 00 00 00            mov dword ptr [rsp + 0xd0], ecx
009C7E01  88 8C 24 C1 00 00 00            mov byte ptr [rsp + 0xc1], cl
009C7E08  49 89 8B E8 FE FF FF            mov qword ptr [r11 - 0x118], rcx
009C7E0F  49 89 8B F0 FE FF FF            mov qword ptr [r11 - 0x110], rcx
009C7E16  C7 84 24 CC 00 00 00 01 00 00 00  mov dword ptr [rsp + 0xcc], 1
009C7E21  89 8C 24 D4 00 00 00            mov dword ptr [rsp + 0xd4], ecx
009C7E28  49 89 8B E0 FE FF FF            mov qword ptr [r11 - 0x120], rcx
009C7E2F  89 8C 24 3C 01 00 00            mov dword ptr [rsp + 0x13c], ecx
009C7E36  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
009C7E3F  40 8A B0 32 02 00 00            mov sil, byte ptr [rax + 0x232]
009C7E46  40 88 B4 24 C2 00 00 00         mov byte ptr [rsp + 0xc2], sil
009C7E4E  40 8A D6                        mov dl, sil
009C7E51  48 8B 0D 28 1D 61 00            mov rcx, qword ptr [rip + 0x611d28]
009C7E58  E8 C3 9F EA FF                  call 0x140871e20
009C7E5D  84 C0                           test al, al
009C7E5F  0F 84 20 08 00 00               je 0x1409c8685
009C7E65  40 84 F6                        test sil, sil
009C7E68  0F 84 9F 01 00 00               je 0x1409c800d
009C7E6E  48 BA 00 00 FF FF FF 7F 00 00   movabs rdx, 0x7fffffff0000
009C7E78  48 8B CA                        mov rcx, rdx
009C7E7B  48 39 94 24 98 01 00 00         cmp qword ptr [rsp + 0x198], rdx
009C7E83  48 0F 42 8C 24 98 01 00 00      cmovb rcx, qword ptr [rsp + 0x198]
009C7E8C  48 8B 01                        mov rax, qword ptr [rcx]
009C7E8F  48 89 01                        mov qword ptr [rcx], rax
009C7E92  41 B0 03                        mov r8b, 3
009C7E95  48 8B 8C 24 50 01 00 00         mov rcx, qword ptr [rsp + 0x150]
009C7E9D  41 84 C8                        test r8b, cl
009C7EA0  0F 84 9A 00 00 00               je 0x1409c7f40
009C7EA6  E8 25 21 ED FF                  call 0x140899fd0
009C7EAB  CC                              int3
009C7EAC  48 8B C2                        mov rax, rdx
009C7EAF  48 3B CA                        cmp rcx, rdx
009C7EB2  48 0F 42 C1                     cmovb rax, rcx
009C7EB6  90                              nop
009C7EB7  8A 00                           mov al, byte ptr [rax]
009C7EB9  48 85 DB                        test rbx, rbx
009C7EBC  74 12                           je 0x1409c7ed0
009C7EBE  41 84 D8                        test r8b, bl
009C7EC1  75 E3                           jne 0x1409c7ea6
009C7EC3  48 8B C2                        mov rax, rdx
009C7EC6  48 3B DA                        cmp rbx, rdx
009C7EC9  48 0F 42 C3                     cmovb rax, rbx
009C7ECD  90                              nop
009C7ECE  8A 00                           mov al, byte ptr [rax]
009C7ED0  48 8B 8C 24 68 01 00 00         mov rcx, qword ptr [rsp + 0x168]
009C7ED8  41 84 C8                        test r8b, cl
009C7EDB  75 C9                           jne 0x1409c7ea6
009C7EDD  48 8B C2                        mov rax, rdx
009C7EE0  48 3B CA                        cmp rcx, rdx
009C7EE3  48 0F 42 C1                     cmovb rax, rcx
009C7EE7  90                              nop
009C7EE8  8A 00                           mov al, byte ptr [rax]
009C7EEA  4D 85 ED                        test r13, r13
009C7EED  74 12                           je 0x1409c7f01
009C7EEF  45 84 E8                        test r8b, r13b
009C7EF2  75 B2                           jne 0x1409c7ea6
009C7EF4  48 8B C2                        mov rax, rdx
009C7EF7  4C 3B EA                        cmp r13, rdx
009C7EFA  49 0F 42 C5                     cmovb rax, r13
009C7EFE  90                              nop
009C7EFF  8A 00                           mov al, byte ptr [rax]
009C7F01  48 8B 8C 24 48 01 00 00         mov rcx, qword ptr [rsp + 0x148]
009C7F09  41 84 C8                        test r8b, cl
009C7F0C  75 98                           jne 0x1409c7ea6
009C7F0E  48 8B C2                        mov rax, rdx
009C7F11  48 3B CA                        cmp rcx, rdx
009C7F14  48 0F 42 C1                     cmovb rax, rcx
009C7F18  90                              nop
009C7F19  8A 00                           mov al, byte ptr [rax]
009C7F1B  48 85 FF                        test rdi, rdi
009C7F1E  75 7F                           jne 0x1409c7f9f
009C7F20  4D 85 F6                        test r14, r14
009C7F23  0F 85 91 00 00 00               jne 0x1409c7fba
009C7F29  4D 85 E4                        test r12, r12
009C7F2C  0F 85 A3 00 00 00               jne 0x1409c7fd5
009C7F32  4D 85 FF                        test r15, r15
009C7F35  0F 85 B5 00 00 00               jne 0x1409c7ff0
009C7F3B  E9 CD 00 00 00                  jmp 0x1409c800d
009C7F40  48 8B C2                        mov rax, rdx
009C7F43  48 3B CA                        cmp rcx, rdx
009C7F46  48 0F 42 C1                     cmovb rax, rcx
009C7F4A  90                              nop
009C7F4B  8A 00                           mov al, byte ptr [rax]
009C7F4D  48 8B 8C 24 58 01 00 00         mov rcx, qword ptr [rsp + 0x158]
009C7F55  41 84 C8                        test r8b, cl
009C7F58  0F 85 48 FF FF FF               jne 0x1409c7ea6
009C7F5E  48 8B C2                        mov rax, rdx
009C7F61  48 3B CA                        cmp rcx, rdx
009C7F64  48 0F 42 C1                     cmovb rax, rcx
009C7F68  90                              nop
009C7F69  8A 00                           mov al, byte ptr [rax]
009C7F6B  48 8B 8C 24 60 01 00 00         mov rcx, qword ptr [rsp + 0x160]
009C7F73  41 84 C8                        test r8b, cl
009C7F76  0F 85 2A FF FF FF               jne 0x1409c7ea6
009C7F7C  48 8B C2                        mov rax, rdx
009C7F7F  48 3B CA                        cmp rcx, rdx
009C7F82  48 0F 42 C1                     cmovb rax, rcx
009C7F86  90                              nop
009C7F87  8A 00                           mov al, byte ptr [rax]
009C7F89  48 8B 8C 24 70 01 00 00         mov rcx, qword ptr [rsp + 0x170]
009C7F91  41 84 C8                        test r8b, cl
009C7F94  0F 85 0C FF FF FF               jne 0x1409c7ea6
009C7F9A  E9 0D FF FF FF                  jmp 0x1409c7eac
009C7F9F  41 84 F8                        test r8b, dil
009C7FA2  0F 85 FE FE FF FF               jne 0x1409c7ea6
009C7FA8  48 8B C2                        mov rax, rdx
009C7FAB  48 3B FA                        cmp rdi, rdx
009C7FAE  48 0F 42 C7                     cmovb rax, rdi
009C7FB2  90                              nop
009C7FB3  8A 00                           mov al, byte ptr [rax]
009C7FB5  E9 66 FF FF FF                  jmp 0x1409c7f20
009C7FBA  45 84 F0                        test r8b, r14b
009C7FBD  0F 85 E3 FE FF FF               jne 0x1409c7ea6
009C7FC3  48 8B C2                        mov rax, rdx
009C7FC6  4C 3B F2                        cmp r14, rdx
009C7FC9  49 0F 42 C6                     cmovb rax, r14
009C7FCD  90                              nop
009C7FCE  8A 00                           mov al, byte ptr [rax]
009C7FD0  E9 54 FF FF FF                  jmp 0x1409c7f29
009C7FD5  45 84 E0                        test r8b, r12b
009C7FD8  0F 85 C8 FE FF FF               jne 0x1409c7ea6
009C7FDE  48 8B C2                        mov rax, rdx
009C7FE1  4C 3B E2                        cmp r12, rdx
009C7FE4  49 0F 42 C4                     cmovb rax, r12
009C7FE8  90                              nop
009C7FE9  8A 00                           mov al, byte ptr [rax]
009C7FEB  E9 42 FF FF FF                  jmp 0x1409c7f32
009C7FF0  45 84 F8                        test r8b, r15b
009C7FF3  0F 85 AD FE FF FF               jne 0x1409c7ea6
009C7FF9  4C 3B FA                        cmp r15, rdx
009C7FFC  49 0F 42 D7                     cmovb rdx, r15
009C8000  90                              nop
009C8001  8A 02                           mov al, byte ptr [rdx]
009C8003  E9 33 FF FF FF                  jmp 0x1409c7f3b
009C8008  E9 D1 04 00 00                  jmp 0x1409c84de
009C800D  8B BC 24 E0 00 00 00            mov edi, dword ptr [rsp + 0xe0]
009C8014  8D 47 FF                        lea eax, [rdi - 1]
009C8017  83 F8 01                        cmp eax, 1
009C801A  0F 87 90 06 00 00               ja 0x1409c86b0
009C8020  4C 8D 8C 24 A0 01 00 00         lea r9, [rsp + 0x1a0]
009C8028  4C 8D 84 24 C0 00 00 00         lea r8, [rsp + 0xc0]
009C8030  40 8A D6                        mov dl, sil
009C8033  48 8B 8C 24 88 01 00 00         mov rcx, qword ptr [rsp + 0x188]
009C803B  E8 78 F1 EE FF                  call 0x1408b71b8
009C8040  33 C9                           xor ecx, ecx
009C8042  85 C0                           test eax, eax
009C8044  0F 88 94 04 00 00               js 0x1409c84de
009C804A  83 FF 02                        cmp edi, 2
009C804D  0F 84 C4 04 00 00               je 0x1409c8517
009C8053  89 8C 24 C4 00 00 00            mov dword ptr [rsp + 0xc4], ecx
009C805A  48 8B 84 24 48 01 00 00         mov rax, qword ptr [rsp + 0x148]
009C8062  48 8B 00                        mov rax, qword ptr [rax]
009C8065  48 89 84 24 80 01 00 00         mov qword ptr [rsp + 0x180], rax
009C806D  48 8B 84 24 50 01 00 00         mov rax, qword ptr [rsp + 0x150]
009C8075  48 8B 00                        mov rax, qword ptr [rax]
009C8078  48 89 84 24 78 01 00 00         mov qword ptr [rsp + 0x178], rax
009C8080  48 8D 84 24 30 01 00 00         lea rax, [rsp + 0x130]
009C8088  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
009C808D  48 8D 84 24 10 01 00 00         lea rax, [rsp + 0x110]
009C8095  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
009C809A  89 4C 24 20                     mov dword ptr [rsp + 0x20], ecx
009C809E  45 33 C9                        xor r9d, r9d
009C80A1  44 8A C6                        mov r8b, sil
009C80A4  41 8D 51 01                     lea edx, [r9 + 1]
009C80A8  48 8B 8C 24 B0 01 00 00         mov rcx, qword ptr [rsp + 0x1b0]
009C80B0  E8 BB 1C 00 00                  call 0x1409c9d70
009C80B5  8B F8                           mov edi, eax
009C80B7  89 84 24 C4 00 00 00            mov dword ptr [rsp + 0xc4], eax
009C80BE  85 C0                           test eax, eax
009C80C0  78 72                           js 0x1409c8134
009C80C2  48 8B 84 24 58 01 00 00         mov rax, qword ptr [rsp + 0x158]
009C80CA  8B 18                           mov ebx, dword ptr [rax]
009C80CC  89 9C 24 DC 00 00 00            mov dword ptr [rsp + 0xdc], ebx
009C80D3  48 8D 48 08                     lea rcx, [rax + 8]
009C80D7  48 8D 84 24 C8 00 00 00         lea rax, [rsp + 0xc8]
009C80DF  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
009C80E4  48 8D 84 24 18 01 00 00         lea rax, [rsp + 0x118]
009C80EC  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
009C80F1  83 64 24 20 00                  and dword ptr [rsp + 0x20], 0
009C80F6  45 33 C9                        xor r9d, r9d
009C80F9  44 8A C6                        mov r8b, sil
009C80FC  8B D3                           mov edx, ebx
009C80FE  E8 6D 1C 00 00                  call 0x1409c9d70
009C8103  8B F8                           mov edi, eax
009C8105  89 84 24 C4 00 00 00            mov dword ptr [rsp + 0xc4], eax
009C810C  C1 E3 04                        shl ebx, 4
009C810F  8B 84 24 C8 00 00 00            mov eax, dword ptr [rsp + 0xc8]
009C8116  2B C3                           sub eax, ebx
009C8118  89 84 24 C8 00 00 00            mov dword ptr [rsp + 0xc8], eax
009C811F  83 C0 03                        add eax, 3
009C8122  83 E0 FC                        and eax, 0xfffffffc
009C8125  89 84 24 C8 00 00 00            mov dword ptr [rsp + 0xc8], eax
009C812C  48 8B 9C 24 B8 01 00 00         mov rbx, qword ptr [rsp + 0x1b8]
009C8134  85 FF                           test edi, edi
009C8136  78 40                           js 0x1409c8178
009C8138  48 8B 84 24 60 01 00 00         mov rax, qword ptr [rsp + 0x160]
009C8140  8B 10                           mov edx, dword ptr [rax]
009C8142  89 94 24 D8 00 00 00            mov dword ptr [rsp + 0xd8], edx
009C8149  48 8D 48 04                     lea rcx, [rax + 4]
009C814D  48 8D 84 24 34 01 00 00         lea rax, [rsp + 0x134]
009C8155  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
009C815A  48 8D 84 24 20 01 00 00         lea rax, [rsp + 0x120]
009C8162  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
009C8167  44 8A C6                        mov r8b, sil
009C816A  E8 A9 0B 00 00                  call 0x1409c8d18
009C816F  8B F8                           mov edi, eax
009C8171  89 84 24 C4 00 00 00            mov dword ptr [rsp + 0xc4], eax
009C8178  48 85 DB                        test rbx, rbx
009C817B  0F 85 D3 00 00 00               jne 0x1409c8254
009C8181  33 DB                           xor ebx, ebx
009C8183  85 FF                           test edi, edi
009C8185  78 2E                           js 0x1409c81b5
009C8187  48 8B 8C 24 68 01 00 00         mov rcx, qword ptr [rsp + 0x168]
009C818F  48 8B 09                        mov rcx, qword ptr [rcx]
009C8192  48 8D 84 24 E8 00 00 00         lea rax, [rsp + 0xe8]
009C819A  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
009C819F  C6 44 24 28 01                  mov byte ptr [rsp + 0x28], 1
009C81A4  40 8A D6                        mov dl, sil
009C81A7  E8 28 F5 F5 FF                  call 0x1409276d4
009C81AC  8B F8                           mov edi, eax
009C81AE  89 84 24 C4 00 00 00            mov dword ptr [rsp + 0xc4], eax
009C81B5  4D 85 ED                        test r13, r13
009C81B8  74 40                           je 0x1409c81fa
009C81BA  85 FF                           test edi, edi
009C81BC  78 3C                           js 0x1409c81fa
009C81BE  49 8B 4D 00                     mov rcx, qword ptr [r13]
009C81C2  48 85 C9                        test rcx, rcx
009C81C5  74 33                           je 0x1409c81fa
009C81C7  48 8D 84 24 38 01 00 00         lea rax, [rsp + 0x138]
009C81CF  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
009C81D4  48 8D 84 24 F0 00 00 00         lea rax, [rsp + 0xf0]
009C81DC  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
009C81E1  C7 44 24 20 00 02 00 00         mov dword ptr [rsp + 0x20], 0x200
009C81E9  40 8A D6                        mov dl, sil
009C81EC  E8 67 E8 FF FF                  call 0x1409c6a58
009C81F1  8B F8                           mov edi, eax
009C81F3  89 84 24 C4 00 00 00            mov dword ptr [rsp + 0xc4], eax
009C81FA  48 8B 84 24 70 01 00 00         mov rax, qword ptr [rsp + 0x170]
009C8202  0F 10 00                        movups xmm0, xmmword ptr [rax]
009C8205  F3 0F 7F 84 24 C8 01 00 00      movdqu xmmword ptr [rsp + 0x1c8], xmm0
009C820E  4D 85 F6                        test r14, r14
009C8211  75 74                           jne 0x1409c8287
009C8213  4D 85 FF                        test r15, r15
009C8216  0F 85 B4 00 00 00               jne 0x1409c82d0
009C821C  4D 85 E4                        test r12, r12
009C821F  0F 85 EB 00 00 00               jne 0x1409c8310
009C8225  48 8B 84 24 C0 01 00 00         mov rax, qword ptr [rsp + 0x1c0]
009C822D  48 85 C0                        test rax, rax
009C8230  0F 84 1A 01 00 00               je 0x1409c8350
009C8236  85 FF                           test edi, edi
009C8238  0F 88 12 01 00 00               js 0x1409c8350
009C823E  8B 00                           mov eax, dword ptr [rax]
009C8240  89 84 24 D0 00 00 00            mov dword ptr [rsp + 0xd0], eax
009C8247  C6 84 24 C1 00 00 00 01         mov byte ptr [rsp + 0xc1], 1
009C824F  E9 FC 00 00 00                  jmp 0x1409c8350
009C8254  85 FF                           test edi, edi
009C8256  0F 88 25 FF FF FF               js 0x1409c8181
009C825C  48 8B 0B                        mov rcx, qword ptr [rbx]
009C825F  48 8D 84 24 28 01 00 00         lea rax, [rsp + 0x128]
009C8267  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
009C826C  C6 44 24 28 01                  mov byte ptr [rsp + 0x28], 1
009C8271  40 8A D6                        mov dl, sil
009C8274  E8 5B F4 F5 FF                  call 0x1409276d4
009C8279  8B F8                           mov edi, eax
009C827B  89 84 24 C4 00 00 00            mov dword ptr [rsp + 0xc4], eax
009C8282  E9 FA FE FF FF                  jmp 0x1409c8181
009C8287  85 FF                           test edi, edi
009C8289  78 88                           js 0x1409c8213
009C828B  41 8B 16                        mov edx, dword ptr [r14]
009C828E  89 94 24 D4 00 00 00            mov dword ptr [rsp + 0xd4], edx
009C8295  49 8D 4E 08                     lea rcx, [r14 + 8]
009C8299  48 8D 84 24 3C 01 00 00         lea rax, [rsp + 0x13c]
009C82A1  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
009C82A6  48 8D 84 24 F8 00 00 00         lea rax, [rsp + 0xf8]
009C82AE  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
009C82B3  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
009C82B7  45 33 C9                        xor r9d, r9d
009C82BA  44 8A C6                        mov r8b, sil
009C82BD  E8 AE 1A 00 00                  call 0x1409c9d70
009C82C2  8B F8                           mov edi, eax
009C82C4  89 84 24 C4 00 00 00            mov dword ptr [rsp + 0xc4], eax
009C82CB  E9 43 FF FF FF                  jmp 0x1409c8213
009C82D0  85 FF                           test edi, edi
009C82D2  0F 88 44 FF FF FF               js 0x1409c821c
009C82D8  48 8D 84 24 00 01 00 00         lea rax, [rsp + 0x100]
009C82E0  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009C82E5  88 5C 24 20                     mov byte ptr [rsp + 0x20], bl
009C82E9  44 8A CE                        mov r9b, sil
009C82EC  41 B8 01 00 00 00               mov r8d, 1
009C82F2  48 8D 94 24 CC 00 00 00         lea rdx, [rsp + 0xcc]
009C82FA  49 8B CF                        mov rcx, r15
009C82FD  E8 B6 9C FA FF                  call 0x140971fb8
009C8302  8B F8                           mov edi, eax
009C8304  89 84 24 C4 00 00 00            mov dword ptr [rsp + 0xc4], eax
009C830B  E9 0C FF FF FF                  jmp 0x1409c821c
009C8310  85 FF                           test edi, edi
009C8312  0F 88 0D FF FF FF               js 0x1409c8225
009C8318  48 8D 84 24 08 01 00 00         lea rax, [rsp + 0x108]
009C8320  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009C8325  88 5C 24 20                     mov byte ptr [rsp + 0x20], bl
009C8329  44 8A CE                        mov r9b, sil
009C832C  41 B8 01 00 00 00               mov r8d, 1
009C8332  48 8D 94 24 CC 00 00 00         lea rdx, [rsp + 0xcc]
009C833A  49 8B CC                        mov rcx, r12
009C833D  E8 76 9C FA FF                  call 0x140971fb8
009C8342  8B F8                           mov edi, eax
009C8344  89 84 24 C4 00 00 00            mov dword ptr [rsp + 0xc4], eax
009C834B  E9 D5 FE FF FF                  jmp 0x1409c8225
009C8350  E9 C6 00 00 00                  jmp 0x1409c841b
009C8355  8B F8                           mov edi, eax
009C8357  48 8B 8C 24 10 01 00 00         mov rcx, qword ptr [rsp + 0x110]
009C835F  8A 9C 24 C2 00 00 00            mov bl, byte ptr [rsp + 0xc2]
009C8366  48 85 C9                        test rcx, rcx
009C8369  74 07                           je 0x1409c8372
009C836B  8A D3                           mov dl, bl
009C836D  E8 CE F8 FF FF                  call 0x1409c7c40
009C8372  48 8B 8C 24 18 01 00 00         mov rcx, qword ptr [rsp + 0x118]
009C837A  48 85 C9                        test rcx, rcx
009C837D  74 07                           je 0x1409c8386
009C837F  8A D3                           mov dl, bl
009C8381  E8 BA F8 FF FF                  call 0x1409c7c40
009C8386  48 8B 8C 24 20 01 00 00         mov rcx, qword ptr [rsp + 0x120]
009C838E  48 85 C9                        test rcx, rcx
009C8391  74 07                           je 0x1409c839a
009C8393  8A D3                           mov dl, bl
009C8395  E8 A6 F8 FF FF                  call 0x1409c7c40
009C839A  48 8B 8C 24 28 01 00 00         mov rcx, qword ptr [rsp + 0x128]
009C83A2  48 85 C9                        test rcx, rcx
009C83A5  74 0A                           je 0x1409c83b1
009C83A7  41 B0 01                        mov r8b, 1
009C83AA  8A D3                           mov dl, bl
009C83AC  E8 9F 6B 06 00                  call 0x140a2ef50
009C83B1  48 8B 8C 24 E8 00 00 00         mov rcx, qword ptr [rsp + 0xe8]
009C83B9  48 85 C9                        test rcx, rcx
009C83BC  74 0A                           je 0x1409c83c8
009C83BE  41 B0 01                        mov r8b, 1
009C83C1  8A D3                           mov dl, bl
009C83C3  E8 88 6B 06 00                  call 0x140a2ef50
009C83C8  48 8B 8C 24 F0 00 00 00         mov rcx, qword ptr [rsp + 0xf0]
009C83D0  48 85 C9                        test rcx, rcx
009C83D3  74 07                           je 0x1409c83dc
009C83D5  8A D3                           mov dl, bl
009C83D7  E8 88 F8 FF FF                  call 0x1409c7c64
009C83DC  48 8B 8C 24 F8 00 00 00         mov rcx, qword ptr [rsp + 0xf8]
009C83E4  48 85 C9                        test rcx, rcx
009C83E7  74 07                           je 0x1409c83f0
009C83E9  8A D3                           mov dl, bl
009C83EB  E8 50 F8 FF FF                  call 0x1409c7c40
009C83F0  48 8B 8C 24 00 01 00 00         mov rcx, qword ptr [rsp + 0x100]
009C83F8  48 85 C9                        test rcx, rcx
009C83FB  74 05                           je 0x1409c8402
009C83FD  E8 22 4D 08 00                  call 0x140a4d124
009C8402  48 8B 8C 24 08 01 00 00         mov rcx, qword ptr [rsp + 0x108]
009C840A  48 85 C9                        test rcx, rcx
009C840D  74 05                           je 0x1409c8414
009C840F  E8 10 4D 08 00                  call 0x140a4d124
009C8414  8B C7                           mov eax, edi
009C8416  E9 C3 00 00 00                  jmp 0x1409c84de
009C841B  85 FF                           test edi, edi
009C841D  0F 89 08 01 00 00               jns 0x1409c852b
009C8423  48 8B 8C 24 10 01 00 00         mov rcx, qword ptr [rsp + 0x110]
009C842B  48 85 C9                        test rcx, rcx
009C842E  74 08                           je 0x1409c8438
009C8430  40 8A D6                        mov dl, sil
009C8433  E8 08 F8 FF FF                  call 0x1409c7c40
009C8438  48 8B 8C 24 18 01 00 00         mov rcx, qword ptr [rsp + 0x118]
009C8440  48 85 C9                        test rcx, rcx
009C8443  74 08                           je 0x1409c844d
009C8445  40 8A D6                        mov dl, sil
009C8448  E8 F3 F7 FF FF                  call 0x1409c7c40
009C844D  48 8B 8C 24 20 01 00 00         mov rcx, qword ptr [rsp + 0x120]
009C8455  48 85 C9                        test rcx, rcx
009C8458  74 08                           je 0x1409c8462
009C845A  40 8A D6                        mov dl, sil
009C845D  E8 DE F7 FF FF                  call 0x1409c7c40
009C8462  48 8B 8C 24 28 01 00 00         mov rcx, qword ptr [rsp + 0x128]
009C846A  48 85 C9                        test rcx, rcx
009C846D  74 0A                           je 0x1409c8479
009C846F  40 80 FE 01                     cmp sil, 1
009C8473  0F 86 92 00 00 00               jbe 0x1409c850b
009C8479  48 8B 8C 24 E8 00 00 00         mov rcx, qword ptr [rsp + 0xe8]
009C8481  48 85 C9                        test rcx, rcx
009C8484  74 06                           je 0x1409c848c
009C8486  40 80 FE 01                     cmp sil, 1
009C848A  76 76                           jbe 0x1409c8502
009C848C  48 8B 8C 24 F0 00 00 00         mov rcx, qword ptr [rsp + 0xf0]
009C8494  48 85 C9                        test rcx, rcx
009C8497  74 08                           je 0x1409c84a1
009C8499  40 8A D6                        mov dl, sil
009C849C  E8 C3 F7 FF FF                  call 0x1409c7c64
009C84A1  48 8B 8C 24 F8 00 00 00         mov rcx, qword ptr [rsp + 0xf8]
009C84A9  48 85 C9                        test rcx, rcx
009C84AC  0F 85 DD 01 00 00               jne 0x1409c868f
009C84B2  48 8B 8C 24 00 01 00 00         mov rcx, qword ptr [rsp + 0x100]
009C84BA  48 85 C9                        test rcx, rcx
009C84BD  0F 85 D9 01 00 00               jne 0x1409c869c
009C84C3  48 8B 8C 24 08 01 00 00         mov rcx, qword ptr [rsp + 0x108]
009C84CB  48 85 C9                        test rcx, rcx
009C84CE  0F 85 D2 01 00 00               jne 0x1409c86a6
009C84D4  85 FF                           test edi, edi
009C84D6  0F 89 8C 01 00 00               jns 0x1409c8668
009C84DC  8B C7                           mov eax, edi
009C84DE  48 8B 8C 24 D8 01 00 00         mov rcx, qword ptr [rsp + 0x1d8]
009C84E6  48 33 CC                        xor rcx, rsp
009C84E9  E8 52 41 CE FF                  call 0x1406ac640
009C84EE  48 81 C4 E0 01 00 00            add rsp, 0x1e0
009C84F5  41 5F                           pop r15
009C84F7  41 5E                           pop r14
009C84F9  41 5D                           pop r13
009C84FB  41 5C                           pop r12
009C84FD  5F                              pop rdi
009C84FE  5E                              pop rsi
009C84FF  5B                              pop rbx
009C8500  C3                              ret
009C8501  CC                              int3
009C8502  33 D2                           xor edx, edx
009C8504  E8 67 A3 1B 00                  call 0x140b82870
009C8509  EB 81                           jmp 0x1409c848c
009C850B  33 D2                           xor edx, edx
009C850D  E8 5E A3 1B 00                  call 0x140b82870
009C8512  E9 62 FF FF FF                  jmp 0x1409c8479
009C8517  38 8C 24 C0 00 00 00            cmp byte ptr [rsp + 0xc0], cl
009C851E  0F 85 2F FB FF FF               jne 0x1409c8053
009C8524  B8 A5 00 00 C0                  mov eax, 0xc00000a5
009C8529  EB B3                           jmp 0x1409c84de
009C852B  8A 84 24 C1 00 00 00            mov al, byte ptr [rsp + 0xc1]
009C8532  F6 D8                           neg al
009C8534  48 1B C9                        sbb rcx, rcx
009C8537  48 8D 84 24 D0 00 00 00         lea rax, [rsp + 0xd0]
009C853F  48 23 C8                        and rcx, rax
009C8542  88 9C 24 B8 00 00 00            mov byte ptr [rsp + 0xb8], bl
009C8549  48 89 8C 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rcx
009C8551  48 8B 84 24 F8 00 00 00         mov rax, qword ptr [rsp + 0xf8]
009C8559  48 89 84 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rax
009C8561  8B 84 24 D4 00 00 00            mov eax, dword ptr [rsp + 0xd4]
009C8568  89 84 24 A0 00 00 00            mov dword ptr [rsp + 0xa0], eax
009C856F  48 8B 84 24 08 01 00 00         mov rax, qword ptr [rsp + 0x108]
009C8577  48 89 84 24 98 00 00 00         mov qword ptr [rsp + 0x98], rax
009C857F  48 8B 84 24 00 01 00 00         mov rax, qword ptr [rsp + 0x100]
009C8587  48 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], rax
009C858F  48 8D 84 24 C8 01 00 00         lea rax, [rsp + 0x1c8]
009C8597  48 89 84 24 88 00 00 00         mov qword ptr [rsp + 0x88], rax
009C859F  48 8B 84 24 F0 00 00 00         mov rax, qword ptr [rsp + 0xf0]
009C85A7  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
009C85AF  48 8B 84 24 E8 00 00 00         mov rax, qword ptr [rsp + 0xe8]
009C85B7  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
009C85BC  48 8B 84 24 28 01 00 00         mov rax, qword ptr [rsp + 0x128]
009C85C4  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
009C85C9  48 8B 84 24 20 01 00 00         mov rax, qword ptr [rsp + 0x120]
009C85D1  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
009C85D6  8B 84 24 D8 00 00 00            mov eax, dword ptr [rsp + 0xd8]
009C85DD  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
009C85E1  8B 84 24 C8 00 00 00            mov eax, dword ptr [rsp + 0xc8]
009C85E8  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
009C85EC  48 8B 84 24 18 01 00 00         mov rax, qword ptr [rsp + 0x118]
009C85F4  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
009C85F9  8B 84 24 DC 00 00 00            mov eax, dword ptr [rsp + 0xdc]
009C8600  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
009C8604  48 8B 84 24 10 01 00 00         mov rax, qword ptr [rsp + 0x110]
009C860C  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
009C8611  48 8D 84 24 78 01 00 00         lea rax, [rsp + 0x178]
009C8619  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
009C861E  48 8D 84 24 80 01 00 00         lea rax, [rsp + 0x180]
009C8626  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
009C862B  8B 84 24 A4 01 00 00            mov eax, dword ptr [rsp + 0x1a4]
009C8632  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
009C8636  8B 84 24 E0 00 00 00            mov eax, dword ptr [rsp + 0xe0]
009C863D  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
009C8641  4C 8B 8C 24 88 01 00 00         mov r9, qword ptr [rsp + 0x188]
009C8649  44 8B 84 24 40 01 00 00         mov r8d, dword ptr [rsp + 0x140]
009C8651  40 8A D6                        mov dl, sil
009C8654  48 8D 8C 24 90 01 00 00         lea rcx, [rsp + 0x190]
009C865C  E8 6F 16 B2 FF                  call 0x1404e9cd0
009C8661  8B F8                           mov edi, eax
009C8663  E9 BB FD FF FF                  jmp 0x1409c8423
009C8668  48 8B 84 24 90 01 00 00         mov rax, qword ptr [rsp + 0x190]
009C8670  48 8B 8C 24 98 01 00 00         mov rcx, qword ptr [rsp + 0x198]
009C8678  48 89 01                        mov qword ptr [rcx], rax
009C867B  E9 5C FE FF FF                  jmp 0x1409c84dc
009C8680  E9 59 FE FF FF                  jmp 0x1409c84de
009C8685  B8 61 00 00 C0                  mov eax, 0xc0000061
009C868A  E9 4F FE FF FF                  jmp 0x1409c84de
009C868F  40 8A D6                        mov dl, sil
009C8692  E8 A9 F5 FF FF                  call 0x1409c7c40
009C8697  E9 16 FE FF FF                  jmp 0x1409c84b2
009C869C  E8 83 4A 08 00                  call 0x140a4d124
009C86A1  E9 1D FE FF FF                  jmp 0x1409c84c3
009C86A6  E8 79 4A 08 00                  call 0x140a4d124
009C86AB  E9 24 FE FF FF                  jmp 0x1409c84d4
009C86B0  B8 A8 00 00 C0                  mov eax, 0xc00000a8
009C86B5  E9 24 FE FF FF                  jmp 0x1409c84de
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NtCreateTokenEx(__int64 a1, int a2, __int64 a3, int a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, __int64 a12, __int64 a13, __int64 a14, __int64 a15, __int64 a16, __int64 a17)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned int v_stack_m138;
    unsigned int v_stack_m13C;
    unsigned int v_stack_m140;
    unsigned int v_stack_m144;
    unsigned int v_stack_m148;
    unsigned int v_stack_m14C;
    unsigned int v_stack_m150;
    unsigned int v_stack_m154;
    unsigned __int8 v_stack_m156;
    unsigned __int8 v_stack_m157;
    unsigned __int8 v_stack_m158;
    unsigned __int64 v_stack_m1D8;
    unsigned __int64 v_stack_m1E0;
    unsigned __int64 v_stack_m1E8;
    unsigned __int8 v_stack_m1F0;
    unsigned int v_stack_m1F8;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned int v_stack_mD8;
    unsigned int v_stack_mDC;
    unsigned int v_stack_mE0;
    unsigned int v_stack_mE4;
    unsigned int v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p100;
    unsigned __int64 v_stack_p108;
    unsigned __int64 v_stack_p110;
    unsigned __int64 v_stack_p118;
    unsigned __int64 v_stack_p120;
    unsigned __int64 v_stack_p128;
    unsigned int v_stack_p140;
    unsigned __int64 v_stack_p178;
    unsigned __int64 v_stack_p180;
    unsigned __int64 v_stack_p188;
    unsigned __int64 v_stack_p190;
    unsigned __int64 v_stack_p198;
    unsigned int v_stack_p1A4;
    unsigned __int64 v_stack_p1C8;
    unsigned int v_stack_p20;
    unsigned int v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned int v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned int v_stack_p58;
    unsigned int v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p78;
    unsigned __int64 v_stack_p80;
    unsigned __int64 v_stack_p88;
    unsigned __int64 v_stack_p90;
    unsigned __int64 v_stack_p98;
    unsigned int v_stack_pA0;
    unsigned __int64 v_stack_pA8;
    unsigned __int64 v_stack_pB0;
    unsigned __int8 v_stack_pB8;
    unsigned __int8 v_stack_pC0;
    unsigned __int8 v_stack_pC1;
    unsigned int v_stack_pC8;
    unsigned __int64 v_stack_pD0;
    unsigned int v_stack_pD4;
    unsigned int v_stack_pD8;
    unsigned int v_stack_pDC;
    unsigned int v_stack_pE0;
    unsigned __int64 v_stack_pE8;
    unsigned __int64 v_stack_pF0;
    unsigned __int64 v_stack_pF8;

    v_rsp = (v_rsp) - (480);
    result = (*(unsigned __int64 *)(v_rip + 4467364)) ^ (v_rsp);
    v_stack_m40 = result;
    v_stack_m138 = a4;
    v_stack_m90 = a3;
    v_stack_mD8 = a2;
    v_stack_m80 = a1;
    v_stack_m58 = a13;
    v_stack_mD0 = a5;
    v_stack_mB0 = a15;
    v_stack_m60 = a14;
    v_stack_mA8 = a17;
    v_stack_mB8 = a9;
    v_stack_mC0 = a8;
    v_stack_mC8 = a6;
    v_stack_m68 = a7;
    a1 = 0;
    v_stack_mE0 = 0;
    *(unsigned __int64 *)(v_rsp - 136) = 0;
    v_stack_m158 = 0;
    result = 0;
    *(unsigned __int64 *)(v_rsp - 120) = 0;
    *(unsigned int *)(v_rsp - 112) = 0;
    *(unsigned __int64 *)(v_rsp - 152) = 0;
    *(unsigned __int64 *)(v_rsp - 160) = 0;
    *(unsigned __int64 *)(v_rsp - 264) = 0;
    v_stack_mE8 = 0;
    v_stack_m13C = 0;
    *(unsigned __int64 *)(v_rsp - 256) = 0;
    v_stack_m150 = 0;
    v_stack_m140 = 0;
    *(unsigned __int64 *)(v_rsp - 248) = 0;
    v_stack_mE4 = 0;
    *(unsigned __int64 *)(v_rsp - 240) = 0;
    *(unsigned __int64 *)(v_rsp - 304) = 0;
    *(unsigned __int64 *)(v_rsp - 296) = 0;
    *(unsigned __int64 *)(v_rsp - 80) = v_xmm0;
    v_stack_m148 = 0;
    v_stack_m157 = 0;
    *(unsigned __int64 *)(v_rsp - 280) = 0;
    *(unsigned __int64 *)(v_rsp - 272) = 0;
    v_stack_m14C = 1;
    v_stack_m144 = 0;
    *(unsigned __int64 *)(v_rsp - 288) = 0;
    v_stack_mDC = 0;
    v_stack_m156 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 6364456), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_009C8685;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == 0) goto loc_009C800D;
    a1 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    if (v_stack_m80 < ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)))) { a1 = v_stack_m80; }
    *(unsigned __int64 *)(a1) = *(unsigned __int64 *)(a1);
    if (((3) & ((unsigned __int8)(v_stack_mC8))) == 0) goto loc_009C7F40;
loc_009C7EA6:
    result = ExRaiseDatatypeMisalignment(v_stack_mC8, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), 3, a4);
loc_009C7EAC:
    result = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    if (v_stack_mC8 < ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)))) { result = v_stack_mC8; }
    if (a14 == 0) goto loc_009C7ED0;
    if (((3) & ((unsigned __int8)(a14))) != 0) goto loc_009C7EA6;
    result = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    if (a14 < ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)))) { result = a14; }
loc_009C7ED0:
    if (((3) & ((unsigned __int8)(v_stack_mB0))) != 0) goto loc_009C7EA6;
    result = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    if (v_stack_mB0 < ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)))) { result = v_stack_mB0; }
    if (a16 == 0) goto loc_009C7F01;
    if (((3) & ((unsigned __int8)(a16))) != 0) goto loc_009C7EA6;
    result = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    if (a16 < ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)))) { result = a16; }
loc_009C7F01:
    if (((3) & ((unsigned __int8)(v_stack_mD0))) != 0) goto loc_009C7EA6;
    result = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    if (v_stack_mD0 < ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)))) { result = v_stack_mD0; }
    if (a13 != 0) goto loc_009C7F9F;
loc_009C7F20:
    if (a12 != 0) goto loc_009C7FBA;
loc_009C7F29:
    if (a11 != 0) goto loc_009C7FD5;
loc_009C7F32:
    if (a10 != 0) goto loc_009C7FF0;
loc_009C7F3B:
    goto loc_009C800D;
loc_009C7F40:
    result = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    if (v_stack_mD0 < ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)))) { result = v_stack_mD0; }
    if (((3) & ((unsigned __int8)(v_stack_mC0))) != 0) goto loc_009C7EA6;
    result = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    if (v_stack_mC0 < ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)))) { result = v_stack_mC0; }
    if (((3) & ((unsigned __int8)(v_stack_mB8))) != 0) goto loc_009C7EA6;
    result = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    if (v_stack_mB8 < ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)))) { result = v_stack_mB8; }
    if (((3) & ((unsigned __int8)(v_stack_mA8))) != 0) goto loc_009C7EA6;
    goto loc_009C7EAC;
loc_009C7F9F:
    if (((3) & ((unsigned __int8)(a13))) != 0) goto loc_009C7EA6;
    result = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    if (a13 < ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)))) { result = a13; }
    goto loc_009C7F20;
loc_009C7FBA:
    if (((3) & ((unsigned __int8)(a12))) != 0) goto loc_009C7EA6;
    result = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    if (a12 < ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)))) { result = a12; }
    goto loc_009C7F29;
loc_009C7FD5:
    if (((3) & ((unsigned __int8)(a11))) != 0) goto loc_009C7EA6;
    result = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    if (a11 < ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)))) { result = a11; }
    goto loc_009C7F32;
loc_009C7FF0:
    if (((3) & ((unsigned __int8)(a10))) != 0) goto loc_009C7EA6;
    a2 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    if (a10 < ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)))) { a2 = a10; }
    goto loc_009C7F3B;
loc_009C800D:
    if (((unsigned int)((unsigned int)(v_stack_m138) - 1)) > 1) goto loc_009C86B0;
    result = SeCaptureSecurityQos(v_stack_m90, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), v_stack_m158, v_stack_m78);
    a1 = 0;
    if (sign_flag) goto loc_009C84DE;
    if (((unsigned int)((unsigned int)(v_stack_m138))) == 2) goto loc_009C8517;
loc_009C8053:
    v_stack_m154 = 0;
    v_stack_m98 = *(unsigned __int64 *)(v_stack_mD0);
    v_stack_mA0 = *(unsigned __int64 *)(v_stack_mC8);
    v_stack_m1D8 = v_stack_mE8;
    v_stack_m1E0 = v_stack_m108;
    v_stack_m1F8 = 0;
    a4 = 0;
    result = SeCaptureSidAndAttributesArray(v_stack_m68, a4 + 1, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), a4);
    v_stack_m154 = (unsigned int)(result);
    v_rbx = a14;
    v_rdi = (unsigned int)((unsigned int)(result));
    if (!(sign_flag)) {
        result = v_stack_mC0;
        v_rbx = *(unsigned int *)(result);
        v_stack_m13C = (unsigned int)(v_rbx);
        a1 = result + 8;
        result = v_stack_m150;
        v_stack_m1D8 = result;
        result = v_stack_m100;
        v_stack_m1E0 = result;
        a4 = 0;
        a3 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
        a2 = (unsigned int)(v_rbx);
        result = SeCaptureSidAndAttributesArray(a1, a2, a3, a4);
        v_rdi = (unsigned int)(result);
        v_stack_m154 = (unsigned int)(result);
        v_rbx = (unsigned int)((v_rbx) << (4));
        result = v_stack_m150;
        result = (unsigned int)((result) - ((unsigned int)(v_rbx)));
        v_stack_m150 = (unsigned int)(result);
        result = (unsigned int)((result) + (3));
        result = (unsigned int)((result) & (0xFFFFFFFCULL));
        v_stack_m150 = (unsigned int)(result);
        v_rbx = v_stack_m60;
    }
    if (!(sign_flag)) {
        result = v_stack_mB8;
        a2 = *(unsigned int *)(result);
        v_stack_m140 = a2;
        a1 = result + 4;
        result = v_stack_mE4;
        v_stack_m1D8 = result;
        result = v_stack_mF8;
        v_stack_m1E0 = result;
        a3 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
        result = SeCaptureLuidAndAttributesArray(a1, a2, a3, a4);
        v_rdi = (unsigned int)(result);
        v_stack_m154 = (unsigned int)(result);
    }
    if (v_rbx != 0) goto loc_009C8254;
loc_009C8181:
    v_rbx = 0;
    if (!(sign_flag)) {
        a1 = v_stack_mB0;
        a1 = *(unsigned __int64 *)(a1);
        result = v_stack_m130;
        v_stack_m1E8 = result;
        v_stack_m1F0 = 1;
        a2 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
        result = SeCaptureSid(a1, a2, a3, a4);
        v_rdi = (unsigned int)(result);
        v_stack_m154 = (unsigned int)(result);
    }
    if (a16 == 0) goto loc_009C81FA;
    if (sign_flag) goto loc_009C81FA;
    if (*(unsigned __int64 *)(a16) != 0) {
        result = v_stack_mE0;
        v_stack_m1E0 = result;
        result = v_stack_m128;
        v_stack_m1E8 = result;
        v_stack_m1F8 = 512;
        a2 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
        result = SeCaptureAcl(*(unsigned __int64 *)(a16), a2, a3, a4);
        v_rdi = (unsigned int)(result);
        v_stack_m154 = (unsigned int)(result);
    }
    v_stack_m50 = v_xmm0;
    if (a12 != 0) goto loc_009C8287;
loc_009C8213:
    if (a10 != 0) goto loc_009C82D0;
loc_009C821C:
    if (a11 != 0) goto loc_009C8310;
loc_009C8225:
    if (v_stack_m58 == 0) goto loc_009C8350;
    if (sign_flag) goto loc_009C8350;
    v_stack_m148 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m58)));
    v_stack_m157 = 1;
    goto loc_009C8350;
loc_009C8254:
    if (sign_flag) goto loc_009C8181;
    v_stack_m1E8 = v_stack_mF0;
    v_stack_m1F0 = 1;
    result = SeCaptureSid(*(unsigned __int64 *)(v_rbx), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), a3, a4);
    v_stack_m154 = (unsigned int)(result);
    goto loc_009C8181;
loc_009C8287:
    if (sign_flag) goto loc_009C8213;
    v_stack_m144 = (unsigned int)((unsigned int)(*(unsigned int *)(a12)));
    v_stack_m1D8 = v_stack_mDC;
    v_stack_m1E0 = v_stack_m120;
    v_stack_m1F8 = 0;
    a4 = 0;
    result = SeCaptureSidAndAttributesArray(a12 + 8, (unsigned int)(*(unsigned int *)(a12)), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), a4);
    v_stack_m154 = (unsigned int)(result);
    goto loc_009C8213;
loc_009C82D0:
    if (sign_flag) goto loc_009C821C;
    v_stack_m1F0 = v_stack_m118;
    v_stack_m1F8 = 0;
    result = SepCaptureTokenSecurityAttributesInformation(a10, v_stack_m14C, 1, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    v_stack_m154 = (unsigned int)(result);
    goto loc_009C821C;
loc_009C8310:
    if (sign_flag) goto loc_009C8225;
    v_stack_m1F0 = v_stack_m110;
    v_stack_m1F8 = 0;
    result = SepCaptureTokenSecurityAttributesInformation(a11, v_stack_m14C, 1, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    v_stack_m154 = (unsigned int)(result);
    goto loc_009C8225;
loc_009C8350:
    goto loc_009C841B;
loc_009C841B:
    if (!sign_flag) goto loc_009C852B;
loc_009C8423:
    if (v_stack_m108 != 0) {
        a2 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
        result = SeReleaseLuidAndAttributesArray(v_stack_m108, a2, 1, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    }
    if (v_stack_m100 != 0) {
        a2 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
        result = SeReleaseLuidAndAttributesArray(v_stack_m100, a2, 1, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    }
    if (v_stack_mF8 != 0) {
        a2 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
        result = SeReleaseLuidAndAttributesArray(v_stack_mF8, a2, 1, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    }
    if (v_stack_mF0 == 0) goto loc_009C8479;
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562))) <= 1) goto loc_009C850B;
loc_009C8479:
    if (v_stack_m130 == 0) goto loc_009C848C;
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562))) <= 1) goto loc_009C8502;
loc_009C848C:
    if (v_stack_m128 != 0) {
        a2 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
        result = SeReleaseAcl(v_stack_m128, a2, 1, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    }
    if (v_stack_m120 != 0) goto loc_009C868F;
loc_009C84B2:
    if (v_stack_m118 != 0) goto loc_009C869C;
loc_009C84C3:
    if (v_stack_m110 != 0) goto loc_009C86A6;
loc_009C84D4:
    if (!sign_flag) goto loc_009C8668;
loc_009C84DC:
loc_009C84DE:
    a1 = (v_stack_m40) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, 1, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    v_rsp = (v_rsp) + (480);
    return result;
loc_009C8502:
    a2 = 0;
    result = ExFreePoolWithTag(a1, a2, 1, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    goto loc_009C848C;
loc_009C850B:
    a2 = 0;
    result = ExFreePoolWithTag(a1, a2, 1, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    goto loc_009C8479;
loc_009C8517:
    if (v_stack_pC0 != ((unsigned __int8)(a1))) goto loc_009C8053;
    goto loc_009C84DE;
loc_009C852B:
    result = (unsigned __int8)(-(v_stack_pC1));
    a1 = (a1) & (v_stack_pD0);
    v_stack_pB8 = 0;
    v_stack_pB0 = a1;
    v_stack_pA8 = v_stack_pF8;
    v_stack_pA0 = (unsigned int)((unsigned int)(v_stack_pD4));
    v_stack_p98 = v_stack_p108;
    v_stack_p90 = v_stack_p100;
    v_stack_p88 = v_stack_p1C8;
    v_stack_p80 = v_stack_pF0;
    v_stack_p78 = v_stack_pE8;
    v_stack_p70 = v_stack_p128;
    v_stack_p68 = v_stack_p120;
    v_stack_p60 = (unsigned int)((unsigned int)(v_stack_pD8));
    v_stack_p58 = (unsigned int)((unsigned int)(v_stack_pC8));
    v_stack_p50 = v_stack_p118;
    v_stack_p48 = (unsigned int)((unsigned int)(v_stack_pDC));
    v_stack_p40 = v_stack_p110;
    v_stack_p38 = v_stack_p178;
    v_stack_p30 = v_stack_p180;
    v_stack_p28 = (unsigned int)((unsigned int)(v_stack_p1A4));
    v_stack_p20 = (unsigned int)((unsigned int)(v_stack_pE0));
    result = SepCreateTokenEx(v_stack_p190, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), (unsigned int)(v_stack_p140), v_stack_p188);
    goto loc_009C8423;
loc_009C8668:
    *(unsigned __int64 *)(v_stack_p198) = v_stack_p190;
    goto loc_009C84DC;
loc_009C8685:
    goto loc_009C84DE;
loc_009C868F:
    result = SeReleaseLuidAndAttributesArray(v_stack_p198, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), (unsigned int)(v_stack_p140), v_stack_p188);
    goto loc_009C84B2;
loc_009C869C:
    result = SepFreeCapturedTokenSecurityAttributesInformation(v_stack_p198, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), (unsigned int)(v_stack_p140), v_stack_p188);
    goto loc_009C84C3;
loc_009C86A6:
    result = SepFreeCapturedTokenSecurityAttributesInformation(v_stack_p198, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), (unsigned int)(v_stack_p140), v_stack_p188);
    goto loc_009C84D4;
loc_009C86B0:
    goto loc_009C84DE;
}
```

## 5. (Beta) C Style

```c
int64_t NtCreateTokenEx(int64_t Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4, int64_t Arg5, int64_t Arg6, int64_t Arg7, int64_t Arg8, int64_t Arg9, int64_t Arg10, int64_t Arg11, int64_t Arg12, int64_t Arg13, int64_t Arg14, int64_t Arg15, int64_t Arg16, int64_t Arg17)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint64_t v_stack_m130;
    uint32_t v_stack_m138;
    uint32_t v_stack_m13C;
    uint32_t v_stack_m140;
    uint32_t v_stack_m144;
    uint32_t v_stack_m148;
    uint32_t v_stack_m14C;
    uint32_t v_stack_m150;
    uint32_t v_stack_m154;
    uint8_t v_stack_m156;
    uint8_t v_stack_m157;
    uint8_t v_stack_m158;
    uint64_t v_stack_m1D8;
    uint64_t v_stack_m1E0;
    uint64_t v_stack_m1E8;
    uint8_t v_stack_m1F0;
    uint32_t v_stack_m1F8;
    uint64_t v_stack_m40;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint32_t v_stack_mD8;
    uint32_t v_stack_mDC;
    uint32_t v_stack_mE0;
    uint32_t v_stack_mE4;
    uint32_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p100;
    uint64_t v_stack_p108;
    uint64_t v_stack_p110;
    uint64_t v_stack_p118;
    uint64_t v_stack_p120;
    uint64_t v_stack_p128;
    uint32_t v_stack_p140;
    uint64_t v_stack_p178;
    uint64_t v_stack_p180;
    uint64_t v_stack_p188;
    uint64_t v_stack_p190;
    uint64_t v_stack_p198;
    uint32_t v_stack_p1A4;
    uint64_t v_stack_p1C8;
    uint32_t v_stack_p20;
    uint32_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint32_t v_stack_p48;
    uint64_t v_stack_p50;
    uint32_t v_stack_p58;
    uint32_t v_stack_p60;
    uint64_t v_stack_p68;
    uint64_t v_stack_p70;
    uint64_t v_stack_p78;
    uint64_t v_stack_p80;
    uint64_t v_stack_p88;
    uint64_t v_stack_p90;
    uint64_t v_stack_p98;
    uint32_t v_stack_pA0;
    uint64_t v_stack_pA8;
    uint64_t v_stack_pB0;
    uint8_t v_stack_pB8;
    uint8_t v_stack_pC0;
    uint8_t v_stack_pC1;
    uint32_t v_stack_pC8;
    uint64_t v_stack_pD0;
    uint32_t v_stack_pD4;
    uint32_t v_stack_pD8;
    uint32_t v_stack_pDC;
    uint32_t v_stack_pE0;
    uint64_t v_stack_pE8;
    uint64_t v_stack_pF0;
    uint64_t v_stack_pF8;

    local_rsp = (local_rsp) - (480);
    result = (*(uint64_t *)(v_rip + 0x442AA4)) ^ (local_rsp);
    v_stack_m40 = result;
    v_stack_m138 = Arg4;
    v_stack_m90 = Arg3;
    v_stack_mD8 = Arg2;
    v_stack_m80 = Arg1;
    v_stack_m58 = Arg13;
    v_stack_mD0 = Arg5;
    v_stack_mB0 = Arg15;
    v_stack_m60 = Arg14;
    v_stack_mA8 = Arg17;
    v_stack_mB8 = Arg9;
    v_stack_mC0 = Arg8;
    v_stack_mC8 = Arg6;
    v_stack_m68 = Arg7;
    Arg1 = 0;
    v_stack_mE0 = 0;
    *(uint64_t *)(local_rsp - 0x88) = 0;
    v_stack_m158 = 0;
    result = 0;
    *(uint64_t *)(local_rsp - 0x78) = 0;
    *(uint32_t *)(local_rsp - 0x70) = 0;
    *(uint64_t *)(local_rsp - 0x98) = 0;
    *(uint64_t *)(local_rsp - 0xA0) = 0;
    *(uint64_t *)(local_rsp - 0x108) = 0;
    v_stack_mE8 = 0;
    v_stack_m13C = 0;
    *(uint64_t *)(local_rsp - 0x100) = 0;
    v_stack_m150 = 0;
    v_stack_m140 = 0;
    *(uint64_t *)(local_rsp - 0xF8) = 0;
    v_stack_mE4 = 0;
    *(uint64_t *)(local_rsp - 0xF0) = 0;
    *(uint64_t *)(local_rsp - 0x130) = 0;
    *(uint64_t *)(local_rsp - 0x128) = 0;
    *(uint64_t *)(local_rsp - 0x50) = v_xmm0;
    v_stack_m148 = 0;
    v_stack_m157 = 0;
    *(uint64_t *)(local_rsp - 0x118) = 0;
    *(uint64_t *)(local_rsp - 0x110) = 0;
    v_stack_m14C = 1;
    v_stack_m144 = 0;
    *(uint64_t *)(local_rsp - 0x120) = 0;
    v_stack_mDC = 0;
    v_stack_m156 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x611D28), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_009C8685;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == 0) goto loc_009C800D;
    Arg1 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    if (v_stack_m80 < ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)))) { Arg1 = v_stack_m80; }
    *(uint64_t *)(Arg1) = *(uint64_t *)(Arg1);
    if (((3) & ((uint8_t)(v_stack_mC8))) == 0) goto loc_009C7F40;
loc_009C7EA6:
    result = ExRaiseDatatypeMisalignment(v_stack_mC8, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), 3, Arg4);
loc_009C7EAC:
    result = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    if (v_stack_mC8 < ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)))) { result = v_stack_mC8; }
    if (Arg14 == 0) goto loc_009C7ED0;
    if (((3) & ((uint8_t)(Arg14))) != 0) goto loc_009C7EA6;
    result = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    if (Arg14 < ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)))) { result = Arg14; }
loc_009C7ED0:
    if (((3) & ((uint8_t)(v_stack_mB0))) != 0) goto loc_009C7EA6;
    result = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    if (v_stack_mB0 < ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)))) { result = v_stack_mB0; }
    if (Arg16 == 0) goto loc_009C7F01;
    if (((3) & ((uint8_t)(Arg16))) != 0) goto loc_009C7EA6;
    result = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    if (Arg16 < ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)))) { result = Arg16; }
loc_009C7F01:
    if (((3) & ((uint8_t)(v_stack_mD0))) != 0) goto loc_009C7EA6;
    result = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    if (v_stack_mD0 < ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)))) { result = v_stack_mD0; }
    if (Arg13 != 0) goto loc_009C7F9F;
loc_009C7F20:
    if (Arg12 != 0) goto loc_009C7FBA;
loc_009C7F29:
    if (Arg11 != 0) goto loc_009C7FD5;
loc_009C7F32:
    if (Arg10 != 0) goto loc_009C7FF0;
loc_009C7F3B:
    goto loc_009C800D;
loc_009C7F40:
    result = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    if (v_stack_mD0 < ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)))) { result = v_stack_mD0; }
    if (((3) & ((uint8_t)(v_stack_mC0))) != 0) goto loc_009C7EA6;
    result = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    if (v_stack_mC0 < ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)))) { result = v_stack_mC0; }
    if (((3) & ((uint8_t)(v_stack_mB8))) != 0) goto loc_009C7EA6;
    result = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    if (v_stack_mB8 < ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)))) { result = v_stack_mB8; }
    if (((3) & ((uint8_t)(v_stack_mA8))) != 0) goto loc_009C7EA6;
    goto loc_009C7EAC;
loc_009C7F9F:
    if (((3) & ((uint8_t)(Arg13))) != 0) goto loc_009C7EA6;
    result = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    if (Arg13 < ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)))) { result = Arg13; }
    goto loc_009C7F20;
loc_009C7FBA:
    if (((3) & ((uint8_t)(Arg12))) != 0) goto loc_009C7EA6;
    result = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    if (Arg12 < ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)))) { result = Arg12; }
    goto loc_009C7F29;
loc_009C7FD5:
    if (((3) & ((uint8_t)(Arg11))) != 0) goto loc_009C7EA6;
    result = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    if (Arg11 < ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)))) { result = Arg11; }
    goto loc_009C7F32;
loc_009C7FF0:
    if (((3) & ((uint8_t)(Arg10))) != 0) goto loc_009C7EA6;
    Arg2 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    if (Arg10 < ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)))) { Arg2 = Arg10; }
    goto loc_009C7F3B;
loc_009C800D:
    if (((uint32_t)((uint32_t)(v_stack_m138) - 1)) > 1) goto loc_009C86B0;
    result = SeCaptureSecurityQos(v_stack_m90, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), v_stack_m158, v_stack_m78);
    Arg1 = 0;
    if (sign_flag) goto loc_009C84DE;
    if (((uint32_t)((uint32_t)(v_stack_m138))) == 2) goto loc_009C8517;
loc_009C8053:
    v_stack_m154 = 0;
    v_stack_m98 = *(uint64_t *)(v_stack_mD0);
    v_stack_mA0 = *(uint64_t *)(v_stack_mC8);
    v_stack_m1D8 = v_stack_mE8;
    v_stack_m1E0 = v_stack_m108;
    v_stack_m1F8 = 0;
    Arg4 = 0;
    result = SeCaptureSidAndAttributesArray(v_stack_m68, Arg4 + 1, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), Arg4);
    v_stack_m154 = (uint32_t)(result);
    local_rbx = Arg14;
    local_rdi = (uint32_t)((uint32_t)(result));
    if (!(sign_flag)) {
        result = v_stack_mC0;
        local_rbx = *(uint32_t *)(result);
        v_stack_m13C = (uint32_t)(local_rbx);
        Arg1 = result + 8;
        result = v_stack_m150;
        v_stack_m1D8 = result;
        result = v_stack_m100;
        v_stack_m1E0 = result;
        Arg4 = 0;
        Arg3 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
        Arg2 = (uint32_t)(local_rbx);
        result = SeCaptureSidAndAttributesArray(Arg1, Arg2, Arg3, Arg4);
        local_rdi = (uint32_t)(result);
        v_stack_m154 = (uint32_t)(result);
        local_rbx = (uint32_t)((local_rbx) << (4));
        result = v_stack_m150;
        result = (uint32_t)((result) - ((uint32_t)(local_rbx)));
        v_stack_m150 = (uint32_t)(result);
        result = (uint32_t)((result) + (3));
        result = (uint32_t)((result) & (0xFFFFFFFCULL));
        v_stack_m150 = (uint32_t)(result);
        local_rbx = v_stack_m60;
    }
    if (!(sign_flag)) {
        result = v_stack_mB8;
        Arg2 = *(uint32_t *)(result);
        v_stack_m140 = Arg2;
        Arg1 = result + 4;
        result = v_stack_mE4;
        v_stack_m1D8 = result;
        result = v_stack_mF8;
        v_stack_m1E0 = result;
        Arg3 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
        result = SeCaptureLuidAndAttributesArray(Arg1, Arg2, Arg3, Arg4);
        local_rdi = (uint32_t)(result);
        v_stack_m154 = (uint32_t)(result);
    }
    if (local_rbx != 0) goto loc_009C8254;
loc_009C8181:
    local_rbx = 0;
    if (!(sign_flag)) {
        Arg1 = v_stack_mB0;
        Arg1 = *(uint64_t *)(Arg1);
        result = v_stack_m130;
        v_stack_m1E8 = result;
        v_stack_m1F0 = 1;
        Arg2 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
        result = SeCaptureSid(Arg1, Arg2, Arg3, Arg4);
        local_rdi = (uint32_t)(result);
        v_stack_m154 = (uint32_t)(result);
    }
    if (Arg16 == 0) goto loc_009C81FA;
    if (sign_flag) goto loc_009C81FA;
    if (*(uint64_t *)(Arg16) != 0) {
        result = v_stack_mE0;
        v_stack_m1E0 = result;
        result = v_stack_m128;
        v_stack_m1E8 = result;
        v_stack_m1F8 = 512;
        Arg2 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
        result = SeCaptureAcl(*(uint64_t *)(Arg16), Arg2, Arg3, Arg4);
        local_rdi = (uint32_t)(result);
        v_stack_m154 = (uint32_t)(result);
    }
    v_stack_m50 = v_xmm0;
    if (Arg12 != 0) goto loc_009C8287;
loc_009C8213:
    if (Arg10 != 0) goto loc_009C82D0;
loc_009C821C:
    if (Arg11 != 0) goto loc_009C8310;
loc_009C8225:
    if (v_stack_m58 == 0) goto loc_009C8350;
    if (sign_flag) goto loc_009C8350;
    v_stack_m148 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m58)));
    v_stack_m157 = 1;
    goto loc_009C8350;
loc_009C8254:
    if (sign_flag) goto loc_009C8181;
    v_stack_m1E8 = v_stack_mF0;
    v_stack_m1F0 = 1;
    result = SeCaptureSid(*(uint64_t *)(local_rbx), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), Arg3, Arg4);
    v_stack_m154 = (uint32_t)(result);
    goto loc_009C8181;
loc_009C8287:
    if (sign_flag) goto loc_009C8213;
    v_stack_m144 = (uint32_t)((uint32_t)(*(uint32_t *)(Arg12)));
    v_stack_m1D8 = v_stack_mDC;
    v_stack_m1E0 = v_stack_m120;
    v_stack_m1F8 = 0;
    Arg4 = 0;
    result = SeCaptureSidAndAttributesArray(Arg12 + 8, (uint32_t)(*(uint32_t *)(Arg12)), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), Arg4);
    v_stack_m154 = (uint32_t)(result);
    goto loc_009C8213;
loc_009C82D0:
    if (sign_flag) goto loc_009C821C;
    v_stack_m1F0 = v_stack_m118;
    v_stack_m1F8 = 0;
    result = SepCaptureTokenSecurityAttributesInformation(Arg10, v_stack_m14C, 1, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    v_stack_m154 = (uint32_t)(result);
    goto loc_009C821C;
loc_009C8310:
    if (sign_flag) goto loc_009C8225;
    v_stack_m1F0 = v_stack_m110;
    v_stack_m1F8 = 0;
    result = SepCaptureTokenSecurityAttributesInformation(Arg11, v_stack_m14C, 1, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    v_stack_m154 = (uint32_t)(result);
    goto loc_009C8225;
loc_009C8350:
    goto loc_009C841B;
loc_009C841B:
    if (!sign_flag) goto loc_009C852B;
loc_009C8423:
    if (v_stack_m108 != 0) {
        Arg2 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
        result = SeReleaseLuidAndAttributesArray(v_stack_m108, Arg2, 1, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    }
    if (v_stack_m100 != 0) {
        Arg2 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
        result = SeReleaseLuidAndAttributesArray(v_stack_m100, Arg2, 1, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    }
    if (v_stack_mF8 != 0) {
        Arg2 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
        result = SeReleaseLuidAndAttributesArray(v_stack_mF8, Arg2, 1, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    }
    if (v_stack_mF0 == 0) goto loc_009C8479;
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232))) <= 1) goto loc_009C850B;
loc_009C8479:
    if (v_stack_m130 == 0) goto loc_009C848C;
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232))) <= 1) goto loc_009C8502;
loc_009C848C:
    if (v_stack_m128 != 0) {
        Arg2 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
        result = SeReleaseAcl(v_stack_m128, Arg2, 1, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    }
    if (v_stack_m120 != 0) goto loc_009C868F;
loc_009C84B2:
    if (v_stack_m118 != 0) goto loc_009C869C;
loc_009C84C3:
    if (v_stack_m110 != 0) goto loc_009C86A6;
loc_009C84D4:
    if (!sign_flag) goto loc_009C8668;
loc_009C84DC:
loc_009C84DE:
    Arg1 = (v_stack_m40) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, 1, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    local_rsp = (local_rsp) + (480);
    return result;
loc_009C8502:
    Arg2 = 0;
    result = ExFreePoolWithTag(Arg1, Arg2, 1, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    goto loc_009C848C;
loc_009C850B:
    Arg2 = 0;
    result = ExFreePoolWithTag(Arg1, Arg2, 1, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    goto loc_009C8479;
loc_009C8517:
    if (v_stack_pC0 != ((uint8_t)(Arg1))) goto loc_009C8053;
    goto loc_009C84DE;
loc_009C852B:
    result = (uint8_t)(-(v_stack_pC1));
    Arg1 = (Arg1) & (v_stack_pD0);
    v_stack_pB8 = 0;
    v_stack_pB0 = Arg1;
    v_stack_pA8 = v_stack_pF8;
    v_stack_pA0 = (uint32_t)((uint32_t)(v_stack_pD4));
    v_stack_p98 = v_stack_p108;
    v_stack_p90 = v_stack_p100;
    v_stack_p88 = v_stack_p1C8;
    v_stack_p80 = v_stack_pF0;
    v_stack_p78 = v_stack_pE8;
    v_stack_p70 = v_stack_p128;
    v_stack_p68 = v_stack_p120;
    v_stack_p60 = (uint32_t)((uint32_t)(v_stack_pD8));
    v_stack_p58 = (uint32_t)((uint32_t)(v_stack_pC8));
    v_stack_p50 = v_stack_p118;
    v_stack_p48 = (uint32_t)((uint32_t)(v_stack_pDC));
    v_stack_p40 = v_stack_p110;
    v_stack_p38 = v_stack_p178;
    v_stack_p30 = v_stack_p180;
    v_stack_p28 = (uint32_t)((uint32_t)(v_stack_p1A4));
    v_stack_p20 = (uint32_t)((uint32_t)(v_stack_pE0));
    result = SepCreateTokenEx(v_stack_p190, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), (uint32_t)(v_stack_p140), v_stack_p188);
    goto loc_009C8423;
loc_009C8668:
    *(uint64_t *)(v_stack_p198) = v_stack_p190;
    goto loc_009C84DC;
loc_009C8685:
    goto loc_009C84DE;
loc_009C868F:
    result = SeReleaseLuidAndAttributesArray(v_stack_p198, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), (uint32_t)(v_stack_p140), v_stack_p188);
    goto loc_009C84B2;
loc_009C869C:
    result = SepFreeCapturedTokenSecurityAttributesInformation(v_stack_p198, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), (uint32_t)(v_stack_p140), v_stack_p188);
    goto loc_009C84C3;
loc_009C86A6:
    result = SepFreeCapturedTokenSecurityAttributesInformation(v_stack_p198, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), (uint32_t)(v_stack_p140), v_stack_p188);
    goto loc_009C84D4;
loc_009C86B0:
    goto loc_009C84DE;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009C7C80&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
