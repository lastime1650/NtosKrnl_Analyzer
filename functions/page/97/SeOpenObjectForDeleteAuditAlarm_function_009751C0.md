# SeOpenObjectForDeleteAuditAlarm

- RVA: `0x009751C0`–`0x00975219` (길이 `89` bytes)
- VA: `0x00000001409751C0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00096558`
- 디코드: `19`개 명령, `89/89` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00975212` → [SeOpenObjectForDeleteAuditAlarmWithTransaction](SeOpenObjectForDeleteAuditAlarmWithTransaction_function_00973EC0.md) (function, `0x00973EC0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009751C0  48 83 EC 58                     sub rsp, 0x58
009751C4  44 8A 94 24 98 00 00 00         mov r10b, byte ptr [rsp + 0x98]
009751CC  45 84 D2                        test r10b, r10b
009751CF  75 06                           jne 0x1409751d7
009751D1  48 83 C4 58                     add rsp, 0x58
009751D5  C3                              ret
009751D6  CC                              int3
009751D7  48 8B 84 24 A0 00 00 00         mov rax, qword ptr [rsp + 0xa0]
009751DF  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
009751E4  48 83 64 24 40 00               and qword ptr [rsp + 0x40], 0
009751EA  8A 84 24 90 00 00 00            mov al, byte ptr [rsp + 0x90]
009751F1  44 88 54 24 38                  mov byte ptr [rsp + 0x38], r10b
009751F6  88 44 24 30                     mov byte ptr [rsp + 0x30], al
009751FA  8A 84 24 88 00 00 00            mov al, byte ptr [rsp + 0x88]
00975201  88 44 24 28                     mov byte ptr [rsp + 0x28], al
00975205  48 8B 84 24 80 00 00 00         mov rax, qword ptr [rsp + 0x80]
0097520D  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00975212  E8 A9 EC FF FF                  call 0x140973ec0
00975217  EB B8                           jmp 0x1409751d1
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SeOpenObjectForDeleteAuditAlarm(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, unsigned __int8 a6, unsigned __int8 a7, unsigned __int8 a8, __int64 a9)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p20;
    unsigned __int8 v_stack_p28;
    unsigned __int8 v_stack_p30;
    unsigned __int8 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p48;

    v_rsp = (v_rsp) - (88);
    if (a8 != 0) goto loc_009751D7;
loc_009751D1:
    v_rsp = (v_rsp) + (88);
    return result;
loc_009751D7:
    v_stack_p48 = a9;
    v_stack_p38 = a8;
    v_stack_p30 = a7;
    v_stack_p28 = a6;
    v_stack_p20 = a5;
    result = SeOpenObjectForDeleteAuditAlarmWithTransaction(a1, a2, a3, a4);
    goto loc_009751D1;
}
```

## 5. (Beta) C Style

```c
int64_t SeOpenObjectForDeleteAuditAlarm(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5, uint8_t Arg6, uint8_t Arg7, uint8_t Arg8, int64_t Arg9)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p20;
    uint8_t v_stack_p28;
    uint8_t v_stack_p30;
    uint8_t v_stack_p38;
    uint64_t v_stack_p40;
    uint64_t v_stack_p48;

    local_rsp = (local_rsp) - (88);
    if (Arg8 != 0) goto loc_009751D7;
loc_009751D1:
    local_rsp = (local_rsp) + (88);
    return result;
loc_009751D7:
    v_stack_p48 = Arg9;
    v_stack_p38 = Arg8;
    v_stack_p30 = Arg7;
    v_stack_p28 = Arg6;
    v_stack_p20 = Arg5;
    result = SeOpenObjectForDeleteAuditAlarmWithTransaction(Arg1, Arg2, Arg3, Arg4);
    goto loc_009751D1;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009751C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_009751C0[BB_009751C0]
  bb_009751D1[BB_009751D1]
  bb_009751D6[BB_009751D6]
  bb_009751D7[BB_009751D7]
  bb_009751C0 -->|branch| bb_009751D7
  bb_009751C0 -->|fallthrough| bb_009751D1
  bb_009751D6 -->|flow| bb_009751D7
  bb_009751D7 -->|branch| bb_009751D1
```
