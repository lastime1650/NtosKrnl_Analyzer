# PiDrvDbResolveFilePathKeyValues

- RVA: `0x00742C00`–`0x00743264` (길이 `1,636` bytes)
- VA: `0x0000000140742C00`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C92D8`
- 디코드: `443`개 명령, `1,636/1,636` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **34**; 고유 호출 대상: **15**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x00742C7E` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00742C89` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00742C94` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00742CB9` → [PnpCtxRegOpenKey](../8E/PnpCtxRegOpenKey_function_008EF7B8.md) (function, `0x008EF7B8`)
- `0x00742CCF` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x00742CD8` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x00742CE1` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x00742CEF` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x00742D16` → [PiDrvDbQuerySystemPathWin32](PiDrvDbQuerySystemPathWin32_function_007421F4.md) (function, `0x007421F4`)
- `0x00742D2B` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00742D48` → [RtlEqualUnicodeString](../93/RtlEqualUnicodeString_function_00932A20.md) (function, `0x00932A20`)
- `0x00742D67` → [RtlEqualUnicodeString](../93/RtlEqualUnicodeString_function_00932A20.md) (function, `0x00932A20`)
- `0x00742D9F` → [RtlEqualUnicodeString](../93/RtlEqualUnicodeString_function_00932A20.md) (function, `0x00932A20`)
- `0x00742DCD` → [PnpCtxRegQueryInfoKey](../99/PnpCtxRegQueryInfoKey_function_009945FC.md) (function, `0x009945FC`)
- `0x00742E00` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00742E2E` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00742E84` → [PnpCtxRegEnumValue](../99/PnpCtxRegEnumValue_function_0099364C.md) (function, `0x0099364C`)
- `0x00742EB8` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00742ECB` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00742EF8` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00742F0B` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00742F80` → [PnpCtxRegOpenKey](../8E/PnpCtxRegOpenKey_function_008EF7B8.md) (function, `0x008EF7B8`)
- `0x00742FB7` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (function, `0x00500080`)
- `0x00742FDB` → [IopGetRegistryValue](../99/IopGetRegistryValue_function_009990EC.md) (function, `0x009990EC`)
- `0x0074305D` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00743095` → [PiDrvDbResolveSystemFilePath](PiDrvDbResolveSystemFilePath_function_00743514.md) (function, `0x00743514`)
- `0x007430DE` → [PiDevCfgAppendMultiSz](../73/PiDevCfgAppendMultiSz_function_00731B28.md) (function, `0x00731B28`)
- `0x0074313C` → [PnpCtxRegSetValue](../99/PnpCtxRegSetValue_function_00991B8C.md) (function, `0x00991B8C`)
- `0x0074316C` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x007431A6` → [PiDrvDbResolveSystemFilePath](PiDrvDbResolveSystemFilePath_function_00743514.md) (function, `0x00743514`)
- `0x007431DE` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00743220` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x00743247` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0074325A` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [PiDrvDbResolveKeyFilePaths](PiDrvDbResolveKeyFilePaths_function_0074326C.md) at `0x00743378`
- [PiDrvDbResolveNodeFilePaths](PiDrvDbResolveNodeFilePaths_function_007433A4.md) at `0x007434DA`

### Static image references
- `0x00742CA5` → RVA `0x00AFF170` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00742D3E` → RVA `0x00B4AD48` (`PiDrvDbSystemRootNt`; read)
- `0x00742D5C` → RVA `0x00B4B0F0` (`PiDrvDbSystemRootWin32`; read)
- `0x00742FAD` → RVA `0x00AFCA30` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00742FC0` → RVA `0x00AFCAD0` (` ?? ::NNGAKEGL::`string'`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **18**
  - `0x00742C7E` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00742C89` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00742C94` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00742CEF` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x00742D2B` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00742E00` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00742E2E` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00742EB8` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00742ECB` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00742EF8` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00742F0B` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00742FB7` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (`PAGE` → `.text`)
  - `0x0074305D` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x0074316C` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x007431DE` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00743220` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x00743247` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0074325A` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00742C00  48 8B C4                        mov rax, rsp
