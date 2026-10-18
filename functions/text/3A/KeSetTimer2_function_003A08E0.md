# KeSetTimer2

- RVA: `0x003A08E0`–`0x003A10CF` (길이 `2,031` bytes)
- VA: `0x00000001403A08E0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00081E2C`
- 디코드: `465`개 명령, `2,031/2,031` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **20**; 고유 호출 대상: **17**
- 직접 호출자로 확인된 함수: **44**
- RIP 상대 이미지 참조: **19**

### Outgoing calls
- `0x003A09CE` → [KiAcquireTimer2LockUnlessDisabled](KiAcquireTimer2LockUnlessDisabled_function_003A10D8.md) (function, `0x003A10D8`)
- `0x003A09DE` → [KiAcquireTimer2CollectionLockIfInserted](KiAcquireTimer2CollectionLockIfInserted_function_003A1150.md) (function, `0x003A1150`)
- `0x003A09EE` → [KiRemoveTimer2](KiRemoveTimer2_function_003A1D60.md) (function, `0x003A1D60`)
- `0x003A0A79` → [KiAcquireSpinLockInstrumented](../20/KiAcquireSpinLockInstrumented_function_002084F0.md) (function, `0x002084F0`)
- `0x003A0B2C` → [RtlGetInterruptTimePrecise](../20/RtlGetInterruptTimePrecise_function_0020A4C0.md) (function, `0x0020A4C0`)
- `0x003A0BE7` → [KxWaitForSpinLockAndAcquire](../20/KxWaitForSpinLockAndAcquire_function_002085C0.md) (function, `0x002085C0`)
- `0x003A0C45` → [RtlRbInsertNodeEx](../2E/RtlRbInsertNodeEx_function_002E4570.md) (function, `0x002E4570`)
- `0x003A0D74` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x003A0E51` → [RtlRbInsertNodeEx](../2E/RtlRbInsertNodeEx_function_002E4570.md) (function, `0x002E4570`)
- `0x003A0E89` → [KiTraceSetTimer2](KiTraceSetTimer2_function_003A1F28.md) (function, `0x003A1F28`)
- `0x003A0EA5` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x003A0ECD` → [KiUpdateTimer2Collections](KiUpdateTimer2Collections_function_003A2408.md) (function, `0x003A2408`)
- `0x003A0F19` → [PsTimerResolutionActive](PsTimerResolutionActive_function_003A3010.md) (function, `0x003A3010`)
- `0x003A0F3B` → [KiUpdateTimer2Collections](KiUpdateTimer2Collections_function_003A2408.md) (function, `0x003A2408`)
- `0x003A0F9D` → [KiRequestTimer2Expiration](../39/KiRequestTimer2Expiration_function_0039F118.md) (function, `0x0039F118`)
- `0x003A1005` → [KiReleaseSpinLockInstrumented](../39/KiReleaseSpinLockInstrumented_function_00392EF0.md) (function, `0x00392EF0`)
- `0x003A1039` → [KiReleaseSpinLockInstrumented](../39/KiReleaseSpinLockInstrumented_function_00392EF0.md) (function, `0x00392EF0`)
- `0x003A1087` → [KiSendClockInterruptToTargetProcessor](../23/KiSendClockInterruptToTargetProcessor_function_00234700.md) (function, `0x00234700`)
- `0x003A1091` → [RtlGetSystemTimePrecise](../37/RtlGetSystemTimePrecise_function_0037EDD0.md) (function, `0x0037EDD0`)
- `0x003A10C5` → [KiHvEnlightenedGuestPriorityKick](../44/KiHvEnlightenedGuestPriorityKick_function_00443880.md) (function, `0x00443880`)

### Direct callers
- [RtlpHpEnvCompactionSchedule](../32/RtlpHpEnvCompactionSchedule_function_003264A0.md) at `0x00326570`
- [SMKM_STORE_MGR&lt;SM_TRAITS&gt;::SmHighMemPriorityTimerStart](../34/SMKM_STORE_MGR_SM_TRAITS_SmHighMemPriorityTimerStart_function_0034BF50.md) at `0x0034BF9B`
- [NtSetInformationWorkerFactory](../35/NtSetInformationWorkerFactory_function_00350A30.md) at `0x00351105`
- [WdtpArmTimer](../39/WdtpArmTimer_function_0039F230.md) at `0x0039F274`
- [ExpSetTimer2](ExpSetTimer2_function_003A0470.md) at `0x003A05ED`
- [ExpSetTimerObject2](ExpSetTimerObject2_function_003A0658.md) at `0x003A06C0`
- [ExSetTimer](ExSetTimer_function_003A0800.md) at `0x003A086C`
- [MiStoreEvictThread](MiStoreEvictThread_function_003A42D0.md) at `0x003A4384`
- [EnableFlushTimer](../45/EnableFlushTimer_function_0045B5B8.md) at `0x0045B63B`
- [PpmCheckArmPeriod](../4B/PpmCheckArmPeriod_function_004B5D1C.md) at `0x004B5DCC`
- [KiProcessPendingForegroundBoosts](../4C/KiProcessPendingForegroundBoosts_function_004C5A80.md) at `0x004C5B5F`
- [PopIdleArmAoAcDozeS4Timer](../4E/PopIdleArmAoAcDozeS4Timer_function_004E03A8.md) at `0x004E045C`
- [PopThermalEventTransitionDisableDeepSleep](../4E/PopThermalEventTransitionDisableDeepSleep_function_004E1284.md) at `0x004E12EF`
- [KiInitializeIdealProcessorRebalancer](../5C/KiInitializeIdealProcessorRebalancer_function_005C1BA0.md) at `0x005C1C27`
- [KiTriggerForegroundBoostDpc](../5C/KiTriggerForegroundBoostDpc_function_005C4770.md) at `0x005C4796`
- [KiForceParkDutyCycleDpcCallback](../5C/KiForceParkDutyCycleDpcCallback_function_005C97D0.md) at `0x005C9969`
- [PopDirectedDripsStartDisengageTimer](../5D/PopDirectedDripsStartDisengageTimer_function_005D1230.md) at `0x005D12A6`
- [PopThermalUpdateTelemetryClientCount](../5D/PopThermalUpdateTelemetryClientCount_function_005D58C4.md) at `0x005D5914`
- [PopCheckPowerSourceAfterRtcWakeSet](../5D/PopCheckPowerSourceAfterRtcWakeSet_function_005D5A88.md) at `0x005D5AC0`
- [PopPowerButtonWorkCallback](../5D/PopPowerButtonWorkCallback_function_005D9A70.md) at `0x005D9BFA`
- [EtwpCoverageEnsureContext](../../page/70/EtwpCoverageEnsureContext_function_007028E4.md) at `0x00702C97`
- [PopDripsWatchdogScheduleNextTimer](../../page/70/PopDripsWatchdogScheduleNextTimer_function_00705880.md) at `0x007058C5`
- [PopPowerRequestDebounceTimerWorker](../../page/75/PopPowerRequestDebounceTimerWorker_function_00754A40.md) at `0x00754ACC`
- [PopPowerRequestSetExecutionRequiredTimeoutTimer](../../page/75/PopPowerRequestSetExecutionRequiredTimeoutTimer_function_00754C5C.md) at `0x00754CBF`
- [PpmRegisterPerfStates](../../page/75/PpmRegisterPerfStates_function_0075B084.md) at `0x0075BD48`
- [PopPowerAggregatorDozeTimerArm](../../page/76/PopPowerAggregatorDozeTimerArm_function_007643BC.md) at `0x00764465`
- [PopPowerAggregatorSessionSwitchWorker](../../page/76/PopPowerAggregatorSessionSwitchWorker_function_00764FB0.md) at `0x0076504A`
- [PopDispatchShutdownEvent](../../page/76/PopDispatchShutdownEvent_function_00765C60.md) at `0x00765CB4`
- [PopNetArmRefreshTimer](../../page/76/PopNetArmRefreshTimer_function_007689D0.md) at `0x007689FF`
- [PopNetResiliencyPhaseStateChanged](../../page/76/PopNetResiliencyPhaseStateChanged_function_00768DD8.md) at `0x00768E44`
- [PopAdaptiveStandbySetPolicyTimer](../../page/76/PopAdaptiveStandbySetPolicyTimer_function_0076EF18.md) at `0x0076EF65`
- [SshpAlpcCloseTraceSession](../../page/77/SshpAlpcCloseTraceSession_function_00774DE8.md) at `0x00774E58`
- [ExStartStopWorkQueueProvider](../../page/7C/ExStartStopWorkQueueProvider_function_007CF59C.md) at `0x007CF737`
- [EtwpCoverageRecord](../../page/98/EtwpCoverageRecord_function_009821BC.md) at `0x009823F2`
- [NtCreateWorkerFactory](../../page/9A/NtCreateWorkerFactory_function_009A7E10.md) at `0x009A811F`
- [PopThermalWorker](../../page/A4/PopThermalWorker_function_00A4E200.md) at `0x00A4E341`
- [EtwpEnableKernelTrace](../../page/A4/EtwpEnableKernelTrace_function_00A4FBCC.md) at `0x00A4FFCA`
- [PopPowerRequestHandleRequestUpdate](../../page/A6/PopPowerRequestHandleRequestUpdate_function_00A652D8.md) at `0x00A6540F`
- [PopSleepstudyStartNextSession](../../page/AC/PopSleepstudyStartNextSession_function_00AC4720.md) at `0x00AC4B24`
- [ExpWorkQueueManagerThread](../../page/AF/ExpWorkQueueManagerThread_function_00AF6D60.md) at `0x00AF6E4E`
- [ExpTimeRefreshWork](../../pagelk/B7/ExpTimeRefreshWork_function_00B72A80.md) at `0x00B72AEF`
- [HalpBlkInitSystem](../../init/C2/HalpBlkInitSystem_function_00C24B98.md) at `0x00C24BE9`
- [KiInitializeDpcRuntimeHistoryHashTables](../../init/C3/KiInitializeDpcRuntimeHistoryHashTables_function_00C3A398.md) at `0x00C3A436`
- [ExInitializeTimeRefresh](../../init/C5/ExInitializeTimeRefresh_function_00C51090.md) at `0x00C51179`

