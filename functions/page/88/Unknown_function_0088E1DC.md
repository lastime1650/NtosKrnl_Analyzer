# sub_0088E1DC

- RVA: `0x0088E1DC`–`0x0088EC66` (길이 `2,698` bytes)
- VA: `0x000000014088E1DC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007D540`
- 디코드: `599`개 명령, `2,698/2,698` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **39**; 고유 호출 대상: **16**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0088E242` → [PsGetProcessInheritedFromUniqueProcessId](../../text/45/PsGetProcessInheritedFromUniqueProcessId_function_0045D350.md) (function, `0x0045D350`)
- `0x0088E270` → [PspChargeProcessWakeCounter](PspChargeProcessWakeCounter_function_0088D2A0.md) (function, `0x0088D2A0`)
- `0x0088E317` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0088E331` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x0088E358` → [AlpcpCaptureMessageDataSafe](AlpcpCaptureMessageDataSafe_function_0088F3B0.md) (function, `0x0088F3B0`)
- `0x0088E373` → [AlpcpExposeViewAttributeInSenderContext](AlpcpExposeViewAttributeInSenderContext_function_0088F600.md) (function, `0x0088F600`)
- `0x0088E3F1` → [AlpcpLogSendMessage](../89/AlpcpLogSendMessage_function_008903B4.md) (function, `0x008903B4`)
- `0x0088E41F` → [AlpcpCaptureMessageDataSafe](AlpcpCaptureMessageDataSafe_function_0088F3B0.md) (function, `0x0088F3B0`)
- `0x0088E43A` → [AlpcpExposeViewAttributeInSenderContext](AlpcpExposeViewAttributeInSenderContext_function_0088F600.md) (function, `0x0088F600`)
- `0x0088E453` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0088E46C` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x0088E4DB` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0088E4FD` → [AlpcpUnlockMessage](../89/AlpcpUnlockMessage_function_00897AE0.md) (function, `0x00897AE0`)
- `0x0088E51B` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x0088E524` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0088E544` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0088E54C` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x0088E57E` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x0088E587` → [AlpcpReleaseDirectAttribute](../../text/47/AlpcpReleaseDirectAttribute_function_00474804.md) (function, `0x00474804`)
- `0x0088E5AB` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0088E5E5` → [AlpcpCaptureMessageDataSafe](AlpcpCaptureMessageDataSafe_function_0088F3B0.md) (function, `0x0088F3B0`)
- `0x0088E600` → [AlpcpExposeViewAttributeInSenderContext](AlpcpExposeViewAttributeInSenderContext_function_0088F600.md) (function, `0x0088F600`)
- `0x0088E619` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0088E632` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x0088E69B` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0088E6DB` → [AlpcpUnlockMessage](../89/AlpcpUnlockMessage_function_00897AE0.md) (function, `0x00897AE0`)
- `0x0088E6F9` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x0088E702` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0088E8B6` → [AlpcpAllocateFromBitmap](../9C/AlpcpAllocateFromBitmap_function_009CB130.md) (function, `0x009CB130`)
- `0x0088E9BB` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0088E9F9` → [AlpcpExposeAttributes](../89/AlpcpExposeAttributes_function_00897630.md) (function, `0x00897630`)
- `0x0088EA46` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0088EA61` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x0088EAEB` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0088EB79` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0088EB92` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x0088EBFB` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0088EC29` → [PsGetProcessInheritedFromUniqueProcessId](../../text/45/PsGetProcessInheritedFromUniqueProcessId_function_0045D350.md) (function, `0x0045D350`)
- `0x0088EC55` → [PspChargeProcessWakeCounter](PspChargeProcessWakeCounter_function_0088D2A0.md) (function, `0x0088D2A0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0088E21E` → RVA `0x00FC50BC` (`ALMOSTRO`; read)
- `0x0088E281` → RVA `0x00FC6B78` (`ALMOSTRO`; read)
- `0x0088E3E1` → RVA `0x00E66D00` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **26**
  - `0x0088E242` → [PsGetProcessInheritedFromUniqueProcessId](../../text/45/PsGetProcessInheritedFromUniqueProcessId_function_0045D350.md) (`PAGE` → `.text`)
  - `0x0088E317` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x0088E331` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x0088E453` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x0088E46C` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x0088E4DB` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0088E51B` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x0088E524` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0088E544` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0088E54C` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x0088E57E` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (`PAGE` → `.text`)
  - `0x0088E587` → [AlpcpReleaseDirectAttribute](../../text/47/AlpcpReleaseDirectAttribute_function_00474804.md) (`PAGE` → `.text`)
  - `0x0088E5AB` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0088E619` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x0088E632` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x0088E69B` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0088E6F9` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x0088E702` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0088E9BB` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0088EA46` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x0088EA61` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x0088EAEB` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0088EB79` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x0088EB92` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x0088EBFB` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0088EC29` → [PsGetProcessInheritedFromUniqueProcessId](../../text/45/PsGetProcessInheritedFromUniqueProcessId_function_0045D350.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **34**
  - `0x0088E20B` → [sub_0088EC77 + 0x47](Unknown_function_0088EC77.md) (`tail-transfer`)
  - `0x0088E24A` → [sub_0088EC77 + 0x22D](Unknown_function_0088EC77.md) (`tail-transfer`)
  - `0x0088E385` → [sub_0088EC77 + 0x1B7](Unknown_function_0088EC77.md) (`tail-transfer`)
  - `0x0088E3C1` → [sub_0088EC77 + 0x1B7](Unknown_function_0088EC77.md) (`tail-transfer`)
  - `0x0088E406` → [sub_0088EC77 + 0x24F](Unknown_function_0088EC77.md) (`tail-transfer`)
  - `0x0088E4D2` → [sub_0088EC77](Unknown_function_0088EC77.md) (`tail-transfer`)
  - `0x0088E537` → [sub_0088EC77 + 0x525](Unknown_function_0088EC77.md) (`tail-transfer`)
  - `0x0088E5A2` → [sub_0088EC77 + 0x673](Unknown_function_0088EC77.md) (`tail-transfer`)
  - `0x0088E5B4` → [sub_0088EC77 + 0x27](Unknown_function_0088EC77.md) (`tail-transfer`)
  - `0x0088E692` → [sub_0088EC77 + 0x16D](Unknown_function_0088EC77.md) (`tail-transfer`)
  - `0x0088E6AA` → [sub_0088EC77 + 0x713](Unknown_function_0088EC77.md) (`tail-transfer`)
  - `0x0088E6B3` → [sub_0088EC77 + 0xD](Unknown_function_0088EC77.md) (`tail-transfer`)
  - `0x0088E6CA` → [sub_0088EC77 + 0x720](Unknown_function_0088EC77.md) (`tail-transfer`)
  - `0x0088E70B` → [sub_0088EC77 + 0x329](Unknown_function_0088EC77.md) (`tail-transfer`)
  - `0x0088E714` → [sub_0088EC77 + 0x393](Unknown_function_0088EC77.md) (`tail-transfer`)
  - `0x0088E71D` → [sub_0088EC77 + 0x35B](Unknown_function_0088EC77.md) (`tail-transfer`)
  - `0x0088E7CC` → [sub_0088EC77 + 0x5F8](Unknown_function_0088EC77.md) (`tail-transfer`)
  - `0x0088E7E1` → [sub_0088EC77 + 0x5F1](Unknown_function_0088EC77.md) (`tail-transfer`)
  - `0x0088E80B` → [sub_0088EC77 + 0x3F](Unknown_function_0088EC77.md) (`tail-transfer`)
  - `0x0088E8C1` → [sub_0088EC77 + 0x563](Unknown_function_0088EC77.md) (`tail-transfer`)
  - `0x0088E8CA` → [sub_0088EC77 + 0x536](Unknown_function_0088EC77.md) (`tail-transfer`)
  - `0x0088E8E1` → [sub_0088EC77 + 0x31C](Unknown_function_0088EC77.md) (`tail-transfer`)
  - `0x0088E90D` → [sub_0088EC77 + 0x441](Unknown_function_0088EC77.md) (`tail-transfer`)
  - `0x0088E97B` → [sub_0088EC77 + 0x1A7](Unknown_function_0088EC77.md) (`tail-transfer`)
  - `0x0088E988` → [sub_0088EC77 + 0x242](Unknown_function_0088EC77.md) (`tail-transfer`)
  - `0x0088E9AF` → [sub_0088EC77 + 0x13F](Unknown_function_0088EC77.md) (`tail-transfer`)
  - `0x0088EA2D` → [sub_0088EC77 + 0xE8](Unknown_function_0088EC77.md) (`tail-transfer`)
  - `0x0088EA95` → [sub_0088EC77 + 0x62](Unknown_function_0088EC77.md) (`tail-transfer`)
  - `0x0088EAD6` → [sub_0088EC77 + 0x41A](Unknown_function_0088EC77.md) (`tail-transfer`)
  - `0x0088EAE5` → [sub_0088EC77 + 0x4F8](Unknown_function_0088EC77.md) (`tail-transfer`)
  - `0x0088EB44` → [sub_0088EC77 + 0x17A](Unknown_function_0088EC77.md) (`tail-transfer`)
  - `0x0088EB52` → [sub_0088EC77 + 0x599](Unknown_function_0088EC77.md) (`tail-transfer`)
  - `0x0088EBF2` → [sub_0088EC77 + 0x235](Unknown_function_0088EC77.md) (`tail-transfer`)
  - `0x0088EC31` → [sub_0088EC77 + 0x4F0](Unknown_function_0088EC77.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0088E1DC  48 89 9C 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rbx
0088E1E4  48 89 BC 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rdi
0088E1EC  0F 85 F3 00 00 00               jne 0x14088e2e5
0088E1F2  48 8B 5D 18                     mov rbx, qword ptr [rbp + 0x18]
0088E1F6  F6 C3 01                        test bl, 1
0088E1F9  0F 85 E6 00 00 00               jne 0x14088e2e5
0088E1FF  48 85 DB                        test rbx, rbx
0088E202  0F 84 DD 00 00 00               je 0x14088e2e5
0088E208  45 85 E4                        test r12d, r12d
0088E20B  0F 84 AD 0A 00 00               je 0x14088ecbe
0088E211  BF 01 00 00 00                  mov edi, 1
0088E216  85 D2                           test edx, edx
0088E218  0F 85 EF 09 00 00               jne 0x14088ec0d
0088E21E  8B 05 98 6E 73 00               mov eax, dword ptr [rip + 0x736e98]
0088E224  40 84 C7                        test dil, al
0088E227  74 0F                           je 0x14088e238
0088E229  A8 02                           test al, 2
0088E22B  BF 03 00 00 00                  mov edi, 3
0088E230  B8 03 00 00 80                  mov eax, 0x80000003
0088E235  0F 45 F8                        cmovne edi, eax
0088E238  45 8B BE 08 01 00 00            mov r15d, dword ptr [r14 + 0x108]
0088E23F  48 8B CB                        mov rcx, rbx
0088E242  E8 09 F1 BC FF                  call 0x14045d350
0088E247  48 85 C0                        test rax, rax
0088E24A  0F 84 54 0C 00 00               je 0x14088eea4
0088E250  48 89 74 24 30                  mov qword ptr [rsp + 0x30], rsi
0088E255  45 8B CF                        mov r9d, r15d
0088E258  C6 44 24 28 01                  mov byte ptr [rsp + 0x28], 1
0088E25D  41 B8 02 00 00 00               mov r8d, 2
0088E263  8B D7                           mov edx, edi
0088E265  C7 44 24 20 01 00 00 00         mov dword ptr [rsp + 0x20], 1
0088E26D  48 8B CB                        mov rcx, rbx
0088E270  E8 2B F0 FF FF                  call 0x14088d2a0
0088E275  44 8B 7C 24 50                  mov r15d, dword ptr [rsp + 0x50]
0088E27A  49 89 86 D0 00 00 00            mov qword ptr [r14 + 0xd0], rax
0088E281  39 35 F1 88 73 00               cmp dword ptr [rip + 0x7388f1], esi
0088E287  74 5C                           je 0x14088e2e5
0088E289  45 85 E4                        test r12d, r12d
0088E28C  74 57                           je 0x14088e2e5
0088E28E  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0088E297  0F B6 88 04 02 00 00            movzx ecx, byte ptr [rax + 0x204]
0088E29E  84 C9                           test cl, cl
0088E2A0  0F 84 79 09 00 00               je 0x14088ec1f
0088E2A6  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0088E2AF  48 8B 88 20 02 00 00            mov rcx, qword ptr [rax + 0x220]
0088E2B6  8B 81 88 00 00 00               mov eax, dword ptr [rcx + 0x88]
0088E2BC  25 80 07 00 00                  and eax, 0x780
0088E2C1  3D 80 01 00 00                  cmp eax, 0x180
0088E2C6  0F 84 53 09 00 00               je 0x14088ec1f
0088E2CC  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0088E2D5  0F B6 88 BE 03 00 00            movzx ecx, byte ptr [rax + 0x3be]
0088E2DC  80 F9 03                        cmp cl, 3
0088E2DF  0F 84 3A 09 00 00               je 0x14088ec1f
0088E2E5  41 8B 45 30                     mov eax, dword ptr [r13 + 0x30]
0088E2E9  A8 08                           test al, 8
0088E2EB  0F 85 22 01 00 00               jne 0x14088e413
0088E2F1  48 8D BD E8 00 00 00            lea rdi, [rbp + 0xe8]
0088E2F8  48 C7 C3 FF FF FF FF            mov rbx, 0xffffffffffffffff
0088E2FF  48 39 3F                        cmp qword ptr [rdi], rdi
0088E302  0F 84 A8 02 00 00               je 0x14088e5b0
0088E308  4C 8D A5 E0 00 00 00            lea r12, [rbp + 0xe0]
0088E30F  45 33 C0                        xor r8d, r8d
0088E312  49 8B CC                        mov rcx, r12
0088E315  33 D2                           xor edx, edx
0088E317  E8 14 1F 98 FF                  call 0x140210230
0088E31C  F0 49 0F BA 2C 24 00            lock bts qword ptr [r12], 0
0088E323  4C 8B F8                        mov r15, rax
0088E326  73 0E                           jae 0x14088e336
0088E328  4D 8B C4                        mov r8, r12
0088E32B  48 8B D0                        mov rdx, rax
0088E32E  49 8B CC                        mov rcx, r12
0088E331  E8 5A 19 98 FF                  call 0x14020fc90
0088E336  4D 85 FF                        test r15, r15
0088E339  74 05                           je 0x14088e340
0088E33B  41 C6 47 0A 01                  mov byte ptr [r15 + 0xa], 1
0088E340  4C 8B 3F                        mov r15, qword ptr [rdi]
0088E343  4C 3B FF                        cmp r15, rdi
0088E346  0F 84 49 02 00 00               je 0x14088e595
0088E34C  49 39 B6 B0 00 00 00            cmp qword ptr [r14 + 0xb0], rsi
0088E353  74 0F                           je 0x14088e364
0088E355  49 8B CE                        mov rcx, r14
0088E358  E8 53 10 00 00                  call 0x14088f3b0
0088E35D  49 89 B6 B0 00 00 00            mov qword ptr [r14 + 0xb0], rsi
0088E364  49 39 B6 90 00 00 00            cmp qword ptr [r14 + 0x90], rsi
0088E36B  74 0B                           je 0x14088e378
0088E36D  49 8B D6                        mov rdx, r14
0088E370  48 8B CD                        mov rcx, rbp
0088E373  E8 88 12 00 00                  call 0x14088f600
0088E378  41 F7 46 28 00 02 00 00         test dword ptr [r14 + 0x28], 0x200
0088E380  BF 00 20 00 00                  mov edi, 0x2000
0088E385  0F 84 A3 0A 00 00               je 0x14088ee2e
0088E38B  49 8B 86 88 00 00 00            mov rax, qword ptr [r14 + 0x88]
0088E392  48 F7 D8                        neg rax
0088E395  1B C9                           sbb ecx, ecx
0088E397  81 E1 00 00 00 80               and ecx, 0x80000000
0088E39D  8B D1                           mov edx, ecx
0088E39F  0F BA EA 1E                     bts edx, 0x1e
0088E3A3  49 39 B6 90 00 00 00            cmp qword ptr [r14 + 0x90], rsi
0088E3AA  0F 44 D1                        cmove edx, ecx
0088E3AD  8B CA                           mov ecx, edx
0088E3AF  0F BA E9 1C                     bts ecx, 0x1c
0088E3B3  49 39 B6 98 00 00 00            cmp qword ptr [r14 + 0x98], rsi
0088E3BA  0F 44 CA                        cmove ecx, edx
0088E3BD  41 85 4F F8                     test dword ptr [r15 - 8], ecx
0088E3C1  0F 85 67 0A 00 00               jne 0x14088ee2e
0088E3C7  B8 FF DF FF FF                  mov eax, 0xffffdfff
0088E3CC  66 41 21 86 F4 00 00 00         and word ptr [r14 + 0xf4], ax
0088E3D4  66 41 FF 46 E2                  inc word ptr [r14 - 0x1e]
0088E3D9  49 8D 46 E2                     lea rax, [r14 - 0x1e]
0088E3DD  41 09 7E 28                     or dword ptr [r14 + 0x28], edi
0088E3E1  40 38 35 18 89 5D 00            cmp byte ptr [rip + 0x5d8918], sil
0088E3E8  4D 89 77 F8                     mov qword ptr [r15 - 8], r14
0088E3EC  74 08                           je 0x14088e3f6
0088E3EE  49 8B CE                        mov rcx, r14
0088E3F1  E8 BE 1F 00 00                  call 0x1408903b4
0088E3F6  49 8B 0F                        mov rcx, qword ptr [r15]
0088E3F9  4C 39 79 08                     cmp qword ptr [rcx + 8], r15
0088E3FD  75 0D                           jne 0x14088e40c
0088E3FF  49 8B 47 08                     mov rax, qword ptr [r15 + 8]
0088E403  4C 39 38                        cmp qword ptr [rax], r15
0088E406  0F 84 BA 0A 00 00               je 0x14088eec6
0088E40C  B9 03 00 00 00                  mov ecx, 3
0088E411  CD 29                           int 0x29
0088E413  49 39 B6 B0 00 00 00            cmp qword ptr [r14 + 0xb0], rsi
0088E41A  74 0F                           je 0x14088e42b
0088E41C  49 8B CE                        mov rcx, r14
0088E41F  E8 8C 0F 00 00                  call 0x14088f3b0
0088E424  49 89 B6 B0 00 00 00            mov qword ptr [r14 + 0xb0], rsi
0088E42B  49 39 B6 90 00 00 00            cmp qword ptr [r14 + 0x90], rsi
0088E432  74 0B                           je 0x14088e43f
0088E434  49 8B D6                        mov rdx, r14
0088E437  48 8B CD                        mov rcx, rbp
0088E43A  E8 C1 11 00 00                  call 0x14088f600
0088E43F  66 41 FF 46 E2                  inc word ptr [r14 - 0x1e]
0088E444  48 8D BD C8 00 00 00            lea rdi, [rbp + 0xc8]
0088E44B  48 8B CF                        mov rcx, rdi
0088E44E  45 33 C0                        xor r8d, r8d
0088E451  33 D2                           xor edx, edx
0088E453  E8 D8 1D 98 FF                  call 0x140210230
0088E458  F0 48 0F BA 2F 00               lock bts qword ptr [rdi], 0
0088E45E  48 8B D8                        mov rbx, rax
0088E461  73 0E                           jae 0x14088e471
0088E463  4C 8B C7                        mov r8, rdi
0088E466  48 8B D0                        mov rdx, rax
0088E469  48 8B CF                        mov rcx, rdi
0088E46C  E8 1F 18 98 FF                  call 0x14020fc90
0088E471  48 85 DB                        test rbx, rbx
0088E474  74 04                           je 0x14088e47a
0088E476  C6 43 0A 01                     mov byte ptr [rbx + 0xa], 1
0088E47A  41 8B 46 28                     mov eax, dword ptr [r14 + 0x28]
0088E47E  48 C7 C3 FF FF FF FF            mov rbx, 0xffffffffffffffff
0088E485  49 89 6E 10                     mov qword ptr [r14 + 0x10], rbp
0088E489  83 E0 87                        and eax, 0xffffff87
0088E48C  8B 8D A0 01 00 00               mov ecx, dword ptr [rbp + 0x1a0]
0088E492  83 E1 06                        and ecx, 6
0088E495  C1 E1 02                        shl ecx, 2
0088E498  0B C8                           or ecx, eax
0088E49A  83 E1 FC                        and ecx, 0xfffffffc
0088E49D  83 C9 04                        or ecx, 4
0088E4A0  41 89 4E 28                     mov dword ptr [r14 + 0x28], ecx
0088E4A4  48 8D 8D D0 00 00 00            lea rcx, [rbp + 0xd0]
0088E4AB  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
0088E4AF  49 89 46 08                     mov qword ptr [r14 + 8], rax
0088E4B3  49 89 0E                        mov qword ptr [r14], rcx
0088E4B6  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
0088E4BA  4C 89 30                        mov qword ptr [rax], r14
0088E4BD  4C 89 71 08                     mov qword ptr [rcx + 8], r14
0088E4C1  FF 85 CC 01 00 00               inc dword ptr [rbp + 0x1cc]
0088E4C7  F0 48 0F C1 1F                  lock xadd qword ptr [rdi], rbx
0088E4CC  80 E3 06                        and bl, 6
0088E4CF  80 FB 02                        cmp bl, 2
0088E4D2  0F 84 9F 07 00 00               je 0x14088ec77
0088E4D8  48 8B CF                        mov rcx, rdi
0088E4DB  E8 20 31 A5 FF                  call 0x1402e1600
0088E4E0  49 8B 86 A0 00 00 00            mov rax, qword ptr [r14 + 0xa0]
0088E4E7  49 8B CE                        mov rcx, r14
0088E4EA  49 89 45 28                     mov qword ptr [r13 + 0x28], rax
0088E4EE  41 81 66 28 FF FF FE FF         and dword ptr [r14 + 0x28], 0xfffeffff
0088E4F6  49 89 B6 A0 00 00 00            mov qword ptr [r14 + 0xa0], rsi
0088E4FD  E8 DE 95 00 00                  call 0x140897ae0
0088E502  48 8B 9C 24 80 00 00 00         mov rbx, qword ptr [rsp + 0x80]
0088E50A  B8 11 00 00 00                  mov eax, 0x11
0088E50F  F0 48 0F B1 73 F0               lock cmpxchg qword ptr [rbx - 0x10], rsi
0088E515  74 09                           je 0x14088e520
0088E517  48 8D 4B F0                     lea rcx, [rbx - 0x10]
0088E51B  E8 20 4F 9D FF                  call 0x140263440
0088E520  48 8D 4B F0                     lea rcx, [rbx - 0x10]
0088E524  E8 D7 30 A5 FF                  call 0x1402e1600
0088E529  B8 11 00 00 00                  mov eax, 0x11
0088E52E  F0 48 0F B1 B5 60 01 00 00      lock cmpxchg qword ptr [rbp + 0x160], rsi
0088E537  0F 85 5F 0C 00 00               jne 0x14088f19c
0088E53D  48 8D 8D 60 01 00 00            lea rcx, [rbp + 0x160]
0088E544  E8 B7 30 A5 FF                  call 0x1402e1600
0088E549  48 8B CD                        mov rcx, rbp
0088E54C  E8 FF AD A6 FF                  call 0x1402f9350
0088E551  49 89 75 20                     mov qword ptr [r13 + 0x20], rsi
0088E555  45 85 FF                        test r15d, r15d
0088E558  0F 85 CE 01 00 00               jne 0x14088e72c
0088E55E  39 B4 24 00 01 00 00            cmp dword ptr [rsp + 0x100], esi
0088E565  0F 85 C1 01 00 00               jne 0x14088e72c
0088E56B  49 8B 4D 28                     mov rcx, qword ptr [r13 + 0x28]
0088E56F  48 83 F9 04                     cmp rcx, 4
0088E573  72 17                           jb 0x14088e58c
0088E575  48 83 E1 FC                     and rcx, 0xfffffffffffffffc
0088E579  45 33 C0                        xor r8d, r8d
0088E57C  33 D2                           xor edx, edx
0088E57E  E8 8D 0D AB FF                  call 0x14033f310
0088E583  49 8B 4D 28                     mov rcx, qword ptr [r13 + 0x28]
0088E587  E8 78 62 BE FF                  call 0x140474804
0088E58C  49 89 75 28                     mov qword ptr [r13 + 0x28], rsi
0088E590  E9 97 01 00 00                  jmp 0x14088e72c
0088E595  48 8B C3                        mov rax, rbx
0088E598  F0 49 0F C1 04 24               lock xadd qword ptr [r12], rax
0088E59E  24 06                           and al, 6
0088E5A0  3C 02                           cmp al, 2
0088E5A2  0F 84 42 0D 00 00               je 0x14088f2ea
0088E5A8  49 8B CC                        mov rcx, r12
0088E5AB  E8 50 30 A5 FF                  call 0x1402e1600
0088E5B0  48 39 75 20                     cmp qword ptr [rbp + 0x20], rsi
0088E5B4  0F 84 E4 06 00 00               je 0x14088ec9e
0088E5BA  41 B4 01                        mov r12b, 1
0088E5BD  89 74 24 68                     mov dword ptr [rsp + 0x68], esi
0088E5C1  4C 8B BD 68 01 00 00            mov r15, qword ptr [rbp + 0x168]
0088E5C8  44 89 A4 24 F8 00 00 00         mov dword ptr [rsp + 0xf8], r12d
0088E5D0  4D 85 FF                        test r15, r15
0088E5D3  0F 85 76 01 00 00               jne 0x14088e74f
0088E5D9  49 39 B6 B0 00 00 00            cmp qword ptr [r14 + 0xb0], rsi
0088E5E0  74 0F                           je 0x14088e5f1
0088E5E2  49 8B CE                        mov rcx, r14
0088E5E5  E8 C6 0D 00 00                  call 0x14088f3b0
0088E5EA  49 89 B6 B0 00 00 00            mov qword ptr [r14 + 0xb0], rsi
0088E5F1  49 39 B6 90 00 00 00            cmp qword ptr [r14 + 0x90], rsi
0088E5F8  74 0B                           je 0x14088e605
0088E5FA  49 8B D6                        mov rdx, r14
0088E5FD  48 8B CD                        mov rcx, rbp
0088E600  E8 FB 0F 00 00                  call 0x14088f600
0088E605  66 41 FF 46 E2                  inc word ptr [r14 - 0x1e]
0088E60A  48 8D BD 88 00 00 00            lea rdi, [rbp + 0x88]
0088E611  48 8B CF                        mov rcx, rdi
0088E614  45 33 C0                        xor r8d, r8d
0088E617  33 D2                           xor edx, edx
0088E619  E8 12 1C 98 FF                  call 0x140210230
0088E61E  F0 48 0F BA 2F 00               lock bts qword ptr [rdi], 0
0088E624  4C 8B F8                        mov r15, rax
0088E627  73 0E                           jae 0x14088e637
0088E629  4C 8B C7                        mov r8, rdi
0088E62C  48 8B D0                        mov rdx, rax
0088E62F  48 8B CF                        mov rcx, rdi
0088E632  E8 59 16 98 FF                  call 0x14020fc90
0088E637  4D 85 FF                        test r15, r15
0088E63A  74 05                           je 0x14088e641
0088E63C  41 C6 47 0A 01                  mov byte ptr [r15 + 0xa], 1
0088E641  41 8B 46 28                     mov eax, dword ptr [r14 + 0x28]
0088E645  49 89 6E 10                     mov qword ptr [r14 + 0x10], rbp
0088E649  83 E0 87                        and eax, 0xffffff87
0088E64C  8B 8D A0 01 00 00               mov ecx, dword ptr [rbp + 0x1a0]
0088E652  83 E1 06                        and ecx, 6
0088E655  C1 E1 02                        shl ecx, 2
0088E658  0B C8                           or ecx, eax
0088E65A  83 E1 F9                        and ecx, 0xfffffff9
0088E65D  83 C9 01                        or ecx, 1
0088E660  41 89 4E 28                     mov dword ptr [r14 + 0x28], ecx
0088E664  48 8D 8D 90 00 00 00            lea rcx, [rbp + 0x90]
0088E66B  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
0088E66F  49 89 46 08                     mov qword ptr [r14 + 8], rax
0088E673  49 89 0E                        mov qword ptr [r14], rcx
0088E676  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
0088E67A  4C 89 30                        mov qword ptr [rax], r14
0088E67D  4C 89 71 08                     mov qword ptr [rcx + 8], r14
0088E681  FF 85 C0 01 00 00               inc dword ptr [rbp + 0x1c0]
0088E687  F0 48 0F C1 1F                  lock xadd qword ptr [rdi], rbx
0088E68C  80 E3 06                        and bl, 6
0088E68F  80 FB 02                        cmp bl, 2
0088E692  0F 84 4C 07 00 00               je 0x14088ede4
0088E698  48 8B CF                        mov rcx, rdi
0088E69B  E8 60 2F A5 FF                  call 0x1402e1600
0088E6A0  40 32 FF                        xor dil, dil
0088E6A3  40 38 35 56 86 5D 00            cmp byte ptr [rip + 0x5d8656], sil
0088E6AA  0F 85 DA 0C 00 00               jne 0x14088f38a
0088E6B0  40 84 FF                        test dil, dil
0088E6B3  0F 85 CB 05 00 00               jne 0x14088ec84
0088E6B9  44 8B 7C 24 50                  mov r15d, dword ptr [rsp + 0x50]
0088E6BE  45 85 FF                        test r15d, r15d
0088E6C1  74 0D                           je 0x14088e6d0
0088E6C3  40 38 35 36 86 5D 00            cmp byte ptr [rip + 0x5d8636], sil
0088E6CA  0F 85 C7 0C 00 00               jne 0x14088f397
0088E6D0  41 81 66 28 FF FF FE FF         and dword ptr [r14 + 0x28], 0xfffeffff
0088E6D8  49 8B CE                        mov rcx, r14
0088E6DB  E8 00 94 00 00                  call 0x140897ae0
0088E6E0  48 8B 9C 24 80 00 00 00         mov rbx, qword ptr [rsp + 0x80]
0088E6E8  B8 11 00 00 00                  mov eax, 0x11
0088E6ED  F0 48 0F B1 73 F0               lock cmpxchg qword ptr [rbx - 0x10], rsi
0088E6F3  74 09                           je 0x14088e6fe
0088E6F5  48 8D 4B F0                     lea rcx, [rbx - 0x10]
0088E6F9  E8 42 4D 9D FF                  call 0x140263440
0088E6FE  48 8D 4B F0                     lea rcx, [rbx - 0x10]
0088E702  E8 F9 2E A5 FF                  call 0x1402e1600
0088E707  39 74 24 68                     cmp dword ptr [rsp + 0x68], esi
0088E70B  0F 85 8F 08 00 00               jne 0x14088efa0
0088E711  45 84 E4                        test r12b, r12b
0088E714  0F 84 F0 08 00 00               je 0x14088f00a
0088E71A  45 85 FF                        test r15d, r15d
0088E71D  0F 84 AF 08 00 00               je 0x14088efd2
0088E723  41 C6 45 3A 01                  mov byte ptr [r13 + 0x3a], 1
0088E728  41 88 7D 3B                     mov byte ptr [r13 + 0x3b], dil
0088E72C  48 8B BC 24 A8 00 00 00         mov rdi, qword ptr [rsp + 0xa8]
0088E734  48 8B 9C 24 B0 00 00 00         mov rbx, qword ptr [rsp + 0xb0]
0088E73C  48 81 C4 B8 00 00 00            add rsp, 0xb8
0088E743  41 5F                           pop r15
0088E745  41 5E                           pop r14
0088E747  41 5D                           pop r13
0088E749  41 5C                           pop r12
0088E74B  5E                              pop rsi
0088E74C  5D                              pop rbp
0088E74D  C3                              ret
0088E74E  CC                              int3
0088E74F  44 8B 85 A0 01 00 00            mov r8d, dword ptr [rbp + 0x1a0]
0088E756  41 0F BA E0 10                  bt r8d, 0x10
0088E75B  0F 83 78 FE FF FF               jae 0x14088e5d9
0088E761  49 8B 86 88 00 00 00            mov rax, qword ptr [r14 + 0x88]
0088E768  48 F7 D8                        neg rax
0088E76B  48 89 B4 24 90 00 00 00         mov qword ptr [rsp + 0x90], rsi
0088E773  1B C9                           sbb ecx, ecx
0088E775  81 E1 00 00 00 80               and ecx, 0x80000000
0088E77B  8B D1                           mov edx, ecx
0088E77D  0F BA EA 1E                     bts edx, 0x1e
0088E781  49 39 B6 90 00 00 00            cmp qword ptr [r14 + 0x90], rsi
0088E788  0F 44 D1                        cmove edx, ecx
0088E78B  8B CA                           mov ecx, edx
0088E78D  0F BA E9 1C                     bts ecx, 0x1c
0088E791  49 39 B6 98 00 00 00            cmp qword ptr [r14 + 0x98], rsi
0088E798  0F 44 CA                        cmove ecx, edx
0088E79B  49 39 B6 A8 00 00 00            cmp qword ptr [r14 + 0xa8], rsi
0088E7A2  74 04                           je 0x14088e7a8
0088E7A4  0F BA E9 19                     bts ecx, 0x19
0088E7A8  45 8B 8F 94 00 00 00            mov r9d, dword ptr [r15 + 0x94]
0088E7AF  41 8B C1                        mov eax, r9d
0088E7B2  F7 D0                           not eax
0088E7B4  85 C1                           test ecx, eax
0088E7B6  0F 85 1D FE FF FF               jne 0x14088e5d9
0088E7BC  41 0F B7 86 F4 00 00 00         movzx eax, word ptr [r14 + 0xf4]
0088E7C4  25 FF 00 FF FF                  and eax, 0xffff00ff
0088E7C9  83 F8 05                        cmp eax, 5
0088E7CC  0F 84 9D 0A 00 00               je 0x14088f26f
0088E7D2  41 0F B7 96 F2 00 00 00         movzx edx, word ptr [r14 + 0xf2]
0088E7DA  41 C1 E8 0B                     shr r8d, 0xb
0088E7DE  45 85 C9                        test r9d, r9d
0088E7E1  0F 84 81 0A 00 00               je 0x14088f268
0088E7E7  49 8D 8E F0 00 00 00            lea rcx, [r14 + 0xf0]
0088E7EE  41 8B C0                        mov eax, r8d
0088E7F1  44 0F B7 49 02                  movzx r9d, word ptr [rcx + 2]
0088E7F6  F7 D0                           not eax
0088E7F8  83 E0 01                        and eax, 1
0088E7FB  4C 03 C9                        add r9, rcx
0088E7FE  8D 3C 85 04 00 00 00            lea edi, [rax*4 + 4]
0088E805  8D 4F FF                        lea ecx, [rdi - 1]
0088E808  4C 23 C9                        and r9, rcx
0088E80B  0F 85 A5 04 00 00               jne 0x14088ecb6
0088E811  8B FE                           mov edi, esi
0088E813  41 8B 87 98 00 00 00            mov eax, dword ptr [r15 + 0x98]
0088E81A  03 C7                           add eax, edi
0088E81C  03 D0                           add edx, eax
0088E81E  89 B4 24 08 01 00 00            mov dword ptr [rsp + 0x108], esi
0088E825  41 F6 C0 01                     test r8b, 1
0088E829  74 0E                           je 0x14088e839
0088E82B  83 C2 F0                        add edx, -0x10
0088E82E  C7 84 24 08 01 00 00 00 00 00 80  mov dword ptr [rsp + 0x108], 0x80000000
0088E839  4D 8B 4F 68                     mov r9, qword ptr [r15 + 0x68]
0088E83D  44 8D 42 3F                     lea r8d, [rdx + 0x3f]
0088E841  41 8B 87 88 00 00 00            mov eax, dword ptr [r15 + 0x88]
0088E848  41 BC FF FF FF FF               mov r12d, 0xffffffff
0088E84E  49 8B 4F 60                     mov rcx, qword ptr [r15 + 0x60]
0088E852  48 C1 E8 05                     shr rax, 5
0088E856  41 C1 E8 06                     shr r8d, 6
0088E85A  48 C1 E9 02                     shr rcx, 2
0088E85E  44 89 84 24 F0 00 00 00         mov dword ptr [rsp + 0xf0], r8d
0088E866  4D 8D 14 81                     lea r10, [r9 + rax*4]
0088E86A  4C 89 4C 24 58                  mov qword ptr [rsp + 0x58], r9
0088E86F  4C 89 54 24 70                  mov qword ptr [rsp + 0x70], r10
0088E874  48 8B C6                        mov rax, rsi
0088E877  48 89 8C 24 88 00 00 00         mov qword ptr [rsp + 0x88], rcx
0088E87F  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
0088E883  48 3B C1                        cmp rax, rcx
0088E886  73 55                           jae 0x14088e8dd
0088E888  41 8B 97 8C 00 00 00            mov edx, dword ptr [r15 + 0x8c]
0088E88F  8B C2                           mov eax, edx
0088E891  83 E0 E0                        and eax, 0xffffffe0
0088E894  41 3B 97 88 00 00 00            cmp edx, dword ptr [r15 + 0x88]
0088E89B  49 8B D2                        mov rdx, r10
0088E89E  0F 43 C6                        cmovae eax, esi
0088E8A1  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
0088E8A6  48 C1 E8 05                     shr rax, 5
0088E8AA  49 8D 04 81                     lea rax, [r9 + rax*4]
0088E8AE  48 8B C8                        mov rcx, rax
0088E8B1  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
0088E8B6  E8 75 C8 13 00                  call 0x1409cb130
0088E8BB  44 8B E0                        mov r12d, eax
0088E8BE  83 F8 FE                        cmp eax, -2
0088E8C1  0F 84 13 09 00 00               je 0x14088f1da
0088E8C7  83 F8 FF                        cmp eax, -1
0088E8CA  0F 84 DD 08 00 00               je 0x14088f1ad
0088E8D0  44 03 64 24 48                  add r12d, dword ptr [rsp + 0x48]
0088E8D5  44 8B 84 24 F0 00 00 00         mov r8d, dword ptr [rsp + 0xf0]
0088E8DD  41 83 FC FD                     cmp r12d, -3
0088E8E1  0F 87 AC 06 00 00               ja 0x14088ef93
0088E8E7  43 8D 04 04                     lea eax, [r12 + r8]
0088E8EB  41 C1 E4 06                     shl r12d, 6
0088E8EF  45 8B C4                        mov r8d, r12d
0088E8F2  41 89 87 8C 00 00 00            mov dword ptr [r15 + 0x8c], eax
0088E8F9  4D 03 47 78                     add r8, qword ptr [r15 + 0x78]
0088E8FD  81 BC 24 08 01 00 00 00 00 00 80  cmp dword ptr [rsp + 0x108], 0x80000000
0088E908  4C 89 44 24 60                  mov qword ptr [rsp + 0x60], r8
0088E90D  0F 84 A5 07 00 00               je 0x14088f0b8
0088E913  41 0F 10 86 F0 00 00 00         movups xmm0, xmmword ptr [r14 + 0xf0]
0088E91B  41 0F 11 00                     movups xmmword ptr [r8], xmm0
0088E91F  41 0F 10 8E 00 01 00 00         movups xmm1, xmmword ptr [r14 + 0x100]
0088E927  41 0F 11 48 10                  movups xmmword ptr [r8 + 0x10], xmm1
0088E92C  F2 41 0F 10 86 10 01 00 00      movsd xmm0, qword ptr [r14 + 0x110]
0088E935  F2 41 0F 11 40 20               movsd qword ptr [r8 + 0x20], xmm0
0088E93B  F7 85 00 01 00 00 00 10 00 00   test dword ptr [rbp + 0x100], 0x1000
0088E945  74 15                           je 0x14088e95c
0088E947  41 0F B7 86 F4 00 00 00         movzx eax, word ptr [r14 + 0xf4]
0088E94F  B9 0F C0 FF FF                  mov ecx, 0xffffc00f
0088E954  66 23 C1                        and ax, cx
0088E957  66 41 89 40 04                  mov word ptr [r8 + 4], ax
0088E95C  4D 8D 48 28                     lea r9, [r8 + 0x28]
0088E960  41 0F B7 86 F2 00 00 00         movzx eax, word ptr [r14 + 0xf2]
0088E968  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
0088E96C  4C 89 8C 24 88 00 00 00         mov qword ptr [rsp + 0x88], r9
0088E974  49 39 B6 B0 00 00 00            cmp qword ptr [r14 + 0xb0], rsi
0088E97B  0F 85 9D 04 00 00               jne 0x14088ee1e
0088E981  49 8B 4E 60                     mov rcx, qword ptr [r14 + 0x60]
0088E985  48 85 C9                        test rcx, rcx
0088E988  0F 85 2B 05 00 00               jne 0x14088eeb9
0088E98E  B9 00 02 00 00                  mov ecx, 0x200
0088E993  41 0F B7 86 F0 00 00 00         movzx eax, word ptr [r14 + 0xf0]
0088E99B  49 8D 96 18 01 00 00            lea rdx, [r14 + 0x118]
0088E9A2  48 89 4C 24 48                  mov qword ptr [rsp + 0x48], rcx
0088E9A7  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
0088E9AC  48 3B C1                        cmp rax, rcx
0088E9AF  0F 87 01 04 00 00               ja 0x14088edb6
0088E9B5  44 8B C0                        mov r8d, eax
0088E9B8  49 8B C9                        mov rcx, r9
0088E9BB  E8 80 7E E3 FF                  call 0x1406c6840
0088E9C0  45 8B 87 94 00 00 00            mov r8d, dword ptr [r15 + 0x94]
0088E9C7  45 85 C0                        test r8d, r8d
0088E9CA  74 32                           je 0x14088e9fe
0088E9CC  8B 44 24 40                     mov eax, dword ptr [rsp + 0x40]
0088E9D0  48 03 44 24 60                  add rax, qword ptr [rsp + 0x60]
0088E9D5  8B 94 24 08 01 00 00            mov edx, dword ptr [rsp + 0x108]
0088E9DC  8B CF                           mov ecx, edi
0088E9DE  48 03 C8                        add rcx, rax
0088E9E1  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0088E9E6  44 89 01                        mov dword ptr [rcx], r8d
0088E9E9  4D 8B C6                        mov r8, r14
0088E9EC  89 71 04                        mov dword ptr [rcx + 4], esi
0088E9EF  48 8B CD                        mov rcx, rbp
0088E9F2  45 8B 8F 94 00 00 00            mov r9d, dword ptr [r15 + 0x94]
0088E9F9  E8 32 8C 00 00                  call 0x140897630
0088E9FE  48 8B 8D 68 01 00 00            mov rcx, qword ptr [rbp + 0x168]
0088EA05  48 89 4C 24 60                  mov qword ptr [rsp + 0x60], rcx
0088EA0A  48 8B 41 50                     mov rax, qword ptr [rcx + 0x50]
0088EA0E  48 8B 79 60                     mov rdi, qword ptr [rcx + 0x60]
0088EA12  48 C1 EF 02                     shr rdi, 2
0088EA16  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
0088EA1B  48 8B C6                        mov rax, rsi
0088EA1E  48 89 7C 24 48                  mov qword ptr [rsp + 0x48], rdi
0088EA23  89 84 24 08 01 00 00            mov dword ptr [rsp + 0x108], eax
0088EA2A  48 3B C7                        cmp rax, rdi
0088EA2D  0F 83 2C 03 00 00               jae 0x14088ed5f
0088EA33  48 8B BD 68 01 00 00            mov rdi, qword ptr [rbp + 0x168]
0088EA3A  45 33 C0                        xor r8d, r8d
0088EA3D  48 83 C7 18                     add rdi, 0x18
0088EA41  33 D2                           xor edx, edx
0088EA43  48 8B CF                        mov rcx, rdi
0088EA46  E8 E5 17 98 FF                  call 0x140210230
0088EA4B  F0 48 0F BA 2F 00               lock bts qword ptr [rdi], 0
0088EA51  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
0088EA56  73 13                           jae 0x14088ea6b
0088EA58  4C 8B C7                        mov r8, rdi
0088EA5B  48 8B D0                        mov rdx, rax
0088EA5E  48 8B CF                        mov rcx, rdi
0088EA61  E8 2A 12 98 FF                  call 0x14020fc90
0088EA66  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
0088EA6B  48 85 C0                        test rax, rax
0088EA6E  74 04                           je 0x14088ea74
0088EA70  C6 40 0A 01                     mov byte ptr [rax + 0xa], 1
0088EA74  4C 8B 4C 24 58                  mov r9, qword ptr [rsp + 0x58]
0088EA79  4D 8B 41 40                     mov r8, qword ptr [r9 + 0x40]
0088EA7D  49 8B C8                        mov rcx, r8
0088EA80  48 C1 E9 18                     shr rcx, 0x18
0088EA84  48 8B C1                        mov rax, rcx
0088EA87  49 23 C0                        and rax, r8
0088EA8A  25 FF FF FF 00                  and eax, 0xffffff
0088EA8F  48 3D FF FF FF 00               cmp rax, 0xffffff
0088EA95  0F 85 3E 02 00 00               jne 0x14088ecd9
0088EA9B  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
0088EAA0  49 8B F8                        mov rdi, r8
0088EAA3  48 8B 40 58                     mov rax, qword ptr [rax + 0x58]
0088EAA7  44 89 20                        mov dword ptr [rax], r12d
0088EAAA  48 B8 00 00 00 00 00 00 FF FF   movabs rax, 0xffff000000000000
0088EAB4  48 23 F8                        and rdi, rax
0088EAB7  49 8B C0                        mov rax, r8
0088EABA  F0 49 0F B1 79 40               lock cmpxchg qword ptr [r9 + 0x40], rdi
0088EAC0  48 8B 8D 68 01 00 00            mov rcx, qword ptr [rbp + 0x168]
0088EAC7  48 83 C1 18                     add rcx, 0x18
0088EACB  49 3B C0                        cmp rax, r8
0088EACE  48 89 4C 24 40                  mov qword ptr [rsp + 0x40], rcx
0088EAD3  48 8B C3                        mov rax, rbx
0088EAD6  0F 85 B5 05 00 00               jne 0x14088f091
0088EADC  F0 48 0F C1 01                  lock xadd qword ptr [rcx], rax
0088EAE1  24 06                           and al, 6
0088EAE3  3C 02                           cmp al, 2
0088EAE5  0F 84 84 06 00 00               je 0x14088f16f
0088EAEB  E8 10 2B A5 FF                  call 0x1402e1600
0088EAF0  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
0088EAF5  F0 FF 80 80 00 00 00            lock inc dword ptr [rax + 0x80]
0088EAFC  48 B8 00 00 00 00 00 00 01 00   movabs rax, 0x1000000000000
0088EB06  48 3B F8                        cmp rdi, rax
0088EB09  1B D2                           sbb edx, edx
0088EB0B  83 E2 02                        and edx, 2
0088EB0E  49 8B 47 50                     mov rax, qword ptr [r15 + 0x50]
0088EB12  40 B7 01                        mov dil, 1
0088EB15  41 8B 8E 08 01 00 00            mov ecx, dword ptr [r14 + 0x108]
0088EB1C  44 8B A4 24 F8 00 00 00         mov r12d, dword ptr [rsp + 0xf8]
0088EB24  40 88 BC 24 F0 00 00 00         mov byte ptr [rsp + 0xf0], dil
0088EB2C  89 48 48                        mov dword ptr [rax + 0x48], ecx
0088EB2F  49 8B 47 50                     mov rax, qword ptr [r15 + 0x50]
0088EB33  41 8B 8E 10 01 00 00            mov ecx, dword ptr [r14 + 0x110]
0088EB3A  89 48 4C                        mov dword ptr [rax + 0x4c], ecx
0088EB3D  45 84 E4                        test r12b, r12b
0088EB40  74 08                           je 0x14088eb4a
0088EB42  85 D2                           test edx, edx
0088EB44  0F 84 A7 02 00 00               je 0x14088edf1
0088EB4A  41 F7 46 28 00 02 00 00         test dword ptr [r14 + 0x28], 0x200
0088EB52  0F 85 B8 06 00 00               jne 0x14088f210
0088EB58  BF 00 20 00 00                  mov edi, 0x2000
0088EB5D  45 33 C0                        xor r8d, r8d
0088EB60  66 41 09 BE F4 00 00 00         or word ptr [r14 + 0xf4], di
0088EB68  33 D2                           xor edx, edx
0088EB6A  66 41 FF 46 E2                  inc word ptr [r14 - 0x1e]
0088EB6F  48 8D BD B0 00 00 00            lea rdi, [rbp + 0xb0]
0088EB76  48 8B CF                        mov rcx, rdi
0088EB79  E8 B2 16 98 FF                  call 0x140210230
0088EB7E  F0 48 0F BA 2F 00               lock bts qword ptr [rdi], 0
0088EB84  4C 8B F8                        mov r15, rax
0088EB87  73 0E                           jae 0x14088eb97
0088EB89  4C 8B C7                        mov r8, rdi
0088EB8C  48 8B D0                        mov rdx, rax
0088EB8F  48 8B CF                        mov rcx, rdi
0088EB92  E8 F9 10 98 FF                  call 0x14020fc90
0088EB97  4D 85 FF                        test r15, r15
0088EB9A  74 05                           je 0x14088eba1
0088EB9C  41 C6 47 0A 01                  mov byte ptr [r15 + 0xa], 1
0088EBA1  41 8B 46 28                     mov eax, dword ptr [r14 + 0x28]
0088EBA5  49 89 6E 10                     mov qword ptr [r14 + 0x10], rbp
0088EBA9  83 E0 87                        and eax, 0xffffff87
0088EBAC  8B 8D A0 01 00 00               mov ecx, dword ptr [rbp + 0x1a0]
0088EBB2  83 E1 06                        and ecx, 6
0088EBB5  C1 E1 02                        shl ecx, 2
0088EBB8  0B C8                           or ecx, eax
0088EBBA  83 E1 FB                        and ecx, 0xfffffffb
0088EBBD  83 C9 03                        or ecx, 3
0088EBC0  41 89 4E 28                     mov dword ptr [r14 + 0x28], ecx
0088EBC4  48 8D 8D B8 00 00 00            lea rcx, [rbp + 0xb8]
0088EBCB  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
0088EBCF  49 89 46 08                     mov qword ptr [r14 + 8], rax
0088EBD3  49 89 0E                        mov qword ptr [r14], rcx
0088EBD6  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
0088EBDA  4C 89 30                        mov qword ptr [rax], r14
0088EBDD  4C 89 71 08                     mov qword ptr [rcx + 8], r14
0088EBE1  FF 85 C8 01 00 00               inc dword ptr [rbp + 0x1c8]
0088EBE7  F0 48 0F C1 1F                  lock xadd qword ptr [rdi], rbx
0088EBEC  80 E3 06                        and bl, 6
0088EBEF  80 FB 02                        cmp bl, 2
0088EBF2  0F 84 B4 02 00 00               je 0x14088eeac
0088EBF8  48 8B CF                        mov rcx, rdi
0088EBFB  E8 00 2A A5 FF                  call 0x1402e1600
0088EC00  0F B6 BC 24 F0 00 00 00         movzx edi, byte ptr [rsp + 0xf0]
0088EC08  E9 96 FA FF FF                  jmp 0x14088e6a3
0088EC0D  3B D7                           cmp edx, edi
0088EC0F  0F 85 23 F6 FF FF               jne 0x14088e238
0088EC15  BF 03 00 00 00                  mov edi, 3
0088EC1A  E9 19 F6 FF FF                  jmp 0x14088e238
0088EC1F  41 8B BE 08 01 00 00            mov edi, dword ptr [r14 + 0x108]
0088EC26  48 8B CB                        mov rcx, rbx
0088EC29  E8 22 E7 BC FF                  call 0x14045d350
0088EC2E  48 85 C0                        test rax, rax
0088EC31  0F 84 30 05 00 00               je 0x14088f167
0088EC37  33 D2                           xor edx, edx
0088EC39  48 89 74 24 30                  mov qword ptr [rsp + 0x30], rsi
0088EC3E  C6 44 24 28 01                  mov byte ptr [rsp + 0x28], 1
0088EC43  44 8B CF                        mov r9d, edi
0088EC46  48 8B CB                        mov rcx, rbx
0088EC49  C7 44 24 20 01 00 00 00         mov dword ptr [rsp + 0x20], 1
0088EC51  44 8D 42 06                     lea r8d, [rdx + 6]
0088EC55  E8 46 E6 FF FF                  call 0x14088d2a0
0088EC5A  49 89 86 D8 00 00 00            mov qword ptr [r14 + 0xd8], rax
0088EC61  E9 7F F6 FF FF                  jmp 0x14088e2e5
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0088E1DC(__int64 a1, int a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, unsigned int a8, unsigned int a9, unsigned int a10, __int64 a11, __int64 a12, unsigned int a13, __int64 a14, __int64 a15, __int64 a16, __int64 a17, __int64 a18, __int64 a19, __int64 a20, __int64 a21, __int64 a22, __int64 a23, __int64 a24, __int64 a25, __int64 a26, __int64 a27, __int64 a28, __int64 a29, unsigned __int8 a30, unsigned int a31, unsigned int a32, unsigned int a33)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p108;
    unsigned __int8 v_stack_p110;
    unsigned __int64 v_stack_p118;
    unsigned int v_stack_p128;
    unsigned __int64 v_stack_p130;
    unsigned __int64 v_stack_p140;
    unsigned __int64 v_stack_p148;
    unsigned __int64 v_stack_p158;
    unsigned __int64 v_stack_p170;
    unsigned __int64 v_stack_p178;
    unsigned int v_stack_p1D8;
    unsigned int v_stack_p1F0;
    unsigned int v_stack_p20;
    unsigned __int8 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned int v_stack_p68;
    unsigned __int64 v_stack_pA8;
    unsigned __int64 v_stack_pB0;
    unsigned int v_stack_pF8;

    v_stack_pB0 = v_rbx;
    v_stack_pA8 = v_rdi;
    if (condition_is_not_equal) goto loc_0088E2E5;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rbp + 24))) & (1)) != 0) goto loc_0088E2E5;
    if (*(unsigned __int64 *)(v_rbp + 24) == 0) goto loc_0088E2E5;
    if (a2 != 0) goto loc_0088EC0D;
    result = (unsigned int)(*(unsigned int *)(v_rip + 7564952));
    v_rdi = 1;
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 7564952))))) != 0) {
        v_rdi = 3;
        result = 0x80000003ULL;
        if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 7564952)))) & (2)) != 0) { v_rdi = (unsigned int)(result); }
    }
    result = PsGetProcessInheritedFromUniqueProcessId(*(unsigned __int64 *)(v_rbp + 24), a2, a3, a4);
    v_stack_p30 = v_rsi;
    v_stack_p28 = 1;
    v_stack_p20 = 1;
    result = PspChargeProcessWakeCounter(*(unsigned __int64 *)(v_rbp + 24), (unsigned int)((unsigned int)(v_rdi)), 2, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + 264)))));
    *(unsigned __int64 *)(v_r14 + 208) = result;
    if ((*(unsigned int *)(v_rip + 7571697)) == ((unsigned int)(v_rsi))) goto loc_0088E2E5;
    if ((unsigned int)(v_r12) == 0) goto loc_0088E2E5;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 516)) == 0) goto loc_0088EC1F;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544) + 136))) & (0x780ULL));
    if (((unsigned int)(result)) == 384) goto loc_0088EC1F;
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 958))) == 3) goto loc_0088EC1F;
loc_0088E2E5:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_r13 + 48)))) & (8)) != 0) goto loc_0088E413;
    if ((*(unsigned __int64 *)(v_rbp + 232)) == (v_rbp + 232)) goto loc_0088E5B0;
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_rbp + 224, a2, a3, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + 264)))));
    if (!(condition_is_above_or_equal)) {
        a3 = v_rbp + 224;
        a2 = result;
        a1 = v_rbp + 224;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + 264)))));
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    if ((*(unsigned __int64 *)(v_rbp + 232)) == (v_rbp + 232)) goto loc_0088E595;
    if ((*(unsigned __int64 *)(v_r14 + 176)) != v_rsi) {
        a1 = v_r14;
        result = AlpcpCaptureMessageDataSafe(a1, a2, a3, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + 264)))));
        *(unsigned __int64 *)(v_r14 + 176) = v_rsi;
    }
    if ((*(unsigned __int64 *)(v_r14 + 144)) != v_rsi) {
        a2 = v_r14;
        a1 = v_rbp;
        result = AlpcpExposeViewAttributeInSenderContext(a1, a2, a3, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + 264)))));
    }
    result = -(*(unsigned __int64 *)(v_r14 + 136));
    a1 = (unsigned int)((a1) & (0x80000000ULL));
    a2 = (unsigned int)((unsigned int)(a1));
    if ((*(unsigned __int64 *)(v_r14 + 144)) == v_rsi) { a2 = (unsigned int)(a1); }
    a1 = (unsigned int)(a2);
    if ((*(unsigned __int64 *)(v_r14 + 152)) == v_rsi) { a1 = a2; }
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 232) - 8) = v_r14;
    result = v_r14 - 30;
    if ((*(unsigned __int8 *)(v_rip + 6129944)) != ((unsigned __int8)(v_rsi))) {
        a1 = v_r14;
        result = AlpcpLogSendMessage(a1, a2, a3, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + 264)))));
    }
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 232)) + 8)) != (*(unsigned __int64 *)(v_rbp + 232))) goto loc_0088E40C;
loc_0088E40C:
loc_0088E413:
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 232) + 8);
    if ((*(unsigned __int64 *)(v_r14 + 176)) != v_rsi) {
        a1 = v_r14;
        result = AlpcpCaptureMessageDataSafe(a1, a2, a3, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + 264)))));
        *(unsigned __int64 *)(v_r14 + 176) = v_rsi;
    }
    if ((*(unsigned __int64 *)(v_r14 + 144)) != v_rsi) {
        a2 = v_r14;
        a1 = v_rbp;
        result = AlpcpExposeViewAttributeInSenderContext(a1, a2, a3, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + 264)))));
    }
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_rbp + 200, a2, a3, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + 264)))));
    if (!(condition_is_above_or_equal)) {
        a3 = v_rbp + 200;
        a2 = result;
        a1 = v_rbp + 200;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + 264)))));
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    *(unsigned __int64 *)(v_r14 + 16) = v_rbp;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r14 + 40))) & (0xFFFFFF87ULL));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbp + 416))) & (6));
    a1 = (unsigned int)((a1) << (2));
    a1 = (unsigned int)((a1) | ((unsigned int)(result)));
    a1 = (unsigned int)((a1) & (0xFFFFFFFCULL));
    a1 = (unsigned int)((a1) | (4));
    *(unsigned int *)(v_r14 + 40) = (unsigned int)(a1);
    *(unsigned __int64 *)(v_r14 + 8) = *(unsigned __int64 *)(v_rbp + 208 + 8);
    *(unsigned __int64 *)(v_r14) = v_rbp + 208;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 208 + 8)) = v_r14;
    *(unsigned __int64 *)(v_rbp + 208 + 8) = v_r14;
    v_rbx = (unsigned __int8)((-1) & (6));
    result = KeAbPostRelease(v_rbp + 200, a2, a3, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + 264)))));
    *(unsigned __int64 *)(v_r13 + 40) = *(unsigned __int64 *)(v_r14 + 160);
    *(unsigned __int64 *)(v_r14 + 160) = v_rsi;
    result = AlpcpUnlockMessage(v_r14, a2, a3, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + 264)))));
    result = 17;
    if (((unsigned __int8)(v_rbx)) != 2) {
        a1 = a16 - 16;
        result = ExfReleasePushLockShared(a1, a2, a3, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + 264)))));
    }
    result = KeAbPostRelease(a16 - 16, a2, a3, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + 264)))));
    result = KeAbPostRelease(v_rbp + 352, a2, a3, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + 264)))));
    result = ObfDereferenceObject(v_rbp, a2, a3, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + 264)))));
    *(unsigned __int64 *)(v_r13 + 32) = v_rsi;
    if ((unsigned int)(*(unsigned __int64 *)(v_rbp + 232)) != 0) goto loc_0088E72C;
    if (a32 != ((unsigned int)(v_rsi))) goto loc_0088E72C;
    if ((*(unsigned __int64 *)(v_r13 + 40)) >= 4) {
        a1 = (*(unsigned __int64 *)(v_r13 + 40)) & (-4);
        a3 = 0;
        a2 = 0;
        result = KeSetEvent(a1, a2, a3, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + 264)))));
        a1 = *(unsigned __int64 *)(v_r13 + 40);
        result = AlpcpReleaseDirectAttribute(a1, a2, a3, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + 264)))));
    }
    *(unsigned __int64 *)(v_r13 + 40) = v_rsi;
    goto loc_0088E72C;
