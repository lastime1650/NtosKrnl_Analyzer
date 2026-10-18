# KeQueryGroupAffinityEx

- RVA: `0x0040DB00`–`0x0040DB13` (길이 `19` bytes)
- VA: `0x000000014040DB00`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `9`개 명령, `19/19` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0040DB00  66 3B 11                        cmp dx, word ptr [rcx]
0040DB03  73 0A                           jae 0x14040db0f
0040DB05  0F B7 C2                        movzx eax, dx
0040DB08  48 8B 44 C1 08                  mov rax, qword ptr [rcx + rax*8 + 8]
0040DB0D  C3                              ret
0040DB0E  CC                              int3
0040DB0F  33 C0                           xor eax, eax
0040DB11  C3                              ret
0040DB12  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KeQueryGroupAffinityEx(__int64 a1, unsigned __int16 a2)
{
    __int64 result;

    if (a2 >= (*(unsigned __int16 *)(a1))) goto loc_0040DB0F;
    return *(unsigned __int64 *)(a1 + a2 * 8 + 8);
loc_0040DB0F:
    result = 0;
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KeQueryGroupAffinityEx(void *Arg1, uint16_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    if (Arg2 >= (*(uint16_t *)(arg1))) goto loc_0040DB0F;
    return *(uint64_t *)(arg1 + Arg2 * 8 + 0x8);
loc_0040DB0F:
    result = 0;
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `16` | `R` |
| `Arg1` | `+ 0x8 + rax*8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0040DB00&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0040DB00[BB_0040DB00]
  bb_0040DB05[BB_0040DB05]
  bb_0040DB0E[BB_0040DB0E]
  bb_0040DB0F[BB_0040DB0F]
  bb_0040DB12[BB_0040DB12]
  bb_0040DB00 -->|branch| bb_0040DB0F
  bb_0040DB00 -->|fallthrough| bb_0040DB05
  bb_0040DB0E -->|flow| bb_0040DB0F
```
