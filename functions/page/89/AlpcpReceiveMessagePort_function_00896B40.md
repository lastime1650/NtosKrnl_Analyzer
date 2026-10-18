# AlpcpReceiveMessagePort

- RVA: `0x00896B40`–`0x008973F9` (길이 `2,233` bytes)
- VA: `0x0000000140896B40`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0007E260`
- 디코드: `539`개 명령, `2,233/2,233` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **64**; 고유 호출 대상: **17**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00896B98` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00896BB4` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)
- `0x00896BEA` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00896C03` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x00896C14` → [AlpcpQueryHeadLargeQueue](AlpcpQueryHeadLargeQueue_function_00897400.md) (function, `0x00897400`)
- `0x00896C28` → [AlpcpQueryHeadMainQueue](AlpcpQueryHeadMainQueue_function_00897444.md) (function, `0x00897444`)
- `0x00896C3C` → [AlpcpQueryHeadCanceledQueue](AlpcpQueryHeadCanceledQueue_function_0089741C.md) (function, `0x0089741C`)
- `0x00896C85` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00896CA9` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x00896CB1` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00896CD2` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00896D40` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00896D5A` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x00896DB1` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x00896DB9` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00896DC6` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00896DDF` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x00896E1A` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00896E51` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x00896E7F` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (function, `0x0020E6B0`)
- `0x00896ED7` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00896EF1` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00896F28` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x00896F56` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (function, `0x0020E6B0`)
- `0x00896FA6` → [AlpcpLockForCachedReferenceBlob](../88/AlpcpLockForCachedReferenceBlob_function_0088A8B0.md) (function, `0x0088A8B0`)
- `0x00897009` → [AlpcpSignalAndWait](../../text/2F/AlpcpSignalAndWait_function_002F9620.md) (function, `0x002F9620`)
- `0x00897018` → [AlpcpTryLockForCachedReferenceBlob](../9E/AlpcpTryLockForCachedReferenceBlob_function_009E7920.md) (function, `0x009E7920`)
- `0x0089703A` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0089705F` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0089706C` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00897085` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x008970A4` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x008970BE` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x008970ED` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x008970FB` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x00897113` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (function, `0x0020E6B0`)
- `0x0089716F` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x008971A0` → [AlpcpSignalAndWait](../../text/2F/AlpcpSignalAndWait_function_002F9620.md) (function, `0x002F9620`)
- `0x008971C3` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x008971D0` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x008971DD` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x008971EA` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x008971F7` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x00897204` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x00897211` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x0089721E` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x0089723C` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x00897244` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00897265` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x008972A8` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x008972C3` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x008972E6` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00897341` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0089734E` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x0089735B` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x00897365` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x00897376` → [AlpcpTryLockForCachedReferenceBlob](../9E/AlpcpTryLockForCachedReferenceBlob_function_009E7920.md) (function, `0x009E7920`)
- `0x008973A3` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x008973B1` → [AlpcpLogWaitForNewMessage](../74/AlpcpLogWaitForNewMessage_function_0074D294.md) (function, `0x0074D294`)
- `0x008973BD` → [AlpcpLogUnwait](../74/AlpcpLogUnwait_function_0074D228.md) (function, `0x0074D228`)
- `0x008973CA` → [AlpcpLogWaitForNewMessage](../74/AlpcpLogWaitForNewMessage_function_0074D294.md) (function, `0x0074D294`)
- `0x008973D6` → [AlpcpLogUnwait](../74/AlpcpLogUnwait_function_0074D228.md) (function, `0x0074D228`)
- `0x008973E2` → [AlpcpLogUnwait](../74/AlpcpLogUnwait_function_0074D228.md) (function, `0x0074D228`)
- `0x008973EF` → [AlpcpLogReceiveMessage](../88/AlpcpLogReceiveMessage_function_0088F80C.md) (function, `0x0088F80C`)

### Direct callers
- [AlpcpReceiveLegacyMessage](AlpcpReceiveLegacyMessage_function_00895DE0.md) at `0x00895EFA`
- [AlpcpReceiveMessage](AlpcpReceiveMessage_function_00897ED0.md) at `0x008981AA`