loc_0088E595:
    result = (unsigned __int8)((a16) & (6));
    result = KeAbPostRelease(v_rbp + 224, a2, a3, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + 264)))));
loc_0088E5B0:
    v_stack_p68 = (unsigned int)(v_rsi);
    v_stack_pF8 = 1;
    if (*(unsigned __int64 *)(v_rbp + 360) != 0) goto loc_0088E74F;
loc_0088E5D9:
    if ((*(unsigned __int64 *)(v_r14 + 176)) != v_rsi) {
        a1 = v_r14;
        result = AlpcpCaptureMessageDataSafe(a1, a2, a3, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + 264)))));
        *(unsigned __int64 *)(v_r14 + 176) = v_rsi;
    }
    if ((*(unsigned __int64 *)(v_r14 + 144)) != v_rsi) {
        a2 = v_r14;
        a1 = v_rbp;
        result = AlpcpExposeViewAttributeInSenderContext(a1, a2, a3, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + 264)))));
    }
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_rbp + 136, a2, a3, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + 264)))));
    if (!(condition_is_above_or_equal)) {
        a3 = v_rbp + 136;
        a2 = result;
        a1 = v_rbp + 136;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + 264)))));
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    *(unsigned __int64 *)(v_r14 + 16) = v_rbp;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r14 + 40))) & (0xFFFFFF87ULL));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbp + 416))) & (6));
    a1 = (unsigned int)((a1) << (2));
    a1 = (unsigned int)((a1) | ((unsigned int)(result)));
    a1 = (unsigned int)((a1) & (0xFFFFFFF9ULL));
    a1 = (unsigned int)((a1) | (1));
    *(unsigned int *)(v_r14 + 40) = (unsigned int)(a1);
    *(unsigned __int64 *)(v_r14 + 8) = *(unsigned __int64 *)(v_rbp + 144 + 8);
    *(unsigned __int64 *)(v_r14) = v_rbp + 144;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 144 + 8)) = v_r14;
    *(unsigned __int64 *)(v_rbp + 144 + 8) = v_r14;
    v_rbx = (unsigned __int8)((a16) & (6));
    result = KeAbPostRelease(v_rbp + 136, a2, a3, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + 264)))));
    v_rdi = 0;
