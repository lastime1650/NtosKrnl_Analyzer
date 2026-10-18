# SeCaptureSidAndAttributesArray

- RVA: `0x009C9D70`–`0x009CA216` (길이 `1,190` bytes)
- VA: `0x00000001409C9D70`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A0A94`
- 디코드: `320`개 명령, `1,190/1,190` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **19**; 고유 호출 대상: **7**
- 직접 호출자로 확인된 함수: **11**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x009C9E6F` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x009C9EA4` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x009C9ED0` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x009C9F08` → [ExAllocatePoolWithTag](../../poolcode/B8/ExAllocatePoolWithTag_function_00B82010.md) (function, `0x00B82010`)
- `0x009C9F57` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x009C9FA7` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x009C9FDA` → [RtlValidSid](../92/RtlValidSid_function_00929710.md) (function, `0x00929710`)
- `0x009C9FE6` → [RtlLengthSid](../../text/45/RtlLengthSid_function_0045D270.md) (function, `0x0045D270`)
- `0x009CA02E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x009CA041` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x009CA05B` → [ExAllocatePoolWithTag](../../poolcode/B8/ExAllocatePoolWithTag_function_00B82010.md) (function, `0x00B82010`)
- `0x009CA0D8` → [RtlLengthRequiredSid](RtlLengthRequiredSid_function_009CA4D0.md) (function, `0x009CA4D0`)
- `0x009CA143` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x009CA155` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x009CA16B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x009CA19F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x009CA1B6` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x009CA1FB` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x009CA20C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [SeSetTokenTamperProtection](../../text/60/SeSetTokenTamperProtection_function_00609644.md) at `0x00609906`
- [NtAdjustGroupsToken](NtAdjustGroupsToken_function_009C6640.md) at `0x009C6753`
- [NtFilterToken](NtFilterToken_function_009C7890.md) at `0x009C79F0`
- [NtFilterToken](NtFilterToken_function_009C7890.md) at `0x009C7A5C`
- [NtCreateTokenEx](NtCreateTokenEx_function_009C7C80.md) at `0x009C80B0`
- [NtCreateTokenEx](NtCreateTokenEx_function_009C7C80.md) at `0x009C80FE`
- [NtCreateTokenEx](NtCreateTokenEx_function_009C7C80.md) at `0x009C82BD`
- [SepSetTokenCapabilities](SepSetTokenCapabilities_function_009C9AF4.md) at `0x009C9BBA`
- [SepLengthSidAndAttributesArray](SepLengthSidAndAttributesArray_function_009C9CB8.md) at `0x009C9D21`
- [PspBuildCreateProcessContext](../9E/PspBuildCreateProcessContext_function_009ED6E0.md) at `0x009EE7DD`
- [NtCreateLowBoxToken](../AB/NtCreateLowBoxToken_function_00AB9880.md) at `0x00AB9A58`
- [NtCreateLowBoxToken](../AB/NtCreateLowBoxToken_function_00AB9880.md) at `0x00AB9DA8`
- [NtSetInformationToken](../AF/NtSetInformationToken_function_00AF0530.md) at `0x00AF1921`
- [sub_00B3F630](../B3/Unknown_function_00B3F630.md) at `0x00B3F736`
- [sub_00B412E4](../B4/Unknown_function_00B412E4.md) at `0x00B41378`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **15**
  - `0x009C9E6F` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x009C9EA4` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x009C9ED0` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x009C9F08` → [ExAllocatePoolWithTag](../../poolcode/B8/ExAllocatePoolWithTag_function_00B82010.md) (`PAGE` → `POOLCODE`)
  - `0x009C9F57` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x009C9FA7` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x009C9FE6` → [RtlLengthSid](../../text/45/RtlLengthSid_function_0045D270.md) (`PAGE` → `.text`)
  - `0x009CA02E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x009CA041` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x009CA05B` → [ExAllocatePoolWithTag](../../poolcode/B8/ExAllocatePoolWithTag_function_00B82010.md) (`PAGE` → `POOLCODE`)
  - `0x009CA16B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x009CA19F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x009CA1B6` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x009CA1FB` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x009CA20C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009C9D70  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
