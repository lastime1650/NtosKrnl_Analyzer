# _CmOpenDeviceInterfaceRegKeyWorker

- RVA: `0x008F2B48`–`0x008F31EE` (길이 `1,702` bytes)
- VA: `0x00000001408F2B48`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00087580`
- 디코드: `430`개 명령, `1,702/1,702` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **19**; 고유 호출 대상: **14**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x008F2BDA` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008F2C0E` → [_CmGetDeviceInterfaceRegKeyPath](_CmGetDeviceInterfaceRegKeyPath_function_008F2010.md) (function, `0x008F2010`)
- `0x008F2C3A` → [RtlInitUnicodeStringEx](../../text/46/RtlInitUnicodeStringEx_function_00463960.md) (function, `0x00463960`)
- `0x008F2C63` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (function, `0x002FE1F0`)
- `0x008F2D01` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (function, `0x002FE1F0`)
- `0x008F2D70` → [_PnpCtxGetCachedNodeBaseKey](../8E/_PnpCtxGetCachedNodeBaseKey_function_008EF9C0.md) (function, `0x008EF9C0`)
- `0x008F2DBA` → [_RegRtlOpenKeyTransacted](../8E/_RegRtlOpenKeyTransacted_function_008EF810.md) (function, `0x008EF810`)
- `0x008F2E13` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008F2F89` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008F2FC4` → [SysCtxRegOpenCurrentUserKey](SysCtxRegOpenCurrentUserKey_function_008F455C.md) (function, `0x008F455C`)
- `0x008F304F` → [CmGetDeviceInterfaceRegKeySecurityDescriptor](../A9/CmGetDeviceInterfaceRegKeySecurityDescriptor_function_00A9EAC0.md) (function, `0x00A9EAC0`)
- `0x008F3097` → [PnpCtxRegCreateTree](../93/PnpCtxRegCreateTree_function_00931CA0.md) (function, `0x00931CA0`)
- `0x008F30E5` → [RtlPrefixUnicodeString](RtlPrefixUnicodeString_function_008F4F70.md) (function, `0x008F4F70`)
- `0x008F3174` → [_CmOpenDeviceInterfaceRegKey](_CmOpenDeviceInterfaceRegKey_function_008F31F4.md) (function, `0x008F31F4`)
- `0x008F319F` → [PnpCtxRegOpenKey](../8E/PnpCtxRegOpenKey_function_008EF7B8.md) (function, `0x008EF7B8`)
- `0x008F31C1` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x008F31CB` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x008F31D5` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x008F31E4` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [_CmOpenDeviceInterfaceRegKey](_CmOpenDeviceInterfaceRegKey_function_008F31F4.md) at `0x008F32D0`

