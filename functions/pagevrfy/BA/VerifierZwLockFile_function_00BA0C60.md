# VerifierZwLockFile

- RVA: `0x00BA0C60`–`0x00BA0CD7` (길이 `119` bytes)
- VA: `0x0000000140BA0C60`
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
- `0x00BA0CC6` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00BA0C95` → RVA `0x00FFEDA0` (`PAGEVRFD`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00BA0CC6` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGEVRFY` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BA0C60  4C 8B DC                        mov r11, rsp
00BA0C63  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
00BA0C67  57                              push rdi
00BA0C68  48 83 EC 60                     sub rsp, 0x60
00BA0C6C  44 8A 94 24 B0 00 00 00         mov r10b, byte ptr [rsp + 0xb0]
00BA0C74  49 8B D9                        mov rbx, r9
00BA0C77  8A 84 24 B8 00 00 00            mov al, byte ptr [rsp + 0xb8]
00BA0C7E  48 8B FA                        mov rdi, rdx
00BA0C81  4C 8B 8C 24 98 00 00 00         mov r9, qword ptr [rsp + 0x98]
00BA0C89  48 8B 94 24 90 00 00 00         mov rdx, qword ptr [rsp + 0x90]
00BA0C91  88 44 24 48                     mov byte ptr [rsp + 0x48], al
00BA0C95  48 8B 05 04 E1 45 00            mov rax, qword ptr [rip + 0x45e104]
00BA0C9C  45 88 53 D8                     mov byte ptr [r11 - 0x28], r10b
00BA0CA0  44 8B 94 24 A8 00 00 00         mov r10d, dword ptr [rsp + 0xa8]
00BA0CA8  45 89 53 D0                     mov dword ptr [r11 - 0x30], r10d
00BA0CAC  4C 8B 94 24 A0 00 00 00         mov r10, qword ptr [rsp + 0xa0]
00BA0CB4  4D 89 53 C8                     mov qword ptr [r11 - 0x38], r10
00BA0CB8  4D 89 4B C0                     mov qword ptr [r11 - 0x40], r9
00BA0CBC  4C 8B CB                        mov r9, rbx
00BA0CBF  49 89 53 B8                     mov qword ptr [r11 - 0x48], rdx
00BA0CC3  48 8B D7                        mov rdx, rdi
00BA0CC6  E8 05 9E B1 FF                  call 0x1406baad0
00BA0CCB  48 8B 5C 24 70                  mov rbx, qword ptr [rsp + 0x70]
00BA0CD0  48 83 C4 60                     add rsp, 0x60
00BA0CD4  5F                              pop rdi
00BA0CD5  C3                              ret
00BA0CD6  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VerifierZwLockFile(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, unsigned int a8, unsigned __int8 a9, unsigned __int8 a10)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int8 v_stack_m20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    v_rsp = (v_rsp) - (96);
    v_stack_m20 = a10;
    *(unsigned __int8 *)(v_rsp - 40) = a9;
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
int64_t VerifierZwLockFile(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5, int64_t Arg6, int64_t Arg7, uint32_t Arg8, uint8_t Arg9, uint8_t Arg10)
{
    int64_t result;
    int64_t local_rsp;
    uint8_t v_stack_m20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    local_rsp = (local_rsp) - (96);
    v_stack_m20 = Arg10;
    *(uint8_t *)(local_rsp - 0x28) = Arg9;
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

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagevrfy&rva=0x00BA0C60&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00BA0C60[BB_00BA0C60]
  bb_00BA0CD6[BB_00BA0CD6]
```
