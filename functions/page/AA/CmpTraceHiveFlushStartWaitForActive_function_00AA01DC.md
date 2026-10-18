# CmpTraceHiveFlushStartWaitForActive

- RVA: `0x00AA01DC`–`0x00AA0241` (길이 `101` bytes)
- VA: `0x0000000140AA01DC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060904`
- 디코드: `23`개 명령, `101/101` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00AA0208` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x00AA0229` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (function, `0x0041C720`)
- `0x00AA0236` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [CmpWaitOnHiveWriteQueue](CmpWaitOnHiveWriteQueue_function_00AA0110.md) at `0x00AA0163`

### Static image references
- `0x00AA01E0` → RVA `0x00E0A740` (`.data`; read)
- `0x00AA01EF` → RVA `0x0001C780` (`.rdata`; read)
- `0x00AA01F6` → RVA `0x00FD8018` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00AA0208` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (`PAGE` → `.text`)
  - `0x00AA0229` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (`PAGE` → `.text`)
  - `0x00AA0236` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AA01DC  48 83 EC 58                     sub rsp, 0x58
00AA01E0  48 8B 05 59 A5 36 00            mov rax, qword ptr [rip + 0x36a559]
00AA01E7  48 33 C4                        xor rax, rsp
00AA01EA  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00AA01EF  0F 10 05 8A C5 57 FF            movups xmm0, xmmword ptr [rip - 0xa83a76]
00AA01F6  48 8B 0D 1B 7E 53 00            mov rcx, qword ptr [rip + 0x537e1b]
00AA01FD  48 8D 54 24 30                  lea rdx, [rsp + 0x30]
00AA0202  F3 0F 7F 44 24 30               movdqu xmmword ptr [rsp + 0x30], xmm0
00AA0208  E8 43 22 8F FF                  call 0x140392450
00AA020D  84 C0                           test al, al
00AA020F  74 1D                           je 0x140aa022e
00AA0211  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
00AA0217  48 8D 54 24 30                  lea rdx, [rsp + 0x30]
00AA021C  48 8B 0D F5 7D 53 00            mov rcx, qword ptr [rip + 0x537df5]
00AA0223  45 33 C9                        xor r9d, r9d
00AA0226  45 33 C0                        xor r8d, r8d
00AA0229  E8 F2 C4 97 FF                  call 0x14041c720
00AA022E  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AA0233  48 33 CC                        xor rcx, rsp
00AA0236  E8 05 C4 C0 FF                  call 0x1406ac640
00AA023B  48 83 C4 58                     add rsp, 0x58
00AA023F  C3                              ret
00AA0240  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpTraceHiveFlushStartWaitForActive(__int64 a1, __int64 a2, int a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;

    v_rsp = (v_rsp) - (88);
    result = (*(unsigned __int64 *)(v_rip + 3581273)) ^ (v_rsp);
    v_stack_m18 = result;
    v_stack_m28 = v_xmm0;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 5471771), v_stack_m28, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        a2 = v_stack_m28;
        a1 = *(unsigned __int64 *)(v_rip + 5471733);
        a4 = 0;
        a3 = 0;
        result = EtwWrite(a1, a2, a3, a4);
    }
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (88);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CmpTraceHiveFlushStartWaitForActive(int64_t Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;

    local_rsp = (local_rsp) - (88);
    result = (*(uint64_t *)(v_rip + 0x36A559)) ^ (local_rsp);
    v_stack_m18 = result;
    v_stack_m28 = v_xmm0;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x537E1B), v_stack_m28, Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        Arg2 = v_stack_m28;
        Arg1 = *(uint64_t *)(v_rip + 0x537DF5);
        Arg4 = 0;
        Arg3 = 0;
        result = EtwWrite(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (88);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AA01DC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00AA01DC[BB_00AA01DC]
  bb_00AA0211[BB_00AA0211]
  bb_00AA022E[BB_00AA022E]
  bb_00AA0240[BB_00AA0240]
  bb_00AA01DC -->|branch| bb_00AA022E
  bb_00AA01DC -->|fallthrough| bb_00AA0211
  bb_00AA0211 -->|flow| bb_00AA022E
```
