# HvpReleaseCellFlat

- RVA: `0x0085CC20`–`0x0085CC32` (길이 `18` bytes)
- VA: `0x000000014085CC20`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `6`개 명령, `18/18` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **213**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0085CC27` → [HvpGetCellContextReinitialize](HvpGetCellContextReinitialize_function_00855D40.md) (function, `0x00855D40`)

### Direct callers
- [CmDeleteLayeredKey](../../text/41/CmDeleteLayeredKey_function_0041B598.md) at `0x0041B929`
- [CmpQueryKeyDataFromKeyNodeStack](../../text/46/CmpQueryKeyDataFromKeyNodeStack_function_0046AC40.md) at `0x0046B107`
- [CmpValueEnumStackEntryCleanup](../../text/49/CmpValueEnumStackEntryCleanup_function_0049C5A4.md) at `0x0049C5CA`
- [CmpSwapValueInList](../../text/4A/CmpSwapValueInList_function_004A266C.md) at `0x004A26E7`
- [CmpDereferenceSecurityNode](../../text/4A/CmpDereferenceSecurityNode_function_004A672C.md) at `0x004A67AD`
- [CmpDereferenceSecurityNode](../../text/4A/CmpDereferenceSecurityNode_function_004A672C.md) at `0x004A67C9`
- [CmpRemoveSecurityCellList](../../text/4B/CmpRemoveSecurityCellList_function_004BC1FC.md) at `0x004BC338`
- [CmpRemoveSecurityCellList](../../text/4B/CmpRemoveSecurityCellList_function_004BC1FC.md) at `0x004BC33F`
- [CmpRemoveSecurityCellList](../../text/4B/CmpRemoveSecurityCellList_function_004BC1FC.md) at `0x004BC346`
- [CmpRemoveSecurityCellList](../../text/4B/CmpRemoveSecurityCellList_function_004BC1FC.md) at `0x004BC361`
- [CmpRemoveSecurityCellList](../../text/4B/CmpRemoveSecurityCellList_function_004BC1FC.md) at `0x004BC37C`
- [CmpRemoveSecurityCellList](../../text/4B/CmpRemoveSecurityCellList_function_004BC1FC.md) at `0x004BC397`
- [CmpCreateTombstone](../../text/66/CmpCreateTombstone_function_0066AF50.md) at `0x0066B1B7`
- [CmpCreateTombstone](../../text/66/CmpCreateTombstone_function_0066AF50.md) at `0x0066B1F3`
- [sub_006ED542](../../text/6E/Unknown_function_006ED542.md) at `0x006ED6A9`
- [CmpMarkCurrentProfileDirty](../7D/CmpMarkCurrentProfileDirty_function_007DBBAC.md) at `0x007DBCD0`
- [CmpMarkCurrentValueDirty](../7D/CmpMarkCurrentValueDirty_function_007DBD1C.md) at `0x007DBD85`
- [CmpMarkCurrentValueDirty](../7D/CmpMarkCurrentValueDirty_function_007DBD1C.md) at `0x007DBDDE`
- [CmRestoreKey](../7D/CmRestoreKey_function_007DCF04.md) at `0x007DD2B0`
- [CmRestoreKey](../7D/CmRestoreKey_function_007DCF04.md) at `0x007DD2D3`
- [CmRestoreKey](../7D/CmRestoreKey_function_007DCF04.md) at `0x007DD623`
- [CmRestoreKey](../7D/CmRestoreKey_function_007DCF04.md) at `0x007DD672`
- [CmRestoreKey](../7D/CmRestoreKey_function_007DCF04.md) at `0x007DD6E6`
- [CmRestoreKey](../7D/CmRestoreKey_function_007DCF04.md) at `0x007DD7F3`
- [CmRestoreKey](../7D/CmRestoreKey_function_007DCF04.md) at `0x007DD838`
- [CmRestoreKey](../7D/CmRestoreKey_function_007DCF04.md) at `0x007DD850`
- [CmRestoreKey](../7D/CmRestoreKey_function_007DCF04.md) at `0x007DD8DA`
- [CmRestoreKey](../7D/CmRestoreKey_function_007DCF04.md) at `0x007DD8FC`
- [CmRestoreKey](../7D/CmRestoreKey_function_007DCF04.md) at `0x007DDA10`
- [CmRestoreKey](../7D/CmRestoreKey_function_007DCF04.md) at `0x007DDB4A`
- [CmRestoreKey](../7D/CmRestoreKey_function_007DCF04.md) at `0x007DDB6B`
- [CmRestoreKey](../7D/CmRestoreKey_function_007DCF04.md) at `0x007DDB8D`
- [CmSaveMergedKeys](../7D/CmSaveMergedKeys_function_007DE040.md) at `0x007DE337`
- [CmSaveMergedKeys](../7D/CmSaveMergedKeys_function_007DE040.md) at `0x007DE371`
- [CmSaveMergedKeys](../7D/CmSaveMergedKeys_function_007DE040.md) at `0x007DE38D`
- [CmSaveMergedKeys](../7D/CmSaveMergedKeys_function_007DE040.md) at `0x007DE41B`
- [CmpLoadHiveVolatile](../7D/CmpLoadHiveVolatile_function_007DE5F0.md) at `0x007DE8DF`
- [CmpLoadHiveVolatile](../7D/CmpLoadHiveVolatile_function_007DE5F0.md) at `0x007DE984`
- [CmpRefreshHive](../7D/CmpRefreshHive_function_007DEAD0.md) at `0x007DEE84`
- [CmpRefreshHive](../7D/CmpRefreshHive_function_007DEAD0.md) at `0x007DEEA1`
- [CmpRefreshHive](../7D/CmpRefreshHive_function_007DEAD0.md) at `0x007DEF1B`
- [CmpRefreshHive](../7D/CmpRefreshHive_function_007DEAD0.md) at `0x007DEF41`
- [CmpCloneHwProfile](../7E/CmpCloneHwProfile_function_007E303C.md) at `0x007E377F`
- [CmpCloneHwProfile](../7E/CmpCloneHwProfile_function_007E303C.md) at `0x007E37AB`
- [CmRenameKey](../7E/CmRenameKey_function_007E8F48.md) at `0x007E947E`
- [CmRenameKey](../7E/CmRenameKey_function_007E8F48.md) at `0x007E9550`
- [CmRenameKey](../7E/CmRenameKey_function_007E8F48.md) at `0x007E9851`
- [CmRenameKey](../7E/CmRenameKey_function_007E8F48.md) at `0x007E9AA7`
- [CmRenameKey](../7E/CmRenameKey_function_007E8F48.md) at `0x007E9B57`
- [CmRenameKey](../7E/CmRenameKey_function_007E8F48.md) at `0x007E9BED`
- [CmRenameKey](../7E/CmRenameKey_function_007E8F48.md) at `0x007E9DF4`
- [CmRenameKey](../7E/CmRenameKey_function_007E8F48.md) at `0x007E9FCA`
- [CmRenameKey](../7E/CmRenameKey_function_007E8F48.md) at `0x007EA09E`
- [CmRenameKey](../7E/CmRenameKey_function_007E8F48.md) at `0x007EA0D6`
- [CmpAddValueKeyTombstone](../7E/CmpAddValueKeyTombstone_function_007EA488.md) at `0x007EA563`
- [CmpDoBuildVirtualStack](../7E/CmpDoBuildVirtualStack_function_007EB4C4.md) at `0x007EB8ED`
- [CmpDoBuildVirtualStack](../7E/CmpDoBuildVirtualStack_function_007EB4C4.md) at `0x007EB911`
- [CmpVirtualPathPresent](../7E/CmpVirtualPathPresent_function_007EBDB4.md) at `0x007EBE9F`
- [CmpAssignKeySecurity](../7E/CmpAssignKeySecurity_function_007EC8B0.md) at `0x007ECA08`
- [CmpCopySaclToVirtualKey](../7E/CmpCopySaclToVirtualKey_function_007ECA6C.md) at `0x007ECD4B`
- [CmpCopySaclToVirtualKey](../7E/CmpCopySaclToVirtualKey_function_007ECA6C.md) at `0x007ECD6E`
- [CmpReferenceSecurityNode](../7E/CmpReferenceSecurityNode_function_007ED6A0.md) at `0x007ED70B`
- [CmpReferenceSecurityNode](../7E/CmpReferenceSecurityNode_function_007ED6A0.md) at `0x007ED731`
- [CmpFindControlSet](../7F/CmpFindControlSet_function_007F1A34.md) at `0x007F1B15`
- [CmpFindControlSet](../7F/CmpFindControlSet_function_007F1A34.md) at `0x007F1B8D`
- [CmpFindControlSet](../7F/CmpFindControlSet_function_007F1A34.md) at `0x007F1BFE`
- [CmpFindControlSet](../7F/CmpFindControlSet_function_007F1A34.md) at `0x007F1C29`
- [CmpFindControlSet](../7F/CmpFindControlSet_function_007F1A34.md) at `0x007F1C81`
- [CmpFindControlSet](../7F/CmpFindControlSet_function_007F1A34.md) at `0x007F1CFE`
- [CmpFindControlSet](../7F/CmpFindControlSet_function_007F1A34.md) at `0x007F1DE7`
- [CmpFindControlSet](../7F/CmpFindControlSet_function_007F1A34.md) at `0x007F1E69`
- [CmpFindControlSet](../7F/CmpFindControlSet_function_007F1A34.md) at `0x007F1EE1`
- [CmpFindControlSet](../7F/CmpFindControlSet_function_007F1A34.md) at `0x007F1F29`
- [CmpFindControlSet](../7F/CmpFindControlSet_function_007F1A34.md) at `0x007F1F46`
- [CmpFindControlSet](../7F/CmpFindControlSet_function_007F1A34.md) at `0x007F1F63`
- [CmpFreeKeyValueList](../7F/CmpFreeKeyValueList_function_007F2250.md) at `0x007F22DA`
- [CmpMergeKeyValues](../7F/CmpMergeKeyValues_function_007F2304.md) at `0x007F2460`
- [CmpMergeKeyValues](../7F/CmpMergeKeyValues_function_007F2304.md) at `0x007F24E0`
- [CmpPreserveSystemHiveData](../7F/CmpPreserveSystemHiveData_function_007F2518.md) at `0x007F274C`
- [CmpPreserveSystemHiveData](../7F/CmpPreserveSystemHiveData_function_007F2518.md) at `0x007F27C6`
- [CmpPreserveSystemHiveData](../7F/CmpPreserveSystemHiveData_function_007F2518.md) at `0x007F284D`
- [CmpPreserveSystemHiveData](../7F/CmpPreserveSystemHiveData_function_007F2518.md) at `0x007F2875`
- [CmpPreserveSystemHiveData](../7F/CmpPreserveSystemHiveData_function_007F2518.md) at `0x007F28CE`
- [CmpPreserveSystemHiveData](../7F/CmpPreserveSystemHiveData_function_007F2518.md) at `0x007F2922`
- [CmpPreserveSystemHiveData](../7F/CmpPreserveSystemHiveData_function_007F2518.md) at `0x007F294E`
- [CmpPreserveSystemHiveData](../7F/CmpPreserveSystemHiveData_function_007F2518.md) at `0x007F2AF4`
- [CmpPreserveSystemHiveData](../7F/CmpPreserveSystemHiveData_function_007F2518.md) at `0x007F2B4A`
- [CmpPreserveSystemHiveData](../7F/CmpPreserveSystemHiveData_function_007F2518.md) at `0x007F2C3C`
- [CmpPreserveSystemHiveData](../7F/CmpPreserveSystemHiveData_function_007F2518.md) at `0x007F2CC1`
- [CmpPreserveSystemHiveData](../7F/CmpPreserveSystemHiveData_function_007F2518.md) at `0x007F2D20`
- [CmpPreserveSystemHiveData](../7F/CmpPreserveSystemHiveData_function_007F2518.md) at `0x007F2D5F`
- [CmpPreserveSystemHiveData](../7F/CmpPreserveSystemHiveData_function_007F2518.md) at `0x007F2D97`
- [CmpPreserveSystemHiveData](../7F/CmpPreserveSystemHiveData_function_007F2518.md) at `0x007F2DBB`
- [CmpSyncKeyValues](../7F/CmpSyncKeyValues_function_007F2DF4.md) at `0x007F304C`
- [CmpMarkAllChildrenDirty](../7F/CmpMarkAllChildrenDirty_function_007F3120.md) at `0x007F31BC`
- [CmpRemoveSubKeyCellNoCellRef](../7F/CmpRemoveSubKeyCellNoCellRef_function_007F3284.md) at `0x007F3362`
- [CmpRemoveSubKeyCellNoCellRef](../7F/CmpRemoveSubKeyCellNoCellRef_function_007F3284.md) at `0x007F3436`
- [CmpRemoveSubKeyCellNoCellRef](../7F/CmpRemoveSubKeyCellNoCellRef_function_007F3284.md) at `0x007F3480`
- [CmpRemoveSubKeyCellNoCellRef](../7F/CmpRemoveSubKeyCellNoCellRef_function_007F3284.md) at `0x007F34B9`
- [CmpRemoveSubKeyCellNoCellRef](../7F/CmpRemoveSubKeyCellNoCellRef_function_007F3284.md) at `0x007F3568`
- [CmpRemoveSubKeyCellNoCellRef](../7F/CmpRemoveSubKeyCellNoCellRef_function_007F3284.md) at `0x007F3589`
- [CmpUpdateParentForEachSon](../7F/CmpUpdateParentForEachSon_function_007F35B8.md) at `0x007F366C`
- [CmpUpdateParentForEachSon](../7F/CmpUpdateParentForEachSon_function_007F35B8.md) at `0x007F368F`
- [CmpWalkUnicodeStringPath](../7F/CmpWalkUnicodeStringPath_function_007F3704.md) at `0x007F3794`
- [CmpGetValueForAudit](../7F/CmpGetValueForAudit_function_007F37C0.md) at `0x007F38E4`
- [CmpGetValueForAudit](../7F/CmpGetValueForAudit_function_007F37C0.md) at `0x007F3900`
- [CmpDeleteTree](../7F/CmpDeleteTree_function_007F3E44.md) at `0x007F3ED0`
- [CmpDeleteTree](../7F/CmpDeleteTree_function_007F3E44.md) at `0x007F3F21`
- [CmpDeleteTree](../7F/CmpDeleteTree_function_007F3E44.md) at `0x007F3F75`
- [CmpDuplicateIndex](../84/CmpDuplicateIndex_function_008420C0.md) at `0x00842207`
- [CmpDuplicateIndex](../84/CmpDuplicateIndex_function_008420C0.md) at `0x0084222E`
- [CmpDuplicateIndex](../84/CmpDuplicateIndex_function_008420C0.md) at `0x00842299`
- [HvDuplicateCell](../84/HvDuplicateCell_function_00843238.md) at `0x00843352`
- [HvDuplicateCell](../84/HvDuplicateCell_function_00843238.md) at `0x00843359`
- [CmSetLastWriteTimeKey](../84/CmSetLastWriteTimeKey_function_00843368.md) at `0x008435DB`
- [CmAddLogForAction](../84/CmAddLogForAction_function_008445AC.md) at `0x00844A3F`
- [CmAddLogForAction](../84/CmAddLogForAction_function_008445AC.md) at `0x00844A49`
- [CmpCloneKCBValueListForTrans](../84/CmpCloneKCBValueListForTrans_function_00844D30.md) at `0x00844DFB`
- [CmSetValueKey](../84/CmSetValueKey_function_008457C0.md) at `0x008464AC`
- [CmSetValueKey](../84/CmSetValueKey_function_008457C0.md) at `0x008465AB`
- [CmSetValueKey](../84/CmSetValueKey_function_008457C0.md) at `0x0084672B`
- [CmpCompareNewValueDataAgainstKCBCache](../84/CmpCompareNewValueDataAgainstKCBCache_function_00846920.md) at `0x00846AC6`
- [CmpCompareNewValueDataAgainstKCBCache](../84/CmpCompareNewValueDataAgainstKCBCache_function_00846920.md) at `0x00846AD8`
- [CmpFindNameInListWithStatus](../84/CmpFindNameInListWithStatus_function_00846B80.md) at `0x00846D7A`
- [CmpFindNameInListWithStatus](../84/CmpFindNameInListWithStatus_function_00846B80.md) at `0x00846DFE`
- [CmQueryMultipleValueKey](../84/CmQueryMultipleValueKey_function_00846EC0.md) at `0x00847442`
- [CmQueryMultipleValueKey](../84/CmQueryMultipleValueKey_function_00846EC0.md) at `0x0084744C`
- [CmQueryMultipleValueKey](../84/CmQueryMultipleValueKey_function_00846EC0.md) at `0x00847456`
- [CmQueryMultipleValueKey](../84/CmQueryMultipleValueKey_function_00846EC0.md) at `0x008475DB`
- [CmQueryMultipleValueKey](../84/CmQueryMultipleValueKey_function_00846EC0.md) at `0x008475FF`
- [CmDeleteValueKey](../84/CmDeleteValueKey_function_008476E8.md) at `0x0084803A`
- [CmDeleteValueKey](../84/CmDeleteValueKey_function_008476E8.md) at `0x008480DA`
- [CmDeleteValueKey](../84/CmDeleteValueKey_function_008476E8.md) at `0x008480F2`
- [CmDeleteValueKey](../84/CmDeleteValueKey_function_008476E8.md) at `0x008480FC`
- [CmDeleteValueKey](../84/CmDeleteValueKey_function_008476E8.md) at `0x0084816C`
- [CmDeleteValueKey](../84/CmDeleteValueKey_function_008476E8.md) at `0x0084828E`
- [CmDeleteKey](../84/CmDeleteKey_function_00848E5C.md) at `0x00849608`
- [CmDeleteKey](../84/CmDeleteKey_function_00848E5C.md) at `0x00849612`
- [CmDeleteKey](../84/CmDeleteKey_function_00848E5C.md) at `0x00849742`
- [CmpFreeSecurityDescriptor](../84/CmpFreeSecurityDescriptor_function_00849E44.md) at `0x00849EBC`
- [CmpFreeKeyBody](../84/CmpFreeKeyBody_function_00849ECC.md) at `0x00849F5D`
- [CmpRemoveSubKey](../84/CmpRemoveSubKey_function_00849F84.md) at `0x0084A01E`
- [CmpRemoveSubKeyFromList](../84/CmpRemoveSubKeyFromList_function_0084A030.md) at `0x0084A307`
- [CmpRemoveSubKeyFromList](../84/CmpRemoveSubKeyFromList_function_0084A030.md) at `0x0084A319`
- [CmpRemoveSubKeyFromList](../84/CmpRemoveSubKeyFromList_function_0084A030.md) at `0x0084A323`
- [CmpRemoveSubKeyFromList](../84/CmpRemoveSubKeyFromList_function_0084A030.md) at `0x0084A32D`
- [CmpRemoveSubKeyFromList](../84/CmpRemoveSubKeyFromList_function_0084A030.md) at `0x0084A337`
- [CmpVirtualBranchIsReplicated](../84/CmpVirtualBranchIsReplicated_function_0084A3E0.md) at `0x0084A56D`
- [CmpFreeKeyByCell](../84/CmpFreeKeyByCell_function_0084AD70.md) at `0x0084AF47`
- [CmpFreeKeyByCell](../84/CmpFreeKeyByCell_function_0084AD70.md) at `0x0084AF51`
- [CmpFreeKeyByCell](../84/CmpFreeKeyByCell_function_0084AD70.md) at `0x0084AF65`
- [CmpFreeKeyByCell](../84/CmpFreeKeyByCell_function_0084AD70.md) at `0x0084AF85`
- [CmpFreeValue](../84/CmpFreeValue_function_0084AF98.md) at `0x0084B01E`
- [CmpFreeValue](../84/CmpFreeValue_function_0084AF98.md) at `0x0084B030`
- [CmpFreeValueData](../84/CmpFreeValueData_function_0084B040.md) at `0x0084B173`
- [CmpFreeValueData](../84/CmpFreeValueData_function_0084B040.md) at `0x0084B17D`
- [CmpFreeValueData](../84/CmpFreeValueData_function_0084B040.md) at `0x0084B198`
- [CmpMarkKeyDirty](../84/CmpMarkKeyDirty_function_0084B1FC.md) at `0x0084B4AF`
- [CmpMarkKeyDirty](../84/CmpMarkKeyDirty_function_0084B1FC.md) at `0x0084B4B9`
- [CmpMarkKeyDirty](../84/CmpMarkKeyDirty_function_0084B1FC.md) at `0x0084B4C0`
- [CmpMarkKeyDirty](../84/CmpMarkKeyDirty_function_0084B1FC.md) at `0x0084B4CE`
- [CmpMarkKeyDirty](../84/CmpMarkKeyDirty_function_0084B1FC.md) at `0x0084B529`
- [CmpSetValueKeyExisting](../84/CmpSetValueKeyExisting_function_0084B53C.md) at `0x0084B865`
- [CmpSetValueKeyExisting](../84/CmpSetValueKeyExisting_function_0084B53C.md) at `0x0084B896`
- [CmpMarkValueDataDirty](../84/CmpMarkValueDataDirty_function_0084B910.md) at `0x0084BA7A`
- [CmpMarkValueDataDirty](../84/CmpMarkValueDataDirty_function_0084B910.md) at `0x0084BA81`
- [CmpFindPathByNameEx](../84/CmpFindPathByNameEx_function_0084BAAC.md) at `0x0084BD6F`
- [CmpFindPathByNameEx](../84/CmpFindPathByNameEx_function_0084BAAC.md) at `0x0084BD82`
- [CmpSelectLeaf](../84/CmpSelectLeaf_function_0084BFB4.md) at `0x0084C24C`
- [CmpSelectLeaf](../84/CmpSelectLeaf_function_0084BFB4.md) at `0x0084C253`
- [CmpSelectLeaf](../84/CmpSelectLeaf_function_0084BFB4.md) at `0x0084C25D`
- [CmpSelectLeaf](../84/CmpSelectLeaf_function_0084BFB4.md) at `0x0084C267`
- [CmpSelectLeaf](../84/CmpSelectLeaf_function_0084BFB4.md) at `0x0084C271`
- [CmpSelectLeaf](../84/CmpSelectLeaf_function_0084BFB4.md) at `0x0084C2CC`
- [CmpSelectLeaf](../84/CmpSelectLeaf_function_0084BFB4.md) at `0x0084C2DB`
- [CmpSelectLeaf](../84/CmpSelectLeaf_function_0084BFB4.md) at `0x0084C2FA`
- [CmpMarkIndexDirty](../84/CmpMarkIndexDirty_function_0084C30C.md) at `0x0084C484`
- [CmpMarkIndexDirty](../84/CmpMarkIndexDirty_function_0084C30C.md) at `0x0084C48B`
- [CmpCleanUpSubKeyInfo](../84/CmpCleanUpSubKeyInfo_function_0084C6F4.md) at `0x0084C793`
- [CmpAddSubKeyEx](../84/CmpAddSubKeyEx_function_0084C940.md) at `0x0084CBF0`
- [CmpAddSubKeyEx](../84/CmpAddSubKeyEx_function_0084C940.md) at `0x0084CBFA`
- [CmpAddSubKeyEx](../84/CmpAddSubKeyEx_function_0084C940.md) at `0x0084CC04`
- [CmpAddSubKeyEx](../84/CmpAddSubKeyEx_function_0084C940.md) at `0x0084CC92`
- [CmpAddSubKeyEx](../84/CmpAddSubKeyEx_function_0084C940.md) at `0x0084CC99`
- [CmpVEExecuteRealStoreParseLogic](../84/CmpVEExecuteRealStoreParseLogic_function_0084CCD4.md) at `0x0084CF47`
- [CmpVEExecuteRealStoreParseLogic](../84/CmpVEExecuteRealStoreParseLogic_function_0084CCD4.md) at `0x0084CF70`
- [CmpAddSubKeyToList](../84/CmpAddSubKeyToList_function_0084D644.md) at `0x0084D88C`
- [CmpAddSubKeyToList](../84/CmpAddSubKeyToList_function_0084D644.md) at `0x0084D896`
- [CmpAddSubKeyToList](../84/CmpAddSubKeyToList_function_0084D644.md) at `0x0084D8A0`
- [sub_0084E7D5](../84/Unknown_function_0084E7D5.md) at `0x0084E862`
- [sub_0084E7D5](../84/Unknown_function_0084E7D5.md) at `0x0084E86C`
- [CmpQueryKeyDataFromNode](../84/CmpQueryKeyDataFromNode_function_0084EAE0.md) at `0x0084EF4B`
- [CmpQueryKeyDataFromNode](../84/CmpQueryKeyDataFromNode_function_0084EAE0.md) at `0x0084F180`
- [CmpFindSubKeyByNumberEx](../84/CmpFindSubKeyByNumberEx_function_0084F1A0.md) at `0x0084F55E`
- [CmpFindSubKeyByNumberEx](../84/CmpFindSubKeyByNumberEx_function_0084F1A0.md) at `0x0084F568`
- [CmpFindSubKeyByNumberEx](../84/CmpFindSubKeyByNumberEx_function_0084F1A0.md) at `0x0084F575`
- [CmpFindSubKeyByNumberEx](../84/CmpFindSubKeyByNumberEx_function_0084F1A0.md) at `0x0084F80C`
- [CmpFindSubKeyByNumberEx](../84/CmpFindSubKeyByNumberEx_function_0084F1A0.md) at `0x0084F816`
- [CmpFindSubKeyByNumberEx](../84/CmpFindSubKeyByNumberEx_function_0084F1A0.md) at `0x0084F820`
- [CmpFindSubKeyByNumberEx](../84/CmpFindSubKeyByNumberEx_function_0084F1A0.md) at `0x0084F87C`
- [CmpCreateKeyControlBlock](CmpCreateKeyControlBlock_function_00851DB0.md) at `0x008525C2`
- [CmpCreateKeyControlBlock](CmpCreateKeyControlBlock_function_00851DB0.md) at `0x008525E7`
- [CmpCreateKeyControlBlock](CmpCreateKeyControlBlock_function_00851DB0.md) at `0x008525F1`
- [CmpFindSubKeyByNameWithStatus](CmpFindSubKeyByNameWithStatus_function_00852770.md) at `0x00852AA7`
- [CmpFindSubKeyByNameWithStatus](CmpFindSubKeyByNameWithStatus_function_00852770.md) at `0x00852B2E`
- [CmpFindSubKeyByNameWithStatus](CmpFindSubKeyByNameWithStatus_function_00852770.md) at `0x00852B49`
- [CmpFindSubKeyByNameWithStatus](CmpFindSubKeyByNameWithStatus_function_00852770.md) at `0x00852B8C`
- [CmpWalkOneLevel](CmpWalkOneLevel_function_00852BA0.md) at `0x0085337A`
- [CmpWalkOneLevel](CmpWalkOneLevel_function_00852BA0.md) at `0x008536B7`
- [CmpWalkOneLevel](CmpWalkOneLevel_function_00852BA0.md) at `0x00853750`
- [CmpWalkOneLevel](CmpWalkOneLevel_function_00852BA0.md) at `0x008538D4`
- [CmpWalkOneLevel](CmpWalkOneLevel_function_00852BA0.md) at `0x008538DE`
- [CmpWalkOneLevel](CmpWalkOneLevel_function_00852BA0.md) at `0x0085394E`
- [sub_0085416A](Unknown_function_0085416A.md) at `0x0085466D`
- [sub_0085416A](Unknown_function_0085416A.md) at `0x00854685`
- [sub_0085416A](Unknown_function_0085416A.md) at `0x008546E6`
- [sub_0085416A](Unknown_function_0085416A.md) at `0x008546F0`
- [sub_0085416A](Unknown_function_0085416A.md) at `0x00854707`
- [sub_00854F9C](Unknown_function_00854F9C.md) at `0x00854FC6`
- [sub_00855472](Unknown_function_00855472.md) at `0x008557B5`
- [sub_00855472](Unknown_function_00855472.md) at `0x008557FD`
- [sub_00855472](Unknown_function_00855472.md) at `0x00855807`
- [sub_00855C1A](Unknown_function_00855C1A.md) at `0x00855C24`
- [sub_00855ECF](Unknown_function_00855ECF.md) at `0x00855EDE`
- [sub_00856008](Unknown_function_00856008.md) at `0x00856150`
- [sub_00856607](Unknown_function_00856607.md) at `0x00856607`
- [CmpQueryKeyValueData](CmpQueryKeyValueData_function_00856650.md) at `0x00856AAB`
- [sub_00857051](Unknown_function_00857051.md) at `0x00857051`
- [sub_0085705E](Unknown_function_0085705E.md) at `0x0085705E`
- [sub_00857065](Unknown_function_00857065.md) at `0x00857065`
- [CmpGetSymbolicLinkTarget](CmpGetSymbolicLinkTarget_function_008570A0.md) at `0x00857636`
- [sub_00857ED3](Unknown_function_00857ED3.md) at `0x00857ED3`
- [sub_00857ED3](Unknown_function_00857ED3.md) at `0x00857EDD`
- [sub_00857EE7](Unknown_function_00857EE7.md) at `0x00857EE7`
- [sub_00857EF1](Unknown_function_00857EF1.md) at `0x00857EFE`
- [sub_00857F4E](Unknown_function_00857F4E.md) at `0x00857F4E`
- [sub_008581ED](Unknown_function_008581ED.md) at `0x008581ED`
- [CmQueryKey](CmQueryKey_function_00858240.md) at `0x00858780`
- [CmpQueryKeyData](CmpQueryKeyData_function_00858E70.md) at `0x00858F52`
- [CmpQueryKeyDataFromCache](CmpQueryKeyDataFromCache_function_00858F70.md) at `0x008591FB`
- [CmpQueryKeyDataFromCache](CmpQueryKeyDataFromCache_function_00858F70.md) at `0x00859393`
- [HvMarkCellDirty](HvMarkCellDirty_function_00859758.md) at `0x0085985E`
- [HvpFindFreeCell](HvpFindFreeCell_function_00859920.md) at `0x00859C65`
- [HvAllocateCell](HvAllocateCell_function_00859C94.md) at `0x00859F45`
- [sub_0085A240](Unknown_function_0085A240.md) at `0x0085A256`
- [CmpCopyCell](CmpCopyCell_function_0085A608.md) at `0x0085A716`
- [CmpCopyCell](CmpCopyCell_function_0085A608.md) at `0x0085A71D`
- [HvpDelistFreeCell](HvpDelistFreeCell_function_0085A99C.md) at `0x0085AA42`
- [CmpAddValueKeyNew](CmpAddValueKeyNew_function_0085AA58.md) at `0x0085ABA9`
- [CmpCopyKeyPartial](CmpCopyKeyPartial_function_0085AFF4.md) at `0x0085B398`
- [CmpCopyKeyPartial](CmpCopyKeyPartial_function_0085AFF4.md) at `0x0085B3A2`
- [CmpCopyKeyPartial](CmpCopyKeyPartial_function_0085AFF4.md) at `0x0085B3AC`
- [CmpAddValueToListEx](CmpAddValueToListEx_function_0085B460.md) at `0x0085B5B5`
- [HvReallocateCell](HvReallocateCell_function_0085B5D0.md) at `0x0085B755`
- [HvReallocateCell](HvReallocateCell_function_0085B5D0.md) at `0x0085B75F`
- [HvReallocateCell](HvReallocateCell_function_0085B5D0.md) at `0x0085B78A`
- [CmpCopyValue](CmpCopyValue_function_0085B798.md) at `0x0085BA19`
- [CmpCopyValue](CmpCopyValue_function_0085B798.md) at `0x0085BA23`
- [CmpCopyValue](CmpCopyValue_function_0085B798.md) at `0x0085BA2D`
- [CmpCopyValue](CmpCopyValue_function_0085B798.md) at `0x0085BA37`
- [CmpCopyValue](CmpCopyValue_function_0085B798.md) at `0x0085BA41`
- [CmpCopyValue](CmpCopyValue_function_0085B798.md) at `0x0085BAF0`
- [CmpCopyValue](CmpCopyValue_function_0085B798.md) at `0x0085BB0E`
- [CmpAddToLeaf](CmpAddToLeaf_function_0085BC2C.md) at `0x0085BF1F`
- [CmpAddToLeaf](CmpAddToLeaf_function_0085BC2C.md) at `0x0085BF33`
- [CmpAddToLeaf](CmpAddToLeaf_function_0085BC2C.md) at `0x0085BF4E`
- [CmpCopySyncTree2](CmpCopySyncTree2_function_0085BF78.md) at `0x0085C38F`
- [CmpCopySyncTree2](CmpCopySyncTree2_function_0085BF78.md) at `0x0085C5D6`
- [CmpCopySyncTree2](CmpCopySyncTree2_function_0085BF78.md) at `0x0085C5E0`
- [CmpCopySyncTree2](CmpCopySyncTree2_function_0085BF78.md) at `0x0085C66D`
- [CmpCopySyncTree2](CmpCopySyncTree2_function_0085BF78.md) at `0x0085C6D9`
- [CmpCopySyncTree2](CmpCopySyncTree2_function_0085BF78.md) at `0x0085C756`
- [CmpCopySyncTree2](CmpCopySyncTree2_function_0085BF78.md) at `0x0085C760`
- [CmpCopySyncTree2](CmpCopySyncTree2_function_0085BF78.md) at `0x0085C76A`
- [CmpCopySyncTree2](CmpCopySyncTree2_function_0085BF78.md) at `0x0085C774`
- [CmpCopySyncTree2](CmpCopySyncTree2_function_0085BF78.md) at `0x0085C77B`
- [CmpCopySyncTree2](CmpCopySyncTree2_function_0085BF78.md) at `0x0085C8C0`
- [CmpCopySyncTree2](CmpCopySyncTree2_function_0085BF78.md) at `0x0085C8DF`
- [CmpCopySyncTree2](CmpCopySyncTree2_function_0085BF78.md) at `0x0085C8FD`
- [sub_0085CABE](Unknown_function_0085CABE.md) at `0x0085CABE`
- [sub_0085CACA](Unknown_function_0085CACA.md) at `0x0085CACA`
- [sub_0085CAD4](Unknown_function_0085CAD4.md) at `0x0085CAE5`
- [CmpCompareInIndex](CmpCompareInIndex_function_0085CC40.md) at `0x0085D0DB`
- [CmpCompareInIndex](CmpCompareInIndex_function_0085CC40.md) at `0x0085D0F3`
- [CmpFindSubKeyInRoot](CmpFindSubKeyInRoot_function_0085D890.md) at `0x0085E087`
- [CmpFindSubKeyInRoot](CmpFindSubKeyInRoot_function_0085D890.md) at `0x0085E0A7`
- [CmpFindSubKeyInRoot](CmpFindSubKeyInRoot_function_0085D890.md) at `0x0085E0BD`
- [CmpFindSubKeyInRoot](CmpFindSubKeyInRoot_function_0085D890.md) at `0x0085E0E8`
- [CmpFindSubKeyInRoot](CmpFindSubKeyInRoot_function_0085D890.md) at `0x0085E0F2`
- [CmpFindSubKeyInRoot](CmpFindSubKeyInRoot_function_0085D890.md) at `0x0085E111`
- [sub_0085E997](Unknown_function_0085E997.md) at `0x0085E997`
- [CmpDoParseKey](CmpDoParseKey_function_0085F750.md) at `0x0086183B`
- [CmpRebuildKcbCache](../87/CmpRebuildKcbCache_function_00874DF8.md) at `0x00874EA4`
- [CmpClearKeyAccessBits](../87/CmpClearKeyAccessBits_function_0087BB5C.md) at `0x0087BC91`
- [CmpClearKeyAccessBits](../87/CmpClearKeyAccessBits_function_0087BB5C.md) at `0x0087BCC7`
- [CmpConcatenateValueLists](../8B/CmpConcatenateValueLists_function_008B0ECC.md) at `0x008B102F`
- [CmpConcatenateValueLists](../8B/CmpConcatenateValueLists_function_008B0ECC.md) at `0x008B1036`
- [CmpFullPromoteSingleKeyFromKeyNodeStacks](../8B/CmpFullPromoteSingleKeyFromKeyNodeStacks_function_008B1A40.md) at `0x008B1E23`
- [CmpValueEnumStackAdvance](../8B/CmpValueEnumStackAdvance_function_008B256C.md) at `0x008B26AE`
- [CmpValueEnumStackAdvance](../8B/CmpValueEnumStackAdvance_function_008B256C.md) at `0x008B26C2`
- [CmEnumerateValueFromLayeredKey](../8B/CmEnumerateValueFromLayeredKey_function_008B31FC.md) at `0x008B353E`
- [CmEnumerateValueFromLayeredKey](../8B/CmEnumerateValueFromLayeredKey_function_008B31FC.md) at `0x008B3548`
- [CmEnumerateValueFromLayeredKey](../8B/CmEnumerateValueFromLayeredKey_function_008B31FC.md) at `0x008B3552`
- [CmEnumerateValueFromLayeredKey](../8B/CmEnumerateValueFromLayeredKey_function_008B31FC.md) at `0x008B355C`
- [NtEnumerateValueKey](../8B/NtEnumerateValueKey_function_008B3B50.md) at `0x008B44F4`
- [NtEnumerateValueKey](../8B/NtEnumerateValueKey_function_008B3B50.md) at `0x008B44FE`
- [CmpKeyEnumStackEntryNotifyPromotion](../94/CmpKeyEnumStackEntryNotifyPromotion_function_00944B74.md) at `0x00944CA1`
- [CmpKeyEnumStackEntryNotifyPromotion](../94/CmpKeyEnumStackEntryNotifyPromotion_function_00944B74.md) at `0x00944CCE`
- [CmpCheckKeyNodeStackAccess](../94/CmpCheckKeyNodeStackAccess_function_009459AC.md) at `0x00945A6A`
- [CmpCopyMergeOfLayeredKeyNode](../94/CmpCopyMergeOfLayeredKeyNode_function_00945A78.md) at `0x00945CCA`
- [CmpCopyMergeOfLayeredKeyNode](../94/CmpCopyMergeOfLayeredKeyNode_function_00945A78.md) at `0x00945CD1`
- [CmpEnumerateLayeredKey](../94/CmpEnumerateLayeredKey_function_00945E58.md) at `0x0094642A`
- [CmpEnumerateLayeredKey](../94/CmpEnumerateLayeredKey_function_00945E58.md) at `0x00946434`
- [CmpKeyNodeStackEntryCleanup](../94/CmpKeyNodeStackEntryCleanup_function_00946AEC.md) at `0x00946B12`
- [CmpKeyEnumStackEntryCleanup](../94/CmpKeyEnumStackEntryCleanup_function_00946B20.md) at `0x00946BBA`
- [CmpKeyEnumStackEntryCleanup](../94/CmpKeyEnumStackEntryCleanup_function_00946B20.md) at `0x00946BC1`
- [CmpKeyEnumStackEntryCleanup](../94/CmpKeyEnumStackEntryCleanup_function_00946B20.md) at `0x00946BC8`
- [CmpKeyEnumStackEntryAdvance](../94/CmpKeyEnumStackEntryAdvance_function_00946BD8.md) at `0x00946CF6`
- [CmpDoFindSubKeyByNumber](../94/CmpDoFindSubKeyByNumber_function_00946F60.md) at `0x00947067`
- [CmpDoFindSubKeyByNumber](../94/CmpDoFindSubKeyByNumber_function_00946F60.md) at `0x00947082`
- [CmpCheckSecurityCellAccess](../94/CmpCheckSecurityCellAccess_function_009470C0.md) at `0x00947148`
- [CmpCreateChild](../94/CmpCreateChild_function_0094817C.md) at `0x00948A34`
- [CmpCreateChild](../94/CmpCreateChild_function_0094817C.md) at `0x00948A3E`
- [CmpCreateChild](../94/CmpCreateChild_function_0094817C.md) at `0x00948E20`
- [CmpCreateChild](../94/CmpCreateChild_function_0094817C.md) at `0x00949178`
- [CmpGetSecurityDescriptorNodeEx](../94/CmpGetSecurityDescriptorNodeEx_function_00949268.md) at `0x00949390`
- [CmpGetSecurityDescriptorNodeEx](../94/CmpGetSecurityDescriptorNodeEx_function_00949268.md) at `0x00949452`
- [CmpSetSecurityDescriptorInfo](../94/CmpSetSecurityDescriptorInfo_function_00949688.md) at `0x00949B39`
- [CmpSetSecurityDescriptorInfo](../94/CmpSetSecurityDescriptorInfo_function_00949688.md) at `0x00949B43`
- [CmpSetSecurityDescriptorInfo](../94/CmpSetSecurityDescriptorInfo_function_00949688.md) at `0x00949B4D`
- [CmpSetSecurityDescriptorInfo](../94/CmpSetSecurityDescriptorInfo_function_00949688.md) at `0x00949C65`
- [CmpSetSecurityDescriptorInfo](../94/CmpSetSecurityDescriptorInfo_function_00949688.md) at `0x00949C6F`
- [CmpSetSecurityDescriptorInfo](../94/CmpSetSecurityDescriptorInfo_function_00949688.md) at `0x00949DF2`
- [CmpSetKeySecurity](../94/CmpSetKeySecurity_function_0094A124.md) at `0x0094A6E1`
- [CmpUndoDeleteKeyForTrans](../94/CmpUndoDeleteKeyForTrans_function_0094A728.md) at `0x0094AB50`
- [CmpUndoDeleteKeyForTrans](../94/CmpUndoDeleteKeyForTrans_function_0094A728.md) at `0x0094AB5A`
- [CmpUndoDeleteKeyForTrans](../94/CmpUndoDeleteKeyForTrans_function_0094A728.md) at `0x0094AB64`
- [CmpUndoDeleteKeyForTrans](../94/CmpUndoDeleteKeyForTrans_function_0094A728.md) at `0x0094AC44`
- [CmpLightWeightPrepareSetSecDescUoW](../94/CmpLightWeightPrepareSetSecDescUoW_function_0094B098.md) at `0x0094B302`
- [CmpLightWeightPrepareSetSecDescUoW](../94/CmpLightWeightPrepareSetSecDescUoW_function_0094B098.md) at `0x0094B30C`
- [CmpLightWeightPrepareSetSecDescUoW](../94/CmpLightWeightPrepareSetSecDescUoW_function_0094B098.md) at `0x0094B344`
- [CmpLightWeightPrepareSetSecDescUoW](../94/CmpLightWeightPrepareSetSecDescUoW_function_0094B098.md) at `0x0094B362`
- [CmpLightWeightCommitSetSecDescUoW](../94/CmpLightWeightCommitSetSecDescUoW_function_0094B4AC.md) at `0x0094B5C1`
- [CmpValidateHiveSecurityDescriptors](../96/CmpValidateHiveSecurityDescriptors_function_0096DAFC.md) at `0x0096DD87`
- [CmpValidateHiveSecurityDescriptors](../96/CmpValidateHiveSecurityDescriptors_function_0096DAFC.md) at `0x0096DDF4`
- [CmpValidateHiveSecurityDescriptors](../96/CmpValidateHiveSecurityDescriptors_function_0096DAFC.md) at `0x0096DDFE`
- [CmpValidateHiveSecurityDescriptors](../96/CmpValidateHiveSecurityDescriptors_function_0096DAFC.md) at `0x0096DEE4`
- [CmpValidateHiveSecurityDescriptors](../96/CmpValidateHiveSecurityDescriptors_function_0096DAFC.md) at `0x0096DF03`
- [CmpInsertSecurityCellList](../96/CmpInsertSecurityCellList_function_0096DF40.md) at `0x0096E1CF`
- [CmpInsertSecurityCellList](../96/CmpInsertSecurityCellList_function_0096DF40.md) at `0x0096E1D9`
- [CmpInsertSecurityCellList](../96/CmpInsertSecurityCellList_function_0096DF40.md) at `0x0096E1E3`
- [CmpInsertSecurityCellList](../96/CmpInsertSecurityCellList_function_0096DF40.md) at `0x0096E1ED`
- [CmpInsertSecurityCellList](../96/CmpInsertSecurityCellList_function_0096DF40.md) at `0x0096E1F7`
- [CmpAddSecurityCellToCache](../96/CmpAddSecurityCellToCache_function_0096E228.md) at `0x0096E46F`
- [CmpAddSecurityCellToCache](../96/CmpAddSecurityCellToCache_function_0096E228.md) at `0x0096E479`
- [CmpCheckLeaf](../96/CmpCheckLeaf_function_0096E5BC.md) at `0x0096E733`
- [CmpCheckLeaf](../96/CmpCheckLeaf_function_0096E5BC.md) at `0x0096E77B`
- [CmpCheckAndFixSecurityCellsRefcount](../96/CmpCheckAndFixSecurityCellsRefcount_function_0096E7FC.md) at `0x0096E92C`
- [CmpCheckAndFixSecurityCellsRefcount](../96/CmpCheckAndFixSecurityCellsRefcount_function_0096E7FC.md) at `0x0096E937`
- [CmpCheckAndFixSecurityCellsRefcount](../96/CmpCheckAndFixSecurityCellsRefcount_function_0096E7FC.md) at `0x0096E980`
- [sub_0096E9E9](../96/Unknown_function_0096E9E9.md) at `0x0096ECB5`
- [sub_0096E9E9](../96/Unknown_function_0096E9E9.md) at `0x0096ECC2`
- [sub_0096E9E9](../96/Unknown_function_0096E9E9.md) at `0x0096ECD7`
- [sub_0096E9E9](../96/Unknown_function_0096E9E9.md) at `0x0096ECF0`
- [CmpCheckKey](../96/CmpCheckKey_function_0096EE2C.md) at `0x0096F8B6`
- [CmpCheckKey](../96/CmpCheckKey_function_0096EE2C.md) at `0x0096FA2F`
- [CmpCheckKey](../96/CmpCheckKey_function_0096EE2C.md) at `0x0096FA39`
- [CmpCheckKey](../96/CmpCheckKey_function_0096EE2C.md) at `0x0096FAB7`
- [CmpCheckKey](../96/CmpCheckKey_function_0096EE2C.md) at `0x0096FBF9`
- [CmpCheckKey](../96/CmpCheckKey_function_0096EE2C.md) at `0x0096FD62`
- [CmpCheckKey](../96/CmpCheckKey_function_0096EE2C.md) at `0x009703FB`
- [CmpCheckKey](../96/CmpCheckKey_function_0096EE2C.md) at `0x00970719`
- [CmpCheckKey](../96/CmpCheckKey_function_0096EE2C.md) at `0x0097073D`
- [CmpCheckKey](../96/CmpCheckKey_function_0096EE2C.md) at `0x00970747`
- [CmpCheckKey](../96/CmpCheckKey_function_0096EE2C.md) at `0x00970751`
- [CmpCheckKey](../96/CmpCheckKey_function_0096EE2C.md) at `0x0097075B`
- [CmpCheckKey](../96/CmpCheckKey_function_0096EE2C.md) at `0x00970765`
- [CmpCheckKey](../96/CmpCheckKey_function_0096EE2C.md) at `0x0097076F`
- [CmpCheckKey](../96/CmpCheckKey_function_0096EE2C.md) at `0x00970794`
- [CmpCheckKey](../96/CmpCheckKey_function_0096EE2C.md) at `0x0097079E`
- [CmpCheckKey](../96/CmpCheckKey_function_0096EE2C.md) at `0x009707A8`
- [CmpCheckKey](../96/CmpCheckKey_function_0096EE2C.md) at `0x009707E8`
- [CmpCheckKey](../96/CmpCheckKey_function_0096EE2C.md) at `0x0097080D`
- [CmpCheckKey](../96/CmpCheckKey_function_0096EE2C.md) at `0x00970817`
- [CmpCheckKey](../96/CmpCheckKey_function_0096EE2C.md) at `0x00970957`
- [CmpCheckKey](../96/CmpCheckKey_function_0096EE2C.md) at `0x009709E2`
- [CmpCheckKey](../96/CmpCheckKey_function_0096EE2C.md) at `0x00970A40`
- [CmpCheckKey](../96/CmpCheckKey_function_0096EE2C.md) at `0x00970A6B`
- [CmpCheckKey](../96/CmpCheckKey_function_0096EE2C.md) at `0x00970A96`
- [sub_00970E3F](../97/Unknown_function_00970E3F.md) at `0x00970E3F`
- [sub_00970E46](../97/Unknown_function_00970E46.md) at `0x00970E46`
- [CmpCheckValueList](../97/CmpCheckValueList_function_00970F6C.md) at `0x00971472`
- [CmpCheckValueList](../97/CmpCheckValueList_function_00970F6C.md) at `0x00971574`
- [CmpCheckValueList](../97/CmpCheckValueList_function_00970F6C.md) at `0x0097162E`
- [CmpCheckValueList](../97/CmpCheckValueList_function_00970F6C.md) at `0x00971638`
- [CmpCheckValueList](../97/CmpCheckValueList_function_00970F6C.md) at `0x009717B1`
- [CmpCheckValueList](../97/CmpCheckValueList_function_00970F6C.md) at `0x00971B05`
- [CmpCheckValueList](../97/CmpCheckValueList_function_00970F6C.md) at `0x00971B7C`
- [CmpCheckValueList](../97/CmpCheckValueList_function_00970F6C.md) at `0x00971B90`
- [CmpCheckValueList](../97/CmpCheckValueList_function_00970F6C.md) at `0x00971BB0`
- [CmpCheckValueList](../97/CmpCheckValueList_function_00970F6C.md) at `0x00971BBA`
- [CmpCheckValueList](../97/CmpCheckValueList_function_00970F6C.md) at `0x00971BC4`
- [CmpCheckValueList](../97/CmpCheckValueList_function_00970F6C.md) at `0x00971BCE`
- [CmpCheckValueList](../97/CmpCheckValueList_function_00970F6C.md) at `0x00971BD8`
- [CmpCheckValueList](../97/CmpCheckValueList_function_00970F6C.md) at `0x00971BE2`
- [CmSetKeyFlags](../9A/CmSetKeyFlags_function_009AEEA4.md) at `0x009AF259`
- [CmpLightWeightPrepareSetValueKeyUoW](../A0/CmpLightWeightPrepareSetValueKeyUoW_function_00A0EF28.md) at `0x00A0F130`
- [CmpLightWeightPrepareSetValueKeyUoW](../A0/CmpLightWeightPrepareSetValueKeyUoW_function_00A0EF28.md) at `0x00A0F13A`
- [CmpLightWeightPrepareSetValueKeyUoW](../A0/CmpLightWeightPrepareSetValueKeyUoW_function_00A0EF28.md) at `0x00A0F278`
- [CmpLightWeightPrepareSetValueKeyUoW](../A0/CmpLightWeightPrepareSetValueKeyUoW_function_00A0EF28.md) at `0x00A0F282`
- [CmpLightWeightPrepareDeleteValueKeyUoW](../A0/CmpLightWeightPrepareDeleteValueKeyUoW_function_00A0F3D8.md) at `0x00A0F609`
- [CmpLightWeightPrepareDeleteValueKeyUoW](../A0/CmpLightWeightPrepareDeleteValueKeyUoW_function_00A0F3D8.md) at `0x00A0F613`
- [CmpRemoveValueFromList](../A0/CmpRemoveValueFromList_function_00A0F6D4.md) at `0x00A0F7D5`
- [CmpRemoveValueFromList](../A0/CmpRemoveValueFromList_function_00A0F6D4.md) at `0x00A0F7DC`
- [CmpLightWeightCreateSetValueData](../A0/CmpLightWeightCreateSetValueData_function_00A0F7EC.md) at `0x00A0F906`
- [CmpSetValueDataNew](../A2/CmpSetValueDataNew_function_00A26550.md) at `0x00A26772`
- [CmpSetValueDataNew](../A2/CmpSetValueDataNew_function_00A26550.md) at `0x00A2677C`
- [CmpSetValueDataNew](../A2/CmpSetValueDataNew_function_00A26550.md) at `0x00A267EA`
- [CmpSetValueDataNew](../A2/CmpSetValueDataNew_function_00A26550.md) at `0x00A267F1`
- [CmpSortedValueEnumStackEntryCleanup](../A3/CmpSortedValueEnumStackEntryCleanup_function_00A310A0.md) at `0x00A310FA`
- [CmpSortedValueEnumStackEntryStart](../A3/CmpSortedValueEnumStackEntryStart_function_00A31110.md) at `0x00A31276`
- [CmpMarkIndexDirtyInStorageType](../A3/CmpMarkIndexDirtyInStorageType_function_00A325B0.md) at `0x00A3278E`
- [CmpMarkIndexDirtyInStorageType](../A3/CmpMarkIndexDirtyInStorageType_function_00A325B0.md) at `0x00A32798`
- [CmpLightWeightCommitDeleteValueKeyUoW](../A3/CmpLightWeightCommitDeleteValueKeyUoW_function_00A39E54.md) at `0x00A39F39`
- [CmpLightWeightCommitSetValueKeyUoW](../A3/CmpLightWeightCommitSetValueKeyUoW_function_00A39FA0.md) at `0x00A3A0EA`
- [CmpLightWeightCommitRecreateKeyUoW](../A5/CmpLightWeightCommitRecreateKeyUoW_function_00A543CC.md) at `0x00A5444A`
- [CmpLightWeightPrepareDeleteKeyUoW](../A5/CmpLightWeightPrepareDeleteKeyUoW_function_00A54494.md) at `0x00A545EA`
- [CmpLightWeightCommitDeleteKeyUoW](../A5/CmpLightWeightCommitDeleteKeyUoW_function_00A54610.md) at `0x00A5479C`
- [CmpLightWeightPrepareAddKeyUoW](../A5/CmpLightWeightPrepareAddKeyUoW_function_00A547FC.md) at `0x00A54A3C`
- [CmpLightWeightPrepareAddKeyUoW](../A5/CmpLightWeightPrepareAddKeyUoW_function_00A547FC.md) at `0x00A54A8F`
- [CmpLightWeightPrepareAddKeyUoW](../A5/CmpLightWeightPrepareAddKeyUoW_function_00A547FC.md) at `0x00A54AAE`
- [CmpLightWeightDuplicateParentLists](../A5/CmpLightWeightDuplicateParentLists_function_00A54BB4.md) at `0x00A54C91`
- [CmpLightWeightCommitAddKeyUoW](../A5/CmpLightWeightCommitAddKeyUoW_function_00A54CA8.md) at `0x00A54E84`
- [CmpLightWeightCommitAddKeyUoW](../A5/CmpLightWeightCommitAddKeyUoW_function_00A54CA8.md) at `0x00A54E8B`
- [CmpLightWeightSwapParentSubKeyList](../A5/CmpLightWeightSwapParentSubKeyList_function_00A54F3C.md) at `0x00A54FEA`
- [CmpLightWeightPrepareSetKeyUserFlags](../A5/CmpLightWeightPrepareSetKeyUserFlags_function_00A553FC.md) at `0x00A55482`
- [CmpLightWeightCommitSetUserFlagsUoW](../A5/CmpLightWeightCommitSetUserFlagsUoW_function_00A5FB7C.md) at `0x00A5FC37`
- [CmpUpdateHiveRootCellFlags](../A6/CmpUpdateHiveRootCellFlags_function_00A6B124.md) at `0x00A6B1CD`
- [CmpCheckKeyAccess](../A6/CmpCheckKeyAccess_function_00A6DE7C.md) at `0x00A6DF1C`
- [CmpMarkKeyParentDirty](../A7/CmpMarkKeyParentDirty_function_00A749E8.md) at `0x00A74A8B`
- [CmpSetValueDataExisting](../A7/CmpSetValueDataExisting_function_00A79260.md) at `0x00A7940E`
- [CmpSetValueDataExisting](../A7/CmpSetValueDataExisting_function_00A79260.md) at `0x00A79418`
- [CmpSetValueDataExisting](../A7/CmpSetValueDataExisting_function_00A79260.md) at `0x00A7941F`
- [CmpSetValueDataExisting](../A7/CmpSetValueDataExisting_function_00A79260.md) at `0x00A7943D`
- [CmpSplitLeaf](../A7/CmpSplitLeaf_function_00A7C7E0.md) at `0x00A7CAC6`
- [CmpSplitLeaf](../A7/CmpSplitLeaf_function_00A7C7E0.md) at `0x00A7CAD0`
- [CmpSplitLeaf](../A7/CmpSplitLeaf_function_00A7C7E0.md) at `0x00A7CADA`
- [CmpSplitLeaf](../A7/CmpSplitLeaf_function_00A7C7E0.md) at `0x00A7CAE4`
- [CmEnumerateValueKeyFromMergedView](../A7/CmEnumerateValueKeyFromMergedView_function_00A7D650.md) at `0x00A7D922`
- [CmEnumerateValueKeyFromMergedView](../A7/CmEnumerateValueKeyFromMergedView_function_00A7D650.md) at `0x00A7D92C`
- [CmEnumerateValueKeyFromMergedView](../A7/CmEnumerateValueKeyFromMergedView_function_00A7D650.md) at `0x00A7DA55`
- [CmEnumerateValueKeyFromMergedView](../A7/CmEnumerateValueKeyFromMergedView_function_00A7D650.md) at `0x00A7DA73`
- [CmEnumerateValueKeyFromMergedView](../A7/CmEnumerateValueKeyFromMergedView_function_00A7D650.md) at `0x00A7DA91`
- [CmEnumerateValueKeyFromMergedView](../A7/CmEnumerateValueKeyFromMergedView_function_00A7D650.md) at `0x00A7DAAF`
- [CmpFreeKeyValues](../A8/CmpFreeKeyValues_function_00A8B3E4.md) at `0x00A8B472`
- [CmpMarkKeyValuesDirty](../A8/CmpMarkKeyValuesDirty_function_00A8B4C8.md) at `0x00A8B600`
- [CmpMarkKeyValuesDirty](../A8/CmpMarkKeyValuesDirty_function_00A8B4C8.md) at `0x00A8B670`
- [CmQueryMultipleValueForLayeredKey](../A8/CmQueryMultipleValueForLayeredKey_function_00A8DE80.md) at `0x00A8E23A`
- [CmQueryMultipleValueForLayeredKey](../A8/CmQueryMultipleValueForLayeredKey_function_00A8DE80.md) at `0x00A8E244`
- [CmQueryMultipleValueForLayeredKey](../A8/CmQueryMultipleValueForLayeredKey_function_00A8DE80.md) at `0x00A8E24E`
- [CmQueryMultipleValueForLayeredKey](../A8/CmQueryMultipleValueForLayeredKey_function_00A8DE80.md) at `0x00A8E339`
- [CmpMarkEntireIndexDirty](../AA/CmpMarkEntireIndexDirty_function_00AA24B4.md) at `0x00AA255D`
- [CmpFreeIndexByCell](../AA/CmpFreeIndexByCell_function_00AA6F0C.md) at `0x00AA6F8A`
- [CmpFindSubKeyByNumberFromMergedView](../AB/CmpFindSubKeyByNumberFromMergedView_function_00AB8284.md) at `0x00AB85AA`
- [CmpFindSubKeyByNumberFromMergedView](../AB/CmpFindSubKeyByNumberFromMergedView_function_00AB8284.md) at `0x00AB86EF`
- [CmpFindSubKeyByNumberFromMergedView](../AB/CmpFindSubKeyByNumberFromMergedView_function_00AB8284.md) at `0x00AB8729`
- [CmpFindSubKeyByNumberFromMergedView](../AB/CmpFindSubKeyByNumberFromMergedView_function_00AB8284.md) at `0x00AB876A`
- [CmpCreateHiveRootCell](../AB/CmpCreateHiveRootCell_function_00ABF568.md) at `0x00ABF801`
- [CmpSyncSubKeysAfterDelete](../AC/CmpSyncSubKeysAfterDelete_function_00AC5980.md) at `0x00AC5A8E`
- [CmpSyncSubKeysAfterDelete](../AC/CmpSyncSubKeysAfterDelete_function_00AC5980.md) at `0x00AC5AA8`
- [sub_00B160F4](../B1/Unknown_function_00B160F4.md) at `0x00B1623E`
- [sub_00B16338](../B1/Unknown_function_00B16338.md) at `0x00B16362`
- [sub_00B16440](../B1/Unknown_function_00B16440.md) at `0x00B165AF`
- [sub_00B169F2](../B1/Unknown_function_00B169F2.md) at `0x00B16BA4`
- [sub_00B16C30](../B1/Unknown_function_00B16C30.md) at `0x00B16CBB`
- [sub_00B16C30](../B1/Unknown_function_00B16C30.md) at `0x00B16CE9`
- [sub_00B16C30](../B1/Unknown_function_00B16C30.md) at `0x00B16D11`
- [sub_00B16D42](../B1/Unknown_function_00B16D42.md) at `0x00B16D7A`
- [sub_00B16DFE](../B1/Unknown_function_00B16DFE.md) at `0x00B16E6E`
- [sub_00B1A6A6](../B1/Unknown_function_00B1A6A6.md) at `0x00B1A6CD`
- [sub_00B258D8](../B2/Unknown_function_00B258D8.md) at `0x00B259A3`
- [sub_00B25C42](../B2/Unknown_function_00B25C42.md) at `0x00B25CD4`
- [sub_00B28C32](../B2/Unknown_function_00B28C32.md) at `0x00B28CB5`
- [sub_00B28CFC](../B2/Unknown_function_00B28CFC.md) at `0x00B28E01`
- [sub_00B28E18](../B2/Unknown_function_00B28E18.md) at `0x00B28E5F`
- [sub_00B28E18](../B2/Unknown_function_00B28E18.md) at `0x00B28E90`
- [sub_00B28E18](../B2/Unknown_function_00B28E18.md) at `0x00B28EC1`
- [sub_00B28E18](../B2/Unknown_function_00B28E18.md) at `0x00B28F02`
- [sub_00B28F1E](../B2/Unknown_function_00B28F1E.md) at `0x00B28F86`
- [sub_00B28F1E](../B2/Unknown_function_00B28F1E.md) at `0x00B28FFA`
- [sub_00B28F1E](../B2/Unknown_function_00B28F1E.md) at `0x00B29016`
- [sub_00B28F1E](../B2/Unknown_function_00B28F1E.md) at `0x00B2908A`
- [sub_00B28F1E](../B2/Unknown_function_00B28F1E.md) at `0x00B290A6`
- [sub_00B28F1E](../B2/Unknown_function_00B28F1E.md) at `0x00B290E5`
- [sub_00B28F1E](../B2/Unknown_function_00B28F1E.md) at `0x00B2911B`
- [sub_00B309F4](../B3/Unknown_function_00B309F4.md) at `0x00B30A46`
- [sub_00B309F4](../B3/Unknown_function_00B309F4.md) at `0x00B30A6B`
- [sub_00B309F4](../B3/Unknown_function_00B309F4.md) at `0x00B30A8F`
- [sub_00B37E2A](../B3/Unknown_function_00B37E2A.md) at `0x00B37E63`
- [sub_00B41CEA](../B4/Unknown_function_00B41CEA.md) at `0x00B41DA6`
- [sub_00B428B8](../B4/Unknown_function_00B428B8.md) at `0x00B429D8`
- [sub_00B46094](../B4/Unknown_function_00B46094.md) at `0x00B460B0`
- [sub_00B46094](../B4/Unknown_function_00B46094.md) at `0x00B46124`
- [sub_00B46510](../B4/Unknown_function_00B46510.md) at `0x00B46559`
- [CmpDoAccessCheckOnSubtree](../../pagecmrc/BC/CmpDoAccessCheckOnSubtree_function_00BC9CD0.md) at `0x00BC9E27`
- [CmpDoAccessCheckOnSubtree](../../pagecmrc/BC/CmpDoAccessCheckOnSubtree_function_00BC9CD0.md) at `0x00BC9E80`
- [CmpCreateRootNode](../../init/C5/CmpCreateRootNode_function_00C57A6C.md) at `0x00C57BA8`
- [CmSelectQualifiedInstallLanguage](../../init/C5/CmSelectQualifiedInstallLanguage_function_00C58F58.md) at `0x00C59170`
- [CmSelectQualifiedInstallLanguage](../../init/C5/CmSelectQualifiedInstallLanguage_function_00C58F58.md) at `0x00C5918C`
- [CmSelectQualifiedInstallLanguage](../../init/C5/CmSelectQualifiedInstallLanguage_function_00C58F58.md) at `0x00C591A8`
- [CmSelectQualifiedInstallLanguage](../../init/C5/CmSelectQualifiedInstallLanguage_function_00C58F58.md) at `0x00C59304`
- [CmSelectQualifiedInstallLanguage](../../init/C5/CmSelectQualifiedInstallLanguage_function_00C58F58.md) at `0x00C59329`
- [CmSelectQualifiedInstallLanguage](../../init/C5/CmSelectQualifiedInstallLanguage_function_00C58F58.md) at `0x00C593A2`
- [CmSelectQualifiedInstallLanguage](../../init/C5/CmSelectQualifiedInstallLanguage_function_00C58F58.md) at `0x00C59484`
- [CmSelectQualifiedInstallLanguage](../../init/C5/CmSelectQualifiedInstallLanguage_function_00C58F58.md) at `0x00C594B2`
- [CmpGetSystemControlValues](../../init/C5/CmpGetSystemControlValues_function_00C5959C.md) at `0x00C5974D`
- [CmpGetSystemControlValues](../../init/C5/CmpGetSystemControlValues_function_00C5959C.md) at `0x00C598A1`
- [CmpGetSystemControlValues](../../init/C5/CmpGetSystemControlValues_function_00C5959C.md) at `0x00C5994E`
- [CmpGetSystemControlValues](../../init/C5/CmpGetSystemControlValues_function_00C5959C.md) at `0x00C59980`
- [CmpAddDriverToList](../../init/C5/CmpAddDriverToList_function_00C5B758.md) at `0x00C5B9C9`
- [CmpAddDriverToList](../../init/C5/CmpAddDriverToList_function_00C5B758.md) at `0x00C5BA2F`
- [CmpAddDriverToList](../../init/C5/CmpAddDriverToList_function_00C5B758.md) at `0x00C5BA73`
- [CmpAddDriverToList](../../init/C5/CmpAddDriverToList_function_00C5B758.md) at `0x00C5BAAD`
- [CmpAddDriverToList](../../init/C5/CmpAddDriverToList_function_00C5B758.md) at `0x00C5BC3A`
- [CmpAddDriverToList](../../init/C5/CmpAddDriverToList_function_00C5B758.md) at `0x00C5BC67`
- [CmpAddDriverToList](../../init/C5/CmpAddDriverToList_function_00C5B758.md) at `0x00C5BCEE`
- [CmpAddDriverToList](../../init/C5/CmpAddDriverToList_function_00C5B758.md) at `0x00C5BD14`
- [CmpAddDriverToList](../../init/C5/CmpAddDriverToList_function_00C5B758.md) at `0x00C5BDB5`
- [CmpAddDriverToList](../../init/C5/CmpAddDriverToList_function_00C5B758.md) at `0x00C5BDDB`
- [CmpFindDrivers](../../init/C5/CmpFindDrivers_function_00C5BFBC.md) at `0x00C5C1F5`
- [CmpFindDrivers](../../init/C5/CmpFindDrivers_function_00C5BFBC.md) at `0x00C5C22B`
- [CmpFindDrivers](../../init/C5/CmpFindDrivers_function_00C5BFBC.md) at `0x00C5C257`
- [CmpFindDrivers](../../init/C5/CmpFindDrivers_function_00C5BFBC.md) at `0x00C5C273`
- [CmpFindGroupOrderList](../../init/C5/CmpFindGroupOrderList_function_00C5C2B0.md) at `0x00C5C313`
- [CmpFindGroupOrderList](../../init/C5/CmpFindGroupOrderList_function_00C5C2B0.md) at `0x00C5C36D`
- [CmpFindRedirectedDriverServiceStateNode](../../init/C5/CmpFindRedirectedDriverServiceStateNode_function_00C5C480.md) at `0x00C5C522`
- [CmpFindStateSepKeysRedirectionMapNode](../../init/C5/CmpFindStateSepKeysRedirectionMapNode_function_00C5C554.md) at `0x00C5C5C8`
- [CmpFindTagIndex](../../init/C5/CmpFindTagIndex_function_00C5C628.md) at `0x00C5C6DC`
- [CmpFindTagIndex](../../init/C5/CmpFindTagIndex_function_00C5C628.md) at `0x00C5C73B`
- [CmpFindTagIndex](../../init/C5/CmpFindTagIndex_function_00C5C628.md) at `0x00C5C7B2`
- [CmpFindTagIndex](../../init/C5/CmpFindTagIndex_function_00C5C628.md) at `0x00C5C800`
- [CmpFindTagIndex](../../init/C5/CmpFindTagIndex_function_00C5C628.md) at `0x00C5C828`
- [CmpGetStateSepKeysRedirectionPathValue](../../init/C5/CmpGetStateSepKeysRedirectionPathValue_function_00C5CA3C.md) at `0x00C5CAC2`
- [CmpGetStateSepKeysRedirectionPathValue](../../init/C5/CmpGetStateSepKeysRedirectionPathValue_function_00C5CA3C.md) at `0x00C5CB22`
- [CmpGetStateSepKeysRedirectionPathValue](../../init/C5/CmpGetStateSepKeysRedirectionPathValue_function_00C5CA3C.md) at `0x00C5CB88`
- [CmpIsLoadType](../../init/C5/CmpIsLoadType_function_00C5CBF8.md) at `0x00C5CD36`
- [CmpIsLoadType](../../init/C5/CmpIsLoadType_function_00C5CBF8.md) at `0x00C5CDD8`
- [CmpIsLoadType](../../init/C5/CmpIsLoadType_function_00C5CBF8.md) at `0x00C5CE14`
- [CmpIsLoadType](../../init/C5/CmpIsLoadType_function_00C5CBF8.md) at `0x00C5CE7F`
- [CmpIsLoadType](../../init/C5/CmpIsLoadType_function_00C5CBF8.md) at `0x00C5CF0B`
- [CmpIsLoadType](../../init/C5/CmpIsLoadType_function_00C5CBF8.md) at `0x00C5CF33`
- [CmpIsLoadType](../../init/C5/CmpIsLoadType_function_00C5CBF8.md) at `0x00C5CF47`
- [CmpIsLoadType](../../init/C5/CmpIsLoadType_function_00C5CBF8.md) at `0x00C5CF66`
- [CmpLoadManufacturingModeNode](../../init/C5/CmpLoadManufacturingModeNode_function_00C5CF94.md) at `0x00C5D011`
- [CmpLoadManufacturingModeNode](../../init/C5/CmpLoadManufacturingModeNode_function_00C5CF94.md) at `0x00C5D06D`
- [CmpLoadManufacturingProfileNode](../../init/C5/CmpLoadManufacturingProfileNode_function_00C5D0C8.md) at `0x00C5D132`
- [CmpLoadManufacturingProfileNode](../../init/C5/CmpLoadManufacturingProfileNode_function_00C5D0C8.md) at `0x00C5D173`
- [CmpLoadManufacturingProfileServicesNode](../../init/C5/CmpLoadManufacturingProfileServicesNode_function_00C5D1B4.md) at `0x00C5D219`
- [CmpLoadServicesNode](../../init/C5/CmpLoadServicesNode_function_00C5D274.md) at `0x00C5D2DC`
- [CmpSortDriverList](../../init/C5/CmpSortDriverList_function_00C5D3D0.md) at `0x00C5D459`
- [CmpSortDriverList](../../init/C5/CmpSortDriverList_function_00C5D3D0.md) at `0x00C5D4B9`
- [CmpSortDriverList](../../init/C5/CmpSortDriverList_function_00C5D3D0.md) at `0x00C5D515`
- [CmpSortDriverList](../../init/C5/CmpSortDriverList_function_00C5D3D0.md) at `0x00C5D55F`
- [CmpSortDriverList](../../init/C5/CmpSortDriverList_function_00C5D3D0.md) at `0x00C5D5B3`
- [CmpSortDriverList](../../init/C5/CmpSortDriverList_function_00C5D3D0.md) at `0x00C5D5F3`
- [CmpGetBootValueData](../../init/C5/CmpGetBootValueData_function_00C5D610.md) at `0x00C5D784`
- [CmpGetBootValueData](../../init/C5/CmpGetBootValueData_function_00C5D610.md) at `0x00C5D7BA`
- [CmpGetBootValueData](../../init/C5/CmpGetBootValueData_function_00C5D610.md) at `0x00C5D7D6`
- [CmpGetBootValueData](../../init/C5/CmpGetBootValueData_function_00C5D610.md) at `0x00C5D830`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0085CC20  48 83 EC 28                     sub rsp, 0x28
0085CC24  48 8B CA                        mov rcx, rdx
0085CC27  E8 14 91 FF FF                  call 0x140855d40
0085CC2C  48 83 C4 28                     add rsp, 0x28
0085CC30  C3                              ret
0085CC31  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HvpReleaseCellFlat(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = HvpGetCellContextReinitialize(a2, a2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HvpReleaseCellFlat(int64_t Arg1, int64_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = HvpGetCellContextReinitialize(Arg2, Arg2, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0085CC20&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0085CC20[BB_0085CC20]
  bb_0085CC31[BB_0085CC31]
```
