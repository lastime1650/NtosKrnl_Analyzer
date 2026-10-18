# CmRenameKey

- RVA: `0x007E8F48`–`0x007EA1C1` (길이 `4,729` bytes)
- VA: `0x00000001407E8F48`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A4B8C`
- 디코드: `1,206`개 명령, `4,729/4,729` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **151**; 고유 호출 대상: **79**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x007E8FBD` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x007E9011` → [HvpGetCellContextInitialize](../85/HvpGetCellContextInitialize_function_00855F10.md) (function, `0x00855F10`)
- `0x007E901A` → [HvpGetCellContextInitialize](../85/HvpGetCellContextInitialize_function_00855F10.md) (function, `0x00855F10`)
- `0x007E902F` → [HvpGetCellContextInitialize](../85/HvpGetCellContextInitialize_function_00855F10.md) (function, `0x00855F10`)
- `0x007E9038` → [HvpGetCellContextInitialize](../85/HvpGetCellContextInitialize_function_00855F10.md) (function, `0x00855F10`)
- `0x007E9049` → [HvpGetCellContextInitialize](../85/HvpGetCellContextInitialize_function_00855F10.md) (function, `0x00855F10`)
- `0x007E9069` → [CmpSubtreeEnumeratorInitialize](../AD/CmpSubtreeEnumeratorInitialize_function_00AD4CF8.md) (function, `0x00AD4CF8`)
- `0x007E9072` → [CmpInitializeDelayDerefContext](../../text/42/CmpInitializeDelayDerefContext_function_0042A7F0.md) (function, `0x0042A7F0`)
- `0x007E9089` → [CmpIsShutdownRundownActive](../../pagecmrc/BC/CmpIsShutdownRundownActive_function_00BC9C20.md) (function, `0x00BC9C20`)
- `0x007E9096` → [CmpLockRegistryExclusive](../84/CmpLockRegistryExclusive_function_0084F9B4.md) (function, `0x0084F9B4`)
- `0x007E90B0` → [CmpStartKcbStackForTopLayerKcb](../84/CmpStartKcbStackForTopLayerKcb_function_00848390.md) (function, `0x00848390`)
- `0x007E90CA` → [CmpStartKcbStackForTopLayerKcb](../84/CmpStartKcbStackForTopLayerKcb_function_00848390.md) (function, `0x00848390`)
- `0x007E911F` → [CmpPerformKeyBodyDeletionCheck](../../pagecmrc/BC/CmpPerformKeyBodyDeletionCheck_function_00BC97D0.md) (function, `0x00BC97D0`)
- `0x007E914D` → [CmpTransSearchAddTransFromKeyBody](../87/CmpTransSearchAddTransFromKeyBody_function_008736B8.md) (function, `0x008736B8`)
- `0x007E916A` → [CmpPerformKeyBodyDeletionCheck](../../pagecmrc/BC/CmpPerformKeyBodyDeletionCheck_function_00BC97D0.md) (function, `0x00BC97D0`)
- `0x007E919D` → [CmpCheckKcbStackAccess](../70/CmpCheckKcbStackAccess_function_00701174.md) (function, `0x00701174`)
- `0x007E91DC` → [CmpDoAccessCheckOnLayeredSubtree](../94/CmpDoAccessCheckOnLayeredSubtree_function_00945488.md) (function, `0x00945488`)
- `0x007E91FE` → [CmpFlushNotifiesOnKeyBodyList](../9B/CmpFlushNotifiesOnKeyBodyList_function_009B3594.md) (function, `0x009B3594`)
- `0x007E920C` → [CmpReportNotify](../8C/CmpReportNotify_function_008C8094.md) (function, `0x008C8094`)
- `0x007E921A` → [CmpTryAcquireKcbIXLocks](../9B/CmpTryAcquireKcbIXLocks_function_009B056C.md) (function, `0x009B056C`)
- `0x007E9248` → [CmpTryAcquireKcbIXLocks](../9B/CmpTryAcquireKcbIXLocks_function_009B056C.md) (function, `0x009B056C`)
- `0x007E927C` → [CmpHashUnicodeComponent](../84/CmpHashUnicodeComponent_function_0084AC24.md) (function, `0x0084AC24`)
- `0x007E929A` → [CmpFindKcbInHashEntryByName](../94/CmpFindKcbInHashEntryByName_function_0094D7A0.md) (function, `0x0094D7A0`)
- `0x007E92B5` → [CmpReferenceKeyControlBlock](../85/CmpReferenceKeyControlBlock_function_0085D370.md) (function, `0x0085D370`)
- `0x007E92CB` → [CmpStartKcbStackForTopLayerKcb](../84/CmpStartKcbStackForTopLayerKcb_function_00848390.md) (function, `0x00848390`)
- `0x007E92E4` → [CmpIsKeyStackDeleted](../84/CmpIsKeyStackDeleted_function_008426E0.md) (function, `0x008426E0`)
- `0x007E930D` → [CmpGetKcbAtLayerHeight](../94/CmpGetKcbAtLayerHeight_function_00949210.md) (function, `0x00949210`)
- `0x007E9318` → [CmpGetEffectiveKcbSemantics](../84/CmpGetEffectiveKcbSemantics_function_00848E20.md) (function, `0x00848E20`)
- `0x007E9342` → [CmpTryAcquireKcbIXLocks](../9B/CmpTryAcquireKcbIXLocks_function_009B056C.md) (function, `0x009B056C`)
- `0x007E9370` → [CmpPrepareToInvalidateAllHigherLayerKcbs](../7F/CmpPrepareToInvalidateAllHigherLayerKcbs_function_007F174C.md) (function, `0x007F174C`)
- `0x007E939B` → [CmpPrepareForSubtreeInvalidation](../9B/CmpPrepareForSubtreeInvalidation_function_009B01B0.md) (function, `0x009B01B0`)
- `0x007E9412` → [CmpGetKcbAtLayerHeight](../94/CmpGetKcbAtLayerHeight_function_00949210.md) (function, `0x00949210`)
- `0x007E9425` → [CmpGetEffectiveKcbSemantics](../84/CmpGetEffectiveKcbSemantics_function_00848E20.md) (function, `0x00848E20`)
- `0x007E9448` → [CmpGetKeyNodeForKcb](../85/CmpGetKeyNodeForKcb_function_00856480.md) (function, `0x00856480`)
- `0x007E945C` → [CmpFindSubKeyByNameWithStatus](../85/CmpFindSubKeyByNameWithStatus_function_00852770.md) (function, `0x00852770`)
- `0x007E947E` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x007E9485` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x007E94A8` → [CmpGetEffectiveKcbSemantics](../84/CmpGetEffectiveKcbSemantics_function_00848E20.md) (function, `0x00848E20`)
- `0x007E951B` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x007E9522` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x007E9532` → [CmpGetEffectiveKeyNodeSemantics](../94/CmpGetEffectiveKeyNodeSemantics_function_00946D18.md) (function, `0x00946D18`)
- `0x007E9550` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x007E9557` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x007E9587` → [CmpPrepareToInvalidateAllHigherLayerKcbs](../7F/CmpPrepareToInvalidateAllHigherLayerKcbs_function_007F174C.md) (function, `0x007F174C`)
- `0x007E95B7` → [CmpPrepareForSubtreeInvalidation](../9B/CmpPrepareForSubtreeInvalidation_function_009B01B0.md) (function, `0x009B01B0`)
- `0x007E95EA` → [CmpLogTransactionAbortedWithChildName](../9A/CmpLogTransactionAbortedWithChildName_function_009AED70.md) (function, `0x009AED70`)
- `0x007E9602` → [CmpDereferenceKeyControlBlockWithLock](../86/CmpDereferenceKeyControlBlockWithLock_function_00862B60.md) (function, `0x00862B60`)
- `0x007E9613` → [CmpDrainDelayDerefContext](../../text/41/CmpDrainDelayDerefContext_function_0041B9A0.md) (function, `0x0041B9A0`)
- `0x007E9618` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x007E9627` → [CmpAbortRollbackPacket](../AB/CmpAbortRollbackPacket_function_00ABEA80.md) (function, `0x00ABEA80`)
- `0x007E963B` → [CmpCleanupRollbackPacket](../9B/CmpCleanupRollbackPacket_function_009B014C.md) (function, `0x009B014C`)
- `0x007E964B` → [CmpCleanupKcbStack](../94/CmpCleanupKcbStack_function_009470A0.md) (function, `0x009470A0`)
- `0x007E9654` → [CmpCleanupKcbStack](../94/CmpCleanupKcbStack_function_009470A0.md) (function, `0x009470A0`)
- `0x007E9671` → [CmpLogTransactionAbortedWithChildName](../9A/CmpLogTransactionAbortedWithChildName_function_009AED70.md) (function, `0x009AED70`)
- `0x007E967C` → [CmpDrainDelayDerefContext](../../text/41/CmpDrainDelayDerefContext_function_0041B9A0.md) (function, `0x0041B9A0`)
- `0x007E9681` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x007E968F` → [CmpAbortRollbackPacket](../AB/CmpAbortRollbackPacket_function_00ABEA80.md) (function, `0x00ABEA80`)
- `0x007E96A3` → [CmpCleanupRollbackPacket](../9B/CmpCleanupRollbackPacket_function_009B014C.md) (function, `0x009B014C`)
- `0x007E96B3` → [CmpCleanupKcbStack](../94/CmpCleanupKcbStack_function_009470A0.md) (function, `0x009470A0`)
- `0x007E96BC` → [CmpCleanupKcbStack](../94/CmpCleanupKcbStack_function_009470A0.md) (function, `0x009470A0`)
- `0x007E9724` → [CmpInvalidateAllHigherLayerKcbs](../7F/CmpInvalidateAllHigherLayerKcbs_function_007F1560.md) (function, `0x007F1560`)
- `0x007E973D` → [CmpInvalidateSubtree](CmpInvalidateSubtree_function_007EAEC0.md) (function, `0x007EAEC0`)
- `0x007E9753` → [CmpFlushNotifiesOnKeyBodyList](../9B/CmpFlushNotifiesOnKeyBodyList_function_009B3594.md) (function, `0x009B3594`)
- `0x007E975F` → [CmpMarkKeyUnbacked](../9B/CmpMarkKeyUnbacked_function_009B3C4C.md) (function, `0x009B3C4C`)
- `0x007E9767` → [CmpDiscardKcb](../9B/CmpDiscardKcb_function_009B2F34.md) (function, `0x009B2F34`)
- `0x007E977C` → [CmpInvalidateAllHigherLayerKcbs](../7F/CmpInvalidateAllHigherLayerKcbs_function_007F1560.md) (function, `0x007F1560`)
- `0x007E979E` → [CmpInvalidateSubtree](CmpInvalidateSubtree_function_007EAEC0.md) (function, `0x007EAEC0`)
- `0x007E97BE` → [CmpGetKcbAtLayerHeight](../94/CmpGetKcbAtLayerHeight_function_00949210.md) (function, `0x00949210`)
- `0x007E97D5` → [CmpFindKcbInHashEntryByName](../94/CmpFindKcbInHashEntryByName_function_0094D7A0.md) (function, `0x0094D7A0`)
- `0x007E97EB` → [CmpReferenceKeyControlBlock](../85/CmpReferenceKeyControlBlock_function_0085D370.md) (function, `0x0085D370`)
- `0x007E97F4` → [CmpDereferenceKeyControlBlockUnsafe](../99/CmpDereferenceKeyControlBlockUnsafe_function_0099F960.md) (function, `0x0099F960`)
- `0x007E981B` → [CmpGetKeyNodeForKcb](../85/CmpGetKeyNodeForKcb_function_00856480.md) (function, `0x00856480`)
- `0x007E982F` → [CmpFindSubKeyByNameWithStatus](../85/CmpFindSubKeyByNameWithStatus_function_00852770.md) (function, `0x00852770`)
- `0x007E9851` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x007E9858` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x007E98AA` → [CmpCreateKeyControlBlock](../85/CmpCreateKeyControlBlock_function_00851DB0.md) (function, `0x00851DB0`)
- `0x007E98C6` → [CmpDereferenceKeyControlBlockUnsafe](../99/CmpDereferenceKeyControlBlockUnsafe_function_0099F960.md) (function, `0x0099F960`)
- `0x007E98EE` → [CmpAllocateLayerInfoForKcb](../85/CmpAllocateLayerInfoForKcb_function_0085CB90.md) (function, `0x0085CB90`)
- `0x007E9910` → [CmpPromoteKey](../84/CmpPromoteKey_function_00844388.md) (function, `0x00844388`)
- `0x007E9926` → [CmpPromoteSubtree](../94/CmpPromoteSubtree_function_00944D60.md) (function, `0x00944D60`)
- `0x007E9945` → [HvpMarkCellDirty](../85/HvpMarkCellDirty_function_00858080.md) (function, `0x00858080`)
- `0x007E9962` → [CmpGetKeyNodeForKcb](../85/CmpGetKeyNodeForKcb_function_00856480.md) (function, `0x00856480`)
- `0x007E9977` → [CmpMarkEntireIndexDirty](../AA/CmpMarkEntireIndexDirty_function_00AA24B4.md) (function, `0x00AA24B4`)
- `0x007E9997` → [CmpMarkEntireIndexDirty](../AA/CmpMarkEntireIndexDirty_function_00AA24B4.md) (function, `0x00AA24B4`)
- `0x007E99B6` → [HvpMarkCellDirty](../85/HvpMarkCellDirty_function_00858080.md) (function, `0x00858080`)
- `0x007E99DA` → [CmpMarkKeyDirty](../84/CmpMarkKeyDirty_function_0084B1FC.md) (function, `0x0084B1FC`)
- `0x007E99FC` → [CmpMarkAllChildrenDirty](../7F/CmpMarkAllChildrenDirty_function_007F3120.md) (function, `0x007F3120`)
- `0x007E9A10` → [CmpNameSize](../85/CmpNameSize_function_0085ABC4.md) (function, `0x0085ABC4`)
- `0x007E9A3D` → [HvAllocateCell](../85/HvAllocateCell_function_00859C94.md) (function, `0x00859C94`)
- `0x007E9A5C` → [CmpGetKeyNodeForKcb](../85/CmpGetKeyNodeForKcb_function_00856480.md) (function, `0x00856480`)
- `0x007E9AA7` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x007E9ABC` → [CmpSubtreeEnumeratorStartForKcbStack](../94/CmpSubtreeEnumeratorStartForKcbStack_function_009445EC.md) (function, `0x009445EC`)
- `0x007E9ACF` → [CmpSubtreeEnumeratorAdvance](../94/CmpSubtreeEnumeratorAdvance_function_00946590.md) (function, `0x00946590`)
- `0x007E9AEC` → [CmpSubtreeEnumeratorGetCurrentKeyStacks](../A7/CmpSubtreeEnumeratorGetCurrentKeyStacks_function_00A7AE18.md) (function, `0x00A7AE18`)
- `0x007E9AFA` → [CmpKeyNodeStackGetEntryAtLayerHeight](../94/CmpKeyNodeStackGetEntryAtLayerHeight_function_00946ABC.md) (function, `0x00946ABC`)
- `0x007E9B0C` → [HvpMarkCellDirty](../85/HvpMarkCellDirty_function_00858080.md) (function, `0x00858080`)
- `0x007E9B2E` → [CmpSubtreeEnumeratorCleanup](../94/CmpSubtreeEnumeratorCleanup_function_00945D98.md) (function, `0x00945D98`)
- `0x007E9B57` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x007E9B61` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x007E9B75` → [CmpCopyName](../85/CmpCopyName_function_0085AF98.md) (function, `0x0085AF98`)
- `0x007E9BBE` → [CmpReferenceSecurityNode](CmpReferenceSecurityNode_function_007ED6A0.md) (function, `0x007ED6A0`)
- `0x007E9BED` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x007E9BF4` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x007E9C06` → [CmpGetNameControlBlock](../84/CmpGetNameControlBlock_function_0084A750.md) (function, `0x0084A750`)
- `0x007E9C3B` → [CmpDuplicateIndex](../84/CmpDuplicateIndex_function_008420C0.md) (function, `0x008420C0`)
- `0x007E9C62` → [CmpDuplicateIndex](../84/CmpDuplicateIndex_function_008420C0.md) (function, `0x008420C0`)
- `0x007E9C90` → [CmpRemoveSubKeyFromList](../84/CmpRemoveSubKeyFromList_function_0084A030.md) (function, `0x0084A030`)
- `0x007E9CBD` → [CmpAddSubKeyToList](../84/CmpAddSubKeyToList_function_0084D644.md) (function, `0x0084D644`)
- `0x007E9CEF` → [CmpRemoveSubKeyFromList](../84/CmpRemoveSubKeyFromList_function_0084A030.md) (function, `0x0084A030`)
- `0x007E9D54` → [CmpCleanUpSubKeyInfo](../84/CmpCleanUpSubKeyInfo_function_0084C6F4.md) (function, `0x0084C6F4`)
- `0x007E9D87` → [HvFreeCell](../85/HvFreeCell_function_0085A72C.md) (function, `0x0085A72C`)
- `0x007E9D9B` → [CmpGetKeyNodeForKcb](../85/CmpGetKeyNodeForKcb_function_00856480.md) (function, `0x00856480`)
- `0x007E9DF4` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x007E9DFB` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x007E9E55` → [CmpDereferenceKeyControlBlockWithLock](../86/CmpDereferenceKeyControlBlockWithLock_function_00862B60.md) (function, `0x00862B60`)
- `0x007E9E6C` → [CmpCreateLayerLink](../85/CmpCreateLayerLink_function_0085CB00.md) (function, `0x0085CB00`)
- `0x007E9E7C` → [CmpRemoveKeyHash](../9B/CmpRemoveKeyHash_function_009B31D8.md) (function, `0x009B31D8`)
- `0x007E9E8A` → [CmpInsertKeyHash](CmpInsertKeyHash_function_007EAE68.md) (function, `0x007EAE68`)
- `0x007E9ECC` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x007E9EED` → [CmpUpdateParentForEachSon](../7F/CmpUpdateParentForEachSon_function_007F35B8.md) (function, `0x007F35B8`)
- `0x007E9F16` → [CmpKeyEnumStackReset](../94/CmpKeyEnumStackReset_function_0094648C.md) (function, `0x0094648C`)
- `0x007E9F3F` → [CmpResetKeyNodeStack](../94/CmpResetKeyNodeStack_function_00945E14.md) (function, `0x00945E14`)
- `0x007E9F4F` → [CmpSubtreeEnumeratorBeginForKcbStack](../7F/CmpSubtreeEnumeratorBeginForKcbStack_function_007F18DC.md) (function, `0x007F18DC`)
- `0x007E9F5B` → [CmpSubtreeEnumeratorAdvance](../94/CmpSubtreeEnumeratorAdvance_function_00946590.md) (function, `0x00946590`)
- `0x007E9F7F` → [CmpSubtreeEnumeratorGetCurrentKeyStacks](../A7/CmpSubtreeEnumeratorGetCurrentKeyStacks_function_00A7AE18.md) (function, `0x00A7AE18`)
- `0x007E9F8D` → [CmpKeyNodeStackGetEntryAtLayerHeight](../94/CmpKeyNodeStackGetEntryAtLayerHeight_function_00946ABC.md) (function, `0x00946ABC`)
- `0x007E9FA1` → [CmpSubtreeEnumeratorAdvance](../94/CmpSubtreeEnumeratorAdvance_function_00946590.md) (function, `0x00946590`)
- `0x007E9FCA` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x007E9FD1` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x007E9FE2` → [CmpSearchForOpenSubKeys](../9A/CmpSearchForOpenSubKeys_function_009AE76C.md) (function, `0x009AE76C`)
- `0x007EA004` → [CmpFreeKeyByCell](../84/CmpFreeKeyByCell_function_0084AD70.md) (function, `0x0084AD70`)
- `0x007EA049` → [CmpLogUnsupportedOperation](../9A/CmpLogUnsupportedOperation_function_009AEA40.md) (function, `0x009AEA40`)
- `0x007EA07E` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x007EA09E` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x007EA0A5` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x007EA0B8` → [CmpDereferenceSecurityNode](../../text/4A/CmpDereferenceSecurityNode_function_004A672C.md) (function, `0x004A672C`)
- `0x007EA0D6` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x007EA0DD` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x007EA0F3` → [CmpFreeIndexByCell](../AA/CmpFreeIndexByCell_function_00AA6F0C.md) (function, `0x00AA6F0C`)
- `0x007EA105` → [CmpFreeIndexByCell](../AA/CmpFreeIndexByCell_function_00AA6F0C.md) (function, `0x00AA6F0C`)
- `0x007EA118` → [HvFreeCell](../85/HvFreeCell_function_0085A72C.md) (function, `0x0085A72C`)
- `0x007EA125` → [CmpDereferenceNameControlBlockWithLock](../86/CmpDereferenceNameControlBlockWithLock_function_00862840.md) (function, `0x00862840`)
- `0x007EA13D` → [CmpDereferenceKeyControlBlockWithLock](../86/CmpDereferenceKeyControlBlockWithLock_function_00862B60.md) (function, `0x00862B60`)
- `0x007EA155` → [CmpDereferenceKeyControlBlockWithLock](../86/CmpDereferenceKeyControlBlockWithLock_function_00862B60.md) (function, `0x00862B60`)
- `0x007EA160` → [CmpDrainDelayDerefContext](../../text/41/CmpDrainDelayDerefContext_function_0041B9A0.md) (function, `0x0041B9A0`)
- `0x007EA16A` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x007EA173` → [CmpCleanupKcbStack](../94/CmpCleanupKcbStack_function_009470A0.md) (function, `0x009470A0`)
- `0x007EA17C` → [CmpCleanupKcbStack](../94/CmpCleanupKcbStack_function_009470A0.md) (function, `0x009470A0`)
- `0x007EA185` → [CmpCleanupKcbStack](../94/CmpCleanupKcbStack_function_009470A0.md) (function, `0x009470A0`)
- `0x007EA18E` → [CmpCleanupRollbackPacket](../9B/CmpCleanupRollbackPacket_function_009B014C.md) (function, `0x009B014C`)
- `0x007EA1A0` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [NtRenameKey](NtRenameKey_function_007E04B0.md) at `0x007E086D`

### Static image references
- `0x007E8F67` → RVA `0x00E0A740` (`.data`; read)
- `0x007E90FE` → RVA `0x00FD9A90` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **14**
  - `0x007E8FBD` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x007E9072` → [CmpInitializeDelayDerefContext](../../text/42/CmpInitializeDelayDerefContext_function_0042A7F0.md) (`PAGE` → `.text`)
  - `0x007E9089` → [CmpIsShutdownRundownActive](../../pagecmrc/BC/CmpIsShutdownRundownActive_function_00BC9C20.md) (`PAGE` → `PAGECMRC`)
  - `0x007E911F` → [CmpPerformKeyBodyDeletionCheck](../../pagecmrc/BC/CmpPerformKeyBodyDeletionCheck_function_00BC97D0.md) (`PAGE` → `PAGECMRC`)
  - `0x007E916A` → [CmpPerformKeyBodyDeletionCheck](../../pagecmrc/BC/CmpPerformKeyBodyDeletionCheck_function_00BC97D0.md) (`PAGE` → `PAGECMRC`)
  - `0x007E9613` → [CmpDrainDelayDerefContext](../../text/41/CmpDrainDelayDerefContext_function_0041B9A0.md) (`PAGE` → `.text`)
  - `0x007E9618` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x007E967C` → [CmpDrainDelayDerefContext](../../text/41/CmpDrainDelayDerefContext_function_0041B9A0.md) (`PAGE` → `.text`)
  - `0x007E9681` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x007E9ECC` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x007EA0B8` → [CmpDereferenceSecurityNode](../../text/4A/CmpDereferenceSecurityNode_function_004A672C.md) (`PAGE` → `.text`)
  - `0x007EA160` → [CmpDrainDelayDerefContext](../../text/41/CmpDrainDelayDerefContext_function_0041B9A0.md) (`PAGE` → `.text`)
  - `0x007EA16A` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x007EA1A0` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007E8F48  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
