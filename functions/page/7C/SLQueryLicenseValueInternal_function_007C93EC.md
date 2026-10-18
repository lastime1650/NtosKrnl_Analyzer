# SLQueryLicenseValueInternal

- RVA: `0x007C93EC`–`0x007C9BD3` (길이 `2,023` bytes)
- VA: `0x00000001407C93EC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D4E90`
- 디코드: `442`개 명령, `2,023/2,023` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **26**; 고유 호출 대상: **18**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **12**

### Outgoing calls
- `0x007C94ED` → [sub_007C87A4](Unknown_function_007C87A4.md) (function, `0x007C87A4`)
- `0x007C95AF` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (function, `0x006C6B10`)
- `0x007C9630` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x007C9650` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)
- `0x007C969A` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x007C9726` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x007C972E` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x007C9733` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x007C97A4` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x007C97B3` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x007C97C5` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x007C980C` → [sub_004BA83C](../../text/4B/Unknown_function_004BA83C.md) (function, `0x004BA83C`)
- `0x007C983F` → [RtlEqualUnicodeString](../93/RtlEqualUnicodeString_function_00932A20.md) (function, `0x00932A20`)
- `0x007C9862` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x007C9890` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x007C991A` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (function, `0x00500080`)
- `0x007C9947` → [SLGetSubscriptionPfn](SLGetSubscriptionPfn_function_007C9108.md) (function, `0x007C9108`)
- `0x007C99A6` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x007C9A11` → [sub_004BA83C](../../text/4B/Unknown_function_004BA83C.md) (function, `0x004BA83C`)
- `0x007C9A43` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x007C9A5C` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x007C9A81` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x007C9A89` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x007C9A8E` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x007C9B2E` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (function, `0x006C6B10`)
- `0x007C9B9F` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [NtQueryLicenseValue](../96/NtQueryLicenseValue_function_0096BCC0.md) at `0x0096BFDA`
- [sub_0096BFF0](../96/Unknown_function_0096BFF0.md) at `0x0096C04A`

