# CmServiceFilterCallback

- RVA: `0x0082D7A0`–`0x0082DBD8` (길이 `1,080` bytes)
- VA: `0x000000014082D7A0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C6DB4`
- 디코드: `286`개 명령, `1,080/1,080` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **15**; 고유 호출 대상: **8**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0082D821` → [RtlInitUnicodeStringEx](../../text/46/RtlInitUnicodeStringEx_function_00463960.md) (function, `0x00463960`)
- `0x0082D869` → [CmGetDeviceRegProp](../8E/CmGetDeviceRegProp_function_008ED870.md) (function, `0x008ED870`)
- `0x0082D89D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0082D8B3` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0082D8FE` → [RtlInitUnicodeStringEx](../../text/46/RtlInitUnicodeStringEx_function_00463960.md) (function, `0x00463960`)
- `0x0082D916` → [RtlEqualUnicodeString](../93/RtlEqualUnicodeString_function_00932A20.md) (function, `0x00932A20`)
- `0x0082D9A1` → [CmGetDeviceRegProp](../8E/CmGetDeviceRegProp_function_008ED870.md) (function, `0x008ED870`)
- `0x0082DA18` → [CmGetDeviceRegProp](../8E/CmGetDeviceRegProp_function_008ED870.md) (function, `0x008ED870`)
- `0x0082DA51` → [CmGetInstallerClassRegProp](../99/CmGetInstallerClassRegProp_function_00994940.md) (function, `0x00994940`)
- `0x0082DAB3` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0082DAC9` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0082DB4B` → [RtlInitUnicodeStringEx](../../text/46/RtlInitUnicodeStringEx_function_00463960.md) (function, `0x00463960`)
- `0x0082DB63` → [RtlEqualUnicodeString](../93/RtlEqualUnicodeString_function_00932A20.md) (function, `0x00932A20`)
- `0x0082DBAC` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0082DBBE` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0082D7B9` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **9**
  - `0x0082D821` → [RtlInitUnicodeStringEx](../../text/46/RtlInitUnicodeStringEx_function_00463960.md) (`PAGE` → `.text`)
  - `0x0082D89D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0082D8B3` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0082D8FE` → [RtlInitUnicodeStringEx](../../text/46/RtlInitUnicodeStringEx_function_00463960.md) (`PAGE` → `.text`)
  - `0x0082DAB3` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0082DAC9` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0082DB4B` → [RtlInitUnicodeStringEx](../../text/46/RtlInitUnicodeStringEx_function_00463960.md) (`PAGE` → `.text`)
  - `0x0082DBAC` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x0082DBBE` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0082D7A0  40 55                           push rbp
