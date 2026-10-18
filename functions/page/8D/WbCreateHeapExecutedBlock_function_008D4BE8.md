# WbCreateHeapExecutedBlock

- RVA: `0x008D4BE8`–`0x008D5410` (길이 `2,088` bytes)
- VA: `0x00000001408D4BE8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000850AC`
- 디코드: `453`개 명령, `2,088/2,088` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **31**; 고유 호출 대상: **15**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x008D4C7A` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008D4C98` → [PdcCloseEvent](PdcCloseEvent_function_008D2404.md) (function, `0x008D2404`)
- `0x008D4CAE` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x008D4CE4` → [sub_008D1C2C](Unknown_function_008D1C2C.md) (function, `0x008D1C2C`)
- `0x008D4D0C` → [IoAllocateMdl](../../text/29/IoAllocateMdl_function_0029EBF0.md) (function, `0x0029EBF0`)
- `0x008D4D2E` → [MmProbeAndLockPagesPrivate](../../text/48/MmProbeAndLockPagesPrivate_function_0048ED68.md) (function, `0x0048ED68`)
- `0x008D4D54` → [sub_009A13B8](../9A/Unknown_function_009A13B8.md) (function, `0x009A13B8`)
- `0x008D4D81` → [sub_009A09B8](../9A/Unknown_function_009A09B8.md) (function, `0x009A09B8`)
- `0x008D4DAA` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008D4DBF` → [PdcCloseEvent](PdcCloseEvent_function_008D2404.md) (function, `0x008D2404`)
- `0x008D4E1A` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x008D4E4B` → [IoAllocateMdl](../../text/29/IoAllocateMdl_function_0029EBF0.md) (function, `0x0029EBF0`)
- `0x008D4E61` → [MmProbeAndLockPagesPrivate](../../text/48/MmProbeAndLockPagesPrivate_function_0048ED68.md) (function, `0x0048ED68`)
- `0x008D4F44` → [sub_0040C640](../../text/40/Unknown_function_0040C640.md) (function, `0x0040C640`)
- `0x008D4F5D` → [sub_009A13B8](../9A/Unknown_function_009A13B8.md) (function, `0x009A13B8`)
- `0x008D4FA7` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x008D4FD8` → [IoAllocateMdl](../../text/29/IoAllocateMdl_function_0029EBF0.md) (function, `0x0029EBF0`)
- `0x008D4FEE` → [MmProbeAndLockPagesPrivate](../../text/48/MmProbeAndLockPagesPrivate_function_0048ED68.md) (function, `0x0048ED68`)
- `0x008D50CB` → [sub_0040C640](../../text/40/Unknown_function_0040C640.md) (function, `0x0040C640`)
- `0x008D50E4` → [sub_009A13B8](../9A/Unknown_function_009A13B8.md) (function, `0x009A13B8`)
- `0x008D51D9` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x008D5297` → [ZwFlushInstructionCache](../../text/6A/ZwFlushInstructionCache_function_006AEEF0.md) (function, `0x006AEEF0`)
- `0x008D52DC` → [MmUnlockPages](../../text/29/MmUnlockPages_function_0029EEE0.md) (function, `0x0029EEE0`)
- `0x008D52E6` → [IoFreeMdl](../../text/29/IoFreeMdl_function_0029EA80.md) (function, `0x0029EA80`)
- `0x008D52FE` → [MmUnlockPages](../../text/29/MmUnlockPages_function_0029EEE0.md) (function, `0x0029EEE0`)
- `0x008D5308` → [IoFreeMdl](../../text/29/IoFreeMdl_function_0029EA80.md) (function, `0x0029EA80`)
- `0x008D5328` → [sub_008D23A4](Unknown_function_008D23A4.md) (function, `0x008D23A4`)
- `0x008D5332` → [PdcCloseEvent](PdcCloseEvent_function_008D2404.md) (function, `0x008D2404`)
- `0x008D5344` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x008D53E4` → [ZwFlushInstructionCache](../../text/6A/ZwFlushInstructionCache_function_006AEEF0.md) (function, `0x006AEEF0`)
- `0x008D5405` → [MmUnlockPages](../../text/29/MmUnlockPages_function_0029EEE0.md) (function, `0x0029EEE0`)

### Direct callers
- [sub_008D2F2C](Unknown_function_008D2F2C.md) at `0x008D3142`

