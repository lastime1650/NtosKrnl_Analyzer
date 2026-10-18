# MiFlowThroughRemoveNode

- RVA: `0x00381BB0`–`0x00381C19` (길이 `105` bytes)
- VA: `0x0000000140381BB0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007BA6C`
- 디코드: `27`개 명령, `105/105` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00381BF3` → [ExAcquireSpinLockExclusive](../24/ExAcquireSpinLockExclusive_function_00248690.md) (function, `0x00248690`)
- `0x00381C08` → [RtlAvlRemoveNode](../29/RtlAvlRemoveNode_function_00296650.md) (function, `0x00296650`)
- `0x00381C12` → [MiReleaseSpinLockExclusive](../24/MiReleaseSpinLockExclusive_function_002482C0.md) (function, `0x002482C0`)

### Direct callers
- [MiWaitForInPageComplete](MiWaitForInPageComplete_function_00380AB8.md) at `0x00380D5C`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00381BB0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00381BB5  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
00381BBA  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
00381BBF  57                              push rdi
00381BC0  48 83 EC 20                     sub rsp, 0x20
00381BC4  48 8B B1 50 01 00 00            mov rsi, qword ptr [rcx + 0x150]
00381BCB  48 8B E9                        mov rbp, rcx
00381BCE  48 85 F6                        test rsi, rsi
00381BD1  75 16                           jne 0x140381be9
00381BD3  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00381BD8  48 8B 6C 24 38                  mov rbp, qword ptr [rsp + 0x38]
00381BDD  48 8B 74 24 40                  mov rsi, qword ptr [rsp + 0x40]
00381BE2  48 83 C4 20                     add rsp, 0x20
00381BE6  5F                              pop rdi
00381BE7  C3                              ret
00381BE8  CC                              int3
00381BE9  48 8D BE C8 00 00 00            lea rdi, [rsi + 0xc8]
00381BF0  48 8B CF                        mov rcx, rdi
00381BF3  E8 98 6A EC FF                  call 0x140248690
00381BF8  48 8D 95 60 01 00 00            lea rdx, [rbp + 0x160]
00381BFF  8A D8                           mov bl, al
00381C01  48 8D 8E D0 00 00 00            lea rcx, [rsi + 0xd0]
00381C08  E8 43 4A F1 FF                  call 0x140296650
00381C0D  8A D3                           mov dl, bl
00381C0F  48 8B CF                        mov rcx, rdi
00381C12  E8 A9 66 EC FF                  call 0x1402482c0
00381C17  EB BA                           jmp 0x140381bd3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiFlowThroughRemoveNode(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (32);
    if (*(unsigned __int64 *)(a1 + 336) != 0) goto loc_00381BE9;
loc_00381BD3:
    v_rsp = (v_rsp) + (32);
    return result;
loc_00381BE9:
    result = ExAcquireSpinLockExclusive(v_stack_p18 + 200, a2, a3, a4);
    result = RtlAvlRemoveNode(v_stack_p18 + 208, v_stack_p10 + 352, a3, a4);
    result = MiReleaseSpinLockExclusive(v_stack_p18 + 200, (unsigned __int8)((unsigned __int8)(result)), a3, a4);
    goto loc_00381BD3;
}
```

## 5. (Beta) C Style

```c
int64_t MiFlowThroughRemoveNode(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (32);
    if (*(uint64_t *)(arg1 + 0x150) != 0) goto loc_00381BE9;
loc_00381BD3:
    local_rsp = (local_rsp) + (32);
    return result;
loc_00381BE9:
    result = ExAcquireSpinLockExclusive(v_stack_p18 + 200, a2, a3, a4);
    result = RtlAvlRemoveNode(v_stack_p18 + 208, v_stack_p10 + 352, a3, a4);
    result = MiReleaseSpinLockExclusive(v_stack_p18 + 200, (uint8_t)((uint8_t)(result)), a3, a4);
    goto loc_00381BD3;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x150` | `64` | `R` |
| `Arg1` | `+ 0x160` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00381BB0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00381BB0[BB_00381BB0]
  bb_00381BD3[BB_00381BD3]
  bb_00381BE8[BB_00381BE8]
  bb_00381BE9[BB_00381BE9]
  bb_00381BB0 -->|branch| bb_00381BE9
  bb_00381BB0 -->|fallthrough| bb_00381BD3
  bb_00381BE8 -->|flow| bb_00381BE9
  bb_00381BE9 -->|branch| bb_00381BD3
```
