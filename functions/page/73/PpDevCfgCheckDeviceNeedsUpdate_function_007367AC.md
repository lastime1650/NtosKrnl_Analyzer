# PpDevCfgCheckDeviceNeedsUpdate

- RVA: `0x007367AC`–`0x0073681E` (길이 `114` bytes)
- VA: `0x00000001407367AC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00087D9C`
- 디코드: `32`개 명령, `114/114` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x007367D2` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x007367E2` → [PiDevCfgInitDeviceContext](../97/PiDevCfgInitDeviceContext_function_00977518.md) (function, `0x00977518`)
- `0x007367F5` → [PiDevCfgCheckDeviceNeedsUpdate](PiDevCfgCheckDeviceNeedsUpdate_function_00731DDC.md) (function, `0x00731DDC`)
- `0x00736801` → [PiDevCfgFreeDeviceContext](../70/PiDevCfgFreeDeviceContext_function_00704A00.md) (function, `0x00704A00`)

### Direct callers
- [PiProcessNewDeviceNode](../A2/PiProcessNewDeviceNode_function_00A28F20.md) at `0x00A29F8D`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x007367D2` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007367AC  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
007367B1  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
007367B6  57                              push rdi
007367B7  48 81 EC 80 00 00 00            sub rsp, 0x80
007367BE  48 8B DA                        mov rbx, rdx
007367C1  49 8B F0                        mov rsi, r8
007367C4  33 D2                           xor edx, edx
007367C6  48 8B F9                        mov rdi, rcx
007367C9  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
007367CE  44 8D 42 58                     lea r8d, [rdx + 0x58]
007367D2  E8 69 04 F9 FF                  call 0x1406c6c40
007367D7  4C 8D 44 24 20                  lea r8, [rsp + 0x20]
007367DC  48 8B D3                        mov rdx, rbx
007367DF  48 8B CF                        mov rcx, rdi
007367E2  E8 31 0D 24 00                  call 0x140977518
007367E7  8B D8                           mov ebx, eax
007367E9  85 C0                           test eax, eax
007367EB  78 0F                           js 0x1407367fc
007367ED  48 8B D6                        mov rdx, rsi
007367F0  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
007367F5  E8 E2 B5 FF FF                  call 0x140731ddc
007367FA  8B D8                           mov ebx, eax
007367FC  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00736801  E8 FA E1 FC FF                  call 0x140704a00
00736806  4C 8D 9C 24 80 00 00 00         lea r11, [rsp + 0x80]
0073680E  8B C3                           mov eax, ebx
00736810  49 8B 5B 10                     mov rbx, qword ptr [r11 + 0x10]
00736814  49 8B 73 18                     mov rsi, qword ptr [r11 + 0x18]
00736818  49 8B E3                        mov rsp, r11
0073681B  5F                              pop rdi
0073681C  C3                              ret
0073681D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PpDevCfgCheckDeviceNeedsUpdate(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m8;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_rsp = (v_rsp) - (128);
    a2 = 0;
    result = memset(v_stack_m68, a2, a2 + 88, a4);
    result = PiDevCfgInitDeviceContext(a1, 0, v_stack_m68, a4);
    v_rbx = (unsigned int)((unsigned int)(result));
    if (!(sign_flag)) {
        a2 = a3;
        a1 = v_stack_m68;
        result = PiDevCfgCheckDeviceNeedsUpdate(a1, a2, v_stack_m68, a4);
        v_rbx = (unsigned int)(result);
    }
    result = PiDevCfgFreeDeviceContext(v_stack_m68, a2, v_stack_m68, a4);
    return (unsigned int)((unsigned int)(v_rbx));
}
```

## 5. (Beta) C Style

```c
int64_t PpDevCfgCheckDeviceNeedsUpdate(int64_t Arg1, int64_t Arg2, int64_t Arg3)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m68;
    uint64_t v_stack_m8;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    local_rsp = (local_rsp) - (128);
    Arg2 = 0;
    result = memset(v_stack_m68, Arg2, Arg2 + 88, a4);
    result = PiDevCfgInitDeviceContext(Arg1, 0, v_stack_m68, a4);
    local_rbx = (uint32_t)((uint32_t)(result));
    if (!(sign_flag)) {
        Arg2 = Arg3;
        Arg1 = v_stack_m68;
        result = PiDevCfgCheckDeviceNeedsUpdate(Arg1, Arg2, v_stack_m68, a4);
        local_rbx = (uint32_t)(result);
    }
    result = PiDevCfgFreeDeviceContext(v_stack_m68, Arg2, v_stack_m68, a4);
    return (uint32_t)((uint32_t)(local_rbx));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007367AC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007367AC[BB_007367AC]
  bb_007367ED[BB_007367ED]
  bb_007367FC[BB_007367FC]
  bb_0073681D[BB_0073681D]
  bb_007367AC -->|branch| bb_007367FC
  bb_007367AC -->|fallthrough| bb_007367ED
  bb_007367ED -->|flow| bb_007367FC
```
