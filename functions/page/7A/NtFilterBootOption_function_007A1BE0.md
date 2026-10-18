# NtFilterBootOption

- RVA: `0x007A1BE0`–`0x007A1FA1` (길이 `961` bytes)
- VA: `0x00000001407A1BE0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D15E4`
- 디코드: `256`개 명령, `961/961` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **11**; 고유 호출 대상: **10**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **11**

### Outgoing calls
- `0x007A1C31` → [HviIsAnyHypervisorPresent](../../text/4A/HviIsAnyHypervisorPresent_function_004ADC50.md) (function, `0x004ADC50`)
- `0x007A1C47` → [HviGetHypervisorFeatures](../../text/66/HviGetHypervisorFeatures_function_00666630.md) (function, `0x00666630`)
- `0x007A1C85` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x007A1CA0` → [RtlCheckTokenMembership](../../text/3A/RtlCheckTokenMembership_function_003A5A10.md) (function, `0x003A5A10`)
- `0x007A1DB9` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x007A1DD8` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x007A1E03` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x007A1EDB` → [SepSecureBootValidateBcdDataAgainstBcdRule](SepSecureBootValidateBcdDataAgainstBcdRule_function_007A26BC.md) (function, `0x007A26BC`)
- `0x007A1F31` → [SepSecureBootCorrectBcd](SepSecureBootCorrectBcd_function_007A2174.md) (function, `0x007A2174`)
- `0x007A1F72` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x007A1F81` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x007A1BF8` → RVA `0x00E0A740` (`.data`; read)
- `0x007A1C7E` → RVA `0x00FD9A78` (`PAGEDATA`; read)
- `0x007A1C97` → RVA `0x00FD9A68` (`PAGEDATA`; read)
- `0x007A1CBD` → RVA `0x00E67DF0` (`.data`; read)
- `0x007A1D1E` → RVA `0x00E67DD8` (`.data`; read)
- `0x007A1E43` → RVA `0x00E67DD0` (`.data`; read)
- `0x007A1E4E` → RVA `0x00E67DE0` (`.data`; read)
- `0x007A1E7A` → RVA `0x00E67E04` (`.data`; read)
- `0x007A1F22` → RVA `0x00E67DF8` (`.data`; read)
- `0x007A1F40` → RVA `0x00E67DFC` (`.data`; read)
- `0x007A1F4E` → RVA `0x00E67DF8` (`.data`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **8**
  - `0x007A1C31` → [HviIsAnyHypervisorPresent](../../text/4A/HviIsAnyHypervisorPresent_function_004ADC50.md) (`PAGE` → `.text`)
  - `0x007A1C47` → [HviGetHypervisorFeatures](../../text/66/HviGetHypervisorFeatures_function_00666630.md) (`PAGE` → `.text`)
  - `0x007A1CA0` → [RtlCheckTokenMembership](../../text/3A/RtlCheckTokenMembership_function_003A5A10.md) (`PAGE` → `.text`)
  - `0x007A1DB9` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x007A1DD8` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x007A1E03` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x007A1F72` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x007A1F81` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007A1BE0  4C 8B DC                        mov r11, rsp
007A1BE3  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
007A1BE7  49 89 73 10                     mov qword ptr [r11 + 0x10], rsi
007A1BEB  57                              push rdi
007A1BEC  41 54                           push r12
007A1BEE  41 55                           push r13
007A1BF0  41 56                           push r14
007A1BF2  41 57                           push r15
007A1BF4  48 83 EC 60                     sub rsp, 0x60
007A1BF8  48 8B 05 41 8B 66 00            mov rax, qword ptr [rip + 0x668b41]
007A1BFF  48 33 C4                        xor rax, rsp
007A1C02  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
007A1C07  45 8B E8                        mov r13d, r8d
007A1C0A  8B F2                           mov esi, edx
007A1C0C  89 54 24 30                     mov dword ptr [rsp + 0x30], edx
007A1C10  44 8B F1                        mov r14d, ecx
007A1C13  89 4C 24 34                     mov dword ptr [rsp + 0x34], ecx
007A1C17  4D 89 4B A0                     mov qword ptr [r11 - 0x60], r9
007A1C1B  44 8B A4 24 B0 00 00 00         mov r12d, dword ptr [rsp + 0xb0]
007A1C23  33 DB                           xor ebx, ebx
007A1C25  49 89 5B B0                     mov qword ptr [r11 - 0x50], rbx
007A1C29  88 5C 24 22                     mov byte ptr [rsp + 0x22], bl
007A1C2D  49 89 5B B8                     mov qword ptr [r11 - 0x48], rbx
007A1C31  E8 1A C0 D0 FF                  call 0x1404adc50
007A1C36  84 C0                           test al, al
007A1C38  74 2B                           je 0x1407a1c65
007A1C3A  0F 57 C0                        xorps xmm0, xmm0
007A1C3D  0F 11 44 24 48                  movups xmmword ptr [rsp + 0x48], xmm0
007A1C42  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
007A1C47  E8 E4 49 EC FF                  call 0x140666630
007A1C4C  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
007A1C51  48 C1 E8 2C                     shr rax, 0x2c
007A1C55  44 8D 7B 01                     lea r15d, [rbx + 1]
007A1C59  41 84 C7                        test r15b, al
007A1C5C  75 0D                           jne 0x1407a1c6b
007A1C5E  44 88 7C 24 21                  mov byte ptr [rsp + 0x21], r15b
007A1C63  EB 0A                           jmp 0x1407a1c6f
007A1C65  41 BF 01 00 00 00               mov r15d, 1
007A1C6B  88 5C 24 21                     mov byte ptr [rsp + 0x21], bl
007A1C6F  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
007A1C78  8A 90 32 02 00 00               mov dl, byte ptr [rax + 0x232]
007A1C7E  48 8B 0D F3 7D 83 00            mov rcx, qword ptr [rip + 0x837df3]
007A1C85  E8 96 01 0D 00                  call 0x140871e20
007A1C8A  88 44 24 20                     mov byte ptr [rsp + 0x20], al
007A1C8E  84 C0                           test al, al
007A1C90  75 25                           jne 0x1407a1cb7
007A1C92  4C 8D 44 24 20                  lea r8, [rsp + 0x20]
007A1C97  48 8B 15 CA 7D 83 00            mov rdx, qword ptr [rip + 0x837dca]
007A1C9E  33 C9                           xor ecx, ecx
007A1CA0  E8 6B 3D C0 FF                  call 0x1403a5a10
007A1CA5  85 C0                           test eax, eax
007A1CA7  0F 88 AE 02 00 00               js 0x1407a1f5b
007A1CAD  38 5C 24 20                     cmp byte ptr [rsp + 0x20], bl
007A1CB1  0F 84 A4 02 00 00               je 0x1407a1f5b
007A1CB7  89 5C 24 24                     mov dword ptr [rsp + 0x24], ebx
007A1CBB  8B FB                           mov edi, ebx
007A1CBD  48 39 1D 2C 61 6C 00            cmp qword ptr [rip + 0x6c612c], rbx
007A1CC4  75 0A                           jne 0x1407a1cd0
007A1CC6  BF 06 00 43 80                  mov edi, 0x80430006
007A1CCB  E9 90 02 00 00                  jmp 0x1407a1f60
007A1CD0  41 8B CE                        mov ecx, r14d
007A1CD3  45 85 F6                        test r14d, r14d
007A1CD6  0F 84 2F 02 00 00               je 0x1407a1f0b
007A1CDC  83 E9 01                        sub ecx, 1
007A1CDF  74 4E                           je 0x1407a1d2f
007A1CE1  83 F9 01                        cmp ecx, 1
007A1CE4  74 0A                           je 0x1407a1cf0
007A1CE6  BF EF 00 00 C0                  mov edi, 0xc00000ef
007A1CEB  E9 70 02 00 00                  jmp 0x1407a1f60
007A1CF0  85 F6                           test esi, esi
007A1CF2  0F 84 0C 02 00 00               je 0x1407a1f04
007A1CF8  45 85 ED                        test r13d, r13d
007A1CFB  0F 84 03 02 00 00               je 0x1407a1f04
007A1D01  48 39 5C 24 28                  cmp qword ptr [rsp + 0x28], rbx
007A1D06  0F 85 F8 01 00 00               jne 0x1407a1f04
007A1D0C  45 85 E4                        test r12d, r12d
007A1D0F  0F 85 EF 01 00 00               jne 0x1407a1f04
007A1D15  41 8B CD                        mov ecx, r13d
007A1D18  C1 E9 18                        shr ecx, 0x18
007A1D1B  83 E1 0F                        and ecx, 0xf
007A1D1E  8B 05 B4 60 6C 00               mov eax, dword ptr [rip + 0x6c60b4]
007A1D24  0F A3 C8                        bt eax, ecx
007A1D27  0F 82 FE 00 00 00               jb 0x1407a1e2b
007A1D2D  EB 39                           jmp 0x1407a1d68
007A1D2F  85 F6                           test esi, esi
007A1D31  0F 84 CD 01 00 00               je 0x1407a1f04
007A1D37  45 85 ED                        test r13d, r13d
007A1D3A  0F 84 C4 01 00 00               je 0x1407a1f04
007A1D40  48 39 5C 24 28                  cmp qword ptr [rsp + 0x28], rbx
007A1D45  0F 84 B9 01 00 00               je 0x1407a1f04
007A1D4B  45 85 E4                        test r12d, r12d
007A1D4E  0F 84 B0 01 00 00               je 0x1407a1f04
007A1D54  41 8B CD                        mov ecx, r13d
007A1D57  C1 E9 18                        shr ecx, 0x18
007A1D5A  83 E1 0F                        and ecx, 0xf
007A1D5D  8B 05 75 60 6C 00               mov eax, dword ptr [rip + 0x6c6075]
007A1D63  0F A3 C8                        bt eax, ecx
007A1D66  72 07                           jb 0x1407a1d6f
007A1D68  8B FB                           mov edi, ebx
007A1D6A  E9 F1 01 00 00                  jmp 0x1407a1f60
007A1D6F  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
007A1D78  38 98 32 02 00 00               cmp byte ptr [rax + 0x232], bl
007A1D7E  0F 84 A3 00 00 00               je 0x1407a1e27
007A1D84  48 8B 7C 24 28                  mov rdi, qword ptr [rsp + 0x28]
007A1D89  49 8D 04 3C                     lea rax, [r12 + rdi]
007A1D8D  48 B9 00 00 FF FF FF 7F 00 00   movabs rcx, 0x7fffffff0000
007A1D97  48 3B C1                        cmp rax, rcx
007A1D9A  77 05                           ja 0x1407a1da1
007A1D9C  48 3B C7                        cmp rax, rdi
007A1D9F  73 07                           jae 0x1407a1da8
007A1DA1  8A 01                           mov al, byte ptr [rcx]
007A1DA3  48 8B 7C 24 28                  mov rdi, qword ptr [rsp + 0x28]
007A1DA8  41 83 FC 08                     cmp r12d, 8
007A1DAC  77 1C                           ja 0x1407a1dca
007A1DAE  4D 8B C4                        mov r8, r12
007A1DB1  48 8B D7                        mov rdx, rdi
007A1DB4  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
007A1DB9  E8 82 4A F2 FF                  call 0x1406c6840
007A1DBE  48 8D 44 24 40                  lea rax, [rsp + 0x40]
007A1DC3  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
007A1DC8  EB 47                           jmp 0x1407a1e11
007A1DCA  41 B8 53 65 53 62               mov r8d, 0x62536553
007A1DD0  49 8B D4                        mov rdx, r12
007A1DD3  B9 00 01 00 00                  mov ecx, 0x100
007A1DD8  E8 13 03 3E 00                  call 0x140b820f0
007A1DDD  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
007A1DE2  48 85 C0                        test rax, rax
007A1DE5  75 0E                           jne 0x1407a1df5
007A1DE7  BF 17 00 00 C0                  mov edi, 0xc0000017
007A1DEC  89 7C 24 24                     mov dword ptr [rsp + 0x24], edi
007A1DF0  E9 6B 01 00 00                  jmp 0x1407a1f60
007A1DF5  4D 8B C4                        mov r8, r12
007A1DF8  48 8B D7                        mov rdx, rdi
007A1DFB  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
007A1E00  48 8B CE                        mov rcx, rsi
007A1E03  E8 38 4A F2 FF                  call 0x1406c6840
007A1E08  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
007A1E0D  8B 74 24 30                     mov esi, dword ptr [rsp + 0x30]
007A1E11  8B 7C 24 24                     mov edi, dword ptr [rsp + 0x24]
007A1E15  44 8B 74 24 34                  mov r14d, dword ptr [rsp + 0x34]
007A1E1A  EB 0F                           jmp 0x1407a1e2b
007A1E1C  8B F8                           mov edi, eax
007A1E1E  89 44 24 24                     mov dword ptr [rsp + 0x24], eax
007A1E22  E9 39 01 00 00                  jmp 0x1407a1f60
007A1E27  8B 7C 24 24                     mov edi, dword ptr [rsp + 0x24]
007A1E2B  44 8B C3                        mov r8d, ebx
007A1E2E  48 8B 05 BB 5F 6C 00            mov rax, qword ptr [rip + 0x6c5fbb]
007A1E35  44 0F B7 50 24                  movzx r10d, word ptr [rax + 0x24]
007A1E3A  45 85 D2                        test r10d, r10d
007A1E3D  0F 84 1D 01 00 00               je 0x1407a1f60
007A1E43  4C 8B 0D 86 5F 6C 00            mov r9, qword ptr [rip + 0x6c5f86]
007A1E4A  49 8D 49 04                     lea rcx, [r9 + 4]
007A1E4E  4C 8B 1D 8B 5F 6C 00            mov r11, qword ptr [rip + 0x6c5f8b]
007A1E55  44 39 29                        cmp dword ptr [rcx], r13d
007A1E58  75 58                           jne 0x1407a1eb2
007A1E5A  8B 41 FC                        mov eax, dword ptr [rcx - 4]
007A1E5D  85 C0                           test eax, eax
007A1E5F  74 04                           je 0x1407a1e65
007A1E61  3B C6                           cmp eax, esi
007A1E63  75 4D                           jne 0x1407a1eb2
007A1E65  8B 41 04                        mov eax, dword ptr [rcx + 4]
007A1E68  42 0F B7 14 18                  movzx edx, word ptr [rax + r11]
007A1E6D  F7 C2 00 F0 FF FF               test edx, 0xfffff000
007A1E73  75 3D                           jne 0x1407a1eb2
007A1E75  F6 C2 20                        test dl, 0x20
007A1E78  74 0A                           je 0x1407a1e84
007A1E7A  8B 05 84 5F 6C 00               mov eax, dword ptr [rip + 0x6c5f84]
007A1E80  A8 04                           test al, 4
007A1E82  74 2E                           je 0x1407a1eb2
007A1E84  F6 C2 40                        test dl, 0x40
007A1E87  74 0A                           je 0x1407a1e93
007A1E89  8B 05 75 5F 6C 00               mov eax, dword ptr [rip + 0x6c5f75]
007A1E8F  A8 10                           test al, 0x10
007A1E91  74 1F                           je 0x1407a1eb2
007A1E93  66 0F BA E2 0B                  bt dx, 0xb
007A1E98  73 0A                           jae 0x1407a1ea4
007A1E9A  8B 05 64 5F 6C 00               mov eax, dword ptr [rip + 0x6c5f64]
007A1EA0  A8 40                           test al, 0x40
007A1EA2  74 0E                           je 0x1407a1eb2
007A1EA4  38 5C 24 21                     cmp byte ptr [rsp + 0x21], bl
007A1EA8  74 19                           je 0x1407a1ec3
007A1EAA  81 39 31 00 00 25               cmp dword ptr [rcx], 0x25000031
007A1EB0  75 11                           jne 0x1407a1ec3
007A1EB2  45 03 C7                        add r8d, r15d
007A1EB5  48 83 C1 0C                     add rcx, 0xc
007A1EB9  45 3B C2                        cmp r8d, r10d
007A1EBC  72 97                           jb 0x1407a1e55
007A1EBE  E9 9D 00 00 00                  jmp 0x1407a1f60
007A1EC3  41 8B C0                        mov eax, r8d
007A1EC6  48 8D 0C 40                     lea rcx, [rax + rax*2]
007A1ECA  45 3B F7                        cmp r14d, r15d
007A1ECD  75 15                           jne 0x1407a1ee4
007A1ECF  49 8D 0C 89                     lea rcx, [r9 + rcx*4]
007A1ED3  45 8B C4                        mov r8d, r12d
007A1ED6  48 8B 54 24 28                  mov rdx, qword ptr [rsp + 0x28]
007A1EDB  E8 DC 07 00 00                  call 0x1407a26bc
007A1EE0  8B F8                           mov edi, eax
007A1EE2  EB 7C                           jmp 0x1407a1f60
007A1EE4  8B FB                           mov edi, ebx
007A1EE6  41 8B 4C 89 08                  mov ecx, dword ptr [r9 + rcx*4 + 8]
007A1EEB  42 8A 04 19                     mov al, byte ptr [rcx + r11]
007A1EEF  24 1F                           and al, 0x1f
007A1EF1  3C 08                           cmp al, 8
007A1EF3  75 08                           jne 0x1407a1efd
007A1EF5  66 42 39 5C 19 02               cmp word ptr [rcx + r11 + 2], bx
007A1EFB  74 63                           je 0x1407a1f60
007A1EFD  BF 02 00 43 C0                  mov edi, 0xc0430002
007A1F02  EB 5C                           jmp 0x1407a1f60
007A1F04  BF 0D 00 00 C0                  mov edi, 0xc000000d
007A1F09  EB 55                           jmp 0x1407a1f60
007A1F0B  85 F6                           test esi, esi
007A1F0D  75 F5                           jne 0x1407a1f04
007A1F0F  45 85 ED                        test r13d, r13d
007A1F12  75 F0                           jne 0x1407a1f04
007A1F14  48 39 5C 24 28                  cmp qword ptr [rsp + 0x28], rbx
007A1F19  75 E9                           jne 0x1407a1f04
007A1F1B  45 85 E4                        test r12d, r12d
007A1F1E  75 E4                           jne 0x1407a1f04
007A1F20  33 C0                           xor eax, eax
007A1F22  F0 0F B1 1D CE 5E 6C 00         lock cmpxchg dword ptr [rip + 0x6c5ece], ebx
007A1F2A  75 29                           jne 0x1407a1f55
007A1F2C  48 8D 4C 24 22                  lea rcx, [rsp + 0x22]
007A1F31  E8 3E 02 00 00                  call 0x1407a2174
007A1F36  8B F8                           mov edi, eax
007A1F38  89 44 24 24                     mov dword ptr [rsp + 0x24], eax
007A1F3C  85 C0                           test eax, eax
007A1F3E  78 20                           js 0x1407a1f60
007A1F40  38 1D B6 5E 6C 00               cmp byte ptr [rip + 0x6c5eb6], bl
007A1F46  75 06                           jne 0x1407a1f4e
007A1F48  38 5C 24 22                     cmp byte ptr [rsp + 0x22], bl
007A1F4C  75 12                           jne 0x1407a1f60
007A1F4E  44 87 3D A3 5E 6C 00            xchg dword ptr [rip + 0x6c5ea3], r15d
007A1F55  8B 7C 24 24                     mov edi, dword ptr [rsp + 0x24]
007A1F59  EB 05                           jmp 0x1407a1f60
007A1F5B  BF 22 00 00 C0                  mov edi, 0xc0000022
007A1F60  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
007A1F65  48 85 F6                        test rsi, rsi
007A1F68  74 0D                           je 0x1407a1f77
007A1F6A  BA 53 65 53 62                  mov edx, 0x62536553
007A1F6F  48 8B CE                        mov rcx, rsi
007A1F72  E8 F9 08 3E 00                  call 0x140b82870
007A1F77  8B C7                           mov eax, edi
007A1F79  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
007A1F7E  48 33 CC                        xor rcx, rsp
007A1F81  E8 BA A6 F0 FF                  call 0x1406ac640
007A1F86  4C 8D 5C 24 60                  lea r11, [rsp + 0x60]
007A1F8B  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
007A1F8F  49 8B 73 38                     mov rsi, qword ptr [r11 + 0x38]
007A1F93  49 8B E3                        mov rsp, r11
007A1F96  41 5F                           pop r15
007A1F98  41 5E                           pop r14
007A1F9A  41 5D                           pop r13
007A1F9C  41 5C                           pop r12
007A1F9E  5F                              pop rdi
007A1F9F  C3                              ret
007A1FA0  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NtFilterBootOption(int a1, int a2, int a3, __int64 a4, unsigned int a5)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned int v_stack_m54;
    unsigned int v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned int v_stack_m64;
    unsigned __int8 v_stack_m66;
    unsigned __int8 v_stack_m67;
    unsigned __int8 v_stack_m68;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rsi;
    v_rsp = (v_rsp) - (96);
    result = (*(unsigned __int64 *)(v_rip + 6720321)) ^ (v_rsp);
    v_stack_m30 = result;
    v_stack_m58 = a2;
    v_stack_m54 = a1;
    *(unsigned __int64 *)(v_rsp - 96) = a4;
    v_rbx = 0;
    *(unsigned __int64 *)(v_rsp - 80) = 0;
    v_stack_m66 = 0;
    *(unsigned __int64 *)(v_rsp - 72) = 0;
    result = HviIsAnyHypervisorPresent(a1, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_007A1C65;
    v_stack_m40 = v_xmm0;
    result = HviGetHypervisorFeatures(v_stack_m40, a2, a3, a4);
    result = (v_stack_m40) >> (44);
    if ((((unsigned __int8)(v_rbx + 1)) & ((unsigned __int8)(result))) != 0) goto loc_007A1C6B;
    v_stack_m67 = (unsigned __int8)(v_rbx + 1);
    goto loc_007A1C6F;
loc_007A1C65:
loc_007A1C6B:
    v_stack_m67 = 0;
loc_007A1C6F:
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 8617459), *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562), a3, a4);
    v_stack_m68 = (unsigned __int8)(result);
    if ((unsigned __int8)(result) != 0) goto loc_007A1CB7;
    a1 = 0;
    result = RtlCheckTokenMembership(a1, *(unsigned __int64 *)(v_rip + 8617418), v_stack_m68, a4);
    if (sign_flag) goto loc_007A1F5B;
    if (v_stack_m68 == 0) goto loc_007A1F5B;