007E8F4D  55                              push rbp
007E8F4E  56                              push rsi
007E8F4F  57                              push rdi
007E8F50  41 54                           push r12
007E8F52  41 55                           push r13
007E8F54  41 56                           push r14
007E8F56  41 57                           push r15
007E8F58  48 8D AC 24 F0 FE FF FF         lea rbp, [rsp - 0x110]
007E8F60  48 81 EC 10 02 00 00            sub rsp, 0x210
007E8F67  48 8B 05 D2 17 62 00            mov rax, qword ptr [rip + 0x6217d2]
007E8F6E  48 33 C4                        xor rax, rsp
007E8F71  48 89 85 00 01 00 00            mov qword ptr [rbp + 0x100], rax
007E8F78  45 33 F6                        xor r14d, r14d
007E8F7B  48 89 55 90                     mov qword ptr [rbp - 0x70], rdx
007E8F7F  41 8A D8                        mov bl, r8b
007E8F82  48 89 4D E8                     mov qword ptr [rbp - 0x18], rcx
007E8F86  4C 8B E1                        mov r12, rcx
007E8F89  88 5C 24 60                     mov byte ptr [rsp + 0x60], bl
007E8F8D  0F 57 C0                        xorps xmm0, xmm0
007E8F90  4C 89 75 20                     mov qword ptr [rbp + 0x20], r14
007E8F94  45 8D 46 68                     lea r8d, [r14 + 0x68]
007E8F98  4C 89 75 E0                     mov qword ptr [rbp - 0x20], r14
007E8F9C  33 D2                           xor edx, edx
007E8F9E  4C 89 75 C8                     mov qword ptr [rbp - 0x38], r14
007E8FA2  48 8D 8D 90 00 00 00            lea rcx, [rbp + 0x90]
007E8FA9  4C 89 75 08                     mov qword ptr [rbp + 8], r14
007E8FAD  0F 11 45 F0                     movups xmmword ptr [rbp - 0x10], xmm0
007E8FB1  4C 89 75 D0                     mov qword ptr [rbp - 0x30], r14
007E8FB5  44 89 75 C0                     mov dword ptr [rbp - 0x40], r14d
007E8FB9  4C 89 75 00                     mov qword ptr [rbp], r14
007E8FBD  E8 7E DC ED FF                  call 0x1406c6c40
007E8FC2  0F 57 C0                        xorps xmm0, xmm0
007E8FC5  4C 89 75 10                     mov qword ptr [rbp + 0x10], r14
007E8FC9  83 C8 FF                        or eax, 0xffffffff
007E8FCC  4C 89 75 A0                     mov qword ptr [rbp - 0x60], r14
007E8FD0  0F 57 C9                        xorps xmm1, xmm1
007E8FD3  4C 89 75 98                     mov qword ptr [rbp - 0x68], r14
007E8FD7  0F 11 4D 28                     movups xmmword ptr [rbp + 0x28], xmm1
007E8FDB  48 8D 4D E0                     lea rcx, [rbp - 0x20]
007E8FDF  66 89 45 2A                     mov word ptr [rbp + 0x2a], ax
007E8FE3  0F 11 45 48                     movups xmmword ptr [rbp + 0x48], xmm0
007E8FE7  66 89 45 4A                     mov word ptr [rbp + 0x4a], ax
007E8FEB  45 8B FE                        mov r15d, r14d
007E8FEE  0F 11 45 68                     movups xmmword ptr [rbp + 0x68], xmm0
007E8FF2  66 89 45 6A                     mov word ptr [rbp + 0x6a], ax
007E8FF6  45 8B EE                        mov r13d, r14d
007E8FF9  0F 11 45 B0                     movups xmmword ptr [rbp - 0x50], xmm0
007E8FFD  41 8B FE                        mov edi, r14d
007E9000  4C 89 74 24 68                  mov qword ptr [rsp + 0x68], r14
007E9005  0F 11 4D 38                     movups xmmword ptr [rbp + 0x38], xmm1
007E9009  0F 11 45 58                     movups xmmword ptr [rbp + 0x58], xmm0
007E900D  0F 11 45 78                     movups xmmword ptr [rbp + 0x78], xmm0
007E9011  E8 FA CE 06 00                  call 0x140855f10
007E9016  48 8D 4D C8                     lea rcx, [rbp - 0x38]
007E901A  E8 F1 CE 06 00                  call 0x140855f10
007E901F  41 83 C8 FF                     or r8d, 0xffffffff
007E9023  4C 89 75 A8                     mov qword ptr [rbp - 0x58], r14
007E9027  48 8D 4D 08                     lea rcx, [rbp + 8]
007E902B  44 89 45 88                     mov dword ptr [rbp - 0x78], r8d
007E902F  E8 DC CE 06 00                  call 0x140855f10
007E9034  48 8D 4D D0                     lea rcx, [rbp - 0x30]
007E9038  E8 D3 CE 06 00                  call 0x140855f10
007E903D  48 8D 4D 00                     lea rcx, [rbp]
007E9041  44 89 45 C4                     mov dword ptr [rbp - 0x3c], r8d
007E9045  4C 89 75 D8                     mov qword ptr [rbp - 0x28], r14
007E9049  E8 C2 CE 06 00                  call 0x140855f10
007E904E  48 8D 8D 90 00 00 00            lea rcx, [rbp + 0x90]
007E9055  4C 89 74 24 58                  mov qword ptr [rsp + 0x58], r14
007E905A  44 89 44 24 70                  mov dword ptr [rsp + 0x70], r8d
007E905F  44 89 44 24 74                  mov dword ptr [rsp + 0x74], r8d
007E9064  44 88 74 24 52                  mov byte ptr [rsp + 0x52], r14b
007E9069  E8 8A BC 2E 00                  call 0x140ad4cf8
007E906E  48 8D 4D F0                     lea rcx, [rbp - 0x10]
007E9072  E8 79 17 C4 FF                  call 0x14042a7f0
007E9077  48 B9 14 00 00 00 80 F7 FF FF   movabs rcx, 0xfffff78000000014
007E9081  48 8B 31                        mov rsi, qword ptr [rcx]
007E9084  48 89 7C 24 78                  mov qword ptr [rsp + 0x78], rdi
007E9089  E8 92 0B 3E 00                  call 0x140bc9c20
007E908E  84 C0                           test al, al
007E9090  0F 85 D3 0F 00 00               jne 0x1407ea069
007E9096  E8 19 69 06 00                  call 0x14084f9b4
007E909B  4D 8B 7C 24 08                  mov r15, qword ptr [r12 + 8]
007E90A0  48 8D 4D 28                     lea rcx, [rbp + 0x28]
007E90A4  49 8B D7                        mov rdx, r15
007E90A7  C6 44 24 50 01                  mov byte ptr [rsp + 0x50], 1
007E90AC  4D 8B 6F 48                     mov r13, qword ptr [r15 + 0x48]
007E90B0  E8 DB F2 05 00                  call 0x140848390
007E90B5  44 8B F0                        mov r14d, eax
007E90B8  33 C0                           xor eax, eax
007E90BA  45 85 F6                        test r14d, r14d
007E90BD  0F 88 1E 06 00 00               js 0x1407e96e1
007E90C3  49 8B D5                        mov rdx, r13
007E90C6  48 8D 4D 48                     lea rcx, [rbp + 0x48]
007E90CA  E8 C1 F2 05 00                  call 0x140848390
007E90CF  33 D2                           xor edx, edx
007E90D1  44 8B F0                        mov r14d, eax
007E90D4  85 C0                           test eax, eax
007E90D6  0F 88 85 0F 00 00               js 0x1407ea061
007E90DC  41 F7 47 08 80 01 00 00         test dword ptr [r15 + 8], 0x180
007E90E4  0F 85 71 0F 00 00               jne 0x1407ea05b
007E90EA  49 8B 4F 20                     mov rcx, qword ptr [r15 + 0x20]
007E90EE  F7 81 A0 00 00 00 00 00 10 00   test dword ptr [rcx + 0xa0], 0x100000
007E90F8  0F 85 5D 0F 00 00               jne 0x1407ea05b
007E90FE  48 3B 0D 8B 09 7F 00            cmp rcx, qword ptr [rip + 0x7f098b]
007E9105  0F 84 50 0F 00 00               je 0x1407ea05b
007E910B  41 F7 87 B8 00 00 00 00 00 04 00  test dword ptr [r15 + 0xb8], 0x40000
007E9116  0F 85 3F 0F 00 00               jne 0x1407ea05b
007E911C  49 8B CC                        mov rcx, r12
007E911F  E8 AC 06 3E 00                  call 0x140bc97d0
007E9124  44 8B F0                        mov r14d, eax
007E9127  33 C0                           xor eax, eax
007E9129  45 85 F6                        test r14d, r14d
007E912C  0F 88 AF 05 00 00               js 0x1407e96e1
007E9132  49 39 44 24 38                  cmp qword ptr [r12 + 0x38], rax
007E9137  75 0D                           jne 0x1407e9146
007E9139  49 39 44 24 40                  cmp qword ptr [r12 + 0x40], rax
007E913E  75 06                           jne 0x1407e9146
007E9140  48 89 45 20                     mov qword ptr [rbp + 0x20], rax
007E9144  EB 44                           jmp 0x1407e918a
007E9146  48 8D 55 20                     lea rdx, [rbp + 0x20]
007E914A  49 8B CC                        mov rcx, r12
007E914D  E8 66 A5 08 00                  call 0x1408736b8
007E9152  44 8B F0                        mov r14d, eax
007E9155  33 C0                           xor eax, eax
007E9157  45 85 F6                        test r14d, r14d
007E915A  0F 88 81 05 00 00               js 0x1407e96e1
007E9160  48 8B 5D 20                     mov rbx, qword ptr [rbp + 0x20]
007E9164  49 8B CC                        mov rcx, r12
007E9167  48 8B D3                        mov rdx, rbx
007E916A  E8 61 06 3E 00                  call 0x140bc97d0
007E916F  44 8B F0                        mov r14d, eax
007E9172  33 C0                           xor eax, eax
007E9174  45 85 F6                        test r14d, r14d
007E9177  0F 88 64 05 00 00               js 0x1407e96e1
007E917D  48 85 DB                        test rbx, rbx
007E9180  0F 85 BE 0E 00 00               jne 0x1407ea044
007E9186  8A 5C 24 60                     mov bl, byte ptr [rsp + 0x60]
007E918A  41 B9 04 00 00 00               mov r9d, 4
007E9190  88 44 24 20                     mov byte ptr [rsp + 0x20], al
007E9194  44 8A C3                        mov r8b, bl
007E9197  48 8D 4D 48                     lea rcx, [rbp + 0x48]
007E919B  33 D2                           xor edx, edx
007E919D  E8 D2 7F F1 FF                  call 0x140701174
007E91A2  44 8B F0                        mov r14d, eax
007E91A5  33 C0                           xor eax, eax
007E91A7  45 85 F6                        test r14d, r14d
007E91AA  0F 88 31 05 00 00               js 0x1407e96e1
007E91B0  41 0F B7 47 42                  movzx eax, word ptr [r15 + 0x42]
007E91B5  44 8A CB                        mov r9b, bl
007E91B8  66 F7 D8                        neg ax
007E91BB  C7 44 24 28 01 00 00 00         mov dword ptr [rsp + 0x28], 1
007E91C3  1B C9                           sbb ecx, ecx
007E91C5  45 33 C0                        xor r8d, r8d
007E91C8  81 E1 19 00 02 00               and ecx, 0x20019
007E91CE  81 C1 00 00 01 00               add ecx, 0x10000
007E91D4  89 4C 24 20                     mov dword ptr [rsp + 0x20], ecx
007E91D8  48 8D 4D 28                     lea rcx, [rbp + 0x28]
007E91DC  E8 A7 C2 15 00                  call 0x140945488
007E91E1  44 8B F0                        mov r14d, eax
007E91E4  33 C0                           xor eax, eax
007E91E6  45 85 F6                        test r14d, r14d
007E91E9  0F 88 F2 04 00 00               js 0x1407e96e1
007E91EF  8D 58 01                        lea ebx, [rax + 1]
007E91F2  33 D2                           xor edx, edx
007E91F4  44 8A CB                        mov r9b, bl
007E91F7  4C 8D 45 F0                     lea r8, [rbp - 0x10]
007E91FB  49 8B CF                        mov rcx, r15
007E91FE  E8 91 A3 1C 00                  call 0x1409b3594
007E9203  45 33 C9                        xor r9d, r9d
007E9206  44 8B C3                        mov r8d, ebx
007E9209  49 8B CF                        mov rcx, r15
007E920C  E8 83 EE 0D 00                  call 0x1408c8094
007E9211  4C 8D 4D B0                     lea r9, [rbp - 0x50]
007E9215  8A D3                           mov dl, bl
007E9217  49 8B CF                        mov rcx, r15
007E921A  E8 4D 73 1C 00                  call 0x1409b056c
007E921F  8B D8                           mov ebx, eax
007E9221  44 8B F0                        mov r14d, eax
007E9224  B8 00 00 00 80                  mov eax, 0x80000000
007E9229  8D 0C 03                        lea ecx, [rbx + rax]
007E922C  85 C8                           test eax, ecx
007E922E  75 0C                           jne 0x1407e923c
007E9230  81 FB 2D 02 00 C0               cmp ebx, 0xc000022d
007E9236  0F 85 93 04 00 00               jne 0x1407e96cf
007E923C  4C 8D 4D B0                     lea r9, [rbp - 0x50]
007E9240  BA 01 00 00 00                  mov edx, 1
007E9245  49 8B CD                        mov rcx, r13
007E9248  E8 1F 73 1C 00                  call 0x1409b056c
007E924D  44 8B F0                        mov r14d, eax
007E9250  B8 2D 02 00 C0                  mov eax, 0xc000022d
007E9255  44 3B F0                        cmp r14d, eax
007E9258  0F 84 01 04 00 00               je 0x1407e965f
007E925E  3B D8                           cmp ebx, eax
007E9260  0F 94 44 24 54                  sete byte ptr [rsp + 0x54]
007E9265  33 FF                           xor edi, edi
007E9267  45 85 F6                        test r14d, r14d
007E926A  0F 88 B7 0D 00 00               js 0x1407ea027
007E9270  3B D8                           cmp ebx, eax
007E9272  0F 84 E9 03 00 00               je 0x1407e9661
007E9278  48 8B 4D 90                     mov rcx, qword ptr [rbp - 0x70]
007E927C  E8 A3 19 06 00                  call 0x14084ac24
007E9281  41 6B 7D 10 25                  imul edi, dword ptr [r13 + 0x10], 0x25
007E9286  4D 8B C5                        mov r8, r13
007E9289  4C 8B 4D 90                     mov r9, qword ptr [rbp - 0x70]
007E928D  8B D8                           mov ebx, eax
007E928F  49 8B 4D 20                     mov rcx, qword ptr [r13 + 0x20]
007E9293  89 45 18                        mov dword ptr [rbp + 0x18], eax
007E9296  03 F8                           add edi, eax
007E9298  8B D7                           mov edx, edi
007E929A  E8 01 45 16 00                  call 0x14094d7a0
007E929F  45 33 DB                        xor r11d, r11d
007E92A2  48 89 45 A0                     mov qword ptr [rbp - 0x60], rax
007E92A6  4C 8B F0                        mov r14, rax
007E92A9  48 85 C0                        test rax, rax
007E92AC  0F 84 34 01 00 00               je 0x1407e93e6
007E92B2  48 8B C8                        mov rcx, rax
007E92B5  E8 B6 40 07 00                  call 0x14085d370
007E92BA  41 8B 46 28                     mov eax, dword ptr [r14 + 0x28]
007E92BE  48 8D 4D 68                     lea rcx, [rbp + 0x68]
007E92C2  49 8B D6                        mov rdx, r14
007E92C5  89 45 80                        mov dword ptr [rbp - 0x80], eax
007E92C8  89 45 84                        mov dword ptr [rbp - 0x7c], eax
007E92CB  E8 C0 F0 05 00                  call 0x140848390
007E92D0  44 8B F0                        mov r14d, eax
007E92D3  33 C0                           xor eax, eax
007E92D5  45 85 F6                        test r14d, r14d
007E92D8  0F 88 F3 03 00 00               js 0x1407e96d1
007E92DE  33 D2                           xor edx, edx
007E92E0  48 8D 4D 68                     lea rcx, [rbp + 0x68]
007E92E4  E8 F7 93 05 00                  call 0x1408426e0
007E92E9  33 C9                           xor ecx, ecx
007E92EB  84 C0                           test al, al
007E92ED  0F 84 F9 03 00 00               je 0x1407e96ec
007E92F3  4C 8B 55 A0                     mov r10, qword ptr [rbp - 0x60]
007E92F7  8D 51 01                        lea edx, [rcx + 1]
007E92FA  45 0F B7 4A 42                  movzx r9d, word ptr [r10 + 0x42]
007E92FF  66 45 85 C9                     test r9w, r9w
007E9303  78 2C                           js 0x1407e9331
007E9305  41 0F B7 D1                     movzx edx, r9w
007E9309  48 8D 4D 68                     lea rcx, [rbp + 0x68]
007E930D  E8 FE FE 15 00                  call 0x140949210
007E9312  48 8B C8                        mov rcx, rax
007E9315  49 8B D4                        mov rdx, r12
007E9318  E8 03 FB 05 00                  call 0x140848e20
007E931D  BA 01 00 00 00                  mov edx, 1
007E9322  3B C2                           cmp eax, edx
007E9324  74 06                           je 0x1407e932c
007E9326  66 41 FF C9                     dec r9w
007E932A  EB D3                           jmp 0x1407e92ff
007E932C  44 8A E2                        mov r12b, dl
007E932F  EB 05                           jmp 0x1407e9336
007E9331  44 8A 64 24 52                  mov r12b, byte ptr [rsp + 0x52]
007E9336  4C 8D 4D B0                     lea r9, [rbp - 0x50]
007E933A  44 88 64 24 52                  mov byte ptr [rsp + 0x52], r12b
007E933F  49 8B CA                        mov rcx, r10
007E9342  E8 25 72 1C 00                  call 0x1409b056c
007E9347  44 8B F0                        mov r14d, eax
007E934A  3D 2D 02 00 C0                  cmp eax, 0xc000022d
007E934F  75 07                           jne 0x1407e9358
007E9351  C6 44 24 54 01                  mov byte ptr [rsp + 0x54], 1
007E9356  EB 0B                           jmp 0x1407e9363
007E9358  33 C0                           xor eax, eax
007E935A  45 85 F6                        test r14d, r14d
007E935D  0F 88 79 03 00 00               js 0x1407e96dc
007E9363  48 8B 4D A0                     mov rcx, qword ptr [rbp - 0x60]
007E9367  4C 8D 45 B0                     lea r8, [rbp - 0x50]
007E936B  BA 02 00 00 00                  mov edx, 2
007E9370  E8 D7 83 00 00                  call 0x1407f174c
007E9375  44 8B F0                        mov r14d, eax
007E9378  3D 2D 02 00 C0                  cmp eax, 0xc000022d
007E937D  75 07                           jne 0x1407e9386
007E937F  C6 44 24 54 01                  mov byte ptr [rsp + 0x54], 1
007E9384  EB 0B                           jmp 0x1407e9391
007E9386  33 C0                           xor eax, eax
007E9388  45 85 F6                        test r14d, r14d
007E938B  0F 88 4B 03 00 00               js 0x1407e96dc
007E9391  48 8B 4D A0                     mov rcx, qword ptr [rbp - 0x60]
007E9395  4C 8D 45 B0                     lea r8, [rbp - 0x50]
007E9399  33 D2                           xor edx, edx
007E939B  E8 10 6E 1C 00                  call 0x1409b01b0
007E93A0  44 8B F0                        mov r14d, eax
007E93A3  3D 2D 02 00 C0                  cmp eax, 0xc000022d
007E93A8  75 14                           jne 0x1407e93be
007E93AA  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
007E93AF  33 C0                           xor eax, eax
007E93B1  44 8B E0                        mov r12d, eax
007E93B4  C6 44 24 54 01                  mov byte ptr [rsp + 0x54], 1
007E93B9  E9 B8 01 00 00                  jmp 0x1407e9576
007E93BE  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
007E93C3  33 D2                           xor edx, edx
007E93C5  44 88 64 24 52                  mov byte ptr [rsp + 0x52], r12b
007E93CA  44 8B E2                        mov r12d, edx
007E93CD  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
007E93D2  45 85 F6                        test r14d, r14d
007E93D5  0F 89 A0 01 00 00               jns 0x1407e957b
007E93DB  48 8B F8                        mov rdi, rax
007E93DE  48 8B DA                        mov rbx, rdx
007E93E1  E9 3C 07 00 00                  jmp 0x1407e9b22
007E93E6  83 4D 84 FF                     or dword ptr [rbp - 0x7c], 0xffffffff
007E93EA  45 0F B7 65 42                  movzx r12d, word ptr [r13 + 0x42]
007E93EF  83 C8 FF                        or eax, 0xffffffff
007E93F2  4C 8B 4D E8                     mov r9, qword ptr [rbp - 0x18]
007E93F6  66 89 44 24 52                  mov word ptr [rsp + 0x52], ax
007E93FB  4C 89 5C 24 68                  mov qword ptr [rsp + 0x68], r11
007E9400  66 45 85 E4                     test r12w, r12w
007E9404  0F 88 D5 00 00 00               js 0x1407e94df
007E940A  41 0F B7 D4                     movzx edx, r12w
007E940E  48 8D 4D 48                     lea rcx, [rbp + 0x48]
007E9412  E8 F9 FD 15 00                  call 0x140949210
007E9417  48 8B C8                        mov rcx, rax
007E941A  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
007E941F  49 8B D1                        mov rdx, r9
007E9422  4C 8B F0                        mov r14, rax
007E9425  E8 F6 F9 05 00                  call 0x140848e20
007E942A  BA 01 00 00 00                  mov edx, 1
007E942F  3B C2                           cmp eax, edx
007E9431  0F 84 9B 00 00 00               je 0x1407e94d2
007E9437  41 83 7E 28 FF                  cmp dword ptr [r14 + 0x28], -1
007E943C  74 77                           je 0x1407e94b5
007E943E  44 8A C2                        mov r8b, dl
007E9441  49 8B CE                        mov rcx, r14
007E9444  48 8D 55 C8                     lea rdx, [rbp - 0x38]
007E9448  E8 33 D0 06 00                  call 0x140856480
007E944D  4C 8B 45 90                     mov r8, qword ptr [rbp - 0x70]
007E9451  4C 8D 4D 84                     lea r9, [rbp - 0x7c]
007E9455  49 8B 4E 20                     mov rcx, qword ptr [r14 + 0x20]
007E9459  48 8B D0                        mov rdx, rax
007E945C  E8 0F 93 06 00                  call 0x140852770
007E9461  BA 01 00 00 00                  mov edx, 1
007E9466  44 8B F0                        mov r14d, eax
007E9469  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
007E946E  48 8B 48 20                     mov rcx, qword ptr [rax + 0x20]
007E9472  84 91 8C 00 00 00               test byte ptr [rcx + 0x8c], dl
007E9478  48 8D 55 C8                     lea rdx, [rbp - 0x38]
007E947C  74 07                           je 0x1407e9485
007E947E  E8 9D 37 07 00                  call 0x14085cc20
007E9483  EB 05                           jmp 0x1407e948a
007E9485  E8 B6 CA 06 00                  call 0x140855f40
007E948A  45 33 DB                        xor r11d, r11d
007E948D  45 85 F6                        test r14d, r14d
007E9490  79 2C                           jns 0x1407e94be
007E9492  41 81 FE 34 00 00 C0            cmp r14d, 0xc0000034
007E9499  0F 85 5E 02 00 00               jne 0x1407e96fd
007E949F  48 8B 55 E8                     mov rdx, qword ptr [rbp - 0x18]
007E94A3  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
007E94A8  E8 73 F9 05 00                  call 0x140848e20
007E94AD  85 C0                           test eax, eax
007E94AF  75 35                           jne 0x1407e94e6
007E94B1  4C 8B 4D E8                     mov r9, qword ptr [rbp - 0x18]
007E94B5  66 41 FF CC                     dec r12w
007E94B9  E9 42 FF FF FF                  jmp 0x1407e9400
007E94BE  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
007E94C3  45 0F B7 F4                     movzx r14d, r12w
007E94C7  4C 8B 50 20                     mov r10, qword ptr [rax + 0x20]
007E94CB  4C 89 54 24 68                  mov qword ptr [rsp + 0x68], r10
007E94D0  EB 1D                           jmp 0x1407e94ef
007E94D2  44 0F B7 74 24 52               movzx r14d, word ptr [rsp + 0x52]
007E94D8  4C 8B 54 24 68                  mov r10, qword ptr [rsp + 0x68]
007E94DD  EB 15                           jmp 0x1407e94f4
007E94DF  4C 8B 54 24 68                  mov r10, qword ptr [rsp + 0x68]
007E94E4  EB 03                           jmp 0x1407e94e9
007E94E6  4D 8B D3                        mov r10, r11
007E94E9  44 0F B7 74 24 52               movzx r14d, word ptr [rsp + 0x52]
007E94EF  BA 01 00 00 00                  mov edx, 1
007E94F4  8B 4D 84                        mov ecx, dword ptr [rbp - 0x7c]
007E94F7  89 4D 80                        mov dword ptr [rbp - 0x80], ecx
007E94FA  83 F9 FF                        cmp ecx, -1
007E94FD  75 0A                           jne 0x1407e9509
007E94FF  44 88 5C 24 52                  mov byte ptr [rsp + 0x52], r11b
007E9504  4D 8B E3                        mov r12, r11
007E9507  EB 72                           jmp 0x1407e957b
007E9509  41 84 92 8C 00 00 00            test byte ptr [r10 + 0x8c], dl
007E9510  4C 8D 45 E0                     lea r8, [rbp - 0x20]
007E9514  8B D1                           mov edx, ecx
007E9516  49 8B CA                        mov rcx, r10
007E9519  74 07                           je 0x1407e9522
007E951B  E8 40 B7 06 00                  call 0x140854c60
007E9520  EB 05                           jmp 0x1407e9527
007E9522  E8 89 B7 06 00                  call 0x140854cb0
007E9527  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
007E952C  48 8B D0                        mov rdx, rax
007E952F  4C 8B E0                        mov r12, rax
007E9532  E8 E1 D7 15 00                  call 0x140946d18
007E9537  BA 01 00 00 00                  mov edx, 1
007E953C  3B C2                           cmp eax, edx
007E953E  0F 85 CD 0A 00 00               jne 0x1407ea011
007E9544  84 91 8C 00 00 00               test byte ptr [rcx + 0x8c], dl
007E954A  48 8D 55 E0                     lea rdx, [rbp - 0x20]
007E954E  74 07                           je 0x1407e9557
007E9550  E8 CB 36 07 00                  call 0x14085cc20
007E9555  EB 05                           jmp 0x1407e955c
007E9557  E8 E4 C9 06 00                  call 0x140855f40
007E955C  33 C9                           xor ecx, ecx
007E955E  C6 44 24 52 01                  mov byte ptr [rsp + 0x52], 1
007E9563  44 8B E1                        mov r12d, ecx
007E9566  66 45 3B 75 42                  cmp r14w, word ptr [r13 + 0x42]
007E956B  74 0E                           je 0x1407e957b
007E956D  83 C8 FF                        or eax, 0xffffffff
007E9570  89 45 80                        mov dword ptr [rbp - 0x80], eax
007E9573  89 45 84                        mov dword ptr [rbp - 0x7c], eax
007E9576  48 89 4C 24 68                  mov qword ptr [rsp + 0x68], rcx
007E957B  4C 8D 45 B0                     lea r8, [rbp - 0x50]
007E957F  BA 02 00 00 00                  mov edx, 2
007E9584  49 8B CF                        mov rcx, r15
007E9587  E8 C0 81 00 00                  call 0x1407f174c
007E958C  33 C9                           xor ecx, ecx
007E958E  44 8B F0                        mov r14d, eax
007E9591  3D 2D 02 00 C0                  cmp eax, 0xc000022d
007E9596  75 07                           jne 0x1407e959f
007E9598  C6 44 24 54 01                  mov byte ptr [rsp + 0x54], 1
007E959D  EB 08                           jmp 0x1407e95a7
007E959F  85 C0                           test eax, eax
007E95A1  0F 88 71 05 00 00               js 0x1407e9b18
007E95A7  66 41 39 4F 42                  cmp word ptr [r15 + 0x42], cx
007E95AC  74 22                           je 0x1407e95d0
007E95AE  4C 8D 45 B0                     lea r8, [rbp - 0x50]
007E95B2  33 D2                           xor edx, edx
007E95B4  49 8B CF                        mov rcx, r15
007E95B7  E8 F4 6B 1C 00                  call 0x1409b01b0
007E95BC  44 8B F0                        mov r14d, eax
007E95BF  3D 2D 02 00 C0                  cmp eax, 0xc000022d
007E95C4  74 14                           je 0x1407e95da
007E95C6  33 C9                           xor ecx, ecx
007E95C8  85 C0                           test eax, eax
007E95CA  0F 88 48 05 00 00               js 0x1407e9b18
007E95D0  38 4C 24 54                     cmp byte ptr [rsp + 0x54], cl
007E95D4  0F 84 31 01 00 00               je 0x1407e970b
007E95DA  8B 45 B0                        mov eax, dword ptr [rbp - 0x50]
007E95DD  33 D2                           xor edx, edx
007E95DF  49 8B CF                        mov rcx, r15
007E95E2  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
007E95E6  44 8D 42 04                     lea r8d, [rdx + 4]
007E95EA  E8 81 57 1C 00                  call 0x1409aed70
007E95EF  48 8B 5D A0                     mov rbx, qword ptr [rbp - 0x60]
007E95F3  48 85 DB                        test rbx, rbx
007E95F6  74 15                           je 0x1407e960d
007E95F8  45 33 C0                        xor r8d, r8d
007E95FB  48 8D 55 F0                     lea rdx, [rbp - 0x10]
007E95FF  48 8B CB                        mov rcx, rbx
007E9602  E8 59 95 07 00                  call 0x140862b60
007E9607  33 DB                           xor ebx, ebx
007E9609  48 89 5D A0                     mov qword ptr [rbp - 0x60], rbx
007E960D  33 D2                           xor edx, edx
007E960F  48 8D 4D F0                     lea rcx, [rbp - 0x10]
007E9613  E8 88 23 C3 FF                  call 0x14041b9a0
007E9618  E8 67 04 3E 00                  call 0x140bc9a84
007E961D  33 D2                           xor edx, edx
007E961F  88 5C 24 50                     mov byte ptr [rsp + 0x50], bl
007E9623  48 8D 4D B0                     lea rcx, [rbp - 0x50]
007E9627  E8 54 54 2D 00                  call 0x140abea80
007E962C  44 8B F0                        mov r14d, eax
007E962F  85 C0                           test eax, eax
007E9631  0F 88 E1 04 00 00               js 0x1407e9b18
007E9637  48 8D 4D B0                     lea rcx, [rbp - 0x50]
007E963B  E8 0C 6B 1C 00                  call 0x1409b014c
007E9640  0F 57 C0                        xorps xmm0, xmm0
007E9643  48 8D 4D 28                     lea rcx, [rbp + 0x28]
007E9647  0F 11 45 B0                     movups xmmword ptr [rbp - 0x50], xmm0
007E964B  E8 50 DA 15 00                  call 0x1409470a0
007E9650  48 8D 4D 48                     lea rcx, [rbp + 0x48]
007E9654  E8 47 DA 15 00                  call 0x1409470a0
007E9659  4C 8B 65 E8                     mov r12, qword ptr [rbp - 0x18]
007E965D  EB 62                           jmp 0x1407e96c1
007E965F  33 FF                           xor edi, edi
007E9661  8B 45 B0                        mov eax, dword ptr [rbp - 0x50]
007E9664  33 D2                           xor edx, edx
007E9666  49 8B CF                        mov rcx, r15
007E9669  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
007E966D  44 8D 42 04                     lea r8d, [rdx + 4]
007E9671  E8 FA 56 1C 00                  call 0x1409aed70
007E9676  33 D2                           xor edx, edx
007E9678  48 8D 4D F0                     lea rcx, [rbp - 0x10]
007E967C  E8 1F 23 C3 FF                  call 0x14041b9a0
007E9681  E8 FE 03 3E 00                  call 0x140bc9a84
007E9686  33 D2                           xor edx, edx
007E9688  48 8D 4D B0                     lea rcx, [rbp - 0x50]
007E968C  40 8A F7                        mov sil, dil
007E968F  E8 EC 53 2D 00                  call 0x140abea80
007E9694  44 8B F0                        mov r14d, eax
007E9697  85 C0                           test eax, eax
007E9699  0F 88 93 09 00 00               js 0x1407ea032
007E969F  48 8D 4D B0                     lea rcx, [rbp - 0x50]
007E96A3  E8 A4 6A 1C 00                  call 0x1409b014c
007E96A8  0F 57 C0                        xorps xmm0, xmm0
007E96AB  48 8D 4D 28                     lea rcx, [rbp + 0x28]
007E96AF  0F 11 45 B0                     movups xmmword ptr [rbp - 0x50], xmm0
007E96B3  E8 E8 D9 15 00                  call 0x1409470a0
007E96B8  48 8D 4D 48                     lea rcx, [rbp + 0x48]
007E96BC  E8 DF D9 15 00                  call 0x1409470a0
007E96C1  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
007E96C6  8A 5C 24 60                     mov bl, byte ptr [rsp + 0x60]
007E96CA  E9 A8 F9 FF FF                  jmp 0x1407e9077
007E96CF  33 C0                           xor eax, eax
007E96D1  4C 8B E0                        mov r12, rax
007E96D4  48 8B D8                        mov rbx, rax
007E96D7  E9 41 04 00 00                  jmp 0x1407e9b1d
007E96DC  48 8B 7C 24 78                  mov rdi, qword ptr [rsp + 0x78]
007E96E1  4C 8B E0                        mov r12, rax
007E96E4  48 8B D8                        mov rbx, rax
007E96E7  E9 36 04 00 00                  jmp 0x1407e9b22
007E96EC  41 BE 21 01 00 C0               mov r14d, 0xc0000121
007E96F2  4C 8B E1                        mov r12, rcx
007E96F5  48 8B D9                        mov rbx, rcx
007E96F8  E9 20 04 00 00                  jmp 0x1407e9b1d
007E96FD  4D 8B E3                        mov r12, r11
007E9700  49 8B FB                        mov rdi, r11
007E9703  49 8B DB                        mov rbx, r11
007E9706  E9 17 04 00 00                  jmp 0x1407e9b22
007E970B  4C 8B 75 A0                     mov r14, qword ptr [rbp - 0x60]
007E970F  4D 85 F6                        test r14, r14
007E9712  74 58                           je 0x1407e976c
007E9714  BA 08 00 00 00                  mov edx, 8
007E9719  4C 8D 4D F0                     lea r9, [rbp - 0x10]
007E971D  49 8B CE                        mov rcx, r14
007E9720  44 8D 42 FA                     lea r8d, [rdx - 6]
007E9724  E8 37 7E 00 00                  call 0x1407f1560
007E9729  33 C0                           xor eax, eax
007E972B  4C 8D 4D F0                     lea r9, [rbp - 0x10]
007E972F  45 33 C0                        xor r8d, r8d
007E9732  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
007E9737  49 8B CE                        mov rcx, r14
007E973A  8D 50 08                        lea edx, [rax + 8]
007E973D  E8 7E 17 00 00                  call 0x1407eaec0
007E9742  41 B9 01 00 00 00               mov r9d, 1
007E9748  4C 8D 45 F0                     lea r8, [rbp - 0x10]
007E974C  49 8B CE                        mov rcx, r14
007E974F  41 8D 51 07                     lea edx, [r9 + 7]
007E9753  E8 3C 9E 1C 00                  call 0x1409b3594
007E9758  48 8D 55 F0                     lea rdx, [rbp - 0x10]
007E975C  49 8B CE                        mov rcx, r14
007E975F  E8 E8 A4 1C 00                  call 0x1409b3c4c
007E9764  49 8B CE                        mov rcx, r14
007E9767  E8 C8 97 1C 00                  call 0x1409b2f34
007E976C  BA 08 00 00 00                  mov edx, 8
007E9771  4C 8D 4D F0                     lea r9, [rbp - 0x10]
007E9775  49 8B CF                        mov rcx, r15
007E9778  44 8D 42 FA                     lea r8d, [rdx - 6]
007E977C  E8 DF 7D 00 00                  call 0x1407f1560
007E9781  45 33 F6                        xor r14d, r14d
007E9784  66 45 39 77 42                  cmp word ptr [r15 + 0x42], r14w
007E9789  74 18                           je 0x1407e97a3
007E978B  4C 8D 4D F0                     lea r9, [rbp - 0x10]
007E978F  4C 89 74 24 20                  mov qword ptr [rsp + 0x20], r14
007E9794  45 33 C0                        xor r8d, r8d
007E9797  41 8D 56 08                     lea edx, [r14 + 8]
007E979B  49 8B CF                        mov rcx, r15
007E979E  E8 1D 17 00 00                  call 0x1407eaec0
007E97A3  41 0F B7 C6                     movzx eax, r14w
007E97A7  66 89 44 24 60                  mov word ptr [rsp + 0x60], ax
007E97AC  66 41 3B 47 42                  cmp ax, word ptr [r15 + 0x42]
007E97B1  0F 8D 29 01 00 00               jge 0x1407e98e0
007E97B7  0F B7 D0                        movzx edx, ax
007E97BA  48 8D 4D 48                     lea rcx, [rbp + 0x48]
007E97BE  E8 4D FA 15 00                  call 0x140949210
007E97C3  49 8B 4D 20                     mov rcx, qword ptr [r13 + 0x20]
007E97C7  4D 8B C5                        mov r8, r13
007E97CA  4C 8B 4D 90                     mov r9, qword ptr [rbp - 0x70]
007E97CE  8B D7                           mov edx, edi
007E97D0  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
007E97D5  E8 C6 3F 16 00                  call 0x14094d7a0
007E97DA  33 C9                           xor ecx, ecx
007E97DC  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
007E97E0  4C 8B F0                        mov r14, rax
007E97E3  48 85 C0                        test rax, rax
007E97E6  74 1A                           je 0x1407e9802
007E97E8  48 8B C8                        mov rcx, rax
007E97EB  E8 80 3B 07 00                  call 0x14085d370
007E97F0  48 8B 4D 98                     mov rcx, qword ptr [rbp - 0x68]
007E97F4  E8 67 61 1B 00                  call 0x14099f960
007E97F9  4C 89 75 98                     mov qword ptr [rbp - 0x68], r14
007E97FD  E9 D1 00 00 00                  jmp 0x1407e98d3
007E9802  4C 8B 74 24 78                  mov r14, qword ptr [rsp + 0x78]
007E9807  41 83 7E 28 FF                  cmp dword ptr [r14 + 0x28], -1
007E980C  74 68                           je 0x1407e9876
007E980E  41 B8 01 00 00 00               mov r8d, 1
007E9814  48 8D 55 C8                     lea rdx, [rbp - 0x38]
007E9818  49 8B CE                        mov rcx, r14
007E981B  E8 60 CC 06 00                  call 0x140856480
007E9820  4C 8B 45 90                     mov r8, qword ptr [rbp - 0x70]
007E9824  4C 8D 4D C0                     lea r9, [rbp - 0x40]
007E9828  49 8B 4E 20                     mov rcx, qword ptr [r14 + 0x20]
007E982C  48 8B D0                        mov rdx, rax
007E982F  E8 3C 8F 06 00                  call 0x140852770
007E9834  BA 01 00 00 00                  mov edx, 1
007E9839  44 8B F0                        mov r14d, eax
007E983C  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
007E9841  48 8B 48 20                     mov rcx, qword ptr [rax + 0x20]
007E9845  84 91 8C 00 00 00               test byte ptr [rcx + 0x8c], dl
007E984B  48 8D 55 C8                     lea rdx, [rbp - 0x38]
007E984F  74 07                           je 0x1407e9858
007E9851  E8 CA 33 07 00                  call 0x14085cc20
007E9856  EB 05                           jmp 0x1407e985d
007E9858  E8 E3 C6 06 00                  call 0x140855f40
007E985D  33 C9                           xor ecx, ecx
007E985F  41 81 FE 34 00 00 C0            cmp r14d, 0xc0000034
007E9866  74 0E                           je 0x1407e9876
007E9868  45 85 F6                        test r14d, r14d
007E986B  0F 88 A7 02 00 00               js 0x1407e9b18
007E9871  8B 55 C0                        mov edx, dword ptr [rbp - 0x40]
007E9874  EB 06                           jmp 0x1407e987c
007E9876  83 CA FF                        or edx, 0xffffffff
007E9879  89 55 C0                        mov dword ptr [rbp - 0x40], edx
007E987C  4C 8B 4D 98                     mov r9, qword ptr [rbp - 0x68]
007E9880  48 8D 45 E8                     lea rax, [rbp - 0x18]
007E9884  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
007E9889  48 8B 45 90                     mov rax, qword ptr [rbp - 0x70]
007E988D  89 7C 24 38                     mov dword ptr [rsp + 0x38], edi
007E9891  89 5C 24 30                     mov dword ptr [rsp + 0x30], ebx
007E9895  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
007E989A  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
007E989F  89 4C 24 20                     mov dword ptr [rsp + 0x20], ecx
007E98A3  4C 8B C0                        mov r8, rax
007E98A6  48 8B 48 20                     mov rcx, qword ptr [rax + 0x20]
007E98AA  E8 01 85 06 00                  call 0x140851db0
007E98AF  44 8B F0                        mov r14d, eax
007E98B2  85 C0                           test eax, eax
007E98B4  0F 88 5E 02 00 00               js 0x1407e9b18
007E98BA  48 8B 45 98                     mov rax, qword ptr [rbp - 0x68]
007E98BE  48 85 C0                        test rax, rax
007E98C1  74 08                           je 0x1407e98cb
007E98C3  48 8B C8                        mov rcx, rax
007E98C6  E8 95 60 1B 00                  call 0x14099f960
007E98CB  48 8B 45 E8                     mov rax, qword ptr [rbp - 0x18]
007E98CF  48 89 45 98                     mov qword ptr [rbp - 0x68], rax
007E98D3  0F B7 44 24 60                  movzx eax, word ptr [rsp + 0x60]
007E98D8  66 FF C0                        inc ax
007E98DB  E9 C7 FE FF FF                  jmp 0x1407e97a7
007E98E0  48 8B 45 98                     mov rax, qword ptr [rbp - 0x68]
007E98E4  33 DB                           xor ebx, ebx
007E98E6  48 85 C0                        test rax, rax
007E98E9  74 13                           je 0x1407e98fe
007E98EB  48 8B C8                        mov rcx, rax
007E98EE  E8 9D 32 07 00                  call 0x14085cb90
007E98F3  44 8B F0                        mov r14d, eax
007E98F6  85 C0                           test eax, eax
007E98F8  0F 88 1F 02 00 00               js 0x1407e9b1d
007E98FE  66 41 39 5F 42                  cmp word ptr [r15 + 0x42], bx
007E9903  74 31                           je 0x1407e9936
007E9905  45 33 C0                        xor r8d, r8d
007E9908  48 8D 4D 28                     lea rcx, [rbp + 0x28]
007E990C  41 8D 50 01                     lea edx, [r8 + 1]
007E9910  E8 73 AA 05 00                  call 0x140844388
007E9915  44 8B F0                        mov r14d, eax
007E9918  85 C0                           test eax, eax
007E991A  0F 88 FD 01 00 00               js 0x1407e9b1d
007E9920  33 D2                           xor edx, edx
007E9922  48 8D 4D 28                     lea rcx, [rbp + 0x28]
007E9926  E8 35 B4 15 00                  call 0x140944d60
007E992B  44 8B F0                        mov r14d, eax
007E992E  85 C0                           test eax, eax
007E9930  0F 88 E7 01 00 00               js 0x1407e9b1d
007E9936  41 8B 55 28                     mov edx, dword ptr [r13 + 0x28]
007E993A  45 33 C9                        xor r9d, r9d
007E993D  49 8B 4D 20                     mov rcx, qword ptr [r13 + 0x20]
007E9941  45 8D 41 01                     lea r8d, [r9 + 1]
007E9945  E8 36 E7 06 00                  call 0x140858080
007E994A  44 8B F0                        mov r14d, eax
007E994D  85 C0                           test eax, eax
007E994F  0F 88 C8 01 00 00               js 0x1407e9b1d
007E9955  41 B8 01 00 00 00               mov r8d, 1
007E995B  48 8D 55 00                     lea rdx, [rbp]
007E995F  49 8B CD                        mov rcx, r13
007E9962  E8 19 CB 06 00                  call 0x140856480
007E9967  48 89 45 D8                     mov qword ptr [rbp - 0x28], rax
007E996B  8B 50 1C                        mov edx, dword ptr [rax + 0x1c]
007E996E  83 FA FF                        cmp edx, -1
007E9971  74 18                           je 0x1407e998b
007E9973  49 8B 4D 20                     mov rcx, qword ptr [r13 + 0x20]
007E9977  E8 38 8B 2B 00                  call 0x140aa24b4
007E997C  44 8B F0                        mov r14d, eax
007E997F  85 C0                           test eax, eax
007E9981  0F 88 96 01 00 00               js 0x1407e9b1d
007E9987  48 8B 45 D8                     mov rax, qword ptr [rbp - 0x28]
007E998B  8B 50 20                        mov edx, dword ptr [rax + 0x20]
007E998E  83 FA FF                        cmp edx, -1
007E9991  74 14                           je 0x1407e99a7
007E9993  49 8B 4D 20                     mov rcx, qword ptr [r13 + 0x20]
007E9997  E8 18 8B 2B 00                  call 0x140aa24b4
007E999C  44 8B F0                        mov r14d, eax
007E999F  85 C0                           test eax, eax
007E99A1  0F 88 76 01 00 00               js 0x1407e9b1d
007E99A7  41 8B 57 28                     mov edx, dword ptr [r15 + 0x28]
007E99AB  45 33 C9                        xor r9d, r9d
007E99AE  49 8B 4F 20                     mov rcx, qword ptr [r15 + 0x20]
007E99B2  45 8D 41 01                     lea r8d, [r9 + 1]
007E99B6  E8 C5 E6 06 00                  call 0x140858080
007E99BB  44 8B F0                        mov r14d, eax
007E99BE  85 C0                           test eax, eax
007E99C0  0F 88 57 01 00 00               js 0x1407e9b1d
007E99C6  8B 45 80                        mov eax, dword ptr [rbp - 0x80]
007E99C9  83 F8 FF                        cmp eax, -1
007E99CC  74 1C                           je 0x1407e99ea
007E99CE  49 8B 4D 20                     mov rcx, qword ptr [r13 + 0x20]
007E99D2  41 B8 01 00 00 00               mov r8d, 1
007E99D8  8B D0                           mov edx, eax
007E99DA  E8 1D 18 06 00                  call 0x14084b1fc
007E99DF  44 8B F0                        mov r14d, eax
007E99E2  85 C0                           test eax, eax
007E99E4  0F 88 33 01 00 00               js 0x1407e9b1d
007E99EA  38 5C 24 52                     cmp byte ptr [rsp + 0x52], bl
007E99EE  0F 85 BD 00 00 00               jne 0x1407e9ab1
007E99F4  41 8B 57 28                     mov edx, dword ptr [r15 + 0x28]
007E99F8  49 8B 4F 20                     mov rcx, qword ptr [r15 + 0x20]
007E99FC  E8 1F 97 00 00                  call 0x1407f3120
007E9A01  44 8B F0                        mov r14d, eax
007E9A04  85 C0                           test eax, eax
007E9A06  0F 88 11 01 00 00               js 0x1407e9b1d
007E9A0C  48 8B 4D 90                     mov rcx, qword ptr [rbp - 0x70]
007E9A10  E8 AF 11 07 00                  call 0x14085abc4
007E9A15  45 8B 47 28                     mov r8d, dword ptr [r15 + 0x28]
007E9A19  4C 8D 4D 88                     lea r9, [rbp - 0x78]
007E9A1D  49 8B 4F 20                     mov rcx, qword ptr [r15 + 0x20]
007E9A21  0F B7 D0                        movzx edx, ax
007E9A24  48 8D 45 08                     lea rax, [rbp + 8]
007E9A28  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
007E9A2D  83 C2 4C                        add edx, 0x4c
007E9A30  48 8D 45 A8                     lea rax, [rbp - 0x58]
007E9A34  41 C1 E8 1F                     shr r8d, 0x1f
007E9A38  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
007E9A3D  E8 52 02 07 00                  call 0x140859c94
007E9A42  44 8B F0                        mov r14d, eax
007E9A45  85 C0                           test eax, eax
007E9A47  0F 88 D0 00 00 00               js 0x1407e9b1d
007E9A4D  BB 01 00 00 00                  mov ebx, 1
007E9A52  48 8D 55 D0                     lea rdx, [rbp - 0x30]
007E9A56  44 8A C3                        mov r8b, bl
007E9A59  49 8B CF                        mov rcx, r15
007E9A5C  E8 1F CA 06 00                  call 0x140856480
007E9A61  48 8B 4D A8                     mov rcx, qword ptr [rbp - 0x58]
007E9A65  48 8D 55 D0                     lea rdx, [rbp - 0x30]
007E9A69  0F 10 00                        movups xmm0, xmmword ptr [rax]
007E9A6C  0F 11 01                        movups xmmword ptr [rcx], xmm0
007E9A6F  0F 10 48 10                     movups xmm1, xmmword ptr [rax + 0x10]
007E9A73  0F 11 49 10                     movups xmmword ptr [rcx + 0x10], xmm1
007E9A77  0F 10 40 20                     movups xmm0, xmmword ptr [rax + 0x20]
007E9A7B  0F 11 41 20                     movups xmmword ptr [rcx + 0x20], xmm0
007E9A7F  0F 10 48 30                     movups xmm1, xmmword ptr [rax + 0x30]
007E9A83  0F 11 49 30                     movups xmmword ptr [rcx + 0x30], xmm1
007E9A87  F2 0F 10 40 40                  movsd xmm0, qword ptr [rax + 0x40]
007E9A8C  F2 0F 11 41 40                  movsd qword ptr [rcx + 0x40], xmm0
007E9A91  8B 40 48                        mov eax, dword ptr [rax + 0x48]
007E9A94  89 41 48                        mov dword ptr [rcx + 0x48], eax
007E9A97  49 8B 4F 20                     mov rcx, qword ptr [r15 + 0x20]
007E9A9B  84 99 8C 00 00 00               test byte ptr [rcx + 0x8c], bl
007E9AA1  0F 84 BA 00 00 00               je 0x1407e9b61
007E9AA7  E8 74 31 07 00                  call 0x14085cc20
007E9AAC  E9 B5 00 00 00                  jmp 0x1407e9b66
007E9AB1  48 8D 55 28                     lea rdx, [rbp + 0x28]
007E9AB5  48 8D 8D 90 00 00 00            lea rcx, [rbp + 0x90]
007E9ABC  E8 2B AB 15 00                  call 0x1409445ec
007E9AC1  44 8B F0                        mov r14d, eax
007E9AC4  85 C0                           test eax, eax
007E9AC6  78 55                           js 0x1407e9b1d
007E9AC8  48 8D 8D 90 00 00 00            lea rcx, [rbp + 0x90]
007E9ACF  E8 BC CA 15 00                  call 0x140946590
007E9AD4  3D 1A 00 00 80                  cmp eax, 0x8000001a
007E9AD9  0F 84 2D FF FF FF               je 0x1407e9a0c
007E9ADF  4C 8D 45 10                     lea r8, [rbp + 0x10]
007E9AE3  33 D2                           xor edx, edx
007E9AE5  48 8D 8D 90 00 00 00            lea rcx, [rbp + 0x90]
007E9AEC  E8 27 13 29 00                  call 0x140a7ae18
007E9AF1  41 0F B7 57 42                  movzx edx, word ptr [r15 + 0x42]
007E9AF6  48 8B 4D 10                     mov rcx, qword ptr [rbp + 0x10]
007E9AFA  E8 BD CF 15 00                  call 0x140946abc
007E9AFF  45 33 C9                        xor r9d, r9d
007E9B02  8B 50 08                        mov edx, dword ptr [rax + 8]
007E9B05  48 8B 08                        mov rcx, qword ptr [rax]
007E9B08  45 8D 41 01                     lea r8d, [r9 + 1]
007E9B0C  E8 6F E5 06 00                  call 0x140858080
007E9B11  44 8B F0                        mov r14d, eax
007E9B14  85 C0                           test eax, eax
007E9B16  79 B0                           jns 0x1407e9ac8
007E9B18  48 8B 5C 24 58                  mov rbx, qword ptr [rsp + 0x58]
007E9B1D  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
007E9B22  40 8A 74 24 50                  mov sil, byte ptr [rsp + 0x50]
007E9B27  48 8D 8D 90 00 00 00            lea rcx, [rbp + 0x90]
007E9B2E  E8 65 C2 15 00                  call 0x140945d98
007E9B33  48 83 7D D8 00                  cmp qword ptr [rbp - 0x28], 0
007E9B38  0F 84 45 05 00 00               je 0x1407ea083
007E9B3E  49 8B 4D 20                     mov rcx, qword ptr [r13 + 0x20]
007E9B42  BA 01 00 00 00                  mov edx, 1
007E9B47  84 91 8C 00 00 00               test byte ptr [rcx + 0x8c], dl
007E9B4D  48 8D 55 00                     lea rdx, [rbp]
007E9B51  0F 84 27 05 00 00               je 0x1407ea07e
007E9B57  E8 C4 30 07 00                  call 0x14085cc20
007E9B5C  E9 22 05 00 00                  jmp 0x1407ea083
007E9B61  E8 DA C3 06 00                  call 0x140855f40
007E9B66  48 8B 5D A8                     mov rbx, qword ptr [rbp - 0x58]
007E9B6A  4C 8B 75 90                     mov r14, qword ptr [rbp - 0x70]
007E9B6E  49 8B D6                        mov rdx, r14
007E9B71  48 8D 4B 4C                     lea rcx, [rbx + 0x4c]
007E9B75  E8 1E 14 07 00                  call 0x14085af98
007E9B7A  66 89 43 48                     mov word ptr [rbx + 0x48], ax
007E9B7E  66 41 3B 06                     cmp ax, word ptr [r14]
007E9B82  73 07                           jae 0x1407e9b8b
007E9B84  66 83 4B 02 20                  or word ptr [rbx + 2], 0x20
007E9B89  EB 0D                           jmp 0x1407e9b98
007E9B8B  48 8B 45 A8                     mov rax, qword ptr [rbp - 0x58]
007E9B8F  B9 DF FF 00 00                  mov ecx, 0xffdf
007E9B94  66 21 48 02                     and word ptr [rax + 2], cx
007E9B98  48 8B 5D A8                     mov rbx, qword ptr [rbp - 0x58]
007E9B9C  33 C0                           xor eax, eax
007E9B9E  48 89 73 04                     mov qword ptr [rbx + 4], rsi
007E9BA2  38 44 24 52                     cmp byte ptr [rsp + 0x52], al
007E9BA6  74 04                           je 0x1407e9bac
007E9BA8  80 4B 0D 03                     or byte ptr [rbx + 0xd], 3
007E9BAC  66 41 39 47 42                  cmp word ptr [r15 + 0x42], ax
007E9BB1  74 25                           je 0x1407e9bd8
007E9BB3  48 8B 5D A8                     mov rbx, qword ptr [rbp - 0x58]
007E9BB7  49 8B 4F 20                     mov rcx, qword ptr [r15 + 0x20]
007E9BBB  8B 53 2C                        mov edx, dword ptr [rbx + 0x2c]
007E9BBE  E8 DD 3A 00 00                  call 0x1407ed6a0
007E9BC3  44 8B F0                        mov r14d, eax
007E9BC6  85 C0                           test eax, eax
007E9BC8  0F 88 4A FF FF FF               js 0x1407e9b18
007E9BCE  8B 53 2C                        mov edx, dword ptr [rbx + 0x2c]
007E9BD1  4C 8B 75 90                     mov r14, qword ptr [rbp - 0x70]
007E9BD5  89 55 C4                        mov dword ptr [rbp - 0x3c], edx
007E9BD8  49 8B 4F 20                     mov rcx, qword ptr [r15 + 0x20]
007E9BDC  BA 01 00 00 00                  mov edx, 1
007E9BE1  84 91 8C 00 00 00               test byte ptr [rcx + 0x8c], dl
007E9BE7  48 8D 55 08                     lea rdx, [rbp + 8]
007E9BEB  74 07                           je 0x1407e9bf4
007E9BED  E8 2E 30 07 00                  call 0x14085cc20
007E9BF2  EB 05                           jmp 0x1407e9bf9
007E9BF4  E8 47 C3 06 00                  call 0x140855f40
007E9BF9  33 C0                           xor eax, eax
007E9BFB  48 8D 55 18                     lea rdx, [rbp + 0x18]
007E9BFF  49 8B CE                        mov rcx, r14
007E9C02  48 89 45 A8                     mov qword ptr [rbp - 0x58], rax
007E9C06  E8 45 0B 06 00                  call 0x14084a750
007E9C0B  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
007E9C10  48 8B D8                        mov rbx, rax
007E9C13  48 85 C0                        test rax, rax
007E9C16  75 0B                           jne 0x1407e9c23
007E9C18  41 BE 9A 00 00 C0               mov r14d, 0xc000009a
007E9C1E  E9 FA FE FF FF                  jmp 0x1407e9b1d
007E9C23  48 8B 5D D8                     mov rbx, qword ptr [rbp - 0x28]
007E9C27  8B 53 1C                        mov edx, dword ptr [rbx + 0x1c]
007E9C2A  83 FA FF                        cmp edx, -1
007E9C2D  74 1C                           je 0x1407e9c4b
007E9C2F  49 8B 4D 20                     mov rcx, qword ptr [r13 + 0x20]
007E9C33  4C 8D 4C 24 70                  lea r9, [rsp + 0x70]
007E9C38  45 33 C0                        xor r8d, r8d
007E9C3B  E8 80 84 05 00                  call 0x1408420c0
007E9C40  44 8B F0                        mov r14d, eax
007E9C43  85 C0                           test eax, eax
007E9C45  0F 88 CD FE FF FF               js 0x1407e9b18
007E9C4B  8B 53 20                        mov edx, dword ptr [rbx + 0x20]
007E9C4E  83 FA FF                        cmp edx, -1
007E9C51  74 1F                           je 0x1407e9c72
007E9C53  49 8B 4D 20                     mov rcx, qword ptr [r13 + 0x20]
007E9C57  4C 8D 4C 24 74                  lea r9, [rsp + 0x74]
007E9C5C  41 B8 01 00 00 00               mov r8d, 1
007E9C62  E8 59 84 05 00                  call 0x1408420c0
007E9C67  44 8B F0                        mov r14d, eax
007E9C6A  85 C0                           test eax, eax
007E9C6C  0F 88 A6 FE FF FF               js 0x1407e9b18
007E9C72  8B 4D 80                        mov ecx, dword ptr [rbp - 0x80]
007E9C75  83 F9 FF                        cmp ecx, -1
007E9C78  74 2A                           je 0x1407e9ca4
007E9C7A  8B C1                           mov eax, ecx
007E9C7C  48 8D 54 24 70                  lea rdx, [rsp + 0x70]
007E9C81  48 C1 E8 1F                     shr rax, 0x1f
007E9C85  44 8B C1                        mov r8d, ecx
007E9C88  49 8B 4D 20                     mov rcx, qword ptr [r13 + 0x20]
007E9C8C  48 8D 14 82                     lea rdx, [rdx + rax*4]
007E9C90  E8 9B 03 06 00                  call 0x14084a030
007E9C95  84 C0                           test al, al
007E9C97  75 0B                           jne 0x1407e9ca4
007E9C99  41 BE 7D 01 00 C0               mov r14d, 0xc000017d
007E9C9F  E9 74 FE FF FF                  jmp 0x1407e9b18
007E9CA4  8B 45 88                        mov eax, dword ptr [rbp - 0x78]
007E9CA7  48 8D 54 24 70                  lea rdx, [rsp + 0x70]
007E9CAC  49 8B 4D 20                     mov rcx, qword ptr [r13 + 0x20]
007E9CB0  8B D8                           mov ebx, eax
007E9CB2  48 C1 EB 1F                     shr rbx, 0x1f
007E9CB6  44 8B C0                        mov r8d, eax
007E9CB9  48 8D 14 9A                     lea rdx, [rdx + rbx*4]
007E9CBD  E8 82 39 06 00                  call 0x14084d644
007E9CC2  44 8B F0                        mov r14d, eax
007E9CC5  33 C0                           xor eax, eax
007E9CC7  45 85 F6                        test r14d, r14d
007E9CCA  0F 88 48 FE FF FF               js 0x1407e9b18
007E9CD0  66 41 39 47 42                  cmp word ptr [r15 + 0x42], ax
007E9CD5  75 21                           jne 0x1407e9cf8
007E9CD7  45 8B 47 28                     mov r8d, dword ptr [r15 + 0x28]
007E9CDB  48 8D 54 24 70                  lea rdx, [rsp + 0x70]
007E9CE0  49 8B 4D 20                     mov rcx, qword ptr [r13 + 0x20]
007E9CE4  41 8B C0                        mov eax, r8d
007E9CE7  48 C1 E8 1F                     shr rax, 0x1f
007E9CEB  48 8D 14 82                     lea rdx, [rdx + rax*4]
007E9CEF  E8 3C 03 06 00                  call 0x14084a030
007E9CF4  84 C0                           test al, al
007E9CF6  74 A1                           je 0x1407e9c99
007E9CF8  4C 8B 75 D8                     mov r14, qword ptr [rbp - 0x28]
007E9CFC  83 CA FF                        or edx, 0xffffffff
007E9CFF  8B 44 24 70                     mov eax, dword ptr [rsp + 0x70]
007E9D03  41 8B 4E 1C                     mov ecx, dword ptr [r14 + 0x1c]
007E9D07  41 89 46 1C                     mov dword ptr [r14 + 0x1c], eax
007E9D0B  8B 44 24 74                     mov eax, dword ptr [rsp + 0x74]
007E9D0F  89 4C 24 70                     mov dword ptr [rsp + 0x70], ecx
007E9D13  41 8B 4E 20                     mov ecx, dword ptr [r14 + 0x20]
007E9D17  41 89 46 20                     mov dword ptr [r14 + 0x20], eax
007E9D1B  8B 45 80                        mov eax, dword ptr [rbp - 0x80]
007E9D1E  89 4C 24 74                     mov dword ptr [rsp + 0x74], ecx
007E9D22  3B C2                           cmp eax, edx
007E9D24  74 09                           je 0x1407e9d2f
007E9D26  48 C1 E8 1F                     shr rax, 0x1f
007E9D2A  41 01 54 86 14                  add dword ptr [r14 + rax*4 + 0x14], edx
007E9D2F  B9 01 00 00 00                  mov ecx, 1
007E9D34  41 01 4C 9E 14                  add dword ptr [r14 + rbx*4 + 0x14], ecx
007E9D39  33 DB                           xor ebx, ebx
007E9D3B  66 41 39 5F 42                  cmp word ptr [r15 + 0x42], bx
007E9D40  75 0D                           jne 0x1407e9d4f
007E9D42  41 8B 47 28                     mov eax, dword ptr [r15 + 0x28]
007E9D46  48 C1 E8 1F                     shr rax, 0x1f
007E9D4A  41 01 54 86 14                  add dword ptr [r14 + rax*4 + 0x14], edx
007E9D4F  8A D1                           mov dl, cl
007E9D51  49 8B CD                        mov rcx, r13
007E9D54  E8 9B 29 06 00                  call 0x14084c6f4
007E9D59  48 8B 45 90                     mov rax, qword ptr [rbp - 0x70]
007E9D5D  0F B7 10                        movzx edx, word ptr [rax]
007E9D60  41 8B 46 34                     mov eax, dword ptr [r14 + 0x34]
007E9D64  0F B7 C8                        movzx ecx, ax
007E9D67  3B CA                           cmp ecx, edx
007E9D69  73 0D                           jae 0x1407e9d78
007E9D6B  66 41 89 56 34                  mov word ptr [r14 + 0x34], dx
007E9D70  66 41 89 95 B0 00 00 00         mov word ptr [r13 + 0xb0], dx
007E9D78  66 41 39 5F 42                  cmp word ptr [r15 + 0x42], bx
007E9D7D  75 0F                           jne 0x1407e9d8e
007E9D7F  41 8B 57 28                     mov edx, dword ptr [r15 + 0x28]
007E9D83  49 8B 4F 20                     mov rcx, qword ptr [r15 + 0x20]
007E9D87  E8 A0 09 07 00                  call 0x14085a72c
007E9D8C  EB 72                           jmp 0x1407e9e00
007E9D8E  41 B8 01 00 00 00               mov r8d, 1
007E9D94  48 8D 55 D0                     lea rdx, [rbp - 0x30]
007E9D98  49 8B CF                        mov rcx, r15
007E9D9B  E8 E0 C6 06 00                  call 0x140856480
007E9DA0  BA 01 00 00 00                  mov edx, 1
007E9DA5  8A 48 0D                        mov cl, byte ptr [rax + 0xd]
007E9DA8  66 83 60 02 20                  and word ptr [rax + 2], 0x20
007E9DAD  80 E1 7C                        and cl, 0x7c
007E9DB0  0A CA                           or cl, dl
007E9DB2  66 89 58 34                     mov word ptr [rax + 0x34], bx
007E9DB6  81 60 34 FF FF 00 FF            and dword ptr [rax + 0x34], 0xff00ffff
007E9DBD  88 48 0D                        mov byte ptr [rax + 0xd], cl
007E9DC0  83 C9 FF                        or ecx, 0xffffffff
007E9DC3  89 48 1C                        mov dword ptr [rax + 0x1c], ecx
007E9DC6  89 48 20                        mov dword ptr [rax + 0x20], ecx
007E9DC9  89 48 28                        mov dword ptr [rax + 0x28], ecx
007E9DCC  89 48 30                        mov dword ptr [rax + 0x30], ecx
007E9DCF  48 89 58 14                     mov qword ptr [rax + 0x14], rbx
007E9DD3  89 58 24                        mov dword ptr [rax + 0x24], ebx
007E9DD6  88 58 37                        mov byte ptr [rax + 0x37], bl
007E9DD9  48 89 58 38                     mov qword ptr [rax + 0x38], rbx
007E9DDD  89 58 40                        mov dword ptr [rax + 0x40], ebx
007E9DE0  66 89 58 4A                     mov word ptr [rax + 0x4a], bx
007E9DE4  49 8B 4F 20                     mov rcx, qword ptr [r15 + 0x20]
007E9DE8  84 91 8C 00 00 00               test byte ptr [rcx + 0x8c], dl
007E9DEE  48 8D 55 D0                     lea rdx, [rbp - 0x30]
007E9DF2  74 07                           je 0x1407e9dfb
007E9DF4  E8 27 2E 07 00                  call 0x14085cc20
007E9DF9  EB 05                           jmp 0x1407e9e00
007E9DFB  E8 40 C1 06 00                  call 0x140855f40
007E9E00  8B 45 88                        mov eax, dword ptr [rbp - 0x78]
007E9E03  41 89 47 28                     mov dword ptr [r15 + 0x28], eax
007E9E07  83 C8 FF                        or eax, 0xffffffff
007E9E0A  89 45 88                        mov dword ptr [rbp - 0x78], eax
007E9E0D  89 45 C4                        mov dword ptr [rbp - 0x3c], eax
007E9E10  66 41 39 5F 42                  cmp word ptr [r15 + 0x42], bx
007E9E15  74 5A                           je 0x1407e9e71
007E9E17  49 8B 87 C0 00 00 00            mov rax, qword ptr [r15 + 0xc0]
007E9E1E  48 8B 10                        mov rdx, qword ptr [rax]
007E9E21  48 39 42 08                     cmp qword ptr [rdx + 8], rax
007E9E25  0F 85 40 01 00 00               jne 0x1407e9f6b
007E9E2B  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
007E9E2F  48 39 01                        cmp qword ptr [rcx], rax
007E9E32  0F 85 33 01 00 00               jne 0x1407e9f6b
007E9E38  48 89 11                        mov qword ptr [rcx], rdx
007E9E3B  45 33 C0                        xor r8d, r8d
007E9E3E  48 89 4A 08                     mov qword ptr [rdx + 8], rcx
007E9E42  48 8D 55 F0                     lea rdx, [rbp - 0x10]
007E9E46  49 8B 87 C0 00 00 00            mov rax, qword ptr [r15 + 0xc0]
007E9E4D  48 8B 48 18                     mov rcx, qword ptr [rax + 0x18]
007E9E51  48 8B 49 10                     mov rcx, qword ptr [rcx + 0x10]
007E9E55  E8 06 8D 07 00                  call 0x140862b60
007E9E5A  49 8B 87 C0 00 00 00            mov rax, qword ptr [r15 + 0xc0]
007E9E61  49 8B D7                        mov rdx, r15
007E9E64  48 8B 4D 98                     mov rcx, qword ptr [rbp - 0x68]
007E9E68  48 89 58 18                     mov qword ptr [rax + 0x18], rbx
007E9E6C  E8 8F 2C 07 00                  call 0x14085cb00
007E9E71  49 8B 4F 20                     mov rcx, qword ptr [r15 + 0x20]
007E9E75  49 8D 5F 10                     lea rbx, [r15 + 0x10]
007E9E79  48 8B D3                        mov rdx, rbx
007E9E7C  E8 57 93 1C 00                  call 0x1409b31d8
007E9E81  49 8B 4F 20                     mov rcx, qword ptr [r15 + 0x20]
007E9E85  48 8B D3                        mov rdx, rbx
007E9E88  89 3B                           mov dword ptr [rbx], edi
007E9E8A  E8 D9 0F 00 00                  call 0x1407eae68
007E9E8F  49 8B 47 50                     mov rax, qword ptr [r15 + 0x50]
007E9E93  33 FF                           xor edi, edi
007E9E95  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
007E9E9A  49 89 57 50                     mov qword ptr [r15 + 0x50], rdx
007E9E9E  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
007E9EA3  49 8B 87 28 01 00 00            mov rax, qword ptr [r15 + 0x128]
007E9EAA  48 85 C0                        test rax, rax
007E9EAD  74 0B                           je 0x1407e9eba
007E9EAF  8D 47 01                        lea eax, [rdi + 1]
007E9EB2  F0 49 09 87 28 01 00 00         lock or qword ptr [r15 + 0x128], rax
007E9EBA  49 8B 8F C8 00 00 00            mov rcx, qword ptr [r15 + 0xc8]
007E9EC1  48 83 F9 02                     cmp rcx, 2
007E9EC5  72 0A                           jb 0x1407e9ed1
007E9EC7  BA 43 4D 4E 62                  mov edx, 0x624e4d43
007E9ECC  E8 9F 89 39 00                  call 0x140b82870
007E9ED1  8A 5C 24 52                     mov bl, byte ptr [rsp + 0x52]
007E9ED5  49 89 BF C8 00 00 00            mov qword ptr [r15 + 0xc8], rdi
007E9EDC  84 DB                           test bl, bl
007E9EDE  74 05                           je 0x1407e9ee5
007E9EE0  41 C6 47 41 03                  mov byte ptr [r15 + 0x41], 3
007E9EE5  41 8B 57 28                     mov edx, dword ptr [r15 + 0x28]
007E9EE9  49 8B 4F 20                     mov rcx, qword ptr [r15 + 0x20]
007E9EED  E8 C6 96 00 00                  call 0x1407f35b8
007E9EF2  84 DB                           test bl, bl
007E9EF4  0F 84 B0 00 00 00               je 0x1407e9faa
007E9EFA  48 8B DF                        mov rbx, rdi
007E9EFD  41 BE 01 00 00 00               mov r14d, 1
007E9F03  BF 00 02 00 00                  mov edi, 0x200
007E9F08  48 8B 8D F0 00 00 00            mov rcx, qword ptr [rbp + 0xf0]
007E9F0F  48 83 C1 38                     add rcx, 0x38
007E9F13  48 03 CB                        add rcx, rbx
007E9F16  E8 71 C5 15 00                  call 0x14094648c
007E9F1B  48 81 C3 98 01 00 00            add rbx, 0x198
007E9F22  49 2B FE                        sub rdi, r14
007E9F25  75 E1                           jne 0x1407e9f08
007E9F27  8D 47 FE                        lea eax, [rdi - 2]
007E9F2A  48 89 BD 98 00 00 00            mov qword ptr [rbp + 0x98], rdi
007E9F31  48 8D 8D A0 00 00 00            lea rcx, [rbp + 0xa0]
007E9F38  66 89 85 90 00 00 00            mov word ptr [rbp + 0x90], ax
007E9F3F  E8 D0 BE 15 00                  call 0x140945e14
007E9F44  48 8D 55 28                     lea rdx, [rbp + 0x28]
007E9F48  48 8D 8D 90 00 00 00            lea rcx, [rbp + 0x90]
007E9F4F  E8 88 79 00 00                  call 0x1407f18dc
007E9F54  48 8D 8D 90 00 00 00            lea rcx, [rbp + 0x90]
007E9F5B  E8 30 C6 15 00                  call 0x140946590
007E9F60  4C 8B 75 D8                     mov r14, qword ptr [rbp - 0x28]
007E9F64  BB 1A 00 00 80                  mov ebx, 0x8000001a
007E9F69  EB 3B                           jmp 0x1407e9fa6
007E9F6B  B9 03 00 00 00                  mov ecx, 3
007E9F70  CD 29                           int 0x29
007E9F72  4C 8D 45 10                     lea r8, [rbp + 0x10]
007E9F76  33 D2                           xor edx, edx
007E9F78  48 8D 8D 90 00 00 00            lea rcx, [rbp + 0x90]
007E9F7F  E8 94 0E 29 00                  call 0x140a7ae18
007E9F84  41 0F B7 57 42                  movzx edx, word ptr [r15 + 0x42]
007E9F89  48 8B 4D 10                     mov rcx, qword ptr [rbp + 0x10]
007E9F8D  E8 2A CB 15 00                  call 0x140946abc
007E9F92  48 8B 48 10                     mov rcx, qword ptr [rax + 0x10]
007E9F96  80 49 0D 03                     or byte ptr [rcx + 0xd], 3
007E9F9A  48 8D 8D 90 00 00 00            lea rcx, [rbp + 0x90]
007E9FA1  E8 EA C5 15 00                  call 0x140946590
007E9FA6  3B C3                           cmp eax, ebx
007E9FA8  75 C8                           jne 0x1407e9f72
007E9FAA  49 89 76 04                     mov qword ptr [r14 + 4], rsi
007E9FAE  48 8D 55 00                     lea rdx, [rbp]
007E9FB2  49 8B 4D 20                     mov rcx, qword ptr [r13 + 0x20]
007E9FB6  BB 01 00 00 00                  mov ebx, 1
007E9FBB  49 89 B5 A8 00 00 00            mov qword ptr [r13 + 0xa8], rsi
007E9FC2  84 99 8C 00 00 00               test byte ptr [rcx + 0x8c], bl
007E9FC8  74 07                           je 0x1407e9fd1
007E9FCA  E8 51 2C 07 00                  call 0x14085cc20
007E9FCF  EB 05                           jmp 0x1407e9fd6
007E9FD1  E8 6A BF 06 00                  call 0x140855f40
007E9FD6  45 33 C0                        xor r8d, r8d
007E9FD9  48 89 7D D8                     mov qword ptr [rbp - 0x28], rdi
007E9FDD  8B D3                           mov edx, ebx
007E9FDF  49 8B CF                        mov rcx, r15
007E9FE2  E8 85 47 1C 00                  call 0x1409ae76c
007E9FE7  49 01 9D 30 01 00 00            add qword ptr [r13 + 0x130], rbx
007E9FEE  49 01 9F 30 01 00 00            add qword ptr [r15 + 0x130], rbx
007E9FF5  8B 55 84                        mov edx, dword ptr [rbp - 0x7c]
007E9FF8  83 FA FF                        cmp edx, -1
007E9FFB  74 0C                           je 0x1407ea009
007E9FFD  49 8B 4D 20                     mov rcx, qword ptr [r13 + 0x20]
007EA001  45 33 C0                        xor r8d, r8d
007EA004  E8 67 0D 06 00                  call 0x14084ad70
007EA009  44 8B F7                        mov r14d, edi
007EA00C  E9 07 FB FF FF                  jmp 0x1407e9b18
007EA011  48 8B 5C 24 58                  mov rbx, qword ptr [rsp + 0x58]
007EA016  41 BE 21 01 00 C0               mov r14d, 0xc0000121
007EA01C  48 8B F9                        mov rdi, rcx
007EA01F  40 8A F2                        mov sil, dl
007EA022  E9 00 FB FF FF                  jmp 0x1407e9b27
007EA027  4C 8B E7                        mov r12, rdi
007EA02A  48 8B DF                        mov rbx, rdi
007EA02D  E9 EB FA FF FF                  jmp 0x1407e9b1d
007EA032  48 8B 5C 24 58                  mov rbx, qword ptr [rsp + 0x58]
007EA037  4C 8B E7                        mov r12, rdi
007EA03A  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
007EA03F  E9 E3 FA FF FF                  jmp 0x1407e9b27
007EA044  B9 18 00 00 00                  mov ecx, 0x18
007EA049  E8 F2 49 1C 00                  call 0x1409aea40
007EA04E  33 C0                           xor eax, eax
007EA050  41 BE 02 00 00 C0               mov r14d, 0xc0000002
007EA056  E9 86 F6 FF FF                  jmp 0x1407e96e1
007EA05B  41 BE 22 00 00 C0               mov r14d, 0xc0000022
007EA061  4C 8B E2                        mov r12, rdx
007EA064  E9 75 F3 FF FF                  jmp 0x1407e93de
007EA069  33 C0                           xor eax, eax
007EA06B  41 BE 89 01 00 C0               mov r14d, 0xc0000189
007EA071  40 8A F0                        mov sil, al
007EA074  44 8B E0                        mov r12d, eax
007EA077  8B D8                           mov ebx, eax
007EA079  E9 A9 FA FF FF                  jmp 0x1407e9b27
007EA07E  E8 BD BE 06 00                  call 0x140855f40
007EA083  4D 85 E4                        test r12, r12
007EA086  41 BC 01 00 00 00               mov r12d, 1
007EA08C  74 1C                           je 0x1407ea0aa
007EA08E  48 8D 55 E0                     lea rdx, [rbp - 0x20]
007EA092  48 8B CF                        mov rcx, rdi
007EA095  44 84 A7 8C 00 00 00            test byte ptr [rdi + 0x8c], r12b
007EA09C  74 07                           je 0x1407ea0a5
007EA09E  E8 7D 2B 07 00                  call 0x14085cc20
007EA0A3  EB 05                           jmp 0x1407ea0aa
007EA0A5  E8 96 BE 06 00                  call 0x140855f40
007EA0AA  8B 45 C4                        mov eax, dword ptr [rbp - 0x3c]
007EA0AD  83 F8 FF                        cmp eax, -1
007EA0B0  74 0B                           je 0x1407ea0bd
007EA0B2  49 8B 4F 20                     mov rcx, qword ptr [r15 + 0x20]
007EA0B6  8B D0                           mov edx, eax
007EA0B8  E8 6F C6 CB FF                  call 0x1404a672c
007EA0BD  33 FF                           xor edi, edi
007EA0BF  48 39 7D A8                     cmp qword ptr [rbp - 0x58], rdi
007EA0C3  74 1D                           je 0x1407ea0e2
007EA0C5  49 8B 4F 20                     mov rcx, qword ptr [r15 + 0x20]
007EA0C9  48 8D 55 08                     lea rdx, [rbp + 8]
007EA0CD  44 84 A1 8C 00 00 00            test byte ptr [rcx + 0x8c], r12b
007EA0D4  74 07                           je 0x1407ea0dd
007EA0D6  E8 45 2B 07 00                  call 0x14085cc20
007EA0DB  EB 05                           jmp 0x1407ea0e2
007EA0DD  E8 5E BE 06 00                  call 0x140855f40
007EA0E2  8B 54 24 70                     mov edx, dword ptr [rsp + 0x70]
007EA0E6  41 83 CC FF                     or r12d, 0xffffffff
007EA0EA  41 3B D4                        cmp edx, r12d
007EA0ED  74 09                           je 0x1407ea0f8
007EA0EF  49 8B 4D 20                     mov rcx, qword ptr [r13 + 0x20]
007EA0F3  E8 14 CE 2B 00                  call 0x140aa6f0c
007EA0F8  8B 54 24 74                     mov edx, dword ptr [rsp + 0x74]
007EA0FC  41 3B D4                        cmp edx, r12d
007EA0FF  74 09                           je 0x1407ea10a
007EA101  49 8B 4D 20                     mov rcx, qword ptr [r13 + 0x20]
007EA105  E8 02 CE 2B 00                  call 0x140aa6f0c
007EA10A  8B 45 88                        mov eax, dword ptr [rbp - 0x78]
007EA10D  41 3B C4                        cmp eax, r12d
007EA110  74 0B                           je 0x1407ea11d
007EA112  49 8B 4F 20                     mov rcx, qword ptr [r15 + 0x20]
007EA116  8B D0                           mov edx, eax
007EA118  E8 0F 06 07 00                  call 0x14085a72c
007EA11D  48 85 DB                        test rbx, rbx
007EA120  74 08                           je 0x1407ea12a
007EA122  48 8B CB                        mov rcx, rbx
007EA125  E8 16 87 07 00                  call 0x140862840
007EA12A  48 8B 45 98                     mov rax, qword ptr [rbp - 0x68]
007EA12E  48 85 C0                        test rax, rax
007EA131  74 0F                           je 0x1407ea142
007EA133  45 33 C0                        xor r8d, r8d
007EA136  48 8D 55 F0                     lea rdx, [rbp - 0x10]
007EA13A  48 8B C8                        mov rcx, rax
007EA13D  E8 1E 8A 07 00                  call 0x140862b60
007EA142  48 8B 45 A0                     mov rax, qword ptr [rbp - 0x60]
007EA146  48 85 C0                        test rax, rax
007EA149  74 0F                           je 0x1407ea15a
007EA14B  45 33 C0                        xor r8d, r8d
007EA14E  48 8D 55 F0                     lea rdx, [rbp - 0x10]
007EA152  48 8B C8                        mov rcx, rax
007EA155  E8 06 8A 07 00                  call 0x140862b60
007EA15A  33 D2                           xor edx, edx
007EA15C  48 8D 4D F0                     lea rcx, [rbp - 0x10]
007EA160  E8 3B 18 C3 FF                  call 0x14041b9a0
007EA165  40 84 F6                        test sil, sil
007EA168  74 05                           je 0x1407ea16f
007EA16A  E8 15 F9 3D 00                  call 0x140bc9a84
007EA16F  48 8D 4D 28                     lea rcx, [rbp + 0x28]
007EA173  E8 28 CF 15 00                  call 0x1409470a0
007EA178  48 8D 4D 48                     lea rcx, [rbp + 0x48]
007EA17C  E8 1F CF 15 00                  call 0x1409470a0
007EA181  48 8D 4D 68                     lea rcx, [rbp + 0x68]
007EA185  E8 16 CF 15 00                  call 0x1409470a0
007EA18A  48 8D 4D B0                     lea rcx, [rbp - 0x50]
007EA18E  E8 B9 5F 1C 00                  call 0x1409b014c
007EA193  41 8B C6                        mov eax, r14d
007EA196  48 8B 8D 00 01 00 00            mov rcx, qword ptr [rbp + 0x100]
007EA19D  48 33 CC                        xor rcx, rsp
007EA1A0  E8 9B 24 EC FF                  call 0x1406ac640
007EA1A5  48 8B 9C 24 60 02 00 00         mov rbx, qword ptr [rsp + 0x260]
007EA1AD  48 81 C4 10 02 00 00            add rsp, 0x210
007EA1B4  41 5F                           pop r15
007EA1B6  41 5E                           pop r14
007EA1B8  41 5D                           pop r13
007EA1BA  41 5C                           pop r12
007EA1BC  5F                              pop rdi
007EA1BD  5E                              pop rsi
007EA1BE  5D                              pop rbp
007EA1BF  C3                              ret
007EA1C0  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmRenameKey(__int64 a1, __int64 a2, unsigned __int8 a3)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m110;
    unsigned __int16 v_stack_m11E;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned int v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m160;
    unsigned __int64 v_stack_m168;
    unsigned __int64 v_stack_m170;
    unsigned __int64 v_stack_m178;
    unsigned __int64 v_stack_m180;
    unsigned int v_stack_m184;
    unsigned int v_stack_m188;
    unsigned __int64 v_stack_m198;
    unsigned __int64 v_stack_m1A0;
    unsigned __int64 v_stack_m1A8;
    unsigned __int64 v_stack_m1B0;
    unsigned __int64 v_stack_m1B8;
    unsigned int v_stack_m1C0;
    unsigned int v_stack_m1C4;
    unsigned int v_stack_m1C8;
    unsigned __int64 v_stack_m1D0;
    unsigned int v_stack_m1D4;
    unsigned int v_stack_m1D8;
    unsigned __int64 v_stack_m1E0;
    unsigned __int8 v_stack_m1E8;
    unsigned __int64 v_stack_m1F0;
    unsigned __int8 v_stack_m1F4;
    unsigned __int8 v_stack_m1F6;
    unsigned __int8 v_stack_m1F8;
    unsigned __int64 v_stack_m208;
    unsigned int v_stack_m210;
    unsigned int v_stack_m218;
    unsigned int v_stack_m220;
    unsigned __int8 v_stack_m228;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mD0;
    unsigned __int16 v_stack_mDE;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mF0;
    unsigned __int16 v_stack_mFE;
    unsigned __int64 v_stack_p18;

    v_stack_p18 = v_rbx;
    v_rsp = (v_rsp) - (528);
    result = (*(unsigned __int64 *)(v_rip + 6428626)) ^ (v_rsp);
    v_stack_m48 = result;
    v_r14 = 0;
    v_stack_m1B8 = a2;
    v_stack_m160 = a1;
    v_stack_m1E8 = a3;
    v_stack_m128 = 0;
    v_stack_m168 = 0;
    a2 = 0;
    v_stack_m180 = 0;
    v_stack_m140 = 0;
    v_stack_m158 = v_xmm0;
    v_stack_m178 = 0;
    v_stack_m188 = 0;
    v_stack_m148 = 0;
    result = memset(v_stack_mB8, a2, v_r14 + 104, a4);
    v_stack_m138 = 0;
    result = (unsigned int)((result) | (0xFFFFFFFFULL));
    v_stack_m1A8 = 0;
    v_stack_m1B0 = 0;
    v_stack_m120 = v_xmm1;
    v_stack_m11E = (unsigned __int16)(result);
    v_stack_m100 = v_xmm0;
    v_stack_mFE = (unsigned __int16)(result);
    v_stack_mE0 = v_xmm0;
    v_stack_mDE = (unsigned __int16)(result);
    v_stack_m198 = v_xmm0;
    v_stack_m1E0 = 0;
    v_stack_m110 = v_xmm1;
    v_stack_mF0 = v_xmm0;
    v_stack_mD0 = v_xmm0;
    result = HvpGetCellContextInitialize(v_stack_m168, a2, v_r14 + 104, a4);
    result = HvpGetCellContextInitialize(v_stack_m180, a2, v_r14 + 104, a4);
    a3 = (unsigned int)((v_r14 + 104) | (0xFFFFFFFFULL));
    v_stack_m1A0 = 0;
    v_stack_m1C0 = a3;
    result = HvpGetCellContextInitialize(v_stack_m140, a2, a3, a4);
    result = HvpGetCellContextInitialize(v_stack_m178, a2, a3, a4);
    v_stack_m184 = a3;
    v_stack_m170 = 0;
    result = HvpGetCellContextInitialize(v_stack_m148, a2, a3, a4);
    v_stack_m1F0 = 0;
    v_stack_m1D8 = a3;
    v_stack_m1D4 = a3;
    v_stack_m1F6 = 0;
    result = CmpSubtreeEnumeratorInitialize(v_stack_mB8, a2, a3, a4);
    result = CmpInitializeDelayDerefContext(v_stack_m158, a2, a3, a4);
