# ExpWnfDispatchKernelSubscription

- RVA: `0x0090C520`–`0x0090C925` (길이 `1,029` bytes)
- VA: `0x000000014090C520`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00089288`
- 디코드: `268`개 명령, `1,029/1,029` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **27**; 고유 호출 대상: **14**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0090C56B` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0090C584` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x0090C601` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0090C616` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x0090C66E` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0090C67B` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0090C69D` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)
- `0x0090C6CD` → [ExfAcquireRundownProtection](../../text/34/ExfAcquireRundownProtection_function_0034C050.md) (function, `0x0034C050`)
- `0x0090C70E` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x0090C716` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0090C77C` → [PopWnfSprActiveSessionChangeCallback](PopWnfSprActiveSessionChangeCallback_function_0090C930.md) (function, `0x0090C930`)
- `0x0090C784` → [ExpWnfValidateKernelCallbackEnvironment](ExpWnfValidateKernelCallbackEnvironment_function_0090CA18.md) (function, `0x0090CA18`)
- `0x0090C7A9` → [ExpWnfNotifyNameSubscribers](ExpWnfNotifyNameSubscribers_function_0090C160.md) (function, `0x0090C160`)
- `0x0090C7D8` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0090C7F1` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x0090C833` → [ExfReleaseRundownProtection](../../text/34/ExfReleaseRundownProtection_function_00349EB0.md) (function, `0x00349EB0`)
- `0x0090C858` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0090C866` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0090C873` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0090C88C` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x0090C8AC` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0090C8BE` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x0090C8CB` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x0090C8EF` → [ExfReleaseRundownProtection](../../text/34/ExfReleaseRundownProtection_function_00349EB0.md) (function, `0x00349EB0`)
- `0x0090C8FD` → [ExfAcquireRundownProtection](../../text/34/ExfAcquireRundownProtection_function_0034C050.md) (function, `0x0034C050`)
- `0x0090C90E` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x0090C91B` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [ExpWnfNotifyNameSubscribers](ExpWnfNotifyNameSubscribers_function_0090C160.md) at `0x0090C46E`
- [ExpWnfWorkItemRoutine](ExpWnfWorkItemRoutine_function_0090C4C0.md) at `0x0090C4E1`
- [ExpWnfStartKernelDispatcher](../9D/ExpWnfStartKernelDispatcher_function_009D5AF8.md) at `0x009D5B3C`

