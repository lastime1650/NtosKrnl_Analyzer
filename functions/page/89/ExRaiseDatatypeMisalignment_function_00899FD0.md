# ExRaiseDatatypeMisalignment

- RVA: `0x00899FD0`–`0x00899FDF` (길이 `15` bytes)
- VA: `0x0000000140899FD0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007E574`
- 디코드: `4`개 명령, `15/15` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **294**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00899FD9` → [RtlRaiseStatus](../../text/2F/RtlRaiseStatus_function_002F6A50.md) (function, `0x002F6A50`)

### Direct callers
- [PoCaptureReasonContext](../../text/23/PoCaptureReasonContext_function_00230A38.md) at `0x00230A87`
- [NtSetTimerEx](../../text/23/NtSetTimerEx_function_00231480.md) at `0x002314FE`
- [NtSetInformationFile](../../text/29/NtSetInformationFile_function_0029C5E0.md) at `0x0029C730`
- [NtSetInformationFile](../../text/29/NtSetInformationFile_function_0029C5E0.md) at `0x0029C735`
- [NtShutdownWorkerFactory](../../text/2A/NtShutdownWorkerFactory_function_002A4E60.md) at `0x002A4EB8`
- [sub_002F31A4](../../text/2F/Unknown_function_002F31A4.md) at `0x002F328E`
- [RtlpLookupDynamicUserFunctionTable](../../text/2F/RtlpLookupDynamicUserFunctionTable_function_002F333C.md) at `0x002F35A5`
- [RtlpLookupUserFunctionTableInverted](../../text/2F/RtlpLookupUserFunctionTableInverted_function_002F3B20.md) at `0x002F3C36`
- [RtlpLookupUserFunctionTableInverted](../../text/2F/RtlpLookupUserFunctionTableInverted_function_002F3B20.md) at `0x002F3C68`
- [RtlpLookupUserFunctionTable](../../text/2F/RtlpLookupUserFunctionTable_function_002F3CD0.md) at `0x002F3DBD`
- [RtlpWalkFrameChain](../../text/2F/RtlpWalkFrameChain_function_002F3ED0.md) at `0x002F49E6`
- [RtlpLookupFunctionEntryForStackWalks](../../text/2F/RtlpLookupFunctionEntryForStackWalks_function_002F4ED0.md) at `0x002F5032`
- [RtlpxVirtualUnwind](../../text/2F/RtlpxVirtualUnwind_function_002F5110.md) at `0x002F517D`
- [RtlpxVirtualUnwind](../../text/2F/RtlpxVirtualUnwind_function_002F5110.md) at `0x002F55BB`
- [RtlpxVirtualUnwind](../../text/2F/RtlpxVirtualUnwind_function_002F5110.md) at `0x002F5645`
- [RtlpxVirtualUnwind](../../text/2F/RtlpxVirtualUnwind_function_002F5110.md) at `0x002F584E`
- [RtlpxVirtualUnwind](../../text/2F/RtlpxVirtualUnwind_function_002F5110.md) at `0x002F59F6`
- [RtlpUnwindPrologue](../../text/2F/RtlpUnwindPrologue_function_002F5FA0.md) at `0x002F6056`
- [RtlpUnwindPrologue](../../text/2F/RtlpUnwindPrologue_function_002F5FA0.md) at `0x002F6100`
- [RtlpUnwindPrologue](../../text/2F/RtlpUnwindPrologue_function_002F5FA0.md) at `0x002F61E7`
- [RtlpUnwindPrologue](../../text/2F/RtlpUnwindPrologue_function_002F5FA0.md) at `0x002F626B`
- [RtlpUnwindPrologue](../../text/2F/RtlpUnwindPrologue_function_002F5FA0.md) at `0x002F6400`
- [RtlpUnwindPrologue](../../text/2F/RtlpUnwindPrologue_function_002F5FA0.md) at `0x002F652D`
- [RtlpUnwindPrologue](../../text/2F/RtlpUnwindPrologue_function_002F5FA0.md) at `0x002F6577`
- [RtlpUnwindPrologue](../../text/2F/RtlpUnwindPrologue_function_002F5FA0.md) at `0x002F6714`
- [RtlpUnwindPrologue](../../text/2F/RtlpUnwindPrologue_function_002F5FA0.md) at `0x002F67C2`
- [NtTraceEvent](../../text/2F/NtTraceEvent_function_002FA6C0.md) at `0x002FA7DC`
- [NtTraceEvent](../../text/2F/NtTraceEvent_function_002FA6C0.md) at `0x002FAB89`
- [NtTraceEvent](../../text/2F/NtTraceEvent_function_002FA6C0.md) at `0x002FACC0`
- [NtTraceEvent](../../text/2F/NtTraceEvent_function_002FA6C0.md) at `0x002FAE7C`
- [NtTraceEvent](../../text/2F/NtTraceEvent_function_002FA6C0.md) at `0x002FAF68`
- [NtTraceEvent](../../text/2F/NtTraceEvent_function_002FA6C0.md) at `0x002FAF72`
- [EtwTraceEvent](../../text/2F/EtwTraceEvent_function_002FD290.md) at `0x002FD521`
- [EtwTraceEvent](../../text/2F/EtwTraceEvent_function_002FD290.md) at `0x002FD54E`
- [EtwTraceEvent](../../text/2F/EtwTraceEvent_function_002FD290.md) at `0x002FD666`
- [EtwTraceEvent](../../text/2F/EtwTraceEvent_function_002FD290.md) at `0x002FD6C9`
- [NtSetInformationWorkerFactory](../../text/35/NtSetInformationWorkerFactory_function_00350A30.md) at `0x00350B6B`
- [NtSetInformationWorkerFactory](../../text/35/NtSetInformationWorkerFactory_function_00350A30.md) at `0x00350BA0`
- [NtSetInformationWorkerFactory](../../text/35/NtSetInformationWorkerFactory_function_00350A30.md) at `0x00350C01`
- [NtWaitForWorkViaWorkerFactory](../../text/39/NtWaitForWorkViaWorkerFactory_function_00394270.md) at `0x003943E3`
- [KiInitializeUserApc](../../text/3D/KiInitializeUserApc_function_003D8D38.md) at `0x003D915A`
- [EtwpApplyEventNameFilter](../../text/3F/EtwpApplyEventNameFilter_function_003F10B8.md) at `0x003F13A3`
- [EtwpApplyPayloadFilterInternal](../../text/3F/EtwpApplyPayloadFilterInternal_function_003F43D0.md) at `0x003F4616`
- [RtlpUnwindEpilogue](../../text/3F/RtlpUnwindEpilogue_function_003F8E90.md) at `0x003F8EE5`
- [RtlpUnwindEpilogue](../../text/3F/RtlpUnwindEpilogue_function_003F8E90.md) at `0x003F8FF4`
- [RtlpUnwindEpilogue](../../text/3F/RtlpUnwindEpilogue_function_003F8E90.md) at `0x003F9123`
- [IopValidateAndGetWriteParameters](../../text/40/IopValidateAndGetWriteParameters_function_00400C30.md) at `0x00400DEF`
- [RtlpWalkWowStack](../../text/40/RtlpWalkWowStack_function_004095B0.md) at `0x0040978B`
- [RtlpConvertFunctionEntry](../../text/41/RtlpConvertFunctionEntry_function_00416CA0.md) at `0x00416CD4`
- [KiContinueEx](../../text/41/KiContinueEx_function_0041C370.md) at `0x0041C413`
- [KiContinueEx](../../text/41/KiContinueEx_function_0041C370.md) at `0x0041C4CB`
- [PopCaptureReasonContext](../../text/41/PopCaptureReasonContext_function_0041CE0C.md) at `0x0041D0A0`
- [PopSafeCopyUnicodeString](../../text/41/PopSafeCopyUnicodeString_function_0041D0AC.md) at `0x0041D156`
- [SeCaptureObjectTypeList](../../text/43/SeCaptureObjectTypeList_function_00434320.md) at `0x0043438C`
- [SeCaptureObjectTypeList](../../text/43/SeCaptureObjectTypeList_function_00434320.md) at `0x00434433`
- [SeAccessCheckByType](../../text/44/SeAccessCheckByType_function_00440BC8.md) at `0x00442796`
- [KiProcessControlProtection](../../text/44/KiProcessControlProtection_function_00444750.md) at `0x00444867`
- [RtlInsertDynamicUserFunctionTable](../../text/45/RtlInsertDynamicUserFunctionTable_function_004513C4.md) at `0x0045141E`
- [SeCaptureObjectAttributeSecurityDescriptorPresent](../../text/45/SeCaptureObjectAttributeSecurityDescriptorPresent_function_0045F834.md) at `0x0045F84C`
- [RtlRemoveDynamicUserFunctionTable](../../text/46/RtlRemoveDynamicUserFunctionTable_function_00466514.md) at `0x0046652A`
- [PsQueryProcessCommandLine](../../text/46/PsQueryProcessCommandLine_function_00469810.md) at `0x004699CF`
- [SepCaptureTokenSecurityOperations](../../text/48/SepCaptureTokenSecurityOperations_function_004883D4.md) at `0x00488483`
- [RtlpLookupPrimaryFunctionEntry](../../text/48/RtlpLookupPrimaryFunctionEntry_function_0048E8D0.md) at `0x0048E8FD`
- [MmUpdateUserShadowStackValue](../../text/49/MmUpdateUserShadowStackValue_function_004935D8.md) at `0x00493604`
- [RtlGetThreadLangIdByIndex](../../text/4A/RtlGetThreadLangIdByIndex_function_004A5FE0.md) at `0x004A6071`
- [RtlGetThreadLangIdByIndex](../../text/4A/RtlGetThreadLangIdByIndex_function_004A5FE0.md) at `0x004A60B0`
- [RtlCreateEnclaveReturnFrame](../../text/4B/RtlCreateEnclaveReturnFrame_function_004B3728.md) at `0x004B37BA`
- [NtQueryInformationWorkerFactory](../../text/4D/NtQueryInformationWorkerFactory_function_004D4480.md) at `0x004D44DB`
- [IopLoadDriverImage](../../text/4F/IopLoadDriverImage_function_004FA0FC.md) at `0x004FA1B6`
- [PsSetCpuQuotaInformation](../../text/5E/PsSetCpuQuotaInformation_function_005E28F8.md) at `0x005E296F`
- [RtlLookupExceptionHandler](../../text/5E/RtlLookupExceptionHandler_function_005E6A48.md) at `0x005E6A7F`
- [SepGetLearningModeObjectInformation](../../text/60/SepGetLearningModeObjectInformation_function_00608F74.md) at `0x00609022`
- [SepGetLearningModeObjectInformation](../../text/60/SepGetLearningModeObjectInformation_function_00608F74.md) at `0x00609086`
- [SepGetLearningModeObjectInformation](../../text/60/SepGetLearningModeObjectInformation_function_00608F74.md) at `0x006090B1`
- [SepGetLearningModeObjectInformation](../../text/60/SepGetLearningModeObjectInformation_function_00608F74.md) at `0x006090FD`
- [SepGetLearningModeObjectInformation](../../text/60/SepGetLearningModeObjectInformation_function_00608F74.md) at `0x0060912F`
- [DifExRaiseDatatypeMisalignmentWrapper](../../text/62/DifExRaiseDatatypeMisalignmentWrapper_function_00621B80.md) at `0x00621C30`
- [DifProbeForReadWrapper](../../text/63/DifProbeForReadWrapper_function_0063A5D0.md) at `0x0063A6B9`
- [EtwTraceRaw](../../text/65/EtwTraceRaw_function_006516CC.md) at `0x006517BD`
- [MiDbgCopyMemory](../../text/68/MiDbgCopyMemory_function_00684A18.md) at `0x00684B74`
- [NtReplacePartitionUnit](../../text/6A/NtReplacePartitionUnit_function_006A85A0.md) at `0x006A864F`
- [NtReplacePartitionUnit](../../text/6A/NtReplacePartitionUnit_function_006A85A0.md) at `0x006A8673`
- [sub_006EBB6A](../../text/6E/Unknown_function_006EBB6A.md) at `0x006EBBB4`
- [sub_006EBB6A](../../text/6E/Unknown_function_006EBB6A.md) at `0x006EBC4D`
- [sub_006FB4B8](../../text/6F/Unknown_function_006FB4B8.md) at `0x006FB4CD`
- [PiCMCaptureProblemInputData](../70/PiCMCaptureProblemInputData_function_00704E10.md) at `0x00704E42`
- [NtSetInformationDebugObject](../71/NtSetInformationDebugObject_function_007107B0.md) at `0x007107E5`
- [IopSetEaOrQuotaInformationFile](../71/IopSetEaOrQuotaInformationFile_function_0071BD70.md) at `0x0071BDF1`
- [IopSetFileObjectIosbRange](../71/IopSetFileObjectIosbRange_function_0071C1C8.md) at `0x0071C349`
- [IopSetFileObjectIosbRange](../71/IopSetFileObjectIosbRange_function_0071C1C8.md) at `0x0071C354`
- [NtQueryQuotaInformationFile](../72/NtQueryQuotaInformationFile_function_00720FE0.md) at `0x007210FB`
- [NtQueryQuotaInformationFile](../72/NtQueryQuotaInformationFile_function_00720FE0.md) at `0x00721140`
- [NtSetVolumeInformationFile](../72/NtSetVolumeInformationFile_function_00721750.md) at `0x00721867`
- [NtSetVolumeInformationFile](../72/NtSetVolumeInformationFile_function_00721750.md) at `0x00721888`
- [AlpcpPortQueryServerInfo](../74/AlpcpPortQueryServerInfo_function_0074C784.md) at `0x0074C7D0`
- [NtSetInformationSymbolicLink](../74/NtSetInformationSymbolicLink_function_0074E910.md) at `0x0074E9BE`
- [NtSetInformationSymbolicLink](../74/NtSetInformationSymbolicLink_function_0074E910.md) at `0x0074EA35`
- [ObSetRefTraceInformation](../74/ObSetRefTraceInformation_function_0074F7B0.md) at `0x0074F804`
- [ObpStartRuntimeStackTrace](../75/ObpStartRuntimeStackTrace_function_00750134.md) at `0x00750225`
- [ObpStartRuntimeStackTrace](../75/ObpStartRuntimeStackTrace_function_00750134.md) at `0x0075033D`
- [PfpQueryFileExtentsRequest](../75/PfpQueryFileExtentsRequest_function_007508E8.md) at `0x00750A91`
- [PspCaptureSystemServiceInMemoryArgs](../77/PspCaptureSystemServiceInMemoryArgs_function_0077E400.md) at `0x0077E419`
- [NtCreateThread](../78/NtCreateThread_function_00780B40.md) at `0x00780CF8`
- [NtCreateCpuPartition](../78/NtCreateCpuPartition_function_00782E30.md) at `0x00782ED5`
- [NtSetInformationCpuPartition](../78/NtSetInformationCpuPartition_function_00783510.md) at `0x0078357B`
- [NtAlertMultipleThreadByThreadId](../78/NtAlertMultipleThreadByThreadId_function_00789650.md) at `0x007896FB`
- [NtAlertMultipleThreadByThreadId](../78/NtAlertMultipleThreadByThreadId_function_00789650.md) at `0x00789756`
- [SepCaptureAuditPolicy](../79/SepCaptureAuditPolicy_function_0079FC80.md) at `0x0079FC96`
- [SepCaptureFqbnArray](../79/SepCaptureFqbnArray_function_0079FD38.md) at `0x0079FDC2`
- [SepCaptureFqbnArray](../79/SepCaptureFqbnArray_function_0079FD38.md) at `0x0079FEAE`
- [SepCaptureOctetStringArray](../79/SepCaptureOctetStringArray_function_0079FF6C.md) at `0x0079FFEE`
- [SmProcessCompressionAcceleratorRequest](../7A/SmProcessCompressionAcceleratorRequest_function_007A5EEC.md) at `0x007A5F47`
- [SmProcessCompressionReadStatsRequest](../7A/SmProcessCompressionReadStatsRequest_function_007A6090.md) at `0x007A6100`
- [SmProcessConfigRequest](../7A/SmProcessConfigRequest_function_007A62E4.md) at `0x007A6714`
- [SmProcessConfigRequest](../7A/SmProcessConfigRequest_function_007A62E4.md) at `0x007A671A`
- [SmProcessDeleteRequest](../7A/SmProcessDeleteRequest_function_007A6728.md) at `0x007A6742`
- [SmProcessListRequest](../7A/SmProcessListRequest_function_007A67A8.md) at `0x007A6834`
- [SmProcessProcessStoreInfoRequest](../7A/SmProcessProcessStoreInfoRequest_function_007A6B48.md) at `0x007A6B92`
- [SmProcessRegistrationRequest](../7A/SmProcessRegistrationRequest_function_007A6C8C.md) at `0x007A6CBD`
- [SmProcessStatsRequest](../7A/SmProcessStatsRequest_function_007A6E68.md) at `0x007A6EDD`
- [SmcProcessCreateRequest](../7A/SmcProcessCreateRequest_function_007A764C.md) at `0x007A76BE`
- [SmcProcessDeleteRequest](../7A/SmcProcessDeleteRequest_function_007A7900.md) at `0x007A791A`
- [SmcProcessListRequest](../7A/SmcProcessListRequest_function_007A7988.md) at `0x007A79DE`
- [SmcProcessResizeRequest](../7A/SmcProcessResizeRequest_function_007A7B1C.md) at `0x007A7B4C`
- [SmcProcessStatsRequest](../7A/SmcProcessStatsRequest_function_007A7BFC.md) at `0x007A7C58`
- [SmcProcessStoreCreateRequest](../7A/SmcProcessStoreCreateRequest_function_007A7E14.md) at `0x007A7E5B`
- [SmcProcessStoreDeleteRequest](../7A/SmcProcessStoreDeleteRequest_function_007A7F80.md) at `0x007A7F9D`
- [WmipQuerySingleMultiple](../7B/WmipQuerySingleMultiple_function_007B36F0.md) at `0x007B3CE4`
- [EtwpSetMark](../7B/EtwpSetMark_function_007B878C.md) at `0x007B87F4`
- [WmiQueryTraceInformation](../7B/WmiQueryTraceInformation_function_007B9370.md) at `0x007B970D`
- [ExpSetTimeZoneInformation](../7C/ExpSetTimeZoneInformation_function_007C5240.md) at `0x007C52AD`
- [ExpSetTimeZoneInformation](../7C/ExpSetTimeZoneInformation_function_007C5240.md) at `0x007C5373`
- [NtQuerySystemTime](../7C/NtQuerySystemTime_function_007C6570.md) at `0x007C658F`
- [NtSetSystemTime](../7C/NtSetSystemTime_function_007C65F0.md) at `0x007C66FD`
- [ExpSetBootEntry](../7C/ExpSetBootEntry_function_007CBD2C.md) at `0x007CBE0B`
- [ExpSetDriverEntry](../7C/ExpSetDriverEntry_function_007CC424.md) at `0x007CC4F2`
- [NtQuerySystemEnvironmentValue](../7C/NtQuerySystemEnvironmentValue_function_007CDFB0.md) at `0x007CE02D`
- [NtQuerySystemEnvironmentValue](../7C/NtQuerySystemEnvironmentValue_function_007CDFB0.md) at `0x007CE06C`
- [NtSetBootOptions](../7C/NtSetBootOptions_function_007CE2B0.md) at `0x007CE345`
- [NtSetDriverEntryOrder](../7C/NtSetDriverEntryOrder_function_007CE490.md) at `0x007CE555`
- [NtSetSystemEnvironmentValue](../7C/NtSetSystemEnvironmentValue_function_007CE650.md) at `0x007CE711`
- [NtSetSystemEnvironmentValue](../7C/NtSetSystemEnvironmentValue_function_007CE650.md) at `0x007CE761`
- [NtSetSystemEnvironmentValue](../7C/NtSetSystemEnvironmentValue_function_007CE650.md) at `0x007CE7AB`
- [NtSetSystemEnvironmentValueEx](../7C/NtSetSystemEnvironmentValueEx_function_007CE990.md) at `0x007CEA63`
- [NtSetSystemEnvironmentValueEx](../7C/NtSetSystemEnvironmentValueEx_function_007CE990.md) at `0x007CEBDE`
- [ExpKdPullRemoteFileForUser](../7D/ExpKdPullRemoteFileForUser_function_007D15AC.md) at `0x007D1610`
- [ExpProfileCreate](../7D/ExpProfileCreate_function_007D1AB8.md) at `0x007D1CB4`
- [NtCreateKeyedEvent](../7D/NtCreateKeyedEvent_function_007D4CF0.md) at `0x007D4D26`
- [NtOpenKeyedEvent](../7D/NtOpenKeyedEvent_function_007D4E00.md) at `0x007D4E2D`
- [NtCompactKeys](../7D/NtCompactKeys_function_007DF730.md) at `0x007DF813`
- [NtRenameKey](../7E/NtRenameKey_function_007E04B0.md) at `0x007E05FF`
- [CmUpdateFeatureConfiguration](../7E/CmUpdateFeatureConfiguration_function_007E5C10.md) at `0x007E5D46`
- [MiCreatePagingFile](../7F/MiCreatePagingFile_function_007FEFF4.md) at `0x007FF133`
- [NtCreateEnclave](../80/NtCreateEnclave_function_00808CC0.md) at `0x00808EE5`
- [MiCaptureUlongPtrArray](../80/MiCaptureUlongPtrArray_function_0080A664.md) at `0x0080A6C6`
- [MiCaptureUlongPtrArray](../80/MiCaptureUlongPtrArray_function_0080A664.md) at `0x0080A733`
- [MmManagePartitionCharges](../80/MmManagePartitionCharges_function_0080DDAC.md) at `0x0080DE8B`
- [AhcCacheQueryHwId](../83/AhcCacheQueryHwId_function_0083ACB8.md) at `0x0083ADE6`
- [NtSetValueKey](../84/NtSetValueKey_function_00844EA0.md) at `0x008450C9`
- [NtDeleteValueKey](../84/NtDeleteValueKey_function_00848770.md) at `0x0084891E`
- [NtQueryKey](../86/NtQueryKey_function_008676E0.md) at `0x008678BE`
- [NtQuerySecurityObject](../87/NtQuerySecurityObject_function_008737B0.md) at `0x0087386E`
- [CmCreateKey](../87/CmCreateKey_function_00875020.md) at `0x008751B8`
- [CmCreateKey](../87/CmCreateKey_function_00875020.md) at `0x008752B7`
- [CmCreateKey](../87/CmCreateKey_function_00875020.md) at `0x008752E2`
- [CmLoadDifferencingKey](../87/CmLoadDifferencingKey_function_00875670.md) at `0x00875A96`
- [CmLoadDifferencingKey](../87/CmLoadDifferencingKey_function_00875670.md) at `0x00875A9C`
- [CmOpenKey](../87/CmOpenKey_function_00876350.md) at `0x0087643C`
- [CmOpenKey](../87/CmOpenKey_function_00876350.md) at `0x008764BB`
- [CmpNameFromAttributes](../87/CmpNameFromAttributes_function_00876AC8.md) at `0x00876C07`
- [CmpNameFromAttributes](../87/CmpNameFromAttributes_function_00876AC8.md) at `0x00876C29`
- [PspFreeUserFiberShadowStack](../87/PspFreeUserFiberShadowStack_function_0087F9A0.md) at `0x0087F9F0`
- [NtAlpcCreateSectionView](../88/NtAlpcCreateSectionView_function_00888640.md) at `0x008886A5`
- [AlpcpCaptureAttributes](../88/AlpcpCaptureAttributes_function_0088CD20.md) at `0x0088CF06`
- [NtAlpcCreateSecurityContext](NtAlpcCreateSecurityContext_function_00890B50.md) at `0x00890C21`
- [AlpcpCaptureHandleAttributeInternal](AlpcpCaptureHandleAttributeInternal_function_00892CDC.md) at `0x00892F5F`
- [NtAlpcQueryInformationMessage](NtAlpcQueryInformationMessage_function_00894700.md) at `0x00894772`
- [PsOpenProcess](PsOpenProcess_function_00894A30.md) at `0x008950A2`
- [PsOpenProcess](PsOpenProcess_function_00894A30.md) at `0x008950A7`
- [NtReplyWaitReceivePortEx](NtReplyWaitReceivePortEx_function_00895850.md) at `0x008958B3`
- [AlpcpReceiveLegacyMessage](AlpcpReceiveLegacyMessage_function_00895DE0.md) at `0x00895E83`
- [NtAlpcImpersonateClientOfPort](NtAlpcImpersonateClientOfPort_function_008961A0.md) at `0x00896225`
- [AlpcpReceiveMessage](AlpcpReceiveMessage_function_00897ED0.md) at `0x00897FB1`
- [AlpcpProbeForWriteMessageHeader](AlpcpProbeForWriteMessageHeader_function_00898660.md) at `0x0089867D`
- [MiMapViewOfSectionCommon](MiMapViewOfSectionCommon_function_00898C90.md) at `0x00898DF3`
- [AlpcpProbeMessageAttributes](AlpcpProbeMessageAttributes_function_008995A0.md) at `0x0089964B`
- [NtDelayExecution](NtDelayExecution_function_00899EE0.md) at `0x00899F01`
- [ObpCaptureObjectCreateInformation](ObpCaptureObjectCreateInformation_function_0089B930.md) at `0x0089BA84`
- [ObpCaptureObjectName](ObpCaptureObjectName_function_0089BC40.md) at `0x0089BCCE`
- [NtQueryFullAttributesFile](../8A/NtQueryFullAttributesFile_function_008A0D10.md) at `0x008A0D76`
- [NtQueryAttributesFile](../8A/NtQueryAttributesFile_function_008A0FA0.md) at `0x008A1005`
- [EtwpQueryProcessCommandLine](../8A/EtwpQueryProcessCommandLine_function_008A5C20.md) at `0x008A5D02`
- [NtQueryObject](../8A/NtQueryObject_function_008A6DB0.md) at `0x008A6EC3`
- [MiCreateSectionCommon](../8A/MiCreateSectionCommon_function_008A9AA4.md) at `0x008A9CF2`
- [IopCreateFile](../8A/IopCreateFile_function_008AB298.md) at `0x008AB41C`
- [IopCreateFile](../8A/IopCreateFile_function_008AB298.md) at `0x008ABB22`
- [IopCreateFile](../8A/IopCreateFile_function_008AB298.md) at `0x008ABBFB`
- [IopCreateFile](../8A/IopCreateFile_function_008AB298.md) at `0x008ABC05`
- [IopCreateFile](../8A/IopCreateFile_function_008AB298.md) at `0x008ABCB6`
- [IopCreateFile](../8A/IopCreateFile_function_008AB298.md) at `0x008ABDD4`
- [NtQueryEaFile](../8A/NtQueryEaFile_function_008AC1B0.md) at `0x008AC3B9`
- [NtQueryVolumeInformationFile](../8A/NtQueryVolumeInformationFile_function_008AC8C0.md) at `0x008ACA1A`
- [IopValidateQueryInformationParameters](../8A/IopValidateQueryInformationParameters_function_008AE440.md) at `0x008AE592`
- [IopReadFile](../8A/IopReadFile_function_008AEFF0.md) at `0x008AF982`
- [CmpCaptureKeyValueArray](../8B/CmpCaptureKeyValueArray_function_008B1074.md) at `0x008B1210`
- [NtQueryValueKey](../8B/NtQueryValueKey_function_008B2A00.md) at `0x008B2D25`
- [NtQueryValueKey](../8B/NtQueryValueKey_function_008B2A00.md) at `0x008B2D2E`
- [NtEnumerateValueKey](../8B/NtEnumerateValueKey_function_008B3B50.md) at `0x008B3D1D`
- [SeCaptureSecurityQos](../8B/SeCaptureSecurityQos_function_008B71B8.md) at `0x008B71D7`
- [EtwpGetLoggerInfoFromContext](../8B/EtwpGetLoggerInfoFromContext_function_008BEF90.md) at `0x008BF2C9`
- [NtSetInformationThread](../8C/NtSetInformationThread_function_008C9F60.md) at `0x008CA0ED`
- [NtSetInformationThread](../8C/NtSetInformationThread_function_008C9F60.md) at `0x008CA865`
- [NtImpersonateThread](../8C/NtImpersonateThread_function_008CD230.md) at `0x008CD288`
- [RtlpWriteExtendedContext](../8D/RtlpWriteExtendedContext_function_008D4A5C.md) at `0x008D4B93`
- [RtlpReadExtendedContext](../8D/RtlpReadExtendedContext_function_008D61D0.md) at `0x008D63FC`
- [RtlpReadExtendedContext](../8D/RtlpReadExtendedContext_function_008D61D0.md) at `0x008D6442`
- [RtlpReadExtendedContextLayout](../8D/RtlpReadExtendedContextLayout_function_008D64F0.md) at `0x008D6551`
- [PiControlCopyUserModeCallersBuffer](../8E/PiControlCopyUserModeCallersBuffer_function_008E4720.md) at `0x008E47E8`
- [PiControlCopyUserModeCallersBuffer](../8E/PiControlCopyUserModeCallersBuffer_function_008E4720.md) at `0x008E47EE`
- [NtAlpcQueryInformation](../8E/NtAlpcQueryInformation_function_008E7200.md) at `0x008E72E5`
- [PiCMCaptureObjectInputData](../8E/PiCMCaptureObjectInputData_function_008E8220.md) at `0x008E82D4`
- [NtRemoveIoCompletionEx](../8E/NtRemoveIoCompletionEx_function_008E8760.md) at `0x008E8970`
- [NtQueryEvent](../8E/NtQueryEvent_function_008E8F90.md) at `0x008E904B`
- [ProbeForWrite](../8E/ProbeForWrite_function_008E91C0.md) at `0x008E9227`
- [BuildQueryDirectoryIrp](../8E/BuildQueryDirectoryIrp_function_008EC770.md) at `0x008ECA2D`
- [PiCMCaptureRegistryPropertyInputData](../8E/PiCMCaptureRegistryPropertyInputData_function_008ED078.md) at `0x008ED13F`
- [PiCMCapturePropertyInputData](../8E/PiCMCapturePropertyInputData_function_008ED3A0.md) at `0x008ED46E`
- [PiCMReturnBufferResultData](../8E/PiCMReturnBufferResultData_function_008ED6D0.md) at `0x008ED7C3`
- [PfpVirtualQuery](../90/PfpVirtualQuery_function_00901C1C.md) at `0x00901C51`
- [PfQuerySuperfetchInformation](../90/PfQuerySuperfetchInformation_function_0090210C.md) at `0x00902311`
- [PfpCopyUserPfnPrioRequest](../90/PfpCopyUserPfnPrioRequest_function_00902690.md) at `0x009026F0`
- [PfGetCompletedTrace](../90/PfGetCompletedTrace_function_00902950.md) at `0x00902A13`
- [NtManagePartition](../90/NtManagePartition_function_00902FC0.md) at `0x009030A3`
- [NtGetCompleteWnfStateSubscription](../90/NtGetCompleteWnfStateSubscription_function_00909450.md) at `0x0090953E`
- [NtQuerySection](../92/NtQuerySection_function_00921770.md) at `0x00921816`
- [NtSecureConnectPort](../92/NtSecureConnectPort_function_00922F20.md) at `0x009230DE`
- [SeCaptureSid](../92/SeCaptureSid_function_009276D4.md) at `0x00927747`
- [SeCaptureSecurityDescriptor](../92/SeCaptureSecurityDescriptor_function_00929F40.md) at `0x00929FF3`
- [SeCaptureSecurityDescriptor](../92/SeCaptureSecurityDescriptor_function_00929F40.md) at `0x00929FF8`
- [SeCaptureSecurityDescriptor](../92/SeCaptureSecurityDescriptor_function_00929F40.md) at `0x0092A16D`
- [SeCaptureSecurityDescriptor](../92/SeCaptureSecurityDescriptor_function_00929F40.md) at `0x0092A20D`
- [SeCaptureSecurityDescriptor](../92/SeCaptureSecurityDescriptor_function_00929F40.md) at `0x0092A4A2`
- [SeCaptureSecurityDescriptor](../92/SeCaptureSecurityDescriptor_function_00929F40.md) at `0x0092A5CE`
- [PfpPrefetchRequest](../93/PfpPrefetchRequest_function_009385CC.md) at `0x00938641`
- [NtCopyFileChunk](../94/NtCopyFileChunk_function_0094B600.md) at `0x0094B73B`
- [NtQuerySystemEnvironmentValueEx](../95/NtQuerySystemEnvironmentValueEx_function_00952180.md) at `0x0095227A`
- [NtQuerySystemEnvironmentValueEx](../95/NtQuerySystemEnvironmentValueEx_function_00952180.md) at `0x0095233F`
- [ExpStringCapture](../95/ExpStringCapture_function_00959BF4.md) at `0x00959C6C`
- [ExpGetDeviceDataInformation](../95/ExpGetDeviceDataInformation_function_0095A300.md) at `0x0095A421`
- [PfSnGetUnsafeProcessParameters](../96/PfSnGetUnsafeProcessParameters_function_00960878.md) at `0x009608A8`
- [PfSnParsePrefetchParam](../96/PfSnParsePrefetchParam_function_0096092C.md) at `0x00960A25`
- [PfSnSetPrefetcherInformation](../96/PfSnSetPrefetcherInformation_function_0096139C.md) at `0x0096148A`
- [PfSnSetPrefetcherInformation](../96/PfSnSetPrefetcherInformation_function_0096139C.md) at `0x0096151A`
- [PiCMCaptureRegistryInputData](../96/PiCMCaptureRegistryInputData_function_00962108.md) at `0x009621BA`
- [PiCMReturnHandleResultData](../96/PiCMReturnHandleResultData_function_00962354.md) at `0x009623E0`
- [PiCMCaptureRegisterInterfaceInputData](../96/PiCMCaptureRegisterInterfaceInputData_function_00962C94.md) at `0x00962D04`
- [PiCMCaptureRegisterInterfaceInputData](../96/PiCMCaptureRegisterInterfaceInputData_function_00962C94.md) at `0x00962DBD`
- [NtQueryLicenseValue](../96/NtQueryLicenseValue_function_0096BCC0.md) at `0x0096BE84`
- [SepCaptureTokenSecurityAttributesAndOperationsInformation](../97/SepCaptureTokenSecurityAttributesAndOperationsInformation_function_00971E0C.md) at `0x00971ED3`
- [SepCaptureTokenSecurityAttributesInformation](../97/SepCaptureTokenSecurityAttributesInformation_function_00971FB8.md) at `0x0097232E`
- [SepCaptureTokenSecurityAttributesInformation](../97/SepCaptureTokenSecurityAttributesInformation_function_00971FB8.md) at `0x00972376`
- [SepCaptureTokenSecurityAttributesInformation](../97/SepCaptureTokenSecurityAttributesInformation_function_00971FB8.md) at `0x009723B9`
- [SepCaptureInt64Array](../97/SepCaptureInt64Array_function_00972B84.md) at `0x00972C16`
- [NtQuerySecurityAttributesToken](../97/NtQuerySecurityAttributesToken_function_00972C80.md) at `0x00972DB0`
- [SepCaptureUnicodeStringArray](../97/SepCaptureUnicodeStringArray_function_00972F70.md) at `0x00973105`
- [SeCaptureUnicodeStringStructures](../97/SeCaptureUnicodeStringStructures_function_00973210.md) at `0x009732DC`
- [NtQuerySecurityPolicy](../97/NtQuerySecurityPolicy_function_00973410.md) at `0x00973537`
- [NtSetCachedSigningLevel2](../97/NtSetCachedSigningLevel2_function_00973720.md) at `0x0097387E`
- [NtSetCachedSigningLevel2](../97/NtSetCachedSigningLevel2_function_00973720.md) at `0x009738BB`
- [NtPrivilegeObjectAuditAlarm](../97/NtPrivilegeObjectAuditAlarm_function_00974170.md) at `0x0097427B`
- [NtPrivilegedServiceAuditAlarm](../97/NtPrivilegedServiceAuditAlarm_function_00974430.md) at `0x0097451B`
- [NtOpenObjectAuditAlarm](../97/NtOpenObjectAuditAlarm_function_00974700.md) at `0x00974940`
- [SepProbeAndCaptureString_U](../97/SepProbeAndCaptureString_U_function_00975070.md) at `0x0097513E`
- [MiInitializeWowPeb](../98/MiInitializeWowPeb_function_0098079C.md) at `0x00980B6B`
- [MmCreatePeb](../98/MmCreatePeb_function_00980FB4.md) at `0x00981322`
- [PiCMCaptureEnumerateInputData](../99/PiCMCaptureEnumerateInputData_function_00992920.md) at `0x00992962`
- [MiCaptureAllocateMapExtendedParameters](../9A/MiCaptureAllocateMapExtendedParameters_function_009A2110.md) at `0x009A23C7`
- [NtQueryInformationProcess](../9A/NtQueryInformationProcess_function_009AA250.md) at `0x009AA91A`
- [NtQueryInformationProcess](../9A/NtQueryInformationProcess_function_009AA250.md) at `0x009ACCA5`
- [CmUnloadKey](../9A/CmUnloadKey_function_009AF2FC.md) at `0x009AF54D`
- [CmUnloadKey](../9A/CmUnloadKey_function_009AF2FC.md) at `0x009AF56F`
- [EtwpCaptureString](../9B/EtwpCaptureString_function_009BD754.md) at `0x009BD7BD`
- [ProbeForRead](../9C/ProbeForRead_function_009C5130.md) at `0x009C5164`
- [PsOpenThread](../9C/PsOpenThread_function_009C5CC0.md) at `0x009C6333`
- [PsOpenThread](../9C/PsOpenThread_function_009C5CC0.md) at `0x009C6338`
- [NtAdjustGroupsToken](../9C/NtAdjustGroupsToken_function_009C6640.md) at `0x009C66FE`
- [SeCaptureAcl](../9C/SeCaptureAcl_function_009C6A58.md) at `0x009C6ABA`
- [NtFilterToken](../9C/NtFilterToken_function_009C7890.md) at `0x009C79A1`
- [NtCreateTokenEx](../9C/NtCreateTokenEx_function_009C7C80.md) at `0x009C7EA6`
- [NtAdjustPrivilegesToken](../9C/NtAdjustPrivilegesToken_function_009C86C0.md) at `0x009C8737`
- [NtPrivilegeCheck](../9C/NtPrivilegeCheck_function_009C8AE0.md) at `0x009C8C19`
- [SeCaptureLuidAndAttributesArray](../9C/SeCaptureLuidAndAttributesArray_function_009C8D18.md) at `0x009C8D74`
- [NtOpenPrivateNamespace](../9C/NtOpenPrivateNamespace_function_009C94E0.md) at `0x009C954F`
- [ObpCaptureBoundaryDescriptor](../9C/ObpCaptureBoundaryDescriptor_function_009C9738.md) at `0x009C97EC`
- [SeCaptureSidAndAttributesArray](../9C/SeCaptureSidAndAttributesArray_function_009C9D70.md) at `0x009CA143`
- [SeCaptureSidAndAttributesArray](../9C/SeCaptureSidAndAttributesArray_function_009C9D70.md) at `0x009CA155`
- [NtLockFile](../9D/NtLockFile_function_009D86D0.md) at `0x009D885E`
- [AlpcpCaptureIdMessage](../9D/AlpcpCaptureIdMessage_function_009DA680.md) at `0x009DA6B1`
- [WmipProbeAndCaptureGuidObjectAttributes](../9D/WmipProbeAndCaptureGuidObjectAttributes_function_009DEA00.md) at `0x009DEAE8`
- [WmipProbeAndCaptureGuidObjectAttributes](../9D/WmipProbeAndCaptureGuidObjectAttributes_function_009DEA00.md) at `0x009DEB48`
- [NtUnlockFile](../9E/NtUnlockFile_function_009E5DA0.md) at `0x009E5E96`
- [PspCaptureUserProcessParameters](../9E/PspCaptureUserProcessParameters_function_009E63C0.md) at `0x009E64AD`
- [NtQuerySymbolicLinkObject](../9E/NtQuerySymbolicLinkObject_function_009EBA20.md) at `0x009EBB16`
- [PspBuildCreateProcessContext](../9E/PspBuildCreateProcessContext_function_009ED6E0.md) at `0x009EEF99`
- [PspBuildCreateProcessContext](../9E/PspBuildCreateProcessContext_function_009ED6E0.md) at `0x009EEF9E`
- [PspBuildCreateProcessContext](../9E/PspBuildCreateProcessContext_function_009ED6E0.md) at `0x009EEFA3`
- [PspBuildCreateProcessContext](../9E/PspBuildCreateProcessContext_function_009ED6E0.md) at `0x009EEFA8`
- [PspBuildCreateProcessContext](../9E/PspBuildCreateProcessContext_function_009ED6E0.md) at `0x009EEFAD`
- [PspBuildCreateProcessContext](../9E/PspBuildCreateProcessContext_function_009ED6E0.md) at `0x009EEFB2`
- [PspBuildCreateProcessContext](../9E/PspBuildCreateProcessContext_function_009ED6E0.md) at `0x009EEFB7`
- [PspBuildCreateProcessContext](../9E/PspBuildCreateProcessContext_function_009ED6E0.md) at `0x009EEFBC`
- [PspBuildCreateProcessContext](../9E/PspBuildCreateProcessContext_function_009ED6E0.md) at `0x009EEFC1`
- [PspBuildCreateProcessContext](../9E/PspBuildCreateProcessContext_function_009ED6E0.md) at `0x009EEFC6`
- [PspBuildCreateProcessContext](../9E/PspBuildCreateProcessContext_function_009ED6E0.md) at `0x009EEFCB`
- [PspBuildCreateProcessContext](../9E/PspBuildCreateProcessContext_function_009ED6E0.md) at `0x009EEFD0`
- [PspBuildCreateProcessContext](../9E/PspBuildCreateProcessContext_function_009ED6E0.md) at `0x009EEFD5`
- [PspBuildCreateProcessContext](../9E/PspBuildCreateProcessContext_function_009ED6E0.md) at `0x009EEFDA`
- [PspBuildCreateProcessContext](../9E/PspBuildCreateProcessContext_function_009ED6E0.md) at `0x009EEFDF`
- [PspBuildCreateProcessContext](../9E/PspBuildCreateProcessContext_function_009ED6E0.md) at `0x009EEFE4`
- [PspBuildCreateProcessContext](../9E/PspBuildCreateProcessContext_function_009ED6E0.md) at `0x009EEFE9`
- [PspBuildCreateProcessContext](../9E/PspBuildCreateProcessContext_function_009ED6E0.md) at `0x009EEFEE`
- [PspBuildCreateProcessContext](../9E/PspBuildCreateProcessContext_function_009ED6E0.md) at `0x009EEFF3`
- [PspBuildCreateProcessContext](../9E/PspBuildCreateProcessContext_function_009ED6E0.md) at `0x009EEFF8`
- [PspBuildCreateProcessContext](../9E/PspBuildCreateProcessContext_function_009ED6E0.md) at `0x009EEFFD`
- [PspBuildCreateProcessContext](../9E/PspBuildCreateProcessContext_function_009ED6E0.md) at `0x009EF002`
- [PspBuildCreateProcessContext](../9E/PspBuildCreateProcessContext_function_009ED6E0.md) at `0x009EF007`
- [PspBuildCreateProcessContext](../9E/PspBuildCreateProcessContext_function_009ED6E0.md) at `0x009EF00C`
- [PspBuildCreateProcessContext](../9E/PspBuildCreateProcessContext_function_009ED6E0.md) at `0x009EF011`
- [PspBuildCreateProcessContext](../9E/PspBuildCreateProcessContext_function_009ED6E0.md) at `0x009EF016`
- [PspBuildCreateProcessContext](../9E/PspBuildCreateProcessContext_function_009ED6E0.md) at `0x009EF01B`
- [PspBuildCreateProcessContext](../9E/PspBuildCreateProcessContext_function_009ED6E0.md) at `0x009EF020`
- [PspBuildCreateProcessContext](../9E/PspBuildCreateProcessContext_function_009ED6E0.md) at `0x009EF025`
- [NtSetInformationVirtualMemory](../9F/NtSetInformationVirtualMemory_function_009F4580.md) at `0x009F473C`
- [NtSetInformationVirtualMemory](../9F/NtSetInformationVirtualMemory_function_009F4580.md) at `0x009F480A`
- [NtSetInformationVirtualMemory](../9F/NtSetInformationVirtualMemory_function_009F4580.md) at `0x009F4817`
- [NtSetInformationVirtualMemory](../9F/NtSetInformationVirtualMemory_function_009F4580.md) at `0x009F4824`
- [NtQueryPerformanceCounter](../9F/NtQueryPerformanceCounter_function_009F5530.md) at `0x009F55B3`
- [NtSetInformationJobObject](../9F/NtSetInformationJobObject_function_009F84C0.md) at `0x009F86D1`
- [NtSetInformationJobObject](../9F/NtSetInformationJobObject_function_009F84C0.md) at `0x009FA8D4`
- [NtSetInformationJobObject](../9F/NtSetInformationJobObject_function_009F84C0.md) at `0x009FAE36`
- [NtQueryInformationJobObject](../9F/NtQueryInformationJobObject_function_009FB860.md) at `0x009FBBD2`
- [NtAllocateLocallyUniqueId](../A0/NtAllocateLocallyUniqueId_function_00A0E030.md) at `0x00A0E059`
- [SmProcessCompressionInfoRequest](../A0/SmProcessCompressionInfoRequest_function_00A0E980.md) at `0x00A0EA08`
- [PspCreateProcess](../A1/PspCreateProcess_function_00A12758.md) at `0x00A1291E`
- [PiCMCaptureInterfaceListInputData](../A1/PiCMCaptureInterfaceListInputData_function_00A165D4.md) at `0x00A16688`
- [SepAccessCheckAndAuditAlarm](../A1/SepAccessCheckAndAuditAlarm_function_00A1AF4C.md) at `0x00A1D859`
- [NtTranslateFilePath](../A2/NtTranslateFilePath_function_00A24D50.md) at `0x00A24F12`
- [PiCMCaptureDeviceListInputData](../A2/PiCMCaptureDeviceListInputData_function_00A2BD70.md) at `0x00A2BDDC`
- [PiCMCaptureDeviceListInputData](../A2/PiCMCaptureDeviceListInputData_function_00A2BD70.md) at `0x00A2BE70`
- [MiCheckForUserStackOverflow](../A3/MiCheckForUserStackOverflow_function_00A30854.md) at `0x00A30A41`
- [NtCreateSymbolicLinkObject](../A3/NtCreateSymbolicLinkObject_function_00A33870.md) at `0x00A33989`
- [AlpcpAcceptConnectPort](../A3/AlpcpAcceptConnectPort_function_00A34290.md) at `0x00A34D82`
- [AlpcpAcceptConnectPort](../A3/AlpcpAcceptConnectPort_function_00A34290.md) at `0x00A34D87`
- [NtAlpcCancelMessage](../A3/NtAlpcCancelMessage_function_00A3A860.md) at `0x00A3A97A`
- [NtCreateNamedPipeFile](../A3/NtCreateNamedPipeFile_function_00A3AF30.md) at `0x00A3AF9D`
- [PiCMCaptureInterfaceAliasInputData](../A4/PiCMCaptureInterfaceAliasInputData_function_00A47B18.md) at `0x00A47B84`
- [PiCMCaptureInterfaceAliasInputData](../A4/PiCMCaptureInterfaceAliasInputData_function_00A47B18.md) at `0x00A47C1F`
- [PspCaptureCreateInfo](../A4/PspCaptureCreateInfo_function_00A4A9B0.md) at `0x00A4A9C4`
- [SmProcessCreateRequest](../A5/SmProcessCreateRequest_function_00A50DD0.md) at `0x00A50E7B`
- [NtQuerySystemInformationEx](../A5/NtQuerySystemInformationEx_function_00A57690.md) at `0x00A5771E`
- [ExpQuerySystemInformation](../A5/ExpQuerySystemInformation_function_00A57858.md) at `0x00A5B7E2`
- [NtQueryTimer](../A6/NtQueryTimer_function_00A62390.md) at `0x00A62416`
- [NtRaiseHardError](../A6/NtRaiseHardError_function_00A64860.md) at `0x00A649BE`
- [NtRaiseHardError](../A6/NtRaiseHardError_function_00A64860.md) at `0x00A64A18`
- [IopRetrieveSystemDeviceName](../A6/IopRetrieveSystemDeviceName_function_00A6CBA8.md) at `0x00A6CC85`
- [PfSnHashUnsafeUnicodeString](../A7/PfSnHashUnsafeUnicodeString_function_00A701F0.md) at `0x00A70383`
- [NtQuerySemaphore](../A7/NtQuerySemaphore_function_00A71370.md) at `0x00A713E9`
- [SmProcessStoreMemoryPriorityRequest](../A7/SmProcessStoreMemoryPriorityRequest_function_00A7830C.md) at `0x00A78375`
- [SmProcessSystemStoreTrimRequest](../A7/SmProcessSystemStoreTrimRequest_function_00A784E0.md) at `0x00A787D0`
- [NtSetEaFile](../A7/NtSetEaFile_function_00A788A0.md) at `0x00A78933`
- [PfpRpControlRequestCopy](../A7/PfpRpControlRequestCopy_function_00A7CFF8.md) at `0x00A7D047`
- [NtQueryIoCompletion](../A8/NtQueryIoCompletion_function_00A885C0.md) at `0x00A88642`
- [NtExtendSection](../A8/NtExtendSection_function_00A8EC60.md) at `0x00A8ED1B`
- [NtCreateMailslotFile](../A9/NtCreateMailslotFile_function_00A945C0.md) at `0x00A94624`
- [NtAllocateUuids](../A9/NtAllocateUuids_function_00A963E0.md) at `0x00A96439`
- [PspGetStandardHandleList](../A9/PspGetStandardHandleList_function_00A98CC8.md) at `0x00A98D08`
- [NtConvertBetweenAuxiliaryCounterAndPerformanceCounter](../AA/NtConvertBetweenAuxiliaryCounterAndPerformanceCounter_function_00AA5B90.md) at `0x00AA5C1C`
- [IopReadFileScatter](../AA/IopReadFileScatter_function_00AA5D78.md) at `0x00AA5EF3`
- [IopReadFileScatter](../AA/IopReadFileScatter_function_00AA5D78.md) at `0x00AA5FE2`
- [IopWriteFileGather](../AA/IopWriteFileGather_function_00AAA95C.md) at `0x00AAAAE1`
- [IopWriteFileGather](../AA/IopWriteFileGather_function_00AAA95C.md) at `0x00AAABF2`
- [NtLoadKey3](../AA/NtLoadKey3_function_00AACC70.md) at `0x00AACD1A`
- [NtCreateLowBoxToken](../AB/NtCreateLowBoxToken_function_00AB9880.md) at `0x00AB9955`
- [NtCreateLowBoxToken](../AB/NtCreateLowBoxToken_function_00AB9880.md) at `0x00AB9C27`
- [IopUnloadDriver](../AB/IopUnloadDriver_function_00ABF868.md) at `0x00ABF943`
- [PiCMCaptureCreateDeviceInputData](../AC/PiCMCaptureCreateDeviceInputData_function_00ACBFA8.md) at `0x00ACC018`
- [PiCMCaptureCreateDeviceInputData](../AC/PiCMCaptureCreateDeviceInputData_function_00ACBFA8.md) at `0x00ACC0C7`
- [PopBootStatCheckIntegrity](../AC/PopBootStatCheckIntegrity_function_00ACDF4C.md) at `0x00ACDFFE`
- [PfpQueryScenarioInformation](../AD/PfpQueryScenarioInformation_function_00AD5324.md) at `0x00AD5365`
- [PfpQueryScenarioInformation](../AD/PfpQueryScenarioInformation_function_00AD5324.md) at `0x00AD53CE`
- [AlpcpValidateDataInformation](../AD/AlpcpValidateDataInformation_function_00ADA7C8.md) at `0x00ADA801`
- [PfSetSuperfetchInformation](../AD/PfSetSuperfetchInformation_function_00ADE6E8.md) at `0x00ADF2C6`
- [PfSetSuperfetchInformation](../AD/PfSetSuperfetchInformation_function_00ADE6E8.md) at `0x00ADF2CC`
- [PfSetSuperfetchInformation](../AD/PfSetSuperfetchInformation_function_00ADE6E8.md) at `0x00ADF2D2`
- [PfSetSuperfetchInformation](../AD/PfSetSuperfetchInformation_function_00ADE6E8.md) at `0x00ADF2D8`
- [PfSetSuperfetchInformation](../AD/PfSetSuperfetchInformation_function_00ADE6E8.md) at `0x00ADF2DE`
- [PfSetSuperfetchInformation](../AD/PfSetSuperfetchInformation_function_00ADE6E8.md) at `0x00ADF2E4`
- [PfSetSuperfetchInformation](../AD/PfSetSuperfetchInformation_function_00ADE6E8.md) at `0x00ADF2EA`
- [PfSetSuperfetchInformation](../AD/PfSetSuperfetchInformation_function_00ADE6E8.md) at `0x00ADF2F0`
- [PfSetSuperfetchInformation](../AD/PfSetSuperfetchInformation_function_00ADE6E8.md) at `0x00ADF2F6`
- [PfSetSuperfetchInformation](../AD/PfSetSuperfetchInformation_function_00ADE6E8.md) at `0x00ADF2FC`
- [PfSetSuperfetchInformation](../AD/PfSetSuperfetchInformation_function_00ADE6E8.md) at `0x00ADF302`
- [NtQueryInformationThread](../AE/NtQueryInformationThread_function_00AE3760.md) at `0x00AE5267`
- [NtSetInformationProcess](../AE/NtSetInformationProcess_function_00AE5370.md) at `0x00AE9FE7`
- [NtSetInformationProcess](../AE/NtSetInformationProcess_function_00AE5370.md) at `0x00AE9FED`
- [NtSetInformationProcess](../AE/NtSetInformationProcess_function_00AE5370.md) at `0x00AE9FF3`
- [NtCreateUserProcess](../AE/NtCreateUserProcess_function_00AEA680.md) at `0x00AEB868`
- [NtSetInformationToken](../AF/NtSetInformationToken_function_00AF0530.md) at `0x00AF1EF7`
- [NtSetInformationToken](../AF/NtSetInformationToken_function_00AF0530.md) at `0x00AF1EFD`
- [EtwpWriteUserEvent](../AF/EtwpWriteUserEvent_function_00AF2FEC.md) at `0x00AF47A1`
- [EtwpWriteUserEvent](../AF/EtwpWriteUserEvent_function_00AF2FEC.md) at `0x00AF47A7`
- [NtSetSystemInformation](../AF/NtSetSystemInformation_function_00AF4A60.md) at `0x00AF688D`
- [NtSetSystemInformation](../AF/NtSetSystemInformation_function_00AF4A60.md) at `0x00AF6893`
- [NtSetSystemInformation](../AF/NtSetSystemInformation_function_00AF4A60.md) at `0x00AF6899`
- [NtAddAtomEx](../AF/NtAddAtomEx_function_00AF7320.md) at `0x00AF74CA`
- [NtFindAtom](../AF/NtFindAtom_function_00AF7560.md) at `0x00AF770A`
- [NtManageHotPatch](../AF/NtManageHotPatch_function_00AF8660.md) at `0x00AF8DD8`
- [NtManageHotPatch](../AF/NtManageHotPatch_function_00AF8660.md) at `0x00AF8DDE`
- [sub_00B1B2E4](../B1/Unknown_function_00B1B2E4.md) at `0x00B1B318`
- [sub_00B1D74C](../B1/Unknown_function_00B1D74C.md) at `0x00B1D751`
- [sub_00B1D8AA](../B1/Unknown_function_00B1D8AA.md) at `0x00B1D8AF`
- [sub_00B1D9AC](../B1/Unknown_function_00B1D9AC.md) at `0x00B1DA35`
- [sub_00B206FE](../B2/Unknown_function_00B206FE.md) at `0x00B2071E`
- [sub_00B206FE](../B2/Unknown_function_00B206FE.md) at `0x00B207C5`
- [sub_00B27DF8](../B2/Unknown_function_00B27DF8.md) at `0x00B27E12`
- [sub_00B27DF8](../B2/Unknown_function_00B27DF8.md) at `0x00B27E70`
- [sub_00B27F7C](../B2/Unknown_function_00B27F7C.md) at `0x00B27F81`
- [sub_00B29218](../B2/Unknown_function_00B29218.md) at `0x00B29267`
- [sub_00B29218](../B2/Unknown_function_00B29218.md) at `0x00B292A3`
- [sub_00B30C5A](../B3/Unknown_function_00B30C5A.md) at `0x00B30C9D`
- [sub_00B36E7C](../B3/Unknown_function_00B36E7C.md) at `0x00B36E81`
- [sub_00B3B9F4](../B3/Unknown_function_00B3B9F4.md) at `0x00B3BA01`
- [sub_00B3BB7A](../B3/Unknown_function_00B3BB7A.md) at `0x00B3BB88`
- [sub_00B3C840](../B3/Unknown_function_00B3C840.md) at `0x00B3C8E7`
- [sub_00B3F842](../B3/Unknown_function_00B3F842.md) at `0x00B3F865`
- [sub_00B46DC6](../B4/Unknown_function_00B46DC6.md) at `0x00B46DD6`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00899FD9` → [RtlRaiseStatus](../../text/2F/RtlRaiseStatus_function_002F6A50.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00899FD0  48 83 EC 28                     sub rsp, 0x28
00899FD4  B9 02 00 00 80                  mov ecx, 0x80000002
00899FD9  E8 72 CA A5 FF                  call 0x1402f6a50
00899FDE  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExRaiseDatatypeMisalignment(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = RtlRaiseStatus((unsigned int)(0x80000002ULL), a2, a3, a4);
    return result;
}
```

## 5. (Beta) C Style

```c
void ExRaiseDatatypeMisalignment(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = RtlRaiseStatus((uint32_t)(0x80000002ULL), a2, a3, a4);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00899FD0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00899FD0[BB_00899FD0]
```