loc_007A1CB7:
    v_stack_m64 = 0;
    if ((*(unsigned __int64 *)(v_rip + 7102764)) != 0) goto loc_007A1CD0;
    goto loc_007A1F60;
loc_007A1CD0:
    if ((unsigned int)((unsigned int)(a1)) == 0) goto loc_007A1F0B;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a1)))) - (1));
    if (condition_is_equal) goto loc_007A1D2F;
    if (a1 == 1) goto loc_007A1CF0;
    goto loc_007A1F60;
loc_007A1CF0:
    if ((unsigned int)((unsigned int)(a2)) == 0) goto loc_007A1F04;
    if ((unsigned int)((unsigned int)(a3)) == 0) goto loc_007A1F04;
    if (v_stack_m60 != 0) goto loc_007A1F04;
    if ((unsigned int)((unsigned int)(a5)) != 0) goto loc_007A1F04;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a3)))) >> (24));
    a1 = (unsigned int)((a1) & (15));
    if (condition_is_below) goto loc_007A1E2B;
    goto loc_007A1D68;
loc_007A1D2F:
    if ((unsigned int)((unsigned int)(a2)) == 0) goto loc_007A1F04;
    if ((unsigned int)((unsigned int)(a3)) == 0) goto loc_007A1F04;
    if (v_stack_m60 == 0) goto loc_007A1F04;
    if ((unsigned int)((unsigned int)(a5)) == 0) goto loc_007A1F04;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a3)))) >> (24));
    a1 = (unsigned int)((a1) & (15));
    if (condition_is_below) goto loc_007A1D6F;
