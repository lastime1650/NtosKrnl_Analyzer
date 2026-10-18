# PiProcessNewDeviceNode

- RVA: `0x00A28F20`–`0x00A2A46D` (길이 `5,453` bytes)
- VA: `0x0000000140A28F20`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000AC0FC`
- 디코드: `1,370`개 명령, `5,453/5,453` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **170**; 고유 호출 대상: **77**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **17**

### Outgoing calls
- `0x00A28F70` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00A28FCA` → [McTemplateK0p_EtwWriteTransfer](../../text/4D/McTemplateK0p_EtwWriteTransfer_function_004D2F24.md) (function, `0x004D2F24`)
- `0x00A29028` → [PiPnpRtlBeginOperation](../8E/PiPnpRtlBeginOperation_function_008E033C.md) (function, `0x008E033C`)
- `0x00A29035` → [PipClearDevNodeFlags](../8F/PipClearDevNodeFlags_function_008F9F54.md) (function, `0x008F9F54`)
- `0x00A29045` → [PnpQueryDeviceID](PnpQueryDeviceID_function_00A2B21C.md) (function, `0x00A2B21C`)
- `0x00A2906B` → [PpIrpQueryCapabilities](../8F/PpIrpQueryCapabilities_function_008FAF8C.md) (function, `0x008FAF8C`)
- `0x00A2907A` → [PipClearDevNodeUserFlags](PipClearDevNodeUserFlags_function_00A2ABC4.md) (function, `0x00A2ABC4`)
- `0x00A2909D` → [PipSetDevNodeUserFlags](../8F/PipSetDevNodeUserFlags_function_008FB8FC.md) (function, `0x008FB8FC`)
- `0x00A290BB` → [PpProfileCancelTransitioningDock](../73/PpProfileCancelTransitioningDock_function_007379A0.md) (function, `0x007379A0`)
- `0x00A290DD` → [PnpQueryExtendedAddress](PnpQueryExtendedAddress_function_00A284DC.md) (function, `0x00A284DC`)
- `0x00A290EC` → [PnpQueryDeviceText](../99/PnpQueryDeviceText_function_0099B150.md) (function, `0x0099B150`)
- `0x00A290FC` → [PnpQueryDeviceText](../99/PnpQueryDeviceText_function_0099B150.md) (function, `0x0099B150`)
- `0x00A2910E` → [PnpIrpQueryID](../8F/PnpIrpQueryID_function_008FB714.md) (function, `0x008FB714`)
- `0x00A29138` → [PnpFixupID](PnpFixupID_function_00A2B36C.md) (function, `0x00A2B36C`)
- `0x00A29161` → [PipSetDevNodeProblem](../8F/PipSetDevNodeProblem_function_008FDE0C.md) (function, `0x008FDE0C`)
- `0x00A2917B` → [PipSetDevNodeFlags](../8F/PipSetDevNodeFlags_function_008FC048.md) (function, `0x008FC048`)
- `0x00A29188` → [PnpSetInvalidIDEvent](../73/PnpSetInvalidIDEvent_function_0073832C.md) (function, `0x0073832C`)
- `0x00A29197` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A291D9` → [PipMakeGloballyUniqueId](../A6/PipMakeGloballyUniqueId_function_00A6F428.md) (function, `0x00A6F428`)
- `0x00A291EA` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A2920C` → [PipSetDevNodeProblem](../8F/PipSetDevNodeProblem_function_008FDE0C.md) (function, `0x008FDE0C`)
- `0x00A2921A` → [PipSetDevNodeFlags](../8F/PipSetDevNodeFlags_function_008FC048.md) (function, `0x008FC048`)
- `0x00A29227` → [PnpSetInvalidIDEvent](../73/PnpSetInvalidIDEvent_function_0073832C.md) (function, `0x0073832C`)
- `0x00A2926B` → [PipSetDevNodeProblem](../8F/PipSetDevNodeProblem_function_008FDE0C.md) (function, `0x008FDE0C`)
- `0x00A2927D` → [PiBuildDeviceNodeInstancePath](../A0/PiBuildDeviceNodeInstancePath_function_00A08DEC.md) (function, `0x00A08DEC`)
- `0x00A292AA` → [McTemplateK0pzz_EtwWriteTransfer](../../text/5A/McTemplateK0pzz_EtwWriteTransfer_function_005A6BF8.md) (function, `0x005A6BF8`)
- `0x00A292BC` → [PiCreateDeviceInstanceKey](../8F/PiCreateDeviceInstanceKey_function_008FFA0C.md) (function, `0x008FFA0C`)
- `0x00A292D2` → [PipSetDevNodeProblem](../8F/PipSetDevNodeProblem_function_008FDE0C.md) (function, `0x008FDE0C`)
- `0x00A292FD` → [PpMarkDeviceStackExtensionFlag](../../text/4A/PpMarkDeviceStackExtensionFlag_function_004AD8D0.md) (function, `0x004AD8D0`)
- `0x00A29344` → [PipSetDevNodeState](../../text/47/PipSetDevNodeState_function_00470708.md) (function, `0x00470708`)
- `0x00A29384` → [PnpDeviceObjectFromDeviceInstanceWithTag](../8E/PnpDeviceObjectFromDeviceInstanceWithTag_function_008E7490.md) (function, `0x008E7490`)
- `0x00A293AA` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x00A293CB` → [PipSetDevNodeProblem](../8F/PipSetDevNodeProblem_function_008FDE0C.md) (function, `0x008FDE0C`)
- `0x00A293E1` → [PnpLogDuplicateDevice](../72/PnpLogDuplicateDevice_function_0072D8B4.md) (function, `0x0072D8B4`)
- `0x00A2941A` → [McTemplateK0zzzzz_EtwWriteTransfer](../../text/5A/McTemplateK0zzzzz_EtwWriteTransfer_function_005A6DB0.md) (function, `0x005A6DB0`)
- `0x00A2943C` → [PpvUtilFailDriver](../../text/5A/PpvUtilFailDriver_function_005AA498.md) (function, `0x005AA498`)
- `0x00A29449` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00A2945D` → [PipMakeGloballyUniqueId](../A6/PipMakeGloballyUniqueId_function_00A6F428.md) (function, `0x00A6F428`)
- `0x00A2946E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A29497` → [PpvUtilFailDriver](../../text/5A/PpvUtilFailDriver_function_005AA498.md) (function, `0x005AA498`)
- `0x00A294A4` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00A294B8` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00A294D1` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00A294E2` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00A29510` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00A29520` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00A2952C` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00A29548` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00A29560` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00A29585` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00A295A1` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00A295AD` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00A295BF` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00A295D4` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00A295E5` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00A29605` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00A29615` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00A29621` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00A2963D` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00A29655` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00A2967A` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00A29696` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00A296B0` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00A296BE` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00A296DF` → [PipClearDevNodeProblem](PipClearDevNodeProblem_function_00A27C8C.md) (function, `0x00A27C8C`)
- `0x00A29701` → [PnpClearDeviceTemporaryProperties](../A8/PnpClearDeviceTemporaryProperties_function_00A8F4DC.md) (function, `0x00A8F4DC`)
- `0x00A29752` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00A29797` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00A297D2` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00A2981A` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00A29848` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x00A298A0` → [CmSetDeviceRegProp](../8F/CmSetDeviceRegProp_function_008FD68C.md) (function, `0x008FD68C`)
- `0x00A298AC` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00A298B1` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00A298F5` → [PnpDisableDevice](../72/PnpDisableDevice_function_0072C6FC.md) (function, `0x0072C6FC`)
- `0x00A29942` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x00A2999A` → [CmSetDeviceRegProp](../8F/CmSetDeviceRegProp_function_008FD68C.md) (function, `0x008FD68C`)
- `0x00A299B5` → [PnpSaveDeviceCapabilities](../8F/PnpSaveDeviceCapabilities_function_008FD478.md) (function, `0x008FD478`)
- `0x00A29A04` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00A29A4D` → [CmGetDeviceRegProp](../8E/CmGetDeviceRegProp_function_008ED870.md) (function, `0x008ED870`)
- `0x00A29AD8` → [CmSetDeviceRegProp](../8F/CmSetDeviceRegProp_function_008FD68C.md) (function, `0x008FD68C`)
- `0x00A29AEA` → [PiDevCfgGetFailedInstallProblemStatus](../73/PiDevCfgGetFailedInstallProblemStatus_function_00733730.md) (function, `0x00733730`)
- `0x00A29AFC` → [PipSetDevNodeProblem](../8F/PipSetDevNodeProblem_function_008FDE0C.md) (function, `0x008FDE0C`)
- `0x00A29B09` → [PnpMapDeviceObjectToDeviceInstance](../A9/PnpMapDeviceObjectToDeviceInstance_function_00A9D884.md) (function, `0x00A9D884`)
- `0x00A29B51` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00A29B56` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00A29B6A` → [PnpIrpQueryID](../8F/PnpIrpQueryID_function_008FB714.md) (function, `0x008FB714`)
- `0x00A29B93` → [PnpFixupID](PnpFixupID_function_00A2B36C.md) (function, `0x00A2B36C`)
- `0x00A29BBA` → [PipSetDevNodeProblem](../8F/PipSetDevNodeProblem_function_008FDE0C.md) (function, `0x008FDE0C`)
- `0x00A29BD0` → [PipSetDevNodeFlags](../8F/PipSetDevNodeFlags_function_008FC048.md) (function, `0x008FC048`)
- `0x00A29BDD` → [PnpSetInvalidIDEvent](../73/PnpSetInvalidIDEvent_function_0073832C.md) (function, `0x0073832C`)
- `0x00A29BEC` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A29BFF` → [KseAddHardwareId](../95/KseAddHardwareId_function_00959254.md) (function, `0x00959254`)
- `0x00A29C15` → [PnpIrpQueryID](../8F/PnpIrpQueryID_function_008FB714.md) (function, `0x008FB714`)
- `0x00A29C3E` → [PnpFixupID](PnpFixupID_function_00A2B36C.md) (function, `0x00A2B36C`)
- `0x00A29C68` → [PipSetDevNodeProblem](../8F/PipSetDevNodeProblem_function_008FDE0C.md) (function, `0x008FDE0C`)
- `0x00A29C7E` → [PipSetDevNodeFlags](../8F/PipSetDevNodeFlags_function_008FC048.md) (function, `0x008FC048`)
- `0x00A29C8B` → [PnpSetInvalidIDEvent](../73/PnpSetInvalidIDEvent_function_0073832C.md) (function, `0x0073832C`)
- `0x00A29C9A` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A29CB7` → [PnpGenerateDeviceIdsHash](PnpGenerateDeviceIdsHash_function_00A2B120.md) (function, `0x00A2B120`)
- `0x00A29CC9` → [PnpIrpQueryID](../8F/PnpIrpQueryID_function_008FB714.md) (function, `0x008FB714`)
- `0x00A29CDE` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00A29CEE` → [RtlGUIDFromString](../8F/RtlGUIDFromString_function_008F1EF0.md) (function, `0x008F1EF0`)
- `0x00A29CFC` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A29D16` → [PiQueryRemovableDeviceOverride](PiQueryRemovableDeviceOverride_function_00A2A474.md) (function, `0x00A2A474`)
- `0x00A29D73` → [PipGenerateContainerID](../A8/PipGenerateContainerID_function_00A87694.md) (function, `0x00A87694`)
- `0x00A29D86` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A29DA6` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00A29DB2` → [RtlGUIDFromString](../8F/RtlGUIDFromString_function_008F1EF0.md) (function, `0x008F1EF0`)
- `0x00A29DE3` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x00A29DEE` → [PipSetDevNodeFlags](../8F/PipSetDevNodeFlags_function_008FC048.md) (function, `0x008FC048`)
- `0x00A29DF6` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00A29DFB` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00A29E24` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (function, `0x00214E20`)
- `0x00A29E36` → [PiDcUpdateDeviceContainerMembership](../8F/PiDcUpdateDeviceContainerMembership_function_008FD0A8.md) (function, `0x008FD0A8`)
- `0x00A29E3E` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00A29E43` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00A29E5F` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x00A29EA5` → [PnpCheckDeviceIdsChanged](../97/PnpCheckDeviceIdsChanged_function_00972938.md) (function, `0x00972938`)
- `0x00A29EDC` → [PnpCheckDeviceIdsChanged](../97/PnpCheckDeviceIdsChanged_function_00972938.md) (function, `0x00972938`)
- `0x00A29F2C` → [CmSetDeviceRegProp](../8F/CmSetDeviceRegProp_function_008FD68C.md) (function, `0x008FD68C`)
- `0x00A29F64` → [CmSetDeviceRegProp](../8F/CmSetDeviceRegProp_function_008FD68C.md) (function, `0x008FD68C`)
- `0x00A29F8D` → [PpDevCfgCheckDeviceNeedsUpdate](../73/PpDevCfgCheckDeviceNeedsUpdate_function_007367AC.md) (function, `0x007367AC`)
- `0x00A29FFB` → [CmSetDeviceRegProp](../8F/CmSetDeviceRegProp_function_008FD68C.md) (function, `0x008FD68C`)
- `0x00A2A018` → [PipSetDevNodeProblem](../8F/PipSetDevNodeProblem_function_008FDE0C.md) (function, `0x008FDE0C`)
- `0x00A2A024` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00A2A029` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00A2A071` → [PnpFindAlternateStringData](PnpFindAlternateStringData_function_00A2D4A8.md) (function, `0x00A2D4A8`)
- `0x00A2A0BA` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00A2A0CC` → [PnpGetDeviceLocationStrings](PnpGetDeviceLocationStrings_function_00A286C0.md) (function, `0x00A286C0`)
- `0x00A2A11E` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00A2A128` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A2A132` → [PnpQueryBusInformation](PnpQueryBusInformation_function_00A2AF8C.md) (function, `0x00A2AF8C`)
- `0x00A2A141` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00A2A149` → [PipDmgDestroyIommuExtension](PipDmgDestroyIommuExtension_function_00A2857C.md) (function, `0x00A2857C`)
- `0x00A2A156` → [PiIommuGetInterface](PiIommuGetInterface_function_00A285B0.md) (function, `0x00A285B0`)
- `0x00A2A166` → [PipDmgInitializeIommuExtension](../73/PipDmgInitializeIommuExtension_function_0073C0B8.md) (function, `0x0073C0B8`)
- `0x00A2A171` → [PiIommuPutInterface](../74/PiIommuPutInterface_function_0074026C.md) (function, `0x0074026C`)
- `0x00A2A1C2` → [PpDevCfgProcessDevice](../AB/PpDevCfgProcessDevice_function_00AB6DB0.md) (function, `0x00AB6DB0`)
- `0x00A2A1D4` → [PpDevCfgProcessDeviceOperations](../A9/PpDevCfgProcessDeviceOperations_function_00A97CFC.md) (function, `0x00A97CFC`)
- `0x00A2A1DC` → [PiQueryResourceRequirements](../8F/PiQueryResourceRequirements_function_008FE61C.md) (function, `0x008FE61C`)
- `0x00A2A21E` → [PnpIsDeviceInstanceEnabled](../A7/PnpIsDeviceInstanceEnabled_function_00A75A3C.md) (function, `0x00A75A3C`)
- `0x00A2A23B` → [PnpInitializeSessionId](../A9/PnpInitializeSessionId_function_00A949E4.md) (function, `0x00A949E4`)
- `0x00A2A253` → [PnpInitializeInheritedRestrictedSd](../A7/PnpInitializeInheritedRestrictedSd_function_00A7FB28.md) (function, `0x00A7FB28`)
- `0x00A2A25B` → [PiQueryAndAllocateBootResources](../8F/PiQueryAndAllocateBootResources_function_008FDB10.md) (function, `0x008FDB10`)
- `0x00A2A2AB` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x00A2A2BF` → [PnpSaveDeviceCapabilities](../8F/PnpSaveDeviceCapabilities_function_008FD478.md) (function, `0x008FD478`)
- `0x00A2A2CB` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00A2A2D0` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00A2A2D8` → [PpHotSwapUpdateRemovalPolicy](../A8/PpHotSwapUpdateRemovalPolicy_function_00A85E40.md) (function, `0x00A85E40`)
- `0x00A2A2EB` → [PpDeviceRegistration](../A0/PpDeviceRegistration_function_00A079D4.md) (function, `0x00A079D4`)
- `0x00A2A2FD` → [PipSetDevNodeProblem](../8F/PipSetDevNodeProblem_function_008FDE0C.md) (function, `0x008FDE0C`)
- `0x00A2A332` → [PnpIrpDeviceEnumerated](../../text/4B/PnpIrpDeviceEnumerated_function_004B77D0.md) (function, `0x004B77D0`)
- `0x00A2A342` → [PiUpdateDevicePanel](../8F/PiUpdateDevicePanel_function_008FBD4C.md) (function, `0x008FBD4C`)
- `0x00A2A356` → [PnpRaiseNtPlugPlayDevicePropertyChangeEvent](../8F/PnpRaiseNtPlugPlayDevicePropertyChangeEvent_function_008F7D80.md) (function, `0x008F7D80`)
- `0x00A2A365` → [PnpRaiseNtPlugPlayDevicePropertyChangeEvent](../8F/PnpRaiseNtPlugPlayDevicePropertyChangeEvent_function_008F7D80.md) (function, `0x008F7D80`)
- `0x00A2A374` → [PnpSetPlugPlayEvent](../8F/PnpSetPlugPlayEvent_function_008FBE04.md) (function, `0x008FBE04`)
- `0x00A2A37C` → [PnpNewDeviceNodeDependencyCheck](../A0/PnpNewDeviceNodeDependencyCheck_function_00A062A0.md) (function, `0x00A062A0`)
- `0x00A2A38B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A2A39A` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A2A3AA` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A2A3B7` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x00A2A3C7` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A2A3D7` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A2A3E6` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A2A3F6` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A2A404` → [PiPnpRtlEndOperation](../8E/PiPnpRtlEndOperation_function_008E0518.md) (function, `0x008E0518`)
- `0x00A2A41F` → [McTemplateK0p_EtwWriteTransfer](../../text/4D/McTemplateK0p_EtwWriteTransfer_function_004D2F24.md) (function, `0x004D2F24`)
- `0x00A2A435` → [PnpTraceDockDeviceEnumeration](../73/PnpTraceDockDeviceEnumeration_function_0073CA88.md) (function, `0x0073CA88`)
- `0x00A2A446` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PiProcessNewDeviceNodeWorker](../72/PiProcessNewDeviceNodeWorker_function_0072D4C0.md) at `0x0072D4D5`
- [PiProcessNewDeviceNodeAsync](PiProcessNewDeviceNodeAsync_function_00A28EA8.md) at `0x00A28EE9`

### Static image references
- `0x00A28F46` → RVA `0x00E0A740` (`.data`; read)
- `0x00A28F75` → RVA `0x00EF012B` (`.data`; read)
- `0x00A28FC0` → RVA `0x00026E60` (`.rdata`; read)
- `0x00A291C1` → RVA `0x00F8C438` (`.data`; read)
- `0x00A2972D` → RVA `0x00E66398` (`.data`; read)
- `0x00A29739` → RVA `0x00011F50` (`.rdata`; read)
- `0x00A2977E` → RVA `0x00027C98` (`.rdata`; read)
- `0x00A297A0` → RVA `0x00014D78` (`.rdata`; read)
- `0x00A297DB` → RVA `0x00E66268` (`.data`; read)
- `0x00A29801` → RVA `0x000212D0` (`.rdata`; read)
- `0x00A2982D` → RVA `0x00F8C600` (`.data`; read)
- `0x00A299EB` → RVA `0x00027CB0` (`.rdata`; read)
- `0x00A29B17` → RVA `0x00E0A9E0` (`.data`; read)
- `0x00A2A0A5` → RVA `0x00027C80` (`.rdata`; read)
- `0x00A2A0FA` → RVA `0x000116A0` (`.rdata`; read)
- `0x00A2A36D` → RVA `0x00011610` (`.rdata`; read)
- `0x00A2A415` → RVA `0x000274C0` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **74**
  - `0x00A28F70` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00A28FCA` → [McTemplateK0p_EtwWriteTransfer](../../text/4D/McTemplateK0p_EtwWriteTransfer_function_004D2F24.md) (`PAGE` → `.text`)
  - `0x00A29197` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A291EA` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A292AA` → [McTemplateK0pzz_EtwWriteTransfer](../../text/5A/McTemplateK0pzz_EtwWriteTransfer_function_005A6BF8.md) (`PAGE` → `.text`)
  - `0x00A292FD` → [PpMarkDeviceStackExtensionFlag](../../text/4A/PpMarkDeviceStackExtensionFlag_function_004AD8D0.md) (`PAGE` → `.text`)
  - `0x00A29344` → [PipSetDevNodeState](../../text/47/PipSetDevNodeState_function_00470708.md) (`PAGE` → `.text`)
  - `0x00A293AA` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x00A2941A` → [McTemplateK0zzzzz_EtwWriteTransfer](../../text/5A/McTemplateK0zzzzz_EtwWriteTransfer_function_005A6DB0.md) (`PAGE` → `.text`)
  - `0x00A2943C` → [PpvUtilFailDriver](../../text/5A/PpvUtilFailDriver_function_005AA498.md) (`PAGE` → `.text`)
  - `0x00A29449` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00A2946E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A29497` → [PpvUtilFailDriver](../../text/5A/PpvUtilFailDriver_function_005AA498.md) (`PAGE` → `.text`)
  - `0x00A294A4` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00A294B8` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00A294D1` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00A294E2` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00A29510` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00A29520` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00A2952C` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00A29548` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00A29560` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00A29585` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00A295A1` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00A295AD` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00A295BF` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00A295D4` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00A295E5` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00A29605` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00A29615` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00A29621` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00A2963D` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00A29655` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00A2967A` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00A29696` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00A296B0` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x00A296BE` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00A29848` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x00A298AC` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00A298B1` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00A29942` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x00A29B51` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00A29B56` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00A29BEC` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A29C9A` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A29CDE` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00A29CFC` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A29D86` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A29DA6` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00A29DE3` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x00A29DF6` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00A29DFB` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00A29E24` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (`PAGE` → `.text`)
  - `0x00A29E3E` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00A29E43` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00A29E5F` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x00A2A024` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00A2A029` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00A2A128` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A2A141` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00A2A2AB` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x00A2A2CB` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00A2A2D0` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00A2A332` → [PnpIrpDeviceEnumerated](../../text/4B/PnpIrpDeviceEnumerated_function_004B77D0.md) (`PAGE` → `.text`)
  - `0x00A2A38B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A2A39A` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A2A3AA` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A2A3B7` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x00A2A3C7` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A2A3D7` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A2A3E6` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A2A3F6` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A2A41F` → [McTemplateK0p_EtwWriteTransfer](../../text/4D/McTemplateK0p_EtwWriteTransfer_function_004D2F24.md) (`PAGE` → `.text`)
  - `0x00A2A446` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A28F20  48 8B C4                        mov rax, rsp
