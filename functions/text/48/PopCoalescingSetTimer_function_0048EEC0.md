# PopCoalescingSetTimer

- RVA: `0x0048EEC0`–`0x0048EF1B` (길이 `91` bytes)
- VA: `0x000000014048EEC0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B29C4`
- 디코드: `19`개 명령, `91/91` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **6**

### Outgoing calls
- `0x0048EEDF` → [PopPrintEx](PopPrintEx_function_0048EF24.md) (function, `0x0048EF24`)
- `0x0048EF0B` → [KiSetTimerEx](../23/KiSetTimerEx_function_00232CB0.md) (function, `0x00232CB0`)

### Direct callers
- [PopCoalescingSetActiveState](../4B/PopCoalescingSetActiveState_function_004B7E18.md) at `0x004B7E87`
- [PopCoalescingNotify](../../page/75/PopCoalescingNotify_function_0075C0E0.md) at `0x0075C13B`

### Static image references
- `0x0048EEC4` → RVA `0x00F0E068` (`.data`; read)
- `0x0048EED3` → RVA `0x006CBF20` (` ?? ::FNODOBFM::`string'`; read)
- `0x0048EEE4` → RVA `0x00E0B544` (`.data`; read)
- `0x0048EEEB` → RVA `0x00F0E000` (`.data`; read)
- `0x0048EEF9` → RVA `0x00F0DFC0` (`.data`; read)
- `0x0048EF10` → RVA `0x00F0E000` (`.data`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0048EEC0  48 83 EC 38                     sub rsp, 0x38
0048EEC4  F6 05 9D F1 A7 00 01            test byte ptr [rip + 0xa7f19d], 1
0048EECB  75 06                           jne 0x14048eed3
0048EECD  48 83 C4 38                     add rsp, 0x38
0048EED1  C3                              ret
0048EED2  CC                              int3
0048EED3  48 8D 15 46 D0 23 00            lea rdx, [rip + 0x23d046]
0048EEDA  B9 03 00 00 00                  mov ecx, 3
0048EEDF  E8 40 00 00 00                  call 0x14048ef24
0048EEE4  48 63 05 59 C6 97 00            movsxd rax, dword ptr [rip + 0x97c659]
0048EEEB  48 8D 0D 0E F1 A7 00            lea rcx, [rip + 0xa7f10e]
0048EEF2  48 69 D0 80 69 67 FF            imul rdx, rax, -0x989680
0048EEF9  48 8D 05 C0 F0 A7 00            lea rax, [rip + 0xa7f0c0]
0048EF00  45 33 C9                        xor r9d, r9d
0048EF03  45 33 C0                        xor r8d, r8d
0048EF06  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0048EF0B  E8 A0 3D DA FF                  call 0x140232cb0
0048EF10  F0 0F BA 2D E7 F0 A7 00 09      lock bts dword ptr [rip + 0xa7f0e7], 9
0048EF19  EB B2                           jmp 0x14048eecd
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopCoalescingSetTimer(__int64 a1, __int64 a2, int a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p20;

    v_rsp = (v_rsp) - (56);
    if (((*(unsigned __int8 *)(v_rip + 11006365)) & (1)) != 0) goto loc_0048EED3;
loc_0048EECD:
    v_rsp = (v_rsp) + (56);
    return result;
loc_0048EED3:
    result = PopPrintEx(3, v_rip + 2347078, a3, a4);
    a2 = (v_rip + 2347078) * ((int)(*(unsigned int *)(v_rip + 9946713)));
    a4 = 0;
    a3 = 0;
    v_stack_p20 = v_rip + 11006144;
    result = KiSetTimerEx(v_rip + 11006222, a2, a3, a4);
    goto loc_0048EECD;
}
```

## 5. (Beta) C Style

```c
int64_t PopCoalescingSetTimer(int64_t Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p20;

    local_rsp = (local_rsp) - (56);
    if (((*(uint8_t *)(v_rip + 0xA7F19D)) & (1)) != 0) goto loc_0048EED3;
loc_0048EECD:
    local_rsp = (local_rsp) + (56);
    return result;
loc_0048EED3:
    result = PopPrintEx(3, v_rip + 2347078, Arg3, Arg4);
    Arg2 = (v_rip + 2347078) * ((int32_t)(*(uint32_t *)(v_rip + 0x97C659)));
    Arg4 = 0;
    Arg3 = 0;
    v_stack_p20 = v_rip + 11006144;
    result = KiSetTimerEx(v_rip + 11006222, Arg2, Arg3, Arg4);
    goto loc_0048EECD;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0048EEC0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0048EEC0[BB_0048EEC0]
  bb_0048EECD[BB_0048EECD]
  bb_0048EED2[BB_0048EED2]
  bb_0048EED3[BB_0048EED3]
  bb_0048EEC0 -->|branch| bb_0048EED3
  bb_0048EEC0 -->|fallthrough| bb_0048EECD
  bb_0048EED2 -->|flow| bb_0048EED3
  bb_0048EED3 -->|branch| bb_0048EECD
```
