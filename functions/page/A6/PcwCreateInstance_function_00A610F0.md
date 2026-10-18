# PcwCreateInstance

- RVA: `0x00A610F0`–`0x00A61173` (길이 `131` bytes)
- VA: `0x0000000140A610F0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000969D8`
- 디코드: `36`개 명령, `131/131` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00A61117` → [ExGetExtensionTable](../../text/42/ExGetExtensionTable_function_00428814.md) (function, `0x00428814`)
- `0x00A6113B` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00A61149` → [ExReleaseExtensionTable](../../text/45/ExReleaseExtensionTable_function_00456DC0.md) (function, `0x00456DC0`)
- `0x00A6116A` → [ExpPcwDisabledStatus](ExpPcwDisabledStatus_function_00A611E0.md) (function, `0x00A611E0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00A6110A` → RVA `0x00FD8080` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00A61117` → [ExGetExtensionTable](../../text/42/ExGetExtensionTable_function_00428814.md) (`PAGE` → `.text`)
  - `0x00A6113B` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00A61149` → [ExReleaseExtensionTable](../../text/45/ExReleaseExtensionTable_function_00456DC0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A610F0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00A610F5  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
00A610FA  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
00A610FF  57                              push rdi
00A61100  48 83 EC 30                     sub rsp, 0x30
00A61104  48 8B D9                        mov rbx, rcx
00A61107  41 8B F9                        mov edi, r9d
00A6110A  48 8B 0D 6F 6F 57 00            mov rcx, qword ptr [rip + 0x576f6f]
00A61111  49 8B F0                        mov rsi, r8
00A61114  48 8B EA                        mov rbp, rdx
00A61117  E8 F8 76 9C FF                  call 0x140428814
00A6111C  48 85 C0                        test rax, rax
00A6111F  74 45                           je 0x140a61166
00A61121  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
00A61126  44 8B CF                        mov r9d, edi
00A61129  48 8B 40 10                     mov rax, qword ptr [rax + 0x10]
00A6112D  4C 8B C6                        mov r8, rsi
00A61130  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00A61135  48 8B D5                        mov rdx, rbp
00A61138  48 8B CB                        mov rcx, rbx
00A6113B  E8 90 99 C5 FF                  call 0x1406baad0
00A61140  48 8B 0D 39 6F 57 00            mov rcx, qword ptr [rip + 0x576f39]
00A61147  8B D8                           mov ebx, eax
00A61149  E8 72 5C 9F FF                  call 0x140456dc0
00A6114E  48 8B 6C 24 48                  mov rbp, qword ptr [rsp + 0x48]
00A61153  8B C3                           mov eax, ebx
00A61155  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
00A6115A  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
00A6115F  48 83 C4 30                     add rsp, 0x30
00A61163  5F                              pop rdi
00A61164  C3                              ret
00A61165  CC                              int3
00A61166  48 83 23 00                     and qword ptr [rbx], 0
00A6116A  E8 71 00 00 00                  call 0x140a611e0
00A6116F  8B D8                           mov ebx, eax
00A61171  EB DB                           jmp 0x140a6114e
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PcwCreateInstance(__int64 a1, __int64 a2, __int64 a3, int a4, __int64 a5)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (48);
    result = ExGetExtensionTable(*(unsigned __int64 *)(v_rip + 5730159), a2, a3, a4);
    if (result == 0) goto loc_00A61166;
    v_stack_m18 = a5;
    result = guard_dispatch_icall(a1, a2, a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    result = ExReleaseExtensionTable(*(unsigned __int64 *)(v_rip + 5730105), a2, a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
loc_00A6114E:
    v_rsp = (v_rsp) + (48);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
loc_00A61166:
    result = ExpPcwDisabledStatus(*(unsigned __int64 *)(v_rip + 5730105), a2, a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    goto loc_00A6114E;
}
```

## 5. (Beta) C Style

```c
int64_t PcwCreateInstance(void *Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4, int64_t Arg5)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (48);
    result = ExGetExtensionTable(*(uint64_t *)(v_rip + 0x576F6F), Arg2, Arg3, Arg4);
    if (result == 0) goto loc_00A61166;
    v_stack_m18 = Arg5;
    result = guard_dispatch_icall(Arg1, Arg2, Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    result = ExReleaseExtensionTable(*(uint64_t *)(v_rip + 0x576F39), Arg2, Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
loc_00A6114E:
    local_rsp = (local_rsp) + (48);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
loc_00A61166:
    result = ExpPcwDisabledStatus(*(uint64_t *)(v_rip + 0x576F39), Arg2, Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    goto loc_00A6114E;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A610F0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A610F0[BB_00A610F0]
  bb_00A61121[BB_00A61121]
  bb_00A6114E[BB_00A6114E]
  bb_00A61165[BB_00A61165]
  bb_00A61166[BB_00A61166]
  bb_00A610F0 -->|branch| bb_00A61166
  bb_00A610F0 -->|fallthrough| bb_00A61121
  bb_00A61121 -->|flow| bb_00A6114E
  bb_00A61165 -->|flow| bb_00A61166
  bb_00A61166 -->|branch| bb_00A6114E
```