00742C03  4C 89 48 20                     mov qword ptr [rax + 0x20], r9
00742C07  4C 89 40 18                     mov qword ptr [rax + 0x18], r8
00742C0B  89 50 10                        mov dword ptr [rax + 0x10], edx
00742C0E  48 89 48 08                     mov qword ptr [rax + 8], rcx
00742C12  55                              push rbp
00742C13  53                              push rbx
00742C14  56                              push rsi
00742C15  57                              push rdi
00742C16  41 54                           push r12
00742C18  41 55                           push r13
00742C1A  41 56                           push r14
00742C1C  41 57                           push r15
00742C1E  48 8D 68 A1                     lea rbp, [rax - 0x5f]
00742C22  48 81 EC D8 00 00 00            sub rsp, 0xd8
00742C29  33 C0                           xor eax, eax
00742C2B  0F 57 C0                        xorps xmm0, xmm0
00742C2E  8B F2                           mov esi, edx
00742C30  48 89 45 D7                     mov qword ptr [rbp - 0x29], rax
00742C34  48 8B D9                        mov rbx, rcx
00742C37  89 45 87                        mov dword ptr [rbp - 0x79], eax
00742C3A  0F 57 C9                        xorps xmm1, xmm1
00742C3D  89 45 97                        mov dword ptr [rbp - 0x69], eax
00742C40  33 D2                           xor edx, edx
00742C42  89 45 8F                        mov dword ptr [rbp - 0x71], eax
00742C45  48 8D 4D A7                     lea rcx, [rbp - 0x59]
00742C49  48 89 45 E7                     mov qword ptr [rbp - 0x19], rax
00742C4D  0F 11 45 A7                     movups xmmword ptr [rbp - 0x59], xmm0
00742C51  44 8B E8                        mov r13d, eax
00742C54  89 45 8B                        mov dword ptr [rbp - 0x75], eax
00742C57  44 8B F8                        mov r15d, eax
00742C5A  48 89 45 DF                     mov qword ptr [rbp - 0x21], rax
00742C5E  44 8B E0                        mov r12d, eax
00742C61  48 89 45 BF                     mov qword ptr [rbp - 0x41], rax
00742C65  44 8B F0                        mov r14d, eax
00742C68  48 89 45 0F                     mov qword ptr [rbp + 0xf], rax
00742C6C  0F 11 45 EF                     movups xmmword ptr [rbp - 0x11], xmm0
00742C70  89 45 B7                        mov dword ptr [rbp - 0x49], eax
00742C73  49 8B F8                        mov rdi, r8
00742C76  0F 11 4D C7                     movups xmmword ptr [rbp - 0x39], xmm1
00742C7A  0F 11 45 FF                     movups xmmword ptr [rbp - 1], xmm0
00742C7E  E8 FD 7A CE FF                  call 0x14042a780
00742C83  33 D2                           xor edx, edx
00742C85  48 8D 4D C7                     lea rcx, [rbp - 0x39]
00742C89  E8 F2 7A CE FF                  call 0x14042a780
00742C8E  33 D2                           xor edx, edx
00742C90  48 8D 4D FF                     lea rcx, [rbp - 1]
00742C94  E8 E7 7A CE FF                  call 0x14042a780
00742C99  48 8D 45 D7                     lea rax, [rbp - 0x29]
00742C9D  45 33 C9                        xor r9d, r9d
00742CA0  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00742CA5  4C 8D 05 C4 C4 3B 00            lea r8, [rip + 0x3bc4c4]
00742CAC  48 8B D3                        mov rdx, rbx
00742CAF  C7 44 24 20 19 00 02 00         mov dword ptr [rsp + 0x20], 0x20019
00742CB7  33 C9                           xor ecx, ecx
00742CB9  E8 FA CA 1A 00                  call 0x1408ef7b8
00742CBE  8B D8                           mov ebx, eax
00742CC0  3D 34 00 00 C0                  cmp eax, 0xc0000034
00742CC5  75 44                           jne 0x140742d0b
00742CC7  33 FF                           xor edi, edi
00742CC9  8B DF                           mov ebx, edi
00742CCB  48 8D 4D A7                     lea rcx, [rbp - 0x59]
00742CCF  E8 2C DB 27 00                  call 0x1409c0800
00742CD4  48 8D 4D C7                     lea rcx, [rbp - 0x39]
00742CD8  E8 23 DB 27 00                  call 0x1409c0800
00742CDD  48 8D 4D FF                     lea rcx, [rbp - 1]
00742CE1  E8 1A DB 27 00                  call 0x1409c0800
00742CE6  48 8B 4D D7                     mov rcx, qword ptr [rbp - 0x29]
00742CEA  48 85 C9                        test rcx, rcx
00742CED  74 05                           je 0x140742cf4
00742CEF  E8 BC A5 F6 FF                  call 0x1406ad2b0
00742CF4  8B C3                           mov eax, ebx
00742CF6  48 81 C4 D8 00 00 00            add rsp, 0xd8
00742CFD  41 5F                           pop r15
00742CFF  41 5E                           pop r14
00742D01  41 5D                           pop r13
00742D03  41 5C                           pop r12
00742D05  5F                              pop rdi
00742D06  5E                              pop rsi
00742D07  5B                              pop rbx
00742D08  5D                              pop rbp
00742D09  C3                              ret
00742D0A  CC                              int3
00742D0B  85 C0                           test eax, eax
00742D0D  78 BC                           js 0x140742ccb
00742D0F  48 8D 55 A7                     lea rdx, [rbp - 0x59]
00742D13  48 8B CF                        mov rcx, rdi
00742D16  E8 D9 F4 FF FF                  call 0x1407421f4
00742D1B  8B D8                           mov ebx, eax
00742D1D  33 C0                           xor eax, eax
00742D1F  85 DB                           test ebx, ebx
00742D21  79 0D                           jns 0x140742d30
00742D23  33 D2                           xor edx, edx
00742D25  48 8D 4D A7                     lea rcx, [rbp - 0x59]
00742D29  8B D8                           mov ebx, eax
00742D2B  E8 50 7A CE FF                  call 0x14042a780
00742D30  40 F6 C6 02                     test sil, 2
00742D34  74 3C                           je 0x140742d72
00742D36  48 85 FF                        test rdi, rdi
00742D39  74 18                           je 0x140742d53
00742D3B  41 B0 01                        mov r8b, 1
00742D3E  48 8D 15 03 80 40 00            lea rdx, [rip + 0x408003]
00742D45  48 8B CF                        mov rcx, rdi
00742D48  E8 D3 FC 1E 00                  call 0x140932a20
00742D4D  33 FF                           xor edi, edi
00742D4F  84 C0                           test al, al
00742D51  74 59                           je 0x140742dac
00742D53  48 39 7D AF                     cmp qword ptr [rbp - 0x51], rdi
00742D57  74 1B                           je 0x140742d74
00742D59  41 B0 01                        mov r8b, 1
00742D5C  48 8D 15 8D 83 40 00            lea rdx, [rip + 0x40838d]
00742D63  48 8D 4D A7                     lea rcx, [rbp - 0x59]
00742D67  E8 B4 FC 1E 00                  call 0x140932a20
00742D6C  84 C0                           test al, al
00742D6E  74 3C                           je 0x140742dac
00742D70  EB 02                           jmp 0x140742d74
00742D72  33 FF                           xor edi, edi
00742D74  40 F6 C6 01                     test sil, 1
00742D78  0F 84 4B FF FF FF               je 0x140742cc9
00742D7E  48 8B 45 7F                     mov rax, qword ptr [rbp + 0x7f]
00742D82  48 85 C0                        test rax, rax
00742D85  0F 84 3E FF FF FF               je 0x140742cc9
00742D8B  48 39 7D AF                     cmp qword ptr [rbp - 0x51], rdi
00742D8F  0F 84 34 FF FF FF               je 0x140742cc9
00742D95  41 B0 01                        mov r8b, 1
00742D98  48 8D 55 A7                     lea rdx, [rbp - 0x59]
00742D9C  48 8B C8                        mov rcx, rax
00742D9F  E8 7C FC 1E 00                  call 0x140932a20
00742DA4  84 C0                           test al, al
00742DA6  0F 85 1D FF FF FF               jne 0x140742cc9
00742DAC  48 8B 55 D7                     mov rdx, qword ptr [rbp - 0x29]
00742DB0  48 8D 45 97                     lea rax, [rbp - 0x69]
00742DB4  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00742DB9  45 33 C9                        xor r9d, r9d
00742DBC  48 8D 45 87                     lea rax, [rbp - 0x79]
00742DC0  45 33 C0                        xor r8d, r8d
00742DC3  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00742DC8  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
00742DCD  E8 2A 18 25 00                  call 0x1409945fc
00742DD2  85 C0                           test eax, eax
00742DD4  78 73                           js 0x140742e49
00742DD6  8B 45 87                        mov eax, dword ptr [rbp - 0x79]
00742DD9  44 8B 65 97                     mov r12d, dword ptr [rbp - 0x69]
00742DDD  44 89 65 8B                     mov dword ptr [rbp - 0x75], r12d
00742DE1  44 8D 2C 45 02 00 00 00         lea r13d, [rax*2 + 2]
00742DE9  44 89 6D 8F                     mov dword ptr [rbp - 0x71], r13d
00742DED  45 85 ED                        test r13d, r13d
00742DF0  74 29                           je 0x140742e1b
00742DF2  41 8B D5                        mov edx, r13d
00742DF5  B9 00 01 00 00                  mov ecx, 0x100
00742DFA  41 B8 50 70 64 62               mov r8d, 0x62647050
00742E00  E8 EB F2 43 00                  call 0x140b820f0
00742E05  48 89 45 E7                     mov qword ptr [rbp - 0x19], rax
00742E09  4C 8B F8                        mov r15, rax
00742E0C  48 85 C0                        test rax, rax
00742E0F  75 0A                           jne 0x140742e1b
00742E11  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00742E16  E9 B0 FE FF FF                  jmp 0x140742ccb
00742E1B  45 85 E4                        test r12d, r12d
00742E1E  74 29                           je 0x140742e49
00742E20  49 8B D4                        mov rdx, r12
00742E23  B9 00 01 00 00                  mov ecx, 0x100
00742E28  41 B8 50 70 64 62               mov r8d, 0x62647050
00742E2E  E8 BD F2 43 00                  call 0x140b820f0
00742E33  48 89 45 DF                     mov qword ptr [rbp - 0x21], rax
00742E37  4C 8B F0                        mov r14, rax
00742E3A  48 85 C0                        test rax, rax
00742E3D  75 0A                           jne 0x140742e49
00742E3F  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00742E44  E9 F4 03 00 00                  jmp 0x14074323d
00742E49  8B F7                           mov esi, edi
00742E4B  48 8B 55 D7                     mov rdx, qword ptr [rbp - 0x29]
00742E4F  48 8D 45 87                     lea rax, [rbp - 0x79]
00742E53  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00742E58  41 8B FD                        mov edi, r13d
00742E5B  48 8D 45 B7                     lea rax, [rbp - 0x49]
00742E5F  4C 89 74 24 30                  mov qword ptr [rsp + 0x30], r14
00742E64  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00742E69  4D 8B CF                        mov r9, r15
00742E6C  48 8D 45 97                     lea rax, [rbp - 0x69]
00742E70  D1 EF                           shr edi, 1
00742E72  44 8B C6                        mov r8d, esi
00742E75  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00742E7A  89 75 9F                        mov dword ptr [rbp - 0x61], esi
00742E7D  89 7D 97                        mov dword ptr [rbp - 0x69], edi
00742E80  44 89 65 87                     mov dword ptr [rbp - 0x79], r12d
00742E84  E8 C3 07 25 00                  call 0x14099364c
00742E89  3D 1A 00 00 80                  cmp eax, 0x8000001a
00742E8E  0F 84 A9 03 00 00               je 0x14074323d
00742E94  3D 23 00 00 C0                  cmp eax, 0xc0000023
00742E99  0F 85 88 00 00 00               jne 0x140742f27
00742E9F  8B 45 97                        mov eax, dword ptr [rbp - 0x69]
00742EA2  3B C7                           cmp eax, edi
00742EA4  76 3A                           jbe 0x140742ee0
00742EA6  44 8D 2C 00                     lea r13d, [rax + rax]
00742EAA  44 89 6D 8F                     mov dword ptr [rbp - 0x71], r13d
00742EAE  4D 85 FF                        test r15, r15
00742EB1  74 0A                           je 0x140742ebd
00742EB3  33 D2                           xor edx, edx
00742EB5  49 8B CF                        mov rcx, r15
00742EB8  E8 B3 F9 43 00                  call 0x140b82870
00742EBD  41 8B D5                        mov edx, r13d
00742EC0  B9 00 01 00 00                  mov ecx, 0x100
00742EC5  41 B8 50 70 64 62               mov r8d, 0x62647050
00742ECB  E8 20 F2 43 00                  call 0x140b820f0
00742ED0  48 89 45 E7                     mov qword ptr [rbp - 0x19], rax
00742ED4  4C 8B F8                        mov r15, rax
00742ED7  48 85 C0                        test rax, rax
00742EDA  0F 84 54 03 00 00               je 0x140743234
00742EE0  44 39 65 87                     cmp dword ptr [rbp - 0x79], r12d
00742EE4  76 3A                           jbe 0x140742f20
00742EE6  44 8B 65 87                     mov r12d, dword ptr [rbp - 0x79]
00742EEA  44 89 65 8B                     mov dword ptr [rbp - 0x75], r12d
00742EEE  4D 85 F6                        test r14, r14
00742EF1  74 0A                           je 0x140742efd
00742EF3  33 D2                           xor edx, edx
00742EF5  49 8B CE                        mov rcx, r14
00742EF8  E8 73 F9 43 00                  call 0x140b82870
00742EFD  49 8B D4                        mov rdx, r12
00742F00  B9 00 01 00 00                  mov ecx, 0x100
00742F05  41 B8 50 70 64 62               mov r8d, 0x62647050
00742F0B  E8 E0 F1 43 00                  call 0x140b820f0
00742F10  48 89 45 DF                     mov qword ptr [rbp - 0x21], rax
00742F14  4C 8B F0                        mov r14, rax
00742F17  48 85 C0                        test rax, rax
00742F1A  0F 84 1F FF FF FF               je 0x140742e3f
00742F20  FF CE                           dec esi
00742F22  E9 02 03 00 00                  jmp 0x140743229
00742F27  33 FF                           xor edi, edi
00742F29  85 C0                           test eax, eax
00742F2B  0F 88 0A 03 00 00               js 0x14074323b
00742F31  83 7D B7 07                     cmp dword ptr [rbp - 0x49], 7
00742F35  0F 85 EE 02 00 00               jne 0x140743229
00742F3B  83 7D 87 04                     cmp dword ptr [rbp - 0x79], 4
00742F3F  0F 82 E4 02 00 00               jb 0x140743229
00742F45  8B 45 87                        mov eax, dword ptr [rbp - 0x79]
00742F48  48 D1 E8                        shr rax, 1
00742F4B  66 41 39 7C 46 FE               cmp word ptr [r14 + rax*2 - 2], di
00742F51  0F 85 D2 02 00 00               jne 0x140743229
00742F57  66 41 39 7C 46 FC               cmp word ptr [r14 + rax*2 - 4], di
00742F5D  0F 85 C6 02 00 00               jne 0x140743229
00742F63  48 8B 55 67                     mov rdx, qword ptr [rbp + 0x67]
00742F67  48 8D 45 BF                     lea rax, [rbp - 0x41]
00742F6B  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00742F70  45 33 C9                        xor r9d, r9d
00742F73  4D 8B C7                        mov r8, r15
00742F76  C7 44 24 20 1F 00 02 00         mov dword ptr [rsp + 0x20], 0x2001f
00742F7E  33 C9                           xor ecx, ecx
00742F80  E8 33 C8 1A 00                  call 0x1408ef7b8
00742F85  3D 34 00 00 C0                  cmp eax, 0xc0000034
00742F8A  0F 84 99 02 00 00               je 0x140743229
00742F90  85 C0                           test eax, eax
00742F92  0F 88 A3 02 00 00               js 0x14074323b
00742F98  4D 8B EE                        mov r13, r14
00742F9B  66 41 39 3E                     cmp word ptr [r14], di
00742F9F  0F 84 77 02 00 00               je 0x14074321c
00742FA5  4C 8B 75 77                     mov r14, qword ptr [rbp + 0x77]
00742FA9  44 8B 7D 6F                     mov r15d, dword ptr [rbp + 0x6f]
00742FAD  48 8D 15 7C 9A 3B 00            lea rdx, [rip + 0x3b9a7c]
00742FB4  49 8B CD                        mov rcx, r13
00742FB7  E8 C4 D0 DB FF                  call 0x140500080
00742FBC  48 8B 4D BF                     mov rcx, qword ptr [rbp - 0x41]
00742FC0  48 8D 3D 09 9B 3B 00            lea rdi, [rip + 0x3b9b09]
00742FC7  85 C0                           test eax, eax
00742FC9  4C 8D 4D 0F                     lea r9, [rbp + 0xf]
00742FCD  49 0F 45 FD                     cmovne rdi, r13
00742FD1  45 33 C0                        xor r8d, r8d
00742FD4  48 8B D7                        mov rdx, rdi
00742FD7  48 89 7D 97                     mov qword ptr [rbp - 0x69], rdi
00742FDB  E8 0C 61 25 00                  call 0x1409990ec
00742FE0  45 33 C0                        xor r8d, r8d
00742FE3  85 C0                           test eax, eax
00742FE5  0F 88 FF 01 00 00               js 0x1407431ea
00742FEB  48 8B 75 0F                     mov rsi, qword ptr [rbp + 0xf]
00742FEF  8B 4E 04                        mov ecx, dword ptr [rsi + 4]
00742FF2  83 E9 01                        sub ecx, 1
00742FF5  0F 84 4D 01 00 00               je 0x140743148
00742FFB  83 E9 01                        sub ecx, 1
00742FFE  0F 84 44 01 00 00               je 0x140743148
00743004  83 F9 05                        cmp ecx, 5
00743007  0F 85 CC 01 00 00               jne 0x1407431d9
0074300D  8B 4E 0C                        mov ecx, dword ptr [rsi + 0xc]
00743010  8B 7E 08                        mov edi, dword ptr [rsi + 8]
00743013  48 03 FE                        add rdi, rsi
00743016  8D 41 FC                        lea eax, [rcx - 4]
00743019  3D FA FF 00 00                  cmp eax, 0xfffa
0074301E  0F 87 B5 01 00 00               ja 0x1407431d9
00743024  8B C1                           mov eax, ecx
00743026  48 D1 E8                        shr rax, 1
00743029  66 44 39 44 47 FE               cmp word ptr [rdi + rax*2 - 2], r8w
0074302F  0F 85 A4 01 00 00               jne 0x1407431d9
00743035  66 44 39 44 47 FC               cmp word ptr [rdi + rax*2 - 4], r8w
0074303B  0F 85 98 01 00 00               jne 0x1407431d9
00743041  41 0F B7 C0                     movzx eax, r8w
00743045  45 8B E0                        mov r12d, r8d
00743048  66 89 45 FF                     mov word ptr [rbp - 1], ax
0074304C  66 44 39 07                     cmp word ptr [rdi], r8w
00743050  0F 84 B9 00 00 00               je 0x14074310f
00743056  48 8B D7                        mov rdx, rdi
00743059  48 8D 4D EF                     lea rcx, [rbp - 0x11]
0074305D  E8 1E 77 CE FF                  call 0x14042a780
00743062  48 8B 45 AF                     mov rax, qword ptr [rbp - 0x51]
00743066  33 C9                           xor ecx, ecx
00743068  48 F7 D8                        neg rax
0074306B  66 89 4D C7                     mov word ptr [rbp - 0x39], cx
0074306F  48 8D 45 A7                     lea rax, [rbp - 0x59]
00743073  4D 8B C6                        mov r8, r14
00743076  4D 1B C9                        sbb r9, r9
00743079  48 8D 4D EF                     lea rcx, [rbp - 0x11]
0074307D  4C 23 C8                        and r9, rax
00743080  41 8B D7                        mov edx, r15d
00743083  48 8D 45 C7                     lea rax, [rbp - 0x39]
00743087  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0074308C  48 8B 45 7F                     mov rax, qword ptr [rbp + 0x7f]
00743090  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00743095  E8 7A 04 00 00                  call 0x140743514
0074309A  8B D8                           mov ebx, eax
0074309C  3D 25 02 00 C0                  cmp eax, 0xc0000225
007430A1  74 18                           je 0x1407430bb
007430A3  3D BB 00 00 C0                  cmp eax, 0xc00000bb
007430A8  74 11                           je 0x1407430bb
007430AA  85 C0                           test eax, eax
007430AC  0F 88 27 01 00 00               js 0x1407431d9
007430B2  0F B7 45 C7                     movzx eax, word ptr [rbp - 0x39]
007430B6  41 FF C4                        inc r12d
007430B9  EB 0A                           jmp 0x1407430c5
007430BB  45 33 C0                        xor r8d, r8d
007430BE  41 8B C0                        mov eax, r8d
007430C1  66 89 45 C7                     mov word ptr [rbp - 0x39], ax
007430C5  66 85 C0                        test ax, ax
007430C8  48 8D 4D EF                     lea rcx, [rbp - 0x11]
007430CC  48 8D 55 C7                     lea rdx, [rbp - 0x39]
007430D0  41 B1 01                        mov r9b, 1
007430D3  48 0F 44 D1                     cmove rdx, rcx
007430D7  45 33 C0                        xor r8d, r8d
007430DA  48 8D 4D FF                     lea rcx, [rbp - 1]
007430DE  E8 45 EA FE FF                  call 0x140731b28
007430E3  45 33 C0                        xor r8d, r8d
007430E6  8B D8                           mov ebx, eax
007430E8  85 C0                           test eax, eax
007430EA  0F 88 E9 00 00 00               js 0x1407431d9
007430F0  0F B7 45 EF                     movzx eax, word ptr [rbp - 0x11]
007430F4  48 D1 E8                        shr rax, 1
007430F7  48 8D 3C 47                     lea rdi, [rdi + rax*2]
007430FB  48 83 C7 02                     add rdi, 2
007430FF  66 44 39 07                     cmp word ptr [rdi], r8w
00743103  0F 85 4D FF FF FF               jne 0x140743056
00743109  0F B7 45 FF                     movzx eax, word ptr [rbp - 1]
0074310D  EB 08                           jmp 0x140743117
0074310F  85 DB                           test ebx, ebx
00743111  0F 88 C2 00 00 00               js 0x1407431d9
00743117  45 85 E4                        test r12d, r12d
0074311A  0F 84 B9 00 00 00               je 0x1407431d9
00743120  4C 8B 45 97                     mov r8, qword ptr [rbp - 0x69]
00743124  0F B7 C0                        movzx eax, ax
00743127  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
0074312B  48 8B 45 07                     mov rax, qword ptr [rbp + 7]
0074312F  44 8B 4E 04                     mov r9d, dword ptr [rsi + 4]
00743133  48 8B 55 BF                     mov rdx, qword ptr [rbp - 0x41]
00743137  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0074313C  E8 4B EA 24 00                  call 0x140991b8c
00743141  8B D8                           mov ebx, eax
00743143  E9 91 00 00 00                  jmp 0x1407431d9
00743148  8B 4E 0C                        mov ecx, dword ptr [rsi + 0xc]
0074314B  8B 56 08                        mov edx, dword ptr [rsi + 8]
0074314E  48 03 D6                        add rdx, rsi
00743151  8D 41 FD                        lea eax, [rcx - 3]
00743154  3D FB FF 00 00                  cmp eax, 0xfffb
00743159  77 7E                           ja 0x1407431d9
0074315B  8B C1                           mov eax, ecx
0074315D  48 D1 E8                        shr rax, 1
00743160  66 44 39 44 42 FE               cmp word ptr [rdx + rax*2 - 2], r8w
00743166  75 71                           jne 0x1407431d9
00743168  48 8D 4D EF                     lea rcx, [rbp - 0x11]
0074316C  E8 0F 76 CE FF                  call 0x14042a780
00743171  48 8B 45 AF                     mov rax, qword ptr [rbp - 0x51]
00743175  48 8D 4D EF                     lea rcx, [rbp - 0x11]
00743179  45 33 E4                        xor r12d, r12d
0074317C  4D 8B C6                        mov r8, r14
0074317F  48 F7 D8                        neg rax
00743182  66 44 89 65 C7                  mov word ptr [rbp - 0x39], r12w
00743187  48 8D 45 A7                     lea rax, [rbp - 0x59]
0074318B  41 8B D7                        mov edx, r15d
0074318E  4D 1B C9                        sbb r9, r9
00743191  4C 23 C8                        and r9, rax
00743194  48 8D 45 C7                     lea rax, [rbp - 0x39]
00743198  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0074319D  48 8B 45 7F                     mov rax, qword ptr [rbp + 0x7f]
007431A1  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
007431A6  E8 69 03 00 00                  call 0x140743514
007431AB  8B D8                           mov ebx, eax
007431AD  3D 25 02 00 C0                  cmp eax, 0xc0000225
007431B2  74 22                           je 0x1407431d6
007431B4  3D BB 00 00 C0                  cmp eax, 0xc00000bb
007431B9  74 1B                           je 0x1407431d6
007431BB  85 C0                           test eax, eax
007431BD  78 1A                           js 0x1407431d9
007431BF  0F B7 45 C7                     movzx eax, word ptr [rbp - 0x39]
007431C3  4C 8B C7                        mov r8, rdi
007431C6  83 C0 02                        add eax, 2
007431C9  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
007431CD  48 8B 45 CF                     mov rax, qword ptr [rbp - 0x31]
007431D1  E9 59 FF FF FF                  jmp 0x14074312f
007431D6  41 8B DC                        mov ebx, r12d
007431D9  33 D2                           xor edx, edx
007431DB  48 8B CE                        mov rcx, rsi
007431DE  E8 8D F6 43 00                  call 0x140b82870
007431E3  45 33 C0                        xor r8d, r8d
007431E6  85 DB                           test ebx, ebx
007431E8  78 23                           js 0x14074320d
007431EA  48 83 C8 FF                     or rax, 0xffffffffffffffff
007431EE  48 FF C0                        inc rax
007431F1  66 45 39 44 45 00               cmp word ptr [r13 + rax*2], r8w
007431F7  75 F5                           jne 0x1407431ee
007431F9  4D 8D 6C 45 00                  lea r13, [r13 + rax*2]
007431FE  49 83 C5 02                     add r13, 2
00743202  66 45 39 45 00                  cmp word ptr [r13], r8w
00743207  0F 85 A0 FD FF FF               jne 0x140742fad
0074320D  4C 8B 75 DF                     mov r14, qword ptr [rbp - 0x21]
00743211  4C 8B 7D E7                     mov r15, qword ptr [rbp - 0x19]
00743215  8B 75 9F                        mov esi, dword ptr [rbp - 0x61]
00743218  44 8B 65 8B                     mov r12d, dword ptr [rbp - 0x75]
0074321C  48 8B 4D BF                     mov rcx, qword ptr [rbp - 0x41]
00743220  E8 8B A0 F6 FF                  call 0x1406ad2b0
00743225  85 DB                           test ebx, ebx
00743227  78 14                           js 0x14074323d
00743229  44 8B 6D 8F                     mov r13d, dword ptr [rbp - 0x71]
0074322D  FF C6                           inc esi
0074322F  E9 17 FC FF FF                  jmp 0x140742e4b
00743234  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00743239  EB 11                           jmp 0x14074324c
0074323B  8B D8                           mov ebx, eax
0074323D  4D 85 FF                        test r15, r15
00743240  74 0A                           je 0x14074324c
00743242  33 D2                           xor edx, edx
00743244  49 8B CF                        mov rcx, r15
00743247  E8 24 F6 43 00                  call 0x140b82870
0074324C  4D 85 F6                        test r14, r14
0074324F  0F 84 76 FA FF FF               je 0x140742ccb
00743255  33 D2                           xor edx, edx
00743257  49 8B CE                        mov rcx, r14
0074325A  E8 11 F6 43 00                  call 0x140b82870
0074325F  E9 67 FA FF FF                  jmp 0x140742ccb
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PiDrvDbResolveFilePathKeyValues(__int64 a1, int a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_mF0;
    unsigned int v_stack_mF8;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;

    *(unsigned __int64 *)(v_rsp + 32) = a4;
    *(unsigned __int64 *)(v_rsp + 24) = a3;
    *(unsigned int *)(v_rsp + 16) = a2;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (216);
    result = 0;
    *(unsigned __int64 *)(v_rsp - 95 - 41) = 0;
    *(unsigned int *)(v_rsp - 95 - 121) = 0;
    *(unsigned int *)(v_rsp - 95 - 105) = 0;
    a2 = 0;
    *(unsigned int *)(v_rsp - 95 - 113) = 0;
    *(unsigned __int64 *)(v_rsp - 95 - 25) = 0;
    *(unsigned __int64 *)(v_rsp - 95 - 89) = v_xmm0;
    *(unsigned int *)(v_rsp - 95 - 117) = 0;
    *(unsigned __int64 *)(v_rsp - 95 - 33) = 0;
    *(unsigned __int64 *)(v_rsp - 95 - 65) = 0;
    *(unsigned __int64 *)(v_rsp - 95 + 15) = 0;
    *(unsigned __int64 *)(v_rsp - 95 - 17) = v_xmm0;
    *(unsigned int *)(v_rsp - 95 - 73) = 0;
    *(unsigned __int64 *)(v_rsp - 95 - 57) = v_xmm1;
    *(unsigned __int64 *)(v_rsp - 95 - 1) = v_xmm0;
    result = RtlInitUnicodeString(v_rsp - 95 - 89, a2, a3, a4);
    a2 = 0;
    result = RtlInitUnicodeString(v_rsp - 95 - 57, a2, a3, a4);
    a2 = 0;
    result = RtlInitUnicodeString(v_rsp - 95 - 1, a2, a3, a4);
    a4 = 0;
    v_stack_mF0 = v_rsp - 95 - 41;
    v_stack_mF8 = 0x20019ULL;
    a1 = 0;
    result = PnpCtxRegOpenKey(a1, a1, v_rip + 3916996, a4);
    if (((unsigned int)(result)) != 0xC0000034ULL) goto loc_00742D0B;
    v_rdi = 0;
loc_00742CC9:
loc_00742CCB:
    result = RtlFreeAnsiString(v_rsp - 95 - 89, a1, v_rip + 3916996, a4);
    result = RtlFreeAnsiString(v_rsp - 95 - 57, a1, v_rip + 3916996, a4);
    result = RtlFreeAnsiString(v_rsp - 95 - 1, a1, v_rip + 3916996, a4);
    if (*(unsigned __int64 *)(v_rsp - 95 - 41) != 0) {
        result = ZwClose(*(unsigned __int64 *)(v_rsp - 95 - 41), a1, v_rip + 3916996, a4);
    }
    v_rsp = (v_rsp) + (216);
    return 0;
loc_00742D0B:
    if (sign_flag) goto loc_00742CCB;
    result = PiDrvDbQuerySystemPathWin32(0, v_rsp - 95 - 89, v_rip + 3916996, a4);
    result = 0;
    v_rbx = (unsigned int)((unsigned int)(result));
    if (sign_flag) {
        a2 = 0;
        a1 = v_rsp - 95 - 89;
        v_rbx = 0;
        result = RtlInitUnicodeString(a1, a2, v_rip + 3916996, a4);
    }
    if ((((unsigned __int8)((unsigned int)(a2))) & (2)) == 0) goto loc_00742D72;
    if (0 == 0) goto loc_00742D53;
    result = RtlEqualUnicodeString(0, v_rip + 4227075, 1, a4);
    v_rdi = 0;
    if ((unsigned __int8)(result) == 0) goto loc_00742DAC;
loc_00742D53:
    if ((*(unsigned __int64 *)(v_rsp - 95 - 81)) == 0) goto loc_00742D74;
    result = RtlEqualUnicodeString(v_rsp - 95 - 89, v_rip + 4227981, 1, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00742DAC;
    goto loc_00742D74;
loc_00742D72:
    v_rdi = 0;
loc_00742D74:
    if ((((unsigned __int8)((unsigned int)(a2))) & (1)) == 0) goto loc_00742CC9;
    if (*(unsigned __int64 *)(v_rsp - 95 + 127) == 0) goto loc_00742CC9;
    if ((*(unsigned __int64 *)(v_rsp - 95 - 81)) == 0) goto loc_00742CC9;
    result = RtlEqualUnicodeString(*(unsigned __int64 *)(v_rsp - 95 + 127), v_rsp - 95 - 89, 1, a4);
    if ((unsigned __int8)(result) != 0) goto loc_00742CC9;
loc_00742DAC:
    v_stack_p30 = v_rsp - 95 - 105;
    a4 = 0;
    a3 = 0;
    v_stack_p28 = v_rsp - 95 - 121;
    v_stack_p20 = 0;
    result = PnpCtxRegQueryInfoKey(*(unsigned __int64 *)(v_rsp - 95 + 127), *(unsigned __int64 *)(v_rsp - 95 - 41), a3, a4);
    if (sign_flag) goto loc_00742E49;
    *(unsigned int *)(v_rsp - 95 - 117) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 105)));
    *(unsigned int *)(v_rsp - 95 - 113) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 121)) * 2 + 2);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 121)) * 2 + 2) == 0) goto loc_00742E1B;
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 121)) * 2 + 2)), (unsigned int)(0x62647050ULL), a4);
    *(unsigned __int64 *)(v_rsp - 95 - 25) = result;
    if (result != 0) goto loc_00742E1B;
    goto loc_00742CCB;
