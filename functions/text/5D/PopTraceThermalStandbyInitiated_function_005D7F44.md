# PopTraceThermalStandbyInitiated

- RVA: `0x005D7F44`–`0x005D7FD8` (길이 `148` bytes)
- VA: `0x00000001405D7F44`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000986E4`
- 디코드: `31`개 명령, `148/148` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x005D7F75` → [tlgKeywordOn](../42/tlgKeywordOn_function_0042EAA0.md) (function, `0x0042EAA0`)
- `0x005D7FC0` → [tlgWriteTransfer_EtwWriteTransfer](../42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x005D7FCD` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PopThermalCsEntry](../42/PopThermalCsEntry_function_0042FE14.md) at `0x0042FE92`

### Static image references
- `0x005D7F48` → RVA `0x00E0A740` (`.data`; read)
- `0x005D7F57` → RVA `0x00E07748` (`.data`; read)
- `0x005D7F8D` → RVA `0x0004AF1E` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005D7F44  48 83 EC 78                     sub rsp, 0x78
005D7F48  48 8B 05 F1 27 83 00            mov rax, qword ptr [rip + 0x8327f1]
005D7F4F  48 33 C4                        xor rax, rsp
005D7F52  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
005D7F57  83 3D EA F7 82 00 05            cmp dword ptr [rip + 0x82f7ea], 5
005D7F5E  44 0F B6 C1                     movzx r8d, cl
005D7F62  76 61                           jbe 0x1405d7fc5
005D7F64  48 BA 00 00 00 00 00 40 00 00   movabs rdx, 0x400000000000
005D7F6E  48 8D 0D D3 F7 82 00            lea rcx, [rip + 0x82f7d3]
005D7F75  E8 26 6B E5 FF                  call 0x14042eaa0
005D7F7A  84 C0                           test al, al
005D7F7C  74 47                           je 0x1405d7fc5
005D7F7E  83 64 24 64 00                  and dword ptr [rsp + 0x64], 0
005D7F83  48 8D 44 24 30                  lea rax, [rsp + 0x30]
005D7F88  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
005D7F8D  48 8D 15 8A 2F A7 FF            lea rdx, [rip - 0x58d076]
005D7F94  48 8D 44 24 38                  lea rax, [rsp + 0x38]
005D7F99  44 89 44 24 30                  mov dword ptr [rsp + 0x30], r8d
005D7F9E  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
005D7FA3  48 8D 0D 9E F7 82 00            lea rcx, [rip + 0x82f79e]
005D7FAA  45 33 C9                        xor r9d, r9d
005D7FAD  C7 44 24 20 03 00 00 00         mov dword ptr [rsp + 0x20], 3
005D7FB5  45 33 C0                        xor r8d, r8d
005D7FB8  C7 44 24 60 04 00 00 00         mov dword ptr [rsp + 0x60], 4
005D7FC0  E8 1B E1 E4 FF                  call 0x1404260e0
005D7FC5  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
005D7FCA  48 33 CC                        xor rcx, rsp
005D7FCD  E8 6E 46 0D 00                  call 0x1406ac640
005D7FD2  48 83 C4 78                     add rsp, 0x78
005D7FD6  C3                              ret
005D7FD7  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopTraceThermalStandbyInitiated(unsigned __int8 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned int v_stack_m14;
    unsigned int v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned int v_stack_m58;

    v_rsp = (v_rsp) - (120);
    result = (*(unsigned __int64 *)(v_rip + 8595441)) ^ (v_rsp);
    v_stack_m10 = result;
    if ((*(unsigned int *)(v_rip + 8583146)) <= 5) goto loc_005D7FC5;
    result = tlgKeywordOn(v_rip + 8583123, a2, a1, a4);
    if ((unsigned __int8)(result) != 0) {
        result = v_stack_m48;
        v_stack_m20 = result;
        a2 = v_rip - 5820534;
        result = v_stack_m40;
        v_stack_m48 = a1;
        v_stack_m50 = result;
        a1 = v_rip + 8583070;
        a4 = 0;
        v_stack_m58 = 3;
        a3 = 0;
        v_stack_m18 = 4;
        result = tlgWriteTransfer_EtwWriteTransfer(a1, a2, a3, a4);
    }
    a1 = (v_stack_m10) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (120);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopTraceThermalStandbyInitiated(uint8_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint32_t v_stack_m14;
    uint32_t v_stack_m18;
    uint64_t v_stack_m20;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint32_t v_stack_m58;

    local_rsp = (local_rsp) - (120);
    result = (*(uint64_t *)(v_rip + 0x8327F1)) ^ (local_rsp);
    v_stack_m10 = result;
    if ((*(uint32_t *)(v_rip + 0x82F7EA)) <= 5) goto loc_005D7FC5;
    result = tlgKeywordOn(v_rip + 8583123, Arg2, Arg1, Arg4);
    if ((uint8_t)(result) != 0) {
        result = v_stack_m48;
        v_stack_m20 = result;
        Arg2 = v_rip - 5820534;
        result = v_stack_m40;
        v_stack_m48 = Arg1;
        v_stack_m50 = result;
        Arg1 = v_rip + 8583070;
        Arg4 = 0;
        v_stack_m58 = 3;
        Arg3 = 0;
        v_stack_m18 = 4;
        result = tlgWriteTransfer_EtwWriteTransfer(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (v_stack_m10) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (120);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005D7F44&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005D7F44[BB_005D7F44]
  bb_005D7F64[BB_005D7F64]
  bb_005D7F7E[BB_005D7F7E]
  bb_005D7FC5[BB_005D7FC5]
  bb_005D7FD7[BB_005D7FD7]
  bb_005D7F44 -->|branch| bb_005D7FC5
  bb_005D7F44 -->|fallthrough| bb_005D7F64
  bb_005D7F64 -->|branch| bb_005D7FC5
  bb_005D7F64 -->|fallthrough| bb_005D7F7E
  bb_005D7F7E -->|flow| bb_005D7FC5
```
