# AlpcpCancelMessage

- RVA: `0x00894120`–`0x008946F7` (길이 `1,495` bytes)
- VA: `0x0000000140894120`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0007DFB0`
- 디코드: `385`개 명령, `1,495/1,495` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **35**; 고유 호출 대상: **18**
- 직접 호출자로 확인된 함수: **13**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x008941B8` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x008941D7` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)
- `0x00894204` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x0089420C` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0089426D` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0089428C` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)
- `0x008942C2` → [ObReferenceObjectSafe](../../text/41/ObReferenceObjectSafe_function_0041DAE0.md) (function, `0x0041DAE0`)
- `0x008942DB` → [ObReferenceObjectSafe](../../text/41/ObReferenceObjectSafe_function_0041DAE0.md) (function, `0x0041DAE0`)
- `0x00894352` → [AlpcpReleaseMessageAttributesOnCancel](AlpcpReleaseMessageAttributesOnCancel_function_00894030.md) (function, `0x00894030`)
- `0x00894371` → [AlpcpClearOwnerPortMessage](../88/AlpcpClearOwnerPortMessage_function_0088FD30.md) (function, `0x0088FD30`)
- `0x00894379` → [AlpcpTransferQuotaMessage](AlpcpTransferQuotaMessage_function_008940D0.md) (function, `0x008940D0`)
- `0x00894390` → [PsReleaseProcessWakeCounter](../88/PsReleaseProcessWakeCounter_function_0088B940.md) (function, `0x0088B940`)
- `0x008943AE` → [PsReleaseProcessWakeCounter](../88/PsReleaseProcessWakeCounter_function_0088B940.md) (function, `0x0088B940`)
- `0x008943F3` → [AlpcpRemoveMessageFromPendingQueue](../88/AlpcpRemoveMessageFromPendingQueue_function_0088FD70.md) (function, `0x0088FD70`)
- `0x0089440D` → [AlpcpUnlockMessage](AlpcpUnlockMessage_function_00897AE0.md) (function, `0x00897AE0`)
- `0x0089441A` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00894427` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00894462` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x0089446A` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x008944AD` → [KeReleaseSemaphoreEx](../../text/34/KeReleaseSemaphoreEx_function_003468C0.md) (function, `0x003468C0`)
- `0x008944CF` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x008944E9` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x008944FE` → [AlpcpRemoveMessagePort](../9F/AlpcpRemoveMessagePort_function_009F441C.md) (function, `0x009F441C`)
- `0x0089451D` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00894555` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00894576` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)
- `0x008945CE` → [AlpcpInsertMessageCanceledQueue](../A6/AlpcpInsertMessageCanceledQueue_function_00A6DC38.md) (function, `0x00A6DC38`)
- `0x008945D6` → [AlpcpSignalPortAndUnlock](../A7/AlpcpSignalPortAndUnlock_function_00A76910.md) (function, `0x00A76910`)
- `0x0089463A` → [ObReferenceObjectSafe](../../text/41/ObReferenceObjectSafe_function_0041DAE0.md) (function, `0x0041DAE0`)
- `0x00894667` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x00894674` → [ObReferenceObjectSafe](../../text/41/ObReferenceObjectSafe_function_0041DAE0.md) (function, `0x0041DAE0`)
- `0x008946A1` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x008946B6` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x008946D4` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x008946ED` → [AlpcpRemoveMessageFromPendingQueue](../88/AlpcpRemoveMessageFromPendingQueue_function_0088FD70.md) (function, `0x0088FD70`)

