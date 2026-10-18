# AlpcpFlushMessagesPort

- RVA: `0x00925554`–`0x00925D17` (길이 `1,987` bytes)
- VA: `0x0000000140925554`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008D490`
- 디코드: `511`개 명령, `1,987/1,987` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **83**; 고유 호출 대상: **14**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00925589` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x009255A2` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x009255E0` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x009255F4` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0092560D` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x0092563E` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00925659` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00925672` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x009256A3` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x009256BE` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x009256D7` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x00925708` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00925712` → [AlpcpFlushCancelQueue](../A2/AlpcpFlushCancelQueue_function_00A270CC.md) (function, `0x00A270CC`)
- `0x00925739` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00925759` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)
- `0x00925776` → [ObReferenceObjectSafe](../../text/41/ObReferenceObjectSafe_function_0041DAE0.md) (function, `0x0041DAE0`)
- `0x00925799` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x009257A1` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x009257C1` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x009257CE` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x009257F4` → [AlpcpReferenceBlob](../89/AlpcpReferenceBlob_function_00890110.md) (function, `0x00890110`)
- `0x00925810` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00925818` → [AlpcpLockForCachedReferenceBlob](../88/AlpcpLockForCachedReferenceBlob_function_0088A8B0.md) (function, `0x0088A8B0`)
- `0x00925837` → [AlpcpCancelMessage](../89/AlpcpCancelMessage_function_00894120.md) (function, `0x00894120`)
- `0x00925844` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0092585D` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x00925877` → [AlpcpReferenceBlob](../89/AlpcpReferenceBlob_function_00890110.md) (function, `0x00890110`)
- `0x00925893` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0092589B` → [AlpcpLockForCachedReferenceBlob](../88/AlpcpLockForCachedReferenceBlob_function_0088A8B0.md) (function, `0x0088A8B0`)
- `0x009258BA` → [AlpcpCancelMessage](../89/AlpcpCancelMessage_function_00894120.md) (function, `0x00894120`)
- `0x009258C7` → [AlpcpReferenceBlob](../89/AlpcpReferenceBlob_function_00890110.md) (function, `0x00890110`)
- `0x009258E3` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x009258EB` → [AlpcpLockForCachedReferenceBlob](../88/AlpcpLockForCachedReferenceBlob_function_0088A8B0.md) (function, `0x0088A8B0`)
- `0x0092590A` → [AlpcpCancelMessage](../89/AlpcpCancelMessage_function_00894120.md) (function, `0x00894120`)
- `0x00925917` → [AlpcpReferenceBlob](../89/AlpcpReferenceBlob_function_00890110.md) (function, `0x00890110`)
- `0x00925933` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0092593B` → [AlpcpLockForCachedReferenceBlob](../88/AlpcpLockForCachedReferenceBlob_function_0088A8B0.md) (function, `0x0088A8B0`)
- `0x0092595A` → [AlpcpCancelMessage](../89/AlpcpCancelMessage_function_00894120.md) (function, `0x00894120`)
- `0x00925967` → [ObReferenceObjectSafe](../../text/41/ObReferenceObjectSafe_function_0041DAE0.md) (function, `0x0041DAE0`)
- `0x0092599B` → [AlpcpFlushMessagesByRequestor](../A3/AlpcpFlushMessagesByRequestor_function_00A352F0.md) (function, `0x00A352F0`)
- `0x009259B6` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x009259CF` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x00925A16` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00925A3C` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00925A55` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x00925A9C` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00925AB7` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00925AD0` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x00925B16` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00925B21` → [AlpcpFlushCancelQueue](../A2/AlpcpFlushCancelQueue_function_00A270CC.md) (function, `0x00A270CC`)
- `0x00925B2E` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x00925B3B` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x00925B48` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x00925B55` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x00925B62` → [AlpcpUnlockMessage](../89/AlpcpUnlockMessage_function_00897AE0.md) (function, `0x00897AE0`)
- `0x00925B6F` → [AlpcpUnlockMessage](../89/AlpcpUnlockMessage_function_00897AE0.md) (function, `0x00897AE0`)
- `0x00925B7C` → [AlpcpUnlockMessage](../89/AlpcpUnlockMessage_function_00897AE0.md) (function, `0x00897AE0`)
- `0x00925B89` → [AlpcpUnlockMessage](../89/AlpcpUnlockMessage_function_00897AE0.md) (function, `0x00897AE0`)
- `0x00925B96` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x00925BA3` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x00925BB0` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x00925BBD` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x00925BCA` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x00925BD7` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x00925BE4` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x00925BF1` → [AlpcpReferenceBlob](../89/AlpcpReferenceBlob_function_00890110.md) (function, `0x00890110`)
- `0x00925C0B` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00925C13` → [AlpcpLockForCachedReferenceBlob](../88/AlpcpLockForCachedReferenceBlob_function_0088A8B0.md) (function, `0x0088A8B0`)
- `0x00925C32` → [AlpcpCancelMessage](../89/AlpcpCancelMessage_function_00894120.md) (function, `0x00894120`)
- `0x00925C3F` → [AlpcpReferenceBlob](../89/AlpcpReferenceBlob_function_00890110.md) (function, `0x00890110`)
- `0x00925C59` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00925C61` → [AlpcpLockForCachedReferenceBlob](../88/AlpcpLockForCachedReferenceBlob_function_0088A8B0.md) (function, `0x0088A8B0`)
- `0x00925C7C` → [AlpcpCancelMessage](../89/AlpcpCancelMessage_function_00894120.md) (function, `0x00894120`)
- `0x00925C89` → [AlpcpReferenceBlob](../89/AlpcpReferenceBlob_function_00890110.md) (function, `0x00890110`)
- `0x00925C9F` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00925CA7` → [AlpcpLockForCachedReferenceBlob](../88/AlpcpLockForCachedReferenceBlob_function_0088A8B0.md) (function, `0x0088A8B0`)
- `0x00925CC2` → [AlpcpCancelMessage](../89/AlpcpCancelMessage_function_00894120.md) (function, `0x00894120`)
- `0x00925CCF` → [AlpcpUnlockMessage](../89/AlpcpUnlockMessage_function_00897AE0.md) (function, `0x00897AE0`)
- `0x00925CDC` → [AlpcpUnlockMessage](../89/AlpcpUnlockMessage_function_00897AE0.md) (function, `0x00897AE0`)
- `0x00925CE9` → [AlpcpUnlockMessage](../89/AlpcpUnlockMessage_function_00897AE0.md) (function, `0x00897AE0`)
- `0x00925CF6` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x00925D03` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x00925D10` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)

### Direct callers
- [AlpcpDoPortCleanup](AlpcpDoPortCleanup_function_00924E54.md) at `0x00924F07`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **52**
  - `0x00925589` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x009255A2` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x009255E0` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x009255F4` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x0092560D` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x0092563E` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x00925659` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x00925672` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x009256A3` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x009256BE` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x009256D7` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x00925708` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x00925739` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x00925759` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (`PAGE` → `.text`)
  - `0x00925776` → [ObReferenceObjectSafe](../../text/41/ObReferenceObjectSafe_function_0041DAE0.md) (`PAGE` → `.text`)
  - `0x00925799` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x009257A1` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x009257C1` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x009257CE` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00925810` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x00925844` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x0092585D` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x00925893` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x009258E3` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x00925933` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x00925967` → [ObReferenceObjectSafe](../../text/41/ObReferenceObjectSafe_function_0041DAE0.md) (`PAGE` → `.text`)
  - `0x009259B6` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x009259CF` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x00925A16` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x00925A3C` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x00925A55` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x00925A9C` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x00925AB7` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x00925AD0` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x00925B16` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x00925B2E` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x00925B3B` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x00925B48` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x00925B55` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x00925B96` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x00925BA3` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x00925BB0` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x00925BBD` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x00925BCA` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x00925BD7` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x00925BE4` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x00925C0B` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x00925C59` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x00925C9F` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x00925CF6` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x00925D03` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x00925D10` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00925554  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
