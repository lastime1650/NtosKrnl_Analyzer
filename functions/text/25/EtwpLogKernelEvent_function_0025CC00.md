# EtwpLogKernelEvent

- RVA: `0x0025CC00`–`0x0025D8A1` (길이 `3,233` bytes)
- VA: `0x000000014025CC00`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00064094`
- 디코드: `717`개 명령, `3,233/3,233` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **31**; 고유 호출 대상: **25**
- 직접 호출자로 확인된 함수: **54**
- RIP 상대 이미지 참조: **13**

### Outgoing calls
- `0x0025CC69` → [KeAreInterruptsEnabled](../2F/KeAreInterruptsEnabled_function_002F8060.md) (function, `0x002F8060`)
- `0x0025CD3A` → [EtwpReserveTraceBuffer](../2F/EtwpReserveTraceBuffer_function_002FC8C0.md) (function, `0x002FC8C0`)
- `0x0025CECB` → [EtwWriteEx](EtwWriteEx_function_0025F0D0.md) (function, `0x0025F0D0`)
- `0x0025CEE6` → [ExReleaseRundownProtectionCacheAwareEx](ExReleaseRundownProtectionCacheAwareEx_function_0025F050.md) (function, `0x0025F050`)
- `0x0025CEF4` → [KeLeaveCriticalRegionThread](KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x0025CF03` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x0025D075` → [EtwpReserveTraceBuffer](../2F/EtwpReserveTraceBuffer_function_002FC8C0.md) (function, `0x002FC8C0`)
- `0x0025D181` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0025D2CB` → [KeAreInterruptsEnabled](../2F/KeAreInterruptsEnabled_function_002F8060.md) (function, `0x002F8060`)
- `0x0025D2E4` → [MmCanThreadFault](../2F/MmCanThreadFault_function_002F86B0.md) (function, `0x002F86B0`)
- `0x0025D350` → [EtwpTraceStackWalk](../2F/EtwpTraceStackWalk_function_002F8D60.md) (function, `0x002F8D60`)
- `0x0025D370` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0025D378` → [EtwpUpdateEventsLostCount](../3F/EtwpUpdateEventsLostCount_function_003F18E0.md) (function, `0x003F18E0`)
- `0x0025D38B` → [EtwEventEnabled](../39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x0025D3AF` → [EtwpTraceLostSystemEvent](../4C/EtwpTraceLostSystemEvent_function_004C37E4.md) (function, `0x004C37E4`)
- `0x0025D418` → [EtwpQueueApc](../20/EtwpQueueApc_function_00203B7C.md) (function, `0x00203B7C`)
- `0x0025D44C` → [EtwpGetNextEventOffsetType](../4B/EtwpGetNextEventOffsetType_function_004B6F8C.md) (function, `0x004B6F8C`)
- `0x0025D45B` → [KeIsTraceCallbackAllowed](../2F/KeIsTraceCallbackAllowed_function_002FCE6C.md) (function, `0x002FCE6C`)
- `0x0025D487` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0025D4F0` → [EtwpReserveTraceBuffer](../2F/EtwpReserveTraceBuffer_function_002FC8C0.md) (function, `0x002FC8C0`)
- `0x0025D5D3` → [EtwpReserveWithPebsIndex](../41/EtwpReserveWithPebsIndex_function_0041809C.md) (function, `0x0041809C`)
- `0x0025D612` → [EtwpReserveWithPmcCounters](../2F/EtwpReserveWithPmcCounters_function_002FCED0.md) (function, `0x002FCED0`)
- `0x0025D686` → [EtwpSendTraceEvent](../4B/EtwpSendTraceEvent_function_004B6E10.md) (function, `0x004B6E10`)
- `0x0025D731` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0025D7A2` → [KeGetCurrentStackPointer](../6B/KeGetCurrentStackPointer_function_006B1070.md) (function, `0x006B1070`)
- `0x0025D7B6` → [KeQueryCurrentStackInformationEx](../2F/KeQueryCurrentStackInformationEx_function_002F7CD0.md) (function, `0x002F7CD0`)
- `0x0025D7F2` → [ExpInterlockedPopEntrySList](../6B/ExpInterlockedPopEntrySList_function_006BA570.md) (function, `0x006BA570`)
- `0x0025D816` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0025D838` → [ExpInterlockedPushEntrySList](../6B/ExpInterlockedPushEntrySList_function_006BA5B0.md) (function, `0x006BA5B0`)
- `0x0025D845` → [KeGetCurrentStackPointer](../6B/KeGetCurrentStackPointer_function_006B1070.md) (function, `0x006B1070`)
- `0x0025D88E` → [EtwpContextRegisterTracingDispatcher](../4D/EtwpContextRegisterTracingDispatcher_function_004D83F4.md) (function, `0x004D83F4`)

### Direct callers
- [EtwpTraceFileIo](../22/EtwpTraceFileIo_function_00223BB0.md) at `0x00223D11`
- [EtwpTraceFileIo](../22/EtwpTraceFileIo_function_00223BB0.md) at `0x00223F8A`
- [EtwTraceSiloKernelEvent](../22/EtwTraceSiloKernelEvent_function_002242A0.md) at `0x0022433D`
- [EtwTraceSiloKernelEvent](../22/EtwTraceSiloKernelEvent_function_002242A0.md) at `0x002243D8`
- [EtwpTraceIo](../22/EtwpTraceIo_function_00224400.md) at `0x00224575`
- [EtwpTraceIo](../22/EtwpTraceIo_function_00224400.md) at `0x00224782`
- [EtwpTraceFileName](../22/EtwpTraceFileName_function_002251F0.md) at `0x00225306`
- [EtwpTraceFileName](../22/EtwpTraceFileName_function_002251F0.md) at `0x002253B4`
- [EtwpTraceFileName](../22/EtwpTraceFileName_function_002251F0.md) at `0x0022544B`
- [PerfInfoLogSysCallExit](../22/PerfInfoLogSysCallExit_function_00225470.md) at `0x00225516`
- [PerfInfoLogSysCallExit](../22/PerfInfoLogSysCallExit_function_00225470.md) at `0x002255AA`
- [PerfInfoLogSysCallEntry](../22/PerfInfoLogSysCallEntry_function_002255C0.md) at `0x00225666`
- [PerfInfoLogSysCallEntry](../22/PerfInfoLogSysCallEntry_function_002255C0.md) at `0x002256FB`
- [KiProcessExpiredTimerList](../23/KiProcessExpiredTimerList_function_00234200.md) at `0x00234612`
- [sub_0023538B](../23/Unknown_function_0023538B.md) at `0x002353E2`
- [EtwTraceReadyThread](EtwTraceReadyThread_function_00251F70.md) at `0x00252094`
- [EtwTraceReadyThread](EtwTraceReadyThread_function_00251F70.md) at `0x00252180`
- [KiExecuteAllDpcs](KiExecuteAllDpcs_function_0025B740.md) at `0x0025C4EA`
- [EtwTracePool](../2E/EtwTracePool_function_002ECEEC.md) at `0x002ED029`
- [sub_002F8E26](../2F/Unknown_function_002F8E26.md) at `0x002F901E`
- [HvcallFastExtended](../31/HvcallFastExtended_function_003130E0.md) at `0x00313202`
- [HvcallFastExtended](../31/HvcallFastExtended_function_003130E0.md) at `0x003132F2`
- [PerfInfoLogInterrupt](../39/PerfInfoLogInterrupt_function_0039FB00.md) at `0x0039FBD8`
- [sub_003A347B](../3A/Unknown_function_003A347B.md) at `0x003A350F`
- [EtwpLogMemInfo](../3B/EtwpLogMemInfo_function_003B9AC0.md) at `0x003B9C16`
- [EtwpTraceStackKey](../3F/EtwpTraceStackKey_function_003FC290.md) at `0x003FC48B`
- [EtwpTraceStackKey](../3F/EtwpTraceStackKey_function_003FC290.md) at `0x003FC6EE`
- [EtwpTraceStackKey](../3F/EtwpTraceStackKey_function_003FC290.md) at `0x003FC7B1`
- [sub_003FCA13](../3F/Unknown_function_003FCA13.md) at `0x003FCA9B`
- [EtwpTraceCachedStack](../3F/EtwpTraceCachedStack_function_003FCAF0.md) at `0x003FCBAE`
- [EtwpCCSwapFlush](../41/EtwpCCSwapFlush_function_00417F50.md) at `0x00417FE9`
- [EtwpTraceImageUnload](../44/EtwpTraceImageUnload_function_0044C048.md) at `0x0044C1BD`
- [EtwpTraceImageUnload](../44/EtwpTraceImageUnload_function_0044C048.md) at `0x0044C264`
- [PerfInfoLogInterruptHv](../45/PerfInfoLogInterruptHv_function_00450110.md) at `0x004501CC`
- [EtwTraceSiloTimedEvent](../48/EtwTraceSiloTimedEvent_function_00485260.md) at `0x00485314`
- [EtwTraceSiloDcEvent](../48/EtwTraceSiloDcEvent_function_0048B28C.md) at `0x0048B2B1`
- [EtwpTraceKernelEventWithFilter](../49/EtwpTraceKernelEventWithFilter_function_00498540.md) at `0x00498599`
- [PerfInfoLogIpiSend](../4B/PerfInfoLogIpiSend_function_004B7AD0.md) at `0x004B7B85`
- [EtwpTraceContextRegisters](../64/EtwpTraceContextRegisters_function_0064F108.md) at `0x0064F2FC`
- [EtwTraceScbRundown](../65/EtwTraceScbRundown_function_0065006C.md) at `0x006500E7`
- [EtwTraceSchedulingGroupRundown](../65/EtwTraceSchedulingGroupRundown_function_0065018C.md) at `0x006501F8`
- [EtwTraceThreadSchedulingGroupRundown](../65/EtwTraceThreadSchedulingGroupRundown_function_00650430.md) at `0x006504B7`
- [EtwpWriteProcessorTrace](../65/EtwpWriteProcessorTrace_function_00653AB0.md) at `0x00653B25`
- [sub_006D8D90](../6D/Unknown_function_006D8D90.md) at `0x006D8E4C`
- [sub_006DF314](../6D/Unknown_function_006DF314.md) at `0x006DF3AA`
- [sub_006DF902](../6D/Unknown_function_006DF902.md) at `0x006DFAE9`
- [sub_006F5476](../6F/Unknown_function_006F5476.md) at `0x006F54D7`
- [EtwpLogTxREvent](../../page/7B/EtwpLogTxREvent_function_007B86A4.md) at `0x007B8768`
- [EtwLogPfnInfoRundown](../../page/7B/EtwLogPfnInfoRundown_function_007BFDF0.md) at `0x007BFE9F`
- [EtwpClockSourceRunDown](../../page/7B/EtwpClockSourceRunDown_function_007BFEE0.md) at `0x007BFF79`
- [EtwpExecutiveResourceConfigRunDown](../../page/7C/EtwpExecutiveResourceConfigRunDown_function_007C005C.md) at `0x007C00CF`
- [EtwpObjectHandleEnumCallback](../../page/7C/EtwpObjectHandleEnumCallback_function_007C0240.md) at `0x007C042F`
- [EtwpObjectTypeRundown](../../page/7C/EtwpObjectTypeRundown_function_007C04F4.md) at `0x007C05FB`
- [EtwpPoolRunDown](../../page/7C/EtwpPoolRunDown_function_007C0650.md) at `0x007C074E`
- [EtwpPoolRunDown](../../page/7C/EtwpPoolRunDown_function_007C0650.md) at `0x007C0818`
- [EtwpProcessorRundown](../../page/7C/EtwpProcessorRundown_function_007C0868.md) at `0x007C095E`
- [EtwpProcessorRundown](../../page/7C/EtwpProcessorRundown_function_007C0868.md) at `0x007C0A06`
- [EtwpProcessorRundown](../../page/7C/EtwpProcessorRundown_function_007C0868.md) at `0x007C0AA0`
- [EtwpSpinLockConfigRunDown](../../page/7C/EtwpSpinLockConfigRunDown_function_007C0B54.md) at `0x007C0BD1`
- [EtwpSysModuleRunDown](../../page/8A/EtwpSysModuleRunDown_function_008A43C0.md) at `0x008A44D1`
- [EtwpSysModuleRunDown](../../page/8A/EtwpSysModuleRunDown_function_008A43C0.md) at `0x008A451A`
- [EtwpTraceProcessRundown](../../page/8A/EtwpTraceProcessRundown_function_008A5024.md) at `0x008A513E`
- [EtwpProcessPerfCtrsRundown](../../page/8A/EtwpProcessPerfCtrsRundown_function_008A5E08.md) at `0x008A5F10`
- [EtwpEnumerateAddressSpace](../../page/8A/EtwpEnumerateAddressSpace_function_008A7590.md) at `0x008A7A95`
- [EtwpEnumerateAddressSpace](../../page/8A/EtwpEnumerateAddressSpace_function_008A7590.md) at `0x008A7D3F`
- [EtwpLogMemInfoWsHelper](../../page/91/EtwpLogMemInfoWsHelper_function_0091E304.md) at `0x0091E3D9`
- [EtwpLogAlwaysPresentRundown](../../page/9E/EtwpLogAlwaysPresentRundown_function_009E4474.md) at `0x009E44A6`
- [EtwpLogAlwaysPresentRundown](../../page/9E/EtwpLogAlwaysPresentRundown_function_009E4474.md) at `0x009E44D1`
- [EtwpLogGroupMask](../../page/9E/EtwpLogGroupMask_function_009E44E0.md) at `0x009E4547`
- [EtwpSystemImageEnumCallback](../../page/A4/EtwpSystemImageEnumCallback_function_00A42420.md) at `0x00A424B5`
- [EtwpSampledProfileRunDown](../../page/A7/EtwpSampledProfileRunDown_function_00A7F60C.md) at `0x00A7F74B`
- [EtwpLogPmcCounterRundown](../../page/A9/EtwpLogPmcCounterRundown_function_00A95790.md) at `0x00A95917`
- [EtwpLogPmcCounterRundown](../../page/A9/EtwpLogPmcCounterRundown_function_00A95790.md) at `0x00A95A20`

### Static image references
- `0x0025CC1F` → RVA `0x00E0A740` (`.data`; read)
- `0x0025CD99` → RVA `0x00EFF840` (`.data`; read)
- `0x0025CE5C` → RVA `0x000105E0` (`.rdata`; read)
- `0x0025CEAB` → RVA `0x000105E8` (`.rdata`; read)
- `0x0025D3EB` → RVA `0x00227870` (`EtwpStackWalkApc`; read)
- `0x0025D400` → RVA `0x004B8470` (`EtwpCancelStackWalkApc`; read)
- `0x0025D46F` → RVA `0x00FC7408` (`ALMOSTRO`; read)
- `0x0025D669` → RVA `0x00E0AA1C` (`.data`; read)
- `0x0025D672` → RVA `0x00F55CB3` (`.data`; read)
- `0x0025D69A` → RVA `0x00F475DC` (`.data`; read)
- `0x0025D7D9` → RVA `0x00FC6DA0` (`ALMOSTRO`; read)
- `0x0025D7DF` → RVA `0x00E28FB0` (`.data`; read)
- `0x0025D805` → RVA `0x00E00BE8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **3**
  - `0x0025D81D` → [sub_006D8D90 + 0x1A](../6D/Unknown_function_006D8D90.md) (`tail-transfer`)
  - `0x0025D865` → [sub_006D8D90](../6D/Unknown_function_006D8D90.md) (`tail-transfer`)
  - `0x0025D875` → [sub_006D8D90](../6D/Unknown_function_006D8D90.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0025CC00  40 55                           push rbp
0025CC02  56                              push rsi
0025CC03  57                              push rdi
0025CC04  41 54                           push r12
0025CC06  41 55                           push r13
0025CC08  41 56                           push r14
0025CC0A  41 57                           push r15
0025CC0C  48 81 EC 30 01 00 00            sub rsp, 0x130
0025CC13  48 8D 6C 24 40                  lea rbp, [rsp + 0x40]
0025CC18  48 89 9D 48 01 00 00            mov qword ptr [rbp + 0x148], rbx
0025CC1F  48 8B 05 1A DB BA 00            mov rax, qword ptr [rip + 0xbadb1a]
0025CC26  48 33 C5                        xor rax, rbp
0025CC29  48 89 85 E0 00 00 00            mov qword ptr [rbp + 0xe0], rax
0025CC30  0F B7 85 50 01 00 00            movzx eax, word ptr [rbp + 0x150]
0025CC37  0F 57 C0                        xorps xmm0, xmm0
0025CC3A  44 8B A5 58 01 00 00            mov r12d, dword ptr [rbp + 0x158]
0025CC41  45 8B F9                        mov r15d, r9d
0025CC44  66 89 45 00                     mov word ptr [rbp], ax
0025CC48  4C 8B F2                        mov r14, rdx
0025CC4B  33 C0                           xor eax, eax
0025CC4D  41 8B F8                        mov edi, r8d
0025CC50  48 89 45 60                     mov qword ptr [rbp + 0x60], rax
0025CC54  4C 8B E9                        mov r13, rcx
0025CC57  48 89 45 10                     mov qword ptr [rbp + 0x10], rax
0025CC5B  32 DB                           xor bl, bl
0025CC5D  48 89 55 70                     mov qword ptr [rbp + 0x70], rdx
0025CC61  48 89 4D 48                     mov qword ptr [rbp + 0x48], rcx
0025CC65  0F 11 45 50                     movups xmmword ptr [rbp + 0x50], xmm0
0025CC69  E8 F2 B3 09 00                  call 0x1402f8060
0025CC6E  84 C0                           test al, al
0025CC70  74 59                           je 0x14025cccb
0025CC72  44 0F 20 C0                     mov rax, cr8
0025CC76  3C 02                           cmp al, 2
0025CC78  73 51                           jae 0x14025cccb
0025CC7A  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0025CC83  33 D2                           xor edx, edx
0025CC85  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
0025CC8C  90                              nop
0025CC8D  49 8B 86 C0 02 00 00            mov rax, qword ptr [r14 + 0x2c0]
0025CC94  4C 8B 04 F8                     mov r8, qword ptr [rax + rdi*8]
0025CC98  65 8B 04 25 A4 01 00 00         mov eax, dword ptr gs:[0x1a4]
0025CCA0  41 F7 70 14                     div dword ptr [r8 + 0x14]
0025CCA4  41 0F AF 50 10                  imul edx, dword ptr [r8 + 0x10]
0025CCA9  44 8B CA                        mov r9d, edx
0025CCAC  4D 03 08                        add r9, qword ptr [r8]
0025CCAF  41 0F 0D 09                     prefetchw byte ptr [r9]
0025CCB3  49 8B 01                        mov rax, qword ptr [r9]
0025CCB6  A8 01                           test al, 1
0025CCB8  0F 85 2D 02 00 00               jne 0x14025ceeb
0025CCBE  48 8D 48 02                     lea rcx, [rax + 2]
0025CCC2  F0 49 0F B1 09                  lock cmpxchg qword ptr [r9], rcx
0025CCC7  75 ED                           jne 0x14025ccb6
0025CCC9  B3 01                           mov bl, 1
0025CCCB  48 8D 34 FD 00 00 00 00         lea rsi, [rdi*8]
0025CCD3  49 8B BE C8 02 00 00            mov rdi, qword ptr [r14 + 0x2c8]
0025CCDA  48 89 75 40                     mov qword ptr [rbp + 0x40], rsi
0025CCDE  48 8B 3C 3E                     mov rdi, qword ptr [rsi + rdi]
0025CCE2  40 F6 C7 01                     test dil, 1
0025CCE6  0F 85 37 02 00 00               jne 0x14025cf23
0025CCEC  48 85 FF                        test rdi, rdi
0025CCEF  0F 84 04 02 00 00               je 0x14025cef9
0025CCF5  45 33 F6                        xor r14d, r14d
0025CCF8  45 33 D2                        xor r10d, r10d
0025CCFB  45 85 FF                        test r15d, r15d
0025CCFE  0F 85 31 02 00 00               jne 0x14025cf35
0025CD04  41 BD 01 00 00 00               mov r13d, 1
0025CD0A  41 0F BA E4 08                  bt r12d, 8
0025CD0F  0F 82 34 03 00 00               jb 0x14025d049
0025CD15  8B 87 30 03 00 00               mov eax, dword ptr [rdi + 0x330]
0025CD1B  A9 00 0C 00 00                  test eax, 0xc00
0025CD20  0F 85 D9 03 00 00               jne 0x14025d0ff
0025CD26  41 8D 56 10                     lea edx, [r14 + 0x10]
0025CD2A  44 89 64 24 20                  mov dword ptr [rsp + 0x20], r12d
0025CD2F  4C 8D 4D 10                     lea r9, [rbp + 0x10]
0025CD33  48 8B CF                        mov rcx, rdi
0025CD36  4C 8D 45 50                     lea r8, [rbp + 0x50]
0025CD3A  E8 81 FB 09 00                  call 0x1402fc8c0
0025CD3F  44 0F B7 4D 00                  movzx r9d, word ptr [rbp]
0025CD44  48 85 C0                        test rax, rax
0025CD47  74 32                           je 0x14025cd7b
0025CD49  48 8B 4D 10                     mov rcx, qword ptr [rbp + 0x10]
0025CD4D  48 89 48 08                     mov qword ptr [rax + 8], rcx
0025CD51  41 0F B6 CC                     movzx ecx, r12b
0025CD55  81 C9 00 00 11 C0               or ecx, 0xc0110000
0025CD5B  66 44 89 48 06                  mov word ptr [rax + 6], r9w
0025CD60  89 08                           mov dword ptr [rax], ecx
0025CD62  41 8D 4E 10                     lea ecx, [r14 + 0x10]
0025CD66  66 89 48 04                     mov word ptr [rax + 4], cx
0025CD6A  48 83 C0 10                     add rax, 0x10
0025CD6E  48 89 45 20                     mov qword ptr [rbp + 0x20], rax
0025CD72  48 85 C0                        test rax, rax
0025CD75  0F 85 CA 03 00 00               jne 0x14025d145
0025CD7B  41 81 FE F8 FF 00 00            cmp r14d, 0xfff8
0025CD82  0F 87 08 09 00 00               ja 0x14025d690
0025CD88  44 3B 77 08                     cmp r14d, dword ptr [rdi + 8]
0025CD8C  BA 17 00 00 C0                  mov edx, 0xc0000017
0025CD91  B8 05 00 00 80                  mov eax, 0x80000005
0025CD96  0F 47 D0                        cmova edx, eax
0025CD99  4C 8B 05 A0 2A CA 00            mov r8, qword ptr [rip + 0xca2aa0]
0025CDA0  4D 85 C0                        test r8, r8
0025CDA3  0F 84 27 01 00 00               je 0x14025ced0
0025CDA9  49 8B 48 20                     mov rcx, qword ptr [r8 + 0x20]
0025CDAD  83 79 60 00                     cmp dword ptr [rcx + 0x60], 0
0025CDB1  0F 85 2A 03 00 00               jne 0x14025d0e1
0025CDB7  66 41 83 78 66 00               cmp word ptr [r8 + 0x66], 0
0025CDBD  0F 84 0D 01 00 00               je 0x14025ced0
0025CDC3  49 8B 48 28                     mov rcx, qword ptr [r8 + 0x28]
0025CDC7  83 79 60 00                     cmp dword ptr [rcx + 0x60], 0
0025CDCB  0F 84 FF 00 00 00               je 0x14025ced0
0025CDD1  0F B6 41 64                     movzx eax, byte ptr [rcx + 0x64]
0025CDD5  3C 02                           cmp al, 2
0025CDD7  0F 82 82 07 00 00               jb 0x14025d55f
0025CDDD  8B 41 68                        mov eax, dword ptr [rcx + 0x68]
0025CDE0  F6 41 70 40                     test byte ptr [rcx + 0x70], 0x40
0025CDE4  0F 84 E6 00 00 00               je 0x14025ced0
0025CDEA  48 8B 49 78                     mov rcx, qword ptr [rcx + 0x78]
0025CDEE  48 8B C1                        mov rax, rcx
0025CDF1  83 E0 40                        and eax, 0x40
0025CDF4  48 3B C1                        cmp rax, rcx
0025CDF7  0F 85 D3 00 00 00               jne 0x14025ced0
0025CDFD  EB 0F                           jmp 0x14025ce0e
0025CDFF  48 8B 49 78                     mov rcx, qword ptr [rcx + 0x78]
0025CE03  48 8B C1                        mov rax, rcx
0025CE06  83 E0 40                        and eax, 0x40
0025CE09  48 3B C1                        cmp rax, rcx
0025CE0C  75 A9                           jne 0x14025cdb7
0025CE0E  33 C9                           xor ecx, ecx
0025CE10  66 44 89 4D 00                  mov word ptr [rbp], r9w
0025CE15  48 8D 45 00                     lea rax, [rbp]
0025CE19  89 55 18                        mov dword ptr [rbp + 0x18], edx
0025CE1C  48 89 85 80 00 00 00            mov qword ptr [rbp + 0x80], rax
0025CE23  41 0F BA E4 09                  bt r12d, 9
0025CE28  48 8D 45 18                     lea rax, [rbp + 0x18]
0025CE2C  48 C7 85 88 00 00 00 02 00 00 00  mov qword ptr [rbp + 0x88], 2
0025CE37  48 89 85 90 00 00 00            mov qword ptr [rbp + 0x90], rax
0025CE3E  45 8B CD                        mov r9d, r13d
0025CE41  48 8B 87 90 00 00 00            mov rax, qword ptr [rdi + 0x90]
0025CE48  48 89 85 A0 00 00 00            mov qword ptr [rbp + 0xa0], rax
0025CE4F  0F B7 87 88 00 00 00            movzx eax, word ptr [rdi + 0x88]
0025CE56  89 85 A8 00 00 00               mov dword ptr [rbp + 0xa8], eax
0025CE5C  48 8D 05 7D 37 DB FF            lea rax, [rip - 0x24c883]
0025CE63  48 89 85 B0 00 00 00            mov qword ptr [rbp + 0xb0], rax
0025CE6A  B8 05 00 00 00                  mov eax, 5
0025CE6F  44 0F 42 C8                     cmovb r9d, eax
0025CE73  48 C7 85 98 00 00 00 04 00 00 00  mov qword ptr [rbp + 0x98], 4
0025CE7E  89 8D AC 00 00 00               mov dword ptr [rbp + 0xac], ecx
0025CE84  48 C7 85 B8 00 00 00 02 00 00 00  mov qword ptr [rbp + 0xb8], 2
0025CE8F  41 F7 C4 00 06 00 00            test r12d, 0x600
0025CE96  0F 85 FC 09 00 00               jne 0x14025d898
0025CE9C  48 8D 85 80 00 00 00            lea rax, [rbp + 0x80]
0025CEA3  45 33 C0                        xor r8d, r8d
0025CEA6  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0025CEAB  48 8D 15 36 37 DB FF            lea rdx, [rip - 0x24c8ca]
0025CEB2  C7 44 24 30 04 00 00 00         mov dword ptr [rsp + 0x30], 4
0025CEBA  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
0025CEBF  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0025CEC4  48 8B 0D 75 29 CA 00            mov rcx, qword ptr [rip + 0xca2975]
0025CECB  E8 00 22 00 00                  call 0x14025f0d0
0025CED0  84 DB                           test bl, bl
0025CED2  74 25                           je 0x14025cef9
0025CED4  48 8B 4D 70                     mov rcx, qword ptr [rbp + 0x70]
0025CED8  41 8B D5                        mov edx, r13d
0025CEDB  48 8B 89 C0 02 00 00            mov rcx, qword ptr [rcx + 0x2c0]
0025CEE2  48 8B 0C 31                     mov rcx, qword ptr [rcx + rsi]
0025CEE6  E8 65 21 00 00                  call 0x14025f050
0025CEEB  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0025CEF4  E8 F7 20 00 00                  call 0x14025eff0
0025CEF9  48 8B 8D E0 00 00 00            mov rcx, qword ptr [rbp + 0xe0]
0025CF00  48 33 CD                        xor rcx, rbp
0025CF03  E8 38 F7 44 00                  call 0x1406ac640
0025CF08  48 8B 9D 48 01 00 00            mov rbx, qword ptr [rbp + 0x148]
0025CF0F  48 8D A5 F0 00 00 00            lea rsp, [rbp + 0xf0]
0025CF16  41 5F                           pop r15
0025CF18  41 5E                           pop r14
0025CF1A  41 5D                           pop r13
0025CF1C  41 5C                           pop r12
0025CF1E  5F                              pop rdi
0025CF1F  5E                              pop rsi
0025CF20  5D                              pop rbp
0025CF21  C3                              ret
0025CF22  CC                              int3
0025CF23  84 DB                           test bl, bl
0025CF25  74 D2                           je 0x14025cef9
0025CF27  49 8B 8E C0 02 00 00            mov rcx, qword ptr [r14 + 0x2c0]
0025CF2E  BA 01 00 00 00                  mov edx, 1
0025CF33  EB AD                           jmp 0x14025cee2
0025CF35  41 83 FF 08                     cmp r15d, 8
0025CF39  73 27                           jae 0x14025cf62
0025CF3B  41 8B CA                        mov ecx, r10d
0025CF3E  41 8B D7                        mov edx, r15d
0025CF41  48 C1 E1 04                     shl rcx, 4
0025CF45  48 83 C1 08                     add rcx, 8
0025CF49  49 03 CD                        add rcx, r13
0025CF4C  41 2B D2                        sub edx, r10d
0025CF4F  44 03 31                        add r14d, dword ptr [rcx]
0025CF52  48 8D 49 10                     lea rcx, [rcx + 0x10]
0025CF56  48 83 EA 01                     sub rdx, 1
0025CF5A  0F 84 A4 FD FF FF               je 0x14025cd04
0025CF60  EB ED                           jmp 0x14025cf4f
0025CF62  45 8B DF                        mov r11d, r15d
0025CF65  0F 57 E4                        xorps xmm4, xmm4
0025CF68  41 83 E3 F8                     and r11d, 0xfffffff8
0025CF6C  0F 57 ED                        xorps xmm5, xmm5
0025CF6F  41 BE 02 00 00 00               mov r14d, 2
0025CF75  45 8B CA                        mov r9d, r10d
0025CF78  45 8D 46 01                     lea r8d, [r14 + 1]
0025CF7C  4D 03 C0                        add r8, r8
0025CF7F  41 8B D6                        mov edx, r14d
0025CF82  48 03 D2                        add rdx, rdx
0025CF85  41 8D 4E FF                     lea ecx, [r14 - 1]
0025CF89  48 03 C9                        add rcx, rcx
0025CF8C  4D 03 C9                        add r9, r9
0025CF8F  41 83 C2 08                     add r10d, 8
0025CF93  66 43 0F 6E 4C C5 08            movd xmm1, dword ptr [r13 + r8*8 + 8]
0025CF9A  45 8D 46 04                     lea r8d, [r14 + 4]
0025CF9E  66 41 0F 6E 54 D5 08            movd xmm2, dword ptr [r13 + rdx*8 + 8]
0025CFA5  4D 03 C0                        add r8, r8
0025CFA8  66 41 0F 6E 44 CD 08            movd xmm0, dword ptr [r13 + rcx*8 + 8]
0025CFAF  41 8D 56 03                     lea edx, [r14 + 3]
0025CFB3  66 43 0F 6E 5C CD 08            movd xmm3, dword ptr [r13 + r9*8 + 8]
0025CFBA  41 8D 4E 02                     lea ecx, [r14 + 2]
0025CFBE  66 0F 62 D8                     punpckldq xmm3, xmm0
0025CFC2  45 8D 4E 05                     lea r9d, [r14 + 5]
0025CFC6  66 0F 62 D1                     punpckldq xmm2, xmm1
0025CFCA  4D 03 C9                        add r9, r9
0025CFCD  66 0F 6C DA                     punpcklqdq xmm3, xmm2
0025CFD1  48 03 D2                        add rdx, rdx
0025CFD4  66 43 0F 6E 54 C5 08            movd xmm2, dword ptr [r13 + r8*8 + 8]
0025CFDB  66 0F FE E3                     paddd xmm4, xmm3
0025CFDF  48 03 C9                        add rcx, rcx
0025CFE2  41 83 C6 08                     add r14d, 8
0025CFE6  66 43 0F 6E 4C CD 08            movd xmm1, dword ptr [r13 + r9*8 + 8]
0025CFED  66 41 0F 6E 44 D5 08            movd xmm0, dword ptr [r13 + rdx*8 + 8]
0025CFF4  66 0F 62 D1                     punpckldq xmm2, xmm1
0025CFF8  66 41 0F 6E 5C CD 08            movd xmm3, dword ptr [r13 + rcx*8 + 8]
0025CFFF  66 0F 62 D8                     punpckldq xmm3, xmm0
0025D003  66 0F 6C DA                     punpcklqdq xmm3, xmm2
0025D007  66 0F FE DD                     paddd xmm3, xmm5
0025D00B  66 0F 6F EB                     movdqa xmm5, xmm3
0025D00F  45 3B D3                        cmp r10d, r11d
0025D012  0F 82 5D FF FF FF               jb 0x14025cf75
0025D018  66 0F FE E3                     paddd xmm4, xmm3
0025D01C  66 0F 6F C4                     movdqa xmm0, xmm4
0025D020  66 0F 73 D8 08                  psrldq xmm0, 8
0025D025  66 0F FE E0                     paddd xmm4, xmm0
0025D029  66 0F 6F C4                     movdqa xmm0, xmm4
0025D02D  66 0F 73 D8 04                  psrldq xmm0, 4
0025D032  66 0F FE E0                     paddd xmm4, xmm0
0025D036  66 41 0F 7E E6                  movd r14d, xmm4
0025D03B  45 3B D7                        cmp r10d, r15d
0025D03E  0F 82 F7 FE FF FF               jb 0x14025cf3b
0025D044  E9 BB FC FF FF                  jmp 0x14025cd04
0025D049  44 89 64 24 20                  mov dword ptr [rsp + 0x20], r12d
0025D04E  4C 8D 4D 10                     lea r9, [rbp + 0x10]
0025D052  4C 8D 45 50                     lea r8, [rbp + 0x50]
0025D056  48 8B CF                        mov rcx, rdi
0025D059  41 0F BA E4 1C                  bt r12d, 0x1c
0025D05E  0F 82 88 04 00 00               jb 0x14025d4ec
0025D064  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0025D06D  41 8D 56 20                     lea edx, [r14 + 0x20]
0025D071  48 89 45 28                     mov qword ptr [rbp + 0x28], rax
0025D075  E8 46 F8 09 00                  call 0x1402fc8c0
0025D07A  44 0F B7 4D 00                  movzx r9d, word ptr [rbp]
0025D07F  48 8B D0                        mov rdx, rax
0025D082  48 85 C0                        test rax, rax
0025D085  0F 84 F0 FC FF FF               je 0x14025cd7b
0025D08B  4C 8B 45 28                     mov r8, qword ptr [rbp + 0x28]
0025D08F  66 44 89 4A 06                  mov word ptr [rdx + 6], r9w
0025D094  41 0F B6 CC                     movzx ecx, r12b
0025D098  81 C9 00 00 02 C0               or ecx, 0xc0020000
0025D09E  89 08                           mov dword ptr [rax], ecx
0025D0A0  48 8B 4D 10                     mov rcx, qword ptr [rbp + 0x10]
0025D0A4  48 89 48 10                     mov qword ptr [rax + 0x10], rcx
0025D0A8  41 8D 46 20                     lea eax, [r14 + 0x20]
0025D0AC  66 89 42 04                     mov word ptr [rdx + 4], ax
0025D0B0  41 8B 88 10 05 00 00            mov ecx, dword ptr [r8 + 0x510]
0025D0B7  89 4A 08                        mov dword ptr [rdx + 8], ecx
0025D0BA  41 8B 88 08 05 00 00            mov ecx, dword ptr [r8 + 0x508]
0025D0C1  89 4A 0C                        mov dword ptr [rdx + 0xc], ecx
0025D0C4  41 8B 80 8C 02 00 00            mov eax, dword ptr [r8 + 0x28c]
0025D0CB  89 42 18                        mov dword ptr [rdx + 0x18], eax
0025D0CE  41 8B 80 DC 02 00 00            mov eax, dword ptr [r8 + 0x2dc]
0025D0D5  89 42 1C                        mov dword ptr [rdx + 0x1c], eax
0025D0D8  48 8D 42 20                     lea rax, [rdx + 0x20]
0025D0DC  E9 8D FC FF FF                  jmp 0x14025cd6e
0025D0E1  0F B6 41 64                     movzx eax, byte ptr [rcx + 0x64]
0025D0E5  3C 02                           cmp al, 2
0025D0E7  0F 82 6D 02 00 00               jb 0x14025d35a
0025D0ED  8B 41 68                        mov eax, dword ptr [rcx + 0x68]
0025D0F0  F6 41 70 40                     test byte ptr [rcx + 0x70], 0x40
0025D0F4  0F 84 BD FC FF FF               je 0x14025cdb7
0025D0FA  E9 00 FD FF FF                  jmp 0x14025cdff
0025D0FF  0F B7 55 00                     movzx edx, word ptr [rbp]
0025D103  0F BA E0 0A                     bt eax, 0xa
0025D107  0F 82 9E 04 00 00               jb 0x14025d5ab
0025D10D  0F BA E0 0B                     bt eax, 0xb
0025D111  0F 83 0F FC FF FF               jae 0x14025cd26
0025D117  45 33 C0                        xor r8d, r8d
0025D11A  48 8B 87 28 04 00 00            mov rax, qword ptr [rdi + 0x428]
0025D121  8B 48 08                        mov ecx, dword ptr [rax + 8]
0025D124  44 3B C1                        cmp r8d, ecx
0025D127  0F 83 F9 FB FF FF               jae 0x14025cd26
0025D12D  48 8B 87 28 04 00 00            mov rax, qword ptr [rdi + 0x428]
0025D134  66 42 39 54 40 0C               cmp word ptr [rax + r8*2 + 0xc], dx
0025D13A  0F 84 BA 04 00 00               je 0x14025d5fa
0025D140  41 FF C0                        inc r8d
0025D143  EB D5                           jmp 0x14025d11a
0025D145  4C 8B 4D 20                     mov r9, qword ptr [rbp + 0x20]
0025D149  45 8B C6                        mov r8d, r14d
0025D14C  33 C0                           xor eax, eax
0025D14E  89 45 34                        mov dword ptr [rbp + 0x34], eax
0025D151  4C 89 4D 28                     mov qword ptr [rbp + 0x28], r9
0025D155  44 89 45 30                     mov dword ptr [rbp + 0x30], r8d
0025D159  41 3B C7                        cmp eax, r15d
0025D15C  73 3D                           jae 0x14025d19b
0025D15E  48 8B 4D 48                     mov rcx, qword ptr [rbp + 0x48]
0025D162  48 03 C0                        add rax, rax
0025D165  8B 54 C1 08                     mov edx, dword ptr [rcx + rax*8 + 8]
0025D169  4C 8B 14 C1                     mov r10, qword ptr [rcx + rax*8]
0025D16D  41 3B D0                        cmp edx, r8d
0025D170  0F 87 F1 01 00 00               ja 0x14025d367
0025D176  8B F2                           mov esi, edx
0025D178  44 8B C2                        mov r8d, edx
0025D17B  49 8B D2                        mov rdx, r10
0025D17E  49 8B C9                        mov rcx, r9
0025D181  E8 BA 96 46 00                  call 0x1406c6840
0025D186  4C 8B 4D 28                     mov r9, qword ptr [rbp + 0x28]
0025D18A  44 8B 45 30                     mov r8d, dword ptr [rbp + 0x30]
0025D18E  4C 03 CE                        add r9, rsi
0025D191  8B 45 34                        mov eax, dword ptr [rbp + 0x34]
0025D194  44 2B C6                        sub r8d, esi
0025D197  FF C0                           inc eax
0025D199  EB B3                           jmp 0x14025d14e
0025D19B  0F B7 75 00                     movzx esi, word ptr [rbp]
0025D19F  F7 47 0C 00 00 08 00            test dword ptr [rdi + 0xc], 0x80000
0025D1A6  0F 85 BD 04 00 00               jne 0x14025d669
0025D1AC  4C 8B 8F 20 06 00 00            mov r9, qword ptr [rdi + 0x620]
0025D1B3  4D 85 C9                        test r9, r9
0025D1B6  0F 85 77 02 00 00               jne 0x14025d433
0025D1BC  48 8B 45 58                     mov rax, qword ptr [rbp + 0x58]
0025D1C0  0F 0D 08                        prefetchw byte ptr [rax]
0025D1C3  48 8B 00                        mov rax, qword ptr [rax]
0025D1C6  48 8B 55 50                     mov rdx, qword ptr [rbp + 0x50]
0025D1CA  48 8B CA                        mov rcx, rdx
0025D1CD  48 33 C8                        xor rcx, rax
0025D1D0  48 83 F9 0F                     cmp rcx, 0xf
0025D1D4  0F 83 17 04 00 00               jae 0x14025d5f1
0025D1DA  48 8B 55 58                     mov rdx, qword ptr [rbp + 0x58]
0025D1DE  48 8D 48 01                     lea rcx, [rax + 1]
0025D1E2  F0 48 0F B1 0A                  lock cmpxchg qword ptr [rdx], rcx
0025D1E7  75 DD                           jne 0x14025d1c6
0025D1E9  8B 87 30 03 00 00               mov eax, dword ptr [rdi + 0x330]
0025D1EF  84 C0                           test al, al
0025D1F1  78 37                           js 0x14025d22a
0025D1F3  8B 87 34 03 00 00               mov eax, dword ptr [rdi + 0x334]
0025D1F9  A8 02                           test al, 2
0025D1FB  0F 85 20 04 00 00               jne 0x14025d621
0025D201  F7 87 30 03 00 00 00 80 00 00   test dword ptr [rdi + 0x330], 0x8000
0025D20B  0F 85 B1 02 00 00               jne 0x14025d4c2
0025D211  F7 87 30 03 00 00 00 00 00 04   test dword ptr [rdi + 0x330], 0x4000000
0025D21B  0F 85 22 04 00 00               jne 0x14025d643
0025D221  48 8B 75 40                     mov rsi, qword ptr [rbp + 0x40]
0025D225  E9 A6 FC FF FF                  jmp 0x14025ced0
0025D22A  8B CE                           mov ecx, esi
0025D22C  81 E1 FF 1F 00 00               and ecx, 0x1fff
0025D232  8B C1                           mov eax, ecx
0025D234  83 E1 07                        and ecx, 7
0025D237  48 C1 E8 03                     shr rax, 3
0025D23B  48 03 87 18 04 00 00            add rax, qword ptr [rdi + 0x418]
0025D242  0F B6 00                        movzx eax, byte ptr [rax]
0025D245  D2 F8                           sar al, cl
0025D247  41 84 C5                        test r13b, al
0025D24A  74 A7                           je 0x14025d1f3
0025D24C  65 4C 8B 3C 25 88 01 00 00      mov r15, qword ptr gs:[0x188]
0025D255  45 8B F4                        mov r14d, r12d
0025D258  45 0F 20 C2                     mov r10, cr8
0025D25C  4C 89 55 20                     mov qword ptr [rbp + 0x20], r10
0025D260  41 0F BA E4 0E                  bt r12d, 0xe
0025D265  0F 82 4E 01 00 00               jb 0x14025d3b9
0025D26B  41 0F BA E4 0C                  bt r12d, 0xc
0025D270  0F 83 C0 00 00 00               jae 0x14025d336
0025D276  32 C9                           xor cl, cl
0025D278  41 0F BA E4 0D                  bt r12d, 0xd
0025D27D  0F 82 B3 00 00 00               jb 0x14025d336
0025D283  65 4C 8B 04 25 88 01 00 00      mov r8, qword ptr gs:[0x188]
0025D28C  41 8B C4                        mov eax, r12d
0025D28F  25 00 80 00 00                  and eax, 0x8000
0025D294  4C 89 45 28                     mov qword ptr [rbp + 0x28], r8
0025D298  41 8B D4                        mov edx, r12d
0025D29B  89 45 08                        mov dword ptr [rbp + 8], eax
0025D29E  81 E2 00 00 00 04               and edx, 0x4000000
0025D2A4  4D 3B C7                        cmp r8, r15
0025D2A7  0F 85 CD 05 00 00               jne 0x14025d87a
0025D2AD  41 F7 40 74 00 04 00 00         test dword ptr [r8 + 0x74], 0x400
0025D2B5  0F 85 B1 02 00 00               jne 0x14025d56c
0025D2BB  41 8B 80 A0 05 00 00            mov eax, dword ptr [r8 + 0x5a0]
0025D2C2  41 84 C5                        test r13b, al
0025D2C5  0F 85 06 01 00 00               jne 0x14025d3d1
0025D2CB  E8 90 AD 09 00                  call 0x1402f8060
0025D2D0  84 C0                           test al, al
0025D2D2  0F 84 C3 01 00 00               je 0x14025d49b
0025D2D8  44 0F 20 C0                     mov rax, cr8
0025D2DC  3C 02                           cmp al, 2
0025D2DE  0F 83 B7 01 00 00               jae 0x14025d49b
0025D2E4  E8 C7 B3 09 00                  call 0x1402f86b0
0025D2E9  85 C0                           test eax, eax
0025D2EB  0F 85 82 02 00 00               jne 0x14025d573
0025D2F1  41 0F B6 CD                     movzx ecx, r13b
0025D2F5  41 0F B6 D5                     movzx edx, r13b
0025D2F9  4C 8B 55 20                     mov r10, qword ptr [rbp + 0x20]
0025D2FD  41 0F BA E4 18                  bt r12d, 0x18
0025D302  0F B6 C1                        movzx eax, cl
0025D305  41 0F 42 C5                     cmovb eax, r13d
0025D309  84 D2                           test dl, dl
0025D30B  0F 84 80 01 00 00               je 0x14025d491
0025D311  84 C0                           test al, al
0025D313  74 21                           je 0x14025d336
0025D315  0F B7 87 32 03 00 00            movzx eax, word ptr [rdi + 0x332]
0025D31C  41 0F BA F6 0C                  btr r14d, 0xc
0025D321  83 E0 07                        and eax, 7
0025D324  83 C0 18                        add eax, 0x18
0025D327  F0 41 0F AB 47 78               lock bts dword ptr [r15 + 0x78], eax
0025D32D  89 45 08                        mov dword ptr [rbp + 8], eax
0025D330  0F 83 A8 00 00 00               jae 0x14025d3de
0025D336  41 F7 C6 00 18 00 00            test r14d, 0x1800
0025D33D  0F 84 B0 FE FF FF               je 0x14025d1f3
0025D343  4C 8D 4D 10                     lea r9, [rbp + 0x10]
0025D347  4D 8B C7                        mov r8, r15
0025D34A  41 8B D6                        mov edx, r14d
0025D34D  48 8B CF                        mov rcx, rdi
0025D350  E8 0B BA 09 00                  call 0x1402f8d60
0025D355  E9 99 FE FF FF                  jmp 0x14025d1f3
0025D35A  84 C0                           test al, al
0025D35C  0F 84 8B FD FF FF               je 0x14025d0ed
0025D362  E9 50 FA FF FF                  jmp 0x14025cdb7
0025D367  48 8B 4D 20                     mov rcx, qword ptr [rbp + 0x20]
0025D36B  33 D2                           xor edx, edx
0025D36D  45 8B C6                        mov r8d, r14d
0025D370  E8 CB 98 46 00                  call 0x1406c6c40
0025D375  48 8B CF                        mov rcx, rdi
0025D378  E8 63 45 19 00                  call 0x1403f18e0
0025D37D  48 8B 0D BC 24 CA 00            mov rcx, qword ptr [rip + 0xca24bc]
0025D384  48 8D 15 5D 32 DB FF            lea rdx, [rip - 0x24cda3]
0025D38B  E8 C0 50 13 00                  call 0x140392450
0025D390  0F B7 75 00                     movzx esi, word ptr [rbp]
0025D394  84 C0                           test al, al
0025D396  0F 84 03 FE FF FF               je 0x14025d19f
0025D39C  48 8D 97 88 00 00 00            lea rdx, [rdi + 0x88]
0025D3A3  41 B9 04 00 00 C0               mov r9d, 0xc0000004
0025D3A9  45 8B C4                        mov r8d, r12d
0025D3AC  0F B7 CE                        movzx ecx, si
0025D3AF  E8 30 64 26 00                  call 0x1404c37e4
0025D3B4  E9 E6 FD FF FF                  jmp 0x14025d19f
0025D3B9  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
0025D3C2  4C 39 78 18                     cmp qword ptr [rax + 0x18], r15
0025D3C6  0F 84 27 FE FF FF               je 0x14025d1f3
0025D3CC  E9 9A FE FF FF                  jmp 0x14025d26b
0025D3D1  85 D2                           test edx, edx
0025D3D3  0F 85 F2 FE FF FF               jne 0x14025d2cb
0025D3D9  E9 1F FF FF FF                  jmp 0x14025d2fd
0025D3DE  8B 45 10                        mov eax, dword ptr [rbp + 0x10]
0025D3E1  48 8D 8F 40 03 00 00            lea rcx, [rdi + 0x340]
0025D3E8  8B 55 14                        mov edx, dword ptr [rbp + 0x14]
0025D3EB  4C 8D 0D 7E A4 FC FF            lea r9, [rip - 0x35b82]
0025D3F2  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0025D3F7  45 0F B6 C2                     movzx r8d, r10b
0025D3FB  48 89 54 24 30                  mov qword ptr [rsp + 0x30], rdx
0025D400  48 8D 05 69 B0 25 00            lea rax, [rip + 0x25b069]
0025D407  48 C7 44 24 28 00 00 00 00      mov qword ptr [rsp + 0x28], 0
0025D410  49 8B D7                        mov rdx, r15
0025D413  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0025D418  E8 5F 67 FA FF                  call 0x140203b7c
0025D41D  85 C0                           test eax, eax
0025D41F  0F 89 11 FF FF FF               jns 0x14025d336
0025D425  8B 45 08                        mov eax, dword ptr [rbp + 8]
0025D428  F0 41 0F B3 47 78               lock btr dword ptr [r15 + 0x78], eax
0025D42E  E9 03 FF FF FF                  jmp 0x14025d336
0025D433  4C 8B 55 60                     mov r10, qword ptr [rbp + 0x60]
0025D437  4C 8D 45 38                     lea r8, [rbp + 0x38]
0025D43B  4C 8B 75 50                     mov r14, qword ptr [rbp + 0x50]
0025D43F  41 8B D2                        mov edx, r10d
0025D442  49 8B CE                        mov rcx, r14
0025D445  C7 45 38 00 00 00 00            mov dword ptr [rbp + 0x38], 0
0025D44C  E8 3B 9B 25 00                  call 0x1404b6f8c
0025D451  85 C0                           test eax, eax
0025D453  0F 84 63 FD FF FF               je 0x14025d1bc
0025D459  33 C9                           xor ecx, ecx
0025D45B  E8 0C FA 09 00                  call 0x1402fce6c
0025D460  85 C0                           test eax, eax
0025D462  0F 84 54 FD FF FF               je 0x14025d1bc
0025D468  49 8B 51 08                     mov rdx, qword ptr [r9 + 8]
0025D46C  45 33 C0                        xor r8d, r8d
0025D46F  48 8B 05 92 9F D6 00            mov rax, qword ptr [rip + 0xd69f92]
0025D476  45 33 C9                        xor r9d, r9d
0025D479  41 8B CA                        mov ecx, r10d
0025D47C  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
0025D481  49 03 CE                        add rcx, r14
0025D484  8B 55 38                        mov edx, dword ptr [rbp + 0x38]
0025D487  E8 44 D6 45 00                  call 0x1406baad0
0025D48C  E9 2B FD FF FF                  jmp 0x14025d1bc
0025D491  41 0F BA F6 0C                  btr r14d, 0xc
0025D496  E9 9B FE FF FF                  jmp 0x14025d336
0025D49B  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
0025D4A4  0F B6 48 20                     movzx ecx, byte ptr [rax + 0x20]
0025D4A8  84 C9                           test cl, cl
0025D4AA  0F 84 41 FE FF FF               je 0x14025d2f1
0025D4B0  41 3A CD                        cmp cl, r13b
0025D4B3  0F 84 29 01 00 00               je 0x14025d5e2
0025D4B9  32 D2                           xor dl, dl
0025D4BB  32 C9                           xor cl, cl
0025D4BD  E9 37 FE FF FF                  jmp 0x14025d2f9
0025D4C2  33 D2                           xor edx, edx
0025D4C4  48 8B 87 30 04 00 00            mov rax, qword ptr [rdi + 0x430]
0025D4CB  8B 48 08                        mov ecx, dword ptr [rax + 8]
0025D4CE  3B D1                           cmp edx, ecx
0025D4D0  0F 83 3B FD FF FF               jae 0x14025d211
0025D4D6  48 8B 87 30 04 00 00            mov rax, qword ptr [rdi + 0x430]
0025D4DD  66 39 74 50 0C                  cmp word ptr [rax + rdx*2 + 0xc], si
0025D4E2  0F 84 57 02 00 00               je 0x14025d73f
0025D4E8  FF C2                           inc edx
0025D4EA  EB D8                           jmp 0x14025d4c4
0025D4EC  41 8D 56 18                     lea edx, [r14 + 0x18]
0025D4F0  E8 CB F3 09 00                  call 0x1402fc8c0
0025D4F5  44 0F B7 4D 00                  movzx r9d, word ptr [rbp]
0025D4FA  4C 8B C0                        mov r8, rax
0025D4FD  48 85 C0                        test rax, rax
0025D500  0F 84 75 F8 FF FF               je 0x14025cd7b
0025D506  66 45 89 48 06                  mov word ptr [r8 + 6], r9w
0025D50B  41 0F B6 CC                     movzx ecx, r12b
0025D50F  81 C9 00 00 04 C0               or ecx, 0xc0040000
0025D515  89 08                           mov dword ptr [rax], ecx
0025D517  48 8B 4D 10                     mov rcx, qword ptr [rbp + 0x10]
0025D51B  48 89 48 10                     mov qword ptr [rax + 0x10], rcx
0025D51F  41 8D 46 18                     lea eax, [r14 + 0x18]
0025D523  66 41 89 40 04                  mov word ptr [r8 + 4], ax
0025D528  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0025D531  48 8B 91 10 05 00 00            mov rdx, qword ptr [rcx + 0x510]
0025D538  41 89 50 08                     mov dword ptr [r8 + 8], edx
0025D53C  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0025D545  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
0025D54C  8B 81 D0 01 00 00               mov eax, dword ptr [rcx + 0x1d0]
0025D552  41 89 40 0C                     mov dword ptr [r8 + 0xc], eax
0025D556  49 8D 40 18                     lea rax, [r8 + 0x18]
0025D55A  E9 0F F8 FF FF                  jmp 0x14025cd6e
0025D55F  84 C0                           test al, al
0025D561  0F 84 76 F8 FF FF               je 0x14025cddd
0025D567  E9 64 F9 FF FF                  jmp 0x14025ced0
0025D56C  32 D2                           xor dl, dl
0025D56E  E9 8A FD FF FF                  jmp 0x14025d2fd
0025D573  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
0025D577  80 B9 AE 05 00 00 00            cmp byte ptr [rcx + 0x5ae], 0
0025D57E  0F 85 6D FD FF FF               jne 0x14025d2f1
0025D584  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0025D58D  44 38 A8 4A 02 00 00            cmp byte ptr [rax + 0x24a], r13b
0025D594  0F 84 57 FD FF FF               je 0x14025d2f1
0025D59A  F6 41 7D 04                     test byte ptr [rcx + 0x7d], 4
0025D59E  0F 85 4D FD FF FF               jne 0x14025d2f1
0025D5A4  32 C9                           xor cl, cl
0025D5A6  E9 4A FD FF FF                  jmp 0x14025d2f5
0025D5AB  B9 24 05 00 00                  mov ecx, 0x524
0025D5B0  66 3B D1                        cmp dx, cx
0025D5B3  0F 85 54 FB FF FF               jne 0x14025d10d
0025D5B9  8B D1                           mov edx, ecx
0025D5BB  44 89 64 24 28                  mov dword ptr [rsp + 0x28], r12d
0025D5C0  48 8D 45 10                     lea rax, [rbp + 0x10]
0025D5C4  48 8B CF                        mov rcx, rdi
0025D5C7  4C 8D 4D 50                     lea r9, [rbp + 0x50]
0025D5CB  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0025D5D0  45 8B C6                        mov r8d, r14d
0025D5D3  E8 C4 AA 1B 00                  call 0x14041809c
0025D5D8  44 0F B7 4D 00                  movzx r9d, word ptr [rbp]
0025D5DD  E9 8C F7 FF FF                  jmp 0x14025cd6e
0025D5E2  83 7D 08 00                     cmp dword ptr [rbp + 8], 0
0025D5E6  0F 84 CD FE FF FF               je 0x14025d4b9
0025D5EC  E9 00 FD FF FF                  jmp 0x14025d2f1
0025D5F1  F0 FF 4A 0C                     lock dec dword ptr [rdx + 0xc]
0025D5F5  E9 EF FB FF FF                  jmp 0x14025d1e9
0025D5FA  48 8D 45 10                     lea rax, [rbp + 0x10]
0025D5FE  44 89 64 24 28                  mov dword ptr [rsp + 0x28], r12d
0025D603  4C 8D 4D 50                     lea r9, [rbp + 0x50]
0025D607  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0025D60C  45 8B C6                        mov r8d, r14d
0025D60F  48 8B CF                        mov rcx, rdi
0025D612  E8 B9 F8 09 00                  call 0x1402fced0
0025D617  44 0F B7 4D 00                  movzx r9d, word ptr [rbp]
0025D61C  E9 4D F7 FF FF                  jmp 0x14025cd6e
0025D621  33 C9                           xor ecx, ecx
0025D623  8B 87 04 05 00 00               mov eax, dword ptr [rdi + 0x504]
0025D629  3B C8                           cmp ecx, eax
0025D62B  0F 83 D0 FB FF FF               jae 0x14025d201
0025D631  66 39 B4 4F 08 05 00 00         cmp word ptr [rdi + rcx*2 + 0x508], si
0025D639  0F 84 42 02 00 00               je 0x14025d881
0025D63F  FF C1                           inc ecx
0025D641  EB E0                           jmp 0x14025d623
0025D643  33 D2                           xor edx, edx
0025D645  48 8B 87 38 04 00 00            mov rax, qword ptr [rdi + 0x438]
0025D64C  8B 48 18                        mov ecx, dword ptr [rax + 0x18]
0025D64F  3B D1                           cmp edx, ecx
0025D651  0F 83 CA FB FF FF               jae 0x14025d221
0025D657  48 8B 8F 38 04 00 00            mov rcx, qword ptr [rdi + 0x438]
0025D65E  66 39 74 51 1C                  cmp word ptr [rcx + rdx*2 + 0x1c], si
0025D663  74 40                           je 0x14025d6a5
0025D665  FF C2                           inc edx
0025D667  EB DC                           jmp 0x14025d645
0025D669  80 3D AC D3 BA 00 00            cmp byte ptr [rip + 0xbad3ac], 0
0025D670  74 28                           je 0x14025d69a
0025D672  80 3D 3A 86 CF 00 00            cmp byte ptr [rip + 0xcf863a], 0
0025D679  0F 84 2D FB FF FF               je 0x14025d1ac
0025D67F  48 8D 55 50                     lea rdx, [rbp + 0x50]
0025D683  48 8B CF                        mov rcx, rdi
0025D686  E8 85 97 25 00                  call 0x1404b6e10
0025D68B  E9 1C FB FF FF                  jmp 0x14025d1ac
0025D690  BA 95 00 00 C0                  mov edx, 0xc0000095
0025D695  E9 FF F6 FF FF                  jmp 0x14025cd99
0025D69A  80 3D 3B 9F CE 00 00            cmp byte ptr [rip + 0xce9f3b], 0
0025D6A1  74 DC                           je 0x14025d67f
0025D6A3  EB CD                           jmp 0x14025d672
0025D6A5  C7 85 B4 00 00 00 00 00 00 00   mov dword ptr [rbp + 0xb4], 0
0025D6AF  0F 57 C0                        xorps xmm0, xmm0
0025D6B2  F3 0F 7F 85 A0 00 00 00         movdqu xmmword ptr [rbp + 0xa0], xmm0
0025D6BA  65 48 8B 14 25 88 01 00 00      mov rdx, qword ptr gs:[0x188]
0025D6C3  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
0025D6CC  48 39 50 18                     cmp qword ptr [rax + 0x18], rdx
0025D6D0  0F 84 4B FB FF FF               je 0x14025d221
0025D6D6  41 F7 C4 00 18 00 00            test r12d, 0x1800
0025D6DD  0F 84 3E FB FF FF               je 0x14025d221
0025D6E3  48 89 BD 80 00 00 00            mov qword ptr [rbp + 0x80], rdi
0025D6EA  44 89 A5 B0 00 00 00            mov dword ptr [rbp + 0xb0], r12d
0025D6F1  8B 82 08 05 00 00               mov eax, dword ptr [rdx + 0x508]
0025D6F7  89 85 90 00 00 00               mov dword ptr [rbp + 0x90], eax
0025D6FD  8B 82 10 05 00 00               mov eax, dword ptr [rdx + 0x510]
0025D703  48 8D 95 80 00 00 00            lea rdx, [rbp + 0x80]
0025D70A  89 85 94 00 00 00               mov dword ptr [rbp + 0x94], eax
0025D710  48 8B 45 10                     mov rax, qword ptr [rbp + 0x10]
0025D714  48 89 85 88 00 00 00            mov qword ptr [rbp + 0x88], rax
0025D71B  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
0025D71F  48 89 85 98 00 00 00            mov qword ptr [rbp + 0x98], rax
0025D726  48 8B 41 10                     mov rax, qword ptr [rcx + 0x10]
0025D72A  48 8B 09                        mov rcx, qword ptr [rcx]
0025D72D  48 8B 40 10                     mov rax, qword ptr [rax + 0x10]
0025D731  E8 9A D3 45 00                  call 0x1406baad0
0025D736  48 8B 75 40                     mov rsi, qword ptr [rbp + 0x40]
0025D73A  E9 91 F7 FF FF                  jmp 0x14025ced0
0025D73F  0F 57 C0                        xorps xmm0, xmm0
0025D742  C7 45 18 00 00 00 00            mov dword ptr [rbp + 0x18], 0
0025D749  0F 11 85 80 00 00 00            movups xmmword ptr [rbp + 0x80], xmm0
0025D750  48 C7 45 68 00 00 00 00         mov qword ptr [rbp + 0x68], 0
0025D758  0F 11 85 90 00 00 00            movups xmmword ptr [rbp + 0x90], xmm0
0025D75F  48 C7 45 48 00 00 00 00         mov qword ptr [rbp + 0x48], 0
0025D767  0F 11 85 A0 00 00 00            movups xmmword ptr [rbp + 0xa0], xmm0
0025D76E  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0025D777  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
0025D780  C7 45 00 00 00 00 00            mov dword ptr [rbp], 0
0025D787  48 89 4D 28                     mov qword ptr [rbp + 0x28], rcx
0025D78B  48 39 48 18                     cmp qword ptr [rax + 0x18], rcx
0025D78F  0F 84 7C FA FF FF               je 0x14025d211
0025D795  41 F7 C4 00 18 00 00            test r12d, 0x1800
0025D79C  0F 84 6F FA FF FF               je 0x14025d211
0025D7A2  E8 C9 38 45 00                  call 0x1406b1070
0025D7A7  48 8B C8                        mov rcx, rax
0025D7AA  4C 8D 4D 68                     lea r9, [rbp + 0x68]
0025D7AE  4C 8D 45 48                     lea r8, [rbp + 0x48]
0025D7B2  48 8D 55 00                     lea rdx, [rbp]
0025D7B6  E8 15 A5 09 00                  call 0x1402f7cd0
0025D7BB  84 C0                           test al, al
0025D7BD  0F 84 4E FA FF FF               je 0x14025d211
0025D7C3  8B 45 00                        mov eax, dword ptr [rbp]
0025D7C6  83 F8 09                        cmp eax, 9
0025D7C9  77 0E                           ja 0x14025d7d9
0025D7CB  B9 A1 03 00 00                  mov ecx, 0x3a1
0025D7D0  0F A3 C1                        bt ecx, eax
0025D7D3  0F 82 38 FA FF FF               jb 0x14025d211
0025D7D9  8B 05 C1 95 D6 00               mov eax, dword ptr [rip + 0xd695c1]
0025D7DF  48 8D 0D CA B7 BC 00            lea rcx, [rip + 0xbcb7ca]
0025D7E6  C6 45 00 00                     mov byte ptr [rbp], 0
0025D7EA  44 8D 34 40                     lea r14d, [rax + rax*2]
0025D7EE  41 C1 E6 03                     shl r14d, 3
0025D7F2  E8 79 CD 45 00                  call 0x1406ba570
0025D7F7  48 85 C0                        test rax, rax
0025D7FA  74 46                           je 0x14025d842
0025D7FC  4C 8D 78 10                     lea r15, [rax + 0x10]
0025D800  4D 85 FF                        test r15, r15
0025D803  74 3D                           je 0x14025d842
0025D805  48 8B 05 DC 33 BA 00            mov rax, qword ptr [rip + 0xba33dc]
0025D80C  4C 8D 45 18                     lea r8, [rbp + 0x18]
0025D810  49 8B D7                        mov rdx, r15
0025D813  41 8B CE                        mov ecx, r14d
0025D816  E8 B5 D2 45 00                  call 0x1406baad0
0025D81B  85 C0                           test eax, eax
0025D81D  0F 89 87 B5 47 00               jns 0x1406d8daa
0025D823  80 7D 00 00                     cmp byte ptr [rbp], 0
0025D827  0F 85 E4 F9 FF FF               jne 0x14025d211
0025D82D  49 8D 57 F0                     lea rdx, [r15 - 0x10]
0025D831  48 8D 0D 78 B7 BC 00            lea rcx, [rip + 0xbcb778]
0025D838  E8 73 CD 45 00                  call 0x1406ba5b0
0025D83D  E9 CF F9 FF FF                  jmp 0x14025d211
0025D842  45 8B FE                        mov r15d, r14d
0025D845  E8 26 38 45 00                  call 0x1406b1070
0025D84A  48 2B 45 48                     sub rax, qword ptr [rbp + 0x48]
0025D84E  49 8D 8E 30 0E 00 00            lea rcx, [r14 + 0xe30]
0025D855  48 3B C1                        cmp rax, rcx
0025D858  0F 86 B3 F9 FF FF               jbe 0x14025d211
0025D85E  49 8D 46 0F                     lea rax, [r14 + 0xf]
0025D862  49 3B C7                        cmp rax, r15
0025D865  0F 87 25 B5 47 00               ja 0x1406d8d90
0025D86B  48 B8 F0 FF FF FF FF FF FF 0F   movabs rax, 0xffffffffffffff0
0025D875  E9 16 B5 47 00                  jmp 0x1406d8d90
0025D87A  32 D2                           xor dl, dl
0025D87C  E9 7C FA FF FF                  jmp 0x14025d2fd
0025D881  45 8B CC                        mov r9d, r12d
0025D884  48 8D 55 10                     lea rdx, [rbp + 0x10]
0025D888  45 33 C0                        xor r8d, r8d
0025D88B  48 8B CF                        mov rcx, rdi
0025D88E  E8 61 AB 27 00                  call 0x1404d83f4
0025D893  E9 69 F9 FF FF                  jmp 0x14025d201
0025D898  41 83 C9 08                     or r9d, 8
0025D89C  E9 FB F5 FF FF                  jmp 0x14025ce9c
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwpLogKernelEvent(__int64 a1, __int64 a2, int a3, int a4, unsigned __int16 a5, unsigned int a6)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned int v_stack_m110;
    unsigned int v_stack_m114;
    unsigned __int64 v_stack_m118;
    unsigned int v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned int v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned int v_stack_m148;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m70;
    unsigned int v_stack_m74;
    unsigned __int64 v_stack_m78;
    unsigned int v_stack_m7C;
    unsigned int v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned int v_stack_m94;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned int v_stack_mF4;
    unsigned int v_stack_mF8;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;

    v_rsp = (v_rsp) - (304);
    v_stack_p20 = v_rbx;
    result = (*(unsigned __int64 *)(v_rip + 12245786)) ^ (v_stack_m128);
    v_stack_m48 = result;
    v_stack_m128 = a5;
    result = 0;
    v_stack_mC8 = 0;
    v_stack_m118 = 0;
    v_rbx = 0;
    v_stack_mB8 = a2;
    v_stack_mE0 = a1;
    v_stack_mD8 = v_xmm0;
    result = KeAreInterruptsEnabled(a1, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0025CCCB;
    if (((unsigned __int8)(v_cr8)) >= 2) goto loc_0025CCCB;
    a2 = 0;
    a2 = (unsigned int)((a2) * (*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 704) + (unsigned int)(a3) * 8) + 16)));
    a4 = ((unsigned int)((unsigned int)(a2))) + (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 704) + (unsigned int)(a3) * 8)));
