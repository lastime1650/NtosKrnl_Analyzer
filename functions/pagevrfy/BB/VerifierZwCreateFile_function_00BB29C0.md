# VerifierZwCreateFile

- RVA: `0x00BB29C0`–`0x00BB2A4F` (길이 `143` bytes)
- VA: `0x0000000140BB29C0`
- 실행 섹션: `PAGEVRFY`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007AFEC`
- 디코드: `33`개 명령, `143/143` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00BB2A39` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00BB2A0E` → RVA `0x00FFE0B0` (`PAGEVRFD`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00BB2A39` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGEVRFY` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BB29C0  4C 8B DC                        mov r11, rsp
00BB29C3  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
00BB29C7  49 89 73 10                     mov qword ptr [r11 + 0x10], rsi
00BB29CB  57                              push rdi
00BB29CC  48 83 EC 60                     sub rsp, 0x60
00BB29D0  44 8B 94 24 B0 00 00 00         mov r10d, dword ptr [rsp + 0xb0]
00BB29D8  49 8B D9                        mov rbx, r9
00BB29DB  8B 84 24 C0 00 00 00            mov eax, dword ptr [rsp + 0xc0]
00BB29E2  8B FA                           mov edi, edx
00BB29E4  8B 94 24 98 00 00 00            mov edx, dword ptr [rsp + 0x98]
00BB29EB  48 8B F1                        mov rsi, rcx
00BB29EE  44 8B 8C 24 A0 00 00 00         mov r9d, dword ptr [rsp + 0xa0]
00BB29F6  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
00BB29FE  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
00BB2A02  48 8B 84 24 B8 00 00 00         mov rax, qword ptr [rsp + 0xb8]
00BB2A0A  49 89 43 E0                     mov qword ptr [r11 - 0x20], rax
00BB2A0E  48 8B 05 9B B6 44 00            mov rax, qword ptr [rip + 0x44b69b]
00BB2A15  45 89 53 D8                     mov dword ptr [r11 - 0x28], r10d
00BB2A19  44 8B 94 24 A8 00 00 00         mov r10d, dword ptr [rsp + 0xa8]
00BB2A21  45 89 53 D0                     mov dword ptr [r11 - 0x30], r10d
00BB2A25  45 89 4B C8                     mov dword ptr [r11 - 0x38], r9d
00BB2A29  4C 8B CB                        mov r9, rbx
00BB2A2C  89 54 24 28                     mov dword ptr [rsp + 0x28], edx
00BB2A30  8B D7                           mov edx, edi
00BB2A32  49 89 4B B8                     mov qword ptr [r11 - 0x48], rcx
00BB2A36  48 8B CE                        mov rcx, rsi
00BB2A39  E8 92 80 B0 FF                  call 0x1406baad0
00BB2A3E  48 8B 5C 24 70                  mov rbx, qword ptr [rsp + 0x70]
00BB2A43  48 8B 74 24 78                  mov rsi, qword ptr [rsp + 0x78]
00BB2A48  48 83 C4 60                     add rsp, 0x60
00BB2A4C  5F                              pop rdi
00BB2A4D  C3                              ret
00BB2A4E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VerifierZwCreateFile(__int64 a1, int a2, __int64 a3, __int64 a4, __int64 a5, unsigned int a6, unsigned int a7, unsigned int a8, unsigned int a9, __int64 a10, unsigned int a11)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_m18;
    unsigned int v_stack_m40;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rsi;
    v_rsp = (v_rsp) - (96);
    v_stack_m18 = (unsigned int)((unsigned int)(a11));
    *(unsigned __int64 *)(v_rsp - 32) = a10;
    *(unsigned int *)(v_rsp - 40) = (unsigned int)((unsigned int)(a9));
    *(unsigned int *)(v_rsp - 48) = (unsigned int)((unsigned int)(a8));
    *(unsigned int *)(v_rsp - 56) = (unsigned int)((unsigned int)(a7));
    v_stack_m40 = (unsigned int)((unsigned int)(a6));
    *(unsigned __int64 *)(v_rsp - 72) = a5;
    result = guard_dispatch_icall(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    v_rsp = (v_rsp) + (96);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t VerifierZwCreateFile(int64_t Arg1, int32_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5, uint32_t Arg6, uint32_t Arg7, uint32_t Arg8, uint32_t Arg9, int64_t Arg10, uint32_t Arg11)
{
    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_m18;
    uint32_t v_stack_m40;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rsi;
    local_rsp = (local_rsp) - (96);
    v_stack_m18 = (uint32_t)((uint32_t)(Arg11));
    *(uint64_t *)(local_rsp - 0x20) = Arg10;
    *(uint32_t *)(local_rsp - 0x28) = (uint32_t)((uint32_t)(Arg9));
    *(uint32_t *)(local_rsp - 0x30) = (uint32_t)((uint32_t)(Arg8));
    *(uint32_t *)(local_rsp - 0x38) = (uint32_t)((uint32_t)(Arg7));
    v_stack_m40 = (uint32_t)((uint32_t)(Arg6));
    *(uint64_t *)(local_rsp - 0x48) = Arg5;
    result = guard_dispatch_icall(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4);
    local_rsp = (local_rsp) + (96);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagevrfy&rva=0x00BB29C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00BB29C0[BB_00BB29C0]
  bb_00BB2A4E[BB_00BB2A4E]
```
