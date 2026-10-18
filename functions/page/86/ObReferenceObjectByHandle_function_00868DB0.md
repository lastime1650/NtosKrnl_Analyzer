# ObReferenceObjectByHandle

- RVA: `0x00868DB0`–`0x00868DE4` (길이 `52` bytes)
- VA: `0x0000000140868DB0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00063458`
- 디코드: `11`개 명령, `52/52` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **307**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00868DD9` → [ObpReferenceObjectByHandleWithTag](ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)

### Direct callers
- [NtCancelTimer](../../text/23/NtCancelTimer_function_00230D90.md) at `0x00230DE3`
- [NtSetTimer](../../text/23/NtSetTimer_function_00231190.md) at `0x0023124F`
- [NtSetTimerEx](../../text/23/NtSetTimerEx_function_00231480.md) at `0x0023159D`
- [NtSetInformationFile](../../text/29/NtSetInformationFile_function_0029C5E0.md) at `0x0029CF91`
- [NtSetInformationFile](../../text/29/NtSetInformationFile_function_0029C5E0.md) at `0x0029D36B`
- [IopReferenceFileObject](../../text/29/IopReferenceFileObject_function_0029D530.md) at `0x0029D565`
- [NtShutdownWorkerFactory](../../text/2A/NtShutdownWorkerFactory_function_002A4E60.md) at `0x002A4EE6`
- [NtTraceEvent](../../text/2F/NtTraceEvent_function_002FA6C0.md) at `0x002FA819`
- [NtReleaseWorkerFactoryWorker](../../text/34/NtReleaseWorkerFactoryWorker_function_00343990.md) at `0x003439D6`
- [NtSetInformationWorkerFactory](../../text/35/NtSetInformationWorkerFactory_function_00350A30.md) at `0x00350C3E`
- [NtWaitForWorkViaWorkerFactory](../../text/39/NtWaitForWorkViaWorkerFactory_function_00394270.md) at `0x0039447D`
- [NtWaitForWorkViaWorkerFactory](../../text/39/NtWaitForWorkViaWorkerFactory_function_00394270.md) at `0x003947D4`
- [ExpSetTimer2](../../text/3A/ExpSetTimer2_function_003A0470.md) at `0x003A056B`
- [RtlCheckTokenCapability](../../text/3A/RtlCheckTokenCapability_function_003A5520.md) at `0x003A5833`
- [RtlCheckTokenMembershipEx](../../text/3A/RtlCheckTokenMembershipEx_function_003A5A30.md) at `0x003A5CC8`
- [SepInternalSetSecurityAttributesToken](../../text/3A/SepInternalSetSecurityAttributesToken_function_003A9474.md) at `0x003A94B2`
- [SmKmStoreHelperStart](../../text/3B/SmKmStoreHelperStart_function_003B1ACC.md) at `0x003B1B40`
- [SMKM_STORE&lt;SM_TRAITS&gt;::SmStWorkerThreadStartThread](../../text/3B/SMKM_STORE_SM_TRAITS_SmStWorkerThreadStartThread_function_003B200C.md) at `0x003B20D6`
- [IopValidateAndGetWriteParameters](../../text/40/IopValidateAndGetWriteParameters_function_00400C30.md) at `0x00400FC7`
- [NtCancelWaitCompletionPacket](../../text/42/NtCancelWaitCompletionPacket_function_0042F100.md) at `0x0042F157`
- [NtAssociateWaitCompletionPacket](../../text/42/NtAssociateWaitCompletionPacket_function_0042F270.md) at `0x0042F2D2`
- [NtAssociateWaitCompletionPacket](../../text/42/NtAssociateWaitCompletionPacket_function_0042F270.md) at `0x0042F34C`
- [NtAssociateWaitCompletionPacket](../../text/42/NtAssociateWaitCompletionPacket_function_0042F270.md) at `0x0042F385`
- [IopCheckInitiatorHint](../../text/45/IopCheckInitiatorHint_function_00457134.md) at `0x004571DD`
- [NtWorkerFactoryWorkerReady](../../text/47/NtWorkerFactoryWorkerReady_function_00474CF0.md) at `0x00474D38`
- [CmSiCreateEvent](../../text/47/CmSiCreateEvent_function_00478F6C.md) at `0x00478FF2`
- [SepLinkLogonSessions](../../text/4A/SepLinkLogonSessions_function_004AAE78.md) at `0x004AAF14`
- [EtwGetProviderIdFromHandle](../../text/4B/EtwGetProviderIdFromHandle_function_004B8850.md) at `0x004B888B`
- [CmpAdjustFileCFSafety](../../text/4B/CmpAdjustFileCFSafety_function_004BCEF8.md) at `0x004BCFB1`
- [SeSetLearningModeObjectInformation](../../text/4C/SeSetLearningModeObjectInformation_function_004C7098.md) at `0x004C7171`
- [PspMapView](../../text/4C/PspMapView_function_004C77E8.md) at `0x004C7834`
- [NtSubmitIoRing](../../text/4C/NtSubmitIoRing_function_004CF9E0.md) at `0x004CFAAD`
- [NtQueryInformationWorkerFactory](../../text/4D/NtQueryInformationWorkerFactory_function_004D4480.md) at `0x004D4568`
- [EtwpGetDriverDataDosPath](../../text/4D/EtwpGetDriverDataDosPath_function_004DDF10.md) at `0x004DDFE8`
- [SmFirstTimeInit](../../text/4E/SmFirstTimeInit_function_004EA944.md) at `0x004EAAEB`
- [WmipReceiveNotifications](../../text/4E/WmipReceiveNotifications_function_004EC280.md) at `0x004EC38E`
- [SepCreateAppContainerToken](../../text/4F/SepCreateAppContainerToken_function_004F43AC.md) at `0x004F449B`
- [IoWriteCapturedPristineTriageDumpToDedicatedDumpFile](../../text/59/IoWriteCapturedPristineTriageDumpToDedicatedDumpFile_function_005934C0.md) at `0x00593595`
- [IopIoRingUpdateCompletionUserEvent](../../text/59/IopIoRingUpdateCompletionUserEvent_function_0059886C.md) at `0x005988AA`
- [IopLiveDumpOpenVMMemoryPartition](../../text/59/IopLiveDumpOpenVMMemoryPartition_function_0059D508.md) at `0x0059D5BC`
- [PsSetCpuQuotaInformation](../../text/5E/PsSetCpuQuotaInformation_function_005E28F8.md) at `0x005E2A82`
- [LdrpMapResourceFile](../../text/5E/LdrpMapResourceFile_function_005E5CBC.md) at `0x005E5E4A`
- [SepOneWayLinkLogonSessions](../../text/60/SepOneWayLinkLogonSessions_function_006068D8.md) at `0x006069A9`
- [SeSetSecurityAttributesTokenEx](../../text/60/SeSetSecurityAttributesTokenEx_function_00609C00.md) at `0x00609C75`
- [DifObReferenceObjectByHandleWrapper](../../text/63/DifObReferenceObjectByHandleWrapper_function_00638040.md) at `0x0063815F`
- [ExRegisterBootDevice](../../text/65/ExRegisterBootDevice_function_00657B90.md) at `0x00657C4E`
- [CmSiProcessTupleStartFromHandle](../../text/66/CmSiProcessTupleStartFromHandle_function_0066DC44.md) at `0x0066DC9C`
- [NtDeletePrivateNamespace](../70/NtDeletePrivateNamespace_function_00700920.md) at `0x00700962`
- [NtSetInformationDebugObject](../71/NtSetInformationDebugObject_function_007107B0.md) at `0x0071089D`
- [DbgkCaptureLiveDump](../71/DbgkCaptureLiveDump_function_0071113C.md) at `0x0071132A`
- [IopInitializeCrashDump](../71/IopInitializeCrashDump_function_0071A270.md) at `0x0071A3E8`
- [IopConnectLinkTrackingPort](../71/IopConnectLinkTrackingPort_function_0071B050.md) at `0x0071B134`
- [IoAttachDevice](../71/IoAttachDevice_function_0071CE80.md) at `0x0071CF20`
- [IoCreateSynchronizationEvent](../71/IoCreateSynchronizationEvent_function_0071D2C0.md) at `0x0071D346`
- [NtSetInformationIoRing](../72/NtSetInformationIoRing_function_00720D80.md) at `0x00720E4B`
- [IopCreatePassiveInterruptRealtimeThreads](../72/IopCreatePassiveInterruptRealtimeThreads_function_0072BA98.md) at `0x0072BB5F`
- [PiUEventGetDmObjectFromUserHandle](../72/PiUEventGetDmObjectFromUserHandle_function_0072DF88.md) at `0x0072DFE0`
- [PiDrvDbQuerySystemPathWin32](../74/PiDrvDbQuerySystemPathWin32_function_007421F4.md) at `0x007422F5`
- [NtQueryInformationPort](../74/NtQueryInformationPort_function_0074BEB0.md) at `0x0074BF38`
- [NtReplyWaitReplyPort](../74/NtReplyWaitReplyPort_function_0074BFB0.md) at `0x0074C006`
- [NtAlpcImpersonateClientContainerOfPort](../74/NtAlpcImpersonateClientContainerOfPort_function_0074C1B0.md) at `0x0074C252`
- [NtAlpcRevokeSecurityContext](../74/NtAlpcRevokeSecurityContext_function_0074C400.md) at `0x0074C463`
- [AlpcpPortQueryServerInfo](../74/AlpcpPortQueryServerInfo_function_0074C784.md) at `0x0074C821`
- [ObpInitializeRootNamespace](../74/ObpInitializeRootNamespace_function_0074E588.md) at `0x0074E710`
- [NtSetInformationSymbolicLink](../74/NtSetInformationSymbolicLink_function_0074E910.md) at `0x0074E962`
- [PfTStart](../75/PfTStart_function_007517AC.md) at `0x0075194D`
- [PfpCreateEventInternal](../75/PfpCreateEventInternal_function_00753480.md) at `0x00753622`
- [TtmpAcquireSessionFromTerminalHandle](../77/TtmpAcquireSessionFromTerminalHandle_function_00778544.md) at `0x007785A1`
- [TtmpDispatchGetTerminalEvent](../77/TtmpDispatchGetTerminalEvent_function_007789F4.md) at `0x00778A35`
- [TtmiOpenDefaultTerminal](../77/TtmiOpenDefaultTerminal_function_0077CC20.md) at `0x0077CC5C`
- [PspLocateSystemDll](../77/PspLocateSystemDll_function_0077F0D0.md) at `0x0077F211`
- [PsCheckProcessFileSigningLevel](../78/PsCheckProcessFileSigningLevel_function_00783800.md) at `0x00783944`
- [PspAssignPrimaryToken](../78/PspAssignPrimaryToken_function_00784870.md) at `0x007848C4`
- [PspCreatePartitionSystemProcess](../78/PspCreatePartitionSystemProcess_function_007882F8.md) at `0x007883A1`
- [SepRmVerifyLsaProtectionLevel](../79/SepRmVerifyLsaProtectionLevel_function_0079C2E8.md) at `0x0079C387`
- [SmProcessProcessStoreInfoRequest](../7A/SmProcessProcessStoreInfoRequest_function_007A6B48.md) at `0x007A6C21`
- [SmKmStoreFileCreateForIoType](../7A/SmKmStoreFileCreateForIoType_function_007A93C8.md) at `0x007A9540`
- [SmKmStoreFileOpenVolume](../7A/SmKmStoreFileOpenVolume_function_007A9C14.md) at `0x007A9D41`
- [SmpUtilsGetControlDevice](../7A/SmpUtilsGetControlDevice_function_007ACBE0.md) at `0x007ACCB7`
- [VmMapSectionExecuteNoAcg](../7A/VmMapSectionExecuteNoAcg_function_007ACDC0.md) at `0x007ACE00`
- [VmCreateMemoryProcess](../7A/VmCreateMemoryProcess_function_007ACFA0.md) at `0x007AD111`
- [VmTerminateMemoryProcess](../7A/VmTerminateMemoryProcess_function_007AD6D0.md) at `0x007AD6F8`
- [VmpLogCreateMemoryProcess](../7A/VmpLogCreateMemoryProcess_function_007AE668.md) at `0x007AE6E4`
- [WmipTranslateFileHandle](../7B/WmipTranslateFileHandle_function_007B3DA4.md) at `0x007B3E0C`
- [EtwpTrackProviderBinary](../7B/EtwpTrackProviderBinary_function_007B9198.md) at `0x007B91CF`
- [EtwpQuerySessionDemuxObject](../7B/EtwpQuerySessionDemuxObject_function_007BC8B0.md) at `0x007BC8E1`
- [EtwpCovSampCaptureContextStart](../7C/EtwpCovSampCaptureContextStart_function_007C14AC.md) at `0x007C171A`
- [EtwpCoverageSamplerSetBloomFilter](../7C/EtwpCoverageSamplerSetBloomFilter_function_007C2070.md) at `0x007C20F2`
- [EtwpSetCoverageSamplerInformation](../7C/EtwpSetCoverageSamplerInformation_function_007C288C.md) at `0x007C299B`
- [EtwpSetCoverageSamplerInformation](../7C/EtwpSetCoverageSamplerInformation_function_007C288C.md) at `0x007C2F07`
- [ExpQueryElamCertInfo](../7C/ExpQueryElamCertInfo_function_007C4564.md) at `0x007C460D`
- [ExInitializeLeapSecondData](../7C/ExInitializeLeapSecondData_function_007C562C.md) at `0x007C56A7`
- [SLUpdateLicenseDataInternal](../7C/SLUpdateLicenseDataInternal_function_007C9C04.md) at `0x007CA152`
- [NtSetDefaultHardErrorPort](../7D/NtSetDefaultHardErrorPort_function_007D0340.md) at `0x007D03C0`
- [NtStartProfile](../7D/NtStartProfile_function_007D22C0.md) at `0x007D230C`
- [NtStopProfile](../7D/NtStopProfile_function_007D25C0.md) at `0x007D25FF`
- [NtAcquireCrossVmMutant](../7D/NtAcquireCrossVmMutant_function_007D26C0.md) at `0x007D275B`
- [CMFSystemThreadRoutine](../7D/CMFSystemThreadRoutine_function_007D3A70.md) at `0x007D3E69`
- [CmpCreatePredefined](../7D/CmpCreatePredefined_function_007DA0CC.md) at `0x007DA1CD`
- [CmpMarkCurrentProfileDirty](../7D/CmpMarkCurrentProfileDirty_function_007DBBAC.md) at `0x007DBC58`
- [NtRollbackRegistryTransaction](../7E/NtRollbackRegistryTransaction_function_007E0F30.md) at `0x007E0FD1`
- [CmpCloneHwProfile](../7E/CmpCloneHwProfile_function_007E303C.md) at `0x007E365A`
- [CmpCloneHwProfile](../7E/CmpCloneHwProfile_function_007E303C.md) at `0x007E368F`
- [CmpVolumeContextStart](../7E/CmpVolumeContextStart_function_007E88A4.md) at `0x007E89E0`
- [CmpHiveCacheSubscribePnpNotifications](../7E/CmpHiveCacheSubscribePnpNotifications_function_007E8D2C.md) at `0x007E8D69`
- [CmpDoReOpenTransKey](../7F/CmpDoReOpenTransKey_function_007F78E8.md) at `0x007F7A84`
- [CmpDoReOpenTransKey](../7F/CmpDoReOpenTransKey_function_007F78E8.md) at `0x007F7BD7`
- [VhdiMountVhdFile](../83/VhdiMountVhdFile_function_0083BED0.md) at `0x0083C2C0`
- [ObCreateSiloRootDirectory](../83/ObCreateSiloRootDirectory_function_0083CA34.md) at `0x0083CBF1`
- [CmpTransInitializeTransaction](../84/CmpTransInitializeTransaction_function_008422C8.md) at `0x008423AB`
- [NtSetInformationKey](../84/NtSetInformationKey_function_00843720.md) at `0x008438ED`
- [NtSetInformationKey](../84/NtSetInformationKey_function_00843720.md) at `0x00843C3F`
- [NtSetInformationKey](../84/NtSetInformationKey_function_00843720.md) at `0x00843E15`
- [NtSetInformationKey](../84/NtSetInformationKey_function_00843720.md) at `0x00843E8A`
- [NtQueryKey](NtQueryKey_function_008676E0.md) at `0x00867934`
- [NtQueryKey](NtQueryKey_function_008676E0.md) at `0x00867FB3`
- [NtAlpcSendWaitReceivePort](NtAlpcSendWaitReceivePort_function_00868040.md) at `0x008680C7`
- [ObpCreateHandle](ObpCreateHandle_function_0086B950.md) at `0x0086D296`
- [NtQuerySecurityObject](../87/NtQuerySecurityObject_function_008737B0.md) at `0x008738B4`
- [NtOpenKeyTransactedEx](../87/NtOpenKeyTransactedEx_function_00874EC0.md) at `0x00874F42`
- [NtOpenKeyTransactedEx](../87/NtOpenKeyTransactedEx_function_00874EC0.md) at `0x00874F93`
- [CmCreateKey](../87/CmCreateKey_function_00875020.md) at `0x00875536`
- [CmLoadDifferencingKey](../87/CmLoadDifferencingKey_function_00875670.md) at `0x00875FB9`
- [CmLoadDifferencingKey](../87/CmLoadDifferencingKey_function_00875670.md) at `0x008762AE`
- [CmOpenKey](../87/CmOpenKey_function_00876350.md) at `0x008766CE`
- [CmConvertHandleToKernelHandle](../87/CmConvertHandleToKernelHandle_function_00876DDC.md) at `0x00876E38`
- [CmLoadAppKey](../87/CmLoadAppKey_function_00876FFC.md) at `0x0087721C`
- [CmpIsThisSameFile](../87/CmpIsThisSameFile_function_00877CE8.md) at `0x00877D1E`
- [CmpLinkHiveToMaster](../87/CmpLinkHiveToMaster_function_00877D6C.md) at `0x00877F3A`
- [CmLoadKey](../87/CmLoadKey_function_008787CC.md) at `0x00878F08`
- [CmpGetVolumeClusterSize](../87/CmpGetVolumeClusterSize_function_0087B3D4.md) at `0x0087B452`
- [CmpCreateEvent](../87/CmpCreateEvent_function_0087B638.md) at `0x0087B6C5`
- [CmpInitCmRM](../87/CmpInitCmRM_function_0087C700.md) at `0x0087CF2F`
- [CmpInitCmRM](../87/CmpInitCmRM_function_0087C700.md) at `0x0087D029`
- [NtAlpcDeletePortSection](../88/NtAlpcDeletePortSection_function_00888420.md) at `0x0088847A`
- [NtAlpcCreateSectionView](../88/NtAlpcCreateSectionView_function_00888640.md) at `0x0088874D`
- [NtAlpcDeleteResourceReserve](../88/NtAlpcDeleteResourceReserve_function_00888870.md) at `0x008888D3`
- [NtAlpcDeleteSecurityContext](../88/NtAlpcDeleteSecurityContext_function_00889E00.md) at `0x00889E5A`
- [NtAlpcCreateSecurityContext](../89/NtAlpcCreateSecurityContext_function_00890B50.md) at `0x00890C58`
- [NtAlpcCreateResourceReserve](../89/NtAlpcCreateResourceReserve_function_00892BE0.md) at `0x00892C55`
- [AlpcpCreateSection](../89/AlpcpCreateSection_function_0089307C.md) at `0x008932D9`
- [NtAlpcCreatePortSection](../89/NtAlpcCreatePortSection_function_00893E60.md) at `0x00893F3C`
- [NtAlpcQueryInformationMessage](../89/NtAlpcQueryInformationMessage_function_00894700.md) at `0x008948A7`
- [NtAlpcOpenSenderProcess](../89/NtAlpcOpenSenderProcess_function_008953B0.md) at `0x00895465`
- [NtReplyWaitReceivePortEx](../89/NtReplyWaitReceivePortEx_function_00895850.md) at `0x00895902`
- [NtAlpcImpersonateClientOfPort](../89/NtAlpcImpersonateClientOfPort_function_008961A0.md) at `0x0089630C`
- [NtQueryObject](../8A/NtQueryObject_function_008A6DB0.md) at `0x008A6F57`
- [PfSnGetSectionObject](../8A/PfSnGetSectionObject_function_008A9448.md) at `0x008A96FC`
- [NtResetEvent](../8A/NtResetEvent_function_008AA2D0.md) at `0x008AA329`
- [IopOpenLinkOrRenameTarget](../8A/IopOpenLinkOrRenameTarget_function_008AAC04.md) at `0x008AAE41`
- [IopReadFile](../8A/IopReadFile_function_008AEFF0.md) at `0x008AF302`
- [NtEnumerateValueKey](../8B/NtEnumerateValueKey_function_008B3B50.md) at `0x008B4574`
- [NtDuplicateToken](../8B/NtDuplicateToken_function_008B6DF0.md) at `0x008B6EDB`
- [NtOpenThreadTokenEx](../8B/NtOpenThreadTokenEx_function_008B7840.md) at `0x008B7955`
- [NtSetInformationThread](../8C/NtSetInformationThread_function_008C9F60.md) at `0x008CA49E`
- [PsAssignImpersonationToken](../8C/PsAssignImpersonationToken_function_008CBCB0.md) at `0x008CBD26`
- [NtImpersonateThread](../8C/NtImpersonateThread_function_008CD230.md) at `0x008CD2E8`
- [NtImpersonateThread](../8C/NtImpersonateThread_function_008CD230.md) at `0x008CD31D`
- [NtAlpcQueryInformation](../8E/NtAlpcQueryInformation_function_008E7200.md) at `0x008E7320`
- [NtRemoveIoCompletionEx](../8E/NtRemoveIoCompletionEx_function_008E8760.md) at `0x008E8848`
- [NtQueryEvent](../8E/NtQueryEvent_function_008E8F90.md) at `0x008E907D`
- [NtQueryEvent](../8E/NtQueryEvent_function_008E8F90.md) at `0x008E9147`
- [IopXxxControlFile](../8E/IopXxxControlFile_function_008E9AD0.md) at `0x008E9D87`
- [BuildQueryDirectoryIrp](../8E/BuildQueryDirectoryIrp_function_008EC770.md) at `0x008ECD11`
- [SepValidateReferencedCachedHandles](../8F/SepValidateReferencedCachedHandles_function_008F4BB0.md) at `0x008F4C7A`
- [NtCompareTokens](../8F/NtCompareTokens_function_008F8F20.md) at `0x008F8F9F`
- [NtCompareTokens](../8F/NtCompareTokens_function_008F8F20.md) at `0x008F8FDB`
- [NtTerminateJobObject](../91/NtTerminateJobObject_function_009172B0.md) at `0x009172EC`
- [sub_0091EFFE](../91/Unknown_function_0091EFFE.md) at `0x0091F069`
- [AlpcpMapLegacyPortView](../92/AlpcpMapLegacyPortView_function_00921588.md) at `0x009215FC`
- [NtRequestWaitReplyPort](../92/NtRequestWaitReplyPort_function_00921E40.md) at `0x00921E9D`
- [sub_0093345B](../93/Unknown_function_0093345B.md) at `0x009336D5`
- [PfpPrefetchRequest](../93/PfpPrefetchRequest_function_009385CC.md) at `0x009386CC`
- [PspInsertProcess](../94/PspInsertProcess_function_009472CC.md) at `0x009475BF`
- [NtCopyFileChunk](../94/NtCopyFileChunk_function_0094B600.md) at `0x0094BB50`
- [NtCopyFileChunk](../94/NtCopyFileChunk_function_0094B600.md) at `0x0094BBB4`
- [CmpVolumeManagerGetContextForFile](../95/CmpVolumeManagerGetContextForFile_function_009525A8.md) at `0x00952602`
- [IoGetDeviceObjectPointer](../95/IoGetDeviceObjectPointer_function_00953220.md) at `0x009532DE`
- [KsepSdbMapToMemory](../95/KsepSdbMapToMemory_function_0095B81C.md) at `0x0095B92C`
- [EtwpQueryCoverageSamplerInformation](../95/EtwpQueryCoverageSamplerInformation_function_0095D2D8.md) at `0x0095D388`
- [PiCMOpenObjectKey](../96/PiCMOpenObjectKey_function_00961E08.md) at `0x00961F28`
- [PiCMDuplicateRegistryHandle](../96/PiCMDuplicateRegistryHandle_function_009624C4.md) at `0x009624F8`
- [NtPrivilegeObjectAuditAlarm](../97/NtPrivilegeObjectAuditAlarm_function_00974170.md) at `0x0097420C`
- [NtPrivilegedServiceAuditAlarm](../97/NtPrivilegedServiceAuditAlarm_function_00974430.md) at `0x009744C4`
- [NtOpenObjectAuditAlarm](../97/NtOpenObjectAuditAlarm_function_00974700.md) at `0x009747EF`
- [IopLoadDriver](../99/IopLoadDriver_function_00997B54.md) at `0x00997E2F`
- [IopLoadDriver](../99/IopLoadDriver_function_00997B54.md) at `0x00998176`
- [IopReferenceDriverObjectByName](../99/IopReferenceDriverObjectByName_function_0099C178.md) at `0x0099C21C`
- [NtSetEventEx](../99/NtSetEventEx_function_0099C570.md) at `0x0099C5F7`
- [NtSetEventEx](../99/NtSetEventEx_function_0099C570.md) at `0x0099C6BC`
- [NtRemoveIoCompletion](../99/NtRemoveIoCompletion_function_0099C8B0.md) at `0x0099C9A0`
- [NtQueryDirectoryObject](../99/NtQueryDirectoryObject_function_0099EA20.md) at `0x0099EB3E`
- [NtReleaseMutant](../9A/NtReleaseMutant_function_009A2780.md) at `0x009A27DD`
- [NtReleaseMutant](../9A/NtReleaseMutant_function_009A2780.md) at `0x009A28A7`
- [NtSetIoCompletionEx](../9A/NtSetIoCompletionEx_function_009A7C90.md) at `0x009A7CDF`
- [sub_009A7D0D](../9A/Unknown_function_009A7D0D.md) at `0x009A7D29`
- [NtCreateWorkerFactory](../9A/NtCreateWorkerFactory_function_009A7E10.md) at `0x009A7ED3`
- [NtClearEvent](../9A/NtClearEvent_function_009A91A0.md) at `0x009A91EB`
- [NtClearEvent](../9A/NtClearEvent_function_009A91A0.md) at `0x009A9259`
- [NtQueryInformationProcess](../9A/NtQueryInformationProcess_function_009AA250.md) at `0x009AC344`
- [NtQueryInformationProcess](../9A/NtQueryInformationProcess_function_009AA250.md) at `0x009AC86C`
- [NtCommitRegistryTransaction](../9A/NtCommitRegistryTransaction_function_009AEAF0.md) at `0x009AEB89`
- [CmUnloadKey](../9A/CmUnloadKey_function_009AF2FC.md) at `0x009AF8B8`
- [CmpFileFlushAndPurge](../9B/CmpFileFlushAndPurge_function_009B2BAC.md) at `0x009B2C37`
- [CmpQueryNameString](../9B/CmpQueryNameString_function_009BA2AC.md) at `0x009BA2E8`
- [NtReleaseSemaphore](../9C/NtReleaseSemaphore_function_009C4BC0.md) at `0x009C4C26`
- [NtAlpcOpenSenderThread](../9C/NtAlpcOpenSenderThread_function_009C5920.md) at `0x009C59BB`
- [NtAdjustGroupsToken](../9C/NtAdjustGroupsToken_function_009C6640.md) at `0x009C679D`
- [NtFilterToken](../9C/NtFilterToken_function_009C7890.md) at `0x009C7AE2`
- [NtAdjustPrivilegesToken](../9C/NtAdjustPrivilegesToken_function_009C86C0.md) at `0x009C8838`
- [NtPrivilegeCheck](../9C/NtPrivilegeCheck_function_009C8AE0.md) at `0x009C8B4E`
- [NtLockFile](../9D/NtLockFile_function_009D86D0.md) at `0x009D8B4D`
- [NtSetIoCompletion](../9D/NtSetIoCompletion_function_009DB700.md) at `0x009DB74A`
- [NtNotifyChangeMultipleKeys](../9D/NtNotifyChangeMultipleKeys_function_009DC6B0.md) at `0x009DCA97`
- [WmipQueryGuidInfo](../9D/WmipQueryGuidInfo_function_009DE66C.md) at `0x009DE6A8`
- [WmipQuerySetExecuteSI](../9E/WmipQuerySetExecuteSI_function_009E0574.md) at `0x009E0612`
- [WmipQueryAllData](../9E/WmipQueryAllData_function_009E086C.md) at `0x009E0921`
- [NtUnlockFile](../9E/NtUnlockFile_function_009E5DA0.md) at `0x009E5E1B`
- [NtQuerySymbolicLinkObject](../9E/NtQuerySymbolicLinkObject_function_009EBA20.md) at `0x009EBB48`
- [ExpCreateWorkerThread](../9E/ExpCreateWorkerThread_function_009ECEFC.md) at `0x009ECF9C`
- [EtwpSetProviderTraitsUm](../9F/EtwpSetProviderTraitsUm_function_009F3514.md) at `0x009F3573`
- [NtPulseEvent](../9F/NtPulseEvent_function_009F4460.md) at `0x009F44B9`
- [NtReplyPort](../9F/NtReplyPort_function_009F5BE0.md) at `0x009F5C4C`
- [NtQueueApcThreadEx2](../9F/NtQueueApcThreadEx2_function_009FE980.md) at `0x009FE9FC`
- [NtQueueApcThreadEx2](../9F/NtQueueApcThreadEx2_function_009FE980.md) at `0x009FEB39`
- [EtwpSendReplyDataBlock](../9F/EtwpSendReplyDataBlock_function_009FEC64.md) at `0x009FECB0`
- [sub_00A0B648](../A0/Unknown_function_00A0B648.md) at `0x00A0B7D1`
- [sub_00A0BA74](../A0/Unknown_function_00A0BA74.md) at `0x00A0BC76`
- [sub_00A0C12C](../A0/Unknown_function_00A0C12C.md) at `0x00A0C277`
- [NtRemoveProcessDebug](../A0/NtRemoveProcessDebug_function_00A0FAF0.md) at `0x00A0FBFB`
- [NtDebugActiveProcess](../A0/NtDebugActiveProcess_function_00A0FC60.md) at `0x00A0FD61`
- [NtDebugContinue](../A1/NtDebugContinue_function_00A10280.md) at `0x00A10310`
- [AlpcpCaptureDirectAttribute](../A1/AlpcpCaptureDirectAttribute_function_00A126AC.md) at `0x00A12710`
- [PspCreateProcess](../A1/PspCreateProcess_function_00A12758.md) at `0x00A12997`
- [PspReferenceTokenForNewProcess](../A1/PspReferenceTokenForNewProcess_function_00A12D58.md) at `0x00A12D93`
- [NtGetNlsSectionPtr](../A1/NtGetNlsSectionPtr_function_00A195B0.md) at `0x00A1975F`
- [NtAlpcSetInformation](../A1/NtAlpcSetInformation_function_00A19DC0.md) at `0x00A19EC8`
- [AlpcpAssociateIoCompletionPort](../A1/AlpcpAssociateIoCompletionPort_function_00A1A28C.md) at `0x00A1A33A`
- [SepAccessCheckAndAuditAlarm](../A1/SepAccessCheckAndAuditAlarm_function_00A1AF4C.md) at `0x00A1B4F8`
- [NtNotifyChangeDirectoryFileEx](../A1/NtNotifyChangeDirectoryFileEx_function_00A1DEA0.md) at `0x00A1E1BC`
- [NtAssignProcessToJobObject](../A2/NtAssignProcessToJobObject_function_00A22FC0.md) at `0x00A23005`
- [NtIsProcessInJob](../A2/NtIsProcessInJob_function_00A23940.md) at `0x00A239E1`
- [AlpcpCaptureDirectAttribute32](../A2/AlpcpCaptureDirectAttribute32_function_00A27044.md) at `0x00A27095`
- [NtAlpcDeleteSectionView](../A2/NtAlpcDeleteSectionView_function_00A2F240.md) at `0x00A2F2A5`
- [NtGetContextThread](../A3/NtGetContextThread_function_00A30BE0.md) at `0x00A30C28`
- [AlpcpAcceptConnectPort](../A3/AlpcpAcceptConnectPort_function_00A34290.md) at `0x00A345E5`
- [IopTrackLink](../A3/IopTrackLink_function_00A36764.md) at `0x00A368A7`
- [NtCompareObjects](../A3/NtCompareObjects_function_00A374C0.md) at `0x00A374F8`
- [NtCompareObjects](../A3/NtCompareObjects_function_00A374C0.md) at `0x00A37522`
- [PiUEventGetDeviceInstanceIdFromUserHandle](../A3/PiUEventGetDeviceInstanceIdFromUserHandle_function_00A38954.md) at `0x00A3899E`
- [NtImpersonateAnonymousToken](../A3/NtImpersonateAnonymousToken_function_00A3A150.md) at `0x00A3A1C0`
- [NtAlpcCancelMessage](../A3/NtAlpcCancelMessage_function_00A3A860.md) at `0x00A3A8E8`
- [NtGetCachedSigningLevel](../A4/NtGetCachedSigningLevel_function_00A42820.md) at `0x00A428F3`
- [NtQueryMutant](../A4/NtQueryMutant_function_00A458D0.md) at `0x00A45981`
- [NtWaitForDebugEvent](../A4/NtWaitForDebugEvent_function_00A464E0.md) at `0x00A465DF`
- [NtSetWnfProcessNotificationEvent](../A4/NtSetWnfProcessNotificationEvent_function_00A48A80.md) at `0x00A48AEC`
- [NtLockProductActivationKeys](../A4/NtLockProductActivationKeys_function_00A492E0.md) at `0x00A49663`
- [NtAlpcDisconnectPort](../A4/NtAlpcDisconnectPort_function_00A4F260.md) at `0x00A4F2B5`
- [ObpCreateDirectoryObject](../A5/ObpCreateDirectoryObject_function_00A56230.md) at `0x00A562C5`
- [ExpQuerySystemInformation](../A5/ExpQuerySystemInformation_function_00A57858.md) at `0x00A5A7EB`
- [ExpQuerySystemInformation](../A5/ExpQuerySystemInformation_function_00A57858.md) at `0x00A5A901`
- [EtwpAddNotificationEvent](../A5/EtwpAddNotificationEvent_function_00A5FC44.md) at `0x00A5FC78`
- [NtQueryTimer](../A6/NtQueryTimer_function_00A62390.md) at `0x00A6244B`
- [EtwpRealtimeConnect](../A6/EtwpRealtimeConnect_function_00A65C88.md) at `0x00A65E8A`
- [EtwpRealtimeConnect](../A6/EtwpRealtimeConnect_function_00A65C88.md) at `0x00A65EC7`
- [SepRmLsaConnectRequest](../A6/SepRmLsaConnectRequest_function_00A6AB54.md) at `0x00A6ABF5`
- [SeGetLogonSessionToken](../A6/SeGetLogonSessionToken_function_00A6E4B0.md) at `0x00A6E4FF`
- [AlpcCreateSecurityContext](../A7/AlpcCreateSecurityContext_function_00A70930.md) at `0x00A70989`
- [NtReleaseKeyedEvent](../A7/NtReleaseKeyedEvent_function_00A70AF0.md) at `0x00A70B81`
- [NtQuerySemaphore](../A7/NtQuerySemaphore_function_00A71370.md) at `0x00A7142E`
- [NtWaitForKeyedEvent](../A7/NtWaitForKeyedEvent_function_00A71D50.md) at `0x00A71E9A`
- [SmProcessStoreMemoryPriorityRequest](../A7/SmProcessStoreMemoryPriorityRequest_function_00A7830C.md) at `0x00A78401`
- [ExCreateCallback](../A7/ExCreateCallback_function_00A7B9D0.md) at `0x00A7BA98`
- [NtRegisterThreadTerminatePort](../A7/NtRegisterThreadTerminatePort_function_00A7CCF0.md) at `0x00A7CD26`
- [NtNotifyChangeSession](../A7/NtNotifyChangeSession_function_00A7E630.md) at `0x00A7E6E3`
- [NtMakeTemporaryObject](../A7/NtMakeTemporaryObject_function_00A7F7D0.md) at `0x00A7F811`
- [IoCreateNotificationEvent](../A8/IoCreateNotificationEvent_function_00A80470.md) at `0x00A804F4`
- [ExpQueryCodeIntegrityCertificateInfo](../A8/ExpQueryCodeIntegrityCertificateInfo_function_00A8552C.md) at `0x00A855DB`
- [IoConvertFileHandleToKernelHandle](../A8/IoConvertFileHandleToKernelHandle_function_00A85680.md) at `0x00A856DB`
- [IoConvertFileHandleToKernelHandle](../A8/IoConvertFileHandleToKernelHandle_function_00A85680.md) at `0x00A85764`
- [EtwpReceiveReplyDataBlock](../A8/EtwpReceiveReplyDataBlock_function_00A87954.md) at `0x00A879AB`
- [NtSetContextThread](../A8/NtSetContextThread_function_00A88440.md) at `0x00A88488`
- [NtQueryIoCompletion](../A8/NtQueryIoCompletion_function_00A885C0.md) at `0x00A88674`
- [ObpSetDeviceMap](../A9/ObpSetDeviceMap_function_00A925D0.md) at `0x00A9261B`
- [NtMakePermanentObject](../A9/NtMakePermanentObject_function_00A979F0.md) at `0x00A97A49`
- [NtRequestPort](../A9/NtRequestPort_function_00A98DA0.md) at `0x00A98DFB`
- [NtGetDevicePowerState](../A9/NtGetDevicePowerState_function_00A9B750.md) at `0x00A9B7CB`
- [EtwpRealtimeDisconnectConsumerByHandle](../A9/EtwpRealtimeDisconnectConsumerByHandle_function_00A9E368.md) at `0x00A9E39E`
- [IopReadFileScatter](../AA/IopReadFileScatter_function_00AA5D78.md) at `0x00AA616E`
- [IopWriteFileGather](../AA/IopWriteFileGather_function_00AAA95C.md) at `0x00AAAD47`
- [WmipGetFilePDO](../AA/WmipGetFilePDO_function_00AAF454.md) at `0x00AAF488`
- [NtCreateKeyTransacted](../AA/NtCreateKeyTransacted_function_00AAF830.md) at `0x00AAF8CE`
- [NtCreateKeyTransacted](../AA/NtCreateKeyTransacted_function_00AAF830.md) at `0x00AAF914`
- [NtSetEventBoostPriority](../AA/NtSetEventBoostPriority_function_00AAFEA0.md) at `0x00AAFEDA`
- [NtCancelSynchronousIoFile](../AB/NtCancelSynchronousIoFile_function_00AB5CE0.md) at `0x00AB5D4A`
- [NtCreateLowBoxToken](../AB/NtCreateLowBoxToken_function_00AB9880.md) at `0x00AB9CC1`
- [IopUnloadDriver](../AB/IopUnloadDriver_function_00ABF868.md) at `0x00ABFAD6`
- [PopBootStatAccessCheck](../AC/PopBootStatAccessCheck_function_00AC0814.md) at `0x00AC0863`
- [EtwpUseDescriptorTypeUm](../AC/EtwpUseDescriptorTypeUm_function_00AC3338.md) at `0x00AC336B`
- [SmKmFileInfoDuplicate](../AC/SmKmFileInfoDuplicate_function_00AC98FC.md) at `0x00AC99B5`
- [IoCreateDriver](../AC/IoCreateDriver_function_00AC9D70.md) at `0x00AC9FE3`
- [SmCreateEvent](../AC/SmCreateEvent_function_00ACCAE4.md) at `0x00ACCB70`
- [CmFcpManagerCreateSection](../AD/CmFcpManagerCreateSection_function_00ADA3BC.md) at `0x00ADA466`
- [NtSetSecurityObject](../AD/NtSetSecurityObject_function_00ADE2B0.md) at `0x00ADE3A4`
- [NtSetInformationProcess](../AE/NtSetInformationProcess_function_00AE5370.md) at `0x00AE5F53`
- [NtSetInformationProcess](../AE/NtSetInformationProcess_function_00AE5370.md) at `0x00AE9096`
- [NtSetInformationProcess](../AE/NtSetInformationProcess_function_00AE5370.md) at `0x00AE99F7`
- [NtSetInformationProcess](../AE/NtSetInformationProcess_function_00AE5370.md) at `0x00AE9BCB`
- [NtSetInformationProcess](../AE/NtSetInformationProcess_function_00AE5370.md) at `0x00AE9E7C`
- [NtCreateUserProcess](../AE/NtCreateUserProcess_function_00AEA680.md) at `0x00AEAD69`
- [NtCreateUserProcess](../AE/NtCreateUserProcess_function_00AEA680.md) at `0x00AEAF46`
- [NtQueryInformationToken](../AE/NtQueryInformationToken_function_00AECDD0.md) at `0x00AEE648`
- [NtSetInformationToken](../AF/NtSetInformationToken_function_00AF0530.md) at `0x00AF0678`
- [NtSetSystemInformation](../AF/NtSetSystemInformation_function_00AF4A60.md) at `0x00AF522E`
- [NtSetSystemInformation](../AF/NtSetSystemInformation_function_00AF4A60.md) at `0x00AF62E9`
- [sub_00B17976](../B1/Unknown_function_00B17976.md) at `0x00B1799C`
- [sub_00B179DA](../B1/Unknown_function_00B179DA.md) at `0x00B17A44`
- [sub_00B17DB0](../B1/Unknown_function_00B17DB0.md) at `0x00B17DDB`
- [sub_00B19ABC](../B1/Unknown_function_00B19ABC.md) at `0x00B19AF7`
- [sub_00B19F84](../B1/Unknown_function_00B19F84.md) at `0x00B19FC0`
- [sub_00B1A6E0](../B1/Unknown_function_00B1A6E0.md) at `0x00B1A71E`
- [sub_00B1A740](../B1/Unknown_function_00B1A740.md) at `0x00B1A77E`
- [sub_00B2A59A](../B2/Unknown_function_00B2A59A.md) at `0x00B2A619`
- [sub_00B3130A](../B3/Unknown_function_00B3130A.md) at `0x00B31346`
- [sub_00B334D2](../B3/Unknown_function_00B334D2.md) at `0x00B33524`
- [sub_00B334D2](../B3/Unknown_function_00B334D2.md) at `0x00B335F1`
- [sub_00B39570](../B3/Unknown_function_00B39570.md) at `0x00B396A9`
- [sub_00B4588A](../B4/Unknown_function_00B4588A.md) at `0x00B45E15`
- [VfPendingInitPhase1](../../pagevrfy/BA/VfPendingInitPhase1_function_00BA1AA4.md) at `0x00BA1B71`
- [VfPoolInitPhase1](../../pagevrfy/BA/VfPoolInitPhase1_function_00BAA3E0.md) at `0x00BAA4AD`
- [VfCheckUserHandle](../../pagevrfy/BB/VfCheckUserHandle_function_00BB9218.md) at `0x00BB9307`
- [CmObReferenceObjectByHandle](../../pagecmrc/BC/CmObReferenceObjectByHandle_function_00BC9350.md) at `0x00BC9391`
- [sub_00C18CD4](../../init/C1/Unknown_function_00C18CD4.md) at `0x00C19071`
- [FsRtlInitializeSmssEvent](../../init/C2/FsRtlInitializeSmssEvent_function_00C29030.md) at `0x00C290C5`
- [IoInitSystemPreDrivers](../../init/C2/IoInitSystemPreDrivers_function_00C2AC3C.md) at `0x00C2B3B7`
- [IoInitSystemPreDrivers](../../init/C2/IoInitSystemPreDrivers_function_00C2AC3C.md) at `0x00C2BE31`
- [IopMarkBootPartition](../../init/C2/IopMarkBootPartition_function_00C2CFA0.md) at `0x00C2D0CB`
- [PspCreateSecureSystemProcess](../../init/C4/PspCreateSecureSystemProcess_function_00C452E4.md) at `0x00C4536B`
- [ExpWatchProductTypeInitialization](../../init/C5/ExpWatchProductTypeInitialization_function_00C52170.md) at `0x00C5227A`
- [ExpWatchProductTypeInitialization](../../init/C5/ExpWatchProductTypeInitialization_function_00C52170.md) at `0x00C5246D`
- [ExpKeyedEventInitialization](../../init/C5/ExpKeyedEventInitialization_function_00C5460C.md) at `0x00C54915`
- [CmpCreateRegistryRoot](../../init/C5/CmpCreateRegistryRoot_function_00C57880.md) at `0x00C57A32`
- [ObInitSystem](../../init/C7/ObInitSystem_function_00C71C7C.md) at `0x00C72208`
- [IopInitializeBuiltinDriver](../../init/C7/IopInitializeBuiltinDriver_function_00C7625C.md) at `0x00C763B2`
- [PspInitPhase0](../../init/C7/PspInitPhase0_function_00C77E2C.md) at `0x00C7890F`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00868DB0  48 83 EC 48                     sub rsp, 0x48
00868DB4  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
00868DB9  48 C7 44 24 38 00 00 00 00      mov qword ptr [rsp + 0x38], 0
00868DC2  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00868DC7  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
00868DCC  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00868DD1  C7 44 24 20 44 66 6C 74         mov dword ptr [rsp + 0x20], 0x746c6644
00868DD9  E8 72 08 00 00                  call 0x140869650
00868DDE  48 83 C4 48                     add rsp, 0x48
00868DE2  C3                              ret
00868DE3  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ObReferenceObjectByHandle(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned int v_stack_m28;

    v_rsp = (v_rsp) - (72);
    v_stack_m10 = 0;
    v_stack_m18 = a6;
    v_stack_m20 = a5;
    v_stack_m28 = 0x746C6644ULL;
    result = ObpReferenceObjectByHandleWithTag(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (72);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ObReferenceObjectByHandle(void *Handle, int64_t DesiredAccess, void *ObjectType, int64_t AccessMode, void *Object, void *HandleInformation)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint64_t v_stack_m18;
    uint64_t v_stack_m20;
    uint32_t v_stack_m28;

    local_rsp = (local_rsp) - (72);
    v_stack_m10 = 0;
    v_stack_m18 = HandleInformation;
    v_stack_m20 = Object;
    v_stack_m28 = 0x746C6644ULL;
    result = ObpReferenceObjectByHandleWithTag(Handle, DesiredAccess, ObjectType, AccessMode);
    local_rsp = (local_rsp) + (72);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00868DB0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00868DB0[BB_00868DB0]
  bb_00868DE3[BB_00868DE3]
```
