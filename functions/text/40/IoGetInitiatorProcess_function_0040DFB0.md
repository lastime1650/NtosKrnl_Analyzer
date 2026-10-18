# IoGetInitiatorProcess

- RVA: `0x0040DFB0`–`0x0040DFCF` (길이 `31` bytes)
- VA: `0x000000014040DFB0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `12`개 명령, `31/31` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [IoIsInitiator32bitProcess](IoIsInitiator32bitProcess_function_0040DF40.md) at `0x0040DF54`
- [IopCheckInitiatorHint](../45/IopCheckInitiatorHint_function_00457134.md) at `0x00457228`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0040DFB0  48 8B 81 D0 00 00 00            mov rax, qword ptr [rcx + 0xd0]
0040DFB7  48 85 C0                        test rax, rax
0040DFBA  74 09                           je 0x14040dfc5
0040DFBC  48 8B 40 10                     mov rax, qword ptr [rax + 0x10]
0040DFC0  48 85 C0                        test rax, rax
0040DFC3  75 04                           jne 0x14040dfc9
0040DFC5  33 C0                           xor eax, eax
0040DFC7  C3                              ret
0040DFC8  CC                              int3
0040DFC9  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0040DFCD  C3                              ret
0040DFCE  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IoGetInitiatorProcess(__int64 a1)
{
    __int64 result;

    if (*(unsigned __int64 *)(a1 + 208) == 0) goto loc_0040DFC5;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 208) + 16) != 0) goto loc_0040DFC9;
loc_0040DFC5:
    result = 0;
    return result;
loc_0040DFC9:
    return *(unsigned __int64 *)(result + 8);
}
```

## 5. (Beta) C Style

```c
int64_t IoGetInitiatorProcess(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    if (*(uint64_t *)(arg1 + 0xD0) == 0) goto loc_0040DFC5;
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0xD0) + 0x10) != 0) goto loc_0040DFC9;
loc_0040DFC5:
    result = 0;
    return result;
loc_0040DFC9:
    return *(uint64_t *)(result + 0x8);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xD0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0040DFB0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0040DFB0[BB_0040DFB0]
  bb_0040DFBC[BB_0040DFBC]
  bb_0040DFC5[BB_0040DFC5]
  bb_0040DFC8[BB_0040DFC8]
  bb_0040DFC9[BB_0040DFC9]
  bb_0040DFCE[BB_0040DFCE]
  bb_0040DFB0 -->|branch| bb_0040DFC5
  bb_0040DFB0 -->|fallthrough| bb_0040DFBC
  bb_0040DFBC -->|branch| bb_0040DFC9
  bb_0040DFBC -->|fallthrough| bb_0040DFC5
  bb_0040DFC8 -->|flow| bb_0040DFC9
```
