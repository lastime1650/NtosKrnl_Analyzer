# EtwpWriteUserEvent

- RVA: `0x00AF2FEC`–`0x00AF47AE` (길이 `6,082` bytes)
- VA: `0x0000000140AF2FEC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D38F4`
- 디코드: `1,463`개 명령, `6,082/6,082` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **71**; 고유 호출 대상: **38**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **8**

### Outgoing calls
- `0x00AF309B` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00AF30B1` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00AF30E5` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (function, `0x002FE1F0`)
- `0x00AF31AE` → [DecodeProviderTraits](../../text/3F/DecodeProviderTraits_function_003FD9D0.md) (function, `0x003FD9D0`)
- `0x00AF329E` → [EtwpLevelKeywordEnabled](../../text/2F/EtwpLevelKeywordEnabled_function_002FD110.md) (function, `0x002FD110`)
- `0x00AF3338` → [EtwpApplyEventIdPayloadFilterOnUserEvent](../9C/EtwpApplyEventIdPayloadFilterOnUserEvent_function_009C50D0.md) (function, `0x009C50D0`)
- `0x00AF3372` → [EtwpIsEventNameFilterEnabled](../../text/3F/EtwpIsEventNameFilterEnabled_function_003F1414.md) (function, `0x003F1414`)
- `0x00AF33A7` → [EtwpApplyEventNameFilter](../../text/3F/EtwpApplyEventNameFilter_function_003F10B8.md) (function, `0x003F10B8`)
- `0x00AF33D2` → [ExAcquireRundownProtectionCacheAwareEx](../../text/41/ExAcquireRundownProtectionCacheAwareEx_function_00411F50.md) (function, `0x00411F50`)
- `0x00AF3434` → [ExReleaseRundownProtectionCacheAwareEx](../../text/25/ExReleaseRundownProtectionCacheAwareEx_function_0025F050.md) (function, `0x0025F050`)
- `0x00AF3439` → [Feature_1345841464__private_IsEnabledDeviceUsageNoInline](../../text/4E/Feature_1345841464__private_IsEnabledDeviceUsageNoInline_function_004EF340.md) (function, `0x004EF340`)
- `0x00AF34FE` → [EtwpGetSidExtendedHeaderItem](../9A/EtwpGetSidExtendedHeaderItem_function_009A8D80.md) (function, `0x009A8D80`)
- `0x00AF35C3` → [EtwpApplyLevelKwFilter](../../text/46/EtwpApplyLevelKwFilter_function_00464740.md) (function, `0x00464740`)
- `0x00AF35DD` → [EtwpApplyStackWalkFilterOnUserEvent](../A5/EtwpApplyStackWalkFilterOnUserEvent_function_00A5F7BC.md) (function, `0x00A5F7BC`)
- `0x00AF3620` → [EtwpApplyEventNameFilter](../../text/3F/EtwpApplyEventNameFilter_function_003F10B8.md) (function, `0x003F10B8`)
- `0x00AF3635` → [EtwpGetStackLookasideListEntry](../../text/44/EtwpGetStackLookasideListEntry_function_004468F0.md) (function, `0x004468F0`)
- `0x00AF3672` → [EtwpGetStackExtendedHeaderItem](../../text/44/EtwpGetStackExtendedHeaderItem_function_00443D70.md) (function, `0x00443D70`)
- `0x00AF3682` → [EtwpReleaseStackLookasideListEntry](../../text/41/EtwpReleaseStackLookasideListEntry_function_0041D770.md) (function, `0x0041D770`)
- `0x00AF36BA` → [EtwpGetCrimsonStackKey](../../text/4D/EtwpGetCrimsonStackKey_function_004D68CC.md) (function, `0x004D68CC`)
- `0x00AF3707` → [IoGetStackLimits](../../text/41/IoGetStackLimits_function_0041FD70.md) (function, `0x0041FD70`)
- `0x00AF3738` → [EtwpGetPsmKeyExtendedHeaderItem](../AC/EtwpGetPsmKeyExtendedHeaderItem_function_00AC3EE0.md) (function, `0x00AC3EE0`)
- `0x00AF381B` → [Feature_1345841464__private_IsEnabledDeviceUsageNoInline](../../text/4E/Feature_1345841464__private_IsEnabledDeviceUsageNoInline_function_004EF340.md) (function, `0x004EF340`)
- `0x00AF383B` → [EtwpDereferenceStackEntry](../../text/3F/EtwpDereferenceStackEntry_function_003FC9D0.md) (function, `0x003FC9D0`)
- `0x00AF3855` → [ExReleaseRundownProtectionCacheAwareEx](../../text/25/ExReleaseRundownProtectionCacheAwareEx_function_0025F050.md) (function, `0x0025F050`)
- `0x00AF38B9` → [RtlReadULong64FromUser](../70/RtlReadULong64FromUser_function_00705DCC.md) (function, `0x00705DCC`)
- `0x00AF38CC` → [Feature_1345841464__private_IsEnabledDeviceUsageNoInline](../../text/4E/Feature_1345841464__private_IsEnabledDeviceUsageNoInline_function_004EF340.md) (function, `0x004EF340`)
- `0x00AF3914` → [Feature_1345841464__private_IsEnabledDeviceUsageNoInline](../../text/4E/Feature_1345841464__private_IsEnabledDeviceUsageNoInline_function_004EF340.md) (function, `0x004EF340`)
- `0x00AF3934` → [EtwpDereferenceStackEntry](../../text/3F/EtwpDereferenceStackEntry_function_003FC9D0.md) (function, `0x003FC9D0`)
- `0x00AF394E` → [ExReleaseRundownProtectionCacheAwareEx](../../text/25/ExReleaseRundownProtectionCacheAwareEx_function_0025F050.md) (function, `0x0025F050`)
- `0x00AF39A7` → [Feature_1345841464__private_IsEnabledDeviceUsageNoInline](../../text/4E/Feature_1345841464__private_IsEnabledDeviceUsageNoInline_function_004EF340.md) (function, `0x004EF340`)
- `0x00AF39CA` → [EtwpDereferenceStackEntry](../../text/3F/EtwpDereferenceStackEntry_function_003FC9D0.md) (function, `0x003FC9D0`)
- `0x00AF39EC` → [ExReleaseRundownProtectionCacheAwareEx](../../text/25/ExReleaseRundownProtectionCacheAwareEx_function_0025F050.md) (function, `0x0025F050`)
- `0x00AF3A2B` → [Feature_1345841464__private_IsEnabledDeviceUsageNoInline](../../text/4E/Feature_1345841464__private_IsEnabledDeviceUsageNoInline_function_004EF340.md) (function, `0x004EF340`)
- `0x00AF3A91` → [Feature_1345841464__private_IsEnabledDeviceUsageNoInline](../../text/4E/Feature_1345841464__private_IsEnabledDeviceUsageNoInline_function_004EF340.md) (function, `0x004EF340`)
- `0x00AF3ADC` → [EtwpReserveTraceBuffer](../../text/2F/EtwpReserveTraceBuffer_function_002FC8C0.md) (function, `0x002FC8C0`)
- `0x00AF3B02` → [EtwpDereferenceStackEntry](../../text/3F/EtwpDereferenceStackEntry_function_003FC9D0.md) (function, `0x003FC9D0`)
- `0x00AF3B07` → [Feature_1345841464__private_IsEnabledDeviceUsageNoInline](../../text/4E/Feature_1345841464__private_IsEnabledDeviceUsageNoInline_function_004EF340.md) (function, `0x004EF340`)
- `0x00AF3B2F` → [EtwpGetReserveTraceBufferStatus](../../text/44/EtwpGetReserveTraceBufferStatus_function_00446430.md) (function, `0x00446430`)
- `0x00AF3B54` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x00AF3B98` → [EtwpTraceLostEvent](../../text/3F/EtwpTraceLostEvent_function_003F0D58.md) (function, `0x003F0D58`)
- `0x00AF3BC7` → [ExReleaseRundownProtectionCacheAwareEx](../../text/25/ExReleaseRundownProtectionCacheAwareEx_function_0025F050.md) (function, `0x0025F050`)
- `0x00AF3BCC` → [Feature_1345841464__private_IsEnabledDeviceUsageNoInline](../../text/4E/Feature_1345841464__private_IsEnabledDeviceUsageNoInline_function_004EF340.md) (function, `0x004EF340`)
- `0x00AF3C40` → [Feature_1345841464__private_IsEnabledDeviceUsageNoInline](../../text/4E/Feature_1345841464__private_IsEnabledDeviceUsageNoInline_function_004EF340.md) (function, `0x004EF340`)
- `0x00AF3D3E` → [RtlCopyFromUser](../../text/4F/RtlCopyFromUser_function_004FDAE8.md) (function, `0x004FDAE8`)
- `0x00AF3D45` → [RtlCopyVolatileMemory](../../text/6B/RtlCopyVolatileMemory_function_006BC9D0.md) (function, `0x006BC9D0`)
- `0x00AF3E25` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00AF3E41` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00AF3EF1` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00AF3F5B` → [PsGetCurrentProcessSessionId](../../text/23/PsGetCurrentProcessSessionId_function_002303D0.md) (function, `0x002303D0`)
- `0x00AF3FDC` → [EtwpGetProcessStartKey](../../text/45/EtwpGetProcessStartKey_function_00459180.md) (function, `0x00459180`)
- `0x00AF405C` → [EtwpCreateEventKey](../../text/43/EtwpCreateEventKey_function_0043C6B0.md) (function, `0x0043C6B0`)
- `0x00AF40DB` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00AF41B7` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00AF4262` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00AF4271` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00AF4329` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00AF4430` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00AF44C8` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00AF45A8` → [EtwpSendTraceEvent](../../text/4B/EtwpSendTraceEvent_function_004B6E10.md) (function, `0x004B6E10`)
- `0x00AF45F6` → [EtwpInvokeEventCallback](../../text/4B/EtwpInvokeEventCallback_function_004B6F0C.md) (function, `0x004B6F0C`)
- `0x00AF466A` → [Feature_1345841464__private_IsEnabledDeviceUsageNoInline](../../text/4E/Feature_1345841464__private_IsEnabledDeviceUsageNoInline_function_004EF340.md) (function, `0x004EF340`)
- `0x00AF4686` → [EtwpDereferenceStackEntry](../../text/3F/EtwpDereferenceStackEntry_function_003FC9D0.md) (function, `0x003FC9D0`)
- `0x00AF46A0` → [ExReleaseRundownProtectionCacheAwareEx](../../text/25/ExReleaseRundownProtectionCacheAwareEx_function_0025F050.md) (function, `0x0025F050`)
- `0x00AF46B2` → [EtwpReleaseStackLookasideListEntry](../../text/41/EtwpReleaseStackLookasideListEntry_function_0041D770.md) (function, `0x0041D770`)
- `0x00AF46DF` → [EtwpReleaseTraceBuffer](../../text/3F/EtwpReleaseTraceBuffer_function_003F0D20.md) (function, `0x003F0D20`)
- `0x00AF46FC` → [ExReleaseRundownProtectionCacheAwareEx](../../text/25/ExReleaseRundownProtectionCacheAwareEx_function_0025F050.md) (function, `0x0025F050`)
- `0x00AF4769` → [EtwpFailLogging](../../text/3F/EtwpFailLogging_function_003F0A50.md) (function, `0x003F0A50`)
- `0x00AF4775` → [KiLeaveCriticalRegionUnsafe](../../text/25/KiLeaveCriticalRegionUnsafe_function_0025F010.md) (function, `0x0025F010`)
- `0x00AF4787` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00AF47A1` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x00AF47A7` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)

### Direct callers
- [NtTraceEvent](../../text/2F/NtTraceEvent_function_002FA6C0.md) at `0x002FA907`
- [NtTraceEvent](../../text/2F/NtTraceEvent_function_002FA6C0.md) at `0x002FA9AD`
- [NtTraceEvent](../../text/2F/NtTraceEvent_function_002FA6C0.md) at `0x002FAF12`
- [NtTraceEvent](../../text/2F/NtTraceEvent_function_002FA6C0.md) at `0x002FB154`
- [sub_006DF40E](../../text/6D/Unknown_function_006DF40E.md) at `0x006DF63D`
- [sub_006DF40E](../../text/6D/Unknown_function_006DF40E.md) at `0x006DF6F2`
- [sub_006DF40E](../../text/6D/Unknown_function_006DF40E.md) at `0x006DF79B`

### Static image references
- `0x00AF3005` → RVA `0x00E0A740` (`.data`; read)
- `0x00AF34CB` → RVA `0x00FC6AA8` (`ALMOSTRO`; read)
- `0x00AF3B46` → RVA `0x00013040` (`.rdata`; read)
- `0x00AF3B4D` → RVA `0x00EFF840` (`.data`; read)
- `0x00AF3D7B` → RVA `0x00038368` (`.rdata`; read)
- `0x00AF4583` → RVA `0x00F475DC` (`.data`; read)
- `0x00AF458C` → RVA `0x00E0AA1C` (`.data`; read)
- `0x00AF4595` → RVA `0x00F55CB3` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **64**
  - `0x00AF309B` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00AF30B1` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00AF30E5` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (`PAGE` → `.text`)
  - `0x00AF31AE` → [DecodeProviderTraits](../../text/3F/DecodeProviderTraits_function_003FD9D0.md) (`PAGE` → `.text`)
  - `0x00AF329E` → [EtwpLevelKeywordEnabled](../../text/2F/EtwpLevelKeywordEnabled_function_002FD110.md) (`PAGE` → `.text`)
  - `0x00AF3372` → [EtwpIsEventNameFilterEnabled](../../text/3F/EtwpIsEventNameFilterEnabled_function_003F1414.md) (`PAGE` → `.text`)
  - `0x00AF33A7` → [EtwpApplyEventNameFilter](../../text/3F/EtwpApplyEventNameFilter_function_003F10B8.md) (`PAGE` → `.text`)
  - `0x00AF33D2` → [ExAcquireRundownProtectionCacheAwareEx](../../text/41/ExAcquireRundownProtectionCacheAwareEx_function_00411F50.md) (`PAGE` → `.text`)
  - `0x00AF3434` → [ExReleaseRundownProtectionCacheAwareEx](../../text/25/ExReleaseRundownProtectionCacheAwareEx_function_0025F050.md) (`PAGE` → `.text`)
  - `0x00AF3439` → [Feature_1345841464__private_IsEnabledDeviceUsageNoInline](../../text/4E/Feature_1345841464__private_IsEnabledDeviceUsageNoInline_function_004EF340.md) (`PAGE` → `.text`)
  - `0x00AF35C3` → [EtwpApplyLevelKwFilter](../../text/46/EtwpApplyLevelKwFilter_function_00464740.md) (`PAGE` → `.text`)
  - `0x00AF3620` → [EtwpApplyEventNameFilter](../../text/3F/EtwpApplyEventNameFilter_function_003F10B8.md) (`PAGE` → `.text`)
  - `0x00AF3635` → [EtwpGetStackLookasideListEntry](../../text/44/EtwpGetStackLookasideListEntry_function_004468F0.md) (`PAGE` → `.text`)
  - `0x00AF3672` → [EtwpGetStackExtendedHeaderItem](../../text/44/EtwpGetStackExtendedHeaderItem_function_00443D70.md) (`PAGE` → `.text`)
  - `0x00AF3682` → [EtwpReleaseStackLookasideListEntry](../../text/41/EtwpReleaseStackLookasideListEntry_function_0041D770.md) (`PAGE` → `.text`)
  - `0x00AF36BA` → [EtwpGetCrimsonStackKey](../../text/4D/EtwpGetCrimsonStackKey_function_004D68CC.md) (`PAGE` → `.text`)
  - `0x00AF3707` → [IoGetStackLimits](../../text/41/IoGetStackLimits_function_0041FD70.md) (`PAGE` → `.text`)
  - `0x00AF381B` → [Feature_1345841464__private_IsEnabledDeviceUsageNoInline](../../text/4E/Feature_1345841464__private_IsEnabledDeviceUsageNoInline_function_004EF340.md) (`PAGE` → `.text`)
  - `0x00AF383B` → [EtwpDereferenceStackEntry](../../text/3F/EtwpDereferenceStackEntry_function_003FC9D0.md) (`PAGE` → `.text`)
  - `0x00AF3855` → [ExReleaseRundownProtectionCacheAwareEx](../../text/25/ExReleaseRundownProtectionCacheAwareEx_function_0025F050.md) (`PAGE` → `.text`)
  - `0x00AF38CC` → [Feature_1345841464__private_IsEnabledDeviceUsageNoInline](../../text/4E/Feature_1345841464__private_IsEnabledDeviceUsageNoInline_function_004EF340.md) (`PAGE` → `.text`)
  - `0x00AF3914` → [Feature_1345841464__private_IsEnabledDeviceUsageNoInline](../../text/4E/Feature_1345841464__private_IsEnabledDeviceUsageNoInline_function_004EF340.md) (`PAGE` → `.text`)
  - `0x00AF3934` → [EtwpDereferenceStackEntry](../../text/3F/EtwpDereferenceStackEntry_function_003FC9D0.md) (`PAGE` → `.text`)
  - `0x00AF394E` → [ExReleaseRundownProtectionCacheAwareEx](../../text/25/ExReleaseRundownProtectionCacheAwareEx_function_0025F050.md) (`PAGE` → `.text`)
  - `0x00AF39A7` → [Feature_1345841464__private_IsEnabledDeviceUsageNoInline](../../text/4E/Feature_1345841464__private_IsEnabledDeviceUsageNoInline_function_004EF340.md) (`PAGE` → `.text`)
  - `0x00AF39CA` → [EtwpDereferenceStackEntry](../../text/3F/EtwpDereferenceStackEntry_function_003FC9D0.md) (`PAGE` → `.text`)
  - `0x00AF39EC` → [ExReleaseRundownProtectionCacheAwareEx](../../text/25/ExReleaseRundownProtectionCacheAwareEx_function_0025F050.md) (`PAGE` → `.text`)
  - `0x00AF3A2B` → [Feature_1345841464__private_IsEnabledDeviceUsageNoInline](../../text/4E/Feature_1345841464__private_IsEnabledDeviceUsageNoInline_function_004EF340.md) (`PAGE` → `.text`)
  - `0x00AF3A91` → [Feature_1345841464__private_IsEnabledDeviceUsageNoInline](../../text/4E/Feature_1345841464__private_IsEnabledDeviceUsageNoInline_function_004EF340.md) (`PAGE` → `.text`)
  - `0x00AF3ADC` → [EtwpReserveTraceBuffer](../../text/2F/EtwpReserveTraceBuffer_function_002FC8C0.md) (`PAGE` → `.text`)
  - `0x00AF3B02` → [EtwpDereferenceStackEntry](../../text/3F/EtwpDereferenceStackEntry_function_003FC9D0.md) (`PAGE` → `.text`)
  - `0x00AF3B07` → [Feature_1345841464__private_IsEnabledDeviceUsageNoInline](../../text/4E/Feature_1345841464__private_IsEnabledDeviceUsageNoInline_function_004EF340.md) (`PAGE` → `.text`)
  - `0x00AF3B2F` → [EtwpGetReserveTraceBufferStatus](../../text/44/EtwpGetReserveTraceBufferStatus_function_00446430.md) (`PAGE` → `.text`)
  - `0x00AF3B54` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (`PAGE` → `.text`)
  - `0x00AF3B98` → [EtwpTraceLostEvent](../../text/3F/EtwpTraceLostEvent_function_003F0D58.md) (`PAGE` → `.text`)
  - `0x00AF3BC7` → [ExReleaseRundownProtectionCacheAwareEx](../../text/25/ExReleaseRundownProtectionCacheAwareEx_function_0025F050.md) (`PAGE` → `.text`)
  - `0x00AF3BCC` → [Feature_1345841464__private_IsEnabledDeviceUsageNoInline](../../text/4E/Feature_1345841464__private_IsEnabledDeviceUsageNoInline_function_004EF340.md) (`PAGE` → `.text`)
  - `0x00AF3C40` → [Feature_1345841464__private_IsEnabledDeviceUsageNoInline](../../text/4E/Feature_1345841464__private_IsEnabledDeviceUsageNoInline_function_004EF340.md) (`PAGE` → `.text`)
  - `0x00AF3D3E` → [RtlCopyFromUser](../../text/4F/RtlCopyFromUser_function_004FDAE8.md) (`PAGE` → `.text`)
  - `0x00AF3D45` → [RtlCopyVolatileMemory](../../text/6B/RtlCopyVolatileMemory_function_006BC9D0.md) (`PAGE` → `.text`)
  - `0x00AF3E25` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00AF3E41` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00AF3EF1` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00AF3F5B` → [PsGetCurrentProcessSessionId](../../text/23/PsGetCurrentProcessSessionId_function_002303D0.md) (`PAGE` → `.text`)
  - `0x00AF3FDC` → [EtwpGetProcessStartKey](../../text/45/EtwpGetProcessStartKey_function_00459180.md) (`PAGE` → `.text`)
  - `0x00AF405C` → [EtwpCreateEventKey](../../text/43/EtwpCreateEventKey_function_0043C6B0.md) (`PAGE` → `.text`)
  - `0x00AF40DB` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00AF41B7` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00AF4262` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00AF4271` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00AF4329` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00AF4430` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00AF44C8` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00AF45A8` → [EtwpSendTraceEvent](../../text/4B/EtwpSendTraceEvent_function_004B6E10.md) (`PAGE` → `.text`)
  - `0x00AF45F6` → [EtwpInvokeEventCallback](../../text/4B/EtwpInvokeEventCallback_function_004B6F0C.md) (`PAGE` → `.text`)
  - `0x00AF466A` → [Feature_1345841464__private_IsEnabledDeviceUsageNoInline](../../text/4E/Feature_1345841464__private_IsEnabledDeviceUsageNoInline_function_004EF340.md) (`PAGE` → `.text`)
  - `0x00AF4686` → [EtwpDereferenceStackEntry](../../text/3F/EtwpDereferenceStackEntry_function_003FC9D0.md) (`PAGE` → `.text`)
  - `0x00AF46A0` → [ExReleaseRundownProtectionCacheAwareEx](../../text/25/ExReleaseRundownProtectionCacheAwareEx_function_0025F050.md) (`PAGE` → `.text`)
  - `0x00AF46B2` → [EtwpReleaseStackLookasideListEntry](../../text/41/EtwpReleaseStackLookasideListEntry_function_0041D770.md) (`PAGE` → `.text`)
  - `0x00AF46DF` → [EtwpReleaseTraceBuffer](../../text/3F/EtwpReleaseTraceBuffer_function_003F0D20.md) (`PAGE` → `.text`)
  - `0x00AF46FC` → [ExReleaseRundownProtectionCacheAwareEx](../../text/25/ExReleaseRundownProtectionCacheAwareEx_function_0025F050.md) (`PAGE` → `.text`)
  - `0x00AF4769` → [EtwpFailLogging](../../text/3F/EtwpFailLogging_function_003F0A50.md) (`PAGE` → `.text`)
  - `0x00AF4775` → [KiLeaveCriticalRegionUnsafe](../../text/25/KiLeaveCriticalRegionUnsafe_function_0025F010.md) (`PAGE` → `.text`)
  - `0x00AF4787` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AF2FEC  40 55                           push rbp
00AF2FEE  53                              push rbx
00AF2FEF  56                              push rsi
00AF2FF0  57                              push rdi
00AF2FF1  41 54                           push r12
00AF2FF3  41 55                           push r13
00AF2FF5  41 56                           push r14
00AF2FF7  41 57                           push r15
00AF2FF9  48 81 EC 38 05 00 00            sub rsp, 0x538
00AF3000  48 8D 6C 24 60                  lea rbp, [rsp + 0x60]
00AF3005  48 8B 05 34 77 31 00            mov rax, qword ptr [rip + 0x317734]
00AF300C  48 33 C5                        xor rax, rbp
00AF300F  48 89 85 C0 04 00 00            mov qword ptr [rbp + 0x4c0], rax
00AF3016  49 8B D9                        mov rbx, r9
00AF3019  66 44 89 45 54                  mov word ptr [rbp + 0x54], r8w
00AF301E  4C 8B E9                        mov r13, rcx
00AF3021  48 89 8D B0 00 00 00            mov qword ptr [rbp + 0xb0], rcx
00AF3028  48 8B 8D 80 05 00 00            mov rcx, qword ptr [rbp + 0x580]
00AF302F  48 89 4D 68                     mov qword ptr [rbp + 0x68], rcx
00AF3033  4C 89 AD 38 01 00 00            mov qword ptr [rbp + 0x138], r13
00AF303A  66 89 55 08                     mov word ptr [rbp + 8], dx
00AF303E  48 8B 85 48 05 00 00            mov rax, qword ptr [rbp + 0x548]
00AF3045  48 89 85 88 00 00 00            mov qword ptr [rbp + 0x88], rax
00AF304C  4C 8B A5 70 05 00 00            mov r12, qword ptr [rbp + 0x570]
00AF3053  4C 89 65 28                     mov qword ptr [rbp + 0x28], r12
00AF3057  4C 89 A5 40 01 00 00            mov qword ptr [rbp + 0x140], r12
00AF305E  48 8B 85 78 05 00 00            mov rax, qword ptr [rbp + 0x578]
00AF3065  48 89 45 70                     mov qword ptr [rbp + 0x70], rax
00AF3069  48 8B 85 90 05 00 00            mov rax, qword ptr [rbp + 0x590]
00AF3070  48 89 85 28 01 00 00            mov qword ptr [rbp + 0x128], rax
00AF3077  48 8B 8D 98 05 00 00            mov rcx, qword ptr [rbp + 0x598]
00AF307E  48 89 8D 20 01 00 00            mov qword ptr [rbp + 0x120], rcx
00AF3085  45 33 F6                        xor r14d, r14d
00AF3088  44 89 75 1C                     mov dword ptr [rbp + 0x1c], r14d
00AF308C  33 D2                           xor edx, edx
00AF308E  41 B8 08 03 00 00               mov r8d, 0x308
00AF3094  48 8D 8D 60 01 00 00            lea rcx, [rbp + 0x160]
00AF309B  E8 A0 3B BD FF                  call 0x1406c6c40
00AF30A0  44 89 75 38                     mov dword ptr [rbp + 0x38], r14d
00AF30A4  33 D2                           xor edx, edx
00AF30A6  45 8D 46 50                     lea r8d, [r14 + 0x50]
00AF30AA  48 8D 8D 70 04 00 00            lea rcx, [rbp + 0x470]
00AF30B1  E8 8A 3B BD FF                  call 0x1406c6c40
00AF30B6  4C 89 B5 A0 00 00 00            mov qword ptr [rbp + 0xa0], r14
00AF30BD  4C 89 B5 00 01 00 00            mov qword ptr [rbp + 0x100], r14
00AF30C4  4C 89 B5 E0 00 00 00            mov qword ptr [rbp + 0xe0], r14
00AF30CB  66 44 89 75 48                  mov word ptr [rbp + 0x48], r14w
00AF30D0  4C 89 B5 18 01 00 00            mov qword ptr [rbp + 0x118], r14
00AF30D7  4C 89 B5 98 00 00 00            mov qword ptr [rbp + 0x98], r14
00AF30DE  4C 89 B5 D8 00 00 00            mov qword ptr [rbp + 0xd8], r14
00AF30E5  E8 06 B1 80 FF                  call 0x1402fe1f0
00AF30EA  48 8B 88 40 03 00 00            mov rcx, qword ptr [rax + 0x340]
00AF30F1  48 89 8D F0 00 00 00            mov qword ptr [rbp + 0xf0], rcx
00AF30F8  0F B7 85 88 05 00 00            movzx eax, word ptr [rbp + 0x588]
00AF30FF  B9 00 01 00 00                  mov ecx, 0x100
00AF3104  66 23 C1                        and ax, cx
00AF3107  66 89 45 4C                     mov word ptr [rbp + 0x4c], ax
00AF310B  0F B7 95 88 05 00 00            movzx edx, word ptr [rbp + 0x588]
00AF3112  66 C1 EA 09                     shr dx, 9
00AF3116  41 8D 76 01                     lea esi, [r14 + 1]
00AF311A  40 22 D6                        and dl, sil
00AF311D  41 8A CE                        mov cl, r14b
00AF3120  89 4D 18                        mov dword ptr [rbp + 0x18], ecx
00AF3123  44 8B FE                        mov r15d, esi
00AF3126  4C 89 75 60                     mov qword ptr [rbp + 0x60], r14
00AF312A  44 89 75 24                     mov dword ptr [rbp + 0x24], r14d
00AF312E  8B BD 68 05 00 00               mov edi, dword ptr [rbp + 0x568]
00AF3134  4D 85 E4                        test r12, r12
00AF3137  75 09                           jne 0x140af3142
00AF3139  85 FF                           test edi, edi
00AF313B  75 11                           jne 0x140af314e
00AF313D  4D 85 E4                        test r12, r12
00AF3140  74 04                           je 0x140af3146
00AF3142  85 FF                           test edi, edi
00AF3144  74 08                           je 0x140af314e
00AF3146  81 FF 80 00 00 00               cmp edi, 0x80
00AF314C  76 0A                           jbe 0x140af3158
00AF314E  B8 0D 00 00 C0                  mov eax, 0xc000000d
00AF3153  E9 25 16 00 00                  jmp 0x140af477d
00AF3158  4C 8B 5D 68                     mov r11, qword ptr [rbp + 0x68]
00AF315C  4D 85 DB                        test r11, r11
00AF315F  4D 0F 44 DD                     cmove r11, r13
00AF3163  4C 89 5D 68                     mov qword ptr [rbp + 0x68], r11
00AF3167  44 88 75 00                     mov byte ptr [rbp], r14b
00AF316B  4D 8B AD 88 02 00 00            mov r13, qword ptr [r13 + 0x288]
00AF3172  4C 89 6D 30                     mov qword ptr [rbp + 0x30], r13
00AF3176  4C 89 AD F8 00 00 00            mov qword ptr [rbp + 0xf8], r13
00AF317D  48 8B 85 20 01 00 00            mov rax, qword ptr [rbp + 0x120]
00AF3184  48 85 C0                        test rax, rax
00AF3187  74 13                           je 0x140af319c
00AF3189  48 8B 00                        mov rax, qword ptr [rax]
00AF318C  48 85 C0                        test rax, rax
00AF318F  74 0B                           je 0x140af319c
00AF3191  48 89 85 D8 00 00 00            mov qword ptr [rbp + 0xd8], rax
00AF3198  C6 45 00 10                     mov byte ptr [rbp], 0x10
00AF319C  4C 8D 8D 18 01 00 00            lea r9, [rbp + 0x118]
00AF31A3  4C 8D 45 48                     lea r8, [rbp + 0x48]
00AF31A7  48 8B 8D 28 01 00 00            mov rcx, qword ptr [rbp + 0x128]
00AF31AE  E8 1D A8 90 FF                  call 0x1403fd9d0
00AF31B3  65 4C 8B 04 25 88 01 00 00      mov r8, qword ptr gs:[0x188]
00AF31BC  4C 89 85 08 01 00 00            mov qword ptr [rbp + 0x108], r8
00AF31C3  66 41 FF 88 E4 01 00 00         dec word ptr [r8 + 0x1e4]
00AF31CB  90                              nop
00AF31CC  66 F7 D3                        not bx
00AF31CF  66 21 5D 08                     and word ptr [rbp + 8], bx
00AF31D3  4C 8B 45 70                     mov r8, qword ptr [rbp + 0x70]
00AF31D7  EB 0C                           jmp 0x140af31e5
00AF31D9  4C 8B 6D 30                     mov r13, qword ptr [rbp + 0x30]
00AF31DD  EB 0D                           jmp 0x140af31ec
00AF31DF  8B BD 68 05 00 00               mov edi, dword ptr [rbp + 0x568]
00AF31E5  48 8B 9D 60 05 00 00            mov rbx, qword ptr [rbp + 0x560]
00AF31EC  0F B7 4D 08                     movzx ecx, word ptr [rbp + 8]
00AF31F0  0F BC D1                        bsf edx, ecx
00AF31F3  89 55 38                        mov dword ptr [rbp + 0x38], edx
00AF31F6  0F 84 66 14 00 00               je 0x140af4662
00AF31FC  0F 57 C0                        xorps xmm0, xmm0
00AF31FF  33 C0                           xor eax, eax
00AF3201  0F 11 85 48 01 00 00            movups xmmword ptr [rbp + 0x148], xmm0
00AF3208  48 89 85 58 01 00 00            mov qword ptr [rbp + 0x158], rax
00AF320F  4C 89 B5 A8 00 00 00            mov qword ptr [rbp + 0xa8], r14
00AF3216  C7 45 10 50 00 00 00            mov dword ptr [rbp + 0x10], 0x50
00AF321D  44 89 75 50                     mov dword ptr [rbp + 0x50], r14d
00AF3221  44 89 75 3C                     mov dword ptr [rbp + 0x3c], r14d
00AF3225  4C 89 B5 C8 00 00 00            mov qword ptr [rbp + 0xc8], r14
00AF322C  4C 89 B5 30 01 00 00            mov qword ptr [rbp + 0x130], r14
00AF3233  45 8A D6                        mov r10b, r14b
00AF3236  44 89 55 18                     mov dword ptr [rbp + 0x18], r10d
00AF323A  44 88 75 14                     mov byte ptr [rbp + 0x14], r14b
00AF323E  4C 8B FE                        mov r15, rsi
00AF3241  48 89 75 40                     mov qword ptr [rbp + 0x40], rsi
00AF3245  48 89 B5 90 00 00 00            mov qword ptr [rbp + 0x90], rsi
00AF324C  4C 89 75 60                     mov qword ptr [rbp + 0x60], r14
00AF3250  66 2B CE                        sub cx, si
00AF3253  66 21 4D 08                     and word ptr [rbp + 8], cx
00AF3257  44 8B CA                        mov r9d, edx
00AF325A  4C 8D 6A 04                     lea r13, [rdx + 4]
00AF325E  49 C1 E5 05                     shl r13, 5
00AF3262  4D 03 EB                        add r13, r11
00AF3265  4D 85 C0                        test r8, r8
00AF3268  74 28                           je 0x140af3292
00AF326A  41 0F B7 45 06                  movzx eax, word ptr [r13 + 6]
00AF326F  8B C8                           mov ecx, eax
00AF3271  C1 E9 05                        shr ecx, 5
00AF3274  25 1F 00 00 80                  and eax, 0x8000001f
00AF3279  7D 07                           jge 0x140af3282
00AF327B  2B C6                           sub eax, esi
00AF327D  83 C8 E0                        or eax, 0xffffffe0
00AF3280  03 C6                           add eax, esi
00AF3282  0F B6 D0                        movzx edx, al
00AF3285  41 8B 0C 88                     mov ecx, dword ptr [r8 + rcx*4]
00AF3289  0F A3 D1                        bt ecx, edx
00AF328C  0F 82 47 FF FF FF               jb 0x140af31d9
00AF3292  4C 8B C3                        mov r8, rbx
00AF3295  8A 95 58 05 00 00               mov dl, byte ptr [rbp + 0x558]
00AF329B  49 8B CD                        mov rcx, r13
00AF329E  E8 6D 9E 80 FF                  call 0x1402fd110
00AF32A3  84 C0                           test al, al
00AF32A5  4C 8B 45 70                     mov r8, qword ptr [rbp + 0x70]
00AF32A9  0F 84 2A FF FF FF               je 0x140af31d9
00AF32AF  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AF32B8  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
00AF32BF  F6 85 40 05 00 00 02            test byte ptr [rbp + 0x540], 2
00AF32C6  75 09                           jne 0x140af32d1
00AF32C8  44 39 B1 F0 01 00 00            cmp dword ptr [rcx + 0x1f0], r14d
00AF32CF  7D 0E                           jge 0x140af32df
00AF32D1  41 F7 45 08 00 02 00 00         test dword ptr [r13 + 8], 0x200
00AF32D9  0F 85 FA FE FF FF               jne 0x140af31d9
00AF32DF  49 8B 8B 80 02 00 00            mov rcx, qword ptr [r11 + 0x280]
00AF32E6  48 85 C9                        test rcx, rcx
00AF32E9  74 27                           je 0x140af3312
00AF32EB  49 6B C1 68                     imul rax, r9, 0x68
00AF32EF  8B 0C 08                        mov ecx, dword ptr [rax + rcx]
00AF32F2  8B C1                           mov eax, ecx
00AF32F4  41 B8 00 02 00 80               mov r8d, 0x80000200
00AF32FA  41 23 C0                        and eax, r8d
00AF32FD  41 3B C0                        cmp eax, r8d
00AF3300  74 0B                           je 0x140af330d
00AF3302  B8 00 01 00 80                  mov eax, 0x80000100
00AF3307  23 C8                           and ecx, eax
00AF3309  3B C8                           cmp ecx, eax
00AF330B  75 05                           jne 0x140af3312
00AF330D  40 8A C6                        mov al, sil
00AF3310  EB 03                           jmp 0x140af3315
00AF3312  41 8A C6                        mov al, r14b
00AF3315  84 C0                           test al, al
00AF3317  74 38                           je 0x140af3351
00AF3319  4C 89 64 24 28                  mov qword ptr [rsp + 0x28], r12
00AF331E  89 7C 24 20                     mov dword ptr [rsp + 0x20], edi
00AF3322  4C 8B 8D 88 00 00 00            mov r9, qword ptr [rbp + 0x88]
00AF3329  44 0F B7 45 54                  movzx r8d, word ptr [rbp + 0x54]
00AF332E  44 8B 65 38                     mov r12d, dword ptr [rbp + 0x38]
00AF3332  41 8B D4                        mov edx, r12d
00AF3335  49 8B CB                        mov rcx, r11
00AF3338  E8 93 1D ED FF                  call 0x1409c50d0
00AF333D  84 C0                           test al, al
00AF333F  0F 84 18 01 00 00               je 0x140af345d
00AF3345  4C 8B 5D 68                     mov r11, qword ptr [rbp + 0x68]
00AF3349  8A 95 58 05 00 00               mov dl, byte ptr [rbp + 0x558]
00AF334F  EB 04                           jmp 0x140af3355
00AF3351  44 8B 65 38                     mov r12d, dword ptr [rbp + 0x38]
00AF3355  66 44 39 75 4C                  cmp word ptr [rbp + 0x4c], r14w
00AF335A  74 58                           je 0x140af33b4
00AF335C  44 88 74 24 28                  mov byte ptr [rsp + 0x28], r14b
00AF3361  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00AF3366  44 8A CA                        mov r9b, dl
00AF3369  45 33 C0                        xor r8d, r8d
00AF336C  41 8B D4                        mov edx, r12d
00AF336F  49 8B CB                        mov rcx, r11
00AF3372  E8 9D E0 8F FF                  call 0x1403f1414
00AF3377  84 C0                           test al, al
00AF3379  74 39                           je 0x140af33b4
00AF337B  44 88 74 24 40                  mov byte ptr [rsp + 0x40], r14b
00AF3380  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
00AF3385  8A 85 58 05 00 00               mov al, byte ptr [rbp + 0x558]
00AF338B  88 44 24 30                     mov byte ptr [rsp + 0x30], al
00AF338F  44 88 74 24 28                  mov byte ptr [rsp + 0x28], r14b
00AF3394  40 88 74 24 20                  mov byte ptr [rsp + 0x20], sil
00AF3399  4C 8B 4D 28                     mov r9, qword ptr [rbp + 0x28]
00AF339D  44 8B C7                        mov r8d, edi
00AF33A0  41 8B D4                        mov edx, r12d
00AF33A3  48 8B 4D 68                     mov rcx, qword ptr [rbp + 0x68]
00AF33A7  E8 0C DD 8F FF                  call 0x1403f10b8
00AF33AC  84 C0                           test al, al
00AF33AE  0F 84 A9 00 00 00               je 0x140af345d
00AF33B4  41 0F B7 45 06                  movzx eax, word ptr [r13 + 6]
00AF33B9  89 45 24                        mov dword ptr [rbp + 0x24], eax
00AF33BC  89 45 78                        mov dword ptr [rbp + 0x78], eax
00AF33BF  8B D8                           mov ebx, eax
00AF33C1  48 8B 7D 30                     mov rdi, qword ptr [rbp + 0x30]
00AF33C5  48 8B 8F C0 02 00 00            mov rcx, qword ptr [rdi + 0x2c0]
00AF33CC  8B D6                           mov edx, esi
00AF33CE  48 8B 0C C1                     mov rcx, qword ptr [rcx + rax*8]
00AF33D2  E8 79 EB 91 FF                  call 0x140411f50
00AF33D7  84 C0                           test al, al
00AF33D9  74 3B                           je 0x140af3416
00AF33DB  3B 5F 10                        cmp ebx, dword ptr [rdi + 0x10]
00AF33DE  73 1F                           jae 0x140af33ff
00AF33E0  0F AE E8                        lfence
00AF33E3  48 8B 87 C8 02 00 00            mov rax, qword ptr [rdi + 0x2c8]
00AF33EA  4C 8B 3C D8                     mov r15, qword ptr [rax + rbx*8]
00AF33EE  4C 89 7D 40                     mov qword ptr [rbp + 0x40], r15
00AF33F2  4C 89 BD 90 00 00 00            mov qword ptr [rbp + 0x90], r15
00AF33F9  44 8B 65 38                     mov r12d, dword ptr [rbp + 0x38]
00AF33FD  EB 0B                           jmp 0x140af340a
00AF33FF  48 89 75 40                     mov qword ptr [rbp + 0x40], rsi
00AF3403  48 89 B5 90 00 00 00            mov qword ptr [rbp + 0x90], rsi
00AF340A  40 8A FE                        mov dil, sil
00AF340D  89 7D 18                        mov dword ptr [rbp + 0x18], edi
00AF3410  40 88 75 14                     mov byte ptr [rbp + 0x14], sil
00AF3414  EB 03                           jmp 0x140af3419
00AF3416  8B 7D 18                        mov edi, dword ptr [rbp + 0x18]
00AF3419  44 84 FE                        test sil, r15b
00AF341C  74 6B                           je 0x140af3489
00AF341E  4C 8B 6D 30                     mov r13, qword ptr [rbp + 0x30]
00AF3422  40 84 FF                        test dil, dil
00AF3425  74 24                           je 0x140af344b
00AF3427  49 8B 8D C0 02 00 00            mov rcx, qword ptr [r13 + 0x2c0]
00AF342E  8B D6                           mov edx, esi
00AF3430  48 8B 0C D9                     mov rcx, qword ptr [rcx + rbx*8]
00AF3434  E8 17 BC 76 FF                  call 0x14025f050
00AF3439  E8 02 BF 9F FF                  call 0x1404ef340
00AF343E  40 0F B6 FF                     movzx edi, dil
00AF3442  85 C0                           test eax, eax
00AF3444  41 0F 45 FE                     cmovne edi, r14d
00AF3448  89 7D 18                        mov dword ptr [rbp + 0x18], edi
00AF344B  83 FB 03                        cmp ebx, 3
00AF344E  74 16                           je 0x140af3466
00AF3450  8B BD 68 05 00 00               mov edi, dword ptr [rbp + 0x568]
00AF3456  48 8B 9D 60 05 00 00            mov rbx, qword ptr [rbp + 0x560]
00AF345D  4C 8B 6D 30                     mov r13, qword ptr [rbp + 0x30]
00AF3461  E9 95 11 00 00                  jmp 0x140af45fb
00AF3466  41 8B 85 F4 10 00 00            mov eax, dword ptr [r13 + 0x10f4]
00AF346D  F7 D8                           neg eax
00AF346F  1B C9                           sbb ecx, ecx
00AF3471  81 E1 F6 02 00 00               and ecx, 0x2f6
00AF3477  81 C1 08 00 00 C0               add ecx, 0xc0000008
00AF347D  89 4D 1C                        mov dword ptr [rbp + 0x1c], ecx
00AF3480  4C 8B 65 28                     mov r12, qword ptr [rbp + 0x28]
00AF3484  E9 D9 11 00 00                  jmp 0x140af4662
00AF3489  41 8B FE                        mov edi, r14d
00AF348C  4C 39 B5 50 05 00 00            cmp qword ptr [rbp + 0x550], r14
00AF3493  74 10                           je 0x140af34a5
00AF3495  41 BF 68 00 00 00               mov r15d, 0x68
00AF349B  44 89 7D 10                     mov dword ptr [rbp + 0x10], r15d
00AF349F  41 8D 7F A8                     lea edi, [r15 - 0x58]
00AF34A3  EB 04                           jmp 0x140af34a9
00AF34A5  44 8B 7D 10                     mov r15d, dword ptr [rbp + 0x10]
00AF34A9  41 8B 4D 08                     mov ecx, dword ptr [r13 + 8]
00AF34AD  F7 C1 9F FF FF FF               test ecx, 0xffffff9f
00AF34B3  0F 84 A0 02 00 00               je 0x140af3759
00AF34B9  0F BA E1 0B                     bt ecx, 0xb
00AF34BD  73 2D                           jae 0x140af34ec
00AF34BF  48 8B 95 F0 00 00 00            mov rdx, qword ptr [rbp + 0xf0]
00AF34C6  48 85 D2                        test rdx, rdx
00AF34C9  74 21                           je 0x140af34ec
00AF34CB  48 3B 15 D6 35 4D 00            cmp rdx, qword ptr [rip + 0x4d35d6]
00AF34D2  74 18                           je 0x140af34ec
00AF34D4  0F BA EF 08                     bts edi, 8
00AF34D8  0F B7 82 90 11 00 00            movzx eax, word ptr [rdx + 0x1190]
00AF34DF  83 C0 0F                        add eax, 0xf
00AF34E2  83 E0 F8                        and eax, 0xfffffff8
00AF34E5  44 03 F8                        add r15d, eax
00AF34E8  44 89 7D 10                     mov dword ptr [rbp + 0x10], r15d
00AF34EC  40 84 CE                        test sil, cl
00AF34EF  74 2B                           je 0x140af351c
00AF34F1  F6 45 00 02                     test byte ptr [rbp], 2
00AF34F5  75 14                           jne 0x140af350b
00AF34F7  48 8D 8D 70 04 00 00            lea rcx, [rbp + 0x470]
00AF34FE  E8 7D 58 EB FF                  call 0x1409a8d80
00AF3503  80 4D 00 02                     or byte ptr [rbp], 2
00AF3507  41 8B 4D 08                     mov ecx, dword ptr [r13 + 8]
00AF350B  83 CF 02                        or edi, 2
00AF350E  0F B7 85 70 04 00 00            movzx eax, word ptr [rbp + 0x470]
00AF3515  44 03 F8                        add r15d, eax
00AF3518  44 89 7D 10                     mov dword ptr [rbp + 0x10], r15d
00AF351C  B8 10 00 00 00                  mov eax, 0x10
00AF3521  F6 C1 02                        test cl, 2
00AF3524  74 09                           je 0x140af352f
00AF3526  0B FE                           or edi, esi
00AF3528  44 03 F8                        add r15d, eax
00AF352B  44 89 7D 10                     mov dword ptr [rbp + 0x10], r15d
00AF352F  84 C9                           test cl, cl
00AF3531  79 0A                           jns 0x140af353d
00AF3533  83 CF 40                        or edi, 0x40
00AF3536  44 03 F8                        add r15d, eax
00AF3539  44 89 7D 10                     mov dword ptr [rbp + 0x10], r15d
00AF353D  0F BA E1 08                     bt ecx, 8
00AF3541  73 0B                           jae 0x140af354e
00AF3543  0F BA EF 07                     bts edi, 7
00AF3547  44 03 F8                        add r15d, eax
00AF354A  44 89 7D 10                     mov dword ptr [rbp + 0x10], r15d
00AF354E  BB 04 00 00 00                  mov ebx, 4
00AF3553  84 CB                           test bl, cl
00AF3555  0F 84 83 01 00 00               je 0x140af36de
00AF355B  48 8B 5D 68                     mov rbx, qword ptr [rbp + 0x68]
00AF355F  48 8B 93 80 02 00 00            mov rdx, qword ptr [rbx + 0x280]
00AF3566  48 85 D2                        test rdx, rdx
00AF3569  74 34                           je 0x140af359f
00AF356B  41 8B C4                        mov eax, r12d
00AF356E  48 6B C8 68                     imul rcx, rax, 0x68
00AF3572  8B 14 11                        mov edx, dword ptr [rcx + rdx]
00AF3575  8B C2                           mov eax, edx
00AF3577  B9 00 10 00 80                  mov ecx, 0x80001000
00AF357C  23 C1                           and eax, ecx
00AF357E  3B C1                           cmp eax, ecx
00AF3580  74 18                           je 0x140af359a
00AF3582  8B C2                           mov eax, edx
00AF3584  B9 00 20 00 80                  mov ecx, 0x80002000
00AF3589  23 C1                           and eax, ecx
00AF358B  3B C1                           cmp eax, ecx
00AF358D  74 0B                           je 0x140af359a
00AF358F  B8 00 40 00 80                  mov eax, 0x80004000
00AF3594  23 D0                           and edx, eax
00AF3596  3B D0                           cmp edx, eax
00AF3598  75 05                           jne 0x140af359f
00AF359A  40 8A C6                        mov al, sil
00AF359D  EB 03                           jmp 0x140af35a2
00AF359F  41 8A C6                        mov al, r14b
00AF35A2  84 C0                           test al, al
00AF35A4  0F 84 83 00 00 00               je 0x140af362d
00AF35AA  40 88 74 24 20                  mov byte ptr [rsp + 0x20], sil
00AF35AF  4C 8B 8D 60 05 00 00            mov r9, qword ptr [rbp + 0x560]
00AF35B6  44 8A 85 58 05 00 00            mov r8b, byte ptr [rbp + 0x558]
00AF35BD  41 8B D4                        mov edx, r12d
00AF35C0  48 8B CB                        mov rcx, rbx
00AF35C3  E8 78 11 97 FF                  call 0x140464740
00AF35C8  84 C0                           test al, al
00AF35CA  0F 84 09 01 00 00               je 0x140af36d9
00AF35D0  45 8B C4                        mov r8d, r12d
00AF35D3  48 8B D3                        mov rdx, rbx
00AF35D6  48 8B 8D 88 00 00 00            mov rcx, qword ptr [rbp + 0x88]
00AF35DD  E8 DA C1 F6 FF                  call 0x140a5f7bc
00AF35E2  84 C0                           test al, al
00AF35E4  0F 84 EF 00 00 00               je 0x140af36d9
00AF35EA  40 88 74 24 40                  mov byte ptr [rsp + 0x40], sil
00AF35EF  48 8B 85 60 05 00 00            mov rax, qword ptr [rbp + 0x560]
00AF35F6  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00AF35FB  8A 85 58 05 00 00               mov al, byte ptr [rbp + 0x558]
00AF3601  88 44 24 30                     mov byte ptr [rsp + 0x30], al
00AF3605  44 88 74 24 28                  mov byte ptr [rsp + 0x28], r14b
00AF360A  40 88 74 24 20                  mov byte ptr [rsp + 0x20], sil
00AF360F  4C 8B 4D 28                     mov r9, qword ptr [rbp + 0x28]
00AF3613  44 8B 85 68 05 00 00            mov r8d, dword ptr [rbp + 0x568]
00AF361A  41 8B D4                        mov edx, r12d
00AF361D  48 8B CB                        mov rcx, rbx
00AF3620  E8 93 DA 8F FF                  call 0x1403f10b8
00AF3625  84 C0                           test al, al
00AF3627  0F 84 AC 00 00 00               je 0x140af36d9
00AF362D  8A 5D 00                        mov bl, byte ptr [rbp]
00AF3630  40 84 DE                        test sil, bl
00AF3633  75 63                           jne 0x140af3698
00AF3635  E8 B6 32 95 FF                  call 0x1404468f0
00AF363A  48 89 85 00 01 00 00            mov qword ptr [rbp + 0x100], rax
00AF3641  48 85 C0                        test rax, rax
00AF3644  74 4E                           je 0x140af3694
00AF3646  80 CB 08                        or bl, 8
00AF3649  88 5D 00                        mov byte ptr [rbp], bl
00AF364C  48 8D 50 20                     lea rdx, [rax + 0x20]
00AF3650  48 89 95 A0 00 00 00            mov qword ptr [rbp + 0xa0], rdx
00AF3657  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
00AF365C  44 88 74 24 20                  mov byte ptr [rsp + 0x20], r14b
00AF3661  4C 8B C8                        mov r9, rax
00AF3664  45 33 C0                        xor r8d, r8d
00AF3667  48 8B 95 08 01 00 00            mov rdx, qword ptr [rbp + 0x108]
00AF366E  48 8B 4D 40                     mov rcx, qword ptr [rbp + 0x40]
00AF3672  E8 F9 06 95 FF                  call 0x140443d70
00AF3677  84 C0                           test al, al
00AF3679  75 19                           jne 0x140af3694
00AF367B  48 8B 8D 00 01 00 00            mov rcx, qword ptr [rbp + 0x100]
00AF3682  E8 E9 A0 92 FF                  call 0x14041d770
00AF3687  80 E3 F7                        and bl, 0xf7
00AF368A  88 5D 00                        mov byte ptr [rbp], bl
00AF368D  4C 89 B5 A0 00 00 00            mov qword ptr [rbp + 0xa0], r14
00AF3694  40 08 75 00                     or byte ptr [rbp], sil
00AF3698  48 8B 9D A0 00 00 00            mov rbx, qword ptr [rbp + 0xa0]
00AF369F  48 85 DB                        test rbx, rbx
00AF36A2  74 35                           je 0x140af36d9
00AF36A4  48 8B 4D 40                     mov rcx, qword ptr [rbp + 0x40]
00AF36A8  8B 81 34 03 00 00               mov eax, dword ptr [rcx + 0x334]
00AF36AE  40 84 C6                        test sil, al
00AF36B1  74 19                           je 0x140af36cc
00AF36B3  4C 8D 45 60                     lea r8, [rbp + 0x60]
00AF36B7  48 8B D3                        mov rdx, rbx
00AF36BA  E8 0D 32 9E FF                  call 0x1404d68cc
00AF36BF  84 C0                           test al, al
00AF36C1  74 09                           je 0x140af36cc
00AF36C3  83 CF 08                        or edi, 8
00AF36C6  41 83 C7 18                     add r15d, 0x18
00AF36CA  EB 09                           jmp 0x140af36d5
00AF36CC  83 CF 04                        or edi, 4
00AF36CF  0F B7 03                        movzx eax, word ptr [rbx]
00AF36D2  44 03 F8                        add r15d, eax
00AF36D5  44 89 7D 10                     mov dword ptr [rbp + 0x10], r15d
00AF36D9  BB 04 00 00 00                  mov ebx, 4
00AF36DE  41 8B 45 08                     mov eax, dword ptr [r13 + 8]
00AF36E2  A8 08                           test al, 8
00AF36E4  74 73                           je 0x140af3759
00AF36E6  84 5D 00                        test byte ptr [rbp], bl
00AF36E9  75 55                           jne 0x140af3740
00AF36EB  4C 89 B5 10 01 00 00            mov qword ptr [rbp + 0x110], r14
00AF36F2  4C 89 B5 B8 00 00 00            mov qword ptr [rbp + 0xb8], r14
00AF36F9  48 8D 95 10 01 00 00            lea rdx, [rbp + 0x110]
00AF3700  48 8D 8D B8 00 00 00            lea rcx, [rbp + 0xb8]
00AF3707  E8 64 C6 92 FF                  call 0x14041fd70
00AF370C  48 8D 85 10 01 00 00            lea rax, [rbp + 0x110]
00AF3713  48 2B 85 B8 00 00 00            sub rax, qword ptr [rbp + 0xb8]
00AF371A  B9 E0 01 00 00                  mov ecx, 0x1e0
00AF371F  48 3B C1                        cmp rax, rcx
00AF3722  76 19                           jbe 0x140af373d
00AF3724  8B 04 24                        mov eax, dword ptr [rsp]
00AF3727  48 2B E1                        sub rsp, rcx
00AF372A  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
00AF372F  48 89 8D E0 00 00 00            mov qword ptr [rbp + 0xe0], rcx
00AF3736  8B 01                           mov eax, dword ptr [rcx]
00AF3738  E8 A3 07 FD FF                  call 0x140ac3ee0
00AF373D  08 5D 00                        or byte ptr [rbp], bl
00AF3740  48 8B 85 E0 00 00 00            mov rax, qword ptr [rbp + 0xe0]
00AF3747  48 85 C0                        test rax, rax
00AF374A  74 0D                           je 0x140af3759
00AF374C  83 CF 20                        or edi, 0x20
00AF374F  0F B7 00                        movzx eax, word ptr [rax]
00AF3752  44 03 F8                        add r15d, eax
00AF3755  44 89 7D 10                     mov dword ptr [rbp + 0x10], r15d
00AF3759  8B 85 60 04 00 00               mov eax, dword ptr [rbp + 0x460]
00AF375F  48 8D 0C 40                     lea rcx, [rax + rax*2]
00AF3763  48 C1 E1 04                     shl rcx, 4
00AF3767  48 89 8D 80 00 00 00            mov qword ptr [rbp + 0x80], rcx
00AF376E  8B 95 68 05 00 00               mov edx, dword ptr [rbp + 0x568]
00AF3774  85 D2                           test edx, edx
00AF3776  0F 84 A9 02 00 00               je 0x140af3a25
00AF377C  44 89 B5 D0 00 00 00            mov dword ptr [rbp + 0xd0], r14d
00AF3783  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AF378C  8A 88 32 02 00 00               mov cl, byte ptr [rax + 0x232]
00AF3792  88 4D 15                        mov byte ptr [rbp + 0x15], cl
00AF3795  4C 8B 45 28                     mov r8, qword ptr [rbp + 0x28]
00AF3799  41 B9 03 00 00 00               mov r9d, 3
00AF379F  84 C9                           test cl, cl
00AF37A1  74 2E                           je 0x140af37d1
00AF37A3  8B C2                           mov eax, edx
00AF37A5  48 C1 E0 04                     shl rax, 4
00AF37A9  48 85 C0                        test rax, rax
00AF37AC  74 23                           je 0x140af37d1
00AF37AE  45 84 C1                        test r9b, r8b
00AF37B1  0F 85 EA 0F 00 00               jne 0x140af47a1
00AF37B7  49 8D 0C 00                     lea rcx, [r8 + rax]
00AF37BB  48 B8 00 00 FF FF FF 7F 00 00   movabs rax, 0x7fffffff0000
00AF37C5  48 3B C8                        cmp rcx, rax
00AF37C8  77 05                           ja 0x140af37cf
00AF37CA  49 3B C8                        cmp rcx, r8
00AF37CD  73 02                           jae 0x140af37d1
00AF37CF  8A 00                           mov al, byte ptr [rax]
00AF37D1  45 8B E6                        mov r12d, r14d
00AF37D4  44 89 B5 D0 00 00 00            mov dword ptr [rbp + 0xd0], r14d
00AF37DB  44 8B 7D 10                     mov r15d, dword ptr [rbp + 0x10]
00AF37DF  44 3B E2                        cmp r12d, edx
00AF37E2  0F 83 A5 01 00 00               jae 0x140af398d
00AF37E8  45 8B EF                        mov r13d, r15d
00AF37EB  41 8B D4                        mov edx, r12d
00AF37EE  48 C1 E2 04                     shl rdx, 4
00AF37F2  49 03 D0                        add rdx, r8
00AF37F5  8B 5A 08                        mov ebx, dword ptr [rdx + 8]
00AF37F8  89 9D E8 00 00 00               mov dword ptr [rbp + 0xe8], ebx
00AF37FE  81 FB FF FF 00 00               cmp ebx, 0xffff
00AF3804  76 6F                           jbe 0x140af3875
00AF3806  C7 45 1C 05 00 00 80            mov dword ptr [rbp + 0x1c], 0x80000005
00AF380D  0F B7 4D 08                     movzx ecx, word ptr [rbp + 8]
00AF3811  8B 45 38                        mov eax, dword ptr [rbp + 0x38]
00AF3814  0F AB C1                        bts ecx, eax
00AF3817  66 89 4D 08                     mov word ptr [rbp + 8], cx
00AF381B  E8 20 BB 9F FF                  call 0x1404ef340
00AF3820  85 C0                           test eax, eax
00AF3822  75 38                           jne 0x140af385c
00AF3824  48 8B 5D 60                     mov rbx, qword ptr [rbp + 0x60]
00AF3828  48 85 DB                        test rbx, rbx
00AF382B  74 13                           je 0x140af3840
00AF382D  48 8B 45 40                     mov rax, qword ptr [rbp + 0x40]
00AF3831  48 8B 90 20 04 00 00            mov rdx, qword ptr [rax + 0x420]
00AF3838  48 8B CB                        mov rcx, rbx
00AF383B  E8 90 91 90 FF                  call 0x1403fc9d0
00AF3840  4C 8B 6D 30                     mov r13, qword ptr [rbp + 0x30]
00AF3844  49 8B 8D C0 02 00 00            mov rcx, qword ptr [r13 + 0x2c0]
00AF384B  8B D6                           mov edx, esi
00AF384D  44 8B 45 24                     mov r8d, dword ptr [rbp + 0x24]
00AF3851  4A 8B 0C C1                     mov rcx, qword ptr [rcx + r8*8]
00AF3855  E8 F6 B7 76 FF                  call 0x14025f050
00AF385A  EB 04                           jmp 0x140af3860
00AF385C  4C 8B 6D 30                     mov r13, qword ptr [rbp + 0x30]
00AF3860  BF 01 00 00 00                  mov edi, 1
00AF3865  4C 8B 7D 40                     mov r15, qword ptr [rbp + 0x40]
00AF3869  4C 8B 65 28                     mov r12, qword ptr [rbp + 0x28]
00AF386D  8B 75 18                        mov esi, dword ptr [rbp + 0x18]
00AF3870  E9 F5 0D 00 00                  jmp 0x140af466a
00AF3875  66 44 39 75 4C                  cmp word ptr [rbp + 0x4c], r14w
00AF387A  75 05                           jne 0x140af3881
00AF387C  41 8A C6                        mov al, r14b
00AF387F  EB 09                           jmp 0x140af388a
00AF3881  8A 42 0C                        mov al, byte ptr [rdx + 0xc]
00AF3884  8B 9D E8 00 00 00               mov ebx, dword ptr [rbp + 0xe8]
00AF388A  0F B6 C8                        movzx ecx, al
00AF388D  84 C0                           test al, al
00AF388F  74 5E                           je 0x140af38ef
00AF3891  83 E9 01                        sub ecx, 1
00AF3894  74 36                           je 0x140af38cc
00AF3896  41 3B C9                        cmp ecx, r9d
00AF3899  75 4E                           jne 0x140af38e9
00AF389B  83 FB 10                        cmp ebx, 0x10
00AF389E  75 49                           jne 0x140af38e9
00AF38A0  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AF38A9  8A 88 32 02 00 00               mov cl, byte ptr [rax + 0x232]
00AF38AF  88 4D 15                        mov byte ptr [rbp + 0x15], cl
00AF38B2  84 C9                           test cl, cl
00AF38B4  74 0A                           je 0x140af38c0
00AF38B6  48 8B CA                        mov rcx, rdx
00AF38B9  E8 0E 25 C1 FF                  call 0x140705dcc
00AF38BE  EB 03                           jmp 0x140af38c3
00AF38C0  48 8B 02                        mov rax, qword ptr [rdx]
00AF38C3  48 89 85 98 00 00 00            mov qword ptr [rbp + 0x98], rax
00AF38CA  EB 1D                           jmp 0x140af38e9
00AF38CC  E8 6F BA 9F FF                  call 0x1404ef340
00AF38D1  89 85 B8 00 00 00               mov dword ptr [rbp + 0xb8], eax
00AF38D7  85 C0                           test eax, eax
00AF38D9  74 05                           je 0x140af38e0
00AF38DB  01 5D 50                        add dword ptr [rbp + 0x50], ebx
00AF38DE  EB 06                           jmp 0x140af38e6
00AF38E0  0F B7 C3                        movzx eax, bx
00AF38E3  01 45 50                        add dword ptr [rbp + 0x50], eax
00AF38E6  01 75 3C                        add dword ptr [rbp + 0x3c], esi
00AF38E9  44 8B 7D 10                     mov r15d, dword ptr [rbp + 0x10]
00AF38ED  EB 0B                           jmp 0x140af38fa
00AF38EF  44 8B 7D 10                     mov r15d, dword ptr [rbp + 0x10]
00AF38F3  44 03 FB                        add r15d, ebx
00AF38F6  44 89 7D 10                     mov dword ptr [rbp + 0x10], r15d
00AF38FA  45 3B FD                        cmp r15d, r13d
00AF38FD  73 6F                           jae 0x140af396e
00AF38FF  C7 45 1C 05 00 00 80            mov dword ptr [rbp + 0x1c], 0x80000005
00AF3906  0F B7 4D 08                     movzx ecx, word ptr [rbp + 8]
00AF390A  8B 45 38                        mov eax, dword ptr [rbp + 0x38]
00AF390D  0F AB C1                        bts ecx, eax
00AF3910  66 89 4D 08                     mov word ptr [rbp + 8], cx
00AF3914  E8 27 BA 9F FF                  call 0x1404ef340
00AF3919  85 C0                           test eax, eax
00AF391B  75 38                           jne 0x140af3955
00AF391D  48 8B 5D 60                     mov rbx, qword ptr [rbp + 0x60]
00AF3921  48 85 DB                        test rbx, rbx
00AF3924  74 13                           je 0x140af3939
00AF3926  48 8B 45 40                     mov rax, qword ptr [rbp + 0x40]
00AF392A  48 8B 90 20 04 00 00            mov rdx, qword ptr [rax + 0x420]
00AF3931  48 8B CB                        mov rcx, rbx
00AF3934  E8 97 90 90 FF                  call 0x1403fc9d0
00AF3939  4C 8B 6D 30                     mov r13, qword ptr [rbp + 0x30]
00AF393D  49 8B 8D C0 02 00 00            mov rcx, qword ptr [r13 + 0x2c0]
00AF3944  8B D6                           mov edx, esi
00AF3946  44 8B 45 24                     mov r8d, dword ptr [rbp + 0x24]
00AF394A  4A 8B 0C C1                     mov rcx, qword ptr [rcx + r8*8]
00AF394E  E8 FD B6 76 FF                  call 0x14025f050
00AF3953  EB 04                           jmp 0x140af3959
00AF3955  4C 8B 6D 30                     mov r13, qword ptr [rbp + 0x30]
00AF3959  BF 01 00 00 00                  mov edi, 1
00AF395E  4C 8B 7D 40                     mov r15, qword ptr [rbp + 0x40]
00AF3962  4C 8B 65 28                     mov r12, qword ptr [rbp + 0x28]
00AF3966  8B 75 18                        mov esi, dword ptr [rbp + 0x18]
00AF3969  E9 FC 0C 00 00                  jmp 0x140af466a
00AF396E  44 03 E6                        add r12d, esi
00AF3971  44 89 A5 D0 00 00 00            mov dword ptr [rbp + 0xd0], r12d
00AF3978  8B 95 68 05 00 00               mov edx, dword ptr [rbp + 0x568]
00AF397E  4C 8B 45 28                     mov r8, qword ptr [rbp + 0x28]
00AF3982  41 B9 03 00 00 00               mov r9d, 3
00AF3988  E9 52 FE FF FF                  jmp 0x140af37df
00AF398D  44 8B 65 38                     mov r12d, dword ptr [rbp + 0x38]
00AF3991  E9 8F 00 00 00                  jmp 0x140af3a25
00AF3996  89 45 1C                        mov dword ptr [rbp + 0x1c], eax
00AF3999  0F B7 4D 08                     movzx ecx, word ptr [rbp + 8]
00AF399D  8B 45 38                        mov eax, dword ptr [rbp + 0x38]
00AF39A0  0F AB C1                        bts ecx, eax
00AF39A3  66 89 4D 08                     mov word ptr [rbp + 8], cx
00AF39A7  E8 94 B9 9F FF                  call 0x1404ef340
00AF39AC  4C 8B BD 90 00 00 00            mov r15, qword ptr [rbp + 0x90]
00AF39B3  85 C0                           test eax, eax
00AF39B5  75 3C                           jne 0x140af39f3
00AF39B7  48 8B 5D 60                     mov rbx, qword ptr [rbp + 0x60]
00AF39BB  48 85 DB                        test rbx, rbx
00AF39BE  74 0F                           je 0x140af39cf
00AF39C0  49 8B 97 20 04 00 00            mov rdx, qword ptr [r15 + 0x420]
00AF39C7  48 8B CB                        mov rcx, rbx
00AF39CA  E8 01 90 90 FF                  call 0x1403fc9d0
00AF39CF  8B 5D 78                        mov ebx, dword ptr [rbp + 0x78]
00AF39D2  89 5D 24                        mov dword ptr [rbp + 0x24], ebx
00AF39D5  4C 8B AD F8 00 00 00            mov r13, qword ptr [rbp + 0xf8]
00AF39DC  49 8B 8D C0 02 00 00            mov rcx, qword ptr [r13 + 0x2c0]
00AF39E3  BA 01 00 00 00                  mov edx, 1
00AF39E8  48 8B 0C D9                     mov rcx, qword ptr [rcx + rbx*8]
00AF39EC  E8 5F B6 76 FF                  call 0x14025f050
00AF39F1  EB 0D                           jmp 0x140af3a00
00AF39F3  4C 8B AD F8 00 00 00            mov r13, qword ptr [rbp + 0xf8]
00AF39FA  8B 45 78                        mov eax, dword ptr [rbp + 0x78]
00AF39FD  89 45 24                        mov dword ptr [rbp + 0x24], eax
00AF3A00  45 33 F6                        xor r14d, r14d
00AF3A03  41 8D 7E 01                     lea edi, [r14 + 1]
00AF3A07  40 8A 75 14                     mov sil, byte ptr [rbp + 0x14]
00AF3A0B  48 8B 9D 38 01 00 00            mov rbx, qword ptr [rbp + 0x138]
00AF3A12  48 89 9D B0 00 00 00            mov qword ptr [rbp + 0xb0], rbx
00AF3A19  4C 8B A5 40 01 00 00            mov r12, qword ptr [rbp + 0x140]
00AF3A20  E9 45 0C 00 00                  jmp 0x140af466a
00AF3A25  44 39 75 3C                     cmp dword ptr [rbp + 0x3c], r14d
00AF3A29  74 57                           je 0x140af3a82
00AF3A2B  E8 10 B9 9F FF                  call 0x1404ef340
00AF3A30  41 BD F8 FF FF FF               mov r13d, 0xfffffff8
00AF3A36  85 C0                           test eax, eax
00AF3A38  8B 45 50                        mov eax, dword ptr [rbp + 0x50]
00AF3A3B  74 36                           je 0x140af3a73
00AF3A3D  83 C0 0F                        add eax, 0xf
00AF3A40  41 23 C5                        and eax, r13d
00AF3A43  3D FF FF 00 00                  cmp eax, 0xffff
00AF3A48  76 2F                           jbe 0x140af3a79
00AF3A4A  8B 45 1C                        mov eax, dword ptr [rbp + 0x1c]
00AF3A4D  85 C0                           test eax, eax
00AF3A4F  B9 95 00 00 C0                  mov ecx, 0xc0000095
00AF3A54  0F 49 C1                        cmovns eax, ecx
00AF3A57  89 45 1C                        mov dword ptr [rbp + 0x1c], eax
00AF3A5A  0F B7 45 08                     movzx eax, word ptr [rbp + 8]
00AF3A5E  44 0F AB E0                     bts eax, r12d
00AF3A62  66 89 45 08                     mov word ptr [rbp + 8], ax
00AF3A66  4C 8B 7D 40                     mov r15, qword ptr [rbp + 0x40]
00AF3A6A  4C 8B 6D 30                     mov r13, qword ptr [rbp + 0x30]
00AF3A6E  E9 0D FA FF FF                  jmp 0x140af3480
00AF3A73  83 C0 0F                        add eax, 0xf
00AF3A76  41 23 C5                        and eax, r13d
00AF3A79  44 03 F8                        add r15d, eax
00AF3A7C  44 89 7D 10                     mov dword ptr [rbp + 0x10], r15d
00AF3A80  EB 06                           jmp 0x140af3a88
00AF3A82  41 BD F8 FF FF FF               mov r13d, 0xfffffff8
00AF3A88  0F B7 5D 48                     movzx ebx, word ptr [rbp + 0x48]
00AF3A8C  66 85 DB                        test bx, bx
00AF3A8F  74 22                           je 0x140af3ab3
00AF3A91  E8 AA B8 9F FF                  call 0x1404ef340
00AF3A96  85 C0                           test eax, eax
00AF3A98  8D 43 0F                        lea eax, [rbx + 0xf]
00AF3A9B  74 0C                           je 0x140af3aa9
00AF3A9D  41 23 C5                        and eax, r13d
00AF3AA0  3D FF FF 00 00                  cmp eax, 0xffff
00AF3AA5  76 05                           jbe 0x140af3aac
00AF3AA7  EB A1                           jmp 0x140af3a4a
00AF3AA9  41 23 C5                        and eax, r13d
00AF3AAC  44 03 F8                        add r15d, eax
00AF3AAF  44 89 7D 10                     mov dword ptr [rbp + 0x10], r15d
00AF3AB3  4C 8B A5 80 00 00 00            mov r12, qword ptr [rbp + 0x80]
00AF3ABA  46 89 BC 25 88 01 00 00         mov dword ptr [rbp + r12 + 0x188], r15d
00AF3AC2  44 89 74 24 20                  mov dword ptr [rsp + 0x20], r14d
00AF3AC7  4C 8D 8D A8 00 00 00            lea r9, [rbp + 0xa8]
00AF3ACE  4C 8D 85 48 01 00 00            lea r8, [rbp + 0x148]
00AF3AD5  41 8B D7                        mov edx, r15d
00AF3AD8  48 8B 4D 40                     mov rcx, qword ptr [rbp + 0x40]
00AF3ADC  E8 DF 8D 80 FF                  call 0x1402fc8c0
00AF3AE1  4C 8B E8                        mov r13, rax
00AF3AE4  48 89 85 B8 00 00 00            mov qword ptr [rbp + 0xb8], rax
00AF3AEB  48 8B 5D 60                     mov rbx, qword ptr [rbp + 0x60]
00AF3AEF  48 85 DB                        test rbx, rbx
00AF3AF2  74 22                           je 0x140af3b16
00AF3AF4  48 8B 45 40                     mov rax, qword ptr [rbp + 0x40]
00AF3AF8  48 8B 90 20 04 00 00            mov rdx, qword ptr [rax + 0x420]
00AF3AFF  48 8B CB                        mov rcx, rbx
00AF3B02  E8 C9 8E 90 FF                  call 0x1403fc9d0
00AF3B07  E8 34 B8 9F FF                  call 0x1404ef340
00AF3B0C  85 C0                           test eax, eax
00AF3B0E  49 0F 45 DE                     cmovne rbx, r14
00AF3B12  48 89 5D 60                     mov qword ptr [rbp + 0x60], rbx
00AF3B16  4D 85 ED                        test r13, r13
00AF3B19  0F 85 E5 00 00 00               jne 0x140af3c04
00AF3B1F  41 8B FE                        mov edi, r14d
00AF3B22  4D 8B E6                        mov r12, r14
00AF3B25  41 8B D7                        mov edx, r15d
00AF3B28  4C 8B 7D 40                     mov r15, qword ptr [rbp + 0x40]
00AF3B2C  49 8B CF                        mov rcx, r15
00AF3B2F  E8 FC 28 95 FF                  call 0x140446430
00AF3B34  8B D8                           mov ebx, eax
00AF3B36  44 39 75 3C                     cmp dword ptr [rbp + 0x3c], r14d
00AF3B3A  76 0A                           jbe 0x140af3b46
00AF3B3C  8B BD 68 05 00 00               mov edi, dword ptr [rbp + 0x568]
00AF3B42  4C 8B 65 28                     mov r12, qword ptr [rbp + 0x28]
00AF3B46  48 8D 15 F3 F4 51 FF            lea rdx, [rip - 0xae0b0d]
00AF3B4D  48 8B 0D EC BC 40 00            mov rcx, qword ptr [rip + 0x40bcec]
00AF3B54  E8 F7 E8 89 FF                  call 0x140392450
00AF3B59  84 C0                           test al, al
00AF3B5B  74 40                           je 0x140af3b9d
00AF3B5D  4D 8D 87 88 00 00 00            lea r8, [r15 + 0x88]
00AF3B64  48 8B 95 88 00 00 00            mov rdx, qword ptr [rbp + 0x88]
00AF3B6B  48 83 C2 28                     add rdx, 0x28
00AF3B6F  48 8B 8D B0 00 00 00            mov rcx, qword ptr [rbp + 0xb0]
00AF3B76  48 83 C1 28                     add rcx, 0x28
00AF3B7A  40 88 74 24 40                  mov byte ptr [rsp + 0x40], sil
00AF3B7F  40 88 74 24 38                  mov byte ptr [rsp + 0x38], sil
00AF3B84  4C 89 64 24 30                  mov qword ptr [rsp + 0x30], r12
00AF3B89  89 7C 24 28                     mov dword ptr [rsp + 0x28], edi
00AF3B8D  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
00AF3B91  44 8B 8D 40 05 00 00            mov r9d, dword ptr [rbp + 0x540]
00AF3B98  E8 BB D1 8F FF                  call 0x1403f0d58
00AF3B9D  8B 4D 1C                        mov ecx, dword ptr [rbp + 0x1c]
00AF3BA0  85 C9                           test ecx, ecx
00AF3BA2  78 0E                           js 0x140af3bb2
00AF3BA4  41 F7 47 0C 00 00 00 08         test dword ptr [r15 + 0xc], 0x8000000
00AF3BAC  0F 44 CB                        cmove ecx, ebx
00AF3BAF  89 4D 1C                        mov dword ptr [rbp + 0x1c], ecx
00AF3BB2  4C 8B 6D 30                     mov r13, qword ptr [rbp + 0x30]
00AF3BB6  49 8B 8D C0 02 00 00            mov rcx, qword ptr [r13 + 0x2c0]
00AF3BBD  8B D6                           mov edx, esi
00AF3BBF  44 8B 45 24                     mov r8d, dword ptr [rbp + 0x24]
00AF3BC3  4A 8B 0C C1                     mov rcx, qword ptr [rcx + r8*8]
00AF3BC7  E8 84 B4 76 FF                  call 0x14025f050
00AF3BCC  E8 6F B7 9F FF                  call 0x1404ef340
00AF3BD1  8B 4D 18                        mov ecx, dword ptr [rbp + 0x18]
00AF3BD4  0F B6 C9                        movzx ecx, cl
00AF3BD7  85 C0                           test eax, eax
00AF3BD9  41 0F 45 CE                     cmovne ecx, r14d
00AF3BDD  89 4D 18                        mov dword ptr [rbp + 0x18], ecx
00AF3BE0  41 B9 95 00 00 C0               mov r9d, 0xc0000095
00AF3BE6  41 3B D9                        cmp ebx, r9d
00AF3BE9  4C 8B 65 28                     mov r12, qword ptr [rbp + 0x28]
00AF3BED  4C 8B 5D 68                     mov r11, qword ptr [rbp + 0x68]
00AF3BF1  4C 8B 45 70                     mov r8, qword ptr [rbp + 0x70]
00AF3BF5  0F 85 E4 F5 FF FF               jne 0x140af31df
00AF3BFB  44 89 4D 1C                     mov dword ptr [rbp + 0x1c], r9d
00AF3BFF  E9 7C F8 FF FF                  jmp 0x140af3480
00AF3C04  48 8B 45 40                     mov rax, qword ptr [rbp + 0x40]
00AF3C08  4A 89 84 25 60 01 00 00         mov qword ptr [rbp + r12 + 0x160], rax
00AF3C10  4E 89 AC 25 68 01 00 00         mov qword ptr [rbp + r12 + 0x168], r13
00AF3C18  0F 10 85 48 01 00 00            movups xmm0, xmmword ptr [rbp + 0x148]
00AF3C1F  42 0F 11 84 25 70 01 00 00      movups xmmword ptr [rbp + r12 + 0x170], xmm0
00AF3C28  F2 0F 10 85 58 01 00 00         movsd xmm0, qword ptr [rbp + 0x158]
00AF3C30  F2 42 0F 11 84 25 80 01 00 00   movsd qword ptr [rbp + r12 + 0x180], xmm0
00AF3C3A  01 B5 60 04 00 00               add dword ptr [rbp + 0x460], esi
00AF3C40  E8 FB B6 9F FF                  call 0x1404ef340
00AF3C45  8B 4D 18                        mov ecx, dword ptr [rbp + 0x18]
00AF3C48  0F B6 C9                        movzx ecx, cl
00AF3C4B  85 C0                           test eax, eax
00AF3C4D  41 0F 45 CE                     cmovne ecx, r14d
00AF3C51  89 4D 18                        mov dword ptr [rbp + 0x18], ecx
00AF3C54  88 4D 14                        mov byte ptr [rbp + 0x14], cl
00AF3C57  44 89 B5 C0 00 00 00            mov dword ptr [rbp + 0xc0], r14d
00AF3C5E  BB 50 00 00 00                  mov ebx, 0x50
00AF3C63  89 5D 20                        mov dword ptr [rbp + 0x20], ebx
00AF3C66  4D 8B E6                        mov r12, r14
00AF3C69  4C 89 75 58                     mov qword ptr [rbp + 0x58], r14
00AF3C6D  48 8B 85 88 00 00 00            mov rax, qword ptr [rbp + 0x88]
00AF3C74  0F 10 00                        movups xmm0, xmmword ptr [rax]
00AF3C77  41 0F 11 45 00                  movups xmmword ptr [r13], xmm0
00AF3C7C  0F 10 48 10                     movups xmm1, xmmword ptr [rax + 0x10]
00AF3C80  41 0F 11 4D 10                  movups xmmword ptr [r13 + 0x10], xmm1
00AF3C85  0F 10 40 20                     movups xmm0, xmmword ptr [rax + 0x20]
00AF3C89  41 0F 11 45 20                  movups xmmword ptr [r13 + 0x20], xmm0
00AF3C8E  0F 10 48 30                     movups xmm1, xmmword ptr [rax + 0x30]
00AF3C92  41 0F 11 4D 30                  movups xmmword ptr [r13 + 0x30], xmm1
00AF3C97  0F 10 40 40                     movups xmm0, xmmword ptr [rax + 0x40]
00AF3C9B  41 0F 11 45 40                  movups xmmword ptr [r13 + 0x40], xmm0
00AF3CA0  48 8B 85 18 01 00 00            mov rax, qword ptr [rbp + 0x118]
00AF3CA7  48 85 C0                        test rax, rax
00AF3CAA  75 1F                           jne 0x140af3ccb
00AF3CAC  4C 39 B5 98 00 00 00            cmp qword ptr [rbp + 0x98], r14
00AF3CB3  75 23                           jne 0x140af3cd8
00AF3CB5  48 8B 85 B0 00 00 00            mov rax, qword ptr [rbp + 0xb0]
00AF3CBC  0F 10 40 28                     movups xmm0, xmmword ptr [rax + 0x28]
00AF3CC0  F3 41 0F 7F 45 18               movdqu xmmword ptr [r13 + 0x18], xmm0
00AF3CC6  E9 AC 00 00 00                  jmp 0x140af3d77
00AF3CCB  4C 39 B5 98 00 00 00            cmp qword ptr [rbp + 0x98], r14
00AF3CD2  0F 84 87 00 00 00               je 0x140af3d5f
00AF3CD8  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AF3CE1  8A 88 32 02 00 00               mov cl, byte ptr [rax + 0x232]
00AF3CE7  88 4D 15                        mov byte ptr [rbp + 0x15], cl
00AF3CEA  84 C9                           test cl, cl
00AF3CEC  74 29                           je 0x140af3d17
00AF3CEE  48 8B 85 98 00 00 00            mov rax, qword ptr [rbp + 0x98]
00AF3CF5  A8 03                           test al, 3
00AF3CF7  0F 85 AA 0A 00 00               jne 0x140af47a7
00AF3CFD  48 8D 48 10                     lea rcx, [rax + 0x10]
00AF3D01  48 BA 00 00 FF FF FF 7F 00 00   movabs rdx, 0x7fffffff0000
00AF3D0B  48 3B CA                        cmp rcx, rdx
00AF3D0E  77 05                           ja 0x140af3d15
00AF3D10  48 3B C8                        cmp rcx, rax
00AF3D13  73 02                           jae 0x140af3d17
00AF3D15  8A 02                           mov al, byte ptr [rdx]
00AF3D17  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AF3D20  8A 88 32 02 00 00               mov cl, byte ptr [rax + 0x232]
00AF3D26  88 4D 15                        mov byte ptr [rbp + 0x15], cl
00AF3D29  41 B8 10 00 00 00               mov r8d, 0x10
00AF3D2F  48 8B 95 98 00 00 00            mov rdx, qword ptr [rbp + 0x98]
00AF3D36  84 C9                           test cl, cl
00AF3D38  49 8D 4D 18                     lea rcx, [r13 + 0x18]
00AF3D3C  74 07                           je 0x140af3d45
00AF3D3E  E8 A5 9D A0 FF                  call 0x1404fdae8
00AF3D43  EB 05                           jmp 0x140af3d4a
00AF3D45  E8 86 8C BC FF                  call 0x1406bc9d0
00AF3D4A  B8 80 00 00 00                  mov eax, 0x80
00AF3D4F  66 41 0B 45 04                  or ax, word ptr [r13 + 4]
00AF3D54  66 41 89 45 04                  mov word ptr [r13 + 4], ax
00AF3D59  44 8B 7D 10                     mov r15d, dword ptr [rbp + 0x10]
00AF3D5D  EB 18                           jmp 0x140af3d77
00AF3D5F  0F 10 00                        movups xmm0, xmmword ptr [rax]
00AF3D62  F3 41 0F 7F 45 18               movdqu xmmword ptr [r13 + 0x18], xmm0
00AF3D68  B8 80 00 00 00                  mov eax, 0x80
00AF3D6D  66 41 0B 45 04                  or ax, word ptr [r13 + 4]
00AF3D72  66 41 89 45 04                  mov word ptr [r13 + 4], ax
00AF3D77  0F B7 4D 54                     movzx ecx, word ptr [rbp + 0x54]
00AF3D7B  48 8D 15 E6 45 54 FF            lea rdx, [rip - 0xabba1a]
00AF3D82  41 8B C7                        mov eax, r15d
00AF3D85  0B 04 8A                        or eax, dword ptr [rdx + rcx*4]
00AF3D88  41 89 45 00                     mov dword ptr [r13], eax
00AF3D8C  B8 00 04 00 00                  mov eax, 0x400
00AF3D91  66 85 85 88 05 00 00            test word ptr [rbp + 0x588], ax
00AF3D98  74 05                           je 0x140af3d9f
00AF3D9A  66 41 09 45 04                  or word ptr [r13 + 4], ax
00AF3D9F  85 FF                           test edi, edi
00AF3DA1  0F 84 4C 04 00 00               je 0x140af41f3
00AF3DA7  0F BA E7 08                     bt edi, 8
00AF3DAB  0F 83 AE 00 00 00               jae 0x140af3e5f
00AF3DB1  4D 8D 65 50                     lea r12, [r13 + 0x50]
00AF3DB5  48 8B 8D F0 00 00 00            mov rcx, qword ptr [rbp + 0xf0]
00AF3DBC  0F B7 B1 90 11 00 00            movzx esi, word ptr [rcx + 0x1190]
00AF3DC3  66 83 C6 0F                     add si, 0xf
00AF3DC7  B8 F8 FF 00 00                  mov eax, 0xfff8
00AF3DCC  66 23 F0                        and si, ax
00AF3DCF  66 41 89 34 24                  mov word ptr [r12], si
00AF3DD4  B8 10 00 00 00                  mov eax, 0x10
00AF3DD9  66 41 89 44 24 02               mov word ptr [r12 + 2], ax
00AF3DDF  0F B7 81 90 11 00 00            movzx eax, word ptr [rcx + 0x1190]
00AF3DE6  66 41 89 44 24 06               mov word ptr [r12 + 6], ax
00AF3DEC  41 0F B7 44 24 04               movzx eax, word ptr [r12 + 4]
00AF3DF2  BA FE FF 00 00                  mov edx, 0xfffe
00AF3DF7  66 23 C2                        and ax, dx
00AF3DFA  66 41 89 44 24 04               mov word ptr [r12 + 4], ax
00AF3E00  66 45 89 74 24 04               mov word ptr [r12 + 4], r14w
00AF3E06  44 0F B7 81 90 11 00 00         movzx r8d, word ptr [rcx + 0x1190]
00AF3E0E  66 41 2B F0                     sub si, r8w
00AF3E12  66 83 EE 08                     sub si, 8
00AF3E16  49 8D 5C 24 08                  lea rbx, [r12 + 8]
00AF3E1B  48 8B 91 88 11 00 00            mov rdx, qword ptr [rcx + 0x1188]
00AF3E22  48 8B CB                        mov rcx, rbx
00AF3E25  E8 16 2A BD FF                  call 0x1406c6840
00AF3E2A  44 0F B7 C6                     movzx r8d, si
00AF3E2E  48 8B 8D F0 00 00 00            mov rcx, qword ptr [rbp + 0xf0]
00AF3E35  0F B7 89 90 11 00 00            movzx ecx, word ptr [rcx + 0x1190]
00AF3E3C  48 03 CB                        add rcx, rbx
00AF3E3F  33 D2                           xor edx, edx
00AF3E41  E8 FA 2D BD FF                  call 0x1406c6c40
00AF3E46  BE 01 00 00 00                  mov esi, 1
00AF3E4B  66 41 09 75 04                  or word ptr [r13 + 4], si
00AF3E50  41 0F B7 1C 24                  movzx ebx, word ptr [r12]
00AF3E55  83 C3 50                        add ebx, 0x50
00AF3E58  89 5D 20                        mov dword ptr [rbp + 0x20], ebx
00AF3E5B  4C 89 65 58                     mov qword ptr [rbp + 0x58], r12
00AF3E5F  41 B8 10 00 00 00               mov r8d, 0x10
00AF3E65  41 84 F8                        test r8b, dil
00AF3E68  74 63                           je 0x140af3ecd
00AF3E6A  4A 8D 14 2B                     lea rdx, [rbx + r13]
00AF3E6E  C7 02 18 00 01 00               mov dword ptr [rdx], 0x10018
00AF3E74  66 44 89 42 06                  mov word ptr [rdx + 6], r8w
00AF3E79  0F B7 42 04                     movzx eax, word ptr [rdx + 4]
00AF3E7D  41 B9 FE FF 00 00               mov r9d, 0xfffe
00AF3E83  66 41 23 C1                     and ax, r9w
00AF3E87  66 89 42 04                     mov word ptr [rdx + 4], ax
00AF3E8B  66 44 89 72 04                  mov word ptr [rdx + 4], r14w
00AF3E90  48 8B 85 50 05 00 00            mov rax, qword ptr [rbp + 0x550]
00AF3E97  0F 10 00                        movups xmm0, xmmword ptr [rax]
00AF3E9A  F3 0F 7F 42 08                  movdqu xmmword ptr [rdx + 8], xmm0
00AF3E9F  41 0F B7 45 04                  movzx eax, word ptr [r13 + 4]
00AF3EA4  66 0B C6                        or ax, si
00AF3EA7  66 41 89 45 04                  mov word ptr [r13 + 4], ax
00AF3EAC  83 C3 18                        add ebx, 0x18
00AF3EAF  89 5D 20                        mov dword ptr [rbp + 0x20], ebx
00AF3EB2  4D 85 E4                        test r12, r12
00AF3EB5  74 0F                           je 0x140af3ec6
00AF3EB7  41 0F B7 44 24 04               movzx eax, word ptr [r12 + 4]
00AF3EBD  66 0B C6                        or ax, si
00AF3EC0  66 41 89 44 24 04               mov word ptr [r12 + 4], ax
00AF3EC6  4C 8B E2                        mov r12, rdx
00AF3EC9  48 89 55 58                     mov qword ptr [rbp + 0x58], rdx
00AF3ECD  40 F6 C7 02                     test dil, 2
00AF3ED1  74 5B                           je 0x140af3f2e
00AF3ED3  8B C3                           mov eax, ebx
00AF3ED5  49 03 C5                        add rax, r13
00AF3ED8  48 89 85 80 00 00 00            mov qword ptr [rbp + 0x80], rax
00AF3EDF  44 0F B7 85 70 04 00 00         movzx r8d, word ptr [rbp + 0x470]
00AF3EE7  48 8D 95 70 04 00 00            lea rdx, [rbp + 0x470]
00AF3EEE  48 8B C8                        mov rcx, rax
00AF3EF1  E8 4A 29 BD FF                  call 0x1406c6840
00AF3EF6  41 0F B7 45 04                  movzx eax, word ptr [r13 + 4]
00AF3EFB  66 0B C6                        or ax, si
00AF3EFE  66 41 89 45 04                  mov word ptr [r13 + 4], ax
00AF3F03  0F B7 85 70 04 00 00            movzx eax, word ptr [rbp + 0x470]
00AF3F0A  03 D8                           add ebx, eax
00AF3F0C  89 5D 20                        mov dword ptr [rbp + 0x20], ebx
00AF3F0F  4D 85 E4                        test r12, r12
00AF3F12  74 0F                           je 0x140af3f23
00AF3F14  41 0F B7 44 24 04               movzx eax, word ptr [r12 + 4]
00AF3F1A  66 0B C6                        or ax, si
00AF3F1D  66 41 89 44 24 04               mov word ptr [r12 + 4], ax
00AF3F23  4C 8B A5 80 00 00 00            mov r12, qword ptr [rbp + 0x80]
00AF3F2A  4C 89 65 58                     mov qword ptr [rbp + 0x58], r12
00AF3F2E  40 84 FE                        test sil, dil
00AF3F31  74 62                           je 0x140af3f95
00AF3F33  4A 8D 0C 2B                     lea rcx, [rbx + r13]
00AF3F37  C7 01 10 00 03 00               mov dword ptr [rcx], 0x30010
00AF3F3D  B8 04 00 00 00                  mov eax, 4
00AF3F42  66 89 41 06                     mov word ptr [rcx + 6], ax
00AF3F46  0F B7 41 04                     movzx eax, word ptr [rcx + 4]
00AF3F4A  BA FE FF 00 00                  mov edx, 0xfffe
00AF3F4F  66 23 C2                        and ax, dx
00AF3F52  66 89 41 04                     mov word ptr [rcx + 4], ax
00AF3F56  66 44 89 71 04                  mov word ptr [rcx + 4], r14w
00AF3F5B  E8 70 C4 73 FF                  call 0x1402303d0
00AF3F60  4A 8D 0C 2B                     lea rcx, [rbx + r13]
00AF3F64  89 41 08                        mov dword ptr [rcx + 8], eax
00AF3F67  41 0F B7 45 04                  movzx eax, word ptr [r13 + 4]
00AF3F6C  66 0B C6                        or ax, si
00AF3F6F  66 41 89 45 04                  mov word ptr [r13 + 4], ax
00AF3F74  83 C3 10                        add ebx, 0x10
00AF3F77  89 5D 20                        mov dword ptr [rbp + 0x20], ebx
00AF3F7A  4D 85 E4                        test r12, r12
00AF3F7D  74 0F                           je 0x140af3f8e
00AF3F7F  41 0F B7 44 24 04               movzx eax, word ptr [r12 + 4]
00AF3F85  66 0B C6                        or ax, si
00AF3F88  66 41 89 44 24 04               mov word ptr [r12 + 4], ax
00AF3F8E  4C 8B E1                        mov r12, rcx
00AF3F91  48 89 4D 58                     mov qword ptr [rbp + 0x58], rcx
00AF3F95  41 BB 10 00 00 00               mov r11d, 0x10
00AF3F9B  40 F6 C7 40                     test dil, 0x40
00AF3F9F  74 76                           je 0x140af4017
00AF3FA1  4E 8D 04 2B                     lea r8, [rbx + r13]
00AF3FA5  41 C7 00 10 00 0D 00            mov dword ptr [r8], 0xd0010
00AF3FAC  41 8D 43 F8                     lea eax, [r11 - 8]
00AF3FB0  66 41 89 40 06                  mov word ptr [r8 + 6], ax
00AF3FB5  41 0F B7 40 04                  movzx eax, word ptr [r8 + 4]
00AF3FBA  B9 FE FF 00 00                  mov ecx, 0xfffe
00AF3FBF  66 23 C1                        and ax, cx
00AF3FC2  66 41 89 40 04                  mov word ptr [r8 + 4], ax
00AF3FC7  66 45 89 70 04                  mov word ptr [r8 + 4], r14w
00AF3FCC  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AF3FD5  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
00AF3FDC  E8 9F 51 96 FF                  call 0x140459180
00AF3FE1  49 89 40 08                     mov qword ptr [r8 + 8], rax
00AF3FE5  41 0F B7 45 04                  movzx eax, word ptr [r13 + 4]
00AF3FEA  66 0B C6                        or ax, si
00AF3FED  66 41 89 45 04                  mov word ptr [r13 + 4], ax
00AF3FF2  41 03 DB                        add ebx, r11d
00AF3FF5  89 5D 20                        mov dword ptr [rbp + 0x20], ebx
00AF3FF8  4D 85 E4                        test r12, r12
00AF3FFB  74 0F                           je 0x140af400c
00AF3FFD  41 0F B7 44 24 04               movzx eax, word ptr [r12 + 4]
00AF4003  66 0B C6                        or ax, si
00AF4006  66 41 89 44 24 04               mov word ptr [r12 + 4], ax
00AF400C  4D 8B E0                        mov r12, r8
00AF400F  4C 89 45 58                     mov qword ptr [rbp + 0x58], r8
00AF4013  44 8B 7D 10                     mov r15d, dword ptr [rbp + 0x10]
00AF4017  40 84 FF                        test dil, dil
00AF401A  0F 89 94 00 00 00               jns 0x140af40b4
00AF4020  44 8B D3                        mov r10d, ebx
00AF4023  4E 8D 0C 2B                     lea r9, [rbx + r13]
00AF4027  41 C7 01 10 00 0A 00            mov dword ptr [r9], 0xa0010
00AF402E  B8 08 00 00 00                  mov eax, 8
00AF4033  66 41 89 41 06                  mov word ptr [r9 + 6], ax
00AF4038  41 0F B7 41 04                  movzx eax, word ptr [r9 + 4]
00AF403D  B9 FE FF 00 00                  mov ecx, 0xfffe
00AF4042  66 23 C1                        and ax, cx
00AF4045  66 41 89 41 04                  mov word ptr [r9 + 4], ax
00AF404A  66 45 89 71 04                  mov word ptr [r9 + 4], r14w
00AF404F  44 84 5D 00                     test byte ptr [rbp], r11b
00AF4053  75 26                           jne 0x140af407b
00AF4055  48 8D 8D D8 00 00 00            lea rcx, [rbp + 0xd8]
00AF405C  E8 4F 86 94 FF                  call 0x14043c6b0
00AF4061  44 08 5D 00                     or byte ptr [rbp], r11b
00AF4065  48 8B 8D 20 01 00 00            mov rcx, qword ptr [rbp + 0x120]
00AF406C  48 85 C9                        test rcx, rcx
00AF406F  74 0A                           je 0x140af407b
00AF4071  48 8B 85 D8 00 00 00            mov rax, qword ptr [rbp + 0xd8]
00AF4078  48 89 01                        mov qword ptr [rcx], rax
00AF407B  48 8B 85 D8 00 00 00            mov rax, qword ptr [rbp + 0xd8]
00AF4082  49 89 41 08                     mov qword ptr [r9 + 8], rax
00AF4086  41 0F B7 45 04                  movzx eax, word ptr [r13 + 4]
00AF408B  66 0B C6                        or ax, si
00AF408E  66 41 89 45 04                  mov word ptr [r13 + 4], ax
00AF4093  83 C3 10                        add ebx, 0x10
00AF4096  89 5D 20                        mov dword ptr [rbp + 0x20], ebx
00AF4099  4D 85 E4                        test r12, r12
00AF409C  74 0F                           je 0x140af40ad
00AF409E  41 0F B7 44 24 04               movzx eax, word ptr [r12 + 4]
00AF40A4  66 0B C6                        or ax, si
00AF40A7  66 41 89 44 24 04               mov word ptr [r12 + 4], ax
00AF40AD  4D 8B E1                        mov r12, r9
00AF40B0  4C 89 4D 58                     mov qword ptr [rbp + 0x58], r9
00AF40B4  B8 04 00 00 00                  mov eax, 4
00AF40B9  40 84 F8                        test al, dil
00AF40BC  74 5F                           je 0x140af411d
00AF40BE  8B C3                           mov eax, ebx
00AF40C0  49 03 C5                        add rax, r13
00AF40C3  48 89 85 80 00 00 00            mov qword ptr [rbp + 0x80], rax
00AF40CA  48 8B 8D A0 00 00 00            mov rcx, qword ptr [rbp + 0xa0]
00AF40D1  44 0F B7 01                     movzx r8d, word ptr [rcx]
00AF40D5  48 8B D1                        mov rdx, rcx
00AF40D8  48 8B C8                        mov rcx, rax
00AF40DB  E8 60 27 BD FF                  call 0x1406c6840
00AF40E0  41 0F B7 45 04                  movzx eax, word ptr [r13 + 4]
00AF40E5  66 0B C6                        or ax, si
00AF40E8  66 41 89 45 04                  mov word ptr [r13 + 4], ax
00AF40ED  48 8B 95 A0 00 00 00            mov rdx, qword ptr [rbp + 0xa0]
00AF40F4  0F B7 02                        movzx eax, word ptr [rdx]
00AF40F7  03 D8                           add ebx, eax
00AF40F9  89 5D 20                        mov dword ptr [rbp + 0x20], ebx
00AF40FC  4D 85 E4                        test r12, r12
00AF40FF  74 0F                           je 0x140af4110
00AF4101  41 0F B7 44 24 04               movzx eax, word ptr [r12 + 4]
00AF4107  66 0B C6                        or ax, si
00AF410A  66 41 89 44 24 04               mov word ptr [r12 + 4], ax
00AF4110  4C 8B A5 80 00 00 00            mov r12, qword ptr [rbp + 0x80]
00AF4117  4C 89 65 58                     mov qword ptr [rbp + 0x58], r12
00AF411B  EB 07                           jmp 0x140af4124
00AF411D  48 8B 95 A0 00 00 00            mov rdx, qword ptr [rbp + 0xa0]
00AF4124  41 B8 08 00 00 00               mov r8d, 8
00AF412A  41 84 F8                        test r8b, dil
00AF412D  74 6C                           je 0x140af419b
00AF412F  8B CB                           mov ecx, ebx
00AF4131  49 03 CD                        add rcx, r13
00AF4134  45 8D 50 10                     lea r10d, [r8 + 0x10]
00AF4138  C7 01 18 00 12 00               mov dword ptr [rcx], 0x120018
00AF413E  41 8D 40 08                     lea eax, [r8 + 8]
00AF4142  66 89 41 06                     mov word ptr [rcx + 6], ax
00AF4146  0F B7 41 04                     movzx eax, word ptr [rcx + 4]
00AF414A  41 B9 FE FF 00 00               mov r9d, 0xfffe
00AF4150  66 41 23 C1                     and ax, r9w
00AF4154  66 89 41 04                     mov word ptr [rcx + 4], ax
00AF4158  66 44 89 71 04                  mov word ptr [rcx + 4], r14w
00AF415D  48 8B 45 60                     mov rax, qword ptr [rbp + 0x60]
00AF4161  48 89 41 10                     mov qword ptr [rcx + 0x10], rax
00AF4165  48 8B 42 08                     mov rax, qword ptr [rdx + 8]
00AF4169  48 89 41 08                     mov qword ptr [rcx + 8], rax
00AF416D  41 0F B7 45 04                  movzx eax, word ptr [r13 + 4]
00AF4172  66 0B C6                        or ax, si
00AF4175  66 41 89 45 04                  mov word ptr [r13 + 4], ax
00AF417A  41 03 DA                        add ebx, r10d
00AF417D  89 5D 20                        mov dword ptr [rbp + 0x20], ebx
00AF4180  4D 85 E4                        test r12, r12
00AF4183  74 0F                           je 0x140af4194
00AF4185  41 0F B7 44 24 04               movzx eax, word ptr [r12 + 4]
00AF418B  66 0B C6                        or ax, si
00AF418E  66 41 89 44 24 04               mov word ptr [r12 + 4], ax
00AF4194  4C 8B E1                        mov r12, rcx
00AF4197  48 89 4D 58                     mov qword ptr [rbp + 0x58], rcx
00AF419B  40 F6 C7 20                     test dil, 0x20
00AF419F  74 58                           je 0x140af41f9
00AF41A1  8B FB                           mov edi, ebx
00AF41A3  49 03 FD                        add rdi, r13
00AF41A6  48 8B 85 E0 00 00 00            mov rax, qword ptr [rbp + 0xe0]
00AF41AD  44 0F B7 00                     movzx r8d, word ptr [rax]
00AF41B1  48 8B D0                        mov rdx, rax
00AF41B4  48 8B CF                        mov rcx, rdi
00AF41B7  E8 84 26 BD FF                  call 0x1406c6840
00AF41BC  41 0F B7 45 04                  movzx eax, word ptr [r13 + 4]
00AF41C1  66 0B C6                        or ax, si
00AF41C4  66 41 89 45 04                  mov word ptr [r13 + 4], ax
00AF41C9  48 8B 85 E0 00 00 00            mov rax, qword ptr [rbp + 0xe0]
00AF41D0  0F B7 00                        movzx eax, word ptr [rax]
00AF41D3  03 D8                           add ebx, eax
00AF41D5  89 5D 20                        mov dword ptr [rbp + 0x20], ebx
00AF41D8  4D 85 E4                        test r12, r12
00AF41DB  74 0F                           je 0x140af41ec
00AF41DD  41 0F B7 44 24 04               movzx eax, word ptr [r12 + 4]
00AF41E3  66 0B C6                        or ax, si
00AF41E6  66 41 89 44 24 04               mov word ptr [r12 + 4], ax
00AF41EC  4C 8B E7                        mov r12, rdi
00AF41EF  48 89 7D 58                     mov qword ptr [rbp + 0x58], rdi
00AF41F3  41 B8 08 00 00 00               mov r8d, 8
00AF41F9  0F B7 55 48                     movzx edx, word ptr [rbp + 0x48]
00AF41FD  66 85 D2                        test dx, dx
00AF4200  0F 84 AF 00 00 00               je 0x140af42b5
00AF4206  8B CB                           mov ecx, ebx
00AF4208  49 03 CD                        add rcx, r13
00AF420B  48 89 8D 80 00 00 00            mov qword ptr [rbp + 0x80], rcx
00AF4212  BE 0F 00 00 00                  mov esi, 0xf
00AF4217  03 F2                           add esi, edx
00AF4219  B8 F8 FF 00 00                  mov eax, 0xfff8
00AF421E  66 23 F0                        and si, ax
00AF4221  66 89 31                        mov word ptr [rcx], si
00AF4224  B8 0C 00 00 00                  mov eax, 0xc
00AF4229  66 89 41 02                     mov word ptr [rcx + 2], ax
00AF422D  66 89 51 06                     mov word ptr [rcx + 6], dx
00AF4231  0F B7 41 04                     movzx eax, word ptr [rcx + 4]
00AF4235  41 B9 FE FF 00 00               mov r9d, 0xfffe
00AF423B  66 41 23 C1                     and ax, r9w
00AF423F  66 89 41 04                     mov word ptr [rcx + 4], ax
00AF4243  66 44 89 71 04                  mov word ptr [rcx + 4], r14w
00AF4248  66 2B F2                        sub si, dx
00AF424B  66 41 2B F0                     sub si, r8w
00AF424F  48 8D 79 08                     lea rdi, [rcx + 8]
00AF4253  8B DA                           mov ebx, edx
00AF4255  44 8B C2                        mov r8d, edx
00AF4258  48 8B 95 28 01 00 00            mov rdx, qword ptr [rbp + 0x128]
00AF425F  48 8B CF                        mov rcx, rdi
00AF4262  E8 D9 25 BD FF                  call 0x1406c6840
00AF4267  44 0F B7 C6                     movzx r8d, si
00AF426B  48 8D 0C 3B                     lea rcx, [rbx + rdi]
00AF426F  33 D2                           xor edx, edx
00AF4271  E8 CA 29 BD FF                  call 0x1406c6c40
00AF4276  41 0F B7 45 04                  movzx eax, word ptr [r13 + 4]
00AF427B  BE 01 00 00 00                  mov esi, 1
00AF4280  66 0B C6                        or ax, si
00AF4283  66 41 89 45 04                  mov word ptr [r13 + 4], ax
00AF4288  48 8B 8D 80 00 00 00            mov rcx, qword ptr [rbp + 0x80]
00AF428F  0F B7 01                        movzx eax, word ptr [rcx]
00AF4292  8B 5D 20                        mov ebx, dword ptr [rbp + 0x20]
00AF4295  03 D8                           add ebx, eax
00AF4297  89 5D 20                        mov dword ptr [rbp + 0x20], ebx
00AF429A  4D 85 E4                        test r12, r12
00AF429D  74 0F                           je 0x140af42ae
00AF429F  41 0F B7 44 24 04               movzx eax, word ptr [r12 + 4]
00AF42A5  66 0B C6                        or ax, si
00AF42A8  66 41 89 44 24 04               mov word ptr [r12 + 4], ax
00AF42AE  4C 8B E1                        mov r12, rcx
00AF42B1  48 89 4D 58                     mov qword ptr [rbp + 0x58], rcx
00AF42B5  44 39 75 3C                     cmp dword ptr [rbp + 0x3c], r14d
00AF42B9  0F 84 9B 00 00 00               je 0x140af435a
00AF42BF  49 03 DD                        add rbx, r13
00AF42C2  8B 55 50                        mov edx, dword ptr [rbp + 0x50]
00AF42C5  41 B8 0F 00 00 00               mov r8d, 0xf
00AF42CB  44 03 C2                        add r8d, edx
00AF42CE  B8 F8 FF 00 00                  mov eax, 0xfff8
00AF42D3  66 44 23 C0                     and r8w, ax
00AF42D7  66 44 89 03                     mov word ptr [rbx], r8w
00AF42DB  B8 0B 00 00 00                  mov eax, 0xb
00AF42E0  66 89 43 02                     mov word ptr [rbx + 2], ax
00AF42E4  66 89 53 06                     mov word ptr [rbx + 6], dx
00AF42E8  0F B7 43 04                     movzx eax, word ptr [rbx + 4]
00AF42EC  B9 FE FF 00 00                  mov ecx, 0xfffe
00AF42F1  66 23 C1                        and ax, cx
00AF42F4  66 89 43 04                     mov word ptr [rbx + 4], ax
00AF42F8  66 44 89 73 04                  mov word ptr [rbx + 4], r14w
00AF42FD  66 44 2B C2                     sub r8w, dx
00AF4301  66 41 83 E8 08                  sub r8w, 8
00AF4306  48 8D 4B 08                     lea rcx, [rbx + 8]
00AF430A  48 89 8D C8 00 00 00            mov qword ptr [rbp + 0xc8], rcx
00AF4311  4C 8D 0C 11                     lea r9, [rcx + rdx]
00AF4315  48 8D 04 11                     lea rax, [rcx + rdx]
00AF4319  48 89 85 30 01 00 00            mov qword ptr [rbp + 0x130], rax
00AF4320  45 0F B7 C0                     movzx r8d, r8w
00AF4324  33 D2                           xor edx, edx
00AF4326  49 8B C9                        mov rcx, r9
00AF4329  E8 12 29 BD FF                  call 0x1406c6c40
00AF432E  41 0F B7 45 04                  movzx eax, word ptr [r13 + 4]
00AF4333  66 0B C6                        or ax, si
00AF4336  66 41 89 45 04                  mov word ptr [r13 + 4], ax
00AF433B  0F B7 03                        movzx eax, word ptr [rbx]
00AF433E  8B 5D 20                        mov ebx, dword ptr [rbp + 0x20]
00AF4341  03 D8                           add ebx, eax
00AF4343  89 5D 20                        mov dword ptr [rbp + 0x20], ebx
00AF4346  4D 85 E4                        test r12, r12
00AF4349  74 0F                           je 0x140af435a
00AF434B  41 0F B7 44 24 04               movzx eax, word ptr [r12 + 4]
00AF4351  66 0B C6                        or ax, si
00AF4354  66 41 89 44 24 04               mov word ptr [r12 + 4], ax
00AF435A  45 8B E6                        mov r12d, r14d
00AF435D  44 89 B5 C0 00 00 00            mov dword ptr [rbp + 0xc0], r14d
00AF4364  8B BD 68 05 00 00               mov edi, dword ptr [rbp + 0x568]
00AF436A  44 3B E7                        cmp r12d, edi
00AF436D  0F 83 A7 01 00 00               jae 0x140af451a
00AF4373  41 8B C4                        mov eax, r12d
00AF4376  48 03 C0                        add rax, rax
00AF4379  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
00AF437D  8B 7C C1 08                     mov edi, dword ptr [rcx + rax*8 + 8]
00AF4381  48 8B 14 C1                     mov rdx, qword ptr [rcx + rax*8]
00AF4385  66 44 39 75 4C                  cmp word ptr [rbp + 0x4c], r14w
00AF438A  75 05                           jne 0x140af4391
00AF438C  41 8A C6                        mov al, r14b
00AF438F  EB 08                           jmp 0x140af4399
00AF4391  8A 44 C1 0C                     mov al, byte ptr [rcx + rax*8 + 0xc]
00AF4395  44 8B 7D 10                     mov r15d, dword ptr [rbp + 0x10]
00AF4399  0F B6 C8                        movzx ecx, al
00AF439C  84 C0                           test al, al
00AF439E  0F 84 D3 00 00 00               je 0x140af4477
00AF43A4  83 E9 01                        sub ecx, 1
00AF43A7  74 37                           je 0x140af43e0
00AF43A9  83 F9 02                        cmp ecx, 2
00AF43AC  75 2D                           jne 0x140af43db
00AF43AE  83 FF 08                        cmp edi, 8
00AF43B1  75 28                           jne 0x140af43db
00AF43B3  48 8D 42 08                     lea rax, [rdx + 8]
00AF43B7  48 B9 00 00 FF FF FF 7F 00 00   movabs rcx, 0x7fffffff0000
00AF43C1  48 3B C1                        cmp rax, rcx
00AF43C4  77 05                           ja 0x140af43cb
00AF43C6  48 3B C2                        cmp rax, rdx
00AF43C9  73 06                           jae 0x140af43d1
00AF43CB  8A 01                           mov al, byte ptr [rcx]
00AF43CD  44 8B 7D 10                     mov r15d, dword ptr [rbp + 0x10]
00AF43D1  48 8B 02                        mov rax, qword ptr [rdx]
00AF43D4  48 89 85 A8 00 00 00            mov qword ptr [rbp + 0xa8], rax
00AF43DB  E9 F1 00 00 00                  jmp 0x140af44d1
00AF43E0  48 8B 8D C8 00 00 00            mov rcx, qword ptr [rbp + 0xc8]
00AF43E7  48 85 C9                        test rcx, rcx
00AF43EA  74 55                           je 0x140af4441
00AF43EC  48 8D 04 0F                     lea rax, [rdi + rcx]
00AF43F0  48 3B C1                        cmp rax, rcx
00AF43F3  72 4C                           jb 0x140af4441
00AF43F5  48 3B 85 30 01 00 00            cmp rax, qword ptr [rbp + 0x130]
00AF43FC  77 43                           ja 0x140af4441
00AF43FE  44 39 75 3C                     cmp dword ptr [rbp + 0x3c], r14d
00AF4402  74 3D                           je 0x140af4441
00AF4404  85 FF                           test edi, edi
00AF4406  74 1E                           je 0x140af4426
00AF4408  48 8D 04 17                     lea rax, [rdi + rdx]
00AF440C  48 B9 00 00 FF FF FF 7F 00 00   movabs rcx, 0x7fffffff0000
00AF4416  48 3B C1                        cmp rax, rcx
00AF4419  77 05                           ja 0x140af4420
00AF441B  48 3B C2                        cmp rax, rdx
00AF441E  73 06                           jae 0x140af4426
00AF4420  8A 01                           mov al, byte ptr [rcx]
00AF4422  44 8B 7D 10                     mov r15d, dword ptr [rbp + 0x10]
00AF4426  4C 8B C7                        mov r8, rdi
00AF4429  48 8B 8D C8 00 00 00            mov rcx, qword ptr [rbp + 0xc8]
00AF4430  E8 0B 24 BD FF                  call 0x1406c6840
00AF4435  48 01 BD C8 00 00 00            add qword ptr [rbp + 0xc8], rdi
00AF443C  FF 4D 3C                        dec dword ptr [rbp + 0x3c]
00AF443F  EB 9A                           jmp 0x140af43db
00AF4441  C7 45 1C 04 00 00 C0            mov dword ptr [rbp + 0x1c], 0xc0000004
00AF4448  41 81 CF 00 00 0D C0            or r15d, 0xc00d0000
00AF444F  45 89 7D 00                     mov dword ptr [r13], r15d
00AF4453  48 8B 85 A8 00 00 00            mov rax, qword ptr [rbp + 0xa8]
00AF445A  49 89 45 10                     mov qword ptr [r13 + 0x10], rax
00AF445E  BF 01 00 00 00                  mov edi, 1
00AF4463  4C 8B 7D 40                     mov r15, qword ptr [rbp + 0x40]
00AF4467  4C 8B 6D 30                     mov r13, qword ptr [rbp + 0x30]
00AF446B  4C 8B 65 28                     mov r12, qword ptr [rbp + 0x28]
00AF446F  8B 75 18                        mov esi, dword ptr [rbp + 0x18]
00AF4472  E9 F3 01 00 00                  jmp 0x140af466a
00AF4477  44 8B CB                        mov r9d, ebx
00AF447A  4D 03 CD                        add r9, r13
00AF447D  8D 04 1F                        lea eax, [rdi + rbx]
00AF4480  3B C3                           cmp eax, ebx
00AF4482  72 5C                           jb 0x140af44e0
00AF4484  8B D8                           mov ebx, eax
00AF4486  89 45 20                        mov dword ptr [rbp + 0x20], eax
00AF4489  41 3B C7                        cmp eax, r15d
00AF448C  77 56                           ja 0x140af44e4
00AF448E  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AF4497  8A 88 32 02 00 00               mov cl, byte ptr [rax + 0x232]
00AF449D  88 4D 15                        mov byte ptr [rbp + 0x15], cl
00AF44A0  84 C9                           test cl, cl
00AF44A2  74 1E                           je 0x140af44c2
00AF44A4  85 FF                           test edi, edi
00AF44A6  74 1A                           je 0x140af44c2
00AF44A8  48 8D 0C 3A                     lea rcx, [rdx + rdi]
00AF44AC  48 B8 00 00 FF FF FF 7F 00 00   movabs rax, 0x7fffffff0000
00AF44B6  48 3B C8                        cmp rcx, rax
00AF44B9  77 05                           ja 0x140af44c0
00AF44BB  48 3B CA                        cmp rcx, rdx
00AF44BE  73 02                           jae 0x140af44c2
00AF44C0  8A 00                           mov al, byte ptr [rax]
00AF44C2  4C 8B C7                        mov r8, rdi
00AF44C5  49 8B C9                        mov rcx, r9
00AF44C8  E8 73 23 BD FF                  call 0x1406c6840
00AF44CD  44 8B 7D 10                     mov r15d, dword ptr [rbp + 0x10]
00AF44D1  44 03 E6                        add r12d, esi
00AF44D4  44 89 A5 C0 00 00 00            mov dword ptr [rbp + 0xc0], r12d
00AF44DB  E9 84 FE FF FF                  jmp 0x140af4364
00AF44E0  83 4D 20 FF                     or dword ptr [rbp + 0x20], 0xffffffff
00AF44E4  C7 45 1C 04 00 00 C0            mov dword ptr [rbp + 0x1c], 0xc0000004
00AF44EB  41 81 CF 00 00 0D C0            or r15d, 0xc00d0000
00AF44F2  45 89 7D 00                     mov dword ptr [r13], r15d
00AF44F6  48 8B 85 A8 00 00 00            mov rax, qword ptr [rbp + 0xa8]
00AF44FD  49 89 45 10                     mov qword ptr [r13 + 0x10], rax
00AF4501  BF 01 00 00 00                  mov edi, 1
00AF4506  4C 8B 7D 40                     mov r15, qword ptr [rbp + 0x40]
00AF450A  4C 8B 6D 30                     mov r13, qword ptr [rbp + 0x30]
00AF450E  4C 8B 65 28                     mov r12, qword ptr [rbp + 0x28]
00AF4512  8B 75 18                        mov esi, dword ptr [rbp + 0x18]
00AF4515  E9 50 01 00 00                  jmp 0x140af466a
00AF451A  4C 8B 45 70                     mov r8, qword ptr [rbp + 0x70]
00AF451E  4D 85 C0                        test r8, r8
00AF4521  74 18                           je 0x140af453b
00AF4523  8B 4D 24                        mov ecx, dword ptr [rbp + 0x24]
00AF4526  8B C1                           mov eax, ecx
00AF4528  C1 E8 05                        shr eax, 5
00AF452B  8B D0                           mov edx, eax
00AF452D  83 E1 1F                        and ecx, 0x1f
00AF4530  41 8B 04 80                     mov eax, dword ptr [r8 + rax*4]
00AF4534  0F AB C8                        bts eax, ecx
00AF4537  41 89 04 90                     mov dword ptr [r8 + rdx*4], eax
00AF453B  48 8B 85 A8 00 00 00            mov rax, qword ptr [rbp + 0xa8]
00AF4542  49 89 45 10                     mov qword ptr [r13 + 0x10], rax
00AF4546  48 8B 8D 08 01 00 00            mov rcx, qword ptr [rbp + 0x108]
00AF454D  8B 81 8C 02 00 00               mov eax, dword ptr [rcx + 0x28c]
00AF4553  41 89 45 38                     mov dword ptr [r13 + 0x38], eax
00AF4557  8B 81 DC 02 00 00               mov eax, dword ptr [rcx + 0x2dc]
00AF455D  41 89 45 3C                     mov dword ptr [r13 + 0x3c], eax
00AF4561  8B 81 10 05 00 00               mov eax, dword ptr [rcx + 0x510]
00AF4567  41 89 45 08                     mov dword ptr [r13 + 8], eax
00AF456B  8B 81 08 05 00 00               mov eax, dword ptr [rcx + 0x508]
00AF4571  41 89 45 0C                     mov dword ptr [r13 + 0xc], eax
00AF4575  4C 8B 7D 40                     mov r15, qword ptr [rbp + 0x40]
00AF4579  41 F7 47 0C 00 00 08 00         test dword ptr [r15 + 0xc], 0x80000
00AF4581  74 2E                           je 0x140af45b1
00AF4583  80 3D 52 30 45 00 00            cmp byte ptr [rip + 0x453052], 0
00AF458A  75 09                           jne 0x140af4595
00AF458C  80 3D 89 64 31 00 00            cmp byte ptr [rip + 0x316489], 0
00AF4593  74 09                           je 0x140af459e
00AF4595  80 3D 17 17 46 00 00            cmp byte ptr [rip + 0x461717], 0
00AF459C  74 13                           je 0x140af45b1
00AF459E  48 8D 95 48 01 00 00            lea rdx, [rbp + 0x148]
00AF45A5  49 8B CF                        mov rcx, r15
00AF45A8  E8 63 28 9C FF                  call 0x1404b6e10
00AF45AD  4C 8B 45 70                     mov r8, qword ptr [rbp + 0x70]
00AF45B1  4D 39 B7 20 06 00 00            cmp qword ptr [r15 + 0x620], r14
00AF45B8  4C 8B 6D 30                     mov r13, qword ptr [rbp + 0x30]
00AF45BC  4C 8B 65 28                     mov r12, qword ptr [rbp + 0x28]
00AF45C0  4C 8B 5D 68                     mov r11, qword ptr [rbp + 0x68]
00AF45C4  48 8B 9D 60 05 00 00            mov rbx, qword ptr [rbp + 0x560]
00AF45CB  0F 84 1B EC FF FF               je 0x140af31ec
00AF45D1  65 4C 8B 0C 25 88 01 00 00      mov r9, qword ptr gs:[0x188]
00AF45DA  4C 8B 85 B0 00 00 00            mov r8, qword ptr [rbp + 0xb0]
00AF45E1  49 83 C0 28                     add r8, 0x28
00AF45E5  45 8A 89 32 02 00 00            mov r9b, byte ptr [r9 + 0x232]
00AF45EC  48 8D 95 48 01 00 00            lea rdx, [rbp + 0x148]
00AF45F3  49 8B CF                        mov rcx, r15
00AF45F6  E8 11 29 9C FF                  call 0x1404b6f0c
00AF45FB  4C 8B 65 28                     mov r12, qword ptr [rbp + 0x28]
00AF45FF  4C 8B 5D 68                     mov r11, qword ptr [rbp + 0x68]
00AF4603  4C 8B 45 70                     mov r8, qword ptr [rbp + 0x70]
00AF4607  E9 E0 EB FF FF                  jmp 0x140af31ec
00AF460C  8B 4D 10                        mov ecx, dword ptr [rbp + 0x10]
00AF460F  81 C9 00 00 0D C0               or ecx, 0xc00d0000
00AF4615  48 8B 95 B8 00 00 00            mov rdx, qword ptr [rbp + 0xb8]
00AF461C  89 0A                           mov dword ptr [rdx], ecx
00AF461E  48 8B 8D A8 00 00 00            mov rcx, qword ptr [rbp + 0xa8]
00AF4625  48 89 4A 10                     mov qword ptr [rdx + 0x10], rcx
00AF4629  89 45 1C                        mov dword ptr [rbp + 0x1c], eax
00AF462C  45 33 F6                        xor r14d, r14d
00AF462F  41 8D 7E 01                     lea edi, [r14 + 1]
00AF4633  4C 8B AD F8 00 00 00            mov r13, qword ptr [rbp + 0xf8]
00AF463A  40 8A 75 14                     mov sil, byte ptr [rbp + 0x14]
00AF463E  4C 8B BD 90 00 00 00            mov r15, qword ptr [rbp + 0x90]
00AF4645  8B 45 78                        mov eax, dword ptr [rbp + 0x78]
00AF4648  89 45 24                        mov dword ptr [rbp + 0x24], eax
00AF464B  48 8B 85 38 01 00 00            mov rax, qword ptr [rbp + 0x138]
00AF4652  48 89 85 B0 00 00 00            mov qword ptr [rbp + 0xb0], rax
00AF4659  4C 8B A5 40 01 00 00            mov r12, qword ptr [rbp + 0x140]
00AF4660  EB 08                           jmp 0x140af466a
00AF4662  BF 01 00 00 00                  mov edi, 1
00AF4667  8B 75 18                        mov esi, dword ptr [rbp + 0x18]
00AF466A  E8 D1 AC 9F FF                  call 0x1404ef340
00AF466F  85 C0                           test eax, eax
00AF4671  74 32                           je 0x140af46a5
00AF4673  48 8B 5D 60                     mov rbx, qword ptr [rbp + 0x60]
00AF4677  48 85 DB                        test rbx, rbx
00AF467A  74 0F                           je 0x140af468b
00AF467C  49 8B 97 20 04 00 00            mov rdx, qword ptr [r15 + 0x420]
00AF4683  48 8B CB                        mov rcx, rbx
00AF4686  E8 45 83 90 FF                  call 0x1403fc9d0
00AF468B  40 84 F6                        test sil, sil
00AF468E  74 15                           je 0x140af46a5
00AF4690  8B 45 24                        mov eax, dword ptr [rbp + 0x24]
00AF4693  49 8B 8D C0 02 00 00            mov rcx, qword ptr [r13 + 0x2c0]
00AF469A  8B D7                           mov edx, edi
00AF469C  48 8B 0C C1                     mov rcx, qword ptr [rcx + rax*8]
00AF46A0  E8 AB A9 76 FF                  call 0x14025f050
00AF46A5  F6 45 00 08                     test byte ptr [rbp], 8
00AF46A9  74 0C                           je 0x140af46b7
00AF46AB  48 8B 8D 00 01 00 00            mov rcx, qword ptr [rbp + 0x100]
00AF46B2  E8 B9 90 92 FF                  call 0x14041d770
00AF46B7  44 39 75 1C                     cmp dword ptr [rbp + 0x1c], r14d
00AF46BB  7C 53                           jl 0x140af4710
00AF46BD  44 39 B5 60 04 00 00            cmp dword ptr [rbp + 0x460], r14d
00AF46C4  0F 86 A4 00 00 00               jbe 0x140af476e
00AF46CA  41 8B DE                        mov ebx, r14d
00AF46CD  41 8B C6                        mov eax, r14d
00AF46D0  4C 8D 1C 40                     lea r11, [rax + rax*2]
00AF46D4  4D 03 DB                        add r11, r11
00AF46D7  4A 8D 8C DD 70 01 00 00         lea rcx, [rbp + r11*8 + 0x170]
00AF46DF  E8 3C C6 8F FF                  call 0x1403f0d20
00AF46E4  4E 8B 9C DD 60 01 00 00         mov r11, qword ptr [rbp + r11*8 + 0x160]
00AF46EC  41 8B 03                        mov eax, dword ptr [r11]
00AF46EF  49 8B 8D C0 02 00 00            mov rcx, qword ptr [r13 + 0x2c0]
00AF46F6  8B D7                           mov edx, edi
00AF46F8  48 8B 0C C1                     mov rcx, qword ptr [rcx + rax*8]
00AF46FC  E8 4F A9 76 FF                  call 0x14025f050
00AF4701  FF C3                           inc ebx
00AF4703  44 8B F3                        mov r14d, ebx
00AF4706  3B 9D 60 04 00 00               cmp ebx, dword ptr [rbp + 0x460]
00AF470C  72 BF                           jb 0x140af46cd
00AF470E  EB 5E                           jmp 0x140af476e
00AF4710  48 8B 85 88 00 00 00            mov rax, qword ptr [rbp + 0x88]
00AF4717  48 83 C0 28                     add rax, 0x28
00AF471B  40 88 7C 24 58                  mov byte ptr [rsp + 0x58], dil
00AF4720  4C 89 64 24 50                  mov qword ptr [rsp + 0x50], r12
00AF4725  8B 8D 68 05 00 00               mov ecx, dword ptr [rbp + 0x568]
00AF472B  89 4C 24 48                     mov dword ptr [rsp + 0x48], ecx
00AF472F  40 88 7C 24 40                  mov byte ptr [rsp + 0x40], dil
00AF4734  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00AF4739  8B 45 1C                        mov eax, dword ptr [rbp + 0x1c]
00AF473C  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00AF4740  44 89 74 24 28                  mov dword ptr [rsp + 0x28], r14d
00AF4745  0F B7 45 08                     movzx eax, word ptr [rbp + 8]
00AF4749  66 89 44 24 20                  mov word ptr [rsp + 0x20], ax
00AF474E  4C 8D 8D 60 01 00 00            lea r9, [rbp + 0x160]
00AF4755  4C 8B 85 B0 00 00 00            mov r8, qword ptr [rbp + 0xb0]
00AF475C  48 8B 95 60 05 00 00            mov rdx, qword ptr [rbp + 0x560]
00AF4763  8A 8D 58 05 00 00               mov cl, byte ptr [rbp + 0x558]
00AF4769  E8 E2 C2 8F FF                  call 0x1403f0a50
00AF476E  48 8B 8D 08 01 00 00            mov rcx, qword ptr [rbp + 0x108]
00AF4775  E8 96 A8 76 FF                  call 0x14025f010
00AF477A  8B 45 1C                        mov eax, dword ptr [rbp + 0x1c]
00AF477D  48 8B 8D C0 04 00 00            mov rcx, qword ptr [rbp + 0x4c0]
00AF4784  48 33 CD                        xor rcx, rbp
00AF4787  E8 B4 7E BB FF                  call 0x1406ac640
00AF478C  48 8D A5 D8 04 00 00            lea rsp, [rbp + 0x4d8]
00AF4793  41 5F                           pop r15
00AF4795  41 5E                           pop r14
00AF4797  41 5D                           pop r13
00AF4799  41 5C                           pop r12
00AF479B  5F                              pop rdi
00AF479C  5E                              pop rsi
00AF479D  5B                              pop rbx
00AF479E  5D                              pop rbp
00AF479F  C3                              ret
00AF47A0  CC                              int3
00AF47A1  E8 2A 58 DA FF                  call 0x140899fd0
00AF47A6  90                              nop
00AF47A7  E8 24 58 DA FF                  call 0x140899fd0
00AF47AC  90                              nop
00AF47AD  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwpWriteUserEvent(__int64 a1, int a2, unsigned __int16 a3, __int64 a4, unsigned __int8 a5, __int64 a6, __int64 a7, unsigned __int8 a8, __int64 a9, unsigned int a10, __int64 a11, __int64 a12, __int64 a13, unsigned __int16 a14, __int64 a15, __int64 a16)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m3B8;
    unsigned __int64 v_stack_m3C0;
    unsigned __int64 v_stack_m3D0;
    unsigned __int64 v_stack_m3D8;
    unsigned __int64 v_stack_m3E0;
    unsigned __int64 v_stack_m3E8;
    unsigned __int64 v_stack_m3F0;
    unsigned __int64 v_stack_m3F8;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m400;
    unsigned __int64 v_stack_m408;
    unsigned __int64 v_stack_m410;
    unsigned __int64 v_stack_m418;
    unsigned __int64 v_stack_m420;
    unsigned __int64 v_stack_m428;
    unsigned int v_stack_m430;
    unsigned __int64 v_stack_m438;
    unsigned __int64 v_stack_m440;
    unsigned int v_stack_m448;
    unsigned __int64 v_stack_m450;
    unsigned int v_stack_m458;
    unsigned __int64 v_stack_m460;
    unsigned __int64 v_stack_m468;
    unsigned __int64 v_stack_m470;
    unsigned __int64 v_stack_m478;
    unsigned __int64 v_stack_m480;
    unsigned __int64 v_stack_m488;
    unsigned __int64 v_stack_m490;
    unsigned __int64 v_stack_m498;
    unsigned int v_stack_m4A0;
    unsigned __int64 v_stack_m4A8;
    unsigned __int64 v_stack_m4B0;
    unsigned __int64 v_stack_m4B8;
    unsigned __int64 v_stack_m4C0;
    unsigned __int16 v_stack_m4C4;
    unsigned int v_stack_m4C8;
    unsigned __int16 v_stack_m4CC;
    unsigned __int16 v_stack_m4D0;
    unsigned __int64 v_stack_m4D8;
    unsigned int v_stack_m4DC;
    unsigned int v_stack_m4E0;
    unsigned __int64 v_stack_m4E8;
    unsigned __int64 v_stack_m4F0;
    unsigned int v_stack_m4F4;
    unsigned int v_stack_m4F8;
    unsigned int v_stack_m4FC;
    unsigned int v_stack_m500;
    unsigned __int8 v_stack_m503;
    unsigned __int8 v_stack_m504;
    unsigned int v_stack_m508;
    unsigned __int16 v_stack_m510;
    unsigned __int64 v_stack_m518;
    unsigned __int8 v_stack_m520;
    unsigned __int64 v_stack_m528;
    unsigned int v_stack_m530;
    unsigned __int8 v_stack_m538;
    unsigned __int64 v_stack_m540;
    unsigned __int8 v_stack_m548;
    unsigned __int64 v_stack_m550;
    unsigned int v_stack_m558;
    unsigned int v_stack_m578;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_mA8;
    unsigned int v_stack_mB8;
    unsigned __int16 v_stack_p70;

    v_rsp = (v_rsp) - (0x538ULL);
    result = (*(unsigned __int64 *)(v_rip + 3241780)) ^ (v_stack_m518);
    v_stack_m58 = result;
    v_stack_m4C4 = a3;
    v_stack_m468 = a1;
    v_stack_m4B0 = a13;
    v_stack_m3E0 = a1;
    v_stack_m510 = (unsigned __int16)(a2);
    v_stack_m490 = a6;
    v_stack_m4F0 = a11;
    v_stack_m3D8 = a11;
    v_stack_m4A8 = a12;
    v_stack_m3F0 = a15;
    v_stack_m3F8 = a16;
    v_r14 = 0;
    v_stack_m4FC = 0;
    a2 = 0;
    result = memset(v_stack_m3B8, a2, 776, a4);
    v_stack_m4E0 = 0;
    a2 = 0;
    result = memset(v_stack_mA8, a2, v_r14 + 80, a4);
    v_stack_m478 = 0;
    v_stack_m418 = 0;
    v_stack_m438 = 0;
    v_stack_m4D0 = 0;
    v_stack_m400 = 0;
    v_stack_m480 = 0;
    v_stack_m440 = 0;
    result = PsGetCurrentServerSiloGlobals(v_stack_mA8, a2, v_r14 + 80, a4);
    v_stack_m428 = *(unsigned __int64 *)(result + 832);
    result = (unsigned __int16)((a14) & (256));
    v_stack_m4CC = (unsigned __int16)(result);
    a2 = (unsigned __int16)((a14) >> (9));
    a2 = (unsigned __int8)((a2) & ((unsigned __int8)(v_r14 + 1)));
    v_stack_m500 = 0;
    v_stack_m4B8 = 0;
    v_stack_m4F4 = 0;
    if (a11 != 0) goto loc_00AF3142;
    if ((unsigned int)((unsigned int)(a10)) != 0) goto loc_00AF314E;
    if (a11 == 0) goto loc_00AF3146;
loc_00AF3142:
    if ((unsigned int)((unsigned int)(a10)) == 0) goto loc_00AF314E;
loc_00AF3146:
    if (((unsigned int)((unsigned int)(a10))) <= 128) goto loc_00AF3158;
loc_00AF314E:
    goto loc_00AF477D;
loc_00AF3158:
    v_r11 = v_stack_m4B0;
    if (v_stack_m4B0 == 0) { v_r11 = a1; }
    v_stack_m4B0 = v_r11;
    v_stack_m518 = 0;
    v_stack_m4E8 = *(unsigned __int64 *)(a1 + 648);
    v_stack_m420 = *(unsigned __int64 *)(a1 + 648);
    if (v_stack_m3F8 == 0) goto loc_00AF319C;
    if (*(unsigned __int64 *)(v_stack_m3F8) != 0) {
        v_stack_m440 = *(unsigned __int64 *)(v_stack_m3F8);
        v_stack_m518 = 16;
    }
    result = DecodeProviderTraits(v_stack_m3F0, a2, v_stack_m4D0, v_stack_m400);
    v_stack_m410 = *(unsigned __int64 *)(gs_base + (0 + 392));
    v_rbx = (unsigned __int16)(~(a4));
    goto loc_00AF31E5;
loc_00AF31D9:
    goto loc_00AF31EC;
loc_00AF31DF:
loc_00AF31E5:
loc_00AF31EC:
    v_stack_m4E0 = a2;
    if (*(unsigned __int64 *)(v_stack_m3F8) == 0) goto loc_00AF4662;
    result = 0;
    v_stack_m3D0 = v_xmm0;
    v_stack_m3C0 = 0;
    v_stack_m470 = 0;
    v_stack_m508 = 80;
    v_stack_m4C8 = 0;
    v_stack_m4DC = 0;
    v_stack_m450 = 0;
    v_stack_m3E8 = 0;
    v_stack_m500 = 0;
    v_stack_m504 = 0;
    v_stack_m4D8 = v_r14 + 1;
    v_stack_m488 = v_r14 + 1;
    v_stack_m4B8 = 0;
    a1 = (unsigned __int16)((v_stack_m510) - ((unsigned __int16)(v_r14 + 1)));
    v_r13 = (a2 + 4) << (5);
    v_r13 = (v_r13) + (v_r11);
    if (v_stack_m4A8 == 0) goto loc_00AF3292;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_r13 + 6)))) >> (5));
    result = (unsigned int)((*(unsigned __int16 *)(v_r13 + 6)) & (0x8000001FULL));
    if (!(condition_is_greater_or_equal)) {
        result = (unsigned int)((result) - ((unsigned int)(v_r14 + 1)));
        result = (unsigned int)((result) | (0xFFFFFFE0ULL));
        result = (unsigned int)((result) + ((unsigned int)(v_r14 + 1)));
    }
    if (condition_is_below) goto loc_00AF31D9;
loc_00AF3292:
    result = EtwpLevelKeywordEnabled(v_r13, a8, a9, (unsigned int)(a2));
    if ((unsigned __int8)(result) == 0) goto loc_00AF31D9;
    if (((a5) & (2)) != 0) goto loc_00AF32D1;
    if ((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 496)) >= 0) goto loc_00AF32DF;
loc_00AF32D1:
    if (((*(unsigned int *)(v_r13 + 8)) & (512)) != 0) goto loc_00AF31D9;
loc_00AF32DF:
    if (*(unsigned __int64 *)(v_r11 + 640) == 0) goto loc_00AF3312;
    result = (*(unsigned __int64 *)(gs_base + (0 + 392))) * ((unsigned int)(a2));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + *(unsigned __int64 *)(v_r11 + 640) * 1))))) & ((unsigned int)((unsigned int)(0x80000200ULL))));
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0x80000200ULL)))) goto loc_00AF330D;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(result + *(unsigned __int64 *)(v_r11 + 640) * 1))) & ((unsigned int)((unsigned int)(0x80000100ULL))));
    if (((unsigned int)(a1)) != ((unsigned int)((unsigned int)(0x80000100ULL)))) goto loc_00AF3312;
loc_00AF330D:
    goto loc_00AF3315;
loc_00AF3312:
loc_00AF3315:
    if (0 == 0) goto loc_00AF3351;
    v_stack_m550 = a11;
    v_stack_m558 = (unsigned int)((unsigned int)(a10));
    result = EtwpApplyEventIdPayloadFilterOnUserEvent(v_r11, (unsigned int)((unsigned int)((unsigned int)(v_stack_m4E0))), v_stack_m4C4, v_stack_m490);
    if ((unsigned __int8)(result) == 0) goto loc_00AF345D;
    goto loc_00AF3355;
loc_00AF3351:
loc_00AF3355:
    if (v_stack_m4CC == 0) goto loc_00AF33B4;
    v_stack_m550 = 0;
    v_stack_m558 = a9;
    a3 = 0;
    result = EtwpIsEventNameFilterEnabled(v_stack_m4B0, (unsigned int)((unsigned int)((unsigned int)(v_stack_m4E0))), a3, a8);
    if ((unsigned __int8)(result) == 0) goto loc_00AF33B4;
    v_stack_m538 = 0;
    v_stack_m540 = a9;
    v_stack_m548 = a8;
    v_stack_m550 = 0;
    v_stack_m558 = (unsigned __int8)(v_r14 + 1);
    result = EtwpApplyEventNameFilter(v_stack_m4B0, (unsigned int)((unsigned int)((unsigned int)(v_stack_m4E0))), (unsigned int)((unsigned int)((unsigned int)(a10))), v_stack_m4F0);
    if ((unsigned __int8)(result) == 0) goto loc_00AF345D;
loc_00AF33B4:
    v_stack_m4F4 = (unsigned int)(*(unsigned __int16 *)(v_r13 + 6));
    v_stack_m4A0 = (unsigned int)(*(unsigned __int16 *)(v_r13 + 6));
    result = ExAcquireRundownProtectionCacheAwareEx(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m4E8 + 704) + *(unsigned __int16 *)(v_r13 + 6) * 8), (unsigned int)((unsigned int)(v_r14 + 1)), (unsigned int)((unsigned int)((unsigned int)(a10))), v_stack_m4F0);
    if ((unsigned __int8)(result) == 0) goto loc_00AF3416;
    if (((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_r13 + 6))))) >= (*(unsigned int *)(v_stack_m4E8 + 16))) goto loc_00AF33FF;
    v_stack_m4D8 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m4E8 + 712) + (unsigned int)((unsigned int)(*(unsigned __int16 *)(v_r13 + 6))) * 8);
    v_stack_m488 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m4E8 + 712) + (unsigned int)((unsigned int)(*(unsigned __int16 *)(v_r13 + 6))) * 8);
    goto loc_00AF340A;
loc_00AF33FF:
    v_stack_m4D8 = v_r14 + 1;
    v_stack_m488 = v_r14 + 1;
loc_00AF340A:
    v_stack_m500 = (unsigned int)((unsigned __int8)(v_r14 + 1));
    v_stack_m504 = (unsigned __int8)(v_r14 + 1);
    goto loc_00AF3419;
loc_00AF3416:
loc_00AF3419:
    if ((((unsigned __int8)(v_r14 + 1)) & ((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m4E8 + 712) + (unsigned int)((unsigned int)(*(unsigned __int16 *)(v_r13 + 6))) * 8)))) == 0) goto loc_00AF3489;
    result = *(unsigned __int64 *)(v_stack_m4E8 + 712);
    v_rdi = (unsigned int)(v_stack_m500);
    if ((unsigned __int8)((unsigned int)(v_stack_m500)) != 0) {
        a1 = *(unsigned __int64 *)(v_stack_m4E8 + 704);
        a2 = (unsigned int)(v_r14 + 1);
        a1 = *(unsigned __int64 *)(a1 + (unsigned int)((unsigned int)(*(unsigned __int16 *)(v_r13 + 6))) * 8);
        result = ExReleaseRundownProtectionCacheAwareEx(a1, a2, (unsigned int)((unsigned int)((unsigned int)(a10))), v_stack_m4F0);
        result = Feature_1345841464__private_IsEnabledDeviceUsageNoInline(a1, a2, (unsigned int)((unsigned int)((unsigned int)(a10))), v_stack_m4F0);
        v_rdi = (unsigned __int8)((unsigned int)(v_stack_m500));
        if ((unsigned int)(result) != 0) { v_rdi = 0; }
        v_stack_m500 = (unsigned int)(v_rdi);
    }
    if (((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_r13 + 6))))) == 3) goto loc_00AF3466;
loc_00AF345D:
    goto loc_00AF45FB;
loc_00AF3466:
    result = (unsigned int)(-((unsigned int)(*(unsigned int *)(v_stack_m4E8 + 4340))));
    a1 = (unsigned int)((a1) & (758));
    a1 = (unsigned int)((a1) + (0xC0000008ULL));
    v_stack_m4FC = (unsigned int)(a1);
loc_00AF3480:
    goto loc_00AF4662;
loc_00AF3489:
    if (a7 == 0) goto loc_00AF34A5;
    v_stack_m508 = 104;
    goto loc_00AF34A9;
loc_00AF34A5:
loc_00AF34A9:
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m4E8 + 8)))) & (0xFFFFFF9FULL)) == 0) goto loc_00AF3759;
    if (condition_is_above_or_equal) goto loc_00AF34EC;
    if (v_stack_m428 == 0) goto loc_00AF34EC;
    v_r15 = (unsigned int)(v_stack_m508);
    if (v_stack_m428 != (*(unsigned __int64 *)(v_rip + 5060054))) {
        result = *(unsigned __int16 *)(v_stack_m428 + 4496);
        result = (unsigned int)((result) + (15));
        result = (unsigned int)((result) & (0xFFFFFFF8ULL));
        v_r15 = (unsigned int)(((unsigned int)(v_stack_m508)) + ((unsigned int)(result)));
        v_stack_m508 = (unsigned int)(v_r15);
    }
    if ((((unsigned __int8)(v_r14 + 1)) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m4E8 + 8))))) == 0) goto loc_00AF351C;
    if (((v_stack_m518) & (2)) == 0) {
        a1 = v_stack_mA8;
        result = EtwpGetSidExtendedHeaderItem(a1, v_stack_m428, (unsigned int)((unsigned int)((unsigned int)(a10))), v_stack_m4F0);
        a1 = *(unsigned int *)(v_stack_m4E8 + 8);
    }
    v_rdi = (unsigned int)((104 - 88) | (2));
    v_r15 = (unsigned int)((v_r15) + ((unsigned int)(v_stack_mA8)));
    v_stack_m508 = (unsigned int)(v_r15);
loc_00AF351C:
    if ((((unsigned __int8)(a1)) & (2)) != 0) {
        v_rdi = (unsigned int)((v_rdi) | ((unsigned int)(v_r14 + 1)));
        v_r15 = (unsigned int)((v_r15) + (16));
        v_stack_m508 = (unsigned int)(v_r15);
    }
    if (sign_flag) {
        v_rdi = (unsigned int)((v_rdi) | (64));
        v_r15 = (unsigned int)((v_r15) + (16));
        v_stack_m508 = (unsigned int)(v_r15);
    }
    if (!(condition_is_above_or_equal)) {
        v_r15 = (unsigned int)((v_r15) + (16));
        v_stack_m508 = (unsigned int)(v_r15);
    }
    if (((4) & ((unsigned __int8)(a1))) == 0) goto loc_00AF36DE;
    if (*(unsigned __int64 *)(v_stack_m4B0 + 640) == 0) goto loc_00AF359F;
    a1 = (a1) * ((unsigned int)((unsigned int)(v_stack_m4F0)));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + *(unsigned __int64 *)(v_stack_m4B0 + 640) * 1))))) & ((unsigned int)((unsigned int)(0x80001000ULL))));
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0x80001000ULL)))) goto loc_00AF359A;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + *(unsigned __int64 *)(v_stack_m4B0 + 640) * 1))))) & ((unsigned int)((unsigned int)(0x80002000ULL))));
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0x80002000ULL)))) goto loc_00AF359A;
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + *(unsigned __int64 *)(v_stack_m4B0 + 640) * 1))) & ((unsigned int)((unsigned int)(0x80004000ULL))));
    if (a2 != ((unsigned int)((unsigned int)(0x80004000ULL)))) goto loc_00AF359F;
loc_00AF359A:
    goto loc_00AF35A2;
loc_00AF359F:
loc_00AF35A2:
    if (0 == 0) goto loc_00AF362D;
    v_stack_m558 = (unsigned __int8)(v_r14 + 1);
    result = EtwpApplyLevelKwFilter(v_stack_m4B0, (unsigned int)((unsigned int)(v_stack_m4F0)), a8, a9);
    if ((unsigned __int8)(result) == 0) goto loc_00AF36D9;
    result = EtwpApplyStackWalkFilterOnUserEvent(v_stack_m490, v_stack_m4B0, (unsigned int)((unsigned int)(v_stack_m4F0)), a9);
    if ((unsigned __int8)(result) == 0) goto loc_00AF36D9;
    v_stack_m538 = (unsigned __int8)(v_r14 + 1);
    v_stack_m540 = a9;
    v_stack_m548 = a8;
    v_stack_m550 = 0;
    v_stack_m558 = (unsigned __int8)(v_r14 + 1);
    result = EtwpApplyEventNameFilter(v_stack_m4B0, (unsigned int)((unsigned int)(v_stack_m4F0)), (unsigned int)(a10), v_stack_m4F0);
    if ((unsigned __int8)(result) == 0) goto loc_00AF36D9;
loc_00AF362D:
    if ((((unsigned __int8)(v_r14 + 1)) & ((unsigned __int8)(v_stack_m518))) != 0) goto loc_00AF3698;
    result = EtwpGetStackLookasideListEntry(v_stack_m4B0, (unsigned int)((unsigned int)(v_stack_m4F0)), (unsigned int)(a10), v_stack_m4F0);
    v_stack_m418 = result;
    if (result == 0) goto loc_00AF3694;
    v_rbx = (unsigned __int8)((v_stack_m518) | (8));
    v_stack_m518 = (unsigned __int8)(v_rbx);
    v_stack_m478 = result + 32;
    v_stack_m550 = 0;
    v_stack_m558 = 0;
    a3 = 0;
    result = EtwpGetStackExtendedHeaderItem(v_stack_m4D8, v_stack_m410, a3, result);
    if ((unsigned __int8)(result) == 0) {
        a1 = v_stack_m418;
        result = EtwpReleaseStackLookasideListEntry(a1, v_stack_m410, a3, result);
        v_rbx = (unsigned __int8)((v_rbx) & (247));
        v_stack_m518 = (unsigned __int8)(v_rbx);
        v_stack_m478 = 0;
    }
loc_00AF3698:
    if (v_stack_m478 == 0) goto loc_00AF36D9;
    if ((((unsigned __int8)(v_r14 + 1)) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m4D8 + 820))))) == 0) goto loc_00AF36CC;
    result = EtwpGetCrimsonStackKey(v_stack_m4D8, v_stack_m478, v_stack_m4B8, result);
    if ((unsigned __int8)(result) == 0) goto loc_00AF36CC;
    v_rdi = (unsigned int)((v_rdi) | (8));
    v_r15 = (unsigned int)((v_r15) + (24));
    goto loc_00AF36D5;
loc_00AF36CC:
    v_rdi = (unsigned int)((v_rdi) | (4));
    v_r15 = (unsigned int)((v_r15) + ((unsigned int)(*(unsigned __int16 *)(v_stack_m478))));
loc_00AF36D5:
    v_stack_m508 = (unsigned int)(v_r15);
loc_00AF36D9:
loc_00AF36DE:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m4E8 + 8)))) & (8)) == 0) goto loc_00AF3759;
    if (((v_stack_m518) & (4)) != 0) goto loc_00AF3740;
    v_stack_m408 = 0;
    v_stack_m460 = 0;
    result = IoGetStackLimits(v_stack_m460, v_stack_m408, v_stack_m4B8, result);
    result = (v_stack_m408) - (v_stack_m460);
    if (result >= = 480) {
        result = v_stack_m578;
        v_rsp = (v_rsp) - (480);
        a1 = v_stack_m518;
        v_stack_m438 = a1;
        result = *(unsigned int *)(a1);
        result = EtwpGetPsmKeyExtendedHeaderItem(a1, v_stack_m408, v_stack_m4B8, result);
    }
loc_00AF3740:
    result = v_stack_m438;
    if (v_stack_m438 != 0) {
        v_rdi = (unsigned int)((v_rdi) | (32));
        result = *(unsigned __int16 *)(v_stack_m438);
        v_r15 = (unsigned int)((v_r15) + ((unsigned int)(result)));
        v_stack_m508 = (unsigned int)(v_r15);
    }
    a1 = ((unsigned int)(v_stack_mB8) + (unsigned int)(v_stack_mB8) * 2) << (4);
    v_stack_m498 = a1;
    if ((unsigned int)((unsigned int)(a10)) == 0) goto loc_00AF3A25;
    v_stack_m448 = 0;
    v_stack_m503 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == 0) goto loc_00AF37D1;
    result = ((unsigned int)((unsigned int)((unsigned int)(a10)))) << (4);
    if (result == 0) goto loc_00AF37D1;
    if (((3) & ((unsigned __int8)(v_stack_m4F0))) != 0) goto loc_00AF47A1;
    if ((v_stack_m4F0 + result * 1) > result) goto loc_00AF37CF;
    if ((v_stack_m4F0 + result * 1) < v_stack_m4F0) {
        result = *(unsigned __int8 *)(result);
    }
    v_stack_m448 = 0;
loc_00AF37DF:
    if (0 >= ((unsigned int)((unsigned int)(a10)))) goto loc_00AF398D;
    a2 = (0) << (4);
    a2 = (a2) + (v_stack_m4F0);
    v_stack_m430 = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 8)));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 8)))) <= 0xFFFFULL) goto loc_00AF3875;
    v_stack_m4FC = 0x80000005ULL;
    v_stack_m510 = (unsigned __int16)(v_stack_m510);
    result = Feature_1345841464__private_IsEnabledDeviceUsageNoInline(v_stack_m510, a2, v_stack_m4F0, 3);
    if ((unsigned int)(result) != 0) goto loc_00AF385C;
    if (v_stack_m4B8 != 0) {
        result = v_stack_m4D8;
        a2 = *(unsigned __int64 *)(result + 1056);
        a1 = v_stack_m4B8;
        result = EtwpDereferenceStackEntry(a1, a2, v_stack_m4F0, 3);
    }
    result = ExReleaseRundownProtectionCacheAwareEx(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m4E8 + 704) + (unsigned int)(v_stack_m4F4) * 8), (unsigned int)((unsigned int)(v_r14 + 1)), (unsigned int)(v_stack_m4F4), 3);
    goto loc_00AF3860;
loc_00AF385C:
loc_00AF3860:
    goto loc_00AF466A;
loc_00AF3875:
    if (v_stack_m4CC != 0) goto loc_00AF3881;
    goto loc_00AF388A;
loc_00AF3881:
loc_00AF388A:
    if ((unsigned __int8)(*(unsigned __int8 *)((unsigned int)((unsigned int)(v_r14 + 1)) + 12)) == 0) goto loc_00AF38EF;
    a1 = (unsigned int)(((unsigned __int8)(*(unsigned __int8 *)((unsigned int)((unsigned int)(v_r14 + 1)) + 12))) - (1));
    if (condition_is_equal) goto loc_00AF38CC;
    if (((unsigned int)(a1)) != 3) goto loc_00AF38E9;
    if (((unsigned int)((unsigned int)(v_stack_m430))) != 16) goto loc_00AF38E9;
    v_stack_m503 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == 0) goto loc_00AF38C0;
    result = RtlReadULong64FromUser((unsigned int)((unsigned int)(v_r14 + 1)), (unsigned int)((unsigned int)(v_r14 + 1)), (unsigned int)(v_stack_m4F4), 3);
    goto loc_00AF38C3;
loc_00AF38C0:
loc_00AF38C3:
    v_stack_m480 = *(unsigned __int64 *)((unsigned int)((unsigned int)(v_r14 + 1)));
    goto loc_00AF38E9;
loc_00AF38CC:
    result = Feature_1345841464__private_IsEnabledDeviceUsageNoInline((unsigned int)((unsigned int)(v_r14 + 1)), (unsigned int)((unsigned int)(v_r14 + 1)), (unsigned int)(v_stack_m4F4), 3);
    v_stack_m460 = (unsigned int)(result);
    if ((unsigned int)(result) == 0) goto loc_00AF38E0;
    goto loc_00AF38E6;
loc_00AF38E0:
loc_00AF38E6:
loc_00AF38E9:
    goto loc_00AF38FA;
loc_00AF38EF:
    v_r15 = (unsigned int)(((unsigned int)(v_stack_m508)) + ((unsigned int)((unsigned int)(v_stack_m430))));
    v_stack_m508 = (unsigned int)(v_r15);
loc_00AF38FA:
    if (((unsigned int)(v_r15)) >= ((unsigned int)(v_stack_m4E8))) goto loc_00AF396E;
    v_stack_m4FC = 0x80000005ULL;
    v_stack_m510 = (unsigned __int16)(v_stack_m510);
    result = Feature_1345841464__private_IsEnabledDeviceUsageNoInline(v_stack_m510, (unsigned int)((unsigned int)(v_r14 + 1)), (unsigned int)(v_stack_m4F4), 3);
    if ((unsigned int)(result) != 0) goto loc_00AF3955;
    if (v_stack_m4B8 != 0) {
        result = v_stack_m4D8;
        a2 = *(unsigned __int64 *)(result + 1056);
        a1 = v_stack_m4B8;
        result = EtwpDereferenceStackEntry(a1, a2, (unsigned int)(v_stack_m4F4), 3);
    }
    result = ExReleaseRundownProtectionCacheAwareEx(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m4E8 + 704) + (unsigned int)(v_stack_m4F4) * 8), (unsigned int)((unsigned int)((unsigned int)(v_stack_m500))), (unsigned int)(v_stack_m4F4), 3);
    goto loc_00AF3959;
loc_00AF3955:
loc_00AF3959:
    goto loc_00AF466A;
loc_00AF396E:
    v_r12 = (unsigned int)((v_stack_m4F0) + ((unsigned int)((unsigned int)(v_stack_m500))));
    v_stack_m448 = (unsigned int)(v_r12);
    goto loc_00AF37DF;
loc_00AF398D:
    goto loc_00AF3A25;
loc_00AF3A25:
    if (v_stack_m4DC == 0) goto loc_00AF3A82;
    result = Feature_1345841464__private_IsEnabledDeviceUsageNoInline(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m4E8 + 704) + (unsigned int)(v_stack_m4F4) * 8), (unsigned int)(a10), v_stack_m4F0, 3);
    if ((unsigned int)(result) == 0) goto loc_00AF3A73;
    result = (unsigned int)(((unsigned int)(v_stack_m4C8)) + (15));
    result = (unsigned int)((result) & ((unsigned int)((unsigned int)(0xFFFFFFF8ULL))));
    if (((unsigned int)(result)) <= 0xFFFFULL) goto loc_00AF3A79;
loc_00AF3A4A:
    result = (unsigned int)(v_stack_m4FC);
    if (!sign_flag) { result = (unsigned int)((unsigned int)(0xC0000095ULL)); }
    v_stack_m4FC = (unsigned int)(result);
    v_stack_m510 = (unsigned __int16)(v_stack_m510);
    goto loc_00AF3480;
loc_00AF3A73:
    result = (unsigned int)((v_stack_m510) + (15));
    result = (unsigned int)((result) & ((unsigned int)(v_stack_m4E8)));
loc_00AF3A79:
    v_r15 = (unsigned int)((v_stack_m4D8) + ((unsigned int)(result)));
    v_stack_m508 = (unsigned int)(v_r15);
    goto loc_00AF3A88;
loc_00AF3A82:
loc_00AF3A88:
    if ((unsigned __int16)(v_stack_m4D0) == 0) goto loc_00AF3AB3;
    result = Feature_1345841464__private_IsEnabledDeviceUsageNoInline((unsigned int)(0xC0000095ULL), (unsigned int)(a10), v_stack_m4F0, 3);
    if ((unsigned int)(result) == 0) goto loc_00AF3AA9;
    result = (unsigned int)((v_stack_m4D0 + 15) & ((unsigned int)((unsigned int)(0xFFFFFFF8ULL))));
    if (((unsigned int)(result)) <= 0xFFFFULL) goto loc_00AF3AAC;
    goto loc_00AF3A4A;
loc_00AF3AA9:
    result = (unsigned int)((result) & ((unsigned int)((unsigned int)(0xFFFFFFF8ULL))));
loc_00AF3AAC:
    v_r15 = (unsigned int)((v_r15) + ((unsigned int)(result)));
    v_stack_m508 = (unsigned int)(v_r15);
loc_00AF3AB3:
    *(unsigned int *)(v_stack_m518 + v_stack_m498 * 1 + 392) = (unsigned int)(v_r15);
    v_stack_m558 = 0;
    result = EtwpReserveTraceBuffer(v_stack_m4D8, (unsigned int)((unsigned int)(v_r15)), v_stack_m3D0, v_stack_m470);
    v_stack_m460 = result;
    v_rbx = v_stack_m4B8;
    if (v_stack_m4B8 != 0) {
        result = v_stack_m4D8;
        a2 = *(unsigned __int64 *)(result + 1056);
        a1 = v_stack_m4B8;
        result = EtwpDereferenceStackEntry(a1, a2, v_stack_m3D0, v_stack_m470);
        result = Feature_1345841464__private_IsEnabledDeviceUsageNoInline(a1, a2, v_stack_m3D0, v_stack_m470);
        v_rbx = v_stack_m4B8;
        if ((unsigned int)(result) != 0) { v_rbx = 0; }
        v_stack_m4B8 = v_rbx;
    }
    if (result != 0) goto loc_00AF3C04;
    result = EtwpGetReserveTraceBufferStatus(v_stack_m4D8, (unsigned int)((unsigned int)(v_r15)), v_stack_m3D0, v_stack_m470);
    v_rdi = 0;
    v_r12 = 0;
    if (v_stack_m4DC >= = 0) {
        v_rdi = a10;
        v_r12 = v_stack_m4F0;
    }
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 4242668), v_rip - 11406093, v_stack_m3D0, v_stack_m470);
    if ((unsigned __int8)(result) != 0) {
        a3 = v_stack_m4D8 + 136;
        a2 = v_stack_m490;
        a2 = (a2) + (40);
        a1 = v_stack_m468;
        a1 = (a1) + (40);
        v_stack_m538 = (unsigned __int8)((unsigned int)(v_stack_m500));
        v_stack_m540 = (unsigned __int8)((unsigned int)(v_stack_m500));
        v_stack_m548 = v_r12;
        v_stack_m550 = (unsigned int)(v_rdi);
        v_stack_m558 = (unsigned int)((unsigned int)((unsigned int)(result)));
        a4 = a5;
        result = EtwpTraceLostEvent(a1, a2, a3, a4);
    }
    if (!(sign_flag)) {
        a1 = (unsigned int)(v_stack_m4FC);
        if (((*(unsigned int *)(v_stack_m4D8 + 12)) & (0x8000000ULL)) == 0) { a1 = (unsigned int)((unsigned int)((unsigned int)(result))); }
        v_stack_m4FC = (unsigned int)(a1);
    }
    result = ExReleaseRundownProtectionCacheAwareEx(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m4E8 + 704) + (unsigned int)(v_stack_m4F4) * 8), (unsigned int)((unsigned int)((unsigned int)(v_stack_m500))), (unsigned int)(v_stack_m4F4), a4);
    result = Feature_1345841464__private_IsEnabledDeviceUsageNoInline(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m4E8 + 704) + (unsigned int)(v_stack_m4F4) * 8), (unsigned int)((unsigned int)((unsigned int)(v_stack_m500))), (unsigned int)(v_stack_m4F4), a4);
    a1 = (unsigned __int8)((unsigned int)(v_stack_m500));
    if ((unsigned int)(result) != 0) { a1 = 0; }
    v_stack_m500 = (unsigned int)(a1);
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != ((unsigned int)((unsigned int)(0xC0000095ULL)))) goto loc_00AF31DF;
    v_stack_m4FC = (unsigned int)((unsigned int)(0xC0000095ULL));
    goto loc_00AF3480;
loc_00AF3C04:
    *(unsigned __int64 *)(v_stack_m518 + v_stack_m4F0 * 1 + 352) = v_stack_m4D8;
    *(unsigned __int64 *)(v_stack_m518 + v_stack_m4F0 * 1 + 360) = v_stack_m4E8;
    *(unsigned __int64 *)(v_stack_m518 + v_stack_m4F0 * 1 + 368) = v_xmm0;
    *(unsigned __int64 *)(v_stack_m518 + v_stack_m4F0 * 1 + 384) = v_xmm0;
    result = Feature_1345841464__private_IsEnabledDeviceUsageNoInline(a1, (unsigned int)((unsigned int)((unsigned int)(v_stack_m500))), v_stack_m4A8, (unsigned int)(0xC0000095ULL));
    a1 = (unsigned __int8)((unsigned int)(v_stack_m500));
    if ((unsigned int)(result) != 0) { a1 = 0; }
    v_stack_m500 = (unsigned int)(a1);
    v_stack_m504 = (unsigned __int8)(a1);
    v_stack_m458 = 0;
    v_stack_m4F8 = 80;
    v_stack_m4C0 = 0;
    *(unsigned __int64 *)(v_stack_m4E8) = v_xmm0;
    *(unsigned __int64 *)(v_stack_m4E8 + 16) = v_xmm1;
    *(unsigned __int64 *)(v_stack_m4E8 + 32) = v_xmm0;
    *(unsigned __int64 *)(v_stack_m4E8 + 48) = v_xmm1;
    *(unsigned __int64 *)(v_stack_m4E8 + 64) = v_xmm0;
    if (v_stack_m400 != 0) goto loc_00AF3CCB;
    if (v_stack_m480 != 0) goto loc_00AF3CD8;
    *(unsigned __int64 *)(v_stack_m4E8 + 24) = v_xmm0;
    goto loc_00AF3D77;
loc_00AF3CCB:
    if (v_stack_m480 == 0) goto loc_00AF3D5F;
loc_00AF3CD8:
    v_stack_m503 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == 0) goto loc_00AF3D17;
    if ((((unsigned __int8)(v_stack_m480)) & (3)) != 0) goto loc_00AF47A7;
    if ((v_stack_m480 + 16) > ((unsigned int)((unsigned int)((unsigned int)(v_stack_m500))))) goto loc_00AF3D15;
    result = v_stack_m480;
    if ((v_stack_m480 + 16) < v_stack_m480) {
        result = *(unsigned __int8 *)((unsigned int)((unsigned int)((unsigned int)(v_stack_m500))));
    }
    v_stack_m503 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == 0) goto loc_00AF3D45;
    result = RtlCopyFromUser(v_stack_m4E8 + 24, v_stack_m480, 16, (unsigned int)(0xC0000095ULL));
    goto loc_00AF3D4A;
loc_00AF3D45:
    result = RtlCopyVolatileMemory(v_stack_m4E8 + 24, v_stack_m480, 16, (unsigned int)(0xC0000095ULL));
loc_00AF3D4A:
    result = (unsigned __int16)((128) | (*(unsigned __int16 *)(v_stack_m4E8 + 4)));
    *(unsigned __int16 *)(v_stack_m4E8 + 4) = (unsigned __int16)(result);
    goto loc_00AF3D77;
loc_00AF3D5F:
    *(unsigned __int64 *)(v_stack_m4E8 + 24) = v_xmm0;
    result = (unsigned __int16)((128) | (*(unsigned __int16 *)(v_stack_m4E8 + 4)));
    *(unsigned __int16 *)(v_stack_m4E8 + 4) = (unsigned __int16)(result);
loc_00AF3D77:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m508)))) | (*(unsigned int *)(v_rip - 11254298 + v_stack_m4C4 * 4)));
    *(unsigned int *)(v_stack_m4E8) = (unsigned int)(result);
    if (((v_stack_p70) & ((unsigned __int16)((unsigned int)(0x400ULL)))) != 0) {
    }
    if ((unsigned int)(v_rdi) == 0) goto loc_00AF41F3;
    result = (unsigned int)(0x400ULL);
    v_rbx = 80;
    v_rsi = (unsigned int)(v_stack_m500);
    v_r12 = 0;
    if (!(condition_is_above_or_equal)) {
        v_r12 = v_stack_m4E8 + 80;
        a1 = v_stack_m428;
        v_rsi = *(unsigned __int16 *)(a1 + 4496);
        v_rsi = (unsigned __int16)((v_rsi) + (15));
        result = 0xFFF8ULL;
        v_rsi = (unsigned __int16)((v_rsi) & ((unsigned __int16)(result)));
        *(unsigned __int16 *)(v_r12) = (unsigned __int16)(v_rsi);
        result = 16;
        *(unsigned __int16 *)(v_r12 + 2) = (unsigned __int16)(result);
        result = *(unsigned __int16 *)(a1 + 4496);
        *(unsigned __int16 *)(v_r12 + 6) = (unsigned __int16)(result);
        result = *(unsigned __int16 *)(v_r12 + 4);
        a2 = 0xFFFEULL;
        result = (unsigned __int16)((result) & ((unsigned __int16)(a2)));
        *(unsigned __int16 *)(v_r12 + 4) = (unsigned __int16)(result);
        *(unsigned __int16 *)(v_r12 + 4) = 0;
        a3 = *(unsigned __int16 *)(a1 + 4496);
        v_rsi = (unsigned __int16)((v_rsi) - (a3));
        v_rsi = (unsigned __int16)((v_rsi) - (8));
        v_rbx = v_r12 + 8;
        a2 = *(unsigned __int64 *)(a1 + 4488);
        a1 = v_rbx;
        result = memcpy(a1, a2, a3, (unsigned int)(0xC0000095ULL));
        a3 = (unsigned __int16)(v_rsi);
        a1 = v_stack_m428;
        a1 = *(unsigned __int16 *)(a1 + 4496);
        a1 = (a1) + (v_rbx);
        a2 = 0;
        result = memset(a1, a2, a3, (unsigned int)(0xC0000095ULL));
        v_rsi = 1;
        v_rbx = *(unsigned __int16 *)(v_r12);
        v_rbx = (unsigned int)((v_rbx) + (80));
        v_stack_m4F8 = (unsigned int)(v_rbx);
        v_stack_m4C0 = v_r12;
    }
    if (((16) & ((unsigned __int8)(v_rdi))) == 0) goto loc_00AF3ECD;
    *(unsigned int *)(v_rbx + v_stack_m4E8 * 1) = 0x10018ULL;
    *(unsigned __int16 *)(v_rbx + v_stack_m4E8 * 1 + 6) = 16;
    result = (unsigned __int16)((*(unsigned __int16 *)(v_rbx + v_stack_m4E8 * 1 + 4)) & ((unsigned __int16)((unsigned int)(0xFFFEULL))));
    *(unsigned __int16 *)(v_rbx + v_stack_m4E8 * 1 + 4) = (unsigned __int16)(result);
    *(unsigned __int16 *)(v_rbx + v_stack_m4E8 * 1 + 4) = 0;
    *(unsigned __int64 *)(v_rbx + v_stack_m4E8 * 1 + 8) = v_xmm0;
    result = (unsigned __int16)((*(unsigned __int16 *)(v_stack_m4E8 + 4)) | ((unsigned __int16)(v_rsi)));
    *(unsigned __int16 *)(v_stack_m4E8 + 4) = (unsigned __int16)(result);
    v_rbx = (unsigned int)((v_rbx) + (24));
    v_stack_m4F8 = (unsigned int)(v_rbx);
    if (v_r12 != 0) {
        result = *(unsigned __int16 *)(v_r12 + 4);
        result = (unsigned __int16)((result) | ((unsigned __int16)(v_rsi)));
        *(unsigned __int16 *)(v_r12 + 4) = (unsigned __int16)(result);
    }
    v_stack_m4C0 = v_rbx + v_stack_m4E8 * 1;
loc_00AF3ECD:
    if ((((unsigned __int8)(v_rdi)) & (2)) == 0) goto loc_00AF3F2E;
    result = ((unsigned int)((unsigned int)(v_rbx))) + (v_stack_m4E8);
    v_stack_m498 = result;
    result = memcpy(result, v_stack_mA8, v_stack_mA8, (unsigned int)(0xFFFEULL));
    result = (unsigned __int16)((*(unsigned __int16 *)(v_stack_m4E8 + 4)) | ((unsigned __int16)(v_rsi)));
    *(unsigned __int16 *)(v_stack_m4E8 + 4) = (unsigned __int16)(result);
    v_rbx = (unsigned int)((v_rbx) + ((unsigned int)(v_stack_mA8)));
    v_stack_m4F8 = (unsigned int)(v_rbx);
    result = v_stack_mA8;
    if (v_rbx + v_stack_m4E8 * 1 != 0) {
        result = *(unsigned __int16 *)(v_rbx + v_stack_m4E8 * 1 + 4);
        result = (unsigned __int16)((result) | ((unsigned __int16)(v_rsi)));
        *(unsigned __int16 *)(v_rbx + v_stack_m4E8 * 1 + 4) = (unsigned __int16)(result);
    }
    v_stack_m4C0 = v_stack_m498;
loc_00AF3F2E:
    if ((((unsigned __int8)(v_rsi)) & ((unsigned __int8)(v_rdi))) == 0) goto loc_00AF3F95;
    *(unsigned int *)(v_rbx + v_stack_m4E8 * 1) = 0x30010ULL;
    *(unsigned __int16 *)(v_rbx + v_stack_m4E8 * 1 + 6) = 4;
    result = (unsigned __int16)((*(unsigned __int16 *)(v_rbx + v_stack_m4E8 * 1 + 4)) & ((unsigned __int16)((unsigned int)(0xFFFEULL))));
    *(unsigned __int16 *)(v_rbx + v_stack_m4E8 * 1 + 4) = (unsigned __int16)(result);
    *(unsigned __int16 *)(v_rbx + v_stack_m4E8 * 1 + 4) = 0;
    result = PsGetCurrentProcessSessionId(v_rbx + v_stack_m4E8 * 1, (unsigned int)(0xFFFEULL), v_stack_mA8, (unsigned int)(0xFFFEULL));
    *(unsigned int *)(v_rbx + v_stack_m4E8 * 1 + 8) = (unsigned int)(result);
    result = (unsigned __int16)((*(unsigned __int16 *)(v_stack_m4E8 + 4)) | ((unsigned __int16)(v_rsi)));
    *(unsigned __int16 *)(v_stack_m4E8 + 4) = (unsigned __int16)(result);
    v_rbx = (unsigned int)((v_rbx) + (16));
    v_stack_m4F8 = (unsigned int)(v_rbx);
    if (v_stack_m498 != 0) {
        result = *(unsigned __int16 *)(v_stack_m498 + 4);
        result = (unsigned __int16)((result) | ((unsigned __int16)(v_rsi)));
        *(unsigned __int16 *)(v_stack_m498 + 4) = (unsigned __int16)(result);
    }
    v_stack_m4C0 = v_rbx + v_stack_m4E8 * 1;
loc_00AF3F95:
    if ((((unsigned __int8)(v_rdi)) & (64)) == 0) goto loc_00AF4017;
    *(unsigned int *)(v_rbx + v_stack_m4E8 * 1) = 0xD0010ULL;
    *(unsigned __int16 *)(v_rbx + v_stack_m4E8 * 1 + 6) = (unsigned __int16)(16 - 8);
    result = (unsigned __int16)((*(unsigned __int16 *)(v_rbx + v_stack_m4E8 * 1 + 4)) & ((unsigned __int16)((unsigned int)(0xFFFEULL))));
    *(unsigned __int16 *)(v_rbx + v_stack_m4E8 * 1 + 4) = (unsigned __int16)(result);
    *(unsigned __int16 *)(v_rbx + v_stack_m4E8 * 1 + 4) = 0;
    result = EtwpGetProcessStartKey(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), (unsigned int)(0xFFFEULL), v_rbx + v_stack_m4E8 * 1, (unsigned int)(0xFFFEULL));
    *(unsigned __int64 *)(v_rbx + v_stack_m4E8 * 1 + 8) = result;
    result = (unsigned __int16)((*(unsigned __int16 *)(v_stack_m4E8 + 4)) | ((unsigned __int16)(v_rsi)));
    *(unsigned __int16 *)(v_stack_m4E8 + 4) = (unsigned __int16)(result);
    v_rbx = (unsigned int)((v_rbx) + (16));
    v_stack_m4F8 = (unsigned int)(v_rbx);
    if (v_rbx + v_stack_m4E8 * 1 != 0) {
        result = *(unsigned __int16 *)(v_rbx + v_stack_m4E8 * 1 + 4);
        result = (unsigned __int16)((result) | ((unsigned __int16)(v_rsi)));
        *(unsigned __int16 *)(v_rbx + v_stack_m4E8 * 1 + 4) = (unsigned __int16)(result);
    }
    v_stack_m4C0 = v_rbx + v_stack_m4E8 * 1;
loc_00AF4017:
    if (!sign_flag) goto loc_00AF40B4;
    *(unsigned int *)(v_rbx + v_stack_m4E8 * 1) = 0xA0010ULL;
    *(unsigned __int16 *)(v_rbx + v_stack_m4E8 * 1 + 6) = 8;
    result = (unsigned __int16)((*(unsigned __int16 *)(v_rbx + v_stack_m4E8 * 1 + 4)) & ((unsigned __int16)((unsigned int)(0xFFFEULL))));
    *(unsigned __int16 *)(v_rbx + v_stack_m4E8 * 1 + 4) = (unsigned __int16)(result);
    *(unsigned __int16 *)(v_rbx + v_stack_m4E8 * 1 + 4) = 0;
    if (((v_stack_m518) & (16)) != 0) goto loc_00AF407B;
    result = EtwpCreateEventKey(v_stack_m440, (unsigned int)(0xFFFEULL), v_rbx + v_stack_m4E8 * 1, v_rbx + v_stack_m4E8 * 1);
    if (v_stack_m3F8 != 0) {
        result = v_stack_m440;
        *(unsigned __int64 *)(v_stack_m3F8) = result;
    }
    *(unsigned __int64 *)(v_rbx + v_stack_m4E8 * 1 + 8) = v_stack_m440;
    result = (unsigned __int16)((*(unsigned __int16 *)(v_stack_m4E8 + 4)) | ((unsigned __int16)(v_rsi)));
    *(unsigned __int16 *)(v_stack_m4E8 + 4) = (unsigned __int16)(result);
    v_rbx = (unsigned int)((v_rbx) + (16));
    v_stack_m4F8 = (unsigned int)(v_rbx);
    if (v_rbx + v_stack_m4E8 * 1 != 0) {
        result = *(unsigned __int16 *)(v_rbx + v_stack_m4E8 * 1 + 4);
        result = (unsigned __int16)((result) | ((unsigned __int16)(v_rsi)));
        *(unsigned __int16 *)(v_rbx + v_stack_m4E8 * 1 + 4) = (unsigned __int16)(result);
    }
    v_stack_m4C0 = v_rbx + v_stack_m4E8 * 1;
loc_00AF40B4:
    if (((4) & ((unsigned __int8)(v_rdi))) == 0) goto loc_00AF411D;
    result = ((unsigned int)((unsigned int)(v_rbx))) + (v_stack_m4E8);
    v_stack_m498 = result;
    result = memcpy(result, v_stack_m478, *(unsigned __int16 *)(v_stack_m478), v_rbx + v_stack_m4E8 * 1);
    result = (unsigned __int16)((*(unsigned __int16 *)(v_stack_m4E8 + 4)) | ((unsigned __int16)(v_rsi)));
    *(unsigned __int16 *)(v_stack_m4E8 + 4) = (unsigned __int16)(result);
    v_rbx = (unsigned int)((v_rbx) + ((unsigned int)(*(unsigned __int16 *)(v_stack_m478))));
    v_stack_m4F8 = (unsigned int)(v_rbx);
    result = *(unsigned __int16 *)(v_stack_m478);
    if (v_rbx + v_stack_m4E8 * 1 != 0) {
        result = *(unsigned __int16 *)(v_rbx + v_stack_m4E8 * 1 + 4);
        result = (unsigned __int16)((result) | ((unsigned __int16)(v_rsi)));
        *(unsigned __int16 *)(v_rbx + v_stack_m4E8 * 1 + 4) = (unsigned __int16)(result);
    }
    v_stack_m4C0 = v_stack_m498;
    goto loc_00AF4124;
loc_00AF411D:
loc_00AF4124:
    if (((8) & ((unsigned __int8)(v_rdi))) == 0) goto loc_00AF419B;
    a1 = ((unsigned int)((unsigned int)(v_rbx))) + (v_stack_m4E8);
    *(unsigned int *)(a1) = 0x120018ULL;
    *(unsigned __int16 *)(a1 + 6) = (unsigned __int16)(8 + 8);
    result = (unsigned __int16)((*(unsigned __int16 *)(a1 + 4)) & ((unsigned __int16)((unsigned int)(0xFFFEULL))));
    *(unsigned __int16 *)(a1 + 4) = (unsigned __int16)(result);
    *(unsigned __int16 *)(a1 + 4) = 0;
    *(unsigned __int64 *)(a1 + 16) = v_stack_m4B8;
    *(unsigned __int64 *)(a1 + 8) = *(unsigned __int64 *)(v_stack_m478 + 8);
    result = (unsigned __int16)((*(unsigned __int16 *)(v_stack_m4E8 + 4)) | ((unsigned __int16)(v_rsi)));
    *(unsigned __int16 *)(v_stack_m4E8 + 4) = (unsigned __int16)(result);
    v_rbx = (unsigned int)((v_rbx) + ((unsigned int)(8 + 16)));
    v_stack_m4F8 = (unsigned int)(v_rbx);
    if (v_stack_m498 != 0) {
        result = *(unsigned __int16 *)(v_stack_m498 + 4);
        result = (unsigned __int16)((result) | ((unsigned __int16)(v_rsi)));
        *(unsigned __int16 *)(v_stack_m498 + 4) = (unsigned __int16)(result);
    }
    v_stack_m4C0 = a1;
loc_00AF419B:
    if ((((unsigned __int8)(v_rdi)) & (32)) == 0) goto loc_00AF41F9;
    v_rdi = ((unsigned int)((unsigned int)(v_rbx))) + (v_stack_m4E8);
    result = memcpy(v_rdi, v_stack_m438, *(unsigned __int16 *)(v_stack_m438), (unsigned int)(0xFFFEULL));
    result = (unsigned __int16)((*(unsigned __int16 *)(v_stack_m4E8 + 4)) | ((unsigned __int16)(v_rsi)));
    *(unsigned __int16 *)(v_stack_m4E8 + 4) = (unsigned __int16)(result);
    v_rbx = (unsigned int)((v_rbx) + ((unsigned int)(*(unsigned __int16 *)(v_stack_m438))));
    v_stack_m4F8 = (unsigned int)(v_rbx);
    result = *(unsigned __int16 *)(v_stack_m438);
    if (a1 != 0) {
        result = *(unsigned __int16 *)(a1 + 4);
        result = (unsigned __int16)((result) | ((unsigned __int16)(v_rsi)));
        *(unsigned __int16 *)(a1 + 4) = (unsigned __int16)(result);
    }
    v_stack_m4C0 = v_rdi;
loc_00AF41F3:
loc_00AF41F9:
    if ((unsigned __int16)(v_stack_m4D0) == 0) goto loc_00AF42B5;
    a1 = ((unsigned int)((unsigned int)(v_rbx))) + (v_stack_m4E8);
    v_stack_m498 = a1;
    v_rsi = (unsigned int)((15) + ((unsigned int)(v_stack_m4D0)));
    v_rsi = (unsigned __int16)((v_rsi) & ((unsigned __int16)((unsigned int)(0xFFF8ULL))));
    *(unsigned __int16 *)(a1) = (unsigned __int16)(v_rsi);
    *(unsigned __int16 *)(a1 + 2) = 12;
    *(unsigned __int16 *)(a1 + 6) = (unsigned __int16)(v_stack_m4D0);
    result = (unsigned __int16)((*(unsigned __int16 *)(a1 + 4)) & ((unsigned __int16)((unsigned int)(0xFFFEULL))));
    *(unsigned __int16 *)(a1 + 4) = (unsigned __int16)(result);
    *(unsigned __int16 *)(a1 + 4) = 0;
    v_rsi = (unsigned __int16)((v_rsi) - ((unsigned __int16)(v_stack_m4D0)));
    v_rsi = (unsigned __int16)((v_rsi) - (8));
    result = memcpy(a1 + 8, v_stack_m3F0, (unsigned int)((unsigned int)(v_stack_m4D0)), (unsigned int)(0xFFFEULL));
    a2 = 0;
    result = memset((unsigned int)((unsigned int)(v_stack_m4D0)) + a1 + 8 * 1, a2, (unsigned __int16)(v_rsi), (unsigned int)(0xFFFEULL));
    result = (unsigned __int16)((*(unsigned __int16 *)(v_stack_m4E8 + 4)) | (1));
    *(unsigned __int16 *)(v_stack_m4E8 + 4) = (unsigned __int16)(result);
    v_rbx = (unsigned int)(((unsigned int)(v_stack_m4F8)) + ((unsigned int)(*(unsigned __int16 *)(v_stack_m498))));
    v_stack_m4F8 = (unsigned int)(v_rbx);
    result = *(unsigned __int16 *)(v_stack_m498);
    if (v_rdi != 0) {
        result = *(unsigned __int16 *)(v_rdi + 4);
        result = (unsigned __int16)((result) | (1));
        *(unsigned __int16 *)(v_rdi + 4) = (unsigned __int16)(result);
    }
    v_stack_m4C0 = v_stack_m498;
loc_00AF42B5:
    if (v_stack_m4DC == 0) goto loc_00AF435A;
    v_rbx = (v_rbx) + (v_stack_m4E8);
    a3 = (unsigned int)((15) + ((unsigned int)((unsigned int)(v_stack_m4C8))));
    a3 = (unsigned __int16)((a3) & ((unsigned __int16)((unsigned int)(0xFFF8ULL))));
    *(unsigned __int16 *)(v_rbx) = a3;
    *(unsigned __int16 *)(v_rbx + 2) = 11;
    *(unsigned __int16 *)(v_rbx + 6) = (unsigned __int16)((unsigned int)(v_stack_m4C8));
    result = (unsigned __int16)((*(unsigned __int16 *)(v_rbx + 4)) & ((unsigned __int16)((unsigned int)(0xFFFEULL))));
    *(unsigned __int16 *)(v_rbx + 4) = (unsigned __int16)(result);
    *(unsigned __int16 *)(v_rbx + 4) = 0;
    a3 = (unsigned __int16)((a3) - ((unsigned __int16)((unsigned int)(v_stack_m4C8))));
    a3 = (unsigned __int16)((a3) - (8));
    v_stack_m450 = v_rbx + 8;
    v_stack_m3E8 = v_rbx + 8 + (unsigned int)(v_stack_m4C8) * 1;
    a2 = 0;
    result = memset(v_rbx + 8 + (unsigned int)(v_stack_m4C8) * 1, a2, a3, v_rbx + 8 + (unsigned int)(v_stack_m4C8) * 1);
    result = (unsigned __int16)((*(unsigned __int16 *)(v_stack_m4E8 + 4)) | (1));
    *(unsigned __int16 *)(v_stack_m4E8 + 4) = (unsigned __int16)(result);
    v_rbx = (unsigned int)(((unsigned int)(v_stack_m4F8)) + ((unsigned int)(*(unsigned __int16 *)(v_rbx))));
    v_stack_m4F8 = (unsigned int)(v_rbx);
    result = *(unsigned __int16 *)(v_rbx);
    if (v_stack_m498 != 0) {
        result = *(unsigned __int16 *)(v_stack_m498 + 4);
        result = (unsigned __int16)((result) | (1));
        *(unsigned __int16 *)(v_stack_m498 + 4) = (unsigned __int16)(result);
    }
    v_stack_m458 = 0;
loc_00AF4364:
    if (0 >= ((unsigned int)((unsigned int)(a10)))) goto loc_00AF451A;
    result = (0) + (0);
    if (v_stack_m4CC != 0) goto loc_00AF4391;
    goto loc_00AF4399;
loc_00AF4391:
loc_00AF4399:
    if ((unsigned __int8)(*(unsigned __int8 *)(v_stack_m4F0 + 0 * 8 + 12)) == 0) goto loc_00AF4477;
    a1 = (unsigned int)(((unsigned __int8)(*(unsigned __int8 *)(v_stack_m4F0 + 0 * 8 + 12))) - (1));
    if (condition_is_equal) goto loc_00AF43E0;
    if (((unsigned int)(a1)) != 2) goto loc_00AF43DB;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m4F0 + result * 8 + 8)))) != 8) goto loc_00AF43DB;
    if ((*(unsigned __int64 *)(v_stack_m4F0 + result * 8) + 8) > a1) goto loc_00AF43CB;
    result = *(unsigned __int64 *)(v_stack_m4F0 + result * 8) + 8;
    v_r15 = (unsigned int)(v_stack_m508);
    if ((*(unsigned __int64 *)(v_stack_m4F0 + result * 8) + 8) < (*(unsigned __int64 *)(v_stack_m4F0 + result * 8))) {
        result = *(unsigned __int8 *)(a1);
        v_r15 = v_stack_m508;
    }
    v_stack_m470 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m4F0 + result * 8));
loc_00AF43DB:
    goto loc_00AF44D1;
loc_00AF43E0:
    if (v_stack_m450 == 0) goto loc_00AF4441;
    if (((unsigned int)(*(unsigned int *)(v_stack_m4F0 + result * 8 + 8)) + v_stack_m450 * 1) < v_stack_m450) goto loc_00AF4441;
    if (((unsigned int)(*(unsigned int *)(v_stack_m4F0 + result * 8 + 8)) + v_stack_m450 * 1) > v_stack_m3E8) goto loc_00AF4441;
    if (v_stack_m4DC == 0) goto loc_00AF4441;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m4F0 + result * 8 + 8))) == 0) goto loc_00AF4426;
    if (((unsigned int)(*(unsigned int *)(v_stack_m4F0 + result * 8 + 8)) + *(unsigned __int64 *)(v_stack_m4F0 + result * 8) * 1) > v_stack_m450) goto loc_00AF4420;
    result = (unsigned int)(*(unsigned int *)(v_stack_m4F0 + result * 8 + 8)) + *(unsigned __int64 *)(v_stack_m4F0 + result * 8) * 1;
    if (((unsigned int)(*(unsigned int *)(v_stack_m4F0 + result * 8 + 8)) + *(unsigned __int64 *)(v_stack_m4F0 + result * 8) * 1) < (*(unsigned __int64 *)(v_stack_m4F0 + result * 8))) {
        result = *(unsigned __int8 *)(v_stack_m450);
        v_r15 = v_stack_m508;
    }
    result = memcpy(v_stack_m450, *(unsigned __int64 *)(v_stack_m4F0 + result * 8), (unsigned int)(*(unsigned int *)(v_stack_m4F0 + result * 8 + 8)), v_rbx + 8 + (unsigned int)(v_stack_m4C8) * 1);
    goto loc_00AF43DB;
loc_00AF4441:
    v_stack_m4FC = 0xC0000004ULL;
    v_r15 = (unsigned int)((v_r15) | (0xC00D0000ULL));
    *(unsigned int *)(v_stack_m4E8) = (unsigned int)(v_r15);
    *(unsigned __int64 *)(v_stack_m4E8 + 16) = v_stack_m470;
    goto loc_00AF466A;
loc_00AF4477:
    a4 = ((unsigned int)((unsigned int)(v_rbx))) + (v_stack_m4E8);
    if (((unsigned int)(1 + v_rbx * 1)) < ((unsigned int)(v_rbx))) goto loc_00AF44E0;
    v_stack_m4F8 = (unsigned int)(1 + v_rbx * 1);
    if (((unsigned int)(1 + v_rbx * 1)) > ((unsigned int)(v_stack_m4D8))) goto loc_00AF44E4;
    v_stack_m503 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == 0) goto loc_00AF44C2;
    if (1 == 0) goto loc_00AF44C2;
    if ((*(unsigned __int64 *)(v_stack_m4F0 + result * 8) + 1 * 1) > (*(unsigned __int64 *)(gs_base + (0 + 392)))) goto loc_00AF44C0;
    result = *(unsigned __int64 *)(gs_base + (0 + 392));
    if ((*(unsigned __int64 *)(v_stack_m4F0 + result * 8) + 1 * 1) < (*(unsigned __int64 *)(v_stack_m4F0 + result * 8))) {
        result = *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)));
    }
    result = memcpy(a4, *(unsigned __int64 *)(v_stack_m4F0 + result * 8), 1, a4);
loc_00AF44D1:
    v_r12 = (unsigned int)((v_stack_m4F0) + ((unsigned int)((unsigned int)(v_stack_m500))));
    v_stack_m458 = (unsigned int)(v_r12);
    goto loc_00AF4364;
loc_00AF44E0:
loc_00AF44E4:
    v_stack_m4FC = 0xC0000004ULL;
    v_r15 = (unsigned int)(((unsigned int)(v_stack_m508)) | (0xC00D0000ULL));
    *(unsigned int *)(v_stack_m4E8) = (unsigned int)(v_r15);
    *(unsigned __int64 *)(v_stack_m4E8 + 16) = v_stack_m470;
    goto loc_00AF466A;
loc_00AF451A:
    result = v_stack_m470;
    if (v_stack_m4A8 != 0) {
        a1 = v_stack_m4F4;
        result = (unsigned int)(a1);
        result = (unsigned int)((result) >> (5));
        a2 = (unsigned int)(result);
        a1 = (unsigned int)((a1) & (31));
        result = *(unsigned int *)(v_stack_m4A8 + result * 4);
        *(unsigned int *)(v_stack_m4A8 + a2 * 4) = (unsigned int)(result);
    }
    *(unsigned __int64 *)(v_stack_m4E8 + 16) = v_stack_m470;
    *(unsigned int *)(v_stack_m4E8 + 56) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m410 + 652)));
    *(unsigned int *)(v_stack_m4E8 + 60) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m410 + 732)));
    *(unsigned int *)(v_stack_m4E8 + 8) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m410 + 1296)));
    *(unsigned int *)(v_stack_m4E8 + 12) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m410 + 1288)));
    if (((*(unsigned int *)(v_stack_m4D8 + 12)) & (0x80000ULL)) == 0) goto loc_00AF45B1;
    if ((*(unsigned __int8 *)(v_rip + 4534354)) != 0) goto loc_00AF4595;
    if ((*(unsigned __int8 *)(v_rip + 3237001)) == 0) goto loc_00AF459E;
loc_00AF4595:
    result = (unsigned int)(*(unsigned int *)(v_stack_m410 + 1288));
    if ((*(unsigned __int8 *)(v_rip + 4593431)) != 0) {
        a2 = v_stack_m3D0;
        a1 = v_stack_m4D8;
        result = EtwpSendTraceEvent(a1, a2, v_stack_m4A8, a4);
        a3 = v_stack_m4A8;
    }
    if ((*(unsigned __int64 *)(v_stack_m4D8 + 1568)) == 0) goto loc_00AF31EC;
    a3 = (v_stack_m468) + (40);
    result = EtwpInvokeEventCallback(v_stack_m4D8, v_stack_m3D0, a3, *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
loc_00AF45FB:
    goto loc_00AF31EC;
loc_00AF4662:
loc_00AF466A:
    result = Feature_1345841464__private_IsEnabledDeviceUsageNoInline(v_stack_m4D8, v_stack_m3D0, v_stack_m4A8, *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    if ((unsigned int)(result) == 0) goto loc_00AF46A5;
    if (v_stack_m4B8 != 0) {
        a2 = *(unsigned __int64 *)(v_stack_m4D8 + 1056);
        a1 = v_stack_m4B8;
        result = EtwpDereferenceStackEntry(a1, a2, v_stack_m4A8, *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    }
    if ((unsigned __int8)((unsigned int)(v_stack_m500)) != 0) {
        result = v_stack_m4F4;
        a1 = *(unsigned __int64 *)(v_stack_m4E8 + 704);
        a2 = 1;
        a1 = *(unsigned __int64 *)(a1 + result * 8);
        result = ExReleaseRundownProtectionCacheAwareEx(a1, a2, v_stack_m4A8, *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    }
    if (((v_stack_m518) & (8)) != 0) {
        a1 = v_stack_m418;
        result = EtwpReleaseStackLookasideListEntry(a1, a2, v_stack_m4A8, *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    }
    if (v_stack_m4FC < 0) goto loc_00AF4710;
    if (v_stack_mB8 <= 0) goto loc_00AF476E;
loc_00AF46CD:
    v_r11 = (0 + 0 * 2) + (0 + 0 * 2);
    result = EtwpReleaseTraceBuffer(v_stack_m518 + v_r11 * 8 + 368, a2, v_stack_m4A8, *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    result = ExReleaseRundownProtectionCacheAwareEx(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m4E8 + 704) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m518 + v_r11 * 8 + 352))) * 8), 1, v_stack_m4A8, *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    v_rbx = (unsigned int)((0) + 1);
    if (((unsigned int)(v_rbx)) < v_stack_mB8) goto loc_00AF46CD;
    goto loc_00AF476E;
loc_00AF4710:
    result = (v_stack_m490) + (40);
    v_stack_m520 = 1;
    v_stack_m528 = v_stack_m4F0;
    v_stack_m530 = (unsigned int)((unsigned int)(a10));
    v_stack_m538 = 1;
    v_stack_m540 = result;
    v_stack_m548 = (unsigned int)((unsigned int)(v_stack_m4FC));
    v_stack_m550 = (unsigned int)((unsigned int)((unsigned int)(v_rbx)));
    v_stack_m558 = (unsigned __int16)(v_stack_m510);
    result = EtwpFailLogging(a8, a9, v_stack_m468, v_stack_m3B8);
loc_00AF476E:
    result = KiLeaveCriticalRegionUnsafe(v_stack_m410, a9, v_stack_m468, v_stack_m3B8);
loc_00AF477D:
    a1 = (v_stack_m58) ^ (v_stack_m518);
    result = _security_check_cookie(a1, a9, v_stack_m468, v_stack_m3B8);
    return result;
loc_00AF47A1:
    result = ExRaiseDatatypeMisalignment(a1, a9, v_stack_m468, v_stack_m3B8);
loc_00AF47A7:
    result = ExRaiseDatatypeMisalignment(a1, a9, v_stack_m468, v_stack_m3B8);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t EtwpWriteUserEvent(void *Arg1, int32_t Arg2, uint16_t Arg3, int64_t Arg4, uint8_t Arg5, int64_t Arg6, void *Arg7, uint8_t Arg8, int64_t Arg9, uint32_t Arg10, int64_t Arg11, int64_t Arg12, int64_t Arg13, uint16_t Arg14, int64_t Arg15, int64_t Arg16)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg7 = (uint8_t *)Arg7;

    int64_t result;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m3B8;
    uint64_t v_stack_m3C0;
    uint64_t v_stack_m3D0;
    uint64_t v_stack_m3D8;
    uint64_t v_stack_m3E0;
    uint64_t v_stack_m3E8;
    uint64_t v_stack_m3F0;
    uint64_t v_stack_m3F8;
    uint64_t v_stack_m40;
    uint64_t v_stack_m400;
    uint64_t v_stack_m408;
    uint64_t v_stack_m410;
    uint64_t v_stack_m418;
    uint64_t v_stack_m420;
    uint64_t v_stack_m428;
    uint32_t v_stack_m430;
    uint64_t v_stack_m438;
    uint64_t v_stack_m440;
    uint32_t v_stack_m448;
    uint64_t v_stack_m450;
    uint32_t v_stack_m458;
    uint64_t v_stack_m460;
    uint64_t v_stack_m468;
    uint64_t v_stack_m470;
    uint64_t v_stack_m478;
    uint64_t v_stack_m480;
    uint64_t v_stack_m488;
    uint64_t v_stack_m490;
    uint64_t v_stack_m498;
    uint32_t v_stack_m4A0;
    uint64_t v_stack_m4A8;
    uint64_t v_stack_m4B0;
    uint64_t v_stack_m4B8;
    uint64_t v_stack_m4C0;
    uint16_t v_stack_m4C4;
    uint32_t v_stack_m4C8;
    uint16_t v_stack_m4CC;
    uint16_t v_stack_m4D0;
    uint64_t v_stack_m4D8;
    uint32_t v_stack_m4DC;
    uint32_t v_stack_m4E0;
    uint64_t v_stack_m4E8;
    uint64_t v_stack_m4F0;
    uint32_t v_stack_m4F4;
    uint32_t v_stack_m4F8;
    uint32_t v_stack_m4FC;
    uint32_t v_stack_m500;
    uint8_t v_stack_m503;
    uint8_t v_stack_m504;
    uint32_t v_stack_m508;
    uint16_t v_stack_m510;
    uint64_t v_stack_m518;
    uint8_t v_stack_m520;
    uint64_t v_stack_m528;
    uint32_t v_stack_m530;
    uint8_t v_stack_m538;
    uint64_t v_stack_m540;
    uint8_t v_stack_m548;
    uint64_t v_stack_m550;
    uint32_t v_stack_m558;
    uint32_t v_stack_m578;
    uint64_t v_stack_m58;
    uint64_t v_stack_mA8;
    uint32_t v_stack_mB8;
    uint16_t v_stack_p70;

    local_rsp = (local_rsp) - (0x538ULL);
    result = (*(uint64_t *)(v_rip + 0x317734)) ^ (v_stack_m518);
    v_stack_m58 = result;
    v_stack_m4C4 = Arg3;
    v_stack_m468 = Arg1;
    v_stack_m4B0 = Arg13;
    v_stack_m3E0 = Arg1;
    v_stack_m510 = (uint16_t)(Arg2);
    v_stack_m490 = Arg6;
    v_stack_m4F0 = Arg11;
    v_stack_m3D8 = Arg11;
    v_stack_m4A8 = Arg12;
    v_stack_m3F0 = Arg15;
    v_stack_m3F8 = Arg16;
    local_r14 = 0;
    v_stack_m4FC = 0;
    Arg2 = 0;
    result = memset(v_stack_m3B8, Arg2, 776, Arg4);
    v_stack_m4E0 = 0;
    Arg2 = 0;
    result = memset(v_stack_mA8, Arg2, local_r14 + 80, Arg4);
    v_stack_m478 = 0;
    v_stack_m418 = 0;
    v_stack_m438 = 0;
    v_stack_m4D0 = 0;
    v_stack_m400 = 0;
    v_stack_m480 = 0;
    v_stack_m440 = 0;
    result = PsGetCurrentServerSiloGlobals(v_stack_mA8, Arg2, local_r14 + 80, Arg4);
    v_stack_m428 = *(uint64_t *)(result + 0x340);
    result = (uint16_t)((Arg14) & (256));
    v_stack_m4CC = (uint16_t)(result);
    Arg2 = (uint16_t)((Arg14) >> (9));
    Arg2 = (uint8_t)((Arg2) & ((uint8_t)(local_r14 + 1)));
    v_stack_m500 = 0;
    v_stack_m4B8 = 0;
    v_stack_m4F4 = 0;
    if (Arg11 != 0) goto loc_00AF3142;
    if ((uint32_t)((uint32_t)(Arg10)) != 0) goto loc_00AF314E;
    if (Arg11 == 0) goto loc_00AF3146;
loc_00AF3142:
    if ((uint32_t)((uint32_t)(Arg10)) == 0) goto loc_00AF314E;
loc_00AF3146:
    if (((uint32_t)((uint32_t)(Arg10))) <= 128) goto loc_00AF3158;
loc_00AF314E:
    goto loc_00AF477D;
loc_00AF3158:
    local_r11 = v_stack_m4B0;
    if (v_stack_m4B0 == 0) { local_r11 = Arg1; }
    v_stack_m4B0 = local_r11;
    v_stack_m518 = 0;
    v_stack_m4E8 = *(uint64_t *)(arg1 + 0x288);
    v_stack_m420 = *(uint64_t *)(arg1 + 0x288);
    if (v_stack_m3F8 == 0) goto loc_00AF319C;
    if (*(uint64_t *)(v_stack_m3F8) != 0) {
        v_stack_m440 = *(uint64_t *)(v_stack_m3F8);
        v_stack_m518 = 16;
    }
    result = DecodeProviderTraits(v_stack_m3F0, Arg2, v_stack_m4D0, v_stack_m400);
    v_stack_m410 = *(uint64_t *)(gs_base + (0 + 0x188));
    local_rbx = (uint16_t)(~(Arg4));
    goto loc_00AF31E5;
loc_00AF31D9:
    goto loc_00AF31EC;
loc_00AF31DF:
loc_00AF31E5:
loc_00AF31EC:
    v_stack_m4E0 = Arg2;
    if (*(uint64_t *)(v_stack_m3F8) == 0) goto loc_00AF4662;
    result = 0;
    v_stack_m3D0 = v_xmm0;
    v_stack_m3C0 = 0;
    v_stack_m470 = 0;
    v_stack_m508 = 80;
    v_stack_m4C8 = 0;
    v_stack_m4DC = 0;
    v_stack_m450 = 0;
    v_stack_m3E8 = 0;
    v_stack_m500 = 0;
    v_stack_m504 = 0;
    v_stack_m4D8 = local_r14 + 1;
    v_stack_m488 = local_r14 + 1;
    v_stack_m4B8 = 0;
    Arg1 = (uint16_t)((v_stack_m510) - ((uint16_t)(local_r14 + 1)));
    local_r13 = (Arg2 + 4) << (5);
    local_r13 = (local_r13) + (local_r11);
    if (v_stack_m4A8 == 0) goto loc_00AF3292;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(local_r13 + 0x6)))) >> (5));
    result = (uint32_t)((*(uint16_t *)(local_r13 + 0x6)) & (0x8000001FULL));
    if (!(condition_is_greater_or_equal)) {
        result = (uint32_t)((result) - ((uint32_t)(local_r14 + 1)));
        result = (uint32_t)((result) | (0xFFFFFFE0ULL));
        result = (uint32_t)((result) + ((uint32_t)(local_r14 + 1)));
    }
    if (condition_is_below) goto loc_00AF31D9;
loc_00AF3292:
    result = EtwpLevelKeywordEnabled(local_r13, Arg8, Arg9, (uint32_t)(Arg2));
    if ((uint8_t)(result) == 0) goto loc_00AF31D9;
    if (((Arg5) & (2)) != 0) goto loc_00AF32D1;
    if ((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x1F0)) >= 0) goto loc_00AF32DF;
loc_00AF32D1:
    if (((*(uint32_t *)(local_r13 + 0x8)) & (512)) != 0) goto loc_00AF31D9;
loc_00AF32DF:
    if (*(uint64_t *)(local_r11 + 0x280) == 0) goto loc_00AF3312;
    result = (*(uint64_t *)(gs_base + (0 + 0x188))) * ((uint32_t)(Arg2));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + *(uint64_t *)(local_r11 + 0x280) * 1))))) & ((uint32_t)((uint32_t)(0x80000200ULL))));
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0x80000200ULL)))) goto loc_00AF330D;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(result + *(uint64_t *)(local_r11 + 0x280) * 1))) & ((uint32_t)((uint32_t)(0x80000100ULL))));
    if (((uint32_t)(Arg1)) != ((uint32_t)((uint32_t)(0x80000100ULL)))) goto loc_00AF3312;
loc_00AF330D:
    goto loc_00AF3315;
loc_00AF3312:
loc_00AF3315:
    if (0 == 0) goto loc_00AF3351;
    v_stack_m550 = Arg11;
    v_stack_m558 = (uint32_t)((uint32_t)(Arg10));
    result = EtwpApplyEventIdPayloadFilterOnUserEvent(local_r11, (uint32_t)((uint32_t)((uint32_t)(v_stack_m4E0))), v_stack_m4C4, v_stack_m490);
    if ((uint8_t)(result) == 0) goto loc_00AF345D;
    goto loc_00AF3355;
loc_00AF3351:
loc_00AF3355:
    if (v_stack_m4CC == 0) goto loc_00AF33B4;
    v_stack_m550 = 0;
    v_stack_m558 = Arg9;
    Arg3 = 0;
    result = EtwpIsEventNameFilterEnabled(v_stack_m4B0, (uint32_t)((uint32_t)((uint32_t)(v_stack_m4E0))), Arg3, Arg8);
    if ((uint8_t)(result) == 0) goto loc_00AF33B4;
    v_stack_m538 = 0;
    v_stack_m540 = Arg9;
    v_stack_m548 = Arg8;
    v_stack_m550 = 0;
    v_stack_m558 = (uint8_t)(local_r14 + 1);
    result = EtwpApplyEventNameFilter(v_stack_m4B0, (uint32_t)((uint32_t)((uint32_t)(v_stack_m4E0))), (uint32_t)((uint32_t)((uint32_t)(Arg10))), v_stack_m4F0);
    if ((uint8_t)(result) == 0) goto loc_00AF345D;
loc_00AF33B4:
    v_stack_m4F4 = (uint32_t)(*(uint16_t *)(local_r13 + 0x6));
    v_stack_m4A0 = (uint32_t)(*(uint16_t *)(local_r13 + 0x6));
    result = ExAcquireRundownProtectionCacheAwareEx(*(uint64_t *)(*(uint64_t *)(v_stack_m4E8 + 0x2C0) + *(uint16_t *)(local_r13 + 0x6) * 8), (uint32_t)((uint32_t)(local_r14 + 1)), (uint32_t)((uint32_t)((uint32_t)(Arg10))), v_stack_m4F0);
    if ((uint8_t)(result) == 0) goto loc_00AF3416;
    if (((uint32_t)((uint32_t)((uint32_t)(*(uint16_t *)(local_r13 + 0x6))))) >= (*(uint32_t *)(v_stack_m4E8 + 0x10))) goto loc_00AF33FF;
    v_stack_m4D8 = *(uint64_t *)(*(uint64_t *)(v_stack_m4E8 + 0x2C8) + (uint32_t)((uint32_t)(*(uint16_t *)(local_r13 + 0x6))) * 8);
    v_stack_m488 = *(uint64_t *)(*(uint64_t *)(v_stack_m4E8 + 0x2C8) + (uint32_t)((uint32_t)(*(uint16_t *)(local_r13 + 0x6))) * 8);
    goto loc_00AF340A;
loc_00AF33FF:
    v_stack_m4D8 = local_r14 + 1;
    v_stack_m488 = local_r14 + 1;
loc_00AF340A:
    v_stack_m500 = (uint32_t)((uint8_t)(local_r14 + 1));
    v_stack_m504 = (uint8_t)(local_r14 + 1);
    goto loc_00AF3419;
loc_00AF3416:
loc_00AF3419:
    if ((((uint8_t)(local_r14 + 1)) & ((uint8_t)(*(uint64_t *)(*(uint64_t *)(v_stack_m4E8 + 0x2C8) + (uint32_t)((uint32_t)(*(uint16_t *)(local_r13 + 0x6))) * 8)))) == 0) goto loc_00AF3489;
    result = *(uint64_t *)(v_stack_m4E8 + 0x2C8);
    local_rdi = (uint32_t)(v_stack_m500);
    if ((uint8_t)((uint32_t)(v_stack_m500)) != 0) {
        Arg1 = *(uint64_t *)(v_stack_m4E8 + 0x2C0);
        Arg2 = (uint32_t)(local_r14 + 1);
        Arg1 = *(uint64_t *)(arg1 + (uint32_t)((uint32_t)(*(uint16_t *)(local_r13 + 0x6))) * 8);
        result = ExReleaseRundownProtectionCacheAwareEx(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg10))), v_stack_m4F0);
        result = Feature_1345841464__private_IsEnabledDeviceUsageNoInline(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg10))), v_stack_m4F0);
        local_rdi = (uint8_t)((uint32_t)(v_stack_m500));
        if ((uint32_t)(result) != 0) { local_rdi = 0; }
        v_stack_m500 = (uint32_t)(local_rdi);
    }
    if (((uint32_t)((uint32_t)((uint32_t)(*(uint16_t *)(local_r13 + 0x6))))) == 3) goto loc_00AF3466;
loc_00AF345D:
    goto loc_00AF45FB;
loc_00AF3466:
    result = (uint32_t)(-((uint32_t)(*(uint32_t *)(v_stack_m4E8 + 0x10F4))));
    Arg1 = (uint32_t)((Arg1) & (758));
    Arg1 = (uint32_t)((Arg1) + (0xC0000008ULL));
    v_stack_m4FC = (uint32_t)(Arg1);
loc_00AF3480:
    goto loc_00AF4662;
loc_00AF3489:
    if (Arg7 == NULL) goto loc_00AF34A5;
    v_stack_m508 = 104;
    goto loc_00AF34A9;
loc_00AF34A5:
loc_00AF34A9:
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m4E8 + 0x8)))) & (0xFFFFFF9FULL)) == 0) goto loc_00AF3759;
    if (condition_is_above_or_equal) goto loc_00AF34EC;
    if (v_stack_m428 == 0) goto loc_00AF34EC;
    local_r15 = (uint32_t)(v_stack_m508);
    if (v_stack_m428 != (*(uint64_t *)(v_rip + 0x4D35D6))) {
        result = *(uint16_t *)(v_stack_m428 + 0x1190);
        result = (uint32_t)((result) + (15));
        result = (uint32_t)((result) & (0xFFFFFFF8ULL));
        local_r15 = (uint32_t)(((uint32_t)(v_stack_m508)) + ((uint32_t)(result)));
        v_stack_m508 = (uint32_t)(local_r15);
    }
    if ((((uint8_t)(local_r14 + 1)) & ((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m4E8 + 0x8))))) == 0) goto loc_00AF351C;
    if (((v_stack_m518) & (2)) == 0) {
        Arg1 = v_stack_mA8;
        result = EtwpGetSidExtendedHeaderItem(Arg1, v_stack_m428, (uint32_t)((uint32_t)((uint32_t)(Arg10))), v_stack_m4F0);
        Arg1 = *(uint32_t *)(v_stack_m4E8 + 0x8);
    }
    local_rdi = (uint32_t)((104 - 88) | (2));
    local_r15 = (uint32_t)((local_r15) + ((uint32_t)(v_stack_mA8)));
    v_stack_m508 = (uint32_t)(local_r15);
loc_00AF351C:
    if ((((uint8_t)(Arg1)) & (2)) != 0) {
        local_rdi = (uint32_t)((local_rdi) | ((uint32_t)(local_r14 + 1)));
        local_r15 = (uint32_t)((local_r15) + (16));
        v_stack_m508 = (uint32_t)(local_r15);
    }
    if (sign_flag) {
        local_rdi = (uint32_t)((local_rdi) | (64));
        local_r15 = (uint32_t)((local_r15) + (16));
        v_stack_m508 = (uint32_t)(local_r15);
    }
    if (!(condition_is_above_or_equal)) {
        local_r15 = (uint32_t)((local_r15) + (16));
        v_stack_m508 = (uint32_t)(local_r15);
    }
    if (((4) & ((uint8_t)(Arg1))) == 0) goto loc_00AF36DE;
    if (*(uint64_t *)(v_stack_m4B0 + 0x280) == 0) goto loc_00AF359F;
    Arg1 = (Arg1) * ((uint32_t)((uint32_t)(v_stack_m4F0)));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + *(uint64_t *)(v_stack_m4B0 + 0x280) * 1))))) & ((uint32_t)((uint32_t)(0x80001000ULL))));
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0x80001000ULL)))) goto loc_00AF359A;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + *(uint64_t *)(v_stack_m4B0 + 0x280) * 1))))) & ((uint32_t)((uint32_t)(0x80002000ULL))));
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0x80002000ULL)))) goto loc_00AF359A;
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + *(uint64_t *)(v_stack_m4B0 + 0x280) * 1))) & ((uint32_t)((uint32_t)(0x80004000ULL))));
    if (Arg2 != ((uint32_t)((uint32_t)(0x80004000ULL)))) goto loc_00AF359F;
loc_00AF359A:
    goto loc_00AF35A2;
loc_00AF359F:
loc_00AF35A2:
    if (0 == 0) goto loc_00AF362D;
    v_stack_m558 = (uint8_t)(local_r14 + 1);
    result = EtwpApplyLevelKwFilter(v_stack_m4B0, (uint32_t)((uint32_t)(v_stack_m4F0)), Arg8, Arg9);
    if ((uint8_t)(result) == 0) goto loc_00AF36D9;
    result = EtwpApplyStackWalkFilterOnUserEvent(v_stack_m490, v_stack_m4B0, (uint32_t)((uint32_t)(v_stack_m4F0)), Arg9);
    if ((uint8_t)(result) == 0) goto loc_00AF36D9;
    v_stack_m538 = (uint8_t)(local_r14 + 1);
    v_stack_m540 = Arg9;
    v_stack_m548 = Arg8;
    v_stack_m550 = 0;
    v_stack_m558 = (uint8_t)(local_r14 + 1);
    result = EtwpApplyEventNameFilter(v_stack_m4B0, (uint32_t)((uint32_t)(v_stack_m4F0)), (uint32_t)(Arg10), v_stack_m4F0);
    if ((uint8_t)(result) == 0) goto loc_00AF36D9;
loc_00AF362D:
    if ((((uint8_t)(local_r14 + 1)) & ((uint8_t)(v_stack_m518))) != 0) goto loc_00AF3698;
    result = EtwpGetStackLookasideListEntry(v_stack_m4B0, (uint32_t)((uint32_t)(v_stack_m4F0)), (uint32_t)(Arg10), v_stack_m4F0);
    v_stack_m418 = result;
    if (result == 0) goto loc_00AF3694;
    local_rbx = (uint8_t)((v_stack_m518) | (8));
    v_stack_m518 = (uint8_t)(local_rbx);
    v_stack_m478 = result + 32;
    v_stack_m550 = 0;
    v_stack_m558 = 0;
    Arg3 = 0;
    result = EtwpGetStackExtendedHeaderItem(v_stack_m4D8, v_stack_m410, Arg3, result);
    if ((uint8_t)(result) == 0) {
        Arg1 = v_stack_m418;
        result = EtwpReleaseStackLookasideListEntry(Arg1, v_stack_m410, Arg3, result);
        local_rbx = (uint8_t)((local_rbx) & (247));
        v_stack_m518 = (uint8_t)(local_rbx);
        v_stack_m478 = 0;
    }
loc_00AF3698:
    if (v_stack_m478 == 0) goto loc_00AF36D9;
    if ((((uint8_t)(local_r14 + 1)) & ((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m4D8 + 0x334))))) == 0) goto loc_00AF36CC;
    result = EtwpGetCrimsonStackKey(v_stack_m4D8, v_stack_m478, v_stack_m4B8, result);
    if ((uint8_t)(result) == 0) goto loc_00AF36CC;
    local_rdi = (uint32_t)((local_rdi) | (8));
    local_r15 = (uint32_t)((local_r15) + (24));
    goto loc_00AF36D5;
loc_00AF36CC:
    local_rdi = (uint32_t)((local_rdi) | (4));
    local_r15 = (uint32_t)((local_r15) + ((uint32_t)(*(uint16_t *)(v_stack_m478))));
loc_00AF36D5:
    v_stack_m508 = (uint32_t)(local_r15);
loc_00AF36D9:
loc_00AF36DE:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m4E8 + 0x8)))) & (8)) == 0) goto loc_00AF3759;
    if (((v_stack_m518) & (4)) != 0) goto loc_00AF3740;
    v_stack_m408 = 0;
    v_stack_m460 = 0;
    result = IoGetStackLimits(v_stack_m460, v_stack_m408, v_stack_m4B8, result);
    result = (v_stack_m408) - (v_stack_m460);
    if (result >= = 480) {
        result = v_stack_m578;
        local_rsp = (local_rsp) - (480);
        Arg1 = v_stack_m518;
        v_stack_m438 = Arg1;
        result = *(uint32_t *)(arg1);
        result = EtwpGetPsmKeyExtendedHeaderItem(Arg1, v_stack_m408, v_stack_m4B8, result);
    }
loc_00AF3740:
    result = v_stack_m438;
    if (v_stack_m438 != 0) {
        local_rdi = (uint32_t)((local_rdi) | (32));
        result = *(uint16_t *)(v_stack_m438);
        local_r15 = (uint32_t)((local_r15) + ((uint32_t)(result)));
        v_stack_m508 = (uint32_t)(local_r15);
    }
    Arg1 = ((uint32_t)(v_stack_mB8) + (uint32_t)(v_stack_mB8) * 2) << (4);
    v_stack_m498 = Arg1;
    if ((uint32_t)((uint32_t)(Arg10)) == 0) goto loc_00AF3A25;
    v_stack_m448 = 0;
    v_stack_m503 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == 0) goto loc_00AF37D1;
    result = ((uint32_t)((uint32_t)((uint32_t)(Arg10)))) << (4);
    if (result == 0) goto loc_00AF37D1;
    if (((3) & ((uint8_t)(v_stack_m4F0))) != 0) goto loc_00AF47A1;
    if ((v_stack_m4F0 + result * 1) > result) goto loc_00AF37CF;
    if ((v_stack_m4F0 + result * 1) < v_stack_m4F0) {
        result = *(uint8_t *)(result);
    }
    v_stack_m448 = 0;
loc_00AF37DF:
    if (0 >= ((uint32_t)((uint32_t)(Arg10)))) goto loc_00AF398D;
    Arg2 = (0) << (4);
    Arg2 = (Arg2) + (v_stack_m4F0);
    v_stack_m430 = (uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0x8)));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0x8)))) <= 0xFFFFULL) goto loc_00AF3875;
    v_stack_m4FC = 0x80000005ULL;
    v_stack_m510 = (uint16_t)(v_stack_m510);
    result = Feature_1345841464__private_IsEnabledDeviceUsageNoInline(v_stack_m510, Arg2, v_stack_m4F0, 3);
    if ((uint32_t)(result) != 0) goto loc_00AF385C;
    if (v_stack_m4B8 != 0) {
        result = v_stack_m4D8;
        Arg2 = *(uint64_t *)(result + 0x420);
        Arg1 = v_stack_m4B8;
        result = EtwpDereferenceStackEntry(Arg1, Arg2, v_stack_m4F0, 3);
    }
    result = ExReleaseRundownProtectionCacheAwareEx(*(uint64_t *)(*(uint64_t *)(v_stack_m4E8 + 0x2C0) + (uint32_t)(v_stack_m4F4) * 8), (uint32_t)((uint32_t)(local_r14 + 1)), (uint32_t)(v_stack_m4F4), 3);
    goto loc_00AF3860;
loc_00AF385C:
loc_00AF3860:
    goto loc_00AF466A;
loc_00AF3875:
    if (v_stack_m4CC != 0) goto loc_00AF3881;
    goto loc_00AF388A;
loc_00AF3881:
loc_00AF388A:
    if ((uint8_t)(*(uint8_t *)((uint32_t)((uint32_t)(local_r14 + 0x1)) + 0xC)) == 0) goto loc_00AF38EF;
    Arg1 = (uint32_t)(((uint8_t)(*(uint8_t *)((uint32_t)((uint32_t)(local_r14 + 0x1)) + 0xC))) - (1));
    if (condition_is_equal) goto loc_00AF38CC;
    if (((uint32_t)(Arg1)) != 3) goto loc_00AF38E9;
    if (((uint32_t)((uint32_t)(v_stack_m430))) != 16) goto loc_00AF38E9;
    v_stack_m503 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == 0) goto loc_00AF38C0;
    result = RtlReadULong64FromUser((uint32_t)((uint32_t)(local_r14 + 1)), (uint32_t)((uint32_t)(local_r14 + 1)), (uint32_t)(v_stack_m4F4), 3);
    goto loc_00AF38C3;
loc_00AF38C0:
loc_00AF38C3:
    v_stack_m480 = *(uint64_t *)((uint32_t)((uint32_t)(local_r14 + 0x1)));
    goto loc_00AF38E9;
loc_00AF38CC:
    result = Feature_1345841464__private_IsEnabledDeviceUsageNoInline((uint32_t)((uint32_t)(local_r14 + 1)), (uint32_t)((uint32_t)(local_r14 + 1)), (uint32_t)(v_stack_m4F4), 3);
    v_stack_m460 = (uint32_t)(result);
    if ((uint32_t)(result) == 0) goto loc_00AF38E0;
    goto loc_00AF38E6;
loc_00AF38E0:
loc_00AF38E6:
loc_00AF38E9:
    goto loc_00AF38FA;
loc_00AF38EF:
    local_r15 = (uint32_t)(((uint32_t)(v_stack_m508)) + ((uint32_t)((uint32_t)(v_stack_m430))));
    v_stack_m508 = (uint32_t)(local_r15);
loc_00AF38FA:
    if (((uint32_t)(local_r15)) >= ((uint32_t)(v_stack_m4E8))) goto loc_00AF396E;
    v_stack_m4FC = 0x80000005ULL;
    v_stack_m510 = (uint16_t)(v_stack_m510);
    result = Feature_1345841464__private_IsEnabledDeviceUsageNoInline(v_stack_m510, (uint32_t)((uint32_t)(local_r14 + 1)), (uint32_t)(v_stack_m4F4), 3);
    if ((uint32_t)(result) != 0) goto loc_00AF3955;
    if (v_stack_m4B8 != 0) {
        result = v_stack_m4D8;
        Arg2 = *(uint64_t *)(result + 0x420);
        Arg1 = v_stack_m4B8;
        result = EtwpDereferenceStackEntry(Arg1, Arg2, (uint32_t)(v_stack_m4F4), 3);
    }
    result = ExReleaseRundownProtectionCacheAwareEx(*(uint64_t *)(*(uint64_t *)(v_stack_m4E8 + 0x2C0) + (uint32_t)(v_stack_m4F4) * 8), (uint32_t)((uint32_t)((uint32_t)(v_stack_m500))), (uint32_t)(v_stack_m4F4), 3);
    goto loc_00AF3959;
loc_00AF3955:
loc_00AF3959:
    goto loc_00AF466A;
loc_00AF396E:
    local_r12 = (uint32_t)((v_stack_m4F0) + ((uint32_t)((uint32_t)(v_stack_m500))));
    v_stack_m448 = (uint32_t)(local_r12);
    goto loc_00AF37DF;
loc_00AF398D:
    goto loc_00AF3A25;
loc_00AF3A25:
    if (v_stack_m4DC == 0) goto loc_00AF3A82;
    result = Feature_1345841464__private_IsEnabledDeviceUsageNoInline(*(uint64_t *)(*(uint64_t *)(v_stack_m4E8 + 0x2C0) + (uint32_t)(v_stack_m4F4) * 8), (uint32_t)(Arg10), v_stack_m4F0, 3);
    if ((uint32_t)(result) == 0) goto loc_00AF3A73;
    result = (uint32_t)(((uint32_t)(v_stack_m4C8)) + (15));
    result = (uint32_t)((result) & ((uint32_t)((uint32_t)(0xFFFFFFF8ULL))));
    if (((uint32_t)(result)) <= 0xFFFFULL) goto loc_00AF3A79;
loc_00AF3A4A:
    result = (uint32_t)(v_stack_m4FC);
    if (!sign_flag) { result = (uint32_t)((uint32_t)(0xC0000095ULL)); }
    v_stack_m4FC = (uint32_t)(result);
    v_stack_m510 = (uint16_t)(v_stack_m510);
    goto loc_00AF3480;
loc_00AF3A73:
    result = (uint32_t)((v_stack_m510) + (15));
    result = (uint32_t)((result) & ((uint32_t)(v_stack_m4E8)));
loc_00AF3A79:
    local_r15 = (uint32_t)((v_stack_m4D8) + ((uint32_t)(result)));
    v_stack_m508 = (uint32_t)(local_r15);
    goto loc_00AF3A88;
loc_00AF3A82:
loc_00AF3A88:
    if ((uint16_t)(v_stack_m4D0) == 0) goto loc_00AF3AB3;
    result = Feature_1345841464__private_IsEnabledDeviceUsageNoInline((uint32_t)(0xC0000095ULL), (uint32_t)(Arg10), v_stack_m4F0, 3);
    if ((uint32_t)(result) == 0) goto loc_00AF3AA9;
    result = (uint32_t)((v_stack_m4D0 + 15) & ((uint32_t)((uint32_t)(0xFFFFFFF8ULL))));
    if (((uint32_t)(result)) <= 0xFFFFULL) goto loc_00AF3AAC;
    goto loc_00AF3A4A;
loc_00AF3AA9:
    result = (uint32_t)((result) & ((uint32_t)((uint32_t)(0xFFFFFFF8ULL))));
loc_00AF3AAC:
    local_r15 = (uint32_t)((local_r15) + ((uint32_t)(result)));
    v_stack_m508 = (uint32_t)(local_r15);
loc_00AF3AB3:
    *(uint32_t *)(v_stack_m518 + v_stack_m498 * 1 + 0x188) = (uint32_t)(local_r15);
    v_stack_m558 = 0;
    result = EtwpReserveTraceBuffer(v_stack_m4D8, (uint32_t)((uint32_t)(local_r15)), v_stack_m3D0, v_stack_m470);
    v_stack_m460 = result;
    local_rbx = v_stack_m4B8;
    if (v_stack_m4B8 != 0) {
        result = v_stack_m4D8;
        Arg2 = *(uint64_t *)(result + 0x420);
        Arg1 = v_stack_m4B8;
        result = EtwpDereferenceStackEntry(Arg1, Arg2, v_stack_m3D0, v_stack_m470);
        result = Feature_1345841464__private_IsEnabledDeviceUsageNoInline(Arg1, Arg2, v_stack_m3D0, v_stack_m470);
        local_rbx = v_stack_m4B8;
        if ((uint32_t)(result) != 0) { local_rbx = 0; }
        v_stack_m4B8 = local_rbx;
    }
    if (result != 0) goto loc_00AF3C04;
    result = EtwpGetReserveTraceBufferStatus(v_stack_m4D8, (uint32_t)((uint32_t)(local_r15)), v_stack_m3D0, v_stack_m470);
    local_rdi = 0;
    local_r12 = 0;
    if (v_stack_m4DC >= = 0) {
        local_rdi = Arg10;
        local_r12 = v_stack_m4F0;
    }
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x40BCEC), v_rip - 11406093, v_stack_m3D0, v_stack_m470);
    if ((uint8_t)(result) != 0) {
        Arg3 = v_stack_m4D8 + 136;
        Arg2 = v_stack_m490;
        Arg2 = (Arg2) + (40);
        Arg1 = v_stack_m468;
        Arg1 = (Arg1) + (40);
        v_stack_m538 = (uint8_t)((uint32_t)(v_stack_m500));
        v_stack_m540 = (uint8_t)((uint32_t)(v_stack_m500));
        v_stack_m548 = local_r12;
        v_stack_m550 = (uint32_t)(local_rdi);
        v_stack_m558 = (uint32_t)((uint32_t)((uint32_t)(result)));
        Arg4 = Arg5;
        result = EtwpTraceLostEvent(Arg1, Arg2, Arg3, Arg4);
    }
    if (!(sign_flag)) {
        Arg1 = (uint32_t)(v_stack_m4FC);
        if (((*(uint32_t *)(v_stack_m4D8 + 0xC)) & (0x8000000ULL)) == 0) { Arg1 = (uint32_t)((uint32_t)((uint32_t)(result))); }
        v_stack_m4FC = (uint32_t)(Arg1);
    }
    result = ExReleaseRundownProtectionCacheAwareEx(*(uint64_t *)(*(uint64_t *)(v_stack_m4E8 + 0x2C0) + (uint32_t)(v_stack_m4F4) * 8), (uint32_t)((uint32_t)((uint32_t)(v_stack_m500))), (uint32_t)(v_stack_m4F4), Arg4);
    result = Feature_1345841464__private_IsEnabledDeviceUsageNoInline(*(uint64_t *)(*(uint64_t *)(v_stack_m4E8 + 0x2C0) + (uint32_t)(v_stack_m4F4) * 8), (uint32_t)((uint32_t)((uint32_t)(v_stack_m500))), (uint32_t)(v_stack_m4F4), Arg4);
    Arg1 = (uint8_t)((uint32_t)(v_stack_m500));
    if ((uint32_t)(result) != 0) { Arg1 = 0; }
    v_stack_m500 = (uint32_t)(Arg1);
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != ((uint32_t)((uint32_t)(0xC0000095ULL)))) goto loc_00AF31DF;
    v_stack_m4FC = (uint32_t)((uint32_t)(0xC0000095ULL));
    goto loc_00AF3480;
loc_00AF3C04:
    *(uint64_t *)(v_stack_m518 + v_stack_m4F0 * 1 + 0x160) = v_stack_m4D8;
    *(uint64_t *)(v_stack_m518 + v_stack_m4F0 * 1 + 0x168) = v_stack_m4E8;
    *(uint64_t *)(v_stack_m518 + v_stack_m4F0 * 1 + 0x170) = v_xmm0;
    *(uint64_t *)(v_stack_m518 + v_stack_m4F0 * 1 + 0x180) = v_xmm0;
    result = Feature_1345841464__private_IsEnabledDeviceUsageNoInline(Arg1, (uint32_t)((uint32_t)((uint32_t)(v_stack_m500))), v_stack_m4A8, (uint32_t)(0xC0000095ULL));
    Arg1 = (uint8_t)((uint32_t)(v_stack_m500));
    if ((uint32_t)(result) != 0) { Arg1 = 0; }
    v_stack_m500 = (uint32_t)(Arg1);
    v_stack_m504 = (uint8_t)(Arg1);
    v_stack_m458 = 0;
    v_stack_m4F8 = 80;
    v_stack_m4C0 = 0;
    *(uint64_t *)(v_stack_m4E8) = v_xmm0;
    *(uint64_t *)(v_stack_m4E8 + 0x10) = v_xmm1;
    *(uint64_t *)(v_stack_m4E8 + 0x20) = v_xmm0;
    *(uint64_t *)(v_stack_m4E8 + 0x30) = v_xmm1;
    *(uint64_t *)(v_stack_m4E8 + 0x40) = v_xmm0;
    if (v_stack_m400 != 0) goto loc_00AF3CCB;
    if (v_stack_m480 != 0) goto loc_00AF3CD8;
    *(uint64_t *)(v_stack_m4E8 + 0x18) = v_xmm0;
    goto loc_00AF3D77;
loc_00AF3CCB:
    if (v_stack_m480 == 0) goto loc_00AF3D5F;
loc_00AF3CD8:
    v_stack_m503 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == 0) goto loc_00AF3D17;
    if ((((uint8_t)(v_stack_m480)) & (3)) != 0) goto loc_00AF47A7;
    if ((v_stack_m480 + 16) > ((uint32_t)((uint32_t)((uint32_t)(v_stack_m500))))) goto loc_00AF3D15;
    result = v_stack_m480;
    if ((v_stack_m480 + 16) < v_stack_m480) {
        result = *(uint8_t *)((uint32_t)((uint32_t)((uint32_t)(v_stack_m500))));
    }
    v_stack_m503 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == 0) goto loc_00AF3D45;
    result = RtlCopyFromUser(v_stack_m4E8 + 24, v_stack_m480, 16, (uint32_t)(0xC0000095ULL));
    goto loc_00AF3D4A;
loc_00AF3D45:
    result = RtlCopyVolatileMemory(v_stack_m4E8 + 24, v_stack_m480, 16, (uint32_t)(0xC0000095ULL));
loc_00AF3D4A:
    result = (uint16_t)((128) | (*(uint16_t *)(v_stack_m4E8 + 0x4)));
    *(uint16_t *)(v_stack_m4E8 + 0x4) = (uint16_t)(result);
    goto loc_00AF3D77;
loc_00AF3D5F:
    *(uint64_t *)(v_stack_m4E8 + 0x18) = v_xmm0;
    result = (uint16_t)((128) | (*(uint16_t *)(v_stack_m4E8 + 0x4)));
    *(uint16_t *)(v_stack_m4E8 + 0x4) = (uint16_t)(result);
loc_00AF3D77:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m508)))) | (*(uint32_t *)(v_rip - 0xABBA1A + v_stack_m4C4 * 4)));
    *(uint32_t *)(v_stack_m4E8) = (uint32_t)(result);
    if (((v_stack_p70) & ((uint16_t)((uint32_t)(0x400ULL)))) != 0) {
    }
    if ((uint32_t)(local_rdi) == 0) goto loc_00AF41F3;
    result = (uint32_t)(0x400ULL);
    local_rbx = 80;
    local_rsi = (uint32_t)(v_stack_m500);
    local_r12 = 0;
    if (!(condition_is_above_or_equal)) {
        local_r12 = v_stack_m4E8 + 80;
        Arg1 = v_stack_m428;
        local_rsi = *(uint16_t *)(arg1 + 0x1190);
        local_rsi = (uint16_t)((local_rsi) + (15));
        result = 0xFFF8ULL;
        local_rsi = (uint16_t)((local_rsi) & ((uint16_t)(result)));
        *(uint16_t *)(local_r12) = (uint16_t)(local_rsi);
        result = 16;
        *(uint16_t *)(local_r12 + 0x2) = (uint16_t)(result);
        result = *(uint16_t *)(arg1 + 0x1190);
        *(uint16_t *)(local_r12 + 0x6) = (uint16_t)(result);
        result = *(uint16_t *)(local_r12 + 0x4);
        Arg2 = 0xFFFEULL;
        result = (uint16_t)((result) & ((uint16_t)(Arg2)));
        *(uint16_t *)(local_r12 + 0x4) = (uint16_t)(result);
        *(uint16_t *)(local_r12 + 0x4) = 0;
        Arg3 = *(uint16_t *)(arg1 + 0x1190);
        local_rsi = (uint16_t)((local_rsi) - (Arg3));
        local_rsi = (uint16_t)((local_rsi) - (8));
        local_rbx = local_r12 + 8;
        Arg2 = *(uint64_t *)(arg1 + 0x1188);
        Arg1 = local_rbx;
        result = memcpy(Arg1, Arg2, Arg3, (uint32_t)(0xC0000095ULL));
        Arg3 = (uint16_t)(local_rsi);
        Arg1 = v_stack_m428;
        Arg1 = *(uint16_t *)(arg1 + 0x1190);
        Arg1 = (Arg1) + (local_rbx);
        Arg2 = 0;
        result = memset(Arg1, Arg2, Arg3, (uint32_t)(0xC0000095ULL));
        local_rsi = 1;
        local_rbx = *(uint16_t *)(local_r12);
        local_rbx = (uint32_t)((local_rbx) + (80));
        v_stack_m4F8 = (uint32_t)(local_rbx);
        v_stack_m4C0 = local_r12;
    }
    if (((16) & ((uint8_t)(local_rdi))) == 0) goto loc_00AF3ECD;
    *(uint32_t *)(local_rbx + v_stack_m4E8 * 1) = 0x10018ULL;
    *(uint16_t *)(local_rbx + v_stack_m4E8 * 1 + 0x6) = 16;
    result = (uint16_t)((*(uint16_t *)(local_rbx + v_stack_m4E8 * 1 + 0x4)) & ((uint16_t)((uint32_t)(0xFFFEULL))));
    *(uint16_t *)(local_rbx + v_stack_m4E8 * 1 + 0x4) = (uint16_t)(result);
    *(uint16_t *)(local_rbx + v_stack_m4E8 * 1 + 0x4) = 0;
    *(uint64_t *)(local_rbx + v_stack_m4E8 * 1 + 0x8) = v_xmm0;
    result = (uint16_t)((*(uint16_t *)(v_stack_m4E8 + 0x4)) | ((uint16_t)(local_rsi)));
    *(uint16_t *)(v_stack_m4E8 + 0x4) = (uint16_t)(result);
    local_rbx = (uint32_t)((local_rbx) + (24));
    v_stack_m4F8 = (uint32_t)(local_rbx);
    if (local_r12 != 0) {
        result = *(uint16_t *)(local_r12 + 0x4);
        result = (uint16_t)((result) | ((uint16_t)(local_rsi)));
        *(uint16_t *)(local_r12 + 0x4) = (uint16_t)(result);
    }
    v_stack_m4C0 = local_rbx + v_stack_m4E8 * 1;
loc_00AF3ECD:
    if ((((uint8_t)(local_rdi)) & (2)) == 0) goto loc_00AF3F2E;
    result = ((uint32_t)((uint32_t)(local_rbx))) + (v_stack_m4E8);
    v_stack_m498 = result;
    result = memcpy(result, v_stack_mA8, v_stack_mA8, (uint32_t)(0xFFFEULL));
    result = (uint16_t)((*(uint16_t *)(v_stack_m4E8 + 0x4)) | ((uint16_t)(local_rsi)));
    *(uint16_t *)(v_stack_m4E8 + 0x4) = (uint16_t)(result);
    local_rbx = (uint32_t)((local_rbx) + ((uint32_t)(v_stack_mA8)));
    v_stack_m4F8 = (uint32_t)(local_rbx);
    result = v_stack_mA8;
    if (local_rbx + v_stack_m4E8 * 1 != 0) {
        result = *(uint16_t *)(local_rbx + v_stack_m4E8 * 1 + 0x4);
        result = (uint16_t)((result) | ((uint16_t)(local_rsi)));
        *(uint16_t *)(local_rbx + v_stack_m4E8 * 1 + 0x4) = (uint16_t)(result);
    }
    v_stack_m4C0 = v_stack_m498;
loc_00AF3F2E:
    if ((((uint8_t)(local_rsi)) & ((uint8_t)(local_rdi))) == 0) goto loc_00AF3F95;
    *(uint32_t *)(local_rbx + v_stack_m4E8 * 1) = 0x30010ULL;
    *(uint16_t *)(local_rbx + v_stack_m4E8 * 1 + 0x6) = 4;
    result = (uint16_t)((*(uint16_t *)(local_rbx + v_stack_m4E8 * 1 + 0x4)) & ((uint16_t)((uint32_t)(0xFFFEULL))));
    *(uint16_t *)(local_rbx + v_stack_m4E8 * 1 + 0x4) = (uint16_t)(result);
    *(uint16_t *)(local_rbx + v_stack_m4E8 * 1 + 0x4) = 0;
    result = PsGetCurrentProcessSessionId(local_rbx + v_stack_m4E8 * 1, (uint32_t)(0xFFFEULL), v_stack_mA8, (uint32_t)(0xFFFEULL));
    *(uint32_t *)(local_rbx + v_stack_m4E8 * 1 + 0x8) = (uint32_t)(result);
    result = (uint16_t)((*(uint16_t *)(v_stack_m4E8 + 0x4)) | ((uint16_t)(local_rsi)));
    *(uint16_t *)(v_stack_m4E8 + 0x4) = (uint16_t)(result);
    local_rbx = (uint32_t)((local_rbx) + (16));
    v_stack_m4F8 = (uint32_t)(local_rbx);
    if (v_stack_m498 != 0) {
        result = *(uint16_t *)(v_stack_m498 + 0x4);
        result = (uint16_t)((result) | ((uint16_t)(local_rsi)));
        *(uint16_t *)(v_stack_m498 + 0x4) = (uint16_t)(result);
    }
    v_stack_m4C0 = local_rbx + v_stack_m4E8 * 1;
loc_00AF3F95:
    if ((((uint8_t)(local_rdi)) & (64)) == 0) goto loc_00AF4017;
    *(uint32_t *)(local_rbx + v_stack_m4E8 * 1) = 0xD0010ULL;
    *(uint16_t *)(local_rbx + v_stack_m4E8 * 1 + 0x6) = (uint16_t)(16 - 8);
    result = (uint16_t)((*(uint16_t *)(local_rbx + v_stack_m4E8 * 1 + 0x4)) & ((uint16_t)((uint32_t)(0xFFFEULL))));
    *(uint16_t *)(local_rbx + v_stack_m4E8 * 1 + 0x4) = (uint16_t)(result);
    *(uint16_t *)(local_rbx + v_stack_m4E8 * 1 + 0x4) = 0;
    result = EtwpGetProcessStartKey(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), (uint32_t)(0xFFFEULL), local_rbx + v_stack_m4E8 * 1, (uint32_t)(0xFFFEULL));
    *(uint64_t *)(local_rbx + v_stack_m4E8 * 1 + 0x8) = result;
    result = (uint16_t)((*(uint16_t *)(v_stack_m4E8 + 0x4)) | ((uint16_t)(local_rsi)));
    *(uint16_t *)(v_stack_m4E8 + 0x4) = (uint16_t)(result);
    local_rbx = (uint32_t)((local_rbx) + (16));
    v_stack_m4F8 = (uint32_t)(local_rbx);
    if (local_rbx + v_stack_m4E8 * 1 != 0) {
        result = *(uint16_t *)(local_rbx + v_stack_m4E8 * 1 + 0x4);
        result = (uint16_t)((result) | ((uint16_t)(local_rsi)));
        *(uint16_t *)(local_rbx + v_stack_m4E8 * 1 + 0x4) = (uint16_t)(result);
    }
    v_stack_m4C0 = local_rbx + v_stack_m4E8 * 1;
loc_00AF4017:
    if (!sign_flag) goto loc_00AF40B4;
    *(uint32_t *)(local_rbx + v_stack_m4E8 * 1) = 0xA0010ULL;
    *(uint16_t *)(local_rbx + v_stack_m4E8 * 1 + 0x6) = 8;
    result = (uint16_t)((*(uint16_t *)(local_rbx + v_stack_m4E8 * 1 + 0x4)) & ((uint16_t)((uint32_t)(0xFFFEULL))));
    *(uint16_t *)(local_rbx + v_stack_m4E8 * 1 + 0x4) = (uint16_t)(result);
    *(uint16_t *)(local_rbx + v_stack_m4E8 * 1 + 0x4) = 0;
    if (((v_stack_m518) & (16)) != 0) goto loc_00AF407B;
    result = EtwpCreateEventKey(v_stack_m440, (uint32_t)(0xFFFEULL), local_rbx + v_stack_m4E8 * 1, local_rbx + v_stack_m4E8 * 1);
    if (v_stack_m3F8 != 0) {
        result = v_stack_m440;
        *(uint64_t *)(v_stack_m3F8) = result;
    }
    *(uint64_t *)(local_rbx + v_stack_m4E8 * 1 + 0x8) = v_stack_m440;
    result = (uint16_t)((*(uint16_t *)(v_stack_m4E8 + 0x4)) | ((uint16_t)(local_rsi)));
    *(uint16_t *)(v_stack_m4E8 + 0x4) = (uint16_t)(result);
    local_rbx = (uint32_t)((local_rbx) + (16));
    v_stack_m4F8 = (uint32_t)(local_rbx);
    if (local_rbx + v_stack_m4E8 * 1 != 0) {
        result = *(uint16_t *)(local_rbx + v_stack_m4E8 * 1 + 0x4);
        result = (uint16_t)((result) | ((uint16_t)(local_rsi)));
        *(uint16_t *)(local_rbx + v_stack_m4E8 * 1 + 0x4) = (uint16_t)(result);
    }
    v_stack_m4C0 = local_rbx + v_stack_m4E8 * 1;
loc_00AF40B4:
    if (((4) & ((uint8_t)(local_rdi))) == 0) goto loc_00AF411D;
    result = ((uint32_t)((uint32_t)(local_rbx))) + (v_stack_m4E8);
    v_stack_m498 = result;
    result = memcpy(result, v_stack_m478, *(uint16_t *)(v_stack_m478), local_rbx + v_stack_m4E8 * 1);
    result = (uint16_t)((*(uint16_t *)(v_stack_m4E8 + 0x4)) | ((uint16_t)(local_rsi)));
    *(uint16_t *)(v_stack_m4E8 + 0x4) = (uint16_t)(result);
    local_rbx = (uint32_t)((local_rbx) + ((uint32_t)(*(uint16_t *)(v_stack_m478))));
    v_stack_m4F8 = (uint32_t)(local_rbx);
    result = *(uint16_t *)(v_stack_m478);
    if (local_rbx + v_stack_m4E8 * 1 != 0) {
        result = *(uint16_t *)(local_rbx + v_stack_m4E8 * 1 + 0x4);
        result = (uint16_t)((result) | ((uint16_t)(local_rsi)));
        *(uint16_t *)(local_rbx + v_stack_m4E8 * 1 + 0x4) = (uint16_t)(result);
    }
    v_stack_m4C0 = v_stack_m498;
    goto loc_00AF4124;
loc_00AF411D:
loc_00AF4124:
    if (((8) & ((uint8_t)(local_rdi))) == 0) goto loc_00AF419B;
    Arg1 = ((uint32_t)((uint32_t)(local_rbx))) + (v_stack_m4E8);
    *(uint32_t *)(arg1) = 0x120018ULL;
    *(uint16_t *)(arg1 + 0x6) = (uint16_t)(8 + 8);
    result = (uint16_t)((*(uint16_t *)(arg1 + 0x4)) & ((uint16_t)((uint32_t)(0xFFFEULL))));
    *(uint16_t *)(arg1 + 0x4) = (uint16_t)(result);
    *(uint16_t *)(arg1 + 0x4) = 0;
    *(uint64_t *)(arg1 + 0x10) = v_stack_m4B8;
    *(uint64_t *)(arg1 + 0x8) = *(uint64_t *)(v_stack_m478 + 0x8);
    result = (uint16_t)((*(uint16_t *)(v_stack_m4E8 + 0x4)) | ((uint16_t)(local_rsi)));
    *(uint16_t *)(v_stack_m4E8 + 0x4) = (uint16_t)(result);
    local_rbx = (uint32_t)((local_rbx) + ((uint32_t)(8 + 16)));
    v_stack_m4F8 = (uint32_t)(local_rbx);
    if (v_stack_m498 != 0) {
        result = *(uint16_t *)(v_stack_m498 + 0x4);
        result = (uint16_t)((result) | ((uint16_t)(local_rsi)));
        *(uint16_t *)(v_stack_m498 + 0x4) = (uint16_t)(result);
    }
    v_stack_m4C0 = Arg1;
loc_00AF419B:
    if ((((uint8_t)(local_rdi)) & (32)) == 0) goto loc_00AF41F9;
    local_rdi = ((uint32_t)((uint32_t)(local_rbx))) + (v_stack_m4E8);
    result = memcpy(local_rdi, v_stack_m438, *(uint16_t *)(v_stack_m438), (uint32_t)(0xFFFEULL));
    result = (uint16_t)((*(uint16_t *)(v_stack_m4E8 + 0x4)) | ((uint16_t)(local_rsi)));
    *(uint16_t *)(v_stack_m4E8 + 0x4) = (uint16_t)(result);
    local_rbx = (uint32_t)((local_rbx) + ((uint32_t)(*(uint16_t *)(v_stack_m438))));
    v_stack_m4F8 = (uint32_t)(local_rbx);
    result = *(uint16_t *)(v_stack_m438);
    if (Arg1 != NULL) {
        result = *(uint16_t *)(arg1 + 0x4);
        result = (uint16_t)((result) | ((uint16_t)(local_rsi)));
        *(uint16_t *)(arg1 + 0x4) = (uint16_t)(result);
    }
    v_stack_m4C0 = local_rdi;
loc_00AF41F3:
loc_00AF41F9:
    if ((uint16_t)(v_stack_m4D0) == 0) goto loc_00AF42B5;
    Arg1 = ((uint32_t)((uint32_t)(local_rbx))) + (v_stack_m4E8);
    v_stack_m498 = Arg1;
    local_rsi = (uint32_t)((15) + ((uint32_t)(v_stack_m4D0)));
    local_rsi = (uint16_t)((local_rsi) & ((uint16_t)((uint32_t)(0xFFF8ULL))));
    *(uint16_t *)(arg1) = (uint16_t)(local_rsi);
    *(uint16_t *)(arg1 + 0x2) = 12;
    *(uint16_t *)(arg1 + 0x6) = (uint16_t)(v_stack_m4D0);
    result = (uint16_t)((*(uint16_t *)(arg1 + 0x4)) & ((uint16_t)((uint32_t)(0xFFFEULL))));
    *(uint16_t *)(arg1 + 0x4) = (uint16_t)(result);
    *(uint16_t *)(arg1 + 0x4) = 0;
    local_rsi = (uint16_t)((local_rsi) - ((uint16_t)(v_stack_m4D0)));
    local_rsi = (uint16_t)((local_rsi) - (8));
    result = memcpy(Arg1 + 8, v_stack_m3F0, (uint32_t)((uint32_t)(v_stack_m4D0)), (uint32_t)(0xFFFEULL));
    Arg2 = 0;
    result = memset((uint32_t)((uint32_t)(v_stack_m4D0)) + Arg1 + 8 * 1, Arg2, (uint16_t)(local_rsi), (uint32_t)(0xFFFEULL));
    result = (uint16_t)((*(uint16_t *)(v_stack_m4E8 + 0x4)) | (1));
    *(uint16_t *)(v_stack_m4E8 + 0x4) = (uint16_t)(result);
    local_rbx = (uint32_t)(((uint32_t)(v_stack_m4F8)) + ((uint32_t)(*(uint16_t *)(v_stack_m498))));
    v_stack_m4F8 = (uint32_t)(local_rbx);
    result = *(uint16_t *)(v_stack_m498);
    if (local_rdi != 0) {
        result = *(uint16_t *)(local_rdi + 0x4);
        result = (uint16_t)((result) | (1));
        *(uint16_t *)(local_rdi + 0x4) = (uint16_t)(result);
    }
    v_stack_m4C0 = v_stack_m498;
loc_00AF42B5:
    if (v_stack_m4DC == 0) goto loc_00AF435A;
    local_rbx = (local_rbx) + (v_stack_m4E8);
    Arg3 = (uint32_t)((15) + ((uint32_t)((uint32_t)(v_stack_m4C8))));
    Arg3 = (uint16_t)((Arg3) & ((uint16_t)((uint32_t)(0xFFF8ULL))));
    *(uint16_t *)(local_rbx) = Arg3;
    *(uint16_t *)(local_rbx + 0x2) = 11;
    *(uint16_t *)(local_rbx + 0x6) = (uint16_t)((uint32_t)(v_stack_m4C8));
    result = (uint16_t)((*(uint16_t *)(local_rbx + 0x4)) & ((uint16_t)((uint32_t)(0xFFFEULL))));
    *(uint16_t *)(local_rbx + 0x4) = (uint16_t)(result);
    *(uint16_t *)(local_rbx + 0x4) = 0;
    Arg3 = (uint16_t)((Arg3) - ((uint16_t)((uint32_t)(v_stack_m4C8))));
    Arg3 = (uint16_t)((Arg3) - (8));
    v_stack_m450 = local_rbx + 8;
    v_stack_m3E8 = local_rbx + 8 + (uint32_t)(v_stack_m4C8) * 1;
    Arg2 = 0;
    result = memset(local_rbx + 8 + (uint32_t)(v_stack_m4C8) * 1, Arg2, Arg3, local_rbx + 8 + (uint32_t)(v_stack_m4C8) * 1);
    result = (uint16_t)((*(uint16_t *)(v_stack_m4E8 + 0x4)) | (1));
    *(uint16_t *)(v_stack_m4E8 + 0x4) = (uint16_t)(result);
    local_rbx = (uint32_t)(((uint32_t)(v_stack_m4F8)) + ((uint32_t)(*(uint16_t *)(local_rbx))));
    v_stack_m4F8 = (uint32_t)(local_rbx);
    result = *(uint16_t *)(local_rbx);
    if (v_stack_m498 != 0) {
        result = *(uint16_t *)(v_stack_m498 + 0x4);
        result = (uint16_t)((result) | (1));
        *(uint16_t *)(v_stack_m498 + 0x4) = (uint16_t)(result);
    }
    v_stack_m458 = 0;
loc_00AF4364:
    if (0 >= ((uint32_t)((uint32_t)(Arg10)))) goto loc_00AF451A;
    result = (0) + (0);
    if (v_stack_m4CC != 0) goto loc_00AF4391;
    goto loc_00AF4399;
loc_00AF4391:
loc_00AF4399:
    if ((uint8_t)(*(uint8_t *)(v_stack_m4F0 + 0x0 * 8 + 0xC)) == 0) goto loc_00AF4477;
    Arg1 = (uint32_t)(((uint8_t)(*(uint8_t *)(v_stack_m4F0 + 0x0 * 8 + 0xC))) - (1));
    if (condition_is_equal) goto loc_00AF43E0;
    if (((uint32_t)(Arg1)) != 2) goto loc_00AF43DB;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m4F0 + result * 8 + 0x8)))) != 8) goto loc_00AF43DB;
    if ((*(uint64_t *)(v_stack_m4F0 + result * 8) + 8) > Arg1) goto loc_00AF43CB;
    result = *(uint64_t *)(v_stack_m4F0 + result * 8) + 8;
    local_r15 = (uint32_t)(v_stack_m508);
    if ((*(uint64_t *)(v_stack_m4F0 + result * 8) + 8) < (*(uint64_t *)(v_stack_m4F0 + result * 8))) {
        result = *(uint8_t *)(arg1);
        local_r15 = v_stack_m508;
    }
    v_stack_m470 = *(uint64_t *)(*(uint64_t *)(v_stack_m4F0 + result * 8));
loc_00AF43DB:
    goto loc_00AF44D1;
loc_00AF43E0:
    if (v_stack_m450 == 0) goto loc_00AF4441;
    if (((uint32_t)(*(uint32_t *)(v_stack_m4F0 + result * 8 + 0x8)) + v_stack_m450 * 1) < v_stack_m450) goto loc_00AF4441;
    if (((uint32_t)(*(uint32_t *)(v_stack_m4F0 + result * 8 + 0x8)) + v_stack_m450 * 1) > v_stack_m3E8) goto loc_00AF4441;
    if (v_stack_m4DC == 0) goto loc_00AF4441;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m4F0 + result * 8 + 0x8))) == 0) goto loc_00AF4426;
    if (((uint32_t)(*(uint32_t *)(v_stack_m4F0 + result * 8 + 0x8)) + *(uint64_t *)(v_stack_m4F0 + result * 8) * 1) > v_stack_m450) goto loc_00AF4420;
    result = (uint32_t)(*(uint32_t *)(v_stack_m4F0 + result * 8 + 0x8)) + *(uint64_t *)(v_stack_m4F0 + result * 8) * 1;
    if (((uint32_t)(*(uint32_t *)(v_stack_m4F0 + result * 8 + 0x8)) + *(uint64_t *)(v_stack_m4F0 + result * 8) * 1) < (*(uint64_t *)(v_stack_m4F0 + result * 8))) {
        result = *(uint8_t *)(v_stack_m450);
        local_r15 = v_stack_m508;
    }
    result = memcpy(v_stack_m450, *(uint64_t *)(v_stack_m4F0 + result * 8), (uint32_t)(*(uint32_t *)(v_stack_m4F0 + result * 8 + 0x8)), local_rbx + 8 + (uint32_t)(v_stack_m4C8) * 1);
    goto loc_00AF43DB;
loc_00AF4441:
    v_stack_m4FC = 0xC0000004ULL;
    local_r15 = (uint32_t)((local_r15) | (0xC00D0000ULL));
    *(uint32_t *)(v_stack_m4E8) = (uint32_t)(local_r15);
    *(uint64_t *)(v_stack_m4E8 + 0x10) = v_stack_m470;
    goto loc_00AF466A;
loc_00AF4477:
    Arg4 = ((uint32_t)((uint32_t)(local_rbx))) + (v_stack_m4E8);
    if (((uint32_t)(1 + local_rbx * 1)) < ((uint32_t)(local_rbx))) goto loc_00AF44E0;
    v_stack_m4F8 = (uint32_t)(1 + local_rbx * 1);
    if (((uint32_t)(1 + local_rbx * 1)) > ((uint32_t)(v_stack_m4D8))) goto loc_00AF44E4;
    v_stack_m503 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == 0) goto loc_00AF44C2;
    if (1 == 0) goto loc_00AF44C2;
    if ((*(uint64_t *)(v_stack_m4F0 + result * 8) + 1 * 1) > (*(uint64_t *)(gs_base + (0 + 0x188)))) goto loc_00AF44C0;
    result = *(uint64_t *)(gs_base + (0 + 0x188));
    if ((*(uint64_t *)(v_stack_m4F0 + result * 8) + 1 * 1) < (*(uint64_t *)(v_stack_m4F0 + result * 8))) {
        result = *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)));
    }
    result = memcpy(Arg4, *(uint64_t *)(v_stack_m4F0 + result * 8), 1, Arg4);
loc_00AF44D1:
    local_r12 = (uint32_t)((v_stack_m4F0) + ((uint32_t)((uint32_t)(v_stack_m500))));
    v_stack_m458 = (uint32_t)(local_r12);
    goto loc_00AF4364;
loc_00AF44E0:
loc_00AF44E4:
    v_stack_m4FC = 0xC0000004ULL;
    local_r15 = (uint32_t)(((uint32_t)(v_stack_m508)) | (0xC00D0000ULL));
    *(uint32_t *)(v_stack_m4E8) = (uint32_t)(local_r15);
    *(uint64_t *)(v_stack_m4E8 + 0x10) = v_stack_m470;
    goto loc_00AF466A;
loc_00AF451A:
    result = v_stack_m470;
    if (v_stack_m4A8 != 0) {
        Arg1 = v_stack_m4F4;
        result = (uint32_t)(Arg1);
        result = (uint32_t)((result) >> (5));
        Arg2 = (uint32_t)(result);
        Arg1 = (uint32_t)((Arg1) & (31));
        result = *(uint32_t *)(v_stack_m4A8 + result * 4);
        *(uint32_t *)(v_stack_m4A8 + Arg2 * 4) = (uint32_t)(result);
    }
    *(uint64_t *)(v_stack_m4E8 + 0x10) = v_stack_m470;
    *(uint32_t *)(v_stack_m4E8 + 0x38) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m410 + 0x28C)));
    *(uint32_t *)(v_stack_m4E8 + 0x3C) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m410 + 0x2DC)));
    *(uint32_t *)(v_stack_m4E8 + 0x8) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m410 + 0x510)));
    *(uint32_t *)(v_stack_m4E8 + 0xC) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m410 + 0x508)));
    if (((*(uint32_t *)(v_stack_m4D8 + 0xC)) & (0x80000ULL)) == 0) goto loc_00AF45B1;
    if ((*(uint8_t *)(v_rip + 0x453052)) != 0) goto loc_00AF4595;
    if ((*(uint8_t *)(v_rip + 0x316489)) == 0) goto loc_00AF459E;
loc_00AF4595:
    result = (uint32_t)(*(uint32_t *)(v_stack_m410 + 0x508));
    if ((*(uint8_t *)(v_rip + 0x461717)) != 0) {
        Arg2 = v_stack_m3D0;
        Arg1 = v_stack_m4D8;
        result = EtwpSendTraceEvent(Arg1, Arg2, v_stack_m4A8, Arg4);
        Arg3 = v_stack_m4A8;
    }
    if ((*(uint64_t *)(v_stack_m4D8 + 0x620)) == 0) goto loc_00AF31EC;
    Arg3 = (v_stack_m468) + (40);
    result = EtwpInvokeEventCallback(v_stack_m4D8, v_stack_m3D0, Arg3, *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
loc_00AF45FB:
    goto loc_00AF31EC;
loc_00AF4662:
loc_00AF466A:
    result = Feature_1345841464__private_IsEnabledDeviceUsageNoInline(v_stack_m4D8, v_stack_m3D0, v_stack_m4A8, *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    if ((uint32_t)(result) == 0) goto loc_00AF46A5;
    if (v_stack_m4B8 != 0) {
        Arg2 = *(uint64_t *)(v_stack_m4D8 + 0x420);
        Arg1 = v_stack_m4B8;
        result = EtwpDereferenceStackEntry(Arg1, Arg2, v_stack_m4A8, *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    }
    if ((uint8_t)((uint32_t)(v_stack_m500)) != 0) {
        result = v_stack_m4F4;
        Arg1 = *(uint64_t *)(v_stack_m4E8 + 0x2C0);
        Arg2 = 1;
        Arg1 = *(uint64_t *)(arg1 + result * 8);
        result = ExReleaseRundownProtectionCacheAwareEx(Arg1, Arg2, v_stack_m4A8, *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    }
    if (((v_stack_m518) & (8)) != 0) {
        Arg1 = v_stack_m418;
        result = EtwpReleaseStackLookasideListEntry(Arg1, Arg2, v_stack_m4A8, *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    }
    if (v_stack_m4FC < 0) goto loc_00AF4710;
    if (v_stack_mB8 <= 0) goto loc_00AF476E;
loc_00AF46CD:
    local_r11 = (0 + 0 * 2) + (0 + 0 * 2);
    result = EtwpReleaseTraceBuffer(v_stack_m518 + local_r11 * 8 + 368, Arg2, v_stack_m4A8, *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    result = ExReleaseRundownProtectionCacheAwareEx(*(uint64_t *)(*(uint64_t *)(v_stack_m4E8 + 0x2C0) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m518 + local_r11 * 8 + 0x160))) * 8), 1, v_stack_m4A8, *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    local_rbx = (uint32_t)((0) + 1);
    if (((uint32_t)(local_rbx)) < v_stack_mB8) goto loc_00AF46CD;
    goto loc_00AF476E;
loc_00AF4710:
    result = (v_stack_m490) + (40);
    v_stack_m520 = 1;
    v_stack_m528 = v_stack_m4F0;
    v_stack_m530 = (uint32_t)((uint32_t)(Arg10));
    v_stack_m538 = 1;
    v_stack_m540 = result;
    v_stack_m548 = (uint32_t)((uint32_t)(v_stack_m4FC));
    v_stack_m550 = (uint32_t)((uint32_t)((uint32_t)(local_rbx)));
    v_stack_m558 = (uint16_t)(v_stack_m510);
    result = EtwpFailLogging(Arg8, Arg9, v_stack_m468, v_stack_m3B8);
loc_00AF476E:
    result = KiLeaveCriticalRegionUnsafe(v_stack_m410, Arg9, v_stack_m468, v_stack_m3B8);
loc_00AF477D:
    Arg1 = (v_stack_m58) ^ (v_stack_m518);
    result = _security_check_cookie(Arg1, Arg9, v_stack_m468, v_stack_m3B8);
    return result;
loc_00AF47A1:
    result = ExRaiseDatatypeMisalignment(Arg1, Arg9, v_stack_m468, v_stack_m3B8);
loc_00AF47A7:
    result = ExRaiseDatatypeMisalignment(Arg1, Arg9, v_stack_m468, v_stack_m3B8);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x288` | `64` | `R` |
| `Arg7` | `+ 0x0` | `128` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AF2FEC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
