# EtwpStartLogger

- RVA: `0x00A99D80`–`0x00A9ADFF` (길이 `4,223` bytes)
- VA: `0x0000000140A99D80`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BA2D8`
- 디코드: `1,003`개 명령, `4,223/4,223` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **85**; 고유 호출 대상: **56**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **35**

### Outgoing calls
- `0x00A99DEB` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00A99DF7` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00A99E61` → [EtwpCaptureString](../9B/EtwpCaptureString_function_009BD754.md) (function, `0x009BD754`)
- `0x00A9A048` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x00A9A070` → [EtwpEventWriteTemplateAdmin](../AA/EtwpEventWriteTemplateAdmin_function_00AA5880.md) (function, `0x00AA5880`)
- `0x00A9A07A` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x00A9A084` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x00A9A08E` → [EtwpFreeSecurityDescriptor](../A1/EtwpFreeSecurityDescriptor_function_00A1E7DC.md) (function, `0x00A1E7DC`)
- `0x00A9A09C` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00A9A0D0` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x00A9A0F9` → [EtwpEventWriteTemplateSessionFromCapturedData](../7B/EtwpEventWriteTemplateSessionFromCapturedData_function_007B62F8.md) (function, `0x007B62F8`)
- `0x00A9A15D` → [EtwpValidateFlagExtension](../AB/EtwpValidateFlagExtension_function_00ABD15C.md) (function, `0x00ABD15C`)
- `0x00A9A195` → [EtwpLookupLoggerIdByName](../A6/EtwpLookupLoggerIdByName_function_00A60FF8.md) (function, `0x00A60FF8`)
- `0x00A9A1C6` → [ExUuidCreate](../91/ExUuidCreate_function_00917500.md) (function, `0x00917500`)
- `0x00A9A20B` → [PsGetProcessSessionId](../../text/22/PsGetProcessSessionId_function_002233A0.md) (function, `0x002233A0`)
- `0x00A9A264` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x00A9A2AA` → [RtlCreateUnicodeString](../9B/RtlCreateUnicodeString_function_009BD860.md) (function, `0x009BD860`)
- `0x00A9A2F6` → [ExAcquireRundownProtectionCacheAwareEx](../../text/41/ExAcquireRundownProtectionCacheAwareEx_function_00411F50.md) (function, `0x00411F50`)
- `0x00A9A310` → [EtwpGetSecurityDescriptorByGuid](../8C/EtwpGetSecurityDescriptorByGuid_function_008C04C0.md) (function, `0x008C04C0`)
- `0x00A9A31F` → [EtwpAccessCheck](../8C/EtwpAccessCheck_function_008C6C2C.md) (function, `0x008C6C2C`)
- `0x00A9A33C` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x00A9A356` → [EtwpEventWriteTemplateSessionDesiredAccess](../7B/EtwpEventWriteTemplateSessionDesiredAccess_function_007B6260.md) (function, `0x007B6260`)
- `0x00A9A37D` → [EtwpGetFlagExtension](../A6/EtwpGetFlagExtension_function_00A67748.md) (function, `0x00A67748`)
- `0x00A9A397` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x00A9A3A8` → [RtlCreateUnicodeString](../9B/RtlCreateUnicodeString_function_009BD860.md) (function, `0x009BD860`)
- `0x00A9A3F7` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x00A9A408` → [RtlCreateUnicodeString](../9B/RtlCreateUnicodeString_function_009BD860.md) (function, `0x009BD860`)
- `0x00A9A43A` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (function, `0x00500080`)
- `0x00A9A478` → [EtwpAcquireLoggerContextByLoggerId](../93/EtwpAcquireLoggerContextByLoggerId_function_00932920.md) (function, `0x00932920`)
- `0x00A9A4A1` → [EtwpReleaseLoggerContext](../A0/EtwpReleaseLoggerContext_function_00A04160.md) (function, `0x00A04160`)
- `0x00A9A4B6` → [EtwpReleaseLoggerContext](../A0/EtwpReleaseLoggerContext_function_00A04160.md) (function, `0x00A04160`)
- `0x00A9A54A` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (function, `0x0041C720`)
- `0x00A9A569` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (function, `0x0042EAA0`)
- `0x00A9A5D2` → [tlgWriteAgg](../../text/2F/tlgWriteAgg_function_002F0F7C.md) (function, `0x002F0F7C`)
- `0x00A9A5EA` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x00A9A607` → [EtwpEventWriteTemplateSessionMaxLoggers](../7B/EtwpEventWriteTemplateSessionMaxLoggers_function_007B63C4.md) (function, `0x007B63C4`)
- `0x00A9A642` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (function, `0x006C6B10`)
- `0x00A9A683` → [EtwpCheckGuidAccess](../8C/EtwpCheckGuidAccess_function_008C697C.md) (function, `0x008C697C`)
- `0x00A9A6CF` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x00A9A6EE` → [EtwpEventWriteTemplateSessionMaxLoggers](../7B/EtwpEventWriteTemplateSessionMaxLoggers_function_007B63C4.md) (function, `0x007B63C4`)
- `0x00A9A704` → [EtwpInitLoggerContext](../A7/EtwpInitLoggerContext_function_00A7154C.md) (function, `0x00A7154C`)
- `0x00A9A714` → [EtwpGetFlagExtension](../A6/EtwpGetFlagExtension_function_00A67748.md) (function, `0x00A67748`)
- `0x00A9A743` → [EtwpSetPartitionContext](../../text/65/EtwpSetPartitionContext_function_00652C3C.md) (function, `0x00652C3C`)
- `0x00A9A760` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x00A9A772` → [EtwpEventWriteTemplateSessionAndHandle](../7B/EtwpEventWriteTemplateSessionAndHandle_function_007B61D0.md) (function, `0x007B61D0`)
- `0x00A9A794` → [EtwpFreeApcPool](../../text/4A/EtwpFreeApcPool_function_004A5998.md) (function, `0x004A5998`)
- `0x00A9A7AC` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A9A7CB` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x00A9A7D7` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x00A9A7E8` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x00A9A7F2` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A9A809` → [ExReleaseRundownProtectionCacheAwareEx](../../text/25/ExReleaseRundownProtectionCacheAwareEx_function_0025F050.md) (function, `0x0025F050`)
- `0x00A9A820` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x00A9A86C` → [EtwpSetQpcDeltaTracking](../../text/4C/EtwpSetQpcDeltaTracking_function_004C0660.md) (function, `0x004C0660`)
- `0x00A9A90C` → [EtwpCaptureString](../9B/EtwpCaptureString_function_009BD754.md) (function, `0x009BD754`)
- `0x00A9A959` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00A9A96B` → [EtwpGenerateFileName](EtwpGenerateFileName_function_00A962C8.md) (function, `0x00A962C8`)
- `0x00A9A97E` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00A9A983` → [Feature_1899207995__private_IsEnabledDeviceUsageNoInline](../../text/64/Feature_1899207995__private_IsEnabledDeviceUsageNoInline_function_0064F398.md) (function, `0x0064F398`)
- `0x00A9A9E3` → [SeCreateClientSecurity](../89/SeCreateClientSecurity_function_008911B0.md) (function, `0x008911B0`)
- `0x00A9AA53` → [EtwpInitializeTimeStamp](../A8/EtwpInitializeTimeStamp_function_00A8F750.md) (function, `0x00A8F750`)
- `0x00A9AAC1` → [EtwpCheckForStackTracingExtension](../A6/EtwpCheckForStackTracingExtension_function_00A675F8.md) (function, `0x00A675F8`)
- `0x00A9AB82` → [EtwpCreateLogFile](../9C/EtwpCreateLogFile_function_009C035C.md) (function, `0x009C035C`)
- `0x00A9ABD1` → [EtwpAllocateTraceBufferPool](../A7/EtwpAllocateTraceBufferPool_function_00A74750.md) (function, `0x00A74750`)
- `0x00A9ABE2` → [EtwpFreeTraceBufferPool](../9C/EtwpFreeTraceBufferPool_function_009C1A74.md) (function, `0x009C1A74`)
- `0x00A9AC08` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A9AC6F` → [EtwpInitializeLoggerSecurityDescriptor](../AA/EtwpInitializeLoggerSecurityDescriptor_function_00AA7590.md) (function, `0x00AA7590`)
- `0x00A9AC7B` → [EtwpFreeSecurityDescriptor](../A1/EtwpFreeSecurityDescriptor_function_00A1E7DC.md) (function, `0x00A1E7DC`)
- `0x00A9ACA2` → [ExAcquireRundownProtectionCacheAwareEx](../../text/41/ExAcquireRundownProtectionCacheAwareEx_function_00411F50.md) (function, `0x00411F50`)
- `0x00A9ACB9` → [PsGetCurrentServerSilo](../../text/22/PsGetCurrentServerSilo_function_00225710.md) (function, `0x00225710`)
- `0x00A9ACC4` → [EtwpStartLoggerThread](../../text/4B/EtwpStartLoggerThread_function_004B25C4.md) (function, `0x004B25C4`)
- `0x00A9ACDD` → [ExReleaseRundownProtectionCacheAwareEx](../../text/25/ExReleaseRundownProtectionCacheAwareEx_function_0025F050.md) (function, `0x0025F050`)
- `0x00A9ACE5` → [EtwpFreeLoggerContext](../9C/EtwpFreeLoggerContext_function_009C1688.md) (function, `0x009C1688`)
- `0x00A9ACFD` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x00A9AD10` → [EtwpEventWriteTemplateSession](../9B/EtwpEventWriteTemplateSession_function_009BD120.md) (function, `0x009BD120`)
- `0x00A9AD29` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (function, `0x0020E6B0`)
- `0x00A9AD43` → [EtwpSendSessionNotification](../9B/EtwpSendSessionNotification_function_009BFE28.md) (function, `0x009BFE28`)
- `0x00A9AD63` → [EtwpCheckForPoolTagFilterExtension](../A6/EtwpCheckForPoolTagFilterExtension_function_00A676B0.md) (function, `0x00A676B0`)
- `0x00A9AD90` → [EtwpUpdateLoggerGroupMasks](../A6/EtwpUpdateLoggerGroupMasks_function_00A67490.md) (function, `0x00A67490`)
- `0x00A9ADA1` → [EtwpStopLoggerInstance](../9B/EtwpStopLoggerInstance_function_009BEB94.md) (function, `0x009BEB94`)
- `0x00A9ADB5` → [EtwpGetLoggerInfoFromContext](../8B/EtwpGetLoggerInfoFromContext_function_008BEF90.md) (function, `0x008BEF90`)
- `0x00A9ADC0` → [EtwpReleaseLoggerContext](../A0/EtwpReleaseLoggerContext_function_00A04160.md) (function, `0x00A04160`)
- `0x00A9ADDF` → [EtwpUpdatePerProcessTracing](../A6/EtwpUpdatePerProcessTracing_function_00A67374.md) (function, `0x00A67374`)
- `0x00A9ADEA` → [EtwpGetLoggerInfoFromContext](../8B/EtwpGetLoggerInfoFromContext_function_008BEF90.md) (function, `0x008BEF90`)
- `0x00A9ADF5` → [EtwpReleaseLoggerContext](../A0/EtwpReleaseLoggerContext_function_00A04160.md) (function, `0x00A04160`)

### Direct callers
- [EtwStartAutoLogger](../7B/EtwStartAutoLogger_function_007BD2F8.md) at `0x007BE07B`
- [EtwpStartTrace](EtwpStartTrace_function_00A99D08.md) at `0x00A99D51`
- [EtwpStartBootLogger](../../init/C4/EtwpStartBootLogger_function_00C4F274.md) at `0x00C4F417`

### Static image references
- `0x00A99D9C` → RVA `0x00E0A740` (`.data`; read)
- `0x00A99FB2` → RVA `0x00011F40` (`.rdata`; read)
- `0x00A99FBF` → RVA `0x00011F48` (`.rdata`; read)
- `0x00A99FCC` → RVA `0x0002B0D0` (`.rdata`; read)
- `0x00A99FD9` → RVA `0x0002B0D8` (`.rdata`; read)
- `0x00A9A018` → RVA `0x00FD9F38` (`PAGEDATA`; read)
- `0x00A9A03A` → RVA `0x00EFF840` (`.data`; read)
- `0x00A9A041` → RVA `0x00022218` (`.rdata`; read)
- `0x00A9A0C4` → RVA `0x00022BB8` (`.rdata`; read)
- `0x00A9A10B` → RVA `0x00EFF284` (`.data`; read)
- `0x00A9A140` → RVA `0x000112D0` (`.rdata`; read)
- `0x00A9A14D` → RVA `0x000112D8` (`.rdata`; read)
- `0x00A9A287` → RVA `0x00B071B0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00A9A29A` → RVA `0x00B07170` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00A9A335` → RVA `0x00022348` (`.rdata`; read)
- `0x00A9A360` → RVA `0x00B5A0B0` (`GlobalLoggerGuid`; read)
- `0x00A9A369` → RVA `0x00B5A0B8` (`PAGE`; read)
- `0x00A9A3CD` → RVA `0x0002B1C0` (`.rdata`; read)
- `0x00A9A3D6` → RVA `0x0002B1C8` (`.rdata`; read)
- `0x00A9A3FC` → RVA `0x00B07140` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00A9A50A` → RVA `0x00E3EC39` (`.data`; read)
- `0x00A9A525` → RVA `0x00023130` (`.rdata`; read)
- `0x00A9A530` → RVA `0x00E3EC39` (`.data`; write)
- `0x00A9A54F` → RVA `0x00E09168` (`.data`; read)
- `0x00A9A592` → RVA `0x00053C9C` (`.rdata`; read)
- `0x00A9A5DE` → RVA `0x000235C0` (`.rdata`; read)
- `0x00A9A611` → RVA `0x0002B180` (`.rdata`; read)
- `0x00A9A61E` → RVA `0x0002B188` (`.rdata`; read)
- `0x00A9A63B` → RVA `0x0002B020` (`.rdata`; read)
- `0x00A9A6C3` → RVA `0x00021700` (`.rdata`; read)
- `0x00A9A759` → RVA `0x00021208` (`.rdata`; read)
- `0x00A9A7BD` → RVA `0x00E28F90` (`.data`; read/write)
- `0x00A9ACF6` → RVA `0x00013D78` (`.rdata`; read)
- `0x00A9AD51` → RVA `0x00FC6AA8` (`ALMOSTRO`; read)
- `0x00A9AD72` → RVA `0x00EFF880` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **33**
  - `0x00A99DEB` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00A99DF7` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00A9A048` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (`PAGE` → `.text`)
  - `0x00A9A09C` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x00A9A0D0` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (`PAGE` → `.text`)
  - `0x00A9A20B` → [PsGetProcessSessionId](../../text/22/PsGetProcessSessionId_function_002233A0.md) (`PAGE` → `.text`)
  - `0x00A9A2F6` → [ExAcquireRundownProtectionCacheAwareEx](../../text/41/ExAcquireRundownProtectionCacheAwareEx_function_00411F50.md) (`PAGE` → `.text`)
  - `0x00A9A33C` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (`PAGE` → `.text`)
  - `0x00A9A43A` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (`PAGE` → `.text`)
  - `0x00A9A54A` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (`PAGE` → `.text`)
  - `0x00A9A569` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (`PAGE` → `.text`)
  - `0x00A9A5D2` → [tlgWriteAgg](../../text/2F/tlgWriteAgg_function_002F0F7C.md) (`PAGE` → `.text`)
  - `0x00A9A5EA` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (`PAGE` → `.text`)
  - `0x00A9A642` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (`PAGE` → `.text`)
  - `0x00A9A6CF` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (`PAGE` → `.text`)
  - `0x00A9A743` → [EtwpSetPartitionContext](../../text/65/EtwpSetPartitionContext_function_00652C3C.md) (`PAGE` → `.text`)
  - `0x00A9A760` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (`PAGE` → `.text`)
  - `0x00A9A794` → [EtwpFreeApcPool](../../text/4A/EtwpFreeApcPool_function_004A5998.md) (`PAGE` → `.text`)
  - `0x00A9A7AC` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A9A7E8` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x00A9A7F2` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A9A809` → [ExReleaseRundownProtectionCacheAwareEx](../../text/25/ExReleaseRundownProtectionCacheAwareEx_function_0025F050.md) (`PAGE` → `.text`)
  - `0x00A9A86C` → [EtwpSetQpcDeltaTracking](../../text/4C/EtwpSetQpcDeltaTracking_function_004C0660.md) (`PAGE` → `.text`)
  - `0x00A9A959` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00A9A97E` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00A9A983` → [Feature_1899207995__private_IsEnabledDeviceUsageNoInline](../../text/64/Feature_1899207995__private_IsEnabledDeviceUsageNoInline_function_0064F398.md) (`PAGE` → `.text`)
  - `0x00A9AC08` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A9ACA2` → [ExAcquireRundownProtectionCacheAwareEx](../../text/41/ExAcquireRundownProtectionCacheAwareEx_function_00411F50.md) (`PAGE` → `.text`)
  - `0x00A9ACB9` → [PsGetCurrentServerSilo](../../text/22/PsGetCurrentServerSilo_function_00225710.md) (`PAGE` → `.text`)
  - `0x00A9ACC4` → [EtwpStartLoggerThread](../../text/4B/EtwpStartLoggerThread_function_004B25C4.md) (`PAGE` → `.text`)
  - `0x00A9ACDD` → [ExReleaseRundownProtectionCacheAwareEx](../../text/25/ExReleaseRundownProtectionCacheAwareEx_function_0025F050.md) (`PAGE` → `.text`)
  - `0x00A9ACFD` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (`PAGE` → `.text`)
  - `0x00A9AD29` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A99D80  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
