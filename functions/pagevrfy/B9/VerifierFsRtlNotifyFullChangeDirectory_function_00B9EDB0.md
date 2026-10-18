# VerifierFsRtlNotifyFullChangeDirectory

- RVA: `0x00B9EDB0`–`0x00B9EE27` (길이 `119` bytes)
- VA: `0x0000000140B9EDB0`
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
- `0x00B9EE16` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00B9EDE5` → RVA `0x00FFE7C0` (`PAGEVRFD`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00B9EE16` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGEVRFY` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B9EDB0  4C 8B DC                        mov r11, rsp
00B9EDB3  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
00B9EDB7  57                              push rdi
00B9EDB8  48 83 EC 60                     sub rsp, 0x60
00B9EDBC  48 8B 84 24 B8 00 00 00         mov rax, qword ptr [rsp + 0xb8]
00B9EDC4  49 8B D9                        mov rbx, r9
00B9EDC7  4C 8B 94 24 B0 00 00 00         mov r10, qword ptr [rsp + 0xb0]
00B9EDCF  48 8B FA                        mov rdi, rdx
00B9EDD2  44 8A 8C 24 98 00 00 00         mov r9b, byte ptr [rsp + 0x98]
00B9EDDA  8A 94 24 90 00 00 00            mov dl, byte ptr [rsp + 0x90]
00B9EDE1  49 89 43 E0                     mov qword ptr [r11 - 0x20], rax
00B9EDE5  48 8B 05 D4 F9 45 00            mov rax, qword ptr [rip + 0x45f9d4]
00B9EDEC  4D 89 53 D8                     mov qword ptr [r11 - 0x28], r10
00B9EDF0  4C 8B 94 24 A8 00 00 00         mov r10, qword ptr [rsp + 0xa8]
00B9EDF8  4D 89 53 D0                     mov qword ptr [r11 - 0x30], r10
00B9EDFC  44 8B 94 24 A0 00 00 00         mov r10d, dword ptr [rsp + 0xa0]
00B9EE04  45 89 53 C8                     mov dword ptr [r11 - 0x38], r10d
00B9EE08  45 88 4B C0                     mov byte ptr [r11 - 0x40], r9b
00B9EE0C  4C 8B CB                        mov r9, rbx
00B9EE0F  88 54 24 20                     mov byte ptr [rsp + 0x20], dl
00B9EE13  48 8B D7                        mov rdx, rdi
00B9EE16  E8 B5 BC B1 FF                  call 0x1406baad0
00B9EE1B  48 8B 5C 24 70                  mov rbx, qword ptr [rsp + 0x70]
00B9EE20  48 83 C4 60                     add rsp, 0x60
00B9EE24  5F                              pop rdi
00B9EE25  C3                              ret
00B9EE26  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VerifierFsRtlNotifyFullChangeDirectory(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned __int8 a5, unsigned __int8 a6, unsigned int a7, __int64 a8, __int64 a9, __int64 a10)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int8 v_stack_m48;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    v_rsp = (v_rsp) - (96);
    *(unsigned __int64 *)(v_rsp - 32) = a10;
    *(unsigned __int64 *)(v_rsp - 40) = a9;
    *(unsigned __int64 *)(v_rsp - 48) = a8;
    *(unsigned int *)(v_rsp - 56) = (unsigned int)((unsigned int)(a7));
    *(unsigned __int8 *)(v_rsp - 64) = a6;
    v_stack_m48 = a5;
    result = guard_dispatch_icall(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (96);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t VerifierFsRtlNotifyFullChangeDirectory(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint8_t Arg5, uint8_t Arg6, uint32_t Arg7, int64_t Arg8, int64_t Arg9, int64_t Arg10)
{
    int64_t result;
    int64_t local_rsp;
    uint8_t v_stack_m48;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    local_rsp = (local_rsp) - (96);
    *(uint64_t *)(local_rsp - 0x20) = Arg10;
    *(uint64_t *)(local_rsp - 0x28) = Arg9;
    *(uint64_t *)(local_rsp - 0x30) = Arg8;
    *(uint32_t *)(local_rsp - 0x38) = (uint32_t)((uint32_t)(Arg7));
    *(uint8_t *)(local_rsp - 0x40) = Arg6;
    v_stack_m48 = Arg5;
    result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (96);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagevrfy&rva=0x00B9EDB0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B9EDB0[BB_00B9EDB0]
  bb_00B9EE26[BB_00B9EE26]
```
