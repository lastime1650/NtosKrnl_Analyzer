# SdbpSearchDB

- RVA: `0x00AB3294`–`0x00AB37B5` (길이 `1,313` bytes)
- VA: `0x0000000140AB3294`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BCA74`
- 디코드: `345`개 명령, `1,313/1,313` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **30**; 고유 호출 대상: **13**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x00AB32EC` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00AB3300` → [SdbFindFirstTag](../95/SdbFindFirstTag_function_0095E34C.md) (function, `0x0095E34C`)
- `0x00AB3327` → [AslLogCallPrintf](../95/AslLogCallPrintf_function_0095E4EC.md) (function, `0x0095E4EC`)
- `0x00AB3342` → [SdbGetIndex](../95/SdbGetIndex_function_0095C3C4.md) (function, `0x0095C3C4`)
- `0x00AB3372` → [SdbpFindFirstIndexedWildCardTag](../95/SdbpFindFirstIndexedWildCardTag_function_0095DE58.md) (function, `0x0095DE58`)
- `0x00AB33A6` → [SdbpFindFirstNamedTagHelper](../AD/SdbpFindFirstNamedTagHelper_function_00AD4D2C.md) (function, `0x00AD4D2C`)
- `0x00AB33E0` → [SdbpCheckForMatch](SdbpCheckForMatch_function_00AB37BC.md) (function, `0x00AB37BC`)
- `0x00AB340D` → [AslLogCallPrintf](../95/AslLogCallPrintf_function_0095E4EC.md) (function, `0x0095E4EC`)
- `0x00AB342D` → [SdbpFindNextIndexedWildCardTag](../95/SdbpFindNextIndexedWildCardTag_function_0095A078.md) (function, `0x0095A078`)
- `0x00AB3471` → [SdbpFindNextNamedTagHelper](../81/SdbpFindNextNamedTagHelper_function_00816DF8.md) (function, `0x00816DF8`)
- `0x00AB3490` → [SdbGetIndex](../95/SdbGetIndex_function_0095C3C4.md) (function, `0x0095C3C4`)
- `0x00AB34B6` → [SdbFindFirstStringIndexedTag](../95/SdbFindFirstStringIndexedTag_function_0095C1D8.md) (function, `0x0095C1D8`)
- `0x00AB34D9` → [SdbpFindFirstNamedTagHelper](../AD/SdbpFindFirstNamedTagHelper_function_00AD4D2C.md) (function, `0x00AD4D2C`)
- `0x00AB3512` → [SdbpCheckExe](SdbpCheckExe_function_00AB31A0.md) (function, `0x00AB31A0`)
- `0x00AB353E` → [SdbFindNextStringIndexedTag](../A9/SdbFindNextStringIndexedTag_function_00A914C8.md) (function, `0x00A914C8`)
- `0x00AB355F` → [SdbpFindNextNamedTagHelper](../81/SdbpFindNextNamedTagHelper_function_00816DF8.md) (function, `0x00816DF8`)
- `0x00AB3589` → [SdbGetIndex](../95/SdbGetIndex_function_0095C3C4.md) (function, `0x0095C3C4`)
- `0x00AB35B4` → [SdbFindFirstStringIndexedTag](../95/SdbFindFirstStringIndexedTag_function_0095C1D8.md) (function, `0x0095C1D8`)
- `0x00AB35D7` → [SdbpFindFirstNamedTagHelper](../AD/SdbpFindFirstNamedTagHelper_function_00AD4D2C.md) (function, `0x00AD4D2C`)
- `0x00AB3610` → [SdbpCheckExe](SdbpCheckExe_function_00AB31A0.md) (function, `0x00AB31A0`)
- `0x00AB363C` → [SdbFindNextStringIndexedTag](../A9/SdbFindNextStringIndexedTag_function_00A914C8.md) (function, `0x00A914C8`)
- `0x00AB3661` → [SdbpFindNextNamedTagHelper](../81/SdbpFindNextNamedTagHelper_function_00816DF8.md) (function, `0x00816DF8`)
- `0x00AB367E` → [SdbGetIndex](../95/SdbGetIndex_function_0095C3C4.md) (function, `0x0095C3C4`)
- `0x00AB36A2` → [SdbpFindFirstIndexedWildCardTag](../95/SdbpFindFirstIndexedWildCardTag_function_0095DE58.md) (function, `0x0095DE58`)
- `0x00AB36DA` → [SdbpFindFirstNamedTagHelper](../AD/SdbpFindFirstNamedTagHelper_function_00AD4D2C.md) (function, `0x00AD4D2C`)
- `0x00AB370E` → [SdbpCheckExe](SdbpCheckExe_function_00AB31A0.md) (function, `0x00AB31A0`)
- `0x00AB3733` → [SdbpFindNextIndexedWildCardTag](../95/SdbpFindNextIndexedWildCardTag_function_0095A078.md) (function, `0x0095A078`)
- `0x00AB3754` → [SdbpFindNextNamedTagHelper](../81/SdbpFindNextNamedTagHelper_function_00816DF8.md) (function, `0x00816DF8`)
- `0x00AB377B` → [SdbFindFirstTag](../95/SdbFindFirstTag_function_0095E34C.md) (function, `0x0095E34C`)
- `0x00AB3789` → [SdbGetStringTagPtr](../95/SdbGetStringTagPtr_function_0095DDA8.md) (function, `0x0095DDA8`)

### Direct callers
- [SdbGetDatabaseMatch](../95/SdbGetDatabaseMatch_function_00958240.md) at `0x00958365`
- [SdbGetDatabaseMatch](../95/SdbGetDatabaseMatch_function_00958240.md) at `0x00958392`

### Static image references
- `0x00AB3319` → RVA `0x0003CC70` (`.rdata`; read)
- `0x00AB3320` → RVA `0x0003CC60` (`.rdata`; read)
- `0x00AB33F6` → RVA `0x0003CC98` (`.rdata`; read)
- `0x00AB3403` → RVA `0x0003CC88` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00AB32EC` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AB3294  48 8B C4                        mov rax, rsp
00AB3297  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
00AB329B  4C 89 48 20                     mov qword ptr [rax + 0x20], r9
00AB329F  66 44 89 40 18                  mov word ptr [rax + 0x18], r8w
00AB32A4  48 89 48 08                     mov qword ptr [rax + 8], rcx
00AB32A8  55                              push rbp
00AB32A9  56                              push rsi
00AB32AA  57                              push rdi
00AB32AB  41 54                           push r12
00AB32AD  41 55                           push r13
00AB32AF  41 56                           push r14
00AB32B1  41 57                           push r15
00AB32B3  48 8B EC                        mov rbp, rsp
00AB32B6  48 81 EC 80 00 00 00            sub rsp, 0x80
00AB32BD  4C 8B 6D 60                     mov r13, qword ptr [rbp + 0x60]
00AB32C1  0F 57 C0                        xorps xmm0, xmm0
00AB32C4  49 8B 71 28                     mov rsi, qword ptr [r9 + 0x28]
00AB32C8  33 C0                           xor eax, eax
00AB32CA  21 45 C0                        and dword ptr [rbp - 0x40], eax
00AB32CD  48 8B DA                        mov rbx, rdx
00AB32D0  33 FF                           xor edi, edi
00AB32D2  48 89 45 F8                     mov qword ptr [rbp - 8], rax
00AB32D6  49 8B CD                        mov rcx, r13
00AB32D9  89 7D 50                        mov dword ptr [rbp + 0x50], edi
00AB32DC  33 D2                           xor edx, edx
00AB32DE  41 B8 80 00 00 00               mov r8d, 0x80
00AB32E4  0F 11 45 D8                     movups xmmword ptr [rbp - 0x28], xmm0
00AB32E8  0F 11 45 E8                     movups xmmword ptr [rbp - 0x18], xmm0
00AB32EC  E8 4F 39 C1 FF                  call 0x1406c6c40
00AB32F1  33 D2                           xor edx, edx
00AB32F3  48 89 75 D0                     mov qword ptr [rbp - 0x30], rsi
00AB32F7  41 B8 01 70 00 00               mov r8d, 0x7001
00AB32FD  48 8B CB                        mov rcx, rbx
00AB3300  E8 47 B0 EA FF                  call 0x14095e34c
00AB3305  89 45 68                        mov dword ptr [rbp + 0x68], eax
00AB3308  85 C0                           test eax, eax
00AB330A  75 25                           jne 0x140ab3331
00AB330C  44 8D 77 01                     lea r14d, [rdi + 1]
00AB3310  41 B8 33 11 00 00               mov r8d, 0x1133
00AB3316  41 8B CE                        mov ecx, r14d
00AB3319  4C 8D 0D 50 99 58 FF            lea r9, [rip - 0xa766b0]
00AB3320  48 8D 15 39 99 58 FF            lea rdx, [rip - 0xa766c7]
00AB3327  E8 C0 B1 EA FF                  call 0x14095e4ec
00AB332C  E9 33 04 00 00                  jmp 0x140ab3764
00AB3331  BA 07 70 00 00                  mov edx, 0x7007
00AB3336  41 B8 0B 60 00 00               mov r8d, 0x600b
00AB333C  45 33 C9                        xor r9d, r9d
00AB333F  48 8B CB                        mov rcx, rbx
00AB3342  E8 7D 90 EA FF                  call 0x14095c3c4
00AB3347  41 BE 01 00 00 00               mov r14d, 1
00AB334D  45 8D 7E 0F                     lea r15d, [r14 + 0xf]
00AB3351  85 C0                           test eax, eax
00AB3353  74 24                           je 0x140ab3379
00AB3355  48 8D 45 D8                     lea rax, [rbp - 0x28]
00AB3359  BA 07 70 00 00                  mov edx, 0x7007
00AB335E  41 B8 0B 60 00 00               mov r8d, 0x600b
00AB3364  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AB3369  4C 8B CE                        mov r9, rsi
00AB336C  48 8B CB                        mov rcx, rbx
00AB336F  45 8B E6                        mov r12d, r14d
00AB3372  E8 E1 AA EA FF                  call 0x14095de58
00AB3377  EB 32                           jmp 0x140ab33ab
00AB3379  48 8B 45 40                     mov rax, qword ptr [rbp + 0x40]
00AB337D  45 33 E4                        xor r12d, r12d
00AB3380  48 3B 58 08                     cmp rbx, qword ptr [rax + 8]
00AB3384  0F 84 F5 00 00 00               je 0x140ab347f
00AB338A  8B 55 68                        mov edx, dword ptr [rbp + 0x68]
00AB338D  41 B9 0B 60 00 00               mov r9d, 0x600b
00AB3393  41 B8 07 70 00 00               mov r8d, 0x7007
00AB3399  44 89 74 24 28                  mov dword ptr [rsp + 0x28], r14d
00AB339E  48 8B CB                        mov rcx, rbx
00AB33A1  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
00AB33A6  E8 81 19 02 00                  call 0x140ad4d2c
00AB33AB  8B F0                           mov esi, eax
00AB33AD  85 C0                           test eax, eax
00AB33AF  0F 84 C6 00 00 00               je 0x140ab347b
00AB33B5  4C 8B 4D 58                     mov r9, qword ptr [rbp + 0x58]
00AB33B9  48 8D 45 C8                     lea rax, [rbp - 0x38]
00AB33BD  48 8B 4D 40                     mov rcx, qword ptr [rbp + 0x40]
00AB33C1  44 8B C6                        mov r8d, esi
00AB33C4  83 65 C8 00                     and dword ptr [rbp - 0x38], 0
00AB33C8  48 8B D3                        mov rdx, rbx
00AB33CB  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AB33D0  48 8D 45 C4                     lea rax, [rbp - 0x3c]
00AB33D4  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AB33D9  C7 45 C4 02 00 00 00            mov dword ptr [rbp - 0x3c], 2
00AB33E0  E8 D7 03 00 00                  call 0x140ab37bc
00AB33E5  85 C0                           test eax, eax
00AB33E7  74 2F                           je 0x140ab3418
00AB33E9  8B 55 C4                        mov edx, dword ptr [rbp - 0x3c]
00AB33EC  83 FA 02                        cmp edx, 2
00AB33EF  75 27                           jne 0x140ab3418
00AB33F1  41 3B FF                        cmp edi, r15d
00AB33F4  72 41                           jb 0x140ab3437
00AB33F6  4C 8D 0D 9B 98 58 FF            lea r9, [rip - 0xa76765]
00AB33FD  41 B8 DC 10 00 00               mov r8d, 0x10dc
00AB3403  48 8D 15 7E 98 58 FF            lea rdx, [rip - 0xa76782]
00AB340A  41 8B CE                        mov ecx, r14d
00AB340D  E8 DA B0 EA FF                  call 0x14095e4ec
00AB3412  41 03 FE                        add edi, r14d
00AB3415  89 7D 50                        mov dword ptr [rbp + 0x50], edi
00AB3418  41 3B FF                        cmp edi, r15d
00AB341B  0F 87 4A 03 00 00               ja 0x140ab376b
00AB3421  48 8B CB                        mov rcx, rbx
00AB3424  4D 85 E4                        test r12, r12
00AB3427  74 2E                           je 0x140ab3457
00AB3429  48 8D 55 D8                     lea rdx, [rbp - 0x28]
00AB342D  E8 46 6C EA FF                  call 0x14095a078
00AB3432  E9 74 FF FF FF                  jmp 0x140ab33ab
00AB3437  8B 45 C8                        mov eax, dword ptr [rbp - 0x38]
00AB343A  41 89 74 FD 00                  mov dword ptr [r13 + rdi*8], esi
00AB343F  41 89 44 FD 04                  mov dword ptr [r13 + rdi*8 + 4], eax
00AB3444  41 03 FE                        add edi, r14d
00AB3447  89 7D 50                        mov dword ptr [rbp + 0x50], edi
00AB344A  89 55 C0                        mov dword ptr [rbp - 0x40], edx
00AB344D  83 FA 02                        cmp edx, 2
00AB3450  74 CF                           je 0x140ab3421
00AB3452  E9 08 03 00 00                  jmp 0x140ab375f
00AB3457  48 8B 45 D0                     mov rax, qword ptr [rbp - 0x30]
00AB345B  41 B9 0B 60 00 00               mov r9d, 0x600b
00AB3461  8B 55 68                        mov edx, dword ptr [rbp + 0x68]
00AB3464  44 8B C6                        mov r8d, esi
00AB3467  44 89 74 24 28                  mov dword ptr [rsp + 0x28], r14d
00AB346C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AB3471  E8 82 39 D6 FF                  call 0x140816df8
00AB3476  E9 30 FF FF FF                  jmp 0x140ab33ab
00AB347B  48 8B 75 D0                     mov rsi, qword ptr [rbp - 0x30]
00AB347F  BA 07 70 00 00                  mov edx, 0x7007
00AB3484  41 B8 01 60 00 00               mov r8d, 0x6001
00AB348A  45 33 C9                        xor r9d, r9d
00AB348D  48 8B CB                        mov rcx, rbx
00AB3490  E8 2F 8F EA FF                  call 0x14095c3c4
00AB3495  48 8B CB                        mov rcx, rbx
00AB3498  85 C0                           test eax, eax
00AB349A  74 21                           je 0x140ab34bd
00AB349C  48 8D 45 D8                     lea rax, [rbp - 0x28]
00AB34A0  BA 07 70 00 00                  mov edx, 0x7007
00AB34A5  41 B8 01 60 00 00               mov r8d, 0x6001
00AB34AB  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AB34B0  4C 8B CE                        mov r9, rsi
00AB34B3  4D 8B E6                        mov r12, r14
00AB34B6  E8 1D 8D EA FF                  call 0x14095c1d8
00AB34BB  EB 21                           jmp 0x140ab34de
00AB34BD  8B 55 68                        mov edx, dword ptr [rbp + 0x68]
00AB34C0  45 33 E4                        xor r12d, r12d
00AB34C3  44 21 64 24 28                  and dword ptr [rsp + 0x28], r12d
00AB34C8  41 B9 01 60 00 00               mov r9d, 0x6001
00AB34CE  41 B8 07 70 00 00               mov r8d, 0x7007
00AB34D4  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
00AB34D9  E8 4E 18 02 00                  call 0x140ad4d2c
00AB34DE  8B F0                           mov esi, eax
00AB34E0  85 C0                           test eax, eax
00AB34E2  0F 84 81 00 00 00               je 0x140ab3569
00AB34E8  48 8B 4D 40                     mov rcx, qword ptr [rbp + 0x40]
00AB34EC  48 8D 45 C0                     lea rax, [rbp - 0x40]
00AB34F0  4C 89 6C 24 38                  mov qword ptr [rsp + 0x38], r13
00AB34F5  4C 8D 4D 50                     lea r9, [rbp + 0x50]
00AB34F9  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00AB34FE  44 8B C6                        mov r8d, esi
00AB3501  48 8B 45 58                     mov rax, qword ptr [rbp + 0x58]
00AB3505  48 8B D3                        mov rdx, rbx
00AB3508  83 64 24 28 00                  and dword ptr [rsp + 0x28], 0
00AB350D  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AB3512  E8 89 FC FF FF                  call 0x140ab31a0
00AB3517  8B 7D 50                        mov edi, dword ptr [rbp + 0x50]
00AB351A  85 C0                           test eax, eax
00AB351C  74 0B                           je 0x140ab3529
00AB351E  83 7D C0 02                     cmp dword ptr [rbp - 0x40], 2
00AB3522  74 0E                           je 0x140ab3532
00AB3524  E9 36 02 00 00                  jmp 0x140ab375f
00AB3529  41 3B FF                        cmp edi, r15d
00AB352C  0F 87 39 02 00 00               ja 0x140ab376b
00AB3532  48 8B CB                        mov rcx, rbx
00AB3535  4D 85 E4                        test r12, r12
00AB3538  74 0B                           je 0x140ab3545
00AB353A  48 8D 55 D8                     lea rdx, [rbp - 0x28]
00AB353E  E8 85 DF FD FF                  call 0x140a914c8
00AB3543  EB 99                           jmp 0x140ab34de
00AB3545  48 8B 45 D0                     mov rax, qword ptr [rbp - 0x30]
00AB3549  41 B9 01 60 00 00               mov r9d, 0x6001
00AB354F  83 64 24 28 00                  and dword ptr [rsp + 0x28], 0
00AB3554  44 8B C6                        mov r8d, esi
00AB3557  8B 55 68                        mov edx, dword ptr [rbp + 0x68]
00AB355A  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AB355F  E8 94 38 D6 FF                  call 0x140816df8
00AB3564  E9 75 FF FF FF                  jmp 0x140ab34de
00AB3569  48 8B 75 58                     mov rsi, qword ptr [rbp + 0x58]
00AB356D  48 83 7E 30 00                  cmp qword ptr [rsi + 0x30], 0
00AB3572  0F 84 F3 00 00 00               je 0x140ab366b
00AB3578  BA 07 70 00 00                  mov edx, 0x7007
00AB357D  41 B8 20 60 00 00               mov r8d, 0x6020
00AB3583  45 33 C9                        xor r9d, r9d
00AB3586  48 8B CB                        mov rcx, rbx
00AB3589  E8 36 8E EA FF                  call 0x14095c3c4
00AB358E  44 8B E0                        mov r12d, eax
00AB3591  48 8B 46 30                     mov rax, qword ptr [rsi + 0x30]
00AB3595  45 85 E4                        test r12d, r12d
00AB3598  74 21                           je 0x140ab35bb
00AB359A  48 8D 4D D8                     lea rcx, [rbp - 0x28]
00AB359E  BA 07 70 00 00                  mov edx, 0x7007
00AB35A3  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00AB35A8  41 B8 20 60 00 00               mov r8d, 0x6020
00AB35AE  48 8B CB                        mov rcx, rbx
00AB35B1  4C 8B C8                        mov r9, rax
00AB35B4  E8 1F 8C EA FF                  call 0x14095c1d8
00AB35B9  EB 21                           jmp 0x140ab35dc
00AB35BB  83 64 24 28 00                  and dword ptr [rsp + 0x28], 0
00AB35C0  41 B9 20 60 00 00               mov r9d, 0x6020
00AB35C6  8B 55 68                        mov edx, dword ptr [rbp + 0x68]
00AB35C9  41 B8 07 70 00 00               mov r8d, 0x7007
00AB35CF  48 8B CB                        mov rcx, rbx
00AB35D2  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AB35D7  E8 50 17 02 00                  call 0x140ad4d2c
00AB35DC  8B F0                           mov esi, eax
00AB35DE  85 C0                           test eax, eax
00AB35E0  0F 84 85 00 00 00               je 0x140ab366b
00AB35E6  48 8B 4D 40                     mov rcx, qword ptr [rbp + 0x40]
00AB35EA  48 8D 45 C0                     lea rax, [rbp - 0x40]
00AB35EE  4C 89 6C 24 38                  mov qword ptr [rsp + 0x38], r13
00AB35F3  4C 8D 4D 50                     lea r9, [rbp + 0x50]
00AB35F7  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00AB35FC  44 8B C6                        mov r8d, esi
00AB35FF  48 8B 45 58                     mov rax, qword ptr [rbp + 0x58]
00AB3603  48 8B D3                        mov rdx, rbx
00AB3606  83 64 24 28 00                  and dword ptr [rsp + 0x28], 0
00AB360B  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AB3610  E8 8B FB FF FF                  call 0x140ab31a0
00AB3615  8B 7D 50                        mov edi, dword ptr [rbp + 0x50]
00AB3618  85 C0                           test eax, eax
00AB361A  74 0B                           je 0x140ab3627
00AB361C  83 7D C0 02                     cmp dword ptr [rbp - 0x40], 2
00AB3620  74 0E                           je 0x140ab3630
00AB3622  E9 38 01 00 00                  jmp 0x140ab375f
00AB3627  41 3B FF                        cmp edi, r15d
00AB362A  0F 87 3B 01 00 00               ja 0x140ab376b
00AB3630  48 8B CB                        mov rcx, rbx
00AB3633  45 85 E4                        test r12d, r12d
00AB3636  74 0B                           je 0x140ab3643
00AB3638  48 8D 55 D8                     lea rdx, [rbp - 0x28]
00AB363C  E8 87 DE FD FF                  call 0x140a914c8
00AB3641  EB 99                           jmp 0x140ab35dc
00AB3643  83 64 24 28 00                  and dword ptr [rsp + 0x28], 0
00AB3648  41 B9 20 60 00 00               mov r9d, 0x6020
00AB364E  48 8B 45 58                     mov rax, qword ptr [rbp + 0x58]
00AB3652  44 8B C6                        mov r8d, esi
00AB3655  8B 55 68                        mov edx, dword ptr [rbp + 0x68]
00AB3658  48 8B 40 30                     mov rax, qword ptr [rax + 0x30]
00AB365C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AB3661  E8 92 37 D6 FF                  call 0x140816df8
00AB3666  E9 71 FF FF FF                  jmp 0x140ab35dc
00AB366B  BE 07 70 00 00                  mov esi, 0x7007
00AB3670  41 B8 0B 60 00 00               mov r8d, 0x600b
00AB3676  8B D6                           mov edx, esi
00AB3678  45 33 C9                        xor r9d, r9d
00AB367B  48 8B CB                        mov rcx, rbx
00AB367E  E8 41 8D EA FF                  call 0x14095c3c4
00AB3683  85 C0                           test eax, eax
00AB3685  74 25                           je 0x140ab36ac
00AB3687  4C 8B 4D D0                     mov r9, qword ptr [rbp - 0x30]
00AB368B  48 8D 45 D8                     lea rax, [rbp - 0x28]
00AB368F  41 B8 0B 60 00 00               mov r8d, 0x600b
00AB3695  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AB369A  8B D6                           mov edx, esi
00AB369C  48 8B CB                        mov rcx, rbx
00AB369F  4D 8B E6                        mov r12, r14
00AB36A2  E8 B1 A7 EA FF                  call 0x14095de58
00AB36A7  E9 AD 00 00 00                  jmp 0x140ab3759
00AB36AC  48 8B 45 40                     mov rax, qword ptr [rbp + 0x40]
00AB36B0  45 33 E4                        xor r12d, r12d
00AB36B3  48 3B 58 08                     cmp rbx, qword ptr [rax + 8]
00AB36B7  0F 84 A2 00 00 00               je 0x140ab375f
00AB36BD  48 8B 45 D0                     mov rax, qword ptr [rbp - 0x30]
00AB36C1  41 B9 0B 60 00 00               mov r9d, 0x600b
00AB36C7  8B 55 68                        mov edx, dword ptr [rbp + 0x68]
00AB36CA  44 8B C6                        mov r8d, esi
00AB36CD  44 89 74 24 28                  mov dword ptr [rsp + 0x28], r14d
00AB36D2  48 8B CB                        mov rcx, rbx
00AB36D5  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AB36DA  E8 4D 16 02 00                  call 0x140ad4d2c
00AB36DF  EB 78                           jmp 0x140ab3759
00AB36E1  48 8B 4D 40                     mov rcx, qword ptr [rbp + 0x40]
00AB36E5  48 8D 45 C0                     lea rax, [rbp - 0x40]
00AB36E9  4C 89 6C 24 38                  mov qword ptr [rsp + 0x38], r13
00AB36EE  4C 8D 4D 50                     lea r9, [rbp + 0x50]
00AB36F2  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00AB36F7  44 8B C6                        mov r8d, esi
00AB36FA  48 8B 45 58                     mov rax, qword ptr [rbp + 0x58]
00AB36FE  48 8B D3                        mov rdx, rbx
00AB3701  C7 44 24 28 02 00 00 00         mov dword ptr [rsp + 0x28], 2
00AB3709  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AB370E  E8 8D FA FF FF                  call 0x140ab31a0
00AB3713  8B 7D 50                        mov edi, dword ptr [rbp + 0x50]
00AB3716  85 C0                           test eax, eax
00AB3718  74 08                           je 0x140ab3722
00AB371A  83 7D C0 02                     cmp dword ptr [rbp - 0x40], 2
00AB371E  74 07                           je 0x140ab3727
00AB3720  EB 3D                           jmp 0x140ab375f
00AB3722  41 3B FF                        cmp edi, r15d
00AB3725  77 44                           ja 0x140ab376b
00AB3727  48 8B CB                        mov rcx, rbx
00AB372A  4D 85 E4                        test r12, r12
00AB372D  74 0B                           je 0x140ab373a
00AB372F  48 8D 55 D8                     lea rdx, [rbp - 0x28]
00AB3733  E8 40 69 EA FF                  call 0x14095a078
00AB3738  EB 1F                           jmp 0x140ab3759
00AB373A  48 8B 45 D0                     mov rax, qword ptr [rbp - 0x30]
00AB373E  41 B9 0B 60 00 00               mov r9d, 0x600b
00AB3744  8B 55 68                        mov edx, dword ptr [rbp + 0x68]
00AB3747  44 8B C6                        mov r8d, esi
00AB374A  44 89 74 24 28                  mov dword ptr [rsp + 0x28], r14d
00AB374F  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AB3754  E8 9F 36 D6 FF                  call 0x140816df8
00AB3759  8B F0                           mov esi, eax
00AB375B  85 C0                           test eax, eax
00AB375D  75 82                           jne 0x140ab36e1
00AB375F  41 3B FF                        cmp edi, r15d
00AB3762  77 07                           ja 0x140ab376b
00AB3764  44 8B FF                        mov r15d, edi
00AB3767  85 FF                           test edi, edi
00AB3769  74 2C                           je 0x140ab3797
00AB376B  41 8B F7                        mov esi, r15d
00AB376E  41 8B 55 00                     mov edx, dword ptr [r13]
00AB3772  41 B8 06 60 00 00               mov r8d, 0x6006
00AB3778  48 8B CB                        mov rcx, rbx
00AB377B  E8 CC AB EA FF                  call 0x14095e34c
00AB3780  85 C0                           test eax, eax
00AB3782  74 0A                           je 0x140ab378e
00AB3784  8B D0                           mov edx, eax
00AB3786  48 8B CB                        mov rcx, rbx
00AB3789  E8 1A A6 EA FF                  call 0x14095dda8
00AB378E  49 83 C5 08                     add r13, 8
00AB3792  49 2B F6                        sub rsi, r14
00AB3795  75 D7                           jne 0x140ab376e
00AB3797  48 8B 9C 24 C8 00 00 00         mov rbx, qword ptr [rsp + 0xc8]
00AB379F  8B C7                           mov eax, edi
00AB37A1  48 81 C4 80 00 00 00            add rsp, 0x80
00AB37A8  41 5F                           pop r15
00AB37AA  41 5E                           pop r14
00AB37AC  41 5D                           pop r13
00AB37AE  41 5C                           pop r12
00AB37B0  5F                              pop rdi
00AB37B1  5E                              pop rsi
00AB37B2  5D                              pop rbp
00AB37B3  C3                              ret
00AB37B4  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SdbpSearchDB(__int64 a1, __int64 a2, unsigned __int16 a3, __int64 a4, __int64 a5, unsigned int a6)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m74;
    unsigned int v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned int v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p30;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 32) = a4;
    *(unsigned __int16 *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (128);
    result = 0;
    v_rdi = 0;
    v_stack_m40 = 0;
    v_stack_p18 = 0;
    a2 = 0;
    v_stack_m60 = v_xmm0;
    v_stack_m50 = v_xmm0;
    result = memset(a5, a2, 128, a4);
    a2 = 0;
    v_stack_m68 = *(unsigned __int64 *)(a4 + 40);
    result = SdbFindFirstTag(0, a2, (unsigned int)(0x7001ULL), a4);
    v_stack_p30 = (unsigned int)(result);
    if ((unsigned int)(result) != 0) goto loc_00AB3331;
    result = AslLogCallPrintf((unsigned int)((unsigned int)(v_rdi + 1)), v_rip - 10970823, (unsigned int)(0x1133ULL), v_rip - 10970800);
    goto loc_00AB3764;
loc_00AB3331:
    a4 = 0;
    result = SdbGetIndex(0, (unsigned int)(0x7007ULL), (unsigned int)(0x600BULL), a4);
    if ((unsigned int)(result) == 0) goto loc_00AB3379;
    v_stack_m98 = v_stack_m60;
    result = SdbpFindFirstIndexedWildCardTag(0, (unsigned int)(0x7007ULL), (unsigned int)(0x600BULL), *(unsigned __int64 *)(a4 + 40));
    goto loc_00AB33AB;
loc_00AB3379:
    v_r12 = 0;
    if (0 == (*(unsigned __int64 *)(v_stack_p8 + 8))) goto loc_00AB347F;
    v_stack_m90 = 1;
    v_stack_m98 = *(unsigned __int64 *)(a4 + 40);
    result = SdbpFindFirstNamedTagHelper(0, (unsigned int)(a6), (unsigned int)(0x7007ULL), (unsigned int)(0x600BULL));
loc_00AB33AB:
    if ((unsigned int)(result) == 0) goto loc_00AB347B;
    v_stack_m90 = v_stack_m70;
    v_stack_m98 = v_stack_m74;
    v_stack_m74 = 2;
    result = SdbpCheckForMatch(v_stack_p8, 0, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), v_stack_p20);
    if ((unsigned int)(result) == 0) goto loc_00AB3418;
    if (((unsigned int)((unsigned int)(v_stack_m74))) != 2) goto loc_00AB3418;
    if (0 < ((unsigned int)(1 + 15))) goto loc_00AB3437;
    result = AslLogCallPrintf(1, v_rip - 10971010, (unsigned int)(0x10DCULL), v_rip - 10970981);
    v_rdi = (unsigned int)((v_rdi) + (1));
    v_stack_p18 = (unsigned int)(v_rdi);
