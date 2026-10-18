# CmpGetNameControlBlock

- RVA: `0x0084A750`–`0x0084AC1B` (길이 `1,227` bytes)
- VA: `0x000000014084A750`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00069554`
- 디코드: `330`개 명령, `1,227/1,227` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **13**; 고유 호출 대상: **7**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0084A817` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0084A830` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x0084A894` → [CmpAllocatePool](../../text/3C/CmpAllocatePool_function_003CD504.md) (function, `0x003CD504`)
- `0x0084A981` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0084AAC8` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0084AAD4` → [CmpHashUnicodeComponent](CmpHashUnicodeComponent_function_0084AC24.md) (function, `0x0084AC24`)
- `0x0084AAE3` → [RtlUpcaseUnicodeChar](../85/RtlUpcaseUnicodeChar_function_0085F0F0.md) (function, `0x0085F0F0`)
- `0x0084AAF7` → [RtlUpcaseUnicodeChar](../85/RtlUpcaseUnicodeChar_function_0085F0F0.md) (function, `0x0085F0F0`)
- `0x0084AB04` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (function, `0x002638D0`)
- `0x0084AB11` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (function, `0x002638D0`)
- `0x0084AB18` → [RtlUpcaseUnicodeChar](../85/RtlUpcaseUnicodeChar_function_0085F0F0.md) (function, `0x0085F0F0`)
- `0x0084AB8E` → [RtlUpcaseUnicodeChar](../85/RtlUpcaseUnicodeChar_function_0085F0F0.md) (function, `0x0085F0F0`)
- `0x0084AC04` → [RtlUpcaseUnicodeChar](../85/RtlUpcaseUnicodeChar_function_0085F0F0.md) (function, `0x0085F0F0`)

### Direct callers
- [CmRenameKey](../7E/CmRenameKey_function_007E8F48.md) at `0x007E9C06`
- [CmpCreateKeyControlBlock](../85/CmpCreateKeyControlBlock_function_00851DB0.md) at `0x00852051`

### Static image references
- `0x0084A80D` → RVA `0x00EF5978` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **7**
  - `0x0084A817` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x0084A830` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x0084A894` → [CmpAllocatePool](../../text/3C/CmpAllocatePool_function_003CD504.md) (`PAGE` → `.text`)
  - `0x0084A981` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0084AAC8` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0084AB04` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (`PAGE` → `.text`)
  - `0x0084AB11` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0084A750  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