### Static image references
- `0x007C93FF` → RVA `0x00E0A740` (`.data`; read)
- `0x007C9513` → RVA `0x00B4AAB0` (`PAGE`; read)
- `0x007C9802` → RVA `0x00B4B510` (`PAGE`; read)
- `0x007C9817` → RVA `0x00FD8398` (`PAGEDATA`; read)
- `0x007C9835` → RVA `0x00B4B520` (`PAGE`; read)
- `0x007C9898` → RVA `0x006D0290` (` ?? ::FNODOBFM::`string'`; read)
- `0x007C98A7` → RVA `0x006D01B0` (` ?? ::FNODOBFM::`string'`; read)
- `0x007C98B6` → RVA `0x006D0150` (` ?? ::FNODOBFM::`string'`; read)
- `0x007C98C5` → RVA `0x006D0220` (` ?? ::FNODOBFM::`string'`; read)
- `0x007C98D4` → RVA `0x006D01F0` (` ?? ::FNODOBFM::`string'`; read)
- `0x007C98E3` → RVA `0x006D0120` (` ?? ::FNODOBFM::`string'`; read)
- `0x007C98F2` → RVA `0x006D00A0` (` ?? ::FNODOBFM::`string'`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **23**
  - `0x007C95AF` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (`PAGE` → `.text`)
  - `0x007C9630` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x007C9650` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (`PAGE` → `.text`)
  - `0x007C969A` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x007C9726` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x007C972E` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x007C9733` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x007C97A4` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x007C97B3` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x007C97C5` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x007C980C` → [sub_004BA83C](../../text/4B/Unknown_function_004BA83C.md) (`PAGE` → `.text`)
  - `0x007C9862` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x007C9890` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x007C991A` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (`PAGE` → `.text`)
  - `0x007C99A6` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x007C9A11` → [sub_004BA83C](../../text/4B/Unknown_function_004BA83C.md) (`PAGE` → `.text`)
  - `0x007C9A43` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x007C9A5C` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x007C9A81` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x007C9A89` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x007C9A8E` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x007C9B2E` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (`PAGE` → `.text`)
  - `0x007C9B9F` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007C93EC  40 53                           push rbx
007C93EE  56                              push rsi
007C93EF  57                              push rdi
007C93F0  41 54                           push r12
007C93F2  41 55                           push r13
007C93F4  41 56                           push r14
007C93F6  41 57                           push r15
007C93F8  48 81 EC D0 01 00 00            sub rsp, 0x1d0
007C93FF  48 8B 05 3A 13 64 00            mov rax, qword ptr [rip + 0x64133a]
007C9406  48 33 C4                        xor rax, rsp
007C9409  48 89 84 24 C0 01 00 00         mov qword ptr [rsp + 0x1c0], rax
007C9411  4C 89 8C 24 90 00 00 00         mov qword ptr [rsp + 0x90], r9
007C9419  4C 89 84 24 98 00 00 00         mov qword ptr [rsp + 0x98], r8
007C9421  4C 8B FA                        mov r15, rdx
007C9424  48 89 94 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], rdx
007C942C  48 8B C1                        mov rax, rcx
007C942F  48 89 8C 24 80 00 00 00         mov qword ptr [rsp + 0x80], rcx
007C9437  48 89 8C 24 E8 00 00 00         mov qword ptr [rsp + 0xe8], rcx
007C943F  48 89 94 24 F0 00 00 00         mov qword ptr [rsp + 0xf0], rdx
007C9447  4C 89 84 24 F8 00 00 00         mov qword ptr [rsp + 0xf8], r8
007C944F  4C 89 8C 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], r9
007C9457  48 8B 8C 24 38 02 00 00         mov rcx, qword ptr [rsp + 0x238]
007C945F  48 89 4C 24 70                  mov qword ptr [rsp + 0x70], rcx
007C9464  33 F6                           xor esi, esi
007C9466  89 74 24 64                     mov dword ptr [rsp + 0x64], esi
007C946A  0F 57 C0                        xorps xmm0, xmm0
007C946D  0F 11 84 24 D0 00 00 00         movups xmmword ptr [rsp + 0xd0], xmm0
007C9475  40 88 74 24 61                  mov byte ptr [rsp + 0x61], sil
007C947A  44 8B EE                        mov r13d, esi
007C947D  48 89 74 24 78                  mov qword ptr [rsp + 0x78], rsi
007C9482  48 89 B4 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rsi
007C948A  89 B4 24 8C 00 00 00            mov dword ptr [rsp + 0x8c], esi
007C9491  89 B4 24 A4 00 00 00            mov dword ptr [rsp + 0xa4], esi
007C9498  44 8D 76 01                     lea r14d, [rsi + 1]
007C949C  44 88 74 24 60                  mov byte ptr [rsp + 0x60], r14b
007C94A1  48 85 D2                        test rdx, rdx
007C94A4  0F 84 1B 07 00 00               je 0x1407c9bc5
007C94AA  48 85 C9                        test rcx, rcx
007C94AD  0F 84 12 07 00 00               je 0x1407c9bc5
007C94B3  8B FE                           mov edi, esi
007C94B5  89 74 24 64                     mov dword ptr [rsp + 0x64], esi
007C94B9  48 8D 4A 08                     lea rcx, [rdx + 8]
007C94BD  48 89 8C 24 08 01 00 00         mov qword ptr [rsp + 0x108], rcx
007C94C5  48 39 31                        cmp qword ptr [rcx], rsi
007C94C8  0F 84 F7 06 00 00               je 0x1407c9bc5
007C94CE  8D 4E 02                        lea ecx, [rsi + 2]
007C94D1  66 39 0A                        cmp word ptr [rdx], cx
007C94D4  0F 82 EB 06 00 00               jb 0x1407c9bc5
007C94DA  44 88 B4 24 D0 00 00 00         mov byte ptr [rsp + 0xd0], r14b
007C94E2  48 89 94 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], rdx
007C94EA  48 8B C8                        mov rcx, rax
007C94ED  E8 B2 F2 FF FF                  call 0x1407c87a4
007C94F2  89 84 24 A0 00 00 00            mov dword ptr [rsp + 0xa0], eax
007C94F9  48 89 B4 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rsi
007C9501  40 88 74 24 68                  mov byte ptr [rsp + 0x68], sil
007C9506  41 8B D6                        mov edx, r14d
007C9509  89 94 24 88 00 00 00            mov dword ptr [rsp + 0x88], edx
007C9510  44 8B E6                        mov r12d, esi
007C9513  4C 8D 05 96 15 38 00            lea r8, [rip + 0x381596]
007C951A  41 83 FC 0E                     cmp r12d, 0xe
007C951E  0F 83 CF 00 00 00               jae 0x1407c95f3
007C9524  41 8B C4                        mov eax, r12d
007C9527  48 8D 1C 80                     lea rbx, [rax + rax*4]
007C952B  48 8B 8C 24 D8 00 00 00         mov rcx, qword ptr [rsp + 0xd8]
007C9533  0F B7 01                        movzx eax, word ptr [rcx]
007C9536  45 0F B7 44 D8 08               movzx r8d, word ptr [r8 + rbx*8 + 8]
007C953C  66 41 3B C0                     cmp ax, r8w
007C9540  75 7F                           jne 0x1407c95c1
007C9542  D1 E8                           shr eax, 1
007C9544  74 56                           je 0x1407c959c
007C9546  4C 8D 94 24 50 01 00 00         lea r10, [rsp + 0x150]
007C954E  4C 8D 9C 24 50 01 00 00         lea r11, [rsp + 0x150]
007C9556  4C 8B 49 08                     mov r9, qword ptr [rcx + 8]
007C955A  4D 2B CB                        sub r9, r11
007C955D  44 8B D8                        mov r11d, eax
007C9560  41 BF 55 55 00 00               mov r15d, 0x5555
007C9566  0F B7 CA                        movzx ecx, dx
007C9569  66 C1 E1 08                     shl cx, 8
007C956D  41 8D 04 16                     lea eax, [r14 + rdx]
007C9571  66 0B C8                        or cx, ax
007C9574  66 41 0B CF                     or cx, r15w
007C9578  66 43 33 0C 11                  xor cx, word ptr [r9 + r10]
007C957D  66 41 89 0A                     mov word ptr [r10], cx
007C9581  83 C2 02                        add edx, 2
007C9584  4D 8D 52 02                     lea r10, [r10 + 2]
007C9588  4D 2B DE                        sub r11, r14
007C958B  75 D9                           jne 0x1407c9566
007C958D  89 94 24 88 00 00 00            mov dword ptr [rsp + 0x88], edx
007C9594  4C 8B BC 24 C0 00 00 00         mov r15, qword ptr [rsp + 0xc0]
007C959C  48 8D 05 0D 15 38 00            lea rax, [rip + 0x38150d]
007C95A3  48 8B 14 D8                     mov rdx, qword ptr [rax + rbx*8]
007C95A7  48 8D 8C 24 50 01 00 00         lea rcx, [rsp + 0x150]
007C95AF  E8 5C D5 EF FF                  call 0x1406c6b10
007C95B4  85 C0                           test eax, eax
007C95B6  74 1B                           je 0x1407c95d3
007C95B8  8B 94 24 88 00 00 00            mov edx, dword ptr [rsp + 0x88]
007C95BF  EB 0A                           jmp 0x1407c95cb
007C95C1  41 03 D0                        add edx, r8d
007C95C4  89 94 24 88 00 00 00            mov dword ptr [rsp + 0x88], edx
007C95CB  45 03 E6                        add r12d, r14d
007C95CE  E9 40 FF FF FF                  jmp 0x1407c9513
007C95D3  4C 8D 05 D6 14 38 00            lea r8, [rip + 0x3814d6]
007C95DA  49 8B 44 D8 10                  mov rax, qword ptr [r8 + rbx*8 + 0x10]
007C95DF  48 89 84 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rax
007C95E7  45 8A 6C D8 20                  mov r13b, byte ptr [r8 + rbx*8 + 0x20]
007C95EC  44 88 6C 24 68                  mov byte ptr [rsp + 0x68], r13b
007C95F1  EB 03                           jmp 0x1407c95f6
007C95F3  48 8B C6                        mov rax, rsi
007C95F6  48 83 CB FF                     or rbx, 0xffffffffffffffff
007C95FA  48 85 C0                        test rax, rax
007C95FD  0F 84 3B 01 00 00               je 0x1407c973e
007C9603  45 84 ED                        test r13b, r13b
007C9606  74 5E                           je 0x1407c9666
007C9608  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
007C9611  66 01 98 E4 01 00 00            add word ptr [rax + 0x1e4], bx
007C9618  90                              nop
007C9619  4C 8B A4 24 80 00 00 00         mov r12, qword ptr [rsp + 0x80]
007C9621  49 81 C4 F8 B6 00 00            add r12, 0xb6f8
007C9628  45 33 C0                        xor r8d, r8d
007C962B  33 D2                           xor edx, edx
007C962D  49 8B CC                        mov rcx, r12
007C9630  E8 FB 6B A4 FF                  call 0x140210230
007C9635  48 8B F8                        mov rdi, rax
007C9638  8D 4B 12                        lea ecx, [rbx + 0x12]
007C963B  33 C0                           xor eax, eax
007C963D  F0 49 0F B1 0C 24               lock cmpxchg qword ptr [r12], rcx
007C9643  74 10                           je 0x1407c9655
007C9645  4D 8B CC                        mov r9, r12
007C9648  4C 8B C7                        mov r8, rdi
007C964B  33 D2                           xor edx, edx
007C964D  49 8B CC                        mov rcx, r12
007C9650  E8 F7 6D A4 FF                  call 0x14021044c
007C9655  48 8B 84 24 A8 00 00 00         mov rax, qword ptr [rsp + 0xa8]
007C965D  48 85 FF                        test rdi, rdi
007C9660  74 04                           je 0x1407c9666
007C9662  44 88 77 0A                     mov byte ptr [rdi + 0xa], r14b
007C9666  48 8D 4C 24 61                  lea rcx, [rsp + 0x61]
007C966B  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
007C9670  4C 8B 64 24 70                  mov r12, qword ptr [rsp + 0x70]
007C9675  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
007C967A  44 8B 8C 24 30 02 00 00         mov r9d, dword ptr [rsp + 0x230]
007C9682  4C 8B 84 24 90 00 00 00         mov r8, qword ptr [rsp + 0x90]
007C968A  48 8B 94 24 98 00 00 00         mov rdx, qword ptr [rsp + 0x98]
007C9692  48 8B 8C 24 80 00 00 00         mov rcx, qword ptr [rsp + 0x80]
007C969A  E8 31 14 EF FF                  call 0x1406baad0
007C969F  8B F8                           mov edi, eax
007C96A1  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
007C96A5  EB 5C                           jmp 0x1407c9703
007C96A7  8B F8                           mov edi, eax
007C96A9  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
007C96AD  C6 44 24 61 01                  mov byte ptr [rsp + 0x61], 1
007C96B2  33 F6                           xor esi, esi
007C96B4  44 8D 76 01                     lea r14d, [rsi + 1]
007C96B8  48 83 CB FF                     or rbx, 0xffffffffffffffff
007C96BC  48 89 74 24 78                  mov qword ptr [rsp + 0x78], rsi
007C96C1  44 8A 6C 24 68                  mov r13b, byte ptr [rsp + 0x68]
007C96C6  48 8B 84 24 E8 00 00 00         mov rax, qword ptr [rsp + 0xe8]
007C96CE  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
007C96D6  4C 8B BC 24 F0 00 00 00         mov r15, qword ptr [rsp + 0xf0]
007C96DE  48 8B 84 24 F8 00 00 00         mov rax, qword ptr [rsp + 0xf8]
007C96E6  48 89 84 24 98 00 00 00         mov qword ptr [rsp + 0x98], rax
007C96EE  48 8B 84 24 C8 00 00 00         mov rax, qword ptr [rsp + 0xc8]
007C96F6  48 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], rax
007C96FE  4C 8B 64 24 70                  mov r12, qword ptr [rsp + 0x70]
007C9703  45 84 ED                        test r13b, r13b
007C9706  4C 8B AC 24 80 00 00 00         mov r13, qword ptr [rsp + 0x80]
007C970E  74 3B                           je 0x1407c974b
007C9710  49 8D BD F8 B6 00 00            lea rdi, [r13 + 0xb6f8]
007C9717  B8 11 00 00 00                  mov eax, 0x11
007C971C  F0 48 0F B1 37                  lock cmpxchg qword ptr [rdi], rsi
007C9721  74 08                           je 0x1407c972b
007C9723  48 8B CF                        mov rcx, rdi
007C9726  E8 15 9D A9 FF                  call 0x140263440
007C972B  48 8B CF                        mov rcx, rdi
007C972E  E8 CD 7E B1 FF                  call 0x1402e1600
007C9733  E8 78 41 A9 FF                  call 0x14025d8b0
007C9738  8B 7C 24 64                     mov edi, dword ptr [rsp + 0x64]
007C973C  EB 0D                           jmp 0x1407c974b
007C973E  4C 8B AC 24 80 00 00 00         mov r13, qword ptr [rsp + 0x80]
007C9746  4C 8B 64 24 70                  mov r12, qword ptr [rsp + 0x70]
007C974B  40 38 74 24 61                  cmp byte ptr [rsp + 0x61], sil
007C9750  74 2F                           je 0x1407c9781
007C9752  85 FF                           test edi, edi
007C9754  78 17                           js 0x1407c976d
007C9756  B9 23 00 00 C0                  mov ecx, 0xc0000023
007C975B  8B 84 24 30 02 00 00            mov eax, dword ptr [rsp + 0x230]
007C9762  41 39 04 24                     cmp dword ptr [r12], eax
007C9766  0F 47 F9                        cmova edi, ecx
007C9769  89 7C 24 64                     mov dword ptr [rsp + 0x64], edi
007C976D  4C 8B 6C 24 78                  mov r13, qword ptr [rsp + 0x78]
007C9772  EB 0B                           jmp 0x1407c977f
007C9774  8B F8                           mov edi, eax
007C9776  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
007C977A  33 F6                           xor esi, esi
007C977C  44 8B EE                        mov r13d, esi
007C977F  EB 14                           jmp 0x1407c9795
007C9781  8B BC 24 A0 00 00 00            mov edi, dword ptr [rsp + 0xa0]
007C9788  85 FF                           test edi, edi
007C978A  79 52                           jns 0x1407c97de
007C978C  89 7C 24 64                     mov dword ptr [rsp + 0x64], edi
007C9790  4C 8B 6C 24 78                  mov r13, qword ptr [rsp + 0x78]
007C9795  48 8B 8C 24 B0 00 00 00         mov rcx, qword ptr [rsp + 0xb0]
007C979D  48 85 C9                        test rcx, rcx
007C97A0  74 07                           je 0x1407c97a9
007C97A2  33 D2                           xor edx, edx
007C97A4  E8 C7 90 3B 00                  call 0x140b82870
007C97A9  4D 85 ED                        test r13, r13
007C97AC  74 0A                           je 0x1407c97b8
007C97AE  33 D2                           xor edx, edx
007C97B0  49 8B CD                        mov rcx, r13
007C97B3  E8 B8 90 3B 00                  call 0x140b82870
007C97B8  8B C7                           mov eax, edi
007C97BA  48 8B 8C 24 C0 01 00 00         mov rcx, qword ptr [rsp + 0x1c0]
007C97C2  48 33 CC                        xor rcx, rsp
007C97C5  E8 76 2E EE FF                  call 0x1406ac640
007C97CA  48 81 C4 D0 01 00 00            add rsp, 0x1d0
007C97D1  41 5F                           pop r15
007C97D3  41 5E                           pop r14
007C97D5  41 5D                           pop r13
007C97D7  41 5C                           pop r12
007C97D9  5F                              pop rdi
007C97DA  5E                              pop rsi
007C97DB  5B                              pop rbx
007C97DC  C3                              ret
007C97DD  CC                              int3
007C97DE  89 74 24 64                     mov dword ptr [rsp + 0x64], esi
007C97E2  48 8D 84 24 A4 00 00 00         lea rax, [rsp + 0xa4]
007C97EA  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
007C97EF  C7 44 24 20 04 00 00 00         mov dword ptr [rsp + 0x20], 4
007C97F7  4C 8D 8C 24 8C 00 00 00         lea r9, [rsp + 0x8c]
007C97FF  45 33 C0                        xor r8d, r8d
007C9802  48 8D 15 07 1D 38 00            lea rdx, [rip + 0x381d07]
007C9809  49 8B CD                        mov rcx, r13
007C980C  E8 2B 10 CF FF                  call 0x1404ba83c
007C9811  8B F8                           mov edi, eax
007C9813  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
007C9817  48 83 3D 79 EB 80 00 00         cmp qword ptr [rip + 0x80eb79], 0
007C981F  0F 84 B0 01 00 00               je 0x1407c99d5
007C9825  39 B4 24 8C 00 00 00            cmp dword ptr [rsp + 0x8c], esi
007C982C  0F 84 A3 01 00 00               je 0x1407c99d5
007C9832  45 33 C0                        xor r8d, r8d
007C9835  48 8D 15 E4 1C 38 00            lea rdx, [rip + 0x381ce4]
007C983C  49 8B CF                        mov rcx, r15
007C983F  E8 DC 91 16 00                  call 0x140932a20
007C9844  84 C0                           test al, al
007C9846  0F 85 89 01 00 00               jne 0x1407c99d5
007C984C  45 0F B7 27                     movzx r12d, word ptr [r15]
007C9850  41 83 C4 02                     add r12d, 2
007C9854  41 8B D4                        mov edx, r12d
007C9857  B9 00 01 00 00                  mov ecx, 0x100
007C985C  41 B8 53 4C 53 20               mov r8d, 0x20534c53
007C9862  E8 89 88 3B 00                  call 0x140b820f0
007C9867  4C 8B E8                        mov r13, rax
007C986A  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
007C986F  48 85 C0                        test rax, rax
007C9872  75 0A                           jne 0x1407c987e
007C9874  BF 17 00 00 C0                  mov edi, 0xc0000017
007C9879  E9 4C 03 00 00                  jmp 0x1407c9bca
007C987E  45 0F B7 07                     movzx r8d, word ptr [r15]
007C9882  48 8B 94 24 08 01 00 00         mov rdx, qword ptr [rsp + 0x108]
007C988A  48 8B 12                        mov rdx, qword ptr [rdx]
007C988D  48 8B C8                        mov rcx, rax
007C9890  E8 AB CF EF FF                  call 0x1406c6840
007C9895  44 8A EE                        mov r13b, sil
007C9898  48 8D 05 F1 69 F0 FF            lea rax, [rip - 0xf960f]
007C989F  48 89 84 24 10 01 00 00         mov qword ptr [rsp + 0x110], rax
007C98A7  48 8D 05 02 69 F0 FF            lea rax, [rip - 0xf96fe]
007C98AE  48 89 84 24 18 01 00 00         mov qword ptr [rsp + 0x118], rax
007C98B6  48 8D 05 93 68 F0 FF            lea rax, [rip - 0xf976d]
007C98BD  48 89 84 24 20 01 00 00         mov qword ptr [rsp + 0x120], rax
007C98C5  48 8D 05 54 69 F0 FF            lea rax, [rip - 0xf96ac]
007C98CC  48 89 84 24 28 01 00 00         mov qword ptr [rsp + 0x128], rax
007C98D4  48 8D 05 15 69 F0 FF            lea rax, [rip - 0xf96eb]
007C98DB  48 89 84 24 30 01 00 00         mov qword ptr [rsp + 0x130], rax
007C98E3  48 8D 05 36 68 F0 FF            lea rax, [rip - 0xf97ca]
007C98EA  48 89 84 24 38 01 00 00         mov qword ptr [rsp + 0x138], rax
007C98F2  48 8D 05 A7 67 F0 FF            lea rax, [rip - 0xf9859]
007C98F9  48 89 84 24 40 01 00 00         mov qword ptr [rsp + 0x140], rax
007C9901  44 8B FE                        mov r15d, esi
007C9904  41 83 FF 07                     cmp r15d, 7
007C9908  73 21                           jae 0x1407c992b
007C990A  41 8B D7                        mov edx, r15d
007C990D  48 8B 94 D4 10 01 00 00         mov rdx, qword ptr [rsp + rdx*8 + 0x110]
007C9915  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
007C991A  E8 61 67 D3 FF                  call 0x140500080
007C991F  85 C0                           test eax, eax
007C9921  74 05                           je 0x1407c9928
007C9923  45 03 FE                        add r15d, r14d
007C9926  EB DC                           jmp 0x1407c9904
007C9928  45 8A EE                        mov r13b, r14b
007C992B  45 84 ED                        test r13b, r13b
007C992E  4C 8B AC 24 80 00 00 00         mov r13, qword ptr [rsp + 0x80]
007C9936  0F 85 99 00 00 00               jne 0x1407c99d5
007C993C  48 8D 94 24 B0 00 00 00         lea rdx, [rsp + 0xb0]
007C9944  49 8B CD                        mov rcx, r13
007C9947  E8 BC F7 FF FF                  call 0x1407c9108
007C994C  48 8B 05 45 EA 80 00            mov rax, qword ptr [rip + 0x80ea45]
007C9953  48 89 74 24 50                  mov qword ptr [rsp + 0x50], rsi
007C9958  48 8B 8C 24 98 00 00 00         mov rcx, qword ptr [rsp + 0x98]
007C9960  48 89 4C 24 48                  mov qword ptr [rsp + 0x48], rcx
007C9965  4C 8B 7C 24 70                  mov r15, qword ptr [rsp + 0x70]
007C996A  4C 89 7C 24 40                  mov qword ptr [rsp + 0x40], r15
007C996F  8B 8C 24 30 02 00 00            mov ecx, dword ptr [rsp + 0x230]
007C9976  89 4C 24 38                     mov dword ptr [rsp + 0x38], ecx
007C997A  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
007C9982  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
007C9987  44 89 64 24 28                  mov dword ptr [rsp + 0x28], r12d
007C998C  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
007C9991  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
007C9996  45 33 C9                        xor r9d, r9d
007C9999  45 33 C0                        xor r8d, r8d
007C999C  33 D2                           xor edx, edx
007C999E  48 8B 8C 24 B0 00 00 00         mov rcx, qword ptr [rsp + 0xb0]
007C99A6  E8 25 11 EF FF                  call 0x1406baad0
007C99AB  BA 00 00 00 80                  mov edx, 0x80000000
007C99B0  8D 0C 10                        lea ecx, [rax + rdx]
007C99B3  85 CA                           test edx, ecx
007C99B5  B9 23 00 00 C0                  mov ecx, 0xc0000023
007C99BA  75 04                           jne 0x1407c99c0
007C99BC  3B C1                           cmp eax, ecx
007C99BE  75 1A                           jne 0x1407c99da
007C99C0  8B F8                           mov edi, eax
007C99C2  39 B4 24 30 02 00 00            cmp dword ptr [rsp + 0x230], esi
007C99C9  0F 44 F9                        cmove edi, ecx
007C99CC  89 7C 24 64                     mov dword ptr [rsp + 0x64], edi
007C99D0  40 8A C6                        mov al, sil
007C99D3  EB 09                           jmp 0x1407c99de
007C99D5  4C 8B 7C 24 70                  mov r15, qword ptr [rsp + 0x70]
007C99DA  8A 44 24 60                     mov al, byte ptr [rsp + 0x60]
007C99DE  84 C0                           test al, al
007C99E0  0F 84 B1 00 00 00               je 0x1407c9a97
007C99E6  4C 89 7C 24 28                  mov qword ptr [rsp + 0x28], r15
007C99EB  8B 84 24 30 02 00 00            mov eax, dword ptr [rsp + 0x230]
007C99F2  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
007C99F6  4C 8B 8C 24 90 00 00 00         mov r9, qword ptr [rsp + 0x90]
007C99FE  4C 8B 84 24 98 00 00 00         mov r8, qword ptr [rsp + 0x98]
007C9A06  48 8D 94 24 D0 00 00 00         lea rdx, [rsp + 0xd0]
007C9A0E  49 8B CD                        mov rcx, r13
007C9A11  E8 26 0E CF FF                  call 0x1404ba83c
007C9A16  8B F8                           mov edi, eax
007C9A18  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
007C9A1C  3D 3E 00 00 C0                  cmp eax, 0xc000003e
007C9A21  75 74                           jne 0x1407c9a97
007C9A23  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
007C9A2C  66 01 98 E4 01 00 00            add word ptr [rax + 0x1e4], bx
007C9A33  90                              nop
007C9A34  49 8D BD F8 B6 00 00            lea rdi, [r13 + 0xb6f8]
007C9A3B  45 33 C0                        xor r8d, r8d
007C9A3E  33 D2                           xor edx, edx
007C9A40  48 8B CF                        mov rcx, rdi
007C9A43  E8 E8 67 A4 FF                  call 0x140210230
007C9A48  4C 8B F8                        mov r15, rax
007C9A4B  F0 48 0F BA 2F 00               lock bts qword ptr [rdi], 0
007C9A51  73 0E                           jae 0x1407c9a61
007C9A53  4C 8B C7                        mov r8, rdi
007C9A56  48 8B D0                        mov rdx, rax
007C9A59  48 8B CF                        mov rcx, rdi
007C9A5C  E8 2F 62 A4 FF                  call 0x14020fc90
007C9A61  4D 85 FF                        test r15, r15
007C9A64  74 04                           je 0x1407c9a6a
007C9A66  45 88 77 0A                     mov byte ptr [r15 + 0xa], r14b
007C9A6A  45 88 B5 90 B7 00 00            mov byte ptr [r13 + 0xb790], r14b
007C9A71  F0 48 0F C1 1F                  lock xadd qword ptr [rdi], rbx
007C9A76  80 E3 06                        and bl, 6
007C9A79  80 FB 02                        cmp bl, 2
007C9A7C  75 08                           jne 0x1407c9a86
007C9A7E  48 8B CF                        mov rcx, rdi
007C9A81  E8 4A C3 A9 FF                  call 0x140265dd0
007C9A86  48 8B CF                        mov rcx, rdi
007C9A89  E8 72 7B B1 FF                  call 0x1402e1600
007C9A8E  E8 1D 3E A9 FF                  call 0x14025d8b0
007C9A93  8B 7C 24 64                     mov edi, dword ptr [rsp + 0x64]
007C9A97  4C 8B E6                        mov r12, rsi
007C9A9A  45 8B FE                        mov r15d, r14d
007C9A9D  8B DE                           mov ebx, esi
007C9A9F  83 FB 0E                        cmp ebx, 0xe
007C9AA2  0F 83 9F 00 00 00               jae 0x1407c9b47
007C9AA8  8B C3                           mov eax, ebx
007C9AAA  4C 8D 2C 80                     lea r13, [rax + rax*4]
007C9AAE  48 8B 8C 24 D8 00 00 00         mov rcx, qword ptr [rsp + 0xd8]
007C9AB6  0F B7 01                        movzx eax, word ptr [rcx]
007C9AB9  4C 8D 1D F0 0F 38 00            lea r11, [rip + 0x380ff0]
007C9AC0  43 0F B7 54 EB 08               movzx edx, word ptr [r11 + r13*8 + 8]
007C9AC6  66 3B C2                        cmp ax, dx
007C9AC9  0F 85 EB 00 00 00               jne 0x1407c9bba
007C9ACF  D1 E8                           shr eax, 1
007C9AD1  74 4C                           je 0x1407c9b1f
007C9AD3  4C 8D 84 24 50 01 00 00         lea r8, [rsp + 0x150]
007C9ADB  4C 8D 94 24 50 01 00 00         lea r10, [rsp + 0x150]
007C9AE3  4C 8B 49 08                     mov r9, qword ptr [rcx + 8]
007C9AE7  4D 2B CA                        sub r9, r10
007C9AEA  44 8B D0                        mov r10d, eax
007C9AED  41 BC 55 55 00 00               mov r12d, 0x5555
007C9AF3  41 0F B7 CF                     movzx ecx, r15w
007C9AF7  66 C1 E1 08                     shl cx, 8
007C9AFB  43 8D 04 3E                     lea eax, [r14 + r15]
007C9AFF  66 0B C8                        or cx, ax
007C9B02  66 41 0B CC                     or cx, r12w
007C9B06  66 43 33 0C 01                  xor cx, word ptr [r9 + r8]
007C9B0B  66 41 89 08                     mov word ptr [r8], cx
007C9B0F  41 83 C7 02                     add r15d, 2
007C9B13  4D 8D 40 02                     lea r8, [r8 + 2]
007C9B17  4D 2B D6                        sub r10, r14
007C9B1A  75 D7                           jne 0x1407c9af3
007C9B1C  4C 8B E6                        mov r12, rsi
007C9B1F  4C 8B C2                        mov r8, rdx
007C9B22  4B 8B 14 EB                     mov rdx, qword ptr [r11 + r13*8]
007C9B26  48 8D 8C 24 50 01 00 00         lea rcx, [rsp + 0x150]
007C9B2E  E8 DD CF EF FF                  call 0x1406c6b10
007C9B33  85 C0                           test eax, eax
007C9B35  0F 85 82 00 00 00               jne 0x1407c9bbd
007C9B3B  48 8D 05 6E 0F 38 00            lea rax, [rip + 0x380f6e]
007C9B42  4E 8B 64 E8 18                  mov r12, qword ptr [rax + r13*8 + 0x18]
007C9B47  4D 85 E4                        test r12, r12
007C9B4A  0F 84 40 FC FF FF               je 0x1407c9790
007C9B50  85 FF                           test edi, edi
007C9B52  79 14                           jns 0x1407c9b68
007C9B54  81 FF 34 00 00 C0               cmp edi, 0xc0000034
007C9B5A  74 0C                           je 0x1407c9b68
007C9B5C  81 FF 25 02 00 C0               cmp edi, 0xc0000225
007C9B62  0F 85 28 FC FF FF               jne 0x1407c9790
007C9B68  48 8D 44 24 61                  lea rax, [rsp + 0x61]
007C9B6D  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
007C9B72  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
007C9B77  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
007C9B7C  44 8B 8C 24 30 02 00 00         mov r9d, dword ptr [rsp + 0x230]
007C9B84  4C 8B 84 24 90 00 00 00         mov r8, qword ptr [rsp + 0x90]
007C9B8C  48 8B 94 24 98 00 00 00         mov rdx, qword ptr [rsp + 0x98]
007C9B94  48 8B 8C 24 80 00 00 00         mov rcx, qword ptr [rsp + 0x80]
007C9B9C  49 8B C4                        mov rax, r12
007C9B9F  E8 2C 0F EF FF                  call 0x1406baad0
007C9BA4  40 38 74 24 61                  cmp byte ptr [rsp + 0x61], sil
007C9BA9  0F 84 E1 FB FF FF               je 0x1407c9790
007C9BAF  8B F8                           mov edi, eax
007C9BB1  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
007C9BB5  E9 D6 FB FF FF                  jmp 0x1407c9790
007C9BBA  44 03 FA                        add r15d, edx
007C9BBD  41 03 DE                        add ebx, r14d
007C9BC0  E9 DA FE FF FF                  jmp 0x1407c9a9f
007C9BC5  BF 0D 00 00 C0                  mov edi, 0xc000000d
007C9BCA  89 7C 24 64                     mov dword ptr [rsp + 0x64], edi
007C9BCE  E9 C2 FB FF FF                  jmp 0x1407c9795
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SLQueryLicenseValueInternal(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned int a5, __int64 a6)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m160;
    unsigned int v_stack_m164;
    unsigned int v_stack_m168;
    unsigned __int64 v_stack_m170;
    unsigned __int64 v_stack_m178;
    unsigned int v_stack_m17C;
    unsigned int v_stack_m180;
    unsigned __int64 v_stack_m188;
    unsigned __int64 v_stack_m190;
    unsigned __int64 v_stack_m198;
    unsigned __int8 v_stack_m1A0;
    unsigned int v_stack_m1A4;
    unsigned __int8 v_stack_m1A7;
    unsigned __int8 v_stack_m1A8;
    unsigned __int64 v_stack_m1E0;
    unsigned __int64 v_stack_m1E8;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_p108;
    unsigned __int64 v_stack_p110;
    unsigned __int64 v_stack_p118;
    unsigned __int64 v_stack_p120;
    unsigned __int64 v_stack_p128;
    unsigned __int64 v_stack_p130;
    unsigned __int64 v_stack_p138;
    unsigned __int64 v_stack_p140;
    unsigned __int64 v_stack_p150;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned int v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int8 v_stack_p60;
    unsigned __int64 v_stack_p61;
    unsigned int v_stack_p64;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p78;
    unsigned __int64 v_stack_p80;
    unsigned __int64 v_stack_p8C;
    unsigned __int64 v_stack_p90;
    unsigned __int64 v_stack_p98;
    unsigned __int64 v_stack_pA4;
    unsigned __int64 v_stack_pB0;
    unsigned __int64 v_stack_pD0;
    unsigned __int64 v_stack_pD8;

    v_rsp = (v_rsp) - (464);
    result = (*(unsigned __int64 *)(v_rip + 6558522)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m178 = a4;
    v_stack_m170 = a3;
    v_stack_m148 = a2;
    v_stack_m188 = a1;
    v_stack_m120 = a1;
    v_stack_m118 = a2;
    v_stack_m110 = a3;
    v_stack_m140 = a4;
    v_stack_m198 = a6;
    v_rsi = 0;
    v_stack_m1A4 = 0;
    v_stack_m138 = v_xmm0;
    v_stack_m1A7 = 0;
    v_stack_m190 = 0;
    v_stack_m158 = 0;
    v_stack_m17C = 0;
    v_stack_m164 = 0;
    v_stack_m1A8 = (unsigned __int8)(v_rsi + 1);
    if (a2 == 0) goto loc_007C9BC5;
    if (a6 == 0) goto loc_007C9BC5;
    v_stack_m1A4 = 0;
    v_stack_m100 = a2 + 8;
    if ((*(unsigned __int64 *)(a2 + 8)) == 0) goto loc_007C9BC5;
    if ((*(unsigned __int16 *)(a2)) < ((unsigned __int16)(v_rsi + 2))) goto loc_007C9BC5;
    v_stack_m138 = (unsigned __int8)(v_rsi + 1);
    v_stack_m130 = a2;
    result = sub_007C87A4(a1, a2, a3, a4);
    v_stack_m168 = (unsigned int)(result);
    v_stack_m160 = 0;
    v_stack_m1A0 = 0;
    v_stack_m180 = (unsigned int)((unsigned int)((unsigned int)(v_rsi + 1)));
loc_007C9513:
    if (0 >= 14) goto loc_007C95F3;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_stack_m130))) != ((unsigned __int16)(*(unsigned __int16 *)(v_rip + 3675542 + 0 + 0 * 4 * 8 + 8)))) goto loc_007C95C1;
    result = (unsigned int)((*(unsigned __int16 *)(v_stack_m130)) >> (1));
    if (condition_is_equal) goto loc_007C959C;
    a4 = (*(unsigned __int64 *)(v_stack_m130 + 8)) - (v_stack_mB8);
