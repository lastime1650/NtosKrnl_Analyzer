# KiIsConcurrencyCountWithinIdealProcessorSetBreakpoints

- RVA: `0x003C210C`–`0x003C211F` (길이 `19` bytes)
- VA: `0x00000001403C210C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `11`개 명령, `19/19` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [KiAdjustProcessIdealProcessorSetsForThreadCreation](KiAdjustProcessIdealProcessorSetsForThreadCreation_function_003C2710.md) at `0x003C27A7`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003C210C  8B 02                           mov eax, dword ptr [rdx]
003C210E  39 01                           cmp dword ptr [rcx], eax
003C2110  77 09                           ja 0x1403c211b
003C2112  39 41 04                        cmp dword ptr [rcx + 4], eax
003C2115  72 04                           jb 0x1403c211b
003C2117  B0 01                           mov al, 1
003C2119  C3                              ret
003C211A  CC                              int3
003C211B  33 C0                           xor eax, eax
003C211D  C3                              ret
003C211E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiIsConcurrencyCountWithinIdealProcessorSetBreakpoints(__int64 a1, __int64 a2)
{
    __int64 result;

    if ((*(unsigned int *)(a1)) > ((unsigned int)((unsigned int)(*(unsigned int *)(a2))))) goto loc_003C211B;
    if ((*(unsigned int *)(a1 + 4)) < ((unsigned int)((unsigned int)(*(unsigned int *)(a2))))) goto loc_003C211B;
    return 1;
loc_003C211B:
    result = 0;
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KiIsConcurrencyCountWithinIdealProcessorSetBreakpoints(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;

    if ((*(uint32_t *)(arg1)) > ((uint32_t)((uint32_t)(*(uint32_t *)(arg2))))) goto loc_003C211B;
    if ((*(uint32_t *)(arg1 + 0x4)) < ((uint32_t)((uint32_t)(*(uint32_t *)(arg2))))) goto loc_003C211B;
    return 1;
loc_003C211B:
    result = 0;
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x4` | `32` | `R` |
| `Arg2` | `+ 0x0` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003C210C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003C210C[BB_003C210C]
  bb_003C2112[BB_003C2112]
  bb_003C2117[BB_003C2117]
  bb_003C211A[BB_003C211A]
  bb_003C211B[BB_003C211B]
  bb_003C211E[BB_003C211E]
  bb_003C210C -->|branch| bb_003C211B
  bb_003C210C -->|fallthrough| bb_003C2112
  bb_003C2112 -->|branch| bb_003C211B
  bb_003C2112 -->|fallthrough| bb_003C2117
  bb_003C211A -->|flow| bb_003C211B
```
