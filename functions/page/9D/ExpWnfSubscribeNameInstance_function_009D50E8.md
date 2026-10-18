# ExpWnfSubscribeNameInstance

- RVA: `0x009D50E8`–`0x009D55B2` (길이 `1,226` bytes)
- VA: `0x00000001409D50E8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A1CDC`
- 디코드: `326`개 명령, `1,226/1,226` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **29**; 고유 호출 대상: **12**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x009D5153` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x009D5172` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)
- `0x009D51BA` → [ExpWnfUpdateSubscription](ExpWnfUpdateSubscription_function_009D55C0.md) (function, `0x009D55C0`)
- `0x009D51D1` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x009D51D9` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x009D520E` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x009D522A` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x009D528F` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x009D52A8` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x009D52C3` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x009D52DD` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x009D5339` → [ExpWnfUpdateSubscription](ExpWnfUpdateSubscription_function_009D55C0.md) (function, `0x009D55C0`)
- `0x009D5356` → [ExAcquireRundownProtection](../../text/21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x009D539D` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x009D53B7` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x009D53C4` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x009D5430` → [ExpWnfNotifyNameSubscribers](../90/ExpWnfNotifyNameSubscribers_function_0090C160.md) (function, `0x0090C160`)
- `0x009D5474` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x009D548D` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x009D549A` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x009D54AD` → [ExAcquireRundownProtection](../../text/21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x009D5540` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x009D5556` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x009D556D` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x009D5577` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x009D5581` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x009D558E` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x009D559B` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x009D55A8` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)

### Direct callers
- [ExpWnfSubscribeWnfStateChange](ExpWnfSubscribeWnfStateChange_function_009D4D0C.md) at `0x009D4ED0`

### Static image references
- `0x009D51EF` → RVA `0x00FC6AB0` (`ALMOSTRO`; read)
- `0x009D5268` → RVA `0x00FDA358` (`PAGEDATA`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **26**
  - `0x009D5153` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x009D5172` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (`PAGE` → `.text`)
  - `0x009D51D1` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x009D51D9` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x009D520E` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x009D522A` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x009D528F` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x009D52A8` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x009D52C3` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x009D52DD` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x009D5356` → [ExAcquireRundownProtection](../../text/21/ExAcquireRundownProtection_function_00216620.md) (`PAGE` → `.text`)
  - `0x009D539D` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x009D53B7` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x009D53C4` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x009D5474` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x009D548D` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x009D549A` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x009D54AD` → [ExAcquireRundownProtection](../../text/21/ExAcquireRundownProtection_function_00216620.md) (`PAGE` → `.text`)
  - `0x009D5540` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x009D5556` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x009D556D` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x009D5577` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x009D5581` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x009D558E` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x009D559B` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x009D55A8` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009D50E8  48 8B C4                        mov rax, rsp
009D50EB  48 89 58 08                     mov qword ptr [rax + 8], rbx
009D50EF  4C 89 48 20                     mov qword ptr [rax + 0x20], r9
009D50F3  4C 89 40 18                     mov qword ptr [rax + 0x18], r8
009D50F7  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
009D50FB  55                              push rbp
009D50FC  56                              push rsi
009D50FD  57                              push rdi
009D50FE  41 54                           push r12
009D5100  41 55                           push r13
009D5102  41 56                           push r14
009D5104  41 57                           push r15
009D5106  48 8B EC                        mov rbp, rsp
009D5109  48 83 EC 70                     sub rsp, 0x70
009D510D  48 8B B2 E8 05 00 00            mov rsi, qword ptr [rdx + 0x5e8]
009D5114  33 FF                           xor edi, edi
009D5116  48 8B 85 90 00 00 00            mov rax, qword ptr [rbp + 0x90]
009D511D  48 83 CB FF                     or rbx, 0xffffffffffffffff
009D5121  80 7D 70 01                     cmp byte ptr [rbp + 0x70], 1
009D5125  4D 8B E1                        mov r12, r9
009D5128  4D 8B F0                        mov r14, r8
009D512B  48 89 7D E8                     mov qword ptr [rbp - 0x18], rdi
009D512F  4C 8B FA                        mov r15, rdx
009D5132  48 89 75 F0                     mov qword ptr [rbp - 0x10], rsi
009D5136  89 38                           mov dword ptr [rax], edi
009D5138  4C 8B E9                        mov r13, rcx
009D513B  89 7D E0                        mov dword ptr [rbp - 0x20], edi
009D513E  89 7D E4                        mov dword ptr [rbp - 0x1c], edi
009D5141  0F 85 A8 00 00 00               jne 0x1409d51ef
009D5147  48 83 C6 50                     add rsi, 0x50
009D514B  45 33 C0                        xor r8d, r8d
009D514E  48 8B CE                        mov rcx, rsi
009D5151  33 D2                           xor edx, edx
009D5153  E8 D8 B0 83 FF                  call 0x140210230
009D5158  4C 8B F0                        mov r14, rax
009D515B  8D 4F 11                        lea ecx, [rdi + 0x11]
009D515E  33 C0                           xor eax, eax
009D5160  F0 48 0F B1 0E                  lock cmpxchg qword ptr [rsi], rcx
009D5165  74 10                           je 0x1409d5177
009D5167  4C 8B CE                        mov r9, rsi
009D516A  4D 8B C6                        mov r8, r14
009D516D  33 D2                           xor edx, edx
009D516F  48 8B CE                        mov rcx, rsi
009D5172  E8 D5 B2 83 FF                  call 0x14021044c
009D5177  4D 85 F6                        test r14, r14
009D517A  74 05                           je 0x1409d5181
009D517C  41 C6 46 0A 01                  mov byte ptr [r14 + 0xa], 1
009D5181  48 8B 45 78                     mov rax, qword ptr [rbp + 0x78]
009D5185  48 8D 4D E0                     lea rcx, [rbp - 0x20]
009D5189  4C 8B 45 50                     mov r8, qword ptr [rbp + 0x50]
009D518D  4D 8B CC                        mov r9, r12
009D5190  48 8B 55 F0                     mov rdx, qword ptr [rbp - 0x10]
009D5194  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
009D5199  48 8D 45 E4                     lea rax, [rbp - 0x1c]
009D519D  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
009D51A2  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
009D51A7  48 8D 4D E8                     lea rcx, [rbp - 0x18]
009D51AB  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
009D51B0  8B 4D 68                        mov ecx, dword ptr [rbp + 0x68]
009D51B3  89 4C 24 20                     mov dword ptr [rsp + 0x20], ecx
009D51B7  49 8B CD                        mov rcx, r13
009D51BA  E8 01 04 00 00                  call 0x1409d55c0
009D51BF  44 8B F0                        mov r14d, eax
009D51C2  B8 11 00 00 00                  mov eax, 0x11
009D51C7  F0 48 0F B1 3E                  lock cmpxchg qword ptr [rsi], rdi
009D51CC  74 08                           je 0x1409d51d6
009D51CE  48 8B CE                        mov rcx, rsi
009D51D1  E8 6A E2 88 FF                  call 0x140263440
009D51D6  48 8B CE                        mov rcx, rsi
009D51D9  E8 22 C4 90 FF                  call 0x1402e1600
009D51DE  45 85 F6                        test r14d, r14d
009D51E1  0F 89 E2 01 00 00               jns 0x1409d53c9
009D51E7  48 8B 75 F0                     mov rsi, qword ptr [rbp - 0x10]
009D51EB  4C 8B 75 50                     mov r14, qword ptr [rbp + 0x50]
009D51EF  4C 39 3D BA 18 5F 00            cmp qword ptr [rip + 0x5f18ba], r15
009D51F6  48 8B CF                        mov rcx, rdi
009D51F9  BA 88 00 00 00                  mov edx, 0x88
009D51FE  41 B8 57 6E 66 20               mov r8d, 0x20666e57
009D5204  0F 95 C1                        setne cl
009D5207  48 81 C1 00 01 00 00            add rcx, 0x100
009D520E  E8 DD CE 1A 00                  call 0x140b820f0
009D5213  4C 8B F8                        mov r15, rax
009D5216  48 85 C0                        test rax, rax
009D5219  0F 84 F2 01 00 00               je 0x1409d5411
009D521F  33 D2                           xor edx, edx
009D5221  41 B8 88 00 00 00               mov r8d, 0x88
009D5227  48 8B C8                        mov rcx, rax
009D522A  E8 11 1A CF FF                  call 0x1406c6c40
009D522F  8B 45 60                        mov eax, dword ptr [rbp + 0x60]
009D5232  41 C7 07 05 09 88 00            mov dword ptr [r15], 0x880905
009D5239  41 89 47 60                     mov dword ptr [r15 + 0x60], eax
009D523D  8B 45 68                        mov eax, dword ptr [rbp + 0x68]
009D5240  41 89 47 64                     mov dword ptr [r15 + 0x64], eax
009D5244  4D 89 77 50                     mov qword ptr [r15 + 0x50], r14
009D5248  4D 89 67 58                     mov qword ptr [r15 + 0x58], r12
009D524C  49 89 7F 08                     mov qword ptr [r15 + 8], rdi
009D5250  49 8B 45 28                     mov rax, qword ptr [r13 + 0x28]
009D5254  49 89 47 38                     mov qword ptr [r15 + 0x38], rax
009D5258  40 38 7D 70                     cmp byte ptr [rbp + 0x70], dil
009D525C  0F 84 DE 01 00 00               je 0x1409d5440
009D5262  41 BC 01 00 00 00               mov r12d, 1
009D5268  F0 4C 0F C1 25 E7 50 60 00      lock xadd qword ptr [rip + 0x6050e7], r12
009D5271  49 83 C4 01                     add r12, 1
009D5275  74 EB                           je 0x1409d5262
009D5277  48 8B 45 78                     mov rax, qword ptr [rbp + 0x78]
009D527B  48 85 C0                        test rax, rax
009D527E  74 03                           je 0x1409d5283
009D5280  4C 89 20                        mov qword ptr [rax], r12
009D5283  48 83 C6 50                     add rsi, 0x50
009D5287  45 33 C0                        xor r8d, r8d
009D528A  48 8B CE                        mov rcx, rsi
009D528D  33 D2                           xor edx, edx
009D528F  E8 9C AF 83 FF                  call 0x140210230
009D5294  F0 48 0F BA 2E 00               lock bts qword ptr [rsi], 0
009D529A  4C 8B F0                        mov r14, rax
009D529D  73 0E                           jae 0x1409d52ad
009D529F  4C 8B C6                        mov r8, rsi
009D52A2  48 8B D0                        mov rdx, rax
009D52A5  48 8B CE                        mov rcx, rsi
009D52A8  E8 E3 A9 83 FF                  call 0x14020fc90
009D52AD  4D 85 F6                        test r14, r14
009D52B0  74 05                           je 0x1409d52b7
009D52B2  41 C6 46 0A 01                  mov byte ptr [r14 + 0xa], 1
009D52B7  4D 8D 75 70                     lea r14, [r13 + 0x70]
009D52BB  45 33 C0                        xor r8d, r8d
009D52BE  49 8B CE                        mov rcx, r14
009D52C1  33 D2                           xor edx, edx
009D52C3  E8 68 AF 83 FF                  call 0x140210230
009D52C8  F0 49 0F BA 2E 00               lock bts qword ptr [r14], 0
009D52CE  48 89 45 F8                     mov qword ptr [rbp - 8], rax
009D52D2  73 12                           jae 0x1409d52e6
009D52D4  4D 8B C6                        mov r8, r14
009D52D7  48 8B D0                        mov rdx, rax
009D52DA  49 8B CE                        mov rcx, r14
009D52DD  E8 AE A9 83 FF                  call 0x14020fc90
009D52E2  48 8B 45 F8                     mov rax, qword ptr [rbp - 8]
009D52E6  48 85 C0                        test rax, rax
009D52E9  74 04                           je 0x1409d52ef
009D52EB  C6 40 0A 01                     mov byte ptr [rax + 0xa], 1
009D52EF  49 39 7D 30                     cmp qword ptr [r13 + 0x30], rdi
009D52F3  0F 84 62 01 00 00               je 0x1409d545b
009D52F9  80 7D 70 01                     cmp byte ptr [rbp + 0x70], 1
009D52FD  75 43                           jne 0x1409d5342
009D52FF  48 8B 45 78                     mov rax, qword ptr [rbp + 0x78]
009D5303  49 8B CD                        mov rcx, r13
009D5306  4C 8B 4D 58                     mov r9, qword ptr [rbp + 0x58]
009D530A  4C 8B 45 50                     mov r8, qword ptr [rbp + 0x50]
009D530E  48 8B 55 F0                     mov rdx, qword ptr [rbp - 0x10]
009D5312  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
009D5317  48 8D 45 E4                     lea rax, [rbp - 0x1c]
009D531B  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
009D5320  48 8D 45 E0                     lea rax, [rbp - 0x20]
009D5324  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
009D5329  48 8D 45 E8                     lea rax, [rbp - 0x18]
009D532D  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009D5332  8B 45 68                        mov eax, dword ptr [rbp + 0x68]
009D5335  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
009D5339  E8 82 02 00 00                  call 0x1409d55c0
009D533E  85 C0                           test eax, eax
009D5340  79 46                           jns 0x1409d5388
009D5342  48 8B 45 48                     mov rax, qword ptr [rbp + 0x48]
009D5346  49 8D 4F 08                     lea rcx, [r15 + 8]
009D534A  49 89 47 28                     mov qword ptr [r15 + 0x28], rax
009D534E  4D 89 6F 30                     mov qword ptr [r15 + 0x30], r13
009D5352  4D 89 67 10                     mov qword ptr [r15 + 0x10], r12
009D5356  E8 C5 12 84 FF                  call 0x140216620
009D535B  48 39 BD 80 00 00 00            cmp qword ptr [rbp + 0x80], rdi
009D5362  0F 85 41 01 00 00               jne 0x1409d54a9
009D5368  48 8B 45 F0                     mov rax, qword ptr [rbp - 0x10]
009D536C  49 8D 4F 18                     lea rcx, [r15 + 0x18]
009D5370  48 83 C0 58                     add rax, 0x58
009D5374  48 8B 50 08                     mov rdx, qword ptr [rax + 8]
009D5378  48 39 02                        cmp qword ptr [rdx], rax
009D537B  0F 84 50 01 00 00               je 0x1409d54d1
009D5381  B9 03 00 00 00                  mov ecx, 3
009D5386  CD 29                           int 0x29
009D5388  48 8B C3                        mov rax, rbx
009D538B  F0 49 0F C1 06                  lock xadd qword ptr [r14], rax
009D5390  24 06                           and al, 6
009D5392  3C 02                           cmp al, 2
009D5394  0F 84 E4 01 00 00               je 0x1409d557e
009D539A  49 8B CE                        mov rcx, r14
009D539D  E8 5E C2 90 FF                  call 0x1402e1600
009D53A2  48 8B C3                        mov rax, rbx
009D53A5  F0 48 0F C1 06                  lock xadd qword ptr [rsi], rax
009D53AA  24 06                           and al, 6
009D53AC  3C 02                           cmp al, 2
009D53AE  0F 84 D7 01 00 00               je 0x1409d558b
009D53B4  48 8B CE                        mov rcx, rsi
009D53B7  E8 44 C2 90 FF                  call 0x1402e1600
009D53BC  BA 57 6E 66 20                  mov edx, 0x20666e57
009D53C1  49 8B CF                        mov rcx, r15
009D53C4  E8 A7 D4 1A 00                  call 0x140b82870
009D53C9  48 8B 8D 88 00 00 00            mov rcx, qword ptr [rbp + 0x88]
009D53D0  41 BC 01 00 00 00               mov r12d, 1
009D53D6  48 8B 45 E8                     mov rax, qword ptr [rbp - 0x18]
009D53DA  48 89 01                        mov qword ptr [rcx], rax
009D53DD  8B F7                           mov esi, edi
009D53DF  39 7D E4                        cmp dword ptr [rbp - 0x1c], edi
009D53E2  0F 8C CF 00 00 00               jl 0x1409d54b7
009D53E8  39 7D E0                        cmp dword ptr [rbp - 0x20], edi
009D53EB  7F 2B                           jg 0x1409d5418
009D53ED  7D 03                           jge 0x1409d53f2
009D53EF  83 CE 04                        or esi, 4
009D53F2  85 F6                           test esi, esi
009D53F4  75 27                           jne 0x1409d541d
009D53F6  33 C0                           xor eax, eax
009D53F8  48 8B 9C 24 B0 00 00 00         mov rbx, qword ptr [rsp + 0xb0]
009D5400  48 83 C4 70                     add rsp, 0x70
009D5404  41 5F                           pop r15
009D5406  41 5E                           pop r14
009D5408  41 5D                           pop r13
009D540A  41 5C                           pop r12
009D540C  5F                              pop rdi
009D540D  5E                              pop rsi
009D540E  5D                              pop rbp
009D540F  C3                              ret
009D5410  CC                              int3
009D5411  B8 9A 00 00 C0                  mov eax, 0xc000009a
009D5416  EB E0                           jmp 0x1409d53f8
009D5418  83 CE 02                        or esi, 2
009D541B  EB D5                           jmp 0x1409d53f2
009D541D  40 38 7D 70                     cmp byte ptr [rbp + 0x70], dil
009D5421  45 8B C4                        mov r8d, r12d
009D5424  8B D6                           mov edx, esi
009D5426  49 8B CD                        mov rcx, r13
009D5429  40 0F 95 C7                     setne dil
009D542D  44 8B CF                        mov r9d, edi
009D5430  E8 2B 6D F3 FF                  call 0x14090c160
009D5435  48 8B 85 90 00 00 00            mov rax, qword ptr [rbp + 0x90]
009D543C  89 30                           mov dword ptr [rax], esi
009D543E  EB B6                           jmp 0x1409d53f6
009D5440  48 8B 85 80 00 00 00            mov rax, qword ptr [rbp + 0x80]
009D5447  4D 8B E7                        mov r12, r15
009D544A  48 85 C0                        test rax, rax
009D544D  0F 84 30 FE FF FF               je 0x1409d5283
009D5453  4C 89 38                        mov qword ptr [rax], r15
009D5456  E9 28 FE FF FF                  jmp 0x1409d5283
009D545B  48 83 CB FF                     or rbx, 0xffffffffffffffff
009D545F  48 8B C3                        mov rax, rbx
009D5462  F0 49 0F C1 06                  lock xadd qword ptr [r14], rax
009D5467  24 06                           and al, 6
009D5469  3C 02                           cmp al, 2
009D546B  0F 84 27 01 00 00               je 0x1409d5598
009D5471  49 8B CE                        mov rcx, r14
009D5474  E8 87 C1 90 FF                  call 0x1402e1600
009D5479  F0 48 0F C1 1E                  lock xadd qword ptr [rsi], rbx
009D547E  80 E3 06                        and bl, 6
009D5481  80 FB 02                        cmp bl, 2
009D5484  0F 84 1B 01 00 00               je 0x1409d55a5
009D548A  48 8B CE                        mov rcx, rsi
009D548D  E8 6E C1 90 FF                  call 0x1402e1600
009D5492  BA 57 6E 66 20                  mov edx, 0x20666e57
009D5497  49 8B CF                        mov rcx, r15
009D549A  E8 D1 D3 1A 00                  call 0x140b82870
009D549F  B8 34 00 00 C0                  mov eax, 0xc0000034
009D54A4  E9 4F FF FF FF                  jmp 0x1409d53f8
009D54A9  49 8D 4F 08                     lea rcx, [r15 + 8]
009D54AD  E8 6E 11 84 FF                  call 0x140216620
009D54B2  E9 B1 FE FF FF                  jmp 0x1409d5368
009D54B7  8B C3                           mov eax, ebx
009D54B9  F0 41 0F C1 85 A4 00 00 00      lock xadd dword ptr [r13 + 0xa4], eax
009D54C2  03 C3                           add eax, ebx
009D54C4  B8 08 00 00 00                  mov eax, 8
009D54C9  0F 44 F0                        cmove esi, eax
009D54CC  E9 17 FF FF FF                  jmp 0x1409d53e8
009D54D1  48 89 01                        mov qword ptr [rcx], rax
009D54D4  48 89 51 08                     mov qword ptr [rcx + 8], rdx
009D54D8  48 89 0A                        mov qword ptr [rdx], rcx
009D54DB  48 89 48 08                     mov qword ptr [rax + 8], rcx
009D54DF  49 8D 4D 78                     lea rcx, [r13 + 0x78]
009D54E3  48 8B 51 08                     mov rdx, qword ptr [rcx + 8]
009D54E7  49 8D 47 40                     lea rax, [r15 + 0x40]
009D54EB  48 39 0A                        cmp qword ptr [rdx], rcx
009D54EE  0F 85 8D FE FF FF               jne 0x1409d5381
009D54F4  48 89 08                        mov qword ptr [rax], rcx
009D54F7  41 BC 01 00 00 00               mov r12d, 1
009D54FD  48 89 50 08                     mov qword ptr [rax + 8], rdx
009D5501  48 89 02                        mov qword ptr [rdx], rax
009D5504  48 89 41 08                     mov qword ptr [rcx + 8], rax
009D5508  41 8B 47 64                     mov eax, dword ptr [r15 + 0x64]
009D550C  41 23 C4                        and eax, r12d
009D550F  84 C0                           test al, al
009D5511  74 1C                           je 0x1409d552f
009D5513  41 8B CC                        mov ecx, r12d
009D5516  F0 41 0F C1 8D A0 00 00 00      lock xadd dword ptr [r13 + 0xa0], ecx
009D551F  8B 45 E0                        mov eax, dword ptr [rbp - 0x20]
009D5522  41 03 CC                        add ecx, r12d
009D5525  41 3B CC                        cmp ecx, r12d
009D5528  41 0F 44 C4                     cmove eax, r12d
009D552C  89 45 E0                        mov dword ptr [rbp - 0x20], eax
009D552F  48 8B C3                        mov rax, rbx
009D5532  F0 49 0F C1 06                  lock xadd qword ptr [r14], rax
009D5537  24 06                           and al, 6
009D5539  3C 02                           cmp al, 2
009D553B  74 2D                           je 0x1409d556a
009D553D  49 8B CE                        mov rcx, r14
009D5540  E8 BB C0 90 FF                  call 0x1402e1600
009D5545  48 8B C3                        mov rax, rbx
009D5548  F0 48 0F C1 06                  lock xadd qword ptr [rsi], rax
009D554D  24 06                           and al, 6
009D554F  3C 02                           cmp al, 2
009D5551  74 21                           je 0x1409d5574
009D5553  48 8B CE                        mov rcx, rsi
009D5556  E8 A5 C0 90 FF                  call 0x1402e1600
009D555B  48 8B 85 88 00 00 00            mov rax, qword ptr [rbp + 0x88]
009D5562  4C 89 38                        mov qword ptr [rax], r15
009D5565  E9 73 FE FF FF                  jmp 0x1409d53dd
009D556A  49 8B CE                        mov rcx, r14
009D556D  E8 5E 08 89 FF                  call 0x140265dd0
009D5572  EB C9                           jmp 0x1409d553d
009D5574  48 8B CE                        mov rcx, rsi
009D5577  E8 54 08 89 FF                  call 0x140265dd0
009D557C  EB D5                           jmp 0x1409d5553
009D557E  49 8B CE                        mov rcx, r14
009D5581  E8 4A 08 89 FF                  call 0x140265dd0
009D5586  E9 0F FE FF FF                  jmp 0x1409d539a
009D558B  48 8B CE                        mov rcx, rsi
009D558E  E8 3D 08 89 FF                  call 0x140265dd0
009D5593  E9 1C FE FF FF                  jmp 0x1409d53b4
009D5598  49 8B CE                        mov rcx, r14
009D559B  E8 30 08 89 FF                  call 0x140265dd0
009D55A0  E9 CC FE FF FF                  jmp 0x1409d5471
009D55A5  48 8B CE                        mov rcx, rsi
009D55A8  E8 23 08 89 FF                  call 0x140265dd0
009D55AD  E9 D8 FE FF FF                  jmp 0x1409d548a
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExpWnfSubscribeNameInstance(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned int a5, unsigned int a6, unsigned __int8 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned int v_stack_m54;
    unsigned int v_stack_m58;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned int v_stack_m88;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 32) = a4;
    *(unsigned __int64 *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    v_rsp = (v_rsp) - (112);
    v_rdi = 0;
    v_rbx = (v_rbx) | (-1);
    v_stack_m50 = 0;
    v_stack_m48 = *(unsigned __int64 *)(a2 + 1512);
    *(unsigned int *)(a11) = 0;
    v_stack_m58 = 0;
    v_stack_m54 = 0;
    if (a7 != 1) goto loc_009D51EF;
    v_rsi = (*(unsigned __int64 *)(a2 + 1512)) + (80);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_rsi, a2, a3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = v_rsi;
        a3 = 0;
        a2 = 0;
        a1 = v_rsi;
        result = ExfAcquirePushLockSharedEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    v_stack_m68 = a8;
    v_stack_m70 = v_stack_m54;
    v_stack_m78 = v_stack_m58;
    v_stack_m80 = v_stack_m50;
    v_stack_m88 = (unsigned int)((unsigned int)(a6));
    result = ExpWnfUpdateSubscription(a1, v_stack_m48, v_stack_p18, a4);
    result = 17;
    if (result != 0) {
        a1 = v_rsi;
        result = ExfReleasePushLockShared(a1, v_stack_m48, v_stack_p18, a4);
    }
    result = KeAbPostRelease(v_rsi, v_stack_m48, v_stack_p18, a4);
    if (!sign_flag) goto loc_009D53C9;
loc_009D51EF:
    a1 = ((*(unsigned __int64 *)(v_rip + 6232250)) != 0) ? 1 : 0;
    a1 = (a1) + (256);
    result = ExAllocatePool2(a1, 136, (unsigned int)(0x20666E57ULL), a4);
    if (result == 0) goto loc_009D5411;
    a2 = 0;
    result = memset(result, a2, 136, a4);
    *(unsigned int *)(result) = 0x880905ULL;
    *(unsigned int *)(result + 96) = (unsigned int)((unsigned int)(a5));
    *(unsigned int *)(result + 100) = (unsigned int)((unsigned int)(a6));
    *(unsigned __int64 *)(result + 80) = v_stack_p18;
    *(unsigned __int64 *)(result + 88) = a4;
    *(unsigned __int64 *)(result + 8) = 0;
    *(unsigned __int64 *)(result + 56) = *(unsigned __int64 *)(a1 + 40);
    if (a7 == 0) goto loc_009D5440;
loc_009D5262:
    v_r12 = (1) + (1);
    if (condition_is_equal) goto loc_009D5262;
    if (a8 != 0) {
        *(unsigned __int64 *)(a8) = v_r12;
    }
    v_rsi = (v_stack_m48) + (80);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_rsi, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = v_rsi;
        a2 = result;
        a1 = v_rsi;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(a1 + 112, a2, a3, a4);
    v_stack_m40 = result;
    if (!(condition_is_above_or_equal)) {
        a3 = a1 + 112;
        a2 = result;
        a1 = a1 + 112;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
        result = v_stack_m40;
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    if ((*(unsigned __int64 *)(a1 + 48)) == 0) goto loc_009D545B;
    if (a7 != 1) goto loc_009D5342;
    v_stack_m68 = a8;
    v_stack_m70 = v_stack_m54;
    v_stack_m78 = v_stack_m58;
    v_stack_m80 = v_stack_m50;
    v_stack_m88 = (unsigned int)((unsigned int)(a6));
    result = ExpWnfUpdateSubscription(a1, v_stack_m48, v_stack_p18, v_stack_p20);
    if (!sign_flag) goto loc_009D5388;
loc_009D5342:
    *(unsigned __int64 *)(result + 40) = v_stack_p10;
    *(unsigned __int64 *)(result + 48) = a1;
    *(unsigned __int64 *)(result + 16) = v_r12;
    result = ExAcquireRundownProtection(result + 8, v_stack_m48, v_stack_p18, v_stack_p20);
    if (a9 != 0) goto loc_009D54A9;
loc_009D5368:
    result = (v_stack_m48) + (88);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8))) == result) goto loc_009D54D1;
loc_009D5381:
loc_009D5388:
    result = (unsigned __int8)((v_rbx) & (6));
    if (((unsigned __int8)(result)) == 2) goto loc_009D557E;
loc_009D539A:
    result = KeAbPostRelease(a1 + 112, *(unsigned __int64 *)(result + 8), v_stack_p18, v_stack_p20);
    result = (unsigned __int8)((v_rbx) & (6));
    if (((unsigned __int8)(result)) == 2) goto loc_009D558B;
loc_009D53B4:
    result = KeAbPostRelease(v_rsi, *(unsigned __int64 *)(result + 8), v_stack_p18, v_stack_p20);
    result = ExFreePoolWithTag(result, (unsigned int)(0x20666E57ULL), v_stack_p18, v_stack_p20);
loc_009D53C9:
    *(unsigned __int64 *)(a10) = v_stack_m50;
loc_009D53DD:
    if (v_stack_m54 < 0) goto loc_009D54B7;
loc_009D53E8:
    if (v_stack_m58 > 0) goto loc_009D5418;
    v_rsi = 0;
    if (v_stack_m58 < 0) {
        v_rsi = (unsigned int)((0) | (4));
    }
    if ((unsigned int)(v_rsi) != 0) goto loc_009D541D;
loc_009D53F6:
    result = 0;
loc_009D53F8:
    v_rsp = (v_rsp) + (112);
    return result;
loc_009D5411:
    goto loc_009D53F8;
loc_009D5418:
    v_rsi = (unsigned int)((v_rsi) | (2));
    goto loc_009D53F2;
loc_009D541D:
    v_rdi = (a7 != 0) ? 1 : 0;
    result = ExpWnfNotifyNameSubscribers(a1, (unsigned int)((unsigned int)(v_rsi)), 1, (unsigned int)((unsigned int)(v_rdi)));
    *(unsigned int *)(a11) = (unsigned int)(v_rsi);
    goto loc_009D53F6;
loc_009D5440:
    if (a9 == 0) goto loc_009D5283;
    *(unsigned __int64 *)(a9) = result;
    goto loc_009D5283;
loc_009D545B:
    v_rbx = (v_stack_p8) | (-1);
    result = (unsigned __int8)((v_rbx) & (6));
    if (((unsigned __int8)(result)) == 2) goto loc_009D5598;
loc_009D5471:
    result = KeAbPostRelease(a1 + 112, (unsigned int)((unsigned int)(v_rsi)), 1, (unsigned int)((unsigned int)(v_rdi)));
    v_rbx = (unsigned __int8)((v_rbx) & (6));
    if (((unsigned __int8)(v_rbx)) == 2) goto loc_009D55A5;
loc_009D548A:
    result = KeAbPostRelease(v_rsi, (unsigned int)((unsigned int)(v_rsi)), 1, (unsigned int)((unsigned int)(v_rdi)));
    result = ExFreePoolWithTag(result, (unsigned int)(0x20666E57ULL), 1, (unsigned int)((unsigned int)(v_rdi)));
    goto loc_009D53F8;
loc_009D54A9:
    result = ExAcquireRundownProtection(result + 8, (unsigned int)(0x20666E57ULL), 1, (unsigned int)((unsigned int)(v_rdi)));
    goto loc_009D5368;
loc_009D54B7:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) + ((unsigned int)(v_rbx)));
    if (condition_is_equal) { v_rsi = 8; }
    goto loc_009D53E8;
loc_009D54D1:
    *(unsigned __int64 *)(result + 8) = 8;
    *(unsigned __int64 *)(result + 8 + 8) = (unsigned int)(0x20666E57ULL);
    *(unsigned __int64 *)((unsigned int)(0x20666E57ULL)) = result + 8;
    *(unsigned __int64 *)(8 + 8) = result + 8;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 120 + 8))) != (a1 + 120)) goto loc_009D5381;
    *(unsigned __int64 *)(result + 64) = a1 + 120;
    *(unsigned __int64 *)(result + 64 + 8) = *(unsigned __int64 *)(a1 + 120 + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 120 + 8)) = result + 64;
    *(unsigned __int64 *)(a1 + 120 + 8) = result + 64;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 100))) & (1));
    if ((unsigned __int8)(result) != 0) {
        a1 = 1;
        result = v_stack_m58;
        a1 = (unsigned int)((a1) + (1));
        if (((unsigned int)(a1)) == 1) { result = 1; }
        v_stack_m58 = (unsigned int)(result);
    }
    result = (unsigned __int8)((v_rbx) & (6));
    if (((unsigned __int8)(result)) == 2) goto loc_009D556A;
loc_009D553D:
    result = KeAbPostRelease(a1 + 112, *(unsigned __int64 *)(a1 + 120 + 8), 1, (unsigned int)((unsigned int)(v_rdi)));
    result = (unsigned __int8)((v_rbx) & (6));
    if (((unsigned __int8)(result)) == 2) goto loc_009D5574;
loc_009D5553:
    result = KeAbPostRelease(v_rsi, *(unsigned __int64 *)(a1 + 120 + 8), 1, (unsigned int)((unsigned int)(v_rdi)));
    *(unsigned __int64 *)(a10) = result;
    goto loc_009D53DD;
loc_009D556A:
    result = ExfTryToWakePushLock(a1 + 112, *(unsigned __int64 *)(a1 + 120 + 8), 1, (unsigned int)((unsigned int)(v_rdi)));
    goto loc_009D553D;
loc_009D5574:
    result = ExfTryToWakePushLock(v_rsi, *(unsigned __int64 *)(a1 + 120 + 8), 1, (unsigned int)((unsigned int)(v_rdi)));
    goto loc_009D5553;
loc_009D557E:
    result = ExfTryToWakePushLock(a1 + 112, *(unsigned __int64 *)(a1 + 120 + 8), 1, (unsigned int)((unsigned int)(v_rdi)));
    goto loc_009D539A;
loc_009D558B:
    result = ExfTryToWakePushLock(v_rsi, *(unsigned __int64 *)(a1 + 120 + 8), 1, (unsigned int)((unsigned int)(v_rdi)));
    goto loc_009D53B4;
loc_009D5598:
    result = ExfTryToWakePushLock(a1 + 112, *(unsigned __int64 *)(a1 + 120 + 8), 1, (unsigned int)((unsigned int)(v_rdi)));
    goto loc_009D5471;
loc_009D55A5:
    result = ExfTryToWakePushLock(v_rsi, *(unsigned __int64 *)(a1 + 120 + 8), 1, (unsigned int)((unsigned int)(v_rdi)));
    goto loc_009D548A;
}
```

## 5. (Beta) C Style

```c
int64_t ExpWnfSubscribeNameInstance(void *Arg1, void *Arg2, int64_t Arg3, int64_t Arg4, uint32_t Arg5, uint32_t Arg6, uint8_t Arg7, int64_t Arg8, int64_t Arg9, void *Arg10, void *Arg11)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg10 = (uint8_t *)Arg10;
    uint8_t *arg11 = (uint8_t *)Arg11;

    int64_t result;
    int64_t local_r12;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint32_t v_stack_m54;
    uint32_t v_stack_m58;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint32_t v_stack_m88;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x20) = Arg4;
    *(uint64_t *)(local_rsp + 0x18) = Arg3;
    *(void **)(local_rsp + 0x10) = Arg2;
    local_rsp = (local_rsp) - (112);
    local_rdi = 0;
    local_rbx = (local_rbx) | (-1);
    v_stack_m50 = 0;
    v_stack_m48 = *(uint64_t *)(arg2 + 0x5E8);
    *(uint32_t *)(arg11) = 0;
    v_stack_m58 = 0;
    v_stack_m54 = 0;
    if (Arg7 != 1) goto loc_009D51EF;
    local_rsi = (*(uint64_t *)(arg2 + 0x5E8)) + (80);
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(local_rsi, Arg2, Arg3, Arg4);
    result = 0;
    if (!(condition_is_equal)) {
        Arg4 = local_rsi;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = local_rsi;
        result = ExfAcquirePushLockSharedEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    v_stack_m68 = Arg8;
    v_stack_m70 = v_stack_m54;
    v_stack_m78 = v_stack_m58;
    v_stack_m80 = v_stack_m50;
    v_stack_m88 = (uint32_t)((uint32_t)(Arg6));
    result = ExpWnfUpdateSubscription(Arg1, v_stack_m48, v_stack_p18, Arg4);
    result = 17;
    if (result != 0) {
        Arg1 = local_rsi;
        result = ExfReleasePushLockShared(Arg1, v_stack_m48, v_stack_p18, Arg4);
    }
    result = KeAbPostRelease(local_rsi, v_stack_m48, v_stack_p18, Arg4);
    if (!sign_flag) goto loc_009D53C9;
loc_009D51EF:
    Arg1 = ((*(uint64_t *)(v_rip + 0x5F18BA)) != 0) ? 1 : 0;
    Arg1 = (Arg1) + (256);
    result = ExAllocatePool2(Arg1, 136, (uint32_t)(0x20666E57ULL), Arg4);
    if (result == 0) goto loc_009D5411;
    Arg2 = 0;
    result = memset(result, Arg2, 136, Arg4);
    *(uint32_t *)(result) = 0x880905ULL;
    *(uint32_t *)(result + 0x60) = (uint32_t)((uint32_t)(Arg5));
    *(uint32_t *)(result + 0x64) = (uint32_t)((uint32_t)(Arg6));
    *(uint64_t *)(result + 0x50) = v_stack_p18;
    *(uint64_t *)(result + 0x58) = Arg4;
    *(uint64_t *)(result + 0x8) = 0;
    *(uint64_t *)(result + 0x38) = *(uint64_t *)(arg1 + 0x28);
    if (Arg7 == 0) goto loc_009D5440;
loc_009D5262:
    local_r12 = (1) + (1);
    if (condition_is_equal) goto loc_009D5262;
    if (Arg8 != 0) {
        *(uint64_t *)(Arg8) = local_r12;
    }
    local_rsi = (v_stack_m48) + (80);
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(local_rsi, Arg2, Arg3, Arg4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = local_rsi;
        Arg2 = result;
        Arg1 = local_rsi;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(Arg1 + 112, Arg2, Arg3, Arg4);
    v_stack_m40 = result;
    if (!(condition_is_above_or_equal)) {
        Arg3 = Arg1 + 112;
        Arg2 = result;
        Arg1 = Arg1 + 112;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, Arg4);
        result = v_stack_m40;
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    if ((*(uint64_t *)(arg1 + 0x30)) == 0) goto loc_009D545B;
    if (Arg7 != 1) goto loc_009D5342;
    v_stack_m68 = Arg8;
    v_stack_m70 = v_stack_m54;
    v_stack_m78 = v_stack_m58;
    v_stack_m80 = v_stack_m50;
    v_stack_m88 = (uint32_t)((uint32_t)(Arg6));
    result = ExpWnfUpdateSubscription(Arg1, v_stack_m48, v_stack_p18, v_stack_p20);
    if (!sign_flag) goto loc_009D5388;
loc_009D5342:
    *(uint64_t *)(result + 0x28) = v_stack_p10;
    *(void **)(result + 0x30) = Arg1;
    *(uint64_t *)(result + 0x10) = local_r12;
    result = ExAcquireRundownProtection(result + 8, v_stack_m48, v_stack_p18, v_stack_p20);
    if (Arg9 != 0) goto loc_009D54A9;
loc_009D5368:
    result = (v_stack_m48) + (88);
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x8))) == result) goto loc_009D54D1;
loc_009D5381:
loc_009D5388:
    result = (uint8_t)((local_rbx) & (6));
    if (((uint8_t)(result)) == 2) goto loc_009D557E;
loc_009D539A:
    result = KeAbPostRelease(Arg1 + 112, *(uint64_t *)(result + 0x8), v_stack_p18, v_stack_p20);
    result = (uint8_t)((local_rbx) & (6));
    if (((uint8_t)(result)) == 2) goto loc_009D558B;
loc_009D53B4:
    result = KeAbPostRelease(local_rsi, *(uint64_t *)(result + 0x8), v_stack_p18, v_stack_p20);
    result = ExFreePoolWithTag(result, (uint32_t)(0x20666E57ULL), v_stack_p18, v_stack_p20);
loc_009D53C9:
    *(uint64_t *)(arg10) = v_stack_m50;
loc_009D53DD:
    if (v_stack_m54 < 0) goto loc_009D54B7;
loc_009D53E8:
    if (v_stack_m58 > 0) goto loc_009D5418;
    local_rsi = 0;
    if (v_stack_m58 < 0) {
        local_rsi = (uint32_t)((0) | (4));
    }
    if ((uint32_t)(local_rsi) != 0) goto loc_009D541D;
loc_009D53F6:
    result = 0;
loc_009D53F8:
    local_rsp = (local_rsp) + (112);
    return result;
loc_009D5411:
    goto loc_009D53F8;
loc_009D5418:
    local_rsi = (uint32_t)((local_rsi) | (2));
    goto loc_009D53F2;
loc_009D541D:
    local_rdi = (Arg7 != 0) ? 1 : 0;
    result = ExpWnfNotifyNameSubscribers(Arg1, (uint32_t)((uint32_t)(local_rsi)), 1, (uint32_t)((uint32_t)(local_rdi)));
    *(uint32_t *)(arg11) = (uint32_t)(local_rsi);
    goto loc_009D53F6;
loc_009D5440:
    if (Arg9 == 0) goto loc_009D5283;
    *(uint64_t *)(Arg9) = result;
    goto loc_009D5283;
loc_009D545B:
    local_rbx = (v_stack_p8) | (-1);
    result = (uint8_t)((local_rbx) & (6));
    if (((uint8_t)(result)) == 2) goto loc_009D5598;
loc_009D5471:
    result = KeAbPostRelease(Arg1 + 112, (uint32_t)((uint32_t)(local_rsi)), 1, (uint32_t)((uint32_t)(local_rdi)));
    local_rbx = (uint8_t)((local_rbx) & (6));
    if (((uint8_t)(local_rbx)) == 2) goto loc_009D55A5;
loc_009D548A:
    result = KeAbPostRelease(local_rsi, (uint32_t)((uint32_t)(local_rsi)), 1, (uint32_t)((uint32_t)(local_rdi)));
    result = ExFreePoolWithTag(result, (uint32_t)(0x20666E57ULL), 1, (uint32_t)((uint32_t)(local_rdi)));
    goto loc_009D53F8;
loc_009D54A9:
    result = ExAcquireRundownProtection(result + 8, (uint32_t)(0x20666E57ULL), 1, (uint32_t)((uint32_t)(local_rdi)));
    goto loc_009D5368;
loc_009D54B7:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) + ((uint32_t)(local_rbx)));
    if (condition_is_equal) { local_rsi = 8; }
    goto loc_009D53E8;
loc_009D54D1:
    *(uint64_t *)(result + 0x8) = 8;
    *(uint64_t *)(result + 0x8 + 0x8) = (uint32_t)(0x20666E57ULL);
    *(uint64_t *)((uint32_t)(0x20666E57ULL)) = result + 8;
    *(uint64_t *)(8 + 0x8) = result + 8;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x78 + 0x8))) != (Arg1 + 120)) goto loc_009D5381;
    *(void **)(result + 0x40) = Arg1 + 120;
    *(uint64_t *)(result + 0x40 + 0x8) = *(uint64_t *)(arg1 + 0x78 + 0x8);
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x78 + 0x8)) = result + 64;
    *(uint64_t *)(arg1 + 0x78 + 0x8) = result + 64;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x64))) & (1));
    if ((uint8_t)(result) != 0) {
        Arg1 = 1;
        result = v_stack_m58;
        Arg1 = (uint32_t)((Arg1) + (1));
        if (((uint32_t)(Arg1)) == 1) { result = 1; }
        v_stack_m58 = (uint32_t)(result);
    }
    result = (uint8_t)((local_rbx) & (6));
    if (((uint8_t)(result)) == 2) goto loc_009D556A;
loc_009D553D:
    result = KeAbPostRelease(Arg1 + 112, *(uint64_t *)(arg1 + 0x78 + 0x8), 1, (uint32_t)((uint32_t)(local_rdi)));
    result = (uint8_t)((local_rbx) & (6));
    if (((uint8_t)(result)) == 2) goto loc_009D5574;
loc_009D5553:
    result = KeAbPostRelease(local_rsi, *(uint64_t *)(arg1 + 0x78 + 0x8), 1, (uint32_t)((uint32_t)(local_rdi)));
    *(uint64_t *)(arg10) = result;
    goto loc_009D53DD;
loc_009D556A:
    result = ExfTryToWakePushLock(Arg1 + 112, *(uint64_t *)(arg1 + 0x78 + 0x8), 1, (uint32_t)((uint32_t)(local_rdi)));
    goto loc_009D553D;
loc_009D5574:
    result = ExfTryToWakePushLock(local_rsi, *(uint64_t *)(arg1 + 0x78 + 0x8), 1, (uint32_t)((uint32_t)(local_rdi)));
    goto loc_009D5553;
loc_009D557E:
    result = ExfTryToWakePushLock(Arg1 + 112, *(uint64_t *)(arg1 + 0x78 + 0x8), 1, (uint32_t)((uint32_t)(local_rdi)));
    goto loc_009D539A;
loc_009D558B:
    result = ExfTryToWakePushLock(local_rsi, *(uint64_t *)(arg1 + 0x78 + 0x8), 1, (uint32_t)((uint32_t)(local_rdi)));
    goto loc_009D53B4;
loc_009D5598:
    result = ExfTryToWakePushLock(Arg1 + 112, *(uint64_t *)(arg1 + 0x78 + 0x8), 1, (uint32_t)((uint32_t)(local_rdi)));
    goto loc_009D5471;
loc_009D55A5:
    result = ExfTryToWakePushLock(local_rsi, *(uint64_t *)(arg1 + 0x78 + 0x8), 1, (uint32_t)((uint32_t)(local_rdi)));
    goto loc_009D548A;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R/W` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `W` |
| `Arg1` | `+ 0x28` | `64` | `R` |
| `Arg1` | `+ 0x30` | `64` | `R` |
| `Arg1` | `+ 0x70` | `64` | `R` |
| `Arg1` | `+ 0x78` | `64` | `R` |
| `Arg1` | `+ 0xA0` | `32` | `R/W` |
| `Arg1` | `+ 0xA4` | `32` | `R/W` |
| `Arg2` | `+ 0x5E8` | `64` | `R` |
| `Arg10` | `+ 0x0` | `64` | `W` |
| `Arg11` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009D50E8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