0084A755  53                              push rbx
0084A756  55                              push rbp
0084A757  56                              push rsi
0084A758  57                              push rdi
0084A759  41 54                           push r12
0084A75B  41 55                           push r13
0084A75D  41 56                           push r14
0084A75F  41 57                           push r15
0084A761  48 83 EC 28                     sub rsp, 0x28
0084A765  4C 8B F1                        mov r14, rcx
0084A768  48 85 D2                        test rdx, rdx
0084A76B  0F 84 63 03 00 00               je 0x14084aad4
0084A771  8B 1A                           mov ebx, dword ptr [rdx]
0084A773  45 0F B7 06                     movzx r8d, word ptr [r14]
0084A777  33 C0                           xor eax, eax
0084A779  41 0F B7 F0                     movzx esi, r8w
0084A77D  40 B5 01                        mov bpl, 1
0084A780  66 D1 EE                        shr si, 1
0084A783  8B F8                           mov edi, eax
0084A785  41 F7 C0 FE FF FF FF            test r8d, 0xfffffffe
0084A78C  76 55                           jbe 0x14084a7e3
0084A78E  41 BF FF 00 00 00               mov r15d, 0xff
0084A794  0F 1F 40 00                     nop dword ptr [rax]
0084A798  0F 1F 84 00 00 00 00 00         nop dword ptr [rax + rax]
0084A7A0  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
0084A7A4  8B CF                           mov ecx, edi
0084A7A6  0F B7 14 48                     movzx edx, word ptr [rax + rcx*2]
0084A7AA  66 83 FA 61                     cmp dx, 0x61
0084A7AE  73 06                           jae 0x14084a7b6
0084A7B0  41 0F B7 C0                     movzx eax, r8w
0084A7B4  EB 1E                           jmp 0x14084a7d4
0084A7B6  66 83 FA 7A                     cmp dx, 0x7a
0084A7BA  0F 87 20 03 00 00               ja 0x14084aae0
0084A7C0  41 0F B7 C0                     movzx eax, r8w
0084A7C4  66 83 EA 20                     sub dx, 0x20
0084A7C8  66 41 3B D7                     cmp dx, r15w
0084A7CC  76 06                           jbe 0x14084a7d4
0084A7CE  0F B7 F0                        movzx esi, ax
0084A7D1  40 32 ED                        xor bpl, bpl
0084A7D4  44 0F B7 C0                     movzx r8d, ax
0084A7D8  FF C7                           inc edi
0084A7DA  0F B7 C0                        movzx eax, ax
0084A7DD  D1 E8                           shr eax, 1
0084A7DF  3B F8                           cmp edi, eax
0084A7E1  72 BD                           jb 0x14084a7a0
0084A7E3  8B C3                           mov eax, ebx
0084A7E5  45 33 C0                        xor r8d, r8d
0084A7E8  C1 E8 09                        shr eax, 9
0084A7EB  33 D2                           xor edx, edx
0084A7ED  33 C3                           xor eax, ebx
0084A7EF  44 69 E8 A3 8A 01 00            imul r13d, eax, 0x18aa3
0084A7F6  41 8B C5                        mov eax, r13d
0084A7F9  41 8B FD                        mov edi, r13d
0084A7FC  48 C1 EF 09                     shr rdi, 9
0084A800  48 33 F8                        xor rdi, rax
0084A803  81 E7 FF 07 00 00               and edi, 0x7ff
0084A809  48 C1 E7 04                     shl rdi, 4
0084A80D  48 03 3D 64 B1 6A 00            add rdi, qword ptr [rip + 0x6ab164]
0084A814  48 8B CF                        mov rcx, rdi
0084A817  E8 14 5A 9C FF                  call 0x140210230
0084A81C  F0 48 0F BA 2F 00               lock bts qword ptr [rdi], 0
0084A822  4C 8B F8                        mov r15, rax
0084A825  73 0E                           jae 0x14084a835
0084A827  4C 8B C7                        mov r8, rdi
0084A82A  48 8B D0                        mov rdx, rax
0084A82D  48 8B CF                        mov rcx, rdi
0084A830  E8 5B 54 9C FF                  call 0x14020fc90
0084A835  4D 85 FF                        test r15, r15
0084A838  74 05                           je 0x14084a83f
0084A83A  41 C6 47 0A 01                  mov byte ptr [r15 + 0xa], 1
0084A83F  48 8B 05 32 B1 6A 00            mov rax, qword ptr [rip + 0x6ab132]
0084A846  45 8B E5                        mov r12d, r13d
0084A849  41 C1 EC 09                     shr r12d, 9
0084A84D  41 BB E0 FF 00 00               mov r11d, 0xffe0
0084A853  45 33 E5                        xor r12d, r13d
0084A856  41 81 E4 FF 07 00 00            and r12d, 0x7ff
0084A85D  41 8B CC                        mov ecx, r12d
0084A860  48 03 C9                        add rcx, rcx
0084A863  45 8D 53 1F                     lea r10d, [r11 + 0x1f]
0084A867  48 8B 7C C8 08                  mov rdi, qword ptr [rax + rcx*8 + 8]
0084A86C  48 85 FF                        test rdi, rdi
0084A86F  74 12                           je 0x14084a883
0084A871  4C 8D 6F F8                     lea r13, [rdi - 8]
0084A875  3B 1F                           cmp ebx, dword ptr [rdi]
0084A877  0F 84 2F 01 00 00               je 0x14084a9ac
0084A87D  48 8B 7F 08                     mov rdi, qword ptr [rdi + 8]
0084A881  EB E9                           jmp 0x14084a86c
0084A883  0F B7 FE                        movzx edi, si
0084A886  B9 00 01 00 00                  mov ecx, 0x100
0084A88B  41 B8 43 4D 4E 62               mov r8d, 0x624e4d43
0084A891  8D 57 1A                        lea edx, [rdi + 0x1a]
0084A894  E8 6B 2C B8 FF                  call 0x1403cd504
0084A899  4C 8B E8                        mov r13, rax
0084A89C  48 85 C0                        test rax, rax
0084A89F  0F 84 CD 01 00 00               je 0x14084aa72
0084A8A5  8B 00                           mov eax, dword ptr [rax]
0084A8A7  40 84 ED                        test bpl, bpl
0084A8AA  0F 84 99 02 00 00               je 0x14084ab49
0084A8B0  83 C8 01                        or eax, 1
0084A8B3  41 89 45 00                     mov dword ptr [r13], eax
0084A8B7  85 FF                           test edi, edi
0084A8B9  74 37                           je 0x14084a8f2
0084A8BB  33 C0                           xor eax, eax
0084A8BD  0F B7 EE                        movzx ebp, si
0084A8C0  44 8B F8                        mov r15d, eax
0084A8C3  49 8D 7D 1A                     lea rdi, [r13 + 0x1a]
0084A8C7  66 0F 1F 84 00 00 00 00 00      nop word ptr [rax + rax]
0084A8D0  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
0084A8D4  41 0F B7 04 07                  movzx eax, word ptr [r15 + rax]
0084A8D9  66 83 F8 61                     cmp ax, 0x61
0084A8DD  0F 83 B8 00 00 00               jae 0x14084a99b
0084A8E3  88 07                           mov byte ptr [rdi], al
0084A8E5  49 83 C7 02                     add r15, 2
0084A8E9  48 FF C7                        inc rdi
0084A8EC  48 83 ED 01                     sub rbp, 1
0084A8F0  75 DE                           jne 0x14084a8d0
0084A8F2  41 8B 45 00                     mov eax, dword ptr [r13]
0084A8F6  4D 8D 45 08                     lea r8, [r13 + 8]
0084A8FA  83 E0 01                        and eax, 1
0084A8FD  41 89 18                        mov dword ptr [r8], ebx
0084A900  83 C8 02                        or eax, 2
0084A903  66 41 89 75 18                  mov word ptr [r13 + 0x18], si
0084A908  41 89 45 00                     mov dword ptr [r13], eax
0084A90C  41 8B D4                        mov edx, r12d
0084A90F  48 C1 E2 04                     shl rdx, 4
0084A913  48 03 15 5E B0 6A 00            add rdx, qword ptr [rip + 0x6ab05e]
0084A91A  48 8B 42 08                     mov rax, qword ptr [rdx + 8]
0084A91E  49 89 40 08                     mov qword ptr [r8 + 8], rax
0084A922  4C 89 42 08                     mov qword ptr [rdx + 8], r8
0084A926  45 33 C0                        xor r8d, r8d
0084A929  8B C3                           mov eax, ebx
0084A92B  C1 E8 09                        shr eax, 9
0084A92E  33 C3                           xor eax, ebx
0084A930  69 C0 A3 8A 01 00               imul eax, eax, 0x18aa3
0084A936  8B D8                           mov ebx, eax
0084A938  48 C1 EB 09                     shr rbx, 9
0084A93C  8B C8                           mov ecx, eax
0084A93E  48 33 D9                        xor rbx, rcx
0084A941  81 E3 FF 07 00 00               and ebx, 0x7ff
0084A947  48 C1 E3 04                     shl rbx, 4
0084A94B  48 03 1D 26 B0 6A 00            add rbx, qword ptr [rip + 0x6ab026]
0084A952  0F 0D 0B                        prefetchw byte ptr [rbx]
0084A955  48 8B 03                        mov rax, qword ptr [rbx]
0084A958  48 8B C8                        mov rcx, rax
0084A95B  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
0084A95F  48 83 F9 10                     cmp rcx, 0x10
0084A963  48 8D 50 F0                     lea rdx, [rax - 0x10]
0084A967  49 0F 46 D0                     cmovbe rdx, r8
0084A96B  A8 02                           test al, 2
0084A96D  0F 85 8E 01 00 00               jne 0x14084ab01
0084A973  F0 48 0F B1 13                  lock cmpxchg qword ptr [rbx], rdx
0084A978  0F 85 83 01 00 00               jne 0x14084ab01
0084A97E  48 8B CB                        mov rcx, rbx
0084A981  E8 7A 6C A9 FF                  call 0x1402e1600
0084A986  49 8B C5                        mov rax, r13
0084A989  48 83 C4 28                     add rsp, 0x28
0084A98D  41 5F                           pop r15
0084A98F  41 5E                           pop r14
0084A991  41 5D                           pop r13
0084A993  41 5C                           pop r12
0084A995  5F                              pop rdi
0084A996  5E                              pop rsi
0084A997  5D                              pop rbp
0084A998  5B                              pop rbx
0084A999  C3                              ret
0084A99A  CC                              int3
0084A99B  66 83 F8 7A                     cmp ax, 0x7a
0084A99F  0F 87 4F 01 00 00               ja 0x14084aaf4
0084A9A5  2C 20                           sub al, 0x20
0084A9A7  E9 37 FF FF FF                  jmp 0x14084a8e3
0084A9AC  66 41 3B 75 18                  cmp si, word ptr [r13 + 0x18]
0084A9B1  0F 85 C6 FE FF FF               jne 0x14084a87d
0084A9B7  4D 8B 46 08                     mov r8, qword ptr [r14 + 8]
0084A9BB  4D 8D 4D 1A                     lea r9, [r13 + 0x1a]
0084A9BF  41 8B 45 00                     mov eax, dword ptr [r13]
0084A9C3  4C 89 8C 24 88 00 00 00         mov qword ptr [rsp + 0x88], r9
0084A9CB  4C 89 44 24 78                  mov qword ptr [rsp + 0x78], r8
0084A9D0  A8 01                           test al, 1
0084A9D2  0F 84 BD 01 00 00               je 0x14084ab95
0084A9D8  45 0F B7 3E                     movzx r15d, word ptr [r14]
0084A9DC  0F B7 D6                        movzx edx, si
0084A9DF  66 41 D1 EF                     shr r15w, 1
0084A9E3  66 89 94 24 80 00 00 00         mov word ptr [rsp + 0x80], dx
0084A9EB  66 45 85 FF                     test r15w, r15w
0084A9EF  74 52                           je 0x14084aa43
0084A9F1  66 85 D2                        test dx, dx
0084A9F4  74 4D                           je 0x14084aa43
0084A9F6  41 0F B6 01                     movzx eax, byte ptr [r9]
0084A9FA  49 FF C1                        inc r9
0084A9FD  41 0F B7 08                     movzx ecx, word ptr [r8]
0084AA01  49 83 C0 02                     add r8, 2
0084AA05  4C 89 44 24 78                  mov qword ptr [rsp + 0x78], r8
0084AA0A  66 89 44 24 70                  mov word ptr [rsp + 0x70], ax
0084AA0F  4C 89 8C 24 88 00 00 00         mov qword ptr [rsp + 0x88], r9
0084AA17  66 3B C8                        cmp cx, ax
0084AA1A  74 1D                           je 0x14084aa39
0084AA1C  66 83 F9 61                     cmp cx, 0x61
0084AA20  72 0E                           jb 0x14084aa30
0084AA22  66 83 F9 7A                     cmp cx, 0x7a
0084AA26  0F 87 EC 00 00 00               ja 0x14084ab18
0084AA2C  66 41 03 CB                     add cx, r11w
0084AA30  66 3B C8                        cmp cx, ax
0084AA33  0F 85 44 FE FF FF               jne 0x14084a87d
0084AA39  66 45 03 FA                     add r15w, r10w
0084AA3D  66 41 03 D2                     add dx, r10w
0084AA41  EB A0                           jmp 0x14084a9e3
0084AA43  66 44 3B FA                     cmp r15w, dx
0084AA47  0F 85 30 FE FF FF               jne 0x14084a87d
0084AA4D  41 8B 4D 00                     mov ecx, dword ptr [r13]
0084AA51  8B C1                           mov eax, ecx
0084AA53  83 E0 FE                        and eax, 0xfffffffe
0084AA56  83 F8 FE                        cmp eax, -2
0084AA59  0F 84 97 01 00 00               je 0x14084abf6
0084AA5F  8D 41 02                        lea eax, [rcx + 2]
0084AA62  33 C8                           xor ecx, eax
0084AA64  83 E1 01                        and ecx, 1
0084AA67  33 C8                           xor ecx, eax
0084AA69  41 89 4D 00                     mov dword ptr [r13], ecx
0084AA6D  E9 B4 FE FF FF                  jmp 0x14084a926
0084AA72  8B C3                           mov eax, ebx
0084AA74  C1 E8 09                        shr eax, 9
0084AA77  33 C3                           xor eax, ebx
0084AA79  69 C0 A3 8A 01 00               imul eax, eax, 0x18aa3
0084AA7F  8B D8                           mov ebx, eax
0084AA81  48 C1 EB 09                     shr rbx, 9
0084AA85  8B C8                           mov ecx, eax
0084AA87  48 33 D9                        xor rbx, rcx
0084AA8A  81 E3 FF 07 00 00               and ebx, 0x7ff
0084AA90  48 C1 E3 04                     shl rbx, 4
0084AA94  48 03 1D DD AE 6A 00            add rbx, qword ptr [rip + 0x6aaedd]
0084AA9B  0F 0D 0B                        prefetchw byte ptr [rbx]
0084AA9E  48 8B 03                        mov rax, qword ptr [rbx]
0084AAA1  41 B8 00 00 00 00               mov r8d, 0
0084AAA7  48 8B C8                        mov rcx, rax
0084AAAA  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
0084AAAE  48 83 F9 10                     cmp rcx, 0x10
0084AAB2  48 8D 50 F0                     lea rdx, [rax - 0x10]
0084AAB6  49 0F 46 D0                     cmovbe rdx, r8
0084AABA  A8 02                           test al, 2
0084AABC  75 50                           jne 0x14084ab0e
0084AABE  F0 48 0F B1 13                  lock cmpxchg qword ptr [rbx], rdx
0084AAC3  75 49                           jne 0x14084ab0e
0084AAC5  48 8B CB                        mov rcx, rbx
0084AAC8  E8 33 6B A9 FF                  call 0x1402e1600
0084AACD  33 C0                           xor eax, eax
0084AACF  E9 B5 FE FF FF                  jmp 0x14084a989
0084AAD4  E8 4B 01 00 00                  call 0x14084ac24
0084AAD9  8B D8                           mov ebx, eax
0084AADB  E9 93 FC FF FF                  jmp 0x14084a773
0084AAE0  0F B7 CA                        movzx ecx, dx
0084AAE3  E8 08 46 01 00                  call 0x14085f0f0
0084AAE8  0F B7 D0                        movzx edx, ax
0084AAEB  41 0F B7 06                     movzx eax, word ptr [r14]
0084AAEF  E9 D4 FC FF FF                  jmp 0x14084a7c8
0084AAF4  0F B7 C8                        movzx ecx, ax
0084AAF7  E8 F4 45 01 00                  call 0x14085f0f0
0084AAFC  E9 E2 FD FF FF                  jmp 0x14084a8e3
0084AB01  48 8B CB                        mov rcx, rbx
0084AB04  E8 C7 8D A1 FF                  call 0x1402638d0
0084AB09  E9 70 FE FF FF                  jmp 0x14084a97e
0084AB0E  48 8B CB                        mov rcx, rbx
0084AB11  E8 BA 8D A1 FF                  call 0x1402638d0
0084AB16  EB AD                           jmp 0x14084aac5
0084AB18  E8 D3 45 01 00                  call 0x14085f0f0
0084AB1D  0F B7 94 24 80 00 00 00         movzx edx, word ptr [rsp + 0x80]
0084AB25  41 BA FF FF 00 00               mov r10d, 0xffff
0084AB2B  4C 8B 44 24 78                  mov r8, qword ptr [rsp + 0x78]
0084AB30  0F B7 C8                        movzx ecx, ax
0084AB33  0F B7 44 24 70                  movzx eax, word ptr [rsp + 0x70]
0084AB38  4C 8B 8C 24 88 00 00 00         mov r9, qword ptr [rsp + 0x88]
0084AB40  45 8D 5A E1                     lea r11d, [r10 - 0x1f]
0084AB44  E9 E7 FE FF FF                  jmp 0x14084aa30
0084AB49  83 E0 FE                        and eax, 0xfffffffe
0084AB4C  D1 EF                           shr edi, 1
0084AB4E  41 89 45 00                     mov dword ptr [r13], eax
0084AB52  0F 84 9A FD FF FF               je 0x14084a8f2
0084AB58  33 C0                           xor eax, eax
0084AB5A  44 8B F8                        mov r15d, eax
0084AB5D  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
0084AB61  41 0F B7 04 07                  movzx eax, word ptr [r15 + rax]
0084AB66  66 83 F8 61                     cmp ax, 0x61
0084AB6A  72 0A                           jb 0x14084ab76
0084AB6C  66 83 F8 7A                     cmp ax, 0x7a
0084AB70  77 19                           ja 0x14084ab8b
0084AB72  66 83 E8 20                     sub ax, 0x20
0084AB76  66 43 89 44 2F 1A               mov word ptr [r15 + r13 + 0x1a], ax
0084AB7C  49 83 C7 02                     add r15, 2
0084AB80  48 83 EF 01                     sub rdi, 1
0084AB84  75 D7                           jne 0x14084ab5d
0084AB86  E9 67 FD FF FF                  jmp 0x14084a8f2
0084AB8B  0F B7 C8                        movzx ecx, ax
0084AB8E  E8 5D 45 01 00                  call 0x14085f0f0
0084AB93  EB E1                           jmp 0x14084ab76
0084AB95  33 D2                           xor edx, edx
0084AB97  44 8B FA                        mov r15d, edx
0084AB9A  66 0F 1F 44 00 00               nop word ptr [rax + rax]
0084ABA0  41 0F B7 45 18                  movzx eax, word ptr [r13 + 0x18]
0084ABA5  D1 E8                           shr eax, 1
0084ABA7  44 3B F8                        cmp r15d, eax
0084ABAA  0F 83 9D FE FF FF               jae 0x14084aa4d
0084ABB0  41 0F B7 00                     movzx eax, word ptr [r8]
0084ABB4  83 F8 61                        cmp eax, 0x61
0084ABB7  72 0A                           jb 0x14084abc3
0084ABB9  83 F8 7A                        cmp eax, 0x7a
0084ABBC  77 43                           ja 0x14084ac01
0084ABBE  8D 48 E0                        lea ecx, [rax - 0x20]
0084ABC1  EB 02                           jmp 0x14084abc5
0084ABC3  8B C8                           mov ecx, eax
0084ABC5  41 0F B7 01                     movzx eax, word ptr [r9]
0084ABC9  3B C8                           cmp ecx, eax
0084ABCB  75 1A                           jne 0x14084abe7
0084ABCD  49 83 C0 02                     add r8, 2
0084ABD1  49 83 C1 02                     add r9, 2
0084ABD5  4C 89 44 24 78                  mov qword ptr [rsp + 0x78], r8
0084ABDA  41 FF C7                        inc r15d
0084ABDD  4C 89 8C 24 88 00 00 00         mov qword ptr [rsp + 0x88], r9
0084ABE5  EB B9                           jmp 0x14084aba0
0084ABE7  41 BA FF FF 00 00               mov r10d, 0xffff
0084ABED  45 8D 5A E1                     lea r11d, [r10 - 0x1f]
0084ABF1  E9 87 FC FF FF                  jmp 0x14084a87d
0084ABF6  45 33 C0                        xor r8d, r8d
0084ABF9  45 8B E8                        mov r13d, r8d
0084ABFC  E9 28 FD FF FF                  jmp 0x14084a929
0084AC01  0F B7 C8                        movzx ecx, ax
0084AC04  E8 E7 44 01 00                  call 0x14085f0f0
0084AC09  4C 8B 44 24 78                  mov r8, qword ptr [rsp + 0x78]
0084AC0E  4C 8B 8C 24 88 00 00 00         mov r9, qword ptr [rsp + 0x88]
0084AC16  0F B7 C8                        movzx ecx, ax
0084AC19  EB AA                           jmp 0x14084abc5
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpGetNameControlBlock(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p18;
    unsigned __int16 v_stack_p70;
    unsigned __int64 v_stack_p78;
    unsigned __int16 v_stack_p80;
    unsigned __int64 v_stack_p88;

    v_stack_p18 = a3;
    v_rsp = (v_rsp) - (40);
    if (a2 == 0) goto loc_0084AAD4;
loc_0084A773:
    result = 0;
    v_rsi = (unsigned __int16)(((unsigned __int16)(*(unsigned __int16 *)(a1))) >> (1));
    if (condition_is_below_or_equal) goto loc_0084A7E3;
loc_0084A7A0:
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 0 * 2))) >= 97) goto loc_0084A7B6;
    goto loc_0084A7D4;
