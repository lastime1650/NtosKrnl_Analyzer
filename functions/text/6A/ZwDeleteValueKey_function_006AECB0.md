# ZwDeleteValueKey

- RVA: `0x006AECB0`–`0x006AECCF` (길이 `31` bytes)
- VA: `0x00000001406AECB0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C0904`
- 디코드: `11`개 명령, `31/31` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **34**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [VfClearVerifierSettings](../61/VfClearVerifierSettings_function_00611DB0.md) at `0x00611E9E`
- [VfClearVerifierSettings](../61/VfClearVerifierSettings_function_00611DB0.md) at `0x00611EDE`
- [VfClearVerifierSettings](../61/VfClearVerifierSettings_function_00611DB0.md) at `0x00611F14`
- [VfClearVerifierSettings](../61/VfClearVerifierSettings_function_00611DB0.md) at `0x00611F4A`
- [VfClearVerifierSettings](../61/VfClearVerifierSettings_function_00611DB0.md) at `0x00611F89`
- [VfClearVerifierSettings](../61/VfClearVerifierSettings_function_00611DB0.md) at `0x00611FBF`
- [VfClearVerifierSettings](../61/VfClearVerifierSettings_function_00611DB0.md) at `0x00611FF5`
- [VfClearVerifierSettings](../61/VfClearVerifierSettings_function_00611DB0.md) at `0x00612034`
- [VfClearVerifierSettings](../61/VfClearVerifierSettings_function_00611DB0.md) at `0x0061206A`
- [VfClearVerifierSettings](../61/VfClearVerifierSettings_function_00611DB0.md) at `0x006120A0`
- [VfClearVerifierSettings](../61/VfClearVerifierSettings_function_00611DB0.md) at `0x006120D6`
- [VfClearVerifierSettings](../61/VfClearVerifierSettings_function_00611DB0.md) at `0x0061210C`
- [VfClearVerifierSettings](../61/VfClearVerifierSettings_function_00611DB0.md) at `0x00612142`
- [DifZwDeleteValueKeyWrapper](../64/DifZwDeleteValueKeyWrapper_function_00640ED0.md) at `0x00640FA4`
- [CmpSetSystemRegistryString](../66/CmpSetSystemRegistryString_function_0066A2F0.md) at `0x0066A35B`
- [BiZwDeleteValueKey](../69/BiZwDeleteValueKey_function_0069E3EC.md) at `0x0069E3F0`
- [IopWriteResourceList](../../page/72/IopWriteResourceList_function_0072A5F0.md) at `0x0072A682`
- [PopThermalHandlePreviousShutdown](../../page/75/PopThermalHandlePreviousShutdown_function_0075F400.md) at `0x0075F62D`
- [PopThermalHandlePreviousShutdown](../../page/75/PopThermalHandlePreviousShutdown_function_0075F400.md) at `0x0075F7AB`
- [PopThermalHandlePreviousShutdown](../../page/75/PopThermalHandlePreviousShutdown_function_0075F400.md) at `0x0075F7B8`
- [PopThermalHandlePreviousShutdown](../../page/75/PopThermalHandlePreviousShutdown_function_0075F400.md) at `0x0075F7C4`
- [SmKmKeyGenNewKey](../../page/7A/SmKmKeyGenNewKey_function_007A8990.md) at `0x007A8B30`
- [WdipSemLoadConfigInfo](../../page/7A/WdipSemLoadConfigInfo_function_007AF700.md) at `0x007AF7FB`
- [ExpWnfDeletePermanentStateData](../../page/7D/ExpWnfDeletePermanentStateData_function_007D6254.md) at `0x007D6305`
- [CmpSetVersionData](../../page/7E/CmpSetVersionData_function_007E7854.md) at `0x007E7C4C`
- [CmpSetVersionData](../../page/7E/CmpSetVersionData_function_007E7854.md) at `0x007E7CDE`
- [CmpDoReDoRecord](../../page/7F/CmpDoReDoRecord_function_007F76B8.md) at `0x007F7839`
- [NtEnableLastKnownGood](../../page/83/NtEnableLastKnownGood_function_0083C680.md) at `0x0083C7C1`
- [RtlpQueryRegistryValues](../../page/8C/RtlpQueryRegistryValues_function_008C9050.md) at `0x008C9480`
- [RtlpQueryRegistryValues](../../page/8C/RtlpQueryRegistryValues_function_008C9050.md) at `0x008C9513`
- [PnpCtxRegDeleteValue](../../page/8F/PnpCtxRegDeleteValue_function_008FE5E0.md) at `0x008FE60A`
- [PiDevCfgCopyDeviceKey](../../page/99/PiDevCfgCopyDeviceKey_function_00997374.md) at `0x00997A6D`
- [PiProcessDriverInstance](../../page/99/PiProcessDriverInstance_function_00998530.md) at `0x00998755`
- [PiRearrangeDeviceInstances](../../page/99/PiRearrangeDeviceInstances_function_0099AF9C.md) at `0x0099B0A6`
- [CmpCompleteUnloadKey](../../page/9B/CmpCompleteUnloadKey_function_009B32FC.md) at `0x009B342D`
- [IopReleaseDeviceResources](../../page/A0/IopReleaseDeviceResources_function_00A0867C.md) at `0x00A087F1`
- [ExpSetPendingUILanguage](../../page/A8/ExpSetPendingUILanguage_function_00A87E70.md) at `0x00A88222`
- [ExpWnfDeletePermanentName](../../page/A9/ExpWnfDeletePermanentName_function_00A99434.md) at `0x00A99497`
- [PerfDiagpSaveActiveDCLLogFileName](../../page/A9/PerfDiagpSaveActiveDCLLogFileName_function_00A9EB80.md) at `0x00A9ED1F`
- [IopWriteAllocatedResourcesToRegistry](../../page/AA/IopWriteAllocatedResourcesToRegistry_function_00AA54E4.md) at `0x00AA55CC`
- [NtSetDefaultLocale](../../page/AA/NtSetDefaultLocale_function_00AAE850.md) at `0x00AAEA7B`
- [PnpDriverLoadingFailed](../../page/AB/PnpDriverLoadingFailed_function_00AB8928.md) at `0x00AB8C63`
- [RtlDeleteRegistryValue](../../page/AD/RtlDeleteRegistryValue_function_00ADA1B0.md) at `0x00ADA1F4`
- [sub_00B1FD92](../../page/B1/Unknown_function_00B1FD92.md) at `0x00B1FDFE`
- [sub_00B1FEC0](../../page/B1/Unknown_function_00B1FEC0.md) at `0x00B1FF4B`
- [sub_00B44C1A](../../page/B4/Unknown_function_00B44C1A.md) at `0x00B44CBB`
- [sub_00B44C1A](../../page/B4/Unknown_function_00B44C1A.md) at `0x00B44DF6`
- [sub_00B44C1A](../../page/B4/Unknown_function_00B44C1A.md) at `0x00B44E3F`
- [sub_00B44C1A](../../page/B4/Unknown_function_00B44C1A.md) at `0x00B44F0A`
- [BapdRemoveWbclData](../../pagelk/B5/BapdRemoveWbclData_function_00B5B2EC.md) at `0x00B5B326`
- [BapdRemoveWbclData](../../pagelk/B5/BapdRemoveWbclData_function_00B5B2EC.md) at `0x00B5B343`
- [BapdRemoveWbclData](../../pagelk/B5/BapdRemoveWbclData_function_00B5B2EC.md) at `0x00B5B360`
- [ArbDeleteMmConfigRange](../../init/C2/ArbDeleteMmConfigRange_function_00C25D5C.md) at `0x00C25E3A`
- [PipHardwareConfigInit](../../init/C3/PipHardwareConfigInit_function_00C30D24.md) at `0x00C30DFB`
- [PipHardwareConfigInit](../../init/C3/PipHardwareConfigInit_function_00C30D24.md) at `0x00C3118B`
- [PipHardwareConfigInit](../../init/C3/PipHardwareConfigInit_function_00C30D24.md) at `0x00C3125B`
- [BapdpProcessVsmKeyBlobs](../../init/C4/BapdpProcessVsmKeyBlobs_function_00C4FD60.md) at `0x00C50009`
- [PipInitComputerIds](../../init/C7/PipInitComputerIds_function_00C74734.md) at `0x00C74D3C`

### Static image references
- `0x006AECBC` → RVA `0x006B3460` (`KiServiceLinkage`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006AECC9` → [KiServiceInternal](../6C/KiServiceInternal_function_006C49C0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006AECB0  48 8B C4                        mov rax, rsp
006AECB3  FA                              cli
006AECB4  48 83 EC 10                     sub rsp, 0x10
006AECB8  50                              push rax
006AECB9  9C                              pushfq
006AECBA  6A 10                           push 0x10
006AECBC  48 8D 05 9D 47 00 00            lea rax, [rip + 0x479d]
006AECC3  50                              push rax
006AECC4  B8 DF 00 00 00                  mov eax, 0xdf
006AECC9  E9 F2 5C 01 00                  jmp 0x1406c49c0
006AECCE  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ZwDeleteValueKey(void)
{
    __int64 v_rsp;

    v_rsp = (v_rsp) - (16);
}
```

## 5. (Beta) C Style

```c
void ZwDeleteValueKey(void)
{
    int64_t local_rsp;

    local_rsp = (local_rsp) - (16);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006AECB0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006AECB0[BB_006AECB0]
  bb_006AECCE[BB_006AECCE]
```