loc_00AB3418:
    if (((unsigned int)(v_rdi)) > ((unsigned int)(1 + 15))) goto loc_00AB376B;
loc_00AB3421:
    if (0 == 0) goto loc_00AB3457;
    result = SdbpFindNextIndexedWildCardTag(0, v_stack_m60, (unsigned int)(0x10DCULL), v_rip - 10970981);
    goto loc_00AB33AB;
loc_00AB3437:
    *(unsigned int *)(a5 + v_rdi * 8) = (unsigned int)((unsigned int)((unsigned int)(result)));
    *(unsigned int *)(a5 + v_rdi * 8 + 4) = (unsigned int)((unsigned int)(v_stack_m70));
    v_rdi = (unsigned int)((v_rdi) + (1));
    v_stack_p18 = (unsigned int)(v_rdi);
    v_stack_m78 = (unsigned int)(v_stack_m60);
    if (((unsigned int)(v_stack_m60)) == 2) goto loc_00AB3421;
    goto loc_00AB375F;
loc_00AB3457:
    v_stack_m90 = 1;
    v_stack_m98 = v_stack_m68;
    result = SdbpFindNextNamedTagHelper(0, (unsigned int)(a6), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)(0x600BULL));
    goto loc_00AB33AB;
loc_00AB347B:
loc_00AB347F:
    a4 = 0;
    result = SdbGetIndex(0, (unsigned int)(0x7007ULL), (unsigned int)(0x6001ULL), a4);
    if ((unsigned int)(result) == 0) goto loc_00AB34BD;
    v_stack_m98 = v_stack_m60;
    result = SdbFindFirstStringIndexedTag(0, (unsigned int)(0x7007ULL), (unsigned int)(0x6001ULL), v_stack_m68);
    goto loc_00AB34DE;
