# KeInitializeClock

- RVA: `0x00C70C30`–`0x00C71148` (길이 `1,304` bytes)
- VA: `0x0000000140C70C30`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BAEFC`
- 디코드: `294`개 명령, `1,304/1,304` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **25**; 고유 호출 대상: **18**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **60**

### Outgoing calls
- `0x00C70CA9` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C70CDD` → [EmClientQueryRuleState](../../pagelk/B7/EmClientQueryRuleState_function_00B77D70.md) (function, `0x00B77D70`)
- `0x00C70CFB` → [PoTraceDynamicTickDisabled](../../text/5D/PoTraceDynamicTickDisabled_function_005D5BB8.md) (function, `0x005D5BB8`)
- `0x00C70D50` → [wil_details_FeatureReporting_ReportUsageToService](../../text/53/wil_details_FeatureReporting_ReportUsageToService_function_0053E6E4.md) (function, `0x0053E6E4`)
- `0x00C70D65` → [wil_details_FeatureStateCache_TryEnableDeviceUsageFastPath](../../text/53/wil_details_FeatureStateCache_TryEnableDeviceUsageFastPath_function_0053E774.md) (function, `0x0053E774`)
- `0x00C70DB8` → [wil_details_FeatureReporting_ReportUsageToService](../../text/53/wil_details_FeatureReporting_ReportUsageToService_function_0053E6E4.md) (function, `0x0053E6E4`)
- `0x00C70DCD` → [wil_details_FeatureStateCache_TryEnableDeviceUsageFastPath](../../text/53/wil_details_FeatureStateCache_TryEnableDeviceUsageFastPath_function_0053E774.md) (function, `0x0053E774`)
- `0x00C70E5B` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)
- `0x00C70E9D` → [KiRaiseIrqlProcessIrqlFlags](../../text/4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x00C70EBA` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00C70EC1` → [KiSetPendingTick](../../text/44/KiSetPendingTick_function_004400F4.md) (function, `0x004400F4`)
- `0x00C70ECD` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00C70EDB` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00C70F8F` → [RtlRbInsertNodeEx](../../text/2E/RtlRbInsertNodeEx_function_002E4570.md) (function, `0x002E4570`)
- `0x00C70FCD` → [KiSetClockTimer](../../text/39/KiSetClockTimer_function_0039DB2C.md) (function, `0x0039DB2C`)
- `0x00C70FDB` → [KiSetClockTimerKTimerDeadlines](../../text/23/KiSetClockTimerKTimerDeadlines_function_0023671C.md) (function, `0x0023671C`)
- `0x00C70FE5` → [KiSetNextClockTickDueTime](../../text/23/KiSetNextClockTickDueTime_function_002363F0.md) (function, `0x002363F0`)
- `0x00C71005` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00C7100C` → [KiSetPendingTick](../../text/44/KiSetPendingTick_function_004400F4.md) (function, `0x004400F4`)
- `0x00C71054` → [KiLowerIrqlProcessIrqlFlags](../../text/4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x00C710AF` → [strstr](../../text/4F/strstr_function_004FF680.md) (function, `0x004FF680`)
- `0x00C710CE` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00C71115` → [KiSetupTimeIncrement](../../text/5B/KiSetupTimeIncrement_function_005B2244.md) (function, `0x005B2244`)
- `0x00C7111D` → [KiInitializeProcessorCycleAccumulation](../../text/5B/KiInitializeProcessorCycleAccumulation_function_005B2014.md) (function, `0x005B2014`)
- `0x00C71129` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [InitBootProcessor](../C1/InitBootProcessor_function_00C1B1C8.md) at `0x00C1B478`
- [Phase1InitializationDiscard](../C1/Phase1InitializationDiscard_function_00C1C728.md) at `0x00C1CAA3`
- [Phase1InitializationIoReady](Phase1InitializationIoReady_function_00C70458.md) at `0x00C705EC`

### Static image references
- `0x00C70C4A` → RVA `0x00E0A740` (`.data`; read)
- `0x00C70CAF` → RVA `0x00FC5364` (`ALMOSTRO`; read)
- `0x00C70CB8` → RVA `0x00FC6A97` (`ALMOSTRO`; read)
- `0x00C70CC1` → RVA `0x00FC6A90` (`ALMOSTRO`; read)
- `0x00C70CD6` → RVA `0x00028BD8` (`.rdata`; read)
- `0x00C70CE8` → RVA `0x00FC5364` (`ALMOSTRO`; write)
- `0x00C70D00` → RVA `0x00FC6FF0` (`ALMOSTRO`; write)
- `0x00C70D0F` → RVA `0x00FC6BC4` (`ALMOSTRO`; write)
- `0x00C70D1B` → RVA `0x00FC4608` (`.data`; read)
- `0x00C70D41` → RVA `0x000DCC58` (`.rdata`; read)
- `0x00C70D6A` → RVA `0x00FC6ABF` (`ALMOSTRO`; read)
- `0x00C70D71` → RVA `0x00FC6A95` (`ALMOSTRO`; write)
- `0x00C70D7A` → RVA `0x00FC5030` (`ALMOSTRO`; read)
- `0x00C70D83` → RVA `0x00FC4610` (`.data`; read)
- `0x00C70DA9` → RVA `0x000DCC90` (`.rdata`; read)
- `0x00C70DD2` → RVA `0x00FC6A85` (`ALMOSTRO`; write)
- `0x00C70DD9` → RVA `0x00FC6E6C` (`ALMOSTRO`; read)
- `0x00C70DED` → RVA `0x00FC6E70` (`ALMOSTRO`; read)
- `0x00C70E0A` → RVA `0x00FC6B38` (`ALMOSTRO`; read)
- `0x00C70E19` → RVA `0x00FC6AA0` (`ALMOSTRO`; read)
- `0x00C70E2C` → RVA `0x00FC6AF8` (`ALMOSTRO`; write)
- `0x00C70E33` → RVA `0x00FC6D5C` (`ALMOSTRO`; write)
- `0x00C70E3D` → RVA `0x00FC6AA5` (`ALMOSTRO`; write)
- `0x00C70E44` → RVA `0x00FC7058` (`ALMOSTRO`; write)
- `0x00C70E68` → RVA `0x00F21FB0` (`.data`; read)
- `0x00C70E6E` → RVA `0x00FC7390` (`ALMOSTRO`; write)
- `0x00C70E75` → RVA `0x00FC8C40` (`ALMOSTRO`; read)
- `0x00C70E91` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x00C70EAC` → RVA `0x00E00AE8` (`.data`; read)
- `0x00C70EB3` → RVA `0x00FCF000` (`CACHEALI`; write)
- `0x00C70EC6` → RVA `0x00E00AE0` (`.data`; read)
- `0x00C70ED2` → RVA `0x00E00AD8` (`.data`; read)
- `0x00C70EE7` → RVA `0x00E668E0` (`.data`; read)
- `0x00C70EEE` → RVA `0x00FC6BEC` (`ALMOSTRO`; write)
- `0x00C70EF5` → RVA `0x00FC6BB8` (`ALMOSTRO`; write)
- `0x00C70EFC` → RVA `0x00E668A8` (`.data`; write)
- `0x00C70F03` → RVA `0x00E668B0` (`.data`; write)
- `0x00C70F0A` → RVA `0x00F223BC` (`.data`; write)
- `0x00C70F16` → RVA `0x00E668D8` (`.data`; read)
- `0x00C70F81` → RVA `0x00F223A0` (`.data`; read)
- `0x00C70F94` → RVA `0x00FC6A85` (`ALMOSTRO`; read)
- `0x00C70F9B` → RVA `0x00F223B8` (`.data`; write)
- `0x00C70FA4` → RVA `0x00FC6D5C` (`ALMOSTRO`; read)
- `0x00C70FAE` → RVA `0x00FC6B3C` (`ALMOSTRO`; read)
- `0x00C70FFC` → RVA `0x00E00AF0` (`.data`; read)
- `0x00C7101B` → RVA `0x00FC6B7C` (`ALMOSTRO`; write)
- `0x00C71037` → RVA `0x00F21FC0` (`.data`; write)
- `0x00C71061` → RVA `0x00FC6B7C` (`ALMOSTRO`; read)
- `0x00C71067` → RVA `0x00F21F50` (`.data`; write)
- `0x00C7106D` → RVA `0x00F21F54` (`.data`; write)
- `0x00C71073` → RVA `0x00F21FC0` (`.data`; read)
- `0x00C71079` → RVA `0x00F21F58` (`.data`; write)
- `0x00C7107F` → RVA `0x00F21F5C` (`.data`; write)
- `0x00C71095` → RVA `0x00F21F48` (`.data`; write)
- `0x00C7109C` → RVA `0x00F21F68` (`.data`; write)
- `0x00C710A8` → RVA `0x00C7B260` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C710C3` → RVA `0x00E00AD0` (`.data`; read)
- `0x00C710DA` → RVA `0x00FC6ABF` (`ALMOSTRO`; write)
- `0x00C710E5` → RVA `0x00FC6BA7` (`ALMOSTRO`; write)
- `0x00C710F0` → RVA `0x00FC6BD7` (`ALMOSTRO`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **25**
  - `0x00C70CA9` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C70CDD` → [EmClientQueryRuleState](../../pagelk/B7/EmClientQueryRuleState_function_00B77D70.md) (`INIT` → `PAGELK`)
  - `0x00C70CFB` → [PoTraceDynamicTickDisabled](../../text/5D/PoTraceDynamicTickDisabled_function_005D5BB8.md) (`INIT` → `.text`)
  - `0x00C70D50` → [wil_details_FeatureReporting_ReportUsageToService](../../text/53/wil_details_FeatureReporting_ReportUsageToService_function_0053E6E4.md) (`INIT` → `.text`)
  - `0x00C70D65` → [wil_details_FeatureStateCache_TryEnableDeviceUsageFastPath](../../text/53/wil_details_FeatureStateCache_TryEnableDeviceUsageFastPath_function_0053E774.md) (`INIT` → `.text`)
  - `0x00C70DB8` → [wil_details_FeatureReporting_ReportUsageToService](../../text/53/wil_details_FeatureReporting_ReportUsageToService_function_0053E6E4.md) (`INIT` → `.text`)
  - `0x00C70DCD` → [wil_details_FeatureStateCache_TryEnableDeviceUsageFastPath](../../text/53/wil_details_FeatureStateCache_TryEnableDeviceUsageFastPath_function_0053E774.md) (`INIT` → `.text`)
  - `0x00C70E5B` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (`INIT` → `.text`)
  - `0x00C70E9D` → [KiRaiseIrqlProcessIrqlFlags](../../text/4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (`INIT` → `.text`)
  - `0x00C70EBA` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`INIT` → `.text`)
  - `0x00C70EC1` → [KiSetPendingTick](../../text/44/KiSetPendingTick_function_004400F4.md) (`INIT` → `.text`)
  - `0x00C70ECD` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`INIT` → `.text`)
  - `0x00C70EDB` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`INIT` → `.text`)
  - `0x00C70F8F` → [RtlRbInsertNodeEx](../../text/2E/RtlRbInsertNodeEx_function_002E4570.md) (`INIT` → `.text`)
  - `0x00C70FCD` → [KiSetClockTimer](../../text/39/KiSetClockTimer_function_0039DB2C.md) (`INIT` → `.text`)
  - `0x00C70FDB` → [KiSetClockTimerKTimerDeadlines](../../text/23/KiSetClockTimerKTimerDeadlines_function_0023671C.md) (`INIT` → `.text`)
  - `0x00C70FE5` → [KiSetNextClockTickDueTime](../../text/23/KiSetNextClockTickDueTime_function_002363F0.md) (`INIT` → `.text`)
  - `0x00C71005` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`INIT` → `.text`)
  - `0x00C7100C` → [KiSetPendingTick](../../text/44/KiSetPendingTick_function_004400F4.md) (`INIT` → `.text`)
  - `0x00C71054` → [KiLowerIrqlProcessIrqlFlags](../../text/4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (`INIT` → `.text`)
  - `0x00C710AF` → [strstr](../../text/4F/strstr_function_004FF680.md) (`INIT` → `.text`)
  - `0x00C710CE` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`INIT` → `.text`)
  - `0x00C71115` → [KiSetupTimeIncrement](../../text/5B/KiSetupTimeIncrement_function_005B2244.md) (`INIT` → `.text`)
  - `0x00C7111D` → [KiInitializeProcessorCycleAccumulation](../../text/5B/KiInitializeProcessorCycleAccumulation_function_005B2014.md) (`INIT` → `.text`)
  - `0x00C71129` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`INIT` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C70C30  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
