# wil_details_ReevaluateOnFeatureConfigurationChange

- RVA: `0x007E6030`–`0x007E6044` (길이 `20` bytes)
- VA: `0x00000001407E6030`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `6`개 명령, `20/20` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x007E6034` → [wil_details_UpdateFeatureConfiguredStates](../AB/wil_details_UpdateFeatureConfiguredStates_function_00ABD258.md) (function, `0x00ABD258`)
- `0x007E6039` → [wil_details_EvaluateFeatureDependencies](../70/wil_details_EvaluateFeatureDependencies_function_0070282C.md) (function, `0x0070282C`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007E6030  48 83 EC 28                     sub rsp, 0x28
007E6034  E8 1F 72 2D 00                  call 0x140abd258
007E6039  E8 EE C7 F1 FF                  call 0x14070282c
007E603E  48 83 C4 28                     add rsp, 0x28
007E6042  C3                              ret
007E6043  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall wil_details_ReevaluateOnFeatureConfigurationChange(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = wil_details_UpdateFeatureConfiguredStates(a1, a2, a3, a4);
    result = wil_details_EvaluateFeatureDependencies(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void wil_details_ReevaluateOnFeatureConfigurationChange(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = wil_details_UpdateFeatureConfiguredStates(a1, a2, a3, a4);
    result = wil_details_EvaluateFeatureDependencies(a1, a2, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007E6030&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007E6030[BB_007E6030]
  bb_007E6043[BB_007E6043]
```