00A28F23  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
00A28F27  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
00A28F2B  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
00A28F2F  55                              push rbp
00A28F30  41 54                           push r12
00A28F32  41 55                           push r13
00A28F34  41 56                           push r14
00A28F36  41 57                           push r15
00A28F38  48 8D A8 18 FF FF FF            lea rbp, [rax - 0xe8]
00A28F3F  48 81 EC C0 01 00 00            sub rsp, 0x1c0
00A28F46  48 8B 05 F3 17 3E 00            mov rax, qword ptr [rip + 0x3e17f3]
00A28F4D  48 33 C4                        xor rax, rsp
00A28F50  48 89 85 B0 00 00 00            mov qword ptr [rbp + 0xb0], rax
00A28F57  45 33 E4                        xor r12d, r12d
00A28F5A  48 8B F9                        mov rdi, rcx
00A28F5D  33 D2                           xor edx, edx
00A28F5F  4C 89 65 A0                     mov qword ptr [rbp - 0x60], r12
00A28F63  48 8D 4D 60                     lea rcx, [rbp + 0x60]
00A28F67  4C 89 65 E0                     mov qword ptr [rbp - 0x20], r12
00A28F6B  45 8D 44 24 40                  lea r8d, [r12 + 0x40]
00A28F70  E8 CB DC C9 FF                  call 0x1406c6c40
00A28F75  F6 05 AF 71 4C 00 10            test byte ptr [rip + 0x4c71af], 0x10
00A28F7C  0F 57 C0                        xorps xmm0, xmm0
00A28F7F  0F 11 85 A0 00 00 00            movups xmmword ptr [rbp + 0xa0], xmm0
00A28F86  4C 89 65 A8                     mov qword ptr [rbp - 0x58], r12
00A28F8A  0F 11 45 F8                     movups xmmword ptr [rbp - 8], xmm0
00A28F8E  4C 89 65 C8                     mov qword ptr [rbp - 0x38], r12
00A28F92  4C 89 65 88                     mov qword ptr [rbp - 0x78], r12
00A28F96  4C 89 65 F0                     mov qword ptr [rbp - 0x10], r12
00A28F9A  4C 89 65 B0                     mov qword ptr [rbp - 0x50], r12
00A28F9E  4C 89 65 B8                     mov qword ptr [rbp - 0x48], r12
00A28FA2  4C 89 65 D8                     mov qword ptr [rbp - 0x28], r12
00A28FA6  4C 89 65 E8                     mov qword ptr [rbp - 0x18], r12
00A28FAA  44 89 65 90                     mov dword ptr [rbp - 0x70], r12d
00A28FAE  44 89 65 C0                     mov dword ptr [rbp - 0x40], r12d
00A28FB2  44 88 64 24 58                  mov byte ptr [rsp + 0x58], r12b
00A28FB7  4C 89 65 80                     mov qword ptr [rbp - 0x80], r12
00A28FBB  74 12                           je 0x140a28fcf
00A28FBD  4C 8B CF                        mov r9, rdi
00A28FC0  48 8D 15 99 DE 5F FF            lea rdx, [rip - 0xa02167]
00A28FC7  45 33 C0                        xor r8d, r8d
00A28FCA  E8 55 9F AA FF                  call 0x1404d2f24
00A28FCF  48 B8 14 00 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000014
00A28FD9  44 88 65 94                     mov byte ptr [rbp - 0x6c], r12b
00A28FDD  48 8D 4D F0                     lea rcx, [rbp - 0x10]
00A28FE1  44 88 64 24 50                  mov byte ptr [rsp + 0x50], r12b
00A28FE6  44 89 65 98                     mov dword ptr [rbp - 0x68], r12d
00A28FEA  41 8B F4                        mov esi, r12d
00A28FED  44 89 64 24 68                  mov dword ptr [rsp + 0x68], r12d
00A28FF2  48 8B 00                        mov rax, qword ptr [rax]
00A28FF5  4C 8B 6F 20                     mov r13, qword ptr [rdi + 0x20]
00A28FF9  48 89 45 08                     mov qword ptr [rbp + 8], rax
00A28FFD  49 8B C4                        mov rax, r12
00A29000  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
00A29005  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
00A2900A  44 89 64 24 54                  mov dword ptr [rsp + 0x54], r12d
00A2900F  44 89 64 24 6C                  mov dword ptr [rsp + 0x6c], r12d
00A29014  44 89 64 24 5C                  mov dword ptr [rsp + 0x5c], r12d
00A29019  44 89 64 24 64                  mov dword ptr [rsp + 0x64], r12d
00A2901E  44 88 64 24 51                  mov byte ptr [rsp + 0x51], r12b
00A29023  44 89 64 24 60                  mov dword ptr [rsp + 0x60], r12d
00A29028  E8 0F 73 EB FF                  call 0x1408e033c
00A2902D  BA 00 00 00 02                  mov edx, 0x2000000
00A29032  48 8B CF                        mov rcx, rdi
00A29035  E8 1A 0F ED FF                  call 0x1408f9f54
00A2903A  4C 8D 45 88                     lea r8, [rbp - 0x78]
00A2903E  48 8B CF                        mov rcx, rdi
00A29041  48 8D 55 E0                     lea rdx, [rbp - 0x20]
00A29045  E8 D2 21 00 00                  call 0x140a2b21c
00A2904A  85 C0                           test eax, eax
00A2904C  79 16                           jns 0x140a29064
00A2904E  3D 38 00 04 C0                  cmp eax, 0xc0040038
00A29053  44 8B F0                        mov r14d, eax
00A29056  B9 01 00 00 C0                  mov ecx, 0xc0000001
00A2905B  44 0F 44 F1                     cmove r14d, ecx
00A2905F  44 89 74 24 64                  mov dword ptr [rsp + 0x64], r14d
00A29064  48 8D 55 60                     lea rdx, [rbp + 0x60]
00A29068  49 8B CD                        mov rcx, r13
00A2906B  E8 1C 1F ED FF                  call 0x1408faf8c
00A29070  BA 02 00 00 00                  mov edx, 2
00A29075  48 8B CF                        mov rcx, rdi
00A29078  8B D8                           mov ebx, eax
00A2907A  E8 45 1B 00 00                  call 0x140a2abc4
00A2907F  8B 45 64                        mov eax, dword ptr [rbp + 0x64]
00A29082  41 BE 01 00 00 00               mov r14d, 1
00A29088  45 0F B6 FC                     movzx r15d, r12b
00A2908C  85 DB                           test ebx, ebx
00A2908E  78 1B                           js 0x140a290ab
00A29090  0F BA E0 11                     bt eax, 0x11
00A29094  73 0F                           jae 0x140a290a5
00A29096  41 8D 56 01                     lea edx, [r14 + 1]
00A2909A  48 8B CF                        mov rcx, rdi
00A2909D  E8 5A 28 ED FF                  call 0x1408fb8fc
00A290A2  8B 45 64                        mov eax, dword ptr [rbp + 0x64]
00A290A5  A8 40                           test al, 0x40
00A290A7  45 0F 45 FE                     cmovne r15d, r14d
00A290AB  A8 20                           test al, 0x20
00A290AD  74 16                           je 0x140a290c5
00A290AF  83 BF 38 02 00 00 04            cmp dword ptr [rdi + 0x238], 4
00A290B6  75 08                           jne 0x140a290c0
00A290B8  48 8B CF                        mov rcx, rdi
00A290BB  E8 E0 E8 D0 FF                  call 0x1407379a0
00A290C0  41 8B C6                        mov eax, r14d
00A290C3  EB 03                           jmp 0x140a290c8
00A290C5  41 8B C4                        mov eax, r12d
00A290C8  89 87 38 02 00 00               mov dword ptr [rdi + 0x238], eax
00A290CE  48 8D 55 D0                     lea rdx, [rbp - 0x30]
00A290D2  48 83 C8 FF                     or rax, 0xffffffffffffffff
00A290D6  49 8B CD                        mov rcx, r13
00A290D9  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
00A290DD  E8 FA F3 FF FF                  call 0x140a284dc
00A290E2  48 8B 4F 20                     mov rcx, qword ptr [rdi + 0x20]
00A290E6  4C 8D 4D C8                     lea r9, [rbp - 0x38]
00A290EA  33 D2                           xor edx, edx
00A290EC  E8 5F 20 F7 FF                  call 0x14099b150
00A290F1  48 8B 4F 20                     mov rcx, qword ptr [rdi + 0x20]
00A290F5  4C 8D 4D D8                     lea r9, [rbp - 0x28]
00A290F9  41 8B D6                        mov edx, r14d
00A290FC  E8 4F 20 F7 FF                  call 0x14099b150
00A29101  48 8B 4F 20                     mov rcx, qword ptr [rdi + 0x20]
00A29105  4C 8D 45 B8                     lea r8, [rbp - 0x48]
00A29109  BA 03 00 00 00                  mov edx, 3
00A2910E  E8 01 26 ED FF                  call 0x1408fb714
00A29113  4C 8B 75 B8                     mov r14, qword ptr [rbp - 0x48]
00A29117  8B D8                           mov ebx, eax
00A29119  85 C0                           test eax, eax
00A2911B  78 2B                           js 0x140a29148
00A2911D  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
00A29121  45 33 C9                        xor r9d, r9d
00A29124  48 83 C0 38                     add rax, 0x38
00A29128  45 33 C0                        xor r8d, r8d
00A2912B  BA C8 00 00 00                  mov edx, 0xc8
00A29130  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A29135  49 8B CE                        mov rcx, r14
00A29138  E8 2F 22 00 00                  call 0x140a2b36c
00A2913D  03 C0                           add eax, eax
00A2913F  75 62                           jne 0x140a291a3
00A29141  BB 38 00 04 C0                  mov ebx, 0xc0040038
00A29146  EB 0E                           jmp 0x140a29156
00A29148  3D 38 00 04 C0                  cmp eax, 0xc0040038
00A2914D  74 07                           je 0x140a29156
00A2914F  3D 9A 00 00 C0                  cmp eax, 0xc000009a
00A29154  75 37                           jne 0x140a2918d
00A29156  44 8B C3                        mov r8d, ebx
00A29159  BA 09 00 00 00                  mov edx, 9
00A2915E  48 8B CF                        mov rcx, rdi
00A29161  E8 A6 4C ED FF                  call 0x1408fde0c
00A29166  48 8B 4F 10                     mov rcx, qword ptr [rdi + 0x10]
00A2916A  F7 81 8C 01 00 00 00 00 20 00   test dword ptr [rcx + 0x18c], 0x200000
00A29174  75 17                           jne 0x140a2918d
00A29176  BA 00 00 20 00                  mov edx, 0x200000
00A2917B  E8 C8 2E ED FF                  call 0x1408fc048
00A29180  48 8B 4F 10                     mov rcx, qword ptr [rdi + 0x10]
00A29184  48 83 C1 28                     add rcx, 0x28
00A29188  E8 9F F1 D0 FF                  call 0x14073832c
00A2918D  4D 85 F6                        test r14, r14
00A29190  74 11                           je 0x140a291a3
00A29192  33 D2                           xor edx, edx
00A29194  49 8B CE                        mov rcx, r14
00A29197  E8 D4 96 15 00                  call 0x140b82870
00A2919C  4D 8B F4                        mov r14, r12
00A2919F  4C 89 65 B8                     mov qword ptr [rbp - 0x48], r12
00A291A3  45 84 FF                        test r15b, r15b
00A291A6  75 51                           jne 0x140a291f9
00A291A8  F7 87 8C 01 00 00 00 20 00 00   test dword ptr [rdi + 0x18c], 0x2000
00A291B2  74 09                           je 0x140a291bd
00A291B4  83 BF 94 01 00 00 09            cmp dword ptr [rdi + 0x194], 9
00A291BB  74 6F                           je 0x140a2922c
00A291BD  48 8B 4F 10                     mov rcx, qword ptr [rdi + 0x10]
00A291C1  48 3B 0D 70 32 56 00            cmp rcx, qword ptr [rip + 0x563270]
00A291C8  74 62                           je 0x140a2922c
00A291CA  48 8B 49 20                     mov rcx, qword ptr [rcx + 0x20]
00A291CE  4C 8D 45 80                     lea r8, [rbp - 0x80]
00A291D2  49 8B D6                        mov rdx, r14
00A291D5  4C 89 65 80                     mov qword ptr [rbp - 0x80], r12
00A291D9  E8 4A 62 04 00                  call 0x140a6f428
00A291DE  8B D8                           mov ebx, eax
00A291E0  4D 85 F6                        test r14, r14
00A291E3  74 0A                           je 0x140a291ef
00A291E5  33 D2                           xor edx, edx
00A291E7  49 8B CE                        mov rcx, r14
00A291EA  E8 81 96 15 00                  call 0x140b82870
00A291EF  4C 8B 75 80                     mov r14, qword ptr [rbp - 0x80]
00A291F3  4C 89 75 B8                     mov qword ptr [rbp - 0x48], r14
00A291F7  EB 33                           jmp 0x140a2922c
00A291F9  41 B8 BB 00 00 C0               mov r8d, 0xc00000bb
00A291FF  41 3B D8                        cmp ebx, r8d
00A29202  75 28                           jne 0x140a2922c
00A29204  BA 09 00 00 00                  mov edx, 9
00A29209  48 8B CF                        mov rcx, rdi
00A2920C  E8 FB 4B ED FF                  call 0x1408fde0c
00A29211  48 8B 4F 10                     mov rcx, qword ptr [rdi + 0x10]
00A29215  BA 00 00 20 00                  mov edx, 0x200000
00A2921A  E8 29 2E ED FF                  call 0x1408fc048
00A2921F  48 8B 4F 10                     mov rcx, qword ptr [rdi + 0x10]
00A29223  48 83 C1 28                     add rcx, 0x28
00A29227  E8 00 F1 D0 FF                  call 0x14073832c
00A2922C  4C 8B 65 E0                     mov r12, qword ptr [rbp - 0x20]
00A29230  85 DB                           test ebx, ebx
00A29232  79 3C                           jns 0x140a29270
00A29234  F7 87 8C 01 00 00 00 20 00 00   test dword ptr [rdi + 0x18c], 0x2000
00A2923E  89 5C 24 64                     mov dword ptr [rsp + 0x64], ebx
00A29242  74 09                           je 0x140a2924d
00A29244  83 BF 94 01 00 00 09            cmp dword ptr [rdi + 0x194], 9
00A2924B  74 23                           je 0x140a29270
00A2924D  B8 9A 00 00 C0                  mov eax, 0xc000009a
00A29252  48 8B CF                        mov rcx, rdi
00A29255  3B D8                           cmp ebx, eax
00A29257  75 0A                           jne 0x140a29263
00A29259  44 8B C0                        mov r8d, eax
00A2925C  BA 03 00 00 00                  mov edx, 3
00A29261  EB 08                           jmp 0x140a2926b
00A29263  44 8B C3                        mov r8d, ebx
00A29266  BA 13 00 00 00                  mov edx, 0x13
00A2926B  E8 9C 4B ED FF                  call 0x1408fde0c
00A29270  4C 8B 45 88                     mov r8, qword ptr [rbp - 0x78]
00A29274  4D 8B CE                        mov r9, r14
00A29277  49 8B D4                        mov rdx, r12
00A2927A  48 8B CF                        mov rcx, rdi
00A2927D  E8 6A FB FD FF                  call 0x140a08dec
00A29282  8B D8                           mov ebx, eax
00A29284  85 C0                           test eax, eax
00A29286  78 61                           js 0x140a292e9
00A29288  F6 05 9C 6E 4C 00 10            test byte ptr [rip + 0x4c6e9c], 0x10
00A2928F  74 1E                           je 0x140a292af
00A29291  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
00A29295  4C 8B CF                        mov r9, rdi
00A29298  48 8B 48 30                     mov rcx, qword ptr [rax + 0x30]
00A2929C  48 8B 47 30                     mov rax, qword ptr [rdi + 0x30]
00A292A0  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
00A292A5  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A292AA  E8 49 D9 B7 FF                  call 0x1405a6bf8
00A292AF  4C 8D 44 24 5C                  lea r8, [rsp + 0x5c]
00A292B4  48 8B CF                        mov rcx, rdi
00A292B7  48 8D 54 24 70                  lea rdx, [rsp + 0x70]
00A292BC  E8 4B 67 ED FF                  call 0x1408ffa0c
00A292C1  8B D8                           mov ebx, eax
00A292C3  33 C0                           xor eax, eax
00A292C5  85 DB                           test ebx, ebx
00A292C7  79 4B                           jns 0x140a29314
00A292C9  44 8B C3                        mov r8d, ebx
00A292CC  8D 50 13                        lea edx, [rax + 0x13]
00A292CF  48 8B CF                        mov rcx, rdi
00A292D2  E8 35 4B ED FF                  call 0x1408fde0c
00A292D7  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
00A292DC  8B 74 24 5C                     mov esi, dword ptr [rsp + 0x5c]
00A292E0  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
00A292E5  89 74 24 68                     mov dword ptr [rsp + 0x68], esi
00A292E9  89 5C 24 64                     mov dword ptr [rsp + 0x64], ebx
00A292ED  48 8B 5C 24 78                  mov rbx, qword ptr [rsp + 0x78]
00A292F2  41 B0 01                        mov r8b, 1
00A292F5  BA 10 00 00 00                  mov edx, 0x10
00A292FA  49 8B CD                        mov rcx, r13
00A292FD  E8 CE 45 A8 FF                  call 0x1404ad8d0
00A29302  8B 87 2C 01 00 00               mov eax, dword ptr [rdi + 0x12c]
00A29308  3D 01 03 00 00                  cmp eax, 0x301
00A2930D  75 28                           jne 0x140a29337
00A2930F  8D 50 03                        lea edx, [rax + 3]
00A29312  EB 2D                           jmp 0x140a29341
00A29314  8B 74 24 5C                     mov esi, dword ptr [rsp + 0x5c]
00A29318  B9 00 00 02 00                  mov ecx, 0x20000
00A2931D  48 8B 5C 24 70                  mov rbx, qword ptr [rsp + 0x70]
00A29322  83 FE 01                        cmp esi, 1
00A29325  89 74 24 68                     mov dword ptr [rsp + 0x68], esi
00A29329  0F 44 C1                        cmove eax, ecx
00A2932C  48 89 5C 24 78                  mov qword ptr [rsp + 0x78], rbx
00A29331  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
00A29335  EB BB                           jmp 0x140a292f2
00A29337  3D 02 03 00 00                  cmp eax, 0x302
00A2933C  75 0B                           jne 0x140a29349
00A2933E  8D 50 01                        lea edx, [rax + 1]
00A29341  48 8B CF                        mov rcx, rdi
00A29344  E8 BF 73 A4 FF                  call 0x140470708
00A29349  F7 87 8C 01 00 00 00 20 00 00   test dword ptr [rdi + 0x18c], 0x2000
00A29353  74 1D                           je 0x140a29372
00A29355  8B 87 94 01 00 00               mov eax, dword ptr [rdi + 0x194]
00A2935B  83 F8 09                        cmp eax, 9
00A2935E  0F 84 80 03 00 00               je 0x140a296e4
00A29364  83 C0 FD                        add eax, -3
00A29367  A9 EF FF FF FF                  test eax, 0xffffffef
00A2936C  0F 84 72 03 00 00               je 0x140a296e4
00A29372  83 FE 01                        cmp esi, 1
00A29375  0F 84 A9 04 00 00               je 0x140a29824
00A2937B  48 8D 4F 28                     lea rcx, [rdi + 0x28]
00A2937F  BA 50 6E 70 65                  mov edx, 0x65706e50
00A29384  E8 07 E1 EB FF                  call 0x1408e7490
00A29389  48 8B F0                        mov rsi, rax
00A2938C  48 85 C0                        test rax, rax
00A2938F  0F 84 2E 03 00 00               je 0x140a296c3
00A29395  49 3B C5                        cmp rax, r13
00A29398  0F 84 18 03 00 00               je 0x140a296b6
00A2939E  45 84 FF                        test r15b, r15b
00A293A1  0F 84 DD 00 00 00               je 0x140a29484
00A293A7  48 8B CB                        mov rcx, rbx
00A293AA  E8 01 3F C8 FF                  call 0x1406ad2b0
00A293AF  83 65 64 BF                     and dword ptr [rbp + 0x64], 0xffffffbf
00A293B3  33 C9                           xor ecx, ecx
00A293B5  48 89 4C 24 78                  mov qword ptr [rsp + 0x78], rcx
00A293BA  44 8A F9                        mov r15b, cl
00A293BD  48 89 4C 24 70                  mov qword ptr [rsp + 0x70], rcx
00A293C2  45 33 C0                        xor r8d, r8d
00A293C5  8D 51 2A                        lea edx, [rcx + 0x2a]
00A293C8  48 8B CF                        mov rcx, rdi
00A293CB  E8 3C 4A ED FF                  call 0x1408fde0c
00A293D0  48 8B 86 38 01 00 00            mov rax, qword ptr [rsi + 0x138]
00A293D7  49 8B D6                        mov rdx, r14
00A293DA  49 8B CC                        mov rcx, r12
00A293DD  48 8B 58 28                     mov rbx, qword ptr [rax + 0x28]
00A293E1  E8 CE 44 D0 FF                  call 0x14072d8b4
00A293E6  F6 05 3E 6D 4C 00 40            test byte ptr [rip + 0x4c6d3e], 0x40
00A293ED  74 30                           je 0x140a2941f
00A293EF  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
00A293F3  4D 8B CC                        mov r9, r12
00A293F6  48 8B 4B 10                     mov rcx, qword ptr [rbx + 0x10]
00A293FA  48 8B 40 30                     mov rax, qword ptr [rax + 0x30]
00A293FE  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00A29403  48 8B 41 30                     mov rax, qword ptr [rcx + 0x30]
00A29407  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00A2940C  48 8B 45 88                     mov rax, qword ptr [rbp - 0x78]
00A29410  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
00A29415  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A2941A  E8 91 D9 B7 FF                  call 0x1405a6db0
00A2941F  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
00A29423  48 39 43 10                     cmp qword ptr [rbx + 0x10], rax
00A29427  75 18                           jne 0x140a29441
00A29429  49 8B 55 08                     mov rdx, qword ptr [r13 + 8]
00A2942D  4C 8B CE                        mov r9, rsi
00A29430  4D 8B C5                        mov r8, r13
00A29433  33 C9                           xor ecx, ecx
00A29435  48 8B 92 48 01 00 00            mov rdx, qword ptr [rdx + 0x148]
00A2943C  E8 57 10 B8 FF                  call 0x1405aa498
00A29441  BA 50 6E 70 65                  mov edx, 0x65706e50
00A29446  48 8B CE                        mov rcx, rsi
00A29449  E8 92 E4 8C FF                  call 0x1402f78e0
00A2944E  48 8B 4F 10                     mov rcx, qword ptr [rdi + 0x10]
00A29452  4C 8D 45 80                     lea r8, [rbp - 0x80]
00A29456  49 8B D6                        mov rdx, r14
00A29459  48 8B 49 20                     mov rcx, qword ptr [rcx + 0x20]
00A2945D  E8 C6 5F 04 00                  call 0x140a6f428
00A29462  8B D8                           mov ebx, eax
00A29464  4D 85 F6                        test r14, r14
00A29467  74 0A                           je 0x140a29473
00A29469  33 D2                           xor edx, edx
00A2946B  49 8B CE                        mov rcx, r14
00A2946E  E8 FD 93 15 00                  call 0x140b82870
00A29473  4C 8B 75 80                     mov r14, qword ptr [rbp - 0x80]
00A29477  8B 74 24 68                     mov esi, dword ptr [rsp + 0x68]
00A2947B  4C 89 75 B8                     mov qword ptr [rbp - 0x48], r14
00A2947F  E9 AC FD FF FF                  jmp 0x140a29230
00A29484  49 8B 55 08                     mov rdx, qword ptr [r13 + 8]
00A29488  4C 8B CE                        mov r9, rsi
00A2948B  4D 8B C5                        mov r8, r13
00A2948E  33 C9                           xor ecx, ecx
00A29490  48 8B 92 48 01 00 00            mov rdx, qword ptr [rdx + 0x148]
00A29497  E8 FC 0F B8 FF                  call 0x1405aa498
00A2949C  41 0F B7 55 02                  movzx edx, word ptr [r13 + 2]
00A294A1  49 8B CD                        mov rcx, r13
00A294A4  E8 CB EE 9F FF                  call 0x140428374
00A294A9  49 8B 4D 08                     mov rcx, qword ptr [r13 + 8]
00A294AD  33 FF                           xor edi, edi
00A294AF  48 85 C9                        test rcx, rcx
00A294B2  74 35                           je 0x140a294e9
00A294B4  0F BF 51 02                     movsx edx, word ptr [rcx + 2]
00A294B8  E8 B7 EE 9F FF                  call 0x140428374
00A294BD  49 8B 4D 08                     mov rcx, qword ptr [r13 + 8]
00A294C1  44 8D 7F 02                     lea r15d, [rdi + 2]
00A294C5  48 83 C1 38                     add rcx, 0x38
00A294C9  66 39 39                        cmp word ptr [rcx], di
00A294CC  74 21                           je 0x140a294ef
00A294CE  41 8B D7                        mov edx, r15d
00A294D1  E8 9E EE 9F FF                  call 0x140428374
00A294D6  49 8B 4D 08                     mov rcx, qword ptr [r13 + 8]
00A294DA  0F B7 51 38                     movzx edx, word ptr [rcx + 0x38]
00A294DE  48 8B 49 40                     mov rcx, qword ptr [rcx + 0x40]
00A294E2  E8 8D EE 9F FF                  call 0x140428374
00A294E7  EB 06                           jmp 0x140a294ef
00A294E9  41 BF 02 00 00 00               mov r15d, 2
00A294EF  49 8B 85 38 01 00 00            mov rax, qword ptr [r13 + 0x138]
00A294F6  41 BE 88 03 00 00               mov r14d, 0x388
00A294FC  48 8B 48 28                     mov rcx, qword ptr [rax + 0x28]
00A29500  48 85 C9                        test rcx, rcx
00A29503  0F 84 9D 00 00 00               je 0x140a295a6
00A29509  41 8B D6                        mov edx, r14d
00A2950C  48 8D 59 28                     lea rbx, [rcx + 0x28]
00A29510  E8 5F EE 9F FF                  call 0x140428374
00A29515  66 39 3B                        cmp word ptr [rbx], di
00A29518  74 17                           je 0x140a29531
00A2951A  41 8B D7                        mov edx, r15d
00A2951D  48 8B CB                        mov rcx, rbx
00A29520  E8 4F EE 9F FF                  call 0x140428374
00A29525  0F B7 13                        movzx edx, word ptr [rbx]
00A29528  48 8B 4B 08                     mov rcx, qword ptr [rbx + 8]
00A2952C  E8 43 EE 9F FF                  call 0x140428374
00A29531  49 8B 85 38 01 00 00            mov rax, qword ptr [r13 + 0x138]
00A29538  48 8B 48 28                     mov rcx, qword ptr [rax + 0x28]
00A2953C  48 83 C1 38                     add rcx, 0x38
00A29540  66 39 39                        cmp word ptr [rcx], di
00A29543  74 20                           je 0x140a29565
00A29545  41 8B D7                        mov edx, r15d
00A29548  E8 27 EE 9F FF                  call 0x140428374
00A2954D  49 8B 85 38 01 00 00            mov rax, qword ptr [r13 + 0x138]
00A29554  48 8B 48 28                     mov rcx, qword ptr [rax + 0x28]
00A29558  0F B7 51 38                     movzx edx, word ptr [rcx + 0x38]
00A2955C  48 8B 49 40                     mov rcx, qword ptr [rcx + 0x40]
00A29560  E8 0F EE 9F FF                  call 0x140428374
00A29565  49 8B 85 38 01 00 00            mov rax, qword ptr [r13 + 0x138]
00A2956C  48 8B 48 28                     mov rcx, qword ptr [rax + 0x28]
00A29570  48 8B 41 10                     mov rax, qword ptr [rcx + 0x10]
00A29574  48 85 C0                        test rax, rax
00A29577  74 2D                           je 0x140a295a6
00A29579  48 8D 48 38                     lea rcx, [rax + 0x38]
00A2957D  66 39 39                        cmp word ptr [rcx], di
00A29580  74 24                           je 0x140a295a6
00A29582  41 8B D7                        mov edx, r15d
00A29585  E8 EA ED 9F FF                  call 0x140428374
00A2958A  49 8B 85 38 01 00 00            mov rax, qword ptr [r13 + 0x138]
00A29591  48 8B 48 28                     mov rcx, qword ptr [rax + 0x28]
00A29595  48 8B 49 10                     mov rcx, qword ptr [rcx + 0x10]
00A29599  0F B7 51 38                     movzx edx, word ptr [rcx + 0x38]
00A2959D  48 8B 49 40                     mov rcx, qword ptr [rcx + 0x40]
00A295A1  E8 CE ED 9F FF                  call 0x140428374
00A295A6  0F B7 56 02                     movzx edx, word ptr [rsi + 2]
00A295AA  48 8B CE                        mov rcx, rsi
00A295AD  E8 C2 ED 9F FF                  call 0x140428374
00A295B2  48 8B 4E 08                     mov rcx, qword ptr [rsi + 8]
00A295B6  48 85 C9                        test rcx, rcx
00A295B9  74 2F                           je 0x140a295ea
00A295BB  0F BF 51 02                     movsx edx, word ptr [rcx + 2]
00A295BF  E8 B0 ED 9F FF                  call 0x140428374
00A295C4  48 8B 4E 08                     mov rcx, qword ptr [rsi + 8]
00A295C8  48 83 C1 38                     add rcx, 0x38
00A295CC  66 39 39                        cmp word ptr [rcx], di
00A295CF  74 19                           je 0x140a295ea
00A295D1  41 8B D7                        mov edx, r15d
00A295D4  E8 9B ED 9F FF                  call 0x140428374
00A295D9  48 8B 4E 08                     mov rcx, qword ptr [rsi + 8]
00A295DD  0F B7 51 38                     movzx edx, word ptr [rcx + 0x38]
00A295E1  48 8B 49 40                     mov rcx, qword ptr [rcx + 0x40]
00A295E5  E8 8A ED 9F FF                  call 0x140428374
00A295EA  48 8B 86 38 01 00 00            mov rax, qword ptr [rsi + 0x138]
00A295F1  48 8B 48 28                     mov rcx, qword ptr [rax + 0x28]
00A295F5  48 85 C9                        test rcx, rcx
00A295F8  0F 84 9D 00 00 00               je 0x140a2969b
00A295FE  41 8B D6                        mov edx, r14d
00A29601  48 8D 59 28                     lea rbx, [rcx + 0x28]
00A29605  E8 6A ED 9F FF                  call 0x140428374
00A2960A  66 39 3B                        cmp word ptr [rbx], di
00A2960D  74 17                           je 0x140a29626
00A2960F  41 8B D7                        mov edx, r15d
00A29612  48 8B CB                        mov rcx, rbx
00A29615  E8 5A ED 9F FF                  call 0x140428374
00A2961A  0F B7 13                        movzx edx, word ptr [rbx]
00A2961D  48 8B 4B 08                     mov rcx, qword ptr [rbx + 8]
00A29621  E8 4E ED 9F FF                  call 0x140428374
00A29626  48 8B 86 38 01 00 00            mov rax, qword ptr [rsi + 0x138]
00A2962D  48 8B 48 28                     mov rcx, qword ptr [rax + 0x28]
00A29631  48 83 C1 38                     add rcx, 0x38
00A29635  66 39 39                        cmp word ptr [rcx], di
00A29638  74 20                           je 0x140a2965a
00A2963A  41 8B D7                        mov edx, r15d
00A2963D  E8 32 ED 9F FF                  call 0x140428374
00A29642  48 8B 86 38 01 00 00            mov rax, qword ptr [rsi + 0x138]
00A29649  48 8B 48 28                     mov rcx, qword ptr [rax + 0x28]
00A2964D  0F B7 51 38                     movzx edx, word ptr [rcx + 0x38]
00A29651  48 8B 49 40                     mov rcx, qword ptr [rcx + 0x40]
00A29655  E8 1A ED 9F FF                  call 0x140428374
00A2965A  48 8B 86 38 01 00 00            mov rax, qword ptr [rsi + 0x138]
00A29661  48 8B 48 28                     mov rcx, qword ptr [rax + 0x28]
00A29665  48 8B 41 10                     mov rax, qword ptr [rcx + 0x10]
00A29669  48 85 C0                        test rax, rax
00A2966C  74 2D                           je 0x140a2969b
00A2966E  48 8D 48 38                     lea rcx, [rax + 0x38]
00A29672  66 39 39                        cmp word ptr [rcx], di
00A29675  74 24                           je 0x140a2969b
00A29677  41 8B D7                        mov edx, r15d
00A2967A  E8 F5 EC 9F FF                  call 0x140428374
00A2967F  48 8B 86 38 01 00 00            mov rax, qword ptr [rsi + 0x138]
00A29686  48 8B 48 28                     mov rcx, qword ptr [rax + 0x28]
00A2968A  48 8B 49 10                     mov rcx, qword ptr [rcx + 0x10]
00A2968E  0F B7 51 38                     movzx edx, word ptr [rcx + 0x38]
00A29692  48 8B 49 40                     mov rcx, qword ptr [rcx + 0x40]
00A29696  E8 D9 EC 9F FF                  call 0x140428374
00A2969B  4C 8B CE                        mov r9, rsi
00A2969E  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
00A296A3  4D 8B C5                        mov r8, r13
00A296A6  BA 01 00 00 00                  mov edx, 1
00A296AB  B9 CA 00 00 00                  mov ecx, 0xca
00A296B0  E8 AB 3F AD FF                  call 0x1404fd660
00A296B5  CC                              int3
00A296B6  BA 50 6E 70 65                  mov edx, 0x65706e50
00A296BB  48 8B CE                        mov rcx, rsi
00A296BE  E8 1D E2 8C FF                  call 0x1402f78e0
00A296C3  8B 74 24 68                     mov esi, dword ptr [rsp + 0x68]
00A296C7  F7 87 8C 01 00 00 00 20 00 00   test dword ptr [rdi + 0x18c], 0x2000
00A296D1  74 11                           je 0x140a296e4
00A296D3  83 BF 94 01 00 00 2A            cmp dword ptr [rdi + 0x194], 0x2a
00A296DA  75 08                           jne 0x140a296e4
00A296DC  48 8B CF                        mov rcx, rdi
00A296DF  E8 A8 E5 FF FF                  call 0x140a27c8c
00A296E4  45 33 E4                        xor r12d, r12d
00A296E7  45 8D 7C 24 01                  lea r15d, [r12 + 1]
00A296EC  48 85 DB                        test rbx, rbx
00A296EF  0F 84 CE 01 00 00               je 0x140a298c3
00A296F5  41 3B F7                        cmp esi, r15d
00A296F8  74 0C                           je 0x140a29706
00A296FA  48 8B 4F 30                     mov rcx, qword ptr [rdi + 0x30]
00A296FE  48 8B D3                        mov rdx, rbx
00A29701  E8 D6 5D 06 00                  call 0x140a8f4dc
00A29706  48 8B 4F 10                     mov rcx, qword ptr [rdi + 0x10]
00A2970A  4C 8B CB                        mov r9, rbx
00A2970D  44 8B 74 24 60                  mov r14d, dword ptr [rsp + 0x60]
00A29712  45 8B C7                        mov r8d, r15d
00A29715  48 8B 57 30                     mov rdx, qword ptr [rdi + 0x30]
00A29719  44 89 74 24 48                  mov dword ptr [rsp + 0x48], r14d
00A2971E  0F B7 41 28                     movzx eax, word ptr [rcx + 0x28]
00A29722  83 C0 02                        add eax, 2
00A29725  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00A29729  48 8B 41 30                     mov rax, qword ptr [rcx + 0x30]
00A2972D  48 8B 0D 64 CC 43 00            mov rcx, qword ptr [rip + 0x43cc64]
00A29734  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00A29739  48 8D 05 10 88 5E FF            lea rax, [rip - 0xa177f0]
00A29740  C7 44 24 30 12 00 00 00         mov dword ptr [rsp + 0x30], 0x12
00A29748  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A2974D  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
00A29752  E8 91 CF EC FF                  call 0x1408f66e8
00A29757  48 8B 57 30                     mov rdx, qword ptr [rdi + 0x30]
00A2975B  48 8D 45 08                     lea rax, [rbp + 8]
00A2975F  48 8B 0D 32 CC 43 00            mov rcx, qword ptr [rip + 0x43cc32]
00A29766  4C 8B CB                        mov r9, rbx
00A29769  44 89 74 24 48                  mov dword ptr [rsp + 0x48], r14d
00A2976E  45 8B C7                        mov r8d, r15d
00A29771  C7 44 24 40 08 00 00 00         mov dword ptr [rsp + 0x40], 8
00A29779  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00A2977E  48 8D 05 13 E5 5F FF            lea rax, [rip - 0xa01aed]
00A29785  C7 44 24 30 10 00 00 00         mov dword ptr [rsp + 0x30], 0x10
00A2978D  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A29792  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
00A29797  E8 4C CF EC FF                  call 0x1408f66e8
00A2979C  48 8B 57 30                     mov rdx, qword ptr [rdi + 0x30]
00A297A0  48 8D 05 D1 B5 5E FF            lea rax, [rip - 0xa14a2f]
00A297A7  48 8B 0D EA CB 43 00            mov rcx, qword ptr [rip + 0x43cbea]
00A297AE  4C 8B CB                        mov r9, rbx
00A297B1  44 89 74 24 48                  mov dword ptr [rsp + 0x48], r14d
00A297B6  45 8B C7                        mov r8d, r15d
00A297B9  44 89 64 24 40                  mov dword ptr [rsp + 0x40], r12d
00A297BE  4C 89 64 24 38                  mov qword ptr [rsp + 0x38], r12
00A297C3  44 89 64 24 30                  mov dword ptr [rsp + 0x30], r12d
00A297C8  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A297CD  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
00A297D2  E8 11 CF EC FF                  call 0x1408f66e8
00A297D7  48 8B 57 30                     mov rdx, qword ptr [rdi + 0x30]
00A297DB  48 8D 05 86 CA 43 00            lea rax, [rip + 0x43ca86]
00A297E2  48 8B 0D AF CB 43 00            mov rcx, qword ptr [rip + 0x43cbaf]
00A297E9  4C 8B CB                        mov r9, rbx
00A297EC  44 89 74 24 48                  mov dword ptr [rsp + 0x48], r14d
00A297F1  45 8B C7                        mov r8d, r15d
00A297F4  C7 44 24 40 04 00 00 00         mov dword ptr [rsp + 0x40], 4
00A297FC  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00A29801  48 8D 05 C8 7A 5F FF            lea rax, [rip - 0xa08538]
00A29808  C7 44 24 30 07 00 00 00         mov dword ptr [rsp + 0x30], 7
00A29810  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A29815  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
00A2981A  E8 C9 CE EC FF                  call 0x1408f66e8
00A2981F  E9 A4 00 00 00                  jmp 0x140a298c8
00A29824  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00A2982D  48 8D 0D CC 2D 56 00            lea rcx, [rip + 0x562dcc]
00A29834  49 83 CE FF                     or r14, 0xffffffffffffffff
00A29838  66 44 01 B0 E4 01 00 00         add word ptr [rax + 0x1e4], r14w
00A29840  90                              nop
00A29841  41 8D 76 02                     lea esi, [r14 + 2]
00A29845  40 8A D6                        mov dl, sil
00A29848  E8 73 83 7E FF                  call 0x140211bc0
00A2984D  48 8B 5C 24 70                  mov rbx, qword ptr [rsp + 0x70]
00A29852  33 D2                           xor edx, edx
00A29854  48 89 5C 24 78                  mov qword ptr [rsp + 0x78], rbx
00A29859  48 85 DB                        test rbx, rbx
00A2985C  74 47                           je 0x140a298a5
00A2985E  48 8B 4D C8                     mov rcx, qword ptr [rbp - 0x38]
00A29862  48 85 C9                        test rcx, rcx
00A29865  74 3E                           je 0x140a298a5
00A29867  49 8B C6                        mov rax, r14
00A2986A  48 FF C0                        inc rax
00A2986D  66 39 14 41                     cmp word ptr [rcx + rax*2], dx
00A29871  75 F7                           jne 0x140a2986a
00A29873  8B 54 24 60                     mov edx, dword ptr [rsp + 0x60]
00A29877  8D 04 45 02 00 00 00            lea eax, [rax*2 + 2]
00A2987E  89 54 24 38                     mov dword ptr [rsp + 0x38], edx
00A29882  44 8B CE                        mov r9d, esi
00A29885  48 8B 57 30                     mov rdx, qword ptr [rdi + 0x30]
00A29889  4C 8B C3                        mov r8, rbx
00A2988C  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A29890  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
00A29895  48 8B 0D FC CA 43 00            mov rcx, qword ptr [rip + 0x43cafc]
00A2989C  89 74 24 20                     mov dword ptr [rsp + 0x20], esi
00A298A0  E8 E7 3D ED FF                  call 0x1408fd68c
00A298A5  48 8D 0D 54 2D 56 00            lea rcx, [rip + 0x562d54]
00A298AC  E8 5F 61 83 FF                  call 0x14025fa10
00A298B1  E8 FA 3F 83 FF                  call 0x14025d8b0
00A298B6  8B 74 24 5C                     mov esi, dword ptr [rsp + 0x5c]
00A298BA  89 74 24 68                     mov dword ptr [rsp + 0x68], esi
00A298BE  E9 04 FE FF FF                  jmp 0x140a296c7
00A298C3  44 8B 74 24 60                  mov r14d, dword ptr [rsp + 0x60]
00A298C8  F7 45 64 00 40 00 00            test dword ptr [rbp + 0x64], 0x4000
00A298CF  74 29                           je 0x140a298fa
00A298D1  F7 87 8C 01 00 00 00 20 00 00   test dword ptr [rdi + 0x18c], 0x2000
00A298DB  74 10                           je 0x140a298ed
00A298DD  8B 87 94 01 00 00               mov eax, dword ptr [rdi + 0x194]
00A298E3  41 3B C7                        cmp eax, r15d
00A298E6  74 12                           je 0x140a298fa
00A298E8  83 F8 0E                        cmp eax, 0xe
00A298EB  74 0D                           je 0x140a298fa
00A298ED  BA 1D 00 00 00                  mov edx, 0x1d
00A298F2  48 8B CF                        mov rcx, rdi
00A298F5  E8 02 2E D0 FF                  call 0x14072c6fc
00A298FA  F7 87 8C 01 00 00 00 20 00 00   test dword ptr [rdi + 0x18c], 0x2000
00A29904  74 1D                           je 0x140a29923
00A29906  8B 87 94 01 00 00               mov eax, dword ptr [rdi + 0x194]
00A2990C  83 F8 09                        cmp eax, 9
00A2990F  0F 84 46 02 00 00               je 0x140a29b5b
00A29915  83 C0 FD                        add eax, -3
00A29918  A9 EF FF FF FF                  test eax, 0xffffffef
00A2991D  0F 84 38 02 00 00               je 0x140a29b5b
00A29923  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00A2992C  48 8D 0D CD 2C 56 00            lea rcx, [rip + 0x562ccd]
00A29933  48 83 CE FF                     or rsi, 0xffffffffffffffff
00A29937  41 8A D7                        mov dl, r15b
00A2993A  66 01 B0 E4 01 00 00            add word ptr [rax + 0x1e4], si
00A29941  90                              nop
00A29942  E8 79 82 7E FF                  call 0x140211bc0
00A29947  48 8B 5C 24 70                  mov rbx, qword ptr [rsp + 0x70]
00A2994C  48 89 5C 24 78                  mov qword ptr [rsp + 0x78], rbx
00A29951  48 85 DB                        test rbx, rbx
00A29954  74 49                           je 0x140a2999f
00A29956  48 8B 4D D8                     mov rcx, qword ptr [rbp - 0x28]
00A2995A  48 85 C9                        test rcx, rcx
00A2995D  74 40                           je 0x140a2999f
00A2995F  48 8B C6                        mov rax, rsi
00A29962  48 FF C0                        inc rax
00A29965  66 44 39 24 41                  cmp word ptr [rcx + rax*2], r12w
00A2996A  75 F6                           jne 0x140a29962
00A2996C  48 8B 57 30                     mov rdx, qword ptr [rdi + 0x30]
00A29970  8D 04 45 02 00 00 00            lea eax, [rax*2 + 2]
00A29977  44 89 74 24 38                  mov dword ptr [rsp + 0x38], r14d
00A2997C  41 B9 0E 00 00 00               mov r9d, 0xe
00A29982  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A29986  4C 8B C3                        mov r8, rbx
00A29989  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
00A2998E  48 8B 0D 03 CA 43 00            mov rcx, qword ptr [rip + 0x43ca03]
00A29995  44 89 7C 24 20                  mov dword ptr [rsp + 0x20], r15d
00A2999A  E8 ED 3C ED FF                  call 0x1408fd68c
00A2999F  8B 74 24 5C                     mov esi, dword ptr [rsp + 0x5c]
00A299A3  48 8D 55 60                     lea rdx, [rbp + 0x60]
00A299A7  41 3B F7                        cmp esi, r15d
00A299AA  89 74 24 68                     mov dword ptr [rsp + 0x68], esi
00A299AE  48 8B CF                        mov rcx, rdi
00A299B1  41 0F 94 C0                     sete r8b
00A299B5  E8 BE 3A ED FF                  call 0x1408fd478
00A299BA  48 83 C9 FF                     or rcx, 0xffffffffffffffff
00A299BE  48 39 4D D0                     cmp qword ptr [rbp - 0x30], rcx
00A299C2  74 45                           je 0x140a29a09
00A299C4  48 8B 57 30                     mov rdx, qword ptr [rdi + 0x30]
00A299C8  48 8D 45 D0                     lea rax, [rbp - 0x30]
00A299CC  48 8B 0D C5 C9 43 00            mov rcx, qword ptr [rip + 0x43c9c5]
00A299D3  4C 8B CB                        mov r9, rbx
00A299D6  44 89 74 24 48                  mov dword ptr [rsp + 0x48], r14d
00A299DB  45 8B C7                        mov r8d, r15d
00A299DE  C7 44 24 40 08 00 00 00         mov dword ptr [rsp + 0x40], 8
00A299E6  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00A299EB  48 8D 05 BE E2 5F FF            lea rax, [rip - 0xa01d42]
00A299F2  C7 44 24 30 09 00 00 00         mov dword ptr [rsp + 0x30], 9
00A299FA  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A299FF  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
00A29A04  E8 DF CC EC FF                  call 0x1408f66e8
00A29A09  48 8B 57 30                     mov rdx, qword ptr [rdi + 0x30]
00A29A0D  48 8D 45 90                     lea rax, [rbp - 0x70]
00A29A11  48 8B 0D 80 C9 43 00            mov rcx, qword ptr [rip + 0x43c980]
00A29A18  41 3B F7                        cmp esi, r15d
00A29A1B  44 89 64 24 38                  mov dword ptr [rsp + 0x38], r12d
00A29A20  41 B9 0B 00 00 00               mov r9d, 0xb
00A29A26  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00A29A2B  4C 8B C3                        mov r8, rbx
00A29A2E  48 8D 44 24 54                  lea rax, [rsp + 0x54]
00A29A33  C7 45 90 04 00 00 00            mov dword ptr [rbp - 0x70], 4
00A29A3A  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A29A3F  0F 94 44 24 50                  sete byte ptr [rsp + 0x50]
00A29A44  48 8D 45 C0                     lea rax, [rbp - 0x40]
00A29A48  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A29A4D  E8 1E 3E EC FF                  call 0x1408ed870
00A29A52  BE 1C 00 00 00                  mov esi, 0x1c
00A29A57  85 C0                           test eax, eax
00A29A59  78 2A                           js 0x140a29a85
00A29A5B  83 7D C0 04                     cmp dword ptr [rbp - 0x40], 4
00A29A5F  75 24                           jne 0x140a29a85
00A29A61  83 7D 90 04                     cmp dword ptr [rbp - 0x70], 4
00A29A65  75 1E                           jne 0x140a29a85
00A29A67  8B 44 24 54                     mov eax, dword ptr [rsp + 0x54]
00A29A6B  A8 20                           test al, 0x20
00A29A6D  74 0A                           je 0x140a29a79
00A29A6F  8D 56 F6                        lea edx, [rsi - 0xa]
00A29A72  41 84 C7                        test r15b, al
00A29A75  74 18                           je 0x140a29a8f
00A29A77  EB 1B                           jmp 0x140a29a94
00A29A79  A8 40                           test al, 0x40
00A29A7B  0F 84 80 00 00 00               je 0x140a29b01
00A29A81  8B D6                           mov edx, esi
00A29A83  EB 0F                           jmp 0x140a29a94
00A29A85  41 8B C4                        mov eax, r12d
00A29A88  41 8B D7                        mov edx, r15d
00A29A8B  89 44 24 54                     mov dword ptr [rsp + 0x54], eax
00A29A8F  44 88 7C 24 50                  mov byte ptr [rsp + 0x50], r15b
00A29A94  F7 45 64 00 01 00 00            test dword ptr [rbp + 0x64], 0x100
00A29A9B  74 42                           je 0x140a29adf
00A29A9D  48 8B 57 30                     mov rdx, qword ptr [rdi + 0x30]
00A29AA1  0F BA E8 0A                     bts eax, 0xa
00A29AA5  48 8B 0D EC C8 43 00            mov rcx, qword ptr [rip + 0x43c8ec]
00A29AAC  41 B9 0B 00 00 00               mov r9d, 0xb
00A29AB2  44 89 74 24 38                  mov dword ptr [rsp + 0x38], r14d
00A29AB7  4C 8B C3                        mov r8, rbx
00A29ABA  89 44 24 54                     mov dword ptr [rsp + 0x54], eax
00A29ABE  48 8D 44 24 54                  lea rax, [rsp + 0x54]
00A29AC3  C7 44 24 30 04 00 00 00         mov dword ptr [rsp + 0x30], 4
00A29ACB  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A29AD0  C7 44 24 20 04 00 00 00         mov dword ptr [rsp + 0x20], 4
00A29AD8  E8 AF 3B ED FF                  call 0x1408fd68c
00A29ADD  EB 22                           jmp 0x140a29b01
00A29ADF  3B D6                           cmp edx, esi
00A29AE1  75 13                           jne 0x140a29af6
00A29AE3  48 8B 4F 30                     mov rcx, qword ptr [rdi + 0x30]
00A29AE7  48 8B D3                        mov rdx, rbx
00A29AEA  E8 41 9C D0 FF                  call 0x140733730
00A29AEF  44 8B C0                        mov r8d, eax
00A29AF2  8B D6                           mov edx, esi
00A29AF4  EB 03                           jmp 0x140a29af9
00A29AF6  45 33 C0                        xor r8d, r8d
00A29AF9  48 8B CF                        mov rcx, rdi
00A29AFC  E8 0B 43 ED FF                  call 0x1408fde0c
00A29B01  48 8B 4F 20                     mov rcx, qword ptr [rdi + 0x20]
00A29B05  48 8D 57 28                     lea rdx, [rdi + 0x28]
00A29B09  E8 76 3D 07 00                  call 0x140a9d884
00A29B0E  8B 4C 24 64                     mov ecx, dword ptr [rsp + 0x64]
00A29B12  85 C0                           test eax, eax
00A29B14  0F 48 C8                        cmovs ecx, eax
00A29B17  44 38 25 C2 0E 3E 00            cmp byte ptr [rip + 0x3e0ec2], r12b
00A29B1E  89 4C 24 64                     mov dword ptr [rsp + 0x64], ecx
00A29B22  74 11                           je 0x140a29b35
00A29B24  0F BA AF C0 02 00 00 0C         bts dword ptr [rdi + 0x2c0], 0xc
00A29B2C  C7 45 98 02 00 00 00            mov dword ptr [rbp - 0x68], 2
00A29B33  EB 15                           jmp 0x140a29b4a
00A29B35  8B 45 94                        mov eax, dword ptr [rbp - 0x6c]
00A29B38  F7 44 24 54 00 00 04 00         test dword ptr [rsp + 0x54], 0x40000
00A29B40  0F B6 C0                        movzx eax, al
00A29B43  41 0F 45 C7                     cmovne eax, r15d
00A29B47  89 45 94                        mov dword ptr [rbp - 0x6c], eax
00A29B4A  48 8D 0D AF 2A 56 00            lea rcx, [rip + 0x562aaf]
00A29B51  E8 BA 5E 83 FF                  call 0x14025fa10
00A29B56  E8 55 3D 83 FF                  call 0x14025d8b0
00A29B5B  48 8B 4F 20                     mov rcx, qword ptr [rdi + 0x20]
00A29B5F  4C 8D 45 B0                     lea r8, [rbp - 0x50]
00A29B63  41 8B D7                        mov edx, r15d
00A29B66  44 89 65 80                     mov dword ptr [rbp - 0x80], r12d
00A29B6A  E8 A5 1B ED FF                  call 0x1408fb714
00A29B6F  4C 8B 75 B0                     mov r14, qword ptr [rbp - 0x50]
00A29B73  85 C0                           test eax, eax
00A29B75  78 31                           js 0x140a29ba8
00A29B77  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
00A29B7B  41 83 C9 FF                     or r9d, 0xffffffff
00A29B7F  48 83 C0 38                     add rax, 0x38
00A29B83  45 8B C7                        mov r8d, r15d
00A29B86  BA 00 04 00 00                  mov edx, 0x400
00A29B8B  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A29B90  49 8B CE                        mov rcx, r14
00A29B93  E8 D4 17 00 00                  call 0x140a2b36c
00A29B98  8B D8                           mov ebx, eax
00A29B9A  03 DB                           add ebx, ebx
00A29B9C  89 5D 80                        mov dword ptr [rbp - 0x80], ebx
00A29B9F  75 5B                           jne 0x140a29bfc
00A29BA1  B8 38 00 04 C0                  mov eax, 0xc0040038
00A29BA6  EB 07                           jmp 0x140a29baf
00A29BA8  3D 38 00 04 C0                  cmp eax, 0xc0040038
00A29BAD  75 33                           jne 0x140a29be2
00A29BAF  44 8B C0                        mov r8d, eax
00A29BB2  BA 09 00 00 00                  mov edx, 9
00A29BB7  48 8B CF                        mov rcx, rdi
00A29BBA  E8 4D 42 ED FF                  call 0x1408fde0c
00A29BBF  48 8B 4F 10                     mov rcx, qword ptr [rdi + 0x10]
00A29BC3  BA 00 00 20 00                  mov edx, 0x200000
00A29BC8  85 91 8C 01 00 00               test dword ptr [rcx + 0x18c], edx
00A29BCE  75 12                           jne 0x140a29be2
00A29BD0  E8 73 24 ED FF                  call 0x1408fc048
00A29BD5  48 8B 4F 10                     mov rcx, qword ptr [rdi + 0x10]
00A29BD9  48 83 C1 28                     add rcx, 0x28
00A29BDD  E8 4A E7 D0 FF                  call 0x14073832c
00A29BE2  4D 85 F6                        test r14, r14
00A29BE5  74 15                           je 0x140a29bfc
00A29BE7  33 D2                           xor edx, edx
00A29BE9  49 8B CE                        mov rcx, r14
00A29BEC  E8 7F 8C 15 00                  call 0x140b82870
00A29BF1  4D 8B F4                        mov r14, r12
00A29BF4  4C 89 65 B0                     mov qword ptr [rbp - 0x50], r12
00A29BF8  44 89 65 80                     mov dword ptr [rbp - 0x80], r12d
00A29BFC  49 8B CE                        mov rcx, r14
00A29BFF  E8 50 F6 F2 FF                  call 0x140959254
00A29C04  48 8B 4F 20                     mov rcx, qword ptr [rdi + 0x20]
00A29C08  4C 8D 45 A8                     lea r8, [rbp - 0x58]
00A29C0C  BA 02 00 00 00                  mov edx, 2
00A29C11  44 89 65 88                     mov dword ptr [rbp - 0x78], r12d
00A29C15  E8 FA 1A ED FF                  call 0x1408fb714
00A29C1A  48 8B 75 A8                     mov rsi, qword ptr [rbp - 0x58]
00A29C1E  85 C0                           test eax, eax
00A29C20  78 34                           js 0x140a29c56
00A29C22  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
00A29C26  41 83 C9 FF                     or r9d, 0xffffffff
00A29C2A  48 83 C0 38                     add rax, 0x38
00A29C2E  45 8B C7                        mov r8d, r15d
00A29C31  BA 00 04 00 00                  mov edx, 0x400
00A29C36  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A29C3B  48 8B CE                        mov rcx, rsi
00A29C3E  E8 29 17 00 00                  call 0x140a2b36c
00A29C43  44 8B F8                        mov r15d, eax
00A29C46  45 03 FF                        add r15d, r15d
00A29C49  44 89 7D 88                     mov dword ptr [rbp - 0x78], r15d
00A29C4D  75 5B                           jne 0x140a29caa
00A29C4F  B8 38 00 04 C0                  mov eax, 0xc0040038
00A29C54  EB 07                           jmp 0x140a29c5d
00A29C56  3D 38 00 04 C0                  cmp eax, 0xc0040038
00A29C5B  75 33                           jne 0x140a29c90
00A29C5D  44 8B C0                        mov r8d, eax
00A29C60  BA 09 00 00 00                  mov edx, 9
00A29C65  48 8B CF                        mov rcx, rdi
00A29C68  E8 9F 41 ED FF                  call 0x1408fde0c
00A29C6D  48 8B 4F 10                     mov rcx, qword ptr [rdi + 0x10]
00A29C71  BA 00 00 20 00                  mov edx, 0x200000
00A29C76  85 91 8C 01 00 00               test dword ptr [rcx + 0x18c], edx
00A29C7C  75 12                           jne 0x140a29c90
00A29C7E  E8 C5 23 ED FF                  call 0x1408fc048
00A29C83  48 8B 4F 10                     mov rcx, qword ptr [rdi + 0x10]
00A29C87  48 83 C1 28                     add rcx, 0x28
00A29C8B  E8 9C E6 D0 FF                  call 0x14073832c
00A29C90  48 85 F6                        test rsi, rsi
00A29C93  74 15                           je 0x140a29caa
00A29C95  33 D2                           xor edx, edx
00A29C97  48 8B CE                        mov rcx, rsi
00A29C9A  E8 D1 8B 15 00                  call 0x140b82870
00A29C9F  49 8B F4                        mov rsi, r12
00A29CA2  4C 89 65 A8                     mov qword ptr [rbp - 0x58], r12
00A29CA6  44 89 65 88                     mov dword ptr [rbp - 0x78], r12d
00A29CAA  4C 8D 87 AC 02 00 00            lea r8, [rdi + 0x2ac]
00A29CB1  48 8B D6                        mov rdx, rsi
00A29CB4  49 8B CE                        mov rcx, r14
00A29CB7  E8 64 14 00 00                  call 0x140a2b120
00A29CBC  48 8B 4F 20                     mov rcx, qword ptr [rdi + 0x20]
00A29CC0  4C 8D 45 A0                     lea r8, [rbp - 0x60]
00A29CC4  BA 05 00 00 00                  mov edx, 5
00A29CC9  E8 46 1A ED FF                  call 0x1408fb714
00A29CCE  48 8B 5D A0                     mov rbx, qword ptr [rbp - 0x60]
00A29CD2  48 85 DB                        test rbx, rbx
00A29CD5  74 31                           je 0x140a29d08
00A29CD7  48 8B D3                        mov rdx, rbx
00A29CDA  48 8D 4D F8                     lea rcx, [rbp - 8]
00A29CDE  E8 9D 0A A0 FF                  call 0x14042a780
00A29CE3  48 8D 95 A0 00 00 00            lea rdx, [rbp + 0xa0]
00A29CEA  48 8D 4D F8                     lea rcx, [rbp - 8]
00A29CEE  E8 FD 81 EC FF                  call 0x1408f1ef0
00A29CF3  85 C0                           test eax, eax
00A29CF5  79 11                           jns 0x140a29d08
00A29CF7  33 D2                           xor edx, edx
00A29CF9  48 8B CB                        mov rcx, rbx
00A29CFC  E8 6F 8B 15 00                  call 0x140b82870
00A29D01  49 8B DC                        mov rbx, r12
00A29D04  48 89 5D A0                     mov qword ptr [rbp - 0x60], rbx
00A29D08  4C 8D 4C 24 58                  lea r9, [rsp + 0x58]
00A29D0D  4C 8B C6                        mov r8, rsi
00A29D10  49 8B D6                        mov rdx, r14
00A29D13  48 8B CF                        mov rcx, rdi
00A29D16  E8 59 07 00 00                  call 0x140a2a474
00A29D1B  85 C0                           test eax, eax
00A29D1D  79 2C                           jns 0x140a29d4b
00A29D1F  8B 45 64                        mov eax, dword ptr [rbp + 0x64]
00A29D22  A8 20                           test al, 0x20
00A29D24  75 15                           jne 0x140a29d3b
00A29D26  0F BA E0 12                     bt eax, 0x12
00A29D2A  72 0F                           jb 0x140a29d3b
00A29D2C  A8 10                           test al, 0x10
00A29D2E  74 0B                           je 0x140a29d3b
00A29D30  41 BE 01 00 00 00               mov r14d, 1
00A29D36  45 8A C6                        mov r8b, r14b
00A29D39  EB 09                           jmp 0x140a29d44
00A29D3B  45 8A C4                        mov r8b, r12b
00A29D3E  41 BE 01 00 00 00               mov r14d, 1
00A29D44  48 85 DB                        test rbx, rbx
00A29D47  74 0D                           je 0x140a29d56
00A29D49  EB 48                           jmp 0x140a29d93
00A29D4B  44 8A 44 24 58                  mov r8b, byte ptr [rsp + 0x58]
00A29D50  41 BE 01 00 00 00               mov r14d, 1
00A29D56  44 39 74 24 68                  cmp dword ptr [rsp + 0x68], r14d
00A29D5B  48 8D 45 E8                     lea rax, [rbp - 0x18]
00A29D5F  49 8B D4                        mov rdx, r12
00A29D62  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A29D67  48 0F 45 54 24 78               cmovne rdx, qword ptr [rsp + 0x78]
00A29D6D  4C 8B CB                        mov r9, rbx
00A29D70  48 8B CF                        mov rcx, rdi
00A29D73  E8 1C D9 05 00                  call 0x140a87694
00A29D78  85 C0                           test eax, eax
00A29D7A  78 17                           js 0x140a29d93
00A29D7C  48 85 DB                        test rbx, rbx
00A29D7F  74 0A                           je 0x140a29d8b
00A29D81  33 D2                           xor edx, edx
00A29D83  48 8B CB                        mov rcx, rbx
00A29D86  E8 E5 8A 15 00                  call 0x140b82870
00A29D8B  48 8B 5D E8                     mov rbx, qword ptr [rbp - 0x18]
00A29D8F  48 89 5D A0                     mov qword ptr [rbp - 0x60], rbx
00A29D93  48 8D B7 98 02 00 00            lea rsi, [rdi + 0x298]
00A29D9A  48 85 DB                        test rbx, rbx
00A29D9D  74 1C                           je 0x140a29dbb
00A29D9F  48 8B D3                        mov rdx, rbx
00A29DA2  48 8D 4D F8                     lea rcx, [rbp - 8]
00A29DA6  E8 D5 09 A0 FF                  call 0x14042a780
00A29DAB  48 8B D6                        mov rdx, rsi
00A29DAE  48 8D 4D F8                     lea rcx, [rbp - 8]
00A29DB2  E8 39 81 EC FF                  call 0x1408f1ef0
00A29DB7  85 C0                           test eax, eax
00A29DB9  79 06                           jns 0x140a29dc1
00A29DBB  0F 57 C0                        xorps xmm0, xmm0
00A29DBE  0F 11 06                        movups xmmword ptr [rsi], xmm0
00A29DC1  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00A29DCA  48 8D 1D 2F 28 56 00            lea rbx, [rip + 0x56282f]
00A29DD1  48 83 CE FF                     or rsi, 0xffffffffffffffff
00A29DD5  41 8A D6                        mov dl, r14b
00A29DD8  48 8B CB                        mov rcx, rbx
00A29DDB  66 01 B0 E4 01 00 00            add word ptr [rax + 0x1e4], si
00A29DE2  90                              nop
00A29DE3  E8 D8 7D 7E FF                  call 0x140211bc0
00A29DE8  8D 56 21                        lea edx, [rsi + 0x21]
00A29DEB  48 8B CF                        mov rcx, rdi
00A29DEE  E8 55 22 ED FF                  call 0x1408fc048
00A29DF3  48 8B CB                        mov rcx, rbx
00A29DF6  E8 15 5C 83 FF                  call 0x14025fa10
00A29DFB  E8 B0 3A 83 FF                  call 0x14025d8b0
00A29E00  4C 39 64 24 70                  cmp qword ptr [rsp + 0x70], r12
00A29E05  74 41                           je 0x140a29e48
00A29E07  4C 39 65 A0                     cmp qword ptr [rbp - 0x60], r12
00A29E0B  74 3B                           je 0x140a29e48
00A29E0D  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00A29E16  41 8A D6                        mov dl, r14b
00A29E19  48 8B CB                        mov rcx, rbx
00A29E1C  66 01 B0 E4 01 00 00            add word ptr [rax + 0x1e4], si
00A29E23  90                              nop
00A29E24  E8 F7 AF 7E FF                  call 0x140214e20
00A29E29  4C 8B 45 A0                     mov r8, qword ptr [rbp - 0x60]
00A29E2D  48 8B 54 24 70                  mov rdx, qword ptr [rsp + 0x70]
00A29E32  48 8B 4F 30                     mov rcx, qword ptr [rdi + 0x30]
00A29E36  E8 6D 32 ED FF                  call 0x1408fd0a8
00A29E3B  48 8B CB                        mov rcx, rbx
00A29E3E  E8 CD 5B 83 FF                  call 0x14025fa10
00A29E43  E8 68 3A 83 FF                  call 0x14025d8b0
00A29E48  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00A29E51  41 8A D6                        mov dl, r14b
00A29E54  48 8B CB                        mov rcx, rbx
00A29E57  66 01 B0 E4 01 00 00            add word ptr [rax + 0x1e4], si
00A29E5E  90                              nop
00A29E5F  E8 5C 7D 7E FF                  call 0x140211bc0
00A29E64  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
00A29E69  33 DB                           xor ebx, ebx
00A29E6B  4C 8B 7D A8                     mov r15, qword ptr [rbp - 0x58]
00A29E6F  4C 8B 65 B0                     mov r12, qword ptr [rbp - 0x50]
00A29E73  48 85 F6                        test rsi, rsi
00A29E76  0F 84 A1 01 00 00               je 0x140a2a01d
00A29E7C  38 5C 24 50                     cmp byte ptr [rsp + 0x50], bl
00A29E80  75 6D                           jne 0x140a29eef
00A29E82  44 39 74 24 5C                  cmp dword ptr [rsp + 0x5c], r14d
00A29E87  74 66                           je 0x140a29eef
00A29E89  44 8B 4D 80                     mov r9d, dword ptr [rbp - 0x80]
00A29E8D  48 8D 44 24 51                  lea rax, [rsp + 0x51]
00A29E92  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A29E97  4D 8B C4                        mov r8, r12
00A29E9A  48 8B D6                        mov rdx, rsi
00A29E9D  44 88 74 24 20                  mov byte ptr [rsp + 0x20], r14b
00A29EA2  48 8B CF                        mov rcx, rdi
00A29EA5  E8 8E 8A F4 FF                  call 0x140972938
00A29EAA  0F B6 5C 24 51                  movzx ebx, byte ptr [rsp + 0x51]
00A29EAF  33 D2                           xor edx, edx
00A29EB1  44 8B 75 88                     mov r14d, dword ptr [rbp - 0x78]
00A29EB5  85 C0                           test eax, eax
00A29EB7  0F 48 DA                        cmovs ebx, edx
00A29EBA  88 5C 24 51                     mov byte ptr [rsp + 0x51], bl
00A29EBE  84 DB                           test bl, bl
00A29EC0  75 35                           jne 0x140a29ef7
00A29EC2  48 8D 44 24 51                  lea rax, [rsp + 0x51]
00A29EC7  45 8B CE                        mov r9d, r14d
00A29ECA  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A29ECF  4D 8B C7                        mov r8, r15
00A29ED2  88 54 24 20                     mov byte ptr [rsp + 0x20], dl
00A29ED6  48 8B CF                        mov rcx, rdi
00A29ED9  48 8B D6                        mov rdx, rsi
00A29EDC  E8 57 8A F4 FF                  call 0x140972938
00A29EE1  0F B6 5C 24 51                  movzx ebx, byte ptr [rsp + 0x51]
00A29EE6  33 D2                           xor edx, edx
00A29EE8  85 C0                           test eax, eax
00A29EEA  0F 48 DA                        cmovs ebx, edx
00A29EED  EB 08                           jmp 0x140a29ef7
00A29EEF  8A 5C 24 51                     mov bl, byte ptr [rsp + 0x51]
00A29EF3  44 8B 75 88                     mov r14d, dword ptr [rbp - 0x78]
00A29EF7  4D 85 E4                        test r12, r12
00A29EFA  74 35                           je 0x140a29f31
00A29EFC  8B 44 24 60                     mov eax, dword ptr [rsp + 0x60]
00A29F00  41 B9 02 00 00 00               mov r9d, 2
00A29F06  48 8B 57 30                     mov rdx, qword ptr [rdi + 0x30]
00A29F0A  4C 8B C6                        mov r8, rsi
00A29F0D  48 8B 0D 84 C4 43 00            mov rcx, qword ptr [rip + 0x43c484]
00A29F14  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
00A29F18  8B 45 80                        mov eax, dword ptr [rbp - 0x80]
00A29F1B  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A29F1F  4C 89 64 24 28                  mov qword ptr [rsp + 0x28], r12
00A29F24  C7 44 24 20 07 00 00 00         mov dword ptr [rsp + 0x20], 7
00A29F2C  E8 5B 37 ED FF                  call 0x1408fd68c
00A29F31  4D 85 FF                        test r15, r15
00A29F34  74 33                           je 0x140a29f69
00A29F36  8B 44 24 60                     mov eax, dword ptr [rsp + 0x60]
00A29F3A  41 B9 03 00 00 00               mov r9d, 3
00A29F40  48 8B 57 30                     mov rdx, qword ptr [rdi + 0x30]
00A29F44  4C 8B C6                        mov r8, rsi
00A29F47  48 8B 0D 4A C4 43 00            mov rcx, qword ptr [rip + 0x43c44a]
00A29F4E  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
00A29F52  44 89 74 24 30                  mov dword ptr [rsp + 0x30], r14d
00A29F57  4C 89 7C 24 28                  mov qword ptr [rsp + 0x28], r15
00A29F5C  C7 44 24 20 07 00 00 00         mov dword ptr [rsp + 0x20], 7
00A29F64  E8 23 37 ED FF                  call 0x1408fd68c
00A29F69  84 DB                           test bl, bl
00A29F6B  75 0C                           jne 0x140a29f79
00A29F6D  33 DB                           xor ebx, ebx
00A29F6F  38 5D 94                        cmp byte ptr [rbp - 0x6c], bl
00A29F72  75 07                           jne 0x140a29f7b
00A29F74  E9 A4 00 00 00                  jmp 0x140a2a01d
00A29F79  33 DB                           xor ebx, ebx
00A29F7B  38 5C 24 50                     cmp byte ptr [rsp + 0x50], bl
00A29F7F  75 29                           jne 0x140a29faa
00A29F81  48 8B 4F 30                     mov rcx, qword ptr [rdi + 0x30]
00A29F85  4C 8D 44 24 6C                  lea r8, [rsp + 0x6c]
00A29F8A  48 8B D6                        mov rdx, rsi
00A29F8D  E8 1A C8 D0 FF                  call 0x1407367ac
00A29F92  8B 54 24 54                     mov edx, dword ptr [rsp + 0x54]
00A29F96  85 C0                           test eax, eax
00A29F98  78 0C                           js 0x140a29fa6
00A29F9A  8B 44 24 6C                     mov eax, dword ptr [rsp + 0x6c]
00A29F9E  0B D0                           or edx, eax
00A29FA0  89 54 24 54                     mov dword ptr [rsp + 0x54], edx
00A29FA4  EB 0C                           jmp 0x140a29fb2
00A29FA6  8B C3                           mov eax, ebx
00A29FA8  EB 08                           jmp 0x140a29fb2
00A29FAA  8B 54 24 54                     mov edx, dword ptr [rsp + 0x54]
00A29FAE  8B 44 24 6C                     mov eax, dword ptr [rsp + 0x6c]
00A29FB2  A8 20                           test al, 0x20
00A29FB4  0F 94 C1                        sete cl
00A29FB7  0F BA E2 12                     bt edx, 0x12
00A29FBB  0F 93 C0                        setae al
00A29FBE  84 C8                           test al, cl
00A29FC0  75 42                           jne 0x140a2a004
00A29FC2  8B 44 24 60                     mov eax, dword ptr [rsp + 0x60]
00A29FC6  B9 04 00 00 00                  mov ecx, 4
00A29FCB  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
00A29FCF  0F BA F2 12                     btr edx, 0x12
00A29FD3  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
00A29FD7  48 8D 44 24 54                  lea rax, [rsp + 0x54]
00A29FDC  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A29FE1  4C 8B C6                        mov r8, rsi
00A29FE4  89 4C 24 20                     mov dword ptr [rsp + 0x20], ecx
00A29FE8  44 8D 49 07                     lea r9d, [rcx + 7]
00A29FEC  48 8B 0D A5 C3 43 00            mov rcx, qword ptr [rip + 0x43c3a5]
00A29FF3  89 54 24 54                     mov dword ptr [rsp + 0x54], edx
00A29FF7  48 8B 57 30                     mov rdx, qword ptr [rdi + 0x30]
00A29FFB  E8 8C 36 ED FF                  call 0x1408fd68c
00A2A000  8B 54 24 54                     mov edx, dword ptr [rsp + 0x54]
00A2A004  F6 C2 20                        test dl, 0x20
00A2A007  74 14                           je 0x140a2a01d
00A2A009  45 33 C0                        xor r8d, r8d
00A2A00C  C6 44 24 50 01                  mov byte ptr [rsp + 0x50], 1
00A2A011  48 8B CF                        mov rcx, rdi
00A2A014  41 8D 50 12                     lea edx, [r8 + 0x12]
00A2A018  E8 EF 3D ED FF                  call 0x1408fde0c
00A2A01D  48 8D 0D DC 25 56 00            lea rcx, [rip + 0x5625dc]
00A2A024  E8 E7 59 83 FF                  call 0x14025fa10
00A2A029  E8 82 38 83 FF                  call 0x14025d8b0
00A2A02E  4C 8B 75 C8                     mov r14, qword ptr [rbp - 0x38]
00A2A032  48 85 F6                        test rsi, rsi
00A2A035  0F 84 F4 00 00 00               je 0x140a2a12f
00A2A03B  33 C9                           xor ecx, ecx
00A2A03D  8B C3                           mov eax, ebx
00A2A03F  48 89 4C 24 78                  mov qword ptr [rsp + 0x78], rcx
00A2A044  89 4C 24 6C                     mov dword ptr [rsp + 0x6c], ecx
00A2A048  4D 85 F6                        test r14, r14
00A2A04B  74 29                           je 0x140a2a076
00A2A04D  48 83 C8 FF                     or rax, 0xffffffffffffffff
00A2A051  48 FF C0                        inc rax
00A2A054  66 41 39 0C 46                  cmp word ptr [r14 + rax*2], cx
00A2A059  75 F6                           jne 0x140a2a051
00A2A05B  8D 1C 45 02 00 00 00            lea ebx, [rax*2 + 2]
00A2A062  49 8B CE                        mov rcx, r14
00A2A065  8B D3                           mov edx, ebx
00A2A067  4C 8D 4C 24 6C                  lea r9, [rsp + 0x6c]
00A2A06C  4C 8D 44 24 78                  lea r8, [rsp + 0x78]
00A2A071  E8 32 34 00 00                  call 0x140a2d4a8
00A2A076  8B 54 24 60                     mov edx, dword ptr [rsp + 0x60]
00A2A07A  F7 D8                           neg eax
00A2A07C  48 8B 0D 15 C3 43 00            mov rcx, qword ptr [rip + 0x43c315]
00A2A083  4C 8B CE                        mov r9, rsi
00A2A086  89 54 24 48                     mov dword ptr [rsp + 0x48], edx
00A2A08A  1B C0                           sbb eax, eax
00A2A08C  48 8B 57 30                     mov rdx, qword ptr [rdi + 0x30]
00A2A090  83 E0 07                        and eax, 7
00A2A093  89 5C 24 40                     mov dword ptr [rsp + 0x40], ebx
00A2A097  83 C0 12                        add eax, 0x12
00A2A09A  4C 89 74 24 38                  mov qword ptr [rsp + 0x38], r14
00A2A09F  33 DB                           xor ebx, ebx
00A2A0A1  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A2A0A5  48 8D 05 D4 DB 5F FF            lea rax, [rip - 0xa0242c]
00A2A0AC  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A2A0B1  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00A2A0B6  44 8D 43 01                     lea r8d, [rbx + 1]
00A2A0BA  E8 29 C6 EC FF                  call 0x1408f66e8
00A2A0BF  4C 8D 44 24 6C                  lea r8, [rsp + 0x6c]
00A2A0C4  48 8B CF                        mov rcx, rdi
00A2A0C7  48 8D 54 24 78                  lea rdx, [rsp + 0x78]
00A2A0CC  E8 EF E5 FF FF                  call 0x140a286c0
00A2A0D1  85 C0                           test eax, eax
00A2A0D3  78 5A                           js 0x140a2a12f
00A2A0D5  8B 44 24 6C                     mov eax, dword ptr [rsp + 0x6c]
00A2A0D9  4C 8B CE                        mov r9, rsi
00A2A0DC  8B 4C 24 60                     mov ecx, dword ptr [rsp + 0x60]
00A2A0E0  03 C0                           add eax, eax
00A2A0E2  48 8B 5C 24 78                  mov rbx, qword ptr [rsp + 0x78]
00A2A0E7  48 8B 57 30                     mov rdx, qword ptr [rdi + 0x30]
00A2A0EB  89 4C 24 48                     mov dword ptr [rsp + 0x48], ecx
00A2A0EF  48 8B 0D A2 C2 43 00            mov rcx, qword ptr [rip + 0x43c2a2]
00A2A0F6  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00A2A0FA  48 8D 05 9F 75 5E FF            lea rax, [rip - 0xa18a61]
00A2A101  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
00A2A106  C7 44 24 30 12 20 00 00         mov dword ptr [rsp + 0x30], 0x2012
00A2A10E  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A2A113  33 C0                           xor eax, eax
00A2A115  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A2A11A  44 8D 40 01                     lea r8d, [rax + 1]
00A2A11E  E8 C5 C5 EC FF                  call 0x1408f66e8
00A2A123  33 D2                           xor edx, edx
00A2A125  48 8B CB                        mov rcx, rbx
00A2A128  E8 43 87 15 00                  call 0x140b82870
00A2A12D  33 DB                           xor ebx, ebx
00A2A12F  48 8B CF                        mov rcx, rdi
00A2A132  E8 55 0E 00 00                  call 0x140a2af8c
00A2A137  33 D2                           xor edx, edx
00A2A139  48 8D 4D 10                     lea rcx, [rbp + 0x10]
00A2A13D  44 8D 42 50                     lea r8d, [rdx + 0x50]
00A2A141  E8 FA CA C9 FF                  call 0x1406c6c40
00A2A146  48 8B CF                        mov rcx, rdi
00A2A149  E8 2E E4 FF FF                  call 0x140a2857c
00A2A14E  48 8B 4F 20                     mov rcx, qword ptr [rdi + 0x20]
00A2A152  48 8D 55 10                     lea rdx, [rbp + 0x10]
00A2A156  E8 55 E4 FF FF                  call 0x140a285b0
00A2A15B  85 C0                           test eax, eax
00A2A15D  78 26                           js 0x140a2a185
00A2A15F  48 8D 55 10                     lea rdx, [rbp + 0x10]
00A2A163  48 8B CF                        mov rcx, rdi
00A2A166  E8 4D 1F D1 FF                  call 0x14073c0b8
00A2A16B  48 8D 4D 10                     lea rcx, [rbp + 0x10]
00A2A16F  8B D8                           mov ebx, eax
00A2A171  E8 F6 60 D1 FF                  call 0x14074026c
00A2A176  8B 44 24 64                     mov eax, dword ptr [rsp + 0x64]
00A2A17A  85 DB                           test ebx, ebx
00A2A17C  0F 48 C3                        cmovs eax, ebx
00A2A17F  33 DB                           xor ebx, ebx
00A2A181  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
00A2A185  F7 45 64 00 40 00 00            test dword ptr [rbp + 0x64], 0x4000
00A2A18C  75 4B                           jne 0x140a2a1d9
00A2A18E  F7 87 8C 01 00 00 00 20 00 00   test dword ptr [rdi + 0x18c], 0x2000
00A2A198  74 09                           je 0x140a2a1a3
00A2A19A  83 BF 94 01 00 00 0E            cmp dword ptr [rdi + 0x194], 0xe
00A2A1A1  74 36                           je 0x140a2a1d9
00A2A1A3  38 5C 24 50                     cmp byte ptr [rsp + 0x50], bl
00A2A1A7  74 20                           je 0x140a2a1c9
00A2A1A9  8B 45 98                        mov eax, dword ptr [rbp - 0x68]
00A2A1AC  B9 01 00 00 00                  mov ecx, 1
00A2A1B1  39 4C 24 5C                     cmp dword ptr [rsp + 0x5c], ecx
00A2A1B5  75 02                           jne 0x140a2a1b9
00A2A1B7  0B C1                           or eax, ecx
00A2A1B9  44 8B C0                        mov r8d, eax
00A2A1BC  48 8B D6                        mov rdx, rsi
00A2A1BF  48 8B CF                        mov rcx, rdi
00A2A1C2  E8 E9 CB 08 00                  call 0x140ab6db0
00A2A1C7  EB 10                           jmp 0x140a2a1d9
00A2A1C9  48 85 F6                        test rsi, rsi
00A2A1CC  74 0B                           je 0x140a2a1d9
00A2A1CE  48 8B D6                        mov rdx, rsi
00A2A1D1  48 8B CF                        mov rcx, rdi
00A2A1D4  E8 23 DB 06 00                  call 0x140a97cfc
00A2A1D9  48 8B CF                        mov rcx, rdi
00A2A1DC  E8 3B 44 ED FF                  call 0x1408fe61c
00A2A1E1  F7 87 8C 01 00 00 00 20 00 00   test dword ptr [rdi + 0x18c], 0x2000
00A2A1EB  74 24                           je 0x140a2a211
00A2A1ED  8B 87 94 01 00 00               mov eax, dword ptr [rdi + 0x194]
00A2A1F3  83 F8 16                        cmp eax, 0x16
00A2A1F6  74 2B                           je 0x140a2a223
00A2A1F8  83 F8 1D                        cmp eax, 0x1d
00A2A1FB  74 26                           je 0x140a2a223
00A2A1FD  83 F8 0E                        cmp eax, 0xe
00A2A200  74 21                           je 0x140a2a223
00A2A202  83 F8 09                        cmp eax, 9
00A2A205  74 1C                           je 0x140a2a223
00A2A207  83 F8 03                        cmp eax, 3
00A2A20A  74 17                           je 0x140a2a223
00A2A20C  83 F8 13                        cmp eax, 0x13
00A2A20F  74 12                           je 0x140a2a223
00A2A211  48 8D 57 28                     lea rdx, [rdi + 0x28]
00A2A215  41 B8 01 00 00 00               mov r8d, 1
00A2A21B  48 8B CE                        mov rcx, rsi
00A2A21E  E8 19 B8 04 00                  call 0x140a75a3c
00A2A223  48 85 F6                        test rsi, rsi
00A2A226  74 30                           je 0x140a2a258
00A2A228  B8 01 00 00 00                  mov eax, 1
00A2A22D  48 8B D6                        mov rdx, rsi
00A2A230  39 44 24 5C                     cmp dword ptr [rsp + 0x5c], eax
00A2A234  48 8B CF                        mov rcx, rdi
00A2A237  41 0F 94 C0                     sete r8b
00A2A23B  E8 A4 A7 06 00                  call 0x140a949e4
00A2A240  B8 01 00 00 00                  mov eax, 1
00A2A245  48 8B D6                        mov rdx, rsi
00A2A248  39 44 24 5C                     cmp dword ptr [rsp + 0x5c], eax
00A2A24C  48 8B CF                        mov rcx, rdi
00A2A24F  41 0F 94 C0                     sete r8b
00A2A253  E8 D0 58 05 00                  call 0x140a7fb28
00A2A258  48 8B CF                        mov rcx, rdi
00A2A25B  E8 B0 38 ED FF                  call 0x1408fdb10
00A2A260  F7 87 8C 01 00 00 00 20 00 00   test dword ptr [rdi + 0x18c], 0x2000
00A2A26A  74 1D                           je 0x140a2a289
00A2A26C  8B 87 94 01 00 00               mov eax, dword ptr [rdi + 0x194]
00A2A272  83 F8 09                        cmp eax, 9
00A2A275  0F 84 98 00 00 00               je 0x140a2a313
00A2A27B  83 C0 FD                        add eax, -3
00A2A27E  A9 EF FF FF FF                  test eax, 0xffffffef
00A2A283  0F 84 8A 00 00 00               je 0x140a2a313
00A2A289  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00A2A292  48 83 C9 FF                     or rcx, 0xffffffffffffffff
00A2A296  66 01 88 E4 01 00 00            add word ptr [rax + 0x1e4], cx
00A2A29D  8D 71 02                        lea esi, [rcx + 2]
00A2A2A0  40 8A D6                        mov dl, sil
00A2A2A3  48 8D 0D 56 23 56 00            lea rcx, [rip + 0x562356]
00A2A2AA  90                              nop
00A2A2AB  E8 10 79 7E FF                  call 0x140211bc0
00A2A2B0  39 74 24 5C                     cmp dword ptr [rsp + 0x5c], esi
00A2A2B4  48 8D 55 60                     lea rdx, [rbp + 0x60]
00A2A2B8  48 8B CF                        mov rcx, rdi
00A2A2BB  41 0F 94 C0                     sete r8b
00A2A2BF  E8 B4 31 ED FF                  call 0x1408fd478
00A2A2C4  48 8D 0D 35 23 56 00            lea rcx, [rip + 0x562335]
00A2A2CB  E8 40 57 83 FF                  call 0x14025fa10
00A2A2D0  E8 DB 35 83 FF                  call 0x14025d8b0
00A2A2D5  48 8B CF                        mov rcx, rdi
00A2A2D8  E8 63 BB 05 00                  call 0x140a85e40
00A2A2DD  4C 8D 47 38                     lea r8, [rdi + 0x38]
00A2A2E1  45 33 C9                        xor r9d, r9d
00A2A2E4  48 8D 4F 28                     lea rcx, [rdi + 0x28]
00A2A2E8  40 8A D6                        mov dl, sil
00A2A2EB  E8 E4 D6 FD FF                  call 0x140a079d4
00A2A2F0  85 C0                           test eax, eax
00A2A2F2  79 0E                           jns 0x140a2a302
00A2A2F4  44 8B C0                        mov r8d, eax
00A2A2F7  8D 56 12                        lea edx, [rsi + 0x12]
00A2A2FA  48 8B CF                        mov rcx, rdi
00A2A2FD  E8 0A 3B ED FF                  call 0x1408fde0c
00A2A302  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
00A2A307  4C 8B 65 B0                     mov r12, qword ptr [rbp - 0x50]
00A2A30B  4C 8B 75 C8                     mov r14, qword ptr [rbp - 0x38]
00A2A30F  4C 8B 7D A8                     mov r15, qword ptr [rbp - 0x58]
00A2A313  F7 87 8C 01 00 00 00 20 00 00   test dword ptr [rdi + 0x18c], 0x2000
00A2A31D  74 10                           je 0x140a2a32f
00A2A31F  8B 87 94 01 00 00               mov eax, dword ptr [rdi + 0x194]
00A2A325  83 F8 09                        cmp eax, 9
00A2A328  74 57                           je 0x140a2a381
00A2A32A  83 F8 03                        cmp eax, 3
00A2A32D  74 52                           je 0x140a2a381
00A2A32F  49 8B CD                        mov rcx, r13
00A2A332  E8 99 D4 A8 FF                  call 0x1404b77d0
00A2A337  48 85 F6                        test rsi, rsi
00A2A33A  74 0B                           je 0x140a2a347
00A2A33C  48 8B D6                        mov rdx, rsi
00A2A33F  48 8B CF                        mov rcx, rdi
00A2A342  E8 05 1A ED FF                  call 0x1408fbd4c
00A2A347  48 8B 57 30                     mov rdx, qword ptr [rdi + 0x30]
00A2A34B  48 85 D2                        test rdx, rdx
00A2A34E  74 1A                           je 0x140a2a36a
00A2A350  41 B8 01 00 00 00               mov r8d, 1
00A2A356  E8 25 DA EC FF                  call 0x1408f7d80
00A2A35B  48 8B 57 30                     mov rdx, qword ptr [rdi + 0x30]
00A2A35F  41 B8 0E 00 00 00               mov r8d, 0xe
00A2A365  E8 16 DA EC FF                  call 0x1408f7d80
00A2A36A  49 8B D5                        mov rdx, r13
00A2A36D  48 8D 0D 9C 72 5E FF            lea rcx, [rip - 0xa18d64]
00A2A374  E8 8B 1A ED FF                  call 0x1408fbe04
00A2A379  48 8B CF                        mov rcx, rdi
00A2A37C  E8 1F BF FD FF                  call 0x140a062a0
00A2A381  4D 85 E4                        test r12, r12
00A2A384  74 0A                           je 0x140a2a390
00A2A386  33 D2                           xor edx, edx
00A2A388  49 8B CC                        mov rcx, r12
00A2A38B  E8 E0 84 15 00                  call 0x140b82870
00A2A390  4D 85 FF                        test r15, r15
00A2A393  74 0A                           je 0x140a2a39f
00A2A395  33 D2                           xor edx, edx
00A2A397  49 8B CF                        mov rcx, r15
00A2A39A  E8 D1 84 15 00                  call 0x140b82870
00A2A39F  48 8B 4D A0                     mov rcx, qword ptr [rbp - 0x60]
00A2A3A3  48 85 C9                        test rcx, rcx
00A2A3A6  74 07                           je 0x140a2a3af
00A2A3A8  33 D2                           xor edx, edx
00A2A3AA  E8 C1 84 15 00                  call 0x140b82870
00A2A3AF  48 85 F6                        test rsi, rsi
00A2A3B2  74 08                           je 0x140a2a3bc
00A2A3B4  48 8B CE                        mov rcx, rsi
00A2A3B7  E8 F4 2E C8 FF                  call 0x1406ad2b0
00A2A3BC  48 8B 4D B8                     mov rcx, qword ptr [rbp - 0x48]
00A2A3C0  48 85 C9                        test rcx, rcx
00A2A3C3  74 07                           je 0x140a2a3cc
00A2A3C5  33 D2                           xor edx, edx
00A2A3C7  E8 A4 84 15 00                  call 0x140b82870
00A2A3CC  48 8B 4D D8                     mov rcx, qword ptr [rbp - 0x28]
00A2A3D0  48 85 C9                        test rcx, rcx
00A2A3D3  74 07                           je 0x140a2a3dc
00A2A3D5  33 D2                           xor edx, edx
00A2A3D7  E8 94 84 15 00                  call 0x140b82870
00A2A3DC  4D 85 F6                        test r14, r14
00A2A3DF  74 0A                           je 0x140a2a3eb
00A2A3E1  33 D2                           xor edx, edx
00A2A3E3  49 8B CE                        mov rcx, r14
00A2A3E6  E8 85 84 15 00                  call 0x140b82870
00A2A3EB  48 8B 4D E0                     mov rcx, qword ptr [rbp - 0x20]
00A2A3EF  48 85 C9                        test rcx, rcx
00A2A3F2  74 07                           je 0x140a2a3fb
00A2A3F4  33 D2                           xor edx, edx
00A2A3F6  E8 75 84 15 00                  call 0x140b82870
00A2A3FB  48 8B 4D F0                     mov rcx, qword ptr [rbp - 0x10]
00A2A3FF  48 85 C9                        test rcx, rcx
00A2A402  74 05                           je 0x140a2a409
00A2A404  E8 0F 61 EB FF                  call 0x1408e0518
00A2A409  F6 05 1B 5D 4C 00 10            test byte ptr [rip + 0x4c5d1b], 0x10
00A2A410  74 12                           je 0x140a2a424
00A2A412  4C 8B CF                        mov r9, rdi
00A2A415  48 8D 15 A4 D0 5F FF            lea rdx, [rip - 0xa02f5c]
00A2A41C  45 33 C0                        xor r8d, r8d
00A2A41F  E8 00 8B AA FF                  call 0x1404d2f24
00A2A424  39 9F 38 02 00 00               cmp dword ptr [rdi + 0x238], ebx
00A2A42A  8B 5C 24 64                     mov ebx, dword ptr [rsp + 0x64]
00A2A42E  74 0A                           je 0x140a2a43a
00A2A430  8B D3                           mov edx, ebx
00A2A432  48 8B CF                        mov rcx, rdi
00A2A435  E8 4E 26 D1 FF                  call 0x14073ca88
00A2A43A  8B C3                           mov eax, ebx
00A2A43C  48 8B 8D B0 00 00 00            mov rcx, qword ptr [rbp + 0xb0]
00A2A443  48 33 CC                        xor rcx, rsp
00A2A446  E8 F5 21 C8 FF                  call 0x1406ac640
00A2A44B  4C 8D 9C 24 C0 01 00 00         lea r11, [rsp + 0x1c0]
00A2A453  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
00A2A457  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
00A2A45B  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
00A2A45F  49 8B E3                        mov rsp, r11
00A2A462  41 5F                           pop r15
00A2A464  41 5E                           pop r14
00A2A466  41 5D                           pop r13
00A2A468  41 5C                           pop r12
00A2A46A  5D                              pop rbp
00A2A46B  C3                              ret
00A2A46C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PiProcessNewDeviceNode(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m170;
    unsigned __int64 v_stack_m178;
    unsigned int v_stack_m17C;
    unsigned int v_stack_m180;
    unsigned int v_stack_m184;
    unsigned int v_stack_m188;
    unsigned int v_stack_m18C;
    unsigned __int8 v_stack_m190;
    unsigned int v_stack_m194;
    unsigned __int8 v_stack_m197;
    unsigned __int8 v_stack_m198;
    unsigned int v_stack_m1A0;
    unsigned int v_stack_m1A8;
    unsigned __int64 v_stack_m1B0;
    unsigned __int64 v_stack_m1B8;
    unsigned __int64 v_stack_m1C0;
    unsigned __int64 v_stack_m1C8;
    unsigned __int64 v_stack_m28;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (448);
    result = (*(unsigned __int64 *)(v_rip + 4069363)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 232 + 176) = result;
    v_r12 = 0;
    a2 = 0;
    *(unsigned __int64 *)(v_rsp - 232 - 96) = 0;
    *(unsigned __int64 *)(v_rsp - 232 - 32) = 0;
    result = memset(v_rsp - 232 + 96, a2, v_r12 + 64, a4);
    *(unsigned __int64 *)(v_rsp - 232 + 160) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 232 - 88) = 0;
    *(unsigned __int64 *)(v_rsp - 232 - 8) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 232 - 56) = 0;
    *(unsigned __int64 *)(v_rsp - 232 - 120) = 0;
    *(unsigned __int64 *)(v_rsp - 232 - 16) = 0;
    *(unsigned __int64 *)(v_rsp - 232 - 80) = 0;
    *(unsigned __int64 *)(v_rsp - 232 - 72) = 0;
    *(unsigned __int64 *)(v_rsp - 232 - 40) = 0;
    *(unsigned __int64 *)(v_rsp - 232 - 24) = 0;
    *(unsigned int *)(v_rsp - 232 - 112) = 0;
    *(unsigned int *)(v_rsp - 232 - 64) = 0;
    v_stack_m190 = 0;
    *(unsigned __int64 *)(v_rsp - 232 - 128) = 0;
    if (((*(unsigned __int8 *)(v_rip + 5009839)) & (16)) != 0) {
        a4 = a1;
        a2 = v_rip - 10494311;
        a3 = 0;
        result = McTemplateK0p_EtwWriteTransfer(v_rsp - 232 + 96, a2, a3, a4);
    }
    *(unsigned __int8 *)(v_rsp - 232 - 108) = 0;
    v_stack_m198 = 0;
    *(unsigned int *)(v_rsp - 232 - 104) = 0;
    v_stack_m180 = 0;
    *(unsigned __int64 *)(v_rsp - 232 + 8) = *(unsigned __int64 *)(result);
    v_stack_m170 = 0;
    v_stack_m178 = 0;
    v_stack_m194 = 0;
    v_stack_m17C = 0;
    v_stack_m18C = 0;
    v_stack_m184 = 0;
    v_stack_m197 = 0;
    v_stack_m188 = 0;
    result = PiPnpRtlBeginOperation(v_rsp - 232 - 16, a2, a3, a4);
    result = PipClearDevNodeFlags(a1, (unsigned int)(0x2000000ULL), a3, a4);
    result = PnpQueryDeviceID(a1, v_rsp - 232 - 32, v_rsp - 232 - 120, a4);
    if (sign_flag) {
        v_r14 = (unsigned int)(result);
        a1 = 0xC0000001ULL;
        if (((unsigned int)(result)) == 0xC0040038ULL) { v_r14 = (unsigned int)(a1); }
        v_stack_m184 = (unsigned int)(v_r14);
    }
    result = PpIrpQueryCapabilities(*(unsigned __int64 *)(a1 + 32), v_rsp - 232 + 96, v_rsp - 232 - 120, a4);
    result = PipClearDevNodeUserFlags(a1, 2, v_rsp - 232 - 120, a4);
    if (sign_flag) goto loc_00A290AB;
    result = (unsigned int)(*(unsigned int *)(v_rsp - 232 + 100));
    if (!(condition_is_above_or_equal)) {
        a2 = 1 + 1;
        a1 = a1;
        result = PipSetDevNodeUserFlags(a1, a2, v_rsp - 232 - 120, a4);
        result = *(unsigned int *)(v_rsp - 232 + 100);
    }
    v_r15 = 0;
    if ((((unsigned __int8)(result)) & (64)) != 0) { v_r15 = 1; }