009C9D75  44 88 44 24 18                  mov byte ptr [rsp + 0x18], r8b
009C9D7A  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
009C9D7F  53                              push rbx
009C9D80  56                              push rsi
009C9D81  57                              push rdi
009C9D82  41 54                           push r12
009C9D84  41 55                           push r13
009C9D86  41 56                           push r14
009C9D88  41 57                           push r15
009C9D8A  48 83 EC 50                     sub rsp, 0x50
009C9D8E  49 8B F1                        mov rsi, r9
009C9D91  45 0F B6 F0                     movzx r14d, r8b
009C9D95  44 8B EA                        mov r13d, edx
009C9D98  4C 8B E1                        mov r12, rcx
009C9D9B  45 33 C0                        xor r8d, r8d
009C9D9E  4C 89 44 24 30                  mov qword ptr [rsp + 0x30], r8
009C9DA3  33 C9                           xor ecx, ecx
009C9DA5  89 4C 24 20                     mov dword ptr [rsp + 0x20], ecx
009C9DA9  85 D2                           test edx, edx
009C9DAB  0F 84 1F 04 00 00               je 0x1409ca1d0
009C9DB1  41 81 FD 00 10 00 00            cmp r13d, 0x1000
009C9DB8  0F 87 2E 04 00 00               ja 0x1409ca1ec
009C9DBE  45 8B FD                        mov r15d, r13d
009C9DC1  41 C1 E7 04                     shl r15d, 4
009C9DC5  41 8B DF                        mov ebx, r15d
009C9DC8  89 5C 24 24                     mov dword ptr [rsp + 0x24], ebx
009C9DCC  45 84 F6                        test r14b, r14b
009C9DCF  0F 85 78 02 00 00               jne 0x1409ca04d
009C9DD5  BF FC FF FF FF                  mov edi, 0xfffffffc
009C9DDA  85 D2                           test edx, edx
009C9DDC  74 33                           je 0x1409c9e11
009C9DDE  49 8B C4                        mov rax, r12
009C9DE1  45 8B C5                        mov r8d, r13d
009C9DE4  0F 1F 40 00                     nop dword ptr [rax]
009C9DE8  0F 1F 84 00 00 00 00 00         nop dword ptr [rax + rax]
009C9DF0  48 8B 08                        mov rcx, qword ptr [rax]
009C9DF3  0F B6 51 01                     movzx edx, byte ptr [rcx + 1]
009C9DF7  8D 14 95 0B 00 00 00            lea edx, [rdx*4 + 0xb]
009C9DFE  23 D7                           and edx, edi
009C9E00  03 DA                           add ebx, edx
009C9E02  48 8D 40 10                     lea rax, [rax + 0x10]
009C9E06  49 83 E8 01                     sub r8, 1
009C9E0A  75 E4                           jne 0x1409c9df0
009C9E0C  4C 8B 44 24 30                  mov r8, qword ptr [rsp + 0x30]
009C9E11  48 8B 84 24 D0 00 00 00         mov rax, qword ptr [rsp + 0xd0]
009C9E19  89 18                           mov dword ptr [rax], ebx
009C9E1B  48 85 F6                        test rsi, rsi
009C9E1E  0F 84 D7 00 00 00               je 0x1409c9efb
009C9E24  3B 9C 24 B0 00 00 00            cmp ebx, dword ptr [rsp + 0xb0]
009C9E2B  76 1F                           jbe 0x1409c9e4c
009C9E2D  45 84 F6                        test r14b, r14b
009C9E30  0F 85 C0 03 00 00               jne 0x1409ca1f6
009C9E36  B8 23 00 00 C0                  mov eax, 0xc0000023
009C9E3B  48 83 C4 50                     add rsp, 0x50
009C9E3F  41 5F                           pop r15
009C9E41  41 5E                           pop r14
009C9E43  41 5D                           pop r13
009C9E45  41 5C                           pop r12
009C9E47  5F                              pop rdi
009C9E48  5E                              pop rsi
009C9E49  5B                              pop rbx
009C9E4A  C3                              ret
009C9E4B  CC                              int3
009C9E4C  4C 8B A4 24 C8 00 00 00         mov r12, qword ptr [rsp + 0xc8]
009C9E54  49 89 34 24                     mov qword ptr [r12], rsi
009C9E58  45 84 F6                        test r14b, r14b
009C9E5B  0F 85 E3 00 00 00               jne 0x1409c9f44
009C9E61  45 8B C7                        mov r8d, r15d
009C9E64  48 8B 94 24 90 00 00 00         mov rdx, qword ptr [rsp + 0x90]
009C9E6C  48 8B CE                        mov rcx, rsi
009C9E6F  E8 CC C9 CF FF                  call 0x1406c6840
009C9E74  41 8D 47 03                     lea eax, [r15 + 3]
009C9E78  48 23 C7                        and rax, rdi
009C9E7B  48 03 F0                        add rsi, rax
009C9E7E  4D 8B 34 24                     mov r14, qword ptr [r12]
009C9E82  45 85 ED                        test r13d, r13d
009C9E85  74 38                           je 0x1409c9ebf
009C9E87  4D 8B FD                        mov r15, r13
009C9E8A  66 0F 1F 44 00 00               nop word ptr [rax + rax]
009C9E90  49 8B 16                        mov rdx, qword ptr [r14]
009C9E93  0F B6 42 01                     movzx eax, byte ptr [rdx + 1]
009C9E97  8D 1C 85 08 00 00 00            lea ebx, [rax*4 + 8]
009C9E9E  44 8B C3                        mov r8d, ebx
009C9EA1  48 8B CE                        mov rcx, rsi
009C9EA4  E8 97 C9 CF FF                  call 0x1406c6840
009C9EA9  49 89 36                        mov qword ptr [r14], rsi
009C9EAC  4D 8D 76 10                     lea r14, [r14 + 0x10]
009C9EB0  8D 43 03                        lea eax, [rbx + 3]
009C9EB3  48 23 C7                        and rax, rdi
009C9EB6  48 03 F0                        add rsi, rax
009C9EB9  49 83 EF 01                     sub r15, 1
009C9EBD  75 D1                           jne 0x1409c9e90
009C9EBF  80 BC 24 A0 00 00 00 00         cmp byte ptr [rsp + 0xa0], 0
009C9EC7  74 0C                           je 0x1409c9ed5
009C9EC9  33 D2                           xor edx, edx
009C9ECB  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
009C9ED0  E8 9B 89 1B 00                  call 0x140b82870
009C9ED5  8B 5C 24 20                     mov ebx, dword ptr [rsp + 0x20]
009C9ED9  48 83 BC 24 A8 00 00 00 00      cmp qword ptr [rsp + 0xa8], 0
009C9EE2  0F 84 A9 02 00 00               je 0x1409ca191
009C9EE8  8B C3                           mov eax, ebx
009C9EEA  48 83 C4 50                     add rsp, 0x50
009C9EEE  41 5F                           pop r15
009C9EF0  41 5E                           pop r14
009C9EF2  41 5D                           pop r13
009C9EF4  41 5C                           pop r12
009C9EF6  5F                              pop rdi
009C9EF7  5E                              pop rsi
009C9EF8  5B                              pop rbx
009C9EF9  C3                              ret
009C9EFA  CC                              int3
009C9EFB  8B D3                           mov edx, ebx
009C9EFD  B9 01 04 00 00                  mov ecx, 0x401
009C9F02  41 B8 53 65 53 61               mov r8d, 0x61536553
009C9F08  E8 03 81 1B 00                  call 0x140b82010
009C9F0D  48 8B F0                        mov rsi, rax
009C9F10  4C 8B A4 24 C8 00 00 00         mov r12, qword ptr [rsp + 0xc8]
009C9F18  49 89 04 24                     mov qword ptr [r12], rax
009C9F1C  48 85 C0                        test rax, rax
009C9F1F  0F 85 33 FF FF FF               jne 0x1409c9e58
009C9F25  45 84 F6                        test r14b, r14b
009C9F28  0F 85 D7 02 00 00               jne 0x1409ca205
009C9F2E  B8 9A 00 00 C0                  mov eax, 0xc000009a
009C9F33  48 83 C4 50                     add rsp, 0x50
009C9F37  41 5F                           pop r15
009C9F39  41 5E                           pop r14
009C9F3B  41 5D                           pop r13
009C9F3D  41 5C                           pop r12
009C9F3F  5F                              pop rdi
009C9F40  5E                              pop rsi
009C9F41  5B                              pop rbx
009C9F42  C3                              ret
009C9F43  CC                              int3
009C9F44  48 89 74 24 38                  mov qword ptr [rsp + 0x38], rsi
009C9F49  45 8B C7                        mov r8d, r15d
009C9F4C  48 8B 94 24 90 00 00 00         mov rdx, qword ptr [rsp + 0x90]
009C9F54  48 8B CE                        mov rcx, rsi
009C9F57  E8 E4 C8 CF FF                  call 0x1406c6840
009C9F5C  41 8D 47 03                     lea eax, [r15 + 3]
009C9F60  48 23 C7                        and rax, rdi
009C9F63  48 03 F0                        add rsi, rax
009C9F66  48 89 74 24 38                  mov qword ptr [rsp + 0x38], rsi
009C9F6B  45 33 F6                        xor r14d, r14d
009C9F6E  44 89 74 24 28                  mov dword ptr [rsp + 0x28], r14d
009C9F73  49 8B 04 24                     mov rax, qword ptr [r12]
009C9F77  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
009C9F7C  0F 1F 40 00                     nop dword ptr [rax]
009C9F80  45 3B F5                        cmp r14d, r13d
009C9F83  0F 83 86 00 00 00               jae 0x1409ca00f
009C9F89  83 7C 24 20 00                  cmp dword ptr [rsp + 0x20], 0
009C9F8E  75 7F                           jne 0x1409ca00f
009C9F90  41 8B DE                        mov ebx, r14d
009C9F93  48 03 DB                        add rbx, rbx
009C9F96  4C 8B 7C 24 30                  mov r15, qword ptr [rsp + 0x30]
009C9F9B  45 8B 44 DF 08                  mov r8d, dword ptr [r15 + rbx*8 + 8]
009C9FA0  49 8B 14 DF                     mov rdx, qword ptr [r15 + rbx*8]
009C9FA4  48 8B CE                        mov rcx, rsi
009C9FA7  E8 94 C8 CF FF                  call 0x1406c6840
009C9FAC  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
009C9FB1  48 89 34 D9                     mov qword ptr [rcx + rbx*8], rsi
009C9FB5  45 8B 7C DF 08                  mov r15d, dword ptr [r15 + rbx*8 + 8]
009C9FBA  41 8D 47 03                     lea eax, [r15 + 3]
009C9FBE  48 23 C7                        and rax, rdi
009C9FC1  48 03 F0                        add rsi, rax
009C9FC4  48 89 74 24 38                  mov qword ptr [rsp + 0x38], rsi
009C9FC9  F7 44 D9 08 80 FF FF 1F         test dword ptr [rcx + rbx*8 + 8], 0x1fffff80
009C9FD1  75 32                           jne 0x1409ca005
009C9FD3  48 8B 1C D9                     mov rbx, qword ptr [rcx + rbx*8]
009C9FD7  48 8B CB                        mov rcx, rbx
009C9FDA  E8 31 F7 F5 FF                  call 0x140929710
009C9FDF  84 C0                           test al, al
009C9FE1  74 0D                           je 0x1409c9ff0
009C9FE3  48 8B CB                        mov rcx, rbx
009C9FE6  E8 85 32 A9 FF                  call 0x14045d270
009C9FEB  41 3B C7                        cmp eax, r15d
009C9FEE  74 08                           je 0x1409c9ff8
009C9FF0  C7 44 24 20 78 00 00 C0         mov dword ptr [rsp + 0x20], 0xc0000078
009C9FF8  41 FF C6                        inc r14d
009C9FFB  44 89 74 24 28                  mov dword ptr [rsp + 0x28], r14d
009CA000  E9 7B FF FF FF                  jmp 0x1409c9f80
009CA005  C7 44 24 20 0D 00 00 C0         mov dword ptr [rsp + 0x20], 0xc000000d
009CA00D  EB E9                           jmp 0x1409c9ff8
009CA00F  E9 AB FE FF FF                  jmp 0x1409c9ebf
009CA014  8B F8                           mov edi, eax
009CA016  48 83 BC 24 A8 00 00 00 00      cmp qword ptr [rsp + 0xa8], 0
009CA01F  75 19                           jne 0x1409ca03a
009CA021  33 D2                           xor edx, edx
009CA023  48 8B 9C 24 C8 00 00 00         mov rbx, qword ptr [rsp + 0xc8]
009CA02B  48 8B 0B                        mov rcx, qword ptr [rbx]
009CA02E  E8 3D 88 1B 00                  call 0x140b82870
009CA033  48 C7 03 00 00 00 00            mov qword ptr [rbx], 0
009CA03A  33 D2                           xor edx, edx
009CA03C  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
009CA041  E8 2A 88 1B 00                  call 0x140b82870
009CA046  8B C7                           mov eax, edi
009CA048  E9 9D FE FF FF                  jmp 0x1409c9eea
009CA04D  41 B8 53 65 54 61               mov r8d, 0x61546553
009CA053  48 8B D3                        mov rdx, rbx
009CA056  B9 01 04 00 00                  mov ecx, 0x401
009CA05B  E8 B0 7F 1B 00                  call 0x140b82010
009CA060  4C 8B C0                        mov r8, rax
009CA063  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
009CA068  48 85 C0                        test rax, rax
009CA06B  0F 84 BD FE FF FF               je 0x1409c9f2e
009CA071  45 85 FF                        test r15d, r15d
009CA074  0F 84 BA 00 00 00               je 0x1409ca134
009CA07A  41 F6 C4 03                     test r12b, 3
009CA07E  0F 85 BF 00 00 00               jne 0x1409ca143
009CA084  4B 8D 04 27                     lea rax, [r15 + r12]
009CA088  49 BE 00 00 FF FF FF 7F 00 00   movabs r14, 0x7fffffff0000
009CA092  49 3B C6                        cmp rax, r14
009CA095  0F 87 AD 00 00 00               ja 0x1409ca148
009CA09B  49 3B C4                        cmp rax, r12
009CA09E  0F 82 A4 00 00 00               jb 0x1409ca148
009CA0A4  33 C0                           xor eax, eax
009CA0A6  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
009CA0AA  BF FC FF FF FF                  mov edi, 0xfffffffc
009CA0AF  90                              nop
009CA0B0  41 3B C5                        cmp eax, r13d
009CA0B3  73 6A                           jae 0x1409ca11f
009CA0B5  8B F0                           mov esi, eax
009CA0B7  48 03 F6                        add rsi, rsi
009CA0BA  49 8B 1C F4                     mov rbx, qword ptr [r12 + rsi*8]
009CA0BE  48 8D 43 01                     lea rax, [rbx + 1]
009CA0C2  49 3B C6                        cmp rax, r14
009CA0C5  49 0F 43 C6                     cmovae rax, r14
009CA0C9  90                              nop
009CA0CA  0F B6 00                        movzx eax, byte ptr [rax]
009CA0CD  8B C8                           mov ecx, eax
009CA0CF  83 F8 0F                        cmp eax, 0xf
009CA0D2  77 51                           ja 0x1409ca125
009CA0D4  49 89 1C F0                     mov qword ptr [r8 + rsi*8], rbx
009CA0D8  E8 F3 03 00 00                  call 0x1409ca4d0
009CA0DD  4C 8B 44 24 30                  mov r8, qword ptr [rsp + 0x30]
009CA0E2  41 89 44 F0 08                  mov dword ptr [r8 + rsi*8 + 8], eax
009CA0E7  85 C0                           test eax, eax
009CA0E9  74 14                           je 0x1409ca0ff
009CA0EB  F6 C3 03                        test bl, 3
009CA0EE  75 65                           jne 0x1409ca155
009CA0F0  8B C8                           mov ecx, eax
009CA0F2  48 03 CB                        add rcx, rbx
009CA0F5  49 3B CE                        cmp rcx, r14
009CA0F8  77 60                           ja 0x1409ca15a
009CA0FA  48 3B CB                        cmp rcx, rbx
009CA0FD  72 5B                           jb 0x1409ca15a
009CA0FF  41 8B 44 F0 08                  mov eax, dword ptr [r8 + rsi*8 + 8]
009CA104  83 C0 03                        add eax, 3
009CA107  23 C7                           and eax, edi
009CA109  8B 5C 24 24                     mov ebx, dword ptr [rsp + 0x24]
009CA10D  03 D8                           add ebx, eax
009CA10F  89 5C 24 24                     mov dword ptr [rsp + 0x24], ebx
009CA113  8B 44 24 28                     mov eax, dword ptr [rsp + 0x28]
009CA117  FF C0                           inc eax
009CA119  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
009CA11D  EB 91                           jmp 0x1409ca0b0
009CA11F  8B 4C 24 20                     mov ecx, dword ptr [rsp + 0x20]
009CA123  EB 3B                           jmp 0x1409ca160
009CA125  B9 78 00 00 C0                  mov ecx, 0xc0000078
009CA12A  89 4C 24 20                     mov dword ptr [rsp + 0x20], ecx
009CA12E  8B 5C 24 24                     mov ebx, dword ptr [rsp + 0x24]
009CA132  EB 2C                           jmp 0x1409ca160
009CA134  49 BE 00 00 FF FF FF 7F 00 00   movabs r14, 0x7fffffff0000
009CA13E  E9 61 FF FF FF                  jmp 0x1409ca0a4
009CA143  E8 88 FE EC FF                  call 0x140899fd0
009CA148  41 0F B6 06                     movzx eax, byte ptr [r14]
009CA14C  8B 5C 24 24                     mov ebx, dword ptr [rsp + 0x24]
009CA150  E9 4F FF FF FF                  jmp 0x1409ca0a4
009CA155  E8 76 FE EC FF                  call 0x140899fd0
009CA15A  41 0F B6 06                     movzx eax, byte ptr [r14]
009CA15E  EB 9F                           jmp 0x1409ca0ff
009CA160  EB 15                           jmp 0x1409ca177
009CA162  8B D8                           mov ebx, eax
009CA164  33 D2                           xor edx, edx
009CA166  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
009CA16B  E8 00 87 1B 00                  call 0x140b82870
009CA170  8B C3                           mov eax, ebx
009CA172  E9 73 FD FF FF                  jmp 0x1409c9eea
009CA177  85 C9                           test ecx, ecx
009CA179  78 36                           js 0x1409ca1b1
009CA17B  48 8B B4 24 A8 00 00 00         mov rsi, qword ptr [rsp + 0xa8]
009CA183  44 0F B6 B4 24 A0 00 00 00      movzx r14d, byte ptr [rsp + 0xa0]
009CA18C  E9 80 FC FF FF                  jmp 0x1409c9e11
009CA191  85 DB                           test ebx, ebx
009CA193  0F 89 4F FD FF FF               jns 0x1409c9ee8
009CA199  33 D2                           xor edx, edx
009CA19B  49 8B 0C 24                     mov rcx, qword ptr [r12]
009CA19F  E8 CC 86 1B 00                  call 0x140b82870
009CA1A4  49 C7 04 24 00 00 00 00         mov qword ptr [r12], 0
009CA1AC  E9 37 FD FF FF                  jmp 0x1409c9ee8
009CA1B1  33 D2                           xor edx, edx
009CA1B3  49 8B C8                        mov rcx, r8
009CA1B6  E8 B5 86 1B 00                  call 0x140b82870
009CA1BB  8B 44 24 20                     mov eax, dword ptr [rsp + 0x20]
009CA1BF  48 83 C4 50                     add rsp, 0x50
009CA1C3  41 5F                           pop r15
009CA1C5  41 5E                           pop r14
009CA1C7  41 5D                           pop r13
009CA1C9  41 5C                           pop r12
009CA1CB  5F                              pop rdi
009CA1CC  5E                              pop rsi
009CA1CD  5B                              pop rbx
009CA1CE  C3                              ret
009CA1CF  CC                              int3
009CA1D0  48 8B 84 24 C8 00 00 00         mov rax, qword ptr [rsp + 0xc8]
009CA1D8  48 89 08                        mov qword ptr [rax], rcx
009CA1DB  48 8B 84 24 D0 00 00 00         mov rax, qword ptr [rsp + 0xd0]
009CA1E3  89 08                           mov dword ptr [rax], ecx
009CA1E5  33 C0                           xor eax, eax
009CA1E7  E9 FE FC FF FF                  jmp 0x1409c9eea
009CA1EC  B8 0D 00 00 C0                  mov eax, 0xc000000d
009CA1F1  E9 F4 FC FF FF                  jmp 0x1409c9eea
009CA1F6  33 D2                           xor edx, edx
009CA1F8  49 8B C8                        mov rcx, r8
009CA1FB  E8 70 86 1B 00                  call 0x140b82870
009CA200  E9 31 FC FF FF                  jmp 0x1409c9e36
009CA205  33 D2                           xor edx, edx
009CA207  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
009CA20C  E8 5F 86 1B 00                  call 0x140b82870
009CA211  E9 18 FD FF FF                  jmp 0x1409c9f2e
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SeCaptureSidAndAttributesArray(__int64 a1, int a2, int a3, __int64 a4, unsigned int a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_m64;
    unsigned int v_stack_m68;
    unsigned int v_stack_p130;
    unsigned int v_stack_p134;
    unsigned int v_stack_p138;
    unsigned __int64 v_stack_p140;
    unsigned __int64 v_stack_p148;
    unsigned __int64 v_stack_p150;
    unsigned __int8 v_stack_p18;
    unsigned __int64 v_stack_p1A0;
    unsigned __int8 v_stack_p1B0;
    unsigned __int64 v_stack_p1B8;
    unsigned __int64 v_stack_p1C8;
    unsigned __int64 v_stack_p1D8;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p8;
    unsigned __int64 v_stack_p90;
    unsigned __int8 v_stack_pA0;
    unsigned __int64 v_stack_pA8;

    v_stack_p20 = a4;
    v_stack_p18 = (unsigned __int8)(a3);
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (80);
    a3 = 0;
    v_stack_m58 = 0;
    a1 = 0;
    v_stack_m68 = 0;
    if (a2 == 0) goto loc_009CA1D0;
    if (((unsigned int)((unsigned int)(a2))) > 0x1000ULL) goto loc_009CA1EC;
    v_r15 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a2)))) << (4));
    v_stack_m64 = (unsigned int)((unsigned int)((unsigned int)(v_r15)));
    if ((unsigned __int8)((unsigned __int8)(a3)) != 0) goto loc_009CA04D;
    if (a2 == 0) goto loc_009C9E11;
