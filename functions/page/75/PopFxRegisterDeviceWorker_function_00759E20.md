# PopFxRegisterDeviceWorker

- RVA: `0x00759E20`–`0x0075A697` (길이 `2,167` bytes)
- VA: `0x0000000140759E20`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CC1A8`
- 디코드: `547`개 명령, `2,167/2,167` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **19**; 고유 호출 대상: **14**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00759E96` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0075A037` → [PopFxFindAcpiDeviceByUniqueId](../../text/4C/PopFxFindAcpiDeviceByUniqueId_function_004C5C30.md) (function, `0x004C5C30`)
- `0x0075A07B` → [PopFxCreateDeviceCommon](../../text/5D/PopFxCreateDeviceCommon_function_005D2424.md) (function, `0x005D2424`)
- `0x0075A0AE` → [IoInitializeRemoveLockEx](../../text/4C/IoInitializeRemoveLockEx_function_004C8F10.md) (function, `0x004C8F10`)
- `0x0075A0BF` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0075A0E4` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0075A250` → [KeInitializeEvent](../../text/40/KeInitializeEvent_function_0040DD10.md) (function, `0x0040DD10`)
- `0x0075A47C` → [PopFxVerifyDependencies](PopFxVerifyDependencies_function_0075A7E4.md) (function, `0x0075A7E4`)
- `0x0075A501` → [PopFxActivateComponent](../../text/2D/PopFxActivateComponent_function_002D9DBC.md) (function, `0x002D9DBC`)
- `0x0075A528` → [IoAllocateIrp](../../text/20/IoAllocateIrp_function_002065D0.md) (function, `0x002065D0`)
- `0x0075A548` → [PopFxRegisterDeviceWithPep](../../text/4C/PopFxRegisterDeviceWithPep_function_004CF794.md) (function, `0x004CF794`)
- `0x0075A55F` → [PopFxBugCheck](../../text/2B/PopFxBugCheck_function_002BFC6C.md) (function, `0x002BFC6C`)
- `0x0075A568` → [PopPlRegisterDevice](../../text/4B/PopPlRegisterDevice_function_004B820C.md) (function, `0x004B820C`)
- `0x0075A5EE` → [PopPlRegisterComponent](../../text/4A/PopPlRegisterComponent_function_004AA1FC.md) (function, `0x004AA1FC`)
- `0x0075A624` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0075A63F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0075A651` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0075A662` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0075A674` → [PopFxReleaseAcpiRefDevice](../../text/5D/PopFxReleaseAcpiRefDevice_function_005D3444.md) (function, `0x005D3444`)

### Direct callers
- [PoFxRegisterCoreDevice](PoFxRegisterCoreDevice_function_00758800.md) at `0x007588CD`
- [PopFxRegisterDevice](PopFxRegisterDevice_function_00759B80.md) at `0x00759CD0`