loc_0088E6A3:
    if ((unsigned int)((unsigned int)(a10)) == 0) goto loc_0088E6D0;
loc_0088E6D0:
    result = AlpcpUnlockMessage(v_r14, a2, a3, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + 264)))));
    result = 17;
    if ((*(unsigned __int8 *)(v_rip + 6129206)) != ((unsigned __int8)(v_rsi))) {
        a1 = a16 - 16;
        result = ExfReleasePushLockShared(a1, a2, a3, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + 264)))));
    }
    result = KeAbPostRelease(a16 - 16, a2, a3, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + 264)))));
    *(unsigned __int8 *)(v_r13 + 58) = 1;
    *(unsigned __int8 *)(v_r13 + 59) = 0;
loc_0088E72C:
    v_rsp = (v_rsp) + (184);
    return result;
loc_0088E74F:
    if (condition_is_above_or_equal) goto loc_0088E5D9;
    result = -(*(unsigned __int64 *)(v_r14 + 136));
    v_stack_p178 = v_rsi;
    a1 = (unsigned int)((a16 - 16) & (0x80000000ULL));
    a2 = (unsigned int)((unsigned int)(a1));
    if ((*(unsigned __int64 *)(v_r14 + 144)) == v_rsi) { a2 = (unsigned int)(a1); }
    a1 = (unsigned int)(a2);
    if ((*(unsigned __int64 *)(v_r14 + 152)) == v_rsi) { a1 = a2; }
    if ((*(unsigned __int64 *)(v_r14 + 168)) != v_rsi) {
    }
    result = (unsigned int)(~((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(a10) + 148))))));
    if ((((unsigned int)(a1)) & ((unsigned int)(result))) != 0) goto loc_0088E5D9;
    result = (unsigned int)((*(unsigned __int16 *)(v_r14 + 244)) & (0xFFFF00FFULL));
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbp + 416))) >> (11));
    result = (unsigned int)(~((unsigned int)((unsigned int)(a3))));
    result = (unsigned int)((result) & (1));
    a4 = (*(unsigned __int16 *)(v_r14 + 240 + 2)) + (v_r14 + 240);
    a4 = (a4) & (result * 4 + 4 - 1);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)((unsigned int)(a10) + 152))) + ((unsigned int)((unsigned int)((unsigned int)(v_rsi)))));
    a2 = (unsigned int)((*(unsigned __int16 *)(v_r14 + 242)) + ((unsigned int)(result)));
    v_stack_p1F0 = (unsigned int)(v_rsi);
    if ((((unsigned __int8)(a3)) & (1)) != 0) {
        a2 = (unsigned int)((a2) + (-16));
        v_stack_p1F0 = 0x80000000ULL;
    }
    result = ((unsigned int)(*(unsigned int *)((unsigned int)(a10) + 136))) >> (5);
    a3 = (unsigned int)((a2 + 63) >> (6));
    a1 = (*(unsigned __int64 *)((unsigned int)(a10) + 96)) >> (2);
    v_stack_p1D8 = (unsigned int)(a3);
    v_stack_p140 = *(unsigned __int64 *)((unsigned int)(a10) + 104);
    v_stack_p158 = *(unsigned __int64 *)((unsigned int)(a10) + 104) + result * 4;
    v_stack_p170 = a1;
    v_stack_p128 = (unsigned int)(v_rsi);
    if (v_rsi >= a1) goto loc_0088E8DD;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(a10) + 140))))) & (0xFFFFFFE0ULL));
    if (((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(a10) + 140)))) >= (*(unsigned int *)((unsigned int)(a10) + 136))) { result = (unsigned int)(v_rsi); }
    v_stack_p130 = result;
    result = (result) >> (5);
    v_stack_p148 = *(unsigned __int64 *)((unsigned int)(a10) + 104) + result * 4;
    result = AlpcpAllocateFromBitmap(*(unsigned __int64 *)((unsigned int)(a10) + 104) + result * 4, *(unsigned __int64 *)((unsigned int)(a10) + 104) + result * 4, a3, *(unsigned __int64 *)((unsigned int)(a10) + 104));
    v_r12 = (unsigned int)(((unsigned int)((unsigned int)(result))) + (a9));
