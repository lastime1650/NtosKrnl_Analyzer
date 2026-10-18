# sub_0021D7F8

- RVA: `0x0021D7F8`–`0x0021EB7D` (길이 `4,997` bytes)
- VA: `0x000000014021D7F8`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005F0A8`
- 디코드: `1,211`개 명령, `4,997/4,997` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **54**; 고유 호출 대상: **42**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **12**

### Outgoing calls
- `0x0021D804` → [KiAbProcessPreContextSwitch](KiAbProcessPreContextSwitch_function_0021D420.md) (function, `0x0021D420`)
- `0x0021D863` → [KiUpdateTotalCyclesCurrentThread](../37/KiUpdateTotalCyclesCurrentThread_function_0037DE40.md) (function, `0x0037DE40`)
- `0x0021D936` → [KiAcquireKobjectLockSafe](../25/KiAcquireKobjectLockSafe_function_00251C90.md) (function, `0x00251C90`)
- `0x0021D977` → [KiComputeNewPriority](../3C/KiComputeNewPriority_function_003C2D8C.md) (function, `0x003C2D8C`)
- `0x0021D9F9` → [Feature_StackingDecayBoosts__private_IsEnabledNoReportingNoInline](../4E/Feature_StackingDecayBoosts__private_IsEnabledNoReportingNoInline_function_004EF7C0.md) (function, `0x004EF7C0`)
- `0x0021DA0C` → [KiComputeThreadPriority](../3C/KiComputeThreadPriority_function_003C45F4.md) (function, `0x003C45F4`)
- `0x0021DA3F` → [KiComputeThreadQos](../25/KiComputeThreadQos_function_00258010.md) (function, `0x00258010`)
- `0x0021DB7B` → [Feature_StackingDecayBoosts__private_IsEnabledNoReportingNoInline](../4E/Feature_StackingDecayBoosts__private_IsEnabledNoReportingNoInline_function_004EF7C0.md) (function, `0x004EF7C0`)
- `0x0021DBB3` → [KiComputeThreadPriority](../3C/KiComputeThreadPriority_function_003C45F4.md) (function, `0x003C45F4`)
- `0x0021DBF3` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0021DC02` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0021DCBA` → [KiQueryQuantumReset](KiQueryQuantumReset_function_0021F6B4.md) (function, `0x0021F6B4`)
- `0x0021DD22` → [KiComputeThreadQos](../25/KiComputeThreadQos_function_00258010.md) (function, `0x00258010`)
- `0x0021DD7B` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0021DD8A` → [KiStartRescheduleContext](../30/KiStartRescheduleContext_function_0030C6B0.md) (function, `0x0030C6B0`)
- `0x0021DE53` → [KiEvaluateGroupSchedulingPreemption](../25/KiEvaluateGroupSchedulingPreemption_function_00258270.md) (function, `0x00258270`)
- `0x0021DEB7` → [KiScheduleThreadToRescheduleContext](../30/KiScheduleThreadToRescheduleContext_function_0030C2A0.md) (function, `0x0030C2A0`)
- `0x0021DF13` → [KiCommitRescheduleContextEntry](../30/KiCommitRescheduleContextEntry_function_0030CFD0.md) (function, `0x0030CFD0`)
- `0x0021E079` → [EtwTraceThreadAffinity](../3C/EtwTraceThreadAffinity_function_003C29A0.md) (function, `0x003C29A0`)
- `0x0021E0A0` → [EtwTraceIdealProcessor](../3C/EtwTraceIdealProcessor_function_003C0808.md) (function, `0x003C0808`)
- `0x0021E0BD` → [KiAbProcessPostContextSwitch](../24/KiAbProcessPostContextSwitch_function_00248790.md) (function, `0x00248790`)
- `0x0021E21B` → [KiIsThreadConstrainedBySchedulingGroup](../30/KiIsThreadConstrainedBySchedulingGroup_function_0030B200.md) (function, `0x0030B200`)
- `0x0021E228` → [KiShouldPreemptionBeDeferred](../35/KiShouldPreemptionBeDeferred_function_00356310.md) (function, `0x00356310`)
- `0x0021E238` → [KiCheckForMaxOverQuotaScb](../20/KiCheckForMaxOverQuotaScb_function_002027A0.md) (function, `0x002027A0`)
- `0x0021E270` → [KiReadyDeferredReadyList](../30/KiReadyDeferredReadyList_function_0030DD80.md) (function, `0x0030DD80`)
- `0x0021E2AB` → [KiComputeNewPriorityNonStacking](../5C/KiComputeNewPriorityNonStacking_function_005CA75C.md) (function, `0x005CA75C`)
- `0x0021E300` → [Feature_StackingDecayBoosts__private_IsEnabledNoReportingNoInline](../4E/Feature_StackingDecayBoosts__private_IsEnabledNoReportingNoInline_function_004EF7C0.md) (function, `0x004EF7C0`)
- `0x0021E35A` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0021E369` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0021E3A3` → [KiRemoveSystemWorkPriorityKick](../26/KiRemoveSystemWorkPriorityKick_function_002631D0.md) (function, `0x002631D0`)
- `0x0021E3FC` → [KiCanThreadBeReadiedImmediately](../41/KiCanThreadBeReadiedImmediately_function_0041B530.md) (function, `0x0041B530`)
- `0x0021E413` → [KiDeferredReadyThread](../39/KiDeferredReadyThread_function_00398640.md) (function, `0x00398640`)
- `0x0021E44A` → [KiComputeThreadAffinity](../39/KiComputeThreadAffinity_function_00399DE0.md) (function, `0x00399DE0`)
- `0x0021E4AA` → [KiSearchForNewThreadsForRescheduleContext](../25/KiSearchForNewThreadsForRescheduleContext_function_00258620.md) (function, `0x00258620`)
- `0x0021E4E8` → [KiIsThreadConstrainedBySchedulingGroup](../30/KiIsThreadConstrainedBySchedulingGroup_function_0030B200.md) (function, `0x0030B200`)
- `0x0021E4F5` → [KiShouldPreemptionBeDeferred](../35/KiShouldPreemptionBeDeferred_function_00356310.md) (function, `0x00356310`)
- `0x0021E505` → [KiCheckForMaxOverQuotaScb](../20/KiCheckForMaxOverQuotaScb_function_002027A0.md) (function, `0x002027A0`)
- `0x0021E53F` → [KiGetComparisonRanks](../49/KiGetComparisonRanks_function_004975C4.md) (function, `0x004975C4`)
- `0x0021E57E` → [KiReadGuestSchedulerAssistPriority](../30/KiReadGuestSchedulerAssistPriority_function_00304BE4.md) (function, `0x00304BE4`)
- `0x0021E5BF` → [KiComputeThreadPriority](../3C/KiComputeThreadPriority_function_003C45F4.md) (function, `0x003C45F4`)
- `0x0021E719` → [KiFlushSoftwareInterruptBatch](../25/KiFlushSoftwareInterruptBatch_function_00252200.md) (function, `0x00252200`)
- `0x0021E744` → [KeAddProcessorAffinityEx](../25/KeAddProcessorAffinityEx_function_0025B6F0.md) (function, `0x0025B6F0`)
- `0x0021E75A` → [KeAddGroupAffinityEx](../25/KeAddGroupAffinityEx_function_0025B6C0.md) (function, `0x0025B6C0`)
- `0x0021E800` → [EtwTraceXSchedulerPriorityKickSend](../4F/EtwTraceXSchedulerPriorityKickSend_function_004FB2C0.md) (function, `0x004FB2C0`)
- `0x0021E82C` → [EtwTraceScheduleThread](../30/EtwTraceScheduleThread_function_0030B74C.md) (function, `0x0030B74C`)
- `0x0021E8E5` → [KiComputeNewPriority](../3C/KiComputeNewPriority_function_003C2D8C.md) (function, `0x003C2D8C`)
- `0x0021E91E` → [KiInswapAndReadyThread](../39/KiInswapAndReadyThread_function_00398318.md) (function, `0x00398318`)
- `0x0021E955` → [EtwTraceXSchedulerPriorityUpdate](../4D/EtwTraceXSchedulerPriorityUpdate_function_004D2358.md) (function, `0x004D2358`)
- `0x0021E9A8` → [KiDoesThreadDominateRescheduleContextEntry](../25/KiDoesThreadDominateRescheduleContextEntry_function_002581D0.md) (function, `0x002581D0`)
- `0x0021EA70` → [KiAbQueueAutoBoostDpc](../20/KiAbQueueAutoBoostDpc_function_002074D0.md) (function, `0x002074D0`)
- `0x0021EAB3` → [KiAbQueueAutoBoostDpc](../20/KiAbQueueAutoBoostDpc_function_002074D0.md) (function, `0x002074D0`)
- `0x0021EB21` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0021EB34` → [KiUpdateThreadPriority](../25/KiUpdateThreadPriority_function_00257810.md) (function, `0x00257810`)
- `0x0021EB6F` → [KiScheduleNextForegroundBoost](../5C/KiScheduleNextForegroundBoost_function_005C6670.md) (function, `0x005C6670`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0021D8AB` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x0021D9BE` → RVA `0x00FC50A0` (`ALMOSTRO`; read)
- `0x0021DA73` → RVA `0x00FC6BF8` (`ALMOSTRO`; read)
- `0x0021DB0E` → RVA `0x00FC6DB4` (`ALMOSTRO`; read)
- `0x0021DBE5` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)
- `0x0021DCBF` → RVA `0x00FC5098` (`ALMOSTRO`; read)
- `0x0021DE35` → RVA `0x00FC6ABC` (`ALMOSTRO`; read)
- `0x0021DEDF` → RVA `0x00FC6B14` (`ALMOSTRO`; read)
- `0x0021E084` → RVA `0x00FC6B10` (`ALMOSTRO`; read)
- `0x0021E45B` → RVA `0x00FC6B04` (`ALMOSTRO`; read)
- `0x0021E7B9` → RVA `0x00FC5007` (`ALMOSTRO`; read)
- `0x0021E7D0` → RVA `0x00FCD260` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **3**
  - `0x0021E7F4` → [sub_006D6954 + 0x7B](../6D/Unknown_function_006D6954.md) (`tail-transfer`)
  - `0x0021E806` → [sub_006D6954 + 0x7B](../6D/Unknown_function_006D6954.md) (`tail-transfer`)
  - `0x0021EB04` → [sub_006D6954](../6D/Unknown_function_006D6954.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0021D7F8  4C 89 AC 24 10 01 00 00         mov qword ptr [rsp + 0x110], r13
0021D800  4C 89 75 EF                     mov qword ptr [rbp - 0x11], r14
0021D804  E8 17 FC FF FF                  call 0x14021d420
0021D809  48 8B 43 68                     mov rax, qword ptr [rbx + 0x68]
0021D80D  44 89 7D A7                     mov dword ptr [rbp - 0x59], r15d
0021D811  48 85 C0                        test rax, rax
0021D814  0F 84 F0 09 00 00               je 0x14021e20a
0021D81A  44 8B AE D8 00 00 00            mov r13d, dword ptr [rsi + 0xd8]
0021D821  4C 03 E8                        add r13, rax
0021D824  0F 85 E8 09 00 00               jne 0x14021e212
0021D82A  0F B6 83 4B 02 00 00            movzx eax, byte ptr [rbx + 0x24b]
0021D831  48 8B 9B D0 00 00 00            mov rbx, qword ptr [rbx + 0xd0]
0021D838  48 8D 3C 40                     lea rdi, [rax + rax*2]
0021D83C  48 C1 E7 04                     shl rdi, 4
0021D840  48 03 FB                        add rdi, rbx
0021D843  0F B6 43 11                     movzx eax, byte ptr [rbx + 0x11]
0021D847  3C 05                           cmp al, 5
0021D849  0F 82 E0 00 00 00               jb 0x14021d92f
0021D84F  48 83 C3 30                     add rbx, 0x30
0021D853  48 3B DF                        cmp rbx, rdi
0021D856  75 EB                           jne 0x14021d843
0021D858  FA                              cli
0021D859  48 8B 4D 67                     mov rcx, qword ptr [rbp + 0x67]
0021D85D  45 33 C0                        xor r8d, r8d
0021D860  49 8B D6                        mov rdx, r14
0021D863  E8 D8 05 16 00                  call 0x14037de40
0021D868  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
0021D871  48 89 45 E7                     mov qword ptr [rbp - 0x19], rax
0021D875  4C 8B 81 B8 8E 00 00            mov r8, qword ptr [rcx + 0x8eb8]
0021D87C  4D 85 C0                        test r8, r8
0021D87F  0F 85 00 0B 00 00               jne 0x14021e385
0021D885  FB                              sti
0021D886  4C 8B 5D 97                     mov r11, qword ptr [rbp - 0x69]
0021D88A  41 8B DF                        mov ebx, r15d
0021D88D  49 8B 46 20                     mov rax, qword ptr [r14 + 0x20]
0021D891  48 89 45 DF                     mov qword ptr [rbp - 0x21], rax
0021D895  49 8B 4B 48                     mov rcx, qword ptr [r11 + 0x48]
0021D899  48 89 4D BF                     mov qword ptr [rbp - 0x41], rcx
0021D89D  0F 1F 00                        nop dword ptr [rax]
0021D8A0  F0 49 0F BA 6B 40 00            lock bts qword ptr [r11 + 0x40], 0
0021D8A7  73 1B                           jae 0x14021d8c4
0021D8A9  FF C3                           inc ebx
0021D8AB  85 1D FB 79 DA 00               test dword ptr [rip + 0xda79fb], ebx
0021D8B1  0F 84 95 0A 00 00               je 0x14021e34c
0021D8B7  F3 90                           pause
0021D8B9  49 8B 43 40                     mov rax, qword ptr [r11 + 0x40]
0021D8BD  48 85 C0                        test rax, rax
0021D8C0  74 DE                           je 0x14021d8a0
0021D8C2  EB E5                           jmp 0x14021d8a9
0021D8C4  41 F7 43 78 00 00 40 00         test dword ptr [r11 + 0x78], 0x400000
0021D8CC  4C 89 7D D7                     mov qword ptr [rbp - 0x29], r15
0021D8D0  0F 85 93 0C 00 00               jne 0x14021e569
0021D8D6  40 32 FF                        xor dil, dil
0021D8D9  41 B6 3F                        mov r14b, 0x3f
0021D8DC  41 80 BB C3 00 00 00 10         cmp byte ptr [r11 + 0xc3], 0x10
0021D8E4  B9 00 01 00 00                  mov ecx, 0x100
0021D8E9  41 B8 F0 0F 00 00               mov r8d, 0xff0
0021D8EF  0F 8D BF 0B 00 00               jge 0x14021e4b4
0021D8F5  48 8B 55 BF                     mov rdx, qword ptr [rbp - 0x41]
0021D8F9  48 B9 20 03 00 00 80 F7 FF FF   movabs rcx, 0xfffff78000000320
0021D903  32 DB                           xor bl, bl
0021D905  8B 09                           mov ecx, dword ptr [rcx]
0021D907  41 2B 8B B4 01 00 00            sub ecx, dword ptr [r11 + 0x1b4]
0021D90E  49 3B 53 20                     cmp rdx, qword ptr [r11 + 0x20]
0021D912  73 4E                           jae 0x14021d962
0021D914  41 80 BB 33 02 00 00 0E         cmp byte ptr [r11 + 0x233], 0xe
0021D91C  7D 4F                           jge 0x14021d96d
0021D91E  66 45 85 83 06 02 00 00         test word ptr [r11 + 0x206], r8w
0021D926  75 66                           jne 0x14021d98e
0021D928  83 F9 02                        cmp ecx, 2
0021D92B  72 61                           jb 0x14021d98e
0021D92D  EB 3E                           jmp 0x14021d96d
0021D92F  48 8B 73 20                     mov rsi, qword ptr [rbx + 0x20]
0021D933  48 8B CE                        mov rcx, rsi
0021D936  E8 55 43 03 00                  call 0x140251c90
0021D93B  80 7B 11 04                     cmp byte ptr [rbx + 0x11], 4
0021D93F  0F 85 3C 08 00 00               jne 0x14021e181
0021D945  48 8B 0B                        mov rcx, qword ptr [rbx]
0021D948  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
0021D94C  48 39 59 08                     cmp qword ptr [rcx + 8], rbx
0021D950  75 09                           jne 0x14021d95b
0021D952  48 39 18                        cmp qword ptr [rax], rbx
0021D955  0F 84 1F 08 00 00               je 0x14021e17a
0021D95B  B9 03 00 00 00                  mov ecx, 3
0021D960  CD 29                           int 0x29
0021D962  B3 04                           mov bl, 4
0021D964  83 F9 02                        cmp ecx, 2
0021D967  0F 82 DC 0B 00 00               jb 0x14021e549
0021D96D  40 B7 01                        mov dil, 1
0021D970  49 8B CB                        mov rcx, r11
0021D973  44 0F B6 C7                     movzx r8d, dil
0021D977  E8 10 54 1A 00                  call 0x1403c2d8c
0021D97C  4C 8B 5D 97                     mov r11, qword ptr [rbp - 0x69]
0021D980  45 84 FF                        test r15b, r15b
0021D983  45 0F B6 F6                     movzx r14d, r14b
0021D987  0F B6 C8                        movzx ecx, al
0021D98A  44 0F 44 F1                     cmove r14d, ecx
0021D98E  49 8B 83 20 02 00 00            mov rax, qword ptr [r11 + 0x220]
0021D995  8B 80 88 00 00 00               mov eax, dword ptr [rax + 0x88]
0021D99B  0F BA E0 0D                     bt eax, 0xd
0021D99F  73 03                           jae 0x14021d9a4
0021D9A1  80 CB 02                        or bl, 2
0021D9A4  41 8B 53 78                     mov edx, dword ptr [r11 + 0x78]
0021D9A8  0F B6 C3                        movzx eax, bl
0021D9AB  F6 C2 08                        test dl, 8
0021D9AE  F6 D0                           not al
0021D9B0  0F 94 C1                        sete cl
0021D9B3  22 C8                           and cl, al
0021D9B5  F6 C1 01                        test cl, 1
0021D9B8  0F 85 24 09 00 00               jne 0x14021e2e2
0021D9BE  83 3D DB 76 DA 00 00            cmp dword ptr [rip + 0xda76db], 0
0021D9C5  74 52                           je 0x14021da19
0021D9C7  80 E3 06                        and bl, 6
0021D9CA  80 FB 06                        cmp bl, 6
0021D9CD  0F 94 C1                        sete cl
0021D9D0  F6 C2 08                        test dl, 8
0021D9D3  0F 94 C0                        sete al
0021D9D6  84 C8                           test al, cl
0021D9D8  74 3F                           je 0x14021da19
0021D9DA  41 80 BB C3 00 00 00 00         cmp byte ptr [r11 + 0xc3], 0
0021D9E2  7E 35                           jle 0x14021da19
0021D9E4  40 80 CF 02                     or dil, 2
0021D9E8  EB 2F                           jmp 0x14021da19
0021D9EA  03 D8                           add ebx, eax
0021D9EC  B9 0F 00 00 00                  mov ecx, 0xf
0021D9F1  83 FB 10                        cmp ebx, 0x10
0021D9F4  0F 4D D9                        cmovge ebx, ecx
0021D9F7  2B D8                           sub ebx, eax
0021D9F9  E8 C2 1D 2D 00                  call 0x1404ef7c0
0021D9FE  45 33 C0                        xor r8d, r8d
0021DA01  88 9E 66 03 00 00               mov byte ptr [rsi + 0x366], bl
0021DA07  33 D2                           xor edx, edx
0021DA09  48 8B CE                        mov rcx, rsi
0021DA0C  E8 E3 6B 1A 00                  call 0x1403c45f4
0021DA11  4C 8B 5D 97                     mov r11, qword ptr [rbp - 0x69]
0021DA15  44 0F B6 F0                     movzx r14d, al
0021DA19  41 80 FE 3F                     cmp r14b, 0x3f
0021DA1D  74 4A                           je 0x14021da69
0021DA1F  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
0021DA28  45 3A B3 C3 00 00 00            cmp r14b, byte ptr [r11 + 0xc3]
0021DA2F  0F 8F 88 10 00 00               jg 0x14021eabd
0021DA35  49 8B CB                        mov rcx, r11
0021DA38  45 88 B3 C3 00 00 00            mov byte ptr [r11 + 0xc3], r14b
0021DA3F  E8 CC A5 03 00                  call 0x140258010
0021DA44  4C 8B 5D 97                     mov r11, qword ptr [rbp - 0x69]
0021DA48  41 0F B6 8B 04 02 00 00         movzx ecx, byte ptr [r11 + 0x204]
0021DA50  3B C1                           cmp eax, ecx
0021DA52  74 07                           je 0x14021da5b
0021DA54  41 88 83 04 02 00 00            mov byte ptr [r11 + 0x204], al
0021DA5B  41 F7 43 78 00 00 40 00         test dword ptr [r11 + 0x78], 0x400000
0021DA63  0F 85 11 08 00 00               jne 0x14021e27a
0021DA69  40 F6 C7 02                     test dil, 2
0021DA6D  0F 85 F9 10 00 00               jne 0x14021eb6c
0021DA73  48 8B 05 7E 91 DA 00            mov rax, qword ptr [rip + 0xda917e]
0021DA7A  83 E7 01                        and edi, 1
0021DA7D  C1 E7 05                        shl edi, 5
0021DA80  49 39 83 38 02 00 00            cmp qword ptr [r11 + 0x238], rax
0021DA87  0F 85 A4 09 00 00               jne 0x14021e431
0021DA8D  4C 8B 45 67                     mov r8, qword ptr [rbp + 0x67]
0021DA91  49 8B C0                        mov rax, r8
0021DA94  48 83 E0 FE                     and rax, 0xfffffffffffffffe
0021DA98  48 83 C8 01                     or rax, 1
0021DA9C  48 89 45 AF                     mov qword ptr [rbp - 0x51], rax
0021DAA0  49 8B 80 58 8E 00 00            mov rax, qword ptr [r8 + 0x8e58]
0021DAA7  0F B6 08                        movzx ecx, byte ptr [rax]
0021DAAA  4C 8D 70 08                     lea r14, [rax + 8]
0021DAAE  84 C9                           test cl, cl
0021DAB0  74 49                           je 0x14021dafb
0021DAB2  44 8B F9                        mov r15d, ecx
0021DAB5  66 66 66 0F 1F 84 00 00 00 00 00  nop word ptr [rax + rax]
0021DAC0  49 8B 1E                        mov rbx, qword ptr [r14]
0021DAC3  33 F6                           xor esi, esi
0021DAC5  F0 48 0F BA 6B 30 00            lock bts qword ptr [rbx + 0x30], 0
0021DACC  73 1B                           jae 0x14021dae9
0021DACE  FF C6                           inc esi
0021DAD0  85 35 D6 77 DA 00               test dword ptr [rip + 0xda77d6], esi
0021DAD6  0F 84 09 01 00 00               je 0x14021dbe5
0021DADC  F3 90                           pause
0021DADE  48 8B 43 30                     mov rax, qword ptr [rbx + 0x30]
0021DAE2  48 85 C0                        test rax, rax
0021DAE5  74 DE                           je 0x14021dac5
0021DAE7  EB E5                           jmp 0x14021dace
0021DAE9  49 83 C6 08                     add r14, 8
0021DAED  49 83 EF 01                     sub r15, 1
0021DAF1  75 CD                           jne 0x14021dac0
0021DAF3  4C 8B 5D 97                     mov r11, qword ptr [rbp - 0x69]
0021DAF7  4C 8B 45 67                     mov r8, qword ptr [rbp + 0x67]
0021DAFB  45 0F BE B3 C3 00 00 00         movsx r14d, byte ptr [r11 + 0xc3]
0021DB03  83 CF 0F                        or edi, 0xf
0021DB06  4C 8B 5D E7                     mov r11, qword ptr [rbp - 0x19]
0021DB0A  4C 8B 7D EF                     mov r15, qword ptr [rbp - 0x11]
0021DB0E  8B 15 A0 92 DA 00               mov edx, dword ptr [rip + 0xda92a0]
0021DB14  4C 8B 55 DF                     mov r10, qword ptr [rbp - 0x21]
0021DB18  49 03 D3                        add rdx, r11
0021DB1B  89 7D 7F                        mov dword ptr [rbp + 0x7f], edi
0021DB1E  41 0F BE B7 C3 00 00 00         movsx esi, byte ptr [r15 + 0xc3]
0021DB26  49 3B D2                        cmp rdx, r10
0021DB29  76 08                           jbe 0x14021db33
0021DB2B  8B C7                           mov eax, edi
0021DB2D  83 E0 FA                        and eax, 0xfffffffa
0021DB30  89 45 7F                        mov dword ptr [rbp + 0x7f], eax
0021DB33  8B CF                           mov ecx, edi
0021DB35  83 E1 FA                        and ecx, 0xfffffffa
0021DB38  49 3B D2                        cmp rdx, r10
0021DB3B  0F 46 CF                        cmovbe ecx, edi
0021DB3E  89 4D 7F                        mov dword ptr [rbp + 0x7f], ecx
0021DB41  45 84 E4                        test r12b, r12b
0021DB44  75 08                           jne 0x14021db4e
0021DB46  8B C1                           mov eax, ecx
0021DB48  83 E0 F3                        and eax, 0xfffffff3
0021DB4B  89 45 7F                        mov dword ptr [rbp + 0x7f], eax
0021DB4E  8B D9                           mov ebx, ecx
0021DB50  83 E3 F3                        and ebx, 0xfffffff3
0021DB53  45 84 E4                        test r12b, r12b
0021DB56  0F 45 D9                        cmovne ebx, ecx
0021DB59  45 33 E4                        xor r12d, r12d
0021DB5C  44 89 65 9F                     mov dword ptr [rbp - 0x61], r12d
0021DB60  44 3B F6                        cmp r14d, esi
0021DB63  0F 8F A3 00 00 00               jg 0x14021dc0c
0021DB69  F6 C3 04                        test bl, 4
0021DB6C  0F 85 F3 05 00 00               jne 0x14021e165
0021DB72  F6 C3 08                        test bl, 8
0021DB75  0F 84 C6 07 00 00               je 0x14021e341
0021DB7B  E8 40 1C 2D 00                  call 0x1404ef7c0
0021DB80  85 C0                           test eax, eax
0021DB82  0F 84 1D 07 00 00               je 0x14021e2a5
0021DB88  41 0F BE 8F C3 00 00 00         movsx ecx, byte ptr [r15 + 0xc3]
0021DB90  80 F9 10                        cmp cl, 0x10
0021DB93  0F 8D 5A 0D 00 00               jge 0x14021e8f3
0021DB99  44 39 25 00 75 DA 00            cmp dword ptr [rip + 0xda7500], r12d
0021DBA0  BA 0A 00 00 00                  mov edx, 0xa
0021DBA5  B8 0B 00 00 00                  mov eax, 0xb
0021DBAA  41 B0 01                        mov r8b, 1
0021DBAD  0F 45 D0                        cmovne edx, eax
0021DBB0  49 8B CF                        mov rcx, r15
0021DBB3  E8 3C 6A 1A 00                  call 0x1403c45f4
0021DBB8  8B D0                           mov edx, eax
0021DBBA  4C 8B 55 DF                     mov r10, qword ptr [rbp - 0x21]
0021DBBE  3B D6                           cmp edx, esi
0021DBC0  4C 8B 5D E7                     mov r11, qword ptr [rbp - 0x19]
0021DBC4  4C 8B 45 67                     mov r8, qword ptr [rbp + 0x67]
0021DBC8  0F 4F D6                        cmovg edx, esi
0021DBCB  89 55 9F                        mov dword ptr [rbp - 0x61], edx
0021DBCE  83 FA 10                        cmp edx, 0x10
0021DBD1  0F 8D 79 09 00 00               jge 0x14021e550
0021DBD7  41 3B D6                        cmp edx, r14d
0021DBDA  0F 8D FF 05 00 00               jge 0x14021e1df
0021DBE0  41 8B F6                        mov esi, r14d
0021DBE3  EB 35                           jmp 0x14021dc1a
0021DBE5  8B 05 CD 8E DA 00               mov eax, dword ptr [rip + 0xda8ecd]
0021DBEB  A8 40                           test al, 0x40
0021DBED  0F 84 E9 FE FF FF               je 0x14021dadc
0021DBF3  E8 98 18 0F 00                  call 0x14030f490
0021DBF8  84 C0                           test al, al
0021DBFA  0F 84 DC FE FF FF               je 0x14021dadc
0021DC00  8B CE                           mov ecx, esi
0021DC02  E8 59 18 0F 00                  call 0x14030f460
0021DC07  E9 D2 FE FF FF                  jmp 0x14021dade
0021DC0C  41 8B F6                        mov esi, r14d
0021DC0F  41 C6 87 35 02 00 00 01         mov byte ptr [r15 + 0x235], 1
0021DC17  83 E3 FE                        and ebx, 0xfffffffe
0021DC1A  49 8B 40 10                     mov rax, qword ptr [r8 + 0x10]
0021DC1E  8B FB                           mov edi, ebx
0021DC20  83 E7 FD                        and edi, 0xfffffffd
0021DC23  8B CB                           mov ecx, ebx
0021DC25  48 85 C0                        test rax, rax
0021DC28  0F 44 FB                        cmove edi, ebx
0021DC2B  48 8B 5D 67                     mov rbx, qword ptr [rbp + 0x67]
0021DC2F  8B D7                           mov edx, edi
0021DC31  83 E2 01                        and edx, 1
0021DC34  03 D6                           add edx, esi
0021DC36  48 8B 83 48 8E 00 00            mov rax, qword ptr [rbx + 0x8e48]
0021DC3D  44 8B 8B D8 83 00 00            mov r9d, dword ptr [rbx + 0x83d8]
0021DC44  8B 40 08                        mov eax, dword ptr [rax + 8]
0021DC47  44 0B C8                        or r9d, eax
0021DC4A  41 0F BD C1                     bsr eax, r9d
0021DC4E  89 45 CF                        mov dword ptr [rbp - 0x31], eax
0021DC51  3B D0                           cmp edx, eax
0021DC53  0F 8F 9C 04 00 00               jg 0x14021e0f5
0021DC59  83 E7 FD                        and edi, 0xfffffffd
0021DC5C  4C 8B 65 97                     mov r12, qword ptr [rbp - 0x69]
0021DC60  0F B6 83 D0 00 00 00            movzx eax, byte ptr [rbx + 0xd0]
0021DC67  49 8B 94 24 40 02 00 00         mov rdx, qword ptr [r12 + 0x240]
0021DC6F  66 3B 02                        cmp ax, word ptr [rdx]
0021DC72  73 14                           jae 0x14021dc88
0021DC74  0F B6 8B D1 00 00 00            movzx ecx, byte ptr [rbx + 0xd1]
0021DC7B  48 8B 54 C2 08                  mov rdx, qword ptr [rdx + rax*8 + 8]
0021DC80  48 D3 EA                        shr rdx, cl
0021DC83  F6 C2 01                        test dl, 1
0021DC86  75 03                           jne 0x14021dc8b
0021DC88  83 E7 FD                        and edi, 0xfffffffd
0021DC8B  41 8B 44 24 78                  mov eax, dword ptr [r12 + 0x78]
0021DC90  0F BA E0 11                     bt eax, 0x11
0021DC94  0F 83 7A 0B 00 00               jae 0x14021e814
0021DC9A  0F BA E0 14                     bt eax, 0x14
0021DC9E  0F 82 70 0B 00 00               jb 0x14021e814
0021DCA4  40 F6 C7 01                     test dil, 1
0021DCA8  0F 85 DF 04 00 00               jne 0x14021e18d
0021DCAE  44 8B FF                        mov r15d, edi
0021DCB1  40 F6 C7 20                     test dil, 0x20
0021DCB5  74 2B                           je 0x14021dce2
0021DCB7  49 8B CC                        mov rcx, r12
0021DCBA  E8 F5 19 00 00                  call 0x14021f6b4
0021DCBF  0F AF 05 D2 73 DA 00            imul eax, dword ptr [rip + 0xda73d2]
0021DCC6  8B C8                           mov ecx, eax
0021DCC8  48 03 4D BF                     add rcx, qword ptr [rbp - 0x41]
0021DCCC  41 8B 44 24 78                  mov eax, dword ptr [r12 + 0x78]
0021DCD1  A8 20                           test al, 0x20
0021DCD3  74 08                           je 0x14021dcdd
0021DCD5  F0 41 0F BA 74 24 78 05         lock btr dword ptr [r12 + 0x78], 5
0021DCDD  49 89 4C 24 20                  mov qword ptr [r12 + 0x20], rcx
0021DCE2  41 3B F6                        cmp esi, r14d
0021DCE5  74 64                           je 0x14021dd4b
0021DCE7  41 0F B7 8C 24 06 02 00 00      movzx ecx, word ptr [r12 + 0x206]
0021DCF0  8B C1                           mov eax, ecx
0021DCF2  C1 E8 04                        shr eax, 4
0021DCF5  0F B6 C0                        movzx eax, al
0021DCF8  3B C6                           cmp eax, esi
0021DCFA  0F 8C E6 04 00 00               jl 0x14021e1e6
0021DD00  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
0021DD09  41 3A B4 24 C3 00 00 00         cmp sil, byte ptr [r12 + 0xc3]
0021DD11  0F 8F BB 0D 00 00               jg 0x14021ead2
0021DD17  49 8B CC                        mov rcx, r12
0021DD1A  41 88 B4 24 C3 00 00 00         mov byte ptr [r12 + 0xc3], sil
0021DD22  E8 E9 A2 03 00                  call 0x140258010
0021DD27  41 0F B6 8C 24 04 02 00 00      movzx ecx, byte ptr [r12 + 0x204]
0021DD30  3B C1                           cmp eax, ecx
0021DD32  74 08                           je 0x14021dd3c
0021DD34  41 88 84 24 04 02 00 00         mov byte ptr [r12 + 0x204], al
0021DD3C  41 F7 44 24 78 00 00 40 00      test dword ptr [r12 + 0x78], 0x400000
0021DD45  0F 85 6A 05 00 00               jne 0x14021e2b5
0021DD4B  8B 45 6F                        mov eax, dword ptr [rbp + 0x6f]
0021DD4E  41 88 84 24 37 02 00 00         mov byte ptr [r12 + 0x237], al
0021DD56  41 C6 84 24 36 02 00 00 00      mov byte ptr [r12 + 0x236], 0
0021DD5F  41 F6 C7 02                     test r15b, 2
0021DD63  0F 84 7F 03 00 00               je 0x14021e0e8
0021DD69  4C 8B AB E8 37 00 00            mov r13, qword ptr [rbx + 0x37e8]
0021DD70  33 D2                           xor edx, edx
0021DD72  49 8B CD                        mov rcx, r13
0021DD75  41 B8 F0 00 00 00               mov r8d, 0xf0
0021DD7B  E8 C0 8E 4A 00                  call 0x1406c6c40
0021DD80  4D 8B C4                        mov r8, r12
0021DD83  48 8D 55 AF                     lea rdx, [rbp - 0x51]
0021DD87  49 8B CD                        mov rcx, r13
0021DD8A  E8 21 E9 0E 00                  call 0x14030c6b0
0021DD8F  45 0F B6 4D 00                  movzx r9d, byte ptr [r13]
0021DD94  33 F6                           xor esi, esi
0021DD96  44 8B C6                        mov r8d, esi
0021DD99  8B D6                           mov edx, esi
0021DD9B  0F 1F 44 00 00                  nop dword ptr [rax + rax]
0021DDA0  41 3B D1                        cmp edx, r9d
0021DDA3  73 20                           jae 0x14021ddc5
0021DDA5  8B C2                           mov eax, edx
0021DDA7  48 8D 0C 80                     lea rcx, [rax + rax*4]
0021DDAB  48 8D 04 CD 00 00 00 00         lea rax, [rcx*8]
0021DDB3  4A 39 5C 28 10                  cmp qword ptr [rax + r13 + 0x10], rbx
0021DDB8  74 04                           je 0x14021ddbe
0021DDBA  FF C2                           inc edx
0021DDBC  EB E2                           jmp 0x14021dda0
0021DDBE  4D 8D 45 10                     lea r8, [r13 + 0x10]
0021DDC2  4C 03 C0                        add r8, rax
0021DDC5  41 80 48 22 02                  or byte ptr [r8 + 0x22], 2
0021DDCA  41 0F B6 50 20                  movzx edx, byte ptr [r8 + 0x20]
0021DDCF  49 8B 08                        mov rcx, qword ptr [r8]
0021DDD2  48 8B 41 18                     mov rax, qword ptr [rcx + 0x18]
0021DDD6  49 89 40 10                     mov qword ptr [r8 + 0x10], rax
0021DDDA  0F B6 C2                        movzx eax, dl
0021DDDD  24 C5                           and al, 0xc5
0021DDDF  0C 05                           or al, 5
0021DDE1  41 88 40 20                     mov byte ptr [r8 + 0x20], al
0021DDE5  48 8B 41 18                     mov rax, qword ptr [rcx + 0x18]
0021DDE9  41 80 60 21 FE                  and byte ptr [r8 + 0x21], 0xfe
0021DDEE  49 89 40 18                     mov qword ptr [r8 + 0x18], rax
0021DDF2  F6 C2 02                        test dl, 2
0021DDF5  0F 85 C7 0B 00 00               jne 0x14021e9c2
0021DDFB  45 0F B6 45 00                  movzx r8d, byte ptr [r13]
0021DE00  48 8B DE                        mov rbx, rsi
0021DE03  4C 8B 4D 67                     mov r9, qword ptr [rbp + 0x67]
0021DE07  8B D6                           mov edx, esi
0021DE09  0F 1F 80 00 00 00 00            nop dword ptr [rax]
0021DE10  41 3B D0                        cmp edx, r8d
0021DE13  73 20                           jae 0x14021de35
0021DE15  8B C2                           mov eax, edx
0021DE17  48 8D 0C 80                     lea rcx, [rax + rax*4]
0021DE1B  48 8D 04 CD 00 00 00 00         lea rax, [rcx*8]
0021DE23  4E 39 4C 28 10                  cmp qword ptr [rax + r13 + 0x10], r9
0021DE28  74 04                           je 0x14021de2e
0021DE2A  FF C2                           inc edx
0021DE2C  EB E2                           jmp 0x14021de10
0021DE2E  49 8D 5D 10                     lea rbx, [r13 + 0x10]
0021DE32  48 03 D8                        add rbx, rax
0021DE35  40 38 35 80 8C DA 00            cmp byte ptr [rip + 0xda8c80], sil
0021DE3C  48 89 75 17                     mov qword ptr [rbp + 0x17], rsi
0021DE40  0F 84 F0 09 00 00               je 0x14021e836
0021DE46  4C 8D 4D 17                     lea r9, [rbp + 0x17]
0021DE4A  45 33 C0                        xor r8d, r8d
0021DE4D  49 8B D4                        mov rdx, r12
0021DE50  48 8B CB                        mov rcx, rbx
0021DE53  E8 18 A4 03 00                  call 0x140258270
0021DE58  84 C0                           test al, al
0021DE5A  74 23                           je 0x14021de7f
0021DE5C  41 8B 4C 24 78                  mov ecx, dword ptr [r12 + 0x78]
0021DE61  0F B6 43 20                     movzx eax, byte ptr [rbx + 0x20]
0021DE65  D1 E9                           shr ecx, 1
0021DE67  D1 E8                           shr eax, 1
0021DE69  83 E1 01                        and ecx, 1
0021DE6C  83 E0 01                        and eax, 1
0021DE6F  3B C8                           cmp ecx, eax
0021DE71  0F 42 C8                        cmovb ecx, eax
0021DE74  83 F9 01                        cmp ecx, 1
0021DE77  0F 84 F6 0A 00 00               je 0x14021e973
0021DE7D  B0 01                           mov al, 1
0021DE7F  0F B6 C0                        movzx eax, al
0021DE82  8D 3C 00                        lea edi, [rax + rax]
0021DE85  41 33 FF                        xor edi, r15d
0021DE88  83 E7 02                        and edi, 2
0021DE8B  41 33 FF                        xor edi, r15d
0021DE8E  A8 01                           test al, 1
0021DE90  0F 84 52 02 00 00               je 0x14021e0e8
0021DE96  4C 8B 7D 67                     mov r15, qword ptr [rbp + 0x67]
0021DE9A  48 8D 45 C7                     lea rax, [rbp - 0x39]
0021DE9E  4D 8B C7                        mov r8, r15
0021DEA1  41 88 B4 24 35 02 00 00         mov byte ptr [r12 + 0x235], sil
0021DEA9  45 33 C9                        xor r9d, r9d
0021DEAC  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0021DEB1  49 8B D4                        mov rdx, r12
0021DEB4  49 8B CD                        mov rcx, r13
0021DEB7  E8 E4 E3 0E 00                  call 0x14030c2a0
0021DEBC  0F B6 C0                        movzx eax, al
0021DEBF  8B D8                           mov ebx, eax
0021DEC1  C1 E3 07                        shl ebx, 7
0021DEC4  33 DF                           xor ebx, edi
0021DEC6  81 E3 80 00 00 00               and ebx, 0x80
0021DECC  33 DF                           xor ebx, edi
0021DECE  A8 01                           test al, 1
0021DED0  0F 85 CD 05 00 00               jne 0x14021e4a3
0021DED6  45 32 F6                        xor r14b, r14b
0021DED9  41 BC 02 00 00 00               mov r12d, 2
0021DEDF  F7 05 2B 8C DA 00 00 04 00 00   test dword ptr [rip + 0xda8c2b], 0x400
0021DEE9  41 0F 45 F4                     cmovne esi, r12d
0021DEED  33 FF                           xor edi, edi
0021DEEF  41 38 7D 00                     cmp byte ptr [r13], dil
0021DEF3  76 31                           jbe 0x14021df26
0021DEF5  8B CF                           mov ecx, edi
0021DEF7  4C 8D 4D C7                     lea r9, [rbp - 0x39]
0021DEFB  49 03 CC                        add rcx, r12
0021DEFE  44 8B C6                        mov r8d, esi
0021DF01  49 8B D7                        mov rdx, r15
0021DF04  48 8D 0C B9                     lea rcx, [rcx + rdi*4]
0021DF08  48 8D 0C CD 00 00 00 00         lea rcx, [rcx*8]
0021DF10  49 03 CD                        add rcx, r13
0021DF13  E8 B8 F0 0E 00                  call 0x14030cfd0
0021DF18  44 0A F0                        or r14b, al
0021DF1B  FF C7                           inc edi
0021DF1D  41 0F B6 45 00                  movzx eax, byte ptr [r13]
0021DF22  3B F8                           cmp edi, eax
0021DF24  72 CF                           jb 0x14021def5
0021DF26  41 83 7D 08 01                  cmp dword ptr [r13 + 8], 1
0021DF2B  75 1C                           jne 0x14021df49
0021DF2D  49 8B 45 10                     mov rax, qword ptr [r13 + 0x10]
0021DF31  48 8B 88 58 8E 00 00            mov rcx, qword ptr [rax + 0x8e58]
0021DF38  0F B6 41 01                     movzx eax, byte ptr [rcx + 1]
0021DF3C  FE C0                           inc al
0021DF3E  88 41 01                        mov byte ptr [rcx + 1], al
0021DF41  3A 01                           cmp al, byte ptr [rcx]
0021DF43  72 04                           jb 0x14021df49
0021DF45  C6 41 01 00                     mov byte ptr [rcx + 1], 0
0021DF49  48 8B 45 AF                     mov rax, qword ptr [rbp - 0x51]
0021DF4D  45 33 C0                        xor r8d, r8d
0021DF50  4C 8B C8                        mov r9, rax
0021DF53  41 0F B6 FE                     movzx edi, r14b
0021DF57  C1 E7 08                        shl edi, 8
0021DF5A  49 83 E1 FE                     and r9, 0xfffffffffffffffe
0021DF5E  33 FB                           xor edi, ebx
0021DF60  4C 89 4D 1F                     mov qword ptr [rbp + 0x1f], r9
0021DF64  81 E7 00 01 00 00               and edi, 0x100
0021DF6A  33 D2                           xor edx, edx
0021DF6C  33 FB                           xor edi, ebx
0021DF6E  83 E0 01                        and eax, 1
0021DF71  0F 84 F5 01 00 00               je 0x14021e16c
0021DF77  83 F8 01                        cmp eax, 1
0021DF7A  75 15                           jne 0x14021df91
0021DF7C  49 8B 81 58 8E 00 00            mov rax, qword ptr [r9 + 0x8e58]
0021DF83  4D 8B 81 58 8E 00 00            mov r8, qword ptr [r9 + 0x8e58]
0021DF8A  49 83 C0 08                     add r8, 8
0021DF8E  0F B6 10                        movzx edx, byte ptr [rax]
0021DF91  85 D2                           test edx, edx
0021DF93  74 1E                           je 0x14021dfb3
0021DF95  66 66 66 0F 1F 84 00 00 00 00 00  nop word ptr [rax + rax]
0021DFA0  8D 42 FF                        lea eax, [rdx - 1]
0021DFA3  49 8B 0C C0                     mov rcx, qword ptr [r8 + rax*8]
0021DFA7  8B D0                           mov edx, eax
0021DFA9  F0 48 83 61 30 00               lock and qword ptr [rcx + 0x30], 0
0021DFAF  85 C0                           test eax, eax
0021DFB1  75 ED                           jne 0x14021dfa0
0021DFB3  48 8B 45 97                     mov rax, qword ptr [rbp - 0x69]
0021DFB7  33 DB                           xor ebx, ebx
0021DFB9  83 CF 50                        or edi, 0x50
0021DFBC  48 89 5D AF                     mov qword ptr [rbp - 0x51], rbx
0021DFC0  89 7D 7F                        mov dword ptr [rbp + 0x7f], edi
0021DFC3  48 89 58 40                     mov qword ptr [rax + 0x40], rbx
0021DFC7  0F BA E7 08                     bt edi, 8
0021DFCB  0F 82 48 06 00 00               jb 0x14021e619
0021DFD1  48 83 7D C7 00                  cmp qword ptr [rbp - 0x39], 0
0021DFD6  0F 85 8D 02 00 00               jne 0x14021e269
0021DFDC  4C 8B 65 97                     mov r12, qword ptr [rbp - 0x69]
0021DFE0  33 F6                           xor esi, esi
0021DFE2  40 F6 C7 40                     test dil, 0x40
0021DFE6  75 53                           jne 0x14021e03b
0021DFE8  48 8B CB                        mov rcx, rbx
0021DFEB  44 8B C6                        mov r8d, esi
0021DFEE  48 83 E1 FE                     and rcx, 0xfffffffffffffffe
0021DFF2  8B D6                           mov edx, esi
0021DFF4  48 89 4D 97                     mov qword ptr [rbp - 0x69], rcx
0021DFF8  83 E3 01                        and ebx, 1
0021DFFB  0F 84 56 01 00 00               je 0x14021e157
0021E001  83 FB 01                        cmp ebx, 1
0021E004  75 15                           jne 0x14021e01b
0021E006  48 8B 81 58 8E 00 00            mov rax, qword ptr [rcx + 0x8e58]
0021E00D  4C 8B 81 58 8E 00 00            mov r8, qword ptr [rcx + 0x8e58]
0021E014  49 83 C0 08                     add r8, 8
0021E018  0F B6 10                        movzx edx, byte ptr [rax]
0021E01B  85 D2                           test edx, edx
0021E01D  74 13                           je 0x14021e032
0021E01F  90                              nop
0021E020  8D 42 FF                        lea eax, [rdx - 1]
0021E023  49 8B 0C C0                     mov rcx, qword ptr [r8 + rax*8]
0021E027  8B D0                           mov edx, eax
0021E029  F0 48 21 71 30                  lock and qword ptr [rcx + 0x30], rsi
0021E02E  85 C0                           test eax, eax
0021E030  75 EE                           jne 0x14021e020
0021E032  48 89 75 AF                     mov qword ptr [rbp - 0x51], rsi
0021E036  49 89 74 24 40                  mov qword ptr [r12 + 0x40], rsi
0021E03B  F7 C7 00 06 00 00               test edi, 0x600
0021E041  74 6C                           je 0x14021e0af
0021E043  0F BA E7 09                     bt edi, 9
0021E047  73 35                           jae 0x14021e07e
0021E049  45 8B 44 24 74                  mov r8d, dword ptr [r12 + 0x74]
0021E04E  45 33 C9                        xor r9d, r9d
0021E051  49 8B 84 24 40 02 00 00         mov rax, qword ptr [r12 + 0x240]
0021E059  49 8B CC                        mov rcx, r12
0021E05C  41 0F B7 94 24 48 02 00 00      movzx edx, word ptr [r12 + 0x248]
0021E065  41 C1 E8 03                     shr r8d, 3
0021E069  41 80 E0 01                     and r8b, 1
0021E06D  66 C7 44 24 28 36 05            mov word ptr [rsp + 0x28], 0x536
0021E074  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0021E079  E8 22 49 1A 00                  call 0x1403c29a0
0021E07E  0F BA E7 0A                     bt edi, 0xa
0021E082  73 21                           jae 0x14021e0a5
0021E084  F7 05 82 8A DA 00 00 00 00 08   test dword ptr [rip + 0xda8a82], 0x8000000
0021E08E  74 15                           je 0x14021e0a5
0021E090  44 8B 4D B7                     mov r9d, dword ptr [rbp - 0x49]
0021E094  BA 46 05 00 00                  mov edx, 0x546
0021E099  44 8B 45 BB                     mov r8d, dword ptr [rbp - 0x45]
0021E09D  49 8B CC                        mov rcx, r12
0021E0A0  E8 63 27 1A 00                  call 0x1403c0808
0021E0A5  66 F0 41 FF 8C 24 64 03 00 00   lock dec word ptr [r12 + 0x364]
0021E0AF  40 F6 C7 10                     test dil, 0x10
0021E0B3  0F 84 F4 02 00 00               je 0x14021e3ad
0021E0B9  48 8B 4D EF                     mov rcx, qword ptr [rbp - 0x11]
0021E0BD  E8 CE A6 02 00                  call 0x140248790
0021E0C2  49 83 BF 08 2D 00 00 00         cmp qword ptr [r15 + 0x2d08], 0
0021E0CA  4C 8B AC 24 10 01 00 00         mov r13, qword ptr [rsp + 0x110]
0021E0D2  0F 94 C0                        sete al
0021E0D5  48 81 C4 C0 00 00 00            add rsp, 0xc0
0021E0DC  41 5F                           pop r15
0021E0DE  41 5E                           pop r14
0021E0E0  41 5C                           pop r12
0021E0E2  5F                              pop rdi
0021E0E3  5E                              pop rsi
0021E0E4  5B                              pop rbx
0021E0E5  5D                              pop rbp
0021E0E6  C3                              ret
0021E0E7  CC                              int3
0021E0E8  48 8B 5D AF                     mov rbx, qword ptr [rbp - 0x51]
0021E0EC  4C 8B 7D 67                     mov r15, qword ptr [rbp + 0x67]
0021E0F0  E9 EB FE FF FF                  jmp 0x14021dfe0
0021E0F5  44 39 65 A7                     cmp dword ptr [rbp - 0x59], r12d
0021E0F9  0F 84 5D FB FF FF               je 0x14021dc5c
0021E0FF  41 83 F9 01                     cmp r9d, 1
0021E103  0F 87 50 FB FF FF               ja 0x14021dc59
0021E109  49 8B 85 A8 01 00 00            mov rax, qword ptr [r13 + 0x1a8]
0021E110  44 8B 40 7C                     mov r8d, dword ptr [rax + 0x7c]
0021E114  48 8D 83 30 84 00 00            lea rax, [rbx + 0x8430]
0021E11B  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
0021E11F  F6 C1 01                        test cl, 1
0021E122  0F 85 E0 07 00 00               jne 0x14021e908
0021E128  48 8B C1                        mov rax, rcx
0021E12B  48 85 C0                        test rax, rax
0021E12E  0F 84 28 FB FF FF               je 0x14021dc5c
0021E134  8B 48 24                        mov ecx, dword ptr [rax + 0x24]
0021E137  41 3B C8                        cmp ecx, r8d
0021E13A  0F 85 E8 07 00 00               jne 0x14021e928
0021E140  0F B7 40 20                     movzx eax, word ptr [rax + 0x20]
0021E144  0F BD C8                        bsr ecx, eax
0021E147  89 4D D3                        mov dword ptr [rbp - 0x2d], ecx
0021E14A  3B D1                           cmp edx, ecx
0021E14C  0F 8F 0A FB FF FF               jg 0x14021dc5c
0021E152  E9 02 FB FF FF                  jmp 0x14021dc59
0021E157  4C 8D 45 97                     lea r8, [rbp - 0x69]
0021E15B  BA 01 00 00 00                  mov edx, 1
0021E160  E9 BB FE FF FF                  jmp 0x14021e020
0021E165  8B D6                           mov edx, esi
0021E167  E9 5F FA FF FF                  jmp 0x14021dbcb
0021E16C  4C 8D 45 1F                     lea r8, [rbp + 0x1f]
0021E170  BA 01 00 00 00                  mov edx, 1
0021E175  E9 26 FE FF FF                  jmp 0x14021dfa0
0021E17A  48 89 08                        mov qword ptr [rax], rcx
0021E17D  48 89 41 08                     mov qword ptr [rcx + 8], rax
0021E181  F0 81 26 7F FF FF FF            lock and dword ptr [rsi], 0xffffff7f
0021E188  E9 C2 F6 FF FF                  jmp 0x14021d84f
0021E18D  41 0F A3 F1                     bt r9d, esi
0021E191  0F 93 C1                        setae cl
0021E194  40 F6 C7 02                     test dil, 2
0021E198  0F 95 C0                        setne al
0021E19B  84 C8                           test al, cl
0021E19D  48 8B 4D BF                     mov rcx, qword ptr [rbp - 0x41]
0021E1A1  0F 84 76 02 00 00               je 0x14021e41d
0021E1A7  49 2B CB                        sub rcx, r11
0021E1AA  49 03 CA                        add rcx, r10
0021E1AD  40 F6 C7 02                     test dil, 2
0021E1B1  0F 84 C0 01 00 00               je 0x14021e377
0021E1B7  83 E7 DF                        and edi, 0xffffffdf
0021E1BA  F0 41 0F BA 6C 24 78 05         lock bts dword ptr [r12 + 0x78], 5
0021E1C2  49 89 4C 24 20                  mov qword ptr [r12 + 0x20], rcx
0021E1C7  4D 89 5F 20                     mov qword ptr [r15 + 0x20], r11
0021E1CB  E9 DE FA FF FF                  jmp 0x14021dcae
0021E1D0  41 3B D6                        cmp edx, r14d
0021E1D3  0F 8E 01 FA FF FF               jle 0x14021dbda
0021E1D9  41 8B D6                        mov edx, r14d
0021E1DC  89 55 9F                        mov dword ptr [rbp - 0x61], edx
0021E1DF  8B F2                           mov esi, edx
0021E1E1  E9 34 FA FF FF                  jmp 0x14021dc1a
0021E1E6  40 0F BE C6                     movsx eax, sil
0021E1EA  BA F0 0F 00 00                  mov edx, 0xff0
0021E1EF  66 C1 E0 04                     shl ax, 4
0021E1F3  66 33 C1                        xor ax, cx
0021E1F6  66 23 C2                        and ax, dx
0021E1F9  66 33 C1                        xor ax, cx
0021E1FC  66 41 89 84 24 06 02 00 00      mov word ptr [r12 + 0x206], ax
0021E205  E9 F6 FA FF FF                  jmp 0x14021dd00
0021E20A  4D 8B EF                        mov r13, r15
0021E20D  E9 18 F6 FF FF                  jmp 0x14021d82a
0021E212  48 8B CB                        mov rcx, rbx
0021E215  49 8B D5                        mov rdx, r13
0021E218  45 8B C7                        mov r8d, r15d
0021E21B  E8 E0 CF 0E 00                  call 0x14030b200
0021E220  84 C0                           test al, al
0021E222  0F 84 02 F6 FF FF               je 0x14021d82a
0021E228  E8 E3 80 13 00                  call 0x140356310
0021E22D  84 C0                           test al, al
0021E22F  0F 85 F5 F5 FF FF               jne 0x14021d82a
0021E235  49 8B CD                        mov rcx, r13
0021E238  E8 63 45 FE FF                  call 0x1402027a0
0021E23D  84 C0                           test al, al
0021E23F  0F 85 80 02 00 00               jne 0x14021e4c5
0021E245  44 03 42 7C                     add r8d, dword ptr [rdx + 0x7c]
0021E249  75 0C                           jne 0x14021e257
0021E24B  48 8B 92 A0 01 00 00            mov rdx, qword ptr [rdx + 0x1a0]
0021E252  48 85 D2                        test rdx, rdx
0021E255  75 EE                           jne 0x14021e245
0021E257  44 89 45 A7                     mov dword ptr [rbp - 0x59], r8d
0021E25B  45 85 C0                        test r8d, r8d
0021E25E  0F 84 C6 F5 FF FF               je 0x14021d82a
0021E264  E9 5F 02 00 00                  jmp 0x14021e4c8
0021E269  48 8D 55 C7                     lea rdx, [rbp - 0x39]
0021E26D  49 8B CF                        mov rcx, r15
0021E270  E8 0B FB 0E 00                  call 0x14030dd80
0021E275  E9 62 FD FF FF                  jmp 0x14021dfdc
0021E27A  49 8B 8B C8 03 00 00            mov rcx, qword ptr [r11 + 0x3c8]
0021E281  41 0F BE 93 C3 00 00 00         movsx edx, byte ptr [r11 + 0xc3]
0021E289  8B 01                           mov eax, dword ptr [rcx]
0021E28B  44 0F B6 C0                     movzx r8d, al
0021E28F  41 3B D0                        cmp edx, r8d
0021E292  0F 84 D1 F7 FF FF               je 0x14021da69
0021E298  8B C2                           mov eax, edx
0021E29A  41 2B C0                        sub eax, r8d
0021E29D  F0 01 01                        lock add dword ptr [rcx], eax
0021E2A0  E9 C4 F7 FF FF                  jmp 0x14021da69
0021E2A5  45 33 C0                        xor r8d, r8d
0021E2A8  49 8B CF                        mov rcx, r15
0021E2AB  E8 AC C4 3A 00                  call 0x1405ca75c
0021E2B0  E9 03 F9 FF FF                  jmp 0x14021dbb8
0021E2B5  49 8B 8C 24 C8 03 00 00         mov rcx, qword ptr [r12 + 0x3c8]
0021E2BD  41 0F BE 94 24 C3 00 00 00      movsx edx, byte ptr [r12 + 0xc3]
0021E2C6  8B 01                           mov eax, dword ptr [rcx]
0021E2C8  44 0F B6 C0                     movzx r8d, al
0021E2CC  41 3B D0                        cmp edx, r8d
0021E2CF  0F 84 76 FA FF FF               je 0x14021dd4b
0021E2D5  8B C2                           mov eax, edx
0021E2D7  41 2B C0                        sub eax, r8d
0021E2DA  F0 01 01                        lock add dword ptr [rcx], eax
0021E2DD  E9 69 FA FF FF                  jmp 0x14021dd4b
0021E2E2  41 80 BB C3 00 00 00 00         cmp byte ptr [r11 + 0xc3], 0
0021E2EA  0F 8E CE F6 FF FF               jle 0x14021d9be
0021E2F0  8B 5D 6F                        mov ebx, dword ptr [rbp + 0x6f]
0021E2F3  41 3A 9B 66 03 00 00            cmp bl, byte ptr [r11 + 0x366]
0021E2FA  0F 8E 19 F7 FF FF               jle 0x14021da19
0021E300  E8 BB 14 2D 00                  call 0x1404ef7c0
0021E305  48 8B 75 97                     mov rsi, qword ptr [rbp - 0x69]
0021E309  85 C0                           test eax, eax
0021E30B  0F BE DB                        movsx ebx, bl
0021E30E  0F BE 86 33 02 00 00            movsx eax, byte ptr [rsi + 0x233]
0021E315  0F 84 CF F6 FF FF               je 0x14021d9ea
0021E31B  0F B7 8E 06 02 00 00            movzx ecx, word ptr [rsi + 0x206]
0021E322  83 E1 0F                        and ecx, 0xf
0021E325  03 C8                           add ecx, eax
0021E327  B8 0F 00 00 00                  mov eax, 0xf
0021E32C  83 F9 10                        cmp ecx, 0x10
0021E32F  0F 4D C8                        cmovge ecx, eax
0021E332  03 D9                           add ebx, ecx
0021E334  83 FB 10                        cmp ebx, 0x10
0021E337  0F 4D D8                        cmovge ebx, eax
0021E33A  2B D9                           sub ebx, ecx
0021E33C  E9 B8 F6 FF FF                  jmp 0x14021d9f9
0021E341  41 8B D4                        mov edx, r12d
0021E344  89 55 9F                        mov dword ptr [rbp - 0x61], edx
0021E347  E9 8B F8 FF FF                  jmp 0x14021dbd7
0021E34C  8B 05 66 87 DA 00               mov eax, dword ptr [rip + 0xda8766]
0021E352  A8 40                           test al, 0x40
0021E354  0F 84 5D F5 FF FF               je 0x14021d8b7
0021E35A  E8 31 11 0F 00                  call 0x14030f490
0021E35F  84 C0                           test al, al
0021E361  0F 84 7E 07 00 00               je 0x14021eae5
0021E367  8B CB                           mov ecx, ebx
0021E369  E8 F2 10 0F 00                  call 0x14030f460
0021E36E  4C 8B 5D 97                     mov r11, qword ptr [rbp - 0x69]
0021E372  E9 42 F5 FF FF                  jmp 0x14021d8b9
0021E377  41 C6 84 24 35 02 00 00 01      mov byte ptr [r12 + 0x235], 1
0021E380  E9 32 FE FF FF                  jmp 0x14021e1b7
0021E385  41 0F 0D 08                     prefetchw byte ptr [r8]
0021E389  41 8B 00                        mov eax, dword ptr [r8]
0021E38C  8B D0                           mov edx, eax
0021E38E  0F BA F2 15                     btr edx, 0x15
0021E392  F0 41 0F B1 10                  lock cmpxchg dword ptr [r8], edx
0021E397  75 F3                           jne 0x14021e38c
0021E399  0F BA E0 15                     bt eax, 0x15
0021E39D  0F 83 E2 F4 FF FF               jae 0x14021d885
0021E3A3  E8 28 4E 04 00                  call 0x1402631d0
0021E3A8  E9 D8 F4 FF FF                  jmp 0x14021d885
0021E3AD  8B CF                           mov ecx, edi
0021E3AF  89 75 67                        mov dword ptr [rbp + 0x67], esi
0021E3B2  C1 E9 03                        shr ecx, 3
0021E3B5  8B C7                           mov eax, edi
0021E3B7  66 83 E1 01                     and cx, 1
0021E3BB  C1 E8 02                        shr eax, 2
0021E3BE  66 03 C9                        add cx, cx
0021E3C1  66 83 E0 01                     and ax, 1
0021E3C5  66 0B C8                        or cx, ax
0021E3C8  66 83 E7 01                     and di, 1
0021E3CC  8B 45 9F                        mov eax, dword ptr [rbp - 0x61]
0021E3CF  66 03 C9                        add cx, cx
0021E3D2  66 0B CF                        or cx, di
0021E3D5  88 45 69                        mov byte ptr [rbp + 0x69], al
0021E3D8  66 03 C9                        add cx, cx
0021E3DB  48 8D 45 67                     lea rax, [rbp + 0x67]
0021E3DF  0F 57 C0                        xorps xmm0, xmm0
0021E3E2  66 89 4D 67                     mov word ptr [rbp + 0x67], cx
0021E3E6  0F 11 45 F7                     movups xmmword ptr [rbp - 9], xmm0
0021E3EA  49 8B CC                        mov rcx, r12
0021E3ED  C6 45 03 01                     mov byte ptr [rbp + 3], 1
0021E3F1  48 89 45 F7                     mov qword ptr [rbp - 9], rax
0021E3F5  C7 45 FF 04 00 00 00            mov dword ptr [rbp - 1], 4
0021E3FC  E8 2F D1 1F 00                  call 0x14041b530
0021E401  4C 8D 45 F7                     lea r8, [rbp - 9]
0021E405  49 8B D4                        mov rdx, r12
0021E408  49 8B CF                        mov rcx, r15
0021E40B  84 C0                           test al, al
0021E40D  0F 84 0B 05 00 00               je 0x14021e91e
0021E413  E8 28 A2 17 00                  call 0x140398640
0021E418  E9 9C FC FF FF                  jmp 0x14021e0b9
0021E41D  8B 05 91 89 DA 00               mov eax, dword ptr [rip + 0xda8991]
0021E423  4D 8B DA                        mov r11, r10
0021E426  48 03 C8                        add rcx, rax
0021E429  4C 2B D8                        sub r11, rax
0021E42C  E9 7C FD FF FF                  jmp 0x14021e1ad
0021E431  41 8B 43 74                     mov eax, dword ptr [r11 + 0x74]
0021E435  A8 08                           test al, 8
0021E437  0F 85 50 F6 FF FF               jne 0x14021da8d
0021E43D  41 8B 9B 4C 02 00 00            mov ebx, dword ptr [r11 + 0x24c]
0021E444  49 8B CB                        mov rcx, r11
0021E447  89 5D BB                        mov dword ptr [rbp - 0x45], ebx
0021E44A  E8 91 B9 17 00                  call 0x140399de0
0021E44F  4C 8B 5D 97                     mov r11, qword ptr [rbp - 0x69]
0021E453  85 C0                           test eax, eax
0021E455  0F 84 32 F6 FF FF               je 0x14021da8d
0021E45B  F7 05 9F 86 DA 00 00 10 00 00   test dword ptr [rip + 0xda869f], 0x1000
0021E465  41 8B 8B 4C 02 00 00            mov ecx, dword ptr [r11 + 0x24c]
0021E46C  89 4D B7                        mov dword ptr [rbp - 0x49], ecx
0021E46F  74 04                           je 0x14021e475
0021E471  0F BA EF 09                     bts edi, 9
0021E475  F7 05 91 86 DA 00 00 00 00 08   test dword ptr [rip + 0xda8691], 0x8000000
0021E47F  0F 85 DD 04 00 00               jne 0x14021e962
0021E485  0F BA E7 09                     bt edi, 9
0021E489  72 0A                           jb 0x14021e495
0021E48B  0F BA E7 0A                     bt edi, 0xa
0021E48F  0F 83 F8 F5 FF FF               jae 0x14021da8d
0021E495  66 F0 41 FF 83 64 03 00 00      lock inc word ptr [r11 + 0x364]
0021E49E  E9 EA F5 FF FF                  jmp 0x14021da8d
0021E4A3  48 8D 55 C7                     lea rdx, [rbp - 0x39]
0021E4A7  49 8B CD                        mov rcx, r13
0021E4AA  E8 71 A1 03 00                  call 0x140258620
0021E4AF  E9 22 FA FF FF                  jmp 0x14021ded6
0021E4B4  45 84 FF                        test r15b, r15b
0021E4B7  0F 85 FD 03 00 00               jne 0x14021e8ba
0021E4BD  40 B7 01                        mov dil, 1
0021E4C0  E9 54 F5 FF FF                  jmp 0x14021da19
0021E4C5  89 7D A7                        mov dword ptr [rbp - 0x59], edi
0021E4C8  49 8B 46 68                     mov rax, qword ptr [r14 + 0x68]
0021E4CC  48 85 C0                        test rax, rax
0021E4CF  0F 84 55 F3 FF FF               je 0x14021d82a
0021E4D5  44 8B 96 D8 00 00 00            mov r10d, dword ptr [rsi + 0xd8]
0021E4DC  49 8B CE                        mov rcx, r14
0021E4DF  4C 03 D0                        add r10, rax
0021E4E2  45 8B C7                        mov r8d, r15d
0021E4E5  49 8B D2                        mov rdx, r10
0021E4E8  E8 13 CD 0E 00                  call 0x14030b200
0021E4ED  84 C0                           test al, al
0021E4EF  0F 84 C4 04 00 00               je 0x14021e9b9
0021E4F5  E8 16 7E 13 00                  call 0x140356310
0021E4FA  84 C0                           test al, al
0021E4FC  0F 85 AF 03 00 00               jne 0x14021e8b1
0021E502  49 8B CA                        mov rcx, r10
0021E505  E8 96 42 FE FF                  call 0x1402027a0
0021E50A  84 C0                           test al, al
0021E50C  0F 85 CB 04 00 00               jne 0x14021e9dd
0021E512  44 03 42 7C                     add r8d, dword ptr [rdx + 0x7c]
0021E516  75 0C                           jne 0x14021e524
0021E518  48 8B 92 A0 01 00 00            mov rdx, qword ptr [rdx + 0x1a0]
0021E51F  48 85 D2                        test rdx, rdx
0021E522  75 EE                           jne 0x14021e512
0021E524  44 89 45 A3                     mov dword ptr [rbp - 0x5d], r8d
0021E528  45 85 C0                        test r8d, r8d
0021E52B  0F 84 F9 F2 FF FF               je 0x14021d82a
0021E531  4C 8D 4D A3                     lea r9, [rbp - 0x5d]
0021E535  49 8B D2                        mov rdx, r10
0021E538  4C 8D 45 A7                     lea r8, [rbp - 0x59]
0021E53C  49 8B CD                        mov rcx, r13
0021E53F  E8 80 90 27 00                  call 0x1404975c4
0021E544  E9 E1 F2 FF FF                  jmp 0x14021d82a
0021E549  B3 05                           mov bl, 5
0021E54B  E9 1D F4 FF FF                  jmp 0x14021d96d
0021E550  41 83 FE 10                     cmp r14d, 0x10
0021E554  0F 8D 76 FC FF FF               jge 0x14021e1d0
0021E55A  B8 0F 00 00 00                  mov eax, 0xf
0021E55F  8B D0                           mov edx, eax
0021E561  89 45 9F                        mov dword ptr [rbp - 0x61], eax
0021E564  E9 6E F6 FF FF                  jmp 0x14021dbd7
0021E569  49 8B 83 C8 03 00 00            mov rax, qword ptr [r11 + 0x3c8]
0021E570  F0 81 08 00 00 10 00            lock or dword ptr [rax], 0x100000
0021E577  48 8D 55 D7                     lea rdx, [rbp - 0x29]
0021E57B  49 8B CB                        mov rcx, r11
0021E57E  E8 61 66 0E 00                  call 0x140304be4
0021E583  4C 8B 7D 97                     mov r15, qword ptr [rbp - 0x69]
0021E587  4C 63 F0                        movsxd r14, eax
0021E58A  4D 63 8F 00 04 00 00            movsxd r9, dword ptr [r15 + 0x400]
0021E591  45 3B F1                        cmp r14d, r9d
0021E594  0F 85 54 05 00 00               jne 0x14021eaee
0021E59A  41 0F BE BF C3 00 00 00         movsx edi, byte ptr [r15 + 0xc3]
0021E5A2  B8 0F F0 00 00                  mov eax, 0xf00f
0021E5A7  66 41 21 87 06 02 00 00         and word ptr [r15 + 0x206], ax
0021E5AF  45 33 C0                        xor r8d, r8d
0021E5B2  33 D2                           xor edx, edx
0021E5B4  41 C6 87 66 03 00 00 00         mov byte ptr [r15 + 0x366], 0
0021E5BC  49 8B CF                        mov rcx, r15
0021E5BF  E8 30 60 1A 00                  call 0x1403c45f4
0021E5C4  8B D8                           mov ebx, eax
0021E5C6  3B C7                           cmp eax, edi
0021E5C8  0F 85 59 05 00 00               jne 0x14021eb27
0021E5CE  41 0F B6 8F 62 04 00 00         movzx ecx, byte ptr [r15 + 0x462]
0021E5D6  4D 8B DF                        mov r11, r15
0021E5D9  85 C9                           test ecx, ecx
0021E5DB  0F 85 9C 02 00 00               jne 0x14021e87d
0021E5E1  41 0F B6 87 04 02 00 00         movzx eax, byte ptr [r15 + 0x204]
0021E5E9  3B C8                           cmp ecx, eax
0021E5EB  0F 85 6F 05 00 00               jne 0x14021eb60
0021E5F1  41 F7 47 78 00 00 40 00         test dword ptr [r15 + 0x78], 0x400000
0021E5F9  74 0E                           je 0x14021e609
0021E5FB  49 8B 87 C8 03 00 00            mov rax, qword ptr [r15 + 0x3c8]
0021E602  F0 81 20 FF FF EF FF            lock and dword ptr [rax], 0xffefffff
0021E609  3B FB                           cmp edi, ebx
0021E60B  0F 85 22 03 00 00               jne 0x14021e933
0021E611  41 B7 01                        mov r15b, 1
0021E614  E9 BD F2 FF FF                  jmp 0x14021d8d6
0021E619  8B C7                           mov eax, edi
0021E61B  89 5D AB                        mov dword ptr [rbp - 0x55], ebx
0021E61E  C1 E8 02                        shr eax, 2
0021E621  8B CF                           mov ecx, edi
0021E623  C1 E9 03                        shr ecx, 3
0021E626  66 83 E0 01                     and ax, 1
0021E62A  66 83 E1 01                     and cx, 1
0021E62E  0F 57 C0                        xorps xmm0, xmm0
0021E631  66 03 C9                        add cx, cx
0021E634  45 33 F6                        xor r14d, r14d
0021E637  66 0B C8                        or cx, ax
0021E63A  0F B7 C7                        movzx eax, di
0021E63D  66 83 E0 01                     and ax, 1
0021E641  66 03 C9                        add cx, cx
0021E644  66 0B C8                        or cx, ax
0021E647  8B 45 9F                        mov eax, dword ptr [rbp - 0x61]
0021E64A  0F 11 45 07                     movups xmmword ptr [rbp + 7], xmm0
0021E64E  66 03 C9                        add cx, cx
0021E651  88 45 AD                        mov byte ptr [rbp - 0x53], al
0021E654  66 83 C9 01                     or cx, 1
0021E658  C6 45 13 01                     mov byte ptr [rbp + 0x13], 1
0021E65C  48 8D 45 AB                     lea rax, [rbp - 0x55]
0021E660  66 89 4D AB                     mov word ptr [rbp - 0x55], cx
0021E664  48 89 45 07                     mov qword ptr [rbp + 7], rax
0021E668  C7 45 0F 04 00 00 00            mov dword ptr [rbp + 0xf], 4
0021E66F  41 38 5D 00                     cmp byte ptr [r13], bl
0021E673  0F 86 99 00 00 00               jbe 0x14021e712
0021E679  48 8B 7D 97                     mov rdi, qword ptr [rbp - 0x69]
0021E67D  0F 1F 00                        nop dword ptr [rax]
0021E680  4B 8D 0C B6                     lea rcx, [r14 + r14*4]
0021E684  48 8D 1C CD 00 00 00 00         lea rbx, [rcx*8]
0021E68C  49 03 DD                        add rbx, r13
0021E68F  0F B6 43 33                     movzx eax, byte ptr [rbx + 0x33]
0021E693  48 8B 73 10                     mov rsi, qword ptr [rbx + 0x10]
0021E697  A8 10                           test al, 0x10
0021E699  75 0B                           jne 0x14021e6a6
0021E69B  A8 08                           test al, 8
0021E69D  74 25                           je 0x14021e6c4
0021E69F  90                              nop
0021E6A0  80 7E 07 00                     cmp byte ptr [rsi + 7], 0
0021E6A4  74 1E                           je 0x14021e6c4
0021E6A6  41 0F B6 87 D9 35 00 00         movzx eax, byte ptr [r15 + 0x35d9]
0021E6AE  84 C0                           test al, al
0021E6B0  75 71                           jne 0x14021e723
0021E6B2  41 C6 87 D9 35 00 00 01         mov byte ptr [r15 + 0x35d9], 1
0021E6BA  8B 46 24                        mov eax, dword ptr [rsi + 0x24]
0021E6BD  41 89 87 DC 35 00 00            mov dword ptr [r15 + 0x35dc], eax
0021E6C4  44 84 63 33                     test byte ptr [rbx + 0x33], r12b
0021E6C8  0F 85 4E 01 00 00               jne 0x14021e81c
0021E6CE  F6 43 33 04                     test byte ptr [rbx + 0x33], 4
0021E6D2  74 14                           je 0x14021e6e8
0021E6D4  48 8B 86 B8 8E 00 00            mov rax, qword ptr [rsi + 0x8eb8]
0021E6DB  0F BE 4B 34                     movsx ecx, byte ptr [rbx + 0x34]
0021E6DF  48 85 C0                        test rax, rax
0021E6E2  0F 85 89 00 00 00               jne 0x14021e771
0021E6E8  F6 43 33 01                     test byte ptr [rbx + 0x33], 1
0021E6EC  74 0C                           je 0x14021e6fa
0021E6EE  48 8B 43 28                     mov rax, qword ptr [rbx + 0x28]
0021E6F2  66 F0 FF 88 64 03 00 00         lock dec word ptr [rax + 0x364]
0021E6FA  41 0F B6 45 00                  movzx eax, byte ptr [r13]
0021E6FF  41 FF C6                        inc r14d
0021E702  44 3B F0                        cmp r14d, eax
0021E705  0F 82 75 FF FF FF               jb 0x14021e680
0021E70B  48 8B 5D AF                     mov rbx, qword ptr [rbp - 0x51]
0021E70F  8B 7D 7F                        mov edi, dword ptr [rbp + 0x7f]
0021E712  49 8D 8F D8 35 00 00            lea rcx, [r15 + 0x35d8]
0021E719  E8 E2 3A 03 00                  call 0x140252200
0021E71E  E9 AE F8 FF FF                  jmp 0x14021dfd1
0021E723  3C 01                           cmp al, 1
0021E725  75 41                           jne 0x14021e768
0021E727  41 8B 97 DC 35 00 00            mov edx, dword ptr [r15 + 0x35dc]
0021E72E  3B 56 24                        cmp edx, dword ptr [rsi + 0x24]
0021E731  74 91                           je 0x14021e6c4
0021E733  45 88 A7 D9 35 00 00            mov byte ptr [r15 + 0x35d9], r12b
0021E73A  49 81 C7 E0 35 00 00            add r15, 0x35e0
0021E741  49 8B CF                        mov rcx, r15
0021E744  E8 A7 CF 03 00                  call 0x14025b6f0
0021E749  4C 8B 86 C8 00 00 00            mov r8, qword ptr [rsi + 0xc8]
0021E750  49 8B CF                        mov rcx, r15
0021E753  0F B6 96 D0 00 00 00            movzx edx, byte ptr [rsi + 0xd0]
0021E75A  E8 61 CF 03 00                  call 0x14025b6c0
0021E75F  4C 8B 7D 67                     mov r15, qword ptr [rbp + 0x67]
0021E763  E9 5C FF FF FF                  jmp 0x14021e6c4
0021E768  49 81 C7 E0 35 00 00            add r15, 0x35e0
0021E76F  EB D8                           jmp 0x14021e749
0021E771  49 8D 97 B8 8E 00 00            lea rdx, [r15 + 0x8eb8]
0021E778  48 83 3A 00                     cmp qword ptr [rdx], 0
0021E77C  0F 84 66 FF FF FF               je 0x14021e6e8
0021E782  4C 3B FE                        cmp r15, rsi
0021E785  0F 84 5D FF FF FF               je 0x14021e6e8
0021E78B  44 8B 00                        mov r8d, dword ptr [rax]
0021E78E  4C 8B CA                        mov r9, rdx
0021E791  41 8B C0                        mov eax, r8d
0021E794  25 00 00 04 00                  and eax, 0x40000
0021E799  75 70                           jne 0x14021e80b
0021E79B  41 0F BA E0 14                  bt r8d, 0x14
0021E7A0  72 17                           jb 0x14021e7b9
0021E7A2  85 C0                           test eax, eax
0021E7A4  0F 84 3E FF FF FF               je 0x14021e6e8
0021E7AA  41 0F B6 C0                     movzx eax, r8b
0021E7AE  49 8B D1                        mov rdx, r9
0021E7B1  3B C1                           cmp eax, ecx
0021E7B3  0F 8D 2F FF FF FF               jge 0x14021e6e8
0021E7B9  80 3D 47 68 DA 00 00            cmp byte ptr [rip + 0xda6847], 0
0021E7C0  48 8B 0A                        mov rcx, qword ptr [rdx]
0021E7C3  44 89 61 0C                     mov dword ptr [rcx + 0xc], r12d
0021E7C7  44 8B 7E 24                     mov r15d, dword ptr [rsi + 0x24]
0021E7CB  75 1B                           jne 0x14021e7e8
0021E7CD  41 8B C7                        mov eax, r15d
0021E7D0  48 8D 15 89 EA DA 00            lea rdx, [rip + 0xdaea89]
0021E7D7  46 0F B6 3C 7A                  movzx r15d, byte ptr [rdx + r15*2]
0021E7DC  41 C1 E7 06                     shl r15d, 6
0021E7E0  0F B6 44 42 01                  movzx eax, byte ptr [rdx + rax*2 + 1]
0021E7E5  44 0B F8                        or r15d, eax
0021E7E8  44 89 79 08                     mov dword ptr [rcx + 8], r15d
0021E7EC  8B 05 22 83 DA 00               mov eax, dword ptr [rip + 0xda8322]
0021E7F2  A8 20                           test al, 0x20
0021E7F4  0F 84 D5 81 4B 00               je 0x1406d69cf
0021E7FA  8B 4E 24                        mov ecx, dword ptr [rsi + 0x24]
0021E7FD  41 8B D4                        mov edx, r12d
0021E800  E8 BB CA 2D 00                  call 0x1404fb2c0
0021E805  90                              nop
0021E806  E9 C4 81 4B 00                  jmp 0x1406d69cf
0021E80B  4D 8D 8F B8 8E 00 00            lea r9, [r15 + 0x8eb8]
0021E812  EB 87                           jmp 0x14021e79b
0021E814  83 E7 FD                        and edi, 0xfffffffd
0021E817  E9 88 F4 FF FF                  jmp 0x14021dca4
0021E81C  48 8B 4B 28                     mov rcx, qword ptr [rbx + 0x28]
0021E820  48 8B D6                        mov rdx, rsi
0021E823  48 3B CF                        cmp rcx, rdi
0021E826  75 50                           jne 0x14021e878
0021E828  4C 8D 45 07                     lea r8, [rbp + 7]
0021E82C  E8 1B CF 0E 00                  call 0x14030b74c
0021E831  E9 98 FE FF FF                  jmp 0x14021e6ce
0021E836  0F B6 43 20                     movzx eax, byte ptr [rbx + 0x20]
0021E83A  48 8B 53 10                     mov rdx, qword ptr [rbx + 0x10]
0021E83E  A8 01                           test al, 1
0021E840  0F 85 16 F6 FF FF               jne 0x14021de5c
0021E846  41 0F B6 8C 24 C3 00 00 00      movzx ecx, byte ptr [r12 + 0xc3]
0021E84F  3A 8A C3 00 00 00               cmp cl, byte ptr [rdx + 0xc3]
0021E855  0F 8F 01 F6 FF FF               jg 0x14021de5c
0021E85B  75 08                           jne 0x14021e865
0021E85D  A8 18                           test al, 0x18
0021E85F  0F 85 F7 F5 FF FF               jne 0x14021de5c
0021E865  A8 10                           test al, 0x10
0021E867  74 08                           je 0x14021e871
0021E869  84 C9                           test cl, cl
0021E86B  0F 85 EB F5 FF FF               jne 0x14021de5c
0021E871  32 C0                           xor al, al
0021E873  E9 07 F6 FF FF                  jmp 0x14021de7f
0021E878  45 33 C0                        xor r8d, r8d
0021E87B  EB AF                           jmp 0x14021e82c
0021E87D  49 8B 97 C8 03 00 00            mov rdx, qword ptr [r15 + 0x3c8]
0021E884  48 85 D2                        test rdx, rdx
0021E887  0F 84 54 FD FF FF               je 0x14021e5e1
0021E88D  8B 42 1C                        mov eax, dword ptr [rdx + 0x1c]
0021E890  44 8B 4A 20                     mov r9d, dword ptr [rdx + 0x20]
0021E894  44 8B 52 14                     mov r10d, dword ptr [rdx + 0x14]
0021E898  44 8B 02                        mov r8d, dword ptr [rdx]
0021E89B  41 81 E0 00 00 20 00            and r8d, 0x200000
0021E8A2  85 C0                           test eax, eax
0021E8A4  0F 84 94 02 00 00               je 0x14021eb3e
0021E8AA  33 C9                           xor ecx, ecx
0021E8AC  E9 30 FD FF FF                  jmp 0x14021e5e1
0021E8B1  44 89 7D A3                     mov dword ptr [rbp - 0x5d], r15d
0021E8B5  E9 70 EF FF FF                  jmp 0x14021d82a
0021E8BA  41 0F B7 83 06 02 00 00         movzx eax, word ptr [r11 + 0x206]
0021E8C2  66 41 23 C0                     and ax, r8w
0021E8C6  66 3B C1                        cmp ax, cx
0021E8C9  48 8B 45 BF                     mov rax, qword ptr [rbp - 0x41]
0021E8CD  40 0F 92 C7                     setb dil
0021E8D1  49 3B 43 20                     cmp rax, qword ptr [r11 + 0x20]
0021E8D5  0F 82 3E F1 FF FF               jb 0x14021da19
0021E8DB  40 B7 01                        mov dil, 1
0021E8DE  49 8B CB                        mov rcx, r11
0021E8E1  44 0F B6 C7                     movzx r8d, dil
0021E8E5  E8 A2 44 1A 00                  call 0x1403c2d8c
0021E8EA  4C 8B 5D 97                     mov r11, qword ptr [rbp - 0x69]
0021E8EE  E9 26 F1 FF FF                  jmp 0x14021da19
0021E8F3  41 F7 47 78 00 00 40 00         test dword ptr [r15 + 0x78], 0x400000
0021E8FB  0F 85 98 F2 FF FF               jne 0x14021db99
0021E901  8B D1                           mov edx, ecx
0021E903  E9 B2 F2 FF FF                  jmp 0x14021dbba
0021E908  48 83 F9 01                     cmp rcx, 1
0021E90C  0F 84 4A F3 FF FF               je 0x14021dc5c
0021E912  48 83 C8 01                     or rax, 1
0021E916  48 33 C1                        xor rax, rcx
0021E919  E9 0D F8 FF FF                  jmp 0x14021e12b
0021E91E  E8 F5 99 17 00                  call 0x140398318
0021E923  E9 91 F7 FF FF                  jmp 0x14021e0b9
0021E928  0F 86 2B F3 FF FF               jbe 0x14021dc59
0021E92E  E9 29 F3 FF FF                  jmp 0x14021dc5c
0021E933  8B 05 DB 81 DA 00               mov eax, dword ptr [rip + 0xda81db]
0021E939  A8 20                           test al, 0x20
0021E93B  0F 84 D0 FC FF FF               je 0x14021e611
0021E941  48 8D 45 D7                     lea rax, [rbp - 0x29]
0021E945  44 8B CB                        mov r9d, ebx
0021E948  45 8B C6                        mov r8d, r14d
0021E94B  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0021E950  8B D7                           mov edx, edi
0021E952  49 8B CF                        mov rcx, r15
0021E955  E8 FE 39 2B 00                  call 0x1404d2358
0021E95A  4D 8B DF                        mov r11, r15
0021E95D  E9 AF FC FF FF                  jmp 0x14021e611
0021E962  3B D9                           cmp ebx, ecx
0021E964  0F 84 1B FB FF FF               je 0x14021e485
0021E96A  0F BA EF 0A                     bts edi, 0xa
0021E96E  E9 12 FB FF FF                  jmp 0x14021e485
0021E973  8B FE                           mov edi, esi
0021E975  41 0F B6 45 00                  movzx eax, byte ptr [r13]
0021E97A  3B F8                           cmp edi, eax
0021E97C  0F 83 FB F4 FF FF               jae 0x14021de7d
0021E982  8B C7                           mov eax, edi
0021E984  48 8D 0C 85 02 00 00 00         lea rcx, [rax*4 + 2]
0021E98C  48 03 C8                        add rcx, rax
0021E98F  48 8D 0C CD 00 00 00 00         lea rcx, [rcx*8]
0021E997  49 03 CD                        add rcx, r13
0021E99A  48 3B CB                        cmp rcx, rbx
0021E99D  74 16                           je 0x14021e9b5
0021E99F  45 33 C9                        xor r9d, r9d
0021E9A2  45 33 C0                        xor r8d, r8d
0021E9A5  49 8B D4                        mov rdx, r12
0021E9A8  E8 23 98 03 00                  call 0x1402581d0
0021E9AD  84 C0                           test al, al
0021E9AF  0F 84 CA F4 FF FF               je 0x14021de7f
0021E9B5  FF C7                           inc edi
0021E9B7  EB BC                           jmp 0x14021e975
0021E9B9  44 89 7D A3                     mov dword ptr [rbp - 0x5d], r15d
0021E9BD  E9 68 EE FF FF                  jmp 0x14021d82a
0021E9C2  44 8B D6                        mov r10d, esi
0021E9C5  41 38 75 00                     cmp byte ptr [r13], sil
0021E9C9  77 25                           ja 0x14021e9f0
0021E9CB  F6 C2 02                        test dl, 2
0021E9CE  0F 84 27 F4 FF FF               je 0x14021ddfb
0021E9D4  41 89 75 04                     mov dword ptr [r13 + 4], esi
0021E9D8  E9 1E F4 FF FF                  jmp 0x14021ddfb
0021E9DD  89 7D A3                        mov dword ptr [rbp - 0x5d], edi
0021E9E0  E9 4C FB FF FF                  jmp 0x14021e531
0021E9E5  66 66 66 0F 1F 84 00 00 00 00 00  nop word ptr [rax + rax]
0021E9F0  41 8B C2                        mov eax, r10d
0021E9F3  4D 8D 4D 10                     lea r9, [r13 + 0x10]
0021E9F7  48 8D 0C 80                     lea rcx, [rax + rax*4]
0021E9FB  4D 8D 0C C9                     lea r9, [r9 + rcx*8]
0021E9FF  4D 3B C8                        cmp r9, r8
0021EA02  74 2A                           je 0x14021ea2e
0021EA04  41 80 49 22 02                  or byte ptr [r9 + 0x22], 2
0021EA09  49 8B 09                        mov rcx, qword ptr [r9]
0021EA0C  48 8B 41 18                     mov rax, qword ptr [rcx + 0x18]
0021EA10  49 89 41 10                     mov qword ptr [r9 + 0x10], rax
0021EA14  41 0F B6 41 20                  movzx eax, byte ptr [r9 + 0x20]
0021EA19  24 C5                           and al, 0xc5
0021EA1B  0C 05                           or al, 5
0021EA1D  41 88 41 20                     mov byte ptr [r9 + 0x20], al
0021EA21  48 8B 41 18                     mov rax, qword ptr [rcx + 0x18]
0021EA25  41 80 61 21 FE                  and byte ptr [r9 + 0x21], 0xfe
0021EA2A  49 89 41 18                     mov qword ptr [r9 + 0x18], rax
0021EA2E  41 0F B6 45 00                  movzx eax, byte ptr [r13]
0021EA33  41 FF C2                        inc r10d
0021EA36  44 3B D0                        cmp r10d, eax
0021EA39  72 B5                           jb 0x14021e9f0
0021EA3B  EB 8E                           jmp 0x14021e9cb
0021EA3D  4D 8D 83 28 03 00 00            lea r8, [r11 + 0x328]
0021EA44  49 83 38 01                     cmp qword ptr [r8], 1
0021EA48  0F 85 E7 EF FF FF               jne 0x14021da35
0021EA4E  48 8D 91 78 91 00 00            lea rdx, [rcx + 0x9178]
0021EA55  48 85 D2                        test rdx, rdx
0021EA58  0F 84 D7 EF FF FF               je 0x14021da35
0021EA5E  48 8B 02                        mov rax, qword ptr [rdx]
0021EA61  49 89 00                        mov qword ptr [r8], rax
0021EA64  4C 89 02                        mov qword ptr [rdx], r8
0021EA67  66 F0 41 FF 83 64 03 00 00      lock inc word ptr [r11 + 0x364]
0021EA70  E8 5B 8A FE FF                  call 0x1402074d0
0021EA75  4C 8B 5D 97                     mov r11, qword ptr [rbp - 0x69]
0021EA79  E9 B7 EF FF FF                  jmp 0x14021da35
0021EA7E  4D 8D 84 24 28 03 00 00         lea r8, [r12 + 0x328]
0021EA86  49 83 38 01                     cmp qword ptr [r8], 1
0021EA8A  0F 85 87 F2 FF FF               jne 0x14021dd17
0021EA90  48 8D 91 78 91 00 00            lea rdx, [rcx + 0x9178]
0021EA97  48 85 D2                        test rdx, rdx
0021EA9A  0F 84 77 F2 FF FF               je 0x14021dd17
0021EAA0  48 8B 02                        mov rax, qword ptr [rdx]
0021EAA3  49 89 00                        mov qword ptr [r8], rax
0021EAA6  4C 89 02                        mov qword ptr [rdx], r8
0021EAA9  66 F0 41 FF 84 24 64 03 00 00   lock inc word ptr [r12 + 0x364]
0021EAB3  E8 18 8A FE FF                  call 0x1402074d0
0021EAB8  E9 5A F2 FF FF                  jmp 0x14021dd17
0021EABD  41 0F B6 83 18 03 00 00         movzx eax, byte ptr [r11 + 0x318]
0021EAC5  84 C0                           test al, al
0021EAC7  0F 84 68 EF FF FF               je 0x14021da35
0021EACD  E9 6B FF FF FF                  jmp 0x14021ea3d
0021EAD2  41 0F B6 84 24 18 03 00 00      movzx eax, byte ptr [r12 + 0x318]
0021EADB  84 C0                           test al, al
0021EADD  0F 84 34 F2 FF FF               je 0x14021dd17
0021EAE3  EB 99                           jmp 0x14021ea7e
0021EAE5  4C 8B 5D 97                     mov r11, qword ptr [rbp - 0x69]
0021EAE9  E9 C9 ED FF FF                  jmp 0x14021d8b7
0021EAEE  4D 0F BE D6                     movsx r10, r14b
0021EAF2  4D 8B C2                        mov r8, r10
0021EAF5  4F 8D 1C 3A                     lea r11, [r10 + r15]
0021EAF9  41 0F B6 8B 38 03 00 00         movzx ecx, byte ptr [r11 + 0x338]
0021EB01  80 F9 FF                        cmp cl, 0xff
0021EB04  0F 85 4A 7E 4B 00               jne 0x1406d6954
0021EB0A  41 B9 01 00 00 00               mov r9d, 1
0021EB10  48 C7 44 24 20 00 00 00 00      mov qword ptr [rsp + 0x20], 0
0021EB19  49 8B D7                        mov rdx, r15
0021EB1C  B9 57 01 00 00                  mov ecx, 0x157
0021EB21  E8 3A EB 2D 00                  call 0x1404fd660
0021EB26  CC                              int3
0021EB27  44 8B CB                        mov r9d, ebx
0021EB2A  C6 44 24 20 00                  mov byte ptr [rsp + 0x20], 0
0021EB2F  4D 8B C7                        mov r8, r15
0021EB32  33 C9                           xor ecx, ecx
0021EB34  E8 D7 8C 03 00                  call 0x140257810
0021EB39  E9 90 FA FF FF                  jmp 0x14021e5ce
0021EB3E  45 85 C9                        test r9d, r9d
0021EB41  0F 85 63 FD FF FF               jne 0x14021e8aa
0021EB47  41 0F BA E2 0E                  bt r10d, 0xe
0021EB4C  0F 82 58 FD FF FF               jb 0x14021e8aa
0021EB52  45 85 C0                        test r8d, r8d
0021EB55  0F 84 86 FA FF FF               je 0x14021e5e1
0021EB5B  E9 4A FD FF FF                  jmp 0x14021e8aa
0021EB60  41 88 8F 04 02 00 00            mov byte ptr [r15 + 0x204], cl
0021EB67  E9 85 FA FF FF                  jmp 0x14021e5f1
0021EB6C  49 8B CB                        mov rcx, r11
0021EB6F  E8 FC 7A 3A 00                  call 0x1405c6670
0021EB74  4C 8B 5D 97                     mov r11, qword ptr [rbp - 0x69]
0021EB78  E9 F6 EE FF FF                  jmp 0x14021da73
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0021D7F8(__int64 a1, __int64 a2, int a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, __int64 a12, __int64 a13, __int64 a14, __int64 a15, __int64 a16, __int64 a17, __int64 a18, __int64 a19, __int64 a20, __int64 a21, __int64 a22, __int64 a23, __int64 a24, __int64 a25, __int64 a26, __int64 a27, __int64 a28, __int64 a29, __int64 a30, __int64 a31, __int64 a32, __int64 a33, __int64 a34)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p110;
    unsigned __int64 v_stack_p118;
    unsigned __int64 v_stack_p20;
    unsigned __int16 v_stack_p28;

    v_stack_p110 = v_r13;
    *(unsigned __int64 *)(v_rbp - 17) = v_r14;
    result = KiAbProcessPreContextSwitch(a1, a2, a3, a4);
    *(unsigned int *)(v_rbp - 89) = (unsigned int)(v_r15);
    if (*(unsigned __int64 *)(v_rbx + 104) == 0) goto loc_0021E20A;
    v_r13 = ((unsigned int)(*(unsigned int *)(v_rsi + 216))) + (*(unsigned __int64 *)(v_rbx + 104));
    if (condition_is_not_equal) goto loc_0021E212;
loc_0021D82A:
    v_rdi = (*(unsigned __int8 *)(v_rbx + 587) + *(unsigned __int8 *)(v_rbx + 587) * 2) << (4);
    v_rdi = (v_rdi) + (*(unsigned __int64 *)(v_rbx + 208));
loc_0021D843:
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rbx + 208) + 17))) < 5) goto loc_0021D92F;
loc_0021D84F:
    v_rbx = (*(unsigned __int64 *)(v_rbx + 208)) + (48);
    if (v_rbx != v_rdi) goto loc_0021D843;
    a3 = 0;
    result = KiUpdateTotalCyclesCurrentThread(*(unsigned __int64 *)(v_rbp + 103), v_r14, a3, a4);
    *(unsigned __int64 *)(v_rbp - 25) = result;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536) != 0) goto loc_0021E385;
loc_0021D885:
    *(unsigned __int64 *)(v_rbp - 33) = *(unsigned __int64 *)(v_r14 + 32);
    *(unsigned __int64 *)(v_rbp - 65) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 105) + 72);
loc_0021D8A0:
    if (condition_is_above_or_equal) goto loc_0021D8C4;
loc_0021D8A9:
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)(v_r15))) + 1);
    if (((*(unsigned int *)(v_rip + 14318075)) & ((unsigned int)(v_rbx))) == 0) goto loc_0021E34C;
loc_0021D8B7:
loc_0021D8B9:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 105) + 64) == 0) goto loc_0021D8A0;
    goto loc_0021D8A9;
loc_0021D8C4:
    *(unsigned __int64 *)(v_rbp - 41) = v_r15;
    if (((*(unsigned int *)(*(unsigned __int64 *)(v_rbp - 105) + 120)) & (0x400000ULL)) != 0) goto loc_0021E569;
loc_0021D8D6:
    v_rdi = 0;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp - 105) + 195)) >= 16) goto loc_0021E4B4;
    v_rbx = 0;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(256))) - (*(unsigned int *)(*(unsigned __int64 *)(v_rbp - 105) + 436)));
    if ((*(unsigned __int64 *)(v_rbp - 65)) >= (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 105) + 32))) goto loc_0021D962;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp - 105) + 563)) >= 14) goto loc_0021D96D;
    if (((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rbp - 105) + 518)) & ((unsigned __int16)((unsigned int)(0xFF0ULL)))) != 0) goto loc_0021D98E;
    if (((unsigned int)(a1)) < 2) goto loc_0021D98E;
    goto loc_0021D96D;
loc_0021D92F:
    result = KiAcquireKobjectLockSafe(*(unsigned __int64 *)(v_rbx + 32), *(unsigned __int64 *)(v_rbp - 65), (unsigned int)(0xFF0ULL), a4);
    if ((*(unsigned __int8 *)(v_rbx + 17)) != 4) goto loc_0021E181;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx) + 8)) != 0) goto loc_0021D95B;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 8))) == 0) goto loc_0021E17A;
loc_0021D95B:
loc_0021D962:
    if (3 < 2) goto loc_0021E549;
loc_0021D96D:
    result = KiComputeNewPriority(*(unsigned __int64 *)(v_rbp - 105), *(unsigned __int64 *)(v_rbp - 65), 1, a4);
    v_r14 = 63;
    if ((unsigned __int8)(v_r15) == 0) { v_r14 = (unsigned int)((unsigned __int8)(result)); }
loc_0021D98E:
    v_rbx = 4;
    if (!(condition_is_above_or_equal)) {
        v_rbx = (unsigned __int8)((4) | (2));
    }
    result = (unsigned __int8)(~((unsigned __int8)(v_rbx)));
    a1 = ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rbp - 105) + 120)))) & (8)) == 0) ? 1 : 0;
    a1 = (unsigned __int8)((a1) & ((unsigned __int8)(result)));
    if ((((unsigned __int8)(a1)) & (1)) != 0) goto loc_0021E2E2;
loc_0021D9BE:
    if ((*(unsigned int *)(v_rip + 14317275)) == 0) goto loc_0021DA19;
    v_rbx = (unsigned __int8)((v_rbx) & (6));
    a1 = (((unsigned __int8)(v_rbx)) == 6) ? 1 : 0;
    result = ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rbp - 105) + 120)))) & (8)) == 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) == 0) goto loc_0021DA19;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp - 105) + 195)) <= 0) goto loc_0021DA19;
    v_rdi = (unsigned __int8)((1) | (2));
    goto loc_0021DA19;
loc_0021D9EA:
    v_rbx = (unsigned int)((v_rbx) + ((unsigned int)(result)));
    if (((unsigned int)(v_rbx)) >= 16) { v_rbx = 15; }
    v_rbx = (unsigned int)((v_rbx) - ((unsigned int)(result)));
loc_0021D9F9:
    result = Feature_StackingDecayBoosts__private_IsEnabledNoReportingNoInline(15, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rbp - 105) + 120)), 1, a4);
    a3 = 0;
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_rbx + 32) + 870) = (unsigned __int8)(v_rbx);
    a2 = 0;
    result = KiComputeThreadPriority(*(unsigned __int64 *)(v_rbx + 32), a2, a3, a4);
loc_0021DA19:
    if (((unsigned __int8)((unsigned __int8)(result))) == 63) goto loc_0021DA69;
    if (((unsigned __int8)((unsigned __int8)(result))) > (*(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp - 105) + 195))) goto loc_0021EABD;
loc_0021DA35:
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp - 105) + 195) = (unsigned __int8)((unsigned __int8)(result));
    result = KiComputeThreadQos(*(unsigned __int64 *)(v_rbp - 105), a2, a3, a4);
    if (((unsigned int)(result)) != ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp - 105) + 516)))) {
        *(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp - 105) + 516) = (unsigned __int8)(result);
    }
    if (((*(unsigned int *)(*(unsigned __int64 *)(v_rbp - 105) + 120)) & (0x400000ULL)) != 0) goto loc_0021E27A;
loc_0021DA69:
    if ((((unsigned __int8)(v_rdi)) & (2)) != 0) goto loc_0021EB6C;
loc_0021DA73:
    v_rdi = (unsigned int)((v_rdi) & (1));
    v_rdi = (unsigned int)((v_rdi) << (5));
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 105) + 568)) != (*(unsigned __int64 *)(v_rip + 14324094))) goto loc_0021E431;
loc_0021DA8D:
    result = (*(unsigned __int64 *)(v_rbp + 103)) & (-2);
    result = (result) | (1);
    *(unsigned __int64 *)(v_rbp - 81) = result;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 103) + 36440))) == 0) goto loc_0021DAFB;
loc_0021DAC0:
    v_rsi = 0;
loc_0021DAC5:
    if (condition_is_above_or_equal) goto loc_0021DAE9;
loc_0021DACE:
    v_rsi = (unsigned int)((v_rsi) + 1);
    if (((*(unsigned int *)(v_rip + 14317526)) & ((unsigned int)(v_rsi))) == 0) goto loc_0021DBE5;
loc_0021DADC:
loc_0021DADE:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 103) + 36440) + 8) + 48) == 0) goto loc_0021DAC5;
    goto loc_0021DACE;
loc_0021DAE9:
    v_r14 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 103) + 36440) + 8) + (8);
    v_r15 = ((unsigned int)((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 103) + 36440))))) - (1);
    if (condition_is_not_equal) goto loc_0021DAC0;
loc_0021DAFB:
    v_rdi = (unsigned int)((v_rdi) | (15));
    a2 = ((unsigned int)(*(unsigned int *)(v_rip + 14324384))) + (*(unsigned __int64 *)(v_rbp - 25));
    *(unsigned int *)(v_rbp + 127) = (unsigned int)(v_rdi);
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 103) + 36440) + 8) + 48);
    if (a2 >= = (*(unsigned __int64 *)(v_rbp - 33))) {
        result = (unsigned int)(v_rdi);
        result = (unsigned int)((result) & (0xFFFFFFFAULL));
        *(unsigned int *)(v_rbp + 127) = (unsigned int)(result);
    }
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) & (0xFFFFFFFAULL));
    if (a2 <= (*(unsigned __int64 *)(v_rbp - 33))) { a1 = (unsigned int)(v_rdi); }
    *(unsigned int *)(v_rbp + 127) = (unsigned int)(a1);
    if ((unsigned __int8)(v_r12) == 0) {
        result = (unsigned int)(a1);
        result = (unsigned int)((result) & (0xFFFFFFF3ULL));
        *(unsigned int *)(v_rbp + 127) = (unsigned int)(result);
    }
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)(a1))) & (0xFFFFFFF3ULL));
    if ((unsigned __int8)(v_r12) != 0) { v_rbx = (unsigned int)(a1); }
    v_r12 = 0;
    *(unsigned int *)(v_rbp - 97) = 0;
    if (((unsigned int)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp - 105) + 195)))) > ((unsigned int)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp - 17) + 195))))) goto loc_0021DC0C;
    if ((((unsigned __int8)(v_rbx)) & (4)) != 0) goto loc_0021E165;
    if ((((unsigned __int8)(v_rbx)) & (8)) == 0) goto loc_0021E341;
    result = Feature_StackingDecayBoosts__private_IsEnabledNoReportingNoInline(a1, a2, *(unsigned __int64 *)(v_rbp + 103), a4);
    if ((unsigned int)(result) == 0) goto loc_0021E2A5;
    if (((unsigned __int8)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp - 17) + 195)))) >= 16) goto loc_0021E8F3;
loc_0021DB99:
    a2 = 10;
    if ((*(unsigned int *)(v_rip + 14316800)) != 0) { a2 = 11; }
    result = KiComputeThreadPriority(*(unsigned __int64 *)(v_rbp - 17), a2, 1, a4);
loc_0021DBB8:
loc_0021DBBA:
    a2 = (unsigned int)((unsigned int)(result));
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) > ((unsigned int)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp - 17) + 195))))) { a2 = (unsigned int)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp - 17) + 195))); }
loc_0021DBCB:
    *(unsigned int *)(v_rbp - 97) = (unsigned int)(a2);
    if (((unsigned int)(a2)) >= 16) goto loc_0021E550;
loc_0021DBD7:
loc_0021DBDA:
    if (((unsigned int)(a2)) >= ((unsigned int)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp - 105) + 195))))) goto loc_0021E1DF;
    goto loc_0021DC1A;
loc_0021DBE5:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14323405)))) & (64)) == 0) goto loc_0021DADC;
    result = KiCheckVpBackingLongSpinWaitHypercall(*(unsigned __int64 *)(v_rbp - 17), a2, *(unsigned __int64 *)(v_rbp + 103), a4);
    if ((unsigned __int8)(result) == 0) goto loc_0021DADC;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)((unsigned int)((unsigned int)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp - 105) + 195)))))), a2, *(unsigned __int64 *)(v_rbp + 103), a4);
    goto loc_0021DADE;
loc_0021DC0C:
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp - 17) + 565) = 1;
    v_rbx = (unsigned int)((v_rbx) & (0xFFFFFFFEULL));
loc_0021DC1A:
    v_rdi = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) & (0xFFFFFFFDULL));
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 103) + 16) == 0) { v_rdi = (unsigned int)(v_rbx); }
    a2 = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) & (1));
    a2 = (unsigned int)((a2) + ((unsigned int)((unsigned int)((unsigned int)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp - 105) + 195)))))));
    a4 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rbp + 103) + 33752))) | ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 103) + 36424) + 8)))));
    *(unsigned int *)(v_rbp - 49) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 103) + 36424) + 8)));
    if (((unsigned int)(a2)) > ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 103) + 36424) + 8))))) goto loc_0021E0F5;
loc_0021DC59:
    v_rdi = (unsigned int)((v_rdi) & (0xFFFFFFFDULL));
loc_0021DC5C:
    if (((unsigned __int16)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp + 103) + 208))) >= (*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 105) + 576)))) goto loc_0021DC88;
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 105) + 576) + *(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp + 103) + 208) * 8 + 8)) >> ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp + 103) + 209)));
    if ((((unsigned __int8)(a2)) & (1)) == 0) {
        v_rdi = (unsigned int)((v_rdi) & (0xFFFFFFFDULL));
    }
    if (condition_is_above_or_equal) goto loc_0021E814;
    if (condition_is_below) goto loc_0021E814;
loc_0021DCA4:
    if ((((unsigned __int8)(v_rdi)) & (1)) != 0) goto loc_0021E18D;
loc_0021DCAE:
    if ((((unsigned __int8)(v_rdi)) & (32)) == 0) goto loc_0021DCE2;
    result = KiQueryQuantumReset(*(unsigned __int64 *)(v_rbp - 105), a2, *(unsigned __int64 *)(v_rbp + 103), a4);
    result = (unsigned int)((result) * (*(unsigned int *)(v_rip + 14316498)));
    a1 = ((unsigned int)((unsigned int)(result))) + (*(unsigned __int64 *)(v_rbp - 65));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rbp - 105) + 120)))) & (32)) != 0) {
    }
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 105) + 32) = a1;
loc_0021DCE2:
    if (((unsigned int)((unsigned int)((unsigned int)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp - 105) + 195)))))) == ((unsigned int)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp - 105) + 195))))) goto loc_0021DD4B;
    result = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rbp - 105) + 518)))) >> (4));
    if (((unsigned int)((unsigned __int8)(result))) < ((unsigned int)((unsigned int)((unsigned int)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp - 105) + 195))))))) goto loc_0021E1E6;
loc_0021DD00:
    if (((unsigned __int8)((unsigned int)((unsigned int)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp - 105) + 195)))))) > (*(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp - 105) + 195))) goto loc_0021EAD2;
loc_0021DD17:
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp - 105) + 195) = (unsigned __int8)((unsigned int)((unsigned int)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp - 105) + 195)))));
    result = KiComputeThreadQos(*(unsigned __int64 *)(v_rbp - 105), a2, *(unsigned __int64 *)(v_rbp + 103), a4);
    if (((unsigned int)(result)) != ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp - 105) + 516)))) {
        *(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp - 105) + 516) = (unsigned __int8)(result);
    }
    if (((*(unsigned int *)(*(unsigned __int64 *)(v_rbp - 105) + 120)) & (0x400000ULL)) != 0) goto loc_0021E2B5;
loc_0021DD4B:
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp - 105) + 567) = (unsigned __int8)((unsigned int)(*(unsigned int *)(v_rbp + 111)));
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp - 105) + 566) = 0;
    if ((((unsigned __int8)((unsigned int)((unsigned int)(v_rdi)))) & (2)) == 0) goto loc_0021E0E8;
    a2 = 0;
    result = memset(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 103) + 14312), a2, 240, a4);
    result = KiStartRescheduleContext(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 103) + 14312), v_rbp - 81, *(unsigned __int64 *)(v_rbp - 105), a4);
    v_rsi = 0;
loc_0021DDA0:
    if (0 >= ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 103) + 14312))))) goto loc_0021DDC5;
    if ((*(unsigned __int64 *)(0 + 0 * 4 * 8 + *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 103) + 14312) * 1 + 16)) == (*(unsigned __int64 *)(v_rbp + 103))) goto loc_0021DDBE;
    a2 = (unsigned int)((0) + 1);
    goto loc_0021DDA0;
loc_0021DDBE:
    a3 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 103) + 14312) + 16) + (0 + 0 * 4 * 8);
loc_0021DDC5:
    *(unsigned __int64 *)(a3 + 16) = *(unsigned __int64 *)(*(unsigned __int64 *)(a3) + 24);
    result = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(a3 + 32))) & (197));
    result = (unsigned __int8)((result) | (5));
    *(unsigned __int8 *)(a3 + 32) = (unsigned __int8)(result);
    *(unsigned __int64 *)(a3 + 24) = *(unsigned __int64 *)(*(unsigned __int64 *)(a3) + 24);
    if ((((unsigned __int8)(*(unsigned __int8 *)(a3 + 32))) & (2)) != 0) goto loc_0021E9C2;
loc_0021DDFB:
loc_0021DE10:
    if (0 >= ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 103) + 14312))))) goto loc_0021DE35;
    if ((*(unsigned __int64 *)(0 + 0 * 4 * 8 + *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 103) + 14312) * 1 + 16)) == (*(unsigned __int64 *)(v_rbp + 103))) goto loc_0021DE2E;
    a2 = (unsigned int)((0) + 1);
    goto loc_0021DE10;
loc_0021DE2E:
    v_rbx = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 103) + 14312) + 16) + (0 + 0 * 4 * 8);
loc_0021DE35:
    *(unsigned __int64 *)(v_rbp + 23) = 0;
    if ((*(unsigned __int8 *)(v_rip + 14322816)) == 0) goto loc_0021E836;
    a3 = 0;
    result = KiEvaluateGroupSchedulingPreemption(v_rbx, *(unsigned __int64 *)(v_rbp - 105), a3, v_rbp + 23);
    if ((unsigned __int8)(result) == 0) goto loc_0021DE7F;
loc_0021DE5C:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rbp - 105) + 120))) >> (1));
    result = (unsigned int)((*(unsigned __int8 *)(v_rbx + 32)) >> (1));
    a1 = (unsigned int)((a1) & (1));
    result = (unsigned int)((result) & (1));
    if (((unsigned int)(a1)) < ((unsigned int)(result))) { a1 = (unsigned int)(result); }
    if (((unsigned int)(a1)) == 1) goto loc_0021E973;
loc_0021DE7D:
loc_0021DE7F:
    v_rdi = (unsigned int)((1 + 1 * 1) ^ ((unsigned int)((unsigned int)((unsigned int)(v_rdi)))));
    v_rdi = (unsigned int)((v_rdi) & (2));
    v_rdi = (unsigned int)((v_rdi) ^ ((unsigned int)((unsigned int)((unsigned int)(v_rdi)))));
    if (1 == 0) goto loc_0021E0E8;
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp - 105) + 565) = 0;
    a4 = 0;
    v_stack_p20 = v_rbp - 57;
    result = KiScheduleThreadToRescheduleContext(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 103) + 14312), *(unsigned __int64 *)(v_rbp - 105), *(unsigned __int64 *)(v_rbp + 103), a4);
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)((unsigned __int8)(result)))) << (7));
    v_rbx = (unsigned int)((v_rbx) ^ ((unsigned int)(v_rdi)));
    v_rbx = (unsigned int)((v_rbx) & (128));
    v_rbx = (unsigned int)((v_rbx) ^ ((unsigned int)(v_rdi)));
    if ((((unsigned __int8)((unsigned __int8)(result))) & (1)) != 0) goto loc_0021E4A3;
loc_0021DED6:
    v_r14 = 0;
    if (((*(unsigned int *)(v_rip + 14322731)) & (0x400ULL)) != 0) { v_rsi = 2; }
    v_rdi = 0;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 103) + 14312))) <= 0) goto loc_0021DF26;
loc_0021DEF5:
    a1 = (0) + (2);
    a1 = (a1 + v_rdi * 4 * 8) + (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 103) + 14312));
    result = KiCommitRescheduleContextEntry(a1, *(unsigned __int64 *)(v_rbp + 103), (unsigned int)((unsigned int)(v_rsi)), v_rbp - 57);
    v_r14 = (unsigned __int8)((v_r14) | ((unsigned __int8)(result)));
    v_rdi = (unsigned int)((v_rdi) + 1);
    if (((unsigned int)(v_rdi)) < ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 103) + 14312))))) goto loc_0021DEF5;
loc_0021DF26:
    if ((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 103) + 14312) + 8)) != 1) goto loc_0021DF49;
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 103) + 14312) + 16) + 36440) + 1)) + 1);
    *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 103) + 14312) + 16) + 36440) + 1) = (unsigned __int8)(result);
    if (((unsigned __int8)(result)) >= (*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 103) + 14312) + 16) + 36440)))) {
        *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 103) + 14312) + 16) + 36440) + 1) = 0;
    }
    a3 = 0;
    v_rdi = (unsigned int)(((unsigned __int8)(v_r14)) << (8));
    a4 = (*(unsigned __int64 *)(v_rbp - 81)) & (-2);
    v_rdi = (unsigned int)((v_rdi) ^ ((unsigned int)(v_rbx)));
    *(unsigned __int64 *)(v_rbp + 31) = a4;
    v_rdi = (unsigned int)((v_rdi) & (256));
    a2 = 0;
    v_rdi = (unsigned int)((v_rdi) ^ ((unsigned int)(v_rbx)));
    result = (unsigned int)((*(unsigned __int64 *)(v_rbp - 81)) & (1));
    if (condition_is_equal) goto loc_0021E16C;
    if (((unsigned int)(result)) == 1) {
        result = *(unsigned __int64 *)(a4 + 36440);
        a3 = *(unsigned __int64 *)(a4 + 36440);
        a3 = (a3) + (8);
        a2 = *(unsigned __int8 *)(result);
    }
    if ((unsigned int)(a2) == 0) goto loc_0021DFB3;
loc_0021DFA0:
    if ((unsigned int)(a2 - 1) != 0) goto loc_0021DFA0;
loc_0021DFB3:
    v_rbx = 0;
    v_rdi = (unsigned int)((v_rdi) | (80));
    *(unsigned __int64 *)(v_rbp - 81) = 0;
    *(unsigned int *)(v_rbp + 127) = (unsigned int)(v_rdi);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 105) + 64) = 0;
    if (condition_is_below) goto loc_0021E619;
loc_0021DFD1:
    if ((*(unsigned __int64 *)(v_rbp - 57)) != 0) goto loc_0021E269;
loc_0021DFDC:
loc_0021DFE0:
    v_rsi = 0;
    if ((((unsigned __int8)(v_rdi)) & (64)) != 0) goto loc_0021E03B;
    a1 = (0) & (-2);
    *(unsigned __int64 *)(v_rbp - 105) = a1;
    v_rbx = (unsigned int)((v_rbx) & (1));
    if (condition_is_equal) goto loc_0021E157;
    result = *(unsigned __int64 *)(v_rbp - 105);
    if (((unsigned int)(v_rbx)) == 1) {
        result = *(unsigned __int64 *)(a1 + 36440);
        a3 = *(unsigned __int64 *)(a1 + 36440);
        a3 = (a3) + (8);
        a2 = *(unsigned __int8 *)(result);
    }
    if ((unsigned int)(a2) == 0) goto loc_0021E032;
loc_0021E020:
    if ((unsigned int)(a2 - 1) != 0) goto loc_0021E020;
loc_0021E032:
    *(unsigned __int64 *)(v_rbp - 81) = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 105) + 64) = 0;
loc_0021E03B:
    if ((((unsigned int)(v_rdi)) & (0x600ULL)) == 0) goto loc_0021E0AF;
    result = a2 - 1;
    if (!(condition_is_above_or_equal)) {
        a3 = *(unsigned int *)(*(unsigned __int64 *)(v_rbp - 105) + 116);
        a4 = 0;
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 105) + 576);
        a1 = *(unsigned __int64 *)(v_rbp - 105);
        a2 = *(unsigned __int16 *)(*(unsigned __int64 *)(v_rbp - 105) + 584);
        a3 = (unsigned int)((a3) >> (3));
        a3 = (unsigned __int8)((a3) & (1));
        v_stack_p28 = 0x536ULL;
        v_stack_p20 = result;
        result = EtwTraceThreadAffinity(a1, a2, a3, a4);
    }
    if (condition_is_above_or_equal) goto loc_0021E0A5;
    if (((*(unsigned int *)(v_rip + 14322306)) & (0x8000000ULL)) != 0) {
        a4 = *(unsigned int *)(v_rbp - 73);
        a2 = 0x546ULL;
        a3 = *(unsigned int *)(v_rbp - 69);
        a1 = *(unsigned __int64 *)(v_rbp - 105);
        result = EtwTraceIdealProcessor(a1, a2, a3, a4);
    }
loc_0021E0AF:
    if ((((unsigned __int8)(v_rdi)) & (16)) == 0) goto loc_0021E3AD;
loc_0021E0B9:
    result = KiAbProcessPostContextSwitch(*(unsigned __int64 *)(v_rbp - 17), a2, a3, a4);
    result = ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 103) + 11528)) == 0) ? 1 : 0;
    v_rsp = (v_rsp) + (192);
    return result;
loc_0021E0E8:
    goto loc_0021DFE0;
loc_0021E0F5:
    if ((*(unsigned int *)(v_rbp - 89)) == ((unsigned int)(*(unsigned __int64 *)(v_rbp - 105)))) goto loc_0021DC5C;
    if (((unsigned int)(a4)) > 1) goto loc_0021DC59;
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 81) + 33840 + 8))) & (1)) != 0) goto loc_0021E908;
loc_0021E12B:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 81) + 33840 + 8) == 0) goto loc_0021DC5C;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 81) + 33840 + 8) + 36)))) != ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a34 + 424) + 124))))) goto loc_0021E928;
    *(unsigned int *)(v_rbp - 45) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 81) + 33840 + 8) + 36)));
    if (((unsigned int)(a2)) > ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 81) + 33840 + 8) + 36))))) goto loc_0021DC5C;
    goto loc_0021DC59;
loc_0021E157:
    goto loc_0021E020;
loc_0021E165:
    goto loc_0021DBCB;
loc_0021E16C:
    goto loc_0021DFA0;
loc_0021E17A:
    *(unsigned __int64 *)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 81) + 33840 + 8) + 32)) = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 81) + 33840 + 8) + 36));
    *(unsigned __int64 *)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 81) + 33840 + 8) + 36)) + 8) = *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 81) + 33840 + 8) + 32);
loc_0021E181:
    goto loc_0021D84F;
loc_0021E18D:
    a1 = (((unsigned int)(a2)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 81) + 33840 + 8) + 36))))) ? 1 : 0;
    result = ((((unsigned __int8)(v_rdi)) & (2)) != 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) == 0) goto loc_0021E41D;
    a1 = (*(unsigned __int64 *)(v_rbp - 65)) - (*(unsigned __int64 *)(v_rbp - 25));
    a1 = (a1) + (*(unsigned __int64 *)(v_rbp - 33));
loc_0021E1AD:
    if ((((unsigned __int8)(v_rdi)) & (2)) == 0) goto loc_0021E377;
loc_0021E1B7:
    v_rdi = (unsigned int)((v_rdi) & (0xFFFFFFDFULL));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 105) + 32) = a1;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 103) + 32) = *(unsigned __int64 *)(v_rbp - 25);
    goto loc_0021DCAE;
loc_0021E1D0:
    if (1 <= ((unsigned int)(v_r14))) goto loc_0021DBDA;
    *(unsigned int *)(v_rbp - 97) = (unsigned int)((unsigned int)((unsigned int)(v_r14)));
loc_0021E1DF:
    goto loc_0021DC1A;
loc_0021E1E6:
    result = (unsigned __int16)(((__int8)((unsigned __int8)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r14))))))) << (4));
    result = (unsigned __int16)((result) ^ ((unsigned __int16)(a1)));
    result = (unsigned __int16)((result) & ((unsigned __int16)((unsigned int)(0xFF0ULL))));
    result = (unsigned __int16)((result) ^ ((unsigned __int16)(a1)));
    *(unsigned __int16 *)(*(unsigned __int64 *)(v_rbp - 105) + 518) = (unsigned __int16)(result);
    goto loc_0021DD00;
loc_0021E20A:
    goto loc_0021D82A;
loc_0021E212:
    result = KiIsThreadConstrainedBySchedulingGroup(*(unsigned __int64 *)(v_rbp - 81), *(unsigned __int64 *)(v_rbp + 103), (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rbp + 103))), a4);
    if ((unsigned __int8)(result) == 0) goto loc_0021D82A;
    result = KiShouldPreemptionBeDeferred(*(unsigned __int64 *)(v_rbp - 81), *(unsigned __int64 *)(v_rbp + 103), (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rbp + 103))), a4);
    if ((unsigned __int8)(result) != 0) goto loc_0021D82A;
    result = KiCheckForMaxOverQuotaScb(*(unsigned __int64 *)(v_rbp + 103), *(unsigned __int64 *)(v_rbp + 103), (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rbp + 103))), a4);
    if ((unsigned __int8)(result) != 0) goto loc_0021E4C5;
loc_0021E245:
    a3 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rbp + 103)))) + (*(unsigned int *)(*(unsigned __int64 *)(v_rbp + 103) + 124)));
    if (condition_is_not_equal) goto loc_0021E257;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 103) + 416) != 0) goto loc_0021E245;
loc_0021E257:
    *(unsigned int *)(v_rbp - 89) = a3;
    if (a3 == 0) goto loc_0021D82A;
    goto loc_0021E4C8;
loc_0021E269:
    result = KiReadyDeferredReadyList(*(unsigned __int64 *)(v_rbp + 103), v_rbp - 57, a3, a4);
    goto loc_0021DFDC;
loc_0021E27A:
    if (((unsigned int)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp - 25) + 195)))) == ((unsigned int)((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 25) + 968))))))) goto loc_0021DA69;
    result = (unsigned int)(((unsigned int)((unsigned int)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp - 25) + 195))))) - ((unsigned int)((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 25) + 968)))))));
    goto loc_0021DA69;
loc_0021E2A5:
    a3 = 0;
    result = KiComputeNewPriorityNonStacking(*(unsigned __int64 *)(v_rbp + 103), (__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp - 25) + 195)), a3, a4);
    goto loc_0021DBB8;
loc_0021E2B5:
    if (((unsigned int)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp - 105) + 195)))) == ((unsigned int)((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 105) + 968))))))) goto loc_0021DD4B;
    result = (unsigned int)(((unsigned int)((unsigned int)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp - 105) + 195))))) - ((unsigned int)((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 105) + 968)))))));
    goto loc_0021DD4B;
loc_0021E2E2:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp - 25) + 195)) <= 0) goto loc_0021D9BE;
    if (((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rbp + 111)))) <= (*(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp - 25) + 870))) goto loc_0021DA19;
    result = Feature_StackingDecayBoosts__private_IsEnabledNoReportingNoInline(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 105) + 968), (__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp - 105) + 195)), (unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 105) + 968)))), a4);
    if ((unsigned int)(result) == 0) goto loc_0021D9EA;
    a1 = (unsigned int)((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rbp - 105) + 518)) & (15));
    a1 = (unsigned int)((a1) + ((unsigned int)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp - 105) + 563)))));
    if (((unsigned int)(a1)) >= 16) { a1 = 15; }
    v_rbx = (unsigned int)(((__int8)((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rbp + 111))))) + ((unsigned int)(a1)));
    if (((unsigned int)(v_rbx)) >= 16) { v_rbx = 15; }
    v_rbx = (unsigned int)((v_rbx) - ((unsigned int)(a1)));
    goto loc_0021D9F9;
loc_0021E341:
    *(unsigned int *)(v_rbp - 97) = (unsigned int)((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rbp - 105))));
    goto loc_0021DBD7;
loc_0021E34C:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14321510)))) & (64)) == 0) goto loc_0021D8B7;
    result = KiCheckVpBackingLongSpinWaitHypercall(a1, (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rbp - 105))), (unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 105) + 968)))), a4);
    if ((unsigned __int8)(result) == 0) goto loc_0021EAE5;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rbx)), (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rbp - 105))), (unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 105) + 968)))), a4);
    goto loc_0021D8B9;
loc_0021E377:
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp - 105) + 565) = 1;
    goto loc_0021E1B7;
loc_0021E385:
loc_0021E38C:
    if ((unsigned __int8)(result) != 0) goto loc_0021E38C;
    if (condition_is_above_or_equal) goto loc_0021D885;
    result = KiRemoveSystemWorkPriorityKick((unsigned int)((unsigned int)(v_rbx)), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 105) + 968)))))))), (unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 105) + 968)))), a4);
    goto loc_0021D885;
loc_0021E3AD:
    *(unsigned int *)(v_rbp + 103) = (unsigned int)(*(unsigned __int64 *)(v_rbp - 105));
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) >> (3));
    a1 = (unsigned __int16)((a1) & (1));
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) >> (2));
    a1 = (unsigned __int16)((a1) + ((unsigned __int16)(a1)));
    result = (unsigned __int16)((result) & (1));
    a1 = (unsigned __int16)((a1) | ((unsigned __int16)(result)));
    v_rdi = (unsigned __int16)((v_rdi) & (1));
    a1 = (unsigned __int16)((a1) + ((unsigned __int16)(a1)));
    a1 = (unsigned __int16)((a1) | ((unsigned __int16)(v_rdi)));
    *(unsigned __int8 *)(v_rbp + 105) = (unsigned __int8)((unsigned int)(*(unsigned int *)(v_rbp - 97)));
    a1 = (unsigned __int16)((a1) + ((unsigned __int16)(a1)));
    *(unsigned __int16 *)(v_rbp + 103) = (unsigned __int16)(a1);
    *(unsigned __int64 *)(v_rbp - 9) = v_xmm0;
    *(unsigned __int8 *)(v_rbp + 3) = 1;
    *(unsigned __int64 *)(v_rbp - 9) = v_rbp + 103;
    *(unsigned int *)(v_rbp - 1) = 4;
    result = KiCanThreadBeReadiedImmediately(*(unsigned __int64 *)(v_rbp - 105), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 105) + 968)))))))), (unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 105) + 968)))), a4);
    if ((unsigned __int8)(result) == 0) goto loc_0021E91E;
    result = KiDeferredReadyThread(*(unsigned __int64 *)(v_rbp + 103), *(unsigned __int64 *)(v_rbp - 105), v_rbp - 9, a4);
    goto loc_0021E0B9;
loc_0021E41D:
    a1 = (*(unsigned __int64 *)(v_rbp + 103)) + ((unsigned int)(*(unsigned int *)(v_rip + 14322065)));
    v_r11 = (*(unsigned __int64 *)(v_rbp - 33)) - ((unsigned int)(*(unsigned int *)(v_rip + 14322065)));
    goto loc_0021E1AD;
loc_0021E431:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_r11 + 116)))) & (8)) != 0) goto loc_0021DA8D;
    *(unsigned int *)(v_rbp - 69) = (unsigned int)((unsigned int)(*(unsigned int *)(v_r11 + 588)));
    result = KiComputeThreadAffinity(v_r11, *(unsigned __int64 *)(v_rbp - 105), v_rbp - 9, a4);
    if ((unsigned int)(result) == 0) goto loc_0021DA8D;
    *(unsigned int *)(v_rbp - 73) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rbp - 105) + 588)));
    if (((*(unsigned int *)(v_rip + 14321311)) & (0x1000ULL)) != 0) {
    }
    if (((*(unsigned int *)(v_rip + 14321297)) & (0x8000000ULL)) != 0) goto loc_0021E962;
loc_0021E485:
    if (condition_is_below) goto loc_0021E495;
    if (condition_is_above_or_equal) goto loc_0021DA8D;
loc_0021E495:
    goto loc_0021DA8D;
loc_0021E4A3:
    result = KiSearchForNewThreadsForRescheduleContext(*(unsigned __int64 *)(v_rbp + 103), v_rbp - 57, v_rbp - 9, a4);
    goto loc_0021DED6;
loc_0021E4B4:
    if ((unsigned __int8)(*(unsigned __int64 *)(v_rbp + 103)) != 0) goto loc_0021E8BA;
    goto loc_0021DA19;
loc_0021E4C5:
    *(unsigned int *)(v_rbp - 89) = 1;
loc_0021E4C8:
    if (*(unsigned __int64 *)(v_r14 + 104) == 0) goto loc_0021D82A;
    v_r10 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rbp - 105) + 216))) + (*(unsigned __int64 *)(v_r14 + 104));
    result = KiIsThreadConstrainedBySchedulingGroup(v_r14, v_r10, (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rbp + 103))), a4);
    if ((unsigned __int8)(result) == 0) goto loc_0021E9B9;
    result = KiShouldPreemptionBeDeferred(v_r14, v_r10, (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rbp + 103))), a4);
    if ((unsigned __int8)(result) != 0) goto loc_0021E8B1;
    result = KiCheckForMaxOverQuotaScb(v_r10, v_r10, (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rbp + 103))), a4);
    if ((unsigned __int8)(result) != 0) goto loc_0021E9DD;
loc_0021E512:
    a3 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rbp + 103)))) + (*(unsigned int *)(v_r10 + 124)));
    if (condition_is_not_equal) goto loc_0021E524;
    if (*(unsigned __int64 *)(v_r10 + 416) != 0) goto loc_0021E512;
loc_0021E524:
    *(unsigned int *)(v_rbp - 93) = a3;
    if (a3 == 0) goto loc_0021D82A;
loc_0021E531:
    result = KiGetComparisonRanks(*(unsigned __int64 *)(v_rbp + 103), v_r10, v_rbp - 89, v_rbp - 93);
    goto loc_0021D82A;
loc_0021E549:
    goto loc_0021D96D;
loc_0021E550:
    if (((unsigned int)(v_r14)) >= 16) goto loc_0021E1D0;
    *(unsigned int *)(v_rbp - 97) = 15;
    goto loc_0021DBD7;
loc_0021E569:
    result = KiReadGuestSchedulerAssistPriority(*(unsigned __int64 *)(v_rbp - 105), v_rbp - 41, v_rbp - 89, v_rbp - 93);
    if (((unsigned int)((int)((unsigned int)(result)))) != ((unsigned int)((int)(*(unsigned int *)(*(unsigned __int64 *)(v_rbp - 105) + 1024))))) goto loc_0021EAEE;
    a3 = 0;
    a2 = 0;
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp - 105) + 870) = 0;
    result = KiComputeThreadPriority(*(unsigned __int64 *)(v_rbp - 105), a2, a3, (int)(*(unsigned int *)(*(unsigned __int64 *)(v_rbp - 105) + 1024)));
    if (((unsigned int)(result)) != ((unsigned int)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp - 105) + 195))))) goto loc_0021EB27;
loc_0021E5CE:
    if ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp - 105) + 1122)) != 0) goto loc_0021E87D;
loc_0021E5E1:
    if (((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp - 105) + 1122))) != ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp - 105) + 516)))) goto loc_0021EB60;
loc_0021E5F1:
    result = *(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp - 105) + 516);
    if (((*(unsigned int *)(*(unsigned __int64 *)(v_rbp - 105) + 120)) & (0x400000ULL)) != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 105) + 968);
    }
    if (((unsigned int)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp - 105) + 195)))) != ((unsigned int)((unsigned int)((unsigned int)(result))))) goto loc_0021E933;
loc_0021E611:
    goto loc_0021D8D6;
loc_0021E619:
    *(unsigned int *)(v_rbp - 85) = (unsigned int)((unsigned int)((unsigned int)(result)));
    result = (unsigned int)(((unsigned int)((unsigned int)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp - 105) + 195))))) >> (2));
    a1 = (unsigned int)(((unsigned int)((unsigned int)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp - 105) + 195))))) >> (3));
    result = (unsigned __int16)((result) & (1));
    a1 = (unsigned __int16)((a1) & (1));
    a1 = (unsigned __int16)((a1) + ((unsigned __int16)(a1)));
    v_r14 = 0;
    a1 = (unsigned __int16)((a1) | ((unsigned __int16)(result)));
    result = (unsigned __int16)(((unsigned __int16)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp - 105) + 195)))) & (1));
    a1 = (unsigned __int16)((a1) + ((unsigned __int16)(a1)));
    a1 = (unsigned __int16)((a1) | ((unsigned __int16)(result)));
    *(unsigned __int64 *)(v_rbp + 7) = v_xmm0;
    a1 = (unsigned __int16)((a1) + ((unsigned __int16)(a1)));
    *(unsigned __int8 *)(v_rbp - 83) = (unsigned __int8)((unsigned int)(*(unsigned int *)(v_rbp - 97)));
    a1 = (unsigned __int16)((a1) | (1));
    *(unsigned __int8 *)(v_rbp + 19) = 1;
    *(unsigned __int16 *)(v_rbp - 85) = (unsigned __int16)(a1);
    *(unsigned __int64 *)(v_rbp + 7) = v_rbp - 85;
    *(unsigned int *)(v_rbp + 15) = 4;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp + 103))) <= ((unsigned __int8)((unsigned int)((unsigned int)(result))))) goto loc_0021E712;
loc_0021E680:
    v_rbx = (v_r14 + v_r14 * 4 * 8) + (*(unsigned __int64 *)(v_rbp + 103));
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_rbx + 51))) & (16)) != 0) goto loc_0021E6A6;
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_rbx + 51))) & (8)) == 0) goto loc_0021E6C4;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rbx + 16) + 7)) == 0) goto loc_0021E6C4;
loc_0021E6A6:
    if ((unsigned __int8)(*(unsigned __int8 *)(1 + 13785)) != 0) goto loc_0021E723;
    *(unsigned __int8 *)(1 + 13785) = 1;
    *(unsigned int *)(1 + 13788) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rbx + 16) + 36)));
loc_0021E6C4:
    if (((*(unsigned __int8 *)(v_rbx + 51)) & ((unsigned __int8)(*(unsigned __int64 *)(v_rbp - 105)))) != 0) goto loc_0021E81C;
loc_0021E6CE:
    if (((*(unsigned __int8 *)(v_rbx + 51)) & (4)) == 0) goto loc_0021E6E8;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 16) + 36536) != 0) goto loc_0021E771;
loc_0021E6E8:
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 16) + 36536);
    if (((*(unsigned __int8 *)(v_rbx + 51)) & (1)) != 0) {
        result = *(unsigned __int64 *)(v_rbx + 40);
    }
    v_r14 = (unsigned int)((v_r14) + 1);
    if (((unsigned int)(v_r14)) < ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp + 103))))) goto loc_0021E680;
loc_0021E712:
    result = KiFlushSoftwareInterruptBatch(1 + 13784, a2, a3, (int)(*(unsigned int *)(*(unsigned __int64 *)(v_rbp - 105) + 1024)));
    goto loc_0021DFD1;
loc_0021E723:
    if (((unsigned __int8)(result)) != 1) goto loc_0021E768;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(1 + 13788)))) == (*(unsigned int *)(*(unsigned __int64 *)(v_rbx + 16) + 36))) goto loc_0021E6C4;
    *(unsigned __int8 *)(1 + 13785) = (unsigned __int8)(*(unsigned __int64 *)(v_rbp - 105));
    v_r15 = (1) + (0x35E0ULL);
    result = KeAddProcessorAffinityEx(v_r15, (unsigned int)(*(unsigned int *)(1 + 13788)), a3, (int)(*(unsigned int *)(*(unsigned __int64 *)(v_rbp - 105) + 1024)));
loc_0021E749:
    result = KeAddGroupAffinityEx(v_r15, *(unsigned __int8 *)(*(unsigned __int64 *)(v_rbx + 16) + 208), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 16) + 200), (int)(*(unsigned int *)(*(unsigned __int64 *)(v_rbp - 105) + 1024)));
    goto loc_0021E6C4;
loc_0021E768:
    v_r15 = (*(unsigned __int64 *)(v_rbp + 103)) + (0x35E0ULL);
    goto loc_0021E749;
loc_0021E771:
    if ((*(unsigned __int64 *)(v_r15 + 36536)) == 0) goto loc_0021E6E8;
    if (v_r15 == (*(unsigned __int64 *)(v_rbx + 16))) goto loc_0021E6E8;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result))))) & (0x40000ULL));
    if (condition_is_not_equal) goto loc_0021E80B;
loc_0021E79B:
    if (condition_is_below) goto loc_0021E7B9;
    if ((unsigned int)(result) == 0) goto loc_0021E6E8;
    if (((unsigned int)((unsigned __int8)((unsigned int)(*(unsigned int *)(result))))) >= ((unsigned int)(v_r15))) goto loc_0021E6E8;
loc_0021E7B9:
    *(unsigned int *)(*(unsigned __int64 *)(v_r15 + 36536) + 12) = (unsigned int)(*(unsigned __int64 *)(v_rbp - 105));
    result = (unsigned __int8)((unsigned int)(*(unsigned int *)(result)));
    v_r15 = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rbx + 16) + 36));
    if ((*(unsigned __int8 *)(v_rip + 14313543)) == 0) {
        result = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rbx + 16) + 36)));
        a2 = v_rip + 14346889;
        v_r15 = *(unsigned __int8 *)(a2 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rbx + 16) + 36)) * 2);
        v_r15 = (unsigned int)((v_r15) << (6));
        result = *(unsigned __int8 *)(a2 + result * 2 + 1);
        v_r15 = (unsigned int)((v_r15) | ((unsigned int)(result)));
    }
    *(unsigned int *)(*(unsigned __int64 *)(v_r15 + 36536) + 8) = (unsigned int)(v_r15);
    result = EtwTraceXSchedulerPriorityKickSend((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rbx + 16) + 36)), (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rbp - 105))), (unsigned int)(*(unsigned int *)(result)), v_r15 + 36536);
loc_0021E80B:
    goto loc_0021E79B;
loc_0021E814:
    v_rdi = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbp + 127))) & (0xFFFFFFFDULL));
    goto loc_0021DCA4;
loc_0021E81C:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 81) + 40)) != v_rdi) goto loc_0021E878;
loc_0021E82C:
    result = EtwTraceScheduleThread(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 81) + 40), *(unsigned __int64 *)(v_rbx + 16), v_rbp + 7, v_r15 + 36536);
    goto loc_0021E6CE;
loc_0021E836:
    if ((((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp - 81) + 32))) & (1)) != 0) goto loc_0021DE5C;
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp - 105) + 195))) > (*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 81) + 16) + 195))) goto loc_0021DE5C;
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp - 105) + 195))) != (*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 81) + 16) + 195))) goto loc_0021E865;
    if ((((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp - 81) + 32))) & (24)) != 0) goto loc_0021DE5C;
loc_0021E865:
    if ((((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp - 81) + 32))) & (16)) == 0) goto loc_0021E871;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp - 105) + 195)) != 0) goto loc_0021DE5C;
loc_0021E871:
    result = 0;
    goto loc_0021DE7F;
loc_0021E878:
    a3 = 0;
    goto loc_0021E82C;
loc_0021E87D:
    if (*(unsigned __int64 *)(v_r15 + 968) == 0) goto loc_0021E5E1;
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_r15 + 968)))) & (0x200000ULL));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_r15 + 968) + 28))) == 0) goto loc_0021EB3E;
loc_0021E8AA:
    a1 = 0;
    goto loc_0021E5E1;
loc_0021E8B1:
    *(unsigned int *)(v_rbp - 93) = (unsigned int)(v_r15);
    goto loc_0021D82A;
loc_0021E8BA:
    result = (unsigned __int16)((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rbp - 105) + 518)) & ((unsigned __int16)(a3)));
    v_rdi = (((unsigned __int16)(result)) < 0) ? 1 : 0;
    if ((*(unsigned __int64 *)(v_rbp - 65)) < (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 105) + 32))) goto loc_0021DA19;
    result = KiComputeNewPriority(*(unsigned __int64 *)(v_rbp - 105), *(unsigned __int64 *)(v_r15 + 968), 1, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_r15 + 968) + 32)));
    goto loc_0021DA19;
loc_0021E8F3:
    if (((*(unsigned int *)(v_r15 + 120)) & (0x400000ULL)) != 0) goto loc_0021DB99;
    goto loc_0021DBBA;
loc_0021E908:
    if ((*(unsigned __int64 *)(v_rbp - 105)) == 1) goto loc_0021DC5C;
    result = (result) | (1);
    result = (result) ^ (*(unsigned __int64 *)(v_rbp - 105));
    goto loc_0021E12B;
loc_0021E91E:
    result = KiInswapAndReadyThread(*(unsigned __int64 *)(v_rbp - 105), (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rbp - 105))), 1, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_r15 + 968) + 32)));
    goto loc_0021E0B9;
loc_0021E928:
    if (condition_is_below_or_equal) goto loc_0021DC59;
    goto loc_0021DC5C;
loc_0021E933:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14320091)))) & (32)) == 0) goto loc_0021E611;
    v_stack_p118 = v_rbp - 41;
    result = EtwTraceXSchedulerPriorityUpdate(v_r15, 1, (unsigned int)((unsigned int)(v_r14)), (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rbp - 81))));
    goto loc_0021E611;
loc_0021E962:
    if (((unsigned int)(*(unsigned __int64 *)(v_rbp - 81))) == ((unsigned int)(v_r15))) goto loc_0021E485;
    goto loc_0021E485;
loc_0021E973:
loc_0021E975:
    if (((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rbx + 16))))) >= ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp + 103))))) goto loc_0021DE7D;
    a1 = ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rbx + 16))))) * 4 + 2) + ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rbx + 16))))));
    a1 = (a1 * 8) + (*(unsigned __int64 *)(v_rbp + 103));
    if (a1 == (*(unsigned __int64 *)(v_rbp - 81))) goto loc_0021E9B5;
    a4 = 0;
    a3 = 0;
    result = KiDoesThreadDominateRescheduleContextEntry(a1, *(unsigned __int64 *)(v_rbp - 105), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0021DE7F;
loc_0021E9B5:
    v_rdi = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rbx + 16)))) + 1);
    goto loc_0021E975;
loc_0021E9B9:
    *(unsigned int *)(v_rbp - 93) = (unsigned int)(v_r15);
    goto loc_0021D82A;
loc_0021E9C2:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp + 103))) > ((unsigned __int8)(*(unsigned __int64 *)(v_rbx + 16)))) goto loc_0021E9F0;
loc_0021E9CB:
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rbp - 105))) & (2)) == 0) goto loc_0021DDFB;
    *(unsigned int *)(*(unsigned __int64 *)(v_rbp + 103) + 4) = (unsigned int)(*(unsigned __int64 *)(v_rbx + 16));
    goto loc_0021DDFB;
loc_0021E9DD:
    *(unsigned int *)(v_rbp - 93) = (unsigned int)(v_rdi);
    goto loc_0021E531;
loc_0021E9F0:
    result = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rbx + 16)))));
    if ((*(unsigned __int64 *)(v_rbp + 103) + 16 + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rbx + 16))))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rbx + 16))))) * 4 * 8) != 0) {
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 103) + 16 + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rbx + 16))))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rbx + 16))))) * 4 * 8);
        result = *(unsigned __int64 *)(a1 + 24);
        *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 103) + 16 + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rbx + 16))))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rbx + 16))))) * 4 * 8 + 16) = result;
        result = *(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp + 103) + 16 + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rbx + 16))))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rbx + 16))))) * 4 * 8 + 32);
        result = (unsigned __int8)((result) & (197));
        result = (unsigned __int8)((result) | (5));
        *(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp + 103) + 16 + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rbx + 16))))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rbx + 16))))) * 4 * 8 + 32) = (unsigned __int8)(result);
        result = *(unsigned __int64 *)(a1 + 24);
        *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 103) + 16 + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rbx + 16))))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rbx + 16))))) * 4 * 8 + 24) = result;
    }
    v_r10 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rbx + 16)))) + 1);
    if (((unsigned int)(v_r10)) < ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp + 103))))) goto loc_0021E9F0;
    goto loc_0021E9CB;
loc_0021EA3D:
    if ((*(unsigned __int64 *)(v_r15 + 808)) != 1) goto loc_0021DA35;
    if (a1 + 37240 == 0) goto loc_0021DA35;
    *(unsigned __int64 *)(v_r15 + 808) = *(unsigned __int64 *)(a1 + 37240);
    *(unsigned __int64 *)(a1 + 37240) = v_r15 + 808;
    result = KiAbQueueAutoBoostDpc(a1, a1 + 37240, v_r15 + 808, *(unsigned __int64 *)(v_rbp + 103) + 16 + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rbx + 16))))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rbx + 16))))) * 4 * 8);
    goto loc_0021DA35;
loc_0021EA7E:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 105) + 808)) != 1) goto loc_0021DD17;
    if (a1 + 37240 == 0) goto loc_0021DD17;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 105) + 808) = *(unsigned __int64 *)(a1 + 37240);
    *(unsigned __int64 *)(a1 + 37240) = *(unsigned __int64 *)(v_rbp - 105) + 808;
    result = KiAbQueueAutoBoostDpc(a1, a1 + 37240, *(unsigned __int64 *)(v_rbp - 105) + 808, *(unsigned __int64 *)(v_rbp + 103) + 16 + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rbx + 16))))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rbx + 16))))) * 4 * 8);
    goto loc_0021DD17;
loc_0021EABD:
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp - 105) + 792)) == 0) goto loc_0021DA35;
    goto loc_0021EA3D;
loc_0021EAD2:
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp - 105) + 792)) == 0) goto loc_0021DD17;
    goto loc_0021EA7E;
loc_0021EAE5:
    goto loc_0021D8B7;
loc_0021EAEE:
    v_stack_p118 = 0;
    result = KeBugCheckEx(343, v_r15, (__int8)((unsigned __int8)(v_r14)), 1);
loc_0021EB27:
    v_stack_p118 = 0;
    a1 = 0;
    result = KiUpdateThreadPriority(a1, v_r15, v_r15, (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rbp - 81))));
    goto loc_0021E5CE;
loc_0021EB3E:
    if ((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rbp - 81)))) != 0) goto loc_0021E8AA;
    if (condition_is_below) goto loc_0021E8AA;
    if ((unsigned int)(v_r15) == 0) goto loc_0021E5E1;
    goto loc_0021E8AA;
loc_0021EB60:
    *(unsigned __int8 *)(v_r15 + 516) = 0;
    goto loc_0021E5F1;
loc_0021EB6C:
    result = KiScheduleNextForegroundBoost((__int8)((unsigned __int8)(v_r14)) + v_r15 * 1, v_r15, v_r15, (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rbp - 81))));
    goto loc_0021DA73;
}
```