### Static image references
- `0x008F2C68` → RVA `0x00001A10` (`.rdata`; read)
- `0x008F2D06` → RVA `0x00001A60` (`.rdata`; read)
- `0x008F30DE` → RVA `0x00001B78` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **10**
  - `0x008F2BDA` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008F2C3A` → [RtlInitUnicodeStringEx](../../text/46/RtlInitUnicodeStringEx_function_00463960.md) (`PAGE` → `.text`)
  - `0x008F2C63` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (`PAGE` → `.text`)
  - `0x008F2D01` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (`PAGE` → `.text`)
  - `0x008F2E13` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008F2F89` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008F31C1` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x008F31CB` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x008F31D5` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x008F31E4` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **8**
  - `0x008F3108` → [sub_00B1E8E0](../B1/Unknown_function_00B1E8E0.md) (`tail-transfer`)
  - `0x008F3111` → [sub_00B1E8E0 + 0x2B](../B1/Unknown_function_00B1E8E0.md) (`tail-transfer`)
  - `0x008F311A` → [sub_00B1E8E0 + 0x19](../B1/Unknown_function_00B1E8E0.md) (`tail-transfer`)
  - `0x008F3123` → [sub_00B1E8E0 + 0x2B](../B1/Unknown_function_00B1E8E0.md) (`tail-transfer`)
  - `0x008F312C` → [sub_00B1E8E0 + 0x2B](../B1/Unknown_function_00B1E8E0.md) (`tail-transfer`)
  - `0x008F3135` → [sub_00B1E8E0 + 0x14](../B1/Unknown_function_00B1E8E0.md) (`tail-transfer`)
  - `0x008F313B` → [sub_00B1E8E0 + 0x2B](../B1/Unknown_function_00B1E8E0.md) (`tail-transfer`)
  - `0x008F31A7` → [sub_00B1E8E0 + 0x3C](../B1/Unknown_function_00B1E8E0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
008F2B48  48 8B C4                        mov rax, rsp
008F2B4B  48 89 58 08                     mov qword ptr [rax + 8], rbx
008F2B4F  44 89 40 18                     mov dword ptr [rax + 0x18], r8d
008F2B53  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
008F2B57  55                              push rbp
008F2B58  56                              push rsi
008F2B59  57                              push rdi
008F2B5A  41 54                           push r12
008F2B5C  41 55                           push r13
008F2B5E  41 56                           push r14
008F2B60  41 57                           push r15
008F2B62  48 8D 68 C1                     lea rbp, [rax - 0x3f]
008F2B66  48 81 EC 90 00 00 00            sub rsp, 0x90
008F2B6D  48 8B F1                        mov rsi, rcx
008F2B70  0F 57 C0                        xorps xmm0, xmm0
008F2B73  33 C9                           xor ecx, ecx
008F2B75  45 8B F9                        mov r15d, r9d
008F2B78  89 4D B7                        mov dword ptr [rbp - 0x49], ecx
008F2B7B  45 8B E0                        mov r12d, r8d
008F2B7E  48 89 4D DF                     mov qword ptr [rbp - 0x21], rcx
008F2B82  48 8B DA                        mov rbx, rdx
008F2B85  48 89 4D D7                     mov qword ptr [rbp - 0x29], rcx
008F2B89  44 8B E9                        mov r13d, ecx
008F2B8C  48 89 4D CF                     mov qword ptr [rbp - 0x31], rcx
008F2B90  44 8D 71 04                     lea r14d, [rcx + 4]
008F2B94  48 89 4D E7                     mov qword ptr [rbp - 0x19], rcx
008F2B98  8B F9                           mov edi, ecx
008F2B9A  48 89 4D BF                     mov qword ptr [rbp - 0x41], rcx
008F2B9E  0F 11 45 EF                     movups xmmword ptr [rbp - 0x11], xmm0
008F2BA2  45 85 C0                        test r8d, r8d
008F2BA5  0F 84 32 01 00 00               je 0x1408f2cdd
008F2BAB  41 F7 C0 CC FC FF FF            test r8d, 0xfffffccc
008F2BB2  0F 85 25 01 00 00               jne 0x1408f2cdd
008F2BB8  41 8B C0                        mov eax, r8d
008F2BBB  25 00 02 00 00                  and eax, 0x200
008F2BC0  F7 D8                           neg eax
008F2BC2  1B FF                           sbb edi, edi
008F2BC4  83 E7 78                        and edi, 0x78
008F2BC7  81 C7 E0 01 00 00               add edi, 0x1e0
008F2BCD  8B D7                           mov edx, edi
008F2BCF  B9 00 01 00 00                  mov ecx, 0x100
008F2BD4  41 B8 50 4E 50 52               mov r8d, 0x52504e50
008F2BDA  E8 11 F5 28 00                  call 0x140b820f0
008F2BDF  48 89 45 C7                     mov qword ptr [rbp - 0x39], rax
008F2BE3  4C 8B E8                        mov r13, rax
008F2BE6  48 85 C0                        test rax, rax
008F2BE9  0F 84 C8 05 00 00               je 0x1408f31b7
008F2BEF  8B CF                           mov ecx, edi
008F2BF1  48 8D 45 B7                     lea rax, [rbp - 0x49]
008F2BF5  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
008F2BFA  45 8B CF                        mov r9d, r15d
008F2BFD  D1 E9                           shr ecx, 1
008F2BFF  45 8B C4                        mov r8d, r12d
008F2C02  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
008F2C06  48 8B D3                        mov rdx, rbx
008F2C09  4C 89 6C 24 28                  mov qword ptr [rsp + 0x28], r13
008F2C0E  E8 FD F3 FF FF                  call 0x1408f2010
008F2C13  8B D8                           mov ebx, eax
008F2C15  3D 23 00 00 C0                  cmp eax, 0xc0000023
008F2C1A  0F 84 64 03 00 00               je 0x1408f2f84
008F2C20  85 C0                           test eax, eax
008F2C22  0F 88 AD 01 00 00               js 0x1408f2dd5
008F2C28  41 0F BA E4 08                  bt r12d, 8
008F2C2D  0F 82 77 03 00 00               jb 0x1408f2faa
008F2C33  49 8B D5                        mov rdx, r13
008F2C36  48 8D 4D EF                     lea rcx, [rbp - 0x11]
008F2C3A  E8 21 0D B7 FF                  call 0x140463960
008F2C3F  8B D8                           mov ebx, eax
008F2C41  85 C0                           test eax, eax
008F2C43  0F 88 8C 01 00 00               js 0x1408f2dd5
008F2C49  44 0F B7 5D EF                  movzx r11d, word ptr [rbp - 0x11]
008F2C4E  44 3B DF                        cmp r11d, edi
008F2C51  0F 83 82 00 00 00               jae 0x1408f2cd9
008F2C57  41 B8 32 00 00 00               mov r8d, 0x32
008F2C5D  66 45 3B D8                     cmp r11w, r8w
008F2C61  76 76                           jbe 0x1408f2cd9
008F2C63  E8 88 B5 A0 FF                  call 0x1402fe1f0
008F2C68  4C 8B 15 A1 ED 70 FF            mov r10, qword ptr [rip - 0x8f125f]
008F2C6F  48 8B 98 B0 04 00 00            mov rbx, qword ptr [rax + 0x4b0]
008F2C76  45 3B D8                        cmp r11d, r8d
008F2C79  72 5E                           jb 0x1408f2cd9
008F2C7B  48 8B 7D F7                     mov rdi, qword ptr [rbp - 9]
008F2C7F  4D 8D 7A 32                     lea r15, [r10 + 0x32]
008F2C83  49 2B FA                        sub rdi, r10
008F2C86  BA C0 00 00 00                  mov edx, 0xc0
008F2C8B  4D 3B D7                        cmp r10, r15
008F2C8E  73 57                           jae 0x1408f2ce7
008F2C90  45 0F B7 02                     movzx r8d, word ptr [r10]
008F2C94  46 0F B7 0C 17                  movzx r9d, word ptr [rdi + r10]
008F2C99  66 45 3B C1                     cmp r8w, r9w
008F2C9D  75 06                           jne 0x1408f2ca5
008F2C9F  49 83 C2 02                     add r10, 2
008F2CA3  EB E6                           jmp 0x1408f2c8b
008F2CA5  41 83 F8 61                     cmp r8d, 0x61
008F2CA9  72 0F                           jb 0x1408f2cba
008F2CAB  41 83 F8 7A                     cmp r8d, 0x7a
008F2CAF  0F 87 C9 01 00 00               ja 0x1408f2e7e
008F2CB5  66 41 83 E8 20                  sub r8w, 0x20
008F2CBA  41 83 F9 61                     cmp r9d, 0x61
008F2CBE  72 0F                           jb 0x1408f2ccf
008F2CC0  41 83 F9 7A                     cmp r9d, 0x7a
008F2CC4  0F 87 F8 01 00 00               ja 0x1408f2ec2
008F2CCA  66 41 83 E9 20                  sub r9w, 0x20
008F2CCF  66 45 3B C1                     cmp r8w, r9w
008F2CD3  0F 84 9B 01 00 00               je 0x1408f2e74
008F2CD9  48 8B 7D BF                     mov rdi, qword ptr [rbp - 0x41]
008F2CDD  BB 0D 00 00 C0                  mov ebx, 0xc000000d
008F2CE2  E9 F2 00 00 00                  jmp 0x1408f2dd9
008F2CE7  B8 CE FF 00 00                  mov eax, 0xffce
008F2CEC  4D 8D 7D 32                     lea r15, [r13 + 0x32]
008F2CF0  66 01 45 F1                     add word ptr [rbp - 0xf], ax
008F2CF4  66 44 03 D8                     add r11w, ax
008F2CF8  66 44 89 5D EF                  mov word ptr [rbp - 0x11], r11w
008F2CFD  4C 89 7D F7                     mov qword ptr [rbp - 9], r15
008F2D01  E8 EA B4 A0 FF                  call 0x1402fe1f0
008F2D06  4C 8B 15 53 ED 70 FF            mov r10, qword ptr [rip - 0x8f12ad]
008F2D0D  41 BC 2C 00 00 00               mov r12d, 0x2c
008F2D13  48 8B 98 B0 04 00 00            mov rbx, qword ptr [rax + 0x4b0]
008F2D1A  66 45 3B DC                     cmp r11w, r12w
008F2D1E  0F 82 B3 03 00 00               jb 0x1408f30d7
008F2D24  4D 8B DF                        mov r11, r15
008F2D27  49 8D 7A 2C                     lea rdi, [r10 + 0x2c]
008F2D2B  4D 2B DA                        sub r11, r10
008F2D2E  4C 3B D7                        cmp r10, rdi
008F2D31  73 19                           jae 0x1408f2d4c
008F2D33  45 0F B7 02                     movzx r8d, word ptr [r10]
008F2D37  47 0F B7 0C 13                  movzx r9d, word ptr [r11 + r10]
008F2D3C  66 45 3B C1                     cmp r8w, r9w
008F2D40  0F 85 F0 00 00 00               jne 0x1408f2e36
008F2D46  49 83 C2 02                     add r10, 2
008F2D4A  EB E2                           jmp 0x1408f2d2e
008F2D4C  41 BE 09 00 00 00               mov r14d, 9
008F2D52  4D 03 FC                        add r15, r12
008F2D55  41 8B C6                        mov eax, r14d
008F2D58  48 8B 54 C6 60                  mov rdx, qword ptr [rsi + rax*8 + 0x60]
008F2D5D  48 85 D2                        test rdx, rdx
008F2D60  0F 84 9B 03 00 00               je 0x1408f3101
008F2D66  4C 8D 4D DF                     lea r9, [rbp - 0x21]
008F2D6A  45 8B C6                        mov r8d, r14d
008F2D6D  48 8B CE                        mov rcx, rsi
008F2D70  E8 4B CC FF FF                  call 0x1408ef9c0
008F2D75  8B D8                           mov ebx, eax
008F2D77  85 C0                           test eax, eax
008F2D79  78 5A                           js 0x1408f2dd5
008F2D7B  4C 8B 6D DF                     mov r13, qword ptr [rbp - 0x21]
008F2D7F  48 85 F6                        test rsi, rsi
008F2D82  0F 84 54 02 00 00               je 0x1408f2fdc
008F2D88  48 8B 86 E0 00 00 00            mov rax, qword ptr [rsi + 0xe0]
008F2D8F  48 85 C0                        test rax, rax
008F2D92  0F 84 44 02 00 00               je 0x1408f2fdc
008F2D98  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
008F2D9C  4C 8B 65 77                     mov r12, qword ptr [rbp + 0x77]
008F2DA0  45 33 C0                        xor r8d, r8d
008F2DA3  44 8B 75 67                     mov r14d, dword ptr [rbp + 0x67]
008F2DA7  49 8B D7                        mov rdx, r15
008F2DAA  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
008F2DAF  45 8B CE                        mov r9d, r14d
008F2DB2  49 8B CD                        mov rcx, r13
008F2DB5  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
008F2DBA  E8 51 CA FF FF                  call 0x1408ef810
008F2DBF  85 C0                           test eax, eax
008F2DC1  0F 85 26 02 00 00               jne 0x1408f2fed
008F2DC7  48 8B 45 7F                     mov rax, qword ptr [rbp + 0x7f]
008F2DCB  C7 00 02 00 00 00               mov dword ptr [rax], 2
008F2DD1  4C 8B 6D C7                     mov r13, qword ptr [rbp - 0x39]
008F2DD5  48 8B 7D BF                     mov rdi, qword ptr [rbp - 0x41]
008F2DD9  48 8B 4D E7                     mov rcx, qword ptr [rbp - 0x19]
008F2DDD  48 85 C9                        test rcx, rcx
008F2DE0  0F 85 DB 03 00 00               jne 0x1408f31c1
008F2DE6  48 8B 4D D7                     mov rcx, qword ptr [rbp - 0x29]
008F2DEA  48 85 C9                        test rcx, rcx
008F2DED  0F 85 D8 03 00 00               jne 0x1408f31cb
008F2DF3  48 8B 4D CF                     mov rcx, qword ptr [rbp - 0x31]
008F2DF7  48 85 C9                        test rcx, rcx
008F2DFA  0F 85 D5 03 00 00               jne 0x1408f31d5
008F2E00  48 85 FF                        test rdi, rdi
008F2E03  0F 85 D6 03 00 00               jne 0x1408f31df
008F2E09  4D 85 ED                        test r13, r13
008F2E0C  74 0A                           je 0x1408f2e18
008F2E0E  33 D2                           xor edx, edx
008F2E10  49 8B CD                        mov rcx, r13
008F2E13  E8 58 FA 28 00                  call 0x140b82870
008F2E18  8B C3                           mov eax, ebx
008F2E1A  48 8B 9C 24 D0 00 00 00         mov rbx, qword ptr [rsp + 0xd0]
008F2E22  48 81 C4 90 00 00 00            add rsp, 0x90
008F2E29  41 5F                           pop r15
008F2E2B  41 5E                           pop r14
008F2E2D  41 5D                           pop r13
008F2E2F  41 5C                           pop r12
008F2E31  5F                              pop rdi
008F2E32  5E                              pop rsi
008F2E33  5D                              pop rbp
008F2E34  C3                              ret
008F2E35  CC                              int3
008F2E36  41 83 F8 61                     cmp r8d, 0x61
008F2E3A  72 0F                           jb 0x1408f2e4b
008F2E3C  41 83 F8 7A                     cmp r8d, 0x7a
008F2E40  0F 87 BB 00 00 00               ja 0x1408f2f01
008F2E46  66 41 83 E8 20                  sub r8w, 0x20
008F2E4B  41 83 F9 61                     cmp r9d, 0x61
008F2E4F  72 0F                           jb 0x1408f2e60
008F2E51  41 83 F9 7A                     cmp r9d, 0x7a
008F2E55  0F 87 EA 00 00 00               ja 0x1408f2f45
008F2E5B  66 41 83 E9 20                  sub r9w, 0x20
008F2E60  66 45 3B C1                     cmp r8w, r9w
008F2E64  0F 85 6D 02 00 00               jne 0x1408f30d7
008F2E6A  BA C0 00 00 00                  mov edx, 0xc0
008F2E6F  E9 D2 FE FF FF                  jmp 0x1408f2d46
008F2E74  BA C0 00 00 00                  mov edx, 0xc0
008F2E79  E9 21 FE FF FF                  jmp 0x1408f2c9f
008F2E7E  48 85 DB                        test rbx, rbx
008F2E81  0F 84 33 FE FF FF               je 0x1408f2cba
008F2E87  66 44 3B C2                     cmp r8w, dx
008F2E8B  0F 82 29 FE FF FF               jb 0x1408f2cba
008F2E91  49 8B C0                        mov rax, r8
008F2E94  41 8B D0                        mov edx, r8d
008F2E97  48 C1 E8 08                     shr rax, 8
008F2E9B  83 E2 0F                        and edx, 0xf
008F2E9E  0F B7 0C 43                     movzx ecx, word ptr [rbx + rax*2]
008F2EA2  41 8B C0                        mov eax, r8d
008F2EA5  C1 E8 04                        shr eax, 4
008F2EA8  83 E0 0F                        and eax, 0xf
008F2EAB  03 C8                           add ecx, eax
008F2EAD  0F B7 0C 4B                     movzx ecx, word ptr [rbx + rcx*2]
008F2EB1  03 CA                           add ecx, edx
008F2EB3  BA C0 00 00 00                  mov edx, 0xc0
008F2EB8  66 44 03 04 4B                  add r8w, word ptr [rbx + rcx*2]
008F2EBD  E9 F8 FD FF FF                  jmp 0x1408f2cba
008F2EC2  48 85 DB                        test rbx, rbx
008F2EC5  0F 84 04 FE FF FF               je 0x1408f2ccf
008F2ECB  66 44 3B CA                     cmp r9w, dx
008F2ECF  0F 82 FA FD FF FF               jb 0x1408f2ccf
008F2ED5  49 8B C1                        mov rax, r9
008F2ED8  41 8B D1                        mov edx, r9d
008F2EDB  48 C1 E8 08                     shr rax, 8
008F2EDF  83 E2 0F                        and edx, 0xf
008F2EE2  0F B7 0C 43                     movzx ecx, word ptr [rbx + rax*2]
008F2EE6  41 8B C1                        mov eax, r9d
008F2EE9  C1 E8 04                        shr eax, 4
008F2EEC  83 E0 0F                        and eax, 0xf
008F2EEF  03 C8                           add ecx, eax
008F2EF1  0F B7 0C 4B                     movzx ecx, word ptr [rbx + rcx*2]
008F2EF5  03 CA                           add ecx, edx
008F2EF7  66 44 03 0C 4B                  add r9w, word ptr [rbx + rcx*2]
008F2EFC  E9 CE FD FF FF                  jmp 0x1408f2ccf
008F2F01  48 85 DB                        test rbx, rbx
008F2F04  0F 84 41 FF FF FF               je 0x1408f2e4b
008F2F0A  66 44 3B C2                     cmp r8w, dx
008F2F0E  0F 82 37 FF FF FF               jb 0x1408f2e4b
008F2F14  49 8B C0                        mov rax, r8
008F2F17  41 8B D0                        mov edx, r8d
008F2F1A  48 C1 E8 08                     shr rax, 8
008F2F1E  83 E2 0F                        and edx, 0xf
008F2F21  0F B7 0C 43                     movzx ecx, word ptr [rbx + rax*2]
008F2F25  41 8B C0                        mov eax, r8d
008F2F28  C1 E8 04                        shr eax, 4
008F2F2B  83 E0 0F                        and eax, 0xf
008F2F2E  03 C8                           add ecx, eax
008F2F30  0F B7 0C 4B                     movzx ecx, word ptr [rbx + rcx*2]
008F2F34  03 CA                           add ecx, edx
008F2F36  BA C0 00 00 00                  mov edx, 0xc0
008F2F3B  66 44 03 04 4B                  add r8w, word ptr [rbx + rcx*2]
008F2F40  E9 06 FF FF FF                  jmp 0x1408f2e4b
008F2F45  48 85 DB                        test rbx, rbx
008F2F48  0F 84 12 FF FF FF               je 0x1408f2e60
008F2F4E  66 44 3B CA                     cmp r9w, dx
008F2F52  0F 82 08 FF FF FF               jb 0x1408f2e60
008F2F58  49 8B C1                        mov rax, r9
008F2F5B  41 8B D1                        mov edx, r9d
008F2F5E  48 C1 E8 08                     shr rax, 8
008F2F62  83 E2 0F                        and edx, 0xf
008F2F65  0F B7 0C 43                     movzx ecx, word ptr [rbx + rax*2]
008F2F69  41 8B C1                        mov eax, r9d
008F2F6C  C1 E8 04                        shr eax, 4
008F2F6F  83 E0 0F                        and eax, 0xf
008F2F72  03 C8                           add ecx, eax
008F2F74  0F B7 0C 4B                     movzx ecx, word ptr [rbx + rcx*2]
008F2F78  03 CA                           add ecx, edx
008F2F7A  66 44 03 0C 4B                  add r9w, word ptr [rbx + rcx*2]
008F2F7F  E9 DC FE FF FF                  jmp 0x1408f2e60
008F2F84  33 D2                           xor edx, edx
008F2F86  49 8B CD                        mov rcx, r13
008F2F89  E8 E2 F8 28 00                  call 0x140b82870
008F2F8E  8B 7D B7                        mov edi, dword ptr [rbp - 0x49]
008F2F91  45 33 ED                        xor r13d, r13d
008F2F94  48 03 FF                        add rdi, rdi
008F2F97  B8 FF FF FF FF                  mov eax, 0xffffffff
008F2F9C  48 3B F8                        cmp rdi, rax
008F2F9F  77 42                           ja 0x1408f2fe3
008F2FA1  48 8B 5D 4F                     mov rbx, qword ptr [rbp + 0x4f]
008F2FA5  E9 23 FC FF FF                  jmp 0x1408f2bcd
008F2FAA  4D 8B FD                        mov r15, r13
008F2FAD  48 85 F6                        test rsi, rsi
008F2FB0  0F 85 8A 01 00 00               jne 0x1408f3140
008F2FB6  33 C9                           xor ecx, ecx
008F2FB8  4C 8D 4D D7                     lea r9, [rbp - 0x29]
008F2FBC  33 D2                           xor edx, edx
008F2FBE  41 B8 00 00 00 02               mov r8d, 0x2000000
008F2FC4  E8 93 15 00 00                  call 0x1408f455c
008F2FC9  8B D8                           mov ebx, eax
008F2FCB  85 C0                           test eax, eax
008F2FCD  0F 88 02 FE FF FF               js 0x1408f2dd5
008F2FD3  4C 8B 6D D7                     mov r13, qword ptr [rbp - 0x29]
008F2FD7  E9 A3 FD FF FF                  jmp 0x1408f2d7f
008F2FDC  33 C9                           xor ecx, ecx
008F2FDE  E9 B9 FD FF FF                  jmp 0x1408f2d9c
008F2FE3  BB 95 00 00 C0                  mov ebx, 0xc0000095
008F2FE8  E9 E8 FD FF FF                  jmp 0x1408f2dd5
008F2FED  3D 7C 01 00 C0                  cmp eax, 0xc000017c
008F2FF2  0F 84 CE 00 00 00               je 0x1408f30c6
008F2FF8  BA 34 00 00 C0                  mov edx, 0xc0000034
008F2FFD  3B C2                           cmp eax, edx
008F2FFF  0F 85 CB 00 00 00               jne 0x1408f30d0
008F3005  8B 7D 57                        mov edi, dword ptr [rbp + 0x57]
008F3008  33 C9                           xor ecx, ecx
008F300A  40 0F B6 C7                     movzx eax, dil
008F300E  38 4D 6F                        cmp byte ptr [rbp + 0x6f], cl
008F3011  75 1E                           jne 0x1408f3031
008F3013  83 F8 30                        cmp eax, 0x30
008F3016  75 12                           jne 0x1408f302a
008F3018  F7 C7 00 0F 00 00               test edi, 0xf00
008F301E  75 0A                           jne 0x1408f302a
008F3020  BB B9 02 00 C0                  mov ebx, 0xc00002b9
008F3025  E9 A7 FD FF FF                  jmp 0x1408f2dd1
008F302A  8B DA                           mov ebx, edx
008F302C  E9 A0 FD FF FF                  jmp 0x1408f2dd1
008F3031  83 F8 30                        cmp eax, 0x30
008F3034  0F 85 12 01 00 00               jne 0x1408f314c
008F303A  F7 C7 00 0F 00 00               test edi, 0xf00
008F3040  0F 85 06 01 00 00               jne 0x1408f314c
008F3046  4C 8D 45 BF                     lea r8, [rbp - 0x41]
008F304A  8B D7                           mov edx, edi
008F304C  48 8B CE                        mov rcx, rsi
008F304F  E8 6C BA 1A 00                  call 0x140a9eac0
008F3054  8B D8                           mov ebx, eax
008F3056  85 C0                           test eax, eax
008F3058  0F 88 73 FD FF FF               js 0x1408f2dd1
008F305E  48 8B 4D BF                     mov rcx, qword ptr [rbp - 0x41]
008F3062  B8 06 00 0E 00                  mov eax, 0xe0006
008F3067  48 85 C9                        test rcx, rcx
008F306A  41 8B FE                        mov edi, r14d
008F306D  4D 8B C7                        mov r8, r15
008F3070  49 8B D5                        mov rdx, r13
008F3073  0F 45 F8                        cmovne edi, eax
008F3076  48 8B 45 7F                     mov rax, qword ptr [rbp + 0x7f]
008F307A  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
008F307F  45 33 C9                        xor r9d, r9d
008F3082  48 8D 45 CF                     lea rax, [rbp - 0x31]
008F3086  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
008F308B  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
008F3090  48 8B CE                        mov rcx, rsi
008F3093  89 7C 24 20                     mov dword ptr [rsp + 0x20], edi
008F3097  E8 04 EC 03 00                  call 0x140931ca0
008F309C  41 BF 7C 01 00 C0               mov r15d, 0xc000017c
008F30A2  41 3B C7                        cmp eax, r15d
008F30A5  74 1F                           je 0x1408f30c6
008F30A7  85 C0                           test eax, eax
008F30A9  78 25                           js 0x1408f30d0
008F30AB  41 3B FE                        cmp edi, r14d
008F30AE  0F 85 D4 00 00 00               jne 0x1408f3188
008F30B4  48 8B 45 CF                     mov rax, qword ptr [rbp - 0x31]
008F30B8  48 83 65 CF 00                  and qword ptr [rbp - 0x31], 0
008F30BD  49 89 04 24                     mov qword ptr [r12], rax
008F30C1  E9 0B FD FF FF                  jmp 0x1408f2dd1
008F30C6  BB E5 00 00 C0                  mov ebx, 0xc00000e5
008F30CB  E9 01 FD FF FF                  jmp 0x1408f2dd1
008F30D0  8B D8                           mov ebx, eax
008F30D2  E9 FA FC FF FF                  jmp 0x1408f2dd1
008F30D7  41 B0 01                        mov r8b, 1
008F30DA  48 8D 55 EF                     lea rdx, [rbp - 0x11]
008F30DE  48 8D 0D 93 EA 70 FF            lea rcx, [rip - 0x8f156d]
008F30E5  E8 86 1E 00 00                  call 0x1408f4f70
008F30EA  84 C0                           test al, al
008F30EC  0F 84 63 FC FF FF               je 0x1408f2d55
008F30F2  41 BE 0E 00 00 00               mov r14d, 0xe
008F30F8  49 83 C7 24                     add r15, 0x24
008F30FC  E9 54 FC FF FF                  jmp 0x1408f2d55
008F3101  41 8B CE                        mov ecx, r14d
008F3104  41 83 FE 0A                     cmp r14d, 0xa
008F3108  0F 87 D2 B7 22 00               ja 0x140b1e8e0
008F310E  83 E9 04                        sub ecx, 4
008F3111  0F 84 F4 B7 22 00               je 0x140b1e90b
008F3117  83 E9 01                        sub ecx, 1
008F311A  0F 84 D9 B7 22 00               je 0x140b1e8f9
008F3120  83 E9 01                        sub ecx, 1
008F3123  0F 84 E2 B7 22 00               je 0x140b1e90b
008F3129  83 E9 01                        sub ecx, 1
008F312C  0F 84 D9 B7 22 00               je 0x140b1e90b
008F3132  83 E9 01                        sub ecx, 1
008F3135  0F 85 B9 B7 22 00               jne 0x140b1e8f4
008F313B  E9 CB B7 22 00                  jmp 0x140b1e90b
008F3140  48 8B 8E E0 00 00 00            mov rcx, qword ptr [rsi + 0xe0]
008F3147  E9 6C FE FF FF                  jmp 0x1408f2fb8
008F314C  48 8B 55 4F                     mov rdx, qword ptr [rbp + 0x4f]
008F3150  48 8D 45 E7                     lea rax, [rbp - 0x19]
008F3154  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
008F3159  45 33 C9                        xor r9d, r9d
008F315C  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
008F3161  88 4C 24 28                     mov byte ptr [rsp + 0x28], cl
008F3165  48 8B CE                        mov rcx, rsi
008F3168  C7 44 24 20 01 00 00 00         mov dword ptr [rsp + 0x20], 1
008F3170  45 8D 41 30                     lea r8d, [r9 + 0x30]
008F3174  E8 7B 00 00 00                  call 0x1408f31f4
008F3179  8B D8                           mov ebx, eax
008F317B  85 C0                           test eax, eax
008F317D  0F 88 4E FC FF FF               js 0x1408f2dd1
008F3183  E9 BE FE FF FF                  jmp 0x1408f3046
008F3188  48 8B 55 CF                     mov rdx, qword ptr [rbp - 0x31]
008F318C  45 33 C9                        xor r9d, r9d
008F318F  4C 89 64 24 28                  mov qword ptr [rsp + 0x28], r12
008F3194  45 33 C0                        xor r8d, r8d
008F3197  48 8B CE                        mov rcx, rsi
008F319A  44 89 74 24 20                  mov dword ptr [rsp + 0x20], r14d
008F319F  E8 14 C6 FF FF                  call 0x1408ef7b8
008F31A4  41 3B C7                        cmp eax, r15d
008F31A7  0F 85 6F B7 22 00               jne 0x140b1e91c
008F31AD  BB 34 00 00 C0                  mov ebx, 0xc0000034
008F31B2  E9 1A FC FF FF                  jmp 0x1408f2dd1
008F31B7  BB 17 00 00 C0                  mov ebx, 0xc0000017
008F31BC  E9 14 FC FF FF                  jmp 0x1408f2dd5
008F31C1  E8 EA A0 DB FF                  call 0x1406ad2b0
008F31C6  E9 1B FC FF FF                  jmp 0x1408f2de6
008F31CB  E8 E0 A0 DB FF                  call 0x1406ad2b0
008F31D0  E9 1E FC FF FF                  jmp 0x1408f2df3
008F31D5  E8 D6 A0 DB FF                  call 0x1406ad2b0
008F31DA  E9 21 FC FF FF                  jmp 0x1408f2e00
008F31DF  33 D2                           xor edx, edx
008F31E1  48 8B CF                        mov rcx, rdi
008F31E4  E8 87 F6 28 00                  call 0x140b82870
008F31E9  E9 1B FC FF FF                  jmp 0x1408f2e09
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall _CmOpenDeviceInterfaceRegKeyWorker(__int64 a1, __int64 a2, int a3, int a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m90;
    unsigned int v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned int *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    v_rsp = (v_rsp) - (144);
    a1 = 0;
    *(unsigned int *)(v_rsp - 63 - 73) = 0;
    *(unsigned __int64 *)(v_rsp - 63 - 33) = 0;
    *(unsigned __int64 *)(v_rsp - 63 - 41) = 0;
    *(unsigned __int64 *)(v_rsp - 63 - 49) = 0;
    *(unsigned __int64 *)(v_rsp - 63 - 25) = 0;
    *(unsigned __int64 *)(v_rsp - 63 - 65) = 0;
    *(unsigned __int64 *)(v_rsp - 63 - 17) = v_xmm0;
    if (a3 == 0) goto loc_008F2CDD;
    if (((a3) & (0xFFFFFCCCULL)) != 0) goto loc_008F2CDD;
    result = (unsigned int)(((unsigned int)(a3)) & (512));
    result = (unsigned int)(-(result));
    v_rdi = (unsigned int)((0) & (120));
    v_rdi = (unsigned int)((v_rdi) + (480));
loc_008F2BCD:
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(v_rdi)), (unsigned int)(0x52504E50ULL), a4);
    *(unsigned __int64 *)(v_rsp - 63 - 57) = result;
    if (result == 0) goto loc_008F31B7;
    v_stack_m90 = v_rsp - 63 - 73;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) >> (1));
    v_stack_m98 = (unsigned int)(a1);
    v_stack_mA0 = result;
    result = _CmGetDeviceInterfaceRegKeyPath(a1, a2, (unsigned int)((unsigned int)((unsigned int)(a3))), (unsigned int)((unsigned int)((unsigned int)(a4))));
    if (((unsigned int)(result)) == 0xC0000023ULL) goto loc_008F2F84;
    if (sign_flag) goto loc_008F2DD5;
    if (condition_is_below) goto loc_008F2FAA;
    result = RtlInitUnicodeStringEx(v_rsp - 63 - 17, result, (unsigned int)((unsigned int)((unsigned int)(a3))), (unsigned int)((unsigned int)((unsigned int)(a4))));
    if (sign_flag) goto loc_008F2DD5;
    if (((unsigned int)(*(unsigned __int16 *)(v_rsp - 63 - 17))) >= ((unsigned int)(v_rdi))) goto loc_008F2CD9;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rsp - 63 - 17))) <= 50) goto loc_008F2CD9;
    result = PsGetCurrentServerSiloGlobals(v_rsp - 63 - 17, result, 50, (unsigned int)((unsigned int)((unsigned int)(a4))));
    if (((unsigned int)(*(unsigned __int16 *)(v_rsp - 63 - 17))) < 50) goto loc_008F2CD9;
    v_rdi = (*(unsigned __int64 *)(v_rsp - 63 - 9)) - (*(unsigned __int64 *)(v_rip - 9376351));
