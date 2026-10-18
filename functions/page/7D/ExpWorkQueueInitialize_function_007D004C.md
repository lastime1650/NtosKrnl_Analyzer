# ExpWorkQueueInitialize

- RVA: `0x007D004C`–`0x007D00ED` (길이 `161` bytes)
- VA: `0x00000001407D004C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060300`
- 디코드: `40`개 명령, `161/161` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x007D0077` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x007D008A` → [ExpGetNodeSubQueueConcurrencyCount](../../text/65/ExpGetNodeSubQueueConcurrencyCount_function_0065A534.md) (function, `0x0065A534`)
- `0x007D0094` → [KeInitializePriQueue](../../text/5C/KeInitializePriQueue_function_005CA8B4.md) (function, `0x005CA8B4`)

### Direct callers
- [ExpPartitionCreatePoolInternal](../AF/ExpPartitionCreatePoolInternal_function_00AF6C08.md) at `0x00AF6CBD`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x007D0077` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x007D008A` → [ExpGetNodeSubQueueConcurrencyCount](../../text/65/ExpGetNodeSubQueueConcurrencyCount_function_0065A534.md) (`PAGE` → `.text`)
  - `0x007D0094` → [KeInitializePriQueue](../../text/5C/KeInitializePriQueue_function_005CA8B4.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007D004C  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
007D0051  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
007D0056  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
007D005B  57                              push rdi
007D005C  41 56                           push r14
007D005E  41 57                           push r15
007D0060  48 83 EC 20                     sub rsp, 0x20
007D0064  45 8B F0                        mov r14d, r8d
007D0067  8B EA                           mov ebp, edx
007D0069  33 D2                           xor edx, edx
007D006B  41 B8 F0 02 00 00               mov r8d, 0x2f0
007D0071  49 8B F1                        mov rsi, r9
007D0074  4C 8B F9                        mov r15, rcx
007D0077  E8 C4 6B EF FF                  call 0x1406c6c40
007D007C  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
007D0081  8B 7C 24 70                     mov edi, dword ptr [rsp + 0x70]
007D0085  48 8B CB                        mov rcx, rbx
007D0088  8B D7                           mov edx, edi
007D008A  E8 A5 A4 E8 FF                  call 0x14065a534
007D008F  8B D0                           mov edx, eax
007D0091  49 8B CF                        mov rcx, r15
007D0094  E8 1B A8 DF FF                  call 0x1405ca8b4
007D0099  8B 44 24 68                     mov eax, dword ptr [rsp + 0x68]
007D009D  41 89 87 D8 02 00 00            mov dword ptr [r15 + 0x2d8], eax
007D00A4  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
007D00A9  49 89 B7 B0 02 00 00            mov qword ptr [r15 + 0x2b0], rsi
007D00B0  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
007D00B5  49 89 9F B8 02 00 00            mov qword ptr [r15 + 0x2b8], rbx
007D00BC  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
007D00C1  41 89 AF CC 02 00 00            mov dword ptr [r15 + 0x2cc], ebp
007D00C8  48 8B 6C 24 48                  mov rbp, qword ptr [rsp + 0x48]
007D00CD  49 89 87 E8 02 00 00            mov qword ptr [r15 + 0x2e8], rax
007D00D4  45 89 B7 D4 02 00 00            mov dword ptr [r15 + 0x2d4], r14d
007D00DB  41 89 BF DC 02 00 00            mov dword ptr [r15 + 0x2dc], edi
007D00E2  48 83 C4 20                     add rsp, 0x20
007D00E6  41 5F                           pop r15
007D00E8  41 5E                           pop r14
007D00EA  5F                              pop rdi
007D00EB  C3                              ret
007D00EC  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExpWorkQueueInitialize(__int64 a1, int a2, int a3, __int64 a4, __int64 a5, unsigned int a6, unsigned int a7, __int64 a8)
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
    a2 = 0;
    result = memset(a1, a2, 752, a4);
    result = ExpGetNodeSubQueueConcurrencyCount(a5, (unsigned int)((unsigned int)((unsigned int)(a7))), 752, a4);
    result = KeInitializePriQueue(a1, (unsigned int)((unsigned int)(result)), 752, a4);
    *(unsigned int *)(a1 + 728) = (unsigned int)((unsigned int)(a6));
    *(unsigned __int64 *)(a1 + 688) = a4;
    *(unsigned __int64 *)(a1 + 696) = a5;
    *(unsigned int *)(a1 + 716) = (unsigned int)((unsigned int)(a2));
    *(unsigned __int64 *)(a1 + 744) = a8;
    *(unsigned int *)(a1 + 724) = (unsigned int)((unsigned int)(a3));
    *(unsigned int *)(a1 + 732) = (unsigned int)((unsigned int)(a7));
    v_rsp = (v_rsp) + (32);
    return a8;
}
```

## 5. (Beta) C Style

```c
int64_t ExpWorkQueueInitialize(void *Arg1, int32_t Arg2, int32_t Arg3, int64_t Arg4, int64_t Arg5, uint32_t Arg6, uint32_t Arg7, int64_t Arg8)
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
    Arg2 = 0;
    result = memset(Arg1, Arg2, 752, Arg4);
    result = ExpGetNodeSubQueueConcurrencyCount(Arg5, (uint32_t)((uint32_t)((uint32_t)(Arg7))), 752, Arg4);
    result = KeInitializePriQueue(Arg1, (uint32_t)((uint32_t)(result)), 752, Arg4);
    *(uint32_t *)(arg1 + 0x2D8) = (uint32_t)((uint32_t)(Arg6));
    *(uint64_t *)(arg1 + 0x2B0) = Arg4;
    *(uint64_t *)(arg1 + 0x2B8) = Arg5;
    *(uint32_t *)(arg1 + 0x2CC) = (uint32_t)((uint32_t)(Arg2));
    *(uint64_t *)(arg1 + 0x2E8) = Arg8;
    *(uint32_t *)(arg1 + 0x2D4) = (uint32_t)((uint32_t)(Arg3));
    *(uint32_t *)(arg1 + 0x2DC) = (uint32_t)((uint32_t)(Arg7));
    local_rsp = (local_rsp) + (32);
    return Arg8;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x2B0` | `64` | `W` |
| `Arg1` | `+ 0x2B8` | `64` | `W` |
| `Arg1` | `+ 0x2CC` | `32` | `W` |
| `Arg1` | `+ 0x2D4` | `32` | `W` |
| `Arg1` | `+ 0x2D8` | `32` | `W` |
| `Arg1` | `+ 0x2DC` | `32` | `W` |
| `Arg1` | `+ 0x2E8` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007D004C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007D004C[BB_007D004C]
  bb_007D00EC[BB_007D00EC]
```
