# PnpGetObjectProperty

- RVA: `0x008E2180`–`0x008E283C` (길이 `1,724` bytes)
- VA: `0x00000001408E2180`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00085F58`
- 디코드: `418`개 명령, `1,724/1,724` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **21**; 고유 호출 대상: **15**
- 직접 호출자로 확인된 함수: **77**
- RIP 상대 이미지 참조: **9**

### Outgoing calls
- `0x008E225B` → [PiPnpRtlObjectActionCallback](PiPnpRtlObjectActionCallback_function_008E2850.md) (function, `0x008E2850`)
- `0x008E227F` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x008E2315` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x008E2394` → [_PnpDispatchDevice](_PnpDispatchDevice_function_008E1D60.md) (function, `0x008E1D60`)
- `0x008E23AF` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x008E23F0` → [PiPnpRtlObjectActionCallback](PiPnpRtlObjectActionCallback_function_008E2850.md) (function, `0x008E2850`)
- `0x008E2438` → [_PnpDispatchDeviceInterface](_PnpDispatchDeviceInterface_function_008E0DB0.md) (function, `0x008E0DB0`)
- `0x008E2506` → [RtlStringCchPrintfExW](../../text/42/RtlStringCchPrintfExW_function_0042B390.md) (function, `0x0042B390`)
- `0x008E258B` → [RtlStringCchPrintfExW](../../text/42/RtlStringCchPrintfExW_function_0042B390.md) (function, `0x0042B390`)
- `0x008E25C9` → [_RegRtlOpenKeyTransacted](_RegRtlOpenKeyTransacted_function_008EF810.md) (function, `0x008EF810`)
- `0x008E260B` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x008E2622` → [PnpValidatePropertyData](../8F/PnpValidatePropertyData_function_008F7658.md) (function, `0x008F7658`)
- `0x008E2655` → [DrvDbDispatchDriverPackage](../93/DrvDbDispatchDriverPackage_function_009303A0.md) (function, `0x009303A0`)
- `0x008E26D6` → [PnpRegQueryValueIndirect](PnpRegQueryValueIndirect_function_008EE210.md) (function, `0x008EE210`)
- `0x008E2737` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x008E2778` → [PnpOpenObjectRegKey](PnpOpenObjectRegKey_function_008E15E8.md) (function, `0x008E15E8`)
- `0x008E27D1` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x008E27DE` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x008E2805` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008E2825` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008E2832` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [PiRebalanceOptOut](../../text/5A/PiRebalanceOptOut_function_005AA664.md) at `0x005AA6EA`
- [PiRebalanceOptOut](../../text/5A/PiRebalanceOptOut_function_005AA664.md) at `0x005AA77C`
- [PipGetDeviceObjectLocation](../72/PipGetDeviceObjectLocation_function_00724EA4.md) at `0x00724F64`
- [PnpLogDeviceRequiresReboot](../72/PnpLogDeviceRequiresReboot_function_0072C818.md) at `0x0072C890`
- [PnpUpdateRebootRequiredReason](../72/PnpUpdateRebootRequiredReason_function_0072CE64.md) at `0x0072CED9`
- [PnpUpdateRebootRequiredReason](../72/PnpUpdateRebootRequiredReason_function_0072CE64.md) at `0x0072CF3C`
- [PiPnpRtlGatherInterfaceDeleteInfo](../72/PiPnpRtlGatherInterfaceDeleteInfo_function_0072FD48.md) at `0x0072FE2D`
- [PiPnpRtlGatherInterfaceDeleteInfo](../72/PiPnpRtlGatherInterfaceDeleteInfo_function_0072FD48.md) at `0x0072FF5A`
- [PiDmListInitEnumCallback](../73/PiDmListInitEnumCallback_function_007302E0.md) at `0x007303B0`
- [PiDcResetChildDeviceContainerCallback](../73/PiDcResetChildDeviceContainerCallback_function_00730DE0.md) at `0x00730F4B`
- [PiDevCfgGetDeviceClassDriverConfigurable](../73/PiDevCfgGetDeviceClassDriverConfigurable_function_00733504.md) at `0x007335AA`
- [PiDevCfgGetDeviceClassDriverConfigurable](../73/PiDevCfgGetDeviceClassDriverConfigurable_function_00733504.md) at `0x007336CB`
- [PiDevCfgGetFailedInstallProblemStatus](../73/PiDevCfgGetFailedInstallProblemStatus_function_00733730.md) at `0x0073378A`
- [PiDrvDbGetNodeSystemRoot](../74/PiDrvDbGetNodeSystemRoot_function_007411A4.md) at `0x0074125C`
- [PiDrvDbQuerySyncNodesUpdated](../74/PiDrvDbQuerySyncNodesUpdated_function_00741F70.md) at `0x007420E3`
- [PiDrvDbRegisterNode](../74/PiDrvDbRegisterNode_function_00742658.md) at `0x007429A1`
- [PiDrvDbSetupNodes](../74/PiDrvDbSetupNodes_function_00743D0C.md) at `0x00743DC2`
- [CmGetContainerBooleanPropertyCallback](../82/CmGetContainerBooleanPropertyCallback_function_0082B960.md) at `0x0082B9B4`
- [CmGetInstallerClassCompoundFiltersWorker](../83/CmGetInstallerClassCompoundFiltersWorker_function_00830130.md) at `0x00830253`
- [CmGetInstallerClassCompoundFiltersWorker](../83/CmGetInstallerClassCompoundFiltersWorker_function_00830130.md) at `0x008302DD`
- [CmGetInstallerClassCompoundFiltersWorker](../83/CmGetInstallerClassCompoundFiltersWorker_function_00830130.md) at `0x00830329`
- [CmGetInstallerClassCompoundFiltersWorker](../83/CmGetInstallerClassCompoundFiltersWorker_function_00830130.md) at `0x008303AC`
- [CmGetInstallerClassCompoundFiltersWorker](../83/CmGetInstallerClassCompoundFiltersWorker_function_00830130.md) at `0x008303FE`
- [CmGetInstallerClassCompoundFiltersWorker](../83/CmGetInstallerClassCompoundFiltersWorker_function_00830130.md) at `0x00830478`
- [CmGetInterfaceClassMappedPropertyFromComposite](../83/CmGetInterfaceClassMappedPropertyFromComposite_function_00830B68.md) at `0x00830C34`
- [sub_008E2DBC](Unknown_function_008E2DBC.md) at `0x008E2E83`
- [sub_008EDF25](Unknown_function_008EDF25.md) at `0x008EDFC6`
- [CmGetDeviceInterfaceMappedPropertyFromComposite](../8F/CmGetDeviceInterfaceMappedPropertyFromComposite_function_008F3D70.md) at `0x008F3F1A`
- [CmGetDeviceInterfaceMappedPropertyFromComposite](../8F/CmGetDeviceInterfaceMappedPropertyFromComposite_function_008F3D70.md) at `0x008F3FC5`
- [CmGetDeviceInterfaceMappedPropertyFromComposite](../8F/CmGetDeviceInterfaceMappedPropertyFromComposite_function_008F3D70.md) at `0x008F4011`
- [IoGetDeviceInterfaceAlias](../8F/IoGetDeviceInterfaceAlias_function_008F5570.md) at `0x008F577B`
- [PnpGetDeviceInterfacePropertyData](../8F/PnpGetDeviceInterfacePropertyData_function_008F6BD4.md) at `0x008F6D46`
- [PnpDeviceRaisePropertyChangeEventWorker](../8F/PnpDeviceRaisePropertyChangeEventWorker_function_008F80E0.md) at `0x008F82A0`
- [PiAuditDeviceStart](../8F/PiAuditDeviceStart_function_008FCEB4.md) at `0x008FCF18`
- [PipSetDevNodeProblem](../8F/PipSetDevNodeProblem_function_008FDE0C.md) at `0x008FDECE`
- [PnpGetDevicePropertyData](../90/PnpGetDevicePropertyData_function_009006D0.md) at `0x0090079D`
- [CmGetDeviceParent](../93/CmGetDeviceParent_function_00932368.md) at `0x00932556`
- [IopRegisterDeviceInterface](../95/IopRegisterDeviceInterface_function_009501B0.md) at `0x009503BC`
- [IopProcessSetInterfaceState](../95/IopProcessSetInterfaceState_function_00950964.md) at `0x00950B31`
- [PiDevCfgMigrateDevice](../96/PiDevCfgMigrateDevice_function_00963E60.md) at `0x00963F41`
- [PiDevCfgMigrateDevice](../96/PiDevCfgMigrateDevice_function_00963E60.md) at `0x00964011`
- [PiDevCfgResetDeviceDriverSettings](../96/PiDevCfgResetDeviceDriverSettings_function_00966168.md) at `0x00966277`
- [PiDevCfgQueryDriverConfiguration](../97/PiDevCfgQueryDriverConfiguration_function_0097584C.md) at `0x00975E1B`
- [PiDevCfgFindDeviceDriver](../97/PiDevCfgFindDeviceDriver_function_0097602C.md) at `0x009761D3`
- [PiDevCfgFindDeviceDriver](../97/PiDevCfgFindDeviceDriver_function_0097602C.md) at `0x00976279`
- [PiDevCfgProcessDevice](../97/PiDevCfgProcessDevice_function_00976D34.md) at `0x00977085`
- [PiDevCfgProcessDevice](../97/PiDevCfgProcessDevice_function_00976D34.md) at `0x00977332`
- [PiDevCfgQueryObjectProperties](../97/PiDevCfgQueryObjectProperties_function_0097776C.md) at `0x0097789E`
- [PiDevCfgConfigureDevice](../97/PiDevCfgConfigureDevice_function_00977BB4.md) at `0x0097887B`
- [PnpCallDriverQueryServiceHelper](../99/PnpCallDriverQueryServiceHelper_function_00995FB0.md) at `0x00996044`
- [CmIsDeviceSafeRemovalRequired](../9D/CmIsDeviceSafeRemovalRequired_function_009D1040.md) at `0x009D118C`
- [_CmGetDeviceMappedPropertyFromComposite](../9D/_CmGetDeviceMappedPropertyFromComposite_function_009D1684.md) at `0x009D1A26`
- [_CmGetDeviceMappedPropertyFromComposite](../9D/_CmGetDeviceMappedPropertyFromComposite_function_009D1684.md) at `0x009D1A82`
- [_CmGetDeviceMappedPropertyFromComposite](../9D/_CmGetDeviceMappedPropertyFromComposite_function_009D1684.md) at `0x009D1B1A`
- [_CmGetDeviceMappedPropertyFromComposite](../9D/_CmGetDeviceMappedPropertyFromComposite_function_009D1684.md) at `0x009D1B7D`
- [_CmGetDeviceMappedPropertyFromComposite](../9D/_CmGetDeviceMappedPropertyFromComposite_function_009D1684.md) at `0x009D208A`
- [_CmGetDeviceMappedPropertyFromComposite](../9D/_CmGetDeviceMappedPropertyFromComposite_function_009D1684.md) at `0x009D213A`
- [_CmGetDeviceMappedPropertyFromComposite](../9D/_CmGetDeviceMappedPropertyFromComposite_function_009D1684.md) at `0x009D21A0`
- [_CmGetDeviceMappedPropertyFromComposite](../9D/_CmGetDeviceMappedPropertyFromComposite_function_009D1684.md) at `0x009D23E3`
- [_CmGetDeviceMappedPropertyFromComposite](../9D/_CmGetDeviceMappedPropertyFromComposite_function_009D1684.md) at `0x009D2744`
- [_CmGetDeviceMappedPropertyFromComposite](../9D/_CmGetDeviceMappedPropertyFromComposite_function_009D1684.md) at `0x009D2873`
- [_CmGetInstallerClassMappedPropertyFromComposite](../9D/_CmGetInstallerClassMappedPropertyFromComposite_function_009D398C.md) at `0x009D3AF3`
- [_CmGetInstallerClassMappedPropertyFromComposite](../9D/_CmGetInstallerClassMappedPropertyFromComposite_function_009D398C.md) at `0x009D3B6A`
- [_CmGetInstallerClassMappedPropertyFromComposite](../9D/_CmGetInstallerClassMappedPropertyFromComposite_function_009D398C.md) at `0x009D3BD0`
- [_CmGetInstallerClassMappedPropertyFromComposite](../9D/_CmGetInstallerClassMappedPropertyFromComposite_function_009D398C.md) at `0x009D3C20`
- [PpForEachDeviceInstanceDriver](../A0/PpForEachDeviceInstanceDriver_function_00A07D2C.md) at `0x00A0802E`
- [PpForEachDeviceInstanceDriver](../A0/PpForEachDeviceInstanceDriver_function_00A07D2C.md) at `0x00A081A2`
- [_CmDeleteDeviceWorker](../A0/_CmDeleteDeviceWorker_function_00A08F48.md) at `0x00A0907E`
- [_CmUpdateDevicePanelInterface](../A0/_CmUpdateDevicePanelInterface_function_00A09FC4.md) at `0x00A0A114`
- [_CmUpdateDevicePanel](../A0/_CmUpdateDevicePanel_function_00A0A16C.md) at `0x00A0A2E7`
- [_CmUpdateDevicePanel](../A0/_CmUpdateDevicePanel_function_00A0A16C.md) at `0x00A0A409`
- [CmQueryDevicePanelPldProperty](../A0/CmQueryDevicePanelPldProperty_function_00A0AD88.md) at `0x00A0AE22`
- [CmGetParentDeviceContainerId](../A0/CmGetParentDeviceContainerId_function_00A0AF08.md) at `0x00A0AFBC`
- [PiPnpRtlServiceFilterCallback](../A0/PiPnpRtlServiceFilterCallback_function_00A0DB80.md) at `0x00A0DD1B`
- [PipCallDriverAddDevice](../A2/PipCallDriverAddDevice_function_00A272E0.md) at `0x00A2744C`
- [PipCallDriverAddDevice](../A2/PipCallDriverAddDevice_function_00A272E0.md) at `0x00A274D6`
- [PiUEventCacheObjectProperties](../A2/PiUEventCacheObjectProperties_function_00A2C458.md) at `0x00A2C556`
- [PiDcHandleDeviceEvent](../A5/PiDcHandleDeviceEvent_function_00A503B8.md) at `0x00A504A0`
- [PiDcHandleDeviceEvent](../A5/PiDcHandleDeviceEvent_function_00A503B8.md) at `0x00A50542`
- [PiDcHandleInterfaceEvent](../A5/PiDcHandleInterfaceEvent_function_00A50588.md) at `0x00A50628`
- [PiDcGenerateConfigNotificationIfContainerRequiresConfiguration](../A5/PiDcGenerateConfigNotificationIfContainerRequiresConfiguration_function_00A506F8.md) at `0x00A5075E`
- [PiAuditDeviceOperation](../A8/PiAuditDeviceOperation_function_00A864DC.md) at `0x00A86631`
- [PiAuditDeviceOperation](../A8/PiAuditDeviceOperation_function_00A864DC.md) at `0x00A866C9`
- [PiAuditDeviceOperation](../A8/PiAuditDeviceOperation_function_00A864DC.md) at `0x00A86768`
- [PiAuditDeviceOperation](../A8/PiAuditDeviceOperation_function_00A864DC.md) at `0x00A867E7`
- [PiAuditDeviceOperation](../A8/PiAuditDeviceOperation_function_00A864DC.md) at `0x00A86866`
- [PiAuditDeviceOperation](../A8/PiAuditDeviceOperation_function_00A864DC.md) at `0x00A868FF`
- [CmMatchLastKnownParentCallback](../A8/CmMatchLastKnownParentCallback_function_00A89E50.md) at `0x00A89EBE`
- [PiUEventDeviceNeedsInstall](../A8/PiUEventDeviceNeedsInstall_function_00A8B1BC.md) at `0x00A8B22B`
- [PiUEventDeviceNeedsInstall](../A8/PiUEventDeviceNeedsInstall_function_00A8B1BC.md) at `0x00A8B27F`
- [PiUEventDeviceNeedsInstall](../A8/PiUEventDeviceNeedsInstall_function_00A8B1BC.md) at `0x00A8B2F8`
- [PiDcContainerRequiresConfiguration](../AB/PiDcContainerRequiresConfiguration_function_00AB6004.md) at `0x00AB6089`
- [PiDevCfgGetDeviceClassConfigFlags](../AC/PiDevCfgGetDeviceClassConfigFlags_function_00AC7248.md) at `0x00AC72B4`
- [PiDevCfgGetDeviceClassConfigFlags](../AC/PiDevCfgGetDeviceClassConfigFlags_function_00AC7248.md) at `0x00AC730F`
- [PnpGetDeviceInstancePropertyData](../AC/PnpGetDeviceInstancePropertyData_function_00AC9730.md) at `0x00AC9840`
- [PiPnpRtlGatherInstallerClassChangeInfo](../AD/PiPnpRtlGatherInstallerClassChangeInfo_function_00AD26FC.md) at `0x00AD27F2`
- [IopDeviceObjectFromSymbolicName](../AD/IopDeviceObjectFromSymbolicName_function_00AD63EC.md) at `0x00AD64A8`
- [PiCMUnregisterDeviceInterface](../AD/PiCMUnregisterDeviceInterface_function_00AD9758.md) at `0x00AD9855`
- [CmGetDeviceCompoundFiltersWorker](../AF/CmGetDeviceCompoundFiltersWorker_function_00AF9CE8.md) at `0x00AF9E0B`
- [CmGetDeviceCompoundFiltersWorker](../AF/CmGetDeviceCompoundFiltersWorker_function_00AF9CE8.md) at `0x00AF9E95`
- [CmGetDeviceCompoundFiltersWorker](../AF/CmGetDeviceCompoundFiltersWorker_function_00AF9CE8.md) at `0x00AF9F27`
- [CmGetDeviceCompoundFiltersWorker](../AF/CmGetDeviceCompoundFiltersWorker_function_00AF9CE8.md) at `0x00AF9FAA`
- [CmGetDeviceCompoundFiltersWorker](../AF/CmGetDeviceCompoundFiltersWorker_function_00AF9CE8.md) at `0x00AF9FFC`
- [CmGetDeviceCompoundFiltersWorker](../AF/CmGetDeviceCompoundFiltersWorker_function_00AF9CE8.md) at `0x00AFA076`
- [sub_00B1D11D](../B1/Unknown_function_00B1D11D.md) at `0x00B1D17B`
- [sub_00B1D252](../B1/Unknown_function_00B1D252.md) at `0x00B1D2CC`
- [sub_00B1E436](../B1/Unknown_function_00B1E436.md) at `0x00B1E50E`
- [sub_00B1E436](../B1/Unknown_function_00B1E436.md) at `0x00B1E5B7`
- [sub_00B1EBE0](../B1/Unknown_function_00B1EBE0.md) at `0x00B1ECA4`
- [sub_00B1EBE0](../B1/Unknown_function_00B1EBE0.md) at `0x00B1EE0D`
- [sub_00B2834C](../B2/Unknown_function_00B2834C.md) at `0x00B283AB`
- [sub_00B2C332](../B2/Unknown_function_00B2C332.md) at `0x00B2C375`
- [sub_00B2C5F4](../B2/Unknown_function_00B2C5F4.md) at `0x00B2C6D6`
- [sub_00B2F242](../B2/Unknown_function_00B2F242.md) at `0x00B2F294`
- [sub_00B2F242](../B2/Unknown_function_00B2F242.md) at `0x00B2F30B`
- [sub_00B2F242](../B2/Unknown_function_00B2F242.md) at `0x00B2F39B`
- [sub_00B2F242](../B2/Unknown_function_00B2F242.md) at `0x00B2F3FD`
- [sub_00B2F6AC](../B2/Unknown_function_00B2F6AC.md) at `0x00B2F6FF`
- [sub_00B34C12](../B3/Unknown_function_00B34C12.md) at `0x00B34DEB`
- [sub_00B34E9C](../B3/Unknown_function_00B34E9C.md) at `0x00B34EDC`
- [sub_00B34E9C](../B3/Unknown_function_00B34E9C.md) at `0x00B3590C`
- [sub_00B34E9C](../B3/Unknown_function_00B34E9C.md) at `0x00B3615B`
- [sub_00B3807C](../B3/Unknown_function_00B3807C.md) at `0x00B380C8`
- [sub_00B3807C](../B3/Unknown_function_00B3807C.md) at `0x00B38304`
- [sub_00B38C36](../B3/Unknown_function_00B38C36.md) at `0x00B38CA0`
- [sub_00B3C62C](../B3/Unknown_function_00B3C62C.md) at `0x00B3C675`
- [sub_00B44AC4](../B4/Unknown_function_00B44AC4.md) at `0x00B44B2F`
- [sub_00B46EDE](../B4/Unknown_function_00B46EDE.md) at `0x00B46F29`
- [sub_00B46EDE](../B4/Unknown_function_00B46EDE.md) at `0x00B46FB4`
- [sub_00B46EDE](../B4/Unknown_function_00B46EDE.md) at `0x00B47016`