loc_009C9DF0:
    a2 = (unsigned int)((*(unsigned __int8 *)(*(unsigned __int64 *)(0) + 1) * 4 + 11) & ((unsigned int)((unsigned int)(0xFFFFFFFCULL))));
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)(v_r15))) + (a2));
    a3 = ((unsigned int)((unsigned int)((unsigned int)(a2)))) - (1);
    if (condition_is_not_equal) goto loc_009C9DF0;
loc_009C9E11:
    *(unsigned int *)(a9) = (unsigned int)(v_rbx);
    if (a4 == 0) goto loc_009C9EFB;
    if (((unsigned int)(v_rbx)) <= a5) goto loc_009C9E4C;
    if ((unsigned __int8)((unsigned __int8)(a3)) != 0) goto loc_009CA1F6;
loc_009C9E36:
    v_rsp = (v_rsp) + (80);
    return (unsigned int)(0xC0000023ULL);
loc_009C9E4C:
    *(unsigned __int64 *)(a8) = a4;
loc_009C9E58:
    if ((unsigned __int8)((unsigned __int8)(a3)) != 0) goto loc_009C9F44;
    result = memcpy(a4, v_stack_p90, (unsigned int)((unsigned int)(v_r15)), a4);
    result = (v_r15 + 3) & ((unsigned int)(0xFFFFFFFCULL));
    v_rsi = (a4) + (result);
    if ((unsigned int)((unsigned int)(a2)) == 0) goto loc_009C9EBF;