loc_007E9077:
    v_stack_m1D0 = 0;
    result = CmpIsShutdownRundownActive(v_stack_m158, a2, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_007EA069;
    result = CmpLockRegistryExclusive(v_stack_m158, a2, a3, a4);
    v_stack_m1F8 = 1;
    result = CmpStartKcbStackForTopLayerKcb(v_stack_m120, *(unsigned __int64 *)(a1 + 8), a3, a4);
    result = 0;
    if (sign_flag) goto loc_007E96E1;
    result = CmpStartKcbStackForTopLayerKcb(v_stack_m100, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 72), a3, a4);
    a2 = 0;
    if (sign_flag) goto loc_007EA061;
    if (((*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 8)) & (384)) != 0) goto loc_007EA05B;
    if (((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 160)) & (0x100000ULL)) != 0) goto loc_007EA05B;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32)) == (*(unsigned __int64 *)(v_rip + 8325515))) goto loc_007EA05B;
    if (((*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 184)) & (0x40000ULL)) != 0) goto loc_007EA05B;
    result = CmpPerformKeyBodyDeletionCheck(a1, a2, a3, a4);
    result = 0;
    if (sign_flag) goto loc_007E96E1;
    if ((*(unsigned __int64 *)(a1 + 56)) != 0) goto loc_007E9146;
    if ((*(unsigned __int64 *)(a1 + 64)) != 0) goto loc_007E9146;
    v_stack_m128 = 0;
    goto loc_007E918A;
