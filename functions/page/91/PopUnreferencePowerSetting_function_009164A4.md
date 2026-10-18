# PopUnreferencePowerSetting

- RVA: `0x009164A4`–`0x009164BD` (길이 `25` bytes)
- VA: `0x00000001409164A4`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `8`개 명령, `25/25` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x009164B2` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [PopFreeRegistration](../75/PopFreeRegistration_function_0075C484.md) at `0x0075C4A7`
- [PopSetPowerSettingValue](PopSetPowerSettingValue_function_00914E54.md) at `0x009150A9`
- [PopCallPowerSettingCallback](PopCallPowerSettingCallback_function_009162CC.md) at `0x009163C1`
- [PopMarshalSettingValues](PopMarshalSettingValues_function_009165A8.md) at `0x009166CA`
- [PopMarshalSettingValues$fin$0](../B0/PopMarshalSettingValues_fin_0_function_00B0F5DA.md) at `0x00B0F5FC`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x009164B2` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009164A4  48 83 EC 28                     sub rsp, 0x28
009164A8  83 01 FF                        add dword ptr [rcx], -1
009164AB  75 0A                           jne 0x1409164b7
009164AD  BA 50 53 65 74                  mov edx, 0x74655350
009164B2  E8 B9 C3 26 00                  call 0x140b82870
009164B7  48 83 C4 28                     add rsp, 0x28
009164BB  C3                              ret
009164BC  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopUnreferencePowerSetting(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (!(condition_is_not_equal)) {
        a2 = 0x74655350ULL;
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopUnreferencePowerSetting(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (!(condition_is_not_equal)) {
        a2 = 0x74655350ULL;
        result = ExFreePoolWithTag(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009164A4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_009164A4[BB_009164A4]
  bb_009164AD[BB_009164AD]
  bb_009164B7[BB_009164B7]
  bb_009164BC[BB_009164BC]
  bb_009164A4 -->|branch| bb_009164B7
  bb_009164A4 -->|fallthrough| bb_009164AD
  bb_009164AD -->|flow| bb_009164B7
```