0082D7A2  53                              push rbx
0082D7A3  56                              push rsi
0082D7A4  57                              push rdi
0082D7A5  41 54                           push r12
0082D7A7  41 55                           push r13
0082D7A9  41 56                           push r14
0082D7AB  41 57                           push r15
0082D7AD  48 8D 6C 24 F8                  lea rbp, [rsp - 8]
0082D7B2  48 81 EC 08 01 00 00            sub rsp, 0x108
0082D7B9  48 8B 05 80 CF 5D 00            mov rax, qword ptr [rip + 0x5dcf80]
0082D7C0  48 33 C4                        xor rax, rsp
0082D7C3  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
0082D7C7  49 8B D9                        mov rbx, r9
0082D7CA  44 89 44 24 48                  mov dword ptr [rsp + 0x48], r8d
0082D7CF  45 33 C9                        xor r9d, r9d
0082D7D2  48 89 54 24 58                  mov qword ptr [rsp + 0x58], rdx
0082D7D7  48 89 4C 24 50                  mov qword ptr [rsp + 0x50], rcx
0082D7DC  0F 57 C0                        xorps xmm0, xmm0
0082D7DF  44 89 4C 24 40                  mov dword ptr [rsp + 0x40], r9d
0082D7E4  0F 57 C9                        xorps xmm1, xmm1
0082D7E7  44 89 4C 24 44                  mov dword ptr [rsp + 0x44], r9d
0082D7EC  4C 8B FA                        mov r15, rdx
0082D7EF  4C 8B F1                        mov r14, rcx
0082D7F2  41 8A F9                        mov dil, r9b
0082D7F5  0F 11 45 88                     movups xmmword ptr [rbp - 0x78], xmm0
0082D7F9  0F 11 4C 24 78                  movups xmmword ptr [rsp + 0x78], xmm1
0082D7FE  48 85 DB                        test rbx, rbx
0082D801  0F 84 AD 03 00 00               je 0x14082dbb4
0082D807  48 8B 13                        mov rdx, qword ptr [rbx]
0082D80A  48 85 D2                        test rdx, rdx
0082D80D  0F 84 83 03 00 00               je 0x14082db96
0082D813  66 44 39 0A                     cmp word ptr [rdx], r9w
0082D817  0F 84 79 03 00 00               je 0x14082db96
0082D81D  48 8D 4D 88                     lea rcx, [rbp - 0x78]
0082D821  E8 3A 61 C3 FF                  call 0x140463960
0082D826  45 33 C9                        xor r9d, r9d
0082D829  85 C0                           test eax, eax
0082D82B  0F 88 83 03 00 00               js 0x14082dbb4
0082D831  8B 43 10                        mov eax, dword ptr [rbx + 0x10]
0082D834  45 33 C0                        xor r8d, r8d
0082D837  44 89 4C 24 38                  mov dword ptr [rsp + 0x38], r9d
0082D83C  49 8B D7                        mov rdx, r15
0082D83F  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
0082D843  41 B9 05 00 00 00               mov r9d, 5
0082D849  48 8D 44 24 40                  lea rax, [rsp + 0x40]
0082D84E  49 8B CE                        mov rcx, r14
0082D851  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0082D856  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
0082D85A  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0082D85F  48 8D 44 24 44                  lea rax, [rsp + 0x44]
0082D864  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0082D869  E8 02 00 0C 00                  call 0x1408ed870
0082D86E  8B F8                           mov edi, eax
0082D870  45 33 C9                        xor r9d, r9d
0082D873  8B 44 24 40                     mov eax, dword ptr [rsp + 0x40]
0082D877  B9 0D 00 00 C0                  mov ecx, 0xc000000d
0082D87C  85 FF                           test edi, edi
0082D87E  75 05                           jne 0x14082d885
0082D880  83 F8 02                        cmp eax, 2
0082D883  72 4B                           jb 0x14082d8d0
0082D885  81 FF 23 00 00 C0               cmp edi, 0xc0000023
0082D88B  75 52                           jne 0x14082d8df
0082D88D  83 F8 02                        cmp eax, 2
0082D890  72 3E                           jb 0x14082d8d0
0082D892  48 8B 4B 08                     mov rcx, qword ptr [rbx + 8]
0082D896  48 85 C9                        test rcx, rcx
0082D899  74 0B                           je 0x14082d8a6
0082D89B  33 D2                           xor edx, edx
0082D89D  E8 CE 4F 35 00                  call 0x140b82870
0082D8A2  8B 44 24 40                     mov eax, dword ptr [rsp + 0x40]
0082D8A6  8B D0                           mov edx, eax
0082D8A8  B9 00 01 00 00                  mov ecx, 0x100
0082D8AD  41 B8 50 4E 50 52               mov r8d, 0x52504e50
0082D8B3  E8 38 48 35 00                  call 0x140b820f0
0082D8B8  45 33 C9                        xor r9d, r9d
0082D8BB  48 89 43 08                     mov qword ptr [rbx + 8], rax
0082D8BF  48 85 C0                        test rax, rax
0082D8C2  74 10                           je 0x14082d8d4
0082D8C4  8B 44 24 40                     mov eax, dword ptr [rsp + 0x40]
0082D8C8  89 43 10                        mov dword ptr [rbx + 0x10], eax
0082D8CB  E9 61 FF FF FF                  jmp 0x14082d831
0082D8D0  8B F1                           mov esi, ecx
0082D8D2  EB 52                           jmp 0x14082d926
0082D8D4  44 89 4B 10                     mov dword ptr [rbx + 0x10], r9d
0082D8D8  BE 17 00 00 C0                  mov esi, 0xc0000017
0082D8DD  EB 47                           jmp 0x14082d926
0082D8DF  8B F7                           mov esi, edi
0082D8E1  85 FF                           test edi, edi
0082D8E3  75 41                           jne 0x14082d926
0082D8E5  8B 4B 10                        mov ecx, dword ptr [rbx + 0x10]
0082D8E8  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
0082D8EC  48 D1 E9                        shr rcx, 1
0082D8EF  66 44 89 4C 48 FE               mov word ptr [rax + rcx*2 - 2], r9w
0082D8F5  48 8D 4C 24 78                  lea rcx, [rsp + 0x78]
0082D8FA  48 8B 53 08                     mov rdx, qword ptr [rbx + 8]
0082D8FE  E8 5D 60 C3 FF                  call 0x140463960
0082D903  45 33 C9                        xor r9d, r9d
0082D906  85 C0                           test eax, eax
0082D908  78 1C                           js 0x14082d926
0082D90A  41 B0 01                        mov r8b, 1
0082D90D  48 8D 54 24 78                  lea rdx, [rsp + 0x78]
0082D912  48 8D 4D 88                     lea rcx, [rbp - 0x78]
0082D916  E8 05 51 10 00                  call 0x140932a20
0082D91B  45 33 C9                        xor r9d, r9d
0082D91E  84 C0                           test al, al
0082D920  0F 85 6B 02 00 00               jne 0x14082db91
0082D926  C7 44 24 60 01 00 00 00         mov dword ptr [rsp + 0x60], 1
0082D92E  48 8D 44 24 60                  lea rax, [rsp + 0x60]
0082D933  C7 44 24 64 02 00 00 00         mov dword ptr [rsp + 0x64], 2
0082D93B  45 8B E9                        mov r13d, r9d
0082D93E  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
0082D943  41 8A F9                        mov dil, r9b
0082D946  41 83 FD 02                     cmp r13d, 2
0082D94A  0F 83 64 02 00 00               jae 0x14082dbb4
0082D950  44 8B 20                        mov r12d, dword ptr [rax]
0082D953  C7 44 24 68 12 00 00 00         mov dword ptr [rsp + 0x68], 0x12
0082D95B  C7 44 24 6C 13 00 00 00         mov dword ptr [rsp + 0x6c], 0x13
0082D963  41 83 FC 02                     cmp r12d, 2
0082D967  75 68                           jne 0x14082d9d1
0082D969  44 89 4C 24 38                  mov dword ptr [rsp + 0x38], r9d
0082D96E  48 8D 44 24 40                  lea rax, [rsp + 0x40]
0082D973  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0082D978  45 8D 4C 24 07                  lea r9d, [r12 + 7]
0082D97D  48 8D 45 A0                     lea rax, [rbp - 0x60]
0082D981  C7 44 24 40 4E 00 00 00         mov dword ptr [rsp + 0x40], 0x4e
0082D989  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0082D98E  45 33 C0                        xor r8d, r8d
0082D991  48 8D 44 24 44                  lea rax, [rsp + 0x44]
0082D996  49 8B D7                        mov rdx, r15
0082D999  49 8B CE                        mov rcx, r14
0082D99C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0082D9A1  E8 CA FE 0B 00                  call 0x1408ed870
0082D9A6  45 33 C9                        xor r9d, r9d
0082D9A9  8B F0                           mov esi, eax
0082D9AB  41 8A F9                        mov dil, r9b
0082D9AE  85 C0                           test eax, eax
0082D9B0  0F 88 FE 01 00 00               js 0x14082dbb4
0082D9B6  83 7C 24 44 01                  cmp dword ptr [rsp + 0x44], 1
0082D9BB  0F 85 F3 01 00 00               jne 0x14082dbb4
0082D9C1  44 39 64 24 40                  cmp dword ptr [rsp + 0x40], r12d
0082D9C6  0F 82 E8 01 00 00               jb 0x14082dbb4
0082D9CC  66 44 89 4D EC                  mov word ptr [rbp - 0x14], r9w
0082D9D1  45 8B F9                        mov r15d, r9d
0082D9D4  4C 8D 74 24 68                  lea r14, [rsp + 0x68]
0082D9D9  8B 43 10                        mov eax, dword ptr [rbx + 0x10]
0082D9DC  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
0082D9E0  41 83 FC 01                     cmp r12d, 1
0082D9E4  75 39                           jne 0x14082da1f
0082D9E6  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
0082D9EB  48 8D 44 24 40                  lea rax, [rsp + 0x40]
0082D9F0  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
0082D9F5  45 33 C0                        xor r8d, r8d
0082D9F8  44 89 4C 24 38                  mov dword ptr [rsp + 0x38], r9d
0082D9FD  45 8B 0E                        mov r9d, dword ptr [r14]
0082DA00  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0082DA05  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
0082DA09  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0082DA0E  48 8D 44 24 44                  lea rax, [rsp + 0x44]
0082DA13  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0082DA18  E8 53 FE 0B 00                  call 0x1408ed870
0082DA1D  EB 37                           jmp 0x14082da56
0082DA1F  41 83 FC 02                     cmp r12d, 2
0082DA23  75 3A                           jne 0x14082da5f
0082DA25  45 8B 0E                        mov r9d, dword ptr [r14]
0082DA28  48 8D 44 24 40                  lea rax, [rsp + 0x40]
0082DA2D  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
0082DA32  48 8D 55 A0                     lea rdx, [rbp - 0x60]
0082DA36  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0082DA3B  45 33 C0                        xor r8d, r8d
0082DA3E  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
0082DA42  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0082DA47  48 8D 44 24 44                  lea rax, [rsp + 0x44]
0082DA4C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0082DA51  E8 EA 6E 16 00                  call 0x140994940
0082DA56  8B F0                           mov esi, eax
0082DA58  45 33 C9                        xor r9d, r9d
0082DA5B  8B 44 24 40                     mov eax, dword ptr [rsp + 0x40]
0082DA5F  8B D6                           mov edx, esi
0082DA61  85 F6                           test esi, esi
0082DA63  75 36                           jne 0x14082da9b
0082DA65  83 F8 02                        cmp eax, 2
0082DA68  73 31                           jae 0x14082da9b
0082DA6A  BE 0D 00 00 C0                  mov esi, 0xc000000d
0082DA6F  41 FF C7                        inc r15d
0082DA72  49 83 C6 04                     add r14, 4
0082DA76  41 83 FF 02                     cmp r15d, 2
0082DA7A  0F 82 59 FF FF FF               jb 0x14082d9d9
0082DA80  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
0082DA85  41 FF C5                        inc r13d
0082DA88  4C 8B 74 24 50                  mov r14, qword ptr [rsp + 0x50]
0082DA8D  48 83 C0 04                     add rax, 4
0082DA91  4C 8B 7C 24 58                  mov r15, qword ptr [rsp + 0x58]
0082DA96  E9 A3 FE FF FF                  jmp 0x14082d93e
0082DA9B  81 FE 23 00 00 C0               cmp esi, 0xc0000023
0082DAA1  75 51                           jne 0x14082daf4
0082DAA3  83 F8 02                        cmp eax, 2
0082DAA6  72 C2                           jb 0x14082da6a
0082DAA8  48 8B 4B 08                     mov rcx, qword ptr [rbx + 8]
0082DAAC  48 85 C9                        test rcx, rcx
0082DAAF  74 0B                           je 0x14082dabc
0082DAB1  33 D2                           xor edx, edx
0082DAB3  E8 B8 4D 35 00                  call 0x140b82870
0082DAB8  8B 44 24 40                     mov eax, dword ptr [rsp + 0x40]
0082DABC  8B D0                           mov edx, eax
0082DABE  B9 00 01 00 00                  mov ecx, 0x100
0082DAC3  41 B8 50 4E 50 52               mov r8d, 0x52504e50
0082DAC9  E8 22 46 35 00                  call 0x140b820f0
0082DACE  45 33 C9                        xor r9d, r9d
0082DAD1  48 89 43 08                     mov qword ptr [rbx + 8], rax
0082DAD5  48 85 C0                        test rax, rax
0082DAD8  74 0C                           je 0x14082dae6
0082DADA  8B 44 24 40                     mov eax, dword ptr [rsp + 0x40]
0082DADE  89 43 10                        mov dword ptr [rbx + 0x10], eax
0082DAE1  E9 F3 FE FF FF                  jmp 0x14082d9d9
0082DAE6  44 89 4B 10                     mov dword ptr [rbx + 0x10], r9d
0082DAEA  BE 17 00 00 C0                  mov esi, 0xc0000017
0082DAEF  E9 7B FF FF FF                  jmp 0x14082da6f
0082DAF4  85 D2                           test edx, edx
0082DAF6  0F 88 73 FF FF FF               js 0x14082da6f
0082DAFC  83 7C 24 44 07                  cmp dword ptr [rsp + 0x44], 7
0082DB01  0F 85 68 FF FF FF               jne 0x14082da6f
0082DB07  8B 43 10                        mov eax, dword ptr [rbx + 0x10]
0082DB0A  83 F8 02                        cmp eax, 2
0082DB0D  76 0F                           jbe 0x14082db1e
0082DB0F  8B C8                           mov ecx, eax
0082DB11  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
0082DB15  48 D1 E9                        shr rcx, 1
0082DB18  66 44 89 4C 48 FE               mov word ptr [rax + rcx*2 - 2], r9w
0082DB1E  8B 43 10                        mov eax, dword ptr [rbx + 0x10]
0082DB21  83 F8 04                        cmp eax, 4
0082DB24  76 0F                           jbe 0x14082db35
0082DB26  8B C8                           mov ecx, eax
0082DB28  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
0082DB2C  48 D1 E9                        shr rcx, 1
0082DB2F  66 44 89 4C 48 FC               mov word ptr [rax + rcx*2 - 4], r9w
0082DB35  48 8B 7B 08                     mov rdi, qword ptr [rbx + 8]
0082DB39  66 44 39 0F                     cmp word ptr [rdi], r9w
0082DB3D  0F 84 2C FF FF FF               je 0x14082da6f
0082DB43  48 8B D7                        mov rdx, rdi
0082DB46  48 8D 4C 24 78                  lea rcx, [rsp + 0x78]
0082DB4B  E8 10 5E C3 FF                  call 0x140463960
0082DB50  45 33 C9                        xor r9d, r9d
0082DB53  85 C0                           test eax, eax
0082DB55  78 18                           js 0x14082db6f
0082DB57  41 B0 01                        mov r8b, 1
0082DB5A  48 8D 54 24 78                  lea rdx, [rsp + 0x78]
0082DB5F  48 8D 4D 88                     lea rcx, [rbp - 0x78]
0082DB63  E8 B8 4E 10 00                  call 0x140932a20
0082DB68  45 33 C9                        xor r9d, r9d
0082DB6B  84 C0                           test al, al
0082DB6D  75 18                           jne 0x14082db87
0082DB6F  48 83 C8 FF                     or rax, 0xffffffffffffffff
0082DB73  48 FF C0                        inc rax
0082DB76  66 44 39 0C 47                  cmp word ptr [rdi + rax*2], r9w
0082DB7B  75 F6                           jne 0x14082db73
0082DB7D  48 8D 3C 47                     lea rdi, [rdi + rax*2]
0082DB81  48 83 C7 02                     add rdi, 2
0082DB85  EB B2                           jmp 0x14082db39
0082DB87  4C 8B 74 24 50                  mov r14, qword ptr [rsp + 0x50]
0082DB8C  4C 8B 7C 24 58                  mov r15, qword ptr [rsp + 0x58]
0082DB91  44 8B 44 24 48                  mov r8d, dword ptr [rsp + 0x48]
0082DB96  40 B7 01                        mov dil, 1
0082DB99  48 8B 43 18                     mov rax, qword ptr [rbx + 0x18]
0082DB9D  48 85 C0                        test rax, rax
0082DBA0  74 12                           je 0x14082dbb4
0082DBA2  4C 8B 4B 20                     mov r9, qword ptr [rbx + 0x20]
0082DBA6  49 8B D7                        mov rdx, r15
0082DBA9  49 8B CE                        mov rcx, r14
0082DBAC  E8 1F CF E8 FF                  call 0x1406baad0
0082DBB1  40 8A F8                        mov dil, al
0082DBB4  40 8A C7                        mov al, dil
0082DBB7  48 8B 4D F0                     mov rcx, qword ptr [rbp - 0x10]
0082DBBB  48 33 CC                        xor rcx, rsp
0082DBBE  E8 7D EA E7 FF                  call 0x1406ac640
0082DBC3  48 81 C4 08 01 00 00            add rsp, 0x108
0082DBCA  41 5F                           pop r15
0082DBCC  41 5E                           pop r14
0082DBCE  41 5D                           pop r13
0082DBD0  41 5C                           pop r12
0082DBD2  5F                              pop rdi
0082DBD3  5E                              pop rsi
0082DBD4  5B                              pop rbx
0082DBD5  5D                              pop rbp
0082DBD6  C3                              ret
0082DBD7  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmServiceFilterCallback(__int64 a1, __int64 a2, int a3, __int64 a4)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned int v_stack_m100;
    unsigned int v_stack_m104;
    unsigned int v_stack_m108;
    unsigned int v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m58;
    unsigned __int16 v_stack_m5C;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned int v_stack_mDC;
    unsigned int v_stack_mE0;
    unsigned int v_stack_mE4;
    unsigned int v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;

    v_rsp = (v_rsp) - (264);
    result = (*(unsigned __int64 *)(v_rip + 6147968)) ^ (v_rsp);
    v_stack_m58 = result;
    v_stack_m100 = a3;
    a4 = 0;
    v_stack_mF0 = a2;
    v_stack_mF8 = a1;
    v_stack_m108 = 0;
    v_stack_m104 = 0;
    v_stack_mC0 = v_xmm0;
    v_stack_mD0 = v_xmm1;
    if (0 == 0) goto loc_0082DBB4;
    if (*(unsigned __int64 *)(a4) == 0) goto loc_0082DB96;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a4))) == 0) goto loc_0082DB96;
    result = RtlInitUnicodeStringEx(v_stack_mC0, *(unsigned __int64 *)(a4), a3, a4);
    a4 = 0;
    if (sign_flag) goto loc_0082DBB4;