loc_007E9146:
    result = CmpTransSearchAddTransFromKeyBody(a1, v_stack_m128, a3, a4);
    result = 0;
    if (sign_flag) goto loc_007E96E1;
    result = CmpPerformKeyBodyDeletionCheck(a1, v_stack_m128, a3, a4);
    result = 0;
    if (sign_flag) goto loc_007E96E1;
    if (v_stack_m128 != 0) goto loc_007EA044;
loc_007E918A:
    v_stack_m228 = 0;
    a2 = 0;
    result = CmpCheckKcbStackAccess(v_stack_m100, a2, (unsigned __int8)(v_stack_m1E8), 4);
    result = 0;
    if (sign_flag) goto loc_007E96E1;
    result = (unsigned __int16)(-(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 66)));
    v_stack_m220 = 1;
    a3 = 0;
    a1 = (unsigned int)((v_stack_m100) & (0x20019ULL));
    a1 = (unsigned int)((a1) + (0x10000ULL));
    v_stack_m228 = (unsigned int)(a1);
    result = CmpDoAccessCheckOnLayeredSubtree(v_stack_m120, a2, a3, (unsigned __int8)(v_stack_m1E8));
    result = 0;
    if (sign_flag) goto loc_007E96E1;
    a2 = 0;
    result = CmpFlushNotifiesOnKeyBodyList(*(unsigned __int64 *)(a1 + 8), a2, v_stack_m158, (unsigned __int8)(result + 1));
    a4 = 0;
    result = CmpReportNotify(*(unsigned __int64 *)(a1 + 8), a2, (unsigned int)((unsigned int)(result + 1)), a4);
    result = CmpTryAcquireKcbIXLocks(*(unsigned __int64 *)(a1 + 8), (unsigned __int8)(result + 1), (unsigned int)((unsigned int)(result + 1)), v_stack_m198);
    if ((((unsigned int)((unsigned int)(0x80000000ULL))) & ((unsigned int)((unsigned int)((unsigned int)(result)) + (unsigned int)(0x80000000ULL) * 1))) != 0) goto loc_007E923C;
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != 0xC000022DULL) goto loc_007E96CF;
loc_007E923C:
    result = CmpTryAcquireKcbIXLocks(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 72), 1, (unsigned int)((unsigned int)(result + 1)), v_stack_m198);
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == ((unsigned int)((unsigned int)(0xC000022DULL)))) goto loc_007E965F;
    v_rdi = 0;
    if (sign_flag) goto loc_007EA027;
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == ((unsigned int)((unsigned int)(0xC000022DULL)))) goto loc_007E9661;
    result = CmpHashUnicodeComponent(v_stack_m1B8, 1, (unsigned int)((unsigned int)(result + 1)), v_stack_m198);
    v_rdi = (unsigned int)((v_rdi) * (*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 72) + 16)));
    v_stack_m130 = (unsigned int)(result);
    v_rdi = (unsigned int)((v_rdi) + ((unsigned int)(result)));
    result = CmpFindKcbInHashEntryByName(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 72) + 32), (unsigned int)((unsigned int)(v_rdi)), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 72), v_stack_m1B8);
    v_r11 = 0;
    v_stack_m1A8 = result;
    if (result == 0) goto loc_007E93E6;
    result = CmpReferenceKeyControlBlock(result, (unsigned int)((unsigned int)(v_rdi)), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 72), v_stack_m1B8);
    v_stack_m1C8 = (unsigned int)((unsigned int)(*(unsigned int *)(result + 40)));
    v_stack_m1C4 = (unsigned int)((unsigned int)(*(unsigned int *)(result + 40)));
    result = CmpStartKcbStackForTopLayerKcb(v_stack_mE0, result, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 72), v_stack_m1B8);
    result = 0;
    if (sign_flag) goto loc_007E96D1;
    a2 = 0;
    result = CmpIsKeyStackDeleted(v_stack_mE0, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 72), v_stack_m1B8);
    a1 = 0;
    if ((unsigned __int8)(result) == 0) goto loc_007E96EC;