loc_00742E1B:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 105))) == 0) goto loc_00742E49;
    result = ExAllocatePool2(256, (unsigned int)(*(unsigned int *)(v_rsp - 95 - 105)), (unsigned int)(0x62647050ULL), a4);
    *(unsigned __int64 *)(v_rsp - 95 - 33) = result;
    if (result != 0) goto loc_00742E49;
loc_00742E3F:
    goto loc_0074323D;
loc_00742E49:
loc_00742E4B:
    v_stack_p38 = v_rsp - 95 - 121;
    v_stack_p30 = result;
    v_stack_p28 = v_rsp - 95 - 73;
    v_rdi = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 121)) * 2 + 2))) >> (1));
    v_stack_p20 = v_rsp - 95 - 105;
    *(unsigned int *)(v_rsp - 95 - 97) = 0;
    *(unsigned int *)(v_rsp - 95 - 105) = (unsigned int)(v_rdi);
    *(unsigned int *)(v_rsp - 95 - 121) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 105)));
    result = PnpCtxRegEnumValue(256, *(unsigned __int64 *)(v_rsp - 95 - 41), 0, result);
    if (((unsigned int)(result)) == 0x8000001AULL) goto loc_0074323D;
    if (((unsigned int)(result)) != 0xC0000023ULL) goto loc_00742F27;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 105)))) <= ((unsigned int)(v_rdi))) goto loc_00742EE0;
    *(unsigned int *)(v_rsp - 95 - 113) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 105)) + (unsigned int)(*(unsigned int *)(v_rsp - 95 - 105)) * 1);
    result = (unsigned int)(*(unsigned int *)(v_rsp - 95 - 105));
    if (result != 0) {
        a2 = 0;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, 0, result);
    }
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 105)) + (unsigned int)(*(unsigned int *)(v_rsp - 95 - 105)) * 1)), (unsigned int)(0x62647050ULL), result);
    *(unsigned __int64 *)(v_rsp - 95 - 25) = result;
    if (result == 0) goto loc_00743234;