### Static image references
- `0x0090C536` → RVA `0x00E0A740` (`.data`; read)
- `0x0090C551` → RVA `0x00FC6AB0` (`ALMOSTRO`; read)
- `0x0090C753` → RVA `0x0090C930` (`PopWnfSprActiveSessionChangeCallback`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **24**
  - `0x0090C56B` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x0090C584` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x0090C601` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0090C616` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x0090C66E` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0090C67B` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x0090C69D` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (`PAGE` → `.text`)
  - `0x0090C6CD` → [ExfAcquireRundownProtection](../../text/34/ExfAcquireRundownProtection_function_0034C050.md) (`PAGE` → `.text`)
  - `0x0090C70E` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x0090C716` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0090C7D8` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x0090C7F1` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x0090C833` → [ExfReleaseRundownProtection](../../text/34/ExfReleaseRundownProtection_function_00349EB0.md) (`PAGE` → `.text`)
  - `0x0090C858` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0090C866` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (`PAGE` → `.text`)
  - `0x0090C873` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x0090C88C` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x0090C8AC` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (`PAGE` → `.text`)
  - `0x0090C8BE` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x0090C8CB` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x0090C8EF` → [ExfReleaseRundownProtection](../../text/34/ExfReleaseRundownProtection_function_00349EB0.md) (`PAGE` → `.text`)
  - `0x0090C8FD` → [ExfAcquireRundownProtection](../../text/34/ExfAcquireRundownProtection_function_0034C050.md) (`PAGE` → `.text`)
  - `0x0090C90E` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x0090C91B` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0090C520  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
0090C525  48 89 6C 24 18                  mov qword ptr [rsp + 0x18], rbp
0090C52A  56                              push rsi
0090C52B  57                              push rdi
0090C52C  41 54                           push r12
0090C52E  41 56                           push r14
0090C530  41 57                           push r15
0090C532  48 83 EC 70                     sub rsp, 0x70
0090C536  48 8B 05 03 E2 4F 00            mov rax, qword ptr [rip + 0x4fe203]
0090C53D  48 33 C4                        xor rax, rsp
0090C540  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
0090C545  33 C0                           xor eax, eax
0090C547  45 33 C0                        xor r8d, r8d
0090C54A  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
0090C54F  33 D2                           xor edx, edx
0090C551  48 8B 05 58 A5 6B 00            mov rax, qword ptr [rip + 0x6ba558]
0090C558  4C 8B B8 E8 05 00 00            mov r15, qword ptr [rax + 0x5e8]
0090C55F  4C 89 7C 24 48                  mov qword ptr [rsp + 0x48], r15
0090C564  49 8D 77 68                     lea rsi, [r15 + 0x68]
0090C568  48 8B CE                        mov rcx, rsi
0090C56B  E8 C0 3C 90 FF                  call 0x140210230
0090C570  F0 48 0F BA 2E 00               lock bts qword ptr [rsi], 0
0090C576  48 8B D8                        mov rbx, rax
0090C579  73 0E                           jae 0x14090c589
0090C57B  4C 8B C6                        mov r8, rsi
0090C57E  48 8B D0                        mov rdx, rax
0090C581  48 8B CE                        mov rcx, rsi
0090C584  E8 07 37 90 FF                  call 0x14020fc90
0090C589  48 85 DB                        test rbx, rbx
0090C58C  74 04                           je 0x14090c592
0090C58E  C6 43 0A 01                     mov byte ptr [rbx + 0xa], 1
0090C592  4D 8D 77 70                     lea r14, [r15 + 0x70]
0090C596  4C 89 AC 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], r13
0090C59E  48 C7 C3 FF FF FF FF            mov rbx, 0xffffffffffffffff
0090C5A5  49 8B 3E                        mov rdi, qword ptr [r14]
0090C5A8  49 3B FE                        cmp rdi, r14
0090C5AB  74 40                           je 0x14090c5ed
0090C5AD  48 8D 6F 98                     lea rbp, [rdi - 0x68]
0090C5B1  0F 0D 4D 08                     prefetchw byte ptr [rbp + 8]
0090C5B5  48 8B 45 08                     mov rax, qword ptr [rbp + 8]
0090C5B9  48 83 E0 FE                     and rax, 0xfffffffffffffffe
0090C5BD  48 8D 48 02                     lea rcx, [rax + 2]
0090C5C1  F0 48 0F B1 4D 08               lock cmpxchg qword ptr [rbp + 8], rcx
0090C5C7  0F 85 2C 03 00 00               jne 0x14090c8f9
0090C5CD  C7 45 78 02 00 00 00            mov dword ptr [rbp + 0x78], 2
0090C5D4  48 8B 0F                        mov rcx, qword ptr [rdi]
0090C5D7  48 39 79 08                     cmp qword ptr [rcx + 8], rdi
0090C5DB  75 09                           jne 0x14090c5e6
0090C5DD  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
0090C5E1  48 39 38                        cmp qword ptr [rax], rdi
0090C5E4  74 4F                           je 0x14090c635
0090C5E6  B9 03 00 00 00                  mov ecx, 3
0090C5EB  CD 29                           int 0x29
0090C5ED  F0 48 0F C1 1E                  lock xadd qword ptr [rsi], rbx
0090C5F2  80 E3 06                        and bl, 6
0090C5F5  80 FB 02                        cmp bl, 2
0090C5F8  0F 84 CA 02 00 00               je 0x14090c8c8
0090C5FE  48 8B CE                        mov rcx, rsi
0090C601  E8 FA 4F 9D FF                  call 0x1402e1600
0090C606  4C 8B AC 24 A0 00 00 00         mov r13, qword ptr [rsp + 0xa0]
0090C60E  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
0090C613  48 33 CC                        xor rcx, rsp
0090C616  E8 25 00 DA FF                  call 0x1406ac640
0090C61B  4C 8D 5C 24 70                  lea r11, [rsp + 0x70]
0090C620  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
0090C624  49 8B 6B 40                     mov rbp, qword ptr [r11 + 0x40]
0090C628  49 8B E3                        mov rsp, r11
0090C62B  41 5F                           pop r15
0090C62D  41 5E                           pop r14
0090C62F  41 5C                           pop r12
0090C631  5F                              pop rdi
0090C632  5E                              pop rsi
0090C633  C3                              ret
0090C634  CC                              int3
0090C635  4D 8D 67 50                     lea r12, [r15 + 0x50]
0090C639  48 89 08                        mov qword ptr [rax], rcx
0090C63C  4C 89 64 24 50                  mov qword ptr [rsp + 0x50], r12
0090C641  48 89 41 08                     mov qword ptr [rcx + 8], rax
0090C645  66 66 66 0F 1F 84 00 00 00 00 00  nop word ptr [rax + rax]
0090C650  44 8B 7D 7C                     mov r15d, dword ptr [rbp + 0x7c]
0090C654  33 C0                           xor eax, eax
0090C656  89 45 7C                        mov dword ptr [rbp + 0x7c], eax
0090C659  48 8B C3                        mov rax, rbx
0090C65C  F0 48 0F C1 06                  lock xadd qword ptr [rsi], rax
0090C661  24 06                           and al, 6
0090C663  3C 02                           cmp al, 2
0090C665  0F 84 50 02 00 00               je 0x14090c8bb
0090C66B  48 8B CE                        mov rcx, rsi
0090C66E  E8 8D 4F 9D FF                  call 0x1402e1600
0090C673  45 33 C0                        xor r8d, r8d
0090C676  33 D2                           xor edx, edx
0090C678  49 8B CC                        mov rcx, r12
0090C67B  E8 B0 3B 90 FF                  call 0x140210230
0090C680  48 8B F8                        mov rdi, rax
0090C683  B9 11 00 00 00                  mov ecx, 0x11
0090C688  33 C0                           xor eax, eax
0090C68A  F0 49 0F B1 0C 24               lock cmpxchg qword ptr [r12], rcx
0090C690  74 10                           je 0x14090c6a2
0090C692  4D 8B CC                        mov r9, r12
0090C695  4C 8B C7                        mov r8, rdi
0090C698  33 D2                           xor edx, edx
0090C69A  49 8B CC                        mov rcx, r12
0090C69D  E8 AA 3D 90 FF                  call 0x14021044c
0090C6A2  48 85 FF                        test rdi, rdi
0090C6A5  74 04                           je 0x14090c6ab
0090C6A7  C6 47 0A 01                     mov byte ptr [rdi + 0xa], 1
0090C6AB  48 8B 7D 30                     mov rdi, qword ptr [rbp + 0x30]
0090C6AF  48 85 FF                        test rdi, rdi
0090C6B2  74 26                           je 0x14090c6da
0090C6B4  48 8D 4F 08                     lea rcx, [rdi + 8]
0090C6B8  0F 0D 09                        prefetchw byte ptr [rcx]
0090C6BB  48 8B 01                        mov rax, qword ptr [rcx]
0090C6BE  48 83 E0 FE                     and rax, 0xfffffffffffffffe
0090C6C2  48 8D 50 02                     lea rdx, [rax + 2]
0090C6C6  F0 48 0F B1 11                  lock cmpxchg qword ptr [rcx], rdx
0090C6CB  74 11                           je 0x14090c6de
0090C6CD  E8 7E F9 A3 FF                  call 0x14034c050
0090C6D2  84 C0                           test al, al
0090C6D4  75 08                           jne 0x14090c6de
0090C6D6  33 C0                           xor eax, eax
0090C6D8  8B F8                           mov edi, eax
0090C6DA  41 83 E7 FE                     and r15d, 0xfffffffe
0090C6DE  41 F6 C7 01                     test r15b, 1
0090C6E2  74 0F                           je 0x14090c6f3
0090C6E4  8B 47 60                        mov eax, dword ptr [rdi + 0x60]
0090C6E7  3B 45 60                        cmp eax, dword ptr [rbp + 0x60]
0090C6EA  0F 86 4D 01 00 00               jbe 0x14090c83d
0090C6F0  89 45 60                        mov dword ptr [rbp + 0x60], eax
0090C6F3  B8 11 00 00 00                  mov eax, 0x11
0090C6F8  45 85 FF                        test r15d, r15d
0090C6FB  0F 84 45 01 00 00               je 0x14090c846
0090C701  33 C9                           xor ecx, ecx
0090C703  F0 49 0F B1 0C 24               lock cmpxchg qword ptr [r12], rcx
0090C709  74 08                           je 0x14090c713
0090C70B  49 8B CC                        mov rcx, r12
0090C70E  E8 2D 6D 95 FF                  call 0x140263440
0090C713  49 8B CC                        mov rcx, r12
0090C716  E8 E5 4E 9D FF                  call 0x1402e1600
0090C71B  48 8B 45 38                     mov rax, qword ptr [rbp + 0x38]
0090C71F  48 B9 74 00 BC A3 6D 4E C6 41   movabs rcx, 0x41c64e6da3bc0074
0090C729  48 33 C1                        xor rax, rcx
0090C72C  45 8B E7                        mov r12d, r15d
0090C72F  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
0090C734  48 85 FF                        test rdi, rdi
0090C737  0F 84 A2 01 00 00               je 0x14090c8df
0090C73D  48 8B 4F 40                     mov rcx, qword ptr [rdi + 0x40]
0090C741  41 83 E4 01                     and r12d, 1
0090C745  0F 84 BC 01 00 00               je 0x14090c907
0090C74B  44 8B 4F 60                     mov r9d, dword ptr [rdi + 0x60]
0090C74F  48 8B 45 58                     mov rax, qword ptr [rbp + 0x58]
0090C753  48 8D 15 D6 01 00 00            lea rdx, [rip + 0x1d6]
0090C75A  4C 8B 55 50                     mov r10, qword ptr [rbp + 0x50]
0090C75E  45 8B C7                        mov r8d, r15d
0090C761  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0090C766  4C 3B D2                        cmp r10, rdx
0090C769  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0090C76E  48 8D 54 24 58                  lea rdx, [rsp + 0x58]
0090C773  48 8B CD                        mov rcx, rbp
0090C776  0F 85 9C 01 00 00               jne 0x14090c918
0090C77C  E8 AF 01 00 00                  call 0x14090c930
0090C781  48 8B CD                        mov rcx, rbp
0090C784  E8 8F 02 00 00                  call 0x14090ca18
0090C789  45 85 E4                        test r12d, r12d
0090C78C  74 20                           je 0x14090c7ae
0090C78E  8B C3                           mov eax, ebx
0090C790  F0 0F C1 87 A4 00 00 00         lock xadd dword ptr [rdi + 0xa4], eax
0090C798  83 F8 01                        cmp eax, 1
0090C79B  75 11                           jne 0x14090c7ae
0090C79D  45 33 C9                        xor r9d, r9d
0090C7A0  8D 50 07                        lea edx, [rax + 7]
0090C7A3  45 33 C0                        xor r8d, r8d
0090C7A6  48 8B CF                        mov rcx, rdi
0090C7A9  E8 B2 F9 FF FF                  call 0x14090c160
0090C7AE  48 85 FF                        test rdi, rdi
0090C7B1  74 1D                           je 0x14090c7d0
0090C7B3  48 8D 4F 08                     lea rcx, [rdi + 8]
0090C7B7  0F 0D 09                        prefetchw byte ptr [rcx]
0090C7BA  48 8B 01                        mov rax, qword ptr [rcx]
0090C7BD  48 83 E0 FE                     and rax, 0xfffffffffffffffe
0090C7C1  48 8D 50 FE                     lea rdx, [rax - 2]
0090C7C5  F0 48 0F B1 11                  lock cmpxchg qword ptr [rcx], rdx
0090C7CA  0F 85 1F 01 00 00               jne 0x14090c8ef
0090C7D0  45 33 C0                        xor r8d, r8d
0090C7D3  33 D2                           xor edx, edx
0090C7D5  48 8B CE                        mov rcx, rsi
0090C7D8  E8 53 3A 90 FF                  call 0x140210230
0090C7DD  F0 48 0F BA 2E 00               lock bts qword ptr [rsi], 0
0090C7E3  48 8B F8                        mov rdi, rax
0090C7E6  73 0E                           jae 0x14090c7f6
0090C7E8  4C 8B C6                        mov r8, rsi
0090C7EB  48 8B D0                        mov rdx, rax
0090C7EE  48 8B CE                        mov rcx, rsi
0090C7F1  E8 9A 34 90 FF                  call 0x14020fc90
0090C7F6  48 85 FF                        test rdi, rdi
0090C7F9  74 04                           je 0x14090c7ff
0090C7FB  C6 47 0A 01                     mov byte ptr [rdi + 0xa], 1
0090C7FF  83 7D 7C 00                     cmp dword ptr [rbp + 0x7c], 0
0090C803  0F 85 CC 00 00 00               jne 0x14090c8d5
0090C809  33 C0                           xor eax, eax
0090C80B  89 45 78                        mov dword ptr [rbp + 0x78], eax
0090C80E  0F 0D 4D 08                     prefetchw byte ptr [rbp + 8]
0090C812  48 8B 45 08                     mov rax, qword ptr [rbp + 8]
0090C816  48 83 E0 FE                     and rax, 0xfffffffffffffffe
0090C81A  48 8D 50 FE                     lea rdx, [rax - 2]
0090C81E  F0 48 0F B1 55 08               lock cmpxchg qword ptr [rbp + 8], rdx
0090C824  4C 8B 7C 24 48                  mov r15, qword ptr [rsp + 0x48]
0090C829  0F 84 76 FD FF FF               je 0x14090c5a5
0090C82F  48 8D 4D 08                     lea rcx, [rbp + 8]
0090C833  E8 78 D6 A3 FF                  call 0x140349eb0
0090C838  E9 68 FD FF FF                  jmp 0x14090c5a5
0090C83D  41 83 E7 FE                     and r15d, 0xfffffffe
0090C841  E9 AD FE FF FF                  jmp 0x14090c6f3
0090C846  45 33 FF                        xor r15d, r15d
0090C849  F0 4D 0F B1 3C 24               lock cmpxchg qword ptr [r12], r15
0090C84F  0F 85 B6 00 00 00               jne 0x14090c90b
0090C855  49 8B CC                        mov rcx, r12
0090C858  E8 A3 4D 9D FF                  call 0x1402e1600
0090C85D  48 85 FF                        test rdi, rdi
0090C860  74 09                           je 0x14090c86b
0090C862  48 8D 4F 08                     lea rcx, [rdi + 8]
0090C866  E8 15 D6 A3 FF                  call 0x140349e80
0090C86B  45 33 C0                        xor r8d, r8d
0090C86E  33 D2                           xor edx, edx
0090C870  48 8B CE                        mov rcx, rsi
0090C873  E8 B8 39 90 FF                  call 0x140210230
0090C878  F0 48 0F BA 2E 00               lock bts qword ptr [rsi], 0
0090C87E  48 8B F8                        mov rdi, rax
0090C881  73 0E                           jae 0x14090c891
0090C883  4C 8B C6                        mov r8, rsi
0090C886  48 8B D0                        mov rdx, rax
0090C889  48 8B CE                        mov rcx, rsi
0090C88C  E8 FF 33 90 FF                  call 0x14020fc90
0090C891  48 85 FF                        test rdi, rdi
0090C894  74 04                           je 0x14090c89a
0090C896  C6 47 0A 01                     mov byte ptr [rdi + 0xa], 1
0090C89A  44 39 7D 7C                     cmp dword ptr [rbp + 0x7c], r15d
0090C89E  0F 85 AC FD FF FF               jne 0x14090c650
0090C8A4  48 8D 4D 08                     lea rcx, [rbp + 8]
0090C8A8  44 89 7D 78                     mov dword ptr [rbp + 0x78], r15d
0090C8AC  E8 CF D5 A3 FF                  call 0x140349e80
0090C8B1  4C 8B 7C 24 48                  mov r15, qword ptr [rsp + 0x48]
0090C8B6  E9 EA FC FF FF                  jmp 0x14090c5a5
0090C8BB  48 8B CE                        mov rcx, rsi
0090C8BE  E8 0D 95 95 FF                  call 0x140265dd0
0090C8C3  E9 A3 FD FF FF                  jmp 0x14090c66b
0090C8C8  48 8B CE                        mov rcx, rsi
0090C8CB  E8 00 95 95 FF                  call 0x140265dd0
0090C8D0  E9 29 FD FF FF                  jmp 0x14090c5fe
0090C8D5  4C 8B 64 24 50                  mov r12, qword ptr [rsp + 0x50]
0090C8DA  E9 71 FD FF FF                  jmp 0x14090c650
0090C8DF  33 C0                           xor eax, eax
0090C8E1  8B C8                           mov ecx, eax
0090C8E3  41 83 E4 01                     and r12d, 1
0090C8E7  44 8B C8                        mov r9d, eax
0090C8EA  E9 60 FE FF FF                  jmp 0x14090c74f
0090C8EF  E8 BC D5 A3 FF                  call 0x140349eb0
0090C8F4  E9 D7 FE FF FF                  jmp 0x14090c7d0
0090C8F9  48 8D 4D 08                     lea rcx, [rbp + 8]
0090C8FD  E8 4E F7 A3 FF                  call 0x14034c050
0090C902  E9 C6 FC FF FF                  jmp 0x14090c5cd
0090C907  33 C0                           xor eax, eax
0090C909  EB DC                           jmp 0x14090c8e7
0090C90B  49 8B CC                        mov rcx, r12
0090C90E  E8 2D 6B 95 FF                  call 0x140263440
0090C913  E9 3D FF FF FF                  jmp 0x14090c855
0090C918  49 8B C2                        mov rax, r10
0090C91B  E8 B0 E1 DA FF                  call 0x1406baad0
0090C920  E9 5C FE FF FF                  jmp 0x14090c781
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExpWnfDispatchKernelSubscription(__int64 a1, int a2, int a3)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p10 = v_rbx;
    v_stack_p18 = v_rbp;
    v_rsp = (v_rsp) - (112);
    result = (*(unsigned __int64 *)(v_rip + 5235203)) ^ (v_rsp);
    v_stack_m38 = result;
    result = 0;
    a3 = 0;
    v_stack_m40 = 0;
    a2 = 0;
    v_stack_m50 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7054680) + 1512);
    result = KeAbPreAcquire(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7054680) + 1512) + 104, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7054680) + 1512) + 104;
        a2 = result;
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7054680) + 1512) + 104;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    v_stack_p8 = v_r13;
loc_0090C5A5:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7054680) + 1512) + 112)) == (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7054680) + 1512) + 112)) goto loc_0090C5ED;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7054680) + 1512) + 112) - 104 + 8)) & (-2);
    if (condition_is_not_equal) goto loc_0090C8F9;