00925559  48 89 6C 24 18                  mov qword ptr [rsp + 0x18], rbp
0092555E  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
00925563  57                              push rdi
00925564  41 54                           push r12
00925566  41 55                           push r13
00925568  41 56                           push r14
0092556A  41 57                           push r15
0092556C  48 83 EC 20                     sub rsp, 0x20
00925570  48 8D B9 88 00 00 00            lea rdi, [rcx + 0x88]
00925577  4C 8B E9                        mov r13, rcx
0092557A  4C 8D B1 90 00 00 00            lea r14, [rcx + 0x90]
00925581  45 33 C0                        xor r8d, r8d
00925584  48 8B CF                        mov rcx, rdi
00925587  33 D2                           xor edx, edx
00925589  E8 A2 AC 8E FF                  call 0x140210230
0092558E  F0 48 0F BA 2F 00               lock bts qword ptr [rdi], 0
00925594  48 8B D8                        mov rbx, rax
00925597  73 0E                           jae 0x1409255a7
00925599  4C 8B C7                        mov r8, rdi
0092559C  48 8B D0                        mov rdx, rax
0092559F  48 8B CF                        mov rcx, rdi
009255A2  E8 E9 A6 8E FF                  call 0x14020fc90
009255A7  45 33 E4                        xor r12d, r12d
009255AA  48 85 DB                        test rbx, rbx
009255AD  74 04                           je 0x1409255b3
009255AF  C6 43 0A 01                     mov byte ptr [rbx + 0xa], 1
009255B3  48 83 CB FF                     or rbx, 0xffffffffffffffff
009255B7  41 B7 02                        mov r15b, 2
009255BA  8D 6B 07                        lea ebp, [rbx + 7]
009255BD  49 8B 36                        mov rsi, qword ptr [r14]
009255C0  49 3B F6                        cmp rsi, r14
009255C3  0F 85 28 02 00 00               jne 0x1409257f1
009255C9  48 8B C3                        mov rax, rbx
009255CC  F0 48 0F C1 07                  lock xadd qword ptr [rdi], rax
009255D1  40 22 C5                        and al, bpl
009255D4  41 3A C7                        cmp al, r15b
009255D7  0F 84 4E 05 00 00               je 0x140925b2b
009255DD  48 8B CF                        mov rcx, rdi
009255E0  E8 1B C0 9B FF                  call 0x1402e1600
009255E5  4D 8D B5 A0 00 00 00            lea r14, [r13 + 0xa0]
009255EC  45 33 C0                        xor r8d, r8d
009255EF  33 D2                           xor edx, edx
009255F1  48 8B CF                        mov rcx, rdi
009255F4  E8 37 AC 8E FF                  call 0x140210230
009255F9  F0 48 0F BA 2F 00               lock bts qword ptr [rdi], 0
009255FF  48 8B F0                        mov rsi, rax
00925602  73 0E                           jae 0x140925612
00925604  4C 8B C7                        mov r8, rdi
00925607  48 8B D0                        mov rdx, rax
0092560A  48 8B CF                        mov rcx, rdi
0092560D  E8 7E A6 8E FF                  call 0x14020fc90
00925612  48 85 F6                        test rsi, rsi
00925615  74 04                           je 0x14092561b
00925617  C6 46 0A 01                     mov byte ptr [rsi + 0xa], 1
0092561B  49 8B 36                        mov rsi, qword ptr [r14]
0092561E  49 3B F6                        cmp rsi, r14
00925621  0F 85 4D 02 00 00               jne 0x140925874
00925627  48 8B C3                        mov rax, rbx
0092562A  F0 48 0F C1 07                  lock xadd qword ptr [rdi], rax
0092562F  40 22 C5                        and al, bpl
00925632  41 3A C7                        cmp al, r15b
00925635  0F 84 FD 04 00 00               je 0x140925b38
0092563B  48 8B CF                        mov rcx, rdi
0092563E  E8 BD BF 9B FF                  call 0x1402e1600
00925643  4D 8D B5 B8 00 00 00            lea r14, [r13 + 0xb8]
0092564A  49 8D BD B0 00 00 00            lea rdi, [r13 + 0xb0]
00925651  45 33 C0                        xor r8d, r8d
00925654  33 D2                           xor edx, edx
00925656  48 8B CF                        mov rcx, rdi
00925659  E8 D2 AB 8E FF                  call 0x140210230
0092565E  F0 48 0F BA 2F 00               lock bts qword ptr [rdi], 0
00925664  48 8B F0                        mov rsi, rax
00925667  73 0E                           jae 0x140925677
00925669  4C 8B C7                        mov r8, rdi
0092566C  48 8B D0                        mov rdx, rax
0092566F  48 8B CF                        mov rcx, rdi
00925672  E8 19 A6 8E FF                  call 0x14020fc90
00925677  48 85 F6                        test rsi, rsi
0092567A  74 04                           je 0x140925680
0092567C  C6 46 0A 01                     mov byte ptr [rsi + 0xa], 1
00925680  49 8B 36                        mov rsi, qword ptr [r14]
00925683  49 3B F6                        cmp rsi, r14
00925686  0F 85 38 02 00 00               jne 0x1409258c4
0092568C  48 8B C3                        mov rax, rbx
0092568F  F0 48 0F C1 07                  lock xadd qword ptr [rdi], rax
00925694  40 22 C5                        and al, bpl
00925697  41 3A C7                        cmp al, r15b
0092569A  0F 84 B2 04 00 00               je 0x140925b52
009256A0  48 8B CF                        mov rcx, rdi
009256A3  E8 58 BF 9B FF                  call 0x1402e1600
009256A8  4D 8D B5 D0 00 00 00            lea r14, [r13 + 0xd0]
009256AF  49 8D BD C8 00 00 00            lea rdi, [r13 + 0xc8]
009256B6  45 33 C0                        xor r8d, r8d
009256B9  33 D2                           xor edx, edx
009256BB  48 8B CF                        mov rcx, rdi
009256BE  E8 6D AB 8E FF                  call 0x140210230
009256C3  F0 48 0F BA 2F 00               lock bts qword ptr [rdi], 0
009256C9  48 8B F0                        mov rsi, rax
009256CC  73 0E                           jae 0x1409256dc
009256CE  4C 8B C7                        mov r8, rdi
009256D1  48 8B D0                        mov rdx, rax
009256D4  48 8B CF                        mov rcx, rdi
009256D7  E8 B4 A5 8E FF                  call 0x14020fc90
009256DC  48 85 F6                        test rsi, rsi
009256DF  74 04                           je 0x1409256e5
009256E1  C6 46 0A 01                     mov byte ptr [rsi + 0xa], 1
009256E5  49 8B 36                        mov rsi, qword ptr [r14]
009256E8  49 3B F6                        cmp rsi, r14
009256EB  0F 85 23 02 00 00               jne 0x140925914
009256F1  48 8B C3                        mov rax, rbx
009256F4  F0 48 0F C1 07                  lock xadd qword ptr [rdi], rax
009256F9  40 22 C5                        and al, bpl
009256FC  41 3A C7                        cmp al, r15b
009256FF  0F 84 40 04 00 00               je 0x140925b45
00925705  48 8B CF                        mov rcx, rdi
00925708  E8 F3 BE 9B FF                  call 0x1402e1600
0092570D  33 D2                           xor edx, edx
0092570F  49 8B CD                        mov rcx, r13
00925712  E8 B5 19 10 00                  call 0x140a270cc
00925717  41 8B 85 A0 01 00 00            mov eax, dword ptr [r13 + 0x1a0]
0092571E  23 C5                           and eax, ebp
00925720  40 3A C5                        cmp al, bpl
00925723  0F 85 AA 00 00 00               jne 0x1409257d3
00925729  4D 8B 75 10                     mov r14, qword ptr [r13 + 0x10]
0092572D  45 33 C0                        xor r8d, r8d
00925730  33 D2                           xor edx, edx
00925732  49 8D 7E F0                     lea rdi, [r14 - 0x10]
00925736  48 8B CF                        mov rcx, rdi
00925739  E8 F2 AA 8E FF                  call 0x140210230
0092573E  48 8B F0                        mov rsi, rax
00925741  33 C0                           xor eax, eax
00925743  44 8D 78 11                     lea r15d, [rax + 0x11]
00925747  F0 4C 0F B1 3F                  lock cmpxchg qword ptr [rdi], r15
0092574C  74 10                           je 0x14092575e
0092574E  4C 8B CF                        mov r9, rdi
00925751  4C 8B C6                        mov r8, rsi
00925754  33 D2                           xor edx, edx
00925756  48 8B CF                        mov rcx, rdi
00925759  E8 EE AC 8E FF                  call 0x14021044c
0092575E  48 85 F6                        test rsi, rsi
00925761  74 04                           je 0x140925767
00925763  C6 46 0A 01                     mov byte ptr [rsi + 0xa], 1
00925767  49 8B 2E                        mov rbp, qword ptr [r14]
0092576A  4D 8B 76 10                     mov r14, qword ptr [r14 + 0x10]
0092576E  48 85 ED                        test rbp, rbp
00925771  74 10                           je 0x140925783
00925773  48 8B CD                        mov rcx, rbp
00925776  E8 65 83 AF FF                  call 0x14041dae0
0092577B  F6 D8                           neg al
0092577D  48 1B C9                        sbb rcx, rcx
00925780  48 23 E9                        and rbp, rcx
00925783  4D 85 F6                        test r14, r14
00925786  0F 85 D8 01 00 00               jne 0x140925964
0092578C  49 8B C7                        mov rax, r15
0092578F  F0 4C 0F B1 27                  lock cmpxchg qword ptr [rdi], r12
00925794  74 08                           je 0x14092579e
00925796  48 8B CF                        mov rcx, rdi
00925799  E8 A2 DC 93 FF                  call 0x140263440
0092579E  48 8B CF                        mov rcx, rdi
009257A1  E8 5A BE 9B FF                  call 0x1402e1600
009257A6  48 85 ED                        test rbp, rbp
009257A9  74 1B                           je 0x1409257c6
009257AB  8B 85 A0 01 00 00               mov eax, dword ptr [rbp + 0x1a0]
009257B1  A8 40                           test al, 0x40
009257B3  75 09                           jne 0x1409257be
009257B5  4D 85 F6                        test r14, r14
009257B8  0F 85 BB 01 00 00               jne 0x140925979
009257BE  48 8B CD                        mov rcx, rbp
009257C1  E8 8A 3B 9D FF                  call 0x1402f9350
009257C6  4D 85 F6                        test r14, r14
009257C9  74 08                           je 0x1409257d3
009257CB  49 8B CE                        mov rcx, r14
009257CE  E8 7D 3B 9D FF                  call 0x1402f9350
009257D3  48 8B 5C 24 58                  mov rbx, qword ptr [rsp + 0x58]
009257D8  48 8B 6C 24 60                  mov rbp, qword ptr [rsp + 0x60]
009257DD  48 8B 74 24 68                  mov rsi, qword ptr [rsp + 0x68]
009257E2  48 83 C4 20                     add rsp, 0x20
009257E6  41 5F                           pop r15
009257E8  41 5E                           pop r14
009257EA  41 5D                           pop r13
009257EC  41 5C                           pop r12
009257EE  5F                              pop rdi
009257EF  C3                              ret
009257F0  CC                              int3
009257F1  48 8B CE                        mov rcx, rsi
009257F4  E8 17 A9 F6 FF                  call 0x140890110
009257F9  48 8B C3                        mov rax, rbx
009257FC  F0 48 0F C1 07                  lock xadd qword ptr [rdi], rax
00925801  40 22 C5                        and al, bpl
00925804  41 3A C7                        cmp al, r15b
00925807  0F 84 86 03 00 00               je 0x140925b93
0092580D  48 8B CF                        mov rcx, rdi
00925810  E8 EB BD 9B FF                  call 0x1402e1600
00925815  48 8B CE                        mov rcx, rsi
00925818  E8 93 50 F6 FF                  call 0x14088a8b0
0092581D  66 01 5E E2                     add word ptr [rsi - 0x1e], bx
00925821  4C 39 6E 10                     cmp qword ptr [rsi + 0x10], r13
00925825  0F 85 34 03 00 00               jne 0x140925b5f
0092582B  41 B8 00 00 01 00               mov r8d, 0x10000
00925831  48 8B D6                        mov rdx, rsi
00925834  49 8B CD                        mov rcx, r13
00925837  E8 E4 E8 F6 FF                  call 0x140894120
0092583C  45 33 C0                        xor r8d, r8d
0092583F  33 D2                           xor edx, edx
00925841  48 8B CF                        mov rcx, rdi
00925844  E8 E7 A9 8E FF                  call 0x140210230
00925849  F0 48 0F BA 2F 00               lock bts qword ptr [rdi], 0
0092584F  48 8B F0                        mov rsi, rax
00925852  73 0E                           jae 0x140925862
00925854  4C 8B C7                        mov r8, rdi
00925857  48 8B D0                        mov rdx, rax
0092585A  48 8B CF                        mov rcx, rdi
0092585D  E8 2E A4 8E FF                  call 0x14020fc90
00925862  48 85 F6                        test rsi, rsi
00925865  0F 84 52 FD FF FF               je 0x1409255bd
0092586B  C6 46 0A 01                     mov byte ptr [rsi + 0xa], 1
0092586F  E9 49 FD FF FF                  jmp 0x1409255bd
00925874  48 8B CE                        mov rcx, rsi
00925877  E8 94 A8 F6 FF                  call 0x140890110
0092587C  48 8B C3                        mov rax, rbx
0092587F  F0 48 0F C1 07                  lock xadd qword ptr [rdi], rax
00925884  40 22 C5                        and al, bpl
00925887  41 3A C7                        cmp al, r15b
0092588A  0F 84 10 03 00 00               je 0x140925ba0
00925890  48 8B CF                        mov rcx, rdi
00925893  E8 68 BD 9B FF                  call 0x1402e1600
00925898  48 8B CE                        mov rcx, rsi
0092589B  E8 10 50 F6 FF                  call 0x14088a8b0
009258A0  66 01 5E E2                     add word ptr [rsi - 0x1e], bx
009258A4  4C 39 6E 10                     cmp qword ptr [rsi + 0x10], r13
009258A8  0F 85 BE 02 00 00               jne 0x140925b6c
009258AE  41 B8 00 00 01 00               mov r8d, 0x10000
009258B4  48 8B D6                        mov rdx, rsi
009258B7  49 8B CD                        mov rcx, r13
009258BA  E8 61 E8 F6 FF                  call 0x140894120
009258BF  E9 28 FD FF FF                  jmp 0x1409255ec
009258C4  48 8B CE                        mov rcx, rsi
009258C7  E8 44 A8 F6 FF                  call 0x140890110
009258CC  48 8B C3                        mov rax, rbx
009258CF  F0 48 0F C1 07                  lock xadd qword ptr [rdi], rax
009258D4  40 22 C5                        and al, bpl
009258D7  41 3A C7                        cmp al, r15b
009258DA  0F 84 E7 02 00 00               je 0x140925bc7
009258E0  48 8B CF                        mov rcx, rdi
009258E3  E8 18 BD 9B FF                  call 0x1402e1600
009258E8  48 8B CE                        mov rcx, rsi
009258EB  E8 C0 4F F6 FF                  call 0x14088a8b0
009258F0  66 01 5E E2                     add word ptr [rsi - 0x1e], bx
009258F4  4C 39 6E 10                     cmp qword ptr [rsi + 0x10], r13
009258F8  0F 85 7B 02 00 00               jne 0x140925b79
009258FE  41 B8 00 00 01 00               mov r8d, 0x10000
00925904  48 8B D6                        mov rdx, rsi
00925907  49 8B CD                        mov rcx, r13
0092590A  E8 11 E8 F6 FF                  call 0x140894120
0092590F  E9 3D FD FF FF                  jmp 0x140925651
00925914  48 8B CE                        mov rcx, rsi
00925917  E8 F4 A7 F6 FF                  call 0x140890110
0092591C  48 8B C3                        mov rax, rbx
0092591F  F0 48 0F C1 07                  lock xadd qword ptr [rdi], rax
00925924  40 22 C5                        and al, bpl
00925927  41 3A C7                        cmp al, r15b
0092592A  0F 84 8A 02 00 00               je 0x140925bba
00925930  48 8B CF                        mov rcx, rdi
00925933  E8 C8 BC 9B FF                  call 0x1402e1600
00925938  48 8B CE                        mov rcx, rsi
0092593B  E8 70 4F F6 FF                  call 0x14088a8b0
00925940  66 01 5E E2                     add word ptr [rsi - 0x1e], bx
00925944  4C 39 6E 10                     cmp qword ptr [rsi + 0x10], r13
00925948  0F 85 38 02 00 00               jne 0x140925b86
0092594E  41 B8 00 00 01 00               mov r8d, 0x10000
00925954  48 8B D6                        mov rdx, rsi
00925957  49 8B CD                        mov rcx, r13
0092595A  E8 C1 E7 F6 FF                  call 0x140894120
0092595F  E9 52 FD FF FF                  jmp 0x1409256b6
00925964  49 8B CE                        mov rcx, r14
00925967  E8 74 81 AF FF                  call 0x14041dae0
0092596C  F6 D8                           neg al
0092596E  48 1B D2                        sbb rdx, rdx
00925971  4C 23 F2                        and r14, rdx
00925974  E9 13 FE FF FF                  jmp 0x14092578c
00925979  41 8B 86 A0 01 00 00            mov eax, dword ptr [r14 + 0x1a0]
00925980  A8 08                           test al, 8
00925982  0F 85 36 FE FF FF               jne 0x1409257be
00925988  4C 8D 85 90 00 00 00            lea r8, [rbp + 0x90]
0092598F  41 B9 01 00 00 00               mov r9d, 1
00925995  48 8B D5                        mov rdx, rbp
00925998  49 8B CE                        mov rcx, r14
0092599B  E8 50 F9 10 00                  call 0x140a352f0
009259A0  4C 8D BD A0 00 00 00            lea r15, [rbp + 0xa0]
009259A7  48 8D B5 88 00 00 00            lea rsi, [rbp + 0x88]
009259AE  45 33 C0                        xor r8d, r8d
009259B1  33 D2                           xor edx, edx
009259B3  48 8B CE                        mov rcx, rsi
009259B6  E8 75 A8 8E FF                  call 0x140210230
009259BB  F0 48 0F BA 2E 00               lock bts qword ptr [rsi], 0
009259C1  48 8B F8                        mov rdi, rax
009259C4  73 0E                           jae 0x1409259d4
009259C6  4C 8B C6                        mov r8, rsi
009259C9  48 8B D0                        mov rdx, rax
009259CC  48 8B CE                        mov rcx, rsi
009259CF  E8 BC A2 8E FF                  call 0x14020fc90
009259D4  48 85 FF                        test rdi, rdi
009259D7  74 04                           je 0x1409259dd
009259D9  C6 47 0A 01                     mov byte ptr [rdi + 0xa], 1
009259DD  49 8B 3F                        mov rdi, qword ptr [r15]
009259E0  49 3B FF                        cmp rdi, r15
009259E3  74 1C                           je 0x140925a01
009259E5  4C 39 77 18                     cmp qword ptr [rdi + 0x18], r14
009259E9  0F 84 FF 01 00 00               je 0x140925bee
009259EF  F7 47 28 00 00 01 00            test dword ptr [rdi + 0x28], 0x10000
009259F6  0F 85 F2 01 00 00               jne 0x140925bee
009259FC  48 8B 3F                        mov rdi, qword ptr [rdi]
009259FF  EB DF                           jmp 0x1409259e0
00925A01  48 8B C3                        mov rax, rbx
00925A04  F0 48 0F C1 06                  lock xadd qword ptr [rsi], rax
00925A09  24 06                           and al, 6
00925A0B  3C 02                           cmp al, 2
00925A0D  0F 84 9A 01 00 00               je 0x140925bad
00925A13  48 8B CE                        mov rcx, rsi
00925A16  E8 E5 BB 9B FF                  call 0x1402e1600
00925A1B  41 8B 85 A0 01 00 00            mov eax, dword ptr [r13 + 0x1a0]
00925A22  84 C0                           test al, al
00925A24  78 7B                           js 0x140925aa1
00925A26  4C 8D BD B8 00 00 00            lea r15, [rbp + 0xb8]
00925A2D  48 8D B5 B0 00 00 00            lea rsi, [rbp + 0xb0]
00925A34  45 33 C0                        xor r8d, r8d
00925A37  33 D2                           xor edx, edx
00925A39  48 8B CE                        mov rcx, rsi
00925A3C  E8 EF A7 8E FF                  call 0x140210230
00925A41  F0 48 0F BA 2E 00               lock bts qword ptr [rsi], 0
00925A47  48 8B F8                        mov rdi, rax
00925A4A  73 0E                           jae 0x140925a5a
00925A4C  4C 8B C6                        mov r8, rsi
00925A4F  48 8B D0                        mov rdx, rax
00925A52  48 8B CE                        mov rcx, rsi
00925A55  E8 36 A2 8E FF                  call 0x14020fc90
00925A5A  48 85 FF                        test rdi, rdi
00925A5D  74 04                           je 0x140925a63
00925A5F  C6 47 0A 01                     mov byte ptr [rdi + 0xa], 1
00925A63  49 8B 3F                        mov rdi, qword ptr [r15]
00925A66  49 3B FF                        cmp rdi, r15
00925A69  74 1C                           je 0x140925a87
00925A6B  4C 39 77 18                     cmp qword ptr [rdi + 0x18], r14
00925A6F  0F 84 C7 01 00 00               je 0x140925c3c
00925A75  F7 47 28 00 00 01 00            test dword ptr [rdi + 0x28], 0x10000
00925A7C  0F 85 BA 01 00 00               jne 0x140925c3c
00925A82  48 8B 3F                        mov rdi, qword ptr [rdi]
00925A85  EB DF                           jmp 0x140925a66
00925A87  48 8B C3                        mov rax, rbx
00925A8A  F0 48 0F C1 06                  lock xadd qword ptr [rsi], rax
00925A8F  24 06                           and al, 6
00925A91  3C 02                           cmp al, 2
00925A93  0F 84 48 01 00 00               je 0x140925be1
00925A99  48 8B CE                        mov rcx, rsi
00925A9C  E8 5F BB 9B FF                  call 0x1402e1600
00925AA1  4C 8D BD D0 00 00 00            lea r15, [rbp + 0xd0]
00925AA8  48 8D BD C8 00 00 00            lea rdi, [rbp + 0xc8]
00925AAF  45 33 C0                        xor r8d, r8d
00925AB2  33 D2                           xor edx, edx
00925AB4  48 8B CF                        mov rcx, rdi
00925AB7  E8 74 A7 8E FF                  call 0x140210230
00925ABC  F0 48 0F BA 2F 00               lock bts qword ptr [rdi], 0
00925AC2  48 8B F0                        mov rsi, rax
00925AC5  73 0E                           jae 0x140925ad5
00925AC7  4C 8B C7                        mov r8, rdi
00925ACA  48 8B D0                        mov rdx, rax
00925ACD  48 8B CF                        mov rcx, rdi
00925AD0  E8 BB A1 8E FF                  call 0x14020fc90
00925AD5  48 85 F6                        test rsi, rsi
00925AD8  74 04                           je 0x140925ade
00925ADA  C6 46 0A 01                     mov byte ptr [rsi + 0xa], 1
00925ADE  49 8B 37                        mov rsi, qword ptr [r15]
00925AE1  49 3B F7                        cmp rsi, r15
00925AE4  74 1C                           je 0x140925b02
00925AE6  4C 39 76 18                     cmp qword ptr [rsi + 0x18], r14
00925AEA  0F 84 96 01 00 00               je 0x140925c86
00925AF0  F7 46 28 00 00 01 00            test dword ptr [rsi + 0x28], 0x10000
00925AF7  0F 85 89 01 00 00               jne 0x140925c86
00925AFD  48 8B 36                        mov rsi, qword ptr [rsi]
00925B00  EB DF                           jmp 0x140925ae1
00925B02  F0 48 0F C1 1F                  lock xadd qword ptr [rdi], rbx
00925B07  80 E3 06                        and bl, 6
00925B0A  80 FB 02                        cmp bl, 2
00925B0D  0F 84 C1 00 00 00               je 0x140925bd4
00925B13  48 8B CF                        mov rcx, rdi
00925B16  E8 E5 BA 9B FF                  call 0x1402e1600
00925B1B  49 8B D5                        mov rdx, r13
00925B1E  48 8B CD                        mov rcx, rbp
00925B21  E8 A6 15 10 00                  call 0x140a270cc
00925B26  E9 93 FC FF FF                  jmp 0x1409257be
00925B2B  48 8B CF                        mov rcx, rdi
00925B2E  E8 9D 02 94 FF                  call 0x140265dd0
00925B33  E9 A5 FA FF FF                  jmp 0x1409255dd
00925B38  48 8B CF                        mov rcx, rdi
00925B3B  E8 90 02 94 FF                  call 0x140265dd0
00925B40  E9 F6 FA FF FF                  jmp 0x14092563b
00925B45  48 8B CF                        mov rcx, rdi
00925B48  E8 83 02 94 FF                  call 0x140265dd0
00925B4D  E9 B3 FB FF FF                  jmp 0x140925705
00925B52  48 8B CF                        mov rcx, rdi
00925B55  E8 76 02 94 FF                  call 0x140265dd0
00925B5A  E9 41 FB FF FF                  jmp 0x1409256a0
00925B5F  48 8B CE                        mov rcx, rsi
00925B62  E8 79 1F F7 FF                  call 0x140897ae0
00925B67  E9 D0 FC FF FF                  jmp 0x14092583c
00925B6C  48 8B CE                        mov rcx, rsi
00925B6F  E8 6C 1F F7 FF                  call 0x140897ae0
00925B74  E9 73 FA FF FF                  jmp 0x1409255ec
00925B79  48 8B CE                        mov rcx, rsi
00925B7C  E8 5F 1F F7 FF                  call 0x140897ae0
00925B81  E9 CB FA FF FF                  jmp 0x140925651
00925B86  48 8B CE                        mov rcx, rsi
00925B89  E8 52 1F F7 FF                  call 0x140897ae0
00925B8E  E9 23 FB FF FF                  jmp 0x1409256b6
00925B93  48 8B CF                        mov rcx, rdi
00925B96  E8 35 02 94 FF                  call 0x140265dd0
00925B9B  E9 6D FC FF FF                  jmp 0x14092580d
00925BA0  48 8B CF                        mov rcx, rdi
00925BA3  E8 28 02 94 FF                  call 0x140265dd0
00925BA8  E9 E3 FC FF FF                  jmp 0x140925890
00925BAD  48 8B CE                        mov rcx, rsi
00925BB0  E8 1B 02 94 FF                  call 0x140265dd0
00925BB5  E9 59 FE FF FF                  jmp 0x140925a13
00925BBA  48 8B CF                        mov rcx, rdi
00925BBD  E8 0E 02 94 FF                  call 0x140265dd0
00925BC2  E9 69 FD FF FF                  jmp 0x140925930
00925BC7  48 8B CF                        mov rcx, rdi
00925BCA  E8 01 02 94 FF                  call 0x140265dd0
00925BCF  E9 0C FD FF FF                  jmp 0x1409258e0
00925BD4  48 8B CF                        mov rcx, rdi
00925BD7  E8 F4 01 94 FF                  call 0x140265dd0
00925BDC  E9 32 FF FF FF                  jmp 0x140925b13
00925BE1  48 8B CE                        mov rcx, rsi
00925BE4  E8 E7 01 94 FF                  call 0x140265dd0
00925BE9  E9 AB FE FF FF                  jmp 0x140925a99
00925BEE  48 8B CF                        mov rcx, rdi
00925BF1  E8 1A A5 F6 FF                  call 0x140890110
00925BF6  48 8B C3                        mov rax, rbx
00925BF9  F0 48 0F C1 06                  lock xadd qword ptr [rsi], rax
00925BFE  24 06                           and al, 6
00925C00  3C 02                           cmp al, 2
00925C02  0F 84 EB 00 00 00               je 0x140925cf3
00925C08  48 8B CE                        mov rcx, rsi
00925C0B  E8 F0 B9 9B FF                  call 0x1402e1600
00925C10  48 8B CF                        mov rcx, rdi
00925C13  E8 98 4C F6 FF                  call 0x14088a8b0
00925C18  66 01 5F E2                     add word ptr [rdi - 0x1e], bx
00925C1C  4C 39 77 18                     cmp qword ptr [rdi + 0x18], r14
00925C20  0F 85 B3 00 00 00               jne 0x140925cd9
00925C26  41 B8 00 00 01 00               mov r8d, 0x10000
00925C2C  48 8B D7                        mov rdx, rdi
00925C2F  48 8B CD                        mov rcx, rbp
00925C32  E8 E9 E4 F6 FF                  call 0x140894120
00925C37  E9 72 FD FF FF                  jmp 0x1409259ae
00925C3C  48 8B CF                        mov rcx, rdi
00925C3F  E8 CC A4 F6 FF                  call 0x140890110
00925C44  48 8B C3                        mov rax, rbx
00925C47  F0 48 0F C1 06                  lock xadd qword ptr [rsi], rax
00925C4C  24 06                           and al, 6
00925C4E  3C 02                           cmp al, 2
00925C50  0F 84 AA 00 00 00               je 0x140925d00
00925C56  48 8B CE                        mov rcx, rsi
00925C59  E8 A2 B9 9B FF                  call 0x1402e1600
00925C5E  48 8B CF                        mov rcx, rdi
00925C61  E8 4A 4C F6 FF                  call 0x14088a8b0
00925C66  66 01 5F E2                     add word ptr [rdi - 0x1e], bx
00925C6A  4C 39 77 18                     cmp qword ptr [rdi + 0x18], r14
00925C6E  75 76                           jne 0x140925ce6
00925C70  41 B8 00 00 01 00               mov r8d, 0x10000
00925C76  48 8B D7                        mov rdx, rdi
00925C79  48 8B CD                        mov rcx, rbp
00925C7C  E8 9F E4 F6 FF                  call 0x140894120
00925C81  E9 AE FD FF FF                  jmp 0x140925a34
00925C86  48 8B CE                        mov rcx, rsi
00925C89  E8 82 A4 F6 FF                  call 0x140890110
00925C8E  48 8B C3                        mov rax, rbx
00925C91  F0 48 0F C1 07                  lock xadd qword ptr [rdi], rax
00925C96  24 06                           and al, 6
00925C98  3C 02                           cmp al, 2
00925C9A  74 71                           je 0x140925d0d
00925C9C  48 8B CF                        mov rcx, rdi
00925C9F  E8 5C B9 9B FF                  call 0x1402e1600
00925CA4  48 8B CE                        mov rcx, rsi
00925CA7  E8 04 4C F6 FF                  call 0x14088a8b0
00925CAC  66 01 5E E2                     add word ptr [rsi - 0x1e], bx
00925CB0  4C 39 76 18                     cmp qword ptr [rsi + 0x18], r14
00925CB4  75 16                           jne 0x140925ccc
00925CB6  41 B8 00 00 01 00               mov r8d, 0x10000
00925CBC  48 8B D6                        mov rdx, rsi
00925CBF  48 8B CD                        mov rcx, rbp
00925CC2  E8 59 E4 F6 FF                  call 0x140894120
00925CC7  E9 E3 FD FF FF                  jmp 0x140925aaf
00925CCC  48 8B CE                        mov rcx, rsi
00925CCF  E8 0C 1E F7 FF                  call 0x140897ae0
00925CD4  E9 D6 FD FF FF                  jmp 0x140925aaf
00925CD9  48 8B CF                        mov rcx, rdi
00925CDC  E8 FF 1D F7 FF                  call 0x140897ae0
00925CE1  E9 C8 FC FF FF                  jmp 0x1409259ae
00925CE6  48 8B CF                        mov rcx, rdi
00925CE9  E8 F2 1D F7 FF                  call 0x140897ae0
00925CEE  E9 41 FD FF FF                  jmp 0x140925a34
00925CF3  48 8B CE                        mov rcx, rsi
00925CF6  E8 D5 00 94 FF                  call 0x140265dd0
00925CFB  E9 08 FF FF FF                  jmp 0x140925c08
00925D00  48 8B CE                        mov rcx, rsi
00925D03  E8 C8 00 94 FF                  call 0x140265dd0
00925D08  E9 49 FF FF FF                  jmp 0x140925c56
00925D0D  48 8B CF                        mov rcx, rdi
00925D10  E8 BB 00 94 FF                  call 0x140265dd0
00925D15  EB 85                           jmp 0x140925c9c
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall AlpcpFlushMessagesPort(__int64 a1, int a2, int a3)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;

    v_stack_p10 = v_rbx;
    v_stack_p18 = v_rbp;
    v_stack_p20 = v_rsi;
    v_rsp = (v_rsp) - (32);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(a1 + 136, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = a1 + 136;
        a2 = result;
        a1 = a1 + 136;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    v_r12 = 0;
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    v_rbx = (result) | (-1);
loc_009255BD:
    if ((*(unsigned __int64 *)(a1 + 144)) != (a1 + 144)) goto loc_009257F1;
    result = (unsigned __int8)((v_rbx) & ((unsigned __int8)(v_rbx + 7)));
    if (((unsigned __int8)(result)) == 2) goto loc_00925B2B;
loc_009255DD:
    result = KeAbPostRelease(a1 + 136, a2, a3, a4);
loc_009255EC:
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(a1 + 136, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = a1 + 136;
        a2 = result;
        a1 = a1 + 136;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    if ((*(unsigned __int64 *)(a1 + 160)) != (a1 + 160)) goto loc_00925874;
    result = (unsigned __int8)((v_rbx) & ((unsigned __int8)(v_rbx + 7)));
    if (((unsigned __int8)(result)) == 2) goto loc_00925B38;
loc_0092563B:
    result = KeAbPostRelease(a1 + 136, a2, a3, a4);
loc_00925651:
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(a1 + 176, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = a1 + 176;
        a2 = result;
        a1 = a1 + 176;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    if ((*(unsigned __int64 *)(a1 + 184)) != (a1 + 184)) goto loc_009258C4;
    result = (unsigned __int8)((v_rbx) & ((unsigned __int8)(v_rbx + 7)));
    if (((unsigned __int8)(result)) == 2) goto loc_00925B52;
loc_009256A0:
    result = KeAbPostRelease(a1 + 176, a2, a3, a4);
loc_009256B6:
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(a1 + 200, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = a1 + 200;
        a2 = result;
        a1 = a1 + 200;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    if ((*(unsigned __int64 *)(a1 + 208)) != (a1 + 208)) goto loc_00925914;
    result = (unsigned __int8)((v_rbx) & ((unsigned __int8)(v_rbx + 7)));
    if (((unsigned __int8)(result)) == 2) goto loc_00925B45;
loc_00925705:
    result = KeAbPostRelease(a1 + 200, a2, a3, a4);
    a2 = 0;
    result = AlpcpFlushCancelQueue(a1, a2, a3, a4);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 416))) & ((unsigned int)(v_rbx + 7)));
    if (((unsigned __int8)(result)) != ((unsigned __int8)(v_rbx + 7))) goto loc_009257D3;
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(*(unsigned __int64 *)(a1 + 16) - 16, a2, a3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = *(unsigned __int64 *)(a1 + 16) - 16;
        a3 = 0;
        a2 = 0;
        a1 = *(unsigned __int64 *)(a1 + 16) - 16;
        result = ExfAcquirePushLockSharedEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    v_rbp = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16));
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16)) != 0) {
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16));
        result = ObReferenceObjectSafe(a1, a2, a3, a4);
        result = (unsigned __int8)(-(result));
        v_rbp = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16))) & (a1);
    }
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 16) != 0) goto loc_00925964;
loc_0092578C:
    result = result + 17;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 16) != 0) {
        a1 = *(unsigned __int64 *)(a1 + 16) - 16;
        result = ExfReleasePushLockShared(a1, a2, a3, a4);
    }
    result = KeAbPostRelease(*(unsigned __int64 *)(a1 + 16) - 16, a2, a3, a4);
    if (v_rbp == 0) goto loc_009257C6;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rbp + 416)))) & (64)) != 0) goto loc_009257BE;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 16) != 0) goto loc_00925979;
