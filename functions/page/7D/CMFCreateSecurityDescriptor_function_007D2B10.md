# CMFCreateSecurityDescriptor

- RVA: `0x007D2B10`–`0x007D313A` (길이 `1,578` bytes)
- VA: `0x00000001407D2B10`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BC564`
- 디코드: `432`개 명령, `1,578/1,578` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **48**; 고유 호출 대상: **13**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x007D2B89` → [RtlCreateSecurityDescriptor](../9F/RtlCreateSecurityDescriptor_function_009F1DF0.md) (function, `0x009F1DF0`)
- `0x007D2BA4` → [RtlLengthRequiredSid](../9C/RtlLengthRequiredSid_function_009CA4D0.md) (function, `0x009CA4D0`)
- `0x007D2BB6` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x007D2BD8` → [RtlInitializeSid](../9E/RtlInitializeSid_function_009EB720.md) (function, `0x009EB720`)
- `0x007D2BF7` → [RtlSubAuthoritySid](../../text/45/RtlSubAuthoritySid_function_00456D10.md) (function, `0x00456D10`)
- `0x007D2C07` → [RtlLengthRequiredSid](../9C/RtlLengthRequiredSid_function_009CA4D0.md) (function, `0x009CA4D0`)
- `0x007D2C19` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x007D2C3A` → [RtlInitializeSid](../9E/RtlInitializeSid_function_009EB720.md) (function, `0x009EB720`)
- `0x007D2C44` → [RtlSubAuthoritySid](../../text/45/RtlSubAuthoritySid_function_00456D10.md) (function, `0x00456D10`)
- `0x007D2C57` → [RtlSubAuthoritySid](../../text/45/RtlSubAuthoritySid_function_00456D10.md) (function, `0x00456D10`)
- `0x007D2C6C` → [RtlSubAuthoritySid](../../text/45/RtlSubAuthoritySid_function_00456D10.md) (function, `0x00456D10`)
- `0x007D2C7D` → [RtlSubAuthoritySid](../../text/45/RtlSubAuthoritySid_function_00456D10.md) (function, `0x00456D10`)
- `0x007D2C8E` → [RtlSubAuthoritySid](../../text/45/RtlSubAuthoritySid_function_00456D10.md) (function, `0x00456D10`)
- `0x007D2C9F` → [RtlSubAuthoritySid](../../text/45/RtlSubAuthoritySid_function_00456D10.md) (function, `0x00456D10`)
- `0x007D2CB6` → [RtlLengthRequiredSid](../9C/RtlLengthRequiredSid_function_009CA4D0.md) (function, `0x009CA4D0`)
- `0x007D2CCE` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x007D2CED` → [RtlInitializeSid](../9E/RtlInitializeSid_function_009EB720.md) (function, `0x009EB720`)
- `0x007D2D08` → [RtlSubAuthoritySid](../../text/45/RtlSubAuthoritySid_function_00456D10.md) (function, `0x00456D10`)
- `0x007D2D1D` → [RtlSubAuthoritySid](../../text/45/RtlSubAuthoritySid_function_00456D10.md) (function, `0x00456D10`)
- `0x007D2D3D` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x007D2D58` → [RtlInitializeSid](../9E/RtlInitializeSid_function_009EB720.md) (function, `0x009EB720`)
- `0x007D2D73` → [RtlSubAuthoritySid](../../text/45/RtlSubAuthoritySid_function_00456D10.md) (function, `0x00456D10`)
- `0x007D2D85` → [RtlSubAuthoritySid](../../text/45/RtlSubAuthoritySid_function_00456D10.md) (function, `0x00456D10`)
- `0x007D2DA6` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x007D2DC1` → [RtlInitializeSid](../9E/RtlInitializeSid_function_009EB720.md) (function, `0x009EB720`)
- `0x007D2DDC` → [RtlSubAuthoritySid](../../text/45/RtlSubAuthoritySid_function_00456D10.md) (function, `0x00456D10`)
- `0x007D2DEF` → [RtlSubAuthoritySid](../../text/45/RtlSubAuthoritySid_function_00456D10.md) (function, `0x00456D10`)
- `0x007D2E17` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x007D2E39` → [RtlCreateAcl](../91/RtlCreateAcl_function_00916F00.md) (function, `0x00916F00`)
- `0x007D2E7B` → [RtlpAddKnownAce](../92/RtlpAddKnownAce_function_00929A20.md) (function, `0x00929A20`)
- `0x007D2EBD` → [RtlpAddKnownAce](../92/RtlpAddKnownAce_function_00929A20.md) (function, `0x00929A20`)
- `0x007D2F28` → [RtlpAddKnownAce](../92/RtlpAddKnownAce_function_00929A20.md) (function, `0x00929A20`)
- `0x007D2F8E` → [RtlpAddKnownAce](../92/RtlpAddKnownAce_function_00929A20.md) (function, `0x00929A20`)
- `0x007D2FE9` → [RtlpAddKnownAce](../92/RtlpAddKnownAce_function_00929A20.md) (function, `0x00929A20`)
- `0x007D3002` → [RtlValidAcl](../92/RtlValidAcl_function_0092A7A0.md) (function, `0x0092A7A0`)
- `0x007D3021` → [RtlSetDaclSecurityDescriptor](../9E/RtlSetDaclSecurityDescriptor_function_009EC210.md) (function, `0x009EC210`)
- `0x007D3038` → [RtlSetOwnerSecurityDescriptor](../91/RtlSetOwnerSecurityDescriptor_function_00916F90.md) (function, `0x00916F90`)
- `0x007D3049` → [RtlValidSecurityDescriptor](../8B/RtlValidSecurityDescriptor_function_008BD3F0.md) (function, `0x008BD3F0`)
- `0x007D3067` → [RtlAbsoluteToSelfRelativeSD](../A1/RtlAbsoluteToSelfRelativeSD_function_00A119B0.md) (function, `0x00A119B0`)
- `0x007D3082` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x007D30A5` → [RtlAbsoluteToSelfRelativeSD](../A1/RtlAbsoluteToSelfRelativeSD_function_00A119B0.md) (function, `0x00A119B0`)
- `0x007D30B5` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x007D30C4` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x007D30D3` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x007D30E2` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x007D30F1` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x007D3100` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x007D3113` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [CMFCheckAccess](CMFCheckAccess_function_007D28B4.md) at `0x007D2995`
- [CMFSystemThreadRoutine](CMFSystemThreadRoutine_function_007D3A70.md) at `0x007D3DB2`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **27**
  - `0x007D2BB6` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x007D2BF7` → [RtlSubAuthoritySid](../../text/45/RtlSubAuthoritySid_function_00456D10.md) (`PAGE` → `.text`)
  - `0x007D2C19` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x007D2C44` → [RtlSubAuthoritySid](../../text/45/RtlSubAuthoritySid_function_00456D10.md) (`PAGE` → `.text`)
  - `0x007D2C57` → [RtlSubAuthoritySid](../../text/45/RtlSubAuthoritySid_function_00456D10.md) (`PAGE` → `.text`)
  - `0x007D2C6C` → [RtlSubAuthoritySid](../../text/45/RtlSubAuthoritySid_function_00456D10.md) (`PAGE` → `.text`)
  - `0x007D2C7D` → [RtlSubAuthoritySid](../../text/45/RtlSubAuthoritySid_function_00456D10.md) (`PAGE` → `.text`)
  - `0x007D2C8E` → [RtlSubAuthoritySid](../../text/45/RtlSubAuthoritySid_function_00456D10.md) (`PAGE` → `.text`)
  - `0x007D2C9F` → [RtlSubAuthoritySid](../../text/45/RtlSubAuthoritySid_function_00456D10.md) (`PAGE` → `.text`)
  - `0x007D2CCE` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x007D2D08` → [RtlSubAuthoritySid](../../text/45/RtlSubAuthoritySid_function_00456D10.md) (`PAGE` → `.text`)
  - `0x007D2D1D` → [RtlSubAuthoritySid](../../text/45/RtlSubAuthoritySid_function_00456D10.md) (`PAGE` → `.text`)
  - `0x007D2D3D` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x007D2D73` → [RtlSubAuthoritySid](../../text/45/RtlSubAuthoritySid_function_00456D10.md) (`PAGE` → `.text`)
  - `0x007D2D85` → [RtlSubAuthoritySid](../../text/45/RtlSubAuthoritySid_function_00456D10.md) (`PAGE` → `.text`)
  - `0x007D2DA6` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x007D2DDC` → [RtlSubAuthoritySid](../../text/45/RtlSubAuthoritySid_function_00456D10.md) (`PAGE` → `.text`)
  - `0x007D2DEF` → [RtlSubAuthoritySid](../../text/45/RtlSubAuthoritySid_function_00456D10.md) (`PAGE` → `.text`)
  - `0x007D2E17` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x007D3082` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x007D30B5` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x007D30C4` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x007D30D3` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x007D30E2` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x007D30F1` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x007D3100` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x007D3113` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007D2B10  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
