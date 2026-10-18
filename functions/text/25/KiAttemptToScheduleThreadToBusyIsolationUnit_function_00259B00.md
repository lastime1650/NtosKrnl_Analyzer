# KiAttemptToScheduleThreadToBusyIsolationUnit

- RVA: `0x00259B00`–`0x0025B6B9` (길이 `7,097` bytes)
- VA: `0x0000000140259B00`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00064018`
- 디코드: `1,804`개 명령, `7,097/7,097` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **61**; 고유 호출 대상: **32**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **10**

### Outgoing calls
- `0x00259B85` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00259D7C` → [KiEvaluateGroupSchedulingPreemption](KiEvaluateGroupSchedulingPreemption_function_00258270.md) (function, `0x00258270`)
- `0x00259E89` → [KiIsPrcbThread](../35/KiIsPrcbThread_function_00353230.md) (function, `0x00353230`)
- `0x0025A067` → [KeAddProcessorAffinityEx](KeAddProcessorAffinityEx_function_0025B6F0.md) (function, `0x0025B6F0`)
- `0x0025A07D` → [KeAddGroupAffinityEx](KeAddGroupAffinityEx_function_0025B6C0.md) (function, `0x0025B6C0`)
- `0x0025A116` → [EtwTraceXSchedulerPriorityKickSend](../4F/EtwTraceXSchedulerPriorityKickSend_function_004FB2C0.md) (function, `0x004FB2C0`)
- `0x0025A142` → [EtwTraceScheduleThread](../30/EtwTraceScheduleThread_function_0030B74C.md) (function, `0x0030B74C`)
- `0x0025A198` → [KeIsForceParkingEnabled](../21/KeIsForceParkingEnabled_function_00218F20.md) (function, `0x00218F20`)
- `0x0025A1FC` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0025A208` → [KiStartReadyQueueEnumeratorForRescheduleContext](KiStartReadyQueueEnumeratorForRescheduleContext_function_00259820.md) (function, `0x00259820`)
- `0x0025A501` → [KiComputeThreadQos](KiComputeThreadQos_function_00258010.md) (function, `0x00258010`)
- `0x0025A5B6` → [KiEvaluateGroupSchedulingPreemption](KiEvaluateGroupSchedulingPreemption_function_00258270.md) (function, `0x00258270`)
- `0x0025A7C4` → [KiRemoveCurrentlyEnumeratedThreadFromReadyQueue](../20/KiRemoveCurrentlyEnumeratedThreadFromReadyQueue_function_00201790.md) (function, `0x00201790`)
- `0x0025A7DE` → [KiAddThreadToScbQueue](../20/KiAddThreadToScbQueue_function_002010DC.md) (function, `0x002010DC`)
- `0x0025A800` → [EtwTraceReadyQueueInsertion](../22/EtwTraceReadyQueueInsertion_function_00223444.md) (function, `0x00223444`)
- `0x0025A82D` → [KxWaitForLockOwnerShip](KxWaitForLockOwnerShip_function_00257EB0.md) (function, `0x00257EB0`)
- `0x0025A840` → [KiAdvanceReadyQueueEnumeratorToNextList](../20/KiAdvanceReadyQueueEnumeratorToNextList_function_00201C50.md) (function, `0x00201C50`)
- `0x0025A8CE` → [KiCommitRescheduleContextEntry](../30/KiCommitRescheduleContextEntry_function_0030CFD0.md) (function, `0x0030CFD0`)
- `0x0025AA2E` → [KiUpdateSoftParkElectionStatisticsOnRemoval](../20/KiUpdateSoftParkElectionStatisticsOnRemoval_function_00201A50.md) (function, `0x00201A50`)
- `0x0025AAF2` → [KiIsPrcbThread](../35/KiIsPrcbThread_function_00353230.md) (function, `0x00353230`)
- `0x0025AB81` → [KiIsThreadConstrainedBySchedulingGroup](../30/KiIsThreadConstrainedBySchedulingGroup_function_0030B200.md) (function, `0x0030B200`)
- `0x0025AB91` → [KiCheckForMaxOverQuotaScb](../20/KiCheckForMaxOverQuotaScb_function_002027A0.md) (function, `0x002027A0`)
- `0x0025ABA1` → [KiShouldPreemptionBeDeferred](../35/KiShouldPreemptionBeDeferred_function_00356310.md) (function, `0x00356310`)
- `0x0025ACC8` → [KiIsThreadExemptFromForcePark](../4D/KiIsThreadExemptFromForcePark_function_004D7B80.md) (function, `0x004D7B80`)
- `0x0025AD15` → [KiRemoveCurrentlyEnumeratedThreadFromReadyQueue](../20/KiRemoveCurrentlyEnumeratedThreadFromReadyQueue_function_00201790.md) (function, `0x00201790`)
- `0x0025AD1D` → [KiEnterDeferredReadyState](../39/KiEnterDeferredReadyState_function_00397420.md) (function, `0x00397420`)
- `0x0025AD94` → [KiAdvanceReadyQueueEnumeratorToNextScb](../20/KiAdvanceReadyQueueEnumeratorToNextScb_function_0020227C.md) (function, `0x0020227C`)
- `0x0025AE04` → [KiAdvanceReadyQueueEnumeratorToNextList](../20/KiAdvanceReadyQueueEnumeratorToNextList_function_00201C50.md) (function, `0x00201C50`)
- `0x0025AE17` → [KiRemoveThreadFromScbQueue](../20/KiRemoveThreadFromScbQueue_function_00201B64.md) (function, `0x00201B64`)
- `0x0025AE79` → [KxWaitForLockChainValid](../21/KxWaitForLockChainValid_function_00217AA0.md) (function, `0x00217AA0`)
- `0x0025AE95` → [KeWakeAddressAll](../21/KeWakeAddressAll_function_00217C20.md) (function, `0x00217C20`)
- `0x0025AF59` → [KiDoesThreadDominateRescheduleContextEntry](KiDoesThreadDominateRescheduleContextEntry_function_002581D0.md) (function, `0x002581D0`)
- `0x0025B002` → [KiInsertDeferredReadyList](../20/KiInsertDeferredReadyList_function_00201310.md) (function, `0x00201310`)
- `0x0025B055` → [KiIsPrcbThread](../35/KiIsPrcbThread_function_00353230.md) (function, `0x00353230`)
- `0x0025B0D9` → [KiIsPrcbThread](../35/KiIsPrcbThread_function_00353230.md) (function, `0x00353230`)
- `0x0025B0FE` → [KiInsertDeferredReadyList](../20/KiInsertDeferredReadyList_function_00201310.md) (function, `0x00201310`)
- `0x0025B15C` → [KiIsPrcbThread](../35/KiIsPrcbThread_function_00353230.md) (function, `0x00353230`)
- `0x0025B1E1` → [KiIsPrcbThread](../35/KiIsPrcbThread_function_00353230.md) (function, `0x00353230`)
- `0x0025B25B` → [KiIsPrcbThread](../35/KiIsPrcbThread_function_00353230.md) (function, `0x00353230`)
- `0x0025B2B1` → [KiCanLocalReadyThreadBeScheduledToRescheduleContextEntry](KiCanLocalReadyThreadBeScheduledToRescheduleContextEntry_function_00257D10.md) (function, `0x00257D10`)
- `0x0025B2DC` → [KiDoesThreadDominateRescheduleContextEntry](KiDoesThreadDominateRescheduleContextEntry_function_002581D0.md) (function, `0x002581D0`)
- `0x0025B2ED` → [KiIsPrcbThread](../35/KiIsPrcbThread_function_00353230.md) (function, `0x00353230`)
- `0x0025B312` → [KiInsertDeferredReadyList](../20/KiInsertDeferredReadyList_function_00201310.md) (function, `0x00201310`)
- `0x0025B31C` → [KiIsPrcbThread](../35/KiIsPrcbThread_function_00353230.md) (function, `0x00353230`)
- `0x0025B341` → [KiInsertDeferredReadyList](../20/KiInsertDeferredReadyList_function_00201310.md) (function, `0x00201310`)
- `0x0025B355` → [KiIsPrcbThread](../35/KiIsPrcbThread_function_00353230.md) (function, `0x00353230`)
- `0x0025B37A` → [KiInsertDeferredReadyList](../20/KiInsertDeferredReadyList_function_00201310.md) (function, `0x00201310`)
- `0x0025B384` → [KiIsPrcbThread](../35/KiIsPrcbThread_function_00353230.md) (function, `0x00353230`)
- `0x0025B3A9` → [KiInsertDeferredReadyList](../20/KiInsertDeferredReadyList_function_00201310.md) (function, `0x00201310`)
- `0x0025B3B3` → [KiIsPrcbThread](../35/KiIsPrcbThread_function_00353230.md) (function, `0x00353230`)
- `0x0025B3D8` → [KiInsertDeferredReadyList](../20/KiInsertDeferredReadyList_function_00201310.md) (function, `0x00201310`)
- `0x0025B47A` → [KiInsertDeferredReadyList](../20/KiInsertDeferredReadyList_function_00201310.md) (function, `0x00201310`)
- `0x0025B4FC` → [KiIsPrcbThread](../35/KiIsPrcbThread_function_00353230.md) (function, `0x00353230`)
- `0x0025B588` → [KiIsPrcbThread](../35/KiIsPrcbThread_function_00353230.md) (function, `0x00353230`)
- `0x0025B5A3` → [KiIsPrcbThread](../35/KiIsPrcbThread_function_00353230.md) (function, `0x00353230`)
- `0x0025B5C8` → [KiInsertDeferredReadyList](../20/KiInsertDeferredReadyList_function_00201310.md) (function, `0x00201310`)
- `0x0025B5D2` → [KiIsPrcbThread](../35/KiIsPrcbThread_function_00353230.md) (function, `0x00353230`)
- `0x0025B5F7` → [KiInsertDeferredReadyList](../20/KiInsertDeferredReadyList_function_00201310.md) (function, `0x00201310`)
- `0x0025B61E` → [KiIsThreadStateControlledByProcessor](../30/KiIsThreadStateControlledByProcessor_function_00306254.md) (function, `0x00306254`)
- `0x0025B630` → [KiUpdateVPBackingThreadPriority](../30/KiUpdateVPBackingThreadPriority_function_00306040.md) (function, `0x00306040`)
- `0x0025B699` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [sub_0025308F](Unknown_function_0025308F.md) at `0x00253E03`

### Static image references
- `0x00259B1F` → RVA `0x00E0A740` (`.data`; read)
- `0x00259D5F` → RVA `0x00FC6ABC` (`ALMOSTRO`; read)
- `0x00259F0A` → RVA `0x00FC6B38` (`ALMOSTRO`; read)
- `0x0025A0C9` → RVA `0x00FC5007` (`ALMOSTRO`; read)
- `0x0025A0E8` → RVA `0x00FCD260` (`ALMOSTRO`; read)
- `0x0025A109` → RVA `0x00FC6B14` (`ALMOSTRO`; read)
- `0x0025A461` → RVA `0x00FC6BF8` (`ALMOSTRO`; read)
- `0x0025A4B1` → RVA `0x00FC52E0` (`ALMOSTRO`; read)
- `0x0025A51D` → RVA `0x00FC537C` (`ALMOSTRO`; read)
- `0x0025AFBE` → RVA `0x00FCFF00` (`CACHEALI`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x0025A5FA` → [sub_006D8D7A](../6D/Unknown_function_006D8D7A.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00259B00  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
00259B05  55                              push rbp
00259B06  56                              push rsi
00259B07  57                              push rdi
00259B08  41 54                           push r12
00259B0A  41 55                           push r13
00259B0C  41 56                           push r14
00259B0E  41 57                           push r15
00259B10  48 8D AC 24 10 FF FF FF         lea rbp, [rsp - 0xf0]
00259B18  48 81 EC F0 01 00 00            sub rsp, 0x1f0
00259B1F  48 8B 05 1A 0C BB 00            mov rax, qword ptr [rip + 0xbb0c1a]
00259B26  48 33 C4                        xor rax, rsp
00259B29  48 89 85 E0 00 00 00            mov qword ptr [rbp + 0xe0], rax
00259B30  48 8B 85 50 01 00 00            mov rax, qword ptr [rbp + 0x150]
00259B37  49 8B D9                        mov rbx, r9
00259B3A  4C 8B B1 E8 37 00 00            mov r14, qword ptr [rcx + 0x37e8]
00259B41  4C 8B F9                        mov r15, rcx
00259B44  4D 8B 21                        mov r12, qword ptr [r9]
00259B47  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00259B4C  49 83 E4 FE                     and r12, 0xfffffffffffffffe
00259B50  48 8B 85 58 01 00 00            mov rax, qword ptr [rbp + 0x158]
00259B57  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
00259B5B  48 8B 85 60 01 00 00            mov rax, qword ptr [rbp + 0x160]
00259B62  44 88 44 24 30                  mov byte ptr [rsp + 0x30], r8b
00259B67  41 B8 F0 00 00 00               mov r8d, 0xf0
00259B6D  48 89 54 24 38                  mov qword ptr [rsp + 0x38], rdx
00259B72  33 D2                           xor edx, edx
00259B74  48 89 4C 24 60                  mov qword ptr [rsp + 0x60], rcx
00259B79  49 8B CE                        mov rcx, r14
00259B7C  48 89 45 98                     mov qword ptr [rbp - 0x68], rax
00259B80  48 89 5C 24 78                  mov qword ptr [rsp + 0x78], rbx
00259B85  E8 B6 D0 46 00                  call 0x1406c6c40
00259B8A  4C 8B 03                        mov r8, qword ptr [rbx]
00259B8D  33 FF                           xor edi, edi
00259B8F  49 8B C8                        mov rcx, r8
00259B92  48 89 7C 24 68                  mov qword ptr [rsp + 0x68], rdi
00259B97  48 83 E1 FE                     and rcx, 0xfffffffffffffffe
00259B9B  89 7C 24 40                     mov dword ptr [rsp + 0x40], edi
00259B9F  41 83 E0 01                     and r8d, 1
00259BA3  48 89 4D A0                     mov qword ptr [rbp - 0x60], rcx
00259BA7  4C 89 44 24 70                  mov qword ptr [rsp + 0x70], r8
00259BAC  44 8B DF                        mov r11d, edi
00259BAF  44 8B CF                        mov r9d, edi
00259BB2  0F 84 8F 03 00 00               je 0x140259f47
00259BB8  41 83 F8 01                     cmp r8d, 1
00259BBC  75 20                           jne 0x140259bde
00259BBE  48 8B 81 58 8E 00 00            mov rax, qword ptr [rcx + 0x8e58]
00259BC5  4C 8B 99 58 8E 00 00            mov r11, qword ptr [rcx + 0x8e58]
00259BCC  49 83 C3 08                     add r11, 8
00259BD0  4C 89 5C 24 68                  mov qword ptr [rsp + 0x68], r11
00259BD5  44 0F B6 08                     movzx r9d, byte ptr [rax]
00259BD9  44 89 4C 24 40                  mov dword ptr [rsp + 0x40], r9d
00259BDE  44 8B EF                        mov r13d, edi
00259BE1  45 85 C9                        test r9d, r9d
00259BE4  0F 84 FF 00 00 00               je 0x140259ce9
00259BEA  4C 8B 7C 24 38                  mov r15, qword ptr [rsp + 0x38]
00259BEF  49 8D 5E 30                     lea rbx, [r14 + 0x30]
00259BF3  45 8B C1                        mov r8d, r9d
00259BF6  4C 89 44 24 48                  mov qword ptr [rsp + 0x48], r8
00259BFB  0F 57 C0                        xorps xmm0, xmm0
00259BFE  33 C0                           xor eax, eax
00259C00  0F 11 43 E0                     movups xmmword ptr [rbx - 0x20], xmm0
00259C04  0F 11 43 F0                     movups xmmword ptr [rbx - 0x10], xmm0
00259C08  48 89 03                        mov qword ptr [rbx], rax
00259C0B  48 C7 43 F8 FF FF FF FF         mov qword ptr [rbx - 8], 0xffffffffffffffff
00259C13  C6 43 04 3F                     mov byte ptr [rbx + 4], 0x3f
00259C17  49 8B 33                        mov rsi, qword ptr [r11]
00259C1A  48 89 73 E0                     mov qword ptr [rbx - 0x20], rsi
00259C1E  48 89 7B E8                     mov qword ptr [rbx - 0x18], rdi
00259C22  48 8B 8E 48 8E 00 00            mov rcx, qword ptr [rsi + 0x8e48]
00259C29  48 85 C9                        test rcx, rcx
00259C2C  0F 85 39 03 00 00               jne 0x140259f6b
00259C32  4C 8B 56 10                     mov r10, qword ptr [rsi + 0x10]
00259C36  4C 89 53 F0                     mov qword ptr [rbx - 0x10], r10
00259C3A  4D 85 D2                        test r10, r10
00259C3D  75 08                           jne 0x140259c47
00259C3F  4C 8B 56 08                     mov r10, qword ptr [rsi + 8]
00259C43  4C 89 53 F0                     mov qword ptr [rbx - 0x10], r10
00259C47  4C 39 56 10                     cmp qword ptr [rsi + 0x10], r10
00259C4B  0F 84 12 03 00 00               je 0x140259f63
00259C51  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
00259C5A  0F B6 0B                        movzx ecx, byte ptr [rbx]
00259C5D  48 3B F0                        cmp rsi, rax
00259C60  0F 84 D9 02 00 00               je 0x140259f3f
00259C66  80 E1 FB                        and cl, 0xfb
00259C69  88 0B                           mov byte ptr [rbx], cl
00259C6B  45 32 C9                        xor r9b, r9b
00259C6E  41 F7 42 78 00 00 40 00         test dword ptr [r10 + 0x78], 0x400000
00259C76  44 88 4C 24 31                  mov byte ptr [rsp + 0x31], r9b
00259C7B  0F 85 DB 19 00 00               jne 0x14025b65c
00259C81  0F B6 46 23                     movzx eax, byte ptr [rsi + 0x23]
00259C85  0F B6 13                        movzx edx, byte ptr [rbx]
00259C88  F6 D0                           not al
00259C8A  24 01                           and al, 1
00259C8C  80 E2 FE                        and dl, 0xfe
00259C8F  0A D0                           or dl, al
00259C91  88 13                           mov byte ptr [rbx], dl
00259C93  48 8B 46 38                     mov rax, qword ptr [rsi + 0x38]
00259C97  0F B6 08                        movzx ecx, byte ptr [rax]
00259C9A  C0 E9 06                        shr cl, 6
00259C9D  32 CA                           xor cl, dl
00259C9F  80 E1 02                        and cl, 2
00259CA2  32 CA                           xor cl, dl
00259CA4  0F B6 C1                        movzx eax, cl
00259CA7  88 03                           mov byte ptr [rbx], al
00259CA9  D1 E8                           shr eax, 1
00259CAB  83 E0 01                        and eax, 1
00259CAE  41 3B C5                        cmp eax, r13d
00259CB1  44 0F 4F E8                     cmovg r13d, eax
00259CB5  49 83 C3 08                     add r11, 8
00259CB9  48 83 C3 28                     add rbx, 0x28
00259CBD  4C 89 5C 24 68                  mov qword ptr [rsp + 0x68], r11
00259CC2  49 83 E8 01                     sub r8, 1
00259CC6  4C 89 44 24 48                  mov qword ptr [rsp + 0x48], r8
00259CCB  0F 85 2A FF FF FF               jne 0x140259bfb
00259CD1  48 8B 4D A0                     mov rcx, qword ptr [rbp - 0x60]
00259CD5  4C 8B 7C 24 60                  mov r15, qword ptr [rsp + 0x60]
00259CDA  4C 8B 44 24 70                  mov r8, qword ptr [rsp + 0x70]
00259CDF  44 8B 4C 24 40                  mov r9d, dword ptr [rsp + 0x40]
00259CE4  48 8B 5C 24 78                  mov rbx, qword ptr [rsp + 0x78]
00259CE9  45 89 6E 04                     mov dword ptr [r14 + 4], r13d
00259CED  BA 01 00 00 00                  mov edx, 1
00259CF2  45 89 46 08                     mov dword ptr [r14 + 8], r8d
00259CF6  45 88 0E                        mov byte ptr [r14], r9b
00259CF9  45 85 C0                        test r8d, r8d
00259CFC  0F 84 36 02 00 00               je 0x140259f38
00259D02  48 8B 81 58 8E 00 00            mov rax, qword ptr [rcx + 0x8e58]
00259D09  0F B6 40 01                     movzx eax, byte ptr [rax + 1]
00259D0D  49 8B CE                        mov rcx, r14
00259D10  88 04 0A                        mov byte ptr [rdx + rcx], al
00259D13  45 85 ED                        test r13d, r13d
00259D16  0F 85 56 13 00 00               jne 0x14025b072
00259D1C  44 8B 4B 0C                     mov r9d, dword ptr [rbx + 0xc]
00259D20  8B D7                           mov edx, edi
00259D22  45 0F B6 06                     movzx r8d, byte ptr [r14]
00259D26  48 8B DF                        mov rbx, rdi
00259D29  0F 1F 80 00 00 00 00            nop dword ptr [rax]
00259D30  41 3B D0                        cmp edx, r8d
00259D33  73 19                           jae 0x140259d4e
00259D35  8B C2                           mov eax, edx
00259D37  48 8D 0C 80                     lea rcx, [rax + rax*4]
00259D3B  4D 39 64 CE 10                  cmp qword ptr [r14 + rcx*8 + 0x10], r12
00259D40  49 8D 04 CE                     lea rax, [r14 + rcx*8]
00259D44  74 04                           je 0x140259d4a
00259D46  FF C2                           inc edx
00259D48  EB E6                           jmp 0x140259d30
00259D4A  48 8D 58 10                     lea rbx, [rax + 0x10]
00259D4E  45 85 C9                        test r9d, r9d
00259D51  8B F7                           mov esi, edi
00259D53  48 8B D7                        mov rdx, rdi
00259D56  40 0F 95 C6                     setne sil
00259D5A  48 89 54 24 70                  mov qword ptr [rsp + 0x70], rdx
00259D5F  40 38 3D 56 CD D6 00            cmp byte ptr [rip + 0xd6cd56], dil
00259D66  0F 84 E5 03 00 00               je 0x14025a151
00259D6C  48 8B 54 24 38                  mov rdx, qword ptr [rsp + 0x38]
00259D71  4C 8D 4C 24 70                  lea r9, [rsp + 0x70]
00259D76  44 8B C6                        mov r8d, esi
00259D79  48 8B CB                        mov rcx, rbx
00259D7C  E8 EF E4 FF FF                  call 0x140258270
00259D81  48 8B 54 24 70                  mov rdx, qword ptr [rsp + 0x70]
00259D86  48 8B 4D 98                     mov rcx, qword ptr [rbp - 0x68]
00259D8A  48 85 C9                        test rcx, rcx
00259D8D  74 03                           je 0x140259d92
00259D8F  48 89 11                        mov qword ptr [rcx], rdx
00259D92  84 C0                           test al, al
00259D94  0F 84 58 02 00 00               je 0x140259ff2
00259D9A  4C 8B 6C 24 38                  mov r13, qword ptr [rsp + 0x38]
00259D9F  0F B6 43 20                     movzx eax, byte ptr [rbx + 0x20]
00259DA3  D1 E8                           shr eax, 1
00259DA5  83 E0 01                        and eax, 1
00259DA8  41 8B 4D 78                     mov ecx, dword ptr [r13 + 0x78]
00259DAC  D1 E9                           shr ecx, 1
00259DAE  83 E1 01                        and ecx, 1
00259DB1  3B C8                           cmp ecx, eax
00259DB3  0F 42 C8                        cmovb ecx, eax
00259DB6  83 F9 01                        cmp ecx, 1
00259DB9  0F 84 6C 11 00 00               je 0x14025af2b
00259DBF  45 0F B6 06                     movzx r8d, byte ptr [r14]
00259DC3  4C 8B CF                        mov r9, rdi
00259DC6  8B D7                           mov edx, edi
00259DC8  41 3B D0                        cmp edx, r8d
00259DCB  73 19                           jae 0x140259de6
00259DCD  8B C2                           mov eax, edx
00259DCF  48 8D 0C 80                     lea rcx, [rax + rax*4]
00259DD3  4D 39 64 CE 10                  cmp qword ptr [r14 + rcx*8 + 0x10], r12
00259DD8  49 8D 04 CE                     lea rax, [r14 + rcx*8]
00259DDC  74 04                           je 0x140259de2
00259DDE  FF C2                           inc edx
00259DE0  EB E6                           jmp 0x140259dc8
00259DE2  4C 8D 48 10                     lea r9, [rax + 0x10]
00259DE6  45 8B 55 78                     mov r10d, dword ptr [r13 + 0x78]
00259DEA  41 0F B6 41 20                  movzx eax, byte ptr [r9 + 0x20]
00259DEF  41 D1 EA                        shr r10d, 1
00259DF2  D1 E8                           shr eax, 1
00259DF4  41 83 E2 01                     and r10d, 1
00259DF8  83 E0 01                        and eax, 1
00259DFB  44 89 54 24 40                  mov dword ptr [rsp + 0x40], r10d
00259E00  44 3B D0                        cmp r10d, eax
00259E03  0F 83 D9 15 00 00               jae 0x14025b3e2
00259E09  8B DF                           mov ebx, edi
00259E0B  41 38 3E                        cmp byte ptr [r14], dil
00259E0E  0F 86 A0 00 00 00               jbe 0x140259eb4
00259E14  44 0F B6 5C 24 30               movzx r11d, byte ptr [rsp + 0x30]
00259E1A  4C 8B 7C 24 50                  mov r15, qword ptr [rsp + 0x50]
00259E1F  4C 8B 54 24 38                  mov r10, qword ptr [rsp + 0x38]
00259E24  8B C3                           mov eax, ebx
00259E26  48 8D 0C 80                     lea rcx, [rax + rax*4]
00259E2A  4D 8B 6C CE 10                  mov r13, qword ptr [r14 + rcx*8 + 0x10]
00259E2F  4D 8D 0C CE                     lea r9, [r14 + rcx*8]
00259E33  49 8B 4C CE 28                  mov rcx, qword ptr [r14 + rcx*8 + 0x28]
00259E38  48 8D 41 FF                     lea rax, [rcx - 1]
00259E3C  4D 3B EC                        cmp r13, r12
00259E3F  0F 84 C4 11 00 00               je 0x14025b009
00259E45  49 8B 75 18                     mov rsi, qword ptr [r13 + 0x18]
00259E49  48 83 F8 FC                     cmp rax, -4
00259E4D  0F 86 86 12 00 00               jbe 0x14025b0d9
00259E53  41 0F B6 41 30                  movzx eax, byte ptr [r9 + 0x30]
00259E58  0C 01                           or al, 1
00259E5A  49 89 71 20                     mov qword ptr [r9 + 0x20], rsi
00259E5E  41 88 41 30                     mov byte ptr [r9 + 0x30], al
00259E62  24 FD                           and al, 0xfd
00259E64  8B 4E 78                        mov ecx, dword ptr [rsi + 0x78]
00259E67  D1 E9                           shr ecx, 1
00259E69  80 E1 01                        and cl, 1
00259E6C  02 C9                           add cl, cl
00259E6E  32 C8                           xor cl, al
00259E70  80 E1 E7                        and cl, 0xe7
00259E73  80 C9 04                        or cl, 4
00259E76  80 E1 DF                        and cl, 0xdf
00259E79  41 88 49 30                     mov byte ptr [r9 + 0x30], cl
00259E7D  48 8B CE                        mov rcx, rsi
00259E80  41 80 61 31 FE                  and byte ptr [r9 + 0x31], 0xfe
00259E85  49 89 71 28                     mov qword ptr [r9 + 0x28], rsi
00259E89  E8 A2 93 0F 00                  call 0x140353230
00259E8E  84 C0                           test al, al
00259E90  75 0A                           jne 0x140259e9c
00259E92  41 8B 45 24                     mov eax, dword ptr [r13 + 0x24]
00259E96  89 86 18 02 00 00               mov dword ptr [rsi + 0x218], eax
00259E9C  41 0F B6 06                     movzx eax, byte ptr [r14]
00259EA0  FF C3                           inc ebx
00259EA2  3B D8                           cmp ebx, eax
00259EA4  0F 82 7A FF FF FF               jb 0x140259e24
00259EAA  4C 8B 7C 24 60                  mov r15, qword ptr [rsp + 0x60]
00259EAF  44 8B 54 24 40                  mov r10d, dword ptr [rsp + 0x40]
00259EB4  45 89 56 04                     mov dword ptr [r14 + 4], r10d
00259EB8  4C 8B C7                        mov r8, rdi
00259EBB  8B F7                           mov esi, edi
00259EBD  0F 1F 00                        nop dword ptr [rax]
00259EC0  41 0F B6 06                     movzx eax, byte ptr [r14]
00259EC4  48 8B DF                        mov rbx, rdi
00259EC7  84 C0                           test al, al
00259EC9  0F 84 21 03 00 00               je 0x14025a1f0
00259ECF  49 8D 4E 18                     lea rcx, [r14 + 0x18]
00259ED3  8B D0                           mov edx, eax
00259ED5  48 8B 01                        mov rax, qword ptr [rcx]
00259ED8  49 3B C0                        cmp rax, r8
00259EDB  76 0D                           jbe 0x140259eea
00259EDD  48 85 DB                        test rbx, rbx
00259EE0  74 05                           je 0x140259ee7
00259EE2  48 3B C3                        cmp rax, rbx
00259EE5  73 03                           jae 0x140259eea
00259EE7  48 8B D8                        mov rbx, rax
00259EEA  48 83 C1 28                     add rcx, 0x28
00259EEE  48 83 EA 01                     sub rdx, 1
00259EF2  75 E1                           jne 0x140259ed5
00259EF4  48 85 DB                        test rbx, rbx
00259EF7  0F 84 F3 02 00 00               je 0x14025a1f0
00259EFD  8B CE                           mov ecx, esi
00259EFF  48 83 C1 0B                     add rcx, 0xb
00259F03  48 C1 E1 04                     shl rcx, 4
00259F07  49 03 CE                        add rcx, r14
00259F0A  F7 05 24 CC D6 00 00 00 20 00   test dword ptr [rip + 0xd6cc24], 0x200000
00259F14  0F 84 D1 06 00 00               je 0x14025a5eb
00259F1A  48 89 59 08                     mov qword ptr [rcx + 8], rbx
00259F1E  48 8B D1                        mov rdx, rcx
00259F21  48 89 39                        mov qword ptr [rcx], rdi
00259F24  90                              nop
00259F25  48 87 13                        xchg qword ptr [rbx], rdx
00259F28  48 85 D2                        test rdx, rdx
00259F2B  0F 85 FC 08 00 00               jne 0x14025a82d
00259F31  FF C6                           inc esi
00259F33  4C 8B C3                        mov r8, rbx
00259F36  EB 88                           jmp 0x140259ec0
00259F38  32 C0                           xor al, al
00259F3A  E9 CE FD FF FF                  jmp 0x140259d0d
00259F3F  80 C9 04                        or cl, 4
00259F42  E9 22 FD FF FF                  jmp 0x140259c69
00259F47  4C 8D 5D A0                     lea r11, [rbp - 0x60]
00259F4B  41 B9 01 00 00 00               mov r9d, 1
00259F51  4C 89 5C 24 68                  mov qword ptr [rsp + 0x68], r11
00259F56  44 8B EF                        mov r13d, edi
00259F59  44 89 4C 24 40                  mov dword ptr [rsp + 0x40], r9d
00259F5E  E9 87 FC FF FF                  jmp 0x140259bea
00259F63  80 0B 04                        or byte ptr [rbx], 4
00259F66  E9 00 FD FF FF                  jmp 0x140259c6b
00259F6B  F6 46 23 10                     test byte ptr [rsi + 0x23], 0x10
00259F6F  0F 85 1C 02 00 00               jne 0x14025a191
00259F75  48 8B 86 48 8E 00 00            mov rax, qword ptr [rsi + 0x8e48]
00259F7C  48 89 43 E8                     mov qword ptr [rbx - 0x18], rax
00259F80  E9 AD FC FF FF                  jmp 0x140259c32
00259F85  41 0F B6 87 D9 35 00 00         movzx eax, byte ptr [r15 + 0x35d9]
00259F8D  84 C0                           test al, al
00259F8F  0F 85 AC 00 00 00               jne 0x14025a041
00259F95  41 C6 87 D9 35 00 00 01         mov byte ptr [r15 + 0x35d9], 1
00259F9D  8B 46 24                        mov eax, dword ptr [rsi + 0x24]
00259FA0  41 89 87 DC 35 00 00            mov dword ptr [r15 + 0x35dc], eax
00259FA7  41 F6 44 DE 33 02               test byte ptr [r14 + rbx*8 + 0x33], 2
00259FAD  0F 85 7E 01 00 00               jne 0x14025a131
00259FB3  41 F6 44 DE 33 04               test byte ptr [r14 + rbx*8 + 0x33], 4
00259FB9  74 16                           je 0x140259fd1
00259FBB  48 8B 86 B8 8E 00 00            mov rax, qword ptr [rsi + 0x8eb8]
00259FC2  41 0F BE 4C DE 34               movsx ecx, byte ptr [r14 + rbx*8 + 0x34]
00259FC8  48 85 C0                        test rax, rax
00259FCB  0F 85 BF 00 00 00               jne 0x14025a090
00259FD1  41 F6 44 DE 33 01               test byte ptr [r14 + rbx*8 + 0x33], 1
00259FD7  74 0D                           je 0x140259fe6
00259FD9  49 8B 44 DE 28                  mov rax, qword ptr [r14 + rbx*8 + 0x28]
00259FDE  66 F0 FF 88 64 03 00 00         lock dec word ptr [rax + 0x364]
00259FE6  41 0F B6 06                     movzx eax, byte ptr [r14]
00259FEA  FF C7                           inc edi
00259FEC  3B F8                           cmp edi, eax
00259FEE  72 20                           jb 0x14025a010
00259FF0  B0 01                           mov al, 1
00259FF2  E9 98 16 00 00                  jmp 0x14025b68f
00259FF7  CC                              int3
00259FF8  33 C0                           xor eax, eax
00259FFA  49 89 02                        mov qword ptr [r10], rax
00259FFD  49 89 7D 40                     mov qword ptr [r13 + 0x40], rdi
0025A001  45 84 E4                        test r12b, r12b
0025A004  74 EA                           je 0x140259ff0
0025A006  41 38 06                        cmp byte ptr [r14], al
0025A009  76 E5                           jbe 0x140259ff0
0025A00B  0F 1F 44 00 00                  nop dword ptr [rax + rax]
0025A010  8B C7                           mov eax, edi
0025A012  48 8D 1C 80                     lea rbx, [rax + rax*4]
0025A016  41 0F B6 44 DE 33               movzx eax, byte ptr [r14 + rbx*8 + 0x33]
0025A01C  49 8B 74 DE 10                  mov rsi, qword ptr [r14 + rbx*8 + 0x10]
0025A021  A8 10                           test al, 0x10
0025A023  0F 85 5C FF FF FF               jne 0x140259f85
0025A029  A8 08                           test al, 8
0025A02B  0F 84 76 FF FF FF               je 0x140259fa7
0025A031  90                              nop
0025A032  80 7E 07 00                     cmp byte ptr [rsi + 7], 0
0025A036  0F 85 49 FF FF FF               jne 0x140259f85
0025A03C  E9 66 FF FF FF                  jmp 0x140259fa7
0025A041  3C 01                           cmp al, 1
0025A043  75 42                           jne 0x14025a087
0025A045  41 8B 97 DC 35 00 00            mov edx, dword ptr [r15 + 0x35dc]
0025A04C  3B 56 24                        cmp edx, dword ptr [rsi + 0x24]
0025A04F  0F 84 52 FF FF FF               je 0x140259fa7
0025A055  4D 8D A7 E0 35 00 00            lea r12, [r15 + 0x35e0]
0025A05C  41 C6 87 D9 35 00 00 02         mov byte ptr [r15 + 0x35d9], 2
0025A064  49 8B CC                        mov rcx, r12
0025A067  E8 84 16 00 00                  call 0x14025b6f0
0025A06C  4C 8B 86 C8 00 00 00            mov r8, qword ptr [rsi + 0xc8]
0025A073  49 8B CC                        mov rcx, r12
0025A076  0F B6 96 D0 00 00 00            movzx edx, byte ptr [rsi + 0xd0]
0025A07D  E8 3E 16 00 00                  call 0x14025b6c0
0025A082  E9 20 FF FF FF                  jmp 0x140259fa7
0025A087  4D 8D A7 E0 35 00 00            lea r12, [r15 + 0x35e0]
0025A08E  EB DC                           jmp 0x14025a06c
0025A090  49 83 BF B8 8E 00 00 00         cmp qword ptr [r15 + 0x8eb8], 0
0025A098  0F 84 33 FF FF FF               je 0x140259fd1
0025A09E  4C 3B FE                        cmp r15, rsi
0025A0A1  0F 84 2A FF FF FF               je 0x140259fd1
0025A0A7  8B 10                           mov edx, dword ptr [rax]
0025A0A9  8B C2                           mov eax, edx
0025A0AB  25 00 00 04 00                  and eax, 0x40000
0025A0B0  0F BA E2 14                     bt edx, 0x14
0025A0B4  72 13                           jb 0x14025a0c9
0025A0B6  85 C0                           test eax, eax
0025A0B8  0F 84 13 FF FF FF               je 0x140259fd1
0025A0BE  0F B6 C2                        movzx eax, dl
0025A0C1  3B C1                           cmp eax, ecx
0025A0C3  0F 8D 08 FF FF FF               jge 0x140259fd1
0025A0C9  80 3D 37 AF D6 00 00            cmp byte ptr [rip + 0xd6af37], 0
0025A0D0  BA 02 00 00 00                  mov edx, 2
0025A0D5  49 8B 8F B8 8E 00 00            mov rcx, qword ptr [r15 + 0x8eb8]
0025A0DC  89 51 0C                        mov dword ptr [rcx + 0xc], edx
0025A0DF  44 8B 66 24                     mov r12d, dword ptr [rsi + 0x24]
0025A0E3  75 20                           jne 0x14025a105
0025A0E5  41 8B C4                        mov eax, r12d
0025A0E8  48 8D 15 71 31 D7 00            lea rdx, [rip + 0xd73171]
0025A0EF  46 0F B6 24 62                  movzx r12d, byte ptr [rdx + r12*2]
0025A0F4  41 C1 E4 06                     shl r12d, 6
0025A0F8  0F B6 44 42 01                  movzx eax, byte ptr [rdx + rax*2 + 1]
0025A0FD  BA 02 00 00 00                  mov edx, 2
0025A102  44 0B E0                        or r12d, eax
0025A105  44 89 61 08                     mov dword ptr [rcx + 8], r12d
0025A109  8B 05 05 CA D6 00               mov eax, dword ptr [rip + 0xd6ca05]
0025A10F  A8 20                           test al, 0x20
0025A111  74 08                           je 0x14025a11b
0025A113  8B 4E 24                        mov ecx, dword ptr [rsi + 0x24]
0025A116  E8 A5 11 2A 00                  call 0x1404fb2c0
0025A11B  41 8B D4                        mov edx, r12d
0025A11E  B9 C2 00 00 40                  mov ecx, 0x400000c2
0025A123  48 C1 EA 20                     shr rdx, 0x20
0025A127  41 8B C4                        mov eax, r12d
0025A12A  0F 30                           wrmsr
0025A12C  E9 A0 FE FF FF                  jmp 0x140259fd1
0025A131  49 8B 4C DE 28                  mov rcx, qword ptr [r14 + rbx*8 + 0x28]
0025A136  48 8B D6                        mov rdx, rsi
0025A139  49 3B CD                        cmp rcx, r13
0025A13C  75 0E                           jne 0x14025a14c
0025A13E  4C 8B 45 C8                     mov r8, qword ptr [rbp - 0x38]
0025A142  E8 05 16 0B 00                  call 0x14030b74c
0025A147  E9 67 FE FF FF                  jmp 0x140259fb3
0025A14C  45 33 C0                        xor r8d, r8d
0025A14F  EB F1                           jmp 0x14025a142
0025A151  44 0F B6 4B 20                  movzx r9d, byte ptr [rbx + 0x20]
0025A156  48 8B 43 10                     mov rax, qword ptr [rbx + 0x10]
0025A15A  41 F6 C1 01                     test r9b, 1
0025A15E  75 67                           jne 0x14025a1c7
0025A160  4C 8B 44 24 38                  mov r8, qword ptr [rsp + 0x38]
0025A165  45 0F B6 80 C3 00 00 00         movzx r8d, byte ptr [r8 + 0xc3]
0025A16D  44 3A 80 C3 00 00 00            cmp r8b, byte ptr [rax + 0xc3]
0025A174  7F 6A                           jg 0x14025a1e0
0025A176  75 56                           jne 0x14025a1ce
0025A178  41 F6 C1 18                     test r9b, 0x18
0025A17C  0F 94 C1                        sete cl
0025A17F  40 F6 C6 01                     test sil, 1
0025A183  0F 94 C0                        sete al
0025A186  84 C8                           test al, cl
0025A188  75 44                           jne 0x14025a1ce
0025A18A  B0 01                           mov al, 1
0025A18C  E9 F5 FB FF FF                  jmp 0x140259d86
0025A191  48 8B 96 C0 00 00 00            mov rdx, qword ptr [rsi + 0xc0]
0025A198  E8 83 ED FB FF                  call 0x140218f20
0025A19D  84 C0                           test al, al
0025A19F  74 0A                           je 0x14025a1ab
0025A1A1  F6 46 23 20                     test byte ptr [rsi + 0x23], 0x20
0025A1A5  0F 85 C6 10 00 00               jne 0x14025b271
0025A1AB  48 8B 42 50                     mov rax, qword ptr [rdx + 0x50]
0025A1AF  48 8B 91 C8 02 00 00            mov rdx, qword ptr [rcx + 0x2c8]
0025A1B6  48 23 D0                        and rdx, rax
0025A1B9  48 85 D2                        test rdx, rdx
0025A1BC  0F 84 B3 FD FF FF               je 0x140259f75
0025A1C2  E9 6B FA FF FF                  jmp 0x140259c32
0025A1C7  B0 01                           mov al, 1
0025A1C9  E9 B8 FB FF FF                  jmp 0x140259d86
0025A1CE  41 F6 C1 10                     test r9b, 0x10
0025A1D2  74 13                           je 0x14025a1e7
0025A1D4  45 84 C0                        test r8b, r8b
0025A1D7  74 0E                           je 0x14025a1e7
0025A1D9  B0 01                           mov al, 1
0025A1DB  E9 A6 FB FF FF                  jmp 0x140259d86
0025A1E0  B0 01                           mov al, 1
0025A1E2  E9 9F FB FF FF                  jmp 0x140259d86
0025A1E7  32 C0                           xor al, al
0025A1E9  E9 98 FB FF FF                  jmp 0x140259d86
0025A1EE  66 90                           nop
0025A1F0  33 D2                           xor edx, edx
0025A1F2  48 8D 4D F0                     lea rcx, [rbp - 0x10]
0025A1F6  41 B8 F0 00 00 00               mov r8d, 0xf0
0025A1FC  E8 3F CA 46 00                  call 0x1406c6c40
0025A201  49 8B D6                        mov rdx, r14
0025A204  48 8D 4D F0                     lea rcx, [rbp - 0x10]
0025A208  E8 13 F6 FF FF                  call 0x140259820
0025A20D  0F B6 45 FD                     movzx eax, byte ptr [rbp - 3]
0025A211  3C 04                           cmp al, 4
0025A213  0F 84 34 06 00 00               je 0x14025a84d
0025A219  84 C0                           test al, al
0025A21B  0F 85 EE 01 00 00               jne 0x14025a40f
0025A221  44 0F B6 55 F9                  movzx r10d, byte ptr [rbp - 7]
0025A226  40 B6 01                        mov sil, 1
0025A229  44 8B 45 F0                     mov r8d, dword ptr [rbp - 0x10]
0025A22D  0F 1F 00                        nop dword ptr [rax]
0025A230  40 0F B6 CE                     movzx ecx, sil
0025A234  83 F9 02                        cmp ecx, 2
0025A237  0F 84 12 01 00 00               je 0x14025a34f
0025A23D  83 E9 01                        sub ecx, 1
0025A240  0F 85 B9 03 00 00               jne 0x14025a5ff
0025A246  8B C7                           mov eax, edi
0025A248  89 45 F4                        mov dword ptr [rbp - 0xc], eax
0025A24B  45 85 C0                        test r8d, r8d
0025A24E  0F 85 BD 04 00 00               jne 0x14025a711
0025A254  83 E0 FE                        and eax, 0xfffffffe
0025A257  89 45 F4                        mov dword ptr [rbp - 0xc], eax
0025A25A  0F 84 94 01 00 00               je 0x14025a3f4
0025A260  44 0F BD C8                     bsr r9d, eax
0025A264  44 88 55 FA                     mov byte ptr [rbp - 6], r10b
0025A268  41 BB 01 00 00 00               mov r11d, 1
0025A26E  44 88 4D F8                     mov byte ptr [rbp - 8], r9b
0025A272  41 0F B6 C2                     movzx eax, r10b
0025A276  44 89 4D 8C                     mov dword ptr [rbp - 0x74], r9d
0025A27A  48 8D 0C 40                     lea rcx, [rax + rax*2]
0025A27E  48 03 C9                        add rcx, rcx
0025A281  8B 54 CD 48                     mov edx, dword ptr [rbp + rcx*8 + 0x48]
0025A285  0B 54 CD 4C                     or edx, dword ptr [rbp + rcx*8 + 0x4c]
0025A289  41 0F B6 C9                     movzx ecx, r9b
0025A28D  41 D3 E3                        shl r11d, cl
0025A290  44 85 DA                        test edx, r11d
0025A293  75 2F                           jne 0x14025a2c4
0025A295  41 FE C2                        inc r10b
0025A298  41 0F B6 C2                     movzx eax, r10b
0025A29C  44 88 55 FA                     mov byte ptr [rbp - 6], r10b
0025A2A0  41 3B C0                        cmp eax, r8d
0025A2A3  72 07                           jb 0x14025a2ac
0025A2A5  45 32 D2                        xor r10b, r10b
0025A2A8  44 88 55 FA                     mov byte ptr [rbp - 6], r10b
0025A2AC  41 0F B6 C2                     movzx eax, r10b
0025A2B0  48 8D 0C 40                     lea rcx, [rax + rax*2]
0025A2B4  48 03 C9                        add rcx, rcx
0025A2B7  8B 54 CD 48                     mov edx, dword ptr [rbp + rcx*8 + 0x48]
0025A2BB  0B 54 CD 4C                     or edx, dword ptr [rbp + rcx*8 + 0x4c]
0025A2BF  44 85 DA                        test edx, r11d
0025A2C2  74 D1                           je 0x14025a295
0025A2C4  41 0F B6 C2                     movzx eax, r10b
0025A2C8  4C 8D 45 20                     lea r8, [rbp + 0x20]
0025A2CC  32 D2                           xor dl, dl
0025A2CE  48 8D 0C 40                     lea rcx, [rax + rax*2]
0025A2D2  48 C1 E1 04                     shl rcx, 4
0025A2D6  4C 03 C1                        add r8, rcx
0025A2D9  41 0F B6 C9                     movzx ecx, r9b
0025A2DD  4D 8B 18                        mov r11, qword ptr [r8]
0025A2E0  4D 8B 50 08                     mov r10, qword ptr [r8 + 8]
0025A2E4  88 55 FB                        mov byte ptr [rbp - 5], dl
0025A2E7  41 8B 40 28                     mov eax, dword ptr [r8 + 0x28]
0025A2EB  0F A3 C8                        bt eax, ecx
0025A2EE  73 05                           jae 0x14025a2f5
0025A2F0  B2 01                           mov dl, 1
0025A2F2  88 55 FB                        mov byte ptr [rbp - 5], dl
0025A2F5  41 8B 40 2C                     mov eax, dword ptr [r8 + 0x2c]
0025A2F9  41 0F B6 C9                     movzx ecx, r9b
0025A2FD  0F A3 C8                        bt eax, ecx
0025A300  73 06                           jae 0x14025a308
0025A302  80 CA 02                        or dl, 2
0025A305  88 55 FB                        mov byte ptr [rbp - 5], dl
0025A308  0F B6 CA                        movzx ecx, dl
0025A30B  8D 41 FF                        lea eax, [rcx - 1]
0025A30E  85 C1                           test ecx, eax
0025A310  0F 85 B6 0A 00 00               jne 0x14025adcc
0025A316  0F BC C1                        bsf eax, ecx
0025A319  89 45 90                        mov dword ptr [rbp - 0x70], eax
0025A31C  88 45 FC                        mov byte ptr [rbp - 4], al
0025A31F  0F B6 C8                        movzx ecx, al
0025A322  84 C0                           test al, al
0025A324  0F 84 00 09 00 00               je 0x14025ac2a
0025A32A  83 F9 01                        cmp ecx, 1
0025A32D  75 13                           jne 0x14025a342
0025A32F  41 0F B6 C1                     movzx eax, r9b
0025A333  48 83 C0 04                     add rax, 4
0025A337  48 C1 E0 04                     shl rax, 4
0025A33B  49 03 C2                        add rax, r10
0025A33E  48 89 45 10                     mov qword ptr [rbp + 0x10], rax
0025A342  48 8B 45 10                     mov rax, qword ptr [rbp + 0x10]
0025A346  48 89 45 18                     mov qword ptr [rbp + 0x18], rax
0025A34A  E9 B2 00 00 00                  jmp 0x14025a401
0025A34F  32 D2                           xor dl, dl
0025A351  45 85 C0                        test r8d, r8d
0025A354  74 5E                           je 0x14025a3b4
0025A356  66 66 0F 1F 84 00 00 00 00 00   nop word ptr [rax + rax]
0025A360  0F B6 C2                        movzx eax, dl
0025A363  48 8D 0C 40                     lea rcx, [rax + rax*2]
0025A367  48 03 C9                        add rcx, rcx
0025A36A  44 8B 4C CD 40                  mov r9d, dword ptr [rbp + rcx*8 + 0x40]
0025A36F  45 85 C9                        test r9d, r9d
0025A372  74 31                           je 0x14025a3a5
0025A374  48 8B 44 CD 20                  mov rax, qword ptr [rbp + rcx*8 + 0x20]
0025A379  48 05 30 84 00 00               add rax, 0x8430
0025A37F  4C 8B 40 08                     mov r8, qword ptr [rax + 8]
0025A383  41 F6 C0 01                     test r8b, 1
0025A387  0F 85 48 02 00 00               jne 0x14025a5d5
0025A38D  49 8B C0                        mov rax, r8
0025A390  48 85 C0                        test rax, rax
0025A393  0F 85 A7 08 00 00               jne 0x14025ac40
0025A399  48 8B C7                        mov rax, rdi
0025A39C  48 89 44 CD 30                  mov qword ptr [rbp + rcx*8 + 0x30], rax
0025A3A1  44 8B 45 F0                     mov r8d, dword ptr [rbp - 0x10]
0025A3A5  FE C2                           inc dl
0025A3A7  0F B6 C2                        movzx eax, dl
0025A3AA  41 3B C0                        cmp eax, r8d
0025A3AD  72 B1                           jb 0x14025a360
0025A3AF  44 0F B6 55 F9                  movzx r10d, byte ptr [rbp - 7]
0025A3B4  32 DB                           xor bl, bl
0025A3B6  4C 8B DF                        mov r11, rdi
0025A3B9  41 0F B6 D2                     movzx edx, r10b
0025A3BD  0F 1F 00                        nop dword ptr [rax]
0025A3C0  0F B6 C2                        movzx eax, dl
0025A3C3  48 8D 0C 40                     lea rcx, [rax + rax*2]
0025A3C7  48 03 C9                        add rcx, rcx
0025A3CA  4C 8B 4C CD 30                  mov r9, qword ptr [rbp + rcx*8 + 0x30]
0025A3CF  4D 85 C9                        test r9, r9
0025A3D2  0F 85 7B 08 00 00               jne 0x14025ac53
0025A3D8  FE C2                           inc dl
0025A3DA  0F B6 C2                        movzx eax, dl
0025A3DD  41 3B C0                        cmp eax, r8d
0025A3E0  0F B6 D2                        movzx edx, dl
0025A3E3  0F 43 D7                        cmovae edx, edi
0025A3E6  41 3A D2                        cmp dl, r10b
0025A3E9  75 D5                           jne 0x14025a3c0
0025A3EB  4D 85 DB                        test r11, r11
0025A3EE  0F 85 73 08 00 00               jne 0x14025ac67
0025A3F4  40 FE C6                        inc sil
0025A3F7  40 80 FE 04                     cmp sil, 4
0025A3FB  0F 82 2F FE FF FF               jb 0x14025a230
0025A401  40 88 75 FD                     mov byte ptr [rbp - 3], sil
0025A405  40 80 FE 04                     cmp sil, 4
0025A409  0F 84 3E 04 00 00               je 0x14025a84d
0025A40F  48 8B 45 18                     mov rax, qword ptr [rbp + 0x18]
0025A413  48 8B 30                        mov rsi, qword ptr [rax]
0025A416  48 89 75 18                     mov qword ptr [rbp + 0x18], rsi
0025A41A  48 3B 75 10                     cmp rsi, qword ptr [rbp + 0x10]
0025A41E  0F 84 18 04 00 00               je 0x14025a83c
0025A424  0F B6 45 FA                     movzx eax, byte ptr [rbp - 6]
0025A428  48 81 C6 28 FF FF FF            add rsi, -0xd8
0025A42F  48 8D 0C 40                     lea rcx, [rax + rax*2]
0025A433  48 03 C9                        add rcx, rcx
0025A436  80 7D FD 02                     cmp byte ptr [rbp - 3], 2
0025A43A  48 8B 5C CD 20                  mov rbx, qword ptr [rbp + rcx*8 + 0x20]
0025A43F  48 89 5C 24 58                  mov qword ptr [rsp + 0x58], rbx
0025A444  0F 84 0A 09 00 00               je 0x14025ad54
0025A44A  80 7D FC 01                     cmp byte ptr [rbp - 4], 1
0025A44E  0F 85 0C 07 00 00               jne 0x14025ab60
0025A454  4C 8B 4C CD 28                  mov r9, qword ptr [rbp + rcx*8 + 0x28]
0025A459  4C 89 4C 24 40                  mov qword ptr [rsp + 0x40], r9
0025A45E  48 8B D7                        mov rdx, rdi
0025A461  48 8B 05 90 C7 D6 00            mov rax, qword ptr [rip + 0xd6c790]
0025A468  48 39 86 38 02 00 00            cmp qword ptr [rsi + 0x238], rax
0025A46F  0F 85 8E 08 00 00               jne 0x14025ad03
0025A475  48 85 D2                        test rdx, rdx
0025A478  0F 84 B6 02 00 00               je 0x14025a734
0025A47E  8B 4E 78                        mov ecx, dword ptr [rsi + 0x78]
0025A481  D1 E9                           shr ecx, 1
0025A483  83 E1 01                        and ecx, 1
0025A486  41 3B 4E 08                     cmp ecx, dword ptr [r14 + 8]
0025A48A  0F 8F 7D FD FF FF               jg 0x14025a20d
0025A490  41 8B 46 04                     mov eax, dword ptr [r14 + 4]
0025A494  3B C8                           cmp ecx, eax
0025A496  0F 4C C8                        cmovl ecx, eax
0025A499  85 C9                           test ecx, ecx
0025A49B  0F 85 DC 0D 00 00               jne 0x14025b27d
0025A4A1  44 8B E7                        mov r12d, edi
0025A4A4  41 0F B6 06                     movzx eax, byte ptr [r14]
0025A4A8  44 3B E0                        cmp r12d, eax
0025A4AB  0F 83 5C FD FF FF               jae 0x14025a20d
0025A4B1  39 3D 29 AE D6 00               cmp dword ptr [rip + 0xd6ae29], edi
0025A4B7  41 8B C4                        mov eax, r12d
0025A4BA  48 8D 0C 80                     lea rcx, [rax + rax*4]
0025A4BE  49 8B 44 CE 10                  mov rax, qword ptr [r14 + rcx*8 + 0x10]
0025A4C3  4D 8D 2C CE                     lea r13, [r14 + rcx*8]
0025A4C7  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
0025A4CC  74 0A                           je 0x14025a4d8
0025A4CE  F6 40 23 20                     test byte ptr [rax + 0x23], 0x20
0025A4D2  0F 85 ED 07 00 00               jne 0x14025acc5
0025A4D8  4D 85 C9                        test r9, r9
0025A4DB  0F 84 FE 07 00 00               je 0x14025acdf
0025A4E1  49 8B 4D 18                     mov rcx, qword ptr [r13 + 0x18]
0025A4E5  48 85 C9                        test rcx, rcx
0025A4E8  0F 84 D5 00 00 00               je 0x14025a5c3
0025A4EE  49 3B C9                        cmp rcx, r9
0025A4F1  0F 85 CC 00 00 00               jne 0x14025a5c3
0025A4F7  48 8B 98 C0 00 00 00            mov rbx, qword ptr [rax + 0xc0]
0025A4FE  48 8B CE                        mov rcx, rsi
0025A501  E8 0A DB FF FF                  call 0x140258010
0025A506  44 8B 46 50                     mov r8d, dword ptr [rsi + 0x50]
0025A50A  8B D7                           mov edx, edi
0025A50C  8B 4E 54                        mov ecx, dword ptr [rsi + 0x54]
0025A50F  44 3B C1                        cmp r8d, ecx
0025A512  44 0F 46 C1                     cmovbe r8d, ecx
0025A516  0F B6 8E 05 02 00 00            movzx ecx, byte ptr [rsi + 0x205]
0025A51D  44 3B 05 58 AE D6 00            cmp r8d, dword ptr [rip + 0xd6ae58]
0025A524  0F 93 C2                        setae dl
0025A527  44 8D 04 42                     lea r8d, [rdx + rax*2]
0025A52B  0F B6 83 B9 00 00 00            movzx eax, byte ptr [rbx + 0xb9]
0025A532  44 0F AF C0                     imul r8d, eax
0025A536  48 8B 83 C0 00 00 00            mov rax, qword ptr [rbx + 0xc0]
0025A53D  44 03 C1                        add r8d, ecx
0025A540  4B 8D 0C 40                     lea rcx, [r8 + r8*2]
0025A544  4C 8B 4C C8 10                  mov r9, qword ptr [rax + rcx*8 + 0x10]
0025A549  4C 8B 44 C8 08                  mov r8, qword ptr [rax + rcx*8 + 8]
0025A54E  48 8B 14 C8                     mov rdx, qword ptr [rax + rcx*8]
0025A552  4D 23 C1                        and r8, r9
0025A555  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
0025A55A  49 23 D0                        and rdx, r8
0025A55D  48 89 55 A8                     mov qword ptr [rbp - 0x58], rdx
0025A561  48 8B 53 50                     mov rdx, qword ptr [rbx + 0x50]
0025A565  4C 89 45 B0                     mov qword ptr [rbp - 0x50], r8
0025A569  0F 10 45 A8                     movups xmm0, xmmword ptr [rbp - 0x58]
0025A56D  4C 89 4D B8                     mov qword ptr [rbp - 0x48], r9
0025A571  F2 0F 10 4D B8                  movsd xmm1, qword ptr [rbp - 0x48]
0025A576  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
0025A57A  F2 0F 11 4D E0                  movsd qword ptr [rbp - 0x20], xmm1
0025A57F  4C 85 89 C8 00 00 00            test qword ptr [rcx + 0xc8], r9
0025A586  0F 84 23 08 00 00               je 0x14025adaf
0025A58C  48 3B 4C 24 58                  cmp rcx, qword ptr [rsp + 0x58]
0025A591  0F 85 D1 05 00 00               jne 0x14025ab68
0025A597  40 38 3D 1E C5 D6 00            cmp byte ptr [rip + 0xd6c51e], dil
0025A59E  48 89 7D C0                     mov qword ptr [rbp - 0x40], rdi
0025A5A2  0F 84 34 09 00 00               je 0x14025aedc
0025A5A8  4C 8D 4D C0                     lea r9, [rbp - 0x40]
0025A5AC  45 33 C0                        xor r8d, r8d
0025A5AF  48 8B D6                        mov rdx, rsi
0025A5B2  49 8D 4D 10                     lea rcx, [r13 + 0x10]
0025A5B6  E8 B5 DC FF FF                  call 0x140258270
0025A5BB  84 C0                           test al, al
0025A5BD  0F 85 B5 03 00 00               jne 0x14025a978
0025A5C3  4C 8B 4C 24 40                  mov r9, qword ptr [rsp + 0x40]
0025A5C8  41 FF C4                        inc r12d
0025A5CB  48 8B 5C 24 58                  mov rbx, qword ptr [rsp + 0x58]
0025A5D0  E9 CF FE FF FF                  jmp 0x14025a4a4
0025A5D5  49 83 F8 01                     cmp r8, 1
0025A5D9  0F 84 BA FD FF FF               je 0x14025a399
0025A5DF  48 83 C8 01                     or rax, 1
0025A5E3  49 33 C0                        xor rax, r8
0025A5E6  E9 A5 FD FF FF                  jmp 0x14025a390
0025A5EB  89 7D 80                        mov dword ptr [rbp - 0x80], edi
0025A5EE  F0 48 0F BA 2B 00               lock bts qword ptr [rbx], 0
0025A5F4  0F 83 37 F9 FF FF               jae 0x140259f31
0025A5FA  E9 7B E7 47 00                  jmp 0x1406d8d7a
0025A5FF  83 F9 02                        cmp ecx, 2
0025A602  0F 85 EC FD FF FF               jne 0x14025a3f4
0025A608  8B C7                           mov eax, edi
0025A60A  89 45 F4                        mov dword ptr [rbp - 0xc], eax
0025A60D  45 85 C0                        test r8d, r8d
0025A610  0F 85 F4 01 00 00               jne 0x14025a80a
0025A616  83 E0 01                        and eax, 1
0025A619  89 45 F4                        mov dword ptr [rbp - 0xc], eax
0025A61C  0F 84 D2 FD FF FF               je 0x14025a3f4
0025A622  44 0F BD C8                     bsr r9d, eax
0025A626  44 88 55 FA                     mov byte ptr [rbp - 6], r10b
0025A62A  41 BB 01 00 00 00               mov r11d, 1
0025A630  44 88 4D F8                     mov byte ptr [rbp - 8], r9b
0025A634  41 0F B6 C2                     movzx eax, r10b
0025A638  44 89 4D 84                     mov dword ptr [rbp - 0x7c], r9d
0025A63C  48 8D 0C 40                     lea rcx, [rax + rax*2]
0025A640  48 03 C9                        add rcx, rcx
0025A643  8B 54 CD 48                     mov edx, dword ptr [rbp + rcx*8 + 0x48]
0025A647  0B 54 CD 4C                     or edx, dword ptr [rbp + rcx*8 + 0x4c]
0025A64B  41 0F B6 C9                     movzx ecx, r9b
0025A64F  41 D3 E3                        shl r11d, cl
0025A652  44 85 DA                        test edx, r11d
0025A655  75 2F                           jne 0x14025a686
0025A657  41 FE C2                        inc r10b
0025A65A  41 0F B6 C2                     movzx eax, r10b
0025A65E  44 88 55 FA                     mov byte ptr [rbp - 6], r10b
0025A662  41 3B C0                        cmp eax, r8d
0025A665  72 07                           jb 0x14025a66e
0025A667  45 32 D2                        xor r10b, r10b
0025A66A  44 88 55 FA                     mov byte ptr [rbp - 6], r10b
0025A66E  41 0F B6 C2                     movzx eax, r10b
0025A672  48 8D 0C 40                     lea rcx, [rax + rax*2]
0025A676  48 03 C9                        add rcx, rcx
0025A679  8B 54 CD 48                     mov edx, dword ptr [rbp + rcx*8 + 0x48]
0025A67D  0B 54 CD 4C                     or edx, dword ptr [rbp + rcx*8 + 0x4c]
0025A681  41 85 D3                        test r11d, edx
0025A684  74 D1                           je 0x14025a657
0025A686  41 0F B6 C2                     movzx eax, r10b
0025A68A  4C 8D 45 20                     lea r8, [rbp + 0x20]
0025A68E  32 D2                           xor dl, dl
0025A690  48 8D 0C 40                     lea rcx, [rax + rax*2]
0025A694  48 C1 E1 04                     shl rcx, 4
0025A698  4C 03 C1                        add r8, rcx
0025A69B  41 0F B6 C9                     movzx ecx, r9b
0025A69F  4D 8B 10                        mov r10, qword ptr [r8]
0025A6A2  4D 8B 58 08                     mov r11, qword ptr [r8 + 8]
0025A6A6  88 55 FB                        mov byte ptr [rbp - 5], dl
0025A6A9  41 8B 40 28                     mov eax, dword ptr [r8 + 0x28]
0025A6AD  0F A3 C8                        bt eax, ecx
0025A6B0  73 05                           jae 0x14025a6b7
0025A6B2  B2 01                           mov dl, 1
0025A6B4  88 55 FB                        mov byte ptr [rbp - 5], dl
0025A6B7  41 8B 40 2C                     mov eax, dword ptr [r8 + 0x2c]
0025A6BB  41 0F B6 C9                     movzx ecx, r9b
0025A6BF  0F A3 C8                        bt eax, ecx
0025A6C2  73 06                           jae 0x14025a6ca
0025A6C4  80 CA 02                        or dl, 2
0025A6C7  88 55 FB                        mov byte ptr [rbp - 5], dl
0025A6CA  0F B6 CA                        movzx ecx, dl
0025A6CD  8D 41 FF                        lea eax, [rcx - 1]
0025A6D0  85 C1                           test ecx, eax
0025A6D2  0F 85 D3 07 00 00               jne 0x14025aeab
0025A6D8  0F BC C1                        bsf eax, ecx
0025A6DB  89 45 88                        mov dword ptr [rbp - 0x78], eax
0025A6DE  88 45 FC                        mov byte ptr [rbp - 4], al
0025A6E1  0F B6 C8                        movzx ecx, al
0025A6E4  84 C0                           test al, al
0025A6E6  0F 84 01 06 00 00               je 0x14025aced
0025A6EC  83 F9 01                        cmp ecx, 1
0025A6EF  75 13                           jne 0x14025a704
0025A6F1  41 0F B6 C1                     movzx eax, r9b
0025A6F5  48 83 C0 04                     add rax, 4
0025A6F9  48 C1 E0 04                     shl rax, 4
0025A6FD  49 03 C3                        add rax, r11
0025A700  48 89 45 10                     mov qword ptr [rbp + 0x10], rax
0025A704  48 8B 45 10                     mov rax, qword ptr [rbp + 0x10]
0025A708  48 89 45 18                     mov qword ptr [rbp + 0x18], rax
0025A70C  E9 F0 FC FF FF                  jmp 0x14025a401
0025A711  48 8D 4D 4C                     lea rcx, [rbp + 0x4c]
0025A715  41 8B D0                        mov edx, r8d
0025A718  0B 41 FC                        or eax, dword ptr [rcx - 4]
0025A71B  48 8D 49 30                     lea rcx, [rcx + 0x30]
0025A71F  89 45 F4                        mov dword ptr [rbp - 0xc], eax
0025A722  0B 41 D0                        or eax, dword ptr [rcx - 0x30]
0025A725  89 45 F4                        mov dword ptr [rbp - 0xc], eax
0025A728  48 83 EA 01                     sub rdx, 1
0025A72C  0F 84 22 FB FF FF               je 0x14025a254
0025A732  EB E4                           jmp 0x14025a718
0025A734  48 8B 46 68                     mov rax, qword ptr [rsi + 0x68]
0025A738  48 85 C0                        test rax, rax
0025A73B  0F 84 3D FD FF FF               je 0x14025a47e
0025A741  8B 8B D8 00 00 00               mov ecx, dword ptr [rbx + 0xd8]
0025A747  48 03 C8                        add rcx, rax
0025A74A  0F 84 2E FD FF FF               je 0x14025a47e
0025A750  80 BE C3 00 00 00 10            cmp byte ptr [rsi + 0xc3], 0x10
0025A757  44 8B C7                        mov r8d, edi
0025A75A  0F 8D 1E FD FF FF               jge 0x14025a47e
0025A760  F7 46 78 00 02 00 00            test dword ptr [rsi + 0x78], 0x200
0025A767  0F 85 11 FD FF FF               jne 0x14025a47e
0025A76D  39 BE E4 01 00 00               cmp dword ptr [rsi + 0x1e4], edi
0025A773  0F 85 05 FD FF FF               jne 0x14025a47e
0025A779  80 BE 86 01 00 00 01            cmp byte ptr [rsi + 0x186], 1
0025A780  0F 84 F8 FC FF FF               je 0x14025a47e
0025A786  48 8B D1                        mov rdx, rcx
0025A789  4C 8B E1                        mov r12, rcx
0025A78C  0F 1F 40 00                     nop dword ptr [rax]
0025A790  F6 42 70 02                     test byte ptr [rdx + 0x70], 2
0025A794  75 27                           jne 0x14025a7bd
0025A796  48 8B 92 A0 01 00 00            mov rdx, qword ptr [rdx + 0x1a0]
0025A79D  48 85 D2                        test rdx, rdx
0025A7A0  75 EE                           jne 0x14025a790
0025A7A2  44 03 41 7C                     add r8d, dword ptr [rcx + 0x7c]
0025A7A6  75 0C                           jne 0x14025a7b4
0025A7A8  48 8B 89 A0 01 00 00            mov rcx, qword ptr [rcx + 0x1a0]
0025A7AF  48 85 C9                        test rcx, rcx
0025A7B2  75 EE                           jne 0x14025a7a2
0025A7B4  45 85 C0                        test r8d, r8d
0025A7B7  0F 84 C1 FC FF FF               je 0x14025a47e
0025A7BD  48 8B D6                        mov rdx, rsi
0025A7C0  48 8D 4D F0                     lea rcx, [rbp - 0x10]
0025A7C4  E8 C7 6F FA FF                  call 0x140201790
0025A7C9  8B 43 24                        mov eax, dword ptr [rbx + 0x24]
0025A7CC  45 33 C9                        xor r9d, r9d
0025A7CF  4C 8B C6                        mov r8, rsi
0025A7D2  89 86 18 02 00 00               mov dword ptr [rsi + 0x218], eax
0025A7D8  49 8B D4                        mov rdx, r12
0025A7DB  48 8B CB                        mov rcx, rbx
0025A7DE  E8 F9 68 FA FF                  call 0x1402010dc
0025A7E3  F7 05 27 C3 D6 00 00 08 00 00   test dword ptr [rip + 0xd6c327], 0x800
0025A7ED  0F 84 1A FA FF FF               je 0x14025a20d
0025A7F3  8B 53 24                        mov edx, dword ptr [rbx + 0x24]
0025A7F6  45 33 C9                        xor r9d, r9d
0025A7F9  48 8B CE                        mov rcx, rsi
0025A7FC  45 8D 41 02                     lea r8d, [r9 + 2]
0025A800  E8 3F 8C FC FF                  call 0x140223444
0025A805  E9 03 FA FF FF                  jmp 0x14025a20d
0025A80A  48 8D 4D 4C                     lea rcx, [rbp + 0x4c]
0025A80E  41 8B D0                        mov edx, r8d
0025A811  0B 41 FC                        or eax, dword ptr [rcx - 4]
0025A814  48 8D 49 30                     lea rcx, [rcx + 0x30]
0025A818  89 45 F4                        mov dword ptr [rbp - 0xc], eax
0025A81B  0B 41 D0                        or eax, dword ptr [rcx - 0x30]
0025A81E  89 45 F4                        mov dword ptr [rbp - 0xc], eax
0025A821  48 83 EA 01                     sub rdx, 1
0025A825  0F 84 EB FD FF FF               je 0x14025a616
0025A82B  EB E4                           jmp 0x14025a811
0025A82D  E8 7E D6 FF FF                  call 0x140257eb0
0025A832  FF C6                           inc esi
0025A834  4C 8B C3                        mov r8, rbx
0025A837  E9 84 F6 FF FF                  jmp 0x140259ec0
0025A83C  48 8D 4D F0                     lea rcx, [rbp - 0x10]
0025A840  E8 0B 74 FA FF                  call 0x140201c50
0025A845  85 C0                           test eax, eax
0025A847  0F 89 C2 FB FF FF               jns 0x14025a40f
0025A84D  4C 8B C7                        mov r8, rdi
0025A850  44 8B E7                        mov r12d, edi
0025A853  41 0F B6 06                     movzx eax, byte ptr [r14]
0025A857  48 8B DF                        mov rbx, rdi
0025A85A  84 C0                           test al, al
0025A85C  74 2E                           je 0x14025a88c
0025A85E  49 8D 4E 18                     lea rcx, [r14 + 0x18]
0025A862  8B D0                           mov edx, eax
0025A864  48 8B 01                        mov rax, qword ptr [rcx]
0025A867  49 3B C0                        cmp rax, r8
0025A86A  76 0D                           jbe 0x14025a879
0025A86C  48 85 DB                        test rbx, rbx
0025A86F  74 05                           je 0x14025a876
0025A871  48 3B C3                        cmp rax, rbx
0025A874  73 03                           jae 0x14025a879
0025A876  48 8B D8                        mov rbx, rax
0025A879  48 83 C1 28                     add rcx, 0x28
0025A87D  48 83 EA 01                     sub rdx, 1
0025A881  75 E1                           jne 0x14025a864
0025A883  48 85 DB                        test rbx, rbx
0025A886  0F 85 B7 05 00 00               jne 0x14025ae43
0025A88C  4C 8B 6C 24 38                  mov r13, qword ptr [rsp + 0x38]
0025A891  45 32 E4                        xor r12b, r12b
0025A894  8B F7                           mov esi, edi
0025A896  F7 05 74 C2 D6 00 00 04 00 00   test dword ptr [rip + 0xd6c274], 0x400
0025A8A0  B8 02 00 00 00                  mov eax, 2
0025A8A5  8B DF                           mov ebx, edi
0025A8A7  0F 45 F0                        cmovne esi, eax
0025A8AA  41 38 3E                        cmp byte ptr [r14], dil
0025A8AD  76 33                           jbe 0x14025a8e2
0025A8AF  48 8B 7C 24 50                  mov rdi, qword ptr [rsp + 0x50]
0025A8B4  8B C3                           mov eax, ebx
0025A8B6  4C 8B CF                        mov r9, rdi
0025A8B9  44 8B C6                        mov r8d, esi
0025A8BC  49 8B D7                        mov rdx, r15
0025A8BF  48 8D 0C 85 02 00 00 00         lea rcx, [rax*4 + 2]
0025A8C7  48 03 C8                        add rcx, rax
0025A8CA  49 8D 0C CE                     lea rcx, [r14 + rcx*8]
0025A8CE  E8 FD 26 0B 00                  call 0x14030cfd0
0025A8D3  44 0A E0                        or r12b, al
0025A8D6  FF C3                           inc ebx
0025A8D8  41 0F B6 06                     movzx eax, byte ptr [r14]
0025A8DC  3B D8                           cmp ebx, eax
0025A8DE  72 D4                           jb 0x14025a8b4
0025A8E0  33 FF                           xor edi, edi
0025A8E2  41 83 7E 08 01                  cmp dword ptr [r14 + 8], 1
0025A8E7  75 1C                           jne 0x14025a905
0025A8E9  49 8B 46 10                     mov rax, qword ptr [r14 + 0x10]
0025A8ED  48 8B 88 58 8E 00 00            mov rcx, qword ptr [rax + 0x8e58]
0025A8F4  0F B6 41 01                     movzx eax, byte ptr [rcx + 1]
0025A8F8  FE C0                           inc al
0025A8FA  88 41 01                        mov byte ptr [rcx + 1], al
0025A8FD  3A 01                           cmp al, byte ptr [rcx]
0025A8FF  72 04                           jb 0x14025a905
0025A901  C6 41 01 00                     mov byte ptr [rcx + 1], 0
0025A905  4C 8B 54 24 78                  mov r10, qword ptr [rsp + 0x78]
0025A90A  4C 8B C7                        mov r8, rdi
0025A90D  8B D7                           mov edx, edi
0025A90F  49 8B 0A                        mov rcx, qword ptr [r10]
0025A912  4C 8B C9                        mov r9, rcx
0025A915  49 83 E1 FE                     and r9, 0xfffffffffffffffe
0025A919  4C 89 4C 24 78                  mov qword ptr [rsp + 0x78], r9
0025A91E  83 E1 01                        and ecx, 1
0025A921  0F 84 0D 05 00 00               je 0x14025ae34
0025A927  83 F9 01                        cmp ecx, 1
0025A92A  75 15                           jne 0x14025a941
0025A92C  49 8B 81 58 8E 00 00            mov rax, qword ptr [r9 + 0x8e58]
0025A933  4D 8B 81 58 8E 00 00            mov r8, qword ptr [r9 + 0x8e58]
0025A93A  49 83 C0 08                     add r8, 8
0025A93E  0F B6 10                        movzx edx, byte ptr [rax]
0025A941  85 D2                           test edx, edx
0025A943  0F 84 AF F6 FF FF               je 0x140259ff8
0025A949  0F 1F 80 00 00 00 00            nop dword ptr [rax]
0025A950  8D 42 FF                        lea eax, [rdx - 1]
0025A953  49 8B 0C C0                     mov rcx, qword ptr [r8 + rax*8]
0025A957  8B D0                           mov edx, eax
0025A959  F0 48 83 61 30 00               lock and qword ptr [rcx + 0x30], 0
0025A95F  85 C0                           test eax, eax
0025A961  75 ED                           jne 0x14025a950
0025A963  E9 90 F6 FF FF                  jmp 0x140259ff8
0025A968  A8 10                           test al, 0x10
0025A96A  0F 84 53 FC FF FF               je 0x14025a5c3
0025A970  84 C9                           test cl, cl
0025A972  0F 84 4B FC FF FF               je 0x14025a5c3
0025A978  4D 8B 65 10                     mov r12, qword ptr [r13 + 0x10]
0025A97C  4D 85 E4                        test r12, r12
0025A97F  0F 84 88 F8 FF FF               je 0x14025a20d
0025A985  0F B6 45 FA                     movzx eax, byte ptr [rbp - 6]
0025A989  48 8D 96 D8 00 00 00            lea rdx, [rsi + 0xd8]
0025A990  44 0F B6 6D F8                  movzx r13d, byte ptr [rbp - 8]
0025A995  48 8D 0C 40                     lea rcx, [rax + rax*2]
0025A999  48 03 C9                        add rcx, rcx
0025A99C  80 7D FD 02                     cmp byte ptr [rbp - 3], 2
0025A9A0  48 8B 5C CD 20                  mov rbx, qword ptr [rbp + rcx*8 + 0x20]
0025A9A5  0F 84 35 04 00 00               je 0x14025ade0
0025A9AB  48 8B 45 18                     mov rax, qword ptr [rbp + 0x18]
0025A9AF  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
0025A9B3  48 89 4D 18                     mov qword ptr [rbp + 0x18], rcx
0025A9B7  0F B6 4D FC                     movzx ecx, byte ptr [rbp - 4]
0025A9BB  85 C9                           test ecx, ecx
0025A9BD  0F 84 F0 01 00 00               je 0x14025abb3
0025A9C3  83 F9 01                        cmp ecx, 1
0025A9C6  0F 85 67 00 00 00               jne 0x14025aa33
0025A9CC  0F B6 4D FB                     movzx ecx, byte ptr [rbp - 5]
0025A9D0  8D 41 FF                        lea eax, [rcx - 1]
0025A9D3  85 C1                           test ecx, eax
0025A9D5  74 08                           je 0x14025a9df
0025A9D7  44 0F AB AB DC 83 00 00         bts dword ptr [rbx + 0x83dc], r13d
0025A9DF  F7 46 78 00 00 40 00            test dword ptr [rsi + 0x78], 0x400000
0025A9E6  4C 8B 8B 48 8E 00 00            mov r9, qword ptr [rbx + 0x8e48]
0025A9ED  0F 85 20 05 00 00               jne 0x14025af13
0025A9F3  48 8B 0A                        mov rcx, qword ptr [rdx]
0025A9F6  48 8B 42 08                     mov rax, qword ptr [rdx + 8]
0025A9FA  48 39 51 08                     cmp qword ptr [rcx + 8], rdx
0025A9FE  75 09                           jne 0x14025aa09
0025AA00  48 39 10                        cmp qword ptr [rax], rdx
0025AA03  0F 84 33 01 00 00               je 0x14025ab3c
0025AA09  B9 03 00 00 00                  mov ecx, 3
0025AA0E  CD 29                           int 0x29
0025AA10  41 83 41 0C FF                  add dword ptr [r9 + 0xc], -1
0025AA15  0F 84 03 01 00 00               je 0x14025ab1e
0025AA1B  8B 86 F8 06 00 00               mov eax, dword ptr [rsi + 0x6f8]
0025AA21  48 8B D6                        mov rdx, rsi
0025AA24  49 29 41 10                     sub qword ptr [r9 + 0x10], rax
0025AA28  49 8B C9                        mov rcx, r9
0025AA2B  45 33 C0                        xor r8d, r8d
0025AA2E  E8 1D 70 FA FF                  call 0x140201a50
0025AA33  45 0F B6 06                     movzx r8d, byte ptr [r14]
0025AA37  4C 8B CF                        mov r9, rdi
0025AA3A  8B D7                           mov edx, edi
0025AA3C  0F 1F 40 00                     nop dword ptr [rax]
0025AA40  41 3B D0                        cmp edx, r8d
0025AA43  73 19                           jae 0x14025aa5e
0025AA45  8B C2                           mov eax, edx
0025AA47  48 8D 0C 80                     lea rcx, [rax + rax*4]
0025AA4B  4D 39 64 CE 10                  cmp qword ptr [r14 + rcx*8 + 0x10], r12
0025AA50  49 8D 04 CE                     lea rax, [r14 + rcx*8]
0025AA54  74 04                           je 0x14025aa5a
0025AA56  FF C2                           inc edx
0025AA58  EB E6                           jmp 0x14025aa40
0025AA5A  4C 8D 48 10                     lea r9, [rax + 0x10]
0025AA5E  44 8B 56 78                     mov r10d, dword ptr [rsi + 0x78]
0025AA62  41 0F B6 41 20                  movzx eax, byte ptr [r9 + 0x20]
0025AA67  41 D1 EA                        shr r10d, 1
0025AA6A  D1 E8                           shr eax, 1
0025AA6C  41 83 E2 01                     and r10d, 1
0025AA70  83 E0 01                        and eax, 1
0025AA73  44 3B D0                        cmp r10d, eax
0025AA76  0F 83 F9 04 00 00               jae 0x14025af75
0025AA7C  8B DF                           mov ebx, edi
0025AA7E  41 38 3E                        cmp byte ptr [r14], dil
0025AA81  0F 86 4B 05 00 00               jbe 0x14025afd2
0025AA87  4C 8B 7C 24 50                  mov r15, qword ptr [rsp + 0x50]
0025AA8C  8B C3                           mov eax, ebx
0025AA8E  48 8D 0C 80                     lea rcx, [rax + rax*4]
0025AA92  4D 8B 6C CE 10                  mov r13, qword ptr [r14 + rcx*8 + 0x10]
0025AA97  4D 8D 0C CE                     lea r9, [r14 + rcx*8]
0025AA9B  49 8B 4C CE 28                  mov rcx, qword ptr [r14 + rcx*8 + 0x28]
0025AAA0  48 8D 41 FF                     lea rax, [rcx - 1]
0025AAA4  4D 3B EC                        cmp r13, r12
0025AAA7  0F 84 73 06 00 00               je 0x14025b120
0025AAAD  4D 8B 5D 18                     mov r11, qword ptr [r13 + 0x18]
0025AAB1  48 83 F8 FC                     cmp rax, -4
0025AAB5  0F 86 61 08 00 00               jbe 0x14025b31c
0025AABB  41 0F B6 41 30                  movzx eax, byte ptr [r9 + 0x30]
0025AAC0  0C 01                           or al, 1
0025AAC2  4D 89 59 20                     mov qword ptr [r9 + 0x20], r11
0025AAC6  41 88 41 30                     mov byte ptr [r9 + 0x30], al
0025AACA  24 FD                           and al, 0xfd
0025AACC  41 8B 4B 78                     mov ecx, dword ptr [r11 + 0x78]
0025AAD0  D1 E9                           shr ecx, 1
0025AAD2  80 E1 01                        and cl, 1
0025AAD5  02 C9                           add cl, cl
0025AAD7  32 C8                           xor cl, al
0025AAD9  80 E1 E7                        and cl, 0xe7
0025AADC  80 C9 04                        or cl, 4
0025AADF  80 E1 DF                        and cl, 0xdf
0025AAE2  41 88 49 30                     mov byte ptr [r9 + 0x30], cl
0025AAE6  49 8B CB                        mov rcx, r11
0025AAE9  41 80 61 31 FE                  and byte ptr [r9 + 0x31], 0xfe
0025AAEE  4D 89 59 28                     mov qword ptr [r9 + 0x28], r11
0025AAF2  E8 39 87 0F 00                  call 0x140353230
0025AAF7  84 C0                           test al, al
0025AAF9  75 0B                           jne 0x14025ab06
0025AAFB  41 8B 45 24                     mov eax, dword ptr [r13 + 0x24]
0025AAFF  41 89 83 18 02 00 00            mov dword ptr [r11 + 0x218], eax
0025AB06  41 0F B6 06                     movzx eax, byte ptr [r14]
0025AB0A  FF C3                           inc ebx
0025AB0C  3B D8                           cmp ebx, eax
0025AB0E  0F 82 78 FF FF FF               jb 0x14025aa8c
0025AB14  4C 8B 7C 24 60                  mov r15, qword ptr [rsp + 0x60]
0025AB19  E9 B4 04 00 00                  jmp 0x14025afd2
0025AB1E  49 8B 91 C8 02 00 00            mov rdx, qword ptr [r9 + 0x2c8]
0025AB25  49 8B 81 D0 02 00 00            mov rax, qword ptr [r9 + 0x2d0]
0025AB2C  48 F7 D2                        not rdx
0025AB2F  F0 48 21 90 88 01 00 00         lock and qword ptr [rax + 0x188], rdx
0025AB37  E9 DF FE FF FF                  jmp 0x14025aa1b
0025AB3C  48 89 08                        mov qword ptr [rax], rcx
0025AB3F  48 89 41 08                     mov qword ptr [rcx + 8], rax
0025AB43  48 3B C1                        cmp rax, rcx
0025AB46  0F 85 C4 FE FF FF               jne 0x14025aa10
0025AB4C  41 8B 49 08                     mov ecx, dword ptr [r9 + 8]
0025AB50  41 0F B6 C5                     movzx eax, r13b
0025AB54  0F BB C1                        btc ecx, eax
0025AB57  41 89 49 08                     mov dword ptr [r9 + 8], ecx
0025AB5B  E9 B0 FE FF FF                  jmp 0x14025aa10
0025AB60  4C 8B CF                        mov r9, rdi
0025AB63  E9 F1 F8 FF FF                  jmp 0x14025a459
0025AB68  48 8B 46 68                     mov rax, qword ptr [rsi + 0x68]
0025AB6C  48 85 C0                        test rax, rax
0025AB6F  0F 84 22 FA FF FF               je 0x14025a597
0025AB75  8B 91 D8 00 00 00               mov edx, dword ptr [rcx + 0xd8]
0025AB7B  48 8B CE                        mov rcx, rsi
0025AB7E  48 03 D0                        add rdx, rax
0025AB81  E8 7A 06 0B 00                  call 0x14030b200
0025AB86  84 C0                           test al, al
0025AB88  0F 84 09 FA FF FF               je 0x14025a597
0025AB8E  48 8B CA                        mov rcx, rdx
0025AB91  E8 0A 7C FA FF                  call 0x1402027a0
0025AB96  84 C0                           test al, al
0025AB98  0F 84 F9 F9 FF FF               je 0x14025a597
0025AB9E  48 8B CE                        mov rcx, rsi
0025ABA1  E8 6A B7 0F 00                  call 0x140356310
0025ABA6  84 C0                           test al, al
0025ABA8  0F 85 E9 F9 FF FF               jne 0x14025a597
0025ABAE  E9 10 FA FF FF                  jmp 0x14025a5c3
0025ABB3  0F B6 4D FB                     movzx ecx, byte ptr [rbp - 5]
0025ABB7  8D 41 FF                        lea eax, [rcx - 1]
0025ABBA  85 C1                           test ecx, eax
0025ABBC  74 08                           je 0x14025abc6
0025ABBE  44 0F B3 AB DC 83 00 00         btr dword ptr [rbx + 0x83dc], r13d
0025ABC6  F7 42 A0 00 00 40 00            test dword ptr [rdx - 0x60], 0x400000
0025ABCD  0F 85 35 05 00 00               jne 0x14025b108
0025ABD3  48 8B 0A                        mov rcx, qword ptr [rdx]
0025ABD6  48 8B 42 08                     mov rax, qword ptr [rdx + 8]
0025ABDA  48 39 51 08                     cmp qword ptr [rcx + 8], rdx
0025ABDE  0F 85 25 FE FF FF               jne 0x14025aa09
0025ABE4  48 39 10                        cmp qword ptr [rax], rdx
0025ABE7  0F 85 1C FE FF FF               jne 0x14025aa09
0025ABED  48 89 08                        mov qword ptr [rax], rcx
0025ABF0  48 89 41 08                     mov qword ptr [rcx + 8], rax
0025ABF4  48 3B C1                        cmp rax, rcx
0025ABF7  0F 84 3F 01 00 00               je 0x14025ad3c
0025ABFD  83 83 74 86 00 00 FF            add dword ptr [rbx + 0x8674], -1
0025AC04  0F 84 5B 01 00 00               je 0x14025ad65
0025AC0A  8B 82 20 06 00 00               mov eax, dword ptr [rdx + 0x620]
0025AC10  48 29 83 78 86 00 00            sub qword ptr [rbx + 0x8678], rax
0025AC17  48 8B 8B 48 8E 00 00            mov rcx, qword ptr [rbx + 0x8e48]
0025AC1E  48 81 C2 28 FF FF FF            add rdx, -0xd8
0025AC25  E9 01 FE FF FF                  jmp 0x14025aa2b
0025AC2A  41 0F B6 C1                     movzx eax, r9b
0025AC2E  48 05 44 08 00 00               add rax, 0x844
0025AC34  48 C1 E0 04                     shl rax, 4
0025AC38  49 03 C3                        add rax, r11
0025AC3B  E9 FE F6 FF FF                  jmp 0x14025a33e
0025AC40  48 83 C0 A8                     add rax, -0x58
0025AC44  44 39 48 7C                     cmp dword ptr [rax + 0x7c], r9d
0025AC48  0F 87 4B F7 FF FF               ja 0x14025a399
0025AC4E  E9 49 F7 FF FF                  jmp 0x14025a39c
0025AC53  4D 85 DB                        test r11, r11
0025AC56  0F 85 C5 01 00 00               jne 0x14025ae21
0025AC5C  0F B6 DA                        movzx ebx, dl
0025AC5F  4D 8B D9                        mov r11, r9
0025AC62  E9 71 F7 FF FF                  jmp 0x14025a3d8
0025AC67  41 0F B7 4B 78                  movzx ecx, word ptr [r11 + 0x78]
0025AC6C  0F B6 C3                        movzx eax, bl
0025AC6F  88 5D FA                        mov byte ptr [rbp - 6], bl
0025AC72  4C 89 5D 08                     mov qword ptr [rbp + 8], r11
0025AC76  4C 89 5D 00                     mov qword ptr [rbp], r11
0025AC7A  48 8D 14 40                     lea rdx, [rax + rax*2]
0025AC7E  89 4D F4                        mov dword ptr [rbp - 0xc], ecx
0025AC81  48 03 D2                        add rdx, rdx
0025AC84  8B 44 D5 40                     mov eax, dword ptr [rbp + rdx*8 + 0x40]
0025AC88  41 39 43 7C                     cmp dword ptr [r11 + 0x7c], eax
0025AC8C  75 0B                           jne 0x14025ac99
0025AC8E  8B 44 D5 44                     mov eax, dword ptr [rbp + rdx*8 + 0x44]
0025AC92  23 C1                           and eax, ecx
0025AC94  8B C8                           mov ecx, eax
0025AC96  89 45 F4                        mov dword ptr [rbp - 0xc], eax
0025AC99  85 C9                           test ecx, ecx
0025AC9B  0F 84 EF 00 00 00               je 0x14025ad90
0025ACA1  0F BD C1                        bsr eax, ecx
0025ACA4  0F B6 C8                        movzx ecx, al
0025ACA7  48 83 C1 09                     add rcx, 9
0025ACAB  89 45 98                        mov dword ptr [rbp - 0x68], eax
0025ACAE  48 C1 E1 04                     shl rcx, 4
0025ACB2  49 03 CB                        add rcx, r11
0025ACB5  88 45 F8                        mov byte ptr [rbp - 8], al
0025ACB8  48 89 4D 10                     mov qword ptr [rbp + 0x10], rcx
0025ACBC  48 89 4D 18                     mov qword ptr [rbp + 0x18], rcx
0025ACC0  E9 3C F7 FF FF                  jmp 0x14025a401
0025ACC5  48 8B CE                        mov rcx, rsi
0025ACC8  E8 B3 CE 27 00                  call 0x1404d7b80
0025ACCD  84 C0                           test al, al
0025ACCF  0F 84 EE F8 FF FF               je 0x14025a5c3
0025ACD5  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
0025ACDA  E9 F9 F7 FF FF                  jmp 0x14025a4d8
0025ACDF  48 3B C3                        cmp rax, rbx
0025ACE2  0F 85 F9 F7 FF FF               jne 0x14025a4e1
0025ACE8  E9 AA F8 FF FF                  jmp 0x14025a597
0025ACED  41 0F B6 C1                     movzx eax, r9b
0025ACF1  48 05 44 08 00 00               add rax, 0x844
0025ACF7  48 C1 E0 04                     shl rax, 4
0025ACFB  49 03 C2                        add rax, r10
0025ACFE  E9 FD F9 FF FF                  jmp 0x14025a700
0025AD03  8B 46 74                        mov eax, dword ptr [rsi + 0x74]
0025AD06  A8 08                           test al, 8
0025AD08  0F 85 67 F7 FF FF               jne 0x14025a475
0025AD0E  48 8B D6                        mov rdx, rsi
0025AD11  48 8D 4D F0                     lea rcx, [rbp - 0x10]
0025AD15  E8 76 6A FA FF                  call 0x140201790
0025AD1A  48 8B CE                        mov rcx, rsi
0025AD1D  E8 FE C6 13 00                  call 0x140397420
0025AD22  48 8B 54 24 50                  mov rdx, qword ptr [rsp + 0x50]
0025AD27  48 8D 8E D8 00 00 00            lea rcx, [rsi + 0xd8]
0025AD2E  48 8B 02                        mov rax, qword ptr [rdx]
0025AD31  48 89 01                        mov qword ptr [rcx], rax
0025AD34  48 89 0A                        mov qword ptr [rdx], rcx
0025AD37  E9 D1 F4 FF FF                  jmp 0x14025a20d
0025AD3C  8B 8B D8 83 00 00               mov ecx, dword ptr [rbx + 0x83d8]
0025AD42  41 0F B6 C5                     movzx eax, r13b
0025AD46  0F BB C1                        btc ecx, eax
0025AD49  89 8B D8 83 00 00               mov dword ptr [rbx + 0x83d8], ecx
0025AD4F  E9 A9 FE FF FF                  jmp 0x14025abfd
0025AD54  48 8B 55 00                     mov rdx, qword ptr [rbp]
0025AD58  4C 8B CF                        mov r9, rdi
0025AD5B  48 89 7C 24 40                  mov qword ptr [rsp + 0x40], rdi
0025AD60  E9 FC F6 FF FF                  jmp 0x14025a461
0025AD65  48 39 BB 30 84 00 00            cmp qword ptr [rbx + 0x8430], rdi
0025AD6C  0F 85 98 FE FF FF               jne 0x14025ac0a
0025AD72  48 8B 8B C8 00 00 00            mov rcx, qword ptr [rbx + 0xc8]
0025AD79  48 8B 83 C0 00 00 00            mov rax, qword ptr [rbx + 0xc0]
0025AD80  48 F7 D1                        not rcx
0025AD83  F0 48 21 88 80 01 00 00         lock and qword ptr [rax + 0x180], rcx
0025AD8B  E9 7A FE FF FF                  jmp 0x14025ac0a
0025AD90  48 8D 4D F0                     lea rcx, [rbp - 0x10]
0025AD94  E8 E3 74 FA FF                  call 0x14020227c
0025AD99  85 C0                           test eax, eax
0025AD9B  0F 89 1E 01 00 00               jns 0x14025aebf
0025ADA1  44 0F B6 55 F9                  movzx r10d, byte ptr [rbp - 7]
0025ADA6  44 8B 45 F0                     mov r8d, dword ptr [rbp - 0x10]
0025ADAA  E9 45 F6 FF FF                  jmp 0x14025a3f4
0025ADAF  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
0025ADB4  48 8B 80 C8 02 00 00            mov rax, qword ptr [rax + 0x2c8]
0025ADBB  48 23 C2                        and rax, rdx
0025ADBE  49 85 C1                        test r9, rax
0025ADC1  0F 85 FC F7 FF FF               jne 0x14025a5c3
0025ADC7  E9 C0 F7 FF FF                  jmp 0x14025a58c
0025ADCC  41 0F B6 C1                     movzx eax, r9b
0025ADD0  41 0F A3 83 DC 83 00 00         bt dword ptr [r11 + 0x83dc], eax
0025ADD8  0F 93 C0                        setae al
0025ADDB  E9 3C F5 FF FF                  jmp 0x14025a31c
0025ADE0  48 8B 45 00                     mov rax, qword ptr [rbp]
0025ADE4  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
0025ADE9  48 8B 45 10                     mov rax, qword ptr [rbp + 0x10]
0025ADED  48 39 02                        cmp qword ptr [rdx], rax
0025ADF0  0F 85 D5 00 00 00               jne 0x14025aecb
0025ADF6  48 39 42 08                     cmp qword ptr [rdx + 8], rax
0025ADFA  0F 85 CB 00 00 00               jne 0x14025aecb
0025AE00  48 8D 4D F0                     lea rcx, [rbp - 0x10]
0025AE04  E8 47 6E FA FF                  call 0x140201c50
0025AE09  48 8B 54 24 48                  mov rdx, qword ptr [rsp + 0x48]
0025AE0E  45 8B CD                        mov r9d, r13d
0025AE11  4C 8B C6                        mov r8, rsi
0025AE14  48 8B CB                        mov rcx, rbx
0025AE17  E8 48 6D FA FF                  call 0x140201b64
0025AE1C  E9 12 FC FF FF                  jmp 0x14025aa33
0025AE21  41 8B 41 7C                     mov eax, dword ptr [r9 + 0x7c]
0025AE25  41 39 43 7C                     cmp dword ptr [r11 + 0x7c], eax
0025AE29  0F 83 A9 F5 FF FF               jae 0x14025a3d8
0025AE2F  E9 28 FE FF FF                  jmp 0x14025ac5c
0025AE34  4C 8D 44 24 78                  lea r8, [rsp + 0x78]
0025AE39  BA 01 00 00 00                  mov edx, 1
0025AE3E  E9 0D FB FF FF                  jmp 0x14025a950
0025AE43  41 8B F4                        mov esi, r12d
0025AE46  48 83 C6 0B                     add rsi, 0xb
0025AE4A  48 C1 E6 04                     shl rsi, 4
0025AE4E  49 03 F6                        add rsi, r14
0025AE51  F7 05 DD BC D6 00 00 00 20 00   test dword ptr [rip + 0xd6bcdd], 0x200000
0025AE5B  74 48                           je 0x14025aea5
0025AE5D  0F 0D 0E                        prefetchw byte ptr [rsi]
0025AE60  48 8B 06                        mov rax, qword ptr [rsi]
0025AE63  48 85 C0                        test rax, rax
0025AE66  75 16                           jne 0x14025ae7e
0025AE68  48 8B 4E 08                     mov rcx, qword ptr [rsi + 8]
0025AE6C  48 8B C6                        mov rax, rsi
0025AE6F  F0 48 0F B1 39                  lock cmpxchg qword ptr [rcx], rdi
0025AE74  74 24                           je 0x14025ae9a
0025AE76  48 8B CE                        mov rcx, rsi
0025AE79  E8 22 CC FB FF                  call 0x140217aa0
0025AE7E  48 8D 48 08                     lea rcx, [rax + 8]
0025AE82  48 89 3E                        mov qword ptr [rsi], rdi
0025AE85  48 8B 56 08                     mov rdx, qword ptr [rsi + 8]
0025AE89  48 8B C2                        mov rax, rdx
0025AE8C  48 87 01                        xchg qword ptr [rcx], rax
0025AE8F  32 C2                           xor al, dl
0025AE91  A8 04                           test al, 4
0025AE93  74 05                           je 0x14025ae9a
0025AE95  E8 86 CD FB FF                  call 0x140217c20
0025AE9A  41 FF C4                        inc r12d
0025AE9D  4C 8B C3                        mov r8, rbx
0025AEA0  E9 AE F9 FF FF                  jmp 0x14025a853
0025AEA5  F0 48 21 3B                     lock and qword ptr [rbx], rdi
0025AEA9  EB EF                           jmp 0x14025ae9a
0025AEAB  41 0F B6 C1                     movzx eax, r9b
0025AEAF  41 0F A3 82 DC 83 00 00         bt dword ptr [r10 + 0x83dc], eax
0025AEB7  0F 93 C0                        setae al
0025AEBA  E9 1F F8 FF FF                  jmp 0x14025a6de
0025AEBF  4C 8B 5D 00                     mov r11, qword ptr [rbp]
0025AEC3  8B 4D F4                        mov ecx, dword ptr [rbp - 0xc]
0025AEC6  E9 D6 FD FF FF                  jmp 0x14025aca1
0025AECB  48 8B 45 18                     mov rax, qword ptr [rbp + 0x18]
0025AECF  4C 8B 40 08                     mov r8, qword ptr [rax + 8]
0025AED3  4C 89 45 18                     mov qword ptr [rbp + 0x18], r8
0025AED7  E9 2D FF FF FF                  jmp 0x14025ae09
0025AEDC  41 0F B6 45 30                  movzx eax, byte ptr [r13 + 0x30]
0025AEE1  49 8B 55 20                     mov rdx, qword ptr [r13 + 0x20]
0025AEE5  A8 01                           test al, 1
0025AEE7  0F 85 8B FA FF FF               jne 0x14025a978
0025AEED  0F B6 8E C3 00 00 00            movzx ecx, byte ptr [rsi + 0xc3]
0025AEF4  3A 8A C3 00 00 00               cmp cl, byte ptr [rdx + 0xc3]
0025AEFA  0F 8F 78 FA FF FF               jg 0x14025a978
0025AF00  0F 85 62 FA FF FF               jne 0x14025a968
0025AF06  A8 18                           test al, 0x18
0025AF08  0F 85 6A FA FF FF               jne 0x14025a978
0025AF0E  E9 55 FA FF FF                  jmp 0x14025a968
0025AF13  48 8B 86 C8 03 00 00            mov rax, qword ptr [rsi + 0x3c8]
0025AF1A  F0 81 20 FF FF FB FF            lock and dword ptr [rax], 0xfffbffff
0025AF21  44 0F B6 6D F8                  movzx r13d, byte ptr [rbp - 8]
0025AF26  E9 C8 FA FF FF                  jmp 0x14025a9f3
0025AF2B  44 8B EF                        mov r13d, edi
0025AF2E  41 0F B6 06                     movzx eax, byte ptr [r14]
0025AF32  44 3B E8                        cmp r13d, eax
0025AF35  73 34                           jae 0x14025af6b
0025AF37  41 8B C5                        mov eax, r13d
0025AF3A  48 8D 0C 85 02 00 00 00         lea rcx, [rax*4 + 2]
0025AF42  48 03 C8                        add rcx, rax
0025AF45  49 8D 0C CE                     lea rcx, [r14 + rcx*8]
0025AF49  48 3B CB                        cmp rcx, rbx
0025AF4C  74 18                           je 0x14025af66
0025AF4E  48 8B 54 24 38                  mov rdx, qword ptr [rsp + 0x38]
0025AF53  45 33 C9                        xor r9d, r9d
0025AF56  44 8B C6                        mov r8d, esi
0025AF59  E8 72 D2 FF FF                  call 0x1402581d0
0025AF5E  84 C0                           test al, al
0025AF60  0F 84 8C F0 FF FF               je 0x140259ff2
0025AF66  41 FF C5                        inc r13d
0025AF69  EB C3                           jmp 0x14025af2e
0025AF6B  4C 8B 6C 24 38                  mov r13, qword ptr [rsp + 0x38]
0025AF70  E9 4A EE FF FF                  jmp 0x140259dbf
0025AF75  45 85 D2                        test r10d, r10d
0025AF78  0F 85 FA 01 00 00               jne 0x14025b178
0025AF7E  49 8B 51 18                     mov rdx, qword ptr [r9 + 0x18]
0025AF82  4D 8B 19                        mov r11, qword ptr [r9]
0025AF85  48 8D 42 FF                     lea rax, [rdx - 1]
0025AF89  48 83 F8 FC                     cmp rax, -4
0025AF8D  76 4C                           jbe 0x14025afdb
0025AF8F  41 0F B6 49 20                  movzx ecx, byte ptr [r9 + 0x20]
0025AF94  80 E1 FE                        and cl, 0xfe
0025AF97  49 89 71 10                     mov qword ptr [r9 + 0x10], rsi
0025AF9B  41 88 49 20                     mov byte ptr [r9 + 0x20], cl
0025AF9F  80 E1 FD                        and cl, 0xfd
0025AFA2  8B 46 78                        mov eax, dword ptr [rsi + 0x78]
0025AFA5  41 80 61 21 FE                  and byte ptr [r9 + 0x21], 0xfe
0025AFAA  D1 E8                           shr eax, 1
0025AFAC  24 01                           and al, 1
0025AFAE  49 89 71 18                     mov qword ptr [r9 + 0x18], rsi
0025AFB2  02 C0                           add al, al
0025AFB4  32 C1                           xor al, cl
0025AFB6  24 C7                           and al, 0xc7
0025AFB8  0C 04                           or al, 4
0025AFBA  41 88 41 20                     mov byte ptr [r9 + 0x20], al
0025AFBE  48 8D 05 3B 4F D7 00            lea rax, [rip + 0xd74f3b]
0025AFC5  48 39 86 20 02 00 00            cmp qword ptr [rsi + 0x220], rax
0025AFCC  0F 85 9E 06 00 00               jne 0x14025b670
0025AFD2  45 89 56 04                     mov dword ptr [r14 + 4], r10d
0025AFD6  E9 15 F2 FF FF                  jmp 0x14025a1f0
0025AFDB  48 8D 05 1E 4F D7 00            lea rax, [rip + 0xd74f1e]
0025AFE2  48 39 82 20 02 00 00            cmp qword ptr [rdx + 0x220], rax
0025AFE9  74 A4                           je 0x14025af8f
0025AFEB  41 F6 41 21 01                  test byte ptr [r9 + 0x21], 1
0025AFF0  74 04                           je 0x14025aff6
0025AFF2  83 4A 74 02                     or dword ptr [rdx + 0x74], 2
0025AFF6  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
0025AFFB  C6 82 35 02 00 00 01            mov byte ptr [rdx + 0x235], 1
0025B002  E8 09 63 FA FF                  call 0x140201310
0025B007  EB 86                           jmp 0x14025af8f
0025B009  48 83 F8 FC                     cmp rax, -4
0025B00D  0F 86 DA 02 00 00               jbe 0x14025b2ed
0025B013  41 0F B6 49 30                  movzx ecx, byte ptr [r9 + 0x30]
0025B018  80 E1 FE                        and cl, 0xfe
0025B01B  4D 89 51 20                     mov qword ptr [r9 + 0x20], r10
0025B01F  41 88 49 30                     mov byte ptr [r9 + 0x30], cl
0025B023  80 E1 FD                        and cl, 0xfd
0025B026  41 8B 42 78                     mov eax, dword ptr [r10 + 0x78]
0025B02A  D1 E8                           shr eax, 1
0025B02C  24 01                           and al, 1
0025B02E  4D 89 51 28                     mov qword ptr [r9 + 0x28], r10
0025B032  02 C0                           add al, al
0025B034  32 C1                           xor al, cl
0025B036  41 0F B6 CB                     movzx ecx, r11b
0025B03A  24 C7                           and al, 0xc7
0025B03C  0C 04                           or al, 4
0025B03E  41 88 41 30                     mov byte ptr [r9 + 0x30], al
0025B042  41 0F B6 41 31                  movzx eax, byte ptr [r9 + 0x31]
0025B047  32 C8                           xor cl, al
0025B049  80 E1 01                        and cl, 1
0025B04C  32 C8                           xor cl, al
0025B04E  41 88 49 31                     mov byte ptr [r9 + 0x31], cl
0025B052  49 8B CA                        mov rcx, r10
0025B055  E8 D6 81 0F 00                  call 0x140353230
0025B05A  84 C0                           test al, al
0025B05C  0F 85 3A EE FF FF               jne 0x140259e9c
0025B062  41 8B 45 24                     mov eax, dword ptr [r13 + 0x24]
0025B066  41 89 82 18 02 00 00            mov dword ptr [r10 + 0x218], eax
0025B06D  E9 2A EE FF FF                  jmp 0x140259e9c
0025B072  4C 8B C7                        mov r8, rdi
0025B075  8B D7                           mov edx, edi
0025B077  41 3B D1                        cmp edx, r9d
0025B07A  73 20                           jae 0x14025b09c
0025B07C  8B C2                           mov eax, edx
0025B07E  48 8D 0C 80                     lea rcx, [rax + rax*4]
0025B082  49 8B 44 CE 10                  mov rax, qword ptr [r14 + rcx*8 + 0x10]
0025B087  4D 8D 14 CE                     lea r10, [r14 + rcx*8]
0025B08B  48 8B 88 80 8E 00 00            mov rcx, qword ptr [rax + 0x8e80]
0025B092  49 39 4A 20                     cmp qword ptr [r10 + 0x20], rcx
0025B096  74 3D                           je 0x14025b0d5
0025B098  4D 8D 42 10                     lea r8, [r10 + 0x10]
0025B09C  45 85 C9                        test r9d, r9d
0025B09F  0F 84 77 EC FF FF               je 0x140259d1c
0025B0A5  49 8D 4E 30                     lea rcx, [r14 + 0x30]
0025B0A9  41 8B D1                        mov edx, r9d
0025B0AC  48 8D 41 E0                     lea rax, [rcx - 0x20]
0025B0B0  49 3B C0                        cmp rax, r8
0025B0B3  74 11                           je 0x14025b0c6
0025B0B5  49 8B 40 10                     mov rax, qword ptr [r8 + 0x10]
0025B0B9  48 89 41 F0                     mov qword ptr [rcx - 0x10], rax
0025B0BD  41 0F B6 40 20                  movzx eax, byte ptr [r8 + 0x20]
0025B0C2  0C 20                           or al, 0x20
0025B0C4  88 01                           mov byte ptr [rcx], al
0025B0C6  48 83 C1 28                     add rcx, 0x28
0025B0CA  48 83 EA 01                     sub rdx, 1
0025B0CE  75 DC                           jne 0x14025b0ac
0025B0D0  E9 47 EC FF FF                  jmp 0x140259d1c
0025B0D5  FF C2                           inc edx
0025B0D7  EB 9E                           jmp 0x14025b077
0025B0D9  E8 52 81 0F 00                  call 0x140353230
0025B0DE  84 C0                           test al, al
0025B0E0  0F 85 6D ED FF FF               jne 0x140259e53
0025B0E6  41 F6 41 31 01                  test byte ptr [r9 + 0x31], 1
0025B0EB  74 04                           je 0x14025b0f1
0025B0ED  83 49 74 02                     or dword ptr [rcx + 0x74], 2
0025B0F1  C6 81 35 02 00 00 01            mov byte ptr [rcx + 0x235], 1
0025B0F8  48 8B D1                        mov rdx, rcx
0025B0FB  49 8B CF                        mov rcx, r15
0025B0FE  E8 0D 62 FA FF                  call 0x140201310
0025B103  E9 4B ED FF FF                  jmp 0x140259e53
0025B108  48 8B 82 F0 02 00 00            mov rax, qword ptr [rdx + 0x2f0]
0025B10F  F0 81 20 FF FF FB FF            lock and dword ptr [rax], 0xfffbffff
0025B116  44 0F B6 6D F8                  movzx r13d, byte ptr [rbp - 8]
0025B11B  E9 B3 FA FF FF                  jmp 0x14025abd3
0025B120  48 83 F8 FC                     cmp rax, -4
0025B124  0F 86 2B 02 00 00               jbe 0x14025b355
0025B12A  41 0F B6 49 30                  movzx ecx, byte ptr [r9 + 0x30]
0025B12F  80 E1 FE                        and cl, 0xfe
0025B132  49 89 71 20                     mov qword ptr [r9 + 0x20], rsi
0025B136  41 88 49 30                     mov byte ptr [r9 + 0x30], cl
0025B13A  80 E1 FD                        and cl, 0xfd
0025B13D  8B 46 78                        mov eax, dword ptr [rsi + 0x78]
0025B140  41 80 61 31 FE                  and byte ptr [r9 + 0x31], 0xfe
0025B145  D1 E8                           shr eax, 1
0025B147  24 01                           and al, 1
0025B149  49 89 71 28                     mov qword ptr [r9 + 0x28], rsi
0025B14D  02 C0                           add al, al
0025B14F  32 C1                           xor al, cl
0025B151  48 8B CE                        mov rcx, rsi
0025B154  24 C7                           and al, 0xc7
0025B156  0C 04                           or al, 4
0025B158  41 88 41 30                     mov byte ptr [r9 + 0x30], al
0025B15C  E8 CF 80 0F 00                  call 0x140353230
0025B161  84 C0                           test al, al
0025B163  0F 85 9D F9 FF FF               jne 0x14025ab06
0025B169  41 8B 45 24                     mov eax, dword ptr [r13 + 0x24]
0025B16D  89 86 18 02 00 00               mov dword ptr [rsi + 0x218], eax
0025B173  E9 8E F9 FF FF                  jmp 0x14025ab06
0025B178  8B DF                           mov ebx, edi
0025B17A  41 38 3E                        cmp byte ptr [r14], dil
0025B17D  0F 86 4F FE FF FF               jbe 0x14025afd2
0025B183  4C 8B 7C 24 50                  mov r15, qword ptr [rsp + 0x50]
0025B188  8B C3                           mov eax, ebx
0025B18A  48 8D 0C 80                     lea rcx, [rax + rax*4]
0025B18E  4D 8B 5C CE 10                  mov r11, qword ptr [r14 + rcx*8 + 0x10]
0025B193  4D 8D 0C CE                     lea r9, [r14 + rcx*8]
0025B197  49 8B 4C CE 28                  mov rcx, qword ptr [r14 + rcx*8 + 0x28]
0025B19C  48 8D 41 FF                     lea rax, [rcx - 1]
0025B1A0  4D 3B DC                        cmp r11, r12
0025B1A3  75 5E                           jne 0x14025b203
0025B1A5  48 83 F8 FC                     cmp rax, -4
0025B1A9  0F 86 D5 01 00 00               jbe 0x14025b384
0025B1AF  41 0F B6 49 30                  movzx ecx, byte ptr [r9 + 0x30]
0025B1B4  80 E1 FE                        and cl, 0xfe
0025B1B7  49 89 71 20                     mov qword ptr [r9 + 0x20], rsi
0025B1BB  41 88 49 30                     mov byte ptr [r9 + 0x30], cl
0025B1BF  80 E1 FD                        and cl, 0xfd
0025B1C2  8B 46 78                        mov eax, dword ptr [rsi + 0x78]
0025B1C5  41 80 61 31 FE                  and byte ptr [r9 + 0x31], 0xfe
0025B1CA  D1 E8                           shr eax, 1
0025B1CC  24 01                           and al, 1
0025B1CE  49 89 71 28                     mov qword ptr [r9 + 0x28], rsi
0025B1D2  02 C0                           add al, al
0025B1D4  32 C1                           xor al, cl
0025B1D6  48 8B CE                        mov rcx, rsi
0025B1D9  24 C7                           and al, 0xc7
0025B1DB  0C 04                           or al, 4
0025B1DD  41 88 41 30                     mov byte ptr [r9 + 0x30], al
0025B1E1  E8 4A 80 0F 00                  call 0x140353230
0025B1E6  84 C0                           test al, al
0025B1E8  75 0A                           jne 0x14025b1f4
0025B1EA  41 8B 43 24                     mov eax, dword ptr [r11 + 0x24]
0025B1EE  89 86 18 02 00 00               mov dword ptr [rsi + 0x218], eax
0025B1F4  41 0F B6 06                     movzx eax, byte ptr [r14]
0025B1F8  FF C3                           inc ebx
0025B1FA  3B D8                           cmp ebx, eax
0025B1FC  72 8A                           jb 0x14025b188
0025B1FE  E9 11 F9 FF FF                  jmp 0x14025ab14
0025B203  4D 8B AB 80 8E 00 00            mov r13, qword ptr [r11 + 0x8e80]
0025B20A  48 83 F8 FC                     cmp rax, -4
0025B20E  0F 86 9F 01 00 00               jbe 0x14025b3b3
0025B214  41 0F B6 41 30                  movzx eax, byte ptr [r9 + 0x30]
0025B219  24 FE                           and al, 0xfe
0025B21B  49 89 71 20                     mov qword ptr [r9 + 0x20], rsi
0025B21F  41 88 41 30                     mov byte ptr [r9 + 0x30], al
0025B223  24 FD                           and al, 0xfd
0025B225  8B 4E 78                        mov ecx, dword ptr [rsi + 0x78]
0025B228  D1 E9                           shr ecx, 1
0025B22A  80 E1 01                        and cl, 1
0025B22D  02 C9                           add cl, cl
0025B22F  32 C8                           xor cl, al
0025B231  80 E1 E7                        and cl, 0xe7
0025B234  80 C9 04                        or cl, 4
0025B237  0F B6 C1                        movzx eax, cl
0025B23A  80 C9 20                        or cl, 0x20
0025B23D  24 DF                           and al, 0xdf
0025B23F  0F B6 C9                        movzx ecx, cl
0025B242  0F B6 C0                        movzx eax, al
0025B245  49 3B F5                        cmp rsi, r13
0025B248  0F 44 C8                        cmove ecx, eax
0025B24B  41 88 49 30                     mov byte ptr [r9 + 0x30], cl
0025B24F  49 8B CD                        mov rcx, r13
0025B252  41 80 61 31 FE                  and byte ptr [r9 + 0x31], 0xfe
0025B257  4D 89 69 28                     mov qword ptr [r9 + 0x28], r13
0025B25B  E8 D0 7F 0F 00                  call 0x140353230
0025B260  84 C0                           test al, al
0025B262  75 90                           jne 0x14025b1f4
0025B264  41 8B 43 24                     mov eax, dword ptr [r11 + 0x24]
0025B268  41 89 85 18 02 00 00            mov dword ptr [r13 + 0x218], eax
0025B26F  EB 83                           jmp 0x14025b1f4
0025B271  48 8B 42 68                     mov rax, qword ptr [rdx + 0x68]
0025B275  48 F7 D0                        not rax
0025B278  E9 32 EF FF FF                  jmp 0x14025a1af
0025B27D  8B DF                           mov ebx, edi
0025B27F  41 0F B6 06                     movzx eax, byte ptr [r14]
0025B283  3B D8                           cmp ebx, eax
0025B285  72 3B                           jb 0x14025b2c2
0025B287  8B DF                           mov ebx, edi
0025B289  41 0F B6 06                     movzx eax, byte ptr [r14]
0025B28D  3B D8                           cmp ebx, eax
0025B28F  0F 83 78 EF FF FF               jae 0x14025a20d
0025B295  4C 8B 4C 24 40                  mov r9, qword ptr [rsp + 0x40]
0025B29A  48 8B D6                        mov rdx, rsi
0025B29D  4C 8B 44 24 58                  mov r8, qword ptr [rsp + 0x58]
0025B2A2  8B C3                           mov eax, ebx
0025B2A4  48 8D 0C 80                     lea rcx, [rax + rax*4]
0025B2A8  4D 8D 24 CE                     lea r12, [r14 + rcx*8]
0025B2AC  49 8D 4C 24 10                  lea rcx, [r12 + 0x10]
0025B2B1  E8 5A CA FF FF                  call 0x140257d10
0025B2B6  84 C0                           test al, al
0025B2B8  0F 85 8D 00 00 00               jne 0x14025b34b
0025B2BE  FF C3                           inc ebx
0025B2C0  EB C7                           jmp 0x14025b289
0025B2C2  8B C3                           mov eax, ebx
0025B2C4  45 33 C9                        xor r9d, r9d
0025B2C7  45 33 C0                        xor r8d, r8d
0025B2CA  48 8B D6                        mov rdx, rsi
0025B2CD  48 8D 0C 85 02 00 00 00         lea rcx, [rax*4 + 2]
0025B2D5  48 03 C8                        add rcx, rax
0025B2D8  49 8D 0C CE                     lea rcx, [r14 + rcx*8]
0025B2DC  E8 EF CE FF FF                  call 0x1402581d0
0025B2E1  84 C0                           test al, al
0025B2E3  0F 84 24 EF FF FF               je 0x14025a20d
0025B2E9  FF C3                           inc ebx
0025B2EB  EB 92                           jmp 0x14025b27f
0025B2ED  E8 3E 7F 0F 00                  call 0x140353230
0025B2F2  84 C0                           test al, al
0025B2F4  0F 85 19 FD FF FF               jne 0x14025b013
0025B2FA  41 F6 41 31 01                  test byte ptr [r9 + 0x31], 1
0025B2FF  74 04                           je 0x14025b305
0025B301  83 49 74 02                     or dword ptr [rcx + 0x74], 2
0025B305  C6 81 35 02 00 00 01            mov byte ptr [rcx + 0x235], 1
0025B30C  48 8B D1                        mov rdx, rcx
0025B30F  49 8B CF                        mov rcx, r15
0025B312  E8 F9 5F FA FF                  call 0x140201310
0025B317  E9 F7 FC FF FF                  jmp 0x14025b013
0025B31C  E8 0F 7F 0F 00                  call 0x140353230
0025B321  84 C0                           test al, al
0025B323  0F 85 92 F7 FF FF               jne 0x14025aabb
0025B329  41 F6 41 31 01                  test byte ptr [r9 + 0x31], 1
0025B32E  74 04                           je 0x14025b334
0025B330  83 49 74 02                     or dword ptr [rcx + 0x74], 2
0025B334  C6 81 35 02 00 00 01            mov byte ptr [rcx + 0x235], 1
0025B33B  48 8B D1                        mov rdx, rcx
0025B33E  49 8B CF                        mov rcx, r15
0025B341  E8 CA 5F FA FF                  call 0x140201310
0025B346  E9 70 F7 FF FF                  jmp 0x14025aabb
0025B34B  4D 8B 64 24 10                  mov r12, qword ptr [r12 + 0x10]
0025B350  E9 27 F6 FF FF                  jmp 0x14025a97c
0025B355  E8 D6 7E 0F 00                  call 0x140353230
0025B35A  84 C0                           test al, al
0025B35C  0F 85 C8 FD FF FF               jne 0x14025b12a
0025B362  41 F6 41 31 01                  test byte ptr [r9 + 0x31], 1
0025B367  74 04                           je 0x14025b36d
0025B369  83 49 74 02                     or dword ptr [rcx + 0x74], 2
0025B36D  C6 81 35 02 00 00 01            mov byte ptr [rcx + 0x235], 1
0025B374  48 8B D1                        mov rdx, rcx
0025B377  49 8B CF                        mov rcx, r15
0025B37A  E8 91 5F FA FF                  call 0x140201310
0025B37F  E9 A6 FD FF FF                  jmp 0x14025b12a
0025B384  E8 A7 7E 0F 00                  call 0x140353230
0025B389  84 C0                           test al, al
0025B38B  0F 85 1E FE FF FF               jne 0x14025b1af
0025B391  41 F6 41 31 01                  test byte ptr [r9 + 0x31], 1
0025B396  74 04                           je 0x14025b39c
0025B398  83 49 74 02                     or dword ptr [rcx + 0x74], 2
0025B39C  C6 81 35 02 00 00 01            mov byte ptr [rcx + 0x235], 1
0025B3A3  48 8B D1                        mov rdx, rcx
0025B3A6  49 8B CF                        mov rcx, r15
0025B3A9  E8 62 5F FA FF                  call 0x140201310
0025B3AE  E9 FC FD FF FF                  jmp 0x14025b1af
0025B3B3  E8 78 7E 0F 00                  call 0x140353230
0025B3B8  84 C0                           test al, al
0025B3BA  0F 85 54 FE FF FF               jne 0x14025b214
0025B3C0  41 F6 41 31 01                  test byte ptr [r9 + 0x31], 1
0025B3C5  74 04                           je 0x14025b3cb
0025B3C7  83 49 74 02                     or dword ptr [rcx + 0x74], 2
0025B3CB  C6 81 35 02 00 00 01            mov byte ptr [rcx + 0x235], 1
0025B3D2  48 8B D1                        mov rdx, rcx
0025B3D5  49 8B CF                        mov rcx, r15
0025B3D8  E8 33 5F FA FF                  call 0x140201310
0025B3DD  E9 32 FE FF FF                  jmp 0x14025b214
0025B3E2  45 85 D2                        test r10d, r10d
0025B3E5  0F 85 96 00 00 00               jne 0x14025b481
0025B3EB  49 8B 51 18                     mov rdx, qword ptr [r9 + 0x18]
0025B3EF  48 8D 1D 0A 4B D7 00            lea rbx, [rip + 0xd74b0a]
0025B3F6  4D 8B 19                        mov r11, qword ptr [r9]
0025B3F9  48 8D 42 FF                     lea rax, [rdx - 1]
0025B3FD  48 83 F8 FC                     cmp rax, -4
0025B401  76 57                           jbe 0x14025b45a
0025B403  41 0F B6 41 20                  movzx eax, byte ptr [r9 + 0x20]
0025B408  24 FE                           and al, 0xfe
0025B40A  4D 89 69 10                     mov qword ptr [r9 + 0x10], r13
0025B40E  41 88 41 20                     mov byte ptr [r9 + 0x20], al
0025B412  41 8B 4D 78                     mov ecx, dword ptr [r13 + 0x78]
0025B416  D1 E9                           shr ecx, 1
0025B418  02 C9                           add cl, cl
0025B41A  4D 89 69 18                     mov qword ptr [r9 + 0x18], r13
0025B41E  32 C8                           xor cl, al
0025B420  80 E1 02                        and cl, 2
0025B423  32 C8                           xor cl, al
0025B425  41 0F B6 41 21                  movzx eax, byte ptr [r9 + 0x21]
0025B42A  80 C9 04                        or cl, 4
0025B42D  80 E1 C7                        and cl, 0xc7
0025B430  41 88 49 20                     mov byte ptr [r9 + 0x20], cl
0025B434  0F B6 4C 24 30                  movzx ecx, byte ptr [rsp + 0x30]
0025B439  32 C8                           xor cl, al
0025B43B  80 E1 01                        and cl, 1
0025B43E  32 C8                           xor cl, al
0025B440  41 88 49 21                     mov byte ptr [r9 + 0x21], cl
0025B444  49 39 9D 20 02 00 00            cmp qword ptr [r13 + 0x220], rbx
0025B44B  0F 85 2E 02 00 00               jne 0x14025b67f
0025B451  45 89 56 04                     mov dword ptr [r14 + 4], r10d
0025B455  E9 37 F4 FF FF                  jmp 0x14025a891
0025B45A  48 39 9A 20 02 00 00            cmp qword ptr [rdx + 0x220], rbx
0025B461  74 A0                           je 0x14025b403
0025B463  41 F6 41 21 01                  test byte ptr [r9 + 0x21], 1
0025B468  74 04                           je 0x14025b46e
0025B46A  83 4A 74 02                     or dword ptr [rdx + 0x74], 2
0025B46E  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
0025B473  C6 82 35 02 00 00 01            mov byte ptr [rdx + 0x235], 1
0025B47A  E8 91 5E FA FF                  call 0x140201310
0025B47F  EB 82                           jmp 0x14025b403
0025B481  8B DF                           mov ebx, edi
0025B483  41 38 3E                        cmp byte ptr [r14], dil
0025B486  76 C9                           jbe 0x14025b451
0025B488  44 0F B6 5C 24 30               movzx r11d, byte ptr [rsp + 0x30]
0025B48E  4C 8B 7C 24 50                  mov r15, qword ptr [rsp + 0x50]
0025B493  8B C3                           mov eax, ebx
0025B495  48 8D 0C 80                     lea rcx, [rax + rax*4]
0025B499  49 8B 74 CE 10                  mov rsi, qword ptr [r14 + rcx*8 + 0x10]
0025B49E  4D 8D 0C CE                     lea r9, [r14 + rcx*8]
0025B4A2  49 8B 4C CE 28                  mov rcx, qword ptr [r14 + rcx*8 + 0x28]
0025B4A7  48 8D 41 FF                     lea rax, [rcx - 1]
0025B4AB  49 3B F4                        cmp rsi, r12
0025B4AE  75 7B                           jne 0x14025b52b
0025B4B0  48 83 F8 FC                     cmp rax, -4
0025B4B4  0F 86 E9 00 00 00               jbe 0x14025b5a3
0025B4BA  41 0F B6 49 30                  movzx ecx, byte ptr [r9 + 0x30]
0025B4BF  80 E1 FE                        and cl, 0xfe
0025B4C2  4D 89 69 20                     mov qword ptr [r9 + 0x20], r13
0025B4C6  41 88 49 30                     mov byte ptr [r9 + 0x30], cl
0025B4CA  80 E1 FD                        and cl, 0xfd
0025B4CD  41 8B 45 78                     mov eax, dword ptr [r13 + 0x78]
0025B4D1  D1 E8                           shr eax, 1
0025B4D3  24 01                           and al, 1
0025B4D5  4D 89 69 28                     mov qword ptr [r9 + 0x28], r13
0025B4D9  02 C0                           add al, al
0025B4DB  32 C1                           xor al, cl
0025B4DD  41 0F B6 CB                     movzx ecx, r11b
0025B4E1  24 C7                           and al, 0xc7
0025B4E3  0C 04                           or al, 4
0025B4E5  41 88 41 30                     mov byte ptr [r9 + 0x30], al
0025B4E9  41 0F B6 41 31                  movzx eax, byte ptr [r9 + 0x31]
0025B4EE  32 C8                           xor cl, al
0025B4F0  80 E1 01                        and cl, 1
0025B4F3  32 C8                           xor cl, al
0025B4F5  41 88 49 31                     mov byte ptr [r9 + 0x31], cl
0025B4F9  49 8B CD                        mov rcx, r13
0025B4FC  E8 2F 7D 0F 00                  call 0x140353230
0025B501  84 C0                           test al, al
0025B503  75 0A                           jne 0x14025b50f
0025B505  8B 46 24                        mov eax, dword ptr [rsi + 0x24]
0025B508  41 89 85 18 02 00 00            mov dword ptr [r13 + 0x218], eax
0025B50F  41 0F B6 06                     movzx eax, byte ptr [r14]
0025B513  FF C3                           inc ebx
0025B515  3B D8                           cmp ebx, eax
0025B517  0F 82 76 FF FF FF               jb 0x14025b493
0025B51D  4C 8B 7C 24 60                  mov r15, qword ptr [rsp + 0x60]
0025B522  45 89 56 04                     mov dword ptr [r14 + 4], r10d
0025B526  E9 66 F3 FF FF                  jmp 0x14025a891
0025B52B  4C 8B AE 80 8E 00 00            mov r13, qword ptr [rsi + 0x8e80]
0025B532  48 83 F8 FC                     cmp rax, -4
0025B536  0F 86 96 00 00 00               jbe 0x14025b5d2
0025B53C  41 0F B6 41 30                  movzx eax, byte ptr [r9 + 0x30]
0025B541  48 8B 54 24 38                  mov rdx, qword ptr [rsp + 0x38]
0025B546  24 FE                           and al, 0xfe
0025B548  41 88 41 30                     mov byte ptr [r9 + 0x30], al
0025B54C  24 FD                           and al, 0xfd
0025B54E  49 89 51 20                     mov qword ptr [r9 + 0x20], rdx
0025B552  8B 4A 78                        mov ecx, dword ptr [rdx + 0x78]
0025B555  D1 E9                           shr ecx, 1
0025B557  80 E1 01                        and cl, 1
0025B55A  02 C9                           add cl, cl
0025B55C  32 C8                           xor cl, al
0025B55E  80 E1 E7                        and cl, 0xe7
0025B561  80 C9 04                        or cl, 4
0025B564  0F B6 C1                        movzx eax, cl
0025B567  80 C9 20                        or cl, 0x20
0025B56A  24 DF                           and al, 0xdf
0025B56C  0F B6 C9                        movzx ecx, cl
0025B56F  0F B6 C0                        movzx eax, al
0025B572  49 3B D5                        cmp rdx, r13
0025B575  0F 44 C8                        cmove ecx, eax
0025B578  41 88 49 30                     mov byte ptr [r9 + 0x30], cl
0025B57C  49 8B CD                        mov rcx, r13
0025B57F  41 80 61 31 FE                  and byte ptr [r9 + 0x31], 0xfe
0025B584  4D 89 69 28                     mov qword ptr [r9 + 0x28], r13
0025B588  E8 A3 7C 0F 00                  call 0x140353230
0025B58D  84 C0                           test al, al
0025B58F  75 0A                           jne 0x14025b59b
0025B591  8B 46 24                        mov eax, dword ptr [rsi + 0x24]
0025B594  41 89 85 18 02 00 00            mov dword ptr [r13 + 0x218], eax
0025B59B  4C 8B EA                        mov r13, rdx
0025B59E  E9 6C FF FF FF                  jmp 0x14025b50f
0025B5A3  E8 88 7C 0F 00                  call 0x140353230
0025B5A8  84 C0                           test al, al
0025B5AA  0F 85 0A FF FF FF               jne 0x14025b4ba
0025B5B0  41 F6 41 31 01                  test byte ptr [r9 + 0x31], 1
0025B5B5  74 04                           je 0x14025b5bb
0025B5B7  83 49 74 02                     or dword ptr [rcx + 0x74], 2
0025B5BB  C6 81 35 02 00 00 01            mov byte ptr [rcx + 0x235], 1
0025B5C2  48 8B D1                        mov rdx, rcx
0025B5C5  49 8B CF                        mov rcx, r15
0025B5C8  E8 43 5D FA FF                  call 0x140201310
0025B5CD  E9 E8 FE FF FF                  jmp 0x14025b4ba
0025B5D2  E8 59 7C 0F 00                  call 0x140353230
0025B5D7  84 C0                           test al, al
0025B5D9  0F 85 5D FF FF FF               jne 0x14025b53c
0025B5DF  41 F6 41 31 01                  test byte ptr [r9 + 0x31], 1
0025B5E4  74 04                           je 0x14025b5ea
0025B5E6  83 49 74 02                     or dword ptr [rcx + 0x74], 2
0025B5EA  C6 81 35 02 00 00 01            mov byte ptr [rcx + 0x235], 1
0025B5F1  48 8B D1                        mov rdx, rcx
0025B5F4  49 8B CF                        mov rcx, r15
0025B5F7  E8 14 5D FA FF                  call 0x140201310
0025B5FC  E9 3B FF FF FF                  jmp 0x14025b53c
0025B601  41 B1 01                        mov r9b, 1
0025B604  44 88 4C 24 31                  mov byte ptr [rsp + 0x31], r9b
0025B609  41 F7 42 78 00 00 40 00         test dword ptr [r10 + 0x78], 0x400000
0025B611  49 8B CA                        mov rcx, r10
0025B614  48 89 4C 24 58                  mov qword ptr [rsp + 0x58], rcx
0025B619  74 2F                           je 0x14025b64a
0025B61B  48 8B D6                        mov rdx, rsi
0025B61E  E8 31 AC 0A 00                  call 0x140306254
0025B623  84 C0                           test al, al
0025B625  74 19                           je 0x14025b640
0025B627  41 B1 01                        mov r9b, 1
0025B62A  48 8B D6                        mov rdx, rsi
0025B62D  49 8B CA                        mov rcx, r10
0025B630  E8 0B AA 0A 00                  call 0x140306040
0025B635  4C 8B 5C 24 68                  mov r11, qword ptr [rsp + 0x68]
0025B63A  44 0F B6 4C 24 31               movzx r9d, byte ptr [rsp + 0x31]
0025B640  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
0025B645  4C 8B 44 24 48                  mov r8, qword ptr [rsp + 0x48]
0025B64A  45 84 C9                        test r9b, r9b
0025B64D  0F 84 2E E6 FF FF               je 0x140259c81
0025B653  48 89 79 40                     mov qword ptr [rcx + 0x40], rdi
0025B657  E9 25 E6 FF FF                  jmp 0x140259c81
0025B65C  4D 3B D7                        cmp r10, r15
0025B65F  74 A8                           je 0x14025b609
0025B661  F0 49 0F BA 6A 40 00            lock bts qword ptr [r10 + 0x40], 0
0025B668  0F 82 13 E6 FF FF               jb 0x140259c81
0025B66E  EB 91                           jmp 0x14025b601
0025B670  41 8B 43 24                     mov eax, dword ptr [r11 + 0x24]
0025B674  89 86 18 02 00 00               mov dword ptr [rsi + 0x218], eax
0025B67A  E9 53 F9 FF FF                  jmp 0x14025afd2
0025B67F  41 8B 43 24                     mov eax, dword ptr [r11 + 0x24]
0025B683  41 89 85 18 02 00 00            mov dword ptr [r13 + 0x218], eax
0025B68A  E9 C2 FD FF FF                  jmp 0x14025b451
0025B68F  48 8B 8D E0 00 00 00            mov rcx, qword ptr [rbp + 0xe0]
0025B696  48 33 CC                        xor rcx, rsp
0025B699  E8 A2 0F 45 00                  call 0x1406ac640
0025B69E  48 8B 9C 24 40 02 00 00         mov rbx, qword ptr [rsp + 0x240]
0025B6A6  48 81 C4 F0 01 00 00            add rsp, 0x1f0
0025B6AD  41 5F                           pop r15
0025B6AF  41 5E                           pop r14
0025B6B1  41 5D                           pop r13
0025B6B3  41 5C                           pop r12
0025B6B5  5F                              pop rdi
0025B6B6  5E                              pop rsi
0025B6B7  5D                              pop rbp
0025B6B8  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiAttemptToScheduleThreadToBusyIsolationUnit(__int64 a1, __int64 a2, unsigned __int8 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int8 v_stack_m12B;
    unsigned __int8 v_stack_m12C;
    unsigned __int8 v_stack_m12D;
    unsigned __int8 v_stack_m12E;
    unsigned __int8 v_stack_m12F;
    unsigned __int8 v_stack_m130;
    unsigned int v_stack_m134;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m160;
    unsigned __int64 v_stack_m168;
    unsigned __int64 v_stack_m170;
    unsigned __int64 v_stack_m178;
    unsigned __int64 v_stack_m180;
    unsigned __int64 v_stack_m188;
    unsigned __int64 v_stack_m190;
    unsigned int v_stack_m198;
    unsigned int v_stack_m19C;
    unsigned int v_stack_m1A0;
    unsigned int v_stack_m1A4;
    unsigned int v_stack_m1A8;
    unsigned __int64 v_stack_m1B0;
    unsigned __int64 v_stack_m1B8;
    unsigned __int64 v_stack_m1C0;
    unsigned __int64 v_stack_m1C8;
    unsigned __int64 v_stack_m1D0;
    unsigned __int64 v_stack_m1D8;
    unsigned __int64 v_stack_m1E0;
    unsigned int v_stack_m1E8;
    unsigned __int64 v_stack_m1F0;
    unsigned __int8 v_stack_m1F7;
    unsigned __int8 v_stack_m1F8;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_mDC;
    unsigned __int64 v_stack_p18;

    v_stack_p18 = v_rbx;
    v_rsp = (v_rsp) - (496);
    result = (*(unsigned __int64 *)(v_rip + 12258330)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m1D8 = a5;
    v_r12 = (*(unsigned __int64 *)(a4)) & (-2);
    v_stack_m160 = a6;
    v_stack_m1F8 = a3;
    v_stack_m1F0 = a2;
    a2 = 0;
    v_stack_m1C8 = a1;
    v_stack_m190 = a7;
    v_stack_m1B0 = a4;
    result = memset(*(unsigned __int64 *)(a1 + 14312), a2, 240, a4);
    v_rdi = 0;
    v_stack_m1C0 = 0;
    a1 = (*(unsigned __int64 *)(a4)) & (-2);
    v_stack_m1E8 = 0;
    a3 = (unsigned int)((*(unsigned __int64 *)(a4)) & (1));
    v_stack_m188 = a1;
    v_stack_m1B8 = a3;
    if (condition_is_equal) goto loc_00259F47;
    v_r11 = 0;
    if (a3 == 1) {
        result = *(unsigned __int64 *)(a1 + 36440);
        v_r11 = *(unsigned __int64 *)(a1 + 36440);
        v_r11 = (v_r11) + (8);
        v_stack_m1C0 = v_r11;
        a4 = *(unsigned __int8 *)(result);
        v_stack_m1E8 = (unsigned int)(a4);
    }
    if ((unsigned int)(a4) == 0) goto loc_00259CE9;
loc_00259BEA:
    v_stack_m1E0 = (unsigned int)((unsigned int)(a4));
loc_00259BFB:
    result = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 48 - 32) = v_xmm0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 48 - 16) = v_xmm0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 48) = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 48 - 8) = -1;
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312) + 48 + 4) = 63;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 48 - 32) = *(unsigned __int64 *)(v_r11);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 48 - 24) = 0;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_r11) + 36424) != 0) goto loc_00259F6B;
loc_00259C32:
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 48 - 16) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_r11) + 16);
    v_r10 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_r11) + 16);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_r11) + 16) == 0) {
        v_r10 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_r11) + 8);
        *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 48 - 16) = v_r10;
    }
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_r11) + 16)) == v_r10) goto loc_00259F63;
    if ((*(unsigned __int64 *)(v_r11)) == (*(unsigned __int64 *)(gs_base + (0 + 32)))) goto loc_00259F3F;
    a1 = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312) + 48)) & (251));
