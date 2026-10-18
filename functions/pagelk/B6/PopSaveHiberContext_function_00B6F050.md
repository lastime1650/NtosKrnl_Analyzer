# PopSaveHiberContext

- RVA: `0x00B6F050`–`0x00B6FB03` (길이 `2,739` bytes)
- VA: `0x0000000140B6F050`
- 실행 섹션: `PAGELK`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CC3EC`
- 디코드: `633`개 명령, `2,739/2,739` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **56**; 고유 호출 대상: **43**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **54**

### Outgoing calls
- `0x00B6F0B0` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00B6F0BF` → [Feature_CrashDumpOneMBTransferSize__private_IsEnabledDeviceUsageNoInline](../../text/5D/Feature_CrashDumpOneMBTransferSize__private_IsEnabledDeviceUsageNoInline_function_005D4A08.md) (function, `0x005D4A08`)
- `0x00B6F0F8` → [PopCheckpointSystemSleep](../B7/PopCheckpointSystemSleep_function_00B77C90.md) (function, `0x00B77C90`)
- `0x00B6F16A` → [KeDisableInterrupts](../../text/21/KeDisableInterrupts_function_00217BE0.md) (function, `0x00217BE0`)
- `0x00B6F178` → [PopInternalError](../../text/5C/PopInternalError_function_005CEBD0.md) (function, `0x005CEBD0`)
- `0x00B6F19F` → [PopCompressHiberBlocks](PopCompressHiberBlocks_function_00B6CD74.md) (function, `0x00B6CD74`)
- `0x00B6F1C5` → [PopCompressHiberBlocks](PopCompressHiberBlocks_function_00B6CD74.md) (function, `0x00B6CD74`)
- `0x00B6F1E7` → [IoDumpStackResumeCapable](../../text/59/IoDumpStackResumeCapable_function_00591E9C.md) (function, `0x00591E9C`)
- `0x00B6F202` → `PSHED.dll!PshedArePluginsPresent` (import, 간접 대상; import `PSHED.dll!PshedArePluginsPresent`)
- `0x00B6F227` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00B6F247` → [PopIsMktmeEnabled](PopIsMktmeEnabled_function_00B6E054.md) (function, `0x00B6E054`)
- `0x00B6F266` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00B6F2A6` → [HvlDisableEnlightenment](../../text/58/HvlDisableEnlightenment_function_00583AF8.md) (function, `0x00583AF8`)
- `0x00B6F2B2` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00B6F397` → [HvlPrepareForSecureHibernate](../../text/58/HvlPrepareForSecureHibernate_function_0058A7EC.md) (function, `0x0058A7EC`)
- `0x00B6F3E3` → [HvlPrepareForHibernate](../../text/58/HvlPrepareForHibernate_function_0058A6C4.md) (function, `0x0058A6C4`)
- `0x00B6F3FD` → [PopInternalAddToDumpFile](../../text/5C/PopInternalAddToDumpFile_function_005CE634.md) (function, `0x005CE634`)
- `0x00B6F41B` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00B6F456` → [HvlDiscardSecurePagesFromHibernation](../../text/58/HvlDiscardSecurePagesFromHibernation_function_0058A444.md) (function, `0x0058A444`)
- `0x00B6F45D` → [HvlDiscardPagesFromHibernation](../../text/58/HvlDiscardPagesFromHibernation_function_0058A3DC.md) (function, `0x0058A3DC`)
- `0x00B6F48F` → [PopSstInvokeNotificationHandlers](PopSstInvokeNotificationHandlers_function_00B6C1D0.md) (function, `0x00B6C1D0`)
- `0x00B6F4DF` → [RtlCopyBitMap](../../text/3E/RtlCopyBitMap_function_003E2210.md) (function, `0x003E2210`)
- `0x00B6F4EB` → [RtlSetAllBits](../../text/36/RtlSetAllBits_function_00362490.md) (function, `0x00362490`)
- `0x00B6F509` → [IoGetDumpHiberRanges](../../text/59/IoGetDumpHiberRanges_function_005928AC.md) (function, `0x005928AC`)
- `0x00B6F51A` → [IoNotifyDump](../../text/59/IoNotifyDump_function_00592B60.md) (function, `0x00592B60`)
- `0x00B6F532` → [IoInitializeDumpStack](../../text/59/IoInitializeDumpStack_function_00592A50.md) (function, `0x00592A50`)
- `0x00B6F53A` → [Feature_CrashDumpOneMBTransferSize__private_IsEnabledDeviceUsageNoInline](../../text/5D/Feature_CrashDumpOneMBTransferSize__private_IsEnabledDeviceUsageNoInline_function_005D4A08.md) (function, `0x005D4A08`)
- `0x00B6F54A` → [IoGetDumpStackTransferSizes](../../text/59/IoGetDumpStackTransferSizes_function_00592A0C.md) (function, `0x00592A0C`)
- `0x00B6F5A5` → [PopMarkComponentsBootPhase](PopMarkComponentsBootPhase_function_00B6E0E4.md) (function, `0x00B6E0E4`)
- `0x00B6F5E8` → [PopCreateDumpMdl](PopCreateDumpMdl_function_00B6CF5C.md) (function, `0x00B6CF5C`)
- `0x00B6F5F8` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00B6F61E` → [PopResetRangeEnum](../../text/5D/PopResetRangeEnum_function_005D4F7C.md) (function, `0x005D4F7C`)
- `0x00B6F650` → [PopWriteHeaderPages](PopWriteHeaderPages_function_00B6FC14.md) (function, `0x00B6FC14`)
- `0x00B6F6A1` → [PopWriteSecurePages](../../text/5D/PopWriteSecurePages_function_005D4F94.md) (function, `0x005D4F94`)
- `0x00B6F6D8` → [RtlNumberOfClearBits](../../text/43/RtlNumberOfClearBits_function_00433F40.md) (function, `0x00433F40`)
- `0x00B6F708` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00B6F7AA` → [PopWriteHiberImage](PopWriteHiberImage_function_00B6FE30.md) (function, `0x00B6FE30`)
- `0x00B6F902` → [RtlNumberOfClearBits](../../text/43/RtlNumberOfClearBits_function_00433F40.md) (function, `0x00433F40`)
- `0x00B6F92C` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00B6F97C` → [PopWriteHiberImage](PopWriteHiberImage_function_00B6FE30.md) (function, `0x00B6FE30`)
- `0x00B6F9AB` → [PopHiberWriteBootFreePageMap](PopHiberWriteBootFreePageMap_function_00B6DFAC.md) (function, `0x00B6DFAC`)
- `0x00B6F9BE` → [PopWriteChecksumPages](PopWriteChecksumPages_function_00B6FB7C.md) (function, `0x00B6FB7C`)
- `0x00B6F9DC` → [PopWriteImageHeader](../B7/PopWriteImageHeader_function_00B70290.md) (function, `0x00B70290`)
- `0x00B6FA0F` → [DbgUnLoadImageSymbols](../../text/4C/DbgUnLoadImageSymbols_function_004C6690.md) (function, `0x004C6690`)
- `0x00B6FA16` → [VslNotifyShutdown](../../text/58/VslNotifyShutdown_function_0058EBC8.md) (function, `0x0058EBC8`)
- `0x00B6FA2C` → [HalReturnToFirmware](../../text/54/HalReturnToFirmware_function_00546550.md) (function, `0x00546550`)
- `0x00B6FA49` → [KdPowerTransition](../../text/4F/KdPowerTransition_function_004F9AC0.md) (function, `0x004F9AC0`)
- `0x00B6FA63` → [PopNotifyShutdownListener](../B7/PopNotifyShutdownListener_function_00B7170C.md) (function, `0x00B7170C`)
- `0x00B6FA73` → [HvlConfigureMemoryZeroingOnReset](../../text/58/HvlConfigureMemoryZeroingOnReset_function_00583760.md) (function, `0x00583760`)
- `0x00B6FA78` → [PopSetMemoryOverwriteRequestAction](PopSetMemoryOverwriteRequestAction_function_00B6BE14.md) (function, `0x00B6BE14`)
- `0x00B6FA82` → [PopCheckpointSystemSleep](../B7/PopCheckpointSystemSleep_function_00B77C90.md) (function, `0x00B77C90`)
- `0x00B6FA8E` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00B6FA9F` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00B6FACB` → [PopCheckpointSystemSleep](../B7/PopCheckpointSystemSleep_function_00B77C90.md) (function, `0x00B77C90`)
- `0x00B6FADF` → [PopInternalAddToDumpFile](../../text/5C/PopInternalAddToDumpFile_function_005CE634.md) (function, `0x005CE634`)
- `0x00B6FAFD` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)

### Direct callers
- [PopSaveHiberContextWrapper](../../text/6B/PopSaveHiberContextWrapper_function_006BA360.md) at `0x006BA3B3`

### Static image references
- `0x00B6F076` → RVA `0x00E0A740` (`.data`; read)
- `0x00B6F0FF` → RVA `0x00FC6A90` (`ALMOSTRO`; read)
- `0x00B6F10E` → RVA `0x00FC6A84` (`ALMOSTRO`; read)
- `0x00B6F12C` → RVA `0x00F0C680` (`.data`; read)
- `0x00B6F164` → RVA `0x00F0DDA4` (`.data`; write)
- `0x00B6F1D1` → RVA `0x00F0C2E0` (`.data`; read)
- `0x00B6F1F4` → RVA `0x00F0BFF8` (`.data`; read/write)
- `0x00B6F1FB` → RVA `0x00F0BF61` (`.data`; write)
- `0x00B6F202` → RVA `0x001510C0` (`PSHED.dll!PshedArePluginsPresent (IAT)`; read)
- `0x00B6F220` → RVA `0x00E00AB0` (`.data`; read)
- `0x00B6F23E` → RVA `0x00F0BF61` (`.data`; read)
- `0x00B6F26C` → RVA `0x00FC6A97` (`ALMOSTRO`; read)
- `0x00B6F285` → RVA `0x00E27710` (`.data`; read)
- `0x00B6F29F` → RVA `0x00F0DE5C` (`.data`; write)
- `0x00B6F2AB` → RVA `0x00E00A00` (`.data`; read)
- `0x00B6F2E4` → RVA `0x00FC6A80` (`ALMOSTRO`; read)
- `0x00B6F2EE` → RVA `0x00E278F8` (`.data`; read)
- `0x00B6F2FA` → RVA `0x00E27898` (`.data`; read)
- `0x00B6F306` → RVA `0x00E278A0` (`.data`; read)
- `0x00B6F317` → RVA `0x00E27890` (`.data`; read)
- `0x00B6F323` → RVA `0x00E278B0` (`.data`; read)
- `0x00B6F333` → RVA `0x00E278A8` (`.data`; read)
- `0x00B6F33E` → RVA `0x00E278D8` (`.data`; read)
- `0x00B6F349` → RVA `0x00E278E0` (`.data`; read)
- `0x00B6F354` → RVA `0x00E278E8` (`.data`; read)
- `0x00B6F35F` → RVA `0x00E278F0` (`.data`; read)
- `0x00B6F46B` → RVA `0x00B6DC80` (`PopHiberNotificationDiscardMemoryCallback`; read)
- `0x00B6F481` → RVA `0x00B6DCB0` (`PopHiberNotificationDiscardPhysicalMemoryCallback`; read)
- `0x00B6F4FB` → RVA `0x00F0DE58` (`.data`; write)
- `0x00B6F586` → RVA `0x00F0C388` (`.data`; read/write)
- `0x00B6F62A` → RVA `0x00F0BF38` (`.data`; read)
- `0x00B6F69A` → RVA `0x00F0C378` (`.data`; read)
- `0x00B6F6B0` → RVA `0x00F0C658` (`.data`; write)
- `0x00B6F6BE` → RVA `0x00F0C530` (`.data`; write)
- `0x00B6F6E3` → RVA `0x00F0BFC8` (`.data`; read)
- `0x00B6F720` → RVA `0x00F0C538` (`.data`; write)
- `0x00B6F727` → RVA `0x00F0C540` (`.data`; write)
- `0x00B6F7DF` → RVA `0x00F0C660` (`.data`; write)
- `0x00B6F7F3` → RVA `0x00F0C5F8` (`.data`; read)
- `0x00B6F84F` → RVA `0x00F0C398` (`.data`; read/write)
- `0x00B6F882` → RVA `0x00F0C538` (`.data`; read/write)
- `0x00B6F8BD` → RVA `0x00F0C648` (`.data`; write)
- `0x00B6F8C4` → RVA `0x00F0C568` (`.data`; read)
- `0x00B6F8CB` → RVA `0x00F0C548` (`.data`; write)
- `0x00B6F8D2` → RVA `0x00F0C570` (`.data`; read)
- `0x00B6F8D8` → RVA `0x00F0C558` (`.data`; write)
- `0x00B6F8DF` → RVA `0x00F0C568` (`.data`; write)
- `0x00B6F8E6` → RVA `0x00F0C570` (`.data`; write)
- `0x00B6F993` → RVA `0x00F0C668` (`.data`; write)
- `0x00B6F9A4` → RVA `0x00F0C650` (`.data`; write)
- `0x00B6F9EC` → RVA `0x00F0BD74` (`.data`; read)
- `0x00B6F9F2` → RVA `0x00F0BD6C` (`.data`; read)
- `0x00B6F9FA` → RVA `0x00F0CF0C` (`.data`; read)
- `0x00B6FA87` → RVA `0x00E00B28` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **38**
  - `0x00B6F0B0` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGELK` → `.text`)
  - `0x00B6F0BF` → [Feature_CrashDumpOneMBTransferSize__private_IsEnabledDeviceUsageNoInline](../../text/5D/Feature_CrashDumpOneMBTransferSize__private_IsEnabledDeviceUsageNoInline_function_005D4A08.md) (`PAGELK` → `.text`)
  - `0x00B6F16A` → [KeDisableInterrupts](../../text/21/KeDisableInterrupts_function_00217BE0.md) (`PAGELK` → `.text`)
  - `0x00B6F178` → [PopInternalError](../../text/5C/PopInternalError_function_005CEBD0.md) (`PAGELK` → `.text`)
  - `0x00B6F1E7` → [IoDumpStackResumeCapable](../../text/59/IoDumpStackResumeCapable_function_00591E9C.md) (`PAGELK` → `.text`)
  - `0x00B6F227` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGELK` → `.text`)
  - `0x00B6F266` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGELK` → `.text`)
  - `0x00B6F2A6` → [HvlDisableEnlightenment](../../text/58/HvlDisableEnlightenment_function_00583AF8.md) (`PAGELK` → `.text`)
  - `0x00B6F2B2` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGELK` → `.text`)
  - `0x00B6F397` → [HvlPrepareForSecureHibernate](../../text/58/HvlPrepareForSecureHibernate_function_0058A7EC.md) (`PAGELK` → `.text`)
  - `0x00B6F3E3` → [HvlPrepareForHibernate](../../text/58/HvlPrepareForHibernate_function_0058A6C4.md) (`PAGELK` → `.text`)
  - `0x00B6F3FD` → [PopInternalAddToDumpFile](../../text/5C/PopInternalAddToDumpFile_function_005CE634.md) (`PAGELK` → `.text`)
  - `0x00B6F41B` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGELK` → `.text`)
  - `0x00B6F456` → [HvlDiscardSecurePagesFromHibernation](../../text/58/HvlDiscardSecurePagesFromHibernation_function_0058A444.md) (`PAGELK` → `.text`)
  - `0x00B6F45D` → [HvlDiscardPagesFromHibernation](../../text/58/HvlDiscardPagesFromHibernation_function_0058A3DC.md) (`PAGELK` → `.text`)
  - `0x00B6F4DF` → [RtlCopyBitMap](../../text/3E/RtlCopyBitMap_function_003E2210.md) (`PAGELK` → `.text`)
  - `0x00B6F4EB` → [RtlSetAllBits](../../text/36/RtlSetAllBits_function_00362490.md) (`PAGELK` → `.text`)
  - `0x00B6F509` → [IoGetDumpHiberRanges](../../text/59/IoGetDumpHiberRanges_function_005928AC.md) (`PAGELK` → `.text`)
  - `0x00B6F51A` → [IoNotifyDump](../../text/59/IoNotifyDump_function_00592B60.md) (`PAGELK` → `.text`)
  - `0x00B6F532` → [IoInitializeDumpStack](../../text/59/IoInitializeDumpStack_function_00592A50.md) (`PAGELK` → `.text`)
  - `0x00B6F53A` → [Feature_CrashDumpOneMBTransferSize__private_IsEnabledDeviceUsageNoInline](../../text/5D/Feature_CrashDumpOneMBTransferSize__private_IsEnabledDeviceUsageNoInline_function_005D4A08.md) (`PAGELK` → `.text`)
  - `0x00B6F54A` → [IoGetDumpStackTransferSizes](../../text/59/IoGetDumpStackTransferSizes_function_00592A0C.md) (`PAGELK` → `.text`)
  - `0x00B6F5F8` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGELK` → `.text`)
  - `0x00B6F61E` → [PopResetRangeEnum](../../text/5D/PopResetRangeEnum_function_005D4F7C.md) (`PAGELK` → `.text`)
  - `0x00B6F6A1` → [PopWriteSecurePages](../../text/5D/PopWriteSecurePages_function_005D4F94.md) (`PAGELK` → `.text`)
  - `0x00B6F6D8` → [RtlNumberOfClearBits](../../text/43/RtlNumberOfClearBits_function_00433F40.md) (`PAGELK` → `.text`)
  - `0x00B6F708` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGELK` → `.text`)
  - `0x00B6F902` → [RtlNumberOfClearBits](../../text/43/RtlNumberOfClearBits_function_00433F40.md) (`PAGELK` → `.text`)
  - `0x00B6F92C` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGELK` → `.text`)
  - `0x00B6FA0F` → [DbgUnLoadImageSymbols](../../text/4C/DbgUnLoadImageSymbols_function_004C6690.md) (`PAGELK` → `.text`)
  - `0x00B6FA16` → [VslNotifyShutdown](../../text/58/VslNotifyShutdown_function_0058EBC8.md) (`PAGELK` → `.text`)
  - `0x00B6FA2C` → [HalReturnToFirmware](../../text/54/HalReturnToFirmware_function_00546550.md) (`PAGELK` → `.text`)
  - `0x00B6FA49` → [KdPowerTransition](../../text/4F/KdPowerTransition_function_004F9AC0.md) (`PAGELK` → `.text`)
  - `0x00B6FA73` → [HvlConfigureMemoryZeroingOnReset](../../text/58/HvlConfigureMemoryZeroingOnReset_function_00583760.md) (`PAGELK` → `.text`)
  - `0x00B6FA8E` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGELK` → `.text`)
  - `0x00B6FA9F` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGELK` → `.text`)
  - `0x00B6FADF` → [PopInternalAddToDumpFile](../../text/5C/PopInternalAddToDumpFile_function_005CE634.md) (`PAGELK` → `.text`)
  - `0x00B6FAFD` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGELK` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B6F050  48 8B C4                        mov rax, rsp