loc_007A1D68:
    goto loc_007A1F60;
loc_007A1D6F:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == 0) goto loc_007A1E27;
    if (((unsigned int)(a5) + v_stack_m60 * 1) > a1) goto loc_007A1DA1;
    result = (unsigned int)(a5) + v_stack_m60 * 1;
    v_rdi = v_stack_m60;
    if (((unsigned int)(a5) + v_stack_m60 * 1) < v_stack_m60) {
        result = *(unsigned __int8 *)(a1);
        v_rdi = v_stack_m60;
    }
    if (((unsigned int)((unsigned int)(a5))) > 8) goto loc_007A1DCA;
    result = memcpy(v_stack_m48, v_rdi, (unsigned int)(a5), a4);
    v_stack_m60 = v_stack_m48;
    goto loc_007A1E11;
loc_007A1DCA:
    result = ExAllocatePool2(256, (unsigned int)(a5), (unsigned int)(0x62536553ULL), a4);
    v_stack_m50 = result;
    if (result != 0) goto loc_007A1DF5;
    v_stack_m64 = (unsigned int)((unsigned int)(0xC0000017ULL));
    goto loc_007A1F60;
loc_007A1DF5:
    result = memcpy(v_stack_m50, (unsigned int)(0xC0000017ULL), (unsigned int)(a5), a4);
    v_stack_m60 = v_stack_m50;