loc_00259C69:
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312) + 48) = (unsigned __int8)(a1);
loc_00259C6B:
    a4 = 0;
    v_stack_m1F7 = 0;
    if (((*(unsigned int *)(v_r10 + 120)) & (0x400000ULL)) != 0) goto loc_0025B65C;
loc_00259C81:
    result = (unsigned __int8)(~(*(unsigned __int8 *)(*(unsigned __int64 *)(v_r11) + 35)));
    result = (unsigned __int8)((result) & (1));
    a2 = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312) + 48)) & (254));
    a2 = (unsigned __int8)((a2) | ((unsigned __int8)(result)));
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312) + 48) = (unsigned __int8)(a2);
    a1 = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r11) + 56))) >> (6));
    a1 = (unsigned __int8)((a1) ^ ((unsigned __int8)(a2)));
    a1 = (unsigned __int8)((a1) & (2));
    a1 = (unsigned __int8)((a1) ^ ((unsigned __int8)(a2)));
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312) + 48) = (unsigned __int8)((unsigned __int8)(a1));
    result = (unsigned int)(((unsigned __int8)(a1)) >> (1));
    result = (unsigned int)((result) & (1));
    v_r13 = 0;
    if (((unsigned int)(result)) > 0) { v_r13 = (unsigned int)(result); }
    v_r11 = (v_r11) + (8);
    v_rbx = (*(unsigned __int64 *)(a1 + 14312) + 48) + (40);
    v_stack_m1C0 = v_r11;
    a3 = ((unsigned int)((unsigned int)(a4))) - (1);
    v_stack_m1E0 = a3;
    if (condition_is_not_equal) goto loc_00259BFB;
