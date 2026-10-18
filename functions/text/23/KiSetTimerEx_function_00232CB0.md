# KiSetTimerEx

- RVA: `0x00232CB0`–`0x002332E0` (길이 `1,584` bytes)
- VA: `0x0000000140232CB0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000604D0`
- 디코드: `368`개 명령, `1,584/1,584` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **20**; 고유 호출 대상: **10**
- 직접 호출자로 확인된 함수: **51**
- RIP 상대 이미지 참조: **10**

### Outgoing calls
- `0x00232EDF` → [KiComputeDueTime](KiComputeDueTime_function_002332E8.md) (function, `0x002332E8`)
- `0x00232F08` → [KiInsertTimerTable](KiInsertTimerTable_function_00233400.md) (function, `0x00233400`)
- `0x00232F38` → [KiExitDispatcher](../25/KiExitDispatcher_function_00251CF0.md) (function, `0x00251CF0`)
- `0x00232F4C` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00232F76` → [KiTimerWaitTest](KiTimerWaitTest_function_002337D0.md) (function, `0x002337D0`)
- `0x00232F9C` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x00233126` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00233136` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x002331C8` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x002331D3` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x002331E8` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x002331F8` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00233210` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0023321F` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00233237` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00233246` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0023325E` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0023326E` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x002332B4` → [EtwTraceKernelEvent](EtwTraceKernelEvent_function_00235350.md) (function, `0x00235350`)
- `0x002332C7` → [KiTraceSetTimer](../22/KiTraceSetTimer_function_0022FB08.md) (function, `0x0022FB08`)

### Direct callers
- [CcRescheduleLazyWriteScanOnVolume](../22/CcRescheduleLazyWriteScanOnVolume_function_0022FE00.md) at `0x0022FEA2`
- [KeSetCoalescableTimer](../22/KeSetCoalescableTimer_function_0022FFD0.md) at `0x0022FFFC`
- [KeSetTimerEx](KeSetTimerEx_function_00231170.md) at `0x0023117C`
- [PopFxEnableWorkOrderWatchdog](../2B/PopFxEnableWorkOrderWatchdog_function_002BD268.md) at `0x002BD2BB`
- [MiRebuildLargePagesThread](../37/MiRebuildLargePagesThread_function_00379AC0.md) at `0x00379C35`
- [CcScheduleLazyWriteScan](../3C/CcScheduleLazyWriteScan_function_003CBD20.md) at `0x003CBE3B`
- [CcScheduleLazyWriteScan](../3C/CcScheduleLazyWriteScan_function_003CBD20.md) at `0x003CBE8F`
- [CcNotifyWriteBehindVolume](../3C/CcNotifyWriteBehindVolume_function_003CC134.md) at `0x003CC1D6`
- [PopEnableIrpWatchdog](../44/PopEnableIrpWatchdog_function_00447BFC.md) at `0x00447CEF`
- [PopSetWatchdog](../46/PopSetWatchdog_function_00460CAC.md) at `0x00460E6D`
- [MiSetDeleteOnCloseTimer](../46/MiSetDeleteOnCloseTimer_function_00464A24.md) at `0x00464AA1`
- [PfSnTraceTimerRoutine](../48/PfSnTraceTimerRoutine_function_0048AEC0.md) at `0x0048AFE3`
- [PopCoalescingSetTimer](../48/PopCoalescingSetTimer_function_0048EEC0.md) at `0x0048EF0B`
- [PfSnStartTraceTimer](../49/PfSnStartTraceTimer_function_00499BEC.md) at `0x00499C58`
- [PopSetPowerActionWatchdogState](../4C/PopSetPowerActionWatchdogState_function_004C86B8.md) at `0x004C878B`
- [MiStoreExtendVirtualPagefile](../4F/MiStoreExtendVirtualPagefile_function_004F73AC.md) at `0x004F746D`
- [HalpCmcStartPolling](../4F/HalpCmcStartPolling_function_004F8D40.md) at `0x004F8DBB`
- [HalpTimerSchedulePeriodicQueries](../53/HalpTimerSchedulePeriodicQueries_function_0053D388.md) at `0x0053D492`
- [PfpServiceMainThreadBoost](../5C/PfpServiceMainThreadBoost_function_005CDBB0.md) at `0x005CDC80`
- [DifKeSetTimerExWrapper](../63/DifKeSetTimerExWrapper_function_00632AA0.md) at `0x00632B98`
- [DifKeSetTimerWrapper](../63/DifKeSetTimerWrapper_function_00632C30.md) at `0x00632D1D`
- [sub_006E6264](../6E/Unknown_function_006E6264.md) at `0x006E62FF`
- [sub_006E8616](../6E/Unknown_function_006E8616.md) at `0x006E8653`
- [sub_006EFC5A](../6E/Unknown_function_006EFC5A.md) at `0x006EFCB0`
- [sub_006F4466](../6F/Unknown_function_006F4466.md) at `0x006F44CD`
- [sub_006F8088](../6F/Unknown_function_006F8088.md) at `0x006F80EF`
- [DbgkpWerDeferredWriteRoutine](../../page/71/DbgkpWerDeferredWriteRoutine_function_00712340.md) at `0x007123BF`
- [FsRtlpOplockTryStartBreakAckTimeout](../../page/71/FsRtlpOplockTryStartBreakAckTimeout_function_007158B4.md) at `0x0071593A`
- [PfSnQueueEnablePrefetcherTimer](../../page/75/PfSnQueueEnablePrefetcherTimer_function_00751E60.md) at `0x00751E9A`
- [PopSetSystemAwayMode](../../page/75/PopSetSystemAwayMode_function_0075EF00.md) at `0x0075EFBD`
- [TtmiResetInactivityTimer](../../page/77/TtmiResetInactivityTimer_function_0077CCF0.md) at `0x0077CD2B`
- [TtmpResetEvaluationTimer](../../page/77/TtmpResetEvaluationTimer_function_0077D4E4.md) at `0x0077D51F`
- [CmpCmdInit](../../page/7E/CmpCmdInit_function_007E5768.md) at `0x007E580D`
- [CmFreezeRegistry](../../page/7E/CmFreezeRegistry_function_007E834C.md) at `0x007E847F`
- [CmpLazyCommitWorker](../../page/7E/CmpLazyCommitWorker_function_007EE030.md) at `0x007EE1C6`
- [PiDrvDbNodeActionCallback](../../page/93/PiDrvDbNodeActionCallback_function_00931980.md) at `0x00931AA0`
- [PfSnPowerBoost](../../page/93/PfSnPowerBoost_function_00939C14.md) at `0x00939C5A`
- [ExpRefreshTimeZoneInformation](../../page/A6/ExpRefreshTimeZoneInformation_function_00A6B46C.md) at `0x00A6B993`
- [ExpRefreshTimeZoneInformation](../../page/A6/ExpRefreshTimeZoneInformation_function_00A6B46C.md) at `0x00A6B9FF`
- [ExpRefreshTimeZoneInformation](../../page/A6/ExpRefreshTimeZoneInformation_function_00A6B46C.md) at `0x00A6BA4C`
- [CmSetLazyFlushState](../../page/AB/CmSetLazyFlushState_function_00AB7824.md) at `0x00AB78C1`
- [CmpDelayFreeCmRm](../../page/AC/CmpDelayFreeCmRm_function_00AC71B8.md) at `0x00AC7228`
- [PopCancelIgnoreBatteryStatusChange](../../page/AD/PopCancelIgnoreBatteryStatusChange_function_00AD4338.md) at `0x00AD4373`
- [PopBatteryWorker](../../page/AE/PopBatteryWorker_function_00AE1650.md) at `0x00AE1D09`
- [sub_00B30002](../../page/B3/Unknown_function_00B30002.md) at `0x00B3013A`
- [HalpInitGenericErrorSourcePollingRoutine](../../pagelk/B5/HalpInitGenericErrorSourcePollingRoutine_function_00B5E498.md) at `0x00B5E546`
- [PfSnBeginBootPhase](../../pagelk/B6/PfSnBeginBootPhase_function_00B6BAC4.md) at `0x00B6BB37`
- [PopBuildDeviceNotifyList](../../pagelk/B7/PopBuildDeviceNotifyList_function_00B789E8.md) at `0x00B78AD0`
- [PfpStartLoggingHardFaultEvents](../../pagelk/B7/PfpStartLoggingHardFaultEvents_function_00B7D9EC.md) at `0x00B7DA8C`
- [KdpTimeSlipWork](../../pagekd/B8/KdpTimeSlipWork_function_00B88650.md) at `0x00B886BF`
- [ViPendingDelayCompletion](../../pagevrfy/BA/ViPendingDelayCompletion_function_00BA1E78.md) at `0x00BA1F43`
- [ViPendingDelayCompletion](../../pagevrfy/BA/ViPendingDelayCompletion_function_00BA1E78.md) at `0x00BA1FB0`
- [ViShutdownScheduleWatchdog](../../pagevrfy/BA/ViShutdownScheduleWatchdog_function_00BA4DF0.md) at `0x00BA4E51`
- [ViWdStartTimer](../../pagevrfy/BA/ViWdStartTimer_function_00BACD3C.md) at `0x00BACD60`
- [PfSnInitializePrefetcher](../../init/C3/PfSnInitializePrefetcher_function_00C3CC8C.md) at `0x00C3CDD6`