### Static image references
- `0x003A0933` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x003A09F3` → RVA `0x00FC6B06` (`ALMOSTRO`; reference)
- `0x003A0A00` → RVA `0x00FCF600` (`CACHEALI`; read/write)
- `0x003A0A2E` → RVA `0x00FC6C48` (`ALMOSTRO`; read)
- `0x003A0A47` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x003A0A57` → RVA `0x00FC6B06` (`ALMOSTRO`; read)
- `0x003A0A64` → RVA `0x00F0DE58` (`.data`; read)
- `0x003A0A72` → RVA `0x00FCF600` (`CACHEALI`; read)
- `0x003A0C93` → RVA `0x00FC6B08` (`ALMOSTRO`; read)
- `0x003A0D01` → RVA `0x00FC6FF0` (`ALMOSTRO`; read)
- `0x003A0D0A` → RVA `0x00F233CC` (`.data`; read)
- `0x003A0D35` → RVA `0x00FC6AA0` (`ALMOSTRO`; read)
- `0x003A0D43` → RVA `0x00F21F90` (`.data`; read)
- `0x003A0DA3` → RVA `0x00F23300` (`.data`; read)
- `0x003A0DAC` → RVA `0x00F23300` (`.data`; write)
- `0x003A0DD5` → RVA `0x00F232F8` (`.data`; read/write)
- `0x003A0DEE` → RVA `0x00F21FB0` (`.data`; read)
- `0x003A0FBF` → RVA `0x00FC6B3C` (`ALMOSTRO`; read)
- `0x003A10B6` → RVA `0x00FC504C` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003A08E0  40 53                           push rbx
003A08E2  55                              push rbp
003A08E3  56                              push rsi
003A08E4  57                              push rdi
003A08E5  41 54                           push r12
003A08E7  41 55                           push r13
003A08E9  41 56                           push r14
003A08EB  41 57                           push r15
003A08ED  48 83 EC 38                     sub rsp, 0x38
003A08F1  45 33 E4                        xor r12d, r12d
003A08F4  49 8B E9                        mov rbp, r9
003A08F7  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
003A08FC  4D 8B F0                        mov r14, r8
003A08FF  48 8B F2                        mov rsi, rdx
003A0902  48 8B D9                        mov rbx, rcx
003A0905  4D 85 C0                        test r8, r8
003A0908  0F 85 B1 06 00 00               jne 0x1403a0fbf
003A090E  44 0F B6 81 81 00 00 00         movzx r8d, byte ptr [rcx + 0x81]
003A0916  44 88 84 24 80 00 00 00         mov byte ptr [rsp + 0x80], r8b
003A091E  44 0F 20 C0                     mov rax, cr8
003A0922  48 89 84 24 98 00 00 00         mov qword ptr [rsp + 0x98], rax
003A092A  B9 02 00 00 00                  mov ecx, 2
003A092F  44 0F 22 C1                     mov cr8, rcx
003A0933  44 39 25 E6 63 C2 00            cmp dword ptr [rip + 0xc263e6], r12d
003A093A  0F 85 5F 05 00 00               jne 0x1403a0e9f
003A0940  45 32 FF                        xor r15b, r15b
003A0943  48 85 F6                        test rsi, rsi
003A0946  0F 8F 0C 06 00 00               jg 0x1403a0f58
003A094C  48 B8 08 00 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000008
003A0956  41 F6 C0 04                     test r8b, 4
003A095A  0F 85 C7 01 00 00               jne 0x1403a0b27
003A0960  48 8B 00                        mov rax, qword ptr [rax]
003A0963  48 8B F8                        mov rdi, rax
003A0966  48 2B FE                        sub rdi, rsi
003A0969  48 3B F8                        cmp rdi, rax
003A096C  0F 82 A9 01 00 00               jb 0x1403a0b1b
003A0972  48 83 FF FF                     cmp rdi, -1
003A0976  0F 84 9F 01 00 00               je 0x1403a0b1b
003A097C  48 8B F7                        mov rsi, rdi
003A097F  48 85 ED                        test rbp, rbp
003A0982  74 2E                           je 0x1403a09b2
003A0984  80 BB 82 00 00 00 17            cmp byte ptr [rbx + 0x82], 0x17
003A098B  74 25                           je 0x1403a09b2
003A098D  48 8B 45 08                     mov rax, qword ptr [rbp + 8]
003A0991  48 83 F8 FF                     cmp rax, -1
003A0995  0F 84 7D 04 00 00               je 0x1403a0e18
003A099B  48 8D 34 38                     lea rsi, [rax + rdi]
003A099F  48 3B F7                        cmp rsi, rdi
003A09A2  0F 82 EB 04 00 00               jb 0x1403a0e93
003A09A8  48 83 FE FF                     cmp rsi, -1
003A09AC  0F 84 E1 04 00 00               je 0x1403a0e93
003A09B2  41 BD 01 00 00 00               mov r13d, 1
003A09B8  44 88 A4 24 88 00 00 00         mov byte ptr [rsp + 0x88], r12b
003A09C0  48 8B CB                        mov rcx, rbx
003A09C3  44 89 AC 24 90 00 00 00         mov dword ptr [rsp + 0x90], r13d
003A09CB  41 8B ED                        mov ebp, r13d
003A09CE  E8 05 07 00 00                  call 0x1403a10d8
003A09D3  84 C0                           test al, al
003A09D5  0F 85 BB 03 00 00               jne 0x1403a0d96
003A09DB  48 8B CB                        mov rcx, rbx
003A09DE  E8 6D 07 00 00                  call 0x1403a1150
003A09E3  84 C0                           test al, al
003A09E5  0F 84 06 02 00 00               je 0x1403a0bf1
003A09EB  48 8B CB                        mov rcx, rbx
003A09EE  E8 6D 13 00 00                  call 0x1403a1d60
003A09F3  40 84 2D 0C 61 C2 00            test byte ptr [rip + 0xc2610c], bpl
003A09FA  0F 85 1F 06 00 00               jne 0x1403a101f
003A0A00  F0 4C 21 25 F8 EB C2 00         lock and qword ptr [rip + 0xc2ebf8], r12
003A0A08  40 88 AC 24 88 00 00 00         mov byte ptr [rsp + 0x88], bpl
003A0A10  44 89 63 04                     mov dword ptr [rbx + 4], r12d
003A0A14  48 89 7B 48                     mov qword ptr [rbx + 0x48], rdi
003A0A18  48 89 73 50                     mov qword ptr [rbx + 0x50], rsi
003A0A1C  0F B6 93 81 00 00 00            movzx edx, byte ptr [rbx + 0x81]
003A0A23  4C 89 73 58                     mov qword ptr [rbx + 0x58], r14
003A0A27  44 88 BB 80 00 00 00            mov byte ptr [rbx + 0x80], r15b
003A0A2E  44 39 25 13 62 C2 00            cmp dword ptr [rip + 0xc26213], r12d
003A0A35  0F 85 7D 04 00 00               jne 0x1403a0eb8
003A0A3B  F6 C2 2E                        test dl, 0x2e
003A0A3E  0F 84 BD 04 00 00               je 0x1403a0f01
003A0A44  45 32 FF                        xor r15b, r15b
003A0A47  48 8D 15 B2 F5 C5 FF            lea rdx, [rip - 0x3a0a4e]
003A0A4E  41 3B ED                        cmp ebp, r13d
003A0A51  0F 85 B8 05 00 00               jne 0x1403a100f
003A0A57  F6 05 A8 60 C2 00 21            test byte ptr [rip + 0xc260a8], 0x21
003A0A5E  0F 84 6C 01 00 00               je 0x1403a0bd0
003A0A64  8B 05 EE D3 B6 00               mov eax, dword ptr [rip + 0xb6d3ee]
003A0A6A  85 C0                           test eax, eax
003A0A6C  0F 85 5E 01 00 00               jne 0x1403a0bd0
003A0A72  48 8D 0D 87 EB C2 00            lea rcx, [rip + 0xc2eb87]
003A0A79  E8 72 7A E6 FF                  call 0x1402084f0
003A0A7E  48 8D 15 7B F5 C5 FF            lea rdx, [rip - 0x3a0a85]
003A0A85  0F B6 8B 82 00 00 00            movzx ecx, byte ptr [rbx + 0x82]
003A0A8C  45 32 F6                        xor r14b, r14b
003A0A8F  41 8B F4                        mov esi, r12d
003A0A92  80 F9 17                        cmp cl, 0x17
003A0A95  0F 84 A9 00 00 00               je 0x1403a0b44
003A0A9B  F6 C1 20                        test cl, 0x20
003A0A9E  0F 85 92 00 00 00               jne 0x1403a0b36
003A0AA4  0F B6 C1                        movzx eax, cl
003A0AA7  48 8D 6B 18                     lea rbp, [rbx + 0x18]
003A0AAB  83 E1 07                        and ecx, 7
003A0AAE  24 EF                           and al, 0xef
003A0AB0  88 83 82 00 00 00               mov byte ptr [rbx + 0x82], al
003A0AB6  48 8D 04 49                     lea rax, [rcx + rcx*2]
003A0ABA  48 8D 34 C5 20 33 F2 00         lea rsi, [rax*8 + 0xf23320]
003A0AC2  48 03 F2                        add rsi, rdx
003A0AC5  48 8B 4E 08                     mov rcx, qword ptr [rsi + 8]
003A0AC9  48 8B 16                        mov rdx, qword ptr [rsi]
003A0ACC  41 84 CD                        test r13b, cl
003A0ACF  0F 85 09 05 00 00               jne 0x1403a0fde
003A0AD5  41 23 CD                        and ecx, r13d
003A0AD8  45 32 C0                        xor r8b, r8b
003A0ADB  48 85 D2                        test rdx, rdx
003A0ADE  0F 84 67 03 00 00               je 0x1403a0e4b
003A0AE4  4C 8B 43 48                     mov r8, qword ptr [rbx + 0x48]
003A0AE8  0F 1F 84 00 00 00 00 00         nop dword ptr [rax + rax]
003A0AF0  4C 3B 42 30                     cmp r8, qword ptr [rdx + 0x30]
003A0AF4  0F 83 38 03 00 00               jae 0x1403a0e32
003A0AFA  48 8B 02                        mov rax, qword ptr [rdx]
003A0AFD  85 C9                           test ecx, ecx
003A0AFF  74 0C                           je 0x1403a0b0d
003A0B01  48 85 C0                        test rax, rax
003A0B04  0F 84 D9 04 00 00               je 0x1403a0fe3
003A0B0A  48 33 C2                        xor rax, rdx
003A0B0D  48 85 C0                        test rax, rax
003A0B10  0F 84 CD 04 00 00               je 0x1403a0fe3
003A0B16  48 8B D0                        mov rdx, rax
003A0B19  EB D5                           jmp 0x1403a0af0
003A0B1B  48 C7 C7 FE FF FF FF            mov rdi, 0xfffffffffffffffe
003A0B22  E9 55 FE FF FF                  jmp 0x1403a097c
003A0B27  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
003A0B2C  E8 8F 99 E6 FF                  call 0x14020a4c0
003A0B31  E9 2D FE FF FF                  jmp 0x1403a0963
003A0B36  48 8B 43 50                     mov rax, qword ptr [rbx + 0x50]
003A0B3A  48 39 43 48                     cmp qword ptr [rbx + 0x48], rax
003A0B3E  0F 85 60 FF FF FF               jne 0x1403a0aa4
003A0B44  80 C9 10                        or cl, 0x10
003A0B47  88 8B 82 00 00 00               mov byte ptr [rbx + 0x82], cl
003A0B4D  48 83 7B 50 FF                  cmp qword ptr [rbx + 0x50], -1
003A0B52  0F B6 8B 83 00 00 00            movzx ecx, byte ptr [rbx + 0x83]
003A0B59  0F 84 C5 02 00 00               je 0x1403a0e24
003A0B5F  0F B6 C1                        movzx eax, cl
003A0B62  48 8D 6B 30                     lea rbp, [rbx + 0x30]
003A0B66  24 EF                           and al, 0xef
003A0B68  80 E1 07                        and cl, 7
003A0B6B  88 83 83 00 00 00               mov byte ptr [rbx + 0x83], al
003A0B71  0F B6 C1                        movzx eax, cl
003A0B74  48 8D 0C 40                     lea rcx, [rax + rax*2]
003A0B78  48 8D 05 81 F4 C5 FF            lea rax, [rip - 0x3a0b7f]
003A0B7F  4C 8D B0 20 33 F2 00            lea r14, [rax + 0xf23320]
003A0B86  4D 8B 4C CE 08                  mov r9, qword ptr [r14 + rcx*8 + 8]
003A0B8B  4D 8D 34 CE                     lea r14, [r14 + rcx*8]
003A0B8F  49 8B 16                        mov rdx, qword ptr [r14]
003A0B92  45 84 CD                        test r13b, r9b
003A0B95  0F 85 36 04 00 00               jne 0x1403a0fd1
003A0B9B  45 23 CD                        and r9d, r13d
003A0B9E  45 32 C0                        xor r8b, r8b
003A0BA1  48 85 D2                        test rdx, rdx
003A0BA4  0F 84 95 00 00 00               je 0x1403a0c3f
003A0BAA  48 8B 4B 50                     mov rcx, qword ptr [rbx + 0x50]
003A0BAE  66 90                           nop
003A0BB0  48 3B 4A 20                     cmp rcx, qword ptr [rdx + 0x20]
003A0BB4  73 6F                           jae 0x1403a0c25
003A0BB6  48 8B 02                        mov rax, qword ptr [rdx]
003A0BB9  45 85 C9                        test r9d, r9d
003A0BBC  74 08                           je 0x1403a0bc6
003A0BBE  48 85 C0                        test rax, rax
003A0BC1  74 7C                           je 0x1403a0c3f
003A0BC3  48 33 C2                        xor rax, rdx
003A0BC6  48 85 C0                        test rax, rax
003A0BC9  74 74                           je 0x1403a0c3f
003A0BCB  48 8B D0                        mov rdx, rax
003A0BCE  EB E0                           jmp 0x1403a0bb0
003A0BD0  F0 48 0F BA 2D 26 EA C2 00 00   lock bts qword ptr [rip + 0xc2ea26], 0
003A0BDA  0F 83 A5 FE FF FF               jae 0x1403a0a85
003A0BE0  48 8D 0D 19 EA C2 00            lea rcx, [rip + 0xc2ea19]
003A0BE7  E8 D4 79 E6 FF                  call 0x1402085c0
003A0BEC  E9 8D FE FF FF                  jmp 0x1403a0a7e
003A0BF1  0F B6 43 01                     movzx eax, byte ptr [rbx + 1]
003A0BF5  A8 0F                           test al, 0xf
003A0BF7  0F 84 13 FE FF FF               je 0x1403a0a10
003A0BFD  A8 04                           test al, 4
003A0BFF  BD 08 00 00 00                  mov ebp, 8
003A0C04  8B 84 24 88 00 00 00            mov eax, dword ptr [rsp + 0x88]
003A0C0B  0F B6 C0                        movzx eax, al
003A0C0E  41 0F 44 C5                     cmove eax, r13d
003A0C12  89 AC 24 90 00 00 00            mov dword ptr [rsp + 0x90], ebp
003A0C19  89 84 24 88 00 00 00            mov dword ptr [rsp + 0x88], eax
003A0C20  E9 EB FD FF FF                  jmp 0x1403a0a10
003A0C25  48 8B 42 08                     mov rax, qword ptr [rdx + 8]
003A0C29  45 85 C9                        test r9d, r9d
003A0C2C  0F 84 A8 02 00 00               je 0x1403a0eda
003A0C32  48 85 C0                        test rax, rax
003A0C35  0F 85 9C 02 00 00               jne 0x1403a0ed7
003A0C3B  45 0F B6 C5                     movzx r8d, r13b
003A0C3F  4C 8B CD                        mov r9, rbp
003A0C42  49 8B CE                        mov rcx, r14
003A0C45  E8 26 39 F4 FF                  call 0x1402e4570
003A0C4A  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
003A0C4E  41 84 C5                        test r13b, al
003A0C51  0F 85 EE 02 00 00               jne 0x1403a0f45
003A0C57  48 8B C8                        mov rcx, rax
003A0C5A  48 3B CD                        cmp rcx, rbp
003A0C5D  75 0B                           jne 0x1403a0c6a
003A0C5F  48 8B 43 50                     mov rax, qword ptr [rbx + 0x50]
003A0C63  45 8B E5                        mov r12d, r13d
003A0C66  49 89 46 10                     mov qword ptr [r14 + 0x10], rax
003A0C6A  41 0B F4                        or esi, r12d
003A0C6D  45 32 F6                        xor r14b, r14b
003A0C70  85 F6                           test esi, esi
003A0C72  0F 85 27 01 00 00               jne 0x1403a0d9f
003A0C78  F6 83 81 00 00 00 04            test byte ptr [rbx + 0x81], 4
003A0C7F  0F 85 50 01 00 00               jne 0x1403a0dd5
003A0C85  8B AC 24 90 00 00 00            mov ebp, dword ptr [rsp + 0x90]
003A0C8C  4C 8D 25 6D F3 C5 FF            lea r12, [rip - 0x3a0c93]
003A0C93  F7 05 6B 5E C2 00 00 00 02 00   test dword ptr [rip + 0xc25e6b], 0x20000
003A0C9D  44 8B C5                        mov r8d, ebp
003A0CA0  0F 85 D5 01 00 00               jne 0x1403a0e7b
003A0CA6  8B 13                           mov edx, dword ptr [rbx]
003A0CA8  8B CA                           mov ecx, edx
003A0CAA  81 E1 7F F0 FF FF               and ecx, 0xfffff07f
003A0CB0  41 C1 E0 08                     shl r8d, 8
003A0CB4  41 0B C8                        or ecx, r8d
003A0CB7  8B C2                           mov eax, edx
003A0CB9  F0 0F B1 0B                     lock cmpxchg dword ptr [rbx], ecx
003A0CBD  3B D0                           cmp edx, eax
003A0CBF  74 15                           je 0x1403a0cd6
003A0CC1  8B C8                           mov ecx, eax
003A0CC3  8B D0                           mov edx, eax
003A0CC5  81 E1 7F F0 FF FF               and ecx, 0xfffff07f
003A0CCB  41 0B C8                        or ecx, r8d
003A0CCE  F0 0F B1 0B                     lock cmpxchg dword ptr [rbx], ecx
003A0CD2  3B D0                           cmp edx, eax
003A0CD4  75 EB                           jne 0x1403a0cc1
003A0CD6  83 FD 01                        cmp ebp, 1
003A0CD9  75 16                           jne 0x1403a0cf1
003A0CDB  40 84 2D 24 5E C2 00            test byte ptr [rip + 0xc25e24], bpl
003A0CE2  0F 85 03 03 00 00               jne 0x1403a0feb
003A0CE8  F0 48 83 25 0F E9 C2 00 00      lock and qword ptr [rip + 0xc2e90f], 0
003A0CF1  8B B4 24 88 00 00 00            mov esi, dword ptr [rsp + 0x88]
003A0CF8  45 84 FF                        test r15b, r15b
003A0CFB  0F 85 A6 03 00 00               jne 0x1403a10a7
003A0D01  83 3D E8 62 C2 00 00            cmp dword ptr [rip + 0xc262e8], 0
003A0D08  75 0B                           jne 0x1403a0d15
003A0D0A  8B 05 BC 26 B8 00               mov eax, dword ptr [rip + 0xb826bc]
003A0D10  83 F8 04                        cmp eax, 4
003A0D13  74 47                           je 0x1403a0d5c
003A0D15  45 84 F6                        test r14b, r14b
003A0D18  0F 85 7F 02 00 00               jne 0x1403a0f9d
003A0D1E  F6 84 24 80 00 00 00 04         test byte ptr [rsp + 0x80], 4
003A0D26  74 34                           je 0x1403a0d5c
003A0D28  48 B8 08 00 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000008
003A0D32  48 8B 00                        mov rax, qword ptr [rax]
003A0D35  8B 0D 65 5D C2 00               mov ecx, dword ptr [rip + 0xc25d65]
003A0D3B  48 03 C8                        add rcx, rax
003A0D3E  48 3B F9                        cmp rdi, rcx
003A0D41  73 19                           jae 0x1403a0d5c
003A0D43  48 8B 0D 46 12 B8 00            mov rcx, qword ptr [rip + 0xb81246]
003A0D4A  48 85 C9                        test rcx, rcx
003A0D4D  0F 84 2E 03 00 00               je 0x1403a1081
003A0D53  48 3B F9                        cmp rdi, rcx
003A0D56  0F 82 13 03 00 00               jb 0x1403a106f
003A0D5C  83 3D BD 5F C2 00 00            cmp dword ptr [rip + 0xc25fbd], 0
003A0D63  48 8B 9C 24 98 00 00 00         mov rbx, qword ptr [rsp + 0x98]
003A0D6B  74 0C                           je 0x1403a0d79
003A0D6D  44 0F 20 C1                     mov rcx, cr8
003A0D71  0F B6 D3                        movzx edx, bl
003A0D74  E8 1F 49 15 00                  call 0x1404f5698
003A0D79  0F B6 CB                        movzx ecx, bl
003A0D7C  44 0F 22 C1                     mov cr8, rcx
003A0D80  40 0F B6 C6                     movzx eax, sil
003A0D84  48 83 C4 38                     add rsp, 0x38
003A0D88  41 5F                           pop r15
003A0D8A  41 5E                           pop r14
003A0D8C  41 5D                           pop r13
003A0D8E  41 5C                           pop r12
003A0D90  5F                              pop rdi
003A0D91  5E                              pop rsi
003A0D92  5D                              pop rbp
003A0D93  5B                              pop rbx
003A0D94  C3                              ret
003A0D95  CC                              int3
003A0D96  8B B4 24 88 00 00 00            mov esi, dword ptr [rsp + 0x88]
003A0D9D  EB BD                           jmp 0x1403a0d5c
003A0D9F  48 8B 43 48                     mov rax, qword ptr [rbx + 0x48]
003A0DA3  48 39 05 56 25 B8 00            cmp qword ptr [rip + 0xb82556], rax
003A0DAA  76 0C                           jbe 0x1403a0db8
003A0DAC  48 89 05 4D 25 B8 00            mov qword ptr [rip + 0xb8254d], rax
003A0DB3  F0 83 0C 24 00                  lock or dword ptr [rsp], 0
003A0DB8  48 A1 08 00 00 00 80 F7 FF FF   movabs rax, qword ptr [0xfffff78000000008]
003A0DC2  48 39 43 48                     cmp qword ptr [rbx + 0x48], rax
003A0DC6  0F 87 AC FE FF FF               ja 0x1403a0c78
003A0DCC  45 0F B6 F5                     movzx r14d, r13b
003A0DD0  E9 A3 FE FF FF                  jmp 0x1403a0c78
003A0DD5  F0 44 0F C1 2D 1A 25 B8 00      lock xadd dword ptr [rip + 0xb8251a], r13d
003A0DDE  41 FF C5                        inc r13d
003A0DE1  4C 8D 25 18 F2 C5 FF            lea r12, [rip - 0x3a0de8]
003A0DE8  41 83 FD 01                     cmp r13d, 1
003A0DEC  75 1E                           jne 0x1403a0e0c
003A0DEE  8B 05 BC 11 B8 00               mov eax, dword ptr [rip + 0xb811bc]
003A0DF4  49 8B 84 C4 40 8C FC 00         mov rax, qword ptr [r12 + rax*8 + 0xfc8c40]
003A0DFC  48 8B 90 B8 8E 00 00            mov rdx, qword ptr [rax + 0x8eb8]
003A0E03  48 85 D2                        test rdx, rdx
003A0E06  0F 85 3F 02 00 00               jne 0x1403a104b
003A0E0C  8B AC 24 90 00 00 00            mov ebp, dword ptr [rsp + 0x90]
003A0E13  E9 7B FE FF FF                  jmp 0x1403a0c93
003A0E18  48 C7 C6 FF FF FF FF            mov rsi, 0xffffffffffffffff
003A0E1F  E9 8E FB FF FF                  jmp 0x1403a09b2
003A0E24  80 C9 10                        or cl, 0x10
003A0E27  88 8B 83 00 00 00               mov byte ptr [rbx + 0x83], cl
003A0E2D  E9 3E FE FF FF                  jmp 0x1403a0c70
003A0E32  48 8B 42 08                     mov rax, qword ptr [rdx + 8]
003A0E36  85 C9                           test ecx, ecx
003A0E38  0F 84 B5 00 00 00               je 0x1403a0ef3
003A0E3E  48 85 C0                        test rax, rax
003A0E41  0F 85 A9 00 00 00               jne 0x1403a0ef0
003A0E47  45 0F B6 C5                     movzx r8d, r13b
003A0E4B  4C 8B CD                        mov r9, rbp
003A0E4E  48 8B CE                        mov rcx, rsi
003A0E51  E8 1A 37 F4 FF                  call 0x1402e4570
003A0E56  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
003A0E5A  41 84 C5                        test r13b, al
003A0E5D  0F 85 27 01 00 00               jne 0x1403a0f8a
003A0E63  48 8B C8                        mov rcx, rax
003A0E66  48 3B CD                        cmp rcx, rbp
003A0E69  75 7D                           jne 0x1403a0ee8
003A0E6B  48 8B 43 48                     mov rax, qword ptr [rbx + 0x48]
003A0E6F  48 89 46 10                     mov qword ptr [rsi + 0x10], rax
003A0E73  41 8B F5                        mov esi, r13d
003A0E76  E9 D2 FC FF FF                  jmp 0x1403a0b4d
003A0E7B  8B B4 24 88 00 00 00            mov esi, dword ptr [rsp + 0x88]
003A0E82  48 8B CB                        mov rcx, rbx
003A0E85  40 0F B6 D6                     movzx edx, sil
003A0E89  E8 9A 10 00 00                  call 0x1403a1f28
003A0E8E  E9 65 FE FF FF                  jmp 0x1403a0cf8
003A0E93  48 C7 C6 FE FF FF FF            mov rsi, 0xfffffffffffffffe
003A0E9A  E9 13 FB FF FF                  jmp 0x1403a09b2
003A0E9F  0F B6 D1                        movzx edx, cl
003A0EA2  0F B6 C8                        movzx ecx, al
003A0EA5  E8 52 48 15 00                  call 0x1404f56fc
003A0EAA  44 0F B6 84 24 80 00 00 00      movzx r8d, byte ptr [rsp + 0x80]
003A0EB3  E9 88 FA FF FF                  jmp 0x1403a0940
003A0EB8  F6 C2 10                        test dl, 0x10
003A0EBB  0F 85 83 FB FF FF               jne 0x1403a0a44
003A0EC1  80 CA 10                        or dl, 0x10
003A0EC4  48 8B CB                        mov rcx, rbx
003A0EC7  88 93 81 00 00 00               mov byte ptr [rbx + 0x81], dl
003A0ECD  E8 36 15 00 00                  call 0x1403a2408
003A0ED2  E9 6D FB FF FF                  jmp 0x1403a0a44
003A0ED7  48 33 C2                        xor rax, rdx
003A0EDA  48 85 C0                        test rax, rax
003A0EDD  0F 85 E8 FC FF FF               jne 0x1403a0bcb
003A0EE3  E9 53 FD FF FF                  jmp 0x1403a0c3b
003A0EE8  41 8B F4                        mov esi, r12d
003A0EEB  E9 5D FC FF FF                  jmp 0x1403a0b4d
003A0EF0  48 33 C2                        xor rax, rdx
003A0EF3  48 85 C0                        test rax, rax
003A0EF6  0F 85 1A FC FF FF               jne 0x1403a0b16
003A0EFC  E9 46 FF FF FF                  jmp 0x1403a0e47
003A0F01  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
003A0F0A  44 0F B6 C2                     movzx r8d, dl
003A0F0E  41 80 E0 10                     and r8b, 0x10
003A0F12  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
003A0F19  E8 F2 20 00 00                  call 0x1403a3010
003A0F1E  84 C0                           test al, al
003A0F20  0F 85 89 00 00 00               jne 0x1403a0faf
003A0F26  45 84 C0                        test r8b, r8b
003A0F29  0F 84 15 FB FF FF               je 0x1403a0a44
003A0F2F  80 E2 EF                        and dl, 0xef
003A0F32  48 8B CB                        mov rcx, rbx
003A0F35  88 93 81 00 00 00               mov byte ptr [rbx + 0x81], dl
003A0F3B  E8 C8 14 00 00                  call 0x1403a2408
003A0F40  E9 FF FA FF FF                  jmp 0x1403a0a44
003A0F45  49 3B C5                        cmp rax, r13
003A0F48  74 5D                           je 0x1403a0fa7
003A0F4A  49 8B CE                        mov rcx, r14
003A0F4D  49 0B CD                        or rcx, r13
003A0F50  48 33 C8                        xor rcx, rax
003A0F53  E9 02 FD FF FF                  jmp 0x1403a0c5a
003A0F58  41 B7 01                        mov r15b, 1
003A0F5B  41 F6 C0 04                     test r8b, 4
003A0F5F  0F 85 2C 01 00 00               jne 0x1403a1091
003A0F65  48 BA 14 00 00 00 80 F7 FF FF   movabs rdx, 0xfffff78000000014
003A0F6F  48 8B 12                        mov rdx, qword ptr [rdx]
003A0F72  48 8B CA                        mov rcx, rdx
003A0F75  49 8B C4                        mov rax, r12
003A0F78  48 2B CE                        sub rcx, rsi
003A0F7B  48 3B F2                        cmp rsi, rdx
003A0F7E  48 0F 4F C1                     cmovg rax, rcx
003A0F82  48 8B F0                        mov rsi, rax
003A0F85  E9 C2 F9 FF FF                  jmp 0x1403a094c
003A0F8A  49 3B C5                        cmp rax, r13
003A0F8D  74 28                           je 0x1403a0fb7
003A0F8F  48 8B CE                        mov rcx, rsi
003A0F92  49 0B CD                        or rcx, r13
003A0F95  48 33 C8                        xor rcx, rax
003A0F98  E9 C9 FE FF FF                  jmp 0x1403a0e66
003A0F9D  E8 76 E1 FF FF                  call 0x14039f118
003A0FA2  E9 B5 FD FF FF                  jmp 0x1403a0d5c
003A0FA7  49 8B CC                        mov rcx, r12
003A0FAA  E9 AB FC FF FF                  jmp 0x1403a0c5a
003A0FAF  45 84 C0                        test r8b, r8b
003A0FB2  E9 04 FF FF FF                  jmp 0x1403a0ebb
003A0FB7  49 8B CC                        mov rcx, r12
003A0FBA  E9 A7 FE FF FF                  jmp 0x1403a0e66
003A0FBF  8B 05 77 5B C2 00               mov eax, dword ptr [rip + 0xc25b77]
003A0FC5  4C 3B F0                        cmp r14, rax
003A0FC8  4C 0F 4C F0                     cmovl r14, rax
003A0FCC  E9 3D F9 FF FF                  jmp 0x1403a090e
003A0FD1  48 85 D2                        test rdx, rdx
003A0FD4  74 41                           je 0x1403a1017
003A0FD6  49 33 D6                        xor rdx, r14
003A0FD9  E9 BD FB FF FF                  jmp 0x1403a0b9b
003A0FDE  48 85 D2                        test rdx, rdx
003A0FE1  75 60                           jne 0x1403a1043
003A0FE3  45 32 C0                        xor r8b, r8b
003A0FE6  E9 60 FE FF FF                  jmp 0x1403a0e4b
003A0FEB  8B 05 67 CE B6 00               mov eax, dword ptr [rip + 0xb6ce67]
003A0FF1  85 C0                           test eax, eax
003A0FF3  0F 85 EF FC FF FF               jne 0x1403a0ce8
003A0FF9  48 8B 54 24 78                  mov rdx, qword ptr [rsp + 0x78]
003A0FFE  48 8D 0D FB E5 C2 00            lea rcx, [rip + 0xc2e5fb]
003A1005  E8 E6 1E FF FF                  call 0x140392ef0
003A100A  E9 E2 FC FF FF                  jmp 0x1403a0cf1
003A100F  45 32 F6                        xor r14b, r14b
003A1012  E9 75 FC FF FF                  jmp 0x1403a0c8c
003A1017  45 32 C0                        xor r8b, r8b
003A101A  E9 20 FC FF FF                  jmp 0x1403a0c3f
003A101F  8B 05 33 CE B6 00               mov eax, dword ptr [rip + 0xb6ce33]
003A1025  85 C0                           test eax, eax
003A1027  0F 85 D3 F9 FF FF               jne 0x1403a0a00
003A102D  48 8B 54 24 78                  mov rdx, qword ptr [rsp + 0x78]
003A1032  48 8D 0D C7 E5 C2 00            lea rcx, [rip + 0xc2e5c7]
003A1039  E8 B2 1E FF FF                  call 0x140392ef0
003A103E  E9 C5 F9 FF FF                  jmp 0x1403a0a08
003A1043  48 33 D6                        xor rdx, rsi
003A1046  E9 8A FA FF FF                  jmp 0x1403a0ad5
003A104B  0F 0D 0A                        prefetchw byte ptr [rdx]
003A104E  8B 02                           mov eax, dword ptr [rdx]
003A1050  8B C8                           mov ecx, eax
003A1052  0F BA E9 13                     bts ecx, 0x13
003A1056  F0 0F B1 0A                     lock cmpxchg dword ptr [rdx], ecx
003A105A  75 F4                           jne 0x1403a1050
003A105C  44 8B F8                        mov r15d, eax
003A105F  41 C1 EF 13                     shr r15d, 0x13
003A1063  41 F6 D7                        not r15b
003A1066  41 80 E7 01                     and r15b, 1
003A106A  E9 9D FD FF FF                  jmp 0x1403a0e0c
003A106F  8B 05 C7 5A C2 00               mov eax, dword ptr [rip + 0xc25ac7]
003A1075  48 2B CF                        sub rcx, rdi
003A1078  48 3B C8                        cmp rcx, rax
003A107B  0F 86 DB FC FF FF               jbe 0x1403a0d5c
003A1081  8B 0D 29 0F B8 00               mov ecx, dword ptr [rip + 0xb80f29]
003A1087  E8 74 36 E9 FF                  call 0x140234700
003A108C  E9 CB FC FF FF                  jmp 0x1403a0d5c
003A1091  E8 3A DD FD FF                  call 0x14037edd0
003A1096  44 0F B6 84 24 80 00 00 00      movzx r8d, byte ptr [rsp + 0x80]
003A109F  48 8B D0                        mov rdx, rax
003A10A2  E9 CB FE FF FF                  jmp 0x1403a0f72
003A10A7  8B 05 03 0F B8 00               mov eax, dword ptr [rip + 0xb80f03]
003A10AD  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
003A10B6  44 8B 05 8F 3F C2 00            mov r8d, dword ptr [rip + 0xc23f8f]
003A10BD  49 8B 94 C4 40 8C FC 00         mov rdx, qword ptr [r12 + rax*8 + 0xfc8c40]
003A10C5  E8 B6 27 0A 00                  call 0x140443880
003A10CA  E9 32 FC FF FF                  jmp 0x1403a0d01
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KeSetTimer2(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_p0;
    unsigned __int8 v_stack_p10;
    unsigned int v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p78;
    unsigned __int8 v_stack_p8;
    unsigned __int8 v_stack_p80;
    unsigned int v_stack_p88;
    unsigned int v_stack_p90;

    v_rsp = (v_rsp) - (56);
    v_r12 = 0;
    v_stack_m58 = 0;
    if (a3 != 0) goto loc_003A0FBF;
loc_003A090E:
    v_stack_p8 = (unsigned __int8)(*(unsigned __int8 *)(a1 + 129));
    v_stack_p20 = v_cr8;
    if ((*(unsigned int *)(v_rip + 12739558)) != 0) goto loc_003A0E9F;
loc_003A0940:
    v_r15 = 0;
    if (condition_is_greater) goto loc_003A0F58;
loc_003A094C:
    if ((((unsigned __int8)(*(unsigned __int8 *)(a1 + 129))) & (4)) != 0) goto loc_003A0B27;
loc_003A0963:
    v_rdi = (*(unsigned __int64 *)(v_cr8)) - (a2);
    if (v_rdi < (*(unsigned __int64 *)(v_cr8))) goto loc_003A0B1B;
    if (v_rdi == -1) goto loc_003A0B1B;
loc_003A097C:
    if (a4 == 0) goto loc_003A09B2;
    if ((*(unsigned __int8 *)(a1 + 130)) == 23) goto loc_003A09B2;
    if ((*(unsigned __int64 *)(a4 + 8)) == -1) goto loc_003A0E18;
    if ((*(unsigned __int64 *)(a4 + 8) + v_rdi * 1) < v_rdi) goto loc_003A0E93;
    if ((*(unsigned __int64 *)(a4 + 8) + v_rdi * 1) == -1) goto loc_003A0E93;
loc_003A09B2:
    v_stack_p10 = 0;
    v_stack_p18 = 1;
    result = KiAcquireTimer2LockUnlessDisabled(a1, a2, *(unsigned __int8 *)(a1 + 129), a4);
    if ((unsigned __int8)(result) != 0) goto loc_003A0D96;
    result = KiAcquireTimer2CollectionLockIfInserted(a1, a2, *(unsigned __int8 *)(a1 + 129), a4);
    if ((unsigned __int8)(result) == 0) goto loc_003A0BF1;
    result = KiRemoveTimer2(a1, a2, *(unsigned __int8 *)(a1 + 129), a4);
    if (((*(unsigned __int8 *)(v_rip + 12738828)) & (1)) != 0) goto loc_003A101F;
loc_003A0A00:
loc_003A0A08:
    v_stack_p10 = 1;
loc_003A0A10:
    *(unsigned int *)(a1 + 4) = 0;
    *(unsigned __int64 *)(a1 + 72) = v_rdi;
    *(unsigned __int64 *)(a1 + 80) = *(unsigned __int64 *)(a4 + 8) + v_rdi * 1;
    *(unsigned __int64 *)(a1 + 88) = a3;
    *(unsigned __int8 *)(a1 + 128) = 0;
    if ((*(unsigned int *)(v_rip + 12739091)) != 0) goto loc_003A0EB8;
    if ((((unsigned __int8)(*(unsigned __int8 *)(a1 + 129))) & (46)) == 0) goto loc_003A0F01;
loc_003A0A44:
    v_r15 = 0;
    if (1 != 1) goto loc_003A100F;
    if (((*(unsigned __int8 *)(v_rip + 12738728)) & (33)) == 0) goto loc_003A0BD0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11981806))) != 0) goto loc_003A0BD0;
    result = KiAcquireSpinLockInstrumented(v_rip + 12774279, v_rip - 3803726, *(unsigned __int8 *)(a1 + 129), a4);
