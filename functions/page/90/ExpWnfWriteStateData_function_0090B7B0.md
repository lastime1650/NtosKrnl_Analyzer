# ExpWnfWriteStateData

- RVA: `0x0090B7B0`–`0x0090BD1C` (길이 `1,388` bytes)
- VA: `0x000000014090B7B0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000891A0`
- 디코드: `325`개 명령, `1,388/1,388` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **24**; 고유 호출 대상: **15**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x0090B868` → [RtlLargeIntegerToChar](RtlLargeIntegerToChar_function_0090BD30.md) (function, `0x0090BD30`)
- `0x0090B8BB` → [RtlAnsiStringToUnicodeString](RtlAnsiStringToUnicodeString_function_0090BEA0.md) (function, `0x0090BEA0`)
- `0x0090B928` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0090B944` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x0090B9C9` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0090BA07` → [ExpWnfAcquirePermanentDataStoreHandle](../A7/ExpWnfAcquirePermanentDataStoreHandle_function_00A7A210.md) (function, `0x00A7A210`)
- `0x0090BA34` → [ZwSetValueKey](../../text/6A/ZwSetValueKey_function_006ADCD0.md) (function, `0x006ADCD0`)
- `0x0090BA52` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x0090BA5B` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0090BAA6` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0090BAD7` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x0090BB32` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0090BB9F` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0090BBB2` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x0090BBF4` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0090BC2A` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0090BC46` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x0090BC76` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x0090BC8F` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0090BCC7` → [KiStackAttachProcess](../../text/21/KiStackAttachProcess_function_00216820.md) (function, `0x00216820`)
- `0x0090BCE1` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0090BCEF` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x0090BD03` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (function, `0x00217D30`)
- `0x0090BD12` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [ExpNtUpdateWnfStateData](ExpNtUpdateWnfStateData_function_0090A7A0.md) at `0x0090AE41`

