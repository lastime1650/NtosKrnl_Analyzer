# CmpGetComponentNameAtIndex

- RVA: `0x009A7A50`–`0x009A7A7A` (길이 `42` bytes)
- VA: `0x00000001409A7A50`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `15`개 명령, `42/42` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [CmpPerformCompleteKcbCacheLookup](../84/CmpPerformCompleteKcbCacheLookup_function_0084FD20.md) at `0x00850C08`
- [CmpGetSymbolicLinkTarget](../85/CmpGetSymbolicLinkTarget_function_008570A0.md) at `0x0085781D`
- [sub_00857CAB](../85/Unknown_function_00857CAB.md) at `0x00857CD6`
- [CmpDoParseKey](../85/CmpDoParseKey_function_0085F750.md) at `0x0086026D`
- [CmpDoParseKey](../85/CmpDoParseKey_function_0085F750.md) at `0x008602A6`
- [CmpDoParseKey](../85/CmpDoParseKey_function_0085F750.md) at `0x00860C30`
- [CmpDoParseKey](../85/CmpDoParseKey_function_0085F750.md) at `0x00861155`
- [CmpDoParseKey](../85/CmpDoParseKey_function_0085F750.md) at `0x008611B9`
- [CmpDoParseKey](../85/CmpDoParseKey_function_0085F750.md) at `0x008614B6`
- [sub_00B16F66](../B1/Unknown_function_00B16F66.md) at `0x00B16FAC`
- [sub_00B16F66](../B1/Unknown_function_00B16F66.md) at `0x00B1703C`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009A7A50  83 FA 08                        cmp edx, 8
009A7A53  73 0F                           jae 0x1409a7a64
009A7A55  8B C2                           mov eax, edx
009A7A57  48 83 C0 02                     add rax, 2
009A7A5B  48 C1 E0 04                     shl rax, 4
009A7A5F  48 03 C1                        add rax, rcx
009A7A62  C3                              ret
009A7A63  CC                              int3
009A7A64  83 C2 F8                        add edx, -8
009A7A67  8B C2                           mov eax, edx
009A7A69  48 83 C0 06                     add rax, 6
009A7A6D  48 C1 E0 04                     shl rax, 4
009A7A71  48 03 81 A0 00 00 00            add rax, qword ptr [rcx + 0xa0]
009A7A78  C3                              ret
009A7A79  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpGetComponentNameAtIndex(__int64 a1, int a2)
{
    __int64 result;

    if (a2 >= 8) goto loc_009A7A64;
    result = ((unsigned int)(a2)) + (2);
    result = (result) << (4);
    result = (result) + (a1);
    return result;
loc_009A7A64:
    a2 = (unsigned int)((a2) + (-8));
    result = ((unsigned int)(a2)) + (6);
    result = (result) << (4);
    result = (result) + (*(unsigned __int64 *)(a1 + 160));
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CmpGetComponentNameAtIndex(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    if (Arg2 >= 8) goto loc_009A7A64;
    result = ((uint32_t)(Arg2)) + (2);
    result = (result) << (4);
    result = (result) + (Arg1);
    return result;
loc_009A7A64:
    Arg2 = (uint32_t)((Arg2) + (-8));
    result = ((uint32_t)(Arg2)) + (6);
    result = (result) << (4);
    result = (result) + (*(uint64_t *)(arg1 + 0xA0));
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xA0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009A7A50&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_009A7A50[BB_009A7A50]
  bb_009A7A55[BB_009A7A55]
  bb_009A7A63[BB_009A7A63]
  bb_009A7A64[BB_009A7A64]
  bb_009A7A79[BB_009A7A79]
  bb_009A7A50 -->|branch| bb_009A7A64
  bb_009A7A50 -->|fallthrough| bb_009A7A55
  bb_009A7A63 -->|flow| bb_009A7A64
```