00B6F053  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
00B6F057  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
00B6F05B  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
00B6F05F  55                              push rbp
00B6F060  41 54                           push r12
00B6F062  41 55                           push r13
00B6F064  41 56                           push r14
00B6F066  41 57                           push r15
00B6F068  48 8D A8 18 FE FF FF            lea rbp, [rax - 0x1e8]
00B6F06F  48 81 EC C0 02 00 00            sub rsp, 0x2c0
00B6F076  48 8B 05 C3 B6 29 00            mov rax, qword ptr [rip + 0x29b6c3]
00B6F07D  48 33 C4                        xor rax, rsp
00B6F080  48 89 85 B0 01 00 00            mov qword ptr [rbp + 0x1b0], rax
00B6F087  33 C0                           xor eax, eax
00B6F089  4C 8B F9                        mov r15, rcx
00B6F08C  0F 57 C0                        xorps xmm0, xmm0
00B6F08F  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
00B6F093  0F 57 C9                        xorps xmm1, xmm1
00B6F096  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
00B6F09B  48 8D 4D 70                     lea rcx, [rbp + 0x70]
00B6F09F  33 D2                           xor edx, edx
00B6F0A1  41 B8 38 01 00 00               mov r8d, 0x138
00B6F0A7  0F 11 45 B0                     movups xmmword ptr [rbp - 0x50], xmm0
00B6F0AB  0F 11 4C 24 48                  movups xmmword ptr [rsp + 0x48], xmm1
00B6F0B0  E8 8B 7B B5 FF                  call 0x1406c6c40
00B6F0B5  33 F6                           xor esi, esi
00B6F0B7  89 74 24 40                     mov dword ptr [rsp + 0x40], esi
00B6F0BB  89 74 24 34                     mov dword ptr [rsp + 0x34], esi
00B6F0BF  E8 44 59 A6 FF                  call 0x1405d4a08
00B6F0C4  85 C0                           test eax, eax
00B6F0C6  75 0B                           jne 0x140b6f0d3
00B6F0C8  48 8D 4D 70                     lea rcx, [rbp + 0x70]
00B6F0CC  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
00B6F0D1  EB 0C                           jmp 0x140b6f0df
00B6F0D3  49 8B 87 60 01 00 00            mov rax, qword ptr [r15 + 0x160]
00B6F0DA  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00B6F0DF  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
00B6F0E8  41 BE 01 00 00 00               mov r14d, 1
00B6F0EE  8B 58 24                        mov ebx, dword ptr [rax + 0x24]
00B6F0F1  85 DB                           test ebx, ebx
00B6F0F3  75 0A                           jne 0x140b6f0ff
00B6F0F5  8D 4B 13                        lea ecx, [rbx + 0x13]
00B6F0F8  E8 93 8B 00 00                  call 0x140b77c90
00B6F0FD  EB 51                           jmp 0x140b6f150
00B6F0FF  F6 05 8A 79 45 00 02            test byte ptr [rip + 0x45798a], 2
00B6F106  40 0F B6 C6                     movzx eax, sil
00B6F10A  41 0F 45 C6                     cmovne eax, r14d
00B6F10E  40 38 35 6F 79 45 00            cmp byte ptr [rip + 0x45796f], sil
00B6F115  75 04                           jne 0x140b6f11b
00B6F117  84 C0                           test al, al
00B6F119  74 35                           je 0x140b6f150
00B6F11B  F0 45 01 77 10                  lock add dword ptr [r15 + 0x10], r14d
00B6F120  EB 02                           jmp 0x140b6f124
00B6F122  F3 90                           pause
00B6F124  41 8B 47 10                     mov eax, dword ptr [r15 + 0x10]
00B6F128  85 C0                           test eax, eax
00B6F12A  75 F6                           jne 0x140b6f122
00B6F12C  40 38 35 4D D5 39 00            cmp byte ptr [rip + 0x39d54d], sil
00B6F133  74 0A                           je 0x140b6f13f
00B6F135  BB 94 02 00 40                  mov ebx, 0x40000294
00B6F13A  E9 54 09 00 00                  jmp 0x140b6fa93
00B6F13F  F0 45 01 77 14                  lock add dword ptr [r15 + 0x14], r14d
00B6F144  EB 02                           jmp 0x140b6f148
00B6F146  F3 90                           pause
00B6F148  41 8B 47 14                     mov eax, dword ptr [r15 + 0x14]
00B6F14C  85 C0                           test eax, eax
00B6F14E  75 F6                           jne 0x140b6f146
00B6F150  41 3B 9F 20 01 00 00            cmp ebx, dword ptr [r15 + 0x120]
00B6F157  72 07                           jb 0x140b6f160
00B6F159  8B DE                           mov ebx, esi
00B6F15B  E9 33 09 00 00                  jmp 0x140b6fa93
00B6F160  85 DB                           test ebx, ebx
00B6F162  75 1C                           jne 0x140b6f180
00B6F164  89 35 3A EC 39 00               mov dword ptr [rip + 0x39ec3a], esi
00B6F16A  E8 71 8A 6A FF                  call 0x140217be0
00B6F16F  84 C0                           test al, al
00B6F171  74 5E                           je 0x140b6f1d1
00B6F173  B9 60 1E 0A 00                  mov ecx, 0xa1e60
00B6F178  E8 53 FA A5 FF                  call 0x1405cebd0
00B6F17D  CC                              int3
00B6F17E  F3 90                           pause
00B6F180  41 8A 47 03                     mov al, byte ptr [r15 + 3]
00B6F184  84 C0                           test al, al
00B6F186  74 F6                           je 0x140b6f17e
00B6F188  49 8B 97 28 01 00 00            mov rdx, qword ptr [r15 + 0x128]
00B6F18F  45 8A C6                        mov r8b, r14b
00B6F192  48 69 DB A8 00 00 00            imul rbx, rbx, 0xa8
00B6F199  49 8B CF                        mov rcx, r15
00B6F19C  48 03 D3                        add rdx, rbx
00B6F19F  E8 D0 DB FF FF                  call 0x140b6cd74
00B6F1A4  F0 45 01 77 08                  lock add dword ptr [r15 + 8], r14d
00B6F1A9  EB 02                           jmp 0x140b6f1ad
00B6F1AB  F3 90                           pause
00B6F1AD  41 8B 47 08                     mov eax, dword ptr [r15 + 8]
00B6F1B1  85 C0                           test eax, eax
00B6F1B3  75 F6                           jne 0x140b6f1ab
00B6F1B5  49 8B 97 28 01 00 00            mov rdx, qword ptr [r15 + 0x128]
00B6F1BC  45 33 C0                        xor r8d, r8d
00B6F1BF  48 03 D3                        add rdx, rbx
00B6F1C2  49 8B CF                        mov rcx, r15
00B6F1C5  E8 AA DB FF FF                  call 0x140b6cd74
00B6F1CA  8B D8                           mov ebx, eax
00B6F1CC  E9 C2 08 00 00                  jmp 0x140b6fa93
00B6F1D1  8B 05 09 D1 39 00               mov eax, dword ptr [rip + 0x39d109]
00B6F1D7  84 C0                           test al, al
00B6F1D9  79 07                           jns 0x140b6f1e2
00B6F1DB  40 88 74 24 30                  mov byte ptr [rsp + 0x30], sil
00B6F1E0  EB 12                           jmp 0x140b6f1f4
00B6F1E2  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
00B6F1E7  E8 B0 2C A2 FF                  call 0x140591e9c
00B6F1EC  88 44 24 30                     mov byte ptr [rsp + 0x30], al
00B6F1F0  84 C0                           test al, al
00B6F1F2  75 0E                           jne 0x140b6f202
00B6F1F4  83 0D FD CD 39 00 04            or dword ptr [rip + 0x39cdfd], 4
00B6F1FB  44 88 35 5F CD 39 00            mov byte ptr [rip + 0x39cd5f], r14b
00B6F202  48 FF 15 B7 1E 5E FF            call qword ptr [rip - 0xa1e149]
00B6F209  0F 1F 44 00 00                  nop dword ptr [rax + rax]
00B6F20E  85 C0                           test eax, eax
00B6F210  74 0E                           je 0x140b6f220
00B6F212  83 0D DF CD 39 00 08            or dword ptr [rip + 0x39cddf], 8
00B6F219  44 88 35 41 CD 39 00            mov byte ptr [rip + 0x39cd41], r14b
00B6F220  48 8B 05 89 18 29 00            mov rax, qword ptr [rip + 0x291889]
00B6F227  E8 A4 B8 B4 FF                  call 0x1406baad0
00B6F22C  84 C0                           test al, al
00B6F22E  75 0E                           jne 0x140b6f23e
00B6F230  44 09 35 C1 CD 39 00            or dword ptr [rip + 0x39cdc1], r14d
00B6F237  44 88 35 23 CD 39 00            mov byte ptr [rip + 0x39cd23], r14b
00B6F23E  40 38 35 1C CD 39 00            cmp byte ptr [rip + 0x39cd1c], sil
00B6F245  74 25                           je 0x140b6f26c
00B6F247  E8 08 EE FF FF                  call 0x140b6e054
00B6F24C  84 C0                           test al, al
00B6F24E  74 1C                           je 0x140b6f26c
00B6F250  BA 12 01 00 00                  mov edx, 0x112
00B6F255  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
00B6F25A  4D 8B CF                        mov r9, r15
00B6F25D  41 B8 0A 00 00 00               mov r8d, 0xa
00B6F263  8D 4A 8E                        lea ecx, [rdx - 0x72]
00B6F266  E8 F5 E3 98 FF                  call 0x1404fd660
00B6F26B  CC                              int3
00B6F26C  40 38 35 24 78 45 00            cmp byte ptr [rip + 0x457824], sil
00B6F273  48 8D 45 B0                     lea rax, [rbp - 0x50]
00B6F277  4D 8B AF D8 00 00 00            mov r13, qword ptr [r15 + 0xd8]
00B6F27E  49 89 87 B0 00 00 00            mov qword ptr [r15 + 0xb0], rax
00B6F285  48 8D 05 84 84 2B 00            lea rax, [rip + 0x2b8484]
00B6F28C  49 89 87 C0 00 00 00            mov qword ptr [r15 + 0xc0], rax
00B6F293  45 88 77 01                     mov byte ptr [r15 + 1], r14b
00B6F297  0F 84 C5 01 00 00               je 0x140b6f462
00B6F29D  33 C9                           xor ecx, ecx
00B6F29F  44 89 35 B6 EB 39 00            mov dword ptr [rip + 0x39ebb6], r14d
00B6F2A6  E8 4D 48 A1 FF                  call 0x140583af8
00B6F2AB  48 8B 05 4E 17 29 00            mov rax, qword ptr [rip + 0x29174e]
00B6F2B2  E8 19 B8 B4 FF                  call 0x1406baad0
00B6F2B7  F6 05 D2 77 45 00 02            test byte ptr [rip + 0x4577d2], 2
00B6F2BE  40 0F B6 C6                     movzx eax, sil
00B6F2C2  41 0F 45 C6                     cmovne eax, r14d
00B6F2C6  40 38 35 B7 77 45 00            cmp byte ptr [rip + 0x4577b7], sil
00B6F2CD  75 08                           jne 0x140b6f2d7
00B6F2CF  84 C0                           test al, al
00B6F2D1  0F 84 73 01 00 00               je 0x140b6f44a
00B6F2D7  F0 45 01 77 10                  lock add dword ptr [r15 + 0x10], r14d
00B6F2DC  EB 02                           jmp 0x140b6f2e0
00B6F2DE  F3 90                           pause
00B6F2E0  41 8B 4F 10                     mov ecx, dword ptr [r15 + 0x10]
00B6F2E4  8B 05 96 77 45 00               mov eax, dword ptr [rip + 0x457796]
00B6F2EA  3B C8                           cmp ecx, eax
00B6F2EC  75 F0                           jne 0x140b6f2de
00B6F2EE  48 8B 05 03 86 2B 00            mov rax, qword ptr [rip + 0x2b8603]
00B6F2F5  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00B6F2FA  48 8B 05 97 85 2B 00            mov rax, qword ptr [rip + 0x2b8597]
00B6F301  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
00B6F306  48 8B 05 93 85 2B 00            mov rax, qword ptr [rip + 0x2b8593]
00B6F30D  0F 28 44 24 60                  movaps xmm0, xmmword ptr [rsp + 0x60]
00B6F312  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
00B6F317  48 8B 05 72 85 2B 00            mov rax, qword ptr [rip + 0x2b8572]
00B6F31E  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
00B6F323  48 8B 05 86 85 2B 00            mov rax, qword ptr [rip + 0x2b8586]
00B6F32A  0F 28 4C 24 70                  movaps xmm1, xmmword ptr [rsp + 0x70]
00B6F32F  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
00B6F333  48 8B 05 6E 85 2B 00            mov rax, qword ptr [rip + 0x2b856e]
00B6F33A  48 89 45 88                     mov qword ptr [rbp - 0x78], rax
00B6F33E  48 8B 05 93 85 2B 00            mov rax, qword ptr [rip + 0x2b8593]
00B6F345  48 89 45 90                     mov qword ptr [rbp - 0x70], rax
00B6F349  48 8B 05 90 85 2B 00            mov rax, qword ptr [rip + 0x2b8590]
00B6F350  48 89 45 98                     mov qword ptr [rbp - 0x68], rax
00B6F354  48 8B 05 8D 85 2B 00            mov rax, qword ptr [rip + 0x2b858d]
00B6F35B  48 89 45 A0                     mov qword ptr [rbp - 0x60], rax
00B6F35F  48 8B 05 8A 85 2B 00            mov rax, qword ptr [rip + 0x2b858a]
00B6F366  48 89 45 A8                     mov qword ptr [rbp - 0x58], rax
00B6F36A  41 38 B7 E8 01 00 00            cmp byte ptr [r15 + 0x1e8], sil
00B6F371  74 2B                           je 0x140b6f39e
00B6F373  0F 29 45 D0                     movaps xmmword ptr [rbp - 0x30], xmm0
00B6F377  48 8D 4D D0                     lea rcx, [rbp - 0x30]
00B6F37B  0F 28 45 80                     movaps xmm0, xmmword ptr [rbp - 0x80]
00B6F37F  0F 29 45 F0                     movaps xmmword ptr [rbp - 0x10], xmm0
00B6F383  0F 28 45 A0                     movaps xmm0, xmmword ptr [rbp - 0x60]
00B6F387  0F 29 4D E0                     movaps xmmword ptr [rbp - 0x20], xmm1
00B6F38B  0F 28 4D 90                     movaps xmm1, xmmword ptr [rbp - 0x70]
00B6F38F  0F 29 45 10                     movaps xmmword ptr [rbp + 0x10], xmm0
00B6F393  0F 29 4D 00                     movaps xmmword ptr [rbp], xmm1
00B6F397  E8 50 B4 A1 FF                  call 0x14058a7ec
00B6F39C  EB 4A                           jmp 0x140b6f3e8
00B6F39E  0F 29 45 20                     movaps xmmword ptr [rbp + 0x20], xmm0
00B6F3A2  49 8D 85 98 04 00 00            lea rax, [r13 + 0x498]
00B6F3A9  0F 28 45 80                     movaps xmm0, xmmword ptr [rbp - 0x80]
00B6F3AD  4D 8D 8D 90 04 00 00            lea r9, [r13 + 0x490]
00B6F3B4  0F 29 45 40                     movaps xmmword ptr [rbp + 0x40], xmm0
00B6F3B8  4D 8D 85 88 04 00 00            lea r8, [r13 + 0x488]
00B6F3BF  0F 28 45 A0                     movaps xmm0, xmmword ptr [rbp - 0x60]
00B6F3C3  49 8D 95 80 04 00 00            lea rdx, [r13 + 0x480]
00B6F3CA  0F 29 4D 30                     movaps xmmword ptr [rbp + 0x30], xmm1
00B6F3CE  48 8D 4D 20                     lea rcx, [rbp + 0x20]
00B6F3D2  0F 28 4D 90                     movaps xmm1, xmmword ptr [rbp - 0x70]
00B6F3D6  0F 29 45 60                     movaps xmmword ptr [rbp + 0x60], xmm0
00B6F3DA  0F 29 4D 50                     movaps xmmword ptr [rbp + 0x50], xmm1
00B6F3DE  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00B6F3E3  E8 DC B2 A1 FF                  call 0x14058a6c4
00B6F3E8  8B D8                           mov ebx, eax
00B6F3EA  85 C0                           test eax, eax
00B6F3EC  79 33                           jns 0x140b6f421
00B6F3EE  49 8B 8F B8 00 00 00            mov rcx, qword ptr [r15 + 0xb8]
00B6F3F5  45 33 C0                        xor r8d, r8d
00B6F3F8  BA 78 01 00 00                  mov edx, 0x178
00B6F3FD  E8 32 F2 A5 FF                  call 0x1405ce634
00B6F402  4D 8B 8F B8 00 00 00            mov r9, qword ptr [r15 + 0xb8]
00B6F409  BA 0C 00 00 00                  mov edx, 0xc
00B6F40E  4C 63 C3                        movsxd r8, ebx
00B6F411  B9 A0 00 00 00                  mov ecx, 0xa0
00B6F416  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
00B6F41B  E8 40 E2 98 FF                  call 0x1404fd660
00B6F420  CC                              int3
00B6F421  41 89 77 10                     mov dword ptr [r15 + 0x10], esi
00B6F425  F0 45 01 77 14                  lock add dword ptr [r15 + 0x14], r14d
00B6F42A  EB 02                           jmp 0x140b6f42e
00B6F42C  F3 90                           pause
00B6F42E  41 8B 4F 14                     mov ecx, dword ptr [r15 + 0x14]
00B6F432  8B 05 48 76 45 00               mov eax, dword ptr [rip + 0x457648]
00B6F438  3B C8                           cmp ecx, eax
00B6F43A  75 F0                           jne 0x140b6f42c
00B6F43C  8B 05 3E 76 45 00               mov eax, dword ptr [rip + 0x45763e]
00B6F442  41 89 47 10                     mov dword ptr [r15 + 0x10], eax
00B6F446  41 89 77 14                     mov dword ptr [r15 + 0x14], esi
00B6F44A  49 8B CF                        mov rcx, r15
00B6F44D  41 38 B7 E8 01 00 00            cmp byte ptr [r15 + 0x1e8], sil
00B6F454  74 07                           je 0x140b6f45d
00B6F456  E8 E9 AF A1 FF                  call 0x14058a444
00B6F45B  EB 05                           jmp 0x140b6f462
00B6F45D  E8 7A AF A1 FF                  call 0x14058a3dc
00B6F462  41 38 B7 ED 01 00 00            cmp byte ptr [r15 + 0x1ed], sil
00B6F469  74 29                           je 0x140b6f494
00B6F46B  48 8D 05 0E E8 FF FF            lea rax, [rip - 0x17f2]
00B6F472  4C 89 6C 24 48                  mov qword ptr [rsp + 0x48], r13
00B6F477  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00B6F47C  48 8D 54 24 48                  lea rdx, [rsp + 0x48]
00B6F481  48 8D 05 28 E8 FF FF            lea rax, [rip - 0x17d8]
00B6F488  33 C9                           xor ecx, ecx
00B6F48A  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
00B6F48F  E8 3C CD FF FF                  call 0x140b6c1d0
00B6F494  45 01 75 00                     add dword ptr [r13], r14d
00B6F498  44 8B C6                        mov r8d, esi
00B6F49B  41 F7 47 40 E0 FF FF FF         test dword ptr [r15 + 0x40], 0xffffffe0
00B6F4A3  49 8B 4F 48                     mov rcx, qword ptr [r15 + 0x48]
00B6F4A7  49 8B 57 38                     mov rdx, qword ptr [r15 + 0x38]
00B6F4AB  76 1B                           jbe 0x140b6f4c8
00B6F4AD  8B 02                           mov eax, dword ptr [rdx]
00B6F4AF  45 03 C6                        add r8d, r14d
00B6F4B2  09 01                           or dword ptr [rcx], eax
00B6F4B4  48 8D 52 04                     lea rdx, [rdx + 4]
00B6F4B8  41 8B 47 40                     mov eax, dword ptr [r15 + 0x40]
00B6F4BC  48 8D 49 04                     lea rcx, [rcx + 4]
00B6F4C0  C1 E8 05                        shr eax, 5
00B6F4C3  44 3B C0                        cmp r8d, eax
00B6F4C6  72 E5                           jb 0x140b6f4ad
00B6F4C8  40 38 35 92 CA 39 00            cmp byte ptr [rip + 0x39ca92], sil
00B6F4CF  49 8D 47 30                     lea rax, [r15 + 0x30]
00B6F4D3  75 13                           jne 0x140b6f4e8
00B6F4D5  49 8D 4F 40                     lea rcx, [r15 + 0x40]
00B6F4D9  45 33 C0                        xor r8d, r8d
00B6F4DC  48 8B D0                        mov rdx, rax
00B6F4DF  E8 2C 2D 87 FF                  call 0x1403e2210
00B6F4E4  49 8D 47 40                     lea rax, [r15 + 0x40]
00B6F4E8  48 8B C8                        mov rcx, rax
00B6F4EB  E8 A0 2F 7F FF                  call 0x140362490
00B6F4F0  41 C7 87 C8 00 00 00 08 00 00 00  mov dword ptr [r15 + 0xc8], 8
00B6F4FB  44 89 35 56 E9 39 00            mov dword ptr [rip + 0x39e956], r14d
00B6F502  49 8B 97 B8 00 00 00            mov rdx, qword ptr [r15 + 0xb8]
00B6F509  E8 9E 33 A2 FF                  call 0x1405928ac
00B6F50E  40 38 35 4C CA 39 00            cmp byte ptr [rip + 0x39ca4c], sil
00B6F515  75 08                           jne 0x140b6f51f
00B6F517  41 8B CE                        mov ecx, r14d
00B6F51A  E8 41 36 A2 FF                  call 0x140592b60
00B6F51F  0F 31                           rdtsc
00B6F521  49 8B 8F B8 00 00 00            mov rcx, qword ptr [r15 + 0xb8]
00B6F528  48 C1 E2 20                     shl rdx, 0x20
00B6F52C  48 0B C2                        or rax, rdx
00B6F52F  48 8B F8                        mov rdi, rax
00B6F532  E8 19 35 A2 FF                  call 0x140592a50
00B6F537  48 63 D8                        movsxd rbx, eax
00B6F53A  E8 C9 54 A6 FF                  call 0x1405d4a08
00B6F53F  85 C0                           test eax, eax
00B6F541  74 37                           je 0x140b6f57a
00B6F543  48 8D 54 24 34                  lea rdx, [rsp + 0x34]
00B6F548  33 C9                           xor ecx, ecx
00B6F54A  E8 BD 34 A2 FF                  call 0x140592a0c
00B6F54F  8B 4C 24 34                     mov ecx, dword ptr [rsp + 0x34]
00B6F553  B8 00 00 10 00                  mov eax, 0x100000
00B6F558  3B C8                           cmp ecx, eax
00B6F55A  72 06                           jb 0x140b6f562
00B6F55C  8B C8                           mov ecx, eax
00B6F55E  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
00B6F562  41 8B 87 B8 01 00 00            mov eax, dword ptr [r15 + 0x1b8]
00B6F569  C1 E9 0C                        shr ecx, 0xc
00B6F56C  3B C8                           cmp ecx, eax
00B6F56E  74 0A                           je 0x140b6f57a
00B6F570  0F 46 C1                        cmovbe eax, ecx
00B6F573  41 89 87 B8 01 00 00            mov dword ptr [r15 + 0x1b8], eax
00B6F57A  0F 31                           rdtsc
00B6F57C  48 C1 E2 20                     shl rdx, 0x20
00B6F580  48 0B C2                        or rax, rdx
00B6F583  48 2B C7                        sub rax, rdi
00B6F586  48 01 05 FB CD 39 00            add qword ptr [rip + 0x39cdfb], rax
00B6F58D  85 DB                           test ebx, ebx
00B6F58F  0F 88 31 05 00 00               js 0x140b6fac6
00B6F595  44 39 35 44 CD 39 00            cmp dword ptr [rip + 0x39cd44], r14d
00B6F59C  0F 84 24 05 00 00               je 0x140b6fac6
00B6F5A2  49 8B CF                        mov rcx, r15
00B6F5A5  E8 3A EB FF FF                  call 0x140b6e0e4
00B6F5AA  4D 8D 77 50                     lea r14, [r15 + 0x50]
00B6F5AE  49 8B 1E                        mov rbx, qword ptr [r14]
00B6F5B1  49 3B DE                        cmp rbx, r14
00B6F5B4  74 65                           je 0x140b6f61b
00B6F5B6  48 8D 03                        lea rax, [rbx]
00B6F5B9  48 8B 1B                        mov rbx, qword ptr [rbx]
00B6F5BC  48 8B 70 20                     mov rsi, qword ptr [rax + 0x20]
00B6F5C0  48 8B 78 18                     mov rdi, qword ptr [rax + 0x18]
00B6F5C4  4C 8B 60 28                     mov r12, qword ptr [rax + 0x28]
00B6F5C8  48 8B C6                        mov rax, rsi
00B6F5CB  48 2B C7                        sub rax, rdi
00B6F5CE  49 01 47 68                     add qword ptr [r15 + 0x68], rax
00B6F5D2  48 3B FE                        cmp rdi, rsi
00B6F5D5  73 3D                           jae 0x140b6f614
00B6F5D7  4C 8B 74 24 38                  mov r14, qword ptr [rsp + 0x38]
00B6F5DC  4C 8B CE                        mov r9, rsi
00B6F5DF  4C 8B C7                        mov r8, rdi
00B6F5E2  49 8B D6                        mov rdx, r14
00B6F5E5  49 8B CF                        mov rcx, r15
00B6F5E8  E8 6F D9 FF FF                  call 0x140b6cf5c
00B6F5ED  45 8B 46 28                     mov r8d, dword ptr [r14 + 0x28]
00B6F5F1  49 8B CC                        mov rcx, r12
00B6F5F4  49 8B 56 18                     mov rdx, qword ptr [r14 + 0x18]
00B6F5F8  E8 43 72 B5 FF                  call 0x1406c6840
00B6F5FD  41 8B 46 28                     mov eax, dword ptr [r14 + 0x28]
00B6F601  4C 03 E0                        add r12, rax
00B6F604  48 C1 E8 0C                     shr rax, 0xc
00B6F608  48 03 F8                        add rdi, rax
00B6F60B  48 3B FE                        cmp rdi, rsi
00B6F60E  72 CC                           jb 0x140b6f5dc
00B6F610  4D 8D 77 50                     lea r14, [r15 + 0x50]
00B6F614  49 3B DE                        cmp rbx, r14
00B6F617  75 9D                           jne 0x140b6f5b6
00B6F619  33 F6                           xor esi, esi
00B6F61B  49 8B CF                        mov rcx, r15
00B6F61E  E8 59 59 A6 FF                  call 0x1405d4f7c
00B6F623  49 8B 8F B0 00 00 00            mov rcx, qword ptr [r15 + 0xb0]
00B6F62A  48 8B 05 07 C9 39 00            mov rax, qword ptr [rip + 0x39c907]
00B6F631  48 89 01                        mov qword ptr [rcx], rax
00B6F634  48 89 41 08                     mov qword ptr [rcx + 8], rax
00B6F638  48 89 71 10                     mov qword ptr [rcx + 0x10], rsi
00B6F63C  0F 31                           rdtsc
00B6F63E  48 C1 E2 20                     shl rdx, 0x20
00B6F642  49 8B CF                        mov rcx, r15
00B6F645  48 0B C2                        or rax, rdx
00B6F648  49 8B D5                        mov rdx, r13
00B6F64B  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00B6F650  E8 BF 05 00 00                  call 0x140b6fc14
00B6F655  8B D8                           mov ebx, eax
00B6F657  85 C0                           test eax, eax
00B6F659  0F 88 E5 03 00 00               js 0x140b6fa44
00B6F65F  45 8B 65 50                     mov r12d, dword ptr [r13 + 0x50]
00B6F663  41 38 B7 E8 01 00 00            cmp byte ptr [r15 + 0x1e8], sil
00B6F66A  74 59                           je 0x140b6f6c5
00B6F66C  41 8B 4F 20                     mov ecx, dword ptr [r15 + 0x20]
00B6F670  41 8B 87 18 01 00 00            mov eax, dword ptr [r15 + 0x118]
00B6F677  C1 E9 03                        shr ecx, 3
00B6F67A  83 C0 02                        add eax, 2
00B6F67D  81 C1 FF 0F 00 00               add ecx, 0xfff
00B6F683  41 C7 87 C8 00 00 00 03 00 00 00  mov dword ptr [r15 + 0xc8], 3
00B6F68E  C1 E9 0C                        shr ecx, 0xc
00B6F691  03 C1                           add eax, ecx
00B6F693  49 8B CF                        mov rcx, r15
00B6F696  49 89 45 60                     mov qword ptr [r13 + 0x60], rax
00B6F69A  48 8B 1D D7 CC 39 00            mov rbx, qword ptr [rip + 0x39ccd7]
00B6F6A1  E8 EE 58 A6 FF                  call 0x1405d4f94
00B6F6A6  48 8B 05 CB CC 39 00            mov rax, qword ptr [rip + 0x39cccb]
00B6F6AD  48 2B C3                        sub rax, rbx
00B6F6B0  48 89 05 A1 CF 39 00            mov qword ptr [rip + 0x39cfa1], rax
00B6F6B7  41 8B 87 1C 01 00 00            mov eax, dword ptr [r15 + 0x11c]
00B6F6BE  48 89 05 6B CE 39 00            mov qword ptr [rip + 0x39ce6b], rax
00B6F6C5  49 8D 4F 40                     lea rcx, [r15 + 0x40]
00B6F6C9  41 C7 87 C8 00 00 00 04 00 00 00  mov dword ptr [r15 + 0xc8], 4
00B6F6D4  49 89 4F 70                     mov qword ptr [r15 + 0x70], rcx
00B6F6D8  E8 63 48 8C FF                  call 0x140433f40
00B6F6DD  4D 8B 77 68                     mov r14, qword ptr [r15 + 0x68]
00B6F6E1  33 D2                           xor edx, edx
00B6F6E3  48 8B 3D DE C8 39 00            mov rdi, qword ptr [rip + 0x39c8de]
00B6F6EA  41 8B B7 38 01 00 00            mov esi, dword ptr [r15 + 0x138]
00B6F6F1  48 8B CF                        mov rcx, rdi
00B6F6F4  49 8B 9F 30 01 00 00            mov rbx, qword ptr [r15 + 0x130]
00B6F6FB  8B C0                           mov eax, eax
00B6F6FD  44 8D 42 40                     lea r8d, [rdx + 0x40]
00B6F701  4C 03 F0                        add r14, rax
00B6F704  49 C1 E6 0C                     shl r14, 0xc
00B6F708  E8 33 75 B5 FF                  call 0x1406c6c40
00B6F70D  C7 47 18 00 00 00 00            mov dword ptr [rdi + 0x18], 0
00B6F714  89 77 08                        mov dword ptr [rdi + 8], esi
00B6F717  33 F6                           xor esi, esi
00B6F719  48 89 1F                        mov qword ptr [rdi], rbx
00B6F71C  4C 89 77 10                     mov qword ptr [rdi + 0x10], r14
00B6F720  48 89 35 11 CE 39 00            mov qword ptr [rip + 0x39ce11], rsi
00B6F727  48 89 35 12 CE 39 00            mov qword ptr [rip + 0x39ce12], rsi
00B6F72E  41 89 B7 68 01 00 00            mov dword ptr [r15 + 0x168], esi
00B6F735  49 89 B7 78 01 00 00            mov qword ptr [r15 + 0x178], rsi
00B6F73C  48 8B 3D 35 CC 39 00            mov rdi, qword ptr [rip + 0x39cc35]
00B6F743  40 38 74 24 30                  cmp byte ptr [rsp + 0x30], sil
00B6F748  74 18                           je 0x140b6f762
00B6F74A  49 8B 87 B8 00 00 00            mov rax, qword ptr [r15 + 0xb8]
00B6F751  48 39 B0 80 00 00 00            cmp qword ptr [rax + 0x80], rsi
00B6F758  74 08                           je 0x140b6f762
00B6F75A  41 C6 87 A8 01 00 00 01         mov byte ptr [r15 + 0x1a8], 1
00B6F762  41 8B 87 18 01 00 00            mov eax, dword ptr [r15 + 0x118]
00B6F769  41 8B 4F 20                     mov ecx, dword ptr [r15 + 0x20]
00B6F76D  83 C0 02                        add eax, 2
00B6F770  C1 E9 03                        shr ecx, 3
00B6F773  81 C1 FF 0F 00 00               add ecx, 0xfff
00B6F779  C1 E9 0C                        shr ecx, 0xc
00B6F77C  41 03 8F 1C 01 00 00            add ecx, dword ptr [r15 + 0x11c]
00B6F783  03 C1                           add eax, ecx
00B6F785  49 89 45 68                     mov qword ptr [r13 + 0x68], rax
00B6F789  48 C1 E0 0C                     shl rax, 0xc
00B6F78D  49 89 87 98 01 00 00            mov qword ptr [r15 + 0x198], rax
00B6F794  0F 31                           rdtsc
00B6F796  48 C1 E2 20                     shl rdx, 0x20
00B6F79A  49 8B CF                        mov rcx, r15
00B6F79D  48 0B C2                        or rax, rdx
00B6F7A0  41 C6 47 03 01                  mov byte ptr [r15 + 3], 1
00B6F7A5  B2 01                           mov dl, 1
00B6F7A7  48 8B D8                        mov rbx, rax
00B6F7AA  E8 81 06 00 00                  call 0x140b6fe30
00B6F7AF  F0 41 FF 47 08                  lock inc dword ptr [r15 + 8]
00B6F7B4  41 8B 4F 08                     mov ecx, dword ptr [r15 + 8]
00B6F7B8  41 3B 8F 20 01 00 00            cmp ecx, dword ptr [r15 + 0x120]
00B6F7BF  74 0F                           je 0x140b6f7d0
00B6F7C1  F3 90                           pause
00B6F7C3  41 8B 47 08                     mov eax, dword ptr [r15 + 8]
00B6F7C7  41 3B 87 20 01 00 00            cmp eax, dword ptr [r15 + 0x120]
00B6F7CE  75 F1                           jne 0x140b6f7c1
00B6F7D0  0F 31                           rdtsc
00B6F7D2  48 C1 E2 20                     shl rdx, 0x20
00B6F7D6  44 8B C6                        mov r8d, esi
00B6F7D9  48 0B C2                        or rax, rdx
00B6F7DC  48 2B C3                        sub rax, rbx
00B6F7DF  48 89 05 7A CE 39 00            mov qword ptr [rip + 0x39ce7a], rax
00B6F7E6  41 39 B7 20 01 00 00            cmp dword ptr [r15 + 0x120], esi
00B6F7ED  0F 86 BC 00 00 00               jbe 0x140b6f8af
00B6F7F3  48 8D 1D FE CD 39 00            lea rbx, [rip + 0x39cdfe]
00B6F7FA  41 8B C0                        mov eax, r8d
00B6F7FD  4C 8B CB                        mov r9, rbx
00B6F800  4C 69 D0 A8 00 00 00            imul r10, rax, 0xa8
00B6F807  41 BB 05 00 00 00               mov r11d, 5
00B6F80D  4C 2B D3                        sub r10, rbx
00B6F810  49 8B 87 28 01 00 00            mov rax, qword ptr [r15 + 0x128]
00B6F817  4B 8D 14 0A                     lea rdx, [r10 + r9]
00B6F81B  48 8B 4C 02 58                  mov rcx, qword ptr [rdx + rax + 0x58]
00B6F820  49 01 09                        add qword ptr [r9], rcx
00B6F823  4D 8D 49 08                     lea r9, [r9 + 8]
00B6F827  49 8B 87 28 01 00 00            mov rax, qword ptr [r15 + 0x128]
00B6F82E  48 89 74 02 58                  mov qword ptr [rdx + rax + 0x58], rsi
00B6F833  49 83 EB 01                     sub r11, 1
00B6F837  75 D7                           jne 0x140b6f810
00B6F839  41 8B C0                        mov eax, r8d
00B6F83C  48 69 C8 A8 00 00 00            imul rcx, rax, 0xa8
00B6F843  49 8B 87 28 01 00 00            mov rax, qword ptr [r15 + 0x128]
00B6F84A  48 8B 4C 01 28                  mov rcx, qword ptr [rcx + rax + 0x28]
00B6F84F  48 01 0D 42 CB 39 00            add qword ptr [rip + 0x39cb42], rcx
00B6F856  41 8B C0                        mov eax, r8d
00B6F859  48 69 C8 A8 00 00 00            imul rcx, rax, 0xa8
00B6F860  49 8B 87 28 01 00 00            mov rax, qword ptr [r15 + 0x128]
00B6F867  48 89 74 01 28                  mov qword ptr [rcx + rax + 0x28], rsi
00B6F86C  41 8B C0                        mov eax, r8d
00B6F86F  48 69 C8 A8 00 00 00            imul rcx, rax, 0xa8
00B6F876  49 8B 87 28 01 00 00            mov rax, qword ptr [r15 + 0x128]
00B6F87D  48 8B 4C 01 38                  mov rcx, qword ptr [rcx + rax + 0x38]
00B6F882  48 01 0D AF CC 39 00            add qword ptr [rip + 0x39ccaf], rcx
00B6F889  41 8B C0                        mov eax, r8d
00B6F88C  41 FF C0                        inc r8d
00B6F88F  48 69 C8 A8 00 00 00            imul rcx, rax, 0xa8
00B6F896  49 8B 87 28 01 00 00            mov rax, qword ptr [r15 + 0x128]
00B6F89D  48 89 74 01 38                  mov qword ptr [rcx + rax + 0x38], rsi
00B6F8A2  45 3B 87 20 01 00 00            cmp r8d, dword ptr [r15 + 0x120]
00B6F8A9  0F 82 4B FF FF FF               jb 0x140b6f7fa
00B6F8AF  48 8B 05 C2 CA 39 00            mov rax, qword ptr [rip + 0x39cac2]
00B6F8B6  49 8D 4F 30                     lea rcx, [r15 + 0x30]
00B6F8BA  48 2B C7                        sub rax, rdi
00B6F8BD  48 89 05 84 CD 39 00            mov qword ptr [rip + 0x39cd84], rax
00B6F8C4  48 8B 05 9D CC 39 00            mov rax, qword ptr [rip + 0x39cc9d]
00B6F8CB  48 89 05 76 CC 39 00            mov qword ptr [rip + 0x39cc76], rax
00B6F8D2  8B 05 98 CC 39 00               mov eax, dword ptr [rip + 0x39cc98]
00B6F8D8  48 89 05 79 CC 39 00            mov qword ptr [rip + 0x39cc79], rax
00B6F8DF  48 89 35 82 CC 39 00            mov qword ptr [rip + 0x39cc82], rsi
00B6F8E6  89 35 84 CC 39 00               mov dword ptr [rip + 0x39cc84], esi
00B6F8EC  41 C7 87 C8 00 00 00 05 00 00 00  mov dword ptr [r15 + 0xc8], 5
00B6F8F7  49 89 4F 70                     mov qword ptr [r15 + 0x70], rcx
00B6F8FB  49 89 B7 80 00 00 00            mov qword ptr [r15 + 0x80], rsi
00B6F902  E8 39 46 8C FF                  call 0x140433f40
00B6F907  48 8B 3D BA C6 39 00            mov rdi, qword ptr [rip + 0x39c6ba]
00B6F90E  33 D2                           xor edx, edx
00B6F910  41 8B B7 38 01 00 00            mov esi, dword ptr [r15 + 0x138]
00B6F917  48 8B CF                        mov rcx, rdi
00B6F91A  49 8B 9F 30 01 00 00            mov rbx, qword ptr [r15 + 0x130]
00B6F921  44 8B F0                        mov r14d, eax
00B6F924  44 8D 42 40                     lea r8d, [rdx + 0x40]
00B6F928  49 C1 E6 0C                     shl r14, 0xc
00B6F92C  E8 0F 73 B5 FF                  call 0x1406c6c40
00B6F931  C7 47 18 00 00 00 00            mov dword ptr [rdi + 0x18], 0
00B6F938  48 89 1F                        mov qword ptr [rdi], rbx
00B6F93B  89 77 08                        mov dword ptr [rdi + 8], esi
00B6F93E  4C 89 77 10                     mov qword ptr [rdi + 0x10], r14
00B6F942  49 8B 87 98 01 00 00            mov rax, qword ptr [r15 + 0x198]
00B6F949  48 05 FF 0F 00 00               add rax, 0xfff
00B6F94F  48 C1 E8 0C                     shr rax, 0xc
00B6F953  49 89 45 70                     mov qword ptr [r13 + 0x70], rax
00B6F957  48 8B 3D 1A CA 39 00            mov rdi, qword ptr [rip + 0x39ca1a]
00B6F95E  0F 31                           rdtsc
00B6F960  48 C1 E2 20                     shl rdx, 0x20
00B6F964  33 F6                           xor esi, esi
00B6F966  48 0B C2                        or rax, rdx
00B6F969  41 89 77 08                     mov dword ptr [r15 + 8], esi
00B6F96D  33 D2                           xor edx, edx
00B6F96F  49 89 B7 78 01 00 00            mov qword ptr [r15 + 0x178], rsi
00B6F976  49 8B CF                        mov rcx, r15
00B6F979  48 8B D8                        mov rbx, rax
00B6F97C  E8 AF 04 00 00                  call 0x140b6fe30
00B6F981  0F 31                           rdtsc
00B6F983  48 C1 E2 20                     shl rdx, 0x20
00B6F987  49 8B CF                        mov rcx, r15
00B6F98A  48 0B C2                        or rax, rdx
00B6F98D  49 8B D5                        mov rdx, r13
00B6F990  48 2B C3                        sub rax, rbx
00B6F993  48 89 05 CE CC 39 00            mov qword ptr [rip + 0x39ccce], rax
00B6F99A  48 8B 05 D7 C9 39 00            mov rax, qword ptr [rip + 0x39c9d7]
00B6F9A1  48 2B C7                        sub rax, rdi
00B6F9A4  48 89 05 A5 CC 39 00            mov qword ptr [rip + 0x39cca5], rax
00B6F9AB  E8 FC E5 FF FF                  call 0x140b6dfac
00B6F9B0  49 8B CF                        mov rcx, r15
00B6F9B3  41 C7 87 C8 00 00 00 07 00 00 00  mov dword ptr [r15 + 0xc8], 7
00B6F9BE  E8 B9 01 00 00                  call 0x140b6fb7c
00B6F9C3  4C 8B 4C 24 38                  mov r9, qword ptr [rsp + 0x38]
00B6F9C8  45 8B C4                        mov r8d, r12d
00B6F9CB  49 8B D5                        mov rdx, r13
00B6F9CE  41 C7 87 C8 00 00 00 06 00 00 00  mov dword ptr [r15 + 0xc8], 6
00B6F9D9  49 8B CF                        mov rcx, r15
00B6F9DC  E8 AF 08 00 00                  call 0x140b70290
00B6F9E1  41 8B 9F CC 00 00 00            mov ebx, dword ptr [r15 + 0xcc]
00B6F9E8  85 DB                           test ebx, ebx
00B6F9EA  78 58                           js 0x140b6fa44
00B6F9EC  8B 05 82 C3 39 00               mov eax, dword ptr [rip + 0x39c382]
00B6F9F2  39 05 74 C3 39 00               cmp dword ptr [rip + 0x39c374], eax
00B6F9F8  75 21                           jne 0x140b6fa1b
00B6F9FA  F7 05 08 D5 39 00 00 80 00 00   test dword ptr [rip + 0x39d508], 0x8000
00B6FA04  75 0E                           jne 0x140b6fa14
00B6FA06  45 33 C0                        xor r8d, r8d
00B6FA09  48 8D 56 FE                     lea rdx, [rsi - 2]
00B6FA0D  33 C9                           xor ecx, ecx
00B6FA0F  E8 7C 6C 95 FF                  call 0x1404c6690
00B6FA14  B1 01                           mov cl, 1
00B6FA16  E8 AD F1 A1 FF                  call 0x14058ebc8
00B6FA1B  F7 05 E7 D4 39 00 00 10 00 00   test dword ptr [rip + 0x39d4e7], 0x1000
00B6FA25  74 0A                           je 0x140b6fa31
00B6FA27  B9 03 00 00 00                  mov ecx, 3
00B6FA2C  E8 1F 6B 9D FF                  call 0x140546550
00B6FA31  8B 05 A9 C8 39 00               mov eax, dword ptr [rip + 0x39c8a9]
00B6FA37  8B DE                           mov ebx, esi
00B6FA39  A8 10                           test al, 0x10
00B6FA3B  74 07                           je 0x140b6fa44
00B6FA3D  BB 94 02 00 40                  mov ebx, 0x40000294
00B6FA42  EB 39                           jmp 0x140b6fa7d
00B6FA44  B9 04 00 00 00                  mov ecx, 4
00B6FA49  E8 72 A0 98 FF                  call 0x1404f9ac0
00B6FA4E  85 DB                           test ebx, ebx
00B6FA50  78 2B                           js 0x140b6fa7d
00B6FA52  81 FB 94 02 00 40               cmp ebx, 0x40000294
00B6FA58  74 23                           je 0x140b6fa7d
00B6FA5A  83 3D 0B C3 39 00 05            cmp dword ptr [rip + 0x39c30b], 5
00B6FA61  75 1A                           jne 0x140b6fa7d
00B6FA63  E8 A4 1C 00 00                  call 0x140b7170c
00B6FA68  40 38 35 28 70 45 00            cmp byte ptr [rip + 0x457028], sil
00B6FA6F  74 07                           je 0x140b6fa78
00B6FA71  33 C9                           xor ecx, ecx
00B6FA73  E8 E8 3C A1 FF                  call 0x140583760
00B6FA78  E8 97 C3 FF FF                  call 0x140b6be14
00B6FA7D  B9 18 00 00 00                  mov ecx, 0x18
00B6FA82  E8 09 82 00 00                  call 0x140b77c90
00B6FA87  48 8B 05 9A 10 29 00            mov rax, qword ptr [rip + 0x29109a]
00B6FA8E  E8 3D B0 B4 FF                  call 0x1406baad0
00B6FA93  8B C3                           mov eax, ebx
00B6FA95  48 8B 8D B0 01 00 00            mov rcx, qword ptr [rbp + 0x1b0]
00B6FA9C  48 33 CC                        xor rcx, rsp
00B6FA9F  E8 9C CB B3 FF                  call 0x1406ac640
00B6FAA4  4C 8D 9C 24 C0 02 00 00         lea r11, [rsp + 0x2c0]
00B6FAAC  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
00B6FAB0  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
00B6FAB4  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
00B6FAB8  49 8B E3                        mov rsp, r11
00B6FABB  41 5F                           pop r15
00B6FABD  41 5E                           pop r14
00B6FABF  41 5D                           pop r13
00B6FAC1  41 5C                           pop r12
00B6FAC3  5D                              pop rbp
00B6FAC4  C3                              ret
00B6FAC5  CC                              int3
00B6FAC6  B9 14 00 00 00                  mov ecx, 0x14
00B6FACB  E8 C0 81 00 00                  call 0x140b77c90
00B6FAD0  49 8B 8F B8 00 00 00            mov rcx, qword ptr [r15 + 0xb8]
00B6FAD7  45 33 C0                        xor r8d, r8d
00B6FADA  BA 78 01 00 00                  mov edx, 0x178
00B6FADF  E8 50 EB A5 FF                  call 0x1405ce634
00B6FAE4  4D 8B 8F B8 00 00 00            mov r9, qword ptr [r15 + 0xb8]
00B6FAEB  4C 8B C3                        mov r8, rbx
00B6FAEE  BA 0C 00 00 00                  mov edx, 0xc
00B6FAF3  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
00B6FAF8  B9 A0 00 00 00                  mov ecx, 0xa0
00B6FAFD  E8 5E DB 98 FF                  call 0x1404fd660
00B6FB02  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopSaveHiberContext(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m270;
    unsigned __int64 v_stack_m278;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m280;
    unsigned __int64 v_stack_m288;
    unsigned __int64 v_stack_m290;
    unsigned __int64 v_stack_m298;
    unsigned __int64 v_stack_m2A0;
    unsigned int v_stack_m2A8;
    unsigned __int64 v_stack_m2B0;
    unsigned int v_stack_m2B4;
    unsigned __int8 v_stack_m2B8;
    unsigned __int64 v_stack_m2C8;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (704);
    result = (*(unsigned __int64 *)(v_rip + 2733763)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 488 + 432) = result;
    result = 0;
    *(unsigned __int64 *)(v_rsp - 488 - 64) = 0;
    v_stack_m290 = 0;
    a2 = 0;
    *(unsigned __int64 *)(v_rsp - 488 - 80) = v_xmm0;
    v_stack_m2A0 = v_xmm1;
    result = memset(v_rsp - 488 + 112, a2, 312, a4);
    v_rsi = 0;
    v_stack_m2A8 = 0;
    v_stack_m2B4 = 0;
    result = Feature_CrashDumpOneMBTransferSize__private_IsEnabledDeviceUsageNoInline(v_rsp - 488 + 112, a2, 312, a4);
    if ((unsigned int)(result) != 0) goto loc_00B6F0D3;
    v_stack_m2B0 = v_rsp - 488 + 112;
    goto loc_00B6F0DF;
loc_00B6F0D3:
    v_stack_m2B0 = *(unsigned __int64 *)(a1 + 352);
loc_00B6F0DF:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36))) != 0) goto loc_00B6F0FF;
    result = PopCheckpointSystemSleep((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36)) + 19, a2, 312, a4);
    goto loc_00B6F150;