loc_009257BE:
    result = ObfDereferenceObject(v_rbp, a2, a3, a4);
loc_009257C6:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 16) != 0) {
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 16);
        result = ObfDereferenceObject(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (32);
    return result;
loc_009257F1:
    result = AlpcpReferenceBlob(v_stack_p20, a2, a3, a4);
    result = (unsigned __int8)((v_stack_p10) & ((unsigned __int8)(v_stack_p18)));
    if (((unsigned __int8)(result)) == ((unsigned __int8)(result + 17))) goto loc_00925B93;
loc_0092580D:
    result = KeAbPostRelease(*(unsigned __int64 *)(a1 + 16) - 16, a2, a3, a4);
    result = AlpcpLockForCachedReferenceBlob(v_stack_p20, a2, a3, a4);
    if ((*(unsigned __int64 *)(v_stack_p20 + 16)) != a1) goto loc_00925B5F;
    result = AlpcpCancelMessage(a1, v_stack_p20, (unsigned int)(0x10000ULL), a4);
loc_0092583C:
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(*(unsigned __int64 *)(a1 + 16) - 16, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = *(unsigned __int64 *)(a1 + 16) - 16;
        a2 = result;
        a1 = *(unsigned __int64 *)(a1 + 16) - 16;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    if (result == 0) goto loc_009255BD;
    *(unsigned __int8 *)(result + 10) = 1;
    goto loc_009255BD;
loc_00925874:
    result = AlpcpReferenceBlob(result, a2, a3, a4);
    result = (unsigned __int8)((v_stack_p10) & ((unsigned __int8)(v_stack_p18)));
    if (((unsigned __int8)(result)) == ((unsigned __int8)(result + 17))) goto loc_00925BA0;
loc_00925890:
    result = KeAbPostRelease(*(unsigned __int64 *)(a1 + 16) - 16, a2, a3, a4);
    result = AlpcpLockForCachedReferenceBlob(result, a2, a3, a4);
    if ((*(unsigned __int64 *)(result + 16)) != a1) goto loc_00925B6C;
    result = AlpcpCancelMessage(a1, result, (unsigned int)(0x10000ULL), a4);
    goto loc_009255EC;
loc_009258C4:
    result = AlpcpReferenceBlob(result, result, (unsigned int)(0x10000ULL), a4);
    result = (unsigned __int8)((v_stack_p10) & ((unsigned __int8)(v_stack_p18)));
    if (((unsigned __int8)(result)) == ((unsigned __int8)(result + 17))) goto loc_00925BC7;
loc_009258E0:
    result = KeAbPostRelease(*(unsigned __int64 *)(a1 + 16) - 16, result, (unsigned int)(0x10000ULL), a4);
    result = AlpcpLockForCachedReferenceBlob(result, result, (unsigned int)(0x10000ULL), a4);
    if ((*(unsigned __int64 *)(result + 16)) != a1) goto loc_00925B79;
    result = AlpcpCancelMessage(a1, result, (unsigned int)(0x10000ULL), a4);
    goto loc_00925651;
loc_00925914:
    result = AlpcpReferenceBlob(result, result, (unsigned int)(0x10000ULL), a4);
    result = (unsigned __int8)((v_stack_p10) & ((unsigned __int8)(v_stack_p18)));
    if (((unsigned __int8)(result)) == ((unsigned __int8)(result + 17))) goto loc_00925BBA;
loc_00925930:
    result = KeAbPostRelease(*(unsigned __int64 *)(a1 + 16) - 16, result, (unsigned int)(0x10000ULL), a4);
    result = AlpcpLockForCachedReferenceBlob(result, result, (unsigned int)(0x10000ULL), a4);
    if ((*(unsigned __int64 *)(result + 16)) != a1) goto loc_00925B86;
    result = AlpcpCancelMessage(a1, result, (unsigned int)(0x10000ULL), a4);
    goto loc_009256B6;
loc_00925964:
    result = ObReferenceObjectSafe(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 16), result, (unsigned int)(0x10000ULL), a4);
    result = (unsigned __int8)(-(result));
    v_r14 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 16)) & (result);
    goto loc_0092578C;