loc_007A1E11:
    goto loc_007A1E2B;
loc_007A1E27:
loc_007A1E2B:
    if ((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 7102395) + 36)) == 0) goto loc_007A1F60;
loc_007A1E55:
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rip + 7102342) + 4)) != ((unsigned int)((unsigned int)(a3)))) goto loc_007A1EB2;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 7102342) + 4 - 4))) == 0) goto loc_007A1E65;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 7102342) + 4 - 4)))) != ((unsigned int)((unsigned int)(v_stack_m58)))) goto loc_007A1EB2;
loc_007A1E65:
    if ((((unsigned int)(*(unsigned __int16 *)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 7102342) + 4 + 4)) + *(unsigned __int64 *)(v_rip + 7102347) * 1))) & (0xFFFFF000ULL)) != 0) goto loc_007A1EB2;
    if ((((unsigned __int8)(*(unsigned __int16 *)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 7102342) + 4 + 4)) + *(unsigned __int64 *)(v_rip + 7102347) * 1))) & (32)) == 0) goto loc_007A1E84;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 7102340)))) & (4)) == 0) goto loc_007A1EB2;
loc_007A1E84:
    if ((((unsigned __int8)(*(unsigned __int16 *)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 7102342) + 4 + 4)) + *(unsigned __int64 *)(v_rip + 7102347) * 1))) & (64)) == 0) goto loc_007A1E93;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 7102325)))) & (16)) == 0) goto loc_007A1EB2;