00A99D85  55                              push rbp
00A99D86  56                              push rsi
00A99D87  57                              push rdi
00A99D88  41 54                           push r12
00A99D8A  41 55                           push r13
00A99D8C  41 56                           push r14
00A99D8E  41 57                           push r15
00A99D90  48 8D 6C 24 D0                  lea rbp, [rsp - 0x30]
00A99D95  48 81 EC 30 01 00 00            sub rsp, 0x130
00A99D9C  48 8B 05 9D 09 37 00            mov rax, qword ptr [rip + 0x37099d]
00A99DA3  48 33 C4                        xor rax, rsp
00A99DA6  48 89 45 20                     mov qword ptr [rbp + 0x20], rax
00A99DAA  33 DB                           xor ebx, ebx
00A99DAC  48 89 4C 24 68                  mov qword ptr [rsp + 0x68], rcx
00A99DB1  0F 57 C0                        xorps xmm0, xmm0
00A99DB4  89 5C 24 44                     mov dword ptr [rsp + 0x44], ebx
00A99DB8  4C 8B F2                        mov r14, rdx
00A99DBB  66 89 5D 92                     mov word ptr [rbp - 0x6e], bx
00A99DBF  4C 8B E9                        mov r13, rcx
00A99DC2  48 89 5C 24 70                  mov qword ptr [rsp + 0x70], rbx
00A99DC7  0F 57 C9                        xorps xmm1, xmm1
00A99DCA  89 5C 24 60                     mov dword ptr [rsp + 0x60], ebx
00A99DCE  33 D2                           xor edx, edx
00A99DD0  C7 44 24 40 08 00 00 00         mov dword ptr [rsp + 0x40], 8
00A99DD8  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
00A99DDD  0F 11 45 B0                     movups xmmword ptr [rbp - 0x50], xmm0
00A99DE1  0F 11 44 24 78                  movups xmmword ptr [rsp + 0x78], xmm0
00A99DE6  0F 11 4C 24 50                  movups xmmword ptr [rsp + 0x50], xmm1
00A99DEB  E8 90 09 99 FF                  call 0x14042a780
00A99DF0  33 D2                           xor edx, edx
00A99DF2  48 8D 4C 24 78                  lea rcx, [rsp + 0x78]
00A99DF7  E8 84 09 99 FF                  call 0x14042a780
00A99DFC  45 8B 7E 40                     mov r15d, dword ptr [r14 + 0x40]
00A99E00  44 8D 63 01                     lea r12d, [rbx + 1]
00A99E04  41 81 E7 FF E5 EC 9D            and r15d, 0x9dece5ff
00A99E0B  41 F6 C7 03                     test r15b, 3
00A99E0F  75 0F                           jne 0x140a99e20
00A99E11  41 F6 C7 08                     test r15b, 8
00A99E15  75 06                           jne 0x140a99e1d
00A99E17  41 F6 C7 04                     test r15b, 4
00A99E1B  74 03                           je 0x140a99e20
00A99E1D  45 0B FC                        or r15d, r12d
00A99E20  41 0F BA E7 12                  bt r15d, 0x12
00A99E25  73 05                           jae 0x140a99e2c
00A99E27  41 0F BA EF 07                  bts r15d, 7
00A99E2C  41 0F BA E7 13                  bt r15d, 0x13
00A99E31  73 0C                           jae 0x140a99e3f
00A99E33  41 0F BA E7 18                  bt r15d, 0x18
00A99E38  73 05                           jae 0x140a99e3f
00A99E3A  41 0F BA F7 18                  btr r15d, 0x18
00A99E3F  49 8D 8E 90 00 00 00            lea rcx, [r14 + 0x90]
00A99E46  66 39 19                        cmp word ptr [rcx], bx
00A99E49  0F 86 E6 01 00 00               jbe 0x140a9a035
00A99E4F  49 39 9E 98 00 00 00            cmp qword ptr [r14 + 0x98], rbx
00A99E56  0F 84 D9 01 00 00               je 0x140a9a035
00A99E5C  48 8D 54 24 50                  lea rdx, [rsp + 0x50]
00A99E61  E8 EE 38 F2 FF                  call 0x1409bd754
00A99E66  8B F8                           mov edi, eax
00A99E68  85 C0                           test eax, eax
00A99E6A  0F 85 CA 01 00 00               jne 0x140a9a03a
00A99E70  41 0F BA E7 0A                  bt r15d, 0xa
00A99E75  BE 00 01 00 00                  mov esi, 0x100
00A99E7A  73 35                           jae 0x140a99eb1
00A99E7C  49 39 9E 88 00 00 00            cmp qword ptr [r14 + 0x88], rbx
00A99E83  0F 85 AC 01 00 00               jne 0x140a9a035
00A99E89  41 F6 C7 0F                     test r15b, 0xf
00A99E8D  0F 85 A2 01 00 00               jne 0x140a9a035
00A99E93  44 85 FE                        test esi, r15d
00A99E96  74 05                           je 0x140a99e9d
00A99E98  41 0F BA F7 08                  btr r15d, 8
00A99E9D  41 39 5E 44                     cmp dword ptr [r14 + 0x44], ebx
00A99EA1  74 04                           je 0x140a99ea7
00A99EA3  41 89 5E 44                     mov dword ptr [r14 + 0x44], ebx
00A99EA7  41 39 5E 4C                     cmp dword ptr [r14 + 0x4c], ebx
00A99EAB  74 04                           je 0x140a99eb1
00A99EAD  41 89 5E 4C                     mov dword ptr [r14 + 0x4c], ebx
00A99EB1  41 8B C7                        mov eax, r15d
00A99EB4  83 E0 03                        and eax, 3
00A99EB7  3C 03                           cmp al, 3
00A99EB9  0F 84 76 01 00 00               je 0x140a9a035
00A99EBF  B9 00 C0 00 00                  mov ecx, 0xc000
00A99EC4  41 8B C7                        mov eax, r15d
00A99EC7  23 C1                           and eax, ecx
00A99EC9  3B C1                           cmp eax, ecx
00A99ECB  0F 84 64 01 00 00               je 0x140a9a035
00A99ED1  41 F7 C7 00 07 00 00            test r15d, 0x700
00A99ED8  75 0D                           jne 0x140a99ee7
00A99EDA  49 39 9E 88 00 00 00            cmp qword ptr [r14 + 0x88], rbx
00A99EE1  0F 84 4E 01 00 00               je 0x140a9a035
00A99EE7  41 8B C7                        mov eax, r15d
00A99EEA  83 E0 06                        and eax, 6
00A99EED  3C 06                           cmp al, 6
00A99EEF  0F 84 40 01 00 00               je 0x140a9a035
00A99EF5  41 B8 02 00 00 00               mov r8d, 2
00A99EFB  45 84 F8                        test r8b, r15b
00A99EFE  74 0A                           je 0x140a99f0a
00A99F00  41 39 5E 3C                     cmp dword ptr [r14 + 0x3c], ebx
00A99F04  0F 84 2B 01 00 00               je 0x140a9a035
00A99F0A  B9 0C 00 00 00                  mov ecx, 0xc
00A99F0F  41 F6 C7 20                     test r15b, 0x20
00A99F13  74 16                           je 0x140a99f2b
00A99F15  41 39 5E 3C                     cmp dword ptr [r14 + 0x3c], ebx
00A99F19  0F 84 16 01 00 00               je 0x140a9a035
00A99F1F  41 8B 46 40                     mov eax, dword ptr [r14 + 0x40]
00A99F23  84 C1                           test cl, al
00A99F25  0F 85 0A 01 00 00               jne 0x140a9a035
00A99F2B  41 F6 C7 40                     test r15b, 0x40
00A99F2F  74 2C                           je 0x140a99f5d
00A99F31  41 8B 46 70                     mov eax, dword ptr [r14 + 0x70]
00A99F35  41 84 C0                        test r8b, al
00A99F38  0F 84 F7 00 00 00               je 0x140a9a035
00A99F3E  41 F7 C7 02 04 00 00            test r15d, 0x402
00A99F45  75 16                           jne 0x140a99f5d
00A99F47  44 85 FE                        test esi, r15d
00A99F4A  0F 84 E5 00 00 00               je 0x140a9a035
00A99F50  49 39 9E 88 00 00 00            cmp qword ptr [r14 + 0x88], rbx
00A99F57  0F 85 D8 00 00 00               jne 0x140a9a035
00A99F5D  B9 00 00 C0 00                  mov ecx, 0xc00000
00A99F62  41 8B C7                        mov eax, r15d
00A99F65  23 C1                           and eax, ecx
00A99F67  3B C1                           cmp eax, ecx
00A99F69  0F 84 C6 00 00 00               je 0x140a9a035
00A99F6F  41 F6 C7 08                     test r15b, 8
00A99F73  74 73                           je 0x140a99fe8
00A99F75  49 39 9E 88 00 00 00            cmp qword ptr [r14 + 0x88], rbx
00A99F7C  0F 84 B3 00 00 00               je 0x140a9a035
00A99F82  45 84 F8                        test r8b, r15b
00A99F85  0F 85 AA 00 00 00               jne 0x140a9a035
00A99F8B  41 39 5E 3C                     cmp dword ptr [r14 + 0x3c], ebx
00A99F8F  0F 84 A0 00 00 00               je 0x140a9a035
00A99F95  41 8B 46 70                     mov eax, dword ptr [r14 + 0x70]
00A99F99  41 84 C0                        test r8b, al
00A99F9C  0F 85 93 00 00 00               jne 0x140a9a035
00A99FA2  41 0F BA 66 40 19               bt dword ptr [r14 + 0x40], 0x19
00A99FA8  0F 82 87 00 00 00               jb 0x140a9a035
00A99FAE  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
00A99FB2  48 3B 05 87 7F 57 FF            cmp rax, qword ptr [rip - 0xa88079]
00A99FB9  75 0D                           jne 0x140a99fc8
00A99FBB  49 8B 46 20                     mov rax, qword ptr [r14 + 0x20]
00A99FBF  48 3B 05 82 7F 57 FF            cmp rax, qword ptr [rip - 0xa8807e]
00A99FC6  74 6D                           je 0x140a9a035
00A99FC8  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
00A99FCC  48 3B 05 FD 10 59 FF            cmp rax, qword ptr [rip - 0xa6ef03]
00A99FD3  75 0D                           jne 0x140a99fe2
00A99FD5  49 8B 46 20                     mov rax, qword ptr [r14 + 0x20]
00A99FD9  48 3B 05 F8 10 59 FF            cmp rax, qword ptr [rip - 0xa6ef08]
00A99FE0  74 53                           je 0x140a9a035
00A99FE2  41 F6 C7 04                     test r15b, 4
00A99FE6  75 4D                           jne 0x140a9a035
00A99FE8  41 8B 4E 40                     mov ecx, dword ptr [r14 + 0x40]
00A99FEC  BA 00 00 00 03                  mov edx, 0x3000000
00A99FF1  8B C1                           mov eax, ecx
00A99FF3  23 C2                           and eax, edx
00A99FF5  3B C2                           cmp eax, edx
00A99FF7  74 3C                           je 0x140a9a035
00A99FF9  0F BA E1 1A                     bt ecx, 0x1a
00A99FFD  73 08                           jae 0x140a9a007
00A99FFF  F7 C1 06 01 00 00               test ecx, 0x106
00A9A005  75 2E                           jne 0x140a9a035
00A9A007  0F BA E1 10                     bt ecx, 0x10
00A9A00B  72 28                           jb 0x140a9a035
00A9A00D  41 F6 46 50 04                  test byte ptr [r14 + 0x50], 4
00A9A012  0F 84 EB 00 00 00               je 0x140a9a103
00A9A018  48 39 1D 19 FF 53 00            cmp qword ptr [rip + 0x53ff19], rbx
00A9A01F  0F 84 98 00 00 00               je 0x140a9a0bd
00A9A025  0F BA E1 0A                     bt ecx, 0xa
00A9A029  73 0A                           jae 0x140a9a035
00A9A02B  0F BA E1 18                     bt ecx, 0x18
00A9A02F  0F 83 CE 00 00 00               jae 0x140a9a103
00A9A035  BF 0D 00 00 C0                  mov edi, 0xc000000d
00A9A03A  48 8B 0D FF 57 46 00            mov rcx, qword ptr [rip + 0x4657ff]
00A9A041  48 8D 15 D0 81 58 FF            lea rdx, [rip - 0xa77e30]
00A9A048  E8 03 84 8F FF                  call 0x140392450
00A9A04D  84 C0                           test al, al
00A9A04F  74 24                           je 0x140a9a075
00A9A051  44 89 7C 24 30                  mov dword ptr [rsp + 0x30], r15d
00A9A056  48 8D 44 24 78                  lea rax, [rsp + 0x78]
00A9A05B  89 7C 24 28                     mov dword ptr [rsp + 0x28], edi
00A9A05F  4C 8D 4C 24 50                  lea r9, [rsp + 0x50]
00A9A064  48 8D 15 AD 81 58 FF            lea rdx, [rip - 0xa77e53]
00A9A06B  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A9A070  E8 0B B8 00 00                  call 0x140aa5880
00A9A075  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
00A9A07A  E8 81 67 F2 FF                  call 0x1409c0800
00A9A07F  48 8D 4C 24 78                  lea rcx, [rsp + 0x78]
00A9A084  E8 77 67 F2 FF                  call 0x1409c0800
00A9A089  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
00A9A08E  E8 49 47 F8 FF                  call 0x140a1e7dc
00A9A093  8B C7                           mov eax, edi
00A9A095  48 8B 4D 20                     mov rcx, qword ptr [rbp + 0x20]
00A9A099  48 33 CC                        xor rcx, rsp
00A9A09C  E8 9F 25 C1 FF                  call 0x1406ac640
00A9A0A1  48 8B 9C 24 80 01 00 00         mov rbx, qword ptr [rsp + 0x180]
00A9A0A9  48 81 C4 30 01 00 00            add rsp, 0x130
00A9A0B0  41 5F                           pop r15
00A9A0B2  41 5E                           pop r14
00A9A0B4  41 5D                           pop r13
00A9A0B6  41 5C                           pop r12
00A9A0B8  5F                              pop rdi
00A9A0B9  5E                              pop rsi
00A9A0BA  5D                              pop rbp
00A9A0BB  C3                              ret
00A9A0BC  CC                              int3
00A9A0BD  48 8B 0D 7C 57 46 00            mov rcx, qword ptr [rip + 0x46577c]
00A9A0C4  48 8D 15 ED 8A 58 FF            lea rdx, [rip - 0xa77513]
00A9A0CB  BF BB 00 00 C0                  mov edi, 0xc00000bb
00A9A0D0  E8 7B 83 8F FF                  call 0x140392450
00A9A0D5  84 C0                           test al, al
00A9A0D7  0F 84 5D FF FF FF               je 0x140a9a03a
00A9A0DD  45 8B 4E 40                     mov r9d, dword ptr [r14 + 0x40]
00A9A0E1  48 8D 44 24 78                  lea rax, [rsp + 0x78]
00A9A0E6  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A9A0EB  4D 8D 46 18                     lea r8, [r14 + 0x18]
00A9A0EF  48 8D 44 24 50                  lea rax, [rsp + 0x50]
00A9A0F4  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A9A0F9  E8 FA C1 D1 FF                  call 0x1407b62f8
00A9A0FE  E9 37 FF FF FF                  jmp 0x140a9a03a
00A9A103  41 8B 46 70                     mov eax, dword ptr [r14 + 0x70]
00A9A107  85 C0                           test eax, eax
00A9A109  79 4F                           jns 0x140a9a15a
00A9A10B  38 1D 73 51 46 00               cmp byte ptr [rip + 0x465173], bl
00A9A111  0F 85 1E FF FF FF               jne 0x140a9a035
00A9A117  41 84 C0                        test r8b, al
00A9A11A  0F 84 15 FF FF FF               je 0x140a9a035
00A9A120  0F BA E1 19                     bt ecx, 0x19
00A9A124  0F 83 0B FF FF FF               jae 0x140a9a035
00A9A12A  41 8B 46 28                     mov eax, dword ptr [r14 + 0x28]
00A9A12E  41 2B C0                        sub eax, r8d
00A9A131  A9 FD FF FF FF                  test eax, 0xfffffffd
00A9A136  0F 84 F9 FE FF FF               je 0x140a9a035
00A9A13C  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
00A9A140  48 3B 05 89 71 57 FF            cmp rax, qword ptr [rip - 0xa88e77]
00A9A147  75 11                           jne 0x140a9a15a
00A9A149  49 8B 46 20                     mov rax, qword ptr [r14 + 0x20]
00A9A14D  48 3B 05 84 71 57 FF            cmp rax, qword ptr [rip - 0xa88e7c]
00A9A154  0F 84 DB FE FF FF               je 0x140a9a035
00A9A15A  49 8B CE                        mov rcx, r14
00A9A15D  E8 FA 2F 02 00                  call 0x140abd15c
00A9A162  8B F8                           mov edi, eax
00A9A164  85 C0                           test eax, eax
00A9A166  0F 88 CE FE FF FF               js 0x140a9a03a
00A9A16C  41 8B CF                        mov ecx, r15d
00A9A16F  4C 8D 44 24 44                  lea r8, [rsp + 0x44]
00A9A174  23 CE                           and ecx, esi
00A9A176  48 8D 54 24 50                  lea rdx, [rsp + 0x50]
00A9A17B  0F BA E9 0A                     bts ecx, 0xa
00A9A17F  C1 E9 03                        shr ecx, 3
00A9A182  8B F1                           mov esi, ecx
00A9A184  83 CE 40                        or esi, 0x40
00A9A187  66 41 39 9E 80 00 00 00         cmp word ptr [r14 + 0x80], bx
00A9A18F  0F 44 F1                        cmove esi, ecx
00A9A192  49 8B CD                        mov rcx, r13
00A9A195  E8 5E 6E FC FF                  call 0x140a60ff8
00A9A19A  85 C0                           test eax, eax
00A9A19C  75 0A                           jne 0x140a9a1a8
00A9A19E  BF 35 00 00 C0                  mov edi, 0xc0000035
00A9A1A3  E9 92 FE FF FF                  jmp 0x140a9a03a
00A9A1A8  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
00A9A1AC  48 3B 05 1D 71 57 FF            cmp rax, qword ptr [rip - 0xa88ee3]
00A9A1B3  75 22                           jne 0x140a9a1d7
00A9A1B5  49 8B 46 20                     mov rax, qword ptr [r14 + 0x20]
00A9A1B9  48 3B 05 18 71 57 FF            cmp rax, qword ptr [rip - 0xa88ee8]
00A9A1C0  75 15                           jne 0x140a9a1d7
00A9A1C2  48 8D 4D B0                     lea rcx, [rbp - 0x50]
00A9A1C6  E8 35 D3 E7 FF                  call 0x140917500
00A9A1CB  8B F8                           mov edi, eax
00A9A1CD  85 C0                           test eax, eax
00A9A1CF  0F 88 65 FE FF FF               js 0x140a9a03a
00A9A1D5  EB 0A                           jmp 0x140a9a1e1
00A9A1D7  41 0F 10 46 18                  movups xmm0, xmmword ptr [r14 + 0x18]
00A9A1DC  F3 0F 7F 45 B0                  movdqu xmmword ptr [rbp - 0x50], xmm0
00A9A1E1  41 F7 C7 00 00 C0 00            test r15d, 0xc00000
00A9A1E8  75 36                           jne 0x140a9a220
00A9A1EA  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00A9A1F3  38 98 32 02 00 00               cmp byte ptr [rax + 0x232], bl
00A9A1F9  74 20                           je 0x140a9a21b
00A9A1FB  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00A9A204  48 8B 89 B8 00 00 00            mov rcx, qword ptr [rcx + 0xb8]
00A9A20B  E8 90 91 78 FF                  call 0x1402233a0
00A9A210  85 C0                           test eax, eax
00A9A212  74 07                           je 0x140a9a21b
00A9A214  41 0F BA EF 16                  bts r15d, 0x16
00A9A219  EB 05                           jmp 0x140a9a220
00A9A21B  41 0F BA EF 17                  bts r15d, 0x17
00A9A220  48 8B 55 B0                     mov rdx, qword ptr [rbp - 0x50]
00A9A224  48 3B 15 15 7D 57 FF            cmp rdx, qword ptr [rip - 0xa882eb]
00A9A22B  49 8B BD C8 02 00 00            mov rdi, qword ptr [r13 + 0x2c8]
00A9A232  48 8B 4D B8                     mov rcx, qword ptr [rbp - 0x48]
00A9A236  48 89 7D 98                     mov qword ptr [rbp - 0x68], rdi
00A9A23A  75 09                           jne 0x140a9a245
00A9A23C  48 3B 0D 05 7D 57 FF            cmp rcx, qword ptr [rip - 0xa882fb]
00A9A243  74 1A                           je 0x140a9a25f
00A9A245  48 3B 15 84 0E 59 FF            cmp rdx, qword ptr [rip - 0xa6f17c]
00A9A24C  0F 85 0E 01 00 00               jne 0x140a9a360
00A9A252  48 3B 0D 7F 0E 59 FF            cmp rcx, qword ptr [rip - 0xa6f181]
00A9A259  0F 85 01 01 00 00               jne 0x140a9a360
00A9A25F  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
00A9A264  E8 97 65 F2 FF                  call 0x1409c0800
00A9A269  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
00A9A26D  48 3B 05 CC 7C 57 FF            cmp rax, qword ptr [rip - 0xa88334]
00A9A274  75 1A                           jne 0x140a9a290
00A9A276  48 8B 45 B8                     mov rax, qword ptr [rbp - 0x48]
00A9A27A  48 3B 05 C7 7C 57 FF            cmp rax, qword ptr [rip - 0xa88339]
00A9A281  75 0D                           jne 0x140a9a290
00A9A283  21 5C 24 40                     and dword ptr [rsp + 0x40], ebx
00A9A287  48 8D 15 22 CF 06 00            lea rdx, [rip + 0x6cf22]
00A9A28E  EB 11                           jmp 0x140a9a2a1
00A9A290  BB 02 00 00 00                  mov ebx, 2
00A9A295  44 89 64 24 40                  mov dword ptr [rsp + 0x40], r12d
00A9A29A  48 8D 15 CF CE 06 00            lea rdx, [rip + 0x6cecf]
00A9A2A1  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
00A9A2A6  89 5C 24 44                     mov dword ptr [rsp + 0x44], ebx
00A9A2AA  E8 B1 35 F2 FF                  call 0x1409bd860
00A9A2AF  84 C0                           test al, al
00A9A2B1  75 0A                           jne 0x140a9a2bd
00A9A2B3  BF 17 00 00 C0                  mov edi, 0xc0000017
00A9A2B8  E9 7D FD FF FF                  jmp 0x140a9a03a
00A9A2BD  41 0F BA EF 07                  bts r15d, 7
00A9A2C2  41 0F BA E7 18                  bt r15d, 0x18
00A9A2C7  0F 82 68 FD FF FF               jb 0x140a9a035
00A9A2CD  48 8B D7                        mov rdx, rdi
00A9A2D0  8B CB                           mov ecx, ebx
00A9A2D2  49 0B D4                        or rdx, r12
00A9A2D5  49 8B C4                        mov rax, r12
00A9A2D8  F0 48 0F B1 14 CF               lock cmpxchg qword ptr [rdi + rcx*8], rdx
00A9A2DE  0F 85 BA FE FF FF               jne 0x140a9a19e
00A9A2E4  8B 44 24 44                     mov eax, dword ptr [rsp + 0x44]
00A9A2E8  41 8B D4                        mov edx, r12d
00A9A2EB  49 8B 8D C0 02 00 00            mov rcx, qword ptr [r13 + 0x2c0]
00A9A2F2  48 8B 0C C1                     mov rcx, qword ptr [rcx + rax*8]
00A9A2F6  E8 55 7C 97 FF                  call 0x140411f50
00A9A2FB  33 DB                           xor ebx, ebx
00A9A2FD  41 39 5E 70                     cmp dword ptr [r14 + 0x70], ebx
00A9A301  0F 8C 0A 03 00 00               jl 0x140a9a611
00A9A307  48 8D 54 24 70                  lea rdx, [rsp + 0x70]
00A9A30C  48 8D 4D B0                     lea rcx, [rbp - 0x50]
00A9A310  E8 AB 61 E2 FF                  call 0x1408c04c0
00A9A315  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
00A9A31A  45 33 C0                        xor r8d, r8d
00A9A31D  8B D6                           mov edx, esi
00A9A31F  E8 08 C9 E2 FF                  call 0x1408c6c2c
00A9A324  8B F8                           mov edi, eax
00A9A326  85 C0                           test eax, eax
00A9A328  0F 89 E3 02 00 00               jns 0x140a9a611
00A9A32E  48 8B 0D 0B 55 46 00            mov rcx, qword ptr [rip + 0x46550b]
00A9A335  48 8D 15 0C 80 58 FF            lea rdx, [rip - 0xa77ff4]
00A9A33C  E8 0F 81 8F FF                  call 0x140392450
00A9A341  84 C0                           test al, al
00A9A343  0F 84 AE 04 00 00               je 0x140a9a7f7
00A9A349  4C 8D 4D B0                     lea r9, [rbp - 0x50]
00A9A34D  89 74 24 20                     mov dword ptr [rsp + 0x20], esi
00A9A351  4C 8D 44 24 50                  lea r8, [rsp + 0x50]
00A9A356  E8 05 BF D1 FF                  call 0x1407b6260
00A9A35B  E9 97 04 00 00                  jmp 0x140a9a7f7
00A9A360  48 3B 15 49 FD 0B 00            cmp rdx, qword ptr [rip + 0xbfd49]
00A9A367  75 64                           jne 0x140a9a3cd
00A9A369  48 3B 0D 48 FD 0B 00            cmp rcx, qword ptr [rip + 0xbfd48]
00A9A370  75 5B                           jne 0x140a9a3cd
00A9A372  41 8B D4                        mov edx, r12d
00A9A375  44 89 64 24 44                  mov dword ptr [rsp + 0x44], r12d
00A9A37A  49 8B CE                        mov rcx, r14
00A9A37D  E8 C6 D3 FC FF                  call 0x140a67748
00A9A382  48 85 C0                        test rax, rax
00A9A385  74 32                           je 0x140a9a3b9
00A9A387  41 0F BA E7 18                  bt r15d, 0x18
00A9A38C  0F 82 A3 FC FF FF               jb 0x140a9a035
00A9A392  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
00A9A397  E8 64 64 F2 FF                  call 0x1409c0800
00A9A39C  48 8D 15 0D CE 06 00            lea rdx, [rip + 0x6ce0d]
00A9A3A3  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
00A9A3A8  E8 B3 34 F2 FF                  call 0x1409bd860
00A9A3AD  84 C0                           test al, al
00A9A3AF  0F 84 FE FE FF FF               je 0x140a9a2b3
00A9A3B5  89 5C 24 40                     mov dword ptr [rsp + 0x40], ebx
00A9A3B9  48 8B CF                        mov rcx, rdi
00A9A3BC  49 8B C4                        mov rax, r12
00A9A3BF  49 0B CC                        or rcx, r12
00A9A3C2  F0 48 0F B1 4F 08               lock cmpxchg qword ptr [rdi + 8], rcx
00A9A3C8  E9 11 FF FF FF                  jmp 0x140a9a2de
00A9A3CD  48 3B 15 EC 0D 59 FF            cmp rdx, qword ptr [rip - 0xa6f214]
00A9A3D4  75 58                           jne 0x140a9a42e
00A9A3D6  48 3B 0D EB 0D 59 FF            cmp rcx, qword ptr [rip - 0xa6f215]
00A9A3DD  75 4F                           jne 0x140a9a42e
00A9A3DF  C7 44 24 44 03 00 00 00         mov dword ptr [rsp + 0x44], 3
00A9A3E7  41 0F BA E7 18                  bt r15d, 0x18
00A9A3EC  0F 82 43 FC FF FF               jb 0x140a9a035
00A9A3F2  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
00A9A3F7  E8 04 64 F2 FF                  call 0x1409c0800
00A9A3FC  48 8D 15 3D CD 06 00            lea rdx, [rip + 0x6cd3d]
00A9A403  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
00A9A408  E8 53 34 F2 FF                  call 0x1409bd860
00A9A40D  84 C0                           test al, al
00A9A40F  0F 84 9E FE FF FF               je 0x140a9a2b3
00A9A415  41 0F BA EF 07                  bts r15d, 7
00A9A41A  48 8B CF                        mov rcx, rdi
00A9A41D  49 0B CC                        or rcx, r12
00A9A420  49 8B C4                        mov rax, r12
00A9A423  F0 48 0F B1 4F 18               lock cmpxchg qword ptr [rdi + 0x18], rcx
00A9A429  E9 B0 FE FF FF                  jmp 0x140a9a2de
00A9A42E  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00A9A433  48 8D 15 06 CD 06 00            lea rdx, [rip + 0x6cd06]
00A9A43A  E8 41 5C A6 FF                  call 0x140500080
00A9A43F  85 C0                           test eax, eax
00A9A441  75 22                           jne 0x140a9a465
00A9A443  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
00A9A447  48 3B 05 72 0D 59 FF            cmp rax, qword ptr [rip - 0xa6f28e]
00A9A44E  0F 85 4A FD FF FF               jne 0x140a9a19e
00A9A454  48 8B 45 B8                     mov rax, qword ptr [rbp - 0x48]
00A9A458  48 3B 05 69 0D 59 FF            cmp rax, qword ptr [rip - 0xa6f297]
00A9A45F  0F 85 39 FD FF FF               jne 0x140a9a19e
00A9A465  BB 04 00 00 00                  mov ebx, 4
00A9A46A  41 39 5D 10                     cmp dword ptr [r13 + 0x10], ebx
00A9A46E  76 4B                           jbe 0x140a9a4bb
00A9A470  45 33 C0                        xor r8d, r8d
00A9A473  8B D3                           mov edx, ebx
00A9A475  49 8B CD                        mov rcx, r13
00A9A478  E8 A3 84 E9 FF                  call 0x140932920
00A9A47D  48 85 C0                        test rax, rax
00A9A480  74 24                           je 0x140a9a4a6
00A9A482  48 8B 88 14 01 00 00            mov rcx, qword ptr [rax + 0x114]
00A9A489  48 3B 4D B0                     cmp rcx, qword ptr [rbp - 0x50]
00A9A48D  75 0D                           jne 0x140a9a49c
00A9A48F  48 8B 88 1C 01 00 00            mov rcx, qword ptr [rax + 0x11c]
00A9A496  48 3B 4D B8                     cmp rcx, qword ptr [rbp - 0x48]
00A9A49A  74 15                           je 0x140a9a4b1
00A9A49C  33 D2                           xor edx, edx
00A9A49E  48 8B C8                        mov rcx, rax
00A9A4A1  E8 BA 9C F6 FF                  call 0x140a04160
00A9A4A6  41 03 DC                        add ebx, r12d
00A9A4A9  41 3B 5D 10                     cmp ebx, dword ptr [r13 + 0x10]
00A9A4AD  72 C1                           jb 0x140a9a470
00A9A4AF  EB 0A                           jmp 0x140a9a4bb
00A9A4B1  33 D2                           xor edx, edx
00A9A4B3  48 8B C8                        mov rcx, rax
00A9A4B6  E8 A5 9C F6 FF                  call 0x140a04160
00A9A4BB  41 8B 45 10                     mov eax, dword ptr [r13 + 0x10]
00A9A4BF  3B D8                           cmp ebx, eax
00A9A4C1  0F 82 D7 FC FF FF               jb 0x140a9a19e
00A9A4C7  C7 44 24 44 04 00 00 00         mov dword ptr [rsp + 0x44], 4
00A9A4CF  83 F8 04                        cmp eax, 4
00A9A4D2  76 26                           jbe 0x140a9a4fa
00A9A4D4  48 8B D7                        mov rdx, rdi
00A9A4D7  49 0B D4                        or rdx, r12
00A9A4DA  8B 4C 24 44                     mov ecx, dword ptr [rsp + 0x44]
00A9A4DE  49 8B C4                        mov rax, r12
00A9A4E1  F0 48 0F B1 14 CF               lock cmpxchg qword ptr [rdi + rcx*8], rdx
00A9A4E7  74 11                           je 0x140a9a4fa
00A9A4E9  8B 44 24 44                     mov eax, dword ptr [rsp + 0x44]
00A9A4ED  41 03 C4                        add eax, r12d
00A9A4F0  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
00A9A4F4  41 3B 45 10                     cmp eax, dword ptr [r13 + 0x10]
00A9A4F8  72 E0                           jb 0x140a9a4da
00A9A4FA  41 8B 45 10                     mov eax, dword ptr [r13 + 0x10]
00A9A4FE  39 44 24 44                     cmp dword ptr [rsp + 0x44], eax
00A9A502  0F 82 DC FD FF FF               jb 0x140a9a2e4
00A9A508  33 DB                           xor ebx, ebx
00A9A50A  38 1D 29 47 3A 00               cmp byte ptr [rip + 0x3a4729], bl
00A9A510  0F 85 C1 00 00 00               jne 0x140a9a5d7
00A9A516  48 8B 0D 23 53 46 00            mov rcx, qword ptr [rip + 0x465323]
00A9A51D  49 8D 45 10                     lea rax, [r13 + 0x10]
00A9A521  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
00A9A525  48 8D 15 04 8C 58 FF            lea rdx, [rip - 0xa773fc]
00A9A52C  48 8D 45 C0                     lea rax, [rbp - 0x40]
00A9A530  44 88 25 02 47 3A 00            mov byte ptr [rip + 0x3a4702], r12b
00A9A537  45 8B CC                        mov r9d, r12d
00A9A53A  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A9A53F  45 33 C0                        xor r8d, r8d
00A9A542  48 C7 45 C8 04 00 00 00         mov qword ptr [rbp - 0x38], 4
00A9A54A  E8 D1 21 98 FF                  call 0x14041c720
00A9A54F  83 3D 12 EC 36 00 05            cmp dword ptr [rip + 0x36ec12], 5
00A9A556  76 7F                           jbe 0x140a9a5d7
00A9A558  48 BA 00 00 00 00 00 20 00 00   movabs rdx, 0x200000000000
00A9A562  48 8D 0D FF EB 36 00            lea rcx, [rip + 0x36ebff]
00A9A569  E8 32 45 99 FF                  call 0x14042eaa0
00A9A56E  84 C0                           test al, al
00A9A570  74 65                           je 0x140a9a5d7
00A9A572  48 8D 45 A0                     lea rax, [rbp - 0x60]
00A9A576  4C 89 65 A0                     mov qword ptr [rbp - 0x60], r12
00A9A57A  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
00A9A57E  44 8D 4B 05                     lea r9d, [rbx + 5]
00A9A582  48 8D 45 A8                     lea rax, [rbp - 0x58]
00A9A586  48 C7 45 F8 08 00 00 00         mov qword ptr [rbp - 8], 8
00A9A58E  48 89 45 00                     mov qword ptr [rbp], rax
00A9A592  48 8D 15 03 97 5B FF            lea rdx, [rip - 0xa468fd]
00A9A599  41 8B 45 10                     mov eax, dword ptr [r13 + 0x10]
00A9A59D  48 8D 0D C4 EB 36 00            lea rcx, [rip + 0x36ebc4]
00A9A5A4  89 44 24 68                     mov dword ptr [rsp + 0x68], eax
00A9A5A8  48 8D 44 24 68                  lea rax, [rsp + 0x68]
00A9A5AD  48 89 45 10                     mov qword ptr [rbp + 0x10], rax
00A9A5B1  48 8D 45 D0                     lea rax, [rbp - 0x30]
00A9A5B5  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A9A5BA  48 C7 45 A8 00 00 00 01         mov qword ptr [rbp - 0x58], 0x1000000
00A9A5C2  48 C7 45 08 08 00 00 00         mov qword ptr [rbp + 8], 8
00A9A5CA  48 C7 45 18 04 00 00 00         mov qword ptr [rbp + 0x18], 4
00A9A5D2  E8 A5 69 85 FF                  call 0x1402f0f7c
00A9A5D7  48 8B 0D 62 52 46 00            mov rcx, qword ptr [rip + 0x465262]
00A9A5DE  48 8D 15 DB 8F 58 FF            lea rdx, [rip - 0xa77025]
00A9A5E5  BF 9A 00 00 C0                  mov edi, 0xc000009a
00A9A5EA  E8 61 7E 8F FF                  call 0x140392450
00A9A5EF  84 C0                           test al, al
00A9A5F1  0F 84 43 FA FF FF               je 0x140a9a03a
00A9A5F7  45 8B 4D 10                     mov r9d, dword ptr [r13 + 0x10]
00A9A5FB  4C 8D 44 24 50                  lea r8, [rsp + 0x50]
00A9A600  48 8D 15 B9 8F 58 FF            lea rdx, [rip - 0xa77047]
00A9A607  E8 B8 BD D1 FF                  call 0x1407b63c4
00A9A60C  E9 29 FA FF FF                  jmp 0x140a9a03a
00A9A611  48 8B 05 68 0B 59 FF            mov rax, qword ptr [rip - 0xa6f498]
00A9A618  48 3B 45 B0                     cmp rax, qword ptr [rbp - 0x50]
00A9A61C  75 13                           jne 0x140a9a631
00A9A61E  48 8B 05 63 0B 59 FF            mov rax, qword ptr [rip - 0xa6f49d]
00A9A625  48 3B 45 B8                     cmp rax, qword ptr [rbp - 0x48]
00A9A629  75 06                           jne 0x140a9a631
00A9A62B  88 5C 24 48                     mov byte ptr [rsp + 0x48], bl
00A9A62F  EB 24                           jmp 0x140a9a655
00A9A631  41 B8 10 00 00 00               mov r8d, 0x10
00A9A637  48 8D 55 B0                     lea rdx, [rbp - 0x50]
00A9A63B  48 8D 0D DE 09 59 FF            lea rcx, [rip - 0xa6f622]
00A9A642  E8 C9 C4 C2 FF                  call 0x1406c6b10
00A9A647  F7 D8                           neg eax
00A9A649  1A C9                           sbb cl, cl
00A9A64B  80 E1 08                        and cl, 8
00A9A64E  41 02 CC                        add cl, r12b
00A9A651  88 4C 24 48                     mov byte ptr [rsp + 0x48], cl
00A9A655  41 F7 46 40 00 00 00 02         test dword ptr [r14 + 0x40], 0x2000000
00A9A65D  0F 84 95 00 00 00               je 0x140a9a6f8
00A9A663  83 7C 24 40 08                  cmp dword ptr [rsp + 0x40], 8
00A9A668  0F 85 8A 00 00 00               jne 0x140a9a6f8
00A9A66E  41 39 5E 70                     cmp dword ptr [r14 + 0x70], ebx
00A9A672  7C 1E                           jl 0x140a9a692
00A9A674  45 33 C0                        xor r8d, r8d
00A9A677  48 8D 0D C2 78 57 FF            lea rcx, [rip - 0xa8873e]
00A9A67E  BA 80 00 00 00                  mov edx, 0x80
00A9A683  E8 F4 C2 E2 FF                  call 0x1408c697c
00A9A688  8B F8                           mov edi, eax
00A9A68A  85 C0                           test eax, eax
00A9A68C  0F 88 65 01 00 00               js 0x140a9a7f7
00A9A692  BF 02 00 00 00                  mov edi, 2
00A9A697  89 7C 24 40                     mov dword ptr [rsp + 0x40], edi
00A9A69B  41 0F A3 BD A8 11 00 00         bt dword ptr [r13 + 0x11a8], edi
00A9A6A3  73 53                           jae 0x140a9a6f8
00A9A6A5  41 03 FC                        add edi, r12d
00A9A6A8  89 7C 24 40                     mov dword ptr [rsp + 0x40], edi
00A9A6AC  8B C7                           mov eax, edi
00A9A6AE  83 FF 08                        cmp edi, 8
00A9A6B1  72 E8                           jb 0x140a9a69b
00A9A6B3  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00A9A6B7  83 F8 08                        cmp eax, 8
00A9A6BA  75 3C                           jne 0x140a9a6f8
00A9A6BC  48 8B 0D 7D 51 46 00            mov rcx, qword ptr [rip + 0x46517d]
00A9A6C3  48 8D 15 36 70 58 FF            lea rdx, [rip - 0xa78fca]
00A9A6CA  BF 9A 00 00 C0                  mov edi, 0xc000009a
00A9A6CF  E8 7C 7D 8F FF                  call 0x140392450
00A9A6D4  84 C0                           test al, al
00A9A6D6  0F 84 1B 01 00 00               je 0x140a9a7f7
00A9A6DC  41 B9 08 00 00 00               mov r9d, 8
00A9A6E2  4C 8D 44 24 50                  lea r8, [rsp + 0x50]
00A9A6E7  48 8D 15 12 70 58 FF            lea rdx, [rip - 0xa78fee]
00A9A6EE  E8 D1 BC D1 FF                  call 0x1407b63c4
00A9A6F3  E9 FF 00 00 00                  jmp 0x140a9a7f7
00A9A6F8  45 8B 46 70                     mov r8d, dword ptr [r14 + 0x70]
00A9A6FC  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
00A9A701  41 8B D7                        mov edx, r15d
00A9A704  E8 43 6E FD FF                  call 0x140a7154c
00A9A709  BA 06 00 00 00                  mov edx, 6
00A9A70E  49 8B CE                        mov rcx, r14
00A9A711  48 8B F0                        mov rsi, rax
00A9A714  E8 2F D0 FC FF                  call 0x140a67748
00A9A719  48 8B D8                        mov rbx, rax
00A9A71C  48 85 C0                        test rax, rax
00A9A71F  0F 84 F6 00 00 00               je 0x140a9a81b
00A9A725  0F B7 08                        movzx ecx, word ptr [rax]
00A9A728  8D 42 06                        lea eax, [rdx + 6]
00A9A72B  66 C1 E1 02                     shl cx, 2
00A9A72F  66 3B C8                        cmp cx, ax
00A9A732  0F 85 E3 00 00 00               jne 0x140a9a81b
00A9A738  48 8B 53 04                     mov rdx, qword ptr [rbx + 4]
00A9A73C  48 8D 8E 40 06 00 00            lea rcx, [rsi + 0x640]
00A9A743  E8 F4 84 BB FF                  call 0x140652c3c
00A9A748  8B F8                           mov edi, eax
00A9A74A  85 C0                           test eax, eax
00A9A74C  0F 89 C9 00 00 00               jns 0x140a9a81b
00A9A752  48 8B 0D E7 50 46 00            mov rcx, qword ptr [rip + 0x4650e7]
00A9A759  48 8D 15 A8 6A 58 FF            lea rdx, [rip - 0xa79558]
00A9A760  E8 EB 7C 8F FF                  call 0x140392450
00A9A765  84 C0                           test al, al
00A9A767  74 0E                           je 0x140a9a777
00A9A769  4C 8B 4B 04                     mov r9, qword ptr [rbx + 4]
00A9A76D  4C 8D 44 24 50                  lea r8, [rsp + 0x50]
00A9A772  E8 59 BA D1 FF                  call 0x1407b61d0
00A9A777  8B 5C 24 40                     mov ebx, dword ptr [rsp + 0x40]
00A9A77B  F7 46 0C 00 00 00 02            test dword ptr [rsi + 0xc], 0x2000000
00A9A782  74 09                           je 0x140a9a78d
00A9A784  F0 41 0F B3 9D A8 11 00 00      lock btr dword ptr [r13 + 0x11a8], ebx
00A9A78D  48 8D 8E 40 03 00 00            lea rcx, [rsi + 0x340]
00A9A794  E8 FF B1 A0 FF                  call 0x1404a5998
00A9A799  8B 86 30 03 00 00               mov eax, dword ptr [rsi + 0x330]
00A9A79F  84 C0                           test al, al
00A9A7A1  79 0E                           jns 0x140a9a7b1
00A9A7A3  48 8B 8E 18 04 00 00            mov rcx, qword ptr [rsi + 0x418]
00A9A7AA  33 D2                           xor edx, edx
00A9A7AC  E8 BF 80 0E 00                  call 0x140b82870
00A9A7B1  F7 86 30 03 00 00 00 20 00 00   test dword ptr [rsi + 0x330], 0x2000
00A9A7BB  74 07                           je 0x140a9a7c4
00A9A7BD  F0 FF 0D CC E7 38 00            lock dec dword ptr [rip + 0x38e7cc]
00A9A7C4  48 8D 8E 98 00 00 00            lea rcx, [rsi + 0x98]
00A9A7CB  E8 30 60 F2 FF                  call 0x1409c0800
00A9A7D0  48 8D 8E A8 00 00 00            lea rcx, [rsi + 0xa8]
00A9A7D7  E8 24 60 F2 FF                  call 0x1409c0800
00A9A7DC  48 8B 8E 20 03 00 00            mov rcx, qword ptr [rsi + 0x320]
00A9A7E3  48 85 C9                        test rcx, rcx
00A9A7E6  74 05                           je 0x140a9a7ed
00A9A7E8  E8 C3 2A C1 FF                  call 0x1406ad2b0
00A9A7ED  33 D2                           xor edx, edx
00A9A7EF  48 8B CE                        mov rcx, rsi
00A9A7F2  E8 79 80 0E 00                  call 0x140b82870
00A9A7F7  49 8B 8D C0 02 00 00            mov rcx, qword ptr [r13 + 0x2c0]
00A9A7FE  41 8B D4                        mov edx, r12d
00A9A801  8B 5C 24 44                     mov ebx, dword ptr [rsp + 0x44]
00A9A805  48 8B 0C D9                     mov rcx, qword ptr [rcx + rbx*8]
00A9A809  E8 42 48 7C FF                  call 0x14025f050
00A9A80E  48 8B 4D 98                     mov rcx, qword ptr [rbp - 0x68]
00A9A812  4C 87 24 D9                     xchg qword ptr [rcx + rbx*8], r12
00A9A816  E9 1F F8 FF FF                  jmp 0x140a9a03a
00A9A81B  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
00A9A820  E8 DB 5F F2 FF                  call 0x1409c0800
00A9A825  45 33 C0                        xor r8d, r8d
00A9A828  48 85 F6                        test rsi, rsi
00A9A82B  75 07                           jne 0x140a9a834
00A9A82D  BF 17 00 00 C0                  mov edi, 0xc0000017
00A9A832  EB C3                           jmp 0x140a9a7f7
00A9A834  0F 10 45 B0                     movups xmm0, xmmword ptr [rbp - 0x50]
00A9A838  F3 0F 7F 86 14 01 00 00         movdqu xmmword ptr [rsi + 0x114], xmm0
00A9A840  41 8B 46 3C                     mov eax, dword ptr [r14 + 0x3c]
00A9A844  89 86 24 01 00 00               mov dword ptr [rsi + 0x124], eax
00A9A84A  45 84 66 50                     test byte ptr [r14 + 0x50], r12b
00A9A84E  74 08                           je 0x140a9a858
00A9A850  F0 83 8E 30 03 00 00 10         lock or dword ptr [rsi + 0x330], 0x10
00A9A858  41 8B 46 28                     mov eax, dword ptr [r14 + 0x28]
00A9A85C  89 86 C8 00 00 00               mov dword ptr [rsi + 0xc8], eax
00A9A862  41 F6 46 50 02                  test byte ptr [r14 + 0x50], 2
00A9A867  74 12                           je 0x140a9a87b
00A9A869  48 8B CE                        mov rcx, rsi
00A9A86C  E8 EF 5D A2 FF                  call 0x1404c0660
00A9A871  8B F8                           mov edi, eax
00A9A873  85 C0                           test eax, eax
00A9A875  0F 88 FC FE FF FF               js 0x140a9a777
00A9A87B  41 F6 46 50 08                  test byte ptr [r14 + 0x50], 8
00A9A880  74 08                           je 0x140a9a88a
00A9A882  0F BA AE 30 03 00 00 1E         bts dword ptr [rsi + 0x330], 0x1e
00A9A88A  41 8B 46 44                     mov eax, dword ptr [r14 + 0x44]
00A9A88E  85 C0                           test eax, eax
00A9A890  74 08                           je 0x140a9a89a
00A9A892  89 86 D0 00 00 00               mov dword ptr [rsi + 0xd0], eax
00A9A898  EB 1F                           jmp 0x140a9a8b9
00A9A89A  41 0F BA E7 08                  bt r15d, 8
00A9A89F  73 18                           jae 0x140a9a8b9
00A9A8A1  41 8A C7                        mov al, r15b
00A9A8A4  24 10                           and al, 0x10
00A9A8A6  F6 D8                           neg al
00A9A8A8  1B C9                           sbb ecx, ecx
00A9A8AA  81 E1 E7 03 00 00               and ecx, 0x3e7
00A9A8B0  41 03 CC                        add ecx, r12d
00A9A8B3  89 8E D0 00 00 00               mov dword ptr [rsi + 0xd0], ecx
00A9A8B9  41 8B 46 4C                     mov eax, dword ptr [r14 + 0x4c]
00A9A8BD  8B C8                           mov ecx, eax
00A9A8BF  85 C0                           test eax, eax
00A9A8C1  74 14                           je 0x140a9a8d7
00A9A8C3  44 39 86 D0 00 00 00            cmp dword ptr [rsi + 0xd0], r8d
00A9A8CA  77 04                           ja 0x140a9a8d0
00A9A8CC  85 C0                           test eax, eax
00A9A8CE  79 07                           jns 0x140a9a8d7
00A9A8D0  45 89 46 4C                     mov dword ptr [r14 + 0x4c], r8d
00A9A8D4  41 8B C8                        mov ecx, r8d
00A9A8D7  8B 44 24 44                     mov eax, dword ptr [rsp + 0x44]
00A9A8DB  41 8B F8                        mov edi, r8d
00A9A8DE  89 06                           mov dword ptr [rsi], eax
00A9A8E0  89 8E D4 00 00 00               mov dword ptr [rsi + 0xd4], ecx
00A9A8E6  4C 89 AE 50 05 00 00            mov qword ptr [rsi + 0x550], r13
00A9A8ED  66 45 39 86 80 00 00 00         cmp word ptr [r14 + 0x80], r8w
00A9A8F5  76 27                           jbe 0x140a9a91e
00A9A8F7  4D 39 86 88 00 00 00            cmp qword ptr [r14 + 0x88], r8
00A9A8FE  74 1E                           je 0x140a9a91e
00A9A900  49 8D 8E 80 00 00 00            lea rcx, [r14 + 0x80]
00A9A907  48 8D 54 24 78                  lea rdx, [rsp + 0x78]
00A9A90C  E8 43 2E F2 FF                  call 0x1409bd754
00A9A911  45 33 C0                        xor r8d, r8d
00A9A914  8B F8                           mov edi, eax
00A9A916  85 C0                           test eax, eax
00A9A918  0F 88 59 FE FF FF               js 0x140a9a777
00A9A91E  41 8B 46 70                     mov eax, dword ptr [r14 + 0x70]
00A9A922  A8 02                           test al, 2
00A9A924  74 0E                           je 0x140a9a934
00A9A926  41 8B 46 60                     mov eax, dword ptr [r14 + 0x60]
00A9A92A  89 86 28 01 00 00               mov dword ptr [rsi + 0x128], eax
00A9A930  45 89 46 60                     mov dword ptr [r14 + 0x60], r8d
00A9A934  8B 46 0C                        mov eax, dword ptr [rsi + 0xc]
00A9A937  4C 8D AE 98 00 00 00            lea r13, [rsi + 0x98]
00A9A93E  0F 10 44 24 78                  movups xmm0, xmmword ptr [rsp + 0x78]
00A9A943  33 D2                           xor edx, edx
00A9A945  48 8D 4C 24 78                  lea rcx, [rsp + 0x78]
00A9A94A  A8 08                           test al, 8
00A9A94C  74 2A                           je 0x140a9a978
00A9A94E  48 8D 9E A8 00 00 00            lea rbx, [rsi + 0xa8]
00A9A955  F3 0F 7F 03                     movdqu xmmword ptr [rbx], xmm0
00A9A959  E8 22 FE 98 FF                  call 0x14042a780
00A9A95E  48 8D 96 28 01 00 00            lea rdx, [rsi + 0x128]
00A9A965  4D 8B C5                        mov r8, r13
00A9A968  48 8B CB                        mov rcx, rbx
00A9A96B  E8 58 B9 FF FF                  call 0x140a962c8
00A9A970  8B F8                           mov edi, eax
00A9A972  85 C0                           test eax, eax
00A9A974  78 34                           js 0x140a9a9aa
00A9A976  EB 0B                           jmp 0x140a9a983
00A9A978  F3 41 0F 7F 45 00               movdqu xmmword ptr [r13], xmm0
00A9A97E  E8 FD FD 98 FF                  call 0x14042a780
00A9A983  E8 10 4A BB FF                  call 0x14064f398
00A9A988  45 33 C0                        xor r8d, r8d
00A9A98B  85 C0                           test eax, eax
00A9A98D  74 25                           je 0x140a9a9b4
00A9A98F  0F B7 8E 88 00 00 00            movzx ecx, word ptr [rsi + 0x88]
00A9A996  41 0F B7 45 00                  movzx eax, word ptr [r13]
00A9A99B  03 C8                           add ecx, eax
00A9A99D  81 F9 FF 7F 00 00               cmp ecx, 0x7fff
00A9A9A3  76 0F                           jbe 0x140a9a9b4
00A9A9A5  BF 0D 00 00 C0                  mov edi, 0xc000000d
00A9A9AA  4C 8B 6C 24 68                  mov r13, qword ptr [rsp + 0x68]
00A9A9AF  E9 C3 FD FF FF                  jmp 0x140a9a777
00A9A9B4  45 39 46 70                     cmp dword ptr [r14 + 0x70], r8d
00A9A9B8  7C 33                           jl 0x140a9a9ed
00A9A9BA  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00A9A9C3  4C 8D 8E C0 02 00 00            lea r9, [rsi + 0x2c0]
00A9A9CA  B8 0C 00 00 00                  mov eax, 0xc
00A9A9CF  C7 45 8C 02 00 00 00            mov dword ptr [rbp - 0x74], 2
00A9A9D6  48 8D 55 88                     lea rdx, [rbp - 0x78]
00A9A9DA  89 45 88                        mov dword ptr [rbp - 0x78], eax
00A9A9DD  66 C7 45 90 01 01               mov word ptr [rbp - 0x70], 0x101
00A9A9E3  E8 C8 67 DF FF                  call 0x1408911b0
00A9A9E8  8B F8                           mov edi, eax
00A9A9EA  45 33 C0                        xor r8d, r8d
00A9A9ED  85 FF                           test edi, edi
00A9A9EF  78 B9                           js 0x140a9a9aa
00A9A9F1  F7 46 0C 00 01 00 00            test dword ptr [rsi + 0xc], 0x100
00A9A9F8  74 0A                           je 0x140a9aa04
00A9A9FA  F0 83 8E 30 03 00 00 08         lock or dword ptr [rsi + 0x330], 8
00A9AA02  EB 08                           jmp 0x140a9aa0c
00A9AA04  F0 83 A6 30 03 00 00 F7         lock and dword ptr [rsi + 0x330], 0xfffffff7
00A9AA0C  41 8B 46 70                     mov eax, dword ptr [r14 + 0x70]
00A9AA10  A8 02                           test al, 2
00A9AA12  74 08                           je 0x140a9aa1c
00A9AA14  F0 83 8E 30 03 00 00 02         lock or dword ptr [rsi + 0x330], 2
00A9AA1C  45 39 46 70                     cmp dword ptr [r14 + 0x70], r8d
00A9AA20  7D 0B                           jge 0x140a9aa2d
00A9AA22  F0 81 8E 30 03 00 00 00 00 00 80  lock or dword ptr [rsi + 0x330], 0x80000000
00A9AA2D  41 8B 46 70                     mov eax, dword ptr [r14 + 0x70]
00A9AA31  41 84 C4                        test r12b, al
00A9AA34  74 08                           je 0x140a9aa3e
00A9AA36  F0 44 09 A6 30 03 00 00         lock or dword ptr [rsi + 0x330], r12d
00A9AA3E  B9 00 40 00 00                  mov ecx, 0x4000
00A9AA43  41 85 4E 70                     test dword ptr [r14 + 0x70], ecx
00A9AA47  74 07                           je 0x140a9aa50
00A9AA49  F0 09 8E 30 03 00 00            lock or dword ptr [rsi + 0x330], ecx
00A9AA50  48 8B CE                        mov rcx, rsi
00A9AA53  E8 F8 4C FF FF                  call 0x140a8f750
00A9AA58  8B 5C 24 40                     mov ebx, dword ptr [rsp + 0x40]
00A9AA5C  83 FB 08                        cmp ebx, 8
00A9AA5F  73 55                           jae 0x140a9aab6
00A9AA61  0F BA 6E 0C 19                  bts dword ptr [rsi + 0xc], 0x19
00A9AA66  88 9E 32 03 00 00               mov byte ptr [rsi + 0x332], bl
00A9AA6C  41 3B DC                        cmp ebx, r12d
00A9AA6F  77 08                           ja 0x140a9aa79
00A9AA71  F0 83 8E 30 03 00 00 20         lock or dword ptr [rsi + 0x330], 0x20
00A9AA79  8A 44 24 44                     mov al, byte ptr [rsp + 0x44]
00A9AA7D  4C 8B 6C 24 68                  mov r13, qword ptr [rsp + 0x68]
00A9AA82  41 88 84 5D 98 11 00 00         mov byte ptr [r13 + rbx*2 + 0x1198], al
00A9AA8A  8B 86 C8 00 00 00               mov eax, dword ptr [rsi + 0xc8]
00A9AA90  41 2B C4                        sub eax, r12d
00A9AA93  83 F8 04                        cmp eax, 4
00A9AA96  73 08                           jae 0x140a9aaa0
00A9AA98  8A 86 C8 00 00 00               mov al, byte ptr [rsi + 0xc8]
00A9AA9E  EB 03                           jmp 0x140a9aaa3
00A9AAA0  41 8A C4                        mov al, r12b
00A9AAA3  41 88 84 5D 99 11 00 00         mov byte ptr [r13 + rbx*2 + 0x1199], al
00A9AAAB  F0 41 0F AB 9D A8 11 00 00      lock bts dword ptr [r13 + 0x11a8], ebx
00A9AAB4  EB 05                           jmp 0x140a9aabb
00A9AAB6  4C 8B 6C 24 68                  mov r13, qword ptr [rsp + 0x68]
00A9AABB  48 8B D6                        mov rdx, rsi
00A9AABE  49 8B CE                        mov rcx, r14
00A9AAC1  E8 32 CB FC FF                  call 0x140a675f8
00A9AAC6  45 33 C0                        xor r8d, r8d
00A9AAC9  8B F8                           mov edi, eax
00A9AACB  85 C0                           test eax, eax
00A9AACD  0F 88 A8 FC FF FF               js 0x140a9a77b
00A9AAD3  41 8B 46 34                     mov eax, dword ptr [r14 + 0x34]
00A9AAD7  85 C0                           test eax, eax
00A9AAD9  74 06                           je 0x140a9aae1
00A9AADB  89 86 E0 00 00 00               mov dword ptr [rsi + 0xe0], eax
00A9AAE1  41 8B 46 38                     mov eax, dword ptr [r14 + 0x38]
00A9AAE5  85 C0                           test eax, eax
00A9AAE7  74 06                           je 0x140a9aaef
00A9AAE9  89 86 EC 00 00 00               mov dword ptr [rsi + 0xec], eax
00A9AAEF  41 8B 46 30                     mov eax, dword ptr [r14 + 0x30]
00A9AAF3  85 C0                           test eax, eax
00A9AAF5  74 15                           je 0x140a9ab0c
00A9AAF7  B9 00 40 00 00                  mov ecx, 0x4000
00A9AAFC  3B C1                           cmp eax, ecx
00A9AAFE  76 06                           jbe 0x140a9ab06
00A9AB00  41 89 4E 30                     mov dword ptr [r14 + 0x30], ecx
00A9AB04  8B C1                           mov eax, ecx
00A9AB06  C1 E0 0A                        shl eax, 0xa
00A9AB09  89 46 04                        mov dword ptr [rsi + 4], eax
00A9AB0C  41 F6 46 50 04                  test byte ptr [r14 + 0x50], 4
00A9AB11  74 1B                           je 0x140a9ab2e
00A9AB13  8B 46 04                        mov eax, dword ptr [rsi + 4]
00A9AB16  05 FF FF 1F 00                  add eax, 0x1fffff
00A9AB1B  25 00 00 E0 FF                  and eax, 0xffe00000
00A9AB20  89 46 04                        mov dword ptr [rsi + 4], eax
00A9AB23  F0 81 8E 30 03 00 00 00 00 00 20  lock or dword ptr [rsi + 0x330], 0x20000000
00A9AB2E  66 44 39 86 98 00 00 00         cmp word ptr [rsi + 0x98], r8w
00A9AB36  76 58                           jbe 0x140a9ab90
00A9AB38  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00A9AB41  48 89 46 20                     mov qword ptr [rsi + 0x20], rax
00A9AB45  EB 29                           jmp 0x140a9ab70
00A9AB47  81 FF 06 02 00 C0               cmp edi, 0xc0000206
00A9AB4D  0F 85 28 FC FF FF               jne 0x140a9a77b
00A9AB53  8B 44 24 60                     mov eax, dword ptr [rsp + 0x60]
00A9AB57  8B 4E 04                        mov ecx, dword ptr [rsi + 4]
00A9AB5A  8D 50 FF                        lea edx, [rax - 1]
00A9AB5D  03 D1                           add edx, ecx
00A9AB5F  FF C8                           dec eax
00A9AB61  F7 D0                           not eax
00A9AB63  23 D0                           and edx, eax
00A9AB65  3B CA                           cmp ecx, edx
00A9AB67  0F 84 0E FC FF FF               je 0x140a9a77b
00A9AB6D  89 56 04                        mov dword ptr [rsi + 4], edx
00A9AB70  F0 44 09 A6 38 03 00 00         lock or dword ptr [rsi + 0x338], r12d
00A9AB78  4C 8D 44 24 60                  lea r8, [rsp + 0x60]
00A9AB7D  33 D2                           xor edx, edx
00A9AB7F  48 8B CE                        mov rcx, rsi
00A9AB82  E8 D5 57 F2 FF                  call 0x1409c035c
00A9AB87  45 33 C0                        xor r8d, r8d
00A9AB8A  8B F8                           mov edi, eax
00A9AB8C  85 C0                           test eax, eax
00A9AB8E  78 B7                           js 0x140a9ab47
00A9AB90  B9 00 10 00 00                  mov ecx, 0x1000
00A9AB95  39 4E 04                        cmp dword ptr [rsi + 4], ecx
00A9AB98  73 1A                           jae 0x140a9abb4
00A9AB9A  66 44 39 86 98 00 00 00         cmp word ptr [rsi + 0x98], r8w
00A9ABA2  77 09                           ja 0x140a9abad
00A9ABA4  F7 46 0C 00 04 00 00            test dword ptr [rsi + 0xc], 0x400
00A9ABAB  74 07                           je 0x140a9abb4
00A9ABAD  F0 09 8E 30 03 00 00            lock or dword ptr [rsi + 0x330], ecx
00A9ABB4  8B 56 04                        mov edx, dword ptr [rsi + 4]
00A9ABB7  B9 FF FF 00 00                  mov ecx, 0xffff
00A9ABBC  48 8D 42 B8                     lea rax, [rdx - 0x48]
00A9ABC0  48 3B C1                        cmp rax, rcx
00A9ABC3  73 03                           jae 0x140a9abc8
00A9ABC5  8D 4A B8                        lea ecx, [rdx - 0x48]
00A9ABC8  83 E1 F8                        and ecx, 0xfffffff8
00A9ABCB  89 4E 08                        mov dword ptr [rsi + 8], ecx
00A9ABCE  48 8B CE                        mov rcx, rsi
00A9ABD1  E8 7A 9B FD FF                  call 0x140a74750
00A9ABD6  45 33 C0                        xor r8d, r8d
00A9ABD9  8B F8                           mov edi, eax
00A9ABDB  85 C0                           test eax, eax
00A9ABDD  79 0D                           jns 0x140a9abec
00A9ABDF  48 8B CE                        mov rcx, rsi
00A9ABE2  E8 8D 6E F2 FF                  call 0x1409c1a74
00A9ABE7  E9 8F FB FF FF                  jmp 0x140a9a77b
00A9ABEC  41 0F BA E7 1A                  bt r15d, 0x1a
00A9ABF1  73 33                           jae 0x140a9ac26
00A9ABF3  41 0F BA E7 0A                  bt r15d, 0xa
00A9ABF8  72 2C                           jb 0x140a9ac26
00A9ABFA  8B 56 04                        mov edx, dword ptr [rsi + 4]
00A9ABFD  B9 40 00 00 00                  mov ecx, 0x40
00A9AC02  41 B8 45 74 77 5A               mov r8d, 0x5a777445
00A9AC08  E8 E3 74 0E 00                  call 0x140b820f0
00A9AC0D  45 33 C0                        xor r8d, r8d
00A9AC10  48 89 86 88 05 00 00            mov qword ptr [rsi + 0x588], rax
00A9AC17  48 85 C0                        test rax, rax
00A9AC1A  75 0A                           jne 0x140a9ac26
00A9AC1C  BF 17 00 00 C0                  mov edi, 0xc0000017
00A9AC21  E9 55 FB FF FF                  jmp 0x140a9a77b
00A9AC26  8B 8E 24 01 00 00               mov ecx, dword ptr [rsi + 0x124]
00A9AC2C  85 C9                           test ecx, ecx
00A9AC2E  74 11                           je 0x140a9ac41
00A9AC30  F7 46 0C 00 20 00 00            test dword ptr [rsi + 0xc], 0x2000
00A9AC37  75 08                           jne 0x140a9ac41
00A9AC39  8B D1                           mov edx, ecx
00A9AC3B  48 C1 E2 14                     shl rdx, 0x14
00A9AC3F  EB 05                           jmp 0x140a9ac46
00A9AC41  BA 00 00 A0 00                  mov edx, 0xa00000
00A9AC46  8B 86 EC 00 00 00               mov eax, dword ptr [rsi + 0xec]
00A9AC4C  0F AF 46 04                     imul eax, dword ptr [rsi + 4]
00A9AC50  8D 0C 00                        lea ecx, [rax + rax]
00A9AC53  48 3B D1                        cmp rdx, rcx
00A9AC56  48 0F 46 D1                     cmovbe rdx, rcx
00A9AC5A  48 89 96 A0 01 00 00            mov qword ptr [rsi + 0x1a0], rdx
00A9AC61  45 39 46 70                     cmp dword ptr [r14 + 0x70], r8d
00A9AC65  7C 21                           jl 0x140a9ac88
00A9AC67  48 8B 54 24 70                  mov rdx, qword ptr [rsp + 0x70]
00A9AC6C  48 8B CE                        mov rcx, rsi
00A9AC6F  E8 1C C9 00 00                  call 0x140aa7590
00A9AC74  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
00A9AC79  8B F8                           mov edi, eax
00A9AC7B  E8 5C 3B F8 FF                  call 0x140a1e7dc
00A9AC80  85 FF                           test edi, edi
00A9AC82  0F 88 57 FF FF FF               js 0x140a9abdf
00A9AC88  F0 45 01 A5 34 11 00 00         lock add dword ptr [r13 + 0x1134], r12d
00A9AC90  49 8B 8D C0 02 00 00            mov rcx, qword ptr [r13 + 0x2c0]
00A9AC97  41 8B D4                        mov edx, r12d
00A9AC9A  8B 5C 24 44                     mov ebx, dword ptr [rsp + 0x44]
00A9AC9E  48 8B 0C D9                     mov rcx, qword ptr [rcx + rbx*8]
00A9ACA2  E8 A9 72 97 FF                  call 0x140411f50
00A9ACA7  45 33 FF                        xor r15d, r15d
00A9ACAA  F7 46 0C 00 04 00 00            test dword ptr [rsi + 0xc], 0x400
00A9ACB1  75 3C                           jne 0x140a9acef
00A9ACB3  45 39 7E 70                     cmp dword ptr [r14 + 0x70], r15d
00A9ACB7  7C 36                           jl 0x140a9acef
00A9ACB9  E8 52 AA 78 FF                  call 0x140225710
00A9ACBE  48 8B C8                        mov rcx, rax
00A9ACC1  48 8B D6                        mov rdx, rsi
00A9ACC4  E8 FB 78 A1 FF                  call 0x1404b25c4
00A9ACC9  8B F8                           mov edi, eax
00A9ACCB  85 C0                           test eax, eax
00A9ACCD  79 20                           jns 0x140a9acef
00A9ACCF  49 8B 8D C0 02 00 00            mov rcx, qword ptr [r13 + 0x2c0]
00A9ACD6  41 8B D4                        mov edx, r12d
00A9ACD9  48 8B 0C D9                     mov rcx, qword ptr [rcx + rbx*8]
00A9ACDD  E8 6E 43 7C FF                  call 0x14025f050
00A9ACE2  48 8B CE                        mov rcx, rsi
00A9ACE5  E8 9E 69 F2 FF                  call 0x1409c1688
00A9ACEA  E9 A4 F3 FF FF                  jmp 0x140a9a093
00A9ACEF  48 8B 0D 4A 4B 46 00            mov rcx, qword ptr [rip + 0x464b4a]
00A9ACF6  48 8D 15 7B 90 57 FF            lea rdx, [rip - 0xa86f85]
00A9ACFD  E8 4E 77 8F FF                  call 0x140392450
00A9AD02  84 C0                           test al, al
00A9AD04  74 0F                           je 0x140a9ad15
00A9AD06  4C 8B C6                        mov r8, rsi
00A9AD09  48 8D 15 68 90 57 FF            lea rdx, [rip - 0xa86f98]
00A9AD10  E8 0B 24 F2 FF                  call 0x1409bd120
00A9AD15  48 8D 8E 78 02 00 00            lea rcx, [rsi + 0x278]
00A9AD1C  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
00A9AD21  45 33 C9                        xor r9d, r9d
00A9AD24  45 33 C0                        xor r8d, r8d
00A9AD27  33 D2                           xor edx, edx
00A9AD29  E8 82 39 77 FF                  call 0x14020e6b0
00A9AD2E  48 8B 4D 98                     mov rcx, qword ptr [rbp - 0x68]
00A9AD32  45 33 C0                        xor r8d, r8d
00A9AD35  48 8B C6                        mov rax, rsi
00A9AD38  48 87 04 D9                     xchg qword ptr [rcx + rbx*8], rax
00A9AD3C  48 8B CE                        mov rcx, rsi
00A9AD3F  41 8D 50 05                     lea edx, [r8 + 5]
00A9AD43  E8 E0 50 F2 FF                  call 0x1409bfe28
00A9AD48  F7 46 0C 00 00 00 02            test dword ptr [rsi + 0xc], 0x2000000
00A9AD4F  74 79                           je 0x140a9adca
00A9AD51  4C 3B 2D 50 BD 52 00            cmp r13, qword ptr [rip + 0x52bd50]
00A9AD58  75 30                           jne 0x140a9ad8a
00A9AD5A  45 8A C4                        mov r8b, r12b
00A9AD5D  49 8B D6                        mov rdx, r14
00A9AD60  48 8B CE                        mov rcx, rsi
00A9AD63  E8 48 C9 FC FF                  call 0x140a676b0
00A9AD68  8B F8                           mov edi, eax
00A9AD6A  85 C0                           test eax, eax
00A9AD6C  78 2D                           js 0x140a9ad9b
00A9AD6E  8B 4C 24 40                     mov ecx, dword ptr [rsp + 0x40]
00A9AD72  48 8D 05 07 4B 46 00            lea rax, [rip + 0x464b07]
00A9AD79  48 8D 0C 89                     lea rcx, [rcx + rcx*4]
00A9AD7D  66 44 89 24 88                  mov word ptr [rax + rcx*4], r12w
00A9AD82  C7 44 88 04 2A 00 00 00         mov dword ptr [rax + rcx*4 + 4], 0x2a
00A9AD8A  49 8B D6                        mov rdx, r14
00A9AD8D  48 8B CE                        mov rcx, rsi
00A9AD90  E8 FB C6 FC FF                  call 0x140a67490
00A9AD95  8B F8                           mov edi, eax
00A9AD97  85 C0                           test eax, eax
00A9AD99  79 2F                           jns 0x140a9adca
00A9AD9B  48 8B CE                        mov rcx, rsi
00A9AD9E  89 7E 28                        mov dword ptr [rsi + 0x28], edi
00A9ADA1  E8 EE 3D F2 FF                  call 0x1409beb94
00A9ADA6  F7 46 0C 00 04 00 00            test dword ptr [rsi + 0xc], 0x400
00A9ADAD  74 1B                           je 0x140a9adca
00A9ADAF  48 8B D6                        mov rdx, rsi
00A9ADB2  49 8B CE                        mov rcx, r14
00A9ADB5  E8 D6 41 E2 FF                  call 0x1408bef90
00A9ADBA  41 8A D4                        mov dl, r12b
00A9ADBD  48 8B CE                        mov rcx, rsi
00A9ADC0  E8 9B 93 F6 FF                  call 0x140a04160
00A9ADC5  E9 18 FF FF FF                  jmp 0x140a9ace2
00A9ADCA  0F B6 44 24 48                  movzx eax, byte ptr [rsp + 0x48]
00A9ADCF  3C 09                           cmp al, 9
00A9ADD1  74 11                           je 0x140a9ade4
00A9ADD3  44 8B 06                        mov r8d, dword ptr [rsi]
00A9ADD6  44 8B C8                        mov r9d, eax
00A9ADD9  49 8B D5                        mov rdx, r13
00A9ADDC  49 8B CE                        mov rcx, r14
00A9ADDF  E8 90 C5 FC FF                  call 0x140a67374
00A9ADE4  48 8B D6                        mov rdx, rsi
00A9ADE7  49 8B CE                        mov rcx, r14
00A9ADEA  E8 A1 41 E2 FF                  call 0x1408bef90
00A9ADEF  41 8A D4                        mov dl, r12b
00A9ADF2  48 8B CE                        mov rcx, rsi
00A9ADF5  E8 66 93 F6 FF                  call 0x140a04160
00A9ADFA  E9 94 F2 FF FF                  jmp 0x140a9a093
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwpStartLogger(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned int v_stack_m108;
    unsigned __int64 v_stack_m118;
    unsigned int v_stack_m124;
    unsigned int v_stack_m128;
    unsigned int v_stack_m138;
    unsigned int v_stack_m140;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int16 v_stack_mD6;
    unsigned __int16 v_stack_mD8;
    unsigned int v_stack_mDC;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned int v_stack_p40;
    unsigned __int64 v_stack_p44;
    unsigned __int8 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned int v_stack_p60;
    unsigned int v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p78;

    v_stack_p18 = v_rbx;
    v_rsp = (v_rsp) - (304);
    result = (*(unsigned __int64 *)(v_rip + 3606941)) ^ (v_rsp);
    v_stack_m48 = result;
    v_rbx = 0;
    v_stack_m100 = a1;
    v_stack_m124 = 0;
    v_stack_mD6 = 0;
    v_stack_mF8 = 0;
    v_stack_m108 = 0;
    a2 = 0;
    v_stack_m128 = 8;
    v_stack_mB8 = v_xmm0;
    v_stack_mF0 = v_xmm0;
    v_stack_m118 = v_xmm1;
    result = RtlInitUnicodeString(v_stack_m118, a2, a3, a4);
    a2 = 0;
    result = RtlInitUnicodeString(v_stack_mF0, a2, a3, a4);
    v_r15 = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 64))) & (0x9DECE5FFULL));
    if ((((unsigned __int8)(v_r15)) & (3)) != 0) goto loc_00A99E20;
    if ((((unsigned __int8)(v_r15)) & (8)) != 0) goto loc_00A99E1D;
    if ((((unsigned __int8)(v_r15)) & (4)) != 0) {
        v_r15 = (unsigned int)((v_r15) | ((unsigned int)(v_rbx + 1)));
    }
    if (!(condition_is_above_or_equal)) {
    }
    if (condition_is_above_or_equal) goto loc_00A99E3F;
    if (!(condition_is_above_or_equal)) {
    }
    if ((*(unsigned __int16 *)(a2 + 144)) <= 0) goto loc_00A9A035;
    if ((*(unsigned __int64 *)(a2 + 152)) == 0) goto loc_00A9A035;
    result = EtwpCaptureString(a2 + 144, v_stack_m118, a3, a4);
    if ((unsigned int)(result) != 0) goto loc_00A9A03A;
    if (condition_is_above_or_equal) goto loc_00A99EB1;
    if ((*(unsigned __int64 *)(a2 + 136)) != 0) goto loc_00A9A035;
    if ((((unsigned __int8)(v_r15)) & (15)) != 0) goto loc_00A9A035;
    if (((256) & ((unsigned int)(v_r15))) != 0) {
    }
    if ((*(unsigned int *)(a2 + 68)) != 0) {
        *(unsigned int *)(a2 + 68) = 0;
    }
    if ((*(unsigned int *)(a2 + 76)) != 0) {
        *(unsigned int *)(a2 + 76) = 0;
    }
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r15))) & (3));
    if (((unsigned __int8)(result)) == 3) goto loc_00A9A035;
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r15))) & ((unsigned int)((unsigned int)(0xC000ULL))));
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0xC000ULL)))) goto loc_00A9A035;
    if ((((unsigned int)(v_r15)) & (0x700ULL)) != 0) goto loc_00A99EE7;
    if ((*(unsigned __int64 *)(a2 + 136)) == 0) goto loc_00A9A035;
