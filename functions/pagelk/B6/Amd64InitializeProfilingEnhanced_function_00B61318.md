# Amd64InitializeProfilingEnhanced

- RVA: `0x00B61318`–`0x00B618CF` (길이 `1,463` bytes)
- VA: `0x0000000140B61318`
- 실행 섹션: `PAGELK`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C5030`
- 디코드: `367`개 명령, `1,463/1,463` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **15**; 고유 호출 대상: **8**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **28**

### Outgoing calls
- `0x00B614FA` → [HalpQueryMaximumRegisteredProcessorCount](../../text/54/HalpQueryMaximumRegisteredProcessorCount_function_00543BE8.md) (function, `0x00543BE8`)
- `0x00B61551` → [HalpMmAllocateMemory](../../text/54/HalpMmAllocateMemory_function_00544974.md) (function, `0x00544974`)
- `0x00B6156B` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00B615A0` → [HalpMmAllocateMemory](../../text/54/HalpMmAllocateMemory_function_00544974.md) (function, `0x00544974`)
- `0x00B615B6` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00B615E4` → [HalpMmAllocateMemory](../../text/54/HalpMmAllocateMemory_function_00544974.md) (function, `0x00544974`)
- `0x00B615FA` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00B61635` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00B61672` → [HalpMmAllocateMemory](../../text/54/HalpMmAllocateMemory_function_00544974.md) (function, `0x00544974`)
- `0x00B61690` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00B61748` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00B617C3` → [Amd64GetGenericPerfEvent](../../text/56/Amd64GetGenericPerfEvent_function_0056C77C.md) (function, `0x0056C77C`)
- `0x00B61856` → [KeAddProcessorAffinityEx](../../text/25/KeAddProcessorAffinityEx_function_0025B6F0.md) (function, `0x0025B6F0`)
- `0x00B6188D` → [Amd64FreeCounter](../../text/56/Amd64FreeCounter_function_0056C524.md) (function, `0x0056C524`)
- `0x00B618A4` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [Amd64InitializeProfiling](Amd64InitializeProfiling_function_00B612F0.md) at `0x00B612FD`

### Static image references
- `0x00B61334` → RVA `0x00E0A740` (`.data`; read)
- `0x00B6134C` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x00B61362` → RVA `0x00F8F940` (`.data`; read)
- `0x00B6139F` → RVA `0x00F8F8A0` (`.data`; read/write)
- `0x00B613CF` → RVA `0x00042F20` (`.rdata`; read)
- `0x00B613DA` → RVA `0x00042F10` (`.rdata`; read)
- `0x00B613E2` → RVA `0x00F8F8C0` (`.data`; write)
- `0x00B613EA` → RVA `0x00F8F940` (`.data`; write)
- `0x00B613FE` → RVA `0x00042F40` (`.rdata`; read)
- `0x00B6141D` → RVA `0x00042F30` (`.rdata`; read)
- `0x00B6142A` → RVA `0x00F8F890` (`.data`; read)
- `0x00B61431` → RVA `0x00F8F898` (`.data`; write)
- `0x00B61438` → RVA `0x00F8F890` (`.data`; write)
- `0x00B6148C` → RVA `0x00F8F900` (`.data`; read)
- `0x00B61493` → RVA `0x00F8F908` (`.data`; write)
- `0x00B6149A` → RVA `0x00F8F900` (`.data`; write)
- `0x00B614EC` → RVA `0x000260D8` (`.rdata`; read)
- `0x00B614F3` → RVA `0x00FC2BC8` (`.data`; write)
- `0x00B6161B` → RVA `0x00026288` (`.rdata`; read)
- `0x00B61640` → RVA `0x00F8F920` (`.data`; read)
- `0x00B6174E` → RVA `0x00FC2C40` (`.data`; read)
- `0x00B61755` → RVA `0x00FC2BD0` (`.data`; write)
- `0x00B6175C` → RVA `0x00FC2C48` (`.data`; write)
- `0x00B6176A` → RVA `0x00FC2C40` (`.data`; write)
- `0x00B6179C` → RVA `0x00F8F8A0` (`.data`; read)
- `0x00B617DA` → RVA `0x00FC2C48` (`.data`; read)
- `0x00B617F4` → RVA `0x00FC2C20` (`.data`; read/write)
- `0x00B61849` → RVA `0x00E05570` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **15**
  - `0x00B614FA` → [HalpQueryMaximumRegisteredProcessorCount](../../text/54/HalpQueryMaximumRegisteredProcessorCount_function_00543BE8.md) (`PAGELK` → `.text`)
  - `0x00B61551` → [HalpMmAllocateMemory](../../text/54/HalpMmAllocateMemory_function_00544974.md) (`PAGELK` → `.text`)
  - `0x00B6156B` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGELK` → `.text`)
  - `0x00B615A0` → [HalpMmAllocateMemory](../../text/54/HalpMmAllocateMemory_function_00544974.md) (`PAGELK` → `.text`)
  - `0x00B615B6` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGELK` → `.text`)
  - `0x00B615E4` → [HalpMmAllocateMemory](../../text/54/HalpMmAllocateMemory_function_00544974.md) (`PAGELK` → `.text`)
  - `0x00B615FA` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGELK` → `.text`)
  - `0x00B61635` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGELK` → `.text`)
  - `0x00B61672` → [HalpMmAllocateMemory](../../text/54/HalpMmAllocateMemory_function_00544974.md) (`PAGELK` → `.text`)
  - `0x00B61690` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGELK` → `.text`)
  - `0x00B61748` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGELK` → `.text`)
  - `0x00B617C3` → [Amd64GetGenericPerfEvent](../../text/56/Amd64GetGenericPerfEvent_function_0056C77C.md) (`PAGELK` → `.text`)
  - `0x00B61856` → [KeAddProcessorAffinityEx](../../text/25/KeAddProcessorAffinityEx_function_0025B6F0.md) (`PAGELK` → `.text`)
  - `0x00B6188D` → [Amd64FreeCounter](../../text/56/Amd64FreeCounter_function_0056C524.md) (`PAGELK` → `.text`)
  - `0x00B618A4` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGELK` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B61318  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00B6131D  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
00B61322  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
00B61327  57                              push rdi
00B61328  41 54                           push r12
00B6132A  41 55                           push r13
00B6132C  41 56                           push r14
00B6132E  41 57                           push r15
00B61330  48 83 EC 60                     sub rsp, 0x60
00B61334  48 8B 05 05 94 2A 00            mov rax, qword ptr [rip + 0x2a9405]
00B6133B  48 33 C4                        xor rax, rsp
00B6133E  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
00B61343  65 44 8B 3C 25 A4 01 00 00      mov r15d, dword ptr gs:[0x1a4]
00B6134C  4C 8D 2D AD EC 49 FF            lea r13, [rip - 0xb61353]
00B61353  33 FF                           xor edi, edi
00B61355  44 89 7C 24 34                  mov dword ptr [rsp + 0x34], r15d
00B6135A  48 89 7C 24 40                  mov qword ptr [rsp + 0x40], rdi
00B6135F  0F 57 C0                        xorps xmm0, xmm0
00B61362  48 8D 35 D7 E5 42 00            lea rsi, [rip + 0x42e5d7]
00B61369  44 8B F7                        mov r14d, edi
00B6136C  44 8B E7                        mov r12d, edi
00B6136F  8D 6F 12                        lea ebp, [rdi + 0x12]
00B61372  44 8D 57 04                     lea r10d, [rdi + 4]
00B61376  0F 11 44 24 48                  movups xmmword ptr [rsp + 0x48], xmm0
00B6137B  45 85 FF                        test r15d, r15d
00B6137E  0F 85 9F 04 00 00               jne 0x140b61823
00B61384  33 C9                           xor ecx, ecx
00B61386  44 8D 4F 06                     lea r9d, [rdi + 6]
00B6138A  B8 01 00 00 80                  mov eax, 0x80000001
00B6138F  0F A2                           cpuid
00B61391  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
00B61395  89 5C 24 4C                     mov dword ptr [rsp + 0x4c], ebx
00B61399  0F BA E1 17                     bt ecx, 0x17
00B6139D  73 30                           jae 0x140b613cf
00B6139F  83 0D FA E4 42 00 01            or dword ptr [rip + 0x42e4fa], 1
00B613A6  45 8B F9                        mov r15d, r9d
00B613A9  BA 00 02 01 C0                  mov edx, 0xc0010200
00B613AE  8B DF                           mov ebx, edi
00B613B0  45 8B C1                        mov r8d, r9d
00B613B3  8D 42 01                        lea eax, [rdx + 1]
00B613B6  89 14 33                        mov dword ptr [rbx + rsi], edx
00B613B9  42 89 84 2B C0 F8 F8 00         mov dword ptr [rbx + r13 + 0xf8f8c0], eax
00B613C1  83 C2 02                        add edx, 2
00B613C4  49 03 DA                        add rbx, r10
00B613C7  49 83 E8 01                     sub r8, 1
00B613CB  75 E6                           jne 0x140b613b3
00B613CD  EB 23                           jmp 0x140b613f2
00B613CF  66 0F 6F 05 49 1B 4E FF         movdqa xmm0, xmmword ptr [rip - 0xb1e4b7]
00B613D7  45 8B FA                        mov r15d, r10d
00B613DA  66 0F 6F 0D 2E 1B 4E FF         movdqa xmm1, xmmword ptr [rip - 0xb1e4d2]
00B613E2  F3 0F 7F 05 D6 E4 42 00         movdqu xmmword ptr [rip + 0x42e4d6], xmm0
00B613EA  F3 0F 7F 0D 4E E5 42 00         movdqu xmmword ptr [rip + 0x42e54e], xmm1
00B613F2  0F BA E1 18                     bt ecx, 0x18
00B613F6  73 47                           jae 0x140b6143f
00B613F8  0F BA E1 16                     bt ecx, 0x16
00B613FC  73 41                           jae 0x140b6143f
00B613FE  66 0F 6F 05 3A 1B 4E FF         movdqa xmm0, xmmword ptr [rip - 0xb1e4c6]
00B61406  45 8B E2                        mov r12d, r10d
00B61409  83 0D 90 E4 42 00 02            or dword ptr [rip + 0x42e490], 2
00B61410  41 8B C7                        mov eax, r15d
00B61413  F3 41 0F 7F 84 85 C0 F8 F8 00   movdqu xmmword ptr [r13 + rax*4 + 0xf8f8c0], xmm0
00B6141D  66 0F 6F 05 0B 1B 4E FF         movdqa xmm0, xmmword ptr [rip - 0xb1e4f5]
00B61425  F3 0F 7F 04 86                  movdqu xmmword ptr [rsi + rax*4], xmm0
00B6142A  48 8D 05 5F E4 42 00            lea rax, [rip + 0x42e45f]
00B61431  48 89 05 60 E4 42 00            mov qword ptr [rip + 0x42e460], rax
00B61438  48 89 05 51 E4 42 00            mov qword ptr [rip + 0x42e451], rax
00B6143F  0F BA E1 1C                     bt ecx, 0x1c
00B61443  73 5C                           jae 0x140b614a1
00B61445  0F BA E1 16                     bt ecx, 0x16
00B61449  73 56                           jae 0x140b614a1
00B6144B  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
00B61454  43 8D 14 27                     lea edx, [r15 + r12]
00B61458  44 09 15 41 E4 42 00            or dword ptr [rip + 0x42e441], r10d
00B6145F  45 8B F2                        mov r14d, r10d
00B61462  80 78 40 16                     cmp byte ptr [rax + 0x40], 0x16
00B61466  74 03                           je 0x140b6146b
00B61468  45 8B F1                        mov r14d, r9d
00B6146B  BB 30 02 01 C0                  mov ebx, 0xc0010230
00B61470  45 8B C6                        mov r8d, r14d
00B61473  8D 43 01                        lea eax, [rbx + 1]
00B61476  89 1C 96                        mov dword ptr [rsi + rdx*4], ebx
00B61479  41 89 84 95 C0 F8 F8 00         mov dword ptr [r13 + rdx*4 + 0xf8f8c0], eax
00B61481  83 C3 02                        add ebx, 2
00B61484  FF C2                           inc edx
00B61486  49 83 E8 01                     sub r8, 1
00B6148A  75 E7                           jne 0x140b61473
00B6148C  48 8D 05 6D E4 42 00            lea rax, [rip + 0x42e46d]
00B61493  48 89 05 6E E4 42 00            mov qword ptr [rip + 0x42e46e], rax
00B6149A  48 89 05 5F E4 42 00            mov qword ptr [rip + 0x42e45f], rax
00B614A1  33 C9                           xor ecx, ecx
00B614A3  B8 00 00 00 80                  mov eax, 0x80000000
00B614A8  0F A2                           cpuid
00B614AA  89 5C 24 4C                     mov dword ptr [rsp + 0x4c], ebx
00B614AE  3D 08 00 00 80                  cmp eax, 0x80000008
00B614B3  72 37                           jb 0x140b614ec
00B614B5  33 C9                           xor ecx, ecx
00B614B7  B8 08 00 00 80                  mov eax, 0x80000008
00B614BC  0F A2                           cpuid
00B614BE  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
00B614C2  F6 C3 02                        test bl, 2
00B614C5  74 25                           je 0x140b614ec
00B614C7  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
00B614D0  80 78 40 17                     cmp byte ptr [rax + 0x40], 0x17
00B614D4  75 0F                           jne 0x140b614e5
00B614D6  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
00B614DF  80 78 43 1F                     cmp byte ptr [rax + 0x43], 0x1f
00B614E3  72 07                           jb 0x140b614ec
00B614E5  83 0D B4 E3 42 00 08            or dword ptr [rip + 0x42e3b4], 8
00B614EC  48 8D 05 E5 4B 4C FF            lea rax, [rip - 0xb3b41b]
00B614F3  48 89 05 CE 16 46 00            mov qword ptr [rip + 0x4616ce], rax
00B614FA  E8 E9 26 9E FF                  call 0x140543be8
00B614FF  8B C8                           mov ecx, eax
00B61501  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00B61505  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
00B6150E  8B EF                           mov ebp, edi
00B61510  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00B61515  4C 8D 48 58                     lea r9, [rax + 0x58]
00B61519  4C 89 4C 24 38                  mov qword ptr [rsp + 0x38], r9
00B6151E  4D 8B E9                        mov r13, r9
00B61521  3B E9                           cmp ebp, ecx
00B61523  0F 83 12 01 00 00               jae 0x140b6163b
00B61529  4C 8D 68 58                     lea r13, [rax + 0x58]
00B6152D  8B C5                           mov eax, ebp
00B6152F  43 8D 34 7F                     lea esi, [r15 + r15*2]
00B61533  C1 E6 04                        shl esi, 4
00B61536  8B CE                           mov ecx, esi
00B61538  48 8D 1C 40                     lea rbx, [rax + rax*2]
00B6153C  41 8D 47 FF                     lea eax, [r15 - 1]
00B61540  48 C1 E3 05                     shl rbx, 5
00B61544  49 03 5D 00                     add rbx, qword ptr [r13]
00B61548  89 3B                           mov dword ptr [rbx], edi
00B6154A  44 89 7B 04                     mov dword ptr [rbx + 4], r15d
00B6154E  89 43 08                        mov dword ptr [rbx + 8], eax
00B61551  E8 1E 34 9E FF                  call 0x140544974
00B61556  48 89 43 10                     mov qword ptr [rbx + 0x10], rax
00B6155A  48 85 C0                        test rax, rax
00B6155D  0F 84 B5 00 00 00               je 0x140b61618
00B61563  44 8B C6                        mov r8d, esi
00B61566  33 D2                           xor edx, edx
00B61568  48 8B C8                        mov rcx, rax
00B6156B  E8 D0 56 B6 FF                  call 0x1406c6c40
00B61570  48 C7 43 18 01 00 00 00         mov qword ptr [rbx + 0x18], 1
00B61578  89 7B 20                        mov dword ptr [rbx + 0x20], edi
00B6157B  48 89 7B 28                     mov qword ptr [rbx + 0x28], rdi
00B6157F  C7 43 30 64 00 00 00            mov dword ptr [rbx + 0x30], 0x64
00B61586  44 89 63 34                     mov dword ptr [rbx + 0x34], r12d
00B6158A  45 85 E4                        test r12d, r12d
00B6158D  74 2E                           je 0x140b615bd
00B6158F  41 8D 44 24 FF                  lea eax, [r12 - 1]
00B61594  43 8D 34 64                     lea esi, [r12 + r12*2]
00B61598  89 43 38                        mov dword ptr [rbx + 0x38], eax
00B6159B  C1 E6 04                        shl esi, 4
00B6159E  8B CE                           mov ecx, esi
00B615A0  E8 CF 33 9E FF                  call 0x140544974
00B615A5  48 89 43 40                     mov qword ptr [rbx + 0x40], rax
00B615A9  48 85 C0                        test rax, rax
00B615AC  74 6A                           je 0x140b61618
00B615AE  44 8B C6                        mov r8d, esi
00B615B1  33 D2                           xor edx, edx
00B615B3  48 8B C8                        mov rcx, rax
00B615B6  E8 85 56 B6 FF                  call 0x1406c6c40
00B615BB  EB 07                           jmp 0x140b615c4
00B615BD  89 7B 38                        mov dword ptr [rbx + 0x38], edi
00B615C0  48 89 7B 40                     mov qword ptr [rbx + 0x40], rdi
00B615C4  C7 43 48 65 00 00 00            mov dword ptr [rbx + 0x48], 0x65
00B615CB  44 89 73 4C                     mov dword ptr [rbx + 0x4c], r14d
00B615CF  45 85 F6                        test r14d, r14d
00B615D2  74 2D                           je 0x140b61601
00B615D4  41 8D 46 FF                     lea eax, [r14 - 1]
00B615D8  43 8D 34 76                     lea esi, [r14 + r14*2]
00B615DC  89 43 50                        mov dword ptr [rbx + 0x50], eax
00B615DF  C1 E6 04                        shl esi, 4
00B615E2  8B CE                           mov ecx, esi
00B615E4  E8 8B 33 9E FF                  call 0x140544974
00B615E9  48 89 43 58                     mov qword ptr [rbx + 0x58], rax
00B615ED  48 85 C0                        test rax, rax
00B615F0  74 26                           je 0x140b61618
00B615F2  44 8B C6                        mov r8d, esi
00B615F5  33 D2                           xor edx, edx
00B615F7  48 8B C8                        mov rcx, rax
00B615FA  E8 41 56 B6 FF                  call 0x1406c6c40
00B615FF  EB 07                           jmp 0x140b61608
00B61601  89 7B 50                        mov dword ptr [rbx + 0x50], edi
00B61604  48 89 7B 58                     mov qword ptr [rbx + 0x58], rdi
00B61608  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
00B6160D  FF C5                           inc ebp
00B6160F  8B 4C 24 30                     mov ecx, dword ptr [rsp + 0x30]
00B61613  E9 09 FF FF FF                  jmp 0x140b61521
00B61618  44 8B C6                        mov r8d, esi
00B6161B  4C 8D 0D 66 4C 4C FF            lea r9, [rip - 0xb3b39a]
00B61622  BA 02 90 00 00                  mov edx, 0x9002
00B61627  48 C7 44 24 20 5F 0C 00 00      mov qword ptr [rsp + 0x20], 0xc5f
00B61630  B9 5C 00 00 00                  mov ecx, 0x5c
00B61635  E8 26 C0 99 FF                  call 0x1404fd660
00B6163A  CC                              int3
00B6163B  4C 8B 4C 24 38                  mov r9, qword ptr [rsp + 0x38]
00B61640  4C 8D 25 D9 E2 42 00            lea r12, [rip + 0x42e2d9]
00B61647  8B EF                           mov ebp, edi
00B61649  3B E9                           cmp ebp, ecx
00B6164B  0F 83 FD 00 00 00               jae 0x140b6174e
00B61651  8B C5                           mov eax, ebp
00B61653  48 8D 1C 40                     lea rbx, [rax + rax*2]
00B61657  48 C1 E3 05                     shl rbx, 5
00B6165B  49 03 5D 00                     add rbx, qword ptr [r13]
00B6165F  8B 43 04                        mov eax, dword ptr [rbx + 4]
00B61662  4C 8B 73 10                     mov r14, qword ptr [rbx + 0x10]
00B61666  8D 34 40                        lea esi, [rax + rax*2]
00B61669  C1 E6 03                        shl esi, 3
00B6166C  85 F6                           test esi, esi
00B6166E  74 2C                           je 0x140b6169c
00B61670  8B CE                           mov ecx, esi
00B61672  E8 FD 32 9E FF                  call 0x140544974
00B61677  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00B6167C  4C 8B F8                        mov r15, rax
00B6167F  44 8B C6                        mov r8d, esi
00B61682  48 85 C0                        test rax, rax
00B61685  0F 84 A3 00 00 00               je 0x140b6172e
00B6168B  33 D2                           xor edx, edx
00B6168D  48 8B C8                        mov rcx, rax
00B61690  E8 AB 55 B6 FF                  call 0x1406c6c40
00B61695  4C 8B 4C 24 38                  mov r9, qword ptr [rsp + 0x38]
00B6169A  EB 05                           jmp 0x140b616a1
00B6169C  4C 8B 7C 24 40                  mov r15, qword ptr [rsp + 0x40]
00B616A1  44 8B C7                        mov r8d, edi
00B616A4  39 7B 04                        cmp dword ptr [rbx + 4], edi
00B616A7  76 25                           jbe 0x140b616ce
00B616A9  41 8B C0                        mov eax, r8d
00B616AC  41 FF C0                        inc r8d
00B616AF  48 8D 14 40                     lea rdx, [rax + rax*2]
00B616B3  48 03 D2                        add rdx, rdx
00B616B6  48 8D 04 40                     lea rax, [rax + rax*2]
00B616BA  49 8D 0C C7                     lea rcx, [r15 + rax*8]
00B616BE  49 89 4C D6 10                  mov qword ptr [r14 + rdx*8 + 0x10], rcx
00B616C3  41 89 7C D6 1C                  mov dword ptr [r14 + rdx*8 + 0x1c], edi
00B616C8  44 3B 43 04                     cmp r8d, dword ptr [rbx + 4]
00B616CC  72 DB                           jb 0x140b616a9
00B616CE  8B D7                           mov edx, edi
00B616D0  4C 8B 43 40                     mov r8, qword ptr [rbx + 0x40]
00B616D4  39 7B 34                        cmp dword ptr [rbx + 0x34], edi
00B616D7  76 1E                           jbe 0x140b616f7
00B616D9  8B C2                           mov eax, edx
00B616DB  FF C2                           inc edx
00B616DD  48 8D 0C 40                     lea rcx, [rax + rax*2]
00B616E1  48 03 C9                        add rcx, rcx
00B616E4  4D 89 64 C8 10                  mov qword ptr [r8 + rcx*8 + 0x10], r12
00B616E9  41 C7 44 C8 1C 64 00 00 00      mov dword ptr [r8 + rcx*8 + 0x1c], 0x64
00B616F2  3B 53 34                        cmp edx, dword ptr [rbx + 0x34]
00B616F5  72 E2                           jb 0x140b616d9
00B616F7  8B D7                           mov edx, edi
00B616F9  4C 8B 43 58                     mov r8, qword ptr [rbx + 0x58]
00B616FD  39 7B 4C                        cmp dword ptr [rbx + 0x4c], edi
00B61700  76 1E                           jbe 0x140b61720
00B61702  8B C2                           mov eax, edx
00B61704  FF C2                           inc edx
00B61706  48 8D 0C 40                     lea rcx, [rax + rax*2]
00B6170A  48 03 C9                        add rcx, rcx
00B6170D  4D 89 64 C8 10                  mov qword ptr [r8 + rcx*8 + 0x10], r12
00B61712  41 C7 44 C8 1C 65 00 00 00      mov dword ptr [r8 + rcx*8 + 0x1c], 0x65
00B6171B  3B 53 4C                        cmp edx, dword ptr [rbx + 0x4c]
00B6171E  72 E2                           jb 0x140b61702
00B61720  8B 4C 24 30                     mov ecx, dword ptr [rsp + 0x30]
00B61724  FF C5                           inc ebp
00B61726  4D 8B E9                        mov r13, r9
00B61729  E9 1B FF FF FF                  jmp 0x140b61649
00B6172E  4C 8D 0D 53 4B 4C FF            lea r9, [rip - 0xb3b4ad]
00B61735  48 C7 44 24 20 B7 0C 00 00      mov qword ptr [rsp + 0x20], 0xcb7
00B6173E  BA 02 90 00 00                  mov edx, 0x9002
00B61743  B9 5C 00 00 00                  mov ecx, 0x5c
00B61748  E8 13 BF 99 FF                  call 0x1404fd660
00B6174D  CC                              int3
00B6174E  4C 8D 1D EB 14 46 00            lea r11, [rip + 0x4614eb]
00B61755  48 89 3D 74 14 46 00            mov qword ptr [rip + 0x461474], rdi
00B6175C  4C 89 1D E5 14 46 00            mov qword ptr [rip + 0x4614e5], r11
00B61763  4C 8D 2D 96 E8 49 FF            lea r13, [rip - 0xb6176a]
00B6176A  4C 89 1D CF 14 46 00            mov qword ptr [rip + 0x4614cf], r11
00B61771  44 8B CF                        mov r9d, edi
00B61774  BD 12 00 00 00                  mov ebp, 0x12
00B61779  41 8B C1                        mov eax, r9d
00B6177C  48 8D 1C 80                     lea rbx, [rax + rax*4]
00B61780  48 C1 E3 06                     shl rbx, 6
00B61784  46 8A 94 2B 6D 55 E0 00         mov r10b, byte ptr [rbx + r13 + 0xe0556d]
00B6178C  45 84 D2                        test r10b, r10b
00B6178F  74 20                           je 0x140b617b1
00B61791  42 83 BC 2B 50 55 E0 00 20      cmp dword ptr [rbx + r13 + 0xe05550], 0x20
00B6179A  75 15                           jne 0x140b617b1
00B6179C  8B 05 FE E0 42 00               mov eax, dword ptr [rip + 0x42e0fe]
00B617A2  A8 08                           test al, 8
00B617A4  74 0B                           je 0x140b617b1
00B617A6  44 8A D7                        mov r10b, dil
00B617A9  42 88 BC 2B 6D 55 E0 00         mov byte ptr [rbx + r13 + 0xe0556d], dil
00B617B1  4A 39 BC 2B 80 56 E0 00         cmp qword ptr [rbx + r13 + 0xe05680], rdi
00B617B9  75 1A                           jne 0x140b617d5
00B617BB  42 8B 8C 2B 50 55 E0 00         mov ecx, dword ptr [rbx + r13 + 0xe05550]
00B617C3  E8 B4 AF A0 FF                  call 0x14056c77c
00B617C8  48 85 C0                        test rax, rax
00B617CB  74 08                           je 0x140b617d5
00B617CD  4A 89 84 2B 80 56 E0 00         mov qword ptr [rbx + r13 + 0xe05680], rax
00B617D5  45 84 D2                        test r10b, r10b
00B617D8  75 31                           jne 0x140b6180b
00B617DA  48 8B 0D 67 14 46 00            mov rcx, qword ptr [rip + 0x461467]
00B617E1  49 8D 85 58 55 E0 00            lea rax, [r13 + 0xe05558]
00B617E8  48 03 C3                        add rax, rbx
00B617EB  4C 39 19                        cmp qword ptr [rcx], r11
00B617EE  0F 85 D4 00 00 00               jne 0x140b618c8
00B617F4  FF 05 26 14 46 00               inc dword ptr [rip + 0x461426]
00B617FA  4C 89 18                        mov qword ptr [rax], r11
00B617FD  48 89 48 08                     mov qword ptr [rax + 8], rcx
00B61801  48 89 01                        mov qword ptr [rcx], rax
00B61804  48 89 05 3D 14 46 00            mov qword ptr [rip + 0x46143d], rax
00B6180B  41 FF C1                        inc r9d
00B6180E  44 3B CD                        cmp r9d, ebp
00B61811  0F 82 62 FF FF FF               jb 0x140b61779
00B61817  44 8B 7C 24 34                  mov r15d, dword ptr [rsp + 0x34]
00B6181C  48 8D 35 1D E1 42 00            lea rsi, [rip + 0x42e11d]
00B61823  8B 05 77 E0 42 00               mov eax, dword ptr [rip + 0x42e077]
00B61829  A8 08                           test al, 8
00B6182B  74 1C                           je 0x140b61849
00B6182D  B9 15 00 01 C0                  mov ecx, 0xc0010015
00B61832  0F 32                           rdmsr
00B61834  48 C1 E2 20                     shl rdx, 0x20
00B61838  48 0B C2                        or rax, rdx
00B6183B  48 0F BA E8 1E                  bts rax, 0x1e
00B61840  48 8B D0                        mov rdx, rax
00B61843  48 C1 EA 20                     shr rdx, 0x20
00B61847  0F 30                           wrmsr
00B61849  48 8D 1D 20 3D 2A 00            lea rbx, [rip + 0x2a3d20]
00B61850  41 8B D7                        mov edx, r15d
00B61853  48 8B CB                        mov rcx, rbx
00B61856  E8 95 9E 6F FF                  call 0x14025b6f0
00B6185B  48 81 C3 40 01 00 00            add rbx, 0x140
00B61862  48 83 ED 01                     sub rbp, 1
00B61866  75 E8                           jne 0x140b61850
00B61868  41 8B C7                        mov eax, r15d
00B6186B  49 8B 84 C5 40 8C FC 00         mov rax, qword ptr [r13 + rax*8 + 0xfc8c40]
00B61873  48 8B 58 58                     mov rbx, qword ptr [rax + 0x58]
00B61877  48 85 DB                        test rbx, rbx
00B6187A  74 20                           je 0x140b6189c
00B6187C  8B 5B 04                        mov ebx, dword ptr [rbx + 4]
00B6187F  85 DB                           test ebx, ebx
00B61881  74 19                           je 0x140b6189c
00B61883  8B 0E                           mov ecx, dword ptr [rsi]
00B61885  33 C0                           xor eax, eax
00B61887  33 D2                           xor edx, edx
00B61889  0F 30                           wrmsr
00B6188B  8B CF                           mov ecx, edi
00B6188D  E8 92 AC A0 FF                  call 0x14056c524
00B61892  FF C7                           inc edi
00B61894  48 8D 76 04                     lea rsi, [rsi + 4]
00B61898  3B FB                           cmp edi, ebx
00B6189A  72 E7                           jb 0x140b61883
00B6189C  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00B618A1  48 33 CC                        xor rcx, rsp
00B618A4  E8 97 AD B4 FF                  call 0x1406ac640
00B618A9  4C 8D 5C 24 60                  lea r11, [rsp + 0x60]
00B618AE  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
00B618B2  49 8B 6B 38                     mov rbp, qword ptr [r11 + 0x38]
00B618B6  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
00B618BA  49 8B E3                        mov rsp, r11
00B618BD  41 5F                           pop r15
00B618BF  41 5E                           pop r14
00B618C1  41 5D                           pop r13
00B618C3  41 5C                           pop r12
00B618C5  5F                              pop rdi
00B618C6  C3                              ret
00B618C7  CC                              int3
00B618C8  B9 03 00 00 00                  mov ecx, 3
00B618CD  CD 29                           int 0x29
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Amd64InitializeProfilingEnhanced(int a1)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned int v_stack_m3C;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned int v_stack_m54;
    unsigned int v_stack_m58;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (96);
    result = (*(unsigned __int64 *)(v_rip + 2790405)) ^ (v_rsp);
    v_stack_m30 = result;
    v_rdi = 0;
    v_stack_m54 = (unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))));
    v_stack_m48 = 0;
    v_stack_m40 = v_xmm0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420)))) != 0) goto loc_00B61823;
    a1 = 0;
    v_stack_m40 = (unsigned int)((unsigned int)(0x80000001ULL));
    v_stack_m3C = (unsigned int)(v_rbx);
    if (condition_is_above_or_equal) goto loc_00B613CF;
loc_00B613B3:
    *(unsigned int *)(0 + v_rip + 4384215 * 1) = (unsigned int)((unsigned int)(0xC0010200ULL));
    *(unsigned int *)(0 + v_rip - 11932499 * 1 + 16316608) = (unsigned int)((unsigned int)(0xC0010200ULL) + 1);
    a2 = (unsigned int)(((unsigned int)(0xC0010200ULL)) + (2));
    v_rbx = (0) + (v_rdi + 4);
    a3 = ((unsigned int)((unsigned int)(v_rdi + 6))) - (1);
    if (condition_is_not_equal) goto loc_00B613B3;
    goto loc_00B613F2;
loc_00B613CF:
    *(unsigned __int64 *)(v_rip + 4383958) = v_xmm0;
    *(unsigned __int64 *)(v_rip + 4384078) = v_xmm1;
loc_00B613F2:
    if (condition_is_above_or_equal) goto loc_00B6143F;
    result = (unsigned int)(0xC0010200ULL) + 1;
    v_r12 = 0;
    if (!(condition_is_above_or_equal)) {
        v_r12 = (unsigned int)(v_rdi + 4);
        result = (unsigned int)((unsigned int)((unsigned int)(v_rdi + 4)));
        *(unsigned __int64 *)(v_rip - 11932499 + result * 4 + 16316608) = v_xmm0;
        *(unsigned __int64 *)(v_rip + 4384215 + result * 4) = v_xmm0;
        result = v_rip + 4383839;
        *(unsigned __int64 *)(v_rip + 4383840) = result;
        *(unsigned __int64 *)(v_rip + 4383825) = result;
    }
    if (condition_is_above_or_equal) goto loc_00B614A1;
    if (condition_is_above_or_equal) goto loc_00B614A1;
    v_r14 = (unsigned int)((unsigned int)(v_rdi + 4));
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 64)) != 22) {
        v_r14 = (unsigned int)(v_rdi + 6);
    }
loc_00B61473:
    *(unsigned int *)(v_rip + 4384215 + (unsigned int)((unsigned int)(v_rdi + 4)) + v_r12 * 1 * 4) = (unsigned int)((unsigned int)(0xC0010230ULL));
    *(unsigned int *)(v_rip - 11932499 + (unsigned int)((unsigned int)(v_rdi + 4)) + v_r12 * 1 * 4 + 16316608) = (unsigned int)((unsigned int)(0xC0010230ULL) + 1);
    v_rbx = (unsigned int)(((unsigned int)(0xC0010230ULL)) + (2));
    a2 = (unsigned int)(((unsigned int)((unsigned int)(v_rdi + 4)) + v_r12 * 1) + 1);
    a3 = ((unsigned int)((unsigned int)(v_r14))) - (1);
    if (condition_is_not_equal) goto loc_00B61473;
    *(unsigned __int64 *)(v_rip + 4383854) = v_rip + 4383853;
    *(unsigned __int64 *)(v_rip + 4383839) = v_rip + 4383853;
loc_00B614A1:
    a1 = 0;
    v_stack_m3C = (unsigned int)(v_rbx);
    if (((unsigned int)((unsigned int)(0x80000000ULL))) < 0x80000008ULL) goto loc_00B614EC;
    a1 = 0;
    v_stack_m40 = (unsigned int)((unsigned int)(0x80000008ULL));
    if ((((unsigned __int8)(v_rbx)) & (2)) == 0) goto loc_00B614EC;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 64)) != 23) goto loc_00B614E5;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 67)) >= 31) {
    }
    *(unsigned __int64 *)(v_rip + 4593358) = v_rip - 11777051;
    result = HalpQueryMaximumRegisteredProcessorCount(a1, a2, a3, v_rdi + 6);
    v_stack_m58 = (unsigned int)(result);
    v_stack_m40 = *(unsigned __int64 *)(gs_base + (0 + 32));
    v_stack_m50 = *(unsigned __int64 *)(gs_base + (0 + 32)) + 88;
loc_00B61521:
    if (0 >= ((unsigned int)((unsigned int)((unsigned int)(result))))) goto loc_00B6163B;
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)(v_rdi + 4)) + (unsigned int)((unsigned int)(v_rdi + 4)) * 2) << (4));
    v_rbx = (0 + 0 * 2) << (5);
    v_rbx = (v_rbx) + (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 88));
    *(unsigned int *)(v_rbx) = 0;
    *(unsigned int *)(v_rbx + 4) = (unsigned int)((unsigned int)((unsigned int)(v_rdi + 4)));
    *(unsigned int *)(v_rbx + 8) = (unsigned int)((unsigned int)((unsigned int)(v_rdi + 4)) - 1);
    result = HalpMmAllocateMemory((unsigned int)((unsigned int)(v_rsi)), a2, a3, *(unsigned __int64 *)(gs_base + (0 + 32)) + 88);
    *(unsigned __int64 *)(v_rbx + 16) = result;
    if (result == 0) goto loc_00B61618;
    a2 = 0;
    result = memset(result, a2, (unsigned int)((unsigned int)(v_rsi)), *(unsigned __int64 *)(gs_base + (0 + 32)) + 88);
    *(unsigned __int64 *)(v_rbx + 24) = 1;
    *(unsigned int *)(v_rbx + 32) = 0;
    *(unsigned __int64 *)(v_rbx + 40) = 0;
    *(unsigned int *)(v_rbx + 48) = 100;
    *(unsigned int *)(v_rbx + 52) = (unsigned int)(v_r12);
    if ((unsigned int)(v_r12) == 0) goto loc_00B615BD;
    *(unsigned int *)(v_rbx + 56) = (unsigned int)(v_r12 - 1);
    v_rsi = (unsigned int)((v_r12 + v_r12 * 2) << (4));
    result = HalpMmAllocateMemory((unsigned int)((unsigned int)(v_rsi)), a2, (unsigned int)((unsigned int)(v_rsi)), *(unsigned __int64 *)(gs_base + (0 + 32)) + 88);
    *(unsigned __int64 *)(v_rbx + 64) = result;
    if (result == 0) goto loc_00B61618;
    a2 = 0;
    result = memset(result, a2, (unsigned int)((unsigned int)(v_rsi)), *(unsigned __int64 *)(gs_base + (0 + 32)) + 88);
    goto loc_00B615C4;
loc_00B615BD:
    *(unsigned int *)(v_rbx + 56) = 0;
    *(unsigned __int64 *)(v_rbx + 64) = 0;
loc_00B615C4:
    *(unsigned int *)(v_rbx + 72) = 101;
    *(unsigned int *)(v_rbx + 76) = (unsigned int)(v_r14);
    if ((unsigned int)(v_r14) == 0) goto loc_00B61601;
    *(unsigned int *)(v_rbx + 80) = (unsigned int)(v_r14 - 1);
    v_rsi = (unsigned int)((v_r14 + v_r14 * 2) << (4));
    result = HalpMmAllocateMemory((unsigned int)((unsigned int)(v_rsi)), a2, (unsigned int)((unsigned int)(v_rsi)), *(unsigned __int64 *)(gs_base + (0 + 32)) + 88);
    *(unsigned __int64 *)(v_rbx + 88) = result;
    if (result == 0) goto loc_00B61618;
    a2 = 0;
    result = memset(result, a2, (unsigned int)((unsigned int)(v_rsi)), *(unsigned __int64 *)(gs_base + (0 + 32)) + 88);
    goto loc_00B61608;
loc_00B61601:
    *(unsigned int *)(v_rbx + 80) = 0;
    *(unsigned __int64 *)(v_rbx + 88) = 0;
loc_00B61608:
    v_rbp = (unsigned int)((0) + 1);
    goto loc_00B61521;
loc_00B61618:
    v_stack_m68 = 0xC5FULL;
    result = KeBugCheckEx(92, (unsigned int)(0x9002ULL), (unsigned int)((unsigned int)(v_rsi)), v_rip - 11776922);
loc_00B6163B:
loc_00B61649:
    if (0 >= 92) goto loc_00B6174E;
    v_rbx = (0 + 0 * 2) << (5);
    v_rbx = (v_rbx) + (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 88));
    v_rsi = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbx + 4)) + (unsigned int)(*(unsigned int *)(v_rbx + 4)) * 2) << (3));
    if ((unsigned int)(v_rsi) == 0) goto loc_00B6169C;
    result = HalpMmAllocateMemory((unsigned int)((unsigned int)(v_rsi)), (unsigned int)(0x9002ULL), (unsigned int)((unsigned int)(v_rsi)), v_stack_m50);
    v_stack_m48 = result;
    if (result == 0) goto loc_00B6172E;
    a2 = 0;
    result = memset(result, a2, (unsigned int)((unsigned int)(v_rsi)), v_stack_m50);
    goto loc_00B616A1;
loc_00B6169C:
loc_00B616A1:
    if ((*(unsigned int *)(v_rbx + 4)) <= 0) goto loc_00B616CE;
loc_00B616A9:
    a3 = (unsigned int)((0) + 1);
    a2 = (0 + 0 * 2) + (0 + 0 * 2);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 16) + a2 * 8 + 16) = v_stack_m48 + 0 + 0 * 2 * 8;
    *(unsigned int *)(*(unsigned __int64 *)(v_rbx + 16) + a2 * 8 + 28) = 0;
    if (((unsigned int)(a3)) < (*(unsigned int *)(v_rbx + 4))) goto loc_00B616A9;
loc_00B616CE:
    if ((*(unsigned int *)(v_rbx + 52)) <= 0) goto loc_00B616F7;
loc_00B616D9:
    a2 = (unsigned int)((0) + 1);
    a1 = (0 + 0 * 2) + (0 + 0 * 2);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 64) + a1 * 8 + 16) = v_rip + 4383449;
    *(unsigned int *)(*(unsigned __int64 *)(v_rbx + 64) + a1 * 8 + 28) = 100;
    if (((unsigned int)(a2)) < (*(unsigned int *)(v_rbx + 52))) goto loc_00B616D9;
loc_00B616F7:
    if ((*(unsigned int *)(v_rbx + 76)) <= 0) goto loc_00B61720;
loc_00B61702:
    a2 = (unsigned int)((0) + 1);
    a1 = (0 + 0 * 2) + (0 + 0 * 2);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 88) + a1 * 8 + 16) = v_rip + 4383449;
    *(unsigned int *)(*(unsigned __int64 *)(v_rbx + 88) + a1 * 8 + 28) = 101;
    if (((unsigned int)(a2)) < (*(unsigned int *)(v_rbx + 76))) goto loc_00B61702;
loc_00B61720:
    v_rbp = (unsigned int)((0) + 1);
    goto loc_00B61649;
loc_00B6172E:
    v_stack_m68 = 0xCB7ULL;
    result = KeBugCheckEx(92, (unsigned int)(0x9002ULL), *(unsigned __int64 *)(v_rbx + 88), v_rip - 11777197);
loc_00B6174E:
    *(unsigned __int64 *)(v_rip + 4592756) = 0;
    *(unsigned __int64 *)(v_rip + 4592869) = v_rip + 4592875;
    *(unsigned __int64 *)(v_rip + 4592847) = v_rip + 4592875;
loc_00B61779:
    v_rbx = (0 + 0 * 4) << (6);
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rbx + v_rip - 11933546 * 1 + 14701933)) == 0) goto loc_00B617B1;
    if ((*(unsigned int *)(v_rbx + v_rip - 11933546 * 1 + 14701904)) != 32) goto loc_00B617B1;
    v_r10 = *(unsigned __int8 *)(v_rbx + v_rip - 11933546 * 1 + 14701933);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 4382974)))) & (8)) != 0) {
        v_r10 = 0;
        *(unsigned __int8 *)(v_rbx + v_rip - 11933546 * 1 + 14701933) = 0;
    }
    if ((*(unsigned __int64 *)(v_rbx + v_rip - 11933546 * 1 + 14702208)) != 0) goto loc_00B617D5;
    result = Amd64GetGenericPerfEvent((unsigned int)(*(unsigned int *)(v_rbx + v_rip - 11933546 * 1 + 14701904)), (unsigned int)(0x9002ULL), *(unsigned __int64 *)(v_rbx + 88), 0);
    if (result != 0) {
        *(unsigned __int64 *)(v_rbx + v_rip - 11933546 * 1 + 14702208) = result;
    }
    if ((unsigned __int8)(v_r10) != 0) goto loc_00B6180B;
    result = (v_rip - 11933546 + 14701912) + (v_rbx);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4592743))) != (v_rip + 4592875)) goto loc_00B618C8;
    *(unsigned __int64 *)(result) = v_rip + 4592875;
    *(unsigned __int64 *)(result + 8) = *(unsigned __int64 *)(v_rip + 4592743);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4592743)) = result;
    *(unsigned __int64 *)(v_rip + 4592701) = result;
loc_00B6180B:
    a4 = (unsigned int)((0) + 1);
    if (((unsigned int)(a4)) < 18) goto loc_00B61779;
loc_00B61823:
    result = (unsigned int)(*(unsigned int *)(v_rip + 4382839));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 4382839)))) & (8)) != 0) {
        a1 = 0xC0010015ULL;
        a2 = ((unsigned int)(0x9002ULL)) << (32);
        result = ((unsigned int)(*(unsigned int *)(v_rip + 4382839))) | (a2);
        a2 = result;
        a2 = (a2) >> (32);
    }
loc_00B61850:
    result = KeAddProcessorAffinityEx(v_rip + 2768160, (unsigned int)((unsigned int)((unsigned int)(v_stack_m54))), *(unsigned __int64 *)(v_rbx + 88), a4);
    v_rbx = (v_rip + 2768160) + (320);
    v_rbp = (18) - (1);
    if (condition_is_not_equal) goto loc_00B61850;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 11933546 + (unsigned int)((unsigned int)((unsigned int)(v_stack_m54))) * 8 + 16550976) + 88) == 0) goto loc_00B6189C;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 11933546 + (unsigned int)((unsigned int)((unsigned int)(v_stack_m54))) * 8 + 16550976) + 88) + 4))) == 0) goto loc_00B6189C;
loc_00B61883:
    result = 0;
    a2 = 0;
    result = Amd64FreeCounter(0, a2, *(unsigned __int64 *)(v_rbx + 88), a4);
    v_rdi = (unsigned int)((v_rdi) + 1);
    if (((unsigned int)(v_rdi)) < ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 11933546 + (unsigned int)((unsigned int)((unsigned int)(v_stack_m54))) * 8 + 16550976) + 88) + 4))))) goto loc_00B61883;
loc_00B6189C:
    a1 = (v_stack_m30) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, *(unsigned __int64 *)(v_rbx + 88), a4);
    return result;
loc_00B618C8:
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t Amd64InitializeProfilingEnhanced(int32_t Arg1)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint32_t v_stack_m3C;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint32_t v_stack_m54;
    uint32_t v_stack_m58;
    uint64_t v_stack_m68;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (96);
    result = (*(uint64_t *)(v_rip + 0x2A9405)) ^ (local_rsp);
    v_stack_m30 = result;
    local_rdi = 0;
    v_stack_m54 = (uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))));
    v_stack_m48 = 0;
    v_stack_m40 = v_xmm0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4)))) != 0) goto loc_00B61823;
    Arg1 = 0;
    v_stack_m40 = (uint32_t)((uint32_t)(0x80000001ULL));
    v_stack_m3C = (uint32_t)(local_rbx);
    if (condition_is_above_or_equal) goto loc_00B613CF;
loc_00B613B3:
    *(uint32_t *)(0 + v_rip + 0x42E5D7 * 1) = (uint32_t)((uint32_t)(0xC0010200ULL));
    *(uint32_t *)(0 + v_rip - 0xB61353 * 1 + 0xF8F8C0) = (uint32_t)((uint32_t)(0xC0010200ULL) + 1);
    a2 = (uint32_t)(((uint32_t)(0xC0010200ULL)) + (2));
    local_rbx = (0) + (local_rdi + 4);
    a3 = ((uint32_t)((uint32_t)(local_rdi + 6))) - (1);
    if (condition_is_not_equal) goto loc_00B613B3;
    goto loc_00B613F2;
loc_00B613CF:
    *(uint64_t *)(v_rip + 0x42E4D6) = v_xmm0;
    *(uint64_t *)(v_rip + 0x42E54E) = v_xmm1;
loc_00B613F2:
    if (condition_is_above_or_equal) goto loc_00B6143F;
    result = (uint32_t)(0xC0010200ULL) + 1;
    local_r12 = 0;
    if (!(condition_is_above_or_equal)) {
        local_r12 = (uint32_t)(local_rdi + 4);
        result = (uint32_t)((uint32_t)((uint32_t)(local_rdi + 4)));
        *(uint64_t *)(v_rip - 0xB61353 + result * 4 + 0xF8F8C0) = v_xmm0;
        *(uint64_t *)(v_rip + 0x42E5D7 + result * 4) = v_xmm0;
        result = v_rip + 4383839;
        *(uint64_t *)(v_rip + 0x42E460) = result;
        *(uint64_t *)(v_rip + 0x42E451) = result;
    }
    if (condition_is_above_or_equal) goto loc_00B614A1;
    if (condition_is_above_or_equal) goto loc_00B614A1;
    local_r14 = (uint32_t)((uint32_t)(local_rdi + 4));
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x40)) != 22) {
        local_r14 = (uint32_t)(local_rdi + 6);
    }
loc_00B61473:
    *(uint32_t *)(v_rip + 0x42E5D7 + (uint32_t)((uint32_t)(local_rdi + 0x4)) + local_r12 * 1 * 4) = (uint32_t)((uint32_t)(0xC0010230ULL));
    *(uint32_t *)(v_rip - 0xB61353 + (uint32_t)((uint32_t)(local_rdi + 0x4)) + local_r12 * 1 * 4 + 0xF8F8C0) = (uint32_t)((uint32_t)(0xC0010230ULL) + 1);
    local_rbx = (uint32_t)(((uint32_t)(0xC0010230ULL)) + (2));
    a2 = (uint32_t)(((uint32_t)((uint32_t)(local_rdi + 4)) + local_r12 * 1) + 1);
    a3 = ((uint32_t)((uint32_t)(local_r14))) - (1);
    if (condition_is_not_equal) goto loc_00B61473;
    *(uint64_t *)(v_rip + 0x42E46E) = v_rip + 4383853;
    *(uint64_t *)(v_rip + 0x42E45F) = v_rip + 4383853;
loc_00B614A1:
    Arg1 = 0;
    v_stack_m3C = (uint32_t)(local_rbx);
    if (((uint32_t)((uint32_t)(0x80000000ULL))) < 0x80000008ULL) goto loc_00B614EC;
    Arg1 = 0;
    v_stack_m40 = (uint32_t)((uint32_t)(0x80000008ULL));
    if ((((uint8_t)(local_rbx)) & (2)) == 0) goto loc_00B614EC;
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x40)) != 23) goto loc_00B614E5;
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x43)) >= 31) {
    }
    *(uint64_t *)(v_rip + 0x4616CE) = v_rip - 11777051;
    result = HalpQueryMaximumRegisteredProcessorCount(Arg1, a2, a3, local_rdi + 6);
    v_stack_m58 = (uint32_t)(result);
    v_stack_m40 = *(uint64_t *)(gs_base + (0 + 0x20));
    v_stack_m50 = *(uint64_t *)(gs_base + (0 + 0x20)) + 88;
loc_00B61521:
    if (0 >= ((uint32_t)((uint32_t)((uint32_t)(result))))) goto loc_00B6163B;
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)(local_rdi + 4)) + (uint32_t)((uint32_t)(local_rdi + 4)) * 2) << (4));
    local_rbx = (0 + 0 * 2) << (5);
    local_rbx = (local_rbx) + (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x58));
    *(uint32_t *)(local_rbx) = 0;
    *(uint32_t *)(local_rbx + 0x4) = (uint32_t)((uint32_t)((uint32_t)(local_rdi + 4)));
    *(uint32_t *)(local_rbx + 0x8) = (uint32_t)((uint32_t)((uint32_t)(local_rdi + 4)) - 1);
    result = HalpMmAllocateMemory((uint32_t)((uint32_t)(local_rsi)), a2, a3, *(uint64_t *)(gs_base + (0 + 0x20)) + 88);
    *(uint64_t *)(local_rbx + 0x10) = result;
    if (result == 0) goto loc_00B61618;
    a2 = 0;
    result = memset(result, a2, (uint32_t)((uint32_t)(local_rsi)), *(uint64_t *)(gs_base + (0 + 0x20)) + 88);
    *(uint64_t *)(local_rbx + 0x18) = 1;
    *(uint32_t *)(local_rbx + 0x20) = 0;
    *(uint64_t *)(local_rbx + 0x28) = 0;
    *(uint32_t *)(local_rbx + 0x30) = 100;
    *(uint32_t *)(local_rbx + 0x34) = (uint32_t)(local_r12);
    if ((uint32_t)(local_r12) == 0) goto loc_00B615BD;
    *(uint32_t *)(local_rbx + 0x38) = (uint32_t)(local_r12 - 1);
    local_rsi = (uint32_t)((local_r12 + local_r12 * 2) << (4));
    result = HalpMmAllocateMemory((uint32_t)((uint32_t)(local_rsi)), a2, (uint32_t)((uint32_t)(local_rsi)), *(uint64_t *)(gs_base + (0 + 0x20)) + 88);
    *(uint64_t *)(local_rbx + 0x40) = result;
    if (result == 0) goto loc_00B61618;
    a2 = 0;
    result = memset(result, a2, (uint32_t)((uint32_t)(local_rsi)), *(uint64_t *)(gs_base + (0 + 0x20)) + 88);
    goto loc_00B615C4;
loc_00B615BD:
    *(uint32_t *)(local_rbx + 0x38) = 0;
    *(uint64_t *)(local_rbx + 0x40) = 0;
loc_00B615C4:
    *(uint32_t *)(local_rbx + 0x48) = 101;
    *(uint32_t *)(local_rbx + 0x4C) = (uint32_t)(local_r14);
    if ((uint32_t)(local_r14) == 0) goto loc_00B61601;
    *(uint32_t *)(local_rbx + 0x50) = (uint32_t)(local_r14 - 1);
    local_rsi = (uint32_t)((local_r14 + local_r14 * 2) << (4));
    result = HalpMmAllocateMemory((uint32_t)((uint32_t)(local_rsi)), a2, (uint32_t)((uint32_t)(local_rsi)), *(uint64_t *)(gs_base + (0 + 0x20)) + 88);
    *(uint64_t *)(local_rbx + 0x58) = result;
    if (result == 0) goto loc_00B61618;
    a2 = 0;
    result = memset(result, a2, (uint32_t)((uint32_t)(local_rsi)), *(uint64_t *)(gs_base + (0 + 0x20)) + 88);
    goto loc_00B61608;
loc_00B61601:
    *(uint32_t *)(local_rbx + 0x50) = 0;
    *(uint64_t *)(local_rbx + 0x58) = 0;
loc_00B61608:
    local_rbp = (uint32_t)((0) + 1);
    goto loc_00B61521;
loc_00B61618:
    v_stack_m68 = 0xC5FULL;
    result = KeBugCheckEx(92, (uint32_t)(0x9002ULL), (uint32_t)((uint32_t)(local_rsi)), v_rip - 11776922);
loc_00B6163B:
loc_00B61649:
    if (0 >= 92) goto loc_00B6174E;
    local_rbx = (0 + 0 * 2) << (5);
    local_rbx = (local_rbx) + (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x58));
    local_rsi = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbx + 0x4)) + (uint32_t)(*(uint32_t *)(local_rbx + 0x4)) * 2) << (3));
    if ((uint32_t)(local_rsi) == 0) goto loc_00B6169C;
    result = HalpMmAllocateMemory((uint32_t)((uint32_t)(local_rsi)), (uint32_t)(0x9002ULL), (uint32_t)((uint32_t)(local_rsi)), v_stack_m50);
    v_stack_m48 = result;
    if (result == 0) goto loc_00B6172E;
    a2 = 0;
    result = memset(result, a2, (uint32_t)((uint32_t)(local_rsi)), v_stack_m50);
    goto loc_00B616A1;
loc_00B6169C:
loc_00B616A1:
    if ((*(uint32_t *)(local_rbx + 0x4)) <= 0) goto loc_00B616CE;
loc_00B616A9:
    a3 = (uint32_t)((0) + 1);
    a2 = (0 + 0 * 2) + (0 + 0 * 2);
    *(uint64_t *)(*(uint64_t *)(local_rbx + 0x10) + a2 * 8 + 0x10) = v_stack_m48 + 0 + 0 * 2 * 8;
    *(uint32_t *)(*(uint64_t *)(local_rbx + 0x10) + a2 * 8 + 0x1C) = 0;
    if (((uint32_t)(a3)) < (*(uint32_t *)(local_rbx + 0x4))) goto loc_00B616A9;
loc_00B616CE:
    if ((*(uint32_t *)(local_rbx + 0x34)) <= 0) goto loc_00B616F7;
loc_00B616D9:
    a2 = (uint32_t)((0) + 1);
    Arg1 = (0 + 0 * 2) + (0 + 0 * 2);
    *(uint64_t *)(*(uint64_t *)(local_rbx + 0x40) + Arg1 * 8 + 0x10) = v_rip + 4383449;
    *(uint32_t *)(*(uint64_t *)(local_rbx + 0x40) + Arg1 * 8 + 0x1C) = 100;
    if (((uint32_t)(a2)) < (*(uint32_t *)(local_rbx + 0x34))) goto loc_00B616D9;
loc_00B616F7:
    if ((*(uint32_t *)(local_rbx + 0x4C)) <= 0) goto loc_00B61720;
loc_00B61702:
    a2 = (uint32_t)((0) + 1);
    Arg1 = (0 + 0 * 2) + (0 + 0 * 2);
    *(uint64_t *)(*(uint64_t *)(local_rbx + 0x58) + Arg1 * 8 + 0x10) = v_rip + 4383449;
    *(uint32_t *)(*(uint64_t *)(local_rbx + 0x58) + Arg1 * 8 + 0x1C) = 101;
    if (((uint32_t)(a2)) < (*(uint32_t *)(local_rbx + 0x4C))) goto loc_00B61702;
loc_00B61720:
    local_rbp = (uint32_t)((0) + 1);
    goto loc_00B61649;
loc_00B6172E:
    v_stack_m68 = 0xCB7ULL;
    result = KeBugCheckEx(92, (uint32_t)(0x9002ULL), *(uint64_t *)(local_rbx + 0x58), v_rip - 11777197);
loc_00B6174E:
    *(uint64_t *)(v_rip + 0x461474) = 0;
    *(uint64_t *)(v_rip + 0x4614E5) = v_rip + 4592875;
    *(uint64_t *)(v_rip + 0x4614CF) = v_rip + 4592875;
loc_00B61779:
    local_rbx = (0 + 0 * 4) << (6);
    if ((uint8_t)(*(uint8_t *)(local_rbx + v_rip - 0xB6176A * 1 + 0xE0556D)) == 0) goto loc_00B617B1;
    if ((*(uint32_t *)(local_rbx + v_rip - 0xB6176A * 1 + 0xE05550)) != 32) goto loc_00B617B1;
    local_r10 = *(uint8_t *)(local_rbx + v_rip - 0xB6176A * 1 + 0xE0556D);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x42E0FE)))) & (8)) != 0) {
        local_r10 = 0;
        *(uint8_t *)(local_rbx + v_rip - 0xB6176A * 1 + 0xE0556D) = 0;
    }
    if ((*(uint64_t *)(local_rbx + v_rip - 0xB6176A * 1 + 0xE05680)) != 0) goto loc_00B617D5;
    result = Amd64GetGenericPerfEvent((uint32_t)(*(uint32_t *)(local_rbx + v_rip - 0xB6176A * 1 + 0xE05550)), (uint32_t)(0x9002ULL), *(uint64_t *)(local_rbx + 0x58), 0);
    if (result != 0) {
        *(uint64_t *)(local_rbx + v_rip - 0xB6176A * 1 + 0xE05680) = result;
    }
    if ((uint8_t)(local_r10) != 0) goto loc_00B6180B;
    result = (v_rip - 11933546 + 14701912) + (local_rbx);
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0x461467))) != (v_rip + 4592875)) goto loc_00B618C8;
    *(uint64_t *)(result) = v_rip + 4592875;
    *(uint64_t *)(result + 0x8) = *(uint64_t *)(v_rip + 0x461467);
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x461467)) = result;
    *(uint64_t *)(v_rip + 0x46143D) = result;
loc_00B6180B:
    a4 = (uint32_t)((0) + 1);
    if (((uint32_t)(a4)) < 18) goto loc_00B61779;
loc_00B61823:
    result = (uint32_t)(*(uint32_t *)(v_rip + 0x42E077));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x42E077)))) & (8)) != 0) {
        Arg1 = 0xC0010015ULL;
        a2 = ((uint32_t)(0x9002ULL)) << (32);
        result = ((uint32_t)(*(uint32_t *)(v_rip + 0x42E077))) | (a2);
        a2 = result;
        a2 = (a2) >> (32);
    }
loc_00B61850:
    result = KeAddProcessorAffinityEx(v_rip + 2768160, (uint32_t)((uint32_t)((uint32_t)(v_stack_m54))), *(uint64_t *)(local_rbx + 0x58), a4);
    local_rbx = (v_rip + 2768160) + (320);
    local_rbp = (18) - (1);
    if (condition_is_not_equal) goto loc_00B61850;
    if (*(uint64_t *)(*(uint64_t *)(v_rip - 0xB6176A + (uint32_t)((uint32_t)((uint32_t)(v_stack_m54))) * 8 + 0xFC8C40) + 0x58) == 0) goto loc_00B6189C;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip - 0xB6176A + (uint32_t)((uint32_t)((uint32_t)(v_stack_m54))) * 8 + 0xFC8C40) + 0x58) + 0x4))) == 0) goto loc_00B6189C;
loc_00B61883:
    result = 0;
    a2 = 0;
    result = Amd64FreeCounter(0, a2, *(uint64_t *)(local_rbx + 0x58), a4);
    local_rdi = (uint32_t)((local_rdi) + 1);
    if (((uint32_t)(local_rdi)) < ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip - 0xB6176A + (uint32_t)((uint32_t)((uint32_t)(v_stack_m54))) * 8 + 0xFC8C40) + 0x58) + 0x4))))) goto loc_00B61883;
loc_00B6189C:
    Arg1 = (v_stack_m30) ^ (local_rsp);
    result = _security_check_cookie(Arg1, a2, *(uint64_t *)(local_rbx + 0x58), a4);
    return result;
loc_00B618C8:
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagelk&rva=0x00B61318&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