loc_00A290AB:
    if ((((unsigned __int8)(result)) & (32)) == 0) goto loc_00A290C5;
    if ((*(unsigned int *)(a1 + 568)) == 4) {
        a1 = a1;
        result = PpProfileCancelTransitioningDock(a1, a2, v_rsp - 232 - 120, a4);
    }
    goto loc_00A290C8;
loc_00A290C5:
loc_00A290C8:
    *(unsigned int *)(a1 + 568) = 0;
    result = (0) | (-1);
    *(unsigned __int64 *)(v_rsp - 232 - 48) = result;
    result = PnpQueryExtendedAddress(*(unsigned __int64 *)(a1 + 32), v_rsp - 232 - 48, v_rsp - 232 - 120, a4);
    a2 = 0;
    result = PnpQueryDeviceText(*(unsigned __int64 *)(a1 + 32), a2, v_rsp - 232 - 120, v_rsp - 232 - 56);
    result = PnpQueryDeviceText(*(unsigned __int64 *)(a1 + 32), 1, v_rsp - 232 - 120, v_rsp - 232 - 40);
    result = PnpIrpQueryID(*(unsigned __int64 *)(a1 + 32), 3, v_rsp - 232 - 72, v_rsp - 232 - 40);
    if (sign_flag) goto loc_00A29148;
    a4 = 0;
    result = (*(unsigned __int64 *)(a1 + 16)) + (56);
    a3 = 0;
    v_stack_m1C8 = result;
    result = PnpFixupID(*(unsigned __int64 *)(v_rsp - 232 - 72), 200, a3, a4);
    result = (unsigned int)((result) + ((unsigned int)(result)));
    if (condition_is_not_equal) goto loc_00A291A3;
    goto loc_00A29156;
