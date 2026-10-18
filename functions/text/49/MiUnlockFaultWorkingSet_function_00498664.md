# MiUnlockFaultWorkingSet

- RVA: `0x00498664`–`0x00498690` (길이 `44` bytes)
- VA: `0x0000000140498664`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007FBDC`
- 디코드: `15`개 명령, `44/44` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00498679` → [MiUnlockWorkingSetShared](../27/MiUnlockWorkingSetShared_function_0027D690.md) (function, `0x0027D690`)
- `0x00498685` → [MiUnlockWorkingSetExclusive](../27/MiUnlockWorkingSetExclusive_function_0027EC70.md) (function, `0x0027EC70`)

### Direct callers
- [MiCheckHoldFaultForHotPatch](../3D/MiCheckHoldFaultForHotPatch_function_003D4BA8.md) at `0x003D4C86`
- [MiCheckHoldFaultForHotPatch](../3D/MiCheckHoldFaultForHotPatch_function_003D4BA8.md) at `0x003D4CA8`
- [MiWaitForRotateToComplete](../4A/MiWaitForRotateToComplete_function_004A54F4.md) at `0x004A55AC`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00498664  40 53                           push rbx
00498666  48 83 EC 20                     sub rsp, 0x20
0049866A  48 8B D9                        mov rbx, rcx
0049866D  48 8B 09                        mov rcx, qword ptr [rcx]
00498670  F6 43 0D 01                     test byte ptr [rbx + 0xd], 1
00498674  8A 53 0C                        mov dl, byte ptr [rbx + 0xc]
00498677  75 0C                           jne 0x140498685
00498679  E8 12 50 DE FF                  call 0x14027d690
0049867E  48 83 C4 20                     add rsp, 0x20
00498682  5B                              pop rbx
00498683  C3                              ret
00498684  CC                              int3
00498685  E8 E6 65 DE FF                  call 0x14027ec70
0049868A  80 63 0D FE                     and byte ptr [rbx + 0xd], 0xfe
0049868E  EB EE                           jmp 0x14049867e
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiUnlockFaultWorkingSet(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    if (((*(unsigned __int8 *)(a1 + 13)) & (1)) != 0) goto loc_00498685;
    result = MiUnlockWorkingSetShared(*(unsigned __int64 *)(a1), *(unsigned __int8 *)(a1 + 12), a3, a4);
loc_0049867E:
    v_rsp = (v_rsp) + (32);
    return result;
loc_00498685:
    result = MiUnlockWorkingSetExclusive(*(unsigned __int64 *)(a1), *(unsigned __int8 *)(a1 + 12), a3, a4);
    goto loc_0049867E;
}
```

## 5. (Beta) C Style

```c
int64_t MiUnlockFaultWorkingSet(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    if (((*(uint8_t *)(arg1 + 0xD)) & (1)) != 0) goto loc_00498685;
    result = MiUnlockWorkingSetShared(*(uint64_t *)(arg1), *(uint8_t *)(arg1 + 0xC), a3, a4);
loc_0049867E:
    local_rsp = (local_rsp) + (32);
    return result;
loc_00498685:
    result = MiUnlockWorkingSetExclusive(*(uint64_t *)(arg1), *(uint8_t *)(arg1 + 0xC), a3, a4);
    goto loc_0049867E;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0xC` | `8` | `R` |
| `Arg1` | `+ 0xD` | `8` | `R` |
| `Arg1` | `+ 0xD` | `8` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00498664&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00498664[BB_00498664]
  bb_00498679[BB_00498679]
  bb_0049867E[BB_0049867E]
  bb_00498684[BB_00498684]
  bb_00498685[BB_00498685]
  bb_00498664 -->|branch| bb_00498685
  bb_00498664 -->|fallthrough| bb_00498679
  bb_00498679 -->|flow| bb_0049867E
  bb_00498684 -->|flow| bb_00498685
  bb_00498685 -->|branch| bb_0049867E
```