00C70C35  55                              push rbp
00C70C36  41 54                           push r12
00C70C38  41 55                           push r13
00C70C3A  41 56                           push r14
00C70C3C  41 57                           push r15
00C70C3E  48 8D 6C 24 C9                  lea rbp, [rsp - 0x37]
00C70C43  48 81 EC 90 00 00 00            sub rsp, 0x90
00C70C4A  48 8B 05 EF 9A 19 00            mov rax, qword ptr [rip + 0x199aef]
00C70C51  48 33 C4                        xor rax, rsp
00C70C54  48 89 45 27                     mov qword ptr [rbp + 0x27], rax
00C70C58  33 C0                           xor eax, eax
00C70C5A  45 33 ED                        xor r13d, r13d
00C70C5D  48 89 45 17                     mov qword ptr [rbp + 0x17], rax
00C70C61  0F 57 C0                        xorps xmm0, xmm0
00C70C64  89 45 1F                        mov dword ptr [rbp + 0x1f], eax
00C70C67  88 45 23                        mov byte ptr [rbp + 0x23], al
00C70C6A  8B C1                           mov eax, ecx
00C70C6C  4C 89 6D F7                     mov qword ptr [rbp - 9], r13
00C70C70  4C 89 6D FF                     mov qword ptr [rbp - 1], r13
00C70C74  0F 11 45 07                     movups xmmword ptr [rbp + 7], xmm0
00C70C78  65 4C 8B 24 25 20 00 00 00      mov r12, qword ptr gs:[0x20]
00C70C81  85 C9                           test ecx, ecx
00C70C83  0F 84 01 04 00 00               je 0x140c7108a
00C70C89  83 E8 01                        sub eax, 1
00C70C8C  0F 84 89 00 00 00               je 0x140c70d1b
00C70C92  83 F8 01                        cmp eax, 1
00C70C95  74 18                           je 0x140c70caf
00C70C97  41 8D 55 01                     lea edx, [r13 + 1]
00C70C9B  44 8B C1                        mov r8d, ecx
00C70C9E  8D 4A 32                        lea ecx, [rdx + 0x32]
00C70CA1  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
00C70CA6  45 33 C9                        xor r9d, r9d
00C70CA9  E8 B2 C9 88 FF                  call 0x1404fd660
00C70CAE  CC                              int3
00C70CAF  44 38 2D AE 46 35 00            cmp byte ptr [rip + 0x3546ae], r13b
00C70CB6  75 43                           jne 0x140c70cfb
00C70CB8  44 38 2D D8 5D 35 00            cmp byte ptr [rip + 0x355dd8], r13b
00C70CBF  74 0A                           je 0x140c70ccb
00C70CC1  8B 05 C9 5D 35 00               mov eax, dword ptr [rip + 0x355dc9]
00C70CC7  A8 02                           test al, 2
00C70CC9  74 27                           je 0x140c70cf2
00C70CCB  48 8D 55 EF                     lea rdx, [rbp - 0x11]
00C70CCF  C7 45 EF 01 00 00 00            mov dword ptr [rbp - 0x11], 1
00C70CD6  48 8D 0D FB 7E 3B FF            lea rcx, [rip - 0xc48105]
00C70CDD  E8 8E 70 F0 FF                  call 0x140b77d70
00C70CE2  83 7D EF 02                     cmp dword ptr [rbp - 0x11], 2
00C70CE6  75 0A                           jne 0x140c70cf2
00C70CE8  C7 05 72 46 35 00 03 00 00 00   mov dword ptr [rip + 0x354672], 3
00C70CF2  44 38 2D 6B 46 35 00            cmp byte ptr [rip + 0x35466b], r13b
00C70CF9  74 0F                           je 0x140c70d0a
00C70CFB  E8 B8 4E 96 FF                  call 0x1405d5bb8
00C70D00  C7 05 E6 62 35 00 01 00 00 00   mov dword ptr [rip + 0x3562e6], 1
00C70D0A  F0 44 09 2C 24                  lock or dword ptr [rsp], r13d
00C70D0F  C6 05 AE 5E 35 00 01            mov byte ptr [rip + 0x355eae], 1
00C70D16  E9 07 04 00 00                  jmp 0x140c71122
00C70D1B  8B 0D E7 38 35 00               mov ecx, dword ptr [rip + 0x3538e7]
00C70D21  4C 89 6D E7                     mov qword ptr [rbp - 0x19], r13
00C70D25  89 4D E7                        mov dword ptr [rbp - 0x19], ecx
00C70D28  F6 C1 10                        test cl, 0x10
00C70D2B  75 3D                           jne 0x140c70d6a
00C70D2D  48 8B 45 E7                     mov rax, qword ptr [rbp - 0x19]
00C70D31  83 C9 01                        or ecx, 1
00C70D34  48 89 45 E7                     mov qword ptr [rbp - 0x19], rax
00C70D38  41 B9 01 00 00 00               mov r9d, 1
00C70D3E  89 4D E7                        mov dword ptr [rbp - 0x19], ecx
00C70D41  48 8D 0D 10 BF 46 FF            lea rcx, [rip - 0xb940f0]
00C70D48  48 8B 55 E7                     mov rdx, qword ptr [rbp - 0x19]
00C70D4C  45 8D 41 02                     lea r8d, [r9 + 2]
00C70D50  E8 8F D9 8C FF                  call 0x14053e6e4
00C70D55  48 8B 4D E7                     mov rcx, qword ptr [rbp - 0x19]
00C70D59  4C 8D 05 F8 BE 46 FF            lea r8, [rip - 0xb94108]
00C70D60  BA 03 00 00 00                  mov edx, 3
00C70D65  E8 0A DA 8C FF                  call 0x14053e774
00C70D6A  44 38 2D 4E 5D 35 00            cmp byte ptr [rip + 0x355d4e], r13b
00C70D71  C6 05 1D 5D 35 00 01            mov byte ptr [rip + 0x355d1d], 1
00C70D78  74 5F                           je 0x140c70dd9
00C70D7A  44 39 2D AF 42 35 00            cmp dword ptr [rip + 0x3542af], r13d
00C70D81  75 4F                           jne 0x140c70dd2
00C70D83  8B 0D 87 38 35 00               mov ecx, dword ptr [rip + 0x353887]
00C70D89  4C 89 6D E7                     mov qword ptr [rbp - 0x19], r13
00C70D8D  89 4D E7                        mov dword ptr [rbp - 0x19], ecx
00C70D90  F6 C1 10                        test cl, 0x10
00C70D93  75 3D                           jne 0x140c70dd2
00C70D95  48 8B 45 E7                     mov rax, qword ptr [rbp - 0x19]
00C70D99  83 C9 01                        or ecx, 1
00C70D9C  48 89 45 E7                     mov qword ptr [rbp - 0x19], rax
00C70DA0  41 B9 01 00 00 00               mov r9d, 1
00C70DA6  89 4D E7                        mov dword ptr [rbp - 0x19], ecx
00C70DA9  48 8D 0D E0 BE 46 FF            lea rcx, [rip - 0xb94120]
00C70DB0  48 8B 55 E7                     mov rdx, qword ptr [rbp - 0x19]
00C70DB4  45 8D 41 02                     lea r8d, [r9 + 2]
00C70DB8  E8 27 D9 8C FF                  call 0x14053e6e4
00C70DBD  48 8B 4D E7                     mov rcx, qword ptr [rbp - 0x19]
00C70DC1  4C 8D 05 C8 BE 46 FF            lea r8, [rip - 0xb94138]
00C70DC8  BA 03 00 00 00                  mov edx, 3
00C70DCD  E8 A2 D9 8C FF                  call 0x14053e774
00C70DD2  C6 05 AC 5C 35 00 01            mov byte ptr [rip + 0x355cac], 1
00C70DD9  8B 05 8D 60 35 00               mov eax, dword ptr [rip + 0x35608d]
00C70DDF  85 C0                           test eax, eax
00C70DE1  74 0A                           je 0x140c70ded
00C70DE3  83 F8 01                        cmp eax, 1
00C70DE6  0F 94 05 A8 5C 35 00            sete byte ptr [rip + 0x355ca8]
00C70DED  8B 05 7D 60 35 00               mov eax, dword ptr [rip + 0x35607d]
00C70DF3  85 C0                           test eax, eax
00C70DF5  74 13                           je 0x140c70e0a
00C70DF7  44 38 2D C1 5C 35 00            cmp byte ptr [rip + 0x355cc1], r13b
00C70DFE  74 0A                           je 0x140c70e0a
00C70E00  83 F8 01                        cmp eax, 1
00C70E03  0F 94 05 7B 5C 35 00            sete byte ptr [rip + 0x355c7b]
00C70E0A  F7 05 24 5D 35 00 00 00 04 00   test dword ptr [rip + 0x355d24], 0x40000
00C70E14  B9 F8 43 00 00                  mov ecx, 0x43f8
00C70E19  8B 05 81 5C 35 00               mov eax, dword ptr [rip + 0x355c81]
00C70E1F  49 BE 08 00 00 00 80 F7 FF FF   movabs r14, 0xfffff78000000008
00C70E29  0F 45 C1                        cmovne eax, ecx
00C70E2C  C6 05 C5 5C 35 00 01            mov byte ptr [rip + 0x355cc5], 1
00C70E33  89 05 23 5F 35 00               mov dword ptr [rip + 0x355f23], eax
00C70E39  48 8D 4D FF                     lea rcx, [rbp - 1]
00C70E3D  C6 05 61 5C 35 00 01            mov byte ptr [rip + 0x355c61], 1
00C70E44  48 C7 05 09 62 35 00 B8 0B 00 00  mov qword ptr [rip + 0x356209], 0xbb8
00C70E4F  4D 8B 36                        mov r14, qword ptr [r14]
00C70E52  65 4C 8B 3C 25 20 00 00 00      mov r15, qword ptr gs:[0x20]
00C70E5B  E8 80 D9 70 FF                  call 0x14037e7e0
00C70E60  48 8B 45 FF                     mov rax, qword ptr [rbp - 1]
00C70E64  48 8D 0C 80                     lea rcx, [rax + rax*4]
00C70E68  8B 05 42 11 2B 00               mov eax, dword ptr [rip + 0x2b1142]
00C70E6E  48 89 0D 1B 65 35 00            mov qword ptr [rip + 0x35651b], rcx
00C70E75  48 8D 0D C4 7D 35 00            lea rcx, [rip + 0x357dc4]
00C70E7C  48 8B 04 C1                     mov rax, qword ptr [rcx + rax*8]
00C70E80  C6 40 21 01                     mov byte ptr [rax + 0x21], 1
00C70E84  44 0F 20 C6                     mov rsi, cr8
00C70E88  BA 0F 00 00 00                  mov edx, 0xf
00C70E8D  44 0F 22 C2                     mov cr8, rdx
00C70E91  44 39 2D 88 5E 35 00            cmp dword ptr [rip + 0x355e88], r13d
00C70E98  74 08                           je 0x140c70ea2
00C70E9A  40 8A CE                        mov cl, sil
00C70E9D  E8 5A 48 88 FF                  call 0x1404f56fc
00C70EA2  66 41 C7 87 08 96 00 00 01 00   mov word ptr [r15 + 0x9608], 1
00C70EAC  48 8B 05 35 FC 18 00            mov rax, qword ptr [rip + 0x18fc35]
00C70EB3  44 89 2D 46 E1 35 00            mov dword ptr [rip + 0x35e146], r13d
00C70EBA  E8 11 9C A4 FF                  call 0x1406baad0
00C70EBF  33 C9                           xor ecx, ecx
00C70EC1  E8 2E F2 7C FF                  call 0x1404400f4
00C70EC6  48 8B 05 13 FC 18 00            mov rax, qword ptr [rip + 0x18fc13]
00C70ECD  E8 FE 9B A4 FF                  call 0x1406baad0
00C70ED2  48 8B 05 FF FB 18 00            mov rax, qword ptr [rip + 0x18fbff]
00C70ED9  B1 01                           mov cl, 1
00C70EDB  E8 F0 9B A4 FF                  call 0x1406baad0
00C70EE0  44 8B 0D B9 5B 35 00            mov r9d, dword ptr [rip + 0x355bb9]
00C70EE7  48 8B 0D F2 59 1F 00            mov rcx, qword ptr [rip + 0x1f59f2]
00C70EEE  44 89 0D F7 5C 35 00            mov dword ptr [rip + 0x355cf7], r9d
00C70EF5  44 89 0D BC 5C 35 00            mov dword ptr [rip + 0x355cbc], r9d
00C70EFC  4C 89 35 A5 59 1F 00            mov qword ptr [rip + 0x1f59a5], r14
00C70F03  4C 89 35 A6 59 1F 00            mov qword ptr [rip + 0x1f59a6], r14
00C70F0A  44 89 0D AB 14 2B 00            mov dword ptr [rip + 0x2b14ab], r9d
00C70F11  F6 C1 01                        test cl, 1
00C70F14  74 1D                           je 0x140c70f33
00C70F16  48 8B 05 BB 59 1F 00            mov rax, qword ptr [rip + 0x1f59bb]
00C70F1D  48 85 C0                        test rax, rax
00C70F20  74 0C                           je 0x140c70f2e
00C70F22  48 8D 15 AF 59 1F 00            lea rdx, [rip + 0x1f59af]
00C70F29  48 33 D0                        xor rdx, rax
00C70F2C  EB 0C                           jmp 0x140c70f3a
00C70F2E  48 8B D0                        mov rdx, rax
00C70F31  EB 07                           jmp 0x140c70f3a
00C70F33  48 8B 15 9E 59 1F 00            mov rdx, qword ptr [rip + 0x1f599e]
00C70F3A  0F B6 C9                        movzx ecx, cl
00C70F3D  45 8A C5                        mov r8b, r13b
00C70F40  83 E1 01                        and ecx, 1
00C70F43  48 85 D2                        test rdx, rdx
00C70F46  74 39                           je 0x140c70f81
00C70F48  44 3B 4A 1C                     cmp r9d, dword ptr [rdx + 0x1c]
00C70F4C  73 16                           jae 0x140c70f64
00C70F4E  48 8B 02                        mov rax, qword ptr [rdx]
00C70F51  85 C9                           test ecx, ecx
00C70F53  74 08                           je 0x140c70f5d
00C70F55  48 85 C0                        test rax, rax
00C70F58  74 27                           je 0x140c70f81
00C70F5A  48 33 C2                        xor rax, rdx
00C70F5D  48 85 C0                        test rax, rax
00C70F60  75 17                           jne 0x140c70f79
00C70F62  EB 1D                           jmp 0x140c70f81
00C70F64  48 8B 42 08                     mov rax, qword ptr [rdx + 8]
00C70F68  85 C9                           test ecx, ecx
00C70F6A  74 08                           je 0x140c70f74
00C70F6C  48 85 C0                        test rax, rax
00C70F6F  74 0D                           je 0x140c70f7e
00C70F71  48 33 C2                        xor rax, rdx
00C70F74  48 85 C0                        test rax, rax
00C70F77  74 05                           je 0x140c70f7e
00C70F79  48 8B D0                        mov rdx, rax
00C70F7C  EB CA                           jmp 0x140c70f48
00C70F7E  41 B0 01                        mov r8b, 1
00C70F81  4C 8D 0D 18 14 2B 00            lea r9, [rip + 0x2b1418]
00C70F88  48 8D 0D 49 59 1F 00            lea rcx, [rip + 0x1f5949]
00C70F8F  E8 DC 35 67 FF                  call 0x1402e4570
00C70F94  44 38 2D EA 5A 35 00            cmp byte ptr [rip + 0x355aea], r13b
00C70F9B  C6 05 16 14 2B 00 01            mov byte ptr [rip + 0x2b1416], 1
00C70FA2  74 4E                           je 0x140c70ff2
00C70FA4  44 8B 05 B1 5D 35 00            mov r8d, dword ptr [rip + 0x355db1]
00C70FAB  49 8B D6                        mov rdx, r14
00C70FAE  44 8B 0D 87 5B 35 00            mov r9d, dword ptr [rip + 0x355b87]
00C70FB5  49 F7 D8                        neg r8
00C70FB8  44 88 6C 24 30                  mov byte ptr [rsp + 0x30], r13b
00C70FBD  49 8B CC                        mov rcx, r12
00C70FC0  C6 44 24 28 01                  mov byte ptr [rsp + 0x28], 1
00C70FC5  C7 44 24 20 03 00 00 00         mov dword ptr [rsp + 0x20], 3
00C70FCD  E8 5A CB 72 FF                  call 0x14039db2c
00C70FD2  45 33 C0                        xor r8d, r8d
00C70FD5  49 8B D6                        mov rdx, r14
00C70FD8  49 8B CC                        mov rcx, r12
00C70FDB  E8 3C 57 5C FF                  call 0x14023671c
00C70FE0  B2 01                           mov dl, 1
00C70FE2  49 8B CE                        mov rcx, r14
00C70FE5  E8 06 54 5C FF                  call 0x1402363f0
00C70FEA  8B C0                           mov eax, eax
00C70FEC  48 89 45 F7                     mov qword ptr [rbp - 9], rax
00C70FF0  EB 52                           jmp 0x140c71044
00C70FF2  8B 15 A8 5A 35 00               mov edx, dword ptr [rip + 0x355aa8]
00C70FF8  4C 8D 45 F7                     lea r8, [rbp - 9]
00C70FFC  48 8B 05 ED FA 18 00            mov rax, qword ptr [rip + 0x18faed]
00C71003  33 C9                           xor ecx, ecx
00C71005  E8 C6 9A A4 FF                  call 0x1406baad0
00C7100A  B1 01                           mov cl, 1
00C7100C  E8 E3 F0 7C FF                  call 0x1404400f4
00C71011  4C 8B 55 F7                     mov r10, qword ptr [rbp - 9]
00C71015  8B 05 85 5A 35 00               mov eax, dword ptr [rip + 0x355a85]
00C7101B  44 89 15 5A 5B 35 00            mov dword ptr [rip + 0x355b5a], r10d
00C71022  45 89 97 88 95 00 00            mov dword ptr [r15 + 0x9588], r10d
00C71029  41 89 87 8C 95 00 00            mov dword ptr [r15 + 0x958c], eax
00C71030  48 8B 4D F7                     mov rcx, qword ptr [rbp - 9]
00C71034  49 03 CE                        add rcx, r14
00C71037  89 05 83 0F 2B 00               mov dword ptr [rip + 0x2b0f83], eax
00C7103D  49 89 8F 80 95 00 00            mov qword ptr [r15 + 0x9580], rcx
00C71044  44 39 2D D5 5C 35 00            cmp dword ptr [rip + 0x355cd5], r13d
00C7104B  74 0C                           je 0x140c71059
00C7104D  44 0F 20 C1                     mov rcx, cr8
00C71051  40 8A D6                        mov dl, sil
00C71054  E8 3F 46 88 FF                  call 0x1404f5698
00C71059  40 0F B6 C6                     movzx eax, sil
00C7105D  44 0F 22 C0                     mov cr8, rax
00C71061  8B 05 15 5B 35 00               mov eax, dword ptr [rip + 0x355b15]
00C71067  89 05 E3 0E 2B 00               mov dword ptr [rip + 0x2b0ee3], eax
00C7106D  89 05 E1 0E 2B 00               mov dword ptr [rip + 0x2b0ee1], eax
00C71073  8B 05 47 0F 2B 00               mov eax, dword ptr [rip + 0x2b0f47]
00C71079  89 05 D9 0E 2B 00               mov dword ptr [rip + 0x2b0ed9], eax
00C7107F  89 05 D7 0E 2B 00               mov dword ptr [rip + 0x2b0ed7], eax
00C71085  E9 98 00 00 00                  jmp 0x140c71122
00C7108A  48 8B 8A D8 00 00 00            mov rcx, qword ptr [rdx + 0xd8]
00C71091  48 83 C8 FF                     or rax, 0xffffffffffffffff
00C71095  48 89 05 AC 0E 2B 00            mov qword ptr [rip + 0x2b0eac], rax
00C7109C  48 89 05 C5 0E 2B 00            mov qword ptr [rip + 0x2b0ec5], rax
00C710A3  48 85 C9                        test rcx, rcx
00C710A6  74 1B                           je 0x140c710c3
00C710A8  48 8D 15 B1 A1 00 00            lea rdx, [rip + 0xa1b1]
00C710AF  E8 CC E5 88 FF                  call 0x1404ff680
00C710B4  48 85 C0                        test rax, rax
00C710B7  74 0A                           je 0x140c710c3
00C710B9  C7 05 A1 42 35 00 01 00 00 00   mov dword ptr [rip + 0x3542a1], 1
00C710C3  48 8B 05 06 FA 18 00            mov rax, qword ptr [rip + 0x18fa06]
00C710CA  48 8D 4D 07                     lea rcx, [rbp + 7]
00C710CE  E8 FD 99 A4 FF                  call 0x1406baad0
00C710D3  8A 45 07                        mov al, byte ptr [rbp + 7]
00C710D6  A8 04                           test al, 4
00C710D8  74 07                           je 0x140c710e1
00C710DA  C6 05 DE 59 35 00 01            mov byte ptr [rip + 0x3559de], 1
00C710E1  A8 02                           test al, 2
00C710E3  74 07                           je 0x140c710ec
00C710E5  C6 05 BB 5A 35 00 01            mov byte ptr [rip + 0x355abb], 1
00C710EC  A8 01                           test al, 1
00C710EE  74 07                           je 0x140c710f7
00C710F0  C6 05 E0 5A 35 00 01            mov byte ptr [rip + 0x355ae0], 1
00C710F7  44 38 2D 66 42 35 00            cmp byte ptr [rip + 0x354266], r13b
00C710FE  75 0E                           jne 0x140c7110e
00C71100  A8 08                           test al, 8
00C71102  75 0A                           jne 0x140c7110e
00C71104  C7 05 56 42 35 00 02 00 00 00   mov dword ptr [rip + 0x354256], 2
00C7110E  8B 55 1F                        mov edx, dword ptr [rbp + 0x1f]
00C71111  48 8B 4D 17                     mov rcx, qword ptr [rbp + 0x17]
00C71115  E8 2A 11 94 FF                  call 0x1405b2244
00C7111A  49 8B CC                        mov rcx, r12
00C7111D  E8 F2 0E 94 FF                  call 0x1405b2014
00C71122  48 8B 4D 27                     mov rcx, qword ptr [rbp + 0x27]
00C71126  48 33 CC                        xor rcx, rsp
00C71129  E8 12 B5 A3 FF                  call 0x1406ac640
00C7112E  48 8B B4 24 D0 00 00 00         mov rsi, qword ptr [rsp + 0xd0]
00C71136  48 81 C4 90 00 00 00            add rsp, 0x90
00C7113D  41 5F                           pop r15
00C7113F  41 5E                           pop r14
00C71141  41 5D                           pop r13
00C71143  41 5C                           pop r12
00C71145  5D                              pop rbp
00C71146  C3                              ret
00C71147  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KeInitializeClock(int a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_rsp;
    unsigned __int64 v_stack_m38;
    unsigned __int8 v_stack_m3C;
    unsigned int v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m5F;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int8 v_stack_m88;
    unsigned __int8 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned int v_stack_mB8;
    unsigned __int64 v_stack_p18;

    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (144);
    result = (*(unsigned __int64 *)(v_rip + 1678063)) ^ (v_rsp);
    v_stack_m38 = result;
    result = 0;
    v_r13 = 0;
    v_stack_m48 = 0;
    v_stack_m40 = 0;
    v_stack_m3C = 0;
    v_stack_m68 = 0;
    v_stack_m60 = 0;
    v_stack_m58 = v_xmm0;
    if (a1 == 0) goto loc_00C7108A;
    result = (unsigned int)(((unsigned int)(a1)) - (1));
    if (condition_is_equal) goto loc_00C70D1B;
    if (((unsigned int)(result)) != 1) {
        a2 = v_r13 + 1;
        a3 = a1;
        a1 = a2 + 50;
        v_stack_m98 = 0;
        a4 = 0;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    if ((*(unsigned __int8 *)(v_rip + 3491502)) != 0) goto loc_00C70CFB;
    if ((*(unsigned __int8 *)(v_rip + 3497432)) == 0) goto loc_00C70CCB;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 3497417)))) & (2)) == 0) goto loc_00C70CF2;
