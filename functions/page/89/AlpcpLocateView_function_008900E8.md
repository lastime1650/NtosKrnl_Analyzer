# AlpcpLocateView

- RVA: `0x008900E8`–`0x00890103` (길이 `27` bytes)
- VA: `0x00000001408900E8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `11`개 명령, `27/27` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [AlpcpExposeViewAttributeInSenderContext](../88/AlpcpExposeViewAttributeInSenderContext_function_0088F600.md) at `0x0088F656`
- [AlpcpQueryRemoteView](../A4/AlpcpQueryRemoteView_function_00A49744.md) at `0x00A497FF`
- [sub_00B19294](../B1/Unknown_function_00B19294.md) at `0x00B192C2`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008900E8  48 83 C1 38                     add rcx, 0x38
008900EC  48 8B 01                        mov rax, qword ptr [rcx]
008900EF  48 3B C1                        cmp rax, rcx
008900F2  75 04                           jne 0x1408900f8
008900F4  33 C0                           xor eax, eax
008900F6  C3                              ret
008900F7  CC                              int3
008900F8  48 39 50 18                     cmp qword ptr [rax + 0x18], rdx
008900FC  74 F8                           je 0x1408900f6
008900FE  48 8B 00                        mov rax, qword ptr [rax]
00890101  EB EC                           jmp 0x1408900ef
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall AlpcpLocateView(__int64 a1, __int64 a2)
{
    __int64 result;

    a1 = (a1) + (56);
loc_008900EF:
    if ((*(unsigned __int64 *)(a1)) != a1) goto loc_008900F8;
    result = 0;
loc_008900F6:
    return result;
loc_008900F8:
    if ((*(unsigned __int64 *)(result + 24)) == a2) goto loc_008900F6;
    goto loc_008900EF;
}
```

## 5. (Beta) C Style

```c
int64_t AlpcpLocateView(void *Arg1, int64_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    Arg1 = (Arg1) + (56);
loc_008900EF:
    if ((*(uint64_t *)(arg1)) != Arg1) goto loc_008900F8;
    result = 0;
loc_008900F6:
    return result;
loc_008900F8:
    if ((*(uint64_t *)(result + 0x18)) == Arg2) goto loc_008900F6;
    goto loc_008900EF;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008900E8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_008900E8[BB_008900E8]
  bb_008900EF[BB_008900EF]
  bb_008900F4[BB_008900F4]
  bb_008900F6[BB_008900F6]
  bb_008900F7[BB_008900F7]
  bb_008900F8[BB_008900F8]
  bb_008900FE[BB_008900FE]
  bb_008900E8 -->|flow| bb_008900EF
  bb_008900EF -->|branch| bb_008900F8
  bb_008900EF -->|fallthrough| bb_008900F4
  bb_008900F4 -->|flow| bb_008900F6
  bb_008900F7 -->|flow| bb_008900F8
  bb_008900F8 -->|branch| bb_008900F6
  bb_008900F8 -->|fallthrough| bb_008900FE
  bb_008900FE -->|branch| bb_008900EF
```
