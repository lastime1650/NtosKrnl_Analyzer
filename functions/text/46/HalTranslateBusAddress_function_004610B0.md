# HalTranslateBusAddress

- RVA: `0x004610B0`–`0x004610E6` (길이 `54` bytes)
- VA: `0x00000001404610B0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A82A0`
- 디코드: `15`개 명령, `54/54` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x004610DF` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [IopTranslateBusAddress](../../page/72/IopTranslateBusAddress_function_0072F598.md) at `0x0072F5D8`
- [HeadlessTerminalAddResources](../../page/7C/HeadlessTerminalAddResources_function_007C7414.md) at `0x007C74CA`
- [HalpReportResourceUsage](../../init/C1/HalpReportResourceUsage_function_00C1F034.md) at `0x00C1F38F`

### Static image references
- `0x004610D3` → RVA `0x00E00828` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004610B0  48 83 EC 38                     sub rsp, 0x38
004610B4  83 F9 05                        cmp ecx, 5
004610B7  74 10                           je 0x1404610c9
004610B9  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
004610BE  4C 89 00                        mov qword ptr [rax], r8
004610C1  B0 01                           mov al, 1
004610C3  48 83 C4 38                     add rsp, 0x38
004610C7  C3                              ret
004610C8  CC                              int3
004610C9  4C 8B 54 24 60                  mov r10, qword ptr [rsp + 0x60]
004610CE  B9 05 00 00 00                  mov ecx, 5
004610D3  48 8B 05 4E F7 99 00            mov rax, qword ptr [rip + 0x99f74e]
004610DA  4C 89 54 24 20                  mov qword ptr [rsp + 0x20], r10
004610DF  E8 EC 99 25 00                  call 0x1406baad0
004610E4  EB DD                           jmp 0x1404610c3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalTranslateBusAddress(int a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p20;

    v_rsp = (v_rsp) - (56);
    if (a1 == 5) goto loc_004610C9;
    *(unsigned __int64 *)(a5) = a3;
loc_004610C3:
    v_rsp = (v_rsp) + (56);
    return 1;
loc_004610C9:
    v_stack_p20 = a5;
    result = guard_dispatch_icall(5, a2, a3, a4);
    goto loc_004610C3;
}
```

## 5. (Beta) C Style

```c
int64_t HalTranslateBusAddress(int32_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, void *Arg5)
{
    uint8_t *arg5 = (uint8_t *)Arg5;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p20;

    local_rsp = (local_rsp) - (56);
    if (Arg1 == 5) goto loc_004610C9;
    *(uint64_t *)(arg5) = Arg3;
loc_004610C3:
    local_rsp = (local_rsp) + (56);
    return 1;
loc_004610C9:
    v_stack_p20 = Arg5;
    result = guard_dispatch_icall(5, Arg2, Arg3, Arg4);
    goto loc_004610C3;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg5` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004610B0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004610B0[BB_004610B0]
  bb_004610B9[BB_004610B9]
  bb_004610C3[BB_004610C3]
  bb_004610C8[BB_004610C8]
  bb_004610C9[BB_004610C9]
  bb_004610B0 -->|branch| bb_004610C9
  bb_004610B0 -->|fallthrough| bb_004610B9
  bb_004610B9 -->|flow| bb_004610C3
  bb_004610C8 -->|flow| bb_004610C9
  bb_004610C9 -->|branch| bb_004610C3
```