### Static image references
- `0x0090B7C3` → RVA `0x00E0A740` (`.data`; read)
- `0x0090BB50` → RVA `0x00FC6AB0` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **21**
  - `0x0090B928` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x0090B944` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x0090B9C9` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0090BA34` → [ZwSetValueKey](../../text/6A/ZwSetValueKey_function_006ADCD0.md) (`PAGE` → `.text`)
  - `0x0090BA52` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x0090BA5B` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0090BAA6` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0090BAD7` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x0090BB32` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0090BB9F` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0090BBB2` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x0090BBF4` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0090BC2A` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x0090BC46` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x0090BC76` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x0090BC8F` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0090BCC7` → [KiStackAttachProcess](../../text/21/KiStackAttachProcess_function_00216820.md) (`PAGE` → `.text`)
  - `0x0090BCE1` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0090BCEF` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x0090BD03` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (`PAGE` → `.text`)
  - `0x0090BD12` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0090B7B0  40 53                           push rbx
0090B7B2  56                              push rsi
0090B7B3  57                              push rdi
0090B7B4  41 54                           push r12
0090B7B6  41 55                           push r13
0090B7B8  41 56                           push r14
0090B7BA  41 57                           push r15
0090B7BC  48 81 EC 40 01 00 00            sub rsp, 0x140
0090B7C3  48 8B 05 76 EF 4F 00            mov rax, qword ptr [rip + 0x4fef76]
0090B7CA  48 33 C4                        xor rax, rsp
0090B7CD  48 89 84 24 38 01 00 00         mov qword ptr [rsp + 0x138], rax
0090B7D5  45 8B E1                        mov r12d, r9d
0090B7D8  45 8B E8                        mov r13d, r8d
0090B7DB  48 89 54 24 48                  mov qword ptr [rsp + 0x48], rdx
0090B7E0  48 8B F1                        mov rsi, rcx
0090B7E3  48 89 4C 24 78                  mov qword ptr [rsp + 0x78], rcx
0090B7E8  0F 57 C0                        xorps xmm0, xmm0
0090B7EB  0F 11 84 24 88 00 00 00         movups xmmword ptr [rsp + 0x88], xmm0
0090B7F3  0F 11 84 24 98 00 00 00         movups xmmword ptr [rsp + 0x98], xmm0
0090B7FB  0F 11 84 24 A8 00 00 00         movups xmmword ptr [rsp + 0xa8], xmm0
0090B803  33 FF                           xor edi, edi
0090B805  89 7C 24 34                     mov dword ptr [rsp + 0x34], edi
0090B809  0F 11 44 24 50                  movups xmmword ptr [rsp + 0x50], xmm0
0090B80E  B8 22 00 00 00                  mov eax, 0x22
0090B813  66 89 44 24 52                  mov word ptr [rsp + 0x52], ax
0090B818  48 8D 84 24 10 01 00 00         lea rax, [rsp + 0x110]
0090B820  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
0090B825  48 39 79 68                     cmp qword ptr [rcx + 0x68], rdi
0090B829  0F 84 91 03 00 00               je 0x14090bbc0
0090B82F  48 8B 41 28                     mov rax, qword ptr [rcx + 0x28]
0090B833  48 B9 74 00 BC A3 6D 4E C6 41   movabs rcx, 0x41c64e6da3bc0074
0090B83D  48 33 C1                        xor rax, rcx
0090B840  0F 11 44 24 60                  movups xmmword ptr [rsp + 0x60], xmm0
0090B845  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
0090B84A  4C 8D 8C 24 C0 00 00 00         lea r9, [rsp + 0xc0]
0090B852  BB 41 00 00 00                  mov ebx, 0x41
0090B857  44 8B C3                        mov r8d, ebx
0090B85A  41 BF 10 00 00 00               mov r15d, 0x10
0090B860  41 8B D7                        mov edx, r15d
0090B863  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
0090B868  E8 C3 04 00 00                  call 0x14090bd30
0090B86D  85 C0                           test eax, eax
0090B86F  0F 88 2C 04 00 00               js 0x14090bca1
0090B875  48 8D 84 24 C0 00 00 00         lea rax, [rsp + 0xc0]
0090B87D  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
0090B882  66 89 5C 24 62                  mov word ptr [rsp + 0x62], bx
0090B887  48 8D 8C 24 C0 00 00 00         lea rcx, [rsp + 0xc0]
0090B88F  48 C7 C3 FF FF FF FF            mov rbx, 0xffffffffffffffff
0090B896  48 8B C3                        mov rax, rbx
0090B899  0F 1F 80 00 00 00 00            nop dword ptr [rax]
0090B8A0  48 FF C0                        inc rax
0090B8A3  40 38 3C 01                     cmp byte ptr [rcx + rax], dil
0090B8A7  75 F7                           jne 0x14090b8a0
0090B8A9  66 89 44 24 60                  mov word ptr [rsp + 0x60], ax
0090B8AE  45 33 C0                        xor r8d, r8d
0090B8B1  48 8D 54 24 60                  lea rdx, [rsp + 0x60]
0090B8B6  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
0090B8BB  E8 E0 05 00 00                  call 0x14090bea0
0090B8C0  0F B7 44 24 50                  movzx eax, word ptr [rsp + 0x50]
0090B8C5  D1 E8                           shr eax, 1
0090B8C7  45 8B DF                        mov r11d, r15d
0090B8CA  44 2B D8                        sub r11d, eax
0090B8CD  B9 20 00 00 00                  mov ecx, 0x20
0090B8D2  66 89 4C 24 50                  mov word ptr [rsp + 0x50], cx
0090B8D7  85 C0                           test eax, eax
0090B8D9  74 31                           je 0x14090b90c
0090B8DB  45 8B D7                        mov r10d, r15d
0090B8DE  44 8B C8                        mov r9d, eax
0090B8E1  4D 03 C9                        add r9, r9
0090B8E4  0F 1F 40 00                     nop dword ptr [rax]
0090B8E8  0F 1F 84 00 00 00 00 00         nop dword ptr [rax + rax]
0090B8F0  4D 8D 49 FE                     lea r9, [r9 - 2]
0090B8F4  45 8D 52 FF                     lea r10d, [r10 - 1]
0090B8F8  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
0090B8FD  41 0F B7 0C 11                  movzx ecx, word ptr [r9 + rdx]
0090B902  66 42 89 0C 52                  mov word ptr [rdx + r10*2], cx
0090B907  83 C0 FF                        add eax, -1
0090B90A  75 E4                           jne 0x14090b8f0
0090B90C  45 85 DB                        test r11d, r11d
0090B90F  0F 85 DB 01 00 00               jne 0x14090baf0
0090B915  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
0090B91A  48 89 7C 24 40                  mov qword ptr [rsp + 0x40], rdi
0090B91F  45 33 C0                        xor r8d, r8d
0090B922  33 D2                           xor edx, edx
0090B924  48 8D 4E 50                     lea rcx, [rsi + 0x50]
0090B928  E8 03 49 90 FF                  call 0x140210230
0090B92D  4C 8B F0                        mov r14, rax
0090B930  F0 48 0F BA 6E 50 00            lock bts qword ptr [rsi + 0x50], 0
0090B937  73 10                           jae 0x14090b949
0090B939  4C 8D 46 50                     lea r8, [rsi + 0x50]
0090B93D  48 8B D0                        mov rdx, rax
0090B940  48 8D 4E 50                     lea rcx, [rsi + 0x50]
0090B944  E8 47 43 90 FF                  call 0x14020fc90
0090B949  4D 85 F6                        test r14, r14
0090B94C  74 05                           je 0x14090b953
0090B94E  41 C6 46 0A 01                  mov byte ptr [r14 + 0xa], 1
0090B953  39 BC 24 A0 01 00 00            cmp dword ptr [rsp + 0x1a0], edi
0090B95A  0F 85 13 02 00 00               jne 0x14090bb73
0090B960  48 8B 46 58                     mov rax, qword ptr [rsi + 0x58]
0090B964  45 33 E4                        xor r12d, r12d
0090B967  41 8B CC                        mov ecx, r12d
0090B96A  48 83 F8 01                     cmp rax, 1
0090B96E  48 0F 45 C8                     cmovne rcx, rax
0090B972  48 85 C9                        test rcx, rcx
0090B975  74 32                           je 0x14090b9a9
0090B977  4C 8B F1                        mov r14, rcx
0090B97A  48 85 C9                        test rcx, rcx
0090B97D  0F 85 8E 01 00 00               jne 0x14090bb11
0090B983  8B 7E 60                        mov edi, dword ptr [rsi + 0x60]
0090B986  FF C7                           inc edi
0090B988  89 7C 24 30                     mov dword ptr [rsp + 0x30], edi
0090B98C  85 FF                           test edi, edi
0090B98E  0F 84 EE 00 00 00               je 0x14090ba82
0090B994  4D 85 F6                        test r14, r14
0090B997  75 24                           jne 0x14090b9bd
0090B999  48 C7 46 58 01 00 00 00         mov qword ptr [rsi + 0x58], 1
0090B9A1  87 7E 60                        xchg dword ptr [rsi + 0x60], edi
0090B9A4  E9 E7 00 00 00                  jmp 0x14090ba90
0090B9A9  48 39 7E 68                     cmp qword ptr [rsi + 0x68], rdi
0090B9AD  0F 85 68 01 00 00               jne 0x14090bb1b
0090B9B3  45 85 ED                        test r13d, r13d
0090B9B6  74 BF                           je 0x14090b977
0090B9B8  E9 5E 01 00 00                  jmp 0x14090bb1b
0090B9BD  4D 8B C5                        mov r8, r13
0090B9C0  49 8D 4E 10                     lea rcx, [r14 + 0x10]
0090B9C4  48 8B 54 24 48                  mov rdx, qword ptr [rsp + 0x48]
0090B9C9  E8 72 AE DB FF                  call 0x1406c6840
0090B9CE  45 89 6E 08                     mov dword ptr [r14 + 8], r13d
0090B9D2  4D 8D 7E 0C                     lea r15, [r14 + 0xc]
0090B9D6  41 89 3F                        mov dword ptr [r15], edi
0090B9D9  48 8B 4E 68                     mov rcx, qword ptr [rsi + 0x68]
0090B9DD  48 85 C9                        test rcx, rcx
0090B9E0  75 1B                           jne 0x14090b9fd
0090B9E2  4C 3B 74 24 38                  cmp r14, qword ptr [rsp + 0x38]
0090B9E7  75 B8                           jne 0x14090b9a1
0090B9E9  48 8B 46 58                     mov rax, qword ptr [rsi + 0x58]
0090B9ED  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
0090B9F2  4C 89 76 58                     mov qword ptr [rsi + 0x58], r14
0090B9F6  4C 89 64 24 38                  mov qword ptr [rsp + 0x38], r12
0090B9FB  EB A4                           jmp 0x14090b9a1
0090B9FD  4C 89 64 24 48                  mov qword ptr [rsp + 0x48], r12
0090BA02  48 8D 54 24 48                  lea rdx, [rsp + 0x48]
0090BA07  E8 04 E8 16 00                  call 0x140a7a210
0090BA0C  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
0090BA10  85 C0                           test eax, eax
0090BA12  78 5C                           js 0x14090ba70
0090BA14  41 8D 45 04                     lea eax, [r13 + 4]
0090BA18  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
0090BA1C  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
0090BA21  41 B9 03 00 00 00               mov r9d, 3
0090BA27  45 33 C0                        xor r8d, r8d
0090BA2A  48 8D 54 24 50                  lea rdx, [rsp + 0x50]
0090BA2F  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
0090BA34  E8 97 22 DA FF                  call 0x1406adcd0
0090BA39  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
0090BA3D  48 8B 7E 68                     mov rdi, qword ptr [rsi + 0x68]
0090BA41  B8 11 00 00 00                  mov eax, 0x11
0090BA46  F0 4C 0F B1 67 08               lock cmpxchg qword ptr [rdi + 8], r12
0090BA4C  74 09                           je 0x14090ba57
0090BA4E  48 8D 4F 08                     lea rcx, [rdi + 8]
0090BA52  E8 E9 79 95 FF                  call 0x140263440
0090BA57  48 8D 4F 08                     lea rcx, [rdi + 8]
0090BA5B  E8 A0 5B 9D FF                  call 0x1402e1600
0090BA60  8B 44 24 34                     mov eax, dword ptr [rsp + 0x34]
0090BA64  8B 7C 24 30                     mov edi, dword ptr [rsp + 0x30]
0090BA68  85 C0                           test eax, eax
0090BA6A  0F 89 72 FF FF FF               jns 0x14090b9e2
0090BA70  48 8B 46 58                     mov rax, qword ptr [rsi + 0x58]
0090BA74  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
0090BA79  4C 89 66 58                     mov qword ptr [rsi + 0x58], r12
0090BA7D  E9 22 FF FF FF                  jmp 0x14090b9a4
0090BA82  BF 01 00 00 00                  mov edi, 1
0090BA87  89 7C 24 30                     mov dword ptr [rsp + 0x30], edi
0090BA8B  E9 FC FE FF FF                  jmp 0x14090b98c
0090BA90  F0 48 0F C1 5E 50               lock xadd qword ptr [rsi + 0x50], rbx
0090BA96  80 E3 06                        and bl, 6
0090BA99  80 FB 02                        cmp bl, 2
0090BA9C  0F 84 0C 01 00 00               je 0x14090bbae
0090BAA2  48 8D 4E 50                     lea rcx, [rsi + 0x50]
0090BAA6  E8 55 5B 9D FF                  call 0x1402e1600
0090BAAB  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
0090BAB0  48 83 F9 02                     cmp rcx, 2
0090BAB4  0F 83 22 02 00 00               jae 0x14090bcdc
0090BABA  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
0090BABF  48 85 C9                        test rcx, rcx
0090BAC2  0F 85 45 02 00 00               jne 0x14090bd0d
0090BAC8  8B 44 24 34                     mov eax, dword ptr [rsp + 0x34]
0090BACC  48 8B 8C 24 38 01 00 00         mov rcx, qword ptr [rsp + 0x138]
0090BAD4  48 33 CC                        xor rcx, rsp
0090BAD7  E8 64 0B DA FF                  call 0x1406ac640
0090BADC  48 81 C4 40 01 00 00            add rsp, 0x140
0090BAE3  41 5F                           pop r15
0090BAE5  41 5E                           pop r14
0090BAE7  41 5D                           pop r13
0090BAE9  41 5C                           pop r12
0090BAEB  5F                              pop rdi
0090BAEC  5E                              pop rsi
0090BAED  5B                              pop rbx
0090BAEE  C3                              ret
0090BAEF  CC                              int3
0090BAF0  41 8B CB                        mov ecx, r11d
0090BAF3  48 03 C9                        add rcx, rcx
0090BAF6  48 8D 49 FE                     lea rcx, [rcx - 2]
0090BAFA  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
0090BAFF  66 C7 04 01 30 00               mov word ptr [rcx + rax], 0x30
0090BB05  41 83 C3 FF                     add r11d, -1
0090BB09  0F 84 06 FE FF FF               je 0x14090b915
0090BB0F  EB E5                           jmp 0x14090baf6
0090BB11  44 39 69 04                     cmp dword ptr [rcx + 4], r13d
0090BB15  0F 83 68 FE FF FF               jae 0x14090b983
0090BB1B  48 8B C3                        mov rax, rbx
0090BB1E  F0 48 0F C1 46 50               lock xadd qword ptr [rsi + 0x50], rax
0090BB24  24 06                           and al, 6
0090BB26  3C 02                           cmp al, 2
0090BB28  0F 84 44 01 00 00               je 0x14090bc72
0090BB2E  48 8D 4E 50                     lea rcx, [rsi + 0x50]
0090BB32  E8 C9 5A 9D FF                  call 0x1402e1600
0090BB37  8B 46 28                        mov eax, dword ptr [rsi + 0x28]
0090BB3A  48 C1 E8 04                     shr rax, 4
0090BB3E  83 E0 03                        and eax, 3
0090BB41  3C 03                           cmp al, 3
0090BB43  0F 85 37 01 00 00               jne 0x14090bc80
0090BB49  48 8B 86 98 00 00 00            mov rax, qword ptr [rsi + 0x98]
0090BB50  48 39 05 59 AF 6B 00            cmp qword ptr [rip + 0x6baf59], rax
0090BB57  0F 84 23 01 00 00               je 0x14090bc80
0090BB5D  48 8B 8E 98 00 00 00            mov rcx, qword ptr [rsi + 0x98]
0090BB64  48 85 C9                        test rcx, rcx
0090BB67  75 63                           jne 0x14090bbcc
0090BB69  B8 34 00 00 C0                  mov eax, 0xc0000034
0090BB6E  E9 59 FF FF FF                  jmp 0x14090bacc
0090BB73  48 39 7E 58                     cmp qword ptr [rsi + 0x58], rdi
0090BB77  74 43                           je 0x14090bbbc
0090BB79  8B 46 60                        mov eax, dword ptr [rsi + 0x60]
0090BB7C  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
0090BB80  41 3B C4                        cmp eax, r12d
0090BB83  0F 84 D7 FD FF FF               je 0x14090b960
0090BB89  F0 48 0F C1 5E 50               lock xadd qword ptr [rsi + 0x50], rbx
0090BB8F  80 E3 06                        and bl, 6
0090BB92  80 FB 02                        cmp bl, 2
0090BB95  0F 84 50 01 00 00               je 0x14090bceb
0090BB9B  48 8D 4E 50                     lea rcx, [rsi + 0x50]
0090BB9F  E8 5C 5A 9D FF                  call 0x1402e1600
0090BBA4  B8 01 00 00 C0                  mov eax, 0xc0000001
0090BBA9  E9 1E FF FF FF                  jmp 0x14090bacc
0090BBAE  48 8D 4E 50                     lea rcx, [rsi + 0x50]
0090BBB2  E8 19 A2 95 FF                  call 0x140265dd0
0090BBB7  E9 E6 FE FF FF                  jmp 0x14090baa2
0090BBBC  33 C0                           xor eax, eax
0090BBBE  EB BC                           jmp 0x14090bb7c
0090BBC0  48 C7 C3 FF FF FF FF            mov rbx, 0xffffffffffffffff
0090BBC7  E9 49 FD FF FF                  jmp 0x14090b915
0090BBCC  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0090BBD5  48 3B 88 B8 00 00 00            cmp rcx, qword ptr [rax + 0xb8]
0090BBDC  0F 85 D5 00 00 00               jne 0x14090bcb7
0090BBE2  45 8B F4                        mov r14d, r12d
0090BBE5  41 8D 55 10                     lea edx, [r13 + 0x10]
0090BBE9  B9 01 01 00 00                  mov ecx, 0x101
0090BBEE  41 B8 57 6E 66 20               mov r8d, 0x20666e57
0090BBF4  E8 F7 64 27 00                  call 0x140b820f0
0090BBF9  48 8B F8                        mov rdi, rax
0090BBFC  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0090BC01  45 85 F6                        test r14d, r14d
0090BC04  0F 85 EF 00 00 00               jne 0x14090bcf9
0090BC0A  48 85 FF                        test rdi, rdi
0090BC0D  0F 84 9A 00 00 00               je 0x14090bcad
0090BC13  4C 89 67 08                     mov qword ptr [rdi + 8], r12
0090BC17  C7 07 04 09 10 00               mov dword ptr [rdi], 0x100904
0090BC1D  44 89 6F 04                     mov dword ptr [rdi + 4], r13d
0090BC21  45 33 C0                        xor r8d, r8d
0090BC24  33 D2                           xor edx, edx
0090BC26  48 8D 4E 50                     lea rcx, [rsi + 0x50]
0090BC2A  E8 01 46 90 FF                  call 0x140210230
0090BC2F  48 8B F8                        mov rdi, rax
0090BC32  F0 48 0F BA 6E 50 00            lock bts qword ptr [rsi + 0x50], 0
0090BC39  73 10                           jae 0x14090bc4b
0090BC3B  4C 8D 46 50                     lea r8, [rsi + 0x50]
0090BC3F  48 8B D0                        mov rdx, rax
0090BC42  48 8D 4E 50                     lea rcx, [rsi + 0x50]
0090BC46  E8 45 40 90 FF                  call 0x14020fc90
0090BC4B  48 85 FF                        test rdi, rdi
0090BC4E  74 04                           je 0x14090bc54
0090BC50  C6 47 0A 01                     mov byte ptr [rdi + 0xa], 1
0090BC54  48 8B 46 58                     mov rax, qword ptr [rsi + 0x58]
0090BC58  4D 8B F4                        mov r14, r12
0090BC5B  48 83 F8 01                     cmp rax, 1
0090BC5F  4C 0F 45 F0                     cmovne r14, rax
0090BC63  4D 85 F6                        test r14, r14
0090BC66  75 69                           jne 0x14090bcd1
0090BC68  4C 8B 74 24 38                  mov r14, qword ptr [rsp + 0x38]
0090BC6D  E9 11 FD FF FF                  jmp 0x14090b983
0090BC72  48 8D 4E 50                     lea rcx, [rsi + 0x50]
0090BC76  E8 55 A1 95 FF                  call 0x140265dd0
0090BC7B  E9 AE FE FF FF                  jmp 0x14090bb2e
0090BC80  41 8D 55 10                     lea edx, [r13 + 0x10]
0090BC84  B9 00 01 00 00                  mov ecx, 0x100
0090BC89  41 B8 57 6E 66 20               mov r8d, 0x20666e57
0090BC8F  E8 5C 64 27 00                  call 0x140b820f0
0090BC94  48 8B F8                        mov rdi, rax
0090BC97  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0090BC9C  E9 69 FF FF FF                  jmp 0x14090bc0a
0090BCA1  48 C7 C3 FF FF FF FF            mov rbx, 0xffffffffffffffff
0090BCA8  E9 13 FC FF FF                  jmp 0x14090b8c0
0090BCAD  B8 9A 00 00 C0                  mov eax, 0xc000009a
0090BCB2  E9 15 FE FF FF                  jmp 0x14090bacc
0090BCB7  41 BE 01 00 00 00               mov r14d, 1
0090BCBD  4C 8D 84 24 88 00 00 00         lea r8, [rsp + 0x88]
0090BCC5  33 D2                           xor edx, edx
0090BCC7  E8 54 AB 90 FF                  call 0x140216820
0090BCCC  E9 14 FF FF FF                  jmp 0x14090bbe5
0090BCD1  45 39 6E 04                     cmp dword ptr [r14 + 4], r13d
0090BCD5  72 91                           jb 0x14090bc68
0090BCD7  E9 A7 FC FF FF                  jmp 0x14090b983
0090BCDC  BA 57 6E 66 20                  mov edx, 0x20666e57
0090BCE1  E8 8A 6B 27 00                  call 0x140b82870
0090BCE6  E9 CF FD FF FF                  jmp 0x14090baba
0090BCEB  48 8D 4E 50                     lea rcx, [rsi + 0x50]
0090BCEF  E8 DC A0 95 FF                  call 0x140265dd0
0090BCF4  E9 A2 FE FF FF                  jmp 0x14090bb9b
0090BCF9  33 D2                           xor edx, edx
0090BCFB  48 8D 8C 24 88 00 00 00         lea rcx, [rsp + 0x88]
0090BD03  E8 28 C0 90 FF                  call 0x140217d30
0090BD08  E9 FD FE FF FF                  jmp 0x14090bc0a
0090BD0D  BA 57 6E 66 20                  mov edx, 0x20666e57
0090BD12  E8 59 6B 27 00                  call 0x140b82870
0090BD17  E9 AC FD FF FF                  jmp 0x14090bac8
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExpWnfWriteStateData(__int64 a1, __int64 a2, int a3, int a4, unsigned int a5)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int16 v_stack_m116;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int16 v_stack_m126;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned int v_stack_m144;
    unsigned int v_stack_m148;
    unsigned int v_stack_m150;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mF0;
    unsigned int v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p88;

    v_rsp = (v_rsp) - (320);
    result = (*(unsigned __int64 *)(v_rip + 5238646)) ^ (v_rsp);
    v_stack_m40 = result;
    v_stack_m130 = a2;
    v_stack_m100 = a1;
    v_stack_mF0 = v_xmm0;
    v_stack_mE0 = v_xmm0;
    v_stack_mD0 = v_xmm0;
    v_rdi = 0;
    v_stack_m144 = 0;
    v_stack_m128 = v_xmm0;
    v_stack_m126 = 34;
    v_stack_m120 = v_stack_m68;
    if ((*(unsigned __int64 *)(a1 + 104)) == 0) goto loc_0090BBC0;
    result = (*(unsigned __int64 *)(a1 + 40)) ^ (a1);
    v_stack_m118 = v_xmm0;
    v_stack_m108 = result;
    result = RtlLargeIntegerToChar(v_stack_m108, 16, 65, v_stack_mB8);
    if (sign_flag) goto loc_0090BCA1;
    v_stack_m110 = v_stack_mB8;
    v_stack_m116 = 65;
loc_0090B8A0:
    result = (-1) + 1;
    if ((*(unsigned __int8 *)(v_stack_mB8 + result * 1)) != 0) goto loc_0090B8A0;
    v_stack_m118 = (unsigned __int16)(result);
    a3 = 0;
    result = RtlAnsiStringToUnicodeString(v_stack_m128, v_stack_m118, a3, v_stack_mB8);
loc_0090B8C0:
    result = (unsigned int)((v_stack_m128) >> (1));
    v_r11 = (unsigned int)((16) - ((unsigned int)(result)));
    v_stack_m128 = 32;
    if ((unsigned int)(result) == 0) goto loc_0090B90C;
    a4 = ((unsigned int)((unsigned int)(result))) + ((unsigned int)((unsigned int)(result)));
loc_0090B8F0:
    *(unsigned __int16 *)(v_stack_m120 + 16 - 1 * 2) = (unsigned __int16)(*(unsigned __int16 *)(a4 - 2 + v_stack_m120 * 1));
    result = (unsigned int)((result) + (-1));
    if (condition_is_not_equal) goto loc_0090B8F0;
loc_0090B90C:
    if ((unsigned int)(v_r11) != 0) goto loc_0090BAF0;
loc_0090B915:
    v_stack_m140 = 0;
    v_stack_m138 = 0;
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(a1 + 80, a2, a3, a4 - 2);
    if (!(condition_is_above_or_equal)) {
        a3 = a1 + 80;
        a2 = result;
        a1 = a1 + 80;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4 - 2);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    if (a5 != 0) goto loc_0090BB73;
loc_0090B960:
    v_r12 = 0;
    a1 = 0;
    if ((*(unsigned __int64 *)(a1 + 88)) != 1) { a1 = *(unsigned __int64 *)(a1 + 88); }
    if (a1 == 0) goto loc_0090B9A9;
loc_0090B977:
    if (a1 != 0) goto loc_0090BB11;
loc_0090B983:
    v_rdi = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 96))) + 1);
    v_stack_m148 = (unsigned int)(v_rdi);
loc_0090B98C:
    if ((unsigned int)(v_rdi) == 0) goto loc_0090BA82;
    if (a1 != 0) goto loc_0090B9BD;
    *(unsigned __int64 *)(a1 + 88) = 1;
loc_0090B9A1:
loc_0090B9A4:
    goto loc_0090BA90;
loc_0090B9A9:
    if ((*(unsigned __int64 *)(a1 + 104)) != v_rdi) goto loc_0090BB1B;
    if ((unsigned int)((unsigned int)(a3)) == 0) goto loc_0090B977;
    goto loc_0090BB1B;
loc_0090B9BD:
    result = memcpy(a1 + 16, v_stack_m130, (unsigned int)(a3), a4 - 2);
    *(unsigned int *)(a1 + 8) = (unsigned int)((unsigned int)(a3));
    *(unsigned int *)(a1 + 12) = (unsigned int)(v_rdi);
    if (*(unsigned __int64 *)(a1 + 104) != 0) goto loc_0090B9FD;
loc_0090B9E2:
    if (a1 != v_stack_m140) goto loc_0090B9A1;
    v_stack_m138 = *(unsigned __int64 *)(a1 + 88);
    *(unsigned __int64 *)(a1 + 88) = a1;
    v_stack_m140 = 0;
    goto loc_0090B9A1;
loc_0090B9FD:
    v_stack_m130 = 0;
    result = ExpWnfAcquirePermanentDataStoreHandle(*(unsigned __int64 *)(a1 + 104), v_stack_m130, (unsigned int)(a3), a4 - 2);
    v_stack_m144 = (unsigned int)(result);
    if (sign_flag) goto loc_0090BA70;
    v_stack_m150 = (unsigned int)((unsigned int)(a3) + 4);
    v_stack_m158 = a1 + 12;
    a3 = 0;
    result = ZwSetValueKey(v_stack_m130, v_stack_m128, a3, 3);
    v_stack_m144 = (unsigned int)(result);
    result = 17;
    if (!(condition_is_equal)) {
        a1 = *(unsigned __int64 *)(a1 + 104) + 8;
        result = ExfReleasePushLockShared(a1, v_stack_m128, a3, 3);
    }
    result = KeAbPostRelease(*(unsigned __int64 *)(a1 + 104) + 8, v_stack_m128, a3, 3);
    if (!sign_flag) goto loc_0090B9E2;
loc_0090BA70:
    v_stack_m138 = *(unsigned __int64 *)(a1 + 88);
    *(unsigned __int64 *)(a1 + 88) = 0;
    goto loc_0090B9A4;
loc_0090BA82:
    v_stack_m148 = 1;
    goto loc_0090B98C;
loc_0090BA90:
    v_rbx = (unsigned __int8)((-1) & (6));
    if (((unsigned __int8)(v_rbx)) == 2) goto loc_0090BBAE;
loc_0090BAA2:
    result = KeAbPostRelease(a1 + 80, v_stack_m128, a3, 3);
    if (v_stack_m138 >= 2) goto loc_0090BCDC;
loc_0090BABA:
    if (v_stack_m140 != 0) goto loc_0090BD0D;
loc_0090BAC8:
loc_0090BACC:
    a1 = (v_stack_m40) ^ (v_rsp);
    result = _security_check_cookie(a1, v_stack_m128, a3, 3);
    v_rsp = (v_rsp) + (320);
    return result;
loc_0090BAF0:
    a1 = ((unsigned int)((unsigned int)(v_r11))) + ((unsigned int)((unsigned int)(v_r11)));
loc_0090BAF6:
    *(unsigned __int16 *)(a1 - 2 + v_stack_p58 * 1) = 48;
    v_r11 = (unsigned int)((v_r11) + (-1));
    if (condition_is_equal) goto loc_0090B915;
    goto loc_0090BAF6;
loc_0090BB11:
    if ((*(unsigned int *)(a1 - 2 + 4)) >= ((unsigned int)((unsigned int)(a3)))) goto loc_0090B983;
loc_0090BB1B:
    result = (unsigned __int8)((v_rbx) & (6));
    if (((unsigned __int8)(result)) == 2) goto loc_0090BC72;
loc_0090BB2E:
    result = KeAbPostRelease(a1 + 80, v_stack_m128, a3, 3);
    result = ((unsigned int)(*(unsigned int *)(a1 + 40))) >> (4);
    result = (unsigned int)((result) & (3));
    if (((unsigned __int8)(result)) != 3) goto loc_0090BC80;
    if ((*(unsigned __int64 *)(v_rip + 7057241)) == (*(unsigned __int64 *)(a1 + 152))) goto loc_0090BC80;
    if (*(unsigned __int64 *)(a1 + 152) != 0) goto loc_0090BBCC;
    goto loc_0090BACC;
loc_0090BB73:
    if ((*(unsigned __int64 *)(a1 + 88)) == 1) goto loc_0090BBBC;
loc_0090BB7C:
    v_stack_p30 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 96)));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 96)))) == 0) goto loc_0090B960;
    v_rbx = (unsigned __int8)((v_rbx) & (6));
    if (((unsigned __int8)(v_rbx)) == 2) goto loc_0090BCEB;
loc_0090BB9B:
    result = KeAbPostRelease(a1 + 80, v_stack_m128, a3, 3);
    goto loc_0090BACC;
loc_0090BBAE:
    result = ExfTryToWakePushLock(a1 + 80, v_stack_m128, a3, 3);
    goto loc_0090BAA2;
loc_0090BBBC:
    result = 0;
    goto loc_0090BB7C;
loc_0090BBC0:
    goto loc_0090B915;
loc_0090BBCC:
    if ((a1 + 80) != (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184))) goto loc_0090BCB7;
loc_0090BBE5:
    result = ExAllocatePool2(257, (unsigned int)(a3) + 16, (unsigned int)(0x20666E57ULL), 3);
    v_stack_p38 = result;
    if (0 != 0) goto loc_0090BCF9;
loc_0090BC0A:
    if (result == 0) goto loc_0090BCAD;
    *(unsigned __int64 *)(result + 8) = 0;
    *(unsigned int *)(result) = 0x100904ULL;
    *(unsigned int *)(result + 4) = (unsigned int)((unsigned int)(a3));
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(a1 + 80, a2, a3, 3);
    if (!(condition_is_above_or_equal)) {
        a3 = a1 + 80;
        a2 = result;
        a1 = a1 + 80;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, 3);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    v_r14 = 0;
    if ((*(unsigned __int64 *)(a1 + 88)) != 1) { v_r14 = *(unsigned __int64 *)(a1 + 88); }
    if (v_r14 != 0) goto loc_0090BCD1;
loc_0090BC68:
    goto loc_0090B983;
loc_0090BC72:
    result = ExfTryToWakePushLock(a1 + 80, a2, a3, 3);
    goto loc_0090BB2E;
loc_0090BC80:
    result = ExAllocatePool2(256, (unsigned int)(a3) + 16, (unsigned int)(0x20666E57ULL), 3);
    v_stack_p38 = result;
    goto loc_0090BC0A;
loc_0090BCA1:
    goto loc_0090B8C0;
loc_0090BCAD:
    goto loc_0090BACC;
loc_0090BCB7:
    a2 = 0;
    result = KiStackAttachProcess(256, a2, v_stack_p88, 3);
    goto loc_0090BBE5;
loc_0090BCD1:
    if ((*(unsigned int *)(1 + 4)) < ((unsigned int)((unsigned int)(a3)))) goto loc_0090BC68;
    goto loc_0090B983;
loc_0090BCDC:
    result = ExFreePoolWithTag(256, (unsigned int)(0x20666E57ULL), v_stack_p88, 3);
    goto loc_0090BABA;
loc_0090BCEB:
    result = ExfTryToWakePushLock(a1 + 80, (unsigned int)(0x20666E57ULL), v_stack_p88, 3);
    goto loc_0090BB9B;
loc_0090BCF9:
    a2 = 0;
    result = KiUnstackDetachProcess(v_stack_p88, a2, v_stack_p88, 3);
    goto loc_0090BC0A;
loc_0090BD0D:
    result = ExFreePoolWithTag(v_stack_p88, (unsigned int)(0x20666E57ULL), v_stack_p88, 3);
    goto loc_0090BAC8;
}
```

