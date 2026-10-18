# RtlCopyUnicodeString

- RVA: `0x003FEF30`–`0x003FEF4E` (길이 `30` bytes)
- VA: `0x00000001403FEF30`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00099F74`
- 디코드: `9`개 명령, `30/30` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **66**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [RtlPcToFileName](RtlPcToFileName_function_003FEBB0.md) at `0x003FEBE3`
- [AuthzBasepCopyoutInternalSecurityAttributeValues](AuthzBasepCopyoutInternalSecurityAttributeValues_function_003FEC10.md) at `0x003FED43`
- [AuthzBasepCopyoutInternalSecurityAttributeValues](AuthzBasepCopyoutInternalSecurityAttributeValues_function_003FEC10.md) at `0x003FED88`
- [IoQueryFullDriverPath](IoQueryFullDriverPath_function_003FEDF0.md) at `0x003FEE32`
- [PnpAllocateWatchdog](PnpAllocateWatchdog_function_003FEE5C.md) at `0x003FEEF5`
- [HalpRegisterDmaController](../55/HalpRegisterDmaController_function_00554638.md) at `0x005547A0`
- [HalpTimerRegister](../56/HalpTimerRegister_function_005616BC.md) at `0x00561959`
- [HalpInterruptRegisterController](../56/HalpInterruptRegisterController_function_005640F0.md) at `0x00564520`
- [OpenGlobalizationUserSettingsKey_ForSingleUserModel](../65/OpenGlobalizationUserSettingsKey_ForSingleUserModel_function_0065D368.md) at `0x0065D4E1`
- [OpenGlobalizationUserSettingsKey_ForSingleUserModel](../65/OpenGlobalizationUserSettingsKey_ForSingleUserModel_function_0065D368.md) at `0x0065D541`
- [MicrocodeLogRegistry](../66/MicrocodeLogRegistry_function_00667340.md) at `0x00667398`
- [IoReportRootDevice](../../page/72/IoReportRootDevice_function_00726780.md) at `0x0072683B`
- [PnpNotifyHwProfileChange](../../page/72/PnpNotifyHwProfileChange_function_00729B04.md) at `0x00729C36`
- [PnpQueryRemoveLockedDeviceNode](../../page/72/PnpQueryRemoveLockedDeviceNode_function_0072D210.md) at `0x0072D2B5`
- [PnpCopyDeviceInstancePath](../../page/72/PnpCopyDeviceInstancePath_function_0072DC70.md) at `0x0072DC78`
- [PiInitializeDevice](../../page/73/PiInitializeDevice_function_0073EC5C.md) at `0x0073EF85`
- [IopFileUtilWalkDirectoryTreeBottomUp](../../page/73/IopFileUtilWalkDirectoryTreeBottomUp_function_0073FB40.md) at `0x0073FBE2`
- [IopFileUtilWalkDirectoryTreeHelper](../../page/73/IopFileUtilWalkDirectoryTreeHelper_function_0073FD40.md) at `0x0073FEC7`
- [PipSendQueryRemoveIrpAndCheckOpenHandles](../../page/74/PipSendQueryRemoveIrpAndCheckOpenHandles_function_007443E8.md) at `0x0074454F`
- [PopFxRegisterComponentPerfStates](../../page/75/PopFxRegisterComponentPerfStates_function_00759764.md) at `0x00759AA7`
- [PopConnectToPolicyDevice](../../page/76/PopConnectToPolicyDevice_function_00765D20.md) at `0x00765DC4`
- [PspSiloInitializeSystemRootSymlink](../../page/78/PspSiloInitializeSystemRootSymlink_function_00780558.md) at `0x007805E8`
- [PspSiloInitializeUserSharedData](../../page/78/PspSiloInitializeUserSharedData_function_00780684.md) at `0x00780791`
- [PsRegisterSiloMonitor](../../page/78/PsRegisterSiloMonitor_function_007866A0.md) at `0x00786767`
- [CmpLoadHiveVolatile](../../page/7D/CmpLoadHiveVolatile_function_007DE5F0.md) at `0x007DE8F8`
- [CmpMergeVersionDescriptors](../../page/7E/CmpMergeVersionDescriptors_function_007E7320.md) at `0x007E73A6`
- [CmpMergeVersionDescriptors](../../page/7E/CmpMergeVersionDescriptors_function_007E7320.md) at `0x007E73C9`
- [CmpMergeVersionDescriptors](../../page/7E/CmpMergeVersionDescriptors_function_007E7320.md) at `0x007E73F6`
- [CmpMergeVersionDescriptors](../../page/7E/CmpMergeVersionDescriptors_function_007E7320.md) at `0x007E7419`
- [CmpMergeVersionDescriptors](../../page/7E/CmpMergeVersionDescriptors_function_007E7320.md) at `0x007E7443`
- [MiAllocateSecureImageActivePatch](../../page/80/MiAllocateSecureImageActivePatch_function_00801890.md) at `0x008018D2`
- [MiFillActivePatchesQueryBuffer](../../page/80/MiFillActivePatchesQueryBuffer_function_008034D4.md) at `0x00803529`
- [AdtpObjsInitialize](../../page/82/AdtpObjsInitialize_function_00822B30.md) at `0x00822DBA`
- [AdtpObjsInitialize](../../page/82/AdtpObjsInitialize_function_00822B30.md) at `0x00822F78`
- [AhcCacheQueryHwId](../../page/83/AhcCacheQueryHwId_function_0083ACB8.md) at `0x0083AE0F`
- [ObGetSiloRootDirectoryPath](../../page/83/ObGetSiloRootDirectoryPath_function_0083CD74.md) at `0x0083CE74`
- [sub_0086E95E](../../page/86/Unknown_function_0086E95E.md) at `0x0086EBAD`
- [sub_0086E95E](../../page/86/Unknown_function_0086E95E.md) at `0x0086EC09`
- [IopParseDevice](../../page/89/IopParseDevice_function_0089E510.md) at `0x0089F3D6`
- [IopParseDevice](../../page/89/IopParseDevice_function_0089E510.md) at `0x0089F597`
- [IopParseDevice](../../page/89/IopParseDevice_function_0089E510.md) at `0x0089FBB4`
- [IopSymlinkUpdateECP](../../page/8A/IopSymlinkUpdateECP_function_008A20CC.md) at `0x008A212F`
- [EtwpGetLoggerInfoFromContext](../../page/8B/EtwpGetLoggerInfoFromContext_function_008BEF90.md) at `0x008BF270`
- [EtwpGetLoggerInfoFromContext](../../page/8B/EtwpGetLoggerInfoFromContext_function_008BEF90.md) at `0x008BF30D`
- [PipProcessDevNodeTree](../../page/8F/PipProcessDevNodeTree_function_008F9068.md) at `0x008F9455`
- [sub_00927BEB](../../page/92/Unknown_function_00927BEB.md) at `0x00927CD0`
- [sub_0093345B](../../page/93/Unknown_function_0093345B.md) at `0x00933540`
- [VrpBuildKeyPath](../../page/93/VrpBuildKeyPath_function_00934650.md) at `0x009346CD`
- [FsRtlFindInTunnelCacheEx](../../page/93/FsRtlFindInTunnelCacheEx_function_00937A50.md) at `0x00937AE0`
- [FsRtlFindInTunnelCacheEx](../../page/93/FsRtlFindInTunnelCacheEx_function_00937A50.md) at `0x00937B00`
- [PnpConcatenateUnicodeStrings](../../page/95/PnpConcatenateUnicodeStrings_function_00951ED0.md) at `0x00951EF2`
- [SdbMakeIndexKeyFromStringEx](../../page/95/SdbMakeIndexKeyFromStringEx_function_0095E9F4.md) at `0x0095EA81`
- [CmpGetVirtualizationID](../../page/99/CmpGetVirtualizationID_function_00990338.md) at `0x009903DF`
- [IopQueryRegistryKeySystemPath](../../page/99/IopQueryRegistryKeySystemPath_function_0099A1CC.md) at `0x0099A3DE`
- [SepAllocateAndInitializeCachedHandleEntry](../../page/9A/SepAllocateAndInitializeCachedHandleEntry_function_009A97B0.md) at `0x009A989D`
- [AuthzBasepCopyoutInternalSecurityAttributes](../../page/9E/AuthzBasepCopyoutInternalSecurityAttributes_function_009EA280.md) at `0x009EA3B3`
- [sub_009EB6B7](../../page/9E/Unknown_function_009EB6B7.md) at `0x009EB6FA`
- [PipSendTargetDeviceQueryRemoveNotification](../../page/A0/PipSendTargetDeviceQueryRemoveNotification_function_00A04518.md) at `0x00A045CF`
- [PnpFinalizeVetoedRemove](../../page/A0/PnpFinalizeVetoedRemove_function_00A04968.md) at `0x00A049A2`
- [PiDeviceRegistration](../../page/A0/PiDeviceRegistration_function_00A07A60.md) at `0x00A07C05`
- [MiCreateSectionForDriver](../../page/A2/MiCreateSectionForDriver_function_00A2477C.md) at `0x00A248AF`
- [RtlPcToFilePath](../../page/A2/RtlPcToFilePath_function_00A2B9A0.md) at `0x00A2B9C1`
- [MiQuerySingleLoadedPatch](../../page/A4/MiQuerySingleLoadedPatch_function_00A41EB0.md) at `0x00A4204D`
- [PiDeferSetInterfaceState](../../page/AA/PiDeferSetInterfaceState_function_00AA6FA4.md) at `0x00AA6FFA`
- [ObCreateObjectTypeEx](../../page/AB/ObCreateObjectTypeEx_function_00AB46D0.md) at `0x00AB4892`
- [MiQueryLoadedPatches](../../page/AB/MiQueryLoadedPatches_function_00ABE538.md) at `0x00ABE72D`
- [IopSafebootDriverLoad](../../page/AD/IopSafebootDriverLoad_function_00AD2880.md) at `0x00AD2926`
- [SepAddTokenOriginClaim](../../page/AF/SepAddTokenOriginClaim_function_00AF2130.md) at `0x00AF230F`
- [sub_00B29542](../../page/B2/Unknown_function_00B29542.md) at `0x00B2970B`
- [sub_00B29542](../../page/B2/Unknown_function_00B29542.md) at `0x00B2976F`
- [sub_00B2CE30](../../page/B2/Unknown_function_00B2CE30.md) at `0x00B2CE61`
- [sub_00B2EDF4](../../page/B2/Unknown_function_00B2EDF4.md) at `0x00B2EED4`
- [sub_00B336B0](../../page/B3/Unknown_function_00B336B0.md) at `0x00B33DBE`
- [sub_00B33FE8](../../page/B3/Unknown_function_00B33FE8.md) at `0x00B340CF`
- [sub_00B420B0](../../page/B4/Unknown_function_00B420B0.md) at `0x00B42177`
- [sub_00B46996](../../page/B4/Unknown_function_00B46996.md) at `0x00B46996`
- [PopProcessWakeSourceWork](../../pagelk/B7/PopProcessWakeSourceWork_function_00B7C488.md) at `0x00B7C583`
- [ExtEnvRegisterIommu](../../init/C2/ExtEnvRegisterIommu_function_00C213EC.md) at `0x00C21795`
- [StartFirstUserProcess](../../init/C7/StartFirstUserProcess_function_00C70848.md) at `0x00C7097C`
- [StartFirstUserProcess](../../init/C7/StartFirstUserProcess_function_00C70848.md) at `0x00C7099E`
- [StartFirstUserProcess](../../init/C7/StartFirstUserProcess_function_00C70848.md) at `0x00C709CB`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x003FEF3C` → [sub_003FEF9C + 0x1](Unknown_function_003FEF9C.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
003FEF30  40 53                           push rbx
003FEF32  48 83 EC 20                     sub rsp, 0x20
003FEF36  48 8B D9                        mov rbx, rcx
003FEF39  48 85 D2                        test rdx, rdx
003FEF3C  74 5F                           je 0x1403fef9d
003FEF3E  44 0F B7 02                     movzx r8d, word ptr [rdx]
003FEF42  0F B7 41 02                     movzx eax, word ptr [rcx + 2]
003FEF46  4C 8B 4A 08                     mov r9, qword ptr [rdx + 8]
003FEF4A  66 44 3B C0                     cmp r8w, ax
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlCopyUnicodeString(__int64 a1, __int64 a2)
{
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    return *(unsigned __int16 *)(a1 + 2);
}
```

## 5. (Beta) C Style

```c
int64_t RtlCopyUnicodeString(void *Arg1, int64_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    return *(uint16_t *)(arg1 + 0x2);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x2` | `16` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003FEF30&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003FEF30[BB_003FEF30]
  bb_003FEF3E[BB_003FEF3E]
  bb_003FEF30 -->|fallthrough| bb_003FEF3E
```