loc_00AB34BD:
    v_r12 = 0;
    v_stack_m98 = v_stack_m68;
    result = SdbpFindFirstNamedTagHelper(0, (unsigned int)(a6), (unsigned int)(0x7007ULL), (unsigned int)(0x6001ULL));
loc_00AB34DE:
    if ((unsigned int)(result) == 0) goto loc_00AB3569;
    v_stack_m80 = a5;
    v_stack_m88 = v_stack_m78;
    v_stack_m98 = v_stack_p20;
    result = SdbpCheckExe(v_stack_p8, 0, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), v_stack_p18);
    if ((unsigned int)(result) == 0) goto loc_00AB3529;
    if (v_stack_m78 == 2) goto loc_00AB3532;
    goto loc_00AB375F;
loc_00AB3529:
    if (((unsigned int)((unsigned int)(v_stack_p18))) > ((unsigned int)(1 + 15))) goto loc_00AB376B;
loc_00AB3532:
    if (0 == 0) goto loc_00AB3545;
    result = SdbFindNextStringIndexedTag(0, v_stack_m60, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), v_stack_p18);
    goto loc_00AB34DE;
loc_00AB3545:
    v_stack_m98 = v_stack_m68;
    result = SdbpFindNextNamedTagHelper(0, (unsigned int)(a6), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)(0x6001ULL));
    goto loc_00AB34DE;