loc_00A99EE7:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r15))) & (6));
    if (((unsigned __int8)(result)) == 6) goto loc_00A9A035;
    if (((2) & ((unsigned __int8)(v_r15))) == 0) goto loc_00A99F0A;
    if ((*(unsigned int *)(a2 + 60)) == 0) goto loc_00A9A035;
loc_00A99F0A:
    if ((((unsigned __int8)(v_r15)) & (32)) == 0) goto loc_00A99F2B;
    if ((*(unsigned int *)(a2 + 60)) == 0) goto loc_00A9A035;
    if (((12) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 64))))) != 0) goto loc_00A9A035;
loc_00A99F2B:
    if ((((unsigned __int8)(v_r15)) & (64)) == 0) goto loc_00A99F5D;
    if (((2) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 112))))) == 0) goto loc_00A9A035;
    if ((((unsigned int)(v_r15)) & (0x402ULL)) != 0) goto loc_00A99F5D;
    if (((256) & ((unsigned int)(v_r15))) == 0) goto loc_00A9A035;
    if ((*(unsigned __int64 *)(a2 + 136)) != 0) goto loc_00A9A035;
loc_00A99F5D:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r15))) & ((unsigned int)((unsigned int)(0xC00000ULL))));
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0xC00000ULL)))) goto loc_00A9A035;
    if ((((unsigned __int8)(v_r15)) & (8)) == 0) goto loc_00A99FE8;
    if ((*(unsigned __int64 *)(a2 + 136)) == 0) goto loc_00A9A035;
    if (((2) & ((unsigned __int8)(v_r15))) != 0) goto loc_00A9A035;
    if ((*(unsigned int *)(a2 + 60)) == 0) goto loc_00A9A035;
    if (((2) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 112))))) != 0) goto loc_00A9A035;
    if (condition_is_below) goto loc_00A9A035;
    if ((*(unsigned __int64 *)(a2 + 24)) != (*(unsigned __int64 *)(v_rip - 11042937))) goto loc_00A99FC8;
    if ((*(unsigned __int64 *)(a2 + 32)) == (*(unsigned __int64 *)(v_rip - 11042942))) goto loc_00A9A035;