loc_00C70CCB:
    v_stack_m70 = 1;
    result = EmClientQueryRuleState(v_rip - 12878085, v_stack_m70, a3, a4);
    if (v_stack_m70 == 2) {
        *(unsigned int *)(v_rip + 3491442) = 3;
    }
    if ((*(unsigned __int8 *)(v_rip + 3491435)) != 0) {
        result = PoTraceDynamicTickDisabled(v_rip - 12878085, v_stack_m70, a3, a4);
        *(unsigned int *)(v_rip + 3498726) = 1;
    }
    *(unsigned __int8 *)(v_rip + 3497646) = 1;
    goto loc_00C71122;
loc_00C70D1B:
    v_stack_m78 = 0;
    v_stack_m78 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3487975)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 3487975)))) & (16)) == 0) {
        result = v_stack_m78;
        a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 3487975))) | (1));
        v_stack_m78 = result;
        a4 = 1;
        v_stack_m78 = a1;
        a1 = v_rip - 12140784;
        a2 = v_stack_m78;
        a3 = a4 + 2;
        result = wil_details_FeatureReporting_ReportUsageToService(a1, a2, a3, a4);
        a1 = v_stack_m78;
        a3 = v_rip - 12140808;
        a2 = 3;
        result = wil_details_FeatureStateCache_TryEnableDeviceUsageFastPath(a1, a2, a3, a4);
    }
    *(unsigned __int8 *)(v_rip + 3497245) = 1;
    if ((*(unsigned __int8 *)(v_rip + 3497294)) == 0) goto loc_00C70DD9;
    if ((*(unsigned int *)(v_rip + 3490479)) != 0) goto loc_00C70DD2;
    v_stack_m78 = 0;
    v_stack_m78 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3487879)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 3487879)))) & (16)) == 0) {
        result = v_stack_m78;
        a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 3487879))) | (1));
        v_stack_m78 = result;
        a4 = 1;
        v_stack_m78 = a1;
        a1 = v_rip - 12140832;
        a2 = v_stack_m78;
        a3 = a4 + 2;
        result = wil_details_FeatureReporting_ReportUsageToService(a1, a2, a3, a4);
        a1 = v_stack_m78;
        a3 = v_rip - 12140856;
        a2 = 3;
        result = wil_details_FeatureStateCache_TryEnableDeviceUsageFastPath(a1, a2, a3, a4);
    }
    *(unsigned __int8 *)(v_rip + 3497132) = 1;