loc_009C9E90:
    result = memcpy(v_rsi, *(unsigned __int64 *)(*(unsigned __int64 *)(a8)), (unsigned int)((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a8)) + 1) * 4 + 8)), a4);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a8)) = v_rsi;
    result = (*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a8)) + 1) * 4 + 8 + 3) & ((unsigned int)(0xFFFFFFFCULL));
    v_rsi = (v_rsi) + (result);
    v_r15 = ((unsigned int)(a2)) - (1);
    if (condition_is_not_equal) goto loc_009C9E90;
loc_009C9EBF:
    if (v_stack_pA0 != 0) {
        a2 = 0;
        a1 = v_stack_p30;
        result = ExFreePoolWithTag(a1, a2, (unsigned int)((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a8)) + 1) * 4 + 8)), a4);
    }
    if (v_stack_pA8 == 0) goto loc_009CA191;
loc_009C9EE8:
loc_009C9EEA:
    v_rsp = (v_rsp) + (80);
    return (unsigned int)((unsigned int)((unsigned int)(v_stack_p20)));
loc_009C9EFB:
    result = ExAllocatePoolWithTag((unsigned int)(0x401ULL), (unsigned int)((unsigned int)((unsigned int)(v_stack_p20))), (unsigned int)(0x61536553ULL), a4);
    *(unsigned __int64 *)(a8) = result;
    if (result != 0) goto loc_009C9E58;
    if ((unsigned __int8)(*(unsigned __int64 *)(a8) + 16) != 0) goto loc_009CA205;