loc_003A0A7E:
loc_003A0A85:
    v_r14 = 0;
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 130))) == 23) goto loc_003A0B44;
    if ((((unsigned __int8)(*(unsigned __int8 *)(a1 + 130))) & (32)) != 0) goto loc_003A0B36;
loc_003A0AA4:
    a1 = (unsigned int)((*(unsigned __int8 *)(a1 + 130)) & (7));
    result = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(a1 + 130))) & (239));
    *(unsigned __int8 *)(a1 + 130) = (unsigned __int8)(result);
    v_rsi = (a1 + a1 * 2 * 8 + 15872800) + (v_rip - 3803781);
    if (((1) & ((unsigned __int8)(*(unsigned __int64 *)(v_rsi + 8)))) != 0) goto loc_003A0FDE;
loc_003A0AD5:
    a1 = (unsigned int)((*(unsigned __int64 *)(v_rsi + 8)) & (1));
    a3 = 0;
    if (*(unsigned __int64 *)(v_rsi) == 0) goto loc_003A0E4B;
loc_003A0AF0:
    if ((*(unsigned __int64 *)(a1 + 72)) >= (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) + 48))) goto loc_003A0E32;
    if ((unsigned int)(a1) == 0) goto loc_003A0B0D;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi)) == 0) goto loc_003A0FE3;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) ^ (*(unsigned __int64 *)(v_rsi));