loc_00B6F0FF:
    result = 0;
    if (((*(unsigned __int8 *)(v_rip + 4553098)) & (2)) != 0) { result = 1; }
    if ((*(unsigned __int8 *)(v_rip + 4553071)) != 0) goto loc_00B6F11B;
    if ((unsigned __int8)(result) == 0) goto loc_00B6F150;
loc_00B6F11B:
    goto loc_00B6F124;
loc_00B6F122:
loc_00B6F124:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 16))) != 0) goto loc_00B6F122;
    if ((*(unsigned __int8 *)(v_rip + 3790157)) == 0) goto loc_00B6F13F;
    goto loc_00B6FA93;
loc_00B6F13F:
    goto loc_00B6F148;
loc_00B6F146:
loc_00B6F148:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 20))) != 0) goto loc_00B6F146;
loc_00B6F150:
    if (((unsigned int)((unsigned int)(0x40000294ULL))) < (*(unsigned int *)(a1 + 288))) goto loc_00B6F160;
    goto loc_00B6FA93;
loc_00B6F160:
    if (0 != 0) goto loc_00B6F180;
    *(unsigned int *)(v_rip + 3796026) = 0;
    result = KeDisableInterrupts((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36)) + 19, a2, 312, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00B6F1D1;
    result = PopInternalError((unsigned int)(0xA1E60ULL), a2, 312, a4);