007D2B15  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
007D2B1A  55                              push rbp
007D2B1B  56                              push rsi
007D2B1C  57                              push rdi
007D2B1D  41 54                           push r12
007D2B1F  41 55                           push r13
007D2B21  41 56                           push r14
007D2B23  41 57                           push r15
007D2B25  48 8B EC                        mov rbp, rsp
007D2B28  48 81 EC 80 00 00 00            sub rsp, 0x80
007D2B2F  4C 8B F1                        mov r14, rcx
007D2B32  66 C7 45 B4 00 05               mov word ptr [rbp - 0x4c], 0x500
007D2B38  33 C9                           xor ecx, ecx
007D2B3A  66 C7 45 54 00 01               mov word ptr [rbp + 0x54], 0x100
007D2B40  33 C0                           xor eax, eax
007D2B42  89 4D B0                        mov dword ptr [rbp - 0x50], ecx
007D2B45  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
007D2B49  0F 57 C0                        xorps xmm0, xmm0
007D2B4C  89 4D 50                        mov dword ptr [rbp + 0x50], ecx
007D2B4F  48 8B FA                        mov rdi, rdx
007D2B52  89 4D 58                        mov dword ptr [rbp + 0x58], ecx
007D2B55  44 8B E1                        mov r12d, ecx
007D2B58  66 C7 45 5C 00 0F               mov word ptr [rbp + 0x5c], 0xf00
007D2B5E  44 8B E9                        mov r13d, ecx
007D2B61  8B F1                           mov esi, ecx
007D2B63  44 8B F9                        mov r15d, ecx
007D2B66  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
007D2B6A  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
007D2B6E  4D 85 F6                        test r14, r14
007D2B71  75 0A                           jne 0x1407d2b7d
007D2B73  BB 0D 00 00 C0                  mov ebx, 0xc000000d
007D2B78  E9 9F 05 00 00                  jmp 0x1407d311c
007D2B7D  49 89 0E                        mov qword ptr [r14], rcx
007D2B80  BA 01 00 00 00                  mov edx, 1
007D2B85  48 8D 4D D0                     lea rcx, [rbp - 0x30]
007D2B89  E8 62 F2 21 00                  call 0x1409f1df0
007D2B8E  B9 00 00 00 C0                  mov ecx, 0xc0000000
007D2B93  8B D8                           mov ebx, eax
007D2B95  23 C1                           and eax, ecx
007D2B97  3B C1                           cmp eax, ecx
007D2B99  0F 84 66 05 00 00               je 0x1407d3105
007D2B9F  B9 01 00 00 00                  mov ecx, 1
007D2BA4  E8 27 79 1F 00                  call 0x1409ca4d0
007D2BA9  8B D0                           mov edx, eax
007D2BAB  B9 00 01 00 00                  mov ecx, 0x100
007D2BB0  41 B8 50 66 6D 63               mov r8d, 0x636d6650
007D2BB6  E8 35 F5 3A 00                  call 0x140b820f0
007D2BBB  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
007D2BBF  48 85 C0                        test rax, rax
007D2BC2  75 0A                           jne 0x1407d2bce
007D2BC4  BB 17 00 00 C0                  mov ebx, 0xc0000017
007D2BC9  E9 3B 05 00 00                  jmp 0x1407d3109
007D2BCE  41 B0 01                        mov r8b, 1
007D2BD1  48 8D 55 50                     lea rdx, [rbp + 0x50]
007D2BD5  48 8B C8                        mov rcx, rax
007D2BD8  E8 43 8B 21 00                  call 0x1409eb720
007D2BDD  B9 00 00 00 C0                  mov ecx, 0xc0000000
007D2BE2  8B D8                           mov ebx, eax
007D2BE4  23 C1                           and eax, ecx
007D2BE6  3B C1                           cmp eax, ecx
007D2BE8  0F 84 D0 04 00 00               je 0x1407d30be
007D2BEE  48 8B 5D C0                     mov rbx, qword ptr [rbp - 0x40]
007D2BF2  33 D2                           xor edx, edx
007D2BF4  48 8B CB                        mov rcx, rbx
007D2BF7  E8 14 41 C8 FF                  call 0x140456d10
007D2BFC  B9 06 00 00 00                  mov ecx, 6
007D2C01  21 30                           and dword ptr [rax], esi
007D2C03  0F B6 5B 01                     movzx ebx, byte ptr [rbx + 1]
007D2C07  E8 C4 78 1F 00                  call 0x1409ca4d0
007D2C0C  8B D0                           mov edx, eax
007D2C0E  B9 00 01 00 00                  mov ecx, 0x100
007D2C13  41 B8 50 66 6D 63               mov r8d, 0x636d6650
007D2C19  E8 D2 F4 3A 00                  call 0x140b820f0
007D2C1E  4C 8B E8                        mov r13, rax
007D2C21  48 85 C0                        test rax, rax
007D2C24  75 0A                           jne 0x1407d2c30
007D2C26  BB 17 00 00 C0                  mov ebx, 0xc0000017
007D2C2B  E9 8E 04 00 00                  jmp 0x1407d30be
007D2C30  41 B0 06                        mov r8b, 6
007D2C33  48 8D 55 B0                     lea rdx, [rbp - 0x50]
007D2C37  49 8B CD                        mov rcx, r13
007D2C3A  E8 E1 8A 21 00                  call 0x1409eb720
007D2C3F  33 D2                           xor edx, edx
007D2C41  49 8B CD                        mov rcx, r13
007D2C44  E8 C7 40 C8 FF                  call 0x140456d10
007D2C49  BA 01 00 00 00                  mov edx, 1
007D2C4E  49 8B CD                        mov rcx, r13
007D2C51  C7 00 50 00 00 00               mov dword ptr [rax], 0x50
007D2C57  E8 B4 40 C8 FF                  call 0x140456d10
007D2C5C  BE 02 00 00 00                  mov esi, 2
007D2C61  49 8B CD                        mov rcx, r13
007D2C64  8B D6                           mov edx, esi
007D2C66  C7 00 B5 89 FB 38               mov dword ptr [rax], 0x38fb89b5
007D2C6C  E8 9F 40 C8 FF                  call 0x140456d10
007D2C71  8D 56 01                        lea edx, [rsi + 1]
007D2C74  49 8B CD                        mov rcx, r13
007D2C77  C7 00 19 84 C2 CB               mov dword ptr [rax], 0xcbc28419
007D2C7D  E8 8E 40 C8 FF                  call 0x140456d10
007D2C82  8D 56 02                        lea edx, [rsi + 2]
007D2C85  49 8B CD                        mov rcx, r13
007D2C88  C7 00 5C 6C 23 6D               mov dword ptr [rax], 0x6d236c5c
007D2C8E  E8 7D 40 C8 FF                  call 0x140456d10
007D2C93  8D 56 03                        lea edx, [rsi + 3]
007D2C96  49 8B CD                        mov rcx, r13
007D2C99  C7 00 57 00 77 6E               mov dword ptr [rax], 0x6e770057
007D2C9F  E8 6C 40 C8 FF                  call 0x140456d10
007D2CA4  8B CE                           mov ecx, esi
007D2CA6  C7 00 C0 02 64 87               mov dword ptr [rax], 0x876402c0
007D2CAC  41 0F B6 45 01                  movzx eax, byte ptr [r13 + 1]
007D2CB1  03 C3                           add eax, ebx
007D2CB3  89 45 50                        mov dword ptr [rbp + 0x50], eax
007D2CB6  E8 15 78 1F 00                  call 0x1409ca4d0
007D2CBB  8B C0                           mov eax, eax
007D2CBD  41 B8 50 66 6D 63               mov r8d, 0x636d6650
007D2CC3  8B D0                           mov edx, eax
007D2CC5  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
007D2CC9  B9 00 01 00 00                  mov ecx, 0x100
007D2CCE  E8 1D F4 3A 00                  call 0x140b820f0
007D2CD3  48 89 45 B8                     mov qword ptr [rbp - 0x48], rax
007D2CD7  48 8B F0                        mov rsi, rax
007D2CDA  48 85 C0                        test rax, rax
007D2CDD  0F 84 43 FF FF FF               je 0x1407d2c26
007D2CE3  41 B0 02                        mov r8b, 2
007D2CE6  48 8D 55 58                     lea rdx, [rbp + 0x58]
007D2CEA  48 8B C8                        mov rcx, rax
007D2CED  E8 2E 8A 21 00                  call 0x1409eb720
007D2CF2  B9 00 00 00 C0                  mov ecx, 0xc0000000
007D2CF7  8B D8                           mov ebx, eax
007D2CF9  23 C1                           and eax, ecx
007D2CFB  3B C1                           cmp eax, ecx
007D2CFD  0F 84 BB 03 00 00               je 0x1407d30be
007D2D03  33 D2                           xor edx, edx
007D2D05  48 8B CE                        mov rcx, rsi
007D2D08  E8 03 40 C8 FF                  call 0x140456d10
007D2D0D  BB 01 00 00 00                  mov ebx, 1
007D2D12  48 8B CE                        mov rcx, rsi
007D2D15  8B D3                           mov edx, ebx
007D2D17  C7 00 02 00 00 00               mov dword ptr [rax], 2
007D2D1D  E8 EE 3F C8 FF                  call 0x140456d10
007D2D22  48 8B 55 C8                     mov rdx, qword ptr [rbp - 0x38]
007D2D26  41 B8 50 66 6D 63               mov r8d, 0x636d6650
007D2D2C  B9 00 01 00 00                  mov ecx, 0x100
007D2D31  89 18                           mov dword ptr [rax], ebx
007D2D33  0F B6 46 01                     movzx eax, byte ptr [rsi + 1]
007D2D37  03 45 50                        add eax, dword ptr [rbp + 0x50]
007D2D3A  89 45 50                        mov dword ptr [rbp + 0x50], eax
007D2D3D  E8 AE F3 3A 00                  call 0x140b820f0
007D2D42  4C 8B F8                        mov r15, rax
007D2D45  48 85 C0                        test rax, rax
007D2D48  0F 84 D8 FE FF FF               je 0x1407d2c26
007D2D4E  41 B0 02                        mov r8b, 2
007D2D51  48 8D 55 58                     lea rdx, [rbp + 0x58]
007D2D55  48 8B C8                        mov rcx, rax
007D2D58  E8 C3 89 21 00                  call 0x1409eb720
007D2D5D  B9 00 00 00 C0                  mov ecx, 0xc0000000
007D2D62  8B D8                           mov ebx, eax
007D2D64  23 C1                           and eax, ecx
007D2D66  3B C1                           cmp eax, ecx
007D2D68  0F 84 50 03 00 00               je 0x1407d30be
007D2D6E  33 D2                           xor edx, edx
007D2D70  49 8B CF                        mov rcx, r15
007D2D73  E8 98 3F C8 FF                  call 0x140456d10
007D2D78  BB 02 00 00 00                  mov ebx, 2
007D2D7D  49 8B CF                        mov rcx, r15
007D2D80  89 18                           mov dword ptr [rax], ebx
007D2D82  8D 53 FF                        lea edx, [rbx - 1]
007D2D85  E8 86 3F C8 FF                  call 0x140456d10
007D2D8A  48 8B 55 C8                     mov rdx, qword ptr [rbp - 0x38]
007D2D8E  41 B8 50 66 6D 63               mov r8d, 0x636d6650
007D2D94  B9 00 01 00 00                  mov ecx, 0x100
007D2D99  89 18                           mov dword ptr [rax], ebx
007D2D9B  41 0F B6 47 01                  movzx eax, byte ptr [r15 + 1]
007D2DA0  03 45 50                        add eax, dword ptr [rbp + 0x50]
007D2DA3  89 45 50                        mov dword ptr [rbp + 0x50], eax
007D2DA6  E8 45 F3 3A 00                  call 0x140b820f0
007D2DAB  4C 8B E0                        mov r12, rax
007D2DAE  48 85 C0                        test rax, rax
007D2DB1  0F 84 6F FE FF FF               je 0x1407d2c26
007D2DB7  44 8A C3                        mov r8b, bl
007D2DBA  48 8D 55 B0                     lea rdx, [rbp - 0x50]
007D2DBE  48 8B C8                        mov rcx, rax
007D2DC1  E8 5A 89 21 00                  call 0x1409eb720
007D2DC6  B9 00 00 00 C0                  mov ecx, 0xc0000000
007D2DCB  8B D8                           mov ebx, eax
007D2DCD  23 C1                           and eax, ecx
007D2DCF  3B C1                           cmp eax, ecx
007D2DD1  0F 84 E7 02 00 00               je 0x1407d30be
007D2DD7  33 D2                           xor edx, edx
007D2DD9  49 8B CC                        mov rcx, r12
007D2DDC  E8 2F 3F C8 FF                  call 0x140456d10
007D2DE1  BA 01 00 00 00                  mov edx, 1
007D2DE6  49 8B CC                        mov rcx, r12
007D2DE9  C7 00 20 00 00 00               mov dword ptr [rax], 0x20
007D2DEF  E8 1C 3F C8 FF                  call 0x140456d10
007D2DF4  B9 00 01 00 00                  mov ecx, 0x100
007D2DF9  41 B8 50 66 6D 63               mov r8d, 0x636d6650
007D2DFF  C7 00 20 02 00 00               mov dword ptr [rax], 0x220
007D2E05  41 0F B6 44 24 01               movzx eax, byte ptr [r12 + 1]
007D2E0B  03 45 50                        add eax, dword ptr [rbp + 0x50]
007D2E0E  8D 1C 85 6C 00 00 00            lea ebx, [rax*4 + 0x6c]
007D2E15  8B D3                           mov edx, ebx
007D2E17  E8 D4 F2 3A 00                  call 0x140b820f0
007D2E1C  4C 8B F0                        mov r14, rax
007D2E1F  48 85 C0                        test rax, rax
007D2E22  75 0A                           jne 0x1407d2e2e
007D2E24  BB 17 00 00 C0                  mov ebx, 0xc0000017
007D2E29  E9 8C 02 00 00                  jmp 0x1407d30ba
007D2E2E  41 B8 02 00 00 00               mov r8d, 2
007D2E34  8B D3                           mov edx, ebx
007D2E36  49 8B CE                        mov rcx, r14
007D2E39  E8 C2 40 14 00                  call 0x140916f00
007D2E3E  B9 00 00 00 C0                  mov ecx, 0xc0000000
007D2E43  8B D8                           mov ebx, eax
007D2E45  23 C1                           and eax, ecx
007D2E47  3B C1                           cmp eax, ecx
007D2E49  0F 84 61 02 00 00               je 0x1407d30b0
007D2E4F  41 B9 00 00 00 10               mov r9d, 0x10000000
007D2E55  48 85 FF                        test rdi, rdi
007D2E58  74 0B                           je 0x1407d2e65
007D2E5A  44 8B 4F 0C                     mov r9d, dword ptr [rdi + 0xc]
007D2E5E  41 81 E1 FF FF FF 0F            and r9d, 0xfffffff
007D2E65  BA 02 00 00 00                  mov edx, 2
007D2E6A  C6 44 24 28 00                  mov byte ptr [rsp + 0x28], 0
007D2E6F  49 8B CE                        mov rcx, r14
007D2E72  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
007D2E77  44 8D 42 01                     lea r8d, [rdx + 1]
007D2E7B  E8 A0 6B 15 00                  call 0x140929a20
007D2E80  B9 00 00 00 C0                  mov ecx, 0xc0000000
007D2E85  8B D8                           mov ebx, eax
007D2E87  23 C1                           and eax, ecx
007D2E89  3B C1                           cmp eax, ecx
007D2E8B  0F 84 1F 02 00 00               je 0x1407d30b0
007D2E91  41 B9 00 00 00 10               mov r9d, 0x10000000
007D2E97  48 85 FF                        test rdi, rdi
007D2E9A  74 0B                           je 0x1407d2ea7
007D2E9C  44 8B 4F 0C                     mov r9d, dword ptr [rdi + 0xc]
007D2EA0  41 81 E1 FF FF FF 0F            and r9d, 0xfffffff
007D2EA7  BA 02 00 00 00                  mov edx, 2
007D2EAC  C6 44 24 28 00                  mov byte ptr [rsp + 0x28], 0
007D2EB1  49 8B CE                        mov rcx, r14
007D2EB4  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
007D2EB9  44 8D 42 01                     lea r8d, [rdx + 1]
007D2EBD  E8 5E 6B 15 00                  call 0x140929a20
007D2EC2  B9 00 00 00 C0                  mov ecx, 0xc0000000
007D2EC7  8B D8                           mov ebx, eax
007D2EC9  23 C1                           and eax, ecx
007D2ECB  3B C1                           cmp eax, ecx
007D2ECD  0F 84 DD 01 00 00               je 0x1407d30b0
007D2ED3  BE 00 00 00 80                  mov esi, 0x80000000
007D2ED8  44 8B CE                        mov r9d, esi
007D2EDB  48 85 FF                        test rdi, rdi
007D2EDE  74 2E                           je 0x1407d2f0e
007D2EE0  44 8B 0F                        mov r9d, dword ptr [rdi]
007D2EE3  44 0B CE                        or r9d, esi
007D2EE6  41 0F BA E1 1E                  bt r9d, 0x1e
007D2EEB  73 04                           jae 0x1407d2ef1
007D2EED  44 0B 4F 04                     or r9d, dword ptr [rdi + 4]
007D2EF1  41 0F BA E1 1D                  bt r9d, 0x1d
007D2EF6  73 04                           jae 0x1407d2efc
007D2EF8  44 0B 4F 08                     or r9d, dword ptr [rdi + 8]
007D2EFC  41 0F BA E1 1C                  bt r9d, 0x1c
007D2F01  73 04                           jae 0x1407d2f07
007D2F03  44 0B 4F 0C                     or r9d, dword ptr [rdi + 0xc]
007D2F07  41 81 E1 FF FF FF 0F            and r9d, 0xfffffff
007D2F0E  48 8B 45 C0                     mov rax, qword ptr [rbp - 0x40]
007D2F12  BA 02 00 00 00                  mov edx, 2
007D2F17  C6 44 24 28 00                  mov byte ptr [rsp + 0x28], 0
007D2F1C  49 8B CE                        mov rcx, r14
007D2F1F  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
007D2F24  44 8D 42 01                     lea r8d, [rdx + 1]
007D2F28  E8 F3 6A 15 00                  call 0x140929a20
007D2F2D  B9 00 00 00 C0                  mov ecx, 0xc0000000
007D2F32  8B D8                           mov ebx, eax
007D2F34  23 C1                           and eax, ecx
007D2F36  3B C1                           cmp eax, ecx
007D2F38  0F 84 6E 01 00 00               je 0x1407d30ac
007D2F3E  44 8B CE                        mov r9d, esi
007D2F41  48 85 FF                        test rdi, rdi
007D2F44  74 2E                           je 0x1407d2f74
007D2F46  44 8B 0F                        mov r9d, dword ptr [rdi]
007D2F49  44 0B CE                        or r9d, esi
007D2F4C  41 0F BA E1 1E                  bt r9d, 0x1e
007D2F51  73 04                           jae 0x1407d2f57
007D2F53  44 0B 4F 04                     or r9d, dword ptr [rdi + 4]
007D2F57  41 0F BA E1 1D                  bt r9d, 0x1d
007D2F5C  73 04                           jae 0x1407d2f62
007D2F5E  44 0B 4F 08                     or r9d, dword ptr [rdi + 8]
007D2F62  41 0F BA E1 1C                  bt r9d, 0x1c
007D2F67  73 04                           jae 0x1407d2f6d
007D2F69  44 0B 4F 0C                     or r9d, dword ptr [rdi + 0xc]
007D2F6D  41 81 E1 FF FF FF 0F            and r9d, 0xfffffff
007D2F74  48 8B 45 B8                     mov rax, qword ptr [rbp - 0x48]
007D2F78  BA 02 00 00 00                  mov edx, 2
007D2F7D  C6 44 24 28 00                  mov byte ptr [rsp + 0x28], 0
007D2F82  49 8B CE                        mov rcx, r14
007D2F85  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
007D2F8A  44 8D 42 01                     lea r8d, [rdx + 1]
007D2F8E  E8 8D 6A 15 00                  call 0x140929a20
007D2F93  B9 00 00 00 C0                  mov ecx, 0xc0000000
007D2F98  8B D8                           mov ebx, eax
007D2F9A  23 C1                           and eax, ecx
007D2F9C  3B C1                           cmp eax, ecx
007D2F9E  0F 84 08 01 00 00               je 0x1407d30ac
007D2FA4  48 85 FF                        test rdi, rdi
007D2FA7  74 27                           je 0x1407d2fd0
007D2FA9  8B 07                           mov eax, dword ptr [rdi]
007D2FAB  0B C6                           or eax, esi
007D2FAD  8B F0                           mov esi, eax
007D2FAF  0F BA E0 1E                     bt eax, 0x1e
007D2FB3  73 03                           jae 0x1407d2fb8
007D2FB5  0B 77 04                        or esi, dword ptr [rdi + 4]
007D2FB8  0F BA E6 1D                     bt esi, 0x1d
007D2FBC  73 03                           jae 0x1407d2fc1
007D2FBE  0B 77 08                        or esi, dword ptr [rdi + 8]
007D2FC1  0F BA E6 1C                     bt esi, 0x1c
007D2FC5  73 03                           jae 0x1407d2fca
007D2FC7  0B 77 0C                        or esi, dword ptr [rdi + 0xc]
007D2FCA  81 E6 FF FF FF 0F               and esi, 0xfffffff
007D2FD0  BA 02 00 00 00                  mov edx, 2
007D2FD5  C6 44 24 28 00                  mov byte ptr [rsp + 0x28], 0
007D2FDA  44 8B CE                        mov r9d, esi
007D2FDD  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
007D2FE2  49 8B CE                        mov rcx, r14
007D2FE5  44 8D 42 01                     lea r8d, [rdx + 1]
007D2FE9  E8 32 6A 15 00                  call 0x140929a20
007D2FEE  BF 00 00 00 C0                  mov edi, 0xc0000000
007D2FF3  8B D8                           mov ebx, eax
007D2FF5  23 C7                           and eax, edi
007D2FF7  3B C7                           cmp eax, edi
007D2FF9  0F 84 AD 00 00 00               je 0x1407d30ac
007D2FFF  49 8B CE                        mov rcx, r14
007D3002  E8 99 77 15 00                  call 0x14092a7a0
007D3007  84 C0                           test al, al
007D3009  75 0A                           jne 0x1407d3015
007D300B  BB 77 00 00 C0                  mov ebx, 0xc0000077
007D3010  E9 97 00 00 00                  jmp 0x1407d30ac
007D3015  45 33 C9                        xor r9d, r9d
007D3018  48 8D 4D D0                     lea rcx, [rbp - 0x30]
007D301C  4D 8B C6                        mov r8, r14
007D301F  B2 01                           mov dl, 1
007D3021  E8 EA 91 21 00                  call 0x1409ec210
007D3026  8B D8                           mov ebx, eax
007D3028  23 C7                           and eax, edi
007D302A  3B C7                           cmp eax, edi
007D302C  74 7E                           je 0x1407d30ac
007D302E  45 33 C0                        xor r8d, r8d
007D3031  48 8D 4D D0                     lea rcx, [rbp - 0x30]
007D3035  49 8B D5                        mov rdx, r13
007D3038  E8 53 3F 14 00                  call 0x140916f90
007D303D  8B D8                           mov ebx, eax
007D303F  23 C7                           and eax, edi
007D3041  3B C7                           cmp eax, edi
007D3043  74 67                           je 0x1407d30ac
007D3045  48 8D 4D D0                     lea rcx, [rbp - 0x30]
007D3049  E8 A2 A3 0E 00                  call 0x1408bd3f0
007D304E  84 C0                           test al, al
007D3050  75 07                           jne 0x1407d3059
007D3052  BB 79 00 00 C0                  mov ebx, 0xc0000079
007D3057  EB 53                           jmp 0x1407d30ac
007D3059  83 65 50 00                     and dword ptr [rbp + 0x50], 0
007D305D  4C 8D 45 50                     lea r8, [rbp + 0x50]
007D3061  33 D2                           xor edx, edx
007D3063  48 8D 4D D0                     lea rcx, [rbp - 0x30]
007D3067  E8 44 E9 23 00                  call 0x140a119b0
007D306C  8B D8                           mov ebx, eax
007D306E  8B 45 50                        mov eax, dword ptr [rbp + 0x50]
007D3071  85 C0                           test eax, eax
007D3073  74 37                           je 0x1407d30ac
007D3075  8B D0                           mov edx, eax
007D3077  B9 00 01 00 00                  mov ecx, 0x100
007D307C  41 B8 50 66 6D 63               mov r8d, 0x636d6650
007D3082  E8 69 F0 3A 00                  call 0x140b820f0
007D3087  48 8B 4D 40                     mov rcx, qword ptr [rbp + 0x40]
007D308B  48 89 01                        mov qword ptr [rcx], rax
007D308E  48 85 C0                        test rax, rax
007D3091  75 07                           jne 0x1407d309a
007D3093  BB 17 00 00 C0                  mov ebx, 0xc0000017
007D3098  EB 12                           jmp 0x1407d30ac
007D309A  4C 8D 45 50                     lea r8, [rbp + 0x50]
007D309E  48 8B D0                        mov rdx, rax
007D30A1  48 8D 4D D0                     lea rcx, [rbp - 0x30]
007D30A5  E8 06 E9 23 00                  call 0x140a119b0
007D30AA  8B D8                           mov ebx, eax
007D30AC  48 8B 75 B8                     mov rsi, qword ptr [rbp - 0x48]
007D30B0  33 D2                           xor edx, edx
007D30B2  49 8B CE                        mov rcx, r14
007D30B5  E8 B6 F7 3A 00                  call 0x140b82870
007D30BA  4C 8B 75 40                     mov r14, qword ptr [rbp + 0x40]
007D30BE  48 8B 4D C0                     mov rcx, qword ptr [rbp - 0x40]
007D30C2  33 D2                           xor edx, edx
007D30C4  E8 A7 F7 3A 00                  call 0x140b82870
007D30C9  4D 85 ED                        test r13, r13
007D30CC  74 0A                           je 0x1407d30d8
007D30CE  33 D2                           xor edx, edx
007D30D0  49 8B CD                        mov rcx, r13
007D30D3  E8 98 F7 3A 00                  call 0x140b82870
007D30D8  48 85 F6                        test rsi, rsi
007D30DB  74 0A                           je 0x1407d30e7
007D30DD  33 D2                           xor edx, edx
007D30DF  48 8B CE                        mov rcx, rsi
007D30E2  E8 89 F7 3A 00                  call 0x140b82870
007D30E7  4D 85 FF                        test r15, r15
007D30EA  74 0A                           je 0x1407d30f6
007D30EC  33 D2                           xor edx, edx
007D30EE  49 8B CF                        mov rcx, r15
007D30F1  E8 7A F7 3A 00                  call 0x140b82870
007D30F6  4D 85 E4                        test r12, r12
007D30F9  74 0A                           je 0x1407d3105
007D30FB  33 D2                           xor edx, edx
007D30FD  49 8B CC                        mov rcx, r12
007D3100  E8 6B F7 3A 00                  call 0x140b82870
007D3105  85 DB                           test ebx, ebx
007D3107  79 13                           jns 0x1407d311c
007D3109  49 8B 0E                        mov rcx, qword ptr [r14]
007D310C  48 85 C9                        test rcx, rcx
007D310F  74 0B                           je 0x1407d311c
007D3111  33 D2                           xor edx, edx
007D3113  E8 58 F7 3A 00                  call 0x140b82870
007D3118  49 83 26 00                     and qword ptr [r14], 0
007D311C  8B C3                           mov eax, ebx
007D311E  48 8B 9C 24 C8 00 00 00         mov rbx, qword ptr [rsp + 0xc8]
007D3126  48 81 C4 80 00 00 00            add rsp, 0x80
007D312D  41 5F                           pop r15
007D312F  41 5E                           pop r14
007D3131  41 5D                           pop r13
007D3133  41 5C                           pop r12
007D3135  5F                              pop rdi
007D3136  5E                              pop rsi
007D3137  5D                              pop rbp
007D3138  C3                              ret
007D3139  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CMFCreateSecurityDescriptor(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int16 v_stack_m84;
    unsigned int v_stack_m88;
    unsigned __int8 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p18;
    unsigned __int16 v_stack_p1C;
    unsigned int v_stack_p20;
    unsigned __int16 v_stack_p24;
    unsigned __int64 v_stack_p8;

    v_stack_p10 = v_rbx;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (128);
    v_stack_m84 = 0x500ULL;
    a1 = 0;
    v_stack_p1C = 256;
    result = 0;
    v_stack_m88 = 0;
    v_stack_m48 = 0;
    v_stack_p18 = 0;
    v_stack_p20 = 0;
    v_stack_p24 = 0xF00ULL;
    v_stack_m68 = v_xmm0;
    v_stack_m58 = v_xmm0;
    if (0 != 0) goto loc_007D2B7D;
    goto loc_007D311C;
loc_007D2B7D:
    *(unsigned __int64 *)(a1) = 0;
    result = RtlCreateSecurityDescriptor(v_stack_m68, 1, a3, a4);
    result = (unsigned int)((result) & ((unsigned int)((unsigned int)(0xC0000000ULL))));
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0xC0000000ULL)))) goto loc_007D3105;
    result = RtlLengthRequiredSid(1, 1, a3, a4);
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(result)), (unsigned int)(0x636D6650ULL), a4);
    v_stack_m78 = result;
    if (result != 0) goto loc_007D2BCE;
    goto loc_007D3109;
