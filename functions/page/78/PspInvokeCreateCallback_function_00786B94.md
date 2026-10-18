# PspInvokeCreateCallback

- RVA: `0x00786B94`–`0x00786BF1` (길이 `93` bytes)
- VA: `0x0000000140786B94`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060BC4`
- 디코드: `28`개 명령, `93/93` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00786BB8` → [EtwTraceJobServerSiloMonitorCallback](../../text/64/EtwTraceJobServerSiloMonitorCallback_function_0064FB68.md) (function, `0x0064FB68`)
- `0x00786BC4` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00786BD9` → [EtwTraceJobServerSiloMonitorCallback](../../text/64/EtwTraceJobServerSiloMonitorCallback_function_0064FB68.md) (function, `0x0064FB68`)

### Direct callers
- [PsStartSiloMonitor](PsStartSiloMonitor_function_007867C0.md) at `0x0078687D`
- [PsStartSiloMonitor](PsStartSiloMonitor_function_007867C0.md) at `0x007868E4`
- [PsStartSiloMonitor](PsStartSiloMonitor_function_007867C0.md) at `0x007869AF`
- [PspNotifyServerSiloCreation](PspNotifyServerSiloCreation_function_00786C58.md) at `0x00786CB2`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00786BB8` → [EtwTraceJobServerSiloMonitorCallback](../../text/64/EtwTraceJobServerSiloMonitorCallback_function_0064FB68.md) (`PAGE` → `.text`)
  - `0x00786BC4` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00786BD9` → [EtwTraceJobServerSiloMonitorCallback](../../text/64/EtwTraceJobServerSiloMonitorCallback_function_0064FB68.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00786B94  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00786B99  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
00786B9E  57                              push rdi
00786B9F  48 83 EC 20                     sub rsp, 0x20
00786BA3  48 8D 7A 28                     lea rdi, [rdx + 0x28]
00786BA7  48 8B DA                        mov rbx, rdx
00786BAA  48 8B D1                        mov rdx, rcx
00786BAD  48 8B F1                        mov rsi, rcx
00786BB0  4C 8B C7                        mov r8, rdi
00786BB3  33 C9                           xor ecx, ecx
00786BB5  45 33 C9                        xor r9d, r9d
00786BB8  E8 AB 8F EC FF                  call 0x14064fb68
00786BBD  48 8B 43 18                     mov rax, qword ptr [rbx + 0x18]
00786BC1  48 8B CE                        mov rcx, rsi
00786BC4  E8 07 3F F3 FF                  call 0x1406baad0
00786BC9  44 8B C8                        mov r9d, eax
00786BCC  4C 8B C7                        mov r8, rdi
00786BCF  48 8B D6                        mov rdx, rsi
00786BD2  B9 01 00 00 00                  mov ecx, 1
00786BD7  8B D8                           mov ebx, eax
00786BD9  E8 8A 8F EC FF                  call 0x14064fb68
00786BDE  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
00786BE3  8B C3                           mov eax, ebx
00786BE5  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00786BEA  48 83 C4 20                     add rsp, 0x20
00786BEE  5F                              pop rdi
00786BEF  C3                              ret
00786BF0  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PspInvokeCreateCallback(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_rsp = (v_rsp) - (32);
    a1 = 0;
    a4 = 0;
    result = EtwTraceJobServerSiloMonitorCallback(a1, a1, a2 + 40, a4);
    result = guard_dispatch_icall(0, a1, a2 + 40, a4);
    result = EtwTraceJobServerSiloMonitorCallback(1, 0, a2 + 40, (unsigned int)((unsigned int)(result)));
    v_rsp = (v_rsp) + (32);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
}
```

## 5. (Beta) C Style

```c
int64_t PspInvokeCreateCallback(int64_t Arg1, void *Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    local_rsp = (local_rsp) - (32);
    Arg1 = 0;
    Arg4 = 0;
    result = EtwTraceJobServerSiloMonitorCallback(Arg1, Arg1, Arg2 + 40, Arg4);
    result = guard_dispatch_icall(0, Arg1, Arg2 + 40, Arg4);
    result = EtwTraceJobServerSiloMonitorCallback(1, 0, Arg2 + 40, (uint32_t)((uint32_t)(result)));
    local_rsp = (local_rsp) + (32);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x18` | `64` | `R` |
| `Arg2` | `+ 0x28` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00786B94&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00786B94[BB_00786B94]
  bb_00786BF0[BB_00786BF0]
```