loc_00B6F17E:
loc_00B6F180:
    if ((unsigned __int8)(*(unsigned __int8 *)(a1 + 3)) == 0) goto loc_00B6F17E;
    v_rbx = (0) * (0);
    a2 = (*(unsigned __int64 *)(a1 + 296)) + (v_rbx);
    result = PopCompressHiberBlocks(a1, a2, 1, a4);
    goto loc_00B6F1AD;
loc_00B6F1AB:
loc_00B6F1AD:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 8))) != 0) goto loc_00B6F1AB;
    a3 = 0;
    a2 = (*(unsigned __int64 *)(a1 + 296)) + (v_rbx);
    result = PopCompressHiberBlocks(a1, a2, a3, a4);
    goto loc_00B6FA93;
loc_00B6F1D1:
    if (!sign_flag) goto loc_00B6F1E2;
    v_stack_m2B8 = 0;
    goto loc_00B6F1F4;
loc_00B6F1E2:
    result = IoDumpStackResumeCapable(v_stack_m2A8, a2, a3, a4);
    v_stack_m2B8 = (unsigned __int8)(result);
    if ((unsigned __int8)(result) == 0) {
        *(unsigned __int8 *)(v_rip + 3788127) = 1;
    }
    result = PSHED_dll_PshedArePluginsPresent(v_stack_m2A8, a2, a3, a4);
    if ((unsigned int)(result) != 0) {
        *(unsigned __int8 *)(v_rip + 3788097) = 1;
    }
    result = guard_dispatch_icall(v_stack_m2A8, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) {
        *(unsigned __int8 *)(v_rip + 3788067) = 1;
    }
    if ((*(unsigned __int8 *)(v_rip + 3788060)) == 0) goto loc_00B6F26C;
    result = PopIsMktmeEnabled(v_stack_m2A8, a2, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        a2 = 274;
        v_stack_m2C8 = 0;
        a4 = a1;
        a3 = 10;
        a1 = a2 - 114;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    *(unsigned __int64 *)(a1 + 176) = v_rsp - 488 - 80;
    *(unsigned __int64 *)(a1 + 192) = v_rip + 2851972;
    *(unsigned __int8 *)(a1 + 1) = 1;
    if ((*(unsigned __int8 *)(v_rip + 4552740)) == 0) goto loc_00B6F462;
    a1 = 0;
    *(unsigned int *)(v_rip + 3795894) = 1;
    result = HvlDisableEnlightenment(a1, a2, a3, a4);
    result = guard_dispatch_icall(a1, a2, a3, a4);
    result = 0;
    if (((*(unsigned __int8 *)(v_rip + 4552658)) & (2)) != 0) { result = 1; }
    if ((*(unsigned __int8 *)(v_rip + 4552631)) != 0) goto loc_00B6F2D7;
    if ((unsigned __int8)(result) == 0) goto loc_00B6F44A;
loc_00B6F2D7:
    goto loc_00B6F2E0;
loc_00B6F2DE:
loc_00B6F2E0:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 16)))) != ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4552598))))) goto loc_00B6F2DE;
    v_stack_m288 = *(unsigned __int64 *)(v_rip + 2852355);
    v_stack_m280 = *(unsigned __int64 *)(v_rip + 2852247);
    v_stack_m278 = *(unsigned __int64 *)(v_rip + 2852243);
    v_stack_m270 = *(unsigned __int64 *)(v_rip + 2852210);
    *(unsigned __int64 *)(v_rsp - 488 - 128) = *(unsigned __int64 *)(v_rip + 2852230);
    *(unsigned __int64 *)(v_rsp - 488 - 120) = *(unsigned __int64 *)(v_rip + 2852206);
    *(unsigned __int64 *)(v_rsp - 488 - 112) = *(unsigned __int64 *)(v_rip + 2852243);
    *(unsigned __int64 *)(v_rsp - 488 - 104) = *(unsigned __int64 *)(v_rip + 2852240);
    *(unsigned __int64 *)(v_rsp - 488 - 96) = *(unsigned __int64 *)(v_rip + 2852237);
    *(unsigned __int64 *)(v_rsp - 488 - 88) = *(unsigned __int64 *)(v_rip + 2852234);
    if ((*(unsigned __int8 *)(a1 + 488)) == 0) goto loc_00B6F39E;
    *(unsigned __int64 *)(v_rsp - 488 - 48) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 488 - 16) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 488 - 32) = v_xmm1;
    *(unsigned __int64 *)(v_rsp - 488 + 16) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 488) = v_xmm1;
    result = HvlPrepareForSecureHibernate(v_rsp - 488 - 48, a2, a3, a4);
    goto loc_00B6F3E8;