### Static image references
- `0x00232CC7` → RVA `0x00E0A740` (`.data`; read)
- `0x00232CE4` → RVA `0x00FC6F78` (`ALMOSTRO`; read)
- `0x00232CEE` → RVA `0x00FC7250` (`ALMOSTRO`; read)
- `0x00232D2F` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x00232D50` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x00232DBB` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x00232E6E` → RVA `0x00FC6B08` (`ALMOSTRO`; read)
- `0x00232E83` → RVA `0x00FC6C48` (`ALMOSTRO`; read)
- `0x00233024` → RVA `0x00FC5030` (`ALMOSTRO`; read)
- `0x00233118` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00232CB0  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
00232CB5  55                              push rbp
00232CB6  56                              push rsi
00232CB7  57                              push rdi
00232CB8  41 54                           push r12
00232CBA  41 55                           push r13
00232CBC  41 56                           push r14
00232CBE  41 57                           push r15
00232CC0  48 81 EC 90 00 00 00            sub rsp, 0x90
00232CC7  48 8B 05 72 7A BD 00            mov rax, qword ptr [rip + 0xbd7a72]
00232CCE  48 33 C4                        xor rax, rsp
00232CD1  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
00232CD9  4C 8B B4 24 F0 00 00 00         mov r14, qword ptr [rsp + 0xf0]
00232CE1  48 8B F9                        mov rdi, rcx
00232CE4  48 8B 05 8D 42 D9 00            mov rax, qword ptr [rip + 0xd9428d]
00232CEB  49 8B EE                        mov rbp, r14
00232CEE  48 33 2D 5B 45 D9 00            xor rbp, qword ptr [rip + 0xd9455b]
00232CF5  48 8B DA                        mov rbx, rdx
00232CF8  48 0F CD                        bswap rbp
00232CFB  48 33 E9                        xor rbp, rcx
00232CFE  44 88 4C 24 30                  mov byte ptr [rsp + 0x30], r9b
00232D03  8B C8                           mov ecx, eax
00232D05  44 89 44 24 4C                  mov dword ptr [rsp + 0x4c], r8d
00232D0A  48 D3 CD                        ror rbp, cl
00232D0D  48 33 E8                        xor rbp, rax
00232D10  4C 89 74 24 68                  mov qword ptr [rsp + 0x68], r14
00232D15  C7 44 24 34 00 00 00 00         mov dword ptr [rsp + 0x34], 0
00232D1D  45 0F 20 C5                     mov r13, cr8
00232D21  4C 89 6C 24 70                  mov qword ptr [rsp + 0x70], r13
00232D26  B8 02 00 00 00                  mov eax, 2
00232D2B  44 0F 22 C0                     mov cr8, rax
00232D2F  83 3D EA 3F D9 00 00            cmp dword ptr [rip + 0xd93fea], 0
00232D36  0F 85 59 02 00 00               jne 0x140232f95
00232D3C  65 4C 8B 3C 25 20 00 00 00      mov r15, qword ptr gs:[0x20]
00232D45  45 33 F6                        xor r14d, r14d
00232D48  4C 89 74 24 58                  mov qword ptr [rsp + 0x58], r14
00232D4D  45 32 E4                        xor r12b, r12b
00232D50  48 8D 15 A9 D2 DC FF            lea rdx, [rip - 0x232d57]
00232D57  F0 0F BA 2F 07                  lock bts dword ptr [rdi], 7
00232D5C  41 8B F6                        mov esi, r14d
00232D5F  0F 82 FB 02 00 00               jb 0x140233060
00232D65  F6 47 03 C0                     test byte ptr [rdi + 3], 0xc0
00232D69  0F 84 FF 00 00 00               je 0x140232e6e
00232D6F  0F B6 4F 02                     movzx ecx, byte ptr [rdi + 2]
00232D73  0F B7 47 38                     movzx eax, word ptr [rdi + 0x38]
00232D77  89 4C 24 48                     mov dword ptr [rsp + 0x48], ecx
00232D7B  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
00232D80  48 8D 71 10                     lea rsi, [rcx + 0x10]
00232D84  4C 8B 8C C2 40 8C FC 00         mov r9, qword ptr [rdx + rax*8 + 0xfc8c40]
00232D8C  0F B7 47 3A                     movzx eax, word ptr [rdi + 0x3a]
00232D90  48 C1 E0 08                     shl rax, 8
00232D94  48 03 F0                        add rsi, rax
00232D97  4C 89 4C 24 40                  mov qword ptr [rsp + 0x40], r9
00232D9C  48 C1 E6 05                     shl rsi, 5
00232DA0  4D 8D 91 00 41 00 00            lea r10, [r9 + 0x4100]
00232DA7  49 03 F2                        add rsi, r10
00232DAA  66 0F 1F 44 00 00               nop word ptr [rax + rax]
00232DB0  F0 48 0F BA 2E 00               lock bts qword ptr [rsi], 0
00232DB6  73 1C                           jae 0x140232dd4
00232DB8  41 FF C6                        inc r14d
00232DBB  44 85 35 EA 24 D9 00            test dword ptr [rip + 0xd924ea], r14d
00232DC2  0F 84 50 03 00 00               je 0x140233118
00232DC8  F3 90                           pause
00232DCA  48 8B 06                        mov rax, qword ptr [rsi]
00232DCD  48 85 C0                        test rax, rax
00232DD0  74 DE                           je 0x140232db0
00232DD2  EB E4                           jmp 0x140232db8
00232DD4  0F B6 47 03                     movzx eax, byte ptr [rdi + 3]
00232DD8  84 C0                           test al, al
00232DDA  0F 88 7F 03 00 00               js 0x14023315f
00232DE0  4C 8B 5C 24 38                  mov r11, qword ptr [rsp + 0x38]
00232DE5  48 8D 57 20                     lea rdx, [rdi + 0x20]
00232DE9  44 0F B7 47 3A                  movzx r8d, word ptr [rdi + 0x3a]
00232DEE  4C 8B 64 24 40                  mov r12, qword ptr [rsp + 0x40]
00232DF3  41 8B C0                        mov eax, r8d
00232DF6  48 8B 0A                        mov rcx, qword ptr [rdx]
00232DF9  48 C1 E0 08                     shl rax, 8
00232DFD  4D 8D 6B 10                     lea r13, [r11 + 0x10]
00232E01  4C 03 E8                        add r13, rax
00232E04  4D 8D 4B 10                     lea r9, [r11 + 0x10]
00232E08  49 C1 E5 05                     shl r13, 5
00232E0C  4D 8D 94 24 00 41 00 00         lea r10, [r12 + 0x4100]
00232E14  41 8B C0                        mov eax, r8d
00232E17  4D 03 EA                        add r13, r10
00232E1A  48 83 F0 01                     xor rax, 1
00232E1E  48 C1 E0 08                     shl rax, 8
00232E22  4C 03 C8                        add r9, rax
00232E25  48 8B 42 08                     mov rax, qword ptr [rdx + 8]
00232E29  49 C1 E1 05                     shl r9, 5
00232E2D  4D 03 CA                        add r9, r10
00232E30  4C 89 4C 24 50                  mov qword ptr [rsp + 0x50], r9
00232E35  48 39 51 08                     cmp qword ptr [rcx + 8], rdx
00232E39  75 05                           jne 0x140232e40
00232E3B  48 39 10                        cmp qword ptr [rax], rdx
00232E3E  74 07                           je 0x140232e47
00232E40  B9 03 00 00 00                  mov ecx, 3
00232E45  CD 29                           int 0x29
00232E47  48 89 08                        mov qword ptr [rax], rcx
00232E4A  48 89 41 08                     mov qword ptr [rcx + 8], rax
00232E4E  48 3B C1                        cmp rax, rcx
00232E51  0F 84 4F 01 00 00               je 0x140232fa6
00232E57  F0 48 83 26 00                  lock and qword ptr [rsi], 0
00232E5C  F0 81 27 FF FF FF BF            lock and dword ptr [rdi], 0xbfffffff
00232E63  4C 8B 6C 24 70                  mov r13, qword ptr [rsp + 0x70]
00232E68  41 B4 01                        mov r12b, 1
00232E6B  45 33 F6                        xor r14d, r14d
00232E6E  F7 05 90 3C D9 00 00 00 02 00   test dword ptr [rip + 0xd93c90], 0x20000
00232E78  BE 01 00 00 00                  mov esi, 1
00232E7D  0F 85 F5 03 00 00               jne 0x140233278
00232E83  83 3D BE 3D D9 00 00            cmp dword ptr [rip + 0xd93dbe], 0
00232E8A  0F 85 FD 00 00 00               jne 0x140232f8d
00232E90  41 80 7F 20 00                  cmp byte ptr [r15 + 0x20], 0
00232E95  75 20                           jne 0x140232eb7
00232E97  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00232EA0  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
00232EA7  F7 81 F4 01 00 00 00 10 00 00   test dword ptr [rcx + 0x1f4], 0x1000
00232EB1  0F 85 C6 00 00 00               jne 0x140232f7d
00232EB7  0F B7 D6                        movzx edx, si
00232EBA  44 0F B6 44 24 30               movzx r8d, byte ptr [rsp + 0x30]
00232EC0  4C 8D 4C 24 34                  lea r9, [rsp + 0x34]
00232EC5  B8 3A 00 00 00                  mov eax, 0x3a
00232ECA  48 8B CF                        mov rcx, rdi
00232ECD  66 89 14 01                     mov word ptr [rcx + rax], dx
00232ED1  48 8B D3                        mov rdx, rbx
00232ED4  8B 44 24 4C                     mov eax, dword ptr [rsp + 0x4c]
00232ED8  89 47 3C                        mov dword ptr [rdi + 0x3c], eax
00232EDB  48 89 6F 30                     mov qword ptr [rdi + 0x30], rbp
00232EDF  E8 04 04 00 00                  call 0x1402332e8
00232EE4  85 C0                           test eax, eax
00232EE6  0F 84 81 00 00 00               je 0x140232f6d
00232EEC  44 8B 4C 24 34                  mov r9d, dword ptr [rsp + 0x34]
00232EF1  48 8B D7                        mov rdx, rdi
00232EF4  44 89 77 04                     mov dword ptr [rdi + 4], r14d
00232EF8  49 8B CF                        mov rcx, r15
00232EFB  4C 89 74 24 20                  mov qword ptr [rsp + 0x20], r14
00232F00  4C 8B 74 24 68                  mov r14, qword ptr [rsp + 0x68]
00232F05  4D 8B C6                        mov r8, r14
00232F08  E8 F3 04 00 00                  call 0x140233400
00232F0D  84 C0                           test al, al
00232F0F  74 5C                           je 0x140232f6d
00232F11  F7 05 ED 3B D9 00 00 00 02 00   test dword ptr [rip + 0xd93bed], 0x20000
00232F1B  0F 85 9D 03 00 00               jne 0x1402332be
00232F21  F0 81 27 7F FF FF FF            lock and dword ptr [rdi], 0xffffff7f
00232F28  45 33 C9                        xor r9d, r9d
00232F2B  44 88 6C 24 20                  mov byte ptr [rsp + 0x20], r13b
00232F30  44 8B C6                        mov r8d, esi
00232F33  33 D2                           xor edx, edx
00232F35  49 8B CF                        mov rcx, r15
00232F38  E8 B3 ED 01 00                  call 0x140251cf0
00232F3D  41 0F B6 C4                     movzx eax, r12b
00232F41  48 8B 8C 24 80 00 00 00         mov rcx, qword ptr [rsp + 0x80]
00232F49  48 33 CC                        xor rcx, rsp
00232F4C  E8 EF 96 47 00                  call 0x1406ac640
00232F51  48 8B 9C 24 E0 00 00 00         mov rbx, qword ptr [rsp + 0xe0]
00232F59  48 81 C4 90 00 00 00            add rsp, 0x90
00232F60  41 5F                           pop r15
00232F62  41 5E                           pop r14
00232F64  41 5D                           pop r13
00232F66  41 5C                           pop r12
00232F68  5F                              pop rdi
00232F69  5E                              pop rsi
00232F6A  5D                              pop rbp
00232F6B  C3                              ret
00232F6C  CC                              int3
00232F6D  45 33 C0                        xor r8d, r8d
00232F70  48 8B D7                        mov rdx, rdi
00232F73  49 8B CF                        mov rcx, r15
00232F76  E8 55 08 00 00                  call 0x1402337d0
00232F7B  EB AB                           jmp 0x140232f28
00232F7D  F7 81 FC 05 00 00 00 00 00 04   test dword ptr [rcx + 0x5fc], 0x4000000
00232F87  0F 85 2A FF FF FF               jne 0x140232eb7
00232F8D  41 8B D6                        mov edx, r14d
00232F90  E9 25 FF FF FF                  jmp 0x140232eba
00232F95  0F B6 D0                        movzx edx, al
00232F98  41 0F B6 CD                     movzx ecx, r13b
00232F9C  E8 5B 27 2C 00                  call 0x1404f56fc
00232FA1  E9 96 FD FF FF                  jmp 0x140232d3c
00232FA6  41 C7 45 1C FF FF FF FF         mov dword ptr [r13 + 0x1c], 0xffffffff
00232FAE  66 45 85 C0                     test r8w, r8w
00232FB2  0F 85 D1 00 00 00               jne 0x140233089
00232FB8  4D 8D B3 10 01 00 00            lea r14, [r11 + 0x110]
00232FBF  49 C1 E6 05                     shl r14, 5
00232FC3  4D 03 F2                        add r14, r10
00232FC6  45 33 E4                        xor r12d, r12d
00232FC9  0F 1F 80 00 00 00 00            nop dword ptr [rax]
00232FD0  F0 49 0F BA 2E 00               lock bts qword ptr [r14], 0
00232FD6  73 1C                           jae 0x140232ff4
00232FD8  41 FF C4                        inc r12d
00232FDB  44 85 25 CA 22 D9 00            test dword ptr [rip + 0xd922ca], r12d
00232FE2  0F 84 F2 01 00 00               je 0x1402331da
00232FE8  F3 90                           pause
00232FEA  49 8B 06                        mov rax, qword ptr [r14]
00232FED  48 85 C0                        test rax, rax
00232FF0  74 DE                           je 0x140232fd0
00232FF2  EB E4                           jmp 0x140232fd8
00232FF4  4C 8B 64 24 40                  mov r12, qword ptr [rsp + 0x40]
00232FF9  4C 8B 5C 24 38                  mov r11, qword ptr [rsp + 0x38]
00232FFE  4C 8B 4C 24 50                  mov r9, qword ptr [rsp + 0x50]
00233003  41 83 7D 1C FF                  cmp dword ptr [r13 + 0x1c], -1
00233008  75 44                           jne 0x14023304e
0023300A  41 83 79 1C FF                  cmp dword ptr [r9 + 0x1c], -1
0023300F  75 3D                           jne 0x14023304e
00233011  41 0F B6 84 24 D0 00 00 00      movzx eax, byte ptr [r12 + 0xd0]
0023301A  48 8D 0D DF CF DC FF            lea rcx, [rip - 0x233021]
00233021  48 03 C0                        add rax, rax
00233024  83 3D 05 20 D9 00 00            cmp dword ptr [rip + 0xd92005], 0
0023302B  48 8B 8C C1 28 85 FC 00         mov rcx, qword ptr [rcx + rax*8 + 0xfc8528]
00233033  0F 84 07 01 00 00               je 0x140233140
00233039  8B 44 24 48                     mov eax, dword ptr [rsp + 0x48]
0023303D  49 C1 EB 06                     shr r11, 6
00233041  83 E0 3F                        and eax, 0x3f
00233044  F0 4A 0F B3 04 D9               lock btr qword ptr [rcx + r11*8], rax
0023304A  4A 8D 0C D9                     lea rcx, [rcx + r11*8]
0023304E  F0 49 83 26 00                  lock and qword ptr [r14], 0
00233053  E9 FF FD FF FF                  jmp 0x140232e57
00233058  0F 1F 84 00 00 00 00 00         nop dword ptr [rax + rax]
00233060  FF C6                           inc esi
00233062  85 35 44 22 D9 00               test dword ptr [rip + 0xd92244], esi
00233068  0F 84 94 01 00 00               je 0x140233202
0023306E  F3 90                           pause
00233070  8B 07                           mov eax, dword ptr [rdi]
00233072  84 C0                           test al, al
00233074  78 EA                           js 0x140233060
00233076  F0 0F BA 2F 07                  lock bts dword ptr [rdi], 7
0023307B  72 E3                           jb 0x140233060
0023307D  48 8D 15 7C CF DC FF            lea rdx, [rip - 0x233084]
00233084  E9 DC FC FF FF                  jmp 0x140232d65
00233089  4D 8D 73 10                     lea r14, [r11 + 0x10]
0023308D  49 C1 E6 05                     shl r14, 5
00233091  4D 03 F2                        add r14, r10
00233094  F0 49 0F BA 2E 00               lock bts qword ptr [r14], 0
0023309A  73 04                           jae 0x1402330a0
0023309C  F3 90                           pause
0023309E  EB 09                           jmp 0x1402330a9
002330A0  4D 85 F6                        test r14, r14
002330A3  0F 85 5A FF FF FF               jne 0x140233003
002330A9  F0 48 83 26 00                  lock and qword ptr [rsi], 0
002330AE  33 F6                           xor esi, esi
002330B0  F0 49 0F BA 2E 00               lock bts qword ptr [r14], 0
002330B6  73 1A                           jae 0x1402330d2
002330B8  FF C6                           inc esi
002330BA  85 35 EC 21 D9 00               test dword ptr [rip + 0xd921ec], esi
002330C0  0F 84 63 01 00 00               je 0x140233229
002330C6  F3 90                           pause
002330C8  49 8B 06                        mov rax, qword ptr [r14]
002330CB  48 85 C0                        test rax, rax
002330CE  74 E0                           je 0x1402330b0
002330D0  EB E6                           jmp 0x1402330b8
002330D2  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
002330D7  49 8D 94 24 00 41 00 00         lea rdx, [r12 + 0x4100]
002330DF  48 81 C6 10 01 00 00            add rsi, 0x110
002330E6  48 C1 E6 05                     shl rsi, 5
002330EA  48 03 F2                        add rsi, rdx
002330ED  45 33 E4                        xor r12d, r12d
002330F0  F0 48 0F BA 2E 00               lock bts qword ptr [rsi], 0
002330F6  0F 83 F8 FE FF FF               jae 0x140232ff4
002330FC  41 FF C4                        inc r12d
002330FF  44 85 25 A6 21 D9 00            test dword ptr [rip + 0xd921a6], r12d
00233106  0F 84 44 01 00 00               je 0x140233250
0023310C  F3 90                           pause
0023310E  48 8B 06                        mov rax, qword ptr [rsi]
00233111  48 85 C0                        test rax, rax
00233114  74 DA                           je 0x1402330f0
00233116  EB E4                           jmp 0x1402330fc
00233118  8B 05 9A 39 D9 00               mov eax, dword ptr [rip + 0xd9399a]
0023311E  A8 40                           test al, 0x40
00233120  0F 84 A2 FC FF FF               je 0x140232dc8
00233126  E8 65 C3 0D 00                  call 0x14030f490
0023312B  84 C0                           test al, al
0023312D  0F 84 95 FC FF FF               je 0x140232dc8
00233133  41 8B CE                        mov ecx, r14d
00233136  E8 25 C3 0D 00                  call 0x14030f460
0023313B  E9 8A FC FF FF                  jmp 0x140232dca
00233140  41 0F B6 84 24 D1 00 00 00      movzx eax, byte ptr [r12 + 0xd1]
00233149  49 C1 E3 06                     shl r11, 6
0023314D  49 03 CB                        add rcx, r11
00233150  F0 48 0F B3 01                  lock btr qword ptr [rcx], rax
00233155  F0 49 83 26 00                  lock and qword ptr [r14], 0
0023315A  E9 F8 FC FF FF                  jmp 0x140232e57
0023315F  F0 48 83 26 00                  lock and qword ptr [rsi], 0
00233164  0F B6 47 03                     movzx eax, byte ptr [rdi + 3]
00233168  45 33 F6                        xor r14d, r14d
0023316B  4C 8B 44 24 40                  mov r8, qword ptr [rsp + 0x40]
00233170  83 E0 3F                        and eax, 0x3f
00233173  41 8B CE                        mov ecx, r14d
00233176  49 87 8C C0 00 41 00 00         xchg qword ptr [r8 + rax*8 + 0x4100], rcx
0023317E  48 85 C9                        test rcx, rcx
00233181  0F 85 4A 01 00 00               jne 0x1402332d1
00233187  F0 81 27 7F FF FF FF            lock and dword ptr [rdi], 0xffffff7f
0023318E  0F B6 47 03                     movzx eax, byte ptr [rdi + 3]
00233192  48 8D 15 67 CE DC FF            lea rdx, [rip - 0x233199]
00233199  41 8B F6                        mov esi, r14d
0023319C  84 C0                           test al, al
0023319E  0F 89 B3 FB FF FF               jns 0x140232d57
002331A4  FF C6                           inc esi
002331A6  85 35 00 21 D9 00               test dword ptr [rip + 0xd92100], esi
002331AC  74 10                           je 0x1402331be
002331AE  F3 90                           pause
002331B0  0F B6 47 03                     movzx eax, byte ptr [rdi + 3]
002331B4  84 C0                           test al, al
002331B6  0F 89 94 FB FF FF               jns 0x140232d50
002331BC  EB E6                           jmp 0x1402331a4
002331BE  8B 05 F4 38 D9 00               mov eax, dword ptr [rip + 0xd938f4]
002331C4  A8 40                           test al, 0x40
002331C6  74 E6                           je 0x1402331ae
002331C8  E8 C3 C2 0D 00                  call 0x14030f490
002331CD  84 C0                           test al, al
002331CF  74 DD                           je 0x1402331ae
002331D1  8B CE                           mov ecx, esi
002331D3  E8 88 C2 0D 00                  call 0x14030f460
002331D8  EB D6                           jmp 0x1402331b0
002331DA  8B 05 D8 38 D9 00               mov eax, dword ptr [rip + 0xd938d8]
002331E0  A8 40                           test al, 0x40
002331E2  0F 84 00 FE FF FF               je 0x140232fe8
002331E8  E8 A3 C2 0D 00                  call 0x14030f490
002331ED  84 C0                           test al, al
002331EF  0F 84 F3 FD FF FF               je 0x140232fe8
002331F5  41 8B CC                        mov ecx, r12d
002331F8  E8 63 C2 0D 00                  call 0x14030f460
002331FD  E9 E8 FD FF FF                  jmp 0x140232fea
00233202  8B 05 B0 38 D9 00               mov eax, dword ptr [rip + 0xd938b0]
00233208  A8 40                           test al, 0x40
0023320A  0F 84 5E FE FF FF               je 0x14023306e
00233210  E8 7B C2 0D 00                  call 0x14030f490
00233215  84 C0                           test al, al
00233217  0F 84 51 FE FF FF               je 0x14023306e
0023321D  8B CE                           mov ecx, esi
0023321F  E8 3C C2 0D 00                  call 0x14030f460
00233224  E9 47 FE FF FF                  jmp 0x140233070
00233229  8B 05 89 38 D9 00               mov eax, dword ptr [rip + 0xd93889]
0023322F  A8 40                           test al, 0x40
00233231  0F 84 8F FE FF FF               je 0x1402330c6
00233237  E8 54 C2 0D 00                  call 0x14030f490
0023323C  84 C0                           test al, al
0023323E  0F 84 82 FE FF FF               je 0x1402330c6
00233244  8B CE                           mov ecx, esi
00233246  E8 15 C2 0D 00                  call 0x14030f460
0023324B  E9 78 FE FF FF                  jmp 0x1402330c8
00233250  8B 05 62 38 D9 00               mov eax, dword ptr [rip + 0xd93862]
00233256  A8 40                           test al, 0x40
00233258  0F 84 AE FE FF FF               je 0x14023310c
0023325E  E8 2D C2 0D 00                  call 0x14030f490
00233263  84 C0                           test al, al
00233265  0F 84 A1 FE FF FF               je 0x14023310c
0023326B  41 8B CC                        mov ecx, r12d
0023326E  E8 ED C1 0D 00                  call 0x14030f460
00233273  E9 96 FE FF FF                  jmp 0x14023310e
00233278  45 84 E4                        test r12b, r12b
0023327B  0F 84 02 FC FF FF               je 0x140232e83
00233281  48 8D 44 24 58                  lea rax, [rsp + 0x58]
00233286  48 89 7C 24 58                  mov qword ptr [rsp + 0x58], rdi
0023328B  41 B9 55 0F 00 00               mov r9d, 0xf55
00233291  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
00233296  41 B8 00 00 02 40               mov r8d, 0x40020000
0023329C  48 C7 44 24 78 08 00 00 00      mov qword ptr [rsp + 0x78], 8
002332A5  8B D6                           mov edx, esi
002332A7  C7 44 24 20 02 06 00 00         mov dword ptr [rsp + 0x20], 0x602
002332AF  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
002332B4  E8 97 20 00 00                  call 0x140235350
002332B9  E9 C5 FB FF FF                  jmp 0x140232e83
002332BE  45 33 C0                        xor r8d, r8d
002332C1  49 8B D6                        mov rdx, r14
002332C4  48 8B CF                        mov rcx, rdi
002332C7  E8 3C C8 FF FF                  call 0x14022fb08
002332CC  E9 57 FC FF FF                  jmp 0x140232f28
002332D1  F0 81 27 FF FF FF 00            lock and dword ptr [rdi], 0xffffff
002332D8  41 B4 01                        mov r12b, 1
002332DB  E9 8E FB FF FF                  jmp 0x140232e6e
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiSetTimerEx(__int64 a1, __int64 a2, int a3, unsigned __int8 a4, __int64 a5)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rbp;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned int v_stack_m7C;
    unsigned int v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned int v_stack_m94;
    unsigned __int8 v_stack_m98;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned int v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p78;

    v_stack_p18 = v_rbx;
    v_rsp = (v_rsp) - (144);
    result = (*(unsigned __int64 *)(v_rip + 12417650)) ^ (v_rsp);
    v_stack_m48 = result;
    v_rbp = (a5) ^ (*(unsigned __int64 *)(v_rip + 14239067));
    v_rbp = (v_rbp) ^ (a1);
    v_stack_m98 = a4;
    v_stack_m7C = a3;
    v_rbp = (v_rbp) ^ (*(unsigned __int64 *)(v_rip + 14238349));
    v_stack_m60 = a5;
    v_stack_m94 = 0;
    v_stack_m58 = v_cr8;
    if ((*(unsigned int *)(v_rip + 14237674)) != 0) goto loc_00232F95;
loc_00232D3C:
    v_r14 = 0;
    v_stack_m70 = 0;
    v_r12 = 0;
loc_00232D50:
loc_00232D57:
    if (condition_is_below) goto loc_00233060;
loc_00232D65:
    if (((*(unsigned __int8 *)(a1 + 3)) & (192)) == 0) goto loc_00232E6E;
    v_stack_m80 = (unsigned int)(*(unsigned __int8 *)(a1 + 2));
    v_stack_m90 = *(unsigned __int8 *)(a1 + 2);
    result = (*(unsigned __int16 *)(a1 + 58)) << (8);
    v_rsi = (*(unsigned __int8 *)(a1 + 2) + 16) + (result);
    v_stack_m88 = *(unsigned __int64 *)(v_rip - 2305367 + *(unsigned __int16 *)(a1 + 56) * 8 + 16550976);
    v_rsi = (v_rsi) << (5);
    v_rsi = (v_rsi) + (*(unsigned __int64 *)(v_rip - 2305367 + *(unsigned __int16 *)(a1 + 56) * 8 + 16550976) + 16640);
loc_00232DB0:
    if (condition_is_above_or_equal) goto loc_00232DD4;
loc_00232DB8:
    v_r14 = (unsigned int)((v_r14) + 1);
    if (((*(unsigned int *)(v_rip + 14230762)) & ((unsigned int)(v_r14))) == 0) goto loc_00233118;
loc_00232DC8:
loc_00232DCA:
    if (*(unsigned __int64 *)(v_rsi) == 0) goto loc_00232DB0;
    goto loc_00232DB8;
loc_00232DD4:
    if (sign_flag) goto loc_0023315F;
    result = ((unsigned int)((unsigned int)(*(unsigned __int16 *)(a1 + 58)))) << (8);
    v_r13 = (v_stack_m90 + 16) + (result);
    v_r13 = (v_r13) << (5);
    v_r13 = (v_r13) + (v_stack_m88 + 16640);
    result = ((unsigned int)((unsigned int)(*(unsigned __int16 *)(a1 + 58)))) ^ (1);
    result = (result) << (8);
    a4 = (v_stack_m90 + 16) + (result);
    a4 = (a4) << (5);
    a4 = (a4) + (v_stack_m88 + 16640);
    v_stack_m78 = a4;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 8)) != (a1 + 32)) goto loc_00232E40;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32 + 8))) != (a1 + 32)) {
        a1 = 3;
    }
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32 + 8)) = a1;
    *(unsigned __int64 *)(a1 + 8) = *(unsigned __int64 *)(a1 + 32 + 8);
    if ((*(unsigned __int64 *)(a1 + 32 + 8)) == a1) goto loc_00232FA6;
loc_00232E57:
    v_r14 = 0;
loc_00232E6E:
    if (((*(unsigned int *)(v_rip + 14236816)) & (0x20000ULL)) != 0) goto loc_00233278;
loc_00232E83:
    if ((*(unsigned int *)(v_rip + 14237118)) != 0) goto loc_00232F8D;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 32)) != 0) goto loc_00232EB7;
    if (((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 500)) & (0x1000ULL)) != 0) goto loc_00232F7D;
loc_00232EB7:
loc_00232EBA:
    *(unsigned __int16 *)(a1 + 58 * 1) = 1;
    *(unsigned int *)(a1 + 60) = (unsigned int)((unsigned int)(v_stack_m7C));
    *(unsigned __int64 *)(a1 + 48) = v_rbp;
    result = KiComputeDueTime(a1, a2, v_stack_m98, v_stack_m94);
    if ((unsigned int)(result) == 0) goto loc_00232F6D;
    *(unsigned int *)(a1 + 4) = 0;
    v_stack_mA8 = 0;
    result = KiInsertTimerTable(*(unsigned __int64 *)(gs_base + (0 + 32)), a1, v_stack_m60, (unsigned int)(v_stack_m94));
    if ((unsigned __int8)(result) == 0) goto loc_00232F6D;
    if (((*(unsigned int *)(v_rip + 14236653)) & (0x20000ULL)) != 0) goto loc_002332BE;
loc_00232F28:
    a4 = 0;
    v_stack_mA8 = (unsigned __int8)(v_stack_m58);
    a2 = 0;
    result = KiExitDispatcher(*(unsigned __int64 *)(gs_base + (0 + 32)), a2, 1, a4);
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, 1, a4);
    v_rsp = (v_rsp) + (144);
    return result;
loc_00232F6D:
    a3 = 0;
    result = KiTimerWaitTest(*(unsigned __int64 *)(gs_base + (0 + 32)), a1, a3, a4);
    goto loc_00232F28;
loc_00232F7D:
    if (((*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 1532)) & (0x4000000ULL)) != 0) goto loc_00232EB7;
loc_00232F8D:
    goto loc_00232EBA;
loc_00232F95:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(v_stack_m58), (unsigned __int8)(result), a3, a4);
    goto loc_00232D3C;
loc_00232FA6:
    *(unsigned int *)(v_stack_m58 + 28) = 0xFFFFFFFFULL;
    if (0 != 0) goto loc_00233089;
    v_r14 = (v_stack_m90 + 272) << (5);
    v_r14 = (v_r14) + (v_stack_m88 + 16640);
    v_r12 = 0;
loc_00232FD0:
    if (condition_is_above_or_equal) goto loc_00232FF4;
loc_00232FD8:
    v_r12 = (unsigned int)((v_r12) + 1);
    if (((*(unsigned int *)(v_rip + 14230218)) & ((unsigned int)(v_r12))) == 0) goto loc_002331DA;
loc_00232FE8:
loc_00232FEA:
    if (*(unsigned __int64 *)(v_r14) == 0) goto loc_00232FD0;
    goto loc_00232FD8;
loc_00232FF4:
loc_00233003:
    if ((*(unsigned int *)(v_stack_m58 + 28)) != -1) goto loc_0023304E;
    if ((*(unsigned int *)(v_stack_p50 + 28)) != -1) goto loc_0023304E;
    result = (*(unsigned __int8 *)(v_stack_p40 + 208)) + (*(unsigned __int8 *)(v_stack_p40 + 208));
    if ((*(unsigned int *)(v_rip + 14229509)) == 0) goto loc_00233140;
    v_r11 = (v_stack_p38) >> (6);
    result = (unsigned int)(((unsigned int)(v_stack_p48)) & (63));
loc_0023304E:
    goto loc_00232E57;
loc_00233060:
    v_rsi = (unsigned int)((1) + 1);
    if (((*(unsigned int *)(v_rip + 14230084)) & ((unsigned int)(v_rsi))) == 0) goto loc_00233202;
loc_0023306E:
loc_00233070:
    if (sign_flag) goto loc_00233060;
    if (condition_is_below) goto loc_00233060;
    goto loc_00232D65;
loc_00233089:
    v_r14 = (v_r11 + 16) << (5);
    v_r14 = (v_r14) + (v_stack_m88 + 16640);
    if (condition_is_above_or_equal) goto loc_002330A0;
    goto loc_002330A9;
loc_002330A0:
    if (v_r14 != 0) goto loc_00233003;
loc_002330A9:
    v_rsi = 0;
loc_002330B0:
    if (condition_is_above_or_equal) goto loc_002330D2;
loc_002330B8:
    v_rsi = (unsigned int)((v_rsi) + 1);
    if (((*(unsigned int *)(v_rip + 14229996)) & ((unsigned int)(v_rsi))) == 0) goto loc_00233229;
loc_002330C6:
loc_002330C8:
    if (*(unsigned __int64 *)(v_r14) == 0) goto loc_002330B0;
    goto loc_002330B8;
loc_002330D2:
    v_rsi = (v_stack_p38) + (272);
    v_rsi = (v_rsi) << (5);
    v_rsi = (v_rsi) + (v_stack_p40 + 16640);
    v_r12 = 0;
loc_002330F0:
    if (condition_is_above_or_equal) goto loc_00232FF4;
loc_002330FC:
    v_r12 = (unsigned int)((v_r12) + 1);
    if (((*(unsigned int *)(v_rip + 14229926)) & ((unsigned int)(v_r12))) == 0) goto loc_00233250;
loc_0023310C:
loc_0023310E:
    if (*(unsigned __int64 *)(v_rsi) == 0) goto loc_002330F0;
    goto loc_002330FC;
loc_00233118:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14236058)))) & (64)) == 0) goto loc_00232DC8;
    result = KiCheckVpBackingLongSpinWaitHypercall(*(unsigned __int64 *)(v_rip - 2306081 + result * 8 + 16549160) + v_r11 * 8, v_stack_p40 + 16640, a3, v_stack_p50);
    if ((unsigned __int8)(result) == 0) goto loc_00232DC8;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_r14)), v_stack_p40 + 16640, a3, v_stack_p50);
    goto loc_00232DCA;
loc_00233140:
    v_r11 = (v_r11) << (6);
    a1 = ((unsigned int)((unsigned int)(v_r14))) + (v_r11);
    goto loc_00232E57;
loc_0023315F:
    v_r14 = 0;
    result = (unsigned int)((*(unsigned __int8 *)(a1 + 3)) & (63));
    if (0 != 0) goto loc_002332D1;
    if (!sign_flag) goto loc_00232D57;
loc_002331A4:
    v_rsi = (unsigned int)((0) + 1);
    if (((*(unsigned int *)(v_rip + 14229760)) & ((unsigned int)(v_rsi))) == 0) goto loc_002331BE;
loc_002331AE:
loc_002331B0:
    if (!sign_flag) goto loc_00232D50;
    goto loc_002331A4;
loc_002331BE:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14235892)))) & (64)) == 0) goto loc_002331AE;
    result = KiCheckVpBackingLongSpinWaitHypercall(0, v_rip - 2306457, v_stack_p40, v_stack_p50);
    if ((unsigned __int8)(result) == 0) goto loc_002331AE;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rsi)), v_rip - 2306457, v_stack_p40, v_stack_p50);
    goto loc_002331B0;
loc_002331DA:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14235864)))) & (64)) == 0) goto loc_00232FE8;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned int)((unsigned int)(v_rsi)), v_rip - 2306457, v_stack_p40, v_stack_p50);
    if ((unsigned __int8)(result) == 0) goto loc_00232FE8;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_r12)), v_rip - 2306457, v_stack_p40, v_stack_p50);
    goto loc_00232FEA;
loc_00233202:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14235824)))) & (64)) == 0) goto loc_0023306E;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned int)((unsigned int)(v_r12)), v_rip - 2306457, v_stack_p40, v_stack_p50);
    if ((unsigned __int8)(result) == 0) goto loc_0023306E;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rsi)), v_rip - 2306457, v_stack_p40, v_stack_p50);
    goto loc_00233070;
loc_00233229:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14235785)))) & (64)) == 0) goto loc_002330C6;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned int)((unsigned int)(v_rsi)), v_rip - 2306457, v_stack_p40, v_stack_p50);
    if ((unsigned __int8)(result) == 0) goto loc_002330C6;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rsi)), v_rip - 2306457, v_stack_p40, v_stack_p50);
    goto loc_002330C8;
loc_00233250:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14235746)))) & (64)) == 0) goto loc_0023310C;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned int)((unsigned int)(v_rsi)), v_rip - 2306457, v_stack_p40, v_stack_p50);
    if ((unsigned __int8)(result) == 0) goto loc_0023310C;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_r12)), v_rip - 2306457, v_stack_p40, v_stack_p50);
    goto loc_0023310E;
loc_00233278:
    if ((unsigned __int8)(v_r12) == 0) goto loc_00232E83;
    v_stack_p58 = a1;
    v_stack_p70 = v_stack_p58;
    v_stack_p78 = 8;
    v_stack_p20 = 0x602ULL;
    result = EtwTraceKernelEvent(v_stack_p70, (unsigned int)((unsigned int)(v_rsi)), (unsigned int)(0x40020000ULL), (unsigned int)(0xF55ULL));
    goto loc_00232E83;
loc_002332BE:
    a3 = 0;
    result = KiTraceSetTimer(a1, 0, a3, (unsigned int)(0xF55ULL));
    goto loc_00232F28;
loc_002332D1:
    goto loc_00232E6E;
}
```