loc_0090C5CD:
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7054680) + 1512) + 112) - 104 + 120) = 2;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7054680) + 1512) + 112)) + 8)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7054680) + 1512) + 112))) goto loc_0090C5E6;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7054680) + 1512) + 112) + 8))) == (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7054680) + 1512) + 112))) goto loc_0090C635;
loc_0090C5E6:
loc_0090C5ED:
    v_rbx = (unsigned __int8)((-1) & (6));
    if (((unsigned __int8)(v_rbx)) == 2) goto loc_0090C8C8;
loc_0090C5FE:
    result = KeAbPostRelease(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7054680) + 1512) + 104, a2, a3, a4);
    a1 = (v_stack_m38) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    return result;
loc_0090C635:
    *(unsigned __int64 *)(result) = a1;
    v_stack_m20 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7054680) + 1512) + 80;
    *(unsigned __int64 *)(a1 + 8) = result;
loc_0090C650:
    result = 0;
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 124) = 0;
    result = (unsigned __int8)((*(unsigned __int64 *)(v_stack_m28 + 56)) & (6));
    if (((unsigned __int8)(result)) == 2) goto loc_0090C8BB;
loc_0090C66B:
    result = KeAbPostRelease(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7054680) + 1512) + 104, a2, a3, a4);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7054680) + 1512) + 80, a2, a3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7054680) + 1512) + 80;
        a3 = 0;
        a2 = 0;
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7054680) + 1512) + 80;
        result = ExfAcquirePushLockSharedEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 48) == 0) goto loc_0090C6DA;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 48) + 8)) & (-2);
    if (condition_is_equal) goto loc_0090C6DE;
    result = ExfAcquireRundownProtection(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 48) + 8, result + 2, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_0090C6DE;
    result = 0;