loc_00A29148:
    if (((unsigned int)(result)) == 0xC0040038ULL) goto loc_00A29156;
    if (((unsigned int)(result)) != 0xC000009AULL) goto loc_00A2918D;
loc_00A29156:
    result = PipSetDevNodeProblem(a1, 9, (unsigned int)((unsigned int)((unsigned int)(0xC0040038ULL))), a4);
    if (((*(unsigned int *)(*(unsigned __int64 *)(a1 + 16) + 396)) & (0x200000ULL)) == 0) {
        a2 = 0x200000ULL;
        result = PipSetDevNodeFlags(*(unsigned __int64 *)(a1 + 16), a2, (unsigned int)((unsigned int)((unsigned int)(0xC0040038ULL))), a4);
        a1 = *(unsigned __int64 *)(a1 + 16);
        a1 = (a1) + (40);
        result = PnpSetInvalidIDEvent(a1, a2, (unsigned int)((unsigned int)((unsigned int)(0xC0040038ULL))), a4);
    }
    v_r14 = *(unsigned __int64 *)(v_rsp - 232 - 72);
    if (*(unsigned __int64 *)(v_rsp - 232 - 72) != 0) {
        a2 = 0;
        a1 = *(unsigned __int64 *)(v_rsp - 232 - 72);
        result = ExFreePoolWithTag(a1, a2, (unsigned int)((unsigned int)((unsigned int)(0xC0040038ULL))), a4);
        v_r14 = 0;
        *(unsigned __int64 *)(v_rsp - 232 - 72) = 0;
    }
    if ((unsigned __int8)(v_r15) != 0) goto loc_00A291F9;
    if (((*(unsigned int *)(a1 + 396)) & (0x2000ULL)) == 0) goto loc_00A291BD;
    if ((*(unsigned int *)(a1 + 404)) == 9) goto loc_00A2922C;