loc_009C9F2E:
    v_rsp = (v_rsp) + (80);
    return (unsigned int)(0xC000009AULL);
loc_009C9F44:
    v_stack_p148 = result;
    result = memcpy(result, v_stack_p1A0, (unsigned int)((unsigned int)(v_r15)), a4);
    result = (v_r15 + 3) & ((unsigned int)(0xFFFFFFFCULL));
    v_rsi = (result) + (result);
    v_stack_p148 = v_rsi;
    v_r14 = 0;
    v_stack_p138 = 0;
    v_stack_p150 = *(unsigned __int64 *)(a8);
loc_009C9F80:
    if (0 >= ((unsigned int)((unsigned int)(a2)))) goto loc_009CA00F;
    if (v_stack_p130 != 0) goto loc_009CA00F;
    v_rbx = (0) + (0);
    result = memcpy(v_rsi, *(unsigned __int64 *)(v_stack_p140 + v_rbx * 8), (unsigned int)(*(unsigned int *)(v_stack_p140 + v_rbx * 8 + 8)), a4);
    *(unsigned __int64 *)(v_stack_p150 + v_rbx * 8) = v_rsi;
    result = ((unsigned int)(*(unsigned int *)(v_stack_p140 + v_rbx * 8 + 8)) + 3) & ((unsigned int)(0xFFFFFFFCULL));
    v_rsi = (v_rsi) + (result);
    v_stack_p148 = v_rsi;
    if (((*(unsigned int *)(v_stack_p150 + v_rbx * 8 + 8)) & (0x1FFFFF80ULL)) != 0) goto loc_009CA005;
    result = RtlValidSid(*(unsigned __int64 *)(v_stack_p150 + v_rbx * 8), *(unsigned __int64 *)(v_stack_p140 + v_rbx * 8), (unsigned int)(*(unsigned int *)(v_stack_p140 + v_rbx * 8 + 8)), a4);
    if ((unsigned __int8)(result) == 0) goto loc_009C9FF0;
    result = RtlLengthSid(*(unsigned __int64 *)(v_stack_p150 + v_rbx * 8), *(unsigned __int64 *)(v_stack_p140 + v_rbx * 8), (unsigned int)(*(unsigned int *)(v_stack_p140 + v_rbx * 8 + 8)), a4);
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p140 + v_rbx * 8 + 8))))) {
        v_stack_p130 = 0xC0000078ULL;
    }
    v_r14 = (unsigned int)((v_r14) + 1);
    v_stack_p138 = (unsigned int)(v_r14);
    goto loc_009C9F80;
