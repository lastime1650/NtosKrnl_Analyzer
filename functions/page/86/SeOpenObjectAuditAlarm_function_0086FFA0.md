# SeOpenObjectAuditAlarm

- RVA: `0x0086FFA0`–`0x0086FFFA` (길이 `90` bytes)
- VA: `0x000000014086FFA0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006C2A4`
- 디코드: `18`개 명령, `90/90` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0086FFEF` → [SeOpenObjectAuditAlarmWithTransaction](SeOpenObjectAuditAlarmWithTransaction_function_0086E790.md) (function, `0x0086E790`)

### Direct callers
- [IopCreateSecurityCheck](../../text/3A/IopCreateSecurityCheck_function_003A5DA0.md) at `0x003A5EC4`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0086FFA0  48 83 EC 58                     sub rsp, 0x58
0086FFA4  0F B6 84 24 98 00 00 00         movzx eax, byte ptr [rsp + 0x98]
0086FFAC  84 C0                           test al, al
0086FFAE  74 44                           je 0x14086fff4
0086FFB0  4C 8B 94 24 A0 00 00 00         mov r10, qword ptr [rsp + 0xa0]
0086FFB8  4C 89 54 24 48                  mov qword ptr [rsp + 0x48], r10
0086FFBD  48 C7 44 24 40 00 00 00 00      mov qword ptr [rsp + 0x40], 0
0086FFC6  88 44 24 38                     mov byte ptr [rsp + 0x38], al
0086FFCA  0F B6 84 24 90 00 00 00         movzx eax, byte ptr [rsp + 0x90]
0086FFD2  88 44 24 30                     mov byte ptr [rsp + 0x30], al
0086FFD6  0F B6 84 24 88 00 00 00         movzx eax, byte ptr [rsp + 0x88]
0086FFDE  88 44 24 28                     mov byte ptr [rsp + 0x28], al
0086FFE2  48 8B 84 24 80 00 00 00         mov rax, qword ptr [rsp + 0x80]
0086FFEA  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0086FFEF  E8 9C E7 FF FF                  call 0x14086e790
0086FFF4  48 83 C4 58                     add rsp, 0x58
0086FFF8  C3                              ret
0086FFF9  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SeOpenObjectAuditAlarm(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, unsigned __int8 a6, unsigned __int8 a7, unsigned __int8 a8, __int64 a9)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned __int64 v_stack_m18;
    unsigned __int8 v_stack_m20;
    unsigned __int8 v_stack_m28;
    unsigned __int8 v_stack_m30;
    unsigned __int64 v_stack_m38;

    v_rsp = (v_rsp) - (88);
    result = a8;
    if (a8 != 0) {
        v_r10 = a9;
        v_stack_m10 = v_r10;
        v_stack_m18 = 0;
        v_stack_m20 = a8;
        result = a7;
        v_stack_m28 = (unsigned __int8)(result);
        result = a6;
        v_stack_m30 = (unsigned __int8)(result);
        result = a5;
        v_stack_m38 = result;
        result = SeOpenObjectAuditAlarmWithTransaction(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (88);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t SeOpenObjectAuditAlarm(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5, uint8_t Arg6, uint8_t Arg7, uint8_t Arg8, int64_t Arg9)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint64_t v_stack_m18;
    uint8_t v_stack_m20;
    uint8_t v_stack_m28;
    uint8_t v_stack_m30;
    uint64_t v_stack_m38;

    local_rsp = (local_rsp) - (88);
    result = Arg8;
    if (Arg8 != 0) {
        local_r10 = Arg9;
        v_stack_m10 = local_r10;
        v_stack_m18 = 0;
        v_stack_m20 = Arg8;
        result = Arg7;
        v_stack_m28 = (uint8_t)(result);
        result = Arg6;
        v_stack_m30 = (uint8_t)(result);
        result = Arg5;
        v_stack_m38 = result;
        result = SeOpenObjectAuditAlarmWithTransaction(Arg1, Arg2, Arg3, Arg4);
    }
    local_rsp = (local_rsp) + (88);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0086FFA0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0086FFA0[BB_0086FFA0]
  bb_0086FFB0[BB_0086FFB0]
  bb_0086FFF4[BB_0086FFF4]
  bb_0086FFF9[BB_0086FFF9]
  bb_0086FFA0 -->|branch| bb_0086FFF4
  bb_0086FFA0 -->|fallthrough| bb_0086FFB0
  bb_0086FFB0 -->|flow| bb_0086FFF4
```
