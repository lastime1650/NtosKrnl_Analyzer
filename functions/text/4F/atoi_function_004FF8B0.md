# atoi

- RVA: `0x004FF8B0`–`0x004FF8BF` (길이 `15` bytes)
- VA: `0x00000001404FF8B0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `5`개 명령, `15/15` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004FF8B4` → [atol](atol_function_004FF8D0.md) (function, `0x004FF8D0`)

### Direct callers
- [MinAsn1DecodeGeneralizedTime](../../page/83/MinAsn1DecodeGeneralizedTime_function_00839C20.md) at `0x00839C89`
- [MinAsn1DecodeGeneralizedTime](../../page/83/MinAsn1DecodeGeneralizedTime_function_00839C20.md) at `0x00839CA5`
- [MinAsn1DecodeGeneralizedTime](../../page/83/MinAsn1DecodeGeneralizedTime_function_00839C20.md) at `0x00839CBD`
- [MinAsn1DecodeGeneralizedTime](../../page/83/MinAsn1DecodeGeneralizedTime_function_00839C20.md) at `0x00839CD5`
- [MinAsn1DecodeGeneralizedTime](../../page/83/MinAsn1DecodeGeneralizedTime_function_00839C20.md) at `0x00839D26`
- [MinAsn1DecodeUtcTime](../../page/83/MinAsn1DecodeUtcTime_function_00839ECC.md) at `0x00839F0C`
- [MinAsn1DecodeUtcTime](../../page/83/MinAsn1DecodeUtcTime_function_00839ECC.md) at `0x00839F23`
- [MinAsn1DecodeUtcTime](../../page/83/MinAsn1DecodeUtcTime_function_00839ECC.md) at `0x00839F3B`
- [MinAsn1DecodeUtcTime](../../page/83/MinAsn1DecodeUtcTime_function_00839ECC.md) at `0x00839F53`
- [MinAsn1DecodeUtcTime](../../page/83/MinAsn1DecodeUtcTime_function_00839ECC.md) at `0x00839F6B`
- [MinAsn1DecodeUtcTime](../../page/83/MinAsn1DecodeUtcTime_function_00839ECC.md) at `0x00839F9A`
- [KiInitializeBootStructures](../../pagelk/B6/KiInitializeBootStructures_function_00B68530.md) at `0x00B6886C`
- [HalpMiscGetParameters](../../init/C1/HalpMiscGetParameters_function_00C1FD30.md) at `0x00C1FE38`
- [HalpMiscGetParameters](../../init/C1/HalpMiscGetParameters_function_00C1FD30.md) at `0x00C1FE73`
- [HalpMiscGetParameters](../../init/C1/HalpMiscGetParameters_function_00C1FD30.md) at `0x00C2007B`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004FF8B0  48 83 EC 28                     sub rsp, 0x28
004FF8B4  E8 17 00 00 00                  call 0x1404ff8d0
004FF8B9  48 83 C4 28                     add rsp, 0x28
004FF8BD  C3                              ret
004FF8BE  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall atoi(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = atol(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void atoi(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = atol(a1, a2, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004FF8B0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004FF8B0[BB_004FF8B0]
  bb_004FF8BE[BB_004FF8BE]
```