### Static image references
- `0x00759FED` → RVA `0x00E0B3CC` (`.data`; read)
- `0x0075A22C` → RVA `0x002C0420` (`PopFxComponentWork`; read)
- `0x0075A56D` → RVA `0x00E6784C` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **18**
  - `0x00759E96` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0075A037` → [PopFxFindAcpiDeviceByUniqueId](../../text/4C/PopFxFindAcpiDeviceByUniqueId_function_004C5C30.md) (`PAGE` → `.text`)
  - `0x0075A07B` → [PopFxCreateDeviceCommon](../../text/5D/PopFxCreateDeviceCommon_function_005D2424.md) (`PAGE` → `.text`)
  - `0x0075A0AE` → [IoInitializeRemoveLockEx](../../text/4C/IoInitializeRemoveLockEx_function_004C8F10.md) (`PAGE` → `.text`)
  - `0x0075A0BF` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0075A0E4` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0075A250` → [KeInitializeEvent](../../text/40/KeInitializeEvent_function_0040DD10.md) (`PAGE` → `.text`)
  - `0x0075A501` → [PopFxActivateComponent](../../text/2D/PopFxActivateComponent_function_002D9DBC.md) (`PAGE` → `.text`)
  - `0x0075A528` → [IoAllocateIrp](../../text/20/IoAllocateIrp_function_002065D0.md) (`PAGE` → `.text`)
  - `0x0075A548` → [PopFxRegisterDeviceWithPep](../../text/4C/PopFxRegisterDeviceWithPep_function_004CF794.md) (`PAGE` → `.text`)
  - `0x0075A55F` → [PopFxBugCheck](../../text/2B/PopFxBugCheck_function_002BFC6C.md) (`PAGE` → `.text`)
  - `0x0075A568` → [PopPlRegisterDevice](../../text/4B/PopPlRegisterDevice_function_004B820C.md) (`PAGE` → `.text`)
  - `0x0075A5EE` → [PopPlRegisterComponent](../../text/4A/PopPlRegisterComponent_function_004AA1FC.md) (`PAGE` → `.text`)
  - `0x0075A624` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0075A63F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0075A651` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0075A662` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0075A674` → [PopFxReleaseAcpiRefDevice](../../text/5D/PopFxReleaseAcpiRefDevice_function_005D3444.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00759E20  48 8B C4                        mov rax, rsp
00759E23  48 89 58 18                     mov qword ptr [rax + 0x18], rbx
00759E27  4C 89 48 20                     mov qword ptr [rax + 0x20], r9
00759E2B  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
00759E2F  48 89 48 08                     mov qword ptr [rax + 8], rcx
00759E33  55                              push rbp
00759E34  56                              push rsi
00759E35  57                              push rdi
00759E36  41 54                           push r12
00759E38  41 55                           push r13
00759E3A  41 56                           push r14
00759E3C  41 57                           push r15
00759E3E  48 8D 68 C1                     lea rbp, [rax - 0x3f]
00759E42  48 81 EC D0 00 00 00            sub rsp, 0xd0
00759E49  44 8B 75 67                     mov r14d, dword ptr [rbp + 0x67]
00759E4D  33 C0                           xor eax, eax
00759E4F  41 83 CD FF                     or r13d, 0xffffffff
00759E53  48 89 45 87                     mov qword ptr [rbp - 0x79], rax
00759E57  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00759E5C  41 8B DD                        mov ebx, r13d
00759E5F  89 5C 24 30                     mov dword ptr [rsp + 0x30], ebx
00759E63  49 8B F9                        mov rdi, r9
00759E66  4D 8B E0                        mov r12, r8
00759E69  8B F0                           mov esi, eax
00759E6B  45 85 F6                        test r14d, r14d
00759E6E  75 0A                           jne 0x140759e7a
00759E70  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00759E75  E9 FF 07 00 00                  jmp 0x14075a679
00759E7A  8A 45 7F                        mov al, byte ptr [rbp + 0x7f]
00759E7D  24 18                           and al, 0x18
00759E7F  3C 18                           cmp al, 0x18
00759E81  74 ED                           je 0x140759e70
00759E83  4B 8D 14 76                     lea rdx, [r14 + r14*2]
00759E87  B9 00 01 00 00                  mov ecx, 0x100
00759E8C  48 C1 E2 02                     shl rdx, 2
00759E90  41 B8 50 46 58 4D               mov r8d, 0x4d584650
00759E96  E8 55 82 42 00                  call 0x140b820f0
00759E9B  45 33 C9                        xor r9d, r9d
00759E9E  48 89 45 97                     mov qword ptr [rbp - 0x69], rax
00759EA2  4C 8B F8                        mov r15, rax
00759EA5  48 85 C0                        test rax, rax
00759EA8  75 0A                           jne 0x140759eb4
00759EAA  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00759EAF  E9 C5 07 00 00                  jmp 0x14075a679
00759EB4  45 8B D1                        mov r10d, r9d
00759EB7  44 89 4D 67                     mov dword ptr [rbp + 0x67], r9d
00759EBB  45 8B D9                        mov r11d, r9d
00759EBE  45 8B C1                        mov r8d, r9d
00759EC1  45 3B C6                        cmp r8d, r14d
00759EC4  0F 83 A6 00 00 00               jae 0x140759f70
00759ECA  41 8B C0                        mov eax, r8d
00759ECD  48 6B D0 38                     imul rdx, rax, 0x38
00759ED1  48 03 D7                        add rdx, rdi
00759ED4  8B 42 1C                        mov eax, dword ptr [rdx + 0x1c]
00759ED7  85 C0                           test eax, eax
00759ED9  0F 84 87 00 00 00               je 0x140759f66
00759EDF  83 F8 01                        cmp eax, 1
00759EE2  76 19                           jbe 0x140759efd
00759EE4  4D 39 0C 24                     cmp qword ptr [r12], r9
00759EE8  74 7C                           je 0x140759f66
00759EEA  4D 39 4C 24 08                  cmp qword ptr [r12 + 8], r9
00759EEF  74 75                           je 0x140759f66
00759EF1  4D 39 4C 24 10                  cmp qword ptr [r12 + 0x10], r9
00759EF6  74 6E                           je 0x140759f66
00759EF8  39 42 18                        cmp dword ptr [rdx + 0x18], eax
00759EFB  73 69                           jae 0x140759f66
00759EFD  42 8D 0C 10                     lea ecx, [rax + r10]
00759F01  41 3B CA                        cmp ecx, r10d
00759F04  72 60                           jb 0x140759f66
00759F06  8B 42 28                        mov eax, dword ptr [rdx + 0x28]
00759F09  44 8B D1                        mov r10d, ecx
00759F0C  85 C0                           test eax, eax
00759F0E  74 3C                           je 0x140759f4c
00759F10  41 3B C6                        cmp eax, r14d
00759F13  73 51                           jae 0x140759f66
00759F15  42 8D 0C 18                     lea ecx, [rax + r11]
00759F19  41 3B CB                        cmp ecx, r11d
00759F1C  72 48                           jb 0x140759f66
00759F1E  89 4D 67                        mov dword ptr [rbp + 0x67], ecx
00759F21  44 3B 4A 28                     cmp r9d, dword ptr [rdx + 0x28]
00759F25  73 1E                           jae 0x140759f45
00759F27  48 8B 42 30                     mov rax, qword ptr [rdx + 0x30]
00759F2B  41 8B C9                        mov ecx, r9d
00759F2E  44 8B 1C 88                     mov r11d, dword ptr [rax + rcx*4]
00759F32  45 3B DE                        cmp r11d, r14d
00759F35  73 2F                           jae 0x140759f66
00759F37  4B 8D 0C 5B                     lea rcx, [r11 + r11*2]
00759F3B  41 FF 44 8F 08                  inc dword ptr [r15 + rcx*4 + 8]
00759F40  41 FF C1                        inc r9d
00759F43  EB DC                           jmp 0x140759f21
00759F45  44 8B 5D 67                     mov r11d, dword ptr [rbp + 0x67]
00759F49  45 33 C9                        xor r9d, r9d
00759F4C  F6 42 10 04                     test byte ptr [rdx + 0x10], 4
00759F50  74 0C                           je 0x140759f5e
00759F52  41 3B DD                        cmp ebx, r13d
00759F55  75 0F                           jne 0x140759f66
00759F57  41 8B D8                        mov ebx, r8d
00759F5A  89 5C 24 30                     mov dword ptr [rsp + 0x30], ebx
00759F5E  41 FF C0                        inc r8d
00759F61  E9 5B FF FF FF                  jmp 0x140759ec1
00759F66  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00759F6B  E9 EA 06 00 00                  jmp 0x14075a65a
00759F70  49 69 C6 D8 01 00 00            imul rax, r14, 0x1d8
00759F77  4A 8D 1C F5 00 00 00 00         lea rbx, [r14*8]
00759F7F  4C 89 4D AF                     mov qword ptr [rbp - 0x51], r9
00759F83  48 89 5D DF                     mov qword ptr [rbp - 0x21], rbx
00759F87  48 03 D8                        add rbx, rax
00759F8A  41 8B C2                        mov eax, r10d
00759F8D  48 89 5D 9F                     mov qword ptr [rbp - 0x61], rbx
00759F91  4C 89 4C 24 48                  mov qword ptr [rsp + 0x48], r9
00759F96  4C 89 4D B7                     mov qword ptr [rbp - 0x49], r9
00759F9A  48 8D 0C 40                     lea rcx, [rax + rax*2]
00759F9E  4C 89 4C 24 40                  mov qword ptr [rsp + 0x40], r9
00759FA3  8A 45 77                        mov al, byte ptr [rbp + 0x77]
00759FA6  48 8D 14 CD 00 00 00 00         lea rdx, [rcx*8]
00759FAE  48 8D 0C 1A                     lea rcx, [rdx + rbx]
00759FB2  84 C0                           test al, al
00759FB4  4C 8D A9 38 01 00 00            lea r13, [rcx + 0x138]
00759FBB  4C 0F 4E E9                     cmovle r13, rcx
00759FBF  49 0F 4E C9                     cmovle rcx, r9
00759FC3  48 89 4D F7                     mov qword ptr [rbp - 9], rcx
00759FC7  45 85 DB                        test r11d, r11d
00759FCA  74 1A                           je 0x140759fe6
00759FCC  41 8B C3                        mov eax, r11d
00759FCF  48 C1 E0 03                     shl rax, 3
00759FD3  4C 89 6C 24 48                  mov qword ptr [rsp + 0x48], r13
00759FD8  4A 8D 0C 28                     lea rcx, [rax + r13]
00759FDC  48 89 4C 24 40                  mov qword ptr [rsp + 0x40], rcx
00759FE1  4D 8D 6C 45 00                  lea r13, [r13 + rax*2]
00759FE6  48 8B 7D 4F                     mov rdi, qword ptr [rbp + 0x4f]
00759FEA  41 8B C6                        mov eax, r14d
00759FED  0F AF 05 D8 13 6B 00            imul eax, dword ptr [rip + 0x6b13d8]
00759FF4  89 45 A7                        mov dword ptr [rbp - 0x59], eax
00759FF7  48 8D 0C 40                     lea rcx, [rax + rax*2]
00759FFB  48 8D 04 CD 00 00 00 00         lea rax, [rcx*8]
0075A003  49 03 C5                        add rax, r13
0075A006  4B 8D 0C B6                     lea rcx, [r14 + r14*4]
0075A00A  48 89 45 BF                     mov qword ptr [rbp - 0x41], rax
0075A00E  42 8D 04 F5 00 00 00 00         lea eax, [r14*8]
0075A016  4C 63 C0                        movsxd r8, eax
0075A019  49 83 C0 10                     add r8, 0x10
0075A01D  4C 89 45 E7                     mov qword ptr [rbp - 0x19], r8
0075A021  49 8D 34 C8                     lea rsi, [r8 + rcx*8]
0075A025  48 8B CF                        mov rcx, rdi
0075A028  48 89 75 C7                     mov qword ptr [rbp - 0x39], rsi
0075A02C  48 03 F2                        add rsi, rdx
0075A02F  48 8D 55 87                     lea rdx, [rbp - 0x79]
0075A033  48 89 75 CF                     mov qword ptr [rbp - 0x31], rsi
0075A037  E8 F4 BB D6 FF                  call 0x1404c5c30
0075A03C  85 C0                           test eax, eax
0075A03E  78 18                           js 0x14075a058
0075A040  48 8B 45 87                     mov rax, qword ptr [rbp - 0x79]
0075A044  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0075A049  F0 83 88 E8 00 00 00 01         lock or dword ptr [rax + 0xe8], 1
0075A051  48 8B 7C 24 38                  mov rdi, qword ptr [rsp + 0x38]
0075A056  EB 38                           jmp 0x14075a090
0075A058  3D 56 00 00 C0                  cmp eax, 0xc0000056
0075A05D  75 0C                           jne 0x14075a06b
0075A05F  8D 58 4D                        lea ebx, [rax + 0x4d]
0075A062  48 8B 75 87                     mov rsi, qword ptr [rbp - 0x79]
0075A066  E9 EF 05 00 00                  jmp 0x14075a65a
0075A06B  48 8D 44 24 38                  lea rax, [rsp + 0x38]
0075A070  45 33 C9                        xor r9d, r9d
0075A073  48 8B CF                        mov rcx, rdi
0075A076  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0075A07B  E8 A4 83 E7 FF                  call 0x1405d2424
0075A080  48 8B 7C 24 38                  mov rdi, qword ptr [rsp + 0x38]
0075A085  8B D8                           mov ebx, eax
0075A087  48 85 FF                        test rdi, rdi
0075A08A  74 D6                           je 0x14075a062
0075A08C  48 8B 5D 9F                     mov rbx, qword ptr [rbp - 0x61]
0075A090  41 BF 50 46 58 4D               mov r15d, 0x4d584650
0075A096  C7 44 24 20 20 00 00 00         mov dword ptr [rsp + 0x20], 0x20
0075A09E  41 8B D7                        mov edx, r15d
0075A0A1  48 8D 8F F0 00 00 00            lea rcx, [rdi + 0xf0]
0075A0A8  45 33 C9                        xor r9d, r9d
0075A0AB  45 33 C0                        xor r8d, r8d
0075A0AE  E8 5D EE D6 FF                  call 0x1404c8f10
0075A0B3  48 8B 55 BF                     mov rdx, qword ptr [rbp - 0x41]
0075A0B7  45 8B C7                        mov r8d, r15d
0075A0BA  B9 40 00 00 00                  mov ecx, 0x40
0075A0BF  E8 2C 80 42 00                  call 0x140b820f0
0075A0C4  4C 8B F8                        mov r15, rax
0075A0C7  48 85 C0                        test rax, rax
0075A0CA  75 0A                           jne 0x14075a0d6
0075A0CC  BB 9A 00 00 C0                  mov ebx, 0xc000009a
0075A0D1  E9 53 05 00 00                  jmp 0x14075a629
0075A0D6  41 B8 50 46 58 4D               mov r8d, 0x4d584650
0075A0DC  48 8B D6                        mov rdx, rsi
0075A0DF  B9 40 00 00 00                  mov ecx, 0x40
0075A0E4  E8 07 80 42 00                  call 0x140b820f0
0075A0E9  45 33 D2                        xor r10d, r10d
0075A0EC  48 8B F0                        mov rsi, rax
0075A0EF  48 85 C0                        test rax, rax
0075A0F2  74 D8                           je 0x14075a0cc
0075A0F4  48 8B 45 6F                     mov rax, qword ptr [rbp + 0x6f]
0075A0F8  41 0F 28 04 24                  movaps xmm0, xmmword ptr [r12]
0075A0FD  41 0F 28 4C 24 10               movaps xmm1, xmmword ptr [r12 + 0x10]
0075A103  4C 8B 4D DF                     mov r9, qword ptr [rbp - 0x21]
0075A107  44 89 B7 64 03 00 00            mov dword ptr [rdi + 0x364], r14d
0075A10E  4D 03 CF                        add r9, r15
0075A111  4C 89 BF 68 03 00 00            mov qword ptr [rdi + 0x368], r15
0075A118  0F 11 47 70                     movups xmmword ptr [rdi + 0x70], xmm0
0075A11C  4C 89 4D D7                     mov qword ptr [rbp - 0x29], r9
0075A120  41 0F 28 44 24 20               movaps xmm0, xmmword ptr [r12 + 0x20]
0075A126  0F 11 8F 80 00 00 00            movups xmmword ptr [rdi + 0x80], xmm1
0075A12D  41 0F 28 4C 24 30               movaps xmm1, xmmword ptr [r12 + 0x30]
0075A133  0F 11 87 90 00 00 00            movups xmmword ptr [rdi + 0x90], xmm0
0075A13A  41 0F 28 44 24 40               movaps xmm0, xmmword ptr [r12 + 0x40]
0075A140  0F 11 8F A0 00 00 00            movups xmmword ptr [rdi + 0xa0], xmm1
0075A147  0F 11 87 B0 00 00 00            movups xmmword ptr [rdi + 0xb0], xmm0
0075A14E  48 89 87 C0 00 00 00            mov qword ptr [rdi + 0xc0], rax
0075A155  8B 44 24 30                     mov eax, dword ptr [rsp + 0x30]
0075A159  89 87 B8 03 00 00               mov dword ptr [rdi + 0x3b8], eax
0075A15F  48 8D 87 18 05 00 00            lea rax, [rdi + 0x518]
0075A166  4C 89 97 80 02 00 00            mov qword ptr [rdi + 0x280], r10
0075A16D  48 C7 87 8C 02 00 00 05 00 00 00  mov qword ptr [rdi + 0x28c], 5
0075A178  48 89 40 08                     mov qword ptr [rax + 8], rax
0075A17C  48 89 00                        mov qword ptr [rax], rax
0075A17F  48 8B 45 7F                     mov rax, qword ptr [rbp + 0x7f]
0075A183  48 89 06                        mov qword ptr [rsi], rax
0075A186  4A 8D 04 3B                     lea rax, [rbx + r15]
0075A18A  48 89 45 8F                     mov qword ptr [rbp - 0x71], rax
0075A18E  44 89 76 08                     mov dword ptr [rsi + 8], r14d
0075A192  44 39 55 67                     cmp dword ptr [rbp + 0x67], r10d
0075A196  76 18                           jbe 0x14075a1b0
0075A198  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
0075A19D  49 03 C7                        add rax, r15
0075A1A0  48 89 45 AF                     mov qword ptr [rbp - 0x51], rax
0075A1A4  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
0075A1A9  49 03 C7                        add rax, r15
0075A1AC  48 89 45 B7                     mov qword ptr [rbp - 0x49], rax
0075A1B0  48 8B 45 E7                     mov rax, qword ptr [rbp - 0x19]
0075A1B4  49 8D 59 30                     lea rbx, [r9 + 0x30]
0075A1B8  48 03 C6                        add rax, rsi
0075A1BB  49 C7 C0 D0 FF FF FF            mov r8, 0xffffffffffffffd0
0075A1C2  48 89 45 9F                     mov qword ptr [rbp - 0x61], rax
0075A1C6  4D 2B C7                        sub r8, r15
0075A1C9  48 8B 45 C7                     mov rax, qword ptr [rbp - 0x39]
0075A1CD  48 C7 C1 F0 FF FF FF            mov rcx, 0xfffffffffffffff0
0075A1D4  48 03 C6                        add rax, rsi
0075A1D7  4C 89 45 EF                     mov qword ptr [rbp - 0x11], r8
0075A1DB  48 2B CE                        sub rcx, rsi
0075A1DE  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
0075A1E3  48 89 4C 24 48                  mov qword ptr [rsp + 0x48], rcx
0075A1E8  41 8B D2                        mov edx, r10d
0075A1EB  89 54 24 30                     mov dword ptr [rsp + 0x30], edx
0075A1EF  41 3B D6                        cmp edx, r14d
0075A1F2  0F 83 5D 02 00 00               jae 0x14075a455
0075A1F8  48 8B 87 68 03 00 00            mov rax, qword ptr [rdi + 0x368]
0075A1FF  8B CA                           mov ecx, edx
0075A201  4C 6B E1 38                     imul r12, rcx, 0x38
0075A205  4C 89 0C C8                     mov qword ptr [rax + rcx*8], r9
0075A209  49 8D 0C 18                     lea rcx, [r8 + rbx]
0075A20D  48 8B 45 BF                     mov rax, qword ptr [rbp - 0x41]
0075A211  4C 03 65 5F                     add r12, qword ptr [rbp + 0x5f]
0075A215  48 05 28 FE FF FF               add rax, -0x1d8
0075A21B  48 3B C8                        cmp rcx, rax
0075A21E  0F 87 27 02 00 00               ja 0x14075a44b
0075A224  41 0F 10 04 24                  movups xmm0, xmmword ptr [r12]
0075A229  89 53 E0                        mov dword ptr [rbx - 0x20], edx
0075A22C  48 8D 05 ED 61 B6 FF            lea rax, [rip - 0x499e13]
0075A233  48 89 7B 20                     mov qword ptr [rbx + 0x20], rdi
0075A237  48 8D 4B 38                     lea rcx, [rbx + 0x38]
0075A23B  F3 41 0F 7F 01                  movdqu xmmword ptr [r9], xmm0
0075A240  41 B0 01                        mov r8b, 1
0075A243  48 89 43 F8                     mov qword ptr [rbx - 8], rax
0075A247  33 D2                           xor edx, edx
0075A249  4C 89 0B                        mov qword ptr [rbx], r9
0075A24C  4C 89 53 E8                     mov qword ptr [rbx - 0x18], r10
0075A250  E8 BB 3A CB FF                  call 0x14040dd10
0075A255  4C 8B 4D 8F                     mov r9, qword ptr [rbp - 0x71]
0075A259  45 33 DB                        xor r11d, r11d
0075A25C  4C 89 5B 50                     mov qword ptr [rbx + 0x50], r11
0075A260  41 8B 44 24 1C                  mov eax, dword ptr [r12 + 0x1c]
0075A265  89 43 6C                        mov dword ptr [rbx + 0x6c], eax
0075A268  4C 89 4B 70                     mov qword ptr [rbx + 0x70], r9
0075A26C  41 8B 44 24 18                  mov eax, dword ptr [r12 + 0x18]
0075A271  83 8B A4 00 00 00 FF            or dword ptr [rbx + 0xa4], 0xffffffff
0075A278  89 43 78                        mov dword ptr [rbx + 0x78], eax
0075A27B  48 8D 83 98 01 00 00            lea rax, [rbx + 0x198]
0075A282  4C 89 9B 98 00 00 00            mov qword ptr [rbx + 0x98], r11
0075A289  44 89 9B A8 00 00 00            mov dword ptr [rbx + 0xa8], r11d
0075A290  48 89 83 A0 01 00 00            mov qword ptr [rbx + 0x1a0], rax
0075A297  48 89 00                        mov qword ptr [rax], rax
0075A29A  48 8D 83 88 01 00 00            lea rax, [rbx + 0x188]
0075A2A1  48 89 83 90 01 00 00            mov qword ptr [rbx + 0x190], rax
0075A2A8  48 89 00                        mov qword ptr [rax], rax
0075A2AB  41 8B 44 24 28                  mov eax, dword ptr [r12 + 0x28]
0075A2B0  85 C0                           test eax, eax
0075A2B2  74 2D                           je 0x14075a2e1
0075A2B4  4C 8B 45 AF                     mov r8, qword ptr [rbp - 0x51]
0075A2B8  41 8B D3                        mov edx, r11d
0075A2BB  4C 89 83 80 00 00 00            mov qword ptr [rbx + 0x80], r8
0075A2C2  89 43 7C                        mov dword ptr [rbx + 0x7c], eax
0075A2C5  49 8B 44 24 30                  mov rax, qword ptr [r12 + 0x30]
0075A2CA  8B CA                           mov ecx, edx
0075A2CC  FF C2                           inc edx
0075A2CE  8B 0C 88                        mov ecx, dword ptr [rax + rcx*4]
0075A2D1  41 89 08                        mov dword ptr [r8], ecx
0075A2D4  49 83 C0 08                     add r8, 8
0075A2D8  3B 53 7C                        cmp edx, dword ptr [rbx + 0x7c]
0075A2DB  72 E8                           jb 0x14075a2c5
0075A2DD  4C 89 45 AF                     mov qword ptr [rbp - 0x51], r8
0075A2E1  8B 54 24 30                     mov edx, dword ptr [rsp + 0x30]
0075A2E5  4C 8B 55 97                     mov r10, qword ptr [rbp - 0x69]
0075A2E9  48 8D 0C 52                     lea rcx, [rdx + rdx*2]
0075A2ED  45 39 5C 8A 08                  cmp dword ptr [r10 + rcx*4 + 8], r11d
0075A2F2  76 18                           jbe 0x14075a30c
0075A2F4  4C 8B 45 B7                     mov r8, qword ptr [rbp - 0x49]
0075A2F8  4C 89 83 90 00 00 00            mov qword ptr [rbx + 0x90], r8
0075A2FF  41 8B 44 8A 08                  mov eax, dword ptr [r10 + rcx*4 + 8]
0075A304  4D 8D 04 C0                     lea r8, [r8 + rax*8]
0075A308  4C 89 45 B7                     mov qword ptr [rbp - 0x49], r8
0075A30C  4C 8B 45 9F                     mov r8, qword ptr [rbp - 0x61]
0075A310  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
0075A315  48 8B 45 CF                     mov rax, qword ptr [rbp - 0x31]
0075A319  48 83 C1 10                     add rcx, 0x10
0075A31D  49 03 C8                        add rcx, r8
0075A320  4C 89 44 D6 10                  mov qword ptr [rsi + rdx*8 + 0x10], r8
0075A325  48 83 C0 D8                     add rax, -0x28
0075A329  48 3B C8                        cmp rcx, rax
0075A32C  0F 87 19 01 00 00               ja 0x14075a44b
0075A332  41 0F 10 04 24                  movups xmm0, xmmword ptr [r12]
0075A337  48 C7 C1 F0 FF FF FF            mov rcx, 0xfffffffffffffff0
0075A33E  F3 41 0F 7F 00                  movdqu xmmword ptr [r8], xmm0
0075A343  49 8B 44 24 10                  mov rax, qword ptr [r12 + 0x10]
0075A348  49 89 40 10                     mov qword ptr [r8 + 0x10], rax
0075A34C  41 8B 44 24 1C                  mov eax, dword ptr [r12 + 0x1c]
0075A351  41 89 40 1C                     mov dword ptr [r8 + 0x1c], eax
0075A355  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
0075A35A  49 89 40 20                     mov qword ptr [r8 + 0x20], rax
0075A35E  41 8B 44 24 18                  mov eax, dword ptr [r12 + 0x18]
0075A363  41 89 40 18                     mov dword ptr [r8 + 0x18], eax
0075A367  48 8B C1                        mov rax, rcx
0075A36A  49 2B C7                        sub rax, r15
0075A36D  48 2B CE                        sub rcx, rsi
0075A370  48 89 45 C7                     mov qword ptr [rbp - 0x39], rax
0075A374  48 89 4C 24 48                  mov qword ptr [rsp + 0x48], rcx
0075A379  44 3B 5B 6C                     cmp r11d, dword ptr [rbx + 0x6c]
0075A37D  0F 83 9C 00 00 00               jae 0x14075a41f
0075A383  48 8D 48 10                     lea rcx, [rax + 0x10]
0075A387  48 8B 45 BF                     mov rax, qword ptr [rbp - 0x41]
0075A38B  48 83 C0 E8                     add rax, -0x18
0075A38F  49 03 C9                        add rcx, r9
0075A392  48 3B C8                        cmp rcx, rax
0075A395  0F 87 B0 00 00 00               ja 0x14075a44b
0075A39B  4D 8B 54 24 20                  mov r10, qword ptr [r12 + 0x20]
0075A3A0  48 8B 4D 8F                     mov rcx, qword ptr [rbp - 0x71]
0075A3A4  41 8B C3                        mov eax, r11d
0075A3A7  4C 8D 0C 40                     lea r9, [rax + rax*2]
0075A3AB  43 8B 44 CA 10                  mov eax, dword ptr [r10 + r9*8 + 0x10]
0075A3B0  89 41 10                        mov dword ptr [rcx + 0x10], eax
0075A3B3  4B 8B 04 CA                     mov rax, qword ptr [r10 + r9*8]
0075A3B7  48 89 01                        mov qword ptr [rcx], rax
0075A3BA  4B 8B 44 CA 08                  mov rax, qword ptr [r10 + r9*8 + 8]
0075A3BF  48 89 41 08                     mov qword ptr [rcx + 8], rax
0075A3C3  48 83 C1 18                     add rcx, 0x18
0075A3C7  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
0075A3CC  48 83 C0 10                     add rax, 0x10
0075A3D0  48 89 4D 8F                     mov qword ptr [rbp - 0x71], rcx
0075A3D4  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
0075A3D9  48 03 C8                        add rcx, rax
0075A3DC  48 8B 45 CF                     mov rax, qword ptr [rbp - 0x31]
0075A3E0  48 83 C0 E8                     add rax, -0x18
0075A3E4  48 3B C8                        cmp rcx, rax
0075A3E7  77 62                           ja 0x14075a44b
0075A3E9  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
0075A3EE  43 8B 44 CA 10                  mov eax, dword ptr [r10 + r9*8 + 0x10]
0075A3F3  89 41 10                        mov dword ptr [rcx + 0x10], eax
0075A3F6  4B 8B 04 CA                     mov rax, qword ptr [r10 + r9*8]
0075A3FA  48 89 01                        mov qword ptr [rcx], rax
0075A3FD  4B 8B 44 CA 08                  mov rax, qword ptr [r10 + r9*8 + 8]
0075A402  4C 8B 4D 8F                     mov r9, qword ptr [rbp - 0x71]
0075A406  48 89 41 08                     mov qword ptr [rcx + 8], rax
0075A40A  48 83 C1 18                     add rcx, 0x18
0075A40E  48 8B 45 C7                     mov rax, qword ptr [rbp - 0x39]
0075A412  41 FF C3                        inc r11d
0075A415  48 89 4C 24 40                  mov qword ptr [rsp + 0x40], rcx
0075A41A  E9 5A FF FF FF                  jmp 0x14075a379
0075A41F  4C 8B 4D D7                     mov r9, qword ptr [rbp - 0x29]
0075A423  49 83 C0 28                     add r8, 0x28
0075A427  49 81 C1 D8 01 00 00            add r9, 0x1d8
0075A42E  4C 89 45 9F                     mov qword ptr [rbp - 0x61], r8
0075A432  4C 8B 45 EF                     mov r8, qword ptr [rbp - 0x11]
0075A436  48 81 C3 D8 01 00 00            add rbx, 0x1d8
0075A43D  FF C2                           inc edx
0075A43F  4C 89 4D D7                     mov qword ptr [rbp - 0x29], r9
0075A443  45 33 D2                        xor r10d, r10d
0075A446  E9 A0 FD FF FF                  jmp 0x14075a1eb
0075A44B  BB 9A 00 00 C0                  mov ebx, 0xc000009a
0075A450  E9 C7 01 00 00                  jmp 0x14075a61c
0075A455  8B 45 A7                        mov eax, dword ptr [rbp - 0x59]
0075A458  89 87 70 03 00 00               mov dword ptr [rdi + 0x370], eax
0075A45E  4B 8D 04 2F                     lea rax, [r15 + r13]
0075A462  45 33 ED                        xor r13d, r13d
0075A465  48 89 87 78 03 00 00            mov qword ptr [rdi + 0x378], rax
0075A46C  44 39 6D 67                     cmp dword ptr [rbp + 0x67], r13d
0075A470  76 19                           jbe 0x14075a48b
0075A472  48 8B 4D 97                     mov rcx, qword ptr [rbp - 0x69]
0075A476  45 8B C6                        mov r8d, r14d
0075A479  48 8B D7                        mov rdx, rdi
0075A47C  E8 63 03 00 00                  call 0x14075a7e4
0075A481  8B D8                           mov ebx, eax
0075A483  85 C0                           test eax, eax
0075A485  0F 88 91 01 00 00               js 0x14075a61c
0075A48B  41 8B DD                        mov ebx, r13d
0075A48E  45 85 F6                        test r14d, r14d
0075A491  74 7E                           je 0x14075a511
0075A493  4D 8B E5                        mov r12, r13
0075A496  48 8B 87 68 03 00 00            mov rax, qword ptr [rdi + 0x368]
0075A49D  45 8B CD                        mov r9d, r13d
0075A4A0  4D 8B 14 04                     mov r10, qword ptr [r12 + rax]
0075A4A4  45 39 AA AC 00 00 00            cmp dword ptr [r10 + 0xac], r13d
0075A4AB  76 48                           jbe 0x14075a4f5
0075A4AD  49 8B 82 B0 00 00 00            mov rax, qword ptr [r10 + 0xb0]
0075A4B4  41 8B C9                        mov ecx, r9d
0075A4B7  8B 14 C8                        mov edx, dword ptr [rax + rcx*8]
0075A4BA  48 8B 87 68 03 00 00            mov rax, qword ptr [rdi + 0x368]
0075A4C1  4C 8B 04 D0                     mov r8, qword ptr [rax + rdx*8]
0075A4C5  41 8B 88 BC 00 00 00            mov ecx, dword ptr [r8 + 0xbc]
0075A4CC  49 8B 80 C0 00 00 00            mov rax, qword ptr [r8 + 0xc0]
0075A4D3  89 1C C8                        mov dword ptr [rax + rcx*8], ebx
0075A4D6  49 8B 80 C0 00 00 00            mov rax, qword ptr [r8 + 0xc0]
0075A4DD  44 89 4C C8 04                  mov dword ptr [rax + rcx*8 + 4], r9d
0075A4E2  41 FF C1                        inc r9d
0075A4E5  41 FF 80 BC 00 00 00            inc dword ptr [r8 + 0xbc]
0075A4EC  45 3B 8A AC 00 00 00            cmp r9d, dword ptr [r10 + 0xac]
0075A4F3  72 B8                           jb 0x14075a4ad
0075A4F5  41 B1 01                        mov r9b, 1
0075A4F8  45 33 C0                        xor r8d, r8d
0075A4FB  49 8B D2                        mov rdx, r10
0075A4FE  48 8B CF                        mov rcx, rdi
0075A501  E8 B6 F8 B7 FF                  call 0x1402d9dbc
0075A506  FF C3                           inc ebx
0075A508  49 83 C4 08                     add r12, 8
0075A50C  41 3B DE                        cmp ebx, r14d
0075A50F  72 85                           jb 0x14075a496
0075A511  8A 4D 77                        mov cl, byte ptr [rbp + 0x77]
0075A514  84 C9                           test cl, cl
0075A516  7E 22                           jle 0x14075a53a
0075A518  48 8B 45 F7                     mov rax, qword ptr [rbp - 9]
0075A51C  80 C1 02                        add cl, 2
0075A51F  49 03 C7                        add rax, r15
0075A522  33 D2                           xor edx, edx
0075A524  48 89 47 18                     mov qword ptr [rdi + 0x18], rax
0075A528  E8 A3 C0 AA FF                  call 0x1402065d0
0075A52D  48 89 47 10                     mov qword ptr [rdi + 0x10], rax
0075A531  48 85 C0                        test rax, rax
0075A534  0F 84 11 FF FF FF               je 0x14075a44b
0075A53A  48 8B 55 4F                     mov rdx, qword ptr [rbp + 0x4f]
0075A53E  4C 8B CE                        mov r9, rsi
0075A541  48 8B 4D 47                     mov rcx, qword ptr [rbp + 0x47]
0075A545  4C 8B C7                        mov r8, rdi
0075A548  E8 47 52 D7 FF                  call 0x1404cf794
0075A54D  84 C0                           test al, al
0075A54F  75 14                           jne 0x14075a565
0075A551  45 33 C9                        xor r9d, r9d
0075A554  4C 8B C6                        mov r8, rsi
0075A557  48 8B D7                        mov rdx, rdi
0075A55A  B9 01 06 00 00                  mov ecx, 0x601
0075A55F  E8 08 57 B6 FF                  call 0x1402bfc6c
0075A564  CC                              int3
0075A565  48 8B CF                        mov rcx, rdi
0075A568  E8 9F DC D5 FF                  call 0x1404b820c
0075A56D  44 39 2D D8 D2 70 00            cmp dword ptr [rip + 0x70d2d8], r13d
0075A574  48 8B 06                        mov rax, qword ptr [rsi]
0075A577  0F 95 C1                        setne cl
0075A57A  A8 10                           test al, 0x10
0075A57C  75 18                           jne 0x14075a596
0075A57E  A8 08                           test al, 8
0075A580  75 04                           jne 0x14075a586
0075A582  84 C9                           test cl, cl
0075A584  74 10                           je 0x14075a596
0075A586  F0 81 8F 60 03 00 00 80 00 00 00  lock or dword ptr [rdi + 0x360], 0x80
0075A591  48 8B 7C 24 38                  mov rdi, qword ptr [rsp + 0x38]
0075A596  F6 06 20                        test byte ptr [rsi], 0x20
0075A599  74 10                           je 0x14075a5ab
0075A59B  F0 81 8F 60 03 00 00 00 10 00 00  lock or dword ptr [rdi + 0x360], 0x1000
0075A5A6  48 8B 7C 24 38                  mov rdi, qword ptr [rsp + 0x38]
0075A5AB  F6 06 40                        test byte ptr [rsi], 0x40
0075A5AE  74 0D                           je 0x14075a5bd
0075A5B0  F0 83 8F 60 03 00 00 01         lock or dword ptr [rdi + 0x360], 1
0075A5B8  48 8B 7C 24 38                  mov rdi, qword ptr [rsp + 0x38]
0075A5BD  48 8B 5D DF                     mov rbx, qword ptr [rbp - 0x21]
0075A5C1  49 03 DF                        add rbx, r15
0075A5C4  45 85 F6                        test r14d, r14d
0075A5C7  74 40                           je 0x14075a609
0075A5C9  48 8B 7D E7                     mov rdi, qword ptr [rbp - 0x19]
0075A5CD  48 83 C7 1C                     add rdi, 0x1c
0075A5D1  48 03 FE                        add rdi, rsi
0075A5D4  F6 47 F4 02                     test byte ptr [rdi - 0xc], 2
0075A5D8  74 09                           je 0x14075a5e3
0075A5DA  8B 43 5C                        mov eax, dword ptr [rbx + 0x5c]
0075A5DD  83 C8 02                        or eax, 2
0075A5E0  89 43 5C                        mov dword ptr [rbx + 0x5c], eax
0075A5E3  8B 07                           mov eax, dword ptr [rdi]
0075A5E5  48 8B CB                        mov rcx, rbx
0075A5E8  89 83 9C 00 00 00               mov dword ptr [rbx + 0x9c], eax
0075A5EE  E8 09 FC D4 FF                  call 0x1404aa1fc
0075A5F3  48 81 C3 D8 01 00 00            add rbx, 0x1d8
0075A5FA  48 83 C7 28                     add rdi, 0x28
0075A5FE  49 83 EE 01                     sub r14, 1
0075A602  75 D0                           jne 0x14075a5d4
0075A604  48 8B 7C 24 38                  mov rdi, qword ptr [rsp + 0x38]
0075A609  48 8B 85 87 00 00 00            mov rax, qword ptr [rbp + 0x87]
0075A610  4D 8B FD                        mov r15, r13
0075A613  41 8B DD                        mov ebx, r13d
0075A616  48 89 38                        mov qword ptr [rax], rdi
0075A619  49 8B FD                        mov rdi, r13
0075A61C  BA 50 46 58 4D                  mov edx, 0x4d584650
0075A621  48 8B CE                        mov rcx, rsi
0075A624  E8 47 82 42 00                  call 0x140b82870
0075A629  48 8B 75 87                     mov rsi, qword ptr [rbp - 0x79]
0075A62D  48 85 FF                        test rdi, rdi
0075A630  74 12                           je 0x14075a644
0075A632  48 85 F6                        test rsi, rsi
0075A635  75 0D                           jne 0x14075a644
0075A637  BA 50 46 58 4D                  mov edx, 0x4d584650
0075A63C  48 8B CF                        mov rcx, rdi
0075A63F  E8 2C 82 42 00                  call 0x140b82870
0075A644  4D 85 FF                        test r15, r15
0075A647  74 0D                           je 0x14075a656
0075A649  BA 50 46 58 4D                  mov edx, 0x4d584650
0075A64E  49 8B CF                        mov rcx, r15
0075A651  E8 1A 82 42 00                  call 0x140b82870
0075A656  4C 8B 7D 97                     mov r15, qword ptr [rbp - 0x69]
0075A65A  BA 50 46 58 4D                  mov edx, 0x4d584650
0075A65F  49 8B CF                        mov rcx, r15
0075A662  E8 09 82 42 00                  call 0x140b82870
0075A667  48 85 F6                        test rsi, rsi
0075A66A  74 0D                           je 0x14075a679
0075A66C  BA 50 6F 46 66                  mov edx, 0x66466f50
0075A671  48 8B CE                        mov rcx, rsi
0075A674  E8 CB 8D E7 FF                  call 0x1405d3444
0075A679  8B C3                           mov eax, ebx
0075A67B  48 8B 9C 24 20 01 00 00         mov rbx, qword ptr [rsp + 0x120]
0075A683  48 81 C4 D0 00 00 00            add rsp, 0xd0
0075A68A  41 5F                           pop r15
0075A68C  41 5E                           pop r14
0075A68E  41 5D                           pop r13
0075A690  41 5C                           pop r12
0075A692  5F                              pop rdi
0075A693  5E                              pop rsi
0075A694  5D                              pop rbp
0075A695  C3                              ret
0075A696  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopFxRegisterDeviceWorker(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned int v_stack_mD8;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_p18;

    *(unsigned __int64 *)(v_rsp + 24) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 32) = a4;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (208);
    result = 0;
    v_r13 = (unsigned int)((v_r13) | (0xFFFFFFFFULL));
    *(unsigned __int64 *)(v_rsp - 63 - 121) = 0;
    v_stack_mD0 = 0;
    v_stack_mD8 = (unsigned int)((unsigned int)((unsigned int)(v_r13)));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 63 + 103))) != 0) goto loc_00759E7A;