loc_00A99FC8:
    if ((*(unsigned __int64 *)(a2 + 24)) != (*(unsigned __int64 *)(v_rip - 10940163))) goto loc_00A99FE2;
    if ((*(unsigned __int64 *)(a2 + 32)) == (*(unsigned __int64 *)(v_rip - 10940168))) goto loc_00A9A035;
loc_00A99FE2:
    if ((((unsigned __int8)(v_r15)) & (4)) != 0) goto loc_00A9A035;
loc_00A99FE8:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 64))))) & ((unsigned int)((unsigned int)(0x3000000ULL))));
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0x3000000ULL)))) goto loc_00A9A035;
    if (((unsigned int)(result)) >= ((unsigned int)((unsigned int)(0x3000000ULL)))) goto loc_00A9A007;
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 64)))) & (262)) != 0) goto loc_00A9A035;
loc_00A9A007:
    if (condition_is_below) goto loc_00A9A035;
    if (((*(unsigned __int8 *)(a2 + 80)) & (4)) == 0) goto loc_00A9A103;
    if ((*(unsigned __int64 *)(v_rip + 5504793)) == 0) goto loc_00A9A0BD;
    if ((*(unsigned __int64 *)(v_rip + 5504793)) >= 0) goto loc_00A9A035;
    if ((*(unsigned __int64 *)(v_rip + 5504793)) >= 0) goto loc_00A9A103;