loc_0082D831:
    a3 = 0;
    v_stack_m110 = 0;
    v_stack_m108 = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16)));
    v_stack_m118 = v_stack_m108;
    v_stack_m120 = *(unsigned __int64 *)(a4 + 8);
    v_stack_m128 = v_stack_m104;
    result = CmGetDeviceRegProp(a1, a2, a3, 5);
    a4 = 0;
    if ((unsigned int)((unsigned int)((unsigned int)(result))) != 0) goto loc_0082D885;
    if (((unsigned int)((unsigned int)(v_stack_m108))) < 2) goto loc_0082D8D0;
loc_0082D885:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != 0xC0000023ULL) goto loc_0082D8DF;
    if (((unsigned int)((unsigned int)(v_stack_m108))) < 2) goto loc_0082D8D0;
    result = (unsigned int)(v_stack_m108);
    if (*(unsigned __int64 *)(a4 + 8) != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(a4 + 8), a2, a3, a4);
        result = v_stack_m108;
    }
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(result)), (unsigned int)(0x52504E50ULL), a4);
    a4 = 0;
    *(unsigned __int64 *)(a4 + 8) = result;
    if (result == 0) goto loc_0082D8D4;
    *(unsigned int *)(a4 + 16) = (unsigned int)((unsigned int)(v_stack_m108));
    goto loc_0082D831;