loc_0025CCB6:
    if ((((unsigned __int8)(*(unsigned __int64 *)(a4))) & (1)) != 0) goto loc_0025CEEB;
    if ((((unsigned __int8)(*(unsigned __int64 *)(a4))) & (1)) != 0) goto loc_0025CCB6;
loc_0025CCCB:
    v_stack_mE8 = (unsigned int)(a3) * 8;
    if ((((unsigned __int8)(*(unsigned __int64 *)((unsigned int)(a3) * 8 + *(unsigned __int64 *)(a2 + 712) * 1))) & (1)) != 0) goto loc_0025CF23;
    if (*(unsigned __int64 *)((unsigned int)(a3) * 8 + *(unsigned __int64 *)(a2 + 712) * 1) == 0) goto loc_0025CEF9;
    v_r14 = 0;
    v_r10 = 0;
    if ((unsigned int)((unsigned int)(a4)) != 0) goto loc_0025CF35;
loc_0025CD04:
    if (condition_is_below) goto loc_0025D049;
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)((unsigned int)(a3) * 8 + *(unsigned __int64 *)(a2 + 712) * 1) + 816)))) & (0xC00ULL)) != 0) goto loc_0025D0FF;
loc_0025CD26:
    v_stack_m148 = (unsigned int)((unsigned int)(a6));
    result = EtwpReserveTraceBuffer(*(unsigned __int64 *)((unsigned int)(a3) * 8 + *(unsigned __int64 *)(a2 + 712) * 1), v_r14 + 16, v_stack_mD8, v_stack_m118);
    if (result == 0) goto loc_0025CD7B;
    *(unsigned __int64 *)(result + 8) = v_stack_m118;
    a1 = (unsigned int)(((unsigned __int8)((unsigned int)(a6))) | (0xC0110000ULL));
    *(unsigned __int16 *)(result + 6) = (unsigned __int16)(v_stack_m128);
    *(unsigned int *)(result) = (unsigned int)(a1);
    *(unsigned __int16 *)(result + 4) = (unsigned __int16)(v_r14 + 16);
    result = (result) + (16);