loc_00AB3569:
    if ((*(unsigned __int64 *)(v_stack_p20 + 48)) == 0) goto loc_00AB366B;
    a4 = 0;
    result = SdbGetIndex(0, (unsigned int)(0x7007ULL), (unsigned int)(0x6020ULL), a4);
    if ((unsigned int)((unsigned int)((unsigned int)(result))) == 0) goto loc_00AB35BB;
    v_stack_m98 = v_stack_m60;
    result = SdbFindFirstStringIndexedTag(0, (unsigned int)(0x7007ULL), (unsigned int)(0x6020ULL), *(unsigned __int64 *)(v_stack_p20 + 48));
    goto loc_00AB35DC;
loc_00AB35BB:
    v_stack_m98 = result;
    result = SdbpFindFirstNamedTagHelper(0, (unsigned int)(a6), (unsigned int)(0x7007ULL), (unsigned int)(0x6020ULL));
loc_00AB35DC:
    if ((unsigned int)(result) == 0) goto loc_00AB366B;
    v_stack_m80 = a5;
    v_stack_m88 = v_stack_m78;
    v_stack_m98 = v_stack_p20;
    result = SdbpCheckExe(v_stack_p8, 0, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), v_stack_p18);
    if ((unsigned int)(result) == 0) goto loc_00AB3627;
    if (v_stack_m78 == 2) goto loc_00AB3630;
    goto loc_00AB375F;
