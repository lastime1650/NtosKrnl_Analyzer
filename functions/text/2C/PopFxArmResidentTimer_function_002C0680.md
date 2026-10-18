# PopFxArmResidentTimer

- RVA: `0x002C0680`–`0x002C0707` (길이 `135` bytes)
- VA: `0x00000001402C0680`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006E5F8`
- 디코드: `32`개 명령, `135/135` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **7**

### Outgoing calls
- `0x002C0693` → [ExAcquireSpinLockExclusive](../24/ExAcquireSpinLockExclusive_function_00248690.md) (function, `0x00248690`)
- `0x002C06E7` → [KeSetCoalescableTimer](../22/KeSetCoalescableTimer_function_0022FFD0.md) (function, `0x0022FFD0`)
- `0x002C06F6` → [ExReleaseSpinLockExclusive](ExReleaseSpinLockExclusive_function_002C0EF0.md) (function, `0x002C0EF0`)

### Direct callers
- [PopFxIdleComponent](PopFxIdleComponent_function_002C01D8.md) at `0x002C03B8`
- [PopFxResidentTimeoutRoutine](../46/PopFxResidentTimeoutRoutine_function_00462650.md) at `0x00462779`
- [PopFxResidentTimeoutDpcRoutine](../4A/PopFxResidentTimeoutDpcRoutine_function_004A54C0.md) at `0x004A54E5`

### Static image references
- `0x002C068C` → RVA `0x00F0E420` (`.data`; read)
- `0x002C069F` → RVA `0x00F0E434` (`.data`; write)
- `0x002C06A6` → RVA `0x00F0E434` (`.data`; read)
- `0x002C06AF` → RVA `0x00F0E430` (`.data`; read)
- `0x002C06B9` → RVA `0x00E0B3D8` (`.data`; read)
- `0x002C06C0` → RVA `0x00F0E440` (`.data`; read)
- `0x002C06D1` → RVA `0x00F0E480` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002C0680  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
002C0685  57                              push rdi
002C0686  48 83 EC 30                     sub rsp, 0x30
002C068A  8A D9                           mov bl, cl
002C068C  48 8D 0D 8D DD C4 00            lea rcx, [rip + 0xc4dd8d]
002C0693  E8 F8 7F F8 FF                  call 0x140248690
002C0698  40 8A F8                        mov dil, al
002C069B  84 DB                           test bl, bl
002C069D  74 07                           je 0x1402c06a6
002C069F  C6 05 8E DD C4 00 00            mov byte ptr [rip + 0xc4dd8e], 0
002C06A6  80 3D 87 DD C4 00 00            cmp byte ptr [rip + 0xc4dd87], 0
002C06AD  75 3D                           jne 0x1402c06ec
002C06AF  8B 0D 7B DD C4 00               mov ecx, dword ptr [rip + 0xc4dd7b]
002C06B5  85 C9                           test ecx, ecx
002C06B7  7E 33                           jle 0x1402c06ec
002C06B9  44 8B 0D 18 AD B4 00            mov r9d, dword ptr [rip + 0xb4ad18]
002C06C0  48 8D 05 79 DD C4 00            lea rax, [rip + 0xc4dd79]
002C06C7  49 69 D1 F0 D8 FF FF            imul rdx, r9, -0x2710
002C06CE  41 D1 E9                        shr r9d, 1
002C06D1  48 8D 0D A8 DD C4 00            lea rcx, [rip + 0xc4dda8]
002C06D8  45 33 C0                        xor r8d, r8d
002C06DB  C6 05 52 DD C4 00 01            mov byte ptr [rip + 0xc4dd52], 1
002C06E2  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
002C06E7  E8 E4 F8 F6 FF                  call 0x14022ffd0
002C06EC  40 8A D7                        mov dl, dil
002C06EF  48 8D 0D 2A DD C4 00            lea rcx, [rip + 0xc4dd2a]
002C06F6  E8 F5 07 00 00                  call 0x1402c0ef0
002C06FB  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
002C0700  48 83 C4 30                     add rsp, 0x30
002C0704  5F                              pop rdi
002C0705  C3                              ret
002C0706  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopFxArmResidentTimer(unsigned __int8 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (48);
    result = ExAcquireSpinLockExclusive(v_rip + 12901773, a2, a3, a4);
    if (a1 != 0) {
        *(unsigned __int8 *)(v_rip + 12901774) = 0;
    }
    if ((*(unsigned __int8 *)(v_rip + 12901767)) != 0) goto loc_002C06EC;
    if (!(condition_is_less_or_equal)) {
        a4 = *(unsigned int *)(v_rip + 11840792);
        result = v_rip + 12901753;
        a2 = (a2) * (a4);
        a4 = (unsigned int)((a4) >> (1));
        a1 = v_rip + 12901800;
        a3 = 0;
        *(unsigned __int8 *)(v_rip + 12901714) = 1;
        v_stack_m18 = result;
        result = KeSetCoalescableTimer(a1, a2, a3, a4);
    }
    result = ExReleaseSpinLockExclusive(v_rip + 12901674, (unsigned __int8)((unsigned __int8)(result)), a3, a4);
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopFxArmResidentTimer(uint8_t Arg1, int64_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (48);
    result = ExAcquireSpinLockExclusive(v_rip + 12901773, Arg2, Arg3, a4);
    if (Arg1 != 0) {
        *(uint8_t *)(v_rip + 0xC4DD8E) = 0;
    }
    if ((*(uint8_t *)(v_rip + 0xC4DD87)) != 0) goto loc_002C06EC;
    if (!(condition_is_less_or_equal)) {
        a4 = *(uint32_t *)(v_rip + 0xB4AD18);
        result = v_rip + 12901753;
        Arg2 = (Arg2) * (a4);
        a4 = (uint32_t)((a4) >> (1));
        Arg1 = v_rip + 12901800;
        Arg3 = 0;
        *(uint8_t *)(v_rip + 0xC4DD52) = 1;
        v_stack_m18 = result;
        result = KeSetCoalescableTimer(Arg1, Arg2, Arg3, a4);
    }
    result = ExReleaseSpinLockExclusive(v_rip + 12901674, (uint8_t)((uint8_t)(result)), Arg3, a4);
    local_rsp = (local_rsp) + (48);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002C0680&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002C0680[BB_002C0680]
  bb_002C069F[BB_002C069F]
  bb_002C06A6[BB_002C06A6]
  bb_002C06AF[BB_002C06AF]
  bb_002C06B9[BB_002C06B9]
  bb_002C06EC[BB_002C06EC]
  bb_002C0706[BB_002C0706]
  bb_002C0680 -->|branch| bb_002C06A6
  bb_002C0680 -->|fallthrough| bb_002C069F
  bb_002C069F -->|flow| bb_002C06A6
  bb_002C06A6 -->|branch| bb_002C06EC
  bb_002C06A6 -->|fallthrough| bb_002C06AF
  bb_002C06AF -->|branch| bb_002C06EC
  bb_002C06AF -->|fallthrough| bb_002C06B9
  bb_002C06B9 -->|flow| bb_002C06EC
```
