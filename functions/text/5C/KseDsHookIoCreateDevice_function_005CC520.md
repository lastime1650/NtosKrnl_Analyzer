# KseDsHookIoCreateDevice

- RVA: `0x005CC520`–`0x005CC5AC` (길이 `140` bytes)
- VA: `0x00000001405CC520`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00093E28`
- 디코드: `39`개 명령, `140/140` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x005CC569` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x005CC58B` → [KsepDsEventIoCreateDevice](KsepDsEventIoCreateDevice_function_005CCD00.md) (function, `0x005CCD00`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x005CC54E` → RVA `0x00E01588` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005CC520  4C 8B DC                        mov r11, rsp
005CC523  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
005CC527  49 89 6B 10                     mov qword ptr [r11 + 0x10], rbp
005CC52B  49 89 73 18                     mov qword ptr [r11 + 0x18], rsi
005CC52F  57                              push rdi
005CC530  41 56                           push r14
005CC532  41 57                           push r15
005CC534  48 83 EC 40                     sub rsp, 0x40
005CC538  48 8B BC 24 90 00 00 00         mov rdi, qword ptr [rsp + 0x90]
005CC540  41 8B F1                        mov esi, r9d
005CC543  44 8A B4 24 88 00 00 00         mov r14b, byte ptr [rsp + 0x88]
005CC54B  48 8B E9                        mov rbp, rcx
005CC54E  48 8B 05 33 50 83 00            mov rax, qword ptr [rip + 0x835033]
005CC555  44 8B BC 24 80 00 00 00         mov r15d, dword ptr [rsp + 0x80]
005CC55D  49 89 7B D8                     mov qword ptr [r11 - 0x28], rdi
005CC561  45 88 73 D0                     mov byte ptr [r11 - 0x30], r14b
005CC565  45 89 7B C8                     mov dword ptr [r11 - 0x38], r15d
005CC569  E8 62 E5 0E 00                  call 0x1406baad0
005CC56E  33 D2                           xor edx, edx
005CC570  8B D8                           mov ebx, eax
005CC572  85 C0                           test eax, eax
005CC574  78 03                           js 0x1405cc579
005CC576  48 8B 17                        mov rdx, qword ptr [rdi]
005CC579  89 5C 24 28                     mov dword ptr [rsp + 0x28], ebx
005CC57D  45 8B CF                        mov r9d, r15d
005CC580  44 8B C6                        mov r8d, esi
005CC583  44 88 74 24 20                  mov byte ptr [rsp + 0x20], r14b
005CC588  48 8B CD                        mov rcx, rbp
005CC58B  E8 70 07 00 00                  call 0x1405ccd00
005CC590  48 8B 6C 24 68                  mov rbp, qword ptr [rsp + 0x68]
005CC595  8B C3                           mov eax, ebx
005CC597  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
005CC59C  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
005CC5A1  48 83 C4 40                     add rsp, 0x40
005CC5A5  41 5F                           pop r15
005CC5A7  41 5E                           pop r14
005CC5A9  5F                              pop rdi
005CC5AA  C3                              ret
005CC5AB  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KseDsHookIoCreateDevice(__int64 a1, int a2, __int64 a3, int a4, unsigned int a5, unsigned __int8 a6, __int64 a7)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_m30;
    unsigned __int8 v_stack_m38;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    v_rsp = (v_rsp) - (64);
    *(unsigned __int64 *)(v_rsp - 40) = a7;
    *(unsigned __int8 *)(v_rsp - 48) = a6;
    *(unsigned int *)(v_rsp - 56) = (unsigned int)((unsigned int)(a5));
    result = guard_dispatch_icall(a1, a2, a3, a4);
    a2 = 0;
    if (!(sign_flag)) {
        a2 = *(unsigned __int64 *)(a7);
    }
    v_stack_m30 = (unsigned int)((unsigned int)((unsigned int)(result)));
    v_stack_m38 = a6;
    result = KsepDsEventIoCreateDevice(a1, a2, (unsigned int)((unsigned int)((unsigned int)(a4))), (unsigned int)((unsigned int)((unsigned int)(a5))));
    v_rsp = (v_rsp) + (64);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
}
```

## 5. (Beta) C Style

```c
int64_t KseDsHookIoCreateDevice(int64_t Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4, uint32_t Arg5, uint8_t Arg6, void *Arg7)
{
    uint8_t *arg7 = (uint8_t *)Arg7;

    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_m30;
    uint8_t v_stack_m38;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    local_rsp = (local_rsp) - (64);
    *(void **)(local_rsp - 0x28) = Arg7;
    *(uint8_t *)(local_rsp - 0x30) = Arg6;
    *(uint32_t *)(local_rsp - 0x38) = (uint32_t)((uint32_t)(Arg5));
    result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    Arg2 = 0;
    if (!(sign_flag)) {
        Arg2 = *(uint64_t *)(arg7);
    }
    v_stack_m30 = (uint32_t)((uint32_t)((uint32_t)(result)));
    v_stack_m38 = Arg6;
    result = KsepDsEventIoCreateDevice(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg4))), (uint32_t)((uint32_t)((uint32_t)(Arg5))));
    local_rsp = (local_rsp) + (64);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg7` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005CC520&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005CC520[BB_005CC520]
  bb_005CC576[BB_005CC576]
  bb_005CC579[BB_005CC579]
  bb_005CC5AB[BB_005CC5AB]
  bb_005CC520 -->|branch| bb_005CC579
  bb_005CC520 -->|fallthrough| bb_005CC576
  bb_005CC576 -->|flow| bb_005CC579
```
