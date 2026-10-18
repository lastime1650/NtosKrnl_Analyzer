# HvlpWriteEventLog

- RVA: `0x0058C9E4`–`0x0058CA20` (길이 `60` bytes)
- VA: `0x000000014058C9E4`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00063458`
- 디코드: `16`개 명령, `60/60` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0058CA15` → [EtwWriteEx](../25/EtwWriteEx_function_0025F0D0.md) (function, `0x0025F0D0`)

### Direct callers
- [HvlPhase2Initialize](HvlPhase2Initialize_function_00583EA0.md) at `0x00583F80`
- [HvlPhase2Initialize](HvlPhase2Initialize_function_00583EA0.md) at `0x00584014`
- [HvlPhase2Initialize](HvlPhase2Initialize_function_00583EA0.md) at `0x0058403C`
- [HvlPhase2Initialize](HvlPhase2Initialize_function_00583EA0.md) at `0x0058409A`
- [HvlpCheckTscSync](HvlpCheckTscSync_function_0058C300.md) at `0x0058C412`
- [HvlpLogGuestStateScrubbingStatus](HvlpLogGuestStateScrubbingStatus_function_0058C48C.md) at `0x0058C637`
- [HvlpLogGuestStateScrubbingStatus](HvlpLogGuestStateScrubbingStatus_function_0058C48C.md) at `0x0058C6B0`
- [HvlpLogGuestStateScrubbingStatus](HvlpLogGuestStateScrubbingStatus_function_0058C48C.md) at `0x0058C6EC`
- [HvlpLogIommuInitStatus](HvlpLogIommuInitStatus_function_0058C724.md) at `0x0058C896`
- [HvlpLogIommuInitStatus](HvlpLogIommuInitStatus_function_0058C724.md) at `0x0058C8C3`
- [HvlpLogIommuInitStatus](HvlpLogIommuInitStatus_function_0058C724.md) at `0x0058C8EB`
- [HvlpLogProcessorStartupFailure](HvlpLogProcessorStartupFailure_function_0058C91C.md) at `0x0058C9C2`

### Static image references
- `0x0058C9EB` → RVA `0x00E65E38` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0058C9E4  48 83 EC 48                     sub rsp, 0x48
0058C9E8  48 8B C1                        mov rax, rcx
0058C9EB  48 8B 0D 46 94 8D 00            mov rcx, qword ptr [rip + 0x8d9446]
0058C9F2  48 85 C9                        test rcx, rcx
0058C9F5  74 23                           je 0x14058ca1a
0058C9F7  4C 89 44 24 38                  mov qword ptr [rsp + 0x38], r8
0058C9FC  45 33 C9                        xor r9d, r9d
0058C9FF  89 54 24 30                     mov dword ptr [rsp + 0x30], edx
0058CA03  45 33 C0                        xor r8d, r8d
0058CA06  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
0058CA0C  48 8B D0                        mov rdx, rax
0058CA0F  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
0058CA15  E8 B6 26 CD FF                  call 0x14025f0d0
0058CA1A  48 83 C4 48                     add rsp, 0x48
0058CA1E  C3                              ret
0058CA1F  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HvlpWriteEventLog(__int64 a1, int a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned int v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;

    v_rsp = (v_rsp) - (72);
    result = a1;
    if (*(unsigned __int64 *)(v_rip + 9278534) != 0) {
        v_stack_m10 = a3;
        a4 = 0;
        v_stack_m18 = a2;
        a3 = 0;
        a2 = a1;
        result = EtwWriteEx(*(unsigned __int64 *)(v_rip + 9278534), a2, a3, a4);
    }
    v_rsp = (v_rsp) + (72);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HvlpWriteEventLog(int64_t Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint32_t v_stack_m18;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;

    local_rsp = (local_rsp) - (72);
    result = Arg1;
    if (*(uint64_t *)(v_rip + 0x8D9446) != 0) {
        v_stack_m10 = Arg3;
        Arg4 = 0;
        v_stack_m18 = Arg2;
        Arg3 = 0;
        Arg2 = Arg1;
        result = EtwWriteEx(*(uint64_t *)(v_rip + 0x8D9446), Arg2, Arg3, Arg4);
    }
    local_rsp = (local_rsp) + (72);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0058C9E4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0058C9E4[BB_0058C9E4]
  bb_0058C9F7[BB_0058C9F7]
  bb_0058CA1A[BB_0058CA1A]
  bb_0058CA1F[BB_0058CA1F]
  bb_0058C9E4 -->|branch| bb_0058CA1A
  bb_0058C9E4 -->|fallthrough| bb_0058C9F7
  bb_0058C9F7 -->|flow| bb_0058CA1A
```
