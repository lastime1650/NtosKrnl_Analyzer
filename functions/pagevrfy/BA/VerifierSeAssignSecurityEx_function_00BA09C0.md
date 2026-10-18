# VerifierSeAssignSecurityEx

- RVA: `0x00BA09C0`–`0x00BA0A1D` (길이 `93` bytes)
- VA: `0x0000000140BA09C0`
- 실행 섹션: `PAGEVRFY`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006C2A4`
- 디코드: `18`개 명령, `93/93` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00BA0A12` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00BA09D7` → RVA `0x00FFEDD8` (`PAGEVRFD`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00BA0A12` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGEVRFY` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BA09C0  48 83 EC 58                     sub rsp, 0x58
00BA09C4  44 8B 94 24 A0 00 00 00         mov r10d, dword ptr [rsp + 0xa0]
00BA09CC  4D 8B D9                        mov r11, r9
00BA09CF  44 8A 8C 24 80 00 00 00         mov r9b, byte ptr [rsp + 0x80]
00BA09D7  48 8B 05 FA E3 45 00            mov rax, qword ptr [rip + 0x45e3fa]
00BA09DE  44 89 54 24 40                  mov dword ptr [rsp + 0x40], r10d
00BA09E3  4C 8B 94 24 98 00 00 00         mov r10, qword ptr [rsp + 0x98]
00BA09EB  4C 89 54 24 38                  mov qword ptr [rsp + 0x38], r10
00BA09F0  4C 8B 94 24 90 00 00 00         mov r10, qword ptr [rsp + 0x90]
00BA09F8  4C 89 54 24 30                  mov qword ptr [rsp + 0x30], r10
00BA09FD  44 8B 94 24 88 00 00 00         mov r10d, dword ptr [rsp + 0x88]
00BA0A05  44 89 54 24 28                  mov dword ptr [rsp + 0x28], r10d
00BA0A0A  44 88 4C 24 20                  mov byte ptr [rsp + 0x20], r9b
00BA0A0F  4D 8B CB                        mov r9, r11
00BA0A12  E8 B9 A0 B1 FF                  call 0x1406baad0
00BA0A17  48 83 C4 58                     add rsp, 0x58
00BA0A1B  C3                              ret
00BA0A1C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VerifierSeAssignSecurityEx(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned __int8 a5, unsigned int a6, __int64 a7, __int64 a8, unsigned int a9)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m30;
    unsigned __int8 v_stack_m38;

    v_rsp = (v_rsp) - (88);
    v_stack_m18 = (unsigned int)((unsigned int)(a9));
    v_stack_m20 = a8;
    v_stack_m28 = a7;
    v_stack_m30 = (unsigned int)((unsigned int)(a6));
    v_stack_m38 = a5;
    result = guard_dispatch_icall(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (88);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t VerifierSeAssignSecurityEx(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint8_t Arg5, uint32_t Arg6, int64_t Arg7, int64_t Arg8, uint32_t Arg9)
{
    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_m18;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;
    uint32_t v_stack_m30;
    uint8_t v_stack_m38;

    local_rsp = (local_rsp) - (88);
    v_stack_m18 = (uint32_t)((uint32_t)(Arg9));
    v_stack_m20 = Arg8;
    v_stack_m28 = Arg7;
    v_stack_m30 = (uint32_t)((uint32_t)(Arg6));
    v_stack_m38 = Arg5;
    result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (88);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagevrfy&rva=0x00BA09C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00BA09C0[BB_00BA09C0]
  bb_00BA0A1C[BB_00BA0A1C]
```