loc_00A291BD:
    if ((*(unsigned __int64 *)(a1 + 16)) == (*(unsigned __int64 *)(v_rip + 5649008))) goto loc_00A2922C;
    *(unsigned __int64 *)(v_rsp - 232 - 128) = 0;
    result = PipMakeGloballyUniqueId(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 32), v_r14, v_rsp - 232 - 128, a4);
    if (v_r14 != 0) {
        a2 = 0;
        a1 = v_r14;
        result = ExFreePoolWithTag(a1, a2, v_rsp - 232 - 128, a4);
    }
    *(unsigned __int64 *)(v_rsp - 232 - 72) = *(unsigned __int64 *)(v_rsp - 232 - 128);
    goto loc_00A2922C;
loc_00A291F9:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == ((unsigned int)((unsigned int)(0xC00000BBULL)))) {
        a2 = 9;
        a1 = a1;
        result = PipSetDevNodeProblem(a1, a2, (unsigned int)(0xC00000BBULL), a4);
        a1 = *(unsigned __int64 *)(a1 + 16);
        a2 = 0x200000ULL;
        result = PipSetDevNodeFlags(a1, a2, (unsigned int)(0xC00000BBULL), a4);
        a1 = *(unsigned __int64 *)(a1 + 16);
        a1 = (a1) + (40);
        result = PnpSetInvalidIDEvent(a1, a2, (unsigned int)(0xC00000BBULL), a4);
    }
loc_00A29230:
    if (!sign_flag) goto loc_00A29270;
    v_stack_m184 = (unsigned int)((unsigned int)((unsigned int)(result)));
    if (((*(unsigned int *)(a1 + 396)) & (0x2000ULL)) == 0) goto loc_00A2924D;
    if ((*(unsigned int *)(a1 + 404)) == 9) goto loc_00A29270;
loc_00A2924D:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != ((unsigned int)((unsigned int)(0xC000009AULL)))) goto loc_00A29263;
    goto loc_00A2926B;
loc_00A29263:
loc_00A2926B:
    result = PipSetDevNodeProblem(a1, 19, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), a4);
loc_00A29270:
    result = PiBuildDeviceNodeInstancePath(a1, *(unsigned __int64 *)(v_rsp - 232 - 32), *(unsigned __int64 *)(v_rsp - 232 - 120), *(unsigned __int64 *)(v_rsp - 232 - 128));
    if (sign_flag) goto loc_00A292E9;
    if (((*(unsigned __int8 *)(v_rip + 5009052)) & (16)) != 0) {
        result = *(unsigned __int64 *)(a1 + 16);
        a4 = a1;
        a1 = *(unsigned __int64 *)(result + 48);
        result = *(unsigned __int64 *)(a1 + 48);
        v_stack_m1C0 = a1;
        v_stack_m1C8 = result;
        result = McTemplateK0pzz_EtwWriteTransfer(a1, *(unsigned __int64 *)(v_rsp - 232 - 32), *(unsigned __int64 *)(v_rsp - 232 - 120), a4);
    }
    result = PiCreateDeviceInstanceKey(a1, v_stack_m178, v_stack_m18C, a4);
    result = 0;
    if (!sign_flag) goto loc_00A29314;
    result = PipSetDevNodeProblem(a1, result + 19, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), a4);
    v_stack_m170 = v_stack_m178;
    v_stack_m180 = (unsigned int)((unsigned int)(v_stack_m18C));
loc_00A292E9:
    v_stack_m184 = (unsigned int)((unsigned int)((unsigned int)(result)));
loc_00A292F2:
    result = PpMarkDeviceStackExtensionFlag(*(unsigned __int64 *)(a1 + 32), 16, 1, a4);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 300)))) != 769) goto loc_00A29337;
    goto loc_00A29341;
loc_00A29314:
    v_stack_m180 = (unsigned int)((unsigned int)(v_stack_m18C));
    result = (unsigned int)(*(unsigned int *)(a1 + 300));
    if (((unsigned int)((unsigned int)(v_stack_m18C))) == 1) { result = (unsigned int)((unsigned int)(0x20000ULL)); }
    v_stack_m170 = v_stack_m178;
    v_stack_m188 = (unsigned int)(result);
    goto loc_00A292F2;
loc_00A29337:
    if (((unsigned int)(result)) != 770) goto loc_00A29349;
loc_00A29341:
    result = PipSetDevNodeState(a1, result + 1, 1, a4);
loc_00A29349:
    if (((*(unsigned int *)(a1 + 396)) & (0x2000ULL)) == 0) goto loc_00A29372;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 404)))) == 9) goto loc_00A296E4;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 404))) + (-3));
    if ((((unsigned int)(result)) & (0xFFFFFFEFULL)) == 0) goto loc_00A296E4;
loc_00A29372:
    if (((unsigned int)((unsigned int)(v_stack_m18C))) == 1) goto loc_00A29824;
    result = PnpDeviceObjectFromDeviceInstanceWithTag(a1 + 40, (unsigned int)(0x65706E50ULL), 1, a4);
    if (result == 0) goto loc_00A296C3;
    if (result == (*(unsigned __int64 *)(a1 + 32))) goto loc_00A296B6;
    if ((unsigned __int8)(v_r15) == 0) goto loc_00A29484;
    result = ZwClose(v_stack_m178, (unsigned int)(0x65706E50ULL), 1, a4);
    a1 = 0;
    v_stack_m170 = 0;
    v_stack_m178 = 0;
    a3 = 0;
    result = PipSetDevNodeProblem(0, a1 + 42, a3, a4);
    result = PnpLogDuplicateDevice(*(unsigned __int64 *)(v_rsp - 232 - 32), *(unsigned __int64 *)(v_rsp - 232 - 128), a3, a4);
    if (((*(unsigned __int8 *)(v_rip + 5008702)) & (64)) != 0) {
        result = *(unsigned __int64 *)(a1 + 16);
        a4 = *(unsigned __int64 *)(v_rsp - 232 - 32);
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 312) + 40) + 16);
        result = *(unsigned __int64 *)(result + 48);
        v_stack_m1B0 = result;
        result = *(unsigned __int64 *)(a1 + 48);
        v_stack_m1B8 = result;
        result = *(unsigned __int64 *)(v_rsp - 232 - 120);
        v_stack_m1C0 = *(unsigned __int64 *)(v_rsp - 232 - 128);
        v_stack_m1C8 = result;
        result = McTemplateK0zzzzz_EtwWriteTransfer(a1, *(unsigned __int64 *)(v_rsp - 232 - 128), a3, a4);
    }
    result = *(unsigned __int64 *)(a1 + 16);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 312) + 40) + 16)) == (*(unsigned __int64 *)(a1 + 16))) {
        a2 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 8);
        a4 = result;
        a3 = *(unsigned __int64 *)(a1 + 32);
        a1 = 0;
        a2 = *(unsigned __int64 *)(a2 + 328);
        result = PpvUtilFailDriver(a1, a2, a3, a4);
    }
    result = ObfDereferenceObjectWithTag(result, (unsigned int)(0x65706E50ULL), a3, a4);
    result = PipMakeGloballyUniqueId(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 32), *(unsigned __int64 *)(v_rsp - 232 - 128), v_rsp - 232 - 128, a4);
    if (*(unsigned __int64 *)(v_rsp - 232 - 128) != 0) {
        a2 = 0;
        a1 = *(unsigned __int64 *)(v_rsp - 232 - 128);
        result = ExFreePoolWithTag(a1, a2, v_rsp - 232 - 128, a4);
    }
    *(unsigned __int64 *)(v_rsp - 232 - 72) = *(unsigned __int64 *)(v_rsp - 232 - 128);
    goto loc_00A29230;
loc_00A29484:
    a1 = 0;
    result = PpvUtilFailDriver(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 8) + 328), *(unsigned __int64 *)(a1 + 32), (unsigned int)(v_stack_m180));
    result = IoAddTriageDumpDataBlock(*(unsigned __int64 *)(a1 + 32), *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 32) + 2), *(unsigned __int64 *)(a1 + 32), (unsigned int)(v_stack_m180));
    v_rdi = 0;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 8) == 0) goto loc_00A294E9;
    result = IoAddTriageDumpDataBlock(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 8), (__int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 8) + 2)), *(unsigned __int64 *)(a1 + 32), (unsigned int)(v_stack_m180));
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 8)) + (56);
    if ((*(unsigned __int16 *)(a1)) == 0) goto loc_00A294EF;
    result = IoAddTriageDumpDataBlock(a1, (unsigned int)((unsigned int)(v_rdi + 2)), *(unsigned __int64 *)(a1 + 32), (unsigned int)(v_stack_m180));
    result = IoAddTriageDumpDataBlock(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 8) + 64), *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 8) + 56), *(unsigned __int64 *)(a1 + 32), (unsigned int)(v_stack_m180));
    goto loc_00A294EF;
loc_00A294E9:
loc_00A294EF:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 312) + 40) == 0) goto loc_00A295A6;
    result = IoAddTriageDumpDataBlock(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 312) + 40), 904, *(unsigned __int64 *)(a1 + 32), (unsigned int)(v_stack_m180));
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 312) + 40) + 40)) != 0) {
        a2 = 2;
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 312) + 40) + 40;
        result = IoAddTriageDumpDataBlock(a1, a2, *(unsigned __int64 *)(a1 + 32), (unsigned int)(v_stack_m180));
        a2 = *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 312) + 40) + 40);
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 312) + 40) + 40 + 8);
        result = IoAddTriageDumpDataBlock(a1, a2, *(unsigned __int64 *)(a1 + 32), (unsigned int)(v_stack_m180));
    }
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 312) + 40)) + (56);
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 312);
    if ((*(unsigned __int16 *)(a1)) != 0) {
        a2 = 2;
        result = IoAddTriageDumpDataBlock(a1, a2, *(unsigned __int64 *)(a1 + 32), (unsigned int)(v_stack_m180));
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 312);
        a1 = *(unsigned __int64 *)(result + 40);
        a2 = *(unsigned __int16 *)(a1 + 56);
        a1 = *(unsigned __int64 *)(a1 + 64);
        result = IoAddTriageDumpDataBlock(a1, a2, *(unsigned __int64 *)(a1 + 32), (unsigned int)(v_stack_m180));
    }
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 312) + 40) + 16) == 0) goto loc_00A295A6;
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 312) + 40) + 16);
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 312) + 40) + 16) + 56)) != 0) {
        a2 = 2;
        result = IoAddTriageDumpDataBlock(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 312) + 40) + 16) + 56, a2, *(unsigned __int64 *)(a1 + 32), (unsigned int)(v_stack_m180));
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 312);
        a1 = *(unsigned __int64 *)(result + 40);
        a1 = *(unsigned __int64 *)(a1 + 16);
        a2 = *(unsigned __int16 *)(a1 + 56);
        a1 = *(unsigned __int64 *)(a1 + 64);
        result = IoAddTriageDumpDataBlock(a1, a2, *(unsigned __int64 *)(a1 + 32), (unsigned int)(v_stack_m180));
    }
    result = IoAddTriageDumpDataBlock((unsigned int)(v_stack_m180), *(unsigned __int16 *)((unsigned int)(v_stack_m180) + 2), *(unsigned __int64 *)(a1 + 32), (unsigned int)(v_stack_m180));
    if (*(unsigned __int64 *)((unsigned int)(v_stack_m180) + 8) == 0) goto loc_00A295EA;
    result = IoAddTriageDumpDataBlock(*(unsigned __int64 *)((unsigned int)(v_stack_m180) + 8), (__int16)(*(unsigned __int16 *)(*(unsigned __int64 *)((unsigned int)(v_stack_m180) + 8) + 2)), *(unsigned __int64 *)(a1 + 32), (unsigned int)(v_stack_m180));
    a1 = (*(unsigned __int64 *)((unsigned int)(v_stack_m180) + 8)) + (56);
    if ((*(unsigned __int16 *)(a1)) != 0) {
        a2 = 2;
        result = IoAddTriageDumpDataBlock(a1, a2, *(unsigned __int64 *)(a1 + 32), (unsigned int)(v_stack_m180));
        a1 = *(unsigned __int64 *)((unsigned int)(v_stack_m180) + 8);
        a2 = *(unsigned __int16 *)(a1 + 56);
        a1 = *(unsigned __int64 *)(a1 + 64);
        result = IoAddTriageDumpDataBlock(a1, a2, *(unsigned __int64 *)(a1 + 32), (unsigned int)(v_stack_m180));
    }
    if (*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(v_stack_m180) + 312) + 40) == 0) goto loc_00A2969B;
    result = IoAddTriageDumpDataBlock(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(v_stack_m180) + 312) + 40), 904, *(unsigned __int64 *)(a1 + 32), (unsigned int)(v_stack_m180));
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(v_stack_m180) + 312) + 40) + 40)) != 0) {
        a2 = 2;
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(v_stack_m180) + 312) + 40) + 40;
        result = IoAddTriageDumpDataBlock(a1, a2, *(unsigned __int64 *)(a1 + 32), (unsigned int)(v_stack_m180));
        a2 = *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(v_stack_m180) + 312) + 40) + 40);
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(v_stack_m180) + 312) + 40) + 40 + 8);
        result = IoAddTriageDumpDataBlock(a1, a2, *(unsigned __int64 *)(a1 + 32), (unsigned int)(v_stack_m180));
    }
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(v_stack_m180) + 312) + 40)) + (56);
    result = *(unsigned __int64 *)((unsigned int)(v_stack_m180) + 312);
    if ((*(unsigned __int16 *)(a1)) != 0) {
        a2 = 2;
        result = IoAddTriageDumpDataBlock(a1, a2, *(unsigned __int64 *)(a1 + 32), (unsigned int)(v_stack_m180));
        result = *(unsigned __int64 *)((unsigned int)(v_stack_m180) + 312);
        a1 = *(unsigned __int64 *)(result + 40);
        a2 = *(unsigned __int16 *)(a1 + 56);
        a1 = *(unsigned __int64 *)(a1 + 64);
        result = IoAddTriageDumpDataBlock(a1, a2, *(unsigned __int64 *)(a1 + 32), (unsigned int)(v_stack_m180));
    }
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(v_stack_m180) + 312) + 40) + 16) == 0) goto loc_00A2969B;
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(v_stack_m180) + 312) + 40) + 16);
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(v_stack_m180) + 312) + 40) + 16) + 56)) != 0) {
        a2 = 2;
        result = IoAddTriageDumpDataBlock(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(v_stack_m180) + 312) + 40) + 16) + 56, a2, *(unsigned __int64 *)(a1 + 32), (unsigned int)(v_stack_m180));
        result = *(unsigned __int64 *)((unsigned int)(v_stack_m180) + 312);
        a1 = *(unsigned __int64 *)(result + 40);
        a1 = *(unsigned __int64 *)(a1 + 16);
        a2 = *(unsigned __int16 *)(a1 + 56);
        a1 = *(unsigned __int64 *)(a1 + 64);
        result = IoAddTriageDumpDataBlock(a1, a2, *(unsigned __int64 *)(a1 + 32), (unsigned int)(v_stack_m180));
    }
    v_stack_m1C8 = 0;
    result = KeBugCheckEx(202, 1, *(unsigned __int64 *)(a1 + 32), (unsigned int)(v_stack_m180));
loc_00A296B6:
    result = ObfDereferenceObjectWithTag((unsigned int)(v_stack_m180), (unsigned int)(0x65706E50ULL), *(unsigned __int64 *)(a1 + 32), (unsigned int)(v_stack_m180));
loc_00A296C3:
loc_00A296C7:
    if (((*(unsigned int *)(v_rdi + 396)) & (0x2000ULL)) == 0) goto loc_00A296E4;
    if ((*(unsigned int *)(v_rdi + 404)) == 42) {
        a1 = 0;
        result = PipClearDevNodeProblem(a1, (unsigned int)(0x65706E50ULL), *(unsigned __int64 *)(a1 + 32), (unsigned int)(v_stack_m180));
    }
    v_r12 = 0;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(v_stack_m180) + 312) + 40) + 40 == 0) goto loc_00A298C3;
    if (((unsigned int)((unsigned int)(v_stack_m180))) != ((unsigned int)(v_r12 + 1))) {
        a1 = *(unsigned __int64 *)(v_rdi + 48);
        a2 = *(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(v_stack_m180) + 312) + 40) + 40;
        result = PnpClearDeviceTemporaryProperties(a1, a2, *(unsigned __int64 *)(a1 + 32), (unsigned int)(v_stack_m180));
    }
    v_stack_m1A0 = (unsigned int)((unsigned int)(v_stack_m188));
    result = (unsigned int)((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rdi + 16) + 40)) + (2));
    v_stack_m1A8 = (unsigned int)(result);
    v_stack_m1B0 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 16) + 48);
    v_stack_m1B8 = 18;
    v_stack_m1C0 = v_rip - 10582000;
    v_stack_m1C8 = 0;
    result = PnpSetObjectProperty(*(unsigned __int64 *)(v_rip + 4443236), *(unsigned __int64 *)(v_rdi + 48), (unsigned int)((unsigned int)(v_r12 + 1)), *(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(v_stack_m180) + 312) + 40) + 40);
    v_stack_m1A0 = (unsigned int)((unsigned int)(v_stack_m188));
    v_stack_m1A8 = 8;
    v_stack_m1B0 = v_rsp - 232 + 8;
    v_stack_m1B8 = 16;
    v_stack_m1C0 = v_rip - 10492653;
    v_stack_m1C8 = 0;
    result = PnpSetObjectProperty(*(unsigned __int64 *)(v_rip + 4443186), *(unsigned __int64 *)(v_rdi + 48), (unsigned int)((unsigned int)(v_r12 + 1)), *(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(v_stack_m180) + 312) + 40) + 40);
    v_stack_m1A0 = (unsigned int)((unsigned int)(v_stack_m188));
    v_stack_m1A8 = 0;
    v_stack_m1B0 = 0;
    v_stack_m1B8 = 0;
    v_stack_m1C0 = v_rip - 10570287;
    v_stack_m1C8 = 0;
    result = PnpSetObjectProperty(*(unsigned __int64 *)(v_rip + 4443114), *(unsigned __int64 *)(v_rdi + 48), (unsigned int)((unsigned int)(v_r12 + 1)), *(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(v_stack_m180) + 312) + 40) + 40);
    v_stack_m1A0 = (unsigned int)((unsigned int)(v_stack_m188));
    v_stack_m1A8 = 4;
    v_stack_m1B0 = v_rip + 4442758;
    v_stack_m1B8 = 7;
    v_stack_m1C0 = v_rip - 10519864;
    v_stack_m1C8 = 0;
    result = PnpSetObjectProperty(*(unsigned __int64 *)(v_rip + 4443055), *(unsigned __int64 *)(v_rdi + 48), (unsigned int)((unsigned int)(v_r12 + 1)), *(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(v_stack_m180) + 312) + 40) + 40);
    goto loc_00A298C8;
loc_00A29824:
    v_r14 = ((unsigned int)(v_stack_m188)) | (-1);
    result = ExAcquireResourceSharedLite(v_rip + 5647820, (unsigned __int8)(v_r14 + 2), (unsigned int)((unsigned int)(v_r12 + 1)), *(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(v_stack_m180) + 312) + 40) + 40);
    a2 = 0;
    v_stack_m170 = v_stack_m178;
    if (v_stack_m178 == 0) goto loc_00A298A5;
    if (*(unsigned __int64 *)(v_rsp - 232 - 56) == 0) goto loc_00A298A5;
loc_00A2986A:
    result = (v_r14) + 1;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 232 - 56) + result * 2)) != 0) goto loc_00A2986A;
    v_stack_m1B0 = (unsigned int)((unsigned int)(v_stack_m188));
    v_stack_m1B8 = (unsigned int)(result * 2 + 2);
    v_stack_m1C0 = *(unsigned __int64 *)(v_rsp - 232 - 56);
    v_stack_m1C8 = (unsigned int)(v_r14 + 2);
    result = CmSetDeviceRegProp(*(unsigned __int64 *)(v_rip + 4442876), *(unsigned __int64 *)(v_rdi + 48), v_stack_m178, (unsigned int)((unsigned int)(v_r14 + 2)));
loc_00A298A5:
    result = ExReleaseResourceLite(v_rip + 5647700, *(unsigned __int64 *)(v_rdi + 48), v_stack_m178, (unsigned int)((unsigned int)(v_r14 + 2)));
    result = KeLeaveCriticalRegion(v_rip + 5647700, *(unsigned __int64 *)(v_rdi + 48), v_stack_m178, (unsigned int)((unsigned int)(v_r14 + 2)));
    v_stack_m180 = (unsigned int)((unsigned int)(v_stack_m18C));
    goto loc_00A296C7;
loc_00A298C3:
loc_00A298C8:
    if (((*(unsigned int *)(v_rsp - 232 + 100)) & (0x4000ULL)) == 0) goto loc_00A298FA;
    if (((*(unsigned int *)(v_rdi + 396)) & (0x2000ULL)) == 0) goto loc_00A298ED;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 404)))) == ((unsigned int)(v_r12 + 1))) goto loc_00A298FA;
    result = (unsigned int)(*(unsigned int *)(v_rdi + 404));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 404)))) != 14) {
        a2 = 29;
        a1 = 0;
        result = PnpDisableDevice(a1, a2, v_stack_m178, (unsigned int)((unsigned int)(v_r14 + 2)));
    }
    if (((*(unsigned int *)(v_rdi + 396)) & (0x2000ULL)) == 0) goto loc_00A29923;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 404)))) == 9) goto loc_00A29B5B;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rdi + 404))) + (-3));
    if ((((unsigned int)(result)) & (0xFFFFFFEFULL)) == 0) goto loc_00A29B5B;
loc_00A29923:
    v_rsi = ((unsigned int)(v_stack_m18C)) | (-1);
    result = ExAcquireResourceSharedLite(v_rip + 5647565, (unsigned __int8)(v_r12 + 1), v_stack_m178, (unsigned int)((unsigned int)(v_r14 + 2)));
    v_stack_m170 = v_stack_m178;
    if (v_stack_m178 == 0) goto loc_00A2999F;
    if (*(unsigned __int64 *)(v_rsp - 232 - 40) == 0) goto loc_00A2999F;
loc_00A29962:
    result = (v_rsi) + 1;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 232 - 40) + result * 2)) != 0) goto loc_00A29962;
    v_stack_m1B0 = (unsigned int)((unsigned int)(v_stack_m188));
    v_stack_m1B8 = (unsigned int)(result * 2 + 2);
    v_stack_m1C0 = *(unsigned __int64 *)(v_rsp - 232 - 40);
    v_stack_m1C8 = (unsigned int)(v_r12 + 1);
    result = CmSetDeviceRegProp(*(unsigned __int64 *)(v_rip + 4442627), *(unsigned __int64 *)(v_rdi + 48), v_stack_m178, 14);
loc_00A2999F:
    v_stack_m180 = (unsigned int)((unsigned int)(v_stack_m18C));
    a3 = (((unsigned int)((unsigned int)(v_stack_m18C))) == ((unsigned int)(v_r12 + 1))) ? 1 : 0;
    result = PnpSaveDeviceCapabilities(0, v_rsp - 232 + 96, a3, 14);
    a1 = (0) | (-1);
    if ((*(unsigned __int64 *)(v_rsp - 232 - 48)) != a1) {
        a2 = *(unsigned __int64 *)(v_rdi + 48);
        result = v_rsp - 232 - 48;
        a1 = *(unsigned __int64 *)(v_rip + 4442565);
        a4 = v_stack_m178;
        v_stack_m1A0 = (unsigned int)((unsigned int)(v_stack_m188));
        a3 = (unsigned int)(v_r12 + 1);
        v_stack_m1A8 = 8;
        v_stack_m1B0 = result;
        result = v_rip - 10493250;
        v_stack_m1B8 = 9;
        v_stack_m1C0 = result;
        v_stack_m1C8 = 0;
        result = PnpSetObjectProperty(a1, a2, a3, a4);
    }
    v_stack_m1B0 = 0;
    v_stack_m1B8 = v_rsp - 232 - 112;
    *(unsigned int *)(v_rsp - 232 - 112) = 4;
    v_stack_m1C0 = v_stack_m194;
    v_stack_m1C8 = v_rsp - 232 - 64;
    result = CmGetDeviceRegProp(*(unsigned __int64 *)(v_rip + 4442496), *(unsigned __int64 *)(v_rdi + 48), v_stack_m178, 11);
    if (sign_flag) goto loc_00A29A85;
    if ((*(unsigned int *)(v_rsp - 232 - 64)) != 4) goto loc_00A29A85;
    if ((*(unsigned int *)(v_rsp - 232 - 112)) != 4) goto loc_00A29A85;
    if ((((unsigned __int8)((unsigned int)(v_stack_m194))) & (32)) == 0) goto loc_00A29A79;
    if ((((unsigned __int8)(v_r12 + 1)) & ((unsigned __int8)((unsigned int)(v_stack_m194)))) == 0) goto loc_00A29A8F;
    goto loc_00A29A94;
loc_00A29A79:
    if ((((unsigned __int8)((unsigned int)(v_stack_m194))) & (64)) == 0) goto loc_00A29B01;
    goto loc_00A29A94;
loc_00A29A85:
    v_stack_m194 = 0;
loc_00A29A8F:
    v_stack_m198 = (unsigned __int8)(v_r12 + 1);
loc_00A29A94:
    if (((*(unsigned int *)(v_rsp - 232 + 100)) & (256)) == 0) goto loc_00A29ADF;
    v_stack_m1B0 = (unsigned int)((unsigned int)(v_stack_m188));
    v_stack_m194 = 0;
    v_stack_m1B8 = 4;
    v_stack_m1C0 = v_stack_m194;
    v_stack_m1C8 = 4;
    result = CmSetDeviceRegProp(*(unsigned __int64 *)(v_rip + 4442348), *(unsigned __int64 *)(v_rdi + 48), v_stack_m178, 11);
    goto loc_00A29B01;
loc_00A29ADF:
    if (((unsigned int)(*(unsigned __int64 *)(v_rdi + 48))) != 28) goto loc_00A29AF6;
    result = PiDevCfgGetFailedInstallProblemStatus(*(unsigned __int64 *)(v_rdi + 48), v_stack_m178, v_stack_m178, 11);
    goto loc_00A29AF9;
loc_00A29AF6:
    a3 = 0;
loc_00A29AF9:
    result = PipSetDevNodeProblem(0, 28, a3, 11);