loc_00742EE0:
    if ((*(unsigned int *)(v_rsp - 95 - 121)) <= ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 105))))) goto loc_00742F20;
    *(unsigned int *)(v_rsp - 95 - 117) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 121)));
    if (result != 0) {
        a2 = 0;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, (unsigned int)(0x62647050ULL), result);
    }
    result = ExAllocatePool2(256, (unsigned int)(*(unsigned int *)(v_rsp - 95 - 121)), (unsigned int)(0x62647050ULL), result);
    *(unsigned __int64 *)(v_rsp - 95 - 33) = result;
    if (result == 0) goto loc_00742E3F;
loc_00742F20:
    v_rsi = (unsigned int)((0) - 1);
    goto loc_00743229;
loc_00742F27:
    v_rdi = 0;
    if (sign_flag) goto loc_0074323B;
    if ((*(unsigned int *)(v_rsp - 95 - 73)) != 7) goto loc_00743229;
    if ((*(unsigned int *)(v_rsp - 95 - 121)) < 4) goto loc_00743229;
    result = ((unsigned int)(*(unsigned int *)(v_rsp - 95 - 121))) >> (1);
    if ((*(unsigned __int16 *)(result + result * 2 - 2)) != 0) goto loc_00743229;
    if ((*(unsigned __int16 *)(result + result * 2 - 4)) != 0) goto loc_00743229;
    v_stack_p28 = v_rsp - 95 - 65;
    a4 = 0;
    v_stack_p20 = 0x2001FULL;
    a1 = 0;
    result = PnpCtxRegOpenKey(a1, *(unsigned __int64 *)(v_rsp - 95 + 103), result, a4);
    if (((unsigned int)(result)) == 0xC0000034ULL) goto loc_00743229;
    if (sign_flag) goto loc_0074323B;
    if ((*(unsigned __int16 *)(result)) == 0) goto loc_0074321C;