loc_007A1E93:
    if (condition_is_above_or_equal) goto loc_007A1EA4;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 7102308)))) & (64)) == 0) goto loc_007A1EB2;
loc_007A1EA4:
    if (v_stack_m67 == 0) goto loc_007A1EC3;
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rip + 7102342) + 4)) != 0x25000031ULL) goto loc_007A1EC3;
loc_007A1EB2:
    a3 = (unsigned int)((0) + (1));
    a1 = (*(unsigned __int64 *)(v_rip + 7102342) + 4) + (12);
    if (a3 < ((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 7102395) + 36)))) goto loc_007A1E55;
    goto loc_007A1F60;
loc_007A1EC3:
    if (((unsigned int)((unsigned int)(v_stack_m54))) != 1) goto loc_007A1EE4;
    result = SepSecureBootValidateBcdDataAgainstBcdRule(*(unsigned __int64 *)(v_rip + 7102342) + (unsigned int)(a3) + (unsigned int)(a3) * 2 * 4, v_stack_m60, (unsigned int)((unsigned int)((unsigned int)(a5))), *(unsigned __int64 *)(v_rip + 7102342));
    goto loc_007A1F60;
loc_007A1EE4:
    result = (unsigned __int8)((*(unsigned __int8 *)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 7102342) + *(unsigned __int64 *)(v_rip + 7102342) + (unsigned int)(a3) + (unsigned int)(a3) * 2 * 4 * 4 + 8)) + *(unsigned __int64 *)(v_rip + 7102347) * 1)) & (31));
    if (((unsigned __int8)(result)) != 8) goto loc_007A1EFD;
    if ((*(unsigned __int16 *)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 7102342) + *(unsigned __int64 *)(v_rip + 7102342) + (unsigned int)(a3) + (unsigned int)(a3) * 2 * 4 * 4 + 8)) + *(unsigned __int64 *)(v_rip + 7102347) * 1 + 2)) == 0) goto loc_007A1F60;