loc_00C70DD9:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3498125))) != 0) {
    }
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3498109))) == 0) goto loc_00C70E0A;
    if ((*(unsigned __int8 *)(v_rip + 3497153)) != 0) {
    }
    result = (unsigned int)(*(unsigned int *)(v_rip + 3497089));
    if (((*(unsigned int *)(v_rip + 3497252)) & (0x40000ULL)) != 0) { result = (unsigned int)((unsigned int)(0x43F8ULL)); }
    *(unsigned __int8 *)(v_rip + 3497157) = 1;
    *(unsigned int *)(v_rip + 3497763) = (unsigned int)(result);
    *(unsigned __int8 *)(v_rip + 3497057) = 1;
    *(unsigned __int64 *)(v_rip + 3498505) = 0xBB8ULL;
    result = KeQueryPerformanceCounter(v_stack_m60, a2, a3, a4);
    *(unsigned __int64 *)(v_rip + 3499291) = v_stack_m60 + v_stack_m60 * 4;
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3505604 + (unsigned int)(*(unsigned int *)(v_rip + 2822466)) * 8) + 33) = 1;
    result = *(unsigned __int64 *)(v_rip + 3505604 + (unsigned int)(*(unsigned int *)(v_rip + 2822466)) * 8);
    if ((*(unsigned int *)(v_rip + 3497608)) != 0) {
        a1 = (unsigned __int8)(v_cr8);
        result = KiRaiseIrqlProcessIrqlFlags(a1, 15, a3, a4);
    }
    *(unsigned __int16 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 38408) = 1;
    *(unsigned int *)(v_rip + 3531078) = 0;
    result = guard_dispatch_icall(a1, 15, a3, a4);
    a1 = 0;
    result = KiSetPendingTick(a1, 15, a3, a4);
    result = guard_dispatch_icall(a1, 15, a3, a4);
    result = guard_dispatch_icall(1, 15, a3, a4);
    *(unsigned int *)(v_rip + 3497207) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3496889)));
    *(unsigned int *)(v_rip + 3497148) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3496889)));
    *(unsigned __int64 *)(v_rip + 2054565) = *(unsigned __int64 *)(v_r14);
    *(unsigned __int64 *)(v_rip + 2054566) = *(unsigned __int64 *)(v_r14);
    *(unsigned int *)(v_rip + 2823339) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3496889)));
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rip + 2054642))) & (1)) == 0) goto loc_00C70F33;
    if (*(unsigned __int64 *)(v_rip + 2054587) == 0) goto loc_00C70F2E;
    a2 = (v_rip + 2054575) ^ (*(unsigned __int64 *)(v_rip + 2054587));
    goto loc_00C70F3A;