loc_0025CD6E:
    v_stack_m108 = result;
    if (result != 0) goto loc_0025D145;
loc_0025CD7B:
    if (0 > 0xFFF8ULL) goto loc_0025D690;
    a2 = (unsigned int)(0xC0000017ULL);
    if (0 > (*(unsigned int *)(*(unsigned __int64 *)((unsigned int)(a3) * 8 + *(unsigned __int64 *)(a2 + 712) * 1) + 8))) { a2 = (unsigned int)((unsigned int)(0x80000005ULL)); }
loc_0025CD99:
    if (*(unsigned __int64 *)(v_rip + 13249184) == 0) goto loc_0025CED0;
    if ((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 13249184) + 32) + 96)) != 0) goto loc_0025D0E1;
loc_0025CDB7:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 13249184) + 102)) == 0) goto loc_0025CED0;
    if ((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 13249184) + 40) + 96)) == 0) goto loc_0025CED0;
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 13249184) + 40) + 100))) < 2) goto loc_0025D55F;
loc_0025CDDD:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 13249184) + 40) + 112)) & (64)) == 0) goto loc_0025CED0;
    result = (unsigned int)((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 13249184) + 40) + 120)) & (64));
    if (result != (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 13249184) + 40) + 120))) goto loc_0025CED0;
    goto loc_0025CE0E;