loc_00759E70:
    goto loc_0075A679;
loc_00759E7A:
    result = (unsigned __int8)((*(unsigned __int8 *)(v_rsp - 63 + 127)) & (24));
    if (((unsigned __int8)(result)) == 24) goto loc_00759E70;
    a2 = ((unsigned int)(*(unsigned int *)(v_rsp - 63 + 103)) + (unsigned int)(*(unsigned int *)(v_rsp - 63 + 103)) * 2) << (2);
    result = ExAllocatePool2(256, a2, (unsigned int)(0x4D584650ULL), a4);
    a4 = 0;
    *(unsigned __int64 *)(v_rsp - 63 - 105) = result;
    if (result != 0) goto loc_00759EB4;
    goto loc_0075A679;
loc_00759EB4:
    *(unsigned int *)(v_rsp - 63 + 103) = 0;
loc_00759EC1:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 63 + 103))))) goto loc_00759F70;
    a2 = (a2) * (0);
    a2 = (a2) + (0);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 28))) == 0) goto loc_00759F66;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 28)))) <= 1) goto loc_00759EFD;
    if ((*(unsigned __int64 *)(a3)) == 0) goto loc_00759F66;
    if ((*(unsigned __int64 *)(a3 + 8)) == 0) goto loc_00759F66;
    if ((*(unsigned __int64 *)(a3 + 16)) == 0) goto loc_00759F66;
    if ((*(unsigned int *)(a2 + 24)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 28))))) goto loc_00759F66;