loc_00742FAD:
    result = wcsicmp(result, v_rip + 3906172, result, a4);
    v_rdi = v_rip + 3906313;
    if ((unsigned int)(result) != 0) { v_rdi = result; }
    a3 = 0;
    *(unsigned __int64 *)(v_rsp - 95 - 105) = v_rdi;
    result = IopGetRegistryValue(*(unsigned __int64 *)(v_rsp - 95 - 65), v_rdi, a3, v_rsp - 95 + 15);
    a3 = 0;
    if (sign_flag) goto loc_007431EA;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 + 15) + 4))) - (1));
    if (condition_is_equal) goto loc_00743148;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00743148;
    if (((unsigned int)(a1)) != 5) goto loc_007431D9;
    v_rdi = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 + 15) + 8))) + (*(unsigned __int64 *)(v_rsp - 95 + 15));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 + 15) + 12)) - 4)) > 0xFFFAULL) goto loc_007431D9;
    result = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 + 15) + 12))))) >> (1);
    if ((*(unsigned __int16 *)(v_rdi + result * 2 - 2)) != 0) goto loc_007431D9;
    if ((*(unsigned __int16 *)(v_rdi + result * 2 - 4)) != 0) goto loc_007431D9;
    *(unsigned __int16 *)(v_rsp - 95 - 1) = 0;
    if ((*(unsigned __int16 *)(v_rdi)) == 0) goto loc_0074310F;