loc_007E92FF:
    if (sign_flag) goto loc_007E9331;
    result = CmpGetKcbAtLayerHeight(v_stack_mE0, (unsigned __int16)(*(unsigned __int16 *)(v_stack_m1A8 + 66)), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 72), *(unsigned __int16 *)(v_stack_m1A8 + 66));
    result = CmpGetEffectiveKcbSemantics(result, 0, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 72), *(unsigned __int16 *)(v_stack_m1A8 + 66));
    if (((unsigned int)(result)) == 1) goto loc_007E932C;
    a4 = (unsigned __int16)((*(unsigned __int16 *)(v_stack_m1A8 + 66)) - 1);
    goto loc_007E92FF;
loc_007E932C:
    goto loc_007E9336;
loc_007E9331:
loc_007E9336:
    v_stack_m1F6 = (unsigned __int8)(v_stack_m1F6);
    result = CmpTryAcquireKcbIXLocks(v_stack_m1A8, 1, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 72), v_stack_m198);
    if (((unsigned int)(result)) != 0xC000022DULL) goto loc_007E9358;
    v_stack_m1F4 = 1;
    goto loc_007E9363;
loc_007E9358:
    result = 0;
    if (sign_flag) goto loc_007E96DC;
loc_007E9363:
    result = CmpPrepareToInvalidateAllHigherLayerKcbs(v_stack_m1A8, 2, v_stack_m198, v_stack_m198);
    if (((unsigned int)(result)) != 0xC000022DULL) goto loc_007E9386;
    v_stack_m1F4 = 1;
    goto loc_007E9391;
loc_007E9386:
    result = 0;
    if (sign_flag) goto loc_007E96DC;
loc_007E9391:
    a2 = 0;
    result = CmpPrepareForSubtreeInvalidation(v_stack_m1A8, a2, v_stack_m198, v_stack_m198);
    if (((unsigned int)(result)) != 0xC000022DULL) goto loc_007E93BE;
    result = 0;
    v_stack_m1F4 = 1;
    goto loc_007E9576;
loc_007E93BE:
    a2 = 0;
    v_stack_m1F6 = 0;
    v_stack_m1E0 = v_stack_m1D0;
    if (!sign_flag) goto loc_007E957B;
loc_007E93DE:
    goto loc_007E9B22;
loc_007E93E6:
    result = (unsigned int)((v_stack_m1D0) | (0xFFFFFFFFULL));
    v_stack_m1F6 = (unsigned __int16)(result);
    v_stack_m1E0 = 0;
loc_007E9400:
    if (sign_flag) goto loc_007E94DF;
    result = CmpGetKcbAtLayerHeight(v_stack_m100, (unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 72) + 66)), v_stack_m198, v_stack_m160);
    v_stack_m1D0 = result;
    result = CmpGetEffectiveKcbSemantics(result, v_stack_m160, v_stack_m198, v_stack_m160);
    if (((unsigned int)(result)) == 1) goto loc_007E94D2;
    if ((*(unsigned int *)(result + 40)) == -1) goto loc_007E94B5;
    result = CmpGetKeyNodeForKcb(result, v_stack_m180, 1, v_stack_m160);
    result = CmpFindSubKeyByNameWithStatus(*(unsigned __int64 *)(result + 32), result, v_stack_m1B8, v_stack_m1C4);
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m1D0 + 32) + 140)) & (1)) == 0) goto loc_007E9485;
    result = HvpReleaseCellFlat(*(unsigned __int64 *)(v_stack_m1D0 + 32), v_stack_m180, v_stack_m1B8, v_stack_m1C4);
    goto loc_007E948A;
loc_007E9485:
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(v_stack_m1D0 + 32), v_stack_m180, v_stack_m1B8, v_stack_m1C4);
loc_007E948A:
    v_r11 = 0;
    if (!sign_flag) goto loc_007E94BE;
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != 0xC0000034ULL) goto loc_007E96FD;
    result = CmpGetEffectiveKcbSemantics(v_stack_m1D0, v_stack_m160, v_stack_m1B8, v_stack_m1C4);
    if ((unsigned int)(result) != 0) goto loc_007E94E6;
loc_007E94B5:
    v_r12 = (unsigned __int16)((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 72) + 66)) - 1);
    goto loc_007E9400;
loc_007E94BE:
    v_stack_m1E0 = *(unsigned __int64 *)(v_stack_m1D0 + 32);
    goto loc_007E94EF;
loc_007E94D2:
    goto loc_007E94F4;
loc_007E94DF:
    goto loc_007E94E9;
loc_007E94E6:
loc_007E94E9:
loc_007E94EF:
loc_007E94F4:
    v_stack_m1C8 = (unsigned int)((unsigned int)(v_stack_m1C4));
    if (((unsigned int)((unsigned int)(v_stack_m1C4))) != -1) goto loc_007E9509;
    v_stack_m1F6 = 0;
    goto loc_007E957B;
loc_007E9509:
    if (((*(unsigned __int8 *)(0 + 140)) & (1)) == 0) goto loc_007E9522;
    result = HvpGetCellFlat(0, (unsigned int)((unsigned int)((unsigned int)(v_stack_m1C4))), v_stack_m168, v_stack_m160);
    goto loc_007E9527;
loc_007E9522:
    result = HvpGetCellPaged(0, (unsigned int)((unsigned int)((unsigned int)(v_stack_m1C4))), v_stack_m168, v_stack_m160);
loc_007E9527:
    result = CmpGetEffectiveKeyNodeSemantics(v_stack_m1E0, result, v_stack_m168, v_stack_m160);
    if (((unsigned int)(result)) != 1) goto loc_007EA011;
    if (((*(unsigned __int8 *)(v_stack_m1E0 + 140)) & (1)) == 0) goto loc_007E9557;
    result = HvpReleaseCellFlat(v_stack_m1E0, v_stack_m168, v_stack_m168, v_stack_m160);
    goto loc_007E955C;
loc_007E9557:
    result = HvpReleaseCellPaged(v_stack_m1E0, v_stack_m168, v_stack_m168, v_stack_m160);
loc_007E955C:
    a1 = 0;
    v_stack_m1F6 = 1;
    if (((unsigned __int16)(v_stack_m1F6)) == (*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 72) + 66))) goto loc_007E957B;
    result = (unsigned int)((result) | (0xFFFFFFFFULL));
    v_stack_m1C8 = (unsigned int)(result);
    v_stack_m1C4 = (unsigned int)(result);
loc_007E9576:
    v_stack_m1E0 = 0;
loc_007E957B:
    result = CmpPrepareToInvalidateAllHigherLayerKcbs(*(unsigned __int64 *)(a1 + 8), 2, v_stack_m198, v_stack_m160);
    a1 = 0;
    if (((unsigned int)(result)) != 0xC000022DULL) goto loc_007E959F;
    v_stack_m1F4 = 1;
    goto loc_007E95A7;
loc_007E959F:
    if (sign_flag) goto loc_007E9B18;