loc_0084A7B6:
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 0 * 2))) > 122) goto loc_0084AAE0;
    a2 = (unsigned __int16)((*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 0 * 2)) - (32));
loc_0084A7C8:
    v_rbp = 1;
    if (((unsigned __int16)(a2)) >= = 255) {
        v_rsi = (unsigned __int16)((unsigned __int16)(*(unsigned __int16 *)(a1)));
        v_rbp = 0;
    }
    v_rdi = (unsigned int)((0) + 1);
    result = (unsigned int)(((unsigned __int16)((unsigned __int16)(*(unsigned __int16 *)(a1)))) >> (1));
    if (((unsigned int)(v_rdi)) < ((unsigned int)(result))) goto loc_0084A7A0;
loc_0084A7E3:
    a3 = 0;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2))))) >> (9));
    a2 = 0;
    result = (unsigned int)((result) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(a2)))));
    v_r13 = (unsigned int)((v_r13) * ((unsigned int)(result)));
    v_rdi = ((unsigned int)((unsigned int)(v_r13))) >> (9);
    v_rdi = (v_rdi) ^ ((unsigned int)((unsigned int)(v_r13)));
    v_rdi = (unsigned int)((v_rdi) & (0x7FFULL));
    v_rdi = (v_rdi) << (4);
    v_rdi = (v_rdi) + (*(unsigned __int64 *)(v_rip + 6992228));
    result = KeAbPreAcquire(v_rdi, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = v_rdi;
        a2 = result;
        a1 = v_rdi;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    v_r12 = (unsigned int)(((unsigned int)((unsigned int)(v_r13))) >> (9));
    v_r12 = (unsigned int)((v_r12) ^ ((unsigned int)(v_r13)));
    v_r12 = (unsigned int)((v_r12) & (0x7FFULL));
    a1 = ((unsigned int)((unsigned int)(v_r12))) + ((unsigned int)((unsigned int)(v_r12)));
loc_0084A86C:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 6992178) + a1 * 8 + 8) == 0) goto loc_0084A883;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2)))) == (*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 6992178) + a1 * 8 + 8)))) goto loc_0084A9AC;
loc_0084A87D:
    goto loc_0084A86C;