loc_0088E8DD:
    v_r12 = (unsigned int)((v_r12) << (6));
    *(unsigned int *)((unsigned int)(a10) + 140) = (unsigned int)(v_r12 + (unsigned int)(a30) * 1);
    a3 = ((unsigned int)((unsigned int)(v_r12))) + (*(unsigned __int64 *)((unsigned int)(a10) + 120));
    v_stack_p148 = a3;
    *(unsigned __int64 *)(a3) = v_xmm0;
    *(unsigned __int64 *)(a3 + 16) = v_xmm1;
    *(unsigned __int64 *)(a3 + 32) = v_xmm0;
    result = v_r12 + (unsigned int)(a30) * 1;
    if (((*(unsigned int *)(v_rbp + 256)) & (0x1000ULL)) != 0) {
        result = *(unsigned __int16 *)(v_r14 + 244);
        a1 = 0xFFFFC00FULL;
        result = (unsigned __int16)((result) & ((unsigned __int16)(a1)));
        *(unsigned __int16 *)(a3 + 4) = (unsigned __int16)(result);
    }
    v_stack_p128 = (unsigned int)(*(unsigned __int16 *)(v_r14 + 242));
    v_stack_p170 = a3 + 40;
    v_stack_p130 = 512;
    v_stack_p158 = *(unsigned __int16 *)(v_r14 + 240);
    result = memcpy(a3 + 40, v_r14 + 280, (unsigned int)((unsigned int)(*(unsigned __int16 *)(v_r14 + 240))), a3 + 40);
    if ((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(a10) + 148))) != 0) {
        result = a8;
        result = (result) + (a12);
        a2 = a33;
        a1 = (unsigned int)((unsigned int)((unsigned int)(v_rsi)));
        a1 = (a1) + (result);
        v_stack_p108 = a1;
        *(unsigned int *)(a1) = (unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(a10) + 148)));
        a3 = v_r14;
        *(unsigned int *)(a1 + 4) = (unsigned int)(v_rsi);
        a1 = v_rbp;
        a4 = *(unsigned int *)((unsigned int)(a10) + 148);
        result = AlpcpExposeAttributes(a1, a2, a3, a4);
    }
    v_stack_p148 = *(unsigned __int64 *)(v_rbp + 360);
    v_rdi = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 360) + 96)) >> (2);
    v_stack_p140 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 360) + 80);
    v_stack_p130 = v_rdi;
    v_stack_p1F0 = (unsigned int)(v_rsi);
    a3 = 0;
    v_rdi = (*(unsigned __int64 *)(v_rbp + 360)) + (24);
    a2 = 0;
    result = KeAbPreAcquire(v_rdi, a2, a3, a4);
    v_stack_p158 = result;
    if (!(condition_is_above_or_equal)) {
        a3 = v_rdi;
        a2 = result;
        a1 = v_rdi;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
        result = a14;
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    a1 = (*(unsigned __int64 *)(a11 + 64)) >> (24);
    result = (a1) & (*(unsigned __int64 *)(a11 + 64));
    result = (unsigned int)((result) & (0xFFFFFFULL));
    *(unsigned int *)(*(unsigned __int64 *)(a12 + 88)) = (unsigned int)(v_r12);
    v_rdi = (*(unsigned __int64 *)(a11 + 64)) & (*(unsigned __int64 *)(a12 + 88));
    a1 = (*(unsigned __int64 *)(v_rbp + 360)) + (24);
    v_stack_p128 = a1;
    result = (unsigned __int8)((a22) & (6));
    result = KeAbPostRelease(a1, a2, *(unsigned __int64 *)(a11 + 64), a11);
    a2 = (unsigned int)((a2) & (2));
    v_stack_p1D8 = 1;
    *(unsigned int *)(*(unsigned __int64 *)((unsigned int)(a10) + 80) + 72) = (unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + 264)));
    *(unsigned int *)(*(unsigned __int64 *)((unsigned int)(a10) + 80) + 76) = (unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + 272)));
    if ((unsigned __int8)((unsigned int)(a31)) == 0) goto loc_0088EB4A;