loc_00B6F39E:
    *(unsigned __int64 *)(v_rsp - 488 + 32) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 488 + 64) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 488 + 48) = v_xmm1;
    *(unsigned __int64 *)(v_rsp - 488 + 96) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 488 + 80) = v_xmm1;
    v_stack_m2C8 = *(unsigned __int64 *)(a1 + 216) + 1176;
    result = HvlPrepareForHibernate(v_rsp - 488 + 32, *(unsigned __int64 *)(a1 + 216) + 1152, *(unsigned __int64 *)(a1 + 216) + 1160, *(unsigned __int64 *)(a1 + 216) + 1168);
loc_00B6F3E8:
    if (sign_flag) {
        a1 = *(unsigned __int64 *)(a1 + 184);
        a3 = 0;
        a2 = 376;
        result = PopInternalAddToDumpFile(a1, a2, a3, *(unsigned __int64 *)(a1 + 216) + 1168);
        a4 = *(unsigned __int64 *)(a1 + 184);
        a2 = 12;
        a3 = (int)((unsigned int)((unsigned int)((unsigned int)(result))));
        a1 = 160;
        v_stack_m2C8 = 0;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    *(unsigned int *)(a1 + 16) = 0;
    goto loc_00B6F42E;
loc_00B6F42C:
loc_00B6F42E:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 20)))) != ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4552264))))) goto loc_00B6F42C;
    *(unsigned int *)(a1 + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4552254)));
    *(unsigned int *)(a1 + 20) = 0;
loc_00B6F44A:
    if ((*(unsigned __int8 *)(a1 + 488)) == 0) goto loc_00B6F45D;
    result = HvlDiscardSecurePagesFromHibernation(a1, a2, a3, a4);
    goto loc_00B6F462;
