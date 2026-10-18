# IoGetCopyInformationExtension

- RVA: `0x004ACA80`–`0x004ACAB5` (길이 `53` bytes)
- VA: `0x00000001404ACA80`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `17`개 명령, `53/53` bytes 표시
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
004ACA80  48 8B 81 C8 00 00 00            mov rax, qword ptr [rcx + 0xc8]
004ACA87  90                              nop
004ACA88  80 79 47 00                     cmp byte ptr [rcx + 0x47], 0
004ACA8C  7C 20                           jl 0x1404acaae
004ACA8E  48 85 C0                        test rax, rax
004ACA91  74 1B                           je 0x1404acaae
004ACA93  66 0F BA 60 02 09               bt word ptr [rax + 2], 9
004ACA99  73 13                           jae 0x1404acaae
004ACA9B  48 8B 81 C8 00 00 00            mov rax, qword ptr [rcx + 0xc8]
004ACAA2  0F 10 40 40                     movups xmm0, xmmword ptr [rax + 0x40]
004ACAA6  33 C0                           xor eax, eax
004ACAA8  F3 0F 7F 02                     movdqu xmmword ptr [rdx], xmm0
004ACAAC  C3                              ret
004ACAAD  CC                              int3
004ACAAE  B8 25 02 00 C0                  mov eax, 0xc0000225
004ACAB3  C3                              ret
004ACAB4  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IoGetCopyInformationExtension(__int64 a1, __int64 a2)
{
    __int64 result;

    if ((*(unsigned __int8 *)(a1 + 71)) < 0) goto loc_004ACAAE;
    if (*(unsigned __int64 *)(a1 + 200) == 0) goto loc_004ACAAE;
    if (condition_is_above_or_equal) goto loc_004ACAAE;
    result = 0;
    *(unsigned __int64 *)(a2) = v_xmm0;
    return result;
loc_004ACAAE:
    return (unsigned int)(0xC0000225ULL);
}
```

## 5. (Beta) C Style

```c
int64_t IoGetCopyInformationExtension(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;

    if ((*(uint8_t *)(arg1 + 0x47)) < 0) goto loc_004ACAAE;
    if (*(uint64_t *)(arg1 + 0xC8) == 0) goto loc_004ACAAE;
    if (condition_is_above_or_equal) goto loc_004ACAAE;
    result = 0;
    *(uint64_t *)(arg2) = v_xmm0;
    return result;
loc_004ACAAE:
    return (uint32_t)(0xC0000225ULL);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x47` | `8` | `R` |
| `Arg1` | `+ 0xC8` | `64` | `R` |
| `Arg2` | `+ 0x0` | `128` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004ACA80&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004ACA80[BB_004ACA80]
  bb_004ACA8E[BB_004ACA8E]
  bb_004ACA93[BB_004ACA93]
  bb_004ACA9B[BB_004ACA9B]
  bb_004ACAAD[BB_004ACAAD]
  bb_004ACAAE[BB_004ACAAE]
  bb_004ACAB4[BB_004ACAB4]
  bb_004ACA80 -->|branch| bb_004ACAAE
  bb_004ACA80 -->|fallthrough| bb_004ACA8E
  bb_004ACA8E -->|branch| bb_004ACAAE
  bb_004ACA8E -->|fallthrough| bb_004ACA93
  bb_004ACA93 -->|branch| bb_004ACAAE
  bb_004ACA93 -->|fallthrough| bb_004ACA9B
  bb_004ACAAD -->|flow| bb_004ACAAE
```