loc_0088EB4A:
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_rbp + 176, a2, a3, a11);
    if (!(condition_is_above_or_equal)) {
        a3 = v_rbp + 176;
        a2 = result;
        a1 = v_rbp + 176;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a11);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    *(unsigned __int64 *)(v_r14 + 16) = v_rbp;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r14 + 40))) & (0xFFFFFF87ULL));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbp + 416))) & (6));
    a1 = (unsigned int)((a1) << (2));
    a1 = (unsigned int)((a1) | ((unsigned int)(result)));
    a1 = (unsigned int)((a1) & (0xFFFFFFFBULL));
    a1 = (unsigned int)((a1) | (3));
    *(unsigned int *)(v_r14 + 40) = (unsigned int)(a1);
    *(unsigned __int64 *)(v_r14 + 8) = *(unsigned __int64 *)(v_rbp + 184 + 8);
    *(unsigned __int64 *)(v_r14) = v_rbp + 184;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 184 + 8)) = v_r14;
    *(unsigned __int64 *)(v_rbp + 184 + 8) = v_r14;
    v_rbx = (unsigned __int8)((a22) & (6));
    result = KeAbPostRelease(v_rbp + 176, a2, a3, a11);
    goto loc_0088E6A3;
loc_0088EC0D:
    if (a2 != a30) goto loc_0088E238;
    goto loc_0088E238;
