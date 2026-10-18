# PiDrvDbOverlayNodeHive

- RVA: `0x00741990`–`0x00741DD6` (길이 `1,094` bytes)
- VA: `0x0000000140741990`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C9364`
- 디코드: `293`개 명령, `1,094/1,094` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **23**; 고유 호출 대상: **11**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **9**

### Outgoing calls
- `0x007419D5` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00741A07` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (function, `0x00500080`)
- `0x00741A6A` → [PnpCtxRegOpenKey](../8E/PnpCtxRegOpenKey_function_008EF7B8.md) (function, `0x008EF7B8`)
- `0x00741A99` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (function, `0x00500080`)
- `0x00741AE7` → [PnpCtxRegOpenKey](../8E/PnpCtxRegOpenKey_function_008EF7B8.md) (function, `0x008EF7B8`)
- `0x00741B20` → [PnpCtxRegOpenKey](../8E/PnpCtxRegOpenKey_function_008EF7B8.md) (function, `0x008EF7B8`)
- `0x00741B58` → [PnpCtxRegOpenKey](../8E/PnpCtxRegOpenKey_function_008EF7B8.md) (function, `0x008EF7B8`)
- `0x00741B89` → [PiDrvDbOverlayCopyKeys](PiDrvDbOverlayCopyKeys_function_007413FC.md) (function, `0x007413FC`)
- `0x00741BB2` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00741BF9` → [PnpCtxRegOpenKey](../8E/PnpCtxRegOpenKey_function_008EF7B8.md) (function, `0x008EF7B8`)
- `0x00741C2F` → [PnpCtxRegQueryValue](../99/PnpCtxRegQueryValue_function_009940FC.md) (function, `0x009940FC`)
- `0x00741C66` → [PnpCtxRegQueryValue](../99/PnpCtxRegQueryValue_function_009940FC.md) (function, `0x009940FC`)
- `0x00741C98` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x00741CFC` → [PnpCtxRegCreateKey](../A6/PnpCtxRegCreateKey_function_00A692E4.md) (function, `0x00A692E4`)
- `0x00741D24` → [PiDrvDbOverlayCopyKeys](PiDrvDbOverlayCopyKeys_function_007413FC.md) (function, `0x007413FC`)
- `0x00741D4C` → [PnpCtxRegEnumKey](../99/PnpCtxRegEnumKey_function_009929C0.md) (function, `0x009929C0`)
- `0x00741D61` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00741D6F` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x00741D7D` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x00741D8B` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x00741D99` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x00741DA7` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x00741DB5` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PiDrvDbSetupNodeHive](PiDrvDbSetupNodeHive_function_00743884.md) at `0x00743CA5`