loc_007C9566:
    a1 = (unsigned __int16)(((unsigned __int16)((unsigned int)((unsigned int)(v_rsi + 1)))) << (8));
    a1 = (unsigned __int16)((a1) | ((unsigned __int16)(v_rsi + 1 + (unsigned int)((unsigned int)(v_rsi + 1)) * 1)));
    a1 = (unsigned __int16)((a1) | ((unsigned __int16)((unsigned int)(0x5555ULL))));
    a1 = (unsigned __int16)((a1) ^ (*(unsigned __int16 *)(a4 + v_stack_mB8 * 1)));
    *(unsigned __int16 *)(v_stack_mB8) = (unsigned __int16)(a1);
    a2 = (unsigned int)(((unsigned int)((unsigned int)(v_rsi + 1))) + (2));
    v_r11 = ((unsigned int)((unsigned int)(result))) - (v_rsi + 1);
    if (condition_is_not_equal) goto loc_007C9566;
    v_stack_m180 = (unsigned int)(a2);
loc_007C959C:
    result = memcmp(v_stack_mB8, *(unsigned __int64 *)(v_rip + 3675405 + 0 + 0 * 4 * 8), *(unsigned __int16 *)(v_rip + 3675542 + 0 + 0 * 4 * 8 + 8), a4);
    if ((unsigned int)(result) == 0) goto loc_007C95D3;
    goto loc_007C95CB;