loc_0082D8D0:
    goto loc_0082D926;
loc_0082D8D4:
    *(unsigned int *)(a4 + 16) = 0;
    goto loc_0082D926;
loc_0082D8DF:
    if ((unsigned int)((unsigned int)((unsigned int)(result))) != 0) goto loc_0082D926;
    a1 = ((unsigned int)(*(unsigned int *)(a4 + 16))) >> (1);
    *(unsigned __int16 *)(*(unsigned __int64 *)(a4 + 8) + a1 * 2 - 2) = 0;
    result = RtlInitUnicodeStringEx(v_stack_mD0, *(unsigned __int64 *)(a4 + 8), (unsigned int)(0x52504E50ULL), a4);
    a4 = 0;
    if (sign_flag) goto loc_0082D926;
    result = RtlEqualUnicodeString(v_stack_mC0, v_stack_mD0, 1, a4);
    a4 = 0;
    if ((unsigned __int8)(result) != 0) goto loc_0082DB91;
loc_0082D926:
    v_stack_mE8 = 1;
    v_stack_mE4 = 2;
loc_0082D93E:
    v_stack_mD8 = v_stack_mE8;
    if (0 >= 2) goto loc_0082DBB4;
    v_stack_mE0 = 18;
    v_stack_mDC = 19;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mE8)))) != 2) goto loc_0082D9D1;
    v_stack_m110 = 0;
    v_stack_m118 = v_stack_m108;
    v_stack_m108 = 78;
    v_stack_m120 = v_stack_mA8;
    a3 = 0;
    v_stack_m128 = v_stack_m104;
    result = CmGetDeviceRegProp(a1, 0, a3, (unsigned int)(*(unsigned int *)(v_stack_mE8)) + 7);
    a4 = 0;
    if (sign_flag) goto loc_0082DBB4;
    if (v_stack_m104 != 1) goto loc_0082DBB4;
    if (v_stack_m108 < ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mE8))))) goto loc_0082DBB4;
    v_stack_m5C = 0;
