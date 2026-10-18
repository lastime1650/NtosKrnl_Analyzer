# ExpTimerSetParametersAreValid

- RVA: `0x0045B68C`–`0x0045B69F` (길이 `19` bytes)
- VA: `0x000000014045B68C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `9`개 명령, `19/19` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [RtlpHpEnvCompactionSchedule](../32/RtlpHpEnvCompactionSchedule_function_003264A0.md) at `0x0032652C`
- [EnableFlushTimer](EnableFlushTimer_function_0045B5B8.md) at `0x0045B5FE`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0045B68C  83 39 00                        cmp dword ptr [rcx], 0
0045B68F  75 0A                           jne 0x14045b69b
0045B691  48 83 79 08 FF                  cmp qword ptr [rcx + 8], -1
0045B696  0F 9D C0                        setge al
0045B699  C3                              ret
0045B69A  CC                              int3
0045B69B  32 C0                           xor al, al
0045B69D  C3                              ret
0045B69E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExpTimerSetParametersAreValid(__int64 a1)
{
    __int64 result;

    if ((*(unsigned int *)(a1)) != 0) goto loc_0045B69B;
    result = ((*(unsigned __int64 *)(a1 + 8)) >= -1) ? 1 : 0;
    return result;
loc_0045B69B:
    result = 0;
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ExpTimerSetParametersAreValid(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    if ((*(uint32_t *)(arg1)) != 0) goto loc_0045B69B;
    result = ((*(uint64_t *)(arg1 + 0x8)) >= -1) ? 1 : 0;
    return result;
loc_0045B69B:
    result = 0;
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0045B68C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0045B68C[BB_0045B68C]
  bb_0045B691[BB_0045B691]
  bb_0045B69A[BB_0045B69A]
  bb_0045B69B[BB_0045B69B]
  bb_0045B69E[BB_0045B69E]
  bb_0045B68C -->|branch| bb_0045B69B
  bb_0045B68C -->|fallthrough| bb_0045B691
  bb_0045B69A -->|flow| bb_0045B69B
```