loc_00AB3627:
    if (((unsigned int)((unsigned int)(v_stack_p18))) > ((unsigned int)(1 + 15))) goto loc_00AB376B;
loc_00AB3630:
    if ((unsigned int)((unsigned int)((unsigned int)(result))) == 0) goto loc_00AB3643;
    result = SdbFindNextStringIndexedTag(0, v_stack_m60, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), v_stack_p18);
    goto loc_00AB35DC;
loc_00AB3643:
    v_stack_m98 = *(unsigned __int64 *)(v_stack_p20 + 48);
    result = SdbpFindNextNamedTagHelper(0, (unsigned int)(a6), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)(0x6020ULL));
    goto loc_00AB35DC;
loc_00AB366B:
    a4 = 0;
    result = SdbGetIndex(0, (unsigned int)((unsigned int)((unsigned int)(0x7007ULL))), (unsigned int)(0x600BULL), a4);
    if ((unsigned int)(result) == 0) goto loc_00AB36AC;
    v_stack_m98 = v_stack_m60;
    result = SdbpFindFirstIndexedWildCardTag(0, (unsigned int)((unsigned int)((unsigned int)(0x7007ULL))), (unsigned int)(0x600BULL), v_stack_m68);
    goto loc_00AB3759;
loc_00AB36AC:
    v_r12 = 0;
    if (0 == (*(unsigned __int64 *)(v_stack_p8 + 8))) goto loc_00AB375F;
    v_stack_m90 = 1;
    v_stack_m98 = v_stack_m68;
    result = SdbpFindFirstNamedTagHelper(0, (unsigned int)(a6), (unsigned int)((unsigned int)((unsigned int)(0x7007ULL))), (unsigned int)(0x600BULL));
    goto loc_00AB3759;