loc_0025CDFF:
    result = (unsigned int)((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 13249184) + 40) + 120) + 120)) & (64));
    if (result != (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 13249184) + 40) + 120) + 120))) goto loc_0025CDB7;
loc_0025CE0E:
    a1 = 0;
    v_stack_m128 = (unsigned __int16)(v_stack_m128);
    v_stack_m110 = (unsigned int)(a2);
    v_stack_mA8 = v_stack_m128;
    v_stack_mA0 = 2;
    v_stack_m98 = v_stack_m110;
    v_stack_m88 = *(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(a3) * 8 + *(unsigned __int64 *)(a2 + 712) * 1) + 144);
    v_stack_m80 = (unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)((unsigned int)(a3) * 8 + *(unsigned __int64 *)(a2 + 712) * 1) + 136));
    v_stack_m78 = v_rip - 2410627;
    a4 = 1;
    if (condition_is_below) { a4 = 5; }
    v_stack_m90 = 4;
    v_stack_m7C = 0;
    v_stack_m70 = 2;
    if ((((unsigned int)((unsigned int)(a6))) & (0x600ULL)) != 0) goto loc_0025D898;
loc_0025CE9C:
    a3 = 0;
    v_stack_m130 = v_stack_mA8;
    v_stack_m138 = 4;
    v_stack_m140 = 0;
    v_stack_m148 = 0;
    result = EtwWriteEx(*(unsigned __int64 *)(v_rip + 13248885), v_rip - 2410698, a3, a4);