loc_007C95C1:
    a2 = (unsigned int)(((unsigned int)(v_stack_m180)) + ((unsigned int)(*(unsigned __int16 *)(v_rip + 3675542 + 0 + 0 * 4 * 8 + 8))));
    v_stack_m180 = (unsigned int)(a2);
loc_007C95CB:
    v_r12 = (unsigned int)((0) + ((unsigned int)(v_rsi + 1)));
    goto loc_007C9513;
loc_007C95D3:
    v_stack_m160 = *(unsigned __int64 *)(v_rip + 3675350 + 0 + 0 * 4 * 8 + 16);
    v_stack_m1A0 = (unsigned __int8)(*(unsigned __int8 *)(v_rip + 3675350 + 0 + 0 * 4 * 8 + 32));
    goto loc_007C95F6;
loc_007C95F3:
loc_007C95F6:
    v_rbx = (0 + 0 * 4) | (-1);
    if (0 == 0) goto loc_007C973E;
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rip + 3675350 + 0 + 0 * 4 * 8 + 32)) == 0) goto loc_007C9666;
    v_r12 = (v_stack_m188) + (0xB6F8ULL);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_r12, a2, a3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = v_r12;
        a3 = 0;
        a2 = 0;
        a1 = v_r12;
        result = ExfAcquirePushLockSharedEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = (unsigned __int8)(v_rsi + 1);
    }
    v_stack_m1E0 = v_stack_m1A7;
    v_stack_m1E8 = v_stack_m198;
    result = guard_dispatch_icall(v_stack_m188, v_stack_m170, v_stack_m178, (unsigned int)(a5));
    v_stack_m1A4 = (unsigned int)(result);
    goto loc_007C9703;