loc_00A9A035:
loc_00A9A03A:
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 4610047), v_rip - 10976816, 2, a4);
    if ((unsigned __int8)(result) != 0) {
        v_stack_m138 = (unsigned int)(v_r15);
        result = v_stack_mF0;
        v_stack_m140 = (unsigned int)((unsigned int)(0xC000000DULL));
        a4 = v_stack_m118;
        a2 = v_rip - 10976851;
        v_stack_m148 = result;
        result = EtwpEventWriteTemplateAdmin(*(unsigned __int64 *)(v_rip + 4610047), a2, 2, a4);
    }
    result = RtlFreeAnsiString(v_stack_m118, a2, 2, a4);
    result = RtlFreeAnsiString(v_stack_mF0, a2, 2, a4);
    result = EtwpFreeSecurityDescriptor(v_stack_mF8, a2, 2, a4);
loc_00A9A093:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, 2, a4);
    v_rsp = (v_rsp) + (304);
    return result;
loc_00A9A0BD:
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 4609916), v_rip - 10974483, 2, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00A9A03A;
    v_stack_p28 = v_stack_p78;
    v_stack_p20 = v_stack_p50;
    result = EtwpEventWriteTemplateSessionFromCapturedData(*(unsigned __int64 *)(v_rip + 4609916), v_rip - 10974483, a2 + 24, (unsigned int)(*(unsigned int *)(a2 + 64)));
    goto loc_00A9A03A;
loc_00A9A103:
    if (!sign_flag) goto loc_00A9A15A;
    if ((*(unsigned __int8 *)(v_rip + 4608371)) != ((unsigned __int8)(v_stack_p18))) goto loc_00A9A035;
    if ((((unsigned __int8)(a2 + 24)) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 112))))) == 0) goto loc_00A9A035;
    if (condition_is_above_or_equal) goto loc_00A9A035;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 40))) - ((unsigned int)(a2 + 24)));
    if ((((unsigned int)(result)) & (0xFFFFFFFDULL)) == 0) goto loc_00A9A035;
    if ((*(unsigned __int64 *)(a2 + 24)) != (*(unsigned __int64 *)(v_rip - 11046519))) goto loc_00A9A15A;
    if ((*(unsigned __int64 *)(a2 + 32)) == (*(unsigned __int64 *)(v_rip - 11046524))) goto loc_00A9A035;
loc_00A9A15A:
    result = EtwpValidateFlagExtension(a2, v_rip - 10974483, a2 + 24, (unsigned int)(*(unsigned int *)(a2 + 64)));
    if (sign_flag) goto loc_00A9A03A;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_r15))) & (256));
    a1 = (unsigned int)((a1) >> (3));
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)(a1))) | (64));
    if ((*(unsigned __int16 *)(a2 + 128)) == ((unsigned __int16)(v_stack_p18))) { v_rsi = (unsigned int)(a1); }
    result = EtwpLookupLoggerIdByName(a1, v_stack_p50, v_stack_p44, (unsigned int)(*(unsigned int *)(a2 + 64)));
    if ((unsigned int)(result) != 0) goto loc_00A9A1A8;
loc_00A9A19E:
    goto loc_00A9A03A;
loc_00A9A1A8:
    if ((*(unsigned __int64 *)(a2 + 24)) != (*(unsigned __int64 *)(v_rip - 11046627))) goto loc_00A9A1D7;
    if ((*(unsigned __int64 *)(a2 + 32)) != (*(unsigned __int64 *)(v_rip - 11046632))) goto loc_00A9A1D7;
    result = ExUuidCreate(v_stack_mB8, v_stack_p50, v_stack_p44, (unsigned int)(*(unsigned int *)(a2 + 64)));
    if (sign_flag) goto loc_00A9A03A;
    goto loc_00A9A1E1;
loc_00A9A1D7:
    v_stack_mB8 = v_xmm0;
loc_00A9A1E1:
    if ((((unsigned int)(v_r15)) & (0xC00000ULL)) != 0) goto loc_00A9A220;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == ((unsigned __int8)(v_stack_p18))) goto loc_00A9A21B;
    result = PsGetProcessSessionId(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), v_stack_p50, v_stack_p44, (unsigned int)(*(unsigned int *)(a2 + 64)));
    if ((unsigned int)(result) == 0) goto loc_00A9A21B;
    goto loc_00A9A220;
loc_00A9A21B:
loc_00A9A220:
    v_stack_mD0 = *(unsigned __int64 *)(a1 + 712);
    if (v_stack_mB8 != (*(unsigned __int64 *)(v_rip - 11043563))) goto loc_00A9A245;
    if (v_stack_mB0 == (*(unsigned __int64 *)(v_rip - 11043579))) goto loc_00A9A25F;
loc_00A9A245:
    if (v_stack_mB8 != (*(unsigned __int64 *)(v_rip - 10940796))) goto loc_00A9A360;
    if (v_stack_mB0 != (*(unsigned __int64 *)(v_rip - 10940801))) goto loc_00A9A360;
loc_00A9A25F:
    result = RtlFreeAnsiString(v_stack_p50, v_stack_mB8, v_stack_p44, (unsigned int)(*(unsigned int *)(a2 + 64)));
    if (v_stack_mB8 != (*(unsigned __int64 *)(v_rip - 11043636))) goto loc_00A9A290;
    if (v_stack_mB0 != (*(unsigned __int64 *)(v_rip - 11043641))) goto loc_00A9A290;
    goto loc_00A9A2A1;
loc_00A9A290:
    v_stack_p40 = (unsigned int)(v_rbx + 1);
loc_00A9A2A1:
    v_stack_p44 = 2;
    result = RtlCreateUnicodeString(v_stack_p50, v_rip + 446159, v_stack_p44, (unsigned int)(*(unsigned int *)(a2 + 64)));
    if ((unsigned __int8)(result) != 0) goto loc_00A9A2BD;
loc_00A9A2B3:
    goto loc_00A9A03A;
loc_00A9A2BD:
    if (condition_is_below) goto loc_00A9A035;
    a2 = ((unsigned int)(0xC0000017ULL)) | (v_rbx + 1);
loc_00A9A2DE:
    if (condition_is_not_equal) goto loc_00A9A19E;
loc_00A9A2E4:
    result = ExAcquireRundownProtectionCacheAwareEx(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 704) + (unsigned int)(v_stack_p44) * 8), (unsigned int)((unsigned int)(v_rbx + 1)), v_stack_p44, (unsigned int)(*(unsigned int *)(a2 + 64)));
    v_rbx = 0;
    if ((*(unsigned int *)(a2 + 112)) < 0) goto loc_00A9A611;
    result = EtwpGetSecurityDescriptorByGuid(v_stack_mB8, v_stack_p70, v_stack_p44, (unsigned int)(*(unsigned int *)(a2 + 64)));
    a3 = 0;
    result = EtwpAccessCheck(v_stack_p70, (unsigned int)((unsigned int)(v_rsi)), a3, (unsigned int)(*(unsigned int *)(a2 + 64)));
    if (!sign_flag) goto loc_00A9A611;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 4609291), v_rip - 10977268, a3, (unsigned int)(*(unsigned int *)(a2 + 64)));
    if ((unsigned __int8)(result) == 0) goto loc_00A9A7F7;
    v_stack_p20 = (unsigned int)(v_rsi);
    result = EtwpEventWriteTemplateSessionDesiredAccess(*(unsigned __int64 *)(v_rip + 4609291), v_rip - 10977268, v_stack_p50, v_stack_mB8);
    goto loc_00A9A7F7;
loc_00A9A360:
    if ((v_rip - 10977268) != (*(unsigned __int64 *)(v_rip + 785737))) goto loc_00A9A3CD;
    if ((*(unsigned __int64 *)(v_rip + 4609291)) != (*(unsigned __int64 *)(v_rip + 785736))) goto loc_00A9A3CD;
    v_stack_p44 = (unsigned int)(v_rbx + 1);
    result = EtwpGetFlagExtension(a2, (unsigned int)((unsigned int)(v_rbx + 1)), v_stack_p50, v_stack_mB8);
    if (result == 0) goto loc_00A9A3B9;
    if (condition_is_below) goto loc_00A9A035;
    result = RtlFreeAnsiString(v_stack_p50, (unsigned int)((unsigned int)(v_rbx + 1)), v_stack_p50, v_stack_mB8);
    result = RtlCreateUnicodeString(v_stack_p50, v_rip + 445965, v_stack_p50, v_stack_mB8);
    if ((unsigned __int8)(result) == 0) goto loc_00A9A2B3;
    v_stack_p40 = 0;
loc_00A9A3B9:
    a1 = ((unsigned int)((unsigned int)(result))) | (v_rbx + 1);
    goto loc_00A9A2DE;
loc_00A9A3CD:
    if ((v_rip + 445965) != (*(unsigned __int64 *)(v_rip - 10940948))) goto loc_00A9A42E;
    if (a1 != (*(unsigned __int64 *)(v_rip - 10940949))) goto loc_00A9A42E;
    v_stack_p44 = 3;
    if (a1 < (*(unsigned __int64 *)(v_rip - 10940949))) goto loc_00A9A035;
    result = RtlFreeAnsiString(v_stack_p50, v_rip + 445965, v_stack_p50, v_stack_mB8);
    result = RtlCreateUnicodeString(v_stack_p50, v_rip + 445757, v_stack_p50, v_stack_mB8);
    if ((unsigned __int8)(result) == 0) goto loc_00A9A2B3;
    a1 = ((unsigned int)((unsigned int)(result))) | (v_rbx + 1);
    goto loc_00A9A2DE;
loc_00A9A42E:
    result = wcsicmp(v_stack_p58, v_rip + 445702, v_stack_p50, v_stack_mB8);
    if ((unsigned int)(result) != 0) goto loc_00A9A465;
    if (v_stack_mB8 != (*(unsigned __int64 *)(v_rip - 10941070))) goto loc_00A9A19E;
    if (v_stack_mB0 != (*(unsigned __int64 *)(v_rip - 10941079))) goto loc_00A9A19E;
loc_00A9A465:
    if ((*(unsigned int *)(a1 + 16)) <= 4) goto loc_00A9A4BB;
loc_00A9A470:
    a3 = 0;
    result = EtwpAcquireLoggerContextByLoggerId(a1, 4, a3, v_stack_mB8);
    if (result == 0) goto loc_00A9A4A6;
    if ((*(unsigned __int64 *)(result + 276)) != v_stack_mB8) goto loc_00A9A49C;
    if ((*(unsigned __int64 *)(result + 284)) == v_stack_mB0) goto loc_00A9A4B1;
loc_00A9A49C:
    a2 = 0;
    result = EtwpReleaseLoggerContext(result, a2, a3, v_stack_mB8);
loc_00A9A4A6:
    v_rbx = (unsigned int)((4) + ((unsigned int)(v_rbx + 1)));
    if (((unsigned int)(v_rbx)) < (*(unsigned int *)(a1 + 16))) goto loc_00A9A470;
    goto loc_00A9A4BB;
loc_00A9A4B1:
    a2 = 0;
    result = EtwpReleaseLoggerContext(result, a2, a3, v_stack_mB8);