### Static image references
- `0x00896E1F` → RVA `0x00E66D00` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **52**
  - `0x00896B98` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x00896BB4` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (`PAGE` → `.text`)
  - `0x00896BEA` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x00896C03` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x00896C85` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x00896CA9` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x00896CB1` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x00896CD2` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x00896D40` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x00896D5A` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x00896DB1` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x00896DB9` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x00896DC6` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x00896DDF` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x00896E1A` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x00896E51` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x00896E7F` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (`PAGE` → `.text`)
  - `0x00896ED7` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x00896EF1` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x00896F28` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x00896F56` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (`PAGE` → `.text`)
  - `0x00897009` → [AlpcpSignalAndWait](../../text/2F/AlpcpSignalAndWait_function_002F9620.md) (`PAGE` → `.text`)
  - `0x0089703A` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0089705F` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0089706C` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x00897085` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x008970A4` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x008970BE` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x008970ED` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x008970FB` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x00897113` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (`PAGE` → `.text`)
  - `0x0089716F` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x008971A0` → [AlpcpSignalAndWait](../../text/2F/AlpcpSignalAndWait_function_002F9620.md) (`PAGE` → `.text`)
  - `0x008971C3` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x008971D0` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x008971DD` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x008971EA` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x008971F7` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x00897204` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x00897211` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x0089721E` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x0089723C` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x00897244` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x00897265` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x008972A8` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x008972C3` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x008972E6` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x00897341` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0089734E` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x0089735B` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x00897365` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x008973A3` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **4**
  - `0x0089737D` → [sub_00B197CC + 0x216](../B1/Unknown_function_00B197CC.md) (`tail-transfer`)
  - `0x00897388` → [sub_00B197CC + 0x66](../B1/Unknown_function_00B197CC.md) (`tail-transfer`)
  - `0x0089739A` → [sub_00B197CC](../B1/Unknown_function_00B197CC.md) (`tail-transfer`)
  - `0x008973A9` → [sub_00B197CC](../B1/Unknown_function_00B197CC.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00896B40  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
00896B45  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
00896B4A  88 54 24 10                     mov byte ptr [rsp + 0x10], dl
00896B4E  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
00896B53  53                              push rbx
00896B54  55                              push rbp
00896B55  56                              push rsi
00896B56  57                              push rdi
00896B57  41 54                           push r12
00896B59  41 55                           push r13
00896B5B  41 56                           push r14
00896B5D  41 57                           push r15
00896B5F  48 83 EC 48                     sub rsp, 0x48
00896B63  65 4C 8B 24 25 88 01 00 00      mov r12, qword ptr gs:[0x188]
00896B6C  4C 8B E9                        mov r13, rcx
00896B6F  48 8B 39                        mov rdi, qword ptr [rcx]
00896B72  48 C7 C3 FF FF FF FF            mov rbx, 0xffffffffffffffff
00896B79  4C 89 64 24 30                  mov qword ptr [rsp + 0x30], r12
00896B7E  4C 8D B7 60 01 00 00            lea r14, [rdi + 0x160]
00896B85  41 BF 11 00 00 00               mov r15d, 0x11
00896B8B  33 ED                           xor ebp, ebp
00896B8D  0F 1F 00                        nop dword ptr [rax]
00896B90  45 33 C0                        xor r8d, r8d
00896B93  33 D2                           xor edx, edx
00896B95  49 8B CE                        mov rcx, r14
00896B98  E8 93 96 97 FF                  call 0x140210230
00896B9D  48 8B F0                        mov rsi, rax
00896BA0  33 C0                           xor eax, eax
00896BA2  F0 4D 0F B1 3E                  lock cmpxchg qword ptr [r14], r15
00896BA7  74 10                           je 0x140896bb9
00896BA9  4D 8B CE                        mov r9, r14
00896BAC  4C 8B C6                        mov r8, rsi
00896BAF  33 D2                           xor edx, edx
00896BB1  49 8B CE                        mov rcx, r14
00896BB4  E8 93 98 97 FF                  call 0x14021044c
00896BB9  48 85 F6                        test rsi, rsi
00896BBC  74 04                           je 0x140896bc2
00896BBE  C6 46 0A 01                     mov byte ptr [rsi + 0xa], 1
00896BC2  44 8B FD                        mov r15d, ebp
00896BC5  8B 87 A0 01 00 00               mov eax, dword ptr [rdi + 0x1a0]
00896BCB  A8 40                           test al, 0x40
00896BCD  0F 85 D9 05 00 00               jne 0x1408971ac
00896BD3  A8 10                           test al, 0x10
00896BD5  0F 85 DB 05 00 00               jne 0x1408971b6
00896BDB  48 8D B7 88 00 00 00            lea rsi, [rdi + 0x88]
00896BE2  45 33 C0                        xor r8d, r8d
00896BE5  48 8B CE                        mov rcx, rsi
00896BE8  33 D2                           xor edx, edx
00896BEA  E8 41 96 97 FF                  call 0x140210230
00896BEF  F0 48 0F BA 2E 00               lock bts qword ptr [rsi], 0
00896BF5  48 8B E8                        mov rbp, rax
00896BF8  73 0E                           jae 0x140896c08
00896BFA  4C 8B C6                        mov r8, rsi
00896BFD  48 8B D0                        mov rdx, rax
00896C00  48 8B CE                        mov rcx, rsi
00896C03  E8 88 90 97 FF                  call 0x14020fc90
00896C08  48 85 ED                        test rbp, rbp
00896C0B  74 04                           je 0x140896c11
00896C0D  C6 45 0A 01                     mov byte ptr [rbp + 0xa], 1
00896C11  48 8B CF                        mov rcx, rdi
00896C14  E8 E7 07 00 00                  call 0x140897400
00896C19  48 8B E8                        mov rbp, rax
00896C1C  48 85 C0                        test rax, rax
00896C1F  0F 85 4E 07 00 00               jne 0x140897373
00896C25  48 8B CF                        mov rcx, rdi
00896C28  E8 17 08 00 00                  call 0x140897444
00896C2D  48 8B E8                        mov rbp, rax
00896C30  48 85 C0                        test rax, rax
00896C33  0F 85 3A 07 00 00               jne 0x140897373
00896C39  48 8B CF                        mov rcx, rdi
00896C3C  E8 DB 07 00 00                  call 0x14089741c
00896C41  48 8B E8                        mov rbp, rax
00896C44  48 85 C0                        test rax, rax
00896C47  0F 85 C8 03 00 00               jne 0x140897015
00896C4D  48 8B 87 68 01 00 00            mov rax, qword ptr [rdi + 0x168]
00896C54  48 85 C0                        test rax, rax
00896C57  74 64                           je 0x140896cbd
00896C59  48 8B 40 50                     mov rax, qword ptr [rax + 0x50]
00896C5D  48 8B 48 40                     mov rcx, qword ptr [rax + 0x40]
00896C61  81 E1 FF FF FF 00               and ecx, 0xffffff
00896C67  48 81 F9 FF FF FF 00            cmp rcx, 0xffffff
00896C6E  74 4D                           je 0x140896cbd
00896C70  48 8B C3                        mov rax, rbx
00896C73  F0 48 0F C1 06                  lock xadd qword ptr [rsi], rax
00896C78  24 06                           and al, 6
00896C7A  3C 02                           cmp al, 2
00896C7C  0F 84 3E 05 00 00               je 0x1408971c0
00896C82  48 8B CE                        mov rcx, rsi
00896C85  E8 76 A9 A4 FF                  call 0x1402e1600
00896C8A  33 ED                           xor ebp, ebp
00896C8C  BF 30 00 00 40                  mov edi, 0x40000030
00896C91  45 85 FF                        test r15d, r15d
00896C94  0F 85 8E 05 00 00               jne 0x140897228
00896C9A  B8 11 00 00 00                  mov eax, 0x11
00896C9F  F0 49 0F B1 2E                  lock cmpxchg qword ptr [r14], rbp
00896CA4  74 08                           je 0x140896cae
00896CA6  49 8B CE                        mov rcx, r14
00896CA9  E8 92 C7 9C FF                  call 0x140263440
00896CAE  49 8B CE                        mov rcx, r14
00896CB1  E8 4A A9 A4 FF                  call 0x1402e1600
00896CB6  8B C7                           mov eax, edi
00896CB8  E9 13 03 00 00                  jmp 0x140896fd0
00896CBD  48 8B C3                        mov rax, rbx
00896CC0  F0 48 0F C1 06                  lock xadd qword ptr [rsi], rax
00896CC5  24 06                           and al, 6
00896CC7  3C 02                           cmp al, 2
00896CC9  0F 84 FE 04 00 00               je 0x1408971cd
00896CCF  48 8B CE                        mov rcx, rsi
00896CD2  E8 29 A9 A4 FF                  call 0x1402e1600
00896CD7  48 83 7F 20 00                  cmp qword ptr [rdi + 0x20], 0
00896CDC  75 1C                           jne 0x140896cfa
00896CDE  F7 87 A0 01 00 00 00 02 00 00   test dword ptr [rdi + 0x1a0], 0x200
00896CE8  74 19                           je 0x140896d03
00896CEA  F7 87 00 01 00 00 00 10 00 00   test dword ptr [rdi + 0x100], 0x1000
00896CF4  0F 85 FC 00 00 00               jne 0x140896df6
00896CFA  BF 01 00 00 C0                  mov edi, 0xc0000001
00896CFF  33 ED                           xor ebp, ebp
00896D01  EB 8E                           jmp 0x140896c91
00896D03  48 83 BF 70 01 00 00 00         cmp qword ptr [rdi + 0x170], 0
00896D0B  0F 85 B9 05 00 00               jne 0x1408972ca
00896D11  41 8B 84 24 A4 05 00 00         mov eax, dword ptr [r12 + 0x5a4]
00896D19  A8 20                           test al, 0x20
00896D1B  75 DD                           jne 0x140896cfa
00896D1D  45 85 FF                        test r15d, r15d
00896D20  74 69                           je 0x140896d8b
00896D22  8B 84 24 B0 00 00 00            mov eax, dword ptr [rsp + 0xb0]
00896D29  48 8D AF E0 00 00 00            lea rbp, [rdi + 0xe0]
00896D30  48 8B CD                        mov rcx, rbp
00896D33  41 89 84 24 C0 05 00 00         mov dword ptr [r12 + 0x5c0], eax
00896D3B  45 33 C0                        xor r8d, r8d
00896D3E  33 D2                           xor edx, edx
00896D40  E8 EB 94 97 FF                  call 0x140210230
00896D45  F0 48 0F BA 6D 00 00            lock bts qword ptr [rbp], 0
00896D4C  48 8B F0                        mov rsi, rax
00896D4F  73 0E                           jae 0x140896d5f
00896D51  4C 8B C5                        mov r8, rbp
00896D54  48 8B D0                        mov rdx, rax
00896D57  48 8B CD                        mov rcx, rbp
00896D5A  E8 31 8F 97 FF                  call 0x14020fc90
00896D5F  48 85 F6                        test rsi, rsi
00896D62  74 04                           je 0x140896d68
00896D64  C6 46 0A 01                     mov byte ptr [rsi + 0xa], 1
00896D68  48 8D 87 E8 00 00 00            lea rax, [rdi + 0xe8]
00896D6F  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
00896D73  4D 8D BC 24 C8 05 00 00         lea r15, [r12 + 0x5c8]
00896D7B  48 39 01                        cmp qword ptr [rcx], rax
00896D7E  0F 84 2F 01 00 00               je 0x140896eb3
00896D84  B9 03 00 00 00                  mov ecx, 3
00896D89  CD 29                           int 0x29
00896D8B  B9 11 00 00 00                  mov ecx, 0x11
00896D90  41 BF 01 00 00 00               mov r15d, 1
00896D96  8B C1                           mov eax, ecx
00896D98  F0 4D 0F B1 3E                  lock cmpxchg qword ptr [r14], r15
00896D9D  0F 84 C9 05 00 00               je 0x14089736c
00896DA3  8B C1                           mov eax, ecx
00896DA5  33 ED                           xor ebp, ebp
00896DA7  F0 49 0F B1 2E                  lock cmpxchg qword ptr [r14], rbp
00896DAC  74 08                           je 0x140896db6
00896DAE  49 8B CE                        mov rcx, r14
00896DB1  E8 8A C6 9C FF                  call 0x140263440
00896DB6  49 8B CE                        mov rcx, r14
00896DB9  E8 42 A8 A4 FF                  call 0x1402e1600
00896DBE  45 33 C0                        xor r8d, r8d
00896DC1  33 D2                           xor edx, edx
00896DC3  49 8B CE                        mov rcx, r14
00896DC6  E8 65 94 97 FF                  call 0x140210230
00896DCB  F0 49 0F BA 2E 00               lock bts qword ptr [r14], 0
00896DD1  48 8B F0                        mov rsi, rax
00896DD4  73 0E                           jae 0x140896de4
00896DD6  4D 8B C6                        mov r8, r14
00896DD9  48 8B D0                        mov rdx, rax
00896DDC  49 8B CE                        mov rcx, r14
00896DDF  E8 AC 8E 97 FF                  call 0x14020fc90
00896DE4  48 85 F6                        test rsi, rsi
00896DE7  0F 84 D8 FD FF FF               je 0x140896bc5
00896DED  44 88 7E 0A                     mov byte ptr [rsi + 0xa], r15b
00896DF1  E9 CF FD FF FF                  jmp 0x140896bc5
00896DF6  45 85 FF                        test r15d, r15d
00896DF9  0F 84 57 03 00 00               je 0x140897156
00896DFF  48 8B C3                        mov rax, rbx
00896E02  F0 49 0F C1 06                  lock xadd qword ptr [r14], rax
00896E07  24 06                           and al, 6
00896E09  3C 02                           cmp al, 2
00896E0B  0F 84 0A 04 00 00               je 0x14089721b
00896E11  41 BF 11 00 00 00               mov r15d, 0x11
00896E17  49 8B CE                        mov rcx, r14
00896E1A  E8 E1 A7 A4 FF                  call 0x1402e1600
00896E1F  80 3D DA FE 5C 00 00            cmp byte ptr [rip + 0x5cfeda], 0
00896E26  0F 85 9B 05 00 00               jne 0x1408973c7
00896E2C  48 8B AF F8 00 00 00            mov rbp, qword ptr [rdi + 0xf8]
00896E33  41 0F BA 75 30 02               btr dword ptr [r13 + 0x30], 2
00896E39  0F 92 C0                        setb al
00896E3C  84 C0                           test al, al
00896E3E  0F 85 35 03 00 00               jne 0x140897179
00896E44  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00896E4D  41 8B 75 30                     mov esi, dword ptr [r13 + 0x30]
00896E51  E8 9A 81 9C FF                  call 0x14025eff0
00896E56  48 8B 84 24 A0 00 00 00         mov rax, qword ptr [rsp + 0xa0]
00896E5E  BA 10 00 00 00                  mov edx, 0x10
00896E63  44 0F B6 84 24 98 00 00 00      movzx r8d, byte ptr [rsp + 0x98]
00896E6C  48 8B CD                        mov rcx, rbp
00896E6F  C1 EE 15                        shr esi, 0x15
00896E72  40 80 E6 01                     and sil, 1
00896E76  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00896E7B  44 0F B6 CE                     movzx r9d, sil
00896E7F  E8 2C 78 97 FF                  call 0x14020e6b0
00896E84  8B F0                           mov esi, eax
00896E86  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00896E8F  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00896E96  90                              nop
00896E97  80 3D 62 FE 5C 00 00            cmp byte ptr [rip + 0x5cfe62], 0
00896E9E  0F 85 30 05 00 00               jne 0x1408973d4
00896EA4  85 F6                           test esi, esi
00896EA6  0F 84 DF FC FF FF               je 0x140896b8b
00896EAC  8B C6                           mov eax, esi
00896EAE  E9 1D 01 00 00                  jmp 0x140896fd0
00896EB3  49 89 07                        mov qword ptr [r15], rax
00896EB6  49 89 4F 08                     mov qword ptr [r15 + 8], rcx
00896EBA  4C 89 39                        mov qword ptr [rcx], r15
00896EBD  4C 89 78 08                     mov qword ptr [rax + 8], r15
00896EC1  48 8B C3                        mov rax, rbx
00896EC4  F0 48 0F C1 45 00               lock xadd qword ptr [rbp], rax
00896ECA  24 06                           and al, 6
00896ECC  3C 02                           cmp al, 2
00896ECE  0F 84 06 03 00 00               je 0x1408971da
00896ED4  48 8B CD                        mov rcx, rbp
00896ED7  E8 24 A7 A4 FF                  call 0x1402e1600
00896EDC  48 8B C3                        mov rax, rbx
00896EDF  F0 49 0F C1 06                  lock xadd qword ptr [r14], rax
00896EE4  24 06                           and al, 6
00896EE6  3C 02                           cmp al, 2
00896EE8  0F 84 F9 02 00 00               je 0x1408971e7
00896EEE  49 8B CE                        mov rcx, r14
00896EF1  E8 0A A7 A4 FF                  call 0x1402e1600
00896EF6  80 3D 03 FE 5C 00 00            cmp byte ptr [rip + 0x5cfe03], 0
00896EFD  0F 85 AB 04 00 00               jne 0x1408973ae
00896F03  49 81 C4 18 05 00 00            add r12, 0x518
00896F0A  41 0F BA 75 30 02               btr dword ptr [r13 + 0x30], 2
00896F10  0F 92 C0                        setb al
00896F13  84 C0                           test al, al
00896F15  0F 85 C7 00 00 00               jne 0x140896fe2
00896F1B  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00896F24  41 8B 75 30                     mov esi, dword ptr [r13 + 0x30]
00896F28  E8 C3 80 9C FF                  call 0x14025eff0
00896F2D  48 8B 84 24 A0 00 00 00         mov rax, qword ptr [rsp + 0xa0]
00896F35  BA 10 00 00 00                  mov edx, 0x10
00896F3A  44 0F B6 84 24 98 00 00 00      movzx r8d, byte ptr [rsp + 0x98]
00896F43  49 8B CC                        mov rcx, r12
00896F46  C1 EE 15                        shr esi, 0x15
00896F49  40 80 E6 01                     and sil, 1
00896F4D  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00896F52  44 0F B6 CE                     movzx r9d, sil
00896F56  E8 55 77 97 FF                  call 0x14020e6b0
00896F5B  8B F0                           mov esi, eax
00896F5D  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00896F66  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00896F6D  90                              nop
00896F6E  80 3D 8B FD 5C 00 00            cmp byte ptr [rip + 0x5cfd8b], 0
00896F75  0F 85 40 04 00 00               jne 0x1408973bb
00896F7B  33 D2                           xor edx, edx
00896F7D  85 F6                           test esi, esi
00896F7F  0F 85 19 01 00 00               jne 0x14089709e
00896F85  4C 8B 64 24 30                  mov r12, qword ptr [rsp + 0x30]
00896F8A  49 8B AC 24 C0 05 00 00         mov rbp, qword ptr [r12 + 0x5c0]
00896F92  49 89 94 24 C0 05 00 00         mov qword ptr [r12 + 0x5c0], rdx
00896F9A  48 85 ED                        test rbp, rbp
00896F9D  0F 84 E2 FB FF FF               je 0x140896b85
00896FA3  48 8B CD                        mov rcx, rbp
00896FA6  E8 05 39 FF FF                  call 0x14088a8b0
00896FAB  66 FF 4D E2                     dec word ptr [rbp - 0x1e]
00896FAF  81 65 28 FF DF FF FF            and dword ptr [rbp + 0x28], 0xffffdfff
00896FB6  80 3D 43 FD 5C 00 00            cmp byte ptr [rip + 0x5cfd43], 0
00896FBD  0F 85 29 04 00 00               jne 0x1408973ec
00896FC3  48 8B 84 24 A8 00 00 00         mov rax, qword ptr [rsp + 0xa8]
00896FCB  48 89 28                        mov qword ptr [rax], rbp
00896FCE  33 C0                           xor eax, eax
00896FD0  48 83 C4 48                     add rsp, 0x48
00896FD4  41 5F                           pop r15
00896FD6  41 5E                           pop r14
00896FD8  41 5D                           pop r13
00896FDA  41 5C                           pop r12
00896FDC  5F                              pop rdi
00896FDD  5E                              pop rsi
00896FDE  5D                              pop rbp
00896FDF  5B                              pop rbx
00896FE0  C3                              ret
00896FE1  CC                              int3
00896FE2  48 8B 84 24 A0 00 00 00         mov rax, qword ptr [rsp + 0xa0]
00896FEA  41 B8 10 00 00 00               mov r8d, 0x10
00896FF0  44 0F B6 8C 24 98 00 00 00      movzx r9d, byte ptr [rsp + 0x98]
00896FF9  49 8B D4                        mov rdx, r12
00896FFC  C6 44 24 28 00                  mov byte ptr [rsp + 0x28], 0
00897001  49 8B CD                        mov rcx, r13
00897004  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00897009  E8 12 26 A6 FF                  call 0x1402f9620
0089700E  8B F0                           mov esi, eax
00897010  E9 66 FF FF FF                  jmp 0x140896f7b
00897015  48 8B CD                        mov rcx, rbp
00897018  E8 03 09 15 00                  call 0x1409e7920
0089701D  84 C0                           test al, al
0089701F  0F 85 4A 02 00 00               jne 0x14089726f
00897025  48 8B C3                        mov rax, rbx
00897028  F0 48 0F C1 06                  lock xadd qword ptr [rsi], rax
0089702D  24 06                           and al, 6
0089702F  3C 02                           cmp al, 2
00897031  0F 84 BD 01 00 00               je 0x1408971f4
00897037  48 8B CE                        mov rcx, rsi
0089703A  E8 C1 A5 A4 FF                  call 0x1402e1600
0089703F  45 85 FF                        test r15d, r15d
00897042  0F 84 08 02 00 00               je 0x140897250
00897048  48 8B C3                        mov rax, rbx
0089704B  F0 49 0F C1 06                  lock xadd qword ptr [r14], rax
00897050  24 06                           and al, 6
00897052  3C 02                           cmp al, 2
00897054  0F 84 A7 01 00 00               je 0x140897201
0089705A  33 ED                           xor ebp, ebp
0089705C  49 8B CE                        mov rcx, r14
0089705F  E8 9C A5 A4 FF                  call 0x1402e1600
00897064  45 33 C0                        xor r8d, r8d
00897067  33 D2                           xor edx, edx
00897069  49 8B CE                        mov rcx, r14
0089706C  E8 BF 91 97 FF                  call 0x140210230
00897071  F0 49 0F BA 2E 00               lock bts qword ptr [r14], 0
00897077  48 8B F0                        mov rsi, rax
0089707A  73 0E                           jae 0x14089708a
0089707C  4D 8B C6                        mov r8, r14
0089707F  48 8B D6                        mov rdx, rsi
00897082  49 8B CE                        mov rcx, r14
00897085  E8 06 8C 97 FF                  call 0x14020fc90
0089708A  48 85 F6                        test rsi, rsi
0089708D  74 04                           je 0x140897093
0089708F  C6 46 0A 01                     mov byte ptr [rsi + 0xa], 1
00897093  41 BF 01 00 00 00               mov r15d, 1
00897099  E9 27 FB FF FF                  jmp 0x140896bc5
0089709E  45 33 C0                        xor r8d, r8d
008970A1  48 8B CD                        mov rcx, rbp
008970A4  E8 87 91 97 FF                  call 0x140210230
008970A9  F0 48 0F BA 6D 00 00            lock bts qword ptr [rbp], 0
008970B0  48 8B F8                        mov rdi, rax
008970B3  73 0E                           jae 0x1408970c3
008970B5  4C 8B C5                        mov r8, rbp
008970B8  48 8B D0                        mov rdx, rax
008970BB  48 8B CD                        mov rcx, rbp
008970BE  E8 CD 8B 97 FF                  call 0x14020fc90
008970C3  48 85 FF                        test rdi, rdi
008970C6  74 04                           je 0x1408970cc
008970C8  C6 47 0A 01                     mov byte ptr [rdi + 0xa], 1
008970CC  49 8B 07                        mov rax, qword ptr [r15]
008970CF  48 85 C0                        test rax, rax
008970D2  0F 85 29 02 00 00               jne 0x140897301
008970D8  F0 48 0F C1 5D 00               lock xadd qword ptr [rbp], rbx
008970DE  80 E3 06                        and bl, 6
008970E1  80 FB 02                        cmp bl, 2
008970E4  0F 84 24 01 00 00               je 0x14089720e
008970EA  48 8B CD                        mov rcx, rbp
008970ED  E8 0E A5 A4 FF                  call 0x1402e1600
008970F2  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
008970FB  E8 F0 7E 9C FF                  call 0x14025eff0
00897100  33 DB                           xor ebx, ebx
00897102  45 33 C9                        xor r9d, r9d
00897105  45 33 C0                        xor r8d, r8d
00897108  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
0089710D  49 8B CC                        mov rcx, r12
00897110  8D 53 10                        lea edx, [rbx + 0x10]
00897113  E8 98 75 97 FF                  call 0x14020e6b0
00897118  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00897121  66 FF 89 E4 01 00 00            dec word ptr [rcx + 0x1e4]
00897128  90                              nop
00897129  38 1D D1 FB 5C 00               cmp byte ptr [rip + 0x5cfbd1], bl
0089712F  0F 85 AB 02 00 00               jne 0x1408973e0
00897135  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0089713A  48 8B A9 C0 05 00 00            mov rbp, qword ptr [rcx + 0x5c0]
00897141  48 89 99 C0 05 00 00            mov qword ptr [rcx + 0x5c0], rbx
00897148  48 85 ED                        test rbp, rbp
0089714B  0F 85 52 FE FF FF               jne 0x140896fa3
00897151  E9 56 FD FF FF                  jmp 0x140896eac
00897156  41 BF 11 00 00 00               mov r15d, 0x11
0089715C  33 D2                           xor edx, edx
0089715E  41 8B C7                        mov eax, r15d
00897161  F0 49 0F B1 16                  lock cmpxchg qword ptr [r14], rdx
00897166  0F 84 AB FC FF FF               je 0x140896e17
0089716C  49 8B CE                        mov rcx, r14
0089716F  E8 CC C2 9C FF                  call 0x140263440
00897174  E9 9E FC FF FF                  jmp 0x140896e17
00897179  48 8B 84 24 A0 00 00 00         mov rax, qword ptr [rsp + 0xa0]
00897181  41 B8 10 00 00 00               mov r8d, 0x10
00897187  44 0F B6 8C 24 98 00 00 00      movzx r9d, byte ptr [rsp + 0x98]
00897190  48 8B D5                        mov rdx, rbp
00897193  C6 44 24 28 00                  mov byte ptr [rsp + 0x28], 0
00897198  49 8B CD                        mov rcx, r13
0089719B  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008971A0  E8 7B 24 A6 FF                  call 0x1402f9620
008971A5  8B F0                           mov esi, eax
008971A7  E9 F8 FC FF FF                  jmp 0x140896ea4
008971AC  BF 00 07 00 C0                  mov edi, 0xc0000700
008971B1  E9 DB FA FF FF                  jmp 0x140896c91
008971B6  BF 41 00 00 C0                  mov edi, 0xc0000041
008971BB  E9 D1 FA FF FF                  jmp 0x140896c91
008971C0  48 8B CE                        mov rcx, rsi
008971C3  E8 08 EC 9C FF                  call 0x140265dd0
008971C8  E9 B5 FA FF FF                  jmp 0x140896c82
008971CD  48 8B CE                        mov rcx, rsi
008971D0  E8 FB EB 9C FF                  call 0x140265dd0
008971D5  E9 F5 FA FF FF                  jmp 0x140896ccf
008971DA  48 8B CD                        mov rcx, rbp
008971DD  E8 EE EB 9C FF                  call 0x140265dd0
008971E2  E9 ED FC FF FF                  jmp 0x140896ed4
008971E7  49 8B CE                        mov rcx, r14
008971EA  E8 E1 EB 9C FF                  call 0x140265dd0
008971EF  E9 FA FC FF FF                  jmp 0x140896eee
008971F4  48 8B CE                        mov rcx, rsi
008971F7  E8 D4 EB 9C FF                  call 0x140265dd0
008971FC  E9 36 FE FF FF                  jmp 0x140897037
00897201  49 8B CE                        mov rcx, r14
00897204  E8 C7 EB 9C FF                  call 0x140265dd0
00897209  E9 4C FE FF FF                  jmp 0x14089705a
0089720E  48 8B CD                        mov rcx, rbp
00897211  E8 BA EB 9C FF                  call 0x140265dd0
00897216  E9 CF FE FF FF                  jmp 0x1408970ea
0089721B  49 8B CE                        mov rcx, r14
0089721E  E8 AD EB 9C FF                  call 0x140265dd0
00897223  E9 E9 FB FF FF                  jmp 0x140896e11
00897228  F0 49 0F C1 1E                  lock xadd qword ptr [r14], rbx
0089722D  80 E3 06                        and bl, 6
00897230  80 FB 02                        cmp bl, 2
00897233  0F 85 75 FA FF FF               jne 0x140896cae
00897239  49 8B CE                        mov rcx, r14
0089723C  E8 8F EB 9C FF                  call 0x140265dd0
00897241  49 8B CE                        mov rcx, r14
00897244  E8 B7 A3 A4 FF                  call 0x1402e1600
00897249  8B C7                           mov eax, edi
0089724B  E9 80 FD FF FF                  jmp 0x140896fd0
00897250  B8 11 00 00 00                  mov eax, 0x11
00897255  33 ED                           xor ebp, ebp
00897257  F0 49 0F B1 2E                  lock cmpxchg qword ptr [r14], rbp
0089725C  0F 84 FA FD FF FF               je 0x14089705c
00897262  49 8B CE                        mov rcx, r14
00897265  E8 D6 C1 9C FF                  call 0x140263440
0089726A  E9 ED FD FF FF                  jmp 0x14089705c
0089726F  81 65 28 FF FF FD FF            and dword ptr [rbp + 0x28], 0xfffdffff
00897276  48 8B 4D 58                     mov rcx, qword ptr [rbp + 0x58]
0089727A  48 8B 45 50                     mov rax, qword ptr [rbp + 0x50]
0089727E  48 89 01                        mov qword ptr [rcx], rax
00897281  48 8B 45 58                     mov rax, qword ptr [rbp + 0x58]
00897285  48 8B 4D 50                     mov rcx, qword ptr [rbp + 0x50]
00897289  48 89 41 08                     mov qword ptr [rcx + 8], rax
0089728D  48 8B C3                        mov rax, rbx
00897290  FF 8F D0 01 00 00               dec dword ptr [rdi + 0x1d0]
00897296  F0 48 0F C1 06                  lock xadd qword ptr [rsi], rax
0089729B  24 06                           and al, 6
0089729D  3C 02                           cmp al, 2
0089729F  0F 84 A6 00 00 00               je 0x14089734b
008972A5  48 8B CE                        mov rcx, rsi
008972A8  E8 53 A3 A4 FF                  call 0x1402e1600
008972AD  45 85 FF                        test r15d, r15d
008972B0  75 24                           jne 0x1408972d6
008972B2  B8 11 00 00 00                  mov eax, 0x11
008972B7  33 D2                           xor edx, edx
008972B9  F0 49 0F B1 16                  lock cmpxchg qword ptr [r14], rdx
008972BE  74 23                           je 0x1408972e3
008972C0  49 8B CE                        mov rcx, r14
008972C3  E8 78 C1 9C FF                  call 0x140263440
008972C8  EB 19                           jmp 0x1408972e3
008972CA  BF 02 01 00 00                  mov edi, 0x102
008972CF  33 ED                           xor ebp, ebp
008972D1  E9 BB F9 FF FF                  jmp 0x140896c91
008972D6  F0 49 0F C1 1E                  lock xadd qword ptr [r14], rbx
008972DB  80 E3 06                        and bl, 6
008972DE  80 FB 02                        cmp bl, 2
008972E1  74 75                           je 0x140897358
008972E3  49 8B CE                        mov rcx, r14
008972E6  E8 15 A3 A4 FF                  call 0x1402e1600
008972EB  48 8B 84 24 A8 00 00 00         mov rax, qword ptr [rsp + 0xa8]
008972F3  66 FF 4D E2                     dec word ptr [rbp - 0x1e]
008972F7  48 89 28                        mov qword ptr [rax], rbp
008972FA  33 C0                           xor eax, eax
008972FC  E9 CF FC FF FF                  jmp 0x140896fd0
00897301  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
00897306  33 D2                           xor edx, edx
00897308  48 89 91 C0 05 00 00            mov qword ptr [rcx + 0x5c0], rdx
0089730F  4C 39 78 08                     cmp qword ptr [rax + 8], r15
00897313  0F 85 6B FA FF FF               jne 0x140896d84
00897319  49 8B 4F 08                     mov rcx, qword ptr [r15 + 8]
0089731D  4C 39 39                        cmp qword ptr [rcx], r15
00897320  0F 85 5E FA FF FF               jne 0x140896d84
00897326  48 89 01                        mov qword ptr [rcx], rax
00897329  48 89 48 08                     mov qword ptr [rax + 8], rcx
0089732D  49 89 17                        mov qword ptr [r15], rdx
00897330  F0 48 0F C1 5D 00               lock xadd qword ptr [rbp], rbx
00897336  80 E3 06                        and bl, 6
00897339  80 FB 02                        cmp bl, 2
0089733C  74 24                           je 0x140897362
0089733E  48 8B CD                        mov rcx, rbp
00897341  E8 BA A2 A4 FF                  call 0x1402e1600
00897346  E9 61 FB FF FF                  jmp 0x140896eac
0089734B  48 8B CE                        mov rcx, rsi
0089734E  E8 7D EA 9C FF                  call 0x140265dd0
00897353  E9 4D FF FF FF                  jmp 0x1408972a5
00897358  49 8B CE                        mov rcx, r14
0089735B  E8 70 EA 9C FF                  call 0x140265dd0
00897360  EB 81                           jmp 0x1408972e3
00897362  48 8B CD                        mov rcx, rbp
00897365  E8 66 EA 9C FF                  call 0x140265dd0
0089736A  EB D2                           jmp 0x14089733e
0089736C  33 ED                           xor ebp, ebp
0089736E  E9 52 F8 FF FF                  jmp 0x140896bc5
00897373  48 8B CD                        mov rcx, rbp
00897376  E8 A5 05 15 00                  call 0x1409e7920
0089737B  84 C0                           test al, al
0089737D  0F 85 5F 26 28 00               jne 0x140b199e2
00897383  48 83 7D 60 00                  cmp qword ptr [rbp + 0x60], 0
00897388  0F 84 A4 24 28 00               je 0x140b19832
0089738E  48 8B C3                        mov rax, rbx
00897391  F0 48 0F C1 06                  lock xadd qword ptr [rsi], rax
00897396  24 06                           and al, 6
00897398  3C 02                           cmp al, 2
0089739A  0F 85 2C 24 28 00               jne 0x140b197cc
008973A0  48 8B CE                        mov rcx, rsi
008973A3  E8 28 EA 9C FF                  call 0x140265dd0
008973A8  90                              nop
008973A9  E9 1E 24 28 00                  jmp 0x140b197cc
008973AE  48 8B CF                        mov rcx, rdi
008973B1  E8 DE 5E EB FF                  call 0x14074d294
008973B6  E9 48 FB FF FF                  jmp 0x140896f03
008973BB  8B CE                           mov ecx, esi
008973BD  E8 66 5E EB FF                  call 0x14074d228
008973C2  E9 B4 FB FF FF                  jmp 0x140896f7b
008973C7  48 8B CF                        mov rcx, rdi
008973CA  E8 C5 5E EB FF                  call 0x14074d294
008973CF  E9 58 FA FF FF                  jmp 0x140896e2c
008973D4  8B CE                           mov ecx, esi
008973D6  E8 4D 5E EB FF                  call 0x14074d228
008973DB  E9 C4 FA FF FF                  jmp 0x140896ea4
008973E0  8B C8                           mov ecx, eax
008973E2  E8 41 5E EB FF                  call 0x14074d228
008973E7  E9 49 FD FF FF                  jmp 0x140897135
008973EC  48 8B CD                        mov rcx, rbp
008973EF  E8 18 84 FF FF                  call 0x14088f80c
008973F4  E9 CA FB FF FF                  jmp 0x140896fc3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall AlpcpReceiveMessagePort(__int64 a1, int a2, __int64 a3, __int64 a4, unsigned int a5)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m68;
    unsigned __int8 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int8 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p8;
    unsigned __int8 v_stack_p98;
    unsigned __int64 v_stack_pA0;
    unsigned __int64 v_stack_pA8;

    v_stack_p20 = a4;
    v_stack_p18 = a3;
    v_stack_p10 = (unsigned __int8)(a2);
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (72);
    v_stack_m58 = *(unsigned __int64 *)(gs_base + (0 + 392));
loc_00896B85:
loc_00896B8B:
    v_rbp = 0;
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(*(unsigned __int64 *)(a1) + 352, a2, a3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = *(unsigned __int64 *)(a1) + 352;
        a3 = 0;
        a2 = 0;
        a1 = *(unsigned __int64 *)(a1) + 352;
        result = ExfAcquirePushLockSharedEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
loc_00896BC5:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 416)))) & (64)) != 0) goto loc_008971AC;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 416)))) & (16)) != 0) goto loc_008971B6;
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(*(unsigned __int64 *)(a1) + 136, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = *(unsigned __int64 *)(a1) + 136;
        a2 = result;
        a1 = *(unsigned __int64 *)(a1) + 136;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    result = AlpcpQueryHeadLargeQueue(*(unsigned __int64 *)(a1), a2, a3, a4);
    if (result != 0) goto loc_00897373;
    result = AlpcpQueryHeadMainQueue(*(unsigned __int64 *)(a1), a2, a3, a4);
    if (result != 0) goto loc_00897373;
    result = AlpcpQueryHeadCanceledQueue(*(unsigned __int64 *)(a1), a2, a3, a4);
    if (result != 0) goto loc_00897015;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 360) == 0) goto loc_00896CBD;
    a1 = (unsigned int)((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 360) + 80) + 64)) & (0xFFFFFFULL));
    if (a1 == 0xFFFFFFULL) goto loc_00896CBD;
    result = (unsigned __int8)((-1) & (6));
    if (((unsigned __int8)(result)) == 2) goto loc_008971C0;
loc_00896C82:
    result = KeAbPostRelease(*(unsigned __int64 *)(a1) + 136, a2, a3, a4);
    v_rbp = 0;
loc_00896C91:
    if (0 != 0) goto loc_00897228;
    result = 17;
    if (0 != 0) {
        a1 = *(unsigned __int64 *)(a1) + 352;
        result = ExfReleasePushLockShared(a1, a2, a3, a4);
    }
    result = KeAbPostRelease(*(unsigned __int64 *)(a1) + 352, a2, a3, a4);
    goto loc_00896FD0;
loc_00896CBD:
    result = (unsigned __int8)((-1) & (6));
    if (((unsigned __int8)(result)) == 2) goto loc_008971CD;
loc_00896CCF:
    result = KeAbPostRelease(*(unsigned __int64 *)(a1) + 136, a2, a3, a4);
    if ((*(unsigned __int64 *)((unsigned int)(0x40000030ULL) + 32)) != 0) goto loc_00896CFA;
    if (((*(unsigned int *)((unsigned int)(0x40000030ULL) + 416)) & (512)) == 0) goto loc_00896D03;
    if (((*(unsigned int *)((unsigned int)(0x40000030ULL) + 256)) & (0x1000ULL)) != 0) goto loc_00896DF6;
loc_00896CFA:
    v_rbp = 0;
    goto loc_00896C91;
loc_00896D03:
    if ((*(unsigned __int64 *)((unsigned int)(0xC0000001ULL) + 368)) != 0) goto loc_008972CA;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1444)))) & (32)) != 0) goto loc_00896CFA;
    if (0 == 0) goto loc_00896D8B;
    *(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1472) = (unsigned int)((unsigned int)(a5));
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire((unsigned int)(0xC0000001ULL) + 224, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = (unsigned int)(0xC0000001ULL) + 224;
        a2 = result;
        a1 = (unsigned int)(0xC0000001ULL) + 224;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC0000001ULL) + 232 + 8))) == ((unsigned int)(0xC0000001ULL) + 232)) goto loc_00896EB3;
loc_00896D84:
loc_00896D8B:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC0000001ULL) + 232 + 8))) == ((unsigned int)(0xC0000001ULL) + 232)) goto loc_0089736C;
    v_rbp = 0;
    result = 17;
    if (!(condition_is_equal)) {
        a1 = *(unsigned __int64 *)(a1) + 352;
        result = ExfReleasePushLockShared(a1, a2, a3, a4);
    }
    result = KeAbPostRelease(*(unsigned __int64 *)(a1) + 352, a2, a3, a4);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(*(unsigned __int64 *)(a1) + 352, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = *(unsigned __int64 *)(a1) + 352;
        a2 = result;
        a1 = *(unsigned __int64 *)(a1) + 352;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    if (result == 0) goto loc_00896BC5;
    *(unsigned __int8 *)(result + 10) = 1;
    goto loc_00896BC5;
loc_00896DF6:
    if (1 == 0) goto loc_00897156;
    result = (unsigned __int8)((-1) & (6));
    if (((unsigned __int8)(result)) == 2) goto loc_0089721B;
loc_00896E11:
loc_00896E17:
    result = KeAbPostRelease(*(unsigned __int64 *)(a1) + 352, a2, a3, a4);
    if ((*(unsigned __int8 *)(v_rip + 6094554)) != 0) goto loc_008973C7;
loc_00896E2C:
    result = ((*(unsigned __int8 *)(v_rip + 6094554)) < 0) ? 1 : 0;
    if ((unsigned __int8)(result) != 0) goto loc_00897179;
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, a3, a4);
    v_rsi = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 48))) >> (21));
    v_rsi = (unsigned __int8)((v_rsi) & (1));
    v_stack_m68 = v_stack_p18;
    result = KeWaitForSingleObject(*(unsigned __int64 *)((unsigned int)(0xC0000001ULL) + 248), 16, v_stack_p10, (unsigned __int8)(v_rsi));
    if ((*(unsigned __int8 *)(v_rip + 6094434)) != 0) goto loc_008973D4;
loc_00896EA4:
    if ((unsigned int)((unsigned int)((unsigned int)(result))) == 0) goto loc_00896B8B;
loc_00896EAC:
    goto loc_00896FD0;
loc_00896EB3:
    *(unsigned __int64 *)(17) = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
    *(unsigned __int64 *)(17 + 8) = *(unsigned __int64 *)((unsigned int)(0xC0000001ULL) + 248);
    *(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC0000001ULL) + 248)) = 17;
    *(unsigned __int64 *)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))) + 8) = 17;
    result = (unsigned __int8)((-1) & (6));
    if (((unsigned __int8)(result)) == 2) goto loc_008971DA;
loc_00896ED4:
    result = KeAbPostRelease(*(unsigned __int64 *)((unsigned int)(0xC0000001ULL) + 248), 16, v_stack_p10, (unsigned __int8)(v_rsi));
    result = (unsigned __int8)((-1) & (6));
    if (((unsigned __int8)(result)) == 2) goto loc_008971E7;
loc_00896EEE:
    result = KeAbPostRelease(*(unsigned __int64 *)(a1) + 352, 16, v_stack_p10, (unsigned __int8)(v_rsi));
    if ((*(unsigned __int8 *)(v_rip + 6094339)) != 0) goto loc_008973AE;
loc_00896F03:
    v_r12 = (*(unsigned __int64 *)(gs_base + (0 + 392))) + (0x518ULL);
    result = (condition_is_below) ? 1 : 0;
    if ((unsigned __int8)(result) != 0) goto loc_00896FE2;
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), 16, v_stack_p10, (unsigned __int8)(v_rsi));
    v_rsi = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 48))) >> (21));
    v_rsi = (unsigned __int8)((v_rsi) & (1));
    v_stack_m68 = v_stack_p18;
    result = KeWaitForSingleObject(v_r12, 16, v_stack_p10, (unsigned __int8)(v_rsi));
    if ((*(unsigned __int8 *)(v_rip + 6094219)) != 0) goto loc_008973BB;
loc_00896F7B:
    a2 = 0;
    if ((unsigned int)((unsigned int)((unsigned int)(result))) != 0) goto loc_0089709E;
    *(unsigned __int64 *)(v_stack_m58 + 1472) = 0;
    if (*(unsigned __int64 *)(v_stack_m58 + 1472) == 0) goto loc_00896B85;
loc_00896FA3:
    result = AlpcpLockForCachedReferenceBlob(*(unsigned __int64 *)(v_stack_m58 + 1472), a2, v_stack_p10, (unsigned __int8)(v_rsi));
    if ((*(unsigned __int8 *)(v_rip + 6094147)) != 0) goto loc_008973EC;
loc_00896FC3:
    *(unsigned __int64 *)(v_stack_p20) = *(unsigned __int64 *)(v_stack_m58 + 1472);
    result = 0;
loc_00896FD0:
    v_rsp = (v_rsp) + (72);
    return result;
loc_00896FE2:
    v_stack_p28 = 0;
    v_stack_p20 = v_stack_pA0;
    result = AlpcpSignalAndWait(a1, v_stack_m58, 16, v_stack_p98);
    goto loc_00896F7B;
loc_00897015:
    result = AlpcpTryLockForCachedReferenceBlob(*(unsigned __int64 *)(v_stack_m58 + 1472), v_stack_m58, 16, v_stack_p98);
    if ((unsigned __int8)(result) != 0) goto loc_0089726F;
    result = (unsigned __int8)((-1) & (6));
    if (((unsigned __int8)(result)) == 2) goto loc_008971F4;
loc_00897037:
    result = KeAbPostRelease((unsigned int)((unsigned int)(result)), v_stack_m58, 16, v_stack_p98);
    if (17 == 0) goto loc_00897250;
    result = (unsigned __int8)((-1) & (6));
    if (((unsigned __int8)(result)) == 2) goto loc_00897201;
loc_0089705A:
    v_rbp = 0;
loc_0089705C:
    result = KeAbPostRelease(*(unsigned __int64 *)(a1) + 352, v_stack_m58, 16, v_stack_p98);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(*(unsigned __int64 *)(a1) + 352, a2, a3, v_stack_p98);
    if (!(condition_is_above_or_equal)) {
        a3 = *(unsigned __int64 *)(a1) + 352;
        a2 = result;
        a1 = *(unsigned __int64 *)(a1) + 352;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, v_stack_p98);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    goto loc_00896BC5;
loc_0089709E:
    a3 = 0;
    result = KeAbPreAcquire(0, a2, a3, v_stack_p98);
    if (!(condition_is_above_or_equal)) {
        a3 = 0;
        a2 = result;
        a1 = 0;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, v_stack_p98);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    if (*(unsigned __int64 *)(1) != 0) goto loc_00897301;
    v_rbx = (unsigned __int8)((-1) & (6));
    if (((unsigned __int8)(v_rbx)) == 2) goto loc_0089720E;
loc_008970EA:
    result = KeAbPostRelease(0, a2, a3, v_stack_p98);
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, a3, v_stack_p98);
    v_rbx = 0;
    a4 = 0;
    a3 = 0;
    v_stack_p20 = 0;
    result = KeWaitForSingleObject(v_stack_m58, v_rbx + 16, a3, a4);
    if ((*(unsigned __int8 *)(v_rip + 6093777)) != 0) goto loc_008973E0;
loc_00897135:
    *(unsigned __int64 *)(v_stack_p30 + 1472) = 0;
    if (*(unsigned __int64 *)(v_stack_p30 + 1472) != 0) goto loc_00896FA3;
    goto loc_00896EAC;
loc_00897156:
    a2 = 0;
    if (condition_is_equal) goto loc_00896E17;
    result = ExfReleasePushLockShared(*(unsigned __int64 *)(a1) + 352, a2, a3, a4);
    goto loc_00896E17;
loc_00897179:
    v_stack_p28 = 0;
    v_stack_p20 = v_stack_pA0;
    result = AlpcpSignalAndWait(a1, *(unsigned __int64 *)(v_stack_p30 + 1472), 16, v_stack_p98);
    goto loc_00896EA4;
loc_008971AC:
    goto loc_00896C91;
loc_008971B6:
    goto loc_00896C91;
loc_008971C0:
    result = ExfTryToWakePushLock((unsigned int)((unsigned int)(result)), *(unsigned __int64 *)(v_stack_p30 + 1472), 16, v_stack_p98);
    goto loc_00896C82;
loc_008971CD:
    result = ExfTryToWakePushLock((unsigned int)((unsigned int)(result)), *(unsigned __int64 *)(v_stack_p30 + 1472), 16, v_stack_p98);
    goto loc_00896CCF;
loc_008971DA:
    result = ExfTryToWakePushLock(*(unsigned __int64 *)(v_stack_p30 + 1472), *(unsigned __int64 *)(v_stack_p30 + 1472), 16, v_stack_p98);
    goto loc_00896ED4;
loc_008971E7:
    result = ExfTryToWakePushLock(*(unsigned __int64 *)(a1) + 352, *(unsigned __int64 *)(v_stack_p30 + 1472), 16, v_stack_p98);
    goto loc_00896EEE;
loc_008971F4:
    result = ExfTryToWakePushLock((unsigned int)((unsigned int)(result)), *(unsigned __int64 *)(v_stack_p30 + 1472), 16, v_stack_p98);
    goto loc_00897037;
loc_00897201:
    result = ExfTryToWakePushLock(*(unsigned __int64 *)(a1) + 352, *(unsigned __int64 *)(v_stack_p30 + 1472), 16, v_stack_p98);
    goto loc_0089705A;
loc_0089720E:
    result = ExfTryToWakePushLock(*(unsigned __int64 *)(v_stack_p30 + 1472), *(unsigned __int64 *)(v_stack_p30 + 1472), 16, v_stack_p98);
    goto loc_008970EA;
loc_0089721B:
    result = ExfTryToWakePushLock(*(unsigned __int64 *)(a1) + 352, *(unsigned __int64 *)(v_stack_p30 + 1472), 16, v_stack_p98);
    goto loc_00896E11;
loc_00897228:
    v_rbx = (unsigned __int8)((v_rbx) & (6));
    if (((unsigned __int8)(v_rbx)) != 2) goto loc_00896CAE;
    result = ExfTryToWakePushLock(*(unsigned __int64 *)(a1) + 352, *(unsigned __int64 *)(v_stack_p30 + 1472), 16, v_stack_p98);
    result = KeAbPostRelease(*(unsigned __int64 *)(a1) + 352, *(unsigned __int64 *)(v_stack_p30 + 1472), 16, v_stack_p98);
    goto loc_00896FD0;
loc_00897250:
    v_rbp = 0;
    if (condition_is_equal) goto loc_0089705C;
    result = ExfReleasePushLockShared(*(unsigned __int64 *)(a1) + 352, *(unsigned __int64 *)(v_stack_p30 + 1472), 16, v_stack_p98);
    goto loc_0089705C;
loc_0089726F:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 88)) = *(unsigned __int64 *)(v_rbp + 80);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 80) + 8) = *(unsigned __int64 *)(v_rbp + 88);
    result = (unsigned __int8)((v_rbx) & (6));
    if (((unsigned __int8)(result)) == 2) goto loc_0089734B;
loc_008972A5:
    result = KeAbPostRelease((unsigned int)((unsigned int)(result)), *(unsigned __int64 *)(v_stack_p30 + 1472), 16, v_stack_p98);
    if (17 != 0) goto loc_008972D6;
    a2 = 0;
    if (condition_is_equal) goto loc_008972E3;
    result = ExfReleasePushLockShared(*(unsigned __int64 *)(a1) + 352, a2, 16, v_stack_p98);
    goto loc_008972E3;
loc_008972CA:
    v_rbp = 0;
    goto loc_00896C91;
loc_008972D6:
    v_rbx = (unsigned __int8)((v_rbx) & (6));
    if (((unsigned __int8)(v_rbx)) == 2) goto loc_00897358;
loc_008972E3:
    result = KeAbPostRelease(*(unsigned __int64 *)(a1) + 352, a2, 16, v_stack_p98);
    *(unsigned __int64 *)(v_stack_pA8) = 0;
    result = 0;
    goto loc_00896FD0;
loc_00897301:
    a2 = 0;
    *(unsigned __int64 *)(v_stack_p30 + 1472) = 0;
    if ((*(unsigned __int64 *)(result + 8)) != 17) goto loc_00896D84;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(17 + 8))) != 17) goto loc_00896D84;
    *(unsigned __int64 *)(*(unsigned __int64 *)(17 + 8)) = 0;
    *(unsigned __int64 *)(result + 8) = *(unsigned __int64 *)(17 + 8);
    *(unsigned __int64 *)(17) = 0;
    v_rbx = (unsigned __int8)((v_rbx) & (6));
    if (((unsigned __int8)(v_rbx)) == 2) goto loc_00897362;
loc_0089733E:
    result = KeAbPostRelease(0, a2, 16, v_stack_p98);
    goto loc_00896EAC;
loc_0089734B:
    result = ExfTryToWakePushLock((unsigned int)((unsigned int)(result)), a2, 16, v_stack_p98);
    goto loc_008972A5;
loc_00897358:
    result = ExfTryToWakePushLock(*(unsigned __int64 *)(a1) + 352, a2, 16, v_stack_p98);
    goto loc_008972E3;
loc_00897362:
    result = ExfTryToWakePushLock(0, a2, 16, v_stack_p98);
    goto loc_0089733E;
loc_0089736C:
    v_rbp = 0;
    goto loc_00896BC5;
loc_00897373:
    result = AlpcpTryLockForCachedReferenceBlob(0, a2, 16, v_stack_p98);
    result = (unsigned __int8)((v_rbx) & (6));
    result = ExfTryToWakePushLock((unsigned int)((unsigned int)(result)), a2, 16, v_stack_p98);
loc_008973AE:
    result = AlpcpLogWaitForNewMessage(258, a2, 16, v_stack_p98);
    goto loc_00896F03;
loc_008973BB:
    result = AlpcpLogUnwait((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), a2, 16, v_stack_p98);
    goto loc_00896F7B;
loc_008973C7:
    result = AlpcpLogWaitForNewMessage(258, a2, 16, v_stack_p98);
    goto loc_00896E2C;
loc_008973D4:
    result = AlpcpLogUnwait((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), a2, 16, v_stack_p98);
    goto loc_00896EA4;
loc_008973E0:
    result = AlpcpLogUnwait((unsigned int)((unsigned int)(result)), a2, 16, v_stack_p98);
    goto loc_00897135;
loc_008973EC:
    result = AlpcpLogReceiveMessage(0, a2, 16, v_stack_p98);
    goto loc_00896FC3;
}
```