loc_00259CE9:
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 14312) + 4) = (unsigned int)(v_r13);
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 14312) + 8) = (unsigned int)(v_stack_m1B8);
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312)) = (unsigned __int8)((unsigned int)(v_stack_m1E8));
    if ((unsigned int)(v_stack_m1B8) == 0) goto loc_00259F38;
loc_00259D0D:
    *(unsigned __int8 *)(1 + *(unsigned __int64 *)(a1 + 14312) * 1) = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m188 + 36440) + 1));
    if ((unsigned int)(v_r13) != 0) goto loc_0025B072;
loc_00259D1C:
loc_00259D30:
    if (0 >= ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312))))) goto loc_00259D4E;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16)) == v_r12) goto loc_00259D4A;
    a2 = (unsigned int)((0) + 1);
    goto loc_00259D30;
loc_00259D4A:
loc_00259D4E:
    v_rsi = ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m1B0 + 12))) != 0) ? 1 : 0;
    v_stack_m1B8 = 0;
    if ((*(unsigned __int8 *)(v_rip + 14077270)) == 0) goto loc_0025A151;
    result = KiEvaluateGroupSchedulingPreemption(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16, v_stack_m1F0, (unsigned int)((unsigned int)(v_rsi)), v_stack_m1B8);
loc_00259D86:
    if (v_stack_m190 != 0) {
        *(unsigned __int64 *)(v_stack_m190) = v_stack_m1B8;
    }
    if ((unsigned __int8)(result) == 0) goto loc_00259FF2;
    result = (unsigned int)((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16 + 32)) >> (1));
    result = (unsigned int)((result) & (1));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m1F0 + 120))) >> (1));
    a1 = (unsigned int)((a1) & (1));
    if (((unsigned int)(a1)) < ((unsigned int)(result))) { a1 = (unsigned int)(result); }
    if (((unsigned int)(a1)) == 1) goto loc_0025AF2B;