loc_009CA005:
    v_stack_p130 = 0xC000000DULL;
    goto loc_009C9FF8;
loc_009CA00F:
    goto loc_009C9EBF;
loc_009CA04D:
    result = ExAllocatePoolWithTag((unsigned int)(0x401ULL), *(unsigned __int64 *)(v_stack_p150 + v_rbx * 8), (unsigned int)(0x61546553ULL), a4);
    v_stack_p140 = result;
    if (result == 0) goto loc_009C9F2E;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p140 + v_rbx * 8 + 8))) == 0) goto loc_009CA134;
    if ((((unsigned __int8)(a8)) & (3)) != 0) goto loc_009CA143;
    if (((unsigned int)(*(unsigned int *)(v_stack_p140 + v_rbx * 8 + 8)) + a8 * 1) > v_r14) goto loc_009CA148;
    if (((unsigned int)(*(unsigned int *)(v_stack_p140 + v_rbx * 8 + 8)) + a8 * 1) < a8) goto loc_009CA148;
loc_009CA0A4:
    result = 0;
    v_stack_p138 = 0;
loc_009CA0B0:
    if (0 >= ((unsigned int)((unsigned int)(a2)))) goto loc_009CA11F;
    v_rsi = (0) + (0);
    result = *(unsigned __int64 *)(a8 + v_rsi * 8) + 1;
    if ((*(unsigned __int64 *)(a8 + v_rsi * 8) + 1) >= v_r14) { result = v_r14; }
    if (((unsigned int)(*(unsigned __int8 *)(result))) > 15) goto loc_009CA125;
    *(unsigned __int64 *)(result + v_rsi * 8) = *(unsigned __int64 *)(a8 + v_rsi * 8);
    result = RtlLengthRequiredSid((unsigned int)((unsigned int)(*(unsigned __int8 *)(result))), *(unsigned __int64 *)(v_stack_p150 + v_rbx * 8), result, a4);
    *(unsigned int *)(v_stack_p140 + v_rsi * 8 + 8) = (unsigned int)(result);
    if ((unsigned int)(result) == 0) goto loc_009CA0FF;
    if ((((unsigned __int8)(*(unsigned __int64 *)(a8 + v_rsi * 8))) & (3)) != 0) goto loc_009CA155;
    a1 = ((unsigned int)((unsigned int)(result))) + (*(unsigned __int64 *)(a8 + v_rsi * 8));
    if (a1 > v_r14) goto loc_009CA15A;
    if (a1 < (*(unsigned __int64 *)(a8 + v_rsi * 8))) goto loc_009CA15A;
loc_009CA0FF:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p140 + v_rsi * 8 + 8))) + (3));
    result = (unsigned int)((result) & ((unsigned int)((unsigned int)(0xFFFFFFFCULL))));
    v_rbx = (unsigned int)(((unsigned int)(v_stack_p134)) + ((unsigned int)(result)));
    v_stack_p134 = (unsigned int)(v_rbx);
    result = (unsigned int)(((unsigned int)(v_stack_p138)) + 1);
    v_stack_p138 = (unsigned int)(result);
    goto loc_009CA0B0;
loc_009CA11F:
    goto loc_009CA160;
loc_009CA125:
    v_stack_p130 = (unsigned int)((unsigned int)(0xC0000078ULL));
    goto loc_009CA160;
loc_009CA134:
    goto loc_009CA0A4;
loc_009CA143:
    result = ExRaiseDatatypeMisalignment((unsigned int)(0xC0000078ULL), *(unsigned __int64 *)(v_stack_p150 + v_rbx * 8), v_stack_p140, a4);
loc_009CA148:
    goto loc_009CA0A4;
loc_009CA155:
    result = ExRaiseDatatypeMisalignment((unsigned int)(0xC0000078ULL), *(unsigned __int64 *)(v_stack_p150 + v_rbx * 8), v_stack_p140, a4);
loc_009CA15A:
    goto loc_009CA0FF;
loc_009CA160:
    goto loc_009CA177;
loc_009CA177:
    if (sign_flag) goto loc_009CA1B1;
    goto loc_009C9E11;
loc_009CA191:
    if (!sign_flag) goto loc_009C9EE8;
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(a8), a2, v_stack_p140, a4);
    *(unsigned __int64 *)(a8) = 0;
    goto loc_009C9EE8;
loc_009CA1B1:
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_p140, a2, v_stack_p140, a4);
    v_rsp = (v_rsp) + (80);
    return (unsigned int)(v_stack_p130);
loc_009CA1D0:
    *(unsigned __int64 *)(a8) = v_stack_p140;
    *(unsigned int *)(a9) = (unsigned int)(v_stack_p140);
    result = 0;
    goto loc_009C9EEA;
loc_009CA1EC:
    goto loc_009C9EEA;
loc_009CA1F6:
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_p140, a2, v_stack_p140, a4);
    goto loc_009C9E36;
