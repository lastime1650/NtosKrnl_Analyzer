# PdcPortSendMessageSynchronously

- RVA: `0x0049A6B4`–`0x0049A71A` (길이 `102` bytes)
- VA: `0x000000014049A6B4`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006383C`
- 디코드: `29`개 명령, `102/102` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0049A6D0` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0049A6F1` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0049A6FB` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- [Pdcv2ActivationClientRenewActivation](../../page/79/Pdcv2ActivationClientRenewActivation_function_0079B0F0.md) at `0x0079B22A`
- [Pdcv2ActivationClientActivate](../../page/95/Pdcv2ActivationClientActivate_function_00953C70.md) at `0x00953EC6`
- [Pdcv2ActivationClientDeactivate](../../page/95/Pdcv2ActivationClientDeactivate_function_009552E0.md) at `0x009553FF`
- [sub_00B49A44](../../page/B4/Unknown_function_00B49A44.md) at `0x00B49A72`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0049A6B4  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0049A6B9  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
0049A6BE  57                              push rdi
0049A6BF  48 83 EC 20                     sub rsp, 0x20
0049A6C3  48 8D 79 08                     lea rdi, [rcx + 8]
0049A6C7  48 8B D9                        mov rbx, rcx
0049A6CA  48 8B CF                        mov rcx, rdi
0049A6CD  48 8B F2                        mov rsi, rdx
0049A6D0  E8 4B BF D7 FF                  call 0x140216620
0049A6D5  84 C0                           test al, al
0049A6D7  74 3A                           je 0x14049a713
0049A6D9  C7 46 2C 06 00 00 00            mov dword ptr [rsi + 0x2c], 6
0049A6E0  41 B8 20 03 00 00               mov r8d, 0x320
0049A6E6  48 8B 43 28                     mov rax, qword ptr [rbx + 0x28]
0049A6EA  48 8B D6                        mov rdx, rsi
0049A6ED  48 8B 4B 18                     mov rcx, qword ptr [rbx + 0x18]
0049A6F1  E8 DA 03 22 00                  call 0x1406baad0
0049A6F6  48 8B CF                        mov rcx, rdi
0049A6F9  8B D8                           mov ebx, eax
0049A6FB  E8 80 F7 EA FF                  call 0x140349e80
0049A700  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
0049A705  8B C3                           mov eax, ebx
0049A707  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
0049A70C  48 83 C4 20                     add rsp, 0x20
0049A710  5F                              pop rdi
0049A711  C3                              ret
0049A712  CC                              int3
0049A713  BB 89 01 00 C0                  mov ebx, 0xc0000189
0049A718  EB E6                           jmp 0x14049a700
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PdcPortSendMessageSynchronously(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_rsp = (v_rsp) - (32);
    result = ExAcquireRundownProtection(a1 + 8, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0049A713;
    *(unsigned int *)(a2 + 44) = 6;
    result = guard_dispatch_icall(*(unsigned __int64 *)(a1 + 24), a2, 800, a4);
    result = ExReleaseRundownProtection(a1 + 8, a2, 800, a4);
loc_0049A700:
    v_rsp = (v_rsp) + (32);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
loc_0049A713:
    goto loc_0049A700;
}
```

## 5. (Beta) C Style

```c
int64_t PdcPortSendMessageSynchronously(void *Arg1, void *Arg2)
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
    result = ExAcquireRundownProtection(Arg1 + 8, Arg2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0049A713;
    *(uint32_t *)(arg2 + 0x2C) = 6;
    result = guard_dispatch_icall(*(uint64_t *)(arg1 + 0x18), Arg2, 800, a4);
    result = ExReleaseRundownProtection(Arg1 + 8, Arg2, 800, a4);
loc_0049A700:
    local_rsp = (local_rsp) + (32);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
loc_0049A713:
    goto loc_0049A700;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x28` | `64` | `R` |
| `Arg2` | `+ 0x2C` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0049A6B4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0049A6B4[BB_0049A6B4]
  bb_0049A6D9[BB_0049A6D9]
  bb_0049A700[BB_0049A700]
  bb_0049A712[BB_0049A712]
  bb_0049A713[BB_0049A713]
  bb_0049A6B4 -->|branch| bb_0049A713
  bb_0049A6B4 -->|fallthrough| bb_0049A6D9
  bb_0049A6D9 -->|flow| bb_0049A700
  bb_0049A712 -->|flow| bb_0049A713
  bb_0049A713 -->|branch| bb_0049A700
```