loc_007D2BCE:
    result = RtlInitializeSid(result, v_stack_p18, 1, a4);
    result = (unsigned int)((result) & ((unsigned int)((unsigned int)(0xC0000000ULL))));
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0xC0000000ULL)))) goto loc_007D30BE;
    a2 = 0;
    result = RtlSubAuthoritySid(v_stack_m78, a2, 1, a4);
    result = RtlLengthRequiredSid(6, a2, 1, a4);
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(result)), (unsigned int)(0x636D6650ULL), a4);
    if (result != 0) goto loc_007D2C30;
loc_007D2C26:
    goto loc_007D30BE;
loc_007D2C30:
    result = RtlInitializeSid(result, v_stack_m88, 6, a4);
    a2 = 0;
    result = RtlSubAuthoritySid(result, a2, 6, a4);
    *(unsigned int *)(result) = 80;
    result = RtlSubAuthoritySid(result, 1, 6, a4);
    *(unsigned int *)(result) = 0x38FB89B5ULL;
    result = RtlSubAuthoritySid(result, 2, 6, a4);
    *(unsigned int *)(result) = 0xCBC28419ULL;
    result = RtlSubAuthoritySid(result, 2 + 1, 6, a4);
    *(unsigned int *)(result) = 0x6D236C5CULL;
    result = RtlSubAuthoritySid(result, 2 + 2, 6, a4);
    *(unsigned int *)(result) = 0x6E770057ULL;
    result = RtlSubAuthoritySid(result, 2 + 3, 6, a4);
    *(unsigned int *)(result) = 0x876402C0ULL;
    result = (unsigned int)((*(unsigned __int8 *)(result + 1)) + ((unsigned int)((unsigned int)(0xC0000017ULL))));
    v_stack_p18 = (unsigned int)(result);
    result = RtlLengthRequiredSid(2, 2 + 3, 6, a4);
    v_stack_m70 = (unsigned int)((unsigned int)(result));
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)(0x636D6650ULL), a4);
    v_stack_m80 = result;
    if (result == 0) goto loc_007D2C26;
    result = RtlInitializeSid(result, v_stack_p20, 2, a4);
    result = (unsigned int)((result) & ((unsigned int)((unsigned int)(0xC0000000ULL))));
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0xC0000000ULL)))) goto loc_007D30BE;
    a2 = 0;
    result = RtlSubAuthoritySid(result, a2, 2, a4);
    *(unsigned int *)(result) = 2;
    result = RtlSubAuthoritySid(result, 1, 2, a4);
    *(unsigned int *)(result) = 1;
    result = (unsigned int)((*(unsigned __int8 *)(result + 1)) + (v_stack_p18));
    v_stack_p18 = (unsigned int)(result);
    result = ExAllocatePool2(256, v_stack_m70, (unsigned int)(0x636D6650ULL), a4);
    if (result == 0) goto loc_007D2C26;
    result = RtlInitializeSid(result, v_stack_p20, 2, a4);
    result = (unsigned int)((result) & ((unsigned int)((unsigned int)(0xC0000000ULL))));
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0xC0000000ULL)))) goto loc_007D30BE;
    a2 = 0;
    result = RtlSubAuthoritySid(result, a2, 2, a4);
    *(unsigned int *)(result) = 2;
    result = RtlSubAuthoritySid(result, 2 - 1, 2, a4);
    *(unsigned int *)(result) = 2;
    result = (unsigned int)((*(unsigned __int8 *)(result + 1)) + (v_stack_p18));
    v_stack_p18 = (unsigned int)(result);
    result = ExAllocatePool2(256, v_stack_m70, (unsigned int)(0x636D6650ULL), a4);
    if (result == 0) goto loc_007D2C26;
    result = RtlInitializeSid(result, v_stack_m88, 2, a4);
    result = (unsigned int)((result) & ((unsigned int)((unsigned int)(0xC0000000ULL))));
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0xC0000000ULL)))) goto loc_007D30BE;
    a2 = 0;
    result = RtlSubAuthoritySid(result, a2, 2, a4);
    *(unsigned int *)(result) = 32;
    result = RtlSubAuthoritySid(result, 1, 2, a4);
    *(unsigned int *)(result) = 544;
    result = (unsigned int)((*(unsigned __int8 *)(result + 1)) + (v_stack_p18));
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(result * 4 + 108)), (unsigned int)(0x636D6650ULL), a4);
    if (result != 0) goto loc_007D2E2E;
    goto loc_007D30BA;