### Static image references
- `0x008E219C` → RVA `0x00E0A740` (`.data`; read)
- `0x008E21B4` → RVA `0x008E2850` (`PiPnpRtlObjectActionCallback`; read)
- `0x008E2362` → RVA `0x008E1D60` (`_PnpDispatchDevice`; read)
- `0x008E241C` → RVA `0x008E0DB0` (`_PnpDispatchDeviceInterface`; read)
- `0x008E24F2` → RVA `0x00B0D8D0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x008E2565` → RVA `0x00AFCD40` (` ?? ::NNGAKEGL::`string'`; read)
- `0x008E2577` → RVA `0x00AFD430` (` ?? ::NNGAKEGL::`string'`; read)
- `0x008E2639` → RVA `0x009303A0` (`DrvDbDispatchDriverPackage`; read)
- `0x008E2794` → RVA `0x008EE210` (`PnpRegQueryValueIndirect`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **12**
  - `0x008E227F` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x008E2315` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x008E23AF` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x008E2506` → [RtlStringCchPrintfExW](../../text/42/RtlStringCchPrintfExW_function_0042B390.md) (`PAGE` → `.text`)
  - `0x008E258B` → [RtlStringCchPrintfExW](../../text/42/RtlStringCchPrintfExW_function_0042B390.md) (`PAGE` → `.text`)
  - `0x008E260B` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x008E2737` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x008E27D1` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x008E27DE` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x008E2805` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008E2825` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008E2832` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008E2180  40 55                           push rbp
008E2182  53                              push rbx
008E2183  56                              push rsi
008E2184  57                              push rdi
008E2185  41 54                           push r12
008E2187  41 55                           push r13
008E2189  41 56                           push r14
008E218B  41 57                           push r15
008E218D  48 8D AC 24 98 FE FF FF         lea rbp, [rsp - 0x168]
008E2195  48 81 EC 78 02 00 00            sub rsp, 0x278
008E219C  48 8B 05 9D 85 52 00            mov rax, qword ptr [rip + 0x52859d]
008E21A3  48 33 C4                        xor rax, rsp
008E21A6  48 89 85 50 01 00 00            mov qword ptr [rbp + 0x150], rax
008E21AD  48 8B 85 D0 01 00 00            mov rax, qword ptr [rbp + 0x1d0]
008E21B4  48 8D 1D 95 06 00 00            lea rbx, [rip + 0x695]
008E21BB  4C 8B B5 E0 01 00 00            mov r14, qword ptr [rbp + 0x1e0]
008E21C2  45 33 FF                        xor r15d, r15d
008E21C5  4C 8B E9                        mov r13, rcx
008E21C8  48 89 45 F8                     mov qword ptr [rbp - 8], rax
008E21CC  8B 85 F0 01 00 00               mov eax, dword ptr [rbp + 0x1f0]
008E21D2  48 8B F2                        mov rsi, rdx
008E21D5  48 8B 8D D8 01 00 00            mov rcx, qword ptr [rbp + 0x1d8]
008E21DC  49 63 F8                        movsxd rdi, r8d
008E21DF  4D 8B A5 E8 01 00 00            mov r12, qword ptr [r13 + 0x1e8]
008E21E6  4C 8B 85 F8 01 00 00            mov r8, qword ptr [rbp + 0x1f8]
008E21ED  48 89 55 D8                     mov qword ptr [rbp - 0x28], rdx
008E21F1  48 8B 95 E8 01 00 00            mov rdx, qword ptr [rbp + 0x1e8]
008E21F8  89 45 18                        mov dword ptr [rbp + 0x18], eax
008E21FB  8B 85 00 02 00 00               mov eax, dword ptr [rbp + 0x200]
008E2201  89 7D A0                        mov dword ptr [rbp - 0x60], edi
008E2204  4C 89 75 88                     mov qword ptr [rbp - 0x78], r14
008E2208  4C 89 7D E0                     mov qword ptr [rbp - 0x20], r15
008E220C  4C 89 7D E8                     mov qword ptr [rbp - 0x18], r15
008E2210  44 89 7D 1C                     mov dword ptr [rbp + 0x1c], r15d
008E2214  44 89 7D 2C                     mov dword ptr [rbp + 0x2c], r15d
008E2218  4C 89 4D F0                     mov qword ptr [rbp - 0x10], r9
008E221C  48 89 4D 00                     mov qword ptr [rbp], rcx
008E2220  4C 89 75 08                     mov qword ptr [rbp + 8], r14
008E2224  48 89 55 10                     mov qword ptr [rbp + 0x10], rdx
008E2228  4C 89 45 20                     mov qword ptr [rbp + 0x20], r8
008E222C  89 45 28                        mov dword ptr [rbp + 0x28], eax
008E222F  4D 85 E4                        test r12, r12
008E2232  74 75                           je 0x1408e22a9
008E2234  48 8D 45 E0                     lea rax, [rbp - 0x20]
008E2238  44 8B C7                        mov r8d, edi
008E223B  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008E2240  45 8D 4F 08                     lea r9d, [r15 + 8]
008E2244  C7 44 24 20 01 00 00 00         mov dword ptr [rsp + 0x20], 1
008E224C  48 8B D6                        mov rdx, rsi
008E224F  49 8B CD                        mov rcx, r13
008E2252  4C 3B E3                        cmp r12, rbx
008E2255  0F 85 80 05 00 00               jne 0x1408e27db
008E225B  E8 F0 05 00 00                  call 0x1408e2850
008E2260  3D 02 00 00 C0                  cmp eax, 0xc0000002
008E2265  0F 84 17 04 00 00               je 0x1408e2682
008E226B  3D 20 01 00 C0                  cmp eax, 0xc0000120
008E2270  75 27                           jne 0x1408e2299
008E2272  8B 45 E0                        mov eax, dword ptr [rbp - 0x20]
008E2275  48 8B 8D 50 01 00 00            mov rcx, qword ptr [rbp + 0x150]
008E227C  48 33 CC                        xor rcx, rsp
008E227F  E8 BC A3 DC FF                  call 0x1406ac640
008E2284  48 81 C4 78 02 00 00            add rsp, 0x278
008E228B  41 5F                           pop r15
008E228D  41 5E                           pop r14
008E228F  41 5D                           pop r13
008E2291  41 5C                           pop r12
008E2293  5F                              pop rdi
008E2294  5E                              pop rsi
008E2295  5B                              pop rbx
008E2296  5D                              pop rbp
008E2297  C3                              ret
008E2298  CC                              int3
008E2299  85 C0                           test eax, eax
008E229B  0F 85 6A 01 00 00               jne 0x1408e240b
008E22A1  4C 8B 75 08                     mov r14, qword ptr [rbp + 8]
008E22A5  4C 89 75 88                     mov qword ptr [rbp - 0x78], r14
008E22A9  48 8B 4D 00                     mov rcx, qword ptr [rbp]
008E22AD  8B 45 28                        mov eax, dword ptr [rbp + 0x28]
008E22B0  4C 8B 4D 20                     mov r9, qword ptr [rbp + 0x20]
008E22B4  48 8B 55 10                     mov rdx, qword ptr [rbp + 0x10]
008E22B8  44 8B 45 18                     mov r8d, dword ptr [rbp + 0x18]
008E22BC  48 89 4D C8                     mov qword ptr [rbp - 0x38], rcx
008E22C0  48 8B 4D F8                     mov rcx, qword ptr [rbp - 8]
008E22C4  89 45 84                        mov dword ptr [rbp - 0x7c], eax
008E22C7  48 89 4D C0                     mov qword ptr [rbp - 0x40], rcx
008E22CB  48 8B 4D F0                     mov rcx, qword ptr [rbp - 0x10]
008E22CF  0F B7 C0                        movzx eax, ax
008E22D2  48 89 4D B8                     mov qword ptr [rbp - 0x48], rcx
008E22D6  4C 89 4D 90                     mov qword ptr [rbp - 0x70], r9
008E22DA  44 89 45 9C                     mov dword ptr [rbp - 0x64], r8d
008E22DE  48 89 55 B0                     mov qword ptr [rbp - 0x50], rdx
008E22E2  4C 89 7D D0                     mov qword ptr [rbp - 0x30], r15
008E22E6  85 C0                           test eax, eax
008E22E8  0F 85 62 04 00 00               jne 0x1408e2750
008E22EE  48 85 D2                        test rdx, rdx
008E22F1  0F 84 37 03 00 00               je 0x1408e262e
008E22F7  45 85 C0                        test r8d, r8d
008E22FA  41 8B D8                        mov ebx, r8d
008E22FD  49 0F 44 D7                     cmove rdx, r15
008E2301  48 89 55 B0                     mov qword ptr [rbp - 0x50], rdx
008E2305  33 D2                           xor edx, edx
008E2307  45 89 3E                        mov dword ptr [r14], r15d
008E230A  48 8D 4D 30                     lea rcx, [rbp + 0x30]
008E230E  45 89 39                        mov dword ptr [r9], r15d
008E2311  44 8D 42 40                     lea r8d, [rdx + 0x40]
008E2315  E8 26 49 DE FF                  call 0x1406c6c40
008E231A  8D 47 FF                        lea eax, [rdi - 1]
008E231D  83 F8 0A                        cmp eax, 0xa
008E2320  0F 87 52 03 00 00               ja 0x1408e2678
008E2326  49 8B 84 FD 28 01 00 00         mov rax, qword ptr [r13 + rdi*8 + 0x128]
008E232E  48 85 C0                        test rax, rax
008E2331  0F 84 B1 04 00 00               je 0x1408e27e8
008E2337  48 8B 4D B8                     mov rcx, qword ptr [rbp - 0x48]
008E233B  41 B9 08 00 00 00               mov r9d, 8
008E2341  4C 8B 45 C0                     mov r8, qword ptr [rbp - 0x40]
008E2345  48 8B D6                        mov rdx, rsi
008E2348  48 89 4D 30                     mov qword ptr [rbp + 0x30], rcx
008E234C  48 8B 4D C8                     mov rcx, qword ptr [rbp - 0x38]
008E2350  48 89 4D 40                     mov qword ptr [rbp + 0x40], rcx
008E2354  48 8B 4D B0                     mov rcx, qword ptr [rbp - 0x50]
008E2358  48 89 4D 50                     mov qword ptr [rbp + 0x50], rcx
008E235C  8B 4D 84                        mov ecx, dword ptr [rbp - 0x7c]
008E235F  89 4D 68                        mov dword ptr [rbp + 0x68], ecx
008E2362  48 8D 0D F7 F9 FF FF            lea rcx, [rip - 0x609]
008E2369  89 5D 58                        mov dword ptr [rbp + 0x58], ebx
008E236C  48 8B 5D 90                     mov rbx, qword ptr [rbp - 0x70]
008E2370  4C 89 45 38                     mov qword ptr [rbp + 0x38], r8
008E2374  44 8B C7                        mov r8d, edi
008E2377  4C 89 75 48                     mov qword ptr [rbp + 0x48], r14
008E237B  48 89 5D 60                     mov qword ptr [rbp + 0x60], rbx
008E237F  48 3B C1                        cmp rax, rcx
008E2382  0F 85 94 00 00 00               jne 0x1408e241c
008E2388  48 8D 45 30                     lea rax, [rbp + 0x30]
008E238C  49 8B CD                        mov rcx, r13
008E238F  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008E2394  E8 C7 F9 FF FF                  call 0x1408e1d60
008E2399  8B F0                           mov esi, eax
008E239B  3D 16 00 00 C0                  cmp eax, 0xc0000016
008E23A0  0F 84 9C 00 00 00               je 0x1408e2442
008E23A6  48 8B 4D D0                     mov rcx, qword ptr [rbp - 0x30]
008E23AA  48 85 C9                        test rcx, rcx
008E23AD  74 05                           je 0x1408e23b4
008E23AF  E8 FC AE DC FF                  call 0x1406ad2b0
008E23B4  8B 7D A0                        mov edi, dword ptr [rbp - 0x60]
008E23B7  48 8D 1D 92 04 00 00            lea rbx, [rip + 0x492]
008E23BE  4D 85 E4                        test r12, r12
008E23C1  74 52                           je 0x1408e2415
008E23C3  48 8B 55 D8                     mov rdx, qword ptr [rbp - 0x28]
008E23C7  48 8D 45 E0                     lea rax, [rbp - 0x20]
008E23CB  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008E23D0  41 B9 08 00 00 00               mov r9d, 8
008E23D6  C7 44 24 20 02 00 00 00         mov dword ptr [rsp + 0x20], 2
008E23DE  44 8B C7                        mov r8d, edi
008E23E1  89 75 E0                        mov dword ptr [rbp - 0x20], esi
008E23E4  49 8B CD                        mov rcx, r13
008E23E7  4C 3B E3                        cmp r12, rbx
008E23EA  0F 85 3F 04 00 00               jne 0x1408e282f
008E23F0  E8 5B 04 00 00                  call 0x1408e2850
008E23F5  3D 02 00 00 C0                  cmp eax, 0xc0000002
008E23FA  74 19                           je 0x1408e2415
008E23FC  3D 20 01 00 C0                  cmp eax, 0xc0000120
008E2401  0F 84 6B FE FF FF               je 0x1408e2272
008E2407  85 C0                           test eax, eax
008E2409  74 0A                           je 0x1408e2415
008E240B  B8 E5 00 00 C0                  mov eax, 0xc00000e5
008E2410  E9 60 FE FF FF                  jmp 0x1408e2275
008E2415  8B C6                           mov eax, esi
008E2417  E9 59 FE FF FF                  jmp 0x1408e2275
008E241C  48 8D 0D 8D E9 FF FF            lea rcx, [rip - 0x1673]
008E2423  48 3B C1                        cmp rax, rcx
008E2426  0F 85 0D 02 00 00               jne 0x1408e2639
008E242C  48 8D 45 30                     lea rax, [rbp + 0x30]
008E2430  49 8B CD                        mov rcx, r13
008E2433  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008E2438  E8 73 E9 FF FF                  call 0x1408e0db0
008E243D  E9 57 FF FF FF                  jmp 0x1408e2399
008E2442  4C 39 7D B8                     cmp qword ptr [rbp - 0x48], r15
008E2446  0F 84 0E 03 00 00               je 0x1408e275a
008E244C  48 8B 45 C0                     mov rax, qword ptr [rbp - 0x40]
008E2450  45 89 3E                        mov dword ptr [r14], r15d
008E2453  4C 89 7D A8                     mov qword ptr [rbp - 0x58], r15
008E2457  44 89 7D 84                     mov dword ptr [rbp - 0x7c], r15d
008E245B  44 89 7D 98                     mov dword ptr [rbp - 0x68], r15d
008E245F  44 88 7D 80                     mov byte ptr [rbp - 0x80], r15b
008E2463  44 89 3B                        mov dword ptr [rbx], r15d
008E2466  48 85 C0                        test rax, rax
008E2469  0F 85 F0 01 00 00               jne 0x1408e265f
008E246F  48 8B 45 C8                     mov rax, qword ptr [rbp - 0x38]
008E2473  0F B6 48 0F                     movzx ecx, byte ptr [rax + 0xf]
008E2477  0F B6 50 0E                     movzx edx, byte ptr [rax + 0xe]
008E247B  44 0F B6 40 0D                  movzx r8d, byte ptr [rax + 0xd]
008E2480  44 0F B6 48 0C                  movzx r9d, byte ptr [rax + 0xc]
008E2485  44 0F B6 50 0B                  movzx r10d, byte ptr [rax + 0xb]
008E248A  44 0F B6 58 0A                  movzx r11d, byte ptr [rax + 0xa]
008E248F  0F B6 58 09                     movzx ebx, byte ptr [rax + 9]
008E2493  0F B6 78 08                     movzx edi, byte ptr [rax + 8]
008E2497  0F B7 70 06                     movzx esi, word ptr [rax + 6]
008E249B  44 0F B7 70 04                  movzx r14d, word ptr [rax + 4]
008E24A0  8B 40 10                        mov eax, dword ptr [rax + 0x10]
008E24A3  89 84 24 88 00 00 00            mov dword ptr [rsp + 0x88], eax
008E24AA  89 8C 24 80 00 00 00            mov dword ptr [rsp + 0x80], ecx
008E24B1  48 8B 4D C8                     mov rcx, qword ptr [rbp - 0x38]
008E24B5  89 54 24 78                     mov dword ptr [rsp + 0x78], edx
008E24B9  44 89 44 24 70                  mov dword ptr [rsp + 0x70], r8d
008E24BE  45 33 C0                        xor r8d, r8d
008E24C1  44 89 4C 24 68                  mov dword ptr [rsp + 0x68], r9d
008E24C6  45 33 C9                        xor r9d, r9d
008E24C9  8B 01                           mov eax, dword ptr [rcx]
008E24CB  48 8D 4D 70                     lea rcx, [rbp + 0x70]
008E24CF  44 89 54 24 60                  mov dword ptr [rsp + 0x60], r10d
008E24D4  44 89 5C 24 58                  mov dword ptr [rsp + 0x58], r11d
008E24D9  89 5C 24 50                     mov dword ptr [rsp + 0x50], ebx
008E24DD  41 8D 51 30                     lea edx, [r9 + 0x30]
008E24E1  89 7C 24 48                     mov dword ptr [rsp + 0x48], edi
008E24E5  89 74 24 40                     mov dword ptr [rsp + 0x40], esi
008E24E9  44 89 74 24 38                  mov dword ptr [rsp + 0x38], r14d
008E24EE  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
008E24F2  48 8D 05 D7 B3 22 00            lea rax, [rip + 0x22b3d7]
008E24F9  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008E24FE  C7 44 24 20 00 08 00 00         mov dword ptr [rsp + 0x20], 0x800
008E2506  E8 85 8E B4 FF                  call 0x14042b390
008E250B  8B F0                           mov esi, eax
008E250D  85 C0                           test eax, eax
008E250F  0F 88 E5 00 00 00               js 0x1408e25fa
008E2515  BF 00 02 00 00                  mov edi, 0x200
008E251A  4C 89 7D A8                     mov qword ptr [rbp - 0x58], r15
008E251E  8B CF                           mov ecx, edi
008E2520  48 8D 45 70                     lea rax, [rbp + 0x70]
008E2524  66 44 39 38                     cmp word ptr [rax], r15w
008E2528  74 14                           je 0x1408e253e
008E252A  48 83 C0 02                     add rax, 2
008E252E  48 83 E9 01                     sub rcx, 1
008E2532  75 F0                           jne 0x1408e2524
008E2534  BE 0D 00 00 C0                  mov esi, 0xc000000d
008E2539  E9 BC 00 00 00                  jmp 0x1408e25fa
008E253E  48 2B F9                        sub rdi, rcx
008E2541  48 83 FF 30                     cmp rdi, 0x30
008E2545  0F 83 A7 02 00 00               jae 0x1408e27f2
008E254B  48 8D 9D D0 00 00 00            lea rbx, [rbp + 0xd0]
008E2552  BF 3B 00 00 00                  mov edi, 0x3b
008E2557  48 8D 45 70                     lea rax, [rbp + 0x70]
008E255B  8B D7                           mov edx, edi
008E255D  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
008E2562  45 33 C9                        xor r9d, r9d
008E2565  48 8D 05 D4 A7 21 00            lea rax, [rip + 0x21a7d4]
008E256C  45 33 C0                        xor r8d, r8d
008E256F  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
008E2574  48 8B CB                        mov rcx, rbx
008E2577  48 8D 05 B2 AE 21 00            lea rax, [rip + 0x21aeb2]
008E257E  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008E2583  C7 44 24 20 00 08 00 00         mov dword ptr [rsp + 0x20], 0x800
008E258B  E8 00 8E B4 FF                  call 0x14042b390
008E2590  8B F8                           mov edi, eax
008E2592  BE 34 00 00 C0                  mov esi, 0xc0000034
008E2597  85 C0                           test eax, eax
008E2599  78 3D                           js 0x1408e25d8
008E259B  49 8B 85 E0 00 00 00            mov rax, qword ptr [r13 + 0xe0]
008E25A2  48 85 C0                        test rax, rax
008E25A5  74 04                           je 0x1408e25ab
008E25A7  4C 8B 78 08                     mov r15, qword ptr [rax + 8]
008E25AB  48 8B 4D B8                     mov rcx, qword ptr [rbp - 0x48]
008E25AF  48 8D 45 A8                     lea rax, [rbp - 0x58]
008E25B3  4C 89 7C 24 28                  mov qword ptr [rsp + 0x28], r15
008E25B8  41 B9 01 00 00 00               mov r9d, 1
008E25BE  45 33 C0                        xor r8d, r8d
008E25C1  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008E25C6  48 8B D3                        mov rdx, rbx
008E25C9  E8 42 D2 00 00                  call 0x1408ef810
008E25CE  3D 7C 01 00 C0                  cmp eax, 0xc000017c
008E25D3  8B F8                           mov edi, eax
008E25D5  0F 44 FE                        cmove edi, esi
008E25D8  48 85 DB                        test rbx, rbx
008E25DB  74 10                           je 0x1408e25ed
008E25DD  48 8D 85 D0 00 00 00            lea rax, [rbp + 0xd0]
008E25E4  48 3B D8                        cmp rbx, rax
008E25E7  0F 85 33 02 00 00               jne 0x1408e2820
008E25ED  3B FE                           cmp edi, esi
008E25EF  0F 85 95 00 00 00               jne 0x1408e268a
008E25F5  BE 25 02 00 C0                  mov esi, 0xc0000225
008E25FA  48 8B 5D 88                     mov rbx, qword ptr [rbp - 0x78]
008E25FE  4C 8B 7D 90                     mov r15, qword ptr [rbp - 0x70]
008E2602  48 8B 4D A8                     mov rcx, qword ptr [rbp - 0x58]
008E2606  48 85 C9                        test rcx, rcx
008E2609  74 05                           je 0x1408e2610
008E260B  E8 A0 AC DC FF                  call 0x1406ad2b0
008E2610  85 F6                           test esi, esi
008E2612  0F 88 8E FD FF FF               js 0x1408e23a6
008E2618  44 8B 03                        mov r8d, dword ptr [rbx]
008E261B  41 8B 17                        mov edx, dword ptr [r15]
008E261E  48 8B 4D B0                     mov rcx, qword ptr [rbp - 0x50]
008E2622  E8 31 50 01 00                  call 0x1408f7658
008E2627  8B F0                           mov esi, eax
008E2629  E9 78 FD FF FF                  jmp 0x1408e23a6
008E262E  41 8B DF                        mov ebx, r15d
008E2631  89 5D 9C                        mov dword ptr [rbp - 0x64], ebx
008E2634  E9 CC FC FF FF                  jmp 0x1408e2305
008E2639  48 8D 0D 60 DD 04 00            lea rcx, [rip + 0x4dd60]
008E2640  48 3B C1                        cmp rax, rcx
008E2643  0F 85 E2 00 00 00               jne 0x1408e272b
008E2649  48 8D 45 30                     lea rax, [rbp + 0x30]
008E264D  49 8B CD                        mov rcx, r13
008E2650  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008E2655  E8 46 DD 04 00                  call 0x1409303a0
008E265A  E9 3A FD FF FF                  jmp 0x1408e2399
008E265F  B9 55 00 00 00                  mov ecx, 0x55
008E2664  66 44 39 38                     cmp word ptr [rax], r15w
008E2668  0F 84 01 FE FF FF               je 0x1408e246f
008E266E  48 83 C0 02                     add rax, 2
008E2672  48 83 E9 01                     sub rcx, 1
008E2676  75 EC                           jne 0x1408e2664
008E2678  BE 0D 00 00 C0                  mov esi, 0xc000000d
008E267D  E9 24 FD FF FF                  jmp 0x1408e23a6
008E2682  4D 8B E7                        mov r12, r15
008E2685  E9 17 FC FF FF                  jmp 0x1408e22a1
008E268A  8B F7                           mov esi, edi
008E268C  85 FF                           test edi, edi
008E268E  0F 88 66 FF FF FF               js 0x1408e25fa
008E2694  4D 8B 95 08 02 00 00            mov r10, qword ptr [r13 + 0x208]
008E269B  44 8B 75 9C                     mov r14d, dword ptr [rbp - 0x64]
008E269F  44 89 75 98                     mov dword ptr [rbp - 0x68], r14d
008E26A3  4D 85 D2                        test r10, r10
008E26A6  0F 85 E8 00 00 00               jne 0x1408e2794
008E26AC  4C 8B 45 C0                     mov r8, qword ptr [rbp - 0x40]
008E26B0  48 8D 45 80                     lea rax, [rbp - 0x80]
008E26B4  48 8B 55 A8                     mov rdx, qword ptr [rbp - 0x58]
008E26B8  4C 8D 4D 84                     lea r9, [rbp - 0x7c]
008E26BC  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
008E26C1  49 8B CD                        mov rcx, r13
008E26C4  48 8D 45 98                     lea rax, [rbp - 0x68]
008E26C8  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008E26CD  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
008E26D1  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008E26D6  E8 35 BB 00 00                  call 0x1408ee210
008E26DB  8B C8                           mov ecx, eax
008E26DD  3D 34 00 00 C0                  cmp eax, 0xc0000034
008E26E2  0F 84 0D FF FF FF               je 0x1408e25f5
008E26E8  3D 7C 01 00 C0                  cmp eax, 0xc000017c
008E26ED  0F 84 02 FF FF FF               je 0x1408e25f5
008E26F3  85 C0                           test eax, eax
008E26F5  75 4A                           jne 0x1408e2741
008E26F7  0F B7 45 84                     movzx eax, word ptr [rbp - 0x7c]
008E26FB  48 8B 5D 88                     mov rbx, qword ptr [rbp - 0x78]
008E26FF  89 03                           mov dword ptr [rbx], eax
008E2701  83 F8 01                        cmp eax, 1
008E2704  0F 84 F4 FE FF FF               je 0x1408e25fe
008E270A  4C 8B 7D 90                     mov r15, qword ptr [rbp - 0x70]
008E270E  8B 45 98                        mov eax, dword ptr [rbp - 0x68]
008E2711  41 89 07                        mov dword ptr [r15], eax
008E2714  85 C9                           test ecx, ecx
008E2716  75 09                           jne 0x1408e2721
008E2718  45 85 F6                        test r14d, r14d
008E271B  0F 85 E1 FE FF FF               jne 0x1408e2602
008E2721  BE 23 00 00 C0                  mov esi, 0xc0000023
008E2726  E9 D7 FE FF FF                  jmp 0x1408e2602
008E272B  48 8D 4D 30                     lea rcx, [rbp + 0x30]
008E272F  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
008E2734  49 8B CD                        mov rcx, r13
008E2737  E8 94 83 DD FF                  call 0x1406baad0
008E273C  E9 58 FC FF FF                  jmp 0x1408e2399
008E2741  81 F9 23 00 00 C0               cmp ecx, 0xc0000023
008E2747  74 AE                           je 0x1408e26f7
008E2749  8B F1                           mov esi, ecx
008E274B  E9 AA FE FF FF                  jmp 0x1408e25fa
008E2750  BE 0D 00 00 C0                  mov esi, 0xc000000d
008E2755  E9 64 FC FF FF                  jmp 0x1408e23be
008E275A  48 8B 55 D8                     mov rdx, qword ptr [rbp - 0x28]
008E275E  48 8D 45 D0                     lea rax, [rbp - 0x30]
008E2762  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008E2767  41 B9 01 00 00 02               mov r9d, 0x2000001
008E276D  44 8B C7                        mov r8d, edi
008E2770  44 88 7C 24 20                  mov byte ptr [rsp + 0x20], r15b
008E2775  49 8B CD                        mov rcx, r13
008E2778  E8 6B EE FF FF                  call 0x1408e15e8
008E277D  8B F0                           mov esi, eax
008E277F  85 C0                           test eax, eax
008E2781  0F 88 1F FC FF FF               js 0x1408e23a6
008E2787  48 8B 45 D0                     mov rax, qword ptr [rbp - 0x30]
008E278B  48 89 45 B8                     mov qword ptr [rbp - 0x48], rax
008E278F  E9 B8 FC FF FF                  jmp 0x1408e244c
008E2794  48 8D 05 75 BA 00 00            lea rax, [rip + 0xba75]
008E279B  4C 3B D0                        cmp r10, rax
008E279E  0F 84 08 FF FF FF               je 0x1408e26ac
008E27A4  4C 8B 45 C0                     mov r8, qword ptr [rbp - 0x40]
008E27A8  48 8D 45 80                     lea rax, [rbp - 0x80]
008E27AC  48 8B 55 A8                     mov rdx, qword ptr [rbp - 0x58]
008E27B0  4C 8D 4D 84                     lea r9, [rbp - 0x7c]
008E27B4  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
008E27B9  49 8B CD                        mov rcx, r13
008E27BC  48 8D 45 98                     lea rax, [rbp - 0x68]
008E27C0  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008E27C5  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
008E27C9  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008E27CE  49 8B C2                        mov rax, r10
008E27D1  E8 FA 82 DD FF                  call 0x1406baad0
008E27D6  E9 00 FF FF FF                  jmp 0x1408e26db
008E27DB  49 8B C4                        mov rax, r12
008E27DE  E8 ED 82 DD FF                  call 0x1406baad0
008E27E3  E9 78 FA FF FF                  jmp 0x1408e2260
008E27E8  BE 02 00 00 C0                  mov esi, 0xc0000002
008E27ED  E9 B4 FB FF FF                  jmp 0x1408e23a6
008E27F2  83 C7 0C                        add edi, 0xc
008E27F5  B9 00 01 00 00                  mov ecx, 0x100
008E27FA  8B D7                           mov edx, edi
008E27FC  41 B8 50 4E 50 52               mov r8d, 0x52504e50
008E2802  48 03 D2                        add rdx, rdx
008E2805  E8 E6 F8 29 00                  call 0x140b820f0
008E280A  48 8B D8                        mov rbx, rax
008E280D  48 85 C0                        test rax, rax
008E2810  0F 85 41 FD FF FF               jne 0x1408e2557
008E2816  BE 17 00 00 C0                  mov esi, 0xc0000017
008E281B  E9 DA FD FF FF                  jmp 0x1408e25fa
008E2820  33 D2                           xor edx, edx
008E2822  48 8B CB                        mov rcx, rbx
008E2825  E8 46 00 2A 00                  call 0x140b82870
008E282A  E9 BE FD FF FF                  jmp 0x1408e25ed
008E282F  49 8B C4                        mov rax, r12
008E2832  E8 99 82 DD FF                  call 0x1406baad0
008E2837  E9 B9 FB FF FF                  jmp 0x1408e23f5
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PnpGetObjectProperty(__int64 a1, __int64 a2, int a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, unsigned int a9, __int64 a10, unsigned int a11)
{
    __int64 result;
    __int64 v_r15;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m138;
    unsigned int v_stack_m140;
    unsigned __int64 v_stack_m148;
    unsigned int v_stack_m150;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m160;
    unsigned __int64 v_stack_m168;
    unsigned __int64 v_stack_m170;
    unsigned __int64 v_stack_m178;
    unsigned int v_stack_m17C;
    unsigned int v_stack_m180;
    unsigned __int64 v_stack_m188;
    unsigned int v_stack_m18C;
    unsigned int v_stack_m190;
    unsigned __int64 v_stack_m198;
    unsigned __int64 v_stack_m1A0;
    unsigned __int64 v_stack_m1A8;
    unsigned __int64 v_stack_m1B0;
    unsigned __int64 v_stack_m1B8;
    unsigned __int64 v_stack_m1C0;
    unsigned __int64 v_stack_m1C8;
    unsigned __int64 v_stack_m1D0;
    unsigned __int64 v_stack_m1D8;
    unsigned __int64 v_stack_m1E0;
    unsigned __int64 v_stack_m1E8;
    unsigned __int64 v_stack_m1F0;
    unsigned __int64 v_stack_m1F8;
    unsigned __int64 v_stack_m200;
    unsigned int v_stack_m208;
    unsigned int v_stack_m20C;
    unsigned int v_stack_m210;
    unsigned __int64 v_stack_m218;
    unsigned __int64 v_stack_m220;
    unsigned int v_stack_m224;
    unsigned __int8 v_stack_m228;
    unsigned __int64 v_stack_m290;
    unsigned int v_stack_m298;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned int v_stack_p30;
    unsigned int v_stack_p38;
    unsigned int v_stack_p40;
    unsigned int v_stack_p48;
    unsigned int v_stack_p50;
    unsigned int v_stack_p58;
    unsigned int v_stack_p60;
    unsigned int v_stack_p68;
    unsigned int v_stack_p70;
    unsigned int v_stack_p78;
    unsigned int v_stack_p80;
    unsigned int v_stack_p88;

    v_rsp = (v_rsp) - (632);
    result = (*(unsigned __int64 *)(v_rip + 5408157)) ^ (v_rsp);
    v_stack_m58 = result;
    v_r15 = 0;
    v_stack_m1B0 = a5;
    v_stack_m1D0 = a2;
    v_stack_m190 = (unsigned int)((unsigned int)(a9));
    v_stack_m208 = (unsigned int)((int)(a3));
    v_stack_m220 = a7;
    v_stack_m1C8 = 0;
    v_stack_m1C0 = 0;
    v_stack_m18C = 0;
    v_stack_m17C = 0;
    v_stack_m1B8 = a4;
    v_stack_m1A8 = a6;
    v_stack_m1A0 = a7;
    v_stack_m198 = a8;
    v_stack_m188 = a10;
    v_stack_m180 = (unsigned int)((unsigned int)(a11));
    if (*(unsigned __int64 *)(a1 + 488) == 0) goto loc_008E22A9;
    v_stack_m290 = v_stack_m1C8;
    v_stack_m298 = 1;
    if ((*(unsigned __int64 *)(a1 + 488)) != (v_rip + 1685)) goto loc_008E27DB;
    result = PiPnpRtlObjectActionCallback(a1, a2, (unsigned int)((unsigned int)((int)(a3))), v_r15 + 8);
loc_008E2260:
    if (((unsigned int)(result)) == 0xC0000002ULL) goto loc_008E2682;
    if (((unsigned int)(result)) != 0xC0000120ULL) goto loc_008E2299;
loc_008E2272:
loc_008E2275:
    a1 = (v_stack_m58) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, (unsigned int)((unsigned int)((int)(a3))), v_r15 + 8);
    v_rsp = (v_rsp) + (632);
    return result;
loc_008E2299:
    if ((unsigned int)(result) != 0) goto loc_008E240B;
loc_008E22A1:
    v_stack_m220 = v_stack_m1A0;
loc_008E22A9:
    v_stack_m1E0 = v_stack_m1A8;
    v_stack_m224 = (unsigned int)((unsigned int)(v_stack_m180));
    v_stack_m1E8 = v_stack_m1B0;
    v_stack_m1F0 = v_stack_m1B8;
    v_stack_m218 = v_stack_m188;
    v_stack_m20C = (unsigned int)((unsigned int)(v_stack_m190));
    v_stack_m1F8 = v_stack_m198;
    v_stack_m1D8 = 0;
    if ((unsigned int)((unsigned __int16)((unsigned int)(v_stack_m180))) != 0) goto loc_008E2750;
    if (v_stack_m198 == 0) goto loc_008E262E;
    a2 = v_stack_m198;
    if ((unsigned int)((unsigned int)(v_stack_m190)) == 0) { a2 = 0; }
    v_stack_m1F8 = a2;
loc_008E2305:
    a2 = 0;
    *(unsigned int *)(v_stack_m1A0) = 0;
    *(unsigned int *)(v_stack_m188) = 0;
    result = memset(v_stack_m178, a2, a2 + 64, v_stack_m188);
    if (((unsigned int)((int)(a3) - 1)) > 10) goto loc_008E2678;
    if (*(unsigned __int64 *)(a1 + (int)(a3) * 8 + 296) == 0) goto loc_008E27E8;
    v_stack_m178 = v_stack_m1F0;
    v_stack_m168 = v_stack_m1E0;
    v_stack_m158 = v_stack_m1F8;
    v_stack_m140 = (unsigned int)((unsigned int)(v_stack_m224));
    v_stack_m150 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m190))));
    v_stack_m170 = v_stack_m1E8;
    v_stack_m160 = v_stack_m1A0;
    v_stack_m148 = v_stack_m218;
    if ((*(unsigned __int64 *)(a1 + (int)(a3) * 8 + 296)) != (v_rip - 1545)) goto loc_008E241C;
    v_stack_p20 = v_stack_m178;
    result = _PnpDispatchDevice(a1, 0, (unsigned int)((unsigned int)((int)(a3))), 8);
loc_008E2399:
    if (((unsigned int)(result)) == 0xC0000016ULL) goto loc_008E2442;
loc_008E23A6:
    if (v_stack_m1D8 != 0) {
        result = ZwClose(v_stack_m1D8, 0, (unsigned int)((unsigned int)((int)(a3))), 8);
    }
loc_008E23BE:
    if (*(unsigned __int64 *)(a1 + 488) == 0) goto loc_008E2415;
    v_stack_p28 = v_stack_m1C8;
    v_stack_p20 = 2;
    v_stack_m1C8 = (unsigned int)((unsigned int)((unsigned int)(result)));
    if ((*(unsigned __int64 *)(a1 + 488)) != (v_rip + 1170)) goto loc_008E282F;
    result = PiPnpRtlObjectActionCallback(a1, v_stack_m1D0, (unsigned int)((unsigned int)((unsigned int)(v_stack_m208))), 8);
loc_008E23F5:
    if (((unsigned int)(result)) == 0xC0000002ULL) goto loc_008E2415;
    if (((unsigned int)(result)) == 0xC0000120ULL) goto loc_008E2272;
    if ((unsigned int)(result) == 0) goto loc_008E2415;
loc_008E240B:
    goto loc_008E2275;
loc_008E2415:
    goto loc_008E2275;
loc_008E241C:
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))))) != (v_rip - 5747)) goto loc_008E2639;
    v_stack_p20 = v_stack_m178;
    result = _PnpDispatchDeviceInterface(a1, v_stack_m1D0, (unsigned int)((unsigned int)((unsigned int)(v_stack_m208))), 8);
    goto loc_008E2399;
loc_008E2442:
    if (v_stack_m1F0 == 0) goto loc_008E275A;
loc_008E244C:
    *(unsigned int *)(v_stack_m1A0) = 0;
    v_stack_m200 = 0;
    v_stack_m224 = 0;
    v_stack_m210 = 0;
    v_stack_m228 = 0;
    *(unsigned int *)(v_rip + 1170) = 0;
    if (v_stack_m1E8 != 0) goto loc_008E265F;
loc_008E246F:
    v_stack_p88 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m1E0 + 16)));
    v_stack_p80 = (unsigned int)(*(unsigned __int8 *)(v_stack_m1E0 + 15));
    v_stack_p78 = (unsigned int)(*(unsigned __int8 *)(v_stack_m1E0 + 14));
    v_stack_p70 = (unsigned int)(*(unsigned __int8 *)(v_stack_m1E0 + 13));
    a3 = 0;
    v_stack_p68 = (unsigned int)(*(unsigned __int8 *)(v_stack_m1E0 + 12));
    a4 = 0;
    v_stack_p60 = (unsigned int)(*(unsigned __int8 *)(v_stack_m1E0 + 11));
    v_stack_p58 = (unsigned int)(*(unsigned __int8 *)(v_stack_m1E0 + 10));
    v_stack_p50 = (unsigned int)(*(unsigned __int8 *)(v_stack_m1E0 + 9));
    v_stack_p48 = (unsigned int)(*(unsigned __int8 *)(v_stack_m1E0 + 8));
    v_stack_p40 = (unsigned int)(*(unsigned __int16 *)(v_stack_m1E0 + 6));
    v_stack_p38 = (unsigned int)(*(unsigned __int16 *)(v_stack_m1E0 + 4));
    v_stack_p30 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m1E0)));
    v_stack_p28 = v_rip + 2274263;
    v_stack_p20 = 0x800ULL;
    result = RtlStringCchPrintfExW(v_stack_m138, a4 + 48, a3, a4);
    if (sign_flag) goto loc_008E25FA;
    v_stack_m200 = 0;
loc_008E2524:
    if ((*(unsigned __int16 *)(v_stack_m138)) == 0) goto loc_008E253E;
    result = (v_stack_m138) + (2);
    a1 = (512) - (1);
    if (condition_is_not_equal) goto loc_008E2524;
    goto loc_008E25FA;
loc_008E253E:
    v_rdi = (512) - (a1);
    if (v_rdi >= 48) goto loc_008E27F2;
loc_008E2557:
    v_stack_p38 = v_stack_m138;
    a4 = 0;
    a3 = 0;
    v_stack_p30 = v_rip + 2205652;
    v_stack_p28 = v_rip + 2207410;
    v_stack_p20 = 0x800ULL;
    result = RtlStringCchPrintfExW(v_stack_mD8, 59, a3, a4);
    if (sign_flag) goto loc_008E25D8;
    if (*(unsigned __int64 *)(a1 + 224) != 0) {
        v_r15 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 224) + 8);
    }
    v_stack_p28 = v_r15;
    a3 = 0;
    v_stack_p20 = v_stack_m200;
    result = _RegRtlOpenKeyTransacted(v_stack_m1F0, v_stack_mD8, a3, 1);
    v_rdi = (unsigned int)((unsigned int)(result));
    if (((unsigned int)(result)) == 0xC000017CULL) { v_rdi = (unsigned int)((unsigned int)(0xC0000034ULL)); }
loc_008E25D8:
    if (v_stack_mD8 == 0) goto loc_008E25ED;
    if (v_stack_mD8 != v_stack_mD8) goto loc_008E2820;
loc_008E25ED:
    if (((unsigned int)(v_rdi)) != ((unsigned int)((unsigned int)(0xC0000034ULL)))) goto loc_008E268A;
loc_008E25F5:
loc_008E25FA:
loc_008E25FE:
loc_008E2602:
    result = v_stack_mD8;
    if (v_stack_m200 != 0) {
        result = ZwClose(v_stack_m200, v_stack_mD8, a3, 1);
    }
    if (sign_flag) goto loc_008E23A6;
    result = PnpValidatePropertyData(v_stack_m1F8, (unsigned int)(*(unsigned int *)(v_stack_m218)), (unsigned int)(*(unsigned int *)(v_stack_m220)), 1);
    goto loc_008E23A6;
loc_008E262E:
    v_stack_m20C = (unsigned int)((unsigned int)((unsigned int)(v_stack_m218)));
    goto loc_008E2305;
loc_008E2639:
    if (result != (v_rip + 318816)) goto loc_008E272B;
    v_stack_p20 = v_stack_m178;
    result = DrvDbDispatchDriverPackage(a1, (unsigned int)(*(unsigned int *)(v_stack_m218)), (unsigned int)(*(unsigned int *)(v_stack_m220)), 1);
    goto loc_008E2399;
loc_008E265F:
loc_008E2664:
    if ((*(unsigned __int16 *)(result)) == ((unsigned __int16)(v_stack_m218))) goto loc_008E246F;
    result = (result) + (2);
    a1 = (85) - (1);
    if (condition_is_not_equal) goto loc_008E2664;
loc_008E2678:
    goto loc_008E23A6;
loc_008E2682:
    goto loc_008E22A1;
loc_008E268A:
    if (sign_flag) goto loc_008E25FA;
    v_stack_m210 = (unsigned int)((unsigned int)(v_stack_m20C));
    if (*(unsigned __int64 *)(a1 + 520) != 0) goto loc_008E2794;
loc_008E26AC:
    v_stack_p30 = v_stack_m228;
    v_stack_p28 = v_stack_m210;
    v_stack_p20 = v_stack_m1F8;
    result = PnpRegQueryValueIndirect(a1, v_stack_m200, v_stack_m1E8, v_stack_m224);
loc_008E26DB:
    if (((unsigned int)(result)) == 0xC0000034ULL) goto loc_008E25F5;
    if (((unsigned int)(result)) == 0xC000017CULL) goto loc_008E25F5;
    if ((unsigned int)(result) != 0) goto loc_008E2741;
loc_008E26F7:
    *(unsigned int *)(v_stack_m220) = (unsigned int)(v_stack_m224);
    if (((unsigned int)(v_stack_m224)) == 1) goto loc_008E25FE;
    *(unsigned int *)(v_stack_m218) = (unsigned int)((unsigned int)(v_stack_m210));
    if ((unsigned int)((unsigned int)((unsigned int)(result))) != 0) goto loc_008E2721;
    if ((unsigned int)((unsigned int)(v_stack_m20C)) != 0) goto loc_008E2602;
loc_008E2721:
    goto loc_008E2602;
loc_008E272B:
    v_stack_p20 = v_stack_m178;
    result = guard_dispatch_icall(a1, v_stack_m200, v_stack_m1E8, v_stack_m224);
    goto loc_008E2399;
loc_008E2741:
    if (((unsigned int)(a1)) == 0xC0000023ULL) goto loc_008E26F7;
    goto loc_008E25FA;
loc_008E2750:
    goto loc_008E23BE;
loc_008E275A:
    v_stack_p28 = v_stack_m1D8;
    v_stack_p20 = (unsigned __int8)(v_stack_m218);
    result = PnpOpenObjectRegKey(a1, v_stack_m1D0, (unsigned int)((unsigned int)(v_rdi)), (unsigned int)(0x2000001ULL));
    if (sign_flag) goto loc_008E23A6;
    v_stack_m1F0 = v_stack_m1D8;
    goto loc_008E244C;
loc_008E2794:
    if ((*(unsigned __int64 *)(a1 + 520)) == (v_rip + 47733)) goto loc_008E26AC;
    v_stack_p30 = v_stack_m228;
    v_stack_p28 = v_stack_m210;
    v_stack_p20 = v_stack_m1F8;
    result = guard_dispatch_icall(a1, v_stack_m200, v_stack_m1E8, v_stack_m224);
    goto loc_008E26DB;
loc_008E27DB:
    result = guard_dispatch_icall(a1, v_stack_m200, v_stack_m1E8, v_stack_m224);
    goto loc_008E2260;
loc_008E27E8:
    goto loc_008E23A6;
loc_008E27F2:
    v_rdi = (unsigned int)((v_rdi) + (12));
    a2 = ((unsigned int)((unsigned int)(v_rdi))) + ((unsigned int)((unsigned int)(v_rdi)));
    result = ExAllocatePool2(256, a2, (unsigned int)(0x52504E50ULL), v_stack_m224);
    if (result != 0) goto loc_008E2557;
    goto loc_008E25FA;
loc_008E2820:
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, (unsigned int)(0x52504E50ULL), v_stack_m224);
    goto loc_008E25ED;
loc_008E282F:
    result = guard_dispatch_icall(result, a2, (unsigned int)(0x52504E50ULL), v_stack_m224);
    goto loc_008E23F5;
}
```

## 5. (Beta) C Style

```c
int64_t PnpGetObjectProperty(void *Arg1, int64_t Arg2, void *Arg3, int64_t Arg4, int64_t Arg5, int64_t Arg6, int64_t Arg7, int64_t Arg8, uint32_t Arg9, int64_t Arg10, uint32_t Arg11)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_r15;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m138;
    uint32_t v_stack_m140;
    uint64_t v_stack_m148;
    uint32_t v_stack_m150;
    uint64_t v_stack_m158;
    uint64_t v_stack_m160;
    uint64_t v_stack_m168;
    uint64_t v_stack_m170;
    uint64_t v_stack_m178;
    uint32_t v_stack_m17C;
    uint32_t v_stack_m180;
    uint64_t v_stack_m188;
    uint32_t v_stack_m18C;
    uint32_t v_stack_m190;
    uint64_t v_stack_m198;
    uint64_t v_stack_m1A0;
    uint64_t v_stack_m1A8;
    uint64_t v_stack_m1B0;
    uint64_t v_stack_m1B8;
    uint64_t v_stack_m1C0;
    uint64_t v_stack_m1C8;
    uint64_t v_stack_m1D0;
    uint64_t v_stack_m1D8;
    uint64_t v_stack_m1E0;
    uint64_t v_stack_m1E8;
    uint64_t v_stack_m1F0;
    uint64_t v_stack_m1F8;
    uint64_t v_stack_m200;
    uint32_t v_stack_m208;
    uint32_t v_stack_m20C;
    uint32_t v_stack_m210;
    uint64_t v_stack_m218;
    uint64_t v_stack_m220;
    uint32_t v_stack_m224;
    uint8_t v_stack_m228;
    uint64_t v_stack_m290;
    uint32_t v_stack_m298;
    uint64_t v_stack_m58;
    uint64_t v_stack_mD8;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint32_t v_stack_p30;
    uint32_t v_stack_p38;
    uint32_t v_stack_p40;
    uint32_t v_stack_p48;
    uint32_t v_stack_p50;
    uint32_t v_stack_p58;
    uint32_t v_stack_p60;
    uint32_t v_stack_p68;
    uint32_t v_stack_p70;
    uint32_t v_stack_p78;
    uint32_t v_stack_p80;
    uint32_t v_stack_p88;

    local_rsp = (local_rsp) - (632);
    result = (*(uint64_t *)(v_rip + 0x52859D)) ^ (local_rsp);
    v_stack_m58 = result;
    local_r15 = 0;
    v_stack_m1B0 = Arg5;
    v_stack_m1D0 = Arg2;
    v_stack_m190 = (uint32_t)((uint32_t)(Arg9));
    v_stack_m208 = (uint32_t)((int32_t)(Arg3));
    v_stack_m220 = Arg7;
    v_stack_m1C8 = 0;
    v_stack_m1C0 = 0;
    v_stack_m18C = 0;
    v_stack_m17C = 0;
    v_stack_m1B8 = Arg4;
    v_stack_m1A8 = Arg6;
    v_stack_m1A0 = Arg7;
    v_stack_m198 = Arg8;
    v_stack_m188 = Arg10;
    v_stack_m180 = (uint32_t)((uint32_t)(Arg11));
    if (*(uint64_t *)(arg1 + 0x1E8) == 0) goto loc_008E22A9;
    v_stack_m290 = v_stack_m1C8;
    v_stack_m298 = 1;
    if ((*(uint64_t *)(arg1 + 0x1E8)) != (v_rip + 1685)) goto loc_008E27DB;
    result = PiPnpRtlObjectActionCallback(Arg1, Arg2, (uint32_t)((uint32_t)((int32_t)(Arg3))), local_r15 + 8);
loc_008E2260:
    if (((uint32_t)(result)) == 0xC0000002ULL) goto loc_008E2682;
    if (((uint32_t)(result)) != 0xC0000120ULL) goto loc_008E2299;
loc_008E2272:
loc_008E2275:
    Arg1 = (v_stack_m58) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, (uint32_t)((uint32_t)((int32_t)(Arg3))), local_r15 + 8);
    local_rsp = (local_rsp) + (632);
    return result;
loc_008E2299:
    if ((uint32_t)(result) != 0) goto loc_008E240B;
loc_008E22A1:
    v_stack_m220 = v_stack_m1A0;
loc_008E22A9:
    v_stack_m1E0 = v_stack_m1A8;
    v_stack_m224 = (uint32_t)((uint32_t)(v_stack_m180));
    v_stack_m1E8 = v_stack_m1B0;
    v_stack_m1F0 = v_stack_m1B8;
    v_stack_m218 = v_stack_m188;
    v_stack_m20C = (uint32_t)((uint32_t)(v_stack_m190));
    v_stack_m1F8 = v_stack_m198;
    v_stack_m1D8 = 0;
    if ((uint32_t)((uint16_t)((uint32_t)(v_stack_m180))) != 0) goto loc_008E2750;
    if (v_stack_m198 == 0) goto loc_008E262E;
    Arg2 = v_stack_m198;
    if ((uint32_t)((uint32_t)(v_stack_m190)) == 0) { Arg2 = 0; }
    v_stack_m1F8 = Arg2;
loc_008E2305:
    Arg2 = 0;
    *(uint32_t *)(v_stack_m1A0) = 0;
    *(uint32_t *)(v_stack_m188) = 0;
    result = memset(v_stack_m178, Arg2, Arg2 + 64, v_stack_m188);
    if (((uint32_t)((int32_t)(Arg3) - 1)) > 10) goto loc_008E2678;
    if (*(uint64_t *)(arg1 + (int32_t)(arg3) * 8 + 0x128) == 0) goto loc_008E27E8;
    v_stack_m178 = v_stack_m1F0;
    v_stack_m168 = v_stack_m1E0;
    v_stack_m158 = v_stack_m1F8;
    v_stack_m140 = (uint32_t)((uint32_t)(v_stack_m224));
    v_stack_m150 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m190))));
    v_stack_m170 = v_stack_m1E8;
    v_stack_m160 = v_stack_m1A0;
    v_stack_m148 = v_stack_m218;
    if ((*(uint64_t *)(arg1 + (int32_t)(arg3) * 8 + 0x128)) != (v_rip - 1545)) goto loc_008E241C;
    v_stack_p20 = v_stack_m178;
    result = _PnpDispatchDevice(Arg1, 0, (uint32_t)((uint32_t)((int32_t)(Arg3))), 8);
loc_008E2399:
    if (((uint32_t)(result)) == 0xC0000016ULL) goto loc_008E2442;
loc_008E23A6:
    if (v_stack_m1D8 != 0) {
        result = ZwClose(v_stack_m1D8, 0, (uint32_t)((uint32_t)((int32_t)(Arg3))), 8);
    }
loc_008E23BE:
    if (*(uint64_t *)(arg1 + 0x1E8) == 0) goto loc_008E2415;
    v_stack_p28 = v_stack_m1C8;
    v_stack_p20 = 2;
    v_stack_m1C8 = (uint32_t)((uint32_t)((uint32_t)(result)));
    if ((*(uint64_t *)(arg1 + 0x1E8)) != (v_rip + 1170)) goto loc_008E282F;
    result = PiPnpRtlObjectActionCallback(Arg1, v_stack_m1D0, (uint32_t)((uint32_t)((uint32_t)(v_stack_m208))), 8);
loc_008E23F5:
    if (((uint32_t)(result)) == 0xC0000002ULL) goto loc_008E2415;
    if (((uint32_t)(result)) == 0xC0000120ULL) goto loc_008E2272;
    if ((uint32_t)(result) == 0) goto loc_008E2415;
loc_008E240B:
    goto loc_008E2275;
loc_008E2415:
    goto loc_008E2275;
loc_008E241C:
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))))) != (v_rip - 5747)) goto loc_008E2639;
    v_stack_p20 = v_stack_m178;
    result = _PnpDispatchDeviceInterface(Arg1, v_stack_m1D0, (uint32_t)((uint32_t)((uint32_t)(v_stack_m208))), 8);
    goto loc_008E2399;
loc_008E2442:
    if (v_stack_m1F0 == 0) goto loc_008E275A;
loc_008E244C:
    *(uint32_t *)(v_stack_m1A0) = 0;
    v_stack_m200 = 0;
    v_stack_m224 = 0;
    v_stack_m210 = 0;
    v_stack_m228 = 0;
    *(uint32_t *)(v_rip + 0x492) = 0;
    if (v_stack_m1E8 != 0) goto loc_008E265F;
loc_008E246F:
    v_stack_p88 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m1E0 + 0x10)));
    v_stack_p80 = (uint32_t)(*(uint8_t *)(v_stack_m1E0 + 0xF));
    v_stack_p78 = (uint32_t)(*(uint8_t *)(v_stack_m1E0 + 0xE));
    v_stack_p70 = (uint32_t)(*(uint8_t *)(v_stack_m1E0 + 0xD));
    Arg3 = 0;
    v_stack_p68 = (uint32_t)(*(uint8_t *)(v_stack_m1E0 + 0xC));
    Arg4 = 0;
    v_stack_p60 = (uint32_t)(*(uint8_t *)(v_stack_m1E0 + 0xB));
    v_stack_p58 = (uint32_t)(*(uint8_t *)(v_stack_m1E0 + 0xA));
    v_stack_p50 = (uint32_t)(*(uint8_t *)(v_stack_m1E0 + 0x9));
    v_stack_p48 = (uint32_t)(*(uint8_t *)(v_stack_m1E0 + 0x8));
    v_stack_p40 = (uint32_t)(*(uint16_t *)(v_stack_m1E0 + 0x6));
    v_stack_p38 = (uint32_t)(*(uint16_t *)(v_stack_m1E0 + 0x4));
    v_stack_p30 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m1E0)));
    v_stack_p28 = v_rip + 2274263;
    v_stack_p20 = 0x800ULL;
    result = RtlStringCchPrintfExW(v_stack_m138, Arg4 + 48, Arg3, Arg4);
    if (sign_flag) goto loc_008E25FA;
    v_stack_m200 = 0;
loc_008E2524:
    if ((*(uint16_t *)(v_stack_m138)) == 0) goto loc_008E253E;
    result = (v_stack_m138) + (2);
    Arg1 = (512) - (1);
    if (condition_is_not_equal) goto loc_008E2524;
    goto loc_008E25FA;
loc_008E253E:
    local_rdi = (512) - (Arg1);
    if (local_rdi >= 48) goto loc_008E27F2;
loc_008E2557:
    v_stack_p38 = v_stack_m138;
    Arg4 = 0;
    Arg3 = 0;
    v_stack_p30 = v_rip + 2205652;
    v_stack_p28 = v_rip + 2207410;
    v_stack_p20 = 0x800ULL;
    result = RtlStringCchPrintfExW(v_stack_mD8, 59, Arg3, Arg4);
    if (sign_flag) goto loc_008E25D8;
    if (*(uint64_t *)(arg1 + 0xE0) != 0) {
        local_r15 = *(uint64_t *)(*(uint64_t *)(arg1 + 0xE0) + 0x8);
    }
    v_stack_p28 = local_r15;
    Arg3 = 0;
    v_stack_p20 = v_stack_m200;
    result = _RegRtlOpenKeyTransacted(v_stack_m1F0, v_stack_mD8, Arg3, 1);
    local_rdi = (uint32_t)((uint32_t)(result));
    if (((uint32_t)(result)) == 0xC000017CULL) { local_rdi = (uint32_t)((uint32_t)(0xC0000034ULL)); }
loc_008E25D8:
    if (v_stack_mD8 == 0) goto loc_008E25ED;
    if (v_stack_mD8 != v_stack_mD8) goto loc_008E2820;
loc_008E25ED:
    if (((uint32_t)(local_rdi)) != ((uint32_t)((uint32_t)(0xC0000034ULL)))) goto loc_008E268A;
loc_008E25F5:
loc_008E25FA:
loc_008E25FE:
loc_008E2602:
    result = v_stack_mD8;
    if (v_stack_m200 != 0) {
        result = ZwClose(v_stack_m200, v_stack_mD8, Arg3, 1);
    }
    if (sign_flag) goto loc_008E23A6;
    result = PnpValidatePropertyData(v_stack_m1F8, (uint32_t)(*(uint32_t *)(v_stack_m218)), (uint32_t)(*(uint32_t *)(v_stack_m220)), 1);
    goto loc_008E23A6;
loc_008E262E:
    v_stack_m20C = (uint32_t)((uint32_t)((uint32_t)(v_stack_m218)));
    goto loc_008E2305;
loc_008E2639:
    if (result != (v_rip + 318816)) goto loc_008E272B;
    v_stack_p20 = v_stack_m178;
    result = DrvDbDispatchDriverPackage(Arg1, (uint32_t)(*(uint32_t *)(v_stack_m218)), (uint32_t)(*(uint32_t *)(v_stack_m220)), 1);
    goto loc_008E2399;
loc_008E265F:
loc_008E2664:
    if ((*(uint16_t *)(result)) == ((uint16_t)(v_stack_m218))) goto loc_008E246F;
    result = (result) + (2);
    Arg1 = (85) - (1);
    if (condition_is_not_equal) goto loc_008E2664;
loc_008E2678:
    goto loc_008E23A6;
loc_008E2682:
    goto loc_008E22A1;
loc_008E268A:
    if (sign_flag) goto loc_008E25FA;
    v_stack_m210 = (uint32_t)((uint32_t)(v_stack_m20C));
    if (*(uint64_t *)(arg1 + 0x208) != 0) goto loc_008E2794;
loc_008E26AC:
    v_stack_p30 = v_stack_m228;
    v_stack_p28 = v_stack_m210;
    v_stack_p20 = v_stack_m1F8;
    result = PnpRegQueryValueIndirect(Arg1, v_stack_m200, v_stack_m1E8, v_stack_m224);
loc_008E26DB:
    if (((uint32_t)(result)) == 0xC0000034ULL) goto loc_008E25F5;
    if (((uint32_t)(result)) == 0xC000017CULL) goto loc_008E25F5;
    if ((uint32_t)(result) != 0) goto loc_008E2741;
loc_008E26F7:
    *(uint32_t *)(v_stack_m220) = (uint32_t)(v_stack_m224);
    if (((uint32_t)(v_stack_m224)) == 1) goto loc_008E25FE;
    *(uint32_t *)(v_stack_m218) = (uint32_t)((uint32_t)(v_stack_m210));
    if ((uint32_t)((uint32_t)((uint32_t)(result))) != 0) goto loc_008E2721;
    if ((uint32_t)((uint32_t)(v_stack_m20C)) != 0) goto loc_008E2602;
loc_008E2721:
    goto loc_008E2602;
loc_008E272B:
    v_stack_p20 = v_stack_m178;
    result = guard_dispatch_icall(Arg1, v_stack_m200, v_stack_m1E8, v_stack_m224);
    goto loc_008E2399;
loc_008E2741:
    if (((uint32_t)(Arg1)) == 0xC0000023ULL) goto loc_008E26F7;
    goto loc_008E25FA;
loc_008E2750:
    goto loc_008E23BE;
loc_008E275A:
    v_stack_p28 = v_stack_m1D8;
    v_stack_p20 = (uint8_t)(v_stack_m218);
    result = PnpOpenObjectRegKey(Arg1, v_stack_m1D0, (uint32_t)((uint32_t)(local_rdi)), (uint32_t)(0x2000001ULL));
    if (sign_flag) goto loc_008E23A6;
    v_stack_m1F0 = v_stack_m1D8;
    goto loc_008E244C;
loc_008E2794:
    if ((*(uint64_t *)(arg1 + 0x208)) == (v_rip + 47733)) goto loc_008E26AC;
    v_stack_p30 = v_stack_m228;
    v_stack_p28 = v_stack_m210;
    v_stack_p20 = v_stack_m1F8;
    result = guard_dispatch_icall(Arg1, v_stack_m200, v_stack_m1E8, v_stack_m224);
    goto loc_008E26DB;
loc_008E27DB:
    result = guard_dispatch_icall(Arg1, v_stack_m200, v_stack_m1E8, v_stack_m224);
    goto loc_008E2260;
loc_008E27E8:
    goto loc_008E23A6;
loc_008E27F2:
    local_rdi = (uint32_t)((local_rdi) + (12));
    Arg2 = ((uint32_t)((uint32_t)(local_rdi))) + ((uint32_t)((uint32_t)(local_rdi)));
    result = ExAllocatePool2(256, Arg2, (uint32_t)(0x52504E50ULL), v_stack_m224);
    if (result != 0) goto loc_008E2557;
    goto loc_008E25FA;
loc_008E2820:
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, (uint32_t)(0x52504E50ULL), v_stack_m224);
    goto loc_008E25ED;
loc_008E282F:
    result = guard_dispatch_icall(result, Arg2, (uint32_t)(0x52504E50ULL), v_stack_m224);
    goto loc_008E23F5;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xE0` | `64` | `R` |
| `Arg1` | `+ 0x128 + rdi*8` | `64` | `R` |
| `Arg1` | `+ 0x1E8` | `64` | `R` |
| `Arg1` | `+ 0x208` | `64` | `R` |
| `Arg3` | `- 0x1` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008E2180&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