loc_003A0B0D:
    if (result == 0) goto loc_003A0FE3;
loc_003A0B16:
    goto loc_003A0AF0;
loc_003A0B1B:
    goto loc_003A097C;
loc_003A0B27:
    result = RtlGetInterruptTimePrecise(v_stack_m58, result, *(unsigned __int64 *)(a1 + 72), a4);
    goto loc_003A0963;
loc_003A0B36:
    if ((*(unsigned __int64 *)(a1 + 72)) != (*(unsigned __int64 *)(a1 + 80))) goto loc_003A0AA4;
loc_003A0B44:
    a1 = (unsigned __int8)((v_stack_m58) | (16));
    *(unsigned __int8 *)(a1 + 130) = (unsigned __int8)(a1);
loc_003A0B4D:
    if ((*(unsigned __int64 *)(a1 + 80)) == -1) goto loc_003A0E24;
    result = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(a1 + 131))) & (239));
    a1 = (unsigned __int8)((*(unsigned __int8 *)(a1 + 131)) & (7));
    *(unsigned __int8 *)(a1 + 131) = (unsigned __int8)(result);
    if (((1) & ((unsigned __int8)(*(unsigned __int64 *)(v_rip - 3804031 + 15872800 + (unsigned __int8)(a1) + (unsigned __int8)(a1) * 2 * 8 + 8)))) != 0) goto loc_003A0FD1;
