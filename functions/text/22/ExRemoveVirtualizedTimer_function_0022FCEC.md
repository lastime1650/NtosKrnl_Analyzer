# ExRemoveVirtualizedTimer

- RVA: `0x0022FCEC`–`0x0022FD58` (길이 `108` bytes)
- VA: `0x000000014022FCEC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C954`
- 디코드: `26`개 명령, `108/108` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0022FD15` → [KeAcquireSpinLockAtDpcLevel](../20/KeAcquireSpinLockAtDpcLevel_function_00208430.md) (function, `0x00208430`)
- `0x0022FD31` → [ExpTimerResume](ExpTimerResume_function_0022FD60.md) (function, `0x0022FD60`)
- `0x0022FD3A` → [KxReleaseSpinLock](../20/KxReleaseSpinLock_function_00206670.md) (function, `0x00206670`)

### Direct callers
- [PspProcessUnbindVirtualizedTimers](PspProcessUnbindVirtualizedTimers_function_0022FC3C.md) at `0x0022FCBB`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0022FCEC  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0022FCF1  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
0022FCF6  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
0022FCFB  57                              push rdi
0022FCFC  48 83 EC 20                     sub rsp, 0x20
0022FD00  48 8D 99 E0 FE FF FF            lea rbx, [rcx - 0x120]
0022FD07  48 8B EA                        mov rbp, rdx
0022FD0A  48 8B B3 18 01 00 00            mov rsi, qword ptr [rbx + 0x118]
0022FD11  48 8D 4B 40                     lea rcx, [rbx + 0x40]
0022FD15  E8 16 87 FD FF                  call 0x140208430
0022FD1A  48 83 A3 18 01 00 00 00         and qword ptr [rbx + 0x118], 0
0022FD22  F6 83 30 01 00 00 02            test byte ptr [rbx + 0x130], 2
0022FD29  74 0B                           je 0x14022fd36
0022FD2B  48 8B D5                        mov rdx, rbp
0022FD2E  48 8B CB                        mov rcx, rbx
0022FD31  E8 2A 00 00 00                  call 0x14022fd60
0022FD36  48 8D 4B 40                     lea rcx, [rbx + 0x40]
0022FD3A  E8 31 69 FD FF                  call 0x140206670
0022FD3F  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
0022FD44  48 8B C6                        mov rax, rsi
0022FD47  48 8B 74 24 40                  mov rsi, qword ptr [rsp + 0x40]
0022FD4C  48 8B 6C 24 38                  mov rbp, qword ptr [rsp + 0x38]
0022FD51  48 83 C4 20                     add rsp, 0x20
0022FD55  5F                              pop rdi
0022FD56  C3                              ret
0022FD57  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExRemoveVirtualizedTimer(__int64 a1, __int64 a2)
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
    result = KeAcquireSpinLockAtDpcLevel(a1 - 288 + 64, a2, a3, a4);
    if (((*(unsigned __int8 *)(a1 - 288 + 304)) & (2)) != 0) {
        a2 = a2;
        a1 = a1 - 288;
        result = ExpTimerResume(a1, a2, a3, a4);
    }
    result = KxReleaseSpinLock(a1 - 288 + 64, a2, a3, a4);
    v_rsp = (v_rsp) + (32);
    return *(unsigned __int64 *)(a1 - 288 + 280);
}
```

## 5. (Beta) C Style

```c
int64_t ExRemoveVirtualizedTimer(void *Arg1, int64_t Arg2)
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
    result = KeAcquireSpinLockAtDpcLevel(Arg1 - 288 + 64, Arg2, a3, a4);
    if (((*(uint8_t *)(arg1 - 0x120 + 0x130)) & (2)) != 0) {
        Arg2 = Arg2;
        Arg1 = Arg1 - 288;
        result = ExpTimerResume(Arg1, Arg2, a3, a4);
    }
    result = KxReleaseSpinLock(Arg1 - 288 + 64, Arg2, a3, a4);
    local_rsp = (local_rsp) + (32);
    return *(uint64_t *)(arg1 - 0x120 + 0x118);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `- 0x120` | `64` | `R` |
| `Arg1` | `+ 0x40` | `64` | `R` |
| `Arg1` | `+ 0x118` | `64` | `R` |
| `Arg1` | `+ 0x118` | `64` | `R/W` |
| `Arg1` | `+ 0x130` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0022FCEC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0022FCEC[BB_0022FCEC]
  bb_0022FD2B[BB_0022FD2B]
  bb_0022FD36[BB_0022FD36]
  bb_0022FD57[BB_0022FD57]
  bb_0022FCEC -->|branch| bb_0022FD36
  bb_0022FCEC -->|fallthrough| bb_0022FD2B
  bb_0022FD2B -->|flow| bb_0022FD36
```
