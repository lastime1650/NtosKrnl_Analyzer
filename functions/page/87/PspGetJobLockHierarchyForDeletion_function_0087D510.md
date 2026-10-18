# PspGetJobLockHierarchyForDeletion

- RVA: `0x0087D510`–`0x0087D57D` (길이 `109` bytes)
- VA: `0x000000014087D510`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060BC4`
- 디코드: `30`개 명령, `109/109` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0087D531` → [PspLockJobAssignment](PspLockJobAssignment_function_0087DC18.md) (function, `0x0087DC18`)
- `0x0087D567` → [PspUnlockJobAssignment](PspUnlockJobAssignment_function_0087DBB4.md) (function, `0x0087DBB4`)

### Direct callers
- [PspJobDelete](../../text/4B/PspJobDelete_function_004BF8F0.md) at `0x004BFB65`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0087D510  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0087D515  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
0087D51A  57                              push rdi
0087D51B  48 83 EC 20                     sub rsp, 0x20
0087D51F  65 48 8B 34 25 88 01 00 00      mov rsi, qword ptr gs:[0x188]
0087D528  48 8B F9                        mov rdi, rcx
0087D52B  48 8B CE                        mov rcx, rsi
0087D52E  48 8B DA                        mov rbx, rdx
0087D531  E8 E2 06 00 00                  call 0x14087dc18
0087D536  48 8B 87 18 05 00 00            mov rax, qword ptr [rdi + 0x518]
0087D53D  33 D2                           xor edx, edx
0087D53F  48 85 C0                        test rax, rax
0087D542  74 0C                           je 0x14087d550
0087D544  88 53 10                        mov byte ptr [rbx + 0x10], dl
0087D547  BA 01 00 00 00                  mov edx, 1
0087D54C  48 89 43 08                     mov qword ptr [rbx + 8], rax
0087D550  8B C2                           mov eax, edx
0087D552  48 8B CE                        mov rcx, rsi
0087D555  48 03 C0                        add rax, rax
0087D558  48 89 7C C3 08                  mov qword ptr [rbx + rax*8 + 8], rdi
0087D55D  C6 44 C3 10 00                  mov byte ptr [rbx + rax*8 + 0x10], 0
0087D562  8D 42 01                        lea eax, [rdx + 1]
0087D565  89 03                           mov dword ptr [rbx], eax
0087D567  E8 48 06 00 00                  call 0x14087dbb4
0087D56C  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
0087D571  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
0087D576  48 83 C4 20                     add rsp, 0x20
0087D57A  5F                              pop rdi
0087D57B  C3                              ret
0087D57C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PspGetJobLockHierarchyForDeletion(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_rsp = (v_rsp) - (32);
    result = PspLockJobAssignment(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, a3, a4);
    a2 = 0;
    if (*(unsigned __int64 *)(a1 + 1304) != 0) {
        *(unsigned __int8 *)(a2 + 16) = 0;
        a2 = 1;
        *(unsigned __int64 *)(a2 + 8) = *(unsigned __int64 *)(a1 + 1304);
    }
    result = ((unsigned int)((unsigned int)(a2))) + ((unsigned int)((unsigned int)(a2)));
    *(unsigned __int64 *)(a2 + result * 8 + 8) = a1;
    *(unsigned __int8 *)(a2 + result * 8 + 16) = 0;
    *(unsigned int *)(a2) = (unsigned int)(a2 + 1);
    result = PspUnlockJobAssignment(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PspGetJobLockHierarchyForDeletion(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    local_rsp = (local_rsp) - (32);
    result = PspLockJobAssignment(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, a3, a4);
    Arg2 = 0;
    if (*(uint64_t *)(arg1 + 0x518) != 0) {
        *(uint8_t *)(arg2 + 0x10) = 0;
        Arg2 = 1;
        *(uint64_t *)(arg2 + 0x8) = *(uint64_t *)(arg1 + 0x518);
    }
    result = ((uint32_t)((uint32_t)(Arg2))) + ((uint32_t)((uint32_t)(Arg2)));
    *(void **)(arg2 + result * 8 + 0x8) = Arg1;
    *(uint8_t *)(arg2 + result * 8 + 0x10) = 0;
    *(uint32_t *)(arg2) = (uint32_t)(Arg2 + 1);
    result = PspUnlockJobAssignment(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x518` | `64` | `R` |
| `Arg2` | `+ 0x0` | `32` | `W` |
| `Arg2` | `+ 0x8` | `64` | `W` |
| `Arg2` | `+ 0x8 + rax*8` | `64` | `W` |
| `Arg2` | `+ 0x10` | `8` | `W` |
| `Arg2` | `+ 0x10 + rax*8` | `8` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0087D510&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0087D510[BB_0087D510]
  bb_0087D544[BB_0087D544]
  bb_0087D550[BB_0087D550]
  bb_0087D57C[BB_0087D57C]
  bb_0087D510 -->|branch| bb_0087D550
  bb_0087D510 -->|fallthrough| bb_0087D544
  bb_0087D544 -->|flow| bb_0087D550
```