loc_008F2C8B:
    if ((*(unsigned __int64 *)(v_rip - 9376351)) >= (*(unsigned __int64 *)(v_rip - 9376351) + 50)) goto loc_008F2CE7;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip - 9376351)))) != ((unsigned __int16)(*(unsigned __int16 *)(v_rdi + *(unsigned __int64 *)(v_rip - 9376351) * 1)))) goto loc_008F2CA5;
loc_008F2C9F:
    v_r10 = (*(unsigned __int64 *)(v_rip - 9376351)) + (2);
    goto loc_008F2C8B;
loc_008F2CA5:
    if (((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip - 9376351)))) < 97) goto loc_008F2CBA;
    if (((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip - 9376351)))) > 122) goto loc_008F2E7E;
    a3 = (unsigned __int16)((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip - 9376351))) - (32));
loc_008F2CBA:
    if (((unsigned int)(*(unsigned __int16 *)(v_rdi + *(unsigned __int64 *)(v_rip - 9376351) * 1))) < 97) goto loc_008F2CCF;
    if (((unsigned int)(*(unsigned __int16 *)(v_rdi + *(unsigned __int64 *)(v_rip - 9376351) * 1))) > 122) goto loc_008F2EC2;
    a4 = (unsigned __int16)((*(unsigned __int16 *)(v_rdi + *(unsigned __int64 *)(v_rip - 9376351) * 1)) - (32));