loc_00759EFD:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 28)) + 0 * 1)) < 0) goto loc_00759F66;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 40))) == 0) goto loc_00759F4C;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 40)))) >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 63 + 103))))) goto loc_00759F66;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 40)) + 0 * 1)) < 0) goto loc_00759F66;
    *(unsigned int *)(v_rsp - 63 + 103) = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 40)) + 0 * 1);
loc_00759F21:
    if (0 >= (*(unsigned int *)(a2 + 40))) goto loc_00759F45;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 48) + 0 * 4)))) >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 63 + 103))))) goto loc_00759F66;
    a4 = (unsigned int)((a4) + 1);
    goto loc_00759F21;
loc_00759F45:
    a4 = 0;
loc_00759F4C:
    if (((*(unsigned __int8 *)(a2 + 16)) & (4)) == 0) goto loc_00759F5E;
    if (((unsigned int)((unsigned int)(0xC000009AULL))) != ((unsigned int)(v_r13))) goto loc_00759F66;
    v_stack_mD8 = 0;
loc_00759F5E:
    a3 = (unsigned int)((0) + 1);
    goto loc_00759EC1;
loc_00759F66:
    goto loc_0075A65A;
loc_00759F70:
    result = (*(unsigned __int64 *)(a2 + 48)) * ((unsigned int)(*(unsigned int *)(v_rsp - 63 + 103)));
    *(unsigned __int64 *)(v_rsp - 63 - 81) = 0;
    *(unsigned __int64 *)(v_rsp - 63 - 33) = (unsigned int)(*(unsigned int *)(v_rsp - 63 + 103)) * 8;
    v_rbx = ((unsigned int)(*(unsigned int *)(v_rsp - 63 + 103)) * 8) + (result);
    *(unsigned __int64 *)(v_rsp - 63 - 97) = v_rbx;
    v_stack_mC0 = 0;
    *(unsigned __int64 *)(v_rsp - 63 - 73) = 0;
    v_stack_mC8 = 0;
    v_r13 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 28)) + 0 * 1)))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 28)) + 0 * 1)))) * 2 * 8 + v_rbx * 1 + 312;
    if (condition_is_less_or_equal) { v_r13 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 28)) + 0 * 1)))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 28)) + 0 * 1)))) * 2 * 8 + v_rbx * 1; }
    a1 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 28)) + 0 * 1)))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 28)) + 0 * 1)))) * 2 * 8 + v_rbx * 1;
    if (condition_is_less_or_equal) { a1 = 0; }
    *(unsigned __int64 *)(v_rsp - 63 - 9) = a1;
    result = *(unsigned __int8 *)(v_rsp - 63 + 119);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 63 + 103))) != 0) {
        result = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 63 + 103)));
        result = (result) << (3);
        v_stack_mC0 = v_r13;
        a1 = result + v_r13 * 1;
        v_stack_mC8 = a1;
        v_r13 = v_r13 + result * 2;
    }
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 63 + 103))))) * (*(unsigned int *)(v_rip + 7017432)));
    *(unsigned int *)(v_rsp - 63 - 89) = (unsigned int)(result);
    result = (result + result * 2 * 8) + (v_r13);
    *(unsigned __int64 *)(v_rsp - 63 - 65) = result;
    a3 = ((int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 63 + 103)) * 8))) + (16);
    *(unsigned __int64 *)(v_rsp - 63 - 25) = a3;
    *(unsigned __int64 *)(v_rsp - 63 - 57) = a3 + (unsigned int)(*(unsigned int *)(v_rsp - 63 + 103)) + (unsigned int)(*(unsigned int *)(v_rsp - 63 + 103)) * 4 * 8;
    v_rsi = (a3 + (unsigned int)(*(unsigned int *)(v_rsp - 63 + 103)) + (unsigned int)(*(unsigned int *)(v_rsp - 63 + 103)) * 4 * 8) + ((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 28)) + 0 * 1)))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 28)) + 0 * 1)))) * 2 * 8);
    *(unsigned __int64 *)(v_rsp - 63 - 49) = v_rsi;
    result = PopFxFindAcpiDeviceByUniqueId(*(unsigned __int64 *)(v_rsp - 63 + 79), v_rsp - 63 - 121, a3, a4);
    if (sign_flag) goto loc_0075A058;
    v_stack_mD0 = *(unsigned __int64 *)(v_rsp - 63 - 121);
    goto loc_0075A090;