loc_00C70F2E:
    goto loc_00C70F3A;
loc_00C70F33:
loc_00C70F3A:
    a1 = (unsigned int)(((unsigned __int8)(*(unsigned __int64 *)(v_rip + 2054642))) & (1));
    if (*(unsigned __int64 *)(v_rip + 2054558) == 0) goto loc_00C70F81;
loc_00C70F48:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3496889)))) >= (*(unsigned int *)(*(unsigned __int64 *)(v_rip + 2054558) + 28))) goto loc_00C70F64;
    if (a1 == 0) goto loc_00C70F5D;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 2054558)) == 0) goto loc_00C70F81;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 2054558))) ^ (*(unsigned __int64 *)(v_rip + 2054558));
loc_00C70F5D:
    if (result != 0) goto loc_00C70F79;
    goto loc_00C70F81;
loc_00C70F64:
    if (a1 == 0) goto loc_00C70F74;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 2054558) + 8) == 0) goto loc_00C70F7E;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 2054558) + 8)) ^ (*(unsigned __int64 *)(v_rip + 2054558));
loc_00C70F74:
    if (result == 0) goto loc_00C70F7E;
loc_00C70F79:
    goto loc_00C70F48;
loc_00C70F7E:
loc_00C70F81:
    result = RtlRbInsertNodeEx(v_rip + 2054473, result, 1, v_rip + 2823192);
    *(unsigned __int8 *)(v_rip + 2823190) = 1;
    if ((*(unsigned __int8 *)(v_rip + 3496682)) == 0) goto loc_00C70FF2;
    a3 = -((unsigned int)(*(unsigned int *)(v_rip + 3497393)));
    v_stack_m88 = 0;
    v_stack_m90 = 1;
    v_stack_m98 = 3;
    result = KiSetClockTimer(*(unsigned __int64 *)(gs_base + (0 + 32)), *(unsigned __int64 *)(v_r14), a3, (unsigned int)(*(unsigned int *)(v_rip + 3496839)));
    a3 = 0;
    result = KiSetClockTimerKTimerDeadlines(*(unsigned __int64 *)(gs_base + (0 + 32)), *(unsigned __int64 *)(v_r14), a3, (unsigned int)(*(unsigned int *)(v_rip + 3496839)));
    result = KiSetNextClockTickDueTime(*(unsigned __int64 *)(v_r14), 1, a3, (unsigned int)(*(unsigned int *)(v_rip + 3496839)));
    v_stack_m68 = (unsigned int)((unsigned int)(result));
    goto loc_00C71044;
