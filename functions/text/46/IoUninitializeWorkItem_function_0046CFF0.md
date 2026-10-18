# IoUninitializeWorkItem

- RVA: `0x0046CFF0`–`0x0046D01D` (길이 `45` bytes)
- VA: `0x000000014046CFF0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A82A0`
- 디코드: `13`개 명령, `45/45` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0046D017` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0046CFF0  48 83 EC 38                     sub rsp, 0x38
0046CFF4  48 83 39 00                     cmp qword ptr [rcx], 0
0046CFF8  75 06                           jne 0x14046d000
0046CFFA  48 83 C4 38                     add rsp, 0x38
0046CFFE  C3                              ret
0046CFFF  CC                              int3
0046D000  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
0046D006  4C 8D 49 20                     lea r9, [rcx + 0x20]
0046D00A  4C 8B C1                        mov r8, rcx
0046D00D  BA 02 00 00 00                  mov edx, 2
0046D012  B9 E4 00 00 00                  mov ecx, 0xe4
0046D017  E8 44 06 09 00                  call 0x1404fd660
0046D01C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IoUninitializeWorkItem(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p20;

    v_rsp = (v_rsp) - (56);
    if ((*(unsigned __int64 *)(a1)) != 0) goto loc_0046D000;
    v_rsp = (v_rsp) + (56);
    return result;
loc_0046D000:
    result = KeBugCheckEx(228, 2, a1, a1 + 32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t IoUninitializeWorkItem(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p20;

    local_rsp = (local_rsp) - (56);
    if ((*(uint64_t *)(arg1)) != 0) goto loc_0046D000;
    local_rsp = (local_rsp) + (56);
    return result;
loc_0046D000:
    result = KeBugCheckEx(228, 2, Arg1, Arg1 + 32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0046CFF0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0046CFF0[BB_0046CFF0]
  bb_0046CFFA[BB_0046CFFA]
  bb_0046CFFF[BB_0046CFFF]
  bb_0046D000[BB_0046D000]
  bb_0046CFF0 -->|branch| bb_0046D000
  bb_0046CFF0 -->|fallthrough| bb_0046CFFA
  bb_0046CFFF -->|flow| bb_0046D000
```
