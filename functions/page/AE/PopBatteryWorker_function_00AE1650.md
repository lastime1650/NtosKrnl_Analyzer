# PopBatteryWorker

- RVA: `0x00AE1650`–`0x00AE2D33` (길이 `5,859` bytes)
- VA: `0x0000000140AE1650`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CCF88`
- 디코드: `1,291`개 명령, `5,859/5,859` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **88**; 고유 호출 대상: **40**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **75**

### Outgoing calls
- `0x00AE16D6` → [PopAcquireRwLockShared](../../text/2D/PopAcquireRwLockShared_function_002D9A40.md) (function, `0x002D9A40`)
- `0x00AE16E2` → [PopAcquireRwLockExclusive](../../text/43/PopAcquireRwLockExclusive_function_00430B44.md) (function, `0x00430B44`)
- `0x00AE171C` → [ZwQueryWnfStateData](../../text/6A/ZwQueryWnfStateData_function_006AFEF0.md) (function, `0x006AFEF0`)
- `0x00AE177F` → [IoCancelIrp](../../text/27/IoCancelIrp_function_002720E0.md) (function, `0x002720E0`)
- `0x00AE17A3` → [IoCancelIrp](../../text/27/IoCancelIrp_function_002720E0.md) (function, `0x002720E0`)
- `0x00AE17C2` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (function, `0x0020E6B0`)
- `0x00AE17F3` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (function, `0x0020E6B0`)
- `0x00AE1848` → [PopAcquirePolicyLock](../../pagelk/B7/PopAcquirePolicyLock_function_00B783C0.md) (function, `0x00B783C0`)
- `0x00AE184F` → [PopResetCBTriggers](../76/PopResetCBTriggers_function_007683F8.md) (function, `0x007683F8`)
- `0x00AE1854` → [PopReleasePolicyLock](../../pagelk/B7/PopReleasePolicyLock_function_00B78410.md) (function, `0x00B78410`)
- `0x00AE189E` → [Feature_BatteryChargeLimitV2Support__private_IsEnabledDeviceUsageNoInline](../../text/5D/Feature_BatteryChargeLimitV2Support__private_IsEnabledDeviceUsageNoInline_function_005D9484.md) (function, `0x005D9484`)
- `0x00AE1911` → [PopBatteryReadTag](../AC/PopBatteryReadTag_function_00AC5E1C.md) (function, `0x00AC5E1C`)
- `0x00AE191D` → [PopBatteryWaitTag](../AD/PopBatteryWaitTag_function_00AD2BF8.md) (function, `0x00AD2BF8`)
- `0x00AE195D` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (function, `0x0020E6B0`)
- `0x00AE1965` → [PopBatteryInitialize](../76/PopBatteryInitialize_function_00766834.md) (function, `0x00766834`)
- `0x00AE1976` → [PopBatteryWaitTag](../AD/PopBatteryWaitTag_function_00AD2BF8.md) (function, `0x00AD2BF8`)
- `0x00AE19C8` → [PopBatteryQueryStatus](PopBatteryQueryStatus_function_00AE1450.md) (function, `0x00AE1450`)
- `0x00AE19DB` → [PopBatteryQueueWork](../../text/4A/PopBatteryQueueWork_function_004AE3DC.md) (function, `0x004AE3DC`)
- `0x00AE19E5` → [Feature_BatteryChargeLimitV2Support__private_IsEnabledDeviceUsageNoInline](../../text/5D/Feature_BatteryChargeLimitV2Support__private_IsEnabledDeviceUsageNoInline_function_005D9484.md) (function, `0x005D9484`)
- `0x00AE1A3D` → [PopBatterySetChargeLimitControl](../../text/5D/PopBatterySetChargeLimitControl_function_005D94D8.md) (function, `0x005D94D8`)
- `0x00AE1A58` → [PopAccountBatteryEnergyChange](../AD/PopAccountBatteryEnergyChange_function_00ADFE50.md) (function, `0x00ADFE50`)
- `0x00AE1A9C` → [PopBatteryQueryEstimatedTime](../A9/PopBatteryQueryEstimatedTime_function_00A98E80.md) (function, `0x00A98E80`)
- `0x00AE1AEF` → [DbgPrintEx](../../text/35/DbgPrintEx_function_00359290.md) (function, `0x00359290`)
- `0x00AE1BAE` → [PopPrepareIoctl](../A7/PopPrepareIoctl_function_00A74A98.md) (function, `0x00A74A98`)
- `0x00AE1BBB` → [IoSynchronousCallDriver](../../text/48/IoSynchronousCallDriver_function_00484050.md) (function, `0x00484050`)
- `0x00AE1BCF` → [PopPowerAdapterTraceFailure](../76/PopPowerAdapterTraceFailure_function_007682B8.md) (function, `0x007682B8`)
- `0x00AE1C1D` → [PopPowerAdapterQueryStatus](../76/PopPowerAdapterQueryStatus_function_00767C44.md) (function, `0x00767C44`)
- `0x00AE1C9D` → [PopPowerAdapterPublishRecState](../76/PopPowerAdapterPublishRecState_function_007679CC.md) (function, `0x007679CC`)
- `0x00AE1CAB` → [PopBatteryUpdateCompositeInformation](../90/PopBatteryUpdateCompositeInformation_function_0090FDD0.md) (function, `0x0090FDD0`)
- `0x00AE1D09` → [KiSetTimerEx](../../text/23/KiSetTimerEx_function_00232CB0.md) (function, `0x00232CB0`)
- `0x00AE1D18` → [KeCancelTimer](../../text/23/KeCancelTimer_function_002327E0.md) (function, `0x002327E0`)
- `0x00AE1DCD` → [KiQueryUnbiasedInterruptTime](../../text/42/KiQueryUnbiasedInterruptTime_function_0042D180.md) (function, `0x0042D180`)
- `0x00AE1F5F` → [Feature_BatteryChargeLimitV2Support__private_IsEnabledDeviceUsageNoInline](../../text/5D/Feature_BatteryChargeLimitV2Support__private_IsEnabledDeviceUsageNoInline_function_005D9484.md) (function, `0x005D9484`)
- `0x00AE2055` → [PopBatteryQueryEstimatedTime](../A9/PopBatteryQueryEstimatedTime_function_00A98E80.md) (function, `0x00A98E80`)
- `0x00AE2085` → [PopEstimateChargeTime](../A9/PopEstimateChargeTime_function_00A99264.md) (function, `0x00A99264`)
- `0x00AE2100` → [ZwUpdateWnfStateData](../../text/6B/ZwUpdateWnfStateData_function_006B0D10.md) (function, `0x006B0D10`)
- `0x00AE2116` → [PopSetPowerSettingValueAcDc](../91/PopSetPowerSettingValueAcDc_function_00914D6C.md) (function, `0x00914D6C`)
- `0x00AE213C` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (function, `0x0042EAA0`)
- `0x00AE21BC` → [tlgCreate1Sz_char](../../text/42/tlgCreate1Sz_char_function_00427304.md) (function, `0x00427304`)
- `0x00AE21D7` → [tlgCreate1Sz_char](../../text/42/tlgCreate1Sz_char_function_00427304.md) (function, `0x00427304`)
- `0x00AE21F2` → [tlgCreate1Sz_char](../../text/42/tlgCreate1Sz_char_function_00427304.md) (function, `0x00427304`)
- `0x00AE220D` → [tlgCreate1Sz_char](../../text/42/tlgCreate1Sz_char_function_00427304.md) (function, `0x00427304`)
- `0x00AE2258` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x00AE225D` → [Feature_BatteryChargeLimitV2Support__private_IsEnabledDeviceUsageNoInline](../../text/5D/Feature_BatteryChargeLimitV2Support__private_IsEnabledDeviceUsageNoInline_function_005D9484.md) (function, `0x005D9484`)
- `0x00AE2282` → [PopBatteryPublishChargeLimitStatus](../76/PopBatteryPublishChargeLimitStatus_function_00766BBC.md) (function, `0x00766BBC`)
- `0x00AE22CE` → [PopAcquireRwLockExclusive](../../text/43/PopAcquireRwLockExclusive_function_00430B44.md) (function, `0x00430B44`)
- `0x00AE22E6` → [PopReleaseRwLock](../../text/2D/PopReleaseRwLock_function_002DFBBC.md) (function, `0x002DFBBC`)
- `0x00AE2310` → [PopBatteryApplyCompositeState](PopBatteryApplyCompositeState_function_00AE0CD0.md) (function, `0x00AE0CD0`)
- `0x00AE2331` → [PopEvaluateWeakChargerState](PopEvaluateWeakChargerState_function_00AE2DA0.md) (function, `0x00AE2DA0`)
- `0x00AE2371` → [ExfUnblockPushLock](../../text/2A/ExfUnblockPushLock_function_002A3FE0.md) (function, `0x002A3FE0`)
- `0x00AE23C0` → [PopBatteryQueryStatus](PopBatteryQueryStatus_function_00AE1450.md) (function, `0x00AE1450`)
- `0x00AE23E9` → [PopPowerAdapterQueryStatus](../76/PopPowerAdapterQueryStatus_function_00767C44.md) (function, `0x00767C44`)
- `0x00AE241C` → [ZwUpdateWnfStateData](../../text/6B/ZwUpdateWnfStateData_function_006B0D10.md) (function, `0x006B0D10`)
- `0x00AE242A` → [PopBatteryEstimatesSpoiled](../A9/PopBatteryEstimatesSpoiled_function_00A993F0.md) (function, `0x00A993F0`)
- `0x00AE2460` → [ZwUpdateWnfStateData](../../text/6B/ZwUpdateWnfStateData_function_006B0D10.md) (function, `0x006B0D10`)
- `0x00AE2552` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x00AE25D8` → [ZwUpdateWnfStateData](../../text/6B/ZwUpdateWnfStateData_function_006B0D10.md) (function, `0x006B0D10`)
- `0x00AE25DF` → [Feature_BatteryChargeLimitV2Support__private_IsEnabledDeviceUsageNoInline](../../text/5D/Feature_BatteryChargeLimitV2Support__private_IsEnabledDeviceUsageNoInline_function_005D9484.md) (function, `0x005D9484`)
- `0x00AE260A` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (function, `0x0042EAA0`)
- `0x00AE265D` → [tlgCreate1Sz_char](../../text/42/tlgCreate1Sz_char_function_00427304.md) (function, `0x00427304`)
- `0x00AE267F` → [tlgCreate1Sz_char](../../text/42/tlgCreate1Sz_char_function_00427304.md) (function, `0x00427304`)
- `0x00AE2699` → [tlgCreate1Sz_char](../../text/42/tlgCreate1Sz_char_function_00427304.md) (function, `0x00427304`)
- `0x00AE26B3` → [tlgCreate1Sz_char](../../text/42/tlgCreate1Sz_char_function_00427304.md) (function, `0x00427304`)
- `0x00AE26D2` → [tlgCreate1Sz_char](../../text/42/tlgCreate1Sz_char_function_00427304.md) (function, `0x00427304`)
- `0x00AE26ED` → [tlgCreate1Sz_char](../../text/42/tlgCreate1Sz_char_function_00427304.md) (function, `0x00427304`)
- `0x00AE2708` → [tlgCreate1Sz_char](../../text/42/tlgCreate1Sz_char_function_00427304.md) (function, `0x00427304`)
- `0x00AE2723` → [tlgCreate1Sz_char](../../text/42/tlgCreate1Sz_char_function_00427304.md) (function, `0x00427304`)
- `0x00AE2741` → [tlgCreate1Sz_char](../../text/42/tlgCreate1Sz_char_function_00427304.md) (function, `0x00427304`)
- `0x00AE288F` → [tlgCreate1Sz_char](../../text/42/tlgCreate1Sz_char_function_00427304.md) (function, `0x00427304`)
- `0x00AE2901` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (function, `0x0042EAA0`)
- `0x00AE2954` → [tlgCreate1Sz_char](../../text/42/tlgCreate1Sz_char_function_00427304.md) (function, `0x00427304`)
- `0x00AE2976` → [tlgCreate1Sz_char](../../text/42/tlgCreate1Sz_char_function_00427304.md) (function, `0x00427304`)
- `0x00AE2990` → [tlgCreate1Sz_char](../../text/42/tlgCreate1Sz_char_function_00427304.md) (function, `0x00427304`)
- `0x00AE29AA` → [tlgCreate1Sz_char](../../text/42/tlgCreate1Sz_char_function_00427304.md) (function, `0x00427304`)
- `0x00AE29C9` → [tlgCreate1Sz_char](../../text/42/tlgCreate1Sz_char_function_00427304.md) (function, `0x00427304`)
- `0x00AE29E4` → [tlgCreate1Sz_char](../../text/42/tlgCreate1Sz_char_function_00427304.md) (function, `0x00427304`)
- `0x00AE29FF` → [tlgCreate1Sz_char](../../text/42/tlgCreate1Sz_char_function_00427304.md) (function, `0x00427304`)
- `0x00AE2A1A` → [tlgCreate1Sz_char](../../text/42/tlgCreate1Sz_char_function_00427304.md) (function, `0x00427304`)
- `0x00AE2A38` → [tlgCreate1Sz_char](../../text/42/tlgCreate1Sz_char_function_00427304.md) (function, `0x00427304`)
- `0x00AE2A56` → [tlgCreate1Sz_char](../../text/42/tlgCreate1Sz_char_function_00427304.md) (function, `0x00427304`)
- `0x00AE2BA2` → [tlgCreate1Sz_char](../../text/42/tlgCreate1Sz_char_function_00427304.md) (function, `0x00427304`)
- `0x00AE2C0B` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x00AE2C53` → [ZwUpdateWnfStateData](../../text/6B/ZwUpdateWnfStateData_function_006B0D10.md) (function, `0x006B0D10`)
- `0x00AE2C85` → [ZwUpdateWnfStateData](../../text/6B/ZwUpdateWnfStateData_function_006B0D10.md) (function, `0x006B0D10`)
- `0x00AE2CD6` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x00AE2CE2` → [PopReleaseRwLock](../../text/2D/PopReleaseRwLock_function_002DFBBC.md) (function, `0x002DFBBC`)
- `0x00AE2CEE` → [PopReleaseRwLock](../../text/2D/PopReleaseRwLock_function_002DFBBC.md) (function, `0x002DFBBC`)
- `0x00AE2CFD` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00AE1683` → RVA `0x00E0A740` (`.data`; read)
- `0x00AE1697` → RVA `0x00F0C900` (`.data`; read)
- `0x00AE16DB` → RVA `0x00F0C020` (`.data`; read)
- `0x00AE1715` → RVA `0x0001C140` (`.rdata`; read)
- `0x00AE175F` → RVA `0x00F0C2D8` (`.data`; read)
- `0x00AE1766` → RVA `0x00F0C050` (`.data`; read)
- `0x00AE181F` → RVA `0x00F09058` (`.data`; read/write)
- `0x00AE18FD` → RVA `0x00F0C034` (`.data`; read/write)
- `0x00AE1903` → RVA `0x00F0C0B4` (`.data`; read/write)
- `0x00AE190A` → RVA `0x00F0C038` (`.data`; write)
- `0x00AE1936` → RVA `0x00F0C040` (`.data`; read)
- `0x00AE19EE` → RVA `0x00F0C2C1` (`.data`; read)
- `0x00AE19FB` → RVA `0x00E0B828` (`.data`; read)
- `0x00AE1AA7` → RVA `0x00B02790` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AE1B38` → RVA `0x00E678B0` (`.data`; read)
- `0x00AE1CB3` → RVA `0x00E678B8` (`.data`; write)
- `0x00AE1CC8` → RVA `0x00E678A4` (`.data`; read)
- `0x00AE1CCE` → RVA `0x00F090A0` (`.data`; read)
- `0x00AE1CEF` → RVA `0x00E0B810` (`.data`; write)
- `0x00AE1CFD` → RVA `0x00F09060` (`.data`; read)
- `0x00AE1D10` → RVA `0x00E0B810` (`.data`; read/write)
- `0x00AE1D54` → RVA `0x00F0C034` (`.data`; read)
- `0x00AE1F93` → RVA `0x00F0C084` (`.data`; read)
- `0x00AE1FF4` → RVA `0x00E678B4` (`.data`; read)
- `0x00AE20B4` → RVA `0x00F0C060` (`.data`; read)
- `0x00AE20ED` → RVA `0x00020BE8` (`.rdata`; read)
- `0x00AE210F` → RVA `0x00029748` (`.rdata`; read)
- `0x00AE211B` → RVA `0x00E07748` (`.data`; read)
- `0x00AE2159` → RVA `0x00B02780` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AE216D` → RVA `0x00B028B0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AE21C5` → RVA `0x00B02820` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AE21E0` → RVA `0x00B02810` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AE21FB` → RVA `0x00B02A30` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AE2225` → RVA `0x0004DB5A` (`.rdata`; read)
- `0x00AE2278` → RVA `0x00F0C088` (`.data`; read)
- `0x00AE2297` → RVA `0x00E0B828` (`.data`; read/write)
- `0x00AE22BF` → RVA `0x00F0C21C` (`.data`; read)
- `0x00AE22C7` → RVA `0x00F09010` (`.data`; read)
- `0x00AE22DA` → RVA `0x00F0C21C` (`.data`; write)
- `0x00AE22E0` → RVA `0x00F09040` (`.data`; write)
- `0x00AE2353` → RVA `0x00F0C228` (`.data`; write)
- `0x00AE235F` → RVA `0x00F0C230` (`.data`; read)
- `0x00AE237B` → RVA `0x00F09058` (`.data`; read)
- `0x00AE23EE` → RVA `0x00E678C0` (`.data`; read)
- `0x00AE240A` → RVA `0x00020AC8` (`.rdata`; read)
- `0x00AE244E` → RVA `0x00020A58` (`.rdata`; read)
- `0x00AE247E` → RVA `0x0004E05B` (`.rdata`; read)
- `0x00AE2565` → RVA `0x00F0C090` (`.data`; read)
- `0x00AE256C` → RVA `0x00F0C0B0` (`.data`; read)
- `0x00AE2579` → RVA `0x00F0C0A0` (`.data`; read)
- `0x00AE2586` → RVA `0x00020980` (`.rdata`; read)
- `0x00AE258D` → RVA `0x00F0C030` (`.data`; read)
- `0x00AE262A` → RVA `0x00B02A20` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AE263F` → RVA `0x00B02A60` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AE2666` → RVA `0x00B02A40` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AE2687` → RVA `0x00B02A90` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AE26A1` → RVA `0x00B02A70` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AE26BD` → RVA `0x00B02AE0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AE26DB` → RVA `0x00B02AB0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AE26F6` → RVA `0x00B02990` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AE2711` → RVA `0x00B02970` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AE2728` → RVA `0x00F0C2C0` (`.data`; reference)
- `0x00AE272F` → RVA `0x00B029D0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AE2757` → RVA `0x00F0C064` (`.data`; read)
- `0x00AE27AB` → RVA `0x00B02A00` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AE27F3` → RVA `0x00F0C068` (`.data`; read)
- `0x00AE2807` → RVA `0x00F0C06C` (`.data`; read)
- `0x00AE283A` → RVA `0x00B029F0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AE2894` → RVA `0x00F0C09C` (`.data`; read)
- `0x00AE28A5` → RVA `0x0004DE3E` (`.rdata`; read)
- `0x00AE2A3D` → RVA `0x00F0C2C1` (`.data`; reference)
- `0x00AE2A44` → RVA `0x00B029B0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AE2BB9` → RVA `0x0004DC09` (`.rdata`; read)
- `0x00AE2C6A` → RVA `0x00020888` (`.rdata`; read)
- `0x00AE2C97` → RVA `0x0004D81C` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **66**
  - `0x00AE16D6` → [PopAcquireRwLockShared](../../text/2D/PopAcquireRwLockShared_function_002D9A40.md) (`PAGE` → `.text`)
  - `0x00AE16E2` → [PopAcquireRwLockExclusive](../../text/43/PopAcquireRwLockExclusive_function_00430B44.md) (`PAGE` → `.text`)
  - `0x00AE171C` → [ZwQueryWnfStateData](../../text/6A/ZwQueryWnfStateData_function_006AFEF0.md) (`PAGE` → `.text`)
  - `0x00AE177F` → [IoCancelIrp](../../text/27/IoCancelIrp_function_002720E0.md) (`PAGE` → `.text`)
  - `0x00AE17A3` → [IoCancelIrp](../../text/27/IoCancelIrp_function_002720E0.md) (`PAGE` → `.text`)
  - `0x00AE17C2` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (`PAGE` → `.text`)
  - `0x00AE17F3` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (`PAGE` → `.text`)
  - `0x00AE1848` → [PopAcquirePolicyLock](../../pagelk/B7/PopAcquirePolicyLock_function_00B783C0.md) (`PAGE` → `PAGELK`)
  - `0x00AE1854` → [PopReleasePolicyLock](../../pagelk/B7/PopReleasePolicyLock_function_00B78410.md) (`PAGE` → `PAGELK`)
  - `0x00AE189E` → [Feature_BatteryChargeLimitV2Support__private_IsEnabledDeviceUsageNoInline](../../text/5D/Feature_BatteryChargeLimitV2Support__private_IsEnabledDeviceUsageNoInline_function_005D9484.md) (`PAGE` → `.text`)
  - `0x00AE195D` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (`PAGE` → `.text`)
  - `0x00AE19DB` → [PopBatteryQueueWork](../../text/4A/PopBatteryQueueWork_function_004AE3DC.md) (`PAGE` → `.text`)
  - `0x00AE19E5` → [Feature_BatteryChargeLimitV2Support__private_IsEnabledDeviceUsageNoInline](../../text/5D/Feature_BatteryChargeLimitV2Support__private_IsEnabledDeviceUsageNoInline_function_005D9484.md) (`PAGE` → `.text`)
  - `0x00AE1A3D` → [PopBatterySetChargeLimitControl](../../text/5D/PopBatterySetChargeLimitControl_function_005D94D8.md) (`PAGE` → `.text`)
  - `0x00AE1AEF` → [DbgPrintEx](../../text/35/DbgPrintEx_function_00359290.md) (`PAGE` → `.text`)
  - `0x00AE1BBB` → [IoSynchronousCallDriver](../../text/48/IoSynchronousCallDriver_function_00484050.md) (`PAGE` → `.text`)
  - `0x00AE1D09` → [KiSetTimerEx](../../text/23/KiSetTimerEx_function_00232CB0.md) (`PAGE` → `.text`)
  - `0x00AE1D18` → [KeCancelTimer](../../text/23/KeCancelTimer_function_002327E0.md) (`PAGE` → `.text`)
  - `0x00AE1DCD` → [KiQueryUnbiasedInterruptTime](../../text/42/KiQueryUnbiasedInterruptTime_function_0042D180.md) (`PAGE` → `.text`)
  - `0x00AE1F5F` → [Feature_BatteryChargeLimitV2Support__private_IsEnabledDeviceUsageNoInline](../../text/5D/Feature_BatteryChargeLimitV2Support__private_IsEnabledDeviceUsageNoInline_function_005D9484.md) (`PAGE` → `.text`)
  - `0x00AE2100` → [ZwUpdateWnfStateData](../../text/6B/ZwUpdateWnfStateData_function_006B0D10.md) (`PAGE` → `.text`)
  - `0x00AE213C` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (`PAGE` → `.text`)
  - `0x00AE21BC` → [tlgCreate1Sz_char](../../text/42/tlgCreate1Sz_char_function_00427304.md) (`PAGE` → `.text`)
  - `0x00AE21D7` → [tlgCreate1Sz_char](../../text/42/tlgCreate1Sz_char_function_00427304.md) (`PAGE` → `.text`)
  - `0x00AE21F2` → [tlgCreate1Sz_char](../../text/42/tlgCreate1Sz_char_function_00427304.md) (`PAGE` → `.text`)
  - `0x00AE220D` → [tlgCreate1Sz_char](../../text/42/tlgCreate1Sz_char_function_00427304.md) (`PAGE` → `.text`)
  - `0x00AE2258` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (`PAGE` → `.text`)
  - `0x00AE225D` → [Feature_BatteryChargeLimitV2Support__private_IsEnabledDeviceUsageNoInline](../../text/5D/Feature_BatteryChargeLimitV2Support__private_IsEnabledDeviceUsageNoInline_function_005D9484.md) (`PAGE` → `.text`)
  - `0x00AE22CE` → [PopAcquireRwLockExclusive](../../text/43/PopAcquireRwLockExclusive_function_00430B44.md) (`PAGE` → `.text`)
  - `0x00AE22E6` → [PopReleaseRwLock](../../text/2D/PopReleaseRwLock_function_002DFBBC.md) (`PAGE` → `.text`)
  - `0x00AE2371` → [ExfUnblockPushLock](../../text/2A/ExfUnblockPushLock_function_002A3FE0.md) (`PAGE` → `.text`)
  - `0x00AE241C` → [ZwUpdateWnfStateData](../../text/6B/ZwUpdateWnfStateData_function_006B0D10.md) (`PAGE` → `.text`)
  - `0x00AE2460` → [ZwUpdateWnfStateData](../../text/6B/ZwUpdateWnfStateData_function_006B0D10.md) (`PAGE` → `.text`)
  - `0x00AE2552` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (`PAGE` → `.text`)
  - `0x00AE25D8` → [ZwUpdateWnfStateData](../../text/6B/ZwUpdateWnfStateData_function_006B0D10.md) (`PAGE` → `.text`)
  - `0x00AE25DF` → [Feature_BatteryChargeLimitV2Support__private_IsEnabledDeviceUsageNoInline](../../text/5D/Feature_BatteryChargeLimitV2Support__private_IsEnabledDeviceUsageNoInline_function_005D9484.md) (`PAGE` → `.text`)
  - `0x00AE260A` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (`PAGE` → `.text`)
  - `0x00AE265D` → [tlgCreate1Sz_char](../../text/42/tlgCreate1Sz_char_function_00427304.md) (`PAGE` → `.text`)
  - `0x00AE267F` → [tlgCreate1Sz_char](../../text/42/tlgCreate1Sz_char_function_00427304.md) (`PAGE` → `.text`)
  - `0x00AE2699` → [tlgCreate1Sz_char](../../text/42/tlgCreate1Sz_char_function_00427304.md) (`PAGE` → `.text`)
  - `0x00AE26B3` → [tlgCreate1Sz_char](../../text/42/tlgCreate1Sz_char_function_00427304.md) (`PAGE` → `.text`)
  - `0x00AE26D2` → [tlgCreate1Sz_char](../../text/42/tlgCreate1Sz_char_function_00427304.md) (`PAGE` → `.text`)
  - `0x00AE26ED` → [tlgCreate1Sz_char](../../text/42/tlgCreate1Sz_char_function_00427304.md) (`PAGE` → `.text`)
  - `0x00AE2708` → [tlgCreate1Sz_char](../../text/42/tlgCreate1Sz_char_function_00427304.md) (`PAGE` → `.text`)
  - `0x00AE2723` → [tlgCreate1Sz_char](../../text/42/tlgCreate1Sz_char_function_00427304.md) (`PAGE` → `.text`)
  - `0x00AE2741` → [tlgCreate1Sz_char](../../text/42/tlgCreate1Sz_char_function_00427304.md) (`PAGE` → `.text`)
  - `0x00AE288F` → [tlgCreate1Sz_char](../../text/42/tlgCreate1Sz_char_function_00427304.md) (`PAGE` → `.text`)
  - `0x00AE2901` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (`PAGE` → `.text`)
  - `0x00AE2954` → [tlgCreate1Sz_char](../../text/42/tlgCreate1Sz_char_function_00427304.md) (`PAGE` → `.text`)
  - `0x00AE2976` → [tlgCreate1Sz_char](../../text/42/tlgCreate1Sz_char_function_00427304.md) (`PAGE` → `.text`)
  - `0x00AE2990` → [tlgCreate1Sz_char](../../text/42/tlgCreate1Sz_char_function_00427304.md) (`PAGE` → `.text`)
  - `0x00AE29AA` → [tlgCreate1Sz_char](../../text/42/tlgCreate1Sz_char_function_00427304.md) (`PAGE` → `.text`)
  - `0x00AE29C9` → [tlgCreate1Sz_char](../../text/42/tlgCreate1Sz_char_function_00427304.md) (`PAGE` → `.text`)
  - `0x00AE29E4` → [tlgCreate1Sz_char](../../text/42/tlgCreate1Sz_char_function_00427304.md) (`PAGE` → `.text`)
  - `0x00AE29FF` → [tlgCreate1Sz_char](../../text/42/tlgCreate1Sz_char_function_00427304.md) (`PAGE` → `.text`)
  - `0x00AE2A1A` → [tlgCreate1Sz_char](../../text/42/tlgCreate1Sz_char_function_00427304.md) (`PAGE` → `.text`)
  - `0x00AE2A38` → [tlgCreate1Sz_char](../../text/42/tlgCreate1Sz_char_function_00427304.md) (`PAGE` → `.text`)
  - `0x00AE2A56` → [tlgCreate1Sz_char](../../text/42/tlgCreate1Sz_char_function_00427304.md) (`PAGE` → `.text`)
  - `0x00AE2BA2` → [tlgCreate1Sz_char](../../text/42/tlgCreate1Sz_char_function_00427304.md) (`PAGE` → `.text`)
  - `0x00AE2C0B` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (`PAGE` → `.text`)
  - `0x00AE2C53` → [ZwUpdateWnfStateData](../../text/6B/ZwUpdateWnfStateData_function_006B0D10.md) (`PAGE` → `.text`)
  - `0x00AE2C85` → [ZwUpdateWnfStateData](../../text/6B/ZwUpdateWnfStateData_function_006B0D10.md) (`PAGE` → `.text`)
  - `0x00AE2CD6` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (`PAGE` → `.text`)
  - `0x00AE2CE2` → [PopReleaseRwLock](../../text/2D/PopReleaseRwLock_function_002DFBBC.md) (`PAGE` → `.text`)
  - `0x00AE2CEE` → [PopReleaseRwLock](../../text/2D/PopReleaseRwLock_function_002DFBBC.md) (`PAGE` → `.text`)
  - `0x00AE2CFD` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AE1650  48 8B C4                        mov rax, rsp
00AE1653  48 89 58 08                     mov qword ptr [rax + 8], rbx
00AE1657  48 89 70 10                     mov qword ptr [rax + 0x10], rsi
00AE165B  48 89 78 18                     mov qword ptr [rax + 0x18], rdi
00AE165F  55                              push rbp
00AE1660  41 54                           push r12
00AE1662  41 55                           push r13
00AE1664  41 56                           push r14
00AE1666  41 57                           push r15
00AE1668  48 8D A8 B8 FB FF FF            lea rbp, [rax - 0x448]
00AE166F  48 81 EC 20 05 00 00            sub rsp, 0x520
00AE1676  0F 29 70 C8                     movaps xmmword ptr [rax - 0x38], xmm6
00AE167A  0F 29 78 B8                     movaps xmmword ptr [rax - 0x48], xmm7
00AE167E  44 0F 29 40 A8                  movaps xmmword ptr [rax - 0x58], xmm8
00AE1683  48 8B 05 B6 90 32 00            mov rax, qword ptr [rip + 0x3290b6]
00AE168A  48 33 C4                        xor rax, rsp
00AE168D  48 89 85 E0 03 00 00            mov qword ptr [rbp + 0x3e0], rax
00AE1694  45 33 E4                        xor r12d, r12d
00AE1697  48 8D 0D 62 B2 42 00            lea rcx, [rip + 0x42b262]
00AE169E  0F 57 C0                        xorps xmm0, xmm0
00AE16A1  4C 89 65 B8                     mov qword ptr [rbp - 0x48], r12
00AE16A5  33 C0                           xor eax, eax
00AE16A7  4C 89 65 C0                     mov qword ptr [rbp - 0x40], r12
00AE16AB  4C 89 65 E0                     mov qword ptr [rbp - 0x20], r12
00AE16AF  44 88 64 24 50                  mov byte ptr [rsp + 0x50], r12b
00AE16B4  0F 11 85 C8 00 00 00            movups xmmword ptr [rbp + 0xc8], xmm0
00AE16BB  48 89 85 F8 00 00 00            mov qword ptr [rbp + 0xf8], rax
00AE16C2  0F 11 85 D8 00 00 00            movups xmmword ptr [rbp + 0xd8], xmm0
00AE16C9  89 85 00 01 00 00               mov dword ptr [rbp + 0x100], eax
00AE16CF  0F 11 85 E8 00 00 00            movups xmmword ptr [rbp + 0xe8], xmm0
00AE16D6  E8 65 83 7F FF                  call 0x1402d9a40
00AE16DB  48 8D 0D 3E A9 42 00            lea rcx, [rip + 0x42a93e]
00AE16E2  E8 5D F4 94 FF                  call 0x140430b44
00AE16E7  48 8D 44 24 58                  lea rax, [rsp + 0x58]
00AE16EC  4C 89 65 88                     mov qword ptr [rbp - 0x78], r12
00AE16F0  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE16F5  4C 8D 4C 24 64                  lea r9, [rsp + 0x64]
00AE16FA  48 8D 45 88                     lea rax, [rbp - 0x78]
00AE16FE  44 89 64 24 64                  mov dword ptr [rsp + 0x64], r12d
00AE1703  45 33 C0                        xor r8d, r8d
00AE1706  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AE170B  33 D2                           xor edx, edx
00AE170D  C7 44 24 58 08 00 00 00         mov dword ptr [rsp + 0x58], 8
00AE1715  48 8D 0D 24 AA 53 FF            lea rcx, [rip - 0xac55dc]
00AE171C  E8 CF E7 BC FF                  call 0x1406afef0
00AE1721  45 8D 7C 24 01                  lea r15d, [r12 + 1]
00AE1726  3D 9A 00 00 C0                  cmp eax, 0xc000009a
00AE172B  74 2D                           je 0x140ae175a
00AE172D  3D 89 01 00 C0                  cmp eax, 0xc0000189
00AE1732  74 26                           je 0x140ae175a
00AE1734  85 C0                           test eax, eax
00AE1736  75 1B                           jne 0x140ae1753
00AE1738  83 7C 24 58 08                  cmp dword ptr [rsp + 0x58], 8
00AE173D  75 14                           jne 0x140ae1753
00AE173F  48 8B 45 88                     mov rax, qword ptr [rbp - 0x78]
00AE1743  48 F7 D8                        neg rax
00AE1746  1B C0                           sbb eax, eax
00AE1748  F7 D8                           neg eax
00AE174A  83 C0 02                        add eax, 2
00AE174D  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
00AE1751  EB 0C                           jmp 0x140ae175f
00AE1753  44 89 7C 24 60                  mov dword ptr [rsp + 0x60], r15d
00AE1758  EB 05                           jmp 0x140ae175f
00AE175A  44 89 64 24 60                  mov dword ptr [rsp + 0x60], r12d
00AE175F  48 8B 1D 72 AB 42 00            mov rbx, qword ptr [rip + 0x42ab72]
00AE1766  48 8D 35 E3 A8 42 00            lea rsi, [rip + 0x42a8e3]
00AE176D  48 8B 3D DC A8 42 00            mov rdi, qword ptr [rip + 0x42a8dc]
00AE1774  48 89 5C 24 70                  mov qword ptr [rsp + 0x70], rbx
00AE1779  EB 0C                           jmp 0x140ae1787
00AE177B  48 8B 4F F8                     mov rcx, qword ptr [rdi - 8]
00AE177F  E8 5C 09 79 FF                  call 0x1402720e0
00AE1784  48 8B 3F                        mov rdi, qword ptr [rdi]
00AE1787  48 3B FE                        cmp rdi, rsi
00AE178A  75 EF                           jne 0x140ae177b
00AE178C  48 85 DB                        test rbx, rbx
00AE178F  74 17                           je 0x140ae17a8
00AE1791  8B 83 80 00 00 00               mov eax, dword ptr [rbx + 0x80]
00AE1797  41 2B C7                        sub eax, r15d
00AE179A  41 3B C7                        cmp eax, r15d
00AE179D  77 09                           ja 0x140ae17a8
00AE179F  48 8B 4B 38                     mov rcx, qword ptr [rbx + 0x38]
00AE17A3  E8 38 09 79 FF                  call 0x1402720e0
00AE17A8  48 8B 3D A1 A8 42 00            mov rdi, qword ptr [rip + 0x42a8a1]
00AE17AF  EB 19                           jmp 0x140ae17ca
00AE17B1  48 8D 4F 10                     lea rcx, [rdi + 0x10]
00AE17B5  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
00AE17BA  45 33 C9                        xor r9d, r9d
00AE17BD  45 33 C0                        xor r8d, r8d
00AE17C0  33 D2                           xor edx, edx
00AE17C2  E8 E9 CE 72 FF                  call 0x14020e6b0
00AE17C7  48 8B 3F                        mov rdi, qword ptr [rdi]
00AE17CA  48 3B FE                        cmp rdi, rsi
00AE17CD  75 E2                           jne 0x140ae17b1
00AE17CF  48 85 DB                        test rbx, rbx
00AE17D2  74 24                           je 0x140ae17f8
00AE17D4  8B 83 80 00 00 00               mov eax, dword ptr [rbx + 0x80]
00AE17DA  41 2B C7                        sub eax, r15d
00AE17DD  41 3B C7                        cmp eax, r15d
00AE17E0  77 16                           ja 0x140ae17f8
00AE17E2  48 8D 4B 68                     lea rcx, [rbx + 0x68]
00AE17E6  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
00AE17EB  45 33 C9                        xor r9d, r9d
00AE17EE  45 33 C0                        xor r8d, r8d
00AE17F1  33 D2                           xor edx, edx
00AE17F3  E8 B8 CE 72 FF                  call 0x14020e6b0
00AE17F8  41 8A F4                        mov sil, r12b
00AE17FB  44 88 64 24 51                  mov byte ptr [rsp + 0x51], r12b
00AE1800  89 74 24 54                     mov dword ptr [rsp + 0x54], esi
00AE1804  41 8A C4                        mov al, r12b
00AE1807  45 8A F4                        mov r14b, r12b
00AE180A  0F B6 C0                        movzx eax, al
00AE180D  41 8A FC                        mov dil, r12b
00AE1810  44 89 74 24 68                  mov dword ptr [rsp + 0x68], r14d
00AE1815  41 BD 00 00 00 80               mov r13d, 0x80000000
00AE181B  89 7C 24 6C                     mov dword ptr [rsp + 0x6c], edi
00AE181F  44 87 2D 32 78 42 00            xchg dword ptr [rip + 0x427832], r13d
00AE1826  45 8B E5                        mov r12d, r13d
00AE1829  44 89 6D 84                     mov dword ptr [rbp - 0x7c], r13d
00AE182D  41 D1 EC                        shr r12d, 1
00AE1830  B9 10 00 00 00                  mov ecx, 0x10
00AE1835  45 22 E7                        and r12b, r15b
00AE1838  41 F6 C5 08                     test r13b, 8
00AE183C  41 0F 45 C7                     cmovne eax, r15d
00AE1840  89 45 80                        mov dword ptr [rbp - 0x80], eax
00AE1843  44 84 E9                        test cl, r13b
00AE1846  74 11                           je 0x140ae1859
00AE1848  E8 73 6B 09 00                  call 0x140b783c0
00AE184D  B1 80                           mov cl, 0x80
00AE184F  E8 A4 6B C8 FF                  call 0x1407683f8
00AE1854  E8 B7 6B 09 00                  call 0x140b78410
00AE1859  41 0F BA E5 06                  bt r13d, 6
00AE185E  0F 92 44 24 5D                  setb byte ptr [rsp + 0x5d]
00AE1863  33 F6                           xor esi, esi
00AE1865  41 0F BA E5 06                  bt r13d, 6
00AE186A  8B CE                           mov ecx, esi
00AE186C  0F 92 C1                        setb cl
00AE186F  89 4D B0                        mov dword ptr [rbp - 0x50], ecx
00AE1872  45 84 ED                        test r13b, r13b
00AE1875  79 27                           jns 0x140ae189e
00AE1877  48 85 DB                        test rbx, rbx
00AE187A  74 22                           je 0x140ae189e
00AE187C  8B 83 80 00 00 00               mov eax, dword ptr [rbx + 0x80]
00AE1882  41 2B C7                        sub eax, r15d
00AE1885  41 3B C7                        cmp eax, r15d
00AE1888  77 14                           ja 0x140ae189e
00AE188A  44 84 BB 8C 00 00 00            test byte ptr [rbx + 0x8c], r15b
00AE1891  45 0F B6 F6                     movzx r14d, r14b
00AE1895  45 0F 45 F7                     cmovne r14d, r15d
00AE1899  44 89 74 24 68                  mov dword ptr [rsp + 0x68], r14d
00AE189E  E8 E1 7B AF FF                  call 0x1405d9484
00AE18A3  85 C0                           test eax, eax
00AE18A5  74 11                           je 0x140ae18b8
00AE18A7  41 0F BA E5 08                  bt r13d, 8
00AE18AC  40 0F B6 FF                     movzx edi, dil
00AE18B0  41 0F 42 FF                     cmovb edi, r15d
00AE18B4  89 7C 24 6C                     mov dword ptr [rsp + 0x6c], edi
00AE18B8  48 8B 05 91 A7 42 00            mov rax, qword ptr [rip + 0x42a791]
00AE18BF  48 8D 0D 8A A7 42 00            lea rcx, [rip + 0x42a78a]
00AE18C6  48 3B C1                        cmp rax, rcx
00AE18C9  74 6B                           je 0x140ae1936
00AE18CB  48 8B 38                        mov rdi, qword ptr [rax]
00AE18CE  48 8D 70 C0                     lea rsi, [rax - 0x40]
00AE18D2  83 7E 68 02                     cmp dword ptr [rsi + 0x68], 2
00AE18D6  75 54                           jne 0x140ae192c
00AE18D8  48 39 47 08                     cmp qword ptr [rdi + 8], rax
00AE18DC  0F 85 B7 0A 00 00               jne 0x140ae2399
00AE18E2  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
00AE18E6  48 39 01                        cmp qword ptr [rcx], rax
00AE18E9  0F 85 AA 0A 00 00               jne 0x140ae2399
00AE18EF  48 89 39                        mov qword ptr [rcx], rdi
00AE18F2  48 89 4F 08                     mov qword ptr [rdi + 8], rcx
00AE18F6  48 8B CE                        mov rcx, rsi
00AE18F9  48 83 20 00                     and qword ptr [rax], 0
00AE18FD  FF 0D 31 A7 42 00               dec dword ptr [rip + 0x42a731]
00AE1903  44 01 3D AA A7 42 00            add dword ptr [rip + 0x42a7aa], r15d
00AE190A  44 88 3D 27 A7 42 00            mov byte ptr [rip + 0x42a727], r15b
00AE1911  E8 06 45 FE FF                  call 0x140ac5e1c
00AE1916  85 C0                           test eax, eax
00AE1918  79 08                           jns 0x140ae1922
00AE191A  48 8B CE                        mov rcx, rsi
00AE191D  E8 D6 12 FF FF                  call 0x140ad2bf8
00AE1922  45 8A E7                        mov r12b, r15b
00AE1925  48 8D 0D 24 A7 42 00            lea rcx, [rip + 0x42a724]
00AE192C  48 8B C7                        mov rax, rdi
00AE192F  48 3B F9                        cmp rdi, rcx
00AE1932  75 97                           jne 0x140ae18cb
00AE1934  33 F6                           xor esi, esi
00AE1936  48 8B 3D 03 A7 42 00            mov rdi, qword ptr [rip + 0x42a703]
00AE193D  48 8D 05 FC A6 42 00            lea rax, [rip + 0x42a6fc]
00AE1944  EB 3F                           jmp 0x140ae1985
00AE1946  44 39 7F 68                     cmp dword ptr [rdi + 0x68], r15d
00AE194A  75 36                           jne 0x140ae1982
00AE194C  48 8D 4F 50                     lea rcx, [rdi + 0x50]
00AE1950  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
00AE1955  45 33 C9                        xor r9d, r9d
00AE1958  45 33 C0                        xor r8d, r8d
00AE195B  33 D2                           xor edx, edx
00AE195D  E8 4E CD 72 FF                  call 0x14020e6b0
00AE1962  48 8B CF                        mov rcx, rdi
00AE1965  E8 CA 4E C8 FF                  call 0x140766834
00AE196A  85 C0                           test eax, eax
00AE196C  78 05                           js 0x140ae1973
00AE196E  45 8A E7                        mov r12b, r15b
00AE1971  EB 08                           jmp 0x140ae197b
00AE1973  48 8B CF                        mov rcx, rdi
00AE1976  E8 7D 12 FF FF                  call 0x140ad2bf8
00AE197B  48 8D 05 BE A6 42 00            lea rax, [rip + 0x42a6be]
00AE1982  48 8B 3F                        mov rdi, qword ptr [rdi]
00AE1985  48 3B F8                        cmp rdi, rax
00AE1988  75 BC                           jne 0x140ae1946
00AE198A  4C 8B 3D BF A6 42 00            mov r15, qword ptr [rip + 0x42a6bf]
00AE1991  48 8D 05 B8 A6 42 00            lea rax, [rip + 0x42a6b8]
00AE1998  4C 3B F8                        cmp r15, rax
00AE199B  0F 84 6D 01 00 00               je 0x140ae1b0e
00AE19A1  8B 5C 24 6C                     mov ebx, dword ptr [rsp + 0x6c]
00AE19A5  4C 8D 2D A4 A6 42 00            lea r13, [rip + 0x42a6a4]
00AE19AC  41 BE 01 00 00 00               mov r14d, 1
00AE19B2  49 8D 7F C0                     lea rdi, [r15 - 0x40]
00AE19B6  41 8A D6                        mov dl, r14b
00AE19B9  0F 10 87 A4 00 00 00            movups xmm0, xmmword ptr [rdi + 0xa4]
00AE19C0  48 8B CF                        mov rcx, rdi
00AE19C3  F3 0F 7F 45 F8                  movdqu xmmword ptr [rbp - 8], xmm0
00AE19C8  E8 83 FA FF FF                  call 0x140ae1450
00AE19CD  85 C0                           test eax, eax
00AE19CF  79 14                           jns 0x140ae19e5
00AE19D1  41 8B CE                        mov ecx, r14d
00AE19D4  C7 47 68 02 00 00 00            mov dword ptr [rdi + 0x68], 2
00AE19DB  E8 FC C9 9C FF                  call 0x1404ae3dc
00AE19E0  E9 0F 01 00 00                  jmp 0x140ae1af4
00AE19E5  E8 9A 7A AF FF                  call 0x1405d9484
00AE19EA  85 C0                           test eax, eax
00AE19EC  74 67                           je 0x140ae1a55
00AE19EE  40 38 35 CC A8 42 00            cmp byte ptr [rip + 0x42a8cc], sil
00AE19F5  74 5E                           je 0x140ae1a55
00AE19F7  84 DB                           test bl, bl
00AE19F9  74 5A                           je 0x140ae1a55
00AE19FB  0F 0D 0D 26 9E 32 00            prefetchw byte ptr [rip + 0x329e26]
00AE1A02  48 8B 05 1F 9E 32 00            mov rax, qword ptr [rip + 0x329e1f]
00AE1A09  48 8B C8                        mov rcx, rax
00AE1A0C  48 0B CE                        or rcx, rsi
00AE1A0F  F0 48 0F B1 0D 10 9E 32 00      lock cmpxchg qword ptr [rip + 0x329e10], rcx
00AE1A18  75 EF                           jne 0x140ae1a09
00AE1A1A  48 8B F0                        mov rsi, rax
00AE1A1D  4C 8B F0                        mov r14, rax
00AE1A20  48 C1 EE 20                     shr rsi, 0x20
00AE1A24  3B 87 1C 01 00 00               cmp eax, dword ptr [rdi + 0x11c]
00AE1A2A  75 08                           jne 0x140ae1a34
00AE1A2C  3B B7 20 01 00 00               cmp esi, dword ptr [rdi + 0x120]
00AE1A32  74 1B                           je 0x140ae1a4f
00AE1A34  44 8B C6                        mov r8d, esi
00AE1A37  41 8B D6                        mov edx, r14d
00AE1A3A  48 8B CF                        mov rcx, rdi
00AE1A3D  E8 96 7A AF FF                  call 0x1405d94d8
00AE1A42  44 89 B7 1C 01 00 00            mov dword ptr [rdi + 0x11c], r14d
00AE1A49  89 B7 20 01 00 00               mov dword ptr [rdi + 0x120], esi
00AE1A4F  41 BE 01 00 00 00               mov r14d, 1
00AE1A55  48 8B CF                        mov rcx, rdi
00AE1A58  E8 F3 E3 FF FF                  call 0x140adfe50
00AE1A5D  8B 8F A4 00 00 00               mov ecx, dword ptr [rdi + 0xa4]
00AE1A63  8B C1                           mov eax, ecx
00AE1A65  33 45 F8                        xor eax, dword ptr [rbp - 8]
00AE1A68  A8 07                           test al, 7
00AE1A6A  74 09                           je 0x140ae1a75
00AE1A6C  41 8A F6                        mov sil, r14b
00AE1A6F  89 74 24 54                     mov dword ptr [rsp + 0x54], esi
00AE1A73  EB 1A                           jmp 0x140ae1a8f
00AE1A75  8B 87 A8 00 00 00               mov eax, dword ptr [rdi + 0xa8]
00AE1A7B  39 45 FC                        cmp dword ptr [rbp - 4], eax
00AE1A7E  75 0B                           jne 0x140ae1a8b
00AE1A80  8B 87 B0 00 00 00               mov eax, dword ptr [rdi + 0xb0]
00AE1A86  39 45 04                        cmp dword ptr [rbp + 4], eax
00AE1A89  74 04                           je 0x140ae1a8f
00AE1A8B  44 88 75 80                     mov byte ptr [rbp - 0x80], r14b
00AE1A8F  83 C8 FF                        or eax, 0xffffffff
00AE1A92  F6 C1 02                        test cl, 2
00AE1A95  74 0A                           je 0x140ae1aa1
00AE1A97  33 D2                           xor edx, edx
00AE1A99  48 8B CF                        mov rcx, rdi
00AE1A9C  E8 DF 73 FB FF                  call 0x140a98e80
00AE1AA1  89 87 D0 00 00 00               mov dword ptr [rdi + 0xd0], eax
00AE1AA7  4C 8D 05 E2 0C 02 00            lea r8, [rip + 0x20ce2]
00AE1AAE  33 F6                           xor esi, esi
00AE1AB0  4C 8B CF                        mov r9, rdi
00AE1AB3  83 F8 FF                        cmp eax, -1
00AE1AB6  8B CE                           mov ecx, esi
00AE1AB8  0F 45 C8                        cmovne ecx, eax
00AE1ABB  8B 87 B0 00 00 00               mov eax, dword ptr [rdi + 0xb0]
00AE1AC1  89 4C 24 40                     mov dword ptr [rsp + 0x40], ecx
00AE1AC5  8D 56 03                        lea edx, [rsi + 3]
00AE1AC8  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
00AE1ACC  B9 92 00 00 00                  mov ecx, 0x92
00AE1AD1  8B 87 AC 00 00 00               mov eax, dword ptr [rdi + 0xac]
00AE1AD7  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00AE1ADB  8B 87 A8 00 00 00               mov eax, dword ptr [rdi + 0xa8]
00AE1AE1  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
00AE1AE5  8B 87 A4 00 00 00               mov eax, dword ptr [rdi + 0xa4]
00AE1AEB  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00AE1AEF  E8 9C 77 87 FF                  call 0x140359290
00AE1AF4  4D 8B 3F                        mov r15, qword ptr [r15]
00AE1AF7  4D 3B FD                        cmp r15, r13
00AE1AFA  0F 85 B2 FE FF FF               jne 0x140ae19b2
00AE1B00  48 8B 5C 24 70                  mov rbx, qword ptr [rsp + 0x70]
00AE1B05  44 8B 6D 84                     mov r13d, dword ptr [rbp - 0x7c]
00AE1B09  44 8B 74 24 68                  mov r14d, dword ptr [rsp + 0x68]
00AE1B0E  41 BF 01 00 00 00               mov r15d, 1
00AE1B14  48 85 DB                        test rbx, rbx
00AE1B17  0F 84 85 01 00 00               je 0x140ae1ca2
00AE1B1D  8B 83 80 00 00 00               mov eax, dword ptr [rbx + 0x80]
00AE1B23  41 2B C7                        sub eax, r15d
00AE1B26  41 3B C7                        cmp eax, r15d
00AE1B29  0F 87 73 01 00 00               ja 0x140ae1ca2
00AE1B2F  45 84 F6                        test r14b, r14b
00AE1B32  0F 84 B4 00 00 00               je 0x140ae1bec
00AE1B38  0F 0D 0D 71 5D 38 00            prefetchw byte ptr [rip + 0x385d71]
00AE1B3F  8A 05 6B 5D 38 00               mov al, byte ptr [rip + 0x385d6b]
00AE1B45  8A C8                           mov cl, al
00AE1B47  40 0A CE                        or cl, sil
00AE1B4A  F0 0F B0 0D 5E 5D 38 00         lock cmpxchg byte ptr [rip + 0x385d5e], cl
00AE1B52  75 F1                           jne 0x140ae1b45
00AE1B54  40 8A F8                        mov dil, al
00AE1B57  3A 83 D8 00 00 00               cmp al, byte ptr [rbx + 0xd8]
00AE1B5D  0F 84 3F 01 00 00               je 0x140ae1ca2
00AE1B63  8B 8B B4 00 00 00               mov ecx, dword ptr [rbx + 0xb4]
00AE1B69  48 8B C3                        mov rax, rbx
00AE1B6C  BA B4 00 00 00                  mov edx, 0xb4
00AE1B71  40 84 FF                        test dil, dil
00AE1B74  74 05                           je 0x140ae1b7b
00AE1B76  83 C9 04                        or ecx, 4
00AE1B79  EB 03                           jmp 0x140ae1b7e
00AE1B7B  83 E1 FB                        and ecx, 0xfffffffb
00AE1B7E  89 0C 02                        mov dword ptr [rdx + rax], ecx
00AE1B81  4C 8D 4D 90                     lea r9, [rbp - 0x70]
00AE1B85  89 75 90                        mov dword ptr [rbp - 0x70], esi
00AE1B88  F6 C1 04                        test cl, 4
00AE1B8B  0F B6 45 91                     movzx eax, byte ptr [rbp - 0x6f]
00AE1B8F  BA 74 40 29 00                  mov edx, 0x294074
00AE1B94  48 8B 4B 38                     mov rcx, qword ptr [rbx + 0x38]
00AE1B98  41 0F 45 C7                     cmovne eax, r15d
00AE1B9C  45 33 C0                        xor r8d, r8d
00AE1B9F  89 74 24 28                     mov dword ptr [rsp + 0x28], esi
00AE1BA3  88 45 91                        mov byte ptr [rbp - 0x6f], al
00AE1BA6  C7 44 24 20 04 00 00 00         mov dword ptr [rsp + 0x20], 4
00AE1BAE  E8 E5 2E F9 FF                  call 0x140a74a98
00AE1BB3  48 8B 53 38                     mov rdx, qword ptr [rbx + 0x38]
00AE1BB7  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
00AE1BBB  E8 90 24 9A FF                  call 0x140484050
00AE1BC0  85 C0                           test eax, eax
00AE1BC2  79 15                           jns 0x140ae1bd9
00AE1BC4  BA 03 00 00 00                  mov edx, 3
00AE1BC9  44 8B C0                        mov r8d, eax
00AE1BCC  48 8B CB                        mov rcx, rbx
00AE1BCF  E8 E4 66 C8 FF                  call 0x1407682b8
00AE1BD4  E9 C9 00 00 00                  jmp 0x140ae1ca2
00AE1BD9  44 89 BB 80 00 00 00            mov dword ptr [rbx + 0x80], r15d
00AE1BE0  40 88 BB D8 00 00 00            mov byte ptr [rbx + 0xd8], dil
00AE1BE7  E9 B6 00 00 00                  jmp 0x140ae1ca2
00AE1BEC  0F 10 B3 B0 00 00 00            movups xmm6, xmmword ptr [rbx + 0xb0]
00AE1BF3  41 8A D7                        mov dl, r15b
00AE1BF6  48 8B CB                        mov rcx, rbx
00AE1BF9  0F 10 BB C0 00 00 00            movups xmm7, xmmword ptr [rbx + 0xc0]
00AE1C00  F2 44 0F 10 83 D0 00 00 00      movsd xmm8, qword ptr [rbx + 0xd0]
00AE1C09  0F 11 75 70                     movups xmmword ptr [rbp + 0x70], xmm6
00AE1C0D  0F 11 BD 80 00 00 00            movups xmmword ptr [rbp + 0x80], xmm7
00AE1C14  F2 44 0F 11 85 90 00 00 00      movsd qword ptr [rbp + 0x90], xmm8
00AE1C1D  E8 22 60 C8 FF                  call 0x140767c44
00AE1C22  85 C0                           test eax, eax
00AE1C24  79 07                           jns 0x140ae1c2d
00AE1C26  BA 04 00 00 00                  mov edx, 4
00AE1C2B  EB 9C                           jmp 0x140ae1bc9
00AE1C2D  8B 4C 24 54                     mov ecx, dword ptr [rsp + 0x54]
00AE1C31  66 0F 6F C6                     movdqa xmm0, xmm6
00AE1C35  66 0F 73 D8 04                  psrldq xmm0, 4
00AE1C3A  66 0F 7E C0                     movd eax, xmm0
00AE1C3E  0F B6 C9                        movzx ecx, cl
00AE1C41  44 89 BB 80 00 00 00            mov dword ptr [rbx + 0x80], r15d
00AE1C48  32 83 B4 00 00 00               xor al, byte ptr [rbx + 0xb4]
00AE1C4E  41 84 C7                        test r15b, al
00AE1C51  8B 83 8C 00 00 00               mov eax, dword ptr [rbx + 0x8c]
00AE1C57  41 0F 45 CF                     cmovne ecx, r15d
00AE1C5B  89 4C 24 54                     mov dword ptr [rsp + 0x54], ecx
00AE1C5F  41 84 C7                        test r15b, al
00AE1C62  74 42                           je 0x140ae1ca6
00AE1C64  0F 10 83 B0 00 00 00            movups xmm0, xmmword ptr [rbx + 0xb0]
00AE1C6B  48 8D 55 10                     lea rdx, [rbp + 0x10]
00AE1C6F  0F 10 8B C0 00 00 00            movups xmm1, xmmword ptr [rbx + 0xc0]
00AE1C76  48 8D 4D 40                     lea rcx, [rbp + 0x40]
00AE1C7A  0F 29 45 10                     movaps xmmword ptr [rbp + 0x10], xmm0
00AE1C7E  F2 0F 10 83 D0 00 00 00         movsd xmm0, qword ptr [rbx + 0xd0]
00AE1C86  F2 0F 11 45 30                  movsd qword ptr [rbp + 0x30], xmm0
00AE1C8B  0F 29 4D 20                     movaps xmmword ptr [rbp + 0x20], xmm1
00AE1C8F  0F 29 75 40                     movaps xmmword ptr [rbp + 0x40], xmm6
00AE1C93  0F 29 7D 50                     movaps xmmword ptr [rbp + 0x50], xmm7
00AE1C97  F2 44 0F 11 45 60               movsd qword ptr [rbp + 0x60], xmm8
00AE1C9D  E8 2A 5D C8 FF                  call 0x1407679cc
00AE1CA2  8B 4C 24 54                     mov ecx, dword ptr [rsp + 0x54]
00AE1CA6  45 84 E4                        test r12b, r12b
00AE1CA9  74 13                           je 0x140ae1cbe
00AE1CAB  E8 20 E1 E2 FF                  call 0x14090fdd0
00AE1CB0  41 8A CF                        mov cl, r15b
00AE1CB3  48 89 35 FE 5B 38 00            mov qword ptr [rip + 0x385bfe], rsi
00AE1CBA  89 4C 24 54                     mov dword ptr [rsp + 0x54], ecx
00AE1CBE  41 F6 C5 04                     test r13b, 4
00AE1CC2  75 04                           jne 0x140ae1cc8
00AE1CC4  84 C9                           test cl, cl
00AE1CC6  74 55                           je 0x140ae1d1d
00AE1CC8  8B 05 D6 5B 38 00               mov eax, dword ptr [rip + 0x385bd6]
00AE1CCE  48 8D 0D CB 73 42 00            lea rcx, [rip + 0x4273cb]
00AE1CD5  85 C0                           test eax, eax
00AE1CD7  75 37                           jne 0x140ae1d10
00AE1CD9  48 A1 08 00 00 00 80 F7 FF FF   movabs rax, qword ptr [0xfffff78000000008]
00AE1CE3  45 33 C9                        xor r9d, r9d
00AE1CE6  48 05 00 A3 E1 11               add rax, 0x11e1a300
00AE1CEC  45 33 C0                        xor r8d, r8d
00AE1CEF  48 89 05 1A 9B 32 00            mov qword ptr [rip + 0x329b1a], rax
00AE1CF6  48 C7 C2 00 5D 1E EE            mov rdx, 0xffffffffee1e5d00
00AE1CFD  48 8D 05 5C 73 42 00            lea rax, [rip + 0x42735c]
00AE1D04  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AE1D09  E8 A2 0F 75 FF                  call 0x140232cb0
00AE1D0E  EB 0D                           jmp 0x140ae1d1d
00AE1D10  48 83 0D F8 9A 32 00 FF         or qword ptr [rip + 0x329af8], 0xffffffffffffffff
00AE1D18  E8 C3 0A 75 FF                  call 0x1402327e0
00AE1D1D  B8 00 00 00 80                  mov eax, 0x80000000
00AE1D22  89 74 24 68                     mov dword ptr [rsp + 0x68], esi
00AE1D26  33 D2                           xor edx, edx
00AE1D28  89 44 24 6C                     mov dword ptr [rsp + 0x6c], eax
00AE1D2C  48 83 C9 FF                     or rcx, 0xffffffffffffffff
00AE1D30  89 45 C8                        mov dword ptr [rbp - 0x38], eax
00AE1D33  0F 57 C0                        xorps xmm0, xmm0
00AE1D36  48 89 95 B8 00 00 00            mov qword ptr [rbp + 0xb8], rdx
00AE1D3D  0F 11 85 98 00 00 00            movups xmmword ptr [rbp + 0x98], xmm0
00AE1D44  89 85 A4 00 00 00               mov dword ptr [rbp + 0xa4], eax
00AE1D4A  44 8B D8                        mov r11d, eax
00AE1D4D  83 C8 FF                        or eax, 0xffffffff
00AE1D50  48 89 55 D8                     mov qword ptr [rbp - 0x28], rdx
00AE1D54  39 35 DA A2 42 00               cmp dword ptr [rip + 0x42a2da], esi
00AE1D5A  44 8B E8                        mov r13d, eax
00AE1D5D  0F 11 85 A8 00 00 00            movups xmmword ptr [rbp + 0xa8], xmm0
00AE1D64  89 95 C0 00 00 00               mov dword ptr [rbp + 0xc0], edx
00AE1D6A  44 8B F0                        mov r14d, eax
00AE1D6D  89 85 A0 00 00 00               mov dword ptr [rbp + 0xa0], eax
00AE1D73  44 8B F8                        mov r15d, eax
00AE1D76  89 85 9C 00 00 00               mov dword ptr [rbp + 0x9c], eax
00AE1D7C  44 8B C8                        mov r9d, eax
00AE1D7F  89 85 AC 00 00 00               mov dword ptr [rbp + 0xac], eax
00AE1D85  44 8B E0                        mov r12d, eax
00AE1D88  89 45 AC                        mov dword ptr [rbp - 0x54], eax
00AE1D8B  44 8B D0                        mov r10d, eax
00AE1D8E  89 85 B0 00 00 00               mov dword ptr [rbp + 0xb0], eax
00AE1D94  89 85 B4 00 00 00               mov dword ptr [rbp + 0xb4], eax
00AE1D9A  89 45 84                        mov dword ptr [rbp - 0x7c], eax
00AE1D9D  89 85 B8 00 00 00               mov dword ptr [rbp + 0xb8], eax
00AE1DA3  48 89 4D B8                     mov qword ptr [rbp - 0x48], rcx
00AE1DA7  48 89 4D C0                     mov qword ptr [rbp - 0x40], rcx
00AE1DAB  89 44 24 7C                     mov dword ptr [rsp + 0x7c], eax
00AE1DAF  75 37                           jne 0x140ae1de8
00AE1DB1  83 7C 24 60 03                  cmp dword ptr [rsp + 0x60], 3
00AE1DB6  44 8D 6A 01                     lea r13d, [rdx + 1]
00AE1DBA  41 8B F5                        mov esi, r13d
00AE1DBD  44 89 AD 98 00 00 00            mov dword ptr [rbp + 0x98], r13d
00AE1DC4  0F 85 C4 02 00 00               jne 0x140ae208e
00AE1DCA  41 8A CD                        mov cl, r13b
00AE1DCD  E8 AE B3 94 FF                  call 0x14042d180
00AE1DD2  48 3D 00 A3 E1 11               cmp rax, 0x11e1a300
00AE1DD8  0F 82 B0 02 00 00               jb 0x140ae208e
00AE1DDE  44 89 6C 24 60                  mov dword ptr [rsp + 0x60], r13d
00AE1DE3  E9 A6 02 00 00                  jmp 0x140ae208e
00AE1DE8  48 8B 3D 61 A2 42 00            mov rdi, qword ptr [rip + 0x42a261]
00AE1DEF  48 8D 05 5A A2 42 00            lea rax, [rip + 0x42a25a]
00AE1DF6  8B B5 98 00 00 00               mov esi, dword ptr [rbp + 0x98]
00AE1DFC  48 3B F8                        cmp rdi, rax
00AE1DFF  0F 84 CE 01 00 00               je 0x140ae1fd3
00AE1E05  8B 5D C8                        mov ebx, dword ptr [rbp - 0x38]
00AE1E08  8B 57 64                        mov edx, dword ptr [rdi + 0x64]
00AE1E0B  8B CA                           mov ecx, edx
00AE1E0D  81 E1 E7 00 00 00               and ecx, 0xe7
00AE1E13  8B C2                           mov eax, edx
00AE1E15  83 E0 0A                        and eax, 0xa
00AE1E18  44 8B C1                        mov r8d, ecx
00AE1E1B  41 83 C8 08                     or r8d, 8
00AE1E1F  3C 0A                           cmp al, 0xa
00AE1E21  44 0F 45 C1                     cmovne r8d, ecx
00AE1E25  33 C9                           xor ecx, ecx
00AE1E27  8D 41 10                        lea eax, [rcx + 0x10]
00AE1E2A  40 84 F0                        test al, sil
00AE1E2D  75 0C                           jne 0x140ae1e3b
00AE1E2F  8A C2                           mov al, dl
00AE1E31  24 11                           and al, 0x11
00AE1E33  3C 11                           cmp al, 0x11
00AE1E35  8D 41 10                        lea eax, [rcx + 0x10]
00AE1E38  0F 44 C8                        cmove ecx, eax
00AE1E3B  8B C2                           mov eax, edx
00AE1E3D  83 E0 10                        and eax, 0x10
00AE1E40  F6 C2 01                        test dl, 1
00AE1E43  75 0C                           jne 0x140ae1e51
00AE1E45  F7 D8                           neg eax
00AE1E47  1B C0                           sbb eax, eax
00AE1E49  83 E0 FD                        and eax, 0xfffffffd
00AE1E4C  83 C0 04                        add eax, 4
00AE1E4F  EB 0A                           jmp 0x140ae1e5b
00AE1E51  F7 D8                           neg eax
00AE1E53  1B C0                           sbb eax, eax
00AE1E55  83 E0 FA                        and eax, 0xfffffffa
00AE1E58  83 C0 08                        add eax, 8
00AE1E5B  09 44 24 68                     or dword ptr [rsp + 0x68], eax
00AE1E5F  33 F1                           xor esi, ecx
00AE1E61  8B 47 68                        mov eax, dword ptr [rdi + 0x68]
00AE1E64  41 0B F0                        or esi, r8d
00AE1E67  83 C9 FF                        or ecx, 0xffffffff
00AE1E6A  3B C1                           cmp eax, ecx
00AE1E6C  74 18                           je 0x140ae1e86
00AE1E6E  44 3B F1                        cmp r14d, ecx
00AE1E71  BA 00 00 00 00                  mov edx, 0
00AE1E76  44 0F 44 F2                     cmove r14d, edx
00AE1E7A  44 03 F0                        add r14d, eax
00AE1E7D  44 89 B5 9C 00 00 00            mov dword ptr [rbp + 0x9c], r14d
00AE1E84  EB 02                           jmp 0x140ae1e88
00AE1E86  33 D2                           xor edx, edx
00AE1E88  44 8B 47 6C                     mov r8d, dword ptr [rdi + 0x6c]
00AE1E8C  44 3B C1                        cmp r8d, ecx
00AE1E8F  74 15                           je 0x140ae1ea6
00AE1E91  44 3B E9                        cmp r13d, ecx
00AE1E94  44 0F 44 EA                     cmove r13d, edx
00AE1E98  45 3B C5                        cmp r8d, r13d
00AE1E9B  45 0F 47 E8                     cmova r13d, r8d
00AE1E9F  44 89 AD A0 00 00 00            mov dword ptr [rbp + 0xa0], r13d
00AE1EA6  8B 4F 70                        mov ecx, dword ptr [rdi + 0x70]
00AE1EA9  B8 00 00 00 80                  mov eax, 0x80000000
00AE1EAE  3B C8                           cmp ecx, eax
00AE1EB0  74 0D                           je 0x140ae1ebf
00AE1EB2  3B D8                           cmp ebx, eax
00AE1EB4  0F 44 DA                        cmove ebx, edx
00AE1EB7  03 D9                           add ebx, ecx
00AE1EB9  89 9D A4 00 00 00               mov dword ptr [rbp + 0xa4], ebx
00AE1EBF  41 83 F8 FF                     cmp r8d, -1
00AE1EC3  74 2F                           je 0x140ae1ef4
00AE1EC5  3B C8                           cmp ecx, eax
00AE1EC7  74 2B                           je 0x140ae1ef4
00AE1EC9  44 3B D8                        cmp r11d, eax
00AE1ECC  44 0F 44 DA                     cmove r11d, edx
00AE1ED0  45 85 C0                        test r8d, r8d
00AE1ED3  75 04                           jne 0x140ae1ed9
00AE1ED5  8B C2                           mov eax, edx
00AE1ED7  EB 13                           jmp 0x140ae1eec
00AE1ED9  69 C9 E8 03 00 00               imul ecx, ecx, 0x3e8
00AE1EDF  41 8B C0                        mov eax, r8d
00AE1EE2  D1 E8                           shr eax, 1
00AE1EE4  03 C1                           add eax, ecx
00AE1EE6  99                              cdq
00AE1EE7  41 F7 F8                        idiv r8d
00AE1EEA  33 D2                           xor edx, edx
00AE1EEC  44 03 D8                        add r11d, eax
00AE1EEF  44 89 5C 24 6C                  mov dword ptr [rsp + 0x6c], r11d
00AE1EF4  8B 47 78                        mov eax, dword ptr [rdi + 0x78]
00AE1EF7  83 C9 FF                        or ecx, 0xffffffff
00AE1EFA  3B C1                           cmp eax, ecx
00AE1EFC  74 11                           je 0x140ae1f0f
00AE1EFE  44 3B F9                        cmp r15d, ecx
00AE1F01  44 0F 44 FA                     cmove r15d, edx
00AE1F05  44 03 F8                        add r15d, eax
00AE1F08  44 89 BD AC 00 00 00            mov dword ptr [rbp + 0xac], r15d
00AE1F0F  8B 87 80 00 00 00               mov eax, dword ptr [rdi + 0x80]
00AE1F15  3B C1                           cmp eax, ecx
00AE1F17  74 11                           je 0x140ae1f2a
00AE1F19  44 3B E1                        cmp r12d, ecx
00AE1F1C  44 0F 44 E2                     cmove r12d, edx
00AE1F20  44 03 E0                        add r12d, eax
00AE1F23  44 89 A5 B4 00 00 00            mov dword ptr [rbp + 0xb4], r12d
00AE1F2A  8B 47 7C                        mov eax, dword ptr [rdi + 0x7c]
00AE1F2D  3B C1                           cmp eax, ecx
00AE1F2F  74 12                           je 0x140ae1f43
00AE1F31  44 3B C9                        cmp r9d, ecx
00AE1F34  44 0F 44 C8                     cmove r9d, eax
00AE1F38  44 89 4D AC                     mov dword ptr [rbp - 0x54], r9d
00AE1F3C  44 89 8D B0 00 00 00            mov dword ptr [rbp + 0xb0], r9d
00AE1F43  8B 87 84 00 00 00               mov eax, dword ptr [rdi + 0x84]
00AE1F49  3B C1                           cmp eax, ecx
00AE1F4B  74 12                           je 0x140ae1f5f
00AE1F4D  44 3B D1                        cmp r10d, ecx
00AE1F50  44 0F 44 D0                     cmove r10d, eax
00AE1F54  44 89 55 84                     mov dword ptr [rbp - 0x7c], r10d
00AE1F58  44 89 95 B8 00 00 00            mov dword ptr [rbp + 0xb8], r10d
00AE1F5F  E8 20 75 AF FF                  call 0x1405d9484
00AE1F64  33 C9                           xor ecx, ecx
00AE1F66  85 C0                           test eax, eax
00AE1F68  74 3E                           je 0x140ae1fa8
00AE1F6A  38 0D 51 A3 42 00               cmp byte ptr [rip + 0x42a351], cl
00AE1F70  74 36                           je 0x140ae1fa8
00AE1F72  8B 87 8C 00 00 00               mov eax, dword ptr [rdi + 0x8c]
00AE1F78  BA 10 00 00 00                  mov edx, 0x10
00AE1F7D  8B 8F 88 00 00 00               mov ecx, dword ptr [rdi + 0x88]
00AE1F83  09 8D BC 00 00 00               or dword ptr [rbp + 0xbc], ecx
00AE1F89  48 89 45 D8                     mov qword ptr [rbp - 0x28], rax
00AE1F8D  89 85 C0 00 00 00               mov dword ptr [rbp + 0xc0], eax
00AE1F93  8B 05 EB A0 42 00               mov eax, dword ptr [rip + 0x42a0eb]
00AE1F99  84 C2                           test dl, al
00AE1F9B  74 0B                           je 0x140ae1fa8
00AE1F9D  84 CA                           test dl, cl
00AE1F9F  75 07                           jne 0x140ae1fa8
00AE1FA1  83 A7 DC 00 00 00 F7            and dword ptr [rdi + 0xdc], 0xfffffff7
00AE1FA8  48 8B 3F                        mov rdi, qword ptr [rdi]
00AE1FAB  48 8D 05 9E A0 42 00            lea rax, [rip + 0x42a09e]
00AE1FB2  44 8B 4D AC                     mov r9d, dword ptr [rbp - 0x54]
00AE1FB6  44 8B 55 84                     mov r10d, dword ptr [rbp - 0x7c]
00AE1FBA  44 8B 5C 24 6C                  mov r11d, dword ptr [rsp + 0x6c]
00AE1FBF  48 3B F8                        cmp rdi, rax
00AE1FC2  0F 85 40 FE FF FF               jne 0x140ae1e08
00AE1FC8  48 8B 5C 24 70                  mov rbx, qword ptr [rsp + 0x70]
00AE1FCD  89 B5 98 00 00 00               mov dword ptr [rbp + 0x98], esi
00AE1FD3  40 F6 C6 02                     test sil, 2
00AE1FD7  74 09                           je 0x140ae1fe2
00AE1FD9  83 E6 FB                        and esi, 0xfffffffb
00AE1FDC  89 B5 98 00 00 00               mov dword ptr [rbp + 0x98], esi
00AE1FE2  41 BD 01 00 00 00               mov r13d, 1
00AE1FE8  41 84 F5                        test r13b, sil
00AE1FEB  0F 85 8E 00 00 00               jne 0x140ae207f
00AE1FF1  45 33 E4                        xor r12d, r12d
00AE1FF4  44 39 25 B9 58 38 00            cmp dword ptr [rip + 0x3858b9], r12d
00AE1FFB  0F 85 90 00 00 00               jne 0x140ae2091
00AE2001  48 8B 0D 48 A0 42 00            mov rcx, qword ptr [rip + 0x42a048]
00AE2008  4C 8D 3D 41 A0 42 00            lea r15, [rip + 0x42a041]
00AE200F  45 8B F4                        mov r14d, r12d
00AE2012  49 3B CF                        cmp rcx, r15
00AE2015  74 7A                           je 0x140ae2091
00AE2017  44 8B 81 90 00 00 00            mov r8d, dword ptr [rcx + 0x90]
00AE201E  41 8D 40 FF                     lea eax, [r8 - 1]
00AE2022  83 F8 FD                        cmp eax, -3
00AE2025  77 0F                           ja 0x140ae2036
00AE2027  69 41 68 10 0E 00 00            imul eax, dword ptr [rcx + 0x68], 0xe10
00AE202E  33 D2                           xor edx, edx
00AE2030  41 F7 F0                        div r8d
00AE2033  44 2B F0                        sub r14d, eax
00AE2036  48 8B 09                        mov rcx, qword ptr [rcx]
00AE2039  49 3B CF                        cmp rcx, r15
00AE203C  75 D9                           jne 0x140ae2017
00AE203E  45 85 F6                        test r14d, r14d
00AE2041  74 4E                           je 0x140ae2091
00AE2043  48 8B 3D 06 A0 42 00            mov rdi, qword ptr [rip + 0x42a006]
00AE204A  8B 5C 24 7C                     mov ebx, dword ptr [rsp + 0x7c]
00AE204E  48 8D 4F C0                     lea rcx, [rdi - 0x40]
00AE2052  41 8B D6                        mov edx, r14d
00AE2055  E8 26 6E FB FF                  call 0x140a98e80
00AE205A  83 CA FF                        or edx, 0xffffffff
00AE205D  3B C2                           cmp eax, edx
00AE205F  74 0B                           je 0x140ae206c
00AE2061  3B DA                           cmp ebx, edx
00AE2063  41 8B CC                        mov ecx, r12d
00AE2066  0F 45 CB                        cmovne ecx, ebx
00AE2069  8D 1C 08                        lea ebx, [rax + rcx]
00AE206C  48 8B 3F                        mov rdi, qword ptr [rdi]
00AE206F  49 3B FF                        cmp rdi, r15
00AE2072  75 DA                           jne 0x140ae204e
00AE2074  89 5C 24 7C                     mov dword ptr [rsp + 0x7c], ebx
00AE2078  48 8B 5C 24 70                  mov rbx, qword ptr [rsp + 0x70]
00AE207D  EB 12                           jmp 0x140ae2091
00AE207F  40 F6 C6 04                     test sil, 4
00AE2083  74 09                           je 0x140ae208e
00AE2085  E8 DA 71 FB FF                  call 0x140a99264
00AE208A  48 89 45 B8                     mov qword ptr [rbp - 0x48], rax
00AE208E  45 33 E4                        xor r12d, r12d
00AE2091  8B 44 24 60                     mov eax, dword ptr [rsp + 0x60]
00AE2095  44 8A F6                        mov r14b, sil
00AE2098  45 22 F5                        and r14b, r13b
00AE209B  83 F8 02                        cmp eax, 2
00AE209E  75 05                           jne 0x140ae20a5
00AE20A0  45 84 F6                        test r14b, r14b
00AE20A3  74 0A                           je 0x140ae20af
00AE20A5  83 F8 03                        cmp eax, 3
00AE20A8  75 0A                           jne 0x140ae20b4
00AE20AA  45 84 F6                        test r14b, r14b
00AE20AD  74 05                           je 0x140ae20b4
00AE20AF  44 89 6C 24 60                  mov dword ptr [rsp + 0x60], r13d
00AE20B4  8B 05 A6 9F 42 00               mov eax, dword ptr [rip + 0x429fa6]
00AE20BA  41 BF 10 00 00 00               mov r15d, 0x10
00AE20C0  8B CE                           mov ecx, esi
00AE20C2  41 23 C7                        and eax, r15d
00AE20C5  41 23 CF                        and ecx, r15d
00AE20C8  3B C1                           cmp eax, ecx
00AE20CA  0F 84 8D 01 00 00               je 0x140ae225d
00AE20D0  85 C9                           test ecx, ecx
00AE20D2  44 89 64 24 30                  mov dword ptr [rsp + 0x30], r12d
00AE20D7  44 89 64 24 28                  mov dword ptr [rsp + 0x28], r12d
00AE20DC  48 8D 54 24 50                  lea rdx, [rsp + 0x50]
00AE20E1  0F 95 C0                        setne al
00AE20E4  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
00AE20E9  88 44 24 50                     mov byte ptr [rsp + 0x50], al
00AE20ED  48 8D 0D F4 EA 53 FF            lea rcx, [rip - 0xac150c]
00AE20F4  0F B6 C0                        movzx eax, al
00AE20F7  45 33 C9                        xor r9d, r9d
00AE20FA  45 8B C5                        mov r8d, r13d
00AE20FD  89 45 D0                        mov dword ptr [rbp - 0x30], eax
00AE2100  E8 0B EC BC FF                  call 0x1406b0d10
00AE2105  4C 8D 45 D0                     lea r8, [rbp - 0x30]
00AE2109  8B F8                           mov edi, eax
00AE210B  41 8D 57 F4                     lea edx, [r15 - 0xc]
00AE210F  48 8D 0D 32 76 54 FF            lea rcx, [rip - 0xab89ce]
00AE2116  E8 51 2C E3 FF                  call 0x140914d6c
00AE211B  83 3D 26 56 32 00 05            cmp dword ptr [rip + 0x325626], 5
00AE2122  44 8B C0                        mov r8d, eax
00AE2125  0F 86 32 01 00 00               jbe 0x140ae225d
00AE212B  48 BA 00 00 00 00 00 40 00 00   movabs rdx, 0x400000000000
00AE2135  48 8D 0D 0C 56 32 00            lea rcx, [rip + 0x32560c]
00AE213C  E8 5F C9 94 FF                  call 0x14042eaa0
00AE2141  84 C0                           test al, al
00AE2143  0F 84 14 01 00 00               je 0x140ae225d
00AE2149  8A 4C 24 50                     mov cl, byte ptr [rsp + 0x50]
00AE214D  48 8D 44 24 5C                  lea rax, [rsp + 0x5c]
00AE2152  48 89 85 30 03 00 00            mov qword ptr [rbp + 0x330], rax
00AE2159  48 8D 15 20 06 02 00            lea rdx, [rip + 0x20620]
00AE2160  48 8D 45 CC                     lea rax, [rbp - 0x34]
00AE2164  44 89 45 D4                     mov dword ptr [rbp - 0x2c], r8d
00AE2168  44 8B 44 24 68                  mov r8d, dword ptr [rsp + 0x68]
00AE216D  4C 8D 0D 3C 07 02 00            lea r9, [rip + 0x2073c]
00AE2174  48 89 85 40 03 00 00            mov qword ptr [rbp + 0x340], rax
00AE217B  45 84 C5                        test r13b, r8b
00AE217E  48 8D 45 D4                     lea rax, [rbp - 0x2c]
00AE2182  88 4C 24 5C                     mov byte ptr [rsp + 0x5c], cl
00AE2186  49 0F 44 D1                     cmove rdx, r9
00AE218A  48 89 85 50 03 00 00            mov qword ptr [rbp + 0x350], rax
00AE2191  48 8D 8D 60 03 00 00            lea rcx, [rbp + 0x360]
00AE2198  48 C7 85 38 03 00 00 01 00 00 00  mov qword ptr [rbp + 0x338], 1
00AE21A3  89 7D CC                        mov dword ptr [rbp - 0x34], edi
00AE21A6  48 C7 85 48 03 00 00 04 00 00 00  mov qword ptr [rbp + 0x348], 4
00AE21B1  48 C7 85 58 03 00 00 04 00 00 00  mov qword ptr [rbp + 0x358], 4
00AE21BC  E8 43 51 94 FF                  call 0x140427304
00AE21C1  41 F6 C0 02                     test r8b, 2
00AE21C5  48 8D 15 54 06 02 00            lea rdx, [rip + 0x20654]
00AE21CC  48 8D 8D 70 03 00 00            lea rcx, [rbp + 0x370]
00AE21D3  49 0F 44 D1                     cmove rdx, r9
00AE21D7  E8 28 51 94 FF                  call 0x140427304
00AE21DC  41 F6 C0 04                     test r8b, 4
00AE21E0  48 8D 15 29 06 02 00            lea rdx, [rip + 0x20629]
00AE21E7  48 8D 8D 80 03 00 00            lea rcx, [rbp + 0x380]
00AE21EE  49 0F 44 D1                     cmove rdx, r9
00AE21F2  E8 0D 51 94 FF                  call 0x140427304
00AE21F7  41 F6 C0 08                     test r8b, 8
00AE21FB  48 8D 15 2E 08 02 00            lea rdx, [rip + 0x2082e]
00AE2202  48 8D 8D 90 03 00 00            lea rcx, [rbp + 0x390]
00AE2209  49 0F 44 D1                     cmove rdx, r9
00AE220D  E8 F2 50 94 FF                  call 0x140427304
00AE2212  48 8D 45 F0                     lea rax, [rbp - 0x10]
00AE2216  48 C7 45 F0 00 00 00 01         mov qword ptr [rbp - 0x10], 0x1000000
00AE221E  48 89 85 A0 03 00 00            mov qword ptr [rbp + 0x3a0], rax
00AE2225  48 8D 15 2E B9 56 FF            lea rdx, [rip - 0xa946d2]
00AE222C  48 8D 85 10 03 00 00            lea rax, [rbp + 0x310]
00AE2233  48 C7 85 A8 03 00 00 08 00 00 00  mov qword ptr [rbp + 0x3a8], 8
00AE223E  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE2243  48 8D 0D FE 54 32 00            lea rcx, [rip + 0x3254fe]
00AE224A  45 33 C9                        xor r9d, r9d
00AE224D  C7 44 24 20 0A 00 00 00         mov dword ptr [rsp + 0x20], 0xa
00AE2255  45 33 C0                        xor r8d, r8d
00AE2258  E8 83 3E 94 FF                  call 0x1404260e0
00AE225D  E8 22 72 AF FF                  call 0x1405d9484
00AE2262  85 C0                           test eax, eax
00AE2264  74 40                           je 0x140ae22a6
00AE2266  8B BD BC 00 00 00               mov edi, dword ptr [rbp + 0xbc]
00AE226C  39 3D 12 9E 42 00               cmp dword ptr [rip + 0x429e12], edi
00AE2272  48 8B 55 D8                     mov rdx, qword ptr [rbp - 0x28]
00AE2276  75 08                           jne 0x140ae2280
00AE2278  39 15 0A 9E 42 00               cmp dword ptr [rip + 0x429e0a], edx
00AE227E  74 26                           je 0x140ae22a6
00AE2280  8B CF                           mov ecx, edi
00AE2282  E8 35 49 C8 FF                  call 0x140766bbc
00AE2287  8B 05 F7 9D 42 00               mov eax, dword ptr [rip + 0x429df7]
00AE228D  41 84 C7                        test r15b, al
00AE2290  74 14                           je 0x140ae22a6
00AE2292  41 84 FF                        test r15b, dil
00AE2295  75 0F                           jne 0x140ae22a6
00AE2297  F0 48 83 25 88 95 32 00 F7      lock and qword ptr [rip + 0x329588], 0xfffffffffffffff7
00AE22A0  8B B5 98 00 00 00               mov esi, dword ptr [rbp + 0x98]
00AE22A6  8B C6                           mov eax, esi
00AE22A8  83 E0 40                        and eax, 0x40
00AE22AB  40 F6 C6 20                     test sil, 0x20
00AE22AF  74 0B                           je 0x140ae22bc
00AE22B1  F7 D8                           neg eax
00AE22B3  1B FF                           sbb edi, edi
00AE22B5  F7 DF                           neg edi
00AE22B7  41 03 FD                        add edi, r13d
00AE22BA  EB 03                           jmp 0x140ae22bf
00AE22BC  41 8B FC                        mov edi, r12d
00AE22BF  39 3D 57 9F 42 00               cmp dword ptr [rip + 0x429f57], edi
00AE22C5  74 2F                           je 0x140ae22f6
00AE22C7  48 8D 0D 42 6D 42 00            lea rcx, [rip + 0x426d42]
00AE22CE  E8 71 E8 94 FF                  call 0x140430b44
00AE22D3  48 8D 0D 36 6D 42 00            lea rcx, [rip + 0x426d36]
00AE22DA  89 3D 3C 9F 42 00               mov dword ptr [rip + 0x429f3c], edi
00AE22E0  89 3D 5A 6D 42 00               mov dword ptr [rip + 0x426d5a], edi
00AE22E6  E8 D1 D8 7F FF                  call 0x1402dfbbc
00AE22EB  8B 7D B0                        mov edi, dword ptr [rbp - 0x50]
00AE22EE  45 8A FD                        mov r15b, r13b
00AE22F1  83 CF 02                        or edi, 2
00AE22F4  EB 08                           jmp 0x140ae22fe
00AE22F6  8B 7D B0                        mov edi, dword ptr [rbp - 0x50]
00AE22F9  44 8A 7C 24 5D                  mov r15b, byte ptr [rsp + 0x5d]
00AE22FE  8B 74 24 7C                     mov esi, dword ptr [rsp + 0x7c]
00AE2302  48 8D 8D 98 00 00 00            lea rcx, [rbp + 0x98]
00AE2309  44 8B 44 24 6C                  mov r8d, dword ptr [rsp + 0x6c]
00AE230E  8B D6                           mov edx, esi
00AE2310  E8 BB E9 FF FF                  call 0x140ae0cd0
00AE2315  84 C0                           test al, al
00AE2317  75 05                           jne 0x140ae231e
00AE2319  45 84 FF                        test r15b, r15b
00AE231C  74 1A                           je 0x140ae2338
00AE231E  8B D7                           mov edx, edi
00AE2320  41 BF 04 00 00 00               mov r15d, 4
00AE2326  41 0B D7                        or edx, r15d
00AE2329  41 8A CE                        mov cl, r14b
00AE232C  84 C0                           test al, al
00AE232E  0F 44 D7                        cmove edx, edi
00AE2331  E8 6A 0A 00 00                  call 0x140ae2da0
00AE2336  EB 06                           jmp 0x140ae233e
00AE2338  41 BF 04 00 00 00               mov r15d, 4
00AE233E  F0 83 25 12 6D 42 00 DF         lock and dword ptr [rip + 0x426d12], 0xffffffdf
00AE2346  48 B8 08 00 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000008
00AE2350  48 8B 00                        mov rax, qword ptr [rax]
00AE2353  48 89 05 CE 9E 42 00            mov qword ptr [rip + 0x429ece], rax
00AE235A  F0 44 09 24 24                  lock or dword ptr [rsp], r12d
00AE235F  4C 39 25 CA 9E 42 00            cmp qword ptr [rip + 0x429eca], r12
00AE2366  74 0E                           je 0x140ae2376
00AE2368  33 D2                           xor edx, edx
00AE236A  48 8D 0D BF 9E 42 00            lea rcx, [rip + 0x429ebf]
00AE2371  E8 6A 1C 7C FF                  call 0x1402a3fe0
00AE2376  B8 00 00 00 80                  mov eax, 0x80000000
00AE237B  F0 44 0F B1 25 D4 6C 42 00      lock cmpxchg dword ptr [rip + 0x426cd4], r12d
00AE2384  3D 00 00 00 80                  cmp eax, 0x80000000
00AE2389  74 15                           je 0x140ae23a0
00AE238B  8B 45 80                        mov eax, dword ptr [rbp - 0x80]
00AE238E  41 BF 01 00 00 00               mov r15d, 1
00AE2394  E9 6E F4 FF FF                  jmp 0x140ae1807
00AE2399  B9 03 00 00 00                  mov ecx, 3
00AE239E  CD 29                           int 0x29
00AE23A0  48 8B 3D A9 9C 42 00            mov rdi, qword ptr [rip + 0x429ca9]
00AE23A7  48 8D 05 A2 9C 42 00            lea rax, [rip + 0x429ca2]
00AE23AE  48 3B F8                        cmp rdi, rax
00AE23B1  74 1E                           je 0x140ae23d1
00AE23B3  48 8D 35 96 9C 42 00            lea rsi, [rip + 0x429c96]
00AE23BA  48 8D 4F C0                     lea rcx, [rdi - 0x40]
00AE23BE  33 D2                           xor edx, edx
00AE23C0  E8 8B F0 FF FF                  call 0x140ae1450
00AE23C5  48 8B 3F                        mov rdi, qword ptr [rdi]
00AE23C8  48 3B FE                        cmp rdi, rsi
00AE23CB  75 ED                           jne 0x140ae23ba
00AE23CD  8B 74 24 7C                     mov esi, dword ptr [rsp + 0x7c]
00AE23D1  48 85 DB                        test rbx, rbx
00AE23D4  74 18                           je 0x140ae23ee
00AE23D6  8B 83 80 00 00 00               mov eax, dword ptr [rbx + 0x80]
00AE23DC  41 2B C5                        sub eax, r13d
00AE23DF  41 3B C5                        cmp eax, r13d
00AE23E2  77 0A                           ja 0x140ae23ee
00AE23E4  33 D2                           xor edx, edx
00AE23E6  48 8B CB                        mov rcx, rbx
00AE23E9  E8 56 58 C8 FF                  call 0x140767c44
00AE23EE  44 39 25 CB 54 38 00            cmp dword ptr [rip + 0x3854cb], r12d
00AE23F5  BF 08 00 00 00                  mov edi, 8
00AE23FA  75 25                           jne 0x140ae2421
00AE23FC  44 89 64 24 30                  mov dword ptr [rsp + 0x30], r12d
00AE2401  48 8D 55 B8                     lea rdx, [rbp - 0x48]
00AE2405  44 89 64 24 28                  mov dword ptr [rsp + 0x28], r12d
00AE240A  48 8D 0D B7 E6 53 FF            lea rcx, [rip - 0xac1949]
00AE2411  45 33 C9                        xor r9d, r9d
00AE2414  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
00AE2419  44 8B C7                        mov r8d, edi
00AE241C  E8 EF E8 BC FF                  call 0x1406b0d10
00AE2421  44 39 25 8C 54 38 00            cmp dword ptr [rip + 0x38548c], r12d
00AE2428  75 3D                           jne 0x140ae2467
00AE242A  E8 C1 6F FB FF                  call 0x140a993f0
00AE242F  8A D8                           mov bl, al
00AE2431  83 FE FF                        cmp esi, -1
00AE2434  74 0A                           je 0x140ae2440
00AE2436  84 C0                           test al, al
00AE2438  75 06                           jne 0x140ae2440
00AE243A  8B CE                           mov ecx, esi
00AE243C  48 89 4D C0                     mov qword ptr [rbp - 0x40], rcx
00AE2440  44 89 64 24 30                  mov dword ptr [rsp + 0x30], r12d
00AE2445  48 8D 55 C0                     lea rdx, [rbp - 0x40]
00AE2449  44 89 64 24 28                  mov dword ptr [rsp + 0x28], r12d
00AE244E  48 8D 0D 03 E6 53 FF            lea rcx, [rip - 0xac19fd]
00AE2455  45 33 C9                        xor r9d, r9d
00AE2458  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
00AE245D  44 8B C7                        mov r8d, edi
00AE2460  E8 AB E8 BC FF                  call 0x1406b0d10
00AE2465  EB 04                           jmp 0x140ae246b
00AE2467  8A 5C 24 51                     mov bl, byte ptr [rsp + 0x51]
00AE246B  83 3D D6 52 32 00 05            cmp dword ptr [rip + 0x3252d6], 5
00AE2472  0F 86 DF 00 00 00               jbe 0x140ae2557
00AE2478  8B 05 42 54 38 00               mov eax, dword ptr [rip + 0x385442]
00AE247E  48 8D 15 D6 BB 56 FF            lea rdx, [rip - 0xa9442a]
00AE2485  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
00AE2489  48 8D 0D B8 52 32 00            lea rcx, [rip + 0x3252b8]
00AE2490  48 8D 44 24 64                  lea rax, [rsp + 0x64]
00AE2495  48 C7 85 B8 02 00 00 04 00 00 00  mov qword ptr [rbp + 0x2b8], 4
00AE24A0  48 89 85 B0 02 00 00            mov qword ptr [rbp + 0x2b0], rax
00AE24A7  45 33 C9                        xor r9d, r9d
00AE24AA  48 8B 45 B8                     mov rax, qword ptr [rbp - 0x48]
00AE24AE  45 33 C0                        xor r8d, r8d
00AE24B1  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
00AE24B6  48 8D 44 24 70                  lea rax, [rsp + 0x70]
00AE24BB  48 89 85 C0 02 00 00            mov qword ptr [rbp + 0x2c0], rax
00AE24C2  8B 05 EC 53 38 00               mov eax, dword ptr [rip + 0x3853ec]
00AE24C8  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
00AE24CC  48 8D 44 24 58                  lea rax, [rsp + 0x58]
00AE24D1  48 89 85 D0 02 00 00            mov qword ptr [rbp + 0x2d0], rax
00AE24D8  48 8D 44 24 78                  lea rax, [rsp + 0x78]
00AE24DD  48 89 85 E0 02 00 00            mov qword ptr [rbp + 0x2e0], rax
00AE24E4  48 8B 45 C0                     mov rax, qword ptr [rbp - 0x40]
00AE24E8  48 89 45 88                     mov qword ptr [rbp - 0x78], rax
00AE24EC  48 8D 45 88                     lea rax, [rbp - 0x78]
00AE24F0  48 89 85 F0 02 00 00            mov qword ptr [rbp + 0x2f0], rax
00AE24F7  48 8D 44 24 51                  lea rax, [rsp + 0x51]
00AE24FC  48 89 85 00 03 00 00            mov qword ptr [rbp + 0x300], rax
00AE2503  48 8D 85 90 02 00 00            lea rax, [rbp + 0x290]
00AE250A  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE250F  89 7C 24 20                     mov dword ptr [rsp + 0x20], edi
00AE2513  48 C7 85 C8 02 00 00 08 00 00 00  mov qword ptr [rbp + 0x2c8], 8
00AE251E  48 C7 85 D8 02 00 00 04 00 00 00  mov qword ptr [rbp + 0x2d8], 4
00AE2529  89 74 24 78                     mov dword ptr [rsp + 0x78], esi
00AE252D  48 C7 85 E8 02 00 00 04 00 00 00  mov qword ptr [rbp + 0x2e8], 4
00AE2538  48 C7 85 F8 02 00 00 08 00 00 00  mov qword ptr [rbp + 0x2f8], 8
00AE2543  88 5C 24 51                     mov byte ptr [rsp + 0x51], bl
00AE2547  48 C7 85 08 03 00 00 01 00 00 00  mov qword ptr [rbp + 0x308], 1
00AE2552  E8 89 3B 94 FF                  call 0x1404260e0
00AE2557  8B 74 24 54                     mov esi, dword ptr [rsp + 0x54]
00AE255B  40 08 75 80                     or byte ptr [rbp - 0x80], sil
00AE255F  0F 84 76 07 00 00               je 0x140ae2cdb
00AE2565  0F 10 05 24 9B 42 00            movups xmm0, xmmword ptr [rip + 0x429b24]
00AE256C  8B 05 3E 9B 42 00               mov eax, dword ptr [rip + 0x429b3e]
00AE2572  48 8D 95 C8 00 00 00            lea rdx, [rbp + 0xc8]
00AE2579  0F 10 0D 20 9B 42 00            movups xmm1, xmmword ptr [rip + 0x429b20]
00AE2580  89 85 E8 00 00 00               mov dword ptr [rbp + 0xe8], eax
00AE2586  48 8D 0D F3 E3 53 FF            lea rcx, [rip - 0xac1c0d]
00AE258D  8B 05 9D 9A 42 00               mov eax, dword ptr [rip + 0x429a9d]
00AE2593  45 33 C9                        xor r9d, r9d
00AE2596  0F 11 85 C8 00 00 00            movups xmmword ptr [rbp + 0xc8], xmm0
00AE259D  89 85 00 01 00 00               mov dword ptr [rbp + 0x100], eax
00AE25A3  0F 10 05 B6 9A 42 00            movups xmm0, xmmword ptr [rip + 0x429ab6]
00AE25AA  8B 05 84 9A 42 00               mov eax, dword ptr [rip + 0x429a84]
00AE25B0  45 8D 41 3C                     lea r8d, [r9 + 0x3c]
00AE25B4  44 89 64 24 30                  mov dword ptr [rsp + 0x30], r12d
00AE25B9  44 89 64 24 28                  mov dword ptr [rsp + 0x28], r12d
00AE25BE  F3 0F 7F 85 EC 00 00 00         movdqu xmmword ptr [rbp + 0xec], xmm0
00AE25C6  89 85 FC 00 00 00               mov dword ptr [rbp + 0xfc], eax
00AE25CC  0F 11 8D D8 00 00 00            movups xmmword ptr [rbp + 0xd8], xmm1
00AE25D3  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
00AE25D8  E8 33 E7 BC FF                  call 0x1406b0d10
00AE25DD  8B D8                           mov ebx, eax
00AE25DF  E8 A0 6E AF FF                  call 0x1405d9484
00AE25E4  85 C0                           test eax, eax
00AE25E6  0F 85 F7 02 00 00               jne 0x140ae28e3
00AE25EC  83 3D 55 51 32 00 05            cmp dword ptr [rip + 0x325155], 5
00AE25F3  0F 86 17 06 00 00               jbe 0x140ae2c10
00AE25F9  48 BA 00 00 00 00 00 40 00 00   movabs rdx, 0x400000000000
00AE2603  48 8D 0D 3E 51 32 00            lea rcx, [rip + 0x32513e]
00AE260A  E8 91 C4 94 FF                  call 0x14042eaa0
00AE260F  84 C0                           test al, al
00AE2611  0F 84 F9 05 00 00               je 0x140ae2c10
00AE2617  44 8B 05 42 9A 42 00            mov r8d, dword ptr [rip + 0x429a42]
00AE261E  48 8D 44 24 78                  lea rax, [rsp + 0x78]
00AE2623  44 8B 0D 0A 9A 42 00            mov r9d, dword ptr [rip + 0x429a0a]
00AE262A  48 8D 15 EF 03 02 00            lea rdx, [rip + 0x203ef]
00AE2631  48 89 85 30 01 00 00            mov qword ptr [rbp + 0x130], rax
00AE2638  48 8D 8D 40 01 00 00            lea rcx, [rbp + 0x140]
00AE263F  48 8D 05 1A 04 02 00            lea rax, [rip + 0x2041a]
00AE2646  44 89 4C 24 78                  mov dword ptr [rsp + 0x78], r9d
00AE264B  45 84 C5                        test r13b, r8b
00AE264E  48 C7 85 38 01 00 00 04 00 00 00  mov qword ptr [rbp + 0x138], 4
00AE2659  48 0F 44 D0                     cmove rdx, rax
00AE265D  E8 A2 4C 94 FF                  call 0x140427304
00AE2662  41 F6 C0 02                     test r8b, 2
00AE2666  48 8D 15 D3 03 02 00            lea rdx, [rip + 0x203d3]
00AE266D  4C 8D 15 3C 02 02 00            lea r10, [rip + 0x2023c]
00AE2674  49 0F 44 D2                     cmove rdx, r10
00AE2678  48 8D 8D 50 01 00 00            lea rcx, [rbp + 0x150]
00AE267F  E8 80 4C 94 FF                  call 0x140427304
00AE2684  45 84 C7                        test r15b, r8b
00AE2687  48 8D 15 02 04 02 00            lea rdx, [rip + 0x20402]
00AE268E  48 8D 8D 60 01 00 00            lea rcx, [rbp + 0x160]
00AE2695  49 0F 44 D2                     cmove rdx, r10
00AE2699  E8 66 4C 94 FF                  call 0x140427304
00AE269E  44 84 C7                        test dil, r8b
00AE26A1  48 8D 15 C8 03 02 00            lea rdx, [rip + 0x203c8]
00AE26A8  48 8D 8D 70 01 00 00            lea rcx, [rbp + 0x170]
00AE26AF  49 0F 44 D2                     cmove rdx, r10
00AE26B3  E8 4C 4C 94 FF                  call 0x140427304
00AE26B8  B8 10 00 00 00                  mov eax, 0x10
00AE26BD  48 8D 15 1C 04 02 00            lea rdx, [rip + 0x2041c]
00AE26C4  44 84 C0                        test al, r8b
00AE26C7  48 8D 8D 80 01 00 00            lea rcx, [rbp + 0x180]
00AE26CE  49 0F 44 D2                     cmove rdx, r10
00AE26D2  E8 2D 4C 94 FF                  call 0x140427304
00AE26D7  41 F6 C0 20                     test r8b, 0x20
00AE26DB  48 8D 15 CE 03 02 00            lea rdx, [rip + 0x203ce]
00AE26E2  48 8D 8D 90 01 00 00            lea rcx, [rbp + 0x190]
00AE26E9  49 0F 44 D2                     cmove rdx, r10
00AE26ED  E8 12 4C 94 FF                  call 0x140427304
00AE26F2  41 F6 C0 40                     test r8b, 0x40
00AE26F6  48 8D 15 93 02 02 00            lea rdx, [rip + 0x20293]
00AE26FD  48 8D 8D A0 01 00 00            lea rcx, [rbp + 0x1a0]
00AE2704  49 0F 44 D2                     cmove rdx, r10
00AE2708  E8 F7 4B 94 FF                  call 0x140427304
00AE270D  41 F6 C0 80                     test r8b, 0x80
00AE2711  48 8D 15 58 02 02 00            lea rdx, [rip + 0x20258]
00AE2718  48 8D 8D B0 01 00 00            lea rcx, [rbp + 0x1b0]
00AE271F  49 0F 44 D2                     cmove rdx, r10
00AE2723  E8 DC 4B 94 FF                  call 0x140427304
00AE2728  44 84 2D 91 9B 42 00            test byte ptr [rip + 0x429b91], r13b
00AE272F  48 8D 15 9A 02 02 00            lea rdx, [rip + 0x2029a]
00AE2736  48 8D 8D C0 01 00 00            lea rcx, [rbp + 0x1c0]
00AE273D  49 0F 44 D2                     cmove rdx, r10
00AE2741  E8 BE 4B 94 FF                  call 0x140427304
00AE2746  44 8B 05 53 99 42 00            mov r8d, dword ptr [rip + 0x429953]
00AE274D  45 85 C0                        test r8d, r8d
00AE2750  75 05                           jne 0x140ae2757
00AE2752  41 8B C4                        mov eax, r12d
00AE2755  EB 13                           jmp 0x140ae276a
00AE2757  6B 05 06 99 42 00 64            imul eax, dword ptr [rip + 0x429906], 0x64
00AE275E  41 8B C8                        mov ecx, r8d
00AE2761  D1 E9                           shr ecx, 1
00AE2763  33 D2                           xor edx, edx
00AE2765  03 C1                           add eax, ecx
00AE2767  41 F7 F0                        div r8d
00AE276A  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
00AE276E  48 8D 44 24 64                  lea rax, [rsp + 0x64]
00AE2773  48 89 85 D0 01 00 00            mov qword ptr [rbp + 0x1d0], rax
00AE277A  48 C7 85 D8 01 00 00 04 00 00 00  mov qword ptr [rbp + 0x1d8], 4
00AE2785  45 85 C0                        test r8d, r8d
00AE2788  75 05                           jne 0x140ae278f
00AE278A  41 8B C4                        mov eax, r12d
00AE278D  EB 12                           jmp 0x140ae27a1
00AE278F  8B 05 CF 98 42 00               mov eax, dword ptr [rip + 0x4298cf]
00AE2795  33 D2                           xor edx, edx
00AE2797  48 69 C0 A0 86 01 00            imul rax, rax, 0x186a0
00AE279E  49 F7 F0                        div r8
00AE27A1  F7 05 E5 98 42 00 00 00 00 40   test dword ptr [rip + 0x4298e5], 0x40000000
00AE27AB  48 8D 15 4E 02 02 00            lea rdx, [rip + 0x2024e]
00AE27B2  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
00AE27B6  48 8D 8D 50 02 00 00            lea rcx, [rbp + 0x250]
00AE27BD  48 8D 44 24 58                  lea rax, [rsp + 0x58]
00AE27C2  48 C7 85 E8 01 00 00 04 00 00 00  mov qword ptr [rbp + 0x1e8], 4
00AE27CD  48 89 85 E0 01 00 00            mov qword ptr [rbp + 0x1e0], rax
00AE27D4  8B 05 8A 98 42 00               mov eax, dword ptr [rip + 0x42988a]
00AE27DA  89 45 A4                        mov dword ptr [rbp - 0x5c], eax
00AE27DD  48 8D 45 A4                     lea rax, [rbp - 0x5c]
00AE27E1  48 89 85 F0 01 00 00            mov qword ptr [rbp + 0x1f0], rax
00AE27E8  48 8D 45 A8                     lea rax, [rbp - 0x58]
00AE27EC  48 89 85 00 02 00 00            mov qword ptr [rbp + 0x200], rax
00AE27F3  8B 05 6F 98 42 00               mov eax, dword ptr [rip + 0x42986f]
00AE27F9  89 45 94                        mov dword ptr [rbp - 0x6c], eax
00AE27FC  48 8D 45 94                     lea rax, [rbp - 0x6c]
00AE2800  48 89 85 10 02 00 00            mov qword ptr [rbp + 0x210], rax
00AE2807  8B 05 5F 98 42 00               mov eax, dword ptr [rip + 0x42985f]
00AE280D  89 45 98                        mov dword ptr [rbp - 0x68], eax
00AE2810  48 8D 45 98                     lea rax, [rbp - 0x68]
00AE2814  48 89 85 20 02 00 00            mov qword ptr [rbp + 0x220], rax
00AE281B  8B 05 0F 98 42 00               mov eax, dword ptr [rip + 0x42980f]
00AE2821  89 45 9C                        mov dword ptr [rbp - 0x64], eax
00AE2824  48 8D 45 9C                     lea rax, [rbp - 0x64]
00AE2828  48 89 85 30 02 00 00            mov qword ptr [rbp + 0x230], rax
00AE282F  48 8D 45 A0                     lea rax, [rbp - 0x60]
00AE2833  48 89 85 40 02 00 00            mov qword ptr [rbp + 0x240], rax
00AE283A  48 8D 05 AF 01 02 00            lea rax, [rip + 0x201af]
00AE2841  48 0F 44 D0                     cmove rdx, rax
00AE2845  48 C7 85 F8 01 00 00 04 00 00 00  mov qword ptr [rbp + 0x1f8], 4
00AE2850  44 89 45 A8                     mov dword ptr [rbp - 0x58], r8d
00AE2854  48 C7 85 08 02 00 00 04 00 00 00  mov qword ptr [rbp + 0x208], 4
00AE285F  48 C7 85 18 02 00 00 04 00 00 00  mov qword ptr [rbp + 0x218], 4
00AE286A  48 C7 85 28 02 00 00 04 00 00 00  mov qword ptr [rbp + 0x228], 4
00AE2875  48 C7 85 38 02 00 00 04 00 00 00  mov qword ptr [rbp + 0x238], 4
00AE2880  44 89 4D A0                     mov dword ptr [rbp - 0x60], r9d
00AE2884  48 C7 85 48 02 00 00 04 00 00 00  mov qword ptr [rbp + 0x248], 4
00AE288F  E8 70 4A 94 FF                  call 0x140427304
00AE2894  8B 0D 02 98 42 00               mov ecx, dword ptr [rip + 0x429802]
00AE289A  48 8D 45 88                     lea rax, [rbp - 0x78]
00AE289E  48 89 85 60 02 00 00            mov qword ptr [rbp + 0x260], rax
00AE28A5  48 8D 15 92 B5 56 FF            lea rdx, [rip - 0xa94a6e]
00AE28AC  48 8D 44 24 70                  lea rax, [rsp + 0x70]
00AE28B1  89 4D 88                        mov dword ptr [rbp - 0x78], ecx
00AE28B4  48 89 85 70 02 00 00            mov qword ptr [rbp + 0x270], rax
00AE28BB  48 8D 85 10 01 00 00            lea rax, [rbp + 0x110]
00AE28C2  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE28C7  C7 44 24 20 17 00 00 00         mov dword ptr [rsp + 0x20], 0x17
00AE28CF  48 C7 85 68 02 00 00 04 00 00 00  mov qword ptr [rbp + 0x268], 4
00AE28DA  89 5C 24 70                     mov dword ptr [rsp + 0x70], ebx
00AE28DE  E9 10 03 00 00                  jmp 0x140ae2bf3
00AE28E3  83 3D 5E 4E 32 00 05            cmp dword ptr [rip + 0x324e5e], 5
00AE28EA  0F 86 20 03 00 00               jbe 0x140ae2c10
00AE28F0  48 BA 00 00 00 00 00 40 00 00   movabs rdx, 0x400000000000
00AE28FA  48 8D 0D 47 4E 32 00            lea rcx, [rip + 0x324e47]
00AE2901  E8 9A C1 94 FF                  call 0x14042eaa0
00AE2906  84 C0                           test al, al
00AE2908  0F 84 02 03 00 00               je 0x140ae2c10
00AE290E  44 8B 05 4B 97 42 00            mov r8d, dword ptr [rip + 0x42974b]
00AE2915  48 8D 44 24 70                  lea rax, [rsp + 0x70]
00AE291A  44 8B 0D 13 97 42 00            mov r9d, dword ptr [rip + 0x429713]
00AE2921  48 8D 15 F8 00 02 00            lea rdx, [rip + 0x200f8]
00AE2928  48 89 85 30 01 00 00            mov qword ptr [rbp + 0x130], rax
00AE292F  48 8D 8D 40 01 00 00            lea rcx, [rbp + 0x140]
00AE2936  48 8D 05 23 01 02 00            lea rax, [rip + 0x20123]
00AE293D  44 89 4C 24 70                  mov dword ptr [rsp + 0x70], r9d
00AE2942  45 84 C5                        test r13b, r8b
00AE2945  48 C7 85 38 01 00 00 04 00 00 00  mov qword ptr [rbp + 0x138], 4
00AE2950  48 0F 44 D0                     cmove rdx, rax
00AE2954  E8 AB 49 94 FF                  call 0x140427304
00AE2959  41 F6 C0 02                     test r8b, 2
00AE295D  48 8D 15 DC 00 02 00            lea rdx, [rip + 0x200dc]
00AE2964  4C 8D 15 45 FF 01 00            lea r10, [rip + 0x1ff45]
00AE296B  49 0F 44 D2                     cmove rdx, r10
00AE296F  48 8D 8D 50 01 00 00            lea rcx, [rbp + 0x150]
00AE2976  E8 89 49 94 FF                  call 0x140427304
00AE297B  45 84 C7                        test r15b, r8b
00AE297E  48 8D 15 0B 01 02 00            lea rdx, [rip + 0x2010b]
00AE2985  48 8D 8D 60 01 00 00            lea rcx, [rbp + 0x160]
00AE298C  49 0F 44 D2                     cmove rdx, r10
00AE2990  E8 6F 49 94 FF                  call 0x140427304
00AE2995  44 84 C7                        test dil, r8b
00AE2998  48 8D 15 D1 00 02 00            lea rdx, [rip + 0x200d1]
00AE299F  48 8D 8D 70 01 00 00            lea rcx, [rbp + 0x170]
00AE29A6  49 0F 44 D2                     cmove rdx, r10
00AE29AA  E8 55 49 94 FF                  call 0x140427304
00AE29AF  B8 10 00 00 00                  mov eax, 0x10
00AE29B4  48 8D 15 25 01 02 00            lea rdx, [rip + 0x20125]
00AE29BB  44 84 C0                        test al, r8b
00AE29BE  48 8D 8D 80 01 00 00            lea rcx, [rbp + 0x180]
00AE29C5  49 0F 44 D2                     cmove rdx, r10
00AE29C9  E8 36 49 94 FF                  call 0x140427304
00AE29CE  41 F6 C0 20                     test r8b, 0x20
00AE29D2  48 8D 15 D7 00 02 00            lea rdx, [rip + 0x200d7]
00AE29D9  48 8D 8D 90 01 00 00            lea rcx, [rbp + 0x190]
00AE29E0  49 0F 44 D2                     cmove rdx, r10
00AE29E4  E8 1B 49 94 FF                  call 0x140427304
00AE29E9  41 F6 C0 40                     test r8b, 0x40
00AE29ED  48 8D 15 9C FF 01 00            lea rdx, [rip + 0x1ff9c]
00AE29F4  48 8D 8D A0 01 00 00            lea rcx, [rbp + 0x1a0]
00AE29FB  49 0F 44 D2                     cmove rdx, r10
00AE29FF  E8 00 49 94 FF                  call 0x140427304
00AE2A04  41 F6 C0 80                     test r8b, 0x80
00AE2A08  48 8D 15 61 FF 01 00            lea rdx, [rip + 0x1ff61]
00AE2A0F  48 8D 8D B0 01 00 00            lea rcx, [rbp + 0x1b0]
00AE2A16  49 0F 44 D2                     cmove rdx, r10
00AE2A1A  E8 E5 48 94 FF                  call 0x140427304
00AE2A1F  44 84 2D 9A 98 42 00            test byte ptr [rip + 0x42989a], r13b
00AE2A26  48 8D 15 A3 FF 01 00            lea rdx, [rip + 0x1ffa3]
00AE2A2D  48 8D 8D C0 01 00 00            lea rcx, [rbp + 0x1c0]
00AE2A34  49 0F 44 D2                     cmove rdx, r10
00AE2A38  E8 C7 48 94 FF                  call 0x140427304
00AE2A3D  44 84 2D 7D 98 42 00            test byte ptr [rip + 0x42987d], r13b
00AE2A44  48 8D 15 65 FF 01 00            lea rdx, [rip + 0x1ff65]
00AE2A4B  48 8D 8D D0 01 00 00            lea rcx, [rbp + 0x1d0]
00AE2A52  49 0F 44 D2                     cmove rdx, r10
00AE2A56  E8 A9 48 94 FF                  call 0x140427304
00AE2A5B  44 8B 05 3E 96 42 00            mov r8d, dword ptr [rip + 0x42963e]
00AE2A62  45 85 C0                        test r8d, r8d
00AE2A65  75 05                           jne 0x140ae2a6c
00AE2A67  41 8B C4                        mov eax, r12d
00AE2A6A  EB 13                           jmp 0x140ae2a7f
00AE2A6C  6B 05 F1 95 42 00 64            imul eax, dword ptr [rip + 0x4295f1], 0x64
00AE2A73  41 8B C8                        mov ecx, r8d
00AE2A76  D1 E9                           shr ecx, 1
00AE2A78  33 D2                           xor edx, edx
00AE2A7A  03 C1                           add eax, ecx
00AE2A7C  41 F7 F0                        div r8d
00AE2A7F  89 45 88                        mov dword ptr [rbp - 0x78], eax
00AE2A82  48 8D 45 88                     lea rax, [rbp - 0x78]
00AE2A86  48 89 85 E0 01 00 00            mov qword ptr [rbp + 0x1e0], rax
00AE2A8D  48 C7 85 E8 01 00 00 04 00 00 00  mov qword ptr [rbp + 0x1e8], 4
00AE2A98  45 85 C0                        test r8d, r8d
00AE2A9B  75 05                           jne 0x140ae2aa2
00AE2A9D  41 8B C4                        mov eax, r12d
00AE2AA0  EB 12                           jmp 0x140ae2ab4
00AE2AA2  8B 05 BC 95 42 00               mov eax, dword ptr [rip + 0x4295bc]
00AE2AA8  33 D2                           xor edx, edx
00AE2AAA  48 69 C0 A0 86 01 00            imul rax, rax, 0x186a0
00AE2AB1  49 F7 F0                        div r8
00AE2AB4  F7 05 D2 95 42 00 00 00 00 40   test dword ptr [rip + 0x4295d2], 0x40000000
00AE2ABE  48 8D 15 3B FF 01 00            lea rdx, [rip + 0x1ff3b]
00AE2AC5  89 45 A0                        mov dword ptr [rbp - 0x60], eax
00AE2AC8  48 8D 8D 60 02 00 00            lea rcx, [rbp + 0x260]
00AE2ACF  48 8D 45 A0                     lea rax, [rbp - 0x60]
00AE2AD3  48 C7 85 F8 01 00 00 04 00 00 00  mov qword ptr [rbp + 0x1f8], 4
00AE2ADE  48 89 85 F0 01 00 00            mov qword ptr [rbp + 0x1f0], rax
00AE2AE5  8B 05 79 95 42 00               mov eax, dword ptr [rip + 0x429579]
00AE2AEB  89 45 9C                        mov dword ptr [rbp - 0x64], eax
00AE2AEE  48 8D 45 9C                     lea rax, [rbp - 0x64]
00AE2AF2  48 89 85 00 02 00 00            mov qword ptr [rbp + 0x200], rax
00AE2AF9  48 8D 45 98                     lea rax, [rbp - 0x68]
00AE2AFD  48 89 85 10 02 00 00            mov qword ptr [rbp + 0x210], rax
00AE2B04  8B 05 5E 95 42 00               mov eax, dword ptr [rip + 0x42955e]
00AE2B0A  89 45 94                        mov dword ptr [rbp - 0x6c], eax
00AE2B0D  48 8D 45 94                     lea rax, [rbp - 0x6c]
00AE2B11  48 89 85 20 02 00 00            mov qword ptr [rbp + 0x220], rax
00AE2B18  8B 05 4E 95 42 00               mov eax, dword ptr [rip + 0x42954e]
00AE2B1E  89 45 A8                        mov dword ptr [rbp - 0x58], eax
00AE2B21  48 8D 45 A8                     lea rax, [rbp - 0x58]
00AE2B25  48 89 85 30 02 00 00            mov qword ptr [rbp + 0x230], rax
00AE2B2C  8B 05 FE 94 42 00               mov eax, dword ptr [rip + 0x4294fe]
00AE2B32  89 45 A4                        mov dword ptr [rbp - 0x5c], eax
00AE2B35  48 8D 45 A4                     lea rax, [rbp - 0x5c]
00AE2B39  48 89 85 40 02 00 00            mov qword ptr [rbp + 0x240], rax
00AE2B40  48 8D 44 24 78                  lea rax, [rsp + 0x78]
00AE2B45  48 89 85 50 02 00 00            mov qword ptr [rbp + 0x250], rax
00AE2B4C  48 8D 05 9D FE 01 00            lea rax, [rip + 0x1fe9d]
00AE2B53  48 0F 44 D0                     cmove rdx, rax
00AE2B57  48 C7 85 08 02 00 00 04 00 00 00  mov qword ptr [rbp + 0x208], 4
00AE2B62  44 89 45 98                     mov dword ptr [rbp - 0x68], r8d
00AE2B66  48 C7 85 18 02 00 00 04 00 00 00  mov qword ptr [rbp + 0x218], 4
00AE2B71  48 C7 85 28 02 00 00 04 00 00 00  mov qword ptr [rbp + 0x228], 4
00AE2B7C  48 C7 85 38 02 00 00 04 00 00 00  mov qword ptr [rbp + 0x238], 4
00AE2B87  48 C7 85 48 02 00 00 04 00 00 00  mov qword ptr [rbp + 0x248], 4
00AE2B92  44 89 4C 24 78                  mov dword ptr [rsp + 0x78], r9d
00AE2B97  48 C7 85 58 02 00 00 04 00 00 00  mov qword ptr [rbp + 0x258], 4
00AE2BA2  E8 5D 47 94 FF                  call 0x140427304
00AE2BA7  8B 0D EF 94 42 00               mov ecx, dword ptr [rip + 0x4294ef]
00AE2BAD  48 8D 44 24 64                  lea rax, [rsp + 0x64]
00AE2BB2  48 89 85 70 02 00 00            mov qword ptr [rbp + 0x270], rax
00AE2BB9  48 8D 15 49 B0 56 FF            lea rdx, [rip - 0xa94fb7]
00AE2BC0  48 8D 44 24 58                  lea rax, [rsp + 0x58]
00AE2BC5  89 4C 24 64                     mov dword ptr [rsp + 0x64], ecx
00AE2BC9  48 89 85 80 02 00 00            mov qword ptr [rbp + 0x280], rax
00AE2BD0  48 8D 85 10 01 00 00            lea rax, [rbp + 0x110]
00AE2BD7  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE2BDC  C7 44 24 20 18 00 00 00         mov dword ptr [rsp + 0x20], 0x18
00AE2BE4  89 5C 24 58                     mov dword ptr [rsp + 0x58], ebx
00AE2BE8  48 C7 85 88 02 00 00 04 00 00 00  mov qword ptr [rbp + 0x288], 4
00AE2BF3  45 33 C9                        xor r9d, r9d
00AE2BF6  48 C7 85 78 02 00 00 04 00 00 00  mov qword ptr [rbp + 0x278], 4
00AE2C01  45 33 C0                        xor r8d, r8d
00AE2C04  48 8D 0D 3D 4B 32 00            lea rcx, [rip + 0x324b3d]
00AE2C0B  E8 D0 34 94 FF                  call 0x1404260e0
00AE2C10  44 39 6C 24 60                  cmp dword ptr [rsp + 0x60], r13d
00AE2C15  75 41                           jne 0x140ae2c58
00AE2C17  45 84 F6                        test r14b, r14b
00AE2C1A  75 13                           jne 0x140ae2c2f
00AE2C1C  48 B8 14 00 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000014
00AE2C26  48 8B 00                        mov rax, qword ptr [rax]
00AE2C29  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
00AE2C2D  EB 04                           jmp 0x140ae2c33
00AE2C2F  4C 89 65 E8                     mov qword ptr [rbp - 0x18], r12
00AE2C33  44 89 64 24 30                  mov dword ptr [rsp + 0x30], r12d
00AE2C38  48 8D 55 E8                     lea rdx, [rbp - 0x18]
00AE2C3C  44 89 64 24 28                  mov dword ptr [rsp + 0x28], r12d
00AE2C41  48 8D 0D F8 94 53 FF            lea rcx, [rip - 0xac6b08]
00AE2C48  45 33 C9                        xor r9d, r9d
00AE2C4B  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
00AE2C50  44 8B C7                        mov r8d, edi
00AE2C53  E8 B8 E0 BC FF                  call 0x1406b0d10
00AE2C58  40 84 F6                        test sil, sil
00AE2C5B  74 7E                           je 0x140ae2cdb
00AE2C5D  44 89 64 24 30                  mov dword ptr [rsp + 0x30], r12d
00AE2C62  48 8D 55 E0                     lea rdx, [rbp - 0x20]
00AE2C66  4C 89 65 E0                     mov qword ptr [rbp - 0x20], r12
00AE2C6A  48 8D 0D 17 DC 53 FF            lea rcx, [rip - 0xac23e9]
00AE2C71  83 4D E4 FF                     or dword ptr [rbp - 0x1c], 0xffffffff
00AE2C75  45 33 C9                        xor r9d, r9d
00AE2C78  44 89 64 24 28                  mov dword ptr [rsp + 0x28], r12d
00AE2C7D  44 8B C7                        mov r8d, edi
00AE2C80  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
00AE2C85  E8 86 E0 BC FF                  call 0x1406b0d10
00AE2C8A  83 3D B7 4A 32 00 05            cmp dword ptr [rip + 0x324ab7], 5
00AE2C91  76 48                           jbe 0x140ae2cdb
00AE2C93  89 44 24 70                     mov dword ptr [rsp + 0x70], eax
00AE2C97  48 8D 15 7E AB 56 FF            lea rdx, [rip - 0xa95482]
00AE2C9E  48 8D 44 24 70                  lea rax, [rsp + 0x70]
00AE2CA3  48 C7 85 D8 03 00 00 04 00 00 00  mov qword ptr [rbp + 0x3d8], 4
00AE2CAE  48 89 85 D0 03 00 00            mov qword ptr [rbp + 0x3d0], rax
00AE2CB5  48 8D 0D 8C 4A 32 00            lea rcx, [rip + 0x324a8c]
00AE2CBC  48 8D 85 B0 03 00 00            lea rax, [rbp + 0x3b0]
00AE2CC3  45 33 C9                        xor r9d, r9d
00AE2CC6  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE2CCB  45 33 C0                        xor r8d, r8d
00AE2CCE  C7 44 24 20 03 00 00 00         mov dword ptr [rsp + 0x20], 3
00AE2CD6  E8 05 34 94 FF                  call 0x1404260e0
00AE2CDB  48 8D 0D 3E 93 42 00            lea rcx, [rip + 0x42933e]
00AE2CE2  E8 D5 CE 7F FF                  call 0x1402dfbbc
00AE2CE7  48 8D 0D 12 9C 42 00            lea rcx, [rip + 0x429c12]
00AE2CEE  E8 C9 CE 7F FF                  call 0x1402dfbbc
00AE2CF3  48 8B 8D E0 03 00 00            mov rcx, qword ptr [rbp + 0x3e0]
00AE2CFA  48 33 CC                        xor rcx, rsp
00AE2CFD  E8 3E 99 BC FF                  call 0x1406ac640
00AE2D02  4C 8D 9C 24 20 05 00 00         lea r11, [rsp + 0x520]
00AE2D0A  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
00AE2D0E  49 8B 73 38                     mov rsi, qword ptr [r11 + 0x38]
00AE2D12  49 8B 7B 40                     mov rdi, qword ptr [r11 + 0x40]
00AE2D16  41 0F 28 73 F0                  movaps xmm6, xmmword ptr [r11 - 0x10]
00AE2D1B  41 0F 28 7B E0                  movaps xmm7, xmmword ptr [r11 - 0x20]
00AE2D20  45 0F 28 43 D0                  movaps xmm8, xmmword ptr [r11 - 0x30]
00AE2D25  49 8B E3                        mov rsp, r11
00AE2D28  41 5F                           pop r15
00AE2D2A  41 5E                           pop r14
00AE2D2C  41 5D                           pop r13
00AE2D2E  41 5C                           pop r12
00AE2D30  5D                              pop rbp
00AE2D31  C3                              ret
00AE2D32  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopBatteryWorker(__int64 a1, int a2, int a3)
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
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m4CC;
    unsigned __int64 v_stack_m4D0;
    unsigned __int64 v_stack_m4D8;
    unsigned int v_stack_m4DC;
    unsigned int v_stack_m4E0;
    unsigned __int64 v_stack_m4E4;
    unsigned int v_stack_m4E8;
    unsigned __int8 v_stack_m4EB;
    unsigned __int64 v_stack_m4EC;
    unsigned __int64 v_stack_m4F0;
    unsigned int v_stack_m4F4;
    unsigned __int8 v_stack_m4F7;
    unsigned __int8 v_stack_m4F8;
    unsigned int v_stack_m508;
    unsigned int v_stack_m510;
    unsigned int v_stack_m518;
    unsigned __int64 v_stack_m520;
    unsigned __int64 v_stack_m528;
    unsigned int v_stack_m548;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 24) = v_rdi;
    v_rsp = (v_rsp) - (0x520ULL);
    *(unsigned __int64 *)(v_rsp - 56) = v_xmm6;
    *(unsigned __int64 *)(v_rsp - 72) = v_xmm7;
    *(unsigned __int64 *)(v_rsp - 88) = v_xmm8;
    result = (*(unsigned __int64 *)(v_rip + 3313846)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 1096 + 992) = result;
    v_r12 = 0;
    *(unsigned __int64 *)(v_rsp - 1096 - 72) = 0;
    result = 0;
    *(unsigned __int64 *)(v_rsp - 1096 - 64) = 0;
    *(unsigned __int64 *)(v_rsp - 1096 - 32) = 0;
    v_stack_m4F8 = 0;
    *(unsigned __int64 *)(v_rsp - 1096 + 200) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 1096 + 248) = 0;
    *(unsigned __int64 *)(v_rsp - 1096 + 216) = v_xmm0;
    *(unsigned int *)(v_rsp - 1096 + 256) = 0;
    *(unsigned __int64 *)(v_rsp - 1096 + 232) = v_xmm0;
    result = PopAcquireRwLockShared(v_rip + 4371042, a2, a3, a4);
    result = PopAcquireRwLockExclusive(v_rip + 4368702, a2, a3, a4);
    *(unsigned __int64 *)(v_rsp - 1096 - 120) = 0;
    v_stack_m520 = v_stack_m4F0;
    v_stack_m4E4 = 0;
    a3 = 0;
    v_stack_m528 = v_rsp - 1096 - 120;
    a2 = 0;
    v_stack_m4F0 = 8;
    result = ZwQueryWnfStateData(v_rip - 11294172, a2, a3, v_stack_m4E4);
    if (((unsigned int)(result)) == 0xC000009AULL) goto loc_00AE175A;
    if (((unsigned int)(result)) == 0xC0000189ULL) goto loc_00AE175A;
    if ((unsigned int)(result) != 0) goto loc_00AE1753;
    if (v_stack_m4F0 != 8) goto loc_00AE1753;
    result = -(*(unsigned __int64 *)(v_rsp - 1096 - 120));
    result = (unsigned int)(-(result));
    result = (unsigned int)((result) + (2));
    v_stack_m4E8 = (unsigned int)(result);
    goto loc_00AE175F;
loc_00AE1753:
    v_stack_m4E8 = (unsigned int)(v_r12 + 1);
    goto loc_00AE175F;
loc_00AE175A:
    v_stack_m4E8 = 0;
loc_00AE175F:
    v_stack_m4D8 = *(unsigned __int64 *)(v_rip + 4369266);
    goto loc_00AE1787;
loc_00AE177B:
    result = IoCancelIrp(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4368604) - 8), a2, a3, v_stack_m4E4);
loc_00AE1787:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4368604))) != (v_rip + 4368611)) goto loc_00AE177B;
    if (*(unsigned __int64 *)(v_rip + 4369266) == 0) goto loc_00AE17A8;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 4369266) + 128))) - ((unsigned int)(v_r12 + 1)));
    if (((unsigned int)(result)) <= ((unsigned int)(v_r12 + 1))) {
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4369266) + 56);
        result = IoCancelIrp(a1, a2, a3, v_stack_m4E4);
    }
    goto loc_00AE17CA;
loc_00AE17B1:
    v_stack_m528 = 0;
    a4 = 0;
    a3 = 0;
    a2 = 0;
    result = KeWaitForSingleObject(*(unsigned __int64 *)(v_rip + 4368545) + 16, a2, a3, a4);
loc_00AE17CA:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4368545))) != (v_rip + 4368611)) goto loc_00AE17B1;
    if (*(unsigned __int64 *)(v_rip + 4369266) == 0) goto loc_00AE17F8;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 4369266) + 128))) - ((unsigned int)(v_r12 + 1)));
    if (((unsigned int)(result)) <= ((unsigned int)(v_r12 + 1))) {
        a1 = *(unsigned __int64 *)(v_rip + 4369266) + 104;
        v_stack_m528 = 0;
        a4 = 0;
        a3 = 0;
        a2 = 0;
        result = KeWaitForSingleObject(a1, a2, a3, a4);
    }
    v_stack_m4F7 = 0;
    v_stack_m4F4 = 0;
loc_00AE1807:
    v_stack_m4E0 = 0;
    v_stack_m4DC = 0;
    *(unsigned int *)(v_rsp - 1096 - 124) = (unsigned int)((unsigned int)(0x80000000ULL));
    v_r12 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(0x80000000ULL)))) >> (1));
    v_r12 = (unsigned __int8)((v_r12) & ((unsigned __int8)(v_r12 + 1)));
    result = 0;
    if ((((unsigned __int8)((unsigned int)(0x80000000ULL))) & (8)) != 0) { result = (unsigned int)(v_r12 + 1); }
    *(unsigned int *)(v_rsp - 1096 - 128) = (unsigned int)(result);
    if (((16) & ((unsigned __int8)((unsigned int)(0x80000000ULL)))) != 0) {
        result = PopAcquirePolicyLock(16, a2, a3, a4);
        a1 = 128;
        result = PopResetCBTriggers(a1, a2, a3, a4);
        result = PopReleasePolicyLock(a1, a2, a3, a4);
    }
    v_rsi = 0;
    a1 = (condition_is_below) ? 1 : 0;
    *(unsigned int *)(v_rsp - 1096 - 80) = (unsigned int)(a1);
    if (!sign_flag) goto loc_00AE189E;
    if (*(unsigned __int64 *)(v_rip + 4369266) == 0) goto loc_00AE189E;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 4369266) + 128))) - ((unsigned int)(v_r12 + 1)));
    v_r14 = 0;
    if (((unsigned int)(result)) <= ((unsigned int)(v_r12 + 1))) {
        v_r14 = 0;
        if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 4369266) + 140)) & ((unsigned __int8)(v_r12 + 1))) != 0) { v_r14 = (unsigned int)(v_r12 + 1); }
        v_stack_m4E0 = (unsigned int)(v_r14);
    }
    result = Feature_BatteryChargeLimitV2Support__private_IsEnabledDeviceUsageNoInline(a1, a2, a3, a4);
    v_rdi = 0;
    if ((unsigned int)(result) != 0) {
        v_rdi = 0;
        if (condition_is_below) { v_rdi = (unsigned int)(v_r12 + 1); }
        v_stack_m4DC = (unsigned int)(v_rdi);
    }
    if ((*(unsigned __int64 *)(v_rip + 4368273)) == (v_rip + 4368266)) goto loc_00AE1936;
loc_00AE18CB:
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rip + 4368273) - 64 + 104)) != 2) goto loc_00AE192C;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4368273)) + 8)) != (*(unsigned __int64 *)(v_rip + 4368273))) goto loc_00AE2399;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4368273) + 8))) != (*(unsigned __int64 *)(v_rip + 4368273))) goto loc_00AE2399;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4368273) + 8)) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4368273));
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4368273)) + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4368273) + 8);
    *(unsigned __int8 *)(v_rip + 4368167) = (unsigned __int8)(v_r12 + 1);
    result = PopBatteryReadTag(*(unsigned __int64 *)(v_rip + 4368273) - 64, a2, a3, a4);
    if (sign_flag) {
        a1 = *(unsigned __int64 *)(v_rip + 4368273) - 64;
        result = PopBatteryWaitTag(a1, a2, a3, a4);
    }
loc_00AE192C:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4368273))) != (v_rip + 4368164)) goto loc_00AE18CB;
    v_rsi = 0;
loc_00AE1936:
    goto loc_00AE1985;
loc_00AE1946:
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rip + 4368131) + 104)) != ((unsigned int)(v_r12 + 1))) goto loc_00AE1982;
    v_stack_m528 = 0;
    a4 = 0;
    a3 = 0;
    a2 = 0;
    result = KeWaitForSingleObject(*(unsigned __int64 *)(v_rip + 4368131) + 80, a2, a3, a4);
    result = PopBatteryInitialize(*(unsigned __int64 *)(v_rip + 4368131), a2, a3, a4);
    if (sign_flag) goto loc_00AE1973;
    goto loc_00AE197B;
loc_00AE1973:
    result = PopBatteryWaitTag(*(unsigned __int64 *)(v_rip + 4368131), a2, a3, a4);
loc_00AE197B:
loc_00AE1982:
loc_00AE1985:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4368131))) != (v_rip + 4368062)) goto loc_00AE1946;
    if ((*(unsigned __int64 *)(v_rip + 4368063)) == (v_rip + 4368056)) goto loc_00AE1B0E;
loc_00AE19B2:
    *(unsigned __int64 *)(v_rsp - 1096 - 8) = v_xmm0;
    result = PopBatteryQueryStatus(*(unsigned __int64 *)(v_rip + 4368063) - 64, 1, a3, a4);
    if (!sign_flag) goto loc_00AE19E5;
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 4368063) - 64 + 104) = 2;
    result = PopBatteryQueueWork(1, 1, a3, a4);
    goto loc_00AE1AF4;
loc_00AE19E5:
    result = Feature_BatteryChargeLimitV2Support__private_IsEnabledDeviceUsageNoInline(1, 1, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_00AE1A55;
    if ((*(unsigned __int8 *)(v_rip + 4368588)) == 0) goto loc_00AE1A55;
    if ((unsigned __int8)((unsigned int)(v_stack_m4DC)) == 0) goto loc_00AE1A55;
loc_00AE1A09:
    a1 = (*(unsigned __int64 *)(v_rip + 3317279)) | (0);
    if (condition_is_not_equal) goto loc_00AE1A09;
    v_rsi = (*(unsigned __int64 *)(v_rip + 3317279)) >> (32);
    if (((unsigned int)(*(unsigned __int64 *)(v_rip + 3317279))) != (*(unsigned int *)(*(unsigned __int64 *)(v_rip + 4368063) - 64 + 284))) goto loc_00AE1A34;
    result = *(unsigned __int64 *)(v_rip + 3317279);
    if (((unsigned int)(v_rsi)) != (*(unsigned int *)(*(unsigned __int64 *)(v_rip + 4368063) - 64 + 288))) {
        a3 = (unsigned int)(v_rsi);
        a2 = (unsigned int)(*(unsigned __int64 *)(v_rip + 3317279));
        a1 = *(unsigned __int64 *)(v_rip + 4368063) - 64;
        result = PopBatterySetChargeLimitControl(a1, a2, a3, a4);
        *(unsigned int *)(*(unsigned __int64 *)(v_rip + 4368063) - 64 + 284) = (unsigned int)(*(unsigned __int64 *)(v_rip + 3317279));
        *(unsigned int *)(*(unsigned __int64 *)(v_rip + 4368063) - 64 + 288) = (unsigned int)(v_rsi);
    }
loc_00AE1A55:
    result = PopAccountBatteryEnergyChange(*(unsigned __int64 *)(v_rip + 4368063) - 64, a2, a3, a4);
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 4368063) - 64 + 164))))) ^ (*(unsigned int *)(v_rsp - 1096 - 8)));
    if ((((unsigned __int8)(result)) & (7)) == 0) goto loc_00AE1A75;
    v_stack_m4F4 = 1;
    goto loc_00AE1A8F;
loc_00AE1A75:
    if ((*(unsigned int *)(v_rsp - 1096 - 4)) != ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 4368063) - 64 + 168))))) goto loc_00AE1A8B;
    if ((*(unsigned int *)(v_rsp - 1096 + 4)) != ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 4368063) - 64 + 176))))) {
        *(unsigned __int8 *)(v_rsp - 1096 - 128) = 1;
    }
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 4368063) - 64 + 176))) | (0xFFFFFFFFULL));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 4368063) - 64 + 164)))) & (2)) != 0) {
        a2 = 0;
        a1 = *(unsigned __int64 *)(v_rip + 4368063) - 64;
        result = PopBatteryQueryEstimatedTime(a1, a2, a3, a4);
    }
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 4368063) - 64 + 208) = (unsigned int)(result);
    v_rsi = 0;
    a1 = 0;
    if (((unsigned int)(result)) != -1) { a1 = (unsigned int)(result); }
    v_stack_m508 = (unsigned int)(a1);
    v_stack_m510 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 4368063) - 64 + 176)));
    v_stack_m518 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 4368063) - 64 + 172)));
    v_stack_m520 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 4368063) - 64 + 168)));
    v_stack_m528 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 4368063) - 64 + 164)));
    result = DbgPrintEx(146, v_rsi + 3, v_rip + 134370, *(unsigned __int64 *)(v_rip + 4368063) - 64);
loc_00AE1AF4:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4368063))) != (v_rip + 4368036)) goto loc_00AE19B2;
loc_00AE1B0E:
    if (v_stack_m4D8 == 0) goto loc_00AE1CA2;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m4D8 + 128))) - (1));
    if (((unsigned int)(result)) > 1) goto loc_00AE1CA2;
    if ((unsigned __int8)((unsigned int)(v_stack_m4E0)) == 0) goto loc_00AE1BEC;
loc_00AE1B45:
    a1 = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(v_rip + 3693931))) | (0));
    if (condition_is_not_equal) goto loc_00AE1B45;
    if (((unsigned __int8)(*(unsigned __int8 *)(v_rip + 3693931))) == (*(unsigned __int8 *)(v_stack_m4D8 + 216))) goto loc_00AE1CA2;
    if ((unsigned __int8)((unsigned __int8)(*(unsigned __int8 *)(v_rip + 3693931))) == 0) goto loc_00AE1B7B;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m4D8 + 180))) | (4));
    goto loc_00AE1B7E;
loc_00AE1B7B:
    a1 = (unsigned int)((a1) & (0xFFFFFFFBULL));
loc_00AE1B7E:
    *(unsigned int *)(180 + v_stack_m4D8 * 1) = (unsigned int)(a1);
    *(unsigned int *)(v_rsp - 1096 - 112) = 0;
    result = *(unsigned __int8 *)(v_rsp - 1096 - 111);
    if ((((unsigned __int8)(a1)) & (4)) != 0) { result = 1; }
    a3 = 0;
    v_stack_m520 = 0;
    *(unsigned __int8 *)(v_rsp - 1096 - 111) = (unsigned __int8)(result);
    v_stack_m528 = 4;
    result = PopPrepareIoctl(*(unsigned __int64 *)(v_stack_m4D8 + 56), (unsigned int)(0x294074ULL), a3, v_rsp - 1096 - 112);
    result = IoSynchronousCallDriver(*(unsigned __int64 *)(v_stack_m4D8 + 48), *(unsigned __int64 *)(v_stack_m4D8 + 56), a3, v_rsp - 1096 - 112);
    if (!sign_flag) goto loc_00AE1BD9;
loc_00AE1BC9:
    result = PopPowerAdapterTraceFailure(v_stack_m4D8, 3, (unsigned int)((unsigned int)(result)), v_rsp - 1096 - 112);
    goto loc_00AE1CA2;
loc_00AE1BD9:
    *(unsigned int *)(v_stack_m4D8 + 128) = 1;
    *(unsigned __int8 *)(v_stack_m4D8 + 216) = (unsigned __int8)((unsigned __int8)(*(unsigned __int8 *)(v_rip + 3693931)));
    goto loc_00AE1CA2;
loc_00AE1BEC:
    *(unsigned __int64 *)(v_rsp - 1096 + 112) = v_xmm6;
    *(unsigned __int64 *)(v_rsp - 1096 + 128) = v_xmm7;
    *(unsigned __int64 *)(v_rsp - 1096 + 144) = v_xmm8;
    result = PopPowerAdapterQueryStatus(v_stack_m4D8, 1, (unsigned int)((unsigned int)(result)), v_rsp - 1096 - 112);
    if (!sign_flag) goto loc_00AE1C2D;
    goto loc_00AE1BC9;
loc_00AE1C2D:
    *(unsigned int *)(v_stack_m4D8 + 128) = 1;
    result = (unsigned __int8)((result) ^ (*(unsigned __int8 *)(v_stack_m4D8 + 180)));
    a1 = (unsigned __int8)((unsigned int)(v_stack_m4F4));
    if (((1) & ((unsigned __int8)(result))) != 0) { a1 = 1; }
    v_stack_m4F4 = (unsigned int)(a1);
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m4D8 + 140))))) == 0) goto loc_00AE1CA6;
    *(unsigned __int64 *)(v_rsp - 1096 + 16) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 1096 + 48) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 1096 + 32) = v_xmm1;
    *(unsigned __int64 *)(v_rsp - 1096 + 64) = v_xmm6;
    *(unsigned __int64 *)(v_rsp - 1096 + 80) = v_xmm7;
    *(unsigned __int64 *)(v_rsp - 1096 + 96) = v_xmm8;
    result = PopPowerAdapterPublishRecState(v_rsp - 1096 + 64, v_rsp - 1096 + 16, (unsigned int)((unsigned int)(result)), v_rsp - 1096 - 112);
loc_00AE1CA2:
loc_00AE1CA6:
    if ((unsigned __int8)((unsigned __int8)(v_r12 + 1)) != 0) {
        result = PopBatteryUpdateCompositeInformation((unsigned int)(v_stack_m4F4), v_rsp - 1096 + 16, (unsigned int)((unsigned int)(result)), v_rsp - 1096 - 112);
        a1 = 1;
        *(unsigned __int64 *)(v_rip + 3693566) = 0;
        v_stack_m4F4 = (unsigned int)(a1);
    }
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rsp - 1096 - 124)))) & (4)) != 0) goto loc_00AE1CC8;
    if ((unsigned __int8)(a1) == 0) goto loc_00AE1D1D;
loc_00AE1CC8:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3693526))) != 0) goto loc_00AE1D10;
    a4 = 0;
    result = ((unsigned int)(*(unsigned int *)(v_rip + 3693526))) + (0x11E1A300ULL);
    a3 = 0;
    *(unsigned __int64 *)(v_rip + 3316506) = result;
    v_stack_m528 = v_rip + 4354908;
    result = KiSetTimerEx(v_rip + 4355019, 0xFFFFFFFFEE1E5D00ULL, a3, a4);
    goto loc_00AE1D1D;
loc_00AE1D10:
    result = KeCancelTimer(v_rip + 4355019, 0xFFFFFFFFEE1E5D00ULL, a3, a4);
loc_00AE1D1D:
    v_stack_m4E0 = 0;
    a2 = 0;
    v_stack_m4DC = (unsigned int)((unsigned int)(0x80000000ULL));
    a1 = (v_rip + 4355019) | (-1);
    *(unsigned int *)(v_rsp - 1096 - 56) = (unsigned int)((unsigned int)(0x80000000ULL));
    *(unsigned __int64 *)(v_rsp - 1096 + 184) = 0;
    *(unsigned __int64 *)(v_rsp - 1096 + 152) = v_xmm0;
    *(unsigned int *)(v_rsp - 1096 + 164) = (unsigned int)((unsigned int)(0x80000000ULL));
    result = (unsigned int)(((unsigned int)(0x80000000ULL)) | (0xFFFFFFFFULL));
    *(unsigned __int64 *)(v_rsp - 1096 - 40) = 0;
    *(unsigned __int64 *)(v_rsp - 1096 + 168) = v_xmm0;
    *(unsigned int *)(v_rsp - 1096 + 192) = 0;
    *(unsigned int *)(v_rsp - 1096 + 160) = (unsigned int)(result);
    *(unsigned int *)(v_rsp - 1096 + 156) = (unsigned int)(result);
    *(unsigned int *)(v_rsp - 1096 + 172) = (unsigned int)(result);
    *(unsigned int *)(v_rsp - 1096 - 84) = (unsigned int)(result);
    *(unsigned int *)(v_rsp - 1096 + 176) = (unsigned int)(result);
    *(unsigned int *)(v_rsp - 1096 + 180) = (unsigned int)(result);
    *(unsigned int *)(v_rsp - 1096 - 124) = (unsigned int)(result);
    *(unsigned int *)(v_rsp - 1096 + 184) = (unsigned int)(result);
    *(unsigned __int64 *)(v_rsp - 1096 - 72) = a1;
    *(unsigned __int64 *)(v_rsp - 1096 - 64) = a1;
    v_stack_m4CC = (unsigned int)(result);
    if ((*(unsigned int *)(v_rip + 4367066)) != 0) goto loc_00AE1DE8;
    *(unsigned int *)(v_rsp - 1096 + 152) = (unsigned int)(a2 + 1);
    if (v_stack_m4E8 != 3) goto loc_00AE208E;
    result = KiQueryUnbiasedInterruptTime((unsigned __int8)(a2 + 1), a2, a3, (unsigned int)((unsigned int)(result)));
    if (result < 0x11E1A300ULL) goto loc_00AE208E;
    v_stack_m4E8 = (unsigned int)(a2 + 1);
    goto loc_00AE208E;
loc_00AE1DE8:
    if ((*(unsigned __int64 *)(v_rip + 4366945)) == (v_rip + 4366938)) goto loc_00AE1FD3;
loc_00AE1E08:
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 4366945) + 100))))) & (231));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 4366945) + 100))))) & (10));
    a3 = (unsigned int)(((unsigned int)((unsigned int)(a1))) | (8));
    if (((unsigned __int8)(result)) != 10) { a3 = (unsigned int)(a1); }
    a1 = 0;
    result = a1 + 16;
    if ((((unsigned __int8)(a1 + 16)) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rsp - 1096 + 152))))) == 0) {
        result = (unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 4366945) + 100)));
        result = (unsigned __int8)((result) & (17));
        result = a1 + 16;
        if (((unsigned __int8)(result)) == 17) { a1 = (unsigned int)(result); }
    }
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 4366945) + 100))))) & (16));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 4366945) + 100)))) & (1)) != 0) goto loc_00AE1E51;
    result = (unsigned int)(-(result));
    result = (unsigned int)((result) & (0xFFFFFFFDULL));
    result = (unsigned int)((result) + (4));
    goto loc_00AE1E5B;
loc_00AE1E51:
    result = (unsigned int)(-(result));
    result = (unsigned int)((result) & (0xFFFFFFFAULL));
    result = (unsigned int)((result) + (8));
loc_00AE1E5B:
    v_rsi = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 1096 + 152))) ^ ((unsigned int)(a1)));
    v_rsi = (unsigned int)((v_rsi) | (a3));
    a1 = (unsigned int)((a1) | (0xFFFFFFFFULL));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 4366945) + 104)))) == ((unsigned int)(a1))) goto loc_00AE1E86;
    v_r14 = (unsigned int)((unsigned int)(result));
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == ((unsigned int)(a1))) { v_r14 = 0; }
    v_r14 = (unsigned int)((v_r14) + ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 4366945) + 104)))));
    *(unsigned int *)(v_rsp - 1096 + 156) = (unsigned int)(v_r14);
    goto loc_00AE1E88;
loc_00AE1E86:
    a2 = 0;
loc_00AE1E88:
    v_r13 = a2 + 1;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 4366945) + 108)))) != ((unsigned int)(a1))) {
        v_r13 = a2 + 1;
        if (((unsigned int)(a2 + 1)) == ((unsigned int)(a1))) { v_r13 = 0; }
        if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 4366945) + 108)))) > ((unsigned int)(v_r13))) { v_r13 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 4366945) + 108))); }
        *(unsigned int *)(v_rsp - 1096 + 160) = (unsigned int)(v_r13);
    }
    v_rbx = (unsigned int)(*(unsigned int *)(v_rsp - 1096 - 56));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 4366945) + 112)))) != ((unsigned int)((unsigned int)(0x80000000ULL)))) {
        v_rbx = (unsigned int)(*(unsigned int *)(v_rsp - 1096 - 56));
        if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 1096 - 56)))) == ((unsigned int)((unsigned int)(0x80000000ULL)))) { v_rbx = 0; }
        v_rbx = (unsigned int)((v_rbx) + ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 4366945) + 112)))));
        *(unsigned int *)(v_rsp - 1096 + 164) = (unsigned int)(v_rbx);
    }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 4366945) + 108)))) == -1) goto loc_00AE1EF4;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 4366945) + 112)))) == ((unsigned int)((unsigned int)(0x80000000ULL)))) goto loc_00AE1EF4;
    v_r11 = (unsigned int)((unsigned int)((unsigned int)(0x80000000ULL)));
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(0x80000000ULL))))) == ((unsigned int)((unsigned int)(0x80000000ULL)))) { v_r11 = 0; }
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 4366945) + 108))) != 0) goto loc_00AE1ED9;
    goto loc_00AE1EEC;
loc_00AE1ED9:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 4366945) + 112))) * ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 4366945) + 112)))));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 4366945) + 108))))) >> (1));
    result = (unsigned int)((result) + ((unsigned int)(a1)));
    a2 = 0;
loc_00AE1EEC:
    v_r11 = (unsigned int)((v_r11) + ((unsigned int)(result)));
    v_stack_m4DC = (unsigned int)(v_r11);
loc_00AE1EF4:
    a1 = (unsigned int)((a1) | (0xFFFFFFFFULL));
    v_r15 = (unsigned int)((unsigned int)(result));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 4366945) + 120)))) != ((unsigned int)(a1))) {
        v_r15 = (unsigned int)((unsigned int)(result));
        if (((unsigned int)((unsigned int)((unsigned int)(result)))) == ((unsigned int)(a1))) { v_r15 = 0; }
        v_r15 = (unsigned int)((v_r15) + ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 4366945) + 120)))));
        *(unsigned int *)(v_rsp - 1096 + 172) = (unsigned int)(v_r15);
    }
    v_r12 = (unsigned int)((unsigned int)(result));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 4366945) + 128)))) != ((unsigned int)(a1))) {
        v_r12 = (unsigned int)((unsigned int)(result));
        if (((unsigned int)((unsigned int)((unsigned int)(result)))) == ((unsigned int)(a1))) { v_r12 = 0; }
        v_r12 = (unsigned int)((v_r12) + ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 4366945) + 128)))));
        *(unsigned int *)(v_rsp - 1096 + 180) = (unsigned int)(v_r12);
    }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 4366945) + 124)))) != ((unsigned int)(a1))) {
        a4 = (unsigned int)((unsigned int)(result));
        if (((unsigned int)((unsigned int)((unsigned int)(result)))) == ((unsigned int)(a1))) { a4 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 4366945) + 124))); }
        *(unsigned int *)(v_rsp - 1096 - 84) = (unsigned int)(a4);
        *(unsigned int *)(v_rsp - 1096 + 176) = (unsigned int)(a4);
    }
    v_r10 = (unsigned int)((unsigned int)(result));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 4366945) + 132)))) != ((unsigned int)(a1))) {
        v_r10 = (unsigned int)((unsigned int)(result));
        if (((unsigned int)((unsigned int)((unsigned int)(result)))) == ((unsigned int)(a1))) { v_r10 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 4366945) + 132))); }
        *(unsigned int *)(v_rsp - 1096 - 124) = (unsigned int)(v_r10);
        *(unsigned int *)(v_rsp - 1096 + 184) = (unsigned int)(v_r10);
    }
    result = Feature_BatteryChargeLimitV2Support__private_IsEnabledDeviceUsageNoInline(a1, a2, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 4366945) + 108)), a4);
    a1 = 0;
    if ((unsigned int)(result) == 0) goto loc_00AE1FA8;
    if ((*(unsigned __int8 *)(v_rip + 4367185)) == 0) goto loc_00AE1FA8;
    *(unsigned __int64 *)(v_rsp - 1096 - 40) = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 4366945) + 140));
    *(unsigned int *)(v_rsp - 1096 + 192) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 4366945) + 140)));
    if (((16) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 4366571))))) == 0) goto loc_00AE1FA8;
    if (((16) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 4366945) + 136))))) == 0) {
    }
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4366945))) != (v_rip + 4366494)) goto loc_00AE1E08;
    *(unsigned int *)(v_rsp - 1096 + 152) = (unsigned int)(v_rsi);
loc_00AE1FD3:
    if ((((unsigned __int8)(v_rsi)) & (2)) != 0) {
        v_rsi = (unsigned int)((v_rsi) & (0xFFFFFFFBULL));
        *(unsigned int *)(v_rsp - 1096 + 152) = (unsigned int)(v_rsi);
    }
    if (((1) & ((unsigned __int8)(v_rsi))) != 0) goto loc_00AE207F;
    v_r12 = 0;
    if ((*(unsigned int *)(v_rip + 3692729)) != 0) goto loc_00AE2091;
    if ((*(unsigned __int64 *)(v_rip + 4366408)) == (v_rip + 4366401)) goto loc_00AE2091;
loc_00AE2017:
    result = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 4366408) + 144)) - 1;
    v_r14 = 0;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 4366408) + 144)) - 1)) <= -3) {
        result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 4366408) + 144)) - 1) * (*(unsigned int *)(*(unsigned __int64 *)(v_rip + 4366408) + 104)));
        a2 = 0;
        v_r14 = (unsigned int)((0) - ((unsigned int)(result)));
    }
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4366408))) != (v_rip + 4366401)) goto loc_00AE2017;
    if ((unsigned int)(v_r14) == 0) goto loc_00AE2091;
loc_00AE204E:
    result = PopBatteryQueryEstimatedTime(*(unsigned __int64 *)(v_rip + 4366342) - 64, (unsigned int)((unsigned int)(v_r14)), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 4366408) + 144)), (unsigned int)(*(unsigned int *)(v_rsp - 1096 - 84)));
    a2 = (unsigned int)(((unsigned int)((unsigned int)(v_r14))) | (0xFFFFFFFFULL));
    v_rbx = (unsigned int)(v_stack_m4CC);
    if (((unsigned int)(result)) != a2) {
        a1 = 0;
        if (((unsigned int)((unsigned int)(v_stack_m4CC))) != a2) { a1 = (unsigned int)((unsigned int)(v_stack_m4CC)); }
        v_rbx = result + a1 * 1;
    }
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4366342))) != (v_rip + 4366401)) goto loc_00AE204E;
    v_stack_m4CC = (unsigned int)(v_rbx);
    goto loc_00AE2091;
loc_00AE207F:
    if ((((unsigned __int8)(v_rsi)) & (4)) != 0) {
        result = PopEstimateChargeTime(a1, a2, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 4366408) + 144)), (unsigned int)(*(unsigned int *)(v_rsp - 1096 - 84)));
        *(unsigned __int64 *)(v_rsp - 1096 - 72) = result;
    }
    v_r12 = 0;
loc_00AE2091:
    v_r14 = (unsigned __int8)(((unsigned __int8)(v_rsi)) & (1));
    if (((unsigned int)((unsigned int)(v_stack_m4E8))) != 2) goto loc_00AE20A5;
    if ((unsigned __int8)(v_r14) == 0) goto loc_00AE20AF;
loc_00AE20A5:
    if (((unsigned int)((unsigned int)(v_stack_m4E8))) != 3) goto loc_00AE20B4;
    if ((unsigned __int8)(v_r14) != 0) {
        v_stack_m4E8 = 1;
    }
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 4366246))) & (16));
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_rsi))) & (16));
    if (((unsigned int)(result)) == ((unsigned int)(a1))) goto loc_00AE225D;
    v_stack_m518 = 0;
    v_stack_m520 = 0;
    result = ((unsigned int)(a1) != 0) ? 1 : 0;
    v_stack_m528 = 0;
    v_stack_m4F8 = (unsigned __int8)(result);
    a4 = 0;
    *(unsigned int *)(v_rsp - 1096 - 48) = (unsigned int)((unsigned __int8)(result));
    result = ZwUpdateWnfStateData(v_rip - 11277580, v_stack_m4F8, 1, a4);
    result = PopSetPowerSettingValueAcDc(v_rip - 11241934, 16 - 12, v_rsp - 1096 - 48, a4);
    if ((*(unsigned int *)(v_rip + 3298854)) <= 5) goto loc_00AE225D;
    result = tlgKeywordOn(v_rip + 3298828, 16 - 12, (unsigned int)((unsigned int)(result)), a4);
    if ((unsigned __int8)(result) != 0) {
        a1 = v_stack_m4F8;
        result = v_stack_m4EC;
        *(unsigned __int64 *)(v_rsp - 1096 + 816) = result;
        a2 = v_rip + 132640;
        result = v_rsp - 1096 - 52;
        *(unsigned int *)(v_rsp - 1096 - 44) = (unsigned int)((unsigned int)((unsigned int)(result)));
        a3 = v_stack_m4E0;
        a4 = v_rip + 132924;
        *(unsigned __int64 *)(v_rsp - 1096 + 832) = result;
        result = v_rsp - 1096 - 44;
        v_stack_m4EC = (unsigned __int8)(a1);
        if (((1) & ((unsigned __int8)(a3))) == 0) { a2 = a4; }
        *(unsigned __int64 *)(v_rsp - 1096 + 848) = result;
        a1 = v_rsp - 1096 + 864;
        *(unsigned __int64 *)(v_rsp - 1096 + 824) = 1;
        *(unsigned int *)(v_rsp - 1096 - 52) = (unsigned int)((unsigned int)((unsigned int)(result)));
        *(unsigned __int64 *)(v_rsp - 1096 + 840) = 4;
        *(unsigned __int64 *)(v_rsp - 1096 + 856) = 4;
        result = tlgCreate1Sz_char(a1, a2, a3, a4);
        a2 = v_rip + 132692;
        a1 = v_rsp - 1096 + 880;
        if ((((unsigned __int8)(a3)) & (2)) == 0) { a2 = a4; }
        result = tlgCreate1Sz_char(a1, a2, a3, a4);
        a2 = v_rip + 132649;
        a1 = v_rsp - 1096 + 896;
        if ((((unsigned __int8)(a3)) & (4)) == 0) { a2 = a4; }
        result = tlgCreate1Sz_char(a1, a2, a3, a4);
        a2 = v_rip + 133166;
        a1 = v_rsp - 1096 + 912;
        if ((((unsigned __int8)(a3)) & (8)) == 0) { a2 = a4; }
        result = tlgCreate1Sz_char(a1, a2, a3, a4);
        result = v_rsp - 1096 - 16;
        *(unsigned __int64 *)(v_rsp - 1096 - 16) = 0x1000000ULL;
        *(unsigned __int64 *)(v_rsp - 1096 + 928) = result;
        a2 = v_rip - 11093714;
        result = v_rsp - 1096 + 784;
        *(unsigned __int64 *)(v_rsp - 1096 + 936) = 8;
        v_stack_m520 = result;
        a1 = v_rip + 3298558;
        a4 = 0;
        v_stack_m528 = 10;
        a3 = 0;
        result = tlgWriteTransfer_EtwWriteTransfer(a1, a2, a3, a4);
    }
    result = Feature_BatteryChargeLimitV2Support__private_IsEnabledDeviceUsageNoInline(a1, a2, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_00AE22A6;
    if ((*(unsigned int *)(v_rip + 4365842)) != ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 1096 + 188))))) goto loc_00AE2280;
    if ((*(unsigned int *)(v_rip + 4365834)) == ((unsigned int)(*(unsigned __int64 *)(v_rsp - 1096 - 40)))) goto loc_00AE22A6;
loc_00AE2280:
    result = PopBatteryPublishChargeLimitStatus((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 1096 + 188)))), *(unsigned __int64 *)(v_rsp - 1096 - 40), a3, a4);
    if (((16) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 4365815))))) == 0) goto loc_00AE22A6;
    if (((16) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rsp - 1096 + 188))))) == 0) {
        v_rsi = *(unsigned int *)(v_rsp - 1096 + 152);
    }
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rsi))) & (64));
    if ((((unsigned __int8)(v_rsi)) & (32)) == 0) goto loc_00AE22BC;
    result = (unsigned int)(-(result));
    v_rdi = (unsigned int)(-((unsigned int)(*(unsigned int *)(v_rsp - 1096 + 188))));
    v_rdi = (unsigned int)((v_rdi) + (1));
    goto loc_00AE22BF;
loc_00AE22BC:
loc_00AE22BF:
    if ((*(unsigned int *)(v_rip + 4366167)) == 0) goto loc_00AE22F6;
    result = PopAcquireRwLockExclusive(v_rip + 4353346, *(unsigned __int64 *)(v_rsp - 1096 - 40), a3, a4);
    *(unsigned int *)(v_rip + 4366140) = 0;
    *(unsigned int *)(v_rip + 4353370) = 0;
    result = PopReleaseRwLock(v_rip + 4353334, *(unsigned __int64 *)(v_rsp - 1096 - 40), a3, a4);
    v_rdi = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 1096 - 80))) | (2));
    goto loc_00AE22FE;
loc_00AE22F6:
loc_00AE22FE:
    result = PopBatteryApplyCompositeState(v_rsp - 1096 + 152, (unsigned int)((unsigned int)((unsigned int)(v_stack_m4CC))), (unsigned int)(v_stack_m4DC), a4);
    if ((unsigned __int8)(result) != 0) goto loc_00AE231E;
    if ((unsigned __int8)(v_stack_m4EB) == 0) goto loc_00AE2338;
loc_00AE231E:
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 1096 - 80))))) | (4));
    if ((unsigned __int8)(result) == 0) { a2 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 1096 - 80))); }
    result = PopEvaluateWeakChargerState((unsigned __int8)(v_r14), a2, (unsigned int)(v_stack_m4DC), a4);
    goto loc_00AE233E;
loc_00AE2338:
loc_00AE233E:
    *(unsigned __int64 *)(v_rip + 4366030) = *(unsigned __int64 *)(result);
    result = *(unsigned __int64 *)(result);
    if ((*(unsigned __int64 *)(v_rip + 4366026)) != 0) {
        a2 = 0;
        a1 = v_rip + 4366015;
        result = ExfUnblockPushLock(a1, a2, (unsigned int)(v_stack_m4DC), a4);
    }
    if (((unsigned int)((unsigned int)(0x80000000ULL))) == 0x80000000ULL) goto loc_00AE23A0;
    goto loc_00AE1807;
loc_00AE2399:
loc_00AE23A0:
    if ((*(unsigned __int64 *)(v_rip + 4365481)) == (v_rip + 4365474)) goto loc_00AE23D1;
loc_00AE23BA:
    a2 = 0;
    result = PopBatteryQueryStatus(*(unsigned __int64 *)(v_rip + 4365481) - 64, a2, (unsigned int)(v_stack_m4DC), a4);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4365481))) != (v_rip + 4365462)) goto loc_00AE23BA;
loc_00AE23D1:
    if (v_stack_m4D8 == 0) goto loc_00AE23EE;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m4D8 + 128))) - (1));
    if (((unsigned int)(result)) <= 1) {
        a2 = 0;
        a1 = v_stack_m4D8;
        result = PopPowerAdapterQueryStatus(a1, a2, (unsigned int)(v_stack_m4DC), a4);
    }
    if ((*(unsigned int *)(v_rip + 3691723)) == 0) {
        v_stack_m518 = 0;
        a2 = v_rsp - 1096 - 72;
        v_stack_m520 = 0;
        a1 = v_rip - 11278665;
        a4 = 0;
        v_stack_m528 = 0;
        a3 = 8;
        result = ZwUpdateWnfStateData(a1, a2, a3, a4);
    }
    if ((*(unsigned int *)(v_rip + 3691660)) != 0) goto loc_00AE2467;
    result = PopBatteryEstimatesSpoiled(a1, a2, a3, a4);
    if (((unsigned int)((unsigned int)(v_stack_m4CC))) == -1) goto loc_00AE2440;
    if ((unsigned __int8)(result) == 0) {
        a1 = (unsigned int)((unsigned int)(v_stack_m4CC));
        *(unsigned __int64 *)(v_rsp - 1096 - 64) = a1;
    }
    v_stack_m518 = 0;
    v_stack_m520 = 0;
    a4 = 0;
    v_stack_m528 = 0;
    result = ZwUpdateWnfStateData(v_rip - 11278845, v_rsp - 1096 - 64, 8, a4);
    goto loc_00AE246B;
loc_00AE2467:
loc_00AE246B:
    if ((*(unsigned int *)(v_rip + 3298006)) >= = 5) {
        result = *(unsigned int *)(v_rip + 3691586);
        a2 = v_rip - 11093034;
        v_stack_m4E4 = (unsigned int)(result);
        a1 = v_rip + 3297976;
        result = v_stack_m4E4;
        *(unsigned __int64 *)(v_rsp - 1096 + 696) = 4;
        *(unsigned __int64 *)(v_rsp - 1096 + 688) = result;
        a4 = 0;
        result = *(unsigned __int64 *)(v_rsp - 1096 - 72);
        a3 = 0;
        v_stack_m4D8 = result;
        result = v_stack_m4D8;
        *(unsigned __int64 *)(v_rsp - 1096 + 704) = result;
        result = *(unsigned int *)(v_rip + 3691500);
        v_stack_m4F0 = (unsigned int)(result);
        result = v_stack_m4F0;
        *(unsigned __int64 *)(v_rsp - 1096 + 720) = result;
        result = v_stack_m4D0;
        *(unsigned __int64 *)(v_rsp - 1096 + 736) = result;
        result = *(unsigned __int64 *)(v_rsp - 1096 - 64);
        *(unsigned __int64 *)(v_rsp - 1096 - 120) = result;
        result = v_rsp - 1096 - 120;
        *(unsigned __int64 *)(v_rsp - 1096 + 752) = result;
        result = v_stack_m4F7;
        *(unsigned __int64 *)(v_rsp - 1096 + 768) = result;
        result = v_rsp - 1096 + 656;
        v_stack_m520 = result;
        v_stack_m528 = 8;
        *(unsigned __int64 *)(v_rsp - 1096 + 712) = 8;
        *(unsigned __int64 *)(v_rsp - 1096 + 728) = 4;
        v_stack_m4D0 = (unsigned int)((unsigned int)(v_stack_m4CC));
        *(unsigned __int64 *)(v_rsp - 1096 + 744) = 4;
        *(unsigned __int64 *)(v_rsp - 1096 + 760) = 8;
        v_stack_m4F7 = (unsigned __int8)(v_stack_m4F7);
        *(unsigned __int64 *)(v_rsp - 1096 + 776) = 1;
        result = tlgWriteTransfer_EtwWriteTransfer(a1, a2, a3, a4);
    }
    if (condition_is_equal) goto loc_00AE2CDB;
    *(unsigned int *)(v_rsp - 1096 + 232) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4365118)));
    a4 = 0;
    *(unsigned __int64 *)(v_rsp - 1096 + 200) = v_xmm0;
    *(unsigned int *)(v_rsp - 1096 + 256) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4364957)));
    v_stack_m518 = 0;
    v_stack_m520 = 0;
    *(unsigned __int64 *)(v_rsp - 1096 + 236) = v_xmm0;
    *(unsigned int *)(v_rsp - 1096 + 252) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4364932)));
    *(unsigned __int64 *)(v_rsp - 1096 + 216) = v_xmm1;
    v_stack_m528 = 0;
    result = ZwUpdateWnfStateData(v_rip - 11279373, v_rsp - 1096 + 200, a4 + 60, a4);
    result = Feature_BatteryChargeLimitV2Support__private_IsEnabledDeviceUsageNoInline(v_rip - 11279373, v_rsp - 1096 + 200, a4 + 60, a4);
    if ((unsigned int)(result) != 0) goto loc_00AE28E3;
    if ((*(unsigned int *)(v_rip + 3297621)) <= 5) goto loc_00AE2C10;
    result = tlgKeywordOn(v_rip + 3297598, v_rsp - 1096 + 200, a4 + 60, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00AE2C10;
    *(unsigned __int64 *)(v_rsp - 1096 + 304) = v_stack_m4D0;
    v_stack_m4D0 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4364810)));
    *(unsigned __int64 *)(v_rsp - 1096 + 312) = 4;
    a2 = v_rip + 132079;
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 4364866))))) == 0) { a2 = v_rip + 132122; }
    result = tlgCreate1Sz_char(v_rsp - 1096 + 320, a2, (unsigned int)(*(unsigned int *)(v_rip + 4364866)), (unsigned int)(*(unsigned int *)(v_rip + 4364810)));
    a2 = v_rip + 132051;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 4364866)))) & (2)) == 0) { a2 = v_rip + 131644; }
    result = tlgCreate1Sz_char(v_rsp - 1096 + 336, a2, (unsigned int)(*(unsigned int *)(v_rip + 4364866)), (unsigned int)(*(unsigned int *)(v_rip + 4364810)));
    a2 = v_rip + 132098;
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 4364866))))) == 0) { a2 = v_rip + 131644; }
    result = tlgCreate1Sz_char(v_rsp - 1096 + 352, a2, (unsigned int)(*(unsigned int *)(v_rip + 4364866)), (unsigned int)(*(unsigned int *)(v_rip + 4364810)));
    a2 = v_rip + 132040;
    if (((8) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 4364866))))) == 0) { a2 = v_rip + 131644; }
    result = tlgCreate1Sz_char(v_rsp - 1096 + 368, a2, (unsigned int)(*(unsigned int *)(v_rip + 4364866)), (unsigned int)(*(unsigned int *)(v_rip + 4364810)));
    a2 = v_rip + 132124;
    if (((16) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 4364866))))) == 0) { a2 = v_rip + 131644; }
    result = tlgCreate1Sz_char(v_rsp - 1096 + 384, a2, (unsigned int)(*(unsigned int *)(v_rip + 4364866)), (unsigned int)(*(unsigned int *)(v_rip + 4364810)));
    a2 = v_rip + 132046;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 4364866)))) & (32)) == 0) { a2 = v_rip + 131644; }
    result = tlgCreate1Sz_char(v_rsp - 1096 + 400, a2, (unsigned int)(*(unsigned int *)(v_rip + 4364866)), (unsigned int)(*(unsigned int *)(v_rip + 4364810)));
    a2 = v_rip + 131731;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 4364866)))) & (64)) == 0) { a2 = v_rip + 131644; }
    result = tlgCreate1Sz_char(v_rsp - 1096 + 416, a2, (unsigned int)(*(unsigned int *)(v_rip + 4364866)), (unsigned int)(*(unsigned int *)(v_rip + 4364810)));
    a2 = v_rip + 131672;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 4364866)))) & (128)) == 0) { a2 = v_rip + 131644; }
    result = tlgCreate1Sz_char(v_rsp - 1096 + 432, a2, (unsigned int)(*(unsigned int *)(v_rip + 4364866)), (unsigned int)(*(unsigned int *)(v_rip + 4364810)));
    a2 = v_rip + 131738;
    if (((*(unsigned __int8 *)(v_rip + 4365201)) & (1)) == 0) { a2 = v_rip + 131644; }
    result = tlgCreate1Sz_char(v_rsp - 1096 + 448, a2, (unsigned int)(*(unsigned int *)(v_rip + 4364866)), (unsigned int)(*(unsigned int *)(v_rip + 4364810)));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4364627))) != 0) goto loc_00AE2757;
    goto loc_00AE276A;
loc_00AE2757:
    result = (unsigned int)((0) * (*(unsigned int *)(v_rip + 4364550)));
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4364627))))) >> (1));
    a2 = 0;
    result = (unsigned int)((result) + ((unsigned int)(a1)));
loc_00AE276A:
    v_stack_m4E4 = (unsigned int)(result);
    *(unsigned __int64 *)(v_rsp - 1096 + 464) = v_stack_m4E4;
    *(unsigned __int64 *)(v_rsp - 1096 + 472) = 4;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4364627))) != 0) goto loc_00AE278F;
    goto loc_00AE27A1;
loc_00AE278F:
    a2 = 0;
    result = ((unsigned int)(*(unsigned int *)(v_rip + 4364495))) * ((unsigned int)(*(unsigned int *)(v_rip + 4364495)));
loc_00AE27A1:
    v_stack_m4F0 = (unsigned int)(result);
    *(unsigned __int64 *)(v_rsp - 1096 + 488) = 4;
    *(unsigned __int64 *)(v_rsp - 1096 + 480) = v_stack_m4F0;
    *(unsigned int *)(v_rsp - 1096 - 92) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4364426)));
    *(unsigned __int64 *)(v_rsp - 1096 + 496) = v_rsp - 1096 - 92;
    *(unsigned __int64 *)(v_rsp - 1096 + 512) = v_rsp - 1096 - 88;
    *(unsigned int *)(v_rsp - 1096 - 108) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4364399)));
    *(unsigned __int64 *)(v_rsp - 1096 + 528) = v_rsp - 1096 - 108;
    *(unsigned int *)(v_rsp - 1096 - 104) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4364383)));
    *(unsigned __int64 *)(v_rsp - 1096 + 544) = v_rsp - 1096 - 104;
    *(unsigned int *)(v_rsp - 1096 - 100) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4364303)));
    *(unsigned __int64 *)(v_rsp - 1096 + 560) = v_rsp - 1096 - 100;
    *(unsigned __int64 *)(v_rsp - 1096 + 576) = v_rsp - 1096 - 96;
    a2 = v_rip + 131662;
    if (((*(unsigned int *)(v_rip + 4364517)) & (0x40000000ULL)) == 0) { a2 = v_rip + 131503; }
    *(unsigned __int64 *)(v_rsp - 1096 + 504) = 4;
    *(unsigned int *)(v_rsp - 1096 - 88) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4364627)));
    *(unsigned __int64 *)(v_rsp - 1096 + 520) = 4;
    *(unsigned __int64 *)(v_rsp - 1096 + 536) = 4;
    *(unsigned __int64 *)(v_rsp - 1096 + 552) = 4;
    *(unsigned __int64 *)(v_rsp - 1096 + 568) = 4;
    *(unsigned int *)(v_rsp - 1096 - 96) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4364810)));
    *(unsigned __int64 *)(v_rsp - 1096 + 584) = 4;
    result = tlgCreate1Sz_char(v_rsp - 1096 + 592, a2, (unsigned int)(*(unsigned int *)(v_rip + 4364627)), (unsigned int)(*(unsigned int *)(v_rip + 4364810)));
    *(unsigned __int64 *)(v_rsp - 1096 + 608) = v_rsp - 1096 - 120;
    *(unsigned int *)(v_rsp - 1096 - 120) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4364290)));
    *(unsigned __int64 *)(v_rsp - 1096 + 624) = v_stack_m4D8;
    v_stack_m520 = v_rsp - 1096 + 272;
    v_stack_m528 = 23;
    *(unsigned __int64 *)(v_rsp - 1096 + 616) = 4;
    v_stack_m4D8 = (unsigned int)((unsigned int)((unsigned int)(result)));
    goto loc_00AE2BF3;
loc_00AE28E3:
    if ((*(unsigned int *)(v_rip + 3296862)) <= 5) goto loc_00AE2C10;
    result = tlgKeywordOn(v_rip + 3296839, v_rip - 11094638, (unsigned int)(*(unsigned int *)(v_rip + 4364627)), (unsigned int)(*(unsigned int *)(v_rip + 4364810)));
    if ((unsigned __int8)(result) == 0) goto loc_00AE2C10;
    *(unsigned __int64 *)(v_rsp - 1096 + 304) = v_stack_m4D8;
    v_stack_m4D8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4364051)));
    *(unsigned __int64 *)(v_rsp - 1096 + 312) = 4;
    a2 = v_rip + 131320;
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 4364107))))) == 0) { a2 = v_rip + 131363; }
    result = tlgCreate1Sz_char(v_rsp - 1096 + 320, a2, (unsigned int)(*(unsigned int *)(v_rip + 4364107)), (unsigned int)(*(unsigned int *)(v_rip + 4364051)));
    a2 = v_rip + 131292;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 4364107)))) & (2)) == 0) { a2 = v_rip + 130885; }
    result = tlgCreate1Sz_char(v_rsp - 1096 + 336, a2, (unsigned int)(*(unsigned int *)(v_rip + 4364107)), (unsigned int)(*(unsigned int *)(v_rip + 4364051)));
    a2 = v_rip + 131339;
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 4364107))))) == 0) { a2 = v_rip + 130885; }
    result = tlgCreate1Sz_char(v_rsp - 1096 + 352, a2, (unsigned int)(*(unsigned int *)(v_rip + 4364107)), (unsigned int)(*(unsigned int *)(v_rip + 4364051)));
    a2 = v_rip + 131281;
    if (((8) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 4364107))))) == 0) { a2 = v_rip + 130885; }
    result = tlgCreate1Sz_char(v_rsp - 1096 + 368, a2, (unsigned int)(*(unsigned int *)(v_rip + 4364107)), (unsigned int)(*(unsigned int *)(v_rip + 4364051)));
    a2 = v_rip + 131365;
    if (((16) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 4364107))))) == 0) { a2 = v_rip + 130885; }
    result = tlgCreate1Sz_char(v_rsp - 1096 + 384, a2, (unsigned int)(*(unsigned int *)(v_rip + 4364107)), (unsigned int)(*(unsigned int *)(v_rip + 4364051)));
    a2 = v_rip + 131287;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 4364107)))) & (32)) == 0) { a2 = v_rip + 130885; }
    result = tlgCreate1Sz_char(v_rsp - 1096 + 400, a2, (unsigned int)(*(unsigned int *)(v_rip + 4364107)), (unsigned int)(*(unsigned int *)(v_rip + 4364051)));
    a2 = v_rip + 130972;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 4364107)))) & (64)) == 0) { a2 = v_rip + 130885; }
    result = tlgCreate1Sz_char(v_rsp - 1096 + 416, a2, (unsigned int)(*(unsigned int *)(v_rip + 4364107)), (unsigned int)(*(unsigned int *)(v_rip + 4364051)));
    a2 = v_rip + 130913;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 4364107)))) & (128)) == 0) { a2 = v_rip + 130885; }
    result = tlgCreate1Sz_char(v_rsp - 1096 + 432, a2, (unsigned int)(*(unsigned int *)(v_rip + 4364107)), (unsigned int)(*(unsigned int *)(v_rip + 4364051)));
    a2 = v_rip + 130979;
    if (((*(unsigned __int8 *)(v_rip + 4364442)) & (1)) == 0) { a2 = v_rip + 130885; }
    result = tlgCreate1Sz_char(v_rsp - 1096 + 448, a2, (unsigned int)(*(unsigned int *)(v_rip + 4364107)), (unsigned int)(*(unsigned int *)(v_rip + 4364051)));
    a2 = v_rip + 130917;
    if (((*(unsigned __int8 *)(v_rip + 4364413)) & (1)) == 0) { a2 = v_rip + 130885; }
    result = tlgCreate1Sz_char(v_rsp - 1096 + 464, a2, (unsigned int)(*(unsigned int *)(v_rip + 4364107)), (unsigned int)(*(unsigned int *)(v_rip + 4364051)));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4363838))) != 0) goto loc_00AE2A6C;
    goto loc_00AE2A7F;
loc_00AE2A6C:
    result = (unsigned int)((0) * (*(unsigned int *)(v_rip + 4363761)));
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4363838))))) >> (1));
    a2 = 0;
    result = (unsigned int)((result) + ((unsigned int)(a1)));
loc_00AE2A7F:
    *(unsigned int *)(v_rsp - 1096 - 120) = (unsigned int)(result);
    *(unsigned __int64 *)(v_rsp - 1096 + 480) = v_rsp - 1096 - 120;
    *(unsigned __int64 *)(v_rsp - 1096 + 488) = 4;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4363838))) != 0) goto loc_00AE2AA2;
    goto loc_00AE2AB4;
loc_00AE2AA2:
    a2 = 0;
    result = ((unsigned int)(*(unsigned int *)(v_rip + 4363708))) * ((unsigned int)(*(unsigned int *)(v_rip + 4363708)));
loc_00AE2AB4:
    *(unsigned int *)(v_rsp - 1096 - 96) = (unsigned int)(result);
    *(unsigned __int64 *)(v_rsp - 1096 + 504) = 4;
    *(unsigned __int64 *)(v_rsp - 1096 + 496) = v_rsp - 1096 - 96;
    *(unsigned int *)(v_rsp - 1096 - 100) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4363641)));
    *(unsigned __int64 *)(v_rsp - 1096 + 512) = v_rsp - 1096 - 100;
    *(unsigned __int64 *)(v_rsp - 1096 + 528) = v_rsp - 1096 - 104;
    *(unsigned int *)(v_rsp - 1096 - 108) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4363614)));
    *(unsigned __int64 *)(v_rsp - 1096 + 544) = v_rsp - 1096 - 108;
    *(unsigned int *)(v_rsp - 1096 - 88) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4363598)));
    *(unsigned __int64 *)(v_rsp - 1096 + 560) = v_rsp - 1096 - 88;
    *(unsigned int *)(v_rsp - 1096 - 92) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4363518)));
    *(unsigned __int64 *)(v_rsp - 1096 + 576) = v_rsp - 1096 - 92;
    *(unsigned __int64 *)(v_rsp - 1096 + 592) = v_stack_m4D0;
    a2 = v_rip + 130875;
    if (((*(unsigned int *)(v_rip + 4363730)) & (0x40000000ULL)) == 0) { a2 = v_rip + 130717; }
    *(unsigned __int64 *)(v_rsp - 1096 + 520) = 4;
    *(unsigned int *)(v_rsp - 1096 - 104) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4363838)));
    *(unsigned __int64 *)(v_rsp - 1096 + 536) = 4;
    *(unsigned __int64 *)(v_rsp - 1096 + 552) = 4;
    *(unsigned __int64 *)(v_rsp - 1096 + 568) = 4;
    *(unsigned __int64 *)(v_rsp - 1096 + 584) = 4;
    v_stack_m4D0 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4364051)));
    *(unsigned __int64 *)(v_rsp - 1096 + 600) = 4;
    result = tlgCreate1Sz_char(v_rsp - 1096 + 608, a2, (unsigned int)(*(unsigned int *)(v_rip + 4363838)), (unsigned int)(*(unsigned int *)(v_rip + 4364051)));
    *(unsigned __int64 *)(v_rsp - 1096 + 624) = v_stack_m4E4;
    v_stack_m4E4 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4363503)));
    *(unsigned __int64 *)(v_rsp - 1096 + 640) = v_stack_m4F0;
    v_stack_m520 = v_rsp - 1096 + 272;
    v_stack_m528 = 24;
    v_stack_m4F0 = (unsigned int)((unsigned int)((unsigned int)(result)));
    *(unsigned __int64 *)(v_rsp - 1096 + 648) = 4;
loc_00AE2BF3:
    a4 = 0;
    *(unsigned __int64 *)(v_rsp - 1096 + 632) = 4;
    a3 = 0;
    result = tlgWriteTransfer_EtwWriteTransfer(v_rip + 3296061, v_rip - 11095991, a3, a4);
loc_00AE2C10:
    if (v_stack_m4E8 != 1) goto loc_00AE2C58;
    if ((unsigned __int8)(v_r14) != 0) goto loc_00AE2C2F;
    *(unsigned __int64 *)(v_rsp - 1096 - 24) = *(unsigned __int64 *)(result);
    goto loc_00AE2C33;
loc_00AE2C2F:
    *(unsigned __int64 *)(v_rsp - 1096 - 24) = 0;
loc_00AE2C33:
    v_stack_m518 = 0;
    v_stack_m520 = 0;
    a4 = 0;
    v_stack_m528 = 0;
    result = ZwUpdateWnfStateData(v_rip - 11299592, v_rsp - 1096 - 24, 8, a4);
loc_00AE2C58:
    if ((unsigned __int8)((unsigned int)(v_stack_m4F4)) == 0) goto loc_00AE2CDB;
    v_stack_m518 = 0;
    *(unsigned __int64 *)(v_rsp - 1096 - 32) = 0;
    a4 = 0;
    v_stack_m520 = 0;
    v_stack_m528 = 0;
    result = ZwUpdateWnfStateData(v_rip - 11281385, v_rsp - 1096 - 32, 8, a4);
    if ((*(unsigned int *)(v_rip + 3295927)) >= = 5) {
        v_stack_m4D8 = (unsigned int)(result);
        a2 = v_rip - 11097218;
        result = v_stack_m4D8;
        *(unsigned __int64 *)(v_rsp - 1096 + 984) = 4;
        *(unsigned __int64 *)(v_rsp - 1096 + 976) = result;
        a1 = v_rip + 3295884;
        result = v_rsp - 1096 + 944;
        a4 = 0;
        v_stack_m520 = result;
        a3 = 0;
        v_stack_m528 = 3;
        result = tlgWriteTransfer_EtwWriteTransfer(a1, a2, a3, a4);
    }
    result = PopReleaseRwLock(v_rip + 4363070, a2, a3, a4);
    result = PopReleaseRwLock(v_rip + 4365330, a2, a3, a4);
    a1 = (*(unsigned __int64 *)(v_rsp - 1096 + 992)) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopBatteryWorker(int64_t Arg1, int32_t Arg2, int32_t Arg3)
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
    uint64_t v_stack_m28;
    uint32_t v_stack_m4CC;
    uint64_t v_stack_m4D0;
    uint64_t v_stack_m4D8;
    uint32_t v_stack_m4DC;
    uint32_t v_stack_m4E0;
    uint64_t v_stack_m4E4;
    uint32_t v_stack_m4E8;
    uint8_t v_stack_m4EB;
    uint64_t v_stack_m4EC;
    uint64_t v_stack_m4F0;
    uint32_t v_stack_m4F4;
    uint8_t v_stack_m4F7;
    uint8_t v_stack_m4F8;
    uint32_t v_stack_m508;
    uint32_t v_stack_m510;
    uint32_t v_stack_m518;
    uint64_t v_stack_m520;
    uint64_t v_stack_m528;
    uint32_t v_stack_m548;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rsi;
    *(uint64_t *)(local_rsp + 0x18) = local_rdi;
    local_rsp = (local_rsp) - (0x520ULL);
    *(uint64_t *)(local_rsp - 0x38) = v_xmm6;
    *(uint64_t *)(local_rsp - 0x48) = v_xmm7;
    *(uint64_t *)(local_rsp - 0x58) = v_xmm8;
    result = (*(uint64_t *)(v_rip + 0x3290B6)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x448 + 0x3E0) = result;
    local_r12 = 0;
    *(uint64_t *)(local_rsp - 0x448 - 0x48) = 0;
    result = 0;
    *(uint64_t *)(local_rsp - 0x448 - 0x40) = 0;
    *(uint64_t *)(local_rsp - 0x448 - 0x20) = 0;
    v_stack_m4F8 = 0;
    *(uint64_t *)(local_rsp - 0x448 + 0xC8) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x448 + 0xF8) = 0;
    *(uint64_t *)(local_rsp - 0x448 + 0xD8) = v_xmm0;
    *(uint32_t *)(local_rsp - 0x448 + 0x100) = 0;
    *(uint64_t *)(local_rsp - 0x448 + 0xE8) = v_xmm0;
    result = PopAcquireRwLockShared(v_rip + 4371042, Arg2, Arg3, a4);
    result = PopAcquireRwLockExclusive(v_rip + 4368702, Arg2, Arg3, a4);
    *(uint64_t *)(local_rsp - 0x448 - 0x78) = 0;
    v_stack_m520 = v_stack_m4F0;
    v_stack_m4E4 = 0;
    Arg3 = 0;
    v_stack_m528 = local_rsp - 1096 - 120;
    Arg2 = 0;
    v_stack_m4F0 = 8;
    result = ZwQueryWnfStateData(v_rip - 11294172, Arg2, Arg3, v_stack_m4E4);
    if (((uint32_t)(result)) == 0xC000009AULL) goto loc_00AE175A;
    if (((uint32_t)(result)) == 0xC0000189ULL) goto loc_00AE175A;
    if ((uint32_t)(result) != 0) goto loc_00AE1753;
    if (v_stack_m4F0 != 8) goto loc_00AE1753;
    result = -(*(uint64_t *)(local_rsp - 0x448 - 0x78));
    result = (uint32_t)(-(result));
    result = (uint32_t)((result) + (2));
    v_stack_m4E8 = (uint32_t)(result);
    goto loc_00AE175F;
loc_00AE1753:
    v_stack_m4E8 = (uint32_t)(local_r12 + 1);
    goto loc_00AE175F;
loc_00AE175A:
    v_stack_m4E8 = 0;
loc_00AE175F:
    v_stack_m4D8 = *(uint64_t *)(v_rip + 0x42AB72);
    goto loc_00AE1787;
loc_00AE177B:
    result = IoCancelIrp(*(uint64_t *)(*(uint64_t *)(v_rip + 0x42A8DC) - 0x8), Arg2, Arg3, v_stack_m4E4);
loc_00AE1787:
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0x42A8DC))) != (v_rip + 4368611)) goto loc_00AE177B;
    if (*(uint64_t *)(v_rip + 0x42AB72) == 0) goto loc_00AE17A8;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x42AB72) + 0x80))) - ((uint32_t)(local_r12 + 1)));
    if (((uint32_t)(result)) <= ((uint32_t)(local_r12 + 1))) {
        Arg1 = *(uint64_t *)(*(uint64_t *)(v_rip + 0x42AB72) + 0x38);
        result = IoCancelIrp(Arg1, Arg2, Arg3, v_stack_m4E4);
    }
    goto loc_00AE17CA;
loc_00AE17B1:
    v_stack_m528 = 0;
    a4 = 0;
    Arg3 = 0;
    Arg2 = 0;
    result = KeWaitForSingleObject(*(uint64_t *)(v_rip + 0x42A8A1) + 16, Arg2, Arg3, a4);
loc_00AE17CA:
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0x42A8A1))) != (v_rip + 4368611)) goto loc_00AE17B1;
    if (*(uint64_t *)(v_rip + 0x42AB72) == 0) goto loc_00AE17F8;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x42AB72) + 0x80))) - ((uint32_t)(local_r12 + 1)));
    if (((uint32_t)(result)) <= ((uint32_t)(local_r12 + 1))) {
        Arg1 = *(uint64_t *)(v_rip + 0x42AB72) + 104;
        v_stack_m528 = 0;
        a4 = 0;
        Arg3 = 0;
        Arg2 = 0;
        result = KeWaitForSingleObject(Arg1, Arg2, Arg3, a4);
    }
    v_stack_m4F7 = 0;
    v_stack_m4F4 = 0;
loc_00AE1807:
    v_stack_m4E0 = 0;
    v_stack_m4DC = 0;
    *(uint32_t *)(local_rsp - 0x448 - 0x7C) = (uint32_t)((uint32_t)(0x80000000ULL));
    local_r12 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(0x80000000ULL)))) >> (1));
    local_r12 = (uint8_t)((local_r12) & ((uint8_t)(local_r12 + 1)));
    result = 0;
    if ((((uint8_t)((uint32_t)(0x80000000ULL))) & (8)) != 0) { result = (uint32_t)(local_r12 + 1); }
    *(uint32_t *)(local_rsp - 0x448 - 0x80) = (uint32_t)(result);
    if (((16) & ((uint8_t)((uint32_t)(0x80000000ULL)))) != 0) {
        result = PopAcquirePolicyLock(16, Arg2, Arg3, a4);
        Arg1 = 128;
        result = PopResetCBTriggers(Arg1, Arg2, Arg3, a4);
        result = PopReleasePolicyLock(Arg1, Arg2, Arg3, a4);
    }
    local_rsi = 0;
    Arg1 = (condition_is_below) ? 1 : 0;
    *(uint32_t *)(local_rsp - 0x448 - 0x50) = (uint32_t)(Arg1);
    if (!sign_flag) goto loc_00AE189E;
    if (*(uint64_t *)(v_rip + 0x42AB72) == 0) goto loc_00AE189E;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x42AB72) + 0x80))) - ((uint32_t)(local_r12 + 1)));
    local_r14 = 0;
    if (((uint32_t)(result)) <= ((uint32_t)(local_r12 + 1))) {
        local_r14 = 0;
        if (((*(uint8_t *)(*(uint64_t *)(v_rip + 0x42AB72) + 0x8C)) & ((uint8_t)(local_r12 + 1))) != 0) { local_r14 = (uint32_t)(local_r12 + 1); }
        v_stack_m4E0 = (uint32_t)(local_r14);
    }
    result = Feature_BatteryChargeLimitV2Support__private_IsEnabledDeviceUsageNoInline(Arg1, Arg2, Arg3, a4);
    local_rdi = 0;
    if ((uint32_t)(result) != 0) {
        local_rdi = 0;
        if (condition_is_below) { local_rdi = (uint32_t)(local_r12 + 1); }
        v_stack_m4DC = (uint32_t)(local_rdi);
    }
    if ((*(uint64_t *)(v_rip + 0x42A791)) == (v_rip + 4368266)) goto loc_00AE1936;
loc_00AE18CB:
    if ((*(uint32_t *)(*(uint64_t *)(v_rip + 0x42A791) - 0x40 + 0x68)) != 2) goto loc_00AE192C;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x42A791)) + 0x8)) != (*(uint64_t *)(v_rip + 0x42A791))) goto loc_00AE2399;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x42A791) + 0x8))) != (*(uint64_t *)(v_rip + 0x42A791))) goto loc_00AE2399;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x42A791) + 0x8)) = *(uint64_t *)(*(uint64_t *)(v_rip + 0x42A791));
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x42A791)) + 0x8) = *(uint64_t *)(*(uint64_t *)(v_rip + 0x42A791) + 0x8);
    *(uint8_t *)(v_rip + 0x42A727) = (uint8_t)(local_r12 + 1);
    result = PopBatteryReadTag(*(uint64_t *)(v_rip + 0x42A791) - 64, Arg2, Arg3, a4);
    if (sign_flag) {
        Arg1 = *(uint64_t *)(v_rip + 0x42A791) - 64;
        result = PopBatteryWaitTag(Arg1, Arg2, Arg3, a4);
    }
loc_00AE192C:
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0x42A791))) != (v_rip + 4368164)) goto loc_00AE18CB;
    local_rsi = 0;
loc_00AE1936:
    goto loc_00AE1985;
loc_00AE1946:
    if ((*(uint32_t *)(*(uint64_t *)(v_rip + 0x42A703) + 0x68)) != ((uint32_t)(local_r12 + 1))) goto loc_00AE1982;
    v_stack_m528 = 0;
    a4 = 0;
    Arg3 = 0;
    Arg2 = 0;
    result = KeWaitForSingleObject(*(uint64_t *)(v_rip + 0x42A703) + 80, Arg2, Arg3, a4);
    result = PopBatteryInitialize(*(uint64_t *)(v_rip + 0x42A703), Arg2, Arg3, a4);
    if (sign_flag) goto loc_00AE1973;
    goto loc_00AE197B;
loc_00AE1973:
    result = PopBatteryWaitTag(*(uint64_t *)(v_rip + 0x42A703), Arg2, Arg3, a4);
loc_00AE197B:
loc_00AE1982:
loc_00AE1985:
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0x42A703))) != (v_rip + 4368062)) goto loc_00AE1946;
    if ((*(uint64_t *)(v_rip + 0x42A6BF)) == (v_rip + 4368056)) goto loc_00AE1B0E;
loc_00AE19B2:
    *(uint64_t *)(local_rsp - 0x448 - 0x8) = v_xmm0;
    result = PopBatteryQueryStatus(*(uint64_t *)(v_rip + 0x42A6BF) - 64, 1, Arg3, a4);
    if (!sign_flag) goto loc_00AE19E5;
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x42A6BF) - 0x40 + 0x68) = 2;
    result = PopBatteryQueueWork(1, 1, Arg3, a4);
    goto loc_00AE1AF4;
loc_00AE19E5:
    result = Feature_BatteryChargeLimitV2Support__private_IsEnabledDeviceUsageNoInline(1, 1, Arg3, a4);
    if ((uint32_t)(result) == 0) goto loc_00AE1A55;
    if ((*(uint8_t *)(v_rip + 0x42A8CC)) == 0) goto loc_00AE1A55;
    if ((uint8_t)((uint32_t)(v_stack_m4DC)) == 0) goto loc_00AE1A55;
loc_00AE1A09:
    Arg1 = (*(uint64_t *)(v_rip + 0x329E1F)) | (0);
    if (condition_is_not_equal) goto loc_00AE1A09;
    local_rsi = (*(uint64_t *)(v_rip + 0x329E1F)) >> (32);
    if (((uint32_t)(*(uint64_t *)(v_rip + 0x329E1F))) != (*(uint32_t *)(*(uint64_t *)(v_rip + 0x42A6BF) - 0x40 + 0x11C))) goto loc_00AE1A34;
    result = *(uint64_t *)(v_rip + 0x329E1F);
    if (((uint32_t)(local_rsi)) != (*(uint32_t *)(*(uint64_t *)(v_rip + 0x42A6BF) - 0x40 + 0x120))) {
        Arg3 = (uint32_t)(local_rsi);
        Arg2 = (uint32_t)(*(uint64_t *)(v_rip + 0x329E1F));
        Arg1 = *(uint64_t *)(v_rip + 0x42A6BF) - 64;
        result = PopBatterySetChargeLimitControl(Arg1, Arg2, Arg3, a4);
        *(uint32_t *)(*(uint64_t *)(v_rip + 0x42A6BF) - 0x40 + 0x11C) = (uint32_t)(*(uint64_t *)(v_rip + 0x329E1F));
        *(uint32_t *)(*(uint64_t *)(v_rip + 0x42A6BF) - 0x40 + 0x120) = (uint32_t)(local_rsi);
    }
loc_00AE1A55:
    result = PopAccountBatteryEnergyChange(*(uint64_t *)(v_rip + 0x42A6BF) - 64, Arg2, Arg3, a4);
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x42A6BF) - 0x40 + 0xA4))))) ^ (*(uint32_t *)(local_rsp - 0x448 - 0x8)));
    if ((((uint8_t)(result)) & (7)) == 0) goto loc_00AE1A75;
    v_stack_m4F4 = 1;
    goto loc_00AE1A8F;
loc_00AE1A75:
    if ((*(uint32_t *)(local_rsp - 0x448 - 0x4)) != ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x42A6BF) - 0x40 + 0xA8))))) goto loc_00AE1A8B;
    if ((*(uint32_t *)(local_rsp - 0x448 + 0x4)) != ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x42A6BF) - 0x40 + 0xB0))))) {
        *(uint8_t *)(local_rsp - 0x448 - 0x80) = 1;
    }
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x42A6BF) - 0x40 + 0xB0))) | (0xFFFFFFFFULL));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x42A6BF) - 0x40 + 0xA4)))) & (2)) != 0) {
        Arg2 = 0;
        Arg1 = *(uint64_t *)(v_rip + 0x42A6BF) - 64;
        result = PopBatteryQueryEstimatedTime(Arg1, Arg2, Arg3, a4);
    }
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x42A6BF) - 0x40 + 0xD0) = (uint32_t)(result);
    local_rsi = 0;
    Arg1 = 0;
    if (((uint32_t)(result)) != -1) { Arg1 = (uint32_t)(result); }
    v_stack_m508 = (uint32_t)(Arg1);
    v_stack_m510 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x42A6BF) - 0x40 + 0xB0)));
    v_stack_m518 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x42A6BF) - 0x40 + 0xAC)));
    v_stack_m520 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x42A6BF) - 0x40 + 0xA8)));
    v_stack_m528 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x42A6BF) - 0x40 + 0xA4)));
    result = DbgPrintEx(146, local_rsi + 3, v_rip + 134370, *(uint64_t *)(v_rip + 0x42A6BF) - 64);
loc_00AE1AF4:
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0x42A6BF))) != (v_rip + 4368036)) goto loc_00AE19B2;
loc_00AE1B0E:
    if (v_stack_m4D8 == 0) goto loc_00AE1CA2;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m4D8 + 0x80))) - (1));
    if (((uint32_t)(result)) > 1) goto loc_00AE1CA2;
    if ((uint8_t)((uint32_t)(v_stack_m4E0)) == 0) goto loc_00AE1BEC;
loc_00AE1B45:
    Arg1 = (uint8_t)(((uint8_t)(*(uint8_t *)(v_rip + 0x385D6B))) | (0));
    if (condition_is_not_equal) goto loc_00AE1B45;
    if (((uint8_t)(*(uint8_t *)(v_rip + 0x385D6B))) == (*(uint8_t *)(v_stack_m4D8 + 0xD8))) goto loc_00AE1CA2;
    if ((uint8_t)((uint8_t)(*(uint8_t *)(v_rip + 0x385D6B))) == 0) goto loc_00AE1B7B;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m4D8 + 0xB4))) | (4));
    goto loc_00AE1B7E;
loc_00AE1B7B:
    Arg1 = (uint32_t)((Arg1) & (0xFFFFFFFBULL));
loc_00AE1B7E:
    *(uint32_t *)(180 + v_stack_m4D8 * 1) = (uint32_t)(Arg1);
    *(uint32_t *)(local_rsp - 0x448 - 0x70) = 0;
    result = *(uint8_t *)(local_rsp - 0x448 - 0x6F);
    if ((((uint8_t)(Arg1)) & (4)) != 0) { result = 1; }
    Arg3 = 0;
    v_stack_m520 = 0;
    *(uint8_t *)(local_rsp - 0x448 - 0x6F) = (uint8_t)(result);
    v_stack_m528 = 4;
    result = PopPrepareIoctl(*(uint64_t *)(v_stack_m4D8 + 0x38), (uint32_t)(0x294074ULL), Arg3, local_rsp - 1096 - 112);
    result = IoSynchronousCallDriver(*(uint64_t *)(v_stack_m4D8 + 0x30), *(uint64_t *)(v_stack_m4D8 + 0x38), Arg3, local_rsp - 1096 - 112);
    if (!sign_flag) goto loc_00AE1BD9;
loc_00AE1BC9:
    result = PopPowerAdapterTraceFailure(v_stack_m4D8, 3, (uint32_t)((uint32_t)(result)), local_rsp - 1096 - 112);
    goto loc_00AE1CA2;
loc_00AE1BD9:
    *(uint32_t *)(v_stack_m4D8 + 0x80) = 1;
    *(uint8_t *)(v_stack_m4D8 + 0xD8) = (uint8_t)((uint8_t)(*(uint8_t *)(v_rip + 0x385D6B)));
    goto loc_00AE1CA2;
loc_00AE1BEC:
    *(uint64_t *)(local_rsp - 0x448 + 0x70) = v_xmm6;
    *(uint64_t *)(local_rsp - 0x448 + 0x80) = v_xmm7;
    *(uint64_t *)(local_rsp - 0x448 + 0x90) = v_xmm8;
    result = PopPowerAdapterQueryStatus(v_stack_m4D8, 1, (uint32_t)((uint32_t)(result)), local_rsp - 1096 - 112);
    if (!sign_flag) goto loc_00AE1C2D;
    goto loc_00AE1BC9;
loc_00AE1C2D:
    *(uint32_t *)(v_stack_m4D8 + 0x80) = 1;
    result = (uint8_t)((result) ^ (*(uint8_t *)(v_stack_m4D8 + 0xB4)));
    Arg1 = (uint8_t)((uint32_t)(v_stack_m4F4));
    if (((1) & ((uint8_t)(result))) != 0) { Arg1 = 1; }
    v_stack_m4F4 = (uint32_t)(Arg1);
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m4D8 + 0x8C))))) == 0) goto loc_00AE1CA6;
    *(uint64_t *)(local_rsp - 0x448 + 0x10) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x448 + 0x30) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x448 + 0x20) = v_xmm1;
    *(uint64_t *)(local_rsp - 0x448 + 0x40) = v_xmm6;
    *(uint64_t *)(local_rsp - 0x448 + 0x50) = v_xmm7;
    *(uint64_t *)(local_rsp - 0x448 + 0x60) = v_xmm8;
    result = PopPowerAdapterPublishRecState(local_rsp - 1096 + 64, local_rsp - 1096 + 16, (uint32_t)((uint32_t)(result)), local_rsp - 1096 - 112);
loc_00AE1CA2:
loc_00AE1CA6:
    if ((uint8_t)((uint8_t)(local_r12 + 1)) != 0) {
        result = PopBatteryUpdateCompositeInformation((uint32_t)(v_stack_m4F4), local_rsp - 1096 + 16, (uint32_t)((uint32_t)(result)), local_rsp - 1096 - 112);
        Arg1 = 1;
        *(uint64_t *)(v_rip + 0x385BFE) = 0;
        v_stack_m4F4 = (uint32_t)(Arg1);
    }
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x448 - 0x7C)))) & (4)) != 0) goto loc_00AE1CC8;
    if ((uint8_t)(Arg1) == 0) goto loc_00AE1D1D;
loc_00AE1CC8:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x385BD6))) != 0) goto loc_00AE1D10;
    a4 = 0;
    result = ((uint32_t)(*(uint32_t *)(v_rip + 0x385BD6))) + (0x11E1A300ULL);
    Arg3 = 0;
    *(uint64_t *)(v_rip + 0x329B1A) = result;
    v_stack_m528 = v_rip + 4354908;
    result = KiSetTimerEx(v_rip + 4355019, 0xFFFFFFFFEE1E5D00ULL, Arg3, a4);
    goto loc_00AE1D1D;
loc_00AE1D10:
    result = KeCancelTimer(v_rip + 4355019, 0xFFFFFFFFEE1E5D00ULL, Arg3, a4);
loc_00AE1D1D:
    v_stack_m4E0 = 0;
    Arg2 = 0;
    v_stack_m4DC = (uint32_t)((uint32_t)(0x80000000ULL));
    Arg1 = (v_rip + 4355019) | (-1);
    *(uint32_t *)(local_rsp - 0x448 - 0x38) = (uint32_t)((uint32_t)(0x80000000ULL));
    *(uint64_t *)(local_rsp - 0x448 + 0xB8) = 0;
    *(uint64_t *)(local_rsp - 0x448 + 0x98) = v_xmm0;
    *(uint32_t *)(local_rsp - 0x448 + 0xA4) = (uint32_t)((uint32_t)(0x80000000ULL));
    result = (uint32_t)(((uint32_t)(0x80000000ULL)) | (0xFFFFFFFFULL));
    *(uint64_t *)(local_rsp - 0x448 - 0x28) = 0;
    *(uint64_t *)(local_rsp - 0x448 + 0xA8) = v_xmm0;
    *(uint32_t *)(local_rsp - 0x448 + 0xC0) = 0;
    *(uint32_t *)(local_rsp - 0x448 + 0xA0) = (uint32_t)(result);
    *(uint32_t *)(local_rsp - 0x448 + 0x9C) = (uint32_t)(result);
    *(uint32_t *)(local_rsp - 0x448 + 0xAC) = (uint32_t)(result);
    *(uint32_t *)(local_rsp - 0x448 - 0x54) = (uint32_t)(result);
    *(uint32_t *)(local_rsp - 0x448 + 0xB0) = (uint32_t)(result);
    *(uint32_t *)(local_rsp - 0x448 + 0xB4) = (uint32_t)(result);
    *(uint32_t *)(local_rsp - 0x448 - 0x7C) = (uint32_t)(result);
    *(uint32_t *)(local_rsp - 0x448 + 0xB8) = (uint32_t)(result);
    *(uint64_t *)(local_rsp - 0x448 - 0x48) = Arg1;
    *(uint64_t *)(local_rsp - 0x448 - 0x40) = Arg1;
    v_stack_m4CC = (uint32_t)(result);
    if ((*(uint32_t *)(v_rip + 0x42A2DA)) != 0) goto loc_00AE1DE8;
    *(uint32_t *)(local_rsp - 0x448 + 0x98) = (uint32_t)(Arg2 + 1);
    if (v_stack_m4E8 != 3) goto loc_00AE208E;
    result = KiQueryUnbiasedInterruptTime((uint8_t)(Arg2 + 1), Arg2, Arg3, (uint32_t)((uint32_t)(result)));
    if (result < 0x11E1A300ULL) goto loc_00AE208E;
    v_stack_m4E8 = (uint32_t)(Arg2 + 1);
    goto loc_00AE208E;
loc_00AE1DE8:
    if ((*(uint64_t *)(v_rip + 0x42A261)) == (v_rip + 4366938)) goto loc_00AE1FD3;
loc_00AE1E08:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x42A261) + 0x64))))) & (231));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x42A261) + 0x64))))) & (10));
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) | (8));
    if (((uint8_t)(result)) != 10) { Arg3 = (uint32_t)(Arg1); }
    Arg1 = 0;
    result = Arg1 + 16;
    if ((((uint8_t)(Arg1 + 16)) & ((uint8_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x448 + 0x98))))) == 0) {
        result = (uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x42A261) + 0x64)));
        result = (uint8_t)((result) & (17));
        result = Arg1 + 16;
        if (((uint8_t)(result)) == 17) { Arg1 = (uint32_t)(result); }
    }
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x42A261) + 0x64))))) & (16));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x42A261) + 0x64)))) & (1)) != 0) goto loc_00AE1E51;
    result = (uint32_t)(-(result));
    result = (uint32_t)((result) & (0xFFFFFFFDULL));
    result = (uint32_t)((result) + (4));
    goto loc_00AE1E5B;
loc_00AE1E51:
    result = (uint32_t)(-(result));
    result = (uint32_t)((result) & (0xFFFFFFFAULL));
    result = (uint32_t)((result) + (8));
loc_00AE1E5B:
    local_rsi = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x448 + 0x98))) ^ ((uint32_t)(Arg1)));
    local_rsi = (uint32_t)((local_rsi) | (Arg3));
    Arg1 = (uint32_t)((Arg1) | (0xFFFFFFFFULL));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x42A261) + 0x68)))) == ((uint32_t)(Arg1))) goto loc_00AE1E86;
    local_r14 = (uint32_t)((uint32_t)(result));
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == ((uint32_t)(Arg1))) { local_r14 = 0; }
    local_r14 = (uint32_t)((local_r14) + ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x42A261) + 0x68)))));
    *(uint32_t *)(local_rsp - 0x448 + 0x9C) = (uint32_t)(local_r14);
    goto loc_00AE1E88;
loc_00AE1E86:
    Arg2 = 0;
loc_00AE1E88:
    local_r13 = Arg2 + 1;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x42A261) + 0x6C)))) != ((uint32_t)(Arg1))) {
        local_r13 = Arg2 + 1;
        if (((uint32_t)(Arg2 + 1)) == ((uint32_t)(Arg1))) { local_r13 = 0; }
        if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x42A261) + 0x6C)))) > ((uint32_t)(local_r13))) { local_r13 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x42A261) + 0x6C))); }
        *(uint32_t *)(local_rsp - 0x448 + 0xA0) = (uint32_t)(local_r13);
    }
    local_rbx = (uint32_t)(*(uint32_t *)(local_rsp - 0x448 - 0x38));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x42A261) + 0x70)))) != ((uint32_t)((uint32_t)(0x80000000ULL)))) {
        local_rbx = (uint32_t)(*(uint32_t *)(local_rsp - 0x448 - 0x38));
        if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x448 - 0x38)))) == ((uint32_t)((uint32_t)(0x80000000ULL)))) { local_rbx = 0; }
        local_rbx = (uint32_t)((local_rbx) + ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x42A261) + 0x70)))));
        *(uint32_t *)(local_rsp - 0x448 + 0xA4) = (uint32_t)(local_rbx);
    }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x42A261) + 0x6C)))) == -1) goto loc_00AE1EF4;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x42A261) + 0x70)))) == ((uint32_t)((uint32_t)(0x80000000ULL)))) goto loc_00AE1EF4;
    local_r11 = (uint32_t)((uint32_t)((uint32_t)(0x80000000ULL)));
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(0x80000000ULL))))) == ((uint32_t)((uint32_t)(0x80000000ULL)))) { local_r11 = 0; }
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x42A261) + 0x6C))) != 0) goto loc_00AE1ED9;
    goto loc_00AE1EEC;
loc_00AE1ED9:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x42A261) + 0x70))) * ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x42A261) + 0x70)))));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x42A261) + 0x6C))))) >> (1));
    result = (uint32_t)((result) + ((uint32_t)(Arg1)));
    Arg2 = 0;
loc_00AE1EEC:
    local_r11 = (uint32_t)((local_r11) + ((uint32_t)(result)));
    v_stack_m4DC = (uint32_t)(local_r11);
loc_00AE1EF4:
    Arg1 = (uint32_t)((Arg1) | (0xFFFFFFFFULL));
    local_r15 = (uint32_t)((uint32_t)(result));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x42A261) + 0x78)))) != ((uint32_t)(Arg1))) {
        local_r15 = (uint32_t)((uint32_t)(result));
        if (((uint32_t)((uint32_t)((uint32_t)(result)))) == ((uint32_t)(Arg1))) { local_r15 = 0; }
        local_r15 = (uint32_t)((local_r15) + ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x42A261) + 0x78)))));
        *(uint32_t *)(local_rsp - 0x448 + 0xAC) = (uint32_t)(local_r15);
    }
    local_r12 = (uint32_t)((uint32_t)(result));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x42A261) + 0x80)))) != ((uint32_t)(Arg1))) {
        local_r12 = (uint32_t)((uint32_t)(result));
        if (((uint32_t)((uint32_t)((uint32_t)(result)))) == ((uint32_t)(Arg1))) { local_r12 = 0; }
        local_r12 = (uint32_t)((local_r12) + ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x42A261) + 0x80)))));
        *(uint32_t *)(local_rsp - 0x448 + 0xB4) = (uint32_t)(local_r12);
    }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x42A261) + 0x7C)))) != ((uint32_t)(Arg1))) {
        a4 = (uint32_t)((uint32_t)(result));
        if (((uint32_t)((uint32_t)((uint32_t)(result)))) == ((uint32_t)(Arg1))) { a4 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x42A261) + 0x7C))); }
        *(uint32_t *)(local_rsp - 0x448 - 0x54) = (uint32_t)(a4);
        *(uint32_t *)(local_rsp - 0x448 + 0xB0) = (uint32_t)(a4);
    }
    local_r10 = (uint32_t)((uint32_t)(result));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x42A261) + 0x84)))) != ((uint32_t)(Arg1))) {
        local_r10 = (uint32_t)((uint32_t)(result));
        if (((uint32_t)((uint32_t)((uint32_t)(result)))) == ((uint32_t)(Arg1))) { local_r10 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x42A261) + 0x84))); }
        *(uint32_t *)(local_rsp - 0x448 - 0x7C) = (uint32_t)(local_r10);
        *(uint32_t *)(local_rsp - 0x448 + 0xB8) = (uint32_t)(local_r10);
    }
    result = Feature_BatteryChargeLimitV2Support__private_IsEnabledDeviceUsageNoInline(Arg1, Arg2, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x42A261) + 0x6C)), a4);
    Arg1 = 0;
    if ((uint32_t)(result) == 0) goto loc_00AE1FA8;
    if ((*(uint8_t *)(v_rip + 0x42A351)) == 0) goto loc_00AE1FA8;
    *(uint64_t *)(local_rsp - 0x448 - 0x28) = (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x42A261) + 0x8C));
    *(uint32_t *)(local_rsp - 0x448 + 0xC0) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x42A261) + 0x8C)));
    if (((16) & ((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x42A0EB))))) == 0) goto loc_00AE1FA8;
    if (((16) & ((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x42A261) + 0x88))))) == 0) {
    }
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0x42A261))) != (v_rip + 4366494)) goto loc_00AE1E08;
    *(uint32_t *)(local_rsp - 0x448 + 0x98) = (uint32_t)(local_rsi);
loc_00AE1FD3:
    if ((((uint8_t)(local_rsi)) & (2)) != 0) {
        local_rsi = (uint32_t)((local_rsi) & (0xFFFFFFFBULL));
        *(uint32_t *)(local_rsp - 0x448 + 0x98) = (uint32_t)(local_rsi);
    }
    if (((1) & ((uint8_t)(local_rsi))) != 0) goto loc_00AE207F;
    local_r12 = 0;
    if ((*(uint32_t *)(v_rip + 0x3858B9)) != 0) goto loc_00AE2091;
    if ((*(uint64_t *)(v_rip + 0x42A048)) == (v_rip + 4366401)) goto loc_00AE2091;
loc_00AE2017:
    result = (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x42A048) + 0x90)) - 1;
    local_r14 = 0;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x42A048) + 0x90)) - 1)) <= -3) {
        result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x42A048) + 0x90)) - 1) * (*(uint32_t *)(*(uint64_t *)(v_rip + 0x42A048) + 0x68)));
        Arg2 = 0;
        local_r14 = (uint32_t)((0) - ((uint32_t)(result)));
    }
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0x42A048))) != (v_rip + 4366401)) goto loc_00AE2017;
    if ((uint32_t)(local_r14) == 0) goto loc_00AE2091;
loc_00AE204E:
    result = PopBatteryQueryEstimatedTime(*(uint64_t *)(v_rip + 0x42A006) - 64, (uint32_t)((uint32_t)(local_r14)), (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x42A048) + 0x90)), (uint32_t)(*(uint32_t *)(local_rsp - 0x448 - 0x54)));
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(local_r14))) | (0xFFFFFFFFULL));
    local_rbx = (uint32_t)(v_stack_m4CC);
    if (((uint32_t)(result)) != Arg2) {
        Arg1 = 0;
        if (((uint32_t)((uint32_t)(v_stack_m4CC))) != Arg2) { Arg1 = (uint32_t)((uint32_t)(v_stack_m4CC)); }
        local_rbx = result + Arg1 * 1;
    }
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0x42A006))) != (v_rip + 4366401)) goto loc_00AE204E;
    v_stack_m4CC = (uint32_t)(local_rbx);
    goto loc_00AE2091;
loc_00AE207F:
    if ((((uint8_t)(local_rsi)) & (4)) != 0) {
        result = PopEstimateChargeTime(Arg1, Arg2, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x42A048) + 0x90)), (uint32_t)(*(uint32_t *)(local_rsp - 0x448 - 0x54)));
        *(uint64_t *)(local_rsp - 0x448 - 0x48) = result;
    }
    local_r12 = 0;
loc_00AE2091:
    local_r14 = (uint8_t)(((uint8_t)(local_rsi)) & (1));
    if (((uint32_t)((uint32_t)(v_stack_m4E8))) != 2) goto loc_00AE20A5;
    if ((uint8_t)(local_r14) == 0) goto loc_00AE20AF;
loc_00AE20A5:
    if (((uint32_t)((uint32_t)(v_stack_m4E8))) != 3) goto loc_00AE20B4;
    if ((uint8_t)(local_r14) != 0) {
        v_stack_m4E8 = 1;
    }
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x429FA6))) & (16));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_rsi))) & (16));
    if (((uint32_t)(result)) == ((uint32_t)(Arg1))) goto loc_00AE225D;
    v_stack_m518 = 0;
    v_stack_m520 = 0;
    result = ((uint32_t)(Arg1) != 0) ? 1 : 0;
    v_stack_m528 = 0;
    v_stack_m4F8 = (uint8_t)(result);
    a4 = 0;
    *(uint32_t *)(local_rsp - 0x448 - 0x30) = (uint32_t)((uint8_t)(result));
    result = ZwUpdateWnfStateData(v_rip - 11277580, v_stack_m4F8, 1, a4);
    result = PopSetPowerSettingValueAcDc(v_rip - 11241934, 16 - 12, local_rsp - 1096 - 48, a4);
    if ((*(uint32_t *)(v_rip + 0x325626)) <= 5) goto loc_00AE225D;
    result = tlgKeywordOn(v_rip + 3298828, 16 - 12, (uint32_t)((uint32_t)(result)), a4);
    if ((uint8_t)(result) != 0) {
        Arg1 = v_stack_m4F8;
        result = v_stack_m4EC;
        *(uint64_t *)(local_rsp - 0x448 + 0x330) = result;
        Arg2 = v_rip + 132640;
        result = local_rsp - 1096 - 52;
        *(uint32_t *)(local_rsp - 0x448 - 0x2C) = (uint32_t)((uint32_t)((uint32_t)(result)));
        Arg3 = v_stack_m4E0;
        a4 = v_rip + 132924;
        *(uint64_t *)(local_rsp - 0x448 + 0x340) = result;
        result = local_rsp - 1096 - 44;
        v_stack_m4EC = (uint8_t)(Arg1);
        if (((1) & ((uint8_t)(Arg3))) == 0) { Arg2 = a4; }
        *(uint64_t *)(local_rsp - 0x448 + 0x350) = result;
        Arg1 = local_rsp - 1096 + 864;
        *(uint64_t *)(local_rsp - 0x448 + 0x338) = 1;
        *(uint32_t *)(local_rsp - 0x448 - 0x34) = (uint32_t)((uint32_t)((uint32_t)(result)));
        *(uint64_t *)(local_rsp - 0x448 + 0x348) = 4;
        *(uint64_t *)(local_rsp - 0x448 + 0x358) = 4;
        result = tlgCreate1Sz_char(Arg1, Arg2, Arg3, a4);
        Arg2 = v_rip + 132692;
        Arg1 = local_rsp - 1096 + 880;
        if ((((uint8_t)(Arg3)) & (2)) == 0) { Arg2 = a4; }
        result = tlgCreate1Sz_char(Arg1, Arg2, Arg3, a4);
        Arg2 = v_rip + 132649;
        Arg1 = local_rsp - 1096 + 896;
        if ((((uint8_t)(Arg3)) & (4)) == 0) { Arg2 = a4; }
        result = tlgCreate1Sz_char(Arg1, Arg2, Arg3, a4);
        Arg2 = v_rip + 133166;
        Arg1 = local_rsp - 1096 + 912;
        if ((((uint8_t)(Arg3)) & (8)) == 0) { Arg2 = a4; }
        result = tlgCreate1Sz_char(Arg1, Arg2, Arg3, a4);
        result = local_rsp - 1096 - 16;
        *(uint64_t *)(local_rsp - 0x448 - 0x10) = 0x1000000ULL;
        *(uint64_t *)(local_rsp - 0x448 + 0x3A0) = result;
        Arg2 = v_rip - 11093714;
        result = local_rsp - 1096 + 784;
        *(uint64_t *)(local_rsp - 0x448 + 0x3A8) = 8;
        v_stack_m520 = result;
        Arg1 = v_rip + 3298558;
        a4 = 0;
        v_stack_m528 = 10;
        Arg3 = 0;
        result = tlgWriteTransfer_EtwWriteTransfer(Arg1, Arg2, Arg3, a4);
    }
    result = Feature_BatteryChargeLimitV2Support__private_IsEnabledDeviceUsageNoInline(Arg1, Arg2, Arg3, a4);
    if ((uint32_t)(result) == 0) goto loc_00AE22A6;
    if ((*(uint32_t *)(v_rip + 0x429E12)) != ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x448 + 0xBC))))) goto loc_00AE2280;
    if ((*(uint32_t *)(v_rip + 0x429E0A)) == ((uint32_t)(*(uint64_t *)(local_rsp - 0x448 - 0x28)))) goto loc_00AE22A6;
loc_00AE2280:
    result = PopBatteryPublishChargeLimitStatus((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x448 + 0xBC)))), *(uint64_t *)(local_rsp - 0x448 - 0x28), Arg3, a4);
    if (((16) & ((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x429DF7))))) == 0) goto loc_00AE22A6;
    if (((16) & ((uint8_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x448 + 0xBC))))) == 0) {
        local_rsi = *(uint32_t *)(local_rsp - 0x448 + 0x98);
    }
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rsi))) & (64));
    if ((((uint8_t)(local_rsi)) & (32)) == 0) goto loc_00AE22BC;
    result = (uint32_t)(-(result));
    local_rdi = (uint32_t)(-((uint32_t)(*(uint32_t *)(local_rsp - 0x448 + 0xBC))));
    local_rdi = (uint32_t)((local_rdi) + (1));
    goto loc_00AE22BF;
loc_00AE22BC:
loc_00AE22BF:
    if ((*(uint32_t *)(v_rip + 0x429F57)) == 0) goto loc_00AE22F6;
    result = PopAcquireRwLockExclusive(v_rip + 4353346, *(uint64_t *)(local_rsp - 0x448 - 0x28), Arg3, a4);
    *(uint32_t *)(v_rip + 0x429F3C) = 0;
    *(uint32_t *)(v_rip + 0x426D5A) = 0;
    result = PopReleaseRwLock(v_rip + 4353334, *(uint64_t *)(local_rsp - 0x448 - 0x28), Arg3, a4);
    local_rdi = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x448 - 0x50))) | (2));
    goto loc_00AE22FE;
loc_00AE22F6:
loc_00AE22FE:
    result = PopBatteryApplyCompositeState(local_rsp - 1096 + 152, (uint32_t)((uint32_t)((uint32_t)(v_stack_m4CC))), (uint32_t)(v_stack_m4DC), a4);
    if ((uint8_t)(result) != 0) goto loc_00AE231E;
    if ((uint8_t)(v_stack_m4EB) == 0) goto loc_00AE2338;
loc_00AE231E:
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x448 - 0x50))))) | (4));
    if ((uint8_t)(result) == 0) { Arg2 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x448 - 0x50))); }
    result = PopEvaluateWeakChargerState((uint8_t)(local_r14), Arg2, (uint32_t)(v_stack_m4DC), a4);
    goto loc_00AE233E;
loc_00AE2338:
loc_00AE233E:
    *(uint64_t *)(v_rip + 0x429ECE) = *(uint64_t *)(result);
    result = *(uint64_t *)(result);
    if ((*(uint64_t *)(v_rip + 0x429ECA)) != 0) {
        Arg2 = 0;
        Arg1 = v_rip + 4366015;
        result = ExfUnblockPushLock(Arg1, Arg2, (uint32_t)(v_stack_m4DC), a4);
    }
    if (((uint32_t)((uint32_t)(0x80000000ULL))) == 0x80000000ULL) goto loc_00AE23A0;
    goto loc_00AE1807;
loc_00AE2399:
loc_00AE23A0:
    if ((*(uint64_t *)(v_rip + 0x429CA9)) == (v_rip + 4365474)) goto loc_00AE23D1;
loc_00AE23BA:
    Arg2 = 0;
    result = PopBatteryQueryStatus(*(uint64_t *)(v_rip + 0x429CA9) - 64, Arg2, (uint32_t)(v_stack_m4DC), a4);
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0x429CA9))) != (v_rip + 4365462)) goto loc_00AE23BA;
loc_00AE23D1:
    if (v_stack_m4D8 == 0) goto loc_00AE23EE;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m4D8 + 0x80))) - (1));
    if (((uint32_t)(result)) <= 1) {
        Arg2 = 0;
        Arg1 = v_stack_m4D8;
        result = PopPowerAdapterQueryStatus(Arg1, Arg2, (uint32_t)(v_stack_m4DC), a4);
    }
    if ((*(uint32_t *)(v_rip + 0x3854CB)) == 0) {
        v_stack_m518 = 0;
        Arg2 = local_rsp - 1096 - 72;
        v_stack_m520 = 0;
        Arg1 = v_rip - 11278665;
        a4 = 0;
        v_stack_m528 = 0;
        Arg3 = 8;
        result = ZwUpdateWnfStateData(Arg1, Arg2, Arg3, a4);
    }
    if ((*(uint32_t *)(v_rip + 0x38548C)) != 0) goto loc_00AE2467;
    result = PopBatteryEstimatesSpoiled(Arg1, Arg2, Arg3, a4);
    if (((uint32_t)((uint32_t)(v_stack_m4CC))) == -1) goto loc_00AE2440;
    if ((uint8_t)(result) == 0) {
        Arg1 = (uint32_t)((uint32_t)(v_stack_m4CC));
        *(uint64_t *)(local_rsp - 0x448 - 0x40) = Arg1;
    }
    v_stack_m518 = 0;
    v_stack_m520 = 0;
    a4 = 0;
    v_stack_m528 = 0;
    result = ZwUpdateWnfStateData(v_rip - 11278845, local_rsp - 1096 - 64, 8, a4);
    goto loc_00AE246B;
loc_00AE2467:
loc_00AE246B:
    if ((*(uint32_t *)(v_rip + 0x3252D6)) >= = 5) {
        result = *(uint32_t *)(v_rip + 0x385442);
        Arg2 = v_rip - 11093034;
        v_stack_m4E4 = (uint32_t)(result);
        Arg1 = v_rip + 3297976;
        result = v_stack_m4E4;
        *(uint64_t *)(local_rsp - 0x448 + 0x2B8) = 4;
        *(uint64_t *)(local_rsp - 0x448 + 0x2B0) = result;
        a4 = 0;
        result = *(uint64_t *)(local_rsp - 0x448 - 0x48);
        Arg3 = 0;
        v_stack_m4D8 = result;
        result = v_stack_m4D8;
        *(uint64_t *)(local_rsp - 0x448 + 0x2C0) = result;
        result = *(uint32_t *)(v_rip + 0x3853EC);
        v_stack_m4F0 = (uint32_t)(result);
        result = v_stack_m4F0;
        *(uint64_t *)(local_rsp - 0x448 + 0x2D0) = result;
        result = v_stack_m4D0;
        *(uint64_t *)(local_rsp - 0x448 + 0x2E0) = result;
        result = *(uint64_t *)(local_rsp - 0x448 - 0x40);
        *(uint64_t *)(local_rsp - 0x448 - 0x78) = result;
        result = local_rsp - 1096 - 120;
        *(uint64_t *)(local_rsp - 0x448 + 0x2F0) = result;
        result = v_stack_m4F7;
        *(uint64_t *)(local_rsp - 0x448 + 0x300) = result;
        result = local_rsp - 1096 + 656;
        v_stack_m520 = result;
        v_stack_m528 = 8;
        *(uint64_t *)(local_rsp - 0x448 + 0x2C8) = 8;
        *(uint64_t *)(local_rsp - 0x448 + 0x2D8) = 4;
        v_stack_m4D0 = (uint32_t)((uint32_t)(v_stack_m4CC));
        *(uint64_t *)(local_rsp - 0x448 + 0x2E8) = 4;
        *(uint64_t *)(local_rsp - 0x448 + 0x2F8) = 8;
        v_stack_m4F7 = (uint8_t)(v_stack_m4F7);
        *(uint64_t *)(local_rsp - 0x448 + 0x308) = 1;
        result = tlgWriteTransfer_EtwWriteTransfer(Arg1, Arg2, Arg3, a4);
    }
    if (condition_is_equal) goto loc_00AE2CDB;
    *(uint32_t *)(local_rsp - 0x448 + 0xE8) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x429B3E)));
    a4 = 0;
    *(uint64_t *)(local_rsp - 0x448 + 0xC8) = v_xmm0;
    *(uint32_t *)(local_rsp - 0x448 + 0x100) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x429A9D)));
    v_stack_m518 = 0;
    v_stack_m520 = 0;
    *(uint64_t *)(local_rsp - 0x448 + 0xEC) = v_xmm0;
    *(uint32_t *)(local_rsp - 0x448 + 0xFC) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x429A84)));
    *(uint64_t *)(local_rsp - 0x448 + 0xD8) = v_xmm1;
    v_stack_m528 = 0;
    result = ZwUpdateWnfStateData(v_rip - 11279373, local_rsp - 1096 + 200, a4 + 60, a4);
    result = Feature_BatteryChargeLimitV2Support__private_IsEnabledDeviceUsageNoInline(v_rip - 11279373, local_rsp - 1096 + 200, a4 + 60, a4);
    if ((uint32_t)(result) != 0) goto loc_00AE28E3;
    if ((*(uint32_t *)(v_rip + 0x325155)) <= 5) goto loc_00AE2C10;
    result = tlgKeywordOn(v_rip + 3297598, local_rsp - 1096 + 200, a4 + 60, a4);
    if ((uint8_t)(result) == 0) goto loc_00AE2C10;
    *(uint64_t *)(local_rsp - 0x448 + 0x130) = v_stack_m4D0;
    v_stack_m4D0 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x429A0A)));
    *(uint64_t *)(local_rsp - 0x448 + 0x138) = 4;
    Arg2 = v_rip + 132079;
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x429A42))))) == 0) { Arg2 = v_rip + 132122; }
    result = tlgCreate1Sz_char(local_rsp - 1096 + 320, Arg2, (uint32_t)(*(uint32_t *)(v_rip + 0x429A42)), (uint32_t)(*(uint32_t *)(v_rip + 0x429A0A)));
    Arg2 = v_rip + 132051;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x429A42)))) & (2)) == 0) { Arg2 = v_rip + 131644; }
    result = tlgCreate1Sz_char(local_rsp - 1096 + 336, Arg2, (uint32_t)(*(uint32_t *)(v_rip + 0x429A42)), (uint32_t)(*(uint32_t *)(v_rip + 0x429A0A)));
    Arg2 = v_rip + 132098;
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x429A42))))) == 0) { Arg2 = v_rip + 131644; }
    result = tlgCreate1Sz_char(local_rsp - 1096 + 352, Arg2, (uint32_t)(*(uint32_t *)(v_rip + 0x429A42)), (uint32_t)(*(uint32_t *)(v_rip + 0x429A0A)));
    Arg2 = v_rip + 132040;
    if (((8) & ((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x429A42))))) == 0) { Arg2 = v_rip + 131644; }
    result = tlgCreate1Sz_char(local_rsp - 1096 + 368, Arg2, (uint32_t)(*(uint32_t *)(v_rip + 0x429A42)), (uint32_t)(*(uint32_t *)(v_rip + 0x429A0A)));
    Arg2 = v_rip + 132124;
    if (((16) & ((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x429A42))))) == 0) { Arg2 = v_rip + 131644; }
    result = tlgCreate1Sz_char(local_rsp - 1096 + 384, Arg2, (uint32_t)(*(uint32_t *)(v_rip + 0x429A42)), (uint32_t)(*(uint32_t *)(v_rip + 0x429A0A)));
    Arg2 = v_rip + 132046;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x429A42)))) & (32)) == 0) { Arg2 = v_rip + 131644; }
    result = tlgCreate1Sz_char(local_rsp - 1096 + 400, Arg2, (uint32_t)(*(uint32_t *)(v_rip + 0x429A42)), (uint32_t)(*(uint32_t *)(v_rip + 0x429A0A)));
    Arg2 = v_rip + 131731;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x429A42)))) & (64)) == 0) { Arg2 = v_rip + 131644; }
    result = tlgCreate1Sz_char(local_rsp - 1096 + 416, Arg2, (uint32_t)(*(uint32_t *)(v_rip + 0x429A42)), (uint32_t)(*(uint32_t *)(v_rip + 0x429A0A)));
    Arg2 = v_rip + 131672;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x429A42)))) & (128)) == 0) { Arg2 = v_rip + 131644; }
    result = tlgCreate1Sz_char(local_rsp - 1096 + 432, Arg2, (uint32_t)(*(uint32_t *)(v_rip + 0x429A42)), (uint32_t)(*(uint32_t *)(v_rip + 0x429A0A)));
    Arg2 = v_rip + 131738;
    if (((*(uint8_t *)(v_rip + 0x429B91)) & (1)) == 0) { Arg2 = v_rip + 131644; }
    result = tlgCreate1Sz_char(local_rsp - 1096 + 448, Arg2, (uint32_t)(*(uint32_t *)(v_rip + 0x429A42)), (uint32_t)(*(uint32_t *)(v_rip + 0x429A0A)));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x429953))) != 0) goto loc_00AE2757;
    goto loc_00AE276A;
loc_00AE2757:
    result = (uint32_t)((0) * (*(uint32_t *)(v_rip + 0x429906)));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x429953))))) >> (1));
    Arg2 = 0;
    result = (uint32_t)((result) + ((uint32_t)(Arg1)));
loc_00AE276A:
    v_stack_m4E4 = (uint32_t)(result);
    *(uint64_t *)(local_rsp - 0x448 + 0x1D0) = v_stack_m4E4;
    *(uint64_t *)(local_rsp - 0x448 + 0x1D8) = 4;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x429953))) != 0) goto loc_00AE278F;
    goto loc_00AE27A1;
loc_00AE278F:
    Arg2 = 0;
    result = ((uint32_t)(*(uint32_t *)(v_rip + 0x4298CF))) * ((uint32_t)(*(uint32_t *)(v_rip + 0x4298CF)));
loc_00AE27A1:
    v_stack_m4F0 = (uint32_t)(result);
    *(uint64_t *)(local_rsp - 0x448 + 0x1E8) = 4;
    *(uint64_t *)(local_rsp - 0x448 + 0x1E0) = v_stack_m4F0;
    *(uint32_t *)(local_rsp - 0x448 - 0x5C) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x42988A)));
    *(uint64_t *)(local_rsp - 0x448 + 0x1F0) = local_rsp - 1096 - 92;
    *(uint64_t *)(local_rsp - 0x448 + 0x200) = local_rsp - 1096 - 88;
    *(uint32_t *)(local_rsp - 0x448 - 0x6C) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x42986F)));
    *(uint64_t *)(local_rsp - 0x448 + 0x210) = local_rsp - 1096 - 108;
    *(uint32_t *)(local_rsp - 0x448 - 0x68) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x42985F)));
    *(uint64_t *)(local_rsp - 0x448 + 0x220) = local_rsp - 1096 - 104;
    *(uint32_t *)(local_rsp - 0x448 - 0x64) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x42980F)));
    *(uint64_t *)(local_rsp - 0x448 + 0x230) = local_rsp - 1096 - 100;
    *(uint64_t *)(local_rsp - 0x448 + 0x240) = local_rsp - 1096 - 96;
    Arg2 = v_rip + 131662;
    if (((*(uint32_t *)(v_rip + 0x4298E5)) & (0x40000000ULL)) == 0) { Arg2 = v_rip + 131503; }
    *(uint64_t *)(local_rsp - 0x448 + 0x1F8) = 4;
    *(uint32_t *)(local_rsp - 0x448 - 0x58) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x429953)));
    *(uint64_t *)(local_rsp - 0x448 + 0x208) = 4;
    *(uint64_t *)(local_rsp - 0x448 + 0x218) = 4;
    *(uint64_t *)(local_rsp - 0x448 + 0x228) = 4;
    *(uint64_t *)(local_rsp - 0x448 + 0x238) = 4;
    *(uint32_t *)(local_rsp - 0x448 - 0x60) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x429A0A)));
    *(uint64_t *)(local_rsp - 0x448 + 0x248) = 4;
    result = tlgCreate1Sz_char(local_rsp - 1096 + 592, Arg2, (uint32_t)(*(uint32_t *)(v_rip + 0x429953)), (uint32_t)(*(uint32_t *)(v_rip + 0x429A0A)));
    *(uint64_t *)(local_rsp - 0x448 + 0x260) = local_rsp - 1096 - 120;
    *(uint32_t *)(local_rsp - 0x448 - 0x78) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x429802)));
    *(uint64_t *)(local_rsp - 0x448 + 0x270) = v_stack_m4D8;
    v_stack_m520 = local_rsp - 1096 + 272;
    v_stack_m528 = 23;
    *(uint64_t *)(local_rsp - 0x448 + 0x268) = 4;
    v_stack_m4D8 = (uint32_t)((uint32_t)((uint32_t)(result)));
    goto loc_00AE2BF3;
loc_00AE28E3:
    if ((*(uint32_t *)(v_rip + 0x324E5E)) <= 5) goto loc_00AE2C10;
    result = tlgKeywordOn(v_rip + 3296839, v_rip - 11094638, (uint32_t)(*(uint32_t *)(v_rip + 0x429953)), (uint32_t)(*(uint32_t *)(v_rip + 0x429A0A)));
    if ((uint8_t)(result) == 0) goto loc_00AE2C10;
    *(uint64_t *)(local_rsp - 0x448 + 0x130) = v_stack_m4D8;
    v_stack_m4D8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x429713)));
    *(uint64_t *)(local_rsp - 0x448 + 0x138) = 4;
    Arg2 = v_rip + 131320;
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x42974B))))) == 0) { Arg2 = v_rip + 131363; }
    result = tlgCreate1Sz_char(local_rsp - 1096 + 320, Arg2, (uint32_t)(*(uint32_t *)(v_rip + 0x42974B)), (uint32_t)(*(uint32_t *)(v_rip + 0x429713)));
    Arg2 = v_rip + 131292;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x42974B)))) & (2)) == 0) { Arg2 = v_rip + 130885; }
    result = tlgCreate1Sz_char(local_rsp - 1096 + 336, Arg2, (uint32_t)(*(uint32_t *)(v_rip + 0x42974B)), (uint32_t)(*(uint32_t *)(v_rip + 0x429713)));
    Arg2 = v_rip + 131339;
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x42974B))))) == 0) { Arg2 = v_rip + 130885; }
    result = tlgCreate1Sz_char(local_rsp - 1096 + 352, Arg2, (uint32_t)(*(uint32_t *)(v_rip + 0x42974B)), (uint32_t)(*(uint32_t *)(v_rip + 0x429713)));
    Arg2 = v_rip + 131281;
    if (((8) & ((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x42974B))))) == 0) { Arg2 = v_rip + 130885; }
    result = tlgCreate1Sz_char(local_rsp - 1096 + 368, Arg2, (uint32_t)(*(uint32_t *)(v_rip + 0x42974B)), (uint32_t)(*(uint32_t *)(v_rip + 0x429713)));
    Arg2 = v_rip + 131365;
    if (((16) & ((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x42974B))))) == 0) { Arg2 = v_rip + 130885; }
    result = tlgCreate1Sz_char(local_rsp - 1096 + 384, Arg2, (uint32_t)(*(uint32_t *)(v_rip + 0x42974B)), (uint32_t)(*(uint32_t *)(v_rip + 0x429713)));
    Arg2 = v_rip + 131287;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x42974B)))) & (32)) == 0) { Arg2 = v_rip + 130885; }
    result = tlgCreate1Sz_char(local_rsp - 1096 + 400, Arg2, (uint32_t)(*(uint32_t *)(v_rip + 0x42974B)), (uint32_t)(*(uint32_t *)(v_rip + 0x429713)));
    Arg2 = v_rip + 130972;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x42974B)))) & (64)) == 0) { Arg2 = v_rip + 130885; }
    result = tlgCreate1Sz_char(local_rsp - 1096 + 416, Arg2, (uint32_t)(*(uint32_t *)(v_rip + 0x42974B)), (uint32_t)(*(uint32_t *)(v_rip + 0x429713)));
    Arg2 = v_rip + 130913;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x42974B)))) & (128)) == 0) { Arg2 = v_rip + 130885; }
    result = tlgCreate1Sz_char(local_rsp - 1096 + 432, Arg2, (uint32_t)(*(uint32_t *)(v_rip + 0x42974B)), (uint32_t)(*(uint32_t *)(v_rip + 0x429713)));
    Arg2 = v_rip + 130979;
    if (((*(uint8_t *)(v_rip + 0x42989A)) & (1)) == 0) { Arg2 = v_rip + 130885; }
    result = tlgCreate1Sz_char(local_rsp - 1096 + 448, Arg2, (uint32_t)(*(uint32_t *)(v_rip + 0x42974B)), (uint32_t)(*(uint32_t *)(v_rip + 0x429713)));
    Arg2 = v_rip + 130917;
    if (((*(uint8_t *)(v_rip + 0x42987D)) & (1)) == 0) { Arg2 = v_rip + 130885; }
    result = tlgCreate1Sz_char(local_rsp - 1096 + 464, Arg2, (uint32_t)(*(uint32_t *)(v_rip + 0x42974B)), (uint32_t)(*(uint32_t *)(v_rip + 0x429713)));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x42963E))) != 0) goto loc_00AE2A6C;
    goto loc_00AE2A7F;
loc_00AE2A6C:
    result = (uint32_t)((0) * (*(uint32_t *)(v_rip + 0x4295F1)));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x42963E))))) >> (1));
    Arg2 = 0;
    result = (uint32_t)((result) + ((uint32_t)(Arg1)));
loc_00AE2A7F:
    *(uint32_t *)(local_rsp - 0x448 - 0x78) = (uint32_t)(result);
    *(uint64_t *)(local_rsp - 0x448 + 0x1E0) = local_rsp - 1096 - 120;
    *(uint64_t *)(local_rsp - 0x448 + 0x1E8) = 4;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x42963E))) != 0) goto loc_00AE2AA2;
    goto loc_00AE2AB4;
loc_00AE2AA2:
    Arg2 = 0;
    result = ((uint32_t)(*(uint32_t *)(v_rip + 0x4295BC))) * ((uint32_t)(*(uint32_t *)(v_rip + 0x4295BC)));
loc_00AE2AB4:
    *(uint32_t *)(local_rsp - 0x448 - 0x60) = (uint32_t)(result);
    *(uint64_t *)(local_rsp - 0x448 + 0x1F8) = 4;
    *(uint64_t *)(local_rsp - 0x448 + 0x1F0) = local_rsp - 1096 - 96;
    *(uint32_t *)(local_rsp - 0x448 - 0x64) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x429579)));
    *(uint64_t *)(local_rsp - 0x448 + 0x200) = local_rsp - 1096 - 100;
    *(uint64_t *)(local_rsp - 0x448 + 0x210) = local_rsp - 1096 - 104;
    *(uint32_t *)(local_rsp - 0x448 - 0x6C) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x42955E)));
    *(uint64_t *)(local_rsp - 0x448 + 0x220) = local_rsp - 1096 - 108;
    *(uint32_t *)(local_rsp - 0x448 - 0x58) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x42954E)));
    *(uint64_t *)(local_rsp - 0x448 + 0x230) = local_rsp - 1096 - 88;
    *(uint32_t *)(local_rsp - 0x448 - 0x5C) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x4294FE)));
    *(uint64_t *)(local_rsp - 0x448 + 0x240) = local_rsp - 1096 - 92;
    *(uint64_t *)(local_rsp - 0x448 + 0x250) = v_stack_m4D0;
    Arg2 = v_rip + 130875;
    if (((*(uint32_t *)(v_rip + 0x4295D2)) & (0x40000000ULL)) == 0) { Arg2 = v_rip + 130717; }
    *(uint64_t *)(local_rsp - 0x448 + 0x208) = 4;
    *(uint32_t *)(local_rsp - 0x448 - 0x68) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x42963E)));
    *(uint64_t *)(local_rsp - 0x448 + 0x218) = 4;
    *(uint64_t *)(local_rsp - 0x448 + 0x228) = 4;
    *(uint64_t *)(local_rsp - 0x448 + 0x238) = 4;
    *(uint64_t *)(local_rsp - 0x448 + 0x248) = 4;
    v_stack_m4D0 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x429713)));
    *(uint64_t *)(local_rsp - 0x448 + 0x258) = 4;
    result = tlgCreate1Sz_char(local_rsp - 1096 + 608, Arg2, (uint32_t)(*(uint32_t *)(v_rip + 0x42963E)), (uint32_t)(*(uint32_t *)(v_rip + 0x429713)));
    *(uint64_t *)(local_rsp - 0x448 + 0x270) = v_stack_m4E4;
    v_stack_m4E4 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x4294EF)));
    *(uint64_t *)(local_rsp - 0x448 + 0x280) = v_stack_m4F0;
    v_stack_m520 = local_rsp - 1096 + 272;
    v_stack_m528 = 24;
    v_stack_m4F0 = (uint32_t)((uint32_t)((uint32_t)(result)));
    *(uint64_t *)(local_rsp - 0x448 + 0x288) = 4;
loc_00AE2BF3:
    a4 = 0;
    *(uint64_t *)(local_rsp - 0x448 + 0x278) = 4;
    Arg3 = 0;
    result = tlgWriteTransfer_EtwWriteTransfer(v_rip + 3296061, v_rip - 11095991, Arg3, a4);
loc_00AE2C10:
    if (v_stack_m4E8 != 1) goto loc_00AE2C58;
    if ((uint8_t)(local_r14) != 0) goto loc_00AE2C2F;
    *(uint64_t *)(local_rsp - 0x448 - 0x18) = *(uint64_t *)(result);
    goto loc_00AE2C33;
loc_00AE2C2F:
    *(uint64_t *)(local_rsp - 0x448 - 0x18) = 0;
loc_00AE2C33:
    v_stack_m518 = 0;
    v_stack_m520 = 0;
    a4 = 0;
    v_stack_m528 = 0;
    result = ZwUpdateWnfStateData(v_rip - 11299592, local_rsp - 1096 - 24, 8, a4);
loc_00AE2C58:
    if ((uint8_t)((uint32_t)(v_stack_m4F4)) == 0) goto loc_00AE2CDB;
    v_stack_m518 = 0;
    *(uint64_t *)(local_rsp - 0x448 - 0x20) = 0;
    a4 = 0;
    v_stack_m520 = 0;
    v_stack_m528 = 0;
    result = ZwUpdateWnfStateData(v_rip - 11281385, local_rsp - 1096 - 32, 8, a4);
    if ((*(uint32_t *)(v_rip + 0x324AB7)) >= = 5) {
        v_stack_m4D8 = (uint32_t)(result);
        Arg2 = v_rip - 11097218;
        result = v_stack_m4D8;
        *(uint64_t *)(local_rsp - 0x448 + 0x3D8) = 4;
        *(uint64_t *)(local_rsp - 0x448 + 0x3D0) = result;
        Arg1 = v_rip + 3295884;
        result = local_rsp - 1096 + 944;
        a4 = 0;
        v_stack_m520 = result;
        Arg3 = 0;
        v_stack_m528 = 3;
        result = tlgWriteTransfer_EtwWriteTransfer(Arg1, Arg2, Arg3, a4);
    }
    result = PopReleaseRwLock(v_rip + 4363070, Arg2, Arg3, a4);
    result = PopReleaseRwLock(v_rip + 4365330, Arg2, Arg3, a4);
    Arg1 = (*(uint64_t *)(local_rsp - 0x448 + 0x3E0)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, a4);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AE1650&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
