# HdlspDispatch

- RVA: `0x00BBD320`–`0x00BBD9CB` (길이 `1,707` bytes)
- VA: `0x0000000140BBD320`
- 실행 섹션: `PAGEHDLS`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C6C4C`
- 디코드: `424`개 명령, `1,707/1,707` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **23**; 고유 호출 대상: **18**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **12**

### Outgoing calls
- `0x00BBD38B` → [KeAcquireSpinLockRaiseToDpc](../../text/20/KeAcquireSpinLockRaiseToDpc_function_00208470.md) (function, `0x00208470`)
- `0x00BBD3A9` → [KeReleaseSpinLock](../../text/39/KeReleaseSpinLock_function_00392BA0.md) (function, `0x00392BA0`)
- `0x00BBD3C4` → [KeReleaseSpinLock](../../text/39/KeReleaseSpinLock_function_00392BA0.md) (function, `0x00392BA0`)
- `0x00BBD4B3` → [HdlspPutString](HdlspPutString_function_00BBE2F0.md) (function, `0x00BBE2F0`)
- `0x00BBD4F5` → [HdlspGetLine](HdlspGetLine_function_00BBDAA4.md) (function, `0x00BBDAA4`)
- `0x00BBD50E` → [strcmp](../../text/6C/strcmp_function_006C7000.md) (function, `0x006C7000`)
- `0x00BBD523` → [strcmp](../../text/6C/strcmp_function_006C7000.md) (function, `0x006C7000`)
- `0x00BBD559` → [HdlspEnableTerminal](HdlspEnableTerminal_function_00BBD9D4.md) (function, `0x00BBD9D4`)
- `0x00BBD5C2` → [InbvPortPollOnly](../../text/6A/InbvPortPollOnly_function_006A82E8.md) (function, `0x006A82E8`)
- `0x00BBD5DC` → [InbvPortGetByte](../../text/6A/InbvPortGetByte_function_006A8134.md) (function, `0x006A8134`)
- `0x00BBD619` → [InbvPortPollOnly](../../text/6A/InbvPortPollOnly_function_006A82E8.md) (function, `0x006A82E8`)
- `0x00BBD659` → [sprintf_s](../../text/50/sprintf_s_function_00505E40.md) (function, `0x00505E40`)
- `0x00BBD690` → [HdlspSendStringAtBaud](HdlspSendStringAtBaud_function_00BBE5CC.md) (function, `0x00BBE5CC`)
- `0x00BBD6D9` → [HdlspGetLine](HdlspGetLine_function_00BBDAA4.md) (function, `0x00BBDAA4`)
- `0x00BBD6FD` → [HdlspSetBlueScreenInformation](HdlspSetBlueScreenInformation_function_00BBE600.md) (function, `0x00BBE600`)
- `0x00BBD78E` → [HdlspPutWideString](HdlspPutWideString_function_00BBE468.md) (function, `0x00BBE468`)
- `0x00BBD7DE` → [InbvPortPutByte](../../text/6A/InbvPortPutByte_function_006A8350.md) (function, `0x006A8350`)
- `0x00BBD847` → [HdlspSendBlueScreenInfo](HdlspSendBlueScreenInfo_function_00BBE528.md) (function, `0x00BBE528`)
- `0x00BBD853` → [HdlspSendStringAtBaud](HdlspSendStringAtBaud_function_00BBE5CC.md) (function, `0x00BBE5CC`)
- `0x00BBD8D2` → [HdlspProcessDumpCommand](HdlspProcessDumpCommand_function_00BBDFDC.md) (function, `0x00BBDFDC`)
- `0x00BBD8EE` → [HdlspAddLogEntry](HdlspAddLogEntry_function_00BBD008.md) (function, `0x00BBD008`)
- `0x00BBD98C` → [HdlspBugCheckProcessing](HdlspBugCheckProcessing_function_00BBD1F8.md) (function, `0x00BBD1F8`)
- `0x00BBD9B3` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [HeadlessDispatch](../../text/65/HeadlessDispatch_function_00655C40.md) at `0x00655C61`
- [HdlspKernelAddLogEntry](HdlspKernelAddLogEntry_function_00BBDD70.md) at `0x00BBDF9F`

### Static image references
- `0x00BBD332` → RVA `0x00E0A740` (`.data`; read)
- `0x00BBD37D` → RVA `0x00E68578` (`.data`; read)
- `0x00BBD47A` → RVA `0x00BBE9A0` (` ?? ::CIFEBFPJ::`string'`; read)
- `0x00BBD502` → RVA `0x00BBF370` (` ?? ::CIFEBFPJ::`string'`; read)
- `0x00BBD517` → RVA `0x00BBF340` (` ?? ::CIFEBFPJ::`string'`; read)
- `0x00BBD640` → RVA `0x00BBE9B0` (` ?? ::CIFEBFPJ::`string'`; read)
- `0x00BBD665` → RVA `0x00BBE980` (` ?? ::CIFEBFPJ::`string'`; read)
- `0x00BBD66E` → RVA `0x00BBE990` (` ?? ::CIFEBFPJ::`string'`; read)
- `0x00BBD677` → RVA `0x00BBF350` (` ?? ::CIFEBFPJ::`string'`; read)
- `0x00BBD680` → RVA `0x00BBF360` (` ?? ::CIFEBFPJ::`string'`; read)
- `0x00BBD689` → RVA `0x00BBF330` (` ?? ::CIFEBFPJ::`string'`; read)
- `0x00BBD84C` → RVA `0x00BBE950` (` ?? ::CIFEBFPJ::`string'`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **11**
  - `0x00BBD38B` → [KeAcquireSpinLockRaiseToDpc](../../text/20/KeAcquireSpinLockRaiseToDpc_function_00208470.md) (`PAGEHDLS` → `.text`)
  - `0x00BBD3A9` → [KeReleaseSpinLock](../../text/39/KeReleaseSpinLock_function_00392BA0.md) (`PAGEHDLS` → `.text`)
  - `0x00BBD3C4` → [KeReleaseSpinLock](../../text/39/KeReleaseSpinLock_function_00392BA0.md) (`PAGEHDLS` → `.text`)
  - `0x00BBD50E` → [strcmp](../../text/6C/strcmp_function_006C7000.md) (`PAGEHDLS` → `.text`)
  - `0x00BBD523` → [strcmp](../../text/6C/strcmp_function_006C7000.md) (`PAGEHDLS` → `.text`)
  - `0x00BBD5C2` → [InbvPortPollOnly](../../text/6A/InbvPortPollOnly_function_006A82E8.md) (`PAGEHDLS` → `.text`)
  - `0x00BBD5DC` → [InbvPortGetByte](../../text/6A/InbvPortGetByte_function_006A8134.md) (`PAGEHDLS` → `.text`)
  - `0x00BBD619` → [InbvPortPollOnly](../../text/6A/InbvPortPollOnly_function_006A82E8.md) (`PAGEHDLS` → `.text`)
  - `0x00BBD659` → [sprintf_s](../../text/50/sprintf_s_function_00505E40.md) (`PAGEHDLS` → `.text`)
  - `0x00BBD7DE` → [InbvPortPutByte](../../text/6A/InbvPortPutByte_function_006A8350.md) (`PAGEHDLS` → `.text`)
  - `0x00BBD9B3` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGEHDLS` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BBD320  40 53                           push rbx
00BBD322  55                              push rbp
00BBD323  56                              push rsi
00BBD324  57                              push rdi
00BBD325  41 54                           push r12
00BBD327  41 56                           push r14
00BBD329  41 57                           push r15
00BBD32B  48 81 EC A0 00 00 00            sub rsp, 0xa0
00BBD332  48 8B 05 07 D4 24 00            mov rax, qword ptr [rip + 0x24d407]
00BBD339  48 33 C4                        xor rax, rsp
00BBD33C  48 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], rax
00BBD344  48 8B AC 24 00 01 00 00         mov rbp, qword ptr [rsp + 0x100]
00BBD34C  33 DB                           xor ebx, ebx
00BBD34E  4D 8B F1                        mov r14, r9
00BBD351  4D 8B E0                        mov r12, r8
00BBD354  4C 8B FA                        mov r15, rdx
00BBD357  8B F1                           mov esi, ecx
00BBD359  83 F9 11                        cmp ecx, 0x11
00BBD35C  0F 84 05 05 00 00               je 0x140bbd867
00BBD362  83 F9 0E                        cmp ecx, 0xe
00BBD365  0F 84 FC 04 00 00               je 0x140bbd867
00BBD36B  83 F9 14                        cmp ecx, 0x14
00BBD36E  0F 84 AF 04 00 00               je 0x140bbd823
00BBD374  83 F9 0F                        cmp ecx, 0xf
00BBD377  0F 84 EA 04 00 00               je 0x140bbd867
00BBD37D  48 8B 0D F4 B1 2A 00            mov rcx, qword ptr [rip + 0x2ab1f4]
00BBD384  8B 41 30                        mov eax, dword ptr [rcx + 0x30]
00BBD387  A8 02                           test al, 2
00BBD389  75 07                           jne 0x140bbd392
00BBD38B  E8 E0 B0 64 FF                  call 0x140208470
00BBD390  EB 02                           jmp 0x140bbd394
00BBD392  B0 FF                           mov al, 0xff
00BBD394  48 8B 0D DD B1 2A 00            mov rcx, qword ptr [rip + 0x2ab1dd]
00BBD39B  8B 51 30                        mov edx, dword ptr [rcx + 0x30]
00BBD39E  F6 C2 40                        test dl, 0x40
00BBD3A1  74 15                           je 0x140bbd3b8
00BBD3A3  3C FF                           cmp al, 0xff
00BBD3A5  74 07                           je 0x140bbd3ae
00BBD3A7  8A D0                           mov dl, al
00BBD3A9  E8 F2 57 7D FF                  call 0x140392ba0
00BBD3AE  B8 01 00 00 C0                  mov eax, 0xc0000001
00BBD3B3  E9 F0 05 00 00                  jmp 0x140bbd9a8
00BBD3B8  83 CA 40                        or edx, 0x40
00BBD3BB  89 51 30                        mov dword ptr [rcx + 0x30], edx
00BBD3BE  3C FF                           cmp al, 0xff
00BBD3C0  74 07                           je 0x140bbd3c9
00BBD3C2  8A D0                           mov dl, al
00BBD3C4  E8 D7 57 7D FF                  call 0x140392ba0
00BBD3C9  83 FE 0D                        cmp esi, 0xd
00BBD3CC  0F 8F 11 03 00 00               jg 0x140bbd6e3
00BBD3D2  0F 84 C2 02 00 00               je 0x140bbd69a
00BBD3D8  83 FE 07                        cmp esi, 7
00BBD3DB  0F 8F 82 01 00 00               jg 0x140bbd563
00BBD3E1  74 30                           je 0x140bbd413
00BBD3E3  8B CE                           mov ecx, esi
00BBD3E5  83 E9 01                        sub ecx, 1
00BBD3E8  0F 84 51 01 00 00               je 0x140bbd53f
00BBD3EE  83 E9 01                        sub ecx, 1
00BBD3F1  0F 84 C6 00 00 00               je 0x140bbd4bd
00BBD3F7  83 E9 01                        sub ecx, 1
00BBD3FA  0F 84 8F 00 00 00               je 0x140bbd48f
00BBD400  83 E9 01                        sub ecx, 1
00BBD403  74 0E                           je 0x140bbd413
00BBD405  83 E9 01                        sub ecx, 1
00BBD408  74 09                           je 0x140bbd413
00BBD40A  83 F9 01                        cmp ecx, 1
00BBD40D  0F 85 77 04 00 00               jne 0x140bbd88a
00BBD413  48 8B 05 5E B1 2A 00            mov rax, qword ptr [rip + 0x2ab15e]
00BBD41A  BF 01 00 00 00                  mov edi, 1
00BBD41F  8B 48 30                        mov ecx, dword ptr [rax + 0x30]
00BBD422  40 84 CF                        test dil, cl
00BBD425  0F 84 40 05 00 00               je 0x140bbd96b
00BBD42B  83 EE 04                        sub esi, 4
00BBD42E  0F 84 55 02 00 00               je 0x140bbd689
00BBD434  2B F7                           sub esi, edi
00BBD436  0F 84 44 02 00 00               je 0x140bbd680
00BBD43C  2B F7                           sub esi, edi
00BBD43E  0F 84 33 02 00 00               je 0x140bbd677
00BBD444  2B F7                           sub esi, edi
00BBD446  0F 84 22 02 00 00               je 0x140bbd66e
00BBD44C  2B F7                           sub esi, edi
00BBD44E  0F 84 11 02 00 00               je 0x140bbd665
00BBD454  2B F7                           sub esi, edi
00BBD456  0F 84 CE 01 00 00               je 0x140bbd62a
00BBD45C  3B F7                           cmp esi, edi
00BBD45E  0F 85 02 05 00 00               jne 0x140bbd966
00BBD464  4D 85 FF                        test r15, r15
00BBD467  0F 84 F9 04 00 00               je 0x140bbd966
00BBD46D  49 83 FC 08                     cmp r12, 8
00BBD471  0F 85 EF 04 00 00               jne 0x140bbd966
00BBD477  41 8B 07                        mov eax, dword ptr [r15]
00BBD47A  4C 8D 05 1F 15 00 00            lea r8, [rip + 0x151f]
00BBD481  45 8B 4F 04                     mov r9d, dword ptr [r15 + 4]
00BBD485  03 C7                           add eax, edi
00BBD487  44 03 CF                        add r9d, edi
00BBD48A  E9 BC 01 00 00                  jmp 0x140bbd64b
00BBD48F  4D 85 FF                        test r15, r15
00BBD492  0F 84 CE 04 00 00               je 0x140bbd966
00BBD498  48 8B 05 D9 B0 2A 00            mov rax, qword ptr [rip + 0x2ab0d9]
00BBD49F  BF 01 00 00 00                  mov edi, 1
00BBD4A4  8B 50 30                        mov edx, dword ptr [rax + 0x30]
00BBD4A7  40 84 D7                        test dil, dl
00BBD4AA  0F 84 BB 04 00 00               je 0x140bbd96b
00BBD4B0  49 8B CF                        mov rcx, r15
00BBD4B3  E8 38 0E 00 00                  call 0x140bbe2f0
00BBD4B8  E9 AE 04 00 00                  jmp 0x140bbd96b
00BBD4BD  4D 85 F6                        test r14, r14
00BBD4C0  0F 84 A0 04 00 00               je 0x140bbd966
00BBD4C6  48 85 ED                        test rbp, rbp
00BBD4C9  0F 84 97 04 00 00               je 0x140bbd966
00BBD4CF  BF 01 00 00 00                  mov edi, 1
00BBD4D4  48 39 7D 00                     cmp qword ptr [rbp], rdi
00BBD4D8  0F 85 88 04 00 00               jne 0x140bbd966
00BBD4DE  48 8B 05 93 B0 2A 00            mov rax, qword ptr [rip + 0x2ab093]
00BBD4E5  8B 48 30                        mov ecx, dword ptr [rax + 0x30]
00BBD4E8  40 84 CF                        test dil, cl
00BBD4EB  74 4A                           je 0x140bbd537
00BBD4ED  8D 57 4F                        lea edx, [rdi + 0x4f]
00BBD4F0  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
00BBD4F5  E8 AA 05 00 00                  call 0x140bbdaa4
00BBD4FA  84 C0                           test al, al
00BBD4FC  0F 84 69 04 00 00               je 0x140bbd96b
00BBD502  48 8D 15 67 1E 00 00            lea rdx, [rip + 0x1e67]
00BBD509  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
00BBD50E  E8 ED 9A B0 FF                  call 0x1406c7000
00BBD513  85 C0                           test eax, eax
00BBD515  74 18                           je 0x140bbd52f
00BBD517  48 8D 15 22 1E 00 00            lea rdx, [rip + 0x1e22]
00BBD51E  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
00BBD523  E8 D8 9A B0 FF                  call 0x1406c7000
00BBD528  85 C0                           test eax, eax
00BBD52A  74 03                           je 0x140bbd52f
00BBD52C  40 8A FB                        mov dil, bl
00BBD52F  41 88 3E                        mov byte ptr [r14], dil
00BBD532  E9 34 04 00 00                  jmp 0x140bbd96b
00BBD537  41 88 1E                        mov byte ptr [r14], bl
00BBD53A  E9 2C 04 00 00                  jmp 0x140bbd96b
00BBD53F  4D 85 FF                        test r15, r15
00BBD542  0F 84 1E 04 00 00               je 0x140bbd966
00BBD548  BF 01 00 00 00                  mov edi, 1
00BBD54D  4C 3B E7                        cmp r12, rdi
00BBD550  0F 85 10 04 00 00               jne 0x140bbd966
00BBD556  41 8A 0F                        mov cl, byte ptr [r15]
00BBD559  E8 76 04 00 00                  call 0x140bbd9d4
00BBD55E  E9 9F 01 00 00                  jmp 0x140bbd702
00BBD563  8B CE                           mov ecx, esi
00BBD565  83 E9 08                        sub ecx, 8
00BBD568  0F 84 A5 FE FF FF               je 0x140bbd413
00BBD56E  83 E9 01                        sub ecx, 1
00BBD571  0F 84 9C FE FF FF               je 0x140bbd413
00BBD577  83 E9 01                        sub ecx, 1
00BBD57A  0F 84 93 FE FF FF               je 0x140bbd413
00BBD580  83 E9 01                        sub ecx, 1
00BBD583  74 61                           je 0x140bbd5e6
00BBD585  83 F9 01                        cmp ecx, 1
00BBD588  0F 85 FC 02 00 00               jne 0x140bbd88a
00BBD58E  4D 85 F6                        test r14, r14
00BBD591  0F 84 CF 03 00 00               je 0x140bbd966
00BBD597  48 85 ED                        test rbp, rbp
00BBD59A  0F 84 C6 03 00 00               je 0x140bbd966
00BBD5A0  8B F9                           mov edi, ecx
00BBD5A2  48 39 7D 00                     cmp qword ptr [rbp], rdi
00BBD5A6  0F 85 BA 03 00 00               jne 0x140bbd966
00BBD5AC  48 8B 0D C5 AF 2A 00            mov rcx, qword ptr [rip + 0x2aafc5]
00BBD5B3  8B 41 30                        mov eax, dword ptr [rcx + 0x30]
00BBD5B6  40 84 C7                        test dil, al
00BBD5B9  0F 84 78 FF FF FF               je 0x140bbd537
00BBD5BF  8B 49 38                        mov ecx, dword ptr [rcx + 0x38]
00BBD5C2  E8 21 AD AE FF                  call 0x1406a82e8
00BBD5C7  84 C0                           test al, al
00BBD5C9  0F 84 68 FF FF FF               je 0x140bbd537
00BBD5CF  48 8B 0D A2 AF 2A 00            mov rcx, qword ptr [rip + 0x2aafa2]
00BBD5D6  49 8B D6                        mov rdx, r14
00BBD5D9  8B 49 38                        mov ecx, dword ptr [rcx + 0x38]
00BBD5DC  E8 53 AB AE FF                  call 0x1406a8134
00BBD5E1  E9 85 03 00 00                  jmp 0x140bbd96b
00BBD5E6  4D 85 F6                        test r14, r14
00BBD5E9  0F 84 77 03 00 00               je 0x140bbd966
00BBD5EF  48 85 ED                        test rbp, rbp
00BBD5F2  0F 84 6E 03 00 00               je 0x140bbd966
00BBD5F8  BF 01 00 00 00                  mov edi, 1
00BBD5FD  48 39 7D 00                     cmp qword ptr [rbp], rdi
00BBD601  0F 85 5F 03 00 00               jne 0x140bbd966
00BBD607  48 8B 0D 6A AF 2A 00            mov rcx, qword ptr [rip + 0x2aaf6a]
00BBD60E  8B 41 30                        mov eax, dword ptr [rcx + 0x30]
00BBD611  40 84 C7                        test dil, al
00BBD614  74 0A                           je 0x140bbd620
00BBD616  8B 49 38                        mov ecx, dword ptr [rcx + 0x38]
00BBD619  E8 CA AC AE FF                  call 0x1406a82e8
00BBD61E  EB 02                           jmp 0x140bbd622
00BBD620  8A C3                           mov al, bl
00BBD622  41 88 06                        mov byte ptr [r14], al
00BBD625  E9 41 03 00 00                  jmp 0x140bbd96b
00BBD62A  4D 85 FF                        test r15, r15
00BBD62D  0F 84 33 03 00 00               je 0x140bbd966
00BBD633  49 83 FC 08                     cmp r12, 8
00BBD637  0F 85 29 03 00 00               jne 0x140bbd966
00BBD63D  41 8B 07                        mov eax, dword ptr [r15]
00BBD640  4C 8D 05 69 13 00 00            lea r8, [rip + 0x1369]
00BBD647  45 8B 4F 04                     mov r9d, dword ptr [r15 + 4]
00BBD64B  BA 50 00 00 00                  mov edx, 0x50
00BBD650  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00BBD654  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
00BBD659  E8 E2 87 94 FF                  call 0x140505e40
00BBD65E  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
00BBD663  EB 2B                           jmp 0x140bbd690
00BBD665  48 8D 0D 14 13 00 00            lea rcx, [rip + 0x1314]
00BBD66C  EB 22                           jmp 0x140bbd690
00BBD66E  48 8D 0D 1B 13 00 00            lea rcx, [rip + 0x131b]
00BBD675  EB 19                           jmp 0x140bbd690
00BBD677  48 8D 0D D2 1C 00 00            lea rcx, [rip + 0x1cd2]
00BBD67E  EB 10                           jmp 0x140bbd690
00BBD680  48 8D 0D D9 1C 00 00            lea rcx, [rip + 0x1cd9]
00BBD687  EB 07                           jmp 0x140bbd690
00BBD689  48 8D 0D A0 1C 00 00            lea rcx, [rip + 0x1ca0]
00BBD690  E8 37 0F 00 00                  call 0x140bbe5cc
00BBD695  E9 D1 02 00 00                  jmp 0x140bbd96b
00BBD69A  4D 85 F6                        test r14, r14
00BBD69D  0F 84 C3 02 00 00               je 0x140bbd966
00BBD6A3  48 85 ED                        test rbp, rbp
00BBD6A6  0F 84 BA 02 00 00               je 0x140bbd966
00BBD6AC  48 8B 55 00                     mov rdx, qword ptr [rbp]
00BBD6B0  48 83 FA 02                     cmp rdx, 2
00BBD6B4  0F 82 AC 02 00 00               jb 0x140bbd966
00BBD6BA  48 8B 05 B7 AE 2A 00            mov rax, qword ptr [rip + 0x2aaeb7]
00BBD6C1  BF 01 00 00 00                  mov edi, 1
00BBD6C6  8B 48 30                        mov ecx, dword ptr [rax + 0x30]
00BBD6C9  40 84 CF                        test dil, cl
00BBD6CC  0F 84 4E FF FF FF               je 0x140bbd620
00BBD6D2  48 FF CA                        dec rdx
00BBD6D5  49 8D 4E 01                     lea rcx, [r14 + 1]
00BBD6D9  E8 C6 03 00 00                  call 0x140bbdaa4
00BBD6DE  E9 3F FF FF FF                  jmp 0x140bbd622
00BBD6E3  83 FE 13                        cmp esi, 0x13
00BBD6E6  7F 21                           jg 0x140bbd709
00BBD6E8  0F 85 79 01 00 00               jne 0x140bbd867
00BBD6EE  4D 85 FF                        test r15, r15
00BBD6F1  0F 84 66 01 00 00               je 0x140bbd85d
00BBD6F7  49 8B D4                        mov rdx, r12
00BBD6FA  49 8B CF                        mov rcx, r15
00BBD6FD  E8 FE 0E 00 00                  call 0x140bbe600
00BBD702  8B D8                           mov ebx, eax
00BBD704  E9 62 02 00 00                  jmp 0x140bbd96b
00BBD709  8B CE                           mov ecx, esi
00BBD70B  83 E9 14                        sub ecx, 0x14
00BBD70E  0F 84 0F 01 00 00               je 0x140bbd823
00BBD714  83 E9 01                        sub ecx, 1
00BBD717  0F 84 D4 00 00 00               je 0x140bbd7f1
00BBD71D  83 E9 01                        sub ecx, 1
00BBD720  74 76                           je 0x140bbd798
00BBD722  83 E9 01                        sub ecx, 1
00BBD725  74 43                           je 0x140bbd76a
00BBD727  83 F9 01                        cmp ecx, 1
00BBD72A  0F 85 5A 01 00 00               jne 0x140bbd88a
00BBD730  4D 85 F6                        test r14, r14
00BBD733  0F 84 2D 02 00 00               je 0x140bbd966
00BBD739  48 85 ED                        test rbp, rbp
00BBD73C  0F 84 24 02 00 00               je 0x140bbd966
00BBD742  48 83 7D 00 0C                  cmp qword ptr [rbp], 0xc
00BBD747  0F 82 19 02 00 00               jb 0x140bbd966
00BBD74D  48 8B 05 24 AE 2A 00            mov rax, qword ptr [rip + 0x2aae24]
00BBD754  F2 0F 10 40 76                  movsd xmm0, qword ptr [rax + 0x76]
00BBD759  F2 41 0F 11 06                  movsd qword ptr [r14], xmm0
00BBD75E  8B 40 7E                        mov eax, dword ptr [rax + 0x7e]
00BBD761  41 89 46 08                     mov dword ptr [r14 + 8], eax
00BBD765  E9 01 02 00 00                  jmp 0x140bbd96b
00BBD76A  4D 85 FF                        test r15, r15
00BBD76D  0F 84 F3 01 00 00               je 0x140bbd966
00BBD773  48 8B 05 FE AD 2A 00            mov rax, qword ptr [rip + 0x2aadfe]
00BBD77A  BF 01 00 00 00                  mov edi, 1
00BBD77F  8B 48 30                        mov ecx, dword ptr [rax + 0x30]
00BBD782  40 84 CF                        test dil, cl
00BBD785  0F 84 E0 01 00 00               je 0x140bbd96b
00BBD78B  49 8B CF                        mov rcx, r15
00BBD78E  E8 D5 0C 00 00                  call 0x140bbe468
00BBD793  E9 D3 01 00 00                  jmp 0x140bbd96b
00BBD798  4D 85 FF                        test r15, r15
00BBD79B  0F 84 C5 01 00 00               je 0x140bbd966
00BBD7A1  4D 85 E4                        test r12, r12
00BBD7A4  0F 84 BC 01 00 00               je 0x140bbd966
00BBD7AA  48 8B 05 C7 AD 2A 00            mov rax, qword ptr [rip + 0x2aadc7]
00BBD7B1  BF 01 00 00 00                  mov edi, 1
00BBD7B6  8B 48 30                        mov ecx, dword ptr [rax + 0x30]
00BBD7B9  40 84 CF                        test dil, cl
00BBD7BC  0F 84 A9 01 00 00               je 0x140bbd96b
00BBD7C2  8B F3                           mov esi, ebx
00BBD7C4  4D 85 E4                        test r12, r12
00BBD7C7  0F 84 9E 01 00 00               je 0x140bbd96b
00BBD7CD  48 8B C3                        mov rax, rbx
00BBD7D0  48 8B 0D A1 AD 2A 00            mov rcx, qword ptr [rip + 0x2aada1]
00BBD7D7  42 8A 14 38                     mov dl, byte ptr [rax + r15]
00BBD7DB  8B 49 38                        mov ecx, dword ptr [rcx + 0x38]
00BBD7DE  E8 6D AB AE FF                  call 0x1406a8350
00BBD7E3  03 F7                           add esi, edi
00BBD7E5  8B C6                           mov eax, esi
00BBD7E7  49 3B C4                        cmp rax, r12
00BBD7EA  72 E4                           jb 0x140bbd7d0
00BBD7EC  E9 7A 01 00 00                  jmp 0x140bbd96b
00BBD7F1  4D 85 F6                        test r14, r14
00BBD7F4  0F 84 6C 01 00 00               je 0x140bbd966
00BBD7FA  48 85 ED                        test rbp, rbp
00BBD7FD  0F 84 63 01 00 00               je 0x140bbd966
00BBD803  48 83 7D 00 10                  cmp qword ptr [rbp], 0x10
00BBD808  0F 82 58 01 00 00               jb 0x140bbd966
00BBD80E  48 8B 05 63 AD 2A 00            mov rax, qword ptr [rip + 0x2aad63]
00BBD815  0F 10 40 64                     movups xmm0, xmmword ptr [rax + 0x64]
00BBD819  F3 41 0F 7F 06                  movdqu xmmword ptr [r14], xmm0
00BBD81E  E9 48 01 00 00                  jmp 0x140bbd96b
00BBD823  48 8B 05 4E AD 2A 00            mov rax, qword ptr [rip + 0x2aad4e]
00BBD82A  8B 48 30                        mov ecx, dword ptr [rax + 0x30]
00BBD82D  83 E1 03                        and ecx, 3
00BBD830  80 F9 03                        cmp cl, 3
00BBD833  0F 85 6D 01 00 00               jne 0x140bbd9a6
00BBD839  4D 85 FF                        test r15, r15
00BBD83C  74 1F                           je 0x140bbd85d
00BBD83E  49 83 FC 04                     cmp r12, 4
00BBD842  75 19                           jne 0x140bbd85d
00BBD844  41 8B 0F                        mov ecx, dword ptr [r15]
00BBD847  E8 DC 0C 00 00                  call 0x140bbe528
00BBD84C  48 8D 0D FD 10 00 00            lea rcx, [rip + 0x10fd]
00BBD853  E8 74 0D 00 00                  call 0x140bbe5cc
00BBD858  E9 49 01 00 00                  jmp 0x140bbd9a6
00BBD85D  B8 0D 00 00 C0                  mov eax, 0xc000000d
00BBD862  E9 41 01 00 00                  jmp 0x140bbd9a8
00BBD867  8B CE                           mov ecx, esi
00BBD869  83 E9 0E                        sub ecx, 0xe
00BBD86C  0F 84 21 01 00 00               je 0x140bbd993
00BBD872  83 E9 01                        sub ecx, 1
00BBD875  0F 84 FD 00 00 00               je 0x140bbd978
00BBD87B  83 E9 01                        sub ecx, 1
00BBD87E  74 78                           je 0x140bbd8f8
00BBD880  83 E9 01                        sub ecx, 1
00BBD883  74 57                           je 0x140bbd8dc
00BBD885  83 F9 01                        cmp ecx, 1
00BBD888  74 2E                           je 0x140bbd8b8
00BBD88A  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00BBD88F  83 FE 11                        cmp esi, 0x11
00BBD892  0F 84 0E 01 00 00               je 0x140bbd9a6
00BBD898  83 FE 0E                        cmp esi, 0xe
00BBD89B  0F 84 05 01 00 00               je 0x140bbd9a6
00BBD8A1  83 FE 14                        cmp esi, 0x14
00BBD8A4  0F 84 FC 00 00 00               je 0x140bbd9a6
00BBD8AA  83 FE 0F                        cmp esi, 0xf
00BBD8AD  0F 84 F3 00 00 00               je 0x140bbd9a6
00BBD8B3  E9 B3 00 00 00                  jmp 0x140bbd96b
00BBD8B8  4D 85 FF                        test r15, r15
00BBD8BB  0F 84 A5 00 00 00               je 0x140bbd966
00BBD8C1  BF 01 00 00 00                  mov edi, 1
00BBD8C6  4C 3B E7                        cmp r12, rdi
00BBD8C9  0F 85 97 00 00 00               jne 0x140bbd966
00BBD8CF  41 8A 0F                        mov cl, byte ptr [r15]
00BBD8D2  E8 05 07 00 00                  call 0x140bbdfdc
00BBD8D7  E9 8F 00 00 00                  jmp 0x140bbd96b
00BBD8DC  4D 85 FF                        test r15, r15
00BBD8DF  75 0A                           jne 0x140bbd8eb
00BBD8E1  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00BBD8E6  E9 BB 00 00 00                  jmp 0x140bbd9a6
00BBD8EB  49 8B CF                        mov rcx, r15
00BBD8EE  E8 15 F7 FF FF                  call 0x140bbd008
00BBD8F3  E9 AE 00 00 00                  jmp 0x140bbd9a6
00BBD8F8  4D 85 F6                        test r14, r14
00BBD8FB  74 69                           je 0x140bbd966
00BBD8FD  48 85 ED                        test rbp, rbp
00BBD900  74 64                           je 0x140bbd966
00BBD902  48 83 7D 00 20                  cmp qword ptr [rbp], 0x20
00BBD907  72 5D                           jb 0x140bbd966
00BBD909  48 8B 0D 68 AC 2A 00            mov rcx, qword ptr [rip + 0x2aac68]
00BBD910  BF 01 00 00 00                  mov edi, 1
00BBD915  41 89 3E                        mov dword ptr [r14], edi
00BBD918  41 88 7E 08                     mov byte ptr [r14 + 8], dil
00BBD91C  8B 41 30                        mov eax, dword ptr [rcx + 0x30]
00BBD91F  C1 E8 03                        shr eax, 3
00BBD922  40 22 C7                        and al, dil
00BBD925  41 88 46 09                     mov byte ptr [r14 + 9], al
00BBD929  8B 41 34                        mov eax, dword ptr [rcx + 0x34]
00BBD92C  41 89 46 18                     mov dword ptr [r14 + 0x18], eax
00BBD930  8B 51 30                        mov edx, dword ptr [rcx + 0x30]
00BBD933  8B C2                           mov eax, edx
00BBD935  C1 E8 09                        shr eax, 9
00BBD938  83 E0 07                        and eax, 7
00BBD93B  3B C7                           cmp eax, edi
00BBD93D  73 12                           jae 0x140bbd951
00BBD93F  C1 EA 03                        shr edx, 3
00BBD942  40 84 D7                        test dil, dl
00BBD945  75 0A                           jne 0x140bbd951
00BBD947  41 89 5E 0C                     mov dword ptr [r14 + 0xc], ebx
00BBD94B  49 89 5E 10                     mov qword ptr [r14 + 0x10], rbx
00BBD94F  EB 0C                           jmp 0x140bbd95d
00BBD951  41 89 46 0C                     mov dword ptr [r14 + 0xc], eax
00BBD955  48 8B 41 40                     mov rax, qword ptr [rcx + 0x40]
00BBD959  49 89 46 10                     mov qword ptr [r14 + 0x10], rax
00BBD95D  8A 41 54                        mov al, byte ptr [rcx + 0x54]
00BBD960  41 88 46 1C                     mov byte ptr [r14 + 0x1c], al
00BBD964  EB 05                           jmp 0x140bbd96b
00BBD966  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00BBD96B  48 8B 05 06 AC 2A 00            mov rax, qword ptr [rip + 0x2aac06]
00BBD972  83 60 30 BF                     and dword ptr [rax + 0x30], 0xffffffbf
00BBD976  EB 2E                           jmp 0x140bbd9a6
00BBD978  48 8B 05 F9 AB 2A 00            mov rax, qword ptr [rip + 0x2aabf9]
00BBD97F  BF 01 00 00 00                  mov edi, 1
00BBD984  8B 48 30                        mov ecx, dword ptr [rax + 0x30]
00BBD987  40 84 CF                        test dil, cl
00BBD98A  74 1A                           je 0x140bbd9a6
00BBD98C  E8 67 F8 FF FF                  call 0x140bbd1f8
00BBD991  EB 13                           jmp 0x140bbd9a6
00BBD993  48 8B 0D DE AB 2A 00            mov rcx, qword ptr [rip + 0x2aabde]
00BBD99A  8B 41 30                        mov eax, dword ptr [rcx + 0x30]
00BBD99D  83 C8 02                        or eax, 2
00BBD9A0  83 E0 BF                        and eax, 0xffffffbf
00BBD9A3  89 41 30                        mov dword ptr [rcx + 0x30], eax
00BBD9A6  8B C3                           mov eax, ebx
00BBD9A8  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
00BBD9B0  48 33 CC                        xor rcx, rsp
00BBD9B3  E8 88 EC AE FF                  call 0x1406ac640
00BBD9B8  48 81 C4 A0 00 00 00            add rsp, 0xa0
00BBD9BF  41 5F                           pop r15
00BBD9C1  41 5E                           pop r14
00BBD9C3  41 5C                           pop r12
00BBD9C5  5F                              pop rdi
00BBD9C6  5E                              pop rsi
00BBD9C7  5D                              pop rbp
00BBD9C8  5B                              pop rbx
00BBD9C9  C3                              ret
00BBD9CA  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HdlspDispatch(int a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m98;
    unsigned int v_stack_mB8;

    v_rsp = (v_rsp) - (160);
    result = (*(unsigned __int64 *)(v_rip + 2413575)) ^ (v_rsp);
    v_stack_m48 = result;
    v_rbx = 0;
    if (a1 == 17) goto loc_00BBD867;
    if (a1 == 14) goto loc_00BBD867;
    if (a1 == 20) goto loc_00BBD823;
    if (a1 == 15) goto loc_00BBD867;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 2798068) + 48)))) & (2)) != 0) goto loc_00BBD392;
    result = KeAcquireSpinLockRaiseToDpc(*(unsigned __int64 *)(v_rip + 2798068), a2, a3, a4);
    goto loc_00BBD394;
loc_00BBD392:
loc_00BBD394:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 2798045) + 48)))) & (64)) == 0) goto loc_00BBD3B8;
    result = 255;
    if (255 != 255) {
        a2 = 255;
        result = KeReleaseSpinLock(*(unsigned __int64 *)(v_rip + 2798045), a2, a3, a4);
    }
    goto loc_00BBD9A8;
loc_00BBD3B8:
    a2 = (unsigned int)((a2) | (64));
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 2798045) + 48) = (unsigned int)(a2);
    result = (unsigned int)(0xC0000001ULL);
    if (((unsigned __int8)((unsigned int)(0xC0000001ULL))) != 255) {
        a2 = (unsigned __int8)((unsigned int)(0xC0000001ULL));
        result = KeReleaseSpinLock(*(unsigned __int64 *)(v_rip + 2798045), a2, a3, a4);
    }
    if (((unsigned int)((unsigned int)(a1))) > 13) goto loc_00BBD6E3;
    if (((unsigned int)((unsigned int)(a1))) == 13) goto loc_00BBD69A;
    if (((unsigned int)((unsigned int)(a1))) > 7) goto loc_00BBD563;
    if (((unsigned int)((unsigned int)(a1))) == 7) goto loc_00BBD413;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a1)))) - (1));
    if (condition_is_equal) goto loc_00BBD53F;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00BBD4BD;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00BBD48F;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00BBD413;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00BBD413;
    if (a1 != 1) goto loc_00BBD88A;
loc_00BBD413:
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 2797918) + 48))))) == 0) goto loc_00BBD96B;
    v_rsi = (unsigned int)(((unsigned int)(a1)) - (4));
    if (condition_is_equal) goto loc_00BBD689;
    v_rsi = (unsigned int)((v_rsi) - (1));
    if (condition_is_equal) goto loc_00BBD680;
    v_rsi = (unsigned int)((v_rsi) - (1));
    if (condition_is_equal) goto loc_00BBD677;
    v_rsi = (unsigned int)((v_rsi) - (1));
    if (condition_is_equal) goto loc_00BBD66E;
    v_rsi = (unsigned int)((v_rsi) - (1));
    if (condition_is_equal) goto loc_00BBD665;
    v_rsi = (unsigned int)((v_rsi) - (1));
    if (condition_is_equal) goto loc_00BBD62A;
    if (((unsigned int)(v_rsi)) != 1) goto loc_00BBD966;
    if (a2 == 0) goto loc_00BBD966;
    if (a3 != 8) goto loc_00BBD966;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2))) + (1));
    a4 = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 4))) + (1));
    goto loc_00BBD64B;
loc_00BBD48F:
    if (a2 == 0) goto loc_00BBD966;
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 2797785) + 48))))) == 0) goto loc_00BBD96B;
    result = HdlspPutString(a2, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 2797785) + 48)), v_rip + 5407, a4);
    goto loc_00BBD96B;
loc_00BBD4BD:
    if (a4 == 0) goto loc_00BBD966;
    if (a5 == 0) goto loc_00BBD966;
    if ((*(unsigned __int64 *)(a5)) != 1) goto loc_00BBD966;
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 2797715) + 48))))) == 0) goto loc_00BBD537;
    result = HdlspGetLine(v_stack_m98, 1 + 79, v_rip + 5407, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00BBD96B;
    result = strcmp(v_stack_m98, v_rip + 7783, v_rip + 5407, a4);
    if ((unsigned int)(result) == 0) goto loc_00BBD52F;
    result = strcmp(v_stack_m98, v_rip + 7714, v_rip + 5407, a4);
    v_rdi = 1;
    if ((unsigned int)(result) != 0) {
        v_rdi = 0;
    }
    *(unsigned __int8 *)(a4) = (unsigned __int8)(v_rdi);
    goto loc_00BBD96B;
loc_00BBD537:
    *(unsigned __int8 *)(a4) = 0;
    goto loc_00BBD96B;
loc_00BBD53F:
    if (a2 == 0) goto loc_00BBD966;
    if (a3 != 1) goto loc_00BBD966;
    result = HdlspEnableTerminal(*(unsigned __int8 *)(a2), v_rip + 7714, v_rip + 5407, a4);
    goto loc_00BBD702;
loc_00BBD563:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_rsi))) - (8));
    if (condition_is_equal) goto loc_00BBD413;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00BBD413;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00BBD413;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00BBD5E6;
    if (a1 != 1) goto loc_00BBD88A;
    if (a4 == 0) goto loc_00BBD966;
    if (a5 == 0) goto loc_00BBD966;
    if ((*(unsigned __int64 *)(a5)) != ((unsigned int)(a1))) goto loc_00BBD966;
    if ((((unsigned __int8)((unsigned int)(a1))) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 2797509) + 48))))) == 0) goto loc_00BBD537;
    result = InbvPortPollOnly((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 2797509) + 56)), v_rip + 7714, v_rip + 5407, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00BBD537;
    result = InbvPortGetByte((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 2797474) + 56)), a4, v_rip + 5407, a4);
    goto loc_00BBD96B;
loc_00BBD5E6:
    if (a4 == 0) goto loc_00BBD966;
    if (a5 == 0) goto loc_00BBD966;
    if ((*(unsigned __int64 *)(a5)) != 1) goto loc_00BBD966;
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 2797418) + 48))))) == 0) goto loc_00BBD620;
    result = InbvPortPollOnly((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 2797418) + 56)), a4, v_rip + 5407, a4);
    goto loc_00BBD622;
loc_00BBD620:
loc_00BBD622:
    *(unsigned __int8 *)(a4) = 0;
    goto loc_00BBD96B;
loc_00BBD62A:
    if (a2 == 0) goto loc_00BBD966;
    if (a3 != 8) goto loc_00BBD966;
loc_00BBD64B:
    v_stack_mB8 = (unsigned int)((unsigned int)(*(unsigned int *)(a2)));
    result = sprintf_s(v_stack_m98, 80, v_rip + 4969, (unsigned int)(*(unsigned int *)(a2 + 4)));
    goto loc_00BBD690;
loc_00BBD665:
    goto loc_00BBD690;
loc_00BBD66E:
    goto loc_00BBD690;
loc_00BBD677:
    goto loc_00BBD690;
loc_00BBD680:
    goto loc_00BBD690;
loc_00BBD689:
loc_00BBD690:
    result = HdlspSendStringAtBaud(v_rip + 7328, 80, v_rip + 4969, (unsigned int)(*(unsigned int *)(a2 + 4)));
    goto loc_00BBD96B;
loc_00BBD69A:
    if (a4 == 0) goto loc_00BBD966;
    if (a5 == 0) goto loc_00BBD966;
    if ((*(unsigned __int64 *)(a5)) < 2) goto loc_00BBD966;
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 2797239) + 48))))) == 0) goto loc_00BBD620;
    a2 = (*(unsigned __int64 *)(a5)) - 1;
    result = HdlspGetLine(a4 + 1, a2, v_rip + 4969, (unsigned int)(*(unsigned int *)(a2 + 4)));
    goto loc_00BBD622;
loc_00BBD6E3:
    if (((unsigned int)(v_rsi)) > 19) goto loc_00BBD709;
    if (((unsigned int)(v_rsi)) != 19) goto loc_00BBD867;
    if (a2 == 0) goto loc_00BBD85D;
    result = HdlspSetBlueScreenInformation(a2, a3, v_rip + 4969, (unsigned int)(*(unsigned int *)(a2 + 4)));
loc_00BBD702:
    goto loc_00BBD96B;
loc_00BBD709:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_rsi))) - (20));
    if (condition_is_equal) goto loc_00BBD823;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00BBD7F1;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00BBD798;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00BBD76A;
    if (a1 != 1) goto loc_00BBD88A;
    if (a4 == 0) goto loc_00BBD966;
    if (a5 == 0) goto loc_00BBD966;
    if ((*(unsigned __int64 *)(a5)) < 12) goto loc_00BBD966;
    *(unsigned __int64 *)(a4) = v_xmm0;
    *(unsigned int *)(a4 + 8) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 2797092) + 126)));
    goto loc_00BBD96B;
loc_00BBD76A:
    if (a2 == 0) goto loc_00BBD966;
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 2797054) + 48))))) == 0) goto loc_00BBD96B;
    result = HdlspPutWideString(a2, a3, v_rip + 4969, (unsigned int)(*(unsigned int *)(a2 + 4)));
    goto loc_00BBD96B;
loc_00BBD798:
    if (a2 == 0) goto loc_00BBD966;
    if (a3 == 0) goto loc_00BBD966;
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 2796999) + 48))))) == 0) goto loc_00BBD96B;
    if (a3 == 0) goto loc_00BBD96B;
loc_00BBD7D0:
    result = InbvPortPutByte((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 2796961) + 56)), *(unsigned __int8 *)((unsigned int)((unsigned int)(result)) + a2 * 1), v_rip + 4969, (unsigned int)(*(unsigned int *)(a2 + 4)));
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))))) + (1));
    if (((unsigned int)((unsigned int)(v_rsi))) < a3) goto loc_00BBD7D0;
    goto loc_00BBD96B;
loc_00BBD7F1:
    if (a4 == 0) goto loc_00BBD966;
    if (a5 == 0) goto loc_00BBD966;
    if ((*(unsigned __int64 *)(a5)) < 16) goto loc_00BBD966;
    *(unsigned __int64 *)(a4) = v_xmm0;
    goto loc_00BBD96B;
loc_00BBD823:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 2796878) + 48))) & (3));
    if (((unsigned __int8)(a1)) != 3) goto loc_00BBD9A6;
    if (a2 == 0) goto loc_00BBD85D;
    if (a3 != 4) goto loc_00BBD85D;
    result = HdlspSendBlueScreenInfo((unsigned int)(*(unsigned int *)(a2)), *(unsigned __int8 *)((unsigned int)((unsigned int)(result)) + a2 * 1), v_rip + 4969, (unsigned int)(*(unsigned int *)(a2 + 4)));
    result = HdlspSendStringAtBaud(v_rip + 4349, *(unsigned __int8 *)((unsigned int)((unsigned int)(result)) + a2 * 1), v_rip + 4969, (unsigned int)(*(unsigned int *)(a2 + 4)));
    goto loc_00BBD9A6;
loc_00BBD85D:
    goto loc_00BBD9A8;
loc_00BBD867:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_rsi))) - (14));
    if (condition_is_equal) goto loc_00BBD993;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00BBD978;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00BBD8F8;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00BBD8DC;
    if (a1 == 1) goto loc_00BBD8B8;
loc_00BBD88A:
    if (((unsigned int)(v_rsi)) == 17) goto loc_00BBD9A6;
    if (((unsigned int)(v_rsi)) == 14) goto loc_00BBD9A6;
    if (((unsigned int)(v_rsi)) == 20) goto loc_00BBD9A6;
    if (((unsigned int)(v_rsi)) == 15) goto loc_00BBD9A6;
    goto loc_00BBD96B;
loc_00BBD8B8:
    if (a2 == 0) goto loc_00BBD966;
    if (a3 != 1) goto loc_00BBD966;
    result = HdlspProcessDumpCommand(*(unsigned __int8 *)(a2), *(unsigned __int8 *)((unsigned int)((unsigned int)(result)) + a2 * 1), v_rip + 4969, (unsigned int)(*(unsigned int *)(a2 + 4)));
    goto loc_00BBD96B;
loc_00BBD8DC:
    if (a2 != 0) goto loc_00BBD8EB;
    goto loc_00BBD9A6;
loc_00BBD8EB:
    result = HdlspAddLogEntry(a2, *(unsigned __int8 *)((unsigned int)((unsigned int)(result)) + a2 * 1), v_rip + 4969, (unsigned int)(*(unsigned int *)(a2 + 4)));
    goto loc_00BBD9A6;
loc_00BBD8F8:
    if (a4 == 0) goto loc_00BBD966;
    if (a5 == 0) goto loc_00BBD966;
    if ((*(unsigned __int64 *)(a5)) < 32) goto loc_00BBD966;
    *(unsigned int *)(a4) = 1;
    *(unsigned __int8 *)(a4 + 8) = 1;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 2796648) + 48))) >> (3));
    result = (unsigned __int8)((result) & (1));
    *(unsigned __int8 *)(a4 + 9) = (unsigned __int8)(result);
    *(unsigned int *)(a4 + 24) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 2796648) + 52)));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 2796648) + 48))))) >> (9));
    result = (unsigned int)((result) & (7));
    if (((unsigned int)(result)) >= 1) goto loc_00BBD951;
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 2796648) + 48))) >> (3));
    if (((1) & ((unsigned __int8)(a2))) != 0) goto loc_00BBD951;
    *(unsigned int *)(a4 + 12) = (unsigned int)((unsigned int)(0xC000000DULL));
    *(unsigned __int64 *)(a4 + 16) = (unsigned int)(0xC000000DULL);
    goto loc_00BBD95D;
loc_00BBD951:
    *(unsigned int *)(a4 + 12) = (unsigned int)(result);
    *(unsigned __int64 *)(a4 + 16) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 2796648) + 64);
loc_00BBD95D:
    *(unsigned __int8 *)(a4 + 28) = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 2796648) + 84));
    goto loc_00BBD96B;
loc_00BBD966:
loc_00BBD96B:
    goto loc_00BBD9A6;
loc_00BBD978:
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 2796537) + 48))))) == 0) goto loc_00BBD9A6;
    result = HdlspBugCheckProcessing((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 2796537) + 48)), a2, v_rip + 4969, (unsigned int)(*(unsigned int *)(a2 + 4)));
    goto loc_00BBD9A6;
loc_00BBD993:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 2796510) + 48))) | (2));
    result = (unsigned int)((result) & (0xFFFFFFBFULL));
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 2796510) + 48) = (unsigned int)(result);
loc_00BBD9A6:
loc_00BBD9A8:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, v_rip + 4969, (unsigned int)(*(unsigned int *)(a2 + 4)));
    v_rsp = (v_rsp) + (160);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HdlspDispatch(int32_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m98;
    uint32_t v_stack_mB8;

    local_rsp = (local_rsp) - (160);
    result = (*(uint64_t *)(v_rip + 0x24D407)) ^ (local_rsp);
    v_stack_m48 = result;
    local_rbx = 0;
    if (Arg1 == 17) goto loc_00BBD867;
    if (Arg1 == 14) goto loc_00BBD867;
    if (Arg1 == 20) goto loc_00BBD823;
    if (Arg1 == 15) goto loc_00BBD867;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x2AB1F4) + 0x30)))) & (2)) != 0) goto loc_00BBD392;
    result = KeAcquireSpinLockRaiseToDpc(*(uint64_t *)(v_rip + 0x2AB1F4), Arg2, Arg3, Arg4);
    goto loc_00BBD394;
loc_00BBD392:
loc_00BBD394:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x2AB1DD) + 0x30)))) & (64)) == 0) goto loc_00BBD3B8;
    result = 255;
    if (255 != 255) {
        Arg2 = 255;
        result = KeReleaseSpinLock(*(uint64_t *)(v_rip + 0x2AB1DD), Arg2, Arg3, Arg4);
    }
    goto loc_00BBD9A8;
loc_00BBD3B8:
    Arg2 = (uint32_t)((Arg2) | (64));
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x2AB1DD) + 0x30) = (uint32_t)(Arg2);
    result = (uint32_t)(0xC0000001ULL);
    if (((uint8_t)((uint32_t)(0xC0000001ULL))) != 255) {
        Arg2 = (uint8_t)((uint32_t)(0xC0000001ULL));
        result = KeReleaseSpinLock(*(uint64_t *)(v_rip + 0x2AB1DD), Arg2, Arg3, Arg4);
    }
    if (((uint32_t)((uint32_t)(Arg1))) > 13) goto loc_00BBD6E3;
    if (((uint32_t)((uint32_t)(Arg1))) == 13) goto loc_00BBD69A;
    if (((uint32_t)((uint32_t)(Arg1))) > 7) goto loc_00BBD563;
    if (((uint32_t)((uint32_t)(Arg1))) == 7) goto loc_00BBD413;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg1)))) - (1));
    if (condition_is_equal) goto loc_00BBD53F;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00BBD4BD;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00BBD48F;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00BBD413;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00BBD413;
    if (Arg1 != 1) goto loc_00BBD88A;
loc_00BBD413:
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x2AB15E) + 0x30))))) == 0) goto loc_00BBD96B;
    local_rsi = (uint32_t)(((uint32_t)(Arg1)) - (4));
    if (condition_is_equal) goto loc_00BBD689;
    local_rsi = (uint32_t)((local_rsi) - (1));
    if (condition_is_equal) goto loc_00BBD680;
    local_rsi = (uint32_t)((local_rsi) - (1));
    if (condition_is_equal) goto loc_00BBD677;
    local_rsi = (uint32_t)((local_rsi) - (1));
    if (condition_is_equal) goto loc_00BBD66E;
    local_rsi = (uint32_t)((local_rsi) - (1));
    if (condition_is_equal) goto loc_00BBD665;
    local_rsi = (uint32_t)((local_rsi) - (1));
    if (condition_is_equal) goto loc_00BBD62A;
    if (((uint32_t)(local_rsi)) != 1) goto loc_00BBD966;
    if (Arg2 == 0) goto loc_00BBD966;
    if (Arg3 != 8) goto loc_00BBD966;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg2))) + (1));
    Arg4 = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg2 + 0x4))) + (1));
    goto loc_00BBD64B;
loc_00BBD48F:
    if (Arg2 == 0) goto loc_00BBD966;
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x2AB0D9) + 0x30))))) == 0) goto loc_00BBD96B;
    result = HdlspPutString(Arg2, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x2AB0D9) + 0x30)), v_rip + 5407, Arg4);
    goto loc_00BBD96B;
loc_00BBD4BD:
    if (Arg4 == 0) goto loc_00BBD966;
    if (Arg5 == 0) goto loc_00BBD966;
    if ((*(uint64_t *)(Arg5)) != 1) goto loc_00BBD966;
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x2AB093) + 0x30))))) == 0) goto loc_00BBD537;
    result = HdlspGetLine(v_stack_m98, 1 + 79, v_rip + 5407, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00BBD96B;
    result = strcmp(v_stack_m98, v_rip + 7783, v_rip + 5407, Arg4);
    if ((uint32_t)(result) == 0) goto loc_00BBD52F;
    result = strcmp(v_stack_m98, v_rip + 7714, v_rip + 5407, Arg4);
    local_rdi = 1;
    if ((uint32_t)(result) != 0) {
        local_rdi = 0;
    }
    *(uint8_t *)(Arg4) = (uint8_t)(local_rdi);
    goto loc_00BBD96B;
loc_00BBD537:
    *(uint8_t *)(Arg4) = 0;
    goto loc_00BBD96B;
loc_00BBD53F:
    if (Arg2 == 0) goto loc_00BBD966;
    if (Arg3 != 1) goto loc_00BBD966;
    result = HdlspEnableTerminal(*(uint8_t *)(Arg2), v_rip + 7714, v_rip + 5407, Arg4);
    goto loc_00BBD702;
loc_00BBD563:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_rsi))) - (8));
    if (condition_is_equal) goto loc_00BBD413;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00BBD413;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00BBD413;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00BBD5E6;
    if (Arg1 != 1) goto loc_00BBD88A;
    if (Arg4 == 0) goto loc_00BBD966;
    if (Arg5 == 0) goto loc_00BBD966;
    if ((*(uint64_t *)(Arg5)) != ((uint32_t)(Arg1))) goto loc_00BBD966;
    if ((((uint8_t)((uint32_t)(Arg1))) & ((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x2AAFC5) + 0x30))))) == 0) goto loc_00BBD537;
    result = InbvPortPollOnly((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x2AAFC5) + 0x38)), v_rip + 7714, v_rip + 5407, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00BBD537;
    result = InbvPortGetByte((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x2AAFA2) + 0x38)), Arg4, v_rip + 5407, Arg4);
    goto loc_00BBD96B;
loc_00BBD5E6:
    if (Arg4 == 0) goto loc_00BBD966;
    if (Arg5 == 0) goto loc_00BBD966;
    if ((*(uint64_t *)(Arg5)) != 1) goto loc_00BBD966;
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x2AAF6A) + 0x30))))) == 0) goto loc_00BBD620;
    result = InbvPortPollOnly((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x2AAF6A) + 0x38)), Arg4, v_rip + 5407, Arg4);
    goto loc_00BBD622;
loc_00BBD620:
loc_00BBD622:
    *(uint8_t *)(Arg4) = 0;
    goto loc_00BBD96B;
loc_00BBD62A:
    if (Arg2 == 0) goto loc_00BBD966;
    if (Arg3 != 8) goto loc_00BBD966;
loc_00BBD64B:
    v_stack_mB8 = (uint32_t)((uint32_t)(*(uint32_t *)(Arg2)));
    result = sprintf_s(v_stack_m98, 80, v_rip + 4969, (uint32_t)(*(uint32_t *)(Arg2 + 0x4)));
    goto loc_00BBD690;
loc_00BBD665:
    goto loc_00BBD690;
loc_00BBD66E:
    goto loc_00BBD690;
loc_00BBD677:
    goto loc_00BBD690;
loc_00BBD680:
    goto loc_00BBD690;
loc_00BBD689:
loc_00BBD690:
    result = HdlspSendStringAtBaud(v_rip + 7328, 80, v_rip + 4969, (uint32_t)(*(uint32_t *)(Arg2 + 0x4)));
    goto loc_00BBD96B;
loc_00BBD69A:
    if (Arg4 == 0) goto loc_00BBD966;
    if (Arg5 == 0) goto loc_00BBD966;
    if ((*(uint64_t *)(Arg5)) < 2) goto loc_00BBD966;
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x2AAEB7) + 0x30))))) == 0) goto loc_00BBD620;
    Arg2 = (*(uint64_t *)(Arg5)) - 1;
    result = HdlspGetLine(Arg4 + 1, Arg2, v_rip + 4969, (uint32_t)(*(uint32_t *)(Arg2 + 0x4)));
    goto loc_00BBD622;
loc_00BBD6E3:
    if (((uint32_t)(local_rsi)) > 19) goto loc_00BBD709;
    if (((uint32_t)(local_rsi)) != 19) goto loc_00BBD867;
    if (Arg2 == 0) goto loc_00BBD85D;
    result = HdlspSetBlueScreenInformation(Arg2, Arg3, v_rip + 4969, (uint32_t)(*(uint32_t *)(Arg2 + 0x4)));
loc_00BBD702:
    goto loc_00BBD96B;
loc_00BBD709:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_rsi))) - (20));
    if (condition_is_equal) goto loc_00BBD823;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00BBD7F1;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00BBD798;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00BBD76A;
    if (Arg1 != 1) goto loc_00BBD88A;
    if (Arg4 == 0) goto loc_00BBD966;
    if (Arg5 == 0) goto loc_00BBD966;
    if ((*(uint64_t *)(Arg5)) < 12) goto loc_00BBD966;
    *(uint64_t *)(Arg4) = v_xmm0;
    *(uint32_t *)(Arg4 + 0x8) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x2AAE24) + 0x7E)));
    goto loc_00BBD96B;
loc_00BBD76A:
    if (Arg2 == 0) goto loc_00BBD966;
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x2AADFE) + 0x30))))) == 0) goto loc_00BBD96B;
    result = HdlspPutWideString(Arg2, Arg3, v_rip + 4969, (uint32_t)(*(uint32_t *)(Arg2 + 0x4)));
    goto loc_00BBD96B;
loc_00BBD798:
    if (Arg2 == 0) goto loc_00BBD966;
    if (Arg3 == 0) goto loc_00BBD966;
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x2AADC7) + 0x30))))) == 0) goto loc_00BBD96B;
    if (Arg3 == 0) goto loc_00BBD96B;
loc_00BBD7D0:
    result = InbvPortPutByte((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x2AADA1) + 0x38)), *(uint8_t *)((uint32_t)((uint32_t)(result)) + Arg2 * 1), v_rip + 4969, (uint32_t)(*(uint32_t *)(Arg2 + 0x4)));
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))))) + (1));
    if (((uint32_t)((uint32_t)(local_rsi))) < Arg3) goto loc_00BBD7D0;
    goto loc_00BBD96B;
loc_00BBD7F1:
    if (Arg4 == 0) goto loc_00BBD966;
    if (Arg5 == 0) goto loc_00BBD966;
    if ((*(uint64_t *)(Arg5)) < 16) goto loc_00BBD966;
    *(uint64_t *)(Arg4) = v_xmm0;
    goto loc_00BBD96B;
loc_00BBD823:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x2AAD4E) + 0x30))) & (3));
    if (((uint8_t)(Arg1)) != 3) goto loc_00BBD9A6;
    if (Arg2 == 0) goto loc_00BBD85D;
    if (Arg3 != 4) goto loc_00BBD85D;
    result = HdlspSendBlueScreenInfo((uint32_t)(*(uint32_t *)(Arg2)), *(uint8_t *)((uint32_t)((uint32_t)(result)) + Arg2 * 1), v_rip + 4969, (uint32_t)(*(uint32_t *)(Arg2 + 0x4)));
    result = HdlspSendStringAtBaud(v_rip + 4349, *(uint8_t *)((uint32_t)((uint32_t)(result)) + Arg2 * 1), v_rip + 4969, (uint32_t)(*(uint32_t *)(Arg2 + 0x4)));
    goto loc_00BBD9A6;
loc_00BBD85D:
    goto loc_00BBD9A8;
loc_00BBD867:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_rsi))) - (14));
    if (condition_is_equal) goto loc_00BBD993;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00BBD978;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00BBD8F8;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00BBD8DC;
    if (Arg1 == 1) goto loc_00BBD8B8;
loc_00BBD88A:
    if (((uint32_t)(local_rsi)) == 17) goto loc_00BBD9A6;
    if (((uint32_t)(local_rsi)) == 14) goto loc_00BBD9A6;
    if (((uint32_t)(local_rsi)) == 20) goto loc_00BBD9A6;
    if (((uint32_t)(local_rsi)) == 15) goto loc_00BBD9A6;
    goto loc_00BBD96B;
loc_00BBD8B8:
    if (Arg2 == 0) goto loc_00BBD966;
    if (Arg3 != 1) goto loc_00BBD966;
    result = HdlspProcessDumpCommand(*(uint8_t *)(Arg2), *(uint8_t *)((uint32_t)((uint32_t)(result)) + Arg2 * 1), v_rip + 4969, (uint32_t)(*(uint32_t *)(Arg2 + 0x4)));
    goto loc_00BBD96B;
loc_00BBD8DC:
    if (Arg2 != 0) goto loc_00BBD8EB;
    goto loc_00BBD9A6;
loc_00BBD8EB:
    result = HdlspAddLogEntry(Arg2, *(uint8_t *)((uint32_t)((uint32_t)(result)) + Arg2 * 1), v_rip + 4969, (uint32_t)(*(uint32_t *)(Arg2 + 0x4)));
    goto loc_00BBD9A6;
loc_00BBD8F8:
    if (Arg4 == 0) goto loc_00BBD966;
    if (Arg5 == 0) goto loc_00BBD966;
    if ((*(uint64_t *)(Arg5)) < 32) goto loc_00BBD966;
    *(uint32_t *)(Arg4) = 1;
    *(uint8_t *)(Arg4 + 0x8) = 1;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x2AAC68) + 0x30))) >> (3));
    result = (uint8_t)((result) & (1));
    *(uint8_t *)(Arg4 + 0x9) = (uint8_t)(result);
    *(uint32_t *)(Arg4 + 0x18) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x2AAC68) + 0x34)));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x2AAC68) + 0x30))))) >> (9));
    result = (uint32_t)((result) & (7));
    if (((uint32_t)(result)) >= 1) goto loc_00BBD951;
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x2AAC68) + 0x30))) >> (3));
    if (((1) & ((uint8_t)(Arg2))) != 0) goto loc_00BBD951;
    *(uint32_t *)(Arg4 + 0xC) = (uint32_t)((uint32_t)(0xC000000DULL));
    *(uint64_t *)(Arg4 + 0x10) = (uint32_t)(0xC000000DULL);
    goto loc_00BBD95D;
loc_00BBD951:
    *(uint32_t *)(Arg4 + 0xC) = (uint32_t)(result);
    *(uint64_t *)(Arg4 + 0x10) = *(uint64_t *)(*(uint64_t *)(v_rip + 0x2AAC68) + 0x40);
loc_00BBD95D:
    *(uint8_t *)(Arg4 + 0x1C) = (uint8_t)(*(uint8_t *)(*(uint64_t *)(v_rip + 0x2AAC68) + 0x54));
    goto loc_00BBD96B;
loc_00BBD966:
loc_00BBD96B:
    goto loc_00BBD9A6;
loc_00BBD978:
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x2AABF9) + 0x30))))) == 0) goto loc_00BBD9A6;
    result = HdlspBugCheckProcessing((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x2AABF9) + 0x30)), Arg2, v_rip + 4969, (uint32_t)(*(uint32_t *)(Arg2 + 0x4)));
    goto loc_00BBD9A6;
loc_00BBD993:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x2AABDE) + 0x30))) | (2));
    result = (uint32_t)((result) & (0xFFFFFFBFULL));
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x2AABDE) + 0x30) = (uint32_t)(result);
loc_00BBD9A6:
loc_00BBD9A8:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, v_rip + 4969, (uint32_t)(*(uint32_t *)(Arg2 + 0x4)));
    local_rsp = (local_rsp) + (160);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagehdls&rva=0x00BBD320&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