loc_003A0B9B:
    a4 = (unsigned int)((*(unsigned __int64 *)(v_rip - 3804031 + 15872800 + (unsigned __int8)(a1) + (unsigned __int8)(a1) * 2 * 8 + 8)) & (1));
    a3 = 0;
    if (*(unsigned __int64 *)(v_rip - 3804031 + 15872800 + (unsigned __int8)(a1) + (unsigned __int8)(a1) * 2 * 8) == 0) goto loc_003A0C3F;
loc_003A0BB0:
    if ((*(unsigned __int64 *)(a1 + 80)) >= (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 3804031 + 15872800 + (unsigned __int8)(a1) + (unsigned __int8)(a1) * 2 * 8) + 32))) goto loc_003A0C25;
    if ((unsigned int)(a4) == 0) goto loc_003A0BC6;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 3804031 + 15872800 + (unsigned __int8)(a1) + (unsigned __int8)(a1) * 2 * 8)) == 0) goto loc_003A0C3F;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 3804031 + 15872800 + (unsigned __int8)(a1) + (unsigned __int8)(a1) * 2 * 8))) ^ (*(unsigned __int64 *)(v_rip - 3804031 + 15872800 + (unsigned __int8)(a1) + (unsigned __int8)(a1) * 2 * 8));
loc_003A0BC6:
    if (result == 0) goto loc_003A0C3F;
loc_003A0BCB:
    goto loc_003A0BB0;
loc_003A0BD0:
    if (condition_is_above_or_equal) goto loc_003A0A85;
    result = KxWaitForSpinLockAndAcquire(v_rip + 12773913, result, a3, a4);
    goto loc_003A0A7E;
loc_003A0BF1:
    if ((((unsigned __int8)(*(unsigned __int8 *)(a1 + 1))) & (15)) == 0) goto loc_003A0A10;
    result = (unsigned __int8)((unsigned int)(v_stack_p10));
    if ((((unsigned __int8)(*(unsigned __int8 *)(a1 + 1))) & (4)) == 0) { result = 1; }
    v_stack_p18 = 8;
    v_stack_p10 = (unsigned int)(result);
    goto loc_003A0A10;
loc_003A0C25:
    if ((unsigned int)(a4) == 0) goto loc_003A0EDA;
    if (*(unsigned __int64 *)(result + 8) != 0) goto loc_003A0ED7;
loc_003A0C3B:
loc_003A0C3F:
    result = RtlRbInsertNodeEx(v_rip - 3804031 + 15872800 + (unsigned __int8)(a1) + (unsigned __int8)(a1) * 2 * 8, result, 1, 8);
    if (((1) & ((unsigned __int8)(*(unsigned __int64 *)(v_rip - 3804031 + 15872800 + (unsigned __int8)(a1) + (unsigned __int8)(a1) * 2 * 8 + 8)))) != 0) goto loc_003A0F45;
loc_003A0C5A:
    result = *(unsigned __int64 *)(v_rip - 3804031 + 15872800 + (unsigned __int8)(a1) + (unsigned __int8)(a1) * 2 * 8 + 8);
    if ((*(unsigned __int64 *)(v_rip - 3804031 + 15872800 + (unsigned __int8)(a1) + (unsigned __int8)(a1) * 2 * 8 + 8)) == 8) {
        result = *(unsigned __int64 *)(a1 + 80);
        v_r12 = 1;
        *(unsigned __int64 *)(v_rip - 3804031 + 15872800 + (unsigned __int8)(a1) + (unsigned __int8)(a1) * 2 * 8 + 16) = result;
    }
    v_rsi = (unsigned int)((v_rsi) | ((unsigned int)(v_r12)));
    v_r14 = 0;
loc_003A0C70:
    if ((unsigned int)(v_rsi) != 0) goto loc_003A0D9F;
loc_003A0C78:
    if (((*(unsigned __int8 *)(a1 + 129)) & (4)) != 0) goto loc_003A0DD5;
loc_003A0C8C:
loc_003A0C93:
    if (((*(unsigned int *)(v_rip + 12738155)) & (0x20000ULL)) != 0) goto loc_003A0E7B;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1))))) & (0xFFFFF07FULL));
    a3 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_p18)))) << (8));
    a1 = (unsigned int)((a1) | ((unsigned int)(a3)));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1)))) == ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1))))))) goto loc_003A0CD6;