loc_00B6F45D:
    result = HvlDiscardPagesFromHibernation(a1, a2, a3, a4);
loc_00B6F462:
    if ((*(unsigned __int8 *)(a1 + 493)) != 0) {
        result = v_rip - 6130;
        v_stack_m2A0 = *(unsigned __int64 *)(a1 + 216);
        v_stack_m298 = result;
        a2 = v_stack_m2A0;
        result = v_rip - 6104;
        a1 = 0;
        v_stack_m290 = result;
        result = PopSstInvokeNotificationHandlers(a1, a2, a3, a4);
    }
    if (condition_is_below_or_equal) goto loc_00B6F4C8;
loc_00B6F4AD:
    a3 = (unsigned int)((0) + (1));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 64))) >> (5));
    if (((unsigned int)(a3)) < ((unsigned int)(result))) goto loc_00B6F4AD;
loc_00B6F4C8:
    result = a1 + 48;
    if ((*(unsigned __int8 *)(v_rip + 3787410)) == 0) {
        a1 = a1 + 64;
        a3 = 0;
        a2 = a1 + 48;
        result = RtlCopyBitMap(a1, a2, a3, a4);
        result = a1 + 64;
    }
    result = RtlSetAllBits(result, a2, a3, a4);
    *(unsigned int *)(a1 + 200) = 8;
    *(unsigned int *)(v_rip + 3795286) = 1;
    result = IoGetDumpHiberRanges(result, *(unsigned __int64 *)(a1 + 184), a3, a4);
    if ((*(unsigned __int8 *)(v_rip + 3787340)) == 0) {
        a1 = 1;
        result = IoNotifyDump(a1, *(unsigned __int64 *)(a1 + 184), a3, a4);
    }
    a2 = (*(unsigned __int64 *)(a1 + 184)) << (32);
    result = (result) | (a2);
    result = IoInitializeDumpStack(*(unsigned __int64 *)(a1 + 184), a2, a3, a4);
    result = Feature_CrashDumpOneMBTransferSize__private_IsEnabledDeviceUsageNoInline(*(unsigned __int64 *)(a1 + 184), a2, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_00B6F57A;
    a1 = 0;
    result = IoGetDumpStackTransferSizes(a1, v_stack_m2B4, a3, a4);
    if (((unsigned int)((unsigned int)(v_stack_m2B4))) >= ((unsigned int)((unsigned int)(0x100000ULL)))) {
        a1 = (unsigned int)((unsigned int)(0x100000ULL));
        v_stack_m2B4 = (unsigned int)((unsigned int)(0x100000ULL));
    }
    a1 = (unsigned int)((a1) >> (12));
    result = (unsigned int)(*(unsigned int *)(a1 + 440));
    if (((unsigned int)(a1)) != ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 440))))) {
        result = (unsigned int)(*(unsigned int *)(a1 + 440));
        if (((unsigned int)(a1)) <= ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 440))))) { result = (unsigned int)(a1); }
        *(unsigned int *)(a1 + 440) = (unsigned int)(result);
    }
    a2 = (v_stack_m2B4) << (32);
    result = (result) | (a2);
    result = (result) - (result);
    if (sign_flag) goto loc_00B6FAC6;
    if ((*(unsigned int *)(v_rip + 3788100)) == 1) goto loc_00B6FAC6;
    result = PopMarkComponentsBootPhase(a1, a2, a3, a4);
    if ((*(unsigned __int64 *)(a1 + 80)) == (a1 + 80)) goto loc_00B6F61B;
loc_00B6F5B6:
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 80) + 32)) - (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 80) + 24));
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 80) + 24)) >= (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 80) + 32))) goto loc_00B6F614;
loc_00B6F5DC:
    result = PopCreateDumpMdl(a1, v_stack_m2B0, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 80) + 24), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 80) + 32));
    result = memcpy(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 80) + 40), *(unsigned __int64 *)(v_stack_m2B0 + 24), (unsigned int)(*(unsigned int *)(v_stack_m2B0 + 40)), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 80) + 32));
    v_r12 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 80) + 40)) + ((unsigned int)(*(unsigned int *)(v_stack_m2B0 + 40)));
    result = ((unsigned int)(*(unsigned int *)(v_stack_m2B0 + 40))) >> (12);
    v_rdi = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 80) + 24)) + (result);
    if (v_rdi < (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 80) + 32))) goto loc_00B6F5DC;
loc_00B6F614:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 80))) != (a1 + 80)) goto loc_00B6F5B6;
    v_rsi = 0;
loc_00B6F61B:
    result = PopResetRangeEnum(a1, *(unsigned __int64 *)(v_stack_m2B0 + 24), (unsigned int)(*(unsigned int *)(v_stack_m2B0 + 40)), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 80) + 32));
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 176)) = *(unsigned __int64 *)(v_rip + 3787015);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 176) + 8) = *(unsigned __int64 *)(v_rip + 3787015);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 176) + 16) = 0;
    a2 = (*(unsigned __int64 *)(v_stack_m2B0 + 24)) << (32);
    result = (*(unsigned __int64 *)(v_rip + 3787015)) | (a2);
    v_stack_m2B0 = result;
    result = PopWriteHeaderPages(a1, *(unsigned __int64 *)(a1 + 216), (unsigned int)(*(unsigned int *)(v_stack_m2B0 + 40)), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 80) + 32));
    if (sign_flag) goto loc_00B6FA44;
    v_rbx = (unsigned int)((unsigned int)(result));
    if ((*(unsigned __int8 *)(a1 + 488)) != 0) {
        a1 = *(unsigned int *)(a1 + 32);
        result = *(unsigned int *)(a1 + 280);
        a1 = (unsigned int)((a1) >> (3));
        result = (unsigned int)((result) + (2));
        a1 = (unsigned int)((a1) + (0xFFFULL));
        *(unsigned int *)(a1 + 200) = 3;
        a1 = (unsigned int)((a1) >> (12));
        result = (unsigned int)((result) + ((unsigned int)(a1)));
        a1 = a1;
        *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 216) + 96) = result;
        v_rbx = *(unsigned __int64 *)(v_rip + 3787991);
        result = PopWriteSecurePages(a1, *(unsigned __int64 *)(a1 + 216), (unsigned int)(*(unsigned int *)(v_stack_m2B0 + 40)), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 80) + 32));
        result = *(unsigned __int64 *)(v_rip + 3787979);
        result = (result) - (v_rbx);
        *(unsigned __int64 *)(v_rip + 3788705) = result;
        result = *(unsigned int *)(a1 + 284);
        *(unsigned __int64 *)(v_rip + 3788395) = result;
    }
    *(unsigned int *)(a1 + 200) = 4;
    *(unsigned __int64 *)(a1 + 112) = a1 + 64;
    result = RtlNumberOfClearBits(a1 + 64, *(unsigned __int64 *)(a1 + 216), (unsigned int)(*(unsigned int *)(v_stack_m2B0 + 40)), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 80) + 32));
    a2 = 0;
    v_r14 = (*(unsigned __int64 *)(a1 + 104)) + ((unsigned int)((unsigned int)(result)));
    v_r14 = (v_r14) << (12);
    result = memset(*(unsigned __int64 *)(v_rip + 3786974), a2, a2 + 64, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 80) + 32));
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 3786974) + 24) = 0;
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 3786974) + 8) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 312)));
    v_rsi = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3786974)) = *(unsigned __int64 *)(a1 + 304);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3786974) + 16) = v_r14;
    *(unsigned __int64 *)(v_rip + 3788305) = 0;
    *(unsigned __int64 *)(v_rip + 3788306) = 0;
    *(unsigned int *)(a1 + 360) = 0;
    *(unsigned __int64 *)(a1 + 376) = 0;
    if (v_stack_m2B8 == 0) goto loc_00B6F762;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184) + 128)) != 0) {
        *(unsigned __int8 *)(a1 + 424) = 1;
    }
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 280))) + (2));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 32))) >> (3));
    a1 = (unsigned int)((a1) + (0xFFFULL));
    a1 = (unsigned int)((a1) >> (12));
    a1 = (unsigned int)((a1) + (*(unsigned int *)(a1 + 284)));
    result = (unsigned int)((result) + ((unsigned int)(a1)));
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 216) + 104) = result;
    result = (result) << (12);
    *(unsigned __int64 *)(a1 + 408) = result;
    a2 = (a2) << (32);
    result = (result) | (a2);
    *(unsigned __int8 *)(a1 + 3) = 1;
    result = PopWriteHiberImage(a1, 1, a2 + 64, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 80) + 32));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 8)))) == (*(unsigned int *)(a1 + 288))) goto loc_00B6F7D0;
loc_00B6F7C1:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 8)))) != (*(unsigned int *)(a1 + 288))) goto loc_00B6F7C1;
loc_00B6F7D0:
    a2 = (1) << (32);
    result = ((unsigned int)(*(unsigned int *)(a1 + 8))) | (a2);
    result = (result) - (result);
    *(unsigned __int64 *)(v_rip + 3788410) = result;
    if ((*(unsigned int *)(a1 + 288)) <= 0) goto loc_00B6F8AF;
loc_00B6F7FA:
    v_r10 = (v_r10) * (0);
    v_r10 = (v_r10) - (v_rip + 3788286);
loc_00B6F810:
    *(unsigned __int64 *)(v_r10 + v_rip + 3788286 * 1 + *(unsigned __int64 *)(a1 + 296) * 1 + 88) = 0;
    v_r11 = (5) - (1);
    if (condition_is_not_equal) goto loc_00B6F810;
    a1 = (*(unsigned __int64 *)(v_r10 + v_rip + 3788286 * 1 + *(unsigned __int64 *)(a1 + 296) * 1 + 88)) * (0);
    a1 = (*(unsigned __int64 *)(a1 + *(unsigned __int64 *)(a1 + 296) * 1 + 40)) * (0);
    *(unsigned __int64 *)(a1 + *(unsigned __int64 *)(a1 + 296) * 1 + 40) = 0;
    a1 = (a1) * (0);
    a3 = (unsigned int)((0) + 1);
    a1 = (*(unsigned __int64 *)(a1 + *(unsigned __int64 *)(a1 + 296) * 1 + 56)) * (0);
    *(unsigned __int64 *)(a1 + *(unsigned __int64 *)(a1 + 296) * 1 + 56) = 0;
    if (((unsigned int)(a3)) < (*(unsigned int *)(a1 + 288))) goto loc_00B6F7FA;
loc_00B6F8AF:
    result = (*(unsigned __int64 *)(v_rip + 3787458)) - (*(unsigned __int64 *)(v_rip + 3787829));
    *(unsigned __int64 *)(v_rip + 3788164) = result;
    *(unsigned __int64 *)(v_rip + 3787894) = *(unsigned __int64 *)(v_rip + 3787933);
    *(unsigned __int64 *)(v_rip + 3787897) = (unsigned int)(*(unsigned int *)(v_rip + 3787928));
    *(unsigned __int64 *)(v_rip + 3787906) = 0;
    *(unsigned int *)(v_rip + 3787908) = 0;
    *(unsigned int *)(a1 + 200) = 5;
    *(unsigned __int64 *)(a1 + 112) = a1 + 48;
    *(unsigned __int64 *)(a1 + 128) = 0;
    result = RtlNumberOfClearBits(a1 + 48, v_r10 + v_rip + 3788286 * 1, a3, v_rip + 3788286 + 8);
    a2 = 0;
    v_r14 = ((unsigned int)((unsigned int)(result))) << (12);
    result = memset(*(unsigned __int64 *)(v_rip + 3786426), a2, a2 + 64, v_rip + 3788286 + 8);
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 3786426) + 24) = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3786426)) = *(unsigned __int64 *)(a1 + 304);
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 3786426) + 8) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 312)));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3786426) + 16) = v_r14;
    result = (*(unsigned __int64 *)(a1 + 408)) + (0xFFFULL);
    result = (result) >> (12);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 216) + 112) = result;
    a2 = (a2) << (32);
    v_rsi = 0;
    result = (result) | (a2);
    *(unsigned int *)(a1 + 8) = 0;
    a2 = 0;
    *(unsigned __int64 *)(a1 + 376) = 0;
    result = PopWriteHiberImage(a1, a2, a2 + 64, v_rip + 3788286 + 8);
    a2 = (a2) << (32);
    result = (result) | (a2);
    result = (result) - (result);
    *(unsigned __int64 *)(v_rip + 3787982) = result;
    result = (*(unsigned __int64 *)(v_rip + 3787223)) - (*(unsigned __int64 *)(v_rip + 3787290));
    *(unsigned __int64 *)(v_rip + 3787941) = result;
    result = PopHiberWriteBootFreePageMap(a1, *(unsigned __int64 *)(a1 + 216), a2 + 64, v_rip + 3788286 + 8);
    *(unsigned int *)(a1 + 200) = 7;
    result = PopWriteChecksumPages(a1, *(unsigned __int64 *)(a1 + 216), a2 + 64, v_rip + 3788286 + 8);
    *(unsigned int *)(a1 + 200) = 6;
    result = PopWriteImageHeader(a1, *(unsigned __int64 *)(a1 + 216), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 216) + 80)))), v_stack_m2B0);
    if (sign_flag) goto loc_00B6FA44;
    if ((*(unsigned int *)(v_rip + 3785588)) != ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3785602))))) goto loc_00B6FA1B;
    result = (unsigned int)(*(unsigned int *)(v_rip + 3785602));
    if (((*(unsigned int *)(v_rip + 3790088)) & (0x8000ULL)) == 0) {
        a3 = 0;
        a2 = v_rsi - 2;
        a1 = 0;
        result = DbgUnLoadImageSymbols(a1, a2, a3, v_stack_m2B0);
    }
    result = VslNotifyShutdown(1, a2, a3, v_stack_m2B0);
loc_00B6FA1B:
    if (((*(unsigned int *)(v_rip + 3790055)) & (0x1000ULL)) != 0) {
        a1 = 3;
        result = HalReturnToFirmware(a1, a2, a3, v_stack_m2B0);
    }
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 3786921)))) & (16)) == 0) goto loc_00B6FA44;
    goto loc_00B6FA7D;
loc_00B6FA44:
    result = KdPowerTransition(4, a2, a3, v_stack_m2B0);
    if (sign_flag) goto loc_00B6FA7D;
    if (((unsigned int)((unsigned int)(0x40000294ULL))) == 0x40000294ULL) goto loc_00B6FA7D;
    if ((*(unsigned int *)(v_rip + 3785483)) != 5) goto loc_00B6FA7D;
    result = PopNotifyShutdownListener(4, a2, a3, v_stack_m2B0);
    if ((*(unsigned __int8 *)(v_rip + 4550696)) != 0) {
        a1 = 0;
        result = HvlConfigureMemoryZeroingOnReset(a1, a2, a3, v_stack_m2B0);
    }
    result = PopSetMemoryOverwriteRequestAction(a1, a2, a3, v_stack_m2B0);
loc_00B6FA7D:
    result = PopCheckpointSystemSleep(24, a2, a3, v_stack_m2B0);
    result = guard_dispatch_icall(24, a2, a3, v_stack_m2B0);
loc_00B6FA93:
    a1 = (*(unsigned __int64 *)(v_rsp - 488 + 432)) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, v_stack_m2B0);
    return result;
