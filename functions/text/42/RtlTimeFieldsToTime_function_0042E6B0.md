# RtlTimeFieldsToTime

- RVA: `0x0042E6B0`–`0x0042E6BF` (길이 `15` bytes)
- VA: `0x000000014042E6B0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `5`개 명령, `15/15` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **11**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0042E6B4` → [RtlpTimeFieldsToTime](RtlpTimeFieldsToTime_function_0042E6C8.md) (function, `0x0042E6C8`)

### Direct callers
- [HalpAcpiRealTimeToUtcTime](../../page/70/HalpAcpiRealTimeToUtcTime_function_007065D8.md) at `0x0070663E`
- [PiDevCfgSplitDriverConfigurationId](../../page/73/PiDevCfgSplitDriverConfigurationId_function_00736568.md) at `0x0073672F`
- [RtlCutoverTimeToSystemTime](../../page/78/RtlCutoverTimeToSystemTime_function_0078B110.md) at `0x0078B157`
- [RtlCutoverTimeToSystemTime](../../page/78/RtlCutoverTimeToSystemTime_function_0078B110.md) at `0x0078B1E5`
- [RtlCutoverTimeToSystemTime](../../page/78/RtlCutoverTimeToSystemTime_function_0078B110.md) at `0x0078B23F`
- [RtlCutoverTimeToSystemTime](../../page/78/RtlCutoverTimeToSystemTime_function_0078B110.md) at `0x0078B270`
- [ExpRefreshSystemTime](../../page/7C/ExpRefreshSystemTime_function_007C6264.md) at `0x007C62BA`
- [NtSetSystemTime](../../page/7C/NtSetSystemTime_function_007C65F0.md) at `0x007C67C2`
- [ExGetExpirationDate](../../page/7C/ExGetExpirationDate_function_007C78C8.md) at `0x007C79F1`
- [I_MinAsn1AdjustFileTime](../../page/83/I_MinAsn1AdjustFileTime_function_008396A4.md) at `0x00839774`
- [I_MinAsn1ConvertTime](../../page/83/I_MinAsn1ConvertTime_function_008398A8.md) at `0x00839910`
- [ExpRefreshTimeZoneInformation](../../page/A6/ExpRefreshTimeZoneInformation_function_00A6B46C.md) at `0x00A6B9CA`
- [ExpRefreshTimeZoneInformation](../../page/A6/ExpRefreshTimeZoneInformation_function_00A6B46C.md) at `0x00A6BA17`
- [ExUpdateSystemTimeFromCmos](../../pagelk/B7/ExUpdateSystemTimeFromCmos_function_00B7BD98.md) at `0x00B7BE10`
- [HaliSetWakeAlarm](../../pagelk/B7/HaliSetWakeAlarm_function_00B7D300.md) at `0x00B7D3A2`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0042E6B0  48 83 EC 28                     sub rsp, 0x28
0042E6B4  E8 0F 00 00 00                  call 0x14042e6c8
0042E6B9  48 83 C4 28                     add rsp, 0x28
0042E6BD  C3                              ret
0042E6BE  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlTimeFieldsToTime(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = RtlpTimeFieldsToTime(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void RtlTimeFieldsToTime(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = RtlpTimeFieldsToTime(a1, a2, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0042E6B0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0042E6B0[BB_0042E6B0]
  bb_0042E6BE[BB_0042E6BE]
```