loc_008F2CCF:
    if (((unsigned __int16)(a3)) == ((unsigned __int16)(a4))) goto loc_008F2E74;
loc_008F2CD9:
loc_008F2CDD:
    goto loc_008F2DD9;
loc_008F2CE7:
    v_r11 = (unsigned __int16)((*(unsigned __int16 *)(v_rsp - 63 - 17)) + ((unsigned __int16)((unsigned int)(0xFFCEULL))));
    *(unsigned __int16 *)(v_rsp - 63 - 17) = (unsigned __int16)(v_r11);
    *(unsigned __int64 *)(v_rsp - 63 - 9) = result + 50;
    result = PsGetCurrentServerSiloGlobals(v_rsp - 63 - 17, 192, a3, a4);
    if (((unsigned __int16)(v_r11)) < 44) goto loc_008F30D7;
    v_r11 = (result + 50) - (*(unsigned __int64 *)(v_rip - 9376429));
loc_008F2D2E:
    if ((*(unsigned __int64 *)(v_rip - 9376429)) >= (*(unsigned __int64 *)(v_rip - 9376429) + 44)) goto loc_008F2D4C;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip - 9376429)))) != ((unsigned __int16)(*(unsigned __int16 *)(v_r11 + *(unsigned __int64 *)(v_rip - 9376429) * 1)))) goto loc_008F2E36;
