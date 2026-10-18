# VerifierNtMapViewOfSection

- RVA: `0x00BB0FA0`–`0x00BB1017` (길이 `119` bytes)
- VA: `0x0000000140BB0FA0`
- 실행 섹션: `PAGEVRFY`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008C33C`
- 디코드: `27`개 명령, `119/119` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00BB1006` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00BB0FD5` → RVA `0x00FFDF28` (`PAGEVRFD`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00BB1006` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGEVRFY` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BB0FA0  4C 8B DC                        mov r11, rsp
00BB0FA3  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
00BB0FA7  57                              push rdi
00BB0FA8  48 83 EC 60                     sub rsp, 0x60
00BB0FAC  44 8B 94 24 B0 00 00 00         mov r10d, dword ptr [rsp + 0xb0]
00BB0FB4  49 8B D9                        mov rbx, r9
00BB0FB7  8B 84 24 B8 00 00 00            mov eax, dword ptr [rsp + 0xb8]
00BB0FBE  48 8B FA                        mov rdi, rdx
00BB0FC1  4C 8B 8C 24 98 00 00 00         mov r9, qword ptr [rsp + 0x98]
00BB0FC9  48 8B 94 24 90 00 00 00         mov rdx, qword ptr [rsp + 0x90]
00BB0FD1  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
00BB0FD5  48 8B 05 4C CF 44 00            mov rax, qword ptr [rip + 0x44cf4c]
00BB0FDC  45 89 53 D8                     mov dword ptr [r11 - 0x28], r10d
00BB0FE0  44 8B 94 24 A8 00 00 00         mov r10d, dword ptr [rsp + 0xa8]
00BB0FE8  45 89 53 D0                     mov dword ptr [r11 - 0x30], r10d
00BB0FEC  4C 8B 94 24 A0 00 00 00         mov r10, qword ptr [rsp + 0xa0]
00BB0FF4  4D 89 53 C8                     mov qword ptr [r11 - 0x38], r10
00BB0FF8  4D 89 4B C0                     mov qword ptr [r11 - 0x40], r9
00BB0FFC  4C 8B CB                        mov r9, rbx
00BB0FFF  49 89 53 B8                     mov qword ptr [r11 - 0x48], rdx
00BB1003  48 8B D7                        mov rdx, rdi
00BB1006  E8 C5 9A B0 FF                  call 0x1406baad0
00BB100B  48 8B 5C 24 70                  mov rbx, qword ptr [rsp + 0x70]
00BB1010  48 83 C4 60                     add rsp, 0x60
00BB1014  5F                              pop rdi
00BB1015  C3                              ret
00BB1016  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VerifierNtMapViewOfSection(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, unsigned int a8, unsigned int a9, unsigned int a10)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_m20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    v_rsp = (v_rsp) - (96);
    v_stack_m20 = (unsigned int)((unsigned int)(a10));
    *(unsigned int *)(v_rsp - 40) = (unsigned int)((unsigned int)(a9));
    *(unsigned int *)(v_rsp - 48) = (unsigned int)((unsigned int)(a8));
    *(unsigned __int64 *)(v_rsp - 56) = a7;
    *(unsigned __int64 *)(v_rsp - 64) = a6;
    *(unsigned __int64 *)(v_rsp - 72) = a5;
    result = guard_dispatch_icall(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (96);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t VerifierNtMapViewOfSection(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5, int64_t Arg6, int64_t Arg7, uint32_t Arg8, uint32_t Arg9, uint32_t Arg10)
{
    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_m20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    local_rsp = (local_rsp) - (96);
    v_stack_m20 = (uint32_t)((uint32_t)(Arg10));
    *(uint32_t *)(local_rsp - 0x28) = (uint32_t)((uint32_t)(Arg9));
    *(uint32_t *)(local_rsp - 0x30) = (uint32_t)((uint32_t)(Arg8));
    *(uint64_t *)(local_rsp - 0x38) = Arg7;
    *(uint64_t *)(local_rsp - 0x40) = Arg6;
    *(uint64_t *)(local_rsp - 0x48) = Arg5;
    result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (96);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagevrfy&rva=0x00BB0FA0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00BB0FA0[BB_00BB0FA0]
  bb_00BB1016[BB_00BB1016]
```
