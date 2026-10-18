# MiGetCombineDomain

- RVA: `0x00465790`–`0x004657A2` (길이 `18` bytes)
- VA: `0x0000000140465790`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `8`개 명령, `18/18` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [MiSharePages](../31/MiSharePages_function_00315110.md) at `0x00315EFB`
- [MiCapturePfnVm](MiCapturePfnVm_function_00465570.md) at `0x004656C3`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00465790  83 F9 01                        cmp ecx, 1
00465793  75 09                           jne 0x14046579e
00465795  48 8B 82 60 03 00 00            mov rax, qword ptr [rdx + 0x360]
0046579C  C3                              ret
0046579D  CC                              int3
0046579E  33 C0                           xor eax, eax
004657A0  C3                              ret
004657A1  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiGetCombineDomain(int a1, __int64 a2)
{
    __int64 result;

    if (a1 != 1) goto loc_0046579E;
    return *(unsigned __int64 *)(a2 + 864);
loc_0046579E:
    result = 0;
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiGetCombineDomain(int32_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;

    if (Arg1 != 1) goto loc_0046579E;
    return *(uint64_t *)(arg2 + 0x360);
loc_0046579E:
    result = 0;
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x360` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00465790&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00465790[BB_00465790]
  bb_00465795[BB_00465795]
  bb_0046579D[BB_0046579D]
  bb_0046579E[BB_0046579E]
  bb_004657A1[BB_004657A1]
  bb_00465790 -->|branch| bb_0046579E
  bb_00465790 -->|fallthrough| bb_00465795
  bb_0046579D -->|flow| bb_0046579E
```