loc_0082D9D1:
loc_0082D9D9:
    v_stack_m108 = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16)));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mE8)))) != 1) goto loc_0082DA1F;
    a3 = 0;
    v_stack_m110 = 0;
    v_stack_m118 = v_stack_m108;
    v_stack_m120 = *(unsigned __int64 *)(a4 + 8);
    v_stack_m128 = v_stack_m104;
    result = CmGetDeviceRegProp(v_stack_mF8, v_stack_mF0, a3, (unsigned int)(*(unsigned int *)(v_stack_mE0)));
    goto loc_0082DA56;
loc_0082DA1F:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mE8)))) != 2) goto loc_0082DA5F;
    v_stack_m118 = v_stack_m108;
    a3 = 0;
    v_stack_m120 = *(unsigned __int64 *)(a4 + 8);
    v_stack_m128 = v_stack_m104;
    result = CmGetInstallerClassRegProp(v_stack_mF8, v_stack_mA8, a3, (unsigned int)(*(unsigned int *)(v_stack_mE0)));
loc_0082DA56:
    a4 = 0;
loc_0082DA5F:
    if ((unsigned int)((unsigned int)((unsigned int)(result))) != 0) goto loc_0082DA9B;
    if (((unsigned int)((unsigned int)(v_stack_m108))) >= 2) goto loc_0082DA9B;