loc_008F2D46:
    v_r10 = (*(unsigned __int64 *)(v_rip - 9376429)) + (2);
    goto loc_008F2D2E;
loc_008F2D4C:
    v_r15 = (result + 50) + (44);
loc_008F2D55:
    if (*(unsigned __int64 *)(a1 + 9 * 8 + 96) == 0) goto loc_008F3101;
    result = _PnpCtxGetCachedNodeBaseKey(a1, *(unsigned __int64 *)(a1 + 9 * 8 + 96), 9, v_rsp - 63 - 33);
    if (sign_flag) goto loc_008F2DD5;
loc_008F2D7F:
    if (a1 == 0) goto loc_008F2FDC;
    if (*(unsigned __int64 *)(a1 + 224) == 0) goto loc_008F2FDC;
loc_008F2D9C:
    a3 = 0;
    v_stack_mA0 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 224) + 8);
    v_stack_mA8 = *(unsigned __int64 *)(v_rsp - 63 + 119);
    result = _RegRtlOpenKeyTransacted(*(unsigned __int64 *)(v_rsp - 63 - 33), v_r15, a3, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 63 + 103)))));
    if ((unsigned int)(result) != 0) goto loc_008F2FED;
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 + 127)) = 2;
loc_008F2DD1:
loc_008F2DD5:
loc_008F2DD9:
    if (*(unsigned __int64 *)(v_rsp - 63 - 25) != 0) goto loc_008F31C1;
loc_008F2DE6:
    if (*(unsigned __int64 *)(v_rsp - 63 - 41) != 0) goto loc_008F31CB;
loc_008F2DF3:
    if (*(unsigned __int64 *)(v_rsp - 63 - 49) != 0) goto loc_008F31D5;
loc_008F2E00:
    if (*(unsigned __int64 *)(v_rsp - 63 - 65) != 0) goto loc_008F31DF;
loc_008F2E09:
    result = *(unsigned __int64 *)(v_rsp - 63 + 127);
    if (*(unsigned __int64 *)(v_rsp - 63 - 57) != 0) {
        a2 = 0;
        a1 = *(unsigned __int64 *)(v_rsp - 63 - 57);
        result = ExFreePoolWithTag(a1, a2, a3, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 63 + 103)))));
    }
    v_rsp = (v_rsp) + (144);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
loc_008F2E36:
    if (0 < 97) goto loc_008F2E4B;
    if (0 > 122) goto loc_008F2F01;
    a3 = (unsigned __int16)((a3) - (32));
loc_008F2E4B:
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 63 + 103)))))) < 97) goto loc_008F2E60;
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 63 + 103)))))) > 122) goto loc_008F2F45;
    a4 = (unsigned __int16)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 63 + 103))))) - (32));
loc_008F2E60:
    if (((unsigned __int16)(a3)) != ((unsigned __int16)(a4))) goto loc_008F30D7;
    goto loc_008F2D46;
loc_008F2E74:
    goto loc_008F2C9F;
loc_008F2E7E:
    if (v_stack_p8 == 0) goto loc_008F2CBA;
    if (((unsigned __int16)(a3)) < 192) goto loc_008F2CBA;
    result = (a3) >> (8);
    a2 = (unsigned int)(((unsigned int)(a3)) & (15));
    result = (unsigned int)(((unsigned int)(a3)) >> (4));
    result = (unsigned int)((result) & (15));
    a1 = (unsigned int)((*(unsigned __int16 *)(v_stack_p8 + result * 2)) + ((unsigned int)(result)));
    a1 = (unsigned int)((*(unsigned __int16 *)(v_stack_p8 + a1 * 2)) + ((unsigned int)(a2)));
    a3 = (unsigned __int16)((a3) + (*(unsigned __int16 *)(v_stack_p8 + a1 * 2)));
    goto loc_008F2CBA;
