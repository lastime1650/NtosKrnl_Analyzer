# ZwPowerInformation

- RVA: `0x006ADCB0`–`0x006ADCCF` (길이 `31` bytes)
- VA: `0x00000001406ADCB0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C0304`
- 디코드: `11`개 명령, `31/31` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **21**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [HalpSetShutdownResetHandler](../54/HalpSetShutdownResetHandler_function_00546948.md) at `0x0054698E`
- [DifZwPowerInformationWrapper](../64/DifZwPowerInformationWrapper_function_006454F0.md) at `0x006455EC`
- [HaliAcpiMachineStateInit](../../page/70/HaliAcpiMachineStateInit_function_0070B730.md) at `0x0070B7E9`
- [HaliAcpiMachineStateInit](../../page/70/HaliAcpiMachineStateInit_function_0070B730.md) at `0x0070B869`
- [HaliAcpiMachineStateInit](../../page/70/HaliAcpiMachineStateInit_function_0070B730.md) at `0x0070B8E5`
- [HaliAcpiMachineStateInit](../../page/70/HaliAcpiMachineStateInit_function_0070B730.md) at `0x0070B95F`
- [HaliAcpiMachineStateInit](../../page/70/HaliAcpiMachineStateInit_function_0070B730.md) at `0x0070B9C5`
- [HaliAcpiMachineStateInit](../../page/70/HaliAcpiMachineStateInit_function_0070B730.md) at `0x0070BA1F`
- [HaliAcpiMachineStateInit](../../page/70/HaliAcpiMachineStateInit_function_0070B730.md) at `0x0070BA83`
- [PoGetLightestSystemStateForEject](../../page/75/PoGetLightestSystemStateForEject_function_00753E30.md) at `0x00753F57`
- [RtlCheckSystemBootStatusIntegrity](../../page/79/RtlCheckSystemBootStatusIntegrity_function_007905C0.md) at `0x00790611`
- [RtlRestoreSystemBootStatusDefaults](../../page/79/RtlRestoreSystemBootStatusDefaults_function_00790900.md) at `0x0079092B`
- [PdcPortOpenCommon](../../page/79/PdcPortOpenCommon_function_0079B544.md) at `0x0079B6B0`
- [PspRecordCrashedProcessIntoBlackbox](../../page/8A/PspRecordCrashedProcessIntoBlackbox_function_008A3514.md) at `0x008A35BC`
- [PopInvokeWin32Callout](../../page/91/PopInvokeWin32Callout_function_009125F4.md) at `0x00912680`
- [PopInvokeWin32Callout](../../page/91/PopInvokeWin32Callout_function_009125F4.md) at `0x009126FB`
- [PopInvokeWin32CalloutWithWatchdog](../../page/91/PopInvokeWin32CalloutWithWatchdog_function_00913920.md) at `0x009139B0`
- [PopInvokeWin32CalloutWithWatchdog](../../page/91/PopInvokeWin32CalloutWithWatchdog_function_00913920.md) at `0x00913A35`
- [PopNotifyConsoleUserPresent](../../page/91/PopNotifyConsoleUserPresent_function_00913C50.md) at `0x00913D64`
- [PopNotifyConsoleUserPresent](../../page/91/PopNotifyConsoleUserPresent_function_00913C50.md) at `0x00913DD1`
- [PopDisarmIdlePhaseWatchdog](../../page/91/PopDisarmIdlePhaseWatchdog_function_00914408.md) at `0x0091444F`
- [PopArmIdlePhaseWatchdog](../../page/98/PopArmIdlePhaseWatchdog_function_0098A10C.md) at `0x0098A20D`
- [PopPowerAggregatorNotifyCsStateExited](../../page/98/PopPowerAggregatorNotifyCsStateExited_function_0098A434.md) at `0x0098A563`
- [PopPowerAggregatorNotifyCsStateExited](../../page/98/PopPowerAggregatorNotifyCsStateExited_function_0098A434.md) at `0x0098A5CE`
- [RtlpGetSetBootStatusData](../../page/A4/RtlpGetSetBootStatusData_function_00A4CD64.md) at `0x00A4CECA`
- [RtlSetSystemBootStatus](../../page/A8/RtlSetSystemBootStatus_function_00A83230.md) at `0x00A8327E`
- [RtlpSystemBootStatusRequest](../../page/A8/RtlpSystemBootStatusRequest_function_00A8B384.md) at `0x00A8B3D3`
- [RtlpRecordBootStatusData](../../page/A8/RtlpRecordBootStatusData_function_00A8F57C.md) at `0x00A8F5B9`
- [PnpPowerStateTransitionWatchdogPushRecord](../../page/A9/PnpPowerStateTransitionWatchdogPushRecord_function_00A95CCC.md) at `0x00A95D27`
- [PnpPowerStateTransitionWatchdogPopRecord](../../page/AD/PnpPowerStateTransitionWatchdogPopRecord_function_00AD19E4.md) at `0x00AD1A24`
- [PopCreateIdlePhaseWatchdog](../../init/C4/PopCreateIdlePhaseWatchdog_function_00C42D20.md) at `0x00C42D65`

### Static image references
- `0x006ADCBC` → RVA `0x006B3460` (`KiServiceLinkage`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006ADCC9` → [KiServiceInternal](../6C/KiServiceInternal_function_006C49C0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006ADCB0  48 8B C4                        mov rax, rsp
006ADCB3  FA                              cli
006ADCB4  48 83 EC 10                     sub rsp, 0x10
006ADCB8  50                              push rax
006ADCB9  9C                              pushfq
006ADCBA  6A 10                           push 0x10
006ADCBC  48 8D 05 9D 57 00 00            lea rax, [rip + 0x579d]
006ADCC3  50                              push rax
006ADCC4  B8 5F 00 00 00                  mov eax, 0x5f
006ADCC9  E9 F2 6C 01 00                  jmp 0x1406c49c0
006ADCCE  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ZwPowerInformation(void)
{
    __int64 v_rsp;

    v_rsp = (v_rsp) - (16);
}
```

## 5. (Beta) C Style

```c
void ZwPowerInformation(void)
{
    int64_t local_rsp;

    local_rsp = (local_rsp) - (16);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006ADCB0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006ADCB0[BB_006ADCB0]
  bb_006ADCCE[BB_006ADCCE]
```