loc_00AB36E1:
    v_stack_m80 = a5;
    v_stack_m88 = v_stack_m78;
    v_stack_m90 = 2;
    v_stack_m98 = v_stack_p20;
    result = SdbpCheckExe(v_stack_p8, 0, (unsigned int)((unsigned int)((unsigned int)(0x7007ULL))), v_stack_p18);
    if ((unsigned int)(result) == 0) goto loc_00AB3722;
    if (v_stack_m78 == 2) goto loc_00AB3727;
    goto loc_00AB375F;
loc_00AB3722:
    if (((unsigned int)((unsigned int)(v_stack_p18))) > ((unsigned int)(1 + 15))) goto loc_00AB376B;
loc_00AB3727:
    if (0 == 0) goto loc_00AB373A;
    result = SdbpFindNextIndexedWildCardTag(0, v_stack_m60, (unsigned int)((unsigned int)((unsigned int)(0x7007ULL))), v_stack_p18);
    goto loc_00AB3759;
loc_00AB373A:
    v_stack_m90 = 1;
    v_stack_m98 = v_stack_m68;
    result = SdbpFindNextNamedTagHelper(0, (unsigned int)(a6), (unsigned int)((unsigned int)((unsigned int)(0x7007ULL))), (unsigned int)(0x600BULL));
loc_00AB3759:
    if ((unsigned int)(result) != 0) goto loc_00AB36E1;
loc_00AB375F:
    if (((unsigned int)((unsigned int)(v_stack_p18))) > ((unsigned int)(1 + 15))) goto loc_00AB376B;
