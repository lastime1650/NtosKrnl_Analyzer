# sub_002546EC

- RVA: `0x002546EC`–`0x002553A1` (길이 `3,253` bytes)
- VA: `0x00000001402546EC`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006376C`
- 디코드: `791`개 명령, `3,253/3,253` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **44**; 고유 호출 대상: **30**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **8**

### Outgoing calls
- `0x002547EA` → [KiIsThreadExemptFromForcePark](../4D/KiIsThreadExemptFromForcePark_function_004D7B80.md) (function, `0x004D7B80`)
- `0x0025483D` → [KiUpdateLocalReadyQueueStatisticsOnInsertion](../4A/KiUpdateLocalReadyQueueStatisticsOnInsertion_function_004A9290.md) (function, `0x004A9290`)
- `0x00254857` → [KiComputeThreadAffinity](../39/KiComputeThreadAffinity_function_00399DE0.md) (function, `0x00399DE0`)
- `0x00254902` → [KxWaitForLockOwnerShip](KxWaitForLockOwnerShip_function_00257EB0.md) (function, `0x00257EB0`)
- `0x00254918` → [KiReleasePrcbLocksForIsolationUnit](../39/KiReleasePrcbLocksForIsolationUnit_function_00399C50.md) (function, `0x00399C50`)
- `0x00254943` → [KiReadGuestSchedulerAssistPriority](../30/KiReadGuestSchedulerAssistPriority_function_00304BE4.md) (function, `0x00304BE4`)
- `0x0025496B` → [KiComputeThreadPriority](../3C/KiComputeThreadPriority_function_003C45F4.md) (function, `0x003C45F4`)
- `0x00254A1B` → [KiSetPriorityBoost](../39/KiSetPriorityBoost_function_00398A40.md) (function, `0x00398A40`)
- `0x00254A49` → [KiIsThreadExemptFromForcePark](../4D/KiIsThreadExemptFromForcePark_function_004D7B80.md) (function, `0x004D7B80`)
- `0x00254A5C` → [KiArmForceParkDutyCyclingForSharedReadyQueue](../4F/KiArmForceParkDutyCyclingForSharedReadyQueue_function_004FB604.md) (function, `0x004FB604`)
- `0x00254A88` → [KeIsForceParkingEnabled](../21/KeIsForceParkingEnabled_function_00218F20.md) (function, `0x00218F20`)
- `0x00254B23` → [KiHeteroAttemptPreemptionSwapOnSubNode](../3C/KiHeteroAttemptPreemptionSwapOnSubNode_function_003C1144.md) (function, `0x003C1144`)
- `0x00254B73` → [KiAcquirePrcbLocksForPreemptionAttemptSlowPath](../43/KiAcquirePrcbLocksForPreemptionAttemptSlowPath_function_00434910.md) (function, `0x00434910`)
- `0x00254B87` → [KiAcquirePrcbLocksForPreemptionAttemptSlowPath](../43/KiAcquirePrcbLocksForPreemptionAttemptSlowPath_function_00434910.md) (function, `0x00434910`)
- `0x00254BEB` → [KiComputeNewPriority](../3C/KiComputeNewPriority_function_003C2D8C.md) (function, `0x003C2D8C`)
- `0x00254CC2` → [KiCommitRescheduleContextEntry](../30/KiCommitRescheduleContextEntry_function_0030CFD0.md) (function, `0x0030CFD0`)
- `0x00254D86` → [KiInsertDeferredReadyList](../20/KiInsertDeferredReadyList_function_00201310.md) (function, `0x00201310`)
- `0x00254DB6` → [EtwTraceXSchedulerPriorityUpdate](../4D/EtwTraceXSchedulerPriorityUpdate_function_004D2358.md) (function, `0x004D2358`)
- `0x00254DC6` → [KiComputeNewPriority](../3C/KiComputeNewPriority_function_003C2D8C.md) (function, `0x003C2D8C`)
- `0x00254DDD` → [KiUpdateThreadPriority](KiUpdateThreadPriority_function_00257810.md) (function, `0x00257810`)
- `0x00254DE8` → [KiTryScheduleNextForegroundBoost](../47/KiTryScheduleNextForegroundBoost_function_0047B51C.md) (function, `0x0047B51C`)
- `0x00254E4D` → [KiIsPrcbThread](../35/KiIsPrcbThread_function_00353230.md) (function, `0x00353230`)
- `0x00254EEE` → [KiIsPrcbThread](../35/KiIsPrcbThread_function_00353230.md) (function, `0x00353230`)
- `0x00254F6F` → [KiIsPrcbThread](../35/KiIsPrcbThread_function_00353230.md) (function, `0x00353230`)
- `0x00254F99` → [KiIsThreadRankBiased](../4F/KiIsThreadRankBiased_function_004F81BC.md) (function, `0x004F81BC`)
- `0x0025501E` → [KiIsPrcbThread](../35/KiIsPrcbThread_function_00353230.md) (function, `0x00353230`)
- `0x00255043` → [KiInsertDeferredReadyList](../20/KiInsertDeferredReadyList_function_00201310.md) (function, `0x00201310`)
- `0x00255066` → [KiIsPrcbThread](../35/KiIsPrcbThread_function_00353230.md) (function, `0x00353230`)
- `0x0025508B` → [KiInsertDeferredReadyList](../20/KiInsertDeferredReadyList_function_00201310.md) (function, `0x00201310`)
- `0x00255095` → [KiIsPrcbThread](../35/KiIsPrcbThread_function_00353230.md) (function, `0x00353230`)
- `0x002550BA` → [KiInsertDeferredReadyList](../20/KiInsertDeferredReadyList_function_00201310.md) (function, `0x00201310`)
- `0x002550C4` → [KiIsPrcbThread](../35/KiIsPrcbThread_function_00353230.md) (function, `0x00353230`)
- `0x002550E9` → [KiInsertDeferredReadyList](../20/KiInsertDeferredReadyList_function_00201310.md) (function, `0x00201310`)
- `0x0025511F` → [EtwTraceThreadAffinity](../3C/EtwTraceThreadAffinity_function_003C29A0.md) (function, `0x003C29A0`)
- `0x00255171` → [KiAbQueueAutoBoostDpc](../20/KiAbQueueAutoBoostDpc_function_002074D0.md) (function, `0x002074D0`)
- `0x0025519E` → [KiIsThreadStateControlledByProcessor](../30/KiIsThreadStateControlledByProcessor_function_00306254.md) (function, `0x00306254`)
- `0x002551B0` → [KiUpdateVPBackingThreadPriority](../30/KiUpdateVPBackingThreadPriority_function_00306040.md) (function, `0x00306040`)
- `0x00255236` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0025524B` → [KiUpdateThreadPriority](KiUpdateThreadPriority_function_00257810.md) (function, `0x00257810`)
- `0x002552B8` → [KiScheduleNextForegroundBoost](../5C/KiScheduleNextForegroundBoost_function_005C6670.md) (function, `0x005C6670`)
- `0x002552C5` → [KeFindFirstSetLeftAffinityEx](../45/KeFindFirstSetLeftAffinityEx_function_004530E0.md) (function, `0x004530E0`)
- `0x00255304` → [KeFindBiasedSetBitGroupMask](../41/KeFindBiasedSetBitGroupMask_function_00418AFC.md) (function, `0x00418AFC`)
- `0x00255350` → [EtwTraceIdealProcessor](../3C/EtwTraceIdealProcessor_function_003C0808.md) (function, `0x003C0808`)
- `0x0025538A` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0025485C` → RVA `0x00FC6B04` (`ALMOSTRO`; read)
- `0x00254862` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x00254A09` → RVA `0x00FC6C4C` (`ALMOSTRO`; read)
- `0x00254C1D` → RVA `0x00FCFF00` (`CACHEALI`; read)
- `0x00254C89` → RVA `0x00FC6B14` (`ALMOSTRO`; read)
- `0x002552E6` → RVA `0x00FC6D10` (`ALMOSTRO`; read)
- `0x00255330` → RVA `0x00FC6B10` (`ALMOSTRO`; read)
- `0x0025536D` → RVA `0x25664473` (`image boundary/outside`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **86**
  - `0x00254717` → [sub_00254461 + 0x41](Unknown_function_00254461.md) (`tail-transfer`)
  - `0x00254736` → [sub_0025308F + 0x15B](Unknown_function_0025308F.md) (`tail-transfer`)
  - `0x0025473E` → [sub_0025308F + 0x452](Unknown_function_0025308F.md) (`tail-transfer`)
  - `0x0025474F` → [sub_0025308F + 0x1380](Unknown_function_0025308F.md) (`tail-transfer`)
  - `0x0025477A` → [sub_0025308F + 0x108E](Unknown_function_0025308F.md) (`tail-transfer`)
  - `0x0025479B` → [sub_0025308F + 0x1086](Unknown_function_0025308F.md) (`tail-transfer`)
  - `0x002547B6` → [sub_0025308F + 0x419](Unknown_function_0025308F.md) (`tail-transfer`)
  - `0x002547BE` → [sub_0025308F + 0x116A](Unknown_function_0025308F.md) (`tail-transfer`)
  - `0x002547C6` → [sub_0025308F + 0x198](Unknown_function_0025308F.md) (`tail-transfer`)
  - `0x002547E2` → [sub_0025308F + 0x198](Unknown_function_0025308F.md) (`tail-transfer`)
  - `0x002547F1` → [sub_0025308F + 0x112D](Unknown_function_0025308F.md) (`tail-transfer`)
  - `0x002547F7` → [sub_0025308F + 0x33F](Unknown_function_0025308F.md) (`tail-transfer`)
  - `0x002547FF` → [sub_0025308F + 0x1123](Unknown_function_0025308F.md) (`tail-transfer`)
  - `0x0025480B` → [sub_00254461 + 0x41](Unknown_function_00254461.md) (`tail-transfer`)
  - `0x00254844` → [sub_00254461 + 0x11F](Unknown_function_00254461.md) (`tail-transfer`)
  - `0x0025484E` → [sub_0025308F + 0x207](Unknown_function_0025308F.md) (`tail-transfer`)
  - `0x0025487D` → [sub_0025308F + 0x20C](Unknown_function_0025308F.md) (`tail-transfer`)
  - `0x0025488B` → [sub_0025308F + 0xC41](Unknown_function_0025308F.md) (`tail-transfer`)
  - `0x0025489A` → [sub_0025308F + 0xFCE](Unknown_function_0025308F.md) (`tail-transfer`)
  - `0x002548AB` → [sub_0025308F + 0xE0](Unknown_function_0025308F.md) (`tail-transfer`)
  - `0x002548C3` → [sub_0025308F + 0x7D](Unknown_function_0025308F.md) (`tail-transfer`)
  - `0x002548EB` → [sub_0025308F + 0x130E](Unknown_function_0025308F.md) (`tail-transfer`)
  - `0x002548F3` → [sub_0025308F + 0x32D](Unknown_function_0025308F.md) (`tail-transfer`)
  - `0x002548F9` → [sub_0025308F + 0x112D](Unknown_function_0025308F.md) (`tail-transfer`)
  - `0x00254907` → [sub_00254461 + 0x27](Unknown_function_00254461.md) (`tail-transfer`)
  - `0x0025490F` → [sub_0025308F + 0xFCE](Unknown_function_0025308F.md) (`tail-transfer`)
  - `0x00254929` → [sub_0025308F + 0x911](Unknown_function_0025308F.md) (`tail-transfer`)
  - `0x002549C7` → [sub_0025308F + 0x15](Unknown_function_0025308F.md) (`tail-transfer`)
  - `0x00254A20` → [sub_0025308F + 0x144](Unknown_function_0025308F.md) (`tail-transfer`)
  - `0x00254A2E` → [sub_00254461 + 0x17F](Unknown_function_00254461.md) (`tail-transfer`)
  - `0x00254A37` → [sub_00254461 + 0x115](Unknown_function_00254461.md) (`tail-transfer`)
  - `0x00254A40` → [sub_00254461 + 0xBC](Unknown_function_00254461.md) (`tail-transfer`)
  - `0x00254A50` → [sub_00254461 + 0xBC](Unknown_function_00254461.md) (`tail-transfer`)
  - `0x00254A61` → [sub_00254461 + 0xBC](Unknown_function_00254461.md) (`tail-transfer`)
  - `0x00254A7C` → [sub_00254461 + 0x95](Unknown_function_00254461.md) (`tail-transfer`)
  - `0x00254AB3` → [sub_0025308F + 0x419](Unknown_function_0025308F.md) (`tail-transfer`)
  - `0x00254ABB` → [sub_0025308F + 0x144](Unknown_function_0025308F.md) (`tail-transfer`)
  - `0x00254AD6` → [sub_0025308F + 0x144](Unknown_function_0025308F.md) (`tail-transfer`)
  - `0x00254AE3` → [sub_0025308F + 0x144](Unknown_function_0025308F.md) (`tail-transfer`)
  - `0x00254AF3` → [sub_00254461 + 0x135](Unknown_function_00254461.md) (`tail-transfer`)
  - `0x00254B2A` → [sub_0025308F + 0x10A9](Unknown_function_0025308F.md) (`tail-transfer`)
  - `0x00254B30` → [sub_0025308F + 0x102F](Unknown_function_0025308F.md) (`tail-transfer`)
  - `0x00254B78` → [sub_0025308F + 0x809](Unknown_function_0025308F.md) (`tail-transfer`)
  - `0x00254B8C` → [sub_0025308F + 0x10F1](Unknown_function_0025308F.md) (`tail-transfer`)
  - `0x00254BA4` → [sub_00254461 + 0x6C](Unknown_function_00254461.md) (`tail-transfer`)
  - `0x00254BB7` → [sub_0025308F + 0xF8F](Unknown_function_0025308F.md) (`tail-transfer`)
  - `0x00254BDB` → [sub_0025308F + 0xE0](Unknown_function_0025308F.md) (`tail-transfer`)
  - `0x00254BF0` → [sub_0025308F + 0xE0](Unknown_function_0025308F.md) (`tail-transfer`)
  - `0x00254C03` → [sub_0025308F + 0x11A7](Unknown_function_0025308F.md) (`tail-transfer`)
  - `0x00254C0B` → [sub_0025308F + 0x11E9](Unknown_function_0025308F.md) (`tail-transfer`)
  - `0x00254D39` → [sub_0025308F + 0xE12](Unknown_function_0025308F.md) (`tail-transfer`)
  - `0x00254D53` → [sub_0025308F + 0xE12](Unknown_function_0025308F.md) (`tail-transfer`)
  - `0x00254DED` → [sub_0025308F + 0x144](Unknown_function_0025308F.md) (`tail-transfer`)
  - `0x00254DF4` → [sub_0025308F + 0x225](Unknown_function_0025308F.md) (`tail-transfer`)
  - `0x00254DFC` → [sub_0025308F + 0x227](Unknown_function_0025308F.md) (`tail-transfer`)
  - `0x00254E54` → [sub_0025308F + 0x5FA](Unknown_function_0025308F.md) (`tail-transfer`)
  - `0x00254E64` → [sub_0025308F + 0x5FA](Unknown_function_0025308F.md) (`tail-transfer`)
  - `0x00254F11` → [sub_0025308F + 0x60A](Unknown_function_0025308F.md) (`tail-transfer`)
  - `0x00254F8E` → [sub_0025308F + 0x1DD](Unknown_function_0025308F.md) (`tail-transfer`)
  - `0x00254FA0` → [sub_0025308F + 0x2A6](Unknown_function_0025308F.md) (`tail-transfer`)
  - `0x00254FA9` → [sub_0025308F + 0x2A6](Unknown_function_0025308F.md) (`tail-transfer`)
  - `0x00254FB2` → [sub_0025308F + 0x2A6](Unknown_function_0025308F.md) (`tail-transfer`)
  - `0x00254FE4` → [sub_0025308F + 0x512](Unknown_function_0025308F.md) (`tail-transfer`)
  - `0x00255015` → [sub_0025308F + 0x512](Unknown_function_0025308F.md) (`tail-transfer`)
  - `0x00255025` → [sub_0025308F + 0x5AD](Unknown_function_0025308F.md) (`tail-transfer`)
  - `0x00255048` → [sub_0025308F + 0x5AD](Unknown_function_0025308F.md) (`tail-transfer`)
  - `0x00255055` → [sub_0025308F + 0x23C](Unknown_function_0025308F.md) (`tail-transfer`)
  - `0x00255147` → [sub_0025308F + 0xFC](Unknown_function_0025308F.md) (`tail-transfer`)
  - `0x00255157` → [sub_0025308F + 0xFC](Unknown_function_0025308F.md) (`tail-transfer`)
  - `0x00255176` → [sub_0025308F + 0xFC](Unknown_function_0025308F.md) (`tail-transfer`)
  - `0x00255184` → [sub_0025308F + 0xFC](Unknown_function_0025308F.md) (`tail-transfer`)
  - `0x002551C6` → [sub_0025308F + 0x462](Unknown_function_0025308F.md) (`tail-transfer`)
  - `0x002551D0` → [sub_0025308F + 0x462](Unknown_function_0025308F.md) (`tail-transfer`)
  - `0x002551E9` → [sub_00254461 + 0x21B](Unknown_function_00254461.md) (`tail-transfer`)
  - `0x002551EF` → [sub_00254461 + 0x205](Unknown_function_00254461.md) (`tail-transfer`)
  - `0x00255200` → [sub_0025308F + 0x462](Unknown_function_0025308F.md) (`tail-transfer`)
  - `0x0025521D` → [sub_006D8256](../6D/Unknown_function_006D8256.md) (`tail-transfer`)
  - `0x00255299` → [sub_0025308F + 0xE0](Unknown_function_0025308F.md) (`tail-transfer`)
  - `0x002552A6` → [sub_0025308F + 0xE0](Unknown_function_0025308F.md) (`tail-transfer`)
  - `0x002552B0` → [sub_0025308F + 0xE0](Unknown_function_0025308F.md) (`tail-transfer`)
  - `0x002552BD` → [sub_0025308F + 0x133](Unknown_function_0025308F.md) (`tail-transfer`)
  - `0x002552E1` → [sub_0025308F + 0x675](Unknown_function_0025308F.md) (`tail-transfer`)
  - `0x002552F2` → [sub_0025308F + 0x8E0](Unknown_function_0025308F.md) (`tail-transfer`)
  - `0x002552F8` → [sub_0025308F + 0x8DB](Unknown_function_0025308F.md) (`tail-transfer`)
  - `0x00255311` → [sub_0025308F + 0xA75](Unknown_function_0025308F.md) (`tail-transfer`)
  - `0x0025532B` → [sub_00254461 + 0x222](Unknown_function_00254461.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002546EC  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
002546F1  49 8D 86 44 08 00 00            lea rax, [r14 + 0x844]
002546F8  48 C1 E0 04                     shl rax, 4
002546FC  48 03 C6                        add rax, rsi
002546FF  48 8D 8B D8 00 00 00            lea rcx, [rbx + 0xd8]
00254706  39 7C 24 58                     cmp dword ptr [rsp + 0x58], edi
0025470A  0F 85 F4 00 00 00               jne 0x140254804
00254710  48 8B 50 08                     mov rdx, qword ptr [rax + 8]
00254714  48 39 02                        cmp qword ptr [rdx], rax
00254717  0F 85 85 FD FF FF               jne 0x1402544a2
0025471D  48 89 01                        mov qword ptr [rcx], rax
00254720  48 89 51 08                     mov qword ptr [rcx + 8], rdx
00254724  48 89 0A                        mov qword ptr [rdx], rcx
00254727  48 89 48 08                     mov qword ptr [rax + 8], rcx
0025472B  E9 F7 00 00 00                  jmp 0x140254827
00254730  88 83 04 02 00 00               mov byte ptr [rbx + 0x204], al
00254736  E9 AF EA FF FF                  jmp 0x1402531ea
0025473B  80 0B 04                        or byte ptr [rbx], 4
0025473E  E9 9E ED FF FF                  jmp 0x1402534e1
00254743  B9 01 00 00 00                  mov ecx, 1
00254748  4C 8D 45 28                     lea r8, [rbp + 0x28]
0025474C  44 8B C9                        mov r9d, ecx
0025474F  E9 BB FC FF FF                  jmp 0x14025440f
00254754  45 85 C0                        test r8d, r8d
00254757  0F 84 53 01 00 00               je 0x1402548b0
0025475D  41 83 F8 01                     cmp r8d, 1
00254761  75 0F                           jne 0x140254772
00254763  48 8B 82 58 8E 00 00            mov rax, qword ptr [rdx + 0x8e58]
0025476A  44 0F B6 08                     movzx r9d, byte ptr [rax]
0025476E  4C 8D 50 08                     lea r10, [rax + 8]
00254772  BA 01 00 00 00                  mov edx, 1
00254777  45 85 C9                        test r9d, r9d
0025477A  0F 84 9D F9 FF FF               je 0x14025411d
00254780  45 8B C1                        mov r8d, r9d
00254783  49 8B 02                        mov rax, qword ptr [r10]
00254786  4D 8D 52 08                     lea r10, [r10 + 8]
0025478A  0F B6 40 23                     movzx eax, byte ptr [rax + 0x23]
0025478E  F6 D0                           not al
00254790  83 E0 01                        and eax, 1
00254793  23 D0                           and edx, eax
00254795  49 83 E8 01                     sub r8, 1
00254799  75 E8                           jne 0x140254783
0025479B  E9 75 F9 FF FF                  jmp 0x140254115
002547A0  41 F6 45 23 10                  test byte ptr [r13 + 0x23], 0x10
002547A5  0F 85 D6 02 00 00               jne 0x140254a81
002547AB  49 8B 85 48 8E 00 00            mov rax, qword ptr [r13 + 0x8e48]
002547B2  48 89 43 E8                     mov qword ptr [rbx - 0x18], rax
002547B6  E9 ED EC FF FF                  jmp 0x1402534a8
002547BB  48 8B D7                        mov rdx, rdi
002547BE  E9 36 FA FF FF                  jmp 0x1402541f9
002547C3  83 F8 06                        cmp eax, 6
002547C6  0F 87 5B EA FF FF               ja 0x140253227
002547CC  41 8B 8C 83 5C 53 25 00         mov ecx, dword ptr [r11 + rax*4 + 0x25535c]
002547D4  49 03 CB                        add rcx, r11
002547D7  FF E1                           jmp rcx
002547D9  CC                              int3
002547DA  CC                              int3
002547DB  CC                              int3
002547DC  CC                              int3
002547DD  BA 12 00 00 00                  mov edx, 0x12
002547E2  E9 40 EA FF FF                  jmp 0x140253227
002547E7  48 8B CB                        mov rcx, rbx
002547EA  E8 91 33 28 00                  call 0x1404d7b80
002547EF  84 C0                           test al, al
002547F1  0F 84 C5 F9 FF FF               je 0x1402541bc
002547F7  E9 D2 EB FF FF                  jmp 0x1402533ce
002547FC  4C 8B CF                        mov r9, rdi
002547FF  E9 AE F9 FF FF                  jmp 0x1402541b2
00254804  48 8B 10                        mov rdx, qword ptr [rax]
00254807  48 39 42 08                     cmp qword ptr [rdx + 8], rax
0025480B  0F 85 91 FC FF FF               jne 0x1402544a2
00254811  48 89 11                        mov qword ptr [rcx], rdx
00254814  48 89 41 08                     mov qword ptr [rcx + 8], rax
00254818  48 89 4A 08                     mov qword ptr [rdx + 8], rcx
0025481C  48 89 08                        mov qword ptr [rax], rcx
0025481F  44 0F AB B6 DC 83 00 00         bts dword ptr [rsi + 0x83dc], r14d
00254827  8B 86 D8 83 00 00               mov eax, dword ptr [rsi + 0x83d8]
0025482D  48 8B D3                        mov rdx, rbx
00254830  44 0F AB F0                     bts eax, r14d
00254834  48 8B CE                        mov rcx, rsi
00254837  89 86 D8 83 00 00               mov dword ptr [rsi + 0x83d8], eax
0025483D  E8 4E 4A 25 00                  call 0x1404a9290
00254842  8B C7                           mov eax, edi
00254844  E9 37 FD FF FF                  jmp 0x140254580
00254849  8B 43 74                        mov eax, dword ptr [rbx + 0x74]
0025484C  A8 08                           test al, 8
0025484E  0F 85 42 EA FF FF               jne 0x140253296
00254854  48 8B CB                        mov rcx, rbx
00254857  E8 84 55 14 00                  call 0x140399de0
0025485C  8B 0D A2 22 D7 00               mov ecx, dword ptr [rip + 0xd722a2]
00254862  4C 8D 1D 97 B7 DA FF            lea r11, [rip - 0x254869]
00254869  8B 55 C0                        mov edx, dword ptr [rbp - 0x40]
0025486C  44 8B C0                        mov r8d, eax
0025486F  C1 E9 0C                        shr ecx, 0xc
00254872  80 E1 01                        and cl, 1
00254875  44 22 C1                        and r8b, cl
00254878  44 89 44 24 78                  mov dword ptr [rsp + 0x78], r8d
0025487D  E9 19 EA FF FF                  jmp 0x14025329b
00254882  4C 8D 45 18                     lea r8, [rbp + 0x18]
00254886  BA 01 00 00 00                  mov edx, 1
0025488B  E9 40 F4 FF FF                  jmp 0x140253cd0
00254890  48 8B 96 80 00 00 00            mov rdx, qword ptr [rsi + 0x80]
00254897  49 23 D0                        and rdx, r8
0025489A  E9 BE F7 FF FF                  jmp 0x14025405d
0025489F  45 84 E4                        test r12b, r12b
002548A2  0F 85 14 03 00 00               jne 0x140254bbc
002548A8  40 B6 01                        mov sil, 1
002548AB  E9 BF E8 FF FF                  jmp 0x14025316f
002548B0  BA 01 00 00 00                  mov edx, 1
002548B5  4C 8D 55 10                     lea r10, [rbp + 0x10]
002548B9  44 8B CA                        mov r9d, edx
002548BC  E9 BF FE FF FF                  jmp 0x140254780
002548C1  B3 05                           mov bl, 5
002548C3  E9 44 E8 FF FF                  jmp 0x14025310c
002548C8  0F B7 88 06 02 00 00            movzx ecx, word ptr [rax + 0x206]
002548CF  0F BE 80 33 02 00 00            movsx eax, byte ptr [rax + 0x233]
002548D6  83 E1 0F                        and ecx, 0xf
002548D9  03 C8                           add ecx, eax
002548DB  83 F9 10                        cmp ecx, 0x10
002548DE  0F 4D CA                        cmovge ecx, edx
002548E1  03 D9                           add ebx, ecx
002548E3  83 FB 10                        cmp ebx, 0x10
002548E6  0F 4D DA                        cmovge ebx, edx
002548E9  2B D9                           sub ebx, ecx
002548EB  E9 AD FA FF FF                  jmp 0x14025439d
002548F0  45 84 E4                        test r12b, r12b
002548F3  0F 85 C3 EA FF FF               jne 0x1402533bc
002548F9  E9 BE F8 FF FF                  jmp 0x1402541bc
002548FE  48 8D 4D B0                     lea rcx, [rbp - 0x50]
00254902  E8 A9 35 00 00                  call 0x140257eb0
00254907  E9 7C FB FF FF                  jmp 0x140254488
0025490C  49 8B D1                        mov rdx, r9
0025490F  E9 49 F7 FF FF                  jmp 0x14025405d
00254914  48 8D 4D C8                     lea rcx, [rbp - 0x38]
00254918  E8 33 53 14 00                  call 0x140399c50
0025491D  48 8B 5C 24 68                  mov rbx, qword ptr [rsp + 0x68]
00254922  4C 8D 1D D7 B6 DA FF            lea r11, [rip - 0x254929]
00254929  E9 72 F0 FF FF                  jmp 0x1402539a0
0025492E  49 8B 86 C8 03 00 00            mov rax, qword ptr [r14 + 0x3c8]
00254935  F0 81 08 00 00 10 00            lock or dword ptr [rax], 0x100000
0025493C  48 8D 55 E8                     lea rdx, [rbp - 0x18]
00254940  48 8B CB                        mov rcx, rbx
00254943  E8 9C 02 0B 00                  call 0x140304be4
00254948  4C 63 8B 00 04 00 00            movsxd r9, dword ptr [rbx + 0x400]
0025494F  4C 63 F0                        movsxd r14, eax
00254952  45 3B F1                        cmp r14d, r9d
00254955  0F 85 AD 08 00 00               jne 0x140255208
0025495B  44 0F BE A3 C3 00 00 00         movsx r12d, byte ptr [rbx + 0xc3]
00254963  45 33 C0                        xor r8d, r8d
00254966  33 D2                           xor edx, edx
00254968  48 8B CB                        mov rcx, rbx
0025496B  E8 84 FC 16 00                  call 0x1403c45f4
00254970  8B D8                           mov ebx, eax
00254972  41 3B C4                        cmp eax, r12d
00254975  0F 85 C1 08 00 00               jne 0x14025523c
0025497B  4C 8B 5C 24 48                  mov r11, qword ptr [rsp + 0x48]
00254980  41 0F B6 93 62 04 00 00         movzx edx, byte ptr [r11 + 0x462]
00254988  85 D2                           test edx, edx
0025498A  0F 85 A5 01 00 00               jne 0x140254b35
00254990  41 0F B6 83 04 02 00 00         movzx eax, byte ptr [r11 + 0x204]
00254998  3B D0                           cmp edx, eax
0025499A  0F 85 D7 08 00 00               jne 0x140255277
002549A0  41 F7 43 78 00 00 40 00         test dword ptr [r11 + 0x78], 0x400000
002549A8  74 0E                           je 0x1402549b8
002549AA  49 8B 83 C8 03 00 00            mov rax, qword ptr [r11 + 0x3c8]
002549B1  F0 81 20 FF FF EF FF            lock and dword ptr [rax], 0xffefffff
002549B8  44 3B E3                        cmp r12d, ebx
002549BB  0F 85 CF 03 00 00               jne 0x140254d90
002549C1  49 8B DB                        mov rbx, r11
002549C4  41 B4 01                        mov r12b, 1
002549C7  E9 D8 E6 FF FF                  jmp 0x1402530a4
002549CC  0F B6 83 C3 00 00 00            movzx eax, byte ptr [rbx + 0xc3]
002549D3  84 C0                           test al, al
002549D5  0F 8E DD 00 00 00               jle 0x140254ab8
002549DB  0F BE 8B 37 02 00 00            movsx ecx, byte ptr [rbx + 0x237]
002549E2  3A C1                           cmp al, cl
002549E4  0F 8D CE 00 00 00               jge 0x140254ab8
002549EA  3C 0D                           cmp al, 0xd
002549EC  0F 8D C6 00 00 00               jge 0x140254ab8
002549F2  8B 43 78                        mov eax, dword ptr [rbx + 0x78]
002549F5  A8 08                           test al, 8
002549F7  0F 85 BB 00 00 00               jne 0x140254ab8
002549FD  80 F9 0D                        cmp cl, 0xd
00254A00  0F 8D A3 01 00 00               jge 0x140254ba9
00254A06  44 8B C1                        mov r8d, ecx
00254A09  8B 05 3D 22 D7 00               mov eax, dword ptr [rip + 0xd7223d]
00254A0F  4D 8B CD                        mov r9, r13
00254A12  48 8B D3                        mov rdx, rbx
00254A15  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00254A19  33 C9                           xor ecx, ecx
00254A1B  E8 20 40 14 00                  call 0x140398a40
00254A20  E9 AE E7 FF FF                  jmp 0x1402531d3
00254A25  4C 8D 45 38                     lea r8, [rbp + 0x38]
00254A29  BA 01 00 00 00                  mov edx, 1
00254A2E  E9 AD FB FF FF                  jmp 0x1402545e0
00254A33  F0 48 21 3B                     lock and qword ptr [rbx], rdi
00254A37  E9 3A FB FF FF                  jmp 0x140254576
00254A3C  F6 46 23 20                     test byte ptr [rsi + 0x23], 0x20
00254A40  0F 84 D7 FA FF FF               je 0x14025451d
00254A46  49 8B CF                        mov rcx, r15
00254A49  E8 32 31 28 00                  call 0x1404d7b80
00254A4E  84 C0                           test al, al
00254A50  0F 85 C7 FA FF FF               jne 0x14025451d
00254A56  48 8B D3                        mov rdx, rbx
00254A59  48 8B CE                        mov rcx, rsi
00254A5C  E8 A3 6B 2A 00                  call 0x1404fb604
00254A61  E9 B7 FA FF FF                  jmp 0x14025451d
00254A66  48 8B 8B D0 02 00 00            mov rcx, qword ptr [rbx + 0x2d0]
00254A6D  48 8B 83 C8 02 00 00            mov rax, qword ptr [rbx + 0x2c8]
00254A74  F0 48 09 81 88 01 00 00         lock or qword ptr [rcx + 0x188], rax
00254A7C  E9 75 FA FF FF                  jmp 0x1402544f6
00254A81  49 8B 95 C0 00 00 00            mov rdx, qword ptr [r13 + 0xc0]
00254A88  E8 93 44 FC FF                  call 0x140218f20
00254A8D  84 C0                           test al, al
00254A8F  74 0B                           je 0x140254a9c
00254A91  41 F6 45 23 20                  test byte ptr [r13 + 0x23], 0x20
00254A96  0F 85 BE 05 00 00               jne 0x14025505a
00254A9C  48 8B 42 50                     mov rax, qword ptr [rdx + 0x50]
00254AA0  48 8B 91 C8 02 00 00            mov rdx, qword ptr [rcx + 0x2c8]
00254AA7  48 23 D0                        and rdx, rax
00254AAA  48 85 D2                        test rdx, rdx
00254AAD  0F 84 F8 FC FF FF               je 0x1402547ab
00254AB3  E9 F0 E9 FF FF                  jmp 0x1402534a8
00254AB8  40 84 F6                        test sil, sil
00254ABB  0F 85 12 E7 FF FF               jne 0x1402531d3
00254AC1  48 8B 53 20                     mov rdx, qword ptr [rbx + 0x20]
00254AC5  8B 05 81 21 D7 00               mov eax, dword ptr [rip + 0xd72181]
00254ACB  4C 3B EA                        cmp r13, rdx
00254ACE  77 0C                           ja 0x140254adc
00254AD0  49 2B D5                        sub rdx, r13
00254AD3  48 3B D0                        cmp rdx, rax
00254AD6  0F 83 F7 E6 FF FF               jae 0x1402531d3
00254ADC  49 03 C5                        add rax, r13
00254ADF  48 89 43 20                     mov qword ptr [rbx + 0x20], rax
00254AE3  E9 EB E6 FF FF                  jmp 0x1402531d3
00254AE8  41 B2 01                        mov r10b, 1
00254AEB  66 F0 FF 83 64 03 00 00         lock inc word ptr [rbx + 0x364]
00254AF3  E9 9E FA FF FF                  jmp 0x140254596
00254AF8  B9 21 00 00 00                  mov ecx, 0x21
00254AFD  CD 29                           int 0x29
00254AFF  4C 8B 4D 80                     mov r9, qword ptr [rbp - 0x80]
00254B03  48 8D 45 40                     lea rax, [rbp + 0x40]
00254B07  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00254B0C  4C 8B C3                        mov r8, rbx
00254B0F  48 8D 45 88                     lea rax, [rbp - 0x78]
00254B13  44 89 74 24 28                  mov dword ptr [rsp + 0x28], r14d
00254B18  49 8B D5                        mov rdx, r13
00254B1B  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00254B20  48 8B CE                        mov rcx, rsi
00254B23  E8 1C C6 16 00                  call 0x1403c1144
00254B28  85 C0                           test eax, eax
00254B2A  0F 89 08 F6 FF FF               jns 0x140254138
00254B30  E9 89 F5 FF FF                  jmp 0x1402540be
00254B35  49 8B 8B C8 03 00 00            mov rcx, qword ptr [r11 + 0x3c8]
00254B3C  48 85 C9                        test rcx, rcx
00254B3F  0F 84 4B FE FF FF               je 0x140254990
00254B45  8B 41 1C                        mov eax, dword ptr [rcx + 0x1c]
00254B48  44 8B 49 20                     mov r9d, dword ptr [rcx + 0x20]
00254B4C  44 8B 51 14                     mov r10d, dword ptr [rcx + 0x14]
00254B50  44 8B 01                        mov r8d, dword ptr [rcx]
00254B53  41 81 E0 00 00 20 00            and r8d, 0x200000
00254B5A  85 C0                           test eax, eax
00254B5C  0F 84 F3 06 00 00               je 0x140255255
00254B62  8B D7                           mov edx, edi
00254B64  E9 27 FE FF FF                  jmp 0x140254990
00254B69  4C 8D 45 40                     lea r8, [rbp + 0x40]
00254B6D  41 8B D1                        mov edx, r9d
00254B70  48 8B CE                        mov rcx, rsi
00254B73  E8 98 FD 1D 00                  call 0x140434910
00254B78  E9 1B ED FF FF                  jmp 0x140253898
00254B7D  4C 8D 45 40                     lea r8, [rbp + 0x40]
00254B81  41 8B D1                        mov edx, r9d
00254B84  48 8B CE                        mov rcx, rsi
00254B87  E8 84 FD 1D 00                  call 0x140434910
00254B8C  E9 EF F5 FF FF                  jmp 0x140254180
00254B91  48 89 30                        mov qword ptr [rax], rsi
00254B94  48 89 48 08                     mov qword ptr [rax + 8], rcx
00254B98  48 89 01                        mov qword ptr [rcx], rax
00254B9B  48 89 46 08                     mov qword ptr [rsi + 8], rax
00254B9F  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
00254BA4  E9 24 F9 FF FF                  jmp 0x1402544cd
00254BA9  41 B8 0D 00 00 00               mov r8d, 0xd
00254BAF  E9 55 FE FF FF                  jmp 0x140254a09
00254BB4  4C 8B C7                        mov r8, rdi
00254BB7  E9 62 F4 FF FF                  jmp 0x14025401e
00254BBC  0F B7 83 06 02 00 00            movzx eax, word ptr [rbx + 0x206]
00254BC3  BA F0 0F 00 00                  mov edx, 0xff0
00254BC8  66 23 C2                        and ax, dx
00254BCB  B9 00 01 00 00                  mov ecx, 0x100
00254BD0  66 3B C1                        cmp ax, cx
00254BD3  40 0F 92 C6                     setb sil
00254BD7  4C 3B 6B 20                     cmp r13, qword ptr [rbx + 0x20]
00254BDB  0F 82 8E E5 FF FF               jb 0x14025316f
00254BE1  40 B6 01                        mov sil, 1
00254BE4  48 8B CB                        mov rcx, rbx
00254BE7  44 0F B6 C6                     movzx r8d, sil
00254BEB  E8 9C E1 16 00                  call 0x1403c2d8c
00254BF0  E9 7A E5 FF FF                  jmp 0x14025316f
00254BF5  49 8B 87 C8 03 00 00            mov rax, qword ptr [r15 + 0x3c8]
00254BFC  F0 81 08 00 00 04 00            lock or dword ptr [rax], 0x40000
00254C03  E9 2E F6 FF FF                  jmp 0x140254236
00254C08  48 8B D7                        mov rdx, rdi
00254C0B  E9 68 F6 FF FF                  jmp 0x140254278
00254C10  45 85 D2                        test r10d, r10d
00254C13  0F 85 50 02 00 00               jne 0x140254e69
00254C19  49 8B 51 18                     mov rdx, qword ptr [r9 + 0x18]
00254C1D  48 8D 35 DC B2 D7 00            lea rsi, [rip + 0xd7b2dc]
00254C24  4D 8B 19                        mov r11, qword ptr [r9]
00254C27  48 8D 42 FF                     lea rax, [rdx - 1]
00254C2B  48 83 F8 FC                     cmp rax, -4
00254C2F  0F 86 2E 01 00 00               jbe 0x140254d63
00254C35  41 0F B6 41 20                  movzx eax, byte ptr [r9 + 0x20]
00254C3A  24 FE                           and al, 0xfe
00254C3C  49 89 59 10                     mov qword ptr [r9 + 0x10], rbx
00254C40  41 88 41 20                     mov byte ptr [r9 + 0x20], al
00254C44  8B 4B 78                        mov ecx, dword ptr [rbx + 0x78]
00254C47  D1 E9                           shr ecx, 1
00254C49  02 C9                           add cl, cl
00254C4B  49 89 59 18                     mov qword ptr [r9 + 0x18], rbx
00254C4F  32 C8                           xor cl, al
00254C51  80 E1 02                        and cl, 2
00254C54  32 C8                           xor cl, al
00254C56  41 0F B6 41 21                  movzx eax, byte ptr [r9 + 0x21]
00254C5B  80 C9 04                        or cl, 4
00254C5E  80 E1 C7                        and cl, 0xc7
00254C61  41 88 49 20                     mov byte ptr [r9 + 0x20], cl
00254C65  0F B6 4C 24 42                  movzx ecx, byte ptr [rsp + 0x42]
00254C6A  32 C8                           xor cl, al
00254C6C  80 E1 01                        and cl, 1
00254C6F  32 C8                           xor cl, al
00254C71  41 88 49 21                     mov byte ptr [r9 + 0x21], cl
00254C75  48 39 B3 20 02 00 00            cmp qword ptr [rbx + 0x220], rsi
00254C7C  0F 85 94 06 00 00               jne 0x140255316
00254C82  45 32 C9                        xor r9b, r9b
00254C85  45 89 56 04                     mov dword ptr [r14 + 4], r10d
00254C89  F7 05 81 1E D7 00 00 04 00 00   test dword ptr [rip + 0xd71e81], 0x400
00254C93  8B F7                           mov esi, edi
00254C95  B8 02 00 00 00                  mov eax, 2
00254C9A  8B DF                           mov ebx, edi
00254C9C  0F 45 F0                        cmovne esi, eax
00254C9F  41 38 3E                        cmp byte ptr [r14], dil
00254CA2  76 42                           jbe 0x140254ce6
00254CA4  4C 8B 65 D0                     mov r12, qword ptr [rbp - 0x30]
00254CA8  8B C3                           mov eax, ebx
00254CAA  4D 8B CC                        mov r9, r12
00254CAD  44 8B C6                        mov r8d, esi
00254CB0  49 8B D7                        mov rdx, r15
00254CB3  48 8D 0C 85 02 00 00 00         lea rcx, [rax*4 + 2]
00254CBB  48 03 C8                        add rcx, rax
00254CBE  49 8D 0C CE                     lea rcx, [r14 + rcx*8]
00254CC2  E8 09 83 0B 00                  call 0x14030cfd0
00254CC7  40 0A F8                        or dil, al
00254CCA  FF C3                           inc ebx
00254CCC  41 0F B6 06                     movzx eax, byte ptr [r14]
00254CD0  3B D8                           cmp ebx, eax
00254CD2  72 D4                           jb 0x140254ca8
00254CD4  4C 8B 64 24 68                  mov r12, qword ptr [rsp + 0x68]
00254CD9  40 88 7C 24 40                  mov byte ptr [rsp + 0x40], dil
00254CDE  33 FF                           xor edi, edi
00254CE0  44 0F B6 4C 24 40               movzx r9d, byte ptr [rsp + 0x40]
00254CE6  41 83 7E 08 01                  cmp dword ptr [r14 + 8], 1
00254CEB  75 1C                           jne 0x140254d09
00254CED  49 8B 46 10                     mov rax, qword ptr [r14 + 0x10]
00254CF1  48 8B 88 58 8E 00 00            mov rcx, qword ptr [rax + 0x8e58]
00254CF8  0F B6 41 01                     movzx eax, byte ptr [rcx + 1]
00254CFC  FE C0                           inc al
00254CFE  88 41 01                        mov byte ptr [rcx + 1], al
00254D01  3A 01                           cmp al, byte ptr [rcx]
00254D03  72 04                           jb 0x140254d09
00254D05  C6 41 01 00                     mov byte ptr [rcx + 1], 0
00254D09  49 83 E5 FE                     and r13, 0xfffffffffffffffe
00254D0D  4C 8B C7                        mov r8, rdi
00254D10  4C 89 6D 30                     mov qword ptr [rbp + 0x30], r13
00254D14  8B D7                           mov edx, edi
00254D16  41 83 E4 01                     and r12d, 1
00254D1A  74 3C                           je 0x140254d58
00254D1C  41 83 FC 01                     cmp r12d, 1
00254D20  75 15                           jne 0x140254d37
00254D22  49 8B 85 58 8E 00 00            mov rax, qword ptr [r13 + 0x8e58]
00254D29  4D 8B 85 58 8E 00 00            mov r8, qword ptr [r13 + 0x8e58]
00254D30  49 83 C0 08                     add r8, 8
00254D34  0F B6 10                        movzx edx, byte ptr [rax]
00254D37  85 D2                           test edx, edx
00254D39  0F 84 62 F1 FF FF               je 0x140253ea1
00254D3F  90                              nop
00254D40  8D 42 FF                        lea eax, [rdx - 1]
00254D43  49 8B 0C C0                     mov rcx, qword ptr [r8 + rax*8]
00254D47  8B D0                           mov edx, eax
00254D49  F0 48 83 61 30 00               lock and qword ptr [rcx + 0x30], 0
00254D4F  85 C0                           test eax, eax
00254D51  75 ED                           jne 0x140254d40
00254D53  E9 49 F1 FF FF                  jmp 0x140253ea1
00254D58  4C 8D 45 30                     lea r8, [rbp + 0x30]
00254D5C  BA 01 00 00 00                  mov edx, 1
00254D61  EB DD                           jmp 0x140254d40
00254D63  48 39 B2 20 02 00 00            cmp qword ptr [rdx + 0x220], rsi
00254D6A  0F 84 C5 FE FF FF               je 0x140254c35
00254D70  41 F6 41 21 01                  test byte ptr [r9 + 0x21], 1
00254D75  74 04                           je 0x140254d7b
00254D77  83 4A 74 02                     or dword ptr [rdx + 0x74], 2
00254D7B  48 8B 4D D0                     mov rcx, qword ptr [rbp - 0x30]
00254D7F  C6 82 35 02 00 00 01            mov byte ptr [rdx + 0x235], 1
00254D86  E8 85 C5 FA FF                  call 0x140201310
00254D8B  E9 A5 FE FF FF                  jmp 0x140254c35
00254D90  8B 05 7E 1D D7 00               mov eax, dword ptr [rip + 0xd71d7e]
00254D96  A8 20                           test al, 0x20
00254D98  0F 84 23 FC FF FF               je 0x1402549c1
00254D9E  48 8D 45 E8                     lea rax, [rbp - 0x18]
00254DA2  44 8B CB                        mov r9d, ebx
00254DA5  45 8B C6                        mov r8d, r14d
00254DA8  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00254DAD  41 8B D4                        mov edx, r12d
00254DB0  49 8B CB                        mov rcx, r11
00254DB3  49 8B DB                        mov rbx, r11
00254DB6  E8 9D D5 27 00                  call 0x1404d2358
00254DBB  E9 04 FC FF FF                  jmp 0x1402549c4
00254DC0  41 B0 01                        mov r8b, 1
00254DC3  48 8B CB                        mov rcx, rbx
00254DC6  E8 C1 DF 16 00                  call 0x1403c2d8c
00254DCB  45 84 E4                        test r12b, r12b
00254DCE  75 12                           jne 0x140254de2
00254DD0  44 8B C8                        mov r9d, eax
00254DD3  40 88 74 24 20                  mov byte ptr [rsp + 0x20], sil
00254DD8  4C 8B C3                        mov r8, rbx
00254DDB  33 C9                           xor ecx, ecx
00254DDD  E8 2E 2A 00 00                  call 0x140257810
00254DE2  48 8B CB                        mov rcx, rbx
00254DE5  40 B6 01                        mov sil, 1
00254DE8  E8 2F 67 22 00                  call 0x14047b51c
00254DED  E9 E1 E3 FF FF                  jmp 0x1402531d3
00254DF2  3B C2                           cmp eax, edx
00254DF4  0F 84 BA E4 FF FF               je 0x1402532b4
00254DFA  B0 01                           mov al, 1
00254DFC  E9 B5 E4 FF FF                  jmp 0x1402532b6
00254E01  48 83 F8 FC                     cmp rax, -4
00254E05  0F 86 5B 02 00 00               jbe 0x140255066
00254E0B  41 0F B6 49 30                  movzx ecx, byte ptr [r9 + 0x30]
00254E10  80 E1 FE                        and cl, 0xfe
00254E13  4D 89 51 20                     mov qword ptr [r9 + 0x20], r10
00254E17  41 88 49 30                     mov byte ptr [r9 + 0x30], cl
00254E1B  80 E1 FD                        and cl, 0xfd
00254E1E  41 8B 42 78                     mov eax, dword ptr [r10 + 0x78]
00254E22  D1 E8                           shr eax, 1
00254E24  24 01                           and al, 1
00254E26  4D 89 51 28                     mov qword ptr [r9 + 0x28], r10
00254E2A  02 C0                           add al, al
00254E2C  32 C1                           xor al, cl
00254E2E  24 C7                           and al, 0xc7
00254E30  0C 04                           or al, 4
00254E32  41 88 41 30                     mov byte ptr [r9 + 0x30], al
00254E36  41 0F B6 41 31                  movzx eax, byte ptr [r9 + 0x31]
00254E3B  0F B6 C8                        movzx ecx, al
00254E3E  41 32 CF                        xor cl, r15b
00254E41  80 E1 01                        and cl, 1
00254E44  32 C8                           xor cl, al
00254E46  41 88 49 31                     mov byte ptr [r9 + 0x31], cl
00254E4A  49 8B CA                        mov rcx, r10
00254E4D  E8 DE E3 0F 00                  call 0x140353230
00254E52  84 C0                           test al, al
00254E54  0F 85 2F E8 FF FF               jne 0x140253689
00254E5A  8B 43 24                        mov eax, dword ptr [rbx + 0x24]
00254E5D  41 89 82 18 02 00 00            mov dword ptr [r10 + 0x218], eax
00254E64  E9 20 E8 FF FF                  jmp 0x140253689
00254E69  44 8B DF                        mov r11d, edi
00254E6C  41 38 3E                        cmp byte ptr [r14], dil
00254E6F  0F 86 0D FE FF FF               jbe 0x140254c82
00254E75  4C 8B 65 D0                     mov r12, qword ptr [rbp - 0x30]
00254E79  44 0F B6 7C 24 42               movzx r15d, byte ptr [rsp + 0x42]
00254E7F  4C 8B 54 24 48                  mov r10, qword ptr [rsp + 0x48]
00254E84  41 8B C3                        mov eax, r11d
00254E87  48 8D 0C 80                     lea rcx, [rax + rax*4]
00254E8B  49 8B 5C CE 10                  mov rbx, qword ptr [r14 + rcx*8 + 0x10]
00254E90  4D 8D 0C CE                     lea r9, [r14 + rcx*8]
00254E94  49 8B 4C CE 28                  mov rcx, qword ptr [r14 + rcx*8 + 0x28]
00254E99  48 8D 41 FF                     lea rax, [rcx - 1]
00254E9D  48 3B DE                        cmp rbx, rsi
00254EA0  75 74                           jne 0x140254f16
00254EA2  48 83 F8 FC                     cmp rax, -4
00254EA6  0F 86 E9 01 00 00               jbe 0x140255095
00254EAC  41 0F B6 49 30                  movzx ecx, byte ptr [r9 + 0x30]
00254EB1  80 E1 FE                        and cl, 0xfe
00254EB4  4D 89 51 20                     mov qword ptr [r9 + 0x20], r10
00254EB8  41 88 49 30                     mov byte ptr [r9 + 0x30], cl
00254EBC  80 E1 FD                        and cl, 0xfd
00254EBF  41 8B 42 78                     mov eax, dword ptr [r10 + 0x78]
00254EC3  D1 E8                           shr eax, 1
00254EC5  24 01                           and al, 1
00254EC7  4D 89 51 28                     mov qword ptr [r9 + 0x28], r10
00254ECB  02 C0                           add al, al
00254ECD  32 C1                           xor al, cl
00254ECF  41 0F B6 CF                     movzx ecx, r15b
00254ED3  24 C7                           and al, 0xc7
00254ED5  0C 04                           or al, 4
00254ED7  41 88 41 30                     mov byte ptr [r9 + 0x30], al
00254EDB  41 0F B6 41 31                  movzx eax, byte ptr [r9 + 0x31]
00254EE0  32 C8                           xor cl, al
00254EE2  80 E1 01                        and cl, 1
00254EE5  32 C8                           xor cl, al
00254EE7  41 88 49 31                     mov byte ptr [r9 + 0x31], cl
00254EEB  49 8B CA                        mov rcx, r10
00254EEE  E8 3D E3 0F 00                  call 0x140353230
00254EF3  84 C0                           test al, al
00254EF5  75 0A                           jne 0x140254f01
00254EF7  8B 43 24                        mov eax, dword ptr [rbx + 0x24]
00254EFA  41 89 82 18 02 00 00            mov dword ptr [r10 + 0x218], eax
00254F01  41 0F B6 06                     movzx eax, byte ptr [r14]
00254F05  41 FF C3                        inc r11d
00254F08  44 3B D8                        cmp r11d, eax
00254F0B  0F 82 73 FF FF FF               jb 0x140254e84
00254F11  E9 83 E7 FF FF                  jmp 0x140253699
00254F16  48 8B B3 80 8E 00 00            mov rsi, qword ptr [rbx + 0x8e80]
00254F1D  48 83 F8 FC                     cmp rax, -4
00254F21  0F 86 9D 01 00 00               jbe 0x1402550c4
00254F27  41 0F B6 41 30                  movzx eax, byte ptr [r9 + 0x30]
00254F2C  24 FE                           and al, 0xfe
00254F2E  4D 89 51 20                     mov qword ptr [r9 + 0x20], r10
00254F32  41 88 41 30                     mov byte ptr [r9 + 0x30], al
00254F36  24 FD                           and al, 0xfd
00254F38  41 8B 4A 78                     mov ecx, dword ptr [r10 + 0x78]
00254F3C  D1 E9                           shr ecx, 1
00254F3E  80 E1 01                        and cl, 1
00254F41  02 C9                           add cl, cl
00254F43  32 C8                           xor cl, al
00254F45  80 E1 E7                        and cl, 0xe7
00254F48  80 C9 04                        or cl, 4
00254F4B  0F B6 C1                        movzx eax, cl
00254F4E  80 C9 20                        or cl, 0x20
00254F51  24 DF                           and al, 0xdf
00254F53  0F B6 C9                        movzx ecx, cl
00254F56  0F B6 C0                        movzx eax, al
00254F59  4C 3B D6                        cmp r10, rsi
00254F5C  0F 44 C8                        cmove ecx, eax
00254F5F  41 88 49 30                     mov byte ptr [r9 + 0x30], cl
00254F63  48 8B CE                        mov rcx, rsi
00254F66  41 80 61 31 FE                  and byte ptr [r9 + 0x31], 0xfe
00254F6B  49 89 71 28                     mov qword ptr [r9 + 0x28], rsi
00254F6F  E8 BC E2 0F 00                  call 0x140353230
00254F74  84 C0                           test al, al
00254F76  75 09                           jne 0x140254f81
00254F78  8B 43 24                        mov eax, dword ptr [rbx + 0x24]
00254F7B  89 86 18 02 00 00               mov dword ptr [rsi + 0x218], eax
00254F81  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
00254F86  E9 76 FF FF FF                  jmp 0x140254f01
00254F8B  45 32 E4                        xor r12b, r12b
00254F8E  E9 D9 E2 FF FF                  jmp 0x14025326c
00254F93  49 8B D7                        mov rdx, r15
00254F96  48 8B CB                        mov rcx, rbx
00254F99  E8 1E 32 2A 00                  call 0x1404f81bc
00254F9E  84 C0                           test al, al
00254FA0  0F 84 8F E3 FF FF               je 0x140253335
00254FA6  45 84 E4                        test r12b, r12b
00254FA9  0F 85 86 E3 FF FF               jne 0x140253335
00254FAF  41 B6 01                        mov r14b, 1
00254FB2  E9 7E E3 FF FF                  jmp 0x140253335
00254FB7  4C 8B C7                        mov r8, rdi
00254FBA  8B D7                           mov edx, edi
00254FBC  41 3B D1                        cmp edx, r9d
00254FBF  73 20                           jae 0x140254fe1
00254FC1  8B C2                           mov eax, edx
00254FC3  48 8D 0C 80                     lea rcx, [rax + rax*4]
00254FC7  49 8B 44 CE 10                  mov rax, qword ptr [r14 + rcx*8 + 0x10]
00254FCC  4D 8D 14 CE                     lea r10, [r14 + rcx*8]
00254FD0  48 8B 88 80 8E 00 00            mov rcx, qword ptr [rax + 0x8e80]
00254FD7  49 39 4A 20                     cmp qword ptr [r10 + 0x20], rcx
00254FDB  74 3D                           je 0x14025501a
00254FDD  4D 8D 42 10                     lea r8, [r10 + 0x10]
00254FE1  45 85 C9                        test r9d, r9d
00254FE4  0F 84 B7 E5 FF FF               je 0x1402535a1
00254FEA  49 8D 4E 30                     lea rcx, [r14 + 0x30]
00254FEE  41 8B D1                        mov edx, r9d
00254FF1  48 8D 41 E0                     lea rax, [rcx - 0x20]
00254FF5  49 3B C0                        cmp rax, r8
00254FF8  74 11                           je 0x14025500b
00254FFA  49 8B 40 10                     mov rax, qword ptr [r8 + 0x10]
00254FFE  48 89 41 F0                     mov qword ptr [rcx - 0x10], rax
00255002  41 0F B6 40 20                  movzx eax, byte ptr [r8 + 0x20]
00255007  0C 20                           or al, 0x20
00255009  88 01                           mov byte ptr [rcx], al
0025500B  48 83 C1 28                     add rcx, 0x28
0025500F  48 83 EA 01                     sub rdx, 1
00255013  75 DC                           jne 0x140254ff1
00255015  E9 87 E5 FF FF                  jmp 0x1402535a1
0025501A  FF C2                           inc edx
0025501C  EB 9E                           jmp 0x140254fbc
0025501E  E8 0D E2 0F 00                  call 0x140353230
00255023  84 C0                           test al, al
00255025  0F 85 11 E6 FF FF               jne 0x14025363c
0025502B  41 F6 41 31 01                  test byte ptr [r9 + 0x31], 1
00255030  74 04                           je 0x140255036
00255032  83 49 74 02                     or dword ptr [rcx + 0x74], 2
00255036  C6 81 35 02 00 00 01            mov byte ptr [rcx + 0x235], 1
0025503D  48 8B D1                        mov rdx, rcx
00255040  49 8B CC                        mov rcx, r12
00255043  E8 C8 C2 FA FF                  call 0x140201310
00255048  E9 EF E5 FF FF                  jmp 0x14025363c
0025504D  66 F0 FF 83 64 03 00 00         lock inc word ptr [rbx + 0x364]
00255055  E9 71 E2 FF FF                  jmp 0x1402532cb
0025505A  48 8B 42 68                     mov rax, qword ptr [rdx + 0x68]
0025505E  48 F7 D0                        not rax
00255061  E9 3A FA FF FF                  jmp 0x140254aa0
00255066  E8 C5 E1 0F 00                  call 0x140353230
0025506B  84 C0                           test al, al
0025506D  0F 85 98 FD FF FF               jne 0x140254e0b
00255073  41 F6 41 31 01                  test byte ptr [r9 + 0x31], 1
00255078  74 04                           je 0x14025507e
0025507A  83 49 74 02                     or dword ptr [rcx + 0x74], 2
0025507E  C6 81 35 02 00 00 01            mov byte ptr [rcx + 0x235], 1
00255085  48 8B D1                        mov rdx, rcx
00255088  49 8B CC                        mov rcx, r12
0025508B  E8 80 C2 FA FF                  call 0x140201310
00255090  E9 76 FD FF FF                  jmp 0x140254e0b
00255095  E8 96 E1 0F 00                  call 0x140353230
0025509A  84 C0                           test al, al
0025509C  0F 85 0A FE FF FF               jne 0x140254eac
002550A2  41 F6 41 31 01                  test byte ptr [r9 + 0x31], 1
002550A7  74 04                           je 0x1402550ad
002550A9  83 49 74 02                     or dword ptr [rcx + 0x74], 2
002550AD  C6 81 35 02 00 00 01            mov byte ptr [rcx + 0x235], 1
002550B4  48 8B D1                        mov rdx, rcx
002550B7  49 8B CC                        mov rcx, r12
002550BA  E8 51 C2 FA FF                  call 0x140201310
002550BF  E9 E8 FD FF FF                  jmp 0x140254eac
002550C4  E8 67 E1 0F 00                  call 0x140353230
002550C9  84 C0                           test al, al
002550CB  0F 85 56 FE FF FF               jne 0x140254f27
002550D1  41 F6 41 31 01                  test byte ptr [r9 + 0x31], 1
002550D6  74 04                           je 0x1402550dc
002550D8  83 49 74 02                     or dword ptr [rcx + 0x74], 2
002550DC  C6 81 35 02 00 00 01            mov byte ptr [rcx + 0x235], 1
002550E3  48 8B D1                        mov rdx, rcx
002550E6  49 8B CC                        mov rcx, r12
002550E9  E8 22 C2 FA FF                  call 0x140201310
002550EE  E9 34 FE FF FF                  jmp 0x140254f27
002550F3  44 8B 43 74                     mov r8d, dword ptr [rbx + 0x74]
002550F7  45 33 C9                        xor r9d, r9d
002550FA  48 8B 83 40 02 00 00            mov rax, qword ptr [rbx + 0x240]
00255101  48 8B CB                        mov rcx, rbx
00255104  0F B7 93 48 02 00 00            movzx edx, word ptr [rbx + 0x248]
0025510B  41 C1 E8 03                     shr r8d, 3
0025510F  41 80 E0 01                     and r8b, 1
00255113  66 C7 44 24 28 36 05            mov word ptr [rsp + 0x28], 0x536
0025511A  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0025511F  E8 7C D8 16 00                  call 0x1403c29a0
00255124  80 7C 24 43 00                  cmp byte ptr [rsp + 0x43], 0
00255129  0F 85 01 02 00 00               jne 0x140255330
0025512F  66 F0 FF 8B 64 03 00 00         lock dec word ptr [rbx + 0x364]
00255137  E9 3C 02 00 00                  jmp 0x140255378
0025513C  4C 8D 83 28 03 00 00            lea r8, [rbx + 0x328]
00255143  49 83 38 01                     cmp qword ptr [r8], 1
00255147  0F 85 3E E0 FF FF               jne 0x14025318b
0025514D  48 8D 8A 78 91 00 00            lea rcx, [rdx + 0x9178]
00255154  48 85 C9                        test rcx, rcx
00255157  0F 84 2E E0 FF FF               je 0x14025318b
0025515D  48 8B 01                        mov rax, qword ptr [rcx]
00255160  49 89 00                        mov qword ptr [r8], rax
00255163  4C 89 01                        mov qword ptr [rcx], r8
00255166  66 F0 FF 83 64 03 00 00         lock inc word ptr [rbx + 0x364]
0025516E  48 8B CA                        mov rcx, rdx
00255171  E8 5A 23 FB FF                  call 0x1402074d0
00255176  E9 10 E0 FF FF                  jmp 0x14025318b
0025517B  0F B6 83 18 03 00 00            movzx eax, byte ptr [rbx + 0x318]
00255182  84 C0                           test al, al
00255184  0F 84 01 E0 FF FF               je 0x14025318b
0025518A  EB B0                           jmp 0x14025513c
0025518C  41 B4 01                        mov r12b, 1
0025518F  F7 46 78 00 00 40 00            test dword ptr [rsi + 0x78], 0x400000
00255196  74 26                           je 0x1402551be
00255198  49 8B D5                        mov rdx, r13
0025519B  48 8B CE                        mov rcx, rsi
0025519E  E8 B1 10 0B 00                  call 0x140306254
002551A3  84 C0                           test al, al
002551A5  74 17                           je 0x1402551be
002551A7  41 B1 01                        mov r9b, 1
002551AA  49 8B D5                        mov rdx, r13
002551AD  48 8B CE                        mov rcx, rsi
002551B0  E8 8B 0E 0B 00                  call 0x140306040
002551B5  4C 8B 55 80                     mov r10, qword ptr [rbp - 0x80]
002551B9  4C 8B 4C 24 68                  mov r9, qword ptr [rsp + 0x68]
002551BE  44 8B 44 24 50                  mov r8d, dword ptr [rsp + 0x50]
002551C3  45 84 E4                        test r12b, r12b
002551C6  0F 84 25 E3 FF FF               je 0x1402534f1
002551CC  48 89 7E 40                     mov qword ptr [rsi + 0x40], rdi
002551D0  E9 1C E3 FF FF                  jmp 0x1402534f1
002551D5  49 8B 81 80 00 00 00            mov rax, qword ptr [r9 + 0x80]
002551DC  44 03 10                        add r10d, dword ptr [rax]
002551DF  4D 8B 89 A0 01 00 00            mov r9, qword ptr [r9 + 0x1a0]
002551E6  4D 85 C9                        test r9, r9
002551E9  0F 84 8D F4 FF FF               je 0x14025467c
002551EF  E9 72 F4 FF FF                  jmp 0x140254666
002551F4  49 3B F7                        cmp rsi, r15
002551F7  74 96                           je 0x14025518f
002551F9  F0 48 0F BA 6E 40 00            lock bts qword ptr [rsi + 0x40], 0
00255200  0F 82 EB E2 FF FF               jb 0x1402534f1
00255206  EB 84                           jmp 0x14025518c
00255208  4D 0F BE D6                     movsx r10, r14b
0025520C  4D 8B C2                        mov r8, r10
0025520F  49 8D 04 1A                     lea rax, [r10 + rbx]
00255213  0F B6 88 38 03 00 00            movzx ecx, byte ptr [rax + 0x338]
0025521A  80 F9 FF                        cmp cl, 0xff
0025521D  0F 85 33 30 48 00               jne 0x1406d8256
00255223  41 B9 01 00 00 00               mov r9d, 1
00255229  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
0025522E  48 8B D3                        mov rdx, rbx
00255231  B9 57 01 00 00                  mov ecx, 0x157
00255236  E8 25 84 2A 00                  call 0x1404fd660
0025523B  CC                              int3
0025523C  4C 8B 44 24 48                  mov r8, qword ptr [rsp + 0x48]
00255241  44 8B CB                        mov r9d, ebx
00255244  33 C9                           xor ecx, ecx
00255246  40 88 74 24 20                  mov byte ptr [rsp + 0x20], sil
0025524B  E8 C0 25 00 00                  call 0x140257810
00255250  E9 26 F7 FF FF                  jmp 0x14025497b
00255255  45 85 C9                        test r9d, r9d
00255258  0F 85 04 F9 FF FF               jne 0x140254b62
0025525E  41 0F BA E2 0E                  bt r10d, 0xe
00255263  0F 82 F9 F8 FF FF               jb 0x140254b62
00255269  45 85 C0                        test r8d, r8d
0025526C  0F 84 1E F7 FF FF               je 0x140254990
00255272  E9 EB F8 FF FF                  jmp 0x140254b62
00255277  41 88 93 04 02 00 00            mov byte ptr [r11 + 0x204], dl
0025527E  E9 1D F7 FF FF                  jmp 0x1402549a0
00255283  80 E3 06                        and bl, 6
00255286  80 FB 06                        cmp bl, 6
00255289  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
0025528E  0F 94 C1                        sete cl
00255291  F6 C2 08                        test dl, 8
00255294  0F 94 C0                        sete al
00255297  84 C8                           test al, cl
00255299  0F 84 D0 DE FF FF               je 0x14025316f
0025529F  40 38 BB C3 00 00 00            cmp byte ptr [rbx + 0xc3], dil
002552A6  0F 8E C3 DE FF FF               jle 0x14025316f
002552AC  40 80 CE 02                     or sil, 2
002552B0  E9 BA DE FF FF                  jmp 0x14025316f
002552B5  48 8B CB                        mov rcx, rbx
002552B8  E8 B3 13 37 00                  call 0x1405c6670
002552BD  E9 00 DF FF FF                  jmp 0x1402531c2
002552C2  49 8B C8                        mov rcx, r8
002552C5  E8 16 DE 1F 00                  call 0x1404530e0
002552CA  44 8B E8                        mov r13d, eax
002552CD  48 8D 35 2C AD DA FF            lea rsi, [rip - 0x2552d4]
002552D4  4A 8B B4 EE 40 8C FC 00         mov rsi, qword ptr [rsi + r13*8 + 0xfc8c40]
002552DC  48 89 74 24 60                  mov qword ptr [rsp + 0x60], rsi
002552E1  E9 1E E4 FF FF                  jmp 0x140253704
002552E6  8B 05 24 1A D7 00               mov eax, dword ptr [rip + 0xd71a24]
002552EC  88 4C 24 54                     mov byte ptr [rsp + 0x54], cl
002552F0  A8 08                           test al, 8
002552F2  0F 85 77 E6 FF FF               jne 0x14025396f
002552F8  E9 6D E6 FF FF                  jmp 0x14025396a
002552FD  8B 53 24                        mov edx, dword ptr [rbx + 0x24]
00255300  48 8D 4D 50                     lea rcx, [rbp + 0x50]
00255304  E8 F3 37 1C 00                  call 0x140418afc
00255309  0F B7 C8                        movzx ecx, ax
0025530C  49 8B 74 CC 20                  mov rsi, qword ptr [r12 + rcx*8 + 0x20]
00255311  E9 EE E7 FF FF                  jmp 0x140253b04
00255316  41 8B 43 24                     mov eax, dword ptr [r11 + 0x24]
0025531A  89 83 18 02 00 00               mov dword ptr [rbx + 0x218], eax
00255320  E9 5D F9 FF FF                  jmp 0x140254c82
00255325  41 B8 FF FF FF FF               mov r8d, 0xffffffff
0025532B  E9 53 F3 FF FF                  jmp 0x140254683
00255330  F7 05 D6 17 D7 00 00 00 00 08   test dword ptr [rip + 0xd717d6], 0x8000000
0025533A  0F 84 EF FD FF FF               je 0x14025512f
00255340  44 8B 4D DC                     mov r9d, dword ptr [rbp - 0x24]
00255344  BA 46 05 00 00                  mov edx, 0x546
00255349  44 8B 45 C0                     mov r8d, dword ptr [rbp - 0x40]
0025534D  48 8B CB                        mov rcx, rbx
00255350  E8 B3 B4 16 00                  call 0x1403c0808
00255355  E9 D5 FD FF FF                  jmp 0x14025512f
0025535A  66 90                           nop
0025535C  22 32                           and dh, byte ptr [rdx]
0025535E  25 00 DD 47 25                  and eax, 0x2547dd00
00255363  00 F1                           add cl, dh
00255365  40 25 00 22 32 25               and eax, 0x25322200
0025536B  00 27                           add byte ptr [rdi], ah
0025536D  32 25 00 F1 40 25               xor ah, byte ptr [rip + 0x2540f100]
00255373  00 F1                           add cl, dh
00255375  40 25 00 4C 8B A4               and eax, 0xa48b4c00
0025537B  24 B8                           and al, 0xb8
0025537D  01 00                           add dword ptr [rax], eax
0025537F  00 48 8B                        add byte ptr [rax - 0x75], cl
00255382  8D A8 00 00 00 48               lea ebp, [rax + 0x48000000]
00255388  33 CC                           xor ecx, esp
0025538A  E8 B1 72 45 00                  call 0x1406ac640
0025538F  48 81 C4 C0 01 00 00            add rsp, 0x1c0
00255396  41 5F                           pop r15
00255398  41 5E                           pop r14
0025539A  41 5D                           pop r13
0025539C  5F                              pop rdi
0025539D  5E                              pop rsi
0025539E  5B                              pop rbx
0025539F  5D                              pop rbp
002553A0  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_002546EC(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, unsigned int a11)
{
    __int64 result;
    unsigned int v_stack_p20;
    unsigned int v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int8 v_stack_p40;
    unsigned __int8 v_stack_p42;
    unsigned __int8 v_stack_p43;
    unsigned __int64 v_stack_p48;
    unsigned int v_stack_p50;
    unsigned __int8 v_stack_p54;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned int v_stack_p78;

    result = (v_r14 + 2116) << (4);
    result = (result) + (v_rsi);
    if (a11 != ((unsigned int)(v_rdi))) goto loc_00254804;
    *(unsigned __int64 *)(a9 + 216) = result;
    *(unsigned __int64 *)(a9 + 216 + 8) = *(unsigned __int64 *)(result + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 8)) = a9 + 216;
    *(unsigned __int64 *)(result + 8) = a9 + 216;
    goto loc_00254827;
loc_00254804:
    *(unsigned __int64 *)(a9 + 216) = *(unsigned __int64 *)(result);
    *(unsigned __int64 *)(a9 + 216 + 8) = result;
    *(unsigned __int64 *)(*(unsigned __int64 *)(result) + 8) = a9 + 216;
    *(unsigned __int64 *)(result) = a9 + 216;
loc_00254827:
    *(unsigned int *)(v_rsi + 33752) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsi + 33752)));
    result = KiUpdateLocalReadyQueueStatisticsOnInsertion(v_rsi, a9, a3, a4);
}
```

## 5. (Beta) C Style

```c
int64_t sub_002546EC(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, uint64_t Arg8, void *Arg9, uint64_t Arg10, uint32_t Arg11)
{
    uint8_t *arg9 = (uint8_t *)Arg9;

    int64_t result;
    uint32_t v_stack_p20;
    uint32_t v_stack_p28;
    uint64_t v_stack_p30;
    uint8_t v_stack_p40;
    uint8_t v_stack_p42;
    uint8_t v_stack_p43;
    uint64_t v_stack_p48;
    uint32_t v_stack_p50;
    uint8_t v_stack_p54;
    uint64_t v_stack_p60;
    uint64_t v_stack_p68;
    uint32_t v_stack_p78;

    result = (local_r14 + 2116) << (4);
    result = (result) + (local_rsi);
    if (Arg11 != ((uint32_t)(local_rdi))) goto loc_00254804;
    *(uint64_t *)(arg9 + 0xD8) = result;
    *(uint64_t *)(arg9 + 0xD8 + 0x8) = *(uint64_t *)(result + 0x8);
    *(void **)(*(uint64_t *)(result + 0x8)) = Arg9 + 216;
    *(void **)(result + 0x8) = Arg9 + 216;
    goto loc_00254827;
loc_00254804:
    *(uint64_t *)(arg9 + 0xD8) = *(uint64_t *)(result);
    *(uint64_t *)(arg9 + 0xD8 + 0x8) = result;
    *(void **)(*(uint64_t *)(result) + 0x8) = Arg9 + 216;
    *(void **)(result) = Arg9 + 216;
loc_00254827:
    *(uint32_t *)(local_rsi + 0x83D8) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsi + 0x83D8)));
    result = KiUpdateLocalReadyQueueStatisticsOnInsertion(local_rsi, Arg9, Arg3, Arg4);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg9` | `+ 0x0` | `64` | `W` |
| `Arg9` | `+ 0x8` | `64` | `W` |
| `Arg9` | `+ 0xD8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002546EC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