loc_0090C6DA:
    v_r15 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 124))) & (0xFFFFFFFEULL));
loc_0090C6DE:
    if ((((unsigned __int8)(v_r15)) & (1)) == 0) goto loc_0090C6F3;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(0 + 96)))) <= (*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 96))) goto loc_0090C83D;
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 96) = (unsigned int)((unsigned int)(*(unsigned int *)(0 + 96)));
loc_0090C6F3:
    if ((unsigned int)(v_r15) == 0) goto loc_0090C846;
    a1 = 0;
    result = 17;
    if (!(condition_is_equal)) {
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7054680) + 1512) + 80;
        result = ExfReleasePushLockShared(a1, result + 2, a3, a4);
    }
    result = KeAbPostRelease(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7054680) + 1512) + 80, result + 2, a3, a4);
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 56)) ^ (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7054680) + 1512) + 80);
    v_stack_m18 = result;
    if (0 == 0) goto loc_0090C8DF;
    v_r12 = (unsigned int)(((unsigned int)((unsigned int)(v_r15))) & (1));
    if (condition_is_equal) goto loc_0090C907;
loc_0090C74F:
    v_stack_m48 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 88);
    v_stack_m50 = *(unsigned __int64 *)(0 + 64);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 80)) != (v_rip + 470)) goto loc_0090C918;
    result = PopWnfSprActiveSessionChangeCallback(*(unsigned __int64 *)(v_stack_m28 + 64), v_stack_m18, (unsigned int)((unsigned int)(v_r15)), (unsigned int)(*(unsigned int *)(0 + 96)));