loc_003A0CC1:
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1))))))) & (0xFFFFF07FULL));
    a1 = (unsigned int)((a1) | ((unsigned int)(a3)));
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1)))))))) != ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1))))))) goto loc_003A0CC1;
loc_003A0CD6:
    if (((unsigned int)((unsigned int)(v_stack_p18))) != 1) goto loc_003A0CF1;
    if (((*(unsigned __int8 *)(v_rip + 12738084)) & ((unsigned __int8)((unsigned int)(v_stack_p18)))) != 0) goto loc_003A0FEB;
loc_003A0CE8:
loc_003A0CF1:
loc_003A0CF8:
    if (0 != 0) goto loc_003A10A7;
loc_003A0D01:
    if ((*(unsigned int *)(v_rip + 12739304)) != 0) goto loc_003A0D15;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12068540)))) == 4) goto loc_003A0D5C;
loc_003A0D15:
    if (0 != 0) goto loc_003A0F9D;
    if (((v_stack_p8) & (4)) == 0) goto loc_003A0D5C;
    a1 = ((unsigned int)(*(unsigned int *)(v_rip + 12737893))) + (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(v_rip + 12068540))));
    if (-2 >= a1) goto loc_003A0D5C;
    if (*(unsigned __int64 *)(v_rip + 12063302) == 0) goto loc_003A1081;
    if (-2 < (*(unsigned __int64 *)(v_rip + 12063302))) goto loc_003A106F;
loc_003A0D5C:
    result = *(unsigned __int64 *)((unsigned int)(*(unsigned int *)(v_rip + 12068540)));
    if ((*(unsigned int *)(v_rip + 12738493)) != 0) {
        a1 = 2;
        a2 = (unsigned __int8)(v_stack_p20);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, a3, 8);
    }
    v_rsp = (v_rsp) + (56);
    return (unsigned __int8)((unsigned int)(v_stack_p10));
loc_003A0D96:
    goto loc_003A0D5C;
loc_003A0D9F:
    if ((*(unsigned __int64 *)(v_rip + 12068182)) >= = (*(unsigned __int64 *)(v_stack_p20 + 72))) {
        *(unsigned __int64 *)(v_rip + 12068173) = *(unsigned __int64 *)(v_stack_p20 + 72);
    }
    if ((*(unsigned __int64 *)(v_stack_p20 + 72)) > (*(unsigned __int64 *)(v_stack_p20 + 72))) goto loc_003A0C78;
    goto loc_003A0C78;
loc_003A0DD5:
    v_r13 = (unsigned int)((1) + 1);
    if (((unsigned int)(v_r13)) != 1) goto loc_003A0E0C;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 3804648 + (unsigned int)(*(unsigned int *)(v_rip + 12063164)) * 8 + 16550976) + 36536) != 0) goto loc_003A104B;
loc_003A0E0C:
    goto loc_003A0C93;
loc_003A0E18:
    goto loc_003A09B2;
loc_003A0E24:
    a1 = (unsigned __int8)(((unsigned __int8)(v_stack_p20)) | (16));
    *(unsigned __int8 *)(v_stack_p20 + 131) = (unsigned __int8)(a1);
    goto loc_003A0C70;
loc_003A0E32:
    if ((unsigned int)(a1) == 0) goto loc_003A0EF3;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 3804648 + (unsigned int)(*(unsigned int *)(v_rip + 12063164)) * 8 + 16550976) + 36536) + 8) != 0) goto loc_003A0EF0;
loc_003A0E47:
loc_003A0E4B:
    result = RtlRbInsertNodeEx(-1, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 3804648 + (unsigned int)(*(unsigned int *)(v_rip + 12063164)) * 8 + 16550976) + 36536), (unsigned __int8)(v_r13), (unsigned int)(v_stack_p90));
    if ((((unsigned __int8)(v_r13)) & ((unsigned __int8)(*(unsigned __int64 *)(-1 + 8)))) != 0) goto loc_003A0F8A;
loc_003A0E66:
    if ((*(unsigned __int64 *)(-1 + 8)) != ((unsigned int)(v_stack_p90))) goto loc_003A0EE8;
    *(unsigned __int64 *)(-1 + 16) = *(unsigned __int64 *)(v_stack_p20 + 72);
    goto loc_003A0B4D;
loc_003A0E7B:
    result = KiTraceSetTimer2(v_stack_p20, (unsigned __int8)((unsigned int)(v_stack_p88)), (unsigned __int8)(v_r13), (unsigned int)(v_stack_p90));
    goto loc_003A0CF8;
loc_003A0E93:
    goto loc_003A09B2;
loc_003A0E9F:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(result), (unsigned __int8)(v_stack_p20), (unsigned __int8)(v_r13), (unsigned int)(v_stack_p90));
    goto loc_003A0940;
loc_003A0EB8:
loc_003A0EBB:
    if ((((unsigned __int8)((unsigned __int8)(v_stack_p20))) & (16)) != 0) goto loc_003A0A44;
    a2 = (unsigned __int8)(((unsigned __int8)(v_stack_p20)) | (16));
    *(unsigned __int8 *)(v_stack_p20 + 129) = (unsigned __int8)(a2);
    result = KiUpdateTimer2Collections(v_stack_p20, a2, v_stack_p80, (unsigned int)(v_stack_p90));
    goto loc_003A0A44;
loc_003A0ED7:
    result = (result) ^ (a2);
loc_003A0EDA:
    if (result != 0) goto loc_003A0BCB;
    goto loc_003A0C3B;
loc_003A0EE8:
    goto loc_003A0B4D;
loc_003A0EF0:
    result = (result) ^ (a2);
loc_003A0EF3:
    if (result != 0) goto loc_003A0B16;
    goto loc_003A0E47;
loc_003A0F01:
    a3 = (unsigned __int8)(((unsigned __int8)(a2)) & (16));
    result = PsTimerResolutionActive(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), a2, a3, (unsigned int)(v_stack_p90));
    if ((unsigned __int8)(result) != 0) goto loc_003A0FAF;
    if ((unsigned __int8)(a3) == 0) goto loc_003A0A44;
    a2 = (unsigned __int8)((a2) & (239));
    *(unsigned __int8 *)(v_stack_p20 + 129) = (unsigned __int8)(a2);
    result = KiUpdateTimer2Collections(v_stack_p20, a2, a3, (unsigned int)(v_stack_p90));
    goto loc_003A0A44;
loc_003A0F45:
    if (result == v_r13) goto loc_003A0FA7;
    a1 = (1) | (v_r13);
    a1 = (a1) ^ (result);
    goto loc_003A0C5A;
loc_003A0F58:
    if ((((unsigned __int8)(a3)) & (4)) != 0) goto loc_003A1091;
loc_003A0F72:
    a1 = (*(unsigned __int64 *)(a2)) - ((unsigned int)((unsigned int)(v_rip - 3804648)));
    result = v_rip - 3804648;
    if (((unsigned int)((unsigned int)(v_rip - 3804648))) > (*(unsigned __int64 *)(a2))) { result = a1; }
    goto loc_003A094C;
loc_003A0F8A:
    if (result == v_r13) goto loc_003A0FB7;
    a1 = (result) | (v_r13);
    a1 = (a1) ^ (result);
    goto loc_003A0E66;
loc_003A0F9D:
    result = KiRequestTimer2Expiration(a1, *(unsigned __int64 *)(a2), a3, (unsigned int)(v_stack_p90));
    goto loc_003A0D5C;
loc_003A0FA7:
    goto loc_003A0C5A;
loc_003A0FAF:
    goto loc_003A0EBB;
loc_003A0FB7:
    goto loc_003A0E66;
loc_003A0FBF:
    v_r14 = 1;
    if (1 < ((unsigned int)(*(unsigned int *)(v_rip + 12737399)))) { v_r14 = (unsigned int)(*(unsigned int *)(v_rip + 12737399)); }
    goto loc_003A090E;
loc_003A0FD1:
    if (*(unsigned __int64 *)(a2) == 0) goto loc_003A1017;
    a2 = (*(unsigned __int64 *)(a2)) ^ (v_r14);
    goto loc_003A0B9B;
loc_003A0FDE:
    if (a2 != 0) goto loc_003A1043;
loc_003A0FE3:
    a3 = 0;
    goto loc_003A0E4B;
loc_003A0FEB:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11980391))) != 0) goto loc_003A0CE8;
    result = KiReleaseSpinLockInstrumented(v_rip + 12772859, v_stack_p78, a3, (unsigned int)(v_stack_p90));
    goto loc_003A0CF1;
loc_003A100F:
    v_r14 = 0;
    goto loc_003A0C8C;
loc_003A1017:
    a3 = 0;
    goto loc_003A0C3F;
loc_003A101F:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11980339))) != 0) goto loc_003A0A00;
    result = KiReleaseSpinLockInstrumented(v_rip + 12772807, v_stack_p78, a3, (unsigned int)(v_stack_p90));
    goto loc_003A0A08;
loc_003A1043:
    a2 = (v_stack_p78) ^ (result);
    goto loc_003A0AD5;
loc_003A104B:
loc_003A1050:
    if (condition_is_not_equal) goto loc_003A1050;
    v_r15 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2))))) >> (19));
    v_r15 = (unsigned __int8)(~(v_r15));
    v_r15 = (unsigned __int8)((v_r15) & (1));
    goto loc_003A0E0C;
loc_003A106F:
    a1 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2))))) - (-2);
    if (a1 <= ((unsigned int)(*(unsigned int *)(v_rip + 12737223)))) goto loc_003A0D5C;
loc_003A1081:
    result = KiSendClockInterruptToTargetProcessor((unsigned int)(*(unsigned int *)(v_rip + 12062505)), a2, a3, (unsigned int)(v_stack_p90));
    goto loc_003A0D5C;
loc_003A1091:
    result = RtlGetSystemTimePrecise((unsigned int)(*(unsigned int *)(v_rip + 12062505)), a2, a3, (unsigned int)(v_stack_p90));
    goto loc_003A0F72;