loc_0025CED0:
    if (1 == 0) goto loc_0025CEF9;
loc_0025CEE2:
    result = ExReleaseRundownProtectionCacheAwareEx(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mB8 + 704) + (unsigned int)(a3) * 8 * 1), 1, a3, a4);
loc_0025CEEB:
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), 1, a3, a4);
loc_0025CEF9:
    a1 = (v_stack_m48) ^ (v_stack_m128);
    result = _security_check_cookie(a1, 1, a3, a4);
    return result;
loc_0025CF23:
    if ((unsigned __int8)(v_stack_p20) == 0) goto loc_0025CEF9;
    goto loc_0025CEE2;
loc_0025CF35:
    if (((unsigned int)((unsigned int)(a4))) >= 8) goto loc_0025CF62;
loc_0025CF3B:
    a1 = (0) << (4);
    a1 = (a1) + (8);
    a1 = (a1) + (1);
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a4)))) - (0));
loc_0025CF4F:
    v_r14 = (unsigned int)((v_r14) + (*(unsigned int *)(a1)));
    a2 = (a2) - (1);
    if (condition_is_equal) goto loc_0025CD04;
    goto loc_0025CF4F;
loc_0025CF62:
    v_r11 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a4)))) & (0xFFFFFFF8ULL));
loc_0025CF75:
    a3 = (2 + 1) + (2 + 1);
    a2 = (2) + (2);
    a1 = (2 - 1) + (2 - 1);
    a4 = (0) + (0);
    v_r10 = (unsigned int)((v_r10) + (8));
    a3 = (2 + 4) + (2 + 4);
    a4 = (2 + 5) + (2 + 5);
    a2 = (2 + 3) + (2 + 3);
    a1 = (2 + 2) + (2 + 2);
    v_r14 = (unsigned int)((2) + (8));
    if (((unsigned int)(v_r10)) < ((unsigned int)(v_r11))) goto loc_0025CF75;
    if (((unsigned int)(v_r10)) < ((unsigned int)((unsigned int)(a4)))) goto loc_0025CF3B;
    goto loc_0025CD04;
loc_0025D049:
    v_stack_p20 = (unsigned int)((unsigned int)(a6));
    if (((unsigned int)(v_r10)) < ((unsigned int)((unsigned int)(a4)))) goto loc_0025D4EC;
    v_stack_m100 = *(unsigned __int64 *)(gs_base + (0 + 392));
    result = EtwpReserveTraceBuffer(*(unsigned __int64 *)((unsigned int)(a3) * 8 + *(unsigned __int64 *)(a2 + 712) * 1), v_r14 + 32, v_stack_mD8, v_stack_m118);
    if (result == 0) goto loc_0025CD7B;
    *(unsigned __int16 *)(result + 6) = (unsigned __int16)(v_stack_m128);
    a1 = (unsigned int)(((unsigned __int8)((unsigned int)(a6))) | (0xC0020000ULL));
    *(unsigned int *)(result) = (unsigned int)(a1);
    *(unsigned __int64 *)(result + 16) = v_stack_m118;
    *(unsigned __int16 *)(result + 4) = (unsigned __int16)(v_r14 + 32);
    *(unsigned int *)(result + 8) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m100 + 1296)));
    *(unsigned int *)(result + 12) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m100 + 1288)));
    *(unsigned int *)(result + 24) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m100 + 652)));
    *(unsigned int *)(result + 28) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m100 + 732)));
    goto loc_0025CD6E;
loc_0025D0E1:
    if (((unsigned __int8)(*(unsigned __int8 *)((unsigned int)(*(unsigned int *)(v_stack_m100 + 1288)) + 100))) < 2) goto loc_0025D35A;
loc_0025D0ED:
    if (((*(unsigned __int8 *)((unsigned int)(*(unsigned int *)(v_stack_m100 + 1288)) + 112)) & (64)) == 0) goto loc_0025CDB7;
    goto loc_0025CDFF;
loc_0025D0FF:
    if (condition_is_below) goto loc_0025D5AB;
loc_0025D10D:
    if (condition_is_above_or_equal) goto loc_0025CD26;
    a3 = 0;
loc_0025D11A:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(a3) * 8 + *(unsigned __int64 *)(a2 + 712) * 1) + 1064) + 8))))) goto loc_0025CD26;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(a3) * 8 + *(unsigned __int64 *)(a2 + 712) * 1) + 1064) + a3 * 2 + 12)) == ((unsigned __int16)(v_stack_m128))) goto loc_0025D5FA;
    a3 = (unsigned int)((a3) + 1);
    goto loc_0025D11A;
loc_0025D145:
    result = 0;
loc_0025D14E:
    v_stack_mF4 = 0;
    v_stack_m100 = v_stack_m108;
    v_stack_mF8 = (unsigned int)((unsigned int)((unsigned int)(v_r14)));
    if (0 >= ((unsigned int)((unsigned int)(a4)))) goto loc_0025D19B;
    result = (result) + (0);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mE0 + result * 8 + 8)))) > ((unsigned int)((unsigned int)((unsigned int)(v_r14))))) goto loc_0025D367;
    result = memcpy(v_stack_m108, *(unsigned __int64 *)(v_stack_mE0 + result * 8), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mE0 + result * 8 + 8)))), v_stack_m108);
    a4 = (v_stack_m100) + ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mE0 + result * 8 + 8)))));
    a3 = (unsigned int)(((unsigned int)(v_stack_mF8)) - ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mE0 + result * 8 + 8)))))));
    result = (unsigned int)(((unsigned int)(v_stack_mF4)) + 1);
    goto loc_0025D14E;