loc_0084A883:
    result = CmpAllocatePool(256, (unsigned __int16)(v_rsi) + 26, (unsigned int)(0x624E4D43ULL), a4);
    if (result == 0) goto loc_0084AA72;
    if (0 == 0) goto loc_0084AB49;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(result))) | (1));
    *(unsigned int *)(result) = (unsigned int)(result);
    if ((unsigned int)((unsigned __int16)(v_rsi)) == 0) goto loc_0084A8F2;
    result = 0;
loc_0084A8D0:
    if (((unsigned __int16)(*(unsigned __int16 *)(0 + *(unsigned __int64 *)(a1 + 8) * 1))) >= 97) goto loc_0084A99B;
loc_0084A8E3:
    *(unsigned __int8 *)(result + 26) = (unsigned __int8)(*(unsigned __int16 *)(0 + *(unsigned __int64 *)(a1 + 8) * 1));
    v_r15 = (0) + (2);
    v_rdi = (result + 26) + 1;
    v_rbp = ((unsigned __int16)(v_rsi)) - (1);
    if (condition_is_not_equal) goto loc_0084A8D0;
loc_0084A8F2:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(result))) & (1));
    *(unsigned int *)(result + 8) = (unsigned int)((unsigned int)(*(unsigned int *)(a2)));
    result = (unsigned int)((result) | (2));
    *(unsigned __int16 *)(result + 24) = (unsigned __int16)(v_rsi);
    *(unsigned int *)(result) = (unsigned int)(result);
    a2 = ((unsigned int)((unsigned int)(v_r12))) << (4);
    a2 = (a2) + (*(unsigned __int64 *)(v_rip + 6991966));
    *(unsigned __int64 *)(result + 8 + 8) = *(unsigned __int64 *)(a2 + 8);
    *(unsigned __int64 *)(a2 + 8) = result + 8;