loc_0090C781:
    result = ExpWnfValidateKernelCallbackEnvironment(*(unsigned __int64 *)(v_stack_m28 + 64), v_stack_m18, (unsigned int)((unsigned int)(v_r15)), (unsigned int)(*(unsigned int *)(0 + 96)));
    if ((unsigned int)(v_r12) == 0) goto loc_0090C7AE;
    result = (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 56)));
    if (((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 56))))) == 1) {
        a4 = 0;
        a2 = (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 56))) + 7;
        a3 = 0;
        a1 = 0;
        result = ExpWnfNotifyNameSubscribers(a1, a2, a3, a4);
    }
    if (0 == 0) goto loc_0090C7D0;
    result = (*(unsigned __int64 *)(0 + 8)) & (-2);
    if (condition_is_not_equal) goto loc_0090C8EF;
loc_0090C7D0:
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7054680) + 1512) + 104, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7054680) + 1512) + 104;
        a2 = result;
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7054680) + 1512) + 104;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 124)) != 0) goto loc_0090C8D5;
    result = 0;
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 120) = 0;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 8)) & (-2);
    if (condition_is_equal) goto loc_0090C5A5;
    result = ExfReleaseRundownProtection(*(unsigned __int64 *)(v_stack_m28 + 64) + 8, result - 2, a3, a4);
    goto loc_0090C5A5;
