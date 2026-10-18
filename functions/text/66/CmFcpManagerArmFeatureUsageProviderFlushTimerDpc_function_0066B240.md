# CmFcpManagerArmFeatureUsageProviderFlushTimerDpc

- RVA: `0x0066B240`–`0x0066B27A` (길이 `58` bytes)
- VA: `0x000000014066B240`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `15`개 명령, `58/58` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0066B26F` → [CmFcpManagerArmFeatureUsageProviderFlushTimer](../4F/CmFcpManagerArmFeatureUsageProviderFlushTimer_function_004FC838.md) (function, `0x004FC838`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0066B240  48 83 EC 28                     sub rsp, 0x28
0066B244  F0 83 A2 30 07 00 00 FB         lock and dword ptr [rdx + 0x730], 0xfffffffb
0066B24C  0F 0D 8A 30 07 00 00            prefetchw byte ptr [rdx + 0x730]
0066B253  8B 82 30 07 00 00               mov eax, dword ptr [rdx + 0x730]
0066B259  8B C8                           mov ecx, eax
0066B25B  83 C9 02                        or ecx, 2
0066B25E  F0 0F B1 8A 30 07 00 00         lock cmpxchg dword ptr [rdx + 0x730], ecx
0066B266  75 F1                           jne 0x14066b259
0066B268  A8 02                           test al, 2
0066B26A  75 08                           jne 0x14066b274
0066B26C  48 8B CA                        mov rcx, rdx
0066B26F  E8 C4 15 E9 FF                  call 0x1404fc838
0066B274  48 83 C4 28                     add rsp, 0x28
0066B278  C3                              ret
0066B279  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmFcpManagerArmFeatureUsageProviderFlushTimerDpc(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
loc_0066B259:
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 1840))))) | (2));
    if (condition_is_not_equal) goto loc_0066B259;
    result = (unsigned int)(*(unsigned int *)(a2 + 1840));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 1840)))) & (2)) == 0) {
        a1 = a2;
        result = CmFcpManagerArmFeatureUsageProviderFlushTimer(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CmFcpManagerArmFeatureUsageProviderFlushTimerDpc(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
loc_0066B259:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x730))))) | (2));
    if (condition_is_not_equal) goto loc_0066B259;
    result = (uint32_t)(*(uint32_t *)(arg2 + 0x730));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg2 + 0x730)))) & (2)) == 0) {
        Arg1 = Arg2;
        result = CmFcpManagerArmFeatureUsageProviderFlushTimer(Arg1, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x730` | `8` | `R` |
| `Arg2` | `+ 0x730` | `32` | `R` |
| `Arg2` | `+ 0x730` | `32` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0066B240&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0066B240[BB_0066B240]
  bb_0066B259[BB_0066B259]
  bb_0066B268[BB_0066B268]
  bb_0066B26C[BB_0066B26C]
  bb_0066B274[BB_0066B274]
  bb_0066B279[BB_0066B279]
  bb_0066B240 -->|flow| bb_0066B259
  bb_0066B259 -->|branch| bb_0066B259
  bb_0066B259 -->|fallthrough| bb_0066B268
  bb_0066B268 -->|branch| bb_0066B274
  bb_0066B268 -->|fallthrough| bb_0066B26C
  bb_0066B26C -->|flow| bb_0066B274
```
