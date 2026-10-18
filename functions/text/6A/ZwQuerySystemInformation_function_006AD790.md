# ZwQuerySystemInformation

- RVA: `0x006AD790`–`0x006AD7AF` (길이 `31` bytes)
- VA: `0x00000001406AD790`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C0118`
- 디코드: `11`개 명령, `31/31` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **41**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [SmQuerySystemInformation](../3B/SmQuerySystemInformation_function_003B29F8.md) at `0x003B2A46`
- [IopLiveDumpIsUnderMemoryPressure](../3F/IopLiveDumpIsUnderMemoryPressure_function_003F5EB8.md) at `0x003F5EFF`
- [HvlpProcessIommu](../4D/HvlpProcessIommu_function_004DE458.md) at `0x004DE4C5`
- [RtlpCreateHeap](../4E/RtlpCreateHeap_function_004E1904.md) at `0x004E1C60`
- [RtlpInitializeNonVolatileFlush](../4E/RtlpInitializeNonVolatileFlush_function_004E2A38.md) at `0x004E2A69`
- [SmKmStoreTerminateWorker](../60/SmKmStoreTerminateWorker_function_0060FB30.md) at `0x0060FBF3`
- [SmKmStoreTerminateWorker](../60/SmKmStoreTerminateWorker_function_0060FB30.md) at `0x0060FC52`
- [DifZwQuerySystemInformationWrapper](../64/DifZwQuerySystemInformationWrapper_function_006488C0.md) at `0x006489B1`
- [ExpInitExpCheckTestSigningInfo](../65/ExpInitExpCheckTestSigningInfo_function_00659800.md) at `0x00659826`
- [HaliSetSystemInformation](../../page/70/HaliSetSystemInformation_function_0070BF54.md) at `0x0070BFBD`
- [PiIsHVCIEnabled](../../page/72/PiIsHVCIEnabled_function_0072E0B4.md) at `0x0072E0D5`
- [PipKsrCallback](../../page/73/PipKsrCallback_function_0073E3B0.md) at `0x0073E46B`
- [KsepGetLoadedModulesList](../../page/74/KsepGetLoadedModulesList_function_0074A960.md) at `0x0074A9AB`
- [PopCheckTestsigningEnabled](../../page/75/PopCheckTestsigningEnabled_function_00753FE0.md) at `0x00754004`
- [PopInitializeHibernateGlobals](../../page/75/PopInitializeHibernateGlobals_function_0075DA64.md) at `0x0075DA91`
- [PopInitializeHibernateGlobals](../../page/75/PopInitializeHibernateGlobals_function_0075DA64.md) at `0x0075DAC3`
- [PopValidateWinresume](../../page/75/PopValidateWinresume_function_0075DFF4.md) at `0x0075E0A8`
- [RtlLocalTimeToSystemTime](../../page/78/RtlLocalTimeToSystemTime_function_0078B2B0.md) at `0x0078B2F1`
- [ExpCloudbookHardwareIDProvider](../../page/7C/ExpCloudbookHardwareIDProvider_function_007C7D20.md) at `0x007C7DB7`
- [ExpCloudbookHardwareLockedProvider](../../page/7C/ExpCloudbookHardwareLockedProvider_function_007C7E20.md) at `0x007C7EBC`
- [SdbpCheckMatchingRegistryEntry](../../page/81/SdbpCheckMatchingRegistryEntry_function_0081444C.md) at `0x00814556`
- [AslEnvGetProcessWowInfo](../../page/81/AslEnvGetProcessWowInfo_function_0081D0A8.md) at `0x0081D0F2`
- [AslEnvGetProcessWowInfo](../../page/81/AslEnvGetProcessWowInfo_function_0081D0A8.md) at `0x0081D13E`
- [BiGetAliasedIdentifier](../../page/82/BiGetAliasedIdentifier_function_00823900.md) at `0x00823950`
- [PfpPrivSourceEnum](../../page/91/PfpPrivSourceEnum_function_0091BF00.md) at `0x0091C14D`
- [EtwpLogMemInfoWs](../../page/91/EtwpLogMemInfoWs_function_0091C594.md) at `0x0091C663`
- [sub_00968AF6](../../page/96/Unknown_function_00968AF6.md) at `0x00969AF7`
- [sub_00968AF6](../../page/96/Unknown_function_00968AF6.md) at `0x0096A05B`
- [sub_00968AF6](../../page/96/Unknown_function_00968AF6.md) at `0x0096A4BD`
- [PnpGetStableSystemBootTime](../../page/A2/PnpGetStableSystemBootTime_function_00A27C10.md) at `0x00A27C58`
- [RtlQueryModuleInformation](../../page/A3/RtlQueryModuleInformation_function_00A35040.md) at `0x00A350D2`
- [BiGetFirmwareType](../../page/A3/BiGetFirmwareType_function_00A3FA5C.md) at `0x00A3FAC9`
- [SiGetFirmwareType](../../page/A5/SiGetFirmwareType_function_00A5597C.md) at `0x00A559B2`
- [ExpFindDiskSignature](../../page/A7/ExpFindDiskSignature_function_00A7B608.md) at `0x00A7B666`
- [SiQuerySystemInformationString](../../page/A9/SiQuerySystemInformationString_function_00A97438.md) at `0x00A97468`
- [SiQuerySystemInformationString](../../page/A9/SiQuerySystemInformationString_function_00A97438.md) at `0x00A974A5`
- [EtwpTiQueryCodeIntegrityOptions](../../page/A9/EtwpTiQueryCodeIntegrityOptions_function_00A986FC.md) at `0x00A98726`
- [RtlSystemTimeToLocalTime](../../page/AA/RtlSystemTimeToLocalTime_function_00AAC390.md) at `0x00AAC3D1`
- [PspQueryComPlusRunUnderWoW](../../page/AB/PspQueryComPlusRunUnderWoW_function_00ABC8EC.md) at `0x00ABC91E`
- [PopAllocateHiberContext](../../page/AD/PopAllocateHiberContext_function_00ADC05C.md) at `0x00ADC679`
- [IoShutdownSystem](../../pagelk/B6/IoShutdownSystem_function_00B63B8C.md) at `0x00B63BED`
- [PopGetHwConfigurationSignature](../../pagelk/B6/PopGetHwConfigurationSignature_function_00B6D5A4.md) at `0x00B6D60A`
- [PopGetHwConfigurationSignature](../../pagelk/B6/PopGetHwConfigurationSignature_function_00B6D5A4.md) at `0x00B6D666`
- [HdlspAddLogEntry](../../pagehdls/BB/HdlspAddLogEntry_function_00BBD008.md) at `0x00BBD080`
- [PopInitPlatformSettings](../../init/C3/PopInitPlatformSettings_function_00C3D40C.md) at `0x00C3D46E`
- [PopInitPlatformSettings](../../init/C3/PopInitPlatformSettings_function_00C3D40C.md) at `0x00C3D4EA`
- [PopCheckShutdownMarker](../../init/C3/PopCheckShutdownMarker_function_00C3DAD4.md) at `0x00C3E0F3`
- [SepInitializeDebugOptions](../../init/C4/SepInitializeDebugOptions_function_00C4A69C.md) at `0x00C4A6FA`
- [MiInitializeCacheFlushing](../../init/C6/MiInitializeCacheFlushing_function_00C6ACF8.md) at `0x00C6AD4B`

### Static image references
- `0x006AD79C` → RVA `0x006B3460` (`KiServiceLinkage`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006AD7A9` → [KiServiceInternal](../6C/KiServiceInternal_function_006C49C0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006AD790  48 8B C4                        mov rax, rsp
006AD793  FA                              cli
006AD794  48 83 EC 10                     sub rsp, 0x10
006AD798  50                              push rax
006AD799  9C                              pushfq
006AD79A  6A 10                           push 0x10
006AD79C  48 8D 05 BD 5C 00 00            lea rax, [rip + 0x5cbd]
006AD7A3  50                              push rax
006AD7A4  B8 36 00 00 00                  mov eax, 0x36
006AD7A9  E9 12 72 01 00                  jmp 0x1406c49c0
006AD7AE  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ZwQuerySystemInformation(void)
{
    __int64 v_rsp;

    v_rsp = (v_rsp) - (16);
}
```

## 5. (Beta) C Style

```c
void ZwQuerySystemInformation(void)
{
    int64_t local_rsp;

    local_rsp = (local_rsp) - (16);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006AD790&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006AD790[BB_006AD790]
  bb_006AD7AE[BB_006AD7AE]
```
