# EtwpInitStateChangeInfo

- RVA: `0x008A48D4`–`0x008A4989` (길이 `181` bytes)
- VA: `0x00000001408A48D4`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000794E0`
- 디코드: `42`개 명령, `181/181` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x008A48F2` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x008A4904` → [PsGetProcessSessionId](../../text/22/PsGetProcessSessionId_function_002233A0.md) (function, `0x002233A0`)
- `0x008A493B` → [EtwpGetProcessStartKey](../../text/45/EtwpGetProcessStartKey_function_00459180.md) (function, `0x00459180`)

### Direct callers
- [EtwTraceProcess](EtwTraceProcess_function_008A4004.md) at `0x008A40F2`
- [EtwTraceAppStateChange](EtwTraceAppStateChange_function_008A452C.md) at `0x008A45C2`

### Static image references
- `0x008A495D` → RVA `0x00EFFA20` (`.data`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x008A48F2` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x008A4904` → [PsGetProcessSessionId](../../text/22/PsGetProcessSessionId_function_002233A0.md) (`PAGE` → `.text`)
  - `0x008A493B` → [EtwpGetProcessStartKey](../../text/45/EtwpGetProcessStartKey_function_00459180.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008A48D4  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
008A48D9  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
008A48DE  57                              push rdi
008A48DF  48 83 EC 30                     sub rsp, 0x30
008A48E3  48 8B F2                        mov rsi, rdx
008A48E6  48 8B F9                        mov rdi, rcx
008A48E9  33 D2                           xor edx, edx
008A48EB  48 8B CE                        mov rcx, rsi
008A48EE  44 8D 42 62                     lea r8d, [rdx + 0x62]
008A48F2  E8 49 23 E2 FF                  call 0x1406c6c40
008A48F7  8B 9F D0 01 00 00               mov ebx, dword ptr [rdi + 0x1d0]
008A48FD  48 8B CF                        mov rcx, rdi
008A4900  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
008A4904  E8 97 EA 97 FF                  call 0x1402233a0
008A4909  48 8B 8F F8 01 00 00            mov rcx, qword ptr [rdi + 0x1f8]
008A4910  44 8B C0                        mov r8d, eax
008A4913  66 A1 C4 02 00 00 80 F7 FF FF   movabs ax, word ptr [0xfffff780000002c4]
008A491D  66 89 44 24 26                  mov word ptr [rsp + 0x26], ax
008A4922  66 44 89 44 24 24               mov word ptr [rsp + 0x24], r8w
008A4928  89 5E 15                        mov dword ptr [rsi + 0x15], ebx
008A492B  66 44 89 46 19                  mov word ptr [rsi + 0x19], r8w
008A4930  66 89 46 1B                     mov word ptr [rsi + 0x1b], ax
008A4934  48 89 4E 1D                     mov qword ptr [rsi + 0x1d], rcx
008A4938  48 8B CF                        mov rcx, rdi
008A493B  E8 40 48 BB FF                  call 0x140459180
008A4940  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008A4945  0F 10 44 24 20                  movups xmm0, xmmword ptr [rsp + 0x20]
008A494A  F3 0F 7F 46 02                  movdqu xmmword ptr [rsi + 2], xmm0
008A494F  8B 87 78 06 00 00               mov eax, dword ptr [rdi + 0x678]
008A4955  89 46 25                        mov dword ptr [rsi + 0x25], eax
008A4958  B8 01 00 00 00                  mov eax, 1
008A495D  F0 48 0F C1 05 BA B0 65 00      lock xadd qword ptr [rip + 0x65b0ba], rax
008A4966  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
008A496B  48 FF C0                        inc rax
008A496E  48 89 46 52                     mov qword ptr [rsi + 0x52], rax
008A4972  48 8B 87 78 06 00 00            mov rax, qword ptr [rdi + 0x678]
008A4979  48 89 46 5A                     mov qword ptr [rsi + 0x5a], rax
008A497D  48 8B 74 24 48                  mov rsi, qword ptr [rsp + 0x48]
008A4982  48 83 C4 30                     add rsp, 0x30
008A4986  5F                              pop rdi
008A4987  C3                              ret
008A4988  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwpInitStateChangeInfo(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned __int16 v_stack_m12;
    unsigned __int16 v_stack_m14;
    unsigned int v_stack_m18;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_rsp = (v_rsp) - (48);
    a2 = 0;
    result = memset(0, a2, a2 + 98, a4);
    v_stack_m18 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 464)));
    result = PsGetProcessSessionId(a1, a2, a2 + 98, a4);
    v_stack_m12 = (unsigned __int16)(result);
    v_stack_m14 = (unsigned __int16)((unsigned int)((unsigned int)(result)));
    *(unsigned int *)(a2 + 21) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 464)));
    *(unsigned __int16 *)(a2 + 25) = (unsigned __int16)((unsigned int)((unsigned int)(result)));
    *(unsigned __int16 *)(a2 + 27) = (unsigned __int16)(result);
    *(unsigned __int64 *)(a2 + 29) = *(unsigned __int64 *)(a1 + 504);
    result = EtwpGetProcessStartKey(a1, a2, (unsigned int)((unsigned int)(result)), a4);
    v_stack_m10 = result;
    *(unsigned __int64 *)(a2 + 2) = v_xmm0;
    *(unsigned int *)(a2 + 37) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 1656)));
    result = (1) + 1;
    *(unsigned __int64 *)(a2 + 82) = result;
    *(unsigned __int64 *)(a2 + 90) = *(unsigned __int64 *)(a1 + 1656);
    v_rsp = (v_rsp) + (48);
    return *(unsigned __int64 *)(a1 + 1656);
}
```