loc_008F2EC2:
    if (v_stack_p8 == 0) goto loc_008F2CCF;
    if (((unsigned __int16)(a4)) < 192) goto loc_008F2CCF;
    result = (a4) >> (8);
    a2 = (unsigned int)(((unsigned int)(a4)) & (15));
    result = (unsigned int)(((unsigned int)(a4)) >> (4));
    result = (unsigned int)((result) & (15));
    a1 = (unsigned int)((*(unsigned __int16 *)(v_stack_p8 + result * 2)) + ((unsigned int)(result)));
    a1 = (unsigned int)((*(unsigned __int16 *)(v_stack_p8 + a1 * 2)) + ((unsigned int)(a2)));
    a4 = (unsigned __int16)((a4) + (*(unsigned __int16 *)(v_stack_p8 + a1 * 2)));
    goto loc_008F2CCF;
loc_008F2F01:
    if (v_stack_p8 == 0) goto loc_008F2E4B;
    if (((unsigned __int16)(a3)) < ((unsigned __int16)(a2))) goto loc_008F2E4B;
    result = (a3) >> (8);
    a2 = (unsigned int)(((unsigned int)(a3)) & (15));
    result = (unsigned int)(((unsigned int)(a3)) >> (4));
    result = (unsigned int)((result) & (15));
    a1 = (unsigned int)((*(unsigned __int16 *)(v_stack_p8 + result * 2)) + ((unsigned int)(result)));
    a1 = (unsigned int)((*(unsigned __int16 *)(v_stack_p8 + a1 * 2)) + ((unsigned int)(a2)));
    a3 = (unsigned __int16)((a3) + (*(unsigned __int16 *)(v_stack_p8 + a1 * 2)));
    goto loc_008F2E4B;
loc_008F2F45:
    if (v_stack_p8 == 0) goto loc_008F2E60;
    if (((unsigned __int16)(a4)) < 192) goto loc_008F2E60;
    result = (a4) >> (8);
    a2 = (unsigned int)(((unsigned int)(a4)) & (15));
    result = (unsigned int)(((unsigned int)(a4)) >> (4));
    result = (unsigned int)((result) & (15));
    a1 = (unsigned int)((*(unsigned __int16 *)(v_stack_p8 + result * 2)) + ((unsigned int)(result)));
    a1 = (unsigned int)((*(unsigned __int16 *)(v_stack_p8 + a1 * 2)) + ((unsigned int)(a2)));
    a4 = (unsigned __int16)((a4) + (*(unsigned __int16 *)(v_stack_p8 + a1 * 2)));
    goto loc_008F2E60;
loc_008F2F84:
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(v_rsp - 63 - 57), a2, a3, a4);
    v_r13 = 0;
    v_rdi = ((unsigned int)(*(unsigned int *)(v_rsp - 63 - 73))) + ((unsigned int)(*(unsigned int *)(v_rsp - 63 - 73)));
    if (v_rdi > ((unsigned int)(0xFFFFFFFFULL))) goto loc_008F2FE3;
    goto loc_008F2BCD;
loc_008F2FAA:
    if (a1 != 0) goto loc_008F3140;
    a1 = 0;
loc_008F2FB8:
    a2 = 0;
    result = SysCtxRegOpenCurrentUserKey(a1, a2, (unsigned int)(0x2000000ULL), v_rsp - 63 - 41);
    if (sign_flag) goto loc_008F2DD5;
    goto loc_008F2D7F;
loc_008F2FDC:
    a1 = 0;
    goto loc_008F2D9C;
loc_008F2FE3:
    goto loc_008F2DD5;
loc_008F2FED:
    if (((unsigned int)(result)) == 0xC000017CULL) goto loc_008F30C6;
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)(0xC0000034ULL)))) goto loc_008F30D0;
    a1 = 0;
    if ((*(unsigned __int8 *)(v_rsp - 63 + 111)) != 0) goto loc_008F3031;
    if (((unsigned int)((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rsp - 63 + 87))))) != 48) goto loc_008F302A;
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 63 + 87)))) & (0xF00ULL)) != 0) goto loc_008F302A;
    goto loc_008F2DD1;
loc_008F302A:
    goto loc_008F2DD1;
loc_008F3031:
    if (((unsigned int)((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rsp - 63 + 87))))) != 48) goto loc_008F314C;
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 63 + 87)))) & (0xF00ULL)) != 0) goto loc_008F314C;
loc_008F3046:
    result = CmGetDeviceInterfaceRegKeySecurityDescriptor(0, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 63 + 87)))), v_rsp - 63 - 65, v_rsp - 63 - 41);
    if (sign_flag) goto loc_008F2DD1;
    v_rdi = (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 63 + 103))));
    if (*(unsigned __int64 *)(v_rsp - 63 - 65) != 0) { v_rdi = (unsigned int)((unsigned int)(0xE0006ULL)); }
    v_stack_p38 = *(unsigned __int64 *)(v_rsp - 63 + 127);
    a4 = 0;
    v_stack_p30 = v_rsp - 63 - 49;
    v_stack_p28 = *(unsigned __int64 *)(v_rsp - 63 - 65);
    v_stack_p20 = (unsigned int)(v_rdi);
    result = PnpCtxRegCreateTree(0, *(unsigned __int64 *)(v_rsp - 63 - 41), 0, a4);
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0xC000017CULL)))) goto loc_008F30C6;
    if (sign_flag) goto loc_008F30D0;
    if (((unsigned int)(v_rdi)) != ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 63 + 103))))) goto loc_008F3188;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 + 119)) = *(unsigned __int64 *)(v_rsp - 63 - 49);
    goto loc_008F2DD1;
loc_008F30C6:
    goto loc_008F2DD1;
loc_008F30D0:
    goto loc_008F2DD1;
loc_008F30D7:
    result = RtlPrefixUnicodeString(v_rip - 9377133, v_rsp - 63 - 17, 1, a4);
    if ((unsigned __int8)(result) == 0) goto loc_008F2D55;
    v_r15 = ((unsigned int)(0xC000017CULL)) + (36);
    goto loc_008F2D55;
loc_008F3101:
    a1 = (unsigned int)((14) - (4));
    a1 = (unsigned int)((a1) - (1));
    a1 = (unsigned int)((a1) - (1));
    a1 = (unsigned int)((a1) - (1));
    a1 = (unsigned int)((a1) - (1));
loc_008F3140:
    goto loc_008F2FB8;
loc_008F314C:
    v_stack_p38 = *(unsigned __int64 *)(a1 + 224);
    a4 = 0;
    v_stack_p30 = v_rsp - 63 - 25;
    v_stack_p28 = (unsigned __int8)(*(unsigned __int64 *)(a1 + 224));
    v_stack_p20 = 1;
    result = _CmOpenDeviceInterfaceRegKey(a1, *(unsigned __int64 *)(v_rsp - 63 + 79), a4 + 48, a4);
    if (sign_flag) goto loc_008F2DD1;
    goto loc_008F3046;
loc_008F3188:
    a4 = 0;
    v_stack_p28 = *(unsigned __int64 *)(v_rsp - 63 + 119);
    a3 = 0;
    v_stack_p20 = 14;
    result = PnpCtxRegOpenKey(a1, *(unsigned __int64 *)(v_rsp - 63 - 49), a3, a4);
    goto loc_008F2DD1;
loc_008F31B7:
    goto loc_008F2DD5;
loc_008F31C1:
    result = ZwClose(a1, *(unsigned __int64 *)(v_rsp - 63 - 49), a3, a4);
    goto loc_008F2DE6;
loc_008F31CB:
    result = ZwClose(a1, *(unsigned __int64 *)(v_rsp - 63 - 49), a3, a4);
    goto loc_008F2DF3;
loc_008F31D5:
    result = ZwClose(a1, *(unsigned __int64 *)(v_rsp - 63 - 49), a3, a4);
    goto loc_008F2E00;
loc_008F31DF:
    a2 = 0;
    result = ExFreePoolWithTag(v_rdi, a2, a3, a4);
    goto loc_008F2E09;
}
```

## 5. (Beta) C Style

```c
int64_t _CmOpenDeviceInterfaceRegKeyWorker(void *Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m90;
    uint32_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint32_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint32_t *)(local_rsp + 0x18) = Arg3;
    *(uint64_t *)(local_rsp + 0x10) = Arg2;
    local_rsp = (local_rsp) - (144);
    Arg1 = 0;
    *(uint32_t *)(local_rsp - 0x3F - 0x49) = 0;
    *(uint64_t *)(local_rsp - 0x3F - 0x21) = 0;
    *(uint64_t *)(local_rsp - 0x3F - 0x29) = 0;
    *(uint64_t *)(local_rsp - 0x3F - 0x31) = 0;
    *(uint64_t *)(local_rsp - 0x3F - 0x19) = 0;
    *(uint64_t *)(local_rsp - 0x3F - 0x41) = 0;
    *(uint64_t *)(local_rsp - 0x3F - 0x11) = v_xmm0;
    if (Arg3 == 0) goto loc_008F2CDD;
    if (((Arg3) & (0xFFFFFCCCULL)) != 0) goto loc_008F2CDD;
    result = (uint32_t)(((uint32_t)(Arg3)) & (512));
    result = (uint32_t)(-(result));
    local_rdi = (uint32_t)((0) & (120));
    local_rdi = (uint32_t)((local_rdi) + (480));
