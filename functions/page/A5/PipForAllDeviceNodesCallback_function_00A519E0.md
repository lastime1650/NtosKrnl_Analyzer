# PipForAllDeviceNodesCallback

- RVA: `0x00A519E0`–`0x00A51A1E` (길이 `62` bytes)
- VA: `0x0000000140A519E0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CAAC`
- 디코드: `20`개 명령, `62/62` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A519F7` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00A51A0D` → [PipForAllChildDeviceNodes](PipForAllChildDeviceNodes_function_00A519A0.md) (function, `0x00A519A0`)

### Direct callers
- [PipForDeviceNodeSubtree](PipForDeviceNodeSubtree_function_00A51920.md) at `0x00A51970`
- [PipForAllChildDeviceNodes](PipForAllChildDeviceNodes_function_00A519A0.md) at `0x00A519C5`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00A519F7` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A519E0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00A519E5  57                              push rdi
00A519E6  48 83 EC 20                     sub rsp, 0x20
00A519EA  48 8B 02                        mov rax, qword ptr [rdx]
00A519ED  48 8B FA                        mov rdi, rdx
00A519F0  48 8B 52 08                     mov rdx, qword ptr [rdx + 8]
00A519F4  48 8B D9                        mov rbx, rcx
00A519F7  E8 D4 90 C6 FF                  call 0x1406baad0
00A519FC  85 C0                           test eax, eax
00A519FE  78 12                           js 0x140a51a12
00A51A00  48 83 7B 08 00                  cmp qword ptr [rbx + 8], 0
00A51A05  74 0B                           je 0x140a51a12
00A51A07  4C 8B C7                        mov r8, rdi
00A51A0A  48 8B CB                        mov rcx, rbx
00A51A0D  E8 8E FF FF FF                  call 0x140a519a0
00A51A12  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00A51A17  48 83 C4 20                     add rsp, 0x20
00A51A1B  5F                              pop rdi
00A51A1C  C3                              ret
00A51A1D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PipForAllDeviceNodesCallback(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    result = guard_dispatch_icall(a1, *(unsigned __int64 *)(a2 + 8), a3, a4);
    if (sign_flag) goto loc_00A51A12;
    if ((*(unsigned __int64 *)(a1 + 8)) != 0) {
        a3 = a2;
        a1 = a1;
        result = PipForAllChildDeviceNodes(a1, *(unsigned __int64 *)(a2 + 8), a3, a4);
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PipForAllDeviceNodesCallback(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    result = guard_dispatch_icall(Arg1, *(uint64_t *)(arg2 + 0x8), a3, a4);
    if (sign_flag) goto loc_00A51A12;
    if ((*(uint64_t *)(arg1 + 0x8)) != 0) {
        a3 = Arg2;
        Arg1 = Arg1;
        result = PipForAllChildDeviceNodes(Arg1, *(uint64_t *)(arg2 + 0x8), a3, a4);
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg2` | `+ 0x0` | `64` | `R` |
| `Arg2` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A519E0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A519E0[BB_00A519E0]
  bb_00A51A00[BB_00A51A00]
  bb_00A51A07[BB_00A51A07]
  bb_00A51A12[BB_00A51A12]
  bb_00A51A1D[BB_00A51A1D]
  bb_00A519E0 -->|branch| bb_00A51A12
  bb_00A519E0 -->|fallthrough| bb_00A51A00
  bb_00A51A00 -->|branch| bb_00A51A12
  bb_00A51A00 -->|fallthrough| bb_00A51A07
  bb_00A51A07 -->|flow| bb_00A51A12
```