loc_007C9703:
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rip + 3675350 + 0 + 0 * 4 * 8 + 32)) == 0) goto loc_007C974B;
    result = 17;
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rip + 3675350 + 0 + 0 * 4 * 8 + 32)) != 0) {
        a1 = v_stack_m188 + 46840;
        result = ExfReleasePushLockShared(a1, v_stack_m170, v_stack_m178, (unsigned int)(a5));
    }
    result = KeAbPostRelease(v_stack_m188 + 46840, v_stack_m170, v_stack_m178, (unsigned int)(a5));
    result = KeLeaveCriticalRegion(v_stack_m188 + 46840, v_stack_m170, v_stack_m178, (unsigned int)(a5));
    goto loc_007C974B;
loc_007C973E:
loc_007C974B:
    if (v_stack_m1A7 == 0) goto loc_007C9781;
    v_rdi = (unsigned int)(v_stack_m1A4);
    if (!(sign_flag)) {
        a1 = 0xC0000023ULL;
        result = a5;
        v_rdi = (unsigned int)(v_stack_m1A4);
        if ((*(unsigned int *)(v_stack_m198)) > ((unsigned int)(result))) { v_rdi = (unsigned int)(a1); }
        v_stack_m1A4 = (unsigned int)(v_rdi);
    }
    goto loc_007C977F;
loc_007C977F:
    goto loc_007C9795;