loc_0088EC1F:
    result = PsGetProcessInheritedFromUniqueProcessId(v_rbx, a2, a3, a11);
    a2 = 0;
    v_stack_p118 = v_rsi;
    v_stack_p110 = 1;
    v_stack_p108 = 1;
    result = PspChargeProcessWakeCounter(v_rbx, a2, a2 + 6, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + 264)))));
    *(unsigned __int64 *)(v_r14 + 216) = result;
    goto loc_0088E2E5;
}
```

## 5. (Beta) C Style

```c
int64_t sub_0088E1DC(int64_t Arg1, int32_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, uint32_t Arg8, uint32_t Arg9, uint32_t Arg10, void *Arg11, void *Arg12, uint32_t Arg13, int64_t Arg14, uint64_t Arg15, void *Arg16, uint64_t Arg17, uint64_t Arg18, uint64_t Arg19, uint64_t Arg20, int64_t Arg21, int64_t Arg22, uint64_t Arg23, uint64_t Arg24, uint64_t Arg25, uint64_t Arg26, uint64_t Arg27, uint64_t Arg28, uint64_t Arg29, uint8_t Arg30, uint32_t Arg31, uint32_t Arg32, uint32_t Arg33)
{
    uint8_t *arg11 = (uint8_t *)Arg11;
    uint8_t *arg12 = (uint8_t *)Arg12;
    uint8_t *arg16 = (uint8_t *)Arg16;

    int64_t result;
    int64_t local_r12;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_p108;
    uint8_t v_stack_p110;
    uint64_t v_stack_p118;
    uint32_t v_stack_p128;
    uint64_t v_stack_p130;
    uint64_t v_stack_p140;
    uint64_t v_stack_p148;
    uint64_t v_stack_p158;
    uint64_t v_stack_p170;
    uint64_t v_stack_p178;
    uint32_t v_stack_p1D8;
    uint32_t v_stack_p1F0;
    uint32_t v_stack_p20;
    uint8_t v_stack_p28;
    uint64_t v_stack_p30;
    uint32_t v_stack_p68;
    uint64_t v_stack_pA8;
    uint64_t v_stack_pB0;
    uint32_t v_stack_pF8;

    v_stack_pB0 = local_rbx;
    v_stack_pA8 = local_rdi;
    if (condition_is_not_equal) goto loc_0088E2E5;
    if ((((uint8_t)(*(uint64_t *)(local_rbp + 0x18))) & (1)) != 0) goto loc_0088E2E5;
    if (*(uint64_t *)(local_rbp + 0x18) == 0) goto loc_0088E2E5;
    if (Arg2 != 0) goto loc_0088EC0D;
    result = (uint32_t)(*(uint32_t *)(v_rip + 0x736E98));
    local_rdi = 1;
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x736E98))))) != 0) {
        local_rdi = 3;
        result = 0x80000003ULL;
        if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x736E98)))) & (2)) != 0) { local_rdi = (uint32_t)(result); }
    }
    result = PsGetProcessInheritedFromUniqueProcessId(*(uint64_t *)(local_rbp + 0x18), Arg2, Arg3, Arg4);
    v_stack_p30 = local_rsi;
    v_stack_p28 = 1;
    v_stack_p20 = 1;
    result = PspChargeProcessWakeCounter(*(uint64_t *)(local_rbp + 0x18), (uint32_t)((uint32_t)(local_rdi)), 2, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x108)))));
    *(uint64_t *)(local_r14 + 0xD0) = result;
    if ((*(uint32_t *)(v_rip + 0x7388F1)) == ((uint32_t)(local_rsi))) goto loc_0088E2E5;
    if ((uint32_t)(local_r12) == 0) goto loc_0088E2E5;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x204)) == 0) goto loc_0088EC1F;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220) + 0x88))) & (0x780ULL));
    if (((uint32_t)(result)) == 384) goto loc_0088EC1F;
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x3BE))) == 3) goto loc_0088EC1F;
loc_0088E2E5:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_r13 + 0x30)))) & (8)) != 0) goto loc_0088E413;
    if ((*(uint64_t *)(local_rbp + 0xE8)) == (local_rbp + 232)) goto loc_0088E5B0;
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(local_rbp + 224, Arg2, Arg3, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x108)))));
    if (!(condition_is_above_or_equal)) {
        Arg3 = local_rbp + 224;
        Arg2 = result;
        Arg1 = local_rbp + 224;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x108)))));
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    if ((*(uint64_t *)(local_rbp + 0xE8)) == (local_rbp + 232)) goto loc_0088E595;
    if ((*(uint64_t *)(local_r14 + 0xB0)) != local_rsi) {
        Arg1 = local_r14;
        result = AlpcpCaptureMessageDataSafe(Arg1, Arg2, Arg3, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x108)))));
        *(uint64_t *)(local_r14 + 0xB0) = local_rsi;
    }
    if ((*(uint64_t *)(local_r14 + 0x90)) != local_rsi) {
        Arg2 = local_r14;
        Arg1 = local_rbp;
        result = AlpcpExposeViewAttributeInSenderContext(Arg1, Arg2, Arg3, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x108)))));
    }
    result = -(*(uint64_t *)(local_r14 + 0x88));
    Arg1 = (uint32_t)((Arg1) & (0x80000000ULL));
    Arg2 = (uint32_t)((uint32_t)(Arg1));
    if ((*(uint64_t *)(local_r14 + 0x90)) == local_rsi) { Arg2 = (uint32_t)(Arg1); }
    Arg1 = (uint32_t)(Arg2);
    if ((*(uint64_t *)(local_r14 + 0x98)) == local_rsi) { Arg1 = Arg2; }
    *(uint64_t *)(*(uint64_t *)(local_rbp + 0xE8) - 0x8) = local_r14;
    result = local_r14 - 30;
    if ((*(uint8_t *)(v_rip + 0x5D8918)) != ((uint8_t)(local_rsi))) {
        Arg1 = local_r14;
        result = AlpcpLogSendMessage(Arg1, Arg2, Arg3, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x108)))));
    }
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rbp + 0xE8)) + 0x8)) != (*(uint64_t *)(local_rbp + 0xE8))) goto loc_0088E40C;
loc_0088E40C:
loc_0088E413:
    result = *(uint64_t *)(*(uint64_t *)(local_rbp + 0xE8) + 0x8);
    if ((*(uint64_t *)(local_r14 + 0xB0)) != local_rsi) {
        Arg1 = local_r14;
        result = AlpcpCaptureMessageDataSafe(Arg1, Arg2, Arg3, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x108)))));
        *(uint64_t *)(local_r14 + 0xB0) = local_rsi;
    }
    if ((*(uint64_t *)(local_r14 + 0x90)) != local_rsi) {
        Arg2 = local_r14;
        Arg1 = local_rbp;
        result = AlpcpExposeViewAttributeInSenderContext(Arg1, Arg2, Arg3, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x108)))));
    }
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(local_rbp + 200, Arg2, Arg3, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x108)))));
    if (!(condition_is_above_or_equal)) {
        Arg3 = local_rbp + 200;
        Arg2 = result;
        Arg1 = local_rbp + 200;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x108)))));
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    *(uint64_t *)(local_r14 + 0x10) = local_rbp;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r14 + 0x28))) & (0xFFFFFF87ULL));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbp + 0x1A0))) & (6));
    Arg1 = (uint32_t)((Arg1) << (2));
    Arg1 = (uint32_t)((Arg1) | ((uint32_t)(result)));
    Arg1 = (uint32_t)((Arg1) & (0xFFFFFFFCULL));
    Arg1 = (uint32_t)((Arg1) | (4));
    *(uint32_t *)(local_r14 + 0x28) = (uint32_t)(Arg1);
    *(uint64_t *)(local_r14 + 0x8) = *(uint64_t *)(local_rbp + 0xD0 + 0x8);
    *(uint64_t *)(local_r14) = local_rbp + 208;
    *(uint64_t *)(*(uint64_t *)(local_rbp + 0xD0 + 0x8)) = local_r14;
    *(uint64_t *)(local_rbp + 0xD0 + 0x8) = local_r14;
    local_rbx = (uint8_t)((-1) & (6));
    result = KeAbPostRelease(local_rbp + 200, Arg2, Arg3, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x108)))));
    *(uint64_t *)(local_r13 + 0x28) = *(uint64_t *)(local_r14 + 0xA0);
    *(uint64_t *)(local_r14 + 0xA0) = local_rsi;
    result = AlpcpUnlockMessage(local_r14, Arg2, Arg3, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x108)))));
    result = 17;
    if (((uint8_t)(local_rbx)) != 2) {
        Arg1 = Arg16 - 16;
        result = ExfReleasePushLockShared(Arg1, Arg2, Arg3, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x108)))));
    }
    result = KeAbPostRelease(Arg16 - 16, Arg2, Arg3, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x108)))));
    result = KeAbPostRelease(local_rbp + 352, Arg2, Arg3, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x108)))));
    result = ObfDereferenceObject(local_rbp, Arg2, Arg3, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x108)))));
    *(uint64_t *)(local_r13 + 0x20) = local_rsi;
    if ((uint32_t)(*(uint64_t *)(local_rbp + 0xE8)) != 0) goto loc_0088E72C;
    if (Arg32 != ((uint32_t)(local_rsi))) goto loc_0088E72C;
    if ((*(uint64_t *)(local_r13 + 0x28)) >= 4) {
        Arg1 = (*(uint64_t *)(local_r13 + 0x28)) & (-4);
        Arg3 = 0;
        Arg2 = 0;
        result = KeSetEvent(Arg1, Arg2, Arg3, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x108)))));
        Arg1 = *(uint64_t *)(local_r13 + 0x28);
        result = AlpcpReleaseDirectAttribute(Arg1, Arg2, Arg3, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x108)))));
    }
    *(uint64_t *)(local_r13 + 0x28) = local_rsi;
    goto loc_0088E72C;
