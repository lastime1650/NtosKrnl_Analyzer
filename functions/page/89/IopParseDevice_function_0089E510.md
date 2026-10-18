# IopParseDevice

- RVA: `0x0089E510`–`0x008A08BC` (길이 `9,132` bytes)
- VA: `0x000000014089E510`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007E834`
- 디코드: `1,990`개 명령, `9,132/9,132` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **176**; 고유 호출 대상: **82**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **9**

### Outgoing calls
- `0x0089E634` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x0089E6F4` → [IopCheckDeviceAndDriver](../../text/3F/IopCheckDeviceAndDriver_function_003FCBE0.md) (function, `0x003FCBE0`)
- `0x0089E7BD` → [IopCheckBackupRestorePrivilege](../8A/IopCheckBackupRestorePrivilege_function_008A08D0.md) (function, `0x008A08D0`)
- `0x0089E842` → [SeIsAppContainerOrIdentifyLevelContext](../A2/SeIsAppContainerOrIdentifyLevelContext_function_00A21A74.md) (function, `0x00A21A74`)
- `0x0089E86F` → [SeUnlockSubjectContext](../8C/SeUnlockSubjectContext_function_008C6520.md) (function, `0x008C6520`)
- `0x0089E900` → [IopCheckVpbMounted](../../text/27/IopCheckVpbMounted_function_00270540.md) (function, `0x00270540`)
- `0x0089E93C` → [IoGetAttachedDevice](../../text/41/IoGetAttachedDevice_function_00410810.md) (function, `0x00410810`)
- `0x0089E989` → [SeIsAppContainerOrIdentifyLevelContext](../A2/SeIsAppContainerOrIdentifyLevelContext_function_00A21A74.md) (function, `0x00A21A74`)
- `0x0089E9B7` → [IopDereferenceVpbAndFree](../../text/43/IopDereferenceVpbAndFree_function_0043F474.md) (function, `0x0043F474`)
- `0x0089E9C4` → [IopDecrementDeviceObjectRef](../../text/27/IopDecrementDeviceObjectRef_function_00270970.md) (function, `0x00270970`)
- `0x0089EA95` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x0089EA9E` → [SeLockSubjectContext](../8C/SeLockSubjectContext_function_008C64C0.md) (function, `0x008C64C0`)
- `0x0089EB0C` → [SeAccessCheck](../../text/3A/SeAccessCheck_function_003A6BC0.md) (function, `0x003A6BC0`)
- `0x0089EB8A` → [SeOpenObjectAuditAlarmWithTransaction](../86/SeOpenObjectAuditAlarmWithTransaction_function_0086E790.md) (function, `0x0086E790`)
- `0x0089EB96` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x0089EBA3` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x0089EC16` → [IopIncrementVpbRefCount](../../text/27/IopIncrementVpbRefCount_function_00272820.md) (function, `0x00272820`)
- `0x0089EC56` → [SeAppendPrivileges](../9D/SeAppendPrivileges_function_009D7980.md) (function, `0x009D7980`)
- `0x0089EC63` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (function, `0x00475D80`)
- `0x0089ECC9` → [IopSymlinkPropagateToExtensionIfNeeded](../8A/IopSymlinkPropagateToExtensionIfNeeded_function_008A1580.md) (function, `0x008A1580`)
- `0x0089ED23` → [IopDequeueIrpFromThread](../../text/20/IopDequeueIrpFromThread_function_00207B20.md) (function, `0x00207B20`)
- `0x0089ED3A` → [IoFreeIrp](../../text/24/IoFreeIrp_function_0024DF70.md) (function, `0x0024DF70`)
- `0x0089ED65` → [IoGetRelatedDeviceObject](../../text/29/IoGetRelatedDeviceObject_function_0029B120.md) (function, `0x0029B120`)
- `0x0089ED92` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (function, `0x0020FA20`)
- `0x0089EE43` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0089EE71` → [VfFastIoCheckState](../../pagevrfy/BB/VfFastIoCheckState_function_00BB9440.md) (function, `0x00BB9440`)
- `0x0089EE86` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0089EEC0` → [IopQueryXxxInformation](../8A/IopQueryXxxInformation_function_008A89D0.md) (function, `0x008A89D0`)
- `0x0089EEDC` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0089EEE6` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0089EEF0` → [MmIsDriverVerifying](../../text/4A/MmIsDriverVerifying_function_004A8770.md) (function, `0x004A8770`)
- `0x0089EF00` → [VfFastIoSnapState](../../pagevrfy/BB/VfFastIoSnapState_function_00BB97BC.md) (function, `0x00BB97BC`)
- `0x0089EF28` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0089EF5B` → [IopCloseFile](../86/IopCloseFile_function_008640C0.md) (function, `0x008640C0`)
- `0x0089EF63` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x0089EF85` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x0089EFE1` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0089EFF2` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x0089F001` → [IopDecrementDeviceObjectRef](../../text/27/IopDecrementDeviceObjectRef_function_00270970.md) (function, `0x00270970`)
- `0x0089F01A` → [IopDereferenceVpbAndFree](../../text/43/IopDereferenceVpbAndFree_function_0043F474.md) (function, `0x0043F474`)
- `0x0089F061` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0089F0A3` → [IopQueryXxxInformation](../8A/IopQueryXxxInformation_function_008A89D0.md) (function, `0x008A89D0`)
- `0x0089F0BD` → [IopGetNetworkOpenInformation](../AC/IopGetNetworkOpenInformation_function_00AC8264.md) (function, `0x00AC8264`)
- `0x0089F0CC` → [IoCancelFileOpen](../70/IoCancelFileOpen_function_007034A0.md) (function, `0x007034A0`)
- `0x0089F10B` → [IopQueryXxxInformation](../8A/IopQueryXxxInformation_function_008A89D0.md) (function, `0x008A89D0`)
- `0x0089F129` → [IoFreeIrp](../../text/24/IoFreeIrp_function_0024DF70.md) (function, `0x0024DF70`)
- `0x0089F136` → [IopDecrementDeviceObjectRef](../../text/27/IopDecrementDeviceObjectRef_function_00270970.md) (function, `0x00270970`)
- `0x0089F14B` → [IopDereferenceVpbAndFree](../../text/43/IopDereferenceVpbAndFree_function_0043F474.md) (function, `0x0043F474`)
- `0x0089F161` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x0089F178` → [VfFastIoCheckState](../../pagevrfy/BB/VfFastIoCheckState_function_00BB9440.md) (function, `0x00BB9440`)
- `0x0089F1C7` → [IopAllocateIrpExReturn](../../text/20/IopAllocateIrpExReturn_function_00207720.md) (function, `0x00207720`)
- `0x0089F329` → [IopAllocRealFileObject](IopAllocRealFileObject_function_00899720.md) (function, `0x00899720`)
- `0x0089F3B8` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0089F3D6` → [RtlCopyUnicodeString](../../text/3F/RtlCopyUnicodeString_function_003FEF30.md) (function, `0x003FEF30`)
- `0x0089F42A` → [KeInitializeEvent](../../text/40/KeInitializeEvent_function_0040DD10.md) (function, `0x0040DD10`)
- `0x0089F43F` → [IopQueueThreadIrp](../../text/20/IopQueueThreadIrp_function_002075C0.md) (function, `0x002075C0`)
- `0x0089F46A` → [IofCallDriver](../../text/29/IofCallDriver_function_0029B4B0.md) (function, `0x0029B4B0`)
- `0x0089F4A9` → [IopSetFileObjectExtensionFlag](../../text/43/IopSetFileObjectExtensionFlag_function_0043D710.md) (function, `0x0043D710`)
- `0x0089F4F4` → [IopQueryInformation](../9D/IopQueryInformation_function_009D8370.md) (function, `0x009D8370`)
- `0x0089F510` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (function, `0x002FE1F0`)
- `0x0089F53A` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0089F545` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x0089F57E` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0089F597` → [RtlCopyUnicodeString](../../text/3F/RtlCopyUnicodeString_function_003FEF30.md) (function, `0x003FEF30`)
- `0x0089F5E7` → [IopAllocRealFileObject](IopAllocRealFileObject_function_00899720.md) (function, `0x00899720`)
- `0x0089F622` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0089F698` → [IopRetrieveTransactionParametersFromOpenPacket](../A2/IopRetrieveTransactionParametersFromOpenPacket_function_00A2027C.md) (function, `0x00A2027C`)
- `0x0089F6DA` → [IopRetrieveTransactionParameters](IopRetrieveTransactionParameters_function_00898520.md) (function, `0x00898520`)
- `0x0089F6F7` → [PsIsHostSilo](../../text/44/PsIsHostSilo_function_00443B30.md) (function, `0x00443B30`)
- `0x0089F70D` → [IoGetSilo](../../text/43/IoGetSilo_function_00438490.md) (function, `0x00438490`)
- `0x0089F715` → [PsIsHostSilo](../../text/44/PsIsHostSilo_function_00443B30.md) (function, `0x00443B30`)
- `0x0089F751` → [PsIsHostSilo](../../text/44/PsIsHostSilo_function_00443B30.md) (function, `0x00443B30`)
- `0x0089F766` → [PsAcquireSiloHardReference](../../text/46/PsAcquireSiloHardReference_function_00467620.md) (function, `0x00467620`)
- `0x0089F798` → [IopGetSetSpecificExtension](../../text/42/IopGetSetSpecificExtension_function_0042EE80.md) (function, `0x0042EE80`)
- `0x0089F7D7` → [ObfReferenceObjectWithTag](../../text/21/ObfReferenceObjectWithTag_function_00210710.md) (function, `0x00210710`)
- `0x0089F881` → [IopCreateSecurityCheck](../../text/3A/IopCreateSecurityCheck_function_003A5DA0.md) (function, `0x003A5DA0`)
- `0x0089F896` → [IopDecrementDeviceObjectRef](../../text/27/IopDecrementDeviceObjectRef_function_00270970.md) (function, `0x00270970`)
- `0x0089F8A3` → [IopDereferenceVpbAndFree](../../text/43/IopDereferenceVpbAndFree_function_0043F474.md) (function, `0x0043F474`)
- `0x0089F8CE` → [IopCheckTopDeviceHint](../9E/IopCheckTopDeviceHint_function_009EB5F0.md) (function, `0x009EB5F0`)
- `0x0089F904` → [IopSymlinkGetECP](../../text/45/IopSymlinkGetECP_function_00458288.md) (function, `0x00458288`)
- `0x0089F91C` → [IopSymlinkGetMostRecentlyUsedName](../../text/48/IopSymlinkGetMostRecentlyUsedName_function_0048476C.md) (function, `0x0048476C`)
- `0x0089F95E` → [IopSymlinkUpdateECP](../8A/IopSymlinkUpdateECP_function_008A20CC.md) (function, `0x008A20CC`)
- `0x0089F989` → [IopDecrementDeviceObjectRef](../../text/27/IopDecrementDeviceObjectRef_function_00270970.md) (function, `0x00270970`)
- `0x0089F9A9` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (function, `0x006C6B10`)
- `0x0089F9FB` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0089FA03` → [IopDeleteFileObjectExtension](../../text/38/IopDeleteFileObjectExtension_function_0038C4F0.md) (function, `0x0038C4F0`)
- `0x0089FA12` → [IopDecrementDeviceObjectRef](../../text/27/IopDecrementDeviceObjectRef_function_00270970.md) (function, `0x00270970`)
- `0x0089FA27` → [IopDereferenceVpbAndFree](../../text/43/IopDereferenceVpbAndFree_function_0043F474.md) (function, `0x0043F474`)
- `0x0089FA2F` → [IoFreeIrp](../../text/24/IoFreeIrp_function_0024DF70.md) (function, `0x0024DF70`)
- `0x0089FA90` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (function, `0x0020E6B0`)
- `0x0089FACB` → [PsReleaseSiloHardReference](../../text/38/PsReleaseSiloHardReference_function_0038DEA0.md) (function, `0x0038DEA0`)
- `0x0089FAE1` → [IopDereferenceVpbAndFree](../../text/43/IopDereferenceVpbAndFree_function_0043F474.md) (function, `0x0043F474`)
- `0x0089FAEE` → [IopDecrementDeviceObjectRef](../../text/27/IopDecrementDeviceObjectRef_function_00270970.md) (function, `0x00270970`)
- `0x0089FAFF` → [IoFreeIrp](../../text/24/IoFreeIrp_function_0024DF70.md) (function, `0x0024DF70`)
- `0x0089FB0E` → [IopDecrementDeviceObjectRef](../../text/27/IopDecrementDeviceObjectRef_function_00270970.md) (function, `0x00270970`)
- `0x0089FB27` → [IopDereferenceVpbAndFree](../../text/43/IopDereferenceVpbAndFree_function_0043F474.md) (function, `0x0043F474`)
- `0x0089FB68` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0089FB8C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0089FBB4` → [RtlCopyUnicodeString](../../text/3F/RtlCopyUnicodeString_function_003FEF30.md) (function, `0x003FEF30`)
- `0x0089FC06` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0089FC17` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x0089FC2D` → [IopDecrementDeviceObjectRef](../../text/27/IopDecrementDeviceObjectRef_function_00270970.md) (function, `0x00270970`)
- `0x0089FC42` → [IopDereferenceVpbAndFree](../../text/43/IopDereferenceVpbAndFree_function_0043F474.md) (function, `0x0043F474`)
- `0x0089FD19` → [PsGetParentSilo](../A7/PsGetParentSilo_function_00A70760.md) (function, `0x00A70760`)
- `0x0089FD2F` → [IoFreeIrp](../../text/24/IoFreeIrp_function_0024DF70.md) (function, `0x0024DF70`)
- `0x0089FD3E` → [IopDecrementDeviceObjectRef](../../text/27/IopDecrementDeviceObjectRef_function_00270970.md) (function, `0x00270970`)
- `0x0089FDF5` → [IopCreateSecurityCheck](../../text/3A/IopCreateSecurityCheck_function_003A5DA0.md) (function, `0x003A5DA0`)
- `0x0089FE67` → [KiLowerIrqlProcessIrqlFlags](../../text/4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x0089FEA0` → [IopSymlinkGetECP](../../text/45/IopSymlinkGetECP_function_00458288.md) (function, `0x00458288`)
- `0x0089FEDA` → [IopSymlinkCreateECP](../8A/IopSymlinkCreateECP_function_008A1F90.md) (function, `0x008A1F90`)
- `0x0089FF52` → [IopSymlinkProcessReparse](../A3/IopSymlinkProcessReparse_function_00A330B4.md) (function, `0x00A330B4`)
- `0x008A002E` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x008A0037` → [SeLockSubjectContext](../8C/SeLockSubjectContext_function_008C64C0.md) (function, `0x008C64C0`)
- `0x008A0090` → [SeAccessCheck](../../text/3A/SeAccessCheck_function_003A6BC0.md) (function, `0x003A6BC0`)
- `0x008A00AD` → [SeUnlockSubjectContext](../8C/SeUnlockSubjectContext_function_008C6520.md) (function, `0x008C6520`)
- `0x008A00B9` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x008A00C6` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x008A0159` → [IopSymlinkEnforceEnabledTypes](../A4/IopSymlinkEnforceEnabledTypes_function_00A4CFCC.md) (function, `0x00A4CFCC`)
- `0x008A01AC` → [IoFreeIrp](../../text/24/IoFreeIrp_function_0024DF70.md) (function, `0x0024DF70`)
- `0x008A01BB` → [IopDecrementDeviceObjectRef](../../text/27/IopDecrementDeviceObjectRef_function_00270970.md) (function, `0x00270970`)
- `0x008A01D0` → [IopDereferenceVpbAndFree](../../text/43/IopDereferenceVpbAndFree_function_0043F474.md) (function, `0x0043F474`)
- `0x008A01E9` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008A0202` → [PsGetCurrentServerSilo](../../text/22/PsGetCurrentServerSilo_function_00225710.md) (function, `0x00225710`)
- `0x008A020A` → [PsGetServerSiloServiceSessionId](../../text/45/PsGetServerSiloServiceSessionId_function_0045ED00.md) (function, `0x0045ED00`)
- `0x008A0211` → [PsGetCurrentProcessSessionId](../../text/23/PsGetCurrentProcessSessionId_function_002303D0.md) (function, `0x002303D0`)
- `0x008A022F` → [IopGetDevicePDO](../../text/27/IopGetDevicePDO_function_002724D8.md) (function, `0x002724D8`)
- `0x008A023F` → [IopCheckSessionDeviceAccess](../../text/22/IopCheckSessionDeviceAccess_function_002233D4.md) (function, `0x002233D4`)
- `0x008A024F` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008A0293` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008A02CA` → [RtlGetActiveConsoleId](../../text/43/RtlGetActiveConsoleId_function_00436230.md) (function, `0x00436230`)
- `0x008A02D1` → [PsGetCurrentProcessSessionId](../../text/23/PsGetCurrentProcessSessionId_function_002303D0.md) (function, `0x002303D0`)
- `0x008A02DE` → [PsGetCurrentServerSilo](../../text/22/PsGetCurrentServerSilo_function_00225710.md) (function, `0x00225710`)
- `0x008A02E6` → [PsGetServerSiloServiceSessionId](../../text/45/PsGetServerSiloServiceSessionId_function_0045ED00.md) (function, `0x0045ED00`)
- `0x008A02ED` → [PsGetCurrentProcessSessionId](../../text/23/PsGetCurrentProcessSessionId_function_002303D0.md) (function, `0x002303D0`)
- `0x008A02FA` → [IopAllowRemoteDASD](../../text/4D/IopAllowRemoteDASD_function_004D5BAC.md) (function, `0x004D5BAC`)
- `0x008A034A` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x008A035F` → [SeFastTraverseCheck](../../text/40/SeFastTraverseCheck_function_00400234.md) (function, `0x00400234`)
- `0x008A0382` → [SeLockSubjectContext](../8C/SeLockSubjectContext_function_008C64C0.md) (function, `0x008C64C0`)
- `0x008A03E5` → [SeAccessCheck](../../text/3A/SeAccessCheck_function_003A6BC0.md) (function, `0x003A6BC0`)
- `0x008A0404` → [SeAppendPrivileges](../9D/SeAppendPrivileges_function_009D7980.md) (function, `0x009D7980`)
- `0x008A0411` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (function, `0x00475D80`)
- `0x008A044E` → [IopDeleteFileObjectExtension](../../text/38/IopDeleteFileObjectExtension_function_0038C4F0.md) (function, `0x0038C4F0`)
- `0x008A0491` → [SeTokenIsAdmin](../9F/SeTokenIsAdmin_function_009FE650.md) (function, `0x009FE650`)
- `0x008A0543` → [IopCreateSecurityCheck](../../text/3A/IopCreateSecurityCheck_function_003A5DA0.md) (function, `0x003A5DA0`)
- `0x008A0561` → [PsIsServerSilo](../../text/22/PsIsServerSilo_function_00225828.md) (function, `0x00225828`)
- `0x008A0571` → [IoGetSilo](../../text/43/IoGetSilo_function_00438490.md) (function, `0x00438490`)
- `0x008A05AC` → [KiLowerIrqlProcessIrqlFlags](../../text/4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x008A05C3` → [IopCancelAlertedRequest](../A9/IopCancelAlertedRequest_function_00A948F8.md) (function, `0x00A948F8`)
- `0x008A05E0` → [IopCheckAndUpdateStopOnSymlinkEcp](../70/IopCheckAndUpdateStopOnSymlinkEcp_function_007043E4.md) (function, `0x007043E4`)
- `0x008A05F4` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008A05FE` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008A060B` → [IopDecrementDeviceObjectRef](../../text/27/IopDecrementDeviceObjectRef_function_00270970.md) (function, `0x00270970`)
- `0x008A0624` → [IopDeleteFileObjectExtension](../../text/38/IopDeleteFileObjectExtension_function_0038C4F0.md) (function, `0x0038C4F0`)
- `0x008A0633` → [IopDecrementDeviceObjectRef](../../text/27/IopDecrementDeviceObjectRef_function_00270970.md) (function, `0x00270970`)
- `0x008A0648` → [IopDereferenceVpbAndFree](../../text/43/IopDereferenceVpbAndFree_function_0043F474.md) (function, `0x0043F474`)
- `0x008A0650` → [IoFreeIrp](../../text/24/IoFreeIrp_function_0024DF70.md) (function, `0x0024DF70`)
- `0x008A0674` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008A067C` → [IopDeleteFileObjectExtension](../../text/38/IopDeleteFileObjectExtension_function_0038C4F0.md) (function, `0x0038C4F0`)
- `0x008A0689` → [IopDecrementDeviceObjectRef](../../text/27/IopDecrementDeviceObjectRef_function_00270970.md) (function, `0x00270970`)
- `0x008A06B9` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008A06F1` → [IopIncrementVpbRefCount](../../text/27/IopIncrementVpbRefCount_function_00272820.md) (function, `0x00272820`)
- `0x008A0702` → [IopDereferenceVpbAndFree](../../text/43/IopDereferenceVpbAndFree_function_0043F474.md) (function, `0x0043F474`)
- `0x008A071D` → [KiRaiseIrqlProcessIrqlFlags](../../text/4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x008A0732` → [MmIsDriverVerifying](../../text/4A/MmIsDriverVerifying_function_004A8770.md) (function, `0x004A8770`)
- `0x008A0742` → [VfFastIoSnapState](../../pagevrfy/BB/VfFastIoSnapState_function_00BB97BC.md) (function, `0x00BB97BC`)
- `0x008A07A9` → [IoSetActivityIdThread](../../text/46/IoSetActivityIdThread_function_00466340.md) (function, `0x00466340`)
- `0x008A07B9` → [IofCallDriver](../../text/29/IofCallDriver_function_0029B4B0.md) (function, `0x0029B4B0`)
- `0x008A07C4` → [IoSetActivityIdThread](../../text/46/IoSetActivityIdThread_function_00466340.md) (function, `0x00466340`)
- `0x008A07F6` → [SeAppendPrivileges](../9D/SeAppendPrivileges_function_009D7980.md) (function, `0x009D7980`)
- `0x008A0803` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (function, `0x00475D80`)
- `0x008A0831` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x008A083A` → [IoFreeIrp](../../text/24/IoFreeIrp_function_0024DF70.md) (function, `0x0024DF70`)
- `0x008A0849` → [IopDecrementDeviceObjectRef](../../text/27/IopDecrementDeviceObjectRef_function_00270970.md) (function, `0x00270970`)
- `0x008A086A` → [IopDereferenceVpbAndFree](../../text/43/IopDereferenceVpbAndFree_function_0043F474.md) (function, `0x0043F474`)
- `0x008A0886` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (function, `0x0020FA20`)
- `0x008A089A` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [ObpLookupObjectName](ObpLookupObjectName_function_0089BE90.md) at `0x0089CA58`
- [ObpLookupObjectName](ObpLookupObjectName_function_0089BE90.md) at `0x0089CB20`
- [IopParseFile](../9F/IopParseFile_function_009FDB60.md) at `0x009FDC22`

### Static image references
- `0x0089E52B` → RVA `0x00E0A740` (`.data`; read)
- `0x0089E609` → RVA `0x00FC6AE0` (`ALMOSTRO`; read)
- `0x0089E629` → RVA `0x00AFCBB0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x0089EA8E` → RVA `0x00F8D2A0` (`.data`; read)
- `0x0089EE11` → RVA `0x00F04A20` (`.data`; read)
- `0x0089F1A6` → RVA `0x00E0A9CC` (`.data`; read)
- `0x0089F647` → RVA `0x00FC6E4C` (`ALMOSTRO`; read)
- `0x0089FE1C` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x008A021A` → RVA `0x00E66120` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **143**
  - `0x0089E634` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x0089E6F4` → [IopCheckDeviceAndDriver](../../text/3F/IopCheckDeviceAndDriver_function_003FCBE0.md) (`PAGE` → `.text`)
  - `0x0089E900` → [IopCheckVpbMounted](../../text/27/IopCheckVpbMounted_function_00270540.md) (`PAGE` → `.text`)
  - `0x0089E93C` → [IoGetAttachedDevice](../../text/41/IoGetAttachedDevice_function_00410810.md) (`PAGE` → `.text`)
  - `0x0089E9B7` → [IopDereferenceVpbAndFree](../../text/43/IopDereferenceVpbAndFree_function_0043F474.md) (`PAGE` → `.text`)
  - `0x0089E9C4` → [IopDecrementDeviceObjectRef](../../text/27/IopDecrementDeviceObjectRef_function_00270970.md) (`PAGE` → `.text`)
  - `0x0089EA95` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x0089EB0C` → [SeAccessCheck](../../text/3A/SeAccessCheck_function_003A6BC0.md) (`PAGE` → `.text`)
  - `0x0089EB96` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x0089EBA3` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x0089EC16` → [IopIncrementVpbRefCount](../../text/27/IopIncrementVpbRefCount_function_00272820.md) (`PAGE` → `.text`)
  - `0x0089EC63` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (`PAGE` → `.text`)
  - `0x0089ED23` → [IopDequeueIrpFromThread](../../text/20/IopDequeueIrpFromThread_function_00207B20.md) (`PAGE` → `.text`)
  - `0x0089ED3A` → [IoFreeIrp](../../text/24/IoFreeIrp_function_0024DF70.md) (`PAGE` → `.text`)
  - `0x0089ED65` → [IoGetRelatedDeviceObject](../../text/29/IoGetRelatedDeviceObject_function_0029B120.md) (`PAGE` → `.text`)
  - `0x0089ED92` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (`PAGE` → `.text`)
  - `0x0089EE43` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x0089EE71` → [VfFastIoCheckState](../../pagevrfy/BB/VfFastIoCheckState_function_00BB9440.md) (`PAGE` → `PAGEVRFY`)
  - `0x0089EE86` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0089EEDC` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0089EEE6` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0089EEF0` → [MmIsDriverVerifying](../../text/4A/MmIsDriverVerifying_function_004A8770.md) (`PAGE` → `.text`)
  - `0x0089EF00` → [VfFastIoSnapState](../../pagevrfy/BB/VfFastIoSnapState_function_00BB97BC.md) (`PAGE` → `PAGEVRFY`)
  - `0x0089EF28` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0089EF63` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x0089EF85` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x0089EFE1` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0089EFF2` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x0089F001` → [IopDecrementDeviceObjectRef](../../text/27/IopDecrementDeviceObjectRef_function_00270970.md) (`PAGE` → `.text`)
  - `0x0089F01A` → [IopDereferenceVpbAndFree](../../text/43/IopDereferenceVpbAndFree_function_0043F474.md) (`PAGE` → `.text`)
  - `0x0089F061` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x0089F129` → [IoFreeIrp](../../text/24/IoFreeIrp_function_0024DF70.md) (`PAGE` → `.text`)
  - `0x0089F136` → [IopDecrementDeviceObjectRef](../../text/27/IopDecrementDeviceObjectRef_function_00270970.md) (`PAGE` → `.text`)
  - `0x0089F14B` → [IopDereferenceVpbAndFree](../../text/43/IopDereferenceVpbAndFree_function_0043F474.md) (`PAGE` → `.text`)
  - `0x0089F161` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x0089F178` → [VfFastIoCheckState](../../pagevrfy/BB/VfFastIoCheckState_function_00BB9440.md) (`PAGE` → `PAGEVRFY`)
  - `0x0089F1C7` → [IopAllocateIrpExReturn](../../text/20/IopAllocateIrpExReturn_function_00207720.md) (`PAGE` → `.text`)
  - `0x0089F3B8` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0089F3D6` → [RtlCopyUnicodeString](../../text/3F/RtlCopyUnicodeString_function_003FEF30.md) (`PAGE` → `.text`)
  - `0x0089F42A` → [KeInitializeEvent](../../text/40/KeInitializeEvent_function_0040DD10.md) (`PAGE` → `.text`)
  - `0x0089F43F` → [IopQueueThreadIrp](../../text/20/IopQueueThreadIrp_function_002075C0.md) (`PAGE` → `.text`)
  - `0x0089F46A` → [IofCallDriver](../../text/29/IofCallDriver_function_0029B4B0.md) (`PAGE` → `.text`)
  - `0x0089F4A9` → [IopSetFileObjectExtensionFlag](../../text/43/IopSetFileObjectExtensionFlag_function_0043D710.md) (`PAGE` → `.text`)
  - `0x0089F510` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (`PAGE` → `.text`)
  - `0x0089F53A` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0089F545` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x0089F57E` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0089F597` → [RtlCopyUnicodeString](../../text/3F/RtlCopyUnicodeString_function_003FEF30.md) (`PAGE` → `.text`)
  - `0x0089F622` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x0089F6F7` → [PsIsHostSilo](../../text/44/PsIsHostSilo_function_00443B30.md) (`PAGE` → `.text`)
  - `0x0089F70D` → [IoGetSilo](../../text/43/IoGetSilo_function_00438490.md) (`PAGE` → `.text`)
  - `0x0089F715` → [PsIsHostSilo](../../text/44/PsIsHostSilo_function_00443B30.md) (`PAGE` → `.text`)
  - `0x0089F751` → [PsIsHostSilo](../../text/44/PsIsHostSilo_function_00443B30.md) (`PAGE` → `.text`)
  - `0x0089F766` → [PsAcquireSiloHardReference](../../text/46/PsAcquireSiloHardReference_function_00467620.md) (`PAGE` → `.text`)
  - `0x0089F798` → [IopGetSetSpecificExtension](../../text/42/IopGetSetSpecificExtension_function_0042EE80.md) (`PAGE` → `.text`)
  - `0x0089F7D7` → [ObfReferenceObjectWithTag](../../text/21/ObfReferenceObjectWithTag_function_00210710.md) (`PAGE` → `.text`)
  - `0x0089F881` → [IopCreateSecurityCheck](../../text/3A/IopCreateSecurityCheck_function_003A5DA0.md) (`PAGE` → `.text`)
  - `0x0089F896` → [IopDecrementDeviceObjectRef](../../text/27/IopDecrementDeviceObjectRef_function_00270970.md) (`PAGE` → `.text`)
  - `0x0089F8A3` → [IopDereferenceVpbAndFree](../../text/43/IopDereferenceVpbAndFree_function_0043F474.md) (`PAGE` → `.text`)
  - `0x0089F904` → [IopSymlinkGetECP](../../text/45/IopSymlinkGetECP_function_00458288.md) (`PAGE` → `.text`)
  - `0x0089F91C` → [IopSymlinkGetMostRecentlyUsedName](../../text/48/IopSymlinkGetMostRecentlyUsedName_function_0048476C.md) (`PAGE` → `.text`)
  - `0x0089F989` → [IopDecrementDeviceObjectRef](../../text/27/IopDecrementDeviceObjectRef_function_00270970.md) (`PAGE` → `.text`)
  - `0x0089F9A9` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (`PAGE` → `.text`)
  - `0x0089F9FB` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0089FA03` → [IopDeleteFileObjectExtension](../../text/38/IopDeleteFileObjectExtension_function_0038C4F0.md) (`PAGE` → `.text`)
  - `0x0089FA12` → [IopDecrementDeviceObjectRef](../../text/27/IopDecrementDeviceObjectRef_function_00270970.md) (`PAGE` → `.text`)
  - `0x0089FA27` → [IopDereferenceVpbAndFree](../../text/43/IopDereferenceVpbAndFree_function_0043F474.md) (`PAGE` → `.text`)
  - `0x0089FA2F` → [IoFreeIrp](../../text/24/IoFreeIrp_function_0024DF70.md) (`PAGE` → `.text`)
  - `0x0089FA90` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (`PAGE` → `.text`)
  - `0x0089FACB` → [PsReleaseSiloHardReference](../../text/38/PsReleaseSiloHardReference_function_0038DEA0.md) (`PAGE` → `.text`)
  - `0x0089FAE1` → [IopDereferenceVpbAndFree](../../text/43/IopDereferenceVpbAndFree_function_0043F474.md) (`PAGE` → `.text`)
  - `0x0089FAEE` → [IopDecrementDeviceObjectRef](../../text/27/IopDecrementDeviceObjectRef_function_00270970.md) (`PAGE` → `.text`)
  - `0x0089FAFF` → [IoFreeIrp](../../text/24/IoFreeIrp_function_0024DF70.md) (`PAGE` → `.text`)
  - `0x0089FB0E` → [IopDecrementDeviceObjectRef](../../text/27/IopDecrementDeviceObjectRef_function_00270970.md) (`PAGE` → `.text`)
  - `0x0089FB27` → [IopDereferenceVpbAndFree](../../text/43/IopDereferenceVpbAndFree_function_0043F474.md) (`PAGE` → `.text`)
  - `0x0089FB68` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0089FB8C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0089FBB4` → [RtlCopyUnicodeString](../../text/3F/RtlCopyUnicodeString_function_003FEF30.md) (`PAGE` → `.text`)
  - `0x0089FC06` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0089FC17` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x0089FC2D` → [IopDecrementDeviceObjectRef](../../text/27/IopDecrementDeviceObjectRef_function_00270970.md) (`PAGE` → `.text`)
  - `0x0089FC42` → [IopDereferenceVpbAndFree](../../text/43/IopDereferenceVpbAndFree_function_0043F474.md) (`PAGE` → `.text`)
  - `0x0089FD2F` → [IoFreeIrp](../../text/24/IoFreeIrp_function_0024DF70.md) (`PAGE` → `.text`)
  - `0x0089FD3E` → [IopDecrementDeviceObjectRef](../../text/27/IopDecrementDeviceObjectRef_function_00270970.md) (`PAGE` → `.text`)
  - `0x0089FDF5` → [IopCreateSecurityCheck](../../text/3A/IopCreateSecurityCheck_function_003A5DA0.md) (`PAGE` → `.text`)
  - `0x0089FE67` → [KiLowerIrqlProcessIrqlFlags](../../text/4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (`PAGE` → `.text`)
  - `0x0089FEA0` → [IopSymlinkGetECP](../../text/45/IopSymlinkGetECP_function_00458288.md) (`PAGE` → `.text`)
  - `0x008A002E` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x008A0090` → [SeAccessCheck](../../text/3A/SeAccessCheck_function_003A6BC0.md) (`PAGE` → `.text`)
  - `0x008A00B9` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x008A00C6` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x008A01AC` → [IoFreeIrp](../../text/24/IoFreeIrp_function_0024DF70.md) (`PAGE` → `.text`)
  - `0x008A01BB` → [IopDecrementDeviceObjectRef](../../text/27/IopDecrementDeviceObjectRef_function_00270970.md) (`PAGE` → `.text`)
  - `0x008A01D0` → [IopDereferenceVpbAndFree](../../text/43/IopDereferenceVpbAndFree_function_0043F474.md) (`PAGE` → `.text`)
  - `0x008A01E9` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008A0202` → [PsGetCurrentServerSilo](../../text/22/PsGetCurrentServerSilo_function_00225710.md) (`PAGE` → `.text`)
  - `0x008A020A` → [PsGetServerSiloServiceSessionId](../../text/45/PsGetServerSiloServiceSessionId_function_0045ED00.md) (`PAGE` → `.text`)
  - `0x008A0211` → [PsGetCurrentProcessSessionId](../../text/23/PsGetCurrentProcessSessionId_function_002303D0.md) (`PAGE` → `.text`)
  - `0x008A022F` → [IopGetDevicePDO](../../text/27/IopGetDevicePDO_function_002724D8.md) (`PAGE` → `.text`)
  - `0x008A023F` → [IopCheckSessionDeviceAccess](../../text/22/IopCheckSessionDeviceAccess_function_002233D4.md) (`PAGE` → `.text`)
  - `0x008A024F` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008A0293` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008A02CA` → [RtlGetActiveConsoleId](../../text/43/RtlGetActiveConsoleId_function_00436230.md) (`PAGE` → `.text`)
  - `0x008A02D1` → [PsGetCurrentProcessSessionId](../../text/23/PsGetCurrentProcessSessionId_function_002303D0.md) (`PAGE` → `.text`)
  - `0x008A02DE` → [PsGetCurrentServerSilo](../../text/22/PsGetCurrentServerSilo_function_00225710.md) (`PAGE` → `.text`)
  - `0x008A02E6` → [PsGetServerSiloServiceSessionId](../../text/45/PsGetServerSiloServiceSessionId_function_0045ED00.md) (`PAGE` → `.text`)
  - `0x008A02ED` → [PsGetCurrentProcessSessionId](../../text/23/PsGetCurrentProcessSessionId_function_002303D0.md) (`PAGE` → `.text`)
  - `0x008A02FA` → [IopAllowRemoteDASD](../../text/4D/IopAllowRemoteDASD_function_004D5BAC.md) (`PAGE` → `.text`)
  - `0x008A034A` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x008A035F` → [SeFastTraverseCheck](../../text/40/SeFastTraverseCheck_function_00400234.md) (`PAGE` → `.text`)
  - `0x008A03E5` → [SeAccessCheck](../../text/3A/SeAccessCheck_function_003A6BC0.md) (`PAGE` → `.text`)
  - `0x008A0411` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (`PAGE` → `.text`)
  - `0x008A044E` → [IopDeleteFileObjectExtension](../../text/38/IopDeleteFileObjectExtension_function_0038C4F0.md) (`PAGE` → `.text`)
  - `0x008A0543` → [IopCreateSecurityCheck](../../text/3A/IopCreateSecurityCheck_function_003A5DA0.md) (`PAGE` → `.text`)
  - `0x008A0561` → [PsIsServerSilo](../../text/22/PsIsServerSilo_function_00225828.md) (`PAGE` → `.text`)
  - `0x008A0571` → [IoGetSilo](../../text/43/IoGetSilo_function_00438490.md) (`PAGE` → `.text`)
  - `0x008A05AC` → [KiLowerIrqlProcessIrqlFlags](../../text/4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (`PAGE` → `.text`)
  - `0x008A05F4` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008A05FE` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008A060B` → [IopDecrementDeviceObjectRef](../../text/27/IopDecrementDeviceObjectRef_function_00270970.md) (`PAGE` → `.text`)
  - `0x008A0624` → [IopDeleteFileObjectExtension](../../text/38/IopDeleteFileObjectExtension_function_0038C4F0.md) (`PAGE` → `.text`)
  - `0x008A0633` → [IopDecrementDeviceObjectRef](../../text/27/IopDecrementDeviceObjectRef_function_00270970.md) (`PAGE` → `.text`)
  - `0x008A0648` → [IopDereferenceVpbAndFree](../../text/43/IopDereferenceVpbAndFree_function_0043F474.md) (`PAGE` → `.text`)
  - `0x008A0650` → [IoFreeIrp](../../text/24/IoFreeIrp_function_0024DF70.md) (`PAGE` → `.text`)
  - `0x008A0674` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008A067C` → [IopDeleteFileObjectExtension](../../text/38/IopDeleteFileObjectExtension_function_0038C4F0.md) (`PAGE` → `.text`)
  - `0x008A0689` → [IopDecrementDeviceObjectRef](../../text/27/IopDecrementDeviceObjectRef_function_00270970.md) (`PAGE` → `.text`)
  - `0x008A06B9` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008A06F1` → [IopIncrementVpbRefCount](../../text/27/IopIncrementVpbRefCount_function_00272820.md) (`PAGE` → `.text`)
  - `0x008A0702` → [IopDereferenceVpbAndFree](../../text/43/IopDereferenceVpbAndFree_function_0043F474.md) (`PAGE` → `.text`)
  - `0x008A071D` → [KiRaiseIrqlProcessIrqlFlags](../../text/4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (`PAGE` → `.text`)
  - `0x008A0732` → [MmIsDriverVerifying](../../text/4A/MmIsDriverVerifying_function_004A8770.md) (`PAGE` → `.text`)
  - `0x008A0742` → [VfFastIoSnapState](../../pagevrfy/BB/VfFastIoSnapState_function_00BB97BC.md) (`PAGE` → `PAGEVRFY`)
  - `0x008A07A9` → [IoSetActivityIdThread](../../text/46/IoSetActivityIdThread_function_00466340.md) (`PAGE` → `.text`)
  - `0x008A07B9` → [IofCallDriver](../../text/29/IofCallDriver_function_0029B4B0.md) (`PAGE` → `.text`)
  - `0x008A07C4` → [IoSetActivityIdThread](../../text/46/IoSetActivityIdThread_function_00466340.md) (`PAGE` → `.text`)
  - `0x008A0803` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (`PAGE` → `.text`)
  - `0x008A0831` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x008A083A` → [IoFreeIrp](../../text/24/IoFreeIrp_function_0024DF70.md) (`PAGE` → `.text`)
  - `0x008A0849` → [IopDecrementDeviceObjectRef](../../text/27/IopDecrementDeviceObjectRef_function_00270970.md) (`PAGE` → `.text`)
  - `0x008A086A` → [IopDereferenceVpbAndFree](../../text/43/IopDereferenceVpbAndFree_function_0043F474.md) (`PAGE` → `.text`)
  - `0x008A0886` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (`PAGE` → `.text`)
  - `0x008A089A` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0089E510  4C 8B DC                        mov r11, rsp
0089E513  49 89 5B 10                     mov qword ptr [r11 + 0x10], rbx
0089E517  49 89 73 20                     mov qword ptr [r11 + 0x20], rsi
0089E51B  57                              push rdi
0089E51C  41 54                           push r12
0089E51E  41 55                           push r13
0089E520  41 56                           push r14
0089E522  41 57                           push r15
0089E524  48 81 EC 80 01 00 00            sub rsp, 0x180
0089E52B  48 8B 05 0E C2 56 00            mov rax, qword ptr [rip + 0x56c20e]
0089E532  48 33 C4                        xor rax, rsp
0089E535  48 89 84 24 78 01 00 00         mov qword ptr [rsp + 0x178], rax
0089E53D  44 88 4C 24 68                  mov byte ptr [rsp + 0x68], r9b
0089E542  4D 8B E8                        mov r13, r8
0089E545  4C 89 84 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], r8
0089E54D  4C 8B F9                        mov r15, rcx
0089E550  48 89 8C 24 20 01 00 00         mov qword ptr [rsp + 0x120], rcx
0089E558  48 8B 84 24 D8 01 00 00         mov rax, qword ptr [rsp + 0x1d8]
0089E560  48 89 84 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rax
0089E568  48 8B B4 24 E0 01 00 00         mov rsi, qword ptr [rsp + 0x1e0]
0089E570  48 89 B4 24 80 00 00 00         mov qword ptr [rsp + 0x80], rsi
0089E578  48 8B BC 24 E8 01 00 00         mov rdi, qword ptr [rsp + 0x1e8]
0089E580  48 89 BC 24 60 01 00 00         mov qword ptr [rsp + 0x160], rdi
0089E588  48 8B 84 24 F8 01 00 00         mov rax, qword ptr [rsp + 0x1f8]
0089E590  48 89 84 24 F0 00 00 00         mov qword ptr [rsp + 0xf0], rax
0089E598  4C 8B B4 24 00 02 00 00         mov r14, qword ptr [rsp + 0x200]
0089E5A0  4C 89 B4 24 08 01 00 00         mov qword ptr [rsp + 0x108], r14
0089E5A8  45 33 E4                        xor r12d, r12d
0089E5AB  45 89 A3 E4 FE FF FF            mov dword ptr [r11 - 0x11c], r12d
0089E5B2  44 89 64 24 64                  mov dword ptr [rsp + 0x64], r12d
0089E5B7  0F 57 C0                        xorps xmm0, xmm0
0089E5BA  0F 11 84 24 10 01 00 00         movups xmmword ptr [rsp + 0x110], xmm0
0089E5C2  0F 57 C9                        xorps xmm1, xmm1
0089E5C5  33 C0                           xor eax, eax
0089E5C7  41 0F 11 4B 90                  movups xmmword ptr [r11 - 0x70], xmm1
0089E5CC  49 89 43 A0                     mov qword ptr [r11 - 0x60], rax
0089E5D0  44 89 A4 24 F8 00 00 00         mov dword ptr [rsp + 0xf8], r12d
0089E5D8  88 84 24 88 00 00 00            mov byte ptr [rsp + 0x88], al
0089E5DF  45 89 A3 2C FF FF FF            mov dword ptr [r11 - 0xd4], r12d
0089E5E6  41 0F 11 43 80                  movups xmmword ptr [r11 - 0x80], xmm0
0089E5EB  4D 89 A3 F0 FE FF FF            mov qword ptr [r11 - 0x110], r12
0089E5F2  4C 89 A4 24 E8 00 00 00         mov qword ptr [rsp + 0xe8], r12
0089E5FA  4C 89 A4 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], r12
0089E602  4D 89 A3 38 FF FF FF            mov qword ptr [r11 - 0xc8], r12
0089E609  48 3B 15 D0 84 72 00            cmp rdx, qword ptr [rip + 0x7284d0]
0089E610  0F 85 57 06 00 00               jne 0x14089ec6d
0089E616  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0089E61F  48 89 84 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rax
0089E627  B3 04                           mov bl, 4
0089E629  48 8D 15 80 E5 25 00            lea rdx, [rip + 0x25e580]
0089E630  49 8D 4B 80                     lea rcx, [r11 - 0x80]
0089E634  E8 47 C1 B8 FF                  call 0x14042a780
0089E639  49 B9 40 00 11 00 00 01 60 00   movabs r9, 0x60010000110040
0089E643  41 B8 03 00 00 A0               mov r8d, 0xa0000003
0089E649  48 BA 84 00 02 80 10 00 00 00   movabs rdx, 0x1080020084
0089E653  B8 E0 00 00 00                  mov eax, 0xe0
0089E658  0F 1F 84 00 00 00 00 00         nop dword ptr [rax + rax]
0089E660  4D 89 26                        mov qword ptr [r14], r12
0089E663  4C 89 A4 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], r12
0089E66B  48 85 FF                        test rdi, rdi
0089E66E  0F 84 F9 05 00 00               je 0x14089ec6d
0089E674  66 83 3F 08                     cmp word ptr [rdi], 8
0089E678  0F 85 EF 05 00 00               jne 0x14089ec6d
0089E67E  66 39 47 02                     cmp word ptr [rdi + 2], ax
0089E682  0F 85 E5 05 00 00               jne 0x14089ec6d
0089E688  4D 8B F7                        mov r14, r15
0089E68B  4C 89 7C 24 70                  mov qword ptr [rsp + 0x70], r15
0089E690  83 7F 20 01                     cmp dword ptr [rdi + 0x20], 1
0089E694  0F 84 DA 21 00 00               je 0x1408a0874
0089E69A  8B 87 98 00 00 00               mov eax, dword ptr [rdi + 0x98]
0089E6A0  A8 10                           test al, 0x10
0089E6A2  0F 85 60 1A 00 00               jne 0x1408a0108
0089E6A8  48 8B 47 28                     mov rax, qword ptr [rdi + 0x28]
0089E6AC  48 85 C0                        test rax, rax
0089E6AF  0F 85 48 03 00 00               jne 0x14089e9fd
0089E6B5  41 83 7E 48 07                  cmp dword ptr [r14 + 0x48], 7
0089E6BA  75 32                           jne 0x14089e6ee
0089E6BC  4C 89 74 24 78                  mov qword ptr [rsp + 0x78], r14
0089E6C1  49 8B C6                        mov rax, r14
0089E6C4  4D 8B C6                        mov r8, r14
0089E6C7  4D 8B CE                        mov r9, r14
0089E6CA  49 8B D6                        mov rdx, r14
0089E6CD  4D 8B D6                        mov r10, r14
0089E6D0  49 8B C8                        mov rcx, r8
0089E6D3  4D 8B D9                        mov r11, r9
0089E6D6  4C 39 62 38                     cmp qword ptr [rdx + 0x38], r12
0089E6DA  0F 84 FF 19 00 00               je 0x1408a00df
0089E6E0  48 85 C0                        test rax, rax
0089E6E3  74 09                           je 0x14089e6ee
0089E6E5  49 3B CE                        cmp rcx, r14
0089E6E8  0F 85 51 05 00 00               jne 0x14089ec3f
0089E6EE  49 8B D6                        mov rdx, r14
0089E6F1  48 8B CF                        mov rcx, rdi
0089E6F4  E8 E7 E4 B5 FF                  call 0x1403fcbe0
0089E6F9  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
0089E6FD  85 C0                           test eax, eax
0089E6FF  0F 88 65 0A 00 00               js 0x14089f16a
0089E705  49 8B 86 38 01 00 00            mov rax, qword ptr [r14 + 0x138]
0089E70C  F7 40 20 00 04 00 00            test dword ptr [rax + 0x20], 0x400
0089E713  0F 85 DF 1A 00 00               jne 0x1408a01f8
0089E719  48 8B 0D C0 83 72 00            mov rcx, qword ptr [rip + 0x7283c0]
0089E720  41 8B 45 10                     mov eax, dword ptr [r13 + 0x10]
0089E724  85 C0                           test eax, eax
0089E726  79 03                           jns 0x14089e72b
0089E728  0B 41 4C                        or eax, dword ptr [rcx + 0x4c]
0089E72B  0F BA E0 1E                     bt eax, 0x1e
0089E72F  73 03                           jae 0x14089e734
0089E731  0B 41 50                        or eax, dword ptr [rcx + 0x50]
0089E734  0F BA E0 1D                     bt eax, 0x1d
0089E738  73 03                           jae 0x14089e73d
0089E73A  0B 41 54                        or eax, dword ptr [rcx + 0x54]
0089E73D  0F BA E0 1C                     bt eax, 0x1c
0089E741  73 03                           jae 0x14089e746
0089E743  0B 41 58                        or eax, dword ptr [rcx + 0x58]
0089E746  25 FF FF FF 0F                  and eax, 0xfffffff
0089E74B  41 89 45 10                     mov dword ptr [r13 + 0x10], eax
0089E74F  48 8B 0D 8A 83 72 00            mov rcx, qword ptr [rip + 0x72838a]
0089E756  41 8B 45 18                     mov eax, dword ptr [r13 + 0x18]
0089E75A  85 C0                           test eax, eax
0089E75C  79 03                           jns 0x14089e761
0089E75E  0B 41 4C                        or eax, dword ptr [rcx + 0x4c]
0089E761  0F BA E0 1E                     bt eax, 0x1e
0089E765  73 03                           jae 0x14089e76a
0089E767  0B 41 50                        or eax, dword ptr [rcx + 0x50]
0089E76A  0F BA E0 1D                     bt eax, 0x1d
0089E76E  73 03                           jae 0x14089e773
0089E770  0B 41 54                        or eax, dword ptr [rcx + 0x54]
0089E773  0F BA E0 1C                     bt eax, 0x1c
0089E777  73 03                           jae 0x14089e77c
0089E779  0B 41 58                        or eax, dword ptr [rcx + 0x58]
0089E77C  25 FF FF FF 0F                  and eax, 0xfffffff
0089E781  41 89 45 18                     mov dword ptr [r13 + 0x18], eax
0089E785  48 8B 0D 54 83 72 00            mov rcx, qword ptr [rip + 0x728354]
0089E78C  49 8B 45 48                     mov rax, qword ptr [r13 + 0x48]
0089E790  0F 10 41 4C                     movups xmm0, xmmword ptr [rcx + 0x4c]
0089E794  0F 11 40 08                     movups xmmword ptr [rax + 8], xmm0
0089E798  45 8B 7D 10                     mov r15d, dword ptr [r13 + 0x10]
0089E79C  44 89 BC 24 B8 00 00 00         mov dword ptr [rsp + 0xb8], r15d
0089E7A4  44 38 64 24 68                  cmp byte ptr [rsp + 0x68], r12b
0089E7A9  0F 84 6C 02 00 00               je 0x14089ea1b
0089E7AF  41 B0 01                        mov r8b, 1
0089E7B2  48 8D 57 40                     lea rdx, [rdi + 0x40]
0089E7B6  44 8B 4F 58                     mov r9d, dword ptr [rdi + 0x58]
0089E7BA  49 8B CD                        mov rcx, r13
0089E7BD  E8 0E 21 00 00                  call 0x1408a08d0
0089E7C2  44 38 A7 88 00 00 00            cmp byte ptr [rdi + 0x88], r12b
0089E7C9  0F 85 0B 02 00 00               jne 0x14089e9da
0089E7CF  41 F7 45 0C 00 01 00 00         test dword ptr [r13 + 0xc], 0x100
0089E7D7  0F 85 07 02 00 00               jne 0x14089e9e4
0089E7DD  48 8B 4F 28                     mov rcx, qword ptr [rdi + 0x28]
0089E7E1  8B 94 24 88 00 00 00            mov edx, dword ptr [rsp + 0x88]
0089E7E8  48 85 C9                        test rcx, rcx
0089E7EB  0F 85 BC 03 00 00               jne 0x14089ebad
0089E7F1  44 0F B6 4C 24 68               movzx r9d, byte ptr [rsp + 0x68]
0089E7F7  45 84 C9                        test r9b, r9b
0089E7FA  0F 84 0B 02 00 00               je 0x14089ea0b
0089E800  48 85 C9                        test rcx, rcx
0089E803  0F 85 10 09 00 00               jne 0x14089f119
0089E809  44 38 A7 88 00 00 00            cmp byte ptr [rdi + 0x88], r12b
0089E810  75 71                           jne 0x14089e883
0089E812  80 E3 DF                        and bl, 0xdf
0089E815  41 8B 46 34                     mov eax, dword ptr [r14 + 0x34]
0089E819  66 44 39 26                     cmp word ptr [rsi], r12w
0089E81D  0F 84 3A 02 00 00               je 0x14089ea5d
0089E823  25 00 01 02 00                  and eax, 0x20100
0089E828  3D 00 00 02 00                  cmp eax, 0x20000
0089E82D  74 28                           je 0x14089e857
0089E82F  45 84 C9                        test r9b, r9b
0089E832  74 23                           je 0x14089e857
0089E834  44 88 64 24 60                  mov byte ptr [rsp + 0x60], r12b
0089E839  48 8D 54 24 60                  lea rdx, [rsp + 0x60]
0089E83E  49 8D 4D 20                     lea rcx, [r13 + 0x20]
0089E842  E8 2D 32 18 00                  call 0x140a21a74
0089E847  44 38 64 24 60                  cmp byte ptr [rsp + 0x60], r12b
0089E84C  0F 85 A8 17 00 00               jne 0x14089fffa
0089E852  4C 8B 74 24 70                  mov r14, qword ptr [rsp + 0x70]
0089E857  41 8B 45 0C                     mov eax, dword ptr [r13 + 0xc]
0089E85B  A8 01                           test al, 1
0089E85D  0F 84 CE 1A 00 00               je 0x1408a0331
0089E863  80 CB 01                        or bl, 1
0089E866  F6 C3 20                        test bl, 0x20
0089E869  74 09                           je 0x14089e874
0089E86B  49 8D 4D 20                     lea rcx, [r13 + 0x20]
0089E86F  E8 AC 7C 02 00                  call 0x1408c6520
0089E874  F6 C3 01                        test bl, 1
0089E877  0F 84 3F 01 00 00               je 0x14089e9bc
0089E87D  44 0F B6 4C 24 68               movzx r9d, byte ptr [rsp + 0x68]
0089E883  44 38 A7 89 00 00 00            cmp byte ptr [rdi + 0x89], r12b
0089E88A  0F 85 43 01 00 00               jne 0x14089e9d3
0089E890  44 38 A7 8A 00 00 00            cmp byte ptr [rdi + 0x8a], r12b
0089E897  0F 85 36 01 00 00               jne 0x14089e9d3
0089E89D  32 C0                           xor al, al
0089E89F  80 E3 BF                        and bl, 0xbf
0089E8A2  0A D8                           or bl, al
0089E8A4  4C 8B 84 24 80 00 00 00         mov r8, qword ptr [rsp + 0x80]
0089E8AC  66 45 39 20                     cmp word ptr [r8], r12w
0089E8B0  0F 84 78 01 00 00               je 0x14089ea2e
0089E8B6  80 E3 F7                        and bl, 0xf7
0089E8B9  4D 8B EC                        mov r13, r12
0089E8BC  4C 89 A4 24 90 00 00 00         mov qword ptr [rsp + 0x90], r12
0089E8C4  48 8B 57 28                     mov rdx, qword ptr [rdi + 0x28]
0089E8C8  48 85 D2                        test rdx, rdx
0089E8CB  0F 85 04 03 00 00               jne 0x14089ebd5
0089E8D1  49 8B F6                        mov rsi, r14
0089E8D4  4C 89 74 24 78                  mov qword ptr [rsp + 0x78], r14
0089E8D9  49 8B CE                        mov rcx, r14
0089E8DC  4D 39 66 38                     cmp qword ptr [r14 + 0x38], r12
0089E8E0  74 43                           je 0x14089e925
0089E8E2  F6 C3 08                        test bl, 8
0089E8E5  75 3E                           jne 0x14089e925
0089E8E7  41 F7 46 34 00 01 00 00         test dword ptr [r14 + 0x34], 0x100
0089E8EF  0F 85 64 14 00 00               jne 0x14089fd59
0089E8F5  4C 8D 4C 24 64                  lea r9, [rsp + 0x64]
0089E8FA  49 8B D6                        mov rdx, r14
0089E8FD  48 8B CF                        mov rcx, rdi
0089E900  E8 3B 1C 9D FF                  call 0x140270540
0089E905  4C 8B E8                        mov r13, rax
0089E908  48 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], rax
0089E910  48 85 C0                        test rax, rax
0089E913  0F 84 DA 11 00 00               je 0x14089faf3
0089E919  48 8B 70 08                     mov rsi, qword ptr [rax + 8]
0089E91D  48 89 74 24 78                  mov qword ptr [rsp + 0x78], rsi
0089E922  48 8B CE                        mov rcx, rsi
0089E925  8B 87 98 00 00 00               mov eax, dword ptr [rdi + 0x98]
0089E92B  A8 01                           test al, 1
0089E92D  0F 85 C2 00 00 00               jne 0x14089e9f5
0089E933  4C 39 61 18                     cmp qword ptr [rcx + 0x18], r12
0089E937  74 10                           je 0x14089e949
0089E939  48 8B CE                        mov rcx, rsi
0089E93C  E8 CF 1E B7 FF                  call 0x140410810
0089E941  48 8B F0                        mov rsi, rax
0089E944  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
0089E949  41 8B 56 34                     mov edx, dword ptr [r14 + 0x34]
0089E94D  F7 C2 01 00 04 00               test edx, 0x40001
0089E953  0F 84 29 08 00 00               je 0x14089f182
0089E959  41 F7 46 30 00 01 60 00         test dword ptr [r14 + 0x30], 0x600100
0089E961  0F 94 C1                        sete cl
0089E964  0F BA E2 08                     bt edx, 8
0089E968  0F 93 C0                        setae al
0089E96B  84 C8                           test al, cl
0089E96D  0F 84 0F 08 00 00               je 0x14089f182
0089E973  44 88 64 24 60                  mov byte ptr [rsp + 0x60], r12b
0089E978  48 8B 8C 24 D8 00 00 00         mov rcx, qword ptr [rsp + 0xd8]
0089E980  48 83 C1 20                     add rcx, 0x20
0089E984  48 8D 54 24 60                  lea rdx, [rsp + 0x60]
0089E989  E8 E6 30 18 00                  call 0x140a21a74
0089E98E  44 38 64 24 60                  cmp byte ptr [rsp + 0x60], r12b
0089E993  0F 84 E9 07 00 00               je 0x14089f182
0089E999  4D 85 ED                        test r13, r13
0089E99C  74 1E                           je 0x14089e9bc
0089E99E  49 8B 45 08                     mov rax, qword ptr [r13 + 8]
0089E9A2  F7 40 30 00 00 02 00            test dword ptr [rax + 0x30], 0x20000
0089E9A9  0F 85 D3 07 00 00               jne 0x14089f182
0089E9AF  4D 85 ED                        test r13, r13
0089E9B2  74 08                           je 0x14089e9bc
0089E9B4  49 8B CD                        mov rcx, r13
0089E9B7  E8 B8 0A BA FF                  call 0x14043f474
0089E9BC  45 33 C0                        xor r8d, r8d
0089E9BF  33 D2                           xor edx, edx
0089E9C1  49 8B CE                        mov rcx, r14
0089E9C4  E8 A7 1F 9D FF                  call 0x140270970
0089E9C9  B8 22 00 00 C0                  mov eax, 0xc0000022
0089E9CE  E9 BC 1E 00 00                  jmp 0x1408a088f
0089E9D3  B0 40                           mov al, 0x40
0089E9D5  E9 C5 FE FF FF                  jmp 0x14089e89f
0089E9DA  66 44 39 26                     cmp word ptr [rsi], r12w
0089E9DE  0F 85 EB FD FF FF               jne 0x14089e7cf
0089E9E4  45 0B 7D 14                     or r15d, dword ptr [r13 + 0x14]
0089E9E8  44 89 BC 24 B8 00 00 00         mov dword ptr [rsp + 0xb8], r15d
0089E9F0  E9 E8 FD FF FF                  jmp 0x14089e7dd
0089E9F5  80 CB 02                        or bl, 2
0089E9F8  E9 4C FF FF FF                  jmp 0x14089e949
0089E9FD  4C 8B 70 08                     mov r14, qword ptr [rax + 8]
0089EA01  4C 89 74 24 70                  mov qword ptr [rsp + 0x70], r14
0089EA06  E9 AA FC FF FF                  jmp 0x14089e6b5
0089EA0B  8B 47 54                        mov eax, dword ptr [rdi + 0x54]
0089EA0E  A8 01                           test al, 1
0089EA10  0F 84 6D FE FF FF               je 0x14089e883
0089EA16  E9 E5 FD FF FF                  jmp 0x14089e800
0089EA1B  8B 47 54                        mov eax, dword ptr [rdi + 0x54]
0089EA1E  A8 01                           test al, 1
0089EA20  0F 85 89 FD FF FF               jne 0x14089e7af
0089EA26  45 32 C0                        xor r8b, r8b
0089EA29  E9 84 FD FF FF                  jmp 0x14089e7b2
0089EA2E  4C 39 67 28                     cmp qword ptr [rdi + 0x28], r12
0089EA32  0F 85 7E FE FF FF               jne 0x14089e8b6
0089EA38  41 F7 C7 7F FF E1 FE            test r15d, 0xfee1ff7f
0089EA3F  0F 94 C1                        sete cl
0089EA42  0F B6 C3                        movzx eax, bl
0089EA45  C0 E8 06                        shr al, 6
0089EA48  F6 D0                           not al
0089EA4A  22 C8                           and cl, al
0089EA4C  F6 C1 01                        test cl, 1
0089EA4F  0F 84 61 FE FF FF               je 0x14089e8b6
0089EA55  80 CB 08                        or bl, 8
0089EA58  E9 5C FE FF FF                  jmp 0x14089e8b9
0089EA5D  A9 01 00 04 00                  test eax, 0x40001
0089EA62  74 0D                           je 0x14089ea71
0089EA64  41 F7 C7 7F FF ED FF            test r15d, 0xffedff7f
0089EA6B  0F 85 59 18 00 00               jne 0x1408a02ca
0089EA71  45 32 F6                        xor r14b, r14b
0089EA74  4C 89 A4 24 98 00 00 00         mov qword ptr [rsp + 0x98], r12
0089EA7C  48 8B 84 24 A8 00 00 00         mov rax, qword ptr [rsp + 0xa8]
0089EA84  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
0089EA8B  90                              nop
0089EA8C  B2 01                           mov dl, 1
0089EA8E  48 8D 0D 0B E8 6E 00            lea rcx, [rip + 0x6ee80b]
0089EA95  E8 26 31 97 FF                  call 0x140211bc0
0089EA9A  49 8D 4D 20                     lea rcx, [r13 + 0x20]
0089EA9E  E8 1D 7A 02 00                  call 0x1408c64c0
0089EAA3  80 CB 20                        or bl, 0x20
0089EAA6  45 84 F6                        test r14b, r14b
0089EAA9  0F 85 D5 19 00 00               jne 0x1408a0484
0089EAAF  48 8B 05 2A 80 72 00            mov rax, qword ptr [rip + 0x72802a]
0089EAB6  48 83 C0 4C                     add rax, 0x4c
0089EABA  44 0F B6 C3                     movzx r8d, bl
0089EABE  41 C0 E8 05                     shr r8b, 5
0089EAC2  41 80 E0 01                     and r8b, 1
0089EAC6  48 8D 4C 24 64                  lea rcx, [rsp + 0x64]
0089EACB  48 89 4C 24 48                  mov qword ptr [rsp + 0x48], rcx
0089EAD0  48 8D 8C 24 8C 00 00 00         lea rcx, [rsp + 0x8c]
0089EAD8  48 89 4C 24 40                  mov qword ptr [rsp + 0x40], rcx
0089EADD  C6 44 24 38 01                  mov byte ptr [rsp + 0x38], 1
0089EAE2  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0089EAE7  48 8D 84 24 98 00 00 00         lea rax, [rsp + 0x98]
0089EAEF  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0089EAF4  44 89 64 24 20                  mov dword ptr [rsp + 0x20], r12d
0089EAF9  45 8B CF                        mov r9d, r15d
0089EAFC  49 8D 55 20                     lea rdx, [r13 + 0x20]
0089EB00  4C 8B 74 24 70                  mov r14, qword ptr [rsp + 0x70]
0089EB05  49 8B 8E 10 01 00 00            mov rcx, qword ptr [r14 + 0x110]
0089EB0C  E8 AF 80 B0 FF                  call 0x1403a6bc0
0089EB11  32 C3                           xor al, bl
0089EB13  24 01                           and al, 1
0089EB15  32 D8                           xor bl, al
0089EB17  48 8B 94 24 98 00 00 00         mov rdx, qword ptr [rsp + 0x98]
0089EB1F  48 85 D2                        test rdx, rdx
0089EB22  0F 85 2B 01 00 00               jne 0x14089ec53
0089EB28  F6 C3 01                        test bl, 1
0089EB2B  74 1C                           je 0x14089eb49
0089EB2D  8B 84 24 8C 00 00 00            mov eax, dword ptr [rsp + 0x8c]
0089EB34  41 09 45 14                     or dword ptr [r13 + 0x14], eax
0089EB38  0F BA E8 19                     bts eax, 0x19
0089EB3C  F7 D0                           not eax
0089EB3E  41 21 45 10                     and dword ptr [r13 + 0x10], eax
0089EB42  C6 87 88 00 00 00 01            mov byte ptr [rdi + 0x88], 1
0089EB49  0F B6 CB                        movzx ecx, bl
0089EB4C  80 E1 01                        and cl, 1
0089EB4F  4D 8B 8E 10 01 00 00            mov r9, qword ptr [r14 + 0x110]
0089EB56  49 8D 45 0A                     lea rax, [r13 + 0xa]
0089EB5A  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
0089EB5F  4C 89 64 24 40                  mov qword ptr [rsp + 0x40], r12
0089EB64  C6 44 24 38 01                  mov byte ptr [rsp + 0x38], 1
0089EB69  88 4C 24 30                     mov byte ptr [rsp + 0x30], cl
0089EB6D  44 88 64 24 28                  mov byte ptr [rsp + 0x28], r12b
0089EB72  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
0089EB77  4C 8B 84 24 B0 00 00 00         mov r8, qword ptr [rsp + 0xb0]
0089EB7F  49 8B D6                        mov rdx, r14
0089EB82  48 8D 8C 24 28 01 00 00         lea rcx, [rsp + 0x128]
0089EB8A  E8 01 FC FC FF                  call 0x14086e790
0089EB8F  48 8D 0D 0A E7 6E 00            lea rcx, [rip + 0x6ee70a]
0089EB96  E8 75 0E 9C FF                  call 0x14025fa10
0089EB9B  48 8B 8C 24 A8 00 00 00         mov rcx, qword ptr [rsp + 0xa8]
0089EBA3  E8 48 04 9C FF                  call 0x14025eff0
0089EBA8  E9 B9 FC FF FF                  jmp 0x14089e866
0089EBAD  F7 41 50 00 00 40 00            test dword ptr [rcx + 0x50], 0x400000
0089EBB4  0F 84 37 FC FF FF               je 0x14089e7f1
0089EBBA  0F B6 D2                        movzx edx, dl
0089EBBD  66 44 39 26                     cmp word ptr [rsi], r12w
0089EBC1  B8 01 00 00 00                  mov eax, 1
0089EBC6  0F 44 D0                        cmove edx, eax
0089EBC9  89 94 24 88 00 00 00            mov dword ptr [rsp + 0x88], edx
0089EBD0  E9 1C FC FF FF                  jmp 0x14089e7f1
0089EBD5  F7 42 50 00 08 00 00            test dword ptr [rdx + 0x50], 0x800
0089EBDC  0F 85 EF FC FF FF               jne 0x14089e8d1
0089EBE2  48 8B B4 24 20 01 00 00         mov rsi, qword ptr [rsp + 0x120]
0089EBEA  48 89 74 24 78                  mov qword ptr [rsp + 0x78], rsi
0089EBEF  48 8B 42 10                     mov rax, qword ptr [rdx + 0x10]
0089EBF3  48 85 C0                        test rax, rax
0089EBF6  74 23                           je 0x14089ec1b
0089EBF8  4C 8B E8                        mov r13, rax
0089EBFB  48 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], rax
0089EC03  41 F7 46 34 00 01 00 00         test dword ptr [r14 + 0x34], 0x100
0089EC0B  0F 85 A2 18 00 00               jne 0x1408a04b3
0089EC11  B2 01                           mov dl, 1
0089EC13  49 8B CD                        mov rcx, r13
0089EC16  E8 05 3C 9D FF                  call 0x140272820
0089EC1B  8B 87 98 00 00 00               mov eax, dword ptr [rdi + 0x98]
0089EC21  A8 01                           test al, 1
0089EC23  0F 84 20 FD FF FF               je 0x14089e949
0089EC29  4D 85 ED                        test r13, r13
0089EC2C  74 09                           je 0x14089ec37
0089EC2E  49 8B 75 08                     mov rsi, qword ptr [r13 + 8]
0089EC32  48 89 74 24 78                  mov qword ptr [rsp + 0x78], rsi
0089EC37  80 CB 02                        or bl, 2
0089EC3A  E9 0A FD FF FF                  jmp 0x14089e949
0089EC3F  83 8F 98 00 00 00 02            or dword ptr [rdi + 0x98], 2
0089EC46  4D 8B F3                        mov r14, r11
0089EC49  4C 89 5C 24 70                  mov qword ptr [rsp + 0x70], r11
0089EC4E  E9 9B FA FF FF                  jmp 0x14089e6ee
0089EC53  49 8B CD                        mov rcx, r13
0089EC56  E8 25 8D 13 00                  call 0x1409d7980
0089EC5B  48 8B 8C 24 98 00 00 00         mov rcx, qword ptr [rsp + 0x98]
0089EC63  E8 18 71 BD FF                  call 0x140475d80
0089EC68  E9 BB FE FF FF                  jmp 0x14089eb28
0089EC6D  B8 24 00 00 C0                  mov eax, 0xc0000024
0089EC72  E9 18 1C 00 00                  jmp 0x1408a088f
0089EC77  4D 8B 46 70                     mov r8, qword ptr [r14 + 0x70]
0089EC7B  4C 89 84 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], r8
0089EC83  B8 0D 00 00 C0                  mov eax, 0xc000000d
0089EC88  85 C9                           test ecx, ecx
0089EC8A  41 0F 45 C4                     cmovne eax, r12d
0089EC8E  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
0089EC92  8B 77 54                        mov esi, dword ptr [rdi + 0x54]
0089EC95  83 E6 08                        and esi, 8
0089EC98  41 0F 95 C5                     setne r13b
0089EC9C  41 81 7E 30 04 01 00 00         cmp dword ptr [r14 + 0x30], 0x104
0089ECA4  0F 84 D7 11 00 00               je 0x14089fe81
0089ECAA  45 39 66 30                     cmp dword ptr [r14 + 0x30], r12d
0089ECAE  75 2A                           jne 0x14089ecda
0089ECB0  44 39 67 78                     cmp dword ptr [rdi + 0x78], r12d
0089ECB4  75 24                           jne 0x14089ecda
0089ECB6  4C 8B 84 24 B0 00 00 00         mov r8, qword ptr [rsp + 0xb0]
0089ECBE  48 8B 94 24 C0 00 00 00         mov rdx, qword ptr [rsp + 0xc0]
0089ECC6  49 8B CF                        mov rcx, r15
0089ECC9  E8 B2 28 00 00                  call 0x1408a1580
0089ECCE  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
0089ECD2  85 C0                           test eax, eax
0089ECD4  0F 88 EA 03 00 00               js 0x14089f0c4
0089ECDA  48 8B 84 24 C0 00 00 00         mov rax, qword ptr [rsp + 0xc0]
0089ECE2  48 85 C0                        test rax, rax
0089ECE5  74 07                           je 0x14089ecee
0089ECE7  48 89 87 A8 00 00 00            mov qword ptr [rdi + 0xa8], rax
0089ECEE  41 0F 10 46 30                  movups xmm0, xmmword ptr [r14 + 0x30]
0089ECF3  0F 11 84 24 10 01 00 00         movups xmmword ptr [rsp + 0x110], xmm0
0089ECFB  66 0F 7E 44 24 64               movd dword ptr [rsp + 0x64], xmm0
0089ED01  41 C7 87 9C 00 00 00 01 00 00 00  mov dword ptr [r15 + 0x9c], 1
0089ED0C  F6 C3 04                        test bl, 4
0089ED0F  74 17                           je 0x14089ed28
0089ED11  48 8B 84 24 A8 00 00 00         mov rax, qword ptr [rsp + 0xa8]
0089ED19  49 89 86 98 00 00 00            mov qword ptr [r14 + 0x98], rax
0089ED20  49 8B CE                        mov rcx, r14
0089ED23  E8 F8 8D 96 FF                  call 0x140207b20
0089ED28  41 8B 46 10                     mov eax, dword ptr [r14 + 0x10]
0089ED2C  83 E0 30                        and eax, 0x30
0089ED2F  3C 30                           cmp al, 0x30
0089ED31  0F 84 B7 18 00 00               je 0x1408a05ee
0089ED37  49 8B CE                        mov rcx, r14
0089ED3A  E8 31 F2 9A FF                  call 0x14024df70
0089ED3F  48 8B 8C 24 18 01 00 00         mov rcx, qword ptr [rsp + 0x118]
0089ED47  48 89 4F 18                     mov qword ptr [rdi + 0x18], rcx
0089ED4B  8B 44 24 64                     mov eax, dword ptr [rsp + 0x64]
0089ED4F  85 C0                           test eax, eax
0089ED51  0F 88 21 02 00 00               js 0x14089ef78
0089ED57  3D 04 01 00 00                  cmp eax, 0x104
0089ED5C  0F 84 CF 0D 00 00               je 0x14089fb31
0089ED62  49 8B CF                        mov rcx, r15
0089ED65  E8 B6 C3 9F FF                  call 0x14029b120
0089ED6A  48 8B F0                        mov rsi, rax
0089ED6D  48 39 44 24 78                  cmp qword ptr [rsp + 0x78], rax
0089ED72  0F 85 5D 19 00 00               jne 0x1408a06d5
0089ED78  F6 C3 40                        test bl, 0x40
0089ED7B  75 42                           jne 0x14089edbf
0089ED7D  48 8B 84 24 08 01 00 00         mov rax, qword ptr [rsp + 0x108]
0089ED85  4C 89 38                        mov qword ptr [rax], r15
0089ED88  C7 47 20 51 02 AA BE            mov dword ptr [rdi + 0x20], 0xbeaa0251
0089ED8F  49 8B CF                        mov rcx, r15
0089ED92  E8 89 0C 97 FF                  call 0x14020fa20
0089ED97  49 8B 47 40                     mov rax, qword ptr [r15 + 0x40]
0089ED9B  48 85 C0                        test rax, rax
0089ED9E  0F 85 1E 02 00 00               jne 0x14089efc2
0089EDA4  66 45 39 67 58                  cmp word ptr [r15 + 0x58], r12w
0089EDA9  0F 84 EB 01 00 00               je 0x14089ef9a
0089EDAF  8B 84 24 10 01 00 00            mov eax, dword ptr [rsp + 0x110]
0089EDB6  89 47 10                        mov dword ptr [rdi + 0x10], eax
0089EDB9  E9 D1 1A 00 00                  jmp 0x1408a088f
0089EDBE  CC                              int3
0089EDBF  44 38 A7 89 00 00 00            cmp byte ptr [rdi + 0x89], r12b
0089EDC6  0F 84 78 01 00 00               je 0x14089ef44
0089EDCC  44 38 A7 D0 00 00 00            cmp byte ptr [rdi + 0xd0], r12b
0089EDD3  0F 85 09 03 00 00               jne 0x14089f0e2
0089EDD9  32 DB                           xor bl, bl
0089EDDB  4C 8B 6E 08                     mov r13, qword ptr [rsi + 8]
0089EDDF  49 8B 45 50                     mov rax, qword ptr [r13 + 0x50]
0089EDE3  38 9F 8B 00 00 00               cmp byte ptr [rdi + 0x8b], bl
0089EDE9  0F 85 35 02 00 00               jne 0x14089f024
0089EDEF  4C 89 A4 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], r12
0089EDF7  48 85 C0                        test rax, rax
0089EDFA  0F 84 27 19 00 00               je 0x1408a0727
0089EE00  4C 8B 70 20                     mov r14, qword ptr [rax + 0x20]
0089EE04  4C 89 B4 24 08 01 00 00         mov qword ptr [rsp + 0x108], r14
0089EE0C  4D 85 F6                        test r14, r14
0089EE0F  74 46                           je 0x14089ee57
0089EE11  8B 05 09 5C 66 00               mov eax, dword ptr [rip + 0x665c09]
0089EE17  A8 10                           test al, 0x10
0089EE19  0F 85 CE 00 00 00               jne 0x14089eeed
0089EE1F  4D 8B EC                        mov r13, r12
0089EE22  4C 89 AC 24 58 01 00 00         mov qword ptr [rsp + 0x158], r13
0089EE2A  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
0089EE2F  4C 8D 8C 24 10 01 00 00         lea r9, [rsp + 0x110]
0089EE37  4C 8B 47 60                     mov r8, qword ptr [rdi + 0x60]
0089EE3B  B2 01                           mov dl, 1
0089EE3D  49 8B CF                        mov rcx, r15
0089EE40  49 8B C6                        mov rax, r14
0089EE43  E8 88 BC E1 FF                  call 0x1406baad0
0089EE48  0F B6 D8                        movzx ebx, al
0089EE4B  88 84 24 D0 00 00 00            mov byte ptr [rsp + 0xd0], al
0089EE52  4D 85 ED                        test r13, r13
0089EE55  75 14                           jne 0x14089ee6b
0089EE57  84 DB                           test bl, bl
0089EE59  74 1D                           je 0x14089ee78
0089EE5B  8B 84 24 10 01 00 00            mov eax, dword ptr [rsp + 0x110]
0089EE62  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
0089EE66  E9 AA 00 00 00                  jmp 0x14089ef15
0089EE6B  49 8B D6                        mov rdx, r14
0089EE6E  49 8B CD                        mov rcx, r13
0089EE71  E8 CA A5 31 00                  call 0x140bb9440
0089EE76  EB DF                           jmp 0x14089ee57
0089EE78  BA 28 00 00 00                  mov edx, 0x28
0089EE7D  8D 4A 18                        lea ecx, [rdx + 0x18]
0089EE80  41 B8 49 6F 20 20               mov r8d, 0x20206f49
0089EE86  E8 65 32 2E 00                  call 0x140b820f0
0089EE8B  48 8B D8                        mov rbx, rax
0089EE8E  48 89 84 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], rax
0089EE96  48 85 C0                        test rax, rax
0089EE99  74 72                           je 0x14089ef0d
0089EE9B  C6 44 24 30 01                  mov byte ptr [rsp + 0x30], 1
0089EEA0  48 8D 84 24 D4 00 00 00         lea rax, [rsp + 0xd4]
0089EEA8  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0089EEAD  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
0089EEB2  45 33 C9                        xor r9d, r9d
0089EEB5  41 8D 51 04                     lea edx, [r9 + 4]
0089EEB9  45 8D 41 28                     lea r8d, [r9 + 0x28]
0089EEBD  49 8B CF                        mov rcx, r15
0089EEC0  E8 0B 9B 00 00                  call 0x1408a89d0
0089EEC5  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
0089EEC9  85 C0                           test eax, eax
0089EECB  78 14                           js 0x14089eee1
0089EECD  44 8B 84 24 D4 00 00 00         mov r8d, dword ptr [rsp + 0xd4]
0089EED5  48 8B D3                        mov rdx, rbx
0089EED8  48 8B 4F 60                     mov rcx, qword ptr [rdi + 0x60]
0089EEDC  E8 5F 79 E2 FF                  call 0x1406c6840
0089EEE1  33 D2                           xor edx, edx
0089EEE3  48 8B CB                        mov rcx, rbx
0089EEE6  E8 85 39 2E 00                  call 0x140b82870
0089EEEB  EB 28                           jmp 0x14089ef15
0089EEED  49 8B CD                        mov rcx, r13
0089EEF0  E8 7B 98 C0 FF                  call 0x1404a8770
0089EEF5  85 C0                           test eax, eax
0089EEF7  0F 84 22 FF FF FF               je 0x14089ee1f
0089EEFD  49 8B CD                        mov rcx, r13
0089EF00  E8 B7 A8 31 00                  call 0x140bb97bc
0089EF05  4C 8B E8                        mov r13, rax
0089EF08  E9 15 FF FF FF                  jmp 0x14089ee22
0089EF0D  C7 44 24 64 9A 00 00 C0         mov dword ptr [rsp + 0x64], 0xc000009a
0089EF15  EB 2D                           jmp 0x14089ef44
0089EF17  8B D8                           mov ebx, eax
0089EF19  48 8B 8C 24 E0 00 00 00         mov rcx, qword ptr [rsp + 0xe0]
0089EF21  48 85 C9                        test rcx, rcx
0089EF24  74 07                           je 0x14089ef2d
0089EF26  33 D2                           xor edx, edx
0089EF28  E8 43 39 2E 00                  call 0x140b82870
0089EF2D  89 5C 24 64                     mov dword ptr [rsp + 0x64], ebx
0089EF31  45 33 E4                        xor r12d, r12d
0089EF34  4C 8B BC 24 A0 00 00 00         mov r15, qword ptr [rsp + 0xa0]
0089EF3C  48 8B BC 24 60 01 00 00         mov rdi, qword ptr [rsp + 0x160]
0089EF44  C7 47 20 51 02 AA BE            mov dword ptr [rdi + 0x20], 0xbeaa0251
0089EF4B  B8 01 00 00 00                  mov eax, 1
0089EF50  44 8B C8                        mov r9d, eax
0089EF53  44 8B C0                        mov r8d, eax
0089EF56  49 8B D7                        mov rdx, r15
0089EF59  33 C9                           xor ecx, ecx
0089EF5B  E8 60 51 FC FF                  call 0x1408640c0
0089EF60  49 8B CF                        mov rcx, r15
0089EF63  E8 E8 A3 A5 FF                  call 0x1402f9350
0089EF68  4C 89 67 08                     mov qword ptr [rdi + 8], r12
0089EF6C  8B 44 24 64                     mov eax, dword ptr [rsp + 0x64]
0089EF70  89 47 10                        mov dword ptr [rdi + 0x10], eax
0089EF73  E9 17 19 00 00                  jmp 0x1408a088f
0089EF78  41 F7 47 50 00 00 20 00         test dword ptr [r15 + 0x50], 0x200000
0089EF80  74 52                           je 0x14089efd4
0089EF82  49 8B CF                        mov rcx, r15
0089EF85  E8 C6 A3 A5 FF                  call 0x1402f9350
0089EF8A  4C 89 67 08                     mov qword ptr [rdi + 8], r12
0089EF8E  8B 44 24 64                     mov eax, dword ptr [rsp + 0x64]
0089EF92  89 47 10                        mov dword ptr [rdi + 0x10], eax
0089EF95  E9 F5 18 00 00                  jmp 0x1408a088f
0089EF9A  8B 4E 48                        mov ecx, dword ptr [rsi + 0x48]
0089EF9D  83 E9 03                        sub ecx, 3
0089EFA0  74 13                           je 0x14089efb5
0089EFA2  83 E9 05                        sub ecx, 5
0089EFA5  74 0E                           je 0x14089efb5
0089EFA7  83 E9 01                        sub ecx, 1
0089EFAA  74 09                           je 0x14089efb5
0089EFAC  83 F9 17                        cmp ecx, 0x17
0089EFAF  0F 85 FA FD FF FF               jne 0x14089edaf
0089EFB5  41 81 4F 50 00 00 40 00         or dword ptr [r15 + 0x50], 0x400000
0089EFBD  E9 ED FD FF FF                  jmp 0x14089edaf
0089EFC2  F7 40 50 00 00 40 00            test dword ptr [rax + 0x50], 0x400000
0089EFC9  0F 84 E0 FD FF FF               je 0x14089edaf
0089EFCF  E9 D0 FD FF FF                  jmp 0x14089eda4
0089EFD4  66 45 39 67 58                  cmp word ptr [r15 + 0x58], r12w
0089EFD9  74 10                           je 0x14089efeb
0089EFDB  33 D2                           xor edx, edx
0089EFDD  49 8B 4F 60                     mov rcx, qword ptr [r15 + 0x60]
0089EFE1  E8 8A 38 2E 00                  call 0x140b82870
0089EFE6  66 45 89 67 58                  mov word ptr [r15 + 0x58], r12w
0089EFEB  4D 89 67 08                     mov qword ptr [r15 + 8], r12
0089EFEF  49 8B CF                        mov rcx, r15
0089EFF2  E8 59 A3 A5 FF                  call 0x1402f9350
0089EFF7  45 33 C0                        xor r8d, r8d
0089EFFA  33 D2                           xor edx, edx
0089EFFC  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
0089F001  E8 6A 19 9D FF                  call 0x140270970
0089F006  48 8B 84 24 90 00 00 00         mov rax, qword ptr [rsp + 0x90]
0089F00E  48 85 C0                        test rax, rax
0089F011  0F 84 73 FF FF FF               je 0x14089ef8a
0089F017  48 8B C8                        mov rcx, rax
0089F01A  E8 55 04 BA FF                  call 0x14043f474
0089F01F  E9 66 FF FF FF                  jmp 0x14089ef8a
0089F024  48 85 C0                        test rax, rax
0089F027  74 49                           je 0x14089f072
0089F029  83 38 70                        cmp dword ptr [rax], 0x70
0089F02C  76 44                           jbe 0x14089f072
0089F02E  4C 8B 70 70                     mov r14, qword ptr [rax + 0x70]
0089F032  4D 85 F6                        test r14, r14
0089F035  74 3B                           je 0x14089f072
0089F037  8B 05 E3 59 66 00               mov eax, dword ptr [rip + 0x6659e3]
0089F03D  A8 10                           test al, 0x10
0089F03F  0F 85 EA 16 00 00               jne 0x1408a072f
0089F045  4D 8B EC                        mov r13, r12
0089F048  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
0089F04D  4C 8D 8C 24 10 01 00 00         lea r9, [rsp + 0x110]
0089F055  4C 8B 47 68                     mov r8, qword ptr [rdi + 0x68]
0089F059  B2 01                           mov dl, 1
0089F05B  49 8B CF                        mov rcx, r15
0089F05E  49 8B C6                        mov rax, r14
0089F061  E8 6A BA E1 FF                  call 0x1406baad0
0089F066  0F B6 D8                        movzx ebx, al
0089F069  4D 85 ED                        test r13, r13
0089F06C  0F 85 00 01 00 00               jne 0x14089f172
0089F072  84 DB                           test bl, bl
0089F074  0F 85 CA FE FF FF               jne 0x14089ef44
0089F07A  48 8B 47 68                     mov rax, qword ptr [rdi + 0x68]
0089F07E  C6 44 24 30 01                  mov byte ptr [rsp + 0x30], 1
0089F083  48 8D 8C 24 D4 00 00 00         lea rcx, [rsp + 0xd4]
0089F08B  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
0089F090  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0089F095  45 33 C9                        xor r9d, r9d
0089F098  41 8D 51 22                     lea edx, [r9 + 0x22]
0089F09C  45 8D 41 38                     lea r8d, [r9 + 0x38]
0089F0A0  49 8B CF                        mov rcx, r15
0089F0A3  E8 28 99 00 00                  call 0x1408a89d0
0089F0A8  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
0089F0AC  3D 0D 00 00 C0                  cmp eax, 0xc000000d
0089F0B1  0F 85 BC 16 00 00               jne 0x1408a0773
0089F0B7  48 8B D7                        mov rdx, rdi
0089F0BA  49 8B CF                        mov rcx, r15
0089F0BD  E8 A2 91 22 00                  call 0x140ac8264
0089F0C2  EB 4C                           jmp 0x14089f110
0089F0C4  49 8B D7                        mov rdx, r15
0089F0C7  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
0089F0CC  E8 CF 43 E6 FF                  call 0x1407034a0
0089F0D1  4D 89 66 38                     mov qword ptr [r14 + 0x38], r12
0089F0D5  8B 44 24 64                     mov eax, dword ptr [rsp + 0x64]
0089F0D9  41 89 46 30                     mov dword ptr [r14 + 0x30], eax
0089F0DD  E9 F8 FB FF FF                  jmp 0x14089ecda
0089F0E2  48 8B 4F 70                     mov rcx, qword ptr [rdi + 0x70]
0089F0E6  48 8D 87 CC 00 00 00            lea rax, [rdi + 0xcc]
0089F0ED  44 8B 00                        mov r8d, dword ptr [rax]
0089F0F0  8B 97 C8 00 00 00               mov edx, dword ptr [rdi + 0xc8]
0089F0F6  C6 44 24 30 01                  mov byte ptr [rsp + 0x30], 1
0089F0FB  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0089F100  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0089F105  45 33 C9                        xor r9d, r9d
0089F108  49 8B CF                        mov rcx, r15
0089F10B  E8 C0 98 00 00                  call 0x1408a89d0
0089F110  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
0089F114  E9 2B FE FF FF                  jmp 0x14089ef44
0089F119  84 D2                           test dl, dl
0089F11B  0F 85 E8 F6 FF FF               jne 0x14089e809
0089F121  E9 5D F7 FF FF                  jmp 0x14089e883
0089F126  49 8B CE                        mov rcx, r14
0089F129  E8 42 EE 9A FF                  call 0x14024df70
0089F12E  45 33 C0                        xor r8d, r8d
0089F131  33 D2                           xor edx, edx
0089F133  49 8B CF                        mov rcx, r15
0089F136  E8 35 18 9D FF                  call 0x140270970
0089F13B  48 8B 84 24 90 00 00 00         mov rax, qword ptr [rsp + 0x90]
0089F143  48 85 C0                        test rax, rax
0089F146  74 08                           je 0x14089f150
0089F148  48 8B C8                        mov rcx, rax
0089F14B  E8 24 03 BA FF                  call 0x14043f474
0089F150  48 8B 8C 24 A0 00 00 00         mov rcx, qword ptr [rsp + 0xa0]
0089F158  48 85 C9                        test rcx, rcx
0089F15B  74 09                           je 0x14089f166
0089F15D  4C 89 61 08                     mov qword ptr [rcx + 8], r12
0089F161  E8 EA A1 A5 FF                  call 0x1402f9350
0089F166  8B 44 24 64                     mov eax, dword ptr [rsp + 0x64]
0089F16A  89 47 10                        mov dword ptr [rdi + 0x10], eax
0089F16D  E9 1D 17 00 00                  jmp 0x1408a088f
0089F172  49 8B D6                        mov rdx, r14
0089F175  49 8B CD                        mov rcx, r13
0089F178  E8 C3 A2 31 00                  call 0x140bb9440
0089F17D  E9 F0 FE FF FF                  jmp 0x14089f072
0089F182  F6 C3 02                        test bl, 2
0089F185  0F 85 27 07 00 00               jne 0x14089f8b2
0089F18B  8B 87 98 00 00 00               mov eax, dword ptr [rdi + 0x98]
0089F191  A8 10                           test al, 0x10
0089F193  0F 85 22 08 00 00               jne 0x14089f9bb
0089F199  F7 46 34 00 01 00 00            test dword ptr [rsi + 0x34], 0x100
0089F1A0  0F 85 45 06 00 00               jne 0x14089f7eb
0089F1A6  44 39 25 1F B8 56 00            cmp dword ptr [rip + 0x56b81f], r12d
0089F1AD  74 0E                           je 0x14089f1bd
0089F1AF  41 F7 46 34 00 00 10 00         test dword ptr [r14 + 0x34], 0x100000
0089F1B7  0F 85 2E 06 00 00               jne 0x14089f7eb
0089F1BD  45 33 C0                        xor r8d, r8d
0089F1C0  0F B6 56 4C                     movzx edx, byte ptr [rsi + 0x4c]
0089F1C4  48 8B CE                        mov rcx, rsi
0089F1C7  E8 54 85 96 FF                  call 0x140207720
0089F1CC  4C 8B F0                        mov r14, rax
0089F1CF  48 85 C0                        test rax, rax
0089F1D2  0F 84 A7 07 00 00               je 0x14089f97f
0089F1D8  48 8B 84 24 A8 00 00 00         mov rax, qword ptr [rsp + 0xa8]
0089F1E0  49 89 86 98 00 00 00            mov qword ptr [r14 + 0x98], rax
0089F1E7  0F B6 54 24 68                  movzx edx, byte ptr [rsp + 0x68]
0089F1EC  41 88 56 40                     mov byte ptr [r14 + 0x40], dl
0089F1F0  41 C7 46 10 84 08 00 00         mov dword ptr [r14 + 0x10], 0x884
0089F1F8  48 8B 84 24 F0 01 00 00         mov rax, qword ptr [rsp + 0x1f0]
0089F200  48 89 84 24 38 01 00 00         mov qword ptr [rsp + 0x138], rax
0089F208  48 8B 84 24 D8 00 00 00         mov rax, qword ptr [rsp + 0xd8]
0089F210  48 89 84 24 40 01 00 00         mov qword ptr [rsp + 0x140], rax
0089F218  44 89 BC 24 48 01 00 00         mov dword ptr [rsp + 0x148], r15d
0089F220  8B 47 40                        mov eax, dword ptr [rdi + 0x40]
0089F223  89 84 24 4C 01 00 00            mov dword ptr [rsp + 0x14c], eax
0089F22A  4D 8B AE B8 00 00 00            mov r13, qword ptr [r14 + 0xb8]
0089F231  49 83 ED 48                     sub r13, 0x48
0089F235  4C 89 AC 24 50 01 00 00         mov qword ptr [rsp + 0x150], r13
0089F23D  45 88 65 03                     mov byte ptr [r13 + 3], r12b
0089F241  8B 47 78                        mov eax, dword ptr [rdi + 0x78]
0089F244  85 C0                           test eax, eax
0089F246  0F 85 67 02 00 00               jne 0x14089f4b3
0089F24C  45 88 65 00                     mov byte ptr [r13], r12b
0089F250  8B 47 50                        mov eax, dword ptr [rdi + 0x50]
0089F253  41 89 45 20                     mov dword ptr [r13 + 0x20], eax
0089F257  0F B6 47 54                     movzx eax, byte ptr [rdi + 0x54]
0089F25B  41 88 45 02                     mov byte ptr [r13 + 2], al
0089F25F  F6 84 24 D0 01 00 00 40         test byte ptr [rsp + 0x1d0], 0x40
0089F267  0F 84 D0 07 00 00               je 0x14089fa3d
0089F26D  48 8B 47 38                     mov rax, qword ptr [rdi + 0x38]
0089F271  49 89 46 58                     mov qword ptr [r14 + 0x58], rax
0089F275  48 8B 47 48                     mov rax, qword ptr [rdi + 0x48]
0089F279  49 89 46 18                     mov qword ptr [r14 + 0x18], rax
0089F27D  8B 4F 58                        mov ecx, dword ptr [rdi + 0x58]
0089F280  C1 E1 18                        shl ecx, 0x18
0089F283  8B 47 40                        mov eax, dword ptr [rdi + 0x40]
0089F286  25 FF FF FF 00                  and eax, 0xffffff
0089F28B  0B C8                           or ecx, eax
0089F28D  41 89 4D 10                     mov dword ptr [r13 + 0x10], ecx
0089F291  0F B7 47 44                     movzx eax, word ptr [rdi + 0x44]
0089F295  66 41 89 45 18                  mov word ptr [r13 + 0x18], ax
0089F29A  0F B7 47 46                     movzx eax, word ptr [rdi + 0x46]
0089F29E  66 41 89 45 1A                  mov word ptr [r13 + 0x1a], ax
0089F2A3  48 8D 84 24 38 01 00 00         lea rax, [rsp + 0x138]
0089F2AB  49 89 45 08                     mov qword ptr [r13 + 8], rax
0089F2AF  48 8B 87 A8 00 00 00            mov rax, qword ptr [rdi + 0xa8]
0089F2B6  49 89 46 70                     mov qword ptr [r14 + 0x70], rax
0089F2BA  48 8D 84 24 10 01 00 00         lea rax, [rsp + 0x110]
0089F2C2  49 89 46 48                     mov qword ptr [r14 + 0x48], rax
0089F2C6  4D 89 66 08                     mov qword ptr [r14 + 8], r12
0089F2CA  45 88 66 41                     mov byte ptr [r14 + 0x41], r12b
0089F2CE  45 88 66 44                     mov byte ptr [r14 + 0x44], r12b
0089F2D2  4D 89 66 50                     mov qword ptr [r14 + 0x50], r12
0089F2D6  4D 89 66 68                     mov qword ptr [r14 + 0x68], r12
0089F2DA  4D 89 A6 A0 00 00 00            mov qword ptr [r14 + 0xa0], r12
0089F2E1  44 38 A7 89 00 00 00            cmp byte ptr [rdi + 0x89], r12b
0089F2E8  0F 85 22 03 00 00               jne 0x14089f610
0089F2EE  44 89 7C 24 40                  mov dword ptr [rsp + 0x40], r15d
0089F2F3  44 88 64 24 38                  mov byte ptr [rsp + 0x38], r12b
0089F2F8  48 8B 84 24 F0 00 00 00         mov rax, qword ptr [rsp + 0xf0]
0089F300  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0089F305  48 89 7C 24 28                  mov qword ptr [rsp + 0x28], rdi
0089F30A  88 54 24 20                     mov byte ptr [rsp + 0x20], dl
0089F30E  44 8B 8C 24 D0 01 00 00         mov r9d, dword ptr [rsp + 0x1d0]
0089F316  4C 8B 7C 24 70                  mov r15, qword ptr [rsp + 0x70]
0089F31B  4D 8B C7                        mov r8, r15
0089F31E  48 8B D6                        mov rdx, rsi
0089F321  48 8D 8C 24 A0 00 00 00         lea rcx, [rsp + 0xa0]
0089F329  E8 F2 A3 FF FF                  call 0x140899720
0089F32E  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
0089F332  85 C0                           test eax, eax
0089F334  0F 88 EC FD FF FF               js 0x14089f126
0089F33A  4C 8B BC 24 A0 00 00 00         mov r15, qword ptr [rsp + 0xa0]
0089F342  F6 C3 08                        test bl, 8
0089F345  74 08                           je 0x14089f34f
0089F347  41 81 4F 50 00 08 00 00         or dword ptr [r15 + 0x50], 0x800
0089F34F  48 8B 87 D8 00 00 00            mov rax, qword ptr [rdi + 0xd8]
0089F356  A8 01                           test al, 1
0089F358  0F 85 43 01 00 00               jne 0x14089f4a1
0089F35E  A8 02                           test al, 2
0089F360  0F 85 63 06 00 00               jne 0x14089f9c9
0089F366  4D 89 BE C0 00 00 00            mov qword ptr [r14 + 0xc0], r15
0089F36D  4D 89 7D 30                     mov qword ptr [r13 + 0x30], r15
0089F371  48 8B 84 24 80 00 00 00         mov rax, qword ptr [rsp + 0x80]
0089F379  0F B7 00                        movzx eax, word ptr [rax]
0089F37C  66 85 C0                        test ax, ax
0089F37F  74 49                           je 0x14089f3ca
0089F381  66 83 F8 38                     cmp ax, 0x38
0089F385  0F 82 56 04 00 00               jb 0x14089f7e1
0089F38B  66 83 F8 78                     cmp ax, 0x78
0089F38F  72 0F                           jb 0x14089f3a0
0089F391  B9 F8 00 00 00                  mov ecx, 0xf8
0089F396  66 3B C1                        cmp ax, cx
0089F399  73 0A                           jae 0x14089f3a5
0089F39B  0F B7 C1                        movzx eax, cx
0089F39E  EB 05                           jmp 0x14089f3a5
0089F3A0  B8 78 00 00 00                  mov eax, 0x78
0089F3A5  66 41 89 47 5A                  mov word ptr [r15 + 0x5a], ax
0089F3AA  0F B7 D0                        movzx edx, ax
0089F3AD  B9 00 01 00 00                  mov ecx, 0x100
0089F3B2  41 B8 49 6F 4E 6D               mov r8d, 0x6d4e6f49
0089F3B8  E8 33 2D 2E 00                  call 0x140b820f0
0089F3BD  49 89 47 60                     mov qword ptr [r15 + 0x60], rax
0089F3C1  48 85 C0                        test rax, rax
0089F3C4  0F 84 DF 0D 00 00               je 0x1408a01a9
0089F3CA  48 8B 94 24 80 00 00 00         mov rdx, qword ptr [rsp + 0x80]
0089F3D2  49 8D 4F 58                     lea rcx, [r15 + 0x58]
0089F3D6  E8 55 FB B5 FF                  call 0x1403fef30
0089F3DB  44 38 A7 89 00 00 00            cmp byte ptr [rdi + 0x89], r12b
0089F3E2  0F 85 EF 00 00 00               jne 0x14089f4d7
0089F3E8  48 8B 74 24 78                  mov rsi, qword ptr [rsp + 0x78]
0089F3ED  44 39 67 78                     cmp dword ptr [rdi + 0x78], r12d
0089F3F1  75 2B                           jne 0x14089f41e
0089F3F3  4D 8B C4                        mov r8, r12
0089F3F6  41 8B 4E 10                     mov ecx, dword ptr [r14 + 0x10]
0089F3FA  81 E1 80 00 00 00               and ecx, 0x80
0089F400  74 04                           je 0x14089f406
0089F402  4D 8B 46 70                     mov r8, qword ptr [r14 + 0x70]
0089F406  B8 0D 00 00 C0                  mov eax, 0xc000000d
0089F40B  85 C9                           test ecx, ecx
0089F40D  41 0F 45 C4                     cmovne eax, r12d
0089F411  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
0089F415  4D 85 C0                        test r8, r8
0089F418  0F 85 DB 04 00 00               jne 0x14089f8f9
0089F41E  49 8D 8F 98 00 00 00            lea rcx, [r15 + 0x98]
0089F425  45 33 C0                        xor r8d, r8d
0089F428  33 D2                           xor edx, edx
0089F42A  E8 E1 E8 B6 FF                  call 0x14040dd10
0089F42F  4C 89 7F 08                     mov qword ptr [rdi + 8], r15
0089F433  F6 C3 04                        test bl, 4
0089F436  0F 84 94 00 00 00               je 0x14089f4d0
0089F43C  49 8B CE                        mov rcx, r14
0089F43F  E8 7C 81 96 FF                  call 0x1402075c0
0089F444  45 38 66 47                     cmp byte ptr [r14 + 0x47], r12b
0089F448  7C 10                           jl 0x14089f45a
0089F44A  49 8B 86 C8 00 00 00            mov rax, qword ptr [r14 + 0xc8]
0089F451  48 85 C0                        test rax, rax
0089F454  0F 85 8F 04 00 00               jne 0x14089f8e9
0089F45A  32 C0                           xor al, al
0089F45C  84 C0                           test al, al
0089F45E  0F 85 1F 13 00 00               jne 0x1408a0783
0089F464  49 8B D6                        mov rdx, r14
0089F467  48 8B CE                        mov rcx, rsi
0089F46A  E8 41 C0 9F FF                  call 0x14029b4b0
0089F46F  44 8B E8                        mov r13d, eax
0089F472  44 89 6C 24 64                  mov dword ptr [rsp + 0x64], r13d
0089F477  41 81 FD 03 01 00 00            cmp r13d, 0x103
0089F47E  0F 84 C4 05 00 00               je 0x14089fa48
0089F484  41 8B 4E 10                     mov ecx, dword ptr [r14 + 0x10]
0089F488  81 E1 80 00 00 00               and ecx, 0x80
0089F48E  0F 85 E3 F7 FF FF               jne 0x14089ec77
0089F494  4C 8B 84 24 C0 00 00 00         mov r8, qword ptr [rsp + 0xc0]
0089F49C  E9 E2 F7 FF FF                  jmp 0x14089ec83
0089F4A1  BA 20 00 00 00                  mov edx, 0x20
0089F4A6  49 8B CF                        mov rcx, r15
0089F4A9  E8 62 E2 B9 FF                  call 0x14043d710
0089F4AE  E9 B3 FE FF FF                  jmp 0x14089f366
0089F4B3  83 F8 01                        cmp eax, 1
0089F4B6  0F 85 50 12 00 00               jne 0x1408a070c
0089F4BC  41 88 45 00                     mov byte ptr [r13], al
0089F4C0  48 8B 87 80 00 00 00            mov rax, qword ptr [rdi + 0x80]
0089F4C7  49 89 45 20                     mov qword ptr [r13 + 0x20], rax
0089F4CB  E9 9D FD FF FF                  jmp 0x14089f26d
0089F4D0  44 8B 6C 24 64                  mov r13d, dword ptr [rsp + 0x64]
0089F4D5  EB A0                           jmp 0x14089f477
0089F4D7  44 88 64 24 60                  mov byte ptr [rsp + 0x60], r12b
0089F4DC  48 8D 44 24 60                  lea rax, [rsp + 0x60]
0089F4E1  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0089F4E6  4D 8B CD                        mov r9, r13
0089F4E9  4D 8B C6                        mov r8, r14
0089F4EC  48 8B 54 24 78                  mov rdx, qword ptr [rsp + 0x78]
0089F4F1  48 8B CF                        mov rcx, rdi
0089F4F4  E8 77 8E 13 00                  call 0x1409d8370
0089F4F9  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
0089F4FD  85 C0                           test eax, eax
0089F4FF  0F 88 CE 04 00 00               js 0x14089f9d3
0089F505  44 38 64 24 60                  cmp byte ptr [rsp + 0x60], r12b
0089F50A  0F 85 C3 04 00 00               jne 0x14089f9d3
0089F510  E8 DB EC A5 FF                  call 0x1402fe1f0
0089F515  45 0F B7 47 58                  movzx r8d, word ptr [r15 + 0x58]
0089F51A  48 8B 84 24 80 00 00 00         mov rax, qword ptr [rsp + 0x80]
0089F522  48 8B F0                        mov rsi, rax
0089F525  66 44 3B 00                     cmp r8w, word ptr [rax]
0089F529  0F 84 72 04 00 00               je 0x14089f9a1
0089F52F  49 8B 4F 60                     mov rcx, qword ptr [r15 + 0x60]
0089F533  48 85 C9                        test rcx, rcx
0089F536  74 12                           je 0x14089f54a
0089F538  33 D2                           xor edx, edx
0089F53A  E8 31 33 2E 00                  call 0x140b82870
0089F53F  49 8D 4F 58                     lea rcx, [r15 + 0x58]
0089F543  33 D2                           xor edx, edx
0089F545  E8 36 B2 B8 FF                  call 0x14042a780
0089F54A  0F B7 06                        movzx eax, word ptr [rsi]
0089F54D  66 85 C0                        test ax, ax
0089F550  74 4A                           je 0x14089f59c
0089F552  66 83 F8 38                     cmp ax, 0x38
0089F556  0F 82 B1 12 00 00               jb 0x1408a080d
0089F55C  66 83 F8 78                     cmp ax, 0x78
0089F560  0F 83 15 10 00 00               jae 0x1408a057b
0089F566  B8 78 00 00 00                  mov eax, 0x78
0089F56B  66 41 89 47 5A                  mov word ptr [r15 + 0x5a], ax
0089F570  0F B7 D0                        movzx edx, ax
0089F573  B9 00 01 00 00                  mov ecx, 0x100
0089F578  41 B8 49 6F 4E 6D               mov r8d, 0x6d4e6f49
0089F57E  E8 6D 2B 2E 00                  call 0x140b820f0
0089F583  49 89 47 60                     mov qword ptr [r15 + 0x60], rax
0089F587  48 85 C0                        test rax, rax
0089F58A  0F 84 91 10 00 00               je 0x1408a0621
0089F590  49 8D 4F 58                     lea rcx, [r15 + 0x58]
0089F594  48 8B D6                        mov rdx, rsi
0089F597  E8 94 F9 B5 FF                  call 0x1403fef30
0089F59C  8B 84 24 B8 00 00 00            mov eax, dword ptr [rsp + 0xb8]
0089F5A3  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
0089F5A7  C6 44 24 38 01                  mov byte ptr [rsp + 0x38], 1
0089F5AC  48 8B 84 24 F0 00 00 00         mov rax, qword ptr [rsp + 0xf0]
0089F5B4  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0089F5B9  48 89 7C 24 28                  mov qword ptr [rsp + 0x28], rdi
0089F5BE  0F B6 44 24 68                  movzx eax, byte ptr [rsp + 0x68]
0089F5C3  88 44 24 20                     mov byte ptr [rsp + 0x20], al
0089F5C7  44 8B 8C 24 D0 01 00 00         mov r9d, dword ptr [rsp + 0x1d0]
0089F5CF  4C 8B 7C 24 70                  mov r15, qword ptr [rsp + 0x70]
0089F5D4  4D 8B C7                        mov r8, r15
0089F5D7  48 8B 74 24 78                  mov rsi, qword ptr [rsp + 0x78]
0089F5DC  48 8B D6                        mov rdx, rsi
0089F5DF  48 8D 8C 24 A0 00 00 00         lea rcx, [rsp + 0xa0]
0089F5E7  E8 34 A1 FF FF                  call 0x140899720
0089F5EC  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
0089F5F0  85 C0                           test eax, eax
0089F5F2  0F 88 67 10 00 00               js 0x1408a065f
0089F5F8  4C 8B BC 24 A0 00 00 00         mov r15, qword ptr [rsp + 0xa0]
0089F600  4D 89 7D 30                     mov qword ptr [r13 + 0x30], r15
0089F604  4D 89 BE C0 00 00 00            mov qword ptr [r14 + 0xc0], r15
0089F60B  E9 DD FD FF FF                  jmp 0x14089f3ed
0089F610  48 8B B7 90 00 00 00            mov rsi, qword ptr [rdi + 0x90]
0089F617  33 D2                           xor edx, edx
0089F619  41 B8 10 01 00 00               mov r8d, 0x110
0089F61F  48 8B CE                        mov rcx, rsi
0089F622  E8 19 76 E2 FF                  call 0x1406c6c40
0089F627  4C 8D 7E 30                     lea r15, [rsi + 0x30]
0089F62B  4C 89 BC 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], r15
0089F633  48 8B 05 A6 74 72 00            mov rax, qword ptr [rip + 0x7274a6]
0089F63A  0F B6 48 28                     movzx ecx, byte ptr [rax + 0x28]
0089F63E  48 8B C6                        mov rax, rsi
0089F641  48 C1 E8 08                     shr rax, 8
0089F645  32 C1                           xor al, cl
0089F647  32 05 FF 77 72 00               xor al, byte ptr [rip + 0x7277ff]
0089F64D  88 46 18                        mov byte ptr [rsi + 0x18], al
0089F650  48 C7 06 01 00 00 00            mov qword ptr [rsi], 1
0089F657  F6 84 24 D0 01 00 00 40         test byte ptr [rsp + 0x1d0], 0x40
0089F65F  0F 84 4F 04 00 00               je 0x14089fab4
0089F665  66 41 C7 07 05 00               mov word ptr [r15], 5
0089F66B  66 C7 46 32 D8 00               mov word ptr [rsi + 0x32], 0xd8
0089F671  48 8B 47 28                     mov rax, qword ptr [rdi + 0x28]
0089F675  48 89 46 70                     mov qword ptr [rsi + 0x70], rax
0089F679  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
0089F67E  48 89 46 38                     mov qword ptr [rsi + 0x38], rax
0089F682  4D 8B CF                        mov r9, r15
0089F685  44 8B 84 24 B8 00 00 00         mov r8d, dword ptr [rsp + 0xb8]
0089F68D  48 8B D7                        mov rdx, rdi
0089F690  48 8B 74 24 78                  mov rsi, qword ptr [rsp + 0x78]
0089F695  48 8B CE                        mov rcx, rsi
0089F698  E8 DF 0B 18 00                  call 0x140a2027c
0089F69D  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
0089F6A1  85 C0                           test eax, eax
0089F6A3  0F 88 8E 11 00 00               js 0x1408a0837
0089F6A9  8B 87 98 00 00 00               mov eax, dword ptr [rdi + 0x98]
0089F6AF  24 24                           and al, 0x24
0089F6B1  3C 20                           cmp al, 0x20
0089F6B3  75 36                           jne 0x14089f6eb
0089F6B5  44 38 64 24 68                  cmp byte ptr [rsp + 0x68], r12b
0089F6BA  74 2F                           je 0x14089f6eb
0089F6BC  F7 46 30 00 00 04 00            test dword ptr [rsi + 0x30], 0x40000
0089F6C3  0F 84 DC 0B 00 00               je 0x1408a02a5
0089F6C9  4D 8B CF                        mov r9, r15
0089F6CC  44 8B 84 24 B8 00 00 00         mov r8d, dword ptr [rsp + 0xb8]
0089F6D4  48 8B D7                        mov rdx, rdi
0089F6D7  48 8B CE                        mov rcx, rsi
0089F6DA  E8 41 8E FF FF                  call 0x140898520
0089F6DF  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
0089F6E3  85 C0                           test eax, eax
0089F6E5  0F 88 41 06 00 00               js 0x14089fd2c
0089F6EB  48 8B 84 24 F0 00 00 00         mov rax, qword ptr [rsp + 0xf0]
0089F6F3  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
0089F6F7  E8 34 44 BA FF                  call 0x140443b30
0089F6FC  84 C0                           test al, al
0089F6FE  74 22                           je 0x14089f722
0089F700  49 8B 4F 40                     mov rcx, qword ptr [r15 + 0x40]
0089F704  48 85 C9                        test rcx, rcx
0089F707  0F 84 35 FC FF FF               je 0x14089f342
0089F70D  E8 7E 8D B9 FF                  call 0x140438490
0089F712  48 8B C8                        mov rcx, rax
0089F715  E8 16 44 BA FF                  call 0x140443b30
0089F71A  84 C0                           test al, al
0089F71C  0F 85 20 FC FF FF               jne 0x14089f342
0089F722  49 8B F4                        mov rsi, r12
0089F725  4C 89 A4 24 00 01 00 00         mov qword ptr [rsp + 0x100], r12
0089F72D  49 8B 57 40                     mov rdx, qword ptr [r15 + 0x40]
0089F731  48 85 D2                        test rdx, rdx
0089F734  0F 85 1B 0E 00 00               jne 0x1408a0555
0089F73A  48 8B 84 24 F0 00 00 00         mov rax, qword ptr [rsp + 0xf0]
0089F742  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0089F746  48 89 84 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], rax
0089F74E  48 8B C8                        mov rcx, rax
0089F751  E8 DA 43 BA FF                  call 0x140443b30
0089F756  84 C0                           test al, al
0089F758  0F 85 E4 FB FF FF               jne 0x14089f342
0089F75E  48 8B 8C 24 C8 00 00 00         mov rcx, qword ptr [rsp + 0xc8]
0089F766  E8 B5 7E BC FF                  call 0x140467620
0089F76B  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
0089F76F  85 C0                           test eax, eax
0089F771  0F 88 85 03 00 00               js 0x14089fafc
0089F777  4C 89 64 24 28                  mov qword ptr [rsp + 0x28], r12
0089F77C  48 8D 84 24 00 01 00 00         lea rax, [rsp + 0x100]
0089F784  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0089F789  41 B1 01                        mov r9b, 1
0089F78C  BA 07 00 00 00                  mov edx, 7
0089F791  44 8D 42 09                     lea r8d, [rdx + 9]
0089F795  49 8B CF                        mov rcx, r15
0089F798  E8 E3 F6 B8 FF                  call 0x14042ee80
0089F79D  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
0089F7A1  85 C0                           test eax, eax
0089F7A3  0F 88 1A 03 00 00               js 0x14089fac3
0089F7A9  48 8B B4 24 00 01 00 00         mov rsi, qword ptr [rsp + 0x100]
0089F7B1  85 C0                           test eax, eax
0089F7B3  0F 88 43 03 00 00               js 0x14089fafc
0089F7B9  C7 06 10 00 00 00               mov dword ptr [rsi], 0x10
0089F7BF  48 8B 84 24 C8 00 00 00         mov rax, qword ptr [rsp + 0xc8]
0089F7C7  48 89 46 08                     mov qword ptr [rsi + 8], rax
0089F7CB  83 4E 04 01                     or dword ptr [rsi + 4], 1
0089F7CF  BA 49 6F 53 70                  mov edx, 0x70536f49
0089F7D4  48 8B C8                        mov rcx, rax
0089F7D7  E8 34 0F 97 FF                  call 0x140210710
0089F7DC  E9 61 FB FF FF                  jmp 0x14089f342
0089F7E1  B8 38 00 00 00                  mov eax, 0x38
0089F7E6  E9 BA FB FF FF                  jmp 0x14089f3a5
0089F7EB  44 38 64 24 68                  cmp byte ptr [rsp + 0x68], r12b
0089F7F0  75 0B                           jne 0x14089f7fd
0089F7F2  8B 47 54                        mov eax, dword ptr [rdi + 0x54]
0089F7F5  A8 01                           test al, 1
0089F7F7  0F 84 C0 F9 FF FF               je 0x14089f1bd
0089F7FD  4C 39 67 28                     cmp qword ptr [rdi + 0x28], r12
0089F801  75 12                           jne 0x14089f815
0089F803  48 8B 84 24 80 00 00 00         mov rax, qword ptr [rsp + 0x80]
0089F80B  66 44 39 20                     cmp word ptr [rax], r12w
0089F80F  0F 84 A8 F9 FF FF               je 0x14089f1bd
0089F815  44 38 A4 24 88 00 00 00         cmp byte ptr [rsp + 0x88], r12b
0089F81D  0F 85 9A F9 FF FF               jne 0x14089f1bd
0089F823  4C 89 A4 24 98 00 00 00         mov qword ptr [rsp + 0x98], r12
0089F82B  C6 44 24 50 01                  mov byte ptr [rsp + 0x50], 1
0089F830  48 8B 84 24 A8 00 00 00         mov rax, qword ptr [rsp + 0xa8]
0089F838  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
0089F83D  48 8D 84 24 28 01 00 00         lea rax, [rsp + 0x128]
0089F845  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
0089F84A  48 8B 84 24 B0 00 00 00         mov rax, qword ptr [rsp + 0xb0]
0089F852  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0089F857  48 8D 84 24 8C 00 00 00         lea rax, [rsp + 0x8c]
0089F85F  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0089F864  4C 89 64 24 28                  mov qword ptr [rsp + 0x28], r12
0089F869  8B 47 58                        mov eax, dword ptr [rdi + 0x58]
0089F86C  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
0089F870  45 8B CF                        mov r9d, r15d
0089F873  4C 8B 84 24 D8 00 00 00         mov r8, qword ptr [rsp + 0xd8]
0089F87B  48 8B D6                        mov rdx, rsi
0089F87E  49 8B CE                        mov rcx, r14
0089F881  E8 1A 65 B0 FF                  call 0x1403a5da0
0089F886  84 C0                           test al, al
0089F888  0F 85 2F F9 FF FF               jne 0x14089f1bd
0089F88E  45 33 C0                        xor r8d, r8d
0089F891  33 D2                           xor edx, edx
0089F893  49 8B CE                        mov rcx, r14
0089F896  E8 D5 10 9D FF                  call 0x140270970
0089F89B  4D 85 ED                        test r13, r13
0089F89E  74 08                           je 0x14089f8a8
0089F8A0  49 8B CD                        mov rcx, r13
0089F8A3  E8 CC FB B9 FF                  call 0x14043f474
0089F8A8  B8 22 00 00 C0                  mov eax, 0xc0000022
0089F8AD  E9 DD 0F 00 00                  jmp 0x1408a088f
0089F8B2  44 0F B6 C3                     movzx r8d, bl
0089F8B6  41 C0 E8 03                     shr r8b, 3
0089F8BA  41 80 E0 01                     and r8b, 1
0089F8BE  4C 8B 8C 24 80 00 00 00         mov r9, qword ptr [rsp + 0x80]
0089F8C6  48 8B D7                        mov rdx, rdi
0089F8C9  48 8D 4C 24 78                  lea rcx, [rsp + 0x78]
0089F8CE  E8 1D BD 14 00                  call 0x1409eb5f0
0089F8D3  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
0089F8D7  85 C0                           test eax, eax
0089F8D9  0F 88 FA 01 00 00               js 0x14089fad9
0089F8DF  48 8B 74 24 78                  mov rsi, qword ptr [rsp + 0x78]
0089F8E4  E9 A2 F8 FF FF                  jmp 0x14089f18b
0089F8E9  F6 00 02                        test byte ptr [rax], 2
0089F8EC  0F 84 68 FB FF FF               je 0x14089f45a
0089F8F2  B0 01                           mov al, 1
0089F8F4  E9 63 FB FF FF                  jmp 0x14089f45c
0089F8F9  48 8D 94 24 E0 00 00 00         lea rdx, [rsp + 0xe0]
0089F901  49 8B C8                        mov rcx, r8
0089F904  E8 7F 89 BB FF                  call 0x140458288
0089F909  3D 25 02 00 C0                  cmp eax, 0xc0000225
0089F90E  0F 84 0A FB FF FF               je 0x14089f41e
0089F914  48 8B 8C 24 E0 00 00 00         mov rcx, qword ptr [rsp + 0xe0]
0089F91C  E8 4B 4E BE FF                  call 0x14048476c
0089F921  48 8B D0                        mov rdx, rax
0089F924  66 44 39 60 04                  cmp word ptr [rax + 4], r12w
0089F929  0F 85 EF FA FF FF               jne 0x14089f41e
0089F92F  48 8B 84 24 80 00 00 00         mov rax, qword ptr [rsp + 0x80]
0089F937  4C 8B 84 24 B0 00 00 00         mov r8, qword ptr [rsp + 0xb0]
0089F93F  41 0F B7 08                     movzx ecx, word ptr [r8]
0089F943  66 2B 08                        sub cx, word ptr [rax]
0089F946  0F B7 42 02                     movzx eax, word ptr [rdx + 2]
0089F94A  66 89 44 24 28                  mov word ptr [rsp + 0x28], ax
0089F94F  66 89 4C 24 20                  mov word ptr [rsp + 0x20], cx
0089F954  4D 8B C8                        mov r9, r8
0089F957  44 0F B7 02                     movzx r8d, word ptr [rdx]
0089F95B  49 8B CE                        mov rcx, r14
0089F95E  E8 69 27 00 00                  call 0x1408a20cc
0089F963  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
0089F967  85 C0                           test eax, eax
0089F969  0F 89 AF FA FF FF               jns 0x14089f41e
0089F96F  41 89 46 30                     mov dword ptr [r14 + 0x30], eax
0089F973  4D 89 66 38                     mov qword ptr [r14 + 0x38], r12
0089F977  80 E3 FB                        and bl, 0xfb
0089F97A  E9 9F FA FF FF                  jmp 0x14089f41e
0089F97F  45 33 C0                        xor r8d, r8d
0089F982  33 D2                           xor edx, edx
0089F984  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
0089F989  E8 E2 0F 9D FF                  call 0x140270970
0089F98E  4D 85 ED                        test r13, r13
0089F991  0F 85 D0 0E 00 00               jne 0x1408a0867
0089F997  B8 9A 00 00 C0                  mov eax, 0xc000009a
0089F99C  E9 EE 0E 00 00                  jmp 0x1408a088f
0089F9A1  49 8B 4F 60                     mov rcx, qword ptr [r15 + 0x60]
0089F9A5  48 8B 56 08                     mov rdx, qword ptr [rsi + 8]
0089F9A9  E8 62 71 E2 FF                  call 0x1406c6b10
0089F9AE  85 C0                           test eax, eax
0089F9B0  0F 84 E6 FB FF FF               je 0x14089f59c
0089F9B6  E9 74 FB FF FF                  jmp 0x14089f52f
0089F9BB  83 E0 EF                        and eax, 0xffffffef
0089F9BE  89 87 98 00 00 00               mov dword ptr [rdi + 0x98], eax
0089F9C4  E9 D0 F7 FF FF                  jmp 0x14089f199
0089F9C9  BA 40 00 00 00                  mov edx, 0x40
0089F9CE  E9 D3 FA FF FF                  jmp 0x14089f4a6
0089F9D3  41 8B 4E 30                     mov ecx, dword ptr [r14 + 0x30]
0089F9D7  89 4F 10                        mov dword ptr [rdi + 0x10], ecx
0089F9DA  49 8B 46 38                     mov rax, qword ptr [r14 + 0x38]
0089F9DE  48 89 47 18                     mov qword ptr [rdi + 0x18], rax
0089F9E2  81 F9 04 01 00 00               cmp ecx, 0x104
0089F9E8  0F 84 B9 0C 00 00               je 0x1408a06a7
0089F9EE  66 45 39 67 58                  cmp word ptr [r15 + 0x58], r12w
0089F9F3  74 0B                           je 0x14089fa00
0089F9F5  33 D2                           xor edx, edx
0089F9F7  49 8B 4F 60                     mov rcx, qword ptr [r15 + 0x60]
0089F9FB  E8 70 2E 2E 00                  call 0x140b82870
0089FA00  49 8B CF                        mov rcx, r15
0089FA03  E8 E8 CA AE FF                  call 0x14038c4f0
0089FA08  45 33 C0                        xor r8d, r8d
0089FA0B  33 D2                           xor edx, edx
0089FA0D  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
0089FA12  E8 59 0F 9D FF                  call 0x140270970
0089FA17  48 8B 84 24 90 00 00 00         mov rax, qword ptr [rsp + 0x90]
0089FA1F  48 85 C0                        test rax, rax
0089FA22  74 08                           je 0x14089fa2c
0089FA24  48 8B C8                        mov rcx, rax
0089FA27  E8 48 FA B9 FF                  call 0x14043f474
0089FA2C  49 8B CE                        mov rcx, r14
0089FA2F  E8 3C E5 9A FF                  call 0x14024df70
0089FA34  8B 44 24 64                     mov eax, dword ptr [rsp + 0x64]
0089FA38  E9 52 0E 00 00                  jmp 0x1408a088f
0089FA3D  0C 80                           or al, 0x80
0089FA3F  41 88 45 02                     mov byte ptr [r13 + 2], al
0089FA43  E9 25 F8 FF FF                  jmp 0x14089f26d
0089FA48  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0089FA51  F7 40 74 00 04 00 00            test dword ptr [rax + 0x74], 0x400
0089FA58  0F 85 BD 09 00 00               jne 0x1408a041b
0089FA5E  80 CB 80                        or bl, 0x80
0089FA61  0F B6 F3                        movzx esi, bl
0089FA64  40 C0 EE 07                     shr sil, 7
0089FA68  4C 8B BC 24 A0 00 00 00         mov r15, qword ptr [rsp + 0xa0]
0089FA70  49 8D 87 98 00 00 00            lea rax, [r15 + 0x98]
0089FA77  48 89 84 24 00 01 00 00         mov qword ptr [rsp + 0x100], rax
0089FA7F  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
0089FA84  44 0F B6 CE                     movzx r9d, sil
0089FA88  45 33 C0                        xor r8d, r8d
0089FA8B  33 D2                           xor edx, edx
0089FA8D  48 8B C8                        mov rcx, rax
0089FA90  E8 1B EC 96 FF                  call 0x14020e6b0
0089FA95  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
0089FA99  3D 01 01 00 00                  cmp eax, 0x101
0089FA9E  0F 84 6B 03 00 00               je 0x14089fe0f
0089FAA4  8B 84 24 10 01 00 00            mov eax, dword ptr [rsp + 0x110]
0089FAAB  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
0089FAAF  E9 D0 F9 FF FF                  jmp 0x14089f484
0089FAB4  81 8E 80 00 00 00 00 00 02 00   or dword ptr [rsi + 0x80], 0x20000
0089FABE  E9 A2 FB FF FF                  jmp 0x14089f665
0089FAC3  48 8B 8C 24 C8 00 00 00         mov rcx, qword ptr [rsp + 0xc8]
0089FACB  E8 D0 E3 AE FF                  call 0x14038dea0
0089FAD0  8B 44 24 64                     mov eax, dword ptr [rsp + 0x64]
0089FAD4  E9 D0 FC FF FF                  jmp 0x14089f7a9
0089FAD9  4D 85 ED                        test r13, r13
0089FADC  74 08                           je 0x14089fae6
0089FADE  49 8B CD                        mov rcx, r13
0089FAE1  E8 8E F9 B9 FF                  call 0x14043f474
0089FAE6  45 33 C0                        xor r8d, r8d
0089FAE9  33 D2                           xor edx, edx
0089FAEB  49 8B CE                        mov rcx, r14
0089FAEE  E8 7D 0E 9D FF                  call 0x140270970
0089FAF3  8B 44 24 64                     mov eax, dword ptr [rsp + 0x64]
0089FAF7  E9 93 0D 00 00                  jmp 0x1408a088f
0089FAFC  49 8B CE                        mov rcx, r14
0089FAFF  E8 6C E4 9A FF                  call 0x14024df70
0089FB04  45 33 C0                        xor r8d, r8d
0089FB07  33 D2                           xor edx, edx
0089FB09  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
0089FB0E  E8 5D 0E 9D FF                  call 0x140270970
0089FB13  48 8B 84 24 90 00 00 00         mov rax, qword ptr [rsp + 0x90]
0089FB1B  48 85 C0                        test rax, rax
0089FB1E  0F 84 42 F6 FF FF               je 0x14089f166
0089FB24  48 8B C8                        mov rcx, rax
0089FB27  E8 48 F9 B9 FF                  call 0x14043f474
0089FB2C  E9 35 F6 FF FF                  jmp 0x14089f166
0089FB31  49 BE FD FF FF 5F FF FF FF FF   movabs r14, 0xffffffff5ffffffd
0089FB3B  48 F7 C1 FD FF FF FF            test rcx, -3
0089FB42  0F 85 93 00 00 00               jne 0x14089fbdb
0089FB48  41 0F B7 47 58                  movzx eax, word ptr [r15 + 0x58]
0089FB4D  48 8B 8C 24 B0 00 00 00         mov rcx, qword ptr [rsp + 0xb0]
0089FB55  66 39 41 02                     cmp word ptr [rcx + 2], ax
0089FB59  73 55                           jae 0x14089fbb0
0089FB5B  8B D0                           mov edx, eax
0089FB5D  B9 00 01 00 00                  mov ecx, 0x100
0089FB62  41 B8 49 6F 46 63               mov r8d, 0x63466f49
0089FB68  E8 83 25 2E 00                  call 0x140b820f0
0089FB6D  4C 8B F0                        mov r14, rax
0089FB70  48 85 C0                        test rax, rax
0089FB73  0F 84 A7 07 00 00               je 0x1408a0320
0089FB79  48 8B 84 24 B0 00 00 00         mov rax, qword ptr [rsp + 0xb0]
0089FB81  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
0089FB85  48 85 C9                        test rcx, rcx
0089FB88  74 07                           je 0x14089fb91
0089FB8A  33 D2                           xor edx, edx
0089FB8C  E8 DF 2C 2E 00                  call 0x140b82870
0089FB91  48 8B 8C 24 B0 00 00 00         mov rcx, qword ptr [rsp + 0xb0]
0089FB99  4C 89 71 08                     mov qword ptr [rcx + 8], r14
0089FB9D  41 0F B7 47 58                  movzx eax, word ptr [r15 + 0x58]
0089FBA2  66 89 41 02                     mov word ptr [rcx + 2], ax
0089FBA6  49 BE FD FF FF 5F FF FF FF FF   movabs r14, 0xffffffff5ffffffd
0089FBB0  49 8D 57 58                     lea rdx, [r15 + 0x58]
0089FBB4  E8 77 F3 B5 FF                  call 0x1403fef30
0089FBB9  48 8B 8C 24 18 01 00 00         mov rcx, qword ptr [rsp + 0x118]
0089FBC1  49 03 CE                        add rcx, r14
0089FBC4  48 83 F9 16                     cmp rcx, 0x16
0089FBC8  77 2F                           ja 0x14089fbf9
0089FBCA  B8 01 02 40 00                  mov eax, 0x400201
0089FBCF  48 0F A3 C8                     bt rax, rcx
0089FBD3  73 24                           jae 0x14089fbf9
0089FBD5  4C 89 67 28                     mov qword ptr [rdi + 0x28], r12
0089FBD9  EB 1E                           jmp 0x14089fbf9
0089FBDB  4A 8D 04 31                     lea rax, [rcx + r14]
0089FBDF  48 83 F8 16                     cmp rax, 0x16
0089FBE3  77 14                           ja 0x14089fbf9
0089FBE5  B9 01 02 40 00                  mov ecx, 0x400201
0089FBEA  48 0F A3 C1                     bt rcx, rax
0089FBEE  73 09                           jae 0x14089fbf9
0089FBF0  45 84 ED                        test r13b, r13b
0089FBF3  0F 84 4F FF FF FF               je 0x14089fb48
0089FBF9  66 45 39 67 58                  cmp word ptr [r15 + 0x58], r12w
0089FBFE  74 10                           je 0x14089fc10
0089FC00  33 D2                           xor edx, edx
0089FC02  49 8B 4F 60                     mov rcx, qword ptr [r15 + 0x60]
0089FC06  E8 65 2C 2E 00                  call 0x140b82870
0089FC0B  66 45 89 67 58                  mov word ptr [r15 + 0x58], r12w
0089FC10  4D 89 67 08                     mov qword ptr [r15 + 8], r12
0089FC14  49 8B CF                        mov rcx, r15
0089FC17  E8 34 97 A5 FF                  call 0x1402f9350
0089FC1C  4C 89 67 08                     mov qword ptr [rdi + 8], r12
0089FC20  45 33 C0                        xor r8d, r8d
0089FC23  33 D2                           xor edx, edx
0089FC25  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
0089FC2A  48 8B CE                        mov rcx, rsi
0089FC2D  E8 3E 0D 9D FF                  call 0x140270970
0089FC32  48 8B 84 24 90 00 00 00         mov rax, qword ptr [rsp + 0x90]
0089FC3A  48 85 C0                        test rax, rax
0089FC3D  74 08                           je 0x14089fc47
0089FC3F  48 8B C8                        mov rcx, rax
0089FC42  E8 2D F8 B9 FF                  call 0x14043f474
0089FC47  48 8B 94 24 18 01 00 00         mov rdx, qword ptr [rsp + 0x118]
0089FC4F  48 83 FA 01                     cmp rdx, 1
0089FC53  0F 84 CA 07 00 00               je 0x1408a0423
0089FC59  4C 89 67 28                     mov qword ptr [rdi + 0x28], r12
0089FC5D  4A 8D 04 32                     lea rax, [rdx + r14]
0089FC61  41 B8 01 02 40 00               mov r8d, 0x400201
0089FC67  48 83 F8 16                     cmp rax, 0x16
0089FC6B  77 48                           ja 0x14089fcb5
0089FC6D  49 0F A3 C0                     bt r8, rax
0089FC71  73 42                           jae 0x14089fcb5
0089FC73  8B 8F 98 00 00 00               mov ecx, dword ptr [rdi + 0x98]
0089FC79  83 C9 10                        or ecx, 0x10
0089FC7C  89 8F 98 00 00 00               mov dword ptr [rdi + 0x98], ecx
0089FC82  8B 46 48                        mov eax, dword ptr [rsi + 0x48]
0089FC85  83 F8 24                        cmp eax, 0x24
0089FC88  0F 87 40 0A 00 00               ja 0x1408a06ce
0089FC8E  49 B9 84 00 02 80 10 00 00 00   movabs r9, 0x1080020084
0089FC98  49 0F A3 C1                     bt r9, rax
0089FC9C  0F 83 2C 0A 00 00               jae 0x1408a06ce
0089FCA2  B0 01                           mov al, 1
0089FCA4  84 C0                           test al, al
0089FCA6  0F 84 9A 07 00 00               je 0x1408a0446
0089FCAC  83 C9 08                        or ecx, 8
0089FCAF  89 8F 98 00 00 00               mov dword ptr [rdi + 0x98], ecx
0089FCB5  44 38 A7 88 00 00 00            cmp byte ptr [rdi + 0x88], r12b
0089FCBC  0F 85 55 0B 00 00               jne 0x1408a0817
0089FCC2  48 8B 86 38 01 00 00            mov rax, qword ptr [rsi + 0x138]
0089FCC9  F7 40 20 00 08 00 00            test dword ptr [rax + 0x20], 0x800
0089FCD0  75 19                           jne 0x14089fceb
0089FCD2  48 8B 8C 24 D8 00 00 00         mov rcx, qword ptr [rsp + 0xd8]
0089FCDA  8B 41 18                        mov eax, dword ptr [rcx + 0x18]
0089FCDD  89 41 10                        mov dword ptr [rcx + 0x10], eax
0089FCE0  44 89 61 14                     mov dword ptr [rcx + 0x14], r12d
0089FCE4  81 61 0C FF FE FF FF            and dword ptr [rcx + 0xc], 0xfffffeff
0089FCEB  4A 8D 04 32                     lea rax, [rdx + r14]
0089FCEF  48 83 F8 16                     cmp rax, 0x16
0089FCF3  77 0A                           ja 0x14089fcff
0089FCF5  49 0F A3 C0                     bt r8, rax
0089FCF9  0F 82 84 04 00 00               jb 0x1408a0183
0089FCFF  B9 19 00 00 A0                  mov ecx, 0xa0000019
0089FD04  48 3B D1                        cmp rdx, rcx
0089FD07  0F 85 62 04 00 00               jne 0x1408a016f
0089FD0D  48 8B 9C 24 F0 00 00 00         mov rbx, qword ptr [rsp + 0xf0]
0089FD15  48 8B 4B 08                     mov rcx, qword ptr [rbx + 8]
0089FD19  E8 42 0A 1D 00                  call 0x140a70760
0089FD1E  48 89 43 08                     mov qword ptr [rbx + 8], rax
0089FD22  B8 68 03 00 00                  mov eax, 0x368
0089FD27  E9 63 0B 00 00                  jmp 0x1408a088f
0089FD2C  49 8B CE                        mov rcx, r14
0089FD2F  E8 3C E2 9A FF                  call 0x14024df70
0089FD34  45 33 C0                        xor r8d, r8d
0089FD37  33 D2                           xor edx, edx
0089FD39  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
0089FD3E  E8 2D 0C 9D FF                  call 0x140270970
0089FD43  4C 8B AC 24 90 00 00 00         mov r13, qword ptr [rsp + 0x90]
0089FD4B  4D 85 ED                        test r13, r13
0089FD4E  0F 84 12 F4 FF FF               je 0x14089f166
0089FD54  E9 06 0B 00 00                  jmp 0x1408a085f
0089FD59  49 8B 86 38 01 00 00            mov rax, qword ptr [r14 + 0x138]
0089FD60  F7 40 20 00 08 00 00            test dword ptr [rax + 0x20], 0x800
0089FD67  0F 85 88 EB FF FF               jne 0x14089e8f5
0089FD6D  45 84 C9                        test r9b, r9b
0089FD70  75 0B                           jne 0x14089fd7d
0089FD72  8B 47 54                        mov eax, dword ptr [rdi + 0x54]
0089FD75  A8 01                           test al, 1
0089FD77  0F 84 78 EB FF FF               je 0x14089e8f5
0089FD7D  48 85 D2                        test rdx, rdx
0089FD80  75 0A                           jne 0x14089fd8c
0089FD82  66 45 39 20                     cmp word ptr [r8], r12w
0089FD86  0F 84 69 EB FF FF               je 0x14089e8f5
0089FD8C  44 38 A4 24 88 00 00 00         cmp byte ptr [rsp + 0x88], r12b
0089FD94  0F 85 5B EB FF FF               jne 0x14089e8f5
0089FD9A  4C 89 A4 24 98 00 00 00         mov qword ptr [rsp + 0x98], r12
0089FDA2  44 88 64 24 50                  mov byte ptr [rsp + 0x50], r12b
0089FDA7  48 8B 84 24 A8 00 00 00         mov rax, qword ptr [rsp + 0xa8]
0089FDAF  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
0089FDB4  48 8D 84 24 28 01 00 00         lea rax, [rsp + 0x128]
0089FDBC  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
0089FDC1  48 8B 84 24 B0 00 00 00         mov rax, qword ptr [rsp + 0xb0]
0089FDC9  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0089FDCE  48 8D 84 24 8C 00 00 00         lea rax, [rsp + 0x8c]
0089FDD6  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0089FDDB  4C 89 64 24 28                  mov qword ptr [rsp + 0x28], r12
0089FDE0  8B 47 58                        mov eax, dword ptr [rdi + 0x58]
0089FDE3  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
0089FDE7  45 8B CF                        mov r9d, r15d
0089FDEA  4C 8B 84 24 D8 00 00 00         mov r8, qword ptr [rsp + 0xd8]
0089FDF2  49 8B D6                        mov rdx, r14
0089FDF5  E8 A6 5F B0 FF                  call 0x1403a5da0
0089FDFA  84 C0                           test al, al
0089FDFC  0F 84 BA EB FF FF               je 0x14089e9bc
0089FE02  4C 8B 84 24 80 00 00 00         mov r8, qword ptr [rsp + 0x80]
0089FE0A  E9 E6 EA FF FF                  jmp 0x14089e8f5
0089FE0F  45 0F 20 C5                     mov r13, cr8
0089FE13  B8 01 00 00 00                  mov eax, 1
0089FE18  44 0F 22 C0                     mov cr8, rax
0089FE1C  44 39 25 FD 6E 72 00            cmp dword ptr [rip + 0x726efd], r12d
0089FE23  0F 85 ED 08 00 00               jne 0x1408a0716
0089FE29  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0089FE32  8B 88 A0 05 00 00               mov ecx, dword ptr [rax + 0x5a0]
0089FE38  4C 8B BC 24 A0 00 00 00         mov r15, qword ptr [rsp + 0xa0]
0089FE40  F6 C1 01                        test cl, 1
0089FE43  0F 85 52 07 00 00               jne 0x1408a059b
0089FE49  45 39 A7 9C 00 00 00            cmp dword ptr [r15 + 0x9c], r12d
0089FE50  0F 84 3B 07 00 00               je 0x1408a0591
0089FE56  44 39 25 C3 6E 72 00            cmp dword ptr [rip + 0x726ec3], r12d
0089FE5D  74 0D                           je 0x14089fe6c
0089FE5F  44 0F 20 C1                     mov rcx, cr8
0089FE63  41 0F B6 D5                     movzx edx, r13b
0089FE67  E8 2C 58 C5 FF                  call 0x1404f5698
0089FE6C  41 0F B6 C5                     movzx eax, r13b
0089FE70  44 0F 22 C0                     mov cr8, rax
0089FE74  48 8B 84 24 00 01 00 00         mov rax, qword ptr [rsp + 0x100]
0089FE7C  E9 FE FB FF FF                  jmp 0x14089fa7f
0089FE81  49 8B 86 A0 00 00 00            mov rax, qword ptr [r14 + 0xa0]
0089FE88  48 89 84 24 E8 00 00 00         mov qword ptr [rsp + 0xe8], rax
0089FE90  4D 85 C0                        test r8, r8
0089FE93  74 17                           je 0x14089feac
0089FE95  48 8D 94 24 E0 00 00 00         lea rdx, [rsp + 0xe0]
0089FE9D  49 8B C8                        mov rcx, r8
0089FEA0  E8 E3 83 BB FF                  call 0x140458288
0089FEA5  3D 25 02 00 C0                  cmp eax, 0xc0000225
0089FEAA  75 73                           jne 0x14089ff1f
0089FEAC  48 8B 84 24 80 00 00 00         mov rax, qword ptr [rsp + 0x80]
0089FEB4  48 8B 8C 24 B0 00 00 00         mov rcx, qword ptr [rsp + 0xb0]
0089FEBC  44 0F B7 09                     movzx r9d, word ptr [rcx]
0089FEC0  66 44 2B 08                     sub r9w, word ptr [rax]
0089FEC4  48 8D 84 24 E0 00 00 00         lea rax, [rsp + 0xe0]
0089FECC  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0089FED1  4C 8B C1                        mov r8, rcx
0089FED4  49 8B D7                        mov rdx, r15
0089FED7  49 8B CE                        mov rcx, r14
0089FEDA  E8 B1 20 00 00                  call 0x1408a1f90
0089FEDF  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
0089FEE3  85 C0                           test eax, eax
0089FEE5  0F 88 24 04 00 00               js 0x1408a030f
0089FEEB  48 8B 84 24 C0 00 00 00         mov rax, qword ptr [rsp + 0xc0]
0089FEF3  48 85 C0                        test rax, rax
0089FEF6  75 2F                           jne 0x14089ff27
0089FEF8  41 8B 4E 10                     mov ecx, dword ptr [r14 + 0x10]
0089FEFC  81 E1 80 00 00 00               and ecx, 0x80
0089FF02  74 0C                           je 0x14089ff10
0089FF04  49 8B 56 70                     mov rdx, qword ptr [r14 + 0x70]
0089FF08  48 89 94 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], rdx
0089FF10  B8 0D 00 00 C0                  mov eax, 0xc000000d
0089FF15  85 C9                           test ecx, ecx
0089FF17  41 0F 45 C4                     cmovne eax, r12d
0089FF1B  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
0089FF1F  48 8B 84 24 C0 00 00 00         mov rax, qword ptr [rsp + 0xc0]
0089FF27  41 81 7E 30 04 01 00 00         cmp dword ptr [r14 + 0x30], 0x104
0089FF2F  0F 85 75 ED FF FF               jne 0x14089ecaa
0089FF35  85 F6                           test esi, esi
0089FF37  48 8B B4 24 E8 00 00 00         mov rsi, qword ptr [rsp + 0xe8]
0089FF3F  0F 85 88 06 00 00               jne 0x1408a05cd
0089FF45  45 0F B6 CD                     movzx r9d, r13b
0089FF49  4C 8B C6                        mov r8, rsi
0089FF4C  49 8B D7                        mov rdx, r15
0089FF4F  49 8B CE                        mov rcx, r14
0089FF52  E8 5D 31 19 00                  call 0x140a330b4
0089FF57  48 B9 FD FF FF 5F FF FF FF FF   movabs rcx, 0xffffffff5ffffffd
0089FF61  49 03 4E 38                     add rcx, qword ptr [r14 + 0x38]
0089FF65  48 83 F9 16                     cmp rcx, 0x16
0089FF69  0F 87 3B ED FF FF               ja 0x14089ecaa
0089FF6F  B8 01 02 40 00                  mov eax, 0x400201
0089FF74  48 0F A3 C8                     bt rax, rcx
0089FF78  0F 83 2C ED FF FF               jae 0x14089ecaa
0089FF7E  45 39 66 30                     cmp dword ptr [r14 + 0x30], r12d
0089FF82  0F 8C FD 02 00 00               jl 0x1408a0285
0089FF88  0F B7 56 06                     movzx edx, word ptr [rsi + 6]
0089FF8C  41 8B CC                        mov ecx, r12d
0089FF8F  66 85 D2                        test dx, dx
0089FF92  B8 10 00 00 00                  mov eax, 0x10
0089FF97  0F 44 C8                        cmove ecx, eax
0089FF9A  0F B6 C3                        movzx eax, bl
0089FF9D  24 EF                           and al, 0xef
0089FF9F  0F B6 D9                        movzx ebx, cl
0089FFA2  0A D8                           or bl, al
0089FFA4  48 8B 84 24 80 00 00 00         mov rax, qword ptr [rsp + 0x80]
0089FFAC  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
0089FFB0  48 2B CA                        sub rcx, rdx
0089FFB3  0F B7 00                        movzx eax, word ptr [rax]
0089FFB6  66 85 D2                        test dx, dx
0089FFB9  74 0B                           je 0x14089ffc6
0089FFBB  66 83 3C 01 3A                  cmp word ptr [rcx + rax], 0x3a
0089FFC0  0F 85 BF 02 00 00               jne 0x1408a0285
0089FFC6  8B 4F 40                        mov ecx, dword ptr [rdi + 0x40]
0089FFC9  F6 C1 41                        test cl, 0x41
0089FFCC  0F 85 B3 02 00 00               jne 0x1408a0285
0089FFD2  48 8B 84 24 50 01 00 00         mov rax, qword ptr [rsp + 0x150]
0089FFDA  44 38 20                        cmp byte ptr [rax], r12b
0089FFDD  0F 85 A2 02 00 00               jne 0x1408a0285
0089FFE3  8B 06                           mov eax, dword ptr [rsi]
0089FFE5  BA 03 00 00 A0                  mov edx, 0xa0000003
0089FFEA  3B C2                           cmp eax, edx
0089FFEC  0F 85 6F 02 00 00               jne 0x1408a0261
0089FFF2  83 C9 01                        or ecx, 1
0089FFF5  E9 88 02 00 00                  jmp 0x1408a0282
0089FFFA  48 8B 84 24 98 00 00 00         mov rax, qword ptr [rsp + 0x98]
008A0002  48 89 84 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], rax
008A000A  41 8B F7                        mov esi, r15d
008A000D  83 CE 20                        or esi, 0x20
008A0010  44 89 64 24 78                  mov dword ptr [rsp + 0x78], r12d
008A0015  48 8B 84 24 A8 00 00 00         mov rax, qword ptr [rsp + 0xa8]
008A001D  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
008A0024  90                              nop
008A0025  B2 01                           mov dl, 1
008A0027  48 8D 0D 72 D2 6E 00            lea rcx, [rip + 0x6ed272]
008A002E  E8 8D 1B 97 FF                  call 0x140211bc0
008A0033  49 8D 4D 20                     lea rcx, [r13 + 0x20]
008A0037  E8 84 64 02 00                  call 0x1408c64c0
008A003C  48 8B 05 9D 6A 72 00            mov rax, qword ptr [rip + 0x726a9d]
008A0043  48 83 C0 4C                     add rax, 0x4c
008A0047  48 8D 4C 24 78                  lea rcx, [rsp + 0x78]
008A004C  48 89 4C 24 48                  mov qword ptr [rsp + 0x48], rcx
008A0051  48 8D 8C 24 8C 00 00 00         lea rcx, [rsp + 0x8c]
008A0059  48 89 4C 24 40                  mov qword ptr [rsp + 0x40], rcx
008A005E  C6 44 24 38 01                  mov byte ptr [rsp + 0x38], 1
008A0063  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
008A0068  48 8D 84 24 C8 00 00 00         lea rax, [rsp + 0xc8]
008A0070  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008A0075  44 89 64 24 20                  mov dword ptr [rsp + 0x20], r12d
008A007A  44 8B CE                        mov r9d, esi
008A007D  41 B0 01                        mov r8b, 1
008A0080  49 8D 55 20                     lea rdx, [r13 + 0x20]
008A0084  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
008A0089  48 8B 88 10 01 00 00            mov rcx, qword ptr [rax + 0x110]
008A0090  E8 2B 6B B0 FF                  call 0x1403a6bc0
008A0095  0F B6 F0                        movzx esi, al
008A0098  48 8B 94 24 C8 00 00 00         mov rdx, qword ptr [rsp + 0xc8]
008A00A0  48 85 D2                        test rdx, rdx
008A00A3  0F 85 4A 07 00 00               jne 0x1408a07f3
008A00A9  49 8D 4D 20                     lea rcx, [r13 + 0x20]
008A00AD  E8 6E 64 02 00                  call 0x1408c6520
008A00B2  48 8D 0D E7 D1 6E 00            lea rcx, [rip + 0x6ed1e7]
008A00B9  E8 52 F9 9B FF                  call 0x14025fa10
008A00BE  48 8B 8C 24 A8 00 00 00         mov rcx, qword ptr [rsp + 0xa8]
008A00C6  E8 25 EF 9B FF                  call 0x14025eff0
008A00CB  40 32 F3                        xor sil, bl
008A00CE  40 80 E6 01                     and sil, 1
008A00D2  40 32 DE                        xor bl, sil
008A00D5  4C 8B 74 24 70                  mov r14, qword ptr [rsp + 0x70]
008A00DA  E9 87 E7 FF FF                  jmp 0x14089e866
008A00DF  49 8B 42 18                     mov rax, qword ptr [r10 + 0x18]
008A00E3  48 8B D0                        mov rdx, rax
008A00E6  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
008A00EB  4C 8B C0                        mov r8, rax
008A00EE  48 8B C8                        mov rcx, rax
008A00F1  4C 8B C8                        mov r9, rax
008A00F4  4C 8B D8                        mov r11, rax
008A00F7  4C 8B D0                        mov r10, rax
008A00FA  48 85 C0                        test rax, rax
008A00FD  0F 85 CD E5 FF FF               jne 0x14089e6d0
008A0103  E9 D8 E5 FF FF                  jmp 0x14089e6e0
008A0108  41 8B 4F 48                     mov ecx, dword ptr [r15 + 0x48]
008A010C  4C 39 47 18                     cmp qword ptr [rdi + 0x18], r8
008A0110  0F 84 39 06 00 00               je 0x1408a074f
008A0116  83 F9 24                        cmp ecx, 0x24
008A0119  0F 87 3E 03 00 00               ja 0x1408a045d
008A011F  48 0F A3 CA                     bt rdx, rcx
008A0123  0F 83 34 03 00 00               jae 0x1408a045d
008A0129  B2 01                           mov dl, 1
008A012B  83 F9 36                        cmp ecx, 0x36
008A012E  0F 87 30 03 00 00               ja 0x1408a0464
008A0134  49 0F A3 C9                     bt r9, rcx
008A0138  0F 83 26 03 00 00               jae 0x1408a0464
008A013E  B0 01                           mov al, 1
008A0140  84 D2                           test dl, dl
008A0142  0F 84 23 03 00 00               je 0x1408a046b
008A0148  0F B6 8F 98 00 00 00            movzx ecx, byte ptr [rdi + 0x98]
008A014F  80 E1 08                        and cl, 8
008A0152  4C 8B 87 A8 00 00 00            mov r8, qword ptr [rdi + 0xa8]
008A0159  E8 6E CE 1A 00                  call 0x140a4cfcc
008A015E  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
008A0162  85 C0                           test eax, eax
008A0164  0F 89 3E E5 FF FF               jns 0x14089e6a8
008A016A  E9 FB EF FF FF                  jmp 0x14089f16a
008A016F  48 83 FA 02                     cmp rdx, 2
008A0173  0F 84 94 FB FF FF               je 0x14089fd0d
008A0179  B8 04 01 00 00                  mov eax, 0x104
008A017E  E9 0C 07 00 00                  jmp 0x1408a088f
008A0183  45 84 ED                        test r13b, r13b
008A0186  0F 84 73 FB FF FF               je 0x14089fcff
008A018C  48 8B 84 24 E8 00 00 00         mov rax, qword ptr [rsp + 0xe8]
008A0194  48 89 47 18                     mov qword ptr [rdi + 0x18], rax
008A0198  C7 47 10 2D 00 00 80            mov dword ptr [rdi + 0x10], 0x8000002d
008A019F  B8 2D 00 00 80                  mov eax, 0x8000002d
008A01A4  E9 E6 06 00 00                  jmp 0x1408a088f
008A01A9  49 8B CE                        mov rcx, r14
008A01AC  E8 BF DD 9A FF                  call 0x14024df70
008A01B1  45 33 C0                        xor r8d, r8d
008A01B4  33 D2                           xor edx, edx
008A01B6  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
008A01BB  E8 B0 07 9D FF                  call 0x140270970
008A01C0  4C 8B AC 24 90 00 00 00         mov r13, qword ptr [rsp + 0x90]
008A01C8  4D 85 ED                        test r13, r13
008A01CB  74 08                           je 0x1408a01d5
008A01CD  49 8B CD                        mov rcx, r13
008A01D0  E8 9F F2 B9 FF                  call 0x14043f474
008A01D5  4D 89 67 08                     mov qword ptr [r15 + 8], r12
008A01D9  49 8B CF                        mov rcx, r15
008A01DC  44 38 A7 89 00 00 00            cmp byte ptr [rdi + 0x89], r12b
008A01E3  0F 85 65 02 00 00               jne 0x1408a044e
008A01E9  E8 62 91 A5 FF                  call 0x1402f9350
008A01EE  B8 9A 00 00 C0                  mov eax, 0xc000009a
008A01F3  E9 97 06 00 00                  jmp 0x1408a088f
008A01F8  4C 39 67 28                     cmp qword ptr [rdi + 0x28], r12
008A01FC  0F 85 17 E5 FF FF               jne 0x14089e719
008A0202  E8 09 55 98 FF                  call 0x140225710
008A0207  48 8B C8                        mov rcx, rax
008A020A  E8 F1 EA BB FF                  call 0x14045ed00
008A020F  8B F0                           mov esi, eax
008A0211  E8 BA 01 99 FF                  call 0x1402303d0
008A0216  3B F0                           cmp esi, eax
008A0218  75 12                           jne 0x1408a022c
008A021A  44 39 25 FF 5E 5C 00            cmp dword ptr [rip + 0x5c5eff], r12d
008A0221  74 31                           je 0x1408a0254
008A0223  F7 47 40 00 00 04 00            test dword ptr [rdi + 0x40], 0x40000
008A022A  75 28                           jne 0x1408a0254
008A022C  49 8B CE                        mov rcx, r14
008A022F  E8 A4 22 9D FF                  call 0x1402724d8
008A0234  48 8B F0                        mov rsi, rax
008A0237  48 85 C0                        test rax, rax
008A023A  74 18                           je 0x1408a0254
008A023C  48 8B C8                        mov rcx, rax
008A023F  E8 90 31 98 FF                  call 0x1402233d4
008A0244  48 8B CE                        mov rcx, rsi
008A0247  84 C0                           test al, al
008A0249  0F 84 AF 03 00 00               je 0x1408a05fe
008A024F  E8 FC 90 A5 FF                  call 0x1402f9350
008A0254  48 8B B4 24 80 00 00 00         mov rsi, qword ptr [rsp + 0x80]
008A025C  E9 B8 E4 FF FF                  jmp 0x14089e719
008A0261  3D 0C 00 00 A0                  cmp eax, 0xa000000c
008A0266  75 1D                           jne 0x1408a0285
008A0268  44 39 66 10                     cmp dword ptr [rsi + 0x10], r12d
008A026C  0F 8C 80 FD FF FF               jl 0x14089fff2
008A0272  3B C0                           cmp eax, eax
008A0274  75 0F                           jne 0x1408a0285
008A0276  F7 46 10 00 00 00 40            test dword ptr [rsi + 0x10], 0x40000000
008A027D  74 06                           je 0x1408a0285
008A027F  83 C9 40                        or ecx, 0x40
008A0282  89 4F 40                        mov dword ptr [rdi + 0x40], ecx
008A0285  45 84 ED                        test r13b, r13b
008A0288  0F 85 1C EA FF FF               jne 0x14089ecaa
008A028E  33 D2                           xor edx, edx
008A0290  48 8B CE                        mov rcx, rsi
008A0293  E8 D8 25 2E 00                  call 0x140b82870
008A0298  4C 89 A4 24 E8 00 00 00         mov qword ptr [rsp + 0xe8], r12
008A02A0  E9 05 EA FF FF                  jmp 0x14089ecaa
008A02A5  8B 46 48                        mov eax, dword ptr [rsi + 0x48]
008A02A8  83 F8 35                        cmp eax, 0x35
008A02AB  0F 87 3A F4 FF FF               ja 0x14089f6eb
008A02B1  48 B9 08 01 10 00 01 00 20 00   movabs rcx, 0x20000100100108
008A02BB  48 0F A3 C1                     bt rcx, rax
008A02BF  0F 82 04 F4 FF FF               jb 0x14089f6c9
008A02C5  E9 21 F4 FF FF                  jmp 0x14089f6eb
008A02CA  E8 61 5F B9 FF                  call 0x140436230
008A02CF  8B F0                           mov esi, eax
008A02D1  E8 FA 00 99 FF                  call 0x1402303d0
008A02D6  3B F0                           cmp esi, eax
008A02D8  0F 84 93 E7 FF FF               je 0x14089ea71
008A02DE  E8 2D 54 98 FF                  call 0x140225710
008A02E3  48 8B C8                        mov rcx, rax
008A02E6  E8 15 EA BB FF                  call 0x14045ed00
008A02EB  8B F0                           mov esi, eax
008A02ED  E8 DE 00 99 FF                  call 0x1402303d0
008A02F2  3B F0                           cmp esi, eax
008A02F4  0F 84 77 E7 FF FF               je 0x14089ea71
008A02FA  E8 AD 58 C3 FF                  call 0x1404d5bac
008A02FF  84 C0                           test al, al
008A0301  0F 85 6A E7 FF FF               jne 0x14089ea71
008A0307  41 B6 01                        mov r14b, 1
008A030A  E9 65 E7 FF FF                  jmp 0x14089ea74
008A030F  4D 89 66 38                     mov qword ptr [r14 + 0x38], r12
008A0313  8B 44 24 64                     mov eax, dword ptr [rsp + 0x64]
008A0317  41 89 46 30                     mov dword ptr [r14 + 0x30], eax
008A031B  E9 FF FB FF FF                  jmp 0x14089ff1f
008A0320  C7 47 10 9A 00 00 C0            mov dword ptr [rdi + 0x10], 0xc000009a
008A0327  B8 9A 00 00 C0                  mov eax, 0xc000009a
008A032C  E9 5E 05 00 00                  jmp 0x1408a088f
008A0331  48 8B 84 24 A8 00 00 00         mov rax, qword ptr [rsp + 0xa8]
008A0339  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
008A0340  90                              nop
008A0341  B2 01                           mov dl, 1
008A0343  48 8D 0D 56 CF 6E 00            lea rcx, [rip + 0x6ecf56]
008A034A  E8 71 18 97 FF                  call 0x140211bc0
008A034F  41 B8 20 00 00 00               mov r8d, 0x20
008A0355  49 8B D5                        mov rdx, r13
008A0358  49 8B 8E 10 01 00 00            mov rcx, qword ptr [r14 + 0x110]
008A035F  E8 D0 FE B5 FF                  call 0x140400234
008A0364  0F B6 C8                        movzx ecx, al
008A0367  32 C3                           xor al, bl
008A0369  24 01                           and al, 1
008A036B  32 D8                           xor bl, al
008A036D  F6 C1 01                        test cl, 1
008A0370  0F 85 19 E8 FF FF               jne 0x14089eb8f
008A0376  4C 89 A4 24 98 00 00 00         mov qword ptr [rsp + 0x98], r12
008A037E  49 8D 4D 20                     lea rcx, [r13 + 0x20]
008A0382  E8 39 61 02 00                  call 0x1408c64c0
008A0387  80 CB 20                        or bl, 0x20
008A038A  48 8B 05 4F 67 72 00            mov rax, qword ptr [rip + 0x72674f]
008A0391  48 83 C0 4C                     add rax, 0x4c
008A0395  44 0F B6 C3                     movzx r8d, bl
008A0399  41 C0 E8 05                     shr r8b, 5
008A039D  41 80 E0 01                     and r8b, 1
008A03A1  48 8D 4C 24 64                  lea rcx, [rsp + 0x64]
008A03A6  48 89 4C 24 48                  mov qword ptr [rsp + 0x48], rcx
008A03AB  48 8D 8C 24 8C 00 00 00         lea rcx, [rsp + 0x8c]
008A03B3  48 89 4C 24 40                  mov qword ptr [rsp + 0x40], rcx
008A03B8  C6 44 24 38 01                  mov byte ptr [rsp + 0x38], 1
008A03BD  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
008A03C2  48 8D 84 24 98 00 00 00         lea rax, [rsp + 0x98]
008A03CA  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008A03CF  44 89 64 24 20                  mov dword ptr [rsp + 0x20], r12d
008A03D4  41 B9 20 00 00 00               mov r9d, 0x20
008A03DA  49 8D 55 20                     lea rdx, [r13 + 0x20]
008A03DE  49 8B 8E 10 01 00 00            mov rcx, qword ptr [r14 + 0x110]
008A03E5  E8 D6 67 B0 FF                  call 0x1403a6bc0
008A03EA  32 C3                           xor al, bl
008A03EC  24 01                           and al, 1
008A03EE  32 D8                           xor bl, al
008A03F0  48 8B 94 24 98 00 00 00         mov rdx, qword ptr [rsp + 0x98]
008A03F8  48 85 D2                        test rdx, rdx
008A03FB  0F 84 8E E7 FF FF               je 0x14089eb8f
008A0401  49 8B CD                        mov rcx, r13
008A0404  E8 77 75 13 00                  call 0x1409d7980
008A0409  48 8B 8C 24 98 00 00 00         mov rcx, qword ptr [rsp + 0x98]
008A0411  E8 6A 59 BD FF                  call 0x140475d80
008A0416  E9 74 E7 FF FF                  jmp 0x14089eb8f
008A041B  80 E3 7F                        and bl, 0x7f
008A041E  E9 3E F6 FF FF                  jmp 0x14089fa61
008A0423  8B 84 24 F8 00 00 00            mov eax, dword ptr [rsp + 0xf8]
008A042A  FF C0                           inc eax
008A042C  89 84 24 F8 00 00 00            mov dword ptr [rsp + 0xf8], eax
008A0433  83 F8 20                        cmp eax, 0x20
008A0436  0F 86 92 03 00 00               jbe 0x1408a07ce
008A043C  B8 01 00 00 C0                  mov eax, 0xc0000001
008A0441  E9 49 04 00 00                  jmp 0x1408a088f
008A0446  83 E1 F7                        and ecx, 0xfffffff7
008A0449  E9 61 F8 FF FF                  jmp 0x14089fcaf
008A044E  E8 9D C0 AE FF                  call 0x14038c4f0
008A0453  B8 9A 00 00 C0                  mov eax, 0xc000009a
008A0458  E9 32 04 00 00                  jmp 0x1408a088f
008A045D  32 D2                           xor dl, dl
008A045F  E9 C7 FC FF FF                  jmp 0x1408a012b
008A0464  32 C0                           xor al, al
008A0466  E9 D5 FC FF FF                  jmp 0x1408a0140
008A046B  84 C0                           test al, al
008A046D  0F 85 D5 FC FF FF               jne 0x1408a0148
008A0473  C7 47 10 78 02 00 C0            mov dword ptr [rdi + 0x10], 0xc0000278
008A047A  B8 78 02 00 C0                  mov eax, 0xc0000278
008A047F  E9 0B 04 00 00                  jmp 0x1408a088f
008A0484  49 8B 4D 20                     mov rcx, qword ptr [r13 + 0x20]
008A0488  48 85 C9                        test rcx, rcx
008A048B  75 04                           jne 0x1408a0491
008A048D  49 8B 4D 30                     mov rcx, qword ptr [r13 + 0x30]
008A0491  E8 BA E1 15 00                  call 0x1409fe650
008A0496  84 C0                           test al, al
008A0498  0F 85 11 E6 FF FF               jne 0x14089eaaf
008A049E  80 E3 FE                        and bl, 0xfe
008A04A1  C7 44 24 64 22 00 00 C0         mov dword ptr [rsp + 0x64], 0xc0000022
008A04A9  4C 8B 74 24 70                  mov r14, qword ptr [rsp + 0x70]
008A04AE  E9 96 E6 FF FF                  jmp 0x14089eb49
008A04B3  49 8B 86 38 01 00 00            mov rax, qword ptr [r14 + 0x138]
008A04BA  F7 40 20 00 08 00 00            test dword ptr [rax + 0x20], 0x800
008A04C1  0F 85 4A E7 FF FF               jne 0x14089ec11
008A04C7  45 84 C9                        test r9b, r9b
008A04CA  75 0B                           jne 0x1408a04d7
008A04CC  8B 47 54                        mov eax, dword ptr [rdi + 0x54]
008A04CF  A8 01                           test al, 1
008A04D1  0F 84 3A E7 FF FF               je 0x14089ec11
008A04D7  44 38 A4 24 88 00 00 00         cmp byte ptr [rsp + 0x88], r12b
008A04DF  0F 85 2C E7 FF FF               jne 0x14089ec11
008A04E5  4C 89 A4 24 98 00 00 00         mov qword ptr [rsp + 0x98], r12
008A04ED  44 88 64 24 50                  mov byte ptr [rsp + 0x50], r12b
008A04F2  48 8B 84 24 A8 00 00 00         mov rax, qword ptr [rsp + 0xa8]
008A04FA  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
008A04FF  48 8D 84 24 28 01 00 00         lea rax, [rsp + 0x128]
008A0507  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
008A050C  48 8B 84 24 B0 00 00 00         mov rax, qword ptr [rsp + 0xb0]
008A0514  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
008A0519  48 8D 84 24 8C 00 00 00         lea rax, [rsp + 0x8c]
008A0521  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
008A0526  4C 89 64 24 28                  mov qword ptr [rsp + 0x28], r12
008A052B  8B 47 58                        mov eax, dword ptr [rdi + 0x58]
008A052E  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
008A0532  45 8B CF                        mov r9d, r15d
008A0535  4C 8B 84 24 D8 00 00 00         mov r8, qword ptr [rsp + 0xd8]
008A053D  49 8B D6                        mov rdx, r14
008A0540  49 8B CE                        mov rcx, r14
008A0543  E8 58 58 B0 FF                  call 0x1403a5da0
008A0548  84 C0                           test al, al
008A054A  0F 85 C1 E6 FF FF               jne 0x14089ec11
008A0550  E9 67 E4 FF FF                  jmp 0x14089e9bc
008A0555  48 8B 84 24 F0 00 00 00         mov rax, qword ptr [rsp + 0xf0]
008A055D  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
008A0561  E8 C2 52 98 FF                  call 0x140225828
008A0566  84 C0                           test al, al
008A0568  0F 84 CC F1 FF FF               je 0x14089f73a
008A056E  48 8B CA                        mov rcx, rdx
008A0571  E8 1A 7F B9 FF                  call 0x140438490
008A0576  E9 CB F1 FF FF                  jmp 0x14089f746
008A057B  B9 F8 00 00 00                  mov ecx, 0xf8
008A0580  66 3B C1                        cmp ax, cx
008A0583  0F 83 E2 EF FF FF               jae 0x14089f56b
008A0589  0F B7 C1                        movzx eax, cx
008A058C  E9 DA EF FF FF                  jmp 0x14089f56b
008A0591  45 38 66 44                     cmp byte ptr [r14 + 0x44], r12b
008A0595  0F 84 BB F8 FF FF               je 0x14089fe56
008A059B  44 39 25 7E 67 72 00            cmp dword ptr [rip + 0x72677e], r12d
008A05A2  74 0D                           je 0x1408a05b1
008A05A4  44 0F 20 C1                     mov rcx, cr8
008A05A8  41 0F B6 D5                     movzx edx, r13b
008A05AC  E8 E7 50 C5 FF                  call 0x1404f5698
008A05B1  41 0F B6 C5                     movzx eax, r13b
008A05B5  44 0F 22 C0                     mov cr8, rax
008A05B9  49 8D 8F 98 00 00 00            lea rcx, [r15 + 0x98]
008A05C0  49 8B D6                        mov rdx, r14
008A05C3  E8 30 43 1F 00                  call 0x140a948f8
008A05C8  E9 D7 F4 FF FF                  jmp 0x14089faa4
008A05CD  48 85 C0                        test rax, rax
008A05D0  0F 84 6F F9 FF FF               je 0x14089ff45
008A05D6  4C 8B C6                        mov r8, rsi
008A05D9  41 8B 56 38                     mov edx, dword ptr [r14 + 0x38]
008A05DD  48 8B C8                        mov rcx, rax
008A05E0  E8 FF 3D E6 FF                  call 0x1407043e4
008A05E5  44 0F B6 E8                     movzx r13d, al
008A05E9  E9 57 F9 FF FF                  jmp 0x14089ff45
008A05EE  33 D2                           xor edx, edx
008A05F0  49 8B 4E 18                     mov rcx, qword ptr [r14 + 0x18]
008A05F4  E8 77 22 2E 00                  call 0x140b82870
008A05F9  E9 39 E7 FF FF                  jmp 0x14089ed37
008A05FE  E8 4D 8D A5 FF                  call 0x1402f9350
008A0603  45 33 C0                        xor r8d, r8d
008A0606  33 D2                           xor edx, edx
008A0608  49 8B CE                        mov rcx, r14
008A060B  E8 60 03 9D FF                  call 0x140270970
008A0610  C7 47 10 22 00 00 C0            mov dword ptr [rdi + 0x10], 0xc0000022
008A0617  B8 22 00 00 C0                  mov eax, 0xc0000022
008A061C  E9 6E 02 00 00                  jmp 0x1408a088f
008A0621  49 8B CF                        mov rcx, r15
008A0624  E8 C7 BE AE FF                  call 0x14038c4f0
008A0629  45 33 C0                        xor r8d, r8d
008A062C  33 D2                           xor edx, edx
008A062E  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
008A0633  E8 38 03 9D FF                  call 0x140270970
008A0638  4C 8B AC 24 90 00 00 00         mov r13, qword ptr [rsp + 0x90]
008A0640  4D 85 ED                        test r13, r13
008A0643  74 08                           je 0x1408a064d
008A0645  49 8B CD                        mov rcx, r13
008A0648  E8 27 EE B9 FF                  call 0x14043f474
008A064D  49 8B CE                        mov rcx, r14
008A0650  E8 1B D9 9A FF                  call 0x14024df70
008A0655  B8 9A 00 00 C0                  mov eax, 0xc000009a
008A065A  E9 30 02 00 00                  jmp 0x1408a088f
008A065F  48 8B 9C 24 A0 00 00 00         mov rbx, qword ptr [rsp + 0xa0]
008A0667  66 44 39 63 58                  cmp word ptr [rbx + 0x58], r12w
008A066C  74 0B                           je 0x1408a0679
008A066E  33 D2                           xor edx, edx
008A0670  48 8B 4B 60                     mov rcx, qword ptr [rbx + 0x60]
008A0674  E8 F7 21 2E 00                  call 0x140b82870
008A0679  48 8B CB                        mov rcx, rbx
008A067C  E8 6F BE AE FF                  call 0x14038c4f0
008A0681  45 33 C0                        xor r8d, r8d
008A0684  33 D2                           xor edx, edx
008A0686  49 8B CF                        mov rcx, r15
008A0689  E8 E2 02 9D FF                  call 0x140270970
008A068E  4C 8B AC 24 90 00 00 00         mov r13, qword ptr [rsp + 0x90]
008A0696  4D 85 ED                        test r13, r13
008A0699  0F 84 8D F3 FF FF               je 0x14089fa2c
008A069F  49 8B CD                        mov rcx, r13
008A06A2  E9 80 F3 FF FF                  jmp 0x14089fa27
008A06A7  49 8B 8E A0 00 00 00            mov rcx, qword ptr [r14 + 0xa0]
008A06AE  48 85 C9                        test rcx, rcx
008A06B1  0F 84 37 F3 FF FF               je 0x14089f9ee
008A06B7  33 D2                           xor edx, edx
008A06B9  E8 B2 21 2E 00                  call 0x140b82870
008A06BE  4D 89 A6 A0 00 00 00            mov qword ptr [r14 + 0xa0], r12
008A06C5  4C 89 67 28                     mov qword ptr [rdi + 0x28], r12
008A06C9  E9 20 F3 FF FF                  jmp 0x14089f9ee
008A06CE  33 C0                           xor eax, eax
008A06D0  E9 CF F5 FF FF                  jmp 0x14089fca4
008A06D5  49 8B 4F 10                     mov rcx, qword ptr [r15 + 0x10]
008A06D9  4C 8B AC 24 90 00 00 00         mov r13, qword ptr [rsp + 0x90]
008A06E1  49 3B CD                        cmp rcx, r13
008A06E4  0F 84 8E E6 FF FF               je 0x14089ed78
008A06EA  48 85 C9                        test rcx, rcx
008A06ED  74 07                           je 0x1408a06f6
008A06EF  B2 01                           mov dl, 1
008A06F1  E8 2A 21 9D FF                  call 0x140272820
008A06F6  4D 85 ED                        test r13, r13
008A06F9  0F 84 79 E6 FF FF               je 0x14089ed78
008A06FF  49 8B CD                        mov rcx, r13
008A0702  E8 6D ED B9 FF                  call 0x14043f474
008A0707  E9 6C E6 FF FF                  jmp 0x14089ed78
008A070C  41 C6 45 00 13                  mov byte ptr [r13], 0x13
008A0711  E9 AA ED FF FF                  jmp 0x14089f4c0
008A0716  0F B6 D0                        movzx edx, al
008A0719  41 0F B6 CD                     movzx ecx, r13b
008A071D  E8 DA 4F C5 FF                  call 0x1404f56fc
008A0722  E9 02 F7 FF FF                  jmp 0x14089fe29
008A0727  4D 8B F4                        mov r14, r12
008A072A  E9 D5 E6 FF FF                  jmp 0x14089ee04
008A072F  49 8B CD                        mov rcx, r13
008A0732  E8 39 80 C0 FF                  call 0x1404a8770
008A0737  85 C0                           test eax, eax
008A0739  0F 84 06 E9 FF FF               je 0x14089f045
008A073F  49 8B CD                        mov rcx, r13
008A0742  E8 75 90 31 00                  call 0x140bb97bc
008A0747  4C 8B E8                        mov r13, rax
008A074A  E9 F9 E8 FF FF                  jmp 0x14089f048
008A074F  83 F9 24                        cmp ecx, 0x24
008A0752  0F 87 1B FD FF FF               ja 0x1408a0473
008A0758  48 0F A3 CA                     bt rdx, rcx
008A075C  0F 82 46 DF FF FF               jb 0x14089e6a8
008A0762  C7 47 10 78 02 00 C0            mov dword ptr [rdi + 0x10], 0xc0000278
008A0769  B8 78 02 00 C0                  mov eax, 0xc0000278
008A076E  E9 1C 01 00 00                  jmp 0x1408a088f
008A0773  3D 02 00 00 C0                  cmp eax, 0xc0000002
008A0778  0F 85 C6 E7 FF FF               jne 0x14089ef44
008A077E  E9 34 E9 FF FF                  jmp 0x14089f0b7
008A0783  0F 57 C0                        xorps xmm0, xmm0
008A0786  0F 11 84 24 68 01 00 00         movups xmmword ptr [rsp + 0x168], xmm0
008A078E  49 8B 86 C8 00 00 00            mov rax, qword ptr [r14 + 0xc8]
008A0795  0F 10 40 18                     movups xmm0, xmmword ptr [rax + 0x18]
008A0799  0F 11 84 24 68 01 00 00         movups xmmword ptr [rsp + 0x168], xmm0
008A07A1  48 8D 8C 24 68 01 00 00         lea rcx, [rsp + 0x168]
008A07A9  E8 92 5B BC FF                  call 0x140466340
008A07AE  48 8B F0                        mov rsi, rax
008A07B1  49 8B D6                        mov rdx, r14
008A07B4  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
008A07B9  E8 F2 AC 9F FF                  call 0x14029b4b0
008A07BE  44 8B E8                        mov r13d, eax
008A07C1  48 8B CE                        mov rcx, rsi
008A07C4  E8 77 5B BC FF                  call 0x140466340
008A07C9  E9 A4 EC FF FF                  jmp 0x14089f472
008A07CE  4C 8B AC 24 D8 00 00 00         mov r13, qword ptr [rsp + 0xd8]
008A07D6  48 8B B4 24 80 00 00 00         mov rsi, qword ptr [rsp + 0x80]
008A07DE  4C 8B B4 24 08 01 00 00         mov r14, qword ptr [rsp + 0x108]
008A07E6  4C 8B BC 24 20 01 00 00         mov r15, qword ptr [rsp + 0x120]
008A07EE  E9 46 DE FF FF                  jmp 0x14089e639
008A07F3  49 8B CD                        mov rcx, r13
008A07F6  E8 85 71 13 00                  call 0x1409d7980
008A07FB  48 8B 8C 24 C8 00 00 00         mov rcx, qword ptr [rsp + 0xc8]
008A0803  E8 78 55 BD FF                  call 0x140475d80
008A0808  E9 9C F8 FF FF                  jmp 0x1408a00a9
008A080D  B8 38 00 00 00                  mov eax, 0x38
008A0812  E9 54 ED FF FF                  jmp 0x14089f56b
008A0817  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
008A081C  4C 8B 8C 24 B0 00 00 00         mov r9, qword ptr [rsp + 0xb0]
008A0824  4C 8B 44 24 78                  mov r8, qword ptr [rsp + 0x78]
008A0829  48 8B D6                        mov rdx, rsi
008A082C  B9 F9 00 00 00                  mov ecx, 0xf9
008A0831  E8 2A CE C5 FF                  call 0x1404fd660
008A0836  CC                              int3
008A0837  49 8B CE                        mov rcx, r14
008A083A  E8 31 D7 9A FF                  call 0x14024df70
008A083F  45 33 C0                        xor r8d, r8d
008A0842  33 D2                           xor edx, edx
008A0844  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
008A0849  E8 22 01 9D FF                  call 0x140270970
008A084E  4C 8B AC 24 90 00 00 00         mov r13, qword ptr [rsp + 0x90]
008A0856  4D 85 ED                        test r13, r13
008A0859  0F 84 07 E9 FF FF               je 0x14089f166
008A085F  49 8B CD                        mov rcx, r13
008A0862  E9 C0 F2 FF FF                  jmp 0x14089fb27
008A0867  49 8B CD                        mov rcx, r13
008A086A  E8 05 EC B9 FF                  call 0x14043f474
008A086F  E9 23 F1 FF FF                  jmp 0x14089f997
008A0874  C7 47 20 51 02 AA BE            mov dword ptr [rdi + 0x20], 0xbeaa0251
008A087B  4C 89 7F 28                     mov qword ptr [rdi + 0x28], r15
008A087F  44 89 67 10                     mov dword ptr [rdi + 0x10], r12d
008A0883  49 8B CF                        mov rcx, r15
008A0886  E8 95 F1 96 FF                  call 0x14020fa20
008A088B  33 C0                           xor eax, eax
008A088D  EB 00                           jmp 0x1408a088f
008A088F  48 8B 8C 24 78 01 00 00         mov rcx, qword ptr [rsp + 0x178]
008A0897  48 33 CC                        xor rcx, rsp
008A089A  E8 A1 BD E0 FF                  call 0x1406ac640
008A089F  4C 8D 9C 24 80 01 00 00         lea r11, [rsp + 0x180]
008A08A7  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
008A08AB  49 8B 73 48                     mov rsi, qword ptr [r11 + 0x48]
008A08AF  49 8B E3                        mov rsp, r11
008A08B2  41 5F                           pop r15
008A08B4  41 5E                           pop r14
008A08B6  41 5D                           pop r13
008A08B8  41 5C                           pop r12
008A08BA  5F                              pop rdi
008A08BB  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IopParseDevice(__int64 a1, __int64 a2, __int64 a3, unsigned __int8 a4, unsigned __int8 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m11C;
    unsigned __int8 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int8 v_stack_m140;
    unsigned int v_stack_m144;
    unsigned __int8 v_stack_m148;
    unsigned __int8 v_stack_m158;
    unsigned __int64 v_stack_m160;
    unsigned __int64 v_stack_m168;
    unsigned __int8 v_stack_m170;
    unsigned __int64 v_stack_m178;
    unsigned __int64 v_stack_m180;
    unsigned int v_stack_m188;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_m5C;
    unsigned int v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned int v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD4;
    unsigned __int8 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned int v_stack_mF0;
    unsigned __int64 v_stack_mF8;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 32) = v_rsi;
    v_rsp = (v_rsp) - (384);
    result = (*(unsigned __int64 *)(v_rip + 5685774)) ^ (v_rsp);
    v_stack_m30 = result;
    v_stack_m140 = a4;
    v_stack_mD0 = a3;
    v_stack_m88 = a1;
    v_stack_mF8 = a6;
    v_stack_m128 = a7;
    v_stack_m48 = a8;
    v_stack_mB8 = a10;
    v_stack_mA0 = a11;
    v_r12 = 0;
    *(unsigned int *)(v_rsp - 284) = 0;
    v_stack_m144 = 0;
    v_stack_m98 = v_xmm0;
    result = 0;
    *(unsigned __int64 *)(v_rsp - 112) = v_xmm1;
    *(unsigned __int64 *)(v_rsp - 96) = 0;
    v_stack_mB0 = 0;
    v_stack_m120 = 0;
    *(unsigned int *)(v_rsp - 212) = 0;
    *(unsigned __int64 *)(v_rsp - 128) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 272) = 0;
    v_stack_mC0 = 0;
    v_stack_mE8 = 0;
    *(unsigned __int64 *)(v_rsp - 200) = 0;
    if (a2 != (*(unsigned __int64 *)(v_rip + 7505104))) goto loc_0089EC6D;
    v_stack_m100 = *(unsigned __int64 *)(gs_base + (0 + 392));
    result = RtlInitUnicodeString(v_rsp - 128, v_rip + 2483584, a3, a4);
loc_0089E639:
    *(unsigned __int64 *)(a11) = 0;
    v_stack_m108 = 0;
    if (a8 == 0) goto loc_0089EC6D;
    if ((*(unsigned __int16 *)(a8)) != 8) goto loc_0089EC6D;
    if ((*(unsigned __int16 *)(a8 + 2)) != 224) goto loc_0089EC6D;
    v_stack_m138 = a1;
    if ((*(unsigned int *)(a8 + 32)) == 1) goto loc_008A0874;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a8 + 152)))) & (16)) != 0) goto loc_008A0108;
loc_0089E6A8:
    if (*(unsigned __int64 *)(a8 + 40) != 0) goto loc_0089E9FD;
loc_0089E6B5:
    if ((*(unsigned int *)(a1 + 72)) != 7) goto loc_0089E6EE;
    v_stack_m130 = a1;
loc_0089E6D0:
    if ((*(unsigned __int64 *)(a1 + 56)) == 0) goto loc_008A00DF;
loc_0089E6E0:
    if (a1 == 0) goto loc_0089E6EE;
    if (a1 != a1) goto loc_0089EC3F;
loc_0089E6EE:
    result = IopCheckDeviceAndDriver(a8, a1, a1, a1);
    v_stack_m144 = (unsigned int)(result);
    if (sign_flag) goto loc_0089F16A;
    if (((*(unsigned int *)(*(unsigned __int64 *)(a1 + 312) + 32)) & (0x400ULL)) != 0) goto loc_008A01F8;
loc_0089E719:
    result = (unsigned int)(*(unsigned int *)(a3 + 16));
    if (sign_flag) {
        result = (unsigned int)(((unsigned int)(*(unsigned int *)(a3 + 16))) | (*(unsigned int *)(*(unsigned __int64 *)(v_rip + 7504832) + 76)));
    }
    if (!(condition_is_above_or_equal)) {
        result = (unsigned int)((result) | (*(unsigned int *)(*(unsigned __int64 *)(v_rip + 7504832) + 80)));
    }
    if (!(condition_is_above_or_equal)) {
        result = (unsigned int)((result) | (*(unsigned int *)(*(unsigned __int64 *)(v_rip + 7504832) + 84)));
    }
    if (!(condition_is_above_or_equal)) {
        result = (unsigned int)((result) | (*(unsigned int *)(*(unsigned __int64 *)(v_rip + 7504832) + 88)));
    }
    result = (unsigned int)((result) & (0xFFFFFFFULL));
    *(unsigned int *)(a3 + 16) = (unsigned int)(result);
    result = (unsigned int)(*(unsigned int *)(a3 + 24));
    if (sign_flag) {
        result = (unsigned int)(((unsigned int)(*(unsigned int *)(a3 + 24))) | (*(unsigned int *)(*(unsigned __int64 *)(v_rip + 7504778) + 76)));
    }
    if (!(condition_is_above_or_equal)) {
        result = (unsigned int)((result) | (*(unsigned int *)(*(unsigned __int64 *)(v_rip + 7504778) + 80)));
    }
    if (!(condition_is_above_or_equal)) {
        result = (unsigned int)((result) | (*(unsigned int *)(*(unsigned __int64 *)(v_rip + 7504778) + 84)));
    }
    if (!(condition_is_above_or_equal)) {
        result = (unsigned int)((result) | (*(unsigned int *)(*(unsigned __int64 *)(v_rip + 7504778) + 88)));
    }
    result = (unsigned int)((result) & (0xFFFFFFFULL));
    *(unsigned int *)(a3 + 24) = (unsigned int)(result);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 72) + 8) = v_xmm0;
    v_stack_mF0 = (unsigned int)((unsigned int)(*(unsigned int *)(a3 + 16)));
    if (v_stack_m140 == 0) goto loc_0089EA1B;
loc_0089E7AF:
loc_0089E7B2:
    result = IopCheckBackupRestorePrivilege(a3, a8 + 64, 1, (unsigned int)(*(unsigned int *)(a8 + 88)));
    if ((*(unsigned __int8 *)(a8 + 136)) != 0) goto loc_0089E9DA;
loc_0089E7CF:
    if (((*(unsigned int *)(a3 + 12)) & (256)) != 0) goto loc_0089E9E4;
loc_0089E7DD:
    if (*(unsigned __int64 *)(a8 + 40) != 0) goto loc_0089EBAD;
loc_0089E7F1:
    if ((unsigned __int8)(v_stack_m140) == 0) goto loc_0089EA0B;
loc_0089E800:
    if (*(unsigned __int64 *)(a8 + 40) != 0) goto loc_0089F119;
loc_0089E809:
    if ((*(unsigned __int8 *)(a8 + 136)) != 0) goto loc_0089E883;
    v_rbx = (unsigned __int8)((4) & (223));
    if ((*(unsigned __int16 *)(a7)) == 0) goto loc_0089EA5D;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 52))) & (0x20100ULL));
    if (((unsigned int)(result)) == 0x20000ULL) goto loc_0089E857;
    if ((unsigned __int8)(v_stack_m140) == 0) goto loc_0089E857;
    v_stack_m148 = 0;
    result = SeIsAppContainerOrIdentifyLevelContext(a3 + 32, v_stack_m148, 1, v_stack_m140);
    if (v_stack_m148 != 0) goto loc_0089FFFA;
loc_0089E857:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a3 + 12)))) & (1)) == 0) goto loc_008A0331;
    v_rbx = (unsigned __int8)((v_rbx) | (1));
loc_0089E866:
    result = (unsigned int)(*(unsigned int *)(a3 + 12));
    if ((((unsigned __int8)(v_rbx)) & (32)) != 0) {
        a1 = a3 + 32;
        result = SeUnlockSubjectContext(a1, v_stack_m148, 1, v_stack_m140);
    }
    if ((((unsigned __int8)(v_rbx)) & (1)) == 0) goto loc_0089E9BC;
loc_0089E883:
    if ((*(unsigned __int8 *)(a8 + 137)) != 0) goto loc_0089E9D3;
    if ((*(unsigned __int8 *)(a8 + 138)) != 0) goto loc_0089E9D3;
    result = 0;
loc_0089E89F:
    v_rbx = (unsigned __int8)((v_rbx) & (191));
    v_rbx = (unsigned __int8)((v_rbx) | (0));
    if ((*(unsigned __int16 *)(v_stack_m128)) == 0) goto loc_0089EA2E;
loc_0089E8B6:
    v_rbx = (unsigned __int8)((v_rbx) & (247));
loc_0089E8B9:
    v_stack_m118 = 0;
    if (*(unsigned __int64 *)(a8 + 40) != 0) goto loc_0089EBD5;
loc_0089E8D1:
    v_stack_m130 = v_stack_m138;
    if ((*(unsigned __int64 *)(v_stack_m138 + 56)) == 0) goto loc_0089E925;
    if ((((unsigned __int8)(v_rbx)) & (8)) != 0) goto loc_0089E925;
    if (((*(unsigned int *)(v_stack_m138 + 52)) & (256)) != 0) goto loc_0089FD59;
loc_0089E8F5:
    result = IopCheckVpbMounted(a8, v_stack_m138, v_stack_m128, v_stack_m144);
    v_stack_m118 = result;
    if (result == 0) goto loc_0089FAF3;
    v_stack_m130 = *(unsigned __int64 *)(result + 8);
loc_0089E925:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a8 + 152)))) & (1)) != 0) goto loc_0089E9F5;
    result = (unsigned int)(*(unsigned int *)(a8 + 152));
    v_rsi = *(unsigned __int64 *)(result + 8);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8) + 24)) != 0) {
        a1 = *(unsigned __int64 *)(result + 8);
        result = IoGetAttachedDevice(a1, v_stack_m138, v_stack_m128, v_stack_m144);
        v_rsi = result;
        v_stack_m130 = result;
    }
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m138 + 52)))) & (0x40001ULL)) == 0) goto loc_0089F182;
    a1 = (((*(unsigned int *)(v_stack_m138 + 48)) & (0x600100ULL)) == 0) ? 1 : 0;
    result = (condition_is_above_or_equal) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) == 0) goto loc_0089F182;
    v_stack_m148 = 0;
    a1 = (v_stack_mD0) + (32);
    result = SeIsAppContainerOrIdentifyLevelContext(a1, v_stack_m148, v_stack_m128, v_stack_m144);
    if (v_stack_m148 == 0) goto loc_0089F182;
    if (result == 0) goto loc_0089E9BC;
    if (((*(unsigned int *)(*(unsigned __int64 *)(result + 8) + 48)) & (0x20000ULL)) != 0) goto loc_0089F182;
    result = *(unsigned __int64 *)(result + 8);
    if (result != 0) {
        a1 = result;
        result = IopDereferenceVpbAndFree(a1, v_stack_m148, v_stack_m128, v_stack_m144);
    }
    a3 = 0;
    a2 = 0;
    result = IopDecrementDeviceObjectRef(v_stack_m138, a2, a3, v_stack_m144);
    goto loc_008A088F;
loc_0089E9D3:
    goto loc_0089E89F;
loc_0089E9DA:
    if ((*(unsigned __int16 *)(v_rsi)) != 0) goto loc_0089E7CF;
loc_0089E9E4:
    v_r15 = (unsigned int)(((unsigned int)(*(unsigned int *)(a3 + 16))) | (*(unsigned int *)(result + 20)));
    v_stack_mF0 = (unsigned int)(v_r15);
    goto loc_0089E7DD;
loc_0089E9F5:
    v_rbx = (unsigned __int8)((v_rbx) | (2));
    goto loc_0089E949;
loc_0089E9FD:
    v_stack_m138 = *(unsigned __int64 *)(64 + 8);
    goto loc_0089E6B5;
loc_0089EA0B:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a8 + 84)))) & (1)) == 0) goto loc_0089E883;
    goto loc_0089E800;
loc_0089EA1B:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a8 + 84)))) & (1)) != 0) goto loc_0089E7AF;
    a3 = 0;
    goto loc_0089E7B2;
loc_0089EA2E:
    if ((*(unsigned __int64 *)(a8 + 40)) != 0) goto loc_0089E8B6;
    a1 = ((((unsigned int)(v_r15)) & (0xFEE1FF7FULL)) == 0) ? 1 : 0;
    result = (unsigned __int8)(((unsigned __int8)(v_rbx)) >> (6));
    result = (unsigned __int8)(~(result));
    a1 = (unsigned __int8)((a1) & ((unsigned __int8)(result)));
    if ((((unsigned __int8)(a1)) & (1)) == 0) goto loc_0089E8B6;
    v_rbx = (unsigned __int8)((v_rbx) | (8));
    goto loc_0089E8B9;
loc_0089EA5D:
    if ((((unsigned int)(result)) & (0x40001ULL)) == 0) goto loc_0089EA71;
    if ((((unsigned int)(v_r15)) & (0xFFEDFF7FULL)) != 0) goto loc_008A02CA;
loc_0089EA71:
    v_r14 = 0;
loc_0089EA74:
    v_stack_m110 = 0;
    result = ExAcquireResourceSharedLite(v_rip + 7268363, 1, a3, v_stack_m144);
    result = SeLockSubjectContext(result + 32, 1, a3, v_stack_m144);
    v_rbx = (unsigned __int8)((v_rbx) | (32));
    if (0 != 0) goto loc_008A0484;
loc_0089EAAF:
    result = (*(unsigned __int64 *)(v_rip + 7503914)) + (76);
    a3 = (unsigned __int8)(((unsigned __int8)(v_rbx)) >> (5));
    a3 = (unsigned __int8)((a3) & (1));
    v_stack_m160 = v_stack_m144;
    v_stack_m168 = v_stack_m11C;
    v_stack_m170 = 1;
    v_stack_m178 = result;
    v_stack_m180 = v_stack_m110;
    v_stack_m188 = 0;
    result = SeAccessCheck(*(unsigned __int64 *)(v_stack_m138 + 272), result + 32, a3, (unsigned int)((unsigned int)(v_r15)));
    result = (unsigned __int8)((result) ^ ((unsigned __int8)(v_rbx)));
    result = (unsigned __int8)((result) & (1));
    v_rbx = (unsigned __int8)((v_rbx) ^ ((unsigned __int8)(result)));
    if (v_stack_m110 != 0) goto loc_0089EC53;
loc_0089EB28:
    if ((((unsigned __int8)(v_rbx)) & (1)) != 0) {
        result = v_stack_m11C;
        result = (unsigned int)(~(result));
        *(unsigned __int8 *)(a8 + 136) = 1;
    }
    a1 = (unsigned __int8)(((unsigned __int8)(v_rbx)) & (1));
    v_stack_m160 = result + 10;
    v_stack_m168 = 0;
    v_stack_m170 = 1;
    v_stack_m178 = (unsigned __int8)(a1);
    v_stack_m180 = 0;
    v_stack_m188 = result;
    result = SeOpenObjectAuditAlarmWithTransaction(v_stack_m80, v_stack_m138, v_stack_mF8, *(unsigned __int64 *)(v_stack_m138 + 272));
loc_0089EB8F:
    result = ExReleaseResourceLite(v_rip + 7268106, v_stack_m138, v_stack_mF8, *(unsigned __int64 *)(v_stack_m138 + 272));
    result = KeLeaveCriticalRegionThread(v_stack_m100, v_stack_m138, v_stack_mF8, *(unsigned __int64 *)(v_stack_m138 + 272));
    goto loc_0089E866;
loc_0089EBAD:
    if (((*(unsigned int *)(v_stack_m100 + 80)) & (0x400000ULL)) == 0) goto loc_0089E7F1;
    a2 = (unsigned __int8)(v_stack_m138);
    if ((*(unsigned __int16 *)(v_rsi)) == 0) { a2 = 1; }
    v_stack_m120 = (unsigned int)(a2);
    goto loc_0089E7F1;
loc_0089EBD5:
    if (((*(unsigned int *)(a2 + 80)) & (0x800ULL)) != 0) goto loc_0089E8D1;
    v_stack_m130 = v_stack_m88;
    if (*(unsigned __int64 *)(a2 + 16) == 0) goto loc_0089EC1B;
    v_stack_m118 = *(unsigned __int64 *)(a2 + 16);
    if (((*(unsigned int *)(v_stack_m138 + 52)) & (256)) != 0) goto loc_008A04B3;
loc_0089EC11:
    result = IopIncrementVpbRefCount(*(unsigned __int64 *)(a2 + 16), 1, v_stack_mF8, *(unsigned __int64 *)(v_stack_m138 + 272));
loc_0089EC1B:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a8 + 152)))) & (1)) == 0) goto loc_0089E949;
    v_rsi = v_stack_m88;
    if (*(unsigned __int64 *)(a2 + 16) != 0) {
        v_rsi = *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 16) + 8);
        v_stack_m130 = v_rsi;
    }
    v_rbx = (unsigned __int8)((v_rbx) | (2));
    goto loc_0089E949;
loc_0089EC3F:
    v_stack_m138 = a1;
    goto loc_0089E6EE;
loc_0089EC53:
    result = SeAppendPrivileges(*(unsigned __int64 *)(a2 + 16), 1, v_stack_mF8, *(unsigned __int64 *)(v_stack_m138 + 272));
    result = CmSiFreeMemory(v_stack_m110, 1, v_stack_mF8, *(unsigned __int64 *)(v_stack_m138 + 272));
    goto loc_0089EB28;
loc_0089EC6D:
    goto loc_008A088F;
loc_0089EC77:
    v_stack_mE8 = *(unsigned __int64 *)(a1 + 112);
loc_0089EC83:
    result = (unsigned int)(0xC000000DULL);
    if ((unsigned int)(v_stack_m110) != 0) { result = 0; }
    v_stack_m144 = (unsigned int)(result);
    v_rsi = (unsigned int)(((unsigned int)(*(unsigned int *)(a8 + 84))) & (8));
    v_r13 = (condition_is_not_equal) ? 1 : 0;
    if ((*(unsigned int *)(a1 + 48)) == 260) goto loc_0089FE81;
loc_0089ECAA:
    if ((*(unsigned int *)(a1 + 48)) != 0) goto loc_0089ECDA;
    if ((*(unsigned int *)(a8 + 120)) != 0) goto loc_0089ECDA;
    result = IopSymlinkPropagateToExtensionIfNeeded(v_r15, v_stack_mE8, v_stack_mF8, *(unsigned __int64 *)(v_stack_m138 + 272));
    v_stack_m144 = (unsigned int)(result);
    if (sign_flag) goto loc_0089F0C4;
loc_0089ECDA:
    if (v_stack_mE8 != 0) {
        *(unsigned __int64 *)(a8 + 168) = v_stack_mE8;
    }
    v_stack_m98 = v_xmm0;
    v_stack_m144 = v_xmm0;
    *(unsigned int *)(v_r15 + 156) = 1;
    result = v_stack_mE8;
    if ((((unsigned __int8)(v_rbx)) & (4)) != 0) {
        result = v_stack_m100;
        *(unsigned __int64 *)(a1 + 152) = result;
        a1 = a1;
        result = IopDequeueIrpFromThread(a1, v_stack_mE8, v_stack_mF8, *(unsigned __int64 *)(v_stack_m138 + 272));
    }
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 16))) & (48));
    if (((unsigned __int8)(result)) == 48) goto loc_008A05EE;
loc_0089ED37:
    result = IoFreeIrp(a1, v_stack_mE8, v_stack_mF8, *(unsigned __int64 *)(v_stack_m138 + 272));
    *(unsigned __int64 *)(a8 + 24) = v_stack_m90;
    if (sign_flag) goto loc_0089EF78;
    if (((unsigned int)((unsigned int)(v_stack_m144))) == 260) goto loc_0089FB31;
    result = IoGetRelatedDeviceObject(v_r15, v_stack_mE8, v_stack_mF8, *(unsigned __int64 *)(v_stack_m138 + 272));
    if (v_stack_m130 != result) goto loc_008A06D5;
loc_0089ED78:
    if ((((unsigned __int8)(v_rbx)) & (64)) != 0) goto loc_0089EDBF;
    *(unsigned __int64 *)(v_stack_mA0) = v_r15;
    *(unsigned int *)(a8 + 32) = 0xBEAA0251ULL;
    result = ObfReferenceObject(v_r15, v_stack_mE8, v_stack_mF8, *(unsigned __int64 *)(v_stack_m138 + 272));
    if (*(unsigned __int64 *)(v_r15 + 64) != 0) goto loc_0089EFC2;
loc_0089EDA4:
    if ((*(unsigned __int16 *)(v_r15 + 88)) == 0) goto loc_0089EF9A;
loc_0089EDAF:
    *(unsigned int *)(a8 + 16) = (unsigned int)((unsigned int)(v_stack_m98));
    goto loc_008A088F;
loc_0089EDBF:
    if ((*(unsigned __int8 *)(a8 + 137)) == 0) goto loc_0089EF44;
    if ((*(unsigned __int8 *)(a8 + 208)) != 0) goto loc_0089F0E2;
    v_rbx = 0;
    if ((*(unsigned __int8 *)(a8 + 139)) != 0) goto loc_0089F024;
    v_stack_mC8 = 0;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8) + 80) == 0) goto loc_008A0727;
loc_0089EE04:
    v_stack_mA0 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8) + 80) + 32);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8) + 80) + 32) == 0) goto loc_0089EE57;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 6708233)))) & (16)) != 0) goto loc_0089EEED;
loc_0089EE1F:
loc_0089EE22:
    v_stack_m50 = 0;
    v_stack_m188 = result;
    result = guard_dispatch_icall(v_r15, 1, *(unsigned __int64 *)(a8 + 96), v_stack_m98);
    v_stack_mD8 = (unsigned __int8)(result);
    if (0 != 0) goto loc_0089EE6B;
loc_0089EE57:
    if ((unsigned __int8)((unsigned __int8)(result)) == 0) goto loc_0089EE78;
    v_stack_m144 = (unsigned int)((unsigned int)(v_stack_m98));
    goto loc_0089EF15;
loc_0089EE6B:
    result = VfFastIoCheckState(0, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8) + 80) + 32), *(unsigned __int64 *)(a8 + 96), v_stack_m98);
    goto loc_0089EE57;
loc_0089EE78:
    result = ExAllocatePool2(40 + 24, 40, (unsigned int)(0x20206F49ULL), v_stack_m98);
    v_stack_mC8 = result;
    if (result == 0) goto loc_0089EF0D;
    v_stack_m178 = 1;
    v_stack_m180 = v_stack_mD4;
    v_stack_m188 = result;
    a4 = 0;
    result = IopQueryXxxInformation(v_r15, a4 + 4, a4 + 40, a4);
    v_stack_m144 = (unsigned int)(result);
    if (!(sign_flag)) {
        a3 = v_stack_mD4;
        a2 = result;
        a1 = *(unsigned __int64 *)(a8 + 96);
        result = memcpy(a1, a2, a3, a4);
    }
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, a3, a4);
    goto loc_0089EF15;
loc_0089EEED:
    result = MmIsDriverVerifying(0, a2, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_0089EE1F;
    result = VfFastIoSnapState(0, a2, a3, a4);
    goto loc_0089EE22;
loc_0089EF0D:
    v_stack_m144 = 0xC000009AULL;
loc_0089EF15:
    goto loc_0089EF44;
loc_0089EF44:
    *(unsigned int *)(a8 + 32) = 0xBEAA0251ULL;
    a1 = 0;
    result = IopCloseFile(a1, v_r15, 1, 1);
    result = ObfDereferenceObject(v_r15, v_r15, 1, 1);
    *(unsigned __int64 *)(a8 + 8) = 0;
    *(unsigned int *)(a8 + 16) = (unsigned int)((unsigned int)(v_stack_m144));
    goto loc_008A088F;
loc_0089EF78:
    if (((*(unsigned int *)(v_r15 + 80)) & (0x200000ULL)) == 0) goto loc_0089EFD4;
    result = ObfDereferenceObject(v_r15, v_r15, 1, 1);
loc_0089EF8A:
    *(unsigned __int64 *)(a8 + 8) = 0;
    *(unsigned int *)(a8 + 16) = (unsigned int)((unsigned int)(v_stack_m144));
    goto loc_008A088F;
loc_0089EF9A:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 72))) - (3));
    if (condition_is_equal) goto loc_0089EFB5;
    a1 = (unsigned int)((a1) - (5));
    if (condition_is_equal) goto loc_0089EFB5;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0089EFB5;
    if (((unsigned int)(a1)) != 23) goto loc_0089EDAF;
loc_0089EFB5:
    goto loc_0089EDAF;
loc_0089EFC2:
    if (((*(unsigned int *)((unsigned int)(v_stack_m144) + 80)) & (0x400000ULL)) == 0) goto loc_0089EDAF;
    goto loc_0089EDA4;
loc_0089EFD4:
    result = (unsigned int)(v_stack_m144);
    if ((*(unsigned __int16 *)(v_r15 + 88)) != 0) {
        a2 = 0;
        a1 = *(unsigned __int64 *)(v_r15 + 96);
        result = ExFreePoolWithTag(a1, a2, 1, 1);
        *(unsigned __int16 *)(v_r15 + 88) = 0;
    }
    *(unsigned __int64 *)(v_r15 + 8) = 0;
    result = ObfDereferenceObject(v_r15, a2, 1, 1);
    a3 = 0;
    a2 = 0;
    result = IopDecrementDeviceObjectRef(v_stack_m138, a2, a3, 1);
    if (v_stack_m118 == 0) goto loc_0089EF8A;
    result = IopDereferenceVpbAndFree(v_stack_m118, a2, a3, 1);
    goto loc_0089EF8A;
loc_0089F024:
    if (result == 0) goto loc_0089F072;
    if ((*(unsigned int *)(result)) <= 112) goto loc_0089F072;
    if (*(unsigned __int64 *)(result + 112) == 0) goto loc_0089F072;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 6707683)))) & (16)) != 0) goto loc_008A072F;
loc_0089F045:
loc_0089F048:
    v_stack_m188 = result;
    result = guard_dispatch_icall(v_r15, 1, *(unsigned __int64 *)(a8 + 104), v_stack_m98);
    if (0 != 0) goto loc_0089F172;
loc_0089F072:
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) goto loc_0089EF44;
    v_stack_m178 = 1;
    v_stack_m180 = v_stack_mD4;
    v_stack_m188 = *(unsigned __int64 *)(a8 + 104);
    a4 = 0;
    result = IopQueryXxxInformation(v_r15, a4 + 34, a4 + 56, a4);
    v_stack_m144 = (unsigned int)(result);
    if (((unsigned int)(result)) != 0xC000000DULL) goto loc_008A0773;
loc_0089F0B7:
    result = IopGetNetworkOpenInformation(v_r15, a8, a4 + 56, a4);
    goto loc_0089F110;
loc_0089F0C4:
    result = IoCancelFileOpen(v_stack_m130, v_r15, a4 + 56, a4);
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 112) + 56) = 0;
    *(unsigned int *)(*(unsigned __int64 *)(result + 112) + 48) = (unsigned int)((unsigned int)(v_stack_m144));
    goto loc_0089ECDA;
loc_0089F0E2:
    v_stack_m178 = 1;
    v_stack_m180 = a8 + 204;
    v_stack_m188 = *(unsigned __int64 *)(a8 + 112);
    a4 = 0;
    result = IopQueryXxxInformation(v_r15, (unsigned int)(*(unsigned int *)(a8 + 200)), (unsigned int)(*(unsigned int *)(a8 + 204)), a4);
loc_0089F110:
    v_stack_m144 = (unsigned int)(result);
    goto loc_0089EF44;
loc_0089F119:
    if ((unsigned __int8)((unsigned int)(*(unsigned int *)(a8 + 200))) != 0) goto loc_0089E809;
    goto loc_0089E883;
loc_0089F126:
    result = IoFreeIrp(*(unsigned __int64 *)(result + 112), (unsigned int)(*(unsigned int *)(a8 + 200)), (unsigned int)(*(unsigned int *)(a8 + 204)), a4);
    a3 = 0;
    a2 = 0;
    result = IopDecrementDeviceObjectRef(v_r15, a2, a3, a4);
    result = v_stack_m118;
    if (v_stack_m118 != 0) {
        a1 = v_stack_m118;
        result = IopDereferenceVpbAndFree(a1, a2, a3, a4);
    }
    if (v_stack_m108 != 0) {
        *(unsigned __int64 *)(v_stack_m108 + 8) = 0;
        result = ObfDereferenceObject(v_stack_m108, a2, a3, a4);
    }
loc_0089F16A:
    *(unsigned int *)(a8 + 16) = (unsigned int)((unsigned int)(v_stack_m144));
    goto loc_008A088F;
loc_0089F172:
    result = VfFastIoCheckState(0, *(unsigned __int64 *)(result + 112), a3, a4);
    goto loc_0089F072;
loc_0089F182:
    if ((((unsigned __int8)((unsigned __int8)(result))) & (2)) != 0) goto loc_0089F8B2;
loc_0089F18B:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a8 + 152)))) & (16)) != 0) goto loc_0089F9BB;
loc_0089F199:
    if (((*(unsigned int *)(result + 52)) & (256)) != 0) goto loc_0089F7EB;
    if ((*(unsigned int *)(v_rip + 5683231)) == 0) goto loc_0089F1BD;
    if (((*(unsigned int *)(*(unsigned __int64 *)(result + 112) + 52)) & (0x100000ULL)) != 0) goto loc_0089F7EB;
loc_0089F1BD:
    a3 = 0;
    result = IopAllocateIrpExReturn(result, *(unsigned __int8 *)(result + 76), a3, a4);
    if (result == 0) goto loc_0089F97F;
    *(unsigned __int64 *)(result + 152) = v_stack_m100;
    *(unsigned __int8 *)(result + 64) = (unsigned __int8)(v_stack_m140);
    *(unsigned int *)(result + 16) = 0x884ULL;
    v_stack_m70 = a9;
    v_stack_m68 = v_stack_mD0;
    v_stack_m60 = (unsigned int)(v_r15);
    v_stack_m5C = (unsigned int)((unsigned int)(*(unsigned int *)(a8 + 64)));
    v_r13 = (*(unsigned __int64 *)(result + 184)) - (72);
    v_stack_m58 = v_r13;
    *(unsigned __int8 *)(v_r13 + 3) = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a8 + 120))) != 0) goto loc_0089F4B3;
    *(unsigned __int8 *)(v_r13) = 0;
    *(unsigned int *)(v_r13 + 32) = (unsigned int)((unsigned int)(*(unsigned int *)(a8 + 80)));
    *(unsigned __int8 *)(v_r13 + 2) = (unsigned __int8)(*(unsigned __int8 *)(a8 + 84));
    if (((a5) & (64)) == 0) goto loc_0089FA3D;
loc_0089F26D:
    *(unsigned __int64 *)(result + 88) = *(unsigned __int64 *)(a8 + 56);
    *(unsigned __int64 *)(result + 24) = *(unsigned __int64 *)(a8 + 72);
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a8 + 88))) << (24));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a8 + 64))) & (0xFFFFFFULL));
    a1 = (unsigned int)((a1) | ((unsigned int)(result)));
    *(unsigned int *)(v_r13 + 16) = (unsigned int)(a1);
    *(unsigned __int16 *)(v_r13 + 24) = (unsigned __int16)(*(unsigned __int16 *)(a8 + 68));
    *(unsigned __int16 *)(v_r13 + 26) = (unsigned __int16)(*(unsigned __int16 *)(a8 + 70));
    *(unsigned __int64 *)(v_r13 + 8) = v_stack_m70;
    *(unsigned __int64 *)(result + 112) = *(unsigned __int64 *)(a8 + 168);
    *(unsigned __int64 *)(result + 72) = v_stack_m98;
    *(unsigned __int64 *)(result + 8) = 0;
    *(unsigned __int8 *)(result + 65) = 0;
    *(unsigned __int8 *)(result + 68) = 0;
    *(unsigned __int64 *)(result + 80) = 0;
    *(unsigned __int64 *)(result + 104) = 0;
    *(unsigned __int64 *)(result + 160) = 0;
    if ((*(unsigned __int8 *)(a8 + 137)) != 0) goto loc_0089F610;
    v_stack_m168 = (unsigned int)(v_r15);
    v_stack_m170 = 0;
    v_stack_m178 = v_stack_mB8;
    v_stack_m180 = a8;
    v_stack_m188 = (unsigned __int8)(v_stack_m140);
    result = IopAllocRealFileObject(v_stack_m108, result, v_stack_m138, (unsigned int)(a5));
    v_stack_m144 = (unsigned int)(result);
    if (sign_flag) goto loc_0089F126;
loc_0089F342:
    if ((((unsigned __int8)((unsigned __int8)(result))) & (8)) != 0) {
    }
    if ((((unsigned __int8)(*(unsigned __int64 *)(a8 + 216))) & (1)) != 0) goto loc_0089F4A1;
    if ((((unsigned __int8)(*(unsigned __int64 *)(a8 + 216))) & (2)) != 0) goto loc_0089F9C9;
loc_0089F366:
    *(unsigned __int64 *)(result + 192) = v_stack_m108;
    *(unsigned __int64 *)(v_r13 + 48) = v_stack_m108;
    if ((unsigned __int16)(*(unsigned __int16 *)(v_stack_m128)) == 0) goto loc_0089F3CA;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_stack_m128))) < 56) goto loc_0089F7E1;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_stack_m128))) < 120) goto loc_0089F3A0;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_stack_m128))) >= 248) goto loc_0089F3A5;
    goto loc_0089F3A5;
loc_0089F3A0:
loc_0089F3A5:
    *(unsigned __int16 *)(v_stack_m108 + 90) = 120;
    result = ExAllocatePool2(256, 120, (unsigned int)(0x6D4E6F49ULL), (unsigned int)(a5));
    *(unsigned __int64 *)(v_stack_m108 + 96) = result;
    if (result == 0) goto loc_008A01A9;
loc_0089F3CA:
    result = RtlCopyUnicodeString(v_stack_m108 + 88, v_stack_m128, (unsigned int)(0x6D4E6F49ULL), (unsigned int)(a5));
    if ((*(unsigned __int8 *)(a8 + 137)) != 0) goto loc_0089F4D7;
loc_0089F3ED:
    if ((*(unsigned int *)(a8 + 120)) != 0) goto loc_0089F41E;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 16))) & (128));
    if (!(condition_is_equal)) {
        a3 = *(unsigned __int64 *)(result + 112);
    }
    result = (unsigned int)(0xC000000DULL);
    if ((unsigned int)(a1) != 0) { result = 0; }
    v_stack_m144 = (unsigned int)(result);
    if (a3 != 0) goto loc_0089F8F9;
loc_0089F41E:
    a3 = 0;
    a2 = 0;
    result = KeInitializeEvent(v_stack_m108 + 152, a2, a3, (unsigned int)(a5));
    *(unsigned __int64 *)(a8 + 8) = v_stack_m108;
    if ((((unsigned __int8)((unsigned __int8)(result))) & (4)) == 0) goto loc_0089F4D0;
    result = IopQueueThreadIrp(result, a2, a3, (unsigned int)(a5));
    if ((*(unsigned __int8 *)(result + 71)) < 0) goto loc_0089F45A;
    if (*(unsigned __int64 *)(result + 200) != 0) goto loc_0089F8E9;
loc_0089F45A:
    result = 0;
loc_0089F45C:
    if (0 != 0) goto loc_008A0783;
    result = IofCallDriver(v_stack_m130, 0, a3, (unsigned int)(a5));
loc_0089F472:
    v_stack_m144 = (unsigned int)((unsigned int)((unsigned int)(result)));
loc_0089F477:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == 259) goto loc_0089FA48;
loc_0089F484:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 16))) & (128));
    if (condition_is_not_equal) goto loc_0089EC77;
    goto loc_0089EC83;
loc_0089F4A1:
loc_0089F4A6:
    result = IopSetFileObjectExtensionFlag(v_stack_m108, 32, v_stack_mE8, (unsigned int)(a5));
    goto loc_0089F366;
loc_0089F4B3:
    if (((unsigned int)(result)) != 1) goto loc_008A070C;
    *(unsigned __int8 *)((unsigned int)((unsigned int)(result))) = (unsigned __int8)(result);
loc_0089F4C0:
    *(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 32) = *(unsigned __int64 *)(a8 + 128);
    goto loc_0089F26D;
loc_0089F4D0:
    goto loc_0089F477;
loc_0089F4D7:
    v_stack_m148 = 0;
    v_stack_m188 = v_stack_m148;
    result = IopQueryInformation(a8, v_stack_m130, result, (unsigned int)(v_stack_m144));
    v_stack_m144 = (unsigned int)(result);
    if (sign_flag) goto loc_0089F9D3;
    if (v_stack_m148 != 0) goto loc_0089F9D3;
    result = PsGetCurrentServerSiloGlobals(a8, v_stack_m130, result, (unsigned int)(v_stack_m144));
    if (((unsigned __int16)(*(unsigned __int16 *)(v_stack_m108 + 88))) == (*(unsigned __int16 *)(v_stack_m128))) goto loc_0089F9A1;
loc_0089F52F:
    result = v_stack_m128;
    if (*(unsigned __int64 *)(v_stack_m108 + 96) != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(v_stack_m108 + 96), a2, *(unsigned __int16 *)(v_stack_m108 + 88), (unsigned int)(v_stack_m144));
        a1 = v_stack_m108 + 88;
        a2 = 0;
        result = RtlInitUnicodeString(a1, a2, *(unsigned __int16 *)(v_stack_m108 + 88), (unsigned int)(v_stack_m144));
    }
    if ((unsigned __int16)(*(unsigned __int16 *)(v_stack_m128)) == 0) goto loc_0089F59C;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_stack_m128))) < 56) goto loc_008A080D;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_stack_m128))) >= 120) goto loc_008A057B;
loc_0089F56B:
    *(unsigned __int16 *)(v_stack_m108 + 90) = 120;
    result = ExAllocatePool2(256, 120, (unsigned int)(0x6D4E6F49ULL), (unsigned int)(v_stack_m144));
    *(unsigned __int64 *)(v_stack_m108 + 96) = result;
    if (result == 0) goto loc_008A0621;
    result = RtlCopyUnicodeString(v_stack_m108 + 88, v_stack_m128, (unsigned int)(0x6D4E6F49ULL), (unsigned int)(v_stack_m144));
loc_0089F59C:
    v_stack_m168 = (unsigned int)((unsigned int)(v_stack_mF0));
    v_stack_m170 = 1;
    v_stack_m178 = v_stack_mB8;
    v_stack_m180 = a8;
    v_stack_m188 = (unsigned __int8)(v_stack_m140);
    result = IopAllocRealFileObject(v_stack_m108, v_stack_m130, v_stack_m138, (unsigned int)(a5));
    v_stack_m144 = (unsigned int)(result);
    if (sign_flag) goto loc_008A065F;
    *(unsigned __int64 *)((unsigned int)(v_stack_m144) + 48) = v_stack_m108;
    *(unsigned __int64 *)(result + 192) = v_stack_m108;
    goto loc_0089F3ED;
loc_0089F610:
    a2 = 0;
    result = memset(*(unsigned __int64 *)(a8 + 144), a2, 272, (unsigned int)(a5));
    v_stack_m108 = *(unsigned __int64 *)(a8 + 144) + 48;
    result = (*(unsigned __int64 *)(a8 + 144)) >> (8);
    result = (unsigned __int8)((result) ^ ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 7500966) + 40))));
    result = (unsigned __int8)((result) ^ (*(unsigned __int8 *)(v_rip + 7501823)));
    *(unsigned __int8 *)(*(unsigned __int64 *)(a8 + 144) + 24) = (unsigned __int8)(result);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a8 + 144)) = 1;
    if (((a5) & (64)) == 0) goto loc_0089FAB4;
loc_0089F665:
    *(unsigned __int16 *)(*(unsigned __int64 *)(a8 + 144) + 48) = 5;
    *(unsigned __int16 *)(*(unsigned __int64 *)(a8 + 144) + 50) = 216;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a8 + 144) + 112) = *(unsigned __int64 *)(a8 + 40);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a8 + 144) + 56) = v_stack_m138;
    result = IopRetrieveTransactionParametersFromOpenPacket(v_stack_m130, a8, (unsigned int)(v_stack_mF0), *(unsigned __int64 *)(a8 + 144) + 48);
    v_stack_m144 = (unsigned int)(result);
    if (sign_flag) goto loc_008A0837;
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(a8 + 152))) & (36));
    if (((unsigned __int8)(result)) != 32) goto loc_0089F6EB;
    if (v_stack_m140 == 0) goto loc_0089F6EB;
    if (((*(unsigned int *)(v_stack_m130 + 48)) & (0x40000ULL)) == 0) goto loc_008A02A5;
loc_0089F6C9:
    result = IopRetrieveTransactionParameters(v_stack_m130, a8, (unsigned int)(v_stack_mF0), *(unsigned __int64 *)(a8 + 144) + 48);
    v_stack_m144 = (unsigned int)(result);
    if (sign_flag) goto loc_0089FD2C;
loc_0089F6EB:
    result = PsIsHostSilo(*(unsigned __int64 *)(v_stack_mB8 + 8), a8, (unsigned int)(v_stack_mF0), *(unsigned __int64 *)(a8 + 144) + 48);
    if ((unsigned __int8)(result) == 0) goto loc_0089F722;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a8 + 144) + 48 + 64) == 0) goto loc_0089F342;
    result = IoGetSilo(*(unsigned __int64 *)(*(unsigned __int64 *)(a8 + 144) + 48 + 64), a8, (unsigned int)(v_stack_mF0), *(unsigned __int64 *)(a8 + 144) + 48);
    result = PsIsHostSilo(result, a8, (unsigned int)(v_stack_mF0), *(unsigned __int64 *)(a8 + 144) + 48);
    if ((unsigned __int8)(result) != 0) goto loc_0089F342;
loc_0089F722:
    v_stack_mA8 = 0;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a8 + 144) + 48 + 64) != 0) goto loc_008A0555;
loc_0089F73A:
loc_0089F746:
    v_stack_mE0 = *(unsigned __int64 *)(v_stack_mB8 + 8);
    result = PsIsHostSilo(*(unsigned __int64 *)(v_stack_mB8 + 8), *(unsigned __int64 *)(*(unsigned __int64 *)(a8 + 144) + 48 + 64), (unsigned int)(v_stack_mF0), *(unsigned __int64 *)(a8 + 144) + 48);
    if ((unsigned __int8)(result) != 0) goto loc_0089F342;
    result = PsAcquireSiloHardReference(v_stack_mE0, *(unsigned __int64 *)(*(unsigned __int64 *)(a8 + 144) + 48 + 64), (unsigned int)(v_stack_mF0), *(unsigned __int64 *)(a8 + 144) + 48);
    v_stack_m144 = (unsigned int)(result);
    if (sign_flag) goto loc_0089FAFC;
    v_stack_m180 = 0;
    v_stack_m188 = v_stack_mA8;
    result = IopGetSetSpecificExtension(*(unsigned __int64 *)(a8 + 144) + 48, 7, 7 + 9, 1);
    v_stack_m144 = (unsigned int)(result);
    if (sign_flag) goto loc_0089FAC3;
loc_0089F7A9:
    if (sign_flag) goto loc_0089FAFC;
    *(unsigned int *)(v_stack_mA8) = 16;
    *(unsigned __int64 *)(v_stack_mA8 + 8) = v_stack_mE0;
    result = ObfReferenceObjectWithTag(v_stack_mE0, (unsigned int)(0x70536F49ULL), 7 + 9, 1);
    goto loc_0089F342;
loc_0089F7E1:
    goto loc_0089F3A5;
loc_0089F7EB:
    if (v_stack_m140 != 0) goto loc_0089F7FD;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a8 + 84)))) & (1)) == 0) goto loc_0089F1BD;
loc_0089F7FD:
    if ((*(unsigned __int64 *)(a8 + 40)) != 0) goto loc_0089F815;
    if ((*(unsigned __int16 *)(v_stack_m128)) == 0) goto loc_0089F1BD;
loc_0089F815:
    if (v_stack_m120 != 0) goto loc_0089F1BD;
    v_stack_m110 = 0;
    v_stack_m158 = 1;
    v_stack_m160 = v_stack_m100;
    v_stack_m168 = v_stack_m80;
    v_stack_m170 = v_stack_mF8;
    v_stack_m178 = v_stack_m11C;
    v_stack_m180 = 0;
    v_stack_m188 = (unsigned int)((unsigned int)(*(unsigned int *)(a8 + 88)));
    result = IopCreateSecurityCheck(result, v_stack_mA8, v_stack_mD0, (unsigned int)((unsigned int)(*(unsigned __int64 *)(a8 + 144) + 48)));
    if ((unsigned __int8)(result) != 0) goto loc_0089F1BD;
    a3 = 0;
    a2 = 0;
    result = IopDecrementDeviceObjectRef(result, a2, a3, (unsigned int)((unsigned int)(*(unsigned __int64 *)(a8 + 144) + 48)));
    if ((unsigned int)(v_stack_m144) != 0) {
        a1 = (unsigned int)(v_stack_m144);
        result = IopDereferenceVpbAndFree(a1, a2, a3, (unsigned int)((unsigned int)(*(unsigned __int64 *)(a8 + 144) + 48)));
    }
    goto loc_008A088F;
loc_0089F8B2:
    a3 = (unsigned __int8)(((unsigned __int8)((unsigned __int8)(result))) >> (3));
    a3 = (unsigned __int8)((a3) & (1));
    result = IopCheckTopDeviceHint(v_stack_m130, a8, a3, v_stack_m128);
    v_stack_m144 = (unsigned int)(result);
    if (sign_flag) goto loc_0089FAD9;
    goto loc_0089F18B;
loc_0089F8E9:
    if (((*(unsigned __int8 *)(result)) & (2)) == 0) goto loc_0089F45A;
    goto loc_0089F45C;
loc_0089F8F9:
    result = IopSymlinkGetECP(a3, v_stack_mC8, a3, v_stack_m128);
    if (((unsigned int)(result)) == 0xC0000225ULL) goto loc_0089F41E;
    result = IopSymlinkGetMostRecentlyUsedName(v_stack_mC8, v_stack_mC8, a3, v_stack_m128);
    if ((*(unsigned __int16 *)(result + 4)) != 0) goto loc_0089F41E;
    a1 = (unsigned __int16)((*(unsigned __int16 *)(v_stack_mF8)) - (*(unsigned __int16 *)(v_stack_m128)));
    v_stack_m180 = (unsigned __int16)(*(unsigned __int16 *)(result + 2));
    v_stack_m188 = (unsigned __int16)(a1);
    result = IopSymlinkUpdateECP(result, result, *(unsigned __int16 *)(result), v_stack_mF8);
    v_stack_m144 = (unsigned int)(result);
    if (!sign_flag) goto loc_0089F41E;
    *(unsigned int *)(result + 48) = (unsigned int)(result);
    *(unsigned __int64 *)(result + 56) = 0;
    v_rbx = (unsigned __int8)(((unsigned __int8)(result)) & (251));
    goto loc_0089F41E;
loc_0089F97F:
    a3 = 0;
    a2 = 0;
    result = IopDecrementDeviceObjectRef(v_stack_m138, a2, a3, v_stack_mF8);
    if ((unsigned int)(v_stack_m144) != 0) goto loc_008A0867;
loc_0089F997:
    goto loc_008A088F;
loc_0089F9A1:
    result = memcmp(*(unsigned __int64 *)(*(unsigned __int64 *)(a8 + 144) + 48 + 96), *(unsigned __int64 *)(v_stack_m130 + 8), a3, v_stack_mF8);
    if ((unsigned int)(result) == 0) goto loc_0089F59C;
    goto loc_0089F52F;
loc_0089F9BB:
    result = (unsigned int)((result) & (0xFFFFFFEFULL));
    *(unsigned int *)(a8 + 152) = (unsigned int)(result);
    goto loc_0089F199;
loc_0089F9C9:
    goto loc_0089F4A6;
loc_0089F9D3:
    *(unsigned int *)(a8 + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 48)));
    *(unsigned __int64 *)(a8 + 24) = *(unsigned __int64 *)(result + 56);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result + 48)))) == 260) goto loc_008A06A7;
loc_0089F9EE:
    result = *(unsigned __int64 *)(result + 56);
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a8 + 144) + 48 + 88)) != 0) {
        a2 = 0;
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(a8 + 144) + 48 + 96);
        result = ExFreePoolWithTag(a1, a2, a3, v_stack_mF8);
    }
    result = IopDeleteFileObjectExtension(*(unsigned __int64 *)(a8 + 144) + 48, a2, a3, v_stack_mF8);
    a3 = 0;
    a2 = 0;
    result = IopDecrementDeviceObjectRef(v_stack_m138, a2, a3, v_stack_mF8);
    if (v_stack_m118 == 0) goto loc_0089FA2C;
loc_0089FA27:
    result = IopDereferenceVpbAndFree(v_stack_m118, a2, a3, v_stack_mF8);
loc_0089FA2C:
    result = IoFreeIrp(result, a2, a3, v_stack_mF8);
    goto loc_008A088F;
loc_0089FA3D:
    result = (unsigned __int8)(((unsigned int)(v_stack_m144)) | (128));
    *(unsigned __int8 *)((unsigned int)(v_stack_m144) + 2) = (unsigned __int8)(result);
    goto loc_0089F26D;
loc_0089FA48:
    if (((*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 116)) & (0x400ULL)) != 0) goto loc_008A041B;
    v_rbx = (unsigned __int8)((v_rbx) | (128));
loc_0089FA61:
    v_rsi = (unsigned __int8)(((unsigned __int8)(v_rbx)) >> (7));
    v_stack_mA8 = v_stack_m108 + 152;
loc_0089FA7F:
    v_stack_m188 = 0;
    a3 = 0;
    a2 = 0;
    result = KeWaitForSingleObject(v_stack_m108 + 152, a2, a3, (unsigned __int8)(v_rsi));
    v_stack_m144 = (unsigned int)(result);
    if (((unsigned int)(result)) == 257) goto loc_0089FE0F;
loc_0089FAA4:
    v_stack_m144 = (unsigned int)((unsigned int)(v_stack_m98));
    goto loc_0089F484;
loc_0089FAB4:
    goto loc_0089F665;
loc_0089FAC3:
    result = PsReleaseSiloHardReference(v_stack_mE0, a2, a3, (unsigned __int8)(v_rsi));
    goto loc_0089F7A9;
loc_0089FAD9:
    result = (unsigned int)(v_stack_m144);
    if ((unsigned int)(v_stack_m144) != 0) {
        a1 = (unsigned int)(v_stack_m144);
        result = IopDereferenceVpbAndFree(a1, a2, a3, (unsigned __int8)(v_rsi));
    }
    a3 = 0;
    a2 = 0;
    result = IopDecrementDeviceObjectRef(result, a2, a3, (unsigned __int8)(v_rsi));
loc_0089FAF3:
    goto loc_008A088F;
loc_0089FAFC:
    result = IoFreeIrp(result, a2, a3, (unsigned __int8)(v_rsi));
    a3 = 0;
    a2 = 0;
    result = IopDecrementDeviceObjectRef(v_stack_m138, a2, a3, (unsigned __int8)(v_rsi));
    if (v_stack_m118 == 0) goto loc_0089F166;
loc_0089FB27:
    result = IopDereferenceVpbAndFree(v_stack_m118, a2, a3, (unsigned __int8)(v_rsi));
    goto loc_0089F166;
loc_0089FB31:
    if (((v_stack_m118) & (-3)) != 0) goto loc_0089FBDB;
loc_0089FB48:
    if ((*(unsigned __int16 *)(v_stack_mF8 + 2)) >= ((unsigned __int16)(*(unsigned __int16 *)(v_stack_m108 + 88)))) goto loc_0089FBB0;
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(*(unsigned __int16 *)(v_stack_m108 + 88))), (unsigned int)(0x63466F49ULL), (unsigned __int8)(v_rsi));
    if (result == 0) goto loc_008A0320;
    result = v_stack_mF8;
    if (*(unsigned __int64 *)(v_stack_mF8 + 8) != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(v_stack_mF8 + 8), a2, (unsigned int)(0x63466F49ULL), (unsigned __int8)(v_rsi));
    }
    *(unsigned __int64 *)(v_stack_mF8 + 8) = result;
    *(unsigned __int16 *)(v_stack_mF8 + 2) = (unsigned __int16)(*(unsigned __int16 *)(v_stack_m108 + 88));
loc_0089FBB0:
    result = RtlCopyUnicodeString(v_stack_mF8, v_stack_m108 + 88, (unsigned int)(0x63466F49ULL), (unsigned __int8)(v_rsi));
    a1 = (v_stack_m90) + (result);
    if (a1 > 22) goto loc_0089FBF9;
    if (a1 >= 22) goto loc_0089FBF9;
    *(unsigned __int64 *)(a8 + 40) = 0;
    goto loc_0089FBF9;
loc_0089FBDB:
    if ((a1 + result * 1) > 22) goto loc_0089FBF9;
    if ((a1 + result * 1) >= 22) goto loc_0089FBF9;
    if ((unsigned __int8)((unsigned int)(v_stack_m144)) == 0) goto loc_0089FB48;
loc_0089FBF9:
    result = a1 + result * 1;
    if ((*(unsigned __int16 *)(v_stack_m108 + 88)) != 0) {
        a2 = 0;
        a1 = *(unsigned __int64 *)(v_stack_m108 + 96);
        result = ExFreePoolWithTag(a1, a2, (unsigned int)(0x63466F49ULL), (unsigned __int8)(v_rsi));
        *(unsigned __int16 *)(v_stack_m108 + 88) = 0;
    }
    *(unsigned __int64 *)(v_stack_m108 + 8) = 0;
    result = ObfDereferenceObject(v_stack_m108, a2, (unsigned int)(0x63466F49ULL), (unsigned __int8)(v_rsi));
    *(unsigned __int64 *)(a8 + 8) = 0;
    a3 = 0;
    a2 = 0;
    result = IopDecrementDeviceObjectRef(v_stack_m138, a2, a3, (unsigned __int8)(v_rsi));
    result = v_stack_m118;
    if (v_stack_m118 != 0) {
        a1 = v_stack_m118;
        result = IopDereferenceVpbAndFree(a1, a2, a3, (unsigned __int8)(v_rsi));
    }
    if (v_stack_m90 == 1) goto loc_008A0423;
    *(unsigned __int64 *)(a8 + 40) = 0;
    if ((v_stack_m90 + result * 1) > 22) goto loc_0089FCB5;
    if ((v_stack_m90 + result * 1) >= 22) goto loc_0089FCB5;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a8 + 152))) | (16));
    *(unsigned int *)(a8 + 152) = (unsigned int)(a1);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m138 + 72)))) > 36) goto loc_008A06CE;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m138 + 72)))) >= 36) goto loc_008A06CE;
loc_0089FCA4:
    if (1 == 0) goto loc_008A0446;
    a1 = (unsigned int)((a1) | (8));
loc_0089FCAF:
    *(unsigned int *)(a8 + 152) = (unsigned int)(a1);
loc_0089FCB5:
    if ((*(unsigned __int8 *)(a8 + 136)) != 0) goto loc_008A0817;
    result = *(unsigned __int64 *)(v_stack_m138 + 312);
    if (((*(unsigned int *)(*(unsigned __int64 *)(v_stack_m138 + 312) + 32)) & (0x800ULL)) == 0) {
        a1 = v_stack_mD0;
        result = *(unsigned int *)(a1 + 24);
        *(unsigned int *)(a1 + 16) = (unsigned int)(result);
        *(unsigned int *)(a1 + 20) = 0;
    }
    if ((v_stack_m90 + result * 1) > 22) goto loc_0089FCFF;
    if ((v_stack_m90 + result * 1) < 22) goto loc_008A0183;
loc_0089FCFF:
    if (v_stack_m90 != ((unsigned int)(0xA0000019ULL))) goto loc_008A016F;
loc_0089FD0D:
    result = PsGetParentSilo(*(unsigned __int64 *)(v_stack_mB8 + 8), v_stack_m90, (unsigned int)(0x400201ULL), (unsigned __int8)(v_rsi));
    *(unsigned __int64 *)(v_stack_mB8 + 8) = result;
    goto loc_008A088F;
loc_0089FD2C:
    result = IoFreeIrp(result, v_stack_m90, (unsigned int)(0x400201ULL), (unsigned __int8)(v_rsi));
    a3 = 0;
    a2 = 0;
    result = IopDecrementDeviceObjectRef(v_stack_m138, a2, a3, (unsigned __int8)(v_rsi));
    if (v_stack_m118 == 0) goto loc_0089F166;
    goto loc_008A085F;
loc_0089FD59:
    if (((*(unsigned int *)(*(unsigned __int64 *)(result + 312) + 32)) & (0x800ULL)) != 0) goto loc_0089E8F5;
    if ((unsigned __int8)((unsigned __int8)(v_rsi)) != 0) goto loc_0089FD7D;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a8 + 84)))) & (1)) == 0) goto loc_0089E8F5;
loc_0089FD7D:
    if (0 != 0) goto loc_0089FD8C;
    if ((*(unsigned __int16 *)(a3)) == 0) goto loc_0089E8F5;
loc_0089FD8C:
    if (v_stack_m120 != 0) goto loc_0089E8F5;
    v_stack_m110 = 0;
    v_stack_m158 = 0;
    v_stack_m160 = v_stack_m100;
    v_stack_m168 = v_stack_m80;
    v_stack_m170 = v_stack_mF8;
    v_stack_m178 = v_stack_m11C;
    v_stack_m180 = 0;
    v_stack_m188 = (unsigned int)((unsigned int)(*(unsigned int *)(a8 + 88)));
    result = IopCreateSecurityCheck(v_stack_m138, result, v_stack_mD0, (unsigned int)((unsigned int)(v_stack_m108)));
    if ((unsigned __int8)(result) == 0) goto loc_0089E9BC;
    goto loc_0089E8F5;
loc_0089FE0F:
    if ((*(unsigned int *)(v_rip + 7499517)) != 0) goto loc_008A0716;
loc_0089FE29:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1440)))) & (1)) != 0) goto loc_008A059B;
    if ((*(unsigned int *)(v_stack_m108 + 156)) == 0) goto loc_008A0591;
loc_0089FE56:
    result = *(unsigned __int64 *)(gs_base + (0 + 392));
    if ((*(unsigned int *)(v_rip + 7499459)) != 0) {
        a1 = 1;
        a2 = (unsigned __int8)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, v_stack_m128, (unsigned int)((unsigned int)(v_stack_m108)));
    }
    goto loc_0089FA7F;
loc_0089FE81:
    v_stack_mC0 = *(unsigned __int64 *)(result + 160);
    if (v_stack_m128 == 0) goto loc_0089FEAC;
    result = IopSymlinkGetECP(v_stack_m128, v_stack_mC8, v_stack_m128, (unsigned int)((unsigned int)(v_stack_m108)));
    if (((unsigned int)(result)) != 0xC0000225ULL) goto loc_0089FF1F;
loc_0089FEAC:
    a4 = (unsigned __int16)((*(unsigned __int16 *)(v_stack_mF8)) - (*(unsigned __int16 *)(v_stack_m128)));
    v_stack_m188 = v_stack_mC8;
    result = IopSymlinkCreateECP(result, v_stack_m108, v_stack_mF8, a4);
    v_stack_m144 = (unsigned int)(result);
    if (sign_flag) goto loc_008A030F;
    if (v_stack_mE8 != 0) goto loc_0089FF27;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 16))) & (128));
    if (!(condition_is_equal)) {
        a2 = *(unsigned __int64 *)(result + 112);
        v_stack_mE8 = a2;
    }
    result = (unsigned int)(0xC000000DULL);
    if ((unsigned int)(a1) != 0) { result = 0; }
    v_stack_m144 = (unsigned int)(result);
loc_0089FF1F:
loc_0089FF27:
    if ((*(unsigned int *)(result + 48)) != 260) goto loc_0089ECAA;
    if ((unsigned int)(v_stack_m138) != 0) goto loc_008A05CD;
loc_0089FF45:
    result = IopSymlinkProcessReparse(result, v_stack_m108, v_stack_mC0, (unsigned __int8)(v_cr8));
    a1 = (result) + (*(unsigned __int64 *)(result + 56));
    if (a1 > 22) goto loc_0089ECAA;
    if (a1 >= 22) goto loc_0089ECAA;
    if ((*(unsigned int *)(result + 48)) < 0) goto loc_008A0285;
    a1 = 0;
    if ((unsigned __int16)(*(unsigned __int16 *)(v_stack_mC0 + 6)) == 0) { a1 = 16; }
    result = (unsigned __int8)(((unsigned __int8)(v_stack_mB8)) & (239));
    v_rbx = (unsigned __int8)(((unsigned __int8)(a1)) | ((unsigned __int8)(result)));
    a1 = (*(unsigned __int64 *)(v_stack_m128 + 8)) - (*(unsigned __int16 *)(v_stack_mC0 + 6));
    if ((unsigned __int16)(*(unsigned __int16 *)(v_stack_mC0 + 6)) == 0) goto loc_0089FFC6;
    if ((*(unsigned __int16 *)(a1 + *(unsigned __int16 *)(v_stack_m128) * 1)) != 58) goto loc_008A0285;
loc_0089FFC6:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a8 + 64)))) & (65)) != 0) goto loc_008A0285;
    if ((*(unsigned __int8 *)(v_stack_m58)) != 0) goto loc_008A0285;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mC0)))) != ((unsigned int)((unsigned int)(0xA0000003ULL)))) goto loc_008A0261;
loc_0089FFF2:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a8 + 64))) | (1));
    goto loc_008A0282;
loc_0089FFFA:
    v_stack_mE0 = v_stack_m110;
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)(v_stack_m108))) | (32));
    v_stack_m130 = 0;
    result = ExAcquireResourceSharedLite(v_rip + 7262834, 1, v_stack_mC0, (unsigned __int8)(v_cr8));
    result = SeLockSubjectContext(v_cr8 + 32, 1, v_stack_mC0, (unsigned __int8)(v_cr8));
    result = (*(unsigned __int64 *)(v_rip + 7498397)) + (76);
    v_stack_m160 = v_stack_m130;
    v_stack_m168 = v_stack_m11C;
    v_stack_m170 = 1;
    v_stack_m178 = result;
    v_stack_m180 = v_stack_mE0;
    v_stack_m188 = 0;
    result = SeAccessCheck(*(unsigned __int64 *)(v_stack_m138 + 272), v_cr8 + 32, 1, (unsigned int)((unsigned int)(v_rsi)));
    if (v_stack_mE0 != 0) goto loc_008A07F3;
loc_008A00A9:
    result = SeUnlockSubjectContext(v_cr8 + 32, v_stack_mE0, 1, (unsigned int)((unsigned int)(v_rsi)));
    result = ExReleaseResourceLite(v_rip + 7262695, v_stack_mE0, 1, (unsigned int)((unsigned int)(v_rsi)));
    result = KeLeaveCriticalRegionThread(v_stack_m100, v_stack_mE0, 1, (unsigned int)((unsigned int)(v_rsi)));
    v_rsi = (unsigned __int8)(((unsigned __int8)(result)) ^ ((unsigned __int8)(v_rbx)));
    v_rsi = (unsigned __int8)((v_rsi) & (1));
    v_rbx = (unsigned __int8)((v_rbx) ^ ((unsigned __int8)(v_rsi)));
    goto loc_0089E866;
loc_008A00DF:
    v_stack_m130 = *(unsigned __int64 *)(a1 + 24);
    if (*(unsigned __int64 *)(a1 + 24) != 0) goto loc_0089E6D0;
    goto loc_0089E6E0;
loc_008A0108:
    if ((*(unsigned __int64 *)(a8 + 24)) == (*(unsigned __int64 *)(a1 + 24))) goto loc_008A074F;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m108 + 72)))) > 36) goto loc_008A045D;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m108 + 72)))) >= 36) goto loc_008A045D;
loc_008A012B:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m108 + 72)))) > 54) goto loc_008A0464;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m108 + 72)))) >= 54) goto loc_008A0464;
loc_008A0140:
    if (1 == 0) goto loc_008A046B;
loc_008A0148:
    a1 = (unsigned __int8)((*(unsigned __int8 *)(a8 + 152)) & (8));
    result = IopSymlinkEnforceEnabledTypes(a1, 1, *(unsigned __int64 *)(a8 + 168), *(unsigned __int64 *)(a1 + 24));
    v_stack_m144 = (unsigned int)(result);
    if (!sign_flag) goto loc_0089E6A8;
    goto loc_0089F16A;
loc_008A016F:
    if (1 == 2) goto loc_0089FD0D;
    goto loc_008A088F;
loc_008A0183:
    if ((unsigned __int8)(v_cr8) == 0) goto loc_0089FCFF;
    *(unsigned __int64 *)(a8 + 24) = v_stack_mC0;
    *(unsigned int *)(a8 + 16) = 0x8000002DULL;
    goto loc_008A088F;
loc_008A01A9:
    result = IoFreeIrp(v_stack_m138, 1, *(unsigned __int64 *)(a8 + 168), *(unsigned __int64 *)(a1 + 24));
    a3 = 0;
    a2 = 0;
    result = IopDecrementDeviceObjectRef(v_stack_m138, a2, a3, *(unsigned __int64 *)(a1 + 24));
    if (v_stack_m118 != 0) {
        a1 = v_stack_m118;
        result = IopDereferenceVpbAndFree(a1, a2, a3, *(unsigned __int64 *)(a1 + 24));
    }
    *(unsigned __int64 *)(v_stack_m108 + 8) = 0;
    if ((*(unsigned __int8 *)(a8 + 137)) != 0) goto loc_008A044E;
    result = ObfDereferenceObject(v_stack_m108, a2, a3, *(unsigned __int64 *)(a1 + 24));
    goto loc_008A088F;
loc_008A01F8:
    if ((*(unsigned __int64 *)(a8 + 40)) != 0) goto loc_0089E719;
    result = PsGetCurrentServerSilo(v_stack_m108, a2, a3, *(unsigned __int64 *)(a1 + 24));
    result = PsGetServerSiloServiceSessionId(result, a2, a3, *(unsigned __int64 *)(a1 + 24));
    result = PsGetCurrentProcessSessionId(result, a2, a3, *(unsigned __int64 *)(a1 + 24));
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != ((unsigned int)(result))) goto loc_008A022C;
    if ((*(unsigned int *)(v_rip + 6053631)) == 0) goto loc_008A0254;
    if (((*(unsigned int *)(a8 + 64)) & (0x40000ULL)) != 0) goto loc_008A0254;
loc_008A022C:
    result = IopGetDevicePDO(v_stack_m138, a2, a3, *(unsigned __int64 *)(a1 + 24));
    if (result == 0) goto loc_008A0254;
    result = IopCheckSessionDeviceAccess(result, a2, a3, *(unsigned __int64 *)(a1 + 24));
    if ((unsigned __int8)(result) == 0) goto loc_008A05FE;
    result = ObfDereferenceObject(result, a2, a3, *(unsigned __int64 *)(a1 + 24));
loc_008A0254:
    goto loc_0089E719;
loc_008A0261:
    if (((unsigned int)(result)) != 0xA000000CULL) goto loc_008A0285;
    if ((*(unsigned int *)(v_stack_m128 + 16)) < 0) goto loc_0089FFF2;
    if (((unsigned int)(result)) != ((unsigned int)(result))) goto loc_008A0285;
    if (((*(unsigned int *)(v_stack_m128 + 16)) & (0x40000000ULL)) == 0) goto loc_008A0285;
    a1 = (unsigned int)((result) | (64));
loc_008A0282:
    *(unsigned int *)(a8 + 64) = (unsigned int)(a1);
loc_008A0285:
    if ((unsigned __int8)(v_stack_m118) != 0) goto loc_0089ECAA;
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m128, a2, a3, *(unsigned __int64 *)(a1 + 24));
    v_stack_mC0 = 0;
    goto loc_0089ECAA;
loc_008A02A5:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m128 + 72)))) > 53) goto loc_0089F6EB;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m128 + 72)))) < 53) goto loc_0089F6C9;
    goto loc_0089F6EB;
loc_008A02CA:
    result = RtlGetActiveConsoleId(v_stack_m128, a2, a3, *(unsigned __int64 *)(a1 + 24));
    result = PsGetCurrentProcessSessionId(v_stack_m128, a2, a3, *(unsigned __int64 *)(a1 + 24));
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == ((unsigned int)(result))) goto loc_0089EA71;
    result = PsGetCurrentServerSilo(v_stack_m128, a2, a3, *(unsigned __int64 *)(a1 + 24));
    result = PsGetServerSiloServiceSessionId(result, a2, a3, *(unsigned __int64 *)(a1 + 24));
    result = PsGetCurrentProcessSessionId(result, a2, a3, *(unsigned __int64 *)(a1 + 24));
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == ((unsigned int)(result))) goto loc_0089EA71;
    result = IopAllowRemoteDASD(result, a2, a3, *(unsigned __int64 *)(a1 + 24));
    if ((unsigned __int8)(result) != 0) goto loc_0089EA71;
    goto loc_0089EA74;
loc_008A030F:
    *(unsigned __int64 *)(1 + 56) = 0;
    *(unsigned int *)(1 + 48) = (unsigned int)((unsigned int)(v_stack_m144));
    goto loc_0089FF1F;
loc_008A0320:
    *(unsigned int *)(a8 + 16) = 0xC000009AULL;
    goto loc_008A088F;
loc_008A0331:
    result = ExAcquireResourceSharedLite(v_rip + 7262038, 1, a3, *(unsigned __int64 *)(a1 + 24));
    result = SeFastTraverseCheck(*(unsigned __int64 *)(1 + 272), v_stack_m118, 32, *(unsigned __int64 *)(a1 + 24));
    result = (unsigned __int8)((result) ^ ((unsigned __int8)(v_rbx)));
    result = (unsigned __int8)((result) & (1));
    v_rbx = (unsigned __int8)((v_rbx) ^ ((unsigned __int8)(result)));
    if ((((unsigned __int8)((unsigned __int8)(result))) & (1)) != 0) goto loc_0089EB8F;
    v_stack_m110 = 0;
    result = SeLockSubjectContext(v_stack_m118 + 32, v_stack_m118, 32, *(unsigned __int64 *)(a1 + 24));
    v_rbx = (unsigned __int8)((v_rbx) | (32));
    result = (*(unsigned __int64 *)(v_rip + 7497551)) + (76);
    a3 = (unsigned __int8)(((unsigned __int8)(v_rbx)) >> (5));
    a3 = (unsigned __int8)((a3) & (1));
    v_stack_m160 = v_stack_m144;
    v_stack_m168 = v_stack_m11C;
    v_stack_m170 = 1;
    v_stack_m178 = result;
    v_stack_m180 = v_stack_m110;
    v_stack_m188 = 0;
    result = SeAccessCheck(*(unsigned __int64 *)(1 + 272), v_stack_m118 + 32, a3, 32);
    result = (unsigned __int8)((result) ^ ((unsigned __int8)(v_rbx)));
    result = (unsigned __int8)((result) & (1));
    v_rbx = (unsigned __int8)((v_rbx) ^ ((unsigned __int8)(result)));
    if (v_stack_m110 == 0) goto loc_0089EB8F;
    result = SeAppendPrivileges(v_stack_m118, v_stack_m110, a3, 32);
    result = CmSiFreeMemory(v_stack_m110, v_stack_m110, a3, 32);
    goto loc_0089EB8F;
loc_008A041B:
    v_rbx = (unsigned __int8)((v_rbx) & (127));
    goto loc_0089FA61;
loc_008A0423:
    result = (unsigned int)(((unsigned int)(v_stack_mB0)) + 1);
    v_stack_mB0 = (unsigned int)(result);
    if (((unsigned int)(result)) <= 32) goto loc_008A07CE;
    goto loc_008A088F;
loc_008A0446:
    a1 = (unsigned int)((v_stack_m110) & (0xFFFFFFF7ULL));
    goto loc_0089FCAF;
loc_008A044E:
    result = IopDeleteFileObjectExtension(a1, v_stack_m110, a3, 32);
    goto loc_008A088F;
loc_008A045D:
    a2 = 0;
    goto loc_008A012B;
loc_008A0464:
    result = 0;
    goto loc_008A0140;
loc_008A046B:
    if (0 != 0) goto loc_008A0148;
loc_008A0473:
    *(unsigned int *)(a8 + 16) = 0xC0000278ULL;
    goto loc_008A088F;
loc_008A0484:
    if (*(unsigned __int64 *)(v_stack_m118 + 32) == 0) {
        a1 = *(unsigned __int64 *)(v_stack_m118 + 48);
    }
    result = SeTokenIsAdmin(a1, a2, a3, 32);
    if ((unsigned __int8)(result) != 0) goto loc_0089EAAF;
    v_rbx = (unsigned __int8)((v_rbx) & (254));
    v_stack_m144 = 0xC0000022ULL;
    goto loc_0089EB49;
loc_008A04B3:
    if (((*(unsigned int *)(*(unsigned __int64 *)(v_stack_m138 + 312) + 32)) & (0x800ULL)) != 0) goto loc_0089EC11;
    if (32 != 0) goto loc_008A04D7;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a8 + 84)))) & (1)) == 0) goto loc_0089EC11;
loc_008A04D7:
    if (v_stack_m120 != 0) goto loc_0089EC11;
    v_stack_m110 = 0;
    v_stack_m158 = 0;
    v_stack_m160 = v_stack_m100;
    v_stack_m168 = v_stack_m80;
    v_stack_m170 = v_stack_mF8;
    v_stack_m178 = v_stack_m11C;
    v_stack_m180 = 0;
    v_stack_m188 = (unsigned int)((unsigned int)(*(unsigned int *)(a8 + 88)));
    result = IopCreateSecurityCheck(v_stack_m138, v_stack_m138, v_stack_mD0, (unsigned int)((unsigned int)(v_stack_m108)));
    if ((unsigned __int8)(result) != 0) goto loc_0089EC11;
    goto loc_0089E9BC;
loc_008A0555:
    result = PsIsServerSilo(*(unsigned __int64 *)(v_stack_mB8 + 8), v_stack_m138, v_stack_mD0, (unsigned int)((unsigned int)(v_stack_m108)));
    if ((unsigned __int8)(result) == 0) goto loc_0089F73A;
    result = IoGetSilo(v_stack_m138, v_stack_m138, v_stack_mD0, (unsigned int)((unsigned int)(v_stack_m108)));
    goto loc_0089F746;
loc_008A057B:
    if (((unsigned __int16)(result)) >= 248) goto loc_0089F56B;
    goto loc_0089F56B;
loc_008A0591:
    if ((*(unsigned __int8 *)(v_stack_m138 + 68)) == 0) goto loc_0089FE56;
loc_008A059B:
    result = 248;
    if ((*(unsigned int *)(v_rip + 7497598)) != 0) {
        a1 = (unsigned __int8)(v_cr8);
        a2 = (unsigned __int8)(v_stack_m118);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, v_stack_mD0, (unsigned int)((unsigned int)(v_stack_m108)));
    }
    result = IopCancelAlertedRequest(v_stack_m108 + 152, v_stack_m138, v_stack_mD0, (unsigned int)((unsigned int)(v_stack_m108)));
    goto loc_0089FAA4;
loc_008A05CD:
    if (result == 0) goto loc_0089FF45;
    result = IopCheckAndUpdateStopOnSymlinkEcp(result, (unsigned int)(*(unsigned int *)(v_stack_m138 + 56)), (unsigned int)((unsigned int)(result)), (unsigned int)((unsigned int)(v_stack_m108)));
    goto loc_0089FF45;
loc_008A05EE:
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(v_stack_m138 + 24), a2, (unsigned int)((unsigned int)(result)), (unsigned int)((unsigned int)(v_stack_m108)));
    goto loc_0089ED37;
loc_008A05FE:
    result = ObfDereferenceObject(*(unsigned __int64 *)(v_stack_m138 + 24), a2, (unsigned int)((unsigned int)(result)), (unsigned int)((unsigned int)(v_stack_m108)));
    a3 = 0;
    a2 = 0;
    result = IopDecrementDeviceObjectRef(v_stack_m138, a2, a3, (unsigned int)((unsigned int)(v_stack_m108)));
    *(unsigned int *)(a8 + 16) = 0xC0000022ULL;
    goto loc_008A088F;
loc_008A0621:
    result = IopDeleteFileObjectExtension(v_stack_m108, a2, a3, (unsigned int)((unsigned int)(v_stack_m108)));
    a3 = 0;
    a2 = 0;
    result = IopDecrementDeviceObjectRef(v_stack_m138, a2, a3, (unsigned int)((unsigned int)(v_stack_m108)));
    if (v_stack_m118 != 0) {
        a1 = v_stack_m118;
        result = IopDereferenceVpbAndFree(a1, a2, a3, (unsigned int)((unsigned int)(v_stack_m108)));
    }
    result = IoFreeIrp(v_stack_m138, a2, a3, (unsigned int)((unsigned int)(v_stack_m108)));
    goto loc_008A088F;
loc_008A065F:
    result = (unsigned int)(0xC000009AULL);
    if ((*(unsigned __int16 *)(v_stack_m108 + 88)) != 0) {
        a2 = 0;
        a1 = *(unsigned __int64 *)(v_stack_m108 + 96);
        result = ExFreePoolWithTag(a1, a2, a3, (unsigned int)((unsigned int)(v_stack_m108)));
    }
    result = IopDeleteFileObjectExtension(v_stack_m108, a2, a3, (unsigned int)((unsigned int)(v_stack_m108)));
    a3 = 0;
    a2 = 0;
    result = IopDecrementDeviceObjectRef(v_stack_m108, a2, a3, (unsigned int)((unsigned int)(v_stack_m108)));
    if (v_stack_m118 == 0) goto loc_0089FA2C;
    goto loc_0089FA27;
loc_008A06A7:
    if (*(unsigned __int64 *)(v_stack_m138 + 160) == 0) goto loc_0089F9EE;
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(v_stack_m138 + 160), a2, a3, (unsigned int)((unsigned int)(v_stack_m108)));
    *(unsigned __int64 *)(v_stack_m138 + 160) = 0;
    *(unsigned __int64 *)(a8 + 40) = 0;
    goto loc_0089F9EE;
loc_008A06CE:
    result = 0;
    goto loc_0089FCA4;
loc_008A06D5:
    if ((*(unsigned __int64 *)(v_stack_m108 + 16)) == v_stack_m118) goto loc_0089ED78;
    if (*(unsigned __int64 *)(v_stack_m108 + 16) != 0) {
        a2 = 1;
        result = IopIncrementVpbRefCount(*(unsigned __int64 *)(v_stack_m108 + 16), a2, a3, (unsigned int)((unsigned int)(v_stack_m108)));
    }
    if (v_stack_m118 == 0) goto loc_0089ED78;
    result = IopDereferenceVpbAndFree(v_stack_m118, a2, a3, (unsigned int)((unsigned int)(v_stack_m108)));
    goto loc_0089ED78;
loc_008A070C:
    *(unsigned __int8 *)(v_stack_m118) = 19;
    goto loc_0089F4C0;
loc_008A0716:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(v_stack_m118), (unsigned __int8)(result), a3, (unsigned int)((unsigned int)(v_stack_m108)));
    goto loc_0089FE29;
loc_008A0727:
    goto loc_0089EE04;
loc_008A072F:
    result = MmIsDriverVerifying(v_stack_m118, (unsigned __int8)(result), a3, (unsigned int)((unsigned int)(v_stack_m108)));
    if ((unsigned int)(result) == 0) goto loc_0089F045;
    result = VfFastIoSnapState(v_stack_m118, (unsigned __int8)(result), a3, (unsigned int)((unsigned int)(v_stack_m108)));
    goto loc_0089F048;
loc_008A074F:
    if (((unsigned int)(v_stack_m118)) > 36) goto loc_008A0473;
    if (((unsigned int)(v_stack_m118)) < 36) goto loc_0089E6A8;
    *(unsigned int *)(a8 + 16) = 0xC0000278ULL;
    goto loc_008A088F;
loc_008A0773:
    if (((unsigned int)((unsigned int)(0xC0000278ULL))) != 0xC0000002ULL) goto loc_0089EF44;
    goto loc_0089F0B7;
loc_008A0783:
    v_stack_m40 = v_xmm0;
    v_stack_m40 = v_xmm0;
    result = IoSetActivityIdThread(v_stack_m40, (unsigned __int8)(result), a3, (unsigned int)((unsigned int)(v_stack_m108)));
    result = IofCallDriver(v_stack_m130, 0, a3, (unsigned int)((unsigned int)(v_stack_m108)));
    result = IoSetActivityIdThread(result, 0, a3, (unsigned int)((unsigned int)(v_stack_m108)));
    goto loc_0089F472;
loc_008A07CE:
    goto loc_0089E639;
loc_008A07F3:
    result = SeAppendPrivileges(v_stack_mD0, 0, a3, (unsigned int)((unsigned int)(v_stack_m108)));
    result = CmSiFreeMemory(v_stack_mE0, 0, a3, (unsigned int)((unsigned int)(v_stack_m108)));
    goto loc_008A00A9;
loc_008A080D:
    goto loc_0089F56B;
loc_008A0817:
    v_stack_m188 = 0;
    result = KeBugCheckEx(249, v_stack_m128, v_stack_m130, v_stack_mF8);
loc_008A0837:
    result = IoFreeIrp(v_stack_mA0, v_stack_m128, v_stack_m130, v_stack_mF8);
    a3 = 0;
    a2 = 0;
    result = IopDecrementDeviceObjectRef(v_stack_m138, a2, a3, v_stack_mF8);
    if (v_stack_m118 == 0) goto loc_0089F166;
loc_008A085F:
    goto loc_0089FB27;
loc_008A0867:
    result = IopDereferenceVpbAndFree(v_stack_m118, a2, a3, v_stack_mF8);
    goto loc_0089F997;
loc_008A0874:
    *(unsigned int *)(a8 + 32) = 0xBEAA0251ULL;
    *(unsigned __int64 *)(a8 + 40) = v_stack_m88;
    *(unsigned int *)(a8 + 16) = 0;
    result = ObfReferenceObject(v_stack_m88, a2, a3, v_stack_mF8);
    result = 0;
    goto loc_008A088F;
loc_008A088F:
    a1 = (v_stack_m30) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, v_stack_mF8);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t IopParseDevice(int64_t Arg1, int64_t Arg2, int64_t Arg3, uint8_t Arg4, uint8_t Arg5, int64_t Arg6, int64_t Arg7, int64_t Arg8, int64_t Arg9, int64_t Arg10, int64_t Arg11)
{
    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m11C;
    uint8_t v_stack_m120;
    uint64_t v_stack_m128;
    uint64_t v_stack_m130;
    uint64_t v_stack_m138;
    uint8_t v_stack_m140;
    uint32_t v_stack_m144;
    uint8_t v_stack_m148;
    uint8_t v_stack_m158;
    uint64_t v_stack_m160;
    uint64_t v_stack_m168;
    uint8_t v_stack_m170;
    uint64_t v_stack_m178;
    uint64_t v_stack_m180;
    uint32_t v_stack_m188;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint32_t v_stack_m5C;
    uint32_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint32_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD4;
    uint8_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint32_t v_stack_mF0;
    uint64_t v_stack_mF8;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x20) = local_rsi;
    local_rsp = (local_rsp) - (384);
    result = (*(uint64_t *)(v_rip + 0x56C20E)) ^ (local_rsp);
    v_stack_m30 = result;
    v_stack_m140 = Arg4;
    v_stack_mD0 = Arg3;
    v_stack_m88 = Arg1;
    v_stack_mF8 = Arg6;
    v_stack_m128 = Arg7;
    v_stack_m48 = Arg8;
    v_stack_mB8 = Arg10;
    v_stack_mA0 = Arg11;
    local_r12 = 0;
    *(uint32_t *)(local_rsp - 0x11C) = 0;
    v_stack_m144 = 0;
    v_stack_m98 = v_xmm0;
    result = 0;
    *(uint64_t *)(local_rsp - 0x70) = v_xmm1;
    *(uint64_t *)(local_rsp - 0x60) = 0;
    v_stack_mB0 = 0;
    v_stack_m120 = 0;
    *(uint32_t *)(local_rsp - 0xD4) = 0;
    *(uint64_t *)(local_rsp - 0x80) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x110) = 0;
    v_stack_mC0 = 0;
    v_stack_mE8 = 0;
    *(uint64_t *)(local_rsp - 0xC8) = 0;
    if (Arg2 != (*(uint64_t *)(v_rip + 0x7284D0))) goto loc_0089EC6D;
    v_stack_m100 = *(uint64_t *)(gs_base + (0 + 0x188));
    result = RtlInitUnicodeString(local_rsp - 128, v_rip + 2483584, Arg3, Arg4);
loc_0089E639:
    *(uint64_t *)(Arg11) = 0;
    v_stack_m108 = 0;
    if (Arg8 == 0) goto loc_0089EC6D;
    if ((*(uint16_t *)(Arg8)) != 8) goto loc_0089EC6D;
    if ((*(uint16_t *)(Arg8 + 0x2)) != 224) goto loc_0089EC6D;
    v_stack_m138 = Arg1;
    if ((*(uint32_t *)(Arg8 + 0x20)) == 1) goto loc_008A0874;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(Arg8 + 0x98)))) & (16)) != 0) goto loc_008A0108;
loc_0089E6A8:
    if (*(uint64_t *)(Arg8 + 0x28) != 0) goto loc_0089E9FD;
loc_0089E6B5:
    if ((*(uint32_t *)(Arg1 + 0x48)) != 7) goto loc_0089E6EE;
    v_stack_m130 = Arg1;
loc_0089E6D0:
    if ((*(uint64_t *)(Arg1 + 0x38)) == 0) goto loc_008A00DF;
loc_0089E6E0:
    if (Arg1 == 0) goto loc_0089E6EE;
    if (Arg1 != Arg1) goto loc_0089EC3F;
loc_0089E6EE:
    result = IopCheckDeviceAndDriver(Arg8, Arg1, Arg1, Arg1);
    v_stack_m144 = (uint32_t)(result);
    if (sign_flag) goto loc_0089F16A;
    if (((*(uint32_t *)(*(uint64_t *)(Arg1 + 0x138) + 0x20)) & (0x400ULL)) != 0) goto loc_008A01F8;
loc_0089E719:
    result = (uint32_t)(*(uint32_t *)(Arg3 + 0x10));
    if (sign_flag) {
        result = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg3 + 0x10))) | (*(uint32_t *)(*(uint64_t *)(v_rip + 0x7283C0) + 0x4C)));
    }
    if (!(condition_is_above_or_equal)) {
        result = (uint32_t)((result) | (*(uint32_t *)(*(uint64_t *)(v_rip + 0x7283C0) + 0x50)));
    }
    if (!(condition_is_above_or_equal)) {
        result = (uint32_t)((result) | (*(uint32_t *)(*(uint64_t *)(v_rip + 0x7283C0) + 0x54)));
    }
    if (!(condition_is_above_or_equal)) {
        result = (uint32_t)((result) | (*(uint32_t *)(*(uint64_t *)(v_rip + 0x7283C0) + 0x58)));
    }
    result = (uint32_t)((result) & (0xFFFFFFFULL));
    *(uint32_t *)(Arg3 + 0x10) = (uint32_t)(result);
    result = (uint32_t)(*(uint32_t *)(Arg3 + 0x18));
    if (sign_flag) {
        result = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg3 + 0x18))) | (*(uint32_t *)(*(uint64_t *)(v_rip + 0x72838A) + 0x4C)));
    }
    if (!(condition_is_above_or_equal)) {
        result = (uint32_t)((result) | (*(uint32_t *)(*(uint64_t *)(v_rip + 0x72838A) + 0x50)));
    }
    if (!(condition_is_above_or_equal)) {
        result = (uint32_t)((result) | (*(uint32_t *)(*(uint64_t *)(v_rip + 0x72838A) + 0x54)));
    }
    if (!(condition_is_above_or_equal)) {
        result = (uint32_t)((result) | (*(uint32_t *)(*(uint64_t *)(v_rip + 0x72838A) + 0x58)));
    }
    result = (uint32_t)((result) & (0xFFFFFFFULL));
    *(uint32_t *)(Arg3 + 0x18) = (uint32_t)(result);
    *(uint64_t *)(*(uint64_t *)(Arg3 + 0x48) + 0x8) = v_xmm0;
    v_stack_mF0 = (uint32_t)((uint32_t)(*(uint32_t *)(Arg3 + 0x10)));
    if (v_stack_m140 == 0) goto loc_0089EA1B;
loc_0089E7AF:
loc_0089E7B2:
    result = IopCheckBackupRestorePrivilege(Arg3, Arg8 + 64, 1, (uint32_t)(*(uint32_t *)(Arg8 + 0x58)));
    if ((*(uint8_t *)(Arg8 + 0x88)) != 0) goto loc_0089E9DA;
loc_0089E7CF:
    if (((*(uint32_t *)(Arg3 + 0xC)) & (256)) != 0) goto loc_0089E9E4;
loc_0089E7DD:
    if (*(uint64_t *)(Arg8 + 0x28) != 0) goto loc_0089EBAD;
loc_0089E7F1:
    if ((uint8_t)(v_stack_m140) == 0) goto loc_0089EA0B;
loc_0089E800:
    if (*(uint64_t *)(Arg8 + 0x28) != 0) goto loc_0089F119;
loc_0089E809:
    if ((*(uint8_t *)(Arg8 + 0x88)) != 0) goto loc_0089E883;
    local_rbx = (uint8_t)((4) & (223));
    if ((*(uint16_t *)(Arg7)) == 0) goto loc_0089EA5D;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg1 + 0x34))) & (0x20100ULL));
    if (((uint32_t)(result)) == 0x20000ULL) goto loc_0089E857;
    if ((uint8_t)(v_stack_m140) == 0) goto loc_0089E857;
    v_stack_m148 = 0;
    result = SeIsAppContainerOrIdentifyLevelContext(Arg3 + 32, v_stack_m148, 1, v_stack_m140);
    if (v_stack_m148 != 0) goto loc_0089FFFA;
loc_0089E857:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(Arg3 + 0xC)))) & (1)) == 0) goto loc_008A0331;
    local_rbx = (uint8_t)((local_rbx) | (1));
loc_0089E866:
    result = (uint32_t)(*(uint32_t *)(Arg3 + 0xC));
    if ((((uint8_t)(local_rbx)) & (32)) != 0) {
        Arg1 = Arg3 + 32;
        result = SeUnlockSubjectContext(Arg1, v_stack_m148, 1, v_stack_m140);
    }
    if ((((uint8_t)(local_rbx)) & (1)) == 0) goto loc_0089E9BC;
loc_0089E883:
    if ((*(uint8_t *)(Arg8 + 0x89)) != 0) goto loc_0089E9D3;
    if ((*(uint8_t *)(Arg8 + 0x8A)) != 0) goto loc_0089E9D3;
    result = 0;
loc_0089E89F:
    local_rbx = (uint8_t)((local_rbx) & (191));
    local_rbx = (uint8_t)((local_rbx) | (0));
    if ((*(uint16_t *)(v_stack_m128)) == 0) goto loc_0089EA2E;
loc_0089E8B6:
    local_rbx = (uint8_t)((local_rbx) & (247));
loc_0089E8B9:
    v_stack_m118 = 0;
    if (*(uint64_t *)(Arg8 + 0x28) != 0) goto loc_0089EBD5;
loc_0089E8D1:
    v_stack_m130 = v_stack_m138;
    if ((*(uint64_t *)(v_stack_m138 + 0x38)) == 0) goto loc_0089E925;
    if ((((uint8_t)(local_rbx)) & (8)) != 0) goto loc_0089E925;
    if (((*(uint32_t *)(v_stack_m138 + 0x34)) & (256)) != 0) goto loc_0089FD59;
loc_0089E8F5:
    result = IopCheckVpbMounted(Arg8, v_stack_m138, v_stack_m128, v_stack_m144);
    v_stack_m118 = result;
    if (result == 0) goto loc_0089FAF3;
    v_stack_m130 = *(uint64_t *)(result + 0x8);
loc_0089E925:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(Arg8 + 0x98)))) & (1)) != 0) goto loc_0089E9F5;
    result = (uint32_t)(*(uint32_t *)(Arg8 + 0x98));
    local_rsi = *(uint64_t *)(result + 0x8);
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x8) + 0x18)) != 0) {
        Arg1 = *(uint64_t *)(result + 0x8);
        result = IoGetAttachedDevice(Arg1, v_stack_m138, v_stack_m128, v_stack_m144);
        local_rsi = result;
        v_stack_m130 = result;
    }
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m138 + 0x34)))) & (0x40001ULL)) == 0) goto loc_0089F182;
    Arg1 = (((*(uint32_t *)(v_stack_m138 + 0x30)) & (0x600100ULL)) == 0) ? 1 : 0;
    result = (condition_is_above_or_equal) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) == 0) goto loc_0089F182;
    v_stack_m148 = 0;
    Arg1 = (v_stack_mD0) + (32);
    result = SeIsAppContainerOrIdentifyLevelContext(Arg1, v_stack_m148, v_stack_m128, v_stack_m144);
    if (v_stack_m148 == 0) goto loc_0089F182;
    if (result == 0) goto loc_0089E9BC;
    if (((*(uint32_t *)(*(uint64_t *)(result + 0x8) + 0x30)) & (0x20000ULL)) != 0) goto loc_0089F182;
    result = *(uint64_t *)(result + 0x8);
    if (result != 0) {
        Arg1 = result;
        result = IopDereferenceVpbAndFree(Arg1, v_stack_m148, v_stack_m128, v_stack_m144);
    }
    Arg3 = 0;
    Arg2 = 0;
    result = IopDecrementDeviceObjectRef(v_stack_m138, Arg2, Arg3, v_stack_m144);
    goto loc_008A088F;
loc_0089E9D3:
    goto loc_0089E89F;
loc_0089E9DA:
    if ((*(uint16_t *)(local_rsi)) != 0) goto loc_0089E7CF;
loc_0089E9E4:
    local_r15 = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg3 + 0x10))) | (*(uint32_t *)(result + 0x14)));
    v_stack_mF0 = (uint32_t)(local_r15);
    goto loc_0089E7DD;
loc_0089E9F5:
    local_rbx = (uint8_t)((local_rbx) | (2));
    goto loc_0089E949;
loc_0089E9FD:
    v_stack_m138 = *(uint64_t *)(64 + 0x8);
    goto loc_0089E6B5;
loc_0089EA0B:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(Arg8 + 0x54)))) & (1)) == 0) goto loc_0089E883;
    goto loc_0089E800;
loc_0089EA1B:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(Arg8 + 0x54)))) & (1)) != 0) goto loc_0089E7AF;
    Arg3 = 0;
    goto loc_0089E7B2;
loc_0089EA2E:
    if ((*(uint64_t *)(Arg8 + 0x28)) != 0) goto loc_0089E8B6;
    Arg1 = ((((uint32_t)(local_r15)) & (0xFEE1FF7FULL)) == 0) ? 1 : 0;
    result = (uint8_t)(((uint8_t)(local_rbx)) >> (6));
    result = (uint8_t)(~(result));
    Arg1 = (uint8_t)((Arg1) & ((uint8_t)(result)));
    if ((((uint8_t)(Arg1)) & (1)) == 0) goto loc_0089E8B6;
    local_rbx = (uint8_t)((local_rbx) | (8));
    goto loc_0089E8B9;
loc_0089EA5D:
    if ((((uint32_t)(result)) & (0x40001ULL)) == 0) goto loc_0089EA71;
    if ((((uint32_t)(local_r15)) & (0xFFEDFF7FULL)) != 0) goto loc_008A02CA;
loc_0089EA71:
    local_r14 = 0;
loc_0089EA74:
    v_stack_m110 = 0;
    result = ExAcquireResourceSharedLite(v_rip + 7268363, 1, Arg3, v_stack_m144);
    result = SeLockSubjectContext(result + 32, 1, Arg3, v_stack_m144);
    local_rbx = (uint8_t)((local_rbx) | (32));
    if (0 != 0) goto loc_008A0484;
loc_0089EAAF:
    result = (*(uint64_t *)(v_rip + 0x72802A)) + (76);
    Arg3 = (uint8_t)(((uint8_t)(local_rbx)) >> (5));
    Arg3 = (uint8_t)((Arg3) & (1));
    v_stack_m160 = v_stack_m144;
    v_stack_m168 = v_stack_m11C;
    v_stack_m170 = 1;
    v_stack_m178 = result;
    v_stack_m180 = v_stack_m110;
    v_stack_m188 = 0;
    result = SeAccessCheck(*(uint64_t *)(v_stack_m138 + 0x110), result + 32, Arg3, (uint32_t)((uint32_t)(local_r15)));
    result = (uint8_t)((result) ^ ((uint8_t)(local_rbx)));
    result = (uint8_t)((result) & (1));
    local_rbx = (uint8_t)((local_rbx) ^ ((uint8_t)(result)));
    if (v_stack_m110 != 0) goto loc_0089EC53;
loc_0089EB28:
    if ((((uint8_t)(local_rbx)) & (1)) != 0) {
        result = v_stack_m11C;
        result = (uint32_t)(~(result));
        *(uint8_t *)(Arg8 + 0x88) = 1;
    }
    Arg1 = (uint8_t)(((uint8_t)(local_rbx)) & (1));
    v_stack_m160 = result + 10;
    v_stack_m168 = 0;
    v_stack_m170 = 1;
    v_stack_m178 = (uint8_t)(Arg1);
    v_stack_m180 = 0;
    v_stack_m188 = result;
    result = SeOpenObjectAuditAlarmWithTransaction(v_stack_m80, v_stack_m138, v_stack_mF8, *(uint64_t *)(v_stack_m138 + 0x110));
loc_0089EB8F:
    result = ExReleaseResourceLite(v_rip + 7268106, v_stack_m138, v_stack_mF8, *(uint64_t *)(v_stack_m138 + 0x110));
    result = KeLeaveCriticalRegionThread(v_stack_m100, v_stack_m138, v_stack_mF8, *(uint64_t *)(v_stack_m138 + 0x110));
    goto loc_0089E866;
loc_0089EBAD:
    if (((*(uint32_t *)(v_stack_m100 + 0x50)) & (0x400000ULL)) == 0) goto loc_0089E7F1;
    Arg2 = (uint8_t)(v_stack_m138);
    if ((*(uint16_t *)(local_rsi)) == 0) { Arg2 = 1; }
    v_stack_m120 = (uint32_t)(Arg2);
    goto loc_0089E7F1;
loc_0089EBD5:
    if (((*(uint32_t *)(Arg2 + 0x50)) & (0x800ULL)) != 0) goto loc_0089E8D1;
    v_stack_m130 = v_stack_m88;
    if (*(uint64_t *)(Arg2 + 0x10) == 0) goto loc_0089EC1B;
    v_stack_m118 = *(uint64_t *)(Arg2 + 0x10);
    if (((*(uint32_t *)(v_stack_m138 + 0x34)) & (256)) != 0) goto loc_008A04B3;
loc_0089EC11:
    result = IopIncrementVpbRefCount(*(uint64_t *)(Arg2 + 0x10), 1, v_stack_mF8, *(uint64_t *)(v_stack_m138 + 0x110));
loc_0089EC1B:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(Arg8 + 0x98)))) & (1)) == 0) goto loc_0089E949;
    local_rsi = v_stack_m88;
    if (*(uint64_t *)(Arg2 + 0x10) != 0) {
        local_rsi = *(uint64_t *)(*(uint64_t *)(Arg2 + 0x10) + 0x8);
        v_stack_m130 = local_rsi;
    }
    local_rbx = (uint8_t)((local_rbx) | (2));
    goto loc_0089E949;
loc_0089EC3F:
    v_stack_m138 = Arg1;
    goto loc_0089E6EE;
loc_0089EC53:
    result = SeAppendPrivileges(*(uint64_t *)(Arg2 + 0x10), 1, v_stack_mF8, *(uint64_t *)(v_stack_m138 + 0x110));
    result = CmSiFreeMemory(v_stack_m110, 1, v_stack_mF8, *(uint64_t *)(v_stack_m138 + 0x110));
    goto loc_0089EB28;
loc_0089EC6D:
    goto loc_008A088F;
loc_0089EC77:
    v_stack_mE8 = *(uint64_t *)(Arg1 + 0x70);
loc_0089EC83:
    result = (uint32_t)(0xC000000DULL);
    if ((uint32_t)(v_stack_m110) != 0) { result = 0; }
    v_stack_m144 = (uint32_t)(result);
    local_rsi = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg8 + 0x54))) & (8));
    local_r13 = (condition_is_not_equal) ? 1 : 0;
    if ((*(uint32_t *)(Arg1 + 0x30)) == 260) goto loc_0089FE81;
loc_0089ECAA:
    if ((*(uint32_t *)(Arg1 + 0x30)) != 0) goto loc_0089ECDA;
    if ((*(uint32_t *)(Arg8 + 0x78)) != 0) goto loc_0089ECDA;
    result = IopSymlinkPropagateToExtensionIfNeeded(local_r15, v_stack_mE8, v_stack_mF8, *(uint64_t *)(v_stack_m138 + 0x110));
    v_stack_m144 = (uint32_t)(result);
    if (sign_flag) goto loc_0089F0C4;
loc_0089ECDA:
    if (v_stack_mE8 != 0) {
        *(uint64_t *)(Arg8 + 0xA8) = v_stack_mE8;
    }
    v_stack_m98 = v_xmm0;
    v_stack_m144 = v_xmm0;
    *(uint32_t *)(local_r15 + 0x9C) = 1;
    result = v_stack_mE8;
    if ((((uint8_t)(local_rbx)) & (4)) != 0) {
        result = v_stack_m100;
        *(uint64_t *)(Arg1 + 0x98) = result;
        Arg1 = Arg1;
        result = IopDequeueIrpFromThread(Arg1, v_stack_mE8, v_stack_mF8, *(uint64_t *)(v_stack_m138 + 0x110));
    }
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg1 + 0x10))) & (48));
    if (((uint8_t)(result)) == 48) goto loc_008A05EE;
loc_0089ED37:
    result = IoFreeIrp(Arg1, v_stack_mE8, v_stack_mF8, *(uint64_t *)(v_stack_m138 + 0x110));
    *(uint64_t *)(Arg8 + 0x18) = v_stack_m90;
    if (sign_flag) goto loc_0089EF78;
    if (((uint32_t)((uint32_t)(v_stack_m144))) == 260) goto loc_0089FB31;
    result = IoGetRelatedDeviceObject(local_r15, v_stack_mE8, v_stack_mF8, *(uint64_t *)(v_stack_m138 + 0x110));
    if (v_stack_m130 != result) goto loc_008A06D5;
loc_0089ED78:
    if ((((uint8_t)(local_rbx)) & (64)) != 0) goto loc_0089EDBF;
    *(uint64_t *)(v_stack_mA0) = local_r15;
    *(uint32_t *)(Arg8 + 0x20) = 0xBEAA0251ULL;
    result = ObfReferenceObject(local_r15, v_stack_mE8, v_stack_mF8, *(uint64_t *)(v_stack_m138 + 0x110));
    if (*(uint64_t *)(local_r15 + 0x40) != 0) goto loc_0089EFC2;
loc_0089EDA4:
    if ((*(uint16_t *)(local_r15 + 0x58)) == 0) goto loc_0089EF9A;
loc_0089EDAF:
    *(uint32_t *)(Arg8 + 0x10) = (uint32_t)((uint32_t)(v_stack_m98));
    goto loc_008A088F;
loc_0089EDBF:
    if ((*(uint8_t *)(Arg8 + 0x89)) == 0) goto loc_0089EF44;
    if ((*(uint8_t *)(Arg8 + 0xD0)) != 0) goto loc_0089F0E2;
    local_rbx = 0;
    if ((*(uint8_t *)(Arg8 + 0x8B)) != 0) goto loc_0089F024;
    v_stack_mC8 = 0;
    if (*(uint64_t *)(*(uint64_t *)(result + 0x8) + 0x50) == 0) goto loc_008A0727;
loc_0089EE04:
    v_stack_mA0 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x8) + 0x50) + 0x20);
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x8) + 0x50) + 0x20) == 0) goto loc_0089EE57;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x665C09)))) & (16)) != 0) goto loc_0089EEED;
loc_0089EE1F:
loc_0089EE22:
    v_stack_m50 = 0;
    v_stack_m188 = result;
    result = guard_dispatch_icall(local_r15, 1, *(uint64_t *)(Arg8 + 0x60), v_stack_m98);
    v_stack_mD8 = (uint8_t)(result);
    if (0 != 0) goto loc_0089EE6B;
loc_0089EE57:
    if ((uint8_t)((uint8_t)(result)) == 0) goto loc_0089EE78;
    v_stack_m144 = (uint32_t)((uint32_t)(v_stack_m98));
    goto loc_0089EF15;
loc_0089EE6B:
    result = VfFastIoCheckState(0, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x8) + 0x50) + 0x20), *(uint64_t *)(Arg8 + 0x60), v_stack_m98);
    goto loc_0089EE57;
loc_0089EE78:
    result = ExAllocatePool2(40 + 24, 40, (uint32_t)(0x20206F49ULL), v_stack_m98);
    v_stack_mC8 = result;
    if (result == 0) goto loc_0089EF0D;
    v_stack_m178 = 1;
    v_stack_m180 = v_stack_mD4;
    v_stack_m188 = result;
    Arg4 = 0;
    result = IopQueryXxxInformation(local_r15, Arg4 + 4, Arg4 + 40, Arg4);
    v_stack_m144 = (uint32_t)(result);
    if (!(sign_flag)) {
        Arg3 = v_stack_mD4;
        Arg2 = result;
        Arg1 = *(uint64_t *)(Arg8 + 0x60);
        result = memcpy(Arg1, Arg2, Arg3, Arg4);
    }
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, Arg3, Arg4);
    goto loc_0089EF15;
loc_0089EEED:
    result = MmIsDriverVerifying(0, Arg2, Arg3, Arg4);
    if ((uint32_t)(result) == 0) goto loc_0089EE1F;
    result = VfFastIoSnapState(0, Arg2, Arg3, Arg4);
    goto loc_0089EE22;
loc_0089EF0D:
    v_stack_m144 = 0xC000009AULL;
loc_0089EF15:
    goto loc_0089EF44;
loc_0089EF44:
    *(uint32_t *)(Arg8 + 0x20) = 0xBEAA0251ULL;
    Arg1 = 0;
    result = IopCloseFile(Arg1, local_r15, 1, 1);
    result = ObfDereferenceObject(local_r15, local_r15, 1, 1);
    *(uint64_t *)(Arg8 + 0x8) = 0;
    *(uint32_t *)(Arg8 + 0x10) = (uint32_t)((uint32_t)(v_stack_m144));
    goto loc_008A088F;
loc_0089EF78:
    if (((*(uint32_t *)(local_r15 + 0x50)) & (0x200000ULL)) == 0) goto loc_0089EFD4;
    result = ObfDereferenceObject(local_r15, local_r15, 1, 1);
loc_0089EF8A:
    *(uint64_t *)(Arg8 + 0x8) = 0;
    *(uint32_t *)(Arg8 + 0x10) = (uint32_t)((uint32_t)(v_stack_m144));
    goto loc_008A088F;
loc_0089EF9A:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x48))) - (3));
    if (condition_is_equal) goto loc_0089EFB5;
    Arg1 = (uint32_t)((Arg1) - (5));
    if (condition_is_equal) goto loc_0089EFB5;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0089EFB5;
    if (((uint32_t)(Arg1)) != 23) goto loc_0089EDAF;
loc_0089EFB5:
    goto loc_0089EDAF;
loc_0089EFC2:
    if (((*(uint32_t *)((uint32_t)(v_stack_m144) + 0x50)) & (0x400000ULL)) == 0) goto loc_0089EDAF;
    goto loc_0089EDA4;
loc_0089EFD4:
    result = (uint32_t)(v_stack_m144);
    if ((*(uint16_t *)(local_r15 + 0x58)) != 0) {
        Arg2 = 0;
        Arg1 = *(uint64_t *)(local_r15 + 0x60);
        result = ExFreePoolWithTag(Arg1, Arg2, 1, 1);
        *(uint16_t *)(local_r15 + 0x58) = 0;
    }
    *(uint64_t *)(local_r15 + 0x8) = 0;
    result = ObfDereferenceObject(local_r15, Arg2, 1, 1);
    Arg3 = 0;
    Arg2 = 0;
    result = IopDecrementDeviceObjectRef(v_stack_m138, Arg2, Arg3, 1);
    if (v_stack_m118 == 0) goto loc_0089EF8A;
    result = IopDereferenceVpbAndFree(v_stack_m118, Arg2, Arg3, 1);
    goto loc_0089EF8A;
loc_0089F024:
    if (result == 0) goto loc_0089F072;
    if ((*(uint32_t *)(result)) <= 112) goto loc_0089F072;
    if (*(uint64_t *)(result + 0x70) == 0) goto loc_0089F072;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x6659E3)))) & (16)) != 0) goto loc_008A072F;
loc_0089F045:
loc_0089F048:
    v_stack_m188 = result;
    result = guard_dispatch_icall(local_r15, 1, *(uint64_t *)(Arg8 + 0x68), v_stack_m98);
    if (0 != 0) goto loc_0089F172;
loc_0089F072:
    if ((uint8_t)((uint8_t)(result)) != 0) goto loc_0089EF44;
    v_stack_m178 = 1;
    v_stack_m180 = v_stack_mD4;
    v_stack_m188 = *(uint64_t *)(Arg8 + 0x68);
    Arg4 = 0;
    result = IopQueryXxxInformation(local_r15, Arg4 + 34, Arg4 + 56, Arg4);
    v_stack_m144 = (uint32_t)(result);
    if (((uint32_t)(result)) != 0xC000000DULL) goto loc_008A0773;
loc_0089F0B7:
    result = IopGetNetworkOpenInformation(local_r15, Arg8, Arg4 + 56, Arg4);
    goto loc_0089F110;
loc_0089F0C4:
    result = IoCancelFileOpen(v_stack_m130, local_r15, Arg4 + 56, Arg4);
    *(uint64_t *)(*(uint64_t *)(result + 0x70) + 0x38) = 0;
    *(uint32_t *)(*(uint64_t *)(result + 0x70) + 0x30) = (uint32_t)((uint32_t)(v_stack_m144));
    goto loc_0089ECDA;
loc_0089F0E2:
    v_stack_m178 = 1;
    v_stack_m180 = Arg8 + 204;
    v_stack_m188 = *(uint64_t *)(Arg8 + 0x70);
    Arg4 = 0;
    result = IopQueryXxxInformation(local_r15, (uint32_t)(*(uint32_t *)(Arg8 + 0xC8)), (uint32_t)(*(uint32_t *)(Arg8 + 0xCC)), Arg4);
loc_0089F110:
    v_stack_m144 = (uint32_t)(result);
    goto loc_0089EF44;
loc_0089F119:
    if ((uint8_t)((uint32_t)(*(uint32_t *)(Arg8 + 0xC8))) != 0) goto loc_0089E809;
    goto loc_0089E883;
loc_0089F126:
    result = IoFreeIrp(*(uint64_t *)(result + 0x70), (uint32_t)(*(uint32_t *)(Arg8 + 0xC8)), (uint32_t)(*(uint32_t *)(Arg8 + 0xCC)), Arg4);
    Arg3 = 0;
    Arg2 = 0;
    result = IopDecrementDeviceObjectRef(local_r15, Arg2, Arg3, Arg4);
    result = v_stack_m118;
    if (v_stack_m118 != 0) {
        Arg1 = v_stack_m118;
        result = IopDereferenceVpbAndFree(Arg1, Arg2, Arg3, Arg4);
    }
    if (v_stack_m108 != 0) {
        *(uint64_t *)(v_stack_m108 + 0x8) = 0;
        result = ObfDereferenceObject(v_stack_m108, Arg2, Arg3, Arg4);
    }
loc_0089F16A:
    *(uint32_t *)(Arg8 + 0x10) = (uint32_t)((uint32_t)(v_stack_m144));
    goto loc_008A088F;
loc_0089F172:
    result = VfFastIoCheckState(0, *(uint64_t *)(result + 0x70), Arg3, Arg4);
    goto loc_0089F072;
loc_0089F182:
    if ((((uint8_t)((uint8_t)(result))) & (2)) != 0) goto loc_0089F8B2;
loc_0089F18B:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(Arg8 + 0x98)))) & (16)) != 0) goto loc_0089F9BB;
loc_0089F199:
    if (((*(uint32_t *)(result + 0x34)) & (256)) != 0) goto loc_0089F7EB;
    if ((*(uint32_t *)(v_rip + 0x56B81F)) == 0) goto loc_0089F1BD;
    if (((*(uint32_t *)(*(uint64_t *)(result + 0x70) + 0x34)) & (0x100000ULL)) != 0) goto loc_0089F7EB;
loc_0089F1BD:
    Arg3 = 0;
    result = IopAllocateIrpExReturn(result, *(uint8_t *)(result + 0x4C), Arg3, Arg4);
    if (result == 0) goto loc_0089F97F;
    *(uint64_t *)(result + 0x98) = v_stack_m100;
    *(uint8_t *)(result + 0x40) = (uint8_t)(v_stack_m140);
    *(uint32_t *)(result + 0x10) = 0x884ULL;
    v_stack_m70 = Arg9;
    v_stack_m68 = v_stack_mD0;
    v_stack_m60 = (uint32_t)(local_r15);
    v_stack_m5C = (uint32_t)((uint32_t)(*(uint32_t *)(Arg8 + 0x40)));
    local_r13 = (*(uint64_t *)(result + 0xB8)) - (72);
    v_stack_m58 = local_r13;
    *(uint8_t *)(local_r13 + 0x3) = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(Arg8 + 0x78))) != 0) goto loc_0089F4B3;
    *(uint8_t *)(local_r13) = 0;
    *(uint32_t *)(local_r13 + 0x20) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg8 + 0x50)));
    *(uint8_t *)(local_r13 + 0x2) = (uint8_t)(*(uint8_t *)(Arg8 + 0x54));
    if (((Arg5) & (64)) == 0) goto loc_0089FA3D;
loc_0089F26D:
    *(uint64_t *)(result + 0x58) = *(uint64_t *)(Arg8 + 0x38);
    *(uint64_t *)(result + 0x18) = *(uint64_t *)(Arg8 + 0x48);
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg8 + 0x58))) << (24));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg8 + 0x40))) & (0xFFFFFFULL));
    Arg1 = (uint32_t)((Arg1) | ((uint32_t)(result)));
    *(uint32_t *)(local_r13 + 0x10) = (uint32_t)(Arg1);
    *(uint16_t *)(local_r13 + 0x18) = (uint16_t)(*(uint16_t *)(Arg8 + 0x44));
    *(uint16_t *)(local_r13 + 0x1A) = (uint16_t)(*(uint16_t *)(Arg8 + 0x46));
    *(uint64_t *)(local_r13 + 0x8) = v_stack_m70;
    *(uint64_t *)(result + 0x70) = *(uint64_t *)(Arg8 + 0xA8);
    *(uint64_t *)(result + 0x48) = v_stack_m98;
    *(uint64_t *)(result + 0x8) = 0;
    *(uint8_t *)(result + 0x41) = 0;
    *(uint8_t *)(result + 0x44) = 0;
    *(uint64_t *)(result + 0x50) = 0;
    *(uint64_t *)(result + 0x68) = 0;
    *(uint64_t *)(result + 0xA0) = 0;
    if ((*(uint8_t *)(Arg8 + 0x89)) != 0) goto loc_0089F610;
    v_stack_m168 = (uint32_t)(local_r15);
    v_stack_m170 = 0;
    v_stack_m178 = v_stack_mB8;
    v_stack_m180 = Arg8;
    v_stack_m188 = (uint8_t)(v_stack_m140);
    result = IopAllocRealFileObject(v_stack_m108, result, v_stack_m138, (uint32_t)(Arg5));
    v_stack_m144 = (uint32_t)(result);
    if (sign_flag) goto loc_0089F126;
loc_0089F342:
    if ((((uint8_t)((uint8_t)(result))) & (8)) != 0) {
    }
    if ((((uint8_t)(*(uint64_t *)(Arg8 + 0xD8))) & (1)) != 0) goto loc_0089F4A1;
    if ((((uint8_t)(*(uint64_t *)(Arg8 + 0xD8))) & (2)) != 0) goto loc_0089F9C9;
loc_0089F366:
    *(uint64_t *)(result + 0xC0) = v_stack_m108;
    *(uint64_t *)(local_r13 + 0x30) = v_stack_m108;
    if ((uint16_t)(*(uint16_t *)(v_stack_m128)) == 0) goto loc_0089F3CA;
    if (((uint16_t)(*(uint16_t *)(v_stack_m128))) < 56) goto loc_0089F7E1;
    if (((uint16_t)(*(uint16_t *)(v_stack_m128))) < 120) goto loc_0089F3A0;
    if (((uint16_t)(*(uint16_t *)(v_stack_m128))) >= 248) goto loc_0089F3A5;
    goto loc_0089F3A5;
loc_0089F3A0:
loc_0089F3A5:
    *(uint16_t *)(v_stack_m108 + 0x5A) = 120;
    result = ExAllocatePool2(256, 120, (uint32_t)(0x6D4E6F49ULL), (uint32_t)(Arg5));
    *(uint64_t *)(v_stack_m108 + 0x60) = result;
    if (result == 0) goto loc_008A01A9;
loc_0089F3CA:
    result = RtlCopyUnicodeString(v_stack_m108 + 88, v_stack_m128, (uint32_t)(0x6D4E6F49ULL), (uint32_t)(Arg5));
    if ((*(uint8_t *)(Arg8 + 0x89)) != 0) goto loc_0089F4D7;
loc_0089F3ED:
    if ((*(uint32_t *)(Arg8 + 0x78)) != 0) goto loc_0089F41E;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x10))) & (128));
    if (!(condition_is_equal)) {
        Arg3 = *(uint64_t *)(result + 0x70);
    }
    result = (uint32_t)(0xC000000DULL);
    if ((uint32_t)(Arg1) != 0) { result = 0; }
    v_stack_m144 = (uint32_t)(result);
    if (Arg3 != 0) goto loc_0089F8F9;
loc_0089F41E:
    Arg3 = 0;
    Arg2 = 0;
    result = KeInitializeEvent(v_stack_m108 + 152, Arg2, Arg3, (uint32_t)(Arg5));
    *(uint64_t *)(Arg8 + 0x8) = v_stack_m108;
    if ((((uint8_t)((uint8_t)(result))) & (4)) == 0) goto loc_0089F4D0;
    result = IopQueueThreadIrp(result, Arg2, Arg3, (uint32_t)(Arg5));
    if ((*(uint8_t *)(result + 0x47)) < 0) goto loc_0089F45A;
    if (*(uint64_t *)(result + 0xC8) != 0) goto loc_0089F8E9;
loc_0089F45A:
    result = 0;
loc_0089F45C:
    if (0 != 0) goto loc_008A0783;
    result = IofCallDriver(v_stack_m130, 0, Arg3, (uint32_t)(Arg5));
loc_0089F472:
    v_stack_m144 = (uint32_t)((uint32_t)((uint32_t)(result)));
loc_0089F477:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == 259) goto loc_0089FA48;
loc_0089F484:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x10))) & (128));
    if (condition_is_not_equal) goto loc_0089EC77;
    goto loc_0089EC83;
loc_0089F4A1:
loc_0089F4A6:
    result = IopSetFileObjectExtensionFlag(v_stack_m108, 32, v_stack_mE8, (uint32_t)(Arg5));
    goto loc_0089F366;
loc_0089F4B3:
    if (((uint32_t)(result)) != 1) goto loc_008A070C;
    *(uint8_t *)((uint32_t)((uint32_t)(result))) = (uint8_t)(result);
loc_0089F4C0:
    *(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x20) = *(uint64_t *)(Arg8 + 0x80);
    goto loc_0089F26D;
loc_0089F4D0:
    goto loc_0089F477;
loc_0089F4D7:
    v_stack_m148 = 0;
    v_stack_m188 = v_stack_m148;
    result = IopQueryInformation(Arg8, v_stack_m130, result, (uint32_t)(v_stack_m144));
    v_stack_m144 = (uint32_t)(result);
    if (sign_flag) goto loc_0089F9D3;
    if (v_stack_m148 != 0) goto loc_0089F9D3;
    result = PsGetCurrentServerSiloGlobals(Arg8, v_stack_m130, result, (uint32_t)(v_stack_m144));
    if (((uint16_t)(*(uint16_t *)(v_stack_m108 + 0x58))) == (*(uint16_t *)(v_stack_m128))) goto loc_0089F9A1;
loc_0089F52F:
    result = v_stack_m128;
    if (*(uint64_t *)(v_stack_m108 + 0x60) != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(*(uint64_t *)(v_stack_m108 + 0x60), Arg2, *(uint16_t *)(v_stack_m108 + 0x58), (uint32_t)(v_stack_m144));
        Arg1 = v_stack_m108 + 88;
        Arg2 = 0;
        result = RtlInitUnicodeString(Arg1, Arg2, *(uint16_t *)(v_stack_m108 + 0x58), (uint32_t)(v_stack_m144));
    }
    if ((uint16_t)(*(uint16_t *)(v_stack_m128)) == 0) goto loc_0089F59C;
    if (((uint16_t)(*(uint16_t *)(v_stack_m128))) < 56) goto loc_008A080D;
    if (((uint16_t)(*(uint16_t *)(v_stack_m128))) >= 120) goto loc_008A057B;
loc_0089F56B:
    *(uint16_t *)(v_stack_m108 + 0x5A) = 120;
    result = ExAllocatePool2(256, 120, (uint32_t)(0x6D4E6F49ULL), (uint32_t)(v_stack_m144));
    *(uint64_t *)(v_stack_m108 + 0x60) = result;
    if (result == 0) goto loc_008A0621;
    result = RtlCopyUnicodeString(v_stack_m108 + 88, v_stack_m128, (uint32_t)(0x6D4E6F49ULL), (uint32_t)(v_stack_m144));
loc_0089F59C:
    v_stack_m168 = (uint32_t)((uint32_t)(v_stack_mF0));
    v_stack_m170 = 1;
    v_stack_m178 = v_stack_mB8;
    v_stack_m180 = Arg8;
    v_stack_m188 = (uint8_t)(v_stack_m140);
    result = IopAllocRealFileObject(v_stack_m108, v_stack_m130, v_stack_m138, (uint32_t)(Arg5));
    v_stack_m144 = (uint32_t)(result);
    if (sign_flag) goto loc_008A065F;
    *(uint64_t *)((uint32_t)(v_stack_m144) + 0x30) = v_stack_m108;
    *(uint64_t *)(result + 0xC0) = v_stack_m108;
    goto loc_0089F3ED;
loc_0089F610:
    Arg2 = 0;
    result = memset(*(uint64_t *)(Arg8 + 0x90), Arg2, 272, (uint32_t)(Arg5));
    v_stack_m108 = *(uint64_t *)(Arg8 + 0x90) + 48;
    result = (*(uint64_t *)(Arg8 + 0x90)) >> (8);
    result = (uint8_t)((result) ^ ((uint8_t)(*(uint8_t *)(*(uint64_t *)(v_rip + 0x7274A6) + 0x28))));
    result = (uint8_t)((result) ^ (*(uint8_t *)(v_rip + 0x7277FF)));
    *(uint8_t *)(*(uint64_t *)(Arg8 + 0x90) + 0x18) = (uint8_t)(result);
    *(uint64_t *)(*(uint64_t *)(Arg8 + 0x90)) = 1;
    if (((Arg5) & (64)) == 0) goto loc_0089FAB4;
loc_0089F665:
    *(uint16_t *)(*(uint64_t *)(Arg8 + 0x90) + 0x30) = 5;
    *(uint16_t *)(*(uint64_t *)(Arg8 + 0x90) + 0x32) = 216;
    *(uint64_t *)(*(uint64_t *)(Arg8 + 0x90) + 0x70) = *(uint64_t *)(Arg8 + 0x28);
    *(uint64_t *)(*(uint64_t *)(Arg8 + 0x90) + 0x38) = v_stack_m138;
    result = IopRetrieveTransactionParametersFromOpenPacket(v_stack_m130, Arg8, (uint32_t)(v_stack_mF0), *(uint64_t *)(Arg8 + 0x90) + 48);
    v_stack_m144 = (uint32_t)(result);
    if (sign_flag) goto loc_008A0837;
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(Arg8 + 0x98))) & (36));
    if (((uint8_t)(result)) != 32) goto loc_0089F6EB;
    if (v_stack_m140 == 0) goto loc_0089F6EB;
    if (((*(uint32_t *)(v_stack_m130 + 0x30)) & (0x40000ULL)) == 0) goto loc_008A02A5;
loc_0089F6C9:
    result = IopRetrieveTransactionParameters(v_stack_m130, Arg8, (uint32_t)(v_stack_mF0), *(uint64_t *)(Arg8 + 0x90) + 48);
    v_stack_m144 = (uint32_t)(result);
    if (sign_flag) goto loc_0089FD2C;
loc_0089F6EB:
    result = PsIsHostSilo(*(uint64_t *)(v_stack_mB8 + 0x8), Arg8, (uint32_t)(v_stack_mF0), *(uint64_t *)(Arg8 + 0x90) + 48);
    if ((uint8_t)(result) == 0) goto loc_0089F722;
    if (*(uint64_t *)(*(uint64_t *)(Arg8 + 0x90) + 0x30 + 0x40) == 0) goto loc_0089F342;
    result = IoGetSilo(*(uint64_t *)(*(uint64_t *)(Arg8 + 0x90) + 0x30 + 0x40), Arg8, (uint32_t)(v_stack_mF0), *(uint64_t *)(Arg8 + 0x90) + 48);
    result = PsIsHostSilo(result, Arg8, (uint32_t)(v_stack_mF0), *(uint64_t *)(Arg8 + 0x90) + 48);
    if ((uint8_t)(result) != 0) goto loc_0089F342;
loc_0089F722:
    v_stack_mA8 = 0;
    if (*(uint64_t *)(*(uint64_t *)(Arg8 + 0x90) + 0x30 + 0x40) != 0) goto loc_008A0555;
loc_0089F73A:
loc_0089F746:
    v_stack_mE0 = *(uint64_t *)(v_stack_mB8 + 0x8);
    result = PsIsHostSilo(*(uint64_t *)(v_stack_mB8 + 0x8), *(uint64_t *)(*(uint64_t *)(Arg8 + 0x90) + 0x30 + 0x40), (uint32_t)(v_stack_mF0), *(uint64_t *)(Arg8 + 0x90) + 48);
    if ((uint8_t)(result) != 0) goto loc_0089F342;
    result = PsAcquireSiloHardReference(v_stack_mE0, *(uint64_t *)(*(uint64_t *)(Arg8 + 0x90) + 0x30 + 0x40), (uint32_t)(v_stack_mF0), *(uint64_t *)(Arg8 + 0x90) + 48);
    v_stack_m144 = (uint32_t)(result);
    if (sign_flag) goto loc_0089FAFC;
    v_stack_m180 = 0;
    v_stack_m188 = v_stack_mA8;
    result = IopGetSetSpecificExtension(*(uint64_t *)(Arg8 + 0x90) + 48, 7, 7 + 9, 1);
    v_stack_m144 = (uint32_t)(result);
    if (sign_flag) goto loc_0089FAC3;
loc_0089F7A9:
    if (sign_flag) goto loc_0089FAFC;
    *(uint32_t *)(v_stack_mA8) = 16;
    *(uint64_t *)(v_stack_mA8 + 0x8) = v_stack_mE0;
    result = ObfReferenceObjectWithTag(v_stack_mE0, (uint32_t)(0x70536F49ULL), 7 + 9, 1);
    goto loc_0089F342;
loc_0089F7E1:
    goto loc_0089F3A5;
loc_0089F7EB:
    if (v_stack_m140 != 0) goto loc_0089F7FD;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(Arg8 + 0x54)))) & (1)) == 0) goto loc_0089F1BD;
loc_0089F7FD:
    if ((*(uint64_t *)(Arg8 + 0x28)) != 0) goto loc_0089F815;
    if ((*(uint16_t *)(v_stack_m128)) == 0) goto loc_0089F1BD;
loc_0089F815:
    if (v_stack_m120 != 0) goto loc_0089F1BD;
    v_stack_m110 = 0;
    v_stack_m158 = 1;
    v_stack_m160 = v_stack_m100;
    v_stack_m168 = v_stack_m80;
    v_stack_m170 = v_stack_mF8;
    v_stack_m178 = v_stack_m11C;
    v_stack_m180 = 0;
    v_stack_m188 = (uint32_t)((uint32_t)(*(uint32_t *)(Arg8 + 0x58)));
    result = IopCreateSecurityCheck(result, v_stack_mA8, v_stack_mD0, (uint32_t)((uint32_t)(*(uint64_t *)(Arg8 + 0x90) + 48)));
    if ((uint8_t)(result) != 0) goto loc_0089F1BD;
    Arg3 = 0;
    Arg2 = 0;
    result = IopDecrementDeviceObjectRef(result, Arg2, Arg3, (uint32_t)((uint32_t)(*(uint64_t *)(Arg8 + 0x90) + 48)));
    if ((uint32_t)(v_stack_m144) != 0) {
        Arg1 = (uint32_t)(v_stack_m144);
        result = IopDereferenceVpbAndFree(Arg1, Arg2, Arg3, (uint32_t)((uint32_t)(*(uint64_t *)(Arg8 + 0x90) + 48)));
    }
    goto loc_008A088F;
loc_0089F8B2:
    Arg3 = (uint8_t)(((uint8_t)((uint8_t)(result))) >> (3));
    Arg3 = (uint8_t)((Arg3) & (1));
    result = IopCheckTopDeviceHint(v_stack_m130, Arg8, Arg3, v_stack_m128);
    v_stack_m144 = (uint32_t)(result);
    if (sign_flag) goto loc_0089FAD9;
    goto loc_0089F18B;
loc_0089F8E9:
    if (((*(uint8_t *)(result)) & (2)) == 0) goto loc_0089F45A;
    goto loc_0089F45C;
loc_0089F8F9:
    result = IopSymlinkGetECP(Arg3, v_stack_mC8, Arg3, v_stack_m128);
    if (((uint32_t)(result)) == 0xC0000225ULL) goto loc_0089F41E;
    result = IopSymlinkGetMostRecentlyUsedName(v_stack_mC8, v_stack_mC8, Arg3, v_stack_m128);
    if ((*(uint16_t *)(result + 0x4)) != 0) goto loc_0089F41E;
    Arg1 = (uint16_t)((*(uint16_t *)(v_stack_mF8)) - (*(uint16_t *)(v_stack_m128)));
    v_stack_m180 = (uint16_t)(*(uint16_t *)(result + 0x2));
    v_stack_m188 = (uint16_t)(Arg1);
    result = IopSymlinkUpdateECP(result, result, *(uint16_t *)(result), v_stack_mF8);
    v_stack_m144 = (uint32_t)(result);
    if (!sign_flag) goto loc_0089F41E;
    *(uint32_t *)(result + 0x30) = (uint32_t)(result);
    *(uint64_t *)(result + 0x38) = 0;
    local_rbx = (uint8_t)(((uint8_t)(result)) & (251));
    goto loc_0089F41E;
loc_0089F97F:
    Arg3 = 0;
    Arg2 = 0;
    result = IopDecrementDeviceObjectRef(v_stack_m138, Arg2, Arg3, v_stack_mF8);
    if ((uint32_t)(v_stack_m144) != 0) goto loc_008A0867;
loc_0089F997:
    goto loc_008A088F;
loc_0089F9A1:
    result = memcmp(*(uint64_t *)(*(uint64_t *)(Arg8 + 0x90) + 0x30 + 0x60), *(uint64_t *)(v_stack_m130 + 0x8), Arg3, v_stack_mF8);
    if ((uint32_t)(result) == 0) goto loc_0089F59C;
    goto loc_0089F52F;
loc_0089F9BB:
    result = (uint32_t)((result) & (0xFFFFFFEFULL));
    *(uint32_t *)(Arg8 + 0x98) = (uint32_t)(result);
    goto loc_0089F199;
loc_0089F9C9:
    goto loc_0089F4A6;
loc_0089F9D3:
    *(uint32_t *)(Arg8 + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x30)));
    *(uint64_t *)(Arg8 + 0x18) = *(uint64_t *)(result + 0x38);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x30)))) == 260) goto loc_008A06A7;
loc_0089F9EE:
    result = *(uint64_t *)(result + 0x38);
    if ((*(uint16_t *)(*(uint64_t *)(Arg8 + 0x90) + 0x30 + 0x58)) != 0) {
        Arg2 = 0;
        Arg1 = *(uint64_t *)(*(uint64_t *)(Arg8 + 0x90) + 0x30 + 0x60);
        result = ExFreePoolWithTag(Arg1, Arg2, Arg3, v_stack_mF8);
    }
    result = IopDeleteFileObjectExtension(*(uint64_t *)(Arg8 + 0x90) + 48, Arg2, Arg3, v_stack_mF8);
    Arg3 = 0;
    Arg2 = 0;
    result = IopDecrementDeviceObjectRef(v_stack_m138, Arg2, Arg3, v_stack_mF8);
    if (v_stack_m118 == 0) goto loc_0089FA2C;
loc_0089FA27:
    result = IopDereferenceVpbAndFree(v_stack_m118, Arg2, Arg3, v_stack_mF8);
loc_0089FA2C:
    result = IoFreeIrp(result, Arg2, Arg3, v_stack_mF8);
    goto loc_008A088F;
loc_0089FA3D:
    result = (uint8_t)(((uint32_t)(v_stack_m144)) | (128));
    *(uint8_t *)((uint32_t)(v_stack_m144) + 0x2) = (uint8_t)(result);
    goto loc_0089F26D;
loc_0089FA48:
    if (((*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x74)) & (0x400ULL)) != 0) goto loc_008A041B;
    local_rbx = (uint8_t)((local_rbx) | (128));
loc_0089FA61:
    local_rsi = (uint8_t)(((uint8_t)(local_rbx)) >> (7));
    v_stack_mA8 = v_stack_m108 + 152;
loc_0089FA7F:
    v_stack_m188 = 0;
    Arg3 = 0;
    Arg2 = 0;
    result = KeWaitForSingleObject(v_stack_m108 + 152, Arg2, Arg3, (uint8_t)(local_rsi));
    v_stack_m144 = (uint32_t)(result);
    if (((uint32_t)(result)) == 257) goto loc_0089FE0F;
loc_0089FAA4:
    v_stack_m144 = (uint32_t)((uint32_t)(v_stack_m98));
    goto loc_0089F484;
loc_0089FAB4:
    goto loc_0089F665;
loc_0089FAC3:
    result = PsReleaseSiloHardReference(v_stack_mE0, Arg2, Arg3, (uint8_t)(local_rsi));
    goto loc_0089F7A9;
loc_0089FAD9:
    result = (uint32_t)(v_stack_m144);
    if ((uint32_t)(v_stack_m144) != 0) {
        Arg1 = (uint32_t)(v_stack_m144);
        result = IopDereferenceVpbAndFree(Arg1, Arg2, Arg3, (uint8_t)(local_rsi));
    }
    Arg3 = 0;
    Arg2 = 0;
    result = IopDecrementDeviceObjectRef(result, Arg2, Arg3, (uint8_t)(local_rsi));
loc_0089FAF3:
    goto loc_008A088F;
loc_0089FAFC:
    result = IoFreeIrp(result, Arg2, Arg3, (uint8_t)(local_rsi));
    Arg3 = 0;
    Arg2 = 0;
    result = IopDecrementDeviceObjectRef(v_stack_m138, Arg2, Arg3, (uint8_t)(local_rsi));
    if (v_stack_m118 == 0) goto loc_0089F166;
loc_0089FB27:
    result = IopDereferenceVpbAndFree(v_stack_m118, Arg2, Arg3, (uint8_t)(local_rsi));
    goto loc_0089F166;
loc_0089FB31:
    if (((v_stack_m118) & (-3)) != 0) goto loc_0089FBDB;
loc_0089FB48:
    if ((*(uint16_t *)(v_stack_mF8 + 0x2)) >= ((uint16_t)(*(uint16_t *)(v_stack_m108 + 0x58)))) goto loc_0089FBB0;
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(*(uint16_t *)(v_stack_m108 + 0x58))), (uint32_t)(0x63466F49ULL), (uint8_t)(local_rsi));
    if (result == 0) goto loc_008A0320;
    result = v_stack_mF8;
    if (*(uint64_t *)(v_stack_mF8 + 0x8) != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(*(uint64_t *)(v_stack_mF8 + 0x8), Arg2, (uint32_t)(0x63466F49ULL), (uint8_t)(local_rsi));
    }
    *(uint64_t *)(v_stack_mF8 + 0x8) = result;
    *(uint16_t *)(v_stack_mF8 + 0x2) = (uint16_t)(*(uint16_t *)(v_stack_m108 + 0x58));
loc_0089FBB0:
    result = RtlCopyUnicodeString(v_stack_mF8, v_stack_m108 + 88, (uint32_t)(0x63466F49ULL), (uint8_t)(local_rsi));
    Arg1 = (v_stack_m90) + (result);
    if (Arg1 > 22) goto loc_0089FBF9;
    if (Arg1 >= 22) goto loc_0089FBF9;
    *(uint64_t *)(Arg8 + 0x28) = 0;
    goto loc_0089FBF9;
loc_0089FBDB:
    if ((Arg1 + result * 1) > 22) goto loc_0089FBF9;
    if ((Arg1 + result * 1) >= 22) goto loc_0089FBF9;
    if ((uint8_t)((uint32_t)(v_stack_m144)) == 0) goto loc_0089FB48;
loc_0089FBF9:
    result = Arg1 + result * 1;
    if ((*(uint16_t *)(v_stack_m108 + 0x58)) != 0) {
        Arg2 = 0;
        Arg1 = *(uint64_t *)(v_stack_m108 + 0x60);
        result = ExFreePoolWithTag(Arg1, Arg2, (uint32_t)(0x63466F49ULL), (uint8_t)(local_rsi));
        *(uint16_t *)(v_stack_m108 + 0x58) = 0;
    }
    *(uint64_t *)(v_stack_m108 + 0x8) = 0;
    result = ObfDereferenceObject(v_stack_m108, Arg2, (uint32_t)(0x63466F49ULL), (uint8_t)(local_rsi));
    *(uint64_t *)(Arg8 + 0x8) = 0;
    Arg3 = 0;
    Arg2 = 0;
    result = IopDecrementDeviceObjectRef(v_stack_m138, Arg2, Arg3, (uint8_t)(local_rsi));
    result = v_stack_m118;
    if (v_stack_m118 != 0) {
        Arg1 = v_stack_m118;
        result = IopDereferenceVpbAndFree(Arg1, Arg2, Arg3, (uint8_t)(local_rsi));
    }
    if (v_stack_m90 == 1) goto loc_008A0423;
    *(uint64_t *)(Arg8 + 0x28) = 0;
    if ((v_stack_m90 + result * 1) > 22) goto loc_0089FCB5;
    if ((v_stack_m90 + result * 1) >= 22) goto loc_0089FCB5;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg8 + 0x98))) | (16));
    *(uint32_t *)(Arg8 + 0x98) = (uint32_t)(Arg1);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m138 + 0x48)))) > 36) goto loc_008A06CE;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m138 + 0x48)))) >= 36) goto loc_008A06CE;
loc_0089FCA4:
    if (1 == 0) goto loc_008A0446;
    Arg1 = (uint32_t)((Arg1) | (8));
loc_0089FCAF:
    *(uint32_t *)(Arg8 + 0x98) = (uint32_t)(Arg1);
loc_0089FCB5:
    if ((*(uint8_t *)(Arg8 + 0x88)) != 0) goto loc_008A0817;
    result = *(uint64_t *)(v_stack_m138 + 0x138);
    if (((*(uint32_t *)(*(uint64_t *)(v_stack_m138 + 0x138) + 0x20)) & (0x800ULL)) == 0) {
        Arg1 = v_stack_mD0;
        result = *(uint32_t *)(Arg1 + 0x18);
        *(uint32_t *)(Arg1 + 0x10) = (uint32_t)(result);
        *(uint32_t *)(Arg1 + 0x14) = 0;
    }
    if ((v_stack_m90 + result * 1) > 22) goto loc_0089FCFF;
    if ((v_stack_m90 + result * 1) < 22) goto loc_008A0183;
loc_0089FCFF:
    if (v_stack_m90 != ((uint32_t)(0xA0000019ULL))) goto loc_008A016F;
loc_0089FD0D:
    result = PsGetParentSilo(*(uint64_t *)(v_stack_mB8 + 0x8), v_stack_m90, (uint32_t)(0x400201ULL), (uint8_t)(local_rsi));
    *(uint64_t *)(v_stack_mB8 + 0x8) = result;
    goto loc_008A088F;
loc_0089FD2C:
    result = IoFreeIrp(result, v_stack_m90, (uint32_t)(0x400201ULL), (uint8_t)(local_rsi));
    Arg3 = 0;
    Arg2 = 0;
    result = IopDecrementDeviceObjectRef(v_stack_m138, Arg2, Arg3, (uint8_t)(local_rsi));
    if (v_stack_m118 == 0) goto loc_0089F166;
    goto loc_008A085F;
loc_0089FD59:
    if (((*(uint32_t *)(*(uint64_t *)(result + 0x138) + 0x20)) & (0x800ULL)) != 0) goto loc_0089E8F5;
    if ((uint8_t)((uint8_t)(local_rsi)) != 0) goto loc_0089FD7D;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(Arg8 + 0x54)))) & (1)) == 0) goto loc_0089E8F5;
loc_0089FD7D:
    if (0 != 0) goto loc_0089FD8C;
    if ((*(uint16_t *)(Arg3)) == 0) goto loc_0089E8F5;
loc_0089FD8C:
    if (v_stack_m120 != 0) goto loc_0089E8F5;
    v_stack_m110 = 0;
    v_stack_m158 = 0;
    v_stack_m160 = v_stack_m100;
    v_stack_m168 = v_stack_m80;
    v_stack_m170 = v_stack_mF8;
    v_stack_m178 = v_stack_m11C;
    v_stack_m180 = 0;
    v_stack_m188 = (uint32_t)((uint32_t)(*(uint32_t *)(Arg8 + 0x58)));
    result = IopCreateSecurityCheck(v_stack_m138, result, v_stack_mD0, (uint32_t)((uint32_t)(v_stack_m108)));
    if ((uint8_t)(result) == 0) goto loc_0089E9BC;
    goto loc_0089E8F5;
loc_0089FE0F:
    if ((*(uint32_t *)(v_rip + 0x726EFD)) != 0) goto loc_008A0716;
loc_0089FE29:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5A0)))) & (1)) != 0) goto loc_008A059B;
    if ((*(uint32_t *)(v_stack_m108 + 0x9C)) == 0) goto loc_008A0591;
loc_0089FE56:
    result = *(uint64_t *)(gs_base + (0 + 0x188));
    if ((*(uint32_t *)(v_rip + 0x726EC3)) != 0) {
        Arg1 = 1;
        Arg2 = (uint8_t)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, v_stack_m128, (uint32_t)((uint32_t)(v_stack_m108)));
    }
    goto loc_0089FA7F;
loc_0089FE81:
    v_stack_mC0 = *(uint64_t *)(result + 0xA0);
    if (v_stack_m128 == 0) goto loc_0089FEAC;
    result = IopSymlinkGetECP(v_stack_m128, v_stack_mC8, v_stack_m128, (uint32_t)((uint32_t)(v_stack_m108)));
    if (((uint32_t)(result)) != 0xC0000225ULL) goto loc_0089FF1F;
loc_0089FEAC:
    Arg4 = (uint16_t)((*(uint16_t *)(v_stack_mF8)) - (*(uint16_t *)(v_stack_m128)));
    v_stack_m188 = v_stack_mC8;
    result = IopSymlinkCreateECP(result, v_stack_m108, v_stack_mF8, Arg4);
    v_stack_m144 = (uint32_t)(result);
    if (sign_flag) goto loc_008A030F;
    if (v_stack_mE8 != 0) goto loc_0089FF27;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x10))) & (128));
    if (!(condition_is_equal)) {
        Arg2 = *(uint64_t *)(result + 0x70);
        v_stack_mE8 = Arg2;
    }
    result = (uint32_t)(0xC000000DULL);
    if ((uint32_t)(Arg1) != 0) { result = 0; }
    v_stack_m144 = (uint32_t)(result);
loc_0089FF1F:
loc_0089FF27:
    if ((*(uint32_t *)(result + 0x30)) != 260) goto loc_0089ECAA;
    if ((uint32_t)(v_stack_m138) != 0) goto loc_008A05CD;
loc_0089FF45:
    result = IopSymlinkProcessReparse(result, v_stack_m108, v_stack_mC0, (uint8_t)(v_cr8));
    Arg1 = (result) + (*(uint64_t *)(result + 0x38));
    if (Arg1 > 22) goto loc_0089ECAA;
    if (Arg1 >= 22) goto loc_0089ECAA;
    if ((*(uint32_t *)(result + 0x30)) < 0) goto loc_008A0285;
    Arg1 = 0;
    if ((uint16_t)(*(uint16_t *)(v_stack_mC0 + 0x6)) == 0) { Arg1 = 16; }
    result = (uint8_t)(((uint8_t)(v_stack_mB8)) & (239));
    local_rbx = (uint8_t)(((uint8_t)(Arg1)) | ((uint8_t)(result)));
    Arg1 = (*(uint64_t *)(v_stack_m128 + 0x8)) - (*(uint16_t *)(v_stack_mC0 + 0x6));
    if ((uint16_t)(*(uint16_t *)(v_stack_mC0 + 0x6)) == 0) goto loc_0089FFC6;
    if ((*(uint16_t *)(Arg1 + *(uint16_t *)(v_stack_m128) * 1)) != 58) goto loc_008A0285;
loc_0089FFC6:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(Arg8 + 0x40)))) & (65)) != 0) goto loc_008A0285;
    if ((*(uint8_t *)(v_stack_m58)) != 0) goto loc_008A0285;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mC0)))) != ((uint32_t)((uint32_t)(0xA0000003ULL)))) goto loc_008A0261;
loc_0089FFF2:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg8 + 0x40))) | (1));
    goto loc_008A0282;
loc_0089FFFA:
    v_stack_mE0 = v_stack_m110;
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)(v_stack_m108))) | (32));
    v_stack_m130 = 0;
    result = ExAcquireResourceSharedLite(v_rip + 7262834, 1, v_stack_mC0, (uint8_t)(v_cr8));
    result = SeLockSubjectContext(v_cr8 + 32, 1, v_stack_mC0, (uint8_t)(v_cr8));
    result = (*(uint64_t *)(v_rip + 0x726A9D)) + (76);
    v_stack_m160 = v_stack_m130;
    v_stack_m168 = v_stack_m11C;
    v_stack_m170 = 1;
    v_stack_m178 = result;
    v_stack_m180 = v_stack_mE0;
    v_stack_m188 = 0;
    result = SeAccessCheck(*(uint64_t *)(v_stack_m138 + 0x110), v_cr8 + 32, 1, (uint32_t)((uint32_t)(local_rsi)));
    if (v_stack_mE0 != 0) goto loc_008A07F3;
loc_008A00A9:
    result = SeUnlockSubjectContext(v_cr8 + 32, v_stack_mE0, 1, (uint32_t)((uint32_t)(local_rsi)));
    result = ExReleaseResourceLite(v_rip + 7262695, v_stack_mE0, 1, (uint32_t)((uint32_t)(local_rsi)));
    result = KeLeaveCriticalRegionThread(v_stack_m100, v_stack_mE0, 1, (uint32_t)((uint32_t)(local_rsi)));
    local_rsi = (uint8_t)(((uint8_t)(result)) ^ ((uint8_t)(local_rbx)));
    local_rsi = (uint8_t)((local_rsi) & (1));
    local_rbx = (uint8_t)((local_rbx) ^ ((uint8_t)(local_rsi)));
    goto loc_0089E866;
loc_008A00DF:
    v_stack_m130 = *(uint64_t *)(Arg1 + 0x18);
    if (*(uint64_t *)(Arg1 + 0x18) != 0) goto loc_0089E6D0;
    goto loc_0089E6E0;
loc_008A0108:
    if ((*(uint64_t *)(Arg8 + 0x18)) == (*(uint64_t *)(Arg1 + 0x18))) goto loc_008A074F;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m108 + 0x48)))) > 36) goto loc_008A045D;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m108 + 0x48)))) >= 36) goto loc_008A045D;
loc_008A012B:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m108 + 0x48)))) > 54) goto loc_008A0464;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m108 + 0x48)))) >= 54) goto loc_008A0464;
loc_008A0140:
    if (1 == 0) goto loc_008A046B;
loc_008A0148:
    Arg1 = (uint8_t)((*(uint8_t *)(Arg8 + 0x98)) & (8));
    result = IopSymlinkEnforceEnabledTypes(Arg1, 1, *(uint64_t *)(Arg8 + 0xA8), *(uint64_t *)(Arg1 + 0x18));
    v_stack_m144 = (uint32_t)(result);
    if (!sign_flag) goto loc_0089E6A8;
    goto loc_0089F16A;
loc_008A016F:
    if (1 == 2) goto loc_0089FD0D;
    goto loc_008A088F;
loc_008A0183:
    if ((uint8_t)(v_cr8) == 0) goto loc_0089FCFF;
    *(uint64_t *)(Arg8 + 0x18) = v_stack_mC0;
    *(uint32_t *)(Arg8 + 0x10) = 0x8000002DULL;
    goto loc_008A088F;
loc_008A01A9:
    result = IoFreeIrp(v_stack_m138, 1, *(uint64_t *)(Arg8 + 0xA8), *(uint64_t *)(Arg1 + 0x18));
    Arg3 = 0;
    Arg2 = 0;
    result = IopDecrementDeviceObjectRef(v_stack_m138, Arg2, Arg3, *(uint64_t *)(Arg1 + 0x18));
    if (v_stack_m118 != 0) {
        Arg1 = v_stack_m118;
        result = IopDereferenceVpbAndFree(Arg1, Arg2, Arg3, *(uint64_t *)(Arg1 + 0x18));
    }
    *(uint64_t *)(v_stack_m108 + 0x8) = 0;
    if ((*(uint8_t *)(Arg8 + 0x89)) != 0) goto loc_008A044E;
    result = ObfDereferenceObject(v_stack_m108, Arg2, Arg3, *(uint64_t *)(Arg1 + 0x18));
    goto loc_008A088F;
loc_008A01F8:
    if ((*(uint64_t *)(Arg8 + 0x28)) != 0) goto loc_0089E719;
    result = PsGetCurrentServerSilo(v_stack_m108, Arg2, Arg3, *(uint64_t *)(Arg1 + 0x18));
    result = PsGetServerSiloServiceSessionId(result, Arg2, Arg3, *(uint64_t *)(Arg1 + 0x18));
    result = PsGetCurrentProcessSessionId(result, Arg2, Arg3, *(uint64_t *)(Arg1 + 0x18));
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != ((uint32_t)(result))) goto loc_008A022C;
    if ((*(uint32_t *)(v_rip + 0x5C5EFF)) == 0) goto loc_008A0254;
    if (((*(uint32_t *)(Arg8 + 0x40)) & (0x40000ULL)) != 0) goto loc_008A0254;
loc_008A022C:
    result = IopGetDevicePDO(v_stack_m138, Arg2, Arg3, *(uint64_t *)(Arg1 + 0x18));
    if (result == 0) goto loc_008A0254;
    result = IopCheckSessionDeviceAccess(result, Arg2, Arg3, *(uint64_t *)(Arg1 + 0x18));
    if ((uint8_t)(result) == 0) goto loc_008A05FE;
    result = ObfDereferenceObject(result, Arg2, Arg3, *(uint64_t *)(Arg1 + 0x18));
loc_008A0254:
    goto loc_0089E719;
loc_008A0261:
    if (((uint32_t)(result)) != 0xA000000CULL) goto loc_008A0285;
    if ((*(uint32_t *)(v_stack_m128 + 0x10)) < 0) goto loc_0089FFF2;
    if (((uint32_t)(result)) != ((uint32_t)(result))) goto loc_008A0285;
    if (((*(uint32_t *)(v_stack_m128 + 0x10)) & (0x40000000ULL)) == 0) goto loc_008A0285;
    Arg1 = (uint32_t)((result) | (64));
loc_008A0282:
    *(uint32_t *)(Arg8 + 0x40) = (uint32_t)(Arg1);
loc_008A0285:
    if ((uint8_t)(v_stack_m118) != 0) goto loc_0089ECAA;
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_m128, Arg2, Arg3, *(uint64_t *)(Arg1 + 0x18));
    v_stack_mC0 = 0;
    goto loc_0089ECAA;
loc_008A02A5:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m128 + 0x48)))) > 53) goto loc_0089F6EB;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m128 + 0x48)))) < 53) goto loc_0089F6C9;
    goto loc_0089F6EB;
loc_008A02CA:
    result = RtlGetActiveConsoleId(v_stack_m128, Arg2, Arg3, *(uint64_t *)(Arg1 + 0x18));
    result = PsGetCurrentProcessSessionId(v_stack_m128, Arg2, Arg3, *(uint64_t *)(Arg1 + 0x18));
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == ((uint32_t)(result))) goto loc_0089EA71;
    result = PsGetCurrentServerSilo(v_stack_m128, Arg2, Arg3, *(uint64_t *)(Arg1 + 0x18));
    result = PsGetServerSiloServiceSessionId(result, Arg2, Arg3, *(uint64_t *)(Arg1 + 0x18));
    result = PsGetCurrentProcessSessionId(result, Arg2, Arg3, *(uint64_t *)(Arg1 + 0x18));
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == ((uint32_t)(result))) goto loc_0089EA71;
    result = IopAllowRemoteDASD(result, Arg2, Arg3, *(uint64_t *)(Arg1 + 0x18));
    if ((uint8_t)(result) != 0) goto loc_0089EA71;
    goto loc_0089EA74;
loc_008A030F:
    *(uint64_t *)(1 + 0x38) = 0;
    *(uint32_t *)(1 + 0x30) = (uint32_t)((uint32_t)(v_stack_m144));
    goto loc_0089FF1F;
loc_008A0320:
    *(uint32_t *)(Arg8 + 0x10) = 0xC000009AULL;
    goto loc_008A088F;
loc_008A0331:
    result = ExAcquireResourceSharedLite(v_rip + 7262038, 1, Arg3, *(uint64_t *)(Arg1 + 0x18));
    result = SeFastTraverseCheck(*(uint64_t *)(1 + 0x110), v_stack_m118, 32, *(uint64_t *)(Arg1 + 0x18));
    result = (uint8_t)((result) ^ ((uint8_t)(local_rbx)));
    result = (uint8_t)((result) & (1));
    local_rbx = (uint8_t)((local_rbx) ^ ((uint8_t)(result)));
    if ((((uint8_t)((uint8_t)(result))) & (1)) != 0) goto loc_0089EB8F;
    v_stack_m110 = 0;
    result = SeLockSubjectContext(v_stack_m118 + 32, v_stack_m118, 32, *(uint64_t *)(Arg1 + 0x18));
    local_rbx = (uint8_t)((local_rbx) | (32));
    result = (*(uint64_t *)(v_rip + 0x72674F)) + (76);
    Arg3 = (uint8_t)(((uint8_t)(local_rbx)) >> (5));
    Arg3 = (uint8_t)((Arg3) & (1));
    v_stack_m160 = v_stack_m144;
    v_stack_m168 = v_stack_m11C;
    v_stack_m170 = 1;
    v_stack_m178 = result;
    v_stack_m180 = v_stack_m110;
    v_stack_m188 = 0;
    result = SeAccessCheck(*(uint64_t *)(1 + 0x110), v_stack_m118 + 32, Arg3, 32);
    result = (uint8_t)((result) ^ ((uint8_t)(local_rbx)));
    result = (uint8_t)((result) & (1));
    local_rbx = (uint8_t)((local_rbx) ^ ((uint8_t)(result)));
    if (v_stack_m110 == 0) goto loc_0089EB8F;
    result = SeAppendPrivileges(v_stack_m118, v_stack_m110, Arg3, 32);
    result = CmSiFreeMemory(v_stack_m110, v_stack_m110, Arg3, 32);
    goto loc_0089EB8F;
loc_008A041B:
    local_rbx = (uint8_t)((local_rbx) & (127));
    goto loc_0089FA61;
loc_008A0423:
    result = (uint32_t)(((uint32_t)(v_stack_mB0)) + 1);
    v_stack_mB0 = (uint32_t)(result);
    if (((uint32_t)(result)) <= 32) goto loc_008A07CE;
    goto loc_008A088F;
loc_008A0446:
    Arg1 = (uint32_t)((v_stack_m110) & (0xFFFFFFF7ULL));
    goto loc_0089FCAF;
loc_008A044E:
    result = IopDeleteFileObjectExtension(Arg1, v_stack_m110, Arg3, 32);
    goto loc_008A088F;
loc_008A045D:
    Arg2 = 0;
    goto loc_008A012B;
loc_008A0464:
    result = 0;
    goto loc_008A0140;
loc_008A046B:
    if (0 != 0) goto loc_008A0148;
loc_008A0473:
    *(uint32_t *)(Arg8 + 0x10) = 0xC0000278ULL;
    goto loc_008A088F;
loc_008A0484:
    if (*(uint64_t *)(v_stack_m118 + 0x20) == 0) {
        Arg1 = *(uint64_t *)(v_stack_m118 + 0x30);
    }
    result = SeTokenIsAdmin(Arg1, Arg2, Arg3, 32);
    if ((uint8_t)(result) != 0) goto loc_0089EAAF;
    local_rbx = (uint8_t)((local_rbx) & (254));
    v_stack_m144 = 0xC0000022ULL;
    goto loc_0089EB49;
loc_008A04B3:
    if (((*(uint32_t *)(*(uint64_t *)(v_stack_m138 + 0x138) + 0x20)) & (0x800ULL)) != 0) goto loc_0089EC11;
    if (32 != 0) goto loc_008A04D7;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(Arg8 + 0x54)))) & (1)) == 0) goto loc_0089EC11;
loc_008A04D7:
    if (v_stack_m120 != 0) goto loc_0089EC11;
    v_stack_m110 = 0;
    v_stack_m158 = 0;
    v_stack_m160 = v_stack_m100;
    v_stack_m168 = v_stack_m80;
    v_stack_m170 = v_stack_mF8;
    v_stack_m178 = v_stack_m11C;
    v_stack_m180 = 0;
    v_stack_m188 = (uint32_t)((uint32_t)(*(uint32_t *)(Arg8 + 0x58)));
    result = IopCreateSecurityCheck(v_stack_m138, v_stack_m138, v_stack_mD0, (uint32_t)((uint32_t)(v_stack_m108)));
    if ((uint8_t)(result) != 0) goto loc_0089EC11;
    goto loc_0089E9BC;
loc_008A0555:
    result = PsIsServerSilo(*(uint64_t *)(v_stack_mB8 + 0x8), v_stack_m138, v_stack_mD0, (uint32_t)((uint32_t)(v_stack_m108)));
    if ((uint8_t)(result) == 0) goto loc_0089F73A;
    result = IoGetSilo(v_stack_m138, v_stack_m138, v_stack_mD0, (uint32_t)((uint32_t)(v_stack_m108)));
    goto loc_0089F746;
loc_008A057B:
    if (((uint16_t)(result)) >= 248) goto loc_0089F56B;
    goto loc_0089F56B;
loc_008A0591:
    if ((*(uint8_t *)(v_stack_m138 + 0x44)) == 0) goto loc_0089FE56;
loc_008A059B:
    result = 248;
    if ((*(uint32_t *)(v_rip + 0x72677E)) != 0) {
        Arg1 = (uint8_t)(v_cr8);
        Arg2 = (uint8_t)(v_stack_m118);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, v_stack_mD0, (uint32_t)((uint32_t)(v_stack_m108)));
    }
    result = IopCancelAlertedRequest(v_stack_m108 + 152, v_stack_m138, v_stack_mD0, (uint32_t)((uint32_t)(v_stack_m108)));
    goto loc_0089FAA4;
loc_008A05CD:
    if (result == 0) goto loc_0089FF45;
    result = IopCheckAndUpdateStopOnSymlinkEcp(result, (uint32_t)(*(uint32_t *)(v_stack_m138 + 0x38)), (uint32_t)((uint32_t)(result)), (uint32_t)((uint32_t)(v_stack_m108)));
    goto loc_0089FF45;
loc_008A05EE:
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(v_stack_m138 + 0x18), Arg2, (uint32_t)((uint32_t)(result)), (uint32_t)((uint32_t)(v_stack_m108)));
    goto loc_0089ED37;
loc_008A05FE:
    result = ObfDereferenceObject(*(uint64_t *)(v_stack_m138 + 0x18), Arg2, (uint32_t)((uint32_t)(result)), (uint32_t)((uint32_t)(v_stack_m108)));
    Arg3 = 0;
    Arg2 = 0;
    result = IopDecrementDeviceObjectRef(v_stack_m138, Arg2, Arg3, (uint32_t)((uint32_t)(v_stack_m108)));
    *(uint32_t *)(Arg8 + 0x10) = 0xC0000022ULL;
    goto loc_008A088F;
loc_008A0621:
    result = IopDeleteFileObjectExtension(v_stack_m108, Arg2, Arg3, (uint32_t)((uint32_t)(v_stack_m108)));
    Arg3 = 0;
    Arg2 = 0;
    result = IopDecrementDeviceObjectRef(v_stack_m138, Arg2, Arg3, (uint32_t)((uint32_t)(v_stack_m108)));
    if (v_stack_m118 != 0) {
        Arg1 = v_stack_m118;
        result = IopDereferenceVpbAndFree(Arg1, Arg2, Arg3, (uint32_t)((uint32_t)(v_stack_m108)));
    }
    result = IoFreeIrp(v_stack_m138, Arg2, Arg3, (uint32_t)((uint32_t)(v_stack_m108)));
    goto loc_008A088F;
loc_008A065F:
    result = (uint32_t)(0xC000009AULL);
    if ((*(uint16_t *)(v_stack_m108 + 0x58)) != 0) {
        Arg2 = 0;
        Arg1 = *(uint64_t *)(v_stack_m108 + 0x60);
        result = ExFreePoolWithTag(Arg1, Arg2, Arg3, (uint32_t)((uint32_t)(v_stack_m108)));
    }
    result = IopDeleteFileObjectExtension(v_stack_m108, Arg2, Arg3, (uint32_t)((uint32_t)(v_stack_m108)));
    Arg3 = 0;
    Arg2 = 0;
    result = IopDecrementDeviceObjectRef(v_stack_m108, Arg2, Arg3, (uint32_t)((uint32_t)(v_stack_m108)));
    if (v_stack_m118 == 0) goto loc_0089FA2C;
    goto loc_0089FA27;
loc_008A06A7:
    if (*(uint64_t *)(v_stack_m138 + 0xA0) == 0) goto loc_0089F9EE;
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(v_stack_m138 + 0xA0), Arg2, Arg3, (uint32_t)((uint32_t)(v_stack_m108)));
    *(uint64_t *)(v_stack_m138 + 0xA0) = 0;
    *(uint64_t *)(Arg8 + 0x28) = 0;
    goto loc_0089F9EE;
loc_008A06CE:
    result = 0;
    goto loc_0089FCA4;
loc_008A06D5:
    if ((*(uint64_t *)(v_stack_m108 + 0x10)) == v_stack_m118) goto loc_0089ED78;
    if (*(uint64_t *)(v_stack_m108 + 0x10) != 0) {
        Arg2 = 1;
        result = IopIncrementVpbRefCount(*(uint64_t *)(v_stack_m108 + 0x10), Arg2, Arg3, (uint32_t)((uint32_t)(v_stack_m108)));
    }
    if (v_stack_m118 == 0) goto loc_0089ED78;
    result = IopDereferenceVpbAndFree(v_stack_m118, Arg2, Arg3, (uint32_t)((uint32_t)(v_stack_m108)));
    goto loc_0089ED78;
loc_008A070C:
    *(uint8_t *)(v_stack_m118) = 19;
    goto loc_0089F4C0;
loc_008A0716:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(v_stack_m118), (uint8_t)(result), Arg3, (uint32_t)((uint32_t)(v_stack_m108)));
    goto loc_0089FE29;
loc_008A0727:
    goto loc_0089EE04;
loc_008A072F:
    result = MmIsDriverVerifying(v_stack_m118, (uint8_t)(result), Arg3, (uint32_t)((uint32_t)(v_stack_m108)));
    if ((uint32_t)(result) == 0) goto loc_0089F045;
    result = VfFastIoSnapState(v_stack_m118, (uint8_t)(result), Arg3, (uint32_t)((uint32_t)(v_stack_m108)));
    goto loc_0089F048;
loc_008A074F:
    if (((uint32_t)(v_stack_m118)) > 36) goto loc_008A0473;
    if (((uint32_t)(v_stack_m118)) < 36) goto loc_0089E6A8;
    *(uint32_t *)(Arg8 + 0x10) = 0xC0000278ULL;
    goto loc_008A088F;
loc_008A0773:
    if (((uint32_t)((uint32_t)(0xC0000278ULL))) != 0xC0000002ULL) goto loc_0089EF44;
    goto loc_0089F0B7;
loc_008A0783:
    v_stack_m40 = v_xmm0;
    v_stack_m40 = v_xmm0;
    result = IoSetActivityIdThread(v_stack_m40, (uint8_t)(result), Arg3, (uint32_t)((uint32_t)(v_stack_m108)));
    result = IofCallDriver(v_stack_m130, 0, Arg3, (uint32_t)((uint32_t)(v_stack_m108)));
    result = IoSetActivityIdThread(result, 0, Arg3, (uint32_t)((uint32_t)(v_stack_m108)));
    goto loc_0089F472;
loc_008A07CE:
    goto loc_0089E639;
loc_008A07F3:
    result = SeAppendPrivileges(v_stack_mD0, 0, Arg3, (uint32_t)((uint32_t)(v_stack_m108)));
    result = CmSiFreeMemory(v_stack_mE0, 0, Arg3, (uint32_t)((uint32_t)(v_stack_m108)));
    goto loc_008A00A9;
loc_008A080D:
    goto loc_0089F56B;
loc_008A0817:
    v_stack_m188 = 0;
    result = KeBugCheckEx(249, v_stack_m128, v_stack_m130, v_stack_mF8);
loc_008A0837:
    result = IoFreeIrp(v_stack_mA0, v_stack_m128, v_stack_m130, v_stack_mF8);
    Arg3 = 0;
    Arg2 = 0;
    result = IopDecrementDeviceObjectRef(v_stack_m138, Arg2, Arg3, v_stack_mF8);
    if (v_stack_m118 == 0) goto loc_0089F166;
loc_008A085F:
    goto loc_0089FB27;
loc_008A0867:
    result = IopDereferenceVpbAndFree(v_stack_m118, Arg2, Arg3, v_stack_mF8);
    goto loc_0089F997;
loc_008A0874:
    *(uint32_t *)(Arg8 + 0x20) = 0xBEAA0251ULL;
    *(uint64_t *)(Arg8 + 0x28) = v_stack_m88;
    *(uint32_t *)(Arg8 + 0x10) = 0;
    result = ObfReferenceObject(v_stack_m88, Arg2, Arg3, v_stack_mF8);
    result = 0;
    goto loc_008A088F;
loc_008A088F:
    Arg1 = (v_stack_m30) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, v_stack_mF8);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0089E510&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
