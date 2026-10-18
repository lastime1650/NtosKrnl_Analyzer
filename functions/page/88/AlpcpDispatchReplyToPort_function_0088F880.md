# AlpcpDispatchReplyToPort

- RVA: `0x0088F880`–`0x0088FD27` (길이 `1,191` bytes)
- VA: `0x000000014088F880`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0007D614`
- 디코드: `288`개 명령, `1,191/1,191` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **28**; 고유 호출 대상: **14**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0088F8DE` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0088F906` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)
- `0x0088F95D` → [ObReferenceObjectSafe](../../text/41/ObReferenceObjectSafe_function_0041DAE0.md) (function, `0x0041DAE0`)
- `0x0088F975` → [ObReferenceObjectSafe](../../text/41/ObReferenceObjectSafe_function_0041DAE0.md) (function, `0x0041DAE0`)
- `0x0088F9D1` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0088F9EB` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x0088FA1B` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0088FA9B` → [AlpcpClearOwnerPortMessage](AlpcpClearOwnerPortMessage_function_0088FD30.md) (function, `0x0088FD30`)
- `0x0088FAA3` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (function, `0x0020FA20`)
- `0x0088FAD3` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x0088FAE2` → [AlpcpRemoveMessageFromPendingQueue](AlpcpRemoveMessageFromPendingQueue_function_0088FD70.md) (function, `0x0088FD70`)
- `0x0088FAF3` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0088FB20` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)
- `0x0088FB6F` → [AlpcpCompleteDispatchMessage](AlpcpCompleteDispatchMessage_function_0088E140.md) (function, `0x0088E140`)
- `0x0088FBA3` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0088FBCA` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)
- `0x0088FC11` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x0088FC19` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0088FC2A` → [AlpcpCancelMessage](../89/AlpcpCancelMessage_function_00894120.md) (function, `0x00894120`)
- `0x0088FC56` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x0088FC74` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x0088FC7C` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0088FC84` → [AlpcpUnlockMessage](../89/AlpcpUnlockMessage_function_00897AE0.md) (function, `0x00897AE0`)
- `0x0088FC96` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x0088FC9E` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x0088FCA8` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x0088FCD3` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0088FCFA` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)