loc_003A10A7:
    result = KiHvEnlightenedGuestPriorityKick(*(unsigned __int64 *)(gs_base + (0 + 32)), *(unsigned __int64 *)(v_rip - 3804648 + (unsigned int)(*(unsigned int *)(v_rip + 12062467)) * 8 + 16550976), (unsigned int)(*(unsigned int *)(v_rip + 12730255)), (unsigned int)(v_stack_p90));
    goto loc_003A0D01;
}
```

## 5. (Beta) C Style

```c
int64_t KeSetTimer2(void *Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m58;
    uint32_t v_stack_p0;
    uint8_t v_stack_p10;
    uint32_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p78;
    uint8_t v_stack_p8;
    uint8_t v_stack_p80;
    uint32_t v_stack_p88;
    uint32_t v_stack_p90;

    local_rsp = (local_rsp) - (56);
    local_r12 = 0;
    v_stack_m58 = 0;
    if (Arg3 != 0) goto loc_003A0FBF;
loc_003A090E:
    v_stack_p8 = (uint8_t)(*(uint8_t *)(arg1 + 0x81));
    v_stack_p20 = v_cr8;
    if ((*(uint32_t *)(v_rip + 0xC263E6)) != 0) goto loc_003A0E9F;
loc_003A0940:
    local_r15 = 0;
    if (condition_is_greater) goto loc_003A0F58;
loc_003A094C:
    if ((((uint8_t)(*(uint8_t *)(arg1 + 0x81))) & (4)) != 0) goto loc_003A0B27;
loc_003A0963:
    local_rdi = (*(uint64_t *)(v_cr8)) - (Arg2);
    if (local_rdi < (*(uint64_t *)(v_cr8))) goto loc_003A0B1B;
    if (local_rdi == -1) goto loc_003A0B1B;
loc_003A097C:
    if (Arg4 == 0) goto loc_003A09B2;
    if ((*(uint8_t *)(arg1 + 0x82)) == 23) goto loc_003A09B2;
    if ((*(uint64_t *)(Arg4 + 0x8)) == -1) goto loc_003A0E18;
    if ((*(uint64_t *)(Arg4 + 0x8) + local_rdi * 1) < local_rdi) goto loc_003A0E93;
    if ((*(uint64_t *)(Arg4 + 0x8) + local_rdi * 1) == -1) goto loc_003A0E93;
loc_003A09B2:
    v_stack_p10 = 0;
    v_stack_p18 = 1;
    result = KiAcquireTimer2LockUnlessDisabled(Arg1, Arg2, *(uint8_t *)(arg1 + 0x81), Arg4);
    if ((uint8_t)(result) != 0) goto loc_003A0D96;
    result = KiAcquireTimer2CollectionLockIfInserted(Arg1, Arg2, *(uint8_t *)(arg1 + 0x81), Arg4);
    if ((uint8_t)(result) == 0) goto loc_003A0BF1;
    result = KiRemoveTimer2(Arg1, Arg2, *(uint8_t *)(arg1 + 0x81), Arg4);
    if (((*(uint8_t *)(v_rip + 0xC2610C)) & (1)) != 0) goto loc_003A101F;
loc_003A0A00:
loc_003A0A08:
    v_stack_p10 = 1;
loc_003A0A10:
    *(uint32_t *)(arg1 + 0x4) = 0;
    *(uint64_t *)(arg1 + 0x48) = local_rdi;
    *(uint64_t *)(arg1 + 0x50) = *(uint64_t *)(Arg4 + 0x8) + local_rdi * 1;
    *(uint64_t *)(arg1 + 0x58) = Arg3;
    *(uint8_t *)(arg1 + 0x80) = 0;
    if ((*(uint32_t *)(v_rip + 0xC26213)) != 0) goto loc_003A0EB8;
    if ((((uint8_t)(*(uint8_t *)(arg1 + 0x81))) & (46)) == 0) goto loc_003A0F01;
loc_003A0A44:
    local_r15 = 0;
    if (1 != 1) goto loc_003A100F;
    if (((*(uint8_t *)(v_rip + 0xC260A8)) & (33)) == 0) goto loc_003A0BD0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB6D3EE))) != 0) goto loc_003A0BD0;
    result = KiAcquireSpinLockInstrumented(v_rip + 12774279, v_rip - 3803726, *(uint8_t *)(arg1 + 0x81), Arg4);
loc_003A0A7E:
loc_003A0A85:
    local_r14 = 0;
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x82))) == 23) goto loc_003A0B44;
    if ((((uint8_t)(*(uint8_t *)(arg1 + 0x82))) & (32)) != 0) goto loc_003A0B36;
loc_003A0AA4:
    Arg1 = (uint32_t)((*(uint8_t *)(arg1 + 0x82)) & (7));
    result = (uint8_t)(((uint8_t)(*(uint8_t *)(arg1 + 0x82))) & (239));
    *(uint8_t *)(arg1 + 0x82) = (uint8_t)(result);
    local_rsi = (Arg1 + Arg1 * 2 * 8 + 15872800) + (v_rip - 3803781);
    if (((1) & ((uint8_t)(*(uint64_t *)(local_rsi + 0x8)))) != 0) goto loc_003A0FDE;
loc_003A0AD5:
    Arg1 = (uint32_t)((*(uint64_t *)(local_rsi + 0x8)) & (1));
    Arg3 = 0;
    if (*(uint64_t *)(local_rsi) == 0) goto loc_003A0E4B;
loc_003A0AF0:
    if ((*(uint64_t *)(arg1 + 0x48)) >= (*(uint64_t *)(*(uint64_t *)(local_rsi) + 0x30))) goto loc_003A0E32;
    if ((uint32_t)(Arg1) == 0) goto loc_003A0B0D;
    if (*(uint64_t *)(*(uint64_t *)(local_rsi)) == 0) goto loc_003A0FE3;
    result = (*(uint64_t *)(*(uint64_t *)(local_rsi))) ^ (*(uint64_t *)(local_rsi));
loc_003A0B0D:
    if (result == 0) goto loc_003A0FE3;
loc_003A0B16:
    goto loc_003A0AF0;
loc_003A0B1B:
    goto loc_003A097C;
loc_003A0B27:
    result = RtlGetInterruptTimePrecise(v_stack_m58, result, *(uint64_t *)(arg1 + 0x48), Arg4);
    goto loc_003A0963;
loc_003A0B36:
    if ((*(uint64_t *)(arg1 + 0x48)) != (*(uint64_t *)(arg1 + 0x50))) goto loc_003A0AA4;
loc_003A0B44:
    Arg1 = (uint8_t)((v_stack_m58) | (16));
    *(uint8_t *)(arg1 + 0x82) = (uint8_t)(Arg1);
loc_003A0B4D:
    if ((*(uint64_t *)(arg1 + 0x50)) == -1) goto loc_003A0E24;
    result = (uint8_t)(((uint8_t)(*(uint8_t *)(arg1 + 0x83))) & (239));
    Arg1 = (uint8_t)((*(uint8_t *)(arg1 + 0x83)) & (7));
    *(uint8_t *)(arg1 + 0x83) = (uint8_t)(result);
    if (((1) & ((uint8_t)(*(uint64_t *)(v_rip - 0x3A0B7F + 0xF23320 + (uint8_t)(arg1) + (uint8_t)(arg1) * 2 * 8 + 0x8)))) != 0) goto loc_003A0FD1;
loc_003A0B9B:
    Arg4 = (uint32_t)((*(uint64_t *)(v_rip - 0x3A0B7F + 0xF23320 + (uint8_t)(arg1) + (uint8_t)(arg1) * 2 * 8 + 0x8)) & (1));
    Arg3 = 0;
    if (*(uint64_t *)(v_rip - 0x3A0B7F + 0xF23320 + (uint8_t)(arg1) + (uint8_t)(arg1) * 2 * 8) == 0) goto loc_003A0C3F;
loc_003A0BB0:
    if ((*(uint64_t *)(arg1 + 0x50)) >= (*(uint64_t *)(*(uint64_t *)(v_rip - 0x3A0B7F + 0xF23320 + (uint8_t)(arg1) + (uint8_t)(arg1) * 2 * 8) + 0x20))) goto loc_003A0C25;
    if ((uint32_t)(Arg4) == 0) goto loc_003A0BC6;
    if (*(uint64_t *)(*(uint64_t *)(v_rip - 0x3A0B7F + 0xF23320 + (uint8_t)(arg1) + (uint8_t)(arg1) * 2 * 8)) == 0) goto loc_003A0C3F;
    result = (*(uint64_t *)(*(uint64_t *)(v_rip - 0x3A0B7F + 0xF23320 + (uint8_t)(arg1) + (uint8_t)(arg1) * 2 * 8))) ^ (*(uint64_t *)(v_rip - 0x3A0B7F + 0xF23320 + (uint8_t)(arg1) + (uint8_t)(arg1) * 2 * 8));
loc_003A0BC6:
    if (result == 0) goto loc_003A0C3F;
loc_003A0BCB:
    goto loc_003A0BB0;
loc_003A0BD0:
    if (condition_is_above_or_equal) goto loc_003A0A85;
    result = KxWaitForSpinLockAndAcquire(v_rip + 12773913, result, Arg3, Arg4);
    goto loc_003A0A7E;
loc_003A0BF1:
    if ((((uint8_t)(*(uint8_t *)(arg1 + 0x1))) & (15)) == 0) goto loc_003A0A10;
    result = (uint8_t)((uint32_t)(v_stack_p10));
    if ((((uint8_t)(*(uint8_t *)(arg1 + 0x1))) & (4)) == 0) { result = 1; }
    v_stack_p18 = 8;
    v_stack_p10 = (uint32_t)(result);
    goto loc_003A0A10;
loc_003A0C25:
    if ((uint32_t)(Arg4) == 0) goto loc_003A0EDA;
    if (*(uint64_t *)(result + 0x8) != 0) goto loc_003A0ED7;
loc_003A0C3B:
loc_003A0C3F:
    result = RtlRbInsertNodeEx(v_rip - 3804031 + 15872800 + (uint8_t)(Arg1) + (uint8_t)(Arg1) * 2 * 8, result, 1, 8);
    if (((1) & ((uint8_t)(*(uint64_t *)(v_rip - 0x3A0B7F + 0xF23320 + (uint8_t)(arg1) + (uint8_t)(arg1) * 2 * 8 + 0x8)))) != 0) goto loc_003A0F45;
loc_003A0C5A:
    result = *(uint64_t *)(v_rip - 0x3A0B7F + 0xF23320 + (uint8_t)(arg1) + (uint8_t)(arg1) * 2 * 8 + 0x8);
    if ((*(uint64_t *)(v_rip - 0x3A0B7F + 0xF23320 + (uint8_t)(arg1) + (uint8_t)(arg1) * 2 * 8 + 0x8)) == 8) {
        result = *(uint64_t *)(arg1 + 0x50);
        local_r12 = 1;
        *(uint64_t *)(v_rip - 0x3A0B7F + 0xF23320 + (uint8_t)(arg1) + (uint8_t)(arg1) * 2 * 8 + 0x10) = result;
    }
    local_rsi = (uint32_t)((local_rsi) | ((uint32_t)(local_r12)));
    local_r14 = 0;
loc_003A0C70:
    if ((uint32_t)(local_rsi) != 0) goto loc_003A0D9F;
loc_003A0C78:
    if (((*(uint8_t *)(arg1 + 0x81)) & (4)) != 0) goto loc_003A0DD5;
loc_003A0C8C:
loc_003A0C93:
    if (((*(uint32_t *)(v_rip + 0xC25E6B)) & (0x20000ULL)) != 0) goto loc_003A0E7B;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1))))) & (0xFFFFF07FULL));
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_p18)))) << (8));
    Arg1 = (uint32_t)((Arg1) | ((uint32_t)(Arg3)));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1)))) == ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1))))))) goto loc_003A0CD6;
loc_003A0CC1:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1))))))) & (0xFFFFF07FULL));
    Arg1 = (uint32_t)((Arg1) | ((uint32_t)(Arg3)));
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1)))))))) != ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1))))))) goto loc_003A0CC1;
loc_003A0CD6:
    if (((uint32_t)((uint32_t)(v_stack_p18))) != 1) goto loc_003A0CF1;
    if (((*(uint8_t *)(v_rip + 0xC25E24)) & ((uint8_t)((uint32_t)(v_stack_p18)))) != 0) goto loc_003A0FEB;
