# PopPepInitializeVetoMasks

- RVA: `0x004C9350`–`0x004C98B2` (길이 `1,378` bytes)
- VA: `0x00000001404C9350`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BD468`
- 디코드: `333`개 명령, `1,378/1,378` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **20**; 고유 호출 대상: **14**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x004C93AB` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x004C93F3` → [RtlEqualUnicodeString](../../page/93/RtlEqualUnicodeString_function_00932A20.md) (function, `0x00932A20`)
- `0x004C94A5` → [EmClientRuleEvaluate](../../pagelk/B7/EmClientRuleEvaluate_function_00B77E90.md) (function, `0x00B77E90`)
- `0x004C9514` → [ExAcquireSpinLockExclusive](../24/ExAcquireSpinLockExclusive_function_00248690.md) (function, `0x00248690`)
- `0x004C952D` → [PpmGetDeepSleepPlatformStateIndex](../4B/PpmGetDeepSleepPlatformStateIndex_function_004B09F0.md) (function, `0x004B09F0`)
- `0x004C9541` → [PopPluginRequestDeviceIdleConstraints](../4D/PopPluginRequestDeviceIdleConstraints_function_004D2660.md) (function, `0x004D2660`)
- `0x004C9607` → [KeAcquireSpinLockAtDpcLevel](../20/KeAcquireSpinLockAtDpcLevel_function_00208430.md) (function, `0x00208430`)
- `0x004C9614` → [PopFxReinitializeAccountingInstance](../4B/PopFxReinitializeAccountingInstance_function_004B0960.md) (function, `0x004B0960`)
- `0x004C9634` → [KxReleaseSpinLock](../20/KxReleaseSpinLock_function_00206670.md) (function, `0x00206670`)
- `0x004C965E` → [PopFxBugCheck](../2B/PopFxBugCheck_function_002BFC6C.md) (function, `0x002BFC6C`)
- `0x004C96AC` → [PopPepUpdateIdleStateRefCount](../2B/PopPepUpdateIdleStateRefCount_function_002BF930.md) (function, `0x002BF930`)
- `0x004C96EF` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x004C9701` → [PopPluginRequestComponentIdleConstraints](../5D/PopPluginRequestComponentIdleConstraints_function_005D3C98.md) (function, `0x005D3C98`)
- `0x004C979F` → [KeAcquireSpinLockAtDpcLevel](../20/KeAcquireSpinLockAtDpcLevel_function_00208430.md) (function, `0x00208430`)
- `0x004C97AC` → [PopFxReinitializeAccountingInstance](../4B/PopFxReinitializeAccountingInstance_function_004B0960.md) (function, `0x004B0960`)
- `0x004C97CD` → [KxReleaseSpinLock](../20/KxReleaseSpinLock_function_00206670.md) (function, `0x00206670`)
- `0x004C981F` → [PopPepUpdateIdleStateRefCount](../2B/PopPepUpdateIdleStateRefCount_function_002BF930.md) (function, `0x002BF930`)
- `0x004C9855` → [PopFxBugCheck](../2B/PopFxBugCheck_function_002BFC6C.md) (function, `0x002BFC6C`)
- `0x004C9882` → [ExReleaseSpinLockExclusive](../2C/ExReleaseSpinLockExclusive_function_002C0EF0.md) (function, `0x002C0EF0`)
- `0x004C9891` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PopPepDeviceStarted](../4B/PopPepDeviceStarted_function_004B58D4.md) at `0x004B5917`
- [PopPepPlatformStateRegistered](../5D/PopPepPlatformStateRegistered_function_005DCDB8.md) at `0x005DCF0D`