loc_007C9781:
    if (!sign_flag) goto loc_007C97DE;
    v_stack_m1A4 = (unsigned int)((unsigned int)(v_stack_m168));
loc_007C9790:
loc_007C9795:
    if (v_stack_m158 != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(v_stack_m158, a2, v_stack_m178, (unsigned int)(a5));
    }
    if (v_stack_m190 != 0) {
        a2 = 0;
        a1 = v_stack_m190;
        result = ExFreePoolWithTag(a1, a2, v_stack_m178, (unsigned int)(a5));
    }
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, v_stack_m178, (unsigned int)(a5));
    v_rsp = (v_rsp) + (464);
    return result;
loc_007C97DE:
    v_stack_p64 = 0;
    v_stack_p28 = v_stack_pA4;
    v_stack_p20 = 4;
    a3 = 0;
    result = sub_004BA83C(v_stack_m190, v_rip + 3677447, a3, v_stack_p8C);
    v_stack_p64 = (unsigned int)(result);
    if ((*(unsigned __int64 *)(v_rip + 8448889)) == 0) goto loc_007C99D5;
    if (v_stack_p8C == 0) goto loc_007C99D5;
    a3 = 0;
    result = RtlEqualUnicodeString(v_stack_m148, v_rip + 3677412, a3, v_stack_p8C);
    if ((unsigned __int8)(result) != 0) goto loc_007C99D5;
    v_r12 = (unsigned int)((*(unsigned __int16 *)(v_stack_m148)) + (2));
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(v_r12)), (unsigned int)(0x20534C53ULL), v_stack_p8C);
    v_stack_p78 = result;
    if (result != 0) goto loc_007C987E;
    goto loc_007C9BCA;
loc_007C987E:
    result = memcpy(result, *(unsigned __int64 *)(v_stack_p108), *(unsigned __int16 *)(v_stack_m148), v_stack_p8C);
    v_stack_p110 = v_rip - 1021455;
    v_stack_p118 = v_rip - 1021694;
    v_stack_p120 = v_rip - 1021805;
    v_stack_p128 = v_rip - 1021612;
    v_stack_p130 = v_rip - 1021675;
    v_stack_p138 = v_rip - 1021898;
    v_stack_p140 = v_rip - 1022041;
loc_007C9904:
    if (0 >= 7) goto loc_007C992B;
    result = wcsicmp(v_stack_p78, *(unsigned __int64 *)(v_rsp + 0 * 8 + 272), *(unsigned __int16 *)(v_stack_m148), v_stack_p8C);
    if ((unsigned int)(result) == 0) goto loc_007C9928;
    v_r15 = (unsigned int)((0) + ((unsigned int)(v_rsi + 1)));
    goto loc_007C9904;
loc_007C9928:
loc_007C992B:
    if ((unsigned __int8)((unsigned __int8)(v_rsi + 1)) != 0) goto loc_007C99D5;
    result = SLGetSubscriptionPfn(v_stack_p80, v_stack_pB0, *(unsigned __int16 *)(v_stack_m148), v_stack_p8C);
    v_stack_p50 = 0;
    v_stack_p48 = v_stack_p98;
    v_stack_p40 = v_stack_p70;
    v_stack_p38 = (unsigned int)((unsigned int)(a5));
    v_stack_p30 = v_stack_p90;
    v_stack_p28 = (unsigned int)(v_r12);
    v_stack_p20 = v_stack_p78;
    a4 = 0;
    a3 = 0;
    a2 = 0;
    result = guard_dispatch_icall(v_stack_pB0, a2, a3, a4);
    if ((((unsigned int)((unsigned int)(0x80000000ULL))) & ((unsigned int)(result + (unsigned int)(0x80000000ULL) * 1))) != 0) goto loc_007C99C0;
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)(0xC0000023ULL)))) goto loc_007C99DA;
loc_007C99C0:
    v_rdi = (unsigned int)((unsigned int)(result));
    if (a5 == 0) { v_rdi = (unsigned int)((unsigned int)(0xC0000023ULL)); }
    v_stack_p64 = (unsigned int)(v_rdi);
    goto loc_007C99DE;
loc_007C99D5:
loc_007C99DA:
loc_007C99DE:
    if ((unsigned __int8)(v_stack_p60) == 0) goto loc_007C9A97;
    v_stack_p28 = v_stack_p70;
    v_stack_p20 = (unsigned int)((unsigned int)(a5));
    result = sub_004BA83C(v_stack_p80, v_stack_pD0, v_stack_p98, v_stack_p90);
    v_stack_p64 = (unsigned int)(result);
    if (((unsigned int)(result)) != 0xC000003EULL) goto loc_007C9A97;
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_stack_p80 + 46840, a2, a3, v_stack_p90);
    if (!(condition_is_above_or_equal)) {
        a3 = v_stack_p80 + 46840;
        a2 = result;
        a1 = v_stack_p80 + 46840;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, v_stack_p90);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = (unsigned __int8)(v_rsi + 1);
    }
    *(unsigned __int8 *)(v_stack_p80 + 46992) = (unsigned __int8)(v_rsi + 1);
    v_rbx = (unsigned __int8)((v_rbx) & (6));
    if (((unsigned __int8)(v_rbx)) == 2) {
        a1 = v_stack_p80 + 46840;
        result = ExfTryToWakePushLock(a1, a2, a3, v_stack_p90);
    }
    result = KeAbPostRelease(v_stack_p80 + 46840, a2, a3, v_stack_p90);
    result = KeLeaveCriticalRegion(v_stack_p80 + 46840, a2, a3, v_stack_p90);
loc_007C9A97:
loc_007C9A9F:
    if (0 >= 14) goto loc_007C9B47;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_stack_pD8))) != ((unsigned __int16)(*(unsigned __int16 *)(v_rip + 3674096 + 0 + 0 * 4 * 8 + 8)))) goto loc_007C9BBA;
    result = (unsigned int)((*(unsigned __int16 *)(v_stack_pD8)) >> (1));
    if (condition_is_equal) goto loc_007C9B1F;
    a4 = (*(unsigned __int64 *)(v_stack_pD8 + 8)) - (v_stack_p150);
loc_007C9AF3:
    a1 = (unsigned __int16)(((unsigned __int16)((unsigned int)((unsigned int)(v_rsi + 1)))) << (8));
    a1 = (unsigned __int16)((a1) | ((unsigned __int16)(v_rsi + 1 + (unsigned int)((unsigned int)(v_rsi + 1)) * 1)));
    a1 = (unsigned __int16)((a1) | ((unsigned __int16)((unsigned int)(0x5555ULL))));
    a1 = (unsigned __int16)((a1) ^ (*(unsigned __int16 *)(a4 + v_stack_p150 * 1)));
    *(unsigned __int16 *)(v_stack_p150) = (unsigned __int16)(a1);
    v_r15 = (unsigned int)(((unsigned int)((unsigned int)(v_rsi + 1))) + (2));
    v_r10 = ((unsigned int)((unsigned int)(result))) - (v_rsi + 1);
    if (condition_is_not_equal) goto loc_007C9AF3;
loc_007C9B1F:
    result = memcmp(v_stack_p150, *(unsigned __int64 *)(v_rip + 3674096 + 0 + 0 * 4 * 8), *(unsigned __int16 *)(v_rip + 3674096 + 0 + 0 * 4 * 8 + 8), a4);
    if ((unsigned int)(result) != 0) goto loc_007C9BBD;
loc_007C9B47:
    if (*(unsigned __int64 *)(v_rip + 3673966 + 0 + 0 * 4 * 8 + 24) == 0) goto loc_007C9790;
    if (!sign_flag) goto loc_007C9B68;
    if (((unsigned int)((unsigned int)(v_stack_p64))) == 0xC0000034ULL) goto loc_007C9B68;
    if (((unsigned int)((unsigned int)(v_stack_p64))) != 0xC0000225ULL) goto loc_007C9790;
loc_007C9B68:
    v_stack_p28 = v_stack_p61;
    v_stack_p20 = v_stack_p70;
    result = guard_dispatch_icall(v_stack_p80, v_stack_p98, v_stack_p90, (unsigned int)(a5));
    if (v_stack_p61 == 0) goto loc_007C9790;
    v_stack_p64 = (unsigned int)(result);
    goto loc_007C9790;
loc_007C9BBA:
    v_r15 = (unsigned int)((v_r15) + ((unsigned int)(v_stack_p98)));
loc_007C9BBD:
    v_rbx = (unsigned int)((0) + ((unsigned int)(v_rsi + 1)));
    goto loc_007C9A9F;