loc_003A0CE8:
loc_003A0CF1:
loc_003A0CF8:
    if (0 != 0) goto loc_003A10A7;
loc_003A0D01:
    if ((*(uint32_t *)(v_rip + 0xC262E8)) != 0) goto loc_003A0D15;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB826BC)))) == 4) goto loc_003A0D5C;
loc_003A0D15:
    if (0 != 0) goto loc_003A0F9D;
    if (((v_stack_p8) & (4)) == 0) goto loc_003A0D5C;
    Arg1 = ((uint32_t)(*(uint32_t *)(v_rip + 0xC25D65))) + (*(uint64_t *)((uint32_t)(*(uint32_t *)(v_rip + 0xB826BC))));
    if (-2 >= Arg1) goto loc_003A0D5C;
    if (*(uint64_t *)(v_rip + 0xB81246) == 0) goto loc_003A1081;
    if (-2 < (*(uint64_t *)(v_rip + 0xB81246))) goto loc_003A106F;
loc_003A0D5C:
    result = *(uint64_t *)((uint32_t)(*(uint32_t *)(v_rip + 0xB826BC)));
    if ((*(uint32_t *)(v_rip + 0xC25FBD)) != 0) {
        Arg1 = 2;
        Arg2 = (uint8_t)(v_stack_p20);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, Arg3, 8);
    }
    local_rsp = (local_rsp) + (56);
    return (uint8_t)((uint32_t)(v_stack_p10));
loc_003A0D96:
    goto loc_003A0D5C;
loc_003A0D9F:
    if ((*(uint64_t *)(v_rip + 0xB82556)) >= = (*(uint64_t *)(v_stack_p20 + 0x48))) {
        *(uint64_t *)(v_rip + 0xB8254D) = *(uint64_t *)(v_stack_p20 + 0x48);
    }
    if ((*(uint64_t *)(v_stack_p20 + 0x48)) > (*(uint64_t *)(v_stack_p20 + 0x48))) goto loc_003A0C78;
    goto loc_003A0C78;
loc_003A0DD5:
    local_r13 = (uint32_t)((1) + 1);
    if (((uint32_t)(local_r13)) != 1) goto loc_003A0E0C;
    if (*(uint64_t *)(*(uint64_t *)(v_rip - 0x3A0DE8 + (uint32_t)(*(uint32_t *)(v_rip + 0xB811BC)) * 8 + 0xFC8C40) + 0x8EB8) != 0) goto loc_003A104B;
loc_003A0E0C:
    goto loc_003A0C93;
loc_003A0E18:
    goto loc_003A09B2;
loc_003A0E24:
    Arg1 = (uint8_t)(((uint8_t)(v_stack_p20)) | (16));
    *(uint8_t *)(v_stack_p20 + 0x83) = (uint8_t)(Arg1);
    goto loc_003A0C70;
loc_003A0E32:
    if ((uint32_t)(Arg1) == 0) goto loc_003A0EF3;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip - 0x3A0DE8 + (uint32_t)(*(uint32_t *)(v_rip + 0xB811BC)) * 8 + 0xFC8C40) + 0x8EB8) + 0x8) != 0) goto loc_003A0EF0;
loc_003A0E47:
loc_003A0E4B:
    result = RtlRbInsertNodeEx(-1, *(uint64_t *)(*(uint64_t *)(v_rip - 0x3A0DE8 + (uint32_t)(*(uint32_t *)(v_rip + 0xB811BC)) * 8 + 0xFC8C40) + 0x8EB8), (uint8_t)(local_r13), (uint32_t)(v_stack_p90));
    if ((((uint8_t)(local_r13)) & ((uint8_t)(*(uint64_t *)(- 0x1 + 0x8)))) != 0) goto loc_003A0F8A;
loc_003A0E66:
    if ((*(uint64_t *)(- 0x1 + 0x8)) != ((uint32_t)(v_stack_p90))) goto loc_003A0EE8;
    *(uint64_t *)(- 0x1 + 0x10) = *(uint64_t *)(v_stack_p20 + 0x48);
    goto loc_003A0B4D;
loc_003A0E7B:
    result = KiTraceSetTimer2(v_stack_p20, (uint8_t)((uint32_t)(v_stack_p88)), (uint8_t)(local_r13), (uint32_t)(v_stack_p90));
    goto loc_003A0CF8;
loc_003A0E93:
    goto loc_003A09B2;
loc_003A0E9F:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(result), (uint8_t)(v_stack_p20), (uint8_t)(local_r13), (uint32_t)(v_stack_p90));
    goto loc_003A0940;
loc_003A0EB8:
loc_003A0EBB:
    if ((((uint8_t)((uint8_t)(v_stack_p20))) & (16)) != 0) goto loc_003A0A44;
    Arg2 = (uint8_t)(((uint8_t)(v_stack_p20)) | (16));
    *(uint8_t *)(v_stack_p20 + 0x81) = (uint8_t)(Arg2);
    result = KiUpdateTimer2Collections(v_stack_p20, Arg2, v_stack_p80, (uint32_t)(v_stack_p90));
    goto loc_003A0A44;
loc_003A0ED7:
    result = (result) ^ (Arg2);
loc_003A0EDA:
    if (result != 0) goto loc_003A0BCB;
    goto loc_003A0C3B;
loc_003A0EE8:
    goto loc_003A0B4D;
loc_003A0EF0:
    result = (result) ^ (Arg2);
loc_003A0EF3:
    if (result != 0) goto loc_003A0B16;
    goto loc_003A0E47;
loc_003A0F01:
    Arg3 = (uint8_t)(((uint8_t)(Arg2)) & (16));
    result = PsTimerResolutionActive(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), Arg2, Arg3, (uint32_t)(v_stack_p90));
    if ((uint8_t)(result) != 0) goto loc_003A0FAF;
    if ((uint8_t)(Arg3) == 0) goto loc_003A0A44;
    Arg2 = (uint8_t)((Arg2) & (239));
    *(uint8_t *)(v_stack_p20 + 0x81) = (uint8_t)(Arg2);
    result = KiUpdateTimer2Collections(v_stack_p20, Arg2, Arg3, (uint32_t)(v_stack_p90));
    goto loc_003A0A44;
loc_003A0F45:
    if (result == local_r13) goto loc_003A0FA7;
    Arg1 = (1) | (local_r13);
    Arg1 = (Arg1) ^ (result);
    goto loc_003A0C5A;
loc_003A0F58:
    if ((((uint8_t)(Arg3)) & (4)) != 0) goto loc_003A1091;
loc_003A0F72:
    Arg1 = (*(uint64_t *)(Arg2)) - ((uint32_t)((uint32_t)(v_rip - 3804648)));
    result = v_rip - 3804648;
    if (((uint32_t)((uint32_t)(v_rip - 3804648))) > (*(uint64_t *)(Arg2))) { result = Arg1; }
    goto loc_003A094C;
loc_003A0F8A:
    if (result == local_r13) goto loc_003A0FB7;
    Arg1 = (result) | (local_r13);
    Arg1 = (Arg1) ^ (result);
    goto loc_003A0E66;
loc_003A0F9D:
    result = KiRequestTimer2Expiration(Arg1, *(uint64_t *)(Arg2), Arg3, (uint32_t)(v_stack_p90));
    goto loc_003A0D5C;
loc_003A0FA7:
    goto loc_003A0C5A;
loc_003A0FAF:
    goto loc_003A0EBB;
loc_003A0FB7:
    goto loc_003A0E66;
loc_003A0FBF:
    local_r14 = 1;
    if (1 < ((uint32_t)(*(uint32_t *)(v_rip + 0xC25B77)))) { local_r14 = (uint32_t)(*(uint32_t *)(v_rip + 0xC25B77)); }
    goto loc_003A090E;
loc_003A0FD1:
    if (*(uint64_t *)(Arg2) == 0) goto loc_003A1017;
    Arg2 = (*(uint64_t *)(Arg2)) ^ (local_r14);
    goto loc_003A0B9B;
loc_003A0FDE:
    if (Arg2 != 0) goto loc_003A1043;
loc_003A0FE3:
    Arg3 = 0;
    goto loc_003A0E4B;
loc_003A0FEB:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB6CE67))) != 0) goto loc_003A0CE8;
    result = KiReleaseSpinLockInstrumented(v_rip + 12772859, v_stack_p78, Arg3, (uint32_t)(v_stack_p90));
    goto loc_003A0CF1;
loc_003A100F:
    local_r14 = 0;
    goto loc_003A0C8C;
loc_003A1017:
    Arg3 = 0;
    goto loc_003A0C3F;
loc_003A101F:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB6CE33))) != 0) goto loc_003A0A00;
    result = KiReleaseSpinLockInstrumented(v_rip + 12772807, v_stack_p78, Arg3, (uint32_t)(v_stack_p90));
    goto loc_003A0A08;
loc_003A1043:
    Arg2 = (v_stack_p78) ^ (result);
    goto loc_003A0AD5;
loc_003A104B:
loc_003A1050:
    if (condition_is_not_equal) goto loc_003A1050;
    local_r15 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg2))))) >> (19));
    local_r15 = (uint8_t)(~(local_r15));
    local_r15 = (uint8_t)((local_r15) & (1));
    goto loc_003A0E0C;
loc_003A106F:
    Arg1 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg2))))) - (-2);
    if (Arg1 <= ((uint32_t)(*(uint32_t *)(v_rip + 0xC25AC7)))) goto loc_003A0D5C;
loc_003A1081:
    result = KiSendClockInterruptToTargetProcessor((uint32_t)(*(uint32_t *)(v_rip + 0xB80F29)), Arg2, Arg3, (uint32_t)(v_stack_p90));
    goto loc_003A0D5C;
loc_003A1091:
    result = RtlGetSystemTimePrecise((uint32_t)(*(uint32_t *)(v_rip + 0xB80F29)), Arg2, Arg3, (uint32_t)(v_stack_p90));
    goto loc_003A0F72;
loc_003A10A7:
    result = KiHvEnlightenedGuestPriorityKick(*(uint64_t *)(gs_base + (0 + 0x20)), *(uint64_t *)(v_rip - 0x3A0DE8 + (uint32_t)(*(uint32_t *)(v_rip + 0xB80F03)) * 8 + 0xFC8C40), (uint32_t)(*(uint32_t *)(v_rip + 0xC23F8F)), (uint32_t)(v_stack_p90));
    goto loc_003A0D01;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x1` | `8` | `R` |
| `Arg1` | `+ 0x4` | `32` | `W` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x30` | `64` | `R` |
| `Arg1` | `+ 0x48` | `64` | `R` |
| `Arg1` | `+ 0x48` | `64` | `W` |
| `Arg1` | `+ 0x50` | `64` | `R` |
| `Arg1` | `+ 0x50` | `64` | `W` |
| `Arg1` | `+ 0x58` | `64` | `W` |
| `Arg1` | `+ 0x80` | `8` | `W` |
| `Arg1` | `+ 0x81` | `8` | `R` |
| `Arg1` | `+ 0x81` | `8` | `W` |
| `Arg1` | `+ 0x82` | `8` | `R` |
| `Arg1` | `+ 0x82` | `8` | `W` |
| `Arg1` | `+ 0x83` | `8` | `R` |
| `Arg1` | `+ 0x83` | `8` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003A08E0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