loc_007A1EFD:
    goto loc_007A1F60;
loc_007A1F04:
    goto loc_007A1F60;
loc_007A1F0B:
    if ((unsigned int)((unsigned int)(v_stack_m58)) != 0) goto loc_007A1F04;
    if ((unsigned int)((unsigned int)(a3)) != 0) goto loc_007A1F04;
    if (v_stack_m60 != 0) goto loc_007A1F04;
    if ((unsigned int)((unsigned int)(a5)) != 0) goto loc_007A1F04;
    result = 0;
    if (condition_is_not_equal) goto loc_007A1F55;
    result = SepSecureBootCorrectBcd(v_stack_m66, v_stack_m60, (unsigned int)((unsigned int)((unsigned int)(a5))), *(unsigned __int64 *)(v_rip + 7102342));
    v_stack_m64 = (unsigned int)(result);
    if (sign_flag) goto loc_007A1F60;
    if ((*(unsigned __int8 *)(v_rip + 7102134)) != 0) goto loc_007A1F4E;
    if (v_stack_m66 != 0) goto loc_007A1F60;
loc_007A1F4E:
loc_007A1F55:
    goto loc_007A1F60;
loc_007A1F5B:
loc_007A1F60:
    if (v_stack_m50 != 0) {
        a2 = 0x62536553ULL;
        a1 = v_stack_m50;
        result = ExFreePoolWithTag(a1, a2, (unsigned int)((unsigned int)((unsigned int)(a5))), *(unsigned __int64 *)(v_rip + 7102342));
    }
    a1 = (v_stack_m30) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, (unsigned int)((unsigned int)((unsigned int)(a5))), *(unsigned __int64 *)(v_rip + 7102342));
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t NtFilterBootOption(int32_t Arg1, int32_t Arg2, int32_t Arg3, int64_t Arg4, uint32_t Arg5)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint32_t v_stack_m54;
    uint32_t v_stack_m58;
    uint64_t v_stack_m60;
    uint32_t v_stack_m64;
    uint8_t v_stack_m66;
    uint8_t v_stack_m67;
    uint8_t v_stack_m68;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rsi;
    local_rsp = (local_rsp) - (96);
    result = (*(uint64_t *)(v_rip + 0x668B41)) ^ (local_rsp);
    v_stack_m30 = result;
    v_stack_m58 = Arg2;
    v_stack_m54 = Arg1;
    *(uint64_t *)(local_rsp - 0x60) = Arg4;
    local_rbx = 0;
    *(uint64_t *)(local_rsp - 0x50) = 0;
    v_stack_m66 = 0;
    *(uint64_t *)(local_rsp - 0x48) = 0;
    result = HviIsAnyHypervisorPresent(Arg1, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_007A1C65;
    v_stack_m40 = v_xmm0;
    result = HviGetHypervisorFeatures(v_stack_m40, Arg2, Arg3, Arg4);
    result = (v_stack_m40) >> (44);
    if ((((uint8_t)(local_rbx + 1)) & ((uint8_t)(result))) != 0) goto loc_007A1C6B;
    v_stack_m67 = (uint8_t)(local_rbx + 1);
    goto loc_007A1C6F;
loc_007A1C65:
loc_007A1C6B:
    v_stack_m67 = 0;
loc_007A1C6F:
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x837DF3), *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232), Arg3, Arg4);
    v_stack_m68 = (uint8_t)(result);
    if ((uint8_t)(result) != 0) goto loc_007A1CB7;
    Arg1 = 0;
    result = RtlCheckTokenMembership(Arg1, *(uint64_t *)(v_rip + 0x837DCA), v_stack_m68, Arg4);
    if (sign_flag) goto loc_007A1F5B;
    if (v_stack_m68 == 0) goto loc_007A1F5B;