loc_0075A058:
    if (((unsigned int)(*(unsigned __int64 *)(v_rsp - 63 - 121))) != 0xC0000056ULL) goto loc_0075A06B;
loc_0075A062:
    goto loc_0075A65A;
loc_0075A06B:
    a4 = 0;
    v_stack_mE8 = v_stack_mD0;
    result = PopFxCreateDeviceCommon(v_stack_mD0, v_rsp - 63 - 121, a3, a4);
    if (v_stack_mD0 == 0) goto loc_0075A062;
loc_0075A090:
    v_stack_mE8 = 32;
    a4 = 0;
    a3 = 0;
    result = IoInitializeRemoveLockEx(v_stack_mD0 + 240, (unsigned int)((unsigned int)((unsigned int)(0x4D584650ULL))), a3, a4);
    result = ExAllocatePool2(64, *(unsigned __int64 *)(v_rsp - 63 - 65), (unsigned int)((unsigned int)((unsigned int)(0x4D584650ULL))), a4);
    if (result != 0) goto loc_0075A0D6;
loc_0075A0CC:
    goto loc_0075A629;
loc_0075A0D6:
    result = ExAllocatePool2(64, *(unsigned __int64 *)(v_rsp - 63 - 121), (unsigned int)(0x4D584650ULL), a4);
    v_r10 = 0;
    if (result == 0) goto loc_0075A0CC;
    *(unsigned int *)(v_stack_mD0 + 868) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 63 + 103)));
    a4 = (*(unsigned __int64 *)(v_rsp - 63 - 33)) + (result);
    *(unsigned __int64 *)(v_stack_mD0 + 872) = result;
    *(unsigned __int64 *)(v_stack_mD0 + 112) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 63 - 41) = a4;
    *(unsigned __int64 *)(v_stack_mD0 + 128) = v_xmm1;
    *(unsigned __int64 *)(v_stack_mD0 + 144) = v_xmm0;
    *(unsigned __int64 *)(v_stack_mD0 + 160) = v_xmm1;
    *(unsigned __int64 *)(v_stack_mD0 + 176) = v_xmm0;
    *(unsigned __int64 *)(v_stack_mD0 + 192) = *(unsigned __int64 *)(v_rsp - 63 + 111);
    *(unsigned int *)(v_stack_mD0 + 952) = (unsigned int)((unsigned int)(v_stack_mD8));
    *(unsigned __int64 *)(v_stack_mD0 + 640) = 0;
    *(unsigned __int64 *)(v_stack_mD0 + 652) = 5;
    *(unsigned __int64 *)(v_stack_mD0 + 1304 + 8) = v_stack_mD0 + 1304;
    *(unsigned __int64 *)(v_stack_mD0 + 1304) = v_stack_mD0 + 1304;
    *(unsigned __int64 *)(result) = *(unsigned __int64 *)(v_rsp - 63 + 127);
    *(unsigned __int64 *)(v_rsp - 63 - 113) = (unsigned int)(0xC000009AULL) + result * 1;
    *(unsigned int *)(result + 8) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 63 + 103)));
    result = (unsigned int)(0xC000009AULL) + result * 1;
    if ((*(unsigned int *)(v_rsp - 63 + 103)) >= = 0) {
        result = v_stack_mC0;
        result = (result) + (result);
        *(unsigned __int64 *)(v_rsp - 63 - 81) = result;
        result = v_stack_mC8;
        result = (result) + (result);
        *(unsigned __int64 *)(v_rsp - 63 - 73) = result;
    }
    result = (*(unsigned __int64 *)(v_rsp - 63 - 25)) + (result);
    *(unsigned __int64 *)(v_rsp - 63 - 97) = result;
    a3 = (-48) - (result);
    result = (*(unsigned __int64 *)(v_rsp - 63 - 57)) + (result);
    *(unsigned __int64 *)(v_rsp - 63 - 17) = a3;
    a1 = (-16) - (result);
    v_stack_mC8 = result;
    v_stack_mC0 = a1;
loc_0075A1EB:
    v_stack_mD8 = 0;
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 63 + 103))))) goto loc_0075A455;
    v_r12 = (a3) * (0);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mD0 + 872) + 0 * 8) = a4;
    v_r12 = (v_r12) + (*(unsigned __int64 *)(v_rsp - 63 + 95));
    result = (*(unsigned __int64 *)(v_rsp - 63 - 65)) + (-472);
    if ((a3 + a4 + 48 * 1) > result) goto loc_0075A44B;
    *(unsigned int *)(a4 + 48 - 32) = 0;
    *(unsigned __int64 *)(a4 + 48 + 32) = v_stack_mD0;
    *(unsigned __int64 *)(a4) = v_xmm0;
    *(unsigned __int64 *)(a4 + 48 - 8) = v_rip - 4824595;
    a2 = 0;
    *(unsigned __int64 *)(a4 + 48) = a4;
    *(unsigned __int64 *)(a4 + 48 - 24) = 0;
    result = KeInitializeEvent(a4 + 48 + 56, a2, 1, a4);
    v_r11 = 0;
    *(unsigned __int64 *)(a4 + 48 + 80) = 0;
    *(unsigned int *)(a4 + 48 + 108) = (unsigned int)((unsigned int)(*(unsigned int *)(v_r12 + 28)));
    *(unsigned __int64 *)(a4 + 48 + 112) = *(unsigned __int64 *)(v_rsp - 63 - 113);
    *(unsigned int *)(a4 + 48 + 120) = (unsigned int)((unsigned int)(*(unsigned int *)(v_r12 + 24)));
    *(unsigned __int64 *)(a4 + 48 + 152) = 0;
    *(unsigned int *)(a4 + 48 + 168) = 0;
    *(unsigned __int64 *)(a4 + 48 + 416) = a4 + 48 + 408;
    *(unsigned __int64 *)(a4 + 48 + 408) = a4 + 48 + 408;
    *(unsigned __int64 *)(a4 + 48 + 400) = a4 + 48 + 392;
    *(unsigned __int64 *)(a4 + 48 + 392) = a4 + 48 + 392;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_r12 + 40))) == 0) goto loc_0075A2E1;
    *(unsigned __int64 *)(a4 + 48 + 128) = *(unsigned __int64 *)(v_rsp - 63 - 81);
    *(unsigned int *)(a4 + 48 + 124) = (unsigned int)((unsigned int)(*(unsigned int *)(v_r12 + 40)));
loc_0075A2C5:
    a2 = (unsigned int)((0) + 1);
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 - 81)) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_r12 + 48) + 0 * 4)));
    a3 = (*(unsigned __int64 *)(v_rsp - 63 - 81)) + (8);
    if (((unsigned int)(a2)) < (*(unsigned int *)(a4 + 48 + 124))) goto loc_0075A2C5;
    *(unsigned __int64 *)(v_rsp - 63 - 81) = a3;
loc_0075A2E1:
    result = *(unsigned __int64 *)(v_r12 + 48);
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 - 105) + (unsigned int)(v_stack_mD8) + (unsigned int)(v_stack_mD8) * 2 * 4 + 8)) >= = 0) {
        a3 = *(unsigned __int64 *)(v_rsp - 63 - 73);
        *(unsigned __int64 *)(a4 + 48 + 144) = a3;
        result = *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 - 105) + (unsigned int)(v_stack_mD8) + (unsigned int)(v_stack_mD8) * 2 * 4 + 8);
        a3 = a3 + result * 8;
        *(unsigned __int64 *)(v_rsp - 63 - 73) = a3;
    }
    a1 = (v_stack_mC0) + (16);
    a1 = (a1) + (*(unsigned __int64 *)(v_rsp - 63 - 97));
    *(unsigned __int64 *)(result + (unsigned int)(v_stack_mD8) * 8 + 16) = *(unsigned __int64 *)(v_rsp - 63 - 97);
    result = (*(unsigned __int64 *)(v_rsp - 63 - 49)) + (-40);
    if (a1 > result) goto loc_0075A44B;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 - 97)) = v_xmm0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 - 97) + 16) = *(unsigned __int64 *)(v_r12 + 16);
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 - 97) + 28) = (unsigned int)((unsigned int)(*(unsigned int *)(v_r12 + 28)));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 - 97) + 32) = v_stack_mC8;
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 - 97) + 24) = (unsigned int)((unsigned int)(*(unsigned int *)(v_r12 + 24)));
    result = (-16) - (result);
    a1 = (-16) - (result);
    *(unsigned __int64 *)(v_rsp - 63 - 57) = result;
    v_stack_mC0 = a1;
