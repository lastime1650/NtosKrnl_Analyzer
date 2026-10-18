# KeReleaseQueuedSpinLock

- RVA: `0x00272540`–`0x0027254F` (길이 `15` bytes)
- VA: `0x0000000140272540`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00065BC8`
- 디코드: `3`개 명령, `15/15` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **99**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [IoBoostThreadIoPriority](../21/IoBoostThreadIoPriority_function_00216110.md) at `0x002163AC`
- [CcExtendVacbArray](../26/CcExtendVacbArray_function_0026DCD0.md) at `0x0026DFC0`
- [IoDetachDevice](../26/IoDetachDevice_function_0026FA10.md) at `0x0026FA81`
- [IoDeleteDevice](../26/IoDeleteDevice_function_0026FE90.md) at `0x0026FF5D`
- [IopCheckVpbMounted](IopCheckVpbMounted_function_00270540.md) at `0x0027081C`
- [IopCompleteUnloadOrDelete](IopCompleteUnloadOrDelete_function_00270BC8.md) at `0x00270C4A`
- [IopCompleteUnloadOrDelete](IopCompleteUnloadOrDelete_function_00270BC8.md) at `0x00270CAE`
- [IopCompleteUnloadOrDelete](IopCompleteUnloadOrDelete_function_00270BC8.md) at `0x00270D37`
- [IopCompleteUnloadOrDelete](IopCompleteUnloadOrDelete_function_00270BC8.md) at `0x00270D96`
- [IopCompleteUnloadOrDelete](IopCompleteUnloadOrDelete_function_00270BC8.md) at `0x00270DF2`
- [CcUnmapInactiveViewsInternal](CcUnmapInactiveViewsInternal_function_0027174C.md) at `0x0027183D`
- [CcUnmapInactiveViewsInternal](CcUnmapInactiveViewsInternal_function_0027174C.md) at `0x00271951`
- [CcUnmapInactiveViewsInternal](CcUnmapInactiveViewsInternal_function_0027174C.md) at `0x00271990`
- [CcUnmapInactiveViewsInternal](CcUnmapInactiveViewsInternal_function_0027174C.md) at `0x00271ABD`
- [PnpGetRelatedTargetDevice](PnpGetRelatedTargetDevice_function_00271F54.md) at `0x00271FA9`
- [IoReleaseVpbSpinLock](IoReleaseVpbSpinLock_function_002720C0.md) at `0x002720CB`
- [IoCancelIrp](IoCancelIrp_function_002720E0.md) at `0x00272174`
- [FsRtlNotifySetCancelRoutine](FsRtlNotifySetCancelRoutine_function_0027239C.md) at `0x002723E1`
- [FsRtlNotifySetCancelRoutine](FsRtlNotifySetCancelRoutine_function_0027239C.md) at `0x00272428`
- [IopGetMountFlag](IopGetMountFlag_function_00272444.md) at `0x0027247B`
- [IopGetDevicePDO](IopGetDevicePDO_function_002724D8.md) at `0x0027251B`
- [IoGetLowerDeviceObjectWithTag](IoGetLowerDeviceObjectWithTag_function_00272660.md) at `0x0027269F`
- [CcGetVacbMiss](CcGetVacbMiss_function_00272900.md) at `0x00272CC2`
- [CcGetVacbMiss](CcGetVacbMiss_function_00272900.md) at `0x00272DC3`
- [IopfCompleteRequest](../29/IopfCompleteRequest_function_0029B5F8.md) at `0x0029BD0B`
- [IopfCompleteRequest](../29/IopfCompleteRequest_function_0029B5F8.md) at `0x0029BD41`
- [PopQueueQuerySetIrp](../2B/PopQueueQuerySetIrp_function_002BEF18.md) at `0x002BF123`
- [CcUnmapVacbArray](../38/CcUnmapVacbArray_function_0038AEAC.md) at `0x0038B047`
- [FsRtlPrivateCheckWaitingLocks](../38/FsRtlPrivateCheckWaitingLocks_function_0038DCBC.md) at `0x0038DD92`
- [FsRtlpAcknowledgeOplockBreakByCacheFlags](../3F/FsRtlpAcknowledgeOplockBreakByCacheFlags_function_003F1988.md) at `0x003F2210`
- [FsRtlpRequestExclusiveOplock](../3F/FsRtlpRequestExclusiveOplock_function_003F3800.md) at `0x003F3D18`
- [FsRtlpRequestExclusiveOplock](../3F/FsRtlpRequestExclusiveOplock_function_003F3800.md) at `0x003F4016`
- [IopAttachDeviceToDeviceStackSafe](../41/IopAttachDeviceToDeviceStackSafe_function_00410574.md) at `0x00410712`
- [IopVerifyDeviceObjectOnStack](../41/IopVerifyDeviceObjectOnStack_function_0041B3B0.md) at `0x0041B43A`
- [FsRtlpOplockCleanup](../42/FsRtlpOplockCleanup_function_00425030.md) at `0x004255B1`
- [FsRtlpRemoveAndCompleteRHIrp](../42/FsRtlpRemoveAndCompleteRHIrp_function_00425964.md) at `0x004259DD`
- [FsRtlpRemoveAndCompleteWaitingIrp](../42/FsRtlpRemoveAndCompleteWaitingIrp_function_00425FC0.md) at `0x004260AA`
- [CcDereferenceVacbArray](../44/CcDereferenceVacbArray_function_004427B0.md) at `0x00442842`
- [IopStartNextPacket](../45/IopStartNextPacket_function_0045F9A4.md) at `0x0045FA12`
- [IopStartNextPacket](../45/IopStartNextPacket_function_0045F9A4.md) at `0x0045FA50`
- [IopStartNextPacketByKey](../45/IopStartNextPacketByKey_function_0045FA64.md) at `0x0045FADC`
- [IopStartNextPacketByKey](../45/IopStartNextPacketByKey_function_0045FA64.md) at `0x0045FB00`
- [IoStartPacket](../45/IoStartPacket_function_0045FC30.md) at `0x0045FCD3`
- [IoStartPacket](../45/IoStartPacket_function_0045FC30.md) at `0x0045FD39`
- [PnpRemoveLockedDeviceNode](../47/PnpRemoveLockedDeviceNode_function_004702AC.md) at `0x0047038E`
- [PnpRemoveLockedDeviceNode](../47/PnpRemoveLockedDeviceNode_function_004702AC.md) at `0x004703E1`
- [PnpRemoveLockedDeviceNode](../47/PnpRemoveLockedDeviceNode_function_004702AC.md) at `0x0047060B`
- [IoEnumerateDeviceObjectList](../47/IoEnumerateDeviceObjectList_function_0047D440.md) at `0x0047D4C3`
- [IopInsertRemoveDevice](../48/IopInsertRemoveDevice_function_0048E350.md) at `0x0048E389`
- [RawInitiateDeleteVolume](../48/RawInitiateDeleteVolume_function_0048FDFC.md) at `0x0048FE59`
- [RawInitiateDeleteVolume](../48/RawInitiateDeleteVolume_function_0048FDFC.md) at `0x0048FEB0`
- [RawInitiateDeleteVolume](../48/RawInitiateDeleteVolume_function_0048FDFC.md) at `0x0048FFB6`
- [WmipNotificationIrpCancel](../49/WmipNotificationIrpCancel_function_00491BA0.md) at `0x00491BE4`
- [IopMountInitializeVpb](../49/IopMountInitializeVpb_function_004972C4.md) at `0x0049734E`
- [IoGetDriverObjectExtension](../49/IoGetDriverObjectExtension_function_00498B90.md) at `0x00498BC4`
- [IopQueryVpbFlagsSafe](../4A/IopQueryVpbFlagsSafe_function_004A1184.md) at `0x004A11AF`
- [FsRtlpCancelOplockRHIrp](../4A/FsRtlpCancelOplockRHIrp_function_004A55F0.md) at `0x004A563D`
- [IopCsqCancelRoutine](../4A/IopCsqCancelRoutine_function_004A7D00.md) at `0x004A7D1F`
- [IoGetDiskDeviceObject](../4A/IoGetDiskDeviceObject_function_004A8540.md) at `0x004A85A1`
- [CcGetRandomVacbArrayWithReference](../4A/CcGetRandomVacbArrayWithReference_function_004A98AC.md) at `0x004A9920`
- [CcGetRandomVacbArrayWithReference](../4A/CcGetRandomVacbArrayWithReference_function_004A98AC.md) at `0x004A993F`
- [PnpIsChainDereferenced](../4A/PnpIsChainDereferenced_function_004ABAE8.md) at `0x004ABBBA`
- [PnpIsChainDereferenced](../4A/PnpIsChainDereferenced_function_004ABAE8.md) at `0x004ABBF5`
- [PpMarkDeviceStackExtensionFlag](../4A/PpMarkDeviceStackExtensionFlag_function_004AD8D0.md) at `0x004AD91B`
- [CcAllocateInitializeVacbArray](../4A/CcAllocateInitializeVacbArray_function_004AE2BC.md) at `0x004AE2EC`
- [CcAllocateInitializeVacbArray](../4A/CcAllocateInitializeVacbArray_function_004AE2BC.md) at `0x004AE335`
- [CcAllocateInitializeVacbArray](../4A/CcAllocateInitializeVacbArray_function_004AE2BC.md) at `0x004AE351`
- [IopResurrectDriver](../4B/IopResurrectDriver_function_004B138C.md) at `0x004B13D3`
- [IopResurrectDriver](../4B/IopResurrectDriver_function_004B138C.md) at `0x004B1408`
- [PnpFindMountableDevice](../4B/PnpFindMountableDevice_function_004B1418.md) at `0x004B144B`
- [FsRtlpRemoveAndCompleteReadOnlyIrp](../4B/FsRtlpRemoveAndCompleteReadOnlyIrp_function_004B495C.md) at `0x004B49DF`
- [IopInterlockedRemoveHeadList](../4B/IopInterlockedRemoveHeadList_function_004B4FB0.md) at `0x004B4FD8`
- [IoAllocateDriverObjectExtension](../4B/IoAllocateDriverObjectExtension_function_004B8650.md) at `0x004B86F6`
- [IoAdjustStackSizeForRedirection](../4B/IoAdjustStackSizeForRedirection_function_004BB3B0.md) at `0x004BB3F3`
- [FsRtlpOplockBreakToII](../4B/FsRtlpOplockBreakToII_function_004BB824.md) at `0x004BB8DB`
- [RawCheckForDeleteVolume](../4C/RawCheckForDeleteVolume_function_004C6FF4.md) at `0x004C702A`
- [RawCheckForDeleteVolume](../4C/RawCheckForDeleteVolume_function_004C6FF4.md) at `0x004C7077`
- [IopReferenceVerifyVpb](../4C/IopReferenceVerifyVpb_function_004C87B4.md) at `0x004C8814`
- [PnpHandleEnumerateHandlesAgainstPdoStack](../4C/PnpHandleEnumerateHandlesAgainstPdoStack_function_004C8F94.md) at `0x004C900C`
- [PnpHandleEnumerateHandlesAgainstPdoStack](../4C/PnpHandleEnumerateHandlesAgainstPdoStack_function_004C8F94.md) at `0x004C907B`
- [PnpMarkDeviceForRemove](../4C/PnpMarkDeviceForRemove_function_004C9DA8.md) at `0x004C9E47`
- [PnpMarkDeviceForRemove](../4C/PnpMarkDeviceForRemove_function_004C9DA8.md) at `0x004C9E71`
- [PnpUnlockMountableDevice](../4C/PnpUnlockMountableDevice_function_004CDD2C.md) at `0x004CDD66`
- [PnpLockMountableDevice](../4C/PnpLockMountableDevice_function_004CFFAC.md) at `0x004CFFEF`
- [FsRtlPrivateCancelFileLockIrp](../4D/FsRtlPrivateCancelFileLockIrp_function_004D4B70.md) at `0x004D4BAE`
- [IopCheckUnloadDriver](../4D/IopCheckUnloadDriver_function_004DC454.md) at `0x004DC4BF`
- [IopCheckUnloadDriver](../4D/IopCheckUnloadDriver_function_004DC454.md) at `0x004DC526`
- [FsRtlUninitializeOplock](../4E/FsRtlUninitializeOplock_function_004E42C0.md) at `0x004E4372`
- [FsRtlUninitializeOplock](../4E/FsRtlUninitializeOplock_function_004E42C0.md) at `0x004E45BC`
- [FsRtlUninitializeOplock](../4E/FsRtlUninitializeOplock_function_004E42C0.md) at `0x004E4660`
- [FsRtlpCancelWaitingIrp](../4E/FsRtlpCancelWaitingIrp_function_004E4698.md) at `0x004E470E`
- [FsRtlpOplockBreakByCacheFlags](../4E/FsRtlpOplockBreakByCacheFlags_function_004E4990.md) at `0x004E52CE`
- [FsRtlpOplockBreakByCacheFlags](../4E/FsRtlpOplockBreakByCacheFlags_function_004E4990.md) at `0x004E53FB`
- [FsRtlpOplockBreakByCacheFlags](../4E/FsRtlpOplockBreakByCacheFlags_function_004E4990.md) at `0x004E54D2`
- [FsRtlpOplockBreakByCacheFlags](../4E/FsRtlpOplockBreakByCacheFlags_function_004E4990.md) at `0x004E5643`
- [FsRtlpOplockBreakByCacheFlags](../4E/FsRtlpOplockBreakByCacheFlags_function_004E4990.md) at `0x004E56E6`
- [FsRtlpRequestShareableOplock](../4E/FsRtlpRequestShareableOplock_function_004E6EC8.md) at `0x004E7598`
- [FsRtlpRequestShareableOplock](../4E/FsRtlpRequestShareableOplock_function_004E6EC8.md) at `0x004E7923`
- [FsRtlpWaitOnIrp](../4E/FsRtlpWaitOnIrp_function_004E7998.md) at `0x004E7C24`
- [FsRtlCancelNotify](../4E/FsRtlCancelNotify_function_004E7F90.md) at `0x004E7FDB`
- [IopCopyCompleteReadIrp](../4E/IopCopyCompleteReadIrp_function_004E83F0.md) at `0x004E85A8`
- [IopCopyCompleteReadIrp](../4E/IopCopyCompleteReadIrp_function_004E83F0.md) at `0x004E85E4`
- [FsRtlpOplockBreakToNone](../4F/FsRtlpOplockBreakToNone_function_004F8354.md) at `0x004F83F1`
- [FsRtlpCancelExclusiveIrp](../4F/FsRtlpCancelExclusiveIrp_function_004F96CC.md) at `0x004F96FC`
- [CcInitializePartitionVacbs](../57/CcInitializePartitionVacbs_function_0057EB60.md) at `0x0057EBB2`
- [CcInitializePartitionVacbs](../57/CcInitializePartitionVacbs_function_0057EB60.md) at `0x0057EBF0`
- [CcInitializePartitionVacbs](../57/CcInitializePartitionVacbs_function_0057EB60.md) at `0x0057EC46`
- [CcUninitializePartitionVacbs](../57/CcUninitializePartitionVacbs_function_0057EC70.md) at `0x0057ECE5`
- [FsRtlpAcknowledgeOplockBreak](../58/FsRtlpAcknowledgeOplockBreak_function_00582144.md) at `0x00582286`
- [FsRtlpCancelReadOnlyOplockIrp](../58/FsRtlpCancelReadOnlyOplockIrp_function_00582380.md) at `0x005823B1`
- [FsRtlpGrantAnyOplockFromExclusive](../58/FsRtlpGrantAnyOplockFromExclusive_function_00582540.md) at `0x005828DB`
- [FsRtlDisallowLegacyFilterOnDevice](../58/FsRtlDisallowLegacyFilterOnDevice_function_00582F80.md) at `0x00582FBE`
- [IopDisassociateThreadIrp](../59/IopDisassociateThreadIrp_function_0059708C.md) at `0x00597102`
- [IopDisassociateThreadIrp](../59/IopDisassociateThreadIrp_function_0059708C.md) at `0x005971D8`
- [IopGetDriverPathInformation](../59/IopGetDriverPathInformation_function_005973A8.md) at `0x00597477`
- [IopInterlockedInsertHeadList](../59/IopInterlockedInsertHeadList_function_005974A8.md) at `0x005974E7`
- [IopInterlockedInsertTailList](../59/IopInterlockedInsertTailList_function_00597500.md) at `0x0059753F`
- [IopGetFsRegistrationInProgress](../59/IopGetFsRegistrationInProgress_function_00597F58.md) at `0x00597F75`
- [IopSetFsRegistrationInProgress](../59/IopSetFsRegistrationInProgress_function_00597FF0.md) at `0x0059800F`
- [IopSetLegacyResourcesFlag](../5A/IopSetLegacyResourcesFlag_function_005A79A4.md) at `0x005A79C2`
- [PiDqIrpCancel](../5A/PiDqIrpCancel_function_005A7CA0.md) at `0x005A7CCC`
- [PiSwIrpCancelStartCreate](../5A/PiSwIrpCancelStartCreate_function_005A9E60.md) at `0x005A9E8C`
- [RawVerifyVolume](../5E/RawVerifyVolume_function_005E5120.md) at `0x005E516B`
- [RawVerifyVolume](../5E/RawVerifyVolume_function_005E5120.md) at `0x005E51C4`
- [DifKeReleaseQueuedSpinLockWrapper](../63/DifKeReleaseQueuedSpinLockWrapper_function_00631AE0.md) at `0x00631BB7`
- [sub_006E206A](../6E/Unknown_function_006E206A.md) at `0x006E208A`
- [sub_006E4D86](../6E/Unknown_function_006E4D86.md) at `0x006E4DB6`
- [sub_006E4D86](../6E/Unknown_function_006E4D86.md) at `0x006E4DCE`
- [sub_006EBD42](../6E/Unknown_function_006EBD42.md) at `0x006EBDE1`
- [sub_006F6F06](../6F/Unknown_function_006F6F06.md) at `0x006F6F26`
- [sub_006FC8F4](../6F/Unknown_function_006FC8F4.md) at `0x006FC917`
- [IoUnregisterShutdownNotification](../../pagelk/B7/IoUnregisterShutdownNotification_function_00B7CCC0.md) at `0x00B7CDA5`
- [IovpCallDriver1](../../pagevrfy/B9/IovpCallDriver1_function_00B9CCA4.md) at `0x00B9D0D0`
- [IovpExamineIrpStackForwarding](../../pagevrfy/B9/IovpExamineIrpStackForwarding_function_00B9D640.md) at `0x00B9D745`
- [IovUtilGetBottomDeviceObjectWithTag](../../pagevrfy/BA/IovUtilGetBottomDeviceObjectWithTag_function_00BA2A20.md) at `0x00BA2A65`
- [IovUtilGetLowerDeviceObjectWithTag](../../pagevrfy/BA/IovUtilGetLowerDeviceObjectWithTag_function_00BA2A84.md) at `0x00BA2AC3`
- [IovUtilGetUpperDeviceObjectWithTag](../../pagevrfy/BA/IovUtilGetUpperDeviceObjectWithTag_function_00BA2AE0.md) at `0x00BA2B18`
- [IovUtilIsVerifiedDeviceStack](../../pagevrfy/BA/IovUtilIsVerifiedDeviceStack_function_00BA2B88.md) at `0x00BA2C3D`
- [IovUtilRelateDeviceObjects](../../pagevrfy/BA/IovUtilRelateDeviceObjects_function_00BA2C98.md) at `0x00BA2D2A`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00272540  40 56                           push rsi
00272542  48 83 EC 20                     sub rsp, 0x20
00272546  65 48 8B 04 25 28 00 00 00      mov rax, qword ptr gs:[0x28]
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KeReleaseQueuedSpinLock(void)
{
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    return *(unsigned __int64 *)(gs_base + (0 + 40));
}
```

## 5. (Beta) C Style

```c
void KeReleaseQueuedSpinLock(void)
{
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    return *(uint64_t *)(gs_base + (0 + 0x28));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00272540&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00272540[BB_00272540]
```