loc_007E95A7:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 66)) == 0) goto loc_007E95D0;
    a2 = 0;
    result = CmpPrepareForSubtreeInvalidation(*(unsigned __int64 *)(a1 + 8), a2, v_stack_m198, v_stack_m160);
    if (((unsigned int)(result)) == 0xC000022DULL) goto loc_007E95DA;
    a1 = 0;
    if (sign_flag) goto loc_007E9B18;
loc_007E95D0:
    if (v_stack_m1F4 == 0) goto loc_007E970B;
loc_007E95DA:
    a2 = 0;
    v_stack_m228 = (unsigned int)((unsigned int)(v_stack_m198));
    result = CmpLogTransactionAbortedWithChildName(*(unsigned __int64 *)(a1 + 8), a2, a2 + 4, v_stack_m160);
    v_rbx = v_stack_m1A8;
    if (v_stack_m1A8 != 0) {
        a3 = 0;
        a2 = v_stack_m158;
        a1 = v_stack_m1A8;
        result = CmpDereferenceKeyControlBlockWithLock(a1, a2, a3, v_stack_m160);
        v_rbx = 0;
        v_stack_m1A8 = 0;
    }
    a2 = 0;
    result = CmpDrainDelayDerefContext(v_stack_m158, a2, a3, v_stack_m160);
    result = CmpUnlockRegistry(v_stack_m158, a2, a3, v_stack_m160);
    a2 = 0;
    v_stack_m1F8 = 0;
    result = CmpAbortRollbackPacket(v_stack_m198, a2, a3, v_stack_m160);
    if (sign_flag) goto loc_007E9B18;
    result = CmpCleanupRollbackPacket(v_stack_m198, a2, a3, v_stack_m160);
    v_stack_m198 = v_xmm0;
    result = CmpCleanupKcbStack(v_stack_m120, a2, a3, v_stack_m160);
    result = CmpCleanupKcbStack(v_stack_m100, a2, a3, v_stack_m160);
    goto loc_007E96C1;
loc_007E965F:
    v_rdi = 0;
loc_007E9661:
    a2 = 0;
    v_stack_m228 = (unsigned int)((unsigned int)(v_stack_m198));
    result = CmpLogTransactionAbortedWithChildName(*(unsigned __int64 *)(a1 + 8), a2, a2 + 4, v_stack_m160);
    a2 = 0;
    result = CmpDrainDelayDerefContext(v_stack_m158, a2, a2 + 4, v_stack_m160);
    result = CmpUnlockRegistry(v_stack_m158, a2, a2 + 4, v_stack_m160);
    a2 = 0;
    result = CmpAbortRollbackPacket(v_stack_m198, a2, a2 + 4, v_stack_m160);
    if (sign_flag) goto loc_007EA032;
    result = CmpCleanupRollbackPacket(v_stack_m198, a2, a2 + 4, v_stack_m160);
    v_stack_m198 = v_xmm0;
    result = CmpCleanupKcbStack(v_stack_m120, a2, a2 + 4, v_stack_m160);
    result = CmpCleanupKcbStack(v_stack_m100, a2, a2 + 4, v_stack_m160);
loc_007E96C1:
    goto loc_007E9077;
loc_007E96CF:
    result = 0;
loc_007E96D1:
    goto loc_007E9B1D;
loc_007E96DC:
loc_007E96E1:
    goto loc_007E9B22;
loc_007E96EC:
    goto loc_007E9B1D;
loc_007E96FD:
    goto loc_007E9B22;
loc_007E970B:
    if (v_stack_m1A8 != 0) {
        a2 = 8;
        a4 = v_stack_m158;
        a1 = v_stack_m1A8;
        a3 = a2 - 6;
        result = CmpInvalidateAllHigherLayerKcbs(a1, a2, a3, a4);
        result = 0;
        a4 = v_stack_m158;
        a3 = 0;
        v_stack_m228 = 0;
        a1 = v_stack_m1A8;
        a2 = result + 8;
        result = CmpInvalidateSubtree(a1, a2, a3, a4);
        a4 = 1;
        a3 = v_stack_m158;
        a1 = v_stack_m1A8;
        a2 = a4 + 7;
        result = CmpFlushNotifiesOnKeyBodyList(a1, a2, a3, a4);
        a2 = v_stack_m158;
        a1 = v_stack_m1A8;
        result = CmpMarkKeyUnbacked(a1, a2, a3, a4);
        a1 = v_stack_m1A8;
        result = CmpDiscardKcb(a1, a2, a3, a4);
    }
    result = CmpInvalidateAllHigherLayerKcbs(*(unsigned __int64 *)(a1 + 8), 8, 8 - 6, v_stack_m158);
    v_r14 = 0;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 66)) != 0) {
        a4 = v_stack_m158;
        v_stack_m228 = 0;
        a3 = 0;
        a2 = v_r14 + 8;
        a1 = *(unsigned __int64 *)(a1 + 8);
        result = CmpInvalidateSubtree(a1, a2, a3, a4);
    }
loc_007E97A7:
    v_stack_m1E8 = 0;
    if (0 >= (*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 66))) goto loc_007E98E0;
    result = CmpGetKcbAtLayerHeight(v_stack_m100, 0, a3, a4);
    v_stack_m1D0 = result;
    result = CmpFindKcbInHashEntryByName(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 72) + 32), 0, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 72), v_stack_m1B8);
    a1 = 0;
    v_stack_m160 = result;
    if (result == 0) goto loc_007E9802;
    result = CmpReferenceKeyControlBlock(result, 0, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 72), v_stack_m1B8);
    result = CmpDereferenceKeyControlBlockUnsafe(v_stack_m1B0, 0, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 72), v_stack_m1B8);
    v_stack_m1B0 = result;
    goto loc_007E98D3;
loc_007E9802:
    if ((*(unsigned int *)(v_stack_m1D0 + 40)) == -1) goto loc_007E9876;
    result = CmpGetKeyNodeForKcb(v_stack_m1D0, v_stack_m180, 1, v_stack_m1B8);
    result = CmpFindSubKeyByNameWithStatus(*(unsigned __int64 *)(v_stack_m1D0 + 32), result, v_stack_m1B8, v_stack_m188);
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m1D0 + 32) + 140)) & (1)) == 0) goto loc_007E9858;
    result = HvpReleaseCellFlat(*(unsigned __int64 *)(v_stack_m1D0 + 32), v_stack_m180, v_stack_m1B8, v_stack_m188);
    goto loc_007E985D;
loc_007E9858:
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(v_stack_m1D0 + 32), v_stack_m180, v_stack_m1B8, v_stack_m188);
loc_007E985D:
    a1 = 0;
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == 0xC0000034ULL) goto loc_007E9876;
    if (sign_flag) goto loc_007E9B18;
    goto loc_007E987C;
loc_007E9876:
    a2 = (unsigned int)(((unsigned int)(v_stack_m188)) | (0xFFFFFFFFULL));
    v_stack_m188 = (unsigned int)(a2);
loc_007E987C:
    v_stack_m208 = v_stack_m160;
    v_stack_m210 = 0;
    v_stack_m218 = 0;
    v_stack_m220 = v_stack_m1B8;
    v_stack_m228 = 0;
    result = CmpCreateKeyControlBlock(*(unsigned __int64 *)(v_stack_m1D0 + 32), a2, v_stack_m1D0, v_stack_m1B0);
    if (sign_flag) goto loc_007E9B18;
    result = v_stack_m1B0;
    if (v_stack_m1B0 != 0) {
        a1 = v_stack_m1B0;
        result = CmpDereferenceKeyControlBlockUnsafe(a1, a2, v_stack_m1D0, v_stack_m1B0);
    }
    v_stack_m1B0 = v_stack_m160;
loc_007E98D3:
    result = (unsigned __int16)((v_stack_m1E8) + 1);
    goto loc_007E97A7;
loc_007E98E0:
    v_rbx = 0;
    if (v_stack_m1B0 == 0) goto loc_007E98FE;
    result = CmpAllocateLayerInfoForKcb(v_stack_m1B0, a2, v_stack_m1D0, v_stack_m1B0);
    if (sign_flag) goto loc_007E9B1D;
loc_007E98FE:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 66)) == 0) goto loc_007E9936;
    a3 = 0;
    result = CmpPromoteKey(v_stack_m120, a3 + 1, a3, v_stack_m1B0);
    if (sign_flag) goto loc_007E9B1D;
    a2 = 0;
    result = CmpPromoteSubtree(v_stack_m120, a2, a3, v_stack_m1B0);
    if (sign_flag) goto loc_007E9B1D;
loc_007E9936:
    a4 = 0;
    result = HvpMarkCellDirty(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 72) + 32), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 72) + 40)), a4 + 1, a4);
    if (sign_flag) goto loc_007E9B1D;
    result = CmpGetKeyNodeForKcb(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 72), v_stack_m148, 1, a4);
    v_stack_m170 = result;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result + 28)))) == -1) goto loc_007E998B;
    result = CmpMarkEntireIndexDirty(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 72) + 32), (unsigned int)(*(unsigned int *)(result + 28)), 1, a4);
    if (sign_flag) goto loc_007E9B1D;
loc_007E998B:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m170 + 32)))) == -1) goto loc_007E99A7;
    result = CmpMarkEntireIndexDirty(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 72) + 32), (unsigned int)(*(unsigned int *)(v_stack_m170 + 32)), 1, a4);
    if (sign_flag) goto loc_007E9B1D;
loc_007E99A7:
    a4 = 0;
    result = HvpMarkCellDirty(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 40)), a4 + 1, a4);
    if (sign_flag) goto loc_007E9B1D;
    if (((unsigned int)((unsigned int)(v_stack_m1C8))) == -1) goto loc_007E99EA;
    result = CmpMarkKeyDirty(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 72) + 32), (unsigned int)((unsigned int)((unsigned int)(v_stack_m1C8))), 1, a4);
    if (sign_flag) goto loc_007E9B1D;
loc_007E99EA:
    if (v_stack_m1F6 != 0) goto loc_007E9AB1;
    result = CmpMarkAllChildrenDirty(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 40)), 1, a4);
    if (sign_flag) goto loc_007E9B1D;
loc_007E9A0C:
    result = CmpNameSize(v_stack_m1B8, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 40)), 1, a4);
    v_stack_m220 = v_stack_m140;
    a2 = (unsigned int)(((unsigned __int16)(result)) + (76));
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 40))) >> (31));
    v_stack_m228 = v_stack_m1A0;
    result = HvAllocateCell(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), a2, a3, v_stack_m1C0);
    if (sign_flag) goto loc_007E9B1D;
    result = CmpGetKeyNodeForKcb(*(unsigned __int64 *)(a1 + 8), v_stack_m178, 1, v_stack_m1C0);
    *(unsigned __int64 *)(v_stack_m1A0) = v_xmm0;
    *(unsigned __int64 *)(v_stack_m1A0 + 16) = v_xmm1;
    *(unsigned __int64 *)(v_stack_m1A0 + 32) = v_xmm0;
    *(unsigned __int64 *)(v_stack_m1A0 + 48) = v_xmm1;
    *(unsigned __int64 *)(v_stack_m1A0 + 64) = v_xmm0;
    *(unsigned int *)(v_stack_m1A0 + 72) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 72)));
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 140)) & (1)) == 0) goto loc_007E9B61;
    result = HvpReleaseCellFlat(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), v_stack_m178, 1, v_stack_m1C0);
    goto loc_007E9B66;
loc_007E9AB1:
    result = CmpSubtreeEnumeratorStartForKcbStack(v_stack_mB8, v_stack_m120, 1, v_stack_m1C0);
    if (sign_flag) goto loc_007E9B1D;
loc_007E9AC8:
    result = CmpSubtreeEnumeratorAdvance(v_stack_mB8, v_stack_m120, 1, v_stack_m1C0);
    if (((unsigned int)(result)) == 0x8000001AULL) goto loc_007E9A0C;
    a2 = 0;
    result = CmpSubtreeEnumeratorGetCurrentKeyStacks(v_stack_mB8, a2, v_stack_m138, v_stack_m1C0);
    result = CmpKeyNodeStackGetEntryAtLayerHeight(v_stack_m138, *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 66), v_stack_m138, v_stack_m1C0);
    a4 = 0;
    result = HvpMarkCellDirty(*(unsigned __int64 *)(result), (unsigned int)(*(unsigned int *)(result + 8)), a4 + 1, a4);
    if (!sign_flag) goto loc_007E9AC8;
loc_007E9B18:
loc_007E9B1D:
loc_007E9B22:
loc_007E9B27:
    result = CmpSubtreeEnumeratorCleanup(v_stack_mB8, (unsigned int)(*(unsigned int *)(result + 8)), a4 + 1, a4);
    if (v_stack_m170 == 0) goto loc_007EA083;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 72) + 32) + 140)) & (1)) == 0) goto loc_007EA07E;
    result = HvpReleaseCellFlat(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 72) + 32), v_stack_m148, a4 + 1, a4);
    goto loc_007EA083;
loc_007E9B61:
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 72) + 32), v_stack_m148, a4 + 1, a4);
loc_007E9B66:
    result = CmpCopyName(v_stack_m1A0 + 76, v_stack_m1B8, a4 + 1, a4);
    *(unsigned __int16 *)(v_stack_m1A0 + 72) = (unsigned __int16)(result);
    if (((unsigned __int16)(result)) >= (*(unsigned __int16 *)(v_stack_m1B8))) goto loc_007E9B8B;
    goto loc_007E9B98;
loc_007E9B8B:
loc_007E9B98:
    result = 0;
    *(unsigned __int64 *)(v_stack_m1A0 + 4) = v_stack_m1F8;
    if (v_stack_m1F6 != 0) {
    }
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 66)) == 0) goto loc_007E9BD8;
    result = CmpReferenceSecurityNode(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), (unsigned int)(*(unsigned int *)(v_stack_m1A0 + 44)), a4 + 1, a4);
    if (sign_flag) goto loc_007E9B18;
    v_stack_m184 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m1A0 + 44)));
loc_007E9BD8:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 140)) & (1)) == 0) goto loc_007E9BF4;
    result = HvpReleaseCellFlat(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), v_stack_m140, a4 + 1, a4);
    goto loc_007E9BF9;
loc_007E9BF4:
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), v_stack_m140, a4 + 1, a4);
loc_007E9BF9:
    result = 0;
    v_stack_m1A0 = 0;
    result = CmpGetNameControlBlock(v_stack_m1B8, v_stack_m130, a4 + 1, a4);
    v_stack_m1F0 = result;
    if (result != 0) goto loc_007E9C23;
    goto loc_007E9B1D;
loc_007E9C23:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m170 + 28)))) == -1) goto loc_007E9C4B;
    a3 = 0;
    result = CmpDuplicateIndex(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 72) + 32), (unsigned int)(*(unsigned int *)(v_stack_m170 + 28)), a3, v_stack_m1D8);
    if (sign_flag) goto loc_007E9B18;
loc_007E9C4B:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m170 + 32)))) == -1) goto loc_007E9C72;
    result = CmpDuplicateIndex(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 72) + 32), (unsigned int)(*(unsigned int *)(v_stack_m170 + 32)), 1, v_stack_m1D4);
    if (sign_flag) goto loc_007E9B18;
loc_007E9C72:
    if (((unsigned int)((unsigned int)(v_stack_m1C8))) == -1) goto loc_007E9CA4;
    result = ((unsigned int)((unsigned int)((unsigned int)(v_stack_m1C8)))) >> (31);
    result = CmpRemoveSubKeyFromList(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 72) + 32), v_stack_m1D8 + result * 4, (unsigned int)((unsigned int)((unsigned int)(v_stack_m1C8))), v_stack_m1D4);
    if ((unsigned __int8)(result) != 0) goto loc_007E9CA4;
loc_007E9C99:
    goto loc_007E9B18;
loc_007E9CA4:
    v_rbx = ((unsigned int)((unsigned int)((unsigned int)(v_stack_m1C0)))) >> (31);
    result = CmpAddSubKeyToList(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 72) + 32), v_stack_m1D8 + v_rbx * 4, (unsigned int)((unsigned int)((unsigned int)(v_stack_m1C0))), v_stack_m1D4);
    result = 0;
    if (sign_flag) goto loc_007E9B18;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 66)) != 0) goto loc_007E9CF8;
    result = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 40))))) >> (31);
    result = CmpRemoveSubKeyFromList(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 72) + 32), v_stack_m1D8 + result * 4, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 40)), v_stack_m1D4);
    if ((unsigned __int8)(result) == 0) goto loc_007E9C99;
loc_007E9CF8:
    a2 = (unsigned int)((v_stack_m1D8 + result * 4) | (0xFFFFFFFFULL));
    *(unsigned int *)(v_stack_m170 + 28) = (unsigned int)((unsigned int)(v_stack_m1D8));
    v_stack_m1D8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m170 + 28)));
    *(unsigned int *)(v_stack_m170 + 32) = (unsigned int)((unsigned int)(v_stack_m1D4));
    v_stack_m1D4 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m170 + 32)));
    result = (unsigned int)(v_stack_m1C8);
    if (((unsigned int)((unsigned int)(v_stack_m1C8))) != ((unsigned int)(a2))) {
        result = ((unsigned int)(v_stack_m1C8)) >> (31);
    }
    v_rbx = 0;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 66)) == 0) {
        result = *(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 40);
        result = (result) >> (31);
    }
    result = CmpCleanUpSubKeyInfo(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 72), 1, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 40)), v_stack_m1D4);
    if (((unsigned int)((unsigned __int16)((unsigned int)(*(unsigned int *)(v_stack_m170 + 52))))) < ((unsigned int)(*(unsigned __int16 *)(v_stack_m1B8)))) {
        *(unsigned __int16 *)(v_stack_m170 + 52) = (unsigned __int16)(*(unsigned __int16 *)(v_stack_m1B8));
        *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 72) + 176) = (unsigned __int16)(*(unsigned __int16 *)(v_stack_m1B8));
    }
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 66)) != 0) goto loc_007E9D8E;
    result = HvFreeCell(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 40)), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 40)), v_stack_m1D4);
    goto loc_007E9E00;
loc_007E9D8E:
    result = CmpGetKeyNodeForKcb(*(unsigned __int64 *)(a1 + 8), v_stack_m178, 1, v_stack_m1D4);
    a1 = (unsigned __int8)((*(unsigned __int8 *)(result + 13)) & (124));
    a1 = (unsigned __int8)((a1) | (1));
    *(unsigned __int16 *)(result + 52) = 0;
    *(unsigned __int8 *)(result + 13) = (unsigned __int8)(a1);
    a1 = (unsigned int)((a1) | (0xFFFFFFFFULL));
    *(unsigned int *)(result + 28) = (unsigned int)(a1);
    *(unsigned int *)(result + 32) = (unsigned int)(a1);
    *(unsigned int *)(result + 40) = (unsigned int)(a1);
    *(unsigned int *)(result + 48) = (unsigned int)(a1);
    *(unsigned __int64 *)(result + 20) = 0;
    *(unsigned int *)(result + 36) = 0;
    *(unsigned __int8 *)(result + 55) = 0;
    *(unsigned __int64 *)(result + 56) = 0;
    *(unsigned int *)(result + 64) = 0;
    *(unsigned __int16 *)(result + 74) = 0;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 140)) & (1)) == 0) goto loc_007E9DFB;
    result = HvpReleaseCellFlat(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), v_stack_m178, 1, v_stack_m1D4);
    goto loc_007E9E00;
loc_007E9DFB:
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), v_stack_m178, 1, v_stack_m1D4);
loc_007E9E00:
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 40) = (unsigned int)((unsigned int)(v_stack_m1C0));
    result = (unsigned int)(((unsigned int)(v_stack_m1C0)) | (0xFFFFFFFFULL));
    v_stack_m1C0 = (unsigned int)(result);
    v_stack_m184 = (unsigned int)(result);
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 66)) == 0) goto loc_007E9E71;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 192)) + 8)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 192))) goto loc_007E9F6B;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 192) + 8))) != (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 192))) goto loc_007E9F6B;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 192) + 8)) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 192));
    a3 = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 192)) + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 192) + 8);
    result = CmpDereferenceKeyControlBlockWithLock(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 192) + 24) + 16), v_stack_m158, a3, v_stack_m1D4);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 192) + 24) = 0;
    result = CmpCreateLayerLink(v_stack_m1B0, *(unsigned __int64 *)(a1 + 8), a3, v_stack_m1D4);
loc_007E9E71:
    result = CmpRemoveKeyHash(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), *(unsigned __int64 *)(a1 + 8) + 16, a3, v_stack_m1D4);
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 16) = (unsigned int)(v_stack_m1E0);
    result = CmpInsertKeyHash(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), *(unsigned __int64 *)(a1 + 8) + 16, a3, v_stack_m1D4);
    v_rdi = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 80) = v_stack_m1F0;
    v_stack_m1F0 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 80);
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 296);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 296) != 0) {
        result = v_rdi + 1;
    }
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 200)) >= 2) {
        a2 = 0x624E4D43ULL;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 200), a2, a3, v_stack_m1D4);
    }
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 200) = 0;
    if ((unsigned __int8)(v_stack_m1F6) != 0) {
        *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 8) + 65) = 3;
    }
    result = CmpUpdateParentForEachSon(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 40)), a3, v_stack_m1D4);
    if ((unsigned __int8)(v_stack_m1F6) == 0) goto loc_007E9FAA;
loc_007E9F08:
    a1 = (v_stack_m58) + (56);
    a1 = (a1) + (0);
    result = CmpKeyEnumStackReset(a1, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 40)), a3, v_stack_m1D4);
    v_rbx = (0) + (408);
    v_rdi = (512) - (1);
    if (condition_is_not_equal) goto loc_007E9F08;
    v_stack_mB0 = v_rdi;
    v_stack_mB8 = (unsigned __int16)(v_rdi - 2);
    result = CmpResetKeyNodeStack(v_stack_mA8, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 40)), a3, v_stack_m1D4);
    result = CmpSubtreeEnumeratorBeginForKcbStack(v_stack_mB8, v_stack_m120, a3, v_stack_m1D4);
    result = CmpSubtreeEnumeratorAdvance(v_stack_mB8, v_stack_m120, a3, v_stack_m1D4);
    goto loc_007E9FA6;
loc_007E9F6B:
loc_007E9F72:
    a2 = 0;
    result = CmpSubtreeEnumeratorGetCurrentKeyStacks(v_stack_mB8, a2, v_stack_m138, v_stack_m1D4);
    result = CmpKeyNodeStackGetEntryAtLayerHeight(v_stack_m138, *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 66), v_stack_m138, v_stack_m1D4);
    result = CmpSubtreeEnumeratorAdvance(v_stack_mB8, *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 66), v_stack_m138, v_stack_m1D4);
loc_007E9FA6:
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)(0x8000001AULL)))) goto loc_007E9F72;
loc_007E9FAA:
    *(unsigned __int64 *)(v_stack_m170 + 4) = v_stack_m1F8;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 72) + 168) = v_stack_m1F8;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 72) + 32) + 140)) & (1)) == 0) goto loc_007E9FD1;
    result = HvpReleaseCellFlat(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 72) + 32), v_stack_m148, v_stack_m138, v_stack_m1D4);
    goto loc_007E9FD6;
loc_007E9FD1:
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 72) + 32), v_stack_m148, v_stack_m138, v_stack_m1D4);
loc_007E9FD6:
    a3 = 0;
    v_stack_m170 = v_rdi;
    result = CmpSearchForOpenSubKeys(*(unsigned __int64 *)(a1 + 8), 1, a3, v_stack_m1D4);
    if (((unsigned int)((unsigned int)(v_stack_m1C4))) != -1) {
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 72) + 32);
        a3 = 0;
        result = CmpFreeKeyByCell(a1, (unsigned int)(v_stack_m1C4), a3, v_stack_m1D4);
    }
    goto loc_007E9B18;
loc_007EA011:
    goto loc_007E9B27;
loc_007EA027:
    goto loc_007E9B1D;
loc_007EA032:
    goto loc_007E9B27;
loc_007EA044:
    result = CmpLogUnsupportedOperation(24, (unsigned int)(v_stack_m1C4), a3, v_stack_m1D4);
    result = 0;
    goto loc_007E96E1;
loc_007EA05B:
loc_007EA061:
    goto loc_007E93DE;
loc_007EA069:
    result = 0;
    goto loc_007E9B27;
loc_007EA07E:
    result = HvpReleaseCellPaged(24, (unsigned int)(v_stack_m1C4), a3, v_stack_m1D4);
loc_007EA083:
    if (0 == 0) goto loc_007EA0AA;
    if (((*(unsigned __int8 *)(v_stack_m1E0 + 140)) & (1)) == 0) goto loc_007EA0A5;
    result = HvpReleaseCellFlat(v_stack_m1E0, v_stack_m168, a3, v_stack_m1D4);
    goto loc_007EA0AA;
loc_007EA0A5:
    result = HvpReleaseCellPaged(v_stack_m1E0, v_stack_m168, a3, v_stack_m1D4);