loc_00259DBF:
loc_00259DC8:
    if (0 >= ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312))))) goto loc_00259DE6;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16)) == v_r12) goto loc_00259DE2;
    a2 = (unsigned int)((0) + 1);
    goto loc_00259DC8;
loc_00259DE2:
loc_00259DE6:
    v_r10 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m1F0 + 120))) >> (1));
    result = (unsigned int)((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16 + 32)) >> (1));
    v_r10 = (unsigned int)((v_r10) & (1));
    result = (unsigned int)((result) & (1));
    v_stack_m1E8 = (unsigned int)(v_r10);
    if (((unsigned int)(v_r10)) >= ((unsigned int)(result))) goto loc_0025B3E2;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312))) <= 0) goto loc_00259EB4;
loc_00259E24:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16)) == v_r12) goto loc_0025B009;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 40) - 1) <= -4) goto loc_0025B0D9;
loc_00259E53:
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 48)) | (1));
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 32) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16) + 24);
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 48) = (unsigned __int8)(result);
    result = (unsigned __int8)((result) & (253));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16) + 24) + 120))) >> (1));
    a1 = (unsigned __int8)((a1) & (1));
    a1 = (unsigned __int8)((a1) + ((unsigned __int8)(a1)));
    a1 = (unsigned __int8)((a1) ^ ((unsigned __int8)(result)));
    a1 = (unsigned __int8)((a1) & (231));
    a1 = (unsigned __int8)((a1) | (4));
    a1 = (unsigned __int8)((a1) & (223));
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 48) = (unsigned __int8)(a1);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 40) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16) + 24);
    result = KiIsPrcbThread(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16) + 24), a2, *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312)), *(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8);
    if ((unsigned __int8)(result) == 0) {
        result = *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16) + 36);
        *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16) + 24) + 536) = (unsigned int)(result);
    }
    v_rbx = (unsigned int)((0) + 1);
    if (((unsigned int)(v_rbx)) < ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312))))) goto loc_00259E24;