loc_007C9BC5:
loc_007C9BCA:
    v_stack_p64 = (unsigned int)((unsigned int)(0xC000000DULL));
    goto loc_007C9795;
}
```

## 5. (Beta) C Style

```c
int64_t SLQueryLicenseValueInternal(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint32_t Arg5, int64_t Arg6)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint64_t v_stack_m130;
    uint64_t v_stack_m138;
    uint64_t v_stack_m140;
    uint64_t v_stack_m148;
    uint64_t v_stack_m158;
    uint64_t v_stack_m160;
    uint32_t v_stack_m164;
    uint32_t v_stack_m168;
    uint64_t v_stack_m170;
    uint64_t v_stack_m178;
    uint32_t v_stack_m17C;
    uint32_t v_stack_m180;
    uint64_t v_stack_m188;
    uint64_t v_stack_m190;
    uint64_t v_stack_m198;
    uint8_t v_stack_m1A0;
    uint32_t v_stack_m1A4;
    uint8_t v_stack_m1A7;
    uint8_t v_stack_m1A8;
    uint64_t v_stack_m1E0;
    uint64_t v_stack_m1E8;
    uint64_t v_stack_m48;
    uint64_t v_stack_mB8;
    uint64_t v_stack_p108;
    uint64_t v_stack_p110;
    uint64_t v_stack_p118;
    uint64_t v_stack_p120;
    uint64_t v_stack_p128;
    uint64_t v_stack_p130;
    uint64_t v_stack_p138;
    uint64_t v_stack_p140;
    uint64_t v_stack_p150;
    uint32_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint32_t v_stack_p38;
    uint64_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint8_t v_stack_p60;
    uint64_t v_stack_p61;
    uint32_t v_stack_p64;
    uint64_t v_stack_p70;
    uint64_t v_stack_p78;
    uint64_t v_stack_p80;
    uint64_t v_stack_p8C;
    uint64_t v_stack_p90;
    uint64_t v_stack_p98;
    uint64_t v_stack_pA4;
    uint64_t v_stack_pB0;
    uint64_t v_stack_pD0;
    uint64_t v_stack_pD8;

    local_rsp = (local_rsp) - (464);
    result = (*(uint64_t *)(v_rip + 0x64133A)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m178 = Arg4;
    v_stack_m170 = Arg3;
    v_stack_m148 = Arg2;
    v_stack_m188 = Arg1;
    v_stack_m120 = Arg1;
    v_stack_m118 = Arg2;
    v_stack_m110 = Arg3;
    v_stack_m140 = Arg4;
    v_stack_m198 = Arg6;
    local_rsi = 0;
    v_stack_m1A4 = 0;
    v_stack_m138 = v_xmm0;
    v_stack_m1A7 = 0;
    v_stack_m190 = 0;
    v_stack_m158 = 0;
    v_stack_m17C = 0;
    v_stack_m164 = 0;
    v_stack_m1A8 = (uint8_t)(local_rsi + 1);
    if (Arg2 == 0) goto loc_007C9BC5;
    if (Arg6 == 0) goto loc_007C9BC5;
    v_stack_m1A4 = 0;
    v_stack_m100 = Arg2 + 8;
    if ((*(uint64_t *)(Arg2 + 0x8)) == 0) goto loc_007C9BC5;
    if ((*(uint16_t *)(Arg2)) < ((uint16_t)(local_rsi + 2))) goto loc_007C9BC5;
    v_stack_m138 = (uint8_t)(local_rsi + 1);
    v_stack_m130 = Arg2;
    result = sub_007C87A4(Arg1, Arg2, Arg3, Arg4);
    v_stack_m168 = (uint32_t)(result);
    v_stack_m160 = 0;
    v_stack_m1A0 = 0;
    v_stack_m180 = (uint32_t)((uint32_t)((uint32_t)(local_rsi + 1)));
loc_007C9513:
    if (0 >= 14) goto loc_007C95F3;
    if (((uint16_t)(*(uint16_t *)(v_stack_m130))) != ((uint16_t)(*(uint16_t *)(v_rip + 0x381596 + 0x0 + 0x0 * 4 * 8 + 0x8)))) goto loc_007C95C1;
    result = (uint32_t)((*(uint16_t *)(v_stack_m130)) >> (1));
    if (condition_is_equal) goto loc_007C959C;
    Arg4 = (*(uint64_t *)(v_stack_m130 + 0x8)) - (v_stack_mB8);
loc_007C9566:
    Arg1 = (uint16_t)(((uint16_t)((uint32_t)((uint32_t)(local_rsi + 1)))) << (8));
    Arg1 = (uint16_t)((Arg1) | ((uint16_t)(local_rsi + 1 + (uint32_t)((uint32_t)(local_rsi + 1)) * 1)));
    Arg1 = (uint16_t)((Arg1) | ((uint16_t)((uint32_t)(0x5555ULL))));
    Arg1 = (uint16_t)((Arg1) ^ (*(uint16_t *)(Arg4 + v_stack_mB8 * 1)));
    *(uint16_t *)(v_stack_mB8) = (uint16_t)(Arg1);
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(local_rsi + 1))) + (2));
    local_r11 = ((uint32_t)((uint32_t)(result))) - (local_rsi + 1);
    if (condition_is_not_equal) goto loc_007C9566;
    v_stack_m180 = (uint32_t)(Arg2);
loc_007C959C:
    result = memcmp(v_stack_mB8, *(uint64_t *)(v_rip + 0x38150D + 0x0 + 0x0 * 4 * 8), *(uint16_t *)(v_rip + 0x381596 + 0x0 + 0x0 * 4 * 8 + 0x8), Arg4);
    if ((uint32_t)(result) == 0) goto loc_007C95D3;
    goto loc_007C95CB;
loc_007C95C1:
    Arg2 = (uint32_t)(((uint32_t)(v_stack_m180)) + ((uint32_t)(*(uint16_t *)(v_rip + 0x381596 + 0x0 + 0x0 * 4 * 8 + 0x8))));
    v_stack_m180 = (uint32_t)(Arg2);
loc_007C95CB:
    local_r12 = (uint32_t)((0) + ((uint32_t)(local_rsi + 1)));
    goto loc_007C9513;
loc_007C95D3:
    v_stack_m160 = *(uint64_t *)(v_rip + 0x3814D6 + 0x0 + 0x0 * 4 * 8 + 0x10);
    v_stack_m1A0 = (uint8_t)(*(uint8_t *)(v_rip + 0x3814D6 + 0x0 + 0x0 * 4 * 8 + 0x20));
    goto loc_007C95F6;
loc_007C95F3:
loc_007C95F6:
    local_rbx = (0 + 0 * 4) | (-1);
    if (0 == 0) goto loc_007C973E;
    if ((uint8_t)(*(uint8_t *)(v_rip + 0x3814D6 + 0x0 + 0x0 * 4 * 8 + 0x20)) == 0) goto loc_007C9666;
    local_r12 = (v_stack_m188) + (0xB6F8ULL);
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(local_r12, Arg2, Arg3, Arg4);
    result = 0;
    if (!(condition_is_equal)) {
        Arg4 = local_r12;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = local_r12;
        result = ExfAcquirePushLockSharedEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = (uint8_t)(local_rsi + 1);
    }
    v_stack_m1E0 = v_stack_m1A7;
    v_stack_m1E8 = v_stack_m198;
    result = guard_dispatch_icall(v_stack_m188, v_stack_m170, v_stack_m178, (uint32_t)(Arg5));
    v_stack_m1A4 = (uint32_t)(result);
    goto loc_007C9703;
loc_007C9703:
    if ((uint8_t)(*(uint8_t *)(v_rip + 0x3814D6 + 0x0 + 0x0 * 4 * 8 + 0x20)) == 0) goto loc_007C974B;
    result = 17;
    if ((uint8_t)(*(uint8_t *)(v_rip + 0x3814D6 + 0x0 + 0x0 * 4 * 8 + 0x20)) != 0) {
        Arg1 = v_stack_m188 + 46840;
        result = ExfReleasePushLockShared(Arg1, v_stack_m170, v_stack_m178, (uint32_t)(Arg5));
    }
    result = KeAbPostRelease(v_stack_m188 + 46840, v_stack_m170, v_stack_m178, (uint32_t)(Arg5));
    result = KeLeaveCriticalRegion(v_stack_m188 + 46840, v_stack_m170, v_stack_m178, (uint32_t)(Arg5));
    goto loc_007C974B;
loc_007C973E:
loc_007C974B:
    if (v_stack_m1A7 == 0) goto loc_007C9781;
    local_rdi = (uint32_t)(v_stack_m1A4);
    if (!(sign_flag)) {
        Arg1 = 0xC0000023ULL;
        result = Arg5;
        local_rdi = (uint32_t)(v_stack_m1A4);
        if ((*(uint32_t *)(v_stack_m198)) > ((uint32_t)(result))) { local_rdi = (uint32_t)(Arg1); }
        v_stack_m1A4 = (uint32_t)(local_rdi);
    }
    goto loc_007C977F;
loc_007C977F:
    goto loc_007C9795;
loc_007C9781:
    if (!sign_flag) goto loc_007C97DE;
    v_stack_m1A4 = (uint32_t)((uint32_t)(v_stack_m168));
