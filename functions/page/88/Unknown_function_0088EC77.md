# sub_0088EC77

- RVA: `0x0088EC77`–`0x0088F3A4` (길이 `1,837` bytes)
- VA: `0x000000014088EC77`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007D56C`
- 디코드: `396`개 명령, `1,837/1,837` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **40**; 고유 호출 대상: **16**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x0088EC7A` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x0088EC94` → [AlpcpLogReceiveMessage](AlpcpLogReceiveMessage_function_0088F80C.md) (function, `0x0088F80C`)
- `0x0088ED5A` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0088EDBC` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0088EDE7` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x0088EE24` → [AlpcpGetDataFromUserVaSafe](../92/AlpcpGetDataFromUserVaSafe_function_00922908.md) (function, `0x00922908`)
- `0x0088EE41` → [AlpcpInsertMessagePendingQueue](../92/AlpcpInsertMessagePendingQueue_function_00922830.md) (function, `0x00922830`)
- `0x0088EE8C` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0088EEAF` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x0088EEDB` → [AlpcpUnlockMessage](../89/AlpcpUnlockMessage_function_00897AE0.md) (function, `0x00897AE0`)
- `0x0088EEFD` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0088EF1E` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0088EF3E` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0088EF46` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x0088EF89` → [KeReleaseSemaphoreEx](../../text/34/KeReleaseSemaphoreEx_function_003468C0.md) (function, `0x003468C0`)
- `0x0088EFBB` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0088EFF4` → [AlpcpQueueIoCompletionPort](../../text/3F/AlpcpQueueIoCompletionPort_function_003FF760.md) (function, `0x003FF760`)
- `0x0088EFFC` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x0088F02C` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0088F044` → [ExNotifyCallback](../../text/39/ExNotifyCallback_function_003926B0.md) (function, `0x003926B0`)
- `0x0088F07B` → [KeReleaseSemaphoreEx](../../text/34/KeReleaseSemaphoreEx_function_003468C0.md) (function, `0x003468C0`)
- `0x0088F083` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x0088F0A5` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0088F15D` → [AlpcpGetDataFromMessage](../92/AlpcpGetDataFromMessage_function_00922958.md) (function, `0x00922958`)
- `0x0088F16F` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x0088F18D` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x0088F1A3` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x0088F1C9` → [AlpcpAllocateFromBitmap](../9C/AlpcpAllocateFromBitmap_function_009CB130.md) (function, `0x009CB130`)
- `0x0088F206` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x0088F282` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x0088F2A0` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x0088F2B1` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x0088F2BB` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x0088F2D1` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x0088F2DB` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x0088F2ED` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x0088F313` → [AlpcpInsertMessagePendingQueue](../92/AlpcpInsertMessagePendingQueue_function_00922830.md) (function, `0x00922830`)
- `0x0088F343` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x0088F38D` → [AlpcpLogSendMessage](../89/AlpcpLogSendMessage_function_008903B4.md) (function, `0x008903B4`)
- `0x0088F39A` → [AlpcpLogWaitForReply](../74/AlpcpLogWaitForReply_function_0074D390.md) (function, `0x0074D390`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0088EC84` → RVA `0x00E66D00` (`.data`; read)
- `0x0088ECC6` → RVA `0x00FC50BC` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **31**
  - `0x0088EC7A` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x0088ED5A` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0088EDBC` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0088EDE7` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x0088EE8C` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0088EEAF` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x0088EEFD` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0088EF1E` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0088EF3E` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0088EF46` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x0088EF89` → [KeReleaseSemaphoreEx](../../text/34/KeReleaseSemaphoreEx_function_003468C0.md) (`PAGE` → `.text`)
  - `0x0088EFBB` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0088EFF4` → [AlpcpQueueIoCompletionPort](../../text/3F/AlpcpQueueIoCompletionPort_function_003FF760.md) (`PAGE` → `.text`)
  - `0x0088EFFC` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x0088F02C` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0088F044` → [ExNotifyCallback](../../text/39/ExNotifyCallback_function_003926B0.md) (`PAGE` → `.text`)
  - `0x0088F07B` → [KeReleaseSemaphoreEx](../../text/34/KeReleaseSemaphoreEx_function_003468C0.md) (`PAGE` → `.text`)
  - `0x0088F083` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x0088F0A5` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0088F16F` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x0088F18D` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x0088F1A3` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x0088F206` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x0088F282` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x0088F2A0` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x0088F2B1` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x0088F2BB` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x0088F2D1` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x0088F2DB` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x0088F2ED` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x0088F343` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **42**
  - `0x0088EC7F` → [sub_0088E1DC + 0x2FC](Unknown_function_0088E1DC.md) (`tail-transfer`)
  - `0x0088EC8B` → [sub_0088E1DC + 0x4DD](Unknown_function_0088E1DC.md) (`tail-transfer`)
  - `0x0088EC99` → [sub_0088E1DC + 0x4DD](Unknown_function_0088E1DC.md) (`tail-transfer`)
  - `0x0088ECB1` → [sub_0088E1DC + 0x3E5](Unknown_function_0088E1DC.md) (`tail-transfer`)
  - `0x0088ECB9` → [sub_0088E1DC + 0x637](Unknown_function_0088E1DC.md) (`tail-transfer`)
  - `0x0088ECC0` → [sub_0088E1DC + 0x35](Unknown_function_0088E1DC.md) (`tail-transfer`)
  - `0x0088ECCE` → [sub_0088E1DC + 0x35](Unknown_function_0088E1DC.md) (`tail-transfer`)
  - `0x0088ECD4` → [sub_0088E1DC + 0xA5](Unknown_function_0088E1DC.md) (`tail-transfer`)
  - `0x0088EDA0` → [sub_0088E1DC + 0x3FD](Unknown_function_0088E1DC.md) (`tail-transfer`)
  - `0x0088EDB1` → [sub_0088E1DC + 0x3FD](Unknown_function_0088E1DC.md) (`tail-transfer`)
  - `0x0088EDDF` → [sub_0088E1DC + 0x7DF](Unknown_function_0088E1DC.md) (`tail-transfer`)
  - `0x0088EDEC` → [sub_0088E1DC + 0x4BC](Unknown_function_0088E1DC.md) (`tail-transfer`)
  - `0x0088EE19` → [sub_0088E1DC + 0x96E](Unknown_function_0088E1DC.md) (`tail-transfer`)
  - `0x0088EE29` → [sub_0088E1DC + 0x7E4](Unknown_function_0088E1DC.md) (`tail-transfer`)
  - `0x0088EE46` → [sub_0088E1DC + 0x1F8](Unknown_function_0088E1DC.md) (`tail-transfer`)
  - `0x0088EE9F` → [sub_0088E1DC + 0x932](Unknown_function_0088E1DC.md) (`tail-transfer`)
  - `0x0088EEA7` → [sub_0088E1DC + 0x99](Unknown_function_0088E1DC.md) (`tail-transfer`)
  - `0x0088EEB4` → [sub_0088E1DC + 0xA1C](Unknown_function_0088E1DC.md) (`tail-transfer`)
  - `0x0088EEC1` → [sub_0088E1DC + 0x7B7](Unknown_function_0088E1DC.md) (`tail-transfer`)
  - `0x0088EF8E` → [sub_0088E1DC + 0x550](Unknown_function_0088E1DC.md) (`tail-transfer`)
  - `0x0088EF9B` → [sub_0088E1DC + 0x3FD](Unknown_function_0088E1DC.md) (`tail-transfer`)
  - `0x0088EFCD` → [sub_0088E1DC + 0x550](Unknown_function_0088E1DC.md) (`tail-transfer`)
  - `0x0088EFD9` → [sub_0088E1DC + 0x547](Unknown_function_0088E1DC.md) (`tail-transfer`)
  - `0x0088F005` → [sub_0088E1DC + 0x550](Unknown_function_0088E1DC.md) (`tail-transfer`)
  - `0x0088F08C` → [sub_0088E1DC + 0x550](Unknown_function_0088E1DC.md) (`tail-transfer`)
  - `0x0088F0B3` → [sub_0088E1DC + 0x847](Unknown_function_0088E1DC.md) (`tail-transfer`)
  - `0x0088F162` → [sub_0088E1DC + 0x7E4](Unknown_function_0088E1DC.md) (`tail-transfer`)
  - `0x0088F16A` → [sub_0088E1DC + 0xA7E](Unknown_function_0088E1DC.md) (`tail-transfer`)
  - `0x0088F179` → [sub_0088E1DC + 0x90F](Unknown_function_0088E1DC.md) (`tail-transfer`)
  - `0x0088F1A8` → [sub_0088E1DC + 0x361](Unknown_function_0088E1DC.md) (`tail-transfer`)
  - `0x0088F1D4` → [sub_0088E1DC + 0x6F9](Unknown_function_0088E1DC.md) (`tail-transfer`)
  - `0x0088F1FA` → [sub_0088E1DC + 0x6A3](Unknown_function_0088E1DC.md) (`tail-transfer`)
  - `0x0088F263` → [sub_0088E1DC + 0x4C7](Unknown_function_0088E1DC.md) (`tail-transfer`)
  - `0x0088F26A` → [sub_0088E1DC + 0x642](Unknown_function_0088E1DC.md) (`tail-transfer`)
  - `0x0088F274` → [sub_0088E1DC + 0x5F6](Unknown_function_0088E1DC.md) (`tail-transfer`)
  - `0x0088F27A` → [sub_0088E1DC + 0x3FD](Unknown_function_0088E1DC.md) (`tail-transfer`)
  - `0x0088F297` → [sub_0088E1DC + 0x550](Unknown_function_0088E1DC.md) (`tail-transfer`)
  - `0x0088F2F2` → [sub_0088E1DC + 0x3CC](Unknown_function_0088E1DC.md) (`tail-transfer`)
  - `0x0088F320` → [sub_0088E1DC + 0x4C7](Unknown_function_0088E1DC.md) (`tail-transfer`)
  - `0x0088F385` → [sub_00B1927C](../B1/Unknown_function_00B1927C.md) (`tail-transfer`)
  - `0x0088F392` → [sub_0088E1DC + 0x4D4](Unknown_function_0088E1DC.md) (`tail-transfer`)
  - `0x0088F39F` → [sub_0088E1DC + 0x4F4](Unknown_function_0088E1DC.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0088EC77  48 8B CF                        mov rcx, rdi
0088EC7A  E8 51 71 9D FF                  call 0x140265dd0
0088EC7F  E9 54 F8 FF FF                  jmp 0x14088e4d8
0088EC84  40 38 35 75 80 5D 00            cmp byte ptr [rip + 0x5d8075], sil
0088EC8B  0F 84 28 FA FF FF               je 0x14088e6b9
0088EC91  49 8B CE                        mov rcx, r14
0088EC94  E8 73 0B 00 00                  call 0x14088f80c
0088EC99  E9 1B FA FF FF                  jmp 0x14088e6b9
0088EC9E  8B 85 A0 01 00 00               mov eax, dword ptr [rbp + 0x1a0]
0088ECA4  45 32 E4                        xor r12b, r12b
0088ECA7  C1 E8 09                        shr eax, 9
0088ECAA  83 E0 01                        and eax, 1
0088ECAD  89 44 24 68                     mov dword ptr [rsp + 0x68], eax
0088ECB1  E9 0B F9 FF FF                  jmp 0x14088e5c1
0088ECB6  41 2B F9                        sub edi, r9d
0088ECB9  E9 55 FB FF FF                  jmp 0x14088e813
0088ECBE  85 D2                           test edx, edx
0088ECC0  0F 85 4B F5 FF FF               jne 0x14088e211
0088ECC6  8B 05 F0 63 73 00               mov eax, dword ptr [rip + 0x7363f0]
0088ECCC  A8 01                           test al, 1
0088ECCE  0F 84 3D F5 FF FF               je 0x14088e211
0088ECD4  E9 A8 F5 FF FF                  jmp 0x14088e281
0088ECD9  48 8B 7C 24 48                  mov rdi, qword ptr [rsp + 0x48]
0088ECDE  49 8B C0                        mov rax, r8
0088ECE1  25 FF FF FF 00                  and eax, 0xffffff
0088ECE6  48 3B C7                        cmp rax, rdi
0088ECE9  0F 83 36 06 00 00               jae 0x14088f325
0088ECEF  81 E1 FF FF FF 00               and ecx, 0xffffff
0088ECF5  48 3B CF                        cmp rcx, rdi
0088ECF8  0F 83 27 06 00 00               jae 0x14088f325
0088ECFE  48 8D 41 01                     lea rax, [rcx + 1]
0088ED02  33 D2                           xor edx, edx
0088ED04  48 F7 F7                        div rdi
0088ED07  48 B8 FF FF FF 00 00 00 FF FF   movabs rax, 0xffff000000ffffff
0088ED11  4C 8B D2                        mov r10, rdx
0088ED14  48 C1 E2 18                     shl rdx, 0x18
0088ED18  48 8B CA                        mov rcx, rdx
0088ED1B  41 81 E2 FF FF FF 00            and r10d, 0xffffff
0088ED22  49 33 C8                        xor rcx, r8
0088ED25  48 23 C8                        and rcx, rax
0088ED28  48 33 CA                        xor rcx, rdx
0088ED2B  48 8B C1                        mov rax, rcx
0088ED2E  25 FF FF FF 00                  and eax, 0xffffff
0088ED33  4C 3B D0                        cmp r10, rax
0088ED36  0F 85 0F 01 00 00               jne 0x14088ee4b
0088ED3C  48 8B BD 68 01 00 00            mov rdi, qword ptr [rbp + 0x168]
0088ED43  48 8B C3                        mov rax, rbx
0088ED46  F0 48 0F C1 47 18               lock xadd qword ptr [rdi + 0x18], rax
0088ED4C  24 06                           and al, 6
0088ED4E  3C 02                           cmp al, 2
0088ED50  0F 84 E9 05 00 00               je 0x14088f33f
0088ED56  48 8D 4F 18                     lea rcx, [rdi + 0x18]
0088ED5A  E8 A1 28 A5 FF                  call 0x1402e1600
0088ED5F  48 8B 85 68 01 00 00            mov rax, qword ptr [rbp + 0x168]
0088ED66  44 8B 84 24 F0 00 00 00         mov r8d, dword ptr [rsp + 0xf0]
0088ED6E  41 C1 EC 06                     shr r12d, 6
0088ED72  41 8B D4                        mov edx, r12d
0088ED75  48 8B 48 68                     mov rcx, qword ptr [rax + 0x68]
0088ED79  48 C1 EA 05                     shr rdx, 5
0088ED7D  4C 8D 0C 91                     lea r9, [rcx + rdx*4]
0088ED81  41 83 E4 1F                     and r12d, 0x1f
0088ED85  0F 87 C2 05 00 00               ja 0x14088f34d
0088ED8B  41 83 F8 20                     cmp r8d, 0x20
0088ED8F  0F 83 E9 05 00 00               jae 0x14088f37e
0088ED95  44 8B A4 24 F8 00 00 00         mov r12d, dword ptr [rsp + 0xf8]
0088ED9D  45 85 C0                        test r8d, r8d
0088EDA0  0F 84 33 F8 FF FF               je 0x14088e5d9
0088EDA6  41 8B C8                        mov ecx, r8d
0088EDA9  8B C3                           mov eax, ebx
0088EDAB  D3 E0                           shl eax, cl
0088EDAD  F0 41 21 01                     lock and dword ptr [r9], eax
0088EDB1  E9 23 F8 FF FF                  jmp 0x14088e5d9
0088EDB6  4C 8B C1                        mov r8, rcx
0088EDB9  49 8B C9                        mov rcx, r9
0088EDBC  E8 7F 7A E3 FF                  call 0x1406c6840
0088EDC1  4C 8B 44 24 70                  mov r8, qword ptr [rsp + 0x70]
0088EDC6  4C 2B 44 24 48                  sub r8, qword ptr [rsp + 0x48]
0088EDCB  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
0088EDD3  48 03 4C 24 48                  add rcx, qword ptr [rsp + 0x48]
0088EDD8  49 8B 96 E0 00 00 00            mov rdx, qword ptr [r14 + 0xe0]
0088EDDF  E9 D7 FB FF FF                  jmp 0x14088e9bb
0088EDE4  48 8B CF                        mov rcx, rdi
0088EDE7  E8 E4 6F 9D FF                  call 0x140265dd0
0088EDEC  E9 A7 F8 FF FF                  jmp 0x14088e698
0088EDF1  49 8B 47 50                     mov rax, qword ptr [r15 + 0x50]
0088EDF5  45 0F B6 E4                     movzx r12d, r12b
0088EDF9  48 8B 48 40                     mov rcx, qword ptr [rax + 0x40]
0088EDFD  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
0088EE01  48 C1 E9 30                     shr rcx, 0x30
0088EE05  8B 50 0C                        mov edx, dword ptr [rax + 0xc]
0088EE08  41 8B 87 90 00 00 00            mov eax, dword ptr [r15 + 0x90]
0088EE0F  48 03 D1                        add rdx, rcx
0088EE12  48 3B D0                        cmp rdx, rax
0088EE15  44 0F 43 E6                     cmovae r12d, esi
0088EE19  E9 2C FD FF FF                  jmp 0x14088eb4a
0088EE1E  49 8B D1                        mov rdx, r9
0088EE21  49 8B CE                        mov rcx, r14
0088EE24  E8 DF 3A 09 00                  call 0x140922908
0088EE29  E9 92 FB FF FF                  jmp 0x14088e9c0
0088EE2E  66 41 09 BE F4 00 00 00         or word ptr [r14 + 0xf4], di
0088EE36  49 8B D6                        mov rdx, r14
0088EE39  66 41 FF 46 E2                  inc word ptr [r14 - 0x1e]
0088EE3E  48 8B CD                        mov rcx, rbp
0088EE41  E8 EA 39 09 00                  call 0x140922830
0088EE46  E9 89 F5 FF FF                  jmp 0x14088e3d4
0088EE4B  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
0088EE50  48 8B 40 58                     mov rax, qword ptr [rax + 0x58]
0088EE54  46 89 24 90                     mov dword ptr [rax + r10*4], r12d
0088EE58  49 8B C0                        mov rax, r8
0088EE5B  F0 49 0F B1 49 40               lock cmpxchg qword ptr [r9 + 0x40], rcx
0088EE61  48 8B 8D 68 01 00 00            mov rcx, qword ptr [rbp + 0x168]
0088EE68  48 83 C1 18                     add rcx, 0x18
0088EE6C  49 3B C0                        cmp rax, r8
0088EE6F  48 89 4C 24 40                  mov qword ptr [rsp + 0x40], rcx
0088EE74  48 8B C3                        mov rax, rbx
0088EE77  0F 85 01 03 00 00               jne 0x14088f17e
0088EE7D  F0 48 0F C1 01                  lock xadd qword ptr [rcx], rax
0088EE82  24 06                           and al, 6
0088EE84  3C 02                           cmp al, 2
0088EE86  0F 84 2F 04 00 00               je 0x14088f2bb
0088EE8C  E8 6F 27 A5 FF                  call 0x1402e1600
0088EE91  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
0088EE96  F0 FF 80 80 00 00 00            lock inc dword ptr [rax + 0x80]
0088EE9D  8B D6                           mov edx, esi
0088EE9F  E9 6A FC FF FF                  jmp 0x14088eb0e
0088EEA4  48 8B C6                        mov rax, rsi
0088EEA7  E9 C9 F3 FF FF                  jmp 0x14088e275
0088EEAC  48 8B CF                        mov rcx, rdi
0088EEAF  E8 1C 6F 9D FF                  call 0x140265dd0
0088EEB4  E9 3F FD FF FF                  jmp 0x14088ebf8
0088EEB9  48 8B 49 20                     mov rcx, qword ptr [rcx + 0x20]
0088EEBD  48 83 E9 28                     sub rcx, 0x28
0088EEC1  E9 CD FA FF FF                  jmp 0x14088e993
0088EEC6  48 89 08                        mov qword ptr [rax], rcx
0088EEC9  48 89 41 08                     mov qword ptr [rcx + 8], rax
0088EECD  49 8B CE                        mov rcx, r14
0088EED0  49 89 37                        mov qword ptr [r15], rsi
0088EED3  41 81 66 28 FF FF FE FF         and dword ptr [r14 + 0x28], 0xfffeffff
0088EEDB  E8 00 8C 00 00                  call 0x140897ae0
0088EEE0  48 8B 9C 24 80 00 00 00         mov rbx, qword ptr [rsp + 0x80]
0088EEE8  B8 11 00 00 00                  mov eax, 0x11
0088EEED  F0 48 0F B1 73 F0               lock cmpxchg qword ptr [rbx - 0x10], rsi
0088EEF3  0F 85 A3 03 00 00               jne 0x14088f29c
0088EEF9  48 8D 4B F0                     lea rcx, [rbx - 0x10]
0088EEFD  E8 FE 26 A5 FF                  call 0x1402e1600
0088EF02  48 C7 C3 FF FF FF FF            mov rbx, 0xffffffffffffffff
0088EF09  F0 49 0F C1 1C 24               lock xadd qword ptr [r12], rbx
0088EF0F  80 E3 06                        and bl, 6
0088EF12  80 FB 02                        cmp bl, 2
0088EF15  0F 84 64 03 00 00               je 0x14088f27f
0088EF1B  49 8B CC                        mov rcx, r12
0088EF1E  E8 DD 26 A5 FF                  call 0x1402e1600
0088EF23  B8 11 00 00 00                  mov eax, 0x11
0088EF28  F0 48 0F B1 B5 60 01 00 00      lock cmpxchg qword ptr [rbp + 0x160], rsi
0088EF31  0F 85 73 03 00 00               jne 0x14088f2aa
0088EF37  48 8D 8D 60 01 00 00            lea rcx, [rbp + 0x160]
0088EF3E  E8 BD 26 A5 FF                  call 0x1402e1600
0088EF43  48 8B CD                        mov rcx, rbp
0088EF46  E8 05 A4 A6 FF                  call 0x1402f9350
0088EF4B  49 89 75 20                     mov qword ptr [r13 + 0x20], rsi
0088EF4F  39 74 24 50                     cmp dword ptr [rsp + 0x50], esi
0088EF53  0F 85 33 03 00 00               jne 0x14088f28c
0088EF59  39 B4 24 00 01 00 00            cmp dword ptr [rsp + 0x100], esi
0088EF60  0F 85 26 03 00 00               jne 0x14088f28c
0088EF66  8B 44 24 6C                     mov eax, dword ptr [rsp + 0x6c]
0088EF6A  49 8D 8F 50 FF FF FF            lea rcx, [r15 - 0xb0]
0088EF71  F7 D8                           neg eax
0088EF73  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
0088EF78  BA 01 00 00 00                  mov edx, 1
0088EF7D  1B C0                           sbb eax, eax
0088EF7F  44 8B C2                        mov r8d, edx
0088EF82  83 E0 02                        and eax, 2
0088EF85  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
0088EF89  E8 32 79 AB FF                  call 0x1403468c0
0088EF8E  E9 99 F7 FF FF                  jmp 0x14088e72c
0088EF93  44 8B A4 24 F8 00 00 00         mov r12d, dword ptr [rsp + 0xf8]
0088EF9B  E9 39 F6 FF FF                  jmp 0x14088e5d9
0088EFA0  B8 11 00 00 00                  mov eax, 0x11
0088EFA5  F0 48 0F B1 B5 60 01 00 00      lock cmpxchg qword ptr [rbp + 0x160], rsi
0088EFAE  0F 85 4B 02 00 00               jne 0x14088f1ff
0088EFB4  48 8D 8D 60 01 00 00            lea rcx, [rbp + 0x160]
0088EFBB  E8 40 26 A5 FF                  call 0x1402e1600
0088EFC0  45 85 FF                        test r15d, r15d
0088EFC3  0F 84 82 00 00 00               je 0x14088f04b
0088EFC9  41 88 75 3A                     mov byte ptr [r13 + 0x3a], sil
0088EFCD  E9 5A F7 FF FF                  jmp 0x14088e72c
0088EFD2  39 B4 24 00 01 00 00            cmp dword ptr [rsp + 0x100], esi
0088EFD9  0F 85 44 F7 FF FF               jne 0x14088e723
0088EFDF  8B 44 24 78                     mov eax, dword ptr [rsp + 0x78]
0088EFE3  45 33 C9                        xor r9d, r9d
0088EFE6  41 B0 01                        mov r8b, 1
0088EFE9  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
0088EFED  40 0F B6 D7                     movzx edx, dil
0088EFF1  48 8B CD                        mov rcx, rbp
0088EFF4  E8 67 07 B7 FF                  call 0x1403ff760
0088EFF9  48 8B CD                        mov rcx, rbp
0088EFFC  E8 4F A3 A6 FF                  call 0x1402f9350
0088F001  49 89 75 20                     mov qword ptr [r13 + 0x20], rsi
0088F005  E9 22 F7 FF FF                  jmp 0x14088e72c
0088F00A  48 8B 9D 70 01 00 00            mov rbx, qword ptr [rbp + 0x170]
0088F011  B8 11 00 00 00                  mov eax, 0x11
0088F016  F0 48 0F B1 B5 60 01 00 00      lock cmpxchg qword ptr [rbp + 0x160], rsi
0088F01F  0F 85 A5 02 00 00               jne 0x14088f2ca
0088F025  48 8D 8D 60 01 00 00            lea rcx, [rbp + 0x160]
0088F02C  E8 CF 25 A5 FF                  call 0x1402e1600
0088F031  48 85 DB                        test rbx, rbx
0088F034  74 4A                           je 0x14088f080
0088F036  45 8B 45 30                     mov r8d, dword ptr [r13 + 0x30]
0088F03A  48 8B CB                        mov rcx, rbx
0088F03D  48 8B 95 78 01 00 00            mov rdx, qword ptr [rbp + 0x178]
0088F044  E8 67 36 B0 FF                  call 0x1403926b0
0088F049  EB 35                           jmp 0x14088f080
0088F04B  39 B4 24 00 01 00 00            cmp dword ptr [rsp + 0x100], esi
0088F052  0F 85 71 FF FF FF               jne 0x14088efc9
0088F058  8B 44 24 6C                     mov eax, dword ptr [rsp + 0x6c]
0088F05C  BA 01 00 00 00                  mov edx, 1
0088F061  48 8B 8D F8 00 00 00            mov rcx, qword ptr [rbp + 0xf8]
0088F068  F7 D8                           neg eax
0088F06A  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
0088F06F  44 8B C2                        mov r8d, edx
0088F072  1B C0                           sbb eax, eax
0088F074  83 E0 02                        and eax, 2
0088F077  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
0088F07B  E8 40 78 AB FF                  call 0x1403468c0
0088F080  48 8B CD                        mov rcx, rbp
0088F083  E8 C8 A2 A6 FF                  call 0x1402f9350
0088F088  49 89 75 20                     mov qword ptr [r13 + 0x20], rsi
0088F08C  E9 9B F6 FF FF                  jmp 0x14088e72c
0088F091  F0 48 0F C1 01                  lock xadd qword ptr [rcx], rax
0088F096  24 06                           and al, 6
0088F098  3C 02                           cmp al, 2
0088F09A  0F 84 3B 02 00 00               je 0x14088f2db
0088F0A0  48 8B 7C 24 48                  mov rdi, qword ptr [rsp + 0x48]
0088F0A5  E8 56 25 A5 FF                  call 0x1402e1600
0088F0AA  8B 84 24 08 01 00 00            mov eax, dword ptr [rsp + 0x108]
0088F0B1  FF C0                           inc eax
0088F0B3  E9 6B F9 FF FF                  jmp 0x14088ea23
0088F0B8  41 0F B7 86 F0 00 00 00         movzx eax, word ptr [r14 + 0xf0]
0088F0C0  66 41 89 00                     mov word ptr [r8], ax
0088F0C4  41 0F B7 86 F0 00 00 00         movzx eax, word ptr [r14 + 0xf0]
0088F0CC  83 C0 18                        add eax, 0x18
0088F0CF  66 41 89 40 02                  mov word ptr [r8 + 2], ax
0088F0D4  41 0F B7 96 F6 00 00 00         movzx edx, word ptr [r14 + 0xf6]
0088F0DC  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
0088F0E0  66 85 D2                        test dx, dx
0088F0E3  8B C6                           mov eax, esi
0088F0E5  8D 4A F0                        lea ecx, [rdx - 0x10]
0088F0E8  66 0F 45 C1                     cmovne ax, cx
0088F0EC  66 41 89 40 06                  mov word ptr [r8 + 6], ax
0088F0F1  B8 00 10 00 00                  mov eax, 0x1000
0088F0F6  66 41 0B 86 F4 00 00 00         or ax, word ptr [r14 + 0xf4]
0088F0FE  66 41 89 40 04                  mov word ptr [r8 + 4], ax
0088F103  0F B7 D0                        movzx edx, ax
0088F106  41 8B 86 F8 00 00 00            mov eax, dword ptr [r14 + 0xf8]
0088F10D  41 89 40 08                     mov dword ptr [r8 + 8], eax
0088F111  41 8B 86 00 01 00 00            mov eax, dword ptr [r14 + 0x100]
0088F118  41 89 40 0C                     mov dword ptr [r8 + 0xc], eax
0088F11C  41 8B 86 08 01 00 00            mov eax, dword ptr [r14 + 0x108]
0088F123  41 89 40 10                     mov dword ptr [r8 + 0x10], eax
0088F127  41 8B 86 10 01 00 00            mov eax, dword ptr [r14 + 0x110]
0088F12E  41 89 40 14                     mov dword ptr [r8 + 0x14], eax
0088F132  41 8B 86 10 01 00 00            mov eax, dword ptr [r14 + 0x110]
0088F139  41 89 40 14                     mov dword ptr [r8 + 0x14], eax
0088F13D  F7 85 00 01 00 00 00 10 00 00   test dword ptr [rbp + 0x100], 0x1000
0088F147  74 0D                           je 0x14088f156
0088F149  B9 0F C0 FF FF                  mov ecx, 0xffffc00f
0088F14E  66 23 D1                        and dx, cx
0088F151  66 41 89 50 04                  mov word ptr [r8 + 4], dx
0088F156  49 8D 50 18                     lea rdx, [r8 + 0x18]
0088F15A  49 8B CE                        mov rcx, r14
0088F15D  E8 F6 37 09 00                  call 0x140922958
0088F162  E9 59 F8 FF FF                  jmp 0x14088e9c0
0088F167  48 8B C6                        mov rax, rsi
0088F16A  E9 EB FA FF FF                  jmp 0x14088ec5a
0088F16F  E8 5C 6C 9D FF                  call 0x140265dd0
0088F174  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
0088F179  E9 6D F9 FF FF                  jmp 0x14088eaeb
0088F17E  F0 48 0F C1 01                  lock xadd qword ptr [rcx], rax
0088F183  24 06                           and al, 6
0088F185  3C 02                           cmp al, 2
0088F187  0F 85 18 FF FF FF               jne 0x14088f0a5
0088F18D  E8 3E 6C 9D FF                  call 0x140265dd0
0088F192  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
0088F197  E9 09 FF FF FF                  jmp 0x14088f0a5
0088F19C  48 8D 8D 60 01 00 00            lea rcx, [rbp + 0x160]
0088F1A3  E8 98 42 9D FF                  call 0x140263440
0088F1A8  E9 90 F3 FF FF                  jmp 0x14088e53d
0088F1AD  39 74 24 48                     cmp dword ptr [rsp + 0x48], esi
0088F1B1  0F 84 DC FD FF FF               je 0x14088ef93
0088F1B7  44 8B 84 24 F0 00 00 00         mov r8d, dword ptr [rsp + 0xf0]
0088F1BF  48 8B 54 24 60                  mov rdx, qword ptr [rsp + 0x60]
0088F1C4  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
0088F1C9  E8 62 BF 13 00                  call 0x1409cb130
0088F1CE  44 8B E0                        mov r12d, eax
0088F1D1  83 F8 FE                        cmp eax, -2
0088F1D4  0F 85 FB F6 FF FF               jne 0x14088e8d5
0088F1DA  8B 44 24 40                     mov eax, dword ptr [rsp + 0x40]
0088F1DE  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
0088F1E6  FF C0                           inc eax
0088F1E8  44 8B 84 24 F0 00 00 00         mov r8d, dword ptr [rsp + 0xf0]
0088F1F0  4C 8B 4C 24 58                  mov r9, qword ptr [rsp + 0x58]
0088F1F5  4C 8B 54 24 70                  mov r10, qword ptr [rsp + 0x70]
0088F1FA  E9 80 F6 FF FF                  jmp 0x14088e87f
0088F1FF  48 8D 8D 60 01 00 00            lea rcx, [rbp + 0x160]
0088F206  E8 35 42 9D FF                  call 0x140263440
0088F20B  E9 A4 FD FF FF                  jmp 0x14088efb4
0088F210  49 8B 86 88 00 00 00            mov rax, qword ptr [r14 + 0x88]
0088F217  45 0F B7 86 F4 00 00 00         movzx r8d, word ptr [r14 + 0xf4]
0088F21F  48 F7 D8                        neg rax
0088F222  1B C9                           sbb ecx, ecx
0088F224  81 E1 00 00 00 80               and ecx, 0x80000000
0088F22A  8B D1                           mov edx, ecx
0088F22C  0F BA EA 1E                     bts edx, 0x1e
0088F230  49 39 B6 90 00 00 00            cmp qword ptr [r14 + 0x90], rsi
0088F237  0F 44 D1                        cmove edx, ecx
0088F23A  8B CA                           mov ecx, edx
0088F23C  0F BA E9 1C                     bts ecx, 0x1c
0088F240  49 39 B6 98 00 00 00            cmp qword ptr [r14 + 0x98], rsi
0088F247  0F 44 CA                        cmove ecx, edx
0088F24A  85 C9                           test ecx, ecx
0088F24C  0F 85 A5 00 00 00               jne 0x14088f2f7
0088F252  B8 FF DF FF FF                  mov eax, 0xffffdfff
0088F257  66 44 23 C0                     and r8w, ax
0088F25B  66 45 89 86 F4 00 00 00         mov word ptr [r14 + 0xf4], r8w
0088F263  E9 3B F4 FF FF                  jmp 0x14088e6a3
0088F268  8B FE                           mov edi, esi
0088F26A  E9 AF F5 FF FF                  jmp 0x14088e81e
0088F26F  41 0F BA E1 1D                  bt r9d, 0x1d
0088F274  0F 82 58 F5 FF FF               jb 0x14088e7d2
0088F27A  E9 5A F3 FF FF                  jmp 0x14088e5d9
0088F27F  49 8B CC                        mov rcx, r12
0088F282  E8 49 6B 9D FF                  call 0x140265dd0
0088F287  E9 8F FC FF FF                  jmp 0x14088ef1b
0088F28C  49 8D 8F 38 FA FF FF            lea rcx, [r15 - 0x5c8]
0088F293  49 89 4D 18                     mov qword ptr [r13 + 0x18], rcx
0088F297  E9 90 F4 FF FF                  jmp 0x14088e72c
0088F29C  48 8D 4B F0                     lea rcx, [rbx - 0x10]
0088F2A0  E8 9B 41 9D FF                  call 0x140263440
0088F2A5  E9 4F FC FF FF                  jmp 0x14088eef9
0088F2AA  48 8D 8D 60 01 00 00            lea rcx, [rbp + 0x160]
0088F2B1  E8 8A 41 9D FF                  call 0x140263440
0088F2B6  E9 7C FC FF FF                  jmp 0x14088ef37
0088F2BB  E8 10 6B 9D FF                  call 0x140265dd0
0088F2C0  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
0088F2C5  E9 C2 FB FF FF                  jmp 0x14088ee8c
0088F2CA  48 8D 8D 60 01 00 00            lea rcx, [rbp + 0x160]
0088F2D1  E8 6A 41 9D FF                  call 0x140263440
0088F2D6  E9 4A FD FF FF                  jmp 0x14088f025
0088F2DB  E8 F0 6A 9D FF                  call 0x140265dd0
0088F2E0  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
0088F2E5  E9 B6 FD FF FF                  jmp 0x14088f0a0
0088F2EA  49 8B CC                        mov rcx, r12
0088F2ED  E8 DE 6A 9D FF                  call 0x140265dd0
0088F2F2  E9 B1 F2 FF FF                  jmp 0x14088e5a8
0088F2F7  BF 00 20 00 00                  mov edi, 0x2000
0088F2FC  49 8B D6                        mov rdx, r14
0088F2FF  66 44 0B C7                     or r8w, di
0088F303  48 8B CD                        mov rcx, rbp
0088F306  66 45 89 86 F4 00 00 00         mov word ptr [r14 + 0xf4], r8w
0088F30E  66 41 FF 46 E2                  inc word ptr [r14 - 0x1e]
0088F313  E8 18 35 09 00                  call 0x140922830
0088F318  0F B6 BC 24 F0 00 00 00         movzx edi, byte ptr [rsp + 0xf0]
0088F320  E9 7E F3 FF FF                  jmp 0x14088e6a3
0088F325  48 8B BD 68 01 00 00            mov rdi, qword ptr [rbp + 0x168]
0088F32C  48 8B C3                        mov rax, rbx
0088F32F  F0 48 0F C1 47 18               lock xadd qword ptr [rdi + 0x18], rax
0088F335  24 06                           and al, 6
0088F337  3C 02                           cmp al, 2
0088F339  0F 85 17 FA FF FF               jne 0x14088ed56
0088F33F  48 8D 4F 18                     lea rcx, [rdi + 0x18]
0088F343  E8 88 6A 9D FF                  call 0x140265dd0
0088F348  E9 09 FA FF FF                  jmp 0x14088ed56
0088F34D  BA 20 00 00 00                  mov edx, 0x20
0088F352  B8 01 00 00 00                  mov eax, 1
0088F357  41 2B D4                        sub edx, r12d
0088F35A  44 3B C2                        cmp r8d, edx
0088F35D  41 0F 42 D0                     cmovb edx, r8d
0088F361  8B CA                           mov ecx, edx
0088F363  D3 E0                           shl eax, cl
0088F365  41 8B CC                        mov ecx, r12d
0088F368  FF C8                           dec eax
0088F36A  D3 E0                           shl eax, cl
0088F36C  F7 D0                           not eax
0088F36E  F0 41 21 01                     lock and dword ptr [r9], eax
0088F372  44 2B C2                        sub r8d, edx
0088F375  49 83 C1 04                     add r9, 4
0088F379  E9 0D FA FF FF                  jmp 0x14088ed8b
0088F37E  41 8B C0                        mov eax, r8d
0088F381  48 C1 E8 05                     shr rax, 5
0088F385  E9 F2 9E 28 00                  jmp 0x140b1927c
0088F38A  49 8B CE                        mov rcx, r14
0088F38D  E8 22 10 00 00                  call 0x1408903b4
0088F392  E9 19 F3 FF FF                  jmp 0x14088e6b0
0088F397  49 8B CE                        mov rcx, r14
0088F39A  E8 F1 DF EB FF                  call 0x14074d390
0088F39F  E9 2C F3 FF FF                  jmp 0x14088e6d0
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0088EC77(__int64 a1, int a2, __int64 a3, int a4)
{
    __int64 result;
    unsigned int v_stack_p100;
    unsigned int v_stack_p108;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned int v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned int v_stack_p68;
    unsigned int v_stack_p6C;
    unsigned __int64 v_stack_p70;
    unsigned int v_stack_p78;
    unsigned __int64 v_stack_p80;
    unsigned __int64 v_stack_p88;
    unsigned int v_stack_pF0;
    unsigned int v_stack_pF8;

    result = ExfTryToWakePushLock(v_rdi, a2, a3, a4);
}
```

## 5. (Beta) C Style

```c
int64_t sub_0088EC77(int64_t Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    uint32_t v_stack_p100;
    uint32_t v_stack_p108;
    uint32_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p40;
    uint64_t v_stack_p48;
    uint32_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_p60;
    uint32_t v_stack_p68;
    uint32_t v_stack_p6C;
    uint64_t v_stack_p70;
    uint32_t v_stack_p78;
    uint64_t v_stack_p80;
    uint64_t v_stack_p88;
    uint32_t v_stack_pF0;
    uint32_t v_stack_pF8;

    result = ExfTryToWakePushLock(local_rdi, Arg2, Arg3, Arg4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0088EC77&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