loc_007D2E2E:
    result = RtlCreateAcl(result, (unsigned int)((unsigned int)((unsigned int)(0xC0000017ULL))), 2, a4);
    result = (unsigned int)((result) & ((unsigned int)((unsigned int)(0xC0000000ULL))));
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0xC0000000ULL)))) goto loc_007D30B0;
    if (0 != 0) {
        a4 = *(unsigned int *)(a2 + 12);
        a4 = (unsigned int)((a4) & (0xFFFFFFFULL));
    }
    v_stack_m90 = 0;
    v_stack_m98 = result;
    result = RtlpAddKnownAce(result, 2, 2 + 1, a4);
    result = (unsigned int)((result) & ((unsigned int)((unsigned int)(0xC0000000ULL))));
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0xC0000000ULL)))) goto loc_007D30B0;
    if (0 != 0) {
        a4 = *(unsigned int *)(a2 + 12);
        a4 = (unsigned int)((a4) & (0xFFFFFFFULL));
    }
    v_stack_m90 = 0;
    v_stack_m98 = result;
    result = RtlpAddKnownAce(result, 2, 2 + 1, a4);
    result = (unsigned int)((result) & ((unsigned int)((unsigned int)(0xC0000000ULL))));
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0xC0000000ULL)))) goto loc_007D30B0;
    if (0 == 0) goto loc_007D2F0E;
    a4 = (unsigned int)(((unsigned int)(*(unsigned int *)(a2))) | ((unsigned int)((unsigned int)(0x80000000ULL))));
    if (!(condition_is_above_or_equal)) {
        a4 = (unsigned int)((a4) | (*(unsigned int *)(a2 + 4)));
    }
    if (!(condition_is_above_or_equal)) {
        a4 = (unsigned int)((a4) | (*(unsigned int *)(a2 + 8)));
    }
    if (!(condition_is_above_or_equal)) {
        a4 = (unsigned int)((a4) | (*(unsigned int *)(a2 + 12)));
    }
    a4 = (unsigned int)((a4) & (0xFFFFFFFULL));