loc_00C70FF2:
    a1 = 0;
    result = guard_dispatch_icall(a1, (unsigned int)(*(unsigned int *)(v_rip + 3496616)), v_stack_m68, (unsigned int)(*(unsigned int *)(v_rip + 3496839)));
    result = KiSetPendingTick(1, (unsigned int)(*(unsigned int *)(v_rip + 3496616)), v_stack_m68, (unsigned int)(*(unsigned int *)(v_rip + 3496839)));
    *(unsigned int *)(v_rip + 3496794) = (unsigned int)(v_stack_m68);
    *(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 38280) = (unsigned int)(v_stack_m68);
    *(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 38284) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3496581)));
    a1 = (v_stack_m68) + (*(unsigned __int64 *)(v_r14));
    *(unsigned int *)(v_rip + 2822019) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3496581)));
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 38272) = a1;
loc_00C71044:
    result = (unsigned int)(*(unsigned int *)(v_rip + 3496581));
    if ((*(unsigned int *)(v_rip + 3497173)) != 0) {
        a1 = 15;
        a2 = (unsigned __int8)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, v_stack_m68, (unsigned int)(*(unsigned int *)(v_rip + 3496839)));
    }
    *(unsigned int *)(v_rip + 2821859) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3496725)));
    *(unsigned int *)(v_rip + 2821857) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3496725)));
    *(unsigned int *)(v_rip + 2821849) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 2821959)));
    *(unsigned int *)(v_rip + 2821847) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 2821959)));
    goto loc_00C71122;
