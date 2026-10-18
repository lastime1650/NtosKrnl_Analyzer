# CmSiFreeMemory

- RVA: `0x00475D80`–`0x00475D91` (길이 `17` bytes)
- VA: `0x0000000140475D80`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `6`개 명령, `17/17` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **143**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00475D86` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [CmpReserveRollbackPacketSpace](../../page/70/CmpReserveRollbackPacketSpace_function_00703A5C.md) at `0x00703AE1`
- [KiInitializeSingleDpcRuntimeHistoryHashTable](../../page/74/KiInitializeSingleDpcRuntimeHistoryHashTable_function_00747808.md) at `0x007479A6`
- [KiInitializeSingleDpcRuntimeHistoryHashTable](../../page/74/KiInitializeSingleDpcRuntimeHistoryHashTable_function_00747808.md) at `0x007479E5`
- [KiInitializeSingleDpcRuntimeHistoryHashTable](../../page/74/KiInitializeSingleDpcRuntimeHistoryHashTable_function_00747808.md) at `0x007479F4`
- [SmDeletePartition](../../page/7A/SmDeletePartition_function_007A59C0.md) at `0x007A5A91`
- [SmPartitionCleanup](../../page/7A/SmPartitionCleanup_function_007A5C14.md) at `0x007A5C6A`
- [SmPartitionCleanup](../../page/7A/SmPartitionCleanup_function_007A5C14.md) at `0x007A5C84`
- [SmProcessListRequest](../../page/7A/SmProcessListRequest_function_007A67A8.md) at `0x007A69F0`
- [SmProcessStatsRequest](../../page/7A/SmProcessStatsRequest_function_007A6E68.md) at `0x007A7141`
- [SmProcessStatsRequest](../../page/7A/SmProcessStatsRequest_function_007A6E68.md) at `0x007A715B`
- [SmcProcessCreateRequest](../../page/7A/SmcProcessCreateRequest_function_007A764C.md) at `0x007A78B3`
- [SmKmCleanup](../../page/7A/SmKmCleanup_function_007A8108.md) at `0x007A8163`
- [SmKmKeyGenKeyDelete](../../page/7A/SmKmKeyGenKeyDelete_function_007A870C.md) at `0x007A8783`
- [SmKmKeyGenNewKey](../../page/7A/SmKmKeyGenNewKey_function_007A8990.md) at `0x007A8B74`
- [SmKmStoreFileGetExtents](../../page/7A/SmKmStoreFileGetExtents_function_007A971C.md) at `0x007A994B`
- [SmKmStoreFileWriteHeader](../../page/7A/SmKmStoreFileWriteHeader_function_007A9DB4.md) at `0x007A9F98`
- [SmHwAcceleratorCreate](../../page/7A/SmHwAcceleratorCreate_function_007AA40C.md) at `0x007AA5D2`
- [SmHwAcceleratorMgrAcquireAccelerators](../../page/7A/SmHwAcceleratorMgrAcquireAccelerators_function_007AA628.md) at `0x007AA874`
- [SmHwAcceleratorMgrAcquireAccelerators](../../page/7A/SmHwAcceleratorMgrAcquireAccelerators_function_007AA628.md) at `0x007AABDC`
- [SmHwAcceleratorMgrAcquireAccelerators](../../page/7A/SmHwAcceleratorMgrAcquireAccelerators_function_007AA628.md) at `0x007AAC1B`
- [SmHwAcceleratorMgrCreatePartitionAccelerators](../../page/7A/SmHwAcceleratorMgrCreatePartitionAccelerators_function_007AAC5C.md) at `0x007AADA7`
- [SmHwAcceleratorMgrReleaseAccelerators](../../page/7A/SmHwAcceleratorMgrReleaseAccelerators_function_007AAFD8.md) at `0x007AB084`
- [SmHwAcceleratorPartitionMgrCleanup](../../page/7A/SmHwAcceleratorPartitionMgrCleanup_function_007AB34C.md) at `0x007AB3BE`
- [SmHwAcceleratorPartitionMgrCleanup](../../page/7A/SmHwAcceleratorPartitionMgrCleanup_function_007AB34C.md) at `0x007AB44B`
- [SmcCacheCleanup](../../page/7A/SmcCacheCleanup_function_007AB7B4.md) at `0x007AB7F9`
- [SmcCacheDelete](../../page/7A/SmcCacheDelete_function_007AB84C.md) at `0x007AB87B`
- [SmcStoreCreate](../../page/7A/SmcStoreCreate_function_007ABFB4.md) at `0x007AC15F`
- [SmcStoreDelete](../../page/7A/SmcStoreDelete_function_007AC214.md) at `0x007AC397`
- [SmcStoreResize](../../page/7A/SmcStoreResize_function_007AC500.md) at `0x007AC7BA`
- [SmcStoreSlotAbort](../../page/7A/SmcStoreSlotAbort_function_007AC7DC.md) at `0x007AC881`
- [SmcStoreSlotReserve](../../page/7A/SmcStoreSlotReserve_function_007AC978.md) at `0x007ACAC0`
- [CMFCheckAccess](../../page/7D/CMFCheckAccess_function_007D28B4.md) at `0x007D2A99`
- [CmpFinishSystemHivesLoad](../../page/7D/CmpFinishSystemHivesLoad_function_007DA210.md) at `0x007DAC2C`
- [CmpFinishSystemHivesLoad](../../page/7D/CmpFinishSystemHivesLoad_function_007DA210.md) at `0x007DAC35`
- [CmpSaveBootControlSet](../../page/7D/CmpSaveBootControlSet_function_007DC744.md) at `0x007DC8AB`
- [CmpSaveBootControlSet](../../page/7D/CmpSaveBootControlSet_function_007DC744.md) at `0x007DC926`
- [CmpLoadHiveVolatile](../../page/7D/CmpLoadHiveVolatile_function_007DE5F0.md) at `0x007DEA84`
- [CmpRefreshHive](../../page/7D/CmpRefreshHive_function_007DEAD0.md) at `0x007DED99`
- [NtCompactKeys](../../page/7D/NtCompactKeys_function_007DF730.md) at `0x007DF991`
- [NtQueryOpenSubKeysEx](../../page/7E/NtQueryOpenSubKeysEx_function_007E0190.md) at `0x007E0470`
- [NtRenameKey](../../page/7E/NtRenameKey_function_007E04B0.md) at `0x007E090F`
- [CmpReadBuildVersion](../../page/7E/CmpReadBuildVersion_function_007E52F4.md) at `0x007E54D5`
- [CmpReadBuildVersion](../../page/7E/CmpReadBuildVersion_function_007E52F4.md) at `0x007E54E6`
- [CmpRecordShutdownStopTime](../../page/7E/CmpRecordShutdownStopTime_function_007E551C.md) at `0x007E5732`
- [CmpRecordShutdownStopTime](../../page/7E/CmpRecordShutdownStopTime_function_007E551C.md) at `0x007E574D`
- [CmUpdateFeatureConfiguration](../../page/7E/CmUpdateFeatureConfiguration_function_007E5C10.md) at `0x007E5E3C`
- [CmUpdateFeatureConfiguration](../../page/7E/CmUpdateFeatureConfiguration_function_007E5C10.md) at `0x007E5E49`
- [CmUpdateFeatureUsageSubscription](../../page/7E/CmUpdateFeatureUsageSubscription_function_007E5E78.md) at `0x007E5F9C`
- [CmpCreateRegistryProcessToken](../../page/7E/CmpCreateRegistryProcessToken_function_007E7F6C.md) at `0x007E80AE`
- [CmpVolumeContextCreate](../../page/7E/CmpVolumeContextCreate_function_007E86F4.md) at `0x007E8766`
- [CmReplaceKey](../../page/7E/CmReplaceKey_function_007EA1C8.md) at `0x007EA44F`
- [CmpLockKeyBodyIntoMemory](../../page/7E/CmpLockKeyBodyIntoMemory_function_007EAF10.md) at `0x007EB04E`
- [HvRecoverFlushProtocolStateFromFiles](../../page/7E/HvRecoverFlushProtocolStateFromFiles_function_007EF224.md) at `0x007EF4E2`
- [HvRecoverFlushProtocolStateFromFiles](../../page/7E/HvRecoverFlushProtocolStateFromFiles_function_007EF224.md) at `0x007EF4F0`
- [CmpDoReadTxRBigLogRecord](../../page/7F/CmpDoReadTxRBigLogRecord_function_007F0338.md) at `0x007F047D`
- [CmpRmReDoPhase](../../page/7F/CmpRmReDoPhase_function_007F0794.md) at `0x007F08EA`
- [CmpCopySyncTree](../../page/7F/CmpCopySyncTree_function_007F21A0.md) at `0x007F2226`
- [CmpMergeKeyValues](../../page/7F/CmpMergeKeyValues_function_007F2304.md) at `0x007F24EF`
- [CmpHiveCacheEntryCleanup](../../page/7F/CmpHiveCacheEntryCleanup_function_007F5B38.md) at `0x007F5C91`
- [CmpHiveCachePopulateHiveEntryThread](../../page/7F/CmpHiveCachePopulateHiveEntryThread_function_007F5FD0.md) at `0x007F63A8`
- [MiDeletePagefile](../../page/7F/MiDeletePagefile_function_007FFB88.md) at `0x007FFBD6`
- [CmSetLastWriteTimeKey](../../page/84/CmSetLastWriteTimeKey_function_00843368.md) at `0x008436C7`
- [CmpPromoteKey](../../page/84/CmpPromoteKey_function_00844388.md) at `0x008444F3`
- [NtSetValueKey](../../page/84/NtSetValueKey_function_00844EA0.md) at `0x008455F2`
- [CmSetValueKey](../../page/84/CmSetValueKey_function_008457C0.md) at `0x00845B16`
- [CmSetValueKey](../../page/84/CmSetValueKey_function_008457C0.md) at `0x00845FC8`
- [CmSetValueKey](../../page/84/CmSetValueKey_function_008457C0.md) at `0x00846676`
- [CmSetValueKey](../../page/84/CmSetValueKey_function_008457C0.md) at `0x008466B3`
- [CmDeleteValueKey](../../page/84/CmDeleteValueKey_function_008476E8.md) at `0x00847CE5`
- [CmDeleteValueKey](../../page/84/CmDeleteValueKey_function_008476E8.md) at `0x00847FD1`
- [NtDeleteValueKey](../../page/84/NtDeleteValueKey_function_00848770.md) at `0x00848BFA`
- [CmDeleteKey](../../page/84/CmDeleteKey_function_00848E5C.md) at `0x00849356`
- [CmDeleteKey](../../page/84/CmDeleteKey_function_00848E5C.md) at `0x00849364`
- [sub_0084BE3E](../../page/84/Unknown_function_0084BE3E.md) at `0x0084BE78`
- [CmpMarkIndexDirty](../../page/84/CmpMarkIndexDirty_function_0084C30C.md) at `0x0084C433`
- [sub_0084D18D](../../page/84/Unknown_function_0084D18D.md) at `0x0084D2D2`
- [sub_0084D378](../../page/84/Unknown_function_0084D378.md) at `0x0084D378`
- [sub_00855451](../../page/85/Unknown_function_00855451.md) at `0x00855454`
- [sub_00855BC3](../../page/85/Unknown_function_00855BC3.md) at `0x00855BC6`
- [CmpConstructNameWithStatus](../../page/85/CmpConstructNameWithStatus_function_008562A0.md) at `0x0085639D`
- [CmpConstructName](../../page/85/CmpConstructName_function_00856BE0.md) at `0x00856CD1`
- [CmpGetSymbolicLinkTarget](../../page/85/CmpGetSymbolicLinkTarget_function_008570A0.md) at `0x00857582`
- [sub_0085F18A](../../page/85/Unknown_function_0085F18A.md) at `0x0085F21A`
- [CmpDoParseKey](../../page/85/CmpDoParseKey_function_0085F750.md) at `0x00860477`
- [CmpDoParseKey](../../page/85/CmpDoParseKey_function_0085F750.md) at `0x00860485`
- [CmpDoParseKey](../../page/85/CmpDoParseKey_function_0085F750.md) at `0x00860496`
- [sub_0086560A](../../page/86/Unknown_function_0086560A.md) at `0x00865A19`
- [sub_0086560A](../../page/86/Unknown_function_0086560A.md) at `0x00865A48`
- [sub_00865B4C](../../page/86/Unknown_function_00865B4C.md) at `0x00865C22`
- [NtQueryKey](../../page/86/NtQueryKey_function_008676E0.md) at `0x00867F07`
- [ObpCreateHandle](../../page/86/ObpCreateHandle_function_0086B950.md) at `0x0086BC16`
- [ObpGrantAccess](../../page/86/ObpGrantAccess_function_0086F250.md) at `0x0086F437`
- [sub_0086FA65](../../page/86/Unknown_function_0086FA65.md) at `0x0086FC30`
- [sub_0086FD23](../../page/86/Unknown_function_0086FD23.md) at `0x0086FD23`
- [CmpCheckOpenAccessOnKeyBody](../../page/87/CmpCheckOpenAccessOnKeyBody_function_00870000.md) at `0x00870114`
- [CmpCheckOpenAccessOnKeyBody](../../page/87/CmpCheckOpenAccessOnKeyBody_function_00870000.md) at `0x0087032C`
- [CmpCheckOpenAccessOnKeyBody](../../page/87/CmpCheckOpenAccessOnKeyBody_function_00870000.md) at `0x008703F5`
- [CmpSecurityMethod](../../page/87/CmpSecurityMethod_function_00870CC0.md) at `0x00870FC3`
- [ObCheckObjectAccess](../../page/87/ObCheckObjectAccess_function_00872260.md) at `0x00872434`
- [CmCreateKey](../../page/87/CmCreateKey_function_00875020.md) at `0x008754DD`
- [CmLoadDifferencingKey](../../page/87/CmLoadDifferencingKey_function_00875670.md) at `0x00875F0C`
- [CmOpenKey](../../page/87/CmOpenKey_function_00876350.md) at `0x00876628`
- [CmpFreeParseContext](../../page/87/CmpFreeParseContext_function_008768E0.md) at `0x008768F3`
- [CmLoadAppKey](../../page/87/CmLoadAppKey_function_00876FFC.md) at `0x00877484`
- [CmLoadKey](../../page/87/CmLoadKey_function_008787CC.md) at `0x00878A40`
- [CmLoadKey](../../page/87/CmLoadKey_function_008787CC.md) at `0x00878A5E`
- [CmpOpenHiveFiles](../../page/87/CmpOpenHiveFiles_function_00879A68.md) at `0x00879B87`
- [CmpOpenHiveFile](../../page/87/CmpOpenHiveFile_function_0087A71C.md) at `0x0087AAF6`
- [CmpLogHiveFileInaccessible](../../page/87/CmpLogHiveFileInaccessible_function_0087AEAC.md) at `0x0087B29B`
- [CmpQueryFileSecurityDescriptor](../../page/87/CmpQueryFileSecurityDescriptor_function_0087B318.md) at `0x0087B3C3`
- [CmpReorganizeHive](../../page/87/CmpReorganizeHive_function_0087B92C.md) at `0x0087BB4B`
- [CmpParseKey](../../page/89/CmpParseKey_function_0089DDC0.md) at `0x0089E4F7`
- [IopParseDevice](../../page/89/IopParseDevice_function_0089E510.md) at `0x0089EC63`
- [IopParseDevice](../../page/89/IopParseDevice_function_0089E510.md) at `0x008A0411`
- [IopParseDevice](../../page/89/IopParseDevice_function_0089E510.md) at `0x008A0803`
- [CmpCaptureKeyValueArray](../../page/8B/CmpCaptureKeyValueArray_function_008B1074.md) at `0x008B138A`
- [CmpCaptureKeyValueArray](../../page/8B/CmpCaptureKeyValueArray_function_008B1074.md) at `0x008B1394`
- [CmpCaptureKeyValueArray](../../page/8B/CmpCaptureKeyValueArray_function_008B1074.md) at `0x008B139E`
- [NtQueryMultipleValueKey](../../page/8B/NtQueryMultipleValueKey_function_008B13B0.md) at `0x008B18F8`
- [NtQueryMultipleValueKey](../../page/8B/NtQueryMultipleValueKey_function_008B13B0.md) at `0x008B190A`
- [NtQueryMultipleValueKey](../../page/8B/NtQueryMultipleValueKey_function_008B13B0.md) at `0x008B191C`
- [CmpValueEnumStackCleanup](../../page/8B/CmpValueEnumStackCleanup_function_008B1F04.md) at `0x008B1F57`
- [CmpBounceContextCleanup](../../page/8B/CmpBounceContextCleanup_function_008B2520.md) at `0x008B255C`
- [NtQueryValueKey](../../page/8B/NtQueryValueKey_function_008B2A00.md) at `0x008B316D`
- [NtQueryValueKey](../../page/8B/NtQueryValueKey_function_008B2A00.md) at `0x008B319E`
- [CmEnumerateValueFromLayeredKey](../../page/8B/CmEnumerateValueFromLayeredKey_function_008B31FC.md) at `0x008B348D`
- [NtEnumerateValueKey](../../page/8B/NtEnumerateValueKey_function_008B3B50.md) at `0x008B451D`
- [ObCheckCreateObjectAccess](../../page/8C/ObCheckCreateObjectAccess_function_008C6340.md) at `0x008C64AD`
- [ObpCheckTraverseAccess](../../page/8C/ObpCheckTraverseAccess_function_008C6CE4.md) at `0x008C6E19`
- [CmpReportNotify](../../page/8C/CmpReportNotify_function_008C8094.md) at `0x008C80E0`
- [CmpGetSubKeyCountForKeyNodeStack](../../page/94/CmpGetSubKeyCountForKeyNodeStack_function_00945624.md) at `0x009457F6`
- [CmpSubtreeEnumeratorCleanup](../../page/94/CmpSubtreeEnumeratorCleanup_function_00945D98.md) at `0x00945DE9`
- [CmpEnumerateLayeredKey](../../page/94/CmpEnumerateLayeredKey_function_00945E58.md) at `0x00946205`
- [CmpEnumerateLayeredKey](../../page/94/CmpEnumerateLayeredKey_function_00945E58.md) at `0x00946250`
- [CmpEnumerateLayeredKey](../../page/94/CmpEnumerateLayeredKey_function_00945E58.md) at `0x00946397`
- [CmpKeyEnumStackCleanup](../../page/94/CmpKeyEnumStackCleanup_function_00946868.md) at `0x009468C5`
- [CmpCleanupKeyNodeStack](../../page/94/CmpCleanupKeyNodeStack_function_00946A5C.md) at `0x00946AAD`
- [CmpCleanupKcbStack](../../page/94/CmpCleanupKcbStack_function_009470A0.md) at `0x009470AD`
- [CmpSetSecurityDescriptorInfo](../../page/94/CmpSetSecurityDescriptorInfo_function_00949688.md) at `0x00949959`
- [CmpSetKeySecurity](../../page/94/CmpSetKeySecurity_function_0094A124.md) at `0x0094A458`
- [CmpSetKeySecurity](../../page/94/CmpSetKeySecurity_function_0094A124.md) at `0x0094A507`
- [CmpSetKeySecurity](../../page/94/CmpSetKeySecurity_function_0094A124.md) at `0x0094A566`
- [sub_0094AD01](../../page/94/Unknown_function_0094AD01.md) at `0x0094AD09`
- [sub_0094AD1C](../../page/94/Unknown_function_0094AD1C.md) at `0x0094AD1C`
- [CmpCheckAdminAccess](../../page/9A/CmpCheckAdminAccess_function_009A87A0.md) at `0x009A87FD`
- [CmpLogTransactionAbortedWithChildName](../../page/9A/CmpLogTransactionAbortedWithChildName_function_009AED70.md) at `0x009AEE82`
- [CmSetKeyFlags](../../page/9A/CmSetKeyFlags_function_009AEEA4.md) at `0x009AEFAF`
- [CmUnloadKey](../../page/9A/CmUnloadKey_function_009AF2FC.md) at `0x009AF7D0`
- [CmpPerformUnloadKey](../../page/9A/CmpPerformUnloadKey_function_009AFA28.md) at `0x009AFD33`
- [CmpCleanupRollbackPacket](../../page/9B/CmpCleanupRollbackPacket_function_009B014C.md) at `0x009B01A3`
- [CmpCleanupLightWeightUoWData](../../page/9B/CmpCleanupLightWeightUoWData_function_009B0A68.md) at `0x009B0B6B`
- [CmpProcessLightWeightUOW](../../page/9B/CmpProcessLightWeightUOW_function_009B0EAC.md) at `0x009B1000`
- [HvpViewMapFreeView](../../page/9B/HvpViewMapFreeView_function_009B6F9C.md) at `0x009B6FDF`
- [HvpPerformLogFileRecovery](../../page/9B/HvpPerformLogFileRecovery_function_009B7994.md) at `0x009B7DEF`
- [HvpPerformLogFileRecovery](../../page/9B/HvpPerformLogFileRecovery_function_009B7994.md) at `0x009B7DFC`
- [HvLoadHive](../../page/9B/HvLoadHive_function_009B8138.md) at `0x009B83C8`
- [HvLoadHive](../../page/9B/HvLoadHive_function_009B8138.md) at `0x009B861C`
- [sub_009DC508](../../page/9D/Unknown_function_009DC508.md) at `0x009DC508`
- [CmpStartSiloRegistryNamespace](../../page/9E/CmpStartSiloRegistryNamespace_function_009E85D0.md) at `0x009E865D`
- [CmpSortedValueEnumStackCleanup](../../page/A3/CmpSortedValueEnumStackCleanup_function_00A30C8C.md) at `0x00A30CE1`
- [CmpSortedValueEnumStackEntryCleanup](../../page/A3/CmpSortedValueEnumStackEntryCleanup_function_00A310A0.md) at `0x00A310E9`
- [CmpSortedValueEnumStackEntryCleanup](../../page/A3/CmpSortedValueEnumStackEntryCleanup_function_00A310A0.md) at `0x00A31101`
- [CmpSortedValueEnumStackEntryStart](../../page/A3/CmpSortedValueEnumStackEntryStart_function_00A31110.md) at `0x00A31285`
- [SmpKeyedStoreCreate](../../page/A5/SmpKeyedStoreCreate_function_00A50B64.md) at `0x00A50CAA`
- [SmProcessCreateRequest](../../page/A5/SmProcessCreateRequest_function_00A50DD0.md) at `0x00A5129A`
- [SmProcessCreateRequest](../../page/A5/SmProcessCreateRequest_function_00A50DD0.md) at `0x00A512BE`
- [SmKmStoreAdd](../../page/A5/SmKmStoreAdd_function_00A512D0.md) at `0x00A5163D`
- [CmpLightWeightCommitDeleteKeyUoW](../../page/A5/CmpLightWeightCommitDeleteKeyUoW_function_00A54610.md) at `0x00A54786`
- [CmpDoFileWrite](../../page/A6/CmpDoFileWrite_function_00A65880.md) at `0x00A65C39`
- [SmProcessDeleteNotification](../../page/A6/SmProcessDeleteNotification_function_00A686F4.md) at `0x00A68747`
- [HvpRecoverDataReadRoutine](../../page/A6/HvpRecoverDataReadRoutine_function_00A6DA60.md) at `0x00A6DB68`
- [CmpKeyEnumStackFreeResumeContext](../../page/A6/CmpKeyEnumStackFreeResumeContext_function_00A6DDD8.md) at `0x00A6DE3D`
- [CmpKeyEnumStackFreeResumeContext](../../page/A6/CmpKeyEnumStackFreeResumeContext_function_00A6DDD8.md) at `0x00A6DE62`
- [VmpFreeMemoryRanges](../../page/A7/VmpFreeMemoryRanges_function_00A75744.md) at `0x00A75773`
- [CmpAddToHiveFileList](../../page/A8/CmpAddToHiveFileList_function_00A81914.md) at `0x00A819FF`
- [CmQueryMultipleValueForLayeredKey](../../page/A8/CmQueryMultipleValueForLayeredKey_function_00A8DE80.md) at `0x00A8DF5D`
- [SmCrEncCleanup](../../page/A9/SmCrEncCleanup_function_00A90A64.md) at `0x00A90AA0`
- [SmCrEncCleanup](../../page/A9/SmCrEncCleanup_function_00A90A64.md) at `0x00A90AAE`
- [SmCrEncCleanup](../../page/A9/SmCrEncCleanup_function_00A90A64.md) at `0x00A90AB5`
- [CmpVolumeContextFree](../../page/AB/CmpVolumeContextFree_function_00AB1CF0.md) at `0x00AB1D01`
- [SmKmFileInfoCleanup](../../page/AC/SmKmFileInfoCleanup_function_00AC9A90.md) at `0x00AC9B13`
- [sub_00B3B882](../../page/B3/Unknown_function_00B3B882.md) at `0x00B3B9DF`
- [sub_00B3C780](../../page/B3/Unknown_function_00B3C780.md) at `0x00B3C82E`
- [sub_00B3D5B8](../../page/B3/Unknown_function_00B3D5B8.md) at `0x00B3D627`
- [sub_00B3F4F4](../../page/B3/Unknown_function_00B3F4F4.md) at `0x00B3F4F4`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00475D86` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00475D80  48 83 EC 28                     sub rsp, 0x28
00475D84  33 D2                           xor edx, edx
00475D86  E8 E5 CA 70 00                  call 0x140b82870
00475D8B  48 83 C4 28                     add rsp, 0x28
00475D8F  C3                              ret
00475D90  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmSiFreeMemory(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a2 = 0;
    result = ExFreePoolWithTag(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CmSiFreeMemory(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    Arg2 = 0;
    result = ExFreePoolWithTag(Arg1, Arg2, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00475D80&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00475D80[BB_00475D80]
  bb_00475D90[BB_00475D90]
```