## 5. (Beta) C Style

```c
int64_t EtwpInitStateChangeInfo(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint16_t v_stack_m12;
    uint16_t v_stack_m14;
    uint32_t v_stack_m18;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    local_rsp = (local_rsp) - (48);
    Arg2 = 0;
    result = memset(0, Arg2, Arg2 + 98, a4);
    v_stack_m18 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x1D0)));
    result = PsGetProcessSessionId(Arg1, Arg2, Arg2 + 98, a4);
    v_stack_m12 = (uint16_t)(result);
    v_stack_m14 = (uint16_t)((uint32_t)((uint32_t)(result)));
    *(uint32_t *)(arg2 + 0x15) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x1D0)));
    *(uint16_t *)(arg2 + 0x19) = (uint16_t)((uint32_t)((uint32_t)(result)));
    *(uint16_t *)(arg2 + 0x1B) = (uint16_t)(result);
    *(uint64_t *)(arg2 + 0x1D) = *(uint64_t *)(arg1 + 0x1F8);
    result = EtwpGetProcessStartKey(Arg1, Arg2, (uint32_t)((uint32_t)(result)), a4);
    v_stack_m10 = result;
    *(uint64_t *)(arg2 + 0x2) = v_xmm0;
    *(uint32_t *)(arg2 + 0x25) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x678)));
    result = (1) + 1;
    *(uint64_t *)(arg2 + 0x52) = result;
    *(uint64_t *)(arg2 + 0x5A) = *(uint64_t *)(arg1 + 0x678);
    local_rsp = (local_rsp) + (48);
    return *(uint64_t *)(arg1 + 0x678);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x1D0` | `32` | `R` |
| `Arg1` | `+ 0x1F8` | `64` | `R` |
| `Arg1` | `+ 0x678` | `32` | `R` |
| `Arg1` | `+ 0x678` | `64` | `R` |
| `Arg2` | `+ 0x2` | `128` | `W` |
| `Arg2` | `+ 0x15` | `32` | `W` |
| `Arg2` | `+ 0x19` | `16` | `W` |
| `Arg2` | `+ 0x1B` | `16` | `W` |
| `Arg2` | `+ 0x1D` | `64` | `W` |
| `Arg2` | `+ 0x25` | `32` | `W` |
| `Arg2` | `+ 0x52` | `64` | `W` |
| `Arg2` | `+ 0x5A` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008A48D4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_008A48D4[BB_008A48D4]
  bb_008A4988[BB_008A4988]
```