loc_0082DA6A:
loc_0082DA6F:
    v_r15 = (unsigned int)((0) + 1);
    v_r14 = (v_stack_mE0) + (4);
    if (((unsigned int)(v_r15)) < 2) goto loc_0082D9D9;
    v_r13 = (unsigned int)((0) + 1);
    result = (v_stack_mD8) + (4);
    goto loc_0082D93E;
loc_0082DA9B:
    if (((unsigned int)((unsigned int)(0xC000000DULL))) != 0xC0000023ULL) goto loc_0082DAF4;
    if (((unsigned int)(result)) < 2) goto loc_0082DA6A;
    if (*(unsigned __int64 *)(a4 + 8) != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(a4 + 8), a2, a3, a4);
        result = v_stack_m108;
    }
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(result)), (unsigned int)(0x52504E50ULL), a4);
    a4 = 0;
    *(unsigned __int64 *)(a4 + 8) = result;
    if (result == 0) goto loc_0082DAE6;
    *(unsigned int *)(a4 + 16) = (unsigned int)((unsigned int)(v_stack_m108));
    goto loc_0082D9D9;
loc_0082DAE6:
    *(unsigned int *)(a4 + 16) = 0;
    goto loc_0082DA6F;
loc_0082DAF4:
    if (sign_flag) goto loc_0082DA6F;
    if (v_stack_m104 != 7) goto loc_0082DA6F;
    result = (unsigned int)(*(unsigned int *)(a4 + 16));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16)))) >= = 2) {
        a1 = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16)));
        result = *(unsigned __int64 *)(a4 + 8);
        a1 = (a1) >> (1);
        *(unsigned __int16 *)(result + a1 * 2 - 2) = 0;
    }
    result = (unsigned int)(*(unsigned int *)(a4 + 16));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16)))) >= = 4) {
        a1 = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16)));
        result = *(unsigned __int64 *)(a4 + 8);
        a1 = (a1) >> (1);
        *(unsigned __int16 *)(result + a1 * 2 - 4) = 0;
    }
loc_0082DB39:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a4 + 8))) == 0) goto loc_0082DA6F;
    result = RtlInitUnicodeStringEx(v_stack_mD0, *(unsigned __int64 *)(a4 + 8), (unsigned int)(0x52504E50ULL), a4);
    a4 = 0;
    if (sign_flag) goto loc_0082DB6F;
    result = RtlEqualUnicodeString(v_stack_mC0, v_stack_mD0, 1, a4);
    a4 = 0;
    if ((unsigned __int8)(result) != 0) goto loc_0082DB87;
loc_0082DB6F:
    result = (result) | (-1);
loc_0082DB73:
    result = (result) + 1;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a4 + 8) + result * 2)) != 0) goto loc_0082DB73;
    v_rdi = (*(unsigned __int64 *)(a4 + 8) + result * 2) + (2);
    goto loc_0082DB39;