loc_0088E595:
    result = (uint8_t)((Arg16) & (6));
    result = KeAbPostRelease(local_rbp + 224, Arg2, Arg3, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x108)))));
loc_0088E5B0:
    v_stack_p68 = (uint32_t)(local_rsi);
    v_stack_pF8 = 1;
    if (*(uint64_t *)(local_rbp + 0x168) != 0) goto loc_0088E74F;
loc_0088E5D9:
    if ((*(uint64_t *)(local_r14 + 0xB0)) != local_rsi) {
        Arg1 = local_r14;
        result = AlpcpCaptureMessageDataSafe(Arg1, Arg2, Arg3, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x108)))));
        *(uint64_t *)(local_r14 + 0xB0) = local_rsi;
    }
    if ((*(uint64_t *)(local_r14 + 0x90)) != local_rsi) {
        Arg2 = local_r14;
        Arg1 = local_rbp;
        result = AlpcpExposeViewAttributeInSenderContext(Arg1, Arg2, Arg3, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x108)))));
    }
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(local_rbp + 136, Arg2, Arg3, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x108)))));
    if (!(condition_is_above_or_equal)) {
        Arg3 = local_rbp + 136;
        Arg2 = result;
        Arg1 = local_rbp + 136;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x108)))));
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    *(uint64_t *)(local_r14 + 0x10) = local_rbp;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r14 + 0x28))) & (0xFFFFFF87ULL));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbp + 0x1A0))) & (6));
    Arg1 = (uint32_t)((Arg1) << (2));
    Arg1 = (uint32_t)((Arg1) | ((uint32_t)(result)));
    Arg1 = (uint32_t)((Arg1) & (0xFFFFFFF9ULL));
    Arg1 = (uint32_t)((Arg1) | (1));
    *(uint32_t *)(local_r14 + 0x28) = (uint32_t)(Arg1);
    *(uint64_t *)(local_r14 + 0x8) = *(uint64_t *)(local_rbp + 0x90 + 0x8);
    *(uint64_t *)(local_r14) = local_rbp + 144;
    *(uint64_t *)(*(uint64_t *)(local_rbp + 0x90 + 0x8)) = local_r14;
    *(uint64_t *)(local_rbp + 0x90 + 0x8) = local_r14;
    local_rbx = (uint8_t)((Arg16) & (6));
    result = KeAbPostRelease(local_rbp + 136, Arg2, Arg3, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x108)))));
    local_rdi = 0;