loc_0090C83D:
    v_r15 = (unsigned int)((v_stack_m28) & (0xFFFFFFFEULL));
    goto loc_0090C6F3;
loc_0090C846:
    v_r15 = 0;
    if (condition_is_not_equal) goto loc_0090C90B;
loc_0090C855:
    result = KeAbPostRelease(v_r12, result - 2, a3, a4);
    if (result != 0) {
        a1 = result + 8;
        result = ExReleaseRundownProtection(a1, result - 2, a3, a4);
    }
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7054680) + 1512) + 104, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7054680) + 1512) + 104;
        a2 = result;
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7054680) + 1512) + 104;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 124)) != 0) goto loc_0090C650;
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 120) = 0;
    result = ExReleaseRundownProtection(*(unsigned __int64 *)(v_stack_m28 + 64) + 8, a2, a3, a4);
    goto loc_0090C5A5;
loc_0090C8BB:
    result = ExfTryToWakePushLock(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7054680) + 1512) + 104, a2, a3, a4);
    goto loc_0090C66B;
loc_0090C8C8:
    result = ExfTryToWakePushLock(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7054680) + 1512) + 104, a2, a3, a4);
    goto loc_0090C5FE;
loc_0090C8D5:
    goto loc_0090C650;
loc_0090C8DF:
    result = 0;
    v_r12 = (unsigned int)((v_stack_m20) & (1));
loc_0090C8E7:
    goto loc_0090C74F;
loc_0090C8EF:
    result = ExfReleaseRundownProtection(0, a2, a3, 0);
    goto loc_0090C7D0;
loc_0090C8F9:
    result = ExfAcquireRundownProtection(*(unsigned __int64 *)(v_stack_m28 + 64) + 8, a2, a3, 0);
    goto loc_0090C5CD;
loc_0090C907:
    result = 0;
    goto loc_0090C8E7;
loc_0090C90B:
    result = ExfReleasePushLockShared(v_r12, a2, a3, 0);
    goto loc_0090C855;