loc_007C9790:
loc_007C9795:
    if (v_stack_m158 != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(v_stack_m158, Arg2, v_stack_m178, (uint32_t)(Arg5));
    }
    if (v_stack_m190 != 0) {
        Arg2 = 0;
        Arg1 = v_stack_m190;
        result = ExFreePoolWithTag(Arg1, Arg2, v_stack_m178, (uint32_t)(Arg5));
    }
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, v_stack_m178, (uint32_t)(Arg5));
    local_rsp = (local_rsp) + (464);
    return result;
loc_007C97DE:
    v_stack_p64 = 0;
    v_stack_p28 = v_stack_pA4;
    v_stack_p20 = 4;
    Arg3 = 0;
    result = sub_004BA83C(v_stack_m190, v_rip + 3677447, Arg3, v_stack_p8C);
    v_stack_p64 = (uint32_t)(result);
    if ((*(uint64_t *)(v_rip + 0x80EB79)) == 0) goto loc_007C99D5;
    if (v_stack_p8C == 0) goto loc_007C99D5;
    Arg3 = 0;
    result = RtlEqualUnicodeString(v_stack_m148, v_rip + 3677412, Arg3, v_stack_p8C);
    if ((uint8_t)(result) != 0) goto loc_007C99D5;
    local_r12 = (uint32_t)((*(uint16_t *)(v_stack_m148)) + (2));
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(local_r12)), (uint32_t)(0x20534C53ULL), v_stack_p8C);
    v_stack_p78 = result;
    if (result != 0) goto loc_007C987E;
    goto loc_007C9BCA;
loc_007C987E:
    result = memcpy(result, *(uint64_t *)(v_stack_p108), *(uint16_t *)(v_stack_m148), v_stack_p8C);
    v_stack_p110 = v_rip - 1021455;
    v_stack_p118 = v_rip - 1021694;
    v_stack_p120 = v_rip - 1021805;
    v_stack_p128 = v_rip - 1021612;
    v_stack_p130 = v_rip - 1021675;
    v_stack_p138 = v_rip - 1021898;
    v_stack_p140 = v_rip - 1022041;
loc_007C9904:
    if (0 >= 7) goto loc_007C992B;
    result = wcsicmp(v_stack_p78, *(uint64_t *)(local_rsp + 0x0 * 8 + 0x110), *(uint16_t *)(v_stack_m148), v_stack_p8C);
    if ((uint32_t)(result) == 0) goto loc_007C9928;
    local_r15 = (uint32_t)((0) + ((uint32_t)(local_rsi + 1)));
    goto loc_007C9904;
loc_007C9928:
loc_007C992B:
    if ((uint8_t)((uint8_t)(local_rsi + 1)) != 0) goto loc_007C99D5;
    result = SLGetSubscriptionPfn(v_stack_p80, v_stack_pB0, *(uint16_t *)(v_stack_m148), v_stack_p8C);
    v_stack_p50 = 0;
    v_stack_p48 = v_stack_p98;
    v_stack_p40 = v_stack_p70;
    v_stack_p38 = (uint32_t)((uint32_t)(Arg5));
    v_stack_p30 = v_stack_p90;
    v_stack_p28 = (uint32_t)(local_r12);
    v_stack_p20 = v_stack_p78;
    Arg4 = 0;
    Arg3 = 0;
    Arg2 = 0;
    result = guard_dispatch_icall(v_stack_pB0, Arg2, Arg3, Arg4);
    if ((((uint32_t)((uint32_t)(0x80000000ULL))) & ((uint32_t)(result + (uint32_t)(0x80000000ULL) * 1))) != 0) goto loc_007C99C0;
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)(0xC0000023ULL)))) goto loc_007C99DA;
loc_007C99C0:
    local_rdi = (uint32_t)((uint32_t)(result));
    if (Arg5 == 0) { local_rdi = (uint32_t)((uint32_t)(0xC0000023ULL)); }
    v_stack_p64 = (uint32_t)(local_rdi);
    goto loc_007C99DE;
loc_007C99D5:
loc_007C99DA:
loc_007C99DE:
    if ((uint8_t)(v_stack_p60) == 0) goto loc_007C9A97;
    v_stack_p28 = v_stack_p70;
    v_stack_p20 = (uint32_t)((uint32_t)(Arg5));
    result = sub_004BA83C(v_stack_p80, v_stack_pD0, v_stack_p98, v_stack_p90);
    v_stack_p64 = (uint32_t)(result);
    if (((uint32_t)(result)) != 0xC000003EULL) goto loc_007C9A97;
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(v_stack_p80 + 46840, Arg2, Arg3, v_stack_p90);
    if (!(condition_is_above_or_equal)) {
        Arg3 = v_stack_p80 + 46840;
        Arg2 = result;
        Arg1 = v_stack_p80 + 46840;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, v_stack_p90);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = (uint8_t)(local_rsi + 1);
    }
    *(uint8_t *)(v_stack_p80 + 0xB790) = (uint8_t)(local_rsi + 1);
    local_rbx = (uint8_t)((local_rbx) & (6));
    if (((uint8_t)(local_rbx)) == 2) {
        Arg1 = v_stack_p80 + 46840;
        result = ExfTryToWakePushLock(Arg1, Arg2, Arg3, v_stack_p90);
    }
    result = KeAbPostRelease(v_stack_p80 + 46840, Arg2, Arg3, v_stack_p90);
    result = KeLeaveCriticalRegion(v_stack_p80 + 46840, Arg2, Arg3, v_stack_p90);
loc_007C9A97:
loc_007C9A9F:
    if (0 >= 14) goto loc_007C9B47;
    if (((uint16_t)(*(uint16_t *)(v_stack_pD8))) != ((uint16_t)(*(uint16_t *)(v_rip + 0x380FF0 + 0x0 + 0x0 * 4 * 8 + 0x8)))) goto loc_007C9BBA;
    result = (uint32_t)((*(uint16_t *)(v_stack_pD8)) >> (1));
    if (condition_is_equal) goto loc_007C9B1F;
    Arg4 = (*(uint64_t *)(v_stack_pD8 + 0x8)) - (v_stack_p150);
loc_007C9AF3:
    Arg1 = (uint16_t)(((uint16_t)((uint32_t)((uint32_t)(local_rsi + 1)))) << (8));
    Arg1 = (uint16_t)((Arg1) | ((uint16_t)(local_rsi + 1 + (uint32_t)((uint32_t)(local_rsi + 1)) * 1)));
    Arg1 = (uint16_t)((Arg1) | ((uint16_t)((uint32_t)(0x5555ULL))));
    Arg1 = (uint16_t)((Arg1) ^ (*(uint16_t *)(Arg4 + v_stack_p150 * 1)));
    *(uint16_t *)(v_stack_p150) = (uint16_t)(Arg1);
    local_r15 = (uint32_t)(((uint32_t)((uint32_t)(local_rsi + 1))) + (2));
    local_r10 = ((uint32_t)((uint32_t)(result))) - (local_rsi + 1);
    if (condition_is_not_equal) goto loc_007C9AF3;
loc_007C9B1F:
    result = memcmp(v_stack_p150, *(uint64_t *)(v_rip + 0x380FF0 + 0x0 + 0x0 * 4 * 8), *(uint16_t *)(v_rip + 0x380FF0 + 0x0 + 0x0 * 4 * 8 + 0x8), Arg4);
    if ((uint32_t)(result) != 0) goto loc_007C9BBD;
loc_007C9B47:
    if (*(uint64_t *)(v_rip + 0x380F6E + 0x0 + 0x0 * 4 * 8 + 0x18) == 0) goto loc_007C9790;
    if (!sign_flag) goto loc_007C9B68;
    if (((uint32_t)((uint32_t)(v_stack_p64))) == 0xC0000034ULL) goto loc_007C9B68;
    if (((uint32_t)((uint32_t)(v_stack_p64))) != 0xC0000225ULL) goto loc_007C9790;
loc_007C9B68:
    v_stack_p28 = v_stack_p61;
    v_stack_p20 = v_stack_p70;
    result = guard_dispatch_icall(v_stack_p80, v_stack_p98, v_stack_p90, (uint32_t)(Arg5));
    if (v_stack_p61 == 0) goto loc_007C9790;
    v_stack_p64 = (uint32_t)(result);
    goto loc_007C9790;
loc_007C9BBA:
    local_r15 = (uint32_t)((local_r15) + ((uint32_t)(v_stack_p98)));
loc_007C9BBD:
    local_rbx = (uint32_t)((0) + ((uint32_t)(local_rsi + 1)));
    goto loc_007C9A9F;
loc_007C9BC5:
loc_007C9BCA:
    v_stack_p64 = (uint32_t)((uint32_t)(0xC000000DULL));
    goto loc_007C9795;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007C93EC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