loc_008F2BCD:
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(local_rdi)), (uint32_t)(0x52504E50ULL), Arg4);
    *(uint64_t *)(local_rsp - 0x3F - 0x39) = result;
    if (result == 0) goto loc_008F31B7;
    v_stack_m90 = local_rsp - 63 - 73;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) >> (1));
    v_stack_m98 = (uint32_t)(Arg1);
    v_stack_mA0 = result;
    result = _CmGetDeviceInterfaceRegKeyPath(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    if (((uint32_t)(result)) == 0xC0000023ULL) goto loc_008F2F84;
    if (sign_flag) goto loc_008F2DD5;
    if (condition_is_below) goto loc_008F2FAA;
    result = RtlInitUnicodeStringEx(local_rsp - 63 - 17, result, (uint32_t)((uint32_t)((uint32_t)(Arg3))), (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    if (sign_flag) goto loc_008F2DD5;
    if (((uint32_t)(*(uint16_t *)(local_rsp - 0x3F - 0x11))) >= ((uint32_t)(local_rdi))) goto loc_008F2CD9;
    if (((uint16_t)(*(uint16_t *)(local_rsp - 0x3F - 0x11))) <= 50) goto loc_008F2CD9;
    result = PsGetCurrentServerSiloGlobals(local_rsp - 63 - 17, result, 50, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    if (((uint32_t)(*(uint16_t *)(local_rsp - 0x3F - 0x11))) < 50) goto loc_008F2CD9;
    local_rdi = (*(uint64_t *)(local_rsp - 0x3F - 0x9)) - (*(uint64_t *)(v_rip - 0x8F125F));
loc_008F2C8B:
    if ((*(uint64_t *)(v_rip - 0x8F125F)) >= (*(uint64_t *)(v_rip - 0x8F125F) + 50)) goto loc_008F2CE7;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(v_rip - 0x8F125F)))) != ((uint16_t)(*(uint16_t *)(local_rdi + *(uint64_t *)(v_rip - 0x8F125F) * 1)))) goto loc_008F2CA5;
loc_008F2C9F:
    local_r10 = (*(uint64_t *)(v_rip - 0x8F125F)) + (2);
    goto loc_008F2C8B;
loc_008F2CA5:
    if (((uint32_t)(*(uint16_t *)(*(uint64_t *)(v_rip - 0x8F125F)))) < 97) goto loc_008F2CBA;
    if (((uint32_t)(*(uint16_t *)(*(uint64_t *)(v_rip - 0x8F125F)))) > 122) goto loc_008F2E7E;
    Arg3 = (uint16_t)((*(uint16_t *)(*(uint64_t *)(v_rip - 0x8F125F))) - (32));
loc_008F2CBA:
    if (((uint32_t)(*(uint16_t *)(local_rdi + *(uint64_t *)(v_rip - 0x8F125F) * 1))) < 97) goto loc_008F2CCF;
    if (((uint32_t)(*(uint16_t *)(local_rdi + *(uint64_t *)(v_rip - 0x8F125F) * 1))) > 122) goto loc_008F2EC2;
    Arg4 = (uint16_t)((*(uint16_t *)(local_rdi + *(uint64_t *)(v_rip - 0x8F125F) * 1)) - (32));
loc_008F2CCF:
    if (((uint16_t)(Arg3)) == ((uint16_t)(Arg4))) goto loc_008F2E74;
loc_008F2CD9:
loc_008F2CDD:
    goto loc_008F2DD9;
loc_008F2CE7:
    local_r11 = (uint16_t)((*(uint16_t *)(local_rsp - 0x3F - 0x11)) + ((uint16_t)((uint32_t)(0xFFCEULL))));
    *(uint16_t *)(local_rsp - 0x3F - 0x11) = (uint16_t)(local_r11);
    *(uint64_t *)(local_rsp - 0x3F - 0x9) = result + 50;
    result = PsGetCurrentServerSiloGlobals(local_rsp - 63 - 17, 192, Arg3, Arg4);
    if (((uint16_t)(local_r11)) < 44) goto loc_008F30D7;
    local_r11 = (result + 50) - (*(uint64_t *)(v_rip - 0x8F12AD));
loc_008F2D2E:
    if ((*(uint64_t *)(v_rip - 0x8F12AD)) >= (*(uint64_t *)(v_rip - 0x8F12AD) + 44)) goto loc_008F2D4C;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(v_rip - 0x8F12AD)))) != ((uint16_t)(*(uint16_t *)(local_r11 + *(uint64_t *)(v_rip - 0x8F12AD) * 1)))) goto loc_008F2E36;
loc_008F2D46:
    local_r10 = (*(uint64_t *)(v_rip - 0x8F12AD)) + (2);
    goto loc_008F2D2E;
loc_008F2D4C:
    local_r15 = (result + 50) + (44);
loc_008F2D55:
    if (*(uint64_t *)(arg1 + 0x9 * 8 + 0x60) == 0) goto loc_008F3101;
    result = _PnpCtxGetCachedNodeBaseKey(Arg1, *(uint64_t *)(arg1 + 0x9 * 8 + 0x60), 9, local_rsp - 63 - 33);
    if (sign_flag) goto loc_008F2DD5;
loc_008F2D7F:
    if (Arg1 == NULL) goto loc_008F2FDC;
    if (*(uint64_t *)(arg1 + 0xE0) == 0) goto loc_008F2FDC;
loc_008F2D9C:
    Arg3 = 0;
    v_stack_mA0 = *(uint64_t *)(*(uint64_t *)(arg1 + 0xE0) + 0x8);
    v_stack_mA8 = *(uint64_t *)(local_rsp - 0x3F + 0x77);
    result = _RegRtlOpenKeyTransacted(*(uint64_t *)(local_rsp - 0x3F - 0x21), local_r15, Arg3, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x3F + 0x67)))));
    if ((uint32_t)(result) != 0) goto loc_008F2FED;
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x7F)) = 2;
loc_008F2DD1:
loc_008F2DD5:
loc_008F2DD9:
    if (*(uint64_t *)(local_rsp - 0x3F - 0x19) != 0) goto loc_008F31C1;
loc_008F2DE6:
    if (*(uint64_t *)(local_rsp - 0x3F - 0x29) != 0) goto loc_008F31CB;
loc_008F2DF3:
    if (*(uint64_t *)(local_rsp - 0x3F - 0x31) != 0) goto loc_008F31D5;
loc_008F2E00:
    if (*(uint64_t *)(local_rsp - 0x3F - 0x41) != 0) goto loc_008F31DF;
loc_008F2E09:
    result = *(uint64_t *)(local_rsp - 0x3F + 0x7F);
    if (*(uint64_t *)(local_rsp - 0x3F - 0x39) != 0) {
        Arg2 = 0;
        Arg1 = *(uint64_t *)(local_rsp - 0x3F - 0x39);
        result = ExFreePoolWithTag(Arg1, Arg2, Arg3, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x3F + 0x67)))));
    }
    local_rsp = (local_rsp) + (144);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
loc_008F2E36:
    if (0 < 97) goto loc_008F2E4B;
    if (0 > 122) goto loc_008F2F01;
    Arg3 = (uint16_t)((Arg3) - (32));
loc_008F2E4B:
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x3F + 0x67)))))) < 97) goto loc_008F2E60;
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x3F + 0x67)))))) > 122) goto loc_008F2F45;
    Arg4 = (uint16_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x3F + 0x67))))) - (32));
loc_008F2E60:
    if (((uint16_t)(Arg3)) != ((uint16_t)(Arg4))) goto loc_008F30D7;
    goto loc_008F2D46;
loc_008F2E74:
    goto loc_008F2C9F;
loc_008F2E7E:
    if (v_stack_p8 == 0) goto loc_008F2CBA;
    if (((uint16_t)(Arg3)) < 192) goto loc_008F2CBA;
    result = (Arg3) >> (8);
    Arg2 = (uint32_t)(((uint32_t)(Arg3)) & (15));
    result = (uint32_t)(((uint32_t)(Arg3)) >> (4));
    result = (uint32_t)((result) & (15));
    Arg1 = (uint32_t)((*(uint16_t *)(v_stack_p8 + result * 2)) + ((uint32_t)(result)));
    Arg1 = (uint32_t)((*(uint16_t *)(v_stack_p8 + arg1 * 2)) + ((uint32_t)(Arg2)));
    Arg3 = (uint16_t)((Arg3) + (*(uint16_t *)(v_stack_p8 + arg1 * 2)));
    goto loc_008F2CBA;