loc_007A1CB7:
    v_stack_m64 = 0;
    if ((*(uint64_t *)(v_rip + 0x6C612C)) != 0) goto loc_007A1CD0;
    goto loc_007A1F60;
loc_007A1CD0:
    if ((uint32_t)((uint32_t)(Arg1)) == 0) goto loc_007A1F0B;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg1)))) - (1));
    if (condition_is_equal) goto loc_007A1D2F;
    if (Arg1 == 1) goto loc_007A1CF0;
    goto loc_007A1F60;
loc_007A1CF0:
    if ((uint32_t)((uint32_t)(Arg2)) == 0) goto loc_007A1F04;
    if ((uint32_t)((uint32_t)(Arg3)) == 0) goto loc_007A1F04;
    if (v_stack_m60 != 0) goto loc_007A1F04;
    if ((uint32_t)((uint32_t)(Arg5)) != 0) goto loc_007A1F04;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg3)))) >> (24));
    Arg1 = (uint32_t)((Arg1) & (15));
    if (condition_is_below) goto loc_007A1E2B;
    goto loc_007A1D68;
loc_007A1D2F:
    if ((uint32_t)((uint32_t)(Arg2)) == 0) goto loc_007A1F04;
    if ((uint32_t)((uint32_t)(Arg3)) == 0) goto loc_007A1F04;
    if (v_stack_m60 == 0) goto loc_007A1F04;
    if ((uint32_t)((uint32_t)(Arg5)) == 0) goto loc_007A1F04;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg3)))) >> (24));
    Arg1 = (uint32_t)((Arg1) & (15));
    if (condition_is_below) goto loc_007A1D6F;
loc_007A1D68:
    goto loc_007A1F60;
loc_007A1D6F:
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == 0) goto loc_007A1E27;
    if (((uint32_t)(Arg5) + v_stack_m60 * 1) > Arg1) goto loc_007A1DA1;
    result = (uint32_t)(Arg5) + v_stack_m60 * 1;
    local_rdi = v_stack_m60;
    if (((uint32_t)(Arg5) + v_stack_m60 * 1) < v_stack_m60) {
        result = *(uint8_t *)(Arg1);
        local_rdi = v_stack_m60;
    }
    if (((uint32_t)((uint32_t)(Arg5))) > 8) goto loc_007A1DCA;
    result = memcpy(v_stack_m48, local_rdi, (uint32_t)(Arg5), Arg4);
    v_stack_m60 = v_stack_m48;
    goto loc_007A1E11;
loc_007A1DCA:
    result = ExAllocatePool2(256, (uint32_t)(Arg5), (uint32_t)(0x62536553ULL), Arg4);
    v_stack_m50 = result;
    if (result != 0) goto loc_007A1DF5;
    v_stack_m64 = (uint32_t)((uint32_t)(0xC0000017ULL));
    goto loc_007A1F60;
loc_007A1DF5:
    result = memcpy(v_stack_m50, (uint32_t)(0xC0000017ULL), (uint32_t)(Arg5), Arg4);
    v_stack_m60 = v_stack_m50;
loc_007A1E11:
    goto loc_007A1E2B;
loc_007A1E27:
loc_007A1E2B:
    if ((uint32_t)(*(uint16_t *)(*(uint64_t *)(v_rip + 0x6C5FBB) + 0x24)) == 0) goto loc_007A1F60;