loc_0075A379:
    if (0 >= (*(unsigned int *)(a4 + 48 + 108))) goto loc_0075A41F;
    result = (*(unsigned __int64 *)(v_rsp - 63 - 65)) + (-24);
    a1 = (result + 16) + (*(unsigned __int64 *)(v_rsp - 63 - 113));
    if (a1 > result) goto loc_0075A44B;
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 - 113) + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_r12 + 32) + 0 + 0 * 2 * 8 + 16)));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 - 113)) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_r12 + 32) + 0 + 0 * 2 * 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 - 113) + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_r12 + 32) + 0 + 0 * 2 * 8 + 8);
    a1 = (*(unsigned __int64 *)(v_rsp - 63 - 113)) + (24);
    result = (v_stack_mC0) + (16);
    *(unsigned __int64 *)(v_rsp - 63 - 113) = a1;
    a1 = (v_stack_mC8) + (result);
    result = (*(unsigned __int64 *)(v_rsp - 63 - 49)) + (-24);
    if (a1 > result) goto loc_0075A44B;
    *(unsigned int *)(v_stack_mC8 + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_r12 + 32) + 0 + 0 * 2 * 8 + 16)));
    *(unsigned __int64 *)(v_stack_mC8) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_r12 + 32) + 0 + 0 * 2 * 8);
    *(unsigned __int64 *)(v_stack_mC8 + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_r12 + 32) + 0 + 0 * 2 * 8 + 8);
    a1 = (v_stack_mC8) + (24);
    v_r11 = (unsigned int)((v_r11) + 1);
    v_stack_mC8 = a1;
    goto loc_0075A379;
loc_0075A41F:
    a3 = (*(unsigned __int64 *)(v_rsp - 63 - 97)) + (40);
    a4 = (*(unsigned __int64 *)(v_rsp - 63 - 41)) + (472);
    *(unsigned __int64 *)(v_rsp - 63 - 97) = a3;
    v_rbx = (a4 + 48) + (472);
    a2 = (unsigned int)(((unsigned int)(v_stack_mD8)) + 1);
    *(unsigned __int64 *)(v_rsp - 63 - 41) = a4;
    v_r10 = 0;
    goto loc_0075A1EB;
loc_0075A44B:
    goto loc_0075A61C;
loc_0075A455:
    *(unsigned int *)(v_stack_mD0 + 880) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 63 - 89)));
    v_r13 = 0;
    *(unsigned __int64 *)(v_stack_mD0 + 888) = result + v_r13 * 1;
    if ((*(unsigned int *)(v_rsp - 63 + 103)) <= 0) goto loc_0075A48B;
    result = PopFxVerifyDependencies(*(unsigned __int64 *)(v_rsp - 63 - 105), v_stack_mD0, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 63 + 103)))), a4);
    if (sign_flag) goto loc_0075A61C;
loc_0075A48B:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 63 + 103))) == 0) goto loc_0075A511;
loc_0075A496:
    if ((*(unsigned int *)(*(unsigned __int64 *)(0 + *(unsigned __int64 *)(v_stack_mD0 + 872) * 1) + 172)) <= 0) goto loc_0075A4F5;
loc_0075A4AD:
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mD0 + 872) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(0 + *(unsigned __int64 *)(v_stack_mD0 + 872) * 1) + 176) + 0 * 8)) * 8) + 192) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mD0 + 872) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(0 + *(unsigned __int64 *)(v_stack_mD0 + 872) * 1) + 176) + 0 * 8)) * 8) + 188)) * 8) = 0;
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mD0 + 872) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(0 + *(unsigned __int64 *)(v_stack_mD0 + 872) * 1) + 176) + 0 * 8)) * 8) + 192) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mD0 + 872) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(0 + *(unsigned __int64 *)(v_stack_mD0 + 872) * 1) + 176) + 0 * 8)) * 8) + 188)) * 8 + 4) = 0;
    a4 = (unsigned int)((0) + 1);
    if (((unsigned int)(a4)) < (*(unsigned int *)(*(unsigned __int64 *)(0 + *(unsigned __int64 *)(v_stack_mD0 + 872) * 1) + 172))) goto loc_0075A4AD;
loc_0075A4F5:
    a3 = 0;
    result = PopFxActivateComponent(v_stack_mD0, *(unsigned __int64 *)(0 + *(unsigned __int64 *)(v_stack_mD0 + 872) * 1), a3, 1);
    v_rbx = (unsigned int)((0) + 1);
    v_r12 = (0) + (8);
    if (((unsigned int)(v_rbx)) < ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 63 + 103))))) goto loc_0075A496;
loc_0075A511:
    if (condition_is_less_or_equal) goto loc_0075A53A;
    a1 = (unsigned __int8)((*(unsigned __int8 *)(v_rsp - 63 + 119)) + (2));
    result = (*(unsigned __int64 *)(v_rsp - 63 - 9)) + (result);
    a2 = 0;
    *(unsigned __int64 *)(v_stack_mD0 + 24) = result;
    result = IoAllocateIrp(a1, a2, a3, 1);
    *(unsigned __int64 *)(v_stack_mD0 + 16) = result;
    if (result == 0) goto loc_0075A44B;
loc_0075A53A:
    result = PopFxRegisterDeviceWithPep(*(unsigned __int64 *)(v_rsp - 63 + 71), *(unsigned __int64 *)(v_rsp - 63 + 79), v_stack_mD0, result);
    if ((unsigned __int8)(result) == 0) {
        a4 = 0;
        a3 = result;
        a2 = v_stack_mD0;
        a1 = 0x601ULL;
        result = PopFxBugCheck(a1, a2, a3, a4);
    }
    result = PopPlRegisterDevice(v_stack_mD0, a2, a3, a4);
    a1 = ((*(unsigned int *)(v_rip + 7394008)) != 0) ? 1 : 0;
    if ((((unsigned __int8)(*(unsigned __int64 *)(result))) & (16)) != 0) goto loc_0075A596;
    if ((((unsigned __int8)(*(unsigned __int64 *)(result))) & (8)) != 0) goto loc_0075A586;
    v_rdi = v_stack_mD0;
    if ((unsigned __int8)(a1) != 0) {
        v_rdi = v_stack_mD0;
    }
    if (((*(unsigned __int8 *)(result)) & (32)) != 0) {
        v_rdi = v_stack_mD0;
    }
    if (((*(unsigned __int8 *)(result)) & (64)) != 0) {
        v_rdi = v_stack_mD0;
    }
    v_rbx = (*(unsigned __int64 *)(v_rsp - 63 - 33)) + (result);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 63 + 103))) == 0) goto loc_0075A609;
    v_rdi = (*(unsigned __int64 *)(v_rsp - 63 - 25)) + (28);
    v_rdi = (v_rdi) + (result);
loc_0075A5D4:
    result = *(unsigned __int64 *)(result);
    if (((*(unsigned __int8 *)(v_rdi - 12)) & (2)) != 0) {
        result = *(unsigned int *)(v_rbx + 92);
        result = (unsigned int)((result) | (2));
        *(unsigned int *)(v_rbx + 92) = (unsigned int)(result);
    }
    *(unsigned int *)(v_rbx + 156) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rdi)));
    result = PopPlRegisterComponent(v_rbx, a2, a3, a4);
    v_rbx = (v_rbx) + (472);
    v_rdi = (v_rdi) + (40);
    v_r14 = ((unsigned int)(*(unsigned int *)(v_rsp - 63 + 103))) - (1);
    if (condition_is_not_equal) goto loc_0075A5D4;
loc_0075A609:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 + 135)) = v_stack_mD0;
loc_0075A61C:
    result = ExFreePoolWithTag(result, (unsigned int)(0x4D584650ULL), a3, a4);
loc_0075A629:
    if (0 == 0) goto loc_0075A644;
    if (*(unsigned __int64 *)(v_rsp - 63 - 121) == 0) {
        a2 = 0x4D584650ULL;
        a1 = 0;
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
    if (0 != 0) {
        a2 = 0x4D584650ULL;
        a1 = 0;
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
loc_0075A65A:
    result = ExFreePoolWithTag(*(unsigned __int64 *)(v_rsp - 63 - 105), (unsigned int)(0x4D584650ULL), a3, a4);
    if (*(unsigned __int64 *)(v_rsp - 63 - 121) != 0) {
        a2 = 0x66466F50ULL;
        a1 = *(unsigned __int64 *)(v_rsp - 63 - 121);
        result = PopFxReleaseAcpiRefDevice(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (208);
    return 0;
}
```

## 5. (Beta) C Style

```c
int64_t PopFxRegisterDeviceWorker(int64_t Arg1, int64_t Arg2, void *Arg3, int64_t Arg4)
{
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint32_t v_stack_mD8;
    uint64_t v_stack_mE8;
    uint64_t v_stack_p18;

    *(uint64_t *)(local_rsp + 0x18) = local_rbx;
    *(uint64_t *)(local_rsp + 0x20) = Arg4;
    *(uint64_t *)(local_rsp + 0x10) = Arg2;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (208);
    result = 0;
    local_r13 = (uint32_t)((local_r13) | (0xFFFFFFFFULL));
    *(uint64_t *)(local_rsp - 0x3F - 0x79) = 0;
    v_stack_mD0 = 0;
    v_stack_mD8 = (uint32_t)((uint32_t)((uint32_t)(local_r13)));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x3F + 0x67))) != 0) goto loc_00759E7A;
loc_00759E70:
    goto loc_0075A679;
loc_00759E7A:
    result = (uint8_t)((*(uint8_t *)(local_rsp - 0x3F + 0x7F)) & (24));
    if (((uint8_t)(result)) == 24) goto loc_00759E70;
    Arg2 = ((uint32_t)(*(uint32_t *)(local_rsp - 0x3F + 0x67)) + (uint32_t)(*(uint32_t *)(local_rsp - 0x3F + 0x67)) * 2) << (2);
    result = ExAllocatePool2(256, Arg2, (uint32_t)(0x4D584650ULL), Arg4);
    Arg4 = 0;
    *(uint64_t *)(local_rsp - 0x3F - 0x69) = result;
    if (result != 0) goto loc_00759EB4;
    goto loc_0075A679;
loc_00759EB4:
    *(uint32_t *)(local_rsp - 0x3F + 0x67) = 0;
loc_00759EC1:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x3F + 0x67))))) goto loc_00759F70;
    Arg2 = (Arg2) * (0);
    Arg2 = (Arg2) + (0);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0x1C))) == 0) goto loc_00759F66;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0x1C)))) <= 1) goto loc_00759EFD;
    if ((*(uint64_t *)(arg3)) == 0) goto loc_00759F66;
    if ((*(uint64_t *)(arg3 + 0x8)) == 0) goto loc_00759F66;
    if ((*(uint64_t *)(arg3 + 0x10)) == 0) goto loc_00759F66;
    if ((*(uint32_t *)(Arg2 + 0x18)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0x1C))))) goto loc_00759F66;
loc_00759EFD:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0x1C)) + 0 * 1)) < 0) goto loc_00759F66;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0x28))) == 0) goto loc_00759F4C;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0x28)))) >= ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x3F + 0x67))))) goto loc_00759F66;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0x28)) + 0 * 1)) < 0) goto loc_00759F66;
    *(uint32_t *)(local_rsp - 0x3F + 0x67) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0x28)) + 0 * 1);