loc_00743056:
    result = RtlInitUnicodeString(v_rsp - 95 - 17, v_rdi, a3, v_rsp - 95 + 15);
    a1 = 0;
    result = -(*(unsigned __int64 *)(v_rsp - 95 - 81));
    *(unsigned __int16 *)(v_rsp - 95 - 57) = 0;
    a4 = (v_rsp - 95 + 15) & (v_rsp - 95 - 89);
    v_stack_p28 = v_rsp - 95 - 57;
    v_stack_p20 = *(unsigned __int64 *)(v_rsp - 95 + 127);
    result = PiDrvDbResolveSystemFilePath(v_rsp - 95 - 17, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 + 111)))), *(unsigned __int64 *)(v_rsp - 95 + 119), a4);
    if (((unsigned int)(result)) == 0xC0000225ULL) goto loc_007430BB;
    if (((unsigned int)(result)) == 0xC00000BBULL) goto loc_007430BB;
    if (sign_flag) goto loc_007431D9;
    v_r12 = (unsigned int)((0) + 1);
    goto loc_007430C5;
loc_007430BB:
    a3 = 0;
    *(unsigned __int16 *)(v_rsp - 95 - 57) = 0;
loc_007430C5:
    a2 = v_rsp - 95 - 57;
    if (0 == 0) { a2 = v_rsp - 95 - 17; }
    a3 = 0;
    result = PiDevCfgAppendMultiSz(v_rsp - 95 - 1, a2, a3, 1);
    a3 = 0;
    if (sign_flag) goto loc_007431D9;
    result = (*(unsigned __int16 *)(v_rsp - 95 - 17)) >> (1);
    v_rdi = (v_rdi + result * 2) + (2);
    if ((*(unsigned __int16 *)(v_rdi)) != 0) goto loc_00743056;
    goto loc_00743117;
loc_0074310F:
    if (sign_flag) goto loc_007431D9;
loc_00743117:
    if ((unsigned int)(v_r12) == 0) goto loc_007431D9;
    v_stack_p28 = (unsigned int)((unsigned __int16)(*(unsigned __int16 *)(v_rsp - 95 - 1)));
loc_0074312F:
    v_stack_p20 = *(unsigned __int64 *)(v_rsp - 95 + 7);
    result = PnpCtxRegSetValue(v_rsp - 95 - 1, *(unsigned __int64 *)(v_rsp - 95 - 65), *(unsigned __int64 *)(v_rsp - 95 - 105), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 + 15) + 4)));
    goto loc_007431D9;
loc_00743148:
    a2 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 + 15) + 8))) + (*(unsigned __int64 *)(v_rsp - 95 + 15));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 + 15) + 12)) - 3)) > 0xFFFBULL) goto loc_007431D9;
    result = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 + 15) + 12))))) >> (1);
    if ((*(unsigned __int16 *)(a2 + result * 2 - 2)) != ((unsigned __int16)(*(unsigned __int64 *)(v_rsp - 95 - 105)))) goto loc_007431D9;
    result = RtlInitUnicodeString(v_rsp - 95 - 17, a2, *(unsigned __int64 *)(v_rsp - 95 - 105), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 + 15) + 4)));
    v_r12 = 0;
    result = -(*(unsigned __int64 *)(v_rsp - 95 - 81));
    *(unsigned __int16 *)(v_rsp - 95 - 57) = 0;
    a4 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 + 15) + 4))) & (v_rsp - 95 - 89);
    v_stack_p28 = v_rsp - 95 - 57;
    v_stack_p20 = *(unsigned __int64 *)(v_rsp - 95 + 127);
    result = PiDrvDbResolveSystemFilePath(v_rsp - 95 - 17, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 + 111)))), *(unsigned __int64 *)(v_rsp - 95 + 119), a4);
    if (((unsigned int)(result)) == 0xC0000225ULL) goto loc_007431D6;
    if (((unsigned int)(result)) == 0xC00000BBULL) goto loc_007431D6;
    if (sign_flag) goto loc_007431D9;
    result = (unsigned int)((*(unsigned __int16 *)(v_rsp - 95 - 57)) + (2));
    v_stack_p28 = (unsigned int)(result);
    goto loc_0074312F;
loc_007431D6:
loc_007431D9:
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(v_rsp - 95 + 15), a2, v_rdi, a4);
    a3 = 0;
    if (sign_flag) goto loc_0074320D;
loc_007431EA:
    result = (result) | (-1);
loc_007431EE:
    result = (result) + 1;
    if ((*(unsigned __int16 *)(result + result * 2)) != 0) goto loc_007431EE;
    v_r13 = (result + result * 2) + (2);
    if ((*(unsigned __int16 *)(v_r13)) != 0) goto loc_00742FAD;
loc_0074320D:
loc_0074321C:
    result = ZwClose(*(unsigned __int64 *)(v_rsp - 95 - 65), a2, a3, a4);
    if (sign_flag) goto loc_0074323D;
loc_00743229:
    v_rsi = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 95 - 97))) + 1);
    goto loc_00742E4B;
loc_00743234:
    goto loc_0074324C;
