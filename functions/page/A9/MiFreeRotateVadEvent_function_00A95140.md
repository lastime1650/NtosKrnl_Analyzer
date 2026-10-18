# MiFreeRotateVadEvent

- RVA: `0x00A95140`–`0x00A95174` (길이 `52` bytes)
- VA: `0x0000000140A95140`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CEE8`
- 디코드: `13`개 명령, `52/52` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A95162` → [PsReturnProcessNonPagedPoolQuota](../../text/41/PsReturnProcessNonPagedPoolQuota_function_0041C200.md) (function, `0x0041C200`)
- `0x00A9516D` → [MiFreeInPageSupportBlock](../../text/2B/MiFreeInPageSupportBlock_function_002B5900.md) (function, `0x002B5900`)

### Direct callers
- [MiFreeRotateView](../7F/MiFreeRotateView_function_007FE6CC.md) at `0x007FE6E7`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00A95162` → [PsReturnProcessNonPagedPoolQuota](../../text/41/PsReturnProcessNonPagedPoolQuota_function_0041C200.md) (`PAGE` → `.text`)
  - `0x00A9516D` → [MiFreeInPageSupportBlock](../../text/2B/MiFreeInPageSupportBlock_function_002B5900.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A95140  48 83 EC 28                     sub rsp, 0x28
00A95144  48 8B 49 08                     mov rcx, qword ptr [rcx + 8]
00A95148  48 85 C9                        test rcx, rcx
00A9514B  75 20                           jne 0x140a9516d
00A9514D  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00A95156  BA 18 02 00 00                  mov edx, 0x218
00A9515B  48 8B 89 B8 00 00 00            mov rcx, qword ptr [rcx + 0xb8]
00A95162  E8 99 70 98 FF                  call 0x14041c200
00A95167  48 83 C4 28                     add rsp, 0x28
00A9516B  C3                              ret
00A9516C  CC                              int3
00A9516D  E8 8E 07 82 FF                  call 0x1402b5900
00A95172  EB D9                           jmp 0x140a9514d
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiFreeRotateVadEvent(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (*(unsigned __int64 *)(a1 + 8) != 0) goto loc_00A9516D;
loc_00A9514D:
    result = PsReturnProcessNonPagedPoolQuota(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), 536, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
loc_00A9516D:
    result = MiFreeInPageSupportBlock(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), 536, a3, a4);
    goto loc_00A9514D;
}
```

## 5. (Beta) C Style

```c
int64_t MiFreeRotateVadEvent(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (*(uint64_t *)(arg1 + 0x8) != 0) goto loc_00A9516D;
loc_00A9514D:
    result = PsReturnProcessNonPagedPoolQuota(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), 536, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
loc_00A9516D:
    result = MiFreeInPageSupportBlock(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), 536, a3, a4);
    goto loc_00A9514D;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A95140&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A95140[BB_00A95140]
  bb_00A9514D[BB_00A9514D]
  bb_00A9516C[BB_00A9516C]
  bb_00A9516D[BB_00A9516D]
  bb_00A95140 -->|branch| bb_00A9516D
  bb_00A95140 -->|fallthrough| bb_00A9514D
  bb_00A9516C -->|flow| bb_00A9516D
  bb_00A9516D -->|branch| bb_00A9514D
```