loc_009CA205:
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_p1C8, a2, v_stack_p140, a4);
    goto loc_009C9F2E;
}
```

## 5. (Beta) C Style

```c
int64_t SeCaptureSidAndAttributesArray(void *Arg1, int32_t Arg2, int32_t Arg3, int64_t Arg4, uint32_t Arg5, uint64_t Arg6, uint64_t Arg7, void *Arg8, void *Arg9)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg8 = (uint8_t *)Arg8;
    uint8_t *arg9 = (uint8_t *)Arg9;

    int64_t result;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m58;
    uint32_t v_stack_m64;
    uint32_t v_stack_m68;
    uint32_t v_stack_p130;
    uint32_t v_stack_p134;
    uint32_t v_stack_p138;
    uint64_t v_stack_p140;
    uint64_t v_stack_p148;
    uint64_t v_stack_p150;
    uint8_t v_stack_p18;
    uint64_t v_stack_p1A0;
    uint8_t v_stack_p1B0;
    uint64_t v_stack_p1B8;
    uint64_t v_stack_p1C8;
    uint64_t v_stack_p1D8;
    uint64_t v_stack_p20;
    uint64_t v_stack_p30;
    uint64_t v_stack_p8;
    uint64_t v_stack_p90;
    uint8_t v_stack_pA0;
    uint64_t v_stack_pA8;

    v_stack_p20 = Arg4;
    v_stack_p18 = (uint8_t)(Arg3);
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (80);
    Arg3 = 0;
    v_stack_m58 = 0;
    Arg1 = 0;
    v_stack_m68 = 0;
    if (Arg2 == 0) goto loc_009CA1D0;
    if (((uint32_t)((uint32_t)(Arg2))) > 0x1000ULL) goto loc_009CA1EC;
    local_r15 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg2)))) << (4));
    v_stack_m64 = (uint32_t)((uint32_t)((uint32_t)(local_r15)));
    if ((uint8_t)((uint8_t)(Arg3)) != 0) goto loc_009CA04D;
    if (Arg2 == 0) goto loc_009C9E11;
loc_009C9DF0:
    Arg2 = (uint32_t)((*(uint8_t *)(*(uint64_t *)(0) + 0x1) * 4 + 11) & ((uint32_t)((uint32_t)(0xFFFFFFFCULL))));
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)(local_r15))) + (Arg2));
    Arg3 = ((uint32_t)((uint32_t)((uint32_t)(Arg2)))) - (1);
    if (condition_is_not_equal) goto loc_009C9DF0;
loc_009C9E11:
    *(uint32_t *)(arg9) = (uint32_t)(local_rbx);
    if (Arg4 == 0) goto loc_009C9EFB;
    if (((uint32_t)(local_rbx)) <= Arg5) goto loc_009C9E4C;
    if ((uint8_t)((uint8_t)(Arg3)) != 0) goto loc_009CA1F6;
loc_009C9E36:
    local_rsp = (local_rsp) + (80);
    return (uint32_t)(0xC0000023ULL);
loc_009C9E4C:
    *(uint64_t *)(arg8) = Arg4;
loc_009C9E58:
    if ((uint8_t)((uint8_t)(Arg3)) != 0) goto loc_009C9F44;
    result = memcpy(Arg4, v_stack_p90, (uint32_t)((uint32_t)(local_r15)), Arg4);
    result = (local_r15 + 3) & ((uint32_t)(0xFFFFFFFCULL));
    local_rsi = (Arg4) + (result);
    if ((uint32_t)((uint32_t)(Arg2)) == 0) goto loc_009C9EBF;
loc_009C9E90:
    result = memcpy(local_rsi, *(uint64_t *)(*(uint64_t *)(arg8)), (uint32_t)((uint32_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg8)) + 0x1) * 4 + 8)), Arg4);
    *(uint64_t *)(*(uint64_t *)(arg8)) = local_rsi;
    result = (*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg8)) + 0x1) * 4 + 8 + 3) & ((uint32_t)(0xFFFFFFFCULL));
    local_rsi = (local_rsi) + (result);
    local_r15 = ((uint32_t)(Arg2)) - (1);
    if (condition_is_not_equal) goto loc_009C9E90;
loc_009C9EBF:
    if (v_stack_pA0 != 0) {
        Arg2 = 0;
        Arg1 = v_stack_p30;
        result = ExFreePoolWithTag(Arg1, Arg2, (uint32_t)((uint32_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg8)) + 0x1) * 4 + 8)), Arg4);
    }
    if (v_stack_pA8 == 0) goto loc_009CA191;
loc_009C9EE8:
loc_009C9EEA:
    local_rsp = (local_rsp) + (80);
    return (uint32_t)((uint32_t)((uint32_t)(v_stack_p20)));
loc_009C9EFB:
    result = ExAllocatePoolWithTag((uint32_t)(0x401ULL), (uint32_t)((uint32_t)((uint32_t)(v_stack_p20))), (uint32_t)(0x61536553ULL), Arg4);
    *(uint64_t *)(arg8) = result;
    if (result != 0) goto loc_009C9E58;
    if ((uint8_t)(*(uint64_t *)(arg8) + 16) != 0) goto loc_009CA205;
loc_009C9F2E:
    local_rsp = (local_rsp) + (80);
    return (uint32_t)(0xC000009AULL);
loc_009C9F44:
    v_stack_p148 = result;
    result = memcpy(result, v_stack_p1A0, (uint32_t)((uint32_t)(local_r15)), Arg4);
    result = (local_r15 + 3) & ((uint32_t)(0xFFFFFFFCULL));
    local_rsi = (result) + (result);
    v_stack_p148 = local_rsi;
    local_r14 = 0;
    v_stack_p138 = 0;
    v_stack_p150 = *(uint64_t *)(arg8);