loc_007D2F0E:
    v_stack_m90 = 0;
    v_stack_m98 = v_stack_m78;
    result = RtlpAddKnownAce(result, 2, 2 + 1, a4);
    result = (unsigned int)((result) & ((unsigned int)((unsigned int)(0xC0000000ULL))));
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0xC0000000ULL)))) goto loc_007D30AC;
    if (0 == 0) goto loc_007D2F74;
    a4 = (unsigned int)(((unsigned int)(*(unsigned int *)(a2))) | ((unsigned int)((unsigned int)(0x80000000ULL))));
    if (!(condition_is_above_or_equal)) {
        a4 = (unsigned int)((a4) | (*(unsigned int *)(a2 + 4)));
    }
    if (!(condition_is_above_or_equal)) {
        a4 = (unsigned int)((a4) | (*(unsigned int *)(a2 + 8)));
    }
    if (!(condition_is_above_or_equal)) {
        a4 = (unsigned int)((a4) | (*(unsigned int *)(a2 + 12)));
    }
    a4 = (unsigned int)((a4) & (0xFFFFFFFULL));
loc_007D2F74:
    v_stack_m90 = 0;
    v_stack_m98 = v_stack_m80;
    result = RtlpAddKnownAce(result, 2, 2 + 1, a4);
    result = (unsigned int)((result) & ((unsigned int)((unsigned int)(0xC0000000ULL))));
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0xC0000000ULL)))) goto loc_007D30AC;
    if (0 == 0) goto loc_007D2FD0;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2))) | ((unsigned int)((unsigned int)(0x80000000ULL))));
    v_rsi = (unsigned int)((unsigned int)(result));
    if (!(condition_is_above_or_equal)) {
        v_rsi = (unsigned int)(((unsigned int)((unsigned int)(result))) | (*(unsigned int *)(a2 + 4)));
    }
    if (!(condition_is_above_or_equal)) {
        v_rsi = (unsigned int)((v_rsi) | (*(unsigned int *)(a2 + 8)));
    }
    if (!(condition_is_above_or_equal)) {
        v_rsi = (unsigned int)((v_rsi) | (*(unsigned int *)(a2 + 12)));
    }
    v_rsi = (unsigned int)((v_rsi) & (0xFFFFFFFULL));