### Static image references
- `0x007419AC` → RVA `0x00E0A740` (`.data`; read)
- `0x007419DA` → RVA `0x00AFF500` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00741A0C` → RVA `0x00B00560` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00741A2C` → RVA `0x00B4C008` (`PAGE`; read)
- `0x00741A8F` → RVA `0x00AFF430` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00741AB3` → RVA `0x00AFF170` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00741AC0` → RVA `0x00B00590` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00741C20` → RVA `0x00AFC720` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00741C5A` → RVA `0x00AFDF50` (` ?? ::NNGAKEGL::`string'`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **12**
  - `0x007419D5` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00741A07` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (`PAGE` → `.text`)
  - `0x00741A99` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (`PAGE` → `.text`)
  - `0x00741BB2` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00741C98` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x00741D61` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00741D6F` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x00741D7D` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x00741D8B` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x00741D99` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x00741DA7` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x00741DB5` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00741990  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00741995  55                              push rbp
00741996  56                              push rsi
00741997  57                              push rdi
00741998  41 54                           push r12
0074199A  41 55                           push r13
0074199C  41 56                           push r14
0074199E  41 57                           push r15
007419A0  48 8D 6C 24 D9                  lea rbp, [rsp - 0x27]
007419A5  48 81 EC D0 00 00 00            sub rsp, 0xd0
007419AC  48 8B 05 8D 8D 6C 00            mov rax, qword ptr [rip + 0x6c8d8d]
007419B3  48 33 C4                        xor rax, rsp
007419B6  48 89 45 17                     mov qword ptr [rbp + 0x17], rax
007419BA  45 33 E4                        xor r12d, r12d
007419BD  4D 8B F0                        mov r14, r8
007419C0  48 8B F2                        mov rsi, rdx
007419C3  4C 89 65 CF                     mov qword ptr [rbp - 0x31], r12
007419C7  4C 8B E9                        mov r13, rcx
007419CA  33 D2                           xor edx, edx
007419CC  48 8D 4D D7                     lea rcx, [rbp - 0x29]
007419D0  45 8D 44 24 40                  lea r8d, [r12 + 0x40]
007419D5  E8 66 52 F8 FF                  call 0x1406c6c40
007419DA  48 8D 15 1F DB 3B 00            lea rdx, [rip + 0x3bdb1f]
007419E1  4C 89 65 BF                     mov qword ptr [rbp - 0x41], r12
007419E5  48 8B CE                        mov rcx, rsi
007419E8  4C 89 65 B7                     mov qword ptr [rbp - 0x49], r12
007419EC  41 8B FC                        mov edi, r12d
007419EF  4C 89 65 A7                     mov qword ptr [rbp - 0x59], r12
007419F3  4C 89 65 C7                     mov qword ptr [rbp - 0x39], r12
007419F7  4C 89 65 AF                     mov qword ptr [rbp - 0x51], r12
007419FB  44 89 65 9F                     mov dword ptr [rbp - 0x61], r12d
007419FF  44 89 65 A3                     mov dword ptr [rbp - 0x5d], r12d
00741A03  44 89 65 9B                     mov dword ptr [rbp - 0x65], r12d
00741A07  E8 74 E6 DB FF                  call 0x140500080
00741A0C  4C 8D 3D 4D EB 3B 00            lea r15, [rip + 0x3beb4d]
00741A13  85 C0                           test eax, eax
00741A15  75 78                           jne 0x140741a8f
00741A17  45 8B 85 EC 01 00 00            mov r8d, dword ptr [r13 + 0x1ec]
00741A1E  41 F6 C0 10                     test r8b, 0x10
00741A22  75 08                           jne 0x140741a2c
00741A24  41 8B DC                        mov ebx, r12d
00741A27  E9 3A 03 00 00                  jmp 0x140741d66
00741A2C  48 8D 15 D5 A5 40 00            lea rdx, [rip + 0x40a5d5]
00741A33  48 8B 02                        mov rax, qword ptr [rdx]
00741A36  48 8D 52 08                     lea rdx, [rdx + 8]
00741A3A  8B CF                           mov ecx, edi
00741A3C  FF C7                           inc edi
00741A3E  48 89 44 CD D7                  mov qword ptr [rbp + rcx*8 - 0x29], rax
00741A43  83 FF 04                        cmp edi, 4
00741A46  72 EB                           jb 0x140741a33
00741A48  41 F6 C0 C0                     test r8b, 0xc0
00741A4C  74 38                           je 0x140741a86
00741A4E  48 8D 45 A7                     lea rax, [rbp - 0x59]
00741A52  45 33 C9                        xor r9d, r9d
00741A55  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00741A5A  4D 8B C7                        mov r8, r15
00741A5D  49 8B D6                        mov rdx, r14
00741A60  C7 44 24 20 19 00 02 00         mov dword ptr [rsp + 0x20], 0x20019
00741A68  33 C9                           xor ecx, ecx
00741A6A  E8 49 DD 1A 00                  call 0x1408ef7b8
00741A6F  8B D8                           mov ebx, eax
00741A71  3D 34 00 00 C0                  cmp eax, 0xc0000034
00741A76  75 06                           jne 0x140741a7e
00741A78  4C 89 65 A7                     mov qword ptr [rbp - 0x59], r12
00741A7C  EB 08                           jmp 0x140741a86
00741A7E  85 C0                           test eax, eax
00741A80  0F 88 E0 02 00 00               js 0x140741d66
00741A86  4C 89 7C FD D7                  mov qword ptr [rbp + rdi*8 - 0x29], r15
00741A8B  FF C7                           inc edi
00741A8D  EB 22                           jmp 0x140741ab1
00741A8F  48 8D 15 9A D9 3B 00            lea rdx, [rip + 0x3bd99a]
00741A96  48 8B CE                        mov rcx, rsi
00741A99  E8 E2 E5 DB FF                  call 0x140500080
00741A9E  85 C0                           test eax, eax
00741AA0  75 0F                           jne 0x140741ab1
00741AA2  41 8B 85 EC 01 00 00            mov eax, dword ptr [r13 + 0x1ec]
00741AA9  A8 20                           test al, 0x20
00741AAB  0F 84 73 FF FF FF               je 0x140741a24
00741AB1  8B C7                           mov eax, edi
00741AB3  48 8D 0D B6 D6 3B 00            lea rcx, [rip + 0x3bd6b6]
00741ABA  41 BF 02 00 00 80               mov r15d, 0x80000002
00741AC0  4C 8D 05 C9 EA 3B 00            lea r8, [rip + 0x3beac9]
00741AC7  45 33 C9                        xor r9d, r9d
00741ACA  41 8B D7                        mov edx, r15d
00741ACD  FF C7                           inc edi
00741ACF  48 89 4C C5 D7                  mov qword ptr [rbp + rax*8 - 0x29], rcx
00741AD4  48 8D 45 BF                     lea rax, [rbp - 0x41]
00741AD8  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00741ADD  33 C9                           xor ecx, ecx
00741ADF  C7 44 24 20 19 00 02 00         mov dword ptr [rsp + 0x20], 0x20019
00741AE7  E8 CC DC 1A 00                  call 0x1408ef7b8
00741AEC  8B D8                           mov ebx, eax
00741AEE  3D 34 00 00 C0                  cmp eax, 0xc0000034
00741AF3  75 06                           jne 0x140741afb
00741AF5  4C 89 65 BF                     mov qword ptr [rbp - 0x41], r12
00741AF9  EB 41                           jmp 0x140741b3c
00741AFB  85 C0                           test eax, eax
00741AFD  0F 88 63 02 00 00               js 0x140741d66
00741B03  48 8B 55 BF                     mov rdx, qword ptr [rbp - 0x41]
00741B07  48 8D 45 B7                     lea rax, [rbp - 0x49]
00741B0B  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00741B10  45 33 C9                        xor r9d, r9d
00741B13  4C 8B C6                        mov r8, rsi
00741B16  C7 44 24 20 19 00 02 00         mov dword ptr [rsp + 0x20], 0x20019
00741B1E  33 C9                           xor ecx, ecx
00741B20  E8 93 DC 1A 00                  call 0x1408ef7b8
00741B25  8B D8                           mov ebx, eax
00741B27  3D 34 00 00 C0                  cmp eax, 0xc0000034
00741B2C  75 06                           jne 0x140741b34
00741B2E  4C 89 65 B7                     mov qword ptr [rbp - 0x49], r12
00741B32  EB 08                           jmp 0x140741b3c
00741B34  85 C0                           test eax, eax
00741B36  0F 88 2A 02 00 00               js 0x140741d66
00741B3C  48 8D 45 CF                     lea rax, [rbp - 0x31]
00741B40  45 33 C9                        xor r9d, r9d
00741B43  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00741B48  4C 8B C6                        mov r8, rsi
00741B4B  49 8B D7                        mov rdx, r15
00741B4E  C7 44 24 20 1F 00 02 00         mov dword ptr [rsp + 0x20], 0x2001f
00741B56  33 C9                           xor ecx, ecx
00741B58  E8 5B DC 1A 00                  call 0x1408ef7b8
00741B5D  8B D8                           mov ebx, eax
00741B5F  85 C0                           test eax, eax
00741B61  0F 88 FF 01 00 00               js 0x140741d66
00741B67  48 8B 45 B7                     mov rax, qword ptr [rbp - 0x49]
00741B6B  45 33 C9                        xor r9d, r9d
00741B6E  4C 8B 45 CF                     mov r8, qword ptr [rbp - 0x31]
00741B72  33 D2                           xor edx, edx
00741B74  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00741B79  49 8B CE                        mov rcx, r14
00741B7C  48 8D 45 D7                     lea rax, [rbp - 0x29]
00741B80  89 7C 24 30                     mov dword ptr [rsp + 0x30], edi
00741B84  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00741B89  E8 6E F8 FF FF                  call 0x1407413fc
00741B8E  8B D8                           mov ebx, eax
00741B90  85 C0                           test eax, eax
00741B92  0F 88 CE 01 00 00               js 0x140741d66
00741B98  4C 39 65 A7                     cmp qword ptr [rbp - 0x59], r12
00741B9C  0F 84 C4 01 00 00               je 0x140741d66
00741BA2  BA 08 02 00 00                  mov edx, 0x208
00741BA7  B9 00 01 00 00                  mov ecx, 0x100
00741BAC  41 B8 50 70 64 62               mov r8d, 0x62647050
00741BB2  E8 39 05 44 00                  call 0x140b820f0
00741BB7  4C 8B F0                        mov r14, rax
00741BBA  48 85 C0                        test rax, rax
00741BBD  75 0A                           jne 0x140741bc9
00741BBF  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00741BC4  E9 9D 01 00 00                  jmp 0x140741d66
00741BC9  45 8B FC                        mov r15d, r12d
00741BCC  45 33 C0                        xor r8d, r8d
00741BCF  E9 61 01 00 00                  jmp 0x140741d35
00741BD4  85 C0                           test eax, eax
00741BD6  0F 88 53 01 00 00               js 0x140741d2f
00741BDC  48 8B 55 A7                     mov rdx, qword ptr [rbp - 0x59]
00741BE0  48 8D 45 AF                     lea rax, [rbp - 0x51]
00741BE4  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00741BE9  45 33 C9                        xor r9d, r9d
00741BEC  4D 8B C6                        mov r8, r14
00741BEF  C7 44 24 20 19 00 02 00         mov dword ptr [rsp + 0x20], 0x20019
00741BF7  33 C9                           xor ecx, ecx
00741BF9  E8 BA DB 1A 00                  call 0x1408ef7b8
00741BFE  85 C0                           test eax, eax
00741C00  0F 88 29 01 00 00               js 0x140741d2f
00741C06  48 8B 55 AF                     mov rdx, qword ptr [rbp - 0x51]
00741C0A  48 8D 45 97                     lea rax, [rbp - 0x69]
00741C0E  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00741C13  4C 8D 4D 9B                     lea r9, [rbp - 0x65]
00741C17  48 8D 45 9F                     lea rax, [rbp - 0x61]
00741C1B  BF 04 00 00 00                  mov edi, 4
00741C20  4C 8D 05 F9 AA 3B 00            lea r8, [rip + 0x3baaf9]
00741C27  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00741C2C  89 7D 97                        mov dword ptr [rbp - 0x69], edi
00741C2F  E8 C8 24 25 00                  call 0x1409940fc
00741C34  85 C0                           test eax, eax
00741C36  78 4E                           js 0x140741c86
00741C38  39 7D 9B                        cmp dword ptr [rbp - 0x65], edi
00741C3B  75 49                           jne 0x140741c86
00741C3D  39 7D 97                        cmp dword ptr [rbp - 0x69], edi
00741C40  75 44                           jne 0x140741c86
00741C42  48 8B 55 AF                     mov rdx, qword ptr [rbp - 0x51]
00741C46  48 8D 45 97                     lea rax, [rbp - 0x69]
00741C4A  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00741C4F  4C 8D 4D 9B                     lea r9, [rbp - 0x65]
00741C53  48 8D 45 A3                     lea rax, [rbp - 0x5d]
00741C57  89 7D 97                        mov dword ptr [rbp - 0x69], edi
00741C5A  4C 8D 05 EF C2 3B 00            lea r8, [rip + 0x3bc2ef]
00741C61  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00741C66  E8 91 24 25 00                  call 0x1409940fc
00741C6B  85 C0                           test eax, eax
00741C6D  78 12                           js 0x140741c81
00741C6F  39 7D 9B                        cmp dword ptr [rbp - 0x65], edi
00741C72  75 0D                           jne 0x140741c81
00741C74  39 7D 97                        cmp dword ptr [rbp - 0x69], edi
00741C77  75 08                           jne 0x140741c81
00741C79  8B 7D 9F                        mov edi, dword ptr [rbp - 0x61]
00741C7C  8B 75 A3                        mov esi, dword ptr [rbp - 0x5d]
00741C7F  EB 13                           jmp 0x140741c94
00741C81  8B 7D 9F                        mov edi, dword ptr [rbp - 0x61]
00741C84  EB 07                           jmp 0x140741c8d
00741C86  41 8B FC                        mov edi, r12d
00741C89  44 89 65 9F                     mov dword ptr [rbp - 0x61], r12d
00741C8D  44 89 65 A3                     mov dword ptr [rbp - 0x5d], r12d
00741C91  41 8B F4                        mov esi, r12d
00741C94  48 8B 4D AF                     mov rcx, qword ptr [rbp - 0x51]
00741C98  E8 13 B6 F6 FF                  call 0x1406ad2b0
00741C9D  85 FF                           test edi, edi
00741C9F  0F 84 8A 00 00 00               je 0x140741d2f
00741CA5  40 F6 C7 0B                     test dil, 0xb
00741CA9  74 12                           je 0x140741cbd
00741CAB  83 FE 02                        cmp esi, 2
00741CAE  74 0D                           je 0x140741cbd
00741CB0  41 8B 85 EC 01 00 00            mov eax, dword ptr [r13 + 0x1ec]
00741CB7  A8 40                           test al, 0x40
00741CB9  74 74                           je 0x140741d2f
00741CBB  EB 0B                           jmp 0x140741cc8
00741CBD  41 8B 85 EC 01 00 00            mov eax, dword ptr [r13 + 0x1ec]
00741CC4  84 C0                           test al, al
00741CC6  79 67                           jns 0x140741d2f
00741CC8  4C 8B 45 C7                     mov r8, qword ptr [rbp - 0x39]
00741CCC  4D 85 C0                        test r8, r8
00741CCF  75 3A                           jne 0x140741d0b
00741CD1  48 8B 55 CF                     mov rdx, qword ptr [rbp - 0x31]
00741CD5  48 8D 45 C7                     lea rax, [rbp - 0x39]
00741CD9  4C 89 64 24 38                  mov qword ptr [rsp + 0x38], r12
00741CDE  4C 8D 05 7B E8 3B 00            lea r8, [rip + 0x3be87b]
00741CE5  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00741CEA  45 33 C9                        xor r9d, r9d
00741CED  4C 89 64 24 28                  mov qword ptr [rsp + 0x28], r12
00741CF2  33 C9                           xor ecx, ecx
00741CF4  C7 44 24 20 1F 00 02 00         mov dword ptr [rsp + 0x20], 0x2001f
00741CFC  E8 E3 75 32 00                  call 0x140a692e4
00741D01  8B D8                           mov ebx, eax
00741D03  85 C0                           test eax, eax
00741D05  78 55                           js 0x140741d5c
00741D07  4C 8B 45 C7                     mov r8, qword ptr [rbp - 0x39]
00741D0B  48 8B 4D A7                     mov rcx, qword ptr [rbp - 0x59]
00741D0F  4D 8B CE                        mov r9, r14
00741D12  4C 89 64 24 38                  mov qword ptr [rsp + 0x38], r12
00741D17  49 8B D6                        mov rdx, r14
00741D1A  44 89 64 24 30                  mov dword ptr [rsp + 0x30], r12d
00741D1F  4C 89 64 24 28                  mov qword ptr [rsp + 0x28], r12
00741D24  E8 D3 F6 FF FF                  call 0x1407413fc
00741D29  8B D8                           mov ebx, eax
00741D2B  85 C0                           test eax, eax
00741D2D  78 2D                           js 0x140741d5c
00741D2F  41 FF C7                        inc r15d
00741D32  45 8B C7                        mov r8d, r15d
00741D35  48 8B 55 A7                     mov rdx, qword ptr [rbp - 0x59]
00741D39  48 8D 45 97                     lea rax, [rbp - 0x69]
00741D3D  4D 8B CE                        mov r9, r14
00741D40  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00741D45  C7 45 97 04 01 00 00            mov dword ptr [rbp - 0x69], 0x104
00741D4C  E8 6F 0C 25 00                  call 0x1409929c0
00741D51  3D 1A 00 00 80                  cmp eax, 0x8000001a
00741D56  0F 85 78 FE FF FF               jne 0x140741bd4
00741D5C  33 D2                           xor edx, edx
00741D5E  49 8B CE                        mov rcx, r14
00741D61  E8 0A 0B 44 00                  call 0x140b82870
00741D66  48 8B 4D B7                     mov rcx, qword ptr [rbp - 0x49]
00741D6A  48 85 C9                        test rcx, rcx
00741D6D  74 05                           je 0x140741d74
00741D6F  E8 3C B5 F6 FF                  call 0x1406ad2b0
00741D74  48 8B 4D BF                     mov rcx, qword ptr [rbp - 0x41]
00741D78  48 85 C9                        test rcx, rcx
00741D7B  74 05                           je 0x140741d82
00741D7D  E8 2E B5 F6 FF                  call 0x1406ad2b0
00741D82  48 8B 4D A7                     mov rcx, qword ptr [rbp - 0x59]
00741D86  48 85 C9                        test rcx, rcx
00741D89  74 05                           je 0x140741d90
00741D8B  E8 20 B5 F6 FF                  call 0x1406ad2b0
00741D90  48 8B 4D C7                     mov rcx, qword ptr [rbp - 0x39]
00741D94  48 85 C9                        test rcx, rcx
00741D97  74 05                           je 0x140741d9e
00741D99  E8 12 B5 F6 FF                  call 0x1406ad2b0
00741D9E  48 8B 4D CF                     mov rcx, qword ptr [rbp - 0x31]
00741DA2  48 85 C9                        test rcx, rcx
00741DA5  74 05                           je 0x140741dac
00741DA7  E8 04 B5 F6 FF                  call 0x1406ad2b0
00741DAC  8B C3                           mov eax, ebx
00741DAE  48 8B 4D 17                     mov rcx, qword ptr [rbp + 0x17]
00741DB2  48 33 CC                        xor rcx, rsp
00741DB5  E8 86 A8 F6 FF                  call 0x1406ac640
00741DBA  48 8B 9C 24 10 01 00 00         mov rbx, qword ptr [rsp + 0x110]
00741DC2  48 81 C4 D0 00 00 00            add rsp, 0xd0
00741DC9  41 5F                           pop r15
00741DCB  41 5E                           pop r14
00741DCD  41 5D                           pop r13
00741DCF  41 5C                           pop r12
00741DD1  5F                              pop rdi
00741DD2  5E                              pop rsi
00741DD3  5D                              pop rbp
00741DD4  C3                              ret
00741DD5  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PiDrvDbOverlayNodeHive(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r15;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m5F;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned int v_stack_mBC;
    unsigned int v_stack_mC0;
    unsigned int v_stack_mC4;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned int v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned int v_stack_mE8;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (208);
    result = (*(unsigned __int64 *)(v_rip + 7114125)) ^ (v_rsp);
    v_stack_m48 = result;
    v_r12 = 0;
    v_stack_m90 = 0;
    a2 = 0;
    result = memset(v_stack_m88, a2, v_r12 + 64, a4);
    v_stack_mA0 = 0;
    v_stack_mA8 = 0;
    v_stack_mB8 = 0;
    v_stack_m98 = 0;
    v_stack_mB0 = 0;
    v_stack_mC0 = 0;
    v_stack_mBC = 0;
    v_stack_mC4 = 0;
    result = wcsicmp(0, v_rip + 3922719, v_r12 + 64, a4);
    if ((unsigned int)(result) != 0) goto loc_00741A8F;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 492)))) & (16)) != 0) goto loc_00741A2C;
loc_00741A24:
    goto loc_00741D66;
loc_00741A2C:
loc_00741A33:
    v_rdi = (unsigned int)((0) + 1);
    *(unsigned __int64 *)(v_stack_m5F + 0 * 8 - 41) = *(unsigned __int64 *)(v_rip + 4236757);
    if (((unsigned int)(v_rdi)) < 4) goto loc_00741A33;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 492)))) & (192)) == 0) goto loc_00741A86;
    a4 = 0;
    v_stack_mE0 = v_stack_mB8;
    v_stack_mE8 = 0x20019ULL;
    a1 = 0;
    result = PnpCtxRegOpenKey(a1, a3, v_rip + 3926861, a4);
    if (((unsigned int)(result)) != 0xC0000034ULL) goto loc_00741A7E;
    v_stack_mB8 = 0;
    goto loc_00741A86;
loc_00741A7E:
    if (sign_flag) goto loc_00741D66;
loc_00741A86:
    *(unsigned __int64 *)(v_stack_m5F + v_rdi * 8 - 41) = v_rip + 3926861;
    v_rdi = (unsigned int)((v_rdi) + 1);
    goto loc_00741AB1;
loc_00741A8F:
    result = wcsicmp(0, v_rip + 3922330, v_rip + 3926861, a4);
    if ((unsigned int)(result) != 0) goto loc_00741AB1;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 492)))) & (32)) == 0) goto loc_00741A24;
loc_00741AB1:
    a4 = 0;
    v_rdi = (unsigned int)((v_rdi) + 1);
    *(unsigned __int64 *)(v_stack_m5F + (unsigned int)((unsigned int)(v_rdi)) * 8 - 41) = v_rip + 3921590;
    v_stack_mE0 = v_stack_mA0;
    a1 = 0;
    v_stack_mE8 = 0x20019ULL;
    result = PnpCtxRegOpenKey(a1, (unsigned int)((unsigned int)((unsigned int)(0x80000002ULL))), v_rip + 3926729, a4);
    if (((unsigned int)(result)) != 0xC0000034ULL) goto loc_00741AFB;
    v_stack_mA0 = 0;
    goto loc_00741B3C;
loc_00741AFB:
    if (sign_flag) goto loc_00741D66;
    v_stack_mE0 = v_stack_mA8;
    a4 = 0;
    v_stack_mE8 = 0x20019ULL;
    a1 = 0;
    result = PnpCtxRegOpenKey(a1, v_stack_mA0, 0, a4);
    if (((unsigned int)(result)) != 0xC0000034ULL) goto loc_00741B34;
    v_stack_mA8 = 0;
    goto loc_00741B3C;
loc_00741B34:
    if (sign_flag) goto loc_00741D66;
loc_00741B3C:
    a4 = 0;
    v_stack_mE0 = v_stack_m90;
    v_stack_mE8 = 0x2001FULL;
    a1 = 0;
    result = PnpCtxRegOpenKey(a1, (unsigned int)(0x80000002ULL), 0, a4);
    if (sign_flag) goto loc_00741D66;
    a4 = 0;
    a2 = 0;
    v_stack_mD0 = v_stack_mA8;
    v_stack_mD8 = (unsigned int)(v_rdi);
    v_stack_mE0 = v_stack_m88;
    result = PiDrvDbOverlayCopyKeys(a3, a2, v_stack_m90, a4);
    if (sign_flag) goto loc_00741D66;
    if (v_stack_mB8 == 0) goto loc_00741D66;
    result = ExAllocatePool2(256, 520, (unsigned int)(0x62647050ULL), a4);
    if (result != 0) goto loc_00741BC9;
    goto loc_00741D66;
loc_00741BC9:
    a3 = 0;
    goto loc_00741D35;
loc_00741BD4:
    if (sign_flag) goto loc_00741D2F;
    v_stack_mE0 = v_stack_mB0;
    a4 = 0;
    v_stack_mE8 = 0x20019ULL;
    a1 = 0;
    result = PnpCtxRegOpenKey(a1, v_stack_mB8, result, a4);
    if (sign_flag) goto loc_00741D2F;
    v_stack_mE0 = v_stack_mC8;
    v_stack_mE8 = v_stack_mC0;
    v_stack_mC8 = 4;
    result = PnpCtxRegQueryValue(a1, v_stack_mB0, v_rip + 3910393, v_stack_mC4);
    if (sign_flag) goto loc_00741C86;
    if (v_stack_mC4 != 4) goto loc_00741C86;
    if (v_stack_mC8 != 4) goto loc_00741C86;
    v_stack_mE0 = v_stack_mC8;
    v_stack_mC8 = 4;
    v_stack_mE8 = v_stack_mBC;
    result = PnpCtxRegQueryValue(a1, v_stack_mB0, v_rip + 3916527, v_stack_mC4);
    if (sign_flag) goto loc_00741C81;
    if (v_stack_mC4 != 4) goto loc_00741C81;
    if (v_stack_mC8 != 4) goto loc_00741C81;
    goto loc_00741C94;
loc_00741C81:
    goto loc_00741C8D;
loc_00741C86:
    v_stack_mC0 = 0;
loc_00741C8D:
    v_stack_mBC = 0;
loc_00741C94:
    result = ZwClose(v_stack_mB0, v_stack_mB0, v_rip + 3916527, v_stack_mC4);
    if (0 == 0) goto loc_00741D2F;
    if (((0) & (11)) == 0) goto loc_00741CBD;
    if (0 == 2) goto loc_00741CBD;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 492)))) & (64)) == 0) goto loc_00741D2F;
    goto loc_00741CC8;
loc_00741CBD:
    if (!sign_flag) goto loc_00741D2F;
loc_00741CC8:
    if (v_stack_m98 != 0) goto loc_00741D0B;
    v_stack_mD0 = 0;
    v_stack_mD8 = v_stack_m98;
    a4 = 0;
    v_stack_mE0 = 0;
    a1 = 0;
    v_stack_mE8 = 0x2001FULL;
    result = PnpCtxRegCreateKey(a1, v_stack_m90, v_rip + 3926139, a4);
    if (sign_flag) goto loc_00741D5C;
loc_00741D0B:
    v_stack_mD0 = 0;
    v_stack_mD8 = 0;
    v_stack_mE0 = 0;
    result = PiDrvDbOverlayCopyKeys(v_stack_mB8, result, v_stack_m98, result);
    if (sign_flag) goto loc_00741D5C;
loc_00741D2F:
    v_r15 = (unsigned int)((0) + 1);
loc_00741D35:
    v_stack_mE8 = v_stack_mC8;
    v_stack_mC8 = 260;
    result = PnpCtxRegEnumKey(v_stack_mB8, v_stack_mB8, (unsigned int)((unsigned int)(v_r15)), result);
    if (((unsigned int)(result)) != 0x8000001AULL) goto loc_00741BD4;
loc_00741D5C:
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, (unsigned int)((unsigned int)(v_r15)), result);
loc_00741D66:
    if (v_stack_mA8 != 0) {
        result = ZwClose(v_stack_mA8, a2, (unsigned int)((unsigned int)(v_r15)), result);
    }
    if (v_stack_mA0 != 0) {
        result = ZwClose(v_stack_mA0, a2, (unsigned int)((unsigned int)(v_r15)), result);
    }
    if (v_stack_mB8 != 0) {
        result = ZwClose(v_stack_mB8, a2, (unsigned int)((unsigned int)(v_r15)), result);
    }
    if (v_stack_m98 != 0) {
        result = ZwClose(v_stack_m98, a2, (unsigned int)((unsigned int)(v_r15)), result);
    }
    if (v_stack_m90 != 0) {
        result = ZwClose(v_stack_m90, a2, (unsigned int)((unsigned int)(v_r15)), result);
    }
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, (unsigned int)((unsigned int)(v_r15)), result);
    v_rsp = (v_rsp) + (208);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PiDrvDbOverlayNodeHive(void *Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_r15;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m5F;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint32_t v_stack_mBC;
    uint32_t v_stack_mC0;
    uint32_t v_stack_mC4;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint32_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint32_t v_stack_mE8;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (208);
    result = (*(uint64_t *)(v_rip + 0x6C8D8D)) ^ (local_rsp);
    v_stack_m48 = result;
    local_r12 = 0;
    v_stack_m90 = 0;
    Arg2 = 0;
    result = memset(v_stack_m88, Arg2, local_r12 + 64, Arg4);
    v_stack_mA0 = 0;
    v_stack_mA8 = 0;
    v_stack_mB8 = 0;
    v_stack_m98 = 0;
    v_stack_mB0 = 0;
    v_stack_mC0 = 0;
    v_stack_mBC = 0;
    v_stack_mC4 = 0;
    result = wcsicmp(0, v_rip + 3922719, local_r12 + 64, Arg4);
    if ((uint32_t)(result) != 0) goto loc_00741A8F;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x1EC)))) & (16)) != 0) goto loc_00741A2C;
loc_00741A24:
    goto loc_00741D66;
loc_00741A2C:
loc_00741A33:
    local_rdi = (uint32_t)((0) + 1);
    *(uint64_t *)(v_stack_m5F + 0x0 * 8 - 0x29) = *(uint64_t *)(v_rip + 0x40A5D5);
    if (((uint32_t)(local_rdi)) < 4) goto loc_00741A33;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x1EC)))) & (192)) == 0) goto loc_00741A86;
    Arg4 = 0;
    v_stack_mE0 = v_stack_mB8;
    v_stack_mE8 = 0x20019ULL;
    Arg1 = 0;
    result = PnpCtxRegOpenKey(Arg1, Arg3, v_rip + 3926861, Arg4);
    if (((uint32_t)(result)) != 0xC0000034ULL) goto loc_00741A7E;
    v_stack_mB8 = 0;
    goto loc_00741A86;
loc_00741A7E:
    if (sign_flag) goto loc_00741D66;
loc_00741A86:
    *(uint64_t *)(v_stack_m5F + local_rdi * 8 - 0x29) = v_rip + 3926861;
    local_rdi = (uint32_t)((local_rdi) + 1);
    goto loc_00741AB1;
loc_00741A8F:
    result = wcsicmp(0, v_rip + 3922330, v_rip + 3926861, Arg4);
    if ((uint32_t)(result) != 0) goto loc_00741AB1;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x1EC)))) & (32)) == 0) goto loc_00741A24;
loc_00741AB1:
    Arg4 = 0;
    local_rdi = (uint32_t)((local_rdi) + 1);
    *(uint64_t *)(v_stack_m5F + (uint32_t)((uint32_t)(local_rdi)) * 8 - 0x29) = v_rip + 3921590;
    v_stack_mE0 = v_stack_mA0;
    Arg1 = 0;
    v_stack_mE8 = 0x20019ULL;
    result = PnpCtxRegOpenKey(Arg1, (uint32_t)((uint32_t)((uint32_t)(0x80000002ULL))), v_rip + 3926729, Arg4);
    if (((uint32_t)(result)) != 0xC0000034ULL) goto loc_00741AFB;
    v_stack_mA0 = 0;
    goto loc_00741B3C;
loc_00741AFB:
    if (sign_flag) goto loc_00741D66;
    v_stack_mE0 = v_stack_mA8;
    Arg4 = 0;
    v_stack_mE8 = 0x20019ULL;
    Arg1 = 0;
    result = PnpCtxRegOpenKey(Arg1, v_stack_mA0, 0, Arg4);
    if (((uint32_t)(result)) != 0xC0000034ULL) goto loc_00741B34;
    v_stack_mA8 = 0;
    goto loc_00741B3C;
loc_00741B34:
    if (sign_flag) goto loc_00741D66;
loc_00741B3C:
    Arg4 = 0;
    v_stack_mE0 = v_stack_m90;
    v_stack_mE8 = 0x2001FULL;
    Arg1 = 0;
    result = PnpCtxRegOpenKey(Arg1, (uint32_t)(0x80000002ULL), 0, Arg4);
    if (sign_flag) goto loc_00741D66;
    Arg4 = 0;
    Arg2 = 0;
    v_stack_mD0 = v_stack_mA8;
    v_stack_mD8 = (uint32_t)(local_rdi);
    v_stack_mE0 = v_stack_m88;
    result = PiDrvDbOverlayCopyKeys(Arg3, Arg2, v_stack_m90, Arg4);
    if (sign_flag) goto loc_00741D66;
    if (v_stack_mB8 == 0) goto loc_00741D66;
    result = ExAllocatePool2(256, 520, (uint32_t)(0x62647050ULL), Arg4);
    if (result != 0) goto loc_00741BC9;
    goto loc_00741D66;
loc_00741BC9:
    Arg3 = 0;
    goto loc_00741D35;
loc_00741BD4:
    if (sign_flag) goto loc_00741D2F;
    v_stack_mE0 = v_stack_mB0;
    Arg4 = 0;
    v_stack_mE8 = 0x20019ULL;
    Arg1 = 0;
    result = PnpCtxRegOpenKey(Arg1, v_stack_mB8, result, Arg4);
    if (sign_flag) goto loc_00741D2F;
    v_stack_mE0 = v_stack_mC8;
    v_stack_mE8 = v_stack_mC0;
    v_stack_mC8 = 4;
    result = PnpCtxRegQueryValue(Arg1, v_stack_mB0, v_rip + 3910393, v_stack_mC4);
    if (sign_flag) goto loc_00741C86;
    if (v_stack_mC4 != 4) goto loc_00741C86;
    if (v_stack_mC8 != 4) goto loc_00741C86;
    v_stack_mE0 = v_stack_mC8;
    v_stack_mC8 = 4;
    v_stack_mE8 = v_stack_mBC;
    result = PnpCtxRegQueryValue(Arg1, v_stack_mB0, v_rip + 3916527, v_stack_mC4);
    if (sign_flag) goto loc_00741C81;
    if (v_stack_mC4 != 4) goto loc_00741C81;
    if (v_stack_mC8 != 4) goto loc_00741C81;
    goto loc_00741C94;
loc_00741C81:
    goto loc_00741C8D;
loc_00741C86:
    v_stack_mC0 = 0;
loc_00741C8D:
    v_stack_mBC = 0;
loc_00741C94:
    result = ZwClose(v_stack_mB0, v_stack_mB0, v_rip + 3916527, v_stack_mC4);
    if (0 == 0) goto loc_00741D2F;
    if (((0) & (11)) == 0) goto loc_00741CBD;
    if (0 == 2) goto loc_00741CBD;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x1EC)))) & (64)) == 0) goto loc_00741D2F;
    goto loc_00741CC8;
loc_00741CBD:
    if (!sign_flag) goto loc_00741D2F;
loc_00741CC8:
    if (v_stack_m98 != 0) goto loc_00741D0B;
    v_stack_mD0 = 0;
    v_stack_mD8 = v_stack_m98;
    Arg4 = 0;
    v_stack_mE0 = 0;
    Arg1 = 0;
    v_stack_mE8 = 0x2001FULL;
    result = PnpCtxRegCreateKey(Arg1, v_stack_m90, v_rip + 3926139, Arg4);
    if (sign_flag) goto loc_00741D5C;
loc_00741D0B:
    v_stack_mD0 = 0;
    v_stack_mD8 = 0;
    v_stack_mE0 = 0;
    result = PiDrvDbOverlayCopyKeys(v_stack_mB8, result, v_stack_m98, result);
    if (sign_flag) goto loc_00741D5C;
loc_00741D2F:
    local_r15 = (uint32_t)((0) + 1);
loc_00741D35:
    v_stack_mE8 = v_stack_mC8;
    v_stack_mC8 = 260;
    result = PnpCtxRegEnumKey(v_stack_mB8, v_stack_mB8, (uint32_t)((uint32_t)(local_r15)), result);
    if (((uint32_t)(result)) != 0x8000001AULL) goto loc_00741BD4;
loc_00741D5C:
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, (uint32_t)((uint32_t)(local_r15)), result);
loc_00741D66:
    if (v_stack_mA8 != 0) {
        result = ZwClose(v_stack_mA8, Arg2, (uint32_t)((uint32_t)(local_r15)), result);
    }
    if (v_stack_mA0 != 0) {
        result = ZwClose(v_stack_mA0, Arg2, (uint32_t)((uint32_t)(local_r15)), result);
    }
    if (v_stack_mB8 != 0) {
        result = ZwClose(v_stack_mB8, Arg2, (uint32_t)((uint32_t)(local_r15)), result);
    }
    if (v_stack_m98 != 0) {
        result = ZwClose(v_stack_m98, Arg2, (uint32_t)((uint32_t)(local_r15)), result);
    }
    if (v_stack_m90 != 0) {
        result = ZwClose(v_stack_m90, Arg2, (uint32_t)((uint32_t)(local_r15)), result);
    }
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, (uint32_t)((uint32_t)(local_r15)), result);
    local_rsp = (local_rsp) + (208);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x1EC` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00741990&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