### Direct callers
- [AlpcpSendMessage](../88/AlpcpSendMessage_function_0088BD40.md) at `0x0088C646`
- [AlpcpDispatchReplyToPort](../88/AlpcpDispatchReplyToPort_function_0088F880.md) at `0x0088FC2A`
- [AlpcpReceiveLegacyMessage](AlpcpReceiveLegacyMessage_function_00895DE0.md) at `0x00896064`
- [AlpcpReceiveMessage](AlpcpReceiveMessage_function_00897ED0.md) at `0x008984A2`
- [AlpcpReceiveSynchronousReply](../92/AlpcpReceiveSynchronousReply_function_009224F0.md) at `0x00922770`
- [AlpcpFlushMessagesPort](../92/AlpcpFlushMessagesPort_function_00925554.md) at `0x00925837`
- [AlpcpFlushMessagesPort](../92/AlpcpFlushMessagesPort_function_00925554.md) at `0x009258BA`
- [AlpcpFlushMessagesPort](../92/AlpcpFlushMessagesPort_function_00925554.md) at `0x0092590A`
- [AlpcpFlushMessagesPort](../92/AlpcpFlushMessagesPort_function_00925554.md) at `0x0092595A`
- [AlpcpFlushMessagesPort](../92/AlpcpFlushMessagesPort_function_00925554.md) at `0x00925C32`
- [AlpcpFlushMessagesPort](../92/AlpcpFlushMessagesPort_function_00925554.md) at `0x00925C7C`
- [AlpcpFlushMessagesPort](../92/AlpcpFlushMessagesPort_function_00925554.md) at `0x00925CC2`
- [AlpcpReplyLegacySynchronousRequest](../9F/AlpcpReplyLegacySynchronousRequest_function_009F5CF0.md) at `0x009F5E89`
- [AlpcpAcceptConnectPort](../A3/AlpcpAcceptConnectPort_function_00A34290.md) at `0x00A346C7`
- [AlpcpFlushMessagesByRequestor](../A3/AlpcpFlushMessagesByRequestor_function_00A352F0.md) at `0x00A35477`
- [NtAlpcCancelMessage](../A3/NtAlpcCancelMessage_function_00A3A860.md) at `0x00A3A93E`
- [sub_00B1979A](../B1/Unknown_function_00B1979A.md) at `0x00B197A6`
- [sub_00B226A4](../B2/Unknown_function_00B226A4.md) at `0x00B2274B`
- [sub_00B22756](../B2/Unknown_function_00B22756.md) at `0x00B22767`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **24**
  - `0x008941B8` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x008941D7` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (`PAGE` → `.text`)
  - `0x00894204` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x0089420C` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0089426D` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x0089428C` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (`PAGE` → `.text`)
  - `0x008942C2` → [ObReferenceObjectSafe](../../text/41/ObReferenceObjectSafe_function_0041DAE0.md) (`PAGE` → `.text`)
  - `0x008942DB` → [ObReferenceObjectSafe](../../text/41/ObReferenceObjectSafe_function_0041DAE0.md) (`PAGE` → `.text`)
  - `0x0089441A` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00894427` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00894462` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x0089446A` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x008944AD` → [KeReleaseSemaphoreEx](../../text/34/KeReleaseSemaphoreEx_function_003468C0.md) (`PAGE` → `.text`)
  - `0x008944CF` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x008944E9` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x0089451D` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x00894555` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x00894576` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (`PAGE` → `.text`)
  - `0x0089463A` → [ObReferenceObjectSafe](../../text/41/ObReferenceObjectSafe_function_0041DAE0.md) (`PAGE` → `.text`)
  - `0x00894667` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x00894674` → [ObReferenceObjectSafe](../../text/41/ObReferenceObjectSafe_function_0041DAE0.md) (`PAGE` → `.text`)
  - `0x008946A1` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x008946B6` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x008946D4` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **5**
  - `0x0089418D` → [sub_00B19682](../B1/Unknown_function_00B19682.md) (`tail-transfer`)
  - `0x00894698` → [sub_00B19682 + 0x79](../B1/Unknown_function_00B19682.md) (`tail-transfer`)
  - `0x008946A7` → [sub_00B19682 + 0x79](../B1/Unknown_function_00B19682.md) (`tail-transfer`)
  - `0x008946C5` → [sub_00B19682 + 0x87](../B1/Unknown_function_00B19682.md) (`tail-transfer`)
  - `0x008946DA` → [sub_00B19682 + 0x87](../B1/Unknown_function_00B19682.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00894120  44 89 44 24 18                  mov dword ptr [rsp + 0x18], r8d
00894125  53                              push rbx
00894126  55                              push rbp
00894127  56                              push rsi
00894128  57                              push rdi
00894129  41 54                           push r12
0089412B  41 55                           push r13
0089412D  41 56                           push r14
0089412F  41 57                           push r15
00894131  48 83 EC 48                     sub rsp, 0x48
00894135  8B 6A 28                        mov ebp, dword ptr [rdx + 0x28]
00894138  4C 8B E1                        mov r12, rcx
0089413B  48 8B DA                        mov rbx, rdx
0089413E  45 8B E8                        mov r13d, r8d
00894141  45 33 C0                        xor r8d, r8d
00894144  8B D5                           mov edx, ebp
00894146  8B CD                           mov ecx, ebp
00894148  81 E2 80 00 00 00               and edx, 0x80
0089414E  41 8B 84 24 A0 01 00 00         mov eax, dword ptr [r12 + 0x1a0]
00894156  83 E1 07                        and ecx, 7
00894159  4C 8B 7B 10                     mov r15, qword ptr [rbx + 0x10]
0089415D  41 8B F8                        mov edi, r8d
00894160  D1 E8                           shr eax, 1
00894162  45 8D 48 01                     lea r9d, [r8 + 1]
00894166  83 E0 03                        and eax, 3
00894169  4C 89 BC 24 98 00 00 00         mov qword ptr [rsp + 0x98], r15
00894171  89 8C 24 90 00 00 00            mov dword ptr [rsp + 0x90], ecx
00894178  41 8B F0                        mov esi, r8d
0089417B  41 2B C1                        sub eax, r9d
0089417E  0F 84 AF 00 00 00               je 0x140894233
00894184  83 E5 78                        and ebp, 0x78
00894187  45 8B F0                        mov r14d, r8d
0089418A  41 3B C1                        cmp eax, r9d
0089418D  0F 85 EF 54 28 00               jne 0x140b19682
00894193  83 FD 10                        cmp ebp, 0x10
00894196  41 0F 94 C6                     sete r14b
0089419A  85 D2                           test edx, edx
0089419C  0F 85 53 01 00 00               jne 0x1408942f5
008941A2  49 8B 44 24 10                  mov rax, qword ptr [r12 + 0x10]
008941A7  33 D2                           xor edx, edx
008941A9  48 89 84 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rax
008941B1  4C 8D 78 F0                     lea r15, [rax - 0x10]
008941B5  49 8B CF                        mov rcx, r15
008941B8  E8 73 C0 97 FF                  call 0x140210230
008941BD  4C 8B E8                        mov r13, rax
008941C0  8D 4E 11                        lea ecx, [rsi + 0x11]
008941C3  33 C0                           xor eax, eax
008941C5  F0 49 0F B1 0F                  lock cmpxchg qword ptr [r15], rcx
008941CA  74 10                           je 0x1408941dc
008941CC  4D 8B CF                        mov r9, r15
008941CF  4D 8B C5                        mov r8, r13
008941D2  33 D2                           xor edx, edx
008941D4  49 8B CF                        mov rcx, r15
008941D7  E8 70 C2 97 FF                  call 0x14021044c
008941DC  4D 85 ED                        test r13, r13
008941DF  74 05                           je 0x1408941e6
008941E1  41 C6 45 0A 01                  mov byte ptr [r13 + 0xa], 1
008941E6  F7 43 28 00 02 00 00            test dword ptr [rbx + 0x28], 0x200
008941ED  0F 84 29 04 00 00               je 0x14089461c
008941F3  33 ED                           xor ebp, ebp
008941F5  B8 11 00 00 00                  mov eax, 0x11
008941FA  F0 49 0F B1 2F                  lock cmpxchg qword ptr [r15], rbp
008941FF  74 08                           je 0x140894209
00894201  49 8B CF                        mov rcx, r15
00894204  E8 37 F2 9C FF                  call 0x140263440
00894209  49 8B CF                        mov rcx, r15
0089420C  E8 EF D3 A4 FF                  call 0x1402e1600
00894211  8B 8C 24 90 00 00 00            mov ecx, dword ptr [rsp + 0x90]
00894218  41 B9 01 00 00 00               mov r9d, 1
0089421E  4C 8B BC 24 98 00 00 00         mov r15, qword ptr [rsp + 0x98]
00894226  44 8B AC 24 A0 00 00 00         mov r13d, dword ptr [rsp + 0xa0]
0089422E  E9 C4 00 00 00                  jmp 0x1408942f7
00894233  83 E5 78                        and ebp, 0x78
00894236  45 8B E0                        mov r12d, r8d
00894239  83 FD 08                        cmp ebp, 8
0089423C  41 0F 94 C4                     sete r12b
00894240  45 8B F4                        mov r14d, r12d
00894243  85 D2                           test edx, edx
00894245  0F 85 AA 00 00 00               jne 0x1408942f5
0089424B  4D 85 FF                        test r15, r15
0089424E  0F 84 A1 00 00 00               je 0x1408942f5
00894254  4C 8B BB B8 00 00 00            mov r15, qword ptr [rbx + 0xb8]
0089425B  4D 85 FF                        test r15, r15
0089425E  0F 84 89 00 00 00               je 0x1408942ed
00894264  4D 8D 77 F0                     lea r14, [r15 - 0x10]
00894268  33 D2                           xor edx, edx
0089426A  49 8B CE                        mov rcx, r14
0089426D  E8 BE BF 97 FF                  call 0x140210230
00894272  4C 8B E8                        mov r13, rax
00894275  33 C0                           xor eax, eax
00894277  8D 48 11                        lea ecx, [rax + 0x11]
0089427A  F0 49 0F B1 0E                  lock cmpxchg qword ptr [r14], rcx
0089427F  74 10                           je 0x140894291
00894281  4D 8B CE                        mov r9, r14
00894284  4D 8B C5                        mov r8, r13
00894287  33 D2                           xor edx, edx
00894289  49 8B CE                        mov rcx, r14
0089428C  E8 BB C1 97 FF                  call 0x14021044c
00894291  4D 85 ED                        test r13, r13
00894294  74 05                           je 0x14089429b
00894296  41 C6 45 0A 01                  mov byte ptr [r13 + 0xa], 1
0089429B  F7 43 28 00 02 00 00            test dword ptr [rbx + 0x28], 0x200
008942A2  0F 85 A9 01 00 00               jne 0x140894451
008942A8  83 FD 08                        cmp ebp, 8
008942AB  0F 85 D2 03 00 00               jne 0x140894683
008942B1  49 8B 7F 10                     mov rdi, qword ptr [r15 + 0x10]
008942B5  48 8B F7                        mov rsi, rdi
008942B8  33 ED                           xor ebp, ebp
008942BA  48 85 FF                        test rdi, rdi
008942BD  74 10                           je 0x1408942cf
008942BF  48 8B CF                        mov rcx, rdi
008942C2  E8 19 98 B8 FF                  call 0x14041dae0
008942C7  F6 D8                           neg al
008942C9  48 1B C9                        sbb rcx, rcx
008942CC  48 23 F9                        and rdi, rcx
008942CF  48 85 F6                        test rsi, rsi
008942D2  0F 84 7B 01 00 00               je 0x140894453
008942D8  48 8B CE                        mov rcx, rsi
008942DB  E8 00 98 B8 FF                  call 0x14041dae0
008942E0  F6 D8                           neg al
008942E2  48 1B C9                        sbb rcx, rcx
008942E5  48 23 F1                        and rsi, rcx
008942E8  E9 66 01 00 00                  jmp 0x140894453
008942ED  4C 8B BC 24 98 00 00 00         mov r15, qword ptr [rsp + 0x98]
008942F5  33 ED                           xor ebp, ebp
008942F7  45 85 F6                        test r14d, r14d
008942FA  0F 84 EA 02 00 00               je 0x1408945ea
00894300  4D 85 FF                        test r15, r15
00894303  0F 84 38 01 00 00               je 0x140894441
00894309  83 F9 03                        cmp ecx, 3
0089430C  0F 85 2F 01 00 00               jne 0x140894441
00894312  F7 43 28 00 20 00 00            test dword ptr [rbx + 0x28], 0x2000
00894319  41 8B C1                        mov eax, r9d
0089431C  0F 85 1F 01 00 00               jne 0x140894441
00894322  41 BC 03 01 00 00               mov r12d, 0x103
00894328  45 84 E9                        test r9b, r13b
0089432B  0F 85 17 01 00 00               jne 0x140894448
00894331  0F BA 6B 28 07                  bts dword ptr [rbx + 0x28], 7
00894336  48 8B CB                        mov rcx, rbx
00894339  40 88 AB F4 00 00 00            mov byte ptr [rbx + 0xf4], bpl
00894340  66 83 8B F4 00 00 00 0C         or word ptr [rbx + 0xf4], 0xc
00894348  C7 83 F0 00 00 00 00 00 28 00   mov dword ptr [rbx + 0xf0], 0x280000
00894352  E8 D9 FC FF FF                  call 0x140894030
00894357  B8 FF DF FF FF                  mov eax, 0xffffdfff
0089435C  66 21 83 F4 00 00 00            and word ptr [rbx + 0xf4], ax
00894363  81 4B 28 00 02 01 00            or dword ptr [rbx + 0x28], 0x10200
0089436A  F0 09 2C 24                     lock or dword ptr [rsp], ebp
0089436E  48 8B CB                        mov rcx, rbx
00894371  E8 BA B9 FF FF                  call 0x14088fd30
00894376  48 8B CB                        mov rcx, rbx
00894379  E8 52 FD FF FF                  call 0x1408940d0
0089437E  48 8B 8B D0 00 00 00            mov rcx, qword ptr [rbx + 0xd0]
00894385  48 85 C9                        test rcx, rcx
00894388  74 12                           je 0x14089439c
0089438A  8B 93 08 01 00 00               mov edx, dword ptr [rbx + 0x108]
00894390  E8 AB 75 FF FF                  call 0x14088b940
00894395  48 89 AB D0 00 00 00            mov qword ptr [rbx + 0xd0], rbp
0089439C  48 8B 8B D8 00 00 00            mov rcx, qword ptr [rbx + 0xd8]
008943A3  48 85 C9                        test rcx, rcx
008943A6  74 12                           je 0x1408943ba
008943A8  8B 93 08 01 00 00               mov edx, dword ptr [rbx + 0x108]
008943AE  E8 8D 75 FF FF                  call 0x14088b940
008943B3  48 89 AB D8 00 00 00            mov qword ptr [rbx + 0xd8], rbp
008943BA  48 8B 4B 20                     mov rcx, qword ptr [rbx + 0x20]
008943BE  48 85 C9                        test rcx, rcx
008943C1  0F 85 B0 00 00 00               jne 0x140894477
008943C7  48 85 FF                        test rdi, rdi
008943CA  0F 85 5E 01 00 00               jne 0x14089452e
008943D0  45 85 F6                        test r14d, r14d
008943D3  74 23                           je 0x1408943f8
008943D5  41 0F BA E5 10                  bt r13d, 0x10
008943DA  73 1C                           jae 0x1408943f8
008943DC  4D 85 FF                        test r15, r15
008943DF  74 17                           je 0x1408943f8
008943E1  8B 43 28                        mov eax, dword ptr [rbx + 0x28]
008943E4  83 E0 07                        and eax, 7
008943E7  83 F8 03                        cmp eax, 3
008943EA  0F 85 C7 00 00 00               jne 0x1408944b7
008943F0  48 8B CB                        mov rcx, rbx
008943F3  E8 78 B9 FF FF                  call 0x14088fd70
008943F8  8B 43 28                        mov eax, dword ptr [rbx + 0x28]
008943FB  0F BA E0 0D                     bt eax, 0xd
008943FF  0F 82 DA 02 00 00               jb 0x1408946df
00894405  0F BA 73 28 10                  btr dword ptr [rbx + 0x28], 0x10
0089440A  48 8B CB                        mov rcx, rbx
0089440D  E8 CE 36 00 00                  call 0x140897ae0
00894412  48 85 FF                        test rdi, rdi
00894415  74 08                           je 0x14089441f
00894417  48 8B CF                        mov rcx, rdi
0089441A  E8 31 4F A6 FF                  call 0x1402f9350
0089441F  48 85 F6                        test rsi, rsi
00894422  74 08                           je 0x14089442c
00894424  48 8B CE                        mov rcx, rsi
00894427  E8 24 4F A6 FF                  call 0x1402f9350
0089442C  41 8B C4                        mov eax, r12d
0089442F  48 83 C4 48                     add rsp, 0x48
00894433  41 5F                           pop r15
00894435  41 5E                           pop r14
00894437  41 5D                           pop r13
00894439  41 5C                           pop r12
0089443B  5F                              pop rdi
0089443C  5E                              pop rsi
0089443D  5D                              pop rbp
0089443E  5B                              pop rbx
0089443F  C3                              ret
00894440  CC                              int3
00894441  8B C5                           mov eax, ebp
00894443  E9 DA FE FF FF                  jmp 0x140894322
00894448  85 C0                           test eax, eax
0089444A  74 B9                           je 0x140894405
0089444C  E9 E0 FE FF FF                  jmp 0x140894331
00894451  33 ED                           xor ebp, ebp
00894453  B8 11 00 00 00                  mov eax, 0x11
00894458  F0 49 0F B1 2E                  lock cmpxchg qword ptr [r14], rbp
0089445D  74 08                           je 0x140894467
0089445F  49 8B CE                        mov rcx, r14
00894462  E8 D9 EF 9C FF                  call 0x140263440
00894467  49 8B CE                        mov rcx, r14
0089446A  E8 91 D1 A4 FF                  call 0x1402e1600
0089446F  45 8B F4                        mov r14d, r12d
00894472  E9 9A FD FF FF                  jmp 0x140894211
00894477  48 8B C5                        mov rax, rbp
0089447A  48 87 81 B8 05 00 00            xchg qword ptr [rcx + 0x5b8], rax
00894481  48 3B C3                        cmp rax, rbx
00894484  0F 85 46 FF FF FF               jne 0x1408943d0
0089448A  B8 01 00 00 00                  mov eax, 1
0089448F  48 89 6B 20                     mov qword ptr [rbx + 0x20], rbp
00894493  66 83 43 E2 FE                  add word ptr [rbx - 0x1e], -2
00894498  44 8B C0                        mov r8d, eax
0089449B  8B D0                           mov edx, eax
0089449D  48 89 6C 24 28                  mov qword ptr [rsp + 0x28], rbp
008944A2  48 81 C1 18 05 00 00            add rcx, 0x518
008944A9  89 6C 24 20                     mov dword ptr [rsp + 0x20], ebp
008944AD  E8 0E 24 AB FF                  call 0x1403468c0
008944B2  E9 19 FF FF FF                  jmp 0x1408943d0
008944B7  45 33 C0                        xor r8d, r8d
008944BA  33 D2                           xor edx, edx
008944BC  83 F8 04                        cmp eax, 4
008944BF  0F 84 E7 01 00 00               je 0x1408946ac
008944C5  49 8D AF 88 00 00 00            lea rbp, [r15 + 0x88]
008944CC  48 8B CD                        mov rcx, rbp
008944CF  E8 5C BD 97 FF                  call 0x140210230
008944D4  F0 48 0F BA 6D 00 00            lock bts qword ptr [rbp], 0
008944DB  4C 8B F0                        mov r14, rax
008944DE  73 0E                           jae 0x1408944ee
008944E0  4C 8B C5                        mov r8, rbp
008944E3  48 8B D0                        mov rdx, rax
008944E6  48 8B CD                        mov rcx, rbp
008944E9  E8 A2 B7 97 FF                  call 0x14020fc90
008944EE  4D 85 F6                        test r14, r14
008944F1  74 05                           je 0x1408944f8
008944F3  41 C6 46 0A 01                  mov byte ptr [r14 + 0xa], 1
008944F8  48 8B D3                        mov rdx, rbx
008944FB  49 8B CF                        mov rcx, r15
008944FE  E8 19 FF 15 00                  call 0x1409f441c
00894503  49 83 CE FF                     or r14, 0xffffffffffffffff
00894507  49 8B C6                        mov rax, r14
0089450A  F0 48 0F C1 45 00               lock xadd qword ptr [rbp], rax
00894510  24 06                           and al, 6
00894512  3C 02                           cmp al, 2
00894514  0F 84 4A 01 00 00               je 0x140894664
0089451A  48 8B CD                        mov rcx, rbp
0089451D  E8 DE D0 A4 FF                  call 0x1402e1600
00894522  66 44 01 73 E2                  add word ptr [rbx - 0x1e], r14w
00894527  33 ED                           xor ebp, ebp
00894529  E9 CA FE FF FF                  jmp 0x1408943f8
0089452E  48 85 F6                        test rsi, rsi
00894531  0F 84 99 FE FF FF               je 0x1408943d0
00894537  45 85 F6                        test r14d, r14d
0089453A  75 0A                           jne 0x140894546
0089453C  41 F6 C5 02                     test r13b, 2
00894540  0F 84 B2 FE FF FF               je 0x1408943f8
00894546  48 8D AF 60 01 00 00            lea rbp, [rdi + 0x160]
0089454D  45 33 C0                        xor r8d, r8d
00894550  48 8B CD                        mov rcx, rbp
00894553  33 D2                           xor edx, edx
00894555  E8 D6 BC 97 FF                  call 0x140210230
0089455A  4C 8B F8                        mov r15, rax
0089455D  33 C0                           xor eax, eax
0089455F  44 8D 48 11                     lea r9d, [rax + 0x11]
00894563  F0 4C 0F B1 4D 00               lock cmpxchg qword ptr [rbp], r9
00894569  74 16                           je 0x140894581
0089456B  4C 8B CD                        mov r9, rbp
0089456E  4D 8B C7                        mov r8, r15
00894571  33 D2                           xor edx, edx
00894573  48 8B CD                        mov rcx, rbp
00894576  E8 D1 BE 97 FF                  call 0x14021044c
0089457B  41 B9 11 00 00 00               mov r9d, 0x11
00894581  33 D2                           xor edx, edx
00894583  44 8D 42 01                     lea r8d, [rdx + 1]
00894587  4D 85 FF                        test r15, r15
0089458A  74 04                           je 0x140894590
0089458C  45 88 47 0A                     mov byte ptr [r15 + 0xa], r8b
00894590  8B 8F A0 01 00 00               mov ecx, dword ptr [rdi + 0x1a0]
00894596  F6 C1 40                        test cl, 0x40
00894599  0F 85 F0 00 00 00               jne 0x14089468f
0089459F  48 89 7B 40                     mov qword ptr [rbx + 0x40], rdi
008945A3  41 8B C0                        mov eax, r8d
008945A6  48 89 73 38                     mov qword ptr [rbx + 0x38], rsi
008945AA  66 44 01 43 E2                  add word ptr [rbx - 0x1e], r8w
008945AF  F0 0F C1 86 90 01 00 00         lock xadd dword ptr [rsi + 0x190], eax
008945B7  41 03 C0                        add eax, r8d
008945BA  48 8B D3                        mov rdx, rbx
008945BD  89 43 48                        mov dword ptr [rbx + 0x48], eax
008945C0  48 8B CF                        mov rcx, rdi
008945C3  48 8B 46 38                     mov rax, qword ptr [rsi + 0x38]
008945C7  48 89 83 80 00 00 00            mov qword ptr [rbx + 0x80], rax
008945CE  E8 65 96 1D 00                  call 0x140a6dc38
008945D3  48 8B CF                        mov rcx, rdi
008945D6  E8 35 23 1E 00                  call 0x140a76910
008945DB  4C 8B BC 24 98 00 00 00         mov r15, qword ptr [rsp + 0x98]
008945E3  33 ED                           xor ebp, ebp
008945E5  E9 E6 FD FF FF                  jmp 0x1408943d0
008945EA  4D 85 FF                        test r15, r15
008945ED  74 0E                           je 0x1408945fd
008945EF  83 F9 03                        cmp ecx, 3
008945F2  75 58                           jne 0x14089464c
008945F4  F7 43 28 00 20 00 00            test dword ptr [rbx + 0x28], 0x2000
008945FB  75 4F                           jne 0x14089464c
008945FD  41 8B C1                        mov eax, r9d
00894600  41 BC 2E 00 00 40               mov r12d, 0x4000002e
00894606  45 84 E9                        test r9b, r13b
00894609  0F 84 22 FD FF FF               je 0x140894331
0089460F  85 C0                           test eax, eax
00894611  0F 85 EE FD FF FF               jne 0x140894405
00894617  E9 15 FD FF FF                  jmp 0x140894331
0089461C  83 FD 10                        cmp ebp, 0x10
0089461F  74 32                           je 0x140894653
00894621  49 8B FC                        mov rdi, r12
00894624  49 8B F4                        mov rsi, r12
00894627  33 ED                           xor ebp, ebp
00894629  48 85 FF                        test rdi, rdi
0089462C  75 43                           jne 0x140894671
0089462E  48 85 F6                        test rsi, rsi
00894631  0F 84 BE FB FF FF               je 0x1408941f5
00894637  48 8B CE                        mov rcx, rsi
0089463A  E8 A1 94 B8 FF                  call 0x14041dae0
0089463F  F6 D8                           neg al
00894641  48 1B C9                        sbb rcx, rcx
00894644  48 23 F1                        and rsi, rcx
00894647  E9 A9 FB FF FF                  jmp 0x1408941f5
0089464C  8B C5                           mov eax, ebp
0089464E  44 8B E5                        mov r12d, ebp
00894651  EB B3                           jmp 0x140894606
00894653  48 8B B4 24 A8 00 00 00         mov rsi, qword ptr [rsp + 0xa8]
0089465B  48 8B 3E                        mov rdi, qword ptr [rsi]
0089465E  48 8B 76 08                     mov rsi, qword ptr [rsi + 8]
00894662  EB C3                           jmp 0x140894627
00894664  48 8B CD                        mov rcx, rbp
00894667  E8 64 17 9D FF                  call 0x140265dd0
0089466C  E9 A9 FE FF FF                  jmp 0x14089451a
00894671  48 8B CF                        mov rcx, rdi
00894674  E8 67 94 B8 FF                  call 0x14041dae0
00894679  F6 D8                           neg al
0089467B  48 1B C9                        sbb rcx, rcx
0089467E  48 23 F9                        and rdi, rcx
00894681  EB AB                           jmp 0x14089462e
00894683  49 8B 3F                        mov rdi, qword ptr [r15]
00894686  49 8B 77 08                     mov rsi, qword ptr [r15 + 8]
0089468A  E9 29 FC FF FF                  jmp 0x1408942b8
0089468F  49 8B C1                        mov rax, r9
00894692  F0 48 0F B1 55 00               lock cmpxchg qword ptr [rbp], rdx
00894698  0F 84 5D 50 28 00               je 0x140b196fb
0089469E  48 8B CD                        mov rcx, rbp
008946A1  E8 9A ED 9C FF                  call 0x140263440
008946A6  90                              nop
008946A7  E9 4F 50 28 00                  jmp 0x140b196fb
008946AC  49 8D AF C8 00 00 00            lea rbp, [r15 + 0xc8]
008946B3  48 8B CD                        mov rcx, rbp
008946B6  E8 75 BB 97 FF                  call 0x140210230
008946BB  F0 48 0F BA 6D 00 00            lock bts qword ptr [rbp], 0
008946C2  4C 8B F0                        mov r14, rax
008946C5  0F 83 3E 50 28 00               jae 0x140b19709
008946CB  4C 8B C5                        mov r8, rbp
008946CE  48 8B D0                        mov rdx, rax
008946D1  48 8B CD                        mov rcx, rbp
008946D4  E8 B7 B5 97 FF                  call 0x14020fc90
008946D9  90                              nop
008946DA  E9 2A 50 28 00                  jmp 0x140b19709
008946DF  83 E0 07                        and eax, 7
008946E2  3C 03                           cmp al, 3
008946E4  0F 85 1B FD FF FF               jne 0x140894405
008946EA  48 8B CB                        mov rcx, rbx
008946ED  E8 7E B6 FF FF                  call 0x14088fd70
008946F2  E9 0E FD FF FF                  jmp 0x140894405
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall AlpcpCancelMessage(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m88;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned int v_stack_p8;
    unsigned __int64 v_stack_p98;
    unsigned __int64 v_stack_pA8;

    v_stack_p18 = a3;
    v_rsp = (v_rsp) - (72);
    a3 = 0;
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 40))))) & (128));
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 40))))) & (7));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 416))) >> (1));
    result = (unsigned int)((result) & (3));
    v_stack_p10 = *(unsigned __int64 *)(a2 + 16);
    v_stack_p8 = (unsigned int)(a1);
    result = (unsigned int)((result) - ((unsigned int)(a3 + 1)));
    if (condition_is_equal) goto loc_00894233;
    v_rbp = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 40))) & (120));
    v_r14 = (((unsigned int)(v_rbp)) == 16) ? 1 : 0;
    if ((unsigned int)(a2) != 0) goto loc_008942F5;
    a2 = 0;
    v_stack_p20 = *(unsigned __int64 *)(a1 + 16);
    result = KeAbPreAcquire(*(unsigned __int64 *)(a1 + 16) - 16, a2, a3, a3 + 1);
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
    if (((*(unsigned int *)(a2 + 40)) & (512)) == 0) goto loc_0089461C;
    v_rbp = 0;
loc_008941F5:
    result = 17;
    if (!(condition_is_equal)) {
        a1 = *(unsigned __int64 *)(a1 + 16) - 16;
        result = ExfReleasePushLockShared(a1, a2, a3, a4);
    }
    result = KeAbPostRelease(*(unsigned __int64 *)(a1 + 16) - 16, a2, a3, a4);
loc_00894211:
    goto loc_008942F7;
loc_00894233:
    v_rbp = (unsigned int)((v_rbp) & (120));
    v_r12 = (((unsigned int)(v_rbp)) == 8) ? 1 : 0;
    if (0 != 0) goto loc_008942F5;
    if (v_stack_p10 == 0) goto loc_008942F5;
    if (*(unsigned __int64 *)(a2 + 184) == 0) goto loc_008942ED;
    a2 = 0;
    result = KeAbPreAcquire(*(unsigned __int64 *)(a2 + 184) - 16, a2, a3, 1);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = *(unsigned __int64 *)(a2 + 184) - 16;
        a3 = 0;
        a2 = 0;
        a1 = *(unsigned __int64 *)(a2 + 184) - 16;
        result = ExfAcquirePushLockSharedEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    if (((*(unsigned int *)(a2 + 40)) & (512)) != 0) goto loc_00894451;
    if (((unsigned int)(v_rbp)) != 8) goto loc_00894683;
loc_008942B8:
    v_rbp = 0;
    v_rdi = *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 184) + 16);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 184) + 16) != 0) {
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 184) + 16);
        result = ObReferenceObjectSafe(a1, a2, a3, a4);
        result = (unsigned __int8)(-(result));
        v_rdi = (*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 184) + 16)) & (a1);
    }
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 184) + 16) == 0) goto loc_00894453;
    result = ObReferenceObjectSafe(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 184) + 16), a2, a3, a4);
    result = (unsigned __int8)(-(result));
    v_rsi = (*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 184) + 16)) & (*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 184) + 16));
    goto loc_00894453;
loc_008942ED:
loc_008942F5:
    v_rbp = 0;
loc_008942F7:
    if ((unsigned int)(*(unsigned __int64 *)(a2 + 184) - 16) == 0) goto loc_008945EA;
    if (v_stack_p10 == 0) goto loc_00894441;
    if (((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 184) + 16))) != 3) goto loc_00894441;
    if (((*(unsigned int *)(a2 + 40)) & (0x2000ULL)) != 0) goto loc_00894441;
loc_00894322:
    if ((((unsigned __int8)(a4)) & ((unsigned __int8)(result))) != 0) goto loc_00894448;
loc_00894331:
    *(unsigned __int8 *)(a2 + 244) = 0;
    *(unsigned int *)(a2 + 240) = 0x280000ULL;
    result = AlpcpReleaseMessageAttributesOnCancel(0, a2, a3, a4);
    result = AlpcpClearOwnerPortMessage(0, a2, a3, a4);
    result = AlpcpTransferQuotaMessage(0, a2, a3, a4);
    if (*(unsigned __int64 *)(a2 + 208) != 0) {
        a2 = *(unsigned int *)(a2 + 264);
        result = PsReleaseProcessWakeCounter(*(unsigned __int64 *)(a2 + 208), a2, a3, a4);
        *(unsigned __int64 *)(a2 + 208) = 0;
    }
    if (*(unsigned __int64 *)(a2 + 216) != 0) {
        a2 = *(unsigned int *)(a2 + 264);
        result = PsReleaseProcessWakeCounter(*(unsigned __int64 *)(a2 + 216), a2, a3, a4);
        *(unsigned __int64 *)(a2 + 216) = 0;
    }
    if (*(unsigned __int64 *)(a2 + 32) != 0) goto loc_00894477;
    if (v_rdi != 0) goto loc_0089452E;
loc_008943D0:
    if ((unsigned int)(*(unsigned __int64 *)(a2 + 184) - 16) == 0) goto loc_008943F8;
    if (condition_is_above_or_equal) goto loc_008943F8;
    if (v_stack_p10 == 0) goto loc_008943F8;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 40))) & (7));
    if (((unsigned int)(result)) != 3) goto loc_008944B7;
    result = AlpcpRemoveMessageFromPendingQueue(a2, a2, a3, a4);
loc_008943F8:
    if (((unsigned int)(result)) < 3) goto loc_008946DF;
loc_00894405:
    result = AlpcpUnlockMessage(a2, a2, a3, a4);
    if (v_rdi != 0) {
        a1 = v_rdi;
        result = ObfDereferenceObject(a1, a2, a3, a4);
    }
    if (v_rsi != 0) {
        a1 = v_rsi;
        result = ObfDereferenceObject(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (72);
    return 259;
loc_00894441:
    goto loc_00894322;
loc_00894448:
    if (0 == 0) goto loc_00894405;
    goto loc_00894331;
loc_00894451:
    v_rbp = 0;
loc_00894453:
    result = 17;
    if (!(condition_is_equal)) {
        a1 = *(unsigned __int64 *)(a2 + 184) - 16;
        result = ExfReleasePushLockShared(a1, a2, a3, a4);
    }
    result = KeAbPostRelease(*(unsigned __int64 *)(a2 + 184) - 16, a2, a3, a4);
    goto loc_00894211;
loc_00894477:
    if (0 != a2) goto loc_008943D0;
    *(unsigned __int64 *)(a2 + 32) = 0;
    v_stack_p28 = 0;
    a1 = (*(unsigned __int64 *)(a2 + 184) - 16) + (0x518ULL);
    v_stack_p20 = 0;
    result = KeReleaseSemaphoreEx(a1, 1, 1, a4);
    goto loc_008943D0;
loc_008944B7:
    a3 = 0;
    a2 = 0;
    if (((unsigned int)(result)) == 4) goto loc_008946AC;
    result = KeAbPreAcquire(v_stack_p10 + 136, a2, a3, a4);
    if (((unsigned int)(result)) < 4) {
        a3 = v_stack_p10 + 136;
        a2 = result;
        a1 = v_stack_p10 + 136;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    result = AlpcpRemoveMessagePort(v_stack_p10, a2, a3, a4);
    v_r14 = (result) | (-1);
    result = (unsigned __int8)((v_r14) & (6));
    if (((unsigned __int8)(result)) == 2) goto loc_00894664;
loc_0089451A:
    result = KeAbPostRelease(v_stack_p10 + 136, a2, a3, a4);
    v_rbp = 0;
    goto loc_008943F8;
loc_0089452E:
    if (v_rsi == 0) goto loc_008943D0;
    if ((unsigned int)(v_r14) != 0) goto loc_00894546;
    if ((((unsigned __int8)(result)) & (2)) == 0) goto loc_008943F8;
loc_00894546:
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_rdi + 352, a2, a3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = v_rdi + 352;
        a3 = 0;
        a2 = 0;
        a1 = v_rdi + 352;
        result = ExfAcquirePushLockSharedEx(a1, a2, a3, a4);
        a4 = 17;
    }
    a2 = 0;
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = (unsigned __int8)(a2 + 1);
    }
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rdi + 416)))) & (64)) != 0) goto loc_0089468F;
    *(unsigned __int64 *)(a2 + 64) = v_rdi;
    *(unsigned __int64 *)(a2 + 56) = v_rsi;
    result = (unsigned int)(((unsigned int)((unsigned int)(a2 + 1))) + ((unsigned int)(a2 + 1)));
    *(unsigned int *)(a2 + 72) = (unsigned int)(result);
    *(unsigned __int64 *)(a2 + 128) = *(unsigned __int64 *)(v_rsi + 56);
    result = AlpcpInsertMessageCanceledQueue(v_rdi, 0, a2 + 1, a4);
    result = AlpcpSignalPortAndUnlock(v_rdi, 0, a2 + 1, a4);
    v_rbp = 0;
    goto loc_008943D0;
loc_008945EA:
    if (v_stack_p98 == 0) goto loc_008945FD;
    if (((unsigned int)(v_rdi)) != 3) goto loc_0089464C;
    if (((*(unsigned int *)(a2 + 40)) & (0x2000ULL)) != 0) goto loc_0089464C;
loc_008945FD:
loc_00894606:
    if ((((unsigned __int8)(a4)) & ((unsigned __int8)(result))) == 0) goto loc_00894331;
    if ((unsigned int)((unsigned int)((unsigned int)(a4))) != 0) goto loc_00894405;
    goto loc_00894331;
loc_0089461C:
    if (0 == 16) goto loc_00894653;
loc_00894627:
    v_rbp = 0;
    if ((unsigned int)(0x4000002EULL) != 0) goto loc_00894671;
loc_0089462E:
    if ((unsigned int)(0x4000002EULL) == 0) goto loc_008941F5;
    result = ObReferenceObjectSafe((unsigned int)(0x4000002EULL), 0, a2 + 1, a4);
    result = (unsigned __int8)(-(result));
    v_rsi = ((unsigned int)(0x4000002EULL)) & ((unsigned int)(0x4000002EULL));
    goto loc_008941F5;
loc_0089464C:
    goto loc_00894606;
loc_00894653:
    goto loc_00894627;
loc_00894664:
    result = ExfTryToWakePushLock(0, 0, a2 + 1, a4);
    goto loc_0089451A;
loc_00894671:
    result = ObReferenceObjectSafe(*(unsigned __int64 *)(v_stack_pA8), 0, a2 + 1, a4);
    result = (unsigned __int8)(-(result));
    v_rdi = (*(unsigned __int64 *)(v_stack_pA8)) & (*(unsigned __int64 *)(v_stack_pA8));
    goto loc_0089462E;
loc_00894683:
    goto loc_008942B8;
loc_0089468F:
    result = ExfReleasePushLockShared(0, 0, a2 + 1, a4);
loc_008946AC:
    result = KeAbPreAcquire(v_stack_p98 + 200, 0, a2 + 1, a4);
    result = ExfAcquirePushLockExclusiveEx(v_stack_p98 + 200, result, v_stack_p98 + 200, a4);
loc_008946DF:
    result = (unsigned int)((result) & (7));
    if (((unsigned __int8)(result)) != 3) goto loc_00894405;
    result = AlpcpRemoveMessageFromPendingQueue(0, result, v_stack_p98 + 200, a4);
    goto loc_00894405;
}
```