loc_007D2FD0:
    v_stack_m90 = 0;
    v_stack_m98 = result;
    result = RtlpAddKnownAce(result, 2, 2 + 1, (unsigned int)((unsigned int)(v_rsi)));
    result = (unsigned int)((result) & ((unsigned int)((unsigned int)(0xC0000000ULL))));
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0xC0000000ULL)))) goto loc_007D30AC;
    result = RtlValidAcl(result, 2, 2 + 1, (unsigned int)((unsigned int)(v_rsi)));
    if ((unsigned __int8)(result) != 0) goto loc_007D3015;
    goto loc_007D30AC;
loc_007D3015:
    a4 = 0;
    result = RtlSetDaclSecurityDescriptor(v_stack_m68, 1, result, a4);
    result = (unsigned int)((result) & ((unsigned int)((unsigned int)(0xC0000000ULL))));
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0xC0000000ULL)))) goto loc_007D30AC;
    a3 = 0;
    result = RtlSetOwnerSecurityDescriptor(v_stack_m68, result, a3, a4);
    result = (unsigned int)((result) & ((unsigned int)((unsigned int)(0xC0000000ULL))));
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0xC0000000ULL)))) goto loc_007D30AC;
    result = RtlValidSecurityDescriptor(v_stack_m68, result, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_007D3059;
    goto loc_007D30AC;
loc_007D3059:
    a2 = 0;
    result = RtlAbsoluteToSelfRelativeSD(v_stack_m68, a2, v_stack_p18, a4);
    if ((unsigned int)((unsigned int)(v_stack_p18)) == 0) goto loc_007D30AC;
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)((unsigned int)(v_stack_p18))), (unsigned int)(0x636D6650ULL), a4);
    *(unsigned __int64 *)(v_stack_p8) = result;
    if (result != 0) goto loc_007D309A;
    goto loc_007D30AC;