loc_00259EB4:
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 14312) + 4) = (unsigned int)((unsigned int)(v_stack_m1E8));
loc_00259EC0:
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312))) == 0) goto loc_0025A1F0;
loc_00259ED5:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 24)) <= 0) goto loc_00259EEA;
    if (0 == 0) goto loc_00259EE7;
    v_rbx = 0;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 24)) < 0) {
        v_rbx = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 24);
    }
    a1 = (*(unsigned __int64 *)(a1 + 14312) + 24) + (40);
    a2 = ((unsigned int)((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312))))) - (1);
    if (condition_is_not_equal) goto loc_00259ED5;
    if (v_rbx == 0) goto loc_0025A1F0;
    a1 = (0) + (11);
    a1 = (a1) << (4);
    a1 = (a1) + (*(unsigned __int64 *)(a1 + 14312));
    if (((*(unsigned int *)(v_rip + 14076964)) & (0x200000ULL)) == 0) goto loc_0025A5EB;
    *(unsigned __int64 *)(a1 + 8) = v_rbx;
    *(unsigned __int64 *)(a1) = 0;
    if (a1 != 0) goto loc_0025A82D;
loc_00259F31:
    v_rsi = (unsigned int)((0) + 1);
    goto loc_00259EC0;
loc_00259F38:
    result = 0;
    goto loc_00259D0D;
loc_00259F3F:
    a1 = (unsigned __int8)((a1) | (4));
    goto loc_00259C69;
loc_00259F47:
    v_stack_m1C0 = v_stack_m188;
    v_stack_m1E8 = 1;
    goto loc_00259BEA;
loc_00259F63:
    goto loc_00259C6B;
loc_00259F6B:
    if (((*(unsigned __int8 *)(v_rsi + 35)) & (16)) != 0) goto loc_0025A191;
loc_00259F75:
    *(unsigned __int64 *)(v_rbx - 24) = *(unsigned __int64 *)(v_rsi + 36424);
    goto loc_00259C32;
loc_00259F85:
    if ((unsigned __int8)(*(unsigned __int8 *)(v_stack_m1C8 + 13785)) != 0) goto loc_0025A041;
    *(unsigned __int8 *)(v_stack_m1C8 + 13785) = 1;
    *(unsigned int *)(v_stack_m1C8 + 13788) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsi + 36)));
loc_00259FA7:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312) + v_rbx * 8 + 51)) & (2)) != 0) goto loc_0025A131;
loc_00259FB3:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312) + v_rbx * 8 + 51)) & (4)) == 0) goto loc_00259FD1;
    if (*(unsigned __int64 *)(v_rsi + 36536) != 0) goto loc_0025A090;
loc_00259FD1:
    result = *(unsigned __int64 *)(v_rsi + 36536);
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312) + v_rbx * 8 + 51)) & (1)) != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + v_rbx * 8 + 40);
    }
    v_rdi = (unsigned int)((v_rdi) + 1);
    if (((unsigned int)(v_rdi)) < ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312))))) goto loc_0025A010;
loc_00259FF0:
loc_00259FF2:
    goto loc_0025B68F;
loc_00259FF8:
    result = 0;
    *(unsigned __int64 *)((unsigned int)(v_stack_m1E8)) = 0;
    *(unsigned __int64 *)(0 + 64) = v_rdi;
    if ((unsigned __int8)(v_r12) == 0) goto loc_00259FF0;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312))) <= 0) goto loc_00259FF0;
loc_0025A010:
    if ((((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312) + (unsigned int)((unsigned int)(v_rdi)) + (unsigned int)((unsigned int)(v_rdi)) * 4 * 8 + 51))) & (16)) != 0) goto loc_00259F85;
    if ((((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312) + (unsigned int)((unsigned int)(v_rdi)) + (unsigned int)((unsigned int)(v_rdi)) * 4 * 8 + 51))) & (8)) == 0) goto loc_00259FA7;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + (unsigned int)((unsigned int)(v_rdi)) + (unsigned int)((unsigned int)(v_rdi)) * 4 * 8 + 16) + 7)) != 0) goto loc_00259F85;
    goto loc_00259FA7;
loc_0025A041:
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312) + (unsigned int)((unsigned int)(v_rdi)) + (unsigned int)((unsigned int)(v_rdi)) * 4 * 8 + 51))) != 1) goto loc_0025A087;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m1C8 + 13788)))) == (*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + (unsigned int)((unsigned int)(v_rdi)) + (unsigned int)((unsigned int)(v_rdi)) * 4 * 8 + 16) + 36))) goto loc_00259FA7;
    *(unsigned __int8 *)(v_stack_m1C8 + 13785) = 2;
    result = KeAddProcessorAffinityEx(v_stack_m1C8 + 13792, (unsigned int)(*(unsigned int *)(v_stack_m1C8 + 13788)), v_rbx, 1);
loc_0025A06C:
    result = KeAddGroupAffinityEx(v_stack_m1C8 + 13792, *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + (unsigned int)((unsigned int)(v_rdi)) + (unsigned int)((unsigned int)(v_rdi)) * 4 * 8 + 16) + 208), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + (unsigned int)((unsigned int)(v_rdi)) + (unsigned int)((unsigned int)(v_rdi)) * 4 * 8 + 16) + 200), 1);
    goto loc_00259FA7;
loc_0025A087:
    goto loc_0025A06C;
loc_0025A090:
    if ((*(unsigned __int64 *)(v_stack_m1C8 + 36536)) == 0) goto loc_00259FD1;
    if (v_stack_m1C8 == (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + (unsigned int)((unsigned int)(v_rdi)) + (unsigned int)((unsigned int)(v_rdi)) * 4 * 8 + 16))) goto loc_00259FD1;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result))))) & (0x40000ULL));
    if (condition_is_below) goto loc_0025A0C9;
    if ((unsigned int)(result) == 0) goto loc_00259FD1;
    if (((unsigned int)((unsigned __int8)((unsigned int)(*(unsigned int *)(result))))) >= ((unsigned int)(v_stack_m1C8 + 13792))) goto loc_00259FD1;
loc_0025A0C9:
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_m1C8 + 36536) + 12) = 2;
    result = (unsigned __int8)((unsigned int)(*(unsigned int *)(result)));
    v_r12 = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + (unsigned int)((unsigned int)(v_rdi)) + (unsigned int)((unsigned int)(v_rdi)) * 4 * 8 + 16) + 36));
    if ((*(unsigned __int8 *)(v_rip + 14069559)) == 0) {
        result = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + (unsigned int)((unsigned int)(v_rdi)) + (unsigned int)((unsigned int)(v_rdi)) * 4 * 8 + 16) + 36)));
        a2 = v_rip + 14102897;
        v_r12 = *(unsigned __int8 *)(a2 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + (unsigned int)((unsigned int)(v_rdi)) + (unsigned int)((unsigned int)(v_rdi)) * 4 * 8 + 16) + 36)) * 2);
        v_r12 = (unsigned int)((v_r12) << (6));
        result = *(unsigned __int8 *)(a2 + result * 2 + 1);
        a2 = 2;
        v_r12 = (unsigned int)((v_r12) | ((unsigned int)(result)));
    }
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_m1C8 + 36536) + 8) = (unsigned int)(v_r12);
    result = (unsigned int)(*(unsigned int *)(v_rip + 14076421));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14076421)))) & (32)) != 0) {
        a1 = *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + (unsigned int)((unsigned int)(v_rdi)) + (unsigned int)((unsigned int)(v_rdi)) * 4 * 8 + 16) + 36);
        result = EtwTraceXSchedulerPriorityKickSend(a1, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + (unsigned int)((unsigned int)(v_rdi)) + (unsigned int)((unsigned int)(v_rdi)) * 4 * 8 + 16) + 200), 1);
    }
    a2 = ((unsigned int)((unsigned int)(v_r12))) >> (32);
    goto loc_00259FD1;
loc_0025A131:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + (unsigned int)((unsigned int)(v_rdi)) + (unsigned int)((unsigned int)(v_rdi)) * 4 * 8 + 40)) != 0) goto loc_0025A14C;
loc_0025A142:
    result = EtwTraceScheduleThread(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + (unsigned int)((unsigned int)(v_rdi)) + (unsigned int)((unsigned int)(v_rdi)) * 4 * 8 + 40), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + (unsigned int)((unsigned int)(v_rdi)) + (unsigned int)((unsigned int)(v_rdi)) * 4 * 8 + 16), v_stack_m160, 1);
    goto loc_00259FB3;
loc_0025A14C:
    a3 = 0;
    goto loc_0025A142;
loc_0025A151:
    if ((((unsigned __int8)(*(unsigned __int8 *)((unsigned int)((unsigned int)(v_rdi)) + (unsigned int)((unsigned int)(v_rdi)) * 4 + 32))) & (1)) != 0) goto loc_0025A1C7;
    if (((unsigned __int8)(*(unsigned __int8 *)(v_stack_m1F0 + 195))) > (*(unsigned __int8 *)(*(unsigned __int64 *)((unsigned int)((unsigned int)(v_rdi)) + (unsigned int)((unsigned int)(v_rdi)) * 4 + 16) + 195))) goto loc_0025A1E0;
    if (((unsigned __int8)(*(unsigned __int8 *)(v_stack_m1F0 + 195))) != (*(unsigned __int8 *)(*(unsigned __int64 *)((unsigned int)((unsigned int)(v_rdi)) + (unsigned int)((unsigned int)(v_rdi)) * 4 + 16) + 195))) goto loc_0025A1CE;
    a1 = ((((unsigned __int8)(*(unsigned __int8 *)((unsigned int)((unsigned int)(v_rdi)) + (unsigned int)((unsigned int)(v_rdi)) * 4 + 32))) & (24)) == 0) ? 1 : 0;
    result = ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + (unsigned int)((unsigned int)(v_rdi)) + (unsigned int)((unsigned int)(v_rdi)) * 4 * 8 + 16))) & (1)) == 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) != 0) goto loc_0025A1CE;
    goto loc_00259D86;
loc_0025A191:
    result = KeIsForceParkingEnabled(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + (unsigned int)((unsigned int)(v_rdi)) + (unsigned int)((unsigned int)(v_rdi)) * 4 * 8 + 16) + 192), *(unsigned __int8 *)(v_stack_m1F0 + 195), *(unsigned __int8 *)((unsigned int)((unsigned int)(v_rdi)) + (unsigned int)((unsigned int)(v_rdi)) * 4 + 32));
    if ((unsigned __int8)(result) == 0) goto loc_0025A1AB;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + (unsigned int)((unsigned int)(v_rdi)) + (unsigned int)((unsigned int)(v_rdi)) * 4 * 8 + 16) + 35)) & (32)) != 0) goto loc_0025B271;
loc_0025A1AB:
loc_0025A1AF:
    a2 = (*(unsigned __int64 *)(a1 + 712)) & (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + (unsigned int)((unsigned int)(v_rdi)) + (unsigned int)((unsigned int)(v_rdi)) * 4 * 8 + 16) + 192) + 80));
    if (a2 == 0) goto loc_00259F75;
    goto loc_00259C32;
loc_0025A1C7:
    goto loc_00259D86;
loc_0025A1CE:
    if ((((unsigned __int8)(*(unsigned __int8 *)((unsigned int)((unsigned int)(v_rdi)) + (unsigned int)((unsigned int)(v_rdi)) * 4 + 32))) & (16)) == 0) goto loc_0025A1E7;
    if ((unsigned __int8)(*(unsigned __int8 *)(v_stack_m1F0 + 195)) == 0) goto loc_0025A1E7;
    goto loc_00259D86;
loc_0025A1E0:
    goto loc_00259D86;
loc_0025A1E7:
    result = 0;
    goto loc_00259D86;
loc_0025A1F0:
    a2 = 0;
    result = memset(v_stack_m138, a2, 240, *(unsigned __int8 *)((unsigned int)((unsigned int)(v_rdi)) + (unsigned int)((unsigned int)(v_rdi)) * 4 + 32));
    result = KiStartReadyQueueEnumeratorForRescheduleContext(v_stack_m138, *(unsigned __int64 *)(a1 + 14312), 240, *(unsigned __int8 *)((unsigned int)((unsigned int)(v_rdi)) + (unsigned int)((unsigned int)(v_rdi)) * 4 + 32));
loc_0025A20D:
    if (((unsigned __int8)(v_stack_m12B)) == 4) goto loc_0025A84D;
    if ((unsigned __int8)(v_stack_m12B) != 0) goto loc_0025A40F;
loc_0025A230:
    if (1 == 2) goto loc_0025A34F;
    a1 = (unsigned int)((1) - (1));
    if (condition_is_not_equal) goto loc_0025A5FF;
    v_stack_m134 = (unsigned int)((unsigned int)((unsigned int)(v_rdi)));
    if ((unsigned int)((unsigned int)(v_stack_m138)) != 0) goto loc_0025A711;
loc_0025A254:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) & (0xFFFFFFFEULL));
    v_stack_m134 = (unsigned int)(result);
    if (condition_is_equal) goto loc_0025A3F4;
    v_stack_m12E = (unsigned __int8)(v_stack_m12F);
    v_stack_m130 = (unsigned __int8)(*(unsigned __int8 *)((unsigned int)((unsigned int)(v_rdi)) + (unsigned int)((unsigned int)(v_rdi)) * 4 + 32));
    v_stack_m19C = (unsigned int)(*(unsigned __int8 *)((unsigned int)((unsigned int)(v_rdi)) + (unsigned int)((unsigned int)(v_rdi)) * 4 + 32));
    a1 = ((unsigned __int8)(v_stack_m12F) + (unsigned __int8)(v_stack_m12F) * 2) + ((unsigned __int8)(v_stack_m12F) + (unsigned __int8)(v_stack_m12F) * 2);
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m128 + a1 * 8 + 72))) | (*(unsigned int *)(v_stack_m128 + a1 * 8 + 76)));
    v_r11 = (unsigned int)((1) << ((unsigned __int8)((unsigned __int8)(*(unsigned __int8 *)((unsigned int)((unsigned int)(v_rdi)) + (unsigned int)((unsigned int)(v_rdi)) * 4 + 32)))));
    if ((((unsigned int)(a2)) & ((unsigned int)(v_r11))) != 0) goto loc_0025A2C4;
loc_0025A295:
    v_r10 = (unsigned __int8)((v_stack_m12F) + 1);
    v_stack_m12E = (unsigned __int8)(v_r10);
    if (((unsigned int)((unsigned __int8)(v_r10))) >= ((unsigned int)((unsigned int)(v_stack_m138)))) {
        v_r10 = 0;
        v_stack_m12E = 0;
    }
    a1 = (0 + 0 * 2) + (0 + 0 * 2);
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m128 + a1 * 8 + 72))) | (*(unsigned int *)(v_stack_m128 + a1 * 8 + 76)));
    if ((((unsigned int)(a2)) & ((unsigned int)(v_r11))) == 0) goto loc_0025A295;
loc_0025A2C4:
    a2 = 0;
    a1 = (0 + 0 * 2) << (4);
    a3 = (v_stack_m108) + (a1);
    v_stack_m12D = 0;
    if (!(condition_is_above_or_equal)) {
        a2 = 1;
        v_stack_m12D = (unsigned __int8)(a2);
    }
    if (!(condition_is_above_or_equal)) {
        a2 = (unsigned __int8)((a2) | (2));
        v_stack_m12D = (unsigned __int8)(a2);
    }
    if ((((unsigned int)((unsigned __int8)(a2))) & ((unsigned int)((unsigned __int8)(a2) - 1))) != 0) goto loc_0025ADCC;
    v_stack_m198 = (unsigned int)((unsigned __int8)(a2) - 1);
loc_0025A31C:
    v_stack_m12C = (unsigned __int8)((unsigned __int8)(a2) - 1);
    if ((unsigned __int8)((unsigned __int8)(a2) - 1) == 0) goto loc_0025AC2A;
    if (((unsigned int)((unsigned __int8)((unsigned __int8)(a2) - 1))) != 1) goto loc_0025A342;
    result = ((unsigned __int8)(*(unsigned __int8 *)((unsigned int)((unsigned int)(v_rdi)) + (unsigned int)((unsigned int)(v_rdi)) * 4 + 32))) + (4);
    result = (result) << (4);
    result = (result) + (*(unsigned __int64 *)(a3 + 8));
loc_0025A33E:
    v_stack_m118 = result;
loc_0025A342:
    v_stack_m110 = v_stack_m118;
    goto loc_0025A401;
loc_0025A34F:
    a2 = 0;
    if (a3 == 0) goto loc_0025A3B4;
loc_0025A360:
    a1 = (0 + 0 * 2) + (0 + 0 * 2);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m128 + a1 * 8 + 64))) == 0) goto loc_0025A3A5;
    result = (*(unsigned __int64 *)(v_stack_m128 + a1 * 8 + 32)) + (0x8430ULL);
    if ((((unsigned __int8)(*(unsigned __int64 *)(result + 8))) & (1)) != 0) goto loc_0025A5D5;
loc_0025A390:
    if (*(unsigned __int64 *)(result + 8) != 0) goto loc_0025AC40;
loc_0025A399:
loc_0025A39C:
    *(unsigned __int64 *)(v_stack_m128 + a1 * 8 + 48) = v_rdi;
loc_0025A3A5:
    a2 = (unsigned __int8)((a2) + 1);
    if (((unsigned int)((unsigned __int8)(a2))) < ((unsigned int)((unsigned int)(v_stack_m138)))) goto loc_0025A360;
loc_0025A3B4:
    v_rbx = 0;
loc_0025A3C0:
    a1 = ((unsigned __int8)((unsigned __int8)(v_stack_m12F)) + (unsigned __int8)((unsigned __int8)(v_stack_m12F)) * 2) + ((unsigned __int8)((unsigned __int8)(v_stack_m12F)) + (unsigned __int8)((unsigned __int8)(v_stack_m12F)) * 2);
    if (*(unsigned __int64 *)(v_stack_m128 + a1 * 8 + 48) != 0) goto loc_0025AC53;
loc_0025A3D8:
    a2 = (unsigned __int8)(((unsigned __int8)(v_stack_m12F)) + 1);
    a2 = (unsigned __int8)(a2);
    if (((unsigned int)((unsigned __int8)(a2))) >= ((unsigned int)((unsigned int)(v_stack_m138)))) { a2 = (unsigned int)(v_rdi); }
    if (((unsigned __int8)(a2)) != ((unsigned __int8)(v_stack_m12F))) goto loc_0025A3C0;
    if (v_rdi != 0) goto loc_0025AC67;
loc_0025A3F4:
    v_rsi = (unsigned __int8)((1) + 1);
    if (((unsigned __int8)(v_rsi)) < 4) goto loc_0025A230;
loc_0025A401:
    v_stack_m12B = (unsigned __int8)(v_rsi);
    if (((unsigned __int8)(v_rsi)) == 4) goto loc_0025A84D;
loc_0025A40F:
    v_stack_m110 = *(unsigned __int64 *)(v_stack_m110);
    if ((*(unsigned __int64 *)(v_stack_m110)) == v_stack_m118) goto loc_0025A83C;
    v_rsi = (*(unsigned __int64 *)(v_stack_m110)) + (-216);
    a1 = (v_stack_m12E + v_stack_m12E * 2) + (v_stack_m12E + v_stack_m12E * 2);
    v_stack_m1D0 = *(unsigned __int64 *)(v_stack_m128 + a1 * 8 + 32);
    if (v_stack_m12B == 2) goto loc_0025AD54;
    if (v_stack_m12C != 1) goto loc_0025AB60;
loc_0025A459:
    v_stack_m1E8 = *(unsigned __int64 *)(v_stack_m128 + a1 * 8 + 40);
loc_0025A461:
    if ((*(unsigned __int64 *)(v_rsi + 568)) != (*(unsigned __int64 *)(v_rip + 14075792))) goto loc_0025AD03;
loc_0025A475:
    if (v_rdi == 0) goto loc_0025A734;
loc_0025A47E:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsi + 120))) >> (1));
    a1 = (unsigned int)((a1) & (1));
    if (((unsigned int)(a1)) > (*(unsigned int *)(*(unsigned __int64 *)(a1 + 14312) + 8))) goto loc_0025A20D;
    if (((unsigned int)(a1)) < ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 14312) + 4))))) { a1 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 14312) + 4))); }
    if ((unsigned int)(a1) != 0) goto loc_0025B27D;
loc_0025A4A4:
    if (((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) >= ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312))))) goto loc_0025A20D;
    v_stack_m1E0 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) * 4 * 8 + 16);
    if ((*(unsigned int *)(v_rip + 14069289)) == ((unsigned int)(v_rdi))) goto loc_0025A4D8;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) * 4 * 8 + 16) + 35)) & (32)) != 0) goto loc_0025ACC5;
loc_0025A4D8:
    if (*(unsigned __int64 *)(v_stack_m128 + a1 * 8 + 40) == 0) goto loc_0025ACDF;
loc_0025A4E1:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) * 4 * 8 + 24) == 0) goto loc_0025A5C3;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) * 4 * 8 + 24)) != (*(unsigned __int64 *)(v_stack_m128 + a1 * 8 + 40))) goto loc_0025A5C3;
    result = KiComputeThreadQos(v_rsi, v_rdi, (unsigned int)(v_stack_m138), *(unsigned __int64 *)(v_stack_m128 + a1 * 8 + 40));
    a3 = (unsigned int)(*(unsigned int *)(v_rsi + 80));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi + 80)))) <= ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi + 84))))) { a3 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsi + 84))); }
    a2 = (a3 >= (*(unsigned int *)(v_rip + 14069336))) ? 1 : 0;
    a3 = (unsigned int)((a2 + result * 2) * ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) * 4 * 8 + 16) + 192) + 185))));
    a3 = (unsigned int)((a3) + ((unsigned int)(*(unsigned __int8 *)(v_rsi + 517))));
    a3 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) * 4 * 8 + 16) + 192) + 192) + a3 + a3 * 2 * 8 + 8)) & (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) * 4 * 8 + 16) + 192) + 192) + a3 + a3 * 2 * 8 + 16));
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) * 4 * 8 + 16) + 192) + 192) + a3 + a3 * 2 * 8)) & (a3);
    v_stack_m180 = a2;
    v_stack_m178 = a3;
    v_stack_m170 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) * 4 * 8 + 16) + 192) + 192) + a3 + a3 * 2 * 8 + 16);
    v_stack_m158 = v_xmm0;
    v_stack_m148 = v_xmm1;
    if (((*(unsigned __int64 *)(v_stack_m1E0 + 200)) & (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) * 4 * 8 + 16) + 192) + 192) + a3 + a3 * 2 * 8 + 16))) == 0) goto loc_0025ADAF;
loc_0025A58C:
    if (v_stack_m1E0 != v_stack_m1D0) goto loc_0025AB68;
loc_0025A597:
    v_stack_m168 = v_rdi;
    if ((*(unsigned __int8 *)(v_rip + 14075166)) == ((unsigned __int8)(v_rdi))) goto loc_0025AEDC;
    a3 = 0;
    result = KiEvaluateGroupSchedulingPreemption(*(unsigned __int64 *)(a1 + 14312) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) * 4 * 8 + 16, v_rsi, a3, v_stack_m168);
    if ((unsigned __int8)(result) != 0) goto loc_0025A978;
loc_0025A5C3:
    v_r12 = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) + 1);
    goto loc_0025A4A4;
loc_0025A5D5:
    if (0 == 1) goto loc_0025A399;
    result = (result) | (1);
    result = (result) ^ (0);
    goto loc_0025A390;
loc_0025A5EB:
    v_stack_m1A8 = (unsigned int)(v_rdi);
    if (condition_is_above_or_equal) goto loc_00259F31;
loc_0025A5FF:
    if (((unsigned int)(*(unsigned __int64 *)(a1 + 14312) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) * 4 * 8 + 16)) != 2) goto loc_0025A3F4;
    v_stack_m134 = (unsigned int)((unsigned int)((unsigned int)(v_rdi)));
    if (0 != 0) goto loc_0025A80A;
loc_0025A616:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) & (1));
    v_stack_m134 = (unsigned int)(result);
    if (condition_is_equal) goto loc_0025A3F4;
    v_stack_m12E = (unsigned __int8)(v_stack_m12F);
    v_stack_m130 = (unsigned __int8)(v_stack_m1E8);
    v_stack_m1A4 = (unsigned int)(v_stack_m1E8);
    a1 = ((unsigned __int8)(v_stack_m12F) + (unsigned __int8)(v_stack_m12F) * 2) + ((unsigned __int8)(v_stack_m12F) + (unsigned __int8)(v_stack_m12F) * 2);
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m128 + a1 * 8 + 72))) | (*(unsigned int *)(v_stack_m128 + a1 * 8 + 76)));
    v_r11 = (unsigned int)((1) << ((unsigned __int8)((unsigned __int8)(v_stack_m1E8))));
    if ((((unsigned int)(a2)) & ((unsigned int)(v_r11))) != 0) goto loc_0025A686;
loc_0025A657:
    v_r10 = (unsigned __int8)((v_stack_m12F) + 1);
    v_stack_m12E = (unsigned __int8)(v_r10);
    if (((unsigned int)((unsigned __int8)(v_r10))) >= 0) {
        v_r10 = 0;
        v_stack_m12E = 0;
    }
    a1 = (0 + 0 * 2) + (0 + 0 * 2);
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m128 + a1 * 8 + 72))) | (*(unsigned int *)(v_stack_m128 + a1 * 8 + 76)));
    if ((((unsigned int)(v_r11)) & ((unsigned int)(a2))) == 0) goto loc_0025A657;
loc_0025A686:
    a2 = 0;
    a1 = (0 + 0 * 2) << (4);
    a3 = (v_stack_m108) + (a1);
    v_stack_m12D = 0;
    if (!(condition_is_above_or_equal)) {
        a2 = 1;
        v_stack_m12D = (unsigned __int8)(a2);
    }
    if (!(condition_is_above_or_equal)) {
        a2 = (unsigned __int8)((a2) | (2));
        v_stack_m12D = (unsigned __int8)(a2);
    }
    if ((((unsigned int)((unsigned __int8)(a2))) & ((unsigned int)((unsigned __int8)(a2) - 1))) != 0) goto loc_0025AEAB;
    v_stack_m1A0 = (unsigned int)((unsigned __int8)(a2) - 1);
loc_0025A6DE:
    v_stack_m12C = (unsigned __int8)((unsigned __int8)(a2) - 1);
    if ((unsigned __int8)((unsigned __int8)(a2) - 1) == 0) goto loc_0025ACED;
    if (((unsigned int)((unsigned __int8)((unsigned __int8)(a2) - 1))) != 1) goto loc_0025A704;
    result = ((unsigned __int8)(v_stack_m1E8)) + (4);
    result = (result) << (4);
    result = (result) + (*(unsigned __int64 *)(a3 + 8));
loc_0025A700:
    v_stack_m118 = result;
loc_0025A704:
    v_stack_m110 = v_stack_m118;
    goto loc_0025A401;
loc_0025A711:
loc_0025A718:
    result = (unsigned int)((v_stack_m118) | (*(unsigned int *)(v_stack_mDC - 4)));
    v_stack_m134 = (unsigned int)(result);
    result = (unsigned int)((result) | (*(unsigned int *)(v_stack_mDC + 48 - 48)));
    v_stack_m134 = (unsigned int)(result);
    a2 = ((unsigned int)(a3)) - (1);
    if (condition_is_equal) goto loc_0025A254;
    goto loc_0025A718;
loc_0025A734:
    if (*(unsigned __int64 *)(v_rsi + 104) == 0) goto loc_0025A47E;
    a1 = ((unsigned int)(*(unsigned int *)(v_stack_m1D0 + 216))) + (*(unsigned __int64 *)(v_rsi + 104));
    if (condition_is_equal) goto loc_0025A47E;
    if ((*(unsigned __int8 *)(v_rsi + 195)) >= 16) goto loc_0025A47E;
    if (((*(unsigned int *)(v_rsi + 120)) & (512)) != 0) goto loc_0025A47E;
    if ((*(unsigned int *)(v_rsi + 484)) != ((unsigned int)(v_rdi))) goto loc_0025A47E;
    if ((*(unsigned __int8 *)(v_rsi + 390)) == 1) goto loc_0025A47E;
loc_0025A790:
    if (((*(unsigned __int8 *)(a1 + 112)) & (2)) != 0) goto loc_0025A7BD;
    if (*(unsigned __int64 *)(a1 + 416) != 0) goto loc_0025A790;
loc_0025A7A2:
    a3 = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) + (*(unsigned int *)(a1 + 124)));
    if (condition_is_not_equal) goto loc_0025A7B4;
    if (*(unsigned __int64 *)(a1 + 416) != 0) goto loc_0025A7A2;
loc_0025A7B4:
    if (a3 == 0) goto loc_0025A47E;
loc_0025A7BD:
    result = KiRemoveCurrentlyEnumeratedThreadFromReadyQueue(v_stack_m138, v_rsi, a3, v_stack_m1E8);
    a4 = 0;
    *(unsigned int *)(v_rsi + 536) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m1D0 + 36)));
    result = KiAddThreadToScbQueue(v_stack_m1D0, a1, v_rsi, a4);
    if (((*(unsigned int *)(v_rip + 14074663)) & (0x800ULL)) == 0) goto loc_0025A20D;
    a4 = 0;
    result = EtwTraceReadyQueueInsertion(v_rsi, (unsigned int)(*(unsigned int *)(v_stack_m1D0 + 36)), a4 + 2, a4);
    goto loc_0025A20D;
loc_0025A80A:
loc_0025A811:
    result = (unsigned int)((result) | (*(unsigned int *)(v_stack_mDC - 4)));
    v_stack_m134 = (unsigned int)(result);
    result = (unsigned int)((result) | (*(unsigned int *)(v_stack_mDC + 48 - 48)));
    v_stack_m134 = (unsigned int)(result);
    a2 = ((unsigned int)((unsigned int)(a4 + 2))) - (1);
    if (condition_is_equal) goto loc_0025A616;
    goto loc_0025A811;
loc_0025A82D:
    result = KxWaitForLockOwnerShip(v_stack_mDC + 48, a2, a4 + 2, a4);
    v_rsi = (unsigned int)((v_rsi) + 1);
    goto loc_00259EC0;
loc_0025A83C:
    result = KiAdvanceReadyQueueEnumeratorToNextList(v_stack_m138, a2, v_stack_m1D0, a4);
    if (!sign_flag) goto loc_0025A40F;
loc_0025A84D:
loc_0025A853:
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312))) == 0) goto loc_0025A88C;
loc_0025A864:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 24)) <= v_rdi) goto loc_0025A879;
    if (v_rdi == 0) goto loc_0025A876;
    v_rbx = v_rdi;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 24)) < v_rdi) {
        v_rbx = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 24);
    }
    a1 = (*(unsigned __int64 *)(a1 + 14312) + 24) + (40);
    a2 = ((unsigned int)((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312))))) - (1);
    if (condition_is_not_equal) goto loc_0025A864;
    if (v_rbx != 0) goto loc_0025AE43;
loc_0025A88C:
loc_0025A891:
    v_r12 = 0;
    v_rsi = (unsigned int)((unsigned int)(v_rdi));
    if (((*(unsigned int *)(v_rip + 14074484)) & (0x400ULL)) != 0) { v_rsi = 2; }
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312))) <= ((unsigned __int8)(v_rdi))) goto loc_0025A8E2;
loc_0025A8B4:
    a1 = ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) * 4 + 2) + ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))));
    result = KiCommitRescheduleContextEntry(*(unsigned __int64 *)(a1 + 14312) + a1 * 8, v_stack_m1C8, (unsigned int)((unsigned int)(v_rsi)), v_stack_m1D8);
    v_r12 = (unsigned __int8)((v_r12) | ((unsigned __int8)(result)));
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) + 1);
    if (((unsigned int)(v_rbx)) < ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312))))) goto loc_0025A8B4;
    v_rdi = 0;
loc_0025A8E2:
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 14312) + 8)) != 1) goto loc_0025A905;
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 16) + 36440) + 1)) + 1);
    *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 16) + 36440) + 1) = (unsigned __int8)(result);
    if (((unsigned __int8)(result)) >= (*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 16) + 36440)))) {
        *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 16) + 36440) + 1) = 0;
    }
    a4 = (*(unsigned __int64 *)(v_stack_m1B0)) & (-2);
    v_stack_m1B0 = a4;
    a1 = (unsigned int)((*(unsigned __int64 *)(v_stack_m1B0)) & (1));
    if (condition_is_equal) goto loc_0025AE34;
    if (((unsigned int)(a1)) == 1) {
        result = *(unsigned __int64 *)(a4 + 36440);
        a3 = *(unsigned __int64 *)(a4 + 36440);
        a3 = (a3) + (8);
        a2 = *(unsigned __int8 *)(result);
    }
    if ((unsigned int)(a2) == 0) goto loc_00259FF8;
loc_0025A950:
    if ((unsigned int)(a2 - 1) != 0) goto loc_0025A950;
    goto loc_00259FF8;
loc_0025A968:
    if ((((unsigned __int8)(a2 - 1)) & (16)) == 0) goto loc_0025A5C3;
    if ((unsigned __int8)(*(unsigned __int64 *)(a3 + a2 - 1 * 8)) == 0) goto loc_0025A5C3;
loc_0025A978:
loc_0025A97C:
    if (*(unsigned __int64 *)(v_stack_m1F0 + 16) == 0) goto loc_0025A20D;
    a1 = (v_stack_m12E + v_stack_m12E * 2) + (v_stack_m12E + v_stack_m12E * 2);
    if (v_stack_m12B == 2) goto loc_0025ADE0;
    v_stack_m110 = *(unsigned __int64 *)(v_stack_m110 + 8);
    if ((unsigned int)(v_stack_m12C) == 0) goto loc_0025ABB3;
    if (((unsigned int)(v_stack_m12C)) != 1) goto loc_0025AA33;
    if ((((unsigned int)(v_stack_m12D)) & ((unsigned int)(v_stack_m12D - 1))) != 0) {
    }
    if (((*(unsigned int *)(v_rsi + 120)) & (0x400000ULL)) != 0) goto loc_0025AF13;
loc_0025A9F3:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 216) + 8)) != (v_rsi + 216)) goto loc_0025AA09;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 216 + 8))) == (v_rsi + 216)) goto loc_0025AB3C;
loc_0025AA09:
loc_0025AA10:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 216 + 8))) == (v_rsi + 216)) goto loc_0025AB1E;
loc_0025AA1B:
loc_0025AA2B:
    a3 = 0;
    result = KiUpdateSoftParkElectionStatisticsOnRemoval(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m128 + a1 * 8 + 32) + 36424), v_rsi, a3, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m128 + a1 * 8 + 32) + 36424));
loc_0025AA33:
loc_0025AA40:
    if (0 >= ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312))))) goto loc_0025AA5E;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16)) == (*(unsigned __int64 *)(v_stack_m1F0 + 16))) goto loc_0025AA5A;
    a2 = (unsigned int)((0) + 1);
    goto loc_0025AA40;
loc_0025AA5A:
loc_0025AA5E:
    v_r10 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsi + 120))) >> (1));
    result = (unsigned int)((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16 + 32)) >> (1));
    v_r10 = (unsigned int)((v_r10) & (1));
    result = (unsigned int)((result) & (1));
    if (((unsigned int)(v_r10)) >= ((unsigned int)(result))) goto loc_0025AF75;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312))) <= 0) goto loc_0025AFD2;
loc_0025AA8C:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16)) == (*(unsigned __int64 *)(v_stack_m1F0 + 16))) goto loc_0025B120;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 40) - 1) <= -4) goto loc_0025B31C;
loc_0025AABB:
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 48)) | (1));
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 32) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16) + 24);
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 48) = (unsigned __int8)(result);
    result = (unsigned __int8)((result) & (253));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16) + 24) + 120))) >> (1));
    a1 = (unsigned __int8)((a1) & (1));
    a1 = (unsigned __int8)((a1) + ((unsigned __int8)(a1)));
    a1 = (unsigned __int8)((a1) ^ ((unsigned __int8)(result)));
    a1 = (unsigned __int8)((a1) & (231));
    a1 = (unsigned __int8)((a1) | (4));
    a1 = (unsigned __int8)((a1) & (223));
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 48) = (unsigned __int8)(a1);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 40) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16) + 24);
    result = KiIsPrcbThread(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16) + 24), a2, *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312)), *(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8);
    if ((unsigned __int8)(result) == 0) {
        result = *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16) + 36);
        *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16) + 24) + 536) = (unsigned int)(result);
    }
    v_rbx = (unsigned int)((0) + 1);
    if (((unsigned int)(v_rbx)) < ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312))))) goto loc_0025AA8C;
loc_0025AB14:
    goto loc_0025AFD2;
loc_0025AB1E:
    a2 = ~(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 712));
    goto loc_0025AA1B;