loc_00A29B01:
    result = PnpMapDeviceObjectToDeviceInstance(*(unsigned __int64 *)(v_rdi + 32), v_rdi + 40, a3, 11);
    a1 = (unsigned int)(v_stack_m184);
    if (sign_flag) { a1 = (unsigned int)(result); }
    v_stack_m184 = (unsigned int)(a1);
    if ((*(unsigned __int8 *)(v_rip + 4067010)) == 0) goto loc_00A29B35;
    *(unsigned int *)(v_rsp - 232 - 104) = 2;
    goto loc_00A29B4A;
loc_00A29B35:
    result = (unsigned __int8)((unsigned int)(*(unsigned int *)(v_rsp - 232 - 108)));
    if (((v_stack_m194) & (0x40000ULL)) != 0) { result = (unsigned int)(v_r12 + 1); }
    *(unsigned int *)(v_rsp - 232 - 108) = (unsigned int)(result);
loc_00A29B4A:
    result = ExReleaseResourceLite(v_rip + 5647023, v_rdi + 40, a3, 11);
    result = KeLeaveCriticalRegion(v_rip + 5647023, v_rdi + 40, a3, 11);
loc_00A29B5B:
    *(unsigned int *)(v_rsp - 232 - 128) = 0;
    result = PnpIrpQueryID(*(unsigned __int64 *)(v_rdi + 32), (unsigned int)((unsigned int)(v_r12 + 1)), v_rsp - 232 - 80, 11);
    if (sign_flag) goto loc_00A29BA8;
    a4 = (unsigned int)((11) | (0xFFFFFFFFULL));
    result = (*(unsigned __int64 *)(v_rdi + 16)) + (56);
    v_stack_m1C8 = result;
    result = PnpFixupID(*(unsigned __int64 *)(v_rsp - 232 - 80), (unsigned int)(0x400ULL), (unsigned int)((unsigned int)(v_r12 + 1)), a4);
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)(result))) + ((unsigned int)((unsigned int)((unsigned int)(result)))));
    *(unsigned int *)(v_rsp - 232 - 128) = (unsigned int)(v_rbx);
    if (condition_is_not_equal) goto loc_00A29BFC;
    goto loc_00A29BAF;
loc_00A29BA8:
    if (((unsigned int)((unsigned int)(0xC0040038ULL))) != 0xC0040038ULL) goto loc_00A29BE2;
loc_00A29BAF:
    result = PipSetDevNodeProblem(0, 9, (unsigned int)((unsigned int)((unsigned int)(0xC0040038ULL))), a4);
    if (((*(unsigned int *)(*(unsigned __int64 *)(v_rdi + 16) + 396)) & ((unsigned int)((unsigned int)(0x200000ULL)))) == 0) {
        result = PipSetDevNodeFlags(*(unsigned __int64 *)(v_rdi + 16), (unsigned int)(0x200000ULL), (unsigned int)((unsigned int)((unsigned int)(0xC0040038ULL))), a4);
        a1 = *(unsigned __int64 *)(v_rdi + 16);
        a1 = (a1) + (40);
        result = PnpSetInvalidIDEvent(a1, (unsigned int)(0x200000ULL), (unsigned int)((unsigned int)((unsigned int)(0xC0040038ULL))), a4);
    }
    v_r14 = *(unsigned __int64 *)(v_rsp - 232 - 80);
    if (*(unsigned __int64 *)(v_rsp - 232 - 80) != 0) {
        a2 = 0;
        a1 = *(unsigned __int64 *)(v_rsp - 232 - 80);
        result = ExFreePoolWithTag(a1, a2, (unsigned int)((unsigned int)((unsigned int)(0xC0040038ULL))), a4);
        v_r14 = 0;
        *(unsigned __int64 *)(v_rsp - 232 - 80) = 0;
        *(unsigned int *)(v_rsp - 232 - 128) = 0;
    }
    result = KseAddHardwareId(v_r14, a2, (unsigned int)((unsigned int)((unsigned int)(0xC0040038ULL))), a4);
    *(unsigned int *)(v_rsp - 232 - 120) = 0;
    result = PnpIrpQueryID(*(unsigned __int64 *)(v_rdi + 32), 2, v_rsp - 232 - 88, a4);
    if (sign_flag) goto loc_00A29C56;
    a4 = (unsigned int)((a4) | (0xFFFFFFFFULL));
    result = (*(unsigned __int64 *)(v_rdi + 16)) + (56);
    v_stack_m1C8 = result;
    result = PnpFixupID(*(unsigned __int64 *)(v_rsp - 232 - 88), (unsigned int)(0x400ULL), (unsigned int)((unsigned int)(v_r12 + 1)), a4);
    v_r15 = (unsigned int)(((unsigned int)((unsigned int)(result))) + ((unsigned int)((unsigned int)((unsigned int)(result)))));
    *(unsigned int *)(v_rsp - 232 - 120) = (unsigned int)(v_r15);
    if (condition_is_not_equal) goto loc_00A29CAA;
    goto loc_00A29C5D;
loc_00A29C56:
    if (((unsigned int)((unsigned int)(0xC0040038ULL))) != 0xC0040038ULL) goto loc_00A29C90;
loc_00A29C5D:
    result = PipSetDevNodeProblem(0, 9, (unsigned int)((unsigned int)((unsigned int)(0xC0040038ULL))), a4);
    if (((*(unsigned int *)(*(unsigned __int64 *)(v_rdi + 16) + 396)) & ((unsigned int)((unsigned int)(0x200000ULL)))) == 0) {
        result = PipSetDevNodeFlags(*(unsigned __int64 *)(v_rdi + 16), (unsigned int)(0x200000ULL), (unsigned int)((unsigned int)((unsigned int)(0xC0040038ULL))), a4);
        a1 = *(unsigned __int64 *)(v_rdi + 16);
        a1 = (a1) + (40);
        result = PnpSetInvalidIDEvent(a1, (unsigned int)(0x200000ULL), (unsigned int)((unsigned int)((unsigned int)(0xC0040038ULL))), a4);
    }
    v_rsi = *(unsigned __int64 *)(v_rsp - 232 - 88);
    if (*(unsigned __int64 *)(v_rsp - 232 - 88) != 0) {
        a2 = 0;
        a1 = *(unsigned __int64 *)(v_rsp - 232 - 88);
        result = ExFreePoolWithTag(a1, a2, (unsigned int)((unsigned int)((unsigned int)(0xC0040038ULL))), a4);
        v_rsi = 0;
        *(unsigned __int64 *)(v_rsp - 232 - 88) = 0;
        *(unsigned int *)(v_rsp - 232 - 120) = 0;
    }
    result = PnpGenerateDeviceIdsHash(v_r14, v_rsi, v_rdi + 684, a4);
    result = PnpIrpQueryID(*(unsigned __int64 *)(v_rdi + 32), 5, v_rsp - 232 - 96, a4);
    if (*(unsigned __int64 *)(v_rsp - 232 - 96) == 0) goto loc_00A29D08;
    result = RtlInitUnicodeString(v_rsp - 232 - 8, *(unsigned __int64 *)(v_rsp - 232 - 96), v_rsp - 232 - 96, a4);
    result = RtlGUIDFromString(v_rsp - 232 - 8, v_rsp - 232 + 160, v_rsp - 232 - 96, a4);
    v_rbx = *(unsigned __int64 *)(v_rsp - 232 - 96);
    if (sign_flag) {
        a2 = 0;
        a1 = *(unsigned __int64 *)(v_rsp - 232 - 96);
        result = ExFreePoolWithTag(a1, a2, v_rsp - 232 - 96, a4);
        v_rbx = 0;
        *(unsigned __int64 *)(v_rsp - 232 - 96) = v_rbx;
    }
    result = PiQueryRemovableDeviceOverride(0, v_r14, v_rsi, v_stack_m190);
    if (!sign_flag) goto loc_00A29D4B;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rsp - 232 + 100)))) & (32)) != 0) goto loc_00A29D3B;
    if (condition_is_below) goto loc_00A29D3B;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rsp - 232 + 100)))) & (16)) == 0) goto loc_00A29D3B;
    goto loc_00A29D44;
loc_00A29D3B:
loc_00A29D44:
    if (v_rbx == 0) goto loc_00A29D56;
    goto loc_00A29D93;
loc_00A29D4B:
loc_00A29D56:
    v_stack_m1C8 = v_rsp - 232 - 24;
    a2 = 0;
    if (v_stack_m180 != 1) { a2 = v_stack_m170; }
    result = PipGenerateContainerID(0, a2, v_stack_m190, v_rbx);
    if (sign_flag) goto loc_00A29D93;
    if (v_rbx != 0) {
        a2 = 0;
        a1 = v_rbx;
        result = ExFreePoolWithTag(a1, a2, v_stack_m190, v_rbx);
    }
    *(unsigned __int64 *)(v_rsp - 232 - 96) = *(unsigned __int64 *)(v_rsp - 232 - 24);
loc_00A29D93:
    if (*(unsigned __int64 *)(v_rsp - 232 - 24) == 0) goto loc_00A29DBB;
    result = RtlInitUnicodeString(v_rsp - 232 - 8, *(unsigned __int64 *)(v_rsp - 232 - 24), v_stack_m190, v_rbx);
    result = RtlGUIDFromString(v_rsp - 232 - 8, v_rdi + 664, v_stack_m190, v_rbx);
    if (sign_flag) {
        *(unsigned __int64 *)(v_rdi + 664) = v_xmm0;
    }
    v_rsi = (v_rdi + 664) | (-1);
    result = ExAcquireResourceSharedLite(v_rip + 5646383, 1, v_stack_m190, v_rbx);
    result = PipSetDevNodeFlags(0, v_rsi + 33, v_stack_m190, v_rbx);
    result = ExReleaseResourceLite(v_rip + 5646383, v_rsi + 33, v_stack_m190, v_rbx);
    result = KeLeaveCriticalRegion(v_rip + 5646383, v_rsi + 33, v_stack_m190, v_rbx);
    if (v_stack_m178 == 0) goto loc_00A29E48;
    if ((*(unsigned __int64 *)(v_rsp - 232 - 96)) != 0) {
        result = *(unsigned __int64 *)(gs_base + (0 + 392));
        a2 = 1;
        a1 = v_rip + 5646383;
        result = ExAcquireResourceExclusiveLite(a1, a2, v_stack_m190, v_rbx);
        a3 = *(unsigned __int64 *)(v_rsp - 232 - 96);
        a2 = v_stack_m178;
        a1 = *(unsigned __int64 *)(v_rdi + 48);
        result = PiDcUpdateDeviceContainerMembership(a1, a2, a3, v_rbx);
        a1 = v_rip + 5646383;
        result = ExReleaseResourceLite(a1, a2, a3, v_rbx);
        result = KeLeaveCriticalRegion(a1, a2, a3, v_rbx);
    }
    result = ExAcquireResourceSharedLite(v_rip + 5646383, 1, a3, v_rbx);
    v_rbx = 0;
    if (v_stack_m178 == 0) goto loc_00A2A01D;
    if (v_stack_m198 != 0) goto loc_00A29EEF;
    if (v_stack_m18C == 1) goto loc_00A29EEF;
    v_stack_m1C0 = v_stack_m197;
    v_stack_m1C8 = 1;
    result = PnpCheckDeviceIdsChanged(0, v_stack_m178, *(unsigned __int64 *)(v_rsp - 232 - 80), (unsigned int)(*(unsigned int *)(v_rsp - 232 - 128)));
    a2 = 0;
    v_rbx = v_stack_m197;
    if (sign_flag) { v_rbx = 0; }
    v_stack_m197 = (unsigned __int8)(v_rbx);
    if ((unsigned __int8)(v_rbx) != 0) goto loc_00A29EF7;
    v_stack_m1C0 = v_stack_m197;
    v_stack_m1C8 = 0;
    result = PnpCheckDeviceIdsChanged(0, v_stack_m178, *(unsigned __int64 *)(v_rsp - 232 - 88), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 232 - 120)))));
    a2 = 0;
    v_rbx = v_stack_m197;
    if (sign_flag) { v_rbx = 0; }
    goto loc_00A29EF7;
loc_00A29EEF:
loc_00A29EF7:
    if (*(unsigned __int64 *)(v_rsp - 232 - 80) != 0) {
        result = v_stack_m188;
        a4 = 2;
        a2 = *(unsigned __int64 *)(v_rdi + 48);
        a3 = v_stack_m178;
        a1 = *(unsigned __int64 *)(v_rip + 4441220);
        v_stack_m1B0 = (unsigned int)(result);
        result = *(unsigned int *)(v_rsp - 232 - 128);
        v_stack_m1B8 = (unsigned int)(result);
        v_stack_m1C0 = *(unsigned __int64 *)(v_rsp - 232 - 80);
        v_stack_m1C8 = 7;
        result = CmSetDeviceRegProp(a1, a2, a3, a4);
    }
    if (*(unsigned __int64 *)(v_rsp - 232 - 88) != 0) {
        result = v_stack_m188;
        a4 = 3;
        a2 = *(unsigned __int64 *)(v_rdi + 48);
        a3 = v_stack_m178;
        a1 = *(unsigned __int64 *)(v_rip + 4441162);
        v_stack_m1B0 = (unsigned int)(result);
        v_stack_m1B8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 232 - 120)));
        v_stack_m1C0 = *(unsigned __int64 *)(v_rsp - 232 - 88);
        v_stack_m1C8 = 7;
        result = CmSetDeviceRegProp(a1, a2, a3, a4);
    }
    if ((unsigned __int8)(v_stack_m197) != 0) goto loc_00A29F79;
    v_rbx = 0;
    if ((*(unsigned __int8 *)(v_rsp - 232 - 108)) != 0) goto loc_00A29F7B;
    goto loc_00A2A01D;
loc_00A29F79:
    v_rbx = 0;
loc_00A29F7B:
    if (v_stack_m198 != 0) goto loc_00A29FAA;
    result = PpDevCfgCheckDeviceNeedsUpdate(*(unsigned __int64 *)(v_rdi + 48), v_stack_m178, v_stack_m17C, a4);
    if (sign_flag) goto loc_00A29FA6;
    a2 = (unsigned int)(((unsigned int)(v_stack_m194)) | ((unsigned int)((unsigned int)(v_stack_m17C))));
    v_stack_m194 = a2;
    goto loc_00A29FB2;
loc_00A29FA6:
    goto loc_00A29FB2;
loc_00A29FAA:
loc_00A29FB2:
    a1 = ((((unsigned __int8)((unsigned int)(v_stack_m17C))) & (32)) == 0) ? 1 : 0;
    result = (condition_is_above_or_equal) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) == 0) {
        result = v_stack_m188;
        a1 = 4;
        v_stack_m1B0 = (unsigned int)(result);
        v_stack_m1B8 = (unsigned int)(a1);
        result = v_stack_m194;
        v_stack_m1C0 = result;
        a3 = v_stack_m178;
        v_stack_m1C8 = (unsigned int)(a1);
        a4 = a1 + 7;
        a1 = *(unsigned __int64 *)(v_rip + 4440997);
        v_stack_m194 = (unsigned int)((unsigned int)(v_stack_m194));
        a2 = *(unsigned __int64 *)(v_rdi + 48);
        result = CmSetDeviceRegProp(a1, a2, a3, a4);
        a2 = v_stack_m194;
    }
    if ((((unsigned __int8)(a2)) & (32)) != 0) {
        a3 = 0;
        v_stack_m198 = 1;
        a1 = 0;
        a2 = a3 + 18;
        result = PipSetDevNodeProblem(a1, a2, a3, a4);
    }
    result = ExReleaseResourceLite(v_rip + 5645788, a2, a3, a4);
    result = KeLeaveCriticalRegion(v_rip + 5645788, a2, a3, a4);
    if (v_stack_m178 == 0) goto loc_00A2A12F;
    a1 = 0;
    v_stack_m170 = 0;
    v_stack_m17C = 0;
    if (*(unsigned __int64 *)(v_rsp - 232 - 56) == 0) goto loc_00A2A076;
    result = (0) | (-1);
loc_00A2A051:
    result = (result) + 1;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 232 - 56) + result * 2)) != 0) goto loc_00A2A051;
    result = PnpFindAlternateStringData(*(unsigned __int64 *)(v_rsp - 232 - 56), (unsigned int)((unsigned int)(result * 2 + 2)), v_stack_m170, v_stack_m17C);
loc_00A2A076:
    result = (unsigned int)(-(result));
    v_stack_m1A0 = (unsigned int)((unsigned int)(v_stack_m188));
    result = (unsigned int)((result) & (7));
    v_stack_m1A8 = (unsigned int)(result * 2 + 2);
    result = (unsigned int)((result) + (18));
    v_stack_m1B0 = *(unsigned __int64 *)(v_rsp - 232 - 56);
    v_rbx = 0;
    v_stack_m1B8 = (unsigned int)(result);
    v_stack_m1C0 = v_rip - 10495020;
    v_stack_m1C8 = 0;
    result = PnpSetObjectProperty(*(unsigned __int64 *)(v_rip + 4440853), *(unsigned __int64 *)(v_rdi + 48), v_rbx + 1, v_stack_m178);
    result = PnpGetDeviceLocationStrings(0, v_stack_m170, v_stack_m17C, v_stack_m178);
    if (!(sign_flag)) {
        result = v_stack_m17C;
        a4 = v_stack_m178;
        a1 = v_stack_m188;
        result = (unsigned int)((result) + ((unsigned int)(result)));
        v_rbx = v_stack_m170;
        a2 = *(unsigned __int64 *)(v_rdi + 48);
        v_stack_m1A0 = (unsigned int)(a1);
        a1 = *(unsigned __int64 *)(v_rip + 4440738);
        v_stack_m1A8 = (unsigned int)(result);
        result = v_rip - 10586721;
        v_stack_m1B0 = v_rbx;
        v_stack_m1B8 = 0x2012ULL;
        v_stack_m1C0 = result;
        result = 0;
        v_stack_m1C8 = 0;
        a3 = result + 1;
        result = PnpSetObjectProperty(a1, a2, a3, a4);
        a2 = 0;
        a1 = v_rbx;
        result = ExFreePoolWithTag(a1, a2, a3, a4);
        v_rbx = 0;
    }
    result = PnpQueryBusInformation(0, a2, a3, a4);
    a2 = 0;
    result = memset(v_rsp - 232 + 16, a2, a2 + 80, a4);
    result = PipDmgDestroyIommuExtension(0, a2, a2 + 80, a4);
    result = PiIommuGetInterface(*(unsigned __int64 *)(v_rdi + 32), v_rsp - 232 + 16, a2 + 80, a4);
    if (!(sign_flag)) {
        a2 = v_rsp - 232 + 16;
        a1 = 0;
        result = PipDmgInitializeIommuExtension(a1, a2, a2 + 80, a4);
        a1 = v_rsp - 232 + 16;
        v_rbx = (unsigned int)(result);
        result = PiIommuPutInterface(a1, a2, a2 + 80, a4);
        result = v_stack_m184;
        if (sign_flag) { result = (unsigned int)(v_rbx); }
        v_rbx = 0;
        v_stack_m184 = (unsigned int)(result);
    }
    if (((*(unsigned int *)(v_rsp - 232 + 100)) & (0x4000ULL)) != 0) goto loc_00A2A1D9;
    if (((*(unsigned int *)(v_rdi + 396)) & (0x2000ULL)) == 0) goto loc_00A2A1A3;
    if ((*(unsigned int *)(v_rdi + 404)) == 14) goto loc_00A2A1D9;
loc_00A2A1A3:
    if (v_stack_m198 == 0) goto loc_00A2A1C9;
    result = (unsigned int)(*(unsigned int *)(v_rsp - 232 - 104));
    if (v_stack_m18C == 1) {
        result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 232 - 104))) | (1));
    }
    result = PpDevCfgProcessDevice(0, v_stack_m178, (unsigned int)((unsigned int)(result)), a4);
    goto loc_00A2A1D9;
loc_00A2A1C9:
    if (v_stack_m178 != 0) {
        a2 = v_stack_m178;
        a1 = 0;
        result = PpDevCfgProcessDeviceOperations(a1, a2, (unsigned int)((unsigned int)(result)), a4);
    }
    result = PiQueryResourceRequirements(0, a2, (unsigned int)((unsigned int)(result)), a4);
    if (((*(unsigned int *)(v_rdi + 396)) & (0x2000ULL)) == 0) goto loc_00A2A211;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 404)))) == 22) goto loc_00A2A223;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 404)))) == 29) goto loc_00A2A223;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 404)))) == 14) goto loc_00A2A223;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 404)))) == 9) goto loc_00A2A223;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 404)))) == 3) goto loc_00A2A223;
    result = (unsigned int)(*(unsigned int *)(v_rdi + 404));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 404)))) != 19) {
        a2 = v_rdi + 40;
        a3 = 1;
        a1 = v_stack_m178;
        result = PnpIsDeviceInstanceEnabled(a1, a2, a3, a4);
    }
    if (v_stack_m178 != 0) {
        result = 1;
        a2 = v_stack_m178;
        a1 = 0;
        a3 = (v_stack_m18C == ((unsigned int)(result))) ? 1 : 0;
        result = PnpInitializeSessionId(a1, a2, a3, a4);
        result = 1;
        a2 = v_stack_m178;
        a1 = 0;
        a3 = (v_stack_m18C == ((unsigned int)(result))) ? 1 : 0;
        result = PnpInitializeInheritedRestrictedSd(a1, a2, a3, a4);
    }
    result = PiQueryAndAllocateBootResources(0, a2, a3, a4);
    if (((*(unsigned int *)(v_rdi + 396)) & (0x2000ULL)) == 0) goto loc_00A2A289;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 404)))) == 9) goto loc_00A2A313;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rdi + 404))) + (-3));
    if ((((unsigned int)(result)) & (0xFFFFFFEFULL)) == 0) goto loc_00A2A313;
loc_00A2A289:
    a1 = (0) | (-1);
    result = ExAcquireResourceSharedLite(v_rip + 5645142, (unsigned __int8)(a1 + 2), a3, a4);
    a3 = (v_stack_m18C == ((unsigned int)(a1 + 2))) ? 1 : 0;
    result = PnpSaveDeviceCapabilities(0, v_rsp - 232 + 96, a3, a4);
    result = ExReleaseResourceLite(v_rip + 5645109, v_rsp - 232 + 96, a3, a4);
    result = KeLeaveCriticalRegion(v_rip + 5645109, v_rsp - 232 + 96, a3, a4);
    result = PpHotSwapUpdateRemovalPolicy(0, v_rsp - 232 + 96, a3, a4);
    a4 = 0;
    result = PpDeviceRegistration(v_rdi + 40, (unsigned __int8)(a1 + 2), v_rdi + 56, a4);
    if (sign_flag) {
        a3 = (unsigned int)(result);
        a2 = a1 + 2 + 18;
        a1 = 0;
        result = PipSetDevNodeProblem(a1, a2, a3, a4);
    }
loc_00A2A313:
    if (((*(unsigned int *)(v_rdi + 396)) & (0x2000ULL)) == 0) goto loc_00A2A32F;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 404)))) == 9) goto loc_00A2A381;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 404)))) == 3) goto loc_00A2A381;
loc_00A2A32F:
    result = PnpIrpDeviceEnumerated(*(unsigned __int64 *)(a1 + 32), a2, a3, a4);
    if (v_stack_m178 != 0) {
        a2 = v_stack_m178;
        a1 = 0;
        result = PiUpdateDevicePanel(a1, a2, a3, a4);
    }
    if (*(unsigned __int64 *)(v_rdi + 48) != 0) {
        a3 = 1;
        result = PnpRaiseNtPlugPlayDevicePropertyChangeEvent(a1, *(unsigned __int64 *)(v_rdi + 48), a3, a4);
        a2 = *(unsigned __int64 *)(v_rdi + 48);
        a3 = 14;
        result = PnpRaiseNtPlugPlayDevicePropertyChangeEvent(a1, a2, a3, a4);
    }
    result = PnpSetPlugPlayEvent(v_rip - 10587492, *(unsigned __int64 *)(a1 + 32), a3, a4);
    result = PnpNewDeviceNodeDependencyCheck(0, *(unsigned __int64 *)(a1 + 32), a3, a4);
loc_00A2A381:
    if (*(unsigned __int64 *)(v_rsp - 232 - 80) != 0) {
        a2 = 0;
        a1 = *(unsigned __int64 *)(v_rsp - 232 - 80);
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
    if (*(unsigned __int64 *)(v_rsp - 232 - 88) != 0) {
        a2 = 0;
        a1 = *(unsigned __int64 *)(v_rsp - 232 - 88);
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
    if (*(unsigned __int64 *)(v_rsp - 232 - 96) != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(v_rsp - 232 - 96), a2, a3, a4);
    }
    if (v_stack_m178 != 0) {
        a1 = v_stack_m178;
        result = ZwClose(a1, a2, a3, a4);
    }
    if (*(unsigned __int64 *)(v_rsp - 232 - 72) != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(v_rsp - 232 - 72), a2, a3, a4);
    }
    if (*(unsigned __int64 *)(v_rsp - 232 - 40) != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(v_rsp - 232 - 40), a2, a3, a4);
    }
    if (*(unsigned __int64 *)(v_rsp - 232 - 56) != 0) {
        a2 = 0;
        a1 = *(unsigned __int64 *)(v_rsp - 232 - 56);
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
    if (*(unsigned __int64 *)(v_rsp - 232 - 32) != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(v_rsp - 232 - 32), a2, a3, a4);
    }
    if (*(unsigned __int64 *)(v_rsp - 232 - 16) != 0) {
        result = PiPnpRtlEndOperation(*(unsigned __int64 *)(v_rsp - 232 - 16), a2, a3, a4);
    }
    if (((*(unsigned __int8 *)(v_rip + 5004571)) & (16)) != 0) {
        a4 = 0;
        a2 = v_rip - 10497884;
        a3 = 0;
        result = McTemplateK0p_EtwWriteTransfer(*(unsigned __int64 *)(v_rsp - 232 - 16), a2, a3, a4);
    }
    if ((*(unsigned int *)(v_rdi + 568)) != 0) {
        a2 = (unsigned int)((unsigned int)(v_stack_m184));
        a1 = 0;
        result = PnpTraceDockDeviceEnumeration(a1, a2, a3, a4);
    }
    a1 = (*(unsigned __int64 *)(v_rsp - 232 + 176)) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PiProcessNewDeviceNode(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m170;
    uint64_t v_stack_m178;
    uint32_t v_stack_m17C;
    uint32_t v_stack_m180;
    uint32_t v_stack_m184;
    uint32_t v_stack_m188;
    uint32_t v_stack_m18C;
    uint8_t v_stack_m190;
    uint32_t v_stack_m194;
    uint8_t v_stack_m197;
    uint8_t v_stack_m198;
    uint32_t v_stack_m1A0;
    uint32_t v_stack_m1A8;
    uint64_t v_stack_m1B0;
    uint64_t v_stack_m1B8;
    uint64_t v_stack_m1C0;
    uint64_t v_stack_m1C8;
    uint64_t v_stack_m28;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (448);
    result = (*(uint64_t *)(v_rip + 0x3E17F3)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0xE8 + 0xB0) = result;
    local_r12 = 0;
    Arg2 = 0;
    *(uint64_t *)(local_rsp - 0xE8 - 0x60) = 0;
    *(uint64_t *)(local_rsp - 0xE8 - 0x20) = 0;
    result = memset(local_rsp - 232 + 96, Arg2, local_r12 + 64, a4);
    *(uint64_t *)(local_rsp - 0xE8 + 0xA0) = v_xmm0;
    *(uint64_t *)(local_rsp - 0xE8 - 0x58) = 0;
    *(uint64_t *)(local_rsp - 0xE8 - 0x8) = v_xmm0;
    *(uint64_t *)(local_rsp - 0xE8 - 0x38) = 0;
    *(uint64_t *)(local_rsp - 0xE8 - 0x78) = 0;
    *(uint64_t *)(local_rsp - 0xE8 - 0x10) = 0;
    *(uint64_t *)(local_rsp - 0xE8 - 0x50) = 0;
    *(uint64_t *)(local_rsp - 0xE8 - 0x48) = 0;
    *(uint64_t *)(local_rsp - 0xE8 - 0x28) = 0;
    *(uint64_t *)(local_rsp - 0xE8 - 0x18) = 0;
    *(uint32_t *)(local_rsp - 0xE8 - 0x70) = 0;
    *(uint32_t *)(local_rsp - 0xE8 - 0x40) = 0;
    v_stack_m190 = 0;
    *(uint64_t *)(local_rsp - 0xE8 - 0x80) = 0;
    if (((*(uint8_t *)(v_rip + 0x4C71AF)) & (16)) != 0) {
        a4 = Arg1;
        Arg2 = v_rip - 10494311;
        a3 = 0;
        result = McTemplateK0p_EtwWriteTransfer(local_rsp - 232 + 96, Arg2, a3, a4);
    }
    *(uint8_t *)(local_rsp - 0xE8 - 0x6C) = 0;
    v_stack_m198 = 0;
    *(uint32_t *)(local_rsp - 0xE8 - 0x68) = 0;
    v_stack_m180 = 0;
    *(uint64_t *)(local_rsp - 0xE8 + 0x8) = *(uint64_t *)(result);
    v_stack_m170 = 0;
    v_stack_m178 = 0;
    v_stack_m194 = 0;
    v_stack_m17C = 0;
    v_stack_m18C = 0;
    v_stack_m184 = 0;
    v_stack_m197 = 0;
    v_stack_m188 = 0;
    result = PiPnpRtlBeginOperation(local_rsp - 232 - 16, Arg2, a3, a4);
    result = PipClearDevNodeFlags(Arg1, (uint32_t)(0x2000000ULL), a3, a4);
    result = PnpQueryDeviceID(Arg1, local_rsp - 232 - 32, local_rsp - 232 - 120, a4);
    if (sign_flag) {
        local_r14 = (uint32_t)(result);
        Arg1 = 0xC0000001ULL;
        if (((uint32_t)(result)) == 0xC0040038ULL) { local_r14 = (uint32_t)(Arg1); }
        v_stack_m184 = (uint32_t)(local_r14);
    }
    result = PpIrpQueryCapabilities(*(uint64_t *)(arg1 + 0x20), local_rsp - 232 + 96, local_rsp - 232 - 120, a4);
    result = PipClearDevNodeUserFlags(Arg1, 2, local_rsp - 232 - 120, a4);
    if (sign_flag) goto loc_00A290AB;
    result = (uint32_t)(*(uint32_t *)(local_rsp - 0xE8 + 0x64));
    if (!(condition_is_above_or_equal)) {
        Arg2 = 1 + 1;
        Arg1 = Arg1;
        result = PipSetDevNodeUserFlags(Arg1, Arg2, local_rsp - 232 - 120, a4);
        result = *(uint32_t *)(local_rsp - 0xE8 + 0x64);
    }
    local_r15 = 0;
    if ((((uint8_t)(result)) & (64)) != 0) { local_r15 = 1; }
loc_00A290AB:
    if ((((uint8_t)(result)) & (32)) == 0) goto loc_00A290C5;
    if ((*(uint32_t *)(arg1 + 0x238)) == 4) {
        Arg1 = Arg1;
        result = PpProfileCancelTransitioningDock(Arg1, Arg2, local_rsp - 232 - 120, a4);
    }
    goto loc_00A290C8;
loc_00A290C5:
loc_00A290C8:
    *(uint32_t *)(arg1 + 0x238) = 0;
    result = (0) | (-1);
    *(uint64_t *)(local_rsp - 0xE8 - 0x30) = result;
    result = PnpQueryExtendedAddress(*(uint64_t *)(arg1 + 0x20), local_rsp - 232 - 48, local_rsp - 232 - 120, a4);
    Arg2 = 0;
    result = PnpQueryDeviceText(*(uint64_t *)(arg1 + 0x20), Arg2, local_rsp - 232 - 120, local_rsp - 232 - 56);
    result = PnpQueryDeviceText(*(uint64_t *)(arg1 + 0x20), 1, local_rsp - 232 - 120, local_rsp - 232 - 40);
    result = PnpIrpQueryID(*(uint64_t *)(arg1 + 0x20), 3, local_rsp - 232 - 72, local_rsp - 232 - 40);
    if (sign_flag) goto loc_00A29148;
    a4 = 0;
    result = (*(uint64_t *)(arg1 + 0x10)) + (56);
    a3 = 0;
    v_stack_m1C8 = result;
    result = PnpFixupID(*(uint64_t *)(local_rsp - 0xE8 - 0x48), 200, a3, a4);
    result = (uint32_t)((result) + ((uint32_t)(result)));
    if (condition_is_not_equal) goto loc_00A291A3;
    goto loc_00A29156;
loc_00A29148:
    if (((uint32_t)(result)) == 0xC0040038ULL) goto loc_00A29156;
    if (((uint32_t)(result)) != 0xC000009AULL) goto loc_00A2918D;
loc_00A29156:
    result = PipSetDevNodeProblem(Arg1, 9, (uint32_t)((uint32_t)((uint32_t)(0xC0040038ULL))), a4);
    if (((*(uint32_t *)(*(uint64_t *)(arg1 + 0x10) + 0x18C)) & (0x200000ULL)) == 0) {
        Arg2 = 0x200000ULL;
        result = PipSetDevNodeFlags(*(uint64_t *)(arg1 + 0x10), Arg2, (uint32_t)((uint32_t)((uint32_t)(0xC0040038ULL))), a4);
        Arg1 = *(uint64_t *)(arg1 + 0x10);
        Arg1 = (Arg1) + (40);
        result = PnpSetInvalidIDEvent(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(0xC0040038ULL))), a4);
    }
    local_r14 = *(uint64_t *)(local_rsp - 0xE8 - 0x48);
    if (*(uint64_t *)(local_rsp - 0xE8 - 0x48) != 0) {
        Arg2 = 0;
        Arg1 = *(uint64_t *)(local_rsp - 0xE8 - 0x48);
        result = ExFreePoolWithTag(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(0xC0040038ULL))), a4);
        local_r14 = 0;
        *(uint64_t *)(local_rsp - 0xE8 - 0x48) = 0;
    }
    if ((uint8_t)(local_r15) != 0) goto loc_00A291F9;
    if (((*(uint32_t *)(arg1 + 0x18C)) & (0x2000ULL)) == 0) goto loc_00A291BD;
    if ((*(uint32_t *)(arg1 + 0x194)) == 9) goto loc_00A2922C;
