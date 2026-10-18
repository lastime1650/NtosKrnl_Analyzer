# VfPtComparePoolInfoCallback

- RVA: `0x00B9BF10`–`0x00B9BF26` (길이 `22` bytes)
- VA: `0x0000000140B9BF10`
- 실행 섹션: `PAGEVRFY`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `11`개 명령, `22/22` bytes 표시
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
00B9BF10  48 8B 02                        mov rax, qword ptr [rdx]
00B9BF13  49 8B 08                        mov rcx, qword ptr [r8]
00B9BF16  48 3B C8                        cmp rcx, rax
00B9BF19  76 04                           jbe 0x140b9bf1f
00B9BF1B  33 C0                           xor eax, eax
00B9BF1D  C3                              ret
00B9BF1E  CC                              int3
00B9BF1F  1B C0                           sbb eax, eax
00B9BF21  83 C0 02                        add eax, 2
00B9BF24  C3                              ret
00B9BF25  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VfPtComparePoolInfoCallback(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;

    if ((*(unsigned __int64 *)(a3)) <= (*(unsigned __int64 *)(a2))) goto loc_00B9BF1F;
    result = 0;
    return result;
loc_00B9BF1F:
    result = (unsigned int)((result) + (2));
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t VfPtComparePoolInfoCallback(int64_t Arg1, void *Arg2, void *Arg3)
{
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;

    if ((*(uint64_t *)(arg3)) <= (*(uint64_t *)(arg2))) goto loc_00B9BF1F;
    result = 0;
    return result;
loc_00B9BF1F:
    result = (uint32_t)((result) + (2));
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `64` | `R` |
| `Arg3` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagevrfy&rva=0x00B9BF10&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B9BF10[BB_00B9BF10]
  bb_00B9BF1B[BB_00B9BF1B]
  bb_00B9BF1E[BB_00B9BF1E]
  bb_00B9BF1F[BB_00B9BF1F]
  bb_00B9BF25[BB_00B9BF25]
  bb_00B9BF10 -->|branch| bb_00B9BF1F
  bb_00B9BF10 -->|fallthrough| bb_00B9BF1B
  bb_00B9BF1E -->|flow| bb_00B9BF1F
```
