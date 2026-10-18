# EmpRuleParserStackPush

- RVA: `0x00C27F2C`–`0x00C27F9D` (길이 `113` bytes)
- VA: `0x0000000140C27F2C`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C954`
- 디코드: `32`개 명령, `113/113` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00C27F5B` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)

### Direct callers
- [EmpParseRuleExpression](EmpParseRuleExpression_function_00C26A70.md) at `0x00C26C13`
- [EmpParseRuleExpression](EmpParseRuleExpression_function_00C26A70.md) at `0x00C26DF9`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00C27F5B` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C27F2C  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00C27F31  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
00C27F36  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
00C27F3B  57                              push rdi
00C27F3C  48 83 EC 20                     sub rsp, 0x20
00C27F40  49 8B F0                        mov rsi, r8
00C27F43  8B EA                           mov ebp, edx
00C27F45  48 8B D9                        mov rbx, rcx
00C27F48  BA 28 00 00 00                  mov edx, 0x28
00C27F4D  41 B8 45 4D 73 74               mov r8d, 0x74734d45
00C27F53  B9 00 01 00 00                  mov ecx, 0x100
00C27F58  49 8B F9                        mov rdi, r9
00C27F5B  E8 90 A1 F5 FF                  call 0x140b820f0
00C27F60  48 85 C0                        test rax, rax
00C27F63  74 22                           je 0x140c27f87
00C27F65  8B 54 24 50                     mov edx, dword ptr [rsp + 0x50]
00C27F69  48 8D 48 20                     lea rcx, [rax + 0x20]
00C27F6D  89 50 18                        mov dword ptr [rax + 0x18], edx
00C27F70  89 28                           mov dword ptr [rax], ebp
00C27F72  48 89 70 08                     mov qword ptr [rax + 8], rsi
00C27F76  48 89 78 10                     mov qword ptr [rax + 0x10], rdi
00C27F7A  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
00C27F7E  48 89 01                        mov qword ptr [rcx], rax
00C27F81  48 89 4B 08                     mov qword ptr [rbx + 8], rcx
00C27F85  FF 03                           inc dword ptr [rbx]
00C27F87  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00C27F8C  48 8B 6C 24 38                  mov rbp, qword ptr [rsp + 0x38]
00C27F91  48 8B 74 24 40                  mov rsi, qword ptr [rsp + 0x40]
00C27F96  48 83 C4 20                     add rsp, 0x20
00C27F9A  5F                              pop rdi
00C27F9B  C3                              ret
00C27F9C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EmpRuleParserStackPush(__int64 a1, int a2, __int64 a3, __int64 a4, unsigned int a5)
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
    result = ExAllocatePool2(256, 40, (unsigned int)(0x74734D45ULL), a4);
    if (result != 0) {
        a2 = a5;
        a1 = result + 32;
        *(unsigned int *)(result + 24) = a2;
        *(unsigned int *)(result) = (unsigned int)((unsigned int)(a2));
        *(unsigned __int64 *)(result + 8) = a3;
        *(unsigned __int64 *)(result + 16) = a4;
        result = *(unsigned __int64 *)(a1 + 8);
        *(unsigned __int64 *)(a1) = result;
        *(unsigned __int64 *)(a1 + 8) = a1;
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t EmpRuleParserStackPush(void *Arg1, int32_t Arg2, int64_t Arg3, int64_t Arg4, uint32_t Arg5)
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
    result = ExAllocatePool2(256, 40, (uint32_t)(0x74734D45ULL), Arg4);
    if (result != 0) {
        Arg2 = Arg5;
        Arg1 = result + 32;
        *(uint32_t *)(result + 0x18) = Arg2;
        *(uint32_t *)(result) = (uint32_t)((uint32_t)(Arg2));
        *(uint64_t *)(result + 0x8) = Arg3;
        *(uint64_t *)(result + 0x10) = Arg4;
        result = *(uint64_t *)(arg1 + 0x8);
        *(uint64_t *)(arg1) = result;
        *(void **)(arg1 + 0x8) = Arg1;
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R/W` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C27F2C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00C27F2C[BB_00C27F2C]
  bb_00C27F65[BB_00C27F65]
  bb_00C27F87[BB_00C27F87]
  bb_00C27F9C[BB_00C27F9C]
  bb_00C27F2C -->|branch| bb_00C27F87
  bb_00C27F2C -->|fallthrough| bb_00C27F65
  bb_00C27F65 -->|flow| bb_00C27F87
```
