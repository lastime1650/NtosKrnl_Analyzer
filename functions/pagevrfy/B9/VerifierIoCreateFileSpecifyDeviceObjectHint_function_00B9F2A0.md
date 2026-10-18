# VerifierIoCreateFileSpecifyDeviceObjectHint

- RVA: `0x00B9F2A0`–`0x00B9F343` (길이 `163` bytes)
- VA: `0x0000000140B9F2A0`
- 실행 섹션: `PAGEVRFY`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007F69C`
- 디코드: `30`개 명령, `163/163` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00B9F335` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00B9F2F9` → RVA `0x00FF40D8` (`PAGEVRFD`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00B9F335` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGEVRFY` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B9F2A0  48 81 EC 88 00 00 00            sub rsp, 0x88
00B9F2A7  48 8B 84 24 00 01 00 00         mov rax, qword ptr [rsp + 0x100]
00B9F2AF  4C 8B D9                        mov r11, rcx
00B9F2B2  8B 8C 24 D0 00 00 00            mov ecx, dword ptr [rsp + 0xd0]
00B9F2B9  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
00B9F2BE  8B 84 24 F8 00 00 00            mov eax, dword ptr [rsp + 0xf8]
00B9F2C5  89 44 24 68                     mov dword ptr [rsp + 0x68], eax
00B9F2C9  48 8B 84 24 F0 00 00 00         mov rax, qword ptr [rsp + 0xf0]
00B9F2D1  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00B9F2D6  8B 84 24 E8 00 00 00            mov eax, dword ptr [rsp + 0xe8]
00B9F2DD  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
00B9F2E1  8B 84 24 E0 00 00 00            mov eax, dword ptr [rsp + 0xe0]
00B9F2E8  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
00B9F2EC  48 8B 84 24 D8 00 00 00         mov rax, qword ptr [rsp + 0xd8]
00B9F2F4  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00B9F2F9  48 8B 05 D8 4D 45 00            mov rax, qword ptr [rip + 0x454dd8]
00B9F300  89 4C 24 40                     mov dword ptr [rsp + 0x40], ecx
00B9F304  8B 8C 24 C8 00 00 00            mov ecx, dword ptr [rsp + 0xc8]
00B9F30B  89 4C 24 38                     mov dword ptr [rsp + 0x38], ecx
00B9F30F  8B 8C 24 C0 00 00 00            mov ecx, dword ptr [rsp + 0xc0]
00B9F316  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
00B9F31A  8B 8C 24 B8 00 00 00            mov ecx, dword ptr [rsp + 0xb8]
00B9F321  89 4C 24 28                     mov dword ptr [rsp + 0x28], ecx
00B9F325  48 8B 8C 24 B0 00 00 00         mov rcx, qword ptr [rsp + 0xb0]
00B9F32D  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00B9F332  49 8B CB                        mov rcx, r11
00B9F335  E8 96 B7 B1 FF                  call 0x1406baad0
00B9F33A  48 81 C4 88 00 00 00            add rsp, 0x88
00B9F341  C3                              ret
00B9F342  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VerifierIoCreateFileSpecifyDeviceObjectHint(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, unsigned int a6, unsigned int a7, unsigned int a8, unsigned int a9, __int64 a10, unsigned int a11, unsigned int a12, __int64 a13, unsigned int a14, __int64 a15)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m30;
    unsigned int v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned int v_stack_m48;
    unsigned int v_stack_m50;
    unsigned int v_stack_m58;
    unsigned int v_stack_m60;
    unsigned __int64 v_stack_m68;

    v_rsp = (v_rsp) - (136);
    v_stack_m18 = a15;
    v_stack_m20 = (unsigned int)((unsigned int)(a14));
    v_stack_m28 = a13;
    v_stack_m30 = (unsigned int)((unsigned int)(a12));
    v_stack_m38 = (unsigned int)((unsigned int)(a11));
    v_stack_m40 = a10;
    v_stack_m48 = (unsigned int)((unsigned int)(a9));
    v_stack_m50 = (unsigned int)((unsigned int)(a8));
    v_stack_m58 = (unsigned int)((unsigned int)(a7));
    v_stack_m60 = (unsigned int)((unsigned int)(a6));
    v_stack_m68 = a5;
    result = guard_dispatch_icall(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (136);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t VerifierIoCreateFileSpecifyDeviceObjectHint(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5, uint32_t Arg6, uint32_t Arg7, uint32_t Arg8, uint32_t Arg9, int64_t Arg10, uint32_t Arg11, uint32_t Arg12, int64_t Arg13, uint32_t Arg14, int64_t Arg15)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint32_t v_stack_m20;
    uint64_t v_stack_m28;
    uint32_t v_stack_m30;
    uint32_t v_stack_m38;
    uint64_t v_stack_m40;
    uint32_t v_stack_m48;
    uint32_t v_stack_m50;
    uint32_t v_stack_m58;
    uint32_t v_stack_m60;
    uint64_t v_stack_m68;

    local_rsp = (local_rsp) - (136);
    v_stack_m18 = Arg15;
    v_stack_m20 = (uint32_t)((uint32_t)(Arg14));
    v_stack_m28 = Arg13;
    v_stack_m30 = (uint32_t)((uint32_t)(Arg12));
    v_stack_m38 = (uint32_t)((uint32_t)(Arg11));
    v_stack_m40 = Arg10;
    v_stack_m48 = (uint32_t)((uint32_t)(Arg9));
    v_stack_m50 = (uint32_t)((uint32_t)(Arg8));
    v_stack_m58 = (uint32_t)((uint32_t)(Arg7));
    v_stack_m60 = (uint32_t)((uint32_t)(Arg6));
    v_stack_m68 = Arg5;
    result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (136);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagevrfy&rva=0x00B9F2A0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B9F2A0[BB_00B9F2A0]
  bb_00B9F342[BB_00B9F342]
```