loc_0084A926:
    a3 = 0;
loc_0084A929:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2))))) >> (9));
    result = (unsigned int)((result) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(a2)))));
    result = (unsigned int)((result) * ((unsigned int)(result)));
    v_rbx = ((unsigned int)((unsigned int)(result))) >> (9);
    v_rbx = (v_rbx) ^ ((unsigned int)((unsigned int)(result)));
    v_rbx = (unsigned int)((v_rbx) & (0x7FFULL));
    v_rbx = (v_rbx) << (4);
    v_rbx = (v_rbx) + (*(unsigned __int64 *)(v_rip + 6991910));
    a1 = (*(unsigned __int64 *)(v_rbx)) & (-16);
    a2 = *(unsigned __int64 *)(v_rbx) - 16;
    if (a1 <= 16) { a2 = 0; }
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rbx))) & (2)) != 0) goto loc_0084AB01;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rbx))) & (2)) != 0) goto loc_0084AB01;
loc_0084A97E:
    result = KeAbPostRelease(v_rbx, a2, a3, a4);
loc_0084A989:
    v_rsp = (v_rsp) + (40);
    return result;
loc_0084A99B:
    if (((unsigned __int16)(result)) > 122) goto loc_0084AAF4;
    result = (unsigned __int8)((result) - (32));
    goto loc_0084A8E3;
loc_0084A9AC:
    if (((unsigned __int16)(v_rsi)) != (*(unsigned __int16 *)(result + 24))) goto loc_0084A87D;
    v_stack_p88 = result + 26;
    v_stack_p78 = *(unsigned __int64 *)(a1 + 8);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result)))) & (1)) == 0) goto loc_0084AB95;
    v_r15 = (unsigned __int16)((*(unsigned __int16 *)(a1)) >> (1));
loc_0084A9E3:
    v_stack_p80 = (unsigned __int16)((unsigned __int16)(v_rsi));
    if ((unsigned __int16)(v_r15) == 0) goto loc_0084AA43;
    if ((unsigned __int16)((unsigned __int16)(v_rsi)) == 0) goto loc_0084AA43;
    a4 = (result + 26) + 1;
    a3 = (*(unsigned __int64 *)(a1 + 8)) + (2);
    v_stack_p78 = a3;
    v_stack_p70 = (unsigned __int16)(*(unsigned __int8 *)(result + 26));
    v_stack_p88 = a4;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8)))) == ((unsigned __int16)(*(unsigned __int8 *)(result + 26)))) goto loc_0084AA39;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8)))) < 97) goto loc_0084AA30;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8)))) > 122) goto loc_0084AB18;
    a1 = (unsigned __int16)((*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8))) + ((unsigned __int16)((unsigned int)(0xFFE0ULL))));
loc_0084AA30:
    if (((unsigned __int16)(a1)) != ((unsigned __int16)(*(unsigned __int8 *)(result + 26)))) goto loc_0084A87D;