loc_0090C918:
    result = guard_dispatch_icall(v_r12, a2, a3, 0);
    goto loc_0090C781;
}
```

## 5. (Beta) C Style

```c
int64_t ExpWnfDispatchKernelSubscription(int64_t Arg1, int32_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_r12;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p10 = local_rbx;
    v_stack_p18 = local_rbp;
    local_rsp = (local_rsp) - (112);
    result = (*(uint64_t *)(v_rip + 0x4FE203)) ^ (local_rsp);
    v_stack_m38 = result;
    result = 0;
    Arg3 = 0;
    v_stack_m40 = 0;
    Arg2 = 0;
    v_stack_m50 = *(uint64_t *)(*(uint64_t *)(v_rip + 0x6BA558) + 0x5E8);
    result = KeAbPreAcquire(*(uint64_t *)(*(uint64_t *)(v_rip + 0x6BA558) + 0x5E8) + 104, Arg2, Arg3, a4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = *(uint64_t *)(*(uint64_t *)(v_rip + 0x6BA558) + 0x5E8) + 104;
        Arg2 = result;
        Arg1 = *(uint64_t *)(*(uint64_t *)(v_rip + 0x6BA558) + 0x5E8) + 104;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, a4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    v_stack_p8 = local_r13;
loc_0090C5A5:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x6BA558) + 0x5E8) + 0x70)) == (*(uint64_t *)(*(uint64_t *)(v_rip + 0x6BA558) + 0x5E8) + 112)) goto loc_0090C5ED;
    result = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x6BA558) + 0x5E8) + 0x70) - 0x68 + 0x8)) & (-2);
    if (condition_is_not_equal) goto loc_0090C8F9;
loc_0090C5CD:
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x6BA558) + 0x5E8) + 0x70) - 0x68 + 0x78) = 2;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x6BA558) + 0x5E8) + 0x70)) + 0x8)) != (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x6BA558) + 0x5E8) + 0x70))) goto loc_0090C5E6;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x6BA558) + 0x5E8) + 0x70) + 0x8))) == (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x6BA558) + 0x5E8) + 0x70))) goto loc_0090C635;
loc_0090C5E6:
loc_0090C5ED:
    local_rbx = (uint8_t)((-1) & (6));
    if (((uint8_t)(local_rbx)) == 2) goto loc_0090C8C8;
loc_0090C5FE:
    result = KeAbPostRelease(*(uint64_t *)(*(uint64_t *)(v_rip + 0x6BA558) + 0x5E8) + 104, Arg2, Arg3, a4);
    Arg1 = (v_stack_m38) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, a4);
    return result;
loc_0090C635:
    *(uint64_t *)(result) = Arg1;
    v_stack_m20 = *(uint64_t *)(*(uint64_t *)(v_rip + 0x6BA558) + 0x5E8) + 80;
    *(uint64_t *)(Arg1 + 0x8) = result;
loc_0090C650:
    result = 0;
    *(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x7C) = 0;
    result = (uint8_t)((*(uint64_t *)(v_stack_m28 + 0x38)) & (6));
    if (((uint8_t)(result)) == 2) goto loc_0090C8BB;
loc_0090C66B:
    result = KeAbPostRelease(*(uint64_t *)(*(uint64_t *)(v_rip + 0x6BA558) + 0x5E8) + 104, Arg2, Arg3, a4);
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(*(uint64_t *)(*(uint64_t *)(v_rip + 0x6BA558) + 0x5E8) + 80, Arg2, Arg3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = *(uint64_t *)(*(uint64_t *)(v_rip + 0x6BA558) + 0x5E8) + 80;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = *(uint64_t *)(*(uint64_t *)(v_rip + 0x6BA558) + 0x5E8) + 80;
        result = ExfAcquirePushLockSharedEx(Arg1, Arg2, Arg3, a4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    if (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x30) == 0) goto loc_0090C6DA;
    result = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x30) + 0x8)) & (-2);
    if (condition_is_equal) goto loc_0090C6DE;
    result = ExfAcquireRundownProtection(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x30) + 8, result + 2, Arg3, a4);
    if ((uint8_t)(result) != 0) goto loc_0090C6DE;
    result = 0;
loc_0090C6DA:
    local_r15 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x7C))) & (0xFFFFFFFEULL));
loc_0090C6DE:
    if ((((uint8_t)(local_r15)) & (1)) == 0) goto loc_0090C6F3;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x60)))) <= (*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x60))) goto loc_0090C83D;
    *(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x60) = (uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x60)));
loc_0090C6F3:
    if ((uint32_t)(local_r15) == 0) goto loc_0090C846;
    Arg1 = 0;
    result = 17;
    if (!(condition_is_equal)) {
        Arg1 = *(uint64_t *)(*(uint64_t *)(v_rip + 0x6BA558) + 0x5E8) + 80;
        result = ExfReleasePushLockShared(Arg1, result + 2, Arg3, a4);
    }
    result = KeAbPostRelease(*(uint64_t *)(*(uint64_t *)(v_rip + 0x6BA558) + 0x5E8) + 80, result + 2, Arg3, a4);
    result = (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x38)) ^ (*(uint64_t *)(*(uint64_t *)(v_rip + 0x6BA558) + 0x5E8) + 80);
    v_stack_m18 = result;
    if (0 == 0) goto loc_0090C8DF;
    local_r12 = (uint32_t)(((uint32_t)((uint32_t)(local_r15))) & (1));
    if (condition_is_equal) goto loc_0090C907;