loc_007EA0AA:
    result = (unsigned int)(v_stack_m184);
    if (((unsigned int)((unsigned int)(v_stack_m184))) != -1) {
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32);
        a2 = (unsigned int)((unsigned int)(v_stack_m184));
        result = CmpDereferenceSecurityNode(a1, a2, a3, v_stack_m1D4);
    }
    v_rdi = 0;
    if (v_stack_m1A0 == 0) goto loc_007EA0E2;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 140)) & (1)) == 0) goto loc_007EA0DD;
    result = HvpReleaseCellFlat(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), v_stack_m140, a3, v_stack_m1D4);
    goto loc_007EA0E2;
loc_007EA0DD:
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), v_stack_m140, a3, v_stack_m1D4);
loc_007EA0E2:
    v_r12 = (unsigned int)((1) | (0xFFFFFFFFULL));
    if (((unsigned int)((unsigned int)(v_stack_m1D8))) != ((unsigned int)(v_r12))) {
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 72) + 32);
        result = CmpFreeIndexByCell(a1, (unsigned int)(v_stack_m1D8), a3, v_stack_m1D4);
    }
    if (((unsigned int)((unsigned int)(v_stack_m1D4))) != ((unsigned int)(v_r12))) {
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 72) + 32);
        result = CmpFreeIndexByCell(a1, (unsigned int)(v_stack_m1D4), a3, v_stack_m1D4);
    }
    result = (unsigned int)(v_stack_m1C0);
    if (((unsigned int)((unsigned int)(v_stack_m1C0))) != ((unsigned int)(v_r12))) {
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32);
        a2 = (unsigned int)((unsigned int)(v_stack_m1C0));
        result = HvFreeCell(a1, a2, a3, v_stack_m1D4);
    }
    if (0 != 0) {
        a1 = 0;
        result = CmpDereferenceNameControlBlockWithLock(a1, a2, a3, v_stack_m1D4);
    }
    result = v_stack_m1B0;
    if (v_stack_m1B0 != 0) {
        a3 = 0;
        a2 = v_stack_m158;
        a1 = v_stack_m1B0;
        result = CmpDereferenceKeyControlBlockWithLock(a1, a2, a3, v_stack_m1D4);
    }
    result = v_stack_m1A8;
    if (v_stack_m1A8 != 0) {
        a3 = 0;
        a2 = v_stack_m158;
        a1 = v_stack_m1A8;
        result = CmpDereferenceKeyControlBlockWithLock(a1, a2, a3, v_stack_m1D4);
    }
    a2 = 0;
    result = CmpDrainDelayDerefContext(v_stack_m158, a2, a3, v_stack_m1D4);
    if (0 != 0) {
        result = CmpUnlockRegistry(v_stack_m158, a2, a3, v_stack_m1D4);
    }
    result = CmpCleanupKcbStack(v_stack_m120, a2, a3, v_stack_m1D4);
    result = CmpCleanupKcbStack(v_stack_m100, a2, a3, v_stack_m1D4);
    result = CmpCleanupKcbStack(v_stack_mE0, a2, a3, v_stack_m1D4);
    result = CmpCleanupRollbackPacket(v_stack_m198, a2, a3, v_stack_m1D4);
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, v_stack_m1D4);
    v_rsp = (v_rsp) + (528);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CmRenameKey(int64_t Arg1, int64_t Arg2, uint8_t Arg3)
{
    int64_t result;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m110;
    uint16_t v_stack_m11E;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint32_t v_stack_m130;
    uint64_t v_stack_m138;
    uint64_t v_stack_m140;
    uint64_t v_stack_m148;
    uint64_t v_stack_m158;
    uint64_t v_stack_m160;
    uint64_t v_stack_m168;
    uint64_t v_stack_m170;
    uint64_t v_stack_m178;
    uint64_t v_stack_m180;
    uint32_t v_stack_m184;
    uint32_t v_stack_m188;
    uint64_t v_stack_m198;
    uint64_t v_stack_m1A0;
    uint64_t v_stack_m1A8;
    uint64_t v_stack_m1B0;
    uint64_t v_stack_m1B8;
    uint32_t v_stack_m1C0;
    uint32_t v_stack_m1C4;
    uint32_t v_stack_m1C8;
    uint64_t v_stack_m1D0;
    uint32_t v_stack_m1D4;
    uint32_t v_stack_m1D8;
    uint64_t v_stack_m1E0;
    uint8_t v_stack_m1E8;
    uint64_t v_stack_m1F0;
    uint8_t v_stack_m1F4;
    uint8_t v_stack_m1F6;
    uint8_t v_stack_m1F8;
    uint64_t v_stack_m208;
    uint32_t v_stack_m210;
    uint32_t v_stack_m218;
    uint32_t v_stack_m220;
    uint8_t v_stack_m228;
    uint64_t v_stack_m48;
    uint64_t v_stack_m58;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mD0;
    uint16_t v_stack_mDE;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mF0;
    uint16_t v_stack_mFE;
    uint64_t v_stack_p18;

    v_stack_p18 = local_rbx;
    local_rsp = (local_rsp) - (528);
    result = (*(uint64_t *)(v_rip + 0x6217D2)) ^ (local_rsp);
    v_stack_m48 = result;
    local_r14 = 0;
    v_stack_m1B8 = Arg2;
    v_stack_m160 = Arg1;
    v_stack_m1E8 = Arg3;
    v_stack_m128 = 0;
    v_stack_m168 = 0;
    Arg2 = 0;
    v_stack_m180 = 0;
    v_stack_m140 = 0;
    v_stack_m158 = v_xmm0;
    v_stack_m178 = 0;
    v_stack_m188 = 0;
    v_stack_m148 = 0;
    result = memset(v_stack_mB8, Arg2, local_r14 + 104, a4);
    v_stack_m138 = 0;
    result = (uint32_t)((result) | (0xFFFFFFFFULL));
    v_stack_m1A8 = 0;
    v_stack_m1B0 = 0;
    v_stack_m120 = v_xmm1;
    v_stack_m11E = (uint16_t)(result);
    v_stack_m100 = v_xmm0;
    v_stack_mFE = (uint16_t)(result);
    v_stack_mE0 = v_xmm0;
    v_stack_mDE = (uint16_t)(result);
    v_stack_m198 = v_xmm0;
    v_stack_m1E0 = 0;
    v_stack_m110 = v_xmm1;
    v_stack_mF0 = v_xmm0;
    v_stack_mD0 = v_xmm0;
    result = HvpGetCellContextInitialize(v_stack_m168, Arg2, local_r14 + 104, a4);
    result = HvpGetCellContextInitialize(v_stack_m180, Arg2, local_r14 + 104, a4);
    Arg3 = (uint32_t)((local_r14 + 104) | (0xFFFFFFFFULL));
    v_stack_m1A0 = 0;
    v_stack_m1C0 = Arg3;
    result = HvpGetCellContextInitialize(v_stack_m140, Arg2, Arg3, a4);
    result = HvpGetCellContextInitialize(v_stack_m178, Arg2, Arg3, a4);
    v_stack_m184 = Arg3;
    v_stack_m170 = 0;
    result = HvpGetCellContextInitialize(v_stack_m148, Arg2, Arg3, a4);
    v_stack_m1F0 = 0;
    v_stack_m1D8 = Arg3;
    v_stack_m1D4 = Arg3;
    v_stack_m1F6 = 0;
    result = CmpSubtreeEnumeratorInitialize(v_stack_mB8, Arg2, Arg3, a4);
    result = CmpInitializeDelayDerefContext(v_stack_m158, Arg2, Arg3, a4);
loc_007E9077:
    v_stack_m1D0 = 0;
    result = CmpIsShutdownRundownActive(v_stack_m158, Arg2, Arg3, a4);
    if ((uint8_t)(result) != 0) goto loc_007EA069;
    result = CmpLockRegistryExclusive(v_stack_m158, Arg2, Arg3, a4);
    v_stack_m1F8 = 1;
    result = CmpStartKcbStackForTopLayerKcb(v_stack_m120, *(uint64_t *)(Arg1 + 0x8), Arg3, a4);
    result = 0;
    if (sign_flag) goto loc_007E96E1;
    result = CmpStartKcbStackForTopLayerKcb(v_stack_m100, *(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x48), Arg3, a4);
    Arg2 = 0;
    if (sign_flag) goto loc_007EA061;
    if (((*(uint32_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x8)) & (384)) != 0) goto loc_007EA05B;
    if (((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x20) + 0xA0)) & (0x100000ULL)) != 0) goto loc_007EA05B;
    if ((*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x20)) == (*(uint64_t *)(v_rip + 0x7F098B))) goto loc_007EA05B;
    if (((*(uint32_t *)(*(uint64_t *)(Arg1 + 0x8) + 0xB8)) & (0x40000ULL)) != 0) goto loc_007EA05B;
    result = CmpPerformKeyBodyDeletionCheck(Arg1, Arg2, Arg3, a4);
    result = 0;
    if (sign_flag) goto loc_007E96E1;
    if ((*(uint64_t *)(Arg1 + 0x38)) != 0) goto loc_007E9146;
    if ((*(uint64_t *)(Arg1 + 0x40)) != 0) goto loc_007E9146;
    v_stack_m128 = 0;
    goto loc_007E918A;
loc_007E9146:
    result = CmpTransSearchAddTransFromKeyBody(Arg1, v_stack_m128, Arg3, a4);
    result = 0;
    if (sign_flag) goto loc_007E96E1;
    result = CmpPerformKeyBodyDeletionCheck(Arg1, v_stack_m128, Arg3, a4);
    result = 0;
    if (sign_flag) goto loc_007E96E1;
    if (v_stack_m128 != 0) goto loc_007EA044;
loc_007E918A:
    v_stack_m228 = 0;
    Arg2 = 0;
    result = CmpCheckKcbStackAccess(v_stack_m100, Arg2, (uint8_t)(v_stack_m1E8), 4);
    result = 0;
    if (sign_flag) goto loc_007E96E1;
    result = (uint16_t)(-(*(uint16_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x42)));
    v_stack_m220 = 1;
    Arg3 = 0;
    Arg1 = (uint32_t)((v_stack_m100) & (0x20019ULL));
    Arg1 = (uint32_t)((Arg1) + (0x10000ULL));
    v_stack_m228 = (uint32_t)(Arg1);
    result = CmpDoAccessCheckOnLayeredSubtree(v_stack_m120, Arg2, Arg3, (uint8_t)(v_stack_m1E8));
    result = 0;
    if (sign_flag) goto loc_007E96E1;
    Arg2 = 0;
    result = CmpFlushNotifiesOnKeyBodyList(*(uint64_t *)(Arg1 + 0x8), Arg2, v_stack_m158, (uint8_t)(result + 1));
    a4 = 0;
    result = CmpReportNotify(*(uint64_t *)(Arg1 + 0x8), Arg2, (uint32_t)((uint32_t)(result + 1)), a4);
    result = CmpTryAcquireKcbIXLocks(*(uint64_t *)(Arg1 + 0x8), (uint8_t)(result + 1), (uint32_t)((uint32_t)(result + 1)), v_stack_m198);
    if ((((uint32_t)((uint32_t)(0x80000000ULL))) & ((uint32_t)((uint32_t)((uint32_t)(result)) + (uint32_t)(0x80000000ULL) * 1))) != 0) goto loc_007E923C;
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != 0xC000022DULL) goto loc_007E96CF;
loc_007E923C:
    result = CmpTryAcquireKcbIXLocks(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x48), 1, (uint32_t)((uint32_t)(result + 1)), v_stack_m198);
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == ((uint32_t)((uint32_t)(0xC000022DULL)))) goto loc_007E965F;
    local_rdi = 0;
    if (sign_flag) goto loc_007EA027;
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == ((uint32_t)((uint32_t)(0xC000022DULL)))) goto loc_007E9661;
    result = CmpHashUnicodeComponent(v_stack_m1B8, 1, (uint32_t)((uint32_t)(result + 1)), v_stack_m198);
    local_rdi = (uint32_t)((local_rdi) * (*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x48) + 0x10)));
    v_stack_m130 = (uint32_t)(result);
    local_rdi = (uint32_t)((local_rdi) + ((uint32_t)(result)));
    result = CmpFindKcbInHashEntryByName(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x48) + 0x20), (uint32_t)((uint32_t)(local_rdi)), *(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x48), v_stack_m1B8);
    local_r11 = 0;
    v_stack_m1A8 = result;
    if (result == 0) goto loc_007E93E6;
    result = CmpReferenceKeyControlBlock(result, (uint32_t)((uint32_t)(local_rdi)), *(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x48), v_stack_m1B8);
    v_stack_m1C8 = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x28)));
    v_stack_m1C4 = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x28)));
    result = CmpStartKcbStackForTopLayerKcb(v_stack_mE0, result, *(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x48), v_stack_m1B8);
    result = 0;
    if (sign_flag) goto loc_007E96D1;
    Arg2 = 0;
    result = CmpIsKeyStackDeleted(v_stack_mE0, Arg2, *(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x48), v_stack_m1B8);
    Arg1 = 0;
    if ((uint8_t)(result) == 0) goto loc_007E96EC;
loc_007E92FF:
    if (sign_flag) goto loc_007E9331;
    result = CmpGetKcbAtLayerHeight(v_stack_mE0, (uint16_t)(*(uint16_t *)(v_stack_m1A8 + 0x42)), *(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x48), *(uint16_t *)(v_stack_m1A8 + 0x42));
    result = CmpGetEffectiveKcbSemantics(result, 0, *(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x48), *(uint16_t *)(v_stack_m1A8 + 0x42));
    if (((uint32_t)(result)) == 1) goto loc_007E932C;
    a4 = (uint16_t)((*(uint16_t *)(v_stack_m1A8 + 0x42)) - 1);
    goto loc_007E92FF;
loc_007E932C:
    goto loc_007E9336;
loc_007E9331:
loc_007E9336:
    v_stack_m1F6 = (uint8_t)(v_stack_m1F6);
    result = CmpTryAcquireKcbIXLocks(v_stack_m1A8, 1, *(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x48), v_stack_m198);
    if (((uint32_t)(result)) != 0xC000022DULL) goto loc_007E9358;
    v_stack_m1F4 = 1;
    goto loc_007E9363;
loc_007E9358:
    result = 0;
    if (sign_flag) goto loc_007E96DC;
loc_007E9363:
    result = CmpPrepareToInvalidateAllHigherLayerKcbs(v_stack_m1A8, 2, v_stack_m198, v_stack_m198);
    if (((uint32_t)(result)) != 0xC000022DULL) goto loc_007E9386;
    v_stack_m1F4 = 1;
    goto loc_007E9391;
loc_007E9386:
    result = 0;
    if (sign_flag) goto loc_007E96DC;
loc_007E9391:
    Arg2 = 0;
    result = CmpPrepareForSubtreeInvalidation(v_stack_m1A8, Arg2, v_stack_m198, v_stack_m198);
    if (((uint32_t)(result)) != 0xC000022DULL) goto loc_007E93BE;
    result = 0;
    v_stack_m1F4 = 1;
    goto loc_007E9576;
loc_007E93BE:
    Arg2 = 0;
    v_stack_m1F6 = 0;
    v_stack_m1E0 = v_stack_m1D0;
    if (!sign_flag) goto loc_007E957B;
loc_007E93DE:
    goto loc_007E9B22;
loc_007E93E6:
    result = (uint32_t)((v_stack_m1D0) | (0xFFFFFFFFULL));
    v_stack_m1F6 = (uint16_t)(result);
    v_stack_m1E0 = 0;
loc_007E9400:
    if (sign_flag) goto loc_007E94DF;
    result = CmpGetKcbAtLayerHeight(v_stack_m100, (uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x48) + 0x42)), v_stack_m198, v_stack_m160);
    v_stack_m1D0 = result;
    result = CmpGetEffectiveKcbSemantics(result, v_stack_m160, v_stack_m198, v_stack_m160);
    if (((uint32_t)(result)) == 1) goto loc_007E94D2;
    if ((*(uint32_t *)(result + 0x28)) == -1) goto loc_007E94B5;
    result = CmpGetKeyNodeForKcb(result, v_stack_m180, 1, v_stack_m160);
    result = CmpFindSubKeyByNameWithStatus(*(uint64_t *)(result + 0x20), result, v_stack_m1B8, v_stack_m1C4);
    if (((*(uint8_t *)(*(uint64_t *)(v_stack_m1D0 + 0x20) + 0x8C)) & (1)) == 0) goto loc_007E9485;
    result = HvpReleaseCellFlat(*(uint64_t *)(v_stack_m1D0 + 0x20), v_stack_m180, v_stack_m1B8, v_stack_m1C4);
    goto loc_007E948A;
loc_007E9485:
    result = HvpReleaseCellPaged(*(uint64_t *)(v_stack_m1D0 + 0x20), v_stack_m180, v_stack_m1B8, v_stack_m1C4);
loc_007E948A:
    local_r11 = 0;
    if (!sign_flag) goto loc_007E94BE;
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != 0xC0000034ULL) goto loc_007E96FD;
    result = CmpGetEffectiveKcbSemantics(v_stack_m1D0, v_stack_m160, v_stack_m1B8, v_stack_m1C4);
    if ((uint32_t)(result) != 0) goto loc_007E94E6;
loc_007E94B5:
    local_r12 = (uint16_t)((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x48) + 0x42)) - 1);
    goto loc_007E9400;
loc_007E94BE:
    v_stack_m1E0 = *(uint64_t *)(v_stack_m1D0 + 0x20);
    goto loc_007E94EF;
loc_007E94D2:
    goto loc_007E94F4;
loc_007E94DF:
    goto loc_007E94E9;
loc_007E94E6:
loc_007E94E9:
loc_007E94EF:
loc_007E94F4:
    v_stack_m1C8 = (uint32_t)((uint32_t)(v_stack_m1C4));
    if (((uint32_t)((uint32_t)(v_stack_m1C4))) != -1) goto loc_007E9509;
    v_stack_m1F6 = 0;
    goto loc_007E957B;
loc_007E9509:
    if (((*(uint8_t *)(0 + 0x8C)) & (1)) == 0) goto loc_007E9522;
    result = HvpGetCellFlat(0, (uint32_t)((uint32_t)((uint32_t)(v_stack_m1C4))), v_stack_m168, v_stack_m160);
    goto loc_007E9527;
loc_007E9522:
    result = HvpGetCellPaged(0, (uint32_t)((uint32_t)((uint32_t)(v_stack_m1C4))), v_stack_m168, v_stack_m160);
loc_007E9527:
    result = CmpGetEffectiveKeyNodeSemantics(v_stack_m1E0, result, v_stack_m168, v_stack_m160);
    if (((uint32_t)(result)) != 1) goto loc_007EA011;
    if (((*(uint8_t *)(v_stack_m1E0 + 0x8C)) & (1)) == 0) goto loc_007E9557;
    result = HvpReleaseCellFlat(v_stack_m1E0, v_stack_m168, v_stack_m168, v_stack_m160);
    goto loc_007E955C;
loc_007E9557:
    result = HvpReleaseCellPaged(v_stack_m1E0, v_stack_m168, v_stack_m168, v_stack_m160);
loc_007E955C:
    Arg1 = 0;
    v_stack_m1F6 = 1;
    if (((uint16_t)(v_stack_m1F6)) == (*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x48) + 0x42))) goto loc_007E957B;
    result = (uint32_t)((result) | (0xFFFFFFFFULL));
    v_stack_m1C8 = (uint32_t)(result);
    v_stack_m1C4 = (uint32_t)(result);
loc_007E9576:
    v_stack_m1E0 = 0;
loc_007E957B:
    result = CmpPrepareToInvalidateAllHigherLayerKcbs(*(uint64_t *)(Arg1 + 0x8), 2, v_stack_m198, v_stack_m160);
    Arg1 = 0;
    if (((uint32_t)(result)) != 0xC000022DULL) goto loc_007E959F;
    v_stack_m1F4 = 1;
    goto loc_007E95A7;
loc_007E959F:
    if (sign_flag) goto loc_007E9B18;
loc_007E95A7:
    if ((*(uint16_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x42)) == 0) goto loc_007E95D0;
    Arg2 = 0;
    result = CmpPrepareForSubtreeInvalidation(*(uint64_t *)(Arg1 + 0x8), Arg2, v_stack_m198, v_stack_m160);
    if (((uint32_t)(result)) == 0xC000022DULL) goto loc_007E95DA;
    Arg1 = 0;
    if (sign_flag) goto loc_007E9B18;
loc_007E95D0:
    if (v_stack_m1F4 == 0) goto loc_007E970B;
loc_007E95DA:
    Arg2 = 0;
    v_stack_m228 = (uint32_t)((uint32_t)(v_stack_m198));
    result = CmpLogTransactionAbortedWithChildName(*(uint64_t *)(Arg1 + 0x8), Arg2, Arg2 + 4, v_stack_m160);
    local_rbx = v_stack_m1A8;
    if (v_stack_m1A8 != 0) {
        Arg3 = 0;
        Arg2 = v_stack_m158;
        Arg1 = v_stack_m1A8;
        result = CmpDereferenceKeyControlBlockWithLock(Arg1, Arg2, Arg3, v_stack_m160);
        local_rbx = 0;
        v_stack_m1A8 = 0;
    }
    Arg2 = 0;
    result = CmpDrainDelayDerefContext(v_stack_m158, Arg2, Arg3, v_stack_m160);
    result = CmpUnlockRegistry(v_stack_m158, Arg2, Arg3, v_stack_m160);
    Arg2 = 0;
    v_stack_m1F8 = 0;
    result = CmpAbortRollbackPacket(v_stack_m198, Arg2, Arg3, v_stack_m160);
    if (sign_flag) goto loc_007E9B18;
    result = CmpCleanupRollbackPacket(v_stack_m198, Arg2, Arg3, v_stack_m160);
    v_stack_m198 = v_xmm0;
    result = CmpCleanupKcbStack(v_stack_m120, Arg2, Arg3, v_stack_m160);
    result = CmpCleanupKcbStack(v_stack_m100, Arg2, Arg3, v_stack_m160);
    goto loc_007E96C1;
loc_007E965F:
    local_rdi = 0;
loc_007E9661:
    Arg2 = 0;
    v_stack_m228 = (uint32_t)((uint32_t)(v_stack_m198));
    result = CmpLogTransactionAbortedWithChildName(*(uint64_t *)(Arg1 + 0x8), Arg2, Arg2 + 4, v_stack_m160);
    Arg2 = 0;
    result = CmpDrainDelayDerefContext(v_stack_m158, Arg2, Arg2 + 4, v_stack_m160);
    result = CmpUnlockRegistry(v_stack_m158, Arg2, Arg2 + 4, v_stack_m160);
    Arg2 = 0;
    result = CmpAbortRollbackPacket(v_stack_m198, Arg2, Arg2 + 4, v_stack_m160);
    if (sign_flag) goto loc_007EA032;
    result = CmpCleanupRollbackPacket(v_stack_m198, Arg2, Arg2 + 4, v_stack_m160);
    v_stack_m198 = v_xmm0;
    result = CmpCleanupKcbStack(v_stack_m120, Arg2, Arg2 + 4, v_stack_m160);
    result = CmpCleanupKcbStack(v_stack_m100, Arg2, Arg2 + 4, v_stack_m160);
loc_007E96C1:
    goto loc_007E9077;
loc_007E96CF:
    result = 0;
loc_007E96D1:
    goto loc_007E9B1D;
loc_007E96DC:
loc_007E96E1:
    goto loc_007E9B22;
loc_007E96EC:
    goto loc_007E9B1D;
loc_007E96FD:
    goto loc_007E9B22;
loc_007E970B:
    if (v_stack_m1A8 != 0) {
        Arg2 = 8;
        a4 = v_stack_m158;
        Arg1 = v_stack_m1A8;
        Arg3 = Arg2 - 6;
        result = CmpInvalidateAllHigherLayerKcbs(Arg1, Arg2, Arg3, a4);
        result = 0;
        a4 = v_stack_m158;
        Arg3 = 0;
        v_stack_m228 = 0;
        Arg1 = v_stack_m1A8;
        Arg2 = result + 8;
        result = CmpInvalidateSubtree(Arg1, Arg2, Arg3, a4);
        a4 = 1;
        Arg3 = v_stack_m158;
        Arg1 = v_stack_m1A8;
        Arg2 = a4 + 7;
        result = CmpFlushNotifiesOnKeyBodyList(Arg1, Arg2, Arg3, a4);
        Arg2 = v_stack_m158;
        Arg1 = v_stack_m1A8;
        result = CmpMarkKeyUnbacked(Arg1, Arg2, Arg3, a4);
        Arg1 = v_stack_m1A8;
        result = CmpDiscardKcb(Arg1, Arg2, Arg3, a4);
    }
    result = CmpInvalidateAllHigherLayerKcbs(*(uint64_t *)(Arg1 + 0x8), 8, 8 - 6, v_stack_m158);
    local_r14 = 0;
    if ((*(uint16_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x42)) != 0) {
        a4 = v_stack_m158;
        v_stack_m228 = 0;
        Arg3 = 0;
        Arg2 = local_r14 + 8;
        Arg1 = *(uint64_t *)(Arg1 + 0x8);
        result = CmpInvalidateSubtree(Arg1, Arg2, Arg3, a4);
    }
