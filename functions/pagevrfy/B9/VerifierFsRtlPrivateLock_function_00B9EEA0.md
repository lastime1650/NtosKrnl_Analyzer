# VerifierFsRtlPrivateLock

- RVA: `0x00B9EEA0`–`0x00B9EF3E` (길이 `158` bytes)
- VA: `0x0000000140B9EEA0`
- 실행 섹션: `PAGEVRFY`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000689A0`
- 디코드: `36`개 명령, `158/158` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00B9EF26` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00B9EEFA` → RVA `0x00FFE790` (`PAGEVRFD`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00B9EF26` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGEVRFY` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B9EEA0  4C 8B DC                        mov r11, rsp
00B9EEA3  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
00B9EEA7  49 89 73 10                     mov qword ptr [r11 + 0x10], rsi
00B9EEAB  57                              push rdi
00B9EEAC  48 83 EC 70                     sub rsp, 0x70
00B9EEB0  8A 84 24 D8 00 00 00            mov al, byte ptr [rsp + 0xd8]
00B9EEB7  48 8B F1                        mov rsi, rcx
00B9EEBA  4C 8B 94 24 C0 00 00 00         mov r10, qword ptr [rsp + 0xc0]
00B9EEC2  49 8B D9                        mov rbx, r9
00B9EEC5  44 8A 8C 24 B8 00 00 00         mov r9b, byte ptr [rsp + 0xb8]
00B9EECD  48 8B FA                        mov rdi, rdx
00B9EED0  8A 94 24 B0 00 00 00            mov dl, byte ptr [rsp + 0xb0]
00B9EED7  8B 8C 24 A8 00 00 00            mov ecx, dword ptr [rsp + 0xa8]
00B9EEDE  88 44 24 58                     mov byte ptr [rsp + 0x58], al
00B9EEE2  48 8B 84 24 D0 00 00 00         mov rax, qword ptr [rsp + 0xd0]
00B9EEEA  49 89 43 D8                     mov qword ptr [r11 - 0x28], rax
00B9EEEE  48 8B 84 24 C8 00 00 00         mov rax, qword ptr [rsp + 0xc8]
00B9EEF6  49 89 43 D0                     mov qword ptr [r11 - 0x30], rax
00B9EEFA  48 8B 05 8F F8 45 00            mov rax, qword ptr [rip + 0x45f88f]
00B9EF01  4D 89 53 C8                     mov qword ptr [r11 - 0x38], r10
00B9EF05  45 88 4B C0                     mov byte ptr [r11 - 0x40], r9b
00B9EF09  4C 8B CB                        mov r9, rbx
00B9EF0C  88 54 24 30                     mov byte ptr [rsp + 0x30], dl
00B9EF10  48 8B D7                        mov rdx, rdi
00B9EF13  89 4C 24 28                     mov dword ptr [rsp + 0x28], ecx
00B9EF17  48 8B 8C 24 A0 00 00 00         mov rcx, qword ptr [rsp + 0xa0]
00B9EF1F  49 89 4B A8                     mov qword ptr [r11 - 0x58], rcx
00B9EF23  48 8B CE                        mov rcx, rsi
00B9EF26  E8 A5 BB B1 FF                  call 0x1406baad0
00B9EF2B  4C 8D 5C 24 70                  lea r11, [rsp + 0x70]
00B9EF30  49 8B 5B 10                     mov rbx, qword ptr [r11 + 0x10]
00B9EF34  49 8B 73 18                     mov rsi, qword ptr [r11 + 0x18]
00B9EF38  49 8B E3                        mov rsp, r11
00B9EF3B  5F                              pop rdi
00B9EF3C  C3                              ret
00B9EF3D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VerifierFsRtlPrivateLock(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, unsigned int a6, unsigned __int8 a7, unsigned __int8 a8, __int64 a9, __int64 a10, __int64 a11, unsigned __int8 a12)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int8 v_stack_m20;
    unsigned __int8 v_stack_m48;
    unsigned int v_stack_m50;
    unsigned __int64 v_stack_m8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rsi;
    v_rsp = (v_rsp) - (112);
    v_stack_m20 = a12;
    *(unsigned __int64 *)(v_rsp - 40) = a11;
    *(unsigned __int64 *)(v_rsp - 48) = a10;
    *(unsigned __int64 *)(v_rsp - 56) = a9;
    *(unsigned __int8 *)(v_rsp - 64) = a8;
    v_stack_m48 = a7;
    v_stack_m50 = (unsigned int)((unsigned int)(a6));
    *(unsigned __int64 *)(v_rsp - 88) = a5;
    result = guard_dispatch_icall(a1, a2, a3, a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t VerifierFsRtlPrivateLock(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5, uint32_t Arg6, uint8_t Arg7, uint8_t Arg8, int64_t Arg9, int64_t Arg10, int64_t Arg11, uint8_t Arg12)
{
    int64_t result;
    int64_t local_rsp;
    uint8_t v_stack_m20;
    uint8_t v_stack_m48;
    uint32_t v_stack_m50;
    uint64_t v_stack_m8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rsi;
    local_rsp = (local_rsp) - (112);
    v_stack_m20 = Arg12;
    *(uint64_t *)(local_rsp - 0x28) = Arg11;
    *(uint64_t *)(local_rsp - 0x30) = Arg10;
    *(uint64_t *)(local_rsp - 0x38) = Arg9;
    *(uint8_t *)(local_rsp - 0x40) = Arg8;
    v_stack_m48 = Arg7;
    v_stack_m50 = (uint32_t)((uint32_t)(Arg6));
    *(uint64_t *)(local_rsp - 0x58) = Arg5;
    result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagevrfy&rva=0x00B9EEA0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B9EEA0[BB_00B9EEA0]
  bb_00B9EF3D[BB_00B9EF3D]
```