loc_00A291BD:
    if ((*(uint64_t *)(arg1 + 0x10)) == (*(uint64_t *)(v_rip + 0x563270))) goto loc_00A2922C;
    *(uint64_t *)(local_rsp - 0xE8 - 0x80) = 0;
    result = PipMakeGloballyUniqueId(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x20), local_r14, local_rsp - 232 - 128, a4);
    if (local_r14 != 0) {
        Arg2 = 0;
        Arg1 = local_r14;
        result = ExFreePoolWithTag(Arg1, Arg2, local_rsp - 232 - 128, a4);
    }
    *(uint64_t *)(local_rsp - 0xE8 - 0x48) = *(uint64_t *)(local_rsp - 0xE8 - 0x80);
    goto loc_00A2922C;
loc_00A291F9:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == ((uint32_t)((uint32_t)(0xC00000BBULL)))) {
        Arg2 = 9;
        Arg1 = Arg1;
        result = PipSetDevNodeProblem(Arg1, Arg2, (uint32_t)(0xC00000BBULL), a4);
        Arg1 = *(uint64_t *)(arg1 + 0x10);
        Arg2 = 0x200000ULL;
        result = PipSetDevNodeFlags(Arg1, Arg2, (uint32_t)(0xC00000BBULL), a4);
        Arg1 = *(uint64_t *)(arg1 + 0x10);
        Arg1 = (Arg1) + (40);
        result = PnpSetInvalidIDEvent(Arg1, Arg2, (uint32_t)(0xC00000BBULL), a4);
    }
loc_00A29230:
    if (!sign_flag) goto loc_00A29270;
    v_stack_m184 = (uint32_t)((uint32_t)((uint32_t)(result)));
    if (((*(uint32_t *)(arg1 + 0x18C)) & (0x2000ULL)) == 0) goto loc_00A2924D;
    if ((*(uint32_t *)(arg1 + 0x194)) == 9) goto loc_00A29270;
loc_00A2924D:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != ((uint32_t)((uint32_t)(0xC000009AULL)))) goto loc_00A29263;
    goto loc_00A2926B;
loc_00A29263:
loc_00A2926B:
    result = PipSetDevNodeProblem(Arg1, 19, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), a4);
loc_00A29270:
    result = PiBuildDeviceNodeInstancePath(Arg1, *(uint64_t *)(local_rsp - 0xE8 - 0x20), *(uint64_t *)(local_rsp - 0xE8 - 0x78), *(uint64_t *)(local_rsp - 0xE8 - 0x80));
    if (sign_flag) goto loc_00A292E9;
    if (((*(uint8_t *)(v_rip + 0x4C6E9C)) & (16)) != 0) {
        result = *(uint64_t *)(arg1 + 0x10);
        a4 = Arg1;
        Arg1 = *(uint64_t *)(result + 0x30);
        result = *(uint64_t *)(arg1 + 0x30);
        v_stack_m1C0 = Arg1;
        v_stack_m1C8 = result;
        result = McTemplateK0pzz_EtwWriteTransfer(Arg1, *(uint64_t *)(local_rsp - 0xE8 - 0x20), *(uint64_t *)(local_rsp - 0xE8 - 0x78), a4);
    }
    result = PiCreateDeviceInstanceKey(Arg1, v_stack_m178, v_stack_m18C, a4);
    result = 0;
    if (!sign_flag) goto loc_00A29314;
    result = PipSetDevNodeProblem(Arg1, result + 19, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), a4);
    v_stack_m170 = v_stack_m178;
    v_stack_m180 = (uint32_t)((uint32_t)(v_stack_m18C));
loc_00A292E9:
    v_stack_m184 = (uint32_t)((uint32_t)((uint32_t)(result)));
loc_00A292F2:
    result = PpMarkDeviceStackExtensionFlag(*(uint64_t *)(arg1 + 0x20), 16, 1, a4);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x12C)))) != 769) goto loc_00A29337;
    goto loc_00A29341;
loc_00A29314:
    v_stack_m180 = (uint32_t)((uint32_t)(v_stack_m18C));
    result = (uint32_t)(*(uint32_t *)(arg1 + 0x12C));
    if (((uint32_t)((uint32_t)(v_stack_m18C))) == 1) { result = (uint32_t)((uint32_t)(0x20000ULL)); }
    v_stack_m170 = v_stack_m178;
    v_stack_m188 = (uint32_t)(result);
    goto loc_00A292F2;
loc_00A29337:
    if (((uint32_t)(result)) != 770) goto loc_00A29349;
loc_00A29341:
    result = PipSetDevNodeState(Arg1, result + 1, 1, a4);
loc_00A29349:
    if (((*(uint32_t *)(arg1 + 0x18C)) & (0x2000ULL)) == 0) goto loc_00A29372;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x194)))) == 9) goto loc_00A296E4;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x194))) + (-3));
    if ((((uint32_t)(result)) & (0xFFFFFFEFULL)) == 0) goto loc_00A296E4;
loc_00A29372:
    if (((uint32_t)((uint32_t)(v_stack_m18C))) == 1) goto loc_00A29824;
    result = PnpDeviceObjectFromDeviceInstanceWithTag(Arg1 + 40, (uint32_t)(0x65706E50ULL), 1, a4);
    if (result == 0) goto loc_00A296C3;
    if (result == (*(uint64_t *)(arg1 + 0x20))) goto loc_00A296B6;
    if ((uint8_t)(local_r15) == 0) goto loc_00A29484;
    result = ZwClose(v_stack_m178, (uint32_t)(0x65706E50ULL), 1, a4);
    Arg1 = 0;
    v_stack_m170 = 0;
    v_stack_m178 = 0;
    a3 = 0;
    result = PipSetDevNodeProblem(0, Arg1 + 42, a3, a4);
    result = PnpLogDuplicateDevice(*(uint64_t *)(local_rsp - 0xE8 - 0x20), *(uint64_t *)(local_rsp - 0xE8 - 0x80), a3, a4);
    if (((*(uint8_t *)(v_rip + 0x4C6D3E)) & (64)) != 0) {
        result = *(uint64_t *)(arg1 + 0x10);
        a4 = *(uint64_t *)(local_rsp - 0xE8 - 0x20);
        Arg1 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x138) + 0x28) + 0x10);
        result = *(uint64_t *)(result + 0x30);
        v_stack_m1B0 = result;
        result = *(uint64_t *)(arg1 + 0x30);
        v_stack_m1B8 = result;
        result = *(uint64_t *)(local_rsp - 0xE8 - 0x78);
        v_stack_m1C0 = *(uint64_t *)(local_rsp - 0xE8 - 0x80);
        v_stack_m1C8 = result;
        result = McTemplateK0zzzzz_EtwWriteTransfer(Arg1, *(uint64_t *)(local_rsp - 0xE8 - 0x80), a3, a4);
    }
    result = *(uint64_t *)(arg1 + 0x10);
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x138) + 0x28) + 0x10)) == (*(uint64_t *)(arg1 + 0x10))) {
        Arg2 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x8);
        a4 = result;
        a3 = *(uint64_t *)(arg1 + 0x20);
        Arg1 = 0;
        Arg2 = *(uint64_t *)(Arg2 + 0x148);
        result = PpvUtilFailDriver(Arg1, Arg2, a3, a4);
    }
    result = ObfDereferenceObjectWithTag(result, (uint32_t)(0x65706E50ULL), a3, a4);
    result = PipMakeGloballyUniqueId(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x20), *(uint64_t *)(local_rsp - 0xE8 - 0x80), local_rsp - 232 - 128, a4);
    if (*(uint64_t *)(local_rsp - 0xE8 - 0x80) != 0) {
        Arg2 = 0;
        Arg1 = *(uint64_t *)(local_rsp - 0xE8 - 0x80);
        result = ExFreePoolWithTag(Arg1, Arg2, local_rsp - 232 - 128, a4);
    }
    *(uint64_t *)(local_rsp - 0xE8 - 0x48) = *(uint64_t *)(local_rsp - 0xE8 - 0x80);
    goto loc_00A29230;
loc_00A29484:
    Arg1 = 0;
    result = PpvUtilFailDriver(Arg1, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x8) + 0x148), *(uint64_t *)(arg1 + 0x20), (uint32_t)(v_stack_m180));
    result = IoAddTriageDumpDataBlock(*(uint64_t *)(arg1 + 0x20), *(uint16_t *)(*(uint64_t *)(arg1 + 0x20) + 0x2), *(uint64_t *)(arg1 + 0x20), (uint32_t)(v_stack_m180));
    local_rdi = 0;
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x8) == 0) goto loc_00A294E9;
    result = IoAddTriageDumpDataBlock(*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x8), (int16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x8) + 0x2)), *(uint64_t *)(arg1 + 0x20), (uint32_t)(v_stack_m180));
    Arg1 = (*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x8)) + (56);
    if ((*(uint16_t *)(arg1)) == 0) goto loc_00A294EF;
    result = IoAddTriageDumpDataBlock(Arg1, (uint32_t)((uint32_t)(local_rdi + 2)), *(uint64_t *)(arg1 + 0x20), (uint32_t)(v_stack_m180));
    result = IoAddTriageDumpDataBlock(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x8) + 0x40), *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x8) + 0x38), *(uint64_t *)(arg1 + 0x20), (uint32_t)(v_stack_m180));
    goto loc_00A294EF;
loc_00A294E9:
loc_00A294EF:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x138) + 0x28) == 0) goto loc_00A295A6;
    result = IoAddTriageDumpDataBlock(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x138) + 0x28), 904, *(uint64_t *)(arg1 + 0x20), (uint32_t)(v_stack_m180));
    if ((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x138) + 0x28) + 0x28)) != 0) {
        Arg2 = 2;
        Arg1 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x138) + 0x28) + 40;
        result = IoAddTriageDumpDataBlock(Arg1, Arg2, *(uint64_t *)(arg1 + 0x20), (uint32_t)(v_stack_m180));
        Arg2 = *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x138) + 0x28) + 0x28);
        Arg1 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x138) + 0x28) + 0x28 + 0x8);
        result = IoAddTriageDumpDataBlock(Arg1, Arg2, *(uint64_t *)(arg1 + 0x20), (uint32_t)(v_stack_m180));
    }
    Arg1 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x138) + 0x28)) + (56);
    result = *(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x138);
    if ((*(uint16_t *)(arg1)) != 0) {
        Arg2 = 2;
        result = IoAddTriageDumpDataBlock(Arg1, Arg2, *(uint64_t *)(arg1 + 0x20), (uint32_t)(v_stack_m180));
        result = *(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x138);
        Arg1 = *(uint64_t *)(result + 0x28);
        Arg2 = *(uint16_t *)(arg1 + 0x38);
        Arg1 = *(uint64_t *)(arg1 + 0x40);
        result = IoAddTriageDumpDataBlock(Arg1, Arg2, *(uint64_t *)(arg1 + 0x20), (uint32_t)(v_stack_m180));
    }
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x138) + 0x28) + 0x10) == 0) goto loc_00A295A6;
    result = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x138) + 0x28) + 0x10);
    if ((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x138) + 0x28) + 0x10) + 0x38)) != 0) {
        Arg2 = 2;
        result = IoAddTriageDumpDataBlock(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x138) + 0x28) + 0x10) + 56, Arg2, *(uint64_t *)(arg1 + 0x20), (uint32_t)(v_stack_m180));
        result = *(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x138);
        Arg1 = *(uint64_t *)(result + 0x28);
        Arg1 = *(uint64_t *)(arg1 + 0x10);
        Arg2 = *(uint16_t *)(arg1 + 0x38);
        Arg1 = *(uint64_t *)(arg1 + 0x40);
        result = IoAddTriageDumpDataBlock(Arg1, Arg2, *(uint64_t *)(arg1 + 0x20), (uint32_t)(v_stack_m180));
    }
    result = IoAddTriageDumpDataBlock((uint32_t)(v_stack_m180), *(uint16_t *)((uint32_t)(v_stack_m180) + 0x2), *(uint64_t *)(arg1 + 0x20), (uint32_t)(v_stack_m180));
    if (*(uint64_t *)((uint32_t)(v_stack_m180) + 0x8) == 0) goto loc_00A295EA;
    result = IoAddTriageDumpDataBlock(*(uint64_t *)((uint32_t)(v_stack_m180) + 0x8), (int16_t)(*(uint16_t *)(*(uint64_t *)((uint32_t)(v_stack_m180) + 0x8) + 0x2)), *(uint64_t *)(arg1 + 0x20), (uint32_t)(v_stack_m180));
    Arg1 = (*(uint64_t *)((uint32_t)(v_stack_m180) + 0x8)) + (56);
    if ((*(uint16_t *)(arg1)) != 0) {
        Arg2 = 2;
        result = IoAddTriageDumpDataBlock(Arg1, Arg2, *(uint64_t *)(arg1 + 0x20), (uint32_t)(v_stack_m180));
        Arg1 = *(uint64_t *)((uint32_t)(v_stack_m180) + 0x8);
        Arg2 = *(uint16_t *)(arg1 + 0x38);
        Arg1 = *(uint64_t *)(arg1 + 0x40);
        result = IoAddTriageDumpDataBlock(Arg1, Arg2, *(uint64_t *)(arg1 + 0x20), (uint32_t)(v_stack_m180));
    }
    if (*(uint64_t *)(*(uint64_t *)((uint32_t)(v_stack_m180) + 0x138) + 0x28) == 0) goto loc_00A2969B;
    result = IoAddTriageDumpDataBlock(*(uint64_t *)(*(uint64_t *)((uint32_t)(v_stack_m180) + 0x138) + 0x28), 904, *(uint64_t *)(arg1 + 0x20), (uint32_t)(v_stack_m180));
    if ((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(v_stack_m180) + 0x138) + 0x28) + 0x28)) != 0) {
        Arg2 = 2;
        Arg1 = *(uint64_t *)(*(uint64_t *)((uint32_t)(v_stack_m180) + 0x138) + 0x28) + 40;
        result = IoAddTriageDumpDataBlock(Arg1, Arg2, *(uint64_t *)(arg1 + 0x20), (uint32_t)(v_stack_m180));
        Arg2 = *(uint16_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(v_stack_m180) + 0x138) + 0x28) + 0x28);
        Arg1 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(v_stack_m180) + 0x138) + 0x28) + 0x28 + 0x8);
        result = IoAddTriageDumpDataBlock(Arg1, Arg2, *(uint64_t *)(arg1 + 0x20), (uint32_t)(v_stack_m180));
    }
    Arg1 = (*(uint64_t *)(*(uint64_t *)((uint32_t)(v_stack_m180) + 0x138) + 0x28)) + (56);
    result = *(uint64_t *)((uint32_t)(v_stack_m180) + 0x138);
    if ((*(uint16_t *)(arg1)) != 0) {
        Arg2 = 2;
        result = IoAddTriageDumpDataBlock(Arg1, Arg2, *(uint64_t *)(arg1 + 0x20), (uint32_t)(v_stack_m180));
        result = *(uint64_t *)((uint32_t)(v_stack_m180) + 0x138);
        Arg1 = *(uint64_t *)(result + 0x28);
        Arg2 = *(uint16_t *)(arg1 + 0x38);
        Arg1 = *(uint64_t *)(arg1 + 0x40);
        result = IoAddTriageDumpDataBlock(Arg1, Arg2, *(uint64_t *)(arg1 + 0x20), (uint32_t)(v_stack_m180));
    }
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(v_stack_m180) + 0x138) + 0x28) + 0x10) == 0) goto loc_00A2969B;
    result = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(v_stack_m180) + 0x138) + 0x28) + 0x10);
    if ((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(v_stack_m180) + 0x138) + 0x28) + 0x10) + 0x38)) != 0) {
        Arg2 = 2;
        result = IoAddTriageDumpDataBlock(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(v_stack_m180) + 0x138) + 0x28) + 0x10) + 56, Arg2, *(uint64_t *)(arg1 + 0x20), (uint32_t)(v_stack_m180));
        result = *(uint64_t *)((uint32_t)(v_stack_m180) + 0x138);
        Arg1 = *(uint64_t *)(result + 0x28);
        Arg1 = *(uint64_t *)(arg1 + 0x10);
        Arg2 = *(uint16_t *)(arg1 + 0x38);
        Arg1 = *(uint64_t *)(arg1 + 0x40);
        result = IoAddTriageDumpDataBlock(Arg1, Arg2, *(uint64_t *)(arg1 + 0x20), (uint32_t)(v_stack_m180));
    }
    v_stack_m1C8 = 0;
    result = KeBugCheckEx(202, 1, *(uint64_t *)(arg1 + 0x20), (uint32_t)(v_stack_m180));
loc_00A296B6:
    result = ObfDereferenceObjectWithTag((uint32_t)(v_stack_m180), (uint32_t)(0x65706E50ULL), *(uint64_t *)(arg1 + 0x20), (uint32_t)(v_stack_m180));
loc_00A296C3:
loc_00A296C7:
    if (((*(uint32_t *)(local_rdi + 0x18C)) & (0x2000ULL)) == 0) goto loc_00A296E4;
    if ((*(uint32_t *)(local_rdi + 0x194)) == 42) {
        Arg1 = 0;
        result = PipClearDevNodeProblem(Arg1, (uint32_t)(0x65706E50ULL), *(uint64_t *)(arg1 + 0x20), (uint32_t)(v_stack_m180));
    }
    local_r12 = 0;
    if (*(uint64_t *)(*(uint64_t *)((uint32_t)(v_stack_m180) + 0x138) + 0x28) + 40 == 0) goto loc_00A298C3;
    if (((uint32_t)((uint32_t)(v_stack_m180))) != ((uint32_t)(local_r12 + 1))) {
        Arg1 = *(uint64_t *)(local_rdi + 0x30);
        Arg2 = *(uint64_t *)(*(uint64_t *)((uint32_t)(v_stack_m180) + 0x138) + 0x28) + 40;
        result = PnpClearDeviceTemporaryProperties(Arg1, Arg2, *(uint64_t *)(arg1 + 0x20), (uint32_t)(v_stack_m180));
    }
    v_stack_m1A0 = (uint32_t)((uint32_t)(v_stack_m188));
    result = (uint32_t)((*(uint16_t *)(*(uint64_t *)(local_rdi + 0x10) + 0x28)) + (2));
    v_stack_m1A8 = (uint32_t)(result);
    v_stack_m1B0 = *(uint64_t *)(*(uint64_t *)(local_rdi + 0x10) + 0x30);
    v_stack_m1B8 = 18;
    v_stack_m1C0 = v_rip - 10582000;
    v_stack_m1C8 = 0;
    result = PnpSetObjectProperty(*(uint64_t *)(v_rip + 0x43CC64), *(uint64_t *)(local_rdi + 0x30), (uint32_t)((uint32_t)(local_r12 + 1)), *(uint64_t *)(*(uint64_t *)((uint32_t)(v_stack_m180) + 0x138) + 0x28) + 40);
    v_stack_m1A0 = (uint32_t)((uint32_t)(v_stack_m188));
    v_stack_m1A8 = 8;
    v_stack_m1B0 = local_rsp - 232 + 8;
    v_stack_m1B8 = 16;
    v_stack_m1C0 = v_rip - 10492653;
    v_stack_m1C8 = 0;
    result = PnpSetObjectProperty(*(uint64_t *)(v_rip + 0x43CC32), *(uint64_t *)(local_rdi + 0x30), (uint32_t)((uint32_t)(local_r12 + 1)), *(uint64_t *)(*(uint64_t *)((uint32_t)(v_stack_m180) + 0x138) + 0x28) + 40);
    v_stack_m1A0 = (uint32_t)((uint32_t)(v_stack_m188));
    v_stack_m1A8 = 0;
    v_stack_m1B0 = 0;
    v_stack_m1B8 = 0;
    v_stack_m1C0 = v_rip - 10570287;
    v_stack_m1C8 = 0;
    result = PnpSetObjectProperty(*(uint64_t *)(v_rip + 0x43CBEA), *(uint64_t *)(local_rdi + 0x30), (uint32_t)((uint32_t)(local_r12 + 1)), *(uint64_t *)(*(uint64_t *)((uint32_t)(v_stack_m180) + 0x138) + 0x28) + 40);
    v_stack_m1A0 = (uint32_t)((uint32_t)(v_stack_m188));
    v_stack_m1A8 = 4;
    v_stack_m1B0 = v_rip + 4442758;
    v_stack_m1B8 = 7;
    v_stack_m1C0 = v_rip - 10519864;
    v_stack_m1C8 = 0;
    result = PnpSetObjectProperty(*(uint64_t *)(v_rip + 0x43CBAF), *(uint64_t *)(local_rdi + 0x30), (uint32_t)((uint32_t)(local_r12 + 1)), *(uint64_t *)(*(uint64_t *)((uint32_t)(v_stack_m180) + 0x138) + 0x28) + 40);
    goto loc_00A298C8;
loc_00A29824:
    local_r14 = ((uint32_t)(v_stack_m188)) | (-1);
    result = ExAcquireResourceSharedLite(v_rip + 5647820, (uint8_t)(local_r14 + 2), (uint32_t)((uint32_t)(local_r12 + 1)), *(uint64_t *)(*(uint64_t *)((uint32_t)(v_stack_m180) + 0x138) + 0x28) + 40);
    Arg2 = 0;
    v_stack_m170 = v_stack_m178;
    if (v_stack_m178 == 0) goto loc_00A298A5;
    if (*(uint64_t *)(local_rsp - 0xE8 - 0x38) == 0) goto loc_00A298A5;
loc_00A2986A:
    result = (local_r14) + 1;
    if ((*(uint16_t *)(*(uint64_t *)(local_rsp - 0xE8 - 0x38) + result * 2)) != 0) goto loc_00A2986A;
    v_stack_m1B0 = (uint32_t)((uint32_t)(v_stack_m188));
    v_stack_m1B8 = (uint32_t)(result * 2 + 2);
    v_stack_m1C0 = *(uint64_t *)(local_rsp - 0xE8 - 0x38);
    v_stack_m1C8 = (uint32_t)(local_r14 + 2);
    result = CmSetDeviceRegProp(*(uint64_t *)(v_rip + 0x43CAFC), *(uint64_t *)(local_rdi + 0x30), v_stack_m178, (uint32_t)((uint32_t)(local_r14 + 2)));
loc_00A298A5:
    result = ExReleaseResourceLite(v_rip + 5647700, *(uint64_t *)(local_rdi + 0x30), v_stack_m178, (uint32_t)((uint32_t)(local_r14 + 2)));
    result = KeLeaveCriticalRegion(v_rip + 5647700, *(uint64_t *)(local_rdi + 0x30), v_stack_m178, (uint32_t)((uint32_t)(local_r14 + 2)));
    v_stack_m180 = (uint32_t)((uint32_t)(v_stack_m18C));
    goto loc_00A296C7;
loc_00A298C3:
loc_00A298C8:
    if (((*(uint32_t *)(local_rsp - 0xE8 + 0x64)) & (0x4000ULL)) == 0) goto loc_00A298FA;
    if (((*(uint32_t *)(local_rdi + 0x18C)) & (0x2000ULL)) == 0) goto loc_00A298ED;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x194)))) == ((uint32_t)(local_r12 + 1))) goto loc_00A298FA;
    result = (uint32_t)(*(uint32_t *)(local_rdi + 0x194));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x194)))) != 14) {
        Arg2 = 29;
        Arg1 = 0;
        result = PnpDisableDevice(Arg1, Arg2, v_stack_m178, (uint32_t)((uint32_t)(local_r14 + 2)));
    }
    if (((*(uint32_t *)(local_rdi + 0x18C)) & (0x2000ULL)) == 0) goto loc_00A29923;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x194)))) == 9) goto loc_00A29B5B;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rdi + 0x194))) + (-3));
    if ((((uint32_t)(result)) & (0xFFFFFFEFULL)) == 0) goto loc_00A29B5B;
loc_00A29923:
    local_rsi = ((uint32_t)(v_stack_m18C)) | (-1);
    result = ExAcquireResourceSharedLite(v_rip + 5647565, (uint8_t)(local_r12 + 1), v_stack_m178, (uint32_t)((uint32_t)(local_r14 + 2)));
    v_stack_m170 = v_stack_m178;
    if (v_stack_m178 == 0) goto loc_00A2999F;
    if (*(uint64_t *)(local_rsp - 0xE8 - 0x28) == 0) goto loc_00A2999F;
loc_00A29962:
    result = (local_rsi) + 1;
    if ((*(uint16_t *)(*(uint64_t *)(local_rsp - 0xE8 - 0x28) + result * 2)) != 0) goto loc_00A29962;
    v_stack_m1B0 = (uint32_t)((uint32_t)(v_stack_m188));
    v_stack_m1B8 = (uint32_t)(result * 2 + 2);
    v_stack_m1C0 = *(uint64_t *)(local_rsp - 0xE8 - 0x28);
    v_stack_m1C8 = (uint32_t)(local_r12 + 1);
    result = CmSetDeviceRegProp(*(uint64_t *)(v_rip + 0x43CA03), *(uint64_t *)(local_rdi + 0x30), v_stack_m178, 14);
loc_00A2999F:
    v_stack_m180 = (uint32_t)((uint32_t)(v_stack_m18C));
    a3 = (((uint32_t)((uint32_t)(v_stack_m18C))) == ((uint32_t)(local_r12 + 1))) ? 1 : 0;
    result = PnpSaveDeviceCapabilities(0, local_rsp - 232 + 96, a3, 14);
    Arg1 = (0) | (-1);
    if ((*(uint64_t *)(local_rsp - 0xE8 - 0x30)) != Arg1) {
        Arg2 = *(uint64_t *)(local_rdi + 0x30);
        result = local_rsp - 232 - 48;
        Arg1 = *(uint64_t *)(v_rip + 0x43C9C5);
        a4 = v_stack_m178;
        v_stack_m1A0 = (uint32_t)((uint32_t)(v_stack_m188));
        a3 = (uint32_t)(local_r12 + 1);
        v_stack_m1A8 = 8;
        v_stack_m1B0 = result;
        result = v_rip - 10493250;
        v_stack_m1B8 = 9;
        v_stack_m1C0 = result;
        v_stack_m1C8 = 0;
        result = PnpSetObjectProperty(Arg1, Arg2, a3, a4);
    }
    v_stack_m1B0 = 0;
    v_stack_m1B8 = local_rsp - 232 - 112;
    *(uint32_t *)(local_rsp - 0xE8 - 0x70) = 4;
    v_stack_m1C0 = v_stack_m194;
    v_stack_m1C8 = local_rsp - 232 - 64;
    result = CmGetDeviceRegProp(*(uint64_t *)(v_rip + 0x43C980), *(uint64_t *)(local_rdi + 0x30), v_stack_m178, 11);
    if (sign_flag) goto loc_00A29A85;
    if ((*(uint32_t *)(local_rsp - 0xE8 - 0x40)) != 4) goto loc_00A29A85;
    if ((*(uint32_t *)(local_rsp - 0xE8 - 0x70)) != 4) goto loc_00A29A85;
    if ((((uint8_t)((uint32_t)(v_stack_m194))) & (32)) == 0) goto loc_00A29A79;
    if ((((uint8_t)(local_r12 + 1)) & ((uint8_t)((uint32_t)(v_stack_m194)))) == 0) goto loc_00A29A8F;
    goto loc_00A29A94;