loc_007D309A:
    result = RtlAbsoluteToSelfRelativeSD(v_stack_m68, result, v_stack_p18, a4);
loc_007D30AC:
loc_007D30B0:
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, v_stack_p18, a4);
loc_007D30BA:
loc_007D30BE:
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m78, a2, v_stack_p18, a4);
    if (result != 0) {
        a2 = 0;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, v_stack_p18, a4);
    }
    if (v_stack_m80 != 0) {
        a2 = 0;
        a1 = v_stack_m80;
        result = ExFreePoolWithTag(a1, a2, v_stack_p18, a4);
    }
    if (result != 0) {
        a2 = 0;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, v_stack_p18, a4);
    }
    if (result != 0) {
        a2 = 0;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, v_stack_p18, a4);
    }
    if (!sign_flag) goto loc_007D311C;
loc_007D3109:
    if (*(unsigned __int64 *)(v_stack_p8) != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(v_stack_p8), a2, v_stack_p18, a4);
    }
    v_rsp = (v_rsp) + (128);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
}
```

## 5. (Beta) C Style

```c
int64_t CMFCreateSecurityDescriptor(int64_t Arg1, int64_t Arg2)
{
    int64_t result;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m58;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint16_t v_stack_m84;
    uint32_t v_stack_m88;
    uint8_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_p10;
    uint32_t v_stack_p18;
    uint16_t v_stack_p1C;
    uint32_t v_stack_p20;
    uint16_t v_stack_p24;
    uint64_t v_stack_p8;

    v_stack_p10 = local_rbx;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (128);
    v_stack_m84 = 0x500ULL;
    Arg1 = 0;
    v_stack_p1C = 256;
    result = 0;
    v_stack_m88 = 0;
    v_stack_m48 = 0;
    v_stack_p18 = 0;
    v_stack_p20 = 0;
    v_stack_p24 = 0xF00ULL;
    v_stack_m68 = v_xmm0;
    v_stack_m58 = v_xmm0;
    if (0 != 0) goto loc_007D2B7D;
    goto loc_007D311C;
loc_007D2B7D:
    *(uint64_t *)(Arg1) = 0;
    result = RtlCreateSecurityDescriptor(v_stack_m68, 1, a3, a4);
    result = (uint32_t)((result) & ((uint32_t)((uint32_t)(0xC0000000ULL))));
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0xC0000000ULL)))) goto loc_007D3105;
    result = RtlLengthRequiredSid(1, 1, a3, a4);
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(result)), (uint32_t)(0x636D6650ULL), a4);
    v_stack_m78 = result;
    if (result != 0) goto loc_007D2BCE;
    goto loc_007D3109;
loc_007D2BCE:
    result = RtlInitializeSid(result, v_stack_p18, 1, a4);
    result = (uint32_t)((result) & ((uint32_t)((uint32_t)(0xC0000000ULL))));
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0xC0000000ULL)))) goto loc_007D30BE;
    Arg2 = 0;
    result = RtlSubAuthoritySid(v_stack_m78, Arg2, 1, a4);
    result = RtlLengthRequiredSid(6, Arg2, 1, a4);
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(result)), (uint32_t)(0x636D6650ULL), a4);
    if (result != 0) goto loc_007D2C30;
loc_007D2C26:
    goto loc_007D30BE;
loc_007D2C30:
    result = RtlInitializeSid(result, v_stack_m88, 6, a4);
    Arg2 = 0;
    result = RtlSubAuthoritySid(result, Arg2, 6, a4);
    *(uint32_t *)(result) = 80;
    result = RtlSubAuthoritySid(result, 1, 6, a4);
    *(uint32_t *)(result) = 0x38FB89B5ULL;
    result = RtlSubAuthoritySid(result, 2, 6, a4);
    *(uint32_t *)(result) = 0xCBC28419ULL;
    result = RtlSubAuthoritySid(result, 2 + 1, 6, a4);
    *(uint32_t *)(result) = 0x6D236C5CULL;
    result = RtlSubAuthoritySid(result, 2 + 2, 6, a4);
    *(uint32_t *)(result) = 0x6E770057ULL;
    result = RtlSubAuthoritySid(result, 2 + 3, 6, a4);
    *(uint32_t *)(result) = 0x876402C0ULL;
    result = (uint32_t)((*(uint8_t *)(result + 0x1)) + ((uint32_t)((uint32_t)(0xC0000017ULL))));
    v_stack_p18 = (uint32_t)(result);
    result = RtlLengthRequiredSid(2, 2 + 3, 6, a4);
    v_stack_m70 = (uint32_t)((uint32_t)(result));
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)(0x636D6650ULL), a4);
    v_stack_m80 = result;
    if (result == 0) goto loc_007D2C26;
    result = RtlInitializeSid(result, v_stack_p20, 2, a4);
    result = (uint32_t)((result) & ((uint32_t)((uint32_t)(0xC0000000ULL))));
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0xC0000000ULL)))) goto loc_007D30BE;
    Arg2 = 0;
    result = RtlSubAuthoritySid(result, Arg2, 2, a4);
    *(uint32_t *)(result) = 2;
    result = RtlSubAuthoritySid(result, 1, 2, a4);
    *(uint32_t *)(result) = 1;
    result = (uint32_t)((*(uint8_t *)(result + 0x1)) + (v_stack_p18));
    v_stack_p18 = (uint32_t)(result);
    result = ExAllocatePool2(256, v_stack_m70, (uint32_t)(0x636D6650ULL), a4);
    if (result == 0) goto loc_007D2C26;
    result = RtlInitializeSid(result, v_stack_p20, 2, a4);
    result = (uint32_t)((result) & ((uint32_t)((uint32_t)(0xC0000000ULL))));
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0xC0000000ULL)))) goto loc_007D30BE;
    Arg2 = 0;
    result = RtlSubAuthoritySid(result, Arg2, 2, a4);
    *(uint32_t *)(result) = 2;
    result = RtlSubAuthoritySid(result, 2 - 1, 2, a4);
    *(uint32_t *)(result) = 2;
    result = (uint32_t)((*(uint8_t *)(result + 0x1)) + (v_stack_p18));
    v_stack_p18 = (uint32_t)(result);
    result = ExAllocatePool2(256, v_stack_m70, (uint32_t)(0x636D6650ULL), a4);
    if (result == 0) goto loc_007D2C26;
    result = RtlInitializeSid(result, v_stack_m88, 2, a4);
    result = (uint32_t)((result) & ((uint32_t)((uint32_t)(0xC0000000ULL))));
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0xC0000000ULL)))) goto loc_007D30BE;
    Arg2 = 0;
    result = RtlSubAuthoritySid(result, Arg2, 2, a4);
    *(uint32_t *)(result) = 32;
    result = RtlSubAuthoritySid(result, 1, 2, a4);
    *(uint32_t *)(result) = 544;
    result = (uint32_t)((*(uint8_t *)(result + 0x1)) + (v_stack_p18));
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(result * 4 + 108)), (uint32_t)(0x636D6650ULL), a4);
    if (result != 0) goto loc_007D2E2E;
    goto loc_007D30BA;