loc_007E97A7:
    v_stack_m1E8 = 0;
    if (0 >= (*(uint16_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x42))) goto loc_007E98E0;
    result = CmpGetKcbAtLayerHeight(v_stack_m100, 0, Arg3, a4);
    v_stack_m1D0 = result;
    result = CmpFindKcbInHashEntryByName(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x48) + 0x20), 0, *(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x48), v_stack_m1B8);
    Arg1 = 0;
    v_stack_m160 = result;
    if (result == 0) goto loc_007E9802;
    result = CmpReferenceKeyControlBlock(result, 0, *(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x48), v_stack_m1B8);
    result = CmpDereferenceKeyControlBlockUnsafe(v_stack_m1B0, 0, *(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x48), v_stack_m1B8);
    v_stack_m1B0 = result;
    goto loc_007E98D3;
loc_007E9802:
    if ((*(uint32_t *)(v_stack_m1D0 + 0x28)) == -1) goto loc_007E9876;
    result = CmpGetKeyNodeForKcb(v_stack_m1D0, v_stack_m180, 1, v_stack_m1B8);
    result = CmpFindSubKeyByNameWithStatus(*(uint64_t *)(v_stack_m1D0 + 0x20), result, v_stack_m1B8, v_stack_m188);
    if (((*(uint8_t *)(*(uint64_t *)(v_stack_m1D0 + 0x20) + 0x8C)) & (1)) == 0) goto loc_007E9858;
    result = HvpReleaseCellFlat(*(uint64_t *)(v_stack_m1D0 + 0x20), v_stack_m180, v_stack_m1B8, v_stack_m188);
    goto loc_007E985D;
loc_007E9858:
    result = HvpReleaseCellPaged(*(uint64_t *)(v_stack_m1D0 + 0x20), v_stack_m180, v_stack_m1B8, v_stack_m188);
loc_007E985D:
    Arg1 = 0;
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == 0xC0000034ULL) goto loc_007E9876;
    if (sign_flag) goto loc_007E9B18;
    goto loc_007E987C;
loc_007E9876:
    Arg2 = (uint32_t)(((uint32_t)(v_stack_m188)) | (0xFFFFFFFFULL));
    v_stack_m188 = (uint32_t)(Arg2);
loc_007E987C:
    v_stack_m208 = v_stack_m160;
    v_stack_m210 = 0;
    v_stack_m218 = 0;
    v_stack_m220 = v_stack_m1B8;
    v_stack_m228 = 0;
    result = CmpCreateKeyControlBlock(*(uint64_t *)(v_stack_m1D0 + 0x20), Arg2, v_stack_m1D0, v_stack_m1B0);
    if (sign_flag) goto loc_007E9B18;
    result = v_stack_m1B0;
    if (v_stack_m1B0 != 0) {
        Arg1 = v_stack_m1B0;
        result = CmpDereferenceKeyControlBlockUnsafe(Arg1, Arg2, v_stack_m1D0, v_stack_m1B0);
    }
    v_stack_m1B0 = v_stack_m160;
loc_007E98D3:
    result = (uint16_t)((v_stack_m1E8) + 1);
    goto loc_007E97A7;
loc_007E98E0:
    local_rbx = 0;
    if (v_stack_m1B0 == 0) goto loc_007E98FE;
    result = CmpAllocateLayerInfoForKcb(v_stack_m1B0, Arg2, v_stack_m1D0, v_stack_m1B0);
    if (sign_flag) goto loc_007E9B1D;
loc_007E98FE:
    if ((*(uint16_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x42)) == 0) goto loc_007E9936;
    Arg3 = 0;
    result = CmpPromoteKey(v_stack_m120, Arg3 + 1, Arg3, v_stack_m1B0);
    if (sign_flag) goto loc_007E9B1D;
    Arg2 = 0;
    result = CmpPromoteSubtree(v_stack_m120, Arg2, Arg3, v_stack_m1B0);
    if (sign_flag) goto loc_007E9B1D;
loc_007E9936:
    a4 = 0;
    result = HvpMarkCellDirty(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x48) + 0x20), (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x48) + 0x28)), a4 + 1, a4);
    if (sign_flag) goto loc_007E9B1D;
    result = CmpGetKeyNodeForKcb(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x48), v_stack_m148, 1, a4);
    v_stack_m170 = result;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x1C)))) == -1) goto loc_007E998B;
    result = CmpMarkEntireIndexDirty(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x48) + 0x20), (uint32_t)(*(uint32_t *)(result + 0x1C)), 1, a4);
    if (sign_flag) goto loc_007E9B1D;
loc_007E998B:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m170 + 0x20)))) == -1) goto loc_007E99A7;
    result = CmpMarkEntireIndexDirty(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x48) + 0x20), (uint32_t)(*(uint32_t *)(v_stack_m170 + 0x20)), 1, a4);
    if (sign_flag) goto loc_007E9B1D;
loc_007E99A7:
    a4 = 0;
    result = HvpMarkCellDirty(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x20), (uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x28)), a4 + 1, a4);
    if (sign_flag) goto loc_007E9B1D;
    if (((uint32_t)((uint32_t)(v_stack_m1C8))) == -1) goto loc_007E99EA;
    result = CmpMarkKeyDirty(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x48) + 0x20), (uint32_t)((uint32_t)((uint32_t)(v_stack_m1C8))), 1, a4);
    if (sign_flag) goto loc_007E9B1D;
loc_007E99EA:
    if (v_stack_m1F6 != 0) goto loc_007E9AB1;
    result = CmpMarkAllChildrenDirty(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x20), (uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x28)), 1, a4);
    if (sign_flag) goto loc_007E9B1D;
loc_007E9A0C:
    result = CmpNameSize(v_stack_m1B8, (uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x28)), 1, a4);
    v_stack_m220 = v_stack_m140;
    Arg2 = (uint32_t)(((uint16_t)(result)) + (76));
    Arg3 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x28))) >> (31));
    v_stack_m228 = v_stack_m1A0;
    result = HvAllocateCell(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x20), Arg2, Arg3, v_stack_m1C0);
    if (sign_flag) goto loc_007E9B1D;
    result = CmpGetKeyNodeForKcb(*(uint64_t *)(Arg1 + 0x8), v_stack_m178, 1, v_stack_m1C0);
    *(uint64_t *)(v_stack_m1A0) = v_xmm0;
    *(uint64_t *)(v_stack_m1A0 + 0x10) = v_xmm1;
    *(uint64_t *)(v_stack_m1A0 + 0x20) = v_xmm0;
    *(uint64_t *)(v_stack_m1A0 + 0x30) = v_xmm1;
    *(uint64_t *)(v_stack_m1A0 + 0x40) = v_xmm0;
    *(uint32_t *)(v_stack_m1A0 + 0x48) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x48)));
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x20) + 0x8C)) & (1)) == 0) goto loc_007E9B61;
    result = HvpReleaseCellFlat(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x20), v_stack_m178, 1, v_stack_m1C0);
    goto loc_007E9B66;
loc_007E9AB1:
    result = CmpSubtreeEnumeratorStartForKcbStack(v_stack_mB8, v_stack_m120, 1, v_stack_m1C0);
    if (sign_flag) goto loc_007E9B1D;
loc_007E9AC8:
    result = CmpSubtreeEnumeratorAdvance(v_stack_mB8, v_stack_m120, 1, v_stack_m1C0);
    if (((uint32_t)(result)) == 0x8000001AULL) goto loc_007E9A0C;
    Arg2 = 0;
    result = CmpSubtreeEnumeratorGetCurrentKeyStacks(v_stack_mB8, Arg2, v_stack_m138, v_stack_m1C0);
    result = CmpKeyNodeStackGetEntryAtLayerHeight(v_stack_m138, *(uint16_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x42), v_stack_m138, v_stack_m1C0);
    a4 = 0;
    result = HvpMarkCellDirty(*(uint64_t *)(result), (uint32_t)(*(uint32_t *)(result + 0x8)), a4 + 1, a4);
    if (!sign_flag) goto loc_007E9AC8;
loc_007E9B18:
loc_007E9B1D:
loc_007E9B22:
loc_007E9B27:
    result = CmpSubtreeEnumeratorCleanup(v_stack_mB8, (uint32_t)(*(uint32_t *)(result + 0x8)), a4 + 1, a4);
    if (v_stack_m170 == 0) goto loc_007EA083;
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x48) + 0x20) + 0x8C)) & (1)) == 0) goto loc_007EA07E;
    result = HvpReleaseCellFlat(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x48) + 0x20), v_stack_m148, a4 + 1, a4);
    goto loc_007EA083;
loc_007E9B61:
    result = HvpReleaseCellPaged(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x48) + 0x20), v_stack_m148, a4 + 1, a4);
loc_007E9B66:
    result = CmpCopyName(v_stack_m1A0 + 76, v_stack_m1B8, a4 + 1, a4);
    *(uint16_t *)(v_stack_m1A0 + 0x48) = (uint16_t)(result);
    if (((uint16_t)(result)) >= (*(uint16_t *)(v_stack_m1B8))) goto loc_007E9B8B;
    goto loc_007E9B98;
loc_007E9B8B:
loc_007E9B98:
    result = 0;
    *(uint64_t *)(v_stack_m1A0 + 0x4) = v_stack_m1F8;
    if (v_stack_m1F6 != 0) {
    }
    if ((*(uint16_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x42)) == 0) goto loc_007E9BD8;
    result = CmpReferenceSecurityNode(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x20), (uint32_t)(*(uint32_t *)(v_stack_m1A0 + 0x2C)), a4 + 1, a4);
    if (sign_flag) goto loc_007E9B18;
    v_stack_m184 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m1A0 + 0x2C)));
loc_007E9BD8:
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x20) + 0x8C)) & (1)) == 0) goto loc_007E9BF4;
    result = HvpReleaseCellFlat(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x20), v_stack_m140, a4 + 1, a4);
    goto loc_007E9BF9;
loc_007E9BF4:
    result = HvpReleaseCellPaged(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x20), v_stack_m140, a4 + 1, a4);
loc_007E9BF9:
    result = 0;
    v_stack_m1A0 = 0;
    result = CmpGetNameControlBlock(v_stack_m1B8, v_stack_m130, a4 + 1, a4);
    v_stack_m1F0 = result;
    if (result != 0) goto loc_007E9C23;
    goto loc_007E9B1D;
loc_007E9C23:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m170 + 0x1C)))) == -1) goto loc_007E9C4B;
    Arg3 = 0;
    result = CmpDuplicateIndex(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x48) + 0x20), (uint32_t)(*(uint32_t *)(v_stack_m170 + 0x1C)), Arg3, v_stack_m1D8);
    if (sign_flag) goto loc_007E9B18;
loc_007E9C4B:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m170 + 0x20)))) == -1) goto loc_007E9C72;
    result = CmpDuplicateIndex(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x48) + 0x20), (uint32_t)(*(uint32_t *)(v_stack_m170 + 0x20)), 1, v_stack_m1D4);
    if (sign_flag) goto loc_007E9B18;
loc_007E9C72:
    if (((uint32_t)((uint32_t)(v_stack_m1C8))) == -1) goto loc_007E9CA4;
    result = ((uint32_t)((uint32_t)((uint32_t)(v_stack_m1C8)))) >> (31);
    result = CmpRemoveSubKeyFromList(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x48) + 0x20), v_stack_m1D8 + result * 4, (uint32_t)((uint32_t)((uint32_t)(v_stack_m1C8))), v_stack_m1D4);
    if ((uint8_t)(result) != 0) goto loc_007E9CA4;
loc_007E9C99:
    goto loc_007E9B18;
loc_007E9CA4:
    local_rbx = ((uint32_t)((uint32_t)((uint32_t)(v_stack_m1C0)))) >> (31);
    result = CmpAddSubKeyToList(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x48) + 0x20), v_stack_m1D8 + local_rbx * 4, (uint32_t)((uint32_t)((uint32_t)(v_stack_m1C0))), v_stack_m1D4);
    result = 0;
    if (sign_flag) goto loc_007E9B18;
    if ((*(uint16_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x42)) != 0) goto loc_007E9CF8;
    result = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x28))))) >> (31);
    result = CmpRemoveSubKeyFromList(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x48) + 0x20), v_stack_m1D8 + result * 4, (uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x28)), v_stack_m1D4);
    if ((uint8_t)(result) == 0) goto loc_007E9C99;
loc_007E9CF8:
    Arg2 = (uint32_t)((v_stack_m1D8 + result * 4) | (0xFFFFFFFFULL));
    *(uint32_t *)(v_stack_m170 + 0x1C) = (uint32_t)((uint32_t)(v_stack_m1D8));
    v_stack_m1D8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m170 + 0x1C)));
    *(uint32_t *)(v_stack_m170 + 0x20) = (uint32_t)((uint32_t)(v_stack_m1D4));
    v_stack_m1D4 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m170 + 0x20)));
    result = (uint32_t)(v_stack_m1C8);
    if (((uint32_t)((uint32_t)(v_stack_m1C8))) != ((uint32_t)(Arg2))) {
        result = ((uint32_t)(v_stack_m1C8)) >> (31);
    }
    local_rbx = 0;
    if ((*(uint16_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x42)) == 0) {
        result = *(uint32_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x28);
        result = (result) >> (31);
    }
    result = CmpCleanUpSubKeyInfo(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x48), 1, (uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x28)), v_stack_m1D4);
    if (((uint32_t)((uint16_t)((uint32_t)(*(uint32_t *)(v_stack_m170 + 0x34))))) < ((uint32_t)(*(uint16_t *)(v_stack_m1B8)))) {
        *(uint16_t *)(v_stack_m170 + 0x34) = (uint16_t)(*(uint16_t *)(v_stack_m1B8));
        *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x48) + 0xB0) = (uint16_t)(*(uint16_t *)(v_stack_m1B8));
    }
    if ((*(uint16_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x42)) != 0) goto loc_007E9D8E;
    result = HvFreeCell(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x20), (uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x28)), (uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x28)), v_stack_m1D4);
    goto loc_007E9E00;
loc_007E9D8E:
    result = CmpGetKeyNodeForKcb(*(uint64_t *)(Arg1 + 0x8), v_stack_m178, 1, v_stack_m1D4);
    Arg1 = (uint8_t)((*(uint8_t *)(result + 0xD)) & (124));
    Arg1 = (uint8_t)((Arg1) | (1));
    *(uint16_t *)(result + 0x34) = 0;
    *(uint8_t *)(result + 0xD) = (uint8_t)(Arg1);
    Arg1 = (uint32_t)((Arg1) | (0xFFFFFFFFULL));
    *(uint32_t *)(result + 0x1C) = (uint32_t)(Arg1);
    *(uint32_t *)(result + 0x20) = (uint32_t)(Arg1);
    *(uint32_t *)(result + 0x28) = (uint32_t)(Arg1);
    *(uint32_t *)(result + 0x30) = (uint32_t)(Arg1);
    *(uint64_t *)(result + 0x14) = 0;
    *(uint32_t *)(result + 0x24) = 0;
    *(uint8_t *)(result + 0x37) = 0;
    *(uint64_t *)(result + 0x38) = 0;
    *(uint32_t *)(result + 0x40) = 0;
    *(uint16_t *)(result + 0x4A) = 0;
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x20) + 0x8C)) & (1)) == 0) goto loc_007E9DFB;
    result = HvpReleaseCellFlat(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x20), v_stack_m178, 1, v_stack_m1D4);
    goto loc_007E9E00;
loc_007E9DFB:
    result = HvpReleaseCellPaged(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x20), v_stack_m178, 1, v_stack_m1D4);
loc_007E9E00:
    *(uint32_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x28) = (uint32_t)((uint32_t)(v_stack_m1C0));
    result = (uint32_t)(((uint32_t)(v_stack_m1C0)) | (0xFFFFFFFFULL));
    v_stack_m1C0 = (uint32_t)(result);
    v_stack_m184 = (uint32_t)(result);
    if ((*(uint16_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x42)) == 0) goto loc_007E9E71;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0xC0)) + 0x8)) != (*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0xC0))) goto loc_007E9F6B;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0xC0) + 0x8))) != (*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0xC0))) goto loc_007E9F6B;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0xC0) + 0x8)) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0xC0));
    Arg3 = 0;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0xC0)) + 0x8) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0xC0) + 0x8);
    result = CmpDereferenceKeyControlBlockWithLock(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0xC0) + 0x18) + 0x10), v_stack_m158, Arg3, v_stack_m1D4);
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0xC0) + 0x18) = 0;
    result = CmpCreateLayerLink(v_stack_m1B0, *(uint64_t *)(Arg1 + 0x8), Arg3, v_stack_m1D4);
loc_007E9E71:
    result = CmpRemoveKeyHash(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x20), *(uint64_t *)(Arg1 + 0x8) + 16, Arg3, v_stack_m1D4);
    *(uint32_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x10) = (uint32_t)(v_stack_m1E0);
    result = CmpInsertKeyHash(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x20), *(uint64_t *)(Arg1 + 0x8) + 16, Arg3, v_stack_m1D4);
    local_rdi = 0;
    *(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x50) = v_stack_m1F0;
    v_stack_m1F0 = *(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x50);
    result = *(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x128);
    if (*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x128) != 0) {
        result = local_rdi + 1;
    }
    if ((*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0xC8)) >= 2) {
        Arg2 = 0x624E4D43ULL;
        result = ExFreePoolWithTag(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0xC8), Arg2, Arg3, v_stack_m1D4);
    }
    *(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0xC8) = 0;
    if ((uint8_t)(v_stack_m1F6) != 0) {
        *(uint8_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x41) = 3;
    }
    result = CmpUpdateParentForEachSon(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x20), (uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x28)), Arg3, v_stack_m1D4);
    if ((uint8_t)(v_stack_m1F6) == 0) goto loc_007E9FAA;
loc_007E9F08:
    Arg1 = (v_stack_m58) + (56);
    Arg1 = (Arg1) + (0);
    result = CmpKeyEnumStackReset(Arg1, (uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x28)), Arg3, v_stack_m1D4);
    local_rbx = (0) + (408);
    local_rdi = (512) - (1);
    if (condition_is_not_equal) goto loc_007E9F08;
    v_stack_mB0 = local_rdi;
    v_stack_mB8 = (uint16_t)(local_rdi - 2);
    result = CmpResetKeyNodeStack(v_stack_mA8, (uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x28)), Arg3, v_stack_m1D4);
    result = CmpSubtreeEnumeratorBeginForKcbStack(v_stack_mB8, v_stack_m120, Arg3, v_stack_m1D4);
    result = CmpSubtreeEnumeratorAdvance(v_stack_mB8, v_stack_m120, Arg3, v_stack_m1D4);
    goto loc_007E9FA6;
loc_007E9F6B:
loc_007E9F72:
    Arg2 = 0;
    result = CmpSubtreeEnumeratorGetCurrentKeyStacks(v_stack_mB8, Arg2, v_stack_m138, v_stack_m1D4);
    result = CmpKeyNodeStackGetEntryAtLayerHeight(v_stack_m138, *(uint16_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x42), v_stack_m138, v_stack_m1D4);
    result = CmpSubtreeEnumeratorAdvance(v_stack_mB8, *(uint16_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x42), v_stack_m138, v_stack_m1D4);
loc_007E9FA6:
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)(0x8000001AULL)))) goto loc_007E9F72;
loc_007E9FAA:
    *(uint64_t *)(v_stack_m170 + 0x4) = v_stack_m1F8;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x48) + 0xA8) = v_stack_m1F8;
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x48) + 0x20) + 0x8C)) & (1)) == 0) goto loc_007E9FD1;
    result = HvpReleaseCellFlat(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x48) + 0x20), v_stack_m148, v_stack_m138, v_stack_m1D4);
    goto loc_007E9FD6;
loc_007E9FD1:
    result = HvpReleaseCellPaged(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x48) + 0x20), v_stack_m148, v_stack_m138, v_stack_m1D4);
loc_007E9FD6:
    Arg3 = 0;
    v_stack_m170 = local_rdi;
    result = CmpSearchForOpenSubKeys(*(uint64_t *)(Arg1 + 0x8), 1, Arg3, v_stack_m1D4);
    if (((uint32_t)((uint32_t)(v_stack_m1C4))) != -1) {
        Arg1 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x48) + 0x20);
        Arg3 = 0;
        result = CmpFreeKeyByCell(Arg1, (uint32_t)(v_stack_m1C4), Arg3, v_stack_m1D4);
    }
    goto loc_007E9B18;
loc_007EA011:
    goto loc_007E9B27;
loc_007EA027:
    goto loc_007E9B1D;
loc_007EA032:
    goto loc_007E9B27;
loc_007EA044:
    result = CmpLogUnsupportedOperation(24, (uint32_t)(v_stack_m1C4), Arg3, v_stack_m1D4);
    result = 0;
    goto loc_007E96E1;
loc_007EA05B:
loc_007EA061:
    goto loc_007E93DE;
loc_007EA069:
    result = 0;
    goto loc_007E9B27;
loc_007EA07E:
    result = HvpReleaseCellPaged(24, (uint32_t)(v_stack_m1C4), Arg3, v_stack_m1D4);
loc_007EA083:
    if (0 == 0) goto loc_007EA0AA;
    if (((*(uint8_t *)(v_stack_m1E0 + 0x8C)) & (1)) == 0) goto loc_007EA0A5;
    result = HvpReleaseCellFlat(v_stack_m1E0, v_stack_m168, Arg3, v_stack_m1D4);
    goto loc_007EA0AA;
loc_007EA0A5:
    result = HvpReleaseCellPaged(v_stack_m1E0, v_stack_m168, Arg3, v_stack_m1D4);
loc_007EA0AA:
    result = (uint32_t)(v_stack_m184);
    if (((uint32_t)((uint32_t)(v_stack_m184))) != -1) {
        Arg1 = *(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x20);
        Arg2 = (uint32_t)((uint32_t)(v_stack_m184));
        result = CmpDereferenceSecurityNode(Arg1, Arg2, Arg3, v_stack_m1D4);
    }
    local_rdi = 0;
    if (v_stack_m1A0 == 0) goto loc_007EA0E2;
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x20) + 0x8C)) & (1)) == 0) goto loc_007EA0DD;
    result = HvpReleaseCellFlat(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x20), v_stack_m140, Arg3, v_stack_m1D4);
    goto loc_007EA0E2;
loc_007EA0DD:
    result = HvpReleaseCellPaged(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x20), v_stack_m140, Arg3, v_stack_m1D4);
loc_007EA0E2:
    local_r12 = (uint32_t)((1) | (0xFFFFFFFFULL));
    if (((uint32_t)((uint32_t)(v_stack_m1D8))) != ((uint32_t)(local_r12))) {
        Arg1 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x48) + 0x20);
        result = CmpFreeIndexByCell(Arg1, (uint32_t)(v_stack_m1D8), Arg3, v_stack_m1D4);
    }
    if (((uint32_t)((uint32_t)(v_stack_m1D4))) != ((uint32_t)(local_r12))) {
        Arg1 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x48) + 0x20);
        result = CmpFreeIndexByCell(Arg1, (uint32_t)(v_stack_m1D4), Arg3, v_stack_m1D4);
    }
    result = (uint32_t)(v_stack_m1C0);
    if (((uint32_t)((uint32_t)(v_stack_m1C0))) != ((uint32_t)(local_r12))) {
        Arg1 = *(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x20);
        Arg2 = (uint32_t)((uint32_t)(v_stack_m1C0));
        result = HvFreeCell(Arg1, Arg2, Arg3, v_stack_m1D4);
    }
    if (0 != 0) {
        Arg1 = 0;
        result = CmpDereferenceNameControlBlockWithLock(Arg1, Arg2, Arg3, v_stack_m1D4);
    }
    result = v_stack_m1B0;
    if (v_stack_m1B0 != 0) {
        Arg3 = 0;
        Arg2 = v_stack_m158;
        Arg1 = v_stack_m1B0;
        result = CmpDereferenceKeyControlBlockWithLock(Arg1, Arg2, Arg3, v_stack_m1D4);
    }
    result = v_stack_m1A8;
    if (v_stack_m1A8 != 0) {
        Arg3 = 0;
        Arg2 = v_stack_m158;
        Arg1 = v_stack_m1A8;
        result = CmpDereferenceKeyControlBlockWithLock(Arg1, Arg2, Arg3, v_stack_m1D4);
    }
    Arg2 = 0;
    result = CmpDrainDelayDerefContext(v_stack_m158, Arg2, Arg3, v_stack_m1D4);
    if (0 != 0) {
        result = CmpUnlockRegistry(v_stack_m158, Arg2, Arg3, v_stack_m1D4);
    }
    result = CmpCleanupKcbStack(v_stack_m120, Arg2, Arg3, v_stack_m1D4);
    result = CmpCleanupKcbStack(v_stack_m100, Arg2, Arg3, v_stack_m1D4);
    result = CmpCleanupKcbStack(v_stack_mE0, Arg2, Arg3, v_stack_m1D4);
    result = CmpCleanupRollbackPacket(v_stack_m198, Arg2, Arg3, v_stack_m1D4);
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, v_stack_m1D4);
    local_rsp = (local_rsp) + (528);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007E8F48&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