loc_00B6FAC6:
    result = PopCheckpointSystemSleep(20, a2, a3, v_stack_m2B0);
    a3 = 0;
    result = PopInternalAddToDumpFile(*(unsigned __int64 *)(a1 + 184), 376, a3, v_stack_m2B0);
    v_stack_m2A0 = *(unsigned __int64 *)(v_stack_m28 + 64);
    result = KeBugCheckEx(160, 12, *(unsigned __int64 *)(v_stack_m28 + 56), *(unsigned __int64 *)(a1 + 184));
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopSaveHiberContext(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m270;
    uint64_t v_stack_m278;
    uint64_t v_stack_m28;
    uint64_t v_stack_m280;
    uint64_t v_stack_m288;
    uint64_t v_stack_m290;
    uint64_t v_stack_m298;
    uint64_t v_stack_m2A0;
    uint32_t v_stack_m2A8;
    uint64_t v_stack_m2B0;
    uint32_t v_stack_m2B4;
    uint8_t v_stack_m2B8;
    uint64_t v_stack_m2C8;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (704);
    result = (*(uint64_t *)(v_rip + 0x29B6C3)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x1E8 + 0x1B0) = result;
    result = 0;
    *(uint64_t *)(local_rsp - 0x1E8 - 0x40) = 0;
    v_stack_m290 = 0;
    Arg2 = 0;
    *(uint64_t *)(local_rsp - 0x1E8 - 0x50) = v_xmm0;
    v_stack_m2A0 = v_xmm1;
    result = memset(local_rsp - 488 + 112, Arg2, 312, a4);
    local_rsi = 0;
    v_stack_m2A8 = 0;
    v_stack_m2B4 = 0;
    result = Feature_CrashDumpOneMBTransferSize__private_IsEnabledDeviceUsageNoInline(local_rsp - 488 + 112, Arg2, 312, a4);
    if ((uint32_t)(result) != 0) goto loc_00B6F0D3;
    v_stack_m2B0 = local_rsp - 488 + 112;
    goto loc_00B6F0DF;
loc_00B6F0D3:
    v_stack_m2B0 = *(uint64_t *)(arg1 + 0x160);
loc_00B6F0DF:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x24))) != 0) goto loc_00B6F0FF;
    result = PopCheckpointSystemSleep((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x24)) + 19, Arg2, 312, a4);
    goto loc_00B6F150;
loc_00B6F0FF:
    result = 0;
    if (((*(uint8_t *)(v_rip + 0x45798A)) & (2)) != 0) { result = 1; }
    if ((*(uint8_t *)(v_rip + 0x45796F)) != 0) goto loc_00B6F11B;
    if ((uint8_t)(result) == 0) goto loc_00B6F150;
loc_00B6F11B:
    goto loc_00B6F124;
loc_00B6F122:
loc_00B6F124:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x10))) != 0) goto loc_00B6F122;
    if ((*(uint8_t *)(v_rip + 0x39D54D)) == 0) goto loc_00B6F13F;
    goto loc_00B6FA93;
loc_00B6F13F:
    goto loc_00B6F148;
loc_00B6F146:
loc_00B6F148:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x14))) != 0) goto loc_00B6F146;
loc_00B6F150:
    if (((uint32_t)((uint32_t)(0x40000294ULL))) < (*(uint32_t *)(arg1 + 0x120))) goto loc_00B6F160;
    goto loc_00B6FA93;
loc_00B6F160:
    if (0 != 0) goto loc_00B6F180;
    *(uint32_t *)(v_rip + 0x39EC3A) = 0;
    result = KeDisableInterrupts((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x24)) + 19, Arg2, 312, a4);
    if ((uint8_t)(result) == 0) goto loc_00B6F1D1;
    result = PopInternalError((uint32_t)(0xA1E60ULL), Arg2, 312, a4);
loc_00B6F17E:
loc_00B6F180:
    if ((uint8_t)(*(uint8_t *)(arg1 + 0x3)) == 0) goto loc_00B6F17E;
    local_rbx = (0) * (0);
    Arg2 = (*(uint64_t *)(arg1 + 0x128)) + (local_rbx);
    result = PopCompressHiberBlocks(Arg1, Arg2, 1, a4);
    goto loc_00B6F1AD;
loc_00B6F1AB:
loc_00B6F1AD:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x8))) != 0) goto loc_00B6F1AB;
    a3 = 0;
    Arg2 = (*(uint64_t *)(arg1 + 0x128)) + (local_rbx);
    result = PopCompressHiberBlocks(Arg1, Arg2, a3, a4);
    goto loc_00B6FA93;
loc_00B6F1D1:
    if (!sign_flag) goto loc_00B6F1E2;
    v_stack_m2B8 = 0;
    goto loc_00B6F1F4;
loc_00B6F1E2:
    result = IoDumpStackResumeCapable(v_stack_m2A8, Arg2, a3, a4);
    v_stack_m2B8 = (uint8_t)(result);
    if ((uint8_t)(result) == 0) {
        *(uint8_t *)(v_rip + 0x39CD5F) = 1;
    }
    result = kernel_indirect_call(v_stack_m2A8, Arg2, a3, a4);
    if ((uint32_t)(result) != 0) {
        *(uint8_t *)(v_rip + 0x39CD41) = 1;
    }
    result = guard_dispatch_icall(v_stack_m2A8, Arg2, a3, a4);
    if ((uint8_t)(result) == 0) {
        *(uint8_t *)(v_rip + 0x39CD23) = 1;
    }
    if ((*(uint8_t *)(v_rip + 0x39CD1C)) == 0) goto loc_00B6F26C;
    result = PopIsMktmeEnabled(v_stack_m2A8, Arg2, a3, a4);
    if ((uint8_t)(result) != 0) {
        Arg2 = 274;
        v_stack_m2C8 = 0;
        a4 = Arg1;
        a3 = 10;
        Arg1 = Arg2 - 114;
        result = KeBugCheckEx(Arg1, Arg2, a3, a4);
    }
    *(uint64_t *)(arg1 + 0xB0) = local_rsp - 488 - 80;
    *(uint64_t *)(arg1 + 0xC0) = v_rip + 2851972;
    *(uint8_t *)(arg1 + 0x1) = 1;
    if ((*(uint8_t *)(v_rip + 0x457824)) == 0) goto loc_00B6F462;
    Arg1 = 0;
    *(uint32_t *)(v_rip + 0x39EBB6) = 1;
    result = HvlDisableEnlightenment(Arg1, Arg2, a3, a4);
    result = guard_dispatch_icall(Arg1, Arg2, a3, a4);
    result = 0;
    if (((*(uint8_t *)(v_rip + 0x4577D2)) & (2)) != 0) { result = 1; }
    if ((*(uint8_t *)(v_rip + 0x4577B7)) != 0) goto loc_00B6F2D7;
    if ((uint8_t)(result) == 0) goto loc_00B6F44A;
loc_00B6F2D7:
    goto loc_00B6F2E0;
loc_00B6F2DE:
loc_00B6F2E0:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x10)))) != ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x457796))))) goto loc_00B6F2DE;
    v_stack_m288 = *(uint64_t *)(v_rip + 0x2B8603);
    v_stack_m280 = *(uint64_t *)(v_rip + 0x2B8597);
    v_stack_m278 = *(uint64_t *)(v_rip + 0x2B8593);
    v_stack_m270 = *(uint64_t *)(v_rip + 0x2B8572);
    *(uint64_t *)(local_rsp - 0x1E8 - 0x80) = *(uint64_t *)(v_rip + 0x2B8586);
    *(uint64_t *)(local_rsp - 0x1E8 - 0x78) = *(uint64_t *)(v_rip + 0x2B856E);
    *(uint64_t *)(local_rsp - 0x1E8 - 0x70) = *(uint64_t *)(v_rip + 0x2B8593);
    *(uint64_t *)(local_rsp - 0x1E8 - 0x68) = *(uint64_t *)(v_rip + 0x2B8590);
    *(uint64_t *)(local_rsp - 0x1E8 - 0x60) = *(uint64_t *)(v_rip + 0x2B858D);
    *(uint64_t *)(local_rsp - 0x1E8 - 0x58) = *(uint64_t *)(v_rip + 0x2B858A);
    if ((*(uint8_t *)(arg1 + 0x1E8)) == 0) goto loc_00B6F39E;
    *(uint64_t *)(local_rsp - 0x1E8 - 0x30) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x1E8 - 0x10) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x1E8 - 0x20) = v_xmm1;
    *(uint64_t *)(local_rsp - 0x1E8 + 0x10) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x1E8) = v_xmm1;
    result = HvlPrepareForSecureHibernate(local_rsp - 488 - 48, Arg2, a3, a4);
    goto loc_00B6F3E8;
loc_00B6F39E:
    *(uint64_t *)(local_rsp - 0x1E8 + 0x20) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x1E8 + 0x40) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x1E8 + 0x30) = v_xmm1;
    *(uint64_t *)(local_rsp - 0x1E8 + 0x60) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x1E8 + 0x50) = v_xmm1;
    v_stack_m2C8 = *(uint64_t *)(arg1 + 0xD8) + 1176;
    result = HvlPrepareForHibernate(local_rsp - 488 + 32, *(uint64_t *)(arg1 + 0xD8) + 1152, *(uint64_t *)(arg1 + 0xD8) + 1160, *(uint64_t *)(arg1 + 0xD8) + 1168);
loc_00B6F3E8:
    if (sign_flag) {
        Arg1 = *(uint64_t *)(arg1 + 0xB8);
        a3 = 0;
        Arg2 = 376;
        result = PopInternalAddToDumpFile(Arg1, Arg2, a3, *(uint64_t *)(arg1 + 0xD8) + 1168);
        a4 = *(uint64_t *)(arg1 + 0xB8);
        Arg2 = 12;
        a3 = (int32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
        Arg1 = 160;
        v_stack_m2C8 = 0;
        result = KeBugCheckEx(Arg1, Arg2, a3, a4);
    }
    *(uint32_t *)(arg1 + 0x10) = 0;
    goto loc_00B6F42E;
loc_00B6F42C:
loc_00B6F42E:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x14)))) != ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x457648))))) goto loc_00B6F42C;
    *(uint32_t *)(arg1 + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x45763E)));
    *(uint32_t *)(arg1 + 0x14) = 0;
loc_00B6F44A:
    if ((*(uint8_t *)(arg1 + 0x1E8)) == 0) goto loc_00B6F45D;
    result = HvlDiscardSecurePagesFromHibernation(Arg1, Arg2, a3, a4);
    goto loc_00B6F462;
loc_00B6F45D:
    result = HvlDiscardPagesFromHibernation(Arg1, Arg2, a3, a4);
loc_00B6F462:
    if ((*(uint8_t *)(arg1 + 0x1ED)) != 0) {
        result = v_rip - 6130;
        v_stack_m2A0 = *(uint64_t *)(arg1 + 0xD8);
        v_stack_m298 = result;
        Arg2 = v_stack_m2A0;
        result = v_rip - 6104;
        Arg1 = 0;
        v_stack_m290 = result;
        result = PopSstInvokeNotificationHandlers(Arg1, Arg2, a3, a4);
    }
    if (condition_is_below_or_equal) goto loc_00B6F4C8;
loc_00B6F4AD:
    a3 = (uint32_t)((0) + (1));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x40))) >> (5));
    if (((uint32_t)(a3)) < ((uint32_t)(result))) goto loc_00B6F4AD;
loc_00B6F4C8:
    result = Arg1 + 48;
    if ((*(uint8_t *)(v_rip + 0x39CA92)) == 0) {
        Arg1 = Arg1 + 64;
        a3 = 0;
        Arg2 = Arg1 + 48;
        result = RtlCopyBitMap(Arg1, Arg2, a3, a4);
        result = Arg1 + 64;
    }
    result = RtlSetAllBits(result, Arg2, a3, a4);
    *(uint32_t *)(arg1 + 0xC8) = 8;
    *(uint32_t *)(v_rip + 0x39E956) = 1;
    result = IoGetDumpHiberRanges(result, *(uint64_t *)(arg1 + 0xB8), a3, a4);
    if ((*(uint8_t *)(v_rip + 0x39CA4C)) == 0) {
        Arg1 = 1;
        result = IoNotifyDump(Arg1, *(uint64_t *)(arg1 + 0xB8), a3, a4);
    }
    Arg2 = (*(uint64_t *)(arg1 + 0xB8)) << (32);
    result = (result) | (Arg2);
    result = IoInitializeDumpStack(*(uint64_t *)(arg1 + 0xB8), Arg2, a3, a4);
    result = Feature_CrashDumpOneMBTransferSize__private_IsEnabledDeviceUsageNoInline(*(uint64_t *)(arg1 + 0xB8), Arg2, a3, a4);
    if ((uint32_t)(result) == 0) goto loc_00B6F57A;
    Arg1 = 0;
    result = IoGetDumpStackTransferSizes(Arg1, v_stack_m2B4, a3, a4);
    if (((uint32_t)((uint32_t)(v_stack_m2B4))) >= ((uint32_t)((uint32_t)(0x100000ULL)))) {
        Arg1 = (uint32_t)((uint32_t)(0x100000ULL));
        v_stack_m2B4 = (uint32_t)((uint32_t)(0x100000ULL));
    }
    Arg1 = (uint32_t)((Arg1) >> (12));
    result = (uint32_t)(*(uint32_t *)(arg1 + 0x1B8));
    if (((uint32_t)(Arg1)) != ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x1B8))))) {
        result = (uint32_t)(*(uint32_t *)(arg1 + 0x1B8));
        if (((uint32_t)(Arg1)) <= ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x1B8))))) { result = (uint32_t)(Arg1); }
        *(uint32_t *)(arg1 + 0x1B8) = (uint32_t)(result);
    }
    Arg2 = (v_stack_m2B4) << (32);
    result = (result) | (Arg2);
    result = (result) - (result);
    if (sign_flag) goto loc_00B6FAC6;
    if ((*(uint32_t *)(v_rip + 0x39CD44)) == 1) goto loc_00B6FAC6;
    result = PopMarkComponentsBootPhase(Arg1, Arg2, a3, a4);
    if ((*(uint64_t *)(arg1 + 0x50)) == (Arg1 + 80)) goto loc_00B6F61B;
loc_00B6F5B6:
    result = (*(uint64_t *)(*(uint64_t *)(arg1 + 0x50) + 0x20)) - (*(uint64_t *)(*(uint64_t *)(arg1 + 0x50) + 0x18));
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x50) + 0x18)) >= (*(uint64_t *)(*(uint64_t *)(arg1 + 0x50) + 0x20))) goto loc_00B6F614;
loc_00B6F5DC:
    result = PopCreateDumpMdl(Arg1, v_stack_m2B0, *(uint64_t *)(*(uint64_t *)(arg1 + 0x50) + 0x18), *(uint64_t *)(*(uint64_t *)(arg1 + 0x50) + 0x20));
    result = memcpy(*(uint64_t *)(*(uint64_t *)(arg1 + 0x50) + 0x28), *(uint64_t *)(v_stack_m2B0 + 0x18), (uint32_t)(*(uint32_t *)(v_stack_m2B0 + 0x28)), *(uint64_t *)(*(uint64_t *)(arg1 + 0x50) + 0x20));
    local_r12 = (*(uint64_t *)(*(uint64_t *)(arg1 + 0x50) + 0x28)) + ((uint32_t)(*(uint32_t *)(v_stack_m2B0 + 0x28)));
    result = ((uint32_t)(*(uint32_t *)(v_stack_m2B0 + 0x28))) >> (12);
    local_rdi = (*(uint64_t *)(*(uint64_t *)(arg1 + 0x50) + 0x18)) + (result);
    if (local_rdi < (*(uint64_t *)(*(uint64_t *)(arg1 + 0x50) + 0x20))) goto loc_00B6F5DC;
