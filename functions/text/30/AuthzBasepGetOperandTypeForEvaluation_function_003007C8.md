# AuthzBasepGetOperandTypeForEvaluation

- RVA: `0x003007C8`–`0x003007D9` (길이 `17` bytes)
- VA: `0x00000001403007C8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `8`개 명령, `17/17` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [AuthzBasepEvaluateExpression](AuthzBasepEvaluateExpression_function_00300578.md) at `0x003005A4`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003007C8  83 79 0C 01                     cmp dword ptr [rcx + 0xc], 1
003007CC  74 05                           je 0x1403007d3
003007CE  0F B7 01                        movzx eax, word ptr [rcx]
003007D1  C3                              ret
003007D2  CC                              int3
003007D3  0F B7 41 28                     movzx eax, word ptr [rcx + 0x28]
003007D7  C3                              ret
003007D8  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall AuthzBasepGetOperandTypeForEvaluation(__int64 a1)
{
    if ((*(unsigned int *)(a1 + 12)) == 1) goto loc_003007D3;
    return *(unsigned __int16 *)(a1);
loc_003007D3:
    return *(unsigned __int16 *)(a1 + 40);
}
```

## 5. (Beta) C Style

```c
int64_t AuthzBasepGetOperandTypeForEvaluation(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    if ((*(uint32_t *)(arg1 + 0xC)) == 1) goto loc_003007D3;
    return *(uint16_t *)(arg1);
loc_003007D3:
    return *(uint16_t *)(arg1 + 0x28);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `16` | `R` |
| `Arg1` | `+ 0xC` | `32` | `R` |
| `Arg1` | `+ 0x28` | `16` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003007C8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003007C8[BB_003007C8]
  bb_003007CE[BB_003007CE]
  bb_003007D2[BB_003007D2]
  bb_003007D3[BB_003007D3]
  bb_003007D8[BB_003007D8]
  bb_003007C8 -->|branch| bb_003007D3
  bb_003007C8 -->|fallthrough| bb_003007CE
  bb_003007D2 -->|flow| bb_003007D3
```