## 5. (Beta) C Style

```c
int64_t AlpcpCancelMessage(void *Arg1, void *Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m88;
    uint64_t v_stack_p10;
    uint32_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint32_t v_stack_p8;
    uint64_t v_stack_p98;
    uint64_t v_stack_pA8;

    v_stack_p18 = Arg3;
    local_rsp = (local_rsp) - (72);
    Arg3 = 0;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x28))))) & (128));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x28))))) & (7));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x1A0))) >> (1));
    result = (uint32_t)((result) & (3));
    v_stack_p10 = *(uint64_t *)(arg2 + 0x10);
    v_stack_p8 = (uint32_t)(Arg1);
    result = (uint32_t)((result) - ((uint32_t)(Arg3 + 1)));
    if (condition_is_equal) goto loc_00894233;
    local_rbp = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0x28))) & (120));
    local_r14 = (((uint32_t)(local_rbp)) == 16) ? 1 : 0;
    if ((uint32_t)(Arg2) != 0) goto loc_008942F5;
    Arg2 = 0;
    v_stack_p20 = *(uint64_t *)(arg1 + 0x10);
    result = KeAbPreAcquire(*(uint64_t *)(arg1 + 0x10) - 16, Arg2, Arg3, Arg3 + 1);
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
    if (((*(uint32_t *)(arg2 + 0x28)) & (512)) == 0) goto loc_0089461C;
    local_rbp = 0;
loc_008941F5:
    result = 17;
    if (!(condition_is_equal)) {
        Arg1 = *(uint64_t *)(arg1 + 0x10) - 16;
        result = ExfReleasePushLockShared(Arg1, Arg2, Arg3, a4);
    }
    result = KeAbPostRelease(*(uint64_t *)(arg1 + 0x10) - 16, Arg2, Arg3, a4);
loc_00894211:
    goto loc_008942F7;
loc_00894233:
    local_rbp = (uint32_t)((local_rbp) & (120));
    local_r12 = (((uint32_t)(local_rbp)) == 8) ? 1 : 0;
    if (0 != 0) goto loc_008942F5;
    if (v_stack_p10 == 0) goto loc_008942F5;
    if (*(uint64_t *)(arg2 + 0xB8) == 0) goto loc_008942ED;
    Arg2 = 0;
    result = KeAbPreAcquire(*(uint64_t *)(arg2 + 0xB8) - 16, Arg2, Arg3, 1);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = *(uint64_t *)(arg2 + 0xB8) - 16;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = *(uint64_t *)(arg2 + 0xB8) - 16;
        result = ExfAcquirePushLockSharedEx(Arg1, Arg2, Arg3, a4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    if (((*(uint32_t *)(arg2 + 0x28)) & (512)) != 0) goto loc_00894451;
    if (((uint32_t)(local_rbp)) != 8) goto loc_00894683;
loc_008942B8:
    local_rbp = 0;
    local_rdi = *(uint64_t *)(*(uint64_t *)(arg2 + 0xB8) + 0x10);
    if (*(uint64_t *)(*(uint64_t *)(arg2 + 0xB8) + 0x10) != 0) {
        Arg1 = *(uint64_t *)(*(uint64_t *)(arg2 + 0xB8) + 0x10);
        result = ObReferenceObjectSafe(Arg1, Arg2, Arg3, a4);
        result = (uint8_t)(-(result));
        local_rdi = (*(uint64_t *)(*(uint64_t *)(arg2 + 0xB8) + 0x10)) & (Arg1);
    }
    if (*(uint64_t *)(*(uint64_t *)(arg2 + 0xB8) + 0x10) == 0) goto loc_00894453;
    result = ObReferenceObjectSafe(*(uint64_t *)(*(uint64_t *)(arg2 + 0xB8) + 0x10), Arg2, Arg3, a4);
    result = (uint8_t)(-(result));
    local_rsi = (*(uint64_t *)(*(uint64_t *)(arg2 + 0xB8) + 0x10)) & (*(uint64_t *)(*(uint64_t *)(arg2 + 0xB8) + 0x10));
    goto loc_00894453;
loc_008942ED:
loc_008942F5:
    local_rbp = 0;
loc_008942F7:
    if ((uint32_t)(*(uint64_t *)(arg2 + 0xB8) - 16) == 0) goto loc_008945EA;
    if (v_stack_p10 == 0) goto loc_00894441;
    if (((uint32_t)(*(uint64_t *)(*(uint64_t *)(arg2 + 0xB8) + 0x10))) != 3) goto loc_00894441;
    if (((*(uint32_t *)(arg2 + 0x28)) & (0x2000ULL)) != 0) goto loc_00894441;
loc_00894322:
    if ((((uint8_t)(a4)) & ((uint8_t)(result))) != 0) goto loc_00894448;
loc_00894331:
    *(uint8_t *)(arg2 + 0xF4) = 0;
    *(uint32_t *)(arg2 + 0xF0) = 0x280000ULL;
    result = AlpcpReleaseMessageAttributesOnCancel(0, Arg2, Arg3, a4);
    result = AlpcpClearOwnerPortMessage(0, Arg2, Arg3, a4);
    result = AlpcpTransferQuotaMessage(0, Arg2, Arg3, a4);
    if (*(uint64_t *)(arg2 + 0xD0) != 0) {
        Arg2 = *(uint32_t *)(arg2 + 0x108);
        result = PsReleaseProcessWakeCounter(*(uint64_t *)(arg2 + 0xD0), Arg2, Arg3, a4);
        *(uint64_t *)(arg2 + 0xD0) = 0;
    }
    if (*(uint64_t *)(arg2 + 0xD8) != 0) {
        Arg2 = *(uint32_t *)(arg2 + 0x108);
        result = PsReleaseProcessWakeCounter(*(uint64_t *)(arg2 + 0xD8), Arg2, Arg3, a4);
        *(uint64_t *)(arg2 + 0xD8) = 0;
    }
    if (*(uint64_t *)(arg2 + 0x20) != 0) goto loc_00894477;
    if (local_rdi != 0) goto loc_0089452E;
loc_008943D0:
    if ((uint32_t)(*(uint64_t *)(arg2 + 0xB8) - 16) == 0) goto loc_008943F8;
    if (condition_is_above_or_equal) goto loc_008943F8;
    if (v_stack_p10 == 0) goto loc_008943F8;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0x28))) & (7));
    if (((uint32_t)(result)) != 3) goto loc_008944B7;
    result = AlpcpRemoveMessageFromPendingQueue(Arg2, Arg2, Arg3, a4);
loc_008943F8:
    if (((uint32_t)(result)) < 3) goto loc_008946DF;
loc_00894405:
    result = AlpcpUnlockMessage(Arg2, Arg2, Arg3, a4);
    if (local_rdi != 0) {
        Arg1 = local_rdi;
        result = ObfDereferenceObject(Arg1, Arg2, Arg3, a4);
    }
    if (local_rsi != 0) {
        Arg1 = local_rsi;
        result = ObfDereferenceObject(Arg1, Arg2, Arg3, a4);
    }
    local_rsp = (local_rsp) + (72);
    return 259;
loc_00894441:
    goto loc_00894322;
loc_00894448:
    if (0 == 0) goto loc_00894405;
    goto loc_00894331;
loc_00894451:
    local_rbp = 0;
loc_00894453:
    result = 17;
    if (!(condition_is_equal)) {
        Arg1 = *(uint64_t *)(arg2 + 0xB8) - 16;
        result = ExfReleasePushLockShared(Arg1, Arg2, Arg3, a4);
    }
    result = KeAbPostRelease(*(uint64_t *)(arg2 + 0xB8) - 16, Arg2, Arg3, a4);
    goto loc_00894211;
loc_00894477:
    if (0 != Arg2) goto loc_008943D0;
    *(uint64_t *)(arg2 + 0x20) = 0;
    v_stack_p28 = 0;
    Arg1 = (*(uint64_t *)(arg2 + 0xB8) - 16) + (0x518ULL);
    v_stack_p20 = 0;
    result = KeReleaseSemaphoreEx(Arg1, 1, 1, a4);
    goto loc_008943D0;
loc_008944B7:
    Arg3 = 0;
    Arg2 = 0;
    if (((uint32_t)(result)) == 4) goto loc_008946AC;
    result = KeAbPreAcquire(v_stack_p10 + 136, Arg2, Arg3, a4);
    if (((uint32_t)(result)) < 4) {
        Arg3 = v_stack_p10 + 136;
        Arg2 = result;
        Arg1 = v_stack_p10 + 136;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, a4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    result = AlpcpRemoveMessagePort(v_stack_p10, Arg2, Arg3, a4);
    local_r14 = (result) | (-1);
    result = (uint8_t)((local_r14) & (6));
    if (((uint8_t)(result)) == 2) goto loc_00894664;
loc_0089451A:
    result = KeAbPostRelease(v_stack_p10 + 136, Arg2, Arg3, a4);
    local_rbp = 0;
    goto loc_008943F8;
loc_0089452E:
    if (local_rsi == 0) goto loc_008943D0;
    if ((uint32_t)(local_r14) != 0) goto loc_00894546;
    if ((((uint8_t)(result)) & (2)) == 0) goto loc_008943F8;
loc_00894546:
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(local_rdi + 352, Arg2, Arg3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = local_rdi + 352;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = local_rdi + 352;
        result = ExfAcquirePushLockSharedEx(Arg1, Arg2, Arg3, a4);
        a4 = 17;
    }
    Arg2 = 0;
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = (uint8_t)(Arg2 + 1);
    }
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x1A0)))) & (64)) != 0) goto loc_0089468F;
    *(uint64_t *)(arg2 + 0x40) = local_rdi;
    *(uint64_t *)(arg2 + 0x38) = local_rsi;
    result = (uint32_t)(((uint32_t)((uint32_t)(Arg2 + 1))) + ((uint32_t)(Arg2 + 1)));
    *(uint32_t *)(arg2 + 0x48) = (uint32_t)(result);
    *(uint64_t *)(arg2 + 0x80) = *(uint64_t *)(local_rsi + 0x38);
    result = AlpcpInsertMessageCanceledQueue(local_rdi, 0, Arg2 + 1, a4);
    result = AlpcpSignalPortAndUnlock(local_rdi, 0, Arg2 + 1, a4);
    local_rbp = 0;
    goto loc_008943D0;
loc_008945EA:
    if (v_stack_p98 == 0) goto loc_008945FD;
    if (((uint32_t)(local_rdi)) != 3) goto loc_0089464C;
    if (((*(uint32_t *)(arg2 + 0x28)) & (0x2000ULL)) != 0) goto loc_0089464C;
loc_008945FD:
loc_00894606:
    if ((((uint8_t)(a4)) & ((uint8_t)(result))) == 0) goto loc_00894331;
    if ((uint32_t)((uint32_t)((uint32_t)(a4))) != 0) goto loc_00894405;
    goto loc_00894331;
loc_0089461C:
    if (0 == 16) goto loc_00894653;
loc_00894627:
    local_rbp = 0;
    if ((uint32_t)(0x4000002EULL) != 0) goto loc_00894671;
loc_0089462E:
    if ((uint32_t)(0x4000002EULL) == 0) goto loc_008941F5;
    result = ObReferenceObjectSafe((uint32_t)(0x4000002EULL), 0, Arg2 + 1, a4);
    result = (uint8_t)(-(result));
    local_rsi = ((uint32_t)(0x4000002EULL)) & ((uint32_t)(0x4000002EULL));
    goto loc_008941F5;
loc_0089464C:
    goto loc_00894606;
loc_00894653:
    goto loc_00894627;
loc_00894664:
    result = ExfTryToWakePushLock(0, 0, Arg2 + 1, a4);
    goto loc_0089451A;
loc_00894671:
    result = ObReferenceObjectSafe(*(uint64_t *)(v_stack_pA8), 0, Arg2 + 1, a4);
    result = (uint8_t)(-(result));
    local_rdi = (*(uint64_t *)(v_stack_pA8)) & (*(uint64_t *)(v_stack_pA8));
    goto loc_0089462E;
loc_00894683:
    goto loc_008942B8;
loc_0089468F:
    result = ExfReleasePushLockShared(0, 0, Arg2 + 1, a4);
loc_008946AC:
    result = KeAbPreAcquire(v_stack_p98 + 200, 0, Arg2 + 1, a4);
    result = ExfAcquirePushLockExclusiveEx(v_stack_p98 + 200, result, v_stack_p98 + 200, a4);
loc_008946DF:
    result = (uint32_t)((result) & (7));
    if (((uint8_t)(result)) != 3) goto loc_00894405;
    result = AlpcpRemoveMessageFromPendingQueue(0, result, v_stack_p98 + 200, a4);
    goto loc_00894405;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x1A0` | `32` | `R` |
| `Arg2` | `- 0x1E` | `16` | `R/W` |
| `Arg2` | `+ 0x10` | `64` | `R` |
| `Arg2` | `+ 0x20` | `64` | `R` |
| `Arg2` | `+ 0x20` | `64` | `W` |
| `Arg2` | `+ 0x28` | `32` | `R` |
| `Arg2` | `+ 0x28` | `32` | `R/W` |
| `Arg2` | `+ 0x38` | `64` | `W` |
| `Arg2` | `+ 0x40` | `64` | `W` |
| `Arg2` | `+ 0x48` | `32` | `W` |
| `Arg2` | `+ 0x80` | `64` | `W` |
| `Arg2` | `+ 0xB8` | `64` | `R` |
| `Arg2` | `+ 0xD0` | `64` | `R` |
| `Arg2` | `+ 0xD0` | `64` | `W` |
| `Arg2` | `+ 0xD8` | `64` | `R` |
| `Arg2` | `+ 0xD8` | `64` | `W` |
| `Arg2` | `+ 0xF0` | `32` | `W` |
| `Arg2` | `+ 0xF4` | `8` | `W` |
| `Arg2` | `+ 0xF4` | `16` | `R/W` |
| `Arg2` | `+ 0x108` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00894120&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