loc_0084AA39:
    v_r15 = (unsigned __int16)((v_r15) + ((unsigned __int16)((unsigned int)(0xFFE0ULL) + 31)));
    a2 = (unsigned __int16)(((unsigned __int16)(v_rsi)) + ((unsigned __int16)((unsigned int)(0xFFE0ULL) + 31)));
    goto loc_0084A9E3;
loc_0084AA43:
    if (((unsigned __int16)(v_r15)) != ((unsigned __int16)(a2))) goto loc_0084A87D;
loc_0084AA4D:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result))))) & (0xFFFFFFFEULL));
    if (((unsigned int)(result)) == -2) goto loc_0084ABF6;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(result))) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(result)) + 2)));
    a1 = (unsigned int)((a1) & (1));
    a1 = (unsigned int)((a1) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(result)) + 2)));
    *(unsigned int *)(result) = (unsigned int)(a1);
    goto loc_0084A926;
loc_0084AA72:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) >> (9));
    result = (unsigned int)((result) ^ ((unsigned int)(v_rbx)));
    result = (unsigned int)((result) * ((unsigned int)(result)));
    v_rbx = ((unsigned int)((unsigned int)(result))) >> (9);
    v_rbx = (v_rbx) ^ ((unsigned int)((unsigned int)(result)));
    v_rbx = (unsigned int)((v_rbx) & (0x7FFULL));
    v_rbx = (v_rbx) << (4);
    v_rbx = (v_rbx) + (*(unsigned __int64 *)(v_rip + 6991581));
    a1 = (*(unsigned __int64 *)(v_rbx)) & (-16);
    a2 = *(unsigned __int64 *)(v_rbx) - 16;
    if (a1 <= 16) { a2 = 0; }
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rbx))) & (2)) != 0) goto loc_0084AB0E;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rbx))) & (2)) != 0) goto loc_0084AB0E;
loc_0084AAC5:
    result = KeAbPostRelease(v_rbx, a2, 0, a4);
    result = 0;
    goto loc_0084A989;
loc_0084AAD4:
    result = CmpHashUnicodeComponent(v_rbx, a2, 0, a4);
    goto loc_0084A773;
loc_0084AAE0:
    result = RtlUpcaseUnicodeChar((unsigned __int16)(a2), a2, 0, a4);
    goto loc_0084A7C8;
loc_0084AAF4:
    result = RtlUpcaseUnicodeChar((unsigned __int16)(*(unsigned __int16 *)(a1)), (unsigned __int16)(result), 0, a4);
    goto loc_0084A8E3;
loc_0084AB01:
    result = ExfReleasePushLock((unsigned int)((unsigned int)(result)), (unsigned __int16)(result), 0, a4);
    goto loc_0084A97E;
loc_0084AB0E:
    result = ExfReleasePushLock((unsigned int)((unsigned int)(result)), (unsigned __int16)(result), 0, a4);
    goto loc_0084AAC5;
loc_0084AB18:
    result = RtlUpcaseUnicodeChar((unsigned int)((unsigned int)(result)), (unsigned __int16)(result), 0, a4);
    goto loc_0084AA30;
loc_0084AB49:
    result = (unsigned int)((v_stack_p70) & (0xFFFFFFFEULL));
    v_rdi = (unsigned int)((v_rdi) >> (1));
    *(unsigned int *)(result) = (unsigned int)(result);
    if (condition_is_equal) goto loc_0084A8F2;
    result = 0;
loc_0084AB5D:
    if (((unsigned __int16)(*(unsigned __int16 *)(0 + *(unsigned __int64 *)(a1 + 8) * 1))) < 97) goto loc_0084AB76;
    if (((unsigned __int16)(*(unsigned __int16 *)(0 + *(unsigned __int64 *)(a1 + 8) * 1))) > 122) goto loc_0084AB8B;
    result = (unsigned __int16)((*(unsigned __int16 *)(0 + *(unsigned __int64 *)(a1 + 8) * 1)) - (32));
loc_0084AB76:
    *(unsigned __int16 *)(0 + result * 1 + 26) = (unsigned __int16)(result);
    v_r15 = (0) + (2);
    v_rdi = (v_rdi) - (1);
    if (condition_is_not_equal) goto loc_0084AB5D;
    goto loc_0084A8F2;
loc_0084AB8B:
    result = RtlUpcaseUnicodeChar((unsigned __int16)(result), v_stack_p80, v_stack_p78, v_stack_p88);
    goto loc_0084AB76;
loc_0084AB95:
    a2 = 0;
loc_0084ABA0:
    result = (unsigned int)((*(unsigned __int16 *)(result + 24)) >> (1));
    if (0 >= ((unsigned int)(result))) goto loc_0084AA4D;
    if (((unsigned int)(*(unsigned __int16 *)(v_stack_p78))) < 97) goto loc_0084ABC3;
    if (((unsigned int)(*(unsigned __int16 *)(v_stack_p78))) > 122) goto loc_0084AC01;
    goto loc_0084ABC5;
loc_0084ABC3:
loc_0084ABC5:
    if (((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_stack_p78))))) != ((unsigned int)(*(unsigned __int16 *)(v_stack_p88)))) goto loc_0084ABE7;
    a3 = (v_stack_p78) + (2);
    a4 = (v_stack_p88) + (2);
    v_stack_p78 = a3;
    v_r15 = (unsigned int)((0) + 1);
    v_stack_p88 = a4;
    goto loc_0084ABA0;
loc_0084ABE7:
    goto loc_0084A87D;
loc_0084ABF6:
    a3 = 0;
    goto loc_0084A929;
loc_0084AC01:
    result = RtlUpcaseUnicodeChar((unsigned __int16)(*(unsigned __int16 *)(v_stack_p88)), a2, a3, a4);
    goto loc_0084ABC5;
}
```

## 5. (Beta) C Style

```c
int64_t CmpGetNameControlBlock(void *Arg1, int64_t Arg2, int64_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_p18;
    uint16_t v_stack_p70;
    uint64_t v_stack_p78;
    uint16_t v_stack_p80;
    uint64_t v_stack_p88;

    v_stack_p18 = Arg3;
    local_rsp = (local_rsp) - (40);
    if (Arg2 == 0) goto loc_0084AAD4;
loc_0084A773:
    result = 0;
    local_rsi = (uint16_t)(((uint16_t)(*(uint16_t *)(arg1))) >> (1));
    if (condition_is_below_or_equal) goto loc_0084A7E3;
loc_0084A7A0:
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0x0 * 2))) >= 97) goto loc_0084A7B6;
    goto loc_0084A7D4;