loc_0025D19B:
loc_0025D19F:
    if (((*(unsigned int *)(*(unsigned __int64 *)((unsigned int)(a3) * 8 + *(unsigned __int64 *)(a2 + 712) * 1) + 12)) & (0x80000ULL)) != 0) goto loc_0025D669;
loc_0025D1AC:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(a3) * 8 + *(unsigned __int64 *)(a2 + 712) * 1) + 1568) != 0) goto loc_0025D433;
loc_0025D1BC:
loc_0025D1C6:
    a1 = (v_stack_mD8) ^ (*(unsigned __int64 *)(v_stack_mD0));
    if (a1 >= 15) goto loc_0025D5F1;
    if (a1 != 15) goto loc_0025D1C6;
loc_0025D1E9:
    if (sign_flag) goto loc_0025D22A;
loc_0025D1F3:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)((unsigned int)(a3) * 8 + *(unsigned __int64 *)(a2 + 712) * 1) + 820)))) & (2)) != 0) goto loc_0025D621;
loc_0025D201:
    if (((*(unsigned int *)(*(unsigned __int64 *)((unsigned int)(a3) * 8 + *(unsigned __int64 *)(a2 + 712) * 1) + 816)) & (0x8000ULL)) != 0) goto loc_0025D4C2;
loc_0025D211:
    if (((*(unsigned int *)(*(unsigned __int64 *)((unsigned int)(a3) * 8 + *(unsigned __int64 *)(a2 + 712) * 1) + 816)) & (0x4000000ULL)) != 0) goto loc_0025D643;
loc_0025D221:
    goto loc_0025CED0;
loc_0025D22A:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_stack_mE8))) & (0x1FFFULL));
    a1 = (unsigned int)((a1) & (7));
    result = ((unsigned int)((unsigned int)(a1))) >> (3);
    result = (result) + (*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(a3) * 8 + *(unsigned __int64 *)(a2 + 712) * 1) + 1048));
    result = (unsigned __int8)((*(unsigned __int8 *)(result)) >> ((unsigned __int8)(a1)));
    if (((1) & ((unsigned __int8)(result))) == 0) goto loc_0025D1F3;
    v_stack_m108 = v_cr8;
    if (condition_is_below) goto loc_0025D3B9;
loc_0025D26B:
    if (condition_is_above_or_equal) goto loc_0025D336;
    a1 = 0;
    if (condition_is_below) goto loc_0025D336;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a6)))) & (0x8000ULL));
    v_stack_m100 = *(unsigned __int64 *)(gs_base + (0 + 392));
    v_stack_m120 = (unsigned int)(result);
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a6)))) & (0x4000000ULL));
    if ((*(unsigned __int64 *)(gs_base + (0 + 392))) != (*(unsigned __int64 *)(gs_base + (0 + 392)))) goto loc_0025D87A;
    if (((*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 116)) & (0x400ULL)) != 0) goto loc_0025D56C;
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1440))))) != 0) goto loc_0025D3D1;
loc_0025D2CB:
    result = KeAreInterruptsEnabled(a1, a2, *(unsigned __int64 *)(gs_base + (0 + 392)), *(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(a3) * 8 + *(unsigned __int64 *)(a2 + 712) * 1) + 1568));
    if ((unsigned __int8)(result) == 0) goto loc_0025D49B;
    if (((unsigned __int8)(v_cr8)) >= 2) goto loc_0025D49B;
    result = MmCanThreadFault(a1, a2, *(unsigned __int64 *)(gs_base + (0 + 392)), *(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(a3) * 8 + *(unsigned __int64 *)(a2 + 712) * 1) + 1568));
    if ((unsigned int)(result) != 0) goto loc_0025D573;
loc_0025D2F1:
loc_0025D2F5:
loc_0025D2F9:
loc_0025D2FD:
    result = 1;
    if (condition_is_below) { result = 1; }
    if (1 == 0) goto loc_0025D491;
    if ((unsigned __int8)(result) == 0) goto loc_0025D336;
    result = (unsigned int)((*(unsigned __int16 *)(*(unsigned __int64 *)((unsigned int)(a3) * 8 + *(unsigned __int64 *)(a2 + 712) * 1) + 818)) & (7));
    result = (unsigned int)((result) + (24));
    v_stack_m120 = (unsigned int)(result);
    if (condition_is_above_or_equal) goto loc_0025D3DE;
loc_0025D336:
    if ((((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a6))))) & (0x1800ULL)) == 0) goto loc_0025D1F3;
    result = EtwpTraceStackWalk(*(unsigned __int64 *)((unsigned int)(a3) * 8 + *(unsigned __int64 *)(a2 + 712) * 1), (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a6))))), *(unsigned __int64 *)(gs_base + (0 + 392)), v_stack_m118);
    goto loc_0025D1F3;
loc_0025D35A:
    if ((unsigned __int8)(result) == 0) goto loc_0025D0ED;
    goto loc_0025CDB7;
loc_0025D367:
    a2 = 0;
    result = memset(v_stack_m108, a2, (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a6))))), v_stack_m118);
    result = EtwpUpdateEventsLostCount(*(unsigned __int64 *)((unsigned int)(a3) * 8 + *(unsigned __int64 *)(a2 + 712) * 1), a2, (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a6))))), v_stack_m118);
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 13247676), v_rip - 2411939, (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a6))))), v_stack_m118);
    if ((unsigned __int8)(result) == 0) goto loc_0025D19F;
    result = EtwpTraceLostSystemEvent((unsigned __int16)(v_stack_m128), *(unsigned __int64 *)((unsigned int)(a3) * 8 + *(unsigned __int64 *)(a2 + 712) * 1) + 136, (unsigned int)((unsigned int)((unsigned int)(a6))), (unsigned int)(0xC0000004ULL));
    goto loc_0025D19F;
loc_0025D3B9:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 24)) == (*(unsigned __int64 *)(gs_base + (0 + 392)))) goto loc_0025D1F3;
    goto loc_0025D26B;
loc_0025D3D1:
    if ((unsigned int)(*(unsigned __int64 *)((unsigned int)(a3) * 8 + *(unsigned __int64 *)(a2 + 712) * 1) + 136) != 0) goto loc_0025D2CB;
    goto loc_0025D2FD;
loc_0025D3DE:
    v_stack_p38 = (unsigned int)(v_stack_m118);
    v_stack_p30 = (unsigned int)(v_stack_m114);
    v_stack_p28 = 0;
    v_stack_p20 = v_rip + 2469993;
    result = EtwpQueueApc(*(unsigned __int64 *)((unsigned int)(a3) * 8 + *(unsigned __int64 *)(a2 + 712) * 1) + 832, *(unsigned __int64 *)(gs_base + (0 + 392)), (unsigned __int8)(v_stack_m108), v_rip - 220034);
    if (!sign_flag) goto loc_0025D336;
    goto loc_0025D336;
loc_0025D433:
    v_stack_mF0 = 0;
    result = EtwpGetNextEventOffsetType(v_stack_mD8, (unsigned int)((unsigned int)(v_stack_mC8)), v_stack_mF0, v_rip - 220034);
    if ((unsigned int)(result) == 0) goto loc_0025D1BC;
    a1 = 0;
    result = KeIsTraceCallbackAllowed(a1, (unsigned int)((unsigned int)(v_stack_mC8)), v_stack_mF0, v_rip - 220034);
    if ((unsigned int)(result) == 0) goto loc_0025D1BC;
    a3 = 0;
    a4 = 0;
    v_stack_p20 = *(unsigned __int64 *)(v_rip - 220034 + 8);
    a1 = ((unsigned int)((unsigned int)(v_stack_mC8))) + (v_stack_mD8);
    result = guard_dispatch_icall(a1, (unsigned int)(v_stack_mF0), a3, a4);
    goto loc_0025D1BC;
loc_0025D491:
    goto loc_0025D336;
loc_0025D49B:
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 32)) == 0) goto loc_0025D2F1;
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 32))) == 1) goto loc_0025D5E2;
loc_0025D4B9:
    a2 = 0;
    a1 = 0;
    goto loc_0025D2F9;
loc_0025D4C2:
    a2 = 0;
loc_0025D4C4:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(a3) * 8 + *(unsigned __int64 *)(a2 + 712) * 1) + 1072) + 8))))) goto loc_0025D211;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(a3) * 8 + *(unsigned __int64 *)(a2 + 712) * 1) + 1072) + a2 * 2 + 12)) == ((unsigned __int16)(v_stack_m128))) goto loc_0025D73F;
    a2 = (unsigned int)((a2) + 1);
    goto loc_0025D4C4;
loc_0025D4EC:
    result = EtwpReserveTraceBuffer((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(a3) * 8 + *(unsigned __int64 *)(a2 + 712) * 1) + 1072) + 8)), v_stack_mD8 + 24, a3, a4);
    if (result == 0) goto loc_0025CD7B;
    *(unsigned __int16 *)(result + 6) = (unsigned __int16)(v_stack_m128);
    a1 = (unsigned int)(((unsigned __int8)((unsigned int)(a6))) | (0xC0040000ULL));
    *(unsigned int *)(result) = (unsigned int)(a1);
    *(unsigned __int64 *)(result + 16) = v_stack_m118;
    *(unsigned __int16 *)(result + 4) = (unsigned __int16)(v_stack_mD8 + 24);
    *(unsigned int *)(result + 8) = (unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1296));
    *(unsigned int *)(result + 12) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 464)));
    goto loc_0025CD6E;
loc_0025D55F:
    if ((unsigned __int8)(result + 24) == 0) goto loc_0025CDDD;
    goto loc_0025CED0;
loc_0025D56C:
    a2 = 0;
    goto loc_0025D2FD;
loc_0025D573:
    if ((*(unsigned __int8 *)(v_stack_m100 + 1454)) != 0) goto loc_0025D2F1;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 586)) == 1) goto loc_0025D2F1;
    if (((*(unsigned __int8 *)(v_stack_m100 + 125)) & (4)) != 0) goto loc_0025D2F1;
    a1 = 0;
    goto loc_0025D2F5;
loc_0025D5AB:
    if (0 != ((unsigned __int16)((unsigned int)(0x524ULL)))) goto loc_0025D10D;
    v_stack_p28 = (unsigned int)((unsigned int)(a6));
    v_stack_p20 = v_stack_m118;
    result = EtwpReserveWithPebsIndex(*(unsigned __int64 *)((unsigned int)(a3) * 8 + *(unsigned __int64 *)(a2 + 712) * 1), (unsigned int)((unsigned int)((unsigned int)(0x524ULL))), (unsigned int)((unsigned int)(v_stack_mD8)), v_stack_mD8);
    goto loc_0025CD6E;
loc_0025D5E2:
    if (v_stack_m120 == 0) goto loc_0025D4B9;
    goto loc_0025D2F1;
loc_0025D5F1:
    goto loc_0025D1E9;
loc_0025D5FA:
    v_stack_p28 = (unsigned int)((unsigned int)(a6));
    v_stack_p20 = v_stack_m118;
    result = EtwpReserveWithPmcCounters(*(unsigned __int64 *)((unsigned int)(a3) * 8 + *(unsigned __int64 *)(a2 + 712) * 1), (unsigned int)((unsigned int)((unsigned int)(0x524ULL))), (unsigned int)((unsigned int)(v_stack_mD8)), v_stack_mD8);
    goto loc_0025CD6E;
loc_0025D621:
    a1 = 0;
loc_0025D623:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)((unsigned int)(a3) * 8 + *(unsigned __int64 *)(a2 + 712) * 1) + 1284))))) goto loc_0025D201;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)((unsigned int)(a3) * 8 + *(unsigned __int64 *)(a2 + 712) * 1) + a1 * 2 + 1288)) == ((unsigned __int16)(v_stack_m128))) goto loc_0025D881;
    a1 = (unsigned int)((a1) + 1);
    goto loc_0025D623;
loc_0025D643:
    a2 = 0;
loc_0025D645:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(a3) * 8 + *(unsigned __int64 *)(a2 + 712) * 1) + 1080) + 24))))) goto loc_0025D221;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(a3) * 8 + *(unsigned __int64 *)(a2 + 712) * 1) + 1080) + a2 * 2 + 28)) == ((unsigned __int16)(v_stack_m128))) goto loc_0025D6A5;
    a2 = (unsigned int)((a2) + 1);
    goto loc_0025D645;
loc_0025D669:
    if ((*(unsigned __int8 *)(v_rip + 12243884)) == 0) goto loc_0025D69A;
loc_0025D672:
    if ((*(unsigned __int8 *)(v_rip + 13600314)) == 0) goto loc_0025D1AC;
loc_0025D67F:
    result = EtwpSendTraceEvent(*(unsigned __int64 *)((unsigned int)(a3) * 8 + *(unsigned __int64 *)(a2 + 712) * 1), v_stack_mD8, (unsigned int)((unsigned int)(v_stack_mD8)), v_stack_m128);
    goto loc_0025D1AC;
loc_0025D690:
    goto loc_0025CD99;
loc_0025D69A:
    if ((*(unsigned __int8 *)(v_rip + 13541179)) == 0) goto loc_0025D67F;
    goto loc_0025D672;
loc_0025D6A5:
    v_stack_m74 = 0;
    v_stack_m88 = v_xmm0;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 24)) == (*(unsigned __int64 *)(gs_base + (0 + 392)))) goto loc_0025D221;
    if ((((unsigned int)((unsigned int)(a6))) & (0x1800ULL)) == 0) goto loc_0025D221;
    v_stack_mA8 = *(unsigned __int64 *)((unsigned int)(a3) * 8 + *(unsigned __int64 *)(a2 + 712) * 1);
    v_stack_m78 = (unsigned int)((unsigned int)(a6));
    v_stack_m98 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1288)));
    v_stack_m94 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1296)));
    v_stack_mA0 = v_stack_m118;
    v_stack_m90 = *(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(a3) * 8 + *(unsigned __int64 *)(a2 + 712) * 1) + 8);
    result = guard_dispatch_icall(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(a3) * 8 + *(unsigned __int64 *)(a2 + 712) * 1)), v_stack_mA8, (unsigned int)((unsigned int)(v_stack_mD8)), v_stack_m128);
    goto loc_0025CED0;
loc_0025D73F:
    v_stack_m110 = 0;
    v_stack_mA8 = v_xmm0;
    v_stack_mC0 = 0;
    v_stack_m98 = v_xmm0;
    v_stack_mE0 = 0;
    v_stack_m88 = v_xmm0;
    v_stack_m128 = 0;
    v_stack_m100 = *(unsigned __int64 *)(gs_base + (0 + 392));
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 24)) == (*(unsigned __int64 *)(gs_base + (0 + 392)))) goto loc_0025D211;
    if ((((unsigned int)((unsigned int)(a6))) & (0x1800ULL)) == 0) goto loc_0025D211;
    result = KeGetCurrentStackPointer(*(unsigned __int64 *)(gs_base + (0 + 392)), v_stack_mA8, (unsigned int)((unsigned int)(v_stack_mD8)), v_stack_m128);
    result = KeQueryCurrentStackInformationEx(result, v_stack_m128, v_stack_mE0, v_stack_mC0);
    if ((unsigned __int8)(result) == 0) goto loc_0025D211;
    if (((unsigned int)((unsigned int)(v_stack_m128))) > 9) goto loc_0025D7D9;
    if (((unsigned int)((unsigned int)(v_stack_m128))) < 9) goto loc_0025D211;
loc_0025D7D9:
    v_stack_m128 = 0;
    v_r14 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 14063041)) + (unsigned int)(*(unsigned int *)(v_rip + 14063041)) * 2) << (3));
    result = ExpInterlockedPopEntrySList(v_rip + 12367818, v_stack_m128, v_stack_mE0, v_stack_mC0);
    if (result == 0) goto loc_0025D842;
    if (result + 16 == 0) goto loc_0025D842;
    result = guard_dispatch_icall((unsigned int)((unsigned int)(v_r14)), result + 16, v_stack_m110, v_stack_mC0);
    if (v_stack_m128 != 0) goto loc_0025D211;
    result = ExpInterlockedPushEntrySList(v_rip + 12367736, result + 16 - 16, v_stack_m110, v_stack_mC0);
    goto loc_0025D211;