loc_0074323B:
loc_0074323D:
    if (*(unsigned __int64 *)(v_rsp - 95 - 25) != 0) {
        a2 = 0;
        a1 = *(unsigned __int64 *)(v_rsp - 95 - 25);
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
    if (*(unsigned __int64 *)(v_rsp - 95 - 33) == 0) goto loc_00742CCB;
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(v_rsp - 95 - 33), a2, a3, a4);
    goto loc_00742CCB;
}
```

## 5. (Beta) C Style

```c
int64_t PiDrvDbResolveFilePathKeyValues(int64_t Arg1, int32_t Arg2, int64_t Arg3, int64_t Arg4)
{
    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_mF0;
    uint32_t v_stack_mF8;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;

    *(uint64_t *)(local_rsp + 0x20) = Arg4;
    *(uint64_t *)(local_rsp + 0x18) = Arg3;
    *(uint32_t *)(local_rsp + 0x10) = Arg2;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (216);
    result = 0;
    *(uint64_t *)(local_rsp - 0x5F - 0x29) = 0;
    *(uint32_t *)(local_rsp - 0x5F - 0x79) = 0;
    *(uint32_t *)(local_rsp - 0x5F - 0x69) = 0;
    Arg2 = 0;
    *(uint32_t *)(local_rsp - 0x5F - 0x71) = 0;
    *(uint64_t *)(local_rsp - 0x5F - 0x19) = 0;
    *(uint64_t *)(local_rsp - 0x5F - 0x59) = v_xmm0;
    *(uint32_t *)(local_rsp - 0x5F - 0x75) = 0;
    *(uint64_t *)(local_rsp - 0x5F - 0x21) = 0;
    *(uint64_t *)(local_rsp - 0x5F - 0x41) = 0;
    *(uint64_t *)(local_rsp - 0x5F + 0xF) = 0;
    *(uint64_t *)(local_rsp - 0x5F - 0x11) = v_xmm0;
    *(uint32_t *)(local_rsp - 0x5F - 0x49) = 0;
    *(uint64_t *)(local_rsp - 0x5F - 0x39) = v_xmm1;
    *(uint64_t *)(local_rsp - 0x5F - 0x1) = v_xmm0;
    result = RtlInitUnicodeString(local_rsp - 95 - 89, Arg2, Arg3, Arg4);
    Arg2 = 0;
    result = RtlInitUnicodeString(local_rsp - 95 - 57, Arg2, Arg3, Arg4);
    Arg2 = 0;
    result = RtlInitUnicodeString(local_rsp - 95 - 1, Arg2, Arg3, Arg4);
    Arg4 = 0;
    v_stack_mF0 = local_rsp - 95 - 41;
    v_stack_mF8 = 0x20019ULL;
    Arg1 = 0;
    result = PnpCtxRegOpenKey(Arg1, Arg1, v_rip + 3916996, Arg4);
    if (((uint32_t)(result)) != 0xC0000034ULL) goto loc_00742D0B;
    local_rdi = 0;
loc_00742CC9:
loc_00742CCB:
    result = RtlFreeAnsiString(local_rsp - 95 - 89, Arg1, v_rip + 3916996, Arg4);
    result = RtlFreeAnsiString(local_rsp - 95 - 57, Arg1, v_rip + 3916996, Arg4);
    result = RtlFreeAnsiString(local_rsp - 95 - 1, Arg1, v_rip + 3916996, Arg4);
    if (*(uint64_t *)(local_rsp - 0x5F - 0x29) != 0) {
        result = ZwClose(*(uint64_t *)(local_rsp - 0x5F - 0x29), Arg1, v_rip + 3916996, Arg4);
    }
    local_rsp = (local_rsp) + (216);
    return 0;
loc_00742D0B:
    if (sign_flag) goto loc_00742CCB;
    result = PiDrvDbQuerySystemPathWin32(0, local_rsp - 95 - 89, v_rip + 3916996, Arg4);
    result = 0;
    local_rbx = (uint32_t)((uint32_t)(result));
    if (sign_flag) {
        Arg2 = 0;
        Arg1 = local_rsp - 95 - 89;
        local_rbx = 0;
        result = RtlInitUnicodeString(Arg1, Arg2, v_rip + 3916996, Arg4);
    }
    if ((((uint8_t)((uint32_t)(Arg2))) & (2)) == 0) goto loc_00742D72;
    if (0 == 0) goto loc_00742D53;
    result = RtlEqualUnicodeString(0, v_rip + 4227075, 1, Arg4);
    local_rdi = 0;
    if ((uint8_t)(result) == 0) goto loc_00742DAC;
loc_00742D53:
    if ((*(uint64_t *)(local_rsp - 0x5F - 0x51)) == 0) goto loc_00742D74;
    result = RtlEqualUnicodeString(local_rsp - 95 - 89, v_rip + 4227981, 1, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00742DAC;
    goto loc_00742D74;
loc_00742D72:
    local_rdi = 0;
loc_00742D74:
    if ((((uint8_t)((uint32_t)(Arg2))) & (1)) == 0) goto loc_00742CC9;
    if (*(uint64_t *)(local_rsp - 0x5F + 0x7F) == 0) goto loc_00742CC9;
    if ((*(uint64_t *)(local_rsp - 0x5F - 0x51)) == 0) goto loc_00742CC9;
    result = RtlEqualUnicodeString(*(uint64_t *)(local_rsp - 0x5F + 0x7F), local_rsp - 95 - 89, 1, Arg4);
    if ((uint8_t)(result) != 0) goto loc_00742CC9;
loc_00742DAC:
    v_stack_p30 = local_rsp - 95 - 105;
    Arg4 = 0;
    Arg3 = 0;
    v_stack_p28 = local_rsp - 95 - 121;
    v_stack_p20 = 0;
    result = PnpCtxRegQueryInfoKey(*(uint64_t *)(local_rsp - 0x5F + 0x7F), *(uint64_t *)(local_rsp - 0x5F - 0x29), Arg3, Arg4);
    if (sign_flag) goto loc_00742E49;
    *(uint32_t *)(local_rsp - 0x5F - 0x75) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x69)));
    *(uint32_t *)(local_rsp - 0x5F - 0x71) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x79)) * 2 + 2);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x79)) * 2 + 2) == 0) goto loc_00742E1B;
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x79)) * 2 + 2)), (uint32_t)(0x62647050ULL), Arg4);
    *(uint64_t *)(local_rsp - 0x5F - 0x19) = result;
    if (result != 0) goto loc_00742E1B;
    goto loc_00742CCB;
loc_00742E1B:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x69))) == 0) goto loc_00742E49;
    result = ExAllocatePool2(256, (uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x69)), (uint32_t)(0x62647050ULL), Arg4);
    *(uint64_t *)(local_rsp - 0x5F - 0x21) = result;
    if (result != 0) goto loc_00742E49;
loc_00742E3F:
    goto loc_0074323D;
loc_00742E49:
loc_00742E4B:
    v_stack_p38 = local_rsp - 95 - 121;
    v_stack_p30 = result;
    v_stack_p28 = local_rsp - 95 - 73;
    local_rdi = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x79)) * 2 + 2))) >> (1));
    v_stack_p20 = local_rsp - 95 - 105;
    *(uint32_t *)(local_rsp - 0x5F - 0x61) = 0;
    *(uint32_t *)(local_rsp - 0x5F - 0x69) = (uint32_t)(local_rdi);
    *(uint32_t *)(local_rsp - 0x5F - 0x79) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x69)));
    result = PnpCtxRegEnumValue(256, *(uint64_t *)(local_rsp - 0x5F - 0x29), 0, result);
    if (((uint32_t)(result)) == 0x8000001AULL) goto loc_0074323D;
    if (((uint32_t)(result)) != 0xC0000023ULL) goto loc_00742F27;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x69)))) <= ((uint32_t)(local_rdi))) goto loc_00742EE0;
    *(uint32_t *)(local_rsp - 0x5F - 0x71) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x69)) + (uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x69)) * 1);
    result = (uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x69));
    if (result != 0) {
        Arg2 = 0;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, 0, result);
    }
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x69)) + (uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x69)) * 1)), (uint32_t)(0x62647050ULL), result);
    *(uint64_t *)(local_rsp - 0x5F - 0x19) = result;
    if (result == 0) goto loc_00743234;
loc_00742EE0:
    if ((*(uint32_t *)(local_rsp - 0x5F - 0x79)) <= ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x69))))) goto loc_00742F20;
    *(uint32_t *)(local_rsp - 0x5F - 0x75) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x79)));
    if (result != 0) {
        Arg2 = 0;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, (uint32_t)(0x62647050ULL), result);
    }
    result = ExAllocatePool2(256, (uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x79)), (uint32_t)(0x62647050ULL), result);
    *(uint64_t *)(local_rsp - 0x5F - 0x21) = result;
    if (result == 0) goto loc_00742E3F;
loc_00742F20:
    local_rsi = (uint32_t)((0) - 1);
    goto loc_00743229;