loc_00925979:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_r14 + 416)))) & (8)) != 0) goto loc_009257BE;
    result = AlpcpFlushMessagesByRequestor(v_r14, v_stack_p18, v_stack_p18 + 144, 1);
loc_009259AE:
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_stack_p18 + 136, a2, a3, 1);
    if (!(condition_is_above_or_equal)) {
        a3 = v_stack_p18 + 136;
        a2 = result;
        a1 = v_stack_p18 + 136;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, 1);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
loc_009259E0:
    if ((*(unsigned __int64 *)(v_stack_p18 + 160)) == (v_stack_p18 + 160)) goto loc_00925A01;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p18 + 160) + 24)) == v_r14) goto loc_00925BEE;
    if (((*(unsigned int *)(*(unsigned __int64 *)(v_stack_p18 + 160) + 40)) & (0x10000ULL)) != 0) goto loc_00925BEE;
    goto loc_009259E0;
loc_00925A01:
    result = (unsigned __int8)((v_stack_p10) & (6));
    if (((unsigned __int8)(result)) == 2) goto loc_00925BAD;
loc_00925A13:
    result = KeAbPostRelease(v_stack_p18 + 136, a2, a3, 1);
    if (sign_flag) goto loc_00925AA1;
loc_00925A34:
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_stack_p18 + 176, a2, a3, 1);
    if (!(condition_is_above_or_equal)) {
        a3 = v_stack_p18 + 176;
        a2 = result;
        a1 = v_stack_p18 + 176;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, 1);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