loc_00C7108A:
    result = ((unsigned int)(*(unsigned int *)(v_rip + 2821959))) | (-1);
    *(unsigned __int64 *)(v_rip + 2821804) = result;
    *(unsigned __int64 *)(v_rip + 2821829) = result;
    if (*(unsigned __int64 *)(a2 + 216) == 0) goto loc_00C710C3;
    result = strstr(*(unsigned __int64 *)(a2 + 216), v_rip + 41393, v_stack_m68, (unsigned int)(*(unsigned int *)(v_rip + 3496839)));
    if (result != 0) {
        *(unsigned int *)(v_rip + 3490465) = 1;
    }
    result = guard_dispatch_icall(v_stack_m58, v_rip + 41393, v_stack_m68, (unsigned int)(*(unsigned int *)(v_rip + 3496839)));
    if ((((unsigned __int8)(v_stack_m58)) & (4)) != 0) {
        *(unsigned __int8 *)(v_rip + 3496414) = 1;
    }
    if ((((unsigned __int8)(v_stack_m58)) & (2)) != 0) {
        *(unsigned __int8 *)(v_rip + 3496635) = 1;
    }
    if ((((unsigned __int8)(v_stack_m58)) & (1)) != 0) {
        *(unsigned __int8 *)(v_rip + 3496672) = 1;
    }
    if ((*(unsigned __int8 *)(v_rip + 3490406)) != 0) goto loc_00C7110E;
    if ((((unsigned __int8)(v_stack_m58)) & (8)) == 0) {
        *(unsigned int *)(v_rip + 3490390) = 2;
    }
    result = KiSetupTimeIncrement(v_stack_m48, (unsigned int)(v_stack_m40), v_stack_m68, (unsigned int)(*(unsigned int *)(v_rip + 3496839)));
    result = KiInitializeProcessorCycleAccumulation(*(unsigned __int64 *)(gs_base + (0 + 32)), (unsigned int)(v_stack_m40), v_stack_m68, (unsigned int)(*(unsigned int *)(v_rip + 3496839)));
loc_00C71122:
    a1 = (v_stack_m38) ^ (v_rsp);
    result = _security_check_cookie(a1, (unsigned int)(v_stack_m40), v_stack_m68, (unsigned int)(*(unsigned int *)(v_rip + 3496839)));
    v_rsp = (v_rsp) + (144);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KeInitializeClock(int32_t Arg1, void *Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r13;
    int64_t local_rsp;
    uint64_t v_stack_m38;
    uint8_t v_stack_m3C;
    uint32_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m58;
    uint64_t v_stack_m5F;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint8_t v_stack_m88;
    uint8_t v_stack_m90;
    uint64_t v_stack_m98;
    uint32_t v_stack_mB8;
    uint64_t v_stack_p18;

    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (144);
    result = (*(uint64_t *)(v_rip + 0x199AEF)) ^ (local_rsp);
    v_stack_m38 = result;
    result = 0;
    local_r13 = 0;
    v_stack_m48 = 0;
    v_stack_m40 = 0;
    v_stack_m3C = 0;
    v_stack_m68 = 0;
    v_stack_m60 = 0;
    v_stack_m58 = v_xmm0;
    if (Arg1 == 0) goto loc_00C7108A;
    result = (uint32_t)(((uint32_t)(Arg1)) - (1));
    if (condition_is_equal) goto loc_00C70D1B;
    if (((uint32_t)(result)) != 1) {
        Arg2 = local_r13 + 1;
        Arg3 = Arg1;
        Arg1 = Arg2 + 50;
        v_stack_m98 = 0;
        Arg4 = 0;
        result = KeBugCheckEx(Arg1, Arg2, Arg3, Arg4);
    }
    if ((*(uint8_t *)(v_rip + 0x3546AE)) != 0) goto loc_00C70CFB;
    if ((*(uint8_t *)(v_rip + 0x355DD8)) == 0) goto loc_00C70CCB;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x355DC9)))) & (2)) == 0) goto loc_00C70CF2;
loc_00C70CCB:
    v_stack_m70 = 1;
    result = EmClientQueryRuleState(v_rip - 12878085, v_stack_m70, Arg3, Arg4);
    if (v_stack_m70 == 2) {
        *(uint32_t *)(v_rip + 0x354672) = 3;
    }
    if ((*(uint8_t *)(v_rip + 0x35466B)) != 0) {
        result = PoTraceDynamicTickDisabled(v_rip - 12878085, v_stack_m70, Arg3, Arg4);
        *(uint32_t *)(v_rip + 0x3562E6) = 1;
    }
    *(uint8_t *)(v_rip + 0x355EAE) = 1;
    goto loc_00C71122;
loc_00C70D1B:
    v_stack_m78 = 0;
    v_stack_m78 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x3538E7)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x3538E7)))) & (16)) == 0) {
        result = v_stack_m78;
        Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x3538E7))) | (1));
        v_stack_m78 = result;
        Arg4 = 1;
        v_stack_m78 = Arg1;
        Arg1 = v_rip - 12140784;
        Arg2 = v_stack_m78;
        Arg3 = Arg4 + 2;
        result = wil_details_FeatureReporting_ReportUsageToService(Arg1, Arg2, Arg3, Arg4);
        Arg1 = v_stack_m78;
        Arg3 = v_rip - 12140808;
        Arg2 = 3;
        result = wil_details_FeatureStateCache_TryEnableDeviceUsageFastPath(Arg1, Arg2, Arg3, Arg4);
    }
    *(uint8_t *)(v_rip + 0x355D1D) = 1;
    if ((*(uint8_t *)(v_rip + 0x355D4E)) == 0) goto loc_00C70DD9;
    if ((*(uint32_t *)(v_rip + 0x3542AF)) != 0) goto loc_00C70DD2;
    v_stack_m78 = 0;
    v_stack_m78 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x353887)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x353887)))) & (16)) == 0) {
        result = v_stack_m78;
        Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x353887))) | (1));
        v_stack_m78 = result;
        Arg4 = 1;
        v_stack_m78 = Arg1;
        Arg1 = v_rip - 12140832;
        Arg2 = v_stack_m78;
        Arg3 = Arg4 + 2;
        result = wil_details_FeatureReporting_ReportUsageToService(Arg1, Arg2, Arg3, Arg4);
        Arg1 = v_stack_m78;
        Arg3 = v_rip - 12140856;
        Arg2 = 3;
        result = wil_details_FeatureStateCache_TryEnableDeviceUsageFastPath(Arg1, Arg2, Arg3, Arg4);
    }
    *(uint8_t *)(v_rip + 0x355CAC) = 1;
loc_00C70DD9:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x35608D))) != 0) {
    }
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x35607D))) == 0) goto loc_00C70E0A;
    if ((*(uint8_t *)(v_rip + 0x355CC1)) != 0) {
    }
    result = (uint32_t)(*(uint32_t *)(v_rip + 0x355C81));
    if (((*(uint32_t *)(v_rip + 0x355D24)) & (0x40000ULL)) != 0) { result = (uint32_t)((uint32_t)(0x43F8ULL)); }
    *(uint8_t *)(v_rip + 0x355CC5) = 1;
    *(uint32_t *)(v_rip + 0x355F23) = (uint32_t)(result);
    *(uint8_t *)(v_rip + 0x355C61) = 1;
    *(uint64_t *)(v_rip + 0x356209) = 0xBB8ULL;
    result = KeQueryPerformanceCounter(v_stack_m60, Arg2, Arg3, Arg4);
    *(uint64_t *)(v_rip + 0x35651B) = v_stack_m60 + v_stack_m60 * 4;
    *(uint8_t *)(*(uint64_t *)(v_rip + 0x357DC4 + (uint32_t)(*(uint32_t *)(v_rip + 0x2B1142)) * 8) + 0x21) = 1;
    result = *(uint64_t *)(v_rip + 0x357DC4 + (uint32_t)(*(uint32_t *)(v_rip + 0x2B1142)) * 8);
    if ((*(uint32_t *)(v_rip + 0x355E88)) != 0) {
        Arg1 = (uint8_t)(v_cr8);
        result = KiRaiseIrqlProcessIrqlFlags(Arg1, 15, Arg3, Arg4);
    }
    *(uint16_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x9608) = 1;
    *(uint32_t *)(v_rip + 0x35E146) = 0;
    result = guard_dispatch_icall(Arg1, 15, Arg3, Arg4);
    Arg1 = 0;
    result = KiSetPendingTick(Arg1, 15, Arg3, Arg4);
    result = guard_dispatch_icall(Arg1, 15, Arg3, Arg4);
    result = guard_dispatch_icall(1, 15, Arg3, Arg4);
    *(uint32_t *)(v_rip + 0x355CF7) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x355BB9)));
    *(uint32_t *)(v_rip + 0x355CBC) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x355BB9)));
    *(uint64_t *)(v_rip + 0x1F59A5) = *(uint64_t *)(local_r14);
    *(uint64_t *)(v_rip + 0x1F59A6) = *(uint64_t *)(local_r14);
    *(uint32_t *)(v_rip + 0x2B14AB) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x355BB9)));
    if ((((uint8_t)(*(uint64_t *)(v_rip + 0x1F59F2))) & (1)) == 0) goto loc_00C70F33;
    if (*(uint64_t *)(v_rip + 0x1F59BB) == 0) goto loc_00C70F2E;
    Arg2 = (v_rip + 2054575) ^ (*(uint64_t *)(v_rip + 0x1F59BB));
    goto loc_00C70F3A;