### Static image references
- `0x008D4BFE` → RVA `0x00E0A740` (`.data`; read)
- `0x008D4C5D` → RVA `0x00E3EA70` (`.data`; read)
- `0x008D4E84` → RVA `0x00002A00` (`.rdata`; read)
- `0x008D4E93` → RVA `0x000029F0` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **22**
  - `0x008D4C7A` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008D4CAE` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x008D4D0C` → [IoAllocateMdl](../../text/29/IoAllocateMdl_function_0029EBF0.md) (`PAGE` → `.text`)
  - `0x008D4D2E` → [MmProbeAndLockPagesPrivate](../../text/48/MmProbeAndLockPagesPrivate_function_0048ED68.md) (`PAGE` → `.text`)
  - `0x008D4DAA` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008D4E1A` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x008D4E4B` → [IoAllocateMdl](../../text/29/IoAllocateMdl_function_0029EBF0.md) (`PAGE` → `.text`)
  - `0x008D4E61` → [MmProbeAndLockPagesPrivate](../../text/48/MmProbeAndLockPagesPrivate_function_0048ED68.md) (`PAGE` → `.text`)
  - `0x008D4F44` → [sub_0040C640](../../text/40/Unknown_function_0040C640.md) (`PAGE` → `.text`)
  - `0x008D4FA7` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x008D4FD8` → [IoAllocateMdl](../../text/29/IoAllocateMdl_function_0029EBF0.md) (`PAGE` → `.text`)
  - `0x008D4FEE` → [MmProbeAndLockPagesPrivate](../../text/48/MmProbeAndLockPagesPrivate_function_0048ED68.md) (`PAGE` → `.text`)
  - `0x008D50CB` → [sub_0040C640](../../text/40/Unknown_function_0040C640.md) (`PAGE` → `.text`)
  - `0x008D51D9` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x008D5297` → [ZwFlushInstructionCache](../../text/6A/ZwFlushInstructionCache_function_006AEEF0.md) (`PAGE` → `.text`)
  - `0x008D52DC` → [MmUnlockPages](../../text/29/MmUnlockPages_function_0029EEE0.md) (`PAGE` → `.text`)
  - `0x008D52E6` → [IoFreeMdl](../../text/29/IoFreeMdl_function_0029EA80.md) (`PAGE` → `.text`)
  - `0x008D52FE` → [MmUnlockPages](../../text/29/MmUnlockPages_function_0029EEE0.md) (`PAGE` → `.text`)
  - `0x008D5308` → [IoFreeMdl](../../text/29/IoFreeMdl_function_0029EA80.md) (`PAGE` → `.text`)
  - `0x008D5344` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x008D53E4` → [ZwFlushInstructionCache](../../text/6A/ZwFlushInstructionCache_function_006AEEF0.md) (`PAGE` → `.text`)
  - `0x008D5405` → [MmUnlockPages](../../text/29/MmUnlockPages_function_0029EEE0.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **3**
  - `0x008D4CC9` → [sub_00B1B9DE](../B1/Unknown_function_00B1B9DE.md) (`tail-transfer`)
  - `0x008D53FC` → [sub_00B1B9DE + 0x73](../B1/Unknown_function_00B1B9DE.md) (`tail-transfer`)
  - `0x008D540B` → [sub_00B1B9DE + 0x73](../B1/Unknown_function_00B1B9DE.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
008D4BE8  4C 8B DC                        mov r11, rsp
008D4BEB  49 89 5B 20                     mov qword ptr [r11 + 0x20], rbx
008D4BEF  56                              push rsi
008D4BF0  57                              push rdi
008D4BF1  41 54                           push r12
008D4BF3  41 55                           push r13
008D4BF5  41 56                           push r14
008D4BF7  48 81 EC 40 02 00 00            sub rsp, 0x240
008D4BFE  48 8B 05 3B 5B 53 00            mov rax, qword ptr [rip + 0x535b3b]
008D4C05  48 33 C4                        xor rax, rsp
008D4C08  48 89 84 24 30 02 00 00         mov qword ptr [rsp + 0x230], rax
008D4C10  4C 89 84 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], r8
008D4C18  48 8B F2                        mov rsi, rdx
008D4C1B  48 89 8C 24 90 00 00 00         mov qword ptr [rsp + 0x90], rcx
008D4C23  33 FF                           xor edi, edi
008D4C25  48 89 7C 24 50                  mov qword ptr [rsp + 0x50], rdi
008D4C2A  49 89 BB 20 FE FF FF            mov qword ptr [r11 - 0x1e0], rdi
008D4C31  49 89 BB 18 FE FF FF            mov qword ptr [r11 - 0x1e8], rdi
008D4C38  40 88 7C 24 44                  mov byte ptr [rsp + 0x44], dil
008D4C3D  48 89 7C 24 48                  mov qword ptr [rsp + 0x48], rdi
008D4C42  48 89 7C 24 60                  mov qword ptr [rsp + 0x60], rdi
008D4C47  48 89 7C 24 70                  mov qword ptr [rsp + 0x70], rdi
008D4C4C  48 89 7C 24 78                  mov qword ptr [rsp + 0x78], rdi
008D4C51  89 7C 24 58                     mov dword ptr [rsp + 0x58], edi
008D4C55  89 7C 24 68                     mov dword ptr [rsp + 0x68], edi
008D4C59  89 7C 24 6C                     mov dword ptr [rsp + 0x6c], edi
008D4C5D  8B 05 0D 9E 56 00               mov eax, dword ptr [rip + 0x569e0d]
008D4C63  49 89 83 40 FE FF FF            mov qword ptr [r11 - 0x1c0], rax
008D4C6A  8B DF                           mov ebx, edi
008D4C6C  8D 57 58                        lea edx, [rdi + 0x58]
008D4C6F  B9 00 01 00 00                  mov ecx, 0x100
008D4C74  41 B8 57 41 52 42               mov r8d, 0x42524157
008D4C7A  E8 71 D4 2A 00                  call 0x140b820f0
008D4C7F  4C 8B F0                        mov r14, rax
008D4C82  48 85 C0                        test rax, rax
008D4C85  0F 84 09 07 00 00               je 0x1408d5394
008D4C8B  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
008D4C90  4C 8B E0                        mov r12, rax
008D4C93  4C 8B E8                        mov r13, rax
008D4C96  33 C9                           xor ecx, ecx
008D4C98  E8 67 D7 FF FF                  call 0x1408d2404
008D4C9D  85 DB                           test ebx, ebx
008D4C9F  0F 88 24 06 00 00               js 0x1408d52c9
008D4CA5  33 D2                           xor edx, edx
008D4CA7  44 8D 42 58                     lea r8d, [rdx + 0x58]
008D4CAB  49 8B CE                        mov rcx, r14
008D4CAE  E8 8D 1F DF FF                  call 0x1406c6c40
008D4CB3  41 83 64 24 10 FE               and dword ptr [r12 + 0x10], 0xfffffffe
008D4CB9  41 BE 01 00 00 00               mov r14d, 1
008D4CBF  4D 89 75 50                     mov qword ptr [r13 + 0x50], r14
008D4CC3  8B 46 08                        mov eax, dword ptr [rsi + 8]
008D4CC6  41 3B C6                        cmp eax, r14d
008D4CC9  0F 84 0F 6D 24 00               je 0x140b1b9de
008D4CCF  85 C0                           test eax, eax
008D4CD1  0F 85 8B 06 00 00               jne 0x1408d5362
008D4CD7  48 8D 4E 10                     lea rcx, [rsi + 0x10]
008D4CDB  41 BC F0 00 00 00               mov r12d, 0xf0
008D4CE1  41 8B D4                        mov edx, r12d
008D4CE4  E8 43 CF FF FF                  call 0x1408d1c2c
008D4CE9  8B D8                           mov ebx, eax
008D4CEB  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
008D4CEF  85 C0                           test eax, eax
008D4CF1  0F 88 D2 05 00 00               js 0x1408d52c9
008D4CF7  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
008D4CFC  45 33 C9                        xor r9d, r9d
008D4CFF  45 33 C0                        xor r8d, r8d
008D4D02  41 8B D4                        mov edx, r12d
008D4D05  48 8B 8E 48 01 00 00            mov rcx, qword ptr [rsi + 0x148]
008D4D0C  E8 DF 9E 9C FF                  call 0x14029ebf0
008D4D11  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
008D4D16  48 85 C0                        test rax, rax
008D4D19  75 0E                           jne 0x1408d4d29
008D4D1B  BB 17 00 00 C0                  mov ebx, 0xc0000017
008D4D20  89 5C 24 40                     mov dword ptr [rsp + 0x40], ebx
008D4D24  E9 A0 05 00 00                  jmp 0x1408d52c9
008D4D29  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
008D4D2E  E8 35 A0 BB FF                  call 0x14048ed68
008D4D33  44 89 74 24 58                  mov dword ptr [rsp + 0x58], r14d
008D4D38  EB 0D                           jmp 0x1408d4d47
008D4D3A  8B D8                           mov ebx, eax
008D4D3C  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
008D4D40  33 FF                           xor edi, edi
008D4D42  E9 82 05 00 00                  jmp 0x1408d52c9
008D4D47  45 8B C6                        mov r8d, r14d
008D4D4A  41 8B D4                        mov edx, r12d
008D4D4D  48 8B 8E 48 01 00 00            mov rcx, qword ptr [rsi + 0x148]
008D4D54  E8 5F C6 0C 00                  call 0x1409a13b8
008D4D59  85 C0                           test eax, eax
008D4D5B  8B D8                           mov ebx, eax
008D4D5D  0F 88 66 05 00 00               js 0x1408d52c9
008D4D63  4C 8D 8C 24 80 00 00 00         lea r9, [rsp + 0x80]
008D4D6B  4C 8D 84 24 88 00 00 00         lea r8, [rsp + 0x88]
008D4D73  8B 96 40 01 00 00               mov edx, dword ptr [rsi + 0x140]
008D4D79  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
008D4D81  E8 32 BC 0C 00                  call 0x1409a09b8
008D4D86  8B D8                           mov ebx, eax
008D4D88  85 C0                           test eax, eax
008D4D8A  0F 88 39 05 00 00               js 0x1408d52c9
008D4D90  8B 96 40 01 00 00               mov edx, dword ptr [rsi + 0x140]
008D4D96  48 8B C7                        mov rax, rdi
008D4D99  8B DF                           mov ebx, edi
008D4D9B  85 D2                           test edx, edx
008D4D9D  74 19                           je 0x1408d4db8
008D4D9F  B9 00 01 00 00                  mov ecx, 0x100
008D4DA4  41 B8 57 41 52 42               mov r8d, 0x42524157
008D4DAA  E8 41 D3 2A 00                  call 0x140b820f0
008D4DAF  48 85 C0                        test rax, rax
008D4DB2  0F 84 EF 05 00 00               je 0x1408d53a7
008D4DB8  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
008D4DBD  33 C9                           xor ecx, ecx
008D4DBF  E8 40 D6 FF FF                  call 0x1408d2404
008D4DC4  89 5C 24 40                     mov dword ptr [rsp + 0x40], ebx
008D4DC8  85 DB                           test ebx, ebx
008D4DCA  0F 88 F9 04 00 00               js 0x1408d52c9
008D4DD0  8B 86 1C 01 00 00               mov eax, dword ptr [rsi + 0x11c]
008D4DD6  49 BC 00 00 FF FF FF 7F 00 00   movabs r12, 0x7fffffff0000
008D4DE0  85 C0                           test eax, eax
008D4DE2  74 1D                           je 0x1408d4e01
008D4DE4  48 8B 8E 10 01 00 00            mov rcx, qword ptr [rsi + 0x110]
008D4DEB  48 8D 14 01                     lea rdx, [rcx + rax]
008D4DEF  49 3B D4                        cmp rdx, r12
008D4DF2  0F 87 04 03 00 00               ja 0x1408d50fc
008D4DF8  48 3B D1                        cmp rdx, rcx
008D4DFB  0F 82 FB 02 00 00               jb 0x1408d50fc
008D4E01  44 8B 86 1C 01 00 00            mov r8d, dword ptr [rsi + 0x11c]
008D4E08  8B 8E 20 01 00 00               mov ecx, dword ptr [rsi + 0x120]
008D4E0E  48 03 4C 24 48                  add rcx, qword ptr [rsp + 0x48]
008D4E13  48 8B 96 10 01 00 00            mov rdx, qword ptr [rsi + 0x110]
008D4E1A  E8 21 1A DF FF                  call 0x1406c6840
008D4E1F  8B 46 08                        mov eax, dword ptr [rsi + 8]
008D4E22  41 3B C6                        cmp eax, r14d
008D4E25  0F 84 DA 02 00 00               je 0x1408d5105
008D4E2B  85 C0                           test eax, eax
008D4E2D  0F 85 02 03 00 00               jne 0x1408d5135
008D4E33  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
008D4E38  45 33 C9                        xor r9d, r9d
008D4E3B  45 33 C0                        xor r8d, r8d
008D4E3E  8B 96 1C 01 00 00               mov edx, dword ptr [rsi + 0x11c]
008D4E44  48 8B 8E 10 01 00 00            mov rcx, qword ptr [rsi + 0x110]
008D4E4B  E8 A0 9D 9C FF                  call 0x14029ebf0
008D4E50  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
008D4E55  48 85 C0                        test rax, rax
008D4E58  0F 84 E5 02 00 00               je 0x1408d5143
008D4E5E  48 8B C8                        mov rcx, rax
008D4E61  E8 02 9F BB FF                  call 0x14048ed68
008D4E66  44 89 74 24 68                  mov dword ptr [rsp + 0x68], r14d
008D4E6B  44 8B 86 18 01 00 00            mov r8d, dword ptr [rsi + 0x118]
008D4E72  44 8B 8E 1C 01 00 00            mov r9d, dword ptr [rsi + 0x11c]
008D4E79  8B 96 20 01 00 00               mov edx, dword ptr [rsi + 0x120]
008D4E7F  48 03 54 24 48                  add rdx, qword ptr [rsp + 0x48]
008D4E84  48 8D 05 75 DB 72 FF            lea rax, [rip - 0x8d248b]
008D4E8B  48 89 84 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], rax
008D4E93  48 8D 05 56 DB 72 FF            lea rax, [rip - 0x8d24aa]
008D4E9A  48 89 84 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], rax
008D4EA2  89 BC 24 98 00 00 00            mov dword ptr [rsp + 0x98], edi
008D4EA9  48 8D 8C 24 D8 00 00 00         lea rcx, [rsp + 0xd8]
008D4EB1  0F 10 46 60                     movups xmm0, xmmword ptr [rsi + 0x60]
008D4EB5  0F 11 01                        movups xmmword ptr [rcx], xmm0
008D4EB8  0F 10 4E 70                     movups xmm1, xmmword ptr [rsi + 0x70]
008D4EBC  0F 11 49 10                     movups xmmword ptr [rcx + 0x10], xmm1
008D4EC0  0F 10 86 80 00 00 00            movups xmm0, xmmword ptr [rsi + 0x80]
008D4EC7  0F 11 41 20                     movups xmmword ptr [rcx + 0x20], xmm0
008D4ECB  0F 10 8E 90 00 00 00            movups xmm1, xmmword ptr [rsi + 0x90]
008D4ED2  0F 11 49 30                     movups xmmword ptr [rcx + 0x30], xmm1
008D4ED6  0F 10 86 A0 00 00 00            movups xmm0, xmmword ptr [rsi + 0xa0]
008D4EDD  0F 11 41 40                     movups xmmword ptr [rcx + 0x40], xmm0
008D4EE1  0F 10 8E B0 00 00 00            movups xmm1, xmmword ptr [rsi + 0xb0]
008D4EE8  0F 11 49 50                     movups xmmword ptr [rcx + 0x50], xmm1
008D4EEC  0F 10 86 C0 00 00 00            movups xmm0, xmmword ptr [rsi + 0xc0]
008D4EF3  0F 11 41 60                     movups xmmword ptr [rcx + 0x60], xmm0
008D4EF7  41 BA 80 00 00 00               mov r10d, 0x80
008D4EFD  0F 10 86 D0 00 00 00            movups xmm0, xmmword ptr [rsi + 0xd0]
008D4F04  42 0F 11 44 11 F0               movups xmmword ptr [rcx + r10 - 0x10], xmm0
008D4F0A  42 0F 10 4C 16 60               movups xmm1, xmmword ptr [rsi + r10 + 0x60]
008D4F10  42 0F 11 0C 11                  movups xmmword ptr [rcx + r10], xmm1
008D4F15  42 0F 10 44 16 70               movups xmm0, xmmword ptr [rsi + r10 + 0x70]
008D4F1B  42 0F 11 44 11 10               movups xmmword ptr [rcx + r10 + 0x10], xmm0
008D4F21  48 8D 44 24 44                  lea rax, [rsp + 0x44]
008D4F26  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
008D4F2B  44 89 44 24 28                  mov dword ptr [rsp + 0x28], r8d
008D4F30  48 8B 46 58                     mov rax, qword ptr [rsi + 0x58]
008D4F34  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008D4F39  4C 8B C2                        mov r8, rdx
008D4F3C  48 8D 8C 24 D0 00 00 00         lea rcx, [rsp + 0xd0]
008D4F44  E8 F7 76 B3 FF                  call 0x14040c640
008D4F49  89 7C 24 40                     mov dword ptr [rsp + 0x40], edi
008D4F4D  45 8B C6                        mov r8d, r14d
008D4F50  8B 96 1C 01 00 00               mov edx, dword ptr [rsi + 0x11c]
008D4F56  48 8B 8E 10 01 00 00            mov rcx, qword ptr [rsi + 0x110]
008D4F5D  E8 56 C4 0C 00                  call 0x1409a13b8
008D4F62  8B D8                           mov ebx, eax
008D4F64  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
008D4F68  85 C0                           test eax, eax
008D4F6A  0F 88 E1 01 00 00               js 0x1408d5151
008D4F70  48 8B 8E 28 01 00 00            mov rcx, qword ptr [rsi + 0x128]
008D4F77  48 85 C9                        test rcx, rcx
008D4F7A  0F 84 42 02 00 00               je 0x1408d51c2
008D4F80  8B 86 34 01 00 00               mov eax, dword ptr [rsi + 0x134]
008D4F86  85 C0                           test eax, eax
008D4F88  0F 85 C8 01 00 00               jne 0x1408d5156
008D4F8E  44 8B 86 34 01 00 00            mov r8d, dword ptr [rsi + 0x134]
008D4F95  8B 8E 38 01 00 00               mov ecx, dword ptr [rsi + 0x138]
008D4F9B  48 03 4C 24 48                  add rcx, qword ptr [rsp + 0x48]
008D4FA0  48 8B 96 28 01 00 00            mov rdx, qword ptr [rsi + 0x128]
008D4FA7  E8 94 18 DF FF                  call 0x1406c6840
008D4FAC  8B 46 08                        mov eax, dword ptr [rsi + 8]
008D4FAF  41 3B C6                        cmp eax, r14d
008D4FB2  0F 84 B9 01 00 00               je 0x1408d5171
008D4FB8  85 C0                           test eax, eax
008D4FBA  0F 85 E1 01 00 00               jne 0x1408d51a1
008D4FC0  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
008D4FC5  45 33 C9                        xor r9d, r9d
008D4FC8  45 33 C0                        xor r8d, r8d
008D4FCB  8B 96 34 01 00 00               mov edx, dword ptr [rsi + 0x134]
008D4FD1  48 8B 8E 28 01 00 00            mov rcx, qword ptr [rsi + 0x128]
008D4FD8  E8 13 9C 9C FF                  call 0x14029ebf0
008D4FDD  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
008D4FE2  48 85 C0                        test rax, rax
008D4FE5  0F 84 C4 01 00 00               je 0x1408d51af
008D4FEB  48 8B C8                        mov rcx, rax
008D4FEE  E8 75 9D BB FF                  call 0x14048ed68
008D4FF3  44 89 74 24 6C                  mov dword ptr [rsp + 0x6c], r14d
008D4FF8  44 8B 86 30 01 00 00            mov r8d, dword ptr [rsi + 0x130]
008D4FFF  44 8B 8E 34 01 00 00            mov r9d, dword ptr [rsi + 0x134]
008D5006  8B 96 38 01 00 00               mov edx, dword ptr [rsi + 0x138]
008D500C  48 03 54 24 48                  add rdx, qword ptr [rsp + 0x48]
008D5011  48 8D 05 E8 D9 72 FF            lea rax, [rip - 0x8d2618]
008D5018  48 89 84 24 80 01 00 00         mov qword ptr [rsp + 0x180], rax
008D5020  48 8D 05 C9 D9 72 FF            lea rax, [rip - 0x8d2637]
008D5027  48 89 84 24 80 01 00 00         mov qword ptr [rsp + 0x180], rax
008D502F  89 BC 24 9C 00 00 00            mov dword ptr [rsp + 0x9c], edi
008D5036  48 8D 84 24 88 01 00 00         lea rax, [rsp + 0x188]
008D503E  0F 10 46 60                     movups xmm0, xmmword ptr [rsi + 0x60]
008D5042  0F 11 00                        movups xmmword ptr [rax], xmm0
008D5045  0F 10 4E 70                     movups xmm1, xmmword ptr [rsi + 0x70]
008D5049  0F 11 48 10                     movups xmmword ptr [rax + 0x10], xmm1
008D504D  0F 10 86 80 00 00 00            movups xmm0, xmmword ptr [rsi + 0x80]
008D5054  0F 11 40 20                     movups xmmword ptr [rax + 0x20], xmm0
008D5058  0F 10 8E 90 00 00 00            movups xmm1, xmmword ptr [rsi + 0x90]
008D505F  0F 11 48 30                     movups xmmword ptr [rax + 0x30], xmm1
008D5063  0F 10 86 A0 00 00 00            movups xmm0, xmmword ptr [rsi + 0xa0]
008D506A  0F 11 40 40                     movups xmmword ptr [rax + 0x40], xmm0
008D506E  0F 10 8E B0 00 00 00            movups xmm1, xmmword ptr [rsi + 0xb0]
008D5075  0F 11 48 50                     movups xmmword ptr [rax + 0x50], xmm1
008D5079  0F 10 86 C0 00 00 00            movups xmm0, xmmword ptr [rsi + 0xc0]
008D5080  0F 11 40 60                     movups xmmword ptr [rax + 0x60], xmm0
008D5084  B9 80 00 00 00                  mov ecx, 0x80
008D5089  0F 10 8E D0 00 00 00            movups xmm1, xmmword ptr [rsi + 0xd0]
008D5090  0F 11 4C 08 F0                  movups xmmword ptr [rax + rcx - 0x10], xmm1
008D5095  0F 10 44 0E 60                  movups xmm0, xmmword ptr [rsi + rcx + 0x60]
008D509A  0F 11 04 08                     movups xmmword ptr [rax + rcx], xmm0
008D509E  0F 10 4C 0E 70                  movups xmm1, xmmword ptr [rsi + rcx + 0x70]
008D50A3  0F 11 4C 08 10                  movups xmmword ptr [rax + rcx + 0x10], xmm1
008D50A8  48 8D 44 24 44                  lea rax, [rsp + 0x44]
008D50AD  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
008D50B2  44 89 44 24 28                  mov dword ptr [rsp + 0x28], r8d
008D50B7  48 8B 46 58                     mov rax, qword ptr [rsi + 0x58]
008D50BB  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008D50C0  4C 8B C2                        mov r8, rdx
008D50C3  48 8D 8C 24 80 01 00 00         lea rcx, [rsp + 0x180]
008D50CB  E8 70 75 B3 FF                  call 0x14040c640
008D50D0  89 7C 24 40                     mov dword ptr [rsp + 0x40], edi
008D50D4  45 8B C6                        mov r8d, r14d
008D50D7  8B 96 34 01 00 00               mov edx, dword ptr [rsi + 0x134]
008D50DD  48 8B 8E 28 01 00 00            mov rcx, qword ptr [rsi + 0x128]
008D50E4  E8 CF C2 0C 00                  call 0x1409a13b8
008D50E9  8B D8                           mov ebx, eax
008D50EB  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
008D50EF  85 C0                           test eax, eax
008D50F1  0F 88 C6 00 00 00               js 0x1408d51bd
008D50F7  E9 C6 00 00 00                  jmp 0x1408d51c2
008D50FC  41 8A 04 24                     mov al, byte ptr [r12]
008D5100  E9 FC FC FF FF                  jmp 0x1408d4e01
008D5105  83 BE 1C 01 00 00 04            cmp dword ptr [rsi + 0x11c], 4
008D510C  73 0E                           jae 0x1408d511c
008D510E  BB 0D 00 00 C0                  mov ebx, 0xc000000d
008D5113  89 5C 24 40                     mov dword ptr [rsp + 0x40], ebx
008D5117  E9 AD 01 00 00                  jmp 0x1408d52c9
008D511C  8B 96 24 01 00 00               mov edx, dword ptr [rsi + 0x124]
008D5122  8B 8E 20 01 00 00               mov ecx, dword ptr [rsi + 0x120]
008D5128  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
008D512D  89 14 01                        mov dword ptr [rcx + rax], edx
008D5130  E9 FE FC FF FF                  jmp 0x1408d4e33
008D5135  BB 0D 00 00 C0                  mov ebx, 0xc000000d
008D513A  89 5C 24 40                     mov dword ptr [rsp + 0x40], ebx
008D513E  E9 86 01 00 00                  jmp 0x1408d52c9
008D5143  BB 17 00 00 C0                  mov ebx, 0xc0000017
008D5148  89 5C 24 40                     mov dword ptr [rsp + 0x40], ebx
008D514C  E9 78 01 00 00                  jmp 0x1408d52c9
008D5151  E9 73 01 00 00                  jmp 0x1408d52c9
008D5156  48 8D 14 01                     lea rdx, [rcx + rax]
008D515A  49 3B D4                        cmp rdx, r12
008D515D  77 09                           ja 0x1408d5168
008D515F  48 3B D1                        cmp rdx, rcx
008D5162  0F 83 26 FE FF FF               jae 0x1408d4f8e
008D5168  41 8A 04 24                     mov al, byte ptr [r12]
008D516C  E9 1D FE FF FF                  jmp 0x1408d4f8e
008D5171  83 BE 34 01 00 00 04            cmp dword ptr [rsi + 0x134], 4
008D5178  73 0E                           jae 0x1408d5188
008D517A  BB 0D 00 00 C0                  mov ebx, 0xc000000d
008D517F  89 5C 24 40                     mov dword ptr [rsp + 0x40], ebx
008D5183  E9 41 01 00 00                  jmp 0x1408d52c9
008D5188  8B 96 3C 01 00 00               mov edx, dword ptr [rsi + 0x13c]
008D518E  8B 8E 38 01 00 00               mov ecx, dword ptr [rsi + 0x138]
008D5194  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
008D5199  89 14 01                        mov dword ptr [rcx + rax], edx
008D519C  E9 1F FE FF FF                  jmp 0x1408d4fc0
008D51A1  BB 0D 00 00 C0                  mov ebx, 0xc000000d
008D51A6  89 5C 24 40                     mov dword ptr [rsp + 0x40], ebx
008D51AA  E9 1A 01 00 00                  jmp 0x1408d52c9
008D51AF  BB 17 00 00 C0                  mov ebx, 0xc0000017
008D51B4  89 5C 24 40                     mov dword ptr [rsp + 0x40], ebx
008D51B8  E9 0C 01 00 00                  jmp 0x1408d52c9
008D51BD  E9 07 01 00 00                  jmp 0x1408d52c9
008D51C2  44 8B 86 40 01 00 00            mov r8d, dword ptr [rsi + 0x140]
008D51C9  48 8B 54 24 48                  mov rdx, qword ptr [rsp + 0x48]
008D51CE  48 8B 9C 24 88 00 00 00         mov rbx, qword ptr [rsp + 0x88]
008D51D6  48 8B CB                        mov rcx, rbx
008D51D9  E8 62 16 DF FF                  call 0x1406c6840
008D51DE  EB 0D                           jmp 0x1408d51ed
008D51E0  8B D8                           mov ebx, eax
008D51E2  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
008D51E6  33 FF                           xor edi, edi
008D51E8  E9 DC 00 00 00                  jmp 0x1408d52c9
008D51ED  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
008D51F2  4C 8D 51 40                     lea r10, [rcx + 0x40]
008D51F6  48 8B 06                        mov rax, qword ptr [rsi]
008D51F9  49 89 02                        mov qword ptr [r10], rax
008D51FC  48 8D 51 28                     lea rdx, [rcx + 0x28]
008D5200  48 89 1A                        mov qword ptr [rdx], rbx
008D5203  4C 8D 49 18                     lea r9, [rcx + 0x18]
008D5207  8B 86 20 01 00 00               mov eax, dword ptr [rsi + 0x120]
008D520D  48 03 84 24 80 00 00 00         add rax, qword ptr [rsp + 0x80]
008D5215  49 89 01                        mov qword ptr [r9], rax
008D5218  8B 86 38 01 00 00               mov eax, dword ptr [rsi + 0x138]
008D521E  85 C0                           test eax, eax
008D5220  0F 85 9A 01 00 00               jne 0x1408d53c0
008D5226  48 8B C1                        mov rax, rcx
008D5229  48 89 79 20                     mov qword ptr [rcx + 0x20], rdi
008D522D  8B 86 40 01 00 00               mov eax, dword ptr [rsi + 0x140]
008D5233  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
008D5238  89 41 48                        mov dword ptr [rcx + 0x48], eax
008D523B  48 8B 86 10 01 00 00            mov rax, qword ptr [rsi + 0x110]
008D5242  48 89 41 30                     mov qword ptr [rcx + 0x30], rax
008D5246  4C 8B 86 10 01 00 00            mov r8, qword ptr [rsi + 0x110]
008D524D  4D 2B 01                        sub r8, qword ptr [r9]
008D5250  4C 89 41 38                     mov qword ptr [rcx + 0x38], r8
008D5254  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008D525D  48 8B 80 B8 00 00 00            mov rax, qword ptr [rax + 0xb8]
008D5264  48 39 B8 10 03 00 00            cmp qword ptr [rax + 0x310], rdi
008D526B  0F 85 FB 00 00 00               jne 0x1408d536c
008D5271  48 8B 02                        mov rax, qword ptr [rdx]
008D5274  4C 89 00                        mov qword ptr [rax], r8
008D5277  48 8B 02                        mov rax, qword ptr [rdx]
008D527A  48 8B 8C 24 A8 00 00 00         mov rcx, qword ptr [rsp + 0xa8]
008D5282  48 89 48 08                     mov qword ptr [rax + 8], rcx
008D5286  44 8B 86 1C 01 00 00            mov r8d, dword ptr [rsi + 0x11c]
008D528D  49 8B 11                        mov rdx, qword ptr [r9]
008D5290  49 83 CE FF                     or r14, 0xffffffffffffffff
008D5294  49 8B CE                        mov rcx, r14
008D5297  E8 54 9C DD FF                  call 0x1406aeef0
008D529C  8B D8                           mov ebx, eax
008D529E  85 C0                           test eax, eax
008D52A0  78 27                           js 0x1408d52c9
008D52A2  48 39 BE 28 01 00 00            cmp qword ptr [rsi + 0x128], rdi
008D52A9  0F 85 22 01 00 00               jne 0x1408d53d1
008D52AF  48 8B 8C 24 B0 00 00 00         mov rcx, qword ptr [rsp + 0xb0]
008D52B7  48 85 C9                        test rcx, rcx
008D52BA  74 0D                           je 0x1408d52c9
008D52BC  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
008D52C1  48 89 01                        mov qword ptr [rcx], rax
008D52C4  48 89 7C 24 50                  mov qword ptr [rsp + 0x50], rdi
008D52C9  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
008D52CE  48 85 C0                        test rax, rax
008D52D1  74 18                           je 0x1408d52eb
008D52D3  39 7C 24 58                     cmp dword ptr [rsp + 0x58], edi
008D52D7  74 08                           je 0x1408d52e1
008D52D9  48 8B C8                        mov rcx, rax
008D52DC  E8 FF 9B 9C FF                  call 0x14029eee0
008D52E1  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
008D52E6  E8 95 97 9C FF                  call 0x14029ea80
008D52EB  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
008D52F0  48 85 C0                        test rax, rax
008D52F3  74 18                           je 0x1408d530d
008D52F5  39 7C 24 68                     cmp dword ptr [rsp + 0x68], edi
008D52F9  74 08                           je 0x1408d5303
008D52FB  48 8B C8                        mov rcx, rax
008D52FE  E8 DD 9B 9C FF                  call 0x14029eee0
008D5303  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
008D5308  E8 73 97 9C FF                  call 0x14029ea80
008D530D  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
008D5312  48 85 C0                        test rax, rax
008D5315  0F 85 DD 00 00 00               jne 0x1408d53f8
008D531B  48 8B 54 24 50                  mov rdx, qword ptr [rsp + 0x50]
008D5320  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
008D5328  E8 77 D0 FF FF                  call 0x1408d23a4
008D532D  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
008D5332  E8 CD D0 FF FF                  call 0x1408d2404
008D5337  8B C3                           mov eax, ebx
008D5339  48 8B 8C 24 30 02 00 00         mov rcx, qword ptr [rsp + 0x230]
008D5341  48 33 CC                        xor rcx, rsp
008D5344  E8 F7 72 DD FF                  call 0x1406ac640
008D5349  48 8B 9C 24 88 02 00 00         mov rbx, qword ptr [rsp + 0x288]
008D5351  48 81 C4 40 02 00 00            add rsp, 0x240
008D5358  41 5E                           pop r14
008D535A  41 5D                           pop r13
008D535C  41 5C                           pop r12
008D535E  5F                              pop rdi
008D535F  5E                              pop rsi
008D5360  C3                              ret
008D5361  CC                              int3
008D5362  BB 0D 00 00 C0                  mov ebx, 0xc000000d
008D5367  E9 5D FF FF FF                  jmp 0x1408d52c9
008D536C  0F B7 80 EC 06 00 00            movzx eax, word ptr [rax + 0x6ec]
008D5373  B9 4C 01 00 00                  mov ecx, 0x14c
008D5378  66 3B C1                        cmp ax, cx
008D537B  75 34                           jne 0x1408d53b1
008D537D  45 84 F6                        test r14b, r14b
008D5380  0F 84 EB FE FF FF               je 0x1408d5271
008D5386  48 8B 0A                        mov rcx, qword ptr [rdx]
008D5389  49 8B 02                        mov rax, qword ptr [r10]
008D538C  48 89 01                        mov qword ptr [rcx], rax
008D538F  E9 E3 FE FF FF                  jmp 0x1408d5277
008D5394  BB 17 00 00 C0                  mov ebx, 0xc0000017
008D5399  4C 8B F7                        mov r14, rdi
008D539C  4C 8B E7                        mov r12, rdi
008D539F  4C 8B EF                        mov r13, rdi
008D53A2  E9 EF F8 FF FF                  jmp 0x1408d4c96
008D53A7  BB 17 00 00 C0                  mov ebx, 0xc0000017
008D53AC  E9 0C FA FF FF                  jmp 0x1408d4dbd
008D53B1  B9 C4 01 00 00                  mov ecx, 0x1c4
008D53B6  66 3B C1                        cmp ax, cx
008D53B9  74 C2                           je 0x1408d537d
008D53BB  44 8A F7                        mov r14b, dil
008D53BE  EB BD                           jmp 0x1408d537d
008D53C0  48 03 84 24 80 00 00 00         add rax, qword ptr [rsp + 0x80]
008D53C8  48 89 41 20                     mov qword ptr [rcx + 0x20], rax
008D53CC  E9 5C FE FF FF                  jmp 0x1408d522d
008D53D1  44 8B 86 34 01 00 00            mov r8d, dword ptr [rsi + 0x134]
008D53D8  48 8B 54 24 50                  mov rdx, qword ptr [rsp + 0x50]
008D53DD  48 8B 52 20                     mov rdx, qword ptr [rdx + 0x20]
008D53E1  49 8B CE                        mov rcx, r14
008D53E4  E8 07 9B DD FF                  call 0x1406aeef0
008D53E9  8B D8                           mov ebx, eax
008D53EB  85 C0                           test eax, eax
008D53ED  0F 88 D6 FE FF FF               js 0x1408d52c9
008D53F3  E9 B7 FE FF FF                  jmp 0x1408d52af
008D53F8  39 7C 24 6C                     cmp dword ptr [rsp + 0x6c], edi
008D53FC  0F 84 4F 66 24 00               je 0x140b1ba51
008D5402  48 8B C8                        mov rcx, rax
008D5405  E8 D6 9A 9C FF                  call 0x14029eee0
008D540A  90                              nop
008D540B  E9 41 66 24 00                  jmp 0x140b1ba51
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall WbCreateHeapExecutedBlock(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m190;
    unsigned __int64 v_stack_m198;
    unsigned __int64 v_stack_m1B8;
    unsigned __int64 v_stack_m1C0;
    unsigned int v_stack_m1CC;
    unsigned int v_stack_m1D0;
    unsigned __int64 v_stack_m1D8;
    unsigned __int64 v_stack_m1E0;
    unsigned __int64 v_stack_m1E8;
    unsigned __int64 v_stack_m1F0;
    unsigned __int64 v_stack_m1F8;
    unsigned int v_stack_m1FC;
    unsigned int v_stack_m200;
    unsigned __int64 v_stack_m208;
    unsigned int v_stack_m210;
    unsigned __int64 v_stack_m218;
    unsigned __int64 v_stack_m220;
    unsigned __int8 v_stack_m224;
    unsigned int v_stack_m228;
    unsigned __int64 v_stack_m238;
    unsigned int v_stack_m240;
    unsigned __int64 v_stack_m248;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p50;
    unsigned int v_stack_p6C;
    unsigned __int64 v_stack_p80;

    *(unsigned __int64 *)(v_rsp + 32) = v_rbx;
    v_rsp = (v_rsp) - (576);
    result = (*(unsigned __int64 *)(v_rip + 5462843)) ^ (v_rsp);
    v_stack_m38 = result;
    v_stack_m1B8 = a3;
    v_stack_m1D8 = a1;
    v_rdi = 0;
    v_stack_m218 = 0;
    *(unsigned __int64 *)(v_rsp - 480) = 0;
    *(unsigned __int64 *)(v_rsp - 488) = 0;
    v_stack_m224 = 0;
    v_stack_m220 = 0;
    v_stack_m208 = 0;
    v_stack_m1F8 = 0;
    v_stack_m1F0 = 0;
    v_stack_m210 = 0;
    v_stack_m200 = 0;
    v_stack_m1FC = 0;
    *(unsigned __int64 *)(v_rsp - 448) = (unsigned int)(*(unsigned int *)(v_rip + 5676557));
    result = ExAllocatePool2(256, v_rdi + 88, (unsigned int)(0x42524157ULL), a4);
    if (result == 0) goto loc_008D5394;
    v_stack_m218 = result;
loc_008D4C96:
    a1 = 0;
    result = PdcCloseEvent(a1, v_rdi + 88, (unsigned int)(0x42524157ULL), a4);
    if (sign_flag) goto loc_008D52C9;
    a2 = 0;
    result = memset(result, a2, a2 + 88, a4);
    *(unsigned __int64 *)(result + 80) = 1;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 8))) != 0) goto loc_008D5362;
    result = sub_008D1C2C(a2 + 16, 240, a2 + 88, a4);
    v_stack_m228 = (unsigned int)(result);
    if (sign_flag) goto loc_008D52C9;
    v_stack_m248 = 0;
    a4 = 0;
    a3 = 0;
    result = IoAllocateMdl(*(unsigned __int64 *)(a2 + 328), 240, a3, a4);
    v_stack_m208 = result;
    if (result != 0) goto loc_008D4D29;
    v_stack_m228 = (unsigned int)((unsigned int)(0xC0000017ULL));
    goto loc_008D52C9;
loc_008D4D29:
    result = MmProbeAndLockPagesPrivate(v_stack_m208, 240, a3, a4);
    v_stack_m210 = 1;
    goto loc_008D4D47;
loc_008D4D47:
    result = sub_009A13B8(*(unsigned __int64 *)(a2 + 328), 240, 1, a4);
    if (sign_flag) goto loc_008D52C9;
    result = sub_009A09B8(v_stack_m1D8, (unsigned int)(*(unsigned int *)(a2 + 320)), v_stack_m1E0, v_stack_m1E8);
    if (sign_flag) goto loc_008D52C9;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 320))) == 0) goto loc_008D4DB8;
    result = ExAllocatePool2(256, (unsigned int)(*(unsigned int *)(a2 + 320)), (unsigned int)(0x42524157ULL), v_stack_m1E8);
    if (result == 0) goto loc_008D53A7;
loc_008D4DB8:
    v_stack_m220 = result;
loc_008D4DBD:
    a1 = 0;
    result = PdcCloseEvent(a1, (unsigned int)(*(unsigned int *)(a2 + 320)), (unsigned int)(0x42524157ULL), v_stack_m1E8);
    v_stack_m228 = 0;
    if (sign_flag) goto loc_008D52C9;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 284))) == 0) goto loc_008D4E01;
    if ((*(unsigned __int64 *)(a2 + 272) + (unsigned int)(*(unsigned int *)(a2 + 284)) * 1) > 240) goto loc_008D50FC;
    if ((*(unsigned __int64 *)(a2 + 272) + (unsigned int)(*(unsigned int *)(a2 + 284)) * 1) < (*(unsigned __int64 *)(a2 + 272))) goto loc_008D50FC;
loc_008D4E01:
    a1 = ((unsigned int)(*(unsigned int *)(a2 + 288))) + (v_stack_m220);
    result = memcpy(a1, *(unsigned __int64 *)(a2 + 272), (unsigned int)(*(unsigned int *)(a2 + 284)), v_stack_m1E8);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 8)))) == 1) goto loc_008D5105;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 8))) != 0) goto loc_008D5135;
loc_008D4E33:
    v_stack_m248 = 0;
    a4 = 0;
    a3 = 0;
    result = IoAllocateMdl(*(unsigned __int64 *)(a2 + 272), (unsigned int)(*(unsigned int *)(a2 + 284)), a3, a4);
    v_stack_m1F8 = result;
    if (result == 0) goto loc_008D5143;
    result = MmProbeAndLockPagesPrivate(result, (unsigned int)(*(unsigned int *)(a2 + 284)), a3, a4);
    v_stack_m200 = 1;
    a2 = ((unsigned int)(*(unsigned int *)(a2 + 288))) + (v_stack_m220);
    v_stack_m198 = v_rip - 9249931;
    v_stack_m198 = v_rip - 9249962;
    v_stack_m1D0 = 0;
    *(unsigned __int64 *)(v_stack_m190) = v_xmm0;
    *(unsigned __int64 *)(v_stack_m190 + 16) = v_xmm1;
    *(unsigned __int64 *)(v_stack_m190 + 32) = v_xmm0;
    *(unsigned __int64 *)(v_stack_m190 + 48) = v_xmm1;
    *(unsigned __int64 *)(v_stack_m190 + 64) = v_xmm0;
    *(unsigned __int64 *)(v_stack_m190 + 80) = v_xmm1;
    *(unsigned __int64 *)(v_stack_m190 + 96) = v_xmm0;
    *(unsigned __int64 *)(v_stack_m190 + 128 * 1 - 16) = v_xmm0;
    *(unsigned __int64 *)(v_stack_m190 + 128 * 1) = v_xmm1;
    *(unsigned __int64 *)(v_stack_m190 + 128 * 1 + 16) = v_xmm0;
    v_stack_m238 = v_stack_m224;
    v_stack_m240 = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 280)));
    v_stack_m248 = *(unsigned __int64 *)(a2 + 88);
    result = sub_0040C640(v_stack_m198, a2, a2, (unsigned int)(*(unsigned int *)(a2 + 284)));
    v_stack_m228 = 0;
    result = sub_009A13B8(*(unsigned __int64 *)(a2 + 272), (unsigned int)(*(unsigned int *)(a2 + 284)), 1, (unsigned int)(*(unsigned int *)(a2 + 284)));
    v_stack_m228 = (unsigned int)(result);
    if (sign_flag) goto loc_008D5151;
    if (*(unsigned __int64 *)(a2 + 296) == 0) goto loc_008D51C2;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 308))) != 0) goto loc_008D5156;
loc_008D4F8E:
    a1 = ((unsigned int)(*(unsigned int *)(a2 + 312))) + (v_stack_m220);
    result = memcpy(a1, *(unsigned __int64 *)(a2 + 296), (unsigned int)(*(unsigned int *)(a2 + 308)), (unsigned int)(*(unsigned int *)(a2 + 284)));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 8)))) == 1) goto loc_008D5171;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 8))) != 0) goto loc_008D51A1;
loc_008D4FC0:
    v_stack_m248 = 0;
    a4 = 0;
    a3 = 0;
    result = IoAllocateMdl(*(unsigned __int64 *)(a2 + 296), (unsigned int)(*(unsigned int *)(a2 + 308)), a3, a4);
    v_stack_m1F0 = result;
    if (result == 0) goto loc_008D51AF;
    result = MmProbeAndLockPagesPrivate(result, (unsigned int)(*(unsigned int *)(a2 + 308)), a3, a4);
    v_stack_m1FC = 1;
    a2 = ((unsigned int)(*(unsigned int *)(a2 + 312))) + (v_stack_m220);
    v_stack_mE8 = v_rip - 9250328;
    v_stack_mE8 = v_rip - 9250359;
    v_stack_m1CC = 0;
    *(unsigned __int64 *)(v_stack_mE0) = v_xmm0;
    *(unsigned __int64 *)(v_stack_mE0 + 16) = v_xmm1;
    *(unsigned __int64 *)(v_stack_mE0 + 32) = v_xmm0;
    *(unsigned __int64 *)(v_stack_mE0 + 48) = v_xmm1;
    *(unsigned __int64 *)(v_stack_mE0 + 64) = v_xmm0;
    *(unsigned __int64 *)(v_stack_mE0 + 80) = v_xmm1;
    *(unsigned __int64 *)(v_stack_mE0 + 96) = v_xmm0;
    *(unsigned __int64 *)(v_stack_mE0 + 128 * 1 - 16) = v_xmm1;
    *(unsigned __int64 *)(v_stack_mE0 + 128 * 1) = v_xmm0;
    *(unsigned __int64 *)(v_stack_mE0 + 128 * 1 + 16) = v_xmm1;
    v_stack_m238 = v_stack_m224;
    v_stack_m240 = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 304)));
    v_stack_m248 = *(unsigned __int64 *)(a2 + 88);
    result = sub_0040C640(v_stack_mE8, a2, a2, (unsigned int)(*(unsigned int *)(a2 + 308)));
    v_stack_m228 = 0;
    result = sub_009A13B8(*(unsigned __int64 *)(a2 + 296), (unsigned int)(*(unsigned int *)(a2 + 308)), 1, (unsigned int)(*(unsigned int *)(a2 + 308)));
    v_stack_m228 = (unsigned int)(result);
    if (sign_flag) goto loc_008D51BD;
    goto loc_008D51C2;
loc_008D50FC:
    goto loc_008D4E01;
loc_008D5105:
    if ((*(unsigned int *)(a2 + 284)) >= 4) goto loc_008D511C;
    v_stack_m228 = (unsigned int)((unsigned int)(0xC000000DULL));
    goto loc_008D52C9;
loc_008D511C:
    *(unsigned int *)((unsigned int)(*(unsigned int *)(a2 + 288)) + v_stack_m220 * 1) = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 292)));
    goto loc_008D4E33;
loc_008D5135:
    v_stack_m228 = (unsigned int)((unsigned int)(0xC000000DULL));
    goto loc_008D52C9;
loc_008D5143:
    v_stack_m228 = (unsigned int)((unsigned int)(0xC0000017ULL));
    goto loc_008D52C9;
loc_008D5151:
    goto loc_008D52C9;
loc_008D5156:
    if (((unsigned int)(*(unsigned int *)(a2 + 288)) + v_stack_m220 * 1) > 240) goto loc_008D5168;
    if (((unsigned int)(*(unsigned int *)(a2 + 288)) + v_stack_m220 * 1) >= ((unsigned int)(*(unsigned int *)(a2 + 288)))) goto loc_008D4F8E;
loc_008D5168:
    goto loc_008D4F8E;
loc_008D5171:
    if ((*(unsigned int *)(a2 + 308)) >= 4) goto loc_008D5188;
    v_stack_m228 = (unsigned int)((unsigned int)(0xC000000DULL));
    goto loc_008D52C9;
loc_008D5188:
    *(unsigned int *)((unsigned int)(*(unsigned int *)(a2 + 312)) + v_stack_m220 * 1) = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 316)));
    goto loc_008D4FC0;
loc_008D51A1:
    v_stack_m228 = (unsigned int)((unsigned int)(0xC000000DULL));
    goto loc_008D52C9;
loc_008D51AF:
    v_stack_m228 = (unsigned int)((unsigned int)(0xC0000017ULL));
    goto loc_008D52C9;
loc_008D51BD:
    goto loc_008D52C9;
loc_008D51C2:
    result = memcpy(v_stack_m1E0, v_stack_m220, (unsigned int)(*(unsigned int *)(a2 + 320)), (unsigned int)(*(unsigned int *)(a2 + 308)));
    goto loc_008D51ED;
loc_008D51ED:
    *(unsigned __int64 *)(v_stack_m218 + 64) = *(unsigned __int64 *)(a2);
    *(unsigned __int64 *)(v_stack_m218 + 40) = v_stack_m1E0;
    result = ((unsigned int)(*(unsigned int *)(a2 + 288))) + (v_stack_m1E8);
    *(unsigned __int64 *)(v_stack_m218 + 24) = result;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 312))) != 0) goto loc_008D53C0;
    *(unsigned __int64 *)(v_stack_m218 + 32) = 0;
loc_008D522D:
    *(unsigned int *)(v_stack_m218 + 72) = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 320)));
    *(unsigned __int64 *)(v_stack_m218 + 48) = *(unsigned __int64 *)(a2 + 272);
    a3 = (*(unsigned __int64 *)(a2 + 272)) - (*(unsigned __int64 *)(v_stack_m218 + 24));
    *(unsigned __int64 *)(v_stack_m218 + 56) = a3;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 784)) != 0) goto loc_008D536C;
loc_008D5271:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m218 + 40)) = a3;
loc_008D5277:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m218 + 40) + 8) = v_stack_m1C0;
    v_r14 = (1) | (-1);
    result = ZwFlushInstructionCache(v_r14, *(unsigned __int64 *)(v_stack_m218 + 24), (unsigned int)(*(unsigned int *)(a2 + 284)), v_stack_m218 + 24);
    if (sign_flag) goto loc_008D52C9;
    if ((*(unsigned __int64 *)(a2 + 296)) != 0) goto loc_008D53D1;
loc_008D52AF:
    if (v_stack_m1B8 != 0) {
        result = v_stack_m218;
        *(unsigned __int64 *)(v_stack_m1B8) = result;
        v_stack_m218 = 0;
    }
    if (v_stack_m208 == 0) goto loc_008D52EB;
    result = v_stack_m208;
    if (v_stack_m210 != 0) {
        a1 = v_stack_m208;
        result = MmUnlockPages(a1, *(unsigned __int64 *)(v_stack_m218 + 24), (unsigned int)(*(unsigned int *)(a2 + 284)), v_stack_m218 + 24);
    }
    result = IoFreeMdl(v_stack_m208, *(unsigned __int64 *)(v_stack_m218 + 24), (unsigned int)(*(unsigned int *)(a2 + 284)), v_stack_m218 + 24);
loc_008D52EB:
    if (v_stack_m1F8 == 0) goto loc_008D530D;
    result = v_stack_m1F8;
    if (v_stack_m200 != 0) {
        a1 = v_stack_m1F8;
        result = MmUnlockPages(a1, *(unsigned __int64 *)(v_stack_m218 + 24), (unsigned int)(*(unsigned int *)(a2 + 284)), v_stack_m218 + 24);
    }
    result = IoFreeMdl(v_stack_m1F8, *(unsigned __int64 *)(v_stack_m218 + 24), (unsigned int)(*(unsigned int *)(a2 + 284)), v_stack_m218 + 24);
loc_008D530D:
    if (v_stack_m1F0 != 0) goto loc_008D53F8;
    result = sub_008D23A4(v_stack_m1D8, v_stack_m218, (unsigned int)(*(unsigned int *)(a2 + 284)), v_stack_m218 + 24);
    result = PdcCloseEvent(v_stack_m220, v_stack_m218, (unsigned int)(*(unsigned int *)(a2 + 284)), v_stack_m218 + 24);
    a1 = (v_stack_m38) ^ (v_rsp);
    result = _security_check_cookie(a1, v_stack_m218, (unsigned int)(*(unsigned int *)(a2 + 284)), v_stack_m218 + 24);
    v_rsp = (v_rsp) + (576);
    return result;
loc_008D5362:
    goto loc_008D52C9;
loc_008D536C:
    if (((unsigned __int16)(*(unsigned __int16 *)(result + 1772))) != 332) goto loc_008D53B1;
loc_008D537D:
    if ((unsigned __int8)(v_r14) == 0) goto loc_008D5271;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m218)) = *(unsigned __int64 *)(v_stack_m218 + 64);
    goto loc_008D5277;
loc_008D5394:
    goto loc_008D4C96;
loc_008D53A7:
    goto loc_008D4DBD;
loc_008D53B1:
    if (((unsigned __int16)(*(unsigned __int64 *)(v_stack_m218 + 64))) == 452) goto loc_008D537D;
    goto loc_008D537D;
loc_008D53C0:
    result = (*(unsigned __int64 *)(v_stack_m218 + 64)) + (v_stack_p80);
    *(unsigned __int64 *)(452 + 32) = result;
    goto loc_008D522D;
loc_008D53D1:
    result = ZwFlushInstructionCache(0, *(unsigned __int64 *)(v_stack_p50 + 32), (unsigned int)(*(unsigned int *)(a2 + 308)), v_stack_m218 + 24);
    if (sign_flag) goto loc_008D52C9;
    goto loc_008D52AF;
loc_008D53F8:
    result = MmUnlockPages(result, *(unsigned __int64 *)(v_stack_p50 + 32), (unsigned int)(*(unsigned int *)(a2 + 308)), v_stack_m218 + 24);
}
```

