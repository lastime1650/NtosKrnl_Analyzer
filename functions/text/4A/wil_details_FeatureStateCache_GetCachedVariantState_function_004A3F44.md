# wil_details_FeatureStateCache_GetCachedVariantState

- RVA: `0x004A3F44`–`0x004A3F63` (길이 `31` bytes)
- VA: `0x00000001404A3F44`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CEE8`
- 디코드: `11`개 명령, `31/31` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **7**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004A3F5C` → [wil_details_FeatureStateCache_ReevaluateCachedVariantState](../5B/wil_details_FeatureStateCache_ReevaluateCachedVariantState_function_005B867C.md) (function, `0x005B867C`)

### Direct callers
- [Feature_AntiStarvationReadyPeriodVariable__private_GetVariant](../5B/Feature_AntiStarvationReadyPeriodVariable__private_GetVariant_function_005B5FFC.md) at `0x005B6010`
- [Feature_AntiStarvationScanPeriodVariable__private_GetVariant](../5B/Feature_AntiStarvationScanPeriodVariable__private_GetVariant_function_005B603C.md) at `0x005B6050`
- [Feature_AntiStarvationThreadBoostCountVariable__private_GetVariant](../5B/Feature_AntiStarvationThreadBoostCountVariable__private_GetVariant_function_005B607C.md) at `0x005B6090`
- [Feature_AntiStarvationThreadScanCountVariable__private_GetVariant](../5B/Feature_AntiStarvationThreadScanCountVariable__private_GetVariant_function_005B60BC.md) at `0x005B60D0`
- [Feature_EffectivePriorityNotAlwaysRankBiased__private_GetVariant](../5B/Feature_EffectivePriorityNotAlwaysRankBiased__private_GetVariant_function_005B60FC.md) at `0x005B6110`
- [Feature_UnparkPCoresOnUnimportantUtility__private_GetVariant](../5D/Feature_UnparkPCoresOnUnimportantUtility__private_GetVariant_function_005D9444.md) at `0x005D9458`
- [Feature_AdaptiveHibernateEnhancements__private_GetVariant](../5D/Feature_AdaptiveHibernateEnhancements__private_GetVariant_function_005DC550.md) at `0x005DC564`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004A3F44  48 83 EC 28                     sub rsp, 0x28
004A3F48  4C 8B C2                        mov r8, rdx
004A3F4B  48 8B 11                        mov rdx, qword ptr [rcx]
004A3F4E  F6 C2 08                        test dl, 8
004A3F51  74 09                           je 0x1404a3f5c
004A3F53  48 8B C2                        mov rax, rdx
004A3F56  48 83 C4 28                     add rsp, 0x28
004A3F5A  C3                              ret
004A3F5B  CC                              int3
004A3F5C  E8 1B 47 11 00                  call 0x1405b867c
004A3F61  EB F3                           jmp 0x1404a3f56
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall wil_details_FeatureStateCache_GetCachedVariantState(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if ((((unsigned __int8)(*(unsigned __int64 *)(a1))) & (8)) == 0) goto loc_004A3F5C;
loc_004A3F56:
    v_rsp = (v_rsp) + (40);
    return *(unsigned __int64 *)(a1);
loc_004A3F5C:
    result = wil_details_FeatureStateCache_ReevaluateCachedVariantState(a1, *(unsigned __int64 *)(a1), a2, a4);
    goto loc_004A3F56;
}
```

## 5. (Beta) C Style

```c
int64_t wil_details_FeatureStateCache_GetCachedVariantState(void *Arg1, int64_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if ((((uint8_t)(*(uint64_t *)(arg1))) & (8)) == 0) goto loc_004A3F5C;
loc_004A3F56:
    local_rsp = (local_rsp) + (40);
    return *(uint64_t *)(arg1);
loc_004A3F5C:
    result = wil_details_FeatureStateCache_ReevaluateCachedVariantState(Arg1, *(uint64_t *)(arg1), Arg2, a4);
    goto loc_004A3F56;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004A3F44&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004A3F44[BB_004A3F44]
  bb_004A3F53[BB_004A3F53]
  bb_004A3F56[BB_004A3F56]
  bb_004A3F5B[BB_004A3F5B]
  bb_004A3F5C[BB_004A3F5C]
  bb_004A3F44 -->|branch| bb_004A3F5C
  bb_004A3F44 -->|fallthrough| bb_004A3F53
  bb_004A3F53 -->|flow| bb_004A3F56
  bb_004A3F5B -->|flow| bb_004A3F5C
  bb_004A3F5C -->|branch| bb_004A3F56
```
