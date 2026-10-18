# VerifierFsRtlNotifyFilterChangeDirectory

- RVA: `0x00B9EC90`–`0x00B9ED21` (길이 `145` bytes)
- VA: `0x0000000140B9EC90`
- 실행 섹션: `PAGEVRFY`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007AFEC`
- 디코드: `33`개 명령, `145/145` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00B9ED0B` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00B9ECDF` → RVA `0x00FFE7B0` (`PAGEVRFD`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00B9ED0B` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGEVRFY` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B9EC90  4C 8B DC                        mov r11, rsp
00B9EC93  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
00B9EC97  49 89 73 10                     mov qword ptr [r11 + 0x10], rsi
00B9EC9B  57                              push rdi
00B9EC9C  48 83 EC 60                     sub rsp, 0x60
00B9ECA0  48 8B 84 24 C0 00 00 00         mov rax, qword ptr [rsp + 0xc0]
00B9ECA8  49 8B D9                        mov rbx, r9
00B9ECAB  4C 8B 94 24 B0 00 00 00         mov r10, qword ptr [rsp + 0xb0]
00B9ECB3  48 8B FA                        mov rdi, rdx
00B9ECB6  44 8B 8C 24 A0 00 00 00         mov r9d, dword ptr [rsp + 0xa0]
00B9ECBE  48 8B F1                        mov rsi, rcx
00B9ECC1  8A 94 24 98 00 00 00            mov dl, byte ptr [rsp + 0x98]
00B9ECC8  8A 8C 24 90 00 00 00            mov cl, byte ptr [rsp + 0x90]
00B9ECCF  49 89 43 E8                     mov qword ptr [r11 - 0x18], rax
00B9ECD3  48 8B 84 24 B8 00 00 00         mov rax, qword ptr [rsp + 0xb8]
00B9ECDB  49 89 43 E0                     mov qword ptr [r11 - 0x20], rax
00B9ECDF  48 8B 05 CA FA 45 00            mov rax, qword ptr [rip + 0x45faca]
00B9ECE6  4D 89 53 D8                     mov qword ptr [r11 - 0x28], r10
00B9ECEA  4C 8B 94 24 A8 00 00 00         mov r10, qword ptr [rsp + 0xa8]
00B9ECF2  4D 89 53 D0                     mov qword ptr [r11 - 0x30], r10
00B9ECF6  45 89 4B C8                     mov dword ptr [r11 - 0x38], r9d
00B9ECFA  4C 8B CB                        mov r9, rbx
00B9ECFD  88 54 24 28                     mov byte ptr [rsp + 0x28], dl
00B9ED01  48 8B D7                        mov rdx, rdi
00B9ED04  88 4C 24 20                     mov byte ptr [rsp + 0x20], cl
00B9ED08  48 8B CE                        mov rcx, rsi
00B9ED0B  E8 C0 BD B1 FF                  call 0x1406baad0
00B9ED10  48 8B 5C 24 70                  mov rbx, qword ptr [rsp + 0x70]
00B9ED15  48 8B 74 24 78                  mov rsi, qword ptr [rsp + 0x78]
00B9ED1A  48 83 C4 60                     add rsp, 0x60
00B9ED1E  5F                              pop rdi
00B9ED1F  C3                              ret
00B9ED20  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VerifierFsRtlNotifyFilterChangeDirectory(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned __int8 a5, unsigned __int8 a6, unsigned int a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int8 v_stack_m40;
    unsigned __int8 v_stack_m48;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rsi;
    v_rsp = (v_rsp) - (96);
    *(unsigned __int64 *)(v_rsp - 24) = a11;
    *(unsigned __int64 *)(v_rsp - 32) = a10;
    *(unsigned __int64 *)(v_rsp - 40) = a9;
    *(unsigned __int64 *)(v_rsp - 48) = a8;
    *(unsigned int *)(v_rsp - 56) = (unsigned int)((unsigned int)(a7));
    v_stack_m40 = a6;
    v_stack_m48 = a5;
    result = guard_dispatch_icall(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (96);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t VerifierFsRtlNotifyFilterChangeDirectory(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint8_t Arg5, uint8_t Arg6, uint32_t Arg7, int64_t Arg8, int64_t Arg9, int64_t Arg10, int64_t Arg11)
{
    int64_t result;
    int64_t local_rsp;
    uint8_t v_stack_m40;
    uint8_t v_stack_m48;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rsi;
    local_rsp = (local_rsp) - (96);
    *(uint64_t *)(local_rsp - 0x18) = Arg11;
    *(uint64_t *)(local_rsp - 0x20) = Arg10;
    *(uint64_t *)(local_rsp - 0x28) = Arg9;
    *(uint64_t *)(local_rsp - 0x30) = Arg8;
    *(uint32_t *)(local_rsp - 0x38) = (uint32_t)((uint32_t)(Arg7));
    v_stack_m40 = Arg6;
    v_stack_m48 = Arg5;
    result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (96);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagevrfy&rva=0x00B9EC90&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B9EC90[BB_00B9EC90]
  bb_00B9ED20[BB_00B9ED20]
```