loc_009C9F80:
    if (0 >= ((uint32_t)((uint32_t)(Arg2)))) goto loc_009CA00F;
    if (v_stack_p130 != 0) goto loc_009CA00F;
    local_rbx = (0) + (0);
    result = memcpy(local_rsi, *(uint64_t *)(v_stack_p140 + local_rbx * 8), (uint32_t)(*(uint32_t *)(v_stack_p140 + local_rbx * 8 + 0x8)), Arg4);
    *(uint64_t *)(v_stack_p150 + local_rbx * 8) = local_rsi;
    result = ((uint32_t)(*(uint32_t *)(v_stack_p140 + local_rbx * 8 + 0x8)) + 3) & ((uint32_t)(0xFFFFFFFCULL));
    local_rsi = (local_rsi) + (result);
    v_stack_p148 = local_rsi;
    if (((*(uint32_t *)(v_stack_p150 + local_rbx * 8 + 0x8)) & (0x1FFFFF80ULL)) != 0) goto loc_009CA005;
    result = RtlValidSid(*(uint64_t *)(v_stack_p150 + local_rbx * 8), *(uint64_t *)(v_stack_p140 + local_rbx * 8), (uint32_t)(*(uint32_t *)(v_stack_p140 + local_rbx * 8 + 0x8)), Arg4);
    if ((uint8_t)(result) == 0) goto loc_009C9FF0;
    result = RtlLengthSid(*(uint64_t *)(v_stack_p150 + local_rbx * 8), *(uint64_t *)(v_stack_p140 + local_rbx * 8), (uint32_t)(*(uint32_t *)(v_stack_p140 + local_rbx * 8 + 0x8)), Arg4);
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p140 + local_rbx * 8 + 0x8))))) {
        v_stack_p130 = 0xC0000078ULL;
    }
    local_r14 = (uint32_t)((local_r14) + 1);
    v_stack_p138 = (uint32_t)(local_r14);
    goto loc_009C9F80;
loc_009CA005:
    v_stack_p130 = 0xC000000DULL;
    goto loc_009C9FF8;
loc_009CA00F:
    goto loc_009C9EBF;
loc_009CA04D:
    result = ExAllocatePoolWithTag((uint32_t)(0x401ULL), *(uint64_t *)(v_stack_p150 + local_rbx * 8), (uint32_t)(0x61546553ULL), Arg4);
    v_stack_p140 = result;
    if (result == 0) goto loc_009C9F2E;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p140 + local_rbx * 8 + 0x8))) == 0) goto loc_009CA134;
    if ((((uint8_t)(Arg8)) & (3)) != 0) goto loc_009CA143;
    if (((uint32_t)(*(uint32_t *)(v_stack_p140 + local_rbx * 8 + 0x8)) + Arg8 * 1) > local_r14) goto loc_009CA148;
    if (((uint32_t)(*(uint32_t *)(v_stack_p140 + local_rbx * 8 + 0x8)) + Arg8 * 1) < Arg8) goto loc_009CA148;
loc_009CA0A4:
    result = 0;
    v_stack_p138 = 0;
loc_009CA0B0:
    if (0 >= ((uint32_t)((uint32_t)(Arg2)))) goto loc_009CA11F;
    local_rsi = (0) + (0);
    result = *(uint64_t *)(arg8 + local_rsi * 8) + 1;
    if ((*(uint64_t *)(arg8 + local_rsi * 8) + 1) >= local_r14) { result = local_r14; }
    if (((uint32_t)(*(uint8_t *)(result))) > 15) goto loc_009CA125;
    *(uint64_t *)(result + local_rsi * 8) = *(uint64_t *)(arg8 + local_rsi * 8);
    result = RtlLengthRequiredSid((uint32_t)((uint32_t)(*(uint8_t *)(result))), *(uint64_t *)(v_stack_p150 + local_rbx * 8), result, Arg4);
    *(uint32_t *)(v_stack_p140 + local_rsi * 8 + 0x8) = (uint32_t)(result);
    if ((uint32_t)(result) == 0) goto loc_009CA0FF;
    if ((((uint8_t)(*(uint64_t *)(arg8 + local_rsi * 8))) & (3)) != 0) goto loc_009CA155;
    Arg1 = ((uint32_t)((uint32_t)(result))) + (*(uint64_t *)(arg8 + local_rsi * 8));
    if (Arg1 > local_r14) goto loc_009CA15A;
    if (Arg1 < (*(uint64_t *)(arg8 + local_rsi * 8))) goto loc_009CA15A;
loc_009CA0FF:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p140 + local_rsi * 8 + 0x8))) + (3));
    result = (uint32_t)((result) & ((uint32_t)((uint32_t)(0xFFFFFFFCULL))));
    local_rbx = (uint32_t)(((uint32_t)(v_stack_p134)) + ((uint32_t)(result)));
    v_stack_p134 = (uint32_t)(local_rbx);
    result = (uint32_t)(((uint32_t)(v_stack_p138)) + 1);
    v_stack_p138 = (uint32_t)(result);
    goto loc_009CA0B0;
loc_009CA11F:
    goto loc_009CA160;
loc_009CA125:
    v_stack_p130 = (uint32_t)((uint32_t)(0xC0000078ULL));
    goto loc_009CA160;
loc_009CA134:
    goto loc_009CA0A4;
loc_009CA143:
    result = ExRaiseDatatypeMisalignment((uint32_t)(0xC0000078ULL), *(uint64_t *)(v_stack_p150 + local_rbx * 8), v_stack_p140, Arg4);
loc_009CA148:
    goto loc_009CA0A4;
loc_009CA155:
    result = ExRaiseDatatypeMisalignment((uint32_t)(0xC0000078ULL), *(uint64_t *)(v_stack_p150 + local_rbx * 8), v_stack_p140, Arg4);
loc_009CA15A:
    goto loc_009CA0FF;
loc_009CA160:
    goto loc_009CA177;
loc_009CA177:
    if (sign_flag) goto loc_009CA1B1;
    goto loc_009C9E11;
loc_009CA191:
    if (!sign_flag) goto loc_009C9EE8;
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(arg8), Arg2, v_stack_p140, Arg4);
    *(uint64_t *)(arg8) = 0;
    goto loc_009C9EE8;
loc_009CA1B1:
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_p140, Arg2, v_stack_p140, Arg4);
    local_rsp = (local_rsp) + (80);
    return (uint32_t)(v_stack_p130);
loc_009CA1D0:
    *(uint64_t *)(arg8) = v_stack_p140;
    *(uint32_t *)(arg9) = (uint32_t)(v_stack_p140);
    result = 0;
    goto loc_009C9EEA;
loc_009CA1EC:
    goto loc_009C9EEA;
loc_009CA1F6:
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_p140, Arg2, v_stack_p140, Arg4);
    goto loc_009C9E36;
loc_009CA205:
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_p1C8, Arg2, v_stack_p140, Arg4);
    goto loc_009C9F2E;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x0 + rax*1` | `32` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg8` | `+ 0x0` | `64` | `R` |
| `Arg8` | `+ 0x0` | `64` | `W` |
| `Arg9` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009C9D70&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