loc_00AB3764:
    if ((unsigned int)((unsigned int)(v_stack_p18)) == 0) goto loc_00AB3797;
loc_00AB376B:
loc_00AB376E:
    result = SdbFindFirstTag(0, (unsigned int)(*(unsigned int *)(a5)), (unsigned int)(0x6006ULL), (unsigned int)(0x600BULL));
    if ((unsigned int)(result) != 0) {
        a2 = (unsigned int)(result);
        a1 = a2;
        result = SdbGetStringTagPtr(a1, a2, (unsigned int)(0x6006ULL), (unsigned int)(0x600BULL));
    }
    v_r13 = (a5) + (8);
    v_rsi = ((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_p18)))))) - (1);
    if (condition_is_not_equal) goto loc_00AB376E;
loc_00AB3797:
    v_rsp = (v_rsp) + (128);
    return (unsigned int)((unsigned int)((unsigned int)(v_stack_p18)));
}
```

## 5. (Beta) C Style

```c
int64_t SdbpSearchDB(int64_t Arg1, int64_t Arg2, uint16_t Arg3, void *Arg4, void *Arg5, uint32_t Arg6)
{
    uint8_t *arg4 = (uint8_t *)Arg4;
    uint8_t *arg5 = (uint8_t *)Arg5;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m40;
    uint64_t v_stack_m50;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m74;
    uint32_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint32_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_p10;
    uint32_t v_stack_p18;
    uint64_t v_stack_p20;
    uint32_t v_stack_p30;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(void **)(local_rsp + 0x20) = Arg4;
    *(uint16_t *)(local_rsp + 0x18) = Arg3;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (128);
    result = 0;
    local_rdi = 0;
    v_stack_m40 = 0;
    v_stack_p18 = 0;
    Arg2 = 0;
    v_stack_m60 = v_xmm0;
    v_stack_m50 = v_xmm0;
    result = memset(Arg5, Arg2, 128, Arg4);
    Arg2 = 0;
    v_stack_m68 = *(uint64_t *)(arg4 + 0x28);
    result = SdbFindFirstTag(0, Arg2, (uint32_t)(0x7001ULL), Arg4);
    v_stack_p30 = (uint32_t)(result);
    if ((uint32_t)(result) != 0) goto loc_00AB3331;
    result = AslLogCallPrintf((uint32_t)((uint32_t)(local_rdi + 1)), v_rip - 10970823, (uint32_t)(0x1133ULL), v_rip - 10970800);
    goto loc_00AB3764;
loc_00AB3331:
    Arg4 = 0;
    result = SdbGetIndex(0, (uint32_t)(0x7007ULL), (uint32_t)(0x600BULL), Arg4);
    if ((uint32_t)(result) == 0) goto loc_00AB3379;
    v_stack_m98 = v_stack_m60;
    result = SdbpFindFirstIndexedWildCardTag(0, (uint32_t)(0x7007ULL), (uint32_t)(0x600BULL), *(uint64_t *)(arg4 + 0x28));
    goto loc_00AB33AB;
loc_00AB3379:
    local_r12 = 0;
    if (0 == (*(uint64_t *)(v_stack_p8 + 0x8))) goto loc_00AB347F;
    v_stack_m90 = 1;
    v_stack_m98 = *(uint64_t *)(arg4 + 0x28);
    result = SdbpFindFirstNamedTagHelper(0, (uint32_t)(Arg6), (uint32_t)(0x7007ULL), (uint32_t)(0x600BULL));
loc_00AB33AB:
    if ((uint32_t)(result) == 0) goto loc_00AB347B;
    v_stack_m90 = v_stack_m70;
    v_stack_m98 = v_stack_m74;
    v_stack_m74 = 2;
    result = SdbpCheckForMatch(v_stack_p8, 0, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), v_stack_p20);
    if ((uint32_t)(result) == 0) goto loc_00AB3418;
    if (((uint32_t)((uint32_t)(v_stack_m74))) != 2) goto loc_00AB3418;
    if (0 < ((uint32_t)(1 + 15))) goto loc_00AB3437;
    result = AslLogCallPrintf(1, v_rip - 10971010, (uint32_t)(0x10DCULL), v_rip - 10970981);
    local_rdi = (uint32_t)((local_rdi) + (1));
    v_stack_p18 = (uint32_t)(local_rdi);
loc_00AB3418:
    if (((uint32_t)(local_rdi)) > ((uint32_t)(1 + 15))) goto loc_00AB376B;
loc_00AB3421:
    if (0 == 0) goto loc_00AB3457;
    result = SdbpFindNextIndexedWildCardTag(0, v_stack_m60, (uint32_t)(0x10DCULL), v_rip - 10970981);
    goto loc_00AB33AB;
loc_00AB3437:
    *(uint32_t *)(arg5 + local_rdi * 8) = (uint32_t)((uint32_t)((uint32_t)(result)));
    *(uint32_t *)(arg5 + local_rdi * 8 + 0x4) = (uint32_t)((uint32_t)(v_stack_m70));
    local_rdi = (uint32_t)((local_rdi) + (1));
    v_stack_p18 = (uint32_t)(local_rdi);
    v_stack_m78 = (uint32_t)(v_stack_m60);
    if (((uint32_t)(v_stack_m60)) == 2) goto loc_00AB3421;
    goto loc_00AB375F;
loc_00AB3457:
    v_stack_m90 = 1;
    v_stack_m98 = v_stack_m68;
    result = SdbpFindNextNamedTagHelper(0, (uint32_t)(Arg6), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)(0x600BULL));
    goto loc_00AB33AB;
loc_00AB347B:
loc_00AB347F:
    Arg4 = 0;
    result = SdbGetIndex(0, (uint32_t)(0x7007ULL), (uint32_t)(0x6001ULL), Arg4);
    if ((uint32_t)(result) == 0) goto loc_00AB34BD;
    v_stack_m98 = v_stack_m60;
    result = SdbFindFirstStringIndexedTag(0, (uint32_t)(0x7007ULL), (uint32_t)(0x6001ULL), v_stack_m68);
    goto loc_00AB34DE;
loc_00AB34BD:
    local_r12 = 0;
    v_stack_m98 = v_stack_m68;
    result = SdbpFindFirstNamedTagHelper(0, (uint32_t)(Arg6), (uint32_t)(0x7007ULL), (uint32_t)(0x6001ULL));
loc_00AB34DE:
    if ((uint32_t)(result) == 0) goto loc_00AB3569;
    v_stack_m80 = Arg5;
    v_stack_m88 = v_stack_m78;
    v_stack_m98 = v_stack_p20;
    result = SdbpCheckExe(v_stack_p8, 0, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), v_stack_p18);
    if ((uint32_t)(result) == 0) goto loc_00AB3529;
    if (v_stack_m78 == 2) goto loc_00AB3532;
    goto loc_00AB375F;
