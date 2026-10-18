# Amd64InitializeProfilingOriginal

- RVA: `0x00B618D8`–`0x00B61DBF` (길이 `1,255` bytes)
- VA: `0x0000000140B618D8`
- 실행 섹션: `PAGELK`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C5058`
- 디코드: `304`개 명령, `1,255/1,255` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **28**

### Outgoing calls
- `0x00B61AAD` → [HalpQueryMaximumRegisteredProcessorCount](../../text/54/HalpQueryMaximumRegisteredProcessorCount_function_00543BE8.md) (function, `0x00543BE8`)
- `0x00B61AFA` → [HalpMmAllocateMemory](../../text/54/HalpMmAllocateMemory_function_00544974.md) (function, `0x00544974`)
- `0x00B61B2A` → [HalpMmAllocateMemory](../../text/54/HalpMmAllocateMemory_function_00544974.md) (function, `0x00544974`)
- `0x00B61B49` → [HalpMmAllocateMemory](../../text/54/HalpMmAllocateMemory_function_00544974.md) (function, `0x00544974`)
- `0x00B61B8F` → [HalpMmAllocateMemory](../../text/54/HalpMmAllocateMemory_function_00544974.md) (function, `0x00544974`)
- `0x00B61CA7` → [Amd64GetGenericPerfEvent](../../text/56/Amd64GetGenericPerfEvent_function_0056C77C.md) (function, `0x0056C77C`)
- `0x00B61D45` → [KeAddProcessorAffinityEx](../../text/25/KeAddProcessorAffinityEx_function_0025B6F0.md) (function, `0x0025B6F0`)
- `0x00B61D7D` → [Amd64FreeCounter](../../text/56/Amd64FreeCounter_function_0056C524.md) (function, `0x0056C524`)
- `0x00B61D94` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [Amd64InitializeProfiling](Amd64InitializeProfiling_function_00B612F0.md) at `0x00B61304`

### Static image references
- `0x00B618F4` → RVA `0x00E0A740` (`.data`; read)
- `0x00B6190C` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x00B61928` → RVA `0x00F8F940` (`.data`; read)
- `0x00B61953` → RVA `0x00F8F8A0` (`.data`; read/write)
- `0x00B61983` → RVA `0x00042F20` (`.rdata`; read)
- `0x00B6198E` → RVA `0x00042F10` (`.rdata`; read)
- `0x00B61996` → RVA `0x00F8F8C0` (`.data`; write)
- `0x00B6199E` → RVA `0x00F8F940` (`.data`; write)
- `0x00B619B2` → RVA `0x00042F40` (`.rdata`; read)
- `0x00B619D6` → RVA `0x00042F30` (`.rdata`; read)
- `0x00B619E4` → RVA `0x00F8F890` (`.data`; read)
- `0x00B619EB` → RVA `0x00F8F898` (`.data`; write)
- `0x00B619F2` → RVA `0x00F8F890` (`.data`; write)
- `0x00B61A47` → RVA `0x00F8F900` (`.data`; read)
- `0x00B61A4E` → RVA `0x00F8F908` (`.data`; write)
- `0x00B61A55` → RVA `0x00F8F900` (`.data`; write)
- `0x00B61A9F` → RVA `0x000260D8` (`.rdata`; read)
- `0x00B61AA6` → RVA `0x00FC2BC8` (`.data`; write)
- `0x00B61B6B` → RVA `0x00F8F920` (`.data`; read)
- `0x00B61C3E` → RVA `0x00FC2C40` (`.data`; read)
- `0x00B61C45` → RVA `0x00FC2BD0` (`.data`; write)
- `0x00B61C4C` → RVA `0x00FC2C48` (`.data`; write)
- `0x00B61C56` → RVA `0x00FC2C40` (`.data`; write)
- `0x00B61C80` → RVA `0x00F8F8A0` (`.data`; read)
- `0x00B61CC9` → RVA `0x00E05558` (`.data`; read)
- `0x00B61CD3` → RVA `0x00FC2C48` (`.data`; read)
- `0x00B61CE3` → RVA `0x00FC2C20` (`.data`; read/write)
- `0x00B61D38` → RVA `0x00E05570` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **9**
  - `0x00B61AAD` → [HalpQueryMaximumRegisteredProcessorCount](../../text/54/HalpQueryMaximumRegisteredProcessorCount_function_00543BE8.md) (`PAGELK` → `.text`)
  - `0x00B61AFA` → [HalpMmAllocateMemory](../../text/54/HalpMmAllocateMemory_function_00544974.md) (`PAGELK` → `.text`)
  - `0x00B61B2A` → [HalpMmAllocateMemory](../../text/54/HalpMmAllocateMemory_function_00544974.md) (`PAGELK` → `.text`)
  - `0x00B61B49` → [HalpMmAllocateMemory](../../text/54/HalpMmAllocateMemory_function_00544974.md) (`PAGELK` → `.text`)
  - `0x00B61B8F` → [HalpMmAllocateMemory](../../text/54/HalpMmAllocateMemory_function_00544974.md) (`PAGELK` → `.text`)
  - `0x00B61CA7` → [Amd64GetGenericPerfEvent](../../text/56/Amd64GetGenericPerfEvent_function_0056C77C.md) (`PAGELK` → `.text`)
  - `0x00B61D45` → [KeAddProcessorAffinityEx](../../text/25/KeAddProcessorAffinityEx_function_0025B6F0.md) (`PAGELK` → `.text`)
  - `0x00B61D7D` → [Amd64FreeCounter](../../text/56/Amd64FreeCounter_function_0056C524.md) (`PAGELK` → `.text`)
  - `0x00B61D94` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGELK` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B618D8  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00B618DD  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
00B618E2  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
00B618E7  57                              push rdi
00B618E8  41 54                           push r12
00B618EA  41 55                           push r13
00B618EC  41 56                           push r14
00B618EE  41 57                           push r15
00B618F0  48 83 EC 60                     sub rsp, 0x60
00B618F4  48 8B 05 45 8E 2A 00            mov rax, qword ptr [rip + 0x2a8e45]
00B618FB  48 33 C4                        xor rax, rsp
00B618FE  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00B61903  65 44 8B 34 25 A4 01 00 00      mov r14d, dword ptr gs:[0x1a4]
00B6190C  4C 8D 2D ED E6 49 FF            lea r13, [rip - 0xb61913]
00B61913  33 FF                           xor edi, edi
00B61915  44 89 74 24 2C                  mov dword ptr [rsp + 0x2c], r14d
00B6191A  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
00B6191F  44 8B FF                        mov r15d, edi
00B61922  89 7C 24 20                     mov dword ptr [rsp + 0x20], edi
00B61926  8B F7                           mov esi, edi
00B61928  48 8D 2D 11 E0 42 00            lea rbp, [rip + 0x42e011]
00B6192F  44 8D 57 04                     lea r10d, [rdi + 4]
00B61933  44 8D 67 12                     lea r12d, [rdi + 0x12]
00B61937  45 85 F6                        test r14d, r14d
00B6193A  0F 85 D2 03 00 00               jne 0x140b61d12
00B61940  33 C9                           xor ecx, ecx
00B61942  44 8D 4F 06                     lea r9d, [rdi + 6]
00B61946  B8 01 00 00 80                  mov eax, 0x80000001
00B6194B  0F A2                           cpuid
00B6194D  0F BA E1 17                     bt ecx, 0x17
00B61951  73 30                           jae 0x140b61983
00B61953  83 0D 46 DF 42 00 01            or dword ptr [rip + 0x42df46], 1
00B6195A  45 8B F1                        mov r14d, r9d
00B6195D  BA 00 02 01 C0                  mov edx, 0xc0010200
00B61962  8B DF                           mov ebx, edi
00B61964  45 8B C1                        mov r8d, r9d
00B61967  8D 42 01                        lea eax, [rdx + 1]
00B6196A  89 14 2B                        mov dword ptr [rbx + rbp], edx
00B6196D  42 89 84 2B C0 F8 F8 00         mov dword ptr [rbx + r13 + 0xf8f8c0], eax
00B61975  83 C2 02                        add edx, 2
00B61978  49 03 DA                        add rbx, r10
00B6197B  49 83 E8 01                     sub r8, 1
00B6197F  75 E6                           jne 0x140b61967
00B61981  EB 23                           jmp 0x140b619a6
00B61983  66 0F 6F 05 95 15 4E FF         movdqa xmm0, xmmword ptr [rip - 0xb1ea6b]
00B6198B  45 8B F2                        mov r14d, r10d
00B6198E  66 0F 6F 0D 7A 15 4E FF         movdqa xmm1, xmmword ptr [rip - 0xb1ea86]
00B61996  F3 0F 7F 05 22 DF 42 00         movdqu xmmword ptr [rip + 0x42df22], xmm0
00B6199E  F3 0F 7F 0D 9A DF 42 00         movdqu xmmword ptr [rip + 0x42df9a], xmm1
00B619A6  0F BA E1 18                     bt ecx, 0x18
00B619AA  73 4D                           jae 0x140b619f9
00B619AC  0F BA E1 16                     bt ecx, 0x16
00B619B0  73 47                           jae 0x140b619f9
00B619B2  66 0F 6F 05 86 15 4E FF         movdqa xmm0, xmmword ptr [rip - 0xb1ea7a]
00B619BA  41 8B F2                        mov esi, r10d
00B619BD  83 0D DC DE 42 00 02            or dword ptr [rip + 0x42dedc], 2
00B619C4  41 8B C6                        mov eax, r14d
00B619C7  44 89 54 24 20                  mov dword ptr [rsp + 0x20], r10d
00B619CC  F3 41 0F 7F 84 85 C0 F8 F8 00   movdqu xmmword ptr [r13 + rax*4 + 0xf8f8c0], xmm0
00B619D6  66 0F 6F 05 52 15 4E FF         movdqa xmm0, xmmword ptr [rip - 0xb1eaae]
00B619DE  F3 0F 7F 44 85 00               movdqu xmmword ptr [rbp + rax*4], xmm0
00B619E4  48 8D 05 A5 DE 42 00            lea rax, [rip + 0x42dea5]
00B619EB  48 89 05 A6 DE 42 00            mov qword ptr [rip + 0x42dea6], rax
00B619F2  48 89 05 97 DE 42 00            mov qword ptr [rip + 0x42de97], rax
00B619F9  0F BA E1 1C                     bt ecx, 0x1c
00B619FD  73 5D                           jae 0x140b61a5c
00B619FF  0F BA E1 16                     bt ecx, 0x16
00B61A03  73 57                           jae 0x140b61a5c
00B61A05  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
00B61A0E  42 8D 14 36                     lea edx, [rsi + r14]
00B61A12  44 09 15 87 DE 42 00            or dword ptr [rip + 0x42de87], r10d
00B61A19  45 8B FA                        mov r15d, r10d
00B61A1C  80 78 40 16                     cmp byte ptr [rax + 0x40], 0x16
00B61A20  74 03                           je 0x140b61a25
00B61A22  45 8B F9                        mov r15d, r9d
00B61A25  BB 30 02 01 C0                  mov ebx, 0xc0010230
00B61A2A  45 8B C7                        mov r8d, r15d
00B61A2D  8D 43 01                        lea eax, [rbx + 1]
00B61A30  89 5C 95 00                     mov dword ptr [rbp + rdx*4], ebx
00B61A34  41 89 84 95 C0 F8 F8 00         mov dword ptr [r13 + rdx*4 + 0xf8f8c0], eax
00B61A3C  83 C3 02                        add ebx, 2
00B61A3F  FF C2                           inc edx
00B61A41  49 83 E8 01                     sub r8, 1
00B61A45  75 E6                           jne 0x140b61a2d
00B61A47  48 8D 05 B2 DE 42 00            lea rax, [rip + 0x42deb2]
00B61A4E  48 89 05 B3 DE 42 00            mov qword ptr [rip + 0x42deb3], rax
00B61A55  48 89 05 A4 DE 42 00            mov qword ptr [rip + 0x42dea4], rax
00B61A5C  33 C9                           xor ecx, ecx
00B61A5E  B8 00 00 00 80                  mov eax, 0x80000000
00B61A63  0F A2                           cpuid
00B61A65  3D 08 00 00 80                  cmp eax, 0x80000008
00B61A6A  72 33                           jb 0x140b61a9f
00B61A6C  33 C9                           xor ecx, ecx
00B61A6E  B8 08 00 00 80                  mov eax, 0x80000008
00B61A73  0F A2                           cpuid
00B61A75  F6 C3 02                        test bl, 2
00B61A78  74 25                           je 0x140b61a9f
00B61A7A  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
00B61A83  80 78 40 17                     cmp byte ptr [rax + 0x40], 0x17
00B61A87  75 0F                           jne 0x140b61a98
00B61A89  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
00B61A92  80 78 43 1F                     cmp byte ptr [rax + 0x43], 0x1f
00B61A96  72 07                           jb 0x140b61a9f
00B61A98  83 0D 01 DE 42 00 08            or dword ptr [rip + 0x42de01], 8
00B61A9F  48 8D 05 32 46 4C FF            lea rax, [rip - 0xb3b9ce]
00B61AA6  48 89 05 1B 11 46 00            mov qword ptr [rip + 0x46111b], rax
00B61AAD  E8 36 21 9E FF                  call 0x140543be8
00B61AB2  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
00B61ABB  8B E8                           mov ebp, eax
00B61ABD  89 6C 24 28                     mov dword ptr [rsp + 0x28], ebp
00B61AC1  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
00B61AC6  85 C0                           test eax, eax
00B61AC8  0F 84 70 01 00 00               je 0x140b61c3e
00B61ACE  43 8D 04 76                     lea eax, [r14 + r14*2]
00B61AD2  48 8B DF                        mov rbx, rdi
00B61AD5  C1 E0 04                        shl eax, 4
00B61AD8  44 8D 2C 76                     lea r13d, [rsi + rsi*2]
00B61ADC  41 C1 E5 04                     shl r13d, 4
00B61AE0  47 8D 24 7F                     lea r12d, [r15 + r15*2]
00B61AE4  89 44 24 24                     mov dword ptr [rsp + 0x24], eax
00B61AE8  41 C1 E4 04                     shl r12d, 4
00B61AEC  48 8B 71 58                     mov rsi, qword ptr [rcx + 0x58]
00B61AF0  8B C8                           mov ecx, eax
00B61AF2  89 3C 33                        mov dword ptr [rbx + rsi], edi
00B61AF5  44 89 74 33 04                  mov dword ptr [rbx + rsi + 4], r14d
00B61AFA  E8 75 2E 9E FF                  call 0x140544974
00B61AFF  48 89 44 33 10                  mov qword ptr [rbx + rsi + 0x10], rax
00B61B04  8B 44 24 20                     mov eax, dword ptr [rsp + 0x20]
00B61B08  89 44 33 34                     mov dword ptr [rbx + rsi + 0x34], eax
00B61B0C  48 C7 44 33 18 01 00 00 00      mov qword ptr [rbx + rsi + 0x18], 1
00B61B15  48 89 7C 33 28                  mov qword ptr [rbx + rsi + 0x28], rdi
00B61B1A  C7 44 33 30 64 00 00 00         mov dword ptr [rbx + rsi + 0x30], 0x64
00B61B22  45 85 ED                        test r13d, r13d
00B61B25  74 0D                           je 0x140b61b34
00B61B27  41 8B CD                        mov ecx, r13d
00B61B2A  E8 45 2E 9E FF                  call 0x140544974
00B61B2F  48 89 44 33 40                  mov qword ptr [rbx + rsi + 0x40], rax
00B61B34  C7 44 33 48 65 00 00 00         mov dword ptr [rbx + rsi + 0x48], 0x65
00B61B3C  44 89 7C 33 4C                  mov dword ptr [rbx + rsi + 0x4c], r15d
00B61B41  45 85 E4                        test r12d, r12d
00B61B44  74 0D                           je 0x140b61b53
00B61B46  41 8B CC                        mov ecx, r12d
00B61B49  E8 26 2E 9E FF                  call 0x140544974
00B61B4E  48 89 44 33 58                  mov qword ptr [rbx + rsi + 0x58], rax
00B61B53  8B 44 24 24                     mov eax, dword ptr [rsp + 0x24]
00B61B57  48 83 C3 60                     add rbx, 0x60
00B61B5B  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
00B61B60  48 83 ED 01                     sub rbp, 1
00B61B64  75 86                           jne 0x140b61aec
00B61B66  44 8B 7C 24 28                  mov r15d, dword ptr [rsp + 0x28]
00B61B6B  4C 8D 25 AE DD 42 00            lea r12, [rip + 0x42ddae]
00B61B72  48 8B F7                        mov rsi, rdi
00B61B75  4C 8B E9                        mov r13, rcx
00B61B78  49 8B 6D 58                     mov rbp, qword ptr [r13 + 0x58]
00B61B7C  8B 44 2E 04                     mov eax, dword ptr [rsi + rbp + 4]
00B61B80  4C 8B 74 2E 10                  mov r14, qword ptr [rsi + rbp + 0x10]
00B61B85  8D 0C 40                        lea ecx, [rax + rax*2]
00B61B88  C1 E1 03                        shl ecx, 3
00B61B8B  85 C9                           test ecx, ecx
00B61B8D  74 0C                           je 0x140b61b9b
00B61B8F  E8 E0 2D 9E FF                  call 0x140544974
00B61B94  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00B61B99  EB 05                           jmp 0x140b61ba0
00B61B9B  48 8B 44 24 38                  mov rax, qword ptr [rsp + 0x38]
00B61BA0  44 8B C7                        mov r8d, edi
00B61BA3  39 7C 2E 04                     cmp dword ptr [rsi + rbp + 4], edi
00B61BA7  76 26                           jbe 0x140b61bcf
00B61BA9  41 8B C8                        mov ecx, r8d
00B61BAC  41 FF C0                        inc r8d
00B61BAF  48 8D 1C 49                     lea rbx, [rcx + rcx*2]
00B61BB3  48 03 DB                        add rbx, rbx
00B61BB6  48 8D 0C 49                     lea rcx, [rcx + rcx*2]
00B61BBA  48 8D 14 C8                     lea rdx, [rax + rcx*8]
00B61BBE  49 89 54 DE 10                  mov qword ptr [r14 + rbx*8 + 0x10], rdx
00B61BC3  41 89 7C DE 1C                  mov dword ptr [r14 + rbx*8 + 0x1c], edi
00B61BC8  44 3B 44 2E 04                  cmp r8d, dword ptr [rsi + rbp + 4]
00B61BCD  72 DA                           jb 0x140b61ba9
00B61BCF  8B D7                           mov edx, edi
00B61BD1  48 8B 5C 2E 40                  mov rbx, qword ptr [rsi + rbp + 0x40]
00B61BD6  39 7C 2E 34                     cmp dword ptr [rsi + rbp + 0x34], edi
00B61BDA  76 1E                           jbe 0x140b61bfa
00B61BDC  8B C2                           mov eax, edx
00B61BDE  FF C2                           inc edx
00B61BE0  48 8D 0C 40                     lea rcx, [rax + rax*2]
00B61BE4  48 03 C9                        add rcx, rcx
00B61BE7  4C 89 64 CB 10                  mov qword ptr [rbx + rcx*8 + 0x10], r12
00B61BEC  C7 44 CB 1C 64 00 00 00         mov dword ptr [rbx + rcx*8 + 0x1c], 0x64
00B61BF4  3B 54 2E 34                     cmp edx, dword ptr [rsi + rbp + 0x34]
00B61BF8  72 E2                           jb 0x140b61bdc
00B61BFA  8B D7                           mov edx, edi
00B61BFC  48 8B 5C 2E 58                  mov rbx, qword ptr [rsi + rbp + 0x58]
00B61C01  39 7C 2E 4C                     cmp dword ptr [rsi + rbp + 0x4c], edi
00B61C05  76 1E                           jbe 0x140b61c25
00B61C07  8B C2                           mov eax, edx
00B61C09  FF C2                           inc edx
00B61C0B  48 8D 0C 40                     lea rcx, [rax + rax*2]
00B61C0F  48 03 C9                        add rcx, rcx
00B61C12  4C 89 64 CB 10                  mov qword ptr [rbx + rcx*8 + 0x10], r12
00B61C17  C7 44 CB 1C 65 00 00 00         mov dword ptr [rbx + rcx*8 + 0x1c], 0x65
00B61C1F  3B 54 2E 4C                     cmp edx, dword ptr [rsi + rbp + 0x4c]
00B61C23  72 E2                           jb 0x140b61c07
00B61C25  48 83 C6 60                     add rsi, 0x60
00B61C29  49 83 EF 01                     sub r15, 1
00B61C2D  0F 85 45 FF FF FF               jne 0x140b61b78
00B61C33  45 8D 67 12                     lea r12d, [r15 + 0x12]
00B61C37  4C 8D 2D C2 E3 49 FF            lea r13, [rip - 0xb61c3e]
00B61C3E  4C 8D 1D FB 0F 46 00            lea r11, [rip + 0x460ffb]
00B61C45  48 89 3D 84 0F 46 00            mov qword ptr [rip + 0x460f84], rdi
00B61C4C  4C 89 1D F5 0F 46 00            mov qword ptr [rip + 0x460ff5], r11
00B61C53  44 8B CF                        mov r9d, edi
00B61C56  4C 89 1D E3 0F 46 00            mov qword ptr [rip + 0x460fe3], r11
00B61C5D  41 8B C1                        mov eax, r9d
00B61C60  48 8D 1C 80                     lea rbx, [rax + rax*4]
00B61C64  48 C1 E3 06                     shl rbx, 6
00B61C68  46 8A 94 2B 6D 55 E0 00         mov r10b, byte ptr [rbx + r13 + 0xe0556d]
00B61C70  45 84 D2                        test r10b, r10b
00B61C73  74 20                           je 0x140b61c95
00B61C75  42 83 BC 2B 50 55 E0 00 20      cmp dword ptr [rbx + r13 + 0xe05550], 0x20
00B61C7E  75 15                           jne 0x140b61c95
00B61C80  8B 05 1A DC 42 00               mov eax, dword ptr [rip + 0x42dc1a]
00B61C86  A8 08                           test al, 8
00B61C88  74 0B                           je 0x140b61c95
00B61C8A  44 8A D7                        mov r10b, dil
00B61C8D  42 88 BC 2B 6D 55 E0 00         mov byte ptr [rbx + r13 + 0xe0556d], dil
00B61C95  4A 39 BC 2B 80 56 E0 00         cmp qword ptr [rbx + r13 + 0xe05680], rdi
00B61C9D  75 1A                           jne 0x140b61cb9
00B61C9F  42 8B 8C 2B 50 55 E0 00         mov ecx, dword ptr [rbx + r13 + 0xe05550]
00B61CA7  E8 D0 AA A0 FF                  call 0x14056c77c
00B61CAC  48 85 C0                        test rax, rax
00B61CAF  74 08                           je 0x140b61cb9
00B61CB1  4A 89 84 2B 80 56 E0 00         mov qword ptr [rbx + r13 + 0xe05680], rax
00B61CB9  45 84 D2                        test r10b, r10b
00B61CBC  75 3C                           jne 0x140b61cfa
00B61CBE  41 8B C1                        mov eax, r9d
00B61CC1  48 8D 0C 80                     lea rcx, [rax + rax*4]
00B61CC5  48 C1 E1 06                     shl rcx, 6
00B61CC9  48 8D 05 88 38 2A 00            lea rax, [rip + 0x2a3888]
00B61CD0  48 03 C8                        add rcx, rax
00B61CD3  48 8B 05 6E 0F 46 00            mov rax, qword ptr [rip + 0x460f6e]
00B61CDA  4C 39 18                        cmp qword ptr [rax], r11
00B61CDD  0F 85 D5 00 00 00               jne 0x140b61db8
00B61CE3  FF 05 37 0F 46 00               inc dword ptr [rip + 0x460f37]
00B61CE9  4C 89 19                        mov qword ptr [rcx], r11
00B61CEC  48 89 41 08                     mov qword ptr [rcx + 8], rax
00B61CF0  48 89 08                        mov qword ptr [rax], rcx
00B61CF3  48 89 0D 4E 0F 46 00            mov qword ptr [rip + 0x460f4e], rcx
00B61CFA  41 FF C1                        inc r9d
00B61CFD  45 3B CC                        cmp r9d, r12d
00B61D00  0F 82 57 FF FF FF               jb 0x140b61c5d
00B61D06  44 8B 74 24 2C                  mov r14d, dword ptr [rsp + 0x2c]
00B61D0B  48 8D 2D 2E DC 42 00            lea rbp, [rip + 0x42dc2e]
00B61D12  8B 05 88 DB 42 00               mov eax, dword ptr [rip + 0x42db88]
00B61D18  A8 08                           test al, 8
00B61D1A  74 1C                           je 0x140b61d38
00B61D1C  B9 15 00 01 C0                  mov ecx, 0xc0010015
00B61D21  0F 32                           rdmsr
00B61D23  48 C1 E2 20                     shl rdx, 0x20
00B61D27  48 0B C2                        or rax, rdx
00B61D2A  48 0F BA E8 1E                  bts rax, 0x1e
00B61D2F  48 8B D0                        mov rdx, rax
00B61D32  48 C1 EA 20                     shr rdx, 0x20
00B61D36  0F 30                           wrmsr
00B61D38  48 8D 1D 31 38 2A 00            lea rbx, [rip + 0x2a3831]
00B61D3F  41 8B D6                        mov edx, r14d
00B61D42  48 8B CB                        mov rcx, rbx
00B61D45  E8 A6 99 6F FF                  call 0x14025b6f0
00B61D4A  48 81 C3 40 01 00 00            add rbx, 0x140
00B61D51  49 83 EC 01                     sub r12, 1
00B61D55  75 E8                           jne 0x140b61d3f
00B61D57  41 8B C6                        mov eax, r14d
00B61D5A  49 8B 84 C5 40 8C FC 00         mov rax, qword ptr [r13 + rax*8 + 0xfc8c40]
00B61D62  48 8B 58 58                     mov rbx, qword ptr [rax + 0x58]
00B61D66  48 85 DB                        test rbx, rbx
00B61D69  74 21                           je 0x140b61d8c
00B61D6B  8B 5B 04                        mov ebx, dword ptr [rbx + 4]
00B61D6E  85 DB                           test ebx, ebx
00B61D70  74 1A                           je 0x140b61d8c
00B61D72  8B 4D 00                        mov ecx, dword ptr [rbp]
00B61D75  33 C0                           xor eax, eax
00B61D77  33 D2                           xor edx, edx
00B61D79  0F 30                           wrmsr
00B61D7B  8B CF                           mov ecx, edi
00B61D7D  E8 A2 A7 A0 FF                  call 0x14056c524
00B61D82  FF C7                           inc edi
00B61D84  48 8D 6D 04                     lea rbp, [rbp + 4]
00B61D88  3B FB                           cmp edi, ebx
00B61D8A  72 E6                           jb 0x140b61d72
00B61D8C  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
00B61D91  48 33 CC                        xor rcx, rsp
00B61D94  E8 A7 A8 B4 FF                  call 0x1406ac640
00B61D99  4C 8D 5C 24 60                  lea r11, [rsp + 0x60]
00B61D9E  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
00B61DA2  49 8B 6B 38                     mov rbp, qword ptr [r11 + 0x38]
00B61DA6  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
00B61DAA  49 8B E3                        mov rsp, r11
00B61DAD  41 5F                           pop r15
00B61DAF  41 5E                           pop r14
00B61DB1  41 5D                           pop r13
00B61DB3  41 5C                           pop r12
00B61DB5  5F                              pop rdi
00B61DB6  C3                              ret
00B61DB7  CC                              int3
00B61DB8  B9 03 00 00 00                  mov ecx, 3
00B61DBD  CD 29                           int 0x29
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Amd64InitializeProfilingOriginal(int a1)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_m5C;
    unsigned int v_stack_m60;
    unsigned int v_stack_m64;
    unsigned int v_stack_m68;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (96);
    result = (*(unsigned __int64 *)(v_rip + 2788933)) ^ (v_rsp);
    v_stack_m38 = result;
    v_rdi = 0;
    v_stack_m5C = (unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))));
    v_stack_m50 = 0;
    v_stack_m68 = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420)))) != 0) goto loc_00B61D12;
    a1 = 0;
    if (condition_is_above_or_equal) goto loc_00B61983;
loc_00B61967:
    *(unsigned int *)(0 + v_rip + 4382737 * 1) = (unsigned int)((unsigned int)(0xC0010200ULL));
    *(unsigned int *)(0 + v_rip - 11933971 * 1 + 16316608) = (unsigned int)((unsigned int)(0xC0010200ULL) + 1);
    a2 = (unsigned int)(((unsigned int)(0xC0010200ULL)) + (2));
    v_rbx = (0) + (v_rdi + 4);
    a3 = ((unsigned int)((unsigned int)(v_rdi + 6))) - (1);
    if (condition_is_not_equal) goto loc_00B61967;
    goto loc_00B619A6;
loc_00B61983:
    *(unsigned __int64 *)(v_rip + 4382498) = v_xmm0;
    *(unsigned __int64 *)(v_rip + 4382618) = v_xmm1;
loc_00B619A6:
    if (condition_is_above_or_equal) goto loc_00B619F9;
    result = (unsigned int)(0xC0010200ULL) + 1;
    v_rsi = 0;
    if (!(condition_is_above_or_equal)) {
        v_rsi = (unsigned int)(v_rdi + 4);
        result = (unsigned int)((unsigned int)((unsigned int)(v_rdi + 4)));
        v_stack_m68 = (unsigned int)(v_rdi + 4);
        *(unsigned __int64 *)(v_rip - 11933971 + result * 4 + 16316608) = v_xmm0;
        *(unsigned __int64 *)(v_rip + 4382737 + result * 4) = v_xmm0;
        result = v_rip + 4382373;
        *(unsigned __int64 *)(v_rip + 4382374) = result;
        *(unsigned __int64 *)(v_rip + 4382359) = result;
    }
    if (condition_is_above_or_equal) goto loc_00B61A5C;
    if (condition_is_above_or_equal) goto loc_00B61A5C;
    v_r15 = (unsigned int)((unsigned int)(v_rdi + 4));
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 64)) != 22) {
        v_r15 = (unsigned int)(v_rdi + 6);
    }
loc_00B61A2D:
    *(unsigned int *)(v_rip + 4382737 + v_rsi + (unsigned int)((unsigned int)(v_rdi + 4)) * 1 * 4) = (unsigned int)((unsigned int)(0xC0010230ULL));
    *(unsigned int *)(v_rip - 11933971 + v_rsi + (unsigned int)((unsigned int)(v_rdi + 4)) * 1 * 4 + 16316608) = (unsigned int)((unsigned int)(0xC0010230ULL) + 1);
    v_rbx = (unsigned int)(((unsigned int)(0xC0010230ULL)) + (2));
    a2 = (unsigned int)((v_rsi + (unsigned int)((unsigned int)(v_rdi + 4)) * 1) + 1);
    a3 = ((unsigned int)((unsigned int)(v_r15))) - (1);
    if (condition_is_not_equal) goto loc_00B61A2D;
    *(unsigned __int64 *)(v_rip + 4382387) = v_rip + 4382386;
    *(unsigned __int64 *)(v_rip + 4382372) = v_rip + 4382386;
loc_00B61A5C:
    a1 = 0;
    if (((unsigned int)((unsigned int)(0x80000000ULL))) < 0x80000008ULL) goto loc_00B61A9F;
    a1 = 0;
    if ((((unsigned __int8)(v_rbx)) & (2)) == 0) goto loc_00B61A9F;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 64)) != 23) goto loc_00B61A98;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 67)) >= 31) {
    }
    *(unsigned __int64 *)(v_rip + 4591899) = v_rip - 11778510;
    result = HalpQueryMaximumRegisteredProcessorCount(a1, a2, a3, v_rdi + 6);
    v_stack_m60 = (unsigned int)((unsigned int)((unsigned int)(result)));
    v_stack_m58 = *(unsigned __int64 *)(gs_base + (0 + 32));
    if ((unsigned int)(result) == 0) goto loc_00B61C3E;
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rdi + 4)) + (unsigned int)((unsigned int)(v_rdi + 4)) * 2) << (4));
    v_r13 = (unsigned int)((v_rsi + v_rsi * 2) << (4));
    v_stack_m64 = (unsigned int)(result);
    v_r12 = (unsigned int)((v_r15 + v_r15 * 2) << (4));
loc_00B61AEC:
    *(unsigned int *)(0 + *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 88) * 1) = 0;
    *(unsigned int *)(0 + *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 88) * 1 + 4) = (unsigned int)((unsigned int)((unsigned int)(v_rdi + 4)));
    result = HalpMmAllocateMemory((unsigned int)((unsigned int)(result)), a2, a3, v_rdi + 6);
    *(unsigned __int64 *)(0 + *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 88) * 1 + 16) = result;
    *(unsigned int *)(0 + *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 88) * 1 + 52) = (unsigned int)((unsigned int)(v_stack_m68));
    *(unsigned __int64 *)(0 + *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 88) * 1 + 24) = 1;
    *(unsigned __int64 *)(0 + *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 88) * 1 + 40) = 0;
    *(unsigned int *)(0 + *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 88) * 1 + 48) = 100;
    result = (unsigned int)(v_stack_m68);
    if ((unsigned int)(v_r13) != 0) {
        a1 = (unsigned int)(v_r13);
        result = HalpMmAllocateMemory(a1, a2, a3, v_rdi + 6);
        *(unsigned __int64 *)(0 + *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 88) * 1 + 64) = result;
    }
    *(unsigned int *)(0 + *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 88) * 1 + 72) = 101;
    *(unsigned int *)(0 + *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 88) * 1 + 76) = (unsigned int)(v_r15);
    if ((unsigned int)(v_r12) != 0) {
        a1 = (unsigned int)(v_r12);
        result = HalpMmAllocateMemory(a1, a2, a3, v_rdi + 6);
        *(unsigned __int64 *)(0 + *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 88) * 1 + 88) = result;
    }
    v_rbx = (0) + (96);
    v_rbp = ((unsigned int)((unsigned int)(result))) - (1);
    if (condition_is_not_equal) goto loc_00B61AEC;
loc_00B61B78:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(0 + *(unsigned __int64 *)(v_stack_m58 + 88) * 1 + 4)) + (unsigned int)(*(unsigned int *)(0 + *(unsigned __int64 *)(v_stack_m58 + 88) * 1 + 4)) * 2) << (3));
    if (a1 == 0) goto loc_00B61B9B;
    result = HalpMmAllocateMemory(a1, a2, a3, v_rdi + 6);
    v_stack_m50 = result;
    goto loc_00B61BA0;
loc_00B61B9B:
loc_00B61BA0:
    if ((*(unsigned int *)(0 + *(unsigned __int64 *)(v_stack_m58 + 88) * 1 + 4)) <= 0) goto loc_00B61BCF;
loc_00B61BA9:
    a3 = (unsigned int)((0) + 1);
    v_rbx = (0 + 0 * 2) + (0 + 0 * 2);
    *(unsigned __int64 *)(*(unsigned __int64 *)(0 + *(unsigned __int64 *)(v_stack_m58 + 88) * 1 + 16) + v_rbx * 8 + 16) = v_stack_m50 + 0 + 0 * 2 * 8;
    *(unsigned int *)(*(unsigned __int64 *)(0 + *(unsigned __int64 *)(v_stack_m58 + 88) * 1 + 16) + v_rbx * 8 + 28) = 0;
    if (((unsigned int)(a3)) < (*(unsigned int *)(0 + *(unsigned __int64 *)(v_stack_m58 + 88) * 1 + 4))) goto loc_00B61BA9;
loc_00B61BCF:
    if ((*(unsigned int *)(0 + *(unsigned __int64 *)(v_stack_m58 + 88) * 1 + 52)) <= 0) goto loc_00B61BFA;
loc_00B61BDC:
    a2 = (unsigned int)((0) + 1);
    a1 = (0 + 0 * 2) + (0 + 0 * 2);
    *(unsigned __int64 *)(*(unsigned __int64 *)(0 + *(unsigned __int64 *)(v_stack_m58 + 88) * 1 + 64) + a1 * 8 + 16) = v_rip + 4382126;
    *(unsigned int *)(*(unsigned __int64 *)(0 + *(unsigned __int64 *)(v_stack_m58 + 88) * 1 + 64) + a1 * 8 + 28) = 100;
    if (((unsigned int)(a2)) < (*(unsigned int *)(0 + *(unsigned __int64 *)(v_stack_m58 + 88) * 1 + 52))) goto loc_00B61BDC;
loc_00B61BFA:
    if ((*(unsigned int *)(0 + *(unsigned __int64 *)(v_stack_m58 + 88) * 1 + 76)) <= 0) goto loc_00B61C25;
loc_00B61C07:
    a2 = (unsigned int)((0) + 1);
    a1 = (0 + 0 * 2) + (0 + 0 * 2);
    *(unsigned __int64 *)(*(unsigned __int64 *)(0 + *(unsigned __int64 *)(v_stack_m58 + 88) * 1 + 88) + a1 * 8 + 16) = v_rip + 4382126;
    *(unsigned int *)(*(unsigned __int64 *)(0 + *(unsigned __int64 *)(v_stack_m58 + 88) * 1 + 88) + a1 * 8 + 28) = 101;
    if (((unsigned int)(a2)) < (*(unsigned int *)(0 + *(unsigned __int64 *)(v_stack_m58 + 88) * 1 + 76))) goto loc_00B61C07;
loc_00B61C25:
    v_rsi = (0) + (96);
    v_r15 = ((unsigned int)(v_stack_m60)) - (1);
    if (condition_is_not_equal) goto loc_00B61B78;
loc_00B61C3E:
    *(unsigned __int64 *)(v_rip + 4591492) = 0;
    *(unsigned __int64 *)(v_rip + 4591605) = v_rip + 4591611;
    *(unsigned __int64 *)(v_rip + 4591587) = v_rip + 4591611;
loc_00B61C5D:
    v_rbx = (0 + 0 * 4) << (6);
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rbx + v_rip - 11934782 * 1 + 14701933)) == 0) goto loc_00B61C95;
    if ((*(unsigned int *)(v_rbx + v_rip - 11934782 * 1 + 14701904)) != 32) goto loc_00B61C95;
    v_r10 = *(unsigned __int8 *)(v_rbx + v_rip - 11934782 * 1 + 14701933);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 4381722)))) & (8)) != 0) {
        v_r10 = 0;
        *(unsigned __int8 *)(v_rbx + v_rip - 11934782 * 1 + 14701933) = 0;
    }
    if ((*(unsigned __int64 *)(v_rbx + v_rip - 11934782 * 1 + 14702208)) != 0) goto loc_00B61CB9;
    result = Amd64GetGenericPerfEvent((unsigned int)(*(unsigned int *)(v_rbx + v_rip - 11934782 * 1 + 14701904)), a2, a3, 0);
    if (result != 0) {
        *(unsigned __int64 *)(v_rbx + v_rip - 11934782 * 1 + 14702208) = result;
    }
    if ((unsigned __int8)(v_r10) != 0) goto loc_00B61CFA;
    a1 = (0 + 0 * 4) << (6);
    a1 = (a1) + (v_rip + 2766984);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4591470))) != (v_rip + 4591611)) goto loc_00B61DB8;
    *(unsigned __int64 *)(a1) = v_rip + 4591611;
    *(unsigned __int64 *)(a1 + 8) = *(unsigned __int64 *)(v_rip + 4591470);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4591470)) = a1;
    *(unsigned __int64 *)(v_rip + 4591438) = a1;
loc_00B61CFA:
    a4 = (unsigned int)((0) + 1);
    if (((unsigned int)(a4)) < ((unsigned int)(v_r15 + 18))) goto loc_00B61C5D;
loc_00B61D12:
    result = (unsigned int)(*(unsigned int *)(v_rip + 4381576));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 4381576)))) & (8)) != 0) {
        a1 = 0xC0010015ULL;
        a2 = (a2) << (32);
        result = ((unsigned int)(*(unsigned int *)(v_rip + 4381576))) | (a2);
        a2 = result;
        a2 = (a2) >> (32);
    }
loc_00B61D3F:
    result = KeAddProcessorAffinityEx(v_rip + 2766897, (unsigned int)((unsigned int)((unsigned int)(v_stack_m5C))), a3, a4);
    v_rbx = (v_rip + 2766897) + (320);
    v_r12 = (v_r15 + 18) - (1);
    if (condition_is_not_equal) goto loc_00B61D3F;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 11934782 + (unsigned int)((unsigned int)((unsigned int)(v_stack_m5C))) * 8 + 16550976) + 88) == 0) goto loc_00B61D8C;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 11934782 + (unsigned int)((unsigned int)((unsigned int)(v_stack_m5C))) * 8 + 16550976) + 88) + 4))) == 0) goto loc_00B61D8C;
loc_00B61D72:
    result = 0;
    a2 = 0;
    result = Amd64FreeCounter(0, a2, a3, a4);
    v_rdi = (unsigned int)((v_rdi) + 1);
    if (((unsigned int)(v_rdi)) < ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 11934782 + (unsigned int)((unsigned int)((unsigned int)(v_stack_m5C))) * 8 + 16550976) + 88) + 4))))) goto loc_00B61D72;
loc_00B61D8C:
    a1 = (v_stack_m38) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    return result;
loc_00B61DB8:
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t Amd64InitializeProfilingOriginal(int32_t Arg1)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint32_t v_stack_m5C;
    uint32_t v_stack_m60;
    uint32_t v_stack_m64;
    uint32_t v_stack_m68;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (96);
    result = (*(uint64_t *)(v_rip + 0x2A8E45)) ^ (local_rsp);
    v_stack_m38 = result;
    local_rdi = 0;
    v_stack_m5C = (uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))));
    v_stack_m50 = 0;
    v_stack_m68 = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4)))) != 0) goto loc_00B61D12;
    Arg1 = 0;
    if (condition_is_above_or_equal) goto loc_00B61983;
loc_00B61967:
    *(uint32_t *)(0 + v_rip + 0x42E011 * 1) = (uint32_t)((uint32_t)(0xC0010200ULL));
    *(uint32_t *)(0 + v_rip - 0xB61913 * 1 + 0xF8F8C0) = (uint32_t)((uint32_t)(0xC0010200ULL) + 1);
    a2 = (uint32_t)(((uint32_t)(0xC0010200ULL)) + (2));
    local_rbx = (0) + (local_rdi + 4);
    a3 = ((uint32_t)((uint32_t)(local_rdi + 6))) - (1);
    if (condition_is_not_equal) goto loc_00B61967;
    goto loc_00B619A6;
loc_00B61983:
    *(uint64_t *)(v_rip + 0x42DF22) = v_xmm0;
    *(uint64_t *)(v_rip + 0x42DF9A) = v_xmm1;
loc_00B619A6:
    if (condition_is_above_or_equal) goto loc_00B619F9;
    result = (uint32_t)(0xC0010200ULL) + 1;
    local_rsi = 0;
    if (!(condition_is_above_or_equal)) {
        local_rsi = (uint32_t)(local_rdi + 4);
        result = (uint32_t)((uint32_t)((uint32_t)(local_rdi + 4)));
        v_stack_m68 = (uint32_t)(local_rdi + 4);
        *(uint64_t *)(v_rip - 0xB61913 + result * 4 + 0xF8F8C0) = v_xmm0;
        *(uint64_t *)(v_rip + 0x42E011 + result * 4) = v_xmm0;
        result = v_rip + 4382373;
        *(uint64_t *)(v_rip + 0x42DEA6) = result;
        *(uint64_t *)(v_rip + 0x42DE97) = result;
    }
    if (condition_is_above_or_equal) goto loc_00B61A5C;
    if (condition_is_above_or_equal) goto loc_00B61A5C;
    local_r15 = (uint32_t)((uint32_t)(local_rdi + 4));
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x40)) != 22) {
        local_r15 = (uint32_t)(local_rdi + 6);
    }
loc_00B61A2D:
    *(uint32_t *)(v_rip + 0x42E011 + local_rsi + (uint32_t)((uint32_t)(local_rdi + 0x4)) * 1 * 4) = (uint32_t)((uint32_t)(0xC0010230ULL));
    *(uint32_t *)(v_rip - 0xB61913 + local_rsi + (uint32_t)((uint32_t)(local_rdi + 0x4)) * 1 * 4 + 0xF8F8C0) = (uint32_t)((uint32_t)(0xC0010230ULL) + 1);
    local_rbx = (uint32_t)(((uint32_t)(0xC0010230ULL)) + (2));
    a2 = (uint32_t)((local_rsi + (uint32_t)((uint32_t)(local_rdi + 4)) * 1) + 1);
    a3 = ((uint32_t)((uint32_t)(local_r15))) - (1);
    if (condition_is_not_equal) goto loc_00B61A2D;
    *(uint64_t *)(v_rip + 0x42DEB3) = v_rip + 4382386;
    *(uint64_t *)(v_rip + 0x42DEA4) = v_rip + 4382386;
loc_00B61A5C:
    Arg1 = 0;
    if (((uint32_t)((uint32_t)(0x80000000ULL))) < 0x80000008ULL) goto loc_00B61A9F;
    Arg1 = 0;
    if ((((uint8_t)(local_rbx)) & (2)) == 0) goto loc_00B61A9F;
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x40)) != 23) goto loc_00B61A98;
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x43)) >= 31) {
    }
    *(uint64_t *)(v_rip + 0x46111B) = v_rip - 11778510;
    result = HalpQueryMaximumRegisteredProcessorCount(Arg1, a2, a3, local_rdi + 6);
    v_stack_m60 = (uint32_t)((uint32_t)((uint32_t)(result)));
    v_stack_m58 = *(uint64_t *)(gs_base + (0 + 0x20));
    if ((uint32_t)(result) == 0) goto loc_00B61C3E;
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rdi + 4)) + (uint32_t)((uint32_t)(local_rdi + 4)) * 2) << (4));
    local_r13 = (uint32_t)((local_rsi + local_rsi * 2) << (4));
    v_stack_m64 = (uint32_t)(result);
    local_r12 = (uint32_t)((local_r15 + local_r15 * 2) << (4));
loc_00B61AEC:
    *(uint32_t *)(0 + *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x58) * 1) = 0;
    *(uint32_t *)(0 + *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x58) * 1 + 0x4) = (uint32_t)((uint32_t)((uint32_t)(local_rdi + 4)));
    result = HalpMmAllocateMemory((uint32_t)((uint32_t)(result)), a2, a3, local_rdi + 6);
    *(uint64_t *)(0 + *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x58) * 1 + 0x10) = result;
    *(uint32_t *)(0 + *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x58) * 1 + 0x34) = (uint32_t)((uint32_t)(v_stack_m68));
    *(uint64_t *)(0 + *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x58) * 1 + 0x18) = 1;
    *(uint64_t *)(0 + *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x58) * 1 + 0x28) = 0;
    *(uint32_t *)(0 + *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x58) * 1 + 0x30) = 100;
    result = (uint32_t)(v_stack_m68);
    if ((uint32_t)(local_r13) != 0) {
        Arg1 = (uint32_t)(local_r13);
        result = HalpMmAllocateMemory(Arg1, a2, a3, local_rdi + 6);
        *(uint64_t *)(0 + *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x58) * 1 + 0x40) = result;
    }
    *(uint32_t *)(0 + *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x58) * 1 + 0x48) = 101;
    *(uint32_t *)(0 + *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x58) * 1 + 0x4C) = (uint32_t)(local_r15);
    if ((uint32_t)(local_r12) != 0) {
        Arg1 = (uint32_t)(local_r12);
        result = HalpMmAllocateMemory(Arg1, a2, a3, local_rdi + 6);
        *(uint64_t *)(0 + *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x58) * 1 + 0x58) = result;
    }
    local_rbx = (0) + (96);
    local_rbp = ((uint32_t)((uint32_t)(result))) - (1);
    if (condition_is_not_equal) goto loc_00B61AEC;
loc_00B61B78:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(0 + *(uint64_t *)(v_stack_m58 + 0x58) * 1 + 0x4)) + (uint32_t)(*(uint32_t *)(0 + *(uint64_t *)(v_stack_m58 + 0x58) * 1 + 0x4)) * 2) << (3));
    if (Arg1 == 0) goto loc_00B61B9B;
    result = HalpMmAllocateMemory(Arg1, a2, a3, local_rdi + 6);
    v_stack_m50 = result;
    goto loc_00B61BA0;
loc_00B61B9B:
loc_00B61BA0:
    if ((*(uint32_t *)(0 + *(uint64_t *)(v_stack_m58 + 0x58) * 1 + 0x4)) <= 0) goto loc_00B61BCF;
loc_00B61BA9:
    a3 = (uint32_t)((0) + 1);
    local_rbx = (0 + 0 * 2) + (0 + 0 * 2);
    *(uint64_t *)(*(uint64_t *)(0 + *(uint64_t *)(v_stack_m58 + 0x58) * 1 + 0x10) + local_rbx * 8 + 0x10) = v_stack_m50 + 0 + 0 * 2 * 8;
    *(uint32_t *)(*(uint64_t *)(0 + *(uint64_t *)(v_stack_m58 + 0x58) * 1 + 0x10) + local_rbx * 8 + 0x1C) = 0;
    if (((uint32_t)(a3)) < (*(uint32_t *)(0 + *(uint64_t *)(v_stack_m58 + 0x58) * 1 + 0x4))) goto loc_00B61BA9;
loc_00B61BCF:
    if ((*(uint32_t *)(0 + *(uint64_t *)(v_stack_m58 + 0x58) * 1 + 0x34)) <= 0) goto loc_00B61BFA;
loc_00B61BDC:
    a2 = (uint32_t)((0) + 1);
    Arg1 = (0 + 0 * 2) + (0 + 0 * 2);
    *(uint64_t *)(*(uint64_t *)(0 + *(uint64_t *)(v_stack_m58 + 0x58) * 1 + 0x40) + Arg1 * 8 + 0x10) = v_rip + 4382126;
    *(uint32_t *)(*(uint64_t *)(0 + *(uint64_t *)(v_stack_m58 + 0x58) * 1 + 0x40) + Arg1 * 8 + 0x1C) = 100;
    if (((uint32_t)(a2)) < (*(uint32_t *)(0 + *(uint64_t *)(v_stack_m58 + 0x58) * 1 + 0x34))) goto loc_00B61BDC;
loc_00B61BFA:
    if ((*(uint32_t *)(0 + *(uint64_t *)(v_stack_m58 + 0x58) * 1 + 0x4C)) <= 0) goto loc_00B61C25;
loc_00B61C07:
    a2 = (uint32_t)((0) + 1);
    Arg1 = (0 + 0 * 2) + (0 + 0 * 2);
    *(uint64_t *)(*(uint64_t *)(0 + *(uint64_t *)(v_stack_m58 + 0x58) * 1 + 0x58) + Arg1 * 8 + 0x10) = v_rip + 4382126;
    *(uint32_t *)(*(uint64_t *)(0 + *(uint64_t *)(v_stack_m58 + 0x58) * 1 + 0x58) + Arg1 * 8 + 0x1C) = 101;
    if (((uint32_t)(a2)) < (*(uint32_t *)(0 + *(uint64_t *)(v_stack_m58 + 0x58) * 1 + 0x4C))) goto loc_00B61C07;
loc_00B61C25:
    local_rsi = (0) + (96);
    local_r15 = ((uint32_t)(v_stack_m60)) - (1);
    if (condition_is_not_equal) goto loc_00B61B78;
loc_00B61C3E:
    *(uint64_t *)(v_rip + 0x460F84) = 0;
    *(uint64_t *)(v_rip + 0x460FF5) = v_rip + 4591611;
    *(uint64_t *)(v_rip + 0x460FE3) = v_rip + 4591611;
loc_00B61C5D:
    local_rbx = (0 + 0 * 4) << (6);
    if ((uint8_t)(*(uint8_t *)(local_rbx + v_rip - 0xB61C3E * 1 + 0xE0556D)) == 0) goto loc_00B61C95;
    if ((*(uint32_t *)(local_rbx + v_rip - 0xB61C3E * 1 + 0xE05550)) != 32) goto loc_00B61C95;
    local_r10 = *(uint8_t *)(local_rbx + v_rip - 0xB61C3E * 1 + 0xE0556D);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x42DC1A)))) & (8)) != 0) {
        local_r10 = 0;
        *(uint8_t *)(local_rbx + v_rip - 0xB61C3E * 1 + 0xE0556D) = 0;
    }
    if ((*(uint64_t *)(local_rbx + v_rip - 0xB61C3E * 1 + 0xE05680)) != 0) goto loc_00B61CB9;
    result = Amd64GetGenericPerfEvent((uint32_t)(*(uint32_t *)(local_rbx + v_rip - 0xB61C3E * 1 + 0xE05550)), a2, a3, 0);
    if (result != 0) {
        *(uint64_t *)(local_rbx + v_rip - 0xB61C3E * 1 + 0xE05680) = result;
    }
    if ((uint8_t)(local_r10) != 0) goto loc_00B61CFA;
    Arg1 = (0 + 0 * 4) << (6);
    Arg1 = (Arg1) + (v_rip + 2766984);
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0x460F6E))) != (v_rip + 4591611)) goto loc_00B61DB8;
    *(uint64_t *)(Arg1) = v_rip + 4591611;
    *(uint64_t *)(Arg1 + 0x8) = *(uint64_t *)(v_rip + 0x460F6E);
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x460F6E)) = Arg1;
    *(uint64_t *)(v_rip + 0x460F4E) = Arg1;
loc_00B61CFA:
    a4 = (uint32_t)((0) + 1);
    if (((uint32_t)(a4)) < ((uint32_t)(local_r15 + 18))) goto loc_00B61C5D;
loc_00B61D12:
    result = (uint32_t)(*(uint32_t *)(v_rip + 0x42DB88));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x42DB88)))) & (8)) != 0) {
        Arg1 = 0xC0010015ULL;
        a2 = (a2) << (32);
        result = ((uint32_t)(*(uint32_t *)(v_rip + 0x42DB88))) | (a2);
        a2 = result;
        a2 = (a2) >> (32);
    }
loc_00B61D3F:
    result = KeAddProcessorAffinityEx(v_rip + 2766897, (uint32_t)((uint32_t)((uint32_t)(v_stack_m5C))), a3, a4);
    local_rbx = (v_rip + 2766897) + (320);
    local_r12 = (local_r15 + 18) - (1);
    if (condition_is_not_equal) goto loc_00B61D3F;
    if (*(uint64_t *)(*(uint64_t *)(v_rip - 0xB61C3E + (uint32_t)((uint32_t)((uint32_t)(v_stack_m5C))) * 8 + 0xFC8C40) + 0x58) == 0) goto loc_00B61D8C;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip - 0xB61C3E + (uint32_t)((uint32_t)((uint32_t)(v_stack_m5C))) * 8 + 0xFC8C40) + 0x58) + 0x4))) == 0) goto loc_00B61D8C;
loc_00B61D72:
    result = 0;
    a2 = 0;
    result = Amd64FreeCounter(0, a2, a3, a4);
    local_rdi = (uint32_t)((local_rdi) + 1);
    if (((uint32_t)(local_rdi)) < ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip - 0xB61C3E + (uint32_t)((uint32_t)((uint32_t)(v_stack_m5C))) * 8 + 0xFC8C40) + 0x58) + 0x4))))) goto loc_00B61D72;
loc_00B61D8C:
    Arg1 = (v_stack_m38) ^ (local_rsp);
    result = _security_check_cookie(Arg1, a2, a3, a4);
    return result;
loc_00B61DB8:
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagelk&rva=0x00B618D8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