loc_00A29A79:
    if ((((uint8_t)((uint32_t)(v_stack_m194))) & (64)) == 0) goto loc_00A29B01;
    goto loc_00A29A94;
loc_00A29A85:
    v_stack_m194 = 0;
loc_00A29A8F:
    v_stack_m198 = (uint8_t)(local_r12 + 1);
loc_00A29A94:
    if (((*(uint32_t *)(local_rsp - 0xE8 + 0x64)) & (256)) == 0) goto loc_00A29ADF;
    v_stack_m1B0 = (uint32_t)((uint32_t)(v_stack_m188));
    v_stack_m194 = 0;
    v_stack_m1B8 = 4;
    v_stack_m1C0 = v_stack_m194;
    v_stack_m1C8 = 4;
    result = CmSetDeviceRegProp(*(uint64_t *)(v_rip + 0x43C8EC), *(uint64_t *)(local_rdi + 0x30), v_stack_m178, 11);
    goto loc_00A29B01;
loc_00A29ADF:
    if (((uint32_t)(*(uint64_t *)(local_rdi + 0x30))) != 28) goto loc_00A29AF6;
    result = PiDevCfgGetFailedInstallProblemStatus(*(uint64_t *)(local_rdi + 0x30), v_stack_m178, v_stack_m178, 11);
    goto loc_00A29AF9;
loc_00A29AF6:
    a3 = 0;
loc_00A29AF9:
    result = PipSetDevNodeProblem(0, 28, a3, 11);
loc_00A29B01:
    result = PnpMapDeviceObjectToDeviceInstance(*(uint64_t *)(local_rdi + 0x20), local_rdi + 40, a3, 11);
    Arg1 = (uint32_t)(v_stack_m184);
    if (sign_flag) { Arg1 = (uint32_t)(result); }
    v_stack_m184 = (uint32_t)(Arg1);
    if ((*(uint8_t *)(v_rip + 0x3E0EC2)) == 0) goto loc_00A29B35;
    *(uint32_t *)(local_rsp - 0xE8 - 0x68) = 2;
    goto loc_00A29B4A;
loc_00A29B35:
    result = (uint8_t)((uint32_t)(*(uint32_t *)(local_rsp - 0xE8 - 0x6C)));
    if (((v_stack_m194) & (0x40000ULL)) != 0) { result = (uint32_t)(local_r12 + 1); }
    *(uint32_t *)(local_rsp - 0xE8 - 0x6C) = (uint32_t)(result);
loc_00A29B4A:
    result = ExReleaseResourceLite(v_rip + 5647023, local_rdi + 40, a3, 11);
    result = KeLeaveCriticalRegion(v_rip + 5647023, local_rdi + 40, a3, 11);
loc_00A29B5B:
    *(uint32_t *)(local_rsp - 0xE8 - 0x80) = 0;
    result = PnpIrpQueryID(*(uint64_t *)(local_rdi + 0x20), (uint32_t)((uint32_t)(local_r12 + 1)), local_rsp - 232 - 80, 11);
    if (sign_flag) goto loc_00A29BA8;
    a4 = (uint32_t)((11) | (0xFFFFFFFFULL));
    result = (*(uint64_t *)(local_rdi + 0x10)) + (56);
    v_stack_m1C8 = result;
    result = PnpFixupID(*(uint64_t *)(local_rsp - 0xE8 - 0x50), (uint32_t)(0x400ULL), (uint32_t)((uint32_t)(local_r12 + 1)), a4);
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)(result))) + ((uint32_t)((uint32_t)((uint32_t)(result)))));
    *(uint32_t *)(local_rsp - 0xE8 - 0x80) = (uint32_t)(local_rbx);
    if (condition_is_not_equal) goto loc_00A29BFC;
    goto loc_00A29BAF;
loc_00A29BA8:
    if (((uint32_t)((uint32_t)(0xC0040038ULL))) != 0xC0040038ULL) goto loc_00A29BE2;
loc_00A29BAF:
    result = PipSetDevNodeProblem(0, 9, (uint32_t)((uint32_t)((uint32_t)(0xC0040038ULL))), a4);
    if (((*(uint32_t *)(*(uint64_t *)(local_rdi + 0x10) + 0x18C)) & ((uint32_t)((uint32_t)(0x200000ULL)))) == 0) {
        result = PipSetDevNodeFlags(*(uint64_t *)(local_rdi + 0x10), (uint32_t)(0x200000ULL), (uint32_t)((uint32_t)((uint32_t)(0xC0040038ULL))), a4);
        Arg1 = *(uint64_t *)(local_rdi + 0x10);
        Arg1 = (Arg1) + (40);
        result = PnpSetInvalidIDEvent(Arg1, (uint32_t)(0x200000ULL), (uint32_t)((uint32_t)((uint32_t)(0xC0040038ULL))), a4);
    }
    local_r14 = *(uint64_t *)(local_rsp - 0xE8 - 0x50);
    if (*(uint64_t *)(local_rsp - 0xE8 - 0x50) != 0) {
        Arg2 = 0;
        Arg1 = *(uint64_t *)(local_rsp - 0xE8 - 0x50);
        result = ExFreePoolWithTag(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(0xC0040038ULL))), a4);
        local_r14 = 0;
        *(uint64_t *)(local_rsp - 0xE8 - 0x50) = 0;
        *(uint32_t *)(local_rsp - 0xE8 - 0x80) = 0;
    }
    result = KseAddHardwareId(local_r14, Arg2, (uint32_t)((uint32_t)((uint32_t)(0xC0040038ULL))), a4);
    *(uint32_t *)(local_rsp - 0xE8 - 0x78) = 0;
    result = PnpIrpQueryID(*(uint64_t *)(local_rdi + 0x20), 2, local_rsp - 232 - 88, a4);
    if (sign_flag) goto loc_00A29C56;
    a4 = (uint32_t)((a4) | (0xFFFFFFFFULL));
    result = (*(uint64_t *)(local_rdi + 0x10)) + (56);
    v_stack_m1C8 = result;
    result = PnpFixupID(*(uint64_t *)(local_rsp - 0xE8 - 0x58), (uint32_t)(0x400ULL), (uint32_t)((uint32_t)(local_r12 + 1)), a4);
    local_r15 = (uint32_t)(((uint32_t)((uint32_t)(result))) + ((uint32_t)((uint32_t)((uint32_t)(result)))));
    *(uint32_t *)(local_rsp - 0xE8 - 0x78) = (uint32_t)(local_r15);
    if (condition_is_not_equal) goto loc_00A29CAA;
    goto loc_00A29C5D;
loc_00A29C56:
    if (((uint32_t)((uint32_t)(0xC0040038ULL))) != 0xC0040038ULL) goto loc_00A29C90;
loc_00A29C5D:
    result = PipSetDevNodeProblem(0, 9, (uint32_t)((uint32_t)((uint32_t)(0xC0040038ULL))), a4);
    if (((*(uint32_t *)(*(uint64_t *)(local_rdi + 0x10) + 0x18C)) & ((uint32_t)((uint32_t)(0x200000ULL)))) == 0) {
        result = PipSetDevNodeFlags(*(uint64_t *)(local_rdi + 0x10), (uint32_t)(0x200000ULL), (uint32_t)((uint32_t)((uint32_t)(0xC0040038ULL))), a4);
        Arg1 = *(uint64_t *)(local_rdi + 0x10);
        Arg1 = (Arg1) + (40);
        result = PnpSetInvalidIDEvent(Arg1, (uint32_t)(0x200000ULL), (uint32_t)((uint32_t)((uint32_t)(0xC0040038ULL))), a4);
    }
    local_rsi = *(uint64_t *)(local_rsp - 0xE8 - 0x58);
    if (*(uint64_t *)(local_rsp - 0xE8 - 0x58) != 0) {
        Arg2 = 0;
        Arg1 = *(uint64_t *)(local_rsp - 0xE8 - 0x58);
        result = ExFreePoolWithTag(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(0xC0040038ULL))), a4);
        local_rsi = 0;
        *(uint64_t *)(local_rsp - 0xE8 - 0x58) = 0;
        *(uint32_t *)(local_rsp - 0xE8 - 0x78) = 0;
    }
    result = PnpGenerateDeviceIdsHash(local_r14, local_rsi, local_rdi + 684, a4);
    result = PnpIrpQueryID(*(uint64_t *)(local_rdi + 0x20), 5, local_rsp - 232 - 96, a4);
    if (*(uint64_t *)(local_rsp - 0xE8 - 0x60) == 0) goto loc_00A29D08;
    result = RtlInitUnicodeString(local_rsp - 232 - 8, *(uint64_t *)(local_rsp - 0xE8 - 0x60), local_rsp - 232 - 96, a4);
    result = RtlGUIDFromString(local_rsp - 232 - 8, local_rsp - 232 + 160, local_rsp - 232 - 96, a4);
    local_rbx = *(uint64_t *)(local_rsp - 0xE8 - 0x60);
    if (sign_flag) {
        Arg2 = 0;
        Arg1 = *(uint64_t *)(local_rsp - 0xE8 - 0x60);
        result = ExFreePoolWithTag(Arg1, Arg2, local_rsp - 232 - 96, a4);
        local_rbx = 0;
        *(uint64_t *)(local_rsp - 0xE8 - 0x60) = local_rbx;
    }
    result = PiQueryRemovableDeviceOverride(0, local_r14, local_rsi, v_stack_m190);
    if (!sign_flag) goto loc_00A29D4B;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rsp - 0xE8 + 0x64)))) & (32)) != 0) goto loc_00A29D3B;
    if (condition_is_below) goto loc_00A29D3B;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rsp - 0xE8 + 0x64)))) & (16)) == 0) goto loc_00A29D3B;
    goto loc_00A29D44;
loc_00A29D3B:
loc_00A29D44:
    if (local_rbx == 0) goto loc_00A29D56;
    goto loc_00A29D93;
loc_00A29D4B:
loc_00A29D56:
    v_stack_m1C8 = local_rsp - 232 - 24;
    Arg2 = 0;
    if (v_stack_m180 != 1) { Arg2 = v_stack_m170; }
    result = PipGenerateContainerID(0, Arg2, v_stack_m190, local_rbx);
    if (sign_flag) goto loc_00A29D93;
    if (local_rbx != 0) {
        Arg2 = 0;
        Arg1 = local_rbx;
        result = ExFreePoolWithTag(Arg1, Arg2, v_stack_m190, local_rbx);
    }
    *(uint64_t *)(local_rsp - 0xE8 - 0x60) = *(uint64_t *)(local_rsp - 0xE8 - 0x18);
loc_00A29D93:
    if (*(uint64_t *)(local_rsp - 0xE8 - 0x18) == 0) goto loc_00A29DBB;
    result = RtlInitUnicodeString(local_rsp - 232 - 8, *(uint64_t *)(local_rsp - 0xE8 - 0x18), v_stack_m190, local_rbx);
    result = RtlGUIDFromString(local_rsp - 232 - 8, local_rdi + 664, v_stack_m190, local_rbx);
    if (sign_flag) {
        *(uint64_t *)(local_rdi + 0x298) = v_xmm0;
    }
    local_rsi = (local_rdi + 664) | (-1);
    result = ExAcquireResourceSharedLite(v_rip + 5646383, 1, v_stack_m190, local_rbx);
    result = PipSetDevNodeFlags(0, local_rsi + 33, v_stack_m190, local_rbx);
    result = ExReleaseResourceLite(v_rip + 5646383, local_rsi + 33, v_stack_m190, local_rbx);
    result = KeLeaveCriticalRegion(v_rip + 5646383, local_rsi + 33, v_stack_m190, local_rbx);
    if (v_stack_m178 == 0) goto loc_00A29E48;
    if ((*(uint64_t *)(local_rsp - 0xE8 - 0x60)) != 0) {
        result = *(uint64_t *)(gs_base + (0 + 0x188));
        Arg2 = 1;
        Arg1 = v_rip + 5646383;
        result = ExAcquireResourceExclusiveLite(Arg1, Arg2, v_stack_m190, local_rbx);
        a3 = *(uint64_t *)(local_rsp - 0xE8 - 0x60);
        Arg2 = v_stack_m178;
        Arg1 = *(uint64_t *)(local_rdi + 0x30);
        result = PiDcUpdateDeviceContainerMembership(Arg1, Arg2, a3, local_rbx);
        Arg1 = v_rip + 5646383;
        result = ExReleaseResourceLite(Arg1, Arg2, a3, local_rbx);
        result = KeLeaveCriticalRegion(Arg1, Arg2, a3, local_rbx);
    }
    result = ExAcquireResourceSharedLite(v_rip + 5646383, 1, a3, local_rbx);
    local_rbx = 0;
    if (v_stack_m178 == 0) goto loc_00A2A01D;
    if (v_stack_m198 != 0) goto loc_00A29EEF;
    if (v_stack_m18C == 1) goto loc_00A29EEF;
    v_stack_m1C0 = v_stack_m197;
    v_stack_m1C8 = 1;
    result = PnpCheckDeviceIdsChanged(0, v_stack_m178, *(uint64_t *)(local_rsp - 0xE8 - 0x50), (uint32_t)(*(uint32_t *)(local_rsp - 0xE8 - 0x80)));
    Arg2 = 0;
    local_rbx = v_stack_m197;
    if (sign_flag) { local_rbx = 0; }
    v_stack_m197 = (uint8_t)(local_rbx);
    if ((uint8_t)(local_rbx) != 0) goto loc_00A29EF7;
    v_stack_m1C0 = v_stack_m197;
    v_stack_m1C8 = 0;
    result = PnpCheckDeviceIdsChanged(0, v_stack_m178, *(uint64_t *)(local_rsp - 0xE8 - 0x58), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0xE8 - 0x78)))));
    Arg2 = 0;
    local_rbx = v_stack_m197;
    if (sign_flag) { local_rbx = 0; }
    goto loc_00A29EF7;
loc_00A29EEF:
loc_00A29EF7:
    if (*(uint64_t *)(local_rsp - 0xE8 - 0x50) != 0) {
        result = v_stack_m188;
        a4 = 2;
        Arg2 = *(uint64_t *)(local_rdi + 0x30);
        a3 = v_stack_m178;
        Arg1 = *(uint64_t *)(v_rip + 0x43C484);
        v_stack_m1B0 = (uint32_t)(result);
        result = *(uint32_t *)(local_rsp - 0xE8 - 0x80);
        v_stack_m1B8 = (uint32_t)(result);
        v_stack_m1C0 = *(uint64_t *)(local_rsp - 0xE8 - 0x50);
        v_stack_m1C8 = 7;
        result = CmSetDeviceRegProp(Arg1, Arg2, a3, a4);
    }
    if (*(uint64_t *)(local_rsp - 0xE8 - 0x58) != 0) {
        result = v_stack_m188;
        a4 = 3;
        Arg2 = *(uint64_t *)(local_rdi + 0x30);
        a3 = v_stack_m178;
        Arg1 = *(uint64_t *)(v_rip + 0x43C44A);
        v_stack_m1B0 = (uint32_t)(result);
        v_stack_m1B8 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0xE8 - 0x78)));
        v_stack_m1C0 = *(uint64_t *)(local_rsp - 0xE8 - 0x58);
        v_stack_m1C8 = 7;
        result = CmSetDeviceRegProp(Arg1, Arg2, a3, a4);
    }
    if ((uint8_t)(v_stack_m197) != 0) goto loc_00A29F79;
    local_rbx = 0;
    if ((*(uint8_t *)(local_rsp - 0xE8 - 0x6C)) != 0) goto loc_00A29F7B;
    goto loc_00A2A01D;
loc_00A29F79:
    local_rbx = 0;
loc_00A29F7B:
    if (v_stack_m198 != 0) goto loc_00A29FAA;
    result = PpDevCfgCheckDeviceNeedsUpdate(*(uint64_t *)(local_rdi + 0x30), v_stack_m178, v_stack_m17C, a4);
    if (sign_flag) goto loc_00A29FA6;
    Arg2 = (uint32_t)(((uint32_t)(v_stack_m194)) | ((uint32_t)((uint32_t)(v_stack_m17C))));
    v_stack_m194 = Arg2;
    goto loc_00A29FB2;
loc_00A29FA6:
    goto loc_00A29FB2;
loc_00A29FAA:
loc_00A29FB2:
    Arg1 = ((((uint8_t)((uint32_t)(v_stack_m17C))) & (32)) == 0) ? 1 : 0;
    result = (condition_is_above_or_equal) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) == 0) {
        result = v_stack_m188;
        Arg1 = 4;
        v_stack_m1B0 = (uint32_t)(result);
        v_stack_m1B8 = (uint32_t)(Arg1);
        result = v_stack_m194;
        v_stack_m1C0 = result;
        a3 = v_stack_m178;
        v_stack_m1C8 = (uint32_t)(Arg1);
        a4 = Arg1 + 7;
        Arg1 = *(uint64_t *)(v_rip + 0x43C3A5);
        v_stack_m194 = (uint32_t)((uint32_t)(v_stack_m194));
        Arg2 = *(uint64_t *)(local_rdi + 0x30);
        result = CmSetDeviceRegProp(Arg1, Arg2, a3, a4);
        Arg2 = v_stack_m194;
    }
    if ((((uint8_t)(Arg2)) & (32)) != 0) {
        a3 = 0;
        v_stack_m198 = 1;
        Arg1 = 0;
        Arg2 = a3 + 18;
        result = PipSetDevNodeProblem(Arg1, Arg2, a3, a4);
    }
    result = ExReleaseResourceLite(v_rip + 5645788, Arg2, a3, a4);
    result = KeLeaveCriticalRegion(v_rip + 5645788, Arg2, a3, a4);
    if (v_stack_m178 == 0) goto loc_00A2A12F;
    Arg1 = 0;
    v_stack_m170 = 0;
    v_stack_m17C = 0;
    if (*(uint64_t *)(local_rsp - 0xE8 - 0x38) == 0) goto loc_00A2A076;
    result = (0) | (-1);
loc_00A2A051:
    result = (result) + 1;
    if ((*(uint16_t *)(*(uint64_t *)(local_rsp - 0xE8 - 0x38) + result * 2)) != 0) goto loc_00A2A051;
    result = PnpFindAlternateStringData(*(uint64_t *)(local_rsp - 0xE8 - 0x38), (uint32_t)((uint32_t)(result * 2 + 2)), v_stack_m170, v_stack_m17C);
loc_00A2A076:
    result = (uint32_t)(-(result));
    v_stack_m1A0 = (uint32_t)((uint32_t)(v_stack_m188));
    result = (uint32_t)((result) & (7));
    v_stack_m1A8 = (uint32_t)(result * 2 + 2);
    result = (uint32_t)((result) + (18));
    v_stack_m1B0 = *(uint64_t *)(local_rsp - 0xE8 - 0x38);
    local_rbx = 0;
    v_stack_m1B8 = (uint32_t)(result);
    v_stack_m1C0 = v_rip - 10495020;
    v_stack_m1C8 = 0;
    result = PnpSetObjectProperty(*(uint64_t *)(v_rip + 0x43C315), *(uint64_t *)(local_rdi + 0x30), local_rbx + 1, v_stack_m178);
    result = PnpGetDeviceLocationStrings(0, v_stack_m170, v_stack_m17C, v_stack_m178);
    if (!(sign_flag)) {
        result = v_stack_m17C;
        a4 = v_stack_m178;
        Arg1 = v_stack_m188;
        result = (uint32_t)((result) + ((uint32_t)(result)));
        local_rbx = v_stack_m170;
        Arg2 = *(uint64_t *)(local_rdi + 0x30);
        v_stack_m1A0 = (uint32_t)(Arg1);
        Arg1 = *(uint64_t *)(v_rip + 0x43C2A2);
        v_stack_m1A8 = (uint32_t)(result);
        result = v_rip - 10586721;
        v_stack_m1B0 = local_rbx;
        v_stack_m1B8 = 0x2012ULL;
        v_stack_m1C0 = result;
        result = 0;
        v_stack_m1C8 = 0;
        a3 = result + 1;
        result = PnpSetObjectProperty(Arg1, Arg2, a3, a4);
        Arg2 = 0;
        Arg1 = local_rbx;
        result = ExFreePoolWithTag(Arg1, Arg2, a3, a4);
        local_rbx = 0;
    }
    result = PnpQueryBusInformation(0, Arg2, a3, a4);
    Arg2 = 0;
    result = memset(local_rsp - 232 + 16, Arg2, Arg2 + 80, a4);
    result = PipDmgDestroyIommuExtension(0, Arg2, Arg2 + 80, a4);
    result = PiIommuGetInterface(*(uint64_t *)(local_rdi + 0x20), local_rsp - 232 + 16, Arg2 + 80, a4);
    if (!(sign_flag)) {
        Arg2 = local_rsp - 232 + 16;
        Arg1 = 0;
        result = PipDmgInitializeIommuExtension(Arg1, Arg2, Arg2 + 80, a4);
        Arg1 = local_rsp - 232 + 16;
        local_rbx = (uint32_t)(result);
        result = PiIommuPutInterface(Arg1, Arg2, Arg2 + 80, a4);
        result = v_stack_m184;
        if (sign_flag) { result = (uint32_t)(local_rbx); }
        local_rbx = 0;
        v_stack_m184 = (uint32_t)(result);
    }
    if (((*(uint32_t *)(local_rsp - 0xE8 + 0x64)) & (0x4000ULL)) != 0) goto loc_00A2A1D9;
    if (((*(uint32_t *)(local_rdi + 0x18C)) & (0x2000ULL)) == 0) goto loc_00A2A1A3;
    if ((*(uint32_t *)(local_rdi + 0x194)) == 14) goto loc_00A2A1D9;
loc_00A2A1A3:
    if (v_stack_m198 == 0) goto loc_00A2A1C9;
    result = (uint32_t)(*(uint32_t *)(local_rsp - 0xE8 - 0x68));
    if (v_stack_m18C == 1) {
        result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0xE8 - 0x68))) | (1));
    }
    result = PpDevCfgProcessDevice(0, v_stack_m178, (uint32_t)((uint32_t)(result)), a4);
    goto loc_00A2A1D9;
loc_00A2A1C9:
    if (v_stack_m178 != 0) {
        Arg2 = v_stack_m178;
        Arg1 = 0;
        result = PpDevCfgProcessDeviceOperations(Arg1, Arg2, (uint32_t)((uint32_t)(result)), a4);
    }
    result = PiQueryResourceRequirements(0, Arg2, (uint32_t)((uint32_t)(result)), a4);
    if (((*(uint32_t *)(local_rdi + 0x18C)) & (0x2000ULL)) == 0) goto loc_00A2A211;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x194)))) == 22) goto loc_00A2A223;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x194)))) == 29) goto loc_00A2A223;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x194)))) == 14) goto loc_00A2A223;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x194)))) == 9) goto loc_00A2A223;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x194)))) == 3) goto loc_00A2A223;
    result = (uint32_t)(*(uint32_t *)(local_rdi + 0x194));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x194)))) != 19) {
        Arg2 = local_rdi + 40;
        a3 = 1;
        Arg1 = v_stack_m178;
        result = PnpIsDeviceInstanceEnabled(Arg1, Arg2, a3, a4);
    }
    if (v_stack_m178 != 0) {
        result = 1;
        Arg2 = v_stack_m178;
        Arg1 = 0;
        a3 = (v_stack_m18C == ((uint32_t)(result))) ? 1 : 0;
        result = PnpInitializeSessionId(Arg1, Arg2, a3, a4);
        result = 1;
        Arg2 = v_stack_m178;
        Arg1 = 0;
        a3 = (v_stack_m18C == ((uint32_t)(result))) ? 1 : 0;
        result = PnpInitializeInheritedRestrictedSd(Arg1, Arg2, a3, a4);
    }
    result = PiQueryAndAllocateBootResources(0, Arg2, a3, a4);
    if (((*(uint32_t *)(local_rdi + 0x18C)) & (0x2000ULL)) == 0) goto loc_00A2A289;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x194)))) == 9) goto loc_00A2A313;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rdi + 0x194))) + (-3));
    if ((((uint32_t)(result)) & (0xFFFFFFEFULL)) == 0) goto loc_00A2A313;
loc_00A2A289:
    Arg1 = (0) | (-1);
    result = ExAcquireResourceSharedLite(v_rip + 5645142, (uint8_t)(Arg1 + 2), a3, a4);
    a3 = (v_stack_m18C == ((uint32_t)(Arg1 + 2))) ? 1 : 0;
    result = PnpSaveDeviceCapabilities(0, local_rsp - 232 + 96, a3, a4);
    result = ExReleaseResourceLite(v_rip + 5645109, local_rsp - 232 + 96, a3, a4);
    result = KeLeaveCriticalRegion(v_rip + 5645109, local_rsp - 232 + 96, a3, a4);
    result = PpHotSwapUpdateRemovalPolicy(0, local_rsp - 232 + 96, a3, a4);
    a4 = 0;
    result = PpDeviceRegistration(local_rdi + 40, (uint8_t)(Arg1 + 2), local_rdi + 56, a4);
    if (sign_flag) {
        a3 = (uint32_t)(result);
        Arg2 = Arg1 + 2 + 18;
        Arg1 = 0;
        result = PipSetDevNodeProblem(Arg1, Arg2, a3, a4);
    }
loc_00A2A313:
    if (((*(uint32_t *)(local_rdi + 0x18C)) & (0x2000ULL)) == 0) goto loc_00A2A32F;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x194)))) == 9) goto loc_00A2A381;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x194)))) == 3) goto loc_00A2A381;
loc_00A2A32F:
    result = PnpIrpDeviceEnumerated(*(uint64_t *)(arg1 + 0x20), Arg2, a3, a4);
    if (v_stack_m178 != 0) {
        Arg2 = v_stack_m178;
        Arg1 = 0;
        result = PiUpdateDevicePanel(Arg1, Arg2, a3, a4);
    }
    if (*(uint64_t *)(local_rdi + 0x30) != 0) {
        a3 = 1;
        result = PnpRaiseNtPlugPlayDevicePropertyChangeEvent(Arg1, *(uint64_t *)(local_rdi + 0x30), a3, a4);
        Arg2 = *(uint64_t *)(local_rdi + 0x30);
        a3 = 14;
        result = PnpRaiseNtPlugPlayDevicePropertyChangeEvent(Arg1, Arg2, a3, a4);
    }
    result = PnpSetPlugPlayEvent(v_rip - 10587492, *(uint64_t *)(arg1 + 0x20), a3, a4);
    result = PnpNewDeviceNodeDependencyCheck(0, *(uint64_t *)(arg1 + 0x20), a3, a4);
loc_00A2A381:
    if (*(uint64_t *)(local_rsp - 0xE8 - 0x50) != 0) {
        Arg2 = 0;
        Arg1 = *(uint64_t *)(local_rsp - 0xE8 - 0x50);
        result = ExFreePoolWithTag(Arg1, Arg2, a3, a4);
    }
    if (*(uint64_t *)(local_rsp - 0xE8 - 0x58) != 0) {
        Arg2 = 0;
        Arg1 = *(uint64_t *)(local_rsp - 0xE8 - 0x58);
        result = ExFreePoolWithTag(Arg1, Arg2, a3, a4);
    }
    if (*(uint64_t *)(local_rsp - 0xE8 - 0x60) != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(*(uint64_t *)(local_rsp - 0xE8 - 0x60), Arg2, a3, a4);
    }
    if (v_stack_m178 != 0) {
        Arg1 = v_stack_m178;
        result = ZwClose(Arg1, Arg2, a3, a4);
    }
    if (*(uint64_t *)(local_rsp - 0xE8 - 0x48) != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(*(uint64_t *)(local_rsp - 0xE8 - 0x48), Arg2, a3, a4);
    }
    if (*(uint64_t *)(local_rsp - 0xE8 - 0x28) != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(*(uint64_t *)(local_rsp - 0xE8 - 0x28), Arg2, a3, a4);
    }
    if (*(uint64_t *)(local_rsp - 0xE8 - 0x38) != 0) {
        Arg2 = 0;
        Arg1 = *(uint64_t *)(local_rsp - 0xE8 - 0x38);
        result = ExFreePoolWithTag(Arg1, Arg2, a3, a4);
    }
    if (*(uint64_t *)(local_rsp - 0xE8 - 0x20) != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(*(uint64_t *)(local_rsp - 0xE8 - 0x20), Arg2, a3, a4);
    }
    if (*(uint64_t *)(local_rsp - 0xE8 - 0x10) != 0) {
        result = PiPnpRtlEndOperation(*(uint64_t *)(local_rsp - 0xE8 - 0x10), Arg2, a3, a4);
    }
    if (((*(uint8_t *)(v_rip + 0x4C5D1B)) & (16)) != 0) {
        a4 = 0;
        Arg2 = v_rip - 10497884;
        a3 = 0;
        result = McTemplateK0p_EtwWriteTransfer(*(uint64_t *)(local_rsp - 0xE8 - 0x10), Arg2, a3, a4);
    }
    if ((*(uint32_t *)(local_rdi + 0x238)) != 0) {
        Arg2 = (uint32_t)((uint32_t)(v_stack_m184));
        Arg1 = 0;
        result = PnpTraceDockDeviceEnumeration(Arg1, Arg2, a3, a4);
    }
    Arg1 = (*(uint64_t *)(local_rsp - 0xE8 + 0xB0)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, a3, a4);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x28` | `64` | `R` |
| `Arg1` | `+ 0x30` | `64` | `R` |
| `Arg1` | `+ 0x12C` | `32` | `R` |
| `Arg1` | `+ 0x18C` | `32` | `R` |
| `Arg1` | `+ 0x194` | `32` | `R` |
| `Arg1` | `+ 0x238` | `32` | `R` |
| `Arg1` | `+ 0x238` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A28F20&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