### Direct callers
- [AlpcpSendMessage](AlpcpSendMessage_function_0088BD40.md) at `0x0088C91A`
- [AlpcpDispatchMessage](AlpcpDispatchMessage_function_0088F7D0.md) at `0x0088F7FC`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **23**
  - `0x0088F8DE` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x0088F906` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (`PAGE` → `.text`)
  - `0x0088F95D` → [ObReferenceObjectSafe](../../text/41/ObReferenceObjectSafe_function_0041DAE0.md) (`PAGE` → `.text`)
  - `0x0088F975` → [ObReferenceObjectSafe](../../text/41/ObReferenceObjectSafe_function_0041DAE0.md) (`PAGE` → `.text`)
  - `0x0088F9D1` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x0088F9EB` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x0088FA1B` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0088FAA3` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (`PAGE` → `.text`)
  - `0x0088FAD3` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x0088FAF3` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x0088FB20` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (`PAGE` → `.text`)
  - `0x0088FBA3` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x0088FBCA` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (`PAGE` → `.text`)
  - `0x0088FC11` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x0088FC19` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0088FC56` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x0088FC74` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x0088FC7C` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0088FC96` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x0088FC9E` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x0088FCA8` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x0088FCD3` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x0088FCFA` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x0088FCE9` → [sub_00B193C0](../B1/Unknown_function_00B193C0.md) (`tail-transfer`)
  - `0x0088FD05` → [sub_00B193C0](../B1/Unknown_function_00B193C0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0088F880  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
0088F885  55                              push rbp
0088F886  56                              push rsi
0088F887  57                              push rdi
0088F888  41 54                           push r12
0088F88A  41 55                           push r13
0088F88C  41 56                           push r14
0088F88E  41 57                           push r15
0088F890  48 83 EC 20                     sub rsp, 0x20
0088F894  8B 41 30                        mov eax, dword ptr [rcx + 0x30]
0088F897  45 33 C0                        xor r8d, r8d
0088F89A  48 8B 79 08                     mov rdi, qword ptr [rcx + 8]
0088F89E  33 D2                           xor edx, edx
0088F8A0  4C 8B 31                        mov r14, qword ptr [rcx]
0088F8A3  48 8B D9                        mov rbx, rcx
0088F8A6  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
0088F8AA  33 C0                           xor eax, eax
0088F8AC  48 89 41 20                     mov qword ptr [rcx + 0x20], rax
0088F8B0  48 89 41 18                     mov qword ptr [rcx + 0x18], rax
0088F8B4  48 89 41 28                     mov qword ptr [rcx + 0x28], rax
0088F8B8  48 8B 77 18                     mov rsi, qword ptr [rdi + 0x18]
0088F8BC  8B 86 A0 01 00 00               mov eax, dword ptr [rsi + 0x1a0]
0088F8C2  D1 E8                           shr eax, 1
0088F8C4  83 E0 03                        and eax, 3
0088F8C7  83 F8 02                        cmp eax, 2
0088F8CA  0F 85 BC 02 00 00               jne 0x14088fb8c
0088F8D0  4C 8B 66 10                     mov r12, qword ptr [rsi + 0x10]
0088F8D4  4C 89 64 24 68                  mov qword ptr [rsp + 0x68], r12
0088F8D9  49 8D 4C 24 F0                  lea rcx, [r12 - 0x10]
0088F8DE  E8 4D 09 98 FF                  call 0x140210230
0088F8E3  4C 8B F8                        mov r15, rax
0088F8E6  41 B8 11 00 00 00               mov r8d, 0x11
0088F8EC  33 C0                           xor eax, eax
0088F8EE  F0 4D 0F B1 44 24 F0            lock cmpxchg qword ptr [r12 - 0x10], r8
0088F8F5  74 1A                           je 0x14088f911
0088F8F7  4D 8D 4C 24 F0                  lea r9, [r12 - 0x10]
0088F8FC  4D 8B C7                        mov r8, r15
0088F8FF  33 D2                           xor edx, edx
0088F901  49 8D 4C 24 F0                  lea rcx, [r12 - 0x10]
0088F906  E8 41 0B 98 FF                  call 0x14021044c
0088F90B  41 B8 11 00 00 00               mov r8d, 0x11
0088F911  4D 85 FF                        test r15, r15
0088F914  74 05                           je 0x14088f91b
0088F916  41 C6 47 0A 01                  mov byte ptr [r15 + 0xa], 1
0088F91B  4D 8B 6C 24 10                  mov r13, qword ptr [r12 + 0x10]
0088F920  4D 8B E5                        mov r12, r13
0088F923  48 8B 54 24 68                  mov rdx, qword ptr [rsp + 0x68]
0088F928  41 8B 86 A0 01 00 00            mov eax, dword ptr [r14 + 0x1a0]
0088F92F  A8 20                           test al, 0x20
0088F931  0F 85 B6 02 00 00               jne 0x14088fbed
0088F937  8B 8E A0 01 00 00               mov ecx, dword ptr [rsi + 0x1a0]
0088F93D  F6 C1 20                        test cl, 0x20
0088F940  0F 85 C4 03 00 00               jne 0x14088fd0a
0088F946  0F B7 43 34                     movzx eax, word ptr [rbx + 0x34]
0088F94A  49 3B 85 10 01 00 00            cmp rax, qword ptr [r13 + 0x110]
0088F951  0F 87 0A 03 00 00               ja 0x14088fc61
0088F957  49 8B CD                        mov rcx, r13
0088F95A  49 8B EC                        mov rbp, r12
0088F95D  E8 7E E1 B8 FF                  call 0x14041dae0
0088F962  33 C9                           xor ecx, ecx
0088F964  84 C0                           test al, al
0088F966  44 8B F9                        mov r15d, ecx
0088F969  4D 0F 45 FD                     cmovne r15, r13
0088F96D  4D 85 E4                        test r12, r12
0088F970  74 13                           je 0x14088f985
0088F972  49 8B CC                        mov rcx, r12
0088F975  E8 66 E1 B8 FF                  call 0x14041dae0
0088F97A  84 C0                           test al, al
0088F97C  B9 00 00 00 00                  mov ecx, 0
0088F981  48 0F 44 E9                     cmove rbp, rcx
0088F985  4D 85 FF                        test r15, r15
0088F988  0F 84 AB 02 00 00               je 0x14088fc39
0088F98E  48 85 ED                        test rbp, rbp
0088F991  0F 84 88 03 00 00               je 0x14088fd1f
0088F997  41 8B 87 A0 01 00 00            mov eax, dword ptr [r15 + 0x1a0]
0088F99E  A8 20                           test al, 0x20
0088F9A0  0F 85 ED 02 00 00               jne 0x14088fc93
0088F9A6  8B 85 A0 01 00 00               mov eax, dword ptr [rbp + 0x1a0]
0088F9AC  A8 20                           test al, 0x20
0088F9AE  0F 85 DF 02 00 00               jne 0x14088fc93
0088F9B4  48 89 8F C8 00 00 00            mov qword ptr [rdi + 0xc8], rcx
0088F9BB  66 83 7B 36 0B                  cmp word ptr [rbx + 0x36], 0xb
0088F9C0  75 5E                           jne 0x14088fa20
0088F9C2  48 8D AE 60 01 00 00            lea rbp, [rsi + 0x160]
0088F9C9  45 33 C0                        xor r8d, r8d
0088F9CC  48 8B CD                        mov rcx, rbp
0088F9CF  33 D2                           xor edx, edx
0088F9D1  E8 5A 08 98 FF                  call 0x140210230
0088F9D6  F0 48 0F BA 6D 00 00            lock bts qword ptr [rbp], 0
0088F9DD  4C 8B F8                        mov r15, rax
0088F9E0  73 0E                           jae 0x14088f9f0
0088F9E2  4C 8B C5                        mov r8, rbp
0088F9E5  48 8B D0                        mov rdx, rax
0088F9E8  48 8B CD                        mov rcx, rbp
0088F9EB  E8 A0 02 98 FF                  call 0x14020fc90
0088F9F0  4D 85 FF                        test r15, r15
0088F9F3  74 05                           je 0x14088f9fa
0088F9F5  41 C6 47 0A 01                  mov byte ptr [r15 + 0xa], 1
0088F9FA  83 A6 A0 01 00 00 F7            and dword ptr [rsi + 0x1a0], 0xfffffff7
0088FA01  48 C7 C0 FF FF FF FF            mov rax, 0xffffffffffffffff
0088FA08  F0 48 0F C1 45 00               lock xadd qword ptr [rbp], rax
0088FA0E  24 06                           and al, 6
0088FA10  3C 02                           cmp al, 2
0088FA12  0F 84 8D 02 00 00               je 0x14088fca5
0088FA18  48 8B CD                        mov rcx, rbp
0088FA1B  E8 E0 1B A5 FF                  call 0x1402e1600
0088FA20  65 4C 8B 3C 25 88 01 00 00      mov r15, qword ptr gs:[0x188]
0088FA29  0F B7 43 34                     movzx eax, word ptr [rbx + 0x34]
0088FA2D  66 89 87 F2 00 00 00            mov word ptr [rdi + 0xf2], ax
0088FA34  0F B7 43 34                     movzx eax, word ptr [rbx + 0x34]
0088FA38  66 83 E8 28                     sub ax, 0x28
0088FA3C  F7 44 24 60 00 00 01 00         test dword ptr [rsp + 0x60], 0x10000
0088FA44  66 89 87 F0 00 00 00            mov word ptr [rdi + 0xf0], ax
0088FA4B  0F B7 4B 36                     movzx ecx, word ptr [rbx + 0x36]
0088FA4F  66 89 8F F4 00 00 00            mov word ptr [rdi + 0xf4], cx
0088FA56  0F B7 43 38                     movzx eax, word ptr [rbx + 0x38]
0088FA5A  66 89 87 F6 00 00 00            mov word ptr [rdi + 0xf6], ax
0088FA61  41 0F 10 87 08 05 00 00         movups xmm0, xmmword ptr [r15 + 0x508]
0088FA69  8B 47 28                        mov eax, dword ptr [rdi + 0x28]
0088FA6C  0F 11 87 F8 00 00 00            movups xmmword ptr [rdi + 0xf8], xmm0
0088FA73  0F 84 39 02 00 00               je 0x14088fcb2
0088FA79  BA FF DF FF FF                  mov edx, 0xffffdfff
0088FA7E  66 23 CA                        and cx, dx
0088FA81  0F BA E8 09                     bts eax, 9
0088FA85  0F BA E8 10                     bts eax, 0x10
0088FA89  66 89 8F F4 00 00 00            mov word ptr [rdi + 0xf4], cx
0088FA90  89 47 28                        mov dword ptr [rdi + 0x28], eax
0088FA93  F0 83 0C 24 00                  lock or dword ptr [rsp], 0
0088FA98  48 8B CF                        mov rcx, rdi
0088FA9B  E8 90 02 00 00                  call 0x14088fd30
0088FAA0  49 8B CE                        mov rcx, r14
0088FAA3  E8 78 FF 97 FF                  call 0x14020fa20
0088FAA8  81 4F 28 00 10 00 00            or dword ptr [rdi + 0x28], 0x1000
0088FAAF  B8 01 00 00 00                  mov eax, 1
0088FAB4  4C 89 77 18                     mov qword ptr [rdi + 0x18], r14
0088FAB8  F0 41 0F C1 84 24 90 01 00 00   lock xadd dword ptr [r12 + 0x190], eax
0088FAC2  FF C0                           inc eax
0088FAC4  49 8B CC                        mov rcx, r12
0088FAC7  89 47 2C                        mov dword ptr [rdi + 0x2c], eax
0088FACA  49 8B 44 24 38                  mov rax, qword ptr [r12 + 0x38]
0088FACF  48 89 47 78                     mov qword ptr [rdi + 0x78], rax
0088FAD3  E8 78 98 A6 FF                  call 0x1402f9350
0088FAD8  48 83 7F 10 00                  cmp qword ptr [rdi + 0x10], 0
0088FADD  74 08                           je 0x14088fae7
0088FADF  48 8B CF                        mov rcx, rdi
0088FAE2  E8 89 02 00 00                  call 0x14088fd70
0088FAE7  45 33 C0                        xor r8d, r8d
0088FAEA  49 8D 8D 60 01 00 00            lea rcx, [r13 + 0x160]
0088FAF1  33 D2                           xor edx, edx
0088FAF3  E8 38 07 98 FF                  call 0x140210230
0088FAF8  48 8B E8                        mov rbp, rax
0088FAFB  B9 11 00 00 00                  mov ecx, 0x11
0088FB00  33 C0                           xor eax, eax
0088FB02  F0 49 0F B1 8D 60 01 00 00      lock cmpxchg qword ptr [r13 + 0x160], rcx
0088FB0B  74 18                           je 0x14088fb25
0088FB0D  4D 8D 8D 60 01 00 00            lea r9, [r13 + 0x160]
0088FB14  4C 8B C5                        mov r8, rbp
0088FB17  33 D2                           xor edx, edx
0088FB19  49 8D 8D 60 01 00 00            lea rcx, [r13 + 0x160]
0088FB20  E8 27 09 98 FF                  call 0x14021044c
0088FB25  48 85 ED                        test rbp, rbp
0088FB28  74 04                           je 0x14088fb2e
0088FB2A  C6 45 0A 01                     mov byte ptr [rbp + 0xa], 1
0088FB2E  F7 44 24 60 00 00 02 00         test dword ptr [rsp + 0x60], 0x20000
0088FB36  74 1A                           je 0x14088fb52
0088FB38  81 67 28 FF FE FF FF            and dword ptr [rdi + 0x28], 0xfffffeff
0088FB3F  48 8B C7                        mov rax, rdi
0088FB42  4C 89 7F 20                     mov qword ptr [rdi + 0x20], r15
0088FB46  66 83 47 E2 02                  add word ptr [rdi - 0x1e], 2
0088FB4B  49 87 87 B8 05 00 00            xchg qword ptr [r15 + 0x5b8], rax
0088FB52  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
0088FB57  48 89 43 10                     mov qword ptr [rbx + 0x10], rax
0088FB5B  4C 89 6B 20                     mov qword ptr [rbx + 0x20], r13
0088FB5F  F6 87 A0 00 00 00 01            test byte ptr [rdi + 0xa0], 1
0088FB66  74 04                           je 0x14088fb6c
0088FB68  83 4B 30 08                     or dword ptr [rbx + 0x30], 8
0088FB6C  48 8B CB                        mov rcx, rbx
0088FB6F  E8 CC E5 FF FF                  call 0x14088e140
0088FB74  33 C0                           xor eax, eax
0088FB76  48 8B 5C 24 78                  mov rbx, qword ptr [rsp + 0x78]
0088FB7B  48 83 C4 20                     add rsp, 0x20
0088FB7F  41 5F                           pop r15
0088FB81  41 5E                           pop r14
0088FB83  41 5D                           pop r13
0088FB85  41 5C                           pop r12
0088FB87  5F                              pop rdi
0088FB88  5E                              pop rsi
0088FB89  5D                              pop rbp
0088FB8A  C3                              ret
0088FB8B  CC                              int3
0088FB8C  83 F8 01                        cmp eax, 1
0088FB8F  0F 84 2E 01 00 00               je 0x14088fcc3
0088FB95  4C 8B 66 10                     mov r12, qword ptr [rsi + 0x10]
0088FB99  4C 89 64 24 68                  mov qword ptr [rsp + 0x68], r12
0088FB9E  49 8D 4C 24 F0                  lea rcx, [r12 - 0x10]
0088FBA3  E8 88 06 98 FF                  call 0x140210230
0088FBA8  4C 8B F8                        mov r15, rax
0088FBAB  B9 11 00 00 00                  mov ecx, 0x11
0088FBB0  33 C0                           xor eax, eax
0088FBB2  F0 49 0F B1 4C 24 F0            lock cmpxchg qword ptr [r12 - 0x10], rcx
0088FBB9  74 14                           je 0x14088fbcf
0088FBBB  4D 8D 4C 24 F0                  lea r9, [r12 - 0x10]
0088FBC0  4D 8B C7                        mov r8, r15
0088FBC3  33 D2                           xor edx, edx
0088FBC5  49 8D 4C 24 F0                  lea rcx, [r12 - 0x10]
0088FBCA  E8 7D 08 98 FF                  call 0x14021044c
0088FBCF  4D 85 FF                        test r15, r15
0088FBD2  74 05                           je 0x14088fbd9
0088FBD4  41 C6 47 0A 01                  mov byte ptr [r15 + 0xa], 1
0088FBD9  4D 8B 2C 24                     mov r13, qword ptr [r12]
0088FBDD  41 B8 11 00 00 00               mov r8d, 0x11
0088FBE3  4D 8B 64 24 08                  mov r12, qword ptr [r12 + 8]
0088FBE8  E9 36 FD FF FF                  jmp 0x14088f923
0088FBED  41 F7 86 00 01 00 00 00 10 00 00  test dword ptr [r14 + 0x100], 0x1000
0088FBF8  0F 85 39 FD FF FF               jne 0x14088f937
0088FBFE  48 8D 5A F0                     lea rbx, [rdx - 0x10]
0088FC02  49 8B C0                        mov rax, r8
0088FC05  33 C9                           xor ecx, ecx
0088FC07  F0 48 0F B1 0B                  lock cmpxchg qword ptr [rbx], rcx
0088FC0C  74 08                           je 0x14088fc16
0088FC0E  48 8B CB                        mov rcx, rbx
0088FC11  E8 2A 38 9D FF                  call 0x140263440
0088FC16  48 8B CB                        mov rcx, rbx
0088FC19  E8 E2 19 A5 FF                  call 0x1402e1600
0088FC1E  41 B8 00 00 01 00               mov r8d, 0x10000
0088FC24  48 8B D7                        mov rdx, rdi
0088FC27  49 8B CE                        mov rcx, r14
0088FC2A  E8 F1 44 00 00                  call 0x140894120
0088FC2F  B8 37 00 00 C0                  mov eax, 0xc0000037
0088FC34  E9 3D FF FF FF                  jmp 0x14088fb76
0088FC39  48 85 ED                        test rbp, rbp
0088FC3C  75 5D                           jne 0x14088fc9b
0088FC3E  48 8B 5C 24 68                  mov rbx, qword ptr [rsp + 0x68]
0088FC43  B8 11 00 00 00                  mov eax, 0x11
0088FC48  33 C9                           xor ecx, ecx
0088FC4A  F0 48 0F B1 4B F0               lock cmpxchg qword ptr [rbx - 0x10], rcx
0088FC50  74 09                           je 0x14088fc5b
0088FC52  48 8D 4B F0                     lea rcx, [rbx - 0x10]
0088FC56  E8 E5 37 9D FF                  call 0x140263440
0088FC5B  48 8D 4B F0                     lea rcx, [rbx - 0x10]
0088FC5F  EB B8                           jmp 0x14088fc19
0088FC61  48 8D 5A F0                     lea rbx, [rdx - 0x10]
0088FC65  49 8B C0                        mov rax, r8
0088FC68  33 C9                           xor ecx, ecx
0088FC6A  F0 48 0F B1 0B                  lock cmpxchg qword ptr [rbx], rcx
0088FC6F  74 08                           je 0x14088fc79
0088FC71  48 8B CB                        mov rcx, rbx
0088FC74  E8 C7 37 9D FF                  call 0x140263440
0088FC79  48 8B CB                        mov rcx, rbx
0088FC7C  E8 7F 19 A5 FF                  call 0x1402e1600
0088FC81  48 8B CF                        mov rcx, rdi
0088FC84  E8 57 7E 00 00                  call 0x140897ae0
0088FC89  B8 23 00 00 C0                  mov eax, 0xc0000023
0088FC8E  E9 E3 FE FF FF                  jmp 0x14088fb76
0088FC93  49 8B CF                        mov rcx, r15
0088FC96  E8 B5 96 A6 FF                  call 0x1402f9350
0088FC9B  48 8B CD                        mov rcx, rbp
0088FC9E  E8 AD 96 A6 FF                  call 0x1402f9350
0088FCA3  EB 99                           jmp 0x14088fc3e
0088FCA5  48 8B CD                        mov rcx, rbp
0088FCA8  E8 23 61 9D FF                  call 0x140265dd0
0088FCAD  E9 66 FD FF FF                  jmp 0x14088fa18
0088FCB2  BA 00 20 00 00                  mov edx, 0x2000
0088FCB7  66 0B CA                        or cx, dx
0088FCBA  0F BA F0 09                     btr eax, 9
0088FCBE  E9 C2 FD FF FF                  jmp 0x14088fa85
0088FCC3  49 8B 46 10                     mov rax, qword ptr [r14 + 0x10]
0088FCC7  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
0088FCCC  48 8D 68 F0                     lea rbp, [rax - 0x10]
0088FCD0  48 8B CD                        mov rcx, rbp
0088FCD3  E8 58 05 98 FF                  call 0x140210230
0088FCD8  4C 8B F8                        mov r15, rax
0088FCDB  41 B8 11 00 00 00               mov r8d, 0x11
0088FCE1  33 C0                           xor eax, eax
0088FCE3  F0 4C 0F B1 45 00               lock cmpxchg qword ptr [rbp], r8
0088FCE9  0F 84 D1 96 28 00               je 0x140b193c0
0088FCEF  4C 8B CD                        mov r9, rbp
0088FCF2  4D 8B C7                        mov r8, r15
0088FCF5  33 D2                           xor edx, edx
0088FCF7  48 8B CD                        mov rcx, rbp
0088FCFA  E8 4D 07 98 FF                  call 0x14021044c
0088FCFF  41 B8 11 00 00 00               mov r8d, 0x11
0088FD05  E9 B6 96 28 00                  jmp 0x140b193c0
0088FD0A  F7 86 00 01 00 00 00 10 00 00   test dword ptr [rsi + 0x100], 0x1000
0088FD14  0F 85 2C FC FF FF               jne 0x14088f946
0088FD1A  E9 DF FE FF FF                  jmp 0x14088fbfe
0088FD1F  49 8B CF                        mov rcx, r15
0088FD22  E9 77 FF FF FF                  jmp 0x14088fc9e
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall AlpcpDispatchReplyToPort(__int64 a1, int a2, int a3)
{
    __int64 result;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rsp;
    unsigned int v_stack_m58;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p68;
    unsigned int v_stack_p8;

    v_stack_p20 = v_rbx;
    v_rsp = (v_rsp) - (32);
    a3 = 0;
    a2 = 0;
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 48)));
    result = 0;
    *(unsigned __int64 *)(a1 + 32) = 0;
    *(unsigned __int64 *)(a1 + 24) = 0;
    *(unsigned __int64 *)(a1 + 40) = 0;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 24) + 416))) >> (1));
    result = (unsigned int)((result) & (3));
    if (((unsigned int)(result)) != 2) goto loc_0088FB8C;
    v_stack_p10 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 24) + 16);
    result = KeAbPreAcquire(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 24) + 16) - 16, a2, a3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 24) + 16) - 16;
        a3 = 0;
        a2 = 0;
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 24) + 16) - 16;
        result = ExfAcquirePushLockSharedEx(a1, a2, a3, a4);
        a3 = 17;
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
loc_0088F923:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 416)))) & (32)) != 0) goto loc_0088FBED;
loc_0088F937:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 24) + 416)))) & (32)) != 0) goto loc_0088FD0A;
loc_0088F946:
    if ((*(unsigned __int16 *)(a1 + 52)) > (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 24) + 16) + 16) + 272))) goto loc_0088FC61;
    result = ObReferenceObjectSafe(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 24) + 16) + 16), v_stack_p10, a3, a4);
    a1 = 0;
    v_r15 = 0;
    if ((unsigned __int8)(result) != 0) { v_r15 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 24) + 16) + 16); }
    v_rbp = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 24) + 16) + 16);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 24) + 16) + 16) != 0) {
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 24) + 16) + 16);
        result = ObReferenceObjectSafe(a1, v_stack_p10, a3, a4);
        a1 = 0;
        v_rbp = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 24) + 16) + 16);
        if ((unsigned __int8)(result) == 0) { v_rbp = a1; }
    }
    if (v_r15 == 0) goto loc_0088FC39;
    if (v_rbp == 0) goto loc_0088FD1F;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_r15 + 416)))) & (32)) != 0) goto loc_0088FC93;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rbp + 416)))) & (32)) != 0) goto loc_0088FC93;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 200) = a1;
    if ((*(unsigned __int16 *)(a1 + 54)) != 11) goto loc_0088FA20;
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 24) + 352, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 24) + 352;
        a2 = result;
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 24) + 352;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    result = (unsigned __int8)((-1) & (6));
    if (((unsigned __int8)(result)) == 2) goto loc_0088FCA5;
loc_0088FA18:
    result = KeAbPostRelease(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 24) + 352, a2, a3, a4);
loc_0088FA20:
    *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 242) = (unsigned __int16)(*(unsigned __int16 *)(a1 + 52));
    result = (unsigned __int16)((*(unsigned __int16 *)(a1 + 52)) - (40));
    *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 240) = (unsigned __int16)(result);
    *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 244) = (unsigned __int16)(*(unsigned __int16 *)(a1 + 54));
    *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 246) = (unsigned __int16)(*(unsigned __int16 *)(a1 + 56));
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 248) = v_xmm0;
    if (((v_stack_p8) & (0x10000ULL)) == 0) goto loc_0088FCB2;
    a1 = (unsigned __int16)((*(unsigned __int16 *)(a1 + 54)) & ((unsigned __int16)((unsigned int)(0xFFFFDFFFULL))));
loc_0088FA85:
    *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 244) = (unsigned __int16)(a1);
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 40) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 40)));
    result = AlpcpClearOwnerPortMessage(*(unsigned __int64 *)(a1 + 8), (unsigned int)(0xFFFFDFFFULL), a3, a4);
    result = ObfReferenceObject(*(unsigned __int64 *)(a1), (unsigned int)(0xFFFFDFFFULL), a3, a4);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 24) = *(unsigned __int64 *)(a1);
    result = (unsigned int)((1) + 1);
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 44) = (unsigned int)(result);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 120) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 24) + 16) + 16) + 56);
    result = ObfDereferenceObject(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 24) + 16) + 16), (unsigned int)(0xFFFFDFFFULL), a3, a4);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 16)) != 0) {
        a1 = *(unsigned __int64 *)(a1 + 8);
        result = AlpcpRemoveMessageFromPendingQueue(a1, (unsigned int)(0xFFFFDFFFULL), a3, a4);
    }
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 24) + 16) + 16) + 352, a2, a3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 24) + 16) + 16) + 352;
        a3 = 0;
        a2 = 0;
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 24) + 16) + 16) + 352;
        result = ExfAcquirePushLockSharedEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    if (((v_stack_p8) & (0x20000ULL)) != 0) {
        result = *(unsigned __int64 *)(a1 + 8);
        *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) = *(unsigned __int64 *)(gs_base + (0 + 392));
    }
    *(unsigned __int64 *)(a1 + 16) = v_stack_p10;
    *(unsigned __int64 *)(a1 + 32) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 24) + 16) + 16);
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 8) + 160)) & (1)) != 0) {
    }
    result = AlpcpCompleteDispatchMessage(a1, a2, a3, a4);
    result = 0;
loc_0088FB76:
    v_rsp = (v_rsp) + (32);
    return result;
loc_0088FB8C:
    if (0 == 1) goto loc_0088FCC3;
    v_stack_p68 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 24) + 16);
    result = KeAbPreAcquire(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 24) + 16) - 16, a2, a3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 24) + 16) - 16;
        a3 = 0;
        a2 = 0;
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 24) + 16) - 16;
        result = ExfAcquirePushLockSharedEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    goto loc_0088F923;
loc_0088FBED:
    if (((*(unsigned int *)(*(unsigned __int64 *)(a1) + 256)) & (0x1000ULL)) != 0) goto loc_0088F937;
loc_0088FBFE:
    a1 = 0;
    result = 17;
    if (!(condition_is_equal)) {
        a1 = a2 - 16;
        result = ExfReleasePushLockShared(a1, a2, 17, a4);
    }
loc_0088FC19:
    result = KeAbPostRelease(a2 - 16, a2, 17, a4);
    result = AlpcpCancelMessage(*(unsigned __int64 *)(a1), *(unsigned __int64 *)(a1 + 8), (unsigned int)(0x10000ULL), a4);
    goto loc_0088FB76;
loc_0088FC39:
    if (result != 0) goto loc_0088FC9B;
loc_0088FC3E:
    a1 = 0;
    result = 17;
    if (!(condition_is_equal)) {
        a1 = v_stack_p68 - 16;
        result = ExfReleasePushLockShared(a1, *(unsigned __int64 *)(a1 + 8), (unsigned int)(0x10000ULL), a4);
    }
    goto loc_0088FC19;
loc_0088FC61:
    a1 = 0;
    result = (unsigned int)(0x10000ULL);
    if (!(condition_is_equal)) {
        a1 = *(unsigned __int64 *)(a1 + 8) - 16;
        result = ExfReleasePushLockShared(a1, *(unsigned __int64 *)(a1 + 8), (unsigned int)(0x10000ULL), a4);
    }
    result = KeAbPostRelease(*(unsigned __int64 *)(a1 + 8) - 16, *(unsigned __int64 *)(a1 + 8), (unsigned int)(0x10000ULL), a4);
    result = AlpcpUnlockMessage(*(unsigned __int64 *)(a1 + 8), *(unsigned __int64 *)(a1 + 8), (unsigned int)(0x10000ULL), a4);
    goto loc_0088FB76;
loc_0088FC93:
    result = ObfDereferenceObject(result, *(unsigned __int64 *)(a1 + 8), (unsigned int)(0x10000ULL), a4);
loc_0088FC9B:
loc_0088FC9E:
    result = ObfDereferenceObject(result, *(unsigned __int64 *)(a1 + 8), (unsigned int)(0x10000ULL), a4);
    goto loc_0088FC3E;
loc_0088FCA5:
    result = ExfTryToWakePushLock(result, *(unsigned __int64 *)(a1 + 8), (unsigned int)(0x10000ULL), a4);
    goto loc_0088FA18;
loc_0088FCB2:
    a1 = (unsigned __int16)((result) | ((unsigned __int16)((unsigned int)(0x2000ULL))));
    goto loc_0088FA85;
loc_0088FCC3:
    v_stack_p68 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 16);
    result = KeAbPreAcquire(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 16) - 16, (unsigned int)(0x2000ULL), (unsigned int)(0x10000ULL), a4);
    result = 0;
    a2 = 0;
    result = ExfAcquirePushLockSharedEx(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 16) - 16, a2, 0, *(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 16) - 16);
loc_0088FD0A:
    if (((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 24) + 256)) & (0x1000ULL)) != 0) goto loc_0088F946;
    goto loc_0088FBFE;
loc_0088FD1F:
    goto loc_0088FC9E;
}
```