loc_00925A66:
    if ((*(unsigned __int64 *)(v_stack_p18 + 184)) == (v_stack_p18 + 184)) goto loc_00925A87;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p18 + 184) + 24)) == v_r14) goto loc_00925C3C;
    if (((*(unsigned int *)(*(unsigned __int64 *)(v_stack_p18 + 184) + 40)) & (0x10000ULL)) != 0) goto loc_00925C3C;
    goto loc_00925A66;
loc_00925A87:
    result = (unsigned __int8)((v_stack_p10) & (6));
    if (((unsigned __int8)(result)) == 2) goto loc_00925BE1;
loc_00925A99:
    result = KeAbPostRelease(v_stack_p18 + 176, a2, a3, 1);
loc_00925AA1:
loc_00925AAF:
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_stack_p18 + 200, a2, a3, 1);
    if (!(condition_is_above_or_equal)) {
        a3 = v_stack_p18 + 200;
        a2 = result;
        a1 = v_stack_p18 + 200;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, 1);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
loc_00925AE1:
    if ((*(unsigned __int64 *)(v_stack_p18 + 208)) == (v_stack_p18 + 208)) goto loc_00925B02;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p18 + 208) + 24)) == v_r14) goto loc_00925C86;
    if (((*(unsigned int *)(*(unsigned __int64 *)(v_stack_p18 + 208) + 40)) & (0x10000ULL)) != 0) goto loc_00925C86;
    goto loc_00925AE1;