loc_00B6F614:
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x50))) != (Arg1 + 80)) goto loc_00B6F5B6;
    local_rsi = 0;
loc_00B6F61B:
    result = PopResetRangeEnum(Arg1, *(uint64_t *)(v_stack_m2B0 + 0x18), (uint32_t)(*(uint32_t *)(v_stack_m2B0 + 0x28)), *(uint64_t *)(*(uint64_t *)(arg1 + 0x50) + 0x20));
    *(uint64_t *)(*(uint64_t *)(arg1 + 0xB0)) = *(uint64_t *)(v_rip + 0x39C907);
    *(uint64_t *)(*(uint64_t *)(arg1 + 0xB0) + 0x8) = *(uint64_t *)(v_rip + 0x39C907);
    *(uint64_t *)(*(uint64_t *)(arg1 + 0xB0) + 0x10) = 0;
    Arg2 = (*(uint64_t *)(v_stack_m2B0 + 0x18)) << (32);
    result = (*(uint64_t *)(v_rip + 0x39C907)) | (Arg2);
    v_stack_m2B0 = result;
    result = PopWriteHeaderPages(Arg1, *(uint64_t *)(arg1 + 0xD8), (uint32_t)(*(uint32_t *)(v_stack_m2B0 + 0x28)), *(uint64_t *)(*(uint64_t *)(arg1 + 0x50) + 0x20));
    if (sign_flag) goto loc_00B6FA44;
    local_rbx = (uint32_t)((uint32_t)(result));
    if ((*(uint8_t *)(arg1 + 0x1E8)) != 0) {
        Arg1 = *(uint32_t *)(arg1 + 0x20);
        result = *(uint32_t *)(arg1 + 0x118);
        Arg1 = (uint32_t)((Arg1) >> (3));
        result = (uint32_t)((result) + (2));
        Arg1 = (uint32_t)((Arg1) + (0xFFFULL));
        *(uint32_t *)(arg1 + 0xC8) = 3;
        Arg1 = (uint32_t)((Arg1) >> (12));
        result = (uint32_t)((result) + ((uint32_t)(Arg1)));
        Arg1 = Arg1;
        *(uint64_t *)(*(uint64_t *)(arg1 + 0xD8) + 0x60) = result;
        local_rbx = *(uint64_t *)(v_rip + 0x39CCD7);
        result = PopWriteSecurePages(Arg1, *(uint64_t *)(arg1 + 0xD8), (uint32_t)(*(uint32_t *)(v_stack_m2B0 + 0x28)), *(uint64_t *)(*(uint64_t *)(arg1 + 0x50) + 0x20));
        result = *(uint64_t *)(v_rip + 0x39CCCB);
        result = (result) - (local_rbx);
        *(uint64_t *)(v_rip + 0x39CFA1) = result;
        result = *(uint32_t *)(arg1 + 0x11C);
        *(uint64_t *)(v_rip + 0x39CE6B) = result;
    }
    *(uint32_t *)(arg1 + 0xC8) = 4;
    *(void **)(arg1 + 0x70) = Arg1 + 64;
    result = RtlNumberOfClearBits(Arg1 + 64, *(uint64_t *)(arg1 + 0xD8), (uint32_t)(*(uint32_t *)(v_stack_m2B0 + 0x28)), *(uint64_t *)(*(uint64_t *)(arg1 + 0x50) + 0x20));
    Arg2 = 0;
    local_r14 = (*(uint64_t *)(arg1 + 0x68)) + ((uint32_t)((uint32_t)(result)));
    local_r14 = (local_r14) << (12);
    result = memset(*(uint64_t *)(v_rip + 0x39C8DE), Arg2, Arg2 + 64, *(uint64_t *)(*(uint64_t *)(arg1 + 0x50) + 0x20));
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x39C8DE) + 0x18) = 0;
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x39C8DE) + 0x8) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x138)));
    local_rsi = 0;
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x39C8DE)) = *(uint64_t *)(arg1 + 0x130);
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x39C8DE) + 0x10) = local_r14;
    *(uint64_t *)(v_rip + 0x39CE11) = 0;
    *(uint64_t *)(v_rip + 0x39CE12) = 0;
    *(uint32_t *)(arg1 + 0x168) = 0;
    *(uint64_t *)(arg1 + 0x178) = 0;
    if (v_stack_m2B8 == 0) goto loc_00B6F762;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8) + 0x80)) != 0) {
        *(uint8_t *)(arg1 + 0x1A8) = 1;
    }
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x118))) + (2));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x20))) >> (3));
    Arg1 = (uint32_t)((Arg1) + (0xFFFULL));
    Arg1 = (uint32_t)((Arg1) >> (12));
    Arg1 = (uint32_t)((Arg1) + (*(uint32_t *)(arg1 + 0x11C)));
    result = (uint32_t)((result) + ((uint32_t)(Arg1)));
    *(uint64_t *)(*(uint64_t *)(arg1 + 0xD8) + 0x68) = result;
    result = (result) << (12);
    *(uint64_t *)(arg1 + 0x198) = result;
    Arg2 = (Arg2) << (32);
    result = (result) | (Arg2);
    *(uint8_t *)(arg1 + 0x3) = 1;
    result = PopWriteHiberImage(Arg1, 1, Arg2 + 64, *(uint64_t *)(*(uint64_t *)(arg1 + 0x50) + 0x20));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x8)))) == (*(uint32_t *)(arg1 + 0x120))) goto loc_00B6F7D0;
loc_00B6F7C1:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x8)))) != (*(uint32_t *)(arg1 + 0x120))) goto loc_00B6F7C1;
loc_00B6F7D0:
    Arg2 = (1) << (32);
    result = ((uint32_t)(*(uint32_t *)(arg1 + 0x8))) | (Arg2);
    result = (result) - (result);
    *(uint64_t *)(v_rip + 0x39CE7A) = result;
    if ((*(uint32_t *)(arg1 + 0x120)) <= 0) goto loc_00B6F8AF;
loc_00B6F7FA:
    local_r10 = (local_r10) * (0);
    local_r10 = (local_r10) - (v_rip + 3788286);
loc_00B6F810:
    *(uint64_t *)(local_r10 + v_rip + 0x39CDFE * 1 + *(uint64_t *)(arg1 + 0x128) * 1 + 0x58) = 0;
    local_r11 = (5) - (1);
    if (condition_is_not_equal) goto loc_00B6F810;
    Arg1 = (*(uint64_t *)(local_r10 + v_rip + 0x39CDFE * 1 + *(uint64_t *)(arg1 + 0x128) * 1 + 0x58)) * (0);
    Arg1 = (*(uint64_t *)(arg1 + *(uint64_t *)(arg1 + 0x128) * 1 + 0x28)) * (0);
    *(uint64_t *)(arg1 + *(uint64_t *)(arg1 + 0x128) * 1 + 0x28) = 0;
    Arg1 = (Arg1) * (0);
    a3 = (uint32_t)((0) + 1);
    Arg1 = (*(uint64_t *)(arg1 + *(uint64_t *)(arg1 + 0x128) * 1 + 0x38)) * (0);
    *(uint64_t *)(arg1 + *(uint64_t *)(arg1 + 0x128) * 1 + 0x38) = 0;
    if (((uint32_t)(a3)) < (*(uint32_t *)(arg1 + 0x120))) goto loc_00B6F7FA;
loc_00B6F8AF:
    result = (*(uint64_t *)(v_rip + 0x39CAC2)) - (*(uint64_t *)(v_rip + 0x39CC35));
    *(uint64_t *)(v_rip + 0x39CD84) = result;
    *(uint64_t *)(v_rip + 0x39CC76) = *(uint64_t *)(v_rip + 0x39CC9D);
    *(uint64_t *)(v_rip + 0x39CC79) = (uint32_t)(*(uint32_t *)(v_rip + 0x39CC98));
    *(uint64_t *)(v_rip + 0x39CC82) = 0;
    *(uint32_t *)(v_rip + 0x39CC84) = 0;
    *(uint32_t *)(arg1 + 0xC8) = 5;
    *(void **)(arg1 + 0x70) = Arg1 + 48;
    *(uint64_t *)(arg1 + 0x80) = 0;
    result = RtlNumberOfClearBits(Arg1 + 48, local_r10 + v_rip + 3788286 * 1, a3, v_rip + 3788286 + 8);
    Arg2 = 0;
    local_r14 = ((uint32_t)((uint32_t)(result))) << (12);
    result = memset(*(uint64_t *)(v_rip + 0x39C6BA), Arg2, Arg2 + 64, v_rip + 3788286 + 8);
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x39C6BA) + 0x18) = 0;
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x39C6BA)) = *(uint64_t *)(arg1 + 0x130);
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x39C6BA) + 0x8) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x138)));
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x39C6BA) + 0x10) = local_r14;
    result = (*(uint64_t *)(arg1 + 0x198)) + (0xFFFULL);
    result = (result) >> (12);
    *(uint64_t *)(*(uint64_t *)(arg1 + 0xD8) + 0x70) = result;
    Arg2 = (Arg2) << (32);
    local_rsi = 0;
    result = (result) | (Arg2);
    *(uint32_t *)(arg1 + 0x8) = 0;
    Arg2 = 0;
    *(uint64_t *)(arg1 + 0x178) = 0;
    result = PopWriteHiberImage(Arg1, Arg2, Arg2 + 64, v_rip + 3788286 + 8);
    Arg2 = (Arg2) << (32);
    result = (result) | (Arg2);
    result = (result) - (result);
    *(uint64_t *)(v_rip + 0x39CCCE) = result;
    result = (*(uint64_t *)(v_rip + 0x39C9D7)) - (*(uint64_t *)(v_rip + 0x39CA1A));
    *(uint64_t *)(v_rip + 0x39CCA5) = result;
    result = PopHiberWriteBootFreePageMap(Arg1, *(uint64_t *)(arg1 + 0xD8), Arg2 + 64, v_rip + 3788286 + 8);
    *(uint32_t *)(arg1 + 0xC8) = 7;
    result = PopWriteChecksumPages(Arg1, *(uint64_t *)(arg1 + 0xD8), Arg2 + 64, v_rip + 3788286 + 8);
    *(uint32_t *)(arg1 + 0xC8) = 6;
    result = PopWriteImageHeader(Arg1, *(uint64_t *)(arg1 + 0xD8), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0xD8) + 0x50)))), v_stack_m2B0);
    if (sign_flag) goto loc_00B6FA44;
    if ((*(uint32_t *)(v_rip + 0x39C374)) != ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x39C382))))) goto loc_00B6FA1B;
    result = (uint32_t)(*(uint32_t *)(v_rip + 0x39C382));
    if (((*(uint32_t *)(v_rip + 0x39D508)) & (0x8000ULL)) == 0) {
        a3 = 0;
        Arg2 = local_rsi - 2;
        Arg1 = 0;
        result = DbgUnLoadImageSymbols(Arg1, Arg2, a3, v_stack_m2B0);
    }
    result = VslNotifyShutdown(1, Arg2, a3, v_stack_m2B0);
loc_00B6FA1B:
    if (((*(uint32_t *)(v_rip + 0x39D4E7)) & (0x1000ULL)) != 0) {
        Arg1 = 3;
        result = HalReturnToFirmware(Arg1, Arg2, a3, v_stack_m2B0);
    }
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x39C8A9)))) & (16)) == 0) goto loc_00B6FA44;
    goto loc_00B6FA7D;
loc_00B6FA44:
    result = KdPowerTransition(4, Arg2, a3, v_stack_m2B0);
    if (sign_flag) goto loc_00B6FA7D;
    if (((uint32_t)((uint32_t)(0x40000294ULL))) == 0x40000294ULL) goto loc_00B6FA7D;
    if ((*(uint32_t *)(v_rip + 0x39C30B)) != 5) goto loc_00B6FA7D;
    result = PopNotifyShutdownListener(4, Arg2, a3, v_stack_m2B0);
    if ((*(uint8_t *)(v_rip + 0x457028)) != 0) {
        Arg1 = 0;
        result = HvlConfigureMemoryZeroingOnReset(Arg1, Arg2, a3, v_stack_m2B0);
    }
    result = PopSetMemoryOverwriteRequestAction(Arg1, Arg2, a3, v_stack_m2B0);
loc_00B6FA7D:
    result = PopCheckpointSystemSleep(24, Arg2, a3, v_stack_m2B0);
    result = guard_dispatch_icall(24, Arg2, a3, v_stack_m2B0);
loc_00B6FA93:
    Arg1 = (*(uint64_t *)(local_rsp - 0x1E8 + 0x1B0)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, a3, v_stack_m2B0);
    return result;
loc_00B6FAC6:
    result = PopCheckpointSystemSleep(20, Arg2, a3, v_stack_m2B0);
    a3 = 0;
    result = PopInternalAddToDumpFile(*(uint64_t *)(arg1 + 0xB8), 376, a3, v_stack_m2B0);
    v_stack_m2A0 = *(uint64_t *)(v_stack_m28 + 0x40);
    result = KeBugCheckEx(160, 12, *(uint64_t *)(v_stack_m28 + 0x38), *(uint64_t *)(arg1 + 0xB8));
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x1` | `8` | `W` |
| `Arg1` | `+ 0x3` | `8` | `R` |
| `Arg1` | `+ 0x3` | `8` | `W` |
| `Arg1` | `+ 0x8` | `32` | `R` |
| `Arg1` | `+ 0x8` | `32` | `R/W` |
| `Arg1` | `+ 0x8` | `32` | `W` |
| `Arg1` | `+ 0x10` | `32` | `R` |
| `Arg1` | `+ 0x10` | `32` | `R/W` |
| `Arg1` | `+ 0x10` | `32` | `W` |
| `Arg1` | `+ 0x14` | `32` | `R` |
| `Arg1` | `+ 0x14` | `32` | `R/W` |
| `Arg1` | `+ 0x14` | `32` | `W` |
| `Arg1` | `+ 0x20` | `32` | `R` |
| `Arg1` | `+ 0x30` | `64` | `R` |
| `Arg1` | `+ 0x38` | `64` | `R` |
| `Arg1` | `+ 0x40` | `32` | `R` |
| `Arg1` | `+ 0x40` | `64` | `R` |
| `Arg1` | `+ 0x48` | `64` | `R` |
| `Arg1` | `+ 0x50` | `64` | `R` |
| `Arg1` | `+ 0x68` | `64` | `R` |
| `Arg1` | `+ 0x68` | `64` | `R/W` |
| `Arg1` | `+ 0x70` | `64` | `W` |
| `Arg1` | `+ 0x80` | `64` | `W` |
| `Arg1` | `+ 0xB0` | `64` | `R` |
| `Arg1` | `+ 0xB0` | `64` | `W` |
| `Arg1` | `+ 0xB8` | `64` | `R` |
| `Arg1` | `+ 0xC0` | `64` | `W` |
| `Arg1` | `+ 0xC8` | `32` | `W` |
| `Arg1` | `+ 0xCC` | `32` | `R` |
| `Arg1` | `+ 0xD8` | `64` | `R` |
| `Arg1` | `+ 0x118` | `32` | `R` |

추가 오프셋 15개는 표에서 생략했습니다.

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagelk&rva=0x00B6F050&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