## 5. (Beta) C Style

```c
int64_t sub_0021D7F8(int64_t Arg1, int64_t Arg2, int32_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, uint64_t Arg8, uint64_t Arg9, uint64_t Arg10, uint64_t Arg11, uint64_t Arg12, uint64_t Arg13, uint64_t Arg14, uint64_t Arg15, uint64_t Arg16, uint64_t Arg17, uint64_t Arg18, uint64_t Arg19, uint64_t Arg20, uint64_t Arg21, uint64_t Arg22, uint64_t Arg23, uint64_t Arg24, uint64_t Arg25, uint64_t Arg26, uint64_t Arg27, uint64_t Arg28, uint64_t Arg29, uint64_t Arg30, uint64_t Arg31, uint64_t Arg32, uint64_t Arg33, int64_t Arg34)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_p110;
    uint64_t v_stack_p118;
    uint64_t v_stack_p20;
    uint16_t v_stack_p28;

    v_stack_p110 = local_r13;
    *(uint64_t *)(local_rbp - 0x11) = local_r14;
    result = KiAbProcessPreContextSwitch(Arg1, Arg2, Arg3, Arg4);
    *(uint32_t *)(local_rbp - 0x59) = (uint32_t)(local_r15);
    if (*(uint64_t *)(local_rbx + 0x68) == 0) goto loc_0021E20A;
    local_r13 = ((uint32_t)(*(uint32_t *)(local_rsi + 0xD8))) + (*(uint64_t *)(local_rbx + 0x68));
    if (condition_is_not_equal) goto loc_0021E212;
loc_0021D82A:
    local_rdi = (*(uint8_t *)(local_rbx + 0x24B) + *(uint8_t *)(local_rbx + 0x24B) * 2) << (4);
    local_rdi = (local_rdi) + (*(uint64_t *)(local_rbx + 0xD0));
loc_0021D843:
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(local_rbx + 0xD0) + 0x11))) < 5) goto loc_0021D92F;
loc_0021D84F:
    local_rbx = (*(uint64_t *)(local_rbx + 0xD0)) + (48);
    if (local_rbx != local_rdi) goto loc_0021D843;
    Arg3 = 0;
    result = KiUpdateTotalCyclesCurrentThread(*(uint64_t *)(local_rbp + 0x67), local_r14, Arg3, Arg4);
    *(uint64_t *)(local_rbp - 0x19) = result;
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8) != 0) goto loc_0021E385;
loc_0021D885:
    *(uint64_t *)(local_rbp - 0x21) = *(uint64_t *)(local_r14 + 0x20);
    *(uint64_t *)(local_rbp - 0x41) = *(uint64_t *)(*(uint64_t *)(local_rbp - 0x69) + 0x48);
loc_0021D8A0:
    if (condition_is_above_or_equal) goto loc_0021D8C4;
loc_0021D8A9:
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)(local_r15))) + 1);
    if (((*(uint32_t *)(v_rip + 0xDA79FB)) & ((uint32_t)(local_rbx))) == 0) goto loc_0021E34C;
loc_0021D8B7:
loc_0021D8B9:
    if (*(uint64_t *)(*(uint64_t *)(local_rbp - 0x69) + 0x40) == 0) goto loc_0021D8A0;
    goto loc_0021D8A9;
loc_0021D8C4:
    *(uint64_t *)(local_rbp - 0x29) = local_r15;
    if (((*(uint32_t *)(*(uint64_t *)(local_rbp - 0x69) + 0x78)) & (0x400000ULL)) != 0) goto loc_0021E569;
loc_0021D8D6:
    local_rdi = 0;
    if ((*(uint8_t *)(*(uint64_t *)(local_rbp - 0x69) + 0xC3)) >= 16) goto loc_0021E4B4;
    local_rbx = 0;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(256))) - (*(uint32_t *)(*(uint64_t *)(local_rbp - 0x69) + 0x1B4)));
    if ((*(uint64_t *)(local_rbp - 0x41)) >= (*(uint64_t *)(*(uint64_t *)(local_rbp - 0x69) + 0x20))) goto loc_0021D962;
    if ((*(uint8_t *)(*(uint64_t *)(local_rbp - 0x69) + 0x233)) >= 14) goto loc_0021D96D;
    if (((*(uint16_t *)(*(uint64_t *)(local_rbp - 0x69) + 0x206)) & ((uint16_t)((uint32_t)(0xFF0ULL)))) != 0) goto loc_0021D98E;
    if (((uint32_t)(Arg1)) < 2) goto loc_0021D98E;
    goto loc_0021D96D;
loc_0021D92F:
    result = KiAcquireKobjectLockSafe(*(uint64_t *)(local_rbx + 0x20), *(uint64_t *)(local_rbp - 0x41), (uint32_t)(0xFF0ULL), Arg4);
    if ((*(uint8_t *)(local_rbx + 0x11)) != 4) goto loc_0021E181;
    if ((*(uint64_t *)(*(uint64_t *)(local_rbx) + 0x8)) != 0) goto loc_0021D95B;
    if ((*(uint64_t *)(*(uint64_t *)(local_rbx + 0x8))) == 0) goto loc_0021E17A;
loc_0021D95B:
loc_0021D962:
    if (3 < 2) goto loc_0021E549;
loc_0021D96D:
    result = KiComputeNewPriority(*(uint64_t *)(local_rbp - 0x69), *(uint64_t *)(local_rbp - 0x41), 1, Arg4);
    local_r14 = 63;
    if ((uint8_t)(local_r15) == 0) { local_r14 = (uint32_t)((uint8_t)(result)); }
loc_0021D98E:
    local_rbx = 4;
    if (!(condition_is_above_or_equal)) {
        local_rbx = (uint8_t)((4) | (2));
    }
    result = (uint8_t)(~((uint8_t)(local_rbx)));
    Arg1 = ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rbp - 0x69) + 0x78)))) & (8)) == 0) ? 1 : 0;
    Arg1 = (uint8_t)((Arg1) & ((uint8_t)(result)));
    if ((((uint8_t)(Arg1)) & (1)) != 0) goto loc_0021E2E2;
loc_0021D9BE:
    if ((*(uint32_t *)(v_rip + 0xDA76DB)) == 0) goto loc_0021DA19;
    local_rbx = (uint8_t)((local_rbx) & (6));
    Arg1 = (((uint8_t)(local_rbx)) == 6) ? 1 : 0;
    result = ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rbp - 0x69) + 0x78)))) & (8)) == 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) == 0) goto loc_0021DA19;
    if ((*(uint8_t *)(*(uint64_t *)(local_rbp - 0x69) + 0xC3)) <= 0) goto loc_0021DA19;
    local_rdi = (uint8_t)((1) | (2));
    goto loc_0021DA19;
loc_0021D9EA:
    local_rbx = (uint32_t)((local_rbx) + ((uint32_t)(result)));
    if (((uint32_t)(local_rbx)) >= 16) { local_rbx = 15; }
    local_rbx = (uint32_t)((local_rbx) - ((uint32_t)(result)));
loc_0021D9F9:
    result = Feature_StackingDecayBoosts__private_IsEnabledNoReportingNoInline(15, (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rbp - 0x69) + 0x78)), 1, Arg4);
    Arg3 = 0;
    *(uint8_t *)(*(uint64_t *)(local_rbx + 0x20) + 0x366) = (uint8_t)(local_rbx);
    Arg2 = 0;
    result = KiComputeThreadPriority(*(uint64_t *)(local_rbx + 0x20), Arg2, Arg3, Arg4);
loc_0021DA19:
    if (((uint8_t)((uint8_t)(result))) == 63) goto loc_0021DA69;
    if (((uint8_t)((uint8_t)(result))) > (*(uint8_t *)(*(uint64_t *)(local_rbp - 0x69) + 0xC3))) goto loc_0021EABD;
loc_0021DA35:
    *(uint8_t *)(*(uint64_t *)(local_rbp - 0x69) + 0xC3) = (uint8_t)((uint8_t)(result));
    result = KiComputeThreadQos(*(uint64_t *)(local_rbp - 0x69), Arg2, Arg3, Arg4);
    if (((uint32_t)(result)) != ((uint32_t)(*(uint8_t *)(*(uint64_t *)(local_rbp - 0x69) + 0x204)))) {
        *(uint8_t *)(*(uint64_t *)(local_rbp - 0x69) + 0x204) = (uint8_t)(result);
    }
    if (((*(uint32_t *)(*(uint64_t *)(local_rbp - 0x69) + 0x78)) & (0x400000ULL)) != 0) goto loc_0021E27A;
loc_0021DA69:
    if ((((uint8_t)(local_rdi)) & (2)) != 0) goto loc_0021EB6C;
loc_0021DA73:
    local_rdi = (uint32_t)((local_rdi) & (1));
    local_rdi = (uint32_t)((local_rdi) << (5));
    if ((*(uint64_t *)(*(uint64_t *)(local_rbp - 0x69) + 0x238)) != (*(uint64_t *)(v_rip + 0xDA917E))) goto loc_0021E431;
loc_0021DA8D:
    result = (*(uint64_t *)(local_rbp + 0x67)) & (-2);
    result = (result) | (1);
    *(uint64_t *)(local_rbp - 0x51) = result;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(local_rbp + 0x67) + 0x8E58))) == 0) goto loc_0021DAFB;
loc_0021DAC0:
    local_rsi = 0;
loc_0021DAC5:
    if (condition_is_above_or_equal) goto loc_0021DAE9;
loc_0021DACE:
    local_rsi = (uint32_t)((local_rsi) + 1);
    if (((*(uint32_t *)(v_rip + 0xDA77D6)) & ((uint32_t)(local_rsi))) == 0) goto loc_0021DBE5;
loc_0021DADC:
loc_0021DADE:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rbp + 0x67) + 0x8E58) + 0x8) + 0x30) == 0) goto loc_0021DAC5;
    goto loc_0021DACE;
loc_0021DAE9:
    local_r14 = (*(uint64_t *)(*(uint64_t *)(local_rbp + 0x67) + 0x8E58) + 8) + (8);
    local_r15 = ((uint32_t)((uint32_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(local_rbp + 0x67) + 0x8E58))))) - (1);
    if (condition_is_not_equal) goto loc_0021DAC0;
loc_0021DAFB:
    local_rdi = (uint32_t)((local_rdi) | (15));
    Arg2 = ((uint32_t)(*(uint32_t *)(v_rip + 0xDA92A0))) + (*(uint64_t *)(local_rbp - 0x19));
    *(uint32_t *)(local_rbp + 0x7F) = (uint32_t)(local_rdi);
    result = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rbp + 0x67) + 0x8E58) + 0x8) + 0x30);
    if (Arg2 >= = (*(uint64_t *)(local_rbp - 0x21))) {
        result = (uint32_t)(local_rdi);
        result = (uint32_t)((result) & (0xFFFFFFFAULL));
        *(uint32_t *)(local_rbp + 0x7F) = (uint32_t)(result);
    }
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) & (0xFFFFFFFAULL));
    if (Arg2 <= (*(uint64_t *)(local_rbp - 0x21))) { Arg1 = (uint32_t)(local_rdi); }
    *(uint32_t *)(local_rbp + 0x7F) = (uint32_t)(Arg1);
    if ((uint8_t)(local_r12) == 0) {
        result = (uint32_t)(Arg1);
        result = (uint32_t)((result) & (0xFFFFFFF3ULL));
        *(uint32_t *)(local_rbp + 0x7F) = (uint32_t)(result);
    }
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) & (0xFFFFFFF3ULL));
    if ((uint8_t)(local_r12) != 0) { local_rbx = (uint32_t)(Arg1); }
    local_r12 = 0;
    *(uint32_t *)(local_rbp - 0x61) = 0;
    if (((uint32_t)((int8_t)(*(uint8_t *)(*(uint64_t *)(local_rbp - 0x69) + 0xC3)))) > ((uint32_t)((int8_t)(*(uint8_t *)(*(uint64_t *)(local_rbp - 0x11) + 0xC3))))) goto loc_0021DC0C;
    if ((((uint8_t)(local_rbx)) & (4)) != 0) goto loc_0021E165;
    if ((((uint8_t)(local_rbx)) & (8)) == 0) goto loc_0021E341;
    result = Feature_StackingDecayBoosts__private_IsEnabledNoReportingNoInline(Arg1, Arg2, *(uint64_t *)(local_rbp + 0x67), Arg4);
    if ((uint32_t)(result) == 0) goto loc_0021E2A5;
    if (((uint8_t)((int8_t)(*(uint8_t *)(*(uint64_t *)(local_rbp - 0x11) + 0xC3)))) >= 16) goto loc_0021E8F3;
loc_0021DB99:
    Arg2 = 10;
    if ((*(uint32_t *)(v_rip + 0xDA7500)) != 0) { Arg2 = 11; }
    result = KiComputeThreadPriority(*(uint64_t *)(local_rbp - 0x11), Arg2, 1, Arg4);
loc_0021DBB8:
loc_0021DBBA:
    Arg2 = (uint32_t)((uint32_t)(result));
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) > ((uint32_t)((int8_t)(*(uint8_t *)(*(uint64_t *)(local_rbp - 0x11) + 0xC3))))) { Arg2 = (uint32_t)((int8_t)(*(uint8_t *)(*(uint64_t *)(local_rbp - 0x11) + 0xC3))); }
loc_0021DBCB:
    *(uint32_t *)(local_rbp - 0x61) = (uint32_t)(Arg2);
    if (((uint32_t)(Arg2)) >= 16) goto loc_0021E550;
loc_0021DBD7:
loc_0021DBDA:
    if (((uint32_t)(Arg2)) >= ((uint32_t)((int8_t)(*(uint8_t *)(*(uint64_t *)(local_rbp - 0x69) + 0xC3))))) goto loc_0021E1DF;
    goto loc_0021DC1A;
loc_0021DBE5:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xDA8ECD)))) & (64)) == 0) goto loc_0021DADC;
    result = KiCheckVpBackingLongSpinWaitHypercall(*(uint64_t *)(local_rbp - 0x11), Arg2, *(uint64_t *)(local_rbp + 0x67), Arg4);
    if ((uint8_t)(result) == 0) goto loc_0021DADC;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)((uint32_t)((uint32_t)((int8_t)(*(uint8_t *)(*(uint64_t *)(local_rbp - 0x69) + 0xC3)))))), Arg2, *(uint64_t *)(local_rbp + 0x67), Arg4);
    goto loc_0021DADE;
loc_0021DC0C:
    *(uint8_t *)(*(uint64_t *)(local_rbp - 0x11) + 0x235) = 1;
    local_rbx = (uint32_t)((local_rbx) & (0xFFFFFFFEULL));
loc_0021DC1A:
    local_rdi = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) & (0xFFFFFFFDULL));
    if (*(uint64_t *)(*(uint64_t *)(local_rbp + 0x67) + 0x10) == 0) { local_rdi = (uint32_t)(local_rbx); }
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) & (1));
    Arg2 = (uint32_t)((Arg2) + ((uint32_t)((uint32_t)((uint32_t)((int8_t)(*(uint8_t *)(*(uint64_t *)(local_rbp - 0x69) + 0xC3)))))));
    Arg4 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rbp + 0x67) + 0x83D8))) | ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(local_rbp + 0x67) + 0x8E48) + 0x8)))));
    *(uint32_t *)(local_rbp - 0x31) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(local_rbp + 0x67) + 0x8E48) + 0x8)));
    if (((uint32_t)(Arg2)) > ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(local_rbp + 0x67) + 0x8E48) + 0x8))))) goto loc_0021E0F5;
loc_0021DC59:
    local_rdi = (uint32_t)((local_rdi) & (0xFFFFFFFDULL));
loc_0021DC5C:
    if (((uint16_t)(*(uint8_t *)(*(uint64_t *)(local_rbp + 0x67) + 0xD0))) >= (*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(local_rbp - 0x69) + 0x240)))) goto loc_0021DC88;
    Arg2 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rbp - 0x69) + 0x240) + *(uint8_t *)(*(uint64_t *)(local_rbp + 0x67) + 0xD0) * 8 + 0x8)) >> ((uint8_t)(*(uint8_t *)(*(uint64_t *)(local_rbp + 0x67) + 0xD1)));
    if ((((uint8_t)(Arg2)) & (1)) == 0) {
        local_rdi = (uint32_t)((local_rdi) & (0xFFFFFFFDULL));
    }
    if (condition_is_above_or_equal) goto loc_0021E814;
    if (condition_is_below) goto loc_0021E814;
loc_0021DCA4:
    if ((((uint8_t)(local_rdi)) & (1)) != 0) goto loc_0021E18D;
loc_0021DCAE:
    if ((((uint8_t)(local_rdi)) & (32)) == 0) goto loc_0021DCE2;
    result = KiQueryQuantumReset(*(uint64_t *)(local_rbp - 0x69), Arg2, *(uint64_t *)(local_rbp + 0x67), Arg4);
    result = (uint32_t)((result) * (*(uint32_t *)(v_rip + 0xDA73D2)));
    Arg1 = ((uint32_t)((uint32_t)(result))) + (*(uint64_t *)(local_rbp - 0x41));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rbp - 0x69) + 0x78)))) & (32)) != 0) {
    }
    *(uint64_t *)(*(uint64_t *)(local_rbp - 0x69) + 0x20) = Arg1;
loc_0021DCE2:
    if (((uint32_t)((uint32_t)((uint32_t)((int8_t)(*(uint8_t *)(*(uint64_t *)(local_rbp - 0x69) + 0xC3)))))) == ((uint32_t)((int8_t)(*(uint8_t *)(*(uint64_t *)(local_rbp - 0x69) + 0xC3))))) goto loc_0021DD4B;
    result = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(*(uint64_t *)(local_rbp - 0x69) + 0x206)))) >> (4));
    if (((uint32_t)((uint8_t)(result))) < ((uint32_t)((uint32_t)((uint32_t)((int8_t)(*(uint8_t *)(*(uint64_t *)(local_rbp - 0x69) + 0xC3))))))) goto loc_0021E1E6;
loc_0021DD00:
    if (((uint8_t)((uint32_t)((uint32_t)((int8_t)(*(uint8_t *)(*(uint64_t *)(local_rbp - 0x69) + 0xC3)))))) > (*(uint8_t *)(*(uint64_t *)(local_rbp - 0x69) + 0xC3))) goto loc_0021EAD2;
loc_0021DD17:
    *(uint8_t *)(*(uint64_t *)(local_rbp - 0x69) + 0xC3) = (uint8_t)((uint32_t)((uint32_t)((int8_t)(*(uint8_t *)(*(uint64_t *)(local_rbp - 0x69) + 0xC3)))));
    result = KiComputeThreadQos(*(uint64_t *)(local_rbp - 0x69), Arg2, *(uint64_t *)(local_rbp + 0x67), Arg4);
    if (((uint32_t)(result)) != ((uint32_t)(*(uint8_t *)(*(uint64_t *)(local_rbp - 0x69) + 0x204)))) {
        *(uint8_t *)(*(uint64_t *)(local_rbp - 0x69) + 0x204) = (uint8_t)(result);
    }
    if (((*(uint32_t *)(*(uint64_t *)(local_rbp - 0x69) + 0x78)) & (0x400000ULL)) != 0) goto loc_0021E2B5;
loc_0021DD4B:
    *(uint8_t *)(*(uint64_t *)(local_rbp - 0x69) + 0x237) = (uint8_t)((uint32_t)(*(uint32_t *)(local_rbp + 0x6F)));
    *(uint8_t *)(*(uint64_t *)(local_rbp - 0x69) + 0x236) = 0;
    if ((((uint8_t)((uint32_t)((uint32_t)(local_rdi)))) & (2)) == 0) goto loc_0021E0E8;
    Arg2 = 0;
    result = memset(*(uint64_t *)(*(uint64_t *)(local_rbp + 0x67) + 0x37E8), Arg2, 240, Arg4);
    result = KiStartRescheduleContext(*(uint64_t *)(*(uint64_t *)(local_rbp + 0x67) + 0x37E8), local_rbp - 81, *(uint64_t *)(local_rbp - 0x69), Arg4);
    local_rsi = 0;
loc_0021DDA0:
    if (0 >= ((uint32_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(local_rbp + 0x67) + 0x37E8))))) goto loc_0021DDC5;
    if ((*(uint64_t *)(0 + 0x0 * 4 * 8 + *(uint64_t *)(*(uint64_t *)(local_rbp + 0x67) + 0x37E8) * 1 + 0x10)) == (*(uint64_t *)(local_rbp + 0x67))) goto loc_0021DDBE;
    Arg2 = (uint32_t)((0) + 1);
    goto loc_0021DDA0;
loc_0021DDBE:
    Arg3 = (*(uint64_t *)(*(uint64_t *)(local_rbp + 0x67) + 0x37E8) + 16) + (0 + 0 * 4 * 8);
loc_0021DDC5:
    *(uint64_t *)(Arg3 + 0x10) = *(uint64_t *)(*(uint64_t *)(Arg3) + 0x18);
    result = (uint8_t)(((uint8_t)(*(uint8_t *)(Arg3 + 0x20))) & (197));
    result = (uint8_t)((result) | (5));
    *(uint8_t *)(Arg3 + 0x20) = (uint8_t)(result);
    *(uint64_t *)(Arg3 + 0x18) = *(uint64_t *)(*(uint64_t *)(Arg3) + 0x18);
    if ((((uint8_t)(*(uint8_t *)(Arg3 + 0x20))) & (2)) != 0) goto loc_0021E9C2;
loc_0021DDFB:
loc_0021DE10:
    if (0 >= ((uint32_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(local_rbp + 0x67) + 0x37E8))))) goto loc_0021DE35;
    if ((*(uint64_t *)(0 + 0x0 * 4 * 8 + *(uint64_t *)(*(uint64_t *)(local_rbp + 0x67) + 0x37E8) * 1 + 0x10)) == (*(uint64_t *)(local_rbp + 0x67))) goto loc_0021DE2E;
    Arg2 = (uint32_t)((0) + 1);
    goto loc_0021DE10;
loc_0021DE2E:
    local_rbx = (*(uint64_t *)(*(uint64_t *)(local_rbp + 0x67) + 0x37E8) + 16) + (0 + 0 * 4 * 8);
loc_0021DE35:
    *(uint64_t *)(local_rbp + 0x17) = 0;
    if ((*(uint8_t *)(v_rip + 0xDA8C80)) == 0) goto loc_0021E836;
    Arg3 = 0;
    result = KiEvaluateGroupSchedulingPreemption(local_rbx, *(uint64_t *)(local_rbp - 0x69), Arg3, local_rbp + 23);
    if ((uint8_t)(result) == 0) goto loc_0021DE7F;
loc_0021DE5C:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rbp - 0x69) + 0x78))) >> (1));
    result = (uint32_t)((*(uint8_t *)(local_rbx + 0x20)) >> (1));
    Arg1 = (uint32_t)((Arg1) & (1));
    result = (uint32_t)((result) & (1));
    if (((uint32_t)(Arg1)) < ((uint32_t)(result))) { Arg1 = (uint32_t)(result); }
    if (((uint32_t)(Arg1)) == 1) goto loc_0021E973;
loc_0021DE7D:
loc_0021DE7F:
    local_rdi = (uint32_t)((1 + 1 * 1) ^ ((uint32_t)((uint32_t)((uint32_t)(local_rdi)))));
    local_rdi = (uint32_t)((local_rdi) & (2));
    local_rdi = (uint32_t)((local_rdi) ^ ((uint32_t)((uint32_t)((uint32_t)(local_rdi)))));
    if (1 == 0) goto loc_0021E0E8;
    *(uint8_t *)(*(uint64_t *)(local_rbp - 0x69) + 0x235) = 0;
    Arg4 = 0;
    v_stack_p20 = local_rbp - 57;
    result = KiScheduleThreadToRescheduleContext(*(uint64_t *)(*(uint64_t *)(local_rbp + 0x67) + 0x37E8), *(uint64_t *)(local_rbp - 0x69), *(uint64_t *)(local_rbp + 0x67), Arg4);
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)((uint8_t)(result)))) << (7));
    local_rbx = (uint32_t)((local_rbx) ^ ((uint32_t)(local_rdi)));
    local_rbx = (uint32_t)((local_rbx) & (128));
    local_rbx = (uint32_t)((local_rbx) ^ ((uint32_t)(local_rdi)));
    if ((((uint8_t)((uint8_t)(result))) & (1)) != 0) goto loc_0021E4A3;
loc_0021DED6:
    local_r14 = 0;
    if (((*(uint32_t *)(v_rip + 0xDA8C2B)) & (0x400ULL)) != 0) { local_rsi = 2; }
    local_rdi = 0;
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(local_rbp + 0x67) + 0x37E8))) <= 0) goto loc_0021DF26;
loc_0021DEF5:
    Arg1 = (0) + (2);
    Arg1 = (Arg1 + local_rdi * 4 * 8) + (*(uint64_t *)(*(uint64_t *)(local_rbp + 0x67) + 0x37E8));
    result = KiCommitRescheduleContextEntry(Arg1, *(uint64_t *)(local_rbp + 0x67), (uint32_t)((uint32_t)(local_rsi)), local_rbp - 57);
    local_r14 = (uint8_t)((local_r14) | ((uint8_t)(result)));
    local_rdi = (uint32_t)((local_rdi) + 1);
    if (((uint32_t)(local_rdi)) < ((uint32_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(local_rbp + 0x67) + 0x37E8))))) goto loc_0021DEF5;
loc_0021DF26:
    if ((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(local_rbp + 0x67) + 0x37E8) + 0x8)) != 1) goto loc_0021DF49;
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rbp + 0x67) + 0x37E8) + 0x10) + 0x8E58) + 0x1)) + 1);
    *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rbp + 0x67) + 0x37E8) + 0x10) + 0x8E58) + 0x1) = (uint8_t)(result);
    if (((uint8_t)(result)) >= (*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rbp + 0x67) + 0x37E8) + 0x10) + 0x8E58)))) {
        *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rbp + 0x67) + 0x37E8) + 0x10) + 0x8E58) + 0x1) = 0;
    }
    Arg3 = 0;
    local_rdi = (uint32_t)(((uint8_t)(local_r14)) << (8));
    Arg4 = (*(uint64_t *)(local_rbp - 0x51)) & (-2);
    local_rdi = (uint32_t)((local_rdi) ^ ((uint32_t)(local_rbx)));
    *(uint64_t *)(local_rbp + 0x1F) = Arg4;
    local_rdi = (uint32_t)((local_rdi) & (256));
    Arg2 = 0;
    local_rdi = (uint32_t)((local_rdi) ^ ((uint32_t)(local_rbx)));
    result = (uint32_t)((*(uint64_t *)(local_rbp - 0x51)) & (1));
    if (condition_is_equal) goto loc_0021E16C;
    if (((uint32_t)(result)) == 1) {
        result = *(uint64_t *)(Arg4 + 0x8E58);
        Arg3 = *(uint64_t *)(Arg4 + 0x8E58);
        Arg3 = (Arg3) + (8);
        Arg2 = *(uint8_t *)(result);
    }
    if ((uint32_t)(Arg2) == 0) goto loc_0021DFB3;
loc_0021DFA0:
    if ((uint32_t)(Arg2 - 1) != 0) goto loc_0021DFA0;
loc_0021DFB3:
    local_rbx = 0;
    local_rdi = (uint32_t)((local_rdi) | (80));
    *(uint64_t *)(local_rbp - 0x51) = 0;
    *(uint32_t *)(local_rbp + 0x7F) = (uint32_t)(local_rdi);
    *(uint64_t *)(*(uint64_t *)(local_rbp - 0x69) + 0x40) = 0;
    if (condition_is_below) goto loc_0021E619;
loc_0021DFD1:
    if ((*(uint64_t *)(local_rbp - 0x39)) != 0) goto loc_0021E269;
loc_0021DFDC:
loc_0021DFE0:
    local_rsi = 0;
    if ((((uint8_t)(local_rdi)) & (64)) != 0) goto loc_0021E03B;
    Arg1 = (0) & (-2);
    *(uint64_t *)(local_rbp - 0x69) = Arg1;
    local_rbx = (uint32_t)((local_rbx) & (1));
    if (condition_is_equal) goto loc_0021E157;
    result = *(uint64_t *)(local_rbp - 0x69);
    if (((uint32_t)(local_rbx)) == 1) {
        result = *(uint64_t *)(Arg1 + 0x8E58);
        Arg3 = *(uint64_t *)(Arg1 + 0x8E58);
        Arg3 = (Arg3) + (8);
        Arg2 = *(uint8_t *)(result);
    }
    if ((uint32_t)(Arg2) == 0) goto loc_0021E032;
loc_0021E020:
    if ((uint32_t)(Arg2 - 1) != 0) goto loc_0021E020;
loc_0021E032:
    *(uint64_t *)(local_rbp - 0x51) = 0;
    *(uint64_t *)(*(uint64_t *)(local_rbp - 0x69) + 0x40) = 0;
loc_0021E03B:
    if ((((uint32_t)(local_rdi)) & (0x600ULL)) == 0) goto loc_0021E0AF;
    result = Arg2 - 1;
    if (!(condition_is_above_or_equal)) {
        Arg3 = *(uint32_t *)(*(uint64_t *)(local_rbp - 0x69) + 0x74);
        Arg4 = 0;
        result = *(uint64_t *)(*(uint64_t *)(local_rbp - 0x69) + 0x240);
        Arg1 = *(uint64_t *)(local_rbp - 0x69);
        Arg2 = *(uint16_t *)(*(uint64_t *)(local_rbp - 0x69) + 0x248);
        Arg3 = (uint32_t)((Arg3) >> (3));
        Arg3 = (uint8_t)((Arg3) & (1));
        v_stack_p28 = 0x536ULL;
        v_stack_p20 = result;
        result = EtwTraceThreadAffinity(Arg1, Arg2, Arg3, Arg4);
    }
    if (condition_is_above_or_equal) goto loc_0021E0A5;
    if (((*(uint32_t *)(v_rip + 0xDA8A82)) & (0x8000000ULL)) != 0) {
        Arg4 = *(uint32_t *)(local_rbp - 0x49);
        Arg2 = 0x546ULL;
        Arg3 = *(uint32_t *)(local_rbp - 0x45);
        Arg1 = *(uint64_t *)(local_rbp - 0x69);
        result = EtwTraceIdealProcessor(Arg1, Arg2, Arg3, Arg4);
    }
loc_0021E0AF:
    if ((((uint8_t)(local_rdi)) & (16)) == 0) goto loc_0021E3AD;
loc_0021E0B9:
    result = KiAbProcessPostContextSwitch(*(uint64_t *)(local_rbp - 0x11), Arg2, Arg3, Arg4);
    result = ((*(uint64_t *)(*(uint64_t *)(local_rbp + 0x67) + 0x2D08)) == 0) ? 1 : 0;
    local_rsp = (local_rsp) + (192);
    return result;
loc_0021E0E8:
    goto loc_0021DFE0;
loc_0021E0F5:
    if ((*(uint32_t *)(local_rbp - 0x59)) == ((uint32_t)(*(uint64_t *)(local_rbp - 0x69)))) goto loc_0021DC5C;
    if (((uint32_t)(Arg4)) > 1) goto loc_0021DC59;
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(local_rbp - 0x51) + 0x8430 + 0x8))) & (1)) != 0) goto loc_0021E908;
loc_0021E12B:
    if (*(uint64_t *)(*(uint64_t *)(local_rbp - 0x51) + 0x8430 + 0x8) == 0) goto loc_0021DC5C;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(local_rbp - 0x51) + 0x8430 + 0x8) + 0x24)))) != ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg34 + 0x1A8) + 0x7C))))) goto loc_0021E928;
    *(uint32_t *)(local_rbp - 0x2D) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(local_rbp - 0x51) + 0x8430 + 0x8) + 0x24)));
    if (((uint32_t)(Arg2)) > ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(local_rbp - 0x51) + 0x8430 + 0x8) + 0x24))))) goto loc_0021DC5C;
    goto loc_0021DC59;
loc_0021E157:
    goto loc_0021E020;
loc_0021E165:
    goto loc_0021DBCB;
loc_0021E16C:
    goto loc_0021DFA0;
loc_0021E17A:
    *(uint64_t *)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(local_rbp - 0x51) + 0x8430 + 0x8) + 0x20)) = (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(local_rbp - 0x51) + 0x8430 + 0x8) + 0x24));
    *(uint64_t *)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(local_rbp - 0x51) + 0x8430 + 0x8) + 0x24)) + 0x8) = *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(local_rbp - 0x51) + 0x8430 + 0x8) + 0x20);
loc_0021E181:
    goto loc_0021D84F;
loc_0021E18D:
    Arg1 = (((uint32_t)(Arg2)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(local_rbp - 0x51) + 0x8430 + 0x8) + 0x24))))) ? 1 : 0;
    result = ((((uint8_t)(local_rdi)) & (2)) != 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) == 0) goto loc_0021E41D;
    Arg1 = (*(uint64_t *)(local_rbp - 0x41)) - (*(uint64_t *)(local_rbp - 0x19));
    Arg1 = (Arg1) + (*(uint64_t *)(local_rbp - 0x21));
loc_0021E1AD:
    if ((((uint8_t)(local_rdi)) & (2)) == 0) goto loc_0021E377;
loc_0021E1B7:
    local_rdi = (uint32_t)((local_rdi) & (0xFFFFFFDFULL));
    *(uint64_t *)(*(uint64_t *)(local_rbp - 0x69) + 0x20) = Arg1;
    *(uint64_t *)(*(uint64_t *)(local_rbp + 0x67) + 0x20) = *(uint64_t *)(local_rbp - 0x19);
    goto loc_0021DCAE;
loc_0021E1D0:
    if (1 <= ((uint32_t)(local_r14))) goto loc_0021DBDA;
    *(uint32_t *)(local_rbp - 0x61) = (uint32_t)((uint32_t)((uint32_t)(local_r14)));
loc_0021E1DF:
    goto loc_0021DC1A;
loc_0021E1E6:
    result = (uint16_t)(((int8_t)((uint8_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r14))))))) << (4));
    result = (uint16_t)((result) ^ ((uint16_t)(Arg1)));
    result = (uint16_t)((result) & ((uint16_t)((uint32_t)(0xFF0ULL))));
    result = (uint16_t)((result) ^ ((uint16_t)(Arg1)));
    *(uint16_t *)(*(uint64_t *)(local_rbp - 0x69) + 0x206) = (uint16_t)(result);
    goto loc_0021DD00;
loc_0021E20A:
    goto loc_0021D82A;
loc_0021E212:
    result = KiIsThreadConstrainedBySchedulingGroup(*(uint64_t *)(local_rbp - 0x51), *(uint64_t *)(local_rbp + 0x67), (uint32_t)((uint32_t)(*(uint64_t *)(local_rbp + 0x67))), Arg4);
    if ((uint8_t)(result) == 0) goto loc_0021D82A;
    result = KiShouldPreemptionBeDeferred(*(uint64_t *)(local_rbp - 0x51), *(uint64_t *)(local_rbp + 0x67), (uint32_t)((uint32_t)(*(uint64_t *)(local_rbp + 0x67))), Arg4);
    if ((uint8_t)(result) != 0) goto loc_0021D82A;
    result = KiCheckForMaxOverQuotaScb(*(uint64_t *)(local_rbp + 0x67), *(uint64_t *)(local_rbp + 0x67), (uint32_t)((uint32_t)(*(uint64_t *)(local_rbp + 0x67))), Arg4);
    if ((uint8_t)(result) != 0) goto loc_0021E4C5;
loc_0021E245:
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(*(uint64_t *)(local_rbp + 0x67)))) + (*(uint32_t *)(*(uint64_t *)(local_rbp + 0x67) + 0x7C)));
    if (condition_is_not_equal) goto loc_0021E257;
    if (*(uint64_t *)(*(uint64_t *)(local_rbp + 0x67) + 0x1A0) != 0) goto loc_0021E245;
loc_0021E257:
    *(uint32_t *)(local_rbp - 0x59) = Arg3;
    if (Arg3 == 0) goto loc_0021D82A;
    goto loc_0021E4C8;
loc_0021E269:
    result = KiReadyDeferredReadyList(*(uint64_t *)(local_rbp + 0x67), local_rbp - 57, Arg3, Arg4);
    goto loc_0021DFDC;
loc_0021E27A:
    if (((uint32_t)((int8_t)(*(uint8_t *)(*(uint64_t *)(local_rbp - 0x19) + 0xC3)))) == ((uint32_t)((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(local_rbp - 0x19) + 0x3C8))))))) goto loc_0021DA69;
    result = (uint32_t)(((uint32_t)((uint32_t)((int8_t)(*(uint8_t *)(*(uint64_t *)(local_rbp - 0x19) + 0xC3))))) - ((uint32_t)((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(local_rbp - 0x19) + 0x3C8)))))));
    goto loc_0021DA69;
loc_0021E2A5:
    Arg3 = 0;
    result = KiComputeNewPriorityNonStacking(*(uint64_t *)(local_rbp + 0x67), (int8_t)(*(uint8_t *)(*(uint64_t *)(local_rbp - 0x19) + 0xC3)), Arg3, Arg4);
    goto loc_0021DBB8;
loc_0021E2B5:
    if (((uint32_t)((int8_t)(*(uint8_t *)(*(uint64_t *)(local_rbp - 0x69) + 0xC3)))) == ((uint32_t)((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(local_rbp - 0x69) + 0x3C8))))))) goto loc_0021DD4B;
    result = (uint32_t)(((uint32_t)((uint32_t)((int8_t)(*(uint8_t *)(*(uint64_t *)(local_rbp - 0x69) + 0xC3))))) - ((uint32_t)((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(local_rbp - 0x69) + 0x3C8)))))));
    goto loc_0021DD4B;
loc_0021E2E2:
    if ((*(uint8_t *)(*(uint64_t *)(local_rbp - 0x19) + 0xC3)) <= 0) goto loc_0021D9BE;
    if (((uint8_t)((uint32_t)(*(uint32_t *)(local_rbp + 0x6F)))) <= (*(uint8_t *)(*(uint64_t *)(local_rbp - 0x19) + 0x366))) goto loc_0021DA19;
    result = Feature_StackingDecayBoosts__private_IsEnabledNoReportingNoInline(*(uint64_t *)(*(uint64_t *)(local_rbp - 0x69) + 0x3C8), (int8_t)(*(uint8_t *)(*(uint64_t *)(local_rbp - 0x69) + 0xC3)), (uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(local_rbp - 0x69) + 0x3C8)))), Arg4);
    if ((uint32_t)(result) == 0) goto loc_0021D9EA;
    Arg1 = (uint32_t)((*(uint16_t *)(*(uint64_t *)(local_rbp - 0x69) + 0x206)) & (15));
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)((int8_t)(*(uint8_t *)(*(uint64_t *)(local_rbp - 0x69) + 0x233)))));
    if (((uint32_t)(Arg1)) >= 16) { Arg1 = 15; }
    local_rbx = (uint32_t)(((int8_t)((uint8_t)((uint32_t)(*(uint32_t *)(local_rbp + 0x6F))))) + ((uint32_t)(Arg1)));
    if (((uint32_t)(local_rbx)) >= 16) { local_rbx = 15; }
    local_rbx = (uint32_t)((local_rbx) - ((uint32_t)(Arg1)));
    goto loc_0021D9F9;
loc_0021E341:
    *(uint32_t *)(local_rbp - 0x61) = (uint32_t)((uint32_t)((uint32_t)(*(uint64_t *)(local_rbp - 0x69))));
    goto loc_0021DBD7;
loc_0021E34C:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xDA8766)))) & (64)) == 0) goto loc_0021D8B7;
    result = KiCheckVpBackingLongSpinWaitHypercall(Arg1, (uint32_t)((uint32_t)(*(uint64_t *)(local_rbp - 0x69))), (uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(local_rbp - 0x69) + 0x3C8)))), Arg4);
    if ((uint8_t)(result) == 0) goto loc_0021EAE5;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rbx)), (uint32_t)((uint32_t)(*(uint64_t *)(local_rbp - 0x69))), (uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(local_rbp - 0x69) + 0x3C8)))), Arg4);
    goto loc_0021D8B9;
loc_0021E377:
    *(uint8_t *)(*(uint64_t *)(local_rbp - 0x69) + 0x235) = 1;
    goto loc_0021E1B7;
loc_0021E385:
loc_0021E38C:
    if ((uint8_t)(result) != 0) goto loc_0021E38C;
    if (condition_is_above_or_equal) goto loc_0021D885;
    result = KiRemoveSystemWorkPriorityKick((uint32_t)((uint32_t)(local_rbx)), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(local_rbp - 0x69) + 0x3C8)))))))), (uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(local_rbp - 0x69) + 0x3C8)))), Arg4);
    goto loc_0021D885;
loc_0021E3AD:
    *(uint32_t *)(local_rbp + 0x67) = (uint32_t)(*(uint64_t *)(local_rbp - 0x69));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) >> (3));
    Arg1 = (uint16_t)((Arg1) & (1));
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) >> (2));
    Arg1 = (uint16_t)((Arg1) + ((uint16_t)(Arg1)));
    result = (uint16_t)((result) & (1));
    Arg1 = (uint16_t)((Arg1) | ((uint16_t)(result)));
    local_rdi = (uint16_t)((local_rdi) & (1));
    Arg1 = (uint16_t)((Arg1) + ((uint16_t)(Arg1)));
    Arg1 = (uint16_t)((Arg1) | ((uint16_t)(local_rdi)));
    *(uint8_t *)(local_rbp + 0x69) = (uint8_t)((uint32_t)(*(uint32_t *)(local_rbp - 0x61)));
    Arg1 = (uint16_t)((Arg1) + ((uint16_t)(Arg1)));
    *(uint16_t *)(local_rbp + 0x67) = (uint16_t)(Arg1);
    *(uint64_t *)(local_rbp - 0x9) = v_xmm0;
    *(uint8_t *)(local_rbp + 0x3) = 1;
    *(uint64_t *)(local_rbp - 0x9) = local_rbp + 103;
    *(uint32_t *)(local_rbp - 0x1) = 4;
    result = KiCanThreadBeReadiedImmediately(*(uint64_t *)(local_rbp - 0x69), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(local_rbp - 0x69) + 0x3C8)))))))), (uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(local_rbp - 0x69) + 0x3C8)))), Arg4);
    if ((uint8_t)(result) == 0) goto loc_0021E91E;
    result = KiDeferredReadyThread(*(uint64_t *)(local_rbp + 0x67), *(uint64_t *)(local_rbp - 0x69), local_rbp - 9, Arg4);
    goto loc_0021E0B9;
loc_0021E41D:
    Arg1 = (*(uint64_t *)(local_rbp + 0x67)) + ((uint32_t)(*(uint32_t *)(v_rip + 0xDA8991)));
    local_r11 = (*(uint64_t *)(local_rbp - 0x21)) - ((uint32_t)(*(uint32_t *)(v_rip + 0xDA8991)));
    goto loc_0021E1AD;
loc_0021E431:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_r11 + 0x74)))) & (8)) != 0) goto loc_0021DA8D;
    *(uint32_t *)(local_rbp - 0x45) = (uint32_t)((uint32_t)(*(uint32_t *)(local_r11 + 0x24C)));
    result = KiComputeThreadAffinity(local_r11, *(uint64_t *)(local_rbp - 0x69), local_rbp - 9, Arg4);
    if ((uint32_t)(result) == 0) goto loc_0021DA8D;
    *(uint32_t *)(local_rbp - 0x49) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rbp - 0x69) + 0x24C)));
    if (((*(uint32_t *)(v_rip + 0xDA869F)) & (0x1000ULL)) != 0) {
    }
    if (((*(uint32_t *)(v_rip + 0xDA8691)) & (0x8000000ULL)) != 0) goto loc_0021E962;
loc_0021E485:
    if (condition_is_below) goto loc_0021E495;
    if (condition_is_above_or_equal) goto loc_0021DA8D;
loc_0021E495:
    goto loc_0021DA8D;
loc_0021E4A3:
    result = KiSearchForNewThreadsForRescheduleContext(*(uint64_t *)(local_rbp + 0x67), local_rbp - 57, local_rbp - 9, Arg4);
    goto loc_0021DED6;
loc_0021E4B4:
    if ((uint8_t)(*(uint64_t *)(local_rbp + 0x67)) != 0) goto loc_0021E8BA;
    goto loc_0021DA19;
loc_0021E4C5:
    *(uint32_t *)(local_rbp - 0x59) = 1;
loc_0021E4C8:
    if (*(uint64_t *)(local_r14 + 0x68) == 0) goto loc_0021D82A;
    local_r10 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rbp - 0x69) + 0xD8))) + (*(uint64_t *)(local_r14 + 0x68));
    result = KiIsThreadConstrainedBySchedulingGroup(local_r14, local_r10, (uint32_t)((uint32_t)(*(uint64_t *)(local_rbp + 0x67))), Arg4);
    if ((uint8_t)(result) == 0) goto loc_0021E9B9;
    result = KiShouldPreemptionBeDeferred(local_r14, local_r10, (uint32_t)((uint32_t)(*(uint64_t *)(local_rbp + 0x67))), Arg4);
    if ((uint8_t)(result) != 0) goto loc_0021E8B1;
    result = KiCheckForMaxOverQuotaScb(local_r10, local_r10, (uint32_t)((uint32_t)(*(uint64_t *)(local_rbp + 0x67))), Arg4);
    if ((uint8_t)(result) != 0) goto loc_0021E9DD;
loc_0021E512:
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(*(uint64_t *)(local_rbp + 0x67)))) + (*(uint32_t *)(local_r10 + 0x7C)));
    if (condition_is_not_equal) goto loc_0021E524;
    if (*(uint64_t *)(local_r10 + 0x1A0) != 0) goto loc_0021E512;
loc_0021E524:
    *(uint32_t *)(local_rbp - 0x5D) = Arg3;
    if (Arg3 == 0) goto loc_0021D82A;
loc_0021E531:
    result = KiGetComparisonRanks(*(uint64_t *)(local_rbp + 0x67), local_r10, local_rbp - 89, local_rbp - 93);
    goto loc_0021D82A;
loc_0021E549:
    goto loc_0021D96D;
loc_0021E550:
    if (((uint32_t)(local_r14)) >= 16) goto loc_0021E1D0;
    *(uint32_t *)(local_rbp - 0x61) = 15;
    goto loc_0021DBD7;
loc_0021E569:
    result = KiReadGuestSchedulerAssistPriority(*(uint64_t *)(local_rbp - 0x69), local_rbp - 41, local_rbp - 89, local_rbp - 93);
    if (((uint32_t)((int32_t)((uint32_t)(result)))) != ((uint32_t)((int32_t)(*(uint32_t *)(*(uint64_t *)(local_rbp - 0x69) + 0x400))))) goto loc_0021EAEE;
    Arg3 = 0;
    Arg2 = 0;
    *(uint8_t *)(*(uint64_t *)(local_rbp - 0x69) + 0x366) = 0;
    result = KiComputeThreadPriority(*(uint64_t *)(local_rbp - 0x69), Arg2, Arg3, (int32_t)(*(uint32_t *)(*(uint64_t *)(local_rbp - 0x69) + 0x400)));
    if (((uint32_t)(result)) != ((uint32_t)((int8_t)(*(uint8_t *)(*(uint64_t *)(local_rbp - 0x69) + 0xC3))))) goto loc_0021EB27;
loc_0021E5CE:
    if ((uint32_t)(*(uint8_t *)(*(uint64_t *)(local_rbp - 0x69) + 0x462)) != 0) goto loc_0021E87D;
loc_0021E5E1:
    if (((uint32_t)(*(uint8_t *)(*(uint64_t *)(local_rbp - 0x69) + 0x462))) != ((uint32_t)(*(uint8_t *)(*(uint64_t *)(local_rbp - 0x69) + 0x204)))) goto loc_0021EB60;
loc_0021E5F1:
    result = *(uint8_t *)(*(uint64_t *)(local_rbp - 0x69) + 0x204);
    if (((*(uint32_t *)(*(uint64_t *)(local_rbp - 0x69) + 0x78)) & (0x400000ULL)) != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rbp - 0x69) + 0x3C8);
    }
    if (((uint32_t)((int8_t)(*(uint8_t *)(*(uint64_t *)(local_rbp - 0x69) + 0xC3)))) != ((uint32_t)((uint32_t)((uint32_t)(result))))) goto loc_0021E933;
loc_0021E611:
    goto loc_0021D8D6;
loc_0021E619:
    *(uint32_t *)(local_rbp - 0x55) = (uint32_t)((uint32_t)((uint32_t)(result)));
    result = (uint32_t)(((uint32_t)((uint32_t)((int8_t)(*(uint8_t *)(*(uint64_t *)(local_rbp - 0x69) + 0xC3))))) >> (2));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((int8_t)(*(uint8_t *)(*(uint64_t *)(local_rbp - 0x69) + 0xC3))))) >> (3));
    result = (uint16_t)((result) & (1));
    Arg1 = (uint16_t)((Arg1) & (1));
    Arg1 = (uint16_t)((Arg1) + ((uint16_t)(Arg1)));
    local_r14 = 0;
    Arg1 = (uint16_t)((Arg1) | ((uint16_t)(result)));
    result = (uint16_t)(((uint16_t)((int8_t)(*(uint8_t *)(*(uint64_t *)(local_rbp - 0x69) + 0xC3)))) & (1));
    Arg1 = (uint16_t)((Arg1) + ((uint16_t)(Arg1)));
    Arg1 = (uint16_t)((Arg1) | ((uint16_t)(result)));
    *(uint64_t *)(local_rbp + 0x7) = v_xmm0;
    Arg1 = (uint16_t)((Arg1) + ((uint16_t)(Arg1)));
    *(uint8_t *)(local_rbp - 0x53) = (uint8_t)((uint32_t)(*(uint32_t *)(local_rbp - 0x61)));
    Arg1 = (uint16_t)((Arg1) | (1));
    *(uint8_t *)(local_rbp + 0x13) = 1;
    *(uint16_t *)(local_rbp - 0x55) = (uint16_t)(Arg1);
    *(uint64_t *)(local_rbp + 0x7) = local_rbp - 85;
    *(uint32_t *)(local_rbp + 0xF) = 4;
    if ((*(uint8_t *)(*(uint64_t *)(local_rbp + 0x67))) <= ((uint8_t)((uint32_t)((uint32_t)(result))))) goto loc_0021E712;
loc_0021E680:
    local_rbx = (local_r14 + local_r14 * 4 * 8) + (*(uint64_t *)(local_rbp + 0x67));
    if ((((uint8_t)(*(uint8_t *)(local_rbx + 0x33))) & (16)) != 0) goto loc_0021E6A6;
    if ((((uint8_t)(*(uint8_t *)(local_rbx + 0x33))) & (8)) == 0) goto loc_0021E6C4;
    if ((*(uint8_t *)(*(uint64_t *)(local_rbx + 0x10) + 0x7)) == 0) goto loc_0021E6C4;
loc_0021E6A6:
    if ((uint8_t)(*(uint8_t *)(1 + 0x35D9)) != 0) goto loc_0021E723;
    *(uint8_t *)(1 + 0x35D9) = 1;
    *(uint32_t *)(1 + 0x35DC) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rbx + 0x10) + 0x24)));
loc_0021E6C4:
    if (((*(uint8_t *)(local_rbx + 0x33)) & ((uint8_t)(*(uint64_t *)(local_rbp - 0x69)))) != 0) goto loc_0021E81C;
loc_0021E6CE:
    if (((*(uint8_t *)(local_rbx + 0x33)) & (4)) == 0) goto loc_0021E6E8;
    if (*(uint64_t *)(*(uint64_t *)(local_rbx + 0x10) + 0x8EB8) != 0) goto loc_0021E771;
loc_0021E6E8:
    result = *(uint64_t *)(*(uint64_t *)(local_rbx + 0x10) + 0x8EB8);
    if (((*(uint8_t *)(local_rbx + 0x33)) & (1)) != 0) {
        result = *(uint64_t *)(local_rbx + 0x28);
    }
    local_r14 = (uint32_t)((local_r14) + 1);
    if (((uint32_t)(local_r14)) < ((uint32_t)(*(uint8_t *)(*(uint64_t *)(local_rbp + 0x67))))) goto loc_0021E680;
loc_0021E712:
    result = KiFlushSoftwareInterruptBatch(1 + 13784, Arg2, Arg3, (int32_t)(*(uint32_t *)(*(uint64_t *)(local_rbp - 0x69) + 0x400)));
    goto loc_0021DFD1;
loc_0021E723:
    if (((uint8_t)(result)) != 1) goto loc_0021E768;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(1 + 0x35DC)))) == (*(uint32_t *)(*(uint64_t *)(local_rbx + 0x10) + 0x24))) goto loc_0021E6C4;
    *(uint8_t *)(1 + 0x35D9) = (uint8_t)(*(uint64_t *)(local_rbp - 0x69));
    local_r15 = (1) + (0x35E0ULL);
    result = KeAddProcessorAffinityEx(local_r15, (uint32_t)(*(uint32_t *)(1 + 0x35DC)), Arg3, (int32_t)(*(uint32_t *)(*(uint64_t *)(local_rbp - 0x69) + 0x400)));
loc_0021E749:
    result = KeAddGroupAffinityEx(local_r15, *(uint8_t *)(*(uint64_t *)(local_rbx + 0x10) + 0xD0), *(uint64_t *)(*(uint64_t *)(local_rbx + 0x10) + 0xC8), (int32_t)(*(uint32_t *)(*(uint64_t *)(local_rbp - 0x69) + 0x400)));
    goto loc_0021E6C4;
loc_0021E768:
    local_r15 = (*(uint64_t *)(local_rbp + 0x67)) + (0x35E0ULL);
    goto loc_0021E749;
loc_0021E771:
    if ((*(uint64_t *)(local_r15 + 0x8EB8)) == 0) goto loc_0021E6E8;
    if (local_r15 == (*(uint64_t *)(local_rbx + 0x10))) goto loc_0021E6E8;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result))))) & (0x40000ULL));
    if (condition_is_not_equal) goto loc_0021E80B;
loc_0021E79B:
    if (condition_is_below) goto loc_0021E7B9;
    if ((uint32_t)(result) == 0) goto loc_0021E6E8;
    if (((uint32_t)((uint8_t)((uint32_t)(*(uint32_t *)(result))))) >= ((uint32_t)(local_r15))) goto loc_0021E6E8;
loc_0021E7B9:
    *(uint32_t *)(*(uint64_t *)(local_r15 + 0x8EB8) + 0xC) = (uint32_t)(*(uint64_t *)(local_rbp - 0x69));
    result = (uint8_t)((uint32_t)(*(uint32_t *)(result)));
    local_r15 = (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rbx + 0x10) + 0x24));
    if ((*(uint8_t *)(v_rip + 0xDA6847)) == 0) {
        result = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rbx + 0x10) + 0x24)));
        Arg2 = v_rip + 14346889;
        local_r15 = *(uint8_t *)(Arg2 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rbx + 0x10) + 0x24)) * 2);
        local_r15 = (uint32_t)((local_r15) << (6));
        result = *(uint8_t *)(Arg2 + result * 2 + 0x1);
        local_r15 = (uint32_t)((local_r15) | ((uint32_t)(result)));
    }
    *(uint32_t *)(*(uint64_t *)(local_r15 + 0x8EB8) + 0x8) = (uint32_t)(local_r15);
    result = EtwTraceXSchedulerPriorityKickSend((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rbx + 0x10) + 0x24)), (uint32_t)((uint32_t)(*(uint64_t *)(local_rbp - 0x69))), (uint32_t)(*(uint32_t *)(result)), local_r15 + 36536);
loc_0021E80B:
    goto loc_0021E79B;
loc_0021E814:
    local_rdi = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbp + 0x7F))) & (0xFFFFFFFDULL));
    goto loc_0021DCA4;
loc_0021E81C:
    if ((*(uint64_t *)(*(uint64_t *)(local_rbp - 0x51) + 0x28)) != local_rdi) goto loc_0021E878;
loc_0021E82C:
    result = EtwTraceScheduleThread(*(uint64_t *)(*(uint64_t *)(local_rbp - 0x51) + 0x28), *(uint64_t *)(local_rbx + 0x10), local_rbp + 7, local_r15 + 36536);
    goto loc_0021E6CE;
loc_0021E836:
    if ((((uint8_t)(*(uint8_t *)(*(uint64_t *)(local_rbp - 0x51) + 0x20))) & (1)) != 0) goto loc_0021DE5C;
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(local_rbp - 0x69) + 0xC3))) > (*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(local_rbp - 0x51) + 0x10) + 0xC3))) goto loc_0021DE5C;
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(local_rbp - 0x69) + 0xC3))) != (*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(local_rbp - 0x51) + 0x10) + 0xC3))) goto loc_0021E865;
    if ((((uint8_t)(*(uint8_t *)(*(uint64_t *)(local_rbp - 0x51) + 0x20))) & (24)) != 0) goto loc_0021DE5C;
loc_0021E865:
    if ((((uint8_t)(*(uint8_t *)(*(uint64_t *)(local_rbp - 0x51) + 0x20))) & (16)) == 0) goto loc_0021E871;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(local_rbp - 0x69) + 0xC3)) != 0) goto loc_0021DE5C;
loc_0021E871:
    result = 0;
    goto loc_0021DE7F;
loc_0021E878:
    Arg3 = 0;
    goto loc_0021E82C;
loc_0021E87D:
    if (*(uint64_t *)(local_r15 + 0x3C8) == 0) goto loc_0021E5E1;
    Arg3 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_r15 + 0x3C8)))) & (0x200000ULL));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_r15 + 0x3C8) + 0x1C))) == 0) goto loc_0021EB3E;
loc_0021E8AA:
    Arg1 = 0;
    goto loc_0021E5E1;
loc_0021E8B1:
    *(uint32_t *)(local_rbp - 0x5D) = (uint32_t)(local_r15);
    goto loc_0021D82A;
loc_0021E8BA:
    result = (uint16_t)((*(uint16_t *)(*(uint64_t *)(local_rbp - 0x69) + 0x206)) & ((uint16_t)(Arg3)));
    local_rdi = (((uint16_t)(result)) < 0) ? 1 : 0;
    if ((*(uint64_t *)(local_rbp - 0x41)) < (*(uint64_t *)(*(uint64_t *)(local_rbp - 0x69) + 0x20))) goto loc_0021DA19;
    result = KiComputeNewPriority(*(uint64_t *)(local_rbp - 0x69), *(uint64_t *)(local_r15 + 0x3C8), 1, (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_r15 + 0x3C8) + 0x20)));
    goto loc_0021DA19;
loc_0021E8F3:
    if (((*(uint32_t *)(local_r15 + 0x78)) & (0x400000ULL)) != 0) goto loc_0021DB99;
    goto loc_0021DBBA;
loc_0021E908:
    if ((*(uint64_t *)(local_rbp - 0x69)) == 1) goto loc_0021DC5C;
    result = (result) | (1);
    result = (result) ^ (*(uint64_t *)(local_rbp - 0x69));
    goto loc_0021E12B;
loc_0021E91E:
    result = KiInswapAndReadyThread(*(uint64_t *)(local_rbp - 0x69), (uint32_t)((uint32_t)(*(uint64_t *)(local_rbp - 0x69))), 1, (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_r15 + 0x3C8) + 0x20)));
    goto loc_0021E0B9;
loc_0021E928:
    if (condition_is_below_or_equal) goto loc_0021DC59;
    goto loc_0021DC5C;
loc_0021E933:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xDA81DB)))) & (32)) == 0) goto loc_0021E611;
    v_stack_p118 = local_rbp - 41;
    result = EtwTraceXSchedulerPriorityUpdate(local_r15, 1, (uint32_t)((uint32_t)(local_r14)), (uint32_t)((uint32_t)(*(uint64_t *)(local_rbp - 0x51))));
    goto loc_0021E611;
loc_0021E962:
    if (((uint32_t)(*(uint64_t *)(local_rbp - 0x51))) == ((uint32_t)(local_r15))) goto loc_0021E485;
    goto loc_0021E485;
loc_0021E973:
loc_0021E975:
    if (((uint32_t)((uint32_t)((uint32_t)(*(uint64_t *)(local_rbx + 0x10))))) >= ((uint32_t)(*(uint8_t *)(*(uint64_t *)(local_rbp + 0x67))))) goto loc_0021DE7D;
    Arg1 = ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint64_t *)(local_rbx + 0x10))))) * 4 + 2) + ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint64_t *)(local_rbx + 0x10))))));
    Arg1 = (Arg1 * 8) + (*(uint64_t *)(local_rbp + 0x67));
    if (Arg1 == (*(uint64_t *)(local_rbp - 0x51))) goto loc_0021E9B5;
    Arg4 = 0;
    Arg3 = 0;
    result = KiDoesThreadDominateRescheduleContextEntry(Arg1, *(uint64_t *)(local_rbp - 0x69), Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0021DE7F;
loc_0021E9B5:
    local_rdi = (uint32_t)(((uint32_t)((uint32_t)(*(uint64_t *)(local_rbx + 0x10)))) + 1);
    goto loc_0021E975;
loc_0021E9B9:
    *(uint32_t *)(local_rbp - 0x5D) = (uint32_t)(local_r15);
    goto loc_0021D82A;
loc_0021E9C2:
    if ((*(uint8_t *)(*(uint64_t *)(local_rbp + 0x67))) > ((uint8_t)(*(uint64_t *)(local_rbx + 0x10)))) goto loc_0021E9F0;
loc_0021E9CB:
    if ((((uint8_t)(*(uint64_t *)(local_rbp - 0x69))) & (2)) == 0) goto loc_0021DDFB;
    *(uint32_t *)(*(uint64_t *)(local_rbp + 0x67) + 0x4) = (uint32_t)(*(uint64_t *)(local_rbx + 0x10));
    goto loc_0021DDFB;
loc_0021E9DD:
    *(uint32_t *)(local_rbp - 0x5D) = (uint32_t)(local_rdi);
    goto loc_0021E531;
loc_0021E9F0:
    result = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint64_t *)(local_rbx + 0x10)))));
    if ((*(uint64_t *)(local_rbp + 0x67) + 16 + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint64_t *)(local_rbx + 0x10))))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint64_t *)(local_rbx + 0x10))))) * 4 * 8) != 0) {
        Arg1 = *(uint64_t *)(*(uint64_t *)(local_rbp + 0x67) + 0x10 + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint64_t *)(local_rbx + 0x10))))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint64_t *)(local_rbx + 0x10))))) * 4 * 8);
        result = *(uint64_t *)(Arg1 + 0x18);
        *(uint64_t *)(*(uint64_t *)(local_rbp + 0x67) + 0x10 + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint64_t *)(local_rbx + 0x10))))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint64_t *)(local_rbx + 0x10))))) * 4 * 8 + 0x10) = result;
        result = *(uint8_t *)(*(uint64_t *)(local_rbp + 0x67) + 0x10 + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint64_t *)(local_rbx + 0x10))))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint64_t *)(local_rbx + 0x10))))) * 4 * 8 + 0x20);
        result = (uint8_t)((result) & (197));
        result = (uint8_t)((result) | (5));
        *(uint8_t *)(*(uint64_t *)(local_rbp + 0x67) + 0x10 + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint64_t *)(local_rbx + 0x10))))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint64_t *)(local_rbx + 0x10))))) * 4 * 8 + 0x20) = (uint8_t)(result);
        result = *(uint64_t *)(Arg1 + 0x18);
        *(uint64_t *)(*(uint64_t *)(local_rbp + 0x67) + 0x10 + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint64_t *)(local_rbx + 0x10))))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint64_t *)(local_rbx + 0x10))))) * 4 * 8 + 0x18) = result;
    }
    local_r10 = (uint32_t)(((uint32_t)((uint32_t)(*(uint64_t *)(local_rbx + 0x10)))) + 1);
    if (((uint32_t)(local_r10)) < ((uint32_t)(*(uint8_t *)(*(uint64_t *)(local_rbp + 0x67))))) goto loc_0021E9F0;
    goto loc_0021E9CB;
loc_0021EA3D:
    if ((*(uint64_t *)(local_r15 + 0x328)) != 1) goto loc_0021DA35;
    if (Arg1 + 37240 == 0) goto loc_0021DA35;
    *(uint64_t *)(local_r15 + 0x328) = *(uint64_t *)(Arg1 + 0x9178);
    *(uint64_t *)(Arg1 + 0x9178) = local_r15 + 808;
    result = KiAbQueueAutoBoostDpc(Arg1, Arg1 + 37240, local_r15 + 808, *(uint64_t *)(local_rbp + 0x67) + 16 + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint64_t *)(local_rbx + 0x10))))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint64_t *)(local_rbx + 0x10))))) * 4 * 8);
    goto loc_0021DA35;
loc_0021EA7E:
    if ((*(uint64_t *)(*(uint64_t *)(local_rbp - 0x69) + 0x328)) != 1) goto loc_0021DD17;
    if (Arg1 + 37240 == 0) goto loc_0021DD17;
    *(uint64_t *)(*(uint64_t *)(local_rbp - 0x69) + 0x328) = *(uint64_t *)(Arg1 + 0x9178);
    *(uint64_t *)(Arg1 + 0x9178) = *(uint64_t *)(local_rbp - 0x69) + 808;
    result = KiAbQueueAutoBoostDpc(Arg1, Arg1 + 37240, *(uint64_t *)(local_rbp - 0x69) + 808, *(uint64_t *)(local_rbp + 0x67) + 16 + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint64_t *)(local_rbx + 0x10))))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint64_t *)(local_rbx + 0x10))))) * 4 * 8);
    goto loc_0021DD17;
loc_0021EABD:
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(local_rbp - 0x69) + 0x318)) == 0) goto loc_0021DA35;
    goto loc_0021EA3D;
loc_0021EAD2:
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(local_rbp - 0x69) + 0x318)) == 0) goto loc_0021DD17;
    goto loc_0021EA7E;
loc_0021EAE5:
    goto loc_0021D8B7;
loc_0021EAEE:
    v_stack_p118 = 0;
    result = KeBugCheckEx(343, local_r15, (int8_t)((uint8_t)(local_r14)), 1);
loc_0021EB27:
    v_stack_p118 = 0;
    Arg1 = 0;
    result = KiUpdateThreadPriority(Arg1, local_r15, local_r15, (uint32_t)((uint32_t)(*(uint64_t *)(local_rbp - 0x51))));
    goto loc_0021E5CE;
loc_0021EB3E:
    if ((uint32_t)((uint32_t)((uint32_t)(*(uint64_t *)(local_rbp - 0x51)))) != 0) goto loc_0021E8AA;
    if (condition_is_below) goto loc_0021E8AA;
    if ((uint32_t)(local_r15) == 0) goto loc_0021E5E1;
    goto loc_0021E8AA;
loc_0021EB60:
    *(uint8_t *)(local_r15 + 0x204) = 0;
    goto loc_0021E5F1;
loc_0021EB6C:
    result = KiScheduleNextForegroundBoost((int8_t)((uint8_t)(local_r14)) + local_r15 * 1, local_r15, local_r15, (uint32_t)((uint32_t)(*(uint64_t *)(local_rbp - 0x51))));
    goto loc_0021DA73;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0021D7F8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
