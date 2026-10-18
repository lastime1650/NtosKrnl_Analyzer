# EtwpTraceNetwork

- RVA: `0x002356F0`–`0x0023576F` (길이 `127` bytes)
- VA: `0x00000001402356F0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000606C0`
- 디코드: `30`개 명령, `127/127` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00235735` → [EtwpNetProvTraceNetwork](EtwpNetProvTraceNetwork_function_00235778.md) (function, `0x00235778`)
- `0x00235756` → [EtwTraceKernelEvent](EtwTraceKernelEvent_function_00235350.md) (function, `0x00235350`)
- `0x00235763` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x002356F6` → RVA `0x00E0A740` (`.data`; read)
- `0x0023570C` → RVA `0x00FC6AA8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002356F0  40 53                           push rbx
002356F2  48 83 EC 50                     sub rsp, 0x50
002356F6  48 8B 05 43 50 BD 00            mov rax, qword ptr [rip + 0xbd5043]
002356FD  48 33 C4                        xor rax, rsp
00235700  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00235705  83 64 24 3C 00                  and dword ptr [rsp + 0x3c], 0
0023570A  8B D9                           mov ebx, ecx
0023570C  48 8B 05 95 13 D9 00            mov rax, qword ptr [rip + 0xd91395]
00235713  48 89 54 24 30                  mov qword ptr [rsp + 0x30], rdx
00235718  44 89 44 24 38                  mov dword ptr [rsp + 0x38], r8d
0023571D  48 05 CC 12 00 00               add rax, 0x12cc
00235723  74 15                           je 0x14023573a
00235725  F7 00 00 00 01 00               test dword ptr [rax], 0x10000
0023572B  74 0D                           je 0x14023573a
0023572D  0F B7 D3                        movzx edx, bx
00235730  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
00235735  E8 3E 00 00 00                  call 0x140235778
0023573A  44 0F B7 CB                     movzx r9d, bx
0023573E  C7 44 24 20 02 18 50 00         mov dword ptr [rsp + 0x20], 0x501802
00235746  BA 01 00 00 00                  mov edx, 1
0023574B  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
00235750  41 B8 00 00 01 00               mov r8d, 0x10000
00235756  E8 F5 FB FF FF                  call 0x140235350
0023575B  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00235760  48 33 CC                        xor rcx, rsp
00235763  E8 D8 6E 47 00                  call 0x1406ac640
00235768  48 83 C4 50                     add rsp, 0x50
0023576C  5B                              pop rbx
0023576D  C3                              ret
0023576E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwpTraceNetwork(int a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m1C;
    unsigned int v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m38;

    v_rsp = (v_rsp) - (80);
    result = (*(unsigned __int64 *)(v_rip + 12406851)) ^ (v_rsp);
    v_stack_m18 = result;
    v_stack_m28 = a2;
    v_stack_m20 = a3;
    result = (*(unsigned __int64 *)(v_rip + 14226325)) + (0x12CCULL);
    if (condition_is_equal) goto loc_0023573A;
    if (((*(unsigned int *)(result)) & (0x10000ULL)) != 0) {
        a2 = (unsigned __int16)((unsigned int)(a1));
        a1 = v_stack_m28;
        result = EtwpNetProvTraceNetwork(a1, a2, a3, a4);
    }
    v_stack_m38 = 0x501802ULL;
    result = EtwTraceKernelEvent(v_stack_m28, 1, (unsigned int)(0x10000ULL), (unsigned __int16)((unsigned int)(a1)));
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, 1, (unsigned int)(0x10000ULL), (unsigned __int16)((unsigned int)(a1)));
    v_rsp = (v_rsp) + (80);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t EtwpTraceNetwork(int32_t Arg1, int64_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint32_t v_stack_m1C;
    uint32_t v_stack_m20;
    uint64_t v_stack_m28;
    uint32_t v_stack_m38;

    local_rsp = (local_rsp) - (80);
    result = (*(uint64_t *)(v_rip + 0xBD5043)) ^ (local_rsp);
    v_stack_m18 = result;
    v_stack_m28 = Arg2;
    v_stack_m20 = Arg3;
    result = (*(uint64_t *)(v_rip + 0xD91395)) + (0x12CCULL);
    if (condition_is_equal) goto loc_0023573A;
    if (((*(uint32_t *)(result)) & (0x10000ULL)) != 0) {
        Arg2 = (uint16_t)((uint32_t)(Arg1));
        Arg1 = v_stack_m28;
        result = EtwpNetProvTraceNetwork(Arg1, Arg2, Arg3, a4);
    }
    v_stack_m38 = 0x501802ULL;
    result = EtwTraceKernelEvent(v_stack_m28, 1, (uint32_t)(0x10000ULL), (uint16_t)((uint32_t)(Arg1)));
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, 1, (uint32_t)(0x10000ULL), (uint16_t)((uint32_t)(Arg1)));
    local_rsp = (local_rsp) + (80);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002356F0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002356F0[BB_002356F0]
  bb_00235725[BB_00235725]
  bb_0023572D[BB_0023572D]
  bb_0023573A[BB_0023573A]
  bb_0023576E[BB_0023576E]
  bb_002356F0 -->|branch| bb_0023573A
  bb_002356F0 -->|fallthrough| bb_00235725
  bb_00235725 -->|branch| bb_0023573A
  bb_00235725 -->|fallthrough| bb_0023572D
  bb_0023572D -->|flow| bb_0023573A
```