loc_008F2EC2:
    if (v_stack_p8 == 0) goto loc_008F2CCF;
    if (((uint16_t)(Arg4)) < 192) goto loc_008F2CCF;
    result = (Arg4) >> (8);
    Arg2 = (uint32_t)(((uint32_t)(Arg4)) & (15));
    result = (uint32_t)(((uint32_t)(Arg4)) >> (4));
    result = (uint32_t)((result) & (15));
    Arg1 = (uint32_t)((*(uint16_t *)(v_stack_p8 + result * 2)) + ((uint32_t)(result)));
    Arg1 = (uint32_t)((*(uint16_t *)(v_stack_p8 + arg1 * 2)) + ((uint32_t)(Arg2)));
    Arg4 = (uint16_t)((Arg4) + (*(uint16_t *)(v_stack_p8 + arg1 * 2)));
    goto loc_008F2CCF;
loc_008F2F01:
    if (v_stack_p8 == 0) goto loc_008F2E4B;
    if (((uint16_t)(Arg3)) < ((uint16_t)(Arg2))) goto loc_008F2E4B;
    result = (Arg3) >> (8);
    Arg2 = (uint32_t)(((uint32_t)(Arg3)) & (15));
    result = (uint32_t)(((uint32_t)(Arg3)) >> (4));
    result = (uint32_t)((result) & (15));
    Arg1 = (uint32_t)((*(uint16_t *)(v_stack_p8 + result * 2)) + ((uint32_t)(result)));
    Arg1 = (uint32_t)((*(uint16_t *)(v_stack_p8 + arg1 * 2)) + ((uint32_t)(Arg2)));
    Arg3 = (uint16_t)((Arg3) + (*(uint16_t *)(v_stack_p8 + arg1 * 2)));
    goto loc_008F2E4B;
loc_008F2F45:
    if (v_stack_p8 == 0) goto loc_008F2E60;
    if (((uint16_t)(Arg4)) < 192) goto loc_008F2E60;
    result = (Arg4) >> (8);
    Arg2 = (uint32_t)(((uint32_t)(Arg4)) & (15));
    result = (uint32_t)(((uint32_t)(Arg4)) >> (4));
    result = (uint32_t)((result) & (15));
    Arg1 = (uint32_t)((*(uint16_t *)(v_stack_p8 + result * 2)) + ((uint32_t)(result)));
    Arg1 = (uint32_t)((*(uint16_t *)(v_stack_p8 + arg1 * 2)) + ((uint32_t)(Arg2)));
    Arg4 = (uint16_t)((Arg4) + (*(uint16_t *)(v_stack_p8 + arg1 * 2)));
    goto loc_008F2E60;
loc_008F2F84:
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(local_rsp - 0x3F - 0x39), Arg2, Arg3, Arg4);
    local_r13 = 0;
    local_rdi = ((uint32_t)(*(uint32_t *)(local_rsp - 0x3F - 0x49))) + ((uint32_t)(*(uint32_t *)(local_rsp - 0x3F - 0x49)));
    if (local_rdi > ((uint32_t)(0xFFFFFFFFULL))) goto loc_008F2FE3;
    goto loc_008F2BCD;
loc_008F2FAA:
    if (Arg1 != NULL) goto loc_008F3140;
    Arg1 = 0;
loc_008F2FB8:
    Arg2 = 0;
    result = SysCtxRegOpenCurrentUserKey(Arg1, Arg2, (uint32_t)(0x2000000ULL), local_rsp - 63 - 41);
    if (sign_flag) goto loc_008F2DD5;
    goto loc_008F2D7F;
loc_008F2FDC:
    Arg1 = 0;
    goto loc_008F2D9C;
loc_008F2FE3:
    goto loc_008F2DD5;
loc_008F2FED:
    if (((uint32_t)(result)) == 0xC000017CULL) goto loc_008F30C6;
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)(0xC0000034ULL)))) goto loc_008F30D0;
    Arg1 = 0;
    if ((*(uint8_t *)(local_rsp - 0x3F + 0x6F)) != 0) goto loc_008F3031;
    if (((uint32_t)((uint8_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x3F + 0x57))))) != 48) goto loc_008F302A;
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x3F + 0x57)))) & (0xF00ULL)) != 0) goto loc_008F302A;
    goto loc_008F2DD1;
loc_008F302A:
    goto loc_008F2DD1;
loc_008F3031:
    if (((uint32_t)((uint8_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x3F + 0x57))))) != 48) goto loc_008F314C;
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x3F + 0x57)))) & (0xF00ULL)) != 0) goto loc_008F314C;
loc_008F3046:
    result = CmGetDeviceInterfaceRegKeySecurityDescriptor(0, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x3F + 0x57)))), local_rsp - 63 - 65, local_rsp - 63 - 41);
    if (sign_flag) goto loc_008F2DD1;
    local_rdi = (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x3F + 0x67))));
    if (*(uint64_t *)(local_rsp - 0x3F - 0x41) != 0) { local_rdi = (uint32_t)((uint32_t)(0xE0006ULL)); }
    v_stack_p38 = *(uint64_t *)(local_rsp - 0x3F + 0x7F);
    Arg4 = 0;
    v_stack_p30 = local_rsp - 63 - 49;
    v_stack_p28 = *(uint64_t *)(local_rsp - 0x3F - 0x41);
    v_stack_p20 = (uint32_t)(local_rdi);
    result = PnpCtxRegCreateTree(0, *(uint64_t *)(local_rsp - 0x3F - 0x29), 0, Arg4);
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0xC000017CULL)))) goto loc_008F30C6;
    if (sign_flag) goto loc_008F30D0;
    if (((uint32_t)(local_rdi)) != ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x3F + 0x67))))) goto loc_008F3188;
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x77)) = *(uint64_t *)(local_rsp - 0x3F - 0x31);
    goto loc_008F2DD1;
loc_008F30C6:
    goto loc_008F2DD1;
loc_008F30D0:
    goto loc_008F2DD1;
loc_008F30D7:
    result = RtlPrefixUnicodeString(v_rip - 9377133, local_rsp - 63 - 17, 1, Arg4);
    if ((uint8_t)(result) == 0) goto loc_008F2D55;
    local_r15 = ((uint32_t)(0xC000017CULL)) + (36);
    goto loc_008F2D55;
loc_008F3101:
    Arg1 = (uint32_t)((14) - (4));
    Arg1 = (uint32_t)((Arg1) - (1));
    Arg1 = (uint32_t)((Arg1) - (1));
    Arg1 = (uint32_t)((Arg1) - (1));
    Arg1 = (uint32_t)((Arg1) - (1));
loc_008F3140:
    goto loc_008F2FB8;
loc_008F314C:
    v_stack_p38 = *(uint64_t *)(arg1 + 0xE0);
    Arg4 = 0;
    v_stack_p30 = local_rsp - 63 - 25;
    v_stack_p28 = (uint8_t)(*(uint64_t *)(arg1 + 0xE0));
    v_stack_p20 = 1;
    result = _CmOpenDeviceInterfaceRegKey(Arg1, *(uint64_t *)(local_rsp - 0x3F + 0x4F), Arg4 + 48, Arg4);
    if (sign_flag) goto loc_008F2DD1;
    goto loc_008F3046;
loc_008F3188:
    Arg4 = 0;
    v_stack_p28 = *(uint64_t *)(local_rsp - 0x3F + 0x77);
    Arg3 = 0;
    v_stack_p20 = 14;
    result = PnpCtxRegOpenKey(Arg1, *(uint64_t *)(local_rsp - 0x3F - 0x31), Arg3, Arg4);
    goto loc_008F2DD1;
loc_008F31B7:
    goto loc_008F2DD5;
loc_008F31C1:
    result = ZwClose(Arg1, *(uint64_t *)(local_rsp - 0x3F - 0x31), Arg3, Arg4);
    goto loc_008F2DE6;
loc_008F31CB:
    result = ZwClose(Arg1, *(uint64_t *)(local_rsp - 0x3F - 0x31), Arg3, Arg4);
    goto loc_008F2DF3;
loc_008F31D5:
    result = ZwClose(Arg1, *(uint64_t *)(local_rsp - 0x3F - 0x31), Arg3, Arg4);
    goto loc_008F2E00;
loc_008F31DF:
    Arg2 = 0;
    result = ExFreePoolWithTag(local_rdi, Arg2, Arg3, Arg4);
    goto loc_008F2E09;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x60 + rax*8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008F2B48&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
