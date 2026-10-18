# KeRegisterNmiCallback

- RVA: `0x005B1BE0`–`0x005B1C5E` (길이 `126` bytes)
- VA: `0x00000001405B1BE0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060BC4`
- 디코드: `32`개 명령, `126/126` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x005B1C03` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x005B1C25` → [KeAcquireSpinLockRaiseToDpc](../20/KeAcquireSpinLockRaiseToDpc_function_00208470.md) (function, `0x00208470`)
- `0x005B1C44` → [KeReleaseSpinLock](../39/KeReleaseSpinLock_function_00392BA0.md) (function, `0x00392BA0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x005B1C12` → RVA `0x00F475B0` (`.data`; read)
- `0x005B1C2A` → RVA `0x00F475A8` (`.data`; read)
- `0x005B1C3D` → RVA `0x00F475A8` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x005B1C03` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005B1BE0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
005B1BE5  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
005B1BEA  57                              push rdi
005B1BEB  48 83 EC 20                     sub rsp, 0x20
005B1BEF  48 8B FA                        mov rdi, rdx
005B1BF2  48 8B F1                        mov rsi, rcx
005B1BF5  BA 20 00 00 00                  mov edx, 0x20
005B1BFA  41 B8 4B 4E 4D 49               mov r8d, 0x494d4e4b
005B1C00  8D 4A 20                        lea ecx, [rdx + 0x20]
005B1C03  E8 E8 04 5D 00                  call 0x140b820f0
005B1C08  48 8B D8                        mov rbx, rax
005B1C0B  33 C0                           xor eax, eax
005B1C0D  48 85 DB                        test rbx, rbx
005B1C10  74 3B                           je 0x1405b1c4d
005B1C12  48 8D 0D 97 59 99 00            lea rcx, [rip + 0x995997]
005B1C19  48 89 73 08                     mov qword ptr [rbx + 8], rsi
005B1C1D  48 89 7B 10                     mov qword ptr [rbx + 0x10], rdi
005B1C21  48 89 5B 18                     mov qword ptr [rbx + 0x18], rbx
005B1C25  E8 46 68 C5 FF                  call 0x140208470
005B1C2A  48 8B 15 77 59 99 00            mov rdx, qword ptr [rip + 0x995977]
005B1C31  48 8D 0D 78 59 99 00            lea rcx, [rip + 0x995978]
005B1C38  48 89 13                        mov qword ptr [rbx], rdx
005B1C3B  8A D0                           mov dl, al
005B1C3D  48 89 1D 64 59 99 00            mov qword ptr [rip + 0x995964], rbx
005B1C44  E8 57 0F DE FF                  call 0x140392ba0
005B1C49  48 8B 43 18                     mov rax, qword ptr [rbx + 0x18]
005B1C4D  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
005B1C52  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
005B1C57  48 83 C4 20                     add rsp, 0x20
005B1C5B  5F                              pop rdi
005B1C5C  C3                              ret
005B1C5D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KeRegisterNmiCallback(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_rsp = (v_rsp) - (32);
    result = ExAllocatePool2(32 + 32, 32, (unsigned int)(0x494D4E4BULL), a4);
    result = 0;
    if (0 != 0) {
        a1 = v_rip + 10049943;
        *(unsigned __int64 *)(result + 8) = a1;
        *(unsigned __int64 *)(result + 16) = a2;
        *(unsigned __int64 *)(result + 24) = 0;
        result = KeAcquireSpinLockRaiseToDpc(a1, 32, (unsigned int)(0x494D4E4BULL), a4);
        a2 = *(unsigned __int64 *)(v_rip + 10049911);
        a1 = v_rip + 10049912;
        *(unsigned __int64 *)(result) = a2;
        a2 = (unsigned __int8)(result);
        *(unsigned __int64 *)(v_rip + 10049892) = result;
        result = KeReleaseSpinLock(a1, a2, (unsigned int)(0x494D4E4BULL), a4);
        result = *(unsigned __int64 *)(result + 24);
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KeRegisterNmiCallback(int64_t Arg1, int64_t Arg2)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    local_rsp = (local_rsp) - (32);
    result = ExAllocatePool2(32 + 32, 32, (uint32_t)(0x494D4E4BULL), a4);
    result = 0;
    if (0 != 0) {
        Arg1 = v_rip + 10049943;
        *(uint64_t *)(result + 0x8) = Arg1;
        *(uint64_t *)(result + 0x10) = Arg2;
        *(uint64_t *)(result + 0x18) = 0;
        result = KeAcquireSpinLockRaiseToDpc(Arg1, 32, (uint32_t)(0x494D4E4BULL), a4);
        Arg2 = *(uint64_t *)(v_rip + 0x995977);
        Arg1 = v_rip + 10049912;
        *(uint64_t *)(result) = Arg2;
        Arg2 = (uint8_t)(result);
        *(uint64_t *)(v_rip + 0x995964) = result;
        result = KeReleaseSpinLock(Arg1, Arg2, (uint32_t)(0x494D4E4BULL), a4);
        result = *(uint64_t *)(result + 0x18);
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005B1BE0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005B1BE0[BB_005B1BE0]
  bb_005B1C12[BB_005B1C12]
  bb_005B1C4D[BB_005B1C4D]
  bb_005B1C5D[BB_005B1C5D]
  bb_005B1BE0 -->|branch| bb_005B1C4D
  bb_005B1BE0 -->|fallthrough| bb_005B1C12
  bb_005B1C12 -->|flow| bb_005B1C4D
```
