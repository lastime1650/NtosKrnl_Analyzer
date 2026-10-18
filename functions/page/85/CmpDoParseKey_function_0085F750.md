# CmpDoParseKey

- RVA: `0x0085F750`–`0x00861E9C` (길이 `10,060` bytes)
- VA: `0x000000014085F750`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0006B4B0`
- 디코드: `2,277`개 명령, `10,060/10,060` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **219**; 고유 호출 대상: **91**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **11**

### Outgoing calls
- `0x0085F82C` → [HvpGetCellContextInitialize](HvpGetCellContextInitialize_function_00855F10.md) (function, `0x00855F10`)
- `0x0085F843` → [CmpInitializeDelayDerefContext](../../text/42/CmpInitializeDelayDerefContext_function_0042A7F0.md) (function, `0x0042A7F0`)
- `0x0085F8BD` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0085F8CF` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0085F967` → [CmpComputeComponentHashes](CmpComputeComponentHashes_function_0085F2F0.md) (function, `0x0085F2F0`)
- `0x0085FA0E` → [CmpLockRegistry](../../pagecmrc/BC/CmpLockRegistry_function_00BC9B34.md) (function, `0x00BC9B34`)
- `0x0085FA68` → [CmpPerformCompleteKcbCacheLookup](../84/CmpPerformCompleteKcbCacheLookup_function_0084FD20.md) (function, `0x0084FD20`)
- `0x0085FAC1` → [CmpUnlockHashEntryByKcb](../86/CmpUnlockHashEntryByKcb_function_00864370.md) (function, `0x00864370`)
- `0x0085FACE` → [CmpLockKcbShared](../../pagecmrc/BC/CmpLockKcbShared_function_00BC9A1C.md) (function, `0x00BC9A1C`)
- `0x0085FAE6` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x0085FB1F` → [CmpIsKcbInvolvedInVirtualization](CmpIsKcbInvolvedInVirtualization_function_0085F160.md) (function, `0x0085F160`)
- `0x0085FB3B` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (function, `0x00BC92C0`)
- `0x0085FB7B` → [CmpLockHiveListShared](../84/CmpLockHiveListShared_function_0084E3C8.md) (function, `0x0084E3C8`)
- `0x0085FC18` → [CmpLockRegistry](../../pagecmrc/BC/CmpLockRegistry_function_00BC9B34.md) (function, `0x00BC9B34`)
- `0x0085FC20` → [CmpDereferenceKeyControlBlock](CmpDereferenceKeyControlBlock_function_00851310.md) (function, `0x00851310`)
- `0x0085FC28` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x0085FC51` → [CmpLockRegistry](../../pagecmrc/BC/CmpLockRegistry_function_00BC9B34.md) (function, `0x00BC9B34`)
- `0x0085FC8C` → [RtlPrefixUnicodeString](../8F/RtlPrefixUnicodeString_function_008F4F70.md) (function, `0x008F4F70`)
- `0x0085FD24` → [CmpComputeComponentHashes](CmpComputeComponentHashes_function_0085F2F0.md) (function, `0x0085F2F0`)
- `0x0085FD85` → [CmpIsSystemEntity](../8B/CmpIsSystemEntity_function_008B4E90.md) (function, `0x008B4E90`)
- `0x0085FDAC` → [CmpLockHashEntrySharedByKcb](../9F/CmpLockHashEntrySharedByKcb_function_009F52D4.md) (function, `0x009F52D4`)
- `0x0085FDC1` → [CmpLockKcbShared](../../pagecmrc/BC/CmpLockKcbShared_function_00BC9A1C.md) (function, `0x00BC9A1C`)
- `0x0085FDCB` → [CmpIsKeyDeleted](../84/CmpIsKeyDeleted_function_0084BDB0.md) (function, `0x0084BDB0`)
- `0x0085FDE9` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (function, `0x00BC92C0`)
- `0x0085FE07` → [CmpUnlockHiveList](../84/CmpUnlockHiveList_function_0084E424.md) (function, `0x0084E424`)
- `0x0085FE22` → [CmpTransSilentIgnore](../../text/44/CmpTransSilentIgnore_function_00443B40.md) (function, `0x00443B40`)
- `0x0085FE5D` → [CmpTransReferenceTransaction](../87/CmpTransReferenceTransaction_function_00873434.md) (function, `0x00873434`)
- `0x0085FE89` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x0085FF33` → [CmpLockKcbStackShared](../94/CmpLockKcbStackShared_function_00948000.md) (function, `0x00948000`)
- `0x0085FF96` → [CmpIsKeyStackSymlink](../9A/CmpIsKeyStackSymlink_function_009A8CE0.md) (function, `0x009A8CE0`)
- `0x0085FFA6` → [CmpUnlockKcbStack](../84/CmpUnlockKcbStack_function_00848460.md) (function, `0x00848460`)
- `0x00860028` → [CmpWalkOneLevel](CmpWalkOneLevel_function_00852BA0.md) (function, `0x00852BA0`)
- `0x00860066` → [CmpDereferenceKeyControlBlockUnsafe](../99/CmpDereferenceKeyControlBlockUnsafe_function_0099F960.md) (function, `0x0099F960`)
- `0x008600D3` → [CmpRecordParseFailure](CmpRecordParseFailure_function_00851280.md) (function, `0x00851280`)
- `0x008600DD` → [CmpUnlockKcbStack](../84/CmpUnlockKcbStack_function_00848460.md) (function, `0x00848460`)
- `0x00860129` → [CmpCheckOpenAccessOnKeyBody](../87/CmpCheckOpenAccessOnKeyBody_function_00870000.md) (function, `0x00870000`)
- `0x00860153` → [CmpRecordParseFailure](CmpRecordParseFailure_function_00851280.md) (function, `0x00851280`)
- `0x008601BB` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (function, `0x00BC92C0`)
- `0x008601FC` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (function, `0x00BC92C0`)
- `0x0086026D` → [CmpGetComponentNameAtIndex](../9A/CmpGetComponentNameAtIndex_function_009A7A50.md) (function, `0x009A7A50`)
- `0x00860281` → [CmpWaitForHiveMount](../AC/CmpWaitForHiveMount_function_00ACB524.md) (function, `0x00ACB524`)
- `0x008602A6` → [CmpGetComponentNameAtIndex](../9A/CmpGetComponentNameAtIndex_function_009A7A50.md) (function, `0x009A7A50`)
- `0x008602BA` → [CmpWaitForHiveMount](../AC/CmpWaitForHiveMount_function_00ACB524.md) (function, `0x00ACB524`)
- `0x00860331` → [CmpGetSymbolicLinkTarget](CmpGetSymbolicLinkTarget_function_008570A0.md) (function, `0x008570A0`)
- `0x008603AA` → [CmpUnlockHiveList](../84/CmpUnlockHiveList_function_0084E424.md) (function, `0x0084E424`)
- `0x008603AF` → [PsIsCurrentThreadInServerSilo](../../text/43/PsIsCurrentThreadInServerSilo_function_004362E0.md) (function, `0x004362E0`)
- `0x0086041E` → [tlgWriteAgg](../../text/2F/tlgWriteAgg_function_002F0F7C.md) (function, `0x002F0F7C`)
- `0x00860477` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (function, `0x00475D80`)
- `0x00860485` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (function, `0x00475D80`)
- `0x00860496` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (function, `0x00475D80`)
- `0x008604B0` → [CmpDereferenceKeyControlBlock](CmpDereferenceKeyControlBlock_function_00851310.md) (function, `0x00851310`)
- `0x008604BD` → [CmpDereferenceKeyControlBlock](CmpDereferenceKeyControlBlock_function_00851310.md) (function, `0x00851310`)
- `0x00860516` → [CmpAttachToRegistryProcess](../../pagecmrc/BC/CmpAttachToRegistryProcess_function_00BC98E0.md) (function, `0x00BC98E0`)
- `0x0086052D` → [CmpLockHashEntryByIndexExclusive](../7F/CmpLockHashEntryByIndexExclusive_function_007F1290.md) (function, `0x007F1290`)
- `0x00860550` → [CmpLockKcbExclusive](../86/CmpLockKcbExclusive_function_00861EB0.md) (function, `0x00861EB0`)
- `0x0086055E` → [CmpRemoveFromDelayedClose](../86/CmpRemoveFromDelayedClose_function_00862350.md) (function, `0x00862350`)
- `0x0086056A` → [CmpCleanUpKcbCacheWithLock](../86/CmpCleanUpKcbCacheWithLock_function_00861F20.md) (function, `0x00861F20`)
- `0x00860572` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (function, `0x00BC92C0`)
- `0x0086057E` → [CmpUnlockHashEntryByIndex](../86/CmpUnlockHashEntryByIndex_function_00862460.md) (function, `0x00862460`)
- `0x0086059D` → [CmpSyncKcbCacheForHive](../7E/CmpSyncKcbCacheForHive_function_007EBD50.md) (function, `0x007EBD50`)
- `0x008605C4` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (function, `0x00BC92C0`)
- `0x008605D1` → [CmpUnlockHashEntryByKcb](../86/CmpUnlockHashEntryByKcb_function_00864370.md) (function, `0x00864370`)
- `0x008605F0` → [CmListGetNextElement](../../pagecmrc/BC/CmListGetNextElement_function_00BC9940.md) (function, `0x00BC9940`)
- `0x0086060B` → [CmEqualTrans](../84/CmEqualTrans_function_0084BF60.md) (function, `0x0084BF60`)
- `0x0086063B` → [CmpDereferenceKeyControlBlock](CmpDereferenceKeyControlBlock_function_00851310.md) (function, `0x00851310`)
- `0x00860643` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x008606C2` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (function, `0x00BC92C0`)
- `0x008606D3` → [CmpDereferenceKeyControlBlock](CmpDereferenceKeyControlBlock_function_00851310.md) (function, `0x00851310`)
- `0x008606EE` → [CmpCleanupPathInfo](CmpCleanupPathInfo_function_0085F6D0.md) (function, `0x0085F6D0`)
- `0x008606FE` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0086073D` → [CmpPopulateKcbStack](../84/CmpPopulateKcbStack_function_00842550.md) (function, `0x00842550`)
- `0x0086075D` → [CmpLockKcbShared](../../pagecmrc/BC/CmpLockKcbShared_function_00BC9A1C.md) (function, `0x00BC9A1C`)
- `0x00860770` → [CmpLockKcbStackShared](../94/CmpLockKcbStackShared_function_00948000.md) (function, `0x00948000`)
- `0x0086077D` → [CmpLockKcbStackShared](../94/CmpLockKcbStackShared_function_00948000.md) (function, `0x00948000`)
- `0x0086078A` → [CmpIsKeyDeletedForKeyBody](../../pagecmrc/BC/CmpIsKeyDeletedForKeyBody_function_00BC9480.md) (function, `0x00BC9480`)
- `0x008607C8` → [CmRmIsKcbStackVisible](../9A/CmRmIsKcbStackVisible_function_009A8470.md) (function, `0x009A8470`)
- `0x008607F3` → [CmpIsKeyStackDeleted](../84/CmpIsKeyStackDeleted_function_008426E0.md) (function, `0x008426E0`)
- `0x00860803` → [CmpIsKeyStackSymlink](../9A/CmpIsKeyStackSymlink_function_009A8CE0.md) (function, `0x009A8CE0`)
- `0x00860863` → [CmpDoWritethroughReparse](../94/CmpDoWritethroughReparse_function_0094AC70.md) (function, `0x0094AC70`)
- `0x0086089E` → [CmpVEExecuteOpenLogic](CmpVEExecuteOpenLogic_function_00854D90.md) (function, `0x00854D90`)
- `0x008608E1` → [CmpCreateKeyBody](../8C/CmpCreateKeyBody_function_008C3C10.md) (function, `0x008C3C10`)
- `0x0086097D` → [CmpReferenceKeyControlBlockUnsafe](../87/CmpReferenceKeyControlBlockUnsafe_function_00874DA0.md) (function, `0x00874DA0`)
- `0x008609ED` → [CmpLogUnsupportedOperation](../9A/CmpLogUnsupportedOperation_function_009AEA40.md) (function, `0x009AEA40`)
- `0x008609F2` → [PsIsCurrentThreadInServerSilo](../../text/43/PsIsCurrentThreadInServerSilo_function_004362E0.md) (function, `0x004362E0`)
- `0x00860A1A` → [CmpRecordParseFailure](CmpRecordParseFailure_function_00851280.md) (function, `0x00851280`)
- `0x00860A2D` → [CmpUnlockHashEntryByKcb](../86/CmpUnlockHashEntryByKcb_function_00864370.md) (function, `0x00864370`)
- `0x00860A5E` → [CmpUnlockHashEntryByKcb](../86/CmpUnlockHashEntryByKcb_function_00864370.md) (function, `0x00864370`)
- `0x00860A68` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x00860A93` → [CmpTransSearchAddLightWeightTrans](../87/CmpTransSearchAddLightWeightTrans_function_00873494.md) (function, `0x00873494`)
- `0x00860A9C` → [CmpLockRegistry](../../pagecmrc/BC/CmpLockRegistry_function_00BC9B34.md) (function, `0x00BC9B34`)
- `0x00860AC1` → [CmpRecordParseFailure](CmpRecordParseFailure_function_00851280.md) (function, `0x00851280`)
- `0x00860AF1` → [CmpTransSearchAddTransFromRm](../A6/CmpTransSearchAddTransFromRm_function_00A6023C.md) (function, `0x00A6023C`)
- `0x00860B0D` → [CmpDetachFromRegistryProcess](../../pagecmrc/BC/CmpDetachFromRegistryProcess_function_00BC9920.md) (function, `0x00BC9920`)
- `0x00860B24` → [CmpDrainDelayDerefContext](../../text/41/CmpDrainDelayDerefContext_function_0041B9A0.md) (function, `0x0041B9A0`)
- `0x00860B30` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x00860B4B` → [CmpDetachFromRegistryProcess](../../pagecmrc/BC/CmpDetachFromRegistryProcess_function_00BC9920.md) (function, `0x00BC9920`)
- `0x00860B60` → [CmpCleanupPathInfo](CmpCleanupPathInfo_function_0085F6D0.md) (function, `0x0085F6D0`)
- `0x00860B72` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00860B7C` → [CmpLockHashEntrySharedByKcb](../9F/CmpLockHashEntrySharedByKcb_function_009F52D4.md) (function, `0x009F52D4`)
- `0x00860B8F` → [CmpCheckExeOwnerForPca](../9A/CmpCheckExeOwnerForPca_function_009A343C.md) (function, `0x009A343C`)
- `0x00860B9E` → [CmpPublishEventForPcaResolver](../A6/CmpPublishEventForPcaResolver_function_00A66AC0.md) (function, `0x00A66AC0`)
- `0x00860BAB` → [CmpFreePoolWithTag](../../text/44/CmpFreePoolWithTag_function_004489E0.md) (function, `0x004489E0`)
- `0x00860BB2` → [CmpLockRegistryExclusive](../84/CmpLockRegistryExclusive_function_0084F9B4.md) (function, `0x0084F9B4`)
- `0x00860BE0` → [CmpUnlockKcbStack](../84/CmpUnlockKcbStack_function_00848460.md) (function, `0x00848460`)
- `0x00860BEC` → [CmpUnlockKcbStack](../84/CmpUnlockKcbStack_function_00848460.md) (function, `0x00848460`)
- `0x00860BF4` → [CmpLockKcbStackTopExclusiveRestShared](../84/CmpLockKcbStackTopExclusiveRestShared_function_00846B04.md) (function, `0x00846B04`)
- `0x00860BFC` → [CmpLockKcbStackTopExclusiveRestShared](../84/CmpLockKcbStackTopExclusiveRestShared_function_00846B04.md) (function, `0x00846B04`)
- `0x00860C08` → [CmpIsKeyStackDeleted](../84/CmpIsKeyStackDeleted_function_008426E0.md) (function, `0x008426E0`)
- `0x00860C30` → [CmpGetComponentNameAtIndex](../9A/CmpGetComponentNameAtIndex_function_009A7A50.md) (function, `0x009A7A50`)
- `0x00860C98` → [CmpCreateKeyBody](../8C/CmpCreateKeyBody_function_008C3C10.md) (function, `0x008C3C10`)
- `0x00860CAF` → [CmpIsKeyStackDeleted](../84/CmpIsKeyStackDeleted_function_008426E0.md) (function, `0x008426E0`)
- `0x00860CEC` → [CmpCreateChild](../94/CmpCreateChild_function_0094817C.md) (function, `0x0094817C`)
- `0x00860D8C` → [CmpRecordParseFailure](CmpRecordParseFailure_function_00851280.md) (function, `0x00851280`)
- `0x00860DA3` → [CmpDereferenceKeyControlBlockUnsafe](../99/CmpDereferenceKeyControlBlockUnsafe_function_0099F960.md) (function, `0x0099F960`)
- `0x00860DB3` → [CmpUnlockHashEntryByKcb](../86/CmpUnlockHashEntryByKcb_function_00864370.md) (function, `0x00864370`)
- `0x00860DC3` → [CmpUnlockHashEntry](../86/CmpUnlockHashEntry_function_00864460.md) (function, `0x00864460`)
- `0x00860DD3` → [CmpLockRegistryExclusive](../84/CmpLockRegistryExclusive_function_0084F9B4.md) (function, `0x0084F9B4`)
- `0x00860E0D` → [CmpAttachToRegistryProcess](../../pagecmrc/BC/CmpAttachToRegistryProcess_function_00BC98E0.md) (function, `0x00BC98E0`)
- `0x00860E44` → [CmpVEExecuteRealStoreParseLogic](../84/CmpVEExecuteRealStoreParseLogic_function_0084CCD4.md) (function, `0x0084CCD4`)
- `0x00860E78` → [CmpSetKcbAtLayerHeight](../99/CmpSetKcbAtLayerHeight_function_0099E730.md) (function, `0x0099E730`)
- `0x00860EBA` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (function, `0x00BC92C0`)
- `0x00860F11` → [CmpGetSymbolicLinkTarget](CmpGetSymbolicLinkTarget_function_008570A0.md) (function, `0x008570A0`)
- `0x00860F58` → [CmpRecordParseFailure](CmpRecordParseFailure_function_00851280.md) (function, `0x00851280`)
- `0x00860F8C` → [CmpIsKeyStackDeleted](../84/CmpIsKeyStackDeleted_function_008426E0.md) (function, `0x008426E0`)
- `0x00860F9F` → [CmRmIsKcbStackVisible](../9A/CmRmIsKcbStackVisible_function_009A8470.md) (function, `0x009A8470`)
- `0x00860FF6` → [CmpRecordParseFailure](CmpRecordParseFailure_function_00851280.md) (function, `0x00851280`)
- `0x00861003` → [CmpUnlockKcbStack](../84/CmpUnlockKcbStack_function_00848460.md) (function, `0x00848460`)
- `0x00861022` → [CmpDelayDerefKeyControlBlock](../84/CmpDelayDerefKeyControlBlock_function_0084FA50.md) (function, `0x0084FA50`)
- `0x0086104B` → [CmpAllocatePool](../../text/3C/CmpAllocatePool_function_003CD504.md) (function, `0x003CD504`)
- `0x00861074` → [CmpAllocatePool](../../text/3C/CmpAllocatePool_function_003CD504.md) (function, `0x003CD504`)
- `0x008610A0` → [CmpRecordParseFailure](CmpRecordParseFailure_function_00851280.md) (function, `0x00851280`)
- `0x008610AE` → [CmpUnlockKcbStack](../84/CmpUnlockKcbStack_function_00848460.md) (function, `0x00848460`)
- `0x008610D8` → [CmpRecordParseFailure](CmpRecordParseFailure_function_00851280.md) (function, `0x00851280`)
- `0x008610E2` → [CmpUnlockKcbStack](../84/CmpUnlockKcbStack_function_00848460.md) (function, `0x00848460`)
- `0x008610EF` → [CmpVEExecuteVirtualStoreParseLogic](../A7/CmpVEExecuteVirtualStoreParseLogic_function_00A76A20.md) (function, `0x00A76A20`)
- `0x00861155` → [CmpGetComponentNameAtIndex](../9A/CmpGetComponentNameAtIndex_function_009A7A50.md) (function, `0x009A7A50`)
- `0x00861169` → [CmpWaitForHiveMount](../AC/CmpWaitForHiveMount_function_00ACB524.md) (function, `0x00ACB524`)
- `0x00861192` → [CmpRecordParseFailure](CmpRecordParseFailure_function_00851280.md) (function, `0x00851280`)
- `0x008611B9` → [CmpGetComponentNameAtIndex](../9A/CmpGetComponentNameAtIndex_function_009A7A50.md) (function, `0x009A7A50`)
- `0x008611E4` → [CmpDoWritethroughReparse](../94/CmpDoWritethroughReparse_function_0094AC70.md) (function, `0x0094AC70`)
- `0x00861224` → [CmpCreateKeyBody](../8C/CmpCreateKeyBody_function_008C3C10.md) (function, `0x008C3C10`)
- `0x0086125A` → [CmpUnlockKcbStack](../84/CmpUnlockKcbStack_function_00848460.md) (function, `0x00848460`)
- `0x00861262` → [CmpUnlockKcbStack](../84/CmpUnlockKcbStack_function_00848460.md) (function, `0x00848460`)
- `0x0086126A` → [CmpLockKcbStackTopExclusiveRestShared](../84/CmpLockKcbStackTopExclusiveRestShared_function_00846B04.md) (function, `0x00846B04`)
- `0x00861275` → [CmpLockKcbStackTopExclusiveRestShared](../84/CmpLockKcbStackTopExclusiveRestShared_function_00846B04.md) (function, `0x00846B04`)
- `0x00861281` → [CmRmIsKcbStackVisible](../9A/CmRmIsKcbStackVisible_function_009A8470.md) (function, `0x009A8470`)
- `0x008612A3` → [CmpIsKeyStackDeleted](../84/CmpIsKeyStackDeleted_function_008426E0.md) (function, `0x008426E0`)
- `0x008612B7` → [CmpIsKeyStackDeleted](../84/CmpIsKeyStackDeleted_function_008426E0.md) (function, `0x008426E0`)
- `0x008612CB` → [CmRmIsKcbStackVisible](../9A/CmRmIsKcbStackVisible_function_009A8470.md) (function, `0x009A8470`)
- `0x00861329` → [CmpVEExecuteCreateLogic](../A2/CmpVEExecuteCreateLogic_function_00A26F28.md) (function, `0x00A26F28`)
- `0x00861397` → [CmpCheckCreateAccessOnKcbStack](../8C/CmpCheckCreateAccessOnKcbStack_function_008C7010.md) (function, `0x008C7010`)
- `0x008613B8` → [CmpEnlistKeyBody](../84/CmpEnlistKeyBody_function_008425C0.md) (function, `0x008425C0`)
- `0x00861403` → [CmpCreateChild](../94/CmpCreateChild_function_0094817C.md) (function, `0x0094817C`)
- `0x00861453` → [CmpTransSearchAddTransFromRm](../A6/CmpTransSearchAddTransFromRm_function_00A6023C.md) (function, `0x00A6023C`)
- `0x0086145D` → [CmpUnlockKcbStack](../84/CmpUnlockKcbStack_function_00848460.md) (function, `0x00848460`)
- `0x00861466` → [CmpUnlockKcbStack](../84/CmpUnlockKcbStack_function_00848460.md) (function, `0x00848460`)
- `0x00861482` → [CmpTryToLockHashEntryExclusive](../A6/CmpTryToLockHashEntryExclusive_function_00A68030.md) (function, `0x00A68030`)
- `0x0086149A` → [CmpLockKcbStackTopExclusiveRestShared](../84/CmpLockKcbStackTopExclusiveRestShared_function_00846B04.md) (function, `0x00846B04`)
- `0x008614A2` → [CmpLockKcbStackTopExclusiveRestShared](../84/CmpLockKcbStackTopExclusiveRestShared_function_00846B04.md) (function, `0x00846B04`)
- `0x008614B6` → [CmpGetComponentNameAtIndex](../9A/CmpGetComponentNameAtIndex_function_009A7A50.md) (function, `0x009A7A50`)
- `0x008614C1` → [CmpGetComponentHashAtIndex](../9A/CmpGetComponentHashAtIndex_function_009A2C80.md) (function, `0x009A2C80`)
- `0x008614CE` → [CmpIsKeyDeletedForKeyBody](../../pagecmrc/BC/CmpIsKeyDeletedForKeyBody_function_00BC9480.md) (function, `0x00BC9480`)
- `0x008614E2` → [CmpIsKeyStackDeleted](../84/CmpIsKeyStackDeleted_function_008426E0.md) (function, `0x008426E0`)
- `0x008614F6` → [CmpIsKeyStackDeleted](../84/CmpIsKeyStackDeleted_function_008426E0.md) (function, `0x008426E0`)
- `0x00861565` → [CmpCreateHiveRootCell](../AB/CmpCreateHiveRootCell_function_00ABF568.md) (function, `0x00ABF568`)
- `0x008615B8` → [CmpCreateKeyControlBlock](CmpCreateKeyControlBlock_function_00851DB0.md) (function, `0x00851DB0`)
- `0x008615E6` → [CmpDereferenceKeyControlBlockUnsafe](../99/CmpDereferenceKeyControlBlockUnsafe_function_0099F960.md) (function, `0x0099F960`)
- `0x008615EE` → [CmpUnlockHashEntryByKcb](../86/CmpUnlockHashEntryByKcb_function_00864370.md) (function, `0x00864370`)
- `0x00861603` → [CmpStartKcbStackForTopLayerKcb](../84/CmpStartKcbStackForTopLayerKcb_function_00848390.md) (function, `0x00848390`)
- `0x00861623` → [CmpLockKcbStackTopExclusiveRestShared](../84/CmpLockKcbStackTopExclusiveRestShared_function_00846B04.md) (function, `0x00846B04`)
- `0x00861672` → [CmpCreateKeyBody](../8C/CmpCreateKeyBody_function_008C3C10.md) (function, `0x008C3C10`)
- `0x00861687` → [HvLockHiveFlusherShared](../84/HvLockHiveFlusherShared_function_0084F95C.md) (function, `0x0084F95C`)
- `0x00861694` → [HvLockHiveFlusherExclusive](../../pagecmrc/BC/HvLockHiveFlusherExclusive_function_00BC9C50.md) (function, `0x00BC9C50`)
- `0x008616B0` → [HvpMarkCellDirty](HvpMarkCellDirty_function_00858080.md) (function, `0x00858080`)
- `0x008616F2` → [CmpCreateChild](../94/CmpCreateChild_function_0094817C.md) (function, `0x0094817C`)
- `0x00861719` → [CmpGetKeyNodeForKcb](CmpGetKeyNodeForKcb_function_00856480.md) (function, `0x00856480`)
- `0x00861737` → [CmpRebuildKcbCacheFromNode](../84/CmpRebuildKcbCacheFromNode_function_0084C5A8.md) (function, `0x0084C5A8`)
- `0x00861751` → [HvpReleaseCellPaged](HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x00861764` → [HvUnlockHiveFlusherExclusive](../../pagecmrc/BC/HvUnlockHiveFlusherExclusive_function_00BC9C34.md) (function, `0x00BC9C34`)
- `0x0086176D` → [HvUnlockHiveFlusherShared](../84/HvUnlockHiveFlusherShared_function_00848738.md) (function, `0x00848738`)
- `0x0086177A` → [CmpReferenceKeyControlBlockUnsafe](../87/CmpReferenceKeyControlBlockUnsafe_function_00874DA0.md) (function, `0x00874DA0`)
- `0x00861789` → [CmpUnlockHashEntry](../86/CmpUnlockHashEntry_function_00864460.md) (function, `0x00864460`)
- `0x008617C6` → [CmpRecordParseFailure](CmpRecordParseFailure_function_00851280.md) (function, `0x00851280`)
- `0x00861824` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x0086183B` → [HvpReleaseCellFlat](HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00861860` → [CmpRecordParseFailure](CmpRecordParseFailure_function_00851280.md) (function, `0x00851280`)
- `0x008618AD` → [CmpRecordParseFailure](CmpRecordParseFailure_function_00851280.md) (function, `0x00851280`)
- `0x008618D0` → [CmpRecordParseFailure](CmpRecordParseFailure_function_00851280.md) (function, `0x00851280`)
- `0x00861901` → [CmpRecordParseFailure](CmpRecordParseFailure_function_00851280.md) (function, `0x00851280`)
- `0x0086192E` → [CmpRecordParseFailure](CmpRecordParseFailure_function_00851280.md) (function, `0x00851280`)
- `0x00861940` → [CmpRecordParseFailure](CmpRecordParseFailure_function_00851280.md) (function, `0x00851280`)
- `0x008619FE` → [CmpRecordParseFailure](CmpRecordParseFailure_function_00851280.md) (function, `0x00851280`)
- `0x00861A4D` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (function, `0x00BC92C0`)
- `0x00861A5B` → [CmpLockKcbShared](../../pagecmrc/BC/CmpLockKcbShared_function_00BC9A1C.md) (function, `0x00BC9A1C`)
- `0x00861ACD` → [CmpAttachToRegistryProcess](../../pagecmrc/BC/CmpAttachToRegistryProcess_function_00BC98E0.md) (function, `0x00BC98E0`)
- `0x00861AF1` → [CmpUpdateHiveRootCellFlags](../A6/CmpUpdateHiveRootCellFlags_function_00A6B124.md) (function, `0x00A6B124`)
- `0x00861B36` → [CmpRecordParseFailure](CmpRecordParseFailure_function_00851280.md) (function, `0x00851280`)
- `0x00861B42` → [CmpUnlockKcbStack](../84/CmpUnlockKcbStack_function_00848460.md) (function, `0x00848460`)
- `0x00861B59` → [CmpRecordParseFailure](CmpRecordParseFailure_function_00851280.md) (function, `0x00851280`)
- `0x00861B66` → [HvUnlockHiveFlusherExclusive](../../pagecmrc/BC/HvUnlockHiveFlusherExclusive_function_00BC9C34.md) (function, `0x00BC9C34`)
- `0x00861B6F` → [HvUnlockHiveFlusherShared](../84/HvUnlockHiveFlusherShared_function_00848738.md) (function, `0x00848738`)
- `0x00861B8A` → [HvResetDirtyData](../9B/HvResetDirtyData_function_009B3D84.md) (function, `0x009B3D84`)
- `0x00861BF3` → [CmpAttachToRegistryProcess](../../pagecmrc/BC/CmpAttachToRegistryProcess_function_00BC98E0.md) (function, `0x00BC98E0`)
- `0x00861C25` → [CmpRecordParseFailure](CmpRecordParseFailure_function_00851280.md) (function, `0x00851280`)
- `0x00861C4C` → [CmpRecordParseFailure](CmpRecordParseFailure_function_00851280.md) (function, `0x00851280`)
- `0x00861C76` → [CmpRecordParseFailure](CmpRecordParseFailure_function_00851280.md) (function, `0x00851280`)
- `0x00861C92` → [CmpRecordParseFailure](CmpRecordParseFailure_function_00851280.md) (function, `0x00851280`)
- `0x00861CAE` → [CmpRecordParseFailure](CmpRecordParseFailure_function_00851280.md) (function, `0x00851280`)
- `0x00861CCA` → [CmpRecordParseFailure](CmpRecordParseFailure_function_00851280.md) (function, `0x00851280`)
- `0x00861CF1` → [CmpRecordParseFailure](CmpRecordParseFailure_function_00851280.md) (function, `0x00851280`)
- `0x00861D00` → [CmpIsKeyStackSymlink](../9A/CmpIsKeyStackSymlink_function_009A8CE0.md) (function, `0x009A8CE0`)
- `0x00861D3D` → [CmpRecordParseFailure](CmpRecordParseFailure_function_00851280.md) (function, `0x00851280`)
- `0x00861D64` → [CmpUnlockHashEntryByKcb](../86/CmpUnlockHashEntryByKcb_function_00864370.md) (function, `0x00864370`)
- `0x00861D7E` → [CmpRecordParseFailure](CmpRecordParseFailure_function_00851280.md) (function, `0x00851280`)
- `0x00861E26` → [CmpAttachToRegistryProcess](../../pagecmrc/BC/CmpAttachToRegistryProcess_function_00BC98E0.md) (function, `0x00BC98E0`)
- `0x00861E51` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (function, `0x00BC92C0`)
- `0x00861E5E` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (function, `0x00BC92C0`)
- `0x00861E68` → [CmpUnlockHashEntryByIndex](../86/CmpUnlockHashEntryByIndex_function_00862460.md) (function, `0x00862460`)
- `0x00861E7C` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [CmpParseKey](../89/CmpParseKey_function_0089DDC0.md) at `0x0089E0A4`

### Static image references
- `0x0085F76F` → RVA `0x00E0A740` (`.data`; read)
- `0x0085F926` → RVA `0x00FD9B68` (`PAGEDATA`; read)
- `0x0085FAF3` → RVA `0x00E0ECA0` (`.data`; read)
- `0x008600AB` → RVA `0x00EEFB44` (`.data`; read)
- `0x0086022B` → RVA `0x00EEFB48` (`.data`; read)
- `0x00860240` → RVA `0x00FD9A90` (`PAGEDATA`; read)
- `0x008603B8` → RVA `0x00E09F58` (`.data`; read)
- `0x008603CD` → RVA `0x00E09F68` (`.data`; read)
- `0x008603F3` → RVA `0x00056328` (`.rdata`; read)
- `0x008617DE` → RVA `0x00E09F70` (`.data`; read)
- `0x0086180B` → RVA `0x0005637A` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **56**
  - `0x0085F843` → [CmpInitializeDelayDerefContext](../../text/42/CmpInitializeDelayDerefContext_function_0042A7F0.md) (`PAGE` → `.text`)
  - `0x0085F8BD` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x0085F8CF` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x0085FA0E` → [CmpLockRegistry](../../pagecmrc/BC/CmpLockRegistry_function_00BC9B34.md) (`PAGE` → `PAGECMRC`)
  - `0x0085FACE` → [CmpLockKcbShared](../../pagecmrc/BC/CmpLockKcbShared_function_00BC9A1C.md) (`PAGE` → `PAGECMRC`)
  - `0x0085FAE6` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x0085FB3B` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (`PAGE` → `PAGECMRC`)
  - `0x0085FC18` → [CmpLockRegistry](../../pagecmrc/BC/CmpLockRegistry_function_00BC9B34.md) (`PAGE` → `PAGECMRC`)
  - `0x0085FC28` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x0085FC51` → [CmpLockRegistry](../../pagecmrc/BC/CmpLockRegistry_function_00BC9B34.md) (`PAGE` → `PAGECMRC`)
  - `0x0085FDC1` → [CmpLockKcbShared](../../pagecmrc/BC/CmpLockKcbShared_function_00BC9A1C.md) (`PAGE` → `PAGECMRC`)
  - `0x0085FDE9` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (`PAGE` → `PAGECMRC`)
  - `0x0085FE22` → [CmpTransSilentIgnore](../../text/44/CmpTransSilentIgnore_function_00443B40.md) (`PAGE` → `.text`)
  - `0x0085FE89` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008601BB` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (`PAGE` → `PAGECMRC`)
  - `0x008601FC` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (`PAGE` → `PAGECMRC`)
  - `0x008603AF` → [PsIsCurrentThreadInServerSilo](../../text/43/PsIsCurrentThreadInServerSilo_function_004362E0.md) (`PAGE` → `.text`)
  - `0x0086041E` → [tlgWriteAgg](../../text/2F/tlgWriteAgg_function_002F0F7C.md) (`PAGE` → `.text`)
  - `0x00860477` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (`PAGE` → `.text`)
  - `0x00860485` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (`PAGE` → `.text`)
  - `0x00860496` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (`PAGE` → `.text`)
  - `0x00860516` → [CmpAttachToRegistryProcess](../../pagecmrc/BC/CmpAttachToRegistryProcess_function_00BC98E0.md) (`PAGE` → `PAGECMRC`)
  - `0x00860572` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (`PAGE` → `PAGECMRC`)
  - `0x008605C4` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (`PAGE` → `PAGECMRC`)
  - `0x008605F0` → [CmListGetNextElement](../../pagecmrc/BC/CmListGetNextElement_function_00BC9940.md) (`PAGE` → `PAGECMRC`)
  - `0x00860643` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x008606C2` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (`PAGE` → `PAGECMRC`)
  - `0x008606FE` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x0086075D` → [CmpLockKcbShared](../../pagecmrc/BC/CmpLockKcbShared_function_00BC9A1C.md) (`PAGE` → `PAGECMRC`)
  - `0x0086078A` → [CmpIsKeyDeletedForKeyBody](../../pagecmrc/BC/CmpIsKeyDeletedForKeyBody_function_00BC9480.md) (`PAGE` → `PAGECMRC`)
  - `0x008609F2` → [PsIsCurrentThreadInServerSilo](../../text/43/PsIsCurrentThreadInServerSilo_function_004362E0.md) (`PAGE` → `.text`)
  - `0x00860A68` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x00860A9C` → [CmpLockRegistry](../../pagecmrc/BC/CmpLockRegistry_function_00BC9B34.md) (`PAGE` → `PAGECMRC`)
  - `0x00860B0D` → [CmpDetachFromRegistryProcess](../../pagecmrc/BC/CmpDetachFromRegistryProcess_function_00BC9920.md) (`PAGE` → `PAGECMRC`)
  - `0x00860B24` → [CmpDrainDelayDerefContext](../../text/41/CmpDrainDelayDerefContext_function_0041B9A0.md) (`PAGE` → `.text`)
  - `0x00860B30` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x00860B4B` → [CmpDetachFromRegistryProcess](../../pagecmrc/BC/CmpDetachFromRegistryProcess_function_00BC9920.md) (`PAGE` → `PAGECMRC`)
  - `0x00860B72` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00860BAB` → [CmpFreePoolWithTag](../../text/44/CmpFreePoolWithTag_function_004489E0.md) (`PAGE` → `.text`)
  - `0x00860E0D` → [CmpAttachToRegistryProcess](../../pagecmrc/BC/CmpAttachToRegistryProcess_function_00BC98E0.md) (`PAGE` → `PAGECMRC`)
  - `0x00860EBA` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (`PAGE` → `PAGECMRC`)
  - `0x0086104B` → [CmpAllocatePool](../../text/3C/CmpAllocatePool_function_003CD504.md) (`PAGE` → `.text`)
  - `0x00861074` → [CmpAllocatePool](../../text/3C/CmpAllocatePool_function_003CD504.md) (`PAGE` → `.text`)
  - `0x008614CE` → [CmpIsKeyDeletedForKeyBody](../../pagecmrc/BC/CmpIsKeyDeletedForKeyBody_function_00BC9480.md) (`PAGE` → `PAGECMRC`)
  - `0x00861694` → [HvLockHiveFlusherExclusive](../../pagecmrc/BC/HvLockHiveFlusherExclusive_function_00BC9C50.md) (`PAGE` → `PAGECMRC`)
  - `0x00861764` → [HvUnlockHiveFlusherExclusive](../../pagecmrc/BC/HvUnlockHiveFlusherExclusive_function_00BC9C34.md) (`PAGE` → `PAGECMRC`)
  - `0x00861824` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (`PAGE` → `.text`)
  - `0x00861A4D` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (`PAGE` → `PAGECMRC`)
  - `0x00861A5B` → [CmpLockKcbShared](../../pagecmrc/BC/CmpLockKcbShared_function_00BC9A1C.md) (`PAGE` → `PAGECMRC`)
  - `0x00861ACD` → [CmpAttachToRegistryProcess](../../pagecmrc/BC/CmpAttachToRegistryProcess_function_00BC98E0.md) (`PAGE` → `PAGECMRC`)
  - `0x00861B66` → [HvUnlockHiveFlusherExclusive](../../pagecmrc/BC/HvUnlockHiveFlusherExclusive_function_00BC9C34.md) (`PAGE` → `PAGECMRC`)
  - `0x00861BF3` → [CmpAttachToRegistryProcess](../../pagecmrc/BC/CmpAttachToRegistryProcess_function_00BC98E0.md) (`PAGE` → `PAGECMRC`)
  - `0x00861E26` → [CmpAttachToRegistryProcess](../../pagecmrc/BC/CmpAttachToRegistryProcess_function_00BC98E0.md) (`PAGE` → `PAGECMRC`)
  - `0x00861E51` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (`PAGE` → `PAGECMRC`)
  - `0x00861E5E` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (`PAGE` → `PAGECMRC`)
  - `0x00861E7C` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **15**
  - `0x00860FD7` → [sub_00B16F66](../B1/Unknown_function_00B16F66.md) (`tail-transfer`)
  - `0x008611A9` → [sub_00B16F66 + 0x90](../B1/Unknown_function_00B16F66.md) (`tail-transfer`)
  - `0x00861251` → [sub_00B16F66 + 0x13D](../B1/Unknown_function_00B16F66.md) (`tail-transfer`)
  - `0x0086139E` → [sub_00B16F66 + 0x276](../B1/Unknown_function_00B16F66.md) (`tail-transfer`)
  - `0x00861872` → [sub_00B16F66 + 0x526](../B1/Unknown_function_00B16F66.md) (`tail-transfer`)
  - `0x00861885` → [sub_00B16F66 + 0x526](../B1/Unknown_function_00B16F66.md) (`tail-transfer`)
  - `0x00861898` → [sub_00B16F66 + 0x526](../B1/Unknown_function_00B16F66.md) (`tail-transfer`)
  - `0x00861D0C` → [sub_00B16F66 + 0x3DA](../B1/Unknown_function_00B16F66.md) (`tail-transfer`)
  - `0x00861D16` → [sub_00B16F66 + 0x3DA](../B1/Unknown_function_00B16F66.md) (`tail-transfer`)
  - `0x00861D21` → [sub_00B16F66 + 0x2F7](../B1/Unknown_function_00B16F66.md) (`tail-transfer`)
  - `0x00861DF1` → [sub_00B16F66 + 0x50B](../B1/Unknown_function_00B16F66.md) (`tail-transfer`)
  - `0x00861E02` → [sub_00B16F66 + 0x50B](../B1/Unknown_function_00B16F66.md) (`tail-transfer`)
  - `0x00861E19` → [sub_00B16F66 + 0x515](../B1/Unknown_function_00B16F66.md) (`tail-transfer`)
  - `0x00861E32` → [sub_00B16F66 + 0x515](../B1/Unknown_function_00B16F66.md) (`tail-transfer`)
  - `0x00861E4C` → [sub_00B16F66 + 0x526](../B1/Unknown_function_00B16F66.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0085F750  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
0085F755  55                              push rbp
0085F756  56                              push rsi
0085F757  57                              push rdi
0085F758  41 54                           push r12
0085F75A  41 55                           push r13
0085F75C  41 56                           push r14
0085F75E  41 57                           push r15
0085F760  48 8D AC 24 F0 FE FF FF         lea rbp, [rsp - 0x110]
0085F768  48 81 EC 10 02 00 00            sub rsp, 0x210
0085F76F  48 8B 05 CA AF 5A 00            mov rax, qword ptr [rip + 0x5aafca]
0085F776  48 33 C4                        xor rax, rsp
0085F779  48 89 85 00 01 00 00            mov qword ptr [rbp + 0x100], rax
0085F780  48 8B 85 70 01 00 00            mov rax, qword ptr [rbp + 0x170]
0085F787  33 F6                           xor esi, esi
0085F789  4C 8B BD 80 01 00 00            mov r15, qword ptr [rbp + 0x180]
0085F790  0F 57 C0                        xorps xmm0, xmm0
0085F793  4C 8B A5 78 01 00 00            mov r12, qword ptr [rbp + 0x178]
0085F79A  0F 57 C9                        xorps xmm1, xmm1
0085F79D  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
0085F7A1  45 32 F6                        xor r14b, r14b
0085F7A4  48 8B 85 90 01 00 00            mov rax, qword ptr [rbp + 0x190]
0085F7AB  41 8B F9                        mov edi, r9d
0085F7AE  48 89 45 38                     mov qword ptr [rbp + 0x38], rax
0085F7B2  44 8B EE                        mov r13d, esi
0085F7B5  8B C6                           mov eax, esi
0085F7B7  48 89 4D B0                     mov qword ptr [rbp - 0x50], rcx
0085F7BB  48 8D 4D 10                     lea rcx, [rbp + 0x10]
0085F7BF  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
0085F7C3  48 89 45 B8                     mov qword ptr [rbp - 0x48], rax
0085F7C7  88 44 24 74                     mov byte ptr [rsp + 0x74], al
0085F7CB  88 44 24 61                     mov byte ptr [rsp + 0x61], al
0085F7CF  88 45 98                        mov byte ptr [rbp - 0x68], al
0085F7D2  88 44 24 60                     mov byte ptr [rsp + 0x60], al
0085F7D6  88 44 24 7C                     mov byte ptr [rsp + 0x7c], al
0085F7DA  88 44 24 76                     mov byte ptr [rsp + 0x76], al
0085F7DE  88 45 99                        mov byte ptr [rbp - 0x67], al
0085F7E1  88 44 24 73                     mov byte ptr [rsp + 0x73], al
0085F7E5  44 88 44 24 72                  mov byte ptr [rsp + 0x72], r8b
0085F7EA  48 89 55 E0                     mov qword ptr [rbp - 0x20], rdx
0085F7EE  4C 89 7C 24 68                  mov qword ptr [rsp + 0x68], r15
0085F7F3  66 89 75 D8                     mov word ptr [rbp - 0x28], si
0085F7F7  0F 11 85 B0 00 00 00            movups xmmword ptr [rbp + 0xb0], xmm0
0085F7FE  48 89 75 10                     mov qword ptr [rbp + 0x10], rsi
0085F802  0F 11 4D 28                     movups xmmword ptr [rbp + 0x28], xmm1
0085F806  48 89 75 08                     mov qword ptr [rbp + 8], rsi
0085F80A  48 89 75 D0                     mov qword ptr [rbp - 0x30], rsi
0085F80E  48 89 75 A0                     mov qword ptr [rbp - 0x60], rsi
0085F812  48 89 75 18                     mov qword ptr [rbp + 0x18], rsi
0085F816  48 89 75 A8                     mov qword ptr [rbp - 0x58], rsi
0085F81A  44 88 74 24 71                  mov byte ptr [rsp + 0x71], r14b
0085F81F  66 89 74 24 78                  mov word ptr [rsp + 0x78], si
0085F824  66 89 75 88                     mov word ptr [rbp - 0x78], si
0085F828  48 89 75 20                     mov qword ptr [rbp + 0x20], rsi
0085F82C  E8 DF 66 FF FF                  call 0x140855f10
0085F831  41 0F 10 04 24                  movups xmm0, xmmword ptr [r12]
0085F836  48 8D 4D 28                     lea rcx, [rbp + 0x28]
0085F83A  40 88 74 24 70                  mov byte ptr [rsp + 0x70], sil
0085F83F  0F 11 45 F8                     movups xmmword ptr [rbp - 8], xmm0
0085F843  E8 A8 AF BC FF                  call 0x14042a7f0
0085F848  0F 57 C0                        xorps xmm0, xmm0
0085F84B  40 88 74 24 77                  mov byte ptr [rsp + 0x77], sil
0085F850  B8 FF FF FF FF                  mov eax, 0xffffffff
0085F855  48 89 75 C8                     mov qword ptr [rbp - 0x38], rsi
0085F859  41 0F 11 87 A0 00 00 00         movups xmmword ptr [r15 + 0xa0], xmm0
0085F861  33 D2                           xor edx, edx
0085F863  41 B8 A8 00 00 00               mov r8d, 0xa8
0085F869  41 0F 11 87 B0 00 00 00         movups xmmword ptr [r15 + 0xb0], xmm0
0085F871  0F 11 45 40                     movups xmmword ptr [rbp + 0x40], xmm0
0085F875  66 89 45 42                     mov word ptr [rbp + 0x42], ax
0085F879  0F 11 45 60                     movups xmmword ptr [rbp + 0x60], xmm0
0085F87D  66 89 45 62                     mov word ptr [rbp + 0x62], ax
0085F881  0F 11 85 80 00 00 00            movups xmmword ptr [rbp + 0x80], xmm0
0085F888  66 89 85 82 00 00 00            mov word ptr [rbp + 0x82], ax
0085F88F  33 C0                           xor eax, eax
0085F891  41 0F 11 87 C0 00 00 00         movups xmmword ptr [r15 + 0xc0], xmm0
0085F899  49 89 87 D0 00 00 00            mov qword ptr [r15 + 0xd0], rax
0085F8A0  49 8D 87 D8 00 00 00            lea rax, [r15 + 0xd8]
0085F8A7  48 8B C8                        mov rcx, rax
0085F8AA  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
0085F8AE  0F 11 45 50                     movups xmmword ptr [rbp + 0x50], xmm0
0085F8B2  0F 11 45 70                     movups xmmword ptr [rbp + 0x70], xmm0
0085F8B6  0F 11 85 90 00 00 00            movups xmmword ptr [rbp + 0x90], xmm0
0085F8BD  E8 7E 73 E6 FF                  call 0x1406c6c40
0085F8C2  33 D2                           xor edx, edx
0085F8C4  44 8D 46 50                     lea r8d, [rsi + 0x50]
0085F8C8  49 8D 8F 80 01 00 00            lea rcx, [r15 + 0x180]
0085F8CF  E8 6C 73 E6 FF                  call 0x1406c6c40
0085F8D4  49 8D 4F 58                     lea rcx, [r15 + 0x58]
0085F8D8  4D 85 FF                        test r15, r15
0085F8DB  74 0A                           je 0x14085f8e7
0085F8DD  48 8B 01                        mov rax, qword ptr [rcx]
0085F8E0  49 89 87 80 01 00 00            mov qword ptr [r15 + 0x180], rax
0085F8E7  B8 00 02 00 00                  mov eax, 0x200
0085F8EC  0F BA E7 08                     bt edi, 8
0085F8F0  0F 82 7A 0D 00 00               jb 0x140860670
0085F8F6  4C 8B 44 24 68                  mov r8, qword ptr [rsp + 0x68]
0085F8FB  4C 8B 39                        mov r15, qword ptr [rcx]
0085F8FE  48 8B 7D B0                     mov rdi, qword ptr [rbp - 0x50]
0085F902  48 89 31                        mov qword ptr [rcx], rsi
0085F905  49 8B 58 48                     mov rbx, qword ptr [r8 + 0x48]
0085F909  48 85 DB                        test rbx, rbx
0085F90C  0F 85 AA 12 00 00               jne 0x140860bbc
0085F912  48 8B 57 40                     mov rdx, qword ptr [rdi + 0x40]
0085F916  48 8B 5F 38                     mov rbx, qword ptr [rdi + 0x38]
0085F91A  48 89 55 F0                     mov qword ptr [rbp - 0x10], rdx
0085F91E  0F B7 47 32                     movzx eax, word ptr [rdi + 0x32]
0085F922  41 89 40 14                     mov dword ptr [r8 + 0x14], eax
0085F926  48 8B 05 3B A2 77 00            mov rax, qword ptr [rip + 0x77a23b]
0085F92D  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
0085F931  48 39 4F 08                     cmp qword ptr [rdi + 8], rcx
0085F935  0F 85 D4 02 00 00               jne 0x14085fc0f
0085F93B  4D 85 FF                        test r15, r15
0085F93E  0F 85 00 03 00 00               jne 0x14085fc44
0085F944  44 0F B7 E6                     movzx r12d, si
0085F948  44 88 74 24 71                  mov byte ptr [rsp + 0x71], r14b
0085F94D  40 88 74 24 75                  mov byte ptr [rsp + 0x75], sil
0085F952  40 88 74 24 61                  mov byte ptr [rsp + 0x61], sil
0085F957  4C 8B 45 C0                     mov r8, qword ptr [rbp - 0x40]
0085F95B  48 8D 55 88                     lea rdx, [rbp - 0x78]
0085F95F  48 8B 7F 08                     mov rdi, qword ptr [rdi + 8]
0085F963  48 8D 4D F8                     lea rcx, [rbp - 8]
0085F967  E8 84 F9 FF FF                  call 0x14085f2f0
0085F96C  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
0085F970  85 C0                           test eax, eax
0085F972  0F 88 25 1F 00 00               js 0x14086189d
0085F978  0F BF 55 88                     movsx edx, word ptr [rbp - 0x78]
0085F97C  8B CE                           mov ecx, esi
0085F97E  4C 8B 45 C0                     mov r8, qword ptr [rbp - 0x40]
0085F982  41 B9 00 02 00 00               mov r9d, 0x200
0085F988  3B CA                           cmp ecx, edx
0085F98A  73 24                           jae 0x14085f9b0
0085F98C  83 F9 08                        cmp ecx, 8
0085F98F  0F 83 19 02 00 00               jae 0x14085fbae
0085F995  8B C1                           mov eax, ecx
0085F997  48 83 C0 02                     add rax, 2
0085F99B  48 C1 E0 04                     shl rax, 4
0085F99F  49 03 C0                        add rax, r8
0085F9A2  66 44 39 08                     cmp word ptr [rax], r9w
0085F9A6  0F 87 0B 1F 00 00               ja 0x1408618b7
0085F9AC  FF C1                           inc ecx
0085F9AE  EB D8                           jmp 0x14085f988
0085F9B0  44 89 64 24 78                  mov dword ptr [rsp + 0x78], r12d
0085F9B5  4C 8B 4C 24 68                  mov r9, qword ptr [rsp + 0x68]
0085F9BA  0F B6 54 24 61                  movzx edx, byte ptr [rsp + 0x61]
0085F9BF  41 0F B7 C4                     movzx eax, r12w
0085F9C3  44 88 74 24 71                  mov byte ptr [rsp + 0x71], r14b
0085F9C8  44 0F BF 75 88                  movsx r14d, word ptr [rbp - 0x78]
0085F9CD  49 89 B9 88 01 00 00            mov qword ptr [r9 + 0x188], rdi
0085F9D4  49 89 B9 A0 01 00 00            mov qword ptr [r9 + 0x1a0], rdi
0085F9DB  8B 4F 08                        mov ecx, dword ptr [rdi + 8]
0085F9DE  C1 E9 15                        shr ecx, 0x15
0085F9E1  81 E1 FF 03 00 00               and ecx, 0x3ff
0085F9E7  88 54 24 61                     mov byte ptr [rsp + 0x61], dl
0085F9EB  2B C8                           sub ecx, eax
0085F9ED  B8 00 02 00 00                  mov eax, 0x200
0085F9F2  41 03 CE                        add ecx, r14d
0085F9F5  3B C8                           cmp ecx, eax
0085F9F7  0F 87 ED 1E 00 00               ja 0x1408618ea
0085F9FD  84 D2                           test dl, dl
0085F9FF  75 1C                           jne 0x14085fa1d
0085FA01  41 F7 01 00 04 00 00            test dword ptr [r9], 0x400
0085FA08  0F 85 A4 11 00 00               jne 0x140860bb2
0085FA0E  E8 21 A1 36 00                  call 0x140bc9b34
0085FA13  4C 8B 4C 24 68                  mov r9, qword ptr [rsp + 0x68]
0085FA18  C6 44 24 61 01                  mov byte ptr [rsp + 0x61], 1
0085FA1D  48 8B 4D B0                     mov rcx, qword ptr [rbp - 0x50]
0085FA21  8B 41 30                        mov eax, dword ptr [rcx + 0x30]
0085FA24  A8 09                           test al, 9
0085FA26  0F 85 DF 1E 00 00               jne 0x14086190b
0085FA2C  48 8B CF                        mov rcx, rdi
0085FA2F  66 45 3B E6                     cmp r12w, r14w
0085FA33  0F 84 44 0F 00 00               je 0x14086097d
0085FA39  48 8D 45 D8                     lea rax, [rbp - 0x28]
0085FA3D  41 0F B7 D4                     movzx edx, r12w
0085FA41  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0085FA46  45 8B C6                        mov r8d, r14d
0085FA49  48 8D 44 24 70                  lea rax, [rsp + 0x70]
0085FA4E  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0085FA53  48 8D 45 A0                     lea rax, [rbp - 0x60]
0085FA57  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0085FA5C  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
0085FA61  49 81 C1 D8 00 00 00            add r9, 0xd8
0085FA68  E8 B3 02 FF FF                  call 0x14084fd20
0085FA6D  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
0085FA71  85 C0                           test eax, eax
0085FA73  0F 88 CE 23 00 00               js 0x140861e47
0085FA79  3D 03 01 00 00                  cmp eax, 0x103
0085FA7E  0F 84 C3 23 00 00               je 0x140861e47
0085FA84  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
0085FA89  4C 8B 6D A0                     mov r13, qword ptr [rbp - 0x60]
0085FA8D  0F B7 45 D8                     movzx eax, word ptr [rbp - 0x28]
0085FA91  66 44 03 E0                     add r12w, ax
0085FA95  4C 89 6D 90                     mov qword ptr [rbp - 0x70], r13
0085FA99  4C 89 A9 90 01 00 00            mov qword ptr [rcx + 0x190], r13
0085FAA0  88 81 A8 01 00 00               mov byte ptr [rcx + 0x1a8], al
0085FAA6  4C 89 A9 A0 01 00 00            mov qword ptr [rcx + 0x1a0], r13
0085FAAD  44 89 64 24 78                  mov dword ptr [rsp + 0x78], r12d
0085FAB2  66 45 3B E6                     cmp r12w, r14w
0085FAB6  75 13                           jne 0x14085facb
0085FAB8  8B 01                           mov eax, dword ptr [rcx]
0085FABA  A8 01                           test al, 1
0085FABC  75 0D                           jne 0x14085facb
0085FABE  49 8B CD                        mov rcx, r13
0085FAC1  E8 AA 48 00 00                  call 0x140864370
0085FAC6  40 88 74 24 70                  mov byte ptr [rsp + 0x70], sil
0085FACB  49 8B CD                        mov rcx, r13
0085FACE  E8 49 9F 36 00                  call 0x140bc9a1c
0085FAD3  66 45 3B E6                     cmp r12w, r14w
0085FAD7  0F 8C E8 00 00 00               jl 0x14085fbc5
0085FADD  33 D2                           xor edx, edx
0085FADF  48 8D 8D B0 00 00 00            lea rcx, [rbp + 0xb0]
0085FAE6  E8 95 AC BC FF                  call 0x14042a780
0085FAEB  48 8B 7D E0                     mov rdi, qword ptr [rbp - 0x20]
0085FAEF  48 83 C7 20                     add rdi, 0x20
0085FAF3  40 38 35 A6 F1 5A 00            cmp byte ptr [rip + 0x5af1a6], sil
0085FAFA  0F 84 21 0B 00 00               je 0x140860621
0085FB00  4C 8B 74 24 68                  mov r14, qword ptr [rsp + 0x68]
0085FB05  41 8B 46 18                     mov eax, dword ptr [r14 + 0x18]
0085FB09  A8 10                           test al, 0x10
0085FB0B  0F 85 56 14 00 00               jne 0x140860f67
0085FB11  66 41 39 75 42                  cmp word ptr [r13 + 0x42], si
0085FB16  0F 85 1B 01 00 00               jne 0x14085fc37
0085FB1C  49 8B CD                        mov rcx, r13
0085FB1F  E8 3C F6 FF FF                  call 0x14085f160
0085FB24  84 C0                           test al, al
0085FB26  0F 85 4D 02 00 00               jne 0x14085fd79
0085FB2C  B8 71 02 00 C0                  mov eax, 0xc0000271
0085FB31  49 8B FE                        mov rdi, r14
0085FB34  49 8B CD                        mov rcx, r13
0085FB37  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
0085FB3B  E8 80 97 36 00                  call 0x140bc92c0
0085FB40  44 8B 44 24 64                  mov r8d, dword ptr [rsp + 0x64]
0085FB45  41 81 F8 71 02 00 C0            cmp r8d, 0xc0000271
0085FB4C  0F 85 E6 1D 00 00               jne 0x140861938
0085FB52  48 8B 7F 40                     mov rdi, qword ptr [rdi + 0x40]
0085FB56  4D 8B 75 20                     mov r14, qword ptr [r13 + 0x20]
0085FB5A  48 85 FF                        test rdi, rdi
0085FB5D  0F 84 A9 02 00 00               je 0x14085fe0c
0085FB63  49 3B FE                        cmp rdi, r14
0085FB66  0F 84 A0 02 00 00               je 0x14085fe0c
0085FB6C  41 8B 86 10 10 00 00            mov eax, dword ptr [r14 + 0x1010]
0085FB73  A8 01                           test al, 1
0085FB75  0F 84 34 08 00 00               je 0x1408603af
0085FB7B  E8 48 E8 FE FF                  call 0x14084e3c8
0085FB80  49 81 C6 18 10 00 00            add r14, 0x1018
0085FB87  49 8B 0E                        mov rcx, qword ptr [r14]
0085FB8A  66 0F 1F 44 00 00               nop word ptr [rax + rax]
0085FB90  49 3B CE                        cmp rcx, r14
0085FB93  0F 84 11 08 00 00               je 0x1408603aa
0085FB99  48 8D 81 E8 EF FF FF            lea rax, [rcx - 0x1018]
0085FBA0  48 3B C7                        cmp rax, rdi
0085FBA3  0F 84 5E 02 00 00               je 0x14085fe07
0085FBA9  48 8B 09                        mov rcx, qword ptr [rcx]
0085FBAC  EB E2                           jmp 0x14085fb90
0085FBAE  8D 41 F8                        lea eax, [rcx - 8]
0085FBB1  48 83 C0 06                     add rax, 6
0085FBB5  48 C1 E0 04                     shl rax, 4
0085FBB9  49 03 80 A0 00 00 00            add rax, qword ptr [r8 + 0xa0]
0085FBC0  E9 DD FD FF FF                  jmp 0x14085f9a2
0085FBC5  41 0F BF C4                     movsx eax, r12w
0085FBC9  83 F8 08                        cmp eax, 8
0085FBCC  0F 83 A6 0A 00 00               jae 0x140860678
0085FBD2  48 8B 4D C0                     mov rcx, qword ptr [rbp - 0x40]
0085FBD6  48 C1 E0 04                     shl rax, 4
0085FBDA  48 83 C1 28                     add rcx, 0x28
0085FBDE  48 03 C8                        add rcx, rax
0085FBE1  0F B7 45 F8                     movzx eax, word ptr [rbp - 8]
0085FBE5  48 8B 09                        mov rcx, qword ptr [rcx]
0085FBE8  48 89 8D B8 00 00 00            mov qword ptr [rbp + 0xb8], rcx
0085FBEF  48 2B 4D 00                     sub rcx, qword ptr [rbp]
0085FBF3  48 D1 F9                        sar rcx, 1
0085FBF6  66 03 C9                        add cx, cx
0085FBF9  66 2B C1                        sub ax, cx
0085FBFC  66 89 85 B0 00 00 00            mov word ptr [rbp + 0xb0], ax
0085FC03  66 89 85 B2 00 00 00            mov word ptr [rbp + 0xb2], ax
0085FC0A  E9 DC FE FF FF                  jmp 0x14085faeb
0085FC0F  4D 85 FF                        test r15, r15
0085FC12  0F 84 2C FD FF FF               je 0x14085f944
0085FC18  E8 17 9F 36 00                  call 0x140bc9b34
0085FC1D  49 8B CF                        mov rcx, r15
0085FC20  E8 EB 16 FF FF                  call 0x140851310
0085FC25  4C 8B FE                        mov r15, rsi
0085FC28  E8 57 9E 36 00                  call 0x140bc9a84
0085FC2D  44 8B 64 24 78                  mov r12d, dword ptr [rsp + 0x78]
0085FC32  E9 16 FD FF FF                  jmp 0x14085f94d
0085FC37  B8 71 02 00 C0                  mov eax, 0xc0000271
0085FC3C  49 8B FE                        mov rdi, r14
0085FC3F  E9 F0 FE FF FF                  jmp 0x14085fb34
0085FC44  41 F7 00 00 04 00 00            test dword ptr [r8], 0x400
0085FC4B  0F 85 82 11 00 00               jne 0x140860dd3
0085FC51  E8 DE 9E 36 00                  call 0x140bc9b34
0085FC56  4D 8B B7 28 01 00 00            mov r14, qword ptr [r15 + 0x128]
0085FC5D  49 8B C6                        mov rax, r14
0085FC60  C6 44 24 61 01                  mov byte ptr [rsp + 0x61], 1
0085FC65  83 E0 01                        and eax, 1
0085FC68  74 04                           je 0x14085fc6e
0085FC6A  49 83 E6 FE                     and r14, 0xfffffffffffffffe
0085FC6E  4D 85 F6                        test r14, r14
0085FC71  0F 84 C1 09 00 00               je 0x140860638
0085FC77  84 C0                           test al, al
0085FC79  0F 85 B9 09 00 00               jne 0x140860638
0085FC7F  4C 8B 6D E8                     mov r13, qword ptr [rbp - 0x18]
0085FC83  41 B0 01                        mov r8b, 1
0085FC86  49 8B D5                        mov rdx, r13
0085FC89  49 8B CE                        mov rcx, r14
0085FC8C  E8 DF 52 09 00                  call 0x1408f4f70
0085FC91  84 C0                           test al, al
0085FC93  0F 84 9F 09 00 00               je 0x140860638
0085FC99  41 0F B7 16                     movzx edx, word ptr [r14]
0085FC9D  49 8B 45 08                     mov rax, qword ptr [r13 + 8]
0085FCA1  8B CA                           mov ecx, edx
0085FCA3  48 D1 E9                        shr rcx, 1
0085FCA6  4C 8D 04 48                     lea r8, [rax + rcx*2]
0085FCAA  41 0F B7 4D 00                  movzx ecx, word ptr [r13]
0085FCAF  41 0F B7 45 02                  movzx eax, word ptr [r13 + 2]
0085FCB4  66 2B CA                        sub cx, dx
0085FCB7  66 2B C2                        sub ax, dx
0085FCBA  4C 89 45 00                     mov qword ptr [rbp], r8
0085FCBE  66 89 4D F8                     mov word ptr [rbp - 8], cx
0085FCC2  66 89 45 FA                     mov word ptr [rbp - 6], ax
0085FCC6  66 85 C9                        test cx, cx
0085FCC9  74 27                           je 0x14085fcf2
0085FCCB  BA FE FF 00 00                  mov edx, 0xfffe
0085FCD0  66 41 83 38 5C                  cmp word ptr [r8], 0x5c
0085FCD5  75 17                           jne 0x14085fcee
0085FCD7  66 03 CA                        add cx, dx
0085FCDA  66 03 C2                        add ax, dx
0085FCDD  49 83 C0 02                     add r8, 2
0085FCE1  66 89 4D F8                     mov word ptr [rbp - 8], cx
0085FCE5  66 89 45 FA                     mov word ptr [rbp - 6], ax
0085FCE9  66 85 C9                        test cx, cx
0085FCEC  75 E2                           jne 0x14085fcd0
0085FCEE  4C 89 45 00                     mov qword ptr [rbp], r8
0085FCF2  41 8B 7F 08                     mov edi, dword ptr [r15 + 8]
0085FCF6  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
0085FCFB  C1 EF 15                        shr edi, 0x15
0085FCFE  81 E7 FF 03 00 00               and edi, 0x3ff
0085FD04  FF CF                           dec edi
0085FD06  8B 00                           mov eax, dword ptr [rax]
0085FD08  A8 01                           test al, 1
0085FD0A  0F 85 F9 0F 00 00               jne 0x140860d09
0085FD10  44 8B 74 24 78                  mov r14d, dword ptr [rsp + 0x78]
0085FD15  4C 8B 6D C0                     mov r13, qword ptr [rbp - 0x40]
0085FD19  48 8D 55 88                     lea rdx, [rbp - 0x78]
0085FD1D  4D 8B C5                        mov r8, r13
0085FD20  48 8D 4D F8                     lea rcx, [rbp - 8]
0085FD24  E8 C7 F5 FF FF                  call 0x14085f2f0
0085FD29  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
0085FD2D  85 C0                           test eax, eax
0085FD2F  0F 88 38 1B 00 00               js 0x14086186d
0085FD35  44 0F BF 4D 88                  movsx r9d, word ptr [rbp - 0x78]
0085FD3A  41 8D 04 39                     lea eax, [r9 + rdi]
0085FD3E  83 F8 20                        cmp eax, 0x20
0085FD41  0F 87 30 1B 00 00               ja 0x140861877
0085FD47  8B CE                           mov ecx, esi
0085FD49  41 B8 00 02 00 00               mov r8d, 0x200
0085FD4F  90                              nop
0085FD50  41 3B C9                        cmp ecx, r9d
0085FD53  73 4A                           jae 0x14085fd9f
0085FD55  83 F9 08                        cmp ecx, 8
0085FD58  0F 83 76 05 00 00               jae 0x1408602d4
0085FD5E  8B C1                           mov eax, ecx
0085FD60  48 83 C0 02                     add rax, 2
0085FD64  48 C1 E0 04                     shl rax, 4
0085FD68  49 03 C5                        add rax, r13
0085FD6B  66 44 39 00                     cmp word ptr [rax], r8w
0085FD6F  0F 87 15 1B 00 00               ja 0x14086188a
0085FD75  FF C1                           inc ecx
0085FD77  EB D7                           jmp 0x14085fd50
0085FD79  0F B6 4C 24 72                  movzx ecx, byte ptr [rsp + 0x72]
0085FD7E  4D 8D 46 10                     lea r8, [r14 + 0x10]
0085FD82  48 8B D7                        mov rdx, rdi
0085FD85  E8 06 51 05 00                  call 0x1408b4e90
0085FD8A  84 C0                           test al, al
0085FD8C  0F 84 5E 10 00 00               je 0x140860df0
0085FD92  B8 71 02 00 C0                  mov eax, 0xc0000271
0085FD97  49 8B FE                        mov rdi, r14
0085FD9A  E9 95 FD FF FF                  jmp 0x14085fb34
0085FD9F  66 45 3B F1                     cmp r14w, r9w
0085FDA3  0F 85 87 08 00 00               jne 0x140860630
0085FDA9  49 8B CF                        mov rcx, r15
0085FDAC  E8 23 55 19 00                  call 0x1409f52d4
0085FDB1  41 B6 01                        mov r14b, 1
0085FDB4  44 88 74 24 71                  mov byte ptr [rsp + 0x71], r14b
0085FDB9  49 8B CF                        mov rcx, r15
0085FDBC  44 88 74 24 75                  mov byte ptr [rsp + 0x75], r14b
0085FDC1  E8 56 9C 36 00                  call 0x140bc9a1c
0085FDC6  33 D2                           xor edx, edx
0085FDC8  49 8B CF                        mov rcx, r15
0085FDCB  E8 E0 BF FE FF                  call 0x14084bdb0
0085FDD0  84 C0                           test al, al
0085FDD2  0F 85 E7 08 00 00               jne 0x1408606bf
0085FDD8  41 8B 47 08                     mov eax, dword ptr [r15 + 8]
0085FDDC  0F BA E0 12                     bt eax, 0x12
0085FDE0  0F 82 D9 08 00 00               jb 0x1408606bf
0085FDE6  49 8B CF                        mov rcx, r15
0085FDE9  E8 D2 94 36 00                  call 0x140bc92c0
0085FDEE  48 8B 45 B8                     mov rax, qword ptr [rbp - 0x48]
0085FDF2  49 8B FF                        mov rdi, r15
0085FDF5  4C 8B 6D A0                     mov r13, qword ptr [rbp - 0x60]
0085FDF9  44 8B 64 24 78                  mov r12d, dword ptr [rsp + 0x78]
0085FDFE  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
0085FE02  E9 AE FB FF FF                  jmp 0x14085f9b5
0085FE07  E8 18 E6 FE FF                  call 0x14084e424
0085FE0C  48 8B 7D F0                     mov rdi, qword ptr [rbp - 0x10]
0085FE10  48 85 DB                        test rbx, rbx
0085FE13  0F 85 A5 0B 00 00               jne 0x1408609be
0085FE19  48 85 FF                        test rdi, rdi
0085FE1C  0F 85 9C 0B 00 00               jne 0x1408609be
0085FE22  E8 19 3D BE FF                  call 0x140443b40
0085FE27  84 C0                           test al, al
0085FE29  0F 85 7F 0B 00 00               jne 0x1408609ae
0085FE2F  48 85 DB                        test rbx, rbx
0085FE32  75 09                           jne 0x14085fe3d
0085FE34  48 85 FF                        test rdi, rdi
0085FE37  0F 84 71 0B 00 00               je 0x1408609ae
0085FE3D  49 8B 4D 20                     mov rcx, qword ptr [r13 + 0x20]
0085FE41  48 85 C9                        test rcx, rcx
0085FE44  0F 84 0A 0C 00 00               je 0x140860a54
0085FE4A  F6 C3 01                        test bl, 1
0085FE4D  0F 84 85 0C 00 00               je 0x140860ad8
0085FE53  48 8B FB                        mov rdi, rbx
0085FE56  48 8B CB                        mov rcx, rbx
0085FE59  48 83 E7 FE                     and rdi, 0xfffffffffffffffe
0085FE5D  E8 D2 35 01 00                  call 0x140873434
0085FE62  44 8B F0                        mov r14d, eax
0085FE65  85 C0                           test eax, eax
0085FE67  78 2D                           js 0x14085fe96
0085FE69  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
0085FE6D  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
0085FE71  48 85 C0                        test rax, rax
0085FE74  0F 84 63 0F 00 00               je 0x140860ddd
0085FE7A  48 89 45 B8                     mov qword ptr [rbp - 0x48], rax
0085FE7E  44 8B F6                        mov r14d, esi
0085FE81  48 85 DB                        test rbx, rbx
0085FE84  74 08                           je 0x14085fe8e
0085FE86  48 8B CF                        mov rcx, rdi
0085FE89  E8 C2 94 A9 FF                  call 0x1402f9350
0085FE8E  4C 8B 6D A0                     mov r13, qword ptr [rbp - 0x60]
0085FE92  4C 89 6D 90                     mov qword ptr [rbp - 0x70], r13
0085FE96  48 8B 7D F0                     mov rdi, qword ptr [rbp - 0x10]
0085FE9A  45 85 F6                        test r14d, r14d
0085FE9D  0F 88 B1 0B 00 00               js 0x140860a54
0085FEA3  41 0F BF 5D 42                  movsx ebx, word ptr [r13 + 0x42]
0085FEA8  48 8B CE                        mov rcx, rsi
0085FEAB  83 FB 02                        cmp ebx, 2
0085FEAE  7C 0B                           jl 0x14085febb
0085FEB0  8B C3                           mov eax, ebx
0085FEB2  83 E8 01                        sub eax, 1
0085FEB5  0F 85 7F 11 00 00               jne 0x14086103a
0085FEBB  48 89 4D 58                     mov qword ptr [rbp + 0x58], rcx
0085FEBF  BF FF FF FF FF                  mov edi, 0xffffffff
0085FEC4  66 89 7D 42                     mov word ptr [rbp + 0x42], di
0085FEC8  48 8B CE                        mov rcx, rsi
0085FECB  66 89 5D 40                     mov word ptr [rbp + 0x40], bx
0085FECF  41 0F BF 5D 42                  movsx ebx, word ptr [r13 + 0x42]
0085FED4  83 FB 02                        cmp ebx, 2
0085FED7  7C 0B                           jl 0x14085fee4
0085FED9  8B C3                           mov eax, ebx
0085FEDB  83 E8 01                        sub eax, 1
0085FEDE  0F 85 7F 11 00 00               jne 0x140861063
0085FEE4  66 89 7D 62                     mov word ptr [rbp + 0x62], di
0085FEE8  4C 8D 75 40                     lea r14, [rbp + 0x40]
0085FEEC  66 89 5D 60                     mov word ptr [rbp + 0x60], bx
0085FEF0  48 8D 7D 60                     lea rdi, [rbp + 0x60]
0085FEF4  48 89 4D 78                     mov qword ptr [rbp + 0x78], rcx
0085FEF8  89 74 24 64                     mov dword ptr [rsp + 0x64], esi
0085FEFC  41 0F B7 45 42                  movzx eax, word ptr [r13 + 0x42]
0085FF01  66 89 45 42                     mov word ptr [rbp + 0x42], ax
0085FF05  49 0F BF 55 42                  movsx rdx, word ptr [r13 + 0x42]
0085FF0A  66 85 D2                        test dx, dx
0085FF0D  0F 85 3B 0F 00 00               jne 0x140860e4e
0085FF13  4C 89 6C D5 48                  mov qword ptr [rbp + rdx*8 + 0x48], r13
0085FF18  0F BF 45 88                     movsx eax, word ptr [rbp - 0x78]
0085FF1C  4C 8B 65 90                     mov r12, qword ptr [rbp - 0x70]
0085FF20  44 8B E8                        mov r13d, eax
0085FF23  8B 5C 24 78                     mov ebx, dword ptr [rsp + 0x78]
0085FF27  66 3B D8                        cmp bx, ax
0085FF2A  0F 8D F2 07 00 00               jge 0x140860722
0085FF30  49 8B CE                        mov rcx, r14
0085FF33  E8 C8 80 0E 00                  call 0x140948000
0085FF38  41 F7 44 24 08 00 00 02 00      test dword ptr [r12 + 8], 0x20000
0085FF41  0F 85 76 11 00 00               jne 0x1408610bd
0085FF47  41 0F B7 56 02                  movzx edx, word ptr [r14 + 2]
0085FF4C  48 89 75 F0                     mov qword ptr [rbp - 0x10], rsi
0085FF50  66 85 D2                        test dx, dx
0085FF53  0F 88 52 01 00 00               js 0x1408600ab
0085FF59  48 0F BF CA                     movsx rcx, dx
0085FF5D  66 83 FA 02                     cmp dx, 2
0085FF61  0F 8D DF 0A 00 00               jge 0x140860a46
0085FF67  49 8B 4C CE 08                  mov rcx, qword ptr [r14 + rcx*8 + 8]
0085FF6C  66 39 71 42                     cmp word ptr [rcx + 0x42], si
0085FF70  74 0A                           je 0x14085ff7c
0085FF72  80 79 41 01                     cmp byte ptr [rcx + 0x41], 1
0085FF76  0F 84 2F 01 00 00               je 0x1408600ab
0085FF7C  83 79 28 FF                     cmp dword ptr [rcx + 0x28], -1
0085FF80  0F 84 1D 01 00 00               je 0x1408600a3
0085FF86  4C 8B 55 80                     mov r10, qword ptr [rbp - 0x80]
0085FF8A  4D 85 D2                        test r10, r10
0085FF8D  0F 85 48 06 00 00               jne 0x1408605db
0085FF93  49 8B CE                        mov rcx, r14
0085FF96  E8 45 8D 14 00                  call 0x1409a8ce0
0085FF9B  84 C0                           test al, al
0085FF9D  0F 85 48 03 00 00               jne 0x1408602eb
0085FFA3  49 8B CE                        mov rcx, r14
0085FFA6  E8 B5 84 FE FF                  call 0x140848460
0085FFAB  44 0F BF CB                     movsx r9d, bx
0085FFAF  41 83 F9 08                     cmp r9d, 8
0085FFB3  0F 83 DC 06 00 00               jae 0x140860695
0085FFB9  4C 8B 5D C0                     mov r11, qword ptr [rbp - 0x40]
0085FFBD  45 8B C1                        mov r8d, r9d
0085FFC0  49 83 C0 02                     add r8, 2
0085FFC4  49 C1 E0 04                     shl r8, 4
0085FFC8  43 8B 0C 8B                     mov ecx, dword ptr [r11 + r9*4]
0085FFCC  4D 03 C3                        add r8, r11
0085FFCF  41 6B 44 24 10 25               imul eax, dword ptr [r12 + 0x10], 0x25
0085FFD5  4C 8B 54 24 68                  mov r10, qword ptr [rsp + 0x68]
0085FFDA  41 8B 12                        mov edx, dword ptr [r10]
0085FFDD  03 C1                           add eax, ecx
0085FFDF  F6 C2 01                        test dl, 1
0085FFE2  74 0D                           je 0x14085fff1
0085FFE4  41 8D 55 FF                     lea edx, [r13 - 1]
0085FFE8  44 3B CA                        cmp r9d, edx
0085FFEB  0F 84 4E 0A 00 00               je 0x140860a3f
0085FFF1  32 D2                           xor dl, dl
0085FFF3  4C 89 54 24 50                  mov qword ptr [rsp + 0x50], r10
0085FFF8  4C 8B CF                        mov r9, rdi
0085FFFB  88 54 24 48                     mov byte ptr [rsp + 0x48], dl
0085FFFF  48 8B 55 80                     mov rdx, qword ptr [rbp - 0x80]
00860003  48 89 54 24 40                  mov qword ptr [rsp + 0x40], rdx
00860008  49 8B D6                        mov rdx, r14
0086000B  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
0086000F  48 8D 45 98                     lea rax, [rbp - 0x68]
00860013  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
00860017  49 8B CC                        mov rcx, r12
0086001A  4C 89 44 24 28                  mov qword ptr [rsp + 0x28], r8
0086001F  4C 8D 45 18                     lea r8, [rbp + 0x18]
00860023  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00860028  E8 73 2B FF FF                  call 0x140852ba0
0086002D  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
00860031  3D 34 00 00 C0                  cmp eax, 0xc0000034
00860036  0F 84 D9 01 00 00               je 0x140860215
0086003C  39 74 24 64                     cmp dword ptr [rsp + 0x64], esi
00860040  0F 8C 34 0D 00 00               jl 0x140860d7a
00860046  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
0086004B  49 8B CC                        mov rcx, r12
0086004E  48 8B 5D 18                     mov rbx, qword ptr [rbp + 0x18]
00860052  FE 80 A9 01 00 00               inc byte ptr [rax + 0x1a9]
00860058  48 89 98 98 01 00 00            mov qword ptr [rax + 0x198], rbx
0086005F  48 89 98 A0 01 00 00            mov qword ptr [rax + 0x1a0], rbx
00860066  E8 F5 F8 13 00                  call 0x14099f960
0086006B  0F B6 45 98                     movzx eax, byte ptr [rbp - 0x68]
0086006F  4C 8B E3                        mov r12, rbx
00860072  48 89 5D 90                     mov qword ptr [rbp - 0x70], rbx
00860076  48 89 5D A0                     mov qword ptr [rbp - 0x60], rbx
0086007A  8B 5C 24 78                     mov ebx, dword ptr [rsp + 0x78]
0086007E  88 44 24 70                     mov byte ptr [rsp + 0x70], al
00860082  66 FF C3                        inc bx
00860085  49 8B C6                        mov rax, r14
00860088  48 89 75 18                     mov qword ptr [rbp + 0x18], rsi
0086008C  4C 8B F7                        mov r14, rdi
0086008F  40 88 75 98                     mov byte ptr [rbp - 0x68], sil
00860093  48 8B F8                        mov rdi, rax
00860096  89 5C 24 78                     mov dword ptr [rsp + 0x78], ebx
0086009A  0F B7 45 88                     movzx eax, word ptr [rbp - 0x78]
0086009E  E9 84 FE FF FF                  jmp 0x14085ff27
008600A3  66 FF CA                        dec dx
008600A6  E9 A5 FE FF FF                  jmp 0x14085ff50
008600AB  40 38 35 92 FA 68 00            cmp byte ptr [rip + 0x68fa92], sil
008600B2  0F 85 49 10 00 00               jne 0x140861101
008600B8  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
008600BD  BA 00 10 00 00                  mov edx, 0x1000
008600C2  C7 44 24 64 34 00 00 C0         mov dword ptr [rsp + 0x64], 0xc0000034
008600CA  41 B8 34 00 00 C0               mov r8d, 0xc0000034
008600D0  48 8B CF                        mov rcx, rdi
008600D3  E8 A8 11 FF FF                  call 0x140851280
008600D8  32 DB                           xor bl, bl
008600DA  49 8B CE                        mov rcx, r14
008600DD  E8 7E 83 FE FF                  call 0x140848460
008600E2  E9 8A 00 00 00                  jmp 0x140860171
008600E7  8B 41 18                        mov eax, dword ptr [rcx + 0x18]
008600EA  49 8B D6                        mov rdx, r14
008600ED  4C 8B 4D E0                     mov r9, qword ptr [rbp - 0x20]
008600F1  48 8D 4C 24 64                  lea rcx, [rsp + 0x64]
008600F6  4C 8B 44 24 68                  mov r8, qword ptr [rsp + 0x68]
008600FB  48 89 4C 24 40                  mov qword ptr [rsp + 0x40], rcx
00860100  48 8D 4C 24 77                  lea rcx, [rsp + 0x77]
00860105  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
0086010A  48 8B 4D 80                     mov rcx, qword ptr [rbp - 0x80]
0086010E  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
00860113  48 8B 4D D0                     mov rcx, qword ptr [rbp - 0x30]
00860117  C1 E8 02                        shr eax, 2
0086011A  24 01                           and al, 1
0086011C  88 44 24 28                     mov byte ptr [rsp + 0x28], al
00860120  0F B6 44 24 72                  movzx eax, byte ptr [rsp + 0x72]
00860125  88 44 24 20                     mov byte ptr [rsp + 0x20], al
00860129  E8 D2 FE 00 00                  call 0x140870000
0086012E  84 C0                           test al, al
00860130  0F 85 E1 07 00 00               jne 0x140860917
00860136  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
0086013B  40 38 74 24 77                  cmp byte ptr [rsp + 0x77], sil
00860140  0F 85 CB 1C 00 00               jne 0x140861e11
00860146  44 8B 44 24 64                  mov r8d, dword ptr [rsp + 0x64]
0086014B  BA E0 3C 00 00                  mov edx, 0x3ce0
00860150  48 8B CF                        mov rcx, rdi
00860153  E8 28 11 FF FF                  call 0x140851280
00860158  40 38 74 24 7C                  cmp byte ptr [rsp + 0x7c], sil
0086015D  0F 85 D8 19 00 00               jne 0x140861b3b
00860163  0F B6 5C 24 60                  movzx ebx, byte ptr [rsp + 0x60]
00860168  45 84 E4                        test r12b, r12b
0086016B  0F 85 69 FF FF FF               jne 0x1408600da
00860171  44 0F B6 74 24 74               movzx r14d, byte ptr [rsp + 0x74]
00860177  84 DB                           test bl, bl
00860179  74 6E                           je 0x1408601e9
0086017B  4C 8B 65 A8                     mov r12, qword ptr [rbp - 0x58]
0086017F  0F B7 DE                        movzx ebx, si
00860182  66 41 3B 74 24 02               cmp si, word ptr [r12 + 2]
00860188  7F 5F                           jg 0x1408601e9
0086018A  0F B6 7C 24 71                  movzx edi, byte ptr [rsp + 0x71]
0086018F  44 0F B6 6C 24 73               movzx r13d, byte ptr [rsp + 0x73]
00860195  0F B6 74 24 61                  movzx esi, byte ptr [rsp + 0x61]
0086019A  66 0F 1F 44 00 00               nop word ptr [rax + rax]
008601A0  48 8B 45 C8                     mov rax, qword ptr [rbp - 0x38]
008601A4  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
008601A8  48 0F BF CB                     movsx rcx, bx
008601AC  66 83 FB 02                     cmp bx, 2
008601B0  0F 8D AB 04 00 00               jge 0x140860661
008601B6  49 8B 4C CC 08                  mov rcx, qword ptr [r12 + rcx*8 + 8]
008601BB  E8 00 91 36 00                  call 0x140bc92c0
008601C0  66 FF C3                        inc bx
008601C3  66 41 3B 5C 24 02               cmp bx, word ptr [r12 + 2]
008601C9  7E D5                           jle 0x1408601a0
008601CB  48 8B 45 C8                     mov rax, qword ptr [rbp - 0x38]
008601CF  40 88 74 24 61                  mov byte ptr [rsp + 0x61], sil
008601D4  33 F6                           xor esi, esi
008601D6  40 88 7C 24 71                  mov byte ptr [rsp + 0x71], dil
008601DB  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
008601E0  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
008601E4  44 88 6C 24 73                  mov byte ptr [rsp + 0x73], r13b
008601E9  4C 8B 6D 90                     mov r13, qword ptr [rbp - 0x70]
008601ED  48 8B 5D B0                     mov rbx, qword ptr [rbp - 0x50]
008601F1  80 7C 24 73 00                  cmp byte ptr [rsp + 0x73], 0
008601F6  74 09                           je 0x140860201
008601F8  48 8B 4B 08                     mov rcx, qword ptr [rbx + 8]
008601FC  E8 BF 90 36 00                  call 0x140bc92c0
00860201  45 84 F6                        test r14b, r14b
00860204  0F 85 B3 0B 00 00               jne 0x140860dbd
0086020A  44 0F B6 64 24 61               movzx r12d, byte ptr [rsp + 0x61]
00860210  E9 3F 02 00 00                  jmp 0x140860454
00860215  40 38 35 28 F9 68 00            cmp byte ptr [rip + 0x68f928], sil
0086021C  0F 84 1A FE FF FF               je 0x14086003c
00860222  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0086022B  48 39 05 16 F9 68 00            cmp qword ptr [rip + 0x68f916], rax
00860232  4C 8B 65 A0                     mov r12, qword ptr [rbp - 0x60]
00860236  4C 89 65 90                     mov qword ptr [rbp - 0x70], r12
0086023A  0F 84 87 00 00 00               je 0x1408602c7
00860240  48 8B 05 49 98 77 00            mov rax, qword ptr [rip + 0x779849]
00860247  49 39 44 24 20                  cmp qword ptr [r12 + 0x20], rax
0086024C  75 79                           jne 0x1408602c7
0086024E  41 8B 44 24 08                  mov eax, dword ptr [r12 + 8]
00860253  25 00 00 E0 7F                  and eax, 0x7fe00000
00860258  3D 00 00 60 00                  cmp eax, 0x600000
0086025D  75 2F                           jne 0x14086028e
0086025F  66 85 DB                        test bx, bx
00860262  7E 2A                           jle 0x14086028e
00860264  48 8B 4D C0                     mov rcx, qword ptr [rbp - 0x40]
00860268  0F BF D3                        movsx edx, bx
0086026B  FF CA                           dec edx
0086026D  E8 DE 77 14 00                  call 0x1409a7a50
00860272  4C 8B 4C 24 68                  mov r9, qword ptr [rsp + 0x68]
00860277  48 8B C8                        mov rcx, rax
0086027A  49 81 C1 88 00 00 00            add r9, 0x88
00860281  E8 9E B2 26 00                  call 0x140acb524
00860286  84 C0                           test al, al
00860288  0F 85 07 17 00 00               jne 0x140861995
0086028E  41 8B 44 24 08                  mov eax, dword ptr [r12 + 8]
00860293  25 00 00 E0 7F                  and eax, 0x7fe00000
00860298  3D 00 00 40 00                  cmp eax, 0x400000
0086029D  75 28                           jne 0x1408602c7
0086029F  48 8B 4D C0                     mov rcx, qword ptr [rbp - 0x40]
008602A3  0F BF D3                        movsx edx, bx
008602A6  E8 A5 77 14 00                  call 0x1409a7a50
008602AB  4C 8B 4C 24 68                  mov r9, qword ptr [rsp + 0x68]
008602B0  48 8B C8                        mov rcx, rax
008602B3  49 81 C1 88 00 00 00            add r9, 0x88
008602BA  E8 65 B2 26 00                  call 0x140acb524
008602BF  84 C0                           test al, al
008602C1  0F 85 D5 16 00 00               jne 0x14086199c
008602C7  48 8B 45 B8                     mov rax, qword ptr [rbp - 0x48]
008602CB  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
008602CF  E9 68 FD FF FF                  jmp 0x14086003c
008602D4  8D 41 F8                        lea eax, [rcx - 8]
008602D7  48 83 C0 06                     add rax, 6
008602DB  48 C1 E0 04                     shl rax, 4
008602DF  49 03 85 A0 00 00 00            add rax, qword ptr [r13 + 0xa0]
008602E6  E9 80 FA FF FF                  jmp 0x14085fd6b
008602EB  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
008602F0  48 8D 4D 08                     lea rcx, [rbp + 8]
008602F4  44 0F B7 4D 88                  movzx r9d, word ptr [rbp - 0x78]
008602F9  44 0F B7 C3                     movzx r8d, bx
008602FD  48 89 4C 24 48                  mov qword ptr [rsp + 0x48], rcx
00860302  49 8B CE                        mov rcx, r14
00860305  48 8D 47 58                     lea rax, [rdi + 0x58]
00860309  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
0086030E  48 8D 97 D8 00 00 00            lea rdx, [rdi + 0xd8]
00860315  48 8B 45 E8                     mov rax, qword ptr [rbp - 0x18]
00860319  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0086031E  48 8D 45 28                     lea rax, [rbp + 0x28]
00860322  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00860327  48 89 7C 24 28                  mov qword ptr [rsp + 0x28], rdi
0086032C  4C 89 54 24 20                  mov qword ptr [rsp + 0x20], r10
00860331  E8 6A 6D FF FF                  call 0x1408570a0
00860336  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
0086033A  85 C0                           test eax, eax
0086033C  0F 88 7D 16 00 00               js 0x1408619bf
00860342  83 27 F7                        and dword ptr [rdi], 0xfffffff7
00860345  48 39 77 40                     cmp qword ptr [rdi + 0x40], rsi
00860349  75 16                           jne 0x140860361
0086034B  48 8B 45 08                     mov rax, qword ptr [rbp + 8]
0086034F  48 8B 48 20                     mov rcx, qword ptr [rax + 0x20]
00860353  8B 81 10 10 00 00               mov eax, dword ptr [rcx + 0x1010]
00860359  A8 01                           test al, 1
0086035B  74 04                           je 0x140860361
0086035D  48 89 4F 40                     mov qword ptr [rdi + 0x40], rcx
00860361  0F B6 87 AA 01 00 00            movzx eax, byte ptr [rdi + 0x1aa]
00860368  4C 8B 6D 90                     mov r13, qword ptr [rbp - 0x70]
0086036C  44 0F B6 64 24 61               movzx r12d, byte ptr [rsp + 0x61]
00860372  C7 44 24 64 04 01 00 00         mov dword ptr [rsp + 0x64], 0x104
0086037A  3C 04                           cmp al, 4
0086037C  0F 83 D2 00 00 00               jae 0x140860454
00860382  C7 84 C7 AC 01 00 00 04 01 00 00  mov dword ptr [rdi + rax*8 + 0x1ac], 0x104
0086038D  0F B6 87 AA 01 00 00            movzx eax, byte ptr [rdi + 0x1aa]
00860394  C7 84 C7 B0 01 00 00 00 13 00 00  mov dword ptr [rdi + rax*8 + 0x1b0], 0x1300
0086039F  FE 87 AA 01 00 00               inc byte ptr [rdi + 0x1aa]
008603A5  E9 AA 00 00 00                  jmp 0x140860454
008603AA  E8 75 E0 FE FF                  call 0x14084e424
008603AF  E8 2C 5F BD FF                  call 0x1404362e0
008603B4  84 C0                           test al, al
008603B6  74 7A                           je 0x140860432
008603B8  8B 15 9A 9B 5A 00               mov edx, dword ptr [rip + 0x5a9b9a]
008603BE  83 FA 05                        cmp edx, 5
008603C1  76 6F                           jbe 0x140860432
008603C3  49 B8 00 00 01 00 00 20 00 00   movabs r8, 0x200000010000
008603CD  4C 85 05 94 9B 5A 00            test qword ptr [rip + 0x5a9b94], r8
008603D4  0F 85 04 14 00 00               jne 0x1408617de
008603DA  32 C0                           xor al, al
008603DC  84 C0                           test al, al
008603DE  74 49                           je 0x140860429
008603E0  48 8D 45 20                     lea rax, [rbp + 0x20]
008603E4  48 C7 45 20 00 00 00 01         mov qword ptr [rbp + 0x20], 0x1000000
008603EC  48 89 85 F0 00 00 00            mov qword ptr [rbp + 0xf0], rax
008603F3  48 8D 15 2E 5F 7F FF            lea rdx, [rip - 0x80a0d2]
008603FA  48 8D 85 D0 00 00 00            lea rax, [rbp + 0xd0]
00860401  48 C7 85 F8 00 00 00 08 00 00 00  mov qword ptr [rbp + 0xf8], 8
0086040C  41 B9 03 00 00 00               mov r9d, 3
00860412  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00860417  48 8D 0D 3A 9B 5A 00            lea rcx, [rip + 0x5a9b3a]
0086041E  E8 59 0B A9 FF                  call 0x1402f0f7c
00860423  8B 15 2F 9B 5A 00               mov edx, dword ptr [rip + 0x5a9b2f]
00860429  83 FA 05                        cmp edx, 5
0086042C  0F 87 CA 13 00 00               ja 0x1408617fc
00860432  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
00860437  44 0F B6 64 24 61               movzx r12d, byte ptr [rsp + 0x61]
0086043D  C7 44 24 64 22 00 00 C0         mov dword ptr [rsp + 0x64], 0xc0000022
00860445  0F B6 87 AA 01 00 00            movzx eax, byte ptr [rdi + 0x1aa]
0086044C  3C 04                           cmp al, 4
0086044E  0F 82 F6 14 00 00               jb 0x14086194a
00860454  80 7C 24 70 00                  cmp byte ptr [rsp + 0x70], 0
00860459  4C 8B 75 C8                     mov r14, qword ptr [rbp - 0x38]
0086045D  0F 85 6B 01 00 00               jne 0x1408605ce
00860463  80 7C 24 71 00                  cmp byte ptr [rsp + 0x71], 0
00860468  0F 85 42 09 00 00               jne 0x140860db0
0086046E  48 8B 4D 58                     mov rcx, qword ptr [rbp + 0x58]
00860472  48 85 C9                        test rcx, rcx
00860475  74 05                           je 0x14086047c
00860477  E8 04 59 C1 FF                  call 0x140475d80
0086047C  48 8B 4D 78                     mov rcx, qword ptr [rbp + 0x78]
00860480  48 85 C9                        test rcx, rcx
00860483  74 05                           je 0x14086048a
00860485  E8 F6 58 C1 FF                  call 0x140475d80
0086048A  48 8B 8D 98 00 00 00            mov rcx, qword ptr [rbp + 0x98]
00860491  48 85 C9                        test rcx, rcx
00860494  74 05                           je 0x14086049b
00860496  E8 E5 58 C1 FF                  call 0x140475d80
0086049B  48 8B 5D 18                     mov rbx, qword ptr [rbp + 0x18]
0086049F  48 85 DB                        test rbx, rbx
008604A2  0F 85 F8 08 00 00               jne 0x140860da0
008604A8  4D 85 ED                        test r13, r13
008604AB  74 08                           je 0x1408604b5
008604AD  49 8B CD                        mov rcx, r13
008604B0  E8 5B 0E FF FF                  call 0x140851310
008604B5  4D 85 FF                        test r15, r15
008604B8  74 08                           je 0x1408604c2
008604BA  49 8B CF                        mov rcx, r15
008604BD  E8 4E 0E FF FF                  call 0x140851310
008604C2  8B 47 64                        mov eax, dword ptr [rdi + 0x64]
008604C5  4D 8B EE                        mov r13, r14
008604C8  85 C0                           test eax, eax
008604CA  0F 84 4E 06 00 00               je 0x140860b1e
008604D0  44 88 64 24 61                  mov byte ptr [rsp + 0x61], r12b
008604D5  A8 02                           test al, 2
008604D7  0F 84 41 06 00 00               je 0x140860b1e
008604DD  4C 8B 7F 70                     mov r15, qword ptr [rdi + 0x70]
008604E1  48 8D 8D 80 00 00 00            lea rcx, [rbp + 0x80]
008604E8  0F 57 C0                        xorps xmm0, xmm0
008604EB  0F 11 85 80 00 00 00            movups xmmword ptr [rbp + 0x80], xmm0
008604F2  49 8B BF 70 06 00 00            mov rdi, qword ptr [r15 + 0x670]
008604F9  41 8B 9F 78 06 00 00            mov ebx, dword ptr [r15 + 0x678]
00860500  48 89 7D 38                     mov qword ptr [rbp + 0x38], rdi
00860504  89 5C 24 78                     mov dword ptr [rsp + 0x78], ebx
00860508  0F 11 85 90 00 00 00            movups xmmword ptr [rbp + 0x90], xmm0
0086050F  0F 11 85 A0 00 00 00            movups xmmword ptr [rbp + 0xa0], xmm0
00860516  E8 C5 93 36 00                  call 0x140bc98e0
0086051B  44 88 64 24 61                  mov byte ptr [rsp + 0x61], r12b
00860520  3B F3                           cmp esi, ebx
00860522  0F 83 DE 05 00 00               jae 0x140860b06
00860528  8B D6                           mov edx, esi
0086052A  49 8B CF                        mov rcx, r15
0086052D  E8 5E 0D F9 FF                  call 0x1407f1290
00860532  8B C6                           mov eax, esi
00860534  48 8D 0C 40                     lea rcx, [rax + rax*2]
00860538  4C 8D 24 CF                     lea r12, [rdi + rcx*8]
0086053C  49 8D 7C 24 10                  lea rdi, [r12 + 0x10]
00860541  48 8B 07                        mov rax, qword ptr [rdi]
00860544  48 85 C0                        test rax, rax
00860547  74 30                           je 0x140860579
00860549  48 8D 58 F0                     lea rbx, [rax - 0x10]
0086054D  48 8B CB                        mov rcx, rbx
00860550  E8 5B 19 00 00                  call 0x140861eb0
00860555  48 83 3B 00                     cmp qword ptr [rbx], 0
00860559  48 8B CB                        mov rcx, rbx
0086055C  75 31                           jne 0x14086058f
0086055E  E8 ED 1D 00 00                  call 0x140862350
00860563  48 8D 55 28                     lea rdx, [rbp + 0x28]
00860567  48 8B CB                        mov rcx, rbx
0086056A  E8 B1 19 00 00                  call 0x140861f20
0086056F  48 8B CB                        mov rcx, rbx
00860572  E8 49 8D 36 00                  call 0x140bc92c0
00860577  EB C3                           jmp 0x14086053c
00860579  8B D6                           mov edx, esi
0086057B  49 8B CF                        mov rcx, r15
0086057E  E8 DD 1E 00 00                  call 0x140862460
00860583  8B 5C 24 78                     mov ebx, dword ptr [rsp + 0x78]
00860587  FF C6                           inc esi
00860589  48 8B 7D 38                     mov rdi, qword ptr [rbp + 0x38]
0086058D  EB 91                           jmp 0x140860520
0086058F  4C 8B 6B 18                     mov r13, qword ptr [rbx + 0x18]
00860593  4C 8D 45 28                     lea r8, [rbp + 0x28]
00860597  45 33 C9                        xor r9d, r9d
0086059A  49 8B D7                        mov rdx, r15
0086059D  E8 AE B7 F8 FF                  call 0x1407ebd50
008605A2  48 8B CB                        mov rcx, rbx
008605A5  83 F8 01                        cmp eax, 1
008605A8  0F 84 B0 18 00 00               je 0x140861e5e
008605AE  83 F8 03                        cmp eax, 3
008605B1  0F 84 A7 18 00 00               je 0x140861e5e
008605B7  83 F8 02                        cmp eax, 2
008605BA  0F 84 91 18 00 00               je 0x140861e51
008605C0  48 8D 7B 18                     lea rdi, [rbx + 0x18]
008605C4  E8 F7 8C 36 00                  call 0x140bc92c0
008605C9  E9 73 FF FF FF                  jmp 0x140860541
008605CE  49 8B CD                        mov rcx, r13
008605D1  E8 9A 3D 00 00                  call 0x140864370
008605D6  E9 88 FE FF FF                  jmp 0x140860463
008605DB  4D 8B 4E 08                     mov r9, qword ptr [r14 + 8]
008605DF  41 B8 20 00 00 00               mov r8d, 0x20
008605E5  48 8D 55 F0                     lea rdx, [rbp - 0x10]
008605E9  49 8D 89 D0 00 00 00            lea rcx, [r9 + 0xd0]
008605F0  E8 4B 93 36 00                  call 0x140bc9940
008605F5  48 85 C0                        test rax, rax
008605F8  0F 84 95 F9 FF FF               je 0x14085ff93
008605FE  83 78 44 02                     cmp dword ptr [rax + 0x44], 2
00860602  75 DB                           jne 0x1408605df
00860604  48 8B 48 38                     mov rcx, qword ptr [rax + 0x38]
00860608  49 8B D2                        mov rdx, r10
0086060B  E8 50 B9 FE FF                  call 0x14084bf60
00860610  84 C0                           test al, al
00860612  0F 85 93 FA FF FF               jne 0x1408600ab
00860618  4C 8B 55 80                     mov r10, qword ptr [rbp - 0x80]
0086061C  E9 72 F9 FF FF                  jmp 0x14085ff93
00860621  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
00860626  B8 71 02 00 C0                  mov eax, 0xc0000271
0086062B  E9 04 F5 FF FF                  jmp 0x14085fb34
00860630  45 32 F6                        xor r14b, r14b
00860633  E9 81 F7 FF FF                  jmp 0x14085fdb9
00860638  49 8B CF                        mov rcx, r15
0086063B  E8 D0 0C FF FF                  call 0x140851310
00860640  4C 8B FE                        mov r15, rsi
00860643  E8 3C 94 36 00                  call 0x140bc9a84
00860648  48 8B 45 B8                     mov rax, qword ptr [rbp - 0x48]
0086064C  45 32 F6                        xor r14b, r14b
0086064F  4C 8B 6D A0                     mov r13, qword ptr [rbp - 0x60]
00860653  44 8B 64 24 78                  mov r12d, dword ptr [rsp + 0x78]
00860658  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
0086065C  E9 EC F2 FF FF                  jmp 0x14085f94d
00860661  49 8B 44 24 18                  mov rax, qword ptr [r12 + 0x18]
00860666  48 8B 4C C8 F0                  mov rcx, qword ptr [rax + rcx*8 - 0x10]
0086066B  E9 4B FB FF FF                  jmp 0x1408601bb
00860670  41 09 07                        or dword ptr [r15], eax
00860673  E9 7E F2 FF FF                  jmp 0x14085f8f6
00860678  83 C0 F8                        add eax, -8
0086067B  8B C8                           mov ecx, eax
0086067D  48 8B 45 C0                     mov rax, qword ptr [rbp - 0x40]
00860681  48 C1 E1 04                     shl rcx, 4
00860685  48 8B 80 A0 00 00 00            mov rax, qword ptr [rax + 0xa0]
0086068C  48 83 C0 68                     add rax, 0x68
00860690  E9 49 F5 FF FF                  jmp 0x14085fbde
00860695  48 8B 4D C0                     mov rcx, qword ptr [rbp - 0x40]
00860699  45 8D 41 F8                     lea r8d, [r9 - 8]
0086069D  49 83 C0 06                     add r8, 6
008606A1  41 8D 41 F8                     lea eax, [r9 - 8]
008606A5  49 C1 E0 04                     shl r8, 4
008606A9  4C 03 81 A0 00 00 00            add r8, qword ptr [rcx + 0xa0]
008606B0  48 8B 89 A0 00 00 00            mov rcx, qword ptr [rcx + 0xa0]
008606B7  8B 0C 81                        mov ecx, dword ptr [rcx + rax*4]
008606BA  E9 10 F9 FF FF                  jmp 0x14085ffcf
008606BF  49 8B CF                        mov rcx, r15
008606C2  E8 F9 8B 36 00                  call 0x140bc92c0
008606C7  45 84 F6                        test r14b, r14b
008606CA  0F 85 5A 03 00 00               jne 0x140860a2a
008606D0  49 8B CF                        mov rcx, r15
008606D3  E8 38 0C FF FF                  call 0x140851310
008606D8  41 0F 10 04 24                  movups xmm0, xmmword ptr [r12]
008606DD  0F B7 C6                        movzx eax, si
008606E0  49 8B CD                        mov rcx, r13
008606E3  4C 8B FE                        mov r15, rsi
008606E6  89 44 24 78                     mov dword ptr [rsp + 0x78], eax
008606EA  0F 11 45 F8                     movups xmmword ptr [rbp - 8], xmm0
008606EE  E8 DD EF FF FF                  call 0x14085f6d0
008606F3  33 D2                           xor edx, edx
008606F5  41 B8 A8 00 00 00               mov r8d, 0xa8
008606FB  49 8B CD                        mov rcx, r13
008606FE  E8 3D 65 E6 FF                  call 0x1406c6c40
00860703  48 8B 45 B8                     mov rax, qword ptr [rbp - 0x48]
00860707  4C 8B 6D A0                     mov r13, qword ptr [rbp - 0x60]
0086070B  44 8B 64 24 78                  mov r12d, dword ptr [rsp + 0x78]
00860710  48 8B 7D B0                     mov rdi, qword ptr [rbp - 0x50]
00860714  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
00860718  44 88 74 24 75                  mov byte ptr [rsp + 0x75], r14b
0086071D  E9 35 F2 FF FF                  jmp 0x14085f957
00860722  4C 8B 6D 90                     mov r13, qword ptr [rbp - 0x70]
00860726  4C 8B E7                        mov r12, rdi
00860729  48 89 7D A8                     mov qword ptr [rbp - 0x58], rdi
0086072D  49 8B 55 48                     mov rdx, qword ptr [r13 + 0x48]
00860731  48 85 D2                        test rdx, rdx
00860734  0F 84 98 10 00 00               je 0x1408617d2
0086073A  48 8B CF                        mov rcx, rdi
0086073D  E8 0E 1E FE FF                  call 0x140842550
00860742  48 8B 7D B0                     mov rdi, qword ptr [rbp - 0x50]
00860746  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
0086074A  49 39 4D 48                     cmp qword ptr [r13 + 0x48], rcx
0086074E  0F 84 7D 03 00 00               je 0x140860ad1
00860754  4C 3B E9                        cmp r13, rcx
00860757  0F 84 74 03 00 00               je 0x140860ad1
0086075D  E8 BA 92 36 00                  call 0x140bc9a1c
00860762  B3 01                           mov bl, 1
00860764  88 5C 24 73                     mov byte ptr [rsp + 0x73], bl
00860768  4D 85 E4                        test r12, r12
0086076B  74 0D                           je 0x14086077a
0086076D  49 8B CC                        mov rcx, r12
00860770  E8 8B 78 0E 00                  call 0x140948000
00860775  C6 44 24 60 01                  mov byte ptr [rsp + 0x60], 1
0086077A  49 8B CE                        mov rcx, r14
0086077D  E8 7E 78 0E 00                  call 0x140948000
00860782  33 D2                           xor edx, edx
00860784  48 8B CF                        mov rcx, rdi
00860787  41 B4 01                        mov r12b, 1
0086078A  E8 F1 8C 36 00                  call 0x140bc9480
0086078F  84 C0                           test al, al
00860791  0F 85 42 12 00 00               jne 0x1408619d9
00860797  41 F7 45 08 00 00 02 00         test dword ptr [r13 + 8], 0x20000
0086079F  0F 85 68 12 00 00               jne 0x140861a0d
008607A5  8B 7C 24 78                     mov edi, dword ptr [rsp + 0x78]
008607A9  66 FF CF                        dec di
008607AC  41 F7 85 B8 00 00 00 00 00 02 00  test dword ptr [r13 + 0xb8], 0x20000
008607B7  89 7C 24 78                     mov dword ptr [rsp + 0x78], edi
008607BB  0F 85 7A 12 00 00               jne 0x140861a3b
008607C1  48 8B 55 80                     mov rdx, qword ptr [rbp - 0x80]
008607C5  49 8B CE                        mov rcx, r14
008607C8  E8 A3 7C 14 00                  call 0x1409a8470
008607CD  84 C0                           test al, al
008607CF  0F 84 6D 12 00 00               je 0x140861a42
008607D5  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
008607DA  49 8B CE                        mov rcx, r14
008607DD  8B 00                           mov eax, dword ptr [rax]
008607DF  A8 02                           test al, 2
008607E1  0F 85 76 0C 00 00               jne 0x14086145d
008607E7  A8 20                           test al, 0x20
008607E9  0F 85 F1 03 00 00               jne 0x140860be0
008607EF  48 8B 55 80                     mov rdx, qword ptr [rbp - 0x80]
008607F3  E8 E8 1E FE FF                  call 0x1408426e0
008607F8  84 C0                           test al, al
008607FA  0F 85 74 07 00 00               jne 0x140860f74
00860800  49 8B CE                        mov rcx, r14
00860803  E8 D8 84 14 00                  call 0x1409a8ce0
00860808  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
0086080D  84 C0                           test al, al
0086080F  0F 85 79 06 00 00               jne 0x140860e8e
00860815  40 38 75 99                     cmp byte ptr [rbp - 0x67], sil
00860819  0F 85 77 15 00 00               jne 0x140861d96
0086081F  41 F7 85 B8 00 00 00 00 00 02 00  test dword ptr [r13 + 0xb8], 0x20000
0086082A  0F 85 7C 15 00 00               jne 0x140861dac
00860830  8B 47 18                        mov eax, dword ptr [rdi + 0x18]
00860833  A8 02                           test al, 2
00860835  0F 85 89 15 00 00               jne 0x140861dc4
0086083B  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
00860840  45 33 C9                        xor r9d, r9d
00860843  48 8B 7D E8                     mov rdi, qword ptr [rbp - 0x18]
00860847  49 8B D6                        mov rdx, r14
0086084A  48 8B 5D A8                     mov rbx, qword ptr [rbp - 0x58]
0086084E  49 8B CD                        mov rcx, r13
00860851  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
00860856  4C 8B C3                        mov r8, rbx
00860859  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0086085E  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
00860863  E8 08 A4 0E 00                  call 0x14094ac70
00860868  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
0086086C  3D 71 02 00 C0                  cmp eax, 0xc0000271
00860871  0F 85 B2 11 00 00               jne 0x140861a29
00860877  48 8B 45 E0                     mov rax, qword ptr [rbp - 0x20]
0086087B  4C 8B CF                        mov r9, rdi
0086087E  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
00860883  48 83 C0 20                     add rax, 0x20
00860887  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0086088C  45 33 C0                        xor r8d, r8d
0086088F  0F B6 44 24 72                  movzx eax, byte ptr [rsp + 0x72]
00860894  48 8B D7                        mov rdx, rdi
00860897  49 8B CD                        mov rcx, r13
0086089A  88 44 24 20                     mov byte ptr [rsp + 0x20], al
0086089E  E8 ED 44 FF FF                  call 0x140854d90
008608A3  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
008608A7  3D 71 02 00 C0                  cmp eax, 0xc0000271
008608AC  0F 85 2A 15 00 00               jne 0x140861ddc
008608B2  4C 8B 4D 80                     mov r9, qword ptr [rbp - 0x80]
008608B6  48 8D 44 24 76                  lea rax, [rsp + 0x76]
008608BB  0F B6 54 24 72                  movzx edx, byte ptr [rsp + 0x72]
008608C0  4C 8B C7                        mov r8, rdi
008608C3  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
008608C8  49 8B CD                        mov rcx, r13
008608CB  48 8D 45 D0                     lea rax, [rbp - 0x30]
008608CF  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
008608D4  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
008608D9  C7 44 24 20 02 00 00 00         mov dword ptr [rsp + 0x20], 2
008608E1  E8 2A 33 06 00                  call 0x1408c3c10
008608E6  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
008608EA  44 8B C0                        mov r8d, eax
008608ED  85 C0                           test eax, eax
008608EF  0F 88 F4 14 00 00               js 0x140861de9
008608F5  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
008608FA  40 32 FF                        xor dil, dil
008608FD  83 79 20 01                     cmp dword ptr [rcx + 0x20], 1
00860901  0F 85 E0 F7 FF FF               jne 0x1408600e7
00860907  48 8B 55 D0                     mov rdx, qword ptr [rbp - 0x30]
0086090B  48 8B 42 08                     mov rax, qword ptr [rdx + 8]
0086090F  0F B7 48 42                     movzx ecx, word ptr [rax + 0x42]
00860913  66 89 4A 04                     mov word ptr [rdx + 4], cx
00860917  48 8B 45 D0                     mov rax, qword ptr [rbp - 0x30]
0086091B  48 8B 4D 38                     mov rcx, qword ptr [rbp + 0x38]
0086091F  48 89 75 D0                     mov qword ptr [rbp - 0x30], rsi
00860923  48 89 01                        mov qword ptr [rcx], rax
00860926  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
0086092B  39 70 20                        cmp dword ptr [rax + 0x20], esi
0086092E  75 07                           jne 0x140860937
00860930  C7 40 20 02 00 00 00            mov dword ptr [rax + 0x20], 2
00860937  40 38 74 24 76                  cmp byte ptr [rsp + 0x76], sil
0086093C  0F 85 F5 14 00 00               jne 0x140861e37
00860942  89 74 24 64                     mov dword ptr [rsp + 0x64], esi
00860946  0F B6 44 24 60                  movzx eax, byte ptr [rsp + 0x60]
0086094B  88 44 24 60                     mov byte ptr [rsp + 0x60], al
0086094F  0F B6 44 24 7C                  movzx eax, byte ptr [rsp + 0x7c]
00860954  88 44 24 7C                     mov byte ptr [rsp + 0x7c], al
00860958  0F B6 44 24 73                  movzx eax, byte ptr [rsp + 0x73]
0086095D  88 44 24 73                     mov byte ptr [rsp + 0x73], al
00860961  0F B6 44 24 71                  movzx eax, byte ptr [rsp + 0x71]
00860966  88 44 24 71                     mov byte ptr [rsp + 0x71], al
0086096A  48 89 5D A8                     mov qword ptr [rbp - 0x58], rbx
0086096E  40 88 7C 24 74                  mov byte ptr [rsp + 0x74], dil
00860973  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
00860978  E9 DB F7 FF FF                  jmp 0x140860158
0086097D  E8 1E 44 01 00                  call 0x140874da0
00860982  48 89 7D 90                     mov qword ptr [rbp - 0x70], rdi
00860986  4C 8B EF                        mov r13, rdi
00860989  48 89 7D A0                     mov qword ptr [rbp - 0x60], rdi
0086098D  49 3B FF                        cmp rdi, r15
00860990  0F 85 E3 01 00 00               jne 0x140860b79
00860996  0F B6 44 24 75                  movzx eax, byte ptr [rsp + 0x75]
0086099B  40 88 74 24 71                  mov byte ptr [rsp + 0x71], sil
008609A0  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
008609A5  88 44 24 70                     mov byte ptr [rsp + 0x70], al
008609A9  E9 04 F1 FF FF                  jmp 0x14085fab2
008609AE  48 8B C6                        mov rax, rsi
008609B1  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
008609B5  48 89 45 B8                     mov qword ptr [rbp - 0x48], rax
008609B9  E9 E5 F4 FF FF                  jmp 0x14085fea3
008609BE  48 8B 05 CB 90 77 00            mov rax, qword ptr [rip + 0x7790cb]
008609C5  49 39 45 20                     cmp qword ptr [r13 + 0x20], rax
008609C9  0F 84 A3 0F 00 00               je 0x140861972
008609CF  48 85 DB                        test rbx, rbx
008609D2  75 09                           jne 0x1408609dd
008609D4  48 85 FF                        test rdi, rdi
008609D7  0F 84 45 F4 FF FF               je 0x14085fe22
008609DD  66 41 39 75 42                  cmp word ptr [r13 + 0x42], si
008609E2  0F 84 3A F4 FF FF               je 0x14085fe22
008609E8  B9 08 00 00 00                  mov ecx, 8
008609ED  E8 4E E0 14 00                  call 0x1409aea40
008609F2  E8 E9 58 BD FF                  call 0x1404362e0
008609F7  84 C0                           test al, al
008609F9  0F 85 77 0F 00 00               jne 0x140861976
008609FF  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
00860A04  BA 00 0B 00 00                  mov edx, 0xb00
00860A09  48 8B CF                        mov rcx, rdi
00860A0C  C7 44 24 64 05 00 19 C0         mov dword ptr [rsp + 0x64], 0xc0190005
00860A14  41 B8 05 00 19 C0               mov r8d, 0xc0190005
00860A1A  E8 61 08 FF FF                  call 0x140851280
00860A1F  44 0F B6 64 24 61               movzx r12d, byte ptr [rsp + 0x61]
00860A25  E9 2A FA FF FF                  jmp 0x140860454
00860A2A  49 8B CF                        mov rcx, r15
00860A2D  E8 3E 39 00 00                  call 0x140864370
00860A32  45 32 F6                        xor r14b, r14b
00860A35  44 88 74 24 71                  mov byte ptr [rsp + 0x71], r14b
00860A3A  E9 91 FC FF FF                  jmp 0x1408606d0
00860A3F  B2 01                           mov dl, 1
00860A41  E9 AD F5 FF FF                  jmp 0x14085fff3
00860A46  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
00860A4A  48 8B 4C C8 F0                  mov rcx, qword ptr [rax + rcx*8 - 0x10]
00860A4F  E9 18 F5 FF FF                  jmp 0x14085ff6c
00860A54  40 38 74 24 70                  cmp byte ptr [rsp + 0x70], sil
00860A59  74 0D                           je 0x140860a68
00860A5B  49 8B CD                        mov rcx, r13
00860A5E  E8 0D 39 00 00                  call 0x140864370
00860A63  40 88 74 24 70                  mov byte ptr [rsp + 0x70], sil
00860A68  E8 17 90 36 00                  call 0x140bc9a84
00860A6D  49 8B 4D 20                     mov rcx, qword ptr [r13 + 0x20]
00860A71  48 85 C9                        test rcx, rcx
00860A74  0F 84 B3 09 00 00               je 0x14086142d
00860A7A  F6 C3 01                        test bl, 1
00860A7D  0F 84 B4 09 00 00               je 0x140861437
00860A83  48 8B D1                        mov rdx, rcx
00860A86  4C 8D 4D B8                     lea r9, [rbp - 0x48]
00860A8A  48 8B CB                        mov rcx, rbx
00860A8D  41 B8 01 00 00 00               mov r8d, 1
00860A93  E8 FC 29 01 00                  call 0x140873494
00860A98  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
00860A9C  E8 93 90 36 00                  call 0x140bc9b34
00860AA1  44 8B 44 24 64                  mov r8d, dword ptr [rsp + 0x64]
00860AA6  C6 44 24 61 01                  mov byte ptr [rsp + 0x61], 1
00860AAB  45 85 C0                        test r8d, r8d
00860AAE  0F 89 D1 0E 00 00               jns 0x140861985
00860AB4  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
00860AB9  BA 00 0C 00 00                  mov edx, 0xc00
00860ABE  48 8B CF                        mov rcx, rdi
00860AC1  E8 BA 07 FF FF                  call 0x140851280
00860AC6  44 0F B6 64 24 61               movzx r12d, byte ptr [rsp + 0x61]
00860ACC  E9 83 F9 FF FF                  jmp 0x140860454
00860AD1  32 DB                           xor bl, bl
00860AD3  E9 90 FC FF FF                  jmp 0x140860768
00860AD8  48 8B 89 38 10 00 00            mov rcx, qword ptr [rcx + 0x1038]
00860ADF  48 8D 45 B8                     lea rax, [rbp - 0x48]
00860AE3  45 33 C9                        xor r9d, r9d
00860AE6  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00860AEB  4C 8B C7                        mov r8, rdi
00860AEE  48 8B D3                        mov rdx, rbx
00860AF1  E8 46 F7 1F 00                  call 0x140a6023c
00860AF6  44 8B F0                        mov r14d, eax
00860AF9  48 8B 45 B8                     mov rax, qword ptr [rbp - 0x48]
00860AFD  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
00860B01  E9 94 F3 FF FF                  jmp 0x14085fe9a
00860B06  48 8D 8D 80 00 00 00            lea rcx, [rbp + 0x80]
00860B0D  E8 0E 8E 36 00                  call 0x140bc9920
00860B12  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
00860B17  4D 8B EE                        mov r13, r14
00860B1A  83 67 64 FD                     and dword ptr [rdi + 0x64], 0xfffffffd
00860B1E  33 D2                           xor edx, edx
00860B20  48 8D 4D 28                     lea rcx, [rbp + 0x28]
00860B24  E8 77 AE BB FF                  call 0x14041b9a0
00860B29  80 7C 24 61 00                  cmp byte ptr [rsp + 0x61], 0
00860B2E  74 05                           je 0x140860b35
00860B30  E8 4F 8F 36 00                  call 0x140bc9a84
00860B35  4D 85 ED                        test r13, r13
00860B38  75 4E                           jne 0x140860b88
00860B3A  8B 87 A0 00 00 00               mov eax, dword ptr [rdi + 0xa0]
00860B40  A8 01                           test al, 1
00860B42  74 0C                           je 0x140860b50
00860B44  48 8D 8F A8 00 00 00            lea rcx, [rdi + 0xa8]
00860B4B  E8 D0 8D 36 00                  call 0x140bc9920
00860B50  48 8B 55 D0                     mov rdx, qword ptr [rbp - 0x30]
00860B54  48 85 D2                        test rdx, rdx
00860B57  75 16                           jne 0x140860b6f
00860B59  48 8D 8F D8 00 00 00            lea rcx, [rdi + 0xd8]
00860B60  E8 6B EB FF FF                  call 0x14085f6d0
00860B65  8B 44 24 64                     mov eax, dword ptr [rsp + 0x64]
00860B69  E9 04 13 00 00                  jmp 0x140861e72
00860B6E  CC                              int3
00860B6F  48 8B CA                        mov rcx, rdx
00860B72  E8 D9 87 A9 FF                  call 0x1402f9350
00860B77  EB E0                           jmp 0x140860b59
00860B79  48 8B CF                        mov rcx, rdi
00860B7C  E8 53 47 19 00                  call 0x1409f52d4
00860B81  B0 01                           mov al, 1
00860B83  E9 18 FE FF FF                  jmp 0x1408609a0
00860B88  80 7C 24 77 00                  cmp byte ptr [rsp + 0x77], 0
00860B8D  74 14                           je 0x140860ba3
00860B8F  E8 A8 28 14 00                  call 0x1409a343c
00860B94  84 C0                           test al, al
00860B96  74 0B                           je 0x140860ba3
00860B98  49 8B D5                        mov rdx, r13
00860B9B  48 8B CF                        mov rcx, rdi
00860B9E  E8 1D 5F 20 00                  call 0x140a66ac0
00860BA3  BA 43 4D 4E 62                  mov edx, 0x624e4d43
00860BA8  49 8B CD                        mov rcx, r13
00860BAB  E8 30 7E BE FF                  call 0x1404489e0
00860BB0  EB 88                           jmp 0x140860b3a
00860BB2  E8 FD ED FE FF                  call 0x14084f9b4
00860BB7  E9 57 EE FF FF                  jmp 0x14085fa13
00860BBC  48 8B 47 38                     mov rax, qword ptr [rdi + 0x38]
00860BC0  48 85 C0                        test rax, rax
00860BC3  74 09                           je 0x140860bce
00860BC5  48 3B D8                        cmp rbx, rax
00860BC8  0F 85 77 0C 00 00               jne 0x140861845
00860BCE  48 85 DB                        test rbx, rbx
00860BD1  0F 84 3B ED FF FF               je 0x14085f912
00860BD7  48 89 75 F0                     mov qword ptr [rbp - 0x10], rsi
00860BDB  E9 3E ED FF FF                  jmp 0x14085f91e
00860BE0  E8 7B 78 FE FF                  call 0x140848460
00860BE5  48 8B 5D A8                     mov rbx, qword ptr [rbp - 0x58]
00860BE9  48 8B CB                        mov rcx, rbx
00860BEC  E8 6F 78 FE FF                  call 0x140848460
00860BF1  48 8B CB                        mov rcx, rbx
00860BF4  E8 0B 5F FE FF                  call 0x140846b04
00860BF9  49 8B CE                        mov rcx, r14
00860BFC  E8 03 5F FE FF                  call 0x140846b04
00860C01  48 8B 55 80                     mov rdx, qword ptr [rbp - 0x80]
00860C05  48 8B CB                        mov rcx, rbx
00860C08  E8 D3 1A FE FF                  call 0x1408426e0
00860C0D  84 C0                           test al, al
00860C0F  0F 85 7F 0F 00 00               jne 0x140861b94
00860C15  49 8B 45 48                     mov rax, qword ptr [r13 + 0x48]
00860C19  F7 80 B8 00 00 00 00 00 02 00   test dword ptr [rax + 0xb8], 0x20000
00860C23  0F 85 75 0F 00 00               jne 0x140861b9e
00860C29  48 8B 4D C0                     mov rcx, qword ptr [rbp - 0x40]
00860C2D  0F BF D7                        movsx edx, di
00860C30  E8 1B 6E 14 00                  call 0x1409a7a50
00860C35  41 F7 85 B8 00 00 00 00 00 40 00  test dword ptr [r13 + 0xb8], 0x400000
00860C40  48 8B D8                        mov rbx, rax
00860C43  0F 84 C4 03 00 00               je 0x14086100d
00860C49  66 41 83 8D BA 00 00 00 40      or word ptr [r13 + 0xba], 0x40
00860C52  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
00860C57  48 8B 7D 80                     mov rdi, qword ptr [rbp - 0x80]
00860C5B  4C 8B C1                        mov r8, rcx
00860C5E  0F B6 54 24 72                  movzx edx, byte ptr [rsp + 0x72]
00860C63  4C 8B CF                        mov r9, rdi
00860C66  41 C7 45 64 FF FF FF FF         mov dword ptr [r13 + 0x64], 0xffffffff
00860C6E  8B 41 38                        mov eax, dword ptr [rcx + 0x38]
00860C71  49 8B CD                        mov rcx, r13
00860C74  41 89 45 60                     mov dword ptr [r13 + 0x60], eax
00860C78  48 8D 44 24 76                  lea rax, [rsp + 0x76]
00860C7D  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00860C82  48 8D 45 D0                     lea rax, [rbp - 0x30]
00860C86  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00860C8B  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
00860C90  C7 44 24 20 03 00 00 00         mov dword ptr [rsp + 0x20], 3
00860C98  E8 73 2F 06 00                  call 0x1408c3c10
00860C9D  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
00860CA1  85 C0                           test eax, eax
00860CA3  0F 88 FF 0E 00 00               js 0x140861ba8
00860CA9  48 8B D7                        mov rdx, rdi
00860CAC  49 8B CE                        mov rcx, r14
00860CAF  E8 2C 1A FE FF                  call 0x1408426e0
00860CB4  84 C0                           test al, al
00860CB6  0F 84 4B 11 00 00               je 0x140861e07
00860CBC  4C 8B 45 E0                     mov r8, qword ptr [rbp - 0x20]
00860CC0  4C 8B CB                        mov r9, rbx
00860CC3  48 8B 5D A8                     mov rbx, qword ptr [rbp - 0x58]
00860CC7  49 8B D6                        mov rdx, r14
00860CCA  48 89 7C 24 40                  mov qword ptr [rsp + 0x40], rdi
00860CCF  48 8B CB                        mov rcx, rbx
00860CD2  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
00860CD7  40 88 74 24 38                  mov byte ptr [rsp + 0x38], sil
00860CDC  89 74 24 30                     mov dword ptr [rsp + 0x30], esi
00860CE0  66 C7 44 24 28 40 00            mov word ptr [rsp + 0x28], 0x40
00860CE7  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
00860CEC  E8 8B 74 0E 00                  call 0x14094817c
00860CF1  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
00860CF5  85 C0                           test eax, eax
00860CF7  0F 88 FE 02 00 00               js 0x140860ffb
00860CFD  C7 47 20 01 00 00 00            mov dword ptr [rdi + 0x20], 1
00860D04  E9 EC FB FF FF                  jmp 0x1408608f5
00860D09  66 85 C9                        test cx, cx
00860D0C  0F 85 FE EF FF FF               jne 0x14085fd10
00860D12  41 0F B7 16                     movzx edx, word ptr [r14]
00860D16  49 8B 45 08                     mov rax, qword ptr [r13 + 8]
00860D1A  8B CA                           mov ecx, edx
00860D1C  45 0F B7 45 00                  movzx r8d, word ptr [r13]
00860D21  45 0F B7 4D 02                  movzx r9d, word ptr [r13 + 2]
00860D26  66 44 2B C2                     sub r8w, dx
00860D2A  48 D1 E9                        shr rcx, 1
00860D2D  66 44 2B CA                     sub r9w, dx
00860D31  4C 8D 14 48                     lea r10, [rax + rcx*2]
00860D35  49 8B 47 50                     mov rax, qword ptr [r15 + 0x50]
00860D39  0F B7 48 18                     movzx ecx, word ptr [rax + 0x18]
00860D3D  8B 00                           mov eax, dword ptr [rax]
00860D3F  A8 01                           test al, 1
00860D41  8B C1                           mov eax, ecx
00860D43  0F 84 B0 03 00 00               je 0x1408610f9
00860D49  66 03 C9                        add cx, cx
00860D4C  48 03 C0                        add rax, rax
00860D4F  66 44 03 C1                     add r8w, cx
00860D53  4C 2B D0                        sub r10, rax
00860D56  66 44 89 45 F8                  mov word ptr [rbp - 8], r8w
00860D5B  66 44 03 C9                     add r9w, cx
00860D5F  4C 89 55 00                     mov qword ptr [rbp], r10
00860D63  41 BE 01 00 00 00               mov r14d, 1
00860D69  66 44 89 4D FA                  mov word ptr [rbp - 6], r9w
00860D6E  FF CF                           dec edi
00860D70  44 89 74 24 78                  mov dword ptr [rsp + 0x78], r14d
00860D75  E9 9B EF FF FF                  jmp 0x14085fd15
00860D7A  44 8B 44 24 64                  mov r8d, dword ptr [rsp + 0x64]
00860D7F  BA 80 15 00 00                  mov edx, 0x1580
00860D84  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
00860D89  48 8B CF                        mov rcx, rdi
00860D8C  E8 EF 04 FF FF                  call 0x140851280
00860D91  4C 8B 6D 90                     mov r13, qword ptr [rbp - 0x70]
00860D95  44 0F B6 64 24 61               movzx r12d, byte ptr [rsp + 0x61]
00860D9B  E9 B4 F6 FF FF                  jmp 0x140860454
00860DA0  49 8B CD                        mov rcx, r13
00860DA3  E8 B8 EB 13 00                  call 0x14099f960
00860DA8  48 8B CB                        mov rcx, rbx
00860DAB  E9 00 F7 FF FF                  jmp 0x1408604b0
00860DB0  49 8B CF                        mov rcx, r15
00860DB3  E8 B8 35 00 00                  call 0x140864370
00860DB8  E9 B1 F6 FF FF                  jmp 0x14086046e
00860DBD  48 8B 4F 30                     mov rcx, qword ptr [rdi + 0x30]
00860DC1  8B D6                           mov edx, esi
00860DC3  E8 98 36 00 00                  call 0x140864460
00860DC8  44 0F B6 64 24 61               movzx r12d, byte ptr [rsp + 0x61]
00860DCE  E9 81 F6 FF FF                  jmp 0x140860454
00860DD3  E8 DC EB FE FF                  call 0x14084f9b4
00860DD8  E9 79 EE FF FF                  jmp 0x14085fc56
00860DDD  48 8B 45 B8                     mov rax, qword ptr [rbp - 0x48]
00860DE1  41 BE 02 00 19 C0               mov r14d, 0xc0190002
00860DE7  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
00860DEB  E9 91 F0 FF FF                  jmp 0x14085fe81
00860DF0  41 8B 06                        mov eax, dword ptr [r14]
00860DF3  A8 08                           test al, 8
00860DF5  0F 85 33 0A 00 00               jne 0x14086182e
00860DFB  41 8B 86 A0 00 00 00            mov eax, dword ptr [r14 + 0xa0]
00860E02  A8 01                           test al, 1
00860E04  75 14                           jne 0x140860e1a
00860E06  49 8D 8E A8 00 00 00            lea rcx, [r14 + 0xa8]
00860E0D  E8 CE 8A 36 00                  call 0x140bc98e0
00860E12  41 83 8E A0 00 00 00 01         or dword ptr [r14 + 0xa0], 1
00860E1A  41 F7 85 B8 00 00 00 00 00 00 02  test dword ptr [r13 + 0xb8], 0x2000000
00860E25  48 8D 95 B0 00 00 00            lea rdx, [rbp + 0xb0]
00860E2C  4C 8B 4D E8                     mov r9, qword ptr [rbp - 0x18]
00860E30  4D 8B C6                        mov r8, r14
00860E33  49 8B CD                        mov rcx, r13
00860E36  0F 85 B0 02 00 00               jne 0x1408610ec
00860E3C  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
00860E41  49 8B FE                        mov rdi, r14
00860E44  E8 8B BE FE FF                  call 0x14084ccd4
00860E49  E9 E6 EC FF FF                  jmp 0x14085fb34
00860E4E  4D 8B 8D C0 00 00 00            mov r9, qword ptr [r13 + 0xc0]
00860E55  4D 85 C9                        test r9, r9
00860E58  0F 84 BA F0 FF FF               je 0x14085ff18
00860E5E  66 66 0F 1F 84 00 00 00 00 00   nop word ptr [rax + rax]
00860E68  0F 1F 84 00 00 00 00 00         nop dword ptr [rax + rax]
00860E70  4D 8B 41 10                     mov r8, qword ptr [r9 + 0x10]
00860E74  48 8D 4D 40                     lea rcx, [rbp + 0x40]
00860E78  E8 B3 D8 13 00                  call 0x14099e730
00860E7D  4D 8B 49 18                     mov r9, qword ptr [r9 + 0x18]
00860E81  66 FF CA                        dec dx
00860E84  4D 85 C9                        test r9, r9
00860E87  75 E7                           jne 0x140860e70
00860E89  E9 8A F0 FF FF                  jmp 0x14085ff18
00860E8E  0F BA 27 09                     bt dword ptr [rdi], 9
00860E92  0F 82 7D F9 FF FF               jb 0x140860815
00860E98  8B 47 18                        mov eax, dword ptr [rdi + 0x18]
00860E9B  A8 02                           test al, 2
00860E9D  0F 85 A6 0E 00 00               jne 0x140861d49
00860EA3  40 38 74 24 60                  cmp byte ptr [rsp + 0x60], sil
00860EA8  0F 85 FC 01 00 00               jne 0x1408610aa
00860EAE  84 DB                           test bl, bl
00860EB0  74 12                           je 0x140860ec4
00860EB2  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
00860EB6  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
00860EBA  E8 01 84 36 00                  call 0x140bc92c0
00860EBF  40 88 74 24 73                  mov byte ptr [rsp + 0x73], sil
00860EC4  40 38 74 24 70                  cmp byte ptr [rsp + 0x70], sil
00860EC9  0F 85 92 0E 00 00               jne 0x140861d61
00860ECF  48 8D 4D 08                     lea rcx, [rbp + 8]
00860ED3  45 33 C9                        xor r9d, r9d
00860ED6  48 89 4C 24 48                  mov qword ptr [rsp + 0x48], rcx
00860EDB  48 8D 47 58                     lea rax, [rdi + 0x58]
00860EDF  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00860EE4  48 8D 97 D8 00 00 00            lea rdx, [rdi + 0xd8]
00860EEB  48 8B 45 E8                     mov rax, qword ptr [rbp - 0x18]
00860EEF  45 33 C0                        xor r8d, r8d
00860EF2  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00860EF7  49 8B CE                        mov rcx, r14
00860EFA  48 8D 45 28                     lea rax, [rbp + 0x28]
00860EFE  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00860F03  48 8B 45 80                     mov rax, qword ptr [rbp - 0x80]
00860F07  48 89 7C 24 28                  mov qword ptr [rsp + 0x28], rdi
00860F0C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00860F11  E8 8A 61 FF FF                  call 0x1408570a0
00860F16  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
00860F1A  85 C0                           test eax, eax
00860F1C  0F 88 51 0E 00 00               js 0x140861d73
00860F22  83 27 F7                        and dword ptr [rdi], 0xfffffff7
00860F25  48 39 77 40                     cmp qword ptr [rdi + 0x40], rsi
00860F29  75 17                           jne 0x140860f42
00860F2B  48 8B 45 08                     mov rax, qword ptr [rbp + 8]
00860F2F  48 8B 48 20                     mov rcx, qword ptr [rax + 0x20]
00860F33  8B 81 10 10 00 00               mov eax, dword ptr [rcx + 0x1010]
00860F39  41 84 C4                        test r12b, al
00860F3C  0F 85 4B 0E 00 00               jne 0x140861d8d
00860F42  BA 00 39 00 00                  mov edx, 0x3900
00860F47  C7 44 24 64 04 01 00 00         mov dword ptr [rsp + 0x64], 0x104
00860F4F  41 B8 04 01 00 00               mov r8d, 0x104
00860F55  48 8B CF                        mov rcx, rdi
00860F58  E8 23 03 FF FF                  call 0x140851280
00860F5D  0F B6 5C 24 60                  movzx ebx, byte ptr [rsp + 0x60]
00860F62  E9 0A F2 FF FF                  jmp 0x140860171
00860F67  B8 71 02 00 C0                  mov eax, 0xc0000271
00860F6C  49 8B FE                        mov rdi, r14
00860F6F  E9 C0 EB FF FF                  jmp 0x14085fb34
00860F74  40 38 75 99                     cmp byte ptr [rbp - 0x67], sil
00860F78  0F 85 34 0C 00 00               jne 0x140861bb2
00860F7E  4C 8B 65 80                     mov r12, qword ptr [rbp - 0x80]
00860F82  48 8B 5D A8                     mov rbx, qword ptr [rbp - 0x58]
00860F86  49 8B D4                        mov rdx, r12
00860F89  48 8B CB                        mov rcx, rbx
00860F8C  E8 4F 17 FE FF                  call 0x1408426e0
00860F91  84 C0                           test al, al
00860F93  0F 85 7B 0A 00 00               jne 0x140861a14
00860F99  49 8B D4                        mov rdx, r12
00860F9C  48 8B CB                        mov rcx, rbx
00860F9F  E8 CC 74 14 00                  call 0x1409a8470
00860FA4  84 C0                           test al, al
00860FA6  0F 84 68 0A 00 00               je 0x140861a14
00860FAC  49 8B 45 48                     mov rax, qword ptr [r13 + 0x48]
00860FB0  F7 80 B8 00 00 00 00 00 02 00   test dword ptr [rax + 0xb8], 0x20000
00860FBA  0F 85 08 0C 00 00               jne 0x140861bc8
00860FC0  4C 8B 44 24 68                  mov r8, qword ptr [rsp + 0x68]
00860FC5  41 8B 00                        mov eax, dword ptr [r8]
00860FC8  A8 01                           test al, 1
00860FCA  0F 85 CE 01 00 00               jne 0x14086119e
00860FD0  40 38 35 6D EB 68 00            cmp byte ptr [rip + 0x68eb6d], sil
00860FD7  0F 85 89 5F 2B 00               jne 0x140b16f66
00860FDD  49 8B F8                        mov rdi, r8
00860FE0  C7 44 24 64 34 00 00 C0         mov dword ptr [rsp + 0x64], 0xc0000034
00860FE8  BA 00 2A 00 00                  mov edx, 0x2a00
00860FED  41 B8 34 00 00 C0               mov r8d, 0xc0000034
00860FF3  48 8B CF                        mov rcx, rdi
00860FF6  E8 85 02 FF FF                  call 0x140851280
00860FFB  0F B6 5C 24 60                  movzx ebx, byte ptr [rsp + 0x60]
00861000  49 8B CE                        mov rcx, r14
00861003  E8 58 74 FE FF                  call 0x140848460
00861008  E9 64 F1 FF FF                  jmp 0x140860171
0086100D  41 8B 4D 08                     mov ecx, dword ptr [r13 + 8]
00861011  F6 C1 08                        test cl, 8
00861014  0F 84 2F FC FF FF               je 0x140860c49
0086101A  49 8B 4D 68                     mov rcx, qword ptr [r13 + 0x68]
0086101E  48 8D 55 28                     lea rdx, [rbp + 0x28]
00861022  E8 29 EA FE FF                  call 0x14084fa50
00861027  B8 F7 FF 00 00                  mov eax, 0xfff7
0086102C  49 89 75 68                     mov qword ptr [r13 + 0x68], rsi
00861030  66 41 21 45 08                  and word ptr [r13 + 8], ax
00861035  E9 0F FC FF FF                  jmp 0x140860c49
0086103A  8B D0                           mov edx, eax
0086103C  B9 00 01 00 00                  mov ecx, 0x100
00861041  48 C1 E2 03                     shl rdx, 3
00861045  41 B8 43 4D 36 35               mov r8d, 0x35364d43
0086104B  E8 B4 C4 B6 FF                  call 0x1403cd504
00861050  48 8B C8                        mov rcx, rax
00861053  48 85 C0                        test rax, rax
00861056  0F 85 5F EE FF FF               jne 0x14085febb
0086105C  BA 00 0D 00 00                  mov edx, 0xd00
00861061  EB 27                           jmp 0x14086108a
00861063  8B D0                           mov edx, eax
00861065  B9 00 01 00 00                  mov ecx, 0x100
0086106A  48 C1 E2 03                     shl rdx, 3
0086106E  41 B8 43 4D 36 35               mov r8d, 0x35364d43
00861074  E8 8B C4 B6 FF                  call 0x1403cd504
00861079  48 8B C8                        mov rcx, rax
0086107C  48 85 C0                        test rax, rax
0086107F  0F 85 5F EE FF FF               jne 0x14085fee4
00861085  BA 00 0E 00 00                  mov edx, 0xe00
0086108A  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
0086108F  41 B8 9A 00 00 C0               mov r8d, 0xc000009a
00861095  48 8B CF                        mov rcx, rdi
00861098  C7 44 24 64 9A 00 00 C0         mov dword ptr [rsp + 0x64], 0xc000009a
008610A0  E8 DB 01 FF FF                  call 0x140851280
008610A5  E9 60 F1 FF FF                  jmp 0x14086020a
008610AA  48 8B 4D A8                     mov rcx, qword ptr [rbp - 0x58]
008610AE  E8 AD 73 FE FF                  call 0x140848460
008610B3  40 88 74 24 60                  mov byte ptr [rsp + 0x60], sil
008610B8  E9 F1 FD FF FF                  jmp 0x140860eae
008610BD  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
008610C2  BA 80 0F 00 00                  mov edx, 0xf80
008610C7  48 8B CF                        mov rcx, rdi
008610CA  C7 44 24 64 34 00 00 C0         mov dword ptr [rsp + 0x64], 0xc0000034
008610D2  41 B8 34 00 00 C0               mov r8d, 0xc0000034
008610D8  E8 A3 01 FF FF                  call 0x140851280
008610DD  32 DB                           xor bl, bl
008610DF  49 8B CE                        mov rcx, r14
008610E2  E8 79 73 FE FF                  call 0x140848460
008610E7  E9 85 F0 FF FF                  jmp 0x140860171
008610EC  49 8B FE                        mov rdi, r14
008610EF  E8 2C 59 21 00                  call 0x140a76a20
008610F4  E9 3B EA FF FF                  jmp 0x14085fb34
008610F9  48 D1 E8                        shr rax, 1
008610FC  E9 4B FC FF FF                  jmp 0x140860d4c
00861101  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0086110A  48 39 05 37 EA 68 00            cmp qword ptr [rip + 0x68ea37], rax
00861111  0F 84 B5 08 00 00               je 0x1408619cc
00861117  48 8B 4D A0                     mov rcx, qword ptr [rbp - 0x60]
0086111B  48 8B 05 6E 89 77 00            mov rax, qword ptr [rip + 0x77896e]
00861122  48 89 4D 90                     mov qword ptr [rbp - 0x70], rcx
00861126  48 39 41 20                     cmp qword ptr [rcx + 0x20], rax
0086112A  0F 85 88 EF FF FF               jne 0x1408600b8
00861130  8B 41 08                        mov eax, dword ptr [rcx + 8]
00861133  25 00 00 E0 7F                  and eax, 0x7fe00000
00861138  3D 00 00 60 00                  cmp eax, 0x600000
0086113D  0F 85 75 EF FF FF               jne 0x1408600b8
00861143  66 85 DB                        test bx, bx
00861146  0F 8E 6C EF FF FF               jle 0x1408600b8
0086114C  48 8B 4D C0                     mov rcx, qword ptr [rbp - 0x40]
00861150  0F BF D3                        movsx edx, bx
00861153  FF CA                           dec edx
00861155  E8 F6 68 14 00                  call 0x1409a7a50
0086115A  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
0086115F  48 8B C8                        mov rcx, rax
00861162  4C 8D 8F 88 00 00 00            lea r9, [rdi + 0x88]
00861169  E8 B6 A3 26 00                  call 0x140acb524
0086116E  84 C0                           test al, al
00861170  0F 84 47 EF FF FF               je 0x1408600bd
00861176  81 0F 00 01 00 00               or dword ptr [rdi], 0x100
0086117C  BA 00 0F 00 00                  mov edx, 0xf00
00861181  41 B8 03 01 00 00               mov r8d, 0x103
00861187  C7 44 24 64 03 01 00 00         mov dword ptr [rsp + 0x64], 0x103
0086118F  48 8B CF                        mov rcx, rdi
00861192  E8 E9 00 FF FF                  call 0x140851280
00861197  32 DB                           xor bl, bl
00861199  E9 3C EF FF FF                  jmp 0x1408600da
0086119E  48 8B 05 EB 88 77 00            mov rax, qword ptr [rip + 0x7788eb]
008611A5  49 39 45 20                     cmp qword ptr [r13 + 0x20], rax
008611A9  0F 84 47 5E 2B 00               je 0x140b16ff6
008611AF  0F BF D7                        movsx edx, di
008611B2  49 8D 88 D8 00 00 00            lea rcx, [r8 + 0xd8]
008611B9  E8 92 68 14 00                  call 0x1409a7a50
008611BE  48 8B 7D A8                     mov rdi, qword ptr [rbp - 0x58]
008611C2  48 8B D8                        mov rbx, rax
008611C5  48 8B 45 E8                     mov rax, qword ptr [rbp - 0x18]
008611C9  41 B1 01                        mov r9b, 1
008611CC  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
008611D1  49 8B D6                        mov rdx, r14
008611D4  4C 89 44 24 28                  mov qword ptr [rsp + 0x28], r8
008611D9  49 8B CD                        mov rcx, r13
008611DC  4C 8B C7                        mov r8, rdi
008611DF  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
008611E4  E8 87 9A 0E 00                  call 0x14094ac70
008611E9  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
008611ED  3D 71 02 00 C0                  cmp eax, 0xc0000271
008611F2  0F 85 DA 09 00 00               jne 0x140861bd2
008611F8  4C 8B 44 24 68                  mov r8, qword ptr [rsp + 0x68]
008611FD  48 8D 44 24 76                  lea rax, [rsp + 0x76]
00861202  0F B6 54 24 72                  movzx edx, byte ptr [rsp + 0x72]
00861207  4D 8B CC                        mov r9, r12
0086120A  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0086120F  49 8B CD                        mov rcx, r13
00861212  48 8D 45 D0                     lea rax, [rbp - 0x30]
00861216  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0086121B  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
00861220  89 74 24 20                     mov dword ptr [rsp + 0x20], esi
00861224  E8 E7 29 06 00                  call 0x1408c3c10
00861229  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
0086122D  85 C0                           test eax, eax
0086122F  0F 88 AA 09 00 00               js 0x140861bdf
00861235  4C 8B 44 24 68                  mov r8, qword ptr [rsp + 0x68]
0086123A  41 8B 80 A0 00 00 00            mov eax, dword ptr [r8 + 0xa0]
00861241  A8 01                           test al, 1
00861243  0F 84 A3 09 00 00               je 0x140861bec
00861249  49 8B 45 48                     mov rax, qword ptr [r13 + 0x48]
0086124D  83 78 28 FF                     cmp dword ptr [rax + 0x28], -1
00861251  0F 84 4C 5E 2B 00               je 0x140b170a3
00861257  49 8B CE                        mov rcx, r14
0086125A  E8 01 72 FE FF                  call 0x140848460
0086125F  48 8B CF                        mov rcx, rdi
00861262  E8 F9 71 FE FF                  call 0x140848460
00861267  48 8B CF                        mov rcx, rdi
0086126A  E8 95 58 FE FF                  call 0x140846b04
0086126F  49 8B CE                        mov rcx, r14
00861272  41 B4 01                        mov r12b, 1
00861275  E8 8A 58 FE FF                  call 0x140846b04
0086127A  48 8B 55 80                     mov rdx, qword ptr [rbp - 0x80]
0086127E  49 8B CE                        mov rcx, r14
00861281  E8 EA 71 14 00                  call 0x1409a8470
00861286  84 C0                           test al, al
00861288  0F 84 7C 09 00 00               je 0x140861c0a
0086128E  41 F7 45 08 00 00 02 00         test dword ptr [r13 + 8], 0x20000
00861296  0F 85 0F 05 00 00               jne 0x1408617ab
0086129C  48 8B 55 80                     mov rdx, qword ptr [rbp - 0x80]
008612A0  49 8B CE                        mov rcx, r14
008612A3  E8 38 14 FE FF                  call 0x1408426e0
008612A8  84 C0                           test al, al
008612AA  0F 84 4D 0A 00 00               je 0x140861cfd
008612B0  48 8B 55 80                     mov rdx, qword ptr [rbp - 0x80]
008612B4  48 8B CF                        mov rcx, rdi
008612B7  E8 24 14 FE FF                  call 0x1408426e0
008612BC  84 C0                           test al, al
008612BE  0F 85 12 0A 00 00               jne 0x140861cd6
008612C4  48 8B 55 80                     mov rdx, qword ptr [rbp - 0x80]
008612C8  48 8B CF                        mov rcx, rdi
008612CB  E8 A0 71 14 00                  call 0x1409a8470
008612D0  84 C0                           test al, al
008612D2  0F 84 FE 09 00 00               je 0x140861cd6
008612D8  49 8B 4D 48                     mov rcx, qword ptr [r13 + 0x48]
008612DC  F7 81 B8 00 00 00 00 00 02 00   test dword ptr [rcx + 0xb8], 0x20000
008612E6  0F 85 45 09 00 00               jne 0x140861c31
008612EC  4C 8B 44 24 68                  mov r8, qword ptr [rsp + 0x68]
008612F1  48 8B 55 E8                     mov rdx, qword ptr [rbp - 0x18]
008612F5  4C 8B 4D E0                     mov r9, qword ptr [rbp - 0x20]
008612F9  48 89 54 24 40                  mov qword ptr [rsp + 0x40], rdx
008612FE  41 8B 40 18                     mov eax, dword ptr [r8 + 0x18]
00861302  48 8B 55 80                     mov rdx, qword ptr [rbp - 0x80]
00861306  83 E0 02                        and eax, 2
00861309  4C 89 44 24 38                  mov qword ptr [rsp + 0x38], r8
0086130E  4C 8B C3                        mov r8, rbx
00861311  48 89 54 24 30                  mov qword ptr [rsp + 0x30], rdx
00861316  49 8B D5                        mov rdx, r13
00861319  C1 E0 04                        shl eax, 4
0086131C  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
00861320  0F B6 44 24 72                  movzx eax, byte ptr [rsp + 0x72]
00861325  88 44 24 20                     mov byte ptr [rsp + 0x20], al
00861329  E8 FA 5B 1C 00                  call 0x140a26f28
0086132E  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
00861332  3D 55 00 00 C0                  cmp eax, 0xc0000055
00861337  0F 84 1B 09 00 00               je 0x140861c58
0086133D  3D 71 02 00 C0                  cmp eax, 0xc0000271
00861342  0F 85 3A 09 00 00               jne 0x140861c82
00861348  4C 8B 44 24 68                  mov r8, qword ptr [rsp + 0x68]
0086134D  48 8D 44 24 64                  lea rax, [rsp + 0x64]
00861352  4C 8B 4D E0                     mov r9, qword ptr [rbp - 0x20]
00861356  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
0086135B  48 8B 45 D0                     mov rax, qword ptr [rbp - 0x30]
0086135F  41 8B 50 18                     mov edx, dword ptr [r8 + 0x18]
00861363  8B CA                           mov ecx, edx
00861365  89 74 24 48                     mov dword ptr [rsp + 0x48], esi
00861369  83 E2 02                        and edx, 2
0086136C  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00861371  48 8B 45 80                     mov rax, qword ptr [rbp - 0x80]
00861375  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0086137A  0F B6 44 24 72                  movzx eax, byte ptr [rsp + 0x72]
0086137F  C1 E2 04                        shl edx, 4
00861382  C1 E9 02                        shr ecx, 2
00861385  41 22 CC                        and cl, r12b
00861388  88 4C 24 30                     mov byte ptr [rsp + 0x30], cl
0086138C  89 54 24 28                     mov dword ptr [rsp + 0x28], edx
00861390  48 8B D7                        mov rdx, rdi
00861393  88 44 24 20                     mov byte ptr [rsp + 0x20], al
00861397  E8 74 5C 06 00                  call 0x1408c7010
0086139C  84 C0                           test al, al
0086139E  0F 84 38 5E 2B 00               je 0x140b171dc
008613A4  4C 8B 45 80                     mov r8, qword ptr [rbp - 0x80]
008613A8  45 0F B6 CC                     movzx r9d, r12b
008613AC  48 8B 4D D0                     mov rcx, qword ptr [rbp - 0x30]
008613B0  49 8B D5                        mov rdx, r13
008613B3  4C 89 74 24 20                  mov qword ptr [rsp + 0x20], r14
008613B8  E8 03 12 FE FF                  call 0x1408425c0
008613BD  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
008613C1  85 C0                           test eax, eax
008613C3  0F 88 D5 08 00 00               js 0x140861c9e
008613C9  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
008613CE  4C 8B CB                        mov r9, rbx
008613D1  48 8B 55 80                     mov rdx, qword ptr [rbp - 0x80]
008613D5  4C 8B 45 E0                     mov r8, qword ptr [rbp - 0x20]
008613D9  48 89 54 24 40                  mov qword ptr [rsp + 0x40], rdx
008613DE  49 8B D6                        mov rdx, r14
008613E1  0F B7 41 18                     movzx eax, word ptr [rcx + 0x18]
008613E5  40 88 74 24 38                  mov byte ptr [rsp + 0x38], sil
008613EA  66 83 E0 02                     and ax, 2
008613EE  66 C1 E0 03                     shl ax, 3
008613F2  89 74 24 30                     mov dword ptr [rsp + 0x30], esi
008613F6  66 89 44 24 28                  mov word ptr [rsp + 0x28], ax
008613FB  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00861400  48 8B CF                        mov rcx, rdi
00861403  E8 74 6D 0E 00                  call 0x14094817c
00861408  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
0086140C  85 C0                           test eax, eax
0086140E  0F 88 A6 08 00 00               js 0x140861cba
00861414  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
00861419  C7 41 20 01 00 00 00            mov dword ptr [rcx + 0x20], 1
00861420  C6 44 24 60 01                  mov byte ptr [rsp + 0x60], 1
00861425  40 32 FF                        xor dil, dil
00861428  E9 75 03 00 00                  jmp 0x1408617a2
0086142D  B8 0D 00 00 C0                  mov eax, 0xc000000d
00861432  E9 61 F6 FF FF                  jmp 0x140860a98
00861437  48 8B 89 38 10 00 00            mov rcx, qword ptr [rcx + 0x1038]
0086143E  48 8D 45 B8                     lea rax, [rbp - 0x48]
00861442  41 B9 01 00 00 00               mov r9d, 1
00861448  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0086144D  4C 8B C7                        mov r8, rdi
00861450  48 8B D3                        mov rdx, rbx
00861453  E8 E4 ED 1F 00                  call 0x140a6023c
00861458  E9 3B F6 FF FF                  jmp 0x140860a98
0086145D  E8 FE 6F FE FF                  call 0x140848460
00861462  48 8B 4D A8                     mov rcx, qword ptr [rbp - 0x58]
00861466  E8 F5 6F FE FF                  call 0x140848460
0086146B  4C 8B 6D B0                     mov r13, qword ptr [rbp - 0x50]
0086146F  84 DB                           test bl, bl
00861471  0F 85 D2 05 00 00               jne 0x140861a49
00861477  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
0086147C  8B D6                           mov edx, esi
0086147E  48 8B 48 30                     mov rcx, qword ptr [rax + 0x30]
00861482  E8 A9 6B 20 00                  call 0x140a68030
00861487  88 44 24 74                     mov byte ptr [rsp + 0x74], al
0086148B  84 DB                           test bl, bl
0086148D  0F 85 C4 05 00 00               jne 0x140861a57
00861493  48 8B 7D A8                     mov rdi, qword ptr [rbp - 0x58]
00861497  48 8B CF                        mov rcx, rdi
0086149A  E8 65 56 FE FF                  call 0x140846b04
0086149F  49 8B CE                        mov rcx, r14
008614A2  E8 5D 56 FE FF                  call 0x140846b04
008614A7  8B 44 24 78                     mov eax, dword ptr [rsp + 0x78]
008614AB  48 8B 4D C0                     mov rcx, qword ptr [rbp - 0x40]
008614AF  44 0F BF C0                     movsx r8d, ax
008614B3  41 8B D0                        mov edx, r8d
008614B6  E8 95 65 14 00                  call 0x1409a7a50
008614BB  41 8B D0                        mov edx, r8d
008614BE  4C 8B E8                        mov r13, rax
008614C1  E8 BA 17 14 00                  call 0x1409a2c80
008614C6  48 8B 4D B0                     mov rcx, qword ptr [rbp - 0x50]
008614CA  33 D2                           xor edx, edx
008614CC  8B D8                           mov ebx, eax
008614CE  E8 AD 7F 36 00                  call 0x140bc9480
008614D3  84 C0                           test al, al
008614D5  0F 85 8A 05 00 00               jne 0x140861a65
008614DB  48 8B 55 80                     mov rdx, qword ptr [rbp - 0x80]
008614DF  48 8B CF                        mov rcx, rdi
008614E2  E8 F9 11 FE FF                  call 0x1408426e0
008614E7  84 C0                           test al, al
008614E9  0F 85 99 05 00 00               jne 0x140861a88
008614EF  48 8B 55 80                     mov rdx, qword ptr [rbp - 0x80]
008614F3  49 8B CE                        mov rcx, r14
008614F6  E8 E5 11 FE FF                  call 0x1408426e0
008614FB  84 C0                           test al, al
008614FD  0F 84 8C 05 00 00               je 0x140861a8f
00861503  48 8B 55 90                     mov rdx, qword ptr [rbp - 0x70]
00861507  48 8B 05 82 85 77 00            mov rax, qword ptr [rip + 0x778582]
0086150E  48 8B 4A 48                     mov rcx, qword ptr [rdx + 0x48]
00861512  48 39 41 20                     cmp qword ptr [rcx + 0x20], rax
00861516  0F 85 88 05 00 00               jne 0x140861aa4
0086151C  F7 81 B8 00 00 00 00 00 02 00   test dword ptr [rcx + 0xb8], 0x20000
00861526  0F 85 90 05 00 00               jne 0x140861abc
0086152C  4C 8B 44 24 68                  mov r8, qword ptr [rsp + 0x68]
00861531  41 8B 80 A0 00 00 00            mov eax, dword ptr [r8 + 0xa0]
00861538  41 84 C4                        test r12b, al
0086153B  0F 84 85 05 00 00               je 0x140861ac6
00861541  41 8B 50 28                     mov edx, dword ptr [r8 + 0x28]
00861545  49 8D 78 28                     lea rdi, [r8 + 0x28]
00861549  49 8B 48 30                     mov rcx, qword ptr [r8 + 0x30]
0086154D  83 FA FF                        cmp edx, -1
00861550  0F 85 9B 05 00 00               jne 0x140861af1
00861556  48 8B 55 E0                     mov rdx, qword ptr [rbp - 0x20]
0086155A  4D 8B C8                        mov r9, r8
0086155D  4D 8B C5                        mov r8, r13
00861560  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
00861565  E8 FE DF 25 00                  call 0x140abf568
0086156A  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
0086156E  85 C0                           test eax, eax
00861570  0F 88 6E 05 00 00               js 0x140861ae4
00861576  48 8B 4D 90                     mov rcx, qword ptr [rbp - 0x70]
0086157A  48 8D 45 20                     lea rax, [rbp + 0x20]
0086157E  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00861583  4C 8B C1                        mov r8, rcx
00861586  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
0086158B  BA FF FF FF FF                  mov edx, 0xffffffff
00861590  89 74 24 38                     mov dword ptr [rsp + 0x38], esi
00861594  66 83 89 BA 00 00 00 02         or word ptr [rcx + 0xba], 2
0086159C  89 5C 24 30                     mov dword ptr [rsp + 0x30], ebx
008615A0  48 8B D9                        mov rbx, rcx
008615A3  4C 8B 48 50                     mov r9, qword ptr [rax + 0x50]
008615A7  48 8B 48 30                     mov rcx, qword ptr [rax + 0x30]
008615AB  4C 89 6C 24 28                  mov qword ptr [rsp + 0x28], r13
008615B0  C7 44 24 20 01 00 00 00         mov dword ptr [rsp + 0x20], 1
008615B8  E8 F3 07 FF FF                  call 0x140851db0
008615BD  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
008615C1  B9 FD FF 00 00                  mov ecx, 0xfffd
008615C6  66 21 8B BA 00 00 00            and word ptr [rbx + 0xba], cx
008615CD  44 8B 44 24 64                  mov r8d, dword ptr [rsp + 0x64]
008615D2  45 85 C0                        test r8d, r8d
008615D5  0F 88 34 05 00 00               js 0x140861b0f
008615DB  48 8B 45 20                     mov rax, qword ptr [rbp + 0x20]
008615DF  48 8B CB                        mov rcx, rbx
008615E2  48 89 45 90                     mov qword ptr [rbp - 0x70], rax
008615E6  E8 75 E3 13 00                  call 0x14099f960
008615EB  48 8B CB                        mov rcx, rbx
008615EE  E8 7D 2D 00 00                  call 0x140864370
008615F3  48 8B 55 90                     mov rdx, qword ptr [rbp - 0x70]
008615F7  48 8D 8D 80 00 00 00            lea rcx, [rbp + 0x80]
008615FE  40 88 74 24 70                  mov byte ptr [rsp + 0x70], sil
00861603  E8 88 6D FE FF                  call 0x140848390
00861608  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
0086160C  85 C0                           test eax, eax
0086160E  0F 88 05 05 00 00               js 0x140861b19
00861614  66 83 8B BA 00 00 00 02         or word ptr [rbx + 0xba], 2
0086161C  48 8D 8D 80 00 00 00            lea rcx, [rbp + 0x80]
00861623  E8 DC 54 FE FF                  call 0x140846b04
00861628  4C 8B 4D 80                     mov r9, qword ptr [rbp - 0x80]
0086162C  48 8D 44 24 76                  lea rax, [rsp + 0x76]
00861631  4C 8B 44 24 68                  mov r8, qword ptr [rsp + 0x68]
00861636  B9 FD FF 00 00                  mov ecx, 0xfffd
0086163B  66 21 8B BA 00 00 00            and word ptr [rbx + 0xba], cx
00861642  0F B6 54 24 72                  movzx edx, byte ptr [rsp + 0x72]
00861647  48 8B 4D 90                     mov rcx, qword ptr [rbp - 0x70]
0086164B  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00861650  48 8D 45 D0                     lea rax, [rbp - 0x30]
00861654  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00861659  48 8D 85 80 00 00 00            lea rax, [rbp + 0x80]
00861660  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00861665  C7 44 24 20 03 00 00 00         mov dword ptr [rsp + 0x20], 3
0086166D  44 88 64 24 7C                  mov byte ptr [rsp + 0x7c], r12b
00861672  E8 99 25 06 00                  call 0x1408c3c10
00861677  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
0086167B  85 C0                           test eax, eax
0086167D  0F 88 A3 04 00 00               js 0x140861b26
00861683  48 8B 4B 20                     mov rcx, qword ptr [rbx + 0x20]
00861687  E8 D0 E2 FE FF                  call 0x14084f95c
0086168C  48 8B 45 90                     mov rax, qword ptr [rbp - 0x70]
00861690  48 8B 48 20                     mov rcx, qword ptr [rax + 0x20]
00861694  E8 B7 85 36 00                  call 0x140bc9c50
00861699  48 8B 45 90                     mov rax, qword ptr [rbp - 0x70]
0086169D  45 33 C9                        xor r9d, r9d
008616A0  8B 17                           mov edx, dword ptr [rdi]
008616A2  45 33 C0                        xor r8d, r8d
008616A5  48 8B 48 20                     mov rcx, qword ptr [rax + 0x20]
008616A9  8B 41 68                        mov eax, dword ptr [rcx + 0x68]
008616AC  89 44 24 78                     mov dword ptr [rsp + 0x78], eax
008616B0  E8 CB 69 FF FF                  call 0x140858080
008616B5  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
008616B9  85 C0                           test eax, eax
008616BB  0F 88 8B 04 00 00               js 0x140861b4c
008616C1  48 8B 45 80                     mov rax, qword ptr [rbp - 0x80]
008616C5  4D 8B CD                        mov r9, r13
008616C8  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
008616CD  49 8B D6                        mov rdx, r14
008616D0  4C 8B 45 E0                     mov r8, qword ptr [rbp - 0x20]
008616D4  48 8B 4D A8                     mov rcx, qword ptr [rbp - 0x58]
008616D8  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
008616DD  44 88 64 24 38                  mov byte ptr [rsp + 0x38], r12b
008616E2  89 74 24 30                     mov dword ptr [rsp + 0x30], esi
008616E6  66 C7 44 24 28 0A 00            mov word ptr [rsp + 0x28], 0xa
008616ED  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
008616F2  E8 85 6A 0E 00                  call 0x14094817c
008616F7  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
008616FB  85 C0                           test eax, eax
008616FD  0F 88 5B 04 00 00               js 0x140861b5e
00861703  4C 8B 6D 90                     mov r13, qword ptr [rbp - 0x70]
00861707  48 8D 55 10                     lea rdx, [rbp + 0x10]
0086170B  8B 47 28                        mov eax, dword ptr [rdi + 0x28]
0086170E  45 0F B6 C4                     movzx r8d, r12b
00861712  49 8B CD                        mov rcx, r13
00861715  41 89 45 28                     mov dword ptr [r13 + 0x28], eax
00861719  E8 62 4D FF FF                  call 0x140856480
0086171E  8B 4B 28                        mov ecx, dword ptr [rbx + 0x28]
00861721  45 33 C9                        xor r9d, r9d
00861724  45 33 C0                        xor r8d, r8d
00861727  48 8B D0                        mov rdx, rax
0086172A  89 48 10                        mov dword ptr [rax + 0x10], ecx
0086172D  49 8B CD                        mov rcx, r13
00861730  49 FF 85 30 01 00 00            inc qword ptr [r13 + 0x130]
00861737  E8 6C AE FE FF                  call 0x14084c5a8
0086173C  49 8B 4D 20                     mov rcx, qword ptr [r13 + 0x20]
00861740  48 8D 55 10                     lea rdx, [rbp + 0x10]
00861744  44 84 A1 8C 00 00 00            test byte ptr [rcx + 0x8c], r12b
0086174B  0F 85 EA 00 00 00               jne 0x14086183b
00861751  E8 EA 47 FF FF                  call 0x140855f40
00861756  39 74 24 78                     cmp dword ptr [rsp + 0x78], esi
0086175A  0F 84 26 04 00 00               je 0x140861b86
00861760  49 8B 4D 20                     mov rcx, qword ptr [r13 + 0x20]
00861764  E8 CB 84 36 00                  call 0x140bc9c34
00861769  48 8B 4B 20                     mov rcx, qword ptr [rbx + 0x20]
0086176D  E8 C6 6F FE FF                  call 0x140848738
00861772  66 83 4B 08 08                  or word ptr [rbx + 8], 8
00861777  49 8B CD                        mov rcx, r13
0086177A  E8 21 36 01 00                  call 0x140874da0
0086177F  4C 89 6B 68                     mov qword ptr [rbx + 0x68], r13
00861783  8B D6                           mov edx, esi
00861785  48 8B 4F 30                     mov rcx, qword ptr [rdi + 0x30]
00861789  E8 D2 2C 00 00                  call 0x140864460
0086178E  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
00861793  40 32 FF                        xor dil, dil
00861796  40 88 7C 24 74                  mov byte ptr [rsp + 0x74], dil
0086179B  C7 41 20 01 00 00 00            mov dword ptr [rcx + 0x20], 1
008617A2  48 8B 5D A8                     mov rbx, qword ptr [rbp - 0x58]
008617A6  E9 52 F1 FF FF                  jmp 0x1408608fd
008617AB  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
008617B0  BA 80 2F 00 00                  mov edx, 0x2f80
008617B5  48 8B CF                        mov rcx, rdi
008617B8  C7 44 24 64 34 00 00 C0         mov dword ptr [rsp + 0x64], 0xc0000034
008617C0  41 B8 34 00 00 C0               mov r8d, 0xc0000034
008617C6  E8 B5 FA FE FF                  call 0x140851280
008617CB  B3 01                           mov bl, 1
008617CD  E9 96 E9 FF FF                  jmp 0x140860168
008617D2  4C 8B E6                        mov r12, rsi
008617D5  48 89 75 A8                     mov qword ptr [rbp - 0x58], rsi
008617D9  E9 64 EF FF FF                  jmp 0x140860742
008617DE  48 8B 05 8B 87 5A 00            mov rax, qword ptr [rip + 0x5a878b]
008617E5  49 23 C0                        and rax, r8
008617E8  48 3B 05 81 87 5A 00            cmp rax, qword ptr [rip + 0x5a8781]
008617EF  0F 85 E5 EB FF FF               jne 0x1408603da
008617F5  B0 01                           mov al, 1
008617F7  E9 E0 EB FF FF                  jmp 0x1408603dc
008617FC  48 8D 85 B0 00 00 00            lea rax, [rbp + 0xb0]
00861803  45 33 C9                        xor r9d, r9d
00861806  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0086180B  48 8D 15 68 4B 7F FF            lea rdx, [rip - 0x80b498]
00861812  45 33 C0                        xor r8d, r8d
00861815  C7 44 24 20 02 00 00 00         mov dword ptr [rsp + 0x20], 2
0086181D  48 8D 0D 34 87 5A 00            lea rcx, [rip + 0x5a8734]
00861824  E8 B7 48 BC FF                  call 0x1404260e0
00861829  E9 04 EC FF FF                  jmp 0x140860432
0086182E  B8 71 02 00 C0                  mov eax, 0xc0000271
00861833  49 8B FE                        mov rdi, r14
00861836  E9 F9 E2 FF FF                  jmp 0x14085fb34
0086183B  E8 E0 B3 FF FF                  call 0x14085cc20
00861840  E9 11 FF FF FF                  jmp 0x140861756
00861845  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
0086184A  41 BE 02 00 19 C0               mov r14d, 0xc0190002
00861850  45 8B C6                        mov r8d, r14d
00861853  44 89 74 24 64                  mov dword ptr [rsp + 0x64], r14d
00861858  48 8B CF                        mov rcx, rdi
0086185B  BA 00 01 00 00                  mov edx, 0x100
00861860  E8 1B FA FE FF                  call 0x140851280
00861865  45 32 E4                        xor r12b, r12b
00861868  E9 E7 EB FF FF                  jmp 0x140860454
0086186D  BA 00 02 00 00                  mov edx, 0x200
00861872  E9 15 5C 2B 00                  jmp 0x140b1748c
00861877  B8 0D 00 00 C0                  mov eax, 0xc000000d
0086187C  BA 00 03 00 00                  mov edx, 0x300
00861881  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
00861885  E9 02 5C 2B 00                  jmp 0x140b1748c
0086188A  B8 0D 00 00 C0                  mov eax, 0xc000000d
0086188F  BA 00 04 00 00                  mov edx, 0x400
00861894  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
00861898  E9 EF 5B 2B 00                  jmp 0x140b1748c
0086189D  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
008618A2  44 8B C0                        mov r8d, eax
008618A5  48 8B CF                        mov rcx, rdi
008618A8  BA 00 05 00 00                  mov edx, 0x500
008618AD  E8 CE F9 FE FF                  call 0x140851280
008618B2  E9 53 E9 FF FF                  jmp 0x14086020a
008618B7  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
008618BC  B8 0D 00 00 C0                  mov eax, 0xc000000d
008618C1  44 8B C0                        mov r8d, eax
008618C4  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
008618C8  48 8B CF                        mov rcx, rdi
008618CB  BA 00 06 00 00                  mov edx, 0x600
008618D0  E8 AB F9 FE FF                  call 0x140851280
008618D5  44 0F B6 64 24 61               movzx r12d, byte ptr [rsp + 0x61]
008618DB  44 88 64 24 61                  mov byte ptr [rsp + 0x61], r12b
008618E0  44 88 74 24 71                  mov byte ptr [rsp + 0x71], r14b
008618E5  E9 6A EB FF FF                  jmp 0x140860454
008618EA  B8 0D 00 00 C0                  mov eax, 0xc000000d
008618EF  BA 00 07 00 00                  mov edx, 0x700
008618F4  44 8B C0                        mov r8d, eax
008618F7  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
008618FB  49 8B C9                        mov rcx, r9
008618FE  49 8B F9                        mov rdi, r9
00861901  E8 7A F9 FE FF                  call 0x140851280
00861906  E9 FF E8 FF FF                  jmp 0x14086020a
0086190B  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
00861910  A8 01                           test al, 1
00861912  B8 7C 01 00 C0                  mov eax, 0xc000017c
00861917  41 B8 25 04 00 C0               mov r8d, 0xc0000425
0086191D  44 0F 44 C0                     cmove r8d, eax
00861921  BA 00 08 00 00                  mov edx, 0x800
00861926  48 8B CF                        mov rcx, rdi
00861929  44 89 44 24 64                  mov dword ptr [rsp + 0x64], r8d
0086192E  E8 4D F9 FE FF                  call 0x140851280
00861933  E9 D2 E8 FF FF                  jmp 0x14086020a
00861938  BA C0 09 00 00                  mov edx, 0x9c0
0086193D  48 8B CF                        mov rcx, rdi
00861940  E8 3B F9 FE FF                  call 0x140851280
00861945  E9 C0 E8 FF FF                  jmp 0x14086020a
0086194A  C7 84 C7 AC 01 00 00 22 00 00 C0  mov dword ptr [rdi + rax*8 + 0x1ac], 0xc0000022
00861955  0F B6 87 AA 01 00 00            movzx eax, byte ptr [rdi + 0x1aa]
0086195C  C7 84 C7 B0 01 00 00 00 0A 00 00  mov dword ptr [rdi + rax*8 + 0x1b0], 0xa00
00861967  FE 87 AA 01 00 00               inc byte ptr [rdi + 0x1aa]
0086196D  E9 E2 EA FF FF                  jmp 0x140860454
00861972  C6 45 99 01                     mov byte ptr [rbp - 0x67], 1
00861976  48 8B DE                        mov rbx, rsi
00861979  48 89 75 F0                     mov qword ptr [rbp - 0x10], rsi
0086197D  48 8B FE                        mov rdi, rsi
00861980  E9 9D E4 FF FF                  jmp 0x14085fe22
00861985  41 B8 2D 02 00 C0               mov r8d, 0xc000022d
0086198B  44 89 44 24 64                  mov dword ptr [rsp + 0x64], r8d
00861990  E9 1F F1 FF FF                  jmp 0x140860ab4
00861995  BA 00 14 00 00                  mov edx, 0x1400
0086199A  EB 05                           jmp 0x1408619a1
0086199C  BA 00 15 00 00                  mov edx, 0x1500
008619A1  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
008619A6  41 B8 03 01 00 00               mov r8d, 0x103
008619AC  C7 44 24 64 03 01 00 00         mov dword ptr [rsp + 0x64], 0x103
008619B4  81 0F 00 01 00 00               or dword ptr [rdi], 0x100
008619BA  E9 CA F3 FF FF                  jmp 0x140860d89
008619BF  44 8B C0                        mov r8d, eax
008619C2  BA 00 12 00 00                  mov edx, 0x1200
008619C7  E9 BD F3 FF FF                  jmp 0x140860d89
008619CC  48 8B 45 A0                     mov rax, qword ptr [rbp - 0x60]
008619D0  48 89 45 90                     mov qword ptr [rbp - 0x70], rax
008619D4  E9 DF E6 FF FF                  jmp 0x1408600b8
008619D9  44 84 67 30                     test byte ptr [rdi + 0x30], r12b
008619DD  B8 7C 01 00 C0                  mov eax, 0xc000017c
008619E2  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
008619E7  41 B8 25 04 00 C0               mov r8d, 0xc0000425
008619ED  44 0F 44 C0                     cmove r8d, eax
008619F1  BA 00 17 00 00                  mov edx, 0x1700
008619F6  48 8B CF                        mov rcx, rdi
008619F9  44 89 44 24 64                  mov dword ptr [rsp + 0x64], r8d
008619FE  E8 7D F8 FE FF                  call 0x140851280
00861A03  0F B6 5C 24 60                  movzx ebx, byte ptr [rsp + 0x60]
00861A08  E9 CD E6 FF FF                  jmp 0x1408600da
00861A0D  BA 80 17 00 00                  mov edx, 0x1780
00861A12  EB 05                           jmp 0x140861a19
00861A14  BA 00 27 00 00                  mov edx, 0x2700
00861A19  C7 44 24 64 34 00 00 C0         mov dword ptr [rsp + 0x64], 0xc0000034
00861A21  41 B8 34 00 00 C0               mov r8d, 0xc0000034
00861A27  EB 08                           jmp 0x140861a31
00861A29  44 8B C0                        mov r8d, eax
00861A2C  BA 40 3C 00 00                  mov edx, 0x3c40
00861A31  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
00861A36  E9 B8 F5 FF FF                  jmp 0x140860ff3
00861A3B  BA 00 18 00 00                  mov edx, 0x1800
00861A40  EB D7                           jmp 0x140861a19
00861A42  BA 00 19 00 00                  mov edx, 0x1900
00861A47  EB D0                           jmp 0x140861a19
00861A49  49 8B 4D 08                     mov rcx, qword ptr [r13 + 8]
00861A4D  E8 6E 78 36 00                  call 0x140bc92c0
00861A52  E9 20 FA FF FF                  jmp 0x140861477
00861A57  49 8B 4D 08                     mov rcx, qword ptr [r13 + 8]
00861A5B  E8 BC 7F 36 00                  call 0x140bc9a1c
00861A60  E9 2E FA FF FF                  jmp 0x140861493
00861A65  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
00861A69  41 B8 25 04 00 C0               mov r8d, 0xc0000425
00861A6F  BA 00 1A 00 00                  mov edx, 0x1a00
00861A74  44 84 60 30                     test byte ptr [rax + 0x30], r12b
00861A78  B8 7C 01 00 C0                  mov eax, 0xc000017c
00861A7D  44 0F 44 C0                     cmove r8d, eax
00861A81  44 89 44 24 64                  mov dword ptr [rsp + 0x64], r8d
00861A86  EB A9                           jmp 0x140861a31
00861A88  BA 00 1B 00 00                  mov edx, 0x1b00
00861A8D  EB 8A                           jmp 0x140861a19
00861A8F  C7 44 24 64 22 00 00 C0         mov dword ptr [rsp + 0x64], 0xc0000022
00861A97  BA 00 1C 00 00                  mov edx, 0x1c00
00861A9C  41 B8 22 00 00 C0               mov r8d, 0xc0000022
00861AA2  EB 8D                           jmp 0x140861a31
00861AA4  C7 44 24 64 22 00 00 C0         mov dword ptr [rsp + 0x64], 0xc0000022
00861AAC  BA 00 1D 00 00                  mov edx, 0x1d00
00861AB1  41 B8 22 00 00 C0               mov r8d, 0xc0000022
00861AB7  E9 75 FF FF FF                  jmp 0x140861a31
00861ABC  BA 00 1E 00 00                  mov edx, 0x1e00
00861AC1  E9 53 FF FF FF                  jmp 0x140861a19
00861AC6  49 8D 88 A8 00 00 00            lea rcx, [r8 + 0xa8]
00861ACD  E8 0E 7E 36 00                  call 0x140bc98e0
00861AD2  4C 8B 44 24 68                  mov r8, qword ptr [rsp + 0x68]
00861AD7  41 83 88 A0 00 00 00 01         or dword ptr [r8 + 0xa0], 1
00861ADF  E9 5D FA FF FF                  jmp 0x140861541
00861AE4  44 8B C0                        mov r8d, eax
00861AE7  BA 80 1E 00 00                  mov edx, 0x1e80
00861AEC  E9 40 FF FF FF                  jmp 0x140861a31
00861AF1  E8 2E 96 20 00                  call 0x140a6b124
00861AF6  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
00861AFA  85 C0                           test eax, eax
00861AFC  0F 89 74 FA FF FF               jns 0x140861576
00861B02  44 8B C0                        mov r8d, eax
00861B05  BA 00 1F 00 00                  mov edx, 0x1f00
00861B0A  E9 22 FF FF FF                  jmp 0x140861a31
00861B0F  BA 00 20 00 00                  mov edx, 0x2000
00861B14  E9 18 FF FF FF                  jmp 0x140861a31
00861B19  44 8B C0                        mov r8d, eax
00861B1C  BA 00 21 00 00                  mov edx, 0x2100
00861B21  E9 0B FF FF FF                  jmp 0x140861a31
00861B26  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
00861B2B  44 8B C0                        mov r8d, eax
00861B2E  48 8B CF                        mov rcx, rdi
00861B31  BA 80 21 00 00                  mov edx, 0x2180
00861B36  E8 45 F7 FE FF                  call 0x140851280
00861B3B  48 8D 8D 80 00 00 00            lea rcx, [rbp + 0x80]
00861B42  E8 19 69 FE FF                  call 0x140848460
00861B47  E9 17 E6 FF FF                  jmp 0x140860163
00861B4C  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
00861B51  44 8B C0                        mov r8d, eax
00861B54  BA 00 22 00 00                  mov edx, 0x2200
00861B59  E8 22 F7 FE FF                  call 0x140851280
00861B5E  48 8B 45 90                     mov rax, qword ptr [rbp - 0x70]
00861B62  48 8B 48 20                     mov rcx, qword ptr [rax + 0x20]
00861B66  E8 C9 80 36 00                  call 0x140bc9c34
00861B6B  48 8B 4B 20                     mov rcx, qword ptr [rbx + 0x20]
00861B6F  E8 C4 6B FE FF                  call 0x140848738
00861B74  0F B6 44 24 61                  movzx eax, byte ptr [rsp + 0x61]
00861B79  88 44 24 61                     mov byte ptr [rsp + 0x61], al
00861B7D  48 89 75 C8                     mov qword ptr [rbp - 0x38], rsi
00861B81  E9 ED ED FF FF                  jmp 0x140860973
00861B86  49 8B 4D 20                     mov rcx, qword ptr [r13 + 0x20]
00861B8A  E8 F5 21 15 00                  call 0x1409b3d84
00861B8F  E9 CC FB FF FF                  jmp 0x140861760
00861B94  BA 00 23 00 00                  mov edx, 0x2300
00861B99  E9 7B FE FF FF                  jmp 0x140861a19
00861B9E  BA 00 24 00 00                  mov edx, 0x2400
00861BA3  E9 71 FE FF FF                  jmp 0x140861a19
00861BA8  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
00861BAD  E9 49 F4 FF FF                  jmp 0x140860ffb
00861BB2  B8 0D 00 00 C0                  mov eax, 0xc000000d
00861BB7  BA 00 26 00 00                  mov edx, 0x2600
00861BBC  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
00861BC0  44 8B C0                        mov r8d, eax
00861BC3  E9 69 FE FF FF                  jmp 0x140861a31
00861BC8  BA 00 28 00 00                  mov edx, 0x2800
00861BCD  E9 47 FE FF FF                  jmp 0x140861a19
00861BD2  44 8B C0                        mov r8d, eax
00861BD5  BA 80 2C 00 00                  mov edx, 0x2c80
00861BDA  E9 52 FE FF FF                  jmp 0x140861a31
00861BDF  44 8B C0                        mov r8d, eax
00861BE2  BA C0 2C 00 00                  mov edx, 0x2cc0
00861BE7  E9 45 FE FF FF                  jmp 0x140861a31
00861BEC  49 8D 88 A8 00 00 00            lea rcx, [r8 + 0xa8]
00861BF3  E8 E8 7C 36 00                  call 0x140bc98e0
00861BF8  4C 8B 44 24 68                  mov r8, qword ptr [rsp + 0x68]
00861BFD  41 83 88 A0 00 00 00 01         or dword ptr [r8 + 0xa0], 1
00861C05  E9 3F F6 FF FF                  jmp 0x140861249
00861C0A  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
00861C0F  BA 00 2F 00 00                  mov edx, 0x2f00
00861C14  48 8B CF                        mov rcx, rdi
00861C17  C7 44 24 64 34 00 00 C0         mov dword ptr [rsp + 0x64], 0xc0000034
00861C1F  41 B8 34 00 00 C0               mov r8d, 0xc0000034
00861C25  E8 56 F6 FE FF                  call 0x140851280
00861C2A  B3 01                           mov bl, 1
00861C2C  E9 37 E5 FF FF                  jmp 0x140860168
00861C31  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
00861C36  BA 00 31 00 00                  mov edx, 0x3100
00861C3B  48 8B CF                        mov rcx, rdi
00861C3E  C7 44 24 64 34 00 00 C0         mov dword ptr [rsp + 0x64], 0xc0000034
00861C46  41 B8 34 00 00 C0               mov r8d, 0xc0000034
00861C4C  E8 2F F6 FE FF                  call 0x140851280
00861C51  B3 01                           mov bl, 1
00861C53  E9 10 E5 FF FF                  jmp 0x140860168
00861C58  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
00861C5D  41 B8 2D 02 00 C0               mov r8d, 0xc000022d
00861C63  BA 80 31 00 00                  mov edx, 0x3180
00861C68  44 89 44 24 64                  mov dword ptr [rsp + 0x64], r8d
00861C6D  48 8B CF                        mov rcx, rdi
00861C70  81 0F 00 04 00 00               or dword ptr [rdi], 0x400
00861C76  E8 05 F6 FE FF                  call 0x140851280
00861C7B  B3 01                           mov bl, 1
00861C7D  E9 E6 E4 FF FF                  jmp 0x140860168
00861C82  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
00861C87  44 8B C0                        mov r8d, eax
00861C8A  48 8B CF                        mov rcx, rdi
00861C8D  BA C0 31 00 00                  mov edx, 0x31c0
00861C92  E8 E9 F5 FE FF                  call 0x140851280
00861C97  B3 01                           mov bl, 1
00861C99  E9 CA E4 FF FF                  jmp 0x140860168
00861C9E  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
00861CA3  44 8B C0                        mov r8d, eax
00861CA6  48 8B CF                        mov rcx, rdi
00861CA9  BA 80 32 00 00                  mov edx, 0x3280
00861CAE  E8 CD F5 FE FF                  call 0x140851280
00861CB3  B3 01                           mov bl, 1
00861CB5  E9 AE E4 FF FF                  jmp 0x140860168
00861CBA  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
00861CBF  44 8B C0                        mov r8d, eax
00861CC2  48 8B CF                        mov rcx, rdi
00861CC5  BA C0 32 00 00                  mov edx, 0x32c0
00861CCA  E8 B1 F5 FE FF                  call 0x140851280
00861CCF  B3 01                           mov bl, 1
00861CD1  E9 92 E4 FF FF                  jmp 0x140860168
00861CD6  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
00861CDB  BA 00 30 00 00                  mov edx, 0x3000
00861CE0  48 8B CF                        mov rcx, rdi
00861CE3  C7 44 24 64 34 00 00 C0         mov dword ptr [rsp + 0x64], 0xc0000034
00861CEB  41 B8 34 00 00 C0               mov r8d, 0xc0000034
00861CF1  E8 8A F5 FE FF                  call 0x140851280
00861CF6  B3 01                           mov bl, 1
00861CF8  E9 6B E4 FF FF                  jmp 0x140860168
00861CFD  49 8B CE                        mov rcx, r14
00861D00  E8 DB 6F 14 00                  call 0x1409a8ce0
00861D05  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
00861D0A  84 C0                           test al, al
00861D0C  0F 84 2E 56 2B 00               je 0x140b17340
00861D12  0F BA 21 09                     bt dword ptr [rcx], 9
00861D16  0F 82 24 56 2B 00               jb 0x140b17340
00861D1C  8B 41 18                        mov eax, dword ptr [rcx + 0x18]
00861D1F  A8 02                           test al, 2
00861D21  0F 84 36 55 2B 00               je 0x140b1725d
00861D27  BA 00 33 00 00                  mov edx, 0x3300
00861D2C  C7 44 24 64 35 00 00 C0         mov dword ptr [rsp + 0x64], 0xc0000035
00861D34  41 B8 35 00 00 C0               mov r8d, 0xc0000035
00861D3A  48 8B F9                        mov rdi, rcx
00861D3D  E8 3E F5 FE FF                  call 0x140851280
00861D42  B3 01                           mov bl, 1
00861D44  E9 1F E4 FF FF                  jmp 0x140860168
00861D49  C7 44 24 64 35 00 00 C0         mov dword ptr [rsp + 0x64], 0xc0000035
00861D51  BA 00 37 00 00                  mov edx, 0x3700
00861D56  41 B8 35 00 00 C0               mov r8d, 0xc0000035
00861D5C  E9 92 F2 FF FF                  jmp 0x140860ff3
00861D61  49 8B CD                        mov rcx, r13
00861D64  E8 07 26 00 00                  call 0x140864370
00861D69  40 88 74 24 70                  mov byte ptr [rsp + 0x70], sil
00861D6E  E9 5C F1 FF FF                  jmp 0x140860ecf
00861D73  44 8B C0                        mov r8d, eax
00861D76  BA 00 38 00 00                  mov edx, 0x3800
00861D7B  48 8B CF                        mov rcx, rdi
00861D7E  E8 FD F4 FE FF                  call 0x140851280
00861D83  0F B6 5C 24 60                  movzx ebx, byte ptr [rsp + 0x60]
00861D88  E9 E4 E3 FF FF                  jmp 0x140860171
00861D8D  48 89 4F 40                     mov qword ptr [rdi + 0x40], rcx
00861D91  E9 AC F1 FF FF                  jmp 0x140860f42
00861D96  B8 0D 00 00 C0                  mov eax, 0xc000000d
00861D9B  BA 00 3A 00 00                  mov edx, 0x3a00
00861DA0  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
00861DA4  44 8B C0                        mov r8d, eax
00861DA7  E9 47 F2 FF FF                  jmp 0x140860ff3
00861DAC  C7 44 24 64 34 00 00 C0         mov dword ptr [rsp + 0x64], 0xc0000034
00861DB4  BA 00 3B 00 00                  mov edx, 0x3b00
00861DB9  41 B8 34 00 00 C0               mov r8d, 0xc0000034
00861DBF  E9 2F F2 FF FF                  jmp 0x140860ff3
00861DC4  C7 44 24 64 35 00 00 C0         mov dword ptr [rsp + 0x64], 0xc0000035
00861DCC  BA 00 3C 00 00                  mov edx, 0x3c00
00861DD1  41 B8 35 00 00 C0               mov r8d, 0xc0000035
00861DD7  E9 17 F2 FF FF                  jmp 0x140860ff3
00861DDC  44 8B C0                        mov r8d, eax
00861DDF  BA 80 3C 00 00                  mov edx, 0x3c80
00861DE4  E9 0A F2 FF FF                  jmp 0x140860ff3
00861DE9  B8 7C 01 00 C0                  mov eax, 0xc000017c
00861DEE  44 3B C0                        cmp r8d, eax
00861DF1  0F 85 7A 56 2B 00               jne 0x140b17471
00861DF7  41 B8 34 00 00 C0               mov r8d, 0xc0000034
00861DFD  44 89 44 24 64                  mov dword ptr [rsp + 0x64], r8d
00861E02  E9 6A 56 2B 00                  jmp 0x140b17471
00861E07  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
00861E0C  E9 14 F6 FF FF                  jmp 0x140861425
00861E11  8B 87 A0 00 00 00               mov eax, dword ptr [rdi + 0xa0]
00861E17  A8 01                           test al, 1
00861E19  0F 85 5C 56 2B 00               jne 0x140b1747b
00861E1F  48 8D 8F A8 00 00 00            lea rcx, [rdi + 0xa8]
00861E26  E8 B5 7A 36 00                  call 0x140bc98e0
00861E2B  83 8F A0 00 00 00 01            or dword ptr [rdi + 0xa0], 1
00861E32  E9 44 56 2B 00                  jmp 0x140b1747b
00861E37  C7 44 24 64 16 00 00 40         mov dword ptr [rsp + 0x64], 0x40000016
00861E3F  48 8B F8                        mov rdi, rax
00861E42  E9 11 E3 FF FF                  jmp 0x140860158
00861E47  BA 80 09 00 00                  mov edx, 0x980
00861E4C  E9 3B 56 2B 00                  jmp 0x140b1748c
00861E51  E8 6A 74 36 00                  call 0x140bc92c0
00861E56  4C 89 2F                        mov qword ptr [rdi], r13
00861E59  E9 E3 E6 FF FF                  jmp 0x140860541
00861E5E  E8 5D 74 36 00                  call 0x140bc92c0
00861E63  8B D6                           mov edx, esi
00861E65  49 8B CF                        mov rcx, r15
00861E68  E8 F3 05 00 00                  call 0x140862460
00861E6D  E9 A0 EC FF FF                  jmp 0x140860b12
00861E72  48 8B 8D 00 01 00 00            mov rcx, qword ptr [rbp + 0x100]
00861E79  48 33 CC                        xor rcx, rsp
00861E7C  E8 BF A7 E4 FF                  call 0x1406ac640
00861E81  48 8B 9C 24 68 02 00 00         mov rbx, qword ptr [rsp + 0x268]
00861E89  48 81 C4 10 02 00 00            add rsp, 0x210
00861E90  41 5F                           pop r15
00861E92  41 5E                           pop r14
00861E94  41 5D                           pop r13
00861E96  41 5C                           pop r12
00861E98  5F                              pop rdi
00861E99  5E                              pop rsi
00861E9A  5D                              pop rbp
00861E9B  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpDoParseKey(__int64 a1, __int64 a2, unsigned __int8 a3, int a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int16 v_stack_m106;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned __int64 v_stack_m148;
    unsigned __int16 v_stack_m14E;
    unsigned __int64 v_stack_m150;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m160;
    unsigned __int64 v_stack_m168;
    unsigned __int16 v_stack_m170;
    unsigned __int64 v_stack_m178;
    unsigned __int64 v_stack_m180;
    unsigned __int64 v_stack_m188;
    unsigned __int64 v_stack_m190;
    unsigned __int64 v_stack_m198;
    unsigned __int64 v_stack_m1A0;
    unsigned __int64 v_stack_m1A8;
    unsigned __int8 v_stack_m1AF;
    unsigned __int8 v_stack_m1B0;
    unsigned __int64 v_stack_m1B8;
    unsigned __int16 v_stack_m1C0;
    unsigned __int64 v_stack_m1C8;
    unsigned __int8 v_stack_m1CC;
    unsigned __int16 v_stack_m1D0;
    unsigned __int8 v_stack_m1D1;
    unsigned __int8 v_stack_m1D2;
    unsigned __int8 v_stack_m1D3;
    unsigned __int8 v_stack_m1D4;
    unsigned __int8 v_stack_m1D5;
    unsigned __int8 v_stack_m1D6;
    unsigned __int8 v_stack_m1D7;
    unsigned __int8 v_stack_m1D8;
    unsigned __int64 v_stack_m1E0;
    unsigned int v_stack_m1E4;
    unsigned __int8 v_stack_m1E7;
    unsigned __int8 v_stack_m1E8;
    unsigned __int64 v_stack_m1F8;
    unsigned __int8 v_stack_m200;
    unsigned __int64 v_stack_m208;
    unsigned __int64 v_stack_m210;
    unsigned __int64 v_stack_m218;
    unsigned __int64 v_stack_m220;
    unsigned __int64 v_stack_m228;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m90;
    unsigned __int16 v_stack_m96;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int16 v_stack_mC6;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int16 v_stack_mE6;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p20;

    v_stack_p20 = v_rbx;
    v_rsp = (v_rsp) - (528);
    result = (*(unsigned __int64 *)(v_rip + 5943242)) ^ (v_rsp);
    v_stack_m48 = result;
    v_rsi = 0;
    v_stack_m160 = a5;
    v_r14 = 0;
    v_stack_m110 = a9;
    v_stack_m198 = a1;
    v_stack_m1C8 = 0;
    v_stack_m190 = 0;
    v_stack_m1D4 = 0;
    v_stack_m1E7 = 0;
    v_stack_m1B0 = 0;
    v_stack_m1E8 = 0;
    v_stack_m1CC = 0;
    v_stack_m1D2 = 0;
    v_stack_m1AF = 0;
    v_stack_m1D5 = 0;
    v_stack_m1D6 = a3;
    v_stack_m168 = a2;
    v_stack_m1E0 = a7;
    v_stack_m170 = 0;
    v_stack_m98 = v_xmm0;
    v_stack_m138 = 0;
    v_stack_m120 = v_xmm1;
    v_stack_m140 = 0;
    v_stack_m178 = 0;
    v_stack_m1A8 = 0;
    v_stack_m130 = 0;
    v_stack_m1A0 = 0;
    v_stack_m1D7 = 0;
    v_stack_m1D0 = 0;
    v_stack_m1C0 = 0;
    v_stack_m128 = 0;
    result = HvpGetCellContextInitialize(v_stack_m138, a2, a3, a4);
    v_stack_m1D8 = 0;
    v_stack_m150 = v_xmm0;
    result = CmpInitializeDelayDerefContext(v_stack_m120, a2, a3, a4);
    v_stack_m1D1 = 0;
    v_stack_m180 = 0;
    *(unsigned __int64 *)(a7 + 160) = v_xmm0;
    a2 = 0;
    *(unsigned __int64 *)(a7 + 176) = v_xmm0;
    v_stack_m108 = v_xmm0;
    v_stack_m106 = (unsigned __int16)((unsigned int)(0xFFFFFFFFULL));
    v_stack_mE8 = v_xmm0;
    v_stack_mE6 = (unsigned __int16)((unsigned int)(0xFFFFFFFFULL));
    v_stack_mC8 = v_xmm0;
    v_stack_mC6 = (unsigned __int16)((unsigned int)(0xFFFFFFFFULL));
    result = 0;
    *(unsigned __int64 *)(a7 + 192) = v_xmm0;
    *(unsigned __int64 *)(a7 + 208) = 0;
    v_stack_m188 = a7 + 216;
    v_stack_mF8 = v_xmm0;
    v_stack_mD8 = v_xmm0;
    v_stack_mB8 = v_xmm0;
    result = memset(a7 + 216, a2, 168, a4);
    a2 = 0;
    result = memset(a7 + 384, a2, v_rsi + 80, a4);
    if (a7 != 0) {
        result = *(unsigned __int64 *)(a7 + 88);
        *(unsigned __int64 *)(a7 + 384) = result;
    }
    if (condition_is_below) goto loc_00860670;
loc_0085F8F6:
    *(unsigned __int64 *)(a7 + 88) = 0;
    if (*(unsigned __int64 *)(v_stack_m1E0 + 72) != 0) goto loc_00860BBC;
loc_0085F912:
    v_stack_m158 = *(unsigned __int64 *)(v_stack_m198 + 64);
loc_0085F91E:
    *(unsigned int *)(v_stack_m1E0 + 20) = (unsigned int)(*(unsigned __int16 *)(v_stack_m198 + 50));
    if ((*(unsigned __int64 *)(v_stack_m198 + 8)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7840315) + 8))) goto loc_0085FC0F;
    if (*(unsigned __int64 *)(a7 + 88) != 0) goto loc_0085FC44;
loc_0085F944:
    v_stack_m1D7 = 0;
loc_0085F94D:
    v_stack_m1D3 = 0;
    v_stack_m1E7 = 0;
loc_0085F957:
    result = CmpComputeComponentHashes(v_stack_m150, v_stack_m1C0, v_stack_m188, a4);
    v_stack_m1E4 = (unsigned int)(result);
    if (sign_flag) goto loc_0086189D;
loc_0085F988:
    if (0 >= ((unsigned int)((__int16)(v_stack_m1C0)))) goto loc_0085F9B0;
    if (0 >= 8) goto loc_0085FBAE;
    result = (0) + (2);
    result = (result) << (4);
    result = (result) + (v_stack_m188);
loc_0085F9A2:
    if ((*(unsigned __int16 *)(result)) > 512) goto loc_008618B7;
    a1 = (unsigned int)((0) + 1);
    goto loc_0085F988;
loc_0085F9B0:
    v_stack_m1D0 = 0;
loc_0085F9B5:
    v_stack_m1D7 = 0;
    *(unsigned __int64 *)(v_stack_m1E0 + 392) = *(unsigned __int64 *)(v_stack_m198 + 8);
    *(unsigned __int64 *)(v_stack_m1E0 + 416) = *(unsigned __int64 *)(v_stack_m198 + 8);
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m198 + 8) + 8))) >> (21));
    a1 = (unsigned int)((a1) & (0x3FFULL));
    v_stack_m1E7 = (unsigned __int8)(v_stack_m1E7);
    a1 = (unsigned int)((a1) - (0));
    a1 = (unsigned int)((a1) + ((unsigned int)((__int16)(v_stack_m1C0))));
    if (((unsigned int)(a1)) > 512) goto loc_008618EA;
    if ((unsigned __int8)(v_stack_m1E7) != 0) goto loc_0085FA1D;
    if (((*(unsigned int *)(v_stack_m1E0)) & (0x400ULL)) != 0) goto loc_00860BB2;
    result = CmpLockRegistry(a1, v_stack_m1E7, v_stack_m188, v_stack_m1E0);
loc_0085FA13:
    v_stack_m1E7 = 1;
loc_0085FA1D:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m198 + 48)))) & (9)) != 0) goto loc_0086190B;
    if (0 == ((unsigned __int16)((__int16)(v_stack_m1C0)))) goto loc_0086097D;
    v_stack_m210 = v_stack_m170;
    v_stack_m218 = v_stack_m1D8;
    v_stack_m220 = v_stack_m1A8;
    v_stack_m228 = v_stack_m1E0;
    a4 = (v_stack_m1E0) + (216);
    result = CmpPerformCompleteKcbCacheLookup(*(unsigned __int64 *)(v_stack_m198 + 8), 0, (unsigned int)((unsigned int)((__int16)(v_stack_m1C0))), a4);
    v_stack_m1E4 = (unsigned int)(result);
    if (sign_flag) goto loc_00861E47;
    if (((unsigned int)(result)) == 259) goto loc_00861E47;
    v_r12 = (unsigned __int16)((0) + ((unsigned __int16)(v_stack_m170)));
    v_stack_m1B8 = v_stack_m1A8;
    *(unsigned __int64 *)(v_stack_m1E0 + 400) = v_stack_m1A8;
    *(unsigned __int8 *)(v_stack_m1E0 + 424) = (unsigned __int8)(v_stack_m170);
    *(unsigned __int64 *)(v_stack_m1E0 + 416) = v_stack_m1A8;
    v_stack_m1D0 = (unsigned int)(v_r12);
loc_0085FAB2:
    if (((unsigned __int16)(v_r12)) != ((unsigned __int16)((__int16)(v_stack_m1C0)))) goto loc_0085FACB;
    result = (unsigned int)(*(unsigned int *)(v_stack_m1E0));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m1E0)))) & (1)) == 0) {
        a1 = v_stack_m1A8;
        result = CmpUnlockHashEntryByKcb(a1, 0, (unsigned int)((unsigned int)((__int16)(v_stack_m1C0))), a4);
        v_stack_m1D8 = 0;
    }
    result = CmpLockKcbShared(v_stack_m1A8, 0, (unsigned int)((unsigned int)((__int16)(v_stack_m1C0))), a4);
    if (((unsigned __int16)(v_r12)) < ((unsigned __int16)((__int16)(v_stack_m1C0)))) goto loc_0085FBC5;
    a2 = 0;
    result = RtlInitUnicodeString(v_stack_m98, a2, (unsigned int)((unsigned int)((__int16)(v_stack_m1C0))), a4);
loc_0085FAEB:
    v_rdi = (v_stack_m168) + (32);
    if ((*(unsigned __int8 *)(v_rip + 5960102)) == 0) goto loc_00860621;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m1E0 + 24)))) & (16)) != 0) goto loc_00860F67;
    if ((*(unsigned __int16 *)(v_stack_m1A8 + 66)) != 0) goto loc_0085FC37;
    result = CmpIsKcbInvolvedInVirtualization(v_stack_m1A8, a2, (unsigned int)((unsigned int)((__int16)(v_stack_m1C0))), a4);
    if ((unsigned __int8)(result) != 0) goto loc_0085FD79;
loc_0085FB34:
    v_stack_m1E4 = (unsigned int)((unsigned int)(0xC0000271ULL));
    result = CmpUnlockKcb(v_stack_m1A8, a2, (unsigned int)((unsigned int)((__int16)(v_stack_m1C0))), a4);
    if (((unsigned int)((unsigned int)(v_stack_m1E4))) != 0xC0000271ULL) goto loc_00861938;
    if (*(unsigned __int64 *)(v_stack_m1E0 + 64) == 0) goto loc_0085FE0C;
    if ((*(unsigned __int64 *)(v_stack_m1E0 + 64)) == (*(unsigned __int64 *)(v_stack_m1A8 + 32))) goto loc_0085FE0C;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m1A8 + 32) + 4112)))) & (1)) == 0) goto loc_008603AF;
    result = CmpLockHiveListShared(v_stack_m1A8, a2, (unsigned int)(v_stack_m1E4), a4);
    v_r14 = (*(unsigned __int64 *)(v_stack_m1A8 + 32)) + (0x1018ULL);
loc_0085FB90:
    if ((*(unsigned __int64 *)(v_r14)) == v_r14) goto loc_008603AA;
    if ((*(unsigned __int64 *)(v_r14) - 4120) == (*(unsigned __int64 *)(v_stack_m1E0 + 64))) goto loc_0085FE07;
    goto loc_0085FB90;
loc_0085FBAE:
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_r14)) - 8) + (6);
    result = (result) << (4);
    result = (result) + (*(unsigned __int64 *)((unsigned int)(v_stack_m1E4) + 160));
    goto loc_0085F9A2;
loc_0085FBC5:
    if (((unsigned int)((__int16)((unsigned __int16)(v_r12)))) >= 8) goto loc_00860678;
    result = ((__int16)((unsigned __int16)(v_r12))) << (4);
    a1 = (v_stack_m188) + (40);
loc_0085FBDE:
    a1 = (a1) + (result);
    v_stack_m90 = *(unsigned __int64 *)(a1);
    a1 = (*(unsigned __int64 *)(a1)) - (v_stack_m148);
    a1 = (a1) >> (1);
    a1 = (unsigned __int16)((a1) + ((unsigned __int16)(a1)));
    result = (unsigned __int16)((v_stack_m150) - ((unsigned __int16)(a1)));
    v_stack_m98 = (unsigned __int16)(result);
    v_stack_m96 = (unsigned __int16)(result);
    goto loc_0085FAEB;
loc_0085FC0F:
    if (*(unsigned __int64 *)(a7 + 88) == 0) goto loc_0085F944;
    result = CmpLockRegistry(a1, a2, (unsigned int)(v_stack_m1E4), a4);
    result = CmpDereferenceKeyControlBlock(*(unsigned __int64 *)(a7 + 88), a2, (unsigned int)(v_stack_m1E4), a4);
    result = CmpUnlockRegistry(*(unsigned __int64 *)(a7 + 88), a2, (unsigned int)(v_stack_m1E4), a4);
    goto loc_0085F94D;
loc_0085FC37:
    goto loc_0085FB34;
loc_0085FC44:
    if (((*(unsigned int *)((unsigned int)(v_stack_m1E4))) & (0x400ULL)) != 0) goto loc_00860DD3;
    result = CmpLockRegistry(*(unsigned __int64 *)(a7 + 88), a2, (unsigned int)(v_stack_m1E4), a4);
loc_0085FC56:
    v_stack_m1E7 = 1;
    result = (unsigned int)((*(unsigned __int64 *)(0 + 296)) & (1));
    v_r14 = *(unsigned __int64 *)(0 + 296);
    if (!(condition_is_equal)) {
        v_r14 = (*(unsigned __int64 *)(0 + 296)) & (-2);
    }
    if (v_r14 == 0) goto loc_00860638;
    if ((unsigned __int8)(result) != 0) goto loc_00860638;
    result = RtlPrefixUnicodeString(v_r14, v_stack_m160, 1, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00860638;
    a1 = ((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_r14)))) >> (1);
    a1 = (unsigned __int16)((*(unsigned __int16 *)(v_stack_m160)) - ((unsigned __int16)(*(unsigned __int16 *)(v_r14))));
    result = (unsigned __int16)((*(unsigned __int16 *)(v_stack_m160 + 2)) - ((unsigned __int16)(*(unsigned __int16 *)(v_r14))));
    v_stack_m148 = *(unsigned __int64 *)(v_stack_m160 + 8) + a1 * 2;
    v_stack_m150 = (unsigned __int16)(a1);
    v_stack_m14E = (unsigned __int16)(result);
    if ((unsigned __int16)(a1) == 0) goto loc_0085FCF2;
loc_0085FCD0:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m160 + 8) + a1 * 2)) != 92) goto loc_0085FCEE;
    a1 = (unsigned __int16)((a1) + ((unsigned __int16)((unsigned int)(0xFFFEULL))));
    result = (unsigned __int16)((result) + ((unsigned __int16)((unsigned int)(0xFFFEULL))));
    a3 = (*(unsigned __int64 *)(v_stack_m160 + 8) + a1 * 2) + (2);
    v_stack_m150 = (unsigned __int16)(a1);
    v_stack_m14E = (unsigned __int16)(result);
    if ((unsigned __int16)(a1) != 0) goto loc_0085FCD0;
loc_0085FCEE:
    v_stack_m148 = a3;
loc_0085FCF2:
    v_rdi = (unsigned int)(((unsigned int)(*(unsigned int *)(0 + 8))) >> (21));
    v_rdi = (unsigned int)((v_rdi) & (0x3FFULL));
    v_rdi = (unsigned int)((v_rdi) - 1);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m1E0)))) & (1)) != 0) goto loc_00860D09;
loc_0085FD10:
loc_0085FD15:
    result = CmpComputeComponentHashes(v_stack_m150, v_stack_m1C0, v_stack_m188, a4);
    v_stack_m1E4 = (unsigned int)(result);
    if (sign_flag) goto loc_0086186D;
    if (((unsigned int)((__int16)(v_stack_m1C0) + v_rdi * 1)) > 32) goto loc_00861877;
loc_0085FD50:
    if (0 >= ((unsigned int)((__int16)(v_stack_m1C0)))) goto loc_0085FD9F;
    if (0 >= 8) goto loc_008602D4;
    result = (0) + (2);
    result = (result) << (4);
    result = (result) + (v_stack_m188);
loc_0085FD6B:
    if ((*(unsigned __int16 *)(result)) > 512) goto loc_0086188A;
    a1 = (unsigned int)((0) + 1);
    goto loc_0085FD50;
loc_0085FD79:
    result = CmpIsSystemEntity(v_stack_m1D6, v_rdi, (unsigned int)(v_stack_m1D0) + 16, (__int16)(v_stack_m1C0));
    if ((unsigned __int8)(result) == 0) goto loc_00860DF0;
    goto loc_0085FB34;
loc_0085FD9F:
    if (((unsigned __int16)((unsigned int)(v_stack_m1D0))) != ((unsigned __int16)((__int16)(v_stack_m1C0)))) goto loc_00860630;
    result = CmpLockHashEntrySharedByKcb(0, v_rdi, (unsigned int)(v_stack_m1D0) + 16, (__int16)(v_stack_m1C0));
    v_stack_m1D7 = 1;
loc_0085FDB9:
    v_stack_m1D3 = 1;
    result = CmpLockKcbShared(0, v_rdi, (unsigned int)(v_stack_m1D0) + 16, (__int16)(v_stack_m1C0));
    a2 = 0;
    result = CmpIsKeyDeleted(0, a2, (unsigned int)(v_stack_m1D0) + 16, (__int16)(v_stack_m1C0));
    if ((unsigned __int8)(result) != 0) goto loc_008606BF;
    if (condition_is_below) goto loc_008606BF;
    result = CmpUnlockKcb(0, a2, (unsigned int)(v_stack_m1D0) + 16, (__int16)(v_stack_m1C0));
    v_stack_m1C8 = v_stack_m190;
    goto loc_0085F9B5;
loc_0085FE07:
    result = CmpUnlockHiveList(0, a2, (unsigned int)(v_stack_m1D0) + 16, (__int16)(v_stack_m1C0));
loc_0085FE0C:
    if (*(unsigned __int64 *)(v_stack_m198 + 56) != 0) goto loc_008609BE;
    if (v_stack_m158 != 0) goto loc_008609BE;
loc_0085FE22:
    result = CmpTransSilentIgnore(0, a2, (unsigned int)(v_stack_m1D0) + 16, (__int16)(v_stack_m1C0));
    if ((unsigned __int8)(result) != 0) goto loc_008609AE;
    if (*(unsigned __int64 *)(v_stack_m198 + 56) != 0) goto loc_0085FE3D;
    if (v_stack_m158 == 0) goto loc_008609AE;
loc_0085FE3D:
    if (*(unsigned __int64 *)(v_stack_m1A8 + 32) == 0) goto loc_00860A54;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_m198 + 56))) & (1)) == 0) goto loc_00860AD8;
    v_rdi = (*(unsigned __int64 *)(v_stack_m198 + 56)) & (-2);
    result = CmpTransReferenceTransaction(*(unsigned __int64 *)(v_stack_m198 + 56), a2, (unsigned int)(v_stack_m1D0) + 16, (__int16)(v_stack_m1C0));
    if (sign_flag) goto loc_0085FE96;
    v_stack_m1C8 = *(unsigned __int64 *)(v_rdi + 16);
    if (*(unsigned __int64 *)(v_rdi + 16) == 0) goto loc_00860DDD;
    v_stack_m190 = *(unsigned __int64 *)(v_rdi + 16);
loc_0085FE81:
    result = *(unsigned __int64 *)(v_rdi + 16);
    if (*(unsigned __int64 *)(v_stack_m198 + 56) != 0) {
        a1 = v_rdi;
        result = ObfDereferenceObject(a1, a2, (unsigned int)(v_stack_m1D0) + 16, (__int16)(v_stack_m1C0));
    }
    v_stack_m1B8 = v_stack_m1A8;
loc_0085FE96:
loc_0085FE9A:
    if (sign_flag) goto loc_00860A54;
loc_0085FEA3:
    if (((unsigned int)((__int16)(*(unsigned __int16 *)(v_stack_m1A8 + 66)))) < 2) goto loc_0085FEBB;
    result = (unsigned int)(((unsigned int)((unsigned int)((__int16)(*(unsigned __int16 *)(v_stack_m1A8 + 66))))) - (1));
    if (condition_is_not_equal) goto loc_0086103A;
loc_0085FEBB:
    v_stack_mF0 = 0;
    v_stack_m106 = (unsigned __int16)((unsigned int)(0xFFFFFFFFULL));
    v_stack_m108 = (unsigned __int16)((__int16)(*(unsigned __int16 *)(v_stack_m1A8 + 66)));
    if (((unsigned int)((__int16)(*(unsigned __int16 *)(v_stack_m1A8 + 66)))) < 2) goto loc_0085FEE4;
    result = (unsigned int)(((unsigned int)((unsigned int)((__int16)(*(unsigned __int16 *)(v_stack_m1A8 + 66))))) - (1));
    if (condition_is_not_equal) goto loc_00861063;
loc_0085FEE4:
    v_stack_mE6 = (unsigned __int16)((unsigned int)(0xFFFFFFFFULL));
    v_stack_mE8 = (unsigned __int16)((__int16)(*(unsigned __int16 *)(v_stack_m1A8 + 66)));
    v_stack_mD0 = 0;
    v_stack_m1E4 = 0;
    v_stack_m106 = (unsigned __int16)(*(unsigned __int16 *)(v_stack_m1A8 + 66));
    if ((unsigned __int16)((__int16)(*(unsigned __int16 *)(v_stack_m1A8 + 66))) != 0) goto loc_00860E4E;
    *(unsigned __int64 *)(v_stack_m148 + (__int16)(*(unsigned __int16 *)(v_stack_m1A8 + 66)) * 8 + 72) = v_stack_m1A8;
loc_0085FF18:
loc_0085FF27:
    if (((unsigned __int16)((unsigned int)(v_stack_m1D0))) >= ((unsigned __int16)((__int16)(v_stack_m1C0)))) goto loc_00860722;
    result = CmpLockKcbStackShared(v_stack_m108, (__int16)(*(unsigned __int16 *)(v_stack_m1A8 + 66)), (unsigned int)(v_stack_m1D0) + 16, (__int16)(v_stack_m1C0));
    if (((*(unsigned int *)(v_stack_m1B8 + 8)) & (0x20000ULL)) != 0) goto loc_008610BD;
    v_stack_m158 = 0;
loc_0085FF50:
    if (sign_flag) goto loc_008600AB;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_stack_m108 + 2))) >= 2) goto loc_00860A46;
loc_0085FF6C:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m108 + (__int16)((unsigned __int16)(*(unsigned __int16 *)(v_stack_m108 + 2))) * 8 + 8) + 66)) == 0) goto loc_0085FF7C;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m108 + (__int16)((unsigned __int16)(*(unsigned __int16 *)(v_stack_m108 + 2))) * 8 + 8) + 65)) == 1) goto loc_008600AB;
loc_0085FF7C:
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_stack_m108 + (__int16)((unsigned __int16)(*(unsigned __int16 *)(v_stack_m108 + 2))) * 8 + 8) + 40)) == -1) goto loc_008600A3;
    if (v_stack_m1C8 != 0) goto loc_008605DB;
loc_0085FF93:
    result = CmpIsKeyStackSymlink(v_stack_m108, *(unsigned __int16 *)(v_stack_m108 + 2), (unsigned int)(v_stack_m1D0) + 16, (__int16)(v_stack_m1C0));
    if ((unsigned __int8)(result) != 0) goto loc_008602EB;
    result = CmpUnlockKcbStack(v_stack_m108, *(unsigned __int16 *)(v_stack_m108 + 2), (unsigned int)(v_stack_m1D0) + 16, (__int16)(v_stack_m1C0));
    if (((unsigned int)((__int16)((unsigned __int16)((unsigned int)(v_stack_m1D0))))) >= 8) goto loc_00860695;
    a3 = ((unsigned int)((unsigned int)((__int16)((unsigned __int16)((unsigned int)(v_stack_m1D0)))))) + (2);
    a3 = (a3) << (4);
    a3 = (a3) + (v_stack_m188);
loc_0085FFCF:
    result = (unsigned int)((result) * (*(unsigned int *)(v_stack_m1B8 + 16)));
    result = (unsigned int)((result) + ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m188 + (__int16)((unsigned __int16)((unsigned int)(v_stack_m1D0))) * 4)))));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m1E0)))) & (1)) == 0) goto loc_0085FFF1;
    if (((unsigned int)((__int16)((unsigned __int16)((unsigned int)(v_stack_m1D0))))) == ((unsigned int)((unsigned int)((unsigned int)((__int16)(v_stack_m1C0))) - 1))) goto loc_00860A3F;
loc_0085FFF1:
    a2 = 0;
loc_0085FFF3:
    v_stack_m1F8 = v_stack_m1E0;
    v_stack_m200 = 0;
    v_stack_m208 = v_stack_m1C8;
    v_stack_m210 = (unsigned int)(result);
    v_stack_m218 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m188 + (__int16)((unsigned __int16)((unsigned int)(v_stack_m1D0))) * 4)));
    v_stack_m220 = a3;
    v_stack_m228 = v_stack_m1B0;
    result = CmpWalkOneLevel(v_stack_m1B8, v_stack_m108, v_stack_m130, v_stack_mE8);
    v_stack_m1E4 = (unsigned int)(result);
    if (((unsigned int)(result)) == 0xC0000034ULL) goto loc_00860215;
loc_0086003C:
    if (v_stack_m1E4 < 0) goto loc_00860D7A;
    *(unsigned __int64 *)(v_stack_m1E0 + 408) = v_stack_m130;
    *(unsigned __int64 *)(v_stack_m1E0 + 416) = v_stack_m130;
    result = CmpDereferenceKeyControlBlockUnsafe(v_stack_m1B8, v_stack_m108, v_stack_m130, v_stack_mE8);
    v_stack_m1B8 = v_stack_m130;
    v_stack_m1A8 = v_stack_m130;
    v_stack_m1D8 = (unsigned __int8)(v_stack_m1B0);
    v_rbx = (unsigned __int16)(((unsigned int)(v_stack_m1D0)) + 1);
    v_stack_m130 = 0;
    v_stack_m1B0 = 0;
    v_stack_m1D0 = (unsigned int)(v_rbx);
    goto loc_0085FF27;
loc_008600A3:
    a2 = (unsigned __int16)((v_stack_m108) - 1);
    goto loc_0085FF50;
loc_008600AB:
    if ((*(unsigned __int8 *)(v_rip + 6879890)) != 0) goto loc_00861101;
loc_008600B8:
loc_008600BD:
    v_stack_m1E4 = 0xC0000034ULL;
    result = CmpRecordParseFailure(v_stack_m1E0, (unsigned int)(0x1000ULL), (unsigned int)(0xC0000034ULL), v_stack_mE8);
    v_rbx = 0;
loc_008600DA:
    result = CmpUnlockKcbStack(v_stack_mE8, (unsigned int)(0x1000ULL), (unsigned int)(0xC0000034ULL), v_stack_mE8);
    goto loc_00860171;
loc_008600E7:
    v_stack_m208 = v_stack_m1E4;
    v_stack_m210 = v_stack_m1D1;
    v_stack_m218 = v_stack_m1C8;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_mE8 + 24))) >> (2));
    result = (unsigned __int8)((result) & (1));
    v_stack_m220 = (unsigned __int8)(result);
    v_stack_m228 = (unsigned __int8)(v_stack_m1D6);
    result = CmpCheckOpenAccessOnKeyBody(v_stack_m178, v_stack_mE8, v_stack_m1E0, v_stack_m168);
    if ((unsigned __int8)(result) != 0) goto loc_00860917;
    if (v_stack_m1D1 != 0) goto loc_00861E11;
    result = CmpRecordParseFailure(v_stack_m1E0, (unsigned int)(0x3CE0ULL), (unsigned int)(v_stack_m1E4), v_stack_m168);
loc_00860158:
    if (v_stack_m1CC != 0) goto loc_00861B3B;
loc_00860163:
loc_00860168:
    if ((unsigned __int8)(v_stack_m130) != 0) goto loc_008600DA;
loc_00860171:
    if ((unsigned __int8)(v_stack_m1E8) == 0) goto loc_008601E9;
    if (0 > (*(unsigned __int16 *)(v_stack_m1A0 + 2))) goto loc_008601E9;
loc_008601A0:
    v_stack_m180 = v_stack_m180;
    if (0 >= 2) goto loc_00860661;
loc_008601BB:
    result = CmpUnlockKcb(*(unsigned __int64 *)(v_stack_m1A0 + (__int16)(0) * 8 + 8), (unsigned int)(0x3CE0ULL), (unsigned int)(v_stack_m1E4), v_stack_m168);
    v_rbx = (unsigned __int16)((0) + 1);
    if (((unsigned __int16)(v_rbx)) <= (*(unsigned __int16 *)(v_stack_m1A0 + 2))) goto loc_008601A0;
    v_stack_m1E7 = (unsigned __int8)(v_stack_m1E7);
    v_rsi = 0;
    v_stack_m1D7 = (unsigned __int8)(v_stack_m1D7);
    v_stack_m180 = v_stack_m180;
    v_stack_m1D5 = (unsigned __int8)(v_stack_m1D5);
loc_008601E9:
    result = v_stack_m180;
    if (v_stack_m1D5 != 0) {
        a1 = *(unsigned __int64 *)(v_stack_m198 + 8);
        result = CmpUnlockKcb(a1, (unsigned int)(0x3CE0ULL), (unsigned int)(v_stack_m1E4), v_stack_m168);
    }
    if ((unsigned __int8)(v_stack_m1D4) != 0) goto loc_00860DBD;
loc_0086020A:
    goto loc_00860454;
loc_00860215:
    if ((*(unsigned __int8 *)(v_rip + 6879528)) == 0) goto loc_0086003C;
    v_stack_m1B8 = v_stack_m1A8;
    if ((*(unsigned __int64 *)(v_rip + 6879510)) == (*(unsigned __int64 *)(gs_base + (0 + 392)))) goto loc_008602C7;
    if ((*(unsigned __int64 *)(v_stack_m1A8 + 32)) != (*(unsigned __int64 *)(v_rip + 7837769))) goto loc_008602C7;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m1A8 + 8))) & (0x7FE00000ULL));
    if (((unsigned int)(result)) != 0x600000ULL) goto loc_0086028E;
    if (condition_is_less_or_equal) goto loc_0086028E;
    a2 = (unsigned int)(((__int16)((unsigned __int16)(v_stack_m198))) - 1);
    result = CmpGetComponentNameAtIndex(v_stack_m188, a2, (unsigned int)(v_stack_m1E4), v_stack_m168);
    a4 = (v_stack_m1E0) + (136);
    result = CmpWaitForHiveMount(result, a2, (unsigned int)(v_stack_m1E4), a4);
    if ((unsigned __int8)(result) != 0) goto loc_00861995;
loc_0086028E:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m1A8 + 8))) & (0x7FE00000ULL));
    if (((unsigned int)(result)) != 0x400000ULL) goto loc_008602C7;
    result = CmpGetComponentNameAtIndex(v_stack_m188, (__int16)((unsigned __int16)(v_stack_m198)), (unsigned int)(v_stack_m1E4), a4);
    a4 = (v_stack_m1E0) + (136);
    result = CmpWaitForHiveMount(result, (__int16)((unsigned __int16)(v_stack_m198)), (unsigned int)(v_stack_m1E4), a4);
    if ((unsigned __int8)(result) != 0) goto loc_0086199C;
loc_008602C7:
    v_stack_m1C8 = v_stack_m190;
    goto loc_0086003C;
loc_008602D4:
    result = (result - 8) + (6);
    result = (result) << (4);
    result = (result) + (*(unsigned __int64 *)(v_stack_m1B8 + 160));
    goto loc_0085FD6B;
loc_008602EB:
    v_stack_m200 = v_stack_m140;
    v_stack_m208 = v_stack_m1E0 + 88;
    v_stack_m210 = v_stack_m160;
    v_stack_m218 = v_stack_m120;
    v_stack_m220 = v_stack_m1E0;
    v_stack_m228 = v_stack_m1E0;
    result = CmpGetSymbolicLinkTarget(v_stack_m1D4, v_stack_m1E0 + 216, (unsigned __int16)(v_stack_m198), v_stack_m1C0);
    v_stack_m1E4 = (unsigned int)(result);
    if (sign_flag) goto loc_008619BF;
    if ((*(unsigned __int64 *)(v_stack_m1E0 + 64)) != 0) goto loc_00860361;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m140 + 32) + 4112)))) & (1)) != 0) {
        *(unsigned __int64 *)(v_stack_m1E0 + 64) = *(unsigned __int64 *)(v_stack_m140 + 32);
    }
    v_stack_m1E4 = 260;
    if (((unsigned __int8)(*(unsigned __int8 *)(v_stack_m1E0 + 426))) >= 4) goto loc_00860454;
    *(unsigned int *)(v_stack_m1E0 + *(unsigned __int8 *)(v_stack_m1E0 + 426) * 8 + 428) = 260;
    *(unsigned int *)(v_stack_m1E0 + *(unsigned __int8 *)(v_stack_m1E0 + 426) * 8 + 432) = 0x1300ULL;
    goto loc_00860454;
loc_008603AA:
    result = CmpUnlockHiveList(*(unsigned __int64 *)(v_stack_m140 + 32), v_stack_m1E0 + 216, (unsigned __int16)(v_stack_m198), v_stack_m1C0);
loc_008603AF:
    result = PsIsCurrentThreadInServerSilo(*(unsigned __int64 *)(v_stack_m140 + 32), v_stack_m1E0 + 216, (unsigned __int16)(v_stack_m198), v_stack_m1C0);
    if ((unsigned __int8)(result) == 0) goto loc_00860432;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5938074)))) <= 5) goto loc_00860432;
    if (((*(unsigned __int64 *)(v_rip + 5938068)) & ((unsigned __int16)(v_stack_m198))) != 0) goto loc_008617DE;
loc_008603DA:
    result = 0;
loc_008603DC:
    if (0 != 0) {
        result = v_stack_m128;
        v_stack_m128 = 0x1000000ULL;
        v_stack_m58 = result;
        a2 = v_rip - 8429778;
        result = v_stack_m78;
        v_stack_m50 = 8;
        a4 = 3;
        v_stack_m228 = result;
        a1 = v_rip + 5937978;
        result = tlgWriteAgg(a1, a2, (unsigned __int16)(v_stack_m198), a4);
        a2 = *(unsigned int *)(v_rip + 5937967);
    }
    if (((unsigned int)(a2)) > 5) goto loc_008617FC;
loc_00860432:
    v_stack_m1E4 = 0xC0000022ULL;
    if (((unsigned __int8)(*(unsigned __int8 *)(v_stack_m1E0 + 426))) < 4) goto loc_0086194A;
loc_00860454:
    if (v_stack_m1D8 != 0) goto loc_008605CE;
loc_00860463:
    if (v_stack_m1D7 != 0) goto loc_00860DB0;
loc_0086046E:
    result = *(unsigned __int8 *)(v_stack_m1E0 + 426);
    if (v_stack_mF0 != 0) {
        result = CmSiFreeMemory(v_stack_mF0, a2, (unsigned __int16)(v_stack_m198), a4);
    }
    if (v_stack_mD0 != 0) {
        result = CmSiFreeMemory(v_stack_mD0, a2, (unsigned __int16)(v_stack_m198), a4);
    }
    if (v_stack_mB0 != 0) {
        result = CmSiFreeMemory(v_stack_mB0, a2, (unsigned __int16)(v_stack_m198), a4);
    }
    if (v_stack_m130 != 0) goto loc_00860DA0;
    if (v_stack_m1B8 == 0) goto loc_008604B5;
loc_008604B0:
    result = CmpDereferenceKeyControlBlock(v_stack_m1B8, a2, (unsigned __int16)(v_stack_m198), a4);
loc_008604B5:
    if (0 != 0) {
        a1 = 0;
        result = CmpDereferenceKeyControlBlock(a1, a2, (unsigned __int16)(v_stack_m198), a4);
    }
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m1E0 + 100))) == 0) goto loc_00860B1E;
    v_stack_m1E7 = (unsigned __int8)(v_stack_m1E7);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m1E0 + 100)))) & (2)) == 0) goto loc_00860B1E;
    v_stack_mC8 = v_xmm0;
    v_stack_m110 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m1E0 + 112) + 1648);
    v_stack_m1D0 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m1E0 + 112) + 1656)));
    v_stack_mB8 = v_xmm0;
    v_stack_mA8 = v_xmm0;
    result = CmpAttachToRegistryProcess(v_stack_mC8, a2, (unsigned __int16)(v_stack_m198), a4);
    v_stack_m1E7 = (unsigned __int8)(v_stack_m1E7);
loc_00860520:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m1E0 + 112) + 1656))))) goto loc_00860B06;
    result = CmpLockHashEntryByIndexExclusive(*(unsigned __int64 *)(v_stack_m1E0 + 112), 0, (unsigned __int16)(v_stack_m198), a4);
loc_0086053C:
loc_00860541:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m1E0 + 112) + 1648) + 0 + 0 * 2 * 8 + 16) == 0) goto loc_00860579;
    result = CmpLockKcbExclusive(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m1E0 + 112) + 1648) + 0 + 0 * 2 * 8 + 16) - 16, 0, (unsigned __int16)(v_stack_m198), a4);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m1E0 + 112) + 1648) + 0 + 0 * 2 * 8 + 16) - 16)) != 0) goto loc_0086058F;
    result = CmpRemoveFromDelayedClose(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m1E0 + 112) + 1648) + 0 + 0 * 2 * 8 + 16) - 16, 0, (unsigned __int16)(v_stack_m198), a4);
    result = CmpCleanUpKcbCacheWithLock(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m1E0 + 112) + 1648) + 0 + 0 * 2 * 8 + 16) - 16, v_stack_m120, (unsigned __int16)(v_stack_m198), a4);
    result = CmpUnlockKcb(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m1E0 + 112) + 1648) + 0 + 0 * 2 * 8 + 16) - 16, v_stack_m120, (unsigned __int16)(v_stack_m198), a4);
    goto loc_0086053C;
loc_00860579:
    result = CmpUnlockHashEntryByIndex(*(unsigned __int64 *)(v_stack_m1E0 + 112), 0, (unsigned __int16)(v_stack_m198), a4);
    v_rsi = (unsigned int)((v_rsi) + 1);
    goto loc_00860520;
loc_0086058F:
    a4 = 0;
    result = CmpSyncKcbCacheForHive(*(unsigned __int64 *)(v_stack_m1E0 + 112), *(unsigned __int64 *)(v_stack_m1E0 + 112), v_stack_m120, a4);
    if (((unsigned int)(result)) == 1) goto loc_00861E5E;
    if (((unsigned int)(result)) == 3) goto loc_00861E5E;
    if (((unsigned int)(result)) == 2) goto loc_00861E51;
    result = CmpUnlockKcb((unsigned int)(v_stack_m1D0), *(unsigned __int64 *)(v_stack_m1E0 + 112), v_stack_m120, a4);
    goto loc_00860541;
loc_008605CE:
    result = CmpUnlockHashEntryByKcb(*(unsigned __int64 *)((unsigned int)(v_stack_m1D0) + 24), *(unsigned __int64 *)(v_stack_m1E0 + 112), v_stack_m120, a4);
    goto loc_00860463;
loc_008605DB:
loc_008605DF:
    result = CmListGetNextElement(*(unsigned __int64 *)(v_stack_m180 + 8) + 208, v_stack_m158, 32, *(unsigned __int64 *)(v_stack_m180 + 8));
    if (result == 0) goto loc_0085FF93;
    if ((*(unsigned int *)(result + 68)) != 2) goto loc_008605DF;
    result = CmEqualTrans(*(unsigned __int64 *)(result + 56), v_stack_m1E0, 32, *(unsigned __int64 *)(v_stack_m180 + 8));
    if ((unsigned __int8)(result) != 0) goto loc_008600AB;
    goto loc_0085FF93;
loc_00860621:
    goto loc_0085FB34;
loc_00860630:
    v_r14 = 0;
    goto loc_0085FDB9;
loc_00860638:
    result = CmpDereferenceKeyControlBlock(*(unsigned __int64 *)(v_stack_m1E0 + 112), v_stack_m1E0, 32, *(unsigned __int64 *)(v_stack_m180 + 8));
    result = CmpUnlockRegistry(*(unsigned __int64 *)(v_stack_m1E0 + 112), v_stack_m1E0, 32, *(unsigned __int64 *)(v_stack_m180 + 8));
    v_r14 = 0;
    v_stack_m1C8 = v_stack_m190;
    goto loc_0085F94D;
loc_00860661:
    goto loc_008601BB;
loc_00860670:
    goto loc_0085F8F6;
loc_00860678:
    result = (unsigned int)((*(unsigned __int64 *)((unsigned int)(v_stack_m1D0) + 24)) + (-8));
    a1 = ((unsigned int)((unsigned int)(result))) << (4);
    result = (*(unsigned __int64 *)(v_stack_m188 + 160)) + (104);
    goto loc_0085FBDE;
loc_00860695:
    a3 = (*(unsigned __int64 *)(v_stack_m180 + 8) - 8) + (6);
    a3 = (a3) << (4);
    a3 = (a3) + (*(unsigned __int64 *)(v_stack_m188 + 160));
    goto loc_0085FFCF;
loc_008606BF:
    result = CmpUnlockKcb(v_rsi, v_stack_m1E0, a3, *(unsigned __int64 *)(v_stack_m180 + 8));
    if (0 != 0) goto loc_00860A2A;
loc_008606D0:
    result = CmpDereferenceKeyControlBlock(v_rsi, v_stack_m1E0, a3, *(unsigned __int64 *)(v_stack_m180 + 8));
    v_stack_m1D0 = (unsigned int)((unsigned __int16)(v_rsi));
    v_stack_m150 = v_xmm0;
    result = CmpCleanupPathInfo(v_stack_m1A8, v_stack_m1E0, a3, *(unsigned __int64 *)(v_stack_m180 + 8));
    a2 = 0;
    result = memset(v_stack_m1A8, a2, 168, *(unsigned __int64 *)(v_stack_m180 + 8));
    v_stack_m1C8 = v_stack_m190;
    v_stack_m1D3 = 0;
    goto loc_0085F957;
loc_00860722:
    v_stack_m1A0 = v_stack_m198;
    if (*(unsigned __int64 *)(v_stack_m1B8 + 72) == 0) goto loc_008617D2;
    result = CmpPopulateKcbStack(v_stack_m198, *(unsigned __int64 *)(v_stack_m1B8 + 72), 168, *(unsigned __int64 *)(v_stack_m180 + 8));
loc_00860742:
    if ((*(unsigned __int64 *)(v_stack_m1B8 + 72)) == (*(unsigned __int64 *)(v_stack_m198 + 8))) goto loc_00860AD1;
    if (v_stack_m1B8 == (*(unsigned __int64 *)(v_stack_m198 + 8))) goto loc_00860AD1;
    result = CmpLockKcbShared(*(unsigned __int64 *)(v_stack_m198 + 8), *(unsigned __int64 *)(v_stack_m1B8 + 72), 168, *(unsigned __int64 *)(v_stack_m180 + 8));
    v_stack_m1D5 = 1;
loc_00860768:
    if (v_stack_m198 != 0) {
        a1 = v_stack_m198;
        result = CmpLockKcbStackShared(a1, *(unsigned __int64 *)(v_stack_m1B8 + 72), 168, *(unsigned __int64 *)(v_stack_m180 + 8));
        v_stack_m1E8 = 1;
    }
    result = CmpLockKcbStackShared(0, *(unsigned __int64 *)(v_stack_m1B8 + 72), 168, *(unsigned __int64 *)(v_stack_m180 + 8));
    a2 = 0;
    result = CmpIsKeyDeletedForKeyBody(v_stack_m198, a2, 168, *(unsigned __int64 *)(v_stack_m180 + 8));
    if ((unsigned __int8)(result) != 0) goto loc_008619D9;
    if (((*(unsigned int *)(v_stack_m1B8 + 8)) & (0x20000ULL)) != 0) goto loc_00861A0D;
    v_rdi = (unsigned __int16)(((unsigned int)(v_stack_m1D0)) - 1);
    v_stack_m1D0 = (unsigned int)(v_rdi);
    if (((*(unsigned int *)(v_stack_m1B8 + 184)) & (0x20000ULL)) != 0) goto loc_00861A3B;
    result = CmRmIsKcbStackVisible(0, v_stack_m1C8, 168, *(unsigned __int64 *)(v_stack_m180 + 8));
    if ((unsigned __int8)(result) == 0) goto loc_00861A42;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m1E0)))) & (2)) != 0) goto loc_0086145D;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m1E0)))) & (32)) != 0) goto loc_00860BE0;
    result = CmpIsKeyStackDeleted(0, v_stack_m1C8, 168, *(unsigned __int64 *)(v_stack_m180 + 8));
    if ((unsigned __int8)(result) != 0) goto loc_00860F74;
    result = CmpIsKeyStackSymlink(0, v_stack_m1C8, 168, *(unsigned __int64 *)(v_stack_m180 + 8));
    if ((unsigned __int8)(result) != 0) goto loc_00860E8E;
loc_00860815:
    if (v_stack_m1AF != ((unsigned __int8)(v_rsi))) goto loc_00861D96;
    if (((*(unsigned int *)(v_stack_m1B8 + 184)) & (0x20000ULL)) != 0) goto loc_00861DAC;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m1E0 + 24)))) & (2)) != 0) goto loc_00861DC4;
    a4 = 0;
    v_stack_m218 = v_stack_m160;
    v_stack_m220 = v_stack_m1E0;
    v_stack_m228 = v_rsi;
    result = CmpDoWritethroughReparse(v_stack_m1B8, 0, v_stack_m1A0, a4);
    v_stack_m1E4 = (unsigned int)(result);
    if (((unsigned int)(result)) != 0xC0000271ULL) goto loc_00861A29;
    result = (v_stack_m168) + (32);
    v_stack_m220 = result;
    a3 = 0;
    v_stack_m228 = (unsigned __int8)(v_stack_m1D6);
    result = CmpVEExecuteOpenLogic(v_stack_m1B8, v_stack_m1E0, a3, v_stack_m160);
    v_stack_m1E4 = (unsigned int)(result);
    if (((unsigned int)(result)) != 0xC0000271ULL) goto loc_00861DDC;
    v_stack_m210 = v_stack_m1D2;
    v_stack_m218 = v_stack_m178;
    v_stack_m220 = 0;
    v_stack_m228 = 2;
    result = CmpCreateKeyBody(v_stack_m1B8, v_stack_m1D6, v_stack_m1E0, v_stack_m1C8);
    v_stack_m1E4 = (unsigned int)(result);
    if (sign_flag) goto loc_00861DE9;
loc_008608F5:
    v_rdi = 0;
loc_008608FD:
    if ((*(unsigned int *)(v_stack_m1E0 + 32)) != 1) goto loc_008600E7;
    *(unsigned __int16 *)(v_stack_m178 + 4) = (unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m178 + 8) + 66));
loc_00860917:
    v_stack_m178 = v_rsi;
    *(unsigned __int64 *)(v_stack_m110) = v_stack_m178;
    if ((*(unsigned int *)(v_stack_m1E0 + 32)) == ((unsigned int)(v_rsi))) {
        *(unsigned int *)(v_stack_m1E0 + 32) = 2;
    }
    if (v_stack_m1D2 != ((unsigned __int8)(v_rsi))) goto loc_00861E37;
    v_stack_m1E4 = (unsigned int)(v_rsi);
    v_stack_m1E8 = (unsigned __int8)(v_stack_m1E8);
    v_stack_m1CC = (unsigned __int8)(v_stack_m1CC);
    v_stack_m1D5 = (unsigned __int8)(v_stack_m1D5);
    v_stack_m1D7 = (unsigned __int8)(v_stack_m1D7);
    v_stack_m1A0 = v_stack_m1A0;
    v_stack_m1D4 = 0;
loc_00860973:
    goto loc_00860158;
loc_0086097D:
    result = CmpReferenceKeyControlBlockUnsafe(v_stack_m110, v_stack_m178, (unsigned int)((unsigned int)(result)), v_stack_m1C8);
    v_stack_m1B8 = v_stack_m1E0;
    v_stack_m1A8 = v_stack_m1E0;
    if (v_stack_m1E0 != v_rsi) goto loc_00860B79;
    v_stack_m1D7 = (unsigned __int8)(v_rsi);
loc_008609A0:
    v_stack_m1D8 = (unsigned __int8)(v_stack_m1D3);
    goto loc_0085FAB2;
loc_008609AE:
    v_stack_m1C8 = v_rsi;
    v_stack_m190 = v_rsi;
    goto loc_0085FEA3;
loc_008609BE:
    if ((*(unsigned __int64 *)(v_stack_m1E0 + 32)) == (*(unsigned __int64 *)(v_rip + 7835851))) goto loc_00861972;
    if (v_stack_m1A0 != 0) goto loc_008609DD;
    if (v_stack_m1E0 == 0) goto loc_0085FE22;
loc_008609DD:
    if ((*(unsigned __int16 *)(v_stack_m1E0 + 66)) == ((unsigned __int16)(v_rsi))) goto loc_0085FE22;
    result = CmpLogUnsupportedOperation(8, v_stack_m178, (unsigned int)((unsigned int)(result)), v_stack_m1C8);
    result = PsIsCurrentThreadInServerSilo(8, v_stack_m178, (unsigned int)((unsigned int)(result)), v_stack_m1C8);
    if ((unsigned __int8)(result) != 0) goto loc_00861976;
    v_stack_m1E4 = 0xC0190005ULL;
    result = CmpRecordParseFailure(v_stack_m1E0, (unsigned int)(0xB00ULL), (unsigned int)(0xC0190005ULL), v_stack_m1C8);
    goto loc_00860454;
loc_00860A2A:
    result = CmpUnlockHashEntryByKcb(v_rsi, (unsigned int)(0xB00ULL), (unsigned int)(0xC0190005ULL), v_stack_m1C8);
    v_r14 = 0;
    v_stack_m1D7 = 0;
    goto loc_008606D0;
loc_00860A3F:
    goto loc_0085FFF3;
loc_00860A46:
    goto loc_0085FF6C;
loc_00860A54:
    result = *(unsigned __int64 *)(v_r14 + 24);
    if (v_stack_m1D8 != ((unsigned __int8)(v_rsi))) {
        a1 = v_stack_m1E0;
        result = CmpUnlockHashEntryByKcb(a1, 1, (unsigned int)(0xC0190005ULL), v_stack_m1C8);
        v_stack_m1D8 = (unsigned __int8)(v_rsi);
    }
    result = CmpUnlockRegistry(a1, 1, (unsigned int)(0xC0190005ULL), v_stack_m1C8);
    if (*(unsigned __int64 *)(v_stack_m1E0 + 32) == 0) goto loc_0086142D;
    if ((((unsigned __int8)(v_stack_m1A0)) & (1)) == 0) goto loc_00861437;
    result = CmpTransSearchAddLightWeightTrans(v_stack_m1A0, *(unsigned __int64 *)(v_stack_m1E0 + 32), 1, v_stack_m190);
loc_00860A98:
    v_stack_m1E4 = (unsigned int)(result);
    result = CmpLockRegistry(v_stack_m1A0, *(unsigned __int64 *)(v_stack_m1E0 + 32), 1, v_stack_m190);
    v_stack_m1E7 = 1;
    if (!sign_flag) goto loc_00861985;
loc_00860AB4:
    result = CmpRecordParseFailure(v_stack_m1E0, (unsigned int)(0xC00ULL), (unsigned int)(v_stack_m1E4), v_stack_m190);
    goto loc_00860454;
loc_00860AD1:
    v_rbx = 0;
    goto loc_00860768;
loc_00860AD8:
    a4 = 0;
    v_stack_m228 = v_stack_m190;
    result = CmpTransSearchAddTransFromRm(*(unsigned __int64 *)(v_stack_m1E0 + 4152), 0, v_stack_m1E0, a4);
    v_stack_m1C8 = v_stack_m190;
    goto loc_0085FE9A;
loc_00860B06:
    result = CmpDetachFromRegistryProcess(v_stack_mC8, 0, v_stack_m1E0, a4);
loc_00860B12:
loc_00860B1E:
    a2 = 0;
    result = CmpDrainDelayDerefContext(v_stack_m120, a2, v_stack_m1E0, a4);
    if (v_stack_m1E7 != 0) {
        result = CmpUnlockRegistry(v_stack_m120, a2, v_stack_m1E0, a4);
    }
    if ((unsigned int)((unsigned int)(result)) != 0) goto loc_00860B88;
loc_00860B3A:
    result = (unsigned int)(*(unsigned int *)(v_stack_m1E0 + 160));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m1E0 + 160)))) & (1)) != 0) {
        a1 = v_stack_m1E0 + 168;
        result = CmpDetachFromRegistryProcess(a1, a2, v_stack_m1E0, a4);
    }
    if (v_stack_m178 != 0) goto loc_00860B6F;
loc_00860B59:
    result = CmpCleanupPathInfo(v_stack_m1E0 + 216, v_stack_m178, v_stack_m1E0, a4);
    goto loc_00861E72;
loc_00860B6F:
    result = ObfDereferenceObject(v_stack_m178, v_stack_m178, v_stack_m1E0, a4);
    goto loc_00860B59;
loc_00860B79:
    result = CmpLockHashEntrySharedByKcb(v_stack_m1E0, v_stack_m178, v_stack_m1E0, a4);
    goto loc_008609A0;
loc_00860B88:
    if (v_stack_m1D1 == 0) goto loc_00860BA3;
    result = CmpCheckExeOwnerForPca(v_stack_m1E0, v_stack_m178, v_stack_m1E0, a4);
    if ((unsigned __int8)(result) != 0) {
        a2 = (unsigned int)((unsigned int)(result));
        a1 = v_stack_m1E0;
        result = CmpPublishEventForPcaResolver(a1, a2, v_stack_m1E0, a4);
    }
    result = CmpFreePoolWithTag((unsigned int)((unsigned int)(result)), (unsigned int)(0x624E4D43ULL), v_stack_m1E0, a4);
    goto loc_00860B3A;
loc_00860BB2:
    result = CmpLockRegistryExclusive((unsigned int)((unsigned int)(result)), (unsigned int)(0x624E4D43ULL), v_stack_m1E0, a4);
    goto loc_0085FA13;
loc_00860BBC:
    if (*(unsigned __int64 *)(v_stack_m1E0 + 56) == 0) goto loc_00860BCE;
    if (0 != (*(unsigned __int64 *)(v_stack_m1E0 + 56))) goto loc_00861845;
loc_00860BCE:
    if (0 == 0) goto loc_0085F912;
    v_stack_m158 = v_rsi;
    goto loc_0085F91E;
loc_00860BE0:
    result = CmpUnlockKcbStack((unsigned int)((unsigned int)(result)), (unsigned int)(0x624E4D43ULL), v_stack_m1E0, a4);
    result = CmpUnlockKcbStack(v_stack_m1A0, (unsigned int)(0x624E4D43ULL), v_stack_m1E0, a4);
    result = CmpLockKcbStackTopExclusiveRestShared(v_stack_m1A0, (unsigned int)(0x624E4D43ULL), v_stack_m1E0, a4);
    result = CmpLockKcbStackTopExclusiveRestShared((unsigned int)((unsigned int)(result)), (unsigned int)(0x624E4D43ULL), v_stack_m1E0, a4);
    result = CmpIsKeyStackDeleted(v_stack_m1A0, v_stack_m1C8, v_stack_m1E0, a4);
    if ((unsigned __int8)(result) != 0) goto loc_00861B94;
    if (((*(unsigned int *)(*(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 72) + 184)) & (0x20000ULL)) != 0) goto loc_00861B9E;
    result = CmpGetComponentNameAtIndex(v_stack_m188, (__int16)((unsigned __int16)(v_stack_m1E0)), v_stack_m1E0, a4);
    if (((*(unsigned int *)((unsigned int)((unsigned int)(result)) + 184)) & (0x400000ULL)) == 0) goto loc_0086100D;
loc_00860C49:
    *(unsigned int *)((unsigned int)((unsigned int)(result)) + 100) = 0xFFFFFFFFULL;
    *(unsigned int *)((unsigned int)((unsigned int)(result)) + 96) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m1E0 + 56)));
    v_stack_m210 = v_stack_m1D2;
    v_stack_m218 = v_stack_m178;
    v_stack_m220 = (unsigned int)((unsigned int)(result));
    v_stack_m228 = 3;
    result = CmpCreateKeyBody((unsigned int)((unsigned int)(result)), v_stack_m1D6, v_stack_m1E0, v_stack_m1C8);
    v_stack_m1E4 = (unsigned int)(result);
    if (sign_flag) goto loc_00861BA8;
    result = CmpIsKeyStackDeleted((unsigned int)((unsigned int)(result)), v_stack_m1C8, v_stack_m1E0, v_stack_m1C8);
    if ((unsigned __int8)(result) == 0) goto loc_00861E07;
    v_stack_m208 = v_stack_m1C8;
    v_stack_m210 = (unsigned __int8)(v_rsi);
    v_stack_m218 = (unsigned int)(v_rsi);
    v_stack_m220 = 64;
    v_stack_m228 = v_stack_m1E0;
    result = CmpCreateChild(v_stack_m1A0, (unsigned int)((unsigned int)(result)), v_stack_m168, result);
    v_stack_m1E4 = (unsigned int)(result);
    if (sign_flag) goto loc_00860FFB;
    *(unsigned int *)(v_stack_m1E0 + 32) = 1;
    goto loc_008608F5;
loc_00860D09:
    if ((unsigned __int16)(v_stack_m1A0) != 0) goto loc_0085FD10;
    a3 = (unsigned __int16)((*(unsigned __int16 *)((unsigned int)((unsigned int)(result)))) - ((unsigned __int16)(*(unsigned __int16 *)((unsigned int)((unsigned int)(result))))));
    a1 = ((unsigned int)((unsigned int)(*(unsigned __int16 *)((unsigned int)((unsigned int)(result)))))) >> (1);
    a4 = (unsigned __int16)((*(unsigned __int16 *)((unsigned int)((unsigned int)(result)) + 2)) - ((unsigned __int16)(*(unsigned __int16 *)((unsigned int)((unsigned int)(result))))));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsi + 80))))) & (1)) == 0) goto loc_008610F9;
    a1 = (unsigned __int16)((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsi + 80) + 24)) + ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsi + 80) + 24))));
loc_00860D4C:
    result = ((unsigned int)((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsi + 80) + 24)))) + ((unsigned int)((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsi + 80) + 24))));
    a3 = (unsigned __int16)((a3) + ((unsigned __int16)(a1)));
    v_r10 = (*(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 8) + a1 * 2) - (result);
    v_stack_m150 = a3;
    a4 = (unsigned __int16)((a4) + ((unsigned __int16)(a1)));
    v_stack_m148 = v_r10;
    v_stack_m14E = (unsigned __int16)(a4);
    v_rdi = (unsigned int)((v_stack_m1E0) - 1);
    v_stack_m1D0 = 1;
    goto loc_0085FD15;
loc_00860D7A:
loc_00860D89:
    result = CmpRecordParseFailure(v_stack_m1E0, (unsigned int)(0x1580ULL), (unsigned int)(v_stack_m1E4), a4);
    goto loc_00860454;
loc_00860DA0:
    result = CmpDereferenceKeyControlBlockUnsafe(v_stack_m1B8, (unsigned int)(0x1580ULL), (unsigned int)(v_stack_m1E4), a4);
    goto loc_008604B0;
loc_00860DB0:
    result = CmpUnlockHashEntryByKcb(v_rsi, (unsigned int)(0x1580ULL), (unsigned int)(v_stack_m1E4), a4);
    goto loc_0086046E;
loc_00860DBD:
    result = CmpUnlockHashEntry(*(unsigned __int64 *)(v_stack_m1E0 + 48), (unsigned int)((unsigned int)(v_rsi)), (unsigned int)(v_stack_m1E4), a4);
    goto loc_00860454;
loc_00860DD3:
    result = CmpLockRegistryExclusive(*(unsigned __int64 *)(v_stack_m1E0 + 48), (unsigned int)((unsigned int)(v_rsi)), (unsigned int)(v_stack_m1E4), a4);
    goto loc_0085FC56;
loc_00860DDD:
    v_stack_m1C8 = v_stack_m190;
    goto loc_0085FE81;
loc_00860DF0:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)((unsigned int)(0xC0190002ULL))))) & (8)) != 0) goto loc_0086182E;
    result = (unsigned int)(*(unsigned int *)((unsigned int)(0xC0190002ULL) + 160));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)((unsigned int)(0xC0190002ULL) + 160)))) & (1)) == 0) {
        a1 = (unsigned int)(0xC0190002ULL) + 168;
        result = CmpAttachToRegistryProcess(a1, (unsigned int)((unsigned int)(v_rsi)), (unsigned int)(v_stack_m1E4), a4);
    }
    if (((*(unsigned int *)(v_stack_m1B8 + 184)) & (0x2000000ULL)) != 0) goto loc_008610EC;
    v_stack_m228 = v_stack_m1E0;
    result = CmpVEExecuteRealStoreParseLogic(v_stack_m1B8, v_stack_m98, (unsigned int)(0xC0190002ULL), v_stack_m160);
    goto loc_0085FB34;
loc_00860E4E:
    if (*(unsigned __int64 *)(v_stack_m1B8 + 192) == 0) goto loc_0085FF18;
loc_00860E70:
    result = CmpSetKcbAtLayerHeight(v_stack_m108, v_stack_m98, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m1B8 + 192) + 16), *(unsigned __int64 *)(v_stack_m1B8 + 192));
    a2 = (unsigned __int16)((v_stack_m98) - 1);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m1B8 + 192) + 24) != 0) goto loc_00860E70;
    goto loc_0085FF18;
loc_00860E8E:
    if (condition_is_below) goto loc_00860815;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)((unsigned int)(0xC0190002ULL) + 24)))) & (2)) != 0) goto loc_00861D49;
    if (v_stack_m1E8 != ((unsigned __int8)(v_rsi))) goto loc_008610AA;
loc_00860EAE:
    result = (unsigned int)(*(unsigned int *)((unsigned int)(0xC0190002ULL) + 24));
    if ((unsigned __int8)(v_stack_m1A0) != 0) {
        result = v_stack_m198;
        a1 = *(unsigned __int64 *)(result + 8);
        result = CmpUnlockKcb(a1, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m1B8 + 192) + 16), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m1B8 + 192) + 24));
        v_stack_m1D5 = (unsigned __int8)(v_rsi);
    }
    if (v_stack_m1D8 != ((unsigned __int8)(v_rsi))) goto loc_00861D61;
loc_00860ECF:
    a4 = 0;
    v_stack_m200 = v_stack_m140;
    v_stack_m208 = (unsigned int)(0xC0190002ULL) + 88;
    a3 = 0;
    v_stack_m210 = v_stack_m160;
    v_stack_m218 = v_stack_m120;
    v_stack_m220 = (unsigned int)(0xC0190002ULL);
    v_stack_m228 = v_stack_m1C8;
    result = CmpGetSymbolicLinkTarget((unsigned int)(0xC0190002ULL), (unsigned int)(0xC0190002ULL) + 216, a3, a4);
    v_stack_m1E4 = (unsigned int)(result);
    if (sign_flag) goto loc_00861D73;
    if ((*(unsigned __int64 *)((unsigned int)(0xC0190002ULL) + 64)) != v_rsi) goto loc_00860F42;
    if ((((unsigned __int8)(v_stack_m1E7)) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m140 + 32) + 4112))))) != 0) goto loc_00861D8D;
loc_00860F42:
    v_stack_m1E4 = 260;
    result = CmpRecordParseFailure((unsigned int)(0xC0190002ULL), (unsigned int)(0x3900ULL), 260, a4);
    goto loc_00860171;
loc_00860F67:
    goto loc_0085FB34;
loc_00860F74:
    if (v_stack_m1AF != ((unsigned __int8)(v_rsi))) goto loc_00861BB2;
    result = CmpIsKeyStackDeleted(v_stack_m1A0, v_stack_m1C8, 260, a4);
    if ((unsigned __int8)(result) != 0) goto loc_00861A14;
    result = CmRmIsKcbStackVisible(v_stack_m1A0, v_stack_m1C8, 260, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00861A14;
    if (((*(unsigned int *)(*(unsigned __int64 *)(v_stack_m1B8 + 72) + 184)) & (0x20000ULL)) != 0) goto loc_00861BC8;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m1E0)))) & (1)) != 0) goto loc_0086119E;
    v_stack_m1E4 = 0xC0000034ULL;
loc_00860FF3:
    result = CmpRecordParseFailure(v_stack_m1E0, (unsigned int)(0x2A00ULL), (unsigned int)(0xC0000034ULL), a4);
loc_00860FFB:
    result = CmpUnlockKcbStack((unsigned int)(0xC0190002ULL), (unsigned int)(0x2A00ULL), (unsigned int)(0xC0000034ULL), a4);
    goto loc_00860171;
loc_0086100D:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m1B8 + 8)))) & (8)) == 0) goto loc_00860C49;
    result = CmpDelayDerefKeyControlBlock(*(unsigned __int64 *)(v_stack_m1B8 + 104), v_stack_m120, (unsigned int)(0xC0000034ULL), a4);
    *(unsigned __int64 *)(v_stack_m1B8 + 104) = v_rsi;
    goto loc_00860C49;
loc_0086103A:
    a2 = ((unsigned int)((unsigned int)((unsigned int)(0xFFF7ULL)))) << (3);
    result = CmpAllocatePool(256, a2, (unsigned int)(0x35364D43ULL), a4);
    if (result != 0) goto loc_0085FEBB;
    goto loc_0086108A;
loc_00861063:
    a2 = ((unsigned int)((unsigned int)(result))) << (3);
    result = CmpAllocatePool(256, a2, (unsigned int)(0x35364D43ULL), a4);
    if (result != 0) goto loc_0085FEE4;
loc_0086108A:
    v_stack_m1E4 = 0xC000009AULL;
    result = CmpRecordParseFailure(v_stack_m1E0, (unsigned int)(0xE00ULL), (unsigned int)(0xC000009AULL), a4);
    goto loc_0086020A;
loc_008610AA:
    result = CmpUnlockKcbStack(v_stack_m1A0, (unsigned int)(0xE00ULL), (unsigned int)(0xC000009AULL), a4);
    v_stack_m1E8 = (unsigned __int8)(v_rsi);
    goto loc_00860EAE;
loc_008610BD:
    v_stack_m1E4 = 0xC0000034ULL;
    result = CmpRecordParseFailure(v_stack_m1E0, (unsigned int)(0xF80ULL), (unsigned int)(0xC0000034ULL), a4);
    v_rbx = 0;
    result = CmpUnlockKcbStack((unsigned int)(0xC0190002ULL), (unsigned int)(0xF80ULL), (unsigned int)(0xC0000034ULL), a4);
    goto loc_00860171;
loc_008610EC:
    result = CmpVEExecuteVirtualStoreParseLogic((unsigned int)(0xC0190002ULL), (unsigned int)(0xF80ULL), (unsigned int)(0xC0000034ULL), a4);
    goto loc_0085FB34;
loc_008610F9:
    result = (result) >> (1);
    goto loc_00860D4C;
loc_00861101:
    if ((*(unsigned __int64 *)(v_rip + 6875703)) == (*(unsigned __int64 *)(gs_base + (0 + 392)))) goto loc_008619CC;
    v_stack_m1B8 = v_stack_m1A8;
    if ((*(unsigned __int64 *)(v_stack_m1A8 + 32)) != (*(unsigned __int64 *)(v_rip + 7833966))) goto loc_008600B8;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m1A8 + 8))) & (0x7FE00000ULL));
    if (((unsigned int)(result)) != 0x600000ULL) goto loc_008600B8;
    if (condition_is_less_or_equal) goto loc_008600B8;
    a2 = (unsigned int)(((__int16)(0)) - 1);
    result = CmpGetComponentNameAtIndex(v_stack_m188, a2, (unsigned int)(0xC0000034ULL), a4);
    result = CmpWaitForHiveMount(result, a2, (unsigned int)(0xC0000034ULL), v_stack_m1E0 + 136);
    if ((unsigned __int8)(result) == 0) goto loc_008600BD;
    v_stack_m1E4 = 259;
    result = CmpRecordParseFailure(v_stack_m1E0, (unsigned int)(0xF00ULL), 259, v_stack_m1E0 + 136);
    v_rbx = 0;
    goto loc_008600DA;
loc_0086119E:
    result = CmpGetComponentNameAtIndex(259 + 216, (__int16)((unsigned __int16)(v_stack_m1E0)), 259, v_stack_m1E0 + 136);
    v_stack_m218 = v_stack_m160;
    v_stack_m220 = 259;
    v_stack_m228 = result;
    result = CmpDoWritethroughReparse(v_stack_m1B8, (unsigned int)(0xC0190002ULL), v_stack_m1A0, 1);
    v_stack_m1E4 = (unsigned int)(result);
    if (((unsigned int)(result)) != 0xC0000271ULL) goto loc_00861BD2;
    v_stack_m210 = v_stack_m1D2;
    v_stack_m218 = v_stack_m178;
    v_stack_m220 = (unsigned int)(0xC0190002ULL);
    v_stack_m228 = (unsigned int)(v_rsi);
    result = CmpCreateKeyBody(v_stack_m1B8, v_stack_m1D6, v_stack_m1E0, v_stack_m1C8);
    v_stack_m1E4 = (unsigned int)(result);
    if (sign_flag) goto loc_00861BDF;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m1E0 + 160)))) & (1)) == 0) goto loc_00861BEC;
loc_00861249:
    result = CmpUnlockKcbStack((unsigned int)(0xC0190002ULL), v_stack_m1D6, v_stack_m1E0, v_stack_m1C8);
    result = CmpUnlockKcbStack(v_stack_m1A0, v_stack_m1D6, v_stack_m1E0, v_stack_m1C8);
    result = CmpLockKcbStackTopExclusiveRestShared(v_stack_m1A0, v_stack_m1D6, v_stack_m1E0, v_stack_m1C8);
    result = CmpLockKcbStackTopExclusiveRestShared((unsigned int)(0xC0190002ULL), v_stack_m1D6, v_stack_m1E0, v_stack_m1C8);
    result = CmRmIsKcbStackVisible((unsigned int)(0xC0190002ULL), v_stack_m1C8, v_stack_m1E0, v_stack_m1C8);
    if ((unsigned __int8)(result) == 0) goto loc_00861C0A;
    if (((*(unsigned int *)(v_stack_m1B8 + 8)) & (0x20000ULL)) != 0) goto loc_008617AB;
    result = CmpIsKeyStackDeleted((unsigned int)(0xC0190002ULL), v_stack_m1C8, v_stack_m1E0, v_stack_m1C8);
    if ((unsigned __int8)(result) == 0) goto loc_00861CFD;
    result = CmpIsKeyStackDeleted(v_stack_m1A0, v_stack_m1C8, v_stack_m1E0, v_stack_m1C8);
    if ((unsigned __int8)(result) != 0) goto loc_00861CD6;
    result = CmRmIsKcbStackVisible(v_stack_m1A0, v_stack_m1C8, v_stack_m1E0, v_stack_m1C8);
    if ((unsigned __int8)(result) == 0) goto loc_00861CD6;
    if (((*(unsigned int *)(*(unsigned __int64 *)(v_stack_m1B8 + 72) + 184)) & (0x20000ULL)) != 0) goto loc_00861C31;
    v_stack_m208 = v_stack_m160;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m1E0 + 24))) & (2));
    v_stack_m210 = v_stack_m1E0;
    v_stack_m218 = v_stack_m1C8;
    result = (unsigned int)((result) << (4));
    v_stack_m220 = (unsigned int)(result);
    v_stack_m228 = (unsigned __int8)(v_stack_m1D6);
    result = CmpVEExecuteCreateLogic(*(unsigned __int64 *)(v_stack_m1B8 + 72), v_stack_m1B8, result, v_stack_m168);
    v_stack_m1E4 = (unsigned int)(result);
    if (((unsigned int)(result)) == 0xC0000055ULL) goto loc_00861C58;
    if (((unsigned int)(result)) != 0xC0000271ULL) goto loc_00861C82;
    v_stack_m1F8 = v_stack_m1E4;
    v_stack_m200 = (unsigned int)(v_rsi);
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m1E0 + 24))) & (2));
    v_stack_m208 = v_stack_m178;
    v_stack_m210 = v_stack_m1C8;
    a2 = (unsigned int)((a2) << (4));
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m1E0 + 24))))) >> (2));
    a1 = (unsigned __int8)((a1) & (1));
    v_stack_m218 = (unsigned __int8)(a1);
    v_stack_m220 = (unsigned int)(a2);
    v_stack_m228 = (unsigned __int8)(v_stack_m1D6);
    result = CmpCheckCreateAccessOnKcbStack(a1, v_stack_m1A0, v_stack_m1E0, v_stack_m168);
    v_stack_m228 = (unsigned int)(0xC0190002ULL);
    result = CmpEnlistKeyBody(v_stack_m178, v_stack_m1B8, v_stack_m1C8, 1);
    v_stack_m1E4 = (unsigned int)(result);
    if (sign_flag) goto loc_00861C9E;
    v_stack_m208 = v_stack_m1C8;
    v_stack_m210 = (unsigned __int8)(v_rsi);
    result = (unsigned __int16)((*(unsigned __int16 *)(v_stack_m1E0 + 24)) & (2));
    result = (unsigned __int16)((result) << (3));
    v_stack_m218 = (unsigned int)(v_rsi);
    v_stack_m220 = (unsigned __int16)(result);
    v_stack_m228 = v_stack_m1E0;
    result = CmpCreateChild(v_stack_m1A0, (unsigned int)(0xC0190002ULL), v_stack_m168, result);
    v_stack_m1E4 = (unsigned int)(result);
    if (sign_flag) goto loc_00861CBA;
    *(unsigned int *)(v_stack_m1E0 + 32) = 1;
    v_stack_m1E8 = 1;
loc_00861425:
    v_rdi = 0;
    goto loc_008617A2;
loc_0086142D:
    goto loc_00860A98;
loc_00861437:
    v_stack_m228 = v_stack_m190;
    result = CmpTransSearchAddTransFromRm(*(unsigned __int64 *)(v_stack_m1E0 + 4152), result, 0, 1);
    goto loc_00860A98;
loc_0086145D:
    result = CmpUnlockKcbStack(*(unsigned __int64 *)(v_stack_m1E0 + 4152), result, 0, 1);
    result = CmpUnlockKcbStack(v_stack_m1A0, result, 0, 1);
    if ((unsigned __int8)(result) != 0) goto loc_00861A49;
loc_00861477:
    result = CmpTryToLockHashEntryExclusive(*(unsigned __int64 *)(v_stack_m1E0 + 48), (unsigned int)((unsigned int)(v_rsi)), 0, 1);
    v_stack_m1D4 = (unsigned __int8)(result);
    if ((unsigned __int8)(result) != 0) goto loc_00861A57;
loc_00861493:
    result = CmpLockKcbStackTopExclusiveRestShared(v_stack_m1A0, (unsigned int)((unsigned int)(v_rsi)), 0, 1);
    result = CmpLockKcbStackTopExclusiveRestShared((unsigned int)(0xC0190002ULL), (unsigned int)((unsigned int)(v_rsi)), 0, 1);
    result = CmpGetComponentNameAtIndex(v_stack_m188, (unsigned int)((unsigned int)((__int16)((unsigned __int16)((unsigned int)(v_stack_m1D0))))), (__int16)((unsigned __int16)((unsigned int)(v_stack_m1D0))), 1);
    result = CmpGetComponentHashAtIndex(v_stack_m188, (unsigned int)((unsigned int)((__int16)((unsigned __int16)((unsigned int)(v_stack_m1D0))))), (__int16)((unsigned __int16)((unsigned int)(v_stack_m1D0))), 1);
    a2 = 0;
    result = CmpIsKeyDeletedForKeyBody(v_stack_m198, a2, (__int16)((unsigned __int16)((unsigned int)(v_stack_m1D0))), 1);
    if ((unsigned __int8)(result) != 0) goto loc_00861A65;
    result = CmpIsKeyStackDeleted(v_stack_m1A0, v_stack_m1C8, (__int16)((unsigned __int16)((unsigned int)(v_stack_m1D0))), 1);
    if ((unsigned __int8)(result) != 0) goto loc_00861A88;
    result = CmpIsKeyStackDeleted((unsigned int)(0xC0190002ULL), v_stack_m1C8, (__int16)((unsigned __int16)((unsigned int)(v_stack_m1D0))), 1);
    if ((unsigned __int8)(result) == 0) goto loc_00861A8F;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m1B8 + 72) + 32)) != (*(unsigned __int64 *)(v_rip + 7832962))) goto loc_00861AA4;
    if (((*(unsigned int *)(*(unsigned __int64 *)(v_stack_m1B8 + 72) + 184)) & (0x20000ULL)) != 0) goto loc_00861ABC;
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m1E0 + 160))))) == 0) goto loc_00861AC6;
loc_00861541:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m1E0 + 40)))) != -1) goto loc_00861AF1;
    v_stack_m228 = v_stack_m1E0 + 40;
    result = CmpCreateHiveRootCell(*(unsigned __int64 *)(v_stack_m1E0 + 48), v_stack_m168, result, v_stack_m1E0);
    v_stack_m1E4 = (unsigned int)(result);
    if (sign_flag) goto loc_00861AE4;
loc_00861576:
    v_stack_m208 = v_stack_m128;
    v_stack_m210 = (unsigned int)(v_rsi);
    v_stack_m218 = (unsigned int)((unsigned int)((unsigned int)(result)));
    v_stack_m220 = result;
    v_stack_m228 = 1;
    result = CmpCreateKeyControlBlock(*(unsigned __int64 *)(v_stack_m1E0 + 48), (unsigned int)(0xFFFFFFFFULL), v_stack_m1B8, *(unsigned __int64 *)(v_stack_m1E0 + 80));
    v_stack_m1E4 = (unsigned int)(result);
    if (sign_flag) goto loc_00861B0F;
    v_stack_m1B8 = v_stack_m128;
    result = CmpDereferenceKeyControlBlockUnsafe(v_stack_m1B8, (unsigned int)(0xFFFFFFFFULL), (unsigned int)(v_stack_m1E4), *(unsigned __int64 *)(v_stack_m1E0 + 80));
    result = CmpUnlockHashEntryByKcb(v_stack_m1B8, (unsigned int)(0xFFFFFFFFULL), (unsigned int)(v_stack_m1E4), *(unsigned __int64 *)(v_stack_m1E0 + 80));
    v_stack_m1D8 = (unsigned __int8)(v_rsi);
    result = CmpStartKcbStackForTopLayerKcb(v_stack_mC8, v_stack_m1B8, (unsigned int)(v_stack_m1E4), *(unsigned __int64 *)(v_stack_m1E0 + 80));
    v_stack_m1E4 = (unsigned int)(result);
    if (sign_flag) goto loc_00861B19;
    result = CmpLockKcbStackTopExclusiveRestShared(v_stack_mC8, v_stack_m1B8, (unsigned int)(v_stack_m1E4), *(unsigned __int64 *)(v_stack_m1E0 + 80));
    v_stack_m210 = v_stack_m1D2;
    v_stack_m218 = v_stack_m178;
    v_stack_m220 = v_stack_mC8;
    v_stack_m228 = 3;
    v_stack_m1CC = 1;
    result = CmpCreateKeyBody(v_stack_m1B8, v_stack_m1D6, v_stack_m1E0, v_stack_m1C8);
    v_stack_m1E4 = (unsigned int)(result);
    if (sign_flag) goto loc_00861B26;
    result = HvLockHiveFlusherShared(*(unsigned __int64 *)(v_stack_m1B8 + 32), v_stack_m1D6, v_stack_m1E0, v_stack_m1C8);
    result = HvLockHiveFlusherExclusive(*(unsigned __int64 *)(v_stack_m1B8 + 32), v_stack_m1D6, v_stack_m1E0, v_stack_m1C8);
    a4 = 0;
    a3 = 0;
    v_stack_m1D0 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m1B8 + 32) + 104)));
    result = HvpMarkCellDirty(*(unsigned __int64 *)(v_stack_m1B8 + 32), (unsigned int)(*(unsigned int *)(v_stack_m1E0 + 40)), a3, a4);
    v_stack_m1E4 = (unsigned int)(result);
    if (sign_flag) goto loc_00861B4C;
    v_stack_m208 = v_stack_m1C8;
    v_stack_m210 = 1;
    v_stack_m218 = (unsigned int)(v_rsi);
    v_stack_m220 = 10;
    v_stack_m228 = v_stack_m1E0;
    result = CmpCreateChild(v_stack_m1A0, (unsigned int)(0xC0190002ULL), v_stack_m168, result);
    v_stack_m1E4 = (unsigned int)(result);
    if (sign_flag) goto loc_00861B5E;
    *(unsigned int *)(v_stack_m1B8 + 40) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m1E0 + 40)));
    result = CmpGetKeyNodeForKcb(v_stack_m1B8, v_stack_m138, 1, result);
    a4 = 0;
    a3 = 0;
    *(unsigned int *)(result + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m1B8 + 40)));
    result = CmpRebuildKcbCacheFromNode(v_stack_m1B8, result, a3, a4);
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m1B8 + 32) + 140)) & (1)) != 0) goto loc_0086183B;
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(v_stack_m1B8 + 32), v_stack_m138, a3, a4);
loc_00861756:
    if (v_stack_m1D0 == ((unsigned int)(v_rsi))) goto loc_00861B86;
loc_00861760:
    result = HvUnlockHiveFlusherExclusive(*(unsigned __int64 *)(v_stack_m1B8 + 32), v_stack_m138, a3, a4);
    result = HvUnlockHiveFlusherShared(*(unsigned __int64 *)(v_stack_m1B8 + 32), v_stack_m138, a3, a4);
    result = CmpReferenceKeyControlBlockUnsafe(v_stack_m1B8, v_stack_m138, a3, a4);
    *(unsigned __int64 *)(v_stack_m1B8 + 104) = v_stack_m1B8;
    result = CmpUnlockHashEntry(*(unsigned __int64 *)(v_stack_m1E0 + 48), (unsigned int)((unsigned int)(v_rsi)), a3, a4);
    v_rdi = 0;
    v_stack_m1D4 = 0;
    *(unsigned int *)(v_stack_m1E0 + 32) = 1;
loc_008617A2:
    goto loc_008608FD;
loc_008617AB:
    v_stack_m1E4 = 0xC0000034ULL;
    result = CmpRecordParseFailure(v_stack_m1E0, (unsigned int)(0x2F80ULL), (unsigned int)(0xC0000034ULL), a4);
    goto loc_00860168;
loc_008617D2:
    v_stack_m1A0 = v_rsi;
    goto loc_00860742;
loc_008617DE:
    result = (*(unsigned __int64 *)(v_rip + 5932939)) & ((unsigned int)(0xC0000034ULL));
    if (result != (*(unsigned __int64 *)(v_rip + 5932929))) goto loc_008603DA;
    goto loc_008603DC;
loc_008617FC:
    a4 = 0;
    v_stack_m220 = v_stack_m98;
    a3 = 0;
    v_stack_m228 = 2;
    result = tlgWriteTransfer_EtwWriteTransfer(v_rip + 5932852, v_rip - 8434840, a3, a4);
    goto loc_00860432;
loc_0086182E:
    goto loc_0085FB34;
loc_0086183B:
    result = HvpReleaseCellFlat(v_rip + 5932852, v_rip - 8434840, a3, a4);
    goto loc_00861756;
loc_00861845:
    v_stack_m1E4 = (unsigned int)((unsigned int)(0xC0190002ULL));
    result = CmpRecordParseFailure(v_stack_m1E0, 256, (unsigned int)((unsigned int)((unsigned int)(0xC0190002ULL))), a4);
    v_r12 = 0;
    goto loc_00860454;
loc_0086186D:
loc_00861877:
    v_stack_m1E4 = (unsigned int)((unsigned int)(0xC000000DULL));
loc_0086188A:
    v_stack_m1E4 = (unsigned int)((unsigned int)(0xC000000DULL));
loc_0086189D:
    result = CmpRecordParseFailure(v_stack_m1E0, (unsigned int)(0x500ULL), (unsigned int)((unsigned int)((unsigned int)(0xC000000DULL))), a4);
    goto loc_0086020A;
loc_008618B7:
    v_stack_m1E4 = (unsigned int)((unsigned int)(0xC000000DULL));
    result = CmpRecordParseFailure(v_stack_m1E0, (unsigned int)(0x600ULL), (unsigned int)((unsigned int)((unsigned int)(0xC000000DULL))), a4);
    v_stack_m1E7 = (unsigned __int8)(v_stack_m1E7);
    v_stack_m1D7 = (unsigned __int8)((unsigned int)(0xC0190002ULL));
    goto loc_00860454;
loc_008618EA:
    v_stack_m1E4 = (unsigned int)((unsigned int)(0xC000000DULL));
    result = CmpRecordParseFailure(0, (unsigned int)(0x700ULL), (unsigned int)((unsigned int)((unsigned int)(0xC000000DULL))), a4);
    goto loc_0086020A;
loc_0086190B:
    a3 = (unsigned int)(0xC0000425ULL);
    if ((((unsigned __int8)(result)) & (1)) == 0) { a3 = (unsigned int)((unsigned int)(0xC000017CULL)); }
    v_stack_m1E4 = a3;
    result = CmpRecordParseFailure(v_stack_m1E0, (unsigned int)(0x800ULL), a3, a4);
    goto loc_0086020A;
loc_00861938:
    result = CmpRecordParseFailure(v_stack_m1E0, (unsigned int)(0x9C0ULL), a3, a4);
    goto loc_0086020A;
loc_0086194A:
    *(unsigned int *)(v_stack_m1E0 + result * 8 + 428) = 0xC0000022ULL;
    *(unsigned int *)(v_stack_m1E0 + *(unsigned __int8 *)(v_stack_m1E0 + 426) * 8 + 432) = 0xA00ULL;
    goto loc_00860454;
loc_00861972:
    v_stack_m1AF = 1;
loc_00861976:
    v_stack_m158 = v_rsi;
    goto loc_0085FE22;
loc_00861985:
    v_stack_m1E4 = (unsigned int)((unsigned int)(0xC000022DULL));
    goto loc_00860AB4;
loc_00861995:
    goto loc_008619A1;
loc_0086199C:
loc_008619A1:
    v_stack_m1E4 = 259;
    goto loc_00860D89;
loc_008619BF:
    goto loc_00860D89;
loc_008619CC:
    v_stack_m1B8 = v_stack_m1A8;
    goto loc_008600B8;
loc_008619D9:
    a3 = (unsigned int)(0xC0000425ULL);
    if (((*(unsigned __int8 *)(v_stack_m1E0 + 48)) & ((unsigned __int8)(v_stack_m1E7))) == 0) { a3 = (unsigned int)((unsigned int)(0xC000017CULL)); }
    v_stack_m1E4 = a3;
    result = CmpRecordParseFailure(v_stack_m1E0, (unsigned int)(0x1700ULL), a3, a4);
    goto loc_008600DA;
loc_00861A0D:
    goto loc_00861A19;
loc_00861A14:
loc_00861A19:
    v_stack_m1E4 = 0xC0000034ULL;
    goto loc_00861A31;
loc_00861A29:
loc_00861A31:
    goto loc_00860FF3;
loc_00861A3B:
    goto loc_00861A19;
loc_00861A42:
    goto loc_00861A19;
loc_00861A49:
    result = CmpUnlockKcb(*(unsigned __int64 *)(v_stack_m1B8 + 8), (unsigned int)(0x1900ULL), (unsigned int)((unsigned int)(result)), a4);
    goto loc_00861477;
loc_00861A57:
    result = CmpLockKcbShared(*(unsigned __int64 *)(v_stack_m1B8 + 8), (unsigned int)(0x1900ULL), (unsigned int)((unsigned int)(result)), a4);
    goto loc_00861493;
loc_00861A65:
    a3 = (unsigned int)(0xC0000425ULL);
    if (((*(unsigned __int8 *)(v_stack_m198 + 48)) & ((unsigned __int8)(v_stack_m1E7))) == 0) { a3 = (unsigned int)((unsigned int)(0xC000017CULL)); }
    v_stack_m1E4 = a3;
    goto loc_00861A31;
loc_00861A88:
    goto loc_00861A19;
loc_00861A8F:
    v_stack_m1E4 = 0xC0000022ULL;
    goto loc_00861A31;
loc_00861AA4:
    v_stack_m1E4 = 0xC0000022ULL;
    goto loc_00861A31;
loc_00861ABC:
    goto loc_00861A19;
loc_00861AC6:
    result = CmpAttachToRegistryProcess((unsigned int)(0xC0000022ULL) + 168, (unsigned int)(0x1E00ULL), (unsigned int)(0xC0000022ULL), a4);
    goto loc_00861541;
loc_00861AE4:
    goto loc_00861A31;
loc_00861AF1:
    result = CmpUpdateHiveRootCellFlags((unsigned int)(0xC0000022ULL) + 168, (unsigned int)(0x1E80ULL), (unsigned int)((unsigned int)(result)), a4);
    v_stack_m1E4 = (unsigned int)(result);
    if (!sign_flag) goto loc_00861576;
    goto loc_00861A31;
loc_00861B0F:
    goto loc_00861A31;
loc_00861B19:
    goto loc_00861A31;
loc_00861B26:
    result = CmpRecordParseFailure(v_stack_m1E0, (unsigned int)(0x2180ULL), (unsigned int)((unsigned int)(result)), a4);
loc_00861B3B:
    result = CmpUnlockKcbStack(v_stack_mC8, (unsigned int)(0x2180ULL), (unsigned int)((unsigned int)(result)), a4);
    goto loc_00860163;
loc_00861B4C:
    result = CmpRecordParseFailure(v_stack_m1E0, (unsigned int)(0x2200ULL), (unsigned int)((unsigned int)(result)), a4);
loc_00861B5E:
    result = HvUnlockHiveFlusherExclusive(*(unsigned __int64 *)(v_stack_m1B8 + 32), (unsigned int)(0x2200ULL), (unsigned int)((unsigned int)(result)), a4);
    result = HvUnlockHiveFlusherShared(*(unsigned __int64 *)(v_stack_m1E8 + 32), (unsigned int)(0x2200ULL), (unsigned int)((unsigned int)(result)), a4);
    v_stack_m1E7 = (unsigned __int8)(v_stack_m1E7);
    v_stack_m180 = v_rsi;
    goto loc_00860973;
loc_00861B86:
    result = HvResetDirtyData(*(unsigned __int64 *)(v_stack_m1B8 + 32), (unsigned int)(0x2200ULL), (unsigned int)((unsigned int)(result)), a4);
    goto loc_00861760;
loc_00861B94:
    goto loc_00861A19;
loc_00861B9E:
    goto loc_00861A19;
loc_00861BA8:
    goto loc_00860FFB;
loc_00861BB2:
    v_stack_m1E4 = (unsigned int)((unsigned int)(0xC000000DULL));
    goto loc_00861A31;
loc_00861BC8:
    goto loc_00861A19;
loc_00861BD2:
    goto loc_00861A31;
loc_00861BDF:
    goto loc_00861A31;
loc_00861BEC:
    result = CmpAttachToRegistryProcess((unsigned int)((unsigned int)((unsigned int)(0xC000000DULL))) + 168, (unsigned int)(0x2CC0ULL), (unsigned int)((unsigned int)((unsigned int)(0xC000000DULL))), a4);
    goto loc_00861249;
loc_00861C0A:
    v_stack_m1E4 = 0xC0000034ULL;
    result = CmpRecordParseFailure(v_stack_m1E0, (unsigned int)(0x2F00ULL), (unsigned int)(0xC0000034ULL), a4);
    goto loc_00860168;
loc_00861C31:
    v_stack_m1E4 = 0xC0000034ULL;
    result = CmpRecordParseFailure(v_stack_m1E0, (unsigned int)(0x3100ULL), (unsigned int)(0xC0000034ULL), a4);
    goto loc_00860168;
loc_00861C58:
    v_stack_m1E4 = (unsigned int)((unsigned int)(0xC000022DULL));
    result = CmpRecordParseFailure(v_stack_m1E0, (unsigned int)(0x3180ULL), (unsigned int)(0xC000022DULL), a4);
    goto loc_00860168;
loc_00861C82:
    result = CmpRecordParseFailure(v_stack_m1E0, (unsigned int)(0x31C0ULL), (unsigned int)((unsigned int)(result)), a4);
    goto loc_00860168;
loc_00861C9E:
    result = CmpRecordParseFailure(v_stack_m1E0, (unsigned int)(0x3280ULL), (unsigned int)((unsigned int)(result)), a4);
    goto loc_00860168;
loc_00861CBA:
    result = CmpRecordParseFailure(v_stack_m1E0, (unsigned int)(0x32C0ULL), (unsigned int)((unsigned int)(result)), a4);
    goto loc_00860168;
loc_00861CD6:
    v_stack_m1E4 = 0xC0000034ULL;
    result = CmpRecordParseFailure(v_stack_m1E0, (unsigned int)(0x3000ULL), (unsigned int)(0xC0000034ULL), a4);
    goto loc_00860168;
loc_00861CFD:
    result = CmpIsKeyStackSymlink((unsigned int)(0xC0190002ULL), (unsigned int)(0x3000ULL), (unsigned int)(0xC0000034ULL), a4);
    v_stack_m1E4 = 0xC0000035ULL;
    result = CmpRecordParseFailure(v_stack_m1E0, (unsigned int)(0x3300ULL), (unsigned int)(0xC0000035ULL), a4);
    goto loc_00860168;
loc_00861D49:
    v_stack_m1E4 = 0xC0000035ULL;
    goto loc_00860FF3;
loc_00861D61:
    result = CmpUnlockHashEntryByKcb(v_stack_m1B8, (unsigned int)(0x3700ULL), (unsigned int)(0xC0000035ULL), a4);
    v_stack_m1D8 = (unsigned __int8)(v_rsi);
    goto loc_00860ECF;
loc_00861D73:
    result = CmpRecordParseFailure(v_stack_m1E0, (unsigned int)(0x3800ULL), (unsigned int)((unsigned int)(result)), a4);
    goto loc_00860171;
loc_00861D8D:
    *(unsigned __int64 *)(v_stack_m1E0 + 64) = v_stack_m1E0;
    goto loc_00860F42;
loc_00861D96:
    v_stack_m1E4 = (unsigned int)((unsigned int)(0xC000000DULL));
    goto loc_00860FF3;
loc_00861DAC:
    v_stack_m1E4 = 0xC0000034ULL;
    goto loc_00860FF3;
loc_00861DC4:
    v_stack_m1E4 = 0xC0000035ULL;
    goto loc_00860FF3;
loc_00861DDC:
    goto loc_00860FF3;
loc_00861DE9:
    v_stack_m1E4 = (unsigned int)((unsigned int)(0xC0000034ULL));
loc_00861E07:
    goto loc_00861425;
loc_00861E11:
    result = CmpAttachToRegistryProcess(v_stack_m1E0 + 168, (unsigned int)(0x3C80ULL), (unsigned int)(0xC0000034ULL), a4);
loc_00861E37:
    v_stack_m1E4 = 0x40000016ULL;
    goto loc_00860158;
loc_00861E47:
loc_00861E51:
    result = CmpUnlockKcb(v_stack_m1E0 + 168, (unsigned int)(0x980ULL), (unsigned int)(0xC0000034ULL), a4);
    *(unsigned __int64 *)(result) = v_stack_m1B8;
    goto loc_00860541;
loc_00861E5E:
    result = CmpUnlockKcb(v_stack_m1E0 + 168, (unsigned int)(0x980ULL), (unsigned int)(0xC0000034ULL), a4);
    result = CmpUnlockHashEntryByIndex(v_rsi, (unsigned int)((unsigned int)(v_rsi)), (unsigned int)(0xC0000034ULL), a4);
    goto loc_00860B12;
loc_00861E72:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, (unsigned int)((unsigned int)(v_rsi)), (unsigned int)(0xC0000034ULL), a4);
    v_rsp = (v_rsp) + (528);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CmpDoParseKey(int64_t Arg1, int64_t Arg2, uint8_t Arg3, int32_t Arg4, int64_t Arg5, void *Arg6, void *Arg7, uint64_t Arg8, int64_t Arg9)
{
    uint8_t *arg6 = (uint8_t *)Arg6;
    uint8_t *arg7 = (uint8_t *)Arg7;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint16_t v_stack_m106;
    uint64_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint64_t v_stack_m130;
    uint64_t v_stack_m138;
    uint64_t v_stack_m140;
    uint64_t v_stack_m148;
    uint16_t v_stack_m14E;
    uint64_t v_stack_m150;
    uint64_t v_stack_m158;
    uint64_t v_stack_m160;
    uint64_t v_stack_m168;
    uint16_t v_stack_m170;
    uint64_t v_stack_m178;
    uint64_t v_stack_m180;
    uint64_t v_stack_m188;
    uint64_t v_stack_m190;
    uint64_t v_stack_m198;
    uint64_t v_stack_m1A0;
    uint64_t v_stack_m1A8;
    uint8_t v_stack_m1AF;
    uint8_t v_stack_m1B0;
    uint64_t v_stack_m1B8;
    uint16_t v_stack_m1C0;
    uint64_t v_stack_m1C8;
    uint8_t v_stack_m1CC;
    uint16_t v_stack_m1D0;
    uint8_t v_stack_m1D1;
    uint8_t v_stack_m1D2;
    uint8_t v_stack_m1D3;
    uint8_t v_stack_m1D4;
    uint8_t v_stack_m1D5;
    uint8_t v_stack_m1D6;
    uint8_t v_stack_m1D7;
    uint8_t v_stack_m1D8;
    uint64_t v_stack_m1E0;
    uint32_t v_stack_m1E4;
    uint8_t v_stack_m1E7;
    uint8_t v_stack_m1E8;
    uint64_t v_stack_m1F8;
    uint8_t v_stack_m200;
    uint64_t v_stack_m208;
    uint64_t v_stack_m210;
    uint64_t v_stack_m218;
    uint64_t v_stack_m220;
    uint64_t v_stack_m228;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m78;
    uint64_t v_stack_m90;
    uint16_t v_stack_m96;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint16_t v_stack_mC6;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint16_t v_stack_mE6;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p20;

    v_stack_p20 = local_rbx;
    local_rsp = (local_rsp) - (528);
    result = (*(uint64_t *)(v_rip + 0x5AAFCA)) ^ (local_rsp);
    v_stack_m48 = result;
    local_rsi = 0;
    v_stack_m160 = Arg5;
    local_r14 = 0;
    v_stack_m110 = Arg9;
    v_stack_m198 = Arg1;
    v_stack_m1C8 = 0;
    v_stack_m190 = 0;
    v_stack_m1D4 = 0;
    v_stack_m1E7 = 0;
    v_stack_m1B0 = 0;
    v_stack_m1E8 = 0;
    v_stack_m1CC = 0;
    v_stack_m1D2 = 0;
    v_stack_m1AF = 0;
    v_stack_m1D5 = 0;
    v_stack_m1D6 = Arg3;
    v_stack_m168 = Arg2;
    v_stack_m1E0 = Arg7;
    v_stack_m170 = 0;
    v_stack_m98 = v_xmm0;
    v_stack_m138 = 0;
    v_stack_m120 = v_xmm1;
    v_stack_m140 = 0;
    v_stack_m178 = 0;
    v_stack_m1A8 = 0;
    v_stack_m130 = 0;
    v_stack_m1A0 = 0;
    v_stack_m1D7 = 0;
    v_stack_m1D0 = 0;
    v_stack_m1C0 = 0;
    v_stack_m128 = 0;
    result = HvpGetCellContextInitialize(v_stack_m138, Arg2, Arg3, Arg4);
    v_stack_m1D8 = 0;
    v_stack_m150 = v_xmm0;
    result = CmpInitializeDelayDerefContext(v_stack_m120, Arg2, Arg3, Arg4);
    v_stack_m1D1 = 0;
    v_stack_m180 = 0;
    *(uint64_t *)(arg7 + 0xA0) = v_xmm0;
    Arg2 = 0;
    *(uint64_t *)(arg7 + 0xB0) = v_xmm0;
    v_stack_m108 = v_xmm0;
    v_stack_m106 = (uint16_t)((uint32_t)(0xFFFFFFFFULL));
    v_stack_mE8 = v_xmm0;
    v_stack_mE6 = (uint16_t)((uint32_t)(0xFFFFFFFFULL));
    v_stack_mC8 = v_xmm0;
    v_stack_mC6 = (uint16_t)((uint32_t)(0xFFFFFFFFULL));
    result = 0;
    *(uint64_t *)(arg7 + 0xC0) = v_xmm0;
    *(uint64_t *)(arg7 + 0xD0) = 0;
    v_stack_m188 = Arg7 + 216;
    v_stack_mF8 = v_xmm0;
    v_stack_mD8 = v_xmm0;
    v_stack_mB8 = v_xmm0;
    result = memset(Arg7 + 216, Arg2, 168, Arg4);
    Arg2 = 0;
    result = memset(Arg7 + 384, Arg2, local_rsi + 80, Arg4);
    if (Arg7 != NULL) {
        result = *(uint64_t *)(arg7 + 0x58);
        *(uint64_t *)(arg7 + 0x180) = result;
    }
    if (condition_is_below) goto loc_00860670;
loc_0085F8F6:
    *(uint64_t *)(arg7 + 0x58) = 0;
    if (*(uint64_t *)(v_stack_m1E0 + 0x48) != 0) goto loc_00860BBC;
loc_0085F912:
    v_stack_m158 = *(uint64_t *)(v_stack_m198 + 0x40);
loc_0085F91E:
    *(uint32_t *)(v_stack_m1E0 + 0x14) = (uint32_t)(*(uint16_t *)(v_stack_m198 + 0x32));
    if ((*(uint64_t *)(v_stack_m198 + 0x8)) != (*(uint64_t *)(*(uint64_t *)(v_rip + 0x77A23B) + 0x8))) goto loc_0085FC0F;
    if (*(uint64_t *)(arg7 + 0x58) != 0) goto loc_0085FC44;
loc_0085F944:
    v_stack_m1D7 = 0;
loc_0085F94D:
    v_stack_m1D3 = 0;
    v_stack_m1E7 = 0;
loc_0085F957:
    result = CmpComputeComponentHashes(v_stack_m150, v_stack_m1C0, v_stack_m188, Arg4);
    v_stack_m1E4 = (uint32_t)(result);
    if (sign_flag) goto loc_0086189D;
loc_0085F988:
    if (0 >= ((uint32_t)((int16_t)(v_stack_m1C0)))) goto loc_0085F9B0;
    if (0 >= 8) goto loc_0085FBAE;
    result = (0) + (2);
    result = (result) << (4);
    result = (result) + (v_stack_m188);
loc_0085F9A2:
    if ((*(uint16_t *)(result)) > 512) goto loc_008618B7;
    Arg1 = (uint32_t)((0) + 1);
    goto loc_0085F988;
loc_0085F9B0:
    v_stack_m1D0 = 0;
loc_0085F9B5:
    v_stack_m1D7 = 0;
    *(uint64_t *)(v_stack_m1E0 + 0x188) = *(uint64_t *)(v_stack_m198 + 0x8);
    *(uint64_t *)(v_stack_m1E0 + 0x1A0) = *(uint64_t *)(v_stack_m198 + 0x8);
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m198 + 0x8) + 0x8))) >> (21));
    Arg1 = (uint32_t)((Arg1) & (0x3FFULL));
    v_stack_m1E7 = (uint8_t)(v_stack_m1E7);
    Arg1 = (uint32_t)((Arg1) - (0));
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)((int16_t)(v_stack_m1C0))));
    if (((uint32_t)(Arg1)) > 512) goto loc_008618EA;
    if ((uint8_t)(v_stack_m1E7) != 0) goto loc_0085FA1D;
    if (((*(uint32_t *)(v_stack_m1E0)) & (0x400ULL)) != 0) goto loc_00860BB2;
    result = CmpLockRegistry(Arg1, v_stack_m1E7, v_stack_m188, v_stack_m1E0);
loc_0085FA13:
    v_stack_m1E7 = 1;
loc_0085FA1D:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m198 + 0x30)))) & (9)) != 0) goto loc_0086190B;
    if (0 == ((uint16_t)((int16_t)(v_stack_m1C0)))) goto loc_0086097D;
    v_stack_m210 = v_stack_m170;
    v_stack_m218 = v_stack_m1D8;
    v_stack_m220 = v_stack_m1A8;
    v_stack_m228 = v_stack_m1E0;
    Arg4 = (v_stack_m1E0) + (216);
    result = CmpPerformCompleteKcbCacheLookup(*(uint64_t *)(v_stack_m198 + 0x8), 0, (uint32_t)((uint32_t)((int16_t)(v_stack_m1C0))), Arg4);
    v_stack_m1E4 = (uint32_t)(result);
    if (sign_flag) goto loc_00861E47;
    if (((uint32_t)(result)) == 259) goto loc_00861E47;
    local_r12 = (uint16_t)((0) + ((uint16_t)(v_stack_m170)));
    v_stack_m1B8 = v_stack_m1A8;
    *(uint64_t *)(v_stack_m1E0 + 0x190) = v_stack_m1A8;
    *(uint8_t *)(v_stack_m1E0 + 0x1A8) = (uint8_t)(v_stack_m170);
    *(uint64_t *)(v_stack_m1E0 + 0x1A0) = v_stack_m1A8;
    v_stack_m1D0 = (uint32_t)(local_r12);
loc_0085FAB2:
    if (((uint16_t)(local_r12)) != ((uint16_t)((int16_t)(v_stack_m1C0)))) goto loc_0085FACB;
    result = (uint32_t)(*(uint32_t *)(v_stack_m1E0));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m1E0)))) & (1)) == 0) {
        Arg1 = v_stack_m1A8;
        result = CmpUnlockHashEntryByKcb(Arg1, 0, (uint32_t)((uint32_t)((int16_t)(v_stack_m1C0))), Arg4);
        v_stack_m1D8 = 0;
    }
    result = CmpLockKcbShared(v_stack_m1A8, 0, (uint32_t)((uint32_t)((int16_t)(v_stack_m1C0))), Arg4);
    if (((uint16_t)(local_r12)) < ((uint16_t)((int16_t)(v_stack_m1C0)))) goto loc_0085FBC5;
    Arg2 = 0;
    result = RtlInitUnicodeString(v_stack_m98, Arg2, (uint32_t)((uint32_t)((int16_t)(v_stack_m1C0))), Arg4);
loc_0085FAEB:
    local_rdi = (v_stack_m168) + (32);
    if ((*(uint8_t *)(v_rip + 0x5AF1A6)) == 0) goto loc_00860621;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m1E0 + 0x18)))) & (16)) != 0) goto loc_00860F67;
    if ((*(uint16_t *)(v_stack_m1A8 + 0x42)) != 0) goto loc_0085FC37;
    result = CmpIsKcbInvolvedInVirtualization(v_stack_m1A8, Arg2, (uint32_t)((uint32_t)((int16_t)(v_stack_m1C0))), Arg4);
    if ((uint8_t)(result) != 0) goto loc_0085FD79;
loc_0085FB34:
    v_stack_m1E4 = (uint32_t)((uint32_t)(0xC0000271ULL));
    result = CmpUnlockKcb(v_stack_m1A8, Arg2, (uint32_t)((uint32_t)((int16_t)(v_stack_m1C0))), Arg4);
    if (((uint32_t)((uint32_t)(v_stack_m1E4))) != 0xC0000271ULL) goto loc_00861938;
    if (*(uint64_t *)(v_stack_m1E0 + 0x40) == 0) goto loc_0085FE0C;
    if ((*(uint64_t *)(v_stack_m1E0 + 0x40)) == (*(uint64_t *)(v_stack_m1A8 + 0x20))) goto loc_0085FE0C;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m1A8 + 0x20) + 0x1010)))) & (1)) == 0) goto loc_008603AF;
    result = CmpLockHiveListShared(v_stack_m1A8, Arg2, (uint32_t)(v_stack_m1E4), Arg4);
    local_r14 = (*(uint64_t *)(v_stack_m1A8 + 0x20)) + (0x1018ULL);
loc_0085FB90:
    if ((*(uint64_t *)(local_r14)) == local_r14) goto loc_008603AA;
    if ((*(uint64_t *)(local_r14) - 4120) == (*(uint64_t *)(v_stack_m1E0 + 0x40))) goto loc_0085FE07;
    goto loc_0085FB90;
loc_0085FBAE:
    result = (*(uint64_t *)(*(uint64_t *)(local_r14)) - 8) + (6);
    result = (result) << (4);
    result = (result) + (*(uint64_t *)((uint32_t)(v_stack_m1E4) + 0xA0));
    goto loc_0085F9A2;
loc_0085FBC5:
    if (((uint32_t)((int16_t)((uint16_t)(local_r12)))) >= 8) goto loc_00860678;
    result = ((int16_t)((uint16_t)(local_r12))) << (4);
    Arg1 = (v_stack_m188) + (40);
loc_0085FBDE:
    Arg1 = (Arg1) + (result);
    v_stack_m90 = *(uint64_t *)(Arg1);
    Arg1 = (*(uint64_t *)(Arg1)) - (v_stack_m148);
    Arg1 = (Arg1) >> (1);
    Arg1 = (uint16_t)((Arg1) + ((uint16_t)(Arg1)));
    result = (uint16_t)((v_stack_m150) - ((uint16_t)(Arg1)));
    v_stack_m98 = (uint16_t)(result);
    v_stack_m96 = (uint16_t)(result);
    goto loc_0085FAEB;
loc_0085FC0F:
    if (*(uint64_t *)(arg7 + 0x58) == 0) goto loc_0085F944;
    result = CmpLockRegistry(Arg1, Arg2, (uint32_t)(v_stack_m1E4), Arg4);
    result = CmpDereferenceKeyControlBlock(*(uint64_t *)(arg7 + 0x58), Arg2, (uint32_t)(v_stack_m1E4), Arg4);
    result = CmpUnlockRegistry(*(uint64_t *)(arg7 + 0x58), Arg2, (uint32_t)(v_stack_m1E4), Arg4);
    goto loc_0085F94D;
loc_0085FC37:
    goto loc_0085FB34;
loc_0085FC44:
    if (((*(uint32_t *)((uint32_t)(v_stack_m1E4))) & (0x400ULL)) != 0) goto loc_00860DD3;
    result = CmpLockRegistry(*(uint64_t *)(arg7 + 0x58), Arg2, (uint32_t)(v_stack_m1E4), Arg4);
loc_0085FC56:
    v_stack_m1E7 = 1;
    result = (uint32_t)((*(uint64_t *)(0 + 0x128)) & (1));
    local_r14 = *(uint64_t *)(0 + 0x128);
    if (!(condition_is_equal)) {
        local_r14 = (*(uint64_t *)(0 + 0x128)) & (-2);
    }
    if (local_r14 == 0) goto loc_00860638;
    if ((uint8_t)(result) != 0) goto loc_00860638;
    result = RtlPrefixUnicodeString(local_r14, v_stack_m160, 1, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00860638;
    Arg1 = ((uint32_t)((uint32_t)(*(uint16_t *)(local_r14)))) >> (1);
    Arg1 = (uint16_t)((*(uint16_t *)(v_stack_m160)) - ((uint16_t)(*(uint16_t *)(local_r14))));
    result = (uint16_t)((*(uint16_t *)(v_stack_m160 + 0x2)) - ((uint16_t)(*(uint16_t *)(local_r14))));
    v_stack_m148 = *(uint64_t *)(v_stack_m160 + 0x8) + Arg1 * 2;
    v_stack_m150 = (uint16_t)(Arg1);
    v_stack_m14E = (uint16_t)(result);
    if ((uint16_t)(Arg1) == 0) goto loc_0085FCF2;
loc_0085FCD0:
    if ((*(uint16_t *)(*(uint64_t *)(v_stack_m160 + 0x8) + Arg1 * 2)) != 92) goto loc_0085FCEE;
    Arg1 = (uint16_t)((Arg1) + ((uint16_t)((uint32_t)(0xFFFEULL))));
    result = (uint16_t)((result) + ((uint16_t)((uint32_t)(0xFFFEULL))));
    Arg3 = (*(uint64_t *)(v_stack_m160 + 0x8) + Arg1 * 2) + (2);
    v_stack_m150 = (uint16_t)(Arg1);
    v_stack_m14E = (uint16_t)(result);
    if ((uint16_t)(Arg1) != 0) goto loc_0085FCD0;
loc_0085FCEE:
    v_stack_m148 = Arg3;
loc_0085FCF2:
    local_rdi = (uint32_t)(((uint32_t)(*(uint32_t *)(0 + 0x8))) >> (21));
    local_rdi = (uint32_t)((local_rdi) & (0x3FFULL));
    local_rdi = (uint32_t)((local_rdi) - 1);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m1E0)))) & (1)) != 0) goto loc_00860D09;
loc_0085FD10:
loc_0085FD15:
    result = CmpComputeComponentHashes(v_stack_m150, v_stack_m1C0, v_stack_m188, Arg4);
    v_stack_m1E4 = (uint32_t)(result);
    if (sign_flag) goto loc_0086186D;
    if (((uint32_t)((int16_t)(v_stack_m1C0) + local_rdi * 1)) > 32) goto loc_00861877;
loc_0085FD50:
    if (0 >= ((uint32_t)((int16_t)(v_stack_m1C0)))) goto loc_0085FD9F;
    if (0 >= 8) goto loc_008602D4;
    result = (0) + (2);
    result = (result) << (4);
    result = (result) + (v_stack_m188);
loc_0085FD6B:
    if ((*(uint16_t *)(result)) > 512) goto loc_0086188A;
    Arg1 = (uint32_t)((0) + 1);
    goto loc_0085FD50;
loc_0085FD79:
    result = CmpIsSystemEntity(v_stack_m1D6, local_rdi, (uint32_t)(v_stack_m1D0) + 16, (int16_t)(v_stack_m1C0));
    if ((uint8_t)(result) == 0) goto loc_00860DF0;
    goto loc_0085FB34;
loc_0085FD9F:
    if (((uint16_t)((uint32_t)(v_stack_m1D0))) != ((uint16_t)((int16_t)(v_stack_m1C0)))) goto loc_00860630;
    result = CmpLockHashEntrySharedByKcb(0, local_rdi, (uint32_t)(v_stack_m1D0) + 16, (int16_t)(v_stack_m1C0));
    v_stack_m1D7 = 1;
loc_0085FDB9:
    v_stack_m1D3 = 1;
    result = CmpLockKcbShared(0, local_rdi, (uint32_t)(v_stack_m1D0) + 16, (int16_t)(v_stack_m1C0));
    Arg2 = 0;
    result = CmpIsKeyDeleted(0, Arg2, (uint32_t)(v_stack_m1D0) + 16, (int16_t)(v_stack_m1C0));
    if ((uint8_t)(result) != 0) goto loc_008606BF;
    if (condition_is_below) goto loc_008606BF;
    result = CmpUnlockKcb(0, Arg2, (uint32_t)(v_stack_m1D0) + 16, (int16_t)(v_stack_m1C0));
    v_stack_m1C8 = v_stack_m190;
    goto loc_0085F9B5;
loc_0085FE07:
    result = CmpUnlockHiveList(0, Arg2, (uint32_t)(v_stack_m1D0) + 16, (int16_t)(v_stack_m1C0));
loc_0085FE0C:
    if (*(uint64_t *)(v_stack_m198 + 0x38) != 0) goto loc_008609BE;
    if (v_stack_m158 != 0) goto loc_008609BE;
loc_0085FE22:
    result = CmpTransSilentIgnore(0, Arg2, (uint32_t)(v_stack_m1D0) + 16, (int16_t)(v_stack_m1C0));
    if ((uint8_t)(result) != 0) goto loc_008609AE;
    if (*(uint64_t *)(v_stack_m198 + 0x38) != 0) goto loc_0085FE3D;
    if (v_stack_m158 == 0) goto loc_008609AE;
loc_0085FE3D:
    if (*(uint64_t *)(v_stack_m1A8 + 0x20) == 0) goto loc_00860A54;
    if ((((uint8_t)(*(uint64_t *)(v_stack_m198 + 0x38))) & (1)) == 0) goto loc_00860AD8;
    local_rdi = (*(uint64_t *)(v_stack_m198 + 0x38)) & (-2);
    result = CmpTransReferenceTransaction(*(uint64_t *)(v_stack_m198 + 0x38), Arg2, (uint32_t)(v_stack_m1D0) + 16, (int16_t)(v_stack_m1C0));
    if (sign_flag) goto loc_0085FE96;
    v_stack_m1C8 = *(uint64_t *)(local_rdi + 0x10);
    if (*(uint64_t *)(local_rdi + 0x10) == 0) goto loc_00860DDD;
    v_stack_m190 = *(uint64_t *)(local_rdi + 0x10);
loc_0085FE81:
    result = *(uint64_t *)(local_rdi + 0x10);
    if (*(uint64_t *)(v_stack_m198 + 0x38) != 0) {
        Arg1 = local_rdi;
        result = ObfDereferenceObject(Arg1, Arg2, (uint32_t)(v_stack_m1D0) + 16, (int16_t)(v_stack_m1C0));
    }
    v_stack_m1B8 = v_stack_m1A8;
loc_0085FE96:
loc_0085FE9A:
    if (sign_flag) goto loc_00860A54;
loc_0085FEA3:
    if (((uint32_t)((int16_t)(*(uint16_t *)(v_stack_m1A8 + 0x42)))) < 2) goto loc_0085FEBB;
    result = (uint32_t)(((uint32_t)((uint32_t)((int16_t)(*(uint16_t *)(v_stack_m1A8 + 0x42))))) - (1));
    if (condition_is_not_equal) goto loc_0086103A;
loc_0085FEBB:
    v_stack_mF0 = 0;
    v_stack_m106 = (uint16_t)((uint32_t)(0xFFFFFFFFULL));
    v_stack_m108 = (uint16_t)((int16_t)(*(uint16_t *)(v_stack_m1A8 + 0x42)));
    if (((uint32_t)((int16_t)(*(uint16_t *)(v_stack_m1A8 + 0x42)))) < 2) goto loc_0085FEE4;
    result = (uint32_t)(((uint32_t)((uint32_t)((int16_t)(*(uint16_t *)(v_stack_m1A8 + 0x42))))) - (1));
    if (condition_is_not_equal) goto loc_00861063;
loc_0085FEE4:
    v_stack_mE6 = (uint16_t)((uint32_t)(0xFFFFFFFFULL));
    v_stack_mE8 = (uint16_t)((int16_t)(*(uint16_t *)(v_stack_m1A8 + 0x42)));
    v_stack_mD0 = 0;
    v_stack_m1E4 = 0;
    v_stack_m106 = (uint16_t)(*(uint16_t *)(v_stack_m1A8 + 0x42));
    if ((uint16_t)((int16_t)(*(uint16_t *)(v_stack_m1A8 + 0x42))) != 0) goto loc_00860E4E;
    *(uint64_t *)(v_stack_m148 + (int16_t)(*(uint16_t *)(v_stack_m1A8 + 0x42)) * 8 + 0x48) = v_stack_m1A8;
loc_0085FF18:
loc_0085FF27:
    if (((uint16_t)((uint32_t)(v_stack_m1D0))) >= ((uint16_t)((int16_t)(v_stack_m1C0)))) goto loc_00860722;
    result = CmpLockKcbStackShared(v_stack_m108, (int16_t)(*(uint16_t *)(v_stack_m1A8 + 0x42)), (uint32_t)(v_stack_m1D0) + 16, (int16_t)(v_stack_m1C0));
    if (((*(uint32_t *)(v_stack_m1B8 + 0x8)) & (0x20000ULL)) != 0) goto loc_008610BD;
    v_stack_m158 = 0;
loc_0085FF50:
    if (sign_flag) goto loc_008600AB;
    if (((uint16_t)(*(uint16_t *)(v_stack_m108 + 0x2))) >= 2) goto loc_00860A46;
loc_0085FF6C:
    if ((*(uint16_t *)(*(uint64_t *)(v_stack_m108 + (int16_t)((uint16_t)(*(uint16_t *)(v_stack_m108 + 0x2))) * 8 + 0x8) + 0x42)) == 0) goto loc_0085FF7C;
    if ((*(uint8_t *)(*(uint64_t *)(v_stack_m108 + (int16_t)((uint16_t)(*(uint16_t *)(v_stack_m108 + 0x2))) * 8 + 0x8) + 0x41)) == 1) goto loc_008600AB;
loc_0085FF7C:
    if ((*(uint32_t *)(*(uint64_t *)(v_stack_m108 + (int16_t)((uint16_t)(*(uint16_t *)(v_stack_m108 + 0x2))) * 8 + 0x8) + 0x28)) == -1) goto loc_008600A3;
    if (v_stack_m1C8 != 0) goto loc_008605DB;
loc_0085FF93:
    result = CmpIsKeyStackSymlink(v_stack_m108, *(uint16_t *)(v_stack_m108 + 0x2), (uint32_t)(v_stack_m1D0) + 16, (int16_t)(v_stack_m1C0));
    if ((uint8_t)(result) != 0) goto loc_008602EB;
    result = CmpUnlockKcbStack(v_stack_m108, *(uint16_t *)(v_stack_m108 + 0x2), (uint32_t)(v_stack_m1D0) + 16, (int16_t)(v_stack_m1C0));
    if (((uint32_t)((int16_t)((uint16_t)((uint32_t)(v_stack_m1D0))))) >= 8) goto loc_00860695;
    Arg3 = ((uint32_t)((uint32_t)((int16_t)((uint16_t)((uint32_t)(v_stack_m1D0)))))) + (2);
    Arg3 = (Arg3) << (4);
    Arg3 = (Arg3) + (v_stack_m188);
loc_0085FFCF:
    result = (uint32_t)((result) * (*(uint32_t *)(v_stack_m1B8 + 0x10)));
    result = (uint32_t)((result) + ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m188 + (int16_t)((uint16_t)((uint32_t)(v_stack_m1D0))) * 4)))));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m1E0)))) & (1)) == 0) goto loc_0085FFF1;
    if (((uint32_t)((int16_t)((uint16_t)((uint32_t)(v_stack_m1D0))))) == ((uint32_t)((uint32_t)((uint32_t)((int16_t)(v_stack_m1C0))) - 1))) goto loc_00860A3F;
loc_0085FFF1:
    Arg2 = 0;
loc_0085FFF3:
    v_stack_m1F8 = v_stack_m1E0;
    v_stack_m200 = 0;
    v_stack_m208 = v_stack_m1C8;
    v_stack_m210 = (uint32_t)(result);
    v_stack_m218 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m188 + (int16_t)((uint16_t)((uint32_t)(v_stack_m1D0))) * 4)));
    v_stack_m220 = Arg3;
    v_stack_m228 = v_stack_m1B0;
    result = CmpWalkOneLevel(v_stack_m1B8, v_stack_m108, v_stack_m130, v_stack_mE8);
    v_stack_m1E4 = (uint32_t)(result);
    if (((uint32_t)(result)) == 0xC0000034ULL) goto loc_00860215;
loc_0086003C:
    if (v_stack_m1E4 < 0) goto loc_00860D7A;
    *(uint64_t *)(v_stack_m1E0 + 0x198) = v_stack_m130;
    *(uint64_t *)(v_stack_m1E0 + 0x1A0) = v_stack_m130;
    result = CmpDereferenceKeyControlBlockUnsafe(v_stack_m1B8, v_stack_m108, v_stack_m130, v_stack_mE8);
    v_stack_m1B8 = v_stack_m130;
    v_stack_m1A8 = v_stack_m130;
    v_stack_m1D8 = (uint8_t)(v_stack_m1B0);
    local_rbx = (uint16_t)(((uint32_t)(v_stack_m1D0)) + 1);
    v_stack_m130 = 0;
    v_stack_m1B0 = 0;
    v_stack_m1D0 = (uint32_t)(local_rbx);
    goto loc_0085FF27;
loc_008600A3:
    Arg2 = (uint16_t)((v_stack_m108) - 1);
    goto loc_0085FF50;
loc_008600AB:
    if ((*(uint8_t *)(v_rip + 0x68FA92)) != 0) goto loc_00861101;
loc_008600B8:
loc_008600BD:
    v_stack_m1E4 = 0xC0000034ULL;
    result = CmpRecordParseFailure(v_stack_m1E0, (uint32_t)(0x1000ULL), (uint32_t)(0xC0000034ULL), v_stack_mE8);
    local_rbx = 0;
loc_008600DA:
    result = CmpUnlockKcbStack(v_stack_mE8, (uint32_t)(0x1000ULL), (uint32_t)(0xC0000034ULL), v_stack_mE8);
    goto loc_00860171;
loc_008600E7:
    v_stack_m208 = v_stack_m1E4;
    v_stack_m210 = v_stack_m1D1;
    v_stack_m218 = v_stack_m1C8;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_mE8 + 0x18))) >> (2));
    result = (uint8_t)((result) & (1));
    v_stack_m220 = (uint8_t)(result);
    v_stack_m228 = (uint8_t)(v_stack_m1D6);
    result = CmpCheckOpenAccessOnKeyBody(v_stack_m178, v_stack_mE8, v_stack_m1E0, v_stack_m168);
    if ((uint8_t)(result) != 0) goto loc_00860917;
    if (v_stack_m1D1 != 0) goto loc_00861E11;
    result = CmpRecordParseFailure(v_stack_m1E0, (uint32_t)(0x3CE0ULL), (uint32_t)(v_stack_m1E4), v_stack_m168);
loc_00860158:
    if (v_stack_m1CC != 0) goto loc_00861B3B;
loc_00860163:
loc_00860168:
    if ((uint8_t)(v_stack_m130) != 0) goto loc_008600DA;
loc_00860171:
    if ((uint8_t)(v_stack_m1E8) == 0) goto loc_008601E9;
    if (0 > (*(uint16_t *)(v_stack_m1A0 + 0x2))) goto loc_008601E9;
loc_008601A0:
    v_stack_m180 = v_stack_m180;
    if (0 >= 2) goto loc_00860661;
loc_008601BB:
    result = CmpUnlockKcb(*(uint64_t *)(v_stack_m1A0 + (int16_t)(0) * 8 + 0x8), (uint32_t)(0x3CE0ULL), (uint32_t)(v_stack_m1E4), v_stack_m168);
    local_rbx = (uint16_t)((0) + 1);
    if (((uint16_t)(local_rbx)) <= (*(uint16_t *)(v_stack_m1A0 + 0x2))) goto loc_008601A0;
    v_stack_m1E7 = (uint8_t)(v_stack_m1E7);
    local_rsi = 0;
    v_stack_m1D7 = (uint8_t)(v_stack_m1D7);
    v_stack_m180 = v_stack_m180;
    v_stack_m1D5 = (uint8_t)(v_stack_m1D5);
loc_008601E9:
    result = v_stack_m180;
    if (v_stack_m1D5 != 0) {
        Arg1 = *(uint64_t *)(v_stack_m198 + 0x8);
        result = CmpUnlockKcb(Arg1, (uint32_t)(0x3CE0ULL), (uint32_t)(v_stack_m1E4), v_stack_m168);
    }
    if ((uint8_t)(v_stack_m1D4) != 0) goto loc_00860DBD;
loc_0086020A:
    goto loc_00860454;
loc_00860215:
    if ((*(uint8_t *)(v_rip + 0x68F928)) == 0) goto loc_0086003C;
    v_stack_m1B8 = v_stack_m1A8;
    if ((*(uint64_t *)(v_rip + 0x68F916)) == (*(uint64_t *)(gs_base + (0 + 0x188)))) goto loc_008602C7;
    if ((*(uint64_t *)(v_stack_m1A8 + 0x20)) != (*(uint64_t *)(v_rip + 0x779849))) goto loc_008602C7;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m1A8 + 0x8))) & (0x7FE00000ULL));
    if (((uint32_t)(result)) != 0x600000ULL) goto loc_0086028E;
    if (condition_is_less_or_equal) goto loc_0086028E;
    Arg2 = (uint32_t)(((int16_t)((uint16_t)(v_stack_m198))) - 1);
    result = CmpGetComponentNameAtIndex(v_stack_m188, Arg2, (uint32_t)(v_stack_m1E4), v_stack_m168);
    Arg4 = (v_stack_m1E0) + (136);
    result = CmpWaitForHiveMount(result, Arg2, (uint32_t)(v_stack_m1E4), Arg4);
    if ((uint8_t)(result) != 0) goto loc_00861995;
loc_0086028E:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m1A8 + 0x8))) & (0x7FE00000ULL));
    if (((uint32_t)(result)) != 0x400000ULL) goto loc_008602C7;
    result = CmpGetComponentNameAtIndex(v_stack_m188, (int16_t)((uint16_t)(v_stack_m198)), (uint32_t)(v_stack_m1E4), Arg4);
    Arg4 = (v_stack_m1E0) + (136);
    result = CmpWaitForHiveMount(result, (int16_t)((uint16_t)(v_stack_m198)), (uint32_t)(v_stack_m1E4), Arg4);
    if ((uint8_t)(result) != 0) goto loc_0086199C;
loc_008602C7:
    v_stack_m1C8 = v_stack_m190;
    goto loc_0086003C;
loc_008602D4:
    result = (result - 8) + (6);
    result = (result) << (4);
    result = (result) + (*(uint64_t *)(v_stack_m1B8 + 0xA0));
    goto loc_0085FD6B;
loc_008602EB:
    v_stack_m200 = v_stack_m140;
    v_stack_m208 = v_stack_m1E0 + 88;
    v_stack_m210 = v_stack_m160;
    v_stack_m218 = v_stack_m120;
    v_stack_m220 = v_stack_m1E0;
    v_stack_m228 = v_stack_m1E0;
    result = CmpGetSymbolicLinkTarget(v_stack_m1D4, v_stack_m1E0 + 216, (uint16_t)(v_stack_m198), v_stack_m1C0);
    v_stack_m1E4 = (uint32_t)(result);
    if (sign_flag) goto loc_008619BF;
    if ((*(uint64_t *)(v_stack_m1E0 + 0x40)) != 0) goto loc_00860361;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m140 + 0x20) + 0x1010)))) & (1)) != 0) {
        *(uint64_t *)(v_stack_m1E0 + 0x40) = *(uint64_t *)(v_stack_m140 + 0x20);
    }
    v_stack_m1E4 = 260;
    if (((uint8_t)(*(uint8_t *)(v_stack_m1E0 + 0x1AA))) >= 4) goto loc_00860454;
    *(uint32_t *)(v_stack_m1E0 + *(uint8_t *)(v_stack_m1E0 + 0x1AA) * 8 + 0x1AC) = 260;
    *(uint32_t *)(v_stack_m1E0 + *(uint8_t *)(v_stack_m1E0 + 0x1AA) * 8 + 0x1B0) = 0x1300ULL;
    goto loc_00860454;
loc_008603AA:
    result = CmpUnlockHiveList(*(uint64_t *)(v_stack_m140 + 0x20), v_stack_m1E0 + 216, (uint16_t)(v_stack_m198), v_stack_m1C0);
loc_008603AF:
    result = PsIsCurrentThreadInServerSilo(*(uint64_t *)(v_stack_m140 + 0x20), v_stack_m1E0 + 216, (uint16_t)(v_stack_m198), v_stack_m1C0);
    if ((uint8_t)(result) == 0) goto loc_00860432;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x5A9B9A)))) <= 5) goto loc_00860432;
    if (((*(uint64_t *)(v_rip + 0x5A9B94)) & ((uint16_t)(v_stack_m198))) != 0) goto loc_008617DE;
loc_008603DA:
    result = 0;
loc_008603DC:
    if (0 != 0) {
        result = v_stack_m128;
        v_stack_m128 = 0x1000000ULL;
        v_stack_m58 = result;
        Arg2 = v_rip - 8429778;
        result = v_stack_m78;
        v_stack_m50 = 8;
        Arg4 = 3;
        v_stack_m228 = result;
        Arg1 = v_rip + 5937978;
        result = tlgWriteAgg(Arg1, Arg2, (uint16_t)(v_stack_m198), Arg4);
        Arg2 = *(uint32_t *)(v_rip + 0x5A9B2F);
    }
    if (((uint32_t)(Arg2)) > 5) goto loc_008617FC;
loc_00860432:
    v_stack_m1E4 = 0xC0000022ULL;
    if (((uint8_t)(*(uint8_t *)(v_stack_m1E0 + 0x1AA))) < 4) goto loc_0086194A;
loc_00860454:
    if (v_stack_m1D8 != 0) goto loc_008605CE;
loc_00860463:
    if (v_stack_m1D7 != 0) goto loc_00860DB0;
loc_0086046E:
    result = *(uint8_t *)(v_stack_m1E0 + 0x1AA);
    if (v_stack_mF0 != 0) {
        result = CmSiFreeMemory(v_stack_mF0, Arg2, (uint16_t)(v_stack_m198), Arg4);
    }
    if (v_stack_mD0 != 0) {
        result = CmSiFreeMemory(v_stack_mD0, Arg2, (uint16_t)(v_stack_m198), Arg4);
    }
    if (v_stack_mB0 != 0) {
        result = CmSiFreeMemory(v_stack_mB0, Arg2, (uint16_t)(v_stack_m198), Arg4);
    }
    if (v_stack_m130 != 0) goto loc_00860DA0;
    if (v_stack_m1B8 == 0) goto loc_008604B5;
loc_008604B0:
    result = CmpDereferenceKeyControlBlock(v_stack_m1B8, Arg2, (uint16_t)(v_stack_m198), Arg4);
loc_008604B5:
    if (0 != 0) {
        Arg1 = 0;
        result = CmpDereferenceKeyControlBlock(Arg1, Arg2, (uint16_t)(v_stack_m198), Arg4);
    }
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m1E0 + 0x64))) == 0) goto loc_00860B1E;
    v_stack_m1E7 = (uint8_t)(v_stack_m1E7);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m1E0 + 0x64)))) & (2)) == 0) goto loc_00860B1E;
    v_stack_mC8 = v_xmm0;
    v_stack_m110 = *(uint64_t *)(*(uint64_t *)(v_stack_m1E0 + 0x70) + 0x670);
    v_stack_m1D0 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m1E0 + 0x70) + 0x678)));
    v_stack_mB8 = v_xmm0;
    v_stack_mA8 = v_xmm0;
    result = CmpAttachToRegistryProcess(v_stack_mC8, Arg2, (uint16_t)(v_stack_m198), Arg4);
    v_stack_m1E7 = (uint8_t)(v_stack_m1E7);
loc_00860520:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m1E0 + 0x70) + 0x678))))) goto loc_00860B06;
    result = CmpLockHashEntryByIndexExclusive(*(uint64_t *)(v_stack_m1E0 + 0x70), 0, (uint16_t)(v_stack_m198), Arg4);
loc_0086053C:
loc_00860541:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m1E0 + 0x70) + 0x670) + 0x0 + 0x0 * 2 * 8 + 0x10) == 0) goto loc_00860579;
    result = CmpLockKcbExclusive(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m1E0 + 0x70) + 0x670) + 0x0 + 0x0 * 2 * 8 + 0x10) - 16, 0, (uint16_t)(v_stack_m198), Arg4);
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m1E0 + 0x70) + 0x670) + 0x0 + 0x0 * 2 * 8 + 0x10) - 0x10)) != 0) goto loc_0086058F;
    result = CmpRemoveFromDelayedClose(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m1E0 + 0x70) + 0x670) + 0x0 + 0x0 * 2 * 8 + 0x10) - 16, 0, (uint16_t)(v_stack_m198), Arg4);
    result = CmpCleanUpKcbCacheWithLock(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m1E0 + 0x70) + 0x670) + 0x0 + 0x0 * 2 * 8 + 0x10) - 16, v_stack_m120, (uint16_t)(v_stack_m198), Arg4);
    result = CmpUnlockKcb(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m1E0 + 0x70) + 0x670) + 0x0 + 0x0 * 2 * 8 + 0x10) - 16, v_stack_m120, (uint16_t)(v_stack_m198), Arg4);
    goto loc_0086053C;
loc_00860579:
    result = CmpUnlockHashEntryByIndex(*(uint64_t *)(v_stack_m1E0 + 0x70), 0, (uint16_t)(v_stack_m198), Arg4);
    local_rsi = (uint32_t)((local_rsi) + 1);
    goto loc_00860520;
loc_0086058F:
    Arg4 = 0;
    result = CmpSyncKcbCacheForHive(*(uint64_t *)(v_stack_m1E0 + 0x70), *(uint64_t *)(v_stack_m1E0 + 0x70), v_stack_m120, Arg4);
    if (((uint32_t)(result)) == 1) goto loc_00861E5E;
    if (((uint32_t)(result)) == 3) goto loc_00861E5E;
    if (((uint32_t)(result)) == 2) goto loc_00861E51;
    result = CmpUnlockKcb((uint32_t)(v_stack_m1D0), *(uint64_t *)(v_stack_m1E0 + 0x70), v_stack_m120, Arg4);
    goto loc_00860541;
loc_008605CE:
    result = CmpUnlockHashEntryByKcb(*(uint64_t *)((uint32_t)(v_stack_m1D0) + 0x18), *(uint64_t *)(v_stack_m1E0 + 0x70), v_stack_m120, Arg4);
    goto loc_00860463;
loc_008605DB:
loc_008605DF:
    result = CmListGetNextElement(*(uint64_t *)(v_stack_m180 + 0x8) + 208, v_stack_m158, 32, *(uint64_t *)(v_stack_m180 + 0x8));
    if (result == 0) goto loc_0085FF93;
    if ((*(uint32_t *)(result + 0x44)) != 2) goto loc_008605DF;
    result = CmEqualTrans(*(uint64_t *)(result + 0x38), v_stack_m1E0, 32, *(uint64_t *)(v_stack_m180 + 0x8));
    if ((uint8_t)(result) != 0) goto loc_008600AB;
    goto loc_0085FF93;
loc_00860621:
    goto loc_0085FB34;
loc_00860630:
    local_r14 = 0;
    goto loc_0085FDB9;
loc_00860638:
    result = CmpDereferenceKeyControlBlock(*(uint64_t *)(v_stack_m1E0 + 0x70), v_stack_m1E0, 32, *(uint64_t *)(v_stack_m180 + 0x8));
    result = CmpUnlockRegistry(*(uint64_t *)(v_stack_m1E0 + 0x70), v_stack_m1E0, 32, *(uint64_t *)(v_stack_m180 + 0x8));
    local_r14 = 0;
    v_stack_m1C8 = v_stack_m190;
    goto loc_0085F94D;
loc_00860661:
    goto loc_008601BB;
loc_00860670:
    goto loc_0085F8F6;
loc_00860678:
    result = (uint32_t)((*(uint64_t *)((uint32_t)(v_stack_m1D0) + 0x18)) + (-8));
    Arg1 = ((uint32_t)((uint32_t)(result))) << (4);
    result = (*(uint64_t *)(v_stack_m188 + 0xA0)) + (104);
    goto loc_0085FBDE;
loc_00860695:
    Arg3 = (*(uint64_t *)(v_stack_m180 + 0x8) - 8) + (6);
    Arg3 = (Arg3) << (4);
    Arg3 = (Arg3) + (*(uint64_t *)(v_stack_m188 + 0xA0));
    goto loc_0085FFCF;
loc_008606BF:
    result = CmpUnlockKcb(local_rsi, v_stack_m1E0, Arg3, *(uint64_t *)(v_stack_m180 + 0x8));
    if (0 != 0) goto loc_00860A2A;
loc_008606D0:
    result = CmpDereferenceKeyControlBlock(local_rsi, v_stack_m1E0, Arg3, *(uint64_t *)(v_stack_m180 + 0x8));
    v_stack_m1D0 = (uint32_t)((uint16_t)(local_rsi));
    v_stack_m150 = v_xmm0;
    result = CmpCleanupPathInfo(v_stack_m1A8, v_stack_m1E0, Arg3, *(uint64_t *)(v_stack_m180 + 0x8));
    Arg2 = 0;
    result = memset(v_stack_m1A8, Arg2, 168, *(uint64_t *)(v_stack_m180 + 0x8));
    v_stack_m1C8 = v_stack_m190;
    v_stack_m1D3 = 0;
    goto loc_0085F957;
loc_00860722:
    v_stack_m1A0 = v_stack_m198;
    if (*(uint64_t *)(v_stack_m1B8 + 0x48) == 0) goto loc_008617D2;
    result = CmpPopulateKcbStack(v_stack_m198, *(uint64_t *)(v_stack_m1B8 + 0x48), 168, *(uint64_t *)(v_stack_m180 + 0x8));
loc_00860742:
    if ((*(uint64_t *)(v_stack_m1B8 + 0x48)) == (*(uint64_t *)(v_stack_m198 + 0x8))) goto loc_00860AD1;
    if (v_stack_m1B8 == (*(uint64_t *)(v_stack_m198 + 0x8))) goto loc_00860AD1;
    result = CmpLockKcbShared(*(uint64_t *)(v_stack_m198 + 0x8), *(uint64_t *)(v_stack_m1B8 + 0x48), 168, *(uint64_t *)(v_stack_m180 + 0x8));
    v_stack_m1D5 = 1;
loc_00860768:
    if (v_stack_m198 != 0) {
        Arg1 = v_stack_m198;
        result = CmpLockKcbStackShared(Arg1, *(uint64_t *)(v_stack_m1B8 + 0x48), 168, *(uint64_t *)(v_stack_m180 + 0x8));
        v_stack_m1E8 = 1;
    }
    result = CmpLockKcbStackShared(0, *(uint64_t *)(v_stack_m1B8 + 0x48), 168, *(uint64_t *)(v_stack_m180 + 0x8));
    Arg2 = 0;
    result = CmpIsKeyDeletedForKeyBody(v_stack_m198, Arg2, 168, *(uint64_t *)(v_stack_m180 + 0x8));
    if ((uint8_t)(result) != 0) goto loc_008619D9;
    if (((*(uint32_t *)(v_stack_m1B8 + 0x8)) & (0x20000ULL)) != 0) goto loc_00861A0D;
    local_rdi = (uint16_t)(((uint32_t)(v_stack_m1D0)) - 1);
    v_stack_m1D0 = (uint32_t)(local_rdi);
    if (((*(uint32_t *)(v_stack_m1B8 + 0xB8)) & (0x20000ULL)) != 0) goto loc_00861A3B;
    result = CmRmIsKcbStackVisible(0, v_stack_m1C8, 168, *(uint64_t *)(v_stack_m180 + 0x8));
    if ((uint8_t)(result) == 0) goto loc_00861A42;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m1E0)))) & (2)) != 0) goto loc_0086145D;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m1E0)))) & (32)) != 0) goto loc_00860BE0;
    result = CmpIsKeyStackDeleted(0, v_stack_m1C8, 168, *(uint64_t *)(v_stack_m180 + 0x8));
    if ((uint8_t)(result) != 0) goto loc_00860F74;
    result = CmpIsKeyStackSymlink(0, v_stack_m1C8, 168, *(uint64_t *)(v_stack_m180 + 0x8));
    if ((uint8_t)(result) != 0) goto loc_00860E8E;
loc_00860815:
    if (v_stack_m1AF != ((uint8_t)(local_rsi))) goto loc_00861D96;
    if (((*(uint32_t *)(v_stack_m1B8 + 0xB8)) & (0x20000ULL)) != 0) goto loc_00861DAC;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m1E0 + 0x18)))) & (2)) != 0) goto loc_00861DC4;
    Arg4 = 0;
    v_stack_m218 = v_stack_m160;
    v_stack_m220 = v_stack_m1E0;
    v_stack_m228 = local_rsi;
    result = CmpDoWritethroughReparse(v_stack_m1B8, 0, v_stack_m1A0, Arg4);
    v_stack_m1E4 = (uint32_t)(result);
    if (((uint32_t)(result)) != 0xC0000271ULL) goto loc_00861A29;
    result = (v_stack_m168) + (32);
    v_stack_m220 = result;
    Arg3 = 0;
    v_stack_m228 = (uint8_t)(v_stack_m1D6);
    result = CmpVEExecuteOpenLogic(v_stack_m1B8, v_stack_m1E0, Arg3, v_stack_m160);
    v_stack_m1E4 = (uint32_t)(result);
    if (((uint32_t)(result)) != 0xC0000271ULL) goto loc_00861DDC;
    v_stack_m210 = v_stack_m1D2;
    v_stack_m218 = v_stack_m178;
    v_stack_m220 = 0;
    v_stack_m228 = 2;
    result = CmpCreateKeyBody(v_stack_m1B8, v_stack_m1D6, v_stack_m1E0, v_stack_m1C8);
    v_stack_m1E4 = (uint32_t)(result);
    if (sign_flag) goto loc_00861DE9;
loc_008608F5:
    local_rdi = 0;
loc_008608FD:
    if ((*(uint32_t *)(v_stack_m1E0 + 0x20)) != 1) goto loc_008600E7;
    *(uint16_t *)(v_stack_m178 + 0x4) = (uint16_t)(*(uint16_t *)(*(uint64_t *)(v_stack_m178 + 0x8) + 0x42));
loc_00860917:
    v_stack_m178 = local_rsi;
    *(uint64_t *)(v_stack_m110) = v_stack_m178;
    if ((*(uint32_t *)(v_stack_m1E0 + 0x20)) == ((uint32_t)(local_rsi))) {
        *(uint32_t *)(v_stack_m1E0 + 0x20) = 2;
    }
    if (v_stack_m1D2 != ((uint8_t)(local_rsi))) goto loc_00861E37;
    v_stack_m1E4 = (uint32_t)(local_rsi);
    v_stack_m1E8 = (uint8_t)(v_stack_m1E8);
    v_stack_m1CC = (uint8_t)(v_stack_m1CC);
    v_stack_m1D5 = (uint8_t)(v_stack_m1D5);
    v_stack_m1D7 = (uint8_t)(v_stack_m1D7);
    v_stack_m1A0 = v_stack_m1A0;
    v_stack_m1D4 = 0;
loc_00860973:
    goto loc_00860158;
loc_0086097D:
    result = CmpReferenceKeyControlBlockUnsafe(v_stack_m110, v_stack_m178, (uint32_t)((uint32_t)(result)), v_stack_m1C8);
    v_stack_m1B8 = v_stack_m1E0;
    v_stack_m1A8 = v_stack_m1E0;
    if (v_stack_m1E0 != local_rsi) goto loc_00860B79;
    v_stack_m1D7 = (uint8_t)(local_rsi);
loc_008609A0:
    v_stack_m1D8 = (uint8_t)(v_stack_m1D3);
    goto loc_0085FAB2;
loc_008609AE:
    v_stack_m1C8 = local_rsi;
    v_stack_m190 = local_rsi;
    goto loc_0085FEA3;
loc_008609BE:
    if ((*(uint64_t *)(v_stack_m1E0 + 0x20)) == (*(uint64_t *)(v_rip + 0x7790CB))) goto loc_00861972;
    if (v_stack_m1A0 != 0) goto loc_008609DD;
    if (v_stack_m1E0 == 0) goto loc_0085FE22;
loc_008609DD:
    if ((*(uint16_t *)(v_stack_m1E0 + 0x42)) == ((uint16_t)(local_rsi))) goto loc_0085FE22;
    result = CmpLogUnsupportedOperation(8, v_stack_m178, (uint32_t)((uint32_t)(result)), v_stack_m1C8);
    result = PsIsCurrentThreadInServerSilo(8, v_stack_m178, (uint32_t)((uint32_t)(result)), v_stack_m1C8);
    if ((uint8_t)(result) != 0) goto loc_00861976;
    v_stack_m1E4 = 0xC0190005ULL;
    result = CmpRecordParseFailure(v_stack_m1E0, (uint32_t)(0xB00ULL), (uint32_t)(0xC0190005ULL), v_stack_m1C8);
    goto loc_00860454;
loc_00860A2A:
    result = CmpUnlockHashEntryByKcb(local_rsi, (uint32_t)(0xB00ULL), (uint32_t)(0xC0190005ULL), v_stack_m1C8);
    local_r14 = 0;
    v_stack_m1D7 = 0;
    goto loc_008606D0;
loc_00860A3F:
    goto loc_0085FFF3;
loc_00860A46:
    goto loc_0085FF6C;
loc_00860A54:
    result = *(uint64_t *)(local_r14 + 0x18);
    if (v_stack_m1D8 != ((uint8_t)(local_rsi))) {
        Arg1 = v_stack_m1E0;
        result = CmpUnlockHashEntryByKcb(Arg1, 1, (uint32_t)(0xC0190005ULL), v_stack_m1C8);
        v_stack_m1D8 = (uint8_t)(local_rsi);
    }
    result = CmpUnlockRegistry(Arg1, 1, (uint32_t)(0xC0190005ULL), v_stack_m1C8);
    if (*(uint64_t *)(v_stack_m1E0 + 0x20) == 0) goto loc_0086142D;
    if ((((uint8_t)(v_stack_m1A0)) & (1)) == 0) goto loc_00861437;
    result = CmpTransSearchAddLightWeightTrans(v_stack_m1A0, *(uint64_t *)(v_stack_m1E0 + 0x20), 1, v_stack_m190);
loc_00860A98:
    v_stack_m1E4 = (uint32_t)(result);
    result = CmpLockRegistry(v_stack_m1A0, *(uint64_t *)(v_stack_m1E0 + 0x20), 1, v_stack_m190);
    v_stack_m1E7 = 1;
    if (!sign_flag) goto loc_00861985;
loc_00860AB4:
    result = CmpRecordParseFailure(v_stack_m1E0, (uint32_t)(0xC00ULL), (uint32_t)(v_stack_m1E4), v_stack_m190);
    goto loc_00860454;
loc_00860AD1:
    local_rbx = 0;
    goto loc_00860768;
loc_00860AD8:
    Arg4 = 0;
    v_stack_m228 = v_stack_m190;
    result = CmpTransSearchAddTransFromRm(*(uint64_t *)(v_stack_m1E0 + 0x1038), 0, v_stack_m1E0, Arg4);
    v_stack_m1C8 = v_stack_m190;
    goto loc_0085FE9A;
loc_00860B06:
    result = CmpDetachFromRegistryProcess(v_stack_mC8, 0, v_stack_m1E0, Arg4);
loc_00860B12:
loc_00860B1E:
    Arg2 = 0;
    result = CmpDrainDelayDerefContext(v_stack_m120, Arg2, v_stack_m1E0, Arg4);
    if (v_stack_m1E7 != 0) {
        result = CmpUnlockRegistry(v_stack_m120, Arg2, v_stack_m1E0, Arg4);
    }
    if ((uint32_t)((uint32_t)(result)) != 0) goto loc_00860B88;
loc_00860B3A:
    result = (uint32_t)(*(uint32_t *)(v_stack_m1E0 + 0xA0));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m1E0 + 0xA0)))) & (1)) != 0) {
        Arg1 = v_stack_m1E0 + 168;
        result = CmpDetachFromRegistryProcess(Arg1, Arg2, v_stack_m1E0, Arg4);
    }
    if (v_stack_m178 != 0) goto loc_00860B6F;
loc_00860B59:
    result = CmpCleanupPathInfo(v_stack_m1E0 + 216, v_stack_m178, v_stack_m1E0, Arg4);
    goto loc_00861E72;
loc_00860B6F:
    result = ObfDereferenceObject(v_stack_m178, v_stack_m178, v_stack_m1E0, Arg4);
    goto loc_00860B59;
loc_00860B79:
    result = CmpLockHashEntrySharedByKcb(v_stack_m1E0, v_stack_m178, v_stack_m1E0, Arg4);
    goto loc_008609A0;
loc_00860B88:
    if (v_stack_m1D1 == 0) goto loc_00860BA3;
    result = CmpCheckExeOwnerForPca(v_stack_m1E0, v_stack_m178, v_stack_m1E0, Arg4);
    if ((uint8_t)(result) != 0) {
        Arg2 = (uint32_t)((uint32_t)(result));
        Arg1 = v_stack_m1E0;
        result = CmpPublishEventForPcaResolver(Arg1, Arg2, v_stack_m1E0, Arg4);
    }
    result = CmpFreePoolWithTag((uint32_t)((uint32_t)(result)), (uint32_t)(0x624E4D43ULL), v_stack_m1E0, Arg4);
    goto loc_00860B3A;
loc_00860BB2:
    result = CmpLockRegistryExclusive((uint32_t)((uint32_t)(result)), (uint32_t)(0x624E4D43ULL), v_stack_m1E0, Arg4);
    goto loc_0085FA13;
loc_00860BBC:
    if (*(uint64_t *)(v_stack_m1E0 + 0x38) == 0) goto loc_00860BCE;
    if (0 != (*(uint64_t *)(v_stack_m1E0 + 0x38))) goto loc_00861845;
loc_00860BCE:
    if (0 == 0) goto loc_0085F912;
    v_stack_m158 = local_rsi;
    goto loc_0085F91E;
loc_00860BE0:
    result = CmpUnlockKcbStack((uint32_t)((uint32_t)(result)), (uint32_t)(0x624E4D43ULL), v_stack_m1E0, Arg4);
    result = CmpUnlockKcbStack(v_stack_m1A0, (uint32_t)(0x624E4D43ULL), v_stack_m1E0, Arg4);
    result = CmpLockKcbStackTopExclusiveRestShared(v_stack_m1A0, (uint32_t)(0x624E4D43ULL), v_stack_m1E0, Arg4);
    result = CmpLockKcbStackTopExclusiveRestShared((uint32_t)((uint32_t)(result)), (uint32_t)(0x624E4D43ULL), v_stack_m1E0, Arg4);
    result = CmpIsKeyStackDeleted(v_stack_m1A0, v_stack_m1C8, v_stack_m1E0, Arg4);
    if ((uint8_t)(result) != 0) goto loc_00861B94;
    if (((*(uint32_t *)(*(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x48) + 0xB8)) & (0x20000ULL)) != 0) goto loc_00861B9E;
    result = CmpGetComponentNameAtIndex(v_stack_m188, (int16_t)((uint16_t)(v_stack_m1E0)), v_stack_m1E0, Arg4);
    if (((*(uint32_t *)((uint32_t)((uint32_t)(result)) + 0xB8)) & (0x400000ULL)) == 0) goto loc_0086100D;
loc_00860C49:
    *(uint32_t *)((uint32_t)((uint32_t)(result)) + 0x64) = 0xFFFFFFFFULL;
    *(uint32_t *)((uint32_t)((uint32_t)(result)) + 0x60) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m1E0 + 0x38)));
    v_stack_m210 = v_stack_m1D2;
    v_stack_m218 = v_stack_m178;
    v_stack_m220 = (uint32_t)((uint32_t)(result));
    v_stack_m228 = 3;
    result = CmpCreateKeyBody((uint32_t)((uint32_t)(result)), v_stack_m1D6, v_stack_m1E0, v_stack_m1C8);
    v_stack_m1E4 = (uint32_t)(result);
    if (sign_flag) goto loc_00861BA8;
    result = CmpIsKeyStackDeleted((uint32_t)((uint32_t)(result)), v_stack_m1C8, v_stack_m1E0, v_stack_m1C8);
    if ((uint8_t)(result) == 0) goto loc_00861E07;
    v_stack_m208 = v_stack_m1C8;
    v_stack_m210 = (uint8_t)(local_rsi);
    v_stack_m218 = (uint32_t)(local_rsi);
    v_stack_m220 = 64;
    v_stack_m228 = v_stack_m1E0;
    result = CmpCreateChild(v_stack_m1A0, (uint32_t)((uint32_t)(result)), v_stack_m168, result);
    v_stack_m1E4 = (uint32_t)(result);
    if (sign_flag) goto loc_00860FFB;
    *(uint32_t *)(v_stack_m1E0 + 0x20) = 1;
    goto loc_008608F5;
loc_00860D09:
    if ((uint16_t)(v_stack_m1A0) != 0) goto loc_0085FD10;
    Arg3 = (uint16_t)((*(uint16_t *)((uint32_t)((uint32_t)(result)))) - ((uint16_t)(*(uint16_t *)((uint32_t)((uint32_t)(result))))));
    Arg1 = ((uint32_t)((uint32_t)(*(uint16_t *)((uint32_t)((uint32_t)(result)))))) >> (1);
    Arg4 = (uint16_t)((*(uint16_t *)((uint32_t)((uint32_t)(result)) + 0x2)) - ((uint16_t)(*(uint16_t *)((uint32_t)((uint32_t)(result))))));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsi + 0x50))))) & (1)) == 0) goto loc_008610F9;
    Arg1 = (uint16_t)((*(uint16_t *)(*(uint64_t *)(local_rsi + 0x50) + 0x18)) + ((uint16_t)(*(uint16_t *)(*(uint64_t *)(local_rsi + 0x50) + 0x18))));
loc_00860D4C:
    result = ((uint32_t)((uint32_t)(*(uint16_t *)(*(uint64_t *)(local_rsi + 0x50) + 0x18)))) + ((uint32_t)((uint32_t)(*(uint16_t *)(*(uint64_t *)(local_rsi + 0x50) + 0x18))));
    Arg3 = (uint16_t)((Arg3) + ((uint16_t)(Arg1)));
    local_r10 = (*(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x8) + Arg1 * 2) - (result);
    v_stack_m150 = Arg3;
    Arg4 = (uint16_t)((Arg4) + ((uint16_t)(Arg1)));
    v_stack_m148 = local_r10;
    v_stack_m14E = (uint16_t)(Arg4);
    local_rdi = (uint32_t)((v_stack_m1E0) - 1);
    v_stack_m1D0 = 1;
    goto loc_0085FD15;
loc_00860D7A:
loc_00860D89:
    result = CmpRecordParseFailure(v_stack_m1E0, (uint32_t)(0x1580ULL), (uint32_t)(v_stack_m1E4), Arg4);
    goto loc_00860454;
loc_00860DA0:
    result = CmpDereferenceKeyControlBlockUnsafe(v_stack_m1B8, (uint32_t)(0x1580ULL), (uint32_t)(v_stack_m1E4), Arg4);
    goto loc_008604B0;
loc_00860DB0:
    result = CmpUnlockHashEntryByKcb(local_rsi, (uint32_t)(0x1580ULL), (uint32_t)(v_stack_m1E4), Arg4);
    goto loc_0086046E;
loc_00860DBD:
    result = CmpUnlockHashEntry(*(uint64_t *)(v_stack_m1E0 + 0x30), (uint32_t)((uint32_t)(local_rsi)), (uint32_t)(v_stack_m1E4), Arg4);
    goto loc_00860454;
loc_00860DD3:
    result = CmpLockRegistryExclusive(*(uint64_t *)(v_stack_m1E0 + 0x30), (uint32_t)((uint32_t)(local_rsi)), (uint32_t)(v_stack_m1E4), Arg4);
    goto loc_0085FC56;
loc_00860DDD:
    v_stack_m1C8 = v_stack_m190;
    goto loc_0085FE81;
loc_00860DF0:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)((uint32_t)(0xC0190002ULL))))) & (8)) != 0) goto loc_0086182E;
    result = (uint32_t)(*(uint32_t *)((uint32_t)(0xC0190002ULL) + 0xA0));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)((uint32_t)(0xC0190002ULL) + 0xA0)))) & (1)) == 0) {
        Arg1 = (uint32_t)(0xC0190002ULL) + 168;
        result = CmpAttachToRegistryProcess(Arg1, (uint32_t)((uint32_t)(local_rsi)), (uint32_t)(v_stack_m1E4), Arg4);
    }
    if (((*(uint32_t *)(v_stack_m1B8 + 0xB8)) & (0x2000000ULL)) != 0) goto loc_008610EC;
    v_stack_m228 = v_stack_m1E0;
    result = CmpVEExecuteRealStoreParseLogic(v_stack_m1B8, v_stack_m98, (uint32_t)(0xC0190002ULL), v_stack_m160);
    goto loc_0085FB34;
loc_00860E4E:
    if (*(uint64_t *)(v_stack_m1B8 + 0xC0) == 0) goto loc_0085FF18;
loc_00860E70:
    result = CmpSetKcbAtLayerHeight(v_stack_m108, v_stack_m98, *(uint64_t *)(*(uint64_t *)(v_stack_m1B8 + 0xC0) + 0x10), *(uint64_t *)(v_stack_m1B8 + 0xC0));
    Arg2 = (uint16_t)((v_stack_m98) - 1);
    if (*(uint64_t *)(*(uint64_t *)(v_stack_m1B8 + 0xC0) + 0x18) != 0) goto loc_00860E70;
    goto loc_0085FF18;
loc_00860E8E:
    if (condition_is_below) goto loc_00860815;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)((uint32_t)(0xC0190002ULL) + 0x18)))) & (2)) != 0) goto loc_00861D49;
    if (v_stack_m1E8 != ((uint8_t)(local_rsi))) goto loc_008610AA;
loc_00860EAE:
    result = (uint32_t)(*(uint32_t *)((uint32_t)(0xC0190002ULL) + 0x18));
    if ((uint8_t)(v_stack_m1A0) != 0) {
        result = v_stack_m198;
        Arg1 = *(uint64_t *)(result + 0x8);
        result = CmpUnlockKcb(Arg1, Arg2, *(uint64_t *)(*(uint64_t *)(v_stack_m1B8 + 0xC0) + 0x10), *(uint64_t *)(*(uint64_t *)(v_stack_m1B8 + 0xC0) + 0x18));
        v_stack_m1D5 = (uint8_t)(local_rsi);
    }
    if (v_stack_m1D8 != ((uint8_t)(local_rsi))) goto loc_00861D61;
loc_00860ECF:
    Arg4 = 0;
    v_stack_m200 = v_stack_m140;
    v_stack_m208 = (uint32_t)(0xC0190002ULL) + 88;
    Arg3 = 0;
    v_stack_m210 = v_stack_m160;
    v_stack_m218 = v_stack_m120;
    v_stack_m220 = (uint32_t)(0xC0190002ULL);
    v_stack_m228 = v_stack_m1C8;
    result = CmpGetSymbolicLinkTarget((uint32_t)(0xC0190002ULL), (uint32_t)(0xC0190002ULL) + 216, Arg3, Arg4);
    v_stack_m1E4 = (uint32_t)(result);
    if (sign_flag) goto loc_00861D73;
    if ((*(uint64_t *)((uint32_t)(0xC0190002ULL) + 0x40)) != local_rsi) goto loc_00860F42;
    if ((((uint8_t)(v_stack_m1E7)) & ((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m140 + 0x20) + 0x1010))))) != 0) goto loc_00861D8D;
loc_00860F42:
    v_stack_m1E4 = 260;
    result = CmpRecordParseFailure((uint32_t)(0xC0190002ULL), (uint32_t)(0x3900ULL), 260, Arg4);
    goto loc_00860171;
loc_00860F67:
    goto loc_0085FB34;
loc_00860F74:
    if (v_stack_m1AF != ((uint8_t)(local_rsi))) goto loc_00861BB2;
    result = CmpIsKeyStackDeleted(v_stack_m1A0, v_stack_m1C8, 260, Arg4);
    if ((uint8_t)(result) != 0) goto loc_00861A14;
    result = CmRmIsKcbStackVisible(v_stack_m1A0, v_stack_m1C8, 260, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00861A14;
    if (((*(uint32_t *)(*(uint64_t *)(v_stack_m1B8 + 0x48) + 0xB8)) & (0x20000ULL)) != 0) goto loc_00861BC8;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m1E0)))) & (1)) != 0) goto loc_0086119E;
    v_stack_m1E4 = 0xC0000034ULL;
loc_00860FF3:
    result = CmpRecordParseFailure(v_stack_m1E0, (uint32_t)(0x2A00ULL), (uint32_t)(0xC0000034ULL), Arg4);
loc_00860FFB:
    result = CmpUnlockKcbStack((uint32_t)(0xC0190002ULL), (uint32_t)(0x2A00ULL), (uint32_t)(0xC0000034ULL), Arg4);
    goto loc_00860171;
loc_0086100D:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m1B8 + 0x8)))) & (8)) == 0) goto loc_00860C49;
    result = CmpDelayDerefKeyControlBlock(*(uint64_t *)(v_stack_m1B8 + 0x68), v_stack_m120, (uint32_t)(0xC0000034ULL), Arg4);
    *(uint64_t *)(v_stack_m1B8 + 0x68) = local_rsi;
    goto loc_00860C49;
loc_0086103A:
    Arg2 = ((uint32_t)((uint32_t)((uint32_t)(0xFFF7ULL)))) << (3);
    result = CmpAllocatePool(256, Arg2, (uint32_t)(0x35364D43ULL), Arg4);
    if (result != 0) goto loc_0085FEBB;
    goto loc_0086108A;
loc_00861063:
    Arg2 = ((uint32_t)((uint32_t)(result))) << (3);
    result = CmpAllocatePool(256, Arg2, (uint32_t)(0x35364D43ULL), Arg4);
    if (result != 0) goto loc_0085FEE4;
loc_0086108A:
    v_stack_m1E4 = 0xC000009AULL;
    result = CmpRecordParseFailure(v_stack_m1E0, (uint32_t)(0xE00ULL), (uint32_t)(0xC000009AULL), Arg4);
    goto loc_0086020A;
loc_008610AA:
    result = CmpUnlockKcbStack(v_stack_m1A0, (uint32_t)(0xE00ULL), (uint32_t)(0xC000009AULL), Arg4);
    v_stack_m1E8 = (uint8_t)(local_rsi);
    goto loc_00860EAE;
loc_008610BD:
    v_stack_m1E4 = 0xC0000034ULL;
    result = CmpRecordParseFailure(v_stack_m1E0, (uint32_t)(0xF80ULL), (uint32_t)(0xC0000034ULL), Arg4);
    local_rbx = 0;
    result = CmpUnlockKcbStack((uint32_t)(0xC0190002ULL), (uint32_t)(0xF80ULL), (uint32_t)(0xC0000034ULL), Arg4);
    goto loc_00860171;
loc_008610EC:
    result = CmpVEExecuteVirtualStoreParseLogic((uint32_t)(0xC0190002ULL), (uint32_t)(0xF80ULL), (uint32_t)(0xC0000034ULL), Arg4);
    goto loc_0085FB34;
loc_008610F9:
    result = (result) >> (1);
    goto loc_00860D4C;
loc_00861101:
    if ((*(uint64_t *)(v_rip + 0x68EA37)) == (*(uint64_t *)(gs_base + (0 + 0x188)))) goto loc_008619CC;
    v_stack_m1B8 = v_stack_m1A8;
    if ((*(uint64_t *)(v_stack_m1A8 + 0x20)) != (*(uint64_t *)(v_rip + 0x77896E))) goto loc_008600B8;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m1A8 + 0x8))) & (0x7FE00000ULL));
    if (((uint32_t)(result)) != 0x600000ULL) goto loc_008600B8;
    if (condition_is_less_or_equal) goto loc_008600B8;
    Arg2 = (uint32_t)(((int16_t)(0)) - 1);
    result = CmpGetComponentNameAtIndex(v_stack_m188, Arg2, (uint32_t)(0xC0000034ULL), Arg4);
    result = CmpWaitForHiveMount(result, Arg2, (uint32_t)(0xC0000034ULL), v_stack_m1E0 + 136);
    if ((uint8_t)(result) == 0) goto loc_008600BD;
    v_stack_m1E4 = 259;
    result = CmpRecordParseFailure(v_stack_m1E0, (uint32_t)(0xF00ULL), 259, v_stack_m1E0 + 136);
    local_rbx = 0;
    goto loc_008600DA;
loc_0086119E:
    result = CmpGetComponentNameAtIndex(259 + 216, (int16_t)((uint16_t)(v_stack_m1E0)), 259, v_stack_m1E0 + 136);
    v_stack_m218 = v_stack_m160;
    v_stack_m220 = 259;
    v_stack_m228 = result;
    result = CmpDoWritethroughReparse(v_stack_m1B8, (uint32_t)(0xC0190002ULL), v_stack_m1A0, 1);
    v_stack_m1E4 = (uint32_t)(result);
    if (((uint32_t)(result)) != 0xC0000271ULL) goto loc_00861BD2;
    v_stack_m210 = v_stack_m1D2;
    v_stack_m218 = v_stack_m178;
    v_stack_m220 = (uint32_t)(0xC0190002ULL);
    v_stack_m228 = (uint32_t)(local_rsi);
    result = CmpCreateKeyBody(v_stack_m1B8, v_stack_m1D6, v_stack_m1E0, v_stack_m1C8);
    v_stack_m1E4 = (uint32_t)(result);
    if (sign_flag) goto loc_00861BDF;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m1E0 + 0xA0)))) & (1)) == 0) goto loc_00861BEC;
loc_00861249:
    result = CmpUnlockKcbStack((uint32_t)(0xC0190002ULL), v_stack_m1D6, v_stack_m1E0, v_stack_m1C8);
    result = CmpUnlockKcbStack(v_stack_m1A0, v_stack_m1D6, v_stack_m1E0, v_stack_m1C8);
    result = CmpLockKcbStackTopExclusiveRestShared(v_stack_m1A0, v_stack_m1D6, v_stack_m1E0, v_stack_m1C8);
    result = CmpLockKcbStackTopExclusiveRestShared((uint32_t)(0xC0190002ULL), v_stack_m1D6, v_stack_m1E0, v_stack_m1C8);
    result = CmRmIsKcbStackVisible((uint32_t)(0xC0190002ULL), v_stack_m1C8, v_stack_m1E0, v_stack_m1C8);
    if ((uint8_t)(result) == 0) goto loc_00861C0A;
    if (((*(uint32_t *)(v_stack_m1B8 + 0x8)) & (0x20000ULL)) != 0) goto loc_008617AB;
    result = CmpIsKeyStackDeleted((uint32_t)(0xC0190002ULL), v_stack_m1C8, v_stack_m1E0, v_stack_m1C8);
    if ((uint8_t)(result) == 0) goto loc_00861CFD;
    result = CmpIsKeyStackDeleted(v_stack_m1A0, v_stack_m1C8, v_stack_m1E0, v_stack_m1C8);
    if ((uint8_t)(result) != 0) goto loc_00861CD6;
    result = CmRmIsKcbStackVisible(v_stack_m1A0, v_stack_m1C8, v_stack_m1E0, v_stack_m1C8);
    if ((uint8_t)(result) == 0) goto loc_00861CD6;
    if (((*(uint32_t *)(*(uint64_t *)(v_stack_m1B8 + 0x48) + 0xB8)) & (0x20000ULL)) != 0) goto loc_00861C31;
    v_stack_m208 = v_stack_m160;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m1E0 + 0x18))) & (2));
    v_stack_m210 = v_stack_m1E0;
    v_stack_m218 = v_stack_m1C8;
    result = (uint32_t)((result) << (4));
    v_stack_m220 = (uint32_t)(result);
    v_stack_m228 = (uint8_t)(v_stack_m1D6);
    result = CmpVEExecuteCreateLogic(*(uint64_t *)(v_stack_m1B8 + 0x48), v_stack_m1B8, result, v_stack_m168);
    v_stack_m1E4 = (uint32_t)(result);
    if (((uint32_t)(result)) == 0xC0000055ULL) goto loc_00861C58;
    if (((uint32_t)(result)) != 0xC0000271ULL) goto loc_00861C82;
    v_stack_m1F8 = v_stack_m1E4;
    v_stack_m200 = (uint32_t)(local_rsi);
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m1E0 + 0x18))) & (2));
    v_stack_m208 = v_stack_m178;
    v_stack_m210 = v_stack_m1C8;
    Arg2 = (uint32_t)((Arg2) << (4));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m1E0 + 0x18))))) >> (2));
    Arg1 = (uint8_t)((Arg1) & (1));
    v_stack_m218 = (uint8_t)(Arg1);
    v_stack_m220 = (uint32_t)(Arg2);
    v_stack_m228 = (uint8_t)(v_stack_m1D6);
    result = CmpCheckCreateAccessOnKcbStack(Arg1, v_stack_m1A0, v_stack_m1E0, v_stack_m168);
    v_stack_m228 = (uint32_t)(0xC0190002ULL);
    result = CmpEnlistKeyBody(v_stack_m178, v_stack_m1B8, v_stack_m1C8, 1);
    v_stack_m1E4 = (uint32_t)(result);
    if (sign_flag) goto loc_00861C9E;
    v_stack_m208 = v_stack_m1C8;
    v_stack_m210 = (uint8_t)(local_rsi);
    result = (uint16_t)((*(uint16_t *)(v_stack_m1E0 + 0x18)) & (2));
    result = (uint16_t)((result) << (3));
    v_stack_m218 = (uint32_t)(local_rsi);
    v_stack_m220 = (uint16_t)(result);
    v_stack_m228 = v_stack_m1E0;
    result = CmpCreateChild(v_stack_m1A0, (uint32_t)(0xC0190002ULL), v_stack_m168, result);
    v_stack_m1E4 = (uint32_t)(result);
    if (sign_flag) goto loc_00861CBA;
    *(uint32_t *)(v_stack_m1E0 + 0x20) = 1;
    v_stack_m1E8 = 1;
loc_00861425:
    local_rdi = 0;
    goto loc_008617A2;
loc_0086142D:
    goto loc_00860A98;
loc_00861437:
    v_stack_m228 = v_stack_m190;
    result = CmpTransSearchAddTransFromRm(*(uint64_t *)(v_stack_m1E0 + 0x1038), result, 0, 1);
    goto loc_00860A98;
loc_0086145D:
    result = CmpUnlockKcbStack(*(uint64_t *)(v_stack_m1E0 + 0x1038), result, 0, 1);
    result = CmpUnlockKcbStack(v_stack_m1A0, result, 0, 1);
    if ((uint8_t)(result) != 0) goto loc_00861A49;
loc_00861477:
    result = CmpTryToLockHashEntryExclusive(*(uint64_t *)(v_stack_m1E0 + 0x30), (uint32_t)((uint32_t)(local_rsi)), 0, 1);
    v_stack_m1D4 = (uint8_t)(result);
    if ((uint8_t)(result) != 0) goto loc_00861A57;
loc_00861493:
    result = CmpLockKcbStackTopExclusiveRestShared(v_stack_m1A0, (uint32_t)((uint32_t)(local_rsi)), 0, 1);
    result = CmpLockKcbStackTopExclusiveRestShared((uint32_t)(0xC0190002ULL), (uint32_t)((uint32_t)(local_rsi)), 0, 1);
    result = CmpGetComponentNameAtIndex(v_stack_m188, (uint32_t)((uint32_t)((int16_t)((uint16_t)((uint32_t)(v_stack_m1D0))))), (int16_t)((uint16_t)((uint32_t)(v_stack_m1D0))), 1);
    result = CmpGetComponentHashAtIndex(v_stack_m188, (uint32_t)((uint32_t)((int16_t)((uint16_t)((uint32_t)(v_stack_m1D0))))), (int16_t)((uint16_t)((uint32_t)(v_stack_m1D0))), 1);
    Arg2 = 0;
    result = CmpIsKeyDeletedForKeyBody(v_stack_m198, Arg2, (int16_t)((uint16_t)((uint32_t)(v_stack_m1D0))), 1);
    if ((uint8_t)(result) != 0) goto loc_00861A65;
    result = CmpIsKeyStackDeleted(v_stack_m1A0, v_stack_m1C8, (int16_t)((uint16_t)((uint32_t)(v_stack_m1D0))), 1);
    if ((uint8_t)(result) != 0) goto loc_00861A88;
    result = CmpIsKeyStackDeleted((uint32_t)(0xC0190002ULL), v_stack_m1C8, (int16_t)((uint16_t)((uint32_t)(v_stack_m1D0))), 1);
    if ((uint8_t)(result) == 0) goto loc_00861A8F;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m1B8 + 0x48) + 0x20)) != (*(uint64_t *)(v_rip + 0x778582))) goto loc_00861AA4;
    if (((*(uint32_t *)(*(uint64_t *)(v_stack_m1B8 + 0x48) + 0xB8)) & (0x20000ULL)) != 0) goto loc_00861ABC;
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m1E0 + 0xA0))))) == 0) goto loc_00861AC6;
loc_00861541:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m1E0 + 0x28)))) != -1) goto loc_00861AF1;
    v_stack_m228 = v_stack_m1E0 + 40;
    result = CmpCreateHiveRootCell(*(uint64_t *)(v_stack_m1E0 + 0x30), v_stack_m168, result, v_stack_m1E0);
    v_stack_m1E4 = (uint32_t)(result);
    if (sign_flag) goto loc_00861AE4;
loc_00861576:
    v_stack_m208 = v_stack_m128;
    v_stack_m210 = (uint32_t)(local_rsi);
    v_stack_m218 = (uint32_t)((uint32_t)((uint32_t)(result)));
    v_stack_m220 = result;
    v_stack_m228 = 1;
    result = CmpCreateKeyControlBlock(*(uint64_t *)(v_stack_m1E0 + 0x30), (uint32_t)(0xFFFFFFFFULL), v_stack_m1B8, *(uint64_t *)(v_stack_m1E0 + 0x50));
    v_stack_m1E4 = (uint32_t)(result);
    if (sign_flag) goto loc_00861B0F;
    v_stack_m1B8 = v_stack_m128;
    result = CmpDereferenceKeyControlBlockUnsafe(v_stack_m1B8, (uint32_t)(0xFFFFFFFFULL), (uint32_t)(v_stack_m1E4), *(uint64_t *)(v_stack_m1E0 + 0x50));
    result = CmpUnlockHashEntryByKcb(v_stack_m1B8, (uint32_t)(0xFFFFFFFFULL), (uint32_t)(v_stack_m1E4), *(uint64_t *)(v_stack_m1E0 + 0x50));
    v_stack_m1D8 = (uint8_t)(local_rsi);
    result = CmpStartKcbStackForTopLayerKcb(v_stack_mC8, v_stack_m1B8, (uint32_t)(v_stack_m1E4), *(uint64_t *)(v_stack_m1E0 + 0x50));
    v_stack_m1E4 = (uint32_t)(result);
    if (sign_flag) goto loc_00861B19;
    result = CmpLockKcbStackTopExclusiveRestShared(v_stack_mC8, v_stack_m1B8, (uint32_t)(v_stack_m1E4), *(uint64_t *)(v_stack_m1E0 + 0x50));
    v_stack_m210 = v_stack_m1D2;
    v_stack_m218 = v_stack_m178;
    v_stack_m220 = v_stack_mC8;
    v_stack_m228 = 3;
    v_stack_m1CC = 1;
    result = CmpCreateKeyBody(v_stack_m1B8, v_stack_m1D6, v_stack_m1E0, v_stack_m1C8);
    v_stack_m1E4 = (uint32_t)(result);
    if (sign_flag) goto loc_00861B26;
    result = HvLockHiveFlusherShared(*(uint64_t *)(v_stack_m1B8 + 0x20), v_stack_m1D6, v_stack_m1E0, v_stack_m1C8);
    result = HvLockHiveFlusherExclusive(*(uint64_t *)(v_stack_m1B8 + 0x20), v_stack_m1D6, v_stack_m1E0, v_stack_m1C8);
    Arg4 = 0;
    Arg3 = 0;
    v_stack_m1D0 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m1B8 + 0x20) + 0x68)));
    result = HvpMarkCellDirty(*(uint64_t *)(v_stack_m1B8 + 0x20), (uint32_t)(*(uint32_t *)(v_stack_m1E0 + 0x28)), Arg3, Arg4);
    v_stack_m1E4 = (uint32_t)(result);
    if (sign_flag) goto loc_00861B4C;
    v_stack_m208 = v_stack_m1C8;
    v_stack_m210 = 1;
    v_stack_m218 = (uint32_t)(local_rsi);
    v_stack_m220 = 10;
    v_stack_m228 = v_stack_m1E0;
    result = CmpCreateChild(v_stack_m1A0, (uint32_t)(0xC0190002ULL), v_stack_m168, result);
    v_stack_m1E4 = (uint32_t)(result);
    if (sign_flag) goto loc_00861B5E;
    *(uint32_t *)(v_stack_m1B8 + 0x28) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m1E0 + 0x28)));
    result = CmpGetKeyNodeForKcb(v_stack_m1B8, v_stack_m138, 1, result);
    Arg4 = 0;
    Arg3 = 0;
    *(uint32_t *)(result + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m1B8 + 0x28)));
    result = CmpRebuildKcbCacheFromNode(v_stack_m1B8, result, Arg3, Arg4);
    if (((*(uint8_t *)(*(uint64_t *)(v_stack_m1B8 + 0x20) + 0x8C)) & (1)) != 0) goto loc_0086183B;
    result = HvpReleaseCellPaged(*(uint64_t *)(v_stack_m1B8 + 0x20), v_stack_m138, Arg3, Arg4);
loc_00861756:
    if (v_stack_m1D0 == ((uint32_t)(local_rsi))) goto loc_00861B86;
loc_00861760:
    result = HvUnlockHiveFlusherExclusive(*(uint64_t *)(v_stack_m1B8 + 0x20), v_stack_m138, Arg3, Arg4);
    result = HvUnlockHiveFlusherShared(*(uint64_t *)(v_stack_m1B8 + 0x20), v_stack_m138, Arg3, Arg4);
    result = CmpReferenceKeyControlBlockUnsafe(v_stack_m1B8, v_stack_m138, Arg3, Arg4);
    *(uint64_t *)(v_stack_m1B8 + 0x68) = v_stack_m1B8;
    result = CmpUnlockHashEntry(*(uint64_t *)(v_stack_m1E0 + 0x30), (uint32_t)((uint32_t)(local_rsi)), Arg3, Arg4);
    local_rdi = 0;
    v_stack_m1D4 = 0;
    *(uint32_t *)(v_stack_m1E0 + 0x20) = 1;
loc_008617A2:
    goto loc_008608FD;
loc_008617AB:
    v_stack_m1E4 = 0xC0000034ULL;
    result = CmpRecordParseFailure(v_stack_m1E0, (uint32_t)(0x2F80ULL), (uint32_t)(0xC0000034ULL), Arg4);
    goto loc_00860168;
loc_008617D2:
    v_stack_m1A0 = local_rsi;
    goto loc_00860742;
loc_008617DE:
    result = (*(uint64_t *)(v_rip + 0x5A878B)) & ((uint32_t)(0xC0000034ULL));
    if (result != (*(uint64_t *)(v_rip + 0x5A8781))) goto loc_008603DA;
    goto loc_008603DC;
loc_008617FC:
    Arg4 = 0;
    v_stack_m220 = v_stack_m98;
    Arg3 = 0;
    v_stack_m228 = 2;
    result = tlgWriteTransfer_EtwWriteTransfer(v_rip + 5932852, v_rip - 8434840, Arg3, Arg4);
    goto loc_00860432;
loc_0086182E:
    goto loc_0085FB34;
loc_0086183B:
    result = HvpReleaseCellFlat(v_rip + 5932852, v_rip - 8434840, Arg3, Arg4);
    goto loc_00861756;
loc_00861845:
    v_stack_m1E4 = (uint32_t)((uint32_t)(0xC0190002ULL));
    result = CmpRecordParseFailure(v_stack_m1E0, 256, (uint32_t)((uint32_t)((uint32_t)(0xC0190002ULL))), Arg4);
    local_r12 = 0;
    goto loc_00860454;
loc_0086186D:
loc_00861877:
    v_stack_m1E4 = (uint32_t)((uint32_t)(0xC000000DULL));
loc_0086188A:
    v_stack_m1E4 = (uint32_t)((uint32_t)(0xC000000DULL));
loc_0086189D:
    result = CmpRecordParseFailure(v_stack_m1E0, (uint32_t)(0x500ULL), (uint32_t)((uint32_t)((uint32_t)(0xC000000DULL))), Arg4);
    goto loc_0086020A;
loc_008618B7:
    v_stack_m1E4 = (uint32_t)((uint32_t)(0xC000000DULL));
    result = CmpRecordParseFailure(v_stack_m1E0, (uint32_t)(0x600ULL), (uint32_t)((uint32_t)((uint32_t)(0xC000000DULL))), Arg4);
    v_stack_m1E7 = (uint8_t)(v_stack_m1E7);
    v_stack_m1D7 = (uint8_t)((uint32_t)(0xC0190002ULL));
    goto loc_00860454;
loc_008618EA:
    v_stack_m1E4 = (uint32_t)((uint32_t)(0xC000000DULL));
    result = CmpRecordParseFailure(0, (uint32_t)(0x700ULL), (uint32_t)((uint32_t)((uint32_t)(0xC000000DULL))), Arg4);
    goto loc_0086020A;
loc_0086190B:
    Arg3 = (uint32_t)(0xC0000425ULL);
    if ((((uint8_t)(result)) & (1)) == 0) { Arg3 = (uint32_t)((uint32_t)(0xC000017CULL)); }
    v_stack_m1E4 = Arg3;
    result = CmpRecordParseFailure(v_stack_m1E0, (uint32_t)(0x800ULL), Arg3, Arg4);
    goto loc_0086020A;
loc_00861938:
    result = CmpRecordParseFailure(v_stack_m1E0, (uint32_t)(0x9C0ULL), Arg3, Arg4);
    goto loc_0086020A;
loc_0086194A:
    *(uint32_t *)(v_stack_m1E0 + result * 8 + 0x1AC) = 0xC0000022ULL;
    *(uint32_t *)(v_stack_m1E0 + *(uint8_t *)(v_stack_m1E0 + 0x1AA) * 8 + 0x1B0) = 0xA00ULL;
    goto loc_00860454;
loc_00861972:
    v_stack_m1AF = 1;
loc_00861976:
    v_stack_m158 = local_rsi;
    goto loc_0085FE22;
loc_00861985:
    v_stack_m1E4 = (uint32_t)((uint32_t)(0xC000022DULL));
    goto loc_00860AB4;
loc_00861995:
    goto loc_008619A1;
loc_0086199C:
loc_008619A1:
    v_stack_m1E4 = 259;
    goto loc_00860D89;
loc_008619BF:
    goto loc_00860D89;
loc_008619CC:
    v_stack_m1B8 = v_stack_m1A8;
    goto loc_008600B8;
loc_008619D9:
    Arg3 = (uint32_t)(0xC0000425ULL);
    if (((*(uint8_t *)(v_stack_m1E0 + 0x30)) & ((uint8_t)(v_stack_m1E7))) == 0) { Arg3 = (uint32_t)((uint32_t)(0xC000017CULL)); }
    v_stack_m1E4 = Arg3;
    result = CmpRecordParseFailure(v_stack_m1E0, (uint32_t)(0x1700ULL), Arg3, Arg4);
    goto loc_008600DA;
loc_00861A0D:
    goto loc_00861A19;
loc_00861A14:
loc_00861A19:
    v_stack_m1E4 = 0xC0000034ULL;
    goto loc_00861A31;
loc_00861A29:
loc_00861A31:
    goto loc_00860FF3;
loc_00861A3B:
    goto loc_00861A19;
loc_00861A42:
    goto loc_00861A19;
loc_00861A49:
    result = CmpUnlockKcb(*(uint64_t *)(v_stack_m1B8 + 0x8), (uint32_t)(0x1900ULL), (uint32_t)((uint32_t)(result)), Arg4);
    goto loc_00861477;
loc_00861A57:
    result = CmpLockKcbShared(*(uint64_t *)(v_stack_m1B8 + 0x8), (uint32_t)(0x1900ULL), (uint32_t)((uint32_t)(result)), Arg4);
    goto loc_00861493;
loc_00861A65:
    Arg3 = (uint32_t)(0xC0000425ULL);
    if (((*(uint8_t *)(v_stack_m198 + 0x30)) & ((uint8_t)(v_stack_m1E7))) == 0) { Arg3 = (uint32_t)((uint32_t)(0xC000017CULL)); }
    v_stack_m1E4 = Arg3;
    goto loc_00861A31;
loc_00861A88:
    goto loc_00861A19;
loc_00861A8F:
    v_stack_m1E4 = 0xC0000022ULL;
    goto loc_00861A31;
loc_00861AA4:
    v_stack_m1E4 = 0xC0000022ULL;
    goto loc_00861A31;
loc_00861ABC:
    goto loc_00861A19;
loc_00861AC6:
    result = CmpAttachToRegistryProcess((uint32_t)(0xC0000022ULL) + 168, (uint32_t)(0x1E00ULL), (uint32_t)(0xC0000022ULL), Arg4);
    goto loc_00861541;
loc_00861AE4:
    goto loc_00861A31;
loc_00861AF1:
    result = CmpUpdateHiveRootCellFlags((uint32_t)(0xC0000022ULL) + 168, (uint32_t)(0x1E80ULL), (uint32_t)((uint32_t)(result)), Arg4);
    v_stack_m1E4 = (uint32_t)(result);
    if (!sign_flag) goto loc_00861576;
    goto loc_00861A31;
loc_00861B0F:
    goto loc_00861A31;
loc_00861B19:
    goto loc_00861A31;
loc_00861B26:
    result = CmpRecordParseFailure(v_stack_m1E0, (uint32_t)(0x2180ULL), (uint32_t)((uint32_t)(result)), Arg4);
loc_00861B3B:
    result = CmpUnlockKcbStack(v_stack_mC8, (uint32_t)(0x2180ULL), (uint32_t)((uint32_t)(result)), Arg4);
    goto loc_00860163;
loc_00861B4C:
    result = CmpRecordParseFailure(v_stack_m1E0, (uint32_t)(0x2200ULL), (uint32_t)((uint32_t)(result)), Arg4);
loc_00861B5E:
    result = HvUnlockHiveFlusherExclusive(*(uint64_t *)(v_stack_m1B8 + 0x20), (uint32_t)(0x2200ULL), (uint32_t)((uint32_t)(result)), Arg4);
    result = HvUnlockHiveFlusherShared(*(uint64_t *)(v_stack_m1E8 + 0x20), (uint32_t)(0x2200ULL), (uint32_t)((uint32_t)(result)), Arg4);
    v_stack_m1E7 = (uint8_t)(v_stack_m1E7);
    v_stack_m180 = local_rsi;
    goto loc_00860973;
loc_00861B86:
    result = HvResetDirtyData(*(uint64_t *)(v_stack_m1B8 + 0x20), (uint32_t)(0x2200ULL), (uint32_t)((uint32_t)(result)), Arg4);
    goto loc_00861760;
loc_00861B94:
    goto loc_00861A19;
loc_00861B9E:
    goto loc_00861A19;
loc_00861BA8:
    goto loc_00860FFB;
loc_00861BB2:
    v_stack_m1E4 = (uint32_t)((uint32_t)(0xC000000DULL));
    goto loc_00861A31;
loc_00861BC8:
    goto loc_00861A19;
loc_00861BD2:
    goto loc_00861A31;
loc_00861BDF:
    goto loc_00861A31;
loc_00861BEC:
    result = CmpAttachToRegistryProcess((uint32_t)((uint32_t)((uint32_t)(0xC000000DULL))) + 168, (uint32_t)(0x2CC0ULL), (uint32_t)((uint32_t)((uint32_t)(0xC000000DULL))), Arg4);
    goto loc_00861249;
loc_00861C0A:
    v_stack_m1E4 = 0xC0000034ULL;
    result = CmpRecordParseFailure(v_stack_m1E0, (uint32_t)(0x2F00ULL), (uint32_t)(0xC0000034ULL), Arg4);
    goto loc_00860168;
loc_00861C31:
    v_stack_m1E4 = 0xC0000034ULL;
    result = CmpRecordParseFailure(v_stack_m1E0, (uint32_t)(0x3100ULL), (uint32_t)(0xC0000034ULL), Arg4);
    goto loc_00860168;
loc_00861C58:
    v_stack_m1E4 = (uint32_t)((uint32_t)(0xC000022DULL));
    result = CmpRecordParseFailure(v_stack_m1E0, (uint32_t)(0x3180ULL), (uint32_t)(0xC000022DULL), Arg4);
    goto loc_00860168;
loc_00861C82:
    result = CmpRecordParseFailure(v_stack_m1E0, (uint32_t)(0x31C0ULL), (uint32_t)((uint32_t)(result)), Arg4);
    goto loc_00860168;
loc_00861C9E:
    result = CmpRecordParseFailure(v_stack_m1E0, (uint32_t)(0x3280ULL), (uint32_t)((uint32_t)(result)), Arg4);
    goto loc_00860168;
loc_00861CBA:
    result = CmpRecordParseFailure(v_stack_m1E0, (uint32_t)(0x32C0ULL), (uint32_t)((uint32_t)(result)), Arg4);
    goto loc_00860168;
loc_00861CD6:
    v_stack_m1E4 = 0xC0000034ULL;
    result = CmpRecordParseFailure(v_stack_m1E0, (uint32_t)(0x3000ULL), (uint32_t)(0xC0000034ULL), Arg4);
    goto loc_00860168;
loc_00861CFD:
    result = CmpIsKeyStackSymlink((uint32_t)(0xC0190002ULL), (uint32_t)(0x3000ULL), (uint32_t)(0xC0000034ULL), Arg4);
    v_stack_m1E4 = 0xC0000035ULL;
    result = CmpRecordParseFailure(v_stack_m1E0, (uint32_t)(0x3300ULL), (uint32_t)(0xC0000035ULL), Arg4);
    goto loc_00860168;
loc_00861D49:
    v_stack_m1E4 = 0xC0000035ULL;
    goto loc_00860FF3;
loc_00861D61:
    result = CmpUnlockHashEntryByKcb(v_stack_m1B8, (uint32_t)(0x3700ULL), (uint32_t)(0xC0000035ULL), Arg4);
    v_stack_m1D8 = (uint8_t)(local_rsi);
    goto loc_00860ECF;
loc_00861D73:
    result = CmpRecordParseFailure(v_stack_m1E0, (uint32_t)(0x3800ULL), (uint32_t)((uint32_t)(result)), Arg4);
    goto loc_00860171;
loc_00861D8D:
    *(uint64_t *)(v_stack_m1E0 + 0x40) = v_stack_m1E0;
    goto loc_00860F42;
loc_00861D96:
    v_stack_m1E4 = (uint32_t)((uint32_t)(0xC000000DULL));
    goto loc_00860FF3;
loc_00861DAC:
    v_stack_m1E4 = 0xC0000034ULL;
    goto loc_00860FF3;
loc_00861DC4:
    v_stack_m1E4 = 0xC0000035ULL;
    goto loc_00860FF3;
loc_00861DDC:
    goto loc_00860FF3;
loc_00861DE9:
    v_stack_m1E4 = (uint32_t)((uint32_t)(0xC0000034ULL));
loc_00861E07:
    goto loc_00861425;
loc_00861E11:
    result = CmpAttachToRegistryProcess(v_stack_m1E0 + 168, (uint32_t)(0x3C80ULL), (uint32_t)(0xC0000034ULL), Arg4);
loc_00861E37:
    v_stack_m1E4 = 0x40000016ULL;
    goto loc_00860158;
loc_00861E47:
loc_00861E51:
    result = CmpUnlockKcb(v_stack_m1E0 + 168, (uint32_t)(0x980ULL), (uint32_t)(0xC0000034ULL), Arg4);
    *(uint64_t *)(result) = v_stack_m1B8;
    goto loc_00860541;
loc_00861E5E:
    result = CmpUnlockKcb(v_stack_m1E0 + 168, (uint32_t)(0x980ULL), (uint32_t)(0xC0000034ULL), Arg4);
    result = CmpUnlockHashEntryByIndex(local_rsi, (uint32_t)((uint32_t)(local_rsi)), (uint32_t)(0xC0000034ULL), Arg4);
    goto loc_00860B12;
loc_00861E72:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, (uint32_t)((uint32_t)(local_rsi)), (uint32_t)(0xC0000034ULL), Arg4);
    local_rsp = (local_rsp) + (528);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg6` | `+ 0x0` | `128` | `R` |
| `Arg7` | `+ 0x0` | `64` | `R` |
| `Arg7` | `+ 0x0` | `64` | `W` |
| `Arg7` | `+ 0x58` | `64` | `R` |
| `Arg7` | `+ 0xA0` | `128` | `R` |
| `Arg7` | `+ 0xB0` | `128` | `R` |
| `Arg7` | `+ 0xC0` | `128` | `R` |
| `Arg7` | `+ 0xD0` | `64` | `W` |
| `Arg7` | `+ 0xD8` | `64` | `R` |
| `Arg7` | `+ 0x180` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0085F750&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