loc_007A1E55:
    if ((*(uint32_t *)(*(uint64_t *)(v_rip + 0x6C5F86) + 0x4)) != ((uint32_t)((uint32_t)(Arg3)))) goto loc_007A1EB2;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x6C5F86) + 0x4 - 0x4))) == 0) goto loc_007A1E65;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x6C5F86) + 0x4 - 0x4)))) != ((uint32_t)((uint32_t)(v_stack_m58)))) goto loc_007A1EB2;
loc_007A1E65:
    if ((((uint32_t)(*(uint16_t *)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x6C5F86) + 0x4 + 0x4)) + *(uint64_t *)(v_rip + 0x6C5F8B) * 1))) & (0xFFFFF000ULL)) != 0) goto loc_007A1EB2;
    if ((((uint8_t)(*(uint16_t *)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x6C5F86) + 0x4 + 0x4)) + *(uint64_t *)(v_rip + 0x6C5F8B) * 1))) & (32)) == 0) goto loc_007A1E84;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x6C5F84)))) & (4)) == 0) goto loc_007A1EB2;
loc_007A1E84:
    if ((((uint8_t)(*(uint16_t *)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x6C5F86) + 0x4 + 0x4)) + *(uint64_t *)(v_rip + 0x6C5F8B) * 1))) & (64)) == 0) goto loc_007A1E93;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x6C5F75)))) & (16)) == 0) goto loc_007A1EB2;
loc_007A1E93:
    if (condition_is_above_or_equal) goto loc_007A1EA4;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x6C5F64)))) & (64)) == 0) goto loc_007A1EB2;
loc_007A1EA4:
    if (v_stack_m67 == 0) goto loc_007A1EC3;
    if ((*(uint32_t *)(*(uint64_t *)(v_rip + 0x6C5F86) + 0x4)) != 0x25000031ULL) goto loc_007A1EC3;
loc_007A1EB2:
    Arg3 = (uint32_t)((0) + (1));
    Arg1 = (*(uint64_t *)(v_rip + 0x6C5F86) + 4) + (12);
    if (Arg3 < ((uint32_t)(*(uint16_t *)(*(uint64_t *)(v_rip + 0x6C5FBB) + 0x24)))) goto loc_007A1E55;
    goto loc_007A1F60;
loc_007A1EC3:
    if (((uint32_t)((uint32_t)(v_stack_m54))) != 1) goto loc_007A1EE4;
    result = SepSecureBootValidateBcdDataAgainstBcdRule(*(uint64_t *)(v_rip + 0x6C5F86) + (uint32_t)(Arg3) + (uint32_t)(Arg3) * 2 * 4, v_stack_m60, (uint32_t)((uint32_t)((uint32_t)(Arg5))), *(uint64_t *)(v_rip + 0x6C5F86));
    goto loc_007A1F60;
loc_007A1EE4:
    result = (uint8_t)((*(uint8_t *)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x6C5F86) + *(uint64_t *)(v_rip + 0x6C5F86) + (uint32_t)(Arg3) + (uint32_t)(Arg3) * 2 * 4 * 4 + 0x8)) + *(uint64_t *)(v_rip + 0x6C5F8B) * 1)) & (31));
    if (((uint8_t)(result)) != 8) goto loc_007A1EFD;
    if ((*(uint16_t *)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x6C5F86) + *(uint64_t *)(v_rip + 0x6C5F86) + (uint32_t)(Arg3) + (uint32_t)(Arg3) * 2 * 4 * 4 + 0x8)) + *(uint64_t *)(v_rip + 0x6C5F8B) * 1 + 0x2)) == 0) goto loc_007A1F60;
loc_007A1EFD:
    goto loc_007A1F60;
loc_007A1F04:
    goto loc_007A1F60;
loc_007A1F0B:
    if ((uint32_t)((uint32_t)(v_stack_m58)) != 0) goto loc_007A1F04;
    if ((uint32_t)((uint32_t)(Arg3)) != 0) goto loc_007A1F04;
    if (v_stack_m60 != 0) goto loc_007A1F04;
    if ((uint32_t)((uint32_t)(Arg5)) != 0) goto loc_007A1F04;
    result = 0;
    if (condition_is_not_equal) goto loc_007A1F55;
    result = SepSecureBootCorrectBcd(v_stack_m66, v_stack_m60, (uint32_t)((uint32_t)((uint32_t)(Arg5))), *(uint64_t *)(v_rip + 0x6C5F86));
    v_stack_m64 = (uint32_t)(result);
    if (sign_flag) goto loc_007A1F60;
    if ((*(uint8_t *)(v_rip + 0x6C5EB6)) != 0) goto loc_007A1F4E;
    if (v_stack_m66 != 0) goto loc_007A1F60;
loc_007A1F4E:
loc_007A1F55:
    goto loc_007A1F60;
loc_007A1F5B:
loc_007A1F60:
    if (v_stack_m50 != 0) {
        Arg2 = 0x62536553ULL;
        Arg1 = v_stack_m50;
        result = ExFreePoolWithTag(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg5))), *(uint64_t *)(v_rip + 0x6C5F86));
    }
    Arg1 = (v_stack_m30) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg5))), *(uint64_t *)(v_rip + 0x6C5F86));
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007A1BE0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
