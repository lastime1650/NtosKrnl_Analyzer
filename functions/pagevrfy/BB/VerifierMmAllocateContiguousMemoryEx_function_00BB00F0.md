# VerifierMmAllocateContiguousMemoryEx

- RVA: `0x00BB00F0`–`0x00BB0151` (길이 `97` bytes)
- VA: `0x0000000140BB00F0`
- 실행 섹션: `PAGEVRFY`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007A034`
- 디코드: `19`개 명령, `97/97` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00BB0146` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00BB010B` → RVA `0x00FFDF18` (`PAGEVRFD`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00BB0146` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGEVRFY` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BB00F0  4C 8B DC                        mov r11, rsp
00BB00F3  48 83 EC 68                     sub rsp, 0x68
00BB00F7  44 8B 94 24 B0 00 00 00         mov r10d, dword ptr [rsp + 0xb0]
00BB00FF  48 8B 84 24 B8 00 00 00         mov rax, qword ptr [rsp + 0xb8]
00BB0107  49 89 43 E0                     mov qword ptr [r11 - 0x20], rax
00BB010B  48 8B 05 06 DE 44 00            mov rax, qword ptr [rip + 0x44de06]
00BB0112  45 89 53 D8                     mov dword ptr [r11 - 0x28], r10d
00BB0116  44 8B 94 24 A8 00 00 00         mov r10d, dword ptr [rsp + 0xa8]
00BB011E  45 89 53 D0                     mov dword ptr [r11 - 0x30], r10d
00BB0122  4C 8B 94 24 A0 00 00 00         mov r10, qword ptr [rsp + 0xa0]
00BB012A  4D 89 53 C8                     mov qword ptr [r11 - 0x38], r10
00BB012E  44 8B 94 24 98 00 00 00         mov r10d, dword ptr [rsp + 0x98]
00BB0136  45 89 53 C0                     mov dword ptr [r11 - 0x40], r10d
00BB013A  44 8B 94 24 90 00 00 00         mov r10d, dword ptr [rsp + 0x90]
00BB0142  45 89 53 B8                     mov dword ptr [r11 - 0x48], r10d
00BB0146  E8 85 A9 B0 FF                  call 0x1406baad0
00BB014B  48 83 C4 68                     add rsp, 0x68
00BB014F  C3                              ret
00BB0150  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VerifierMmAllocateContiguousMemoryEx(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned int a5, unsigned int a6, __int64 a7, unsigned int a8, unsigned int a9, __int64 a10)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (104);
    *(unsigned __int64 *)(v_rsp - 32) = a10;
    *(unsigned int *)(v_rsp - 40) = (unsigned int)((unsigned int)(a9));
    *(unsigned int *)(v_rsp - 48) = (unsigned int)((unsigned int)(a8));
    *(unsigned __int64 *)(v_rsp - 56) = a7;
    *(unsigned int *)(v_rsp - 64) = (unsigned int)((unsigned int)(a6));
    *(unsigned int *)(v_rsp - 72) = (unsigned int)((unsigned int)(a5));
    result = guard_dispatch_icall(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (104);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t VerifierMmAllocateContiguousMemoryEx(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint32_t Arg5, uint32_t Arg6, int64_t Arg7, uint32_t Arg8, uint32_t Arg9, int64_t Arg10)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (104);
    *(uint64_t *)(local_rsp - 0x20) = Arg10;
    *(uint32_t *)(local_rsp - 0x28) = (uint32_t)((uint32_t)(Arg9));
    *(uint32_t *)(local_rsp - 0x30) = (uint32_t)((uint32_t)(Arg8));
    *(uint64_t *)(local_rsp - 0x38) = Arg7;
    *(uint32_t *)(local_rsp - 0x40) = (uint32_t)((uint32_t)(Arg6));
    *(uint32_t *)(local_rsp - 0x48) = (uint32_t)((uint32_t)(Arg5));
    result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (104);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagevrfy&rva=0x00BB00F0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00BB00F0[BB_00BB00F0]
  bb_00BB0150[BB_00BB0150]
```