loc_0025D842:
    result = KeGetCurrentStackPointer(v_rip + 12367736, result + 16 - 16, v_stack_m110, v_stack_mC0);
    result = (result) - (v_stack_mE0);
    if (result <= (v_r14 + 3632)) goto loc_0025D211;
loc_0025D87A:
    a2 = 0;
    goto loc_0025D2FD;
loc_0025D881:
    a3 = 0;
    result = EtwpContextRegisterTracingDispatcher(*(unsigned __int64 *)((unsigned int)(a3) * 8 + *(unsigned __int64 *)(a2 + 712) * 1), v_stack_m118, a3, (unsigned int)((unsigned int)((unsigned int)(a6))));
    goto loc_0025D201;
loc_0025D898:
    a4 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a6)))) | (8));
    goto loc_0025CE9C;
}
```

## 5. (Beta) C Style

```c
int64_t EtwpLogKernelEvent(void *Arg1, void *Arg2, int32_t Arg3, int32_t Arg4, uint16_t Arg5, uint32_t Arg6)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint32_t v_stack_m110;
    uint32_t v_stack_m114;
    uint64_t v_stack_m118;
    uint32_t v_stack_m120;
    uint64_t v_stack_m128;
    uint64_t v_stack_m130;
    uint32_t v_stack_m138;
    uint64_t v_stack_m140;
    uint32_t v_stack_m148;
    uint64_t v_stack_m38;
    uint64_t v_stack_m48;
    uint64_t v_stack_m70;
    uint32_t v_stack_m74;
    uint64_t v_stack_m78;
    uint32_t v_stack_m7C;
    uint32_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint32_t v_stack_m94;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint32_t v_stack_mF4;
    uint32_t v_stack_mF8;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;

    local_rsp = (local_rsp) - (304);
    v_stack_p20 = local_rbx;
    result = (*(uint64_t *)(v_rip + 0xBADB1A)) ^ (v_stack_m128);
    v_stack_m48 = result;
    v_stack_m128 = Arg5;
    result = 0;
    v_stack_mC8 = 0;
    v_stack_m118 = 0;
    local_rbx = 0;
    v_stack_mB8 = Arg2;
    v_stack_mE0 = Arg1;
    v_stack_mD8 = v_xmm0;
    result = KeAreInterruptsEnabled(Arg1, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0025CCCB;
    if (((uint8_t)(v_cr8)) >= 2) goto loc_0025CCCB;
    Arg2 = 0;
    Arg2 = (uint32_t)((Arg2) * (*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x2C0) + (uint32_t)(Arg3) * 8) + 0x10)));
    Arg4 = ((uint32_t)((uint32_t)(Arg2))) + (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x2C0) + (uint32_t)(Arg3) * 8)));
loc_0025CCB6:
    if ((((uint8_t)(*(uint64_t *)(Arg4))) & (1)) != 0) goto loc_0025CEEB;
    if ((((uint8_t)(*(uint64_t *)(Arg4))) & (1)) != 0) goto loc_0025CCB6;
loc_0025CCCB:
    v_stack_mE8 = (uint32_t)(Arg3) * 8;
    if ((((uint8_t)(*(uint64_t *)((uint32_t)(Arg3) * 8 + *(uint64_t *)(arg2 + 0x2C8) * 1))) & (1)) != 0) goto loc_0025CF23;
    if (*(uint64_t *)((uint32_t)(Arg3) * 8 + *(uint64_t *)(arg2 + 0x2C8) * 1) == 0) goto loc_0025CEF9;
    local_r14 = 0;
    local_r10 = 0;
    if ((uint32_t)((uint32_t)(Arg4)) != 0) goto loc_0025CF35;
loc_0025CD04:
    if (condition_is_below) goto loc_0025D049;
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)((uint32_t)(Arg3) * 8 + *(uint64_t *)(arg2 + 0x2C8) * 1) + 0x330)))) & (0xC00ULL)) != 0) goto loc_0025D0FF;
loc_0025CD26:
    v_stack_m148 = (uint32_t)((uint32_t)(Arg6));
    result = EtwpReserveTraceBuffer(*(uint64_t *)((uint32_t)(Arg3) * 8 + *(uint64_t *)(arg2 + 0x2C8) * 1), local_r14 + 16, v_stack_mD8, v_stack_m118);
    if (result == 0) goto loc_0025CD7B;
    *(uint64_t *)(result + 0x8) = v_stack_m118;
    Arg1 = (uint32_t)(((uint8_t)((uint32_t)(Arg6))) | (0xC0110000ULL));
    *(uint16_t *)(result + 0x6) = (uint16_t)(v_stack_m128);
    *(uint32_t *)(result) = (uint32_t)(Arg1);
    *(uint16_t *)(result + 0x4) = (uint16_t)(local_r14 + 16);
    result = (result) + (16);
loc_0025CD6E:
    v_stack_m108 = result;
    if (result != 0) goto loc_0025D145;
loc_0025CD7B:
    if (0 > 0xFFF8ULL) goto loc_0025D690;
    Arg2 = (uint32_t)(0xC0000017ULL);
    if (0 > (*(uint32_t *)(*(uint64_t *)((uint32_t)(Arg3) * 8 + *(uint64_t *)(arg2 + 0x2C8) * 1) + 0x8))) { Arg2 = (uint32_t)((uint32_t)(0x80000005ULL)); }
loc_0025CD99:
    if (*(uint64_t *)(v_rip + 0xCA2AA0) == 0) goto loc_0025CED0;
    if ((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xCA2AA0) + 0x20) + 0x60)) != 0) goto loc_0025D0E1;
loc_0025CDB7:
    if ((*(uint16_t *)(*(uint64_t *)(v_rip + 0xCA2AA0) + 0x66)) == 0) goto loc_0025CED0;
    if ((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xCA2AA0) + 0x28) + 0x60)) == 0) goto loc_0025CED0;
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xCA2AA0) + 0x28) + 0x64))) < 2) goto loc_0025D55F;
loc_0025CDDD:
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xCA2AA0) + 0x28) + 0x70)) & (64)) == 0) goto loc_0025CED0;
    result = (uint32_t)((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xCA2AA0) + 0x28) + 0x78)) & (64));
    if (result != (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xCA2AA0) + 0x28) + 0x78))) goto loc_0025CED0;
    goto loc_0025CE0E;
loc_0025CDFF:
    result = (uint32_t)((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xCA2AA0) + 0x28) + 0x78) + 0x78)) & (64));
    if (result != (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xCA2AA0) + 0x28) + 0x78) + 0x78))) goto loc_0025CDB7;
loc_0025CE0E:
    Arg1 = 0;
    v_stack_m128 = (uint16_t)(v_stack_m128);
    v_stack_m110 = (uint32_t)(Arg2);
    v_stack_mA8 = v_stack_m128;
    v_stack_mA0 = 2;
    v_stack_m98 = v_stack_m110;
    v_stack_m88 = *(uint64_t *)(*(uint64_t *)((uint32_t)(Arg3) * 8 + *(uint64_t *)(arg2 + 0x2C8) * 1) + 0x90);
    v_stack_m80 = (uint32_t)(*(uint16_t *)(*(uint64_t *)((uint32_t)(Arg3) * 8 + *(uint64_t *)(arg2 + 0x2C8) * 1) + 0x88));
    v_stack_m78 = v_rip - 2410627;
    Arg4 = 1;
    if (condition_is_below) { Arg4 = 5; }
    v_stack_m90 = 4;
    v_stack_m7C = 0;
    v_stack_m70 = 2;
    if ((((uint32_t)((uint32_t)(Arg6))) & (0x600ULL)) != 0) goto loc_0025D898;
loc_0025CE9C:
    Arg3 = 0;
    v_stack_m130 = v_stack_mA8;
    v_stack_m138 = 4;
    v_stack_m140 = 0;
    v_stack_m148 = 0;
    result = EtwWriteEx(*(uint64_t *)(v_rip + 0xCA2975), v_rip - 2410698, Arg3, Arg4);
loc_0025CED0:
    if (1 == 0) goto loc_0025CEF9;
loc_0025CEE2:
    result = ExReleaseRundownProtectionCacheAwareEx(*(uint64_t *)(*(uint64_t *)(v_stack_mB8 + 0x2C0) + (uint32_t)(Arg3) * 8 * 1), 1, Arg3, Arg4);
loc_0025CEEB:
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), 1, Arg3, Arg4);
loc_0025CEF9:
    Arg1 = (v_stack_m48) ^ (v_stack_m128);
    result = _security_check_cookie(Arg1, 1, Arg3, Arg4);
    return result;
loc_0025CF23:
    if ((uint8_t)(v_stack_p20) == 0) goto loc_0025CEF9;
    goto loc_0025CEE2;
loc_0025CF35:
    if (((uint32_t)((uint32_t)(Arg4))) >= 8) goto loc_0025CF62;
loc_0025CF3B:
    Arg1 = (0) << (4);
    Arg1 = (Arg1) + (8);
    Arg1 = (Arg1) + (1);
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg4)))) - (0));
loc_0025CF4F:
    local_r14 = (uint32_t)((local_r14) + (*(uint32_t *)(arg1)));
    Arg2 = (Arg2) - (1);
    if (condition_is_equal) goto loc_0025CD04;
    goto loc_0025CF4F;
loc_0025CF62:
    local_r11 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg4)))) & (0xFFFFFFF8ULL));
loc_0025CF75:
    Arg3 = (2 + 1) + (2 + 1);
    Arg2 = (2) + (2);
    Arg1 = (2 - 1) + (2 - 1);
    Arg4 = (0) + (0);
    local_r10 = (uint32_t)((local_r10) + (8));
    Arg3 = (2 + 4) + (2 + 4);
    Arg4 = (2 + 5) + (2 + 5);
    Arg2 = (2 + 3) + (2 + 3);
    Arg1 = (2 + 2) + (2 + 2);
    local_r14 = (uint32_t)((2) + (8));
    if (((uint32_t)(local_r10)) < ((uint32_t)(local_r11))) goto loc_0025CF75;
    if (((uint32_t)(local_r10)) < ((uint32_t)((uint32_t)(Arg4)))) goto loc_0025CF3B;
    goto loc_0025CD04;
loc_0025D049:
    v_stack_p20 = (uint32_t)((uint32_t)(Arg6));
    if (((uint32_t)(local_r10)) < ((uint32_t)((uint32_t)(Arg4)))) goto loc_0025D4EC;
    v_stack_m100 = *(uint64_t *)(gs_base + (0 + 0x188));
    result = EtwpReserveTraceBuffer(*(uint64_t *)((uint32_t)(Arg3) * 8 + *(uint64_t *)(arg2 + 0x2C8) * 1), local_r14 + 32, v_stack_mD8, v_stack_m118);
    if (result == 0) goto loc_0025CD7B;
    *(uint16_t *)(result + 0x6) = (uint16_t)(v_stack_m128);
    Arg1 = (uint32_t)(((uint8_t)((uint32_t)(Arg6))) | (0xC0020000ULL));
    *(uint32_t *)(result) = (uint32_t)(Arg1);
    *(uint64_t *)(result + 0x10) = v_stack_m118;
    *(uint16_t *)(result + 0x4) = (uint16_t)(local_r14 + 32);
    *(uint32_t *)(result + 0x8) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m100 + 0x510)));
    *(uint32_t *)(result + 0xC) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m100 + 0x508)));
    *(uint32_t *)(result + 0x18) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m100 + 0x28C)));
    *(uint32_t *)(result + 0x1C) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m100 + 0x2DC)));
    goto loc_0025CD6E;
loc_0025D0E1:
    if (((uint8_t)(*(uint8_t *)((uint32_t)(*(uint32_t *)(v_stack_m100 + 0x508)) + 0x64))) < 2) goto loc_0025D35A;
loc_0025D0ED:
    if (((*(uint8_t *)((uint32_t)(*(uint32_t *)(v_stack_m100 + 0x508)) + 0x70)) & (64)) == 0) goto loc_0025CDB7;
    goto loc_0025CDFF;
loc_0025D0FF:
    if (condition_is_below) goto loc_0025D5AB;
loc_0025D10D:
    if (condition_is_above_or_equal) goto loc_0025CD26;
    Arg3 = 0;
loc_0025D11A:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(Arg3) * 8 + *(uint64_t *)(arg2 + 0x2C8) * 1) + 0x428) + 0x8))))) goto loc_0025CD26;
    if ((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(Arg3) * 8 + *(uint64_t *)(arg2 + 0x2C8) * 1) + 0x428) + Arg3 * 2 + 0xC)) == ((uint16_t)(v_stack_m128))) goto loc_0025D5FA;
    Arg3 = (uint32_t)((Arg3) + 1);
    goto loc_0025D11A;
loc_0025D145:
    result = 0;
loc_0025D14E:
    v_stack_mF4 = 0;
    v_stack_m100 = v_stack_m108;
    v_stack_mF8 = (uint32_t)((uint32_t)((uint32_t)(local_r14)));
    if (0 >= ((uint32_t)((uint32_t)(Arg4)))) goto loc_0025D19B;
    result = (result) + (0);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mE0 + result * 8 + 0x8)))) > ((uint32_t)((uint32_t)((uint32_t)(local_r14))))) goto loc_0025D367;
    result = memcpy(v_stack_m108, *(uint64_t *)(v_stack_mE0 + result * 8), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mE0 + result * 8 + 0x8)))), v_stack_m108);
    Arg4 = (v_stack_m100) + ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mE0 + result * 8 + 0x8)))));
    Arg3 = (uint32_t)(((uint32_t)(v_stack_mF8)) - ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mE0 + result * 8 + 0x8)))))));
    result = (uint32_t)(((uint32_t)(v_stack_mF4)) + 1);
    goto loc_0025D14E;
loc_0025D19B:
loc_0025D19F:
    if (((*(uint32_t *)(*(uint64_t *)((uint32_t)(Arg3) * 8 + *(uint64_t *)(arg2 + 0x2C8) * 1) + 0xC)) & (0x80000ULL)) != 0) goto loc_0025D669;
loc_0025D1AC:
    if (*(uint64_t *)(*(uint64_t *)((uint32_t)(Arg3) * 8 + *(uint64_t *)(arg2 + 0x2C8) * 1) + 0x620) != 0) goto loc_0025D433;
loc_0025D1BC:
loc_0025D1C6:
    Arg1 = (v_stack_mD8) ^ (*(uint64_t *)(v_stack_mD0));
    if (Arg1 >= 15) goto loc_0025D5F1;
    if (Arg1 != 15) goto loc_0025D1C6;
loc_0025D1E9:
    if (sign_flag) goto loc_0025D22A;
loc_0025D1F3:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)((uint32_t)(Arg3) * 8 + *(uint64_t *)(arg2 + 0x2C8) * 1) + 0x334)))) & (2)) != 0) goto loc_0025D621;
loc_0025D201:
    if (((*(uint32_t *)(*(uint64_t *)((uint32_t)(Arg3) * 8 + *(uint64_t *)(arg2 + 0x2C8) * 1) + 0x330)) & (0x8000ULL)) != 0) goto loc_0025D4C2;
loc_0025D211:
    if (((*(uint32_t *)(*(uint64_t *)((uint32_t)(Arg3) * 8 + *(uint64_t *)(arg2 + 0x2C8) * 1) + 0x330)) & (0x4000000ULL)) != 0) goto loc_0025D643;
loc_0025D221:
    goto loc_0025CED0;
loc_0025D22A:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(v_stack_mE8))) & (0x1FFFULL));
    Arg1 = (uint32_t)((Arg1) & (7));
    result = ((uint32_t)((uint32_t)(Arg1))) >> (3);
    result = (result) + (*(uint64_t *)(*(uint64_t *)((uint32_t)(Arg3) * 8 + *(uint64_t *)(arg2 + 0x2C8) * 1) + 0x418));
    result = (uint8_t)((*(uint8_t *)(result)) >> ((uint8_t)(Arg1)));
    if (((1) & ((uint8_t)(result))) == 0) goto loc_0025D1F3;
    v_stack_m108 = v_cr8;
    if (condition_is_below) goto loc_0025D3B9;
