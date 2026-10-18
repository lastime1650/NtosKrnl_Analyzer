# PpmEventExitIdleState

- RVA: `0x002D1AC4`–`0x002D1B3A` (길이 `118` bytes)
- VA: `0x00000001402D1AC4`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006F860`
- 디코드: `25`개 명령, `118/118` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x002D1AEB` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x002D1B33` → [EtwTraceKernelEvent](../23/EtwTraceKernelEvent_function_00235350.md) (function, `0x00235350`)

### Direct callers
- [PpmIdleExecuteTransition](PpmIdleExecuteTransition_function_002D0A1C.md) at `0x002D0F71`

### Static image references
- `0x002D1AC8` → RVA `0x00E0A740` (`.data`; read)
- `0x002D1AD7` → RVA `0x00FC6B08` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002D1AC4  48 83 EC 58                     sub rsp, 0x58
002D1AC8  48 8B 05 71 8C B3 00            mov rax, qword ptr [rip + 0xb38c71]
002D1ACF  48 33 C4                        xor rax, rsp
002D1AD2  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
002D1AD7  F7 05 27 50 CF 00 00 80 00 00   test dword ptr [rip + 0xcf5027], 0x8000
002D1AE1  75 13                           jne 0x1402d1af6
002D1AE3  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
002D1AE8  48 33 CC                        xor rcx, rsp
002D1AEB  E8 50 AB 3D 00                  call 0x1406ac640
002D1AF0  48 83 C4 58                     add rsp, 0x58
002D1AF4  C3                              ret
002D1AF5  CC                              int3
002D1AF6  83 64 24 44 00                  and dword ptr [rsp + 0x44], 0
002D1AFB  48 8D 44 24 30                  lea rax, [rsp + 0x30]
002D1B00  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
002D1B04  41 B9 3A 12 00 00               mov r9d, 0x123a
002D1B0A  89 54 24 34                     mov dword ptr [rsp + 0x34], edx
002D1B0E  48 8D 4C 24 38                  lea rcx, [rsp + 0x38]
002D1B13  BA 01 00 00 00                  mov edx, 1
002D1B18  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
002D1B1D  41 B8 00 80 00 40               mov r8d, 0x40008000
002D1B23  C7 44 24 40 08 00 00 00         mov dword ptr [rsp + 0x40], 8
002D1B2B  C7 44 24 20 02 06 00 00         mov dword ptr [rsp + 0x20], 0x602
002D1B33  E8 18 38 F6 FF                  call 0x140235350
002D1B38  EB A9                           jmp 0x1402d1ae3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PpmEventExitIdleState(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p30;
    unsigned int v_stack_p34;
    unsigned __int64 v_stack_p38;
    unsigned int v_stack_p40;
    unsigned int v_stack_p44;

    v_rsp = (v_rsp) - (88);
    result = (*(unsigned __int64 *)(v_rip + 11766897)) ^ (v_rsp);
    v_stack_m10 = result;
    if (((*(unsigned int *)(v_rip + 13586471)) & (0x8000ULL)) != 0) goto loc_002D1AF6;
loc_002D1AE3:
    a1 = (v_stack_m10) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (88);
    return result;
loc_002D1AF6:
    v_stack_p30 = (unsigned int)(a1);
    v_stack_p34 = a2;
    v_stack_p38 = v_stack_p30;
    v_stack_p40 = 8;
    v_stack_p20 = 0x602ULL;
    result = EtwTraceKernelEvent(v_stack_p38, 1, (unsigned int)(0x40008000ULL), (unsigned int)(0x123AULL));
    goto loc_002D1AE3;
}
```

## 5. (Beta) C Style

```c
int64_t PpmEventExitIdleState(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint32_t v_stack_p20;
    uint64_t v_stack_p30;
    uint32_t v_stack_p34;
    uint64_t v_stack_p38;
    uint32_t v_stack_p40;
    uint32_t v_stack_p44;

    local_rsp = (local_rsp) - (88);
    result = (*(uint64_t *)(v_rip + 0xB38C71)) ^ (local_rsp);
    v_stack_m10 = result;
    if (((*(uint32_t *)(v_rip + 0xCF5027)) & (0x8000ULL)) != 0) goto loc_002D1AF6;
loc_002D1AE3:
    Arg1 = (v_stack_m10) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, a3, a4);
    local_rsp = (local_rsp) + (88);
    return result;
loc_002D1AF6:
    v_stack_p30 = (uint32_t)(Arg1);
    v_stack_p34 = Arg2;
    v_stack_p38 = v_stack_p30;
    v_stack_p40 = 8;
    v_stack_p20 = 0x602ULL;
    result = EtwTraceKernelEvent(v_stack_p38, 1, (uint32_t)(0x40008000ULL), (uint32_t)(0x123AULL));
    goto loc_002D1AE3;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002D1AC4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002D1AC4[BB_002D1AC4]
  bb_002D1AE3[BB_002D1AE3]
  bb_002D1AF5[BB_002D1AF5]
  bb_002D1AF6[BB_002D1AF6]
  bb_002D1AC4 -->|branch| bb_002D1AF6
  bb_002D1AC4 -->|fallthrough| bb_002D1AE3
  bb_002D1AF5 -->|flow| bb_002D1AF6
  bb_002D1AF6 -->|branch| bb_002D1AE3
```