loc_00759F21:
    if (0 >= (*(uint32_t *)(Arg2 + 0x28))) goto loc_00759F45;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg2 + 0x30) + 0x0 * 4)))) >= ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x3F + 0x67))))) goto loc_00759F66;
    Arg4 = (uint32_t)((Arg4) + 1);
    goto loc_00759F21;
loc_00759F45:
    Arg4 = 0;
loc_00759F4C:
    if (((*(uint8_t *)(Arg2 + 0x10)) & (4)) == 0) goto loc_00759F5E;
    if (((uint32_t)((uint32_t)(0xC000009AULL))) != ((uint32_t)(local_r13))) goto loc_00759F66;
    v_stack_mD8 = 0;
loc_00759F5E:
    Arg3 = (uint32_t)((0) + 1);
    goto loc_00759EC1;
loc_00759F66:
    goto loc_0075A65A;
loc_00759F70:
    result = (*(uint64_t *)(Arg2 + 0x30)) * ((uint32_t)(*(uint32_t *)(local_rsp - 0x3F + 0x67)));
    *(uint64_t *)(local_rsp - 0x3F - 0x51) = 0;
    *(uint64_t *)(local_rsp - 0x3F - 0x21) = (uint32_t)(*(uint32_t *)(local_rsp - 0x3F + 0x67)) * 8;
    local_rbx = ((uint32_t)(*(uint32_t *)(local_rsp - 0x3F + 0x67)) * 8) + (result);
    *(uint64_t *)(local_rsp - 0x3F - 0x61) = local_rbx;
    v_stack_mC0 = 0;
    *(uint64_t *)(local_rsp - 0x3F - 0x49) = 0;
    v_stack_mC8 = 0;
    local_r13 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0x1C)) + 0 * 1)))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0x1C)) + 0 * 1)))) * 2 * 8 + local_rbx * 1 + 312;
    if (condition_is_less_or_equal) { local_r13 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0x1C)) + 0 * 1)))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0x1C)) + 0 * 1)))) * 2 * 8 + local_rbx * 1; }
    Arg1 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0x1C)) + 0 * 1)))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0x1C)) + 0 * 1)))) * 2 * 8 + local_rbx * 1;
    if (condition_is_less_or_equal) { Arg1 = 0; }
    *(uint64_t *)(local_rsp - 0x3F - 0x9) = Arg1;
    result = *(uint8_t *)(local_rsp - 0x3F + 0x77);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x3F + 0x67))) != 0) {
        result = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x3F + 0x67)));
        result = (result) << (3);
        v_stack_mC0 = local_r13;
        Arg1 = result + local_r13 * 1;
        v_stack_mC8 = Arg1;
        local_r13 = local_r13 + result * 2;
    }
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x3F + 0x67))))) * (*(uint32_t *)(v_rip + 0x6B13D8)));
    *(uint32_t *)(local_rsp - 0x3F - 0x59) = (uint32_t)(result);
    result = (result + result * 2 * 8) + (local_r13);
    *(uint64_t *)(local_rsp - 0x3F - 0x41) = result;
    Arg3 = ((int32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x3F + 0x67)) * 8))) + (16);
    *(void **)(local_rsp - 0x3F - 0x19) = Arg3;
    *(void **)(local_rsp - 0x3F - 0x39) = Arg3 + (uint32_t)(*(uint32_t *)(local_rsp - 0x3F + 0x67)) + (uint32_t)(*(uint32_t *)(local_rsp - 0x3F + 0x67)) * 4 * 8;
    local_rsi = (Arg3 + (uint32_t)(*(uint32_t *)(local_rsp - 0x3F + 0x67)) + (uint32_t)(*(uint32_t *)(local_rsp - 0x3F + 0x67)) * 4 * 8) + ((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0x1C)) + 0 * 1)))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0x1C)) + 0 * 1)))) * 2 * 8);
    *(uint64_t *)(local_rsp - 0x3F - 0x31) = local_rsi;
    result = PopFxFindAcpiDeviceByUniqueId(*(uint64_t *)(local_rsp - 0x3F + 0x4F), local_rsp - 63 - 121, Arg3, Arg4);
    if (sign_flag) goto loc_0075A058;
    v_stack_mD0 = *(uint64_t *)(local_rsp - 0x3F - 0x79);
    goto loc_0075A090;
loc_0075A058:
    if (((uint32_t)(*(uint64_t *)(local_rsp - 0x3F - 0x79))) != 0xC0000056ULL) goto loc_0075A06B;
loc_0075A062:
    goto loc_0075A65A;
loc_0075A06B:
    Arg4 = 0;
    v_stack_mE8 = v_stack_mD0;
    result = PopFxCreateDeviceCommon(v_stack_mD0, local_rsp - 63 - 121, Arg3, Arg4);
    if (v_stack_mD0 == 0) goto loc_0075A062;
loc_0075A090:
    v_stack_mE8 = 32;
    Arg4 = 0;
    Arg3 = 0;
    result = IoInitializeRemoveLockEx(v_stack_mD0 + 240, (uint32_t)((uint32_t)((uint32_t)(0x4D584650ULL))), Arg3, Arg4);
    result = ExAllocatePool2(64, *(uint64_t *)(local_rsp - 0x3F - 0x41), (uint32_t)((uint32_t)((uint32_t)(0x4D584650ULL))), Arg4);
    if (result != 0) goto loc_0075A0D6;
loc_0075A0CC:
    goto loc_0075A629;
loc_0075A0D6:
    result = ExAllocatePool2(64, *(uint64_t *)(local_rsp - 0x3F - 0x79), (uint32_t)(0x4D584650ULL), Arg4);
    local_r10 = 0;
    if (result == 0) goto loc_0075A0CC;
    *(uint32_t *)(v_stack_mD0 + 0x364) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x3F + 0x67)));
    Arg4 = (*(uint64_t *)(local_rsp - 0x3F - 0x21)) + (result);
    *(uint64_t *)(v_stack_mD0 + 0x368) = result;
    *(uint64_t *)(v_stack_mD0 + 0x70) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x3F - 0x29) = Arg4;
    *(uint64_t *)(v_stack_mD0 + 0x80) = v_xmm1;
    *(uint64_t *)(v_stack_mD0 + 0x90) = v_xmm0;
    *(uint64_t *)(v_stack_mD0 + 0xA0) = v_xmm1;
    *(uint64_t *)(v_stack_mD0 + 0xB0) = v_xmm0;
    *(uint64_t *)(v_stack_mD0 + 0xC0) = *(uint64_t *)(local_rsp - 0x3F + 0x6F);
    *(uint32_t *)(v_stack_mD0 + 0x3B8) = (uint32_t)((uint32_t)(v_stack_mD8));
    *(uint64_t *)(v_stack_mD0 + 0x280) = 0;
    *(uint64_t *)(v_stack_mD0 + 0x28C) = 5;
    *(uint64_t *)(v_stack_mD0 + 0x518 + 0x8) = v_stack_mD0 + 1304;
    *(uint64_t *)(v_stack_mD0 + 0x518) = v_stack_mD0 + 1304;
    *(uint64_t *)(result) = *(uint64_t *)(local_rsp - 0x3F + 0x7F);
    *(uint64_t *)(local_rsp - 0x3F - 0x71) = (uint32_t)(0xC000009AULL) + result * 1;
    *(uint32_t *)(result + 0x8) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x3F + 0x67)));
    result = (uint32_t)(0xC000009AULL) + result * 1;
    if ((*(uint32_t *)(local_rsp - 0x3F + 0x67)) >= = 0) {
        result = v_stack_mC0;
        result = (result) + (result);
        *(uint64_t *)(local_rsp - 0x3F - 0x51) = result;
        result = v_stack_mC8;
        result = (result) + (result);
        *(uint64_t *)(local_rsp - 0x3F - 0x49) = result;
    }
    result = (*(uint64_t *)(local_rsp - 0x3F - 0x19)) + (result);
    *(uint64_t *)(local_rsp - 0x3F - 0x61) = result;
    Arg3 = (-48) - (result);
    result = (*(uint64_t *)(local_rsp - 0x3F - 0x39)) + (result);
    *(void **)(local_rsp - 0x3F - 0x11) = Arg3;
    Arg1 = (-16) - (result);
    v_stack_mC8 = result;
    v_stack_mC0 = Arg1;
loc_0075A1EB:
    v_stack_mD8 = 0;
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x3F + 0x67))))) goto loc_0075A455;
    local_r12 = (Arg3) * (0);
    *(uint64_t *)(*(uint64_t *)(v_stack_mD0 + 0x368) + 0x0 * 8) = Arg4;
    local_r12 = (local_r12) + (*(uint64_t *)(local_rsp - 0x3F + 0x5F));
    result = (*(uint64_t *)(local_rsp - 0x3F - 0x41)) + (-472);
    if ((Arg3 + Arg4 + 48 * 1) > result) goto loc_0075A44B;
    *(uint32_t *)(Arg4 + 0x30 - 0x20) = 0;
    *(uint64_t *)(Arg4 + 0x30 + 0x20) = v_stack_mD0;
    *(uint64_t *)(Arg4) = v_xmm0;
    *(uint64_t *)(Arg4 + 0x30 - 0x8) = v_rip - 4824595;
    Arg2 = 0;
    *(uint64_t *)(Arg4 + 0x30) = Arg4;
    *(uint64_t *)(Arg4 + 0x30 - 0x18) = 0;
    result = KeInitializeEvent(Arg4 + 48 + 56, Arg2, 1, Arg4);
    local_r11 = 0;
    *(uint64_t *)(Arg4 + 0x30 + 0x50) = 0;
    *(uint32_t *)(Arg4 + 0x30 + 0x6C) = (uint32_t)((uint32_t)(*(uint32_t *)(local_r12 + 0x1C)));
    *(uint64_t *)(Arg4 + 0x30 + 0x70) = *(uint64_t *)(local_rsp - 0x3F - 0x71);
    *(uint32_t *)(Arg4 + 0x30 + 0x78) = (uint32_t)((uint32_t)(*(uint32_t *)(local_r12 + 0x18)));
    *(uint64_t *)(Arg4 + 0x30 + 0x98) = 0;
    *(uint32_t *)(Arg4 + 0x30 + 0xA8) = 0;
    *(uint64_t *)(Arg4 + 0x30 + 0x1A0) = Arg4 + 48 + 408;
    *(uint64_t *)(Arg4 + 0x30 + 0x198) = Arg4 + 48 + 408;
    *(uint64_t *)(Arg4 + 0x30 + 0x190) = Arg4 + 48 + 392;
    *(uint64_t *)(Arg4 + 0x30 + 0x188) = Arg4 + 48 + 392;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_r12 + 0x28))) == 0) goto loc_0075A2E1;
    *(uint64_t *)(Arg4 + 0x30 + 0x80) = *(uint64_t *)(local_rsp - 0x3F - 0x51);
    *(uint32_t *)(Arg4 + 0x30 + 0x7C) = (uint32_t)((uint32_t)(*(uint32_t *)(local_r12 + 0x28)));
loc_0075A2C5:
    Arg2 = (uint32_t)((0) + 1);
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F - 0x51)) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_r12 + 0x30) + 0x0 * 4)));
    Arg3 = (*(uint64_t *)(local_rsp - 0x3F - 0x51)) + (8);
    if (((uint32_t)(Arg2)) < (*(uint32_t *)(Arg4 + 0x30 + 0x7C))) goto loc_0075A2C5;
    *(void **)(local_rsp - 0x3F - 0x51) = Arg3;