loc_00A9A4BB:
    if (((unsigned int)(v_rbx)) < ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 16))))) goto loc_00A9A19E;
    v_stack_p44 = 4;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 16)))) <= 4) goto loc_00A9A4FA;
    a2 = ((unsigned int)((unsigned int)(result))) | (v_rbx + 1);
loc_00A9A4DA:
    if (condition_is_equal) goto loc_00A9A4FA;
    result = (unsigned int)(((unsigned int)(v_stack_p44)) + ((unsigned int)(v_rbx + 1)));
    v_stack_p44 = (unsigned int)(result);
    if (((unsigned int)(result)) < (*(unsigned int *)(a1 + 16))) goto loc_00A9A4DA;
loc_00A9A4FA:
    if (v_stack_p44 < ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 16))))) goto loc_00A9A2E4;
    v_rbx = 0;
    if ((*(unsigned __int8 *)(v_rip + 3819305)) != 0) goto loc_00A9A5D7;
    v_stack_mA8 = a1 + 16;
    *(unsigned __int8 *)(v_rip + 3819266) = (unsigned __int8)(v_rbx + 1);
    v_stack_p20 = v_stack_mA8;
    a3 = 0;
    v_stack_mA0 = 4;
    result = EtwWrite(*(unsigned __int64 *)(v_rip + 4608803), v_rip - 10974204, a3, (unsigned int)((unsigned int)(v_rbx + 1)));
    if ((*(unsigned int *)(v_rip + 3599378)) <= 5) goto loc_00A9A5D7;
    result = tlgKeywordOn(v_rip + 3599359, v_rip - 10974204, a3, (unsigned int)((unsigned int)(v_rbx + 1)));
    if ((unsigned __int8)(result) != 0) {
        result = v_stack_mC8;
        v_stack_mC8 = v_rbx + 1;
        v_stack_m78 = result;
        a4 = v_rbx + 5;
        result = v_stack_mC0;
        v_stack_m70 = 8;
        v_stack_m68 = result;
        a2 = v_rip - 10774781;
        result = *(unsigned int *)(a1 + 16);
        a1 = v_rip + 3599300;
        v_stack_p68 = (unsigned int)(result);
        result = v_stack_p68;
        v_stack_m58 = result;
        result = v_stack_m98;
        v_stack_p20 = result;
        v_stack_mC0 = 0x1000000ULL;
        v_stack_m60 = 8;
        v_stack_m50 = 4;
        result = tlgWriteAgg(a1, a2, a3, a4);
    }
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 4608610), v_rip - 10973221, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00A9A03A;
    result = EtwpEventWriteTemplateSessionMaxLoggers(*(unsigned __int64 *)(v_rip + 4608610), v_rip - 10973255, v_stack_p50, (unsigned int)(*(unsigned int *)(a1 + 16)));
    goto loc_00A9A03A;
loc_00A9A611:
    if ((*(unsigned __int64 *)(v_rip - 10941592)) != v_stack_mB8) goto loc_00A9A631;
    if ((*(unsigned __int64 *)(v_rip - 10941597)) != v_stack_mB0) goto loc_00A9A631;
    v_stack_p48 = 0;
    goto loc_00A9A655;
loc_00A9A631:
    result = memcmp(v_rip - 10941986, v_stack_mB8, 16, (unsigned int)(*(unsigned int *)(a1 + 16)));
    result = (unsigned int)(-(result));
    a1 = (unsigned __int8)((v_rip - 10941986) & (8));
    a1 = (unsigned __int8)((a1) + ((unsigned __int8)(v_rbx + 1)));
    v_stack_p48 = (unsigned __int8)(a1);
loc_00A9A655:
    if (((*(unsigned int *)(a2 + 64)) & (0x2000000ULL)) == 0) goto loc_00A9A6F8;
    if (v_stack_p40 != 8) goto loc_00A9A6F8;
    if ((*(unsigned int *)(a2 + 112)) < 0) goto loc_00A9A692;
    a3 = 0;
    result = EtwpCheckGuidAccess(v_rip - 11044670, 128, a3, (unsigned int)(*(unsigned int *)(a1 + 16)));
    if (sign_flag) goto loc_00A9A7F7;
loc_00A9A692:
    v_stack_p40 = 2;
loc_00A9A69B:
    if (condition_is_above_or_equal) goto loc_00A9A6F8;
    v_rdi = (unsigned int)((2) + ((unsigned int)(v_rbx + 1)));
    v_stack_p40 = (unsigned int)(v_rdi);
    if (((unsigned int)(v_rdi)) < 8) goto loc_00A9A69B;
    v_stack_p40 = (unsigned int)((unsigned int)((unsigned int)(v_rdi)));
    if (((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) != 8) goto loc_00A9A6F8;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 4608381), v_rip - 10981322, a3, (unsigned int)(*(unsigned int *)(a1 + 16)));
    if ((unsigned __int8)(result) == 0) goto loc_00A9A7F7;
    result = EtwpEventWriteTemplateSessionMaxLoggers(*(unsigned __int64 *)(v_rip + 4608381), v_rip - 10981358, v_stack_p50, 8);
    goto loc_00A9A7F7;
loc_00A9A6F8:
    result = EtwpInitLoggerContext(v_stack_p50, (unsigned int)((unsigned int)(v_r15)), (unsigned int)(*(unsigned int *)(a2 + 112)), 8);
    result = EtwpGetFlagExtension(a2, 6, (unsigned int)(*(unsigned int *)(a2 + 112)), 8);
    if (result == 0) goto loc_00A9A81B;
    a1 = (unsigned __int16)((*(unsigned __int16 *)(result)) << (2));
    if (((unsigned __int16)(a1)) != ((unsigned __int16)(6 + 6))) goto loc_00A9A81B;
    result = EtwpSetPartitionContext(result + 1600, *(unsigned __int64 *)(result + 4), (unsigned int)(*(unsigned int *)(a2 + 112)), 8);
    if (!sign_flag) goto loc_00A9A81B;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 4608231), v_rip - 10982744, (unsigned int)(*(unsigned int *)(a2 + 112)), 8);
    if ((unsigned __int8)(result) != 0) {
        a4 = *(unsigned __int64 *)(result + 4);
        a3 = v_stack_p50;
        result = EtwpEventWriteTemplateSessionAndHandle(*(unsigned __int64 *)(v_rip + 4608231), v_rip - 10982744, a3, a4);
    }
loc_00A9A77B:
    if (((*(unsigned int *)(result + 12)) & (0x2000000ULL)) != 0) {
    }
    result = EtwpFreeApcPool(result + 832, v_rip - 10982744, a3, a4);
    result = (unsigned int)(*(unsigned int *)(result + 816));
    if (sign_flag) {
        a1 = *(unsigned __int64 *)(result + 1048);
        a2 = 0;
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
    if (((*(unsigned int *)(result + 816)) & (0x2000ULL)) != 0) {
    }
    result = RtlFreeAnsiString(result + 152, a2, a3, a4);
    result = RtlFreeAnsiString(result + 168, a2, a3, a4);
    if (*(unsigned __int64 *)(result + 800) != 0) {
        result = ZwClose(*(unsigned __int64 *)(result + 800), a2, a3, a4);
    }
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, a3, a4);
loc_00A9A7F7:
    result = ExReleaseRundownProtectionCacheAwareEx(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 704) + (unsigned int)(v_stack_p44) * 8), (unsigned int)((unsigned int)(v_rbx + 1)), a3, a4);
    goto loc_00A9A03A;
loc_00A9A81B:
    result = RtlFreeAnsiString(v_stack_p50, (unsigned int)((unsigned int)(v_rbx + 1)), a3, a4);
    a3 = 0;
    if (result != 0) goto loc_00A9A834;
    goto loc_00A9A7F7;
loc_00A9A834:
    *(unsigned __int64 *)(result + 276) = v_xmm0;
    *(unsigned int *)(result + 292) = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 60)));
    if (((*(unsigned __int8 *)(a2 + 80)) & ((unsigned __int8)(v_rbx + 1))) != 0) {
    }
    *(unsigned int *)(result + 200) = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 40)));
    if (((*(unsigned __int8 *)(a2 + 80)) & (2)) == 0) goto loc_00A9A87B;
    result = EtwpSetQpcDeltaTracking(result, (unsigned int)((unsigned int)(v_rbx + 1)), a3, a4);
    if (sign_flag) goto loc_00A9A777;
loc_00A9A87B:
    if (((*(unsigned __int8 *)(a2 + 80)) & (8)) != 0) {
    }
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 68))) == 0) goto loc_00A9A89A;
    *(unsigned int *)(result + 208) = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 68)));
    goto loc_00A9A8B9;
loc_00A9A89A:
    result = (unsigned int)(*(unsigned int *)(a2 + 68));
    if (!(condition_is_above_or_equal)) {
        result = (unsigned __int8)(v_r15);
        result = (unsigned __int8)((result) & (16));
        result = (unsigned __int8)(-(result));
        a1 = (unsigned int)((result) & (999));
        a1 = (unsigned int)((a1) + ((unsigned int)(v_rbx + 1)));
        *(unsigned int *)(result + 208) = (unsigned int)(a1);
    }
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 76))) == 0) goto loc_00A9A8D7;
    if ((*(unsigned int *)(result + 208)) > 0) goto loc_00A9A8D0;
    if (sign_flag) {
        *(unsigned int *)(a2 + 76) = 0;
        a1 = 0;
    }
    *(unsigned int *)(result) = (unsigned int)((unsigned int)(v_stack_p44));
    *(unsigned int *)(result + 212) = (unsigned int)(a1);
    *(unsigned __int64 *)(result + 1360) = a1;
    if ((*(unsigned __int16 *)(a2 + 128)) <= 0) goto loc_00A9A91E;
    if ((*(unsigned __int64 *)(a2 + 136)) == 0) goto loc_00A9A91E;
    result = EtwpCaptureString(a2 + 128, v_stack_p78, a3, a4);
    a3 = 0;
    if (sign_flag) goto loc_00A9A777;
loc_00A9A91E:
    result = (unsigned int)(*(unsigned int *)(a2 + 112));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 112)))) & (2)) != 0) {
        result = *(unsigned int *)(a2 + 96);
        *(unsigned int *)(result + 296) = (unsigned int)(result);
        *(unsigned int *)(a2 + 96) = 0;
    }
    a2 = 0;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (8)) == 0) goto loc_00A9A978;
    *(unsigned __int64 *)(result + 168) = v_xmm0;
    result = RtlInitUnicodeString(v_stack_p78, a2, a3, a4);
    result = EtwpGenerateFileName(result + 168, result + 296, result + 152, a4);
    if (sign_flag) goto loc_00A9A9AA;
    goto loc_00A9A983;
loc_00A9A978:
    *(unsigned __int64 *)(result + 152) = v_xmm0;
    result = RtlInitUnicodeString(result + 168, result + 296, result + 152, a4);
loc_00A9A983:
    result = Feature_1899207995__private_IsEnabledDeviceUsageNoInline(result + 168, result + 296, result + 152, a4);
    a3 = 0;
    if ((unsigned int)(result) == 0) goto loc_00A9A9B4;
    a1 = (unsigned int)((*(unsigned __int16 *)(result + 136)) + ((unsigned int)(*(unsigned __int16 *)(result + 152))));
    if (((unsigned int)(a1)) <= 0x7FFFULL) goto loc_00A9A9B4;
loc_00A9A9AA:
    goto loc_00A9A777;
loc_00A9A9B4:
    result = *(unsigned __int16 *)(result + 152);
    v_rdi = (unsigned int)(0xC000000DULL);
    if ((*(unsigned int *)(a2 + 112)) >= 0) {
        a1 = *(unsigned __int64 *)(gs_base + (0 + 392));
        a4 = result + 704;
        result = 12;
        v_stack_mDC = 2;
        a2 = v_stack_mE0;
        v_stack_mE0 = (unsigned int)(result);
        v_stack_mD8 = 257;
        result = SeCreateClientSecurity(a1, a2, a3, a4);
        v_rdi = (unsigned int)(result);
        a3 = 0;
    }
    if (sign_flag) goto loc_00A9A9AA;
    if (((*(unsigned int *)(result + 12)) & (256)) == 0) goto loc_00A9AA04;
    goto loc_00A9AA0C;
loc_00A9AA04:
loc_00A9AA0C:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 112)))) & (2)) != 0) {
    }
    if ((*(unsigned int *)(a2 + 112)) < 0) {
    }
    if ((((unsigned __int8)(v_rbx + 1)) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 112))))) != 0) {
    }
    if (((*(unsigned int *)(a2 + 112)) & ((unsigned int)((unsigned int)(0x4000ULL)))) != 0) {
    }
    result = EtwpInitializeTimeStamp(result, a2, a3, a4);
    if (((unsigned int)((unsigned int)(v_stack_p40))) >= 8) goto loc_00A9AAB6;
    *(unsigned __int8 *)(result + 818) = (unsigned __int8)((unsigned int)(v_stack_p40));
    if (((unsigned int)((unsigned int)(v_stack_p40))) <= ((unsigned int)(v_rbx + 1))) {
    }
    *(unsigned __int8 *)(v_stack_p68 + (unsigned int)(v_stack_p40) * 2 + 4504) = (unsigned __int8)(v_stack_p44);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 200))) - ((unsigned int)(v_rbx + 1)));
    if (((unsigned int)(result)) >= 4) goto loc_00A9AAA0;
    goto loc_00A9AAA3;
loc_00A9AAA0:
loc_00A9AAA3:
    *(unsigned __int8 *)(v_stack_p68 + (unsigned int)(v_stack_p40) * 2 + 4505) = (unsigned __int8)((unsigned __int8)(v_rbx + 1));
    goto loc_00A9AABB;
loc_00A9AAB6:
loc_00A9AABB:
    result = EtwpCheckForStackTracingExtension(a2, result, a3, a4);
    a3 = 0;
    if (sign_flag) goto loc_00A9A77B;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 52))) != 0) {
        *(unsigned int *)(result + 224) = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 52)));
    }
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 56))) != 0) {
        *(unsigned int *)(result + 236) = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 56)));
    }
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 48))) == 0) goto loc_00A9AB0C;
    result = (unsigned int)(*(unsigned int *)(a2 + 48));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 48)))) >= = ((unsigned int)((unsigned int)(0x4000ULL)))) {
        *(unsigned int *)(a2 + 48) = (unsigned int)((unsigned int)(0x4000ULL));
        result = (unsigned int)((unsigned int)(0x4000ULL));
    }
    result = (unsigned int)((result) << (10));
    *(unsigned int *)(result + 4) = (unsigned int)(result);
loc_00A9AB0C:
    if (((*(unsigned __int8 *)(a2 + 80)) & (4)) != 0) {
        result = *(unsigned int *)(result + 4);
        result = (unsigned int)((result) + (0x1FFFFFULL));
        result = (unsigned int)((result) & (0xFFE00000ULL));
        *(unsigned int *)(result + 4) = (unsigned int)(result);
    }
    if ((*(unsigned __int16 *)(result + 152)) <= 0) goto loc_00A9AB90;
    *(unsigned __int64 *)(result + 32) = *(unsigned __int64 *)(gs_base + (0 + 392));
    goto loc_00A9AB70;
loc_00A9AB47:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != 0xC0000206ULL) goto loc_00A9A77B;
    a2 = (unsigned int)(((unsigned int)(v_stack_p60) - 1) + ((unsigned int)((unsigned int)(*(unsigned int *)(result + 4)))));
    result = (unsigned int)(((unsigned int)(v_stack_p60)) - 1);
    result = (unsigned int)(~(result));
    a2 = (unsigned int)((a2) & ((unsigned int)(result)));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result + 4)))) == ((unsigned int)(a2))) goto loc_00A9A77B;
    *(unsigned int *)(result + 4) = (unsigned int)(a2);
loc_00A9AB70:
    a2 = 0;
    result = EtwpCreateLogFile(result, a2, v_stack_p60, a4);
    a3 = 0;
    if (sign_flag) goto loc_00A9AB47;
loc_00A9AB90:
    if ((*(unsigned int *)(result + 4)) >= ((unsigned int)((unsigned int)(0x1000ULL)))) goto loc_00A9ABB4;
    if ((*(unsigned __int16 *)(result + 152)) > 0) goto loc_00A9ABAD;
    if (((*(unsigned int *)(result + 12)) & (0x400ULL)) != 0) {
    }
    if (((unsigned int)(*(unsigned int *)(result + 4)) - 72) < ((unsigned int)(0xFFFFULL))) {
        a1 = (unsigned int)(*(unsigned int *)(result + 4)) - 72;
    }
    a1 = (unsigned int)((a1) & (0xFFFFFFF8ULL));
    *(unsigned int *)(result + 8) = (unsigned int)(a1);
    result = EtwpAllocateTraceBufferPool(result, (unsigned int)(*(unsigned int *)(result + 4)), a3, a4);
    a3 = 0;
    if (!sign_flag) goto loc_00A9ABEC;
loc_00A9ABDF:
    result = EtwpFreeTraceBufferPool(result, (unsigned int)(*(unsigned int *)(result + 4)), a3, a4);
    goto loc_00A9A77B;
loc_00A9ABEC:
    if (condition_is_above_or_equal) goto loc_00A9AC26;
    if (condition_is_below) goto loc_00A9AC26;
    result = ExAllocatePool2(64, (unsigned int)(*(unsigned int *)(result + 4)), (unsigned int)(0x5A777445ULL), a4);
    a3 = 0;
    *(unsigned __int64 *)(result + 1416) = result;
    if (result != 0) goto loc_00A9AC26;
    goto loc_00A9A77B;
loc_00A9AC26:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(result + 292))) == 0) goto loc_00A9AC41;
    if (((*(unsigned int *)(result + 12)) & (0x2000ULL)) != 0) goto loc_00A9AC41;
    a2 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + 292))))) << (20);
    goto loc_00A9AC46;
loc_00A9AC41:
loc_00A9AC46:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 236))) * (*(unsigned int *)(result + 4)));
    a2 = (unsigned int)(0xA00000ULL);
    if (((unsigned int)(0xA00000ULL)) <= (result + result * 1)) { a2 = result + result * 1; }
    *(unsigned __int64 *)(result + 416) = a2;
    if ((*(unsigned int *)(a2 + 112)) < 0) goto loc_00A9AC88;
    result = EtwpInitializeLoggerSecurityDescriptor(result, v_stack_p70, a3, a4);
    result = EtwpFreeSecurityDescriptor(v_stack_p70, v_stack_p70, a3, a4);
    if (sign_flag) goto loc_00A9ABDF;
loc_00A9AC88:
    result = ExAcquireRundownProtectionCacheAwareEx(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p68 + 704) + (unsigned int)(v_stack_p44) * 8), (unsigned int)((unsigned int)(v_rbx + 1)), a3, a4);
    v_r15 = 0;
    if (((*(unsigned int *)(result + 12)) & (0x400ULL)) != 0) goto loc_00A9ACEF;
    if ((*(unsigned int *)(a2 + 112)) < 0) goto loc_00A9ACEF;
    result = PsGetCurrentServerSilo(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p68 + 704) + (unsigned int)(v_stack_p44) * 8), (unsigned int)((unsigned int)(v_rbx + 1)), a3, a4);
    result = EtwpStartLoggerThread(result, result, a3, a4);
    if (!sign_flag) goto loc_00A9ACEF;
    result = ExReleaseRundownProtectionCacheAwareEx(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p68 + 704) + (unsigned int)(v_stack_p44) * 8), (unsigned int)((unsigned int)(v_rbx + 1)), a3, a4);
loc_00A9ACE2:
    result = EtwpFreeLoggerContext(result, (unsigned int)((unsigned int)(v_rbx + 1)), a3, a4);
    goto loc_00A9A093;
loc_00A9ACEF:
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 4606794), v_rip - 11038597, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        a3 = result;
        a2 = v_rip - 11038616;
        result = EtwpEventWriteTemplateSession(*(unsigned __int64 *)(v_rip + 4606794), a2, a3, a4);
    }
    v_stack_p20 = 0;
    a4 = 0;
    a3 = 0;
    a2 = 0;
    result = KeWaitForSingleObject(result + 632, a2, a3, a4);
    a3 = 0;
    result = EtwpSendSessionNotification(result, a3 + 5, a3, a4);
    if (((*(unsigned int *)(result + 12)) & (0x2000000ULL)) == 0) goto loc_00A9ADCA;
    if (v_stack_p68 != (*(unsigned __int64 *)(v_rip + 5422416))) goto loc_00A9AD8A;
    result = EtwpCheckForPoolTagFilterExtension(result, 0, (unsigned __int8)(v_rbx + 1), a4);
    if (sign_flag) goto loc_00A9AD9B;
    *(unsigned __int16 *)(v_rip + 4606727 + (unsigned int)(v_stack_p40) + (unsigned int)(v_stack_p40) * 4 * 4) = (unsigned __int16)(v_rbx + 1);
    *(unsigned int *)(v_rip + 4606727 + (unsigned int)(v_stack_p40) + (unsigned int)(v_stack_p40) * 4 * 4 + 4) = 42;
loc_00A9AD8A:
    result = EtwpUpdateLoggerGroupMasks(result, 0, (unsigned __int8)(v_rbx + 1), a4);
    if (!sign_flag) goto loc_00A9ADCA;
loc_00A9AD9B:
    *(unsigned int *)(result + 40) = (unsigned int)((unsigned int)((unsigned int)(result)));
    result = EtwpStopLoggerInstance(result, 0, (unsigned __int8)(v_rbx + 1), a4);
    if (((*(unsigned int *)(result + 12)) & (0x400ULL)) == 0) goto loc_00A9ADCA;
    result = EtwpGetLoggerInfoFromContext(0, result, (unsigned __int8)(v_rbx + 1), a4);
    result = EtwpReleaseLoggerContext(result, (unsigned __int8)(v_rbx + 1), (unsigned __int8)(v_rbx + 1), a4);
    goto loc_00A9ACE2;