loc_0082DB87:
loc_0082DB91:
loc_0082DB96:
    result = *(unsigned __int64 *)(a4 + 24);
    v_rdi = 1;
    if (*(unsigned __int64 *)(a4 + 24) != 0) {
        a4 = *(unsigned __int64 *)(a4 + 32);
        a2 = v_stack_mF0;
        a1 = v_stack_mF8;
        result = guard_dispatch_icall(a1, a2, (unsigned int)(v_stack_m100), a4);
        v_rdi = (unsigned __int8)(result);
    }
    a1 = (v_stack_m58) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, (unsigned int)(v_stack_m100), a4);
    v_rsp = (v_rsp) + (264);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CmServiceFilterCallback(int64_t Arg1, int64_t Arg2, int32_t Arg3, int64_t Arg4)
{
    int64_t result;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rdi;
    int64_t local_rsp;
    uint32_t v_stack_m100;
    uint32_t v_stack_m104;
    uint32_t v_stack_m108;
    uint32_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint64_t v_stack_m48;
    uint64_t v_stack_m58;
    uint16_t v_stack_m5C;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint32_t v_stack_mDC;
    uint32_t v_stack_mE0;
    uint32_t v_stack_mE4;
    uint32_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;

    local_rsp = (local_rsp) - (264);
    result = (*(uint64_t *)(v_rip + 0x5DCF80)) ^ (local_rsp);
    v_stack_m58 = result;
    v_stack_m100 = Arg3;
    Arg4 = 0;
    v_stack_mF0 = Arg2;
    v_stack_mF8 = Arg1;
    v_stack_m108 = 0;
    v_stack_m104 = 0;
    v_stack_mC0 = v_xmm0;
    v_stack_mD0 = v_xmm1;
    if (0 == 0) goto loc_0082DBB4;
    if (*(uint64_t *)(Arg4) == 0) goto loc_0082DB96;
    if ((*(uint16_t *)(*(uint64_t *)(Arg4))) == 0) goto loc_0082DB96;
    result = RtlInitUnicodeStringEx(v_stack_mC0, *(uint64_t *)(Arg4), Arg3, Arg4);
    Arg4 = 0;
    if (sign_flag) goto loc_0082DBB4;
loc_0082D831:
    Arg3 = 0;
    v_stack_m110 = 0;
    v_stack_m108 = (uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x10)));
    v_stack_m118 = v_stack_m108;
    v_stack_m120 = *(uint64_t *)(Arg4 + 0x8);
    v_stack_m128 = v_stack_m104;
    result = CmGetDeviceRegProp(Arg1, Arg2, Arg3, 5);
    Arg4 = 0;
    if ((uint32_t)((uint32_t)((uint32_t)(result))) != 0) goto loc_0082D885;
    if (((uint32_t)((uint32_t)(v_stack_m108))) < 2) goto loc_0082D8D0;
loc_0082D885:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != 0xC0000023ULL) goto loc_0082D8DF;
    if (((uint32_t)((uint32_t)(v_stack_m108))) < 2) goto loc_0082D8D0;
    result = (uint32_t)(v_stack_m108);
    if (*(uint64_t *)(Arg4 + 0x8) != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(*(uint64_t *)(Arg4 + 0x8), Arg2, Arg3, Arg4);
        result = v_stack_m108;
    }
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(result)), (uint32_t)(0x52504E50ULL), Arg4);
    Arg4 = 0;
    *(uint64_t *)(Arg4 + 0x8) = result;
    if (result == 0) goto loc_0082D8D4;
    *(uint32_t *)(Arg4 + 0x10) = (uint32_t)((uint32_t)(v_stack_m108));
    goto loc_0082D831;
loc_0082D8D0:
    goto loc_0082D926;
loc_0082D8D4:
    *(uint32_t *)(Arg4 + 0x10) = 0;
    goto loc_0082D926;
loc_0082D8DF:
    if ((uint32_t)((uint32_t)((uint32_t)(result))) != 0) goto loc_0082D926;
    Arg1 = ((uint32_t)(*(uint32_t *)(Arg4 + 0x10))) >> (1);
    *(uint16_t *)(*(uint64_t *)(Arg4 + 0x8) + Arg1 * 2 - 0x2) = 0;
    result = RtlInitUnicodeStringEx(v_stack_mD0, *(uint64_t *)(Arg4 + 0x8), (uint32_t)(0x52504E50ULL), Arg4);
    Arg4 = 0;
    if (sign_flag) goto loc_0082D926;
    result = RtlEqualUnicodeString(v_stack_mC0, v_stack_mD0, 1, Arg4);
    Arg4 = 0;
    if ((uint8_t)(result) != 0) goto loc_0082DB91;
loc_0082D926:
    v_stack_mE8 = 1;
    v_stack_mE4 = 2;
loc_0082D93E:
    v_stack_mD8 = v_stack_mE8;
    if (0 >= 2) goto loc_0082DBB4;
    v_stack_mE0 = 18;
    v_stack_mDC = 19;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mE8)))) != 2) goto loc_0082D9D1;
    v_stack_m110 = 0;
    v_stack_m118 = v_stack_m108;
    v_stack_m108 = 78;
    v_stack_m120 = v_stack_mA8;
    Arg3 = 0;
    v_stack_m128 = v_stack_m104;
    result = CmGetDeviceRegProp(Arg1, 0, Arg3, (uint32_t)(*(uint32_t *)(v_stack_mE8)) + 7);
    Arg4 = 0;
    if (sign_flag) goto loc_0082DBB4;
    if (v_stack_m104 != 1) goto loc_0082DBB4;
    if (v_stack_m108 < ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mE8))))) goto loc_0082DBB4;
    v_stack_m5C = 0;