## 5. (Beta) C Style

```c
int64_t AlpcpDispatchReplyToPort(void *Arg1, int32_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rsp;
    uint32_t v_stack_m58;
    uint64_t v_stack_p10;
    uint64_t v_stack_p20;
    uint64_t v_stack_p68;
    uint32_t v_stack_p8;

    v_stack_p20 = local_rbx;
    local_rsp = (local_rsp) - (32);
    Arg3 = 0;
    Arg2 = 0;
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x30)));
    result = 0;
    *(uint64_t *)(arg1 + 0x20) = 0;
    *(uint64_t *)(arg1 + 0x18) = 0;
    *(uint64_t *)(arg1 + 0x28) = 0;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x18) + 0x1A0))) >> (1));
    result = (uint32_t)((result) & (3));
    if (((uint32_t)(result)) != 2) goto loc_0088FB8C;
    v_stack_p10 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x18) + 0x10);
    result = KeAbPreAcquire(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x18) + 0x10) - 16, Arg2, Arg3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x18) + 0x10) - 16;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x18) + 0x10) - 16;
        result = ExfAcquirePushLockSharedEx(Arg1, Arg2, Arg3, a4);
        Arg3 = 17;
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
loc_0088F923:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x1A0)))) & (32)) != 0) goto loc_0088FBED;
loc_0088F937:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x18) + 0x1A0)))) & (32)) != 0) goto loc_0088FD0A;
loc_0088F946:
    if ((*(uint16_t *)(arg1 + 0x34)) > (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x18) + 0x10) + 0x10) + 0x110))) goto loc_0088FC61;
    result = ObReferenceObjectSafe(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x18) + 0x10) + 0x10), v_stack_p10, Arg3, a4);
    Arg1 = 0;
    local_r15 = 0;
    if ((uint8_t)(result) != 0) { local_r15 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x18) + 0x10) + 0x10); }
    local_rbp = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x18) + 0x10) + 0x10);
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x18) + 0x10) + 0x10) != 0) {
        Arg1 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x18) + 0x10) + 0x10);
        result = ObReferenceObjectSafe(Arg1, v_stack_p10, Arg3, a4);
        Arg1 = 0;
        local_rbp = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x18) + 0x10) + 0x10);
        if ((uint8_t)(result) == 0) { local_rbp = Arg1; }
    }
    if (local_r15 == 0) goto loc_0088FC39;
    if (local_rbp == 0) goto loc_0088FD1F;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_r15 + 0x1A0)))) & (32)) != 0) goto loc_0088FC93;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rbp + 0x1A0)))) & (32)) != 0) goto loc_0088FC93;
    *(void **)(*(uint64_t *)(arg1 + 0x8) + 0xC8) = Arg1;
    if ((*(uint16_t *)(arg1 + 0x36)) != 11) goto loc_0088FA20;
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x18) + 352, Arg2, Arg3, a4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x18) + 352;
        Arg2 = result;
        Arg1 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x18) + 352;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, a4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    result = (uint8_t)((-1) & (6));
    if (((uint8_t)(result)) == 2) goto loc_0088FCA5;
loc_0088FA18:
    result = KeAbPostRelease(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x18) + 352, Arg2, Arg3, a4);
loc_0088FA20:
    *(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0xF2) = (uint16_t)(*(uint16_t *)(arg1 + 0x34));
    result = (uint16_t)((*(uint16_t *)(arg1 + 0x34)) - (40));
    *(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0xF0) = (uint16_t)(result);
    *(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0xF4) = (uint16_t)(*(uint16_t *)(arg1 + 0x36));
    *(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0xF6) = (uint16_t)(*(uint16_t *)(arg1 + 0x38));
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0xF8) = v_xmm0;
    if (((v_stack_p8) & (0x10000ULL)) == 0) goto loc_0088FCB2;
    Arg1 = (uint16_t)((*(uint16_t *)(arg1 + 0x36)) & ((uint16_t)((uint32_t)(0xFFFFDFFFULL))));
loc_0088FA85:
    *(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0xF4) = (uint16_t)(Arg1);
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x28) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x28)));
    result = AlpcpClearOwnerPortMessage(*(uint64_t *)(arg1 + 0x8), (uint32_t)(0xFFFFDFFFULL), Arg3, a4);
    result = ObfReferenceObject(*(uint64_t *)(arg1), (uint32_t)(0xFFFFDFFFULL), Arg3, a4);
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x18) = *(uint64_t *)(arg1);
    result = (uint32_t)((1) + 1);
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x2C) = (uint32_t)(result);
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x78) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x18) + 0x10) + 0x10) + 0x38);
    result = ObfDereferenceObject(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x18) + 0x10) + 0x10), (uint32_t)(0xFFFFDFFFULL), Arg3, a4);
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x10)) != 0) {
        Arg1 = *(uint64_t *)(arg1 + 0x8);
        result = AlpcpRemoveMessageFromPendingQueue(Arg1, (uint32_t)(0xFFFFDFFFULL), Arg3, a4);
    }
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x18) + 0x10) + 0x10) + 352, Arg2, Arg3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x18) + 0x10) + 0x10) + 352;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x18) + 0x10) + 0x10) + 352;
        result = ExfAcquirePushLockSharedEx(Arg1, Arg2, Arg3, a4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    if (((v_stack_p8) & (0x20000ULL)) != 0) {
        result = *(uint64_t *)(arg1 + 0x8);
        *(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) = *(uint64_t *)(gs_base + (0 + 0x188));
    }
    *(uint64_t *)(arg1 + 0x10) = v_stack_p10;
    *(uint64_t *)(arg1 + 0x20) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x18) + 0x10) + 0x10);
    if (((*(uint8_t *)(*(uint64_t *)(arg1 + 0x8) + 0xA0)) & (1)) != 0) {
    }
    result = AlpcpCompleteDispatchMessage(Arg1, Arg2, Arg3, a4);
    result = 0;
loc_0088FB76:
    local_rsp = (local_rsp) + (32);
    return result;
loc_0088FB8C:
    if (0 == 1) goto loc_0088FCC3;
    v_stack_p68 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x18) + 0x10);
    result = KeAbPreAcquire(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x18) + 0x10) - 16, Arg2, Arg3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x18) + 0x10) - 16;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x18) + 0x10) - 16;
        result = ExfAcquirePushLockSharedEx(Arg1, Arg2, Arg3, a4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    goto loc_0088F923;
loc_0088FBED:
    if (((*(uint32_t *)(*(uint64_t *)(arg1) + 0x100)) & (0x1000ULL)) != 0) goto loc_0088F937;
loc_0088FBFE:
    Arg1 = 0;
    result = 17;
    if (!(condition_is_equal)) {
        Arg1 = Arg2 - 16;
        result = ExfReleasePushLockShared(Arg1, Arg2, 17, a4);
    }
loc_0088FC19:
    result = KeAbPostRelease(Arg2 - 16, Arg2, 17, a4);
    result = AlpcpCancelMessage(*(uint64_t *)(arg1), *(uint64_t *)(arg1 + 0x8), (uint32_t)(0x10000ULL), a4);
    goto loc_0088FB76;
loc_0088FC39:
    if (result != 0) goto loc_0088FC9B;
loc_0088FC3E:
    Arg1 = 0;
    result = 17;
    if (!(condition_is_equal)) {
        Arg1 = v_stack_p68 - 16;
        result = ExfReleasePushLockShared(Arg1, *(uint64_t *)(arg1 + 0x8), (uint32_t)(0x10000ULL), a4);
    }
    goto loc_0088FC19;
loc_0088FC61:
    Arg1 = 0;
    result = (uint32_t)(0x10000ULL);
    if (!(condition_is_equal)) {
        Arg1 = *(uint64_t *)(arg1 + 0x8) - 16;
        result = ExfReleasePushLockShared(Arg1, *(uint64_t *)(arg1 + 0x8), (uint32_t)(0x10000ULL), a4);
    }
    result = KeAbPostRelease(*(uint64_t *)(arg1 + 0x8) - 16, *(uint64_t *)(arg1 + 0x8), (uint32_t)(0x10000ULL), a4);
    result = AlpcpUnlockMessage(*(uint64_t *)(arg1 + 0x8), *(uint64_t *)(arg1 + 0x8), (uint32_t)(0x10000ULL), a4);
    goto loc_0088FB76;
loc_0088FC93:
    result = ObfDereferenceObject(result, *(uint64_t *)(arg1 + 0x8), (uint32_t)(0x10000ULL), a4);
loc_0088FC9B:
loc_0088FC9E:
    result = ObfDereferenceObject(result, *(uint64_t *)(arg1 + 0x8), (uint32_t)(0x10000ULL), a4);
    goto loc_0088FC3E;
loc_0088FCA5:
    result = ExfTryToWakePushLock(result, *(uint64_t *)(arg1 + 0x8), (uint32_t)(0x10000ULL), a4);
    goto loc_0088FA18;
loc_0088FCB2:
    Arg1 = (uint16_t)((result) | ((uint16_t)((uint32_t)(0x2000ULL))));
    goto loc_0088FA85;
loc_0088FCC3:
    v_stack_p68 = *(uint64_t *)(*(uint64_t *)(arg1) + 0x10);
    result = KeAbPreAcquire(*(uint64_t *)(*(uint64_t *)(arg1) + 0x10) - 16, (uint32_t)(0x2000ULL), (uint32_t)(0x10000ULL), a4);
    result = 0;
    Arg2 = 0;
    result = ExfAcquirePushLockSharedEx(*(uint64_t *)(*(uint64_t *)(arg1) + 0x10) - 16, Arg2, 0, *(uint64_t *)(*(uint64_t *)(arg1) + 0x10) - 16);
loc_0088FD0A:
    if (((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x18) + 0x100)) & (0x1000ULL)) != 0) goto loc_0088F946;
    goto loc_0088FBFE;
loc_0088FD1F:
    goto loc_0088FC9E;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x10` | `64` | `W` |
| `Arg1` | `+ 0x18` | `64` | `W` |
| `Arg1` | `+ 0x20` | `64` | `W` |
| `Arg1` | `+ 0x28` | `64` | `W` |
| `Arg1` | `+ 0x30` | `32` | `R` |
| `Arg1` | `+ 0x30` | `32` | `R/W` |
| `Arg1` | `+ 0x34` | `16` | `R` |
| `Arg1` | `+ 0x36` | `16` | `R` |
| `Arg1` | `+ 0x38` | `16` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0088F880&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