## 5. (Beta) C Style

```c
int64_t WbCreateHeapExecutedBlock(int64_t Arg1, void *Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r14;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m190;
    uint64_t v_stack_m198;
    uint64_t v_stack_m1B8;
    uint64_t v_stack_m1C0;
    uint32_t v_stack_m1CC;
    uint32_t v_stack_m1D0;
    uint64_t v_stack_m1D8;
    uint64_t v_stack_m1E0;
    uint64_t v_stack_m1E8;
    uint64_t v_stack_m1F0;
    uint64_t v_stack_m1F8;
    uint32_t v_stack_m1FC;
    uint32_t v_stack_m200;
    uint64_t v_stack_m208;
    uint32_t v_stack_m210;
    uint64_t v_stack_m218;
    uint64_t v_stack_m220;
    uint8_t v_stack_m224;
    uint32_t v_stack_m228;
    uint64_t v_stack_m238;
    uint32_t v_stack_m240;
    uint64_t v_stack_m248;
    uint64_t v_stack_m38;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_p20;
    uint64_t v_stack_p50;
    uint32_t v_stack_p6C;
    uint64_t v_stack_p80;

    *(uint64_t *)(local_rsp + 0x20) = local_rbx;
    local_rsp = (local_rsp) - (576);
    result = (*(uint64_t *)(v_rip + 0x535B3B)) ^ (local_rsp);
    v_stack_m38 = result;
    v_stack_m1B8 = Arg3;
    v_stack_m1D8 = Arg1;
    local_rdi = 0;
    v_stack_m218 = 0;
    *(uint64_t *)(local_rsp - 0x1E0) = 0;
    *(uint64_t *)(local_rsp - 0x1E8) = 0;
    v_stack_m224 = 0;
    v_stack_m220 = 0;
    v_stack_m208 = 0;
    v_stack_m1F8 = 0;
    v_stack_m1F0 = 0;
    v_stack_m210 = 0;
    v_stack_m200 = 0;
    v_stack_m1FC = 0;
    *(uint64_t *)(local_rsp - 0x1C0) = (uint32_t)(*(uint32_t *)(v_rip + 0x569E0D));
    result = ExAllocatePool2(256, local_rdi + 88, (uint32_t)(0x42524157ULL), Arg4);
    if (result == 0) goto loc_008D5394;
    v_stack_m218 = result;
loc_008D4C96:
    Arg1 = 0;
    result = PdcCloseEvent(Arg1, local_rdi + 88, (uint32_t)(0x42524157ULL), Arg4);
    if (sign_flag) goto loc_008D52C9;
    Arg2 = 0;
    result = memset(result, Arg2, Arg2 + 88, Arg4);
    *(uint64_t *)(result + 0x50) = 1;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x8))) != 0) goto loc_008D5362;
    result = sub_008D1C2C(Arg2 + 16, 240, Arg2 + 88, Arg4);
    v_stack_m228 = (uint32_t)(result);
    if (sign_flag) goto loc_008D52C9;
    v_stack_m248 = 0;
    Arg4 = 0;
    Arg3 = 0;
    result = IoAllocateMdl(*(uint64_t *)(arg2 + 0x148), 240, Arg3, Arg4);
    v_stack_m208 = result;
    if (result != 0) goto loc_008D4D29;
    v_stack_m228 = (uint32_t)((uint32_t)(0xC0000017ULL));
    goto loc_008D52C9;
loc_008D4D29:
    result = MmProbeAndLockPagesPrivate(v_stack_m208, 240, Arg3, Arg4);
    v_stack_m210 = 1;
    goto loc_008D4D47;
loc_008D4D47:
    result = sub_009A13B8(*(uint64_t *)(arg2 + 0x148), 240, 1, Arg4);
    if (sign_flag) goto loc_008D52C9;
    result = sub_009A09B8(v_stack_m1D8, (uint32_t)(*(uint32_t *)(arg2 + 0x140)), v_stack_m1E0, v_stack_m1E8);
    if (sign_flag) goto loc_008D52C9;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x140))) == 0) goto loc_008D4DB8;
    result = ExAllocatePool2(256, (uint32_t)(*(uint32_t *)(arg2 + 0x140)), (uint32_t)(0x42524157ULL), v_stack_m1E8);
    if (result == 0) goto loc_008D53A7;
loc_008D4DB8:
    v_stack_m220 = result;
loc_008D4DBD:
    Arg1 = 0;
    result = PdcCloseEvent(Arg1, (uint32_t)(*(uint32_t *)(arg2 + 0x140)), (uint32_t)(0x42524157ULL), v_stack_m1E8);
    v_stack_m228 = 0;
    if (sign_flag) goto loc_008D52C9;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x11C))) == 0) goto loc_008D4E01;
    if ((*(uint64_t *)(arg2 + 0x110) + (uint32_t)(*(uint32_t *)(arg2 + 0x11C)) * 1) > 240) goto loc_008D50FC;
    if ((*(uint64_t *)(arg2 + 0x110) + (uint32_t)(*(uint32_t *)(arg2 + 0x11C)) * 1) < (*(uint64_t *)(arg2 + 0x110))) goto loc_008D50FC;
loc_008D4E01:
    Arg1 = ((uint32_t)(*(uint32_t *)(arg2 + 0x120))) + (v_stack_m220);
    result = memcpy(Arg1, *(uint64_t *)(arg2 + 0x110), (uint32_t)(*(uint32_t *)(arg2 + 0x11C)), v_stack_m1E8);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x8)))) == 1) goto loc_008D5105;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x8))) != 0) goto loc_008D5135;
loc_008D4E33:
    v_stack_m248 = 0;
    Arg4 = 0;
    Arg3 = 0;
    result = IoAllocateMdl(*(uint64_t *)(arg2 + 0x110), (uint32_t)(*(uint32_t *)(arg2 + 0x11C)), Arg3, Arg4);
    v_stack_m1F8 = result;
    if (result == 0) goto loc_008D5143;
    result = MmProbeAndLockPagesPrivate(result, (uint32_t)(*(uint32_t *)(arg2 + 0x11C)), Arg3, Arg4);
    v_stack_m200 = 1;
    Arg2 = ((uint32_t)(*(uint32_t *)(arg2 + 0x120))) + (v_stack_m220);
    v_stack_m198 = v_rip - 9249931;
    v_stack_m198 = v_rip - 9249962;
    v_stack_m1D0 = 0;
    *(uint64_t *)(v_stack_m190) = v_xmm0;
    *(uint64_t *)(v_stack_m190 + 0x10) = v_xmm1;
    *(uint64_t *)(v_stack_m190 + 0x20) = v_xmm0;
    *(uint64_t *)(v_stack_m190 + 0x30) = v_xmm1;
    *(uint64_t *)(v_stack_m190 + 0x40) = v_xmm0;
    *(uint64_t *)(v_stack_m190 + 0x50) = v_xmm1;
    *(uint64_t *)(v_stack_m190 + 0x60) = v_xmm0;
    *(uint64_t *)(v_stack_m190 + 0x80 * 1 - 0x10) = v_xmm0;
    *(uint64_t *)(v_stack_m190 + 0x80 * 1) = v_xmm1;
    *(uint64_t *)(v_stack_m190 + 0x80 * 1 + 0x10) = v_xmm0;
    v_stack_m238 = v_stack_m224;
    v_stack_m240 = (uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x118)));
    v_stack_m248 = *(uint64_t *)(arg2 + 0x58);
    result = sub_0040C640(v_stack_m198, Arg2, Arg2, (uint32_t)(*(uint32_t *)(arg2 + 0x11C)));
    v_stack_m228 = 0;
    result = sub_009A13B8(*(uint64_t *)(arg2 + 0x110), (uint32_t)(*(uint32_t *)(arg2 + 0x11C)), 1, (uint32_t)(*(uint32_t *)(arg2 + 0x11C)));
    v_stack_m228 = (uint32_t)(result);
    if (sign_flag) goto loc_008D5151;
    if (*(uint64_t *)(arg2 + 0x128) == 0) goto loc_008D51C2;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x134))) != 0) goto loc_008D5156;
loc_008D4F8E:
    Arg1 = ((uint32_t)(*(uint32_t *)(arg2 + 0x138))) + (v_stack_m220);
    result = memcpy(Arg1, *(uint64_t *)(arg2 + 0x128), (uint32_t)(*(uint32_t *)(arg2 + 0x134)), (uint32_t)(*(uint32_t *)(arg2 + 0x11C)));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x8)))) == 1) goto loc_008D5171;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x8))) != 0) goto loc_008D51A1;
loc_008D4FC0:
    v_stack_m248 = 0;
    Arg4 = 0;
    Arg3 = 0;
    result = IoAllocateMdl(*(uint64_t *)(arg2 + 0x128), (uint32_t)(*(uint32_t *)(arg2 + 0x134)), Arg3, Arg4);
    v_stack_m1F0 = result;
    if (result == 0) goto loc_008D51AF;
    result = MmProbeAndLockPagesPrivate(result, (uint32_t)(*(uint32_t *)(arg2 + 0x134)), Arg3, Arg4);
    v_stack_m1FC = 1;
    Arg2 = ((uint32_t)(*(uint32_t *)(arg2 + 0x138))) + (v_stack_m220);
    v_stack_mE8 = v_rip - 9250328;
    v_stack_mE8 = v_rip - 9250359;
    v_stack_m1CC = 0;
    *(uint64_t *)(v_stack_mE0) = v_xmm0;
    *(uint64_t *)(v_stack_mE0 + 0x10) = v_xmm1;
    *(uint64_t *)(v_stack_mE0 + 0x20) = v_xmm0;
    *(uint64_t *)(v_stack_mE0 + 0x30) = v_xmm1;
    *(uint64_t *)(v_stack_mE0 + 0x40) = v_xmm0;
    *(uint64_t *)(v_stack_mE0 + 0x50) = v_xmm1;
    *(uint64_t *)(v_stack_mE0 + 0x60) = v_xmm0;
    *(uint64_t *)(v_stack_mE0 + 0x80 * 1 - 0x10) = v_xmm1;
    *(uint64_t *)(v_stack_mE0 + 0x80 * 1) = v_xmm0;
    *(uint64_t *)(v_stack_mE0 + 0x80 * 1 + 0x10) = v_xmm1;
    v_stack_m238 = v_stack_m224;
    v_stack_m240 = (uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x130)));
    v_stack_m248 = *(uint64_t *)(arg2 + 0x58);
    result = sub_0040C640(v_stack_mE8, Arg2, Arg2, (uint32_t)(*(uint32_t *)(arg2 + 0x134)));
    v_stack_m228 = 0;
    result = sub_009A13B8(*(uint64_t *)(arg2 + 0x128), (uint32_t)(*(uint32_t *)(arg2 + 0x134)), 1, (uint32_t)(*(uint32_t *)(arg2 + 0x134)));
    v_stack_m228 = (uint32_t)(result);
    if (sign_flag) goto loc_008D51BD;
    goto loc_008D51C2;
loc_008D50FC:
    goto loc_008D4E01;
loc_008D5105:
    if ((*(uint32_t *)(arg2 + 0x11C)) >= 4) goto loc_008D511C;
    v_stack_m228 = (uint32_t)((uint32_t)(0xC000000DULL));
    goto loc_008D52C9;
loc_008D511C:
    *(uint32_t *)((uint32_t)(*(uint32_t *)(arg2 + 0x120)) + v_stack_m220 * 1) = (uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x124)));
    goto loc_008D4E33;
loc_008D5135:
    v_stack_m228 = (uint32_t)((uint32_t)(0xC000000DULL));
    goto loc_008D52C9;
loc_008D5143:
    v_stack_m228 = (uint32_t)((uint32_t)(0xC0000017ULL));
    goto loc_008D52C9;
loc_008D5151:
    goto loc_008D52C9;
loc_008D5156:
    if (((uint32_t)(*(uint32_t *)(arg2 + 0x120)) + v_stack_m220 * 1) > 240) goto loc_008D5168;
    if (((uint32_t)(*(uint32_t *)(arg2 + 0x120)) + v_stack_m220 * 1) >= ((uint32_t)(*(uint32_t *)(arg2 + 0x120)))) goto loc_008D4F8E;
loc_008D5168:
    goto loc_008D4F8E;
loc_008D5171:
    if ((*(uint32_t *)(arg2 + 0x134)) >= 4) goto loc_008D5188;
    v_stack_m228 = (uint32_t)((uint32_t)(0xC000000DULL));
    goto loc_008D52C9;
loc_008D5188:
    *(uint32_t *)((uint32_t)(*(uint32_t *)(arg2 + 0x138)) + v_stack_m220 * 1) = (uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x13C)));
    goto loc_008D4FC0;
loc_008D51A1:
    v_stack_m228 = (uint32_t)((uint32_t)(0xC000000DULL));
    goto loc_008D52C9;
loc_008D51AF:
    v_stack_m228 = (uint32_t)((uint32_t)(0xC0000017ULL));
    goto loc_008D52C9;
loc_008D51BD:
    goto loc_008D52C9;
loc_008D51C2:
    result = memcpy(v_stack_m1E0, v_stack_m220, (uint32_t)(*(uint32_t *)(arg2 + 0x140)), (uint32_t)(*(uint32_t *)(arg2 + 0x134)));
    goto loc_008D51ED;
loc_008D51ED:
    *(uint64_t *)(v_stack_m218 + 0x40) = *(uint64_t *)(arg2);
    *(uint64_t *)(v_stack_m218 + 0x28) = v_stack_m1E0;
    result = ((uint32_t)(*(uint32_t *)(arg2 + 0x120))) + (v_stack_m1E8);
    *(uint64_t *)(v_stack_m218 + 0x18) = result;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x138))) != 0) goto loc_008D53C0;
    *(uint64_t *)(v_stack_m218 + 0x20) = 0;
loc_008D522D:
    *(uint32_t *)(v_stack_m218 + 0x48) = (uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x140)));
    *(uint64_t *)(v_stack_m218 + 0x30) = *(uint64_t *)(arg2 + 0x110);
    Arg3 = (*(uint64_t *)(arg2 + 0x110)) - (*(uint64_t *)(v_stack_m218 + 0x18));
    *(uint64_t *)(v_stack_m218 + 0x38) = Arg3;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x310)) != 0) goto loc_008D536C;
loc_008D5271:
    *(uint64_t *)(*(uint64_t *)(v_stack_m218 + 0x28)) = Arg3;
loc_008D5277:
    *(uint64_t *)(*(uint64_t *)(v_stack_m218 + 0x28) + 0x8) = v_stack_m1C0;
    local_r14 = (1) | (-1);
    result = ZwFlushInstructionCache(local_r14, *(uint64_t *)(v_stack_m218 + 0x18), (uint32_t)(*(uint32_t *)(arg2 + 0x11C)), v_stack_m218 + 24);
    if (sign_flag) goto loc_008D52C9;
    if ((*(uint64_t *)(arg2 + 0x128)) != 0) goto loc_008D53D1;
loc_008D52AF:
    if (v_stack_m1B8 != 0) {
        result = v_stack_m218;
        *(uint64_t *)(v_stack_m1B8) = result;
        v_stack_m218 = 0;
    }
    if (v_stack_m208 == 0) goto loc_008D52EB;
    result = v_stack_m208;
    if (v_stack_m210 != 0) {
        Arg1 = v_stack_m208;
        result = MmUnlockPages(Arg1, *(uint64_t *)(v_stack_m218 + 0x18), (uint32_t)(*(uint32_t *)(arg2 + 0x11C)), v_stack_m218 + 24);
    }
    result = IoFreeMdl(v_stack_m208, *(uint64_t *)(v_stack_m218 + 0x18), (uint32_t)(*(uint32_t *)(arg2 + 0x11C)), v_stack_m218 + 24);
loc_008D52EB:
    if (v_stack_m1F8 == 0) goto loc_008D530D;
    result = v_stack_m1F8;
    if (v_stack_m200 != 0) {
        Arg1 = v_stack_m1F8;
        result = MmUnlockPages(Arg1, *(uint64_t *)(v_stack_m218 + 0x18), (uint32_t)(*(uint32_t *)(arg2 + 0x11C)), v_stack_m218 + 24);
    }
    result = IoFreeMdl(v_stack_m1F8, *(uint64_t *)(v_stack_m218 + 0x18), (uint32_t)(*(uint32_t *)(arg2 + 0x11C)), v_stack_m218 + 24);
loc_008D530D:
    if (v_stack_m1F0 != 0) goto loc_008D53F8;
    result = sub_008D23A4(v_stack_m1D8, v_stack_m218, (uint32_t)(*(uint32_t *)(arg2 + 0x11C)), v_stack_m218 + 24);
    result = PdcCloseEvent(v_stack_m220, v_stack_m218, (uint32_t)(*(uint32_t *)(arg2 + 0x11C)), v_stack_m218 + 24);
    Arg1 = (v_stack_m38) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_stack_m218, (uint32_t)(*(uint32_t *)(arg2 + 0x11C)), v_stack_m218 + 24);
    local_rsp = (local_rsp) + (576);
    return result;
loc_008D5362:
    goto loc_008D52C9;
loc_008D536C:
    if (((uint16_t)(*(uint16_t *)(result + 0x6EC))) != 332) goto loc_008D53B1;
loc_008D537D:
    if ((uint8_t)(local_r14) == 0) goto loc_008D5271;
    *(uint64_t *)(*(uint64_t *)(v_stack_m218)) = *(uint64_t *)(v_stack_m218 + 0x40);
    goto loc_008D5277;
loc_008D5394:
    goto loc_008D4C96;
loc_008D53A7:
    goto loc_008D4DBD;
loc_008D53B1:
    if (((uint16_t)(*(uint64_t *)(v_stack_m218 + 0x40))) == 452) goto loc_008D537D;
    goto loc_008D537D;
loc_008D53C0:
    result = (*(uint64_t *)(v_stack_m218 + 0x40)) + (v_stack_p80);
    *(uint64_t *)(452 + 0x20) = result;
    goto loc_008D522D;
loc_008D53D1:
    result = ZwFlushInstructionCache(0, *(uint64_t *)(v_stack_p50 + 0x20), (uint32_t)(*(uint32_t *)(arg2 + 0x134)), v_stack_m218 + 24);
    if (sign_flag) goto loc_008D52C9;
    goto loc_008D52AF;
loc_008D53F8:
    result = MmUnlockPages(result, *(uint64_t *)(v_stack_p50 + 0x20), (uint32_t)(*(uint32_t *)(arg2 + 0x134)), v_stack_m218 + 24);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `64` | `R` |
| `Arg2` | `+ 0x8` | `32` | `R` |
| `Arg2` | `+ 0x10` | `64` | `R` |
| `Arg2` | `+ 0x58` | `64` | `R` |
| `Arg2` | `+ 0x60` | `128` | `R` |
| `Arg2` | `+ 0x60 + r10*1` | `128` | `R` |
| `Arg2` | `+ 0x60 + rcx*1` | `128` | `R` |
| `Arg2` | `+ 0x70` | `128` | `R` |
| `Arg2` | `+ 0x70 + r10*1` | `128` | `R` |
| `Arg2` | `+ 0x70 + rcx*1` | `128` | `R` |
| `Arg2` | `+ 0x80` | `128` | `R` |
| `Arg2` | `+ 0x90` | `128` | `R` |
| `Arg2` | `+ 0xA0` | `128` | `R` |
| `Arg2` | `+ 0xB0` | `128` | `R` |
| `Arg2` | `+ 0xC0` | `128` | `R` |
| `Arg2` | `+ 0xD0` | `128` | `R` |
| `Arg2` | `+ 0x110` | `64` | `R` |
| `Arg2` | `+ 0x118` | `32` | `R` |
| `Arg2` | `+ 0x11C` | `32` | `R` |
| `Arg2` | `+ 0x120` | `32` | `R` |
| `Arg2` | `+ 0x124` | `32` | `R` |
| `Arg2` | `+ 0x128` | `64` | `R` |
| `Arg2` | `+ 0x130` | `32` | `R` |
| `Arg2` | `+ 0x134` | `32` | `R` |
| `Arg2` | `+ 0x138` | `32` | `R` |
| `Arg2` | `+ 0x13C` | `32` | `R` |
| `Arg2` | `+ 0x140` | `32` | `R` |
| `Arg2` | `+ 0x148` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008D4BE8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