loc_00A9ADCA:
    result = v_stack_p48;
    if (((unsigned __int8)(v_stack_p48)) != 9) {
        a3 = *(unsigned int *)(result);
        a4 = (unsigned int)(v_stack_p48);
        a2 = v_stack_p68;
        a1 = a2;
        result = EtwpUpdatePerProcessTracing(a1, a2, a3, a4);
    }
    result = EtwpGetLoggerInfoFromContext(a2, result, a3, a4);
    result = EtwpReleaseLoggerContext(result, (unsigned __int8)(v_rbx + 1), a3, a4);
    goto loc_00A9A093;
}
```

## 5. (Beta) C Style

```c
int64_t EtwpStartLogger(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint32_t v_stack_m108;
    uint64_t v_stack_m118;
    uint32_t v_stack_m124;
    uint32_t v_stack_m128;
    uint32_t v_stack_m138;
    uint32_t v_stack_m140;
    uint64_t v_stack_m148;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint16_t v_stack_mD6;
    uint16_t v_stack_mD8;
    uint32_t v_stack_mDC;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint32_t v_stack_p40;
    uint64_t v_stack_p44;
    uint8_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint32_t v_stack_p60;
    uint32_t v_stack_p68;
    uint64_t v_stack_p70;
    uint64_t v_stack_p78;

    v_stack_p18 = local_rbx;
    local_rsp = (local_rsp) - (304);
    result = (*(uint64_t *)(v_rip + 0x37099D)) ^ (local_rsp);
    v_stack_m48 = result;
    local_rbx = 0;
    v_stack_m100 = Arg1;
    v_stack_m124 = 0;
    v_stack_mD6 = 0;
    v_stack_mF8 = 0;
    v_stack_m108 = 0;
    Arg2 = 0;
    v_stack_m128 = 8;
    v_stack_mB8 = v_xmm0;
    v_stack_mF0 = v_xmm0;
    v_stack_m118 = v_xmm1;
    result = RtlInitUnicodeString(v_stack_m118, Arg2, a3, a4);
    Arg2 = 0;
    result = RtlInitUnicodeString(v_stack_mF0, Arg2, a3, a4);
    local_r15 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0x40))) & (0x9DECE5FFULL));
    if ((((uint8_t)(local_r15)) & (3)) != 0) goto loc_00A99E20;
    if ((((uint8_t)(local_r15)) & (8)) != 0) goto loc_00A99E1D;
    if ((((uint8_t)(local_r15)) & (4)) != 0) {
        local_r15 = (uint32_t)((local_r15) | ((uint32_t)(local_rbx + 1)));
    }
    if (!(condition_is_above_or_equal)) {
    }
    if (condition_is_above_or_equal) goto loc_00A99E3F;
    if (!(condition_is_above_or_equal)) {
    }
    if ((*(uint16_t *)(arg2 + 0x90)) <= 0) goto loc_00A9A035;
    if ((*(uint64_t *)(arg2 + 0x98)) == 0) goto loc_00A9A035;
    result = EtwpCaptureString(Arg2 + 144, v_stack_m118, a3, a4);
    if ((uint32_t)(result) != 0) goto loc_00A9A03A;
    if (condition_is_above_or_equal) goto loc_00A99EB1;
    if ((*(uint64_t *)(arg2 + 0x88)) != 0) goto loc_00A9A035;
    if ((((uint8_t)(local_r15)) & (15)) != 0) goto loc_00A9A035;
    if (((256) & ((uint32_t)(local_r15))) != 0) {
    }
    if ((*(uint32_t *)(arg2 + 0x44)) != 0) {
        *(uint32_t *)(arg2 + 0x44) = 0;
    }
    if ((*(uint32_t *)(arg2 + 0x4C)) != 0) {
        *(uint32_t *)(arg2 + 0x4C) = 0;
    }
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r15))) & (3));
    if (((uint8_t)(result)) == 3) goto loc_00A9A035;
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r15))) & ((uint32_t)((uint32_t)(0xC000ULL))));
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0xC000ULL)))) goto loc_00A9A035;
    if ((((uint32_t)(local_r15)) & (0x700ULL)) != 0) goto loc_00A99EE7;
    if ((*(uint64_t *)(arg2 + 0x88)) == 0) goto loc_00A9A035;
loc_00A99EE7:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r15))) & (6));
    if (((uint8_t)(result)) == 6) goto loc_00A9A035;
    if (((2) & ((uint8_t)(local_r15))) == 0) goto loc_00A99F0A;
    if ((*(uint32_t *)(arg2 + 0x3C)) == 0) goto loc_00A9A035;
loc_00A99F0A:
    if ((((uint8_t)(local_r15)) & (32)) == 0) goto loc_00A99F2B;
    if ((*(uint32_t *)(arg2 + 0x3C)) == 0) goto loc_00A9A035;
    if (((12) & ((uint8_t)((uint32_t)(*(uint32_t *)(arg2 + 0x40))))) != 0) goto loc_00A9A035;
loc_00A99F2B:
    if ((((uint8_t)(local_r15)) & (64)) == 0) goto loc_00A99F5D;
    if (((2) & ((uint8_t)((uint32_t)(*(uint32_t *)(arg2 + 0x70))))) == 0) goto loc_00A9A035;
    if ((((uint32_t)(local_r15)) & (0x402ULL)) != 0) goto loc_00A99F5D;
    if (((256) & ((uint32_t)(local_r15))) == 0) goto loc_00A9A035;
    if ((*(uint64_t *)(arg2 + 0x88)) != 0) goto loc_00A9A035;
loc_00A99F5D:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r15))) & ((uint32_t)((uint32_t)(0xC00000ULL))));
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0xC00000ULL)))) goto loc_00A9A035;
    if ((((uint8_t)(local_r15)) & (8)) == 0) goto loc_00A99FE8;
    if ((*(uint64_t *)(arg2 + 0x88)) == 0) goto loc_00A9A035;
    if (((2) & ((uint8_t)(local_r15))) != 0) goto loc_00A9A035;
    if ((*(uint32_t *)(arg2 + 0x3C)) == 0) goto loc_00A9A035;
    if (((2) & ((uint8_t)((uint32_t)(*(uint32_t *)(arg2 + 0x70))))) != 0) goto loc_00A9A035;
    if (condition_is_below) goto loc_00A9A035;
    if ((*(uint64_t *)(arg2 + 0x18)) != (*(uint64_t *)(v_rip - 0xA88079))) goto loc_00A99FC8;
    if ((*(uint64_t *)(arg2 + 0x20)) == (*(uint64_t *)(v_rip - 0xA8807E))) goto loc_00A9A035;
loc_00A99FC8:
    if ((*(uint64_t *)(arg2 + 0x18)) != (*(uint64_t *)(v_rip - 0xA6EF03))) goto loc_00A99FE2;
    if ((*(uint64_t *)(arg2 + 0x20)) == (*(uint64_t *)(v_rip - 0xA6EF08))) goto loc_00A9A035;
loc_00A99FE2:
    if ((((uint8_t)(local_r15)) & (4)) != 0) goto loc_00A9A035;
loc_00A99FE8:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x40))))) & ((uint32_t)((uint32_t)(0x3000000ULL))));
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0x3000000ULL)))) goto loc_00A9A035;
    if (((uint32_t)(result)) >= ((uint32_t)((uint32_t)(0x3000000ULL)))) goto loc_00A9A007;
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x40)))) & (262)) != 0) goto loc_00A9A035;
loc_00A9A007:
    if (condition_is_below) goto loc_00A9A035;
    if (((*(uint8_t *)(arg2 + 0x50)) & (4)) == 0) goto loc_00A9A103;
    if ((*(uint64_t *)(v_rip + 0x53FF19)) == 0) goto loc_00A9A0BD;
    if ((*(uint64_t *)(v_rip + 0x53FF19)) >= 0) goto loc_00A9A035;
    if ((*(uint64_t *)(v_rip + 0x53FF19)) >= 0) goto loc_00A9A103;
loc_00A9A035:
loc_00A9A03A:
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x4657FF), v_rip - 10976816, 2, a4);
    if ((uint8_t)(result) != 0) {
        v_stack_m138 = (uint32_t)(local_r15);
        result = v_stack_mF0;
        v_stack_m140 = (uint32_t)((uint32_t)(0xC000000DULL));
        a4 = v_stack_m118;
        Arg2 = v_rip - 10976851;
        v_stack_m148 = result;
        result = EtwpEventWriteTemplateAdmin(*(uint64_t *)(v_rip + 0x4657FF), Arg2, 2, a4);
    }
    result = RtlFreeAnsiString(v_stack_m118, Arg2, 2, a4);
    result = RtlFreeAnsiString(v_stack_mF0, Arg2, 2, a4);
    result = EtwpFreeSecurityDescriptor(v_stack_mF8, Arg2, 2, a4);
loc_00A9A093:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, 2, a4);
    local_rsp = (local_rsp) + (304);
    return result;
loc_00A9A0BD:
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x46577C), v_rip - 10974483, 2, a4);
    if ((uint8_t)(result) == 0) goto loc_00A9A03A;
    v_stack_p28 = v_stack_p78;
    v_stack_p20 = v_stack_p50;
    result = EtwpEventWriteTemplateSessionFromCapturedData(*(uint64_t *)(v_rip + 0x46577C), v_rip - 10974483, Arg2 + 24, (uint32_t)(*(uint32_t *)(arg2 + 0x40)));
    goto loc_00A9A03A;
loc_00A9A103:
    if (!sign_flag) goto loc_00A9A15A;
    if ((*(uint8_t *)(v_rip + 0x465173)) != ((uint8_t)(v_stack_p18))) goto loc_00A9A035;
    if ((((uint8_t)(Arg2 + 24)) & ((uint8_t)((uint32_t)(*(uint32_t *)(arg2 + 0x70))))) == 0) goto loc_00A9A035;
    if (condition_is_above_or_equal) goto loc_00A9A035;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0x28))) - ((uint32_t)(Arg2 + 24)));
    if ((((uint32_t)(result)) & (0xFFFFFFFDULL)) == 0) goto loc_00A9A035;
    if ((*(uint64_t *)(arg2 + 0x18)) != (*(uint64_t *)(v_rip - 0xA88E77))) goto loc_00A9A15A;
    if ((*(uint64_t *)(arg2 + 0x20)) == (*(uint64_t *)(v_rip - 0xA88E7C))) goto loc_00A9A035;
loc_00A9A15A:
    result = EtwpValidateFlagExtension(Arg2, v_rip - 10974483, Arg2 + 24, (uint32_t)(*(uint32_t *)(arg2 + 0x40)));
    if (sign_flag) goto loc_00A9A03A;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_r15))) & (256));
    Arg1 = (uint32_t)((Arg1) >> (3));
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) | (64));
    if ((*(uint16_t *)(arg2 + 0x80)) == ((uint16_t)(v_stack_p18))) { local_rsi = (uint32_t)(Arg1); }
    result = EtwpLookupLoggerIdByName(Arg1, v_stack_p50, v_stack_p44, (uint32_t)(*(uint32_t *)(arg2 + 0x40)));
    if ((uint32_t)(result) != 0) goto loc_00A9A1A8;
loc_00A9A19E:
    goto loc_00A9A03A;
loc_00A9A1A8:
    if ((*(uint64_t *)(arg2 + 0x18)) != (*(uint64_t *)(v_rip - 0xA88EE3))) goto loc_00A9A1D7;
    if ((*(uint64_t *)(arg2 + 0x20)) != (*(uint64_t *)(v_rip - 0xA88EE8))) goto loc_00A9A1D7;
    result = ExUuidCreate(v_stack_mB8, v_stack_p50, v_stack_p44, (uint32_t)(*(uint32_t *)(arg2 + 0x40)));
    if (sign_flag) goto loc_00A9A03A;
    goto loc_00A9A1E1;
loc_00A9A1D7:
    v_stack_mB8 = v_xmm0;
loc_00A9A1E1:
    if ((((uint32_t)(local_r15)) & (0xC00000ULL)) != 0) goto loc_00A9A220;
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == ((uint8_t)(v_stack_p18))) goto loc_00A9A21B;
    result = PsGetProcessSessionId(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), v_stack_p50, v_stack_p44, (uint32_t)(*(uint32_t *)(arg2 + 0x40)));
    if ((uint32_t)(result) == 0) goto loc_00A9A21B;
    goto loc_00A9A220;
loc_00A9A21B:
loc_00A9A220:
    v_stack_mD0 = *(uint64_t *)(arg1 + 0x2C8);
    if (v_stack_mB8 != (*(uint64_t *)(v_rip - 0xA882EB))) goto loc_00A9A245;
    if (v_stack_mB0 == (*(uint64_t *)(v_rip - 0xA882FB))) goto loc_00A9A25F;
loc_00A9A245:
    if (v_stack_mB8 != (*(uint64_t *)(v_rip - 0xA6F17C))) goto loc_00A9A360;
    if (v_stack_mB0 != (*(uint64_t *)(v_rip - 0xA6F181))) goto loc_00A9A360;
loc_00A9A25F:
    result = RtlFreeAnsiString(v_stack_p50, v_stack_mB8, v_stack_p44, (uint32_t)(*(uint32_t *)(arg2 + 0x40)));
    if (v_stack_mB8 != (*(uint64_t *)(v_rip - 0xA88334))) goto loc_00A9A290;
    if (v_stack_mB0 != (*(uint64_t *)(v_rip - 0xA88339))) goto loc_00A9A290;
    goto loc_00A9A2A1;
loc_00A9A290:
    v_stack_p40 = (uint32_t)(local_rbx + 1);
loc_00A9A2A1:
    v_stack_p44 = 2;
    result = RtlCreateUnicodeString(v_stack_p50, v_rip + 446159, v_stack_p44, (uint32_t)(*(uint32_t *)(arg2 + 0x40)));
    if ((uint8_t)(result) != 0) goto loc_00A9A2BD;
loc_00A9A2B3:
    goto loc_00A9A03A;
loc_00A9A2BD:
    if (condition_is_below) goto loc_00A9A035;
    Arg2 = ((uint32_t)(0xC0000017ULL)) | (local_rbx + 1);
loc_00A9A2DE:
    if (condition_is_not_equal) goto loc_00A9A19E;
loc_00A9A2E4:
    result = ExAcquireRundownProtectionCacheAwareEx(*(uint64_t *)(*(uint64_t *)(arg1 + 0x2C0) + (uint32_t)(v_stack_p44) * 8), (uint32_t)((uint32_t)(local_rbx + 1)), v_stack_p44, (uint32_t)(*(uint32_t *)(arg2 + 0x40)));
    local_rbx = 0;
    if ((*(uint32_t *)(arg2 + 0x70)) < 0) goto loc_00A9A611;
    result = EtwpGetSecurityDescriptorByGuid(v_stack_mB8, v_stack_p70, v_stack_p44, (uint32_t)(*(uint32_t *)(arg2 + 0x40)));
    a3 = 0;
    result = EtwpAccessCheck(v_stack_p70, (uint32_t)((uint32_t)(local_rsi)), a3, (uint32_t)(*(uint32_t *)(arg2 + 0x40)));
    if (!sign_flag) goto loc_00A9A611;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x46550B), v_rip - 10977268, a3, (uint32_t)(*(uint32_t *)(arg2 + 0x40)));
    if ((uint8_t)(result) == 0) goto loc_00A9A7F7;
    v_stack_p20 = (uint32_t)(local_rsi);
    result = EtwpEventWriteTemplateSessionDesiredAccess(*(uint64_t *)(v_rip + 0x46550B), v_rip - 10977268, v_stack_p50, v_stack_mB8);
    goto loc_00A9A7F7;
loc_00A9A360:
    if ((v_rip - 10977268) != (*(uint64_t *)(v_rip + 0xBFD49))) goto loc_00A9A3CD;
    if ((*(uint64_t *)(v_rip + 0x46550B)) != (*(uint64_t *)(v_rip + 0xBFD48))) goto loc_00A9A3CD;
    v_stack_p44 = (uint32_t)(local_rbx + 1);
    result = EtwpGetFlagExtension(Arg2, (uint32_t)((uint32_t)(local_rbx + 1)), v_stack_p50, v_stack_mB8);
    if (result == 0) goto loc_00A9A3B9;
    if (condition_is_below) goto loc_00A9A035;
    result = RtlFreeAnsiString(v_stack_p50, (uint32_t)((uint32_t)(local_rbx + 1)), v_stack_p50, v_stack_mB8);
    result = RtlCreateUnicodeString(v_stack_p50, v_rip + 445965, v_stack_p50, v_stack_mB8);
    if ((uint8_t)(result) == 0) goto loc_00A9A2B3;
    v_stack_p40 = 0;
loc_00A9A3B9:
    Arg1 = ((uint32_t)((uint32_t)(result))) | (local_rbx + 1);
    goto loc_00A9A2DE;
loc_00A9A3CD:
    if ((v_rip + 445965) != (*(uint64_t *)(v_rip - 0xA6F214))) goto loc_00A9A42E;
    if (Arg1 != (*(uint64_t *)(v_rip - 0xA6F215))) goto loc_00A9A42E;
    v_stack_p44 = 3;
    if (Arg1 < (*(uint64_t *)(v_rip - 0xA6F215))) goto loc_00A9A035;
    result = RtlFreeAnsiString(v_stack_p50, v_rip + 445965, v_stack_p50, v_stack_mB8);
    result = RtlCreateUnicodeString(v_stack_p50, v_rip + 445757, v_stack_p50, v_stack_mB8);
    if ((uint8_t)(result) == 0) goto loc_00A9A2B3;
    Arg1 = ((uint32_t)((uint32_t)(result))) | (local_rbx + 1);
    goto loc_00A9A2DE;
loc_00A9A42E:
    result = wcsicmp(v_stack_p58, v_rip + 445702, v_stack_p50, v_stack_mB8);
    if ((uint32_t)(result) != 0) goto loc_00A9A465;
    if (v_stack_mB8 != (*(uint64_t *)(v_rip - 0xA6F28E))) goto loc_00A9A19E;
    if (v_stack_mB0 != (*(uint64_t *)(v_rip - 0xA6F297))) goto loc_00A9A19E;
loc_00A9A465:
    if ((*(uint32_t *)(arg1 + 0x10)) <= 4) goto loc_00A9A4BB;
loc_00A9A470:
    a3 = 0;
    result = EtwpAcquireLoggerContextByLoggerId(Arg1, 4, a3, v_stack_mB8);
    if (result == 0) goto loc_00A9A4A6;
    if ((*(uint64_t *)(result + 0x114)) != v_stack_mB8) goto loc_00A9A49C;
    if ((*(uint64_t *)(result + 0x11C)) == v_stack_mB0) goto loc_00A9A4B1;
loc_00A9A49C:
    Arg2 = 0;
    result = EtwpReleaseLoggerContext(result, Arg2, a3, v_stack_mB8);
loc_00A9A4A6:
    local_rbx = (uint32_t)((4) + ((uint32_t)(local_rbx + 1)));
    if (((uint32_t)(local_rbx)) < (*(uint32_t *)(arg1 + 0x10))) goto loc_00A9A470;
    goto loc_00A9A4BB;
loc_00A9A4B1:
    Arg2 = 0;
    result = EtwpReleaseLoggerContext(result, Arg2, a3, v_stack_mB8);
loc_00A9A4BB:
    if (((uint32_t)(local_rbx)) < ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x10))))) goto loc_00A9A19E;
    v_stack_p44 = 4;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x10)))) <= 4) goto loc_00A9A4FA;
    Arg2 = ((uint32_t)((uint32_t)(result))) | (local_rbx + 1);
loc_00A9A4DA:
    if (condition_is_equal) goto loc_00A9A4FA;
    result = (uint32_t)(((uint32_t)(v_stack_p44)) + ((uint32_t)(local_rbx + 1)));
    v_stack_p44 = (uint32_t)(result);
    if (((uint32_t)(result)) < (*(uint32_t *)(arg1 + 0x10))) goto loc_00A9A4DA;
loc_00A9A4FA:
    if (v_stack_p44 < ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x10))))) goto loc_00A9A2E4;
    local_rbx = 0;
    if ((*(uint8_t *)(v_rip + 0x3A4729)) != 0) goto loc_00A9A5D7;
    v_stack_mA8 = Arg1 + 16;
    *(uint8_t *)(v_rip + 0x3A4702) = (uint8_t)(local_rbx + 1);
    v_stack_p20 = v_stack_mA8;
    a3 = 0;
    v_stack_mA0 = 4;
    result = EtwWrite(*(uint64_t *)(v_rip + 0x465323), v_rip - 10974204, a3, (uint32_t)((uint32_t)(local_rbx + 1)));
    if ((*(uint32_t *)(v_rip + 0x36EC12)) <= 5) goto loc_00A9A5D7;
    result = tlgKeywordOn(v_rip + 3599359, v_rip - 10974204, a3, (uint32_t)((uint32_t)(local_rbx + 1)));
    if ((uint8_t)(result) != 0) {
        result = v_stack_mC8;
        v_stack_mC8 = local_rbx + 1;
        v_stack_m78 = result;
        a4 = local_rbx + 5;
        result = v_stack_mC0;
        v_stack_m70 = 8;
        v_stack_m68 = result;
        Arg2 = v_rip - 10774781;
        result = *(uint32_t *)(arg1 + 0x10);
        Arg1 = v_rip + 3599300;
        v_stack_p68 = (uint32_t)(result);
        result = v_stack_p68;
        v_stack_m58 = result;
        result = v_stack_m98;
        v_stack_p20 = result;
        v_stack_mC0 = 0x1000000ULL;
        v_stack_m60 = 8;
        v_stack_m50 = 4;
        result = tlgWriteAgg(Arg1, Arg2, a3, a4);
    }
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x465262), v_rip - 10973221, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00A9A03A;
    result = EtwpEventWriteTemplateSessionMaxLoggers(*(uint64_t *)(v_rip + 0x465262), v_rip - 10973255, v_stack_p50, (uint32_t)(*(uint32_t *)(arg1 + 0x10)));
    goto loc_00A9A03A;
loc_00A9A611:
    if ((*(uint64_t *)(v_rip - 0xA6F498)) != v_stack_mB8) goto loc_00A9A631;
    if ((*(uint64_t *)(v_rip - 0xA6F49D)) != v_stack_mB0) goto loc_00A9A631;
    v_stack_p48 = 0;
    goto loc_00A9A655;