loc_0025D26B:
    if (condition_is_above_or_equal) goto loc_0025D336;
    Arg1 = 0;
    if (condition_is_below) goto loc_0025D336;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg6)))) & (0x8000ULL));
    v_stack_m100 = *(uint64_t *)(gs_base + (0 + 0x188));
    v_stack_m120 = (uint32_t)(result);
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg6)))) & (0x4000000ULL));
    if ((*(uint64_t *)(gs_base + (0 + 0x188))) != (*(uint64_t *)(gs_base + (0 + 0x188)))) goto loc_0025D87A;
    if (((*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x74)) & (0x400ULL)) != 0) goto loc_0025D56C;
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5A0))))) != 0) goto loc_0025D3D1;
loc_0025D2CB:
    result = KeAreInterruptsEnabled(Arg1, Arg2, *(uint64_t *)(gs_base + (0 + 0x188)), *(uint64_t *)(*(uint64_t *)((uint32_t)(Arg3) * 8 + *(uint64_t *)(arg2 + 0x2C8) * 1) + 0x620));
    if ((uint8_t)(result) == 0) goto loc_0025D49B;
    if (((uint8_t)(v_cr8)) >= 2) goto loc_0025D49B;
    result = MmCanThreadFault(Arg1, Arg2, *(uint64_t *)(gs_base + (0 + 0x188)), *(uint64_t *)(*(uint64_t *)((uint32_t)(Arg3) * 8 + *(uint64_t *)(arg2 + 0x2C8) * 1) + 0x620));
    if ((uint32_t)(result) != 0) goto loc_0025D573;
loc_0025D2F1:
loc_0025D2F5:
loc_0025D2F9:
loc_0025D2FD:
    result = 1;
    if (condition_is_below) { result = 1; }
    if (1 == 0) goto loc_0025D491;
    if ((uint8_t)(result) == 0) goto loc_0025D336;
    result = (uint32_t)((*(uint16_t *)(*(uint64_t *)((uint32_t)(Arg3) * 8 + *(uint64_t *)(arg2 + 0x2C8) * 1) + 0x332)) & (7));
    result = (uint32_t)((result) + (24));
    v_stack_m120 = (uint32_t)(result);
    if (condition_is_above_or_equal) goto loc_0025D3DE;
loc_0025D336:
    if ((((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg6))))) & (0x1800ULL)) == 0) goto loc_0025D1F3;
    result = EtwpTraceStackWalk(*(uint64_t *)((uint32_t)(Arg3) * 8 + *(uint64_t *)(arg2 + 0x2C8) * 1), (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg6))))), *(uint64_t *)(gs_base + (0 + 0x188)), v_stack_m118);
    goto loc_0025D1F3;
loc_0025D35A:
    if ((uint8_t)(result) == 0) goto loc_0025D0ED;
    goto loc_0025CDB7;
loc_0025D367:
    Arg2 = 0;
    result = memset(v_stack_m108, Arg2, (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg6))))), v_stack_m118);
    result = EtwpUpdateEventsLostCount(*(uint64_t *)((uint32_t)(Arg3) * 8 + *(uint64_t *)(arg2 + 0x2C8) * 1), Arg2, (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg6))))), v_stack_m118);
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0xCA24BC), v_rip - 2411939, (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg6))))), v_stack_m118);
    if ((uint8_t)(result) == 0) goto loc_0025D19F;
    result = EtwpTraceLostSystemEvent((uint16_t)(v_stack_m128), *(uint64_t *)((uint32_t)(Arg3) * 8 + *(uint64_t *)(arg2 + 0x2C8) * 1) + 136, (uint32_t)((uint32_t)((uint32_t)(Arg6))), (uint32_t)(0xC0000004ULL));
    goto loc_0025D19F;
loc_0025D3B9:
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x18)) == (*(uint64_t *)(gs_base + (0 + 0x188)))) goto loc_0025D1F3;
    goto loc_0025D26B;
loc_0025D3D1:
    if ((uint32_t)(*(uint64_t *)((uint32_t)(Arg3) * 8 + *(uint64_t *)(arg2 + 0x2C8) * 1) + 136) != 0) goto loc_0025D2CB;
    goto loc_0025D2FD;
loc_0025D3DE:
    v_stack_p38 = (uint32_t)(v_stack_m118);
    v_stack_p30 = (uint32_t)(v_stack_m114);
    v_stack_p28 = 0;
    v_stack_p20 = v_rip + 2469993;
    result = EtwpQueueApc(*(uint64_t *)((uint32_t)(Arg3) * 8 + *(uint64_t *)(arg2 + 0x2C8) * 1) + 832, *(uint64_t *)(gs_base + (0 + 0x188)), (uint8_t)(v_stack_m108), v_rip - 220034);
    if (!sign_flag) goto loc_0025D336;
    goto loc_0025D336;
loc_0025D433:
    v_stack_mF0 = 0;
    result = EtwpGetNextEventOffsetType(v_stack_mD8, (uint32_t)((uint32_t)(v_stack_mC8)), v_stack_mF0, v_rip - 220034);
    if ((uint32_t)(result) == 0) goto loc_0025D1BC;
    Arg1 = 0;
    result = KeIsTraceCallbackAllowed(Arg1, (uint32_t)((uint32_t)(v_stack_mC8)), v_stack_mF0, v_rip - 220034);
    if ((uint32_t)(result) == 0) goto loc_0025D1BC;
    Arg3 = 0;
    Arg4 = 0;
    v_stack_p20 = *(uint64_t *)(v_rip - 0x35B82 + 0x8);
    Arg1 = ((uint32_t)((uint32_t)(v_stack_mC8))) + (v_stack_mD8);
    result = guard_dispatch_icall(Arg1, (uint32_t)(v_stack_mF0), Arg3, Arg4);
    goto loc_0025D1BC;
loc_0025D491:
    goto loc_0025D336;
loc_0025D49B:
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x20)) == 0) goto loc_0025D2F1;
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x20))) == 1) goto loc_0025D5E2;
loc_0025D4B9:
    Arg2 = 0;
    Arg1 = 0;
    goto loc_0025D2F9;
loc_0025D4C2:
    Arg2 = 0;
loc_0025D4C4:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(Arg3) * 8 + *(uint64_t *)(arg2 + 0x2C8) * 1) + 0x430) + 0x8))))) goto loc_0025D211;
    if ((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(Arg3) * 8 + *(uint64_t *)(arg2 + 0x2C8) * 1) + 0x430) + arg2 * 2 + 0xC)) == ((uint16_t)(v_stack_m128))) goto loc_0025D73F;
    Arg2 = (uint32_t)((Arg2) + 1);
    goto loc_0025D4C4;
loc_0025D4EC:
    result = EtwpReserveTraceBuffer((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(Arg3) * 8 + *(uint64_t *)(arg2 + 0x2C8) * 1) + 0x430) + 0x8)), v_stack_mD8 + 24, Arg3, Arg4);
    if (result == 0) goto loc_0025CD7B;
    *(uint16_t *)(result + 0x6) = (uint16_t)(v_stack_m128);
    Arg1 = (uint32_t)(((uint8_t)((uint32_t)(Arg6))) | (0xC0040000ULL));
    *(uint32_t *)(result) = (uint32_t)(Arg1);
    *(uint64_t *)(result + 0x10) = v_stack_m118;
    *(uint16_t *)(result + 0x4) = (uint16_t)(v_stack_mD8 + 24);
    *(uint32_t *)(result + 0x8) = (uint32_t)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x510));
    *(uint32_t *)(result + 0xC) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x1D0)));
    goto loc_0025CD6E;
loc_0025D55F:
    if ((uint8_t)(result + 24) == 0) goto loc_0025CDDD;
    goto loc_0025CED0;
loc_0025D56C:
    Arg2 = 0;
    goto loc_0025D2FD;
loc_0025D573:
    if ((*(uint8_t *)(v_stack_m100 + 0x5AE)) != 0) goto loc_0025D2F1;
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x24A)) == 1) goto loc_0025D2F1;
    if (((*(uint8_t *)(v_stack_m100 + 0x7D)) & (4)) != 0) goto loc_0025D2F1;
    Arg1 = 0;
    goto loc_0025D2F5;
loc_0025D5AB:
    if (0 != ((uint16_t)((uint32_t)(0x524ULL)))) goto loc_0025D10D;
    v_stack_p28 = (uint32_t)((uint32_t)(Arg6));
    v_stack_p20 = v_stack_m118;
    result = EtwpReserveWithPebsIndex(*(uint64_t *)((uint32_t)(Arg3) * 8 + *(uint64_t *)(arg2 + 0x2C8) * 1), (uint32_t)((uint32_t)((uint32_t)(0x524ULL))), (uint32_t)((uint32_t)(v_stack_mD8)), v_stack_mD8);
    goto loc_0025CD6E;
loc_0025D5E2:
    if (v_stack_m120 == 0) goto loc_0025D4B9;
    goto loc_0025D2F1;
loc_0025D5F1:
    goto loc_0025D1E9;
loc_0025D5FA:
    v_stack_p28 = (uint32_t)((uint32_t)(Arg6));
    v_stack_p20 = v_stack_m118;
    result = EtwpReserveWithPmcCounters(*(uint64_t *)((uint32_t)(Arg3) * 8 + *(uint64_t *)(arg2 + 0x2C8) * 1), (uint32_t)((uint32_t)((uint32_t)(0x524ULL))), (uint32_t)((uint32_t)(v_stack_mD8)), v_stack_mD8);
    goto loc_0025CD6E;
loc_0025D621:
    Arg1 = 0;
loc_0025D623:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)((uint32_t)(Arg3) * 8 + *(uint64_t *)(arg2 + 0x2C8) * 1) + 0x504))))) goto loc_0025D201;
    if ((*(uint16_t *)(*(uint64_t *)((uint32_t)(Arg3) * 8 + *(uint64_t *)(arg2 + 0x2C8) * 1) + arg1 * 2 + 0x508)) == ((uint16_t)(v_stack_m128))) goto loc_0025D881;
    Arg1 = (uint32_t)((Arg1) + 1);
    goto loc_0025D623;
loc_0025D643:
    Arg2 = 0;
loc_0025D645:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(Arg3) * 8 + *(uint64_t *)(arg2 + 0x2C8) * 1) + 0x438) + 0x18))))) goto loc_0025D221;
    if ((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(Arg3) * 8 + *(uint64_t *)(arg2 + 0x2C8) * 1) + 0x438) + arg2 * 2 + 0x1C)) == ((uint16_t)(v_stack_m128))) goto loc_0025D6A5;
    Arg2 = (uint32_t)((Arg2) + 1);
    goto loc_0025D645;
loc_0025D669:
    if ((*(uint8_t *)(v_rip + 0xBAD3AC)) == 0) goto loc_0025D69A;
loc_0025D672:
    if ((*(uint8_t *)(v_rip + 0xCF863A)) == 0) goto loc_0025D1AC;
loc_0025D67F:
    result = EtwpSendTraceEvent(*(uint64_t *)((uint32_t)(Arg3) * 8 + *(uint64_t *)(arg2 + 0x2C8) * 1), v_stack_mD8, (uint32_t)((uint32_t)(v_stack_mD8)), v_stack_m128);
    goto loc_0025D1AC;
loc_0025D690:
    goto loc_0025CD99;
loc_0025D69A:
    if ((*(uint8_t *)(v_rip + 0xCE9F3B)) == 0) goto loc_0025D67F;
    goto loc_0025D672;
loc_0025D6A5:
    v_stack_m74 = 0;
    v_stack_m88 = v_xmm0;
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x18)) == (*(uint64_t *)(gs_base + (0 + 0x188)))) goto loc_0025D221;
    if ((((uint32_t)((uint32_t)(Arg6))) & (0x1800ULL)) == 0) goto loc_0025D221;
    v_stack_mA8 = *(uint64_t *)((uint32_t)(Arg3) * 8 + *(uint64_t *)(arg2 + 0x2C8) * 1);
    v_stack_m78 = (uint32_t)((uint32_t)(Arg6));
    v_stack_m98 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x508)));
    v_stack_m94 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x510)));
    v_stack_mA0 = v_stack_m118;
    v_stack_m90 = *(uint64_t *)(*(uint64_t *)((uint32_t)(Arg3) * 8 + *(uint64_t *)(arg2 + 0x2C8) * 1) + 0x8);
    result = guard_dispatch_icall(*(uint64_t *)(*(uint64_t *)((uint32_t)(Arg3) * 8 + *(uint64_t *)(arg2 + 0x2C8) * 1)), v_stack_mA8, (uint32_t)((uint32_t)(v_stack_mD8)), v_stack_m128);
    goto loc_0025CED0;
loc_0025D73F:
    v_stack_m110 = 0;
    v_stack_mA8 = v_xmm0;
    v_stack_mC0 = 0;
    v_stack_m98 = v_xmm0;
    v_stack_mE0 = 0;
    v_stack_m88 = v_xmm0;
    v_stack_m128 = 0;
    v_stack_m100 = *(uint64_t *)(gs_base + (0 + 0x188));
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x18)) == (*(uint64_t *)(gs_base + (0 + 0x188)))) goto loc_0025D211;
    if ((((uint32_t)((uint32_t)(Arg6))) & (0x1800ULL)) == 0) goto loc_0025D211;
    result = KeGetCurrentStackPointer(*(uint64_t *)(gs_base + (0 + 0x188)), v_stack_mA8, (uint32_t)((uint32_t)(v_stack_mD8)), v_stack_m128);
    result = KeQueryCurrentStackInformationEx(result, v_stack_m128, v_stack_mE0, v_stack_mC0);
    if ((uint8_t)(result) == 0) goto loc_0025D211;
    if (((uint32_t)((uint32_t)(v_stack_m128))) > 9) goto loc_0025D7D9;
    if (((uint32_t)((uint32_t)(v_stack_m128))) < 9) goto loc_0025D211;
loc_0025D7D9:
    v_stack_m128 = 0;
    local_r14 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xD695C1)) + (uint32_t)(*(uint32_t *)(v_rip + 0xD695C1)) * 2) << (3));
    result = ExpInterlockedPopEntrySList(v_rip + 12367818, v_stack_m128, v_stack_mE0, v_stack_mC0);
    if (result == 0) goto loc_0025D842;
    if (result + 16 == 0) goto loc_0025D842;
    result = guard_dispatch_icall((uint32_t)((uint32_t)(local_r14)), result + 16, v_stack_m110, v_stack_mC0);
    if (v_stack_m128 != 0) goto loc_0025D211;
    result = ExpInterlockedPushEntrySList(v_rip + 12367736, result + 16 - 16, v_stack_m110, v_stack_mC0);
    goto loc_0025D211;
loc_0025D842:
    result = KeGetCurrentStackPointer(v_rip + 12367736, result + 16 - 16, v_stack_m110, v_stack_mC0);
    result = (result) - (v_stack_mE0);
    if (result <= (local_r14 + 3632)) goto loc_0025D211;
loc_0025D87A:
    Arg2 = 0;
    goto loc_0025D2FD;
loc_0025D881:
    Arg3 = 0;
    result = EtwpContextRegisterTracingDispatcher(*(uint64_t *)((uint32_t)(Arg3) * 8 + *(uint64_t *)(arg2 + 0x2C8) * 1), v_stack_m118, Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg6))));
    goto loc_0025D201;
loc_0025D898:
    Arg4 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg6)))) | (8));
    goto loc_0025CE9C;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8 + r8*8` | `32` | `R` |
| `Arg1` | `+ 0x8 + r9*8` | `32` | `R` |
| `Arg1` | `+ 0x8 + rcx*8` | `32` | `R` |
| `Arg1` | `+ 0x8 + rdx*8` | `32` | `R` |
| `Arg2` | `+ 0x2C0` | `64` | `R` |
| `Arg2` | `+ 0x2C8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0025CC00&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
