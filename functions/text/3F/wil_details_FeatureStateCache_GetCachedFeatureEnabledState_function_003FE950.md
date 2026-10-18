# wil_details_FeatureStateCache_GetCachedFeatureEnabledState

- RVA: `0x003FE950`–`0x003FE981` (길이 `49` bytes)
- VA: `0x00000001403FE950`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005D35C`
- 디코드: `14`개 명령, `49/49` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x003FE97A` → [wil_details_FeatureStateCache_ReevaluateCachedFeatureEnabledState](wil_details_FeatureStateCache_ReevaluateCachedFeatureEnabledState_function_003FE988.md) (function, `0x003FE988`)

### Direct callers
- [wil_details_AreDependenciesEnabled](../53/wil_details_AreDependenciesEnabled_function_0053E664.md) at `0x0053E696`
- [wil_details_GetCurrentVariantState](../5B/wil_details_GetCurrentVariantState_function_005B8790.md) at `0x005B8844`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003FE950  48 83 EC 28                     sub rsp, 0x28
003FE954  8B 01                           mov eax, dword ptr [rcx]
003FE956  48 C7 44 24 30 00 00 00 00      mov qword ptr [rsp + 0x30], 0
003FE95F  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
003FE963  A8 02                           test al, 2
003FE965  74 0B                           je 0x1403fe972
003FE967  48 8B 44 24 30                  mov rax, qword ptr [rsp + 0x30]
003FE96C  48 83 C4 28                     add rsp, 0x28
003FE970  C3                              ret
003FE971  CC                              int3
003FE972  4C 8B C2                        mov r8, rdx
003FE975  48 8B 54 24 30                  mov rdx, qword ptr [rsp + 0x30]
003FE97A  E8 09 00 00 00                  call 0x1403fe988
003FE97F  EB EB                           jmp 0x1403fe96c
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall wil_details_FeatureStateCache_GetCachedFeatureEnabledState(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = 0;
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(a1)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1)))) & (2)) == 0) goto loc_003FE972;
loc_003FE96C:
    v_rsp = (v_rsp) + (40);
    return v_stack_p8;
loc_003FE972:
    result = wil_details_FeatureStateCache_ReevaluateCachedFeatureEnabledState(a1, v_stack_p30, a2, a4);
    goto loc_003FE96C;
}
```

## 5. (Beta) C Style

```c
int64_t wil_details_FeatureStateCache_GetCachedFeatureEnabledState(void *Arg1, int64_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p30;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = 0;
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1)))) & (2)) == 0) goto loc_003FE972;
loc_003FE96C:
    local_rsp = (local_rsp) + (40);
    return v_stack_p8;
loc_003FE972:
    result = wil_details_FeatureStateCache_ReevaluateCachedFeatureEnabledState(Arg1, v_stack_p30, Arg2, a4);
    goto loc_003FE96C;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003FE950&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003FE950[BB_003FE950]
  bb_003FE967[BB_003FE967]
  bb_003FE96C[BB_003FE96C]
  bb_003FE971[BB_003FE971]
  bb_003FE972[BB_003FE972]
  bb_003FE950 -->|branch| bb_003FE972
  bb_003FE950 -->|fallthrough| bb_003FE967
  bb_003FE967 -->|flow| bb_003FE96C
  bb_003FE971 -->|flow| bb_003FE972
  bb_003FE972 -->|branch| bb_003FE96C
```