loc_0088E6A3:
    if ((uint32_t)((uint32_t)(Arg10)) == 0) goto loc_0088E6D0;
loc_0088E6D0:
    result = AlpcpUnlockMessage(local_r14, Arg2, Arg3, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x108)))));
    result = 17;
    if ((*(uint8_t *)(v_rip + 0x5D8636)) != ((uint8_t)(local_rsi))) {
        Arg1 = Arg16 - 16;
        result = ExfReleasePushLockShared(Arg1, Arg2, Arg3, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x108)))));
    }
    result = KeAbPostRelease(Arg16 - 16, Arg2, Arg3, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x108)))));
    *(uint8_t *)(local_r13 + 0x3A) = 1;
    *(uint8_t *)(local_r13 + 0x3B) = 0;
loc_0088E72C:
    local_rsp = (local_rsp) + (184);
    return result;
loc_0088E74F:
    if (condition_is_above_or_equal) goto loc_0088E5D9;
    result = -(*(uint64_t *)(local_r14 + 0x88));
    v_stack_p178 = local_rsi;
    Arg1 = (uint32_t)((Arg16 - 16) & (0x80000000ULL));
    Arg2 = (uint32_t)((uint32_t)(Arg1));
    if ((*(uint64_t *)(local_r14 + 0x90)) == local_rsi) { Arg2 = (uint32_t)(Arg1); }
    Arg1 = (uint32_t)(Arg2);
    if ((*(uint64_t *)(local_r14 + 0x98)) == local_rsi) { Arg1 = Arg2; }
    if ((*(uint64_t *)(local_r14 + 0xA8)) != local_rsi) {
    }
    result = (uint32_t)(~((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(Arg10) + 0x94))))));
    if ((((uint32_t)(Arg1)) & ((uint32_t)(result))) != 0) goto loc_0088E5D9;
    result = (uint32_t)((*(uint16_t *)(local_r14 + 0xF4)) & (0xFFFF00FFULL));
    Arg3 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbp + 0x1A0))) >> (11));
    result = (uint32_t)(~((uint32_t)((uint32_t)(Arg3))));
    result = (uint32_t)((result) & (1));
    Arg4 = (*(uint16_t *)(local_r14 + 0xF0 + 0x2)) + (local_r14 + 240);
    Arg4 = (Arg4) & (result * 4 + 4 - 1);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)((uint32_t)(Arg10) + 0x98))) + ((uint32_t)((uint32_t)((uint32_t)(local_rsi)))));
    Arg2 = (uint32_t)((*(uint16_t *)(local_r14 + 0xF2)) + ((uint32_t)(result)));
    v_stack_p1F0 = (uint32_t)(local_rsi);
    if ((((uint8_t)(Arg3)) & (1)) != 0) {
        Arg2 = (uint32_t)((Arg2) + (-16));
        v_stack_p1F0 = 0x80000000ULL;
    }
    result = ((uint32_t)(*(uint32_t *)((uint32_t)(Arg10) + 0x88))) >> (5);
    Arg3 = (uint32_t)((Arg2 + 63) >> (6));
    Arg1 = (*(uint64_t *)((uint32_t)(Arg10) + 0x60)) >> (2);
    v_stack_p1D8 = (uint32_t)(Arg3);
    v_stack_p140 = *(uint64_t *)((uint32_t)(Arg10) + 0x68);
    v_stack_p158 = *(uint64_t *)((uint32_t)(Arg10) + 0x68) + result * 4;
    v_stack_p170 = Arg1;
    v_stack_p128 = (uint32_t)(local_rsi);
    if (local_rsi >= Arg1) goto loc_0088E8DD;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(Arg10) + 0x8C))))) & (0xFFFFFFE0ULL));
    if (((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(Arg10) + 0x8C)))) >= (*(uint32_t *)((uint32_t)(Arg10) + 0x88))) { result = (uint32_t)(local_rsi); }
    v_stack_p130 = result;
    result = (result) >> (5);
    v_stack_p148 = *(uint64_t *)((uint32_t)(Arg10) + 0x68) + result * 4;
    result = AlpcpAllocateFromBitmap(*(uint64_t *)((uint32_t)(Arg10) + 0x68) + result * 4, *(uint64_t *)((uint32_t)(Arg10) + 0x68) + result * 4, Arg3, *(uint64_t *)((uint32_t)(Arg10) + 0x68));
    local_r12 = (uint32_t)(((uint32_t)((uint32_t)(result))) + (Arg9));
loc_0088E8DD:
    local_r12 = (uint32_t)((local_r12) << (6));
    *(uint32_t *)((uint32_t)(Arg10) + 0x8C) = (uint32_t)(local_r12 + (uint32_t)(Arg30) * 1);
    Arg3 = ((uint32_t)((uint32_t)(local_r12))) + (*(uint64_t *)((uint32_t)(Arg10) + 0x78));
    v_stack_p148 = Arg3;
    *(uint64_t *)(Arg3) = v_xmm0;
    *(uint64_t *)(Arg3 + 0x10) = v_xmm1;
    *(uint64_t *)(Arg3 + 0x20) = v_xmm0;
    result = local_r12 + (uint32_t)(Arg30) * 1;
    if (((*(uint32_t *)(local_rbp + 0x100)) & (0x1000ULL)) != 0) {
        result = *(uint16_t *)(local_r14 + 0xF4);
        Arg1 = 0xFFFFC00FULL;
        result = (uint16_t)((result) & ((uint16_t)(Arg1)));
        *(uint16_t *)(Arg3 + 0x4) = (uint16_t)(result);
    }
    v_stack_p128 = (uint32_t)(*(uint16_t *)(local_r14 + 0xF2));
    v_stack_p170 = Arg3 + 40;
    v_stack_p130 = 512;
    v_stack_p158 = *(uint16_t *)(local_r14 + 0xF0);
    result = memcpy(Arg3 + 40, local_r14 + 280, (uint32_t)((uint32_t)(*(uint16_t *)(local_r14 + 0xF0))), Arg3 + 40);
    if ((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(Arg10) + 0x94))) != 0) {
        result = Arg8;
        result = (result) + (Arg12);
        Arg2 = Arg33;
        Arg1 = (uint32_t)((uint32_t)((uint32_t)(local_rsi)));
        Arg1 = (Arg1) + (result);
        v_stack_p108 = Arg1;
        *(uint32_t *)(Arg1) = (uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(Arg10) + 0x94)));
        Arg3 = local_r14;
        *(uint32_t *)(Arg1 + 0x4) = (uint32_t)(local_rsi);
        Arg1 = local_rbp;
        Arg4 = *(uint32_t *)((uint32_t)(Arg10) + 0x94);
        result = AlpcpExposeAttributes(Arg1, Arg2, Arg3, Arg4);
    }
    v_stack_p148 = *(uint64_t *)(local_rbp + 0x168);
    local_rdi = (*(uint64_t *)(*(uint64_t *)(local_rbp + 0x168) + 0x60)) >> (2);
    v_stack_p140 = *(uint64_t *)(*(uint64_t *)(local_rbp + 0x168) + 0x50);
    v_stack_p130 = local_rdi;
    v_stack_p1F0 = (uint32_t)(local_rsi);
    Arg3 = 0;
    local_rdi = (*(uint64_t *)(local_rbp + 0x168)) + (24);
    Arg2 = 0;
    result = KeAbPreAcquire(local_rdi, Arg2, Arg3, Arg4);
    v_stack_p158 = result;
    if (!(condition_is_above_or_equal)) {
        Arg3 = local_rdi;
        Arg2 = result;
        Arg1 = local_rdi;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, Arg4);
        result = Arg14;
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    Arg1 = (*(uint64_t *)(arg11 + 0x40)) >> (24);
    result = (Arg1) & (*(uint64_t *)(arg11 + 0x40));
    result = (uint32_t)((result) & (0xFFFFFFULL));
    *(uint32_t *)(*(uint64_t *)(arg12 + 0x58)) = (uint32_t)(local_r12);
    local_rdi = (*(uint64_t *)(arg11 + 0x40)) & (*(uint64_t *)(arg12 + 0x58));
    Arg1 = (*(uint64_t *)(local_rbp + 0x168)) + (24);
    v_stack_p128 = Arg1;
    result = (uint8_t)((Arg22) & (6));
    result = KeAbPostRelease(Arg1, Arg2, *(uint64_t *)(arg11 + 0x40), Arg11);
    Arg2 = (uint32_t)((Arg2) & (2));
    v_stack_p1D8 = 1;
    *(uint32_t *)(*(uint64_t *)((uint32_t)(Arg10) + 0x50) + 0x48) = (uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x108)));
    *(uint32_t *)(*(uint64_t *)((uint32_t)(Arg10) + 0x50) + 0x4C) = (uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x110)));
    if ((uint8_t)((uint32_t)(Arg31)) == 0) goto loc_0088EB4A;
loc_0088EB4A:
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(local_rbp + 176, Arg2, Arg3, Arg11);
    if (!(condition_is_above_or_equal)) {
        Arg3 = local_rbp + 176;
        Arg2 = result;
        Arg1 = local_rbp + 176;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, Arg11);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    *(uint64_t *)(local_r14 + 0x10) = local_rbp;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r14 + 0x28))) & (0xFFFFFF87ULL));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbp + 0x1A0))) & (6));
    Arg1 = (uint32_t)((Arg1) << (2));
    Arg1 = (uint32_t)((Arg1) | ((uint32_t)(result)));
    Arg1 = (uint32_t)((Arg1) & (0xFFFFFFFBULL));
    Arg1 = (uint32_t)((Arg1) | (3));
    *(uint32_t *)(local_r14 + 0x28) = (uint32_t)(Arg1);
    *(uint64_t *)(local_r14 + 0x8) = *(uint64_t *)(local_rbp + 0xB8 + 0x8);
    *(uint64_t *)(local_r14) = local_rbp + 184;
    *(uint64_t *)(*(uint64_t *)(local_rbp + 0xB8 + 0x8)) = local_r14;
    *(uint64_t *)(local_rbp + 0xB8 + 0x8) = local_r14;
    local_rbx = (uint8_t)((Arg22) & (6));
    result = KeAbPostRelease(local_rbp + 176, Arg2, Arg3, Arg11);
    goto loc_0088E6A3;
loc_0088EC0D:
    if (Arg2 != Arg30) goto loc_0088E238;
    goto loc_0088E238;
loc_0088EC1F:
    result = PsGetProcessInheritedFromUniqueProcessId(local_rbx, Arg2, Arg3, Arg11);
    Arg2 = 0;
    v_stack_p118 = local_rsi;
    v_stack_p110 = 1;
    v_stack_p108 = 1;
    result = PspChargeProcessWakeCounter(local_rbx, Arg2, Arg2 + 6, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x108)))));
    *(uint64_t *)(local_r14 + 0xD8) = result;
    goto loc_0088E2E5;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg11` | `+ 0x40` | `64` | `R` |
| `Arg11` | `+ 0x80` | `32` | `R/W` |
| `Arg12` | `+ 0x58` | `64` | `R` |
| `Arg16` | `- 0x10` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0088E1DC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