## 5. (Beta) C Style

```c
int64_t AlpcpReceiveMessagePort(void *Arg1, int32_t Arg2, int64_t Arg3, int64_t Arg4, uint32_t Arg5)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m58;
    uint64_t v_stack_m68;
    uint8_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint8_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p8;
    uint8_t v_stack_p98;
    uint64_t v_stack_pA0;
    uint64_t v_stack_pA8;

    v_stack_p20 = Arg4;
    v_stack_p18 = Arg3;
    v_stack_p10 = (uint8_t)(Arg2);
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (72);
    v_stack_m58 = *(uint64_t *)(gs_base + (0 + 0x188));
loc_00896B85:
loc_00896B8B:
    local_rbp = 0;
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(*(uint64_t *)(arg1) + 352, Arg2, Arg3, Arg4);
    result = 0;
    if (!(condition_is_equal)) {
        Arg4 = *(uint64_t *)(arg1) + 352;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = *(uint64_t *)(arg1) + 352;
        result = ExfAcquirePushLockSharedEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
loc_00896BC5:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x1A0)))) & (64)) != 0) goto loc_008971AC;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x1A0)))) & (16)) != 0) goto loc_008971B6;
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(*(uint64_t *)(arg1) + 136, Arg2, Arg3, Arg4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = *(uint64_t *)(arg1) + 136;
        Arg2 = result;
        Arg1 = *(uint64_t *)(arg1) + 136;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    result = AlpcpQueryHeadLargeQueue(*(uint64_t *)(arg1), Arg2, Arg3, Arg4);
    if (result != 0) goto loc_00897373;
    result = AlpcpQueryHeadMainQueue(*(uint64_t *)(arg1), Arg2, Arg3, Arg4);
    if (result != 0) goto loc_00897373;
    result = AlpcpQueryHeadCanceledQueue(*(uint64_t *)(arg1), Arg2, Arg3, Arg4);
    if (result != 0) goto loc_00897015;
    if (*(uint64_t *)(*(uint64_t *)(arg1) + 0x168) == 0) goto loc_00896CBD;
    Arg1 = (uint32_t)((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x168) + 0x50) + 0x40)) & (0xFFFFFFULL));
    if (Arg1 == 0xFFFFFFULL) goto loc_00896CBD;
    result = (uint8_t)((-1) & (6));
    if (((uint8_t)(result)) == 2) goto loc_008971C0;
loc_00896C82:
    result = KeAbPostRelease(*(uint64_t *)(arg1) + 136, Arg2, Arg3, Arg4);
    local_rbp = 0;
loc_00896C91:
    if (0 != 0) goto loc_00897228;
    result = 17;
    if (0 != 0) {
        Arg1 = *(uint64_t *)(arg1) + 352;
        result = ExfReleasePushLockShared(Arg1, Arg2, Arg3, Arg4);
    }
    result = KeAbPostRelease(*(uint64_t *)(arg1) + 352, Arg2, Arg3, Arg4);
    goto loc_00896FD0;
loc_00896CBD:
    result = (uint8_t)((-1) & (6));
    if (((uint8_t)(result)) == 2) goto loc_008971CD;
loc_00896CCF:
    result = KeAbPostRelease(*(uint64_t *)(arg1) + 136, Arg2, Arg3, Arg4);
    if ((*(uint64_t *)((uint32_t)(0x40000030ULL) + 0x20)) != 0) goto loc_00896CFA;
    if (((*(uint32_t *)((uint32_t)(0x40000030ULL) + 0x1A0)) & (512)) == 0) goto loc_00896D03;
    if (((*(uint32_t *)((uint32_t)(0x40000030ULL) + 0x100)) & (0x1000ULL)) != 0) goto loc_00896DF6;
loc_00896CFA:
    local_rbp = 0;
    goto loc_00896C91;
loc_00896D03:
    if ((*(uint64_t *)((uint32_t)(0xC0000001ULL) + 0x170)) != 0) goto loc_008972CA;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5A4)))) & (32)) != 0) goto loc_00896CFA;
    if (0 == 0) goto loc_00896D8B;
    *(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5C0) = (uint32_t)((uint32_t)(Arg5));
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire((uint32_t)(0xC0000001ULL) + 224, Arg2, Arg3, Arg4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = (uint32_t)(0xC0000001ULL) + 224;
        Arg2 = result;
        Arg1 = (uint32_t)(0xC0000001ULL) + 224;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    if ((*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC0000001ULL) + 0xE8 + 0x8))) == ((uint32_t)(0xC0000001ULL) + 232)) goto loc_00896EB3;
loc_00896D84:
loc_00896D8B:
    if ((*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC0000001ULL) + 0xE8 + 0x8))) == ((uint32_t)(0xC0000001ULL) + 232)) goto loc_0089736C;
    local_rbp = 0;
    result = 17;
    if (!(condition_is_equal)) {
        Arg1 = *(uint64_t *)(arg1) + 352;
        result = ExfReleasePushLockShared(Arg1, Arg2, Arg3, Arg4);
    }
    result = KeAbPostRelease(*(uint64_t *)(arg1) + 352, Arg2, Arg3, Arg4);
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(*(uint64_t *)(arg1) + 352, Arg2, Arg3, Arg4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = *(uint64_t *)(arg1) + 352;
        Arg2 = result;
        Arg1 = *(uint64_t *)(arg1) + 352;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (result == 0) goto loc_00896BC5;
    *(uint8_t *)(result + 0xA) = 1;
    goto loc_00896BC5;
loc_00896DF6:
    if (1 == 0) goto loc_00897156;
    result = (uint8_t)((-1) & (6));
    if (((uint8_t)(result)) == 2) goto loc_0089721B;
loc_00896E11:
loc_00896E17:
    result = KeAbPostRelease(*(uint64_t *)(arg1) + 352, Arg2, Arg3, Arg4);
    if ((*(uint8_t *)(v_rip + 0x5CFEDA)) != 0) goto loc_008973C7;
loc_00896E2C:
    result = ((*(uint8_t *)(v_rip + 0x5CFEDA)) < 0) ? 1 : 0;
    if ((uint8_t)(result) != 0) goto loc_00897179;
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, Arg3, Arg4);
    local_rsi = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x30))) >> (21));
    local_rsi = (uint8_t)((local_rsi) & (1));
    v_stack_m68 = v_stack_p18;
    result = KeWaitForSingleObject(*(uint64_t *)((uint32_t)(0xC0000001ULL) + 0xF8), 16, v_stack_p10, (uint8_t)(local_rsi));
    if ((*(uint8_t *)(v_rip + 0x5CFE62)) != 0) goto loc_008973D4;
loc_00896EA4:
    if ((uint32_t)((uint32_t)((uint32_t)(result))) == 0) goto loc_00896B8B;
loc_00896EAC:
    goto loc_00896FD0;
loc_00896EB3:
    *(uint64_t *)(17) = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
    *(uint64_t *)(17 + 0x8) = *(uint64_t *)((uint32_t)(0xC0000001ULL) + 0xF8);
    *(uint64_t *)(*(uint64_t *)((uint32_t)(0xC0000001ULL) + 0xF8)) = 17;
    *(uint64_t *)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))) + 0x8) = 17;
    result = (uint8_t)((-1) & (6));
    if (((uint8_t)(result)) == 2) goto loc_008971DA;
loc_00896ED4:
    result = KeAbPostRelease(*(uint64_t *)((uint32_t)(0xC0000001ULL) + 0xF8), 16, v_stack_p10, (uint8_t)(local_rsi));
    result = (uint8_t)((-1) & (6));
    if (((uint8_t)(result)) == 2) goto loc_008971E7;
loc_00896EEE:
    result = KeAbPostRelease(*(uint64_t *)(arg1) + 352, 16, v_stack_p10, (uint8_t)(local_rsi));
    if ((*(uint8_t *)(v_rip + 0x5CFE03)) != 0) goto loc_008973AE;
loc_00896F03:
    local_r12 = (*(uint64_t *)(gs_base + (0 + 0x188))) + (0x518ULL);
    result = (condition_is_below) ? 1 : 0;
    if ((uint8_t)(result) != 0) goto loc_00896FE2;
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), 16, v_stack_p10, (uint8_t)(local_rsi));
    local_rsi = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x30))) >> (21));
    local_rsi = (uint8_t)((local_rsi) & (1));
    v_stack_m68 = v_stack_p18;
    result = KeWaitForSingleObject(local_r12, 16, v_stack_p10, (uint8_t)(local_rsi));
    if ((*(uint8_t *)(v_rip + 0x5CFD8B)) != 0) goto loc_008973BB;
loc_00896F7B:
    Arg2 = 0;
    if ((uint32_t)((uint32_t)((uint32_t)(result))) != 0) goto loc_0089709E;
    *(uint64_t *)(v_stack_m58 + 0x5C0) = 0;
    if (*(uint64_t *)(v_stack_m58 + 0x5C0) == 0) goto loc_00896B85;
loc_00896FA3:
    result = AlpcpLockForCachedReferenceBlob(*(uint64_t *)(v_stack_m58 + 0x5C0), Arg2, v_stack_p10, (uint8_t)(local_rsi));
    if ((*(uint8_t *)(v_rip + 0x5CFD43)) != 0) goto loc_008973EC;
loc_00896FC3:
    *(uint64_t *)(v_stack_p20) = *(uint64_t *)(v_stack_m58 + 0x5C0);
    result = 0;
loc_00896FD0:
    local_rsp = (local_rsp) + (72);
    return result;
loc_00896FE2:
    v_stack_p28 = 0;
    v_stack_p20 = v_stack_pA0;
    result = AlpcpSignalAndWait(Arg1, v_stack_m58, 16, v_stack_p98);
    goto loc_00896F7B;
loc_00897015:
    result = AlpcpTryLockForCachedReferenceBlob(*(uint64_t *)(v_stack_m58 + 0x5C0), v_stack_m58, 16, v_stack_p98);
    if ((uint8_t)(result) != 0) goto loc_0089726F;
    result = (uint8_t)((-1) & (6));
    if (((uint8_t)(result)) == 2) goto loc_008971F4;
loc_00897037:
    result = KeAbPostRelease((uint32_t)((uint32_t)(result)), v_stack_m58, 16, v_stack_p98);
    if (17 == 0) goto loc_00897250;
    result = (uint8_t)((-1) & (6));
    if (((uint8_t)(result)) == 2) goto loc_00897201;
loc_0089705A:
    local_rbp = 0;
loc_0089705C:
    result = KeAbPostRelease(*(uint64_t *)(arg1) + 352, v_stack_m58, 16, v_stack_p98);
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(*(uint64_t *)(arg1) + 352, Arg2, Arg3, v_stack_p98);
    if (!(condition_is_above_or_equal)) {
        Arg3 = *(uint64_t *)(arg1) + 352;
        Arg2 = result;
        Arg1 = *(uint64_t *)(arg1) + 352;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, v_stack_p98);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    goto loc_00896BC5;
loc_0089709E:
    Arg3 = 0;
    result = KeAbPreAcquire(0, Arg2, Arg3, v_stack_p98);
    if (!(condition_is_above_or_equal)) {
        Arg3 = 0;
        Arg2 = result;
        Arg1 = 0;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, v_stack_p98);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    if (*(uint64_t *)(1) != 0) goto loc_00897301;
    local_rbx = (uint8_t)((-1) & (6));
    if (((uint8_t)(local_rbx)) == 2) goto loc_0089720E;
loc_008970EA:
    result = KeAbPostRelease(0, Arg2, Arg3, v_stack_p98);
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, Arg3, v_stack_p98);
    local_rbx = 0;
    Arg4 = 0;
    Arg3 = 0;
    v_stack_p20 = 0;
    result = KeWaitForSingleObject(v_stack_m58, local_rbx + 16, Arg3, Arg4);
    if ((*(uint8_t *)(v_rip + 0x5CFBD1)) != 0) goto loc_008973E0;
loc_00897135:
    *(uint64_t *)(v_stack_p30 + 0x5C0) = 0;
    if (*(uint64_t *)(v_stack_p30 + 0x5C0) != 0) goto loc_00896FA3;
    goto loc_00896EAC;
loc_00897156:
    Arg2 = 0;
    if (condition_is_equal) goto loc_00896E17;
    result = ExfReleasePushLockShared(*(uint64_t *)(arg1) + 352, Arg2, Arg3, Arg4);
    goto loc_00896E17;
loc_00897179:
    v_stack_p28 = 0;
    v_stack_p20 = v_stack_pA0;
    result = AlpcpSignalAndWait(Arg1, *(uint64_t *)(v_stack_p30 + 0x5C0), 16, v_stack_p98);
    goto loc_00896EA4;
loc_008971AC:
    goto loc_00896C91;
loc_008971B6:
    goto loc_00896C91;
loc_008971C0:
    result = ExfTryToWakePushLock((uint32_t)((uint32_t)(result)), *(uint64_t *)(v_stack_p30 + 0x5C0), 16, v_stack_p98);
    goto loc_00896C82;
loc_008971CD:
    result = ExfTryToWakePushLock((uint32_t)((uint32_t)(result)), *(uint64_t *)(v_stack_p30 + 0x5C0), 16, v_stack_p98);
    goto loc_00896CCF;
loc_008971DA:
    result = ExfTryToWakePushLock(*(uint64_t *)(v_stack_p30 + 0x5C0), *(uint64_t *)(v_stack_p30 + 0x5C0), 16, v_stack_p98);
    goto loc_00896ED4;
loc_008971E7:
    result = ExfTryToWakePushLock(*(uint64_t *)(arg1) + 352, *(uint64_t *)(v_stack_p30 + 0x5C0), 16, v_stack_p98);
    goto loc_00896EEE;
loc_008971F4:
    result = ExfTryToWakePushLock((uint32_t)((uint32_t)(result)), *(uint64_t *)(v_stack_p30 + 0x5C0), 16, v_stack_p98);
    goto loc_00897037;
loc_00897201:
    result = ExfTryToWakePushLock(*(uint64_t *)(arg1) + 352, *(uint64_t *)(v_stack_p30 + 0x5C0), 16, v_stack_p98);
    goto loc_0089705A;
loc_0089720E:
    result = ExfTryToWakePushLock(*(uint64_t *)(v_stack_p30 + 0x5C0), *(uint64_t *)(v_stack_p30 + 0x5C0), 16, v_stack_p98);
    goto loc_008970EA;
loc_0089721B:
    result = ExfTryToWakePushLock(*(uint64_t *)(arg1) + 352, *(uint64_t *)(v_stack_p30 + 0x5C0), 16, v_stack_p98);
    goto loc_00896E11;
loc_00897228:
    local_rbx = (uint8_t)((local_rbx) & (6));
    if (((uint8_t)(local_rbx)) != 2) goto loc_00896CAE;
    result = ExfTryToWakePushLock(*(uint64_t *)(arg1) + 352, *(uint64_t *)(v_stack_p30 + 0x5C0), 16, v_stack_p98);
    result = KeAbPostRelease(*(uint64_t *)(arg1) + 352, *(uint64_t *)(v_stack_p30 + 0x5C0), 16, v_stack_p98);
    goto loc_00896FD0;
loc_00897250:
    local_rbp = 0;
    if (condition_is_equal) goto loc_0089705C;
    result = ExfReleasePushLockShared(*(uint64_t *)(arg1) + 352, *(uint64_t *)(v_stack_p30 + 0x5C0), 16, v_stack_p98);
    goto loc_0089705C;
loc_0089726F:
    *(uint64_t *)(*(uint64_t *)(local_rbp + 0x58)) = *(uint64_t *)(local_rbp + 0x50);
    *(uint64_t *)(*(uint64_t *)(local_rbp + 0x50) + 0x8) = *(uint64_t *)(local_rbp + 0x58);
    result = (uint8_t)((local_rbx) & (6));
    if (((uint8_t)(result)) == 2) goto loc_0089734B;
loc_008972A5:
    result = KeAbPostRelease((uint32_t)((uint32_t)(result)), *(uint64_t *)(v_stack_p30 + 0x5C0), 16, v_stack_p98);
    if (17 != 0) goto loc_008972D6;
    Arg2 = 0;
    if (condition_is_equal) goto loc_008972E3;
    result = ExfReleasePushLockShared(*(uint64_t *)(arg1) + 352, Arg2, 16, v_stack_p98);
    goto loc_008972E3;
loc_008972CA:
    local_rbp = 0;
    goto loc_00896C91;
loc_008972D6:
    local_rbx = (uint8_t)((local_rbx) & (6));
    if (((uint8_t)(local_rbx)) == 2) goto loc_00897358;
loc_008972E3:
    result = KeAbPostRelease(*(uint64_t *)(arg1) + 352, Arg2, 16, v_stack_p98);
    *(uint64_t *)(v_stack_pA8) = 0;
    result = 0;
    goto loc_00896FD0;
loc_00897301:
    Arg2 = 0;
    *(uint64_t *)(v_stack_p30 + 0x5C0) = 0;
    if ((*(uint64_t *)(result + 0x8)) != 17) goto loc_00896D84;
    if ((*(uint64_t *)(*(uint64_t *)(17 + 0x8))) != 17) goto loc_00896D84;
    *(uint64_t *)(*(uint64_t *)(17 + 0x8)) = 0;
    *(uint64_t *)(result + 0x8) = *(uint64_t *)(17 + 0x8);
    *(uint64_t *)(17) = 0;
    local_rbx = (uint8_t)((local_rbx) & (6));
    if (((uint8_t)(local_rbx)) == 2) goto loc_00897362;
loc_0089733E:
    result = KeAbPostRelease(0, Arg2, 16, v_stack_p98);
    goto loc_00896EAC;
loc_0089734B:
    result = ExfTryToWakePushLock((uint32_t)((uint32_t)(result)), Arg2, 16, v_stack_p98);
    goto loc_008972A5;
loc_00897358:
    result = ExfTryToWakePushLock(*(uint64_t *)(arg1) + 352, Arg2, 16, v_stack_p98);
    goto loc_008972E3;
loc_00897362:
    result = ExfTryToWakePushLock(0, Arg2, 16, v_stack_p98);
    goto loc_0089733E;
loc_0089736C:
    local_rbp = 0;
    goto loc_00896BC5;
loc_00897373:
    result = AlpcpTryLockForCachedReferenceBlob(0, Arg2, 16, v_stack_p98);
    result = (uint8_t)((local_rbx) & (6));
    result = ExfTryToWakePushLock((uint32_t)((uint32_t)(result)), Arg2, 16, v_stack_p98);
loc_008973AE:
    result = AlpcpLogWaitForNewMessage(258, Arg2, 16, v_stack_p98);
    goto loc_00896F03;
loc_008973BB:
    result = AlpcpLogUnwait((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), Arg2, 16, v_stack_p98);
    goto loc_00896F7B;
loc_008973C7:
    result = AlpcpLogWaitForNewMessage(258, Arg2, 16, v_stack_p98);
    goto loc_00896E2C;
loc_008973D4:
    result = AlpcpLogUnwait((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), Arg2, 16, v_stack_p98);
    goto loc_00896EA4;
loc_008973E0:
    result = AlpcpLogUnwait((uint32_t)((uint32_t)(result)), Arg2, 16, v_stack_p98);
    goto loc_00897135;
loc_008973EC:
    result = AlpcpLogReceiveMessage(0, Arg2, 16, v_stack_p98);
    goto loc_00896FC3;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x30` | `32` | `R` |
| `Arg1` | `+ 0x30` | `32` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00896B40&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