loc_0084A7B6:
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0x0 * 2))) > 122) goto loc_0084AAE0;
    Arg2 = (uint16_t)((*(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0x0 * 2)) - (32));
loc_0084A7C8:
    local_rbp = 1;
    if (((uint16_t)(Arg2)) >= = 255) {
        local_rsi = (uint16_t)((uint16_t)(*(uint16_t *)(arg1)));
        local_rbp = 0;
    }
    local_rdi = (uint32_t)((0) + 1);
    result = (uint32_t)(((uint16_t)((uint16_t)(*(uint16_t *)(arg1)))) >> (1));
    if (((uint32_t)(local_rdi)) < ((uint32_t)(result))) goto loc_0084A7A0;
loc_0084A7E3:
    Arg3 = 0;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg2))))) >> (9));
    Arg2 = 0;
    result = (uint32_t)((result) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(Arg2)))));
    local_r13 = (uint32_t)((local_r13) * ((uint32_t)(result)));
    local_rdi = ((uint32_t)((uint32_t)(local_r13))) >> (9);
    local_rdi = (local_rdi) ^ ((uint32_t)((uint32_t)(local_r13)));
    local_rdi = (uint32_t)((local_rdi) & (0x7FFULL));
    local_rdi = (local_rdi) << (4);
    local_rdi = (local_rdi) + (*(uint64_t *)(v_rip + 0x6AB164));
    result = KeAbPreAcquire(local_rdi, Arg2, Arg3, a4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = local_rdi;
        Arg2 = result;
        Arg1 = local_rdi;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, a4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    local_r12 = (uint32_t)(((uint32_t)((uint32_t)(local_r13))) >> (9));
    local_r12 = (uint32_t)((local_r12) ^ ((uint32_t)(local_r13)));
    local_r12 = (uint32_t)((local_r12) & (0x7FFULL));
    Arg1 = ((uint32_t)((uint32_t)(local_r12))) + ((uint32_t)((uint32_t)(local_r12)));
loc_0084A86C:
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0x6AB132) + arg1 * 8 + 0x8) == 0) goto loc_0084A883;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg2)))) == (*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x6AB132) + arg1 * 8 + 0x8)))) goto loc_0084A9AC;
loc_0084A87D:
    goto loc_0084A86C;
loc_0084A883:
    result = CmpAllocatePool(256, (uint16_t)(local_rsi) + 26, (uint32_t)(0x624E4D43ULL), a4);
    if (result == 0) goto loc_0084AA72;
    if (0 == 0) goto loc_0084AB49;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(result))) | (1));
    *(uint32_t *)(result) = (uint32_t)(result);
    if ((uint32_t)((uint16_t)(local_rsi)) == 0) goto loc_0084A8F2;
    result = 0;
loc_0084A8D0:
    if (((uint16_t)(*(uint16_t *)(0 + *(uint64_t *)(arg1 + 0x8) * 1))) >= 97) goto loc_0084A99B;
loc_0084A8E3:
    *(uint8_t *)(result + 0x1A) = (uint8_t)(*(uint16_t *)(0 + *(uint64_t *)(arg1 + 0x8) * 1));
    local_r15 = (0) + (2);
    local_rdi = (result + 26) + 1;
    local_rbp = ((uint16_t)(local_rsi)) - (1);
    if (condition_is_not_equal) goto loc_0084A8D0;
loc_0084A8F2:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(result))) & (1));
    *(uint32_t *)(result + 0x8) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg2)));
    result = (uint32_t)((result) | (2));
    *(uint16_t *)(result + 0x18) = (uint16_t)(local_rsi);
    *(uint32_t *)(result) = (uint32_t)(result);
    Arg2 = ((uint32_t)((uint32_t)(local_r12))) << (4);
    Arg2 = (Arg2) + (*(uint64_t *)(v_rip + 0x6AB05E));
    *(uint64_t *)(result + 0x8 + 0x8) = *(uint64_t *)(Arg2 + 0x8);
    *(uint64_t *)(Arg2 + 0x8) = result + 8;
loc_0084A926:
    Arg3 = 0;
loc_0084A929:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg2))))) >> (9));
    result = (uint32_t)((result) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(Arg2)))));
    result = (uint32_t)((result) * ((uint32_t)(result)));
    local_rbx = ((uint32_t)((uint32_t)(result))) >> (9);
    local_rbx = (local_rbx) ^ ((uint32_t)((uint32_t)(result)));
    local_rbx = (uint32_t)((local_rbx) & (0x7FFULL));
    local_rbx = (local_rbx) << (4);
    local_rbx = (local_rbx) + (*(uint64_t *)(v_rip + 0x6AB026));
    Arg1 = (*(uint64_t *)(local_rbx)) & (-16);
    Arg2 = *(uint64_t *)(local_rbx) - 16;
    if (Arg1 <= 16) { Arg2 = 0; }
    if ((((uint8_t)(*(uint64_t *)(local_rbx))) & (2)) != 0) goto loc_0084AB01;
    if ((((uint8_t)(*(uint64_t *)(local_rbx))) & (2)) != 0) goto loc_0084AB01;
loc_0084A97E:
    result = KeAbPostRelease(local_rbx, Arg2, Arg3, a4);
loc_0084A989:
    local_rsp = (local_rsp) + (40);
    return result;
loc_0084A99B:
    if (((uint16_t)(result)) > 122) goto loc_0084AAF4;
    result = (uint8_t)((result) - (32));
    goto loc_0084A8E3;
loc_0084A9AC:
    if (((uint16_t)(local_rsi)) != (*(uint16_t *)(result + 0x18))) goto loc_0084A87D;
    v_stack_p88 = result + 26;
    v_stack_p78 = *(uint64_t *)(arg1 + 0x8);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result)))) & (1)) == 0) goto loc_0084AB95;
    local_r15 = (uint16_t)((*(uint16_t *)(arg1)) >> (1));
loc_0084A9E3:
    v_stack_p80 = (uint16_t)((uint16_t)(local_rsi));
    if ((uint16_t)(local_r15) == 0) goto loc_0084AA43;
    if ((uint16_t)((uint16_t)(local_rsi)) == 0) goto loc_0084AA43;
    a4 = (result + 26) + 1;
    Arg3 = (*(uint64_t *)(arg1 + 0x8)) + (2);
    v_stack_p78 = Arg3;
    v_stack_p70 = (uint16_t)(*(uint8_t *)(result + 0x1A));
    v_stack_p88 = a4;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0x8)))) == ((uint16_t)(*(uint8_t *)(result + 0x1A)))) goto loc_0084AA39;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0x8)))) < 97) goto loc_0084AA30;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0x8)))) > 122) goto loc_0084AB18;
    Arg1 = (uint16_t)((*(uint16_t *)(*(uint64_t *)(arg1 + 0x8))) + ((uint16_t)((uint32_t)(0xFFE0ULL))));
