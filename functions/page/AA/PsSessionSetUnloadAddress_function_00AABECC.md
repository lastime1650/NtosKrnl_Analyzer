# PsSessionSetUnloadAddress

- RVA: `0x00AABECC`–`0x00AABF37` (길이 `107` bytes)
- VA: `0x0000000140AABECC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060BC4`
- 디코드: `25`개 명령, `107/107` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00AABF0E` → [PspLockProcessListExclusive](../../text/22/PspLockProcessListExclusive_function_0022578C.md) (function, `0x0022578C`)
- `0x00AABF21` → [PspUnlockProcessListExclusive](../../text/2D/PspUnlockProcessListExclusive_function_002DFD18.md) (function, `0x002DFD18`)

### Direct callers
- [ExpInitializeSessionDriver](../AF/ExpInitializeSessionDriver_function_00AF49D4.md) at `0x00AF4A34`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00AABF0E` → [PspLockProcessListExclusive](../../text/22/PspLockProcessListExclusive_function_0022578C.md) (`PAGE` → `.text`)
  - `0x00AABF21` → [PspUnlockProcessListExclusive](../../text/2D/PspUnlockProcessListExclusive_function_002DFD18.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AABECC  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00AABED1  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
00AABED6  57                              push rdi
00AABED7  48 83 EC 20                     sub rsp, 0x20
00AABEDB  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AABEE4  48 8B 59 68                     mov rbx, qword ptr [rcx + 0x68]
00AABEE8  65 48 8B 3C 25 88 01 00 00      mov rdi, qword ptr gs:[0x188]
00AABEF1  48 85 DB                        test rbx, rbx
00AABEF4  48 8B CF                        mov rcx, rdi
00AABEF7  48 8B 90 B8 00 00 00            mov rdx, qword ptr [rax + 0xb8]
00AABEFE  B8 01 00 00 00                  mov eax, 1
00AABF03  48 0F 44 D8                     cmove rbx, rax
00AABF07  48 8B B2 E8 02 00 00            mov rsi, qword ptr [rdx + 0x2e8]
00AABF0E  E8 79 98 77 FF                  call 0x14022578c
00AABF13  48 83 7E 78 00                  cmp qword ptr [rsi + 0x78], 0
00AABF18  75 04                           jne 0x140aabf1e
00AABF1A  48 89 5E 78                     mov qword ptr [rsi + 0x78], rbx
00AABF1E  48 8B CF                        mov rcx, rdi
00AABF21  E8 F2 3D 83 FF                  call 0x1402dfd18
00AABF26  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00AABF2B  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
00AABF30  48 83 C4 20                     add rsp, 0x20
00AABF34  5F                              pop rdi
00AABF35  C3                              ret
00AABF36  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PsSessionSetUnloadAddress(__int64 a1)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_rsp = (v_rsp) - (32);
    v_rbx = *(unsigned __int64 *)(a1 + 104);
    if (*(unsigned __int64 *)(a1 + 104) == 0) { v_rbx = 1; }
    result = PspLockProcessListExclusive(*(unsigned __int64 *)(gs_base + (0 + 392)), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), a3, a4);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 744) + 120)) == 0) {
        *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 744) + 120) = v_rbx;
    }
    result = PspUnlockProcessListExclusive(*(unsigned __int64 *)(gs_base + (0 + 392)), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PsSessionSetUnloadAddress(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    local_rsp = (local_rsp) - (32);
    local_rbx = *(uint64_t *)(arg1 + 0x68);
    if (*(uint64_t *)(arg1 + 0x68) == 0) { local_rbx = 1; }
    result = PspLockProcessListExclusive(*(uint64_t *)(gs_base + (0 + 0x188)), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), a3, a4);
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x2E8) + 0x78)) == 0) {
        *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x2E8) + 0x78) = local_rbx;
    }
    result = PspUnlockProcessListExclusive(*(uint64_t *)(gs_base + (0 + 0x188)), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x68` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AABECC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00AABECC[BB_00AABECC]
  bb_00AABF1A[BB_00AABF1A]
  bb_00AABF1E[BB_00AABF1E]
  bb_00AABF36[BB_00AABF36]
  bb_00AABECC -->|branch| bb_00AABF1E
  bb_00AABECC -->|fallthrough| bb_00AABF1A
  bb_00AABF1A -->|flow| bb_00AABF1E
```