loc_00C70F2E:
    goto loc_00C70F3A;
loc_00C70F33:
loc_00C70F3A:
    Arg1 = (uint32_t)(((uint8_t)(*(uint64_t *)(v_rip + 0x1F59F2))) & (1));
    if (*(uint64_t *)(v_rip + 0x1F599E) == 0) goto loc_00C70F81;
loc_00C70F48:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x355BB9)))) >= (*(uint32_t *)(*(uint64_t *)(v_rip + 0x1F599E) + 0x1C))) goto loc_00C70F64;
    if (Arg1 == 0) goto loc_00C70F5D;
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0x1F599E)) == 0) goto loc_00C70F81;
    result = (*(uint64_t *)(*(uint64_t *)(v_rip + 0x1F599E))) ^ (*(uint64_t *)(v_rip + 0x1F599E));
loc_00C70F5D:
    if (result != 0) goto loc_00C70F79;
    goto loc_00C70F81;
loc_00C70F64:
    if (Arg1 == 0) goto loc_00C70F74;
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0x1F599E) + 0x8) == 0) goto loc_00C70F7E;
    result = (*(uint64_t *)(*(uint64_t *)(v_rip + 0x1F599E) + 0x8)) ^ (*(uint64_t *)(v_rip + 0x1F599E));
loc_00C70F74:
    if (result == 0) goto loc_00C70F7E;
loc_00C70F79:
    goto loc_00C70F48;
loc_00C70F7E:
loc_00C70F81:
    result = RtlRbInsertNodeEx(v_rip + 2054473, result, 1, v_rip + 2823192);
    *(uint8_t *)(v_rip + 0x2B1416) = 1;
    if ((*(uint8_t *)(v_rip + 0x355AEA)) == 0) goto loc_00C70FF2;
    Arg3 = -((uint32_t)(*(uint32_t *)(v_rip + 0x355DB1)));
    v_stack_m88 = 0;
    v_stack_m90 = 1;
    v_stack_m98 = 3;
    result = KiSetClockTimer(*(uint64_t *)(gs_base + (0 + 0x20)), *(uint64_t *)(local_r14), Arg3, (uint32_t)(*(uint32_t *)(v_rip + 0x355B87)));
    Arg3 = 0;
    result = KiSetClockTimerKTimerDeadlines(*(uint64_t *)(gs_base + (0 + 0x20)), *(uint64_t *)(local_r14), Arg3, (uint32_t)(*(uint32_t *)(v_rip + 0x355B87)));
    result = KiSetNextClockTickDueTime(*(uint64_t *)(local_r14), 1, Arg3, (uint32_t)(*(uint32_t *)(v_rip + 0x355B87)));
    v_stack_m68 = (uint32_t)((uint32_t)(result));
    goto loc_00C71044;
loc_00C70FF2:
    Arg1 = 0;
    result = guard_dispatch_icall(Arg1, (uint32_t)(*(uint32_t *)(v_rip + 0x355AA8)), v_stack_m68, (uint32_t)(*(uint32_t *)(v_rip + 0x355B87)));
    result = KiSetPendingTick(1, (uint32_t)(*(uint32_t *)(v_rip + 0x355AA8)), v_stack_m68, (uint32_t)(*(uint32_t *)(v_rip + 0x355B87)));
    *(uint32_t *)(v_rip + 0x355B5A) = (uint32_t)(v_stack_m68);
    *(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x9588) = (uint32_t)(v_stack_m68);
    *(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x958C) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x355A85)));
    Arg1 = (v_stack_m68) + (*(uint64_t *)(local_r14));
    *(uint32_t *)(v_rip + 0x2B0F83) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x355A85)));
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x9580) = Arg1;
loc_00C71044:
    result = (uint32_t)(*(uint32_t *)(v_rip + 0x355A85));
    if ((*(uint32_t *)(v_rip + 0x355CD5)) != 0) {
        Arg1 = 15;
        Arg2 = (uint8_t)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, v_stack_m68, (uint32_t)(*(uint32_t *)(v_rip + 0x355B87)));
    }
    *(uint32_t *)(v_rip + 0x2B0EE3) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x355B15)));
    *(uint32_t *)(v_rip + 0x2B0EE1) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x355B15)));
    *(uint32_t *)(v_rip + 0x2B0ED9) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x2B0F47)));
    *(uint32_t *)(v_rip + 0x2B0ED7) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x2B0F47)));
    goto loc_00C71122;
loc_00C7108A:
    result = ((uint32_t)(*(uint32_t *)(v_rip + 0x2B0F47))) | (-1);
    *(uint64_t *)(v_rip + 0x2B0EAC) = result;
    *(uint64_t *)(v_rip + 0x2B0EC5) = result;
    if (*(uint64_t *)(arg2 + 0xD8) == 0) goto loc_00C710C3;
    result = strstr(*(uint64_t *)(arg2 + 0xD8), v_rip + 41393, v_stack_m68, (uint32_t)(*(uint32_t *)(v_rip + 0x355B87)));
    if (result != 0) {
        *(uint32_t *)(v_rip + 0x3542A1) = 1;
    }
    result = guard_dispatch_icall(v_stack_m58, v_rip + 41393, v_stack_m68, (uint32_t)(*(uint32_t *)(v_rip + 0x355B87)));
    if ((((uint8_t)(v_stack_m58)) & (4)) != 0) {
        *(uint8_t *)(v_rip + 0x3559DE) = 1;
    }
    if ((((uint8_t)(v_stack_m58)) & (2)) != 0) {
        *(uint8_t *)(v_rip + 0x355ABB) = 1;
    }
    if ((((uint8_t)(v_stack_m58)) & (1)) != 0) {
        *(uint8_t *)(v_rip + 0x355AE0) = 1;
    }
    if ((*(uint8_t *)(v_rip + 0x354266)) != 0) goto loc_00C7110E;
    if ((((uint8_t)(v_stack_m58)) & (8)) == 0) {
        *(uint32_t *)(v_rip + 0x354256) = 2;
    }
    result = KiSetupTimeIncrement(v_stack_m48, (uint32_t)(v_stack_m40), v_stack_m68, (uint32_t)(*(uint32_t *)(v_rip + 0x355B87)));
    result = KiInitializeProcessorCycleAccumulation(*(uint64_t *)(gs_base + (0 + 0x20)), (uint32_t)(v_stack_m40), v_stack_m68, (uint32_t)(*(uint32_t *)(v_rip + 0x355B87)));
loc_00C71122:
    Arg1 = (v_stack_m38) ^ (local_rsp);
    result = _security_check_cookie(Arg1, (uint32_t)(v_stack_m40), v_stack_m68, (uint32_t)(*(uint32_t *)(v_rip + 0x355B87)));
    local_rsp = (local_rsp) + (144);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0xD8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C70C30&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