loc_0082D9D1:
loc_0082D9D9:
    v_stack_m108 = (uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x10)));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mE8)))) != 1) goto loc_0082DA1F;
    Arg3 = 0;
    v_stack_m110 = 0;
    v_stack_m118 = v_stack_m108;
    v_stack_m120 = *(uint64_t *)(Arg4 + 0x8);
    v_stack_m128 = v_stack_m104;
    result = CmGetDeviceRegProp(v_stack_mF8, v_stack_mF0, Arg3, (uint32_t)(*(uint32_t *)(v_stack_mE0)));
    goto loc_0082DA56;
loc_0082DA1F:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mE8)))) != 2) goto loc_0082DA5F;
    v_stack_m118 = v_stack_m108;
    Arg3 = 0;
    v_stack_m120 = *(uint64_t *)(Arg4 + 0x8);
    v_stack_m128 = v_stack_m104;
    result = CmGetInstallerClassRegProp(v_stack_mF8, v_stack_mA8, Arg3, (uint32_t)(*(uint32_t *)(v_stack_mE0)));
loc_0082DA56:
    Arg4 = 0;
loc_0082DA5F:
    if ((uint32_t)((uint32_t)((uint32_t)(result))) != 0) goto loc_0082DA9B;
    if (((uint32_t)((uint32_t)(v_stack_m108))) >= 2) goto loc_0082DA9B;
loc_0082DA6A:
loc_0082DA6F:
    local_r15 = (uint32_t)((0) + 1);
    local_r14 = (v_stack_mE0) + (4);
    if (((uint32_t)(local_r15)) < 2) goto loc_0082D9D9;
    local_r13 = (uint32_t)((0) + 1);
    result = (v_stack_mD8) + (4);
    goto loc_0082D93E;
loc_0082DA9B:
    if (((uint32_t)((uint32_t)(0xC000000DULL))) != 0xC0000023ULL) goto loc_0082DAF4;
    if (((uint32_t)(result)) < 2) goto loc_0082DA6A;
    if (*(uint64_t *)(Arg4 + 0x8) != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(*(uint64_t *)(Arg4 + 0x8), Arg2, Arg3, Arg4);
        result = v_stack_m108;
    }
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(result)), (uint32_t)(0x52504E50ULL), Arg4);
    Arg4 = 0;
    *(uint64_t *)(Arg4 + 0x8) = result;
    if (result == 0) goto loc_0082DAE6;
    *(uint32_t *)(Arg4 + 0x10) = (uint32_t)((uint32_t)(v_stack_m108));
    goto loc_0082D9D9;
loc_0082DAE6:
    *(uint32_t *)(Arg4 + 0x10) = 0;
    goto loc_0082DA6F;
loc_0082DAF4:
    if (sign_flag) goto loc_0082DA6F;
    if (v_stack_m104 != 7) goto loc_0082DA6F;
    result = (uint32_t)(*(uint32_t *)(Arg4 + 0x10));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x10)))) >= = 2) {
        Arg1 = (uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x10)));
        result = *(uint64_t *)(Arg4 + 0x8);
        Arg1 = (Arg1) >> (1);
        *(uint16_t *)(result + Arg1 * 2 - 0x2) = 0;
    }
    result = (uint32_t)(*(uint32_t *)(Arg4 + 0x10));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x10)))) >= = 4) {
        Arg1 = (uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x10)));
        result = *(uint64_t *)(Arg4 + 0x8);
        Arg1 = (Arg1) >> (1);
        *(uint16_t *)(result + Arg1 * 2 - 0x4) = 0;
    }
loc_0082DB39:
    if ((*(uint16_t *)(*(uint64_t *)(Arg4 + 0x8))) == 0) goto loc_0082DA6F;
    result = RtlInitUnicodeStringEx(v_stack_mD0, *(uint64_t *)(Arg4 + 0x8), (uint32_t)(0x52504E50ULL), Arg4);
    Arg4 = 0;
    if (sign_flag) goto loc_0082DB6F;
    result = RtlEqualUnicodeString(v_stack_mC0, v_stack_mD0, 1, Arg4);
    Arg4 = 0;
    if ((uint8_t)(result) != 0) goto loc_0082DB87;
loc_0082DB6F:
    result = (result) | (-1);
loc_0082DB73:
    result = (result) + 1;
    if ((*(uint16_t *)(*(uint64_t *)(Arg4 + 0x8) + result * 2)) != 0) goto loc_0082DB73;
    local_rdi = (*(uint64_t *)(Arg4 + 0x8) + result * 2) + (2);
    goto loc_0082DB39;
loc_0082DB87:
loc_0082DB91:
loc_0082DB96:
    result = *(uint64_t *)(Arg4 + 0x18);
    local_rdi = 1;
    if (*(uint64_t *)(Arg4 + 0x18) != 0) {
        Arg4 = *(uint64_t *)(Arg4 + 0x20);
        Arg2 = v_stack_mF0;
        Arg1 = v_stack_mF8;
        result = guard_dispatch_icall(Arg1, Arg2, (uint32_t)(v_stack_m100), Arg4);
        local_rdi = (uint8_t)(result);
    }
    Arg1 = (v_stack_m58) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, (uint32_t)(v_stack_m100), Arg4);
    local_rsp = (local_rsp) + (264);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0082D7A0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
