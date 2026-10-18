# PnpCompareActivationThread

- RVA: `0x004BE670`–`0x004BE688` (길이 `24` bytes)
- VA: `0x00000001404BE670`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `11`개 명령, `24/24` bytes 표시
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
004BE670  48 8B 42 08                     mov rax, qword ptr [rdx + 8]
004BE674  49 8B 48 08                     mov rcx, qword ptr [r8 + 8]
004BE678  48 3B C8                        cmp rcx, rax
004BE67B  77 07                           ja 0x1404be684
004BE67D  1B C0                           sbb eax, eax
004BE67F  83 C0 02                        add eax, 2
004BE682  C3                              ret
004BE683  CC                              int3
004BE684  33 C0                           xor eax, eax
004BE686  C3                              ret
004BE687  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PnpCompareActivationThread(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;

    if ((*(unsigned __int64 *)(a3 + 8)) > (*(unsigned __int64 *)(a2 + 8))) goto loc_004BE684;
    result = (unsigned int)((*(unsigned __int64 *)(a2 + 8)) + (2));
    return result;
loc_004BE684:
    result = 0;
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PnpCompareActivationThread(int64_t Arg1, void *Arg2, void *Arg3)
{
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;

    if ((*(uint64_t *)(arg3 + 0x8)) > (*(uint64_t *)(arg2 + 0x8))) goto loc_004BE684;
    result = (uint32_t)((*(uint64_t *)(arg2 + 0x8)) + (2));
    return result;
loc_004BE684:
    result = 0;
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x8` | `64` | `R` |
| `Arg3` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004BE670&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004BE670[BB_004BE670]
  bb_004BE67D[BB_004BE67D]
  bb_004BE683[BB_004BE683]
  bb_004BE684[BB_004BE684]
  bb_004BE687[BB_004BE687]
  bb_004BE670 -->|branch| bb_004BE684
  bb_004BE670 -->|fallthrough| bb_004BE67D
  bb_004BE683 -->|flow| bb_004BE684
```