loc_0090C74F:
    v_stack_m48 = *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x58);
    v_stack_m50 = *(uint64_t *)(0 + 0x40);
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x50)) != (v_rip + 470)) goto loc_0090C918;
    result = PopWnfSprActiveSessionChangeCallback(*(uint64_t *)(v_stack_m28 + 0x40), v_stack_m18, (uint32_t)((uint32_t)(local_r15)), (uint32_t)(*(uint32_t *)(0 + 0x60)));
loc_0090C781:
    result = ExpWnfValidateKernelCallbackEnvironment(*(uint64_t *)(v_stack_m28 + 0x40), v_stack_m18, (uint32_t)((uint32_t)(local_r15)), (uint32_t)(*(uint32_t *)(0 + 0x60)));
    if ((uint32_t)(local_r12) == 0) goto loc_0090C7AE;
    result = (uint32_t)((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x38)));
    if (((uint32_t)((uint32_t)((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x38))))) == 1) {
        a4 = 0;
        Arg2 = (uint32_t)((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x38))) + 7;
        Arg3 = 0;
        Arg1 = 0;
        result = ExpWnfNotifyNameSubscribers(Arg1, Arg2, Arg3, a4);
    }
    if (0 == 0) goto loc_0090C7D0;
    result = (*(uint64_t *)(0 + 0x8)) & (-2);
    if (condition_is_not_equal) goto loc_0090C8EF;
loc_0090C7D0:
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(*(uint64_t *)(*(uint64_t *)(v_rip + 0x6BA558) + 0x5E8) + 104, Arg2, Arg3, a4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = *(uint64_t *)(*(uint64_t *)(v_rip + 0x6BA558) + 0x5E8) + 104;
        Arg2 = result;
        Arg1 = *(uint64_t *)(*(uint64_t *)(v_rip + 0x6BA558) + 0x5E8) + 104;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, a4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    if ((*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x7C)) != 0) goto loc_0090C8D5;
    result = 0;
    *(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x78) = 0;
    result = (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x8)) & (-2);
    if (condition_is_equal) goto loc_0090C5A5;
    result = ExfReleaseRundownProtection(*(uint64_t *)(v_stack_m28 + 0x40) + 8, result - 2, Arg3, a4);
    goto loc_0090C5A5;
loc_0090C83D:
    local_r15 = (uint32_t)((v_stack_m28) & (0xFFFFFFFEULL));
    goto loc_0090C6F3;
loc_0090C846:
    local_r15 = 0;
    if (condition_is_not_equal) goto loc_0090C90B;
loc_0090C855:
    result = KeAbPostRelease(local_r12, result - 2, Arg3, a4);
    if (result != 0) {
        Arg1 = result + 8;
        result = ExReleaseRundownProtection(Arg1, result - 2, Arg3, a4);
    }
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(*(uint64_t *)(*(uint64_t *)(v_rip + 0x6BA558) + 0x5E8) + 104, Arg2, Arg3, a4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = *(uint64_t *)(*(uint64_t *)(v_rip + 0x6BA558) + 0x5E8) + 104;
        Arg2 = result;
        Arg1 = *(uint64_t *)(*(uint64_t *)(v_rip + 0x6BA558) + 0x5E8) + 104;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, a4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    if ((*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x7C)) != 0) goto loc_0090C650;
    *(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x78) = 0;
    result = ExReleaseRundownProtection(*(uint64_t *)(v_stack_m28 + 0x40) + 8, Arg2, Arg3, a4);
    goto loc_0090C5A5;
loc_0090C8BB:
    result = ExfTryToWakePushLock(*(uint64_t *)(*(uint64_t *)(v_rip + 0x6BA558) + 0x5E8) + 104, Arg2, Arg3, a4);
    goto loc_0090C66B;
loc_0090C8C8:
    result = ExfTryToWakePushLock(*(uint64_t *)(*(uint64_t *)(v_rip + 0x6BA558) + 0x5E8) + 104, Arg2, Arg3, a4);
    goto loc_0090C5FE;
loc_0090C8D5:
    goto loc_0090C650;
loc_0090C8DF:
    result = 0;
    local_r12 = (uint32_t)((v_stack_m20) & (1));
loc_0090C8E7:
    goto loc_0090C74F;
loc_0090C8EF:
    result = ExfReleaseRundownProtection(0, Arg2, Arg3, 0);
    goto loc_0090C7D0;
loc_0090C8F9:
    result = ExfAcquireRundownProtection(*(uint64_t *)(v_stack_m28 + 0x40) + 8, Arg2, Arg3, 0);
    goto loc_0090C5CD;
loc_0090C907:
    result = 0;
    goto loc_0090C8E7;
loc_0090C90B:
    result = ExfReleasePushLockShared(local_r12, Arg2, Arg3, 0);
    goto loc_0090C855;
loc_0090C918:
    result = guard_dispatch_icall(local_r12, Arg2, Arg3, 0);
    goto loc_0090C781;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0090C520&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