loc_007D2E2E:
    result = RtlCreateAcl(result, (uint32_t)((uint32_t)((uint32_t)(0xC0000017ULL))), 2, a4);
    result = (uint32_t)((result) & ((uint32_t)((uint32_t)(0xC0000000ULL))));
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0xC0000000ULL)))) goto loc_007D30B0;
    if (0 != 0) {
        a4 = *(uint32_t *)(Arg2 + 0xC);
        a4 = (uint32_t)((a4) & (0xFFFFFFFULL));
    }
    v_stack_m90 = 0;
    v_stack_m98 = result;
    result = RtlpAddKnownAce(result, 2, 2 + 1, a4);
    result = (uint32_t)((result) & ((uint32_t)((uint32_t)(0xC0000000ULL))));
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0xC0000000ULL)))) goto loc_007D30B0;
    if (0 != 0) {
        a4 = *(uint32_t *)(Arg2 + 0xC);
        a4 = (uint32_t)((a4) & (0xFFFFFFFULL));
    }
    v_stack_m90 = 0;
    v_stack_m98 = result;
    result = RtlpAddKnownAce(result, 2, 2 + 1, a4);
    result = (uint32_t)((result) & ((uint32_t)((uint32_t)(0xC0000000ULL))));
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0xC0000000ULL)))) goto loc_007D30B0;
    if (0 == 0) goto loc_007D2F0E;
    a4 = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg2))) | ((uint32_t)((uint32_t)(0x80000000ULL))));
    if (!(condition_is_above_or_equal)) {
        a4 = (uint32_t)((a4) | (*(uint32_t *)(Arg2 + 0x4)));
    }
    if (!(condition_is_above_or_equal)) {
        a4 = (uint32_t)((a4) | (*(uint32_t *)(Arg2 + 0x8)));
    }
    if (!(condition_is_above_or_equal)) {
        a4 = (uint32_t)((a4) | (*(uint32_t *)(Arg2 + 0xC)));
    }
    a4 = (uint32_t)((a4) & (0xFFFFFFFULL));
loc_007D2F0E:
    v_stack_m90 = 0;
    v_stack_m98 = v_stack_m78;
    result = RtlpAddKnownAce(result, 2, 2 + 1, a4);
    result = (uint32_t)((result) & ((uint32_t)((uint32_t)(0xC0000000ULL))));
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0xC0000000ULL)))) goto loc_007D30AC;
    if (0 == 0) goto loc_007D2F74;
    a4 = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg2))) | ((uint32_t)((uint32_t)(0x80000000ULL))));
    if (!(condition_is_above_or_equal)) {
        a4 = (uint32_t)((a4) | (*(uint32_t *)(Arg2 + 0x4)));
    }
    if (!(condition_is_above_or_equal)) {
        a4 = (uint32_t)((a4) | (*(uint32_t *)(Arg2 + 0x8)));
    }
    if (!(condition_is_above_or_equal)) {
        a4 = (uint32_t)((a4) | (*(uint32_t *)(Arg2 + 0xC)));
    }
    a4 = (uint32_t)((a4) & (0xFFFFFFFULL));
loc_007D2F74:
    v_stack_m90 = 0;
    v_stack_m98 = v_stack_m80;
    result = RtlpAddKnownAce(result, 2, 2 + 1, a4);
    result = (uint32_t)((result) & ((uint32_t)((uint32_t)(0xC0000000ULL))));
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0xC0000000ULL)))) goto loc_007D30AC;
    if (0 == 0) goto loc_007D2FD0;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg2))) | ((uint32_t)((uint32_t)(0x80000000ULL))));
    local_rsi = (uint32_t)((uint32_t)(result));
    if (!(condition_is_above_or_equal)) {
        local_rsi = (uint32_t)(((uint32_t)((uint32_t)(result))) | (*(uint32_t *)(Arg2 + 0x4)));
    }
    if (!(condition_is_above_or_equal)) {
        local_rsi = (uint32_t)((local_rsi) | (*(uint32_t *)(Arg2 + 0x8)));
    }
    if (!(condition_is_above_or_equal)) {
        local_rsi = (uint32_t)((local_rsi) | (*(uint32_t *)(Arg2 + 0xC)));
    }
    local_rsi = (uint32_t)((local_rsi) & (0xFFFFFFFULL));
loc_007D2FD0:
    v_stack_m90 = 0;
    v_stack_m98 = result;
    result = RtlpAddKnownAce(result, 2, 2 + 1, (uint32_t)((uint32_t)(local_rsi)));
    result = (uint32_t)((result) & ((uint32_t)((uint32_t)(0xC0000000ULL))));
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0xC0000000ULL)))) goto loc_007D30AC;
    result = RtlValidAcl(result, 2, 2 + 1, (uint32_t)((uint32_t)(local_rsi)));
    if ((uint8_t)(result) != 0) goto loc_007D3015;
    goto loc_007D30AC;
loc_007D3015:
    a4 = 0;
    result = RtlSetDaclSecurityDescriptor(v_stack_m68, 1, result, a4);
    result = (uint32_t)((result) & ((uint32_t)((uint32_t)(0xC0000000ULL))));
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0xC0000000ULL)))) goto loc_007D30AC;
    a3 = 0;
    result = RtlSetOwnerSecurityDescriptor(v_stack_m68, result, a3, a4);
    result = (uint32_t)((result) & ((uint32_t)((uint32_t)(0xC0000000ULL))));
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0xC0000000ULL)))) goto loc_007D30AC;
    result = RtlValidSecurityDescriptor(v_stack_m68, result, a3, a4);
    if ((uint8_t)(result) != 0) goto loc_007D3059;
    goto loc_007D30AC;
loc_007D3059:
    Arg2 = 0;
    result = RtlAbsoluteToSelfRelativeSD(v_stack_m68, Arg2, v_stack_p18, a4);
    if ((uint32_t)((uint32_t)(v_stack_p18)) == 0) goto loc_007D30AC;
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)((uint32_t)(v_stack_p18))), (uint32_t)(0x636D6650ULL), a4);
    *(uint64_t *)(v_stack_p8) = result;
    if (result != 0) goto loc_007D309A;
    goto loc_007D30AC;
loc_007D309A:
    result = RtlAbsoluteToSelfRelativeSD(v_stack_m68, result, v_stack_p18, a4);
loc_007D30AC:
loc_007D30B0:
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, v_stack_p18, a4);
loc_007D30BA:
loc_007D30BE:
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_m78, Arg2, v_stack_p18, a4);
    if (result != 0) {
        Arg2 = 0;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, v_stack_p18, a4);
    }
    if (v_stack_m80 != 0) {
        Arg2 = 0;
        Arg1 = v_stack_m80;
        result = ExFreePoolWithTag(Arg1, Arg2, v_stack_p18, a4);
    }
    if (result != 0) {
        Arg2 = 0;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, v_stack_p18, a4);
    }
    if (result != 0) {
        Arg2 = 0;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, v_stack_p18, a4);
    }
    if (!sign_flag) goto loc_007D311C;
loc_007D3109:
    if (*(uint64_t *)(v_stack_p8) != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(*(uint64_t *)(v_stack_p8), Arg2, v_stack_p18, a4);
    }
    local_rsp = (local_rsp) + (128);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007D2B10&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