### Static image references
- `0x004C936F` → RVA `0x00E0A740` (`.data`; read)
- `0x004C93B0` → RVA `0x00FC52C8` (`ALMOSTRO`; read)
- `0x004C93C7` → RVA `0x00E67A58` (`.data`; read)
- `0x004C949E` → RVA `0x0002AED0` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x004C93F3` → [RtlEqualUnicodeString](../../page/93/RtlEqualUnicodeString_function_00932A20.md) (`.text` → `PAGE`)
  - `0x004C94A5` → [EmClientRuleEvaluate](../../pagelk/B7/EmClientRuleEvaluate_function_00B77E90.md) (`.text` → `PAGELK`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004C9350  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
004C9355  55                              push rbp
004C9356  56                              push rsi
004C9357  57                              push rdi
004C9358  41 54                           push r12
004C935A  41 55                           push r13
004C935C  41 56                           push r14
004C935E  41 57                           push r15
004C9360  48 8D AC 24 70 FF FF FF         lea rbp, [rsp - 0x90]
004C9368  48 81 EC 90 01 00 00            sub rsp, 0x190
004C936F  48 8B 05 CA 13 94 00            mov rax, qword ptr [rip + 0x9413ca]
004C9376  48 33 C4                        xor rax, rsp
004C9379  48 89 85 80 00 00 00            mov qword ptr [rbp + 0x80], rax
004C9380  83 64 24 28 00                  and dword ptr [rsp + 0x28], 0
004C9385  48 8B D9                        mov rbx, rcx
004C9388  44 8B E2                        mov r12d, edx
004C938B  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
004C9390  0F 57 C0                        xorps xmm0, xmm0
004C9393  44 89 64 24 24                  mov dword ptr [rsp + 0x24], r12d
004C9398  33 C0                           xor eax, eax
004C939A  33 D2                           xor edx, edx
004C939C  41 B8 94 00 00 00               mov r8d, 0x94
004C93A2  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
004C93A6  0F 11 44 24 50                  movups xmmword ptr [rsp + 0x50], xmm0
004C93AB  E8 90 D8 1F 00                  call 0x1406c6c40
004C93B0  48 8B 05 11 BF AF 00            mov rax, qword ptr [rip + 0xafbf11]
004C93B7  41 BD 01 00 00 00               mov r13d, 1
004C93BD  4C 8B 7B 20                     mov r15, qword ptr [rbx + 0x20]
004C93C1  48 83 64 24 38 00               and qword ptr [rsp + 0x38], 0
004C93C7  48 8B 35 8A E6 99 00            mov rsi, qword ptr [rip + 0x99e68a]
004C93CE  45 32 F6                        xor r14b, r14b
004C93D1  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
004C93D6  49 8D BF D8 00 00 00            lea rdi, [r15 + 0xd8]
004C93DD  48 85 F6                        test rsi, rsi
004C93E0  74 22                           je 0x1404c9404
004C93E2  49 8D BF D8 00 00 00            lea rdi, [r15 + 0xd8]
004C93E9  45 8A C5                        mov r8b, r13b
004C93EC  48 8B D7                        mov rdx, rdi
004C93EF  48 8D 4E 08                     lea rcx, [rsi + 8]
004C93F3  E8 28 96 46 00                  call 0x140932a20
004C93F8  84 C0                           test al, al
004C93FA  75 05                           jne 0x1404c9401
004C93FC  48 8B 36                        mov rsi, qword ptr [rsi]
004C93FF  EB DC                           jmp 0x1404c93dd
004C9401  45 8A F5                        mov r14b, r13b
004C9404  33 F6                           xor esi, esi
004C9406  48 8D 54 24 78                  lea rdx, [rsp + 0x78]
004C940B  40 88 B3 BC 00 00 00            mov byte ptr [rbx + 0xbc], sil
004C9412  0F 10 07                        movups xmm0, xmmword ptr [rdi]
004C9415  F3 0F 7F 44 24 68               movdqu xmmword ptr [rsp + 0x68], xmm0
004C941B  83 E2 04                        and edx, 4
004C941E  74 05                           je 0x1404c9425
004C9420  44 89 6C 24 78                  mov dword ptr [rsp + 0x78], r13d
004C9425  48 85 D2                        test rdx, rdx
004C9428  48 8D 44 24 7C                  lea rax, [rsp + 0x7c]
004C942D  4C 8D 44 24 78                  lea r8, [rsp + 0x78]
004C9432  49 B9 01 00 00 00 01 00 00 00   movabs r9, 0x100000001
004C943C  4C 0F 45 C0                     cmovne r8, rax
004C9440  48 8B C2                        mov rax, rdx
004C9443  48 F7 D8                        neg rax
004C9446  49 8B F8                        mov rdi, r8
004C9449  49 8B C1                        mov rax, r9
004C944C  48 1B C9                        sbb rcx, rcx
004C944F  48 83 C1 10                     add rcx, 0x10
004C9453  F3 48 AB                        rep stosq qword ptr [rdi], rax
004C9456  48 85 D2                        test rdx, rdx
004C9459  74 0F                           je 0x1404c946a
004C945B  48 F7 DA                        neg rdx
004C945E  48 1B C0                        sbb rax, rax
004C9461  48 83 E0 FC                     and rax, 0xfffffffffffffffc
004C9465  46 89 6C 00 7C                  mov dword ptr [rax + r8 + 0x7c], r13d
004C946A  8B FE                           mov edi, esi
004C946C  45 85 E4                        test r12d, r12d
004C946F  74 59                           je 0x1404c94ca
004C9471  48 8D 44 24 60                  lea rax, [rsp + 0x60]
004C9476  89 7C 24 60                     mov dword ptr [rsp + 0x60], edi
004C947A  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
004C947F  4C 8D 4C 24 28                  lea r9, [rsp + 0x28]
004C9484  48 8D 44 24 50                  lea rax, [rsp + 0x50]
004C9489  C7 44 24 58 08 00 00 00         mov dword ptr [rsp + 0x58], 8
004C9491  45 8B C5                        mov r8d, r13d
004C9494  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
004C9499  48 8D 54 24 38                  lea rdx, [rsp + 0x38]
004C949E  48 8D 0D 2B 1A B6 FF            lea rcx, [rip - 0x49e5d5]
004C94A5  E8 E6 E9 6A 00                  call 0x140b77e90
004C94AA  83 7C 24 28 02                  cmp dword ptr [rsp + 0x28], 2
004C94AF  75 07                           jne 0x1404c94b8
004C94B1  44 88 AB BC 00 00 00            mov byte ptr [rbx + 0xbc], r13b
004C94B8  41 03 FD                        add edi, r13d
004C94BB  41 3B FC                        cmp edi, r12d
004C94BE  72 B1                           jb 0x1404c9471
004C94C0  49 B9 01 00 00 00 01 00 00 00   movabs r9, 0x100000001
004C94CA  48 8D 55 00                     lea rdx, [rbp]
004C94CE  83 E2 04                        and edx, 4
004C94D1  74 04                           je 0x1404c94d7
004C94D3  44 89 6D 00                     mov dword ptr [rbp], r13d
004C94D7  48 85 D2                        test rdx, rdx
004C94DA  48 8D 4D 04                     lea rcx, [rbp + 4]
004C94DE  4C 8D 45 00                     lea r8, [rbp]
004C94E2  49 8B C1                        mov rax, r9
004C94E5  4C 0F 45 C1                     cmovne r8, rcx
004C94E9  48 8B CA                        mov rcx, rdx
004C94EC  48 F7 D9                        neg rcx
004C94EF  49 8B F8                        mov rdi, r8
004C94F2  48 1B C9                        sbb rcx, rcx
004C94F5  48 83 C1 10                     add rcx, 0x10
004C94F9  F3 48 AB                        rep stosq qword ptr [rdi], rax
004C94FC  48 85 D2                        test rdx, rdx
004C94FF  74 0F                           je 0x1404c9510
004C9501  48 F7 DA                        neg rdx
004C9504  48 1B C0                        sbb rax, rax
004C9507  48 83 E0 FC                     and rax, 0xfffffffffffffffc
004C950B  46 89 6C 00 7C                  mov dword ptr [rax + r8 + 0x7c], r13d
004C9510  48 8D 4B 40                     lea rcx, [rbx + 0x40]
004C9514  E8 77 F1 D7 FF                  call 0x140248690
004C9519  83 BB AC 00 00 00 02            cmp dword ptr [rbx + 0xac], 2
004C9520  44 8A E8                        mov r13b, al
004C9523  88 44 24 20                     mov byte ptr [rsp + 0x20], al
004C9527  0F 84 4E 03 00 00               je 0x1404c987b
004C952D  E8 BE 74 FE FF                  call 0x1404b09f0
004C9532  48 8B 4B 20                     mov rcx, qword ptr [rbx + 0x20]
004C9536  48 8D 55 00                     lea rdx, [rbp]
004C953A  45 8B C4                        mov r8d, r12d
004C953D  89 44 24 2C                     mov dword ptr [rsp + 0x2c], eax
004C9541  E8 1A 91 00 00                  call 0x1404d2660
004C9546  45 84 F6                        test r14b, r14b
004C9549  74 09                           je 0x1404c9554
004C954B  40 88 B3 BC 00 00 00            mov byte ptr [rbx + 0xbc], sil
004C9552  EB 04                           jmp 0x1404c9558
004C9554  84 C0                           test al, al
004C9556  75 0E                           jne 0x1404c9566
004C9558  40 38 B3 BC 00 00 00            cmp byte ptr [rbx + 0xbc], sil
004C955F  75 0E                           jne 0x1404c956f
004C9561  E9 24 01 00 00                  jmp 0x1404c968a
004C9566  40 38 B3 BC 00 00 00            cmp byte ptr [rbx + 0xbc], sil
004C956D  74 23                           je 0x1404c9592
004C956F  45 85 E4                        test r12d, r12d
004C9572  74 1E                           je 0x1404c9592
004C9574  48 8B C6                        mov rax, rsi
004C9577  49 8B CC                        mov rcx, r12
004C957A  8B 54 04 78                     mov edx, dword ptr [rsp + rax + 0x78]
004C957E  39 54 05 00                     cmp dword ptr [rbp + rax], edx
004C9582  73 04                           jae 0x1404c9588
004C9584  89 54 05 00                     mov dword ptr [rbp + rax], edx
004C9588  48 83 C0 04                     add rax, 4
004C958C  48 83 E9 01                     sub rcx, 1
004C9590  75 E8                           jne 0x1404c957a
004C9592  44 8B 6C 24 24                  mov r13d, dword ptr [rsp + 0x24]
004C9597  4C 8D 75 00                     lea r14, [rbp]
004C959B  41 BC 01 00 00 00               mov r12d, 1
004C95A1  41 3B F5                        cmp esi, r13d
004C95A4  0F 83 BA 00 00 00               jae 0x1404c9664
004C95AA  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
004C95AF  44 8B C6                        mov r8d, esi
004C95B2  49 69 C0 C0 01 00 00            imul rax, r8, 0x1c0
004C95B9  80 7C 08 39 00                  cmp byte ptr [rax + rcx + 0x39], 0
004C95BE  75 0C                           jne 0x1404c95cc
004C95C0  42 83 7C 85 00 01               cmp dword ptr [rbp + r8*4], 1
004C95C6  0F 85 87 00 00 00               jne 0x1404c9653
004C95CC  41 8B 3E                        mov edi, dword ptr [r14]
004C95CF  BA 01 00 00 00                  mov edx, 1
004C95D4  3B D7                           cmp edx, edi
004C95D6  73 12                           jae 0x1404c95ea
004C95D8  8D 42 FF                        lea eax, [rdx - 1]
004C95DB  FF C2                           inc edx
004C95DD  44 09 A4 83 90 00 00 00         or dword ptr [rbx + rax*4 + 0x90], r12d
004C95E5  83 FA 03                        cmp edx, 3
004C95E8  76 EA                           jbe 0x1404c95d4
004C95EA  8B 7C 24 2C                     mov edi, dword ptr [rsp + 0x2c]
004C95EE  83 FF FF                        cmp edi, -1
004C95F1  74 52                           je 0x1404c9645
004C95F3  3B F7                           cmp esi, edi
004C95F5  75 4E                           jne 0x1404c9645
004C95F7  41 83 3E 01                     cmp dword ptr [r14], 1
004C95FB  76 48                           jbe 0x1404c9645
004C95FD  49 8D BF 80 02 00 00            lea rdi, [r15 + 0x280]
004C9604  48 8B CF                        mov rcx, rdi
004C9607  E8 24 EE D3 FF                  call 0x140208430
004C960C  BA 02 00 00 00                  mov edx, 2
004C9611  48 8B CF                        mov rcx, rdi
004C9614  E8 47 73 FE FF                  call 0x1404b0960
004C9619  41 8B 06                        mov eax, dword ptr [r14]
004C961C  48 8B CF                        mov rcx, rdi
004C961F  89 47 0C                        mov dword ptr [rdi + 0xc], eax
004C9622  48 A1 08 00 00 00 80 F7 FF FF   movabs rax, qword ptr [0xfffff78000000008]
004C962C  48 89 47 18                     mov qword ptr [rdi + 0x18], rax
004C9630  C6 47 08 01                     mov byte ptr [rdi + 8], 1
004C9634  E8 37 D0 D3 FF                  call 0x140206670
004C9639  F0 41 81 8F 60 03 00 00 10 08 00 00  lock or dword ptr [r15 + 0x360], 0x810
004C9645  49 83 C6 04                     add r14, 4
004C9649  45 03 E4                        add r12d, r12d
004C964C  FF C6                           inc esi
004C964E  E9 4E FF FF FF                  jmp 0x1404c95a1
004C9653  45 33 C9                        xor r9d, r9d
004C9656  49 8B D7                        mov rdx, r15
004C9659  B9 20 06 00 00                  mov ecx, 0x620
004C965E  E8 09 66 DF FF                  call 0x1402bfc6c
004C9663  CC                              int3
004C9664  F2 0F 10 83 90 00 00 00         movsd xmm0, qword ptr [rbx + 0x90]
004C966C  45 8B E5                        mov r12d, r13d
004C966F  8B 83 98 00 00 00               mov eax, dword ptr [rbx + 0x98]
004C9675  33 F6                           xor esi, esi
004C9677  44 8A 6C 24 20                  mov r13b, byte ptr [rsp + 0x20]
004C967C  F2 0F 11 83 9C 00 00 00         movsd qword ptr [rbx + 0x9c], xmm0
004C9684  89 83 A4 00 00 00               mov dword ptr [rbx + 0xa4], eax
004C968A  48 63 83 A8 00 00 00            movsxd rax, dword ptr [rbx + 0xa8]
004C9691  83 F8 04                        cmp eax, 4
004C9694  74 1B                           je 0x1404c96b1
004C9696  8B 94 83 8C 00 00 00            mov edx, dword ptr [rbx + rax*4 + 0x8c]
004C969D  4C 8D 8B B8 00 00 00            lea r9, [rbx + 0xb8]
004C96A4  41 B8 01 00 00 00               mov r8d, 1
004C96AA  33 C9                           xor ecx, ecx
004C96AC  E8 7F 62 DF FF                  call 0x1402bf930
004C96B1  40 38 73 7C                     cmp byte ptr [rbx + 0x7c], sil
004C96B5  0F 84 AD 01 00 00               je 0x1404c9868
004C96BB  40 8A FE                        mov dil, sil
004C96BE  3B B3 B4 00 00 00               cmp esi, dword ptr [rbx + 0xb4]
004C96C4  0F 83 91 01 00 00               jae 0x1404c985b
004C96CA  49 8B 87 68 03 00 00            mov rax, qword ptr [r15 + 0x368]
004C96D1  33 D2                           xor edx, edx
004C96D3  8B CE                           mov ecx, esi
004C96D5  41 B8 80 00 00 00               mov r8d, 0x80
004C96DB  4C 69 E9 D0 00 00 00            imul r13, rcx, 0xd0
004C96E2  48 8B 04 C8                     mov rax, qword ptr [rax + rcx*8]
004C96E6  48 8D 4D 00                     lea rcx, [rbp]
004C96EA  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
004C96EF  E8 4C D5 1F 00                  call 0x1406c6c40
004C96F4  48 8B 4B 20                     mov rcx, qword ptr [rbx + 0x20]
004C96F8  4C 8D 45 00                     lea r8, [rbp]
004C96FC  45 8B CC                        mov r9d, r12d
004C96FF  8B D6                           mov edx, esi
004C9701  E8 92 A5 10 00                  call 0x1405d3c98
004C9706  84 C0                           test al, al
004C9708  0F 84 E7 00 00 00               je 0x1404c97f5
004C970E  4C 8D 65 00                     lea r12, [rbp]
004C9712  BA 01 00 00 00                  mov edx, 1
004C9717  45 33 F6                        xor r14d, r14d
004C971A  89 54 24 30                     mov dword ptr [rsp + 0x30], edx
004C971E  44 3B 74 24 24                  cmp r14d, dword ptr [rsp + 0x24]
004C9723  0F 83 C7 00 00 00               jae 0x1404c97f0
004C9729  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
004C972E  45 8B CE                        mov r9d, r14d
004C9731  49 69 C1 C0 01 00 00            imul rax, r9, 0x1c0
004C9738  80 7C 08 39 00                  cmp byte ptr [rax + rcx + 0x39], 0
004C973D  75 0C                           jne 0x1404c974b
004C973F  42 83 7C B5 00 00               cmp dword ptr [rbp + r14*4], 0
004C9745  0F 85 FF 00 00 00               jne 0x1404c984a
004C974B  4A 8B 84 2B 88 01 00 00         mov rax, qword ptr [rbx + r13 + 0x188]
004C9753  33 C9                           xor ecx, ecx
004C9755  42 39 8C 2B 7C 01 00 00         cmp dword ptr [rbx + r13 + 0x17c], ecx
004C975D  76 1C                           jbe 0x1404c977b
004C975F  48 83 C0 10                     add rax, 0x10
004C9763  41 3B 0C 24                     cmp ecx, dword ptr [r12]
004C9767  73 12                           jae 0x1404c977b
004C9769  09 10                           or dword ptr [rax], edx
004C976B  FF C1                           inc ecx
004C976D  48 83 C0 18                     add rax, 0x18
004C9771  42 3B 8C 2B 7C 01 00 00         cmp ecx, dword ptr [rbx + r13 + 0x17c]
004C9779  72 E8                           jb 0x1404c9763
004C977B  8B 44 24 2C                     mov eax, dword ptr [rsp + 0x2c]
004C977F  83 F8 FF                        cmp eax, -1
004C9782  74 5E                           je 0x1404c97e2
004C9784  44 3B F0                        cmp r14d, eax
004C9787  75 59                           jne 0x1404c97e2
004C9789  41 83 3C 24 00                  cmp dword ptr [r12], 0
004C978E  76 52                           jbe 0x1404c97e2
004C9790  48 8B 7C 24 48                  mov rdi, qword ptr [rsp + 0x48]
004C9795  48 81 C7 C8 00 00 00            add rdi, 0xc8
004C979C  48 8B CF                        mov rcx, rdi
004C979F  E8 8C EC D3 FF                  call 0x140208430
004C97A4  BA 02 00 00 00                  mov edx, 2
004C97A9  48 8B CF                        mov rcx, rdi
004C97AC  E8 AF 71 FE FF                  call 0x1404b0960
004C97B1  41 8B 04 24                     mov eax, dword ptr [r12]
004C97B5  48 8B CF                        mov rcx, rdi
004C97B8  89 47 0C                        mov dword ptr [rdi + 0xc], eax
004C97BB  48 A1 08 00 00 00 80 F7 FF FF   movabs rax, qword ptr [0xfffff78000000008]
004C97C5  48 89 47 18                     mov qword ptr [rdi + 0x18], rax
004C97C9  C6 47 08 01                     mov byte ptr [rdi + 8], 1
004C97CD  E8 9E CE D3 FF                  call 0x140206670
004C97D2  40 B7 01                        mov dil, 1
004C97D5  F0 41 83 8F 60 03 00 00 10      lock or dword ptr [r15 + 0x360], 0x10
004C97DE  8B 54 24 30                     mov edx, dword ptr [rsp + 0x30]
004C97E2  49 83 C4 04                     add r12, 4
004C97E6  03 D2                           add edx, edx
004C97E8  41 FF C6                        inc r14d
004C97EB  E9 2A FF FF FF                  jmp 0x1404c971a
004C97F0  44 8B 64 24 24                  mov r12d, dword ptr [rsp + 0x24]
004C97F5  42 8B 84 2B 70 01 00 00         mov eax, dword ptr [rbx + r13 + 0x170]
004C97FD  4C 8D 8B 80 01 00 00            lea r9, [rbx + 0x180]
004C9804  4A 8B 94 2B 88 01 00 00         mov rdx, qword ptr [rbx + r13 + 0x188]
004C980C  4D 03 CD                        add r9, r13
004C980F  41 B8 01 00 00 00               mov r8d, 1
004C9815  48 8D 0C 40                     lea rcx, [rax + rax*2]
004C9819  8B 54 CA 10                     mov edx, dword ptr [rdx + rcx*8 + 0x10]
004C981D  33 C9                           xor ecx, ecx
004C981F  E8 0C 61 DF FF                  call 0x1402bf930
004C9824  40 84 FF                        test dil, dil
004C9827  75 0E                           jne 0x1404c9837
004C9829  F0 41 81 A7 60 03 00 00 FF FE FF FF  lock and dword ptr [r15 + 0x360], 0xfffffeff
004C9835  EB 0C                           jmp 0x1404c9843
004C9837  F0 41 81 8F 60 03 00 00 00 01 00 00  lock or dword ptr [r15 + 0x360], 0x100
004C9843  FF C6                           inc esi
004C9845  E9 74 FE FF FF                  jmp 0x1404c96be
004C984A  44 8B C6                        mov r8d, esi
004C984D  49 8B D7                        mov rdx, r15
004C9850  B9 21 06 00 00                  mov ecx, 0x621
004C9855  E8 12 64 DF FF                  call 0x1402bfc6c
004C985A  CC                              int3
004C985B  44 8A 6C 24 20                  mov r13b, byte ptr [rsp + 0x20]
004C9860  33 F6                           xor esi, esi
004C9862  40 38 73 7C                     cmp byte ptr [rbx + 0x7c], sil
004C9866  75 09                           jne 0x1404c9871
004C9868  40 38 B3 BC 00 00 00            cmp byte ptr [rbx + 0xbc], sil
004C986F  74 0A                           je 0x1404c987b
004C9871  C7 83 AC 00 00 00 02 00 00 00   mov dword ptr [rbx + 0xac], 2
004C987B  48 8D 4B 40                     lea rcx, [rbx + 0x40]
004C987F  41 8A D5                        mov dl, r13b
004C9882  E8 69 76 DF FF                  call 0x1402c0ef0
004C9887  48 8B 8D 80 00 00 00            mov rcx, qword ptr [rbp + 0x80]
004C988E  48 33 CC                        xor rcx, rsp
004C9891  E8 AA 2D 1E 00                  call 0x1406ac640
004C9896  48 8B 9C 24 E0 01 00 00         mov rbx, qword ptr [rsp + 0x1e0]
004C989E  48 81 C4 90 01 00 00            add rsp, 0x190
004C98A5  41 5F                           pop r15
004C98A7  41 5E                           pop r14
004C98A9  41 5D                           pop r13
004C98AB  41 5C                           pop r12
004C98AD  5F                              pop rdi
004C98AE  5E                              pop rsi
004C98AF  5D                              pop rbp
004C98B0  C3                              ret
004C98B1  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopPepInitializeVetoMasks(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m14C;
    unsigned __int64 v_stack_m150;
    unsigned __int64 v_stack_m160;
    unsigned int v_stack_m164;
    unsigned __int64 v_stack_m168;
    unsigned int v_stack_m170;
    unsigned __int64 v_stack_m178;
    unsigned __int64 v_stack_m180;
    unsigned __int64 v_stack_m188;
    unsigned __int64 v_stack_m190;
    unsigned int v_stack_m198;
    unsigned int v_stack_m19C;
    unsigned int v_stack_m1A0;
    unsigned int v_stack_m1A4;
    unsigned __int8 v_stack_m1A8;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_mC4;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_p18;

    v_stack_p18 = v_rbx;
    v_rsp = (v_rsp) - (400);
    result = (*(unsigned __int64 *)(v_rip + 9704394)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m1A4 = (unsigned int)((unsigned int)(a2));
    result = 0;
    a2 = 0;
    v_stack_m164 = 0;
    v_stack_m178 = v_xmm0;
    result = memset(v_stack_m168, a2, 148, a4);
    v_r14 = 0;
    v_stack_m188 = *(unsigned __int64 *)(v_rip + 11517713);
loc_004C93DD:
    if (*(unsigned __int64 *)(v_rip + 10086026) == 0) goto loc_004C9404;
    result = RtlEqualUnicodeString(*(unsigned __int64 *)(v_rip + 10086026) + 8, *(unsigned __int64 *)(a1 + 32) + 216, 1, a4);
    if ((unsigned __int8)(result) != 0) goto loc_004C9401;
    goto loc_004C93DD;
loc_004C9401:
loc_004C9404:
    v_rsi = 0;
    *(unsigned __int8 *)(a1 + 188) = 0;
    v_stack_m160 = v_xmm0;
    a2 = (unsigned int)((v_stack_m150) & (4));
    if (!(condition_is_equal)) {
        v_stack_m150 = 1;
    }
    a3 = v_stack_m150;
    if (a2 != 0) { a3 = v_stack_m14C; }
    result = -(a2);
    a1 = (*(unsigned __int64 *)(v_rip + 10086026) + 8) + (16);
    result = a4;
    if (a2 != 0) {
        a2 = -(a2);
        result = (a4) & (-4);
        *(unsigned int *)(result + a3 * 1 + 124) = 1;
    }
    if ((unsigned int)((unsigned int)(a2)) == 0) goto loc_004C94CA;
loc_004C9471:
    v_stack_m168 = 0;
    v_stack_m178 = v_stack_m168;
    v_stack_m170 = 8;
    v_stack_m190 = v_stack_m178;
    result = EmClientRuleEvaluate(v_rip - 4842965, v_stack_m190, 1, v_stack_m1A0);
    if (v_stack_m1A0 == 2) {
        *(unsigned __int8 *)(a1 + 188) = 1;
    }
    v_rdi = (unsigned int)((0) + (1));
    if (((unsigned int)(v_rdi)) < ((unsigned int)((unsigned int)(a2)))) goto loc_004C9471;
loc_004C94CA:
    a2 = (unsigned int)((v_stack_mC8) & (4));
    if (!(condition_is_equal)) {
        v_stack_mC8 = 1;
    }
    a3 = v_stack_mC8;
    if (a2 != 0) { a3 = v_stack_mC4; }
    a1 = -(a2);
    a1 = (a1) + (16);
    result = v_stack_m1A0;
    if (a2 != 0) {
        a2 = -(a2);
        result = (v_stack_m1A0) & (-4);
        *(unsigned int *)(result + a3 * 1 + 124) = 1;
    }
    result = ExAcquireSpinLockExclusive(a1 + 64, a2, a3, v_stack_m1A0);
    v_stack_m1A8 = (unsigned __int8)(result);
    if ((*(unsigned int *)(a1 + 172)) == 2) goto loc_004C987B;
    result = PpmGetDeepSleepPlatformStateIndex(a1 + 64, a2, a3, v_stack_m1A0);
    v_stack_m19C = (unsigned int)(result);
    result = PopPluginRequestDeviceIdleConstraints(*(unsigned __int64 *)(a1 + 32), v_stack_mC8, (unsigned int)((unsigned int)((unsigned int)(a2))), v_stack_m1A0);
    if (1 == 0) goto loc_004C9554;
    *(unsigned __int8 *)(a1 + 188) = 0;
    goto loc_004C9558;
loc_004C9554:
    if ((unsigned __int8)(result) != 0) goto loc_004C9566;
loc_004C9558:
    if ((*(unsigned __int8 *)(a1 + 188)) != 0) goto loc_004C956F;
    goto loc_004C968A;
loc_004C9566:
    if ((*(unsigned __int8 *)(a1 + 188)) == 0) goto loc_004C9592;
loc_004C956F:
    if ((unsigned int)((unsigned int)(a2)) == 0) goto loc_004C9592;
loc_004C957A:
    if ((*(unsigned int *)(v_stack_mC8 + 0 * 1)) < ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp + 0 * 1 + 120))))) {
        *(unsigned int *)(v_stack_mC8 + 0 * 1) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp + 0 * 1 + 120)));
    }
    result = (0) + (4);
    a1 = ((unsigned int)(a2)) - (1);
    if (condition_is_not_equal) goto loc_004C957A;
loc_004C9592:
loc_004C95A1:
    if (0 >= ((unsigned int)((unsigned int)(v_stack_m1A4)))) goto loc_004C9664;
    result = (result) * (0);
    if ((*(unsigned __int8 *)(result + v_stack_m188 * 1 + 57)) != 0) goto loc_004C95CC;
    if ((*(unsigned int *)(v_stack_mC8 + 0 * 4)) != 1) goto loc_004C9653;
loc_004C95CC:
loc_004C95D4:
    if (1 >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mC8))))) goto loc_004C95EA;
    a2 = (unsigned int)((1) + 1);
    if (a2 <= 3) goto loc_004C95D4;
loc_004C95EA:
    if (((unsigned int)((unsigned int)(v_stack_m19C))) == -1) goto loc_004C9645;
    if (0 != ((unsigned int)((unsigned int)(v_stack_m19C)))) goto loc_004C9645;
    result = 1 - 1;
    v_rdi = (unsigned int)(v_stack_m19C);
    if ((*(unsigned int *)(v_stack_mC8)) >= = 1) {
        v_rdi = *(unsigned __int64 *)(a1 + 32) + 640;
        a1 = v_rdi;
        result = KeAcquireSpinLockAtDpcLevel(a1, a2, 0, v_stack_m1A0);
        a2 = 2;
        a1 = v_rdi;
        result = PopFxReinitializeAccountingInstance(a1, a2, 0, v_stack_m1A0);
        result = *(unsigned int *)(v_stack_mC8);
        a1 = v_rdi;
        *(unsigned int *)(v_rdi + 12) = (unsigned int)(result);
        *(unsigned __int64 *)(v_rdi + 24) = result;
        *(unsigned __int8 *)(v_rdi + 8) = 1;
        result = KxReleaseSpinLock(a1, a2, 0, v_stack_m1A0);
    }
    v_r14 = (v_stack_mC8) + (4);
    v_r12 = (unsigned int)((1) + (1));
    v_rsi = (unsigned int)((v_rsi) + 1);
    goto loc_004C95A1;
loc_004C9653:
    a4 = 0;
    result = PopFxBugCheck((unsigned int)(0x620ULL), *(unsigned __int64 *)(a1 + 32), 0, a4);
loc_004C9664:
    v_rsi = 0;
    *(unsigned __int64 *)(a1 + 156) = v_xmm0;
    *(unsigned int *)(a1 + 164) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 152)));
loc_004C968A:
    result = (int)(*(unsigned int *)(a1 + 168));
    if (((unsigned int)((int)(*(unsigned int *)(a1 + 168)))) != 4) {
        a2 = *(unsigned int *)(a1 + (int)(*(unsigned int *)(a1 + 168)) * 4 + 140);
        a4 = a1 + 184;
        a3 = 1;
        a1 = 0;
        result = PopPepUpdateIdleStateRefCount(a1, a2, a3, a4);
    }
    if ((*(unsigned __int8 *)(a1 + 124)) == 0) goto loc_004C9868;
loc_004C96BE:
    if (0 >= (*(unsigned int *)(a1 + 180))) goto loc_004C985B;
    a2 = 0;
    v_r13 = (v_stack_m1A8) * (0);
    v_stack_m180 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 872) + 0 * 8);
    result = memset(v_stack_mC8, a2, 128, a4);
    result = PopPluginRequestComponentIdleConstraints(*(unsigned __int64 *)(a1 + 32), 0, v_stack_mC8, (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m1A4))))));
    if ((unsigned __int8)(result) == 0) goto loc_004C97F5;
    v_r14 = 0;
loc_004C971A:
    v_stack_m198 = 1;
    if (0 >= v_stack_m1A4) goto loc_004C97F0;
    result = (result) * (0);
    if ((*(unsigned __int8 *)(result + v_stack_m188 * 1 + 57)) != 0) goto loc_004C974B;
    if ((*(unsigned int *)(v_stack_mC8 + v_r14 * 4)) != 0) goto loc_004C984A;
loc_004C974B:
    a1 = 0;
    if ((*(unsigned int *)(a1 + v_r13 * 1 + 380)) <= 0) goto loc_004C977B;
    result = (*(unsigned __int64 *)(a1 + v_r13 * 1 + 392)) + (16);
loc_004C9763:
    if (0 >= (*(unsigned int *)(v_stack_mC8))) goto loc_004C977B;
    a1 = (unsigned int)((a1) + 1);
    result = (result) + (24);
    if (((unsigned int)(a1)) < (*(unsigned int *)(a1 + v_r13 * 1 + 380))) goto loc_004C9763;
loc_004C977B:
    if (((unsigned int)((unsigned int)(v_stack_m19C))) == -1) goto loc_004C97E2;
    if (0 != ((unsigned int)((unsigned int)(v_stack_m19C)))) goto loc_004C97E2;
    result = (unsigned int)(v_stack_m19C);
    v_rdi = 0;
    if ((*(unsigned int *)(v_stack_mC8)) >= = 0) {
        v_rdi = v_stack_m180;
        v_rdi = (v_rdi) + (200);
        a1 = v_rdi;
        result = KeAcquireSpinLockAtDpcLevel(a1, 1, v_stack_mC8, 0);
        a2 = 2;
        a1 = v_rdi;
        result = PopFxReinitializeAccountingInstance(a1, a2, v_stack_mC8, 0);
        result = *(unsigned int *)(v_stack_mC8);
        a1 = v_rdi;
        *(unsigned int *)(v_rdi + 12) = (unsigned int)(result);
        *(unsigned __int64 *)(v_rdi + 24) = result;
        *(unsigned __int8 *)(v_rdi + 8) = 1;
        result = KxReleaseSpinLock(a1, a2, v_stack_mC8, 0);
        v_rdi = 1;
        a2 = v_stack_m198;
    }
    v_r12 = (v_stack_mC8) + (4);
    a2 = (unsigned int)((a2) + (a2));
    v_r14 = (unsigned int)((v_r14) + 1);
    goto loc_004C971A;
loc_004C97F0:
loc_004C97F5:
    a4 = (a1 + 384) + (v_r13);
    a1 = 0;
    result = PopPepUpdateIdleStateRefCount(a1, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + v_r13 * 1 + 392) + (unsigned int)(*(unsigned int *)(a1 + v_r13 * 1 + 368)) + (unsigned int)(*(unsigned int *)(a1 + v_r13 * 1 + 368)) * 2 * 8 + 16)), 1, a4);
    if ((unsigned __int8)(v_rdi) != 0) goto loc_004C9837;
    goto loc_004C9843;
loc_004C9837:
loc_004C9843:
    v_rsi = (unsigned int)((v_rsi) + 1);
    goto loc_004C96BE;
loc_004C984A:
    result = PopFxBugCheck((unsigned int)(0x621ULL), *(unsigned __int64 *)(a1 + 32), (unsigned int)((unsigned int)(v_rsi)), a4);
loc_004C985B:
    v_rsi = 0;
    if ((*(unsigned __int8 *)(a1 + 124)) != 0) goto loc_004C9871;
loc_004C9868:
    if ((*(unsigned __int8 *)(a1 + 188)) != 0) {
        *(unsigned int *)(a1 + 172) = 2;
    }
    result = ExReleaseSpinLockExclusive(a1 + 64, (unsigned __int8)(v_stack_m1A8), (unsigned int)((unsigned int)(v_rsi)), a4);
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, (unsigned __int8)(v_stack_m1A8), (unsigned int)((unsigned int)(v_rsi)), a4);
    v_rsp = (v_rsp) + (400);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopPepInitializeVetoMasks(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m14C;
    uint64_t v_stack_m150;
    uint64_t v_stack_m160;
    uint32_t v_stack_m164;
    uint64_t v_stack_m168;
    uint32_t v_stack_m170;
    uint64_t v_stack_m178;
    uint64_t v_stack_m180;
    uint64_t v_stack_m188;
    uint64_t v_stack_m190;
    uint32_t v_stack_m198;
    uint32_t v_stack_m19C;
    uint32_t v_stack_m1A0;
    uint32_t v_stack_m1A4;
    uint8_t v_stack_m1A8;
    uint64_t v_stack_m48;
    uint64_t v_stack_mC4;
    uint64_t v_stack_mC8;
    uint64_t v_stack_p18;

    v_stack_p18 = local_rbx;
    local_rsp = (local_rsp) - (400);
    result = (*(uint64_t *)(v_rip + 0x9413CA)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m1A4 = (uint32_t)((uint32_t)(Arg2));
    result = 0;
    Arg2 = 0;
    v_stack_m164 = 0;
    v_stack_m178 = v_xmm0;
    result = memset(v_stack_m168, Arg2, 148, a4);
    local_r14 = 0;
    v_stack_m188 = *(uint64_t *)(v_rip + 0xAFBF11);
loc_004C93DD:
    if (*(uint64_t *)(v_rip + 0x99E68A) == 0) goto loc_004C9404;
    result = RtlEqualUnicodeString(*(uint64_t *)(v_rip + 0x99E68A) + 8, *(uint64_t *)(arg1 + 0x20) + 216, 1, a4);
    if ((uint8_t)(result) != 0) goto loc_004C9401;
    goto loc_004C93DD;
loc_004C9401:
loc_004C9404:
    local_rsi = 0;
    *(uint8_t *)(arg1 + 0xBC) = 0;
    v_stack_m160 = v_xmm0;
    Arg2 = (uint32_t)((v_stack_m150) & (4));
    if (!(condition_is_equal)) {
        v_stack_m150 = 1;
    }
    a3 = v_stack_m150;
    if (Arg2 != 0) { a3 = v_stack_m14C; }
    result = -(Arg2);
    Arg1 = (*(uint64_t *)(v_rip + 0x99E68A) + 8) + (16);
    result = a4;
    if (Arg2 != 0) {
        Arg2 = -(Arg2);
        result = (a4) & (-4);
        *(uint32_t *)(result + a3 * 1 + 0x7C) = 1;
    }
    if ((uint32_t)((uint32_t)(Arg2)) == 0) goto loc_004C94CA;
loc_004C9471:
    v_stack_m168 = 0;
    v_stack_m178 = v_stack_m168;
    v_stack_m170 = 8;
    v_stack_m190 = v_stack_m178;
    result = EmClientRuleEvaluate(v_rip - 4842965, v_stack_m190, 1, v_stack_m1A0);
    if (v_stack_m1A0 == 2) {
        *(uint8_t *)(arg1 + 0xBC) = 1;
    }
    local_rdi = (uint32_t)((0) + (1));
    if (((uint32_t)(local_rdi)) < ((uint32_t)((uint32_t)(Arg2)))) goto loc_004C9471;
loc_004C94CA:
    Arg2 = (uint32_t)((v_stack_mC8) & (4));
    if (!(condition_is_equal)) {
        v_stack_mC8 = 1;
    }
    a3 = v_stack_mC8;
    if (Arg2 != 0) { a3 = v_stack_mC4; }
    Arg1 = -(Arg2);
    Arg1 = (Arg1) + (16);
    result = v_stack_m1A0;
    if (Arg2 != 0) {
        Arg2 = -(Arg2);
        result = (v_stack_m1A0) & (-4);
        *(uint32_t *)(result + a3 * 1 + 0x7C) = 1;
    }
    result = ExAcquireSpinLockExclusive(Arg1 + 64, Arg2, a3, v_stack_m1A0);
    v_stack_m1A8 = (uint8_t)(result);
    if ((*(uint32_t *)(arg1 + 0xAC)) == 2) goto loc_004C987B;
    result = PpmGetDeepSleepPlatformStateIndex(Arg1 + 64, Arg2, a3, v_stack_m1A0);
    v_stack_m19C = (uint32_t)(result);
    result = PopPluginRequestDeviceIdleConstraints(*(uint64_t *)(arg1 + 0x20), v_stack_mC8, (uint32_t)((uint32_t)((uint32_t)(Arg2))), v_stack_m1A0);
    if (1 == 0) goto loc_004C9554;
    *(uint8_t *)(arg1 + 0xBC) = 0;
    goto loc_004C9558;
loc_004C9554:
    if ((uint8_t)(result) != 0) goto loc_004C9566;
loc_004C9558:
    if ((*(uint8_t *)(arg1 + 0xBC)) != 0) goto loc_004C956F;
    goto loc_004C968A;
loc_004C9566:
    if ((*(uint8_t *)(arg1 + 0xBC)) == 0) goto loc_004C9592;
loc_004C956F:
    if ((uint32_t)((uint32_t)(Arg2)) == 0) goto loc_004C9592;
loc_004C957A:
    if ((*(uint32_t *)(v_stack_mC8 + 0x0 * 1)) < ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp + 0x0 * 1 + 0x78))))) {
        *(uint32_t *)(v_stack_mC8 + 0x0 * 1) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp + 0x0 * 1 + 0x78)));
    }
    result = (0) + (4);
    Arg1 = ((uint32_t)(Arg2)) - (1);
    if (condition_is_not_equal) goto loc_004C957A;
loc_004C9592:
loc_004C95A1:
    if (0 >= ((uint32_t)((uint32_t)(v_stack_m1A4)))) goto loc_004C9664;
    result = (result) * (0);
    if ((*(uint8_t *)(result + v_stack_m188 * 1 + 0x39)) != 0) goto loc_004C95CC;
    if ((*(uint32_t *)(v_stack_mC8 + 0x0 * 4)) != 1) goto loc_004C9653;
loc_004C95CC:
loc_004C95D4:
    if (1 >= ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mC8))))) goto loc_004C95EA;
    Arg2 = (uint32_t)((1) + 1);
    if (Arg2 <= 3) goto loc_004C95D4;
loc_004C95EA:
    if (((uint32_t)((uint32_t)(v_stack_m19C))) == -1) goto loc_004C9645;
    if (0 != ((uint32_t)((uint32_t)(v_stack_m19C)))) goto loc_004C9645;
    result = 1 - 1;
    local_rdi = (uint32_t)(v_stack_m19C);
    if ((*(uint32_t *)(v_stack_mC8)) >= = 1) {
        local_rdi = *(uint64_t *)(arg1 + 0x20) + 640;
        Arg1 = local_rdi;
        result = KeAcquireSpinLockAtDpcLevel(Arg1, Arg2, 0, v_stack_m1A0);
        Arg2 = 2;
        Arg1 = local_rdi;
        result = PopFxReinitializeAccountingInstance(Arg1, Arg2, 0, v_stack_m1A0);
        result = *(uint32_t *)(v_stack_mC8);
        Arg1 = local_rdi;
        *(uint32_t *)(local_rdi + 0xC) = (uint32_t)(result);
        *(uint64_t *)(local_rdi + 0x18) = result;
        *(uint8_t *)(local_rdi + 0x8) = 1;
        result = KxReleaseSpinLock(Arg1, Arg2, 0, v_stack_m1A0);
    }
    local_r14 = (v_stack_mC8) + (4);
    local_r12 = (uint32_t)((1) + (1));
    local_rsi = (uint32_t)((local_rsi) + 1);
    goto loc_004C95A1;
loc_004C9653:
    a4 = 0;
    result = PopFxBugCheck((uint32_t)(0x620ULL), *(uint64_t *)(arg1 + 0x20), 0, a4);
loc_004C9664:
    local_rsi = 0;
    *(uint64_t *)(arg1 + 0x9C) = v_xmm0;
    *(uint32_t *)(arg1 + 0xA4) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x98)));
loc_004C968A:
    result = (int32_t)(*(uint32_t *)(arg1 + 0xA8));
    if (((uint32_t)((int32_t)(*(uint32_t *)(arg1 + 0xA8)))) != 4) {
        Arg2 = *(uint32_t *)(arg1 + (int32_t)(*(uint32_t *)(arg1 + 0xA8)) * 4 + 0x8C);
        a4 = Arg1 + 184;
        a3 = 1;
        Arg1 = 0;
        result = PopPepUpdateIdleStateRefCount(Arg1, Arg2, a3, a4);
    }
    if ((*(uint8_t *)(arg1 + 0x7C)) == 0) goto loc_004C9868;
loc_004C96BE:
    if (0 >= (*(uint32_t *)(arg1 + 0xB4))) goto loc_004C985B;
    Arg2 = 0;
    local_r13 = (v_stack_m1A8) * (0);
    v_stack_m180 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x368) + 0x0 * 8);
    result = memset(v_stack_mC8, Arg2, 128, a4);
    result = PopPluginRequestComponentIdleConstraints(*(uint64_t *)(arg1 + 0x20), 0, v_stack_mC8, (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m1A4))))));
    if ((uint8_t)(result) == 0) goto loc_004C97F5;
    local_r14 = 0;
loc_004C971A:
    v_stack_m198 = 1;
    if (0 >= v_stack_m1A4) goto loc_004C97F0;
    result = (result) * (0);
    if ((*(uint8_t *)(result + v_stack_m188 * 1 + 0x39)) != 0) goto loc_004C974B;
    if ((*(uint32_t *)(v_stack_mC8 + local_r14 * 4)) != 0) goto loc_004C984A;
loc_004C974B:
    Arg1 = 0;
    if ((*(uint32_t *)(arg1 + local_r13 * 1 + 0x17C)) <= 0) goto loc_004C977B;
    result = (*(uint64_t *)(arg1 + local_r13 * 1 + 0x188)) + (16);
loc_004C9763:
    if (0 >= (*(uint32_t *)(v_stack_mC8))) goto loc_004C977B;
    Arg1 = (uint32_t)((Arg1) + 1);
    result = (result) + (24);
    if (((uint32_t)(Arg1)) < (*(uint32_t *)(arg1 + local_r13 * 1 + 0x17C))) goto loc_004C9763;
loc_004C977B:
    if (((uint32_t)((uint32_t)(v_stack_m19C))) == -1) goto loc_004C97E2;
    if (0 != ((uint32_t)((uint32_t)(v_stack_m19C)))) goto loc_004C97E2;
    result = (uint32_t)(v_stack_m19C);
    local_rdi = 0;
    if ((*(uint32_t *)(v_stack_mC8)) >= = 0) {
        local_rdi = v_stack_m180;
        local_rdi = (local_rdi) + (200);
        Arg1 = local_rdi;
        result = KeAcquireSpinLockAtDpcLevel(Arg1, 1, v_stack_mC8, 0);
        Arg2 = 2;
        Arg1 = local_rdi;
        result = PopFxReinitializeAccountingInstance(Arg1, Arg2, v_stack_mC8, 0);
        result = *(uint32_t *)(v_stack_mC8);
        Arg1 = local_rdi;
        *(uint32_t *)(local_rdi + 0xC) = (uint32_t)(result);
        *(uint64_t *)(local_rdi + 0x18) = result;
        *(uint8_t *)(local_rdi + 0x8) = 1;
        result = KxReleaseSpinLock(Arg1, Arg2, v_stack_mC8, 0);
        local_rdi = 1;
        Arg2 = v_stack_m198;
    }
    local_r12 = (v_stack_mC8) + (4);
    Arg2 = (uint32_t)((Arg2) + (Arg2));
    local_r14 = (uint32_t)((local_r14) + 1);
    goto loc_004C971A;
loc_004C97F0:
loc_004C97F5:
    a4 = (Arg1 + 384) + (local_r13);
    Arg1 = 0;
    result = PopPepUpdateIdleStateRefCount(Arg1, (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + local_r13 * 1 + 0x188) + (uint32_t)(*(uint32_t *)(arg1 + local_r13 * 1 + 0x170)) + (uint32_t)(*(uint32_t *)(arg1 + local_r13 * 1 + 0x170)) * 2 * 8 + 0x10)), 1, a4);
    if ((uint8_t)(local_rdi) != 0) goto loc_004C9837;
    goto loc_004C9843;
loc_004C9837:
loc_004C9843:
    local_rsi = (uint32_t)((local_rsi) + 1);
    goto loc_004C96BE;
loc_004C984A:
    result = PopFxBugCheck((uint32_t)(0x621ULL), *(uint64_t *)(arg1 + 0x20), (uint32_t)((uint32_t)(local_rsi)), a4);
loc_004C985B:
    local_rsi = 0;
    if ((*(uint8_t *)(arg1 + 0x7C)) != 0) goto loc_004C9871;
loc_004C9868:
    if ((*(uint8_t *)(arg1 + 0xBC)) != 0) {
        *(uint32_t *)(arg1 + 0xAC) = 2;
    }
    result = ExReleaseSpinLockExclusive(Arg1 + 64, (uint8_t)(v_stack_m1A8), (uint32_t)((uint32_t)(local_rsi)), a4);
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, (uint8_t)(v_stack_m1A8), (uint32_t)((uint32_t)(local_rsi)), a4);
    local_rsp = (local_rsp) + (400);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x40` | `64` | `R` |
| `Arg1` | `+ 0x7C` | `8` | `R` |
| `Arg1` | `+ 0x8C + rax*4` | `32` | `R` |
| `Arg1` | `+ 0x90` | `64` | `R` |
| `Arg1` | `+ 0x90 + rax*4` | `32` | `R/W` |
| `Arg1` | `+ 0x98` | `32` | `R` |
| `Arg1` | `+ 0x9C` | `64` | `W` |
| `Arg1` | `+ 0xA4` | `32` | `W` |
| `Arg1` | `+ 0xA8` | `32` | `R` |
| `Arg1` | `+ 0xAC` | `32` | `R` |
| `Arg1` | `+ 0xAC` | `32` | `W` |
| `Arg1` | `+ 0xB4` | `32` | `R` |
| `Arg1` | `+ 0xB8` | `64` | `R` |
| `Arg1` | `+ 0xBC` | `8` | `R` |
| `Arg1` | `+ 0xBC` | `8` | `W` |
| `Arg1` | `+ 0x170 + r13*1` | `32` | `R` |
| `Arg1` | `+ 0x17C + r13*1` | `32` | `R` |
| `Arg1` | `+ 0x180` | `64` | `R` |
| `Arg1` | `+ 0x188 + r13*1` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004C9350&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