loc_0025AB3C:
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 720)) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16) + 24);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16) + 24) + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 720);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 720)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16) + 24))) goto loc_0025AA10;
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 8) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 8)));
    goto loc_0025AA10;
loc_0025AB60:
    goto loc_0025A459;
loc_0025AB68:
    if (*(unsigned __int64 *)(v_rsi + 104) == 0) goto loc_0025A597;
    a2 = ((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 8)) + 216))) + (*(unsigned __int64 *)(v_rsi + 104));
    result = KiIsThreadConstrainedBySchedulingGroup(v_rsi, a2, *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312)), 0);
    if ((unsigned __int8)(result) == 0) goto loc_0025A597;
    result = KiCheckForMaxOverQuotaScb(a2, a2, *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312)), 0);
    if ((unsigned __int8)(result) == 0) goto loc_0025A597;
    result = KiShouldPreemptionBeDeferred(v_rsi, a2, *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312)), 0);
    if ((unsigned __int8)(result) != 0) goto loc_0025A597;
    goto loc_0025A5C3;
loc_0025ABB3:
    if ((((unsigned int)(v_stack_m12D)) & ((unsigned int)(v_stack_m12D - 1))) != 0) {
    }
    if (((*(unsigned int *)(a2 - 96)) & (0x400000ULL)) != 0) goto loc_0025B108;
loc_0025ABD3:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a2) + 8)) != a2) goto loc_0025AA09;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 8))) != a2) goto loc_0025AA09;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 8)) = *(unsigned __int64 *)(a2);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2) + 8) = *(unsigned __int64 *)(a2 + 8);
    if ((*(unsigned __int64 *)(a2 + 8)) == (*(unsigned __int64 *)(a2))) goto loc_0025AD3C;
loc_0025ABFD:
    if ((*(unsigned __int64 *)(a2 + 8)) == (*(unsigned __int64 *)(a2))) goto loc_0025AD65;
loc_0025AC0A:
    a2 = (a2) + (-216);
    goto loc_0025AA2B;
loc_0025AC2A:
    result = (0) + (0x844ULL);
    result = (result) << (4);
    result = (result) + (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16) + 24));
    goto loc_0025A33E;
loc_0025AC40:
    result = (result) + (-88);
    if ((*(unsigned int *)(result + 124)) > 0) goto loc_0025A399;
    goto loc_0025A39C;
loc_0025AC53:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16) + 24) != 0) goto loc_0025AE21;
loc_0025AC5C:
    goto loc_0025A3D8;
loc_0025AC67:
    v_stack_m12E = (unsigned __int8)((unsigned __int8)(a2));
    v_stack_m120 = 0;
    v_stack_m128 = 0;
    v_stack_m134 = (unsigned int)(*(unsigned __int16 *)(0 + 120));
    a2 = ((unsigned __int8)((unsigned __int8)(a2)) + (unsigned __int8)((unsigned __int8)(a2)) * 2) + ((unsigned __int8)((unsigned __int8)(a2)) + (unsigned __int8)((unsigned __int8)(a2)) * 2);
    result = (unsigned int)(*(unsigned int *)(v_stack_m128 + a2 * 8 + 64));
    if ((*(unsigned int *)(0 + 124)) == ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m128 + a2 * 8 + 64))))) {
        result = *(unsigned int *)(v_stack_m128 + a2 * 8 + 68);
        result = (unsigned int)((result) & ((unsigned int)(*(unsigned __int16 *)(0 + 120))));
        a1 = (unsigned int)(result);
        v_stack_m134 = (unsigned int)(result);
    }
    if ((unsigned int)(a1) == 0) goto loc_0025AD90;
loc_0025ACA1:
    a1 = ((unsigned __int8)(result)) + (9);
    v_stack_m190 = (unsigned int)(result);
    a1 = (a1) << (4);
    a1 = (a1) + (0);
    v_stack_m130 = (unsigned __int8)(result);
    v_stack_m118 = a1;
    v_stack_m110 = a1;
    goto loc_0025A401;
loc_0025ACC5:
    result = KiIsThreadExemptFromForcePark(v_rsi, a2, *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312)), 0);
    if ((unsigned __int8)(result) == 0) goto loc_0025A5C3;
    goto loc_0025A4D8;
loc_0025ACDF:
    if (v_stack_m1E0 != ((unsigned __int8)(a2))) goto loc_0025A4E1;
    goto loc_0025A597;
loc_0025ACED:
    result = (0) + (0x844ULL);
    result = (result) << (4);
    result = (result) + (v_r10);
    goto loc_0025A700;
loc_0025AD03:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rsi + 116)))) & (8)) != 0) goto loc_0025A475;
    result = KiRemoveCurrentlyEnumeratedThreadFromReadyQueue(v_stack_m138, v_rsi, *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312)), 0);
    result = KiEnterDeferredReadyState(v_rsi, v_rsi, *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312)), 0);
    *(unsigned __int64 *)(v_rsi + 216) = *(unsigned __int64 *)(v_stack_m1D8);
    *(unsigned __int64 *)(v_stack_m1D8) = v_rsi + 216;
    goto loc_0025A20D;
loc_0025AD3C:
    *(unsigned int *)((unsigned __int8)(a2) + 33752) = (unsigned int)((unsigned int)(*(unsigned int *)((unsigned __int8)(a2) + 33752)));
    goto loc_0025ABFD;
loc_0025AD54:
    v_stack_m1E8 = 0;
    goto loc_0025A461;
loc_0025AD65:
    if ((*(unsigned __int64 *)((unsigned __int8)(a2) + 33840)) != 0) goto loc_0025AC0A;
    a1 = ~(*(unsigned __int64 *)((unsigned __int8)(a2) + 200));
    goto loc_0025AC0A;
loc_0025AD90:
    result = KiAdvanceReadyQueueEnumeratorToNextScb(v_stack_m138, v_stack_m128, *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312)), 0);
    if (!sign_flag) goto loc_0025AEBF;
    goto loc_0025A3F4;
loc_0025ADAF:
    result = (*(unsigned __int64 *)(v_stack_m1E8 + 712)) & (v_stack_m128);
    if (((0) & (result)) != 0) goto loc_0025A5C3;
    goto loc_0025A58C;
loc_0025ADCC:
    result = (condition_is_above_or_equal) ? 1 : 0;
    goto loc_0025A31C;
loc_0025ADE0:
    v_stack_m1E0 = v_stack_m128;
    if ((*(unsigned __int64 *)(v_stack_m128)) != v_stack_m118) goto loc_0025AECB;
    if ((*(unsigned __int64 *)(v_stack_m128 + 8)) != v_stack_m118) goto loc_0025AECB;
    result = KiAdvanceReadyQueueEnumeratorToNextList(v_stack_m138, v_stack_m128, (unsigned int)(v_stack_m138), 0);
loc_0025AE09:
    result = KiRemoveThreadFromScbQueue((unsigned __int8)(a2), v_stack_m1E0, v_rsi, (unsigned int)((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16))));
    goto loc_0025AA33;
loc_0025AE21:
    if ((*(unsigned int *)(0 + 124)) >= ((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16))) + 124))))) goto loc_0025A3D8;
    goto loc_0025AC5C;
loc_0025AE34:
    goto loc_0025A950;
loc_0025AE43:
    v_rsi = ((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_m1F0 + 16)))) + (11);
    v_rsi = (v_rsi) << (4);
    v_rsi = (v_rsi) + (*(unsigned __int64 *)(a1 + 14312));
    if (((*(unsigned int *)(v_rip + 14073053)) & (0x200000ULL)) == 0) goto loc_0025AEA5;
    if (*(unsigned __int64 *)(v_rsi) != 0) goto loc_0025AE7E;
    if (*(unsigned __int64 *)(v_rsi) == 0) goto loc_0025AE9A;
    result = KxWaitForLockChainValid(v_rsi, 1, v_stack_m1B0, (unsigned int)((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16))));
loc_0025AE7E:
    *(unsigned __int64 *)(v_rsi) = 0;
    result = (unsigned __int8)((*(unsigned __int64 *)(v_rsi + 8)) ^ ((unsigned __int8)(*(unsigned __int64 *)(v_rsi + 8))));
    if ((((unsigned __int8)(result)) & (4)) != 0) {
        result = KeWakeAddressAll(result + 8, *(unsigned __int64 *)(v_rsi + 8), v_stack_m1B0, (unsigned int)((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16))));
    }
    v_r12 = (unsigned int)((*(unsigned __int64 *)(v_stack_m1F0 + 16)) + 1);
    goto loc_0025A853;
loc_0025AEA5:
    goto loc_0025AE9A;
loc_0025AEAB:
    result = (condition_is_above_or_equal) ? 1 : 0;
    goto loc_0025A6DE;
loc_0025AEBF:
    goto loc_0025ACA1;
loc_0025AECB:
    v_stack_m110 = *(unsigned __int64 *)(v_stack_m110 + 8);
    goto loc_0025AE09;
loc_0025AEDC:
    if ((((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16) + 48))) & (1)) != 0) goto loc_0025A978;
    if (((unsigned __int8)(*(unsigned __int8 *)(v_rsi + 195))) > (*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16) + 32) + 195))) goto loc_0025A978;
    if (((unsigned __int8)(*(unsigned __int8 *)(v_rsi + 195))) != (*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16) + 32) + 195))) goto loc_0025A968;
    if ((((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16) + 48))) & (24)) != 0) goto loc_0025A978;
    goto loc_0025A968;
loc_0025AF13:
    goto loc_0025A9F3;
loc_0025AF2B:
loc_0025AF2E:
    if (0 >= ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312))))) goto loc_0025AF6B;
    a1 = (0 * 4 + 2) + (0);
    if ((*(unsigned __int64 *)(a1 + 14312) + a1 * 8) == ((unsigned __int8)(a2))) goto loc_0025AF66;
    a4 = 0;
    result = KiDoesThreadDominateRescheduleContextEntry(*(unsigned __int64 *)(a1 + 14312) + a1 * 8, v_stack_m1F0, (unsigned int)((unsigned int)(v_rsi)), a4);
    if ((unsigned __int8)(result) == 0) goto loc_00259FF2;
loc_0025AF66:
    v_r13 = (unsigned int)((0) + 1);
    goto loc_0025AF2E;
loc_0025AF6B:
    goto loc_00259DBF;
loc_0025AF75:
    if ((unsigned int)(v_stack_m12F) != 0) goto loc_0025B178;
    if ((*(unsigned __int64 *)(a4 + 24) - 1) <= -4) goto loc_0025AFDB;
loc_0025AF8F:
    a1 = (unsigned __int8)((*(unsigned __int8 *)(a4 + 32)) & (254));
    *(unsigned __int64 *)(a4 + 16) = v_rsi;
    *(unsigned __int8 *)(a4 + 32) = (unsigned __int8)(a1);
    a1 = (unsigned __int8)((a1) & (253));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsi + 120))) >> (1));
    result = (unsigned __int8)((result) & (1));
    *(unsigned __int64 *)(a4 + 24) = v_rsi;
    result = (unsigned __int8)((result) + ((unsigned __int8)(result)));
    result = (unsigned __int8)((result) ^ ((unsigned __int8)(a1)));
    result = (unsigned __int8)((result) & (199));
    result = (unsigned __int8)((result) | (4));
    *(unsigned __int8 *)(a4 + 32) = (unsigned __int8)(result);
    if ((*(unsigned __int64 *)(v_rsi + 544)) != (v_rip + 14110523)) goto loc_0025B670;
loc_0025AFD2:
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 14312) + 4) = (unsigned int)(v_stack_m12F);
    goto loc_0025A1F0;
loc_0025AFDB:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 24) + 544)) == (v_rip + 14110494)) goto loc_0025AF8F;
    if (((*(unsigned __int8 *)(a4 + 33)) & (1)) != 0) {
    }
    *(unsigned __int8 *)(*(unsigned __int64 *)(a4 + 24) + 565) = 1;
    result = KiInsertDeferredReadyList(v_stack_m1D8, *(unsigned __int64 *)(a4 + 24), (unsigned int)((unsigned int)(v_rsi)), a4);
    goto loc_0025AF8F;
loc_0025B009:
    if (result <= -4) goto loc_0025B2ED;
loc_0025B013:
    a1 = (unsigned __int8)((*(unsigned __int8 *)(a4 + 48)) & (254));
    *(unsigned __int64 *)(a4 + 32) = v_stack_m12F;
    *(unsigned __int8 *)(a4 + 48) = (unsigned __int8)(a1);
    a1 = (unsigned __int8)((a1) & (253));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m12F + 120))) >> (1));
    result = (unsigned __int8)((result) & (1));
    *(unsigned __int64 *)(a4 + 40) = v_stack_m12F;
    result = (unsigned __int8)((result) + ((unsigned __int8)(result)));
    result = (unsigned __int8)((result) ^ ((unsigned __int8)(a1)));
    result = (unsigned __int8)((result) & (199));
    result = (unsigned __int8)((result) | (4));
    *(unsigned __int8 *)(a4 + 48) = (unsigned __int8)(result);
    a1 = (unsigned __int8)(((unsigned __int8)(*(unsigned __int64 *)(a4))) ^ ((unsigned __int8)(*(unsigned __int8 *)(a4 + 49))));
    a1 = (unsigned __int8)((a1) & (1));
    a1 = (unsigned __int8)((a1) ^ ((unsigned __int8)(*(unsigned __int8 *)(a4 + 49))));
    *(unsigned __int8 *)(a4 + 49) = (unsigned __int8)(a1);
    result = KiIsPrcbThread(v_stack_m12F, *(unsigned __int64 *)(a4 + 24), (unsigned int)((unsigned int)(v_rsi)), a4);
    if ((unsigned __int8)(result) != 0) goto loc_00259E9C;
    *(unsigned int *)(v_stack_m12F + 536) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m1F0 + 36)));
    goto loc_00259E9C;
loc_0025B072:
loc_0025B077:
    if (0 >= 0) goto loc_0025B09C;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 32)) == (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16) + 36480))) goto loc_0025B0D5;
loc_0025B09C:
    if (0 == 0) goto loc_00259D1C;
loc_0025B0AC:
    result = *(unsigned __int64 *)(a1 + 14312) + 48 - 32;
    if ((*(unsigned __int64 *)(a1 + 14312) + 48 - 32) != (*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16)) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16 + 16);
        *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 48 - 16) = result;
        result = *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16 + 32);
        result = (unsigned __int8)((result) | (32));
        *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312) + 48) = (unsigned __int8)(result);
    }
    a1 = (*(unsigned __int64 *)(a1 + 14312) + 48) + (40);
    a2 = (0) - (1);
    if (condition_is_not_equal) goto loc_0025B0AC;
    goto loc_00259D1C;
loc_0025B0D5:
    a2 = (unsigned int)((a2) + 1);
    goto loc_0025B077;
loc_0025B0D9:
    result = KiIsPrcbThread(a1, a2, *(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16, a4);
    if ((unsigned __int8)(result) != 0) goto loc_00259E53;
    if (((*(unsigned __int8 *)(a4 + 49)) & (1)) != 0) {
    }
    *(unsigned __int8 *)(a1 + 565) = 1;
    result = KiInsertDeferredReadyList(v_stack_m1C8, a1, *(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16, a4);
    goto loc_00259E53;
loc_0025B108:
    goto loc_0025ABD3;
loc_0025B120:
    if ((*(unsigned __int64 *)(a1 + 752)) <= -4) goto loc_0025B355;
loc_0025B12A:
    a1 = (unsigned __int8)((*(unsigned __int8 *)(a4 + 48)) & (254));
    *(unsigned __int64 *)(a4 + 32) = v_rsi;
    *(unsigned __int8 *)(a4 + 48) = (unsigned __int8)(a1);
    a1 = (unsigned __int8)((a1) & (253));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsi + 120))) >> (1));
    result = (unsigned __int8)((result) & (1));
    *(unsigned __int64 *)(a4 + 40) = v_rsi;
    result = (unsigned __int8)((result) + ((unsigned __int8)(result)));
    result = (unsigned __int8)((result) ^ ((unsigned __int8)(a1)));
    result = (unsigned __int8)((result) & (199));
    result = (unsigned __int8)((result) | (4));
    *(unsigned __int8 *)(a4 + 48) = (unsigned __int8)(result);
    result = KiIsPrcbThread(v_rsi, a1, *(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16, a4);
    if ((unsigned __int8)(result) != 0) goto loc_0025AB06;
    *(unsigned int *)(v_rsi + 536) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m130 + 36)));
    goto loc_0025AB06;
loc_0025B178:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312))) <= 0) goto loc_0025AFD2;
loc_0025B188:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16)) != v_r12) goto loc_0025B203;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 40) - 1) <= -4) goto loc_0025B384;
loc_0025B1AF:
    a1 = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 48)) & (254));
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 32) = v_rsi;
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 48) = (unsigned __int8)(a1);
    a1 = (unsigned __int8)((a1) & (253));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsi + 120))) >> (1));
    result = (unsigned __int8)((result) & (1));
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 40) = v_rsi;
    result = (unsigned __int8)((result) + ((unsigned __int8)(result)));
    result = (unsigned __int8)((result) ^ ((unsigned __int8)(a1)));
    result = (unsigned __int8)((result) & (199));
    result = (unsigned __int8)((result) | (4));
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 48) = (unsigned __int8)(result);
    result = KiIsPrcbThread(v_rsi, a1, *(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16, *(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8);
    if ((unsigned __int8)(result) == 0) {
        result = *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16) + 36);
        *(unsigned int *)(v_rsi + 536) = (unsigned int)(result);
    }
    v_rbx = (unsigned int)((0) + 1);
    if (((unsigned int)(v_rbx)) < ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312))))) goto loc_0025B188;
    goto loc_0025AB14;
loc_0025B203:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312))) <= -4) goto loc_0025B3B3;
loc_0025B214:
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 48)) & (254));
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 32) = v_rsi;
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 48) = (unsigned __int8)(result);
    result = (unsigned __int8)((result) & (253));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsi + 120))) >> (1));
    a1 = (unsigned __int8)((a1) & (1));
    a1 = (unsigned __int8)((a1) + ((unsigned __int8)(a1)));
    a1 = (unsigned __int8)((a1) ^ ((unsigned __int8)(result)));
    a1 = (unsigned __int8)((a1) & (231));
    a1 = (unsigned __int8)((a1) | (4));
    a1 = (unsigned __int8)((a1) | (32));
    result = (unsigned __int8)(((unsigned __int8)(a1)) & (223));
    a1 = (unsigned __int8)(a1);
    if (v_rsi == (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16) + 36480))) { a1 = (unsigned int)((unsigned __int8)(result)); }
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 48) = (unsigned __int8)(a1);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 40) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16) + 36480);
    result = KiIsPrcbThread(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16) + 36480), a1, *(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16, *(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8);
    if ((unsigned __int8)(result) != 0) goto loc_0025B1F4;
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16) + 36480) + 536) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16) + 36)));
    goto loc_0025B1F4;
loc_0025B271:
    result = ~(*(unsigned __int64 *)(a1 + 104));
    goto loc_0025A1AF;
loc_0025B27D:
loc_0025B27F:
    if (0 < ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312))))) goto loc_0025B2C2;
loc_0025B289:
    if (0 >= ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312))))) goto loc_0025A20D;
    result = KiCanLocalReadyThreadBeScheduledToRescheduleContextEntry(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16, v_rsi, v_stack_m1D0, v_stack_m1E8);
    if ((unsigned __int8)(result) != 0) goto loc_0025B34B;
    v_rbx = (unsigned int)((0) + 1);
    goto loc_0025B289;
loc_0025B2C2:
    a4 = 0;
    a3 = 0;
    a1 = ((unsigned int)((unsigned int)(v_rbx)) * 4 + 2) + ((unsigned int)((unsigned int)(v_rbx)));
    result = KiDoesThreadDominateRescheduleContextEntry(*(unsigned __int64 *)(a1 + 14312) + a1 * 8, v_rsi, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0025A20D;
    v_rbx = (unsigned int)((v_rbx) + 1);
    goto loc_0025B27F;
loc_0025B2ED:
    result = KiIsPrcbThread(*(unsigned __int64 *)(a1 + 14312) + a1 * 8, v_rsi, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_0025B013;
    if (((*(unsigned __int8 *)(a4 + 49)) & (1)) != 0) {
    }
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312) + a1 * 8 + 565) = 1;
    result = KiInsertDeferredReadyList(v_stack_m1D8, *(unsigned __int64 *)(a1 + 14312) + a1 * 8, a3, a4);
    goto loc_0025B013;
loc_0025B31C:
    result = KiIsPrcbThread(v_stack_m1D8, *(unsigned __int64 *)(a1 + 14312) + a1 * 8, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_0025AABB;
    if (((*(unsigned __int8 *)(a4 + 49)) & (1)) != 0) {
    }
    *(unsigned __int8 *)(v_stack_m1D8 + 565) = 1;
    result = KiInsertDeferredReadyList(v_stack_m1D8, v_stack_m1D8, a3, a4);
    goto loc_0025AABB;
loc_0025B34B:
    goto loc_0025A97C;
loc_0025B355:
    result = KiIsPrcbThread(v_stack_m1D8, v_stack_m1D8, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_0025B12A;
    if (((*(unsigned __int8 *)(a4 + 49)) & (1)) != 0) {
    }
    *(unsigned __int8 *)(v_stack_m1D8 + 565) = 1;
    result = KiInsertDeferredReadyList(v_stack_m1D8, v_stack_m1D8, a3, a4);
    goto loc_0025B12A;
loc_0025B384:
    result = KiIsPrcbThread(v_stack_m1D8, v_stack_m1D8, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_0025B1AF;
    if (((*(unsigned __int8 *)(a4 + 49)) & (1)) != 0) {
    }
    *(unsigned __int8 *)(v_stack_m1D8 + 565) = 1;
    result = KiInsertDeferredReadyList(v_stack_m1D8, v_stack_m1D8, a3, a4);
    goto loc_0025B1AF;
loc_0025B3B3:
    result = KiIsPrcbThread(v_stack_m1D8, v_stack_m1D8, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_0025B214;
    if (((*(unsigned __int8 *)(a4 + 49)) & (1)) != 0) {
    }
    *(unsigned __int8 *)(v_stack_m1D8 + 565) = 1;
    result = KiInsertDeferredReadyList(v_stack_m1D8, v_stack_m1D8, a3, a4);
    goto loc_0025B214;
loc_0025B3E2:
    if ((unsigned int)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8) != 0) goto loc_0025B481;
    if ((*(unsigned __int64 *)(a4 + 24) - 1) <= -4) goto loc_0025B45A;
loc_0025B403:
    result = (unsigned __int8)((*(unsigned __int8 *)(a4 + 32)) & (254));
    *(unsigned __int64 *)(a4 + 16) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16) + 36480);
    *(unsigned __int8 *)(a4 + 32) = (unsigned __int8)(result);
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16) + 36480) + 120))) >> (1));
    a1 = (unsigned __int8)((a1) + ((unsigned __int8)(a1)));
    *(unsigned __int64 *)(a4 + 24) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16) + 36480);
    a1 = (unsigned __int8)((a1) ^ ((unsigned __int8)(result)));
    a1 = (unsigned __int8)((a1) & (2));
    a1 = (unsigned __int8)((a1) ^ ((unsigned __int8)(result)));
    a1 = (unsigned __int8)((a1) | (4));
    a1 = (unsigned __int8)((a1) & (199));
    *(unsigned __int8 *)(a4 + 32) = (unsigned __int8)(a1);
    a1 = (unsigned __int8)((v_stack_m1F8) ^ ((unsigned __int8)(*(unsigned __int8 *)(a4 + 33))));
    a1 = (unsigned __int8)((a1) & (1));
    a1 = (unsigned __int8)((a1) ^ ((unsigned __int8)(*(unsigned __int8 *)(a4 + 33))));
    *(unsigned __int8 *)(a4 + 33) = (unsigned __int8)(a1);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16) + 36480) + 544)) != (v_rip + 14109450)) goto loc_0025B67F;
loc_0025B451:
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 14312) + 4) = (unsigned int)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8);
    goto loc_0025A891;
loc_0025B45A:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 24) + 544)) == (v_rip + 14109450)) goto loc_0025B403;
    if (((*(unsigned __int8 *)(a4 + 33)) & (1)) != 0) {
    }
    *(unsigned __int8 *)(*(unsigned __int64 *)(a4 + 24) + 565) = 1;
    result = KiInsertDeferredReadyList(v_stack_m1D8, *(unsigned __int64 *)(a4 + 24), a3, a4);
    goto loc_0025B403;
loc_0025B481:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312))) <= 0) goto loc_0025B451;
loc_0025B493:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16))) goto loc_0025B52B;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 40) - 1) <= -4) goto loc_0025B5A3;
loc_0025B4BA:
    a1 = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 48)) & (254));
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 32) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16) + 36480);
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 48) = (unsigned __int8)(a1);
    a1 = (unsigned __int8)((a1) & (253));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16) + 36480) + 120))) >> (1));
    result = (unsigned __int8)((result) & (1));
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 40) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16) + 36480);
    result = (unsigned __int8)((result) + ((unsigned __int8)(result)));
    result = (unsigned __int8)((result) ^ ((unsigned __int8)(a1)));
    result = (unsigned __int8)((result) & (199));
    result = (unsigned __int8)((result) | (4));
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 48) = (unsigned __int8)(result);
    a1 = (unsigned __int8)(((unsigned __int8)(v_stack_m1F8)) ^ ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 49))));
    a1 = (unsigned __int8)((a1) & (1));
    a1 = (unsigned __int8)((a1) ^ ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 49))));
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 49) = (unsigned __int8)(a1);
    result = KiIsPrcbThread(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16) + 36480), *(unsigned __int64 *)(a4 + 24), a3, *(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8);
    if ((unsigned __int8)(result) == 0) {
        result = *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16) + 36);
        *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16) + 36480) + 536) = (unsigned int)(result);
    }
    v_rbx = (unsigned int)((0) + 1);
    if (((unsigned int)(v_rbx)) < ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312))))) goto loc_0025B493;
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 14312) + 4) = (unsigned int)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8);
    goto loc_0025A891;
loc_0025B52B:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312))) <= -4) goto loc_0025B5D2;
loc_0025B53C:
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 48)) & (254));
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 48) = (unsigned __int8)(result);
    result = (unsigned __int8)((result) & (253));
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 32) = v_stack_m1F0;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m1F0 + 120))) >> (1));
    a1 = (unsigned __int8)((a1) & (1));
    a1 = (unsigned __int8)((a1) + ((unsigned __int8)(a1)));
    a1 = (unsigned __int8)((a1) ^ ((unsigned __int8)(result)));
    a1 = (unsigned __int8)((a1) & (231));
    a1 = (unsigned __int8)((a1) | (4));
    a1 = (unsigned __int8)((a1) | (32));
    result = (unsigned __int8)(((unsigned __int8)(a1)) & (223));
    a1 = (unsigned __int8)(a1);
    if (v_stack_m1F0 == (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16) + 36480))) { a1 = (unsigned int)((unsigned __int8)(result)); }
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 48) = (unsigned __int8)(a1);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 40) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16) + 36480);
    result = KiIsPrcbThread(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16) + 36480), v_stack_m1F0, a3, *(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8);
    if ((unsigned __int8)(result) == 0) {
        result = *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16) + 36);
        *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16) + 36480) + 536) = (unsigned int)(result);
    }
    goto loc_0025B50F;
loc_0025B5A3:
    result = KiIsPrcbThread(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16) + 36480), v_stack_m1F0, a3, *(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8);
    if ((unsigned __int8)(result) != 0) goto loc_0025B4BA;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 49)) & (1)) != 0) {
    }
    *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16) + 36480) + 565) = 1;
    result = KiInsertDeferredReadyList(v_stack_m1C8, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16) + 36480), a3, *(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8);
    goto loc_0025B4BA;
loc_0025B5D2:
    result = KiIsPrcbThread(v_stack_m1C8, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16) + 36480), a3, *(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8);
    if ((unsigned __int8)(result) != 0) goto loc_0025B53C;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 49)) & (1)) != 0) {
    }
    *(unsigned __int8 *)(v_stack_m1C8 + 565) = 1;
    result = KiInsertDeferredReadyList(v_stack_m1C8, v_stack_m1C8, a3, *(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8);
    goto loc_0025B53C;
loc_0025B601:
    v_stack_m1F7 = 1;
loc_0025B609:
    v_stack_m1D0 = *(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8;
    if (((*(unsigned int *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 120)) & (0x400000ULL)) == 0) goto loc_0025B64A;
    result = KiIsThreadStateControlledByProcessor(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16), a3, 1);
    v_r11 = v_stack_m1F8;
    if ((unsigned __int8)(result) != 0) {
        a4 = 1;
        a2 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16);
        a1 = *(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8;
        result = KiUpdateVPBackingThreadPriority(a1, a2, a3, a4);
        v_r11 = v_stack_m1C0;
        a4 = v_stack_m1F7;
    }
loc_0025B64A:
    if ((unsigned __int8)(a4) == 0) goto loc_00259C81;
    *(unsigned __int64 *)(v_stack_m1D0 + 64) = 0;
    goto loc_00259C81;
loc_0025B65C:
    if ((*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8) == v_stack_m1C8) goto loc_0025B609;
    if ((*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8) < v_stack_m1C8) goto loc_00259C81;
    goto loc_0025B601;
loc_0025B670:
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16) + 536) = (unsigned int)((unsigned int)(*(unsigned int *)(v_r11 + 36)));
    goto loc_0025AFD2;
loc_0025B67F:
    *(unsigned int *)(v_stack_m1F0 + 536) = (unsigned int)((unsigned int)(*(unsigned int *)(v_r11 + 36)));
    goto loc_0025B451;
loc_0025B68F:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, v_stack_m1E0, a4);
    v_rsp = (v_rsp) + (496);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KiAttemptToScheduleThreadToBusyIsolationUnit(void *Arg1, int64_t Arg2, uint8_t Arg3, void *Arg4, int64_t Arg5, int64_t Arg6, int64_t Arg7)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint8_t v_stack_m12B;
    uint8_t v_stack_m12C;
    uint8_t v_stack_m12D;
    uint8_t v_stack_m12E;
    uint8_t v_stack_m12F;
    uint8_t v_stack_m130;
    uint32_t v_stack_m134;
    uint64_t v_stack_m138;
    uint64_t v_stack_m148;
    uint64_t v_stack_m158;
    uint64_t v_stack_m160;
    uint64_t v_stack_m168;
    uint64_t v_stack_m170;
    uint64_t v_stack_m178;
    uint64_t v_stack_m180;
    uint64_t v_stack_m188;
    uint64_t v_stack_m190;
    uint32_t v_stack_m198;
    uint32_t v_stack_m19C;
    uint32_t v_stack_m1A0;
    uint32_t v_stack_m1A4;
    uint32_t v_stack_m1A8;
    uint64_t v_stack_m1B0;
    uint64_t v_stack_m1B8;
    uint64_t v_stack_m1C0;
    uint64_t v_stack_m1C8;
    uint64_t v_stack_m1D0;
    uint64_t v_stack_m1D8;
    uint64_t v_stack_m1E0;
    uint32_t v_stack_m1E8;
    uint64_t v_stack_m1F0;
    uint8_t v_stack_m1F7;
    uint8_t v_stack_m1F8;
    uint64_t v_stack_m48;
    uint64_t v_stack_mDC;
    uint64_t v_stack_p18;

    v_stack_p18 = local_rbx;
    local_rsp = (local_rsp) - (496);
    result = (*(uint64_t *)(v_rip + 0xBB0C1A)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m1D8 = Arg5;
    local_r12 = (*(uint64_t *)(arg4)) & (-2);
    v_stack_m160 = Arg6;
    v_stack_m1F8 = Arg3;
    v_stack_m1F0 = Arg2;
    Arg2 = 0;
    v_stack_m1C8 = Arg1;
    v_stack_m190 = Arg7;
    v_stack_m1B0 = Arg4;
    result = memset(*(uint64_t *)(arg1 + 0x37E8), Arg2, 240, Arg4);
    local_rdi = 0;
    v_stack_m1C0 = 0;
    Arg1 = (*(uint64_t *)(arg4)) & (-2);
    v_stack_m1E8 = 0;
    Arg3 = (uint32_t)((*(uint64_t *)(arg4)) & (1));
    v_stack_m188 = Arg1;
    v_stack_m1B8 = Arg3;
    if (condition_is_equal) goto loc_00259F47;
    local_r11 = 0;
    if (Arg3 == 1) {
        result = *(uint64_t *)(arg1 + 0x8E58);
        local_r11 = *(uint64_t *)(arg1 + 0x8E58);
        local_r11 = (local_r11) + (8);
        v_stack_m1C0 = local_r11;
        Arg4 = *(uint8_t *)(result);
        v_stack_m1E8 = (uint32_t)(Arg4);
    }
    if ((uint32_t)(Arg4) == 0) goto loc_00259CE9;
loc_00259BEA:
    v_stack_m1E0 = (uint32_t)((uint32_t)(Arg4));
loc_00259BFB:
    result = 0;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x30 - 0x20) = v_xmm0;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x30 - 0x10) = v_xmm0;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x30) = 0;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x30 - 0x8) = -1;
    *(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x30 + 0x4) = 63;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x30 - 0x20) = *(uint64_t *)(local_r11);
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x30 - 0x18) = 0;
    if (*(uint64_t *)(*(uint64_t *)(local_r11) + 0x8E48) != 0) goto loc_00259F6B;
loc_00259C32:
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x30 - 0x10) = *(uint64_t *)(*(uint64_t *)(local_r11) + 0x10);
    local_r10 = *(uint64_t *)(*(uint64_t *)(local_r11) + 0x10);
    if (*(uint64_t *)(*(uint64_t *)(local_r11) + 0x10) == 0) {
        local_r10 = *(uint64_t *)(*(uint64_t *)(local_r11) + 0x8);
        *(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x30 - 0x10) = local_r10;
    }
    if ((*(uint64_t *)(*(uint64_t *)(local_r11) + 0x10)) == local_r10) goto loc_00259F63;
    if ((*(uint64_t *)(local_r11)) == (*(uint64_t *)(gs_base + (0 + 0x20)))) goto loc_00259F3F;
    Arg1 = (uint8_t)((*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x30)) & (251));
loc_00259C69:
    *(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x30) = (uint8_t)(Arg1);
loc_00259C6B:
    Arg4 = 0;
    v_stack_m1F7 = 0;
    if (((*(uint32_t *)(local_r10 + 0x78)) & (0x400000ULL)) != 0) goto loc_0025B65C;
loc_00259C81:
    result = (uint8_t)(~(*(uint8_t *)(*(uint64_t *)(local_r11) + 0x23)));
    result = (uint8_t)((result) & (1));
    Arg2 = (uint8_t)((*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x30)) & (254));
    Arg2 = (uint8_t)((Arg2) | ((uint8_t)(result)));
    *(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x30) = (uint8_t)(Arg2);
    Arg1 = (uint8_t)((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(local_r11) + 0x38))) >> (6));
    Arg1 = (uint8_t)((Arg1) ^ ((uint8_t)(Arg2)));
    Arg1 = (uint8_t)((Arg1) & (2));
    Arg1 = (uint8_t)((Arg1) ^ ((uint8_t)(Arg2)));
    *(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x30) = (uint8_t)((uint8_t)(Arg1));
    result = (uint32_t)(((uint8_t)(Arg1)) >> (1));
    result = (uint32_t)((result) & (1));
    local_r13 = 0;
    if (((uint32_t)(result)) > 0) { local_r13 = (uint32_t)(result); }
    local_r11 = (local_r11) + (8);
    local_rbx = (*(uint64_t *)(arg1 + 0x37E8) + 48) + (40);
    v_stack_m1C0 = local_r11;
    Arg3 = ((uint32_t)((uint32_t)(Arg4))) - (1);
    v_stack_m1E0 = Arg3;
    if (condition_is_not_equal) goto loc_00259BFB;
loc_00259CE9:
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x4) = (uint32_t)(local_r13);
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x8) = (uint32_t)(v_stack_m1B8);
    *(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8)) = (uint8_t)((uint32_t)(v_stack_m1E8));
    if ((uint32_t)(v_stack_m1B8) == 0) goto loc_00259F38;
loc_00259D0D:
    *(uint8_t *)(1 + *(uint64_t *)(arg1 + 0x37E8) * 1) = (uint8_t)(*(uint8_t *)(*(uint64_t *)(v_stack_m188 + 0x8E58) + 0x1));
    if ((uint32_t)(local_r13) != 0) goto loc_0025B072;
loc_00259D1C:
loc_00259D30:
    if (0 >= ((uint32_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8))))) goto loc_00259D4E;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10)) == local_r12) goto loc_00259D4A;
    Arg2 = (uint32_t)((0) + 1);
    goto loc_00259D30;
loc_00259D4A:
loc_00259D4E:
    local_rsi = ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m1B0 + 0xC))) != 0) ? 1 : 0;
    v_stack_m1B8 = 0;
    if ((*(uint8_t *)(v_rip + 0xD6CD56)) == 0) goto loc_0025A151;
    result = KiEvaluateGroupSchedulingPreemption(*(uint64_t *)(arg1 + 0x37E8) + 0 + 0 * 4 * 8 + 16, v_stack_m1F0, (uint32_t)((uint32_t)(local_rsi)), v_stack_m1B8);
