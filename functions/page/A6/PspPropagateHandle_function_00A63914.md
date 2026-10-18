# PspPropagateHandle

- RVA: `0x00A63914`–`0x00A63964` (길이 `80` bytes)
- VA: `0x0000000140A63914`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B3614`
- 디코드: `22`개 명령, `80/80` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A63951` → [ObDuplicateObject](../8C/ObDuplicateObject_function_008C4FA0.md) (function, `0x008C4FA0`)

### Direct callers
- [PspUpdateCreateInfo](../AE/PspUpdateCreateInfo_function_00AEC060.md) at `0x00AEC0EA`
- [PspUpdateCreateInfo](../AE/PspUpdateCreateInfo_function_00AEC060.md) at `0x00AEC104`
- [PspUpdateCreateInfo](../AE/PspUpdateCreateInfo_function_00AEC060.md) at `0x00AEC230`
- [PspUpdateCreateInfo](../AE/PspUpdateCreateInfo_function_00AEC060.md) at `0x00AEC287`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A63914  48 83 EC 48                     sub rsp, 0x48
00A63918  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00A63921  4C 8B 12                        mov r10, qword ptr [rdx]
00A63924  4C 8B 98 B8 00 00 00            mov r11, qword ptr [rax + 0xb8]
00A6392B  33 C0                           xor eax, eax
00A6392D  84 C9                           test cl, cl
00A6392F  74 2B                           je 0x140a6395c
00A63931  88 44 24 38                     mov byte ptr [rsp + 0x38], al
00A63935  4D 8B C8                        mov r9, r8
00A63938  C7 44 24 30 02 00 00 00         mov dword ptr [rsp + 0x30], 2
00A63940  4D 8B C3                        mov r8, r11
00A63943  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
00A63947  49 8B D2                        mov rdx, r10
00A6394A  49 8B CB                        mov rcx, r11
00A6394D  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00A63951  E8 4A 16 E6 FF                  call 0x1408c4fa0
00A63956  48 83 C4 48                     add rsp, 0x48
00A6395A  C3                              ret
00A6395B  CC                              int3
00A6395C  4D 89 10                        mov qword ptr [r8], r10
00A6395F  48 89 02                        mov qword ptr [rdx], rax
00A63962  EB F2                           jmp 0x140a63956
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PspPropagateHandle(unsigned __int8 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int8 v_stack_m10;
    unsigned int v_stack_m18;
    unsigned int v_stack_m20;
    unsigned int v_stack_m28;

    v_rsp = (v_rsp) - (72);
    result = 0;
    if (a1 == 0) goto loc_00A6395C;
    v_stack_m10 = 0;
    v_stack_m18 = 2;
    v_stack_m20 = 0;
    v_stack_m28 = 0;
    result = ObDuplicateObject(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), *(unsigned __int64 *)(a2), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), a3);
loc_00A63956:
    v_rsp = (v_rsp) + (72);
    return result;
loc_00A6395C:
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184)) = *(unsigned __int64 *)(a2);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2)) = result;
    goto loc_00A63956;
}
```

## 5. (Beta) C Style

```c
int64_t PspPropagateHandle(uint8_t Arg1, void *Arg2, void *Arg3)
{
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_rsp;
    uint8_t v_stack_m10;
    uint32_t v_stack_m18;
    uint32_t v_stack_m20;
    uint32_t v_stack_m28;

    local_rsp = (local_rsp) - (72);
    result = 0;
    if (Arg1 == 0) goto loc_00A6395C;
    v_stack_m10 = 0;
    v_stack_m18 = 2;
    v_stack_m20 = 0;
    v_stack_m28 = 0;
    result = ObDuplicateObject(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), *(uint64_t *)(arg2), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), Arg3);
loc_00A63956:
    local_rsp = (local_rsp) + (72);
    return result;
loc_00A6395C:
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8)) = *(uint64_t *)(arg2);
    *(uint64_t *)(*(uint64_t *)(arg2)) = result;
    goto loc_00A63956;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `64` | `R` |
| `Arg2` | `+ 0x0` | `64` | `W` |
| `Arg3` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A63914&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A63914[BB_00A63914]
  bb_00A63931[BB_00A63931]
  bb_00A63956[BB_00A63956]
  bb_00A6395B[BB_00A6395B]
  bb_00A6395C[BB_00A6395C]
  bb_00A63914 -->|branch| bb_00A6395C
  bb_00A63914 -->|fallthrough| bb_00A63931
  bb_00A63931 -->|flow| bb_00A63956
  bb_00A6395B -->|flow| bb_00A6395C
  bb_00A6395C -->|branch| bb_00A63956
```
