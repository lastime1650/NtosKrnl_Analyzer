# sub_0096BFF0

- RVA: `0x0096BFF0`–`0x0096C051` (길이 `97` bytes)
- VA: `0x000000014096BFF0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000952CC`
- 디코드: `25`개 명령, `97/97` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0096BFF7` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (function, `0x002FE1F0`)
- `0x0096C027` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0096C04A` → [SLQueryLicenseValueInternal](../7C/SLQueryLicenseValueInternal_function_007C93EC.md) (function, `0x007C93EC`)

### Direct callers
- [SPCallServerHandleQueryPolicy](SPCallServerHandleQueryPolicy_function_0096AF24.md) at `0x0096B27C`
- [SPCallServerHandleQueryPolicy](SPCallServerHandleQueryPolicy_function_0096AF24.md) at `0x0096B3E6`
- [SPCallServerHandleQueryPolicy](SPCallServerHandleQueryPolicy_function_0096AF24.md) at `0x0096B931`
- [SPCallServerHandleQueryPolicy](SPCallServerHandleQueryPolicy_function_0096AF24.md) at `0x0096BA8B`
- [SPCallServerHandleQueryPolicy](SPCallServerHandleQueryPolicy_function_0096AF24.md) at `0x0096BAFC`
- [NtQueryLicenseValue](NtQueryLicenseValue_function_0096BCC0.md) at `0x0096BFA6`
- [sub_0096C058](Unknown_function_0096C058.md) at `0x0096C138`

### Static image references
- `0x0096C003` → RVA `0x00FD8490` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x0096BFF7` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (`PAGE` → `.text`)
  - `0x0096C027` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0096BFF0  48 83 EC 48                     sub rsp, 0x48
0096BFF4  4C 8B D9                        mov r11, rcx
0096BFF7  E8 F4 21 99 FF                  call 0x1402fe1f0
0096BFFC  48 8B 88 68 03 00 00            mov rcx, qword ptr [rax + 0x368]
0096C003  48 8B 05 86 C4 66 00            mov rax, qword ptr [rip + 0x66c486]
0096C00A  48 85 C0                        test rax, rax
0096C00D  74 23                           je 0x14096c032
0096C00F  4C 8B 54 24 70                  mov r10, qword ptr [rsp + 0x70]
0096C014  4C 89 54 24 28                  mov qword ptr [rsp + 0x28], r10
0096C019  44 89 4C 24 20                  mov dword ptr [rsp + 0x20], r9d
0096C01E  4D 8B C8                        mov r9, r8
0096C021  4C 8B C2                        mov r8, rdx
0096C024  49 8B D3                        mov rdx, r11
0096C027  E8 A4 EA D4 FF                  call 0x1406baad0
0096C02C  48 83 C4 48                     add rsp, 0x48
0096C030  C3                              ret
0096C031  CC                              int3
0096C032  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
0096C037  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0096C03C  44 89 4C 24 20                  mov dword ptr [rsp + 0x20], r9d
0096C041  4D 8B C8                        mov r9, r8
0096C044  4C 8B C2                        mov r8, rdx
0096C047  49 8B D3                        mov rdx, r11
0096C04A  E8 9D D3 E5 FF                  call 0x1407c93ec
0096C04F  EB DB                           jmp 0x14096c02c
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0096BFF0(__int64 a1, __int64 a2, __int64 a3, int a4, __int64 a5)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m20;
    unsigned int v_stack_m28;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p28;

    v_rsp = (v_rsp) - (72);
    result = PsGetCurrentServerSiloGlobals(a1, a2, a3, a4);
    if (*(unsigned __int64 *)(v_rip + 6734982) == 0) goto loc_0096C032;
    v_stack_m20 = a5;
    v_stack_m28 = a4;
    result = guard_dispatch_icall(*(unsigned __int64 *)(result + 872), a1, a2, a3);
loc_0096C02C:
    v_rsp = (v_rsp) + (72);
    return result;
loc_0096C032:
    v_stack_p28 = a5;
    v_stack_p20 = (unsigned int)(a3);
    result = SLQueryLicenseValueInternal(*(unsigned __int64 *)(result + 872), a1, a1, a2);
    goto loc_0096C02C;
}
```

## 5. (Beta) C Style

```c
int64_t sub_0096BFF0(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4, int64_t Arg5)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m20;
    uint32_t v_stack_m28;
    uint32_t v_stack_p20;
    uint64_t v_stack_p28;

    local_rsp = (local_rsp) - (72);
    result = PsGetCurrentServerSiloGlobals(Arg1, Arg2, Arg3, Arg4);
    if (*(uint64_t *)(v_rip + 0x66C486) == 0) goto loc_0096C032;
    v_stack_m20 = Arg5;
    v_stack_m28 = Arg4;
    result = guard_dispatch_icall(*(uint64_t *)(result + 0x368), Arg1, Arg2, Arg3);
loc_0096C02C:
    local_rsp = (local_rsp) + (72);
    return result;
loc_0096C032:
    v_stack_p28 = Arg5;
    v_stack_p20 = (uint32_t)(Arg3);
    result = SLQueryLicenseValueInternal(*(uint64_t *)(result + 0x368), Arg1, Arg1, Arg2);
    goto loc_0096C02C;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0096BFF0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0096BFF0[BB_0096BFF0]
  bb_0096C00F[BB_0096C00F]
  bb_0096C02C[BB_0096C02C]
  bb_0096C031[BB_0096C031]
  bb_0096C032[BB_0096C032]
  bb_0096BFF0 -->|branch| bb_0096C032
  bb_0096BFF0 -->|fallthrough| bb_0096C00F
  bb_0096C00F -->|flow| bb_0096C02C
  bb_0096C031 -->|flow| bb_0096C032
  bb_0096C032 -->|branch| bb_0096C02C
```