loc_00925B02:
    v_rbx = (unsigned __int8)((v_stack_p10) & (6));
    if (((unsigned __int8)(v_rbx)) == 2) goto loc_00925BD4;
loc_00925B13:
    result = KeAbPostRelease(v_stack_p18 + 200, a2, a3, 1);
    result = AlpcpFlushCancelQueue(v_stack_p18, a1, a3, 1);
    goto loc_009257BE;
loc_00925B2B:
    result = ExfTryToWakePushLock(v_stack_p18 + 200, a1, a3, 1);
    goto loc_009255DD;
loc_00925B38:
    result = ExfTryToWakePushLock(v_stack_p18 + 200, a1, a3, 1);
    goto loc_0092563B;
loc_00925B45:
    result = ExfTryToWakePushLock(v_stack_p18 + 200, a1, a3, 1);
    goto loc_00925705;
loc_00925B52:
    result = ExfTryToWakePushLock(v_stack_p18 + 200, a1, a3, 1);
    goto loc_009256A0;
loc_00925B5F:
    result = AlpcpUnlockMessage(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p18 + 208)), a1, a3, 1);
    goto loc_0092583C;
loc_00925B6C:
    result = AlpcpUnlockMessage(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p18 + 208)), a1, a3, 1);
    goto loc_009255EC;
loc_00925B79:
    result = AlpcpUnlockMessage(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p18 + 208)), a1, a3, 1);
    goto loc_00925651;
loc_00925B86:
    result = AlpcpUnlockMessage(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p18 + 208)), a1, a3, 1);
    goto loc_009256B6;
loc_00925B93:
    result = ExfTryToWakePushLock(v_stack_p18 + 200, a1, a3, 1);
    goto loc_0092580D;
loc_00925BA0:
    result = ExfTryToWakePushLock(v_stack_p18 + 200, a1, a3, 1);
    goto loc_00925890;
loc_00925BAD:
    result = ExfTryToWakePushLock(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p18 + 208)), a1, a3, 1);
    goto loc_00925A13;
loc_00925BBA:
    result = ExfTryToWakePushLock(v_stack_p18 + 200, a1, a3, 1);
    goto loc_00925930;
loc_00925BC7:
    result = ExfTryToWakePushLock(v_stack_p18 + 200, a1, a3, 1);
    goto loc_009258E0;
loc_00925BD4:
    result = ExfTryToWakePushLock(v_stack_p18 + 200, a1, a3, 1);
    goto loc_00925B13;
loc_00925BE1:
    result = ExfTryToWakePushLock(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p18 + 208)), a1, a3, 1);
    goto loc_00925A99;
loc_00925BEE:
    result = AlpcpReferenceBlob(v_stack_p18 + 200, a1, a3, 1);
    result = (unsigned __int8)((v_rbx) & (6));
    if (((unsigned __int8)(result)) == 2) goto loc_00925CF3;
loc_00925C08:
    result = KeAbPostRelease(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p18 + 208)), a1, a3, 1);
    result = AlpcpLockForCachedReferenceBlob(v_stack_p18 + 200, a1, a3, 1);
    if ((*(unsigned __int64 *)(v_stack_p18 + 200 + 24)) != v_r14) goto loc_00925CD9;
    result = AlpcpCancelMessage(v_stack_p18, v_stack_p18 + 200, (unsigned int)(0x10000ULL), 1);
    goto loc_009259AE;
loc_00925C3C:
    result = AlpcpReferenceBlob(v_stack_p18 + 200, v_stack_p18 + 200, (unsigned int)(0x10000ULL), 1);
    result = (unsigned __int8)((v_rbx) & (6));
    if (((unsigned __int8)(result)) == 2) goto loc_00925D00;
loc_00925C56:
    result = KeAbPostRelease(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p18 + 208)), v_stack_p18 + 200, (unsigned int)(0x10000ULL), 1);
    result = AlpcpLockForCachedReferenceBlob(v_stack_p18 + 200, v_stack_p18 + 200, (unsigned int)(0x10000ULL), 1);
    if ((*(unsigned __int64 *)(v_stack_p18 + 200 + 24)) != v_r14) goto loc_00925CE6;
    result = AlpcpCancelMessage(v_stack_p18, v_stack_p18 + 200, (unsigned int)(0x10000ULL), 1);
    goto loc_00925A34;
loc_00925C86:
    result = AlpcpReferenceBlob(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p18 + 208)), v_stack_p18 + 200, (unsigned int)(0x10000ULL), 1);
    result = (unsigned __int8)((v_rbx) & (6));
    if (((unsigned __int8)(result)) == 2) goto loc_00925D0D;
loc_00925C9C:
    result = KeAbPostRelease(v_stack_p18 + 200, v_stack_p18 + 200, (unsigned int)(0x10000ULL), 1);
    result = AlpcpLockForCachedReferenceBlob(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p18 + 208)), v_stack_p18 + 200, (unsigned int)(0x10000ULL), 1);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p18 + 208)) + 24)) != v_r14) goto loc_00925CCC;
    result = AlpcpCancelMessage(v_stack_p18, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p18 + 208)), (unsigned int)(0x10000ULL), 1);
    goto loc_00925AAF;
loc_00925CCC:
    result = AlpcpUnlockMessage(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p18 + 208)), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p18 + 208)), (unsigned int)(0x10000ULL), 1);
    goto loc_00925AAF;
loc_00925CD9:
    result = AlpcpUnlockMessage(v_stack_p18 + 200, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p18 + 208)), (unsigned int)(0x10000ULL), 1);
    goto loc_009259AE;
loc_00925CE6:
    result = AlpcpUnlockMessage(v_stack_p18 + 200, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p18 + 208)), (unsigned int)(0x10000ULL), 1);
    goto loc_00925A34;
loc_00925CF3:
    result = ExfTryToWakePushLock(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p18 + 208)), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p18 + 208)), (unsigned int)(0x10000ULL), 1);
    goto loc_00925C08;
loc_00925D00:
    result = ExfTryToWakePushLock(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p18 + 208)), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p18 + 208)), (unsigned int)(0x10000ULL), 1);
    goto loc_00925C56;
loc_00925D0D:
    result = ExfTryToWakePushLock(v_stack_p18 + 200, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p18 + 208)), (unsigned int)(0x10000ULL), 1);
    goto loc_00925C9C;
}
```

## 5. (Beta) C Style

```c
int64_t AlpcpFlushMessagesPort(void *Arg1, int32_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;

    v_stack_p10 = local_rbx;
    v_stack_p18 = local_rbp;
    v_stack_p20 = local_rsi;
    local_rsp = (local_rsp) - (32);
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(Arg1 + 136, Arg2, Arg3, a4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = Arg1 + 136;
        Arg2 = result;
        Arg1 = Arg1 + 136;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, a4);
    }
    local_r12 = 0;
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    local_rbx = (result) | (-1);
loc_009255BD:
    if ((*(uint64_t *)(arg1 + 0x90)) != (Arg1 + 144)) goto loc_009257F1;
    result = (uint8_t)((local_rbx) & ((uint8_t)(local_rbx + 7)));
    if (((uint8_t)(result)) == 2) goto loc_00925B2B;
