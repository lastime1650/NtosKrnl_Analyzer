# VmpDereferencePinInProgress

- RVA: `0x0064C7C4`–`0x0064C7DC` (길이 `24` bytes)
- VA: `0x000000014064C7C4`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `8`개 명령, `24/24` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0064C7D1` → [VmpVaRangeCheckPinnedGpaRanges](VmpVaRangeCheckPinnedGpaRanges_function_0064D8AC.md) (function, `0x0064D8AC`)

### Direct callers
- [VmpPinMemoryRange](VmpPinMemoryRange_function_0064CCD0.md) at `0x0064D0F3`
- [VmpUnpinMemoryRangeHelper](VmpUnpinMemoryRangeHelper_function_0064D370.md) at `0x0064D52D`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0064C7C4  48 83 EC 28                     sub rsp, 0x28
0064C7C8  33 C0                           xor eax, eax
0064C7CA  48 83 69 40 01                  sub qword ptr [rcx + 0x40], 1
0064C7CF  75 05                           jne 0x14064c7d6
0064C7D1  E8 D6 10 00 00                  call 0x14064d8ac
0064C7D6  48 83 C4 28                     add rsp, 0x28
0064C7DA  C3                              ret
0064C7DB  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VmpDereferencePinInProgress(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = 0;
    if (!(condition_is_not_equal)) {
        result = VmpVaRangeCheckPinnedGpaRanges(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t VmpDereferencePinInProgress(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = 0;
    if (!(condition_is_not_equal)) {
        result = VmpVaRangeCheckPinnedGpaRanges(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x40` | `64` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0064C7C4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0064C7C4[BB_0064C7C4]
  bb_0064C7D1[BB_0064C7D1]
  bb_0064C7D6[BB_0064C7D6]
  bb_0064C7DB[BB_0064C7DB]
  bb_0064C7C4 -->|branch| bb_0064C7D6
  bb_0064C7C4 -->|fallthrough| bb_0064C7D1
  bb_0064C7D1 -->|flow| bb_0064C7D6
```