loc_00AB3529:
    if (((uint32_t)((uint32_t)(v_stack_p18))) > ((uint32_t)(1 + 15))) goto loc_00AB376B;
loc_00AB3532:
    if (0 == 0) goto loc_00AB3545;
    result = SdbFindNextStringIndexedTag(0, v_stack_m60, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), v_stack_p18);
    goto loc_00AB34DE;
loc_00AB3545:
    v_stack_m98 = v_stack_m68;
    result = SdbpFindNextNamedTagHelper(0, (uint32_t)(Arg6), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)(0x6001ULL));
    goto loc_00AB34DE;
loc_00AB3569:
    if ((*(uint64_t *)(v_stack_p20 + 0x30)) == 0) goto loc_00AB366B;
    Arg4 = 0;
    result = SdbGetIndex(0, (uint32_t)(0x7007ULL), (uint32_t)(0x6020ULL), Arg4);
    if ((uint32_t)((uint32_t)((uint32_t)(result))) == 0) goto loc_00AB35BB;
    v_stack_m98 = v_stack_m60;
    result = SdbFindFirstStringIndexedTag(0, (uint32_t)(0x7007ULL), (uint32_t)(0x6020ULL), *(uint64_t *)(v_stack_p20 + 0x30));
    goto loc_00AB35DC;
loc_00AB35BB:
    v_stack_m98 = result;
    result = SdbpFindFirstNamedTagHelper(0, (uint32_t)(Arg6), (uint32_t)(0x7007ULL), (uint32_t)(0x6020ULL));
loc_00AB35DC:
    if ((uint32_t)(result) == 0) goto loc_00AB366B;
    v_stack_m80 = Arg5;
    v_stack_m88 = v_stack_m78;
    v_stack_m98 = v_stack_p20;
    result = SdbpCheckExe(v_stack_p8, 0, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), v_stack_p18);
    if ((uint32_t)(result) == 0) goto loc_00AB3627;
    if (v_stack_m78 == 2) goto loc_00AB3630;
    goto loc_00AB375F;
loc_00AB3627:
    if (((uint32_t)((uint32_t)(v_stack_p18))) > ((uint32_t)(1 + 15))) goto loc_00AB376B;
loc_00AB3630:
    if ((uint32_t)((uint32_t)((uint32_t)(result))) == 0) goto loc_00AB3643;
    result = SdbFindNextStringIndexedTag(0, v_stack_m60, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), v_stack_p18);
    goto loc_00AB35DC;
loc_00AB3643:
    v_stack_m98 = *(uint64_t *)(v_stack_p20 + 0x30);
    result = SdbpFindNextNamedTagHelper(0, (uint32_t)(Arg6), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)(0x6020ULL));
    goto loc_00AB35DC;
loc_00AB366B:
    Arg4 = 0;
    result = SdbGetIndex(0, (uint32_t)((uint32_t)((uint32_t)(0x7007ULL))), (uint32_t)(0x600BULL), Arg4);
    if ((uint32_t)(result) == 0) goto loc_00AB36AC;
    v_stack_m98 = v_stack_m60;
    result = SdbpFindFirstIndexedWildCardTag(0, (uint32_t)((uint32_t)((uint32_t)(0x7007ULL))), (uint32_t)(0x600BULL), v_stack_m68);
    goto loc_00AB3759;
loc_00AB36AC:
    local_r12 = 0;
    if (0 == (*(uint64_t *)(v_stack_p8 + 0x8))) goto loc_00AB375F;
    v_stack_m90 = 1;
    v_stack_m98 = v_stack_m68;
    result = SdbpFindFirstNamedTagHelper(0, (uint32_t)(Arg6), (uint32_t)((uint32_t)((uint32_t)(0x7007ULL))), (uint32_t)(0x600BULL));
    goto loc_00AB3759;
loc_00AB36E1:
    v_stack_m80 = Arg5;
    v_stack_m88 = v_stack_m78;
    v_stack_m90 = 2;
    v_stack_m98 = v_stack_p20;
    result = SdbpCheckExe(v_stack_p8, 0, (uint32_t)((uint32_t)((uint32_t)(0x7007ULL))), v_stack_p18);
    if ((uint32_t)(result) == 0) goto loc_00AB3722;
    if (v_stack_m78 == 2) goto loc_00AB3727;
    goto loc_00AB375F;
loc_00AB3722:
    if (((uint32_t)((uint32_t)(v_stack_p18))) > ((uint32_t)(1 + 15))) goto loc_00AB376B;
loc_00AB3727:
    if (0 == 0) goto loc_00AB373A;
    result = SdbpFindNextIndexedWildCardTag(0, v_stack_m60, (uint32_t)((uint32_t)((uint32_t)(0x7007ULL))), v_stack_p18);
    goto loc_00AB3759;
loc_00AB373A:
    v_stack_m90 = 1;
    v_stack_m98 = v_stack_m68;
    result = SdbpFindNextNamedTagHelper(0, (uint32_t)(Arg6), (uint32_t)((uint32_t)((uint32_t)(0x7007ULL))), (uint32_t)(0x600BULL));
loc_00AB3759:
    if ((uint32_t)(result) != 0) goto loc_00AB36E1;
loc_00AB375F:
    if (((uint32_t)((uint32_t)(v_stack_p18))) > ((uint32_t)(1 + 15))) goto loc_00AB376B;
loc_00AB3764:
    if ((uint32_t)((uint32_t)(v_stack_p18)) == 0) goto loc_00AB3797;
loc_00AB376B:
loc_00AB376E:
    result = SdbFindFirstTag(0, (uint32_t)(*(uint32_t *)(arg5)), (uint32_t)(0x6006ULL), (uint32_t)(0x600BULL));
    if ((uint32_t)(result) != 0) {
        Arg2 = (uint32_t)(result);
        Arg1 = Arg2;
        result = SdbGetStringTagPtr(Arg1, Arg2, (uint32_t)(0x6006ULL), (uint32_t)(0x600BULL));
    }
    local_r13 = (Arg5) + (8);
    local_rsi = ((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_p18)))))) - (1);
    if (condition_is_not_equal) goto loc_00AB376E;
loc_00AB3797:
    local_rsp = (local_rsp) + (128);
    return (uint32_t)((uint32_t)((uint32_t)(v_stack_p18)));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg4` | `+ 0x28` | `64` | `R` |
| `Arg5` | `+ 0x0` | `32` | `R` |
| `Arg5` | `+ 0x0 + rdi*8` | `32` | `W` |
| `Arg5` | `+ 0x4 + rdi*8` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AB3294&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