loc_0084AA30:
    if (((uint16_t)(Arg1)) != ((uint16_t)(*(uint8_t *)(result + 0x1A)))) goto loc_0084A87D;
loc_0084AA39:
    local_r15 = (uint16_t)((local_r15) + ((uint16_t)((uint32_t)(0xFFE0ULL) + 31)));
    Arg2 = (uint16_t)(((uint16_t)(local_rsi)) + ((uint16_t)((uint32_t)(0xFFE0ULL) + 31)));
    goto loc_0084A9E3;
loc_0084AA43:
    if (((uint16_t)(local_r15)) != ((uint16_t)(Arg2))) goto loc_0084A87D;
loc_0084AA4D:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result))))) & (0xFFFFFFFEULL));
    if (((uint32_t)(result)) == -2) goto loc_0084ABF6;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(result))) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(result)) + 2)));
    Arg1 = (uint32_t)((Arg1) & (1));
    Arg1 = (uint32_t)((Arg1) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(result)) + 2)));
    *(uint32_t *)(result) = (uint32_t)(Arg1);
    goto loc_0084A926;
loc_0084AA72:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) >> (9));
    result = (uint32_t)((result) ^ ((uint32_t)(local_rbx)));
    result = (uint32_t)((result) * ((uint32_t)(result)));
    local_rbx = ((uint32_t)((uint32_t)(result))) >> (9);
    local_rbx = (local_rbx) ^ ((uint32_t)((uint32_t)(result)));
    local_rbx = (uint32_t)((local_rbx) & (0x7FFULL));
    local_rbx = (local_rbx) << (4);
    local_rbx = (local_rbx) + (*(uint64_t *)(v_rip + 0x6AAEDD));
    Arg1 = (*(uint64_t *)(local_rbx)) & (-16);
    Arg2 = *(uint64_t *)(local_rbx) - 16;
    if (Arg1 <= 16) { Arg2 = 0; }
    if ((((uint8_t)(*(uint64_t *)(local_rbx))) & (2)) != 0) goto loc_0084AB0E;
    if ((((uint8_t)(*(uint64_t *)(local_rbx))) & (2)) != 0) goto loc_0084AB0E;
loc_0084AAC5:
    result = KeAbPostRelease(local_rbx, Arg2, 0, a4);
    result = 0;
    goto loc_0084A989;
loc_0084AAD4:
    result = CmpHashUnicodeComponent(local_rbx, Arg2, 0, a4);
    goto loc_0084A773;
loc_0084AAE0:
    result = RtlUpcaseUnicodeChar((uint16_t)(Arg2), Arg2, 0, a4);
    goto loc_0084A7C8;
loc_0084AAF4:
    result = RtlUpcaseUnicodeChar((uint16_t)(*(uint16_t *)(arg1)), (uint16_t)(result), 0, a4);
    goto loc_0084A8E3;
loc_0084AB01:
    result = ExfReleasePushLock((uint32_t)((uint32_t)(result)), (uint16_t)(result), 0, a4);
    goto loc_0084A97E;
loc_0084AB0E:
    result = ExfReleasePushLock((uint32_t)((uint32_t)(result)), (uint16_t)(result), 0, a4);
    goto loc_0084AAC5;
loc_0084AB18:
    result = RtlUpcaseUnicodeChar((uint32_t)((uint32_t)(result)), (uint16_t)(result), 0, a4);
    goto loc_0084AA30;
loc_0084AB49:
    result = (uint32_t)((v_stack_p70) & (0xFFFFFFFEULL));
    local_rdi = (uint32_t)((local_rdi) >> (1));
    *(uint32_t *)(result) = (uint32_t)(result);
    if (condition_is_equal) goto loc_0084A8F2;
    result = 0;
loc_0084AB5D:
    if (((uint16_t)(*(uint16_t *)(0 + *(uint64_t *)(arg1 + 0x8) * 1))) < 97) goto loc_0084AB76;
    if (((uint16_t)(*(uint16_t *)(0 + *(uint64_t *)(arg1 + 0x8) * 1))) > 122) goto loc_0084AB8B;
    result = (uint16_t)((*(uint16_t *)(0 + *(uint64_t *)(arg1 + 0x8) * 1)) - (32));
loc_0084AB76:
    *(uint16_t *)(0 + result * 1 + 0x1A) = (uint16_t)(result);
    local_r15 = (0) + (2);
    local_rdi = (local_rdi) - (1);
    if (condition_is_not_equal) goto loc_0084AB5D;
    goto loc_0084A8F2;
loc_0084AB8B:
    result = RtlUpcaseUnicodeChar((uint16_t)(result), v_stack_p80, v_stack_p78, v_stack_p88);
    goto loc_0084AB76;
loc_0084AB95:
    Arg2 = 0;
loc_0084ABA0:
    result = (uint32_t)((*(uint16_t *)(result + 0x18)) >> (1));
    if (0 >= ((uint32_t)(result))) goto loc_0084AA4D;
    if (((uint32_t)(*(uint16_t *)(v_stack_p78))) < 97) goto loc_0084ABC3;
    if (((uint32_t)(*(uint16_t *)(v_stack_p78))) > 122) goto loc_0084AC01;
    goto loc_0084ABC5;
loc_0084ABC3:
loc_0084ABC5:
    if (((uint32_t)((uint32_t)((uint32_t)(*(uint16_t *)(v_stack_p78))))) != ((uint32_t)(*(uint16_t *)(v_stack_p88)))) goto loc_0084ABE7;
    Arg3 = (v_stack_p78) + (2);
    a4 = (v_stack_p88) + (2);
    v_stack_p78 = Arg3;
    local_r15 = (uint32_t)((0) + 1);
    v_stack_p88 = a4;
    goto loc_0084ABA0;
loc_0084ABE7:
    goto loc_0084A87D;
loc_0084ABF6:
    Arg3 = 0;
    goto loc_0084A929;
loc_0084AC01:
    result = RtlUpcaseUnicodeChar((uint16_t)(*(uint16_t *)(v_stack_p88)), Arg2, Arg3, a4);
    goto loc_0084ABC5;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `16` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0084A750&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