loc_00259D86:
    if (v_stack_m190 != 0) {
        *(uint64_t *)(v_stack_m190) = v_stack_m1B8;
    }
    if ((uint8_t)(result) == 0) goto loc_00259FF2;
    result = (uint32_t)((*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10 + 0x20)) >> (1));
    result = (uint32_t)((result) & (1));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m1F0 + 0x78))) >> (1));
    Arg1 = (uint32_t)((Arg1) & (1));
    if (((uint32_t)(Arg1)) < ((uint32_t)(result))) { Arg1 = (uint32_t)(result); }
    if (((uint32_t)(Arg1)) == 1) goto loc_0025AF2B;
loc_00259DBF:
loc_00259DC8:
    if (0 >= ((uint32_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8))))) goto loc_00259DE6;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10)) == local_r12) goto loc_00259DE2;
    Arg2 = (uint32_t)((0) + 1);
    goto loc_00259DC8;
loc_00259DE2:
loc_00259DE6:
    local_r10 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m1F0 + 0x78))) >> (1));
    result = (uint32_t)((*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10 + 0x20)) >> (1));
    local_r10 = (uint32_t)((local_r10) & (1));
    result = (uint32_t)((result) & (1));
    v_stack_m1E8 = (uint32_t)(local_r10);
    if (((uint32_t)(local_r10)) >= ((uint32_t)(result))) goto loc_0025B3E2;
    if ((*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8))) <= 0) goto loc_00259EB4;
loc_00259E24:
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10)) == local_r12) goto loc_0025B009;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x28) - 1) <= -4) goto loc_0025B0D9;
loc_00259E53:
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x30)) | (1));
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x20) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x18);
    *(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x30) = (uint8_t)(result);
    result = (uint8_t)((result) & (253));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x18) + 0x78))) >> (1));
    Arg1 = (uint8_t)((Arg1) & (1));
    Arg1 = (uint8_t)((Arg1) + ((uint8_t)(Arg1)));
    Arg1 = (uint8_t)((Arg1) ^ ((uint8_t)(result)));
    Arg1 = (uint8_t)((Arg1) & (231));
    Arg1 = (uint8_t)((Arg1) | (4));
    Arg1 = (uint8_t)((Arg1) & (223));
    *(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x30) = (uint8_t)(Arg1);
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x28) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x18);
    result = KiIsPrcbThread(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x18), Arg2, *(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8)), *(uint64_t *)(arg1 + 0x37E8) + 0 + 0 * 4 * 8);
    if ((uint8_t)(result) == 0) {
        result = *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x24);
        *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x18) + 0x218) = (uint32_t)(result);
    }
    local_rbx = (uint32_t)((0) + 1);
    if (((uint32_t)(local_rbx)) < ((uint32_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8))))) goto loc_00259E24;
loc_00259EB4:
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x4) = (uint32_t)((uint32_t)(v_stack_m1E8));
loc_00259EC0:
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8))) == 0) goto loc_0025A1F0;
loc_00259ED5:
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x18)) <= 0) goto loc_00259EEA;
    if (0 == 0) goto loc_00259EE7;
    local_rbx = 0;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x18)) < 0) {
        local_rbx = *(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x18);
    }
    Arg1 = (*(uint64_t *)(arg1 + 0x37E8) + 24) + (40);
    Arg2 = ((uint32_t)((uint32_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8))))) - (1);
    if (condition_is_not_equal) goto loc_00259ED5;
    if (local_rbx == 0) goto loc_0025A1F0;
    Arg1 = (0) + (11);
    Arg1 = (Arg1) << (4);
    Arg1 = (Arg1) + (*(uint64_t *)(arg1 + 0x37E8));
    if (((*(uint32_t *)(v_rip + 0xD6CC24)) & (0x200000ULL)) == 0) goto loc_0025A5EB;
    *(uint64_t *)(arg1 + 0x8) = local_rbx;
    *(uint64_t *)(arg1) = 0;
    if (Arg1 != NULL) goto loc_0025A82D;
loc_00259F31:
    local_rsi = (uint32_t)((0) + 1);
    goto loc_00259EC0;
loc_00259F38:
    result = 0;
    goto loc_00259D0D;
loc_00259F3F:
    Arg1 = (uint8_t)((Arg1) | (4));
    goto loc_00259C69;
loc_00259F47:
    v_stack_m1C0 = v_stack_m188;
    v_stack_m1E8 = 1;
    goto loc_00259BEA;
loc_00259F63:
    goto loc_00259C6B;
loc_00259F6B:
    if (((*(uint8_t *)(local_rsi + 0x23)) & (16)) != 0) goto loc_0025A191;
loc_00259F75:
    *(uint64_t *)(local_rbx - 0x18) = *(uint64_t *)(local_rsi + 0x8E48);
    goto loc_00259C32;
loc_00259F85:
    if ((uint8_t)(*(uint8_t *)(v_stack_m1C8 + 0x35D9)) != 0) goto loc_0025A041;
    *(uint8_t *)(v_stack_m1C8 + 0x35D9) = 1;
    *(uint32_t *)(v_stack_m1C8 + 0x35DC) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsi + 0x24)));
loc_00259FA7:
    if (((*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8) + local_rbx * 8 + 0x33)) & (2)) != 0) goto loc_0025A131;
loc_00259FB3:
    if (((*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8) + local_rbx * 8 + 0x33)) & (4)) == 0) goto loc_00259FD1;
    if (*(uint64_t *)(local_rsi + 0x8EB8) != 0) goto loc_0025A090;
loc_00259FD1:
    result = *(uint64_t *)(local_rsi + 0x8EB8);
    if (((*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8) + local_rbx * 8 + 0x33)) & (1)) != 0) {
        result = *(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + local_rbx * 8 + 0x28);
    }
    local_rdi = (uint32_t)((local_rdi) + 1);
    if (((uint32_t)(local_rdi)) < ((uint32_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8))))) goto loc_0025A010;
loc_00259FF0:
loc_00259FF2:
    goto loc_0025B68F;
loc_00259FF8:
    result = 0;
    *(uint64_t *)((uint32_t)(v_stack_m1E8)) = 0;
    *(uint64_t *)(0 + 0x40) = local_rdi;
    if ((uint8_t)(local_r12) == 0) goto loc_00259FF0;
    if ((*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8))) <= 0) goto loc_00259FF0;
loc_0025A010:
    if ((((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8) + (uint32_t)((uint32_t)(local_rdi)) + (uint32_t)((uint32_t)(local_rdi)) * 4 * 8 + 0x33))) & (16)) != 0) goto loc_00259F85;
    if ((((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8) + (uint32_t)((uint32_t)(local_rdi)) + (uint32_t)((uint32_t)(local_rdi)) * 4 * 8 + 0x33))) & (8)) == 0) goto loc_00259FA7;
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + (uint32_t)((uint32_t)(local_rdi)) + (uint32_t)((uint32_t)(local_rdi)) * 4 * 8 + 0x10) + 0x7)) != 0) goto loc_00259F85;
    goto loc_00259FA7;
loc_0025A041:
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8) + (uint32_t)((uint32_t)(local_rdi)) + (uint32_t)((uint32_t)(local_rdi)) * 4 * 8 + 0x33))) != 1) goto loc_0025A087;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m1C8 + 0x35DC)))) == (*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + (uint32_t)((uint32_t)(local_rdi)) + (uint32_t)((uint32_t)(local_rdi)) * 4 * 8 + 0x10) + 0x24))) goto loc_00259FA7;
    *(uint8_t *)(v_stack_m1C8 + 0x35D9) = 2;
    result = KeAddProcessorAffinityEx(v_stack_m1C8 + 13792, (uint32_t)(*(uint32_t *)(v_stack_m1C8 + 0x35DC)), local_rbx, 1);
loc_0025A06C:
    result = KeAddGroupAffinityEx(v_stack_m1C8 + 13792, *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + (uint32_t)((uint32_t)(local_rdi)) + (uint32_t)((uint32_t)(local_rdi)) * 4 * 8 + 0x10) + 0xD0), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + (uint32_t)((uint32_t)(local_rdi)) + (uint32_t)((uint32_t)(local_rdi)) * 4 * 8 + 0x10) + 0xC8), 1);
    goto loc_00259FA7;
loc_0025A087:
    goto loc_0025A06C;
loc_0025A090:
    if ((*(uint64_t *)(v_stack_m1C8 + 0x8EB8)) == 0) goto loc_00259FD1;
    if (v_stack_m1C8 == (*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + (uint32_t)((uint32_t)(local_rdi)) + (uint32_t)((uint32_t)(local_rdi)) * 4 * 8 + 0x10))) goto loc_00259FD1;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result))))) & (0x40000ULL));
    if (condition_is_below) goto loc_0025A0C9;
    if ((uint32_t)(result) == 0) goto loc_00259FD1;
    if (((uint32_t)((uint8_t)((uint32_t)(*(uint32_t *)(result))))) >= ((uint32_t)(v_stack_m1C8 + 13792))) goto loc_00259FD1;
loc_0025A0C9:
    *(uint32_t *)(*(uint64_t *)(v_stack_m1C8 + 0x8EB8) + 0xC) = 2;
    result = (uint8_t)((uint32_t)(*(uint32_t *)(result)));
    local_r12 = (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + (uint32_t)((uint32_t)(local_rdi)) + (uint32_t)((uint32_t)(local_rdi)) * 4 * 8 + 0x10) + 0x24));
    if ((*(uint8_t *)(v_rip + 0xD6AF37)) == 0) {
        result = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + (uint32_t)((uint32_t)(local_rdi)) + (uint32_t)((uint32_t)(local_rdi)) * 4 * 8 + 0x10) + 0x24)));
        Arg2 = v_rip + 14102897;
        local_r12 = *(uint8_t *)(Arg2 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + (uint32_t)((uint32_t)(local_rdi)) + (uint32_t)((uint32_t)(local_rdi)) * 4 * 8 + 0x10) + 0x24)) * 2);
        local_r12 = (uint32_t)((local_r12) << (6));
        result = *(uint8_t *)(Arg2 + result * 2 + 0x1);
        Arg2 = 2;
        local_r12 = (uint32_t)((local_r12) | ((uint32_t)(result)));
    }
    *(uint32_t *)(*(uint64_t *)(v_stack_m1C8 + 0x8EB8) + 0x8) = (uint32_t)(local_r12);
    result = (uint32_t)(*(uint32_t *)(v_rip + 0xD6CA05));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD6CA05)))) & (32)) != 0) {
        Arg1 = *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + (uint32_t)((uint32_t)(local_rdi)) + (uint32_t)((uint32_t)(local_rdi)) * 4 * 8 + 0x10) + 0x24);
        result = EtwTraceXSchedulerPriorityKickSend(Arg1, Arg2, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + (uint32_t)((uint32_t)(local_rdi)) + (uint32_t)((uint32_t)(local_rdi)) * 4 * 8 + 0x10) + 0xC8), 1);
    }
    Arg2 = ((uint32_t)((uint32_t)(local_r12))) >> (32);
    goto loc_00259FD1;
loc_0025A131:
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + (uint32_t)((uint32_t)(local_rdi)) + (uint32_t)((uint32_t)(local_rdi)) * 4 * 8 + 0x28)) != 0) goto loc_0025A14C;
loc_0025A142:
    result = EtwTraceScheduleThread(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + (uint32_t)((uint32_t)(local_rdi)) + (uint32_t)((uint32_t)(local_rdi)) * 4 * 8 + 0x28), *(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + (uint32_t)((uint32_t)(local_rdi)) + (uint32_t)((uint32_t)(local_rdi)) * 4 * 8 + 0x10), v_stack_m160, 1);
    goto loc_00259FB3;
loc_0025A14C:
    Arg3 = 0;
    goto loc_0025A142;
loc_0025A151:
    if ((((uint8_t)(*(uint8_t *)((uint32_t)((uint32_t)(local_rdi)) + (uint32_t)((uint32_t)(local_rdi)) * 4 + 0x20))) & (1)) != 0) goto loc_0025A1C7;
    if (((uint8_t)(*(uint8_t *)(v_stack_m1F0 + 0xC3))) > (*(uint8_t *)(*(uint64_t *)((uint32_t)((uint32_t)(local_rdi)) + (uint32_t)((uint32_t)(local_rdi)) * 4 + 0x10) + 0xC3))) goto loc_0025A1E0;
    if (((uint8_t)(*(uint8_t *)(v_stack_m1F0 + 0xC3))) != (*(uint8_t *)(*(uint64_t *)((uint32_t)((uint32_t)(local_rdi)) + (uint32_t)((uint32_t)(local_rdi)) * 4 + 0x10) + 0xC3))) goto loc_0025A1CE;
    Arg1 = ((((uint8_t)(*(uint8_t *)((uint32_t)((uint32_t)(local_rdi)) + (uint32_t)((uint32_t)(local_rdi)) * 4 + 0x20))) & (24)) == 0) ? 1 : 0;
    result = ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + (uint32_t)((uint32_t)(local_rdi)) + (uint32_t)((uint32_t)(local_rdi)) * 4 * 8 + 0x10))) & (1)) == 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) != 0) goto loc_0025A1CE;
    goto loc_00259D86;
loc_0025A191:
    result = KeIsForceParkingEnabled(Arg1, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + (uint32_t)((uint32_t)(local_rdi)) + (uint32_t)((uint32_t)(local_rdi)) * 4 * 8 + 0x10) + 0xC0), *(uint8_t *)(v_stack_m1F0 + 0xC3), *(uint8_t *)((uint32_t)((uint32_t)(local_rdi)) + (uint32_t)((uint32_t)(local_rdi)) * 4 + 0x20));
    if ((uint8_t)(result) == 0) goto loc_0025A1AB;
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + (uint32_t)((uint32_t)(local_rdi)) + (uint32_t)((uint32_t)(local_rdi)) * 4 * 8 + 0x10) + 0x23)) & (32)) != 0) goto loc_0025B271;
loc_0025A1AB:
loc_0025A1AF:
    Arg2 = (*(uint64_t *)(arg1 + 0x2C8)) & (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + (uint32_t)((uint32_t)(local_rdi)) + (uint32_t)((uint32_t)(local_rdi)) * 4 * 8 + 0x10) + 0xC0) + 0x50));
    if (Arg2 == 0) goto loc_00259F75;
    goto loc_00259C32;
loc_0025A1C7:
    goto loc_00259D86;
loc_0025A1CE:
    if ((((uint8_t)(*(uint8_t *)((uint32_t)((uint32_t)(local_rdi)) + (uint32_t)((uint32_t)(local_rdi)) * 4 + 0x20))) & (16)) == 0) goto loc_0025A1E7;
    if ((uint8_t)(*(uint8_t *)(v_stack_m1F0 + 0xC3)) == 0) goto loc_0025A1E7;
    goto loc_00259D86;
loc_0025A1E0:
    goto loc_00259D86;
loc_0025A1E7:
    result = 0;
    goto loc_00259D86;
loc_0025A1F0:
    Arg2 = 0;
    result = memset(v_stack_m138, Arg2, 240, *(uint8_t *)((uint32_t)((uint32_t)(local_rdi)) + (uint32_t)((uint32_t)(local_rdi)) * 4 + 0x20));
    result = KiStartReadyQueueEnumeratorForRescheduleContext(v_stack_m138, *(uint64_t *)(arg1 + 0x37E8), 240, *(uint8_t *)((uint32_t)((uint32_t)(local_rdi)) + (uint32_t)((uint32_t)(local_rdi)) * 4 + 0x20));
loc_0025A20D:
    if (((uint8_t)(v_stack_m12B)) == 4) goto loc_0025A84D;
    if ((uint8_t)(v_stack_m12B) != 0) goto loc_0025A40F;
loc_0025A230:
    if (1 == 2) goto loc_0025A34F;
    Arg1 = (uint32_t)((1) - (1));
    if (condition_is_not_equal) goto loc_0025A5FF;
    v_stack_m134 = (uint32_t)((uint32_t)((uint32_t)(local_rdi)));
    if ((uint32_t)((uint32_t)(v_stack_m138)) != 0) goto loc_0025A711;
loc_0025A254:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) & (0xFFFFFFFEULL));
    v_stack_m134 = (uint32_t)(result);
    if (condition_is_equal) goto loc_0025A3F4;
    v_stack_m12E = (uint8_t)(v_stack_m12F);
    v_stack_m130 = (uint8_t)(*(uint8_t *)((uint32_t)((uint32_t)(local_rdi)) + (uint32_t)((uint32_t)(local_rdi)) * 4 + 0x20));
    v_stack_m19C = (uint32_t)(*(uint8_t *)((uint32_t)((uint32_t)(local_rdi)) + (uint32_t)((uint32_t)(local_rdi)) * 4 + 0x20));
    Arg1 = ((uint8_t)(v_stack_m12F) + (uint8_t)(v_stack_m12F) * 2) + ((uint8_t)(v_stack_m12F) + (uint8_t)(v_stack_m12F) * 2);
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m128 + arg1 * 8 + 0x48))) | (*(uint32_t *)(v_stack_m128 + arg1 * 8 + 0x4C)));
    local_r11 = (uint32_t)((1) << ((uint8_t)((uint8_t)(*(uint8_t *)((uint32_t)((uint32_t)(local_rdi)) + (uint32_t)((uint32_t)(local_rdi)) * 4 + 0x20)))));
    if ((((uint32_t)(Arg2)) & ((uint32_t)(local_r11))) != 0) goto loc_0025A2C4;
loc_0025A295:
    local_r10 = (uint8_t)((v_stack_m12F) + 1);
    v_stack_m12E = (uint8_t)(local_r10);
    if (((uint32_t)((uint8_t)(local_r10))) >= ((uint32_t)((uint32_t)(v_stack_m138)))) {
        local_r10 = 0;
        v_stack_m12E = 0;
    }
    Arg1 = (0 + 0 * 2) + (0 + 0 * 2);
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m128 + arg1 * 8 + 0x48))) | (*(uint32_t *)(v_stack_m128 + arg1 * 8 + 0x4C)));
    if ((((uint32_t)(Arg2)) & ((uint32_t)(local_r11))) == 0) goto loc_0025A295;
loc_0025A2C4:
    Arg2 = 0;
    Arg1 = (0 + 0 * 2) << (4);
    Arg3 = (v_stack_m108) + (Arg1);
    v_stack_m12D = 0;
    if (!(condition_is_above_or_equal)) {
        Arg2 = 1;
        v_stack_m12D = (uint8_t)(Arg2);
    }
    if (!(condition_is_above_or_equal)) {
        Arg2 = (uint8_t)((Arg2) | (2));
        v_stack_m12D = (uint8_t)(Arg2);
    }
    if ((((uint32_t)((uint8_t)(Arg2))) & ((uint32_t)((uint8_t)(Arg2) - 1))) != 0) goto loc_0025ADCC;
    v_stack_m198 = (uint32_t)((uint8_t)(Arg2) - 1);
loc_0025A31C:
    v_stack_m12C = (uint8_t)((uint8_t)(Arg2) - 1);
    if ((uint8_t)((uint8_t)(Arg2) - 1) == 0) goto loc_0025AC2A;
    if (((uint32_t)((uint8_t)((uint8_t)(Arg2) - 1))) != 1) goto loc_0025A342;
    result = ((uint8_t)(*(uint8_t *)((uint32_t)((uint32_t)(local_rdi)) + (uint32_t)((uint32_t)(local_rdi)) * 4 + 0x20))) + (4);
    result = (result) << (4);
    result = (result) + (*(uint64_t *)(Arg3 + 0x8));
loc_0025A33E:
    v_stack_m118 = result;
loc_0025A342:
    v_stack_m110 = v_stack_m118;
    goto loc_0025A401;
loc_0025A34F:
    Arg2 = 0;
    if (Arg3 == 0) goto loc_0025A3B4;
loc_0025A360:
    Arg1 = (0 + 0 * 2) + (0 + 0 * 2);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m128 + arg1 * 8 + 0x40))) == 0) goto loc_0025A3A5;
    result = (*(uint64_t *)(v_stack_m128 + arg1 * 8 + 0x20)) + (0x8430ULL);
    if ((((uint8_t)(*(uint64_t *)(result + 0x8))) & (1)) != 0) goto loc_0025A5D5;
loc_0025A390:
    if (*(uint64_t *)(result + 0x8) != 0) goto loc_0025AC40;
loc_0025A399:
loc_0025A39C:
    *(uint64_t *)(v_stack_m128 + arg1 * 8 + 0x30) = local_rdi;
loc_0025A3A5:
    Arg2 = (uint8_t)((Arg2) + 1);
    if (((uint32_t)((uint8_t)(Arg2))) < ((uint32_t)((uint32_t)(v_stack_m138)))) goto loc_0025A360;
loc_0025A3B4:
    local_rbx = 0;
loc_0025A3C0:
    Arg1 = ((uint8_t)((uint8_t)(v_stack_m12F)) + (uint8_t)((uint8_t)(v_stack_m12F)) * 2) + ((uint8_t)((uint8_t)(v_stack_m12F)) + (uint8_t)((uint8_t)(v_stack_m12F)) * 2);
    if (*(uint64_t *)(v_stack_m128 + arg1 * 8 + 0x30) != 0) goto loc_0025AC53;
loc_0025A3D8:
    Arg2 = (uint8_t)(((uint8_t)(v_stack_m12F)) + 1);
    Arg2 = (uint8_t)(Arg2);
    if (((uint32_t)((uint8_t)(Arg2))) >= ((uint32_t)((uint32_t)(v_stack_m138)))) { Arg2 = (uint32_t)(local_rdi); }
    if (((uint8_t)(Arg2)) != ((uint8_t)(v_stack_m12F))) goto loc_0025A3C0;
    if (local_rdi != 0) goto loc_0025AC67;
loc_0025A3F4:
    local_rsi = (uint8_t)((1) + 1);
    if (((uint8_t)(local_rsi)) < 4) goto loc_0025A230;
loc_0025A401:
    v_stack_m12B = (uint8_t)(local_rsi);
    if (((uint8_t)(local_rsi)) == 4) goto loc_0025A84D;
loc_0025A40F:
    v_stack_m110 = *(uint64_t *)(v_stack_m110);
    if ((*(uint64_t *)(v_stack_m110)) == v_stack_m118) goto loc_0025A83C;
    local_rsi = (*(uint64_t *)(v_stack_m110)) + (-216);
    Arg1 = (v_stack_m12E + v_stack_m12E * 2) + (v_stack_m12E + v_stack_m12E * 2);
    v_stack_m1D0 = *(uint64_t *)(v_stack_m128 + arg1 * 8 + 0x20);
    if (v_stack_m12B == 2) goto loc_0025AD54;
    if (v_stack_m12C != 1) goto loc_0025AB60;
loc_0025A459:
    v_stack_m1E8 = *(uint64_t *)(v_stack_m128 + arg1 * 8 + 0x28);
loc_0025A461:
    if ((*(uint64_t *)(local_rsi + 0x238)) != (*(uint64_t *)(v_rip + 0xD6C790))) goto loc_0025AD03;
loc_0025A475:
    if (local_rdi == 0) goto loc_0025A734;
loc_0025A47E:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsi + 0x78))) >> (1));
    Arg1 = (uint32_t)((Arg1) & (1));
    if (((uint32_t)(Arg1)) > (*(uint32_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x8))) goto loc_0025A20D;
    if (((uint32_t)(Arg1)) < ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x4))))) { Arg1 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x4))); }
    if ((uint32_t)(Arg1) != 0) goto loc_0025B27D;
loc_0025A4A4:
    if (((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) >= ((uint32_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8))))) goto loc_0025A20D;
    v_stack_m1E0 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) * 4 * 8 + 0x10);
    if ((*(uint32_t *)(v_rip + 0xD6AE29)) == ((uint32_t)(local_rdi))) goto loc_0025A4D8;
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) * 4 * 8 + 0x10) + 0x23)) & (32)) != 0) goto loc_0025ACC5;
loc_0025A4D8:
    if (*(uint64_t *)(v_stack_m128 + arg1 * 8 + 0x28) == 0) goto loc_0025ACDF;
loc_0025A4E1:
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) * 4 * 8 + 0x18) == 0) goto loc_0025A5C3;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) * 4 * 8 + 0x18)) != (*(uint64_t *)(v_stack_m128 + arg1 * 8 + 0x28))) goto loc_0025A5C3;
    result = KiComputeThreadQos(local_rsi, local_rdi, (uint32_t)(v_stack_m138), *(uint64_t *)(v_stack_m128 + arg1 * 8 + 0x28));
    Arg3 = (uint32_t)(*(uint32_t *)(local_rsi + 0x50));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi + 0x50)))) <= ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi + 0x54))))) { Arg3 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsi + 0x54))); }
    Arg2 = (Arg3 >= (*(uint32_t *)(v_rip + 0xD6AE58))) ? 1 : 0;
    Arg3 = (uint32_t)((Arg2 + result * 2) * ((uint32_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) * 4 * 8 + 0x10) + 0xC0) + 0xB9))));
    Arg3 = (uint32_t)((Arg3) + ((uint32_t)(*(uint8_t *)(local_rsi + 0x205))));
    Arg3 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) * 4 * 8 + 0x10) + 0xC0) + 0xC0) + Arg3 + Arg3 * 2 * 8 + 0x8)) & (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) * 4 * 8 + 0x10) + 0xC0) + 0xC0) + Arg3 + Arg3 * 2 * 8 + 0x10));
    Arg2 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) * 4 * 8 + 0x10) + 0xC0) + 0xC0) + Arg3 + Arg3 * 2 * 8)) & (Arg3);
    v_stack_m180 = Arg2;
    v_stack_m178 = Arg3;
    v_stack_m170 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) * 4 * 8 + 0x10) + 0xC0) + 0xC0) + Arg3 + Arg3 * 2 * 8 + 0x10);
    v_stack_m158 = v_xmm0;
    v_stack_m148 = v_xmm1;
    if (((*(uint64_t *)(v_stack_m1E0 + 0xC8)) & (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) * 4 * 8 + 0x10) + 0xC0) + 0xC0) + Arg3 + Arg3 * 2 * 8 + 0x10))) == 0) goto loc_0025ADAF;
loc_0025A58C:
    if (v_stack_m1E0 != v_stack_m1D0) goto loc_0025AB68;
loc_0025A597:
    v_stack_m168 = local_rdi;
    if ((*(uint8_t *)(v_rip + 0xD6C51E)) == ((uint8_t)(local_rdi))) goto loc_0025AEDC;
    Arg3 = 0;
    result = KiEvaluateGroupSchedulingPreemption(*(uint64_t *)(arg1 + 0x37E8) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) * 4 * 8 + 16, local_rsi, Arg3, v_stack_m168);
    if ((uint8_t)(result) != 0) goto loc_0025A978;
loc_0025A5C3:
    local_r12 = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) + 1);
    goto loc_0025A4A4;
loc_0025A5D5:
    if (0 == 1) goto loc_0025A399;
    result = (result) | (1);
    result = (result) ^ (0);
    goto loc_0025A390;
loc_0025A5EB:
    v_stack_m1A8 = (uint32_t)(local_rdi);
    if (condition_is_above_or_equal) goto loc_00259F31;
loc_0025A5FF:
    if (((uint32_t)(*(uint64_t *)(arg1 + 0x37E8) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) * 4 * 8 + 16)) != 2) goto loc_0025A3F4;
    v_stack_m134 = (uint32_t)((uint32_t)((uint32_t)(local_rdi)));
    if (0 != 0) goto loc_0025A80A;
loc_0025A616:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) & (1));
    v_stack_m134 = (uint32_t)(result);
    if (condition_is_equal) goto loc_0025A3F4;
    v_stack_m12E = (uint8_t)(v_stack_m12F);
    v_stack_m130 = (uint8_t)(v_stack_m1E8);
    v_stack_m1A4 = (uint32_t)(v_stack_m1E8);
    Arg1 = ((uint8_t)(v_stack_m12F) + (uint8_t)(v_stack_m12F) * 2) + ((uint8_t)(v_stack_m12F) + (uint8_t)(v_stack_m12F) * 2);
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m128 + arg1 * 8 + 0x48))) | (*(uint32_t *)(v_stack_m128 + arg1 * 8 + 0x4C)));
    local_r11 = (uint32_t)((1) << ((uint8_t)((uint8_t)(v_stack_m1E8))));
    if ((((uint32_t)(Arg2)) & ((uint32_t)(local_r11))) != 0) goto loc_0025A686;
loc_0025A657:
    local_r10 = (uint8_t)((v_stack_m12F) + 1);
    v_stack_m12E = (uint8_t)(local_r10);
    if (((uint32_t)((uint8_t)(local_r10))) >= 0) {
        local_r10 = 0;
        v_stack_m12E = 0;
    }
    Arg1 = (0 + 0 * 2) + (0 + 0 * 2);
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m128 + arg1 * 8 + 0x48))) | (*(uint32_t *)(v_stack_m128 + arg1 * 8 + 0x4C)));
    if ((((uint32_t)(local_r11)) & ((uint32_t)(Arg2))) == 0) goto loc_0025A657;
loc_0025A686:
    Arg2 = 0;
    Arg1 = (0 + 0 * 2) << (4);
    Arg3 = (v_stack_m108) + (Arg1);
    v_stack_m12D = 0;
    if (!(condition_is_above_or_equal)) {
        Arg2 = 1;
        v_stack_m12D = (uint8_t)(Arg2);
    }
    if (!(condition_is_above_or_equal)) {
        Arg2 = (uint8_t)((Arg2) | (2));
        v_stack_m12D = (uint8_t)(Arg2);
    }
    if ((((uint32_t)((uint8_t)(Arg2))) & ((uint32_t)((uint8_t)(Arg2) - 1))) != 0) goto loc_0025AEAB;
    v_stack_m1A0 = (uint32_t)((uint8_t)(Arg2) - 1);
loc_0025A6DE:
    v_stack_m12C = (uint8_t)((uint8_t)(Arg2) - 1);
    if ((uint8_t)((uint8_t)(Arg2) - 1) == 0) goto loc_0025ACED;
    if (((uint32_t)((uint8_t)((uint8_t)(Arg2) - 1))) != 1) goto loc_0025A704;
    result = ((uint8_t)(v_stack_m1E8)) + (4);
    result = (result) << (4);
    result = (result) + (*(uint64_t *)(Arg3 + 0x8));
loc_0025A700:
    v_stack_m118 = result;
loc_0025A704:
    v_stack_m110 = v_stack_m118;
    goto loc_0025A401;
loc_0025A711:
loc_0025A718:
    result = (uint32_t)((v_stack_m118) | (*(uint32_t *)(v_stack_mDC - 0x4)));
    v_stack_m134 = (uint32_t)(result);
    result = (uint32_t)((result) | (*(uint32_t *)(v_stack_mDC + 0x30 - 0x30)));
    v_stack_m134 = (uint32_t)(result);
    Arg2 = ((uint32_t)(Arg3)) - (1);
    if (condition_is_equal) goto loc_0025A254;
    goto loc_0025A718;
loc_0025A734:
    if (*(uint64_t *)(local_rsi + 0x68) == 0) goto loc_0025A47E;
    Arg1 = ((uint32_t)(*(uint32_t *)(v_stack_m1D0 + 0xD8))) + (*(uint64_t *)(local_rsi + 0x68));
    if (condition_is_equal) goto loc_0025A47E;
    if ((*(uint8_t *)(local_rsi + 0xC3)) >= 16) goto loc_0025A47E;
    if (((*(uint32_t *)(local_rsi + 0x78)) & (512)) != 0) goto loc_0025A47E;
    if ((*(uint32_t *)(local_rsi + 0x1E4)) != ((uint32_t)(local_rdi))) goto loc_0025A47E;
    if ((*(uint8_t *)(local_rsi + 0x186)) == 1) goto loc_0025A47E;
loc_0025A790:
    if (((*(uint8_t *)(arg1 + 0x70)) & (2)) != 0) goto loc_0025A7BD;
    if (*(uint64_t *)(arg1 + 0x1A0) != 0) goto loc_0025A790;
loc_0025A7A2:
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) + (*(uint32_t *)(arg1 + 0x7C)));
    if (condition_is_not_equal) goto loc_0025A7B4;
    if (*(uint64_t *)(arg1 + 0x1A0) != 0) goto loc_0025A7A2;
loc_0025A7B4:
    if (Arg3 == 0) goto loc_0025A47E;
loc_0025A7BD:
    result = KiRemoveCurrentlyEnumeratedThreadFromReadyQueue(v_stack_m138, local_rsi, Arg3, v_stack_m1E8);
    Arg4 = 0;
    *(uint32_t *)(local_rsi + 0x218) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m1D0 + 0x24)));
    result = KiAddThreadToScbQueue(v_stack_m1D0, Arg1, local_rsi, Arg4);
    if (((*(uint32_t *)(v_rip + 0xD6C327)) & (0x800ULL)) == 0) goto loc_0025A20D;
    Arg4 = 0;
    result = EtwTraceReadyQueueInsertion(local_rsi, (uint32_t)(*(uint32_t *)(v_stack_m1D0 + 0x24)), Arg4 + 2, Arg4);
    goto loc_0025A20D;
loc_0025A80A:
loc_0025A811:
    result = (uint32_t)((result) | (*(uint32_t *)(v_stack_mDC - 0x4)));
    v_stack_m134 = (uint32_t)(result);
    result = (uint32_t)((result) | (*(uint32_t *)(v_stack_mDC + 0x30 - 0x30)));
    v_stack_m134 = (uint32_t)(result);
    Arg2 = ((uint32_t)((uint32_t)(Arg4 + 2))) - (1);
    if (condition_is_equal) goto loc_0025A616;
    goto loc_0025A811;
loc_0025A82D:
    result = KxWaitForLockOwnerShip(v_stack_mDC + 48, Arg2, Arg4 + 2, Arg4);
    local_rsi = (uint32_t)((local_rsi) + 1);
    goto loc_00259EC0;
loc_0025A83C:
    result = KiAdvanceReadyQueueEnumeratorToNextList(v_stack_m138, Arg2, v_stack_m1D0, Arg4);
    if (!sign_flag) goto loc_0025A40F;
loc_0025A84D:
loc_0025A853:
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8))) == 0) goto loc_0025A88C;
loc_0025A864:
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x18)) <= local_rdi) goto loc_0025A879;
    if (local_rdi == 0) goto loc_0025A876;
    local_rbx = local_rdi;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x18)) < local_rdi) {
        local_rbx = *(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x18);
    }
    Arg1 = (*(uint64_t *)(arg1 + 0x37E8) + 24) + (40);
    Arg2 = ((uint32_t)((uint32_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8))))) - (1);
    if (condition_is_not_equal) goto loc_0025A864;
    if (local_rbx != 0) goto loc_0025AE43;
loc_0025A88C:
loc_0025A891:
    local_r12 = 0;
    local_rsi = (uint32_t)((uint32_t)(local_rdi));
    if (((*(uint32_t *)(v_rip + 0xD6C274)) & (0x400ULL)) != 0) { local_rsi = 2; }
    if ((*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8))) <= ((uint8_t)(local_rdi))) goto loc_0025A8E2;
loc_0025A8B4:
    Arg1 = ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) * 4 + 2) + ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))));
    result = KiCommitRescheduleContextEntry(*(uint64_t *)(arg1 + 0x37E8) + Arg1 * 8, v_stack_m1C8, (uint32_t)((uint32_t)(local_rsi)), v_stack_m1D8);
    local_r12 = (uint8_t)((local_r12) | ((uint8_t)(result)));
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) + 1);
    if (((uint32_t)(local_rbx)) < ((uint32_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8))))) goto loc_0025A8B4;
    local_rdi = 0;
loc_0025A8E2:
    if ((*(uint32_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x8)) != 1) goto loc_0025A905;
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x10) + 0x8E58) + 0x1)) + 1);
    *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x10) + 0x8E58) + 0x1) = (uint8_t)(result);
    if (((uint8_t)(result)) >= (*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x10) + 0x8E58)))) {
        *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x10) + 0x8E58) + 0x1) = 0;
    }
    Arg4 = (*(uint64_t *)(v_stack_m1B0)) & (-2);
    v_stack_m1B0 = Arg4;
    Arg1 = (uint32_t)((*(uint64_t *)(v_stack_m1B0)) & (1));
    if (condition_is_equal) goto loc_0025AE34;
    if (((uint32_t)(Arg1)) == 1) {
        result = *(uint64_t *)(arg4 + 0x8E58);
        Arg3 = *(uint64_t *)(arg4 + 0x8E58);
        Arg3 = (Arg3) + (8);
        Arg2 = *(uint8_t *)(result);
    }
    if ((uint32_t)(Arg2) == 0) goto loc_00259FF8;
loc_0025A950:
    if ((uint32_t)(Arg2 - 1) != 0) goto loc_0025A950;
    goto loc_00259FF8;
loc_0025A968:
    if ((((uint8_t)(Arg2 - 1)) & (16)) == 0) goto loc_0025A5C3;
    if ((uint8_t)(*(uint64_t *)(Arg3 + Arg2 - 0x1 * 8)) == 0) goto loc_0025A5C3;