loc_009255DD:
    result = KeAbPostRelease(Arg1 + 136, Arg2, Arg3, a4);
loc_009255EC:
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(Arg1 + 136, Arg2, Arg3, a4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = Arg1 + 136;
        Arg2 = result;
        Arg1 = Arg1 + 136;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, a4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    if ((*(uint64_t *)(arg1 + 0xA0)) != (Arg1 + 160)) goto loc_00925874;
    result = (uint8_t)((local_rbx) & ((uint8_t)(local_rbx + 7)));
    if (((uint8_t)(result)) == 2) goto loc_00925B38;
loc_0092563B:
    result = KeAbPostRelease(Arg1 + 136, Arg2, Arg3, a4);
loc_00925651:
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(Arg1 + 176, Arg2, Arg3, a4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = Arg1 + 176;
        Arg2 = result;
        Arg1 = Arg1 + 176;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, a4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    if ((*(uint64_t *)(arg1 + 0xB8)) != (Arg1 + 184)) goto loc_009258C4;
    result = (uint8_t)((local_rbx) & ((uint8_t)(local_rbx + 7)));
    if (((uint8_t)(result)) == 2) goto loc_00925B52;
loc_009256A0:
    result = KeAbPostRelease(Arg1 + 176, Arg2, Arg3, a4);
loc_009256B6:
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(Arg1 + 200, Arg2, Arg3, a4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = Arg1 + 200;
        Arg2 = result;
        Arg1 = Arg1 + 200;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, a4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    if ((*(uint64_t *)(arg1 + 0xD0)) != (Arg1 + 208)) goto loc_00925914;
    result = (uint8_t)((local_rbx) & ((uint8_t)(local_rbx + 7)));
    if (((uint8_t)(result)) == 2) goto loc_00925B45;
loc_00925705:
    result = KeAbPostRelease(Arg1 + 200, Arg2, Arg3, a4);
    Arg2 = 0;
    result = AlpcpFlushCancelQueue(Arg1, Arg2, Arg3, a4);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x1A0))) & ((uint32_t)(local_rbx + 7)));
    if (((uint8_t)(result)) != ((uint8_t)(local_rbx + 7))) goto loc_009257D3;
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(*(uint64_t *)(arg1 + 0x10) - 16, Arg2, Arg3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = *(uint64_t *)(arg1 + 0x10) - 16;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = *(uint64_t *)(arg1 + 0x10) - 16;
        result = ExfAcquirePushLockSharedEx(Arg1, Arg2, Arg3, a4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    local_rbp = *(uint64_t *)(*(uint64_t *)(arg1 + 0x10));
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x10)) != 0) {
        Arg1 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x10));
        result = ObReferenceObjectSafe(Arg1, Arg2, Arg3, a4);
        result = (uint8_t)(-(result));
        local_rbp = (*(uint64_t *)(*(uint64_t *)(arg1 + 0x10))) & (Arg1);
    }
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x10) != 0) goto loc_00925964;
loc_0092578C:
    result = result + 17;
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x10) != 0) {
        Arg1 = *(uint64_t *)(arg1 + 0x10) - 16;
        result = ExfReleasePushLockShared(Arg1, Arg2, Arg3, a4);
    }
    result = KeAbPostRelease(*(uint64_t *)(arg1 + 0x10) - 16, Arg2, Arg3, a4);
    if (local_rbp == 0) goto loc_009257C6;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rbp + 0x1A0)))) & (64)) != 0) goto loc_009257BE;
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x10) != 0) goto loc_00925979;
loc_009257BE:
    result = ObfDereferenceObject(local_rbp, Arg2, Arg3, a4);
loc_009257C6:
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x10) != 0) {
        Arg1 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x10);
        result = ObfDereferenceObject(Arg1, Arg2, Arg3, a4);
    }
    local_rsp = (local_rsp) + (32);
    return result;
loc_009257F1:
    result = AlpcpReferenceBlob(v_stack_p20, Arg2, Arg3, a4);
    result = (uint8_t)((v_stack_p10) & ((uint8_t)(v_stack_p18)));
    if (((uint8_t)(result)) == ((uint8_t)(result + 17))) goto loc_00925B93;
loc_0092580D:
    result = KeAbPostRelease(*(uint64_t *)(arg1 + 0x10) - 16, Arg2, Arg3, a4);
    result = AlpcpLockForCachedReferenceBlob(v_stack_p20, Arg2, Arg3, a4);
    if ((*(uint64_t *)(v_stack_p20 + 0x10)) != Arg1) goto loc_00925B5F;
    result = AlpcpCancelMessage(Arg1, v_stack_p20, (uint32_t)(0x10000ULL), a4);
loc_0092583C:
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(*(uint64_t *)(arg1 + 0x10) - 16, Arg2, Arg3, a4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = *(uint64_t *)(arg1 + 0x10) - 16;
        Arg2 = result;
        Arg1 = *(uint64_t *)(arg1 + 0x10) - 16;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, a4);
    }
    if (result == 0) goto loc_009255BD;
    *(uint8_t *)(result + 0xA) = 1;
    goto loc_009255BD;
loc_00925874:
    result = AlpcpReferenceBlob(result, Arg2, Arg3, a4);
    result = (uint8_t)((v_stack_p10) & ((uint8_t)(v_stack_p18)));
    if (((uint8_t)(result)) == ((uint8_t)(result + 17))) goto loc_00925BA0;
loc_00925890:
    result = KeAbPostRelease(*(uint64_t *)(arg1 + 0x10) - 16, Arg2, Arg3, a4);
    result = AlpcpLockForCachedReferenceBlob(result, Arg2, Arg3, a4);
    if ((*(uint64_t *)(result + 0x10)) != Arg1) goto loc_00925B6C;
    result = AlpcpCancelMessage(Arg1, result, (uint32_t)(0x10000ULL), a4);
    goto loc_009255EC;
loc_009258C4:
    result = AlpcpReferenceBlob(result, result, (uint32_t)(0x10000ULL), a4);
    result = (uint8_t)((v_stack_p10) & ((uint8_t)(v_stack_p18)));
    if (((uint8_t)(result)) == ((uint8_t)(result + 17))) goto loc_00925BC7;
loc_009258E0:
    result = KeAbPostRelease(*(uint64_t *)(arg1 + 0x10) - 16, result, (uint32_t)(0x10000ULL), a4);
    result = AlpcpLockForCachedReferenceBlob(result, result, (uint32_t)(0x10000ULL), a4);
    if ((*(uint64_t *)(result + 0x10)) != Arg1) goto loc_00925B79;
    result = AlpcpCancelMessage(Arg1, result, (uint32_t)(0x10000ULL), a4);
    goto loc_00925651;
loc_00925914:
    result = AlpcpReferenceBlob(result, result, (uint32_t)(0x10000ULL), a4);
    result = (uint8_t)((v_stack_p10) & ((uint8_t)(v_stack_p18)));
    if (((uint8_t)(result)) == ((uint8_t)(result + 17))) goto loc_00925BBA;
loc_00925930:
    result = KeAbPostRelease(*(uint64_t *)(arg1 + 0x10) - 16, result, (uint32_t)(0x10000ULL), a4);
    result = AlpcpLockForCachedReferenceBlob(result, result, (uint32_t)(0x10000ULL), a4);
    if ((*(uint64_t *)(result + 0x10)) != Arg1) goto loc_00925B86;
    result = AlpcpCancelMessage(Arg1, result, (uint32_t)(0x10000ULL), a4);
    goto loc_009256B6;
loc_00925964:
    result = ObReferenceObjectSafe(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x10), result, (uint32_t)(0x10000ULL), a4);
    result = (uint8_t)(-(result));
    local_r14 = (*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x10)) & (result);
    goto loc_0092578C;
loc_00925979:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x1A0)))) & (8)) != 0) goto loc_009257BE;
    result = AlpcpFlushMessagesByRequestor(local_r14, v_stack_p18, v_stack_p18 + 144, 1);
loc_009259AE:
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(v_stack_p18 + 136, Arg2, Arg3, 1);
    if (!(condition_is_above_or_equal)) {
        Arg3 = v_stack_p18 + 136;
        Arg2 = result;
        Arg1 = v_stack_p18 + 136;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, 1);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
loc_009259E0:
    if ((*(uint64_t *)(v_stack_p18 + 0xA0)) == (v_stack_p18 + 160)) goto loc_00925A01;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_p18 + 0xA0) + 0x18)) == local_r14) goto loc_00925BEE;
    if (((*(uint32_t *)(*(uint64_t *)(v_stack_p18 + 0xA0) + 0x28)) & (0x10000ULL)) != 0) goto loc_00925BEE;
    goto loc_009259E0;
loc_00925A01:
    result = (uint8_t)((v_stack_p10) & (6));
    if (((uint8_t)(result)) == 2) goto loc_00925BAD;
loc_00925A13:
    result = KeAbPostRelease(v_stack_p18 + 136, Arg2, Arg3, 1);
    if (sign_flag) goto loc_00925AA1;
loc_00925A34:
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(v_stack_p18 + 176, Arg2, Arg3, 1);
    if (!(condition_is_above_or_equal)) {
        Arg3 = v_stack_p18 + 176;
        Arg2 = result;
        Arg1 = v_stack_p18 + 176;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, 1);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