loc_00742F27:
    local_rdi = 0;
    if (sign_flag) goto loc_0074323B;
    if ((*(uint32_t *)(local_rsp - 0x5F - 0x49)) != 7) goto loc_00743229;
    if ((*(uint32_t *)(local_rsp - 0x5F - 0x79)) < 4) goto loc_00743229;
    result = ((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x79))) >> (1);
    if ((*(uint16_t *)(result + result * 2 - 0x2)) != 0) goto loc_00743229;
    if ((*(uint16_t *)(result + result * 2 - 0x4)) != 0) goto loc_00743229;
    v_stack_p28 = local_rsp - 95 - 65;
    Arg4 = 0;
    v_stack_p20 = 0x2001FULL;
    Arg1 = 0;
    result = PnpCtxRegOpenKey(Arg1, *(uint64_t *)(local_rsp - 0x5F + 0x67), result, Arg4);
    if (((uint32_t)(result)) == 0xC0000034ULL) goto loc_00743229;
    if (sign_flag) goto loc_0074323B;
    if ((*(uint16_t *)(result)) == 0) goto loc_0074321C;
loc_00742FAD:
    result = wcsicmp(result, v_rip + 3906172, result, Arg4);
    local_rdi = v_rip + 3906313;
    if ((uint32_t)(result) != 0) { local_rdi = result; }
    Arg3 = 0;
    *(uint64_t *)(local_rsp - 0x5F - 0x69) = local_rdi;
    result = IopGetRegistryValue(*(uint64_t *)(local_rsp - 0x5F - 0x41), local_rdi, Arg3, local_rsp - 95 + 15);
    Arg3 = 0;
    if (sign_flag) goto loc_007431EA;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F + 0xF) + 0x4))) - (1));
    if (condition_is_equal) goto loc_00743148;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00743148;
    if (((uint32_t)(Arg1)) != 5) goto loc_007431D9;
    local_rdi = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F + 0xF) + 0x8))) + (*(uint64_t *)(local_rsp - 0x5F + 0xF));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F + 0xF) + 0xC)) - 4)) > 0xFFFAULL) goto loc_007431D9;
    result = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F + 0xF) + 0xC))))) >> (1);
    if ((*(uint16_t *)(local_rdi + result * 2 - 0x2)) != 0) goto loc_007431D9;
    if ((*(uint16_t *)(local_rdi + result * 2 - 0x4)) != 0) goto loc_007431D9;
    *(uint16_t *)(local_rsp - 0x5F - 0x1) = 0;
    if ((*(uint16_t *)(local_rdi)) == 0) goto loc_0074310F;
loc_00743056:
    result = RtlInitUnicodeString(local_rsp - 95 - 17, local_rdi, Arg3, local_rsp - 95 + 15);
    Arg1 = 0;
    result = -(*(uint64_t *)(local_rsp - 0x5F - 0x51));
    *(uint16_t *)(local_rsp - 0x5F - 0x39) = 0;
    Arg4 = (local_rsp - 95 + 15) & (local_rsp - 95 - 89);
    v_stack_p28 = local_rsp - 95 - 57;
    v_stack_p20 = *(uint64_t *)(local_rsp - 0x5F + 0x7F);
    result = PiDrvDbResolveSystemFilePath(local_rsp - 95 - 17, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F + 0x6F)))), *(uint64_t *)(local_rsp - 0x5F + 0x77), Arg4);
    if (((uint32_t)(result)) == 0xC0000225ULL) goto loc_007430BB;
    if (((uint32_t)(result)) == 0xC00000BBULL) goto loc_007430BB;
    if (sign_flag) goto loc_007431D9;
    local_r12 = (uint32_t)((0) + 1);
    goto loc_007430C5;
loc_007430BB:
    Arg3 = 0;
    *(uint16_t *)(local_rsp - 0x5F - 0x39) = 0;
loc_007430C5:
    Arg2 = local_rsp - 95 - 57;
    if (0 == 0) { Arg2 = local_rsp - 95 - 17; }
    Arg3 = 0;
    result = PiDevCfgAppendMultiSz(local_rsp - 95 - 1, Arg2, Arg3, 1);
    Arg3 = 0;
    if (sign_flag) goto loc_007431D9;
    result = (*(uint16_t *)(local_rsp - 0x5F - 0x11)) >> (1);
    local_rdi = (local_rdi + result * 2) + (2);
    if ((*(uint16_t *)(local_rdi)) != 0) goto loc_00743056;
    goto loc_00743117;
loc_0074310F:
    if (sign_flag) goto loc_007431D9;
loc_00743117:
    if ((uint32_t)(local_r12) == 0) goto loc_007431D9;
    v_stack_p28 = (uint32_t)((uint16_t)(*(uint16_t *)(local_rsp - 0x5F - 0x1)));
loc_0074312F:
    v_stack_p20 = *(uint64_t *)(local_rsp - 0x5F + 0x7);
    result = PnpCtxRegSetValue(local_rsp - 95 - 1, *(uint64_t *)(local_rsp - 0x5F - 0x41), *(uint64_t *)(local_rsp - 0x5F - 0x69), (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F + 0xF) + 0x4)));
    goto loc_007431D9;
loc_00743148:
    Arg2 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F + 0xF) + 0x8))) + (*(uint64_t *)(local_rsp - 0x5F + 0xF));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F + 0xF) + 0xC)) - 3)) > 0xFFFBULL) goto loc_007431D9;
    result = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F + 0xF) + 0xC))))) >> (1);
    if ((*(uint16_t *)(Arg2 + result * 2 - 0x2)) != ((uint16_t)(*(uint64_t *)(local_rsp - 0x5F - 0x69)))) goto loc_007431D9;
    result = RtlInitUnicodeString(local_rsp - 95 - 17, Arg2, *(uint64_t *)(local_rsp - 0x5F - 0x69), (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F + 0xF) + 0x4)));
    local_r12 = 0;
    result = -(*(uint64_t *)(local_rsp - 0x5F - 0x51));
    *(uint16_t *)(local_rsp - 0x5F - 0x39) = 0;
    Arg4 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F + 0xF) + 0x4))) & (local_rsp - 95 - 89);
    v_stack_p28 = local_rsp - 95 - 57;
    v_stack_p20 = *(uint64_t *)(local_rsp - 0x5F + 0x7F);
    result = PiDrvDbResolveSystemFilePath(local_rsp - 95 - 17, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F + 0x6F)))), *(uint64_t *)(local_rsp - 0x5F + 0x77), Arg4);
    if (((uint32_t)(result)) == 0xC0000225ULL) goto loc_007431D6;
    if (((uint32_t)(result)) == 0xC00000BBULL) goto loc_007431D6;
    if (sign_flag) goto loc_007431D9;
    result = (uint32_t)((*(uint16_t *)(local_rsp - 0x5F - 0x39)) + (2));
    v_stack_p28 = (uint32_t)(result);
    goto loc_0074312F;
loc_007431D6:
loc_007431D9:
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(local_rsp - 0x5F + 0xF), Arg2, local_rdi, Arg4);
    Arg3 = 0;
    if (sign_flag) goto loc_0074320D;
loc_007431EA:
    result = (result) | (-1);
loc_007431EE:
    result = (result) + 1;
    if ((*(uint16_t *)(result + result * 2)) != 0) goto loc_007431EE;
    local_r13 = (result + result * 2) + (2);
    if ((*(uint16_t *)(local_r13)) != 0) goto loc_00742FAD;
loc_0074320D:
loc_0074321C:
    result = ZwClose(*(uint64_t *)(local_rsp - 0x5F - 0x41), Arg2, Arg3, Arg4);
    if (sign_flag) goto loc_0074323D;
loc_00743229:
    local_rsi = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x61))) + 1);
    goto loc_00742E4B;
loc_00743234:
    goto loc_0074324C;
loc_0074323B:
loc_0074323D:
    if (*(uint64_t *)(local_rsp - 0x5F - 0x19) != 0) {
        Arg2 = 0;
        Arg1 = *(uint64_t *)(local_rsp - 0x5F - 0x19);
        result = ExFreePoolWithTag(Arg1, Arg2, Arg3, Arg4);
    }
    if (*(uint64_t *)(local_rsp - 0x5F - 0x21) == 0) goto loc_00742CCB;
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(local_rsp - 0x5F - 0x21), Arg2, Arg3, Arg4);
    goto loc_00742CCB;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00742C00&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
