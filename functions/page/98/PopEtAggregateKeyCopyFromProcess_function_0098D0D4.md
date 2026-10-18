# PopEtAggregateKeyCopyFromProcess

- RVA: `0x0098D0D4`–`0x0098D148` (길이 `116` bytes)
- VA: `0x000000014098D0D4`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00098810`
- 디코드: `30`개 명령, `116/116` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0098D11D` → [PopEtAggregateKeyCopy](PopEtAggregateKeyCopy_function_0098D37C.md) (function, `0x0098D37C`)
- `0x0098D131` → [PsGetProcessId](../../text/43/PsGetProcessId_function_0043D910.md) (function, `0x0043D910`)

### Direct callers
- [PopEtProcessSnapshotCreate](PopEtProcessSnapshotCreate_function_0098E4C8.md) at `0x0098E531`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0098D131` → [PsGetProcessId](../../text/43/PsGetProcessId_function_0043D910.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0098D0D4  4C 8B DC                        mov r11, rsp
0098D0D7  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
0098D0DB  57                              push rdi
0098D0DC  48 83 EC 40                     sub rsp, 0x40
0098D0E0  4C 8B 8A 68 06 00 00            mov r9, qword ptr [rdx + 0x668]
0098D0E7  48 8B DA                        mov rbx, rdx
0098D0EA  49 83 63 E8 00                  and qword ptr [r11 - 0x18], 0
0098D0EF  48 8B F9                        mov rdi, rcx
0098D0F2  49 83 63 F0 00                  and qword ptr [r11 - 0x10], 0
0098D0F7  49 8B 81 C8 01 00 00            mov rax, qword ptr [r9 + 0x1c8]
0098D0FE  49 89 43 D8                     mov qword ptr [r11 - 0x28], rax
0098D102  49 8B 81 D0 01 00 00            mov rax, qword ptr [r9 + 0x1d0]
0098D109  49 89 43 E0                     mov qword ptr [r11 - 0x20], rax
0098D10D  41 8B 40 08                     mov eax, dword ptr [r8 + 8]
0098D111  A8 01                           test al, 1
0098D113  75 19                           jne 0x14098d12e
0098D115  48 8D 54 24 20                  lea rdx, [rsp + 0x20]
0098D11A  48 8B CF                        mov rcx, rdi
0098D11D  E8 5A 02 00 00                  call 0x14098d37c
0098D122  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
0098D127  48 83 C4 40                     add rsp, 0x40
0098D12B  5F                              pop rdi
0098D12C  C3                              ret
0098D12D  CC                              int3
0098D12E  48 8B CB                        mov rcx, rbx
0098D131  E8 DA 07 AB FF                  call 0x14043d910
0098D136  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
0098D13A  48 8B 83 78 06 00 00            mov rax, qword ptr [rbx + 0x678]
0098D141  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0098D146  EB CD                           jmp 0x14098d115
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopEtAggregateKeyCopyFromProcess(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_p30;
    unsigned int v_stack_p38;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    v_rsp = (v_rsp) - (64);
    *(unsigned __int64 *)(v_rsp - 40) = *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 1640) + 456);
    *(unsigned __int64 *)(v_rsp - 32) = *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 1640) + 464);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a3 + 8)))) & (1)) != 0) goto loc_0098D12E;
loc_0098D115:
    result = PopEtAggregateKeyCopy(a1, v_stack_m28, a3, *(unsigned __int64 *)(a2 + 1640));
    v_rsp = (v_rsp) + (64);
    return result;
loc_0098D12E:
    result = PsGetProcessId(v_stack_p8, v_stack_m28, a3, *(unsigned __int64 *)(a2 + 1640));
    v_stack_p38 = (unsigned int)(result);
    v_stack_p30 = *(unsigned __int64 *)(v_stack_p8 + 1656);
    goto loc_0098D115;
}
```

## 5. (Beta) C Style

```c
int64_t PopEtAggregateKeyCopyFromProcess(int64_t Arg1, void *Arg2, void *Arg3)
{
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_p30;
    uint32_t v_stack_p38;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    local_rsp = (local_rsp) - (64);
    *(uint64_t *)(local_rsp - 0x28) = *(uint64_t *)(*(uint64_t *)(arg2 + 0x668) + 0x1C8);
    *(uint64_t *)(local_rsp - 0x20) = *(uint64_t *)(*(uint64_t *)(arg2 + 0x668) + 0x1D0);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg3 + 0x8)))) & (1)) != 0) goto loc_0098D12E;
loc_0098D115:
    result = PopEtAggregateKeyCopy(Arg1, v_stack_m28, Arg3, *(uint64_t *)(arg2 + 0x668));
    local_rsp = (local_rsp) + (64);
    return result;
loc_0098D12E:
    result = PsGetProcessId(v_stack_p8, v_stack_m28, Arg3, *(uint64_t *)(arg2 + 0x668));
    v_stack_p38 = (uint32_t)(result);
    v_stack_p30 = *(uint64_t *)(v_stack_p8 + 0x678);
    goto loc_0098D115;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x668` | `64` | `R` |
| `Arg2` | `+ 0x678` | `64` | `R` |
| `Arg3` | `+ 0x8` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0098D0D4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0098D0D4[BB_0098D0D4]
  bb_0098D115[BB_0098D115]
  bb_0098D12D[BB_0098D12D]
  bb_0098D12E[BB_0098D12E]
  bb_0098D0D4 -->|branch| bb_0098D12E
  bb_0098D0D4 -->|fallthrough| bb_0098D115
  bb_0098D12D -->|flow| bb_0098D12E
  bb_0098D12E -->|branch| bb_0098D115
```