## 5. (Beta) C Style

```c
int64_t KiSetTimerEx(void *Arg1, int64_t Arg2, int32_t Arg3, uint8_t Arg4, int64_t Arg5)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rbp;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint32_t v_stack_m7C;
    uint32_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint32_t v_stack_m94;
    uint8_t v_stack_m98;
    uint64_t v_stack_mA8;
    uint64_t v_stack_p18;
    uint32_t v_stack_p20;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint32_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_p70;
    uint64_t v_stack_p78;

    v_stack_p18 = local_rbx;
    local_rsp = (local_rsp) - (144);
    result = (*(uint64_t *)(v_rip + 0xBD7A72)) ^ (local_rsp);
    v_stack_m48 = result;
    local_rbp = (Arg5) ^ (*(uint64_t *)(v_rip + 0xD9455B));
    local_rbp = (local_rbp) ^ (Arg1);
    v_stack_m98 = Arg4;
    v_stack_m7C = Arg3;
    local_rbp = (local_rbp) ^ (*(uint64_t *)(v_rip + 0xD9428D));
    v_stack_m60 = Arg5;
    v_stack_m94 = 0;
    v_stack_m58 = v_cr8;
    if ((*(uint32_t *)(v_rip + 0xD93FEA)) != 0) goto loc_00232F95;
loc_00232D3C:
    local_r14 = 0;
    v_stack_m70 = 0;
    local_r12 = 0;
loc_00232D50:
loc_00232D57:
    if (condition_is_below) goto loc_00233060;
loc_00232D65:
    if (((*(uint8_t *)(arg1 + 0x3)) & (192)) == 0) goto loc_00232E6E;
    v_stack_m80 = (uint32_t)(*(uint8_t *)(arg1 + 0x2));
    v_stack_m90 = *(uint8_t *)(arg1 + 0x2);
    result = (*(uint16_t *)(arg1 + 0x3A)) << (8);
    local_rsi = (*(uint8_t *)(arg1 + 0x2) + 16) + (result);
    v_stack_m88 = *(uint64_t *)(v_rip - 0x232D57 + *(uint16_t *)(arg1 + 0x38) * 8 + 0xFC8C40);
    local_rsi = (local_rsi) << (5);
    local_rsi = (local_rsi) + (*(uint64_t *)(v_rip - 0x232D57 + *(uint16_t *)(arg1 + 0x38) * 8 + 0xFC8C40) + 16640);
loc_00232DB0:
    if (condition_is_above_or_equal) goto loc_00232DD4;
loc_00232DB8:
    local_r14 = (uint32_t)((local_r14) + 1);
    if (((*(uint32_t *)(v_rip + 0xD924EA)) & ((uint32_t)(local_r14))) == 0) goto loc_00233118;
loc_00232DC8:
loc_00232DCA:
    if (*(uint64_t *)(local_rsi) == 0) goto loc_00232DB0;
    goto loc_00232DB8;
loc_00232DD4:
    if (sign_flag) goto loc_0023315F;
    result = ((uint32_t)((uint32_t)(*(uint16_t *)(arg1 + 0x3A)))) << (8);
    local_r13 = (v_stack_m90 + 16) + (result);
    local_r13 = (local_r13) << (5);
    local_r13 = (local_r13) + (v_stack_m88 + 16640);
    result = ((uint32_t)((uint32_t)(*(uint16_t *)(arg1 + 0x3A)))) ^ (1);
    result = (result) << (8);
    Arg4 = (v_stack_m90 + 16) + (result);
    Arg4 = (Arg4) << (5);
    Arg4 = (Arg4) + (v_stack_m88 + 16640);
    v_stack_m78 = Arg4;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x8)) != (Arg1 + 32)) goto loc_00232E40;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x20 + 0x8))) != (Arg1 + 32)) {
        Arg1 = 3;
    }
    *(void **)(*(uint64_t *)(arg1 + 0x20 + 0x8)) = Arg1;
    *(uint64_t *)(arg1 + 0x8) = *(uint64_t *)(arg1 + 0x20 + 0x8);
    if ((*(uint64_t *)(arg1 + 0x20 + 0x8)) == Arg1) goto loc_00232FA6;
loc_00232E57:
    local_r14 = 0;
loc_00232E6E:
    if (((*(uint32_t *)(v_rip + 0xD93C90)) & (0x20000ULL)) != 0) goto loc_00233278;
loc_00232E83:
    if ((*(uint32_t *)(v_rip + 0xD93DBE)) != 0) goto loc_00232F8D;
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x20)) != 0) goto loc_00232EB7;
    if (((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x1F4)) & (0x1000ULL)) != 0) goto loc_00232F7D;
loc_00232EB7:
loc_00232EBA:
    *(uint16_t *)(arg1 + 0x3A * 1) = 1;
    *(uint32_t *)(arg1 + 0x3C) = (uint32_t)((uint32_t)(v_stack_m7C));
    *(uint64_t *)(arg1 + 0x30) = local_rbp;
    result = KiComputeDueTime(Arg1, Arg2, v_stack_m98, v_stack_m94);
    if ((uint32_t)(result) == 0) goto loc_00232F6D;
    *(uint32_t *)(arg1 + 0x4) = 0;
    v_stack_mA8 = 0;
    result = KiInsertTimerTable(*(uint64_t *)(gs_base + (0 + 0x20)), Arg1, v_stack_m60, (uint32_t)(v_stack_m94));
    if ((uint8_t)(result) == 0) goto loc_00232F6D;
    if (((*(uint32_t *)(v_rip + 0xD93BED)) & (0x20000ULL)) != 0) goto loc_002332BE;
loc_00232F28:
    Arg4 = 0;
    v_stack_mA8 = (uint8_t)(v_stack_m58);
    Arg2 = 0;
    result = KiExitDispatcher(*(uint64_t *)(gs_base + (0 + 0x20)), Arg2, 1, Arg4);
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, 1, Arg4);
    local_rsp = (local_rsp) + (144);
    return result;
loc_00232F6D:
    Arg3 = 0;
    result = KiTimerWaitTest(*(uint64_t *)(gs_base + (0 + 0x20)), Arg1, Arg3, Arg4);
    goto loc_00232F28;
loc_00232F7D:
    if (((*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x5FC)) & (0x4000000ULL)) != 0) goto loc_00232EB7;
loc_00232F8D:
    goto loc_00232EBA;
loc_00232F95:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(v_stack_m58), (uint8_t)(result), Arg3, Arg4);
    goto loc_00232D3C;
loc_00232FA6:
    *(uint32_t *)(v_stack_m58 + 0x1C) = 0xFFFFFFFFULL;
    if (0 != 0) goto loc_00233089;
    local_r14 = (v_stack_m90 + 272) << (5);
    local_r14 = (local_r14) + (v_stack_m88 + 16640);
    local_r12 = 0;
loc_00232FD0:
    if (condition_is_above_or_equal) goto loc_00232FF4;
loc_00232FD8:
    local_r12 = (uint32_t)((local_r12) + 1);
    if (((*(uint32_t *)(v_rip + 0xD922CA)) & ((uint32_t)(local_r12))) == 0) goto loc_002331DA;
loc_00232FE8:
loc_00232FEA:
    if (*(uint64_t *)(local_r14) == 0) goto loc_00232FD0;
    goto loc_00232FD8;
loc_00232FF4:
loc_00233003:
    if ((*(uint32_t *)(v_stack_m58 + 0x1C)) != -1) goto loc_0023304E;
    if ((*(uint32_t *)(v_stack_p50 + 0x1C)) != -1) goto loc_0023304E;
    result = (*(uint8_t *)(v_stack_p40 + 0xD0)) + (*(uint8_t *)(v_stack_p40 + 0xD0));
    if ((*(uint32_t *)(v_rip + 0xD92005)) == 0) goto loc_00233140;
    local_r11 = (v_stack_p38) >> (6);
    result = (uint32_t)(((uint32_t)(v_stack_p48)) & (63));
loc_0023304E:
    goto loc_00232E57;
loc_00233060:
    local_rsi = (uint32_t)((1) + 1);
    if (((*(uint32_t *)(v_rip + 0xD92244)) & ((uint32_t)(local_rsi))) == 0) goto loc_00233202;
loc_0023306E:
loc_00233070:
    if (sign_flag) goto loc_00233060;
    if (condition_is_below) goto loc_00233060;
    goto loc_00232D65;
loc_00233089:
    local_r14 = (local_r11 + 16) << (5);
    local_r14 = (local_r14) + (v_stack_m88 + 16640);
    if (condition_is_above_or_equal) goto loc_002330A0;
    goto loc_002330A9;
loc_002330A0:
    if (local_r14 != 0) goto loc_00233003;
loc_002330A9:
    local_rsi = 0;
loc_002330B0:
    if (condition_is_above_or_equal) goto loc_002330D2;
loc_002330B8:
    local_rsi = (uint32_t)((local_rsi) + 1);
    if (((*(uint32_t *)(v_rip + 0xD921EC)) & ((uint32_t)(local_rsi))) == 0) goto loc_00233229;
loc_002330C6:
loc_002330C8:
    if (*(uint64_t *)(local_r14) == 0) goto loc_002330B0;
    goto loc_002330B8;
loc_002330D2:
    local_rsi = (v_stack_p38) + (272);
    local_rsi = (local_rsi) << (5);
    local_rsi = (local_rsi) + (v_stack_p40 + 16640);
    local_r12 = 0;
loc_002330F0:
    if (condition_is_above_or_equal) goto loc_00232FF4;
loc_002330FC:
    local_r12 = (uint32_t)((local_r12) + 1);
    if (((*(uint32_t *)(v_rip + 0xD921A6)) & ((uint32_t)(local_r12))) == 0) goto loc_00233250;
loc_0023310C:
loc_0023310E:
    if (*(uint64_t *)(local_rsi) == 0) goto loc_002330F0;
    goto loc_002330FC;
loc_00233118:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD9399A)))) & (64)) == 0) goto loc_00232DC8;
    result = KiCheckVpBackingLongSpinWaitHypercall(*(uint64_t *)(v_rip - 0x233021 + result * 8 + 0xFC8528) + local_r11 * 8, v_stack_p40 + 16640, Arg3, v_stack_p50);
    if ((uint8_t)(result) == 0) goto loc_00232DC8;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_r14)), v_stack_p40 + 16640, Arg3, v_stack_p50);
    goto loc_00232DCA;
loc_00233140:
    local_r11 = (local_r11) << (6);
    Arg1 = ((uint32_t)((uint32_t)(local_r14))) + (local_r11);
    goto loc_00232E57;
loc_0023315F:
    local_r14 = 0;
    result = (uint32_t)((*(uint8_t *)(arg1 + 0x3)) & (63));
    if (0 != 0) goto loc_002332D1;
    if (!sign_flag) goto loc_00232D57;
loc_002331A4:
    local_rsi = (uint32_t)((0) + 1);
    if (((*(uint32_t *)(v_rip + 0xD92100)) & ((uint32_t)(local_rsi))) == 0) goto loc_002331BE;
loc_002331AE:
loc_002331B0:
    if (!sign_flag) goto loc_00232D50;
    goto loc_002331A4;
loc_002331BE:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD938F4)))) & (64)) == 0) goto loc_002331AE;
    result = KiCheckVpBackingLongSpinWaitHypercall(0, v_rip - 2306457, v_stack_p40, v_stack_p50);
    if ((uint8_t)(result) == 0) goto loc_002331AE;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rsi)), v_rip - 2306457, v_stack_p40, v_stack_p50);
    goto loc_002331B0;
loc_002331DA:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD938D8)))) & (64)) == 0) goto loc_00232FE8;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint32_t)((uint32_t)(local_rsi)), v_rip - 2306457, v_stack_p40, v_stack_p50);
    if ((uint8_t)(result) == 0) goto loc_00232FE8;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_r12)), v_rip - 2306457, v_stack_p40, v_stack_p50);
    goto loc_00232FEA;
loc_00233202:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD938B0)))) & (64)) == 0) goto loc_0023306E;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint32_t)((uint32_t)(local_r12)), v_rip - 2306457, v_stack_p40, v_stack_p50);
    if ((uint8_t)(result) == 0) goto loc_0023306E;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rsi)), v_rip - 2306457, v_stack_p40, v_stack_p50);
    goto loc_00233070;
loc_00233229:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD93889)))) & (64)) == 0) goto loc_002330C6;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint32_t)((uint32_t)(local_rsi)), v_rip - 2306457, v_stack_p40, v_stack_p50);
    if ((uint8_t)(result) == 0) goto loc_002330C6;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rsi)), v_rip - 2306457, v_stack_p40, v_stack_p50);
    goto loc_002330C8;
loc_00233250:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD93862)))) & (64)) == 0) goto loc_0023310C;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint32_t)((uint32_t)(local_rsi)), v_rip - 2306457, v_stack_p40, v_stack_p50);
    if ((uint8_t)(result) == 0) goto loc_0023310C;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_r12)), v_rip - 2306457, v_stack_p40, v_stack_p50);
    goto loc_0023310E;
loc_00233278:
    if ((uint8_t)(local_r12) == 0) goto loc_00232E83;
    v_stack_p58 = Arg1;
    v_stack_p70 = v_stack_p58;
    v_stack_p78 = 8;
    v_stack_p20 = 0x602ULL;
    result = EtwTraceKernelEvent(v_stack_p70, (uint32_t)((uint32_t)(local_rsi)), (uint32_t)(0x40020000ULL), (uint32_t)(0xF55ULL));
    goto loc_00232E83;
loc_002332BE:
    Arg3 = 0;
    result = KiTraceSetTimer(Arg1, 0, Arg3, (uint32_t)(0xF55ULL));
    goto loc_00232F28;
loc_002332D1:
    goto loc_00232E6E;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x0` | `32` | `R/W` |
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x0 + rax*1` | `16` | `W` |
| `Arg1` | `+ 0x2` | `8` | `R` |
| `Arg1` | `+ 0x3` | `8` | `R` |
| `Arg1` | `+ 0x4` | `32` | `W` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x30` | `64` | `W` |
| `Arg1` | `+ 0x38` | `16` | `R` |
| `Arg1` | `+ 0x3A` | `16` | `R` |
| `Arg1` | `+ 0x3C` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00232CB0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
