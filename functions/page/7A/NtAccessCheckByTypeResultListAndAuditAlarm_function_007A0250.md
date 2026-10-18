# NtAccessCheckByTypeResultListAndAuditAlarm

- RVA: `0x007A0250`–`0x007A02F7` (길이 `167` bytes)
- VA: `0x00000001407A0250`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000AA4F0`
- 디코드: `32`개 명령, `167/167` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x007A02E9` → [SepAccessCheckAndAuditAlarm](../A1/SepAccessCheckAndAuditAlarm_function_00A1AF4C.md) (function, `0x00A1AF4C`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007A0250  4C 8B DC                        mov r11, rsp
007A0253  48 81 EC 98 00 00 00            sub rsp, 0x98
007A025A  48 8B 84 24 18 01 00 00         mov rax, qword ptr [rsp + 0x118]
007A0262  41 C6 43 E8 01                  mov byte ptr [r11 - 0x18], 1
007A0267  49 89 43 E0                     mov qword ptr [r11 - 0x20], rax
007A026B  48 8B 84 24 10 01 00 00         mov rax, qword ptr [rsp + 0x110]
007A0273  49 89 43 D8                     mov qword ptr [r11 - 0x28], rax
007A0277  48 8B 84 24 08 01 00 00         mov rax, qword ptr [rsp + 0x108]
007A027F  49 89 43 D0                     mov qword ptr [r11 - 0x30], rax
007A0283  48 8B 84 24 F8 00 00 00         mov rax, qword ptr [rsp + 0xf8]
007A028B  49 89 43 C8                     mov qword ptr [r11 - 0x38], rax
007A028F  8B 84 24 F0 00 00 00            mov eax, dword ptr [rsp + 0xf0]
007A0296  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
007A029A  48 8B 84 24 E8 00 00 00         mov rax, qword ptr [rsp + 0xe8]
007A02A2  49 89 43 B8                     mov qword ptr [r11 - 0x48], rax
007A02A6  8B 84 24 E0 00 00 00            mov eax, dword ptr [rsp + 0xe0]
007A02AD  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
007A02B1  8B 84 24 D8 00 00 00            mov eax, dword ptr [rsp + 0xd8]
007A02B8  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
007A02BC  8B 84 24 D0 00 00 00            mov eax, dword ptr [rsp + 0xd0]
007A02C3  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
007A02C7  48 8B 84 24 C8 00 00 00         mov rax, qword ptr [rsp + 0xc8]
007A02CF  49 89 43 98                     mov qword ptr [r11 - 0x68], rax
007A02D3  48 8B 84 24 C0 00 00 00         mov rax, qword ptr [rsp + 0xc0]
007A02DB  49 89 43 90                     mov qword ptr [r11 - 0x70], rax
007A02DF  4D 89 4B 88                     mov qword ptr [r11 - 0x78], r9
007A02E3  4D 8B C8                        mov r9, r8
007A02E6  45 33 C0                        xor r8d, r8d
007A02E9  E8 5E AC 27 00                  call 0x140a1af4c
007A02EE  48 81 C4 98 00 00 00            add rsp, 0x98
007A02F5  C3                              ret
007A02F6  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NtAccessCheckByTypeResultListAndAuditAlarm(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, unsigned int a7, unsigned int a8, unsigned int a9, __int64 a10, unsigned int a11, __int64 a12, __int64 a13, __int64 a14, __int64 a15, __int64 a16)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_m40;
    unsigned int v_stack_m50;
    unsigned int v_stack_m58;
    unsigned int v_stack_m60;

    v_rsp = (v_rsp) - (152);
    *(unsigned __int8 *)(v_rsp - 24) = 1;
    *(unsigned __int64 *)(v_rsp - 32) = a16;
    *(unsigned __int64 *)(v_rsp - 40) = a15;
    *(unsigned __int64 *)(v_rsp - 48) = a14;
    *(unsigned __int64 *)(v_rsp - 56) = a12;
    v_stack_m40 = (unsigned int)((unsigned int)(a11));
    *(unsigned __int64 *)(v_rsp - 72) = a10;
    v_stack_m50 = (unsigned int)((unsigned int)(a9));
    v_stack_m58 = (unsigned int)((unsigned int)(a8));
    v_stack_m60 = (unsigned int)((unsigned int)(a7));
    *(unsigned __int64 *)(v_rsp - 104) = a6;
    *(unsigned __int64 *)(v_rsp - 112) = a5;
    *(unsigned __int64 *)(v_rsp - 120) = a4;
    a3 = 0;
    result = SepAccessCheckAndAuditAlarm(a1, a2, a3, a3);
    v_rsp = (v_rsp) + (152);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t NtAccessCheckByTypeResultListAndAuditAlarm(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5, int64_t Arg6, uint32_t Arg7, uint32_t Arg8, uint32_t Arg9, int64_t Arg10, uint32_t Arg11, int64_t Arg12, uint64_t Arg13, int64_t Arg14, int64_t Arg15, int64_t Arg16)
{
    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_m40;
    uint32_t v_stack_m50;
    uint32_t v_stack_m58;
    uint32_t v_stack_m60;

    local_rsp = (local_rsp) - (152);
    *(uint8_t *)(local_rsp - 0x18) = 1;
    *(uint64_t *)(local_rsp - 0x20) = Arg16;
    *(uint64_t *)(local_rsp - 0x28) = Arg15;
    *(uint64_t *)(local_rsp - 0x30) = Arg14;
    *(uint64_t *)(local_rsp - 0x38) = Arg12;
    v_stack_m40 = (uint32_t)((uint32_t)(Arg11));
    *(uint64_t *)(local_rsp - 0x48) = Arg10;
    v_stack_m50 = (uint32_t)((uint32_t)(Arg9));
    v_stack_m58 = (uint32_t)((uint32_t)(Arg8));
    v_stack_m60 = (uint32_t)((uint32_t)(Arg7));
    *(uint64_t *)(local_rsp - 0x68) = Arg6;
    *(uint64_t *)(local_rsp - 0x70) = Arg5;
    *(uint64_t *)(local_rsp - 0x78) = Arg4;
    Arg3 = 0;
    result = SepAccessCheckAndAuditAlarm(Arg1, Arg2, Arg3, Arg3);
    local_rsp = (local_rsp) + (152);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007A0250&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007A0250[BB_007A0250]
  bb_007A02F6[BB_007A02F6]
```
