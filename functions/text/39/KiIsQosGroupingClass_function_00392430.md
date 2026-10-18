# KiIsQosGroupingClass

- RVA: `0x00392430`–`0x00392442` (길이 `18` bytes)
- VA: `0x0000000140392430`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `9`개 명령, `18/18` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [sub_0025308F](../25/Unknown_function_0025308F.md) at `0x00253A0D`
- [PpmPerfArbitratorApplyProcessorState](PpmPerfArbitratorApplyProcessorState_function_00391E00.md) at `0x00392188`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00392430  8D 41 FF                        lea eax, [rcx - 1]
00392433  A9 FA FF FF FF                  test eax, 0xfffffffa
00392438  75 04                           jne 0x14039243e
0039243A  B0 01                           mov al, 1
0039243C  C3                              ret
0039243D  CC                              int3
0039243E  32 C0                           xor al, al
00392440  C3                              ret
00392441  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiIsQosGroupingClass(__int64 a1)
{
    __int64 result;

    if ((((unsigned int)(a1 - 1)) & (0xFFFFFFFAULL)) != 0) goto loc_0039243E;
    return 1;
loc_0039243E:
    result = 0;
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KiIsQosGroupingClass(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    if ((((uint32_t)(Arg1 - 1)) & (0xFFFFFFFAULL)) != 0) goto loc_0039243E;
    return 1;
loc_0039243E:
    result = 0;
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `- 0x1` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00392430&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00392430[BB_00392430]
  bb_0039243A[BB_0039243A]
  bb_0039243D[BB_0039243D]
  bb_0039243E[BB_0039243E]
  bb_00392441[BB_00392441]
  bb_00392430 -->|branch| bb_0039243E
  bb_00392430 -->|fallthrough| bb_0039243A
  bb_0039243D -->|flow| bb_0039243E
```
