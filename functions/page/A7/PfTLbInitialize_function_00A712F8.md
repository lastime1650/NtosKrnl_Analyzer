# PfTLbInitialize

- RVA: `0x00A712F8`–`0x00A71345` (길이 `77` bytes)
- VA: `0x0000000140A712F8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00070544`
- 디코드: `25`개 명령, `77/77` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A71316` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00A71337` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)

### Direct callers
- [PfTAllocateBuffers](../75/PfTAllocateBuffers_function_0075110C.md) at `0x00751176`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00A71316` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00A71337` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A712F8  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00A712FD  57                              push rdi
00A712FE  48 83 EC 20                     sub rsp, 0x20
00A71302  8B FA                           mov edi, edx
00A71304  48 8B D9                        mov rbx, rcx
00A71307  33 D2                           xor edx, edx
00A71309  45 85 C0                        test r8d, r8d
00A7130C  74 26                           je 0x140a71334
00A7130E  4C 8D 47 E8                     lea r8, [rdi - 0x18]
00A71312  48 83 C1 18                     add rcx, 0x18
00A71316  E8 25 59 C5 FF                  call 0x1406c6c40
00A7131B  83 63 10 00                     and dword ptr [rbx + 0x10], 0
00A7131F  8D 47 E8                        lea eax, [rdi - 0x18]
00A71322  C1 E8 04                        shr eax, 4
00A71325  89 43 14                        mov dword ptr [rbx + 0x14], eax
00A71328  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00A7132D  48 83 C4 20                     add rsp, 0x20
00A71331  5F                              pop rdi
00A71332  C3                              ret
00A71333  CC                              int3
00A71334  4C 8B C7                        mov r8, rdi
00A71337  E8 04 59 C5 FF                  call 0x1406c6c40
00A7133C  48 89 5B 08                     mov qword ptr [rbx + 8], rbx
00A71340  48 89 1B                        mov qword ptr [rbx], rbx
00A71343  EB D6                           jmp 0x140a7131b
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PfTLbInitialize(__int64 a1, int a2, int a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    a2 = 0;
    if (a3 == 0) goto loc_00A71334;
    a1 = (a1) + (24);
    result = memset(a1, a2, (unsigned int)(a2) - 24, a4);
loc_00A7131B:
    result = (unsigned int)(((unsigned int)(a2) - 24) >> (4));
    *(unsigned int *)(a1 + 20) = (unsigned int)(result);
    v_rsp = (v_rsp) + (32);
    return result;
loc_00A71334:
    result = memset(a1, a2, (unsigned int)(a2), a4);
    *(unsigned __int64 *)(v_stack_p8 + 8) = v_stack_p8;
    *(unsigned __int64 *)(v_stack_p8) = v_stack_p8;
    goto loc_00A7131B;
}
```

## 5. (Beta) C Style

```c
int64_t PfTLbInitialize(void *Arg1, void *Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    Arg2 = 0;
    if (Arg3 == 0) goto loc_00A71334;
    Arg1 = (Arg1) + (24);
    result = memset(Arg1, Arg2, (uint32_t)(Arg2) - 24, a4);
loc_00A7131B:
    result = (uint32_t)(((uint32_t)(Arg2) - 24) >> (4));
    *(uint32_t *)(arg1 + 0x14) = (uint32_t)(result);
    local_rsp = (local_rsp) + (32);
    return result;
loc_00A71334:
    result = memset(Arg1, Arg2, (uint32_t)(Arg2), a4);
    *(uint64_t *)(v_stack_p8 + 0x8) = v_stack_p8;
    *(uint64_t *)(v_stack_p8) = v_stack_p8;
    goto loc_00A7131B;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `W` |
| `Arg1` | `+ 0x8` | `64` | `W` |
| `Arg1` | `+ 0x10` | `32` | `R/W` |
| `Arg1` | `+ 0x14` | `32` | `W` |
| `Arg2` | `- 0x18` | `32` | `R` |
| `Arg2` | `- 0x18` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A712F8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A712F8[BB_00A712F8]
  bb_00A7130E[BB_00A7130E]
  bb_00A7131B[BB_00A7131B]
  bb_00A71333[BB_00A71333]
  bb_00A71334[BB_00A71334]
  bb_00A712F8 -->|branch| bb_00A71334
  bb_00A712F8 -->|fallthrough| bb_00A7130E
  bb_00A7130E -->|flow| bb_00A7131B
  bb_00A71333 -->|flow| bb_00A71334
  bb_00A71334 -->|branch| bb_00A7131B
```
