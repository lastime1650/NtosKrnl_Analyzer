# MiSetStandbyLookasideState

- RVA: `0x0041D620`–`0x0041D672` (길이 `82` bytes)
- VA: `0x000000014041D620`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `22`개 명령, `82/82` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [MiReplaceTransitionPage](../2B/MiReplaceTransitionPage_function_002B1120.md) at `0x002B1A46`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0041D620  48 8D 0C 49                     lea rcx, [rcx + rcx*2]
0041D624  48 C1 E1 04                     shl rcx, 4
0041D628  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
0041D632  48 03 C8                        add rcx, rax
0041D635  44 8B CA                        mov r9d, edx
0041D638  4C 8B 41 10                     mov r8, qword ptr [rcx + 0x10]
0041D63C  49 0F BA E0 0A                  bt r8, 0xa
0041D641  73 1B                           jae 0x14041d65e
0041D643  4A 8D 14 CD 00 00 00 00         lea rdx, [r9*8]
0041D64B  48 8B C2                        mov rax, rdx
0041D64E  49 33 C0                        xor rax, r8
0041D651  48 83 E0 F7                     and rax, 0xfffffffffffffff7
0041D655  48 33 C2                        xor rax, rdx
0041D658  48 89 41 10                     mov qword ptr [rcx + 0x10], rax
0041D65C  C3                              ret
0041D65D  CC                              int3
0041D65E  49 C1 E1 1B                     shl r9, 0x1b
0041D662  49 8B C1                        mov rax, r9
0041D665  49 33 C0                        xor rax, r8
0041D668  48 0F BA F0 1B                  btr rax, 0x1b
0041D66D  49 33 C1                        xor rax, r9
0041D670  EB E6                           jmp 0x14041d658
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiSetStandbyLookasideState(__int64 a1, int a2)
{
    __int64 result;

    a1 = (a1 + a1 * 2) << (4);
    a1 = (a1) + (result);
    if (condition_is_above_or_equal) goto loc_0041D65E;
    result = ((unsigned int)(a2) * 8) ^ (*(unsigned __int64 *)(a1 + 16));
    result = (result) & (-9);
    result = (result) ^ ((unsigned int)(a2) * 8);
loc_0041D658:
    *(unsigned __int64 *)(a1 + 16) = result;
    return result;
loc_0041D65E:
    a4 = ((unsigned int)(a2)) << (27);
    result = (a4) ^ (*(unsigned __int64 *)(a1 + 16));
    result = (result) ^ (a4);
    goto loc_0041D658;
}
```

## 5. (Beta) C Style

```c
int64_t MiSetStandbyLookasideState(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    Arg1 = (Arg1 + Arg1 * 2) << (4);
    Arg1 = (Arg1) + (result);
    if (condition_is_above_or_equal) goto loc_0041D65E;
    result = ((uint32_t)(Arg2) * 8) ^ (*(uint64_t *)(arg1 + 0x10));
    result = (result) & (-9);
    result = (result) ^ ((uint32_t)(Arg2) * 8);
loc_0041D658:
    *(uint64_t *)(arg1 + 0x10) = result;
    return result;
loc_0041D65E:
    a4 = ((uint32_t)(Arg2)) << (27);
    result = (a4) ^ (*(uint64_t *)(arg1 + 0x10));
    result = (result) ^ (a4);
    goto loc_0041D658;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0 + rcx*2` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0041D620&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0041D620[BB_0041D620]
  bb_0041D643[BB_0041D643]
  bb_0041D658[BB_0041D658]
  bb_0041D65D[BB_0041D65D]
  bb_0041D65E[BB_0041D65E]
  bb_0041D620 -->|branch| bb_0041D65E
  bb_0041D620 -->|fallthrough| bb_0041D643
  bb_0041D643 -->|flow| bb_0041D658
  bb_0041D65D -->|flow| bb_0041D65E
  bb_0041D65E -->|branch| bb_0041D658
```