loc_0025A978:
loc_0025A97C:
    if (*(uint64_t *)(v_stack_m1F0 + 0x10) == 0) goto loc_0025A20D;
    Arg1 = (v_stack_m12E + v_stack_m12E * 2) + (v_stack_m12E + v_stack_m12E * 2);
    if (v_stack_m12B == 2) goto loc_0025ADE0;
    v_stack_m110 = *(uint64_t *)(v_stack_m110 + 0x8);
    if ((uint32_t)(v_stack_m12C) == 0) goto loc_0025ABB3;
    if (((uint32_t)(v_stack_m12C)) != 1) goto loc_0025AA33;
    if ((((uint32_t)(v_stack_m12D)) & ((uint32_t)(v_stack_m12D - 1))) != 0) {
    }
    if (((*(uint32_t *)(local_rsi + 0x78)) & (0x400000ULL)) != 0) goto loc_0025AF13;
loc_0025A9F3:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi + 0xD8) + 0x8)) != (local_rsi + 216)) goto loc_0025AA09;
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi + 0xD8 + 0x8))) == (local_rsi + 216)) goto loc_0025AB3C;
loc_0025AA09:
loc_0025AA10:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi + 0xD8 + 0x8))) == (local_rsi + 216)) goto loc_0025AB1E;
loc_0025AA1B:
loc_0025AA2B:
    Arg3 = 0;
    result = KiUpdateSoftParkElectionStatisticsOnRemoval(*(uint64_t *)(*(uint64_t *)(v_stack_m128 + arg1 * 8 + 0x20) + 0x8E48), local_rsi, Arg3, *(uint64_t *)(*(uint64_t *)(v_stack_m128 + arg1 * 8 + 0x20) + 0x8E48));
loc_0025AA33:
loc_0025AA40:
    if (0 >= ((uint32_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8))))) goto loc_0025AA5E;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10)) == (*(uint64_t *)(v_stack_m1F0 + 0x10))) goto loc_0025AA5A;
    Arg2 = (uint32_t)((0) + 1);
    goto loc_0025AA40;
loc_0025AA5A:
loc_0025AA5E:
    local_r10 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsi + 0x78))) >> (1));
    result = (uint32_t)((*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10 + 0x20)) >> (1));
    local_r10 = (uint32_t)((local_r10) & (1));
    result = (uint32_t)((result) & (1));
    if (((uint32_t)(local_r10)) >= ((uint32_t)(result))) goto loc_0025AF75;
    if ((*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8))) <= 0) goto loc_0025AFD2;
loc_0025AA8C:
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10)) == (*(uint64_t *)(v_stack_m1F0 + 0x10))) goto loc_0025B120;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x28) - 1) <= -4) goto loc_0025B31C;
loc_0025AABB:
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x30)) | (1));
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x20) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x18);
    *(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x30) = (uint8_t)(result);
    result = (uint8_t)((result) & (253));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x18) + 0x78))) >> (1));
    Arg1 = (uint8_t)((Arg1) & (1));
    Arg1 = (uint8_t)((Arg1) + ((uint8_t)(Arg1)));
    Arg1 = (uint8_t)((Arg1) ^ ((uint8_t)(result)));
    Arg1 = (uint8_t)((Arg1) & (231));
    Arg1 = (uint8_t)((Arg1) | (4));
    Arg1 = (uint8_t)((Arg1) & (223));
    *(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x30) = (uint8_t)(Arg1);
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x28) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x18);
    result = KiIsPrcbThread(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x18), Arg2, *(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8)), *(uint64_t *)(arg1 + 0x37E8) + 0 + 0 * 4 * 8);
    if ((uint8_t)(result) == 0) {
        result = *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x24);
        *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x18) + 0x218) = (uint32_t)(result);
    }
    local_rbx = (uint32_t)((0) + 1);
    if (((uint32_t)(local_rbx)) < ((uint32_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8))))) goto loc_0025AA8C;
loc_0025AB14:
    goto loc_0025AFD2;
loc_0025AB1E:
    Arg2 = ~(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x2C8));
    goto loc_0025AA1B;
loc_0025AB3C:
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x2D0)) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x18);
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x18) + 0x8) = *(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x2D0);
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x2D0)) != (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x18))) goto loc_0025AA10;
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x8) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x8)));
    goto loc_0025AA10;
loc_0025AB60:
    goto loc_0025A459;
loc_0025AB68:
    if (*(uint64_t *)(local_rsi + 0x68) == 0) goto loc_0025A597;
    Arg2 = ((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x8)) + 0xD8))) + (*(uint64_t *)(local_rsi + 0x68));
    result = KiIsThreadConstrainedBySchedulingGroup(local_rsi, Arg2, *(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8)), 0);
    if ((uint8_t)(result) == 0) goto loc_0025A597;
    result = KiCheckForMaxOverQuotaScb(Arg2, Arg2, *(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8)), 0);
    if ((uint8_t)(result) == 0) goto loc_0025A597;
    result = KiShouldPreemptionBeDeferred(local_rsi, Arg2, *(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8)), 0);
    if ((uint8_t)(result) != 0) goto loc_0025A597;
    goto loc_0025A5C3;
loc_0025ABB3:
    if ((((uint32_t)(v_stack_m12D)) & ((uint32_t)(v_stack_m12D - 1))) != 0) {
    }
    if (((*(uint32_t *)(Arg2 - 0x60)) & (0x400000ULL)) != 0) goto loc_0025B108;
loc_0025ABD3:
    if ((*(uint64_t *)(*(uint64_t *)(Arg2) + 0x8)) != Arg2) goto loc_0025AA09;
    if ((*(uint64_t *)(*(uint64_t *)(Arg2 + 0x8))) != Arg2) goto loc_0025AA09;
    *(uint64_t *)(*(uint64_t *)(Arg2 + 0x8)) = *(uint64_t *)(Arg2);
    *(uint64_t *)(*(uint64_t *)(Arg2) + 0x8) = *(uint64_t *)(Arg2 + 0x8);
    if ((*(uint64_t *)(Arg2 + 0x8)) == (*(uint64_t *)(Arg2))) goto loc_0025AD3C;
loc_0025ABFD:
    if ((*(uint64_t *)(Arg2 + 0x8)) == (*(uint64_t *)(Arg2))) goto loc_0025AD65;
loc_0025AC0A:
    Arg2 = (Arg2) + (-216);
    goto loc_0025AA2B;
loc_0025AC2A:
    result = (0) + (0x844ULL);
    result = (result) << (4);
    result = (result) + (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x18));
    goto loc_0025A33E;
loc_0025AC40:
    result = (result) + (-88);
    if ((*(uint32_t *)(result + 0x7C)) > 0) goto loc_0025A399;
    goto loc_0025A39C;
loc_0025AC53:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x18) != 0) goto loc_0025AE21;
loc_0025AC5C:
    goto loc_0025A3D8;
loc_0025AC67:
    v_stack_m12E = (uint8_t)((uint8_t)(Arg2));
    v_stack_m120 = 0;
    v_stack_m128 = 0;
    v_stack_m134 = (uint32_t)(*(uint16_t *)(0 + 0x78));
    Arg2 = ((uint8_t)((uint8_t)(Arg2)) + (uint8_t)((uint8_t)(Arg2)) * 2) + ((uint8_t)((uint8_t)(Arg2)) + (uint8_t)((uint8_t)(Arg2)) * 2);
    result = (uint32_t)(*(uint32_t *)(v_stack_m128 + Arg2 * 8 + 0x40));
    if ((*(uint32_t *)(0 + 0x7C)) == ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m128 + Arg2 * 8 + 0x40))))) {
        result = *(uint32_t *)(v_stack_m128 + Arg2 * 8 + 0x44);
        result = (uint32_t)((result) & ((uint32_t)(*(uint16_t *)(0 + 0x78))));
        Arg1 = (uint32_t)(result);
        v_stack_m134 = (uint32_t)(result);
    }
    if ((uint32_t)(Arg1) == 0) goto loc_0025AD90;
loc_0025ACA1:
    Arg1 = ((uint8_t)(result)) + (9);
    v_stack_m190 = (uint32_t)(result);
    Arg1 = (Arg1) << (4);
    Arg1 = (Arg1) + (0);
    v_stack_m130 = (uint8_t)(result);
    v_stack_m118 = Arg1;
    v_stack_m110 = Arg1;
    goto loc_0025A401;
loc_0025ACC5:
    result = KiIsThreadExemptFromForcePark(local_rsi, Arg2, *(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8)), 0);
    if ((uint8_t)(result) == 0) goto loc_0025A5C3;
    goto loc_0025A4D8;
loc_0025ACDF:
    if (v_stack_m1E0 != ((uint8_t)(Arg2))) goto loc_0025A4E1;
    goto loc_0025A597;
loc_0025ACED:
    result = (0) + (0x844ULL);
    result = (result) << (4);
    result = (result) + (local_r10);
    goto loc_0025A700;
loc_0025AD03:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rsi + 0x74)))) & (8)) != 0) goto loc_0025A475;
    result = KiRemoveCurrentlyEnumeratedThreadFromReadyQueue(v_stack_m138, local_rsi, *(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8)), 0);
    result = KiEnterDeferredReadyState(local_rsi, local_rsi, *(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8)), 0);
    *(uint64_t *)(local_rsi + 0xD8) = *(uint64_t *)(v_stack_m1D8);
    *(uint64_t *)(v_stack_m1D8) = local_rsi + 216;
    goto loc_0025A20D;
loc_0025AD3C:
    *(uint32_t *)((uint8_t)(Arg2) + 0x83D8) = (uint32_t)((uint32_t)(*(uint32_t *)((uint8_t)(Arg2) + 0x83D8)));
    goto loc_0025ABFD;
loc_0025AD54:
    v_stack_m1E8 = 0;
    goto loc_0025A461;
loc_0025AD65:
    if ((*(uint64_t *)((uint8_t)(Arg2) + 0x8430)) != 0) goto loc_0025AC0A;
    Arg1 = ~(*(uint64_t *)((uint8_t)(Arg2) + 0xC8));
    goto loc_0025AC0A;
loc_0025AD90:
    result = KiAdvanceReadyQueueEnumeratorToNextScb(v_stack_m138, v_stack_m128, *(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8)), 0);
    if (!sign_flag) goto loc_0025AEBF;
    goto loc_0025A3F4;
loc_0025ADAF:
    result = (*(uint64_t *)(v_stack_m1E8 + 0x2C8)) & (v_stack_m128);
    if (((0) & (result)) != 0) goto loc_0025A5C3;
    goto loc_0025A58C;
loc_0025ADCC:
    result = (condition_is_above_or_equal) ? 1 : 0;
    goto loc_0025A31C;
loc_0025ADE0:
    v_stack_m1E0 = v_stack_m128;
    if ((*(uint64_t *)(v_stack_m128)) != v_stack_m118) goto loc_0025AECB;
    if ((*(uint64_t *)(v_stack_m128 + 0x8)) != v_stack_m118) goto loc_0025AECB;
    result = KiAdvanceReadyQueueEnumeratorToNextList(v_stack_m138, v_stack_m128, (uint32_t)(v_stack_m138), 0);
loc_0025AE09:
    result = KiRemoveThreadFromScbQueue((uint8_t)(Arg2), v_stack_m1E0, local_rsi, (uint32_t)((uint32_t)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10))));
    goto loc_0025AA33;
loc_0025AE21:
    if ((*(uint32_t *)(0 + 0x7C)) >= ((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10))) + 0x7C))))) goto loc_0025A3D8;
    goto loc_0025AC5C;
loc_0025AE34:
    goto loc_0025A950;
loc_0025AE43:
    local_rsi = ((uint32_t)((uint32_t)(*(uint64_t *)(v_stack_m1F0 + 0x10)))) + (11);
    local_rsi = (local_rsi) << (4);
    local_rsi = (local_rsi) + (*(uint64_t *)(arg1 + 0x37E8));
    if (((*(uint32_t *)(v_rip + 0xD6BCDD)) & (0x200000ULL)) == 0) goto loc_0025AEA5;
    if (*(uint64_t *)(local_rsi) != 0) goto loc_0025AE7E;
    if (*(uint64_t *)(local_rsi) == 0) goto loc_0025AE9A;
    result = KxWaitForLockChainValid(local_rsi, 1, v_stack_m1B0, (uint32_t)((uint32_t)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10))));
loc_0025AE7E:
    *(uint64_t *)(local_rsi) = 0;
    result = (uint8_t)((*(uint64_t *)(local_rsi + 0x8)) ^ ((uint8_t)(*(uint64_t *)(local_rsi + 0x8))));
    if ((((uint8_t)(result)) & (4)) != 0) {
        result = KeWakeAddressAll(result + 8, *(uint64_t *)(local_rsi + 0x8), v_stack_m1B0, (uint32_t)((uint32_t)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10))));
    }
    local_r12 = (uint32_t)((*(uint64_t *)(v_stack_m1F0 + 0x10)) + 1);
    goto loc_0025A853;
loc_0025AEA5:
    goto loc_0025AE9A;
loc_0025AEAB:
    result = (condition_is_above_or_equal) ? 1 : 0;
    goto loc_0025A6DE;
loc_0025AEBF:
    goto loc_0025ACA1;
loc_0025AECB:
    v_stack_m110 = *(uint64_t *)(v_stack_m110 + 0x8);
    goto loc_0025AE09;
loc_0025AEDC:
    if ((((uint8_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x30))) & (1)) != 0) goto loc_0025A978;
    if (((uint8_t)(*(uint8_t *)(local_rsi + 0xC3))) > (*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x20) + 0xC3))) goto loc_0025A978;
    if (((uint8_t)(*(uint8_t *)(local_rsi + 0xC3))) != (*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x20) + 0xC3))) goto loc_0025A968;
    if ((((uint8_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x30))) & (24)) != 0) goto loc_0025A978;
    goto loc_0025A968;
loc_0025AF13:
    goto loc_0025A9F3;
loc_0025AF2B:
loc_0025AF2E:
    if (0 >= ((uint32_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8))))) goto loc_0025AF6B;
    Arg1 = (0 * 4 + 2) + (0);
    if ((*(uint64_t *)(arg1 + 0x37E8) + Arg1 * 8) == ((uint8_t)(Arg2))) goto loc_0025AF66;
    Arg4 = 0;
    result = KiDoesThreadDominateRescheduleContextEntry(*(uint64_t *)(arg1 + 0x37E8) + Arg1 * 8, v_stack_m1F0, (uint32_t)((uint32_t)(local_rsi)), Arg4);
    if ((uint8_t)(result) == 0) goto loc_00259FF2;
loc_0025AF66:
    local_r13 = (uint32_t)((0) + 1);
    goto loc_0025AF2E;
loc_0025AF6B:
    goto loc_00259DBF;
loc_0025AF75:
    if ((uint32_t)(v_stack_m12F) != 0) goto loc_0025B178;
    if ((*(uint64_t *)(arg4 + 0x18) - 1) <= -4) goto loc_0025AFDB;
loc_0025AF8F:
    Arg1 = (uint8_t)((*(uint8_t *)(arg4 + 0x20)) & (254));
    *(uint64_t *)(arg4 + 0x10) = local_rsi;
    *(uint8_t *)(arg4 + 0x20) = (uint8_t)(Arg1);
    Arg1 = (uint8_t)((Arg1) & (253));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsi + 0x78))) >> (1));
    result = (uint8_t)((result) & (1));
    *(uint64_t *)(arg4 + 0x18) = local_rsi;
    result = (uint8_t)((result) + ((uint8_t)(result)));
    result = (uint8_t)((result) ^ ((uint8_t)(Arg1)));
    result = (uint8_t)((result) & (199));
    result = (uint8_t)((result) | (4));
    *(uint8_t *)(arg4 + 0x20) = (uint8_t)(result);
    if ((*(uint64_t *)(local_rsi + 0x220)) != (v_rip + 14110523)) goto loc_0025B670;
loc_0025AFD2:
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x4) = (uint32_t)(v_stack_m12F);
    goto loc_0025A1F0;
loc_0025AFDB:
    if ((*(uint64_t *)(*(uint64_t *)(arg4 + 0x18) + 0x220)) == (v_rip + 14110494)) goto loc_0025AF8F;
    if (((*(uint8_t *)(arg4 + 0x21)) & (1)) != 0) {
    }
    *(uint8_t *)(*(uint64_t *)(arg4 + 0x18) + 0x235) = 1;
    result = KiInsertDeferredReadyList(v_stack_m1D8, *(uint64_t *)(arg4 + 0x18), (uint32_t)((uint32_t)(local_rsi)), Arg4);
    goto loc_0025AF8F;
loc_0025B009:
    if (result <= -4) goto loc_0025B2ED;
loc_0025B013:
    Arg1 = (uint8_t)((*(uint8_t *)(arg4 + 0x30)) & (254));
    *(uint64_t *)(arg4 + 0x20) = v_stack_m12F;
    *(uint8_t *)(arg4 + 0x30) = (uint8_t)(Arg1);
    Arg1 = (uint8_t)((Arg1) & (253));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m12F + 0x78))) >> (1));
    result = (uint8_t)((result) & (1));
    *(uint64_t *)(arg4 + 0x28) = v_stack_m12F;
    result = (uint8_t)((result) + ((uint8_t)(result)));
    result = (uint8_t)((result) ^ ((uint8_t)(Arg1)));
    result = (uint8_t)((result) & (199));
    result = (uint8_t)((result) | (4));
    *(uint8_t *)(arg4 + 0x30) = (uint8_t)(result);
    Arg1 = (uint8_t)(((uint8_t)(*(uint64_t *)(arg4))) ^ ((uint8_t)(*(uint8_t *)(arg4 + 0x31))));
    Arg1 = (uint8_t)((Arg1) & (1));
    Arg1 = (uint8_t)((Arg1) ^ ((uint8_t)(*(uint8_t *)(arg4 + 0x31))));
    *(uint8_t *)(arg4 + 0x31) = (uint8_t)(Arg1);
    result = KiIsPrcbThread(v_stack_m12F, *(uint64_t *)(arg4 + 0x18), (uint32_t)((uint32_t)(local_rsi)), Arg4);
    if ((uint8_t)(result) != 0) goto loc_00259E9C;
    *(uint32_t *)(v_stack_m12F + 0x218) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m1F0 + 0x24)));
    goto loc_00259E9C;
loc_0025B072:
loc_0025B077:
    if (0 >= 0) goto loc_0025B09C;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x20)) == (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x8E80))) goto loc_0025B0D5;
loc_0025B09C:
    if (0 == 0) goto loc_00259D1C;
loc_0025B0AC:
    result = *(uint64_t *)(arg1 + 0x37E8) + 48 - 32;
    if ((*(uint64_t *)(arg1 + 0x37E8) + 48 - 32) != (*(uint64_t *)(arg1 + 0x37E8) + 0 + 0 * 4 * 8 + 16)) {
        result = *(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10 + 0x10);
        *(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x30 - 0x10) = result;
        result = *(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10 + 0x20);
        result = (uint8_t)((result) | (32));
        *(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x30) = (uint8_t)(result);
    }
    Arg1 = (*(uint64_t *)(arg1 + 0x37E8) + 48) + (40);
    Arg2 = (0) - (1);
    if (condition_is_not_equal) goto loc_0025B0AC;
    goto loc_00259D1C;
loc_0025B0D5:
    Arg2 = (uint32_t)((Arg2) + 1);
    goto loc_0025B077;
loc_0025B0D9:
    result = KiIsPrcbThread(Arg1, Arg2, *(uint64_t *)(arg1 + 0x37E8) + 0 + 0 * 4 * 8 + 16, Arg4);
    if ((uint8_t)(result) != 0) goto loc_00259E53;
    if (((*(uint8_t *)(arg4 + 0x31)) & (1)) != 0) {
    }
    *(uint8_t *)(arg1 + 0x235) = 1;
    result = KiInsertDeferredReadyList(v_stack_m1C8, Arg1, *(uint64_t *)(arg1 + 0x37E8) + 0 + 0 * 4 * 8 + 16, Arg4);
    goto loc_00259E53;
loc_0025B108:
    goto loc_0025ABD3;
loc_0025B120:
    if ((*(uint64_t *)(arg1 + 0x2F0)) <= -4) goto loc_0025B355;
loc_0025B12A:
    Arg1 = (uint8_t)((*(uint8_t *)(arg4 + 0x30)) & (254));
    *(uint64_t *)(arg4 + 0x20) = local_rsi;
    *(uint8_t *)(arg4 + 0x30) = (uint8_t)(Arg1);
    Arg1 = (uint8_t)((Arg1) & (253));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsi + 0x78))) >> (1));
    result = (uint8_t)((result) & (1));
    *(uint64_t *)(arg4 + 0x28) = local_rsi;
    result = (uint8_t)((result) + ((uint8_t)(result)));
    result = (uint8_t)((result) ^ ((uint8_t)(Arg1)));
    result = (uint8_t)((result) & (199));
    result = (uint8_t)((result) | (4));
    *(uint8_t *)(arg4 + 0x30) = (uint8_t)(result);
    result = KiIsPrcbThread(local_rsi, Arg1, *(uint64_t *)(arg1 + 0x37E8) + 0 + 0 * 4 * 8 + 16, Arg4);
    if ((uint8_t)(result) != 0) goto loc_0025AB06;
    *(uint32_t *)(local_rsi + 0x218) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m130 + 0x24)));
    goto loc_0025AB06;
loc_0025B178:
    if ((*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8))) <= 0) goto loc_0025AFD2;
loc_0025B188:
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10)) != local_r12) goto loc_0025B203;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x28) - 1) <= -4) goto loc_0025B384;
loc_0025B1AF:
    Arg1 = (uint8_t)((*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x30)) & (254));
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x20) = local_rsi;
    *(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x30) = (uint8_t)(Arg1);
    Arg1 = (uint8_t)((Arg1) & (253));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsi + 0x78))) >> (1));
    result = (uint8_t)((result) & (1));
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x28) = local_rsi;
    result = (uint8_t)((result) + ((uint8_t)(result)));
    result = (uint8_t)((result) ^ ((uint8_t)(Arg1)));
    result = (uint8_t)((result) & (199));
    result = (uint8_t)((result) | (4));
    *(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x30) = (uint8_t)(result);
    result = KiIsPrcbThread(local_rsi, Arg1, *(uint64_t *)(arg1 + 0x37E8) + 0 + 0 * 4 * 8 + 16, *(uint64_t *)(arg1 + 0x37E8) + 0 + 0 * 4 * 8);
    if ((uint8_t)(result) == 0) {
        result = *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x24);
        *(uint32_t *)(local_rsi + 0x218) = (uint32_t)(result);
    }
    local_rbx = (uint32_t)((0) + 1);
    if (((uint32_t)(local_rbx)) < ((uint32_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8))))) goto loc_0025B188;
    goto loc_0025AB14;
loc_0025B203:
    if ((*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8))) <= -4) goto loc_0025B3B3;
loc_0025B214:
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x30)) & (254));
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x20) = local_rsi;
    *(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x30) = (uint8_t)(result);
    result = (uint8_t)((result) & (253));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsi + 0x78))) >> (1));
    Arg1 = (uint8_t)((Arg1) & (1));
    Arg1 = (uint8_t)((Arg1) + ((uint8_t)(Arg1)));
    Arg1 = (uint8_t)((Arg1) ^ ((uint8_t)(result)));
    Arg1 = (uint8_t)((Arg1) & (231));
    Arg1 = (uint8_t)((Arg1) | (4));
    Arg1 = (uint8_t)((Arg1) | (32));
    result = (uint8_t)(((uint8_t)(Arg1)) & (223));
    Arg1 = (uint8_t)(Arg1);
    if (local_rsi == (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x8E80))) { Arg1 = (uint32_t)((uint8_t)(result)); }
    *(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x30) = (uint8_t)(Arg1);
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x28) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x8E80);
    result = KiIsPrcbThread(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x8E80), Arg1, *(uint64_t *)(arg1 + 0x37E8) + 0 + 0 * 4 * 8 + 16, *(uint64_t *)(arg1 + 0x37E8) + 0 + 0 * 4 * 8);
    if ((uint8_t)(result) != 0) goto loc_0025B1F4;
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x8E80) + 0x218) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x24)));
    goto loc_0025B1F4;
loc_0025B271:
    result = ~(*(uint64_t *)(arg1 + 0x68));
    goto loc_0025A1AF;
loc_0025B27D:
loc_0025B27F:
    if (0 < ((uint32_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8))))) goto loc_0025B2C2;
loc_0025B289:
    if (0 >= ((uint32_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8))))) goto loc_0025A20D;
    result = KiCanLocalReadyThreadBeScheduledToRescheduleContextEntry(*(uint64_t *)(arg1 + 0x37E8) + 0 + 0 * 4 * 8 + 16, local_rsi, v_stack_m1D0, v_stack_m1E8);
    if ((uint8_t)(result) != 0) goto loc_0025B34B;
    local_rbx = (uint32_t)((0) + 1);
    goto loc_0025B289;
loc_0025B2C2:
    Arg4 = 0;
    Arg3 = 0;
    Arg1 = ((uint32_t)((uint32_t)(local_rbx)) * 4 + 2) + ((uint32_t)((uint32_t)(local_rbx)));
    result = KiDoesThreadDominateRescheduleContextEntry(*(uint64_t *)(arg1 + 0x37E8) + Arg1 * 8, local_rsi, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0025A20D;
    local_rbx = (uint32_t)((local_rbx) + 1);
    goto loc_0025B27F;
loc_0025B2ED:
    result = KiIsPrcbThread(*(uint64_t *)(arg1 + 0x37E8) + Arg1 * 8, local_rsi, Arg3, Arg4);
    if ((uint8_t)(result) != 0) goto loc_0025B013;
    if (((*(uint8_t *)(arg4 + 0x31)) & (1)) != 0) {
    }
    *(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8) + arg1 * 8 + 0x235) = 1;
    result = KiInsertDeferredReadyList(v_stack_m1D8, *(uint64_t *)(arg1 + 0x37E8) + Arg1 * 8, Arg3, Arg4);
    goto loc_0025B013;
loc_0025B31C:
    result = KiIsPrcbThread(v_stack_m1D8, *(uint64_t *)(arg1 + 0x37E8) + Arg1 * 8, Arg3, Arg4);
    if ((uint8_t)(result) != 0) goto loc_0025AABB;
    if (((*(uint8_t *)(arg4 + 0x31)) & (1)) != 0) {
    }
    *(uint8_t *)(v_stack_m1D8 + 0x235) = 1;
    result = KiInsertDeferredReadyList(v_stack_m1D8, v_stack_m1D8, Arg3, Arg4);
    goto loc_0025AABB;
loc_0025B34B:
    goto loc_0025A97C;
loc_0025B355:
    result = KiIsPrcbThread(v_stack_m1D8, v_stack_m1D8, Arg3, Arg4);
    if ((uint8_t)(result) != 0) goto loc_0025B12A;
    if (((*(uint8_t *)(arg4 + 0x31)) & (1)) != 0) {
    }
    *(uint8_t *)(v_stack_m1D8 + 0x235) = 1;
    result = KiInsertDeferredReadyList(v_stack_m1D8, v_stack_m1D8, Arg3, Arg4);
    goto loc_0025B12A;
loc_0025B384:
    result = KiIsPrcbThread(v_stack_m1D8, v_stack_m1D8, Arg3, Arg4);
    if ((uint8_t)(result) != 0) goto loc_0025B1AF;
    if (((*(uint8_t *)(arg4 + 0x31)) & (1)) != 0) {
    }
    *(uint8_t *)(v_stack_m1D8 + 0x235) = 1;
    result = KiInsertDeferredReadyList(v_stack_m1D8, v_stack_m1D8, Arg3, Arg4);
    goto loc_0025B1AF;
loc_0025B3B3:
    result = KiIsPrcbThread(v_stack_m1D8, v_stack_m1D8, Arg3, Arg4);
    if ((uint8_t)(result) != 0) goto loc_0025B214;
    if (((*(uint8_t *)(arg4 + 0x31)) & (1)) != 0) {
    }
    *(uint8_t *)(v_stack_m1D8 + 0x235) = 1;
    result = KiInsertDeferredReadyList(v_stack_m1D8, v_stack_m1D8, Arg3, Arg4);
    goto loc_0025B214;
loc_0025B3E2:
    if ((uint32_t)(*(uint64_t *)(arg1 + 0x37E8) + 0 + 0 * 4 * 8) != 0) goto loc_0025B481;
    if ((*(uint64_t *)(arg4 + 0x18) - 1) <= -4) goto loc_0025B45A;
loc_0025B403:
    result = (uint8_t)((*(uint8_t *)(arg4 + 0x20)) & (254));
    *(uint64_t *)(arg4 + 0x10) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x8E80);
    *(uint8_t *)(arg4 + 0x20) = (uint8_t)(result);
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x8E80) + 0x78))) >> (1));
    Arg1 = (uint8_t)((Arg1) + ((uint8_t)(Arg1)));
    *(uint64_t *)(arg4 + 0x18) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x8E80);
    Arg1 = (uint8_t)((Arg1) ^ ((uint8_t)(result)));
    Arg1 = (uint8_t)((Arg1) & (2));
    Arg1 = (uint8_t)((Arg1) ^ ((uint8_t)(result)));
    Arg1 = (uint8_t)((Arg1) | (4));
    Arg1 = (uint8_t)((Arg1) & (199));
    *(uint8_t *)(arg4 + 0x20) = (uint8_t)(Arg1);
    Arg1 = (uint8_t)((v_stack_m1F8) ^ ((uint8_t)(*(uint8_t *)(arg4 + 0x21))));
    Arg1 = (uint8_t)((Arg1) & (1));
    Arg1 = (uint8_t)((Arg1) ^ ((uint8_t)(*(uint8_t *)(arg4 + 0x21))));
    *(uint8_t *)(arg4 + 0x21) = (uint8_t)(Arg1);
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x8E80) + 0x220)) != (v_rip + 14109450)) goto loc_0025B67F;
loc_0025B451:
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x4) = (uint32_t)(*(uint64_t *)(arg1 + 0x37E8) + 0 + 0 * 4 * 8);
    goto loc_0025A891;
loc_0025B45A:
    if ((*(uint64_t *)(*(uint64_t *)(arg4 + 0x18) + 0x220)) == (v_rip + 14109450)) goto loc_0025B403;
    if (((*(uint8_t *)(arg4 + 0x21)) & (1)) != 0) {
    }
    *(uint8_t *)(*(uint64_t *)(arg4 + 0x18) + 0x235) = 1;
    result = KiInsertDeferredReadyList(v_stack_m1D8, *(uint64_t *)(arg4 + 0x18), Arg3, Arg4);
    goto loc_0025B403;
loc_0025B481:
    if ((*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8))) <= 0) goto loc_0025B451;
loc_0025B493:
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10)) != (*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10))) goto loc_0025B52B;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x28) - 1) <= -4) goto loc_0025B5A3;
loc_0025B4BA:
    Arg1 = (uint8_t)((*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x30)) & (254));
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x20) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x8E80);
    *(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x30) = (uint8_t)(Arg1);
    Arg1 = (uint8_t)((Arg1) & (253));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x8E80) + 0x78))) >> (1));
    result = (uint8_t)((result) & (1));
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x28) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x8E80);
    result = (uint8_t)((result) + ((uint8_t)(result)));
    result = (uint8_t)((result) ^ ((uint8_t)(Arg1)));
    result = (uint8_t)((result) & (199));
    result = (uint8_t)((result) | (4));
    *(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x30) = (uint8_t)(result);
    Arg1 = (uint8_t)(((uint8_t)(v_stack_m1F8)) ^ ((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x31))));
    Arg1 = (uint8_t)((Arg1) & (1));
    Arg1 = (uint8_t)((Arg1) ^ ((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x31))));
    *(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x31) = (uint8_t)(Arg1);
    result = KiIsPrcbThread(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x8E80), *(uint64_t *)(arg4 + 0x18), Arg3, *(uint64_t *)(arg1 + 0x37E8) + 0 + 0 * 4 * 8);
    if ((uint8_t)(result) == 0) {
        result = *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x24);
        *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x8E80) + 0x218) = (uint32_t)(result);
    }
    local_rbx = (uint32_t)((0) + 1);
    if (((uint32_t)(local_rbx)) < ((uint32_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8))))) goto loc_0025B493;
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x4) = (uint32_t)(*(uint64_t *)(arg1 + 0x37E8) + 0 + 0 * 4 * 8);
    goto loc_0025A891;
loc_0025B52B:
    if ((*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8))) <= -4) goto loc_0025B5D2;
loc_0025B53C:
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x30)) & (254));
    *(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x30) = (uint8_t)(result);
    result = (uint8_t)((result) & (253));
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x20) = v_stack_m1F0;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m1F0 + 0x78))) >> (1));
    Arg1 = (uint8_t)((Arg1) & (1));
    Arg1 = (uint8_t)((Arg1) + ((uint8_t)(Arg1)));
    Arg1 = (uint8_t)((Arg1) ^ ((uint8_t)(result)));
    Arg1 = (uint8_t)((Arg1) & (231));
    Arg1 = (uint8_t)((Arg1) | (4));
    Arg1 = (uint8_t)((Arg1) | (32));
    result = (uint8_t)(((uint8_t)(Arg1)) & (223));
    Arg1 = (uint8_t)(Arg1);
    if (v_stack_m1F0 == (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x8E80))) { Arg1 = (uint32_t)((uint8_t)(result)); }
    *(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x30) = (uint8_t)(Arg1);
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x28) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x8E80);
    result = KiIsPrcbThread(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x8E80), v_stack_m1F0, Arg3, *(uint64_t *)(arg1 + 0x37E8) + 0 + 0 * 4 * 8);
    if ((uint8_t)(result) == 0) {
        result = *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x24);
        *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x8E80) + 0x218) = (uint32_t)(result);
    }
    goto loc_0025B50F;
loc_0025B5A3:
    result = KiIsPrcbThread(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x8E80), v_stack_m1F0, Arg3, *(uint64_t *)(arg1 + 0x37E8) + 0 + 0 * 4 * 8);
    if ((uint8_t)(result) != 0) goto loc_0025B4BA;
    if (((*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x31)) & (1)) != 0) {
    }
    *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x8E80) + 0x235) = 1;
    result = KiInsertDeferredReadyList(v_stack_m1C8, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x8E80), Arg3, *(uint64_t *)(arg1 + 0x37E8) + 0 + 0 * 4 * 8);
    goto loc_0025B4BA;
loc_0025B5D2:
    result = KiIsPrcbThread(v_stack_m1C8, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x8E80), Arg3, *(uint64_t *)(arg1 + 0x37E8) + 0 + 0 * 4 * 8);
    if ((uint8_t)(result) != 0) goto loc_0025B53C;
    if (((*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x31)) & (1)) != 0) {
    }
    *(uint8_t *)(v_stack_m1C8 + 0x235) = 1;
    result = KiInsertDeferredReadyList(v_stack_m1C8, v_stack_m1C8, Arg3, *(uint64_t *)(arg1 + 0x37E8) + 0 + 0 * 4 * 8);
    goto loc_0025B53C;
loc_0025B601:
    v_stack_m1F7 = 1;
loc_0025B609:
    v_stack_m1D0 = *(uint64_t *)(arg1 + 0x37E8) + 0 + 0 * 4 * 8;
    if (((*(uint32_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x78)) & (0x400000ULL)) == 0) goto loc_0025B64A;
    result = KiIsThreadStateControlledByProcessor(*(uint64_t *)(arg1 + 0x37E8) + 0 + 0 * 4 * 8, *(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10), Arg3, 1);
    local_r11 = v_stack_m1F8;
    if ((uint8_t)(result) != 0) {
        Arg4 = 1;
        Arg2 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10);
        Arg1 = *(uint64_t *)(arg1 + 0x37E8) + 0 + 0 * 4 * 8;
        result = KiUpdateVPBackingThreadPriority(Arg1, Arg2, Arg3, Arg4);
        local_r11 = v_stack_m1C0;
        Arg4 = v_stack_m1F7;
    }
loc_0025B64A:
    if ((uint8_t)(Arg4) == 0) goto loc_00259C81;
    *(uint64_t *)(v_stack_m1D0 + 0x40) = 0;
    goto loc_00259C81;
loc_0025B65C:
    if ((*(uint64_t *)(arg1 + 0x37E8) + 0 + 0 * 4 * 8) == v_stack_m1C8) goto loc_0025B609;
    if ((*(uint64_t *)(arg1 + 0x37E8) + 0 + 0 * 4 * 8) < v_stack_m1C8) goto loc_00259C81;
    goto loc_0025B601;
loc_0025B670:
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x218) = (uint32_t)((uint32_t)(*(uint32_t *)(local_r11 + 0x24)));
    goto loc_0025AFD2;
loc_0025B67F:
    *(uint32_t *)(v_stack_m1F0 + 0x218) = (uint32_t)((uint32_t)(*(uint32_t *)(local_r11 + 0x24)));
    goto loc_0025B451;
loc_0025B68F:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, v_stack_m1E0, Arg4);
    local_rsp = (local_rsp) + (496);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x37E8` | `64` | `R` |
| `Arg4` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00259B00&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