## 5. (Beta) C Style

```c
int64_t ExpWnfWriteStateData(void *Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4, uint32_t Arg5)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint64_t v_stack_m110;
    uint16_t v_stack_m116;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint16_t v_stack_m126;
    uint64_t v_stack_m128;
    uint64_t v_stack_m130;
    uint64_t v_stack_m138;
    uint64_t v_stack_m140;
    uint32_t v_stack_m144;
    uint32_t v_stack_m148;
    uint32_t v_stack_m150;
    uint64_t v_stack_m158;
    uint64_t v_stack_m40;
    uint64_t v_stack_m68;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mF0;
    uint32_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p58;
    uint64_t v_stack_p88;

    local_rsp = (local_rsp) - (320);
    result = (*(uint64_t *)(v_rip + 0x4FEF76)) ^ (local_rsp);
    v_stack_m40 = result;
    v_stack_m130 = Arg2;
    v_stack_m100 = Arg1;
    v_stack_mF0 = v_xmm0;
    v_stack_mE0 = v_xmm0;
    v_stack_mD0 = v_xmm0;
    local_rdi = 0;
    v_stack_m144 = 0;
    v_stack_m128 = v_xmm0;
    v_stack_m126 = 34;
    v_stack_m120 = v_stack_m68;
    if ((*(uint64_t *)(arg1 + 0x68)) == 0) goto loc_0090BBC0;
    result = (*(uint64_t *)(arg1 + 0x28)) ^ (Arg1);
    v_stack_m118 = v_xmm0;
    v_stack_m108 = result;
    result = RtlLargeIntegerToChar(v_stack_m108, 16, 65, v_stack_mB8);
    if (sign_flag) goto loc_0090BCA1;
    v_stack_m110 = v_stack_mB8;
    v_stack_m116 = 65;
loc_0090B8A0:
    result = (-1) + 1;
    if ((*(uint8_t *)(v_stack_mB8 + result * 1)) != 0) goto loc_0090B8A0;
    v_stack_m118 = (uint16_t)(result);
    Arg3 = 0;
    result = RtlAnsiStringToUnicodeString(v_stack_m128, v_stack_m118, Arg3, v_stack_mB8);
loc_0090B8C0:
    result = (uint32_t)((v_stack_m128) >> (1));
    local_r11 = (uint32_t)((16) - ((uint32_t)(result)));
    v_stack_m128 = 32;
    if ((uint32_t)(result) == 0) goto loc_0090B90C;
    Arg4 = ((uint32_t)((uint32_t)(result))) + ((uint32_t)((uint32_t)(result)));
loc_0090B8F0:
    *(uint16_t *)(v_stack_m120 + 0x10 - 0x1 * 2) = (uint16_t)(*(uint16_t *)(Arg4 - 0x2 + v_stack_m120 * 1));
    result = (uint32_t)((result) + (-1));
    if (condition_is_not_equal) goto loc_0090B8F0;
loc_0090B90C:
    if ((uint32_t)(local_r11) != 0) goto loc_0090BAF0;
loc_0090B915:
    v_stack_m140 = 0;
    v_stack_m138 = 0;
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(Arg1 + 80, Arg2, Arg3, Arg4 - 2);
    if (!(condition_is_above_or_equal)) {
        Arg3 = Arg1 + 80;
        Arg2 = result;
        Arg1 = Arg1 + 80;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, Arg4 - 2);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    if (Arg5 != 0) goto loc_0090BB73;
loc_0090B960:
    local_r12 = 0;
    Arg1 = 0;
    if ((*(uint64_t *)(arg1 + 0x58)) != 1) { Arg1 = *(uint64_t *)(arg1 + 0x58); }
    if (Arg1 == NULL) goto loc_0090B9A9;
loc_0090B977:
    if (Arg1 != NULL) goto loc_0090BB11;
loc_0090B983:
    local_rdi = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x60))) + 1);
    v_stack_m148 = (uint32_t)(local_rdi);
loc_0090B98C:
    if ((uint32_t)(local_rdi) == 0) goto loc_0090BA82;
    if (Arg1 != NULL) goto loc_0090B9BD;
    *(uint64_t *)(arg1 + 0x58) = 1;
loc_0090B9A1:
loc_0090B9A4:
    goto loc_0090BA90;
loc_0090B9A9:
    if ((*(uint64_t *)(arg1 + 0x68)) != local_rdi) goto loc_0090BB1B;
    if ((uint32_t)((uint32_t)(Arg3)) == 0) goto loc_0090B977;
    goto loc_0090BB1B;
loc_0090B9BD:
    result = memcpy(Arg1 + 16, v_stack_m130, (uint32_t)(Arg3), Arg4 - 2);
    *(uint32_t *)(arg1 + 0x8) = (uint32_t)((uint32_t)(Arg3));
    *(uint32_t *)(arg1 + 0xC) = (uint32_t)(local_rdi);
    if (*(uint64_t *)(arg1 + 0x68) != 0) goto loc_0090B9FD;
loc_0090B9E2:
    if (Arg1 != v_stack_m140) goto loc_0090B9A1;
    v_stack_m138 = *(uint64_t *)(arg1 + 0x58);
    *(void **)(arg1 + 0x58) = Arg1;
    v_stack_m140 = 0;
    goto loc_0090B9A1;
loc_0090B9FD:
    v_stack_m130 = 0;
    result = ExpWnfAcquirePermanentDataStoreHandle(*(uint64_t *)(arg1 + 0x68), v_stack_m130, (uint32_t)(Arg3), Arg4 - 2);
    v_stack_m144 = (uint32_t)(result);
    if (sign_flag) goto loc_0090BA70;
    v_stack_m150 = (uint32_t)((uint32_t)(Arg3) + 4);
    v_stack_m158 = Arg1 + 12;
    Arg3 = 0;
    result = ZwSetValueKey(v_stack_m130, v_stack_m128, Arg3, 3);
    v_stack_m144 = (uint32_t)(result);
    result = 17;
    if (!(condition_is_equal)) {
        Arg1 = *(uint64_t *)(arg1 + 0x68) + 8;
        result = ExfReleasePushLockShared(Arg1, v_stack_m128, Arg3, 3);
    }
    result = KeAbPostRelease(*(uint64_t *)(arg1 + 0x68) + 8, v_stack_m128, Arg3, 3);
    if (!sign_flag) goto loc_0090B9E2;
loc_0090BA70:
    v_stack_m138 = *(uint64_t *)(arg1 + 0x58);
    *(uint64_t *)(arg1 + 0x58) = 0;
    goto loc_0090B9A4;
loc_0090BA82:
    v_stack_m148 = 1;
    goto loc_0090B98C;
loc_0090BA90:
    local_rbx = (uint8_t)((-1) & (6));
    if (((uint8_t)(local_rbx)) == 2) goto loc_0090BBAE;
loc_0090BAA2:
    result = KeAbPostRelease(Arg1 + 80, v_stack_m128, Arg3, 3);
    if (v_stack_m138 >= 2) goto loc_0090BCDC;
loc_0090BABA:
    if (v_stack_m140 != 0) goto loc_0090BD0D;
loc_0090BAC8:
loc_0090BACC:
    Arg1 = (v_stack_m40) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_stack_m128, Arg3, 3);
    local_rsp = (local_rsp) + (320);
    return result;
loc_0090BAF0:
    Arg1 = ((uint32_t)((uint32_t)(local_r11))) + ((uint32_t)((uint32_t)(local_r11)));
loc_0090BAF6:
    *(uint16_t *)(arg1 - 0x2 + v_stack_p58 * 1) = 48;
    local_r11 = (uint32_t)((local_r11) + (-1));
    if (condition_is_equal) goto loc_0090B915;
    goto loc_0090BAF6;
loc_0090BB11:
    if ((*(uint32_t *)(arg1 - 0x2 + 0x4)) >= ((uint32_t)((uint32_t)(Arg3)))) goto loc_0090B983;
loc_0090BB1B:
    result = (uint8_t)((local_rbx) & (6));
    if (((uint8_t)(result)) == 2) goto loc_0090BC72;
loc_0090BB2E:
    result = KeAbPostRelease(Arg1 + 80, v_stack_m128, Arg3, 3);
    result = ((uint32_t)(*(uint32_t *)(arg1 + 0x28))) >> (4);
    result = (uint32_t)((result) & (3));
    if (((uint8_t)(result)) != 3) goto loc_0090BC80;
    if ((*(uint64_t *)(v_rip + 0x6BAF59)) == (*(uint64_t *)(arg1 + 0x98))) goto loc_0090BC80;
    if (*(uint64_t *)(arg1 + 0x98) != 0) goto loc_0090BBCC;
    goto loc_0090BACC;
loc_0090BB73:
    if ((*(uint64_t *)(arg1 + 0x58)) == 1) goto loc_0090BBBC;
loc_0090BB7C:
    v_stack_p30 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x60)));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x60)))) == 0) goto loc_0090B960;
    local_rbx = (uint8_t)((local_rbx) & (6));
    if (((uint8_t)(local_rbx)) == 2) goto loc_0090BCEB;
loc_0090BB9B:
    result = KeAbPostRelease(Arg1 + 80, v_stack_m128, Arg3, 3);
    goto loc_0090BACC;
loc_0090BBAE:
    result = ExfTryToWakePushLock(Arg1 + 80, v_stack_m128, Arg3, 3);
    goto loc_0090BAA2;
loc_0090BBBC:
    result = 0;
    goto loc_0090BB7C;
loc_0090BBC0:
    goto loc_0090B915;
loc_0090BBCC:
    if ((Arg1 + 80) != (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8))) goto loc_0090BCB7;
loc_0090BBE5:
    result = ExAllocatePool2(257, (uint32_t)(Arg3) + 16, (uint32_t)(0x20666E57ULL), 3);
    v_stack_p38 = result;
    if (0 != 0) goto loc_0090BCF9;
loc_0090BC0A:
    if (result == 0) goto loc_0090BCAD;
    *(uint64_t *)(result + 0x8) = 0;
    *(uint32_t *)(result) = 0x100904ULL;
    *(uint32_t *)(result + 0x4) = (uint32_t)((uint32_t)(Arg3));
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(Arg1 + 80, Arg2, Arg3, 3);
    if (!(condition_is_above_or_equal)) {
        Arg3 = Arg1 + 80;
        Arg2 = result;
        Arg1 = Arg1 + 80;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, 3);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    local_r14 = 0;
    if ((*(uint64_t *)(arg1 + 0x58)) != 1) { local_r14 = *(uint64_t *)(arg1 + 0x58); }
    if (local_r14 != 0) goto loc_0090BCD1;
loc_0090BC68:
    goto loc_0090B983;
loc_0090BC72:
    result = ExfTryToWakePushLock(Arg1 + 80, Arg2, Arg3, 3);
    goto loc_0090BB2E;
loc_0090BC80:
    result = ExAllocatePool2(256, (uint32_t)(Arg3) + 16, (uint32_t)(0x20666E57ULL), 3);
    v_stack_p38 = result;
    goto loc_0090BC0A;
loc_0090BCA1:
    goto loc_0090B8C0;
loc_0090BCAD:
    goto loc_0090BACC;
loc_0090BCB7:
    Arg2 = 0;
    result = KiStackAttachProcess(256, Arg2, v_stack_p88, 3);
    goto loc_0090BBE5;
loc_0090BCD1:
    if ((*(uint32_t *)(1 + 0x4)) < ((uint32_t)((uint32_t)(Arg3)))) goto loc_0090BC68;
    goto loc_0090B983;
loc_0090BCDC:
    result = ExFreePoolWithTag(256, (uint32_t)(0x20666E57ULL), v_stack_p88, 3);
    goto loc_0090BABA;
loc_0090BCEB:
    result = ExfTryToWakePushLock(Arg1 + 80, (uint32_t)(0x20666E57ULL), v_stack_p88, 3);
    goto loc_0090BB9B;
loc_0090BCF9:
    Arg2 = 0;
    result = KiUnstackDetachProcess(v_stack_p88, Arg2, v_stack_p88, 3);
    goto loc_0090BC0A;
loc_0090BD0D:
    result = ExFreePoolWithTag(v_stack_p88, (uint32_t)(0x20666E57ULL), v_stack_p88, 3);
    goto loc_0090BAC8;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x28` | `32` | `R` |
| `Arg1` | `+ 0x28` | `64` | `R` |
| `Arg1` | `+ 0x50` | `64` | `R` |
| `Arg1` | `+ 0x50` | `64` | `R/W` |
| `Arg1` | `+ 0x58` | `64` | `R` |
| `Arg1` | `+ 0x58` | `64` | `W` |
| `Arg1` | `+ 0x60` | `32` | `R` |
| `Arg1` | `+ 0x60` | `32` | `R/W` |
| `Arg1` | `+ 0x68` | `64` | `R` |
| `Arg1` | `+ 0x98` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0090B7B0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