loc_00A9A631:
    result = memcmp(v_rip - 10941986, v_stack_mB8, 16, (uint32_t)(*(uint32_t *)(arg1 + 0x10)));
    result = (uint32_t)(-(result));
    Arg1 = (uint8_t)((v_rip - 10941986) & (8));
    Arg1 = (uint8_t)((Arg1) + ((uint8_t)(local_rbx + 1)));
    v_stack_p48 = (uint8_t)(Arg1);
loc_00A9A655:
    if (((*(uint32_t *)(arg2 + 0x40)) & (0x2000000ULL)) == 0) goto loc_00A9A6F8;
    if (v_stack_p40 != 8) goto loc_00A9A6F8;
    if ((*(uint32_t *)(arg2 + 0x70)) < 0) goto loc_00A9A692;
    a3 = 0;
    result = EtwpCheckGuidAccess(v_rip - 11044670, 128, a3, (uint32_t)(*(uint32_t *)(arg1 + 0x10)));
    if (sign_flag) goto loc_00A9A7F7;
loc_00A9A692:
    v_stack_p40 = 2;
loc_00A9A69B:
    if (condition_is_above_or_equal) goto loc_00A9A6F8;
    local_rdi = (uint32_t)((2) + ((uint32_t)(local_rbx + 1)));
    v_stack_p40 = (uint32_t)(local_rdi);
    if (((uint32_t)(local_rdi)) < 8) goto loc_00A9A69B;
    v_stack_p40 = (uint32_t)((uint32_t)((uint32_t)(local_rdi)));
    if (((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) != 8) goto loc_00A9A6F8;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x46517D), v_rip - 10981322, a3, (uint32_t)(*(uint32_t *)(arg1 + 0x10)));
    if ((uint8_t)(result) == 0) goto loc_00A9A7F7;
    result = EtwpEventWriteTemplateSessionMaxLoggers(*(uint64_t *)(v_rip + 0x46517D), v_rip - 10981358, v_stack_p50, 8);
    goto loc_00A9A7F7;
loc_00A9A6F8:
    result = EtwpInitLoggerContext(v_stack_p50, (uint32_t)((uint32_t)(local_r15)), (uint32_t)(*(uint32_t *)(arg2 + 0x70)), 8);
    result = EtwpGetFlagExtension(Arg2, 6, (uint32_t)(*(uint32_t *)(arg2 + 0x70)), 8);
    if (result == 0) goto loc_00A9A81B;
    Arg1 = (uint16_t)((*(uint16_t *)(result)) << (2));
    if (((uint16_t)(Arg1)) != ((uint16_t)(6 + 6))) goto loc_00A9A81B;
    result = EtwpSetPartitionContext(result + 1600, *(uint64_t *)(result + 0x4), (uint32_t)(*(uint32_t *)(arg2 + 0x70)), 8);
    if (!sign_flag) goto loc_00A9A81B;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x4650E7), v_rip - 10982744, (uint32_t)(*(uint32_t *)(arg2 + 0x70)), 8);
    if ((uint8_t)(result) != 0) {
        a4 = *(uint64_t *)(result + 0x4);
        a3 = v_stack_p50;
        result = EtwpEventWriteTemplateSessionAndHandle(*(uint64_t *)(v_rip + 0x4650E7), v_rip - 10982744, a3, a4);
    }
loc_00A9A77B:
    if (((*(uint32_t *)(result + 0xC)) & (0x2000000ULL)) != 0) {
    }
    result = EtwpFreeApcPool(result + 832, v_rip - 10982744, a3, a4);
    result = (uint32_t)(*(uint32_t *)(result + 0x330));
    if (sign_flag) {
        Arg1 = *(uint64_t *)(result + 0x418);
        Arg2 = 0;
        result = ExFreePoolWithTag(Arg1, Arg2, a3, a4);
    }
    if (((*(uint32_t *)(result + 0x330)) & (0x2000ULL)) != 0) {
    }
    result = RtlFreeAnsiString(result + 152, Arg2, a3, a4);
    result = RtlFreeAnsiString(result + 168, Arg2, a3, a4);
    if (*(uint64_t *)(result + 0x320) != 0) {
        result = ZwClose(*(uint64_t *)(result + 0x320), Arg2, a3, a4);
    }
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, a3, a4);
loc_00A9A7F7:
    result = ExReleaseRundownProtectionCacheAwareEx(*(uint64_t *)(*(uint64_t *)(arg1 + 0x2C0) + (uint32_t)(v_stack_p44) * 8), (uint32_t)((uint32_t)(local_rbx + 1)), a3, a4);
    goto loc_00A9A03A;
loc_00A9A81B:
    result = RtlFreeAnsiString(v_stack_p50, (uint32_t)((uint32_t)(local_rbx + 1)), a3, a4);
    a3 = 0;
    if (result != 0) goto loc_00A9A834;
    goto loc_00A9A7F7;
loc_00A9A834:
    *(uint64_t *)(result + 0x114) = v_xmm0;
    *(uint32_t *)(result + 0x124) = (uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x3C)));
    if (((*(uint8_t *)(arg2 + 0x50)) & ((uint8_t)(local_rbx + 1))) != 0) {
    }
    *(uint32_t *)(result + 0xC8) = (uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x28)));
    if (((*(uint8_t *)(arg2 + 0x50)) & (2)) == 0) goto loc_00A9A87B;
    result = EtwpSetQpcDeltaTracking(result, (uint32_t)((uint32_t)(local_rbx + 1)), a3, a4);
    if (sign_flag) goto loc_00A9A777;
loc_00A9A87B:
    if (((*(uint8_t *)(arg2 + 0x50)) & (8)) != 0) {
    }
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x44))) == 0) goto loc_00A9A89A;
    *(uint32_t *)(result + 0xD0) = (uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x44)));
    goto loc_00A9A8B9;
loc_00A9A89A:
    result = (uint32_t)(*(uint32_t *)(arg2 + 0x44));
    if (!(condition_is_above_or_equal)) {
        result = (uint8_t)(local_r15);
        result = (uint8_t)((result) & (16));
        result = (uint8_t)(-(result));
        Arg1 = (uint32_t)((result) & (999));
        Arg1 = (uint32_t)((Arg1) + ((uint32_t)(local_rbx + 1)));
        *(uint32_t *)(result + 0xD0) = (uint32_t)(Arg1);
    }
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x4C))) == 0) goto loc_00A9A8D7;
    if ((*(uint32_t *)(result + 0xD0)) > 0) goto loc_00A9A8D0;
    if (sign_flag) {
        *(uint32_t *)(arg2 + 0x4C) = 0;
        Arg1 = 0;
    }
    *(uint32_t *)(result) = (uint32_t)((uint32_t)(v_stack_p44));
    *(uint32_t *)(result + 0xD4) = (uint32_t)(Arg1);
    *(void **)(result + 0x550) = Arg1;
    if ((*(uint16_t *)(arg2 + 0x80)) <= 0) goto loc_00A9A91E;
    if ((*(uint64_t *)(arg2 + 0x88)) == 0) goto loc_00A9A91E;
    result = EtwpCaptureString(Arg2 + 128, v_stack_p78, a3, a4);
    a3 = 0;
    if (sign_flag) goto loc_00A9A777;
loc_00A9A91E:
    result = (uint32_t)(*(uint32_t *)(arg2 + 0x70));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg2 + 0x70)))) & (2)) != 0) {
        result = *(uint32_t *)(arg2 + 0x60);
        *(uint32_t *)(result + 0x128) = (uint32_t)(result);
        *(uint32_t *)(arg2 + 0x60) = 0;
    }
    Arg2 = 0;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (8)) == 0) goto loc_00A9A978;
    *(uint64_t *)(result + 0xA8) = v_xmm0;
    result = RtlInitUnicodeString(v_stack_p78, Arg2, a3, a4);
    result = EtwpGenerateFileName(result + 168, result + 296, result + 152, a4);
    if (sign_flag) goto loc_00A9A9AA;
    goto loc_00A9A983;
loc_00A9A978:
    *(uint64_t *)(result + 0x98) = v_xmm0;
    result = RtlInitUnicodeString(result + 168, result + 296, result + 152, a4);
loc_00A9A983:
    result = Feature_1899207995__private_IsEnabledDeviceUsageNoInline(result + 168, result + 296, result + 152, a4);
    a3 = 0;
    if ((uint32_t)(result) == 0) goto loc_00A9A9B4;
    Arg1 = (uint32_t)((*(uint16_t *)(result + 0x88)) + ((uint32_t)(*(uint16_t *)(result + 0x98))));
    if (((uint32_t)(Arg1)) <= 0x7FFFULL) goto loc_00A9A9B4;
loc_00A9A9AA:
    goto loc_00A9A777;
loc_00A9A9B4:
    result = *(uint16_t *)(result + 0x98);
    local_rdi = (uint32_t)(0xC000000DULL);
    if ((*(uint32_t *)(arg2 + 0x70)) >= 0) {
        Arg1 = *(uint64_t *)(gs_base + (0 + 0x188));
        a4 = result + 704;
        result = 12;
        v_stack_mDC = 2;
        Arg2 = v_stack_mE0;
        v_stack_mE0 = (uint32_t)(result);
        v_stack_mD8 = 257;
        result = SeCreateClientSecurity(Arg1, Arg2, a3, a4);
        local_rdi = (uint32_t)(result);
        a3 = 0;
    }
    if (sign_flag) goto loc_00A9A9AA;
    if (((*(uint32_t *)(result + 0xC)) & (256)) == 0) goto loc_00A9AA04;
    goto loc_00A9AA0C;
loc_00A9AA04:
loc_00A9AA0C:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg2 + 0x70)))) & (2)) != 0) {
    }
    if ((*(uint32_t *)(arg2 + 0x70)) < 0) {
    }
    if ((((uint8_t)(local_rbx + 1)) & ((uint8_t)((uint32_t)(*(uint32_t *)(arg2 + 0x70))))) != 0) {
    }
    if (((*(uint32_t *)(arg2 + 0x70)) & ((uint32_t)((uint32_t)(0x4000ULL)))) != 0) {
    }
    result = EtwpInitializeTimeStamp(result, Arg2, a3, a4);
    if (((uint32_t)((uint32_t)(v_stack_p40))) >= 8) goto loc_00A9AAB6;
    *(uint8_t *)(result + 0x332) = (uint8_t)((uint32_t)(v_stack_p40));
    if (((uint32_t)((uint32_t)(v_stack_p40))) <= ((uint32_t)(local_rbx + 1))) {
    }
    *(uint8_t *)(v_stack_p68 + (uint32_t)(v_stack_p40) * 2 + 0x1198) = (uint8_t)(v_stack_p44);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0xC8))) - ((uint32_t)(local_rbx + 1)));
    if (((uint32_t)(result)) >= 4) goto loc_00A9AAA0;
    goto loc_00A9AAA3;
loc_00A9AAA0:
loc_00A9AAA3:
    *(uint8_t *)(v_stack_p68 + (uint32_t)(v_stack_p40) * 2 + 0x1199) = (uint8_t)((uint8_t)(local_rbx + 1));
    goto loc_00A9AABB;
loc_00A9AAB6:
loc_00A9AABB:
    result = EtwpCheckForStackTracingExtension(Arg2, result, a3, a4);
    a3 = 0;
    if (sign_flag) goto loc_00A9A77B;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x34))) != 0) {
        *(uint32_t *)(result + 0xE0) = (uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x34)));
    }
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x38))) != 0) {
        *(uint32_t *)(result + 0xEC) = (uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x38)));
    }
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x30))) == 0) goto loc_00A9AB0C;
    result = (uint32_t)(*(uint32_t *)(arg2 + 0x30));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x30)))) >= = ((uint32_t)((uint32_t)(0x4000ULL)))) {
        *(uint32_t *)(arg2 + 0x30) = (uint32_t)((uint32_t)(0x4000ULL));
        result = (uint32_t)((uint32_t)(0x4000ULL));
    }
    result = (uint32_t)((result) << (10));
    *(uint32_t *)(result + 0x4) = (uint32_t)(result);
loc_00A9AB0C:
    if (((*(uint8_t *)(arg2 + 0x50)) & (4)) != 0) {
        result = *(uint32_t *)(result + 0x4);
        result = (uint32_t)((result) + (0x1FFFFFULL));
        result = (uint32_t)((result) & (0xFFE00000ULL));
        *(uint32_t *)(result + 0x4) = (uint32_t)(result);
    }
    if ((*(uint16_t *)(result + 0x98)) <= 0) goto loc_00A9AB90;
    *(uint64_t *)(result + 0x20) = *(uint64_t *)(gs_base + (0 + 0x188));
    goto loc_00A9AB70;
loc_00A9AB47:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != 0xC0000206ULL) goto loc_00A9A77B;
    Arg2 = (uint32_t)(((uint32_t)(v_stack_p60) - 1) + ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x4)))));
    result = (uint32_t)(((uint32_t)(v_stack_p60)) - 1);
    result = (uint32_t)(~(result));
    Arg2 = (uint32_t)((Arg2) & ((uint32_t)(result)));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x4)))) == ((uint32_t)(Arg2))) goto loc_00A9A77B;
    *(uint32_t *)(result + 0x4) = (uint32_t)(Arg2);
loc_00A9AB70:
    Arg2 = 0;
    result = EtwpCreateLogFile(result, Arg2, v_stack_p60, a4);
    a3 = 0;
    if (sign_flag) goto loc_00A9AB47;
loc_00A9AB90:
    if ((*(uint32_t *)(result + 0x4)) >= ((uint32_t)((uint32_t)(0x1000ULL)))) goto loc_00A9ABB4;
    if ((*(uint16_t *)(result + 0x98)) > 0) goto loc_00A9ABAD;
    if (((*(uint32_t *)(result + 0xC)) & (0x400ULL)) != 0) {
    }
    if (((uint32_t)(*(uint32_t *)(result + 0x4)) - 72) < ((uint32_t)(0xFFFFULL))) {
        Arg1 = (uint32_t)(*(uint32_t *)(result + 0x4)) - 72;
    }
    Arg1 = (uint32_t)((Arg1) & (0xFFFFFFF8ULL));
    *(uint32_t *)(result + 0x8) = (uint32_t)(Arg1);
    result = EtwpAllocateTraceBufferPool(result, (uint32_t)(*(uint32_t *)(result + 0x4)), a3, a4);
    a3 = 0;
    if (!sign_flag) goto loc_00A9ABEC;
loc_00A9ABDF:
    result = EtwpFreeTraceBufferPool(result, (uint32_t)(*(uint32_t *)(result + 0x4)), a3, a4);
    goto loc_00A9A77B;
loc_00A9ABEC:
    if (condition_is_above_or_equal) goto loc_00A9AC26;
    if (condition_is_below) goto loc_00A9AC26;
    result = ExAllocatePool2(64, (uint32_t)(*(uint32_t *)(result + 0x4)), (uint32_t)(0x5A777445ULL), a4);
    a3 = 0;
    *(uint64_t *)(result + 0x588) = result;
    if (result != 0) goto loc_00A9AC26;
    goto loc_00A9A77B;
loc_00A9AC26:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x124))) == 0) goto loc_00A9AC41;
    if (((*(uint32_t *)(result + 0xC)) & (0x2000ULL)) != 0) goto loc_00A9AC41;
    Arg2 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x124))))) << (20);
    goto loc_00A9AC46;
loc_00A9AC41:
loc_00A9AC46:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0xEC))) * (*(uint32_t *)(result + 0x4)));
    Arg2 = (uint32_t)(0xA00000ULL);
    if (((uint32_t)(0xA00000ULL)) <= (result + result * 1)) { Arg2 = result + result * 1; }
    *(void **)(result + 0x1A0) = Arg2;
    if ((*(uint32_t *)(arg2 + 0x70)) < 0) goto loc_00A9AC88;
    result = EtwpInitializeLoggerSecurityDescriptor(result, v_stack_p70, a3, a4);
    result = EtwpFreeSecurityDescriptor(v_stack_p70, v_stack_p70, a3, a4);
    if (sign_flag) goto loc_00A9ABDF;
loc_00A9AC88:
    result = ExAcquireRundownProtectionCacheAwareEx(*(uint64_t *)(*(uint64_t *)(v_stack_p68 + 0x2C0) + (uint32_t)(v_stack_p44) * 8), (uint32_t)((uint32_t)(local_rbx + 1)), a3, a4);
    local_r15 = 0;
    if (((*(uint32_t *)(result + 0xC)) & (0x400ULL)) != 0) goto loc_00A9ACEF;
    if ((*(uint32_t *)(arg2 + 0x70)) < 0) goto loc_00A9ACEF;
    result = PsGetCurrentServerSilo(*(uint64_t *)(*(uint64_t *)(v_stack_p68 + 0x2C0) + (uint32_t)(v_stack_p44) * 8), (uint32_t)((uint32_t)(local_rbx + 1)), a3, a4);
    result = EtwpStartLoggerThread(result, result, a3, a4);
    if (!sign_flag) goto loc_00A9ACEF;
    result = ExReleaseRundownProtectionCacheAwareEx(*(uint64_t *)(*(uint64_t *)(v_stack_p68 + 0x2C0) + (uint32_t)(v_stack_p44) * 8), (uint32_t)((uint32_t)(local_rbx + 1)), a3, a4);
loc_00A9ACE2:
    result = EtwpFreeLoggerContext(result, (uint32_t)((uint32_t)(local_rbx + 1)), a3, a4);
    goto loc_00A9A093;
loc_00A9ACEF:
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x464B4A), v_rip - 11038597, a3, a4);
    if ((uint8_t)(result) != 0) {
        a3 = result;
        Arg2 = v_rip - 11038616;
        result = EtwpEventWriteTemplateSession(*(uint64_t *)(v_rip + 0x464B4A), Arg2, a3, a4);
    }
    v_stack_p20 = 0;
    a4 = 0;
    a3 = 0;
    Arg2 = 0;
    result = KeWaitForSingleObject(result + 632, Arg2, a3, a4);
    a3 = 0;
    result = EtwpSendSessionNotification(result, a3 + 5, a3, a4);
    if (((*(uint32_t *)(result + 0xC)) & (0x2000000ULL)) == 0) goto loc_00A9ADCA;
    if (v_stack_p68 != (*(uint64_t *)(v_rip + 0x52BD50))) goto loc_00A9AD8A;
    result = EtwpCheckForPoolTagFilterExtension(result, 0, (uint8_t)(local_rbx + 1), a4);
    if (sign_flag) goto loc_00A9AD9B;
    *(uint16_t *)(v_rip + 0x464B07 + (uint32_t)(v_stack_p40) + (uint32_t)(v_stack_p40) * 4 * 4) = (uint16_t)(local_rbx + 1);
    *(uint32_t *)(v_rip + 0x464B07 + (uint32_t)(v_stack_p40) + (uint32_t)(v_stack_p40) * 4 * 4 + 0x4) = 42;
loc_00A9AD8A:
    result = EtwpUpdateLoggerGroupMasks(result, 0, (uint8_t)(local_rbx + 1), a4);
    if (!sign_flag) goto loc_00A9ADCA;
loc_00A9AD9B:
    *(uint32_t *)(result + 0x28) = (uint32_t)((uint32_t)((uint32_t)(result)));
    result = EtwpStopLoggerInstance(result, 0, (uint8_t)(local_rbx + 1), a4);
    if (((*(uint32_t *)(result + 0xC)) & (0x400ULL)) == 0) goto loc_00A9ADCA;
    result = EtwpGetLoggerInfoFromContext(0, result, (uint8_t)(local_rbx + 1), a4);
    result = EtwpReleaseLoggerContext(result, (uint8_t)(local_rbx + 1), (uint8_t)(local_rbx + 1), a4);
    goto loc_00A9ACE2;
loc_00A9ADCA:
    result = v_stack_p48;
    if (((uint8_t)(v_stack_p48)) != 9) {
        a3 = *(uint32_t *)(result);
        a4 = (uint32_t)(v_stack_p48);
        Arg2 = v_stack_p68;
        Arg1 = Arg2;
        result = EtwpUpdatePerProcessTracing(Arg1, Arg2, a3, a4);
    }
    result = EtwpGetLoggerInfoFromContext(Arg2, result, a3, a4);
    result = EtwpReleaseLoggerContext(result, (uint8_t)(local_rbx + 1), a3, a4);
    goto loc_00A9A093;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x10` | `32` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x2C0` | `64` | `R` |
| `Arg1` | `+ 0x2C8` | `64` | `R` |
| `Arg1` | `+ 0x11A8` | `32` | `R` |
| `Arg2` | `+ 0x0` | `16` | `R` |
| `Arg2` | `+ 0x18` | `64` | `R` |
| `Arg2` | `+ 0x18` | `128` | `R` |
| `Arg2` | `+ 0x20` | `64` | `R` |
| `Arg2` | `+ 0x28` | `32` | `R` |
| `Arg2` | `+ 0x30` | `32` | `R` |
| `Arg2` | `+ 0x30` | `32` | `W` |
| `Arg2` | `+ 0x34` | `32` | `R` |
| `Arg2` | `+ 0x38` | `32` | `R` |
| `Arg2` | `+ 0x3C` | `32` | `R` |
| `Arg2` | `+ 0x40` | `32` | `R` |
| `Arg2` | `+ 0x44` | `32` | `R` |
| `Arg2` | `+ 0x44` | `32` | `W` |
| `Arg2` | `+ 0x4C` | `32` | `R` |
| `Arg2` | `+ 0x4C` | `32` | `W` |
| `Arg2` | `+ 0x50` | `8` | `R` |
| `Arg2` | `+ 0x60` | `32` | `R` |
| `Arg2` | `+ 0x60` | `32` | `W` |
| `Arg2` | `+ 0x70` | `32` | `R` |
| `Arg2` | `+ 0x80` | `16` | `R` |
| `Arg2` | `+ 0x80` | `64` | `R` |
| `Arg2` | `+ 0x88` | `64` | `R` |
| `Arg2` | `+ 0x90` | `64` | `R` |
| `Arg2` | `+ 0x98` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A99D80&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