loc_0075A2E1:
    result = *(uint64_t *)(local_r12 + 0x30);
    if ((*(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F - 0x69) + (uint32_t)(v_stack_mD8) + (uint32_t)(v_stack_mD8) * 2 * 4 + 0x8)) >= = 0) {
        Arg3 = *(uint64_t *)(local_rsp - 0x3F - 0x49);
        *(void **)(Arg4 + 0x30 + 0x90) = Arg3;
        result = *(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F - 0x69) + (uint32_t)(v_stack_mD8) + (uint32_t)(v_stack_mD8) * 2 * 4 + 0x8);
        Arg3 = Arg3 + result * 8;
        *(void **)(local_rsp - 0x3F - 0x49) = Arg3;
    }
    Arg1 = (v_stack_mC0) + (16);
    Arg1 = (Arg1) + (*(uint64_t *)(local_rsp - 0x3F - 0x61));
    *(uint64_t *)(result + (uint32_t)(v_stack_mD8) * 8 + 0x10) = *(uint64_t *)(local_rsp - 0x3F - 0x61);
    result = (*(uint64_t *)(local_rsp - 0x3F - 0x31)) + (-40);
    if (Arg1 > result) goto loc_0075A44B;
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F - 0x61)) = v_xmm0;
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F - 0x61) + 0x10) = *(uint64_t *)(local_r12 + 0x10);
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F - 0x61) + 0x1C) = (uint32_t)((uint32_t)(*(uint32_t *)(local_r12 + 0x1C)));
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F - 0x61) + 0x20) = v_stack_mC8;
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F - 0x61) + 0x18) = (uint32_t)((uint32_t)(*(uint32_t *)(local_r12 + 0x18)));
    result = (-16) - (result);
    Arg1 = (-16) - (result);
    *(uint64_t *)(local_rsp - 0x3F - 0x39) = result;
    v_stack_mC0 = Arg1;
loc_0075A379:
    if (0 >= (*(uint32_t *)(Arg4 + 0x30 + 0x6C))) goto loc_0075A41F;
    result = (*(uint64_t *)(local_rsp - 0x3F - 0x41)) + (-24);
    Arg1 = (result + 16) + (*(uint64_t *)(local_rsp - 0x3F - 0x71));
    if (Arg1 > result) goto loc_0075A44B;
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F - 0x71) + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_r12 + 0x20) + 0x0 + 0x0 * 2 * 8 + 0x10)));
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F - 0x71)) = *(uint64_t *)(*(uint64_t *)(local_r12 + 0x20) + 0x0 + 0x0 * 2 * 8);
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F - 0x71) + 0x8) = *(uint64_t *)(*(uint64_t *)(local_r12 + 0x20) + 0x0 + 0x0 * 2 * 8 + 0x8);
    Arg1 = (*(uint64_t *)(local_rsp - 0x3F - 0x71)) + (24);
    result = (v_stack_mC0) + (16);
    *(uint64_t *)(local_rsp - 0x3F - 0x71) = Arg1;
    Arg1 = (v_stack_mC8) + (result);
    result = (*(uint64_t *)(local_rsp - 0x3F - 0x31)) + (-24);
    if (Arg1 > result) goto loc_0075A44B;
    *(uint32_t *)(v_stack_mC8 + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_r12 + 0x20) + 0x0 + 0x0 * 2 * 8 + 0x10)));
    *(uint64_t *)(v_stack_mC8) = *(uint64_t *)(*(uint64_t *)(local_r12 + 0x20) + 0x0 + 0x0 * 2 * 8);
    *(uint64_t *)(v_stack_mC8 + 0x8) = *(uint64_t *)(*(uint64_t *)(local_r12 + 0x20) + 0x0 + 0x0 * 2 * 8 + 0x8);
    Arg1 = (v_stack_mC8) + (24);
    local_r11 = (uint32_t)((local_r11) + 1);
    v_stack_mC8 = Arg1;
    goto loc_0075A379;
loc_0075A41F:
    Arg3 = (*(uint64_t *)(local_rsp - 0x3F - 0x61)) + (40);
    Arg4 = (*(uint64_t *)(local_rsp - 0x3F - 0x29)) + (472);
    *(void **)(local_rsp - 0x3F - 0x61) = Arg3;
    local_rbx = (Arg4 + 48) + (472);
    Arg2 = (uint32_t)(((uint32_t)(v_stack_mD8)) + 1);
    *(uint64_t *)(local_rsp - 0x3F - 0x29) = Arg4;
    local_r10 = 0;
    goto loc_0075A1EB;
loc_0075A44B:
    goto loc_0075A61C;
loc_0075A455:
    *(uint32_t *)(v_stack_mD0 + 0x370) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x3F - 0x59)));
    local_r13 = 0;
    *(uint64_t *)(v_stack_mD0 + 0x378) = result + local_r13 * 1;
    if ((*(uint32_t *)(local_rsp - 0x3F + 0x67)) <= 0) goto loc_0075A48B;
    result = PopFxVerifyDependencies(*(uint64_t *)(local_rsp - 0x3F - 0x69), v_stack_mD0, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x3F + 0x67)))), Arg4);
    if (sign_flag) goto loc_0075A61C;
loc_0075A48B:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x3F + 0x67))) == 0) goto loc_0075A511;
loc_0075A496:
    if ((*(uint32_t *)(*(uint64_t *)(0 + *(uint64_t *)(v_stack_mD0 + 0x368) * 1) + 0xAC)) <= 0) goto loc_0075A4F5;
loc_0075A4AD:
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_mD0 + 0x368) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(0 + *(uint64_t *)(v_stack_mD0 + 0x368) * 1) + 0xB0) + 0x0 * 8)) * 8) + 0xC0) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_mD0 + 0x368) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(0 + *(uint64_t *)(v_stack_mD0 + 0x368) * 1) + 0xB0) + 0x0 * 8)) * 8) + 0xBC)) * 8) = 0;
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_mD0 + 0x368) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(0 + *(uint64_t *)(v_stack_mD0 + 0x368) * 1) + 0xB0) + 0x0 * 8)) * 8) + 0xC0) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_mD0 + 0x368) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(0 + *(uint64_t *)(v_stack_mD0 + 0x368) * 1) + 0xB0) + 0x0 * 8)) * 8) + 0xBC)) * 8 + 0x4) = 0;
    Arg4 = (uint32_t)((0) + 1);
    if (((uint32_t)(Arg4)) < (*(uint32_t *)(*(uint64_t *)(0 + *(uint64_t *)(v_stack_mD0 + 0x368) * 1) + 0xAC))) goto loc_0075A4AD;
loc_0075A4F5:
    Arg3 = 0;
    result = PopFxActivateComponent(v_stack_mD0, *(uint64_t *)(0 + *(uint64_t *)(v_stack_mD0 + 0x368) * 1), Arg3, 1);
    local_rbx = (uint32_t)((0) + 1);
    local_r12 = (0) + (8);
    if (((uint32_t)(local_rbx)) < ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x3F + 0x67))))) goto loc_0075A496;
loc_0075A511:
    if (condition_is_less_or_equal) goto loc_0075A53A;
    Arg1 = (uint8_t)((*(uint8_t *)(local_rsp - 0x3F + 0x77)) + (2));
    result = (*(uint64_t *)(local_rsp - 0x3F - 0x9)) + (result);
    Arg2 = 0;
    *(uint64_t *)(v_stack_mD0 + 0x18) = result;
    result = IoAllocateIrp(Arg1, Arg2, Arg3, 1);
    *(uint64_t *)(v_stack_mD0 + 0x10) = result;
    if (result == 0) goto loc_0075A44B;
loc_0075A53A:
    result = PopFxRegisterDeviceWithPep(*(uint64_t *)(local_rsp - 0x3F + 0x47), *(uint64_t *)(local_rsp - 0x3F + 0x4F), v_stack_mD0, result);
    if ((uint8_t)(result) == 0) {
        Arg4 = 0;
        Arg3 = result;
        Arg2 = v_stack_mD0;
        Arg1 = 0x601ULL;
        result = PopFxBugCheck(Arg1, Arg2, Arg3, Arg4);
    }
    result = PopPlRegisterDevice(v_stack_mD0, Arg2, Arg3, Arg4);
    Arg1 = ((*(uint32_t *)(v_rip + 0x70D2D8)) != 0) ? 1 : 0;
    if ((((uint8_t)(*(uint64_t *)(result))) & (16)) != 0) goto loc_0075A596;
    if ((((uint8_t)(*(uint64_t *)(result))) & (8)) != 0) goto loc_0075A586;
    local_rdi = v_stack_mD0;
    if ((uint8_t)(Arg1) != 0) {
        local_rdi = v_stack_mD0;
    }
    if (((*(uint8_t *)(result)) & (32)) != 0) {
        local_rdi = v_stack_mD0;
    }
    if (((*(uint8_t *)(result)) & (64)) != 0) {
        local_rdi = v_stack_mD0;
    }
    local_rbx = (*(uint64_t *)(local_rsp - 0x3F - 0x21)) + (result);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x3F + 0x67))) == 0) goto loc_0075A609;
    local_rdi = (*(uint64_t *)(local_rsp - 0x3F - 0x19)) + (28);
    local_rdi = (local_rdi) + (result);
loc_0075A5D4:
    result = *(uint64_t *)(result);
    if (((*(uint8_t *)(local_rdi - 0xC)) & (2)) != 0) {
        result = *(uint32_t *)(local_rbx + 0x5C);
        result = (uint32_t)((result) | (2));
        *(uint32_t *)(local_rbx + 0x5C) = (uint32_t)(result);
    }
    *(uint32_t *)(local_rbx + 0x9C) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rdi)));
    result = PopPlRegisterComponent(local_rbx, Arg2, Arg3, Arg4);
    local_rbx = (local_rbx) + (472);
    local_rdi = (local_rdi) + (40);
    local_r14 = ((uint32_t)(*(uint32_t *)(local_rsp - 0x3F + 0x67))) - (1);
    if (condition_is_not_equal) goto loc_0075A5D4;
loc_0075A609:
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x87)) = v_stack_mD0;
loc_0075A61C:
    result = ExFreePoolWithTag(result, (uint32_t)(0x4D584650ULL), Arg3, Arg4);
loc_0075A629:
    if (0 == 0) goto loc_0075A644;
    if (*(uint64_t *)(local_rsp - 0x3F - 0x79) == 0) {
        Arg2 = 0x4D584650ULL;
        Arg1 = 0;
        result = ExFreePoolWithTag(Arg1, Arg2, Arg3, Arg4);
    }
    if (0 != 0) {
        Arg2 = 0x4D584650ULL;
        Arg1 = 0;
        result = ExFreePoolWithTag(Arg1, Arg2, Arg3, Arg4);
    }
loc_0075A65A:
    result = ExFreePoolWithTag(*(uint64_t *)(local_rsp - 0x3F - 0x69), (uint32_t)(0x4D584650ULL), Arg3, Arg4);
    if (*(uint64_t *)(local_rsp - 0x3F - 0x79) != 0) {
        Arg2 = 0x66466F50ULL;
        Arg1 = *(uint64_t *)(local_rsp - 0x3F - 0x79);
        result = PopFxReleaseAcpiRefDevice(Arg1, Arg2, Arg3, Arg4);
    }
    local_rsp = (local_rsp) + (208);
    return 0;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x0` | `64` | `R` |
| `Arg3` | `+ 0x0` | `128` | `R` |
| `Arg3` | `+ 0x8` | `64` | `R` |
| `Arg3` | `+ 0x10` | `64` | `R` |
| `Arg3` | `+ 0x10` | `128` | `R` |
| `Arg3` | `+ 0x18` | `32` | `R` |
| `Arg3` | `+ 0x1C` | `32` | `R` |
| `Arg3` | `+ 0x20` | `64` | `R` |
| `Arg3` | `+ 0x20` | `128` | `R` |
| `Arg3` | `+ 0x28` | `32` | `R` |
| `Arg3` | `+ 0x30` | `64` | `R` |
| `Arg3` | `+ 0x30` | `128` | `R` |
| `Arg3` | `+ 0x40` | `128` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00759E20&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