loc_00925A66:
    if ((*(uint64_t *)(v_stack_p18 + 0xB8)) == (v_stack_p18 + 184)) goto loc_00925A87;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_p18 + 0xB8) + 0x18)) == local_r14) goto loc_00925C3C;
    if (((*(uint32_t *)(*(uint64_t *)(v_stack_p18 + 0xB8) + 0x28)) & (0x10000ULL)) != 0) goto loc_00925C3C;
    goto loc_00925A66;
loc_00925A87:
    result = (uint8_t)((v_stack_p10) & (6));
    if (((uint8_t)(result)) == 2) goto loc_00925BE1;
loc_00925A99:
    result = KeAbPostRelease(v_stack_p18 + 176, Arg2, Arg3, 1);
loc_00925AA1:
loc_00925AAF:
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(v_stack_p18 + 200, Arg2, Arg3, 1);
    if (!(condition_is_above_or_equal)) {
        Arg3 = v_stack_p18 + 200;
        Arg2 = result;
        Arg1 = v_stack_p18 + 200;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, 1);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
loc_00925AE1:
    if ((*(uint64_t *)(v_stack_p18 + 0xD0)) == (v_stack_p18 + 208)) goto loc_00925B02;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_p18 + 0xD0) + 0x18)) == local_r14) goto loc_00925C86;
    if (((*(uint32_t *)(*(uint64_t *)(v_stack_p18 + 0xD0) + 0x28)) & (0x10000ULL)) != 0) goto loc_00925C86;
    goto loc_00925AE1;
loc_00925B02:
    local_rbx = (uint8_t)((v_stack_p10) & (6));
    if (((uint8_t)(local_rbx)) == 2) goto loc_00925BD4;
loc_00925B13:
    result = KeAbPostRelease(v_stack_p18 + 200, Arg2, Arg3, 1);
    result = AlpcpFlushCancelQueue(v_stack_p18, Arg1, Arg3, 1);
    goto loc_009257BE;
loc_00925B2B:
    result = ExfTryToWakePushLock(v_stack_p18 + 200, Arg1, Arg3, 1);
    goto loc_009255DD;
loc_00925B38:
    result = ExfTryToWakePushLock(v_stack_p18 + 200, Arg1, Arg3, 1);
    goto loc_0092563B;
loc_00925B45:
    result = ExfTryToWakePushLock(v_stack_p18 + 200, Arg1, Arg3, 1);
    goto loc_00925705;
loc_00925B52:
    result = ExfTryToWakePushLock(v_stack_p18 + 200, Arg1, Arg3, 1);
    goto loc_009256A0;
loc_00925B5F:
    result = AlpcpUnlockMessage(*(uint64_t *)(*(uint64_t *)(v_stack_p18 + 0xD0)), Arg1, Arg3, 1);
    goto loc_0092583C;
loc_00925B6C:
    result = AlpcpUnlockMessage(*(uint64_t *)(*(uint64_t *)(v_stack_p18 + 0xD0)), Arg1, Arg3, 1);
    goto loc_009255EC;
loc_00925B79:
    result = AlpcpUnlockMessage(*(uint64_t *)(*(uint64_t *)(v_stack_p18 + 0xD0)), Arg1, Arg3, 1);
    goto loc_00925651;
loc_00925B86:
    result = AlpcpUnlockMessage(*(uint64_t *)(*(uint64_t *)(v_stack_p18 + 0xD0)), Arg1, Arg3, 1);
    goto loc_009256B6;
loc_00925B93:
    result = ExfTryToWakePushLock(v_stack_p18 + 200, Arg1, Arg3, 1);
    goto loc_0092580D;
loc_00925BA0:
    result = ExfTryToWakePushLock(v_stack_p18 + 200, Arg1, Arg3, 1);
    goto loc_00925890;
loc_00925BAD:
    result = ExfTryToWakePushLock(*(uint64_t *)(*(uint64_t *)(v_stack_p18 + 0xD0)), Arg1, Arg3, 1);
    goto loc_00925A13;
loc_00925BBA:
    result = ExfTryToWakePushLock(v_stack_p18 + 200, Arg1, Arg3, 1);
    goto loc_00925930;
loc_00925BC7:
    result = ExfTryToWakePushLock(v_stack_p18 + 200, Arg1, Arg3, 1);
    goto loc_009258E0;
loc_00925BD4:
    result = ExfTryToWakePushLock(v_stack_p18 + 200, Arg1, Arg3, 1);
    goto loc_00925B13;
loc_00925BE1:
    result = ExfTryToWakePushLock(*(uint64_t *)(*(uint64_t *)(v_stack_p18 + 0xD0)), Arg1, Arg3, 1);
    goto loc_00925A99;
loc_00925BEE:
    result = AlpcpReferenceBlob(v_stack_p18 + 200, Arg1, Arg3, 1);
    result = (uint8_t)((local_rbx) & (6));
    if (((uint8_t)(result)) == 2) goto loc_00925CF3;
loc_00925C08:
    result = KeAbPostRelease(*(uint64_t *)(*(uint64_t *)(v_stack_p18 + 0xD0)), Arg1, Arg3, 1);
    result = AlpcpLockForCachedReferenceBlob(v_stack_p18 + 200, Arg1, Arg3, 1);
    if ((*(uint64_t *)(v_stack_p18 + 0xC8 + 0x18)) != local_r14) goto loc_00925CD9;
    result = AlpcpCancelMessage(v_stack_p18, v_stack_p18 + 200, (uint32_t)(0x10000ULL), 1);
    goto loc_009259AE;
loc_00925C3C:
    result = AlpcpReferenceBlob(v_stack_p18 + 200, v_stack_p18 + 200, (uint32_t)(0x10000ULL), 1);
    result = (uint8_t)((local_rbx) & (6));
    if (((uint8_t)(result)) == 2) goto loc_00925D00;
loc_00925C56:
    result = KeAbPostRelease(*(uint64_t *)(*(uint64_t *)(v_stack_p18 + 0xD0)), v_stack_p18 + 200, (uint32_t)(0x10000ULL), 1);
    result = AlpcpLockForCachedReferenceBlob(v_stack_p18 + 200, v_stack_p18 + 200, (uint32_t)(0x10000ULL), 1);
    if ((*(uint64_t *)(v_stack_p18 + 0xC8 + 0x18)) != local_r14) goto loc_00925CE6;
    result = AlpcpCancelMessage(v_stack_p18, v_stack_p18 + 200, (uint32_t)(0x10000ULL), 1);
    goto loc_00925A34;
loc_00925C86:
    result = AlpcpReferenceBlob(*(uint64_t *)(*(uint64_t *)(v_stack_p18 + 0xD0)), v_stack_p18 + 200, (uint32_t)(0x10000ULL), 1);
    result = (uint8_t)((local_rbx) & (6));
    if (((uint8_t)(result)) == 2) goto loc_00925D0D;
loc_00925C9C:
    result = KeAbPostRelease(v_stack_p18 + 200, v_stack_p18 + 200, (uint32_t)(0x10000ULL), 1);
    result = AlpcpLockForCachedReferenceBlob(*(uint64_t *)(*(uint64_t *)(v_stack_p18 + 0xD0)), v_stack_p18 + 200, (uint32_t)(0x10000ULL), 1);
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p18 + 0xD0)) + 0x18)) != local_r14) goto loc_00925CCC;
    result = AlpcpCancelMessage(v_stack_p18, *(uint64_t *)(*(uint64_t *)(v_stack_p18 + 0xD0)), (uint32_t)(0x10000ULL), 1);
    goto loc_00925AAF;
loc_00925CCC:
    result = AlpcpUnlockMessage(*(uint64_t *)(*(uint64_t *)(v_stack_p18 + 0xD0)), *(uint64_t *)(*(uint64_t *)(v_stack_p18 + 0xD0)), (uint32_t)(0x10000ULL), 1);
    goto loc_00925AAF;
loc_00925CD9:
    result = AlpcpUnlockMessage(v_stack_p18 + 200, *(uint64_t *)(*(uint64_t *)(v_stack_p18 + 0xD0)), (uint32_t)(0x10000ULL), 1);
    goto loc_009259AE;
loc_00925CE6:
    result = AlpcpUnlockMessage(v_stack_p18 + 200, *(uint64_t *)(*(uint64_t *)(v_stack_p18 + 0xD0)), (uint32_t)(0x10000ULL), 1);
    goto loc_00925A34;
loc_00925CF3:
    result = ExfTryToWakePushLock(*(uint64_t *)(*(uint64_t *)(v_stack_p18 + 0xD0)), *(uint64_t *)(*(uint64_t *)(v_stack_p18 + 0xD0)), (uint32_t)(0x10000ULL), 1);
    goto loc_00925C08;
loc_00925D00:
    result = ExfTryToWakePushLock(*(uint64_t *)(*(uint64_t *)(v_stack_p18 + 0xD0)), *(uint64_t *)(*(uint64_t *)(v_stack_p18 + 0xD0)), (uint32_t)(0x10000ULL), 1);
    goto loc_00925C56;
loc_00925D0D:
    result = ExfTryToWakePushLock(v_stack_p18 + 200, *(uint64_t *)(*(uint64_t *)(v_stack_p18 + 0xD0)), (uint32_t)(0x10000ULL), 1);
    goto loc_00925C9C;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x0` | `64` | `R/W` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x88` | `64` | `R` |
| `Arg1` | `+ 0x90` | `64` | `R` |
| `Arg1` | `+ 0xA0` | `64` | `R` |
| `Arg1` | `+ 0xB0` | `64` | `R` |
| `Arg1` | `+ 0xB8` | `64` | `R` |
| `Arg1` | `+ 0xC8` | `64` | `R` |
| `Arg1` | `+ 0xD0` | `64` | `R` |
| `Arg1` | `+ 0x1A0` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00925554&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
