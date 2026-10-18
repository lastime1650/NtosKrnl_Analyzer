# InbvCheckDisplayOwnership

- RVA: `0x00590190`–`0x005901B8` (길이 `40` bytes)
- VA: `0x0000000140590190`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `13`개 명령, `40/40` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x005901A9` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [HaliHaltSystem](../54/HaliHaltSystem_function_005465C0.md) at `0x005465D9`
- [HalpCheckPowerButton](../54/HalpCheckPowerButton_function_00546660.md) at `0x00546679`
- [InbvRotateGuiBootDisplay](InbvRotateGuiBootDisplay_function_00590680.md) at `0x005906BC`

### Static image references
- `0x00590194` → RVA `0x00E65E58` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00590190  48 83 EC 28                     sub rsp, 0x28
00590194  48 8B 05 BD 5C 8D 00            mov rax, qword ptr [rip + 0x8d5cbd]
0059019B  48 85 C0                        test rax, rax
0059019E  74 10                           je 0x1405901b0
005901A0  48 8B 40 40                     mov rax, qword ptr [rax + 0x40]
005901A4  48 85 C0                        test rax, rax
005901A7  74 07                           je 0x1405901b0
005901A9  E8 22 A9 12 00                  call 0x1406baad0
005901AE  EB 02                           jmp 0x1405901b2
005901B0  32 C0                           xor al, al
005901B2  48 83 C4 28                     add rsp, 0x28
005901B6  C3                              ret
005901B7  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall InbvCheckDisplayOwnership(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (*(unsigned __int64 *)(v_rip + 9264317) == 0) goto loc_005901B0;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9264317) + 64) == 0) goto loc_005901B0;
    result = guard_dispatch_icall(a1, a2, a3, a4);
    goto loc_005901B2;
loc_005901B0:
    result = 0;
loc_005901B2:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void InbvCheckDisplayOwnership(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (*(uint64_t *)(v_rip + 0x8D5CBD) == 0) goto loc_005901B0;
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0x8D5CBD) + 0x40) == 0) goto loc_005901B0;
    result = guard_dispatch_icall(a1, a2, a3, a4);
    goto loc_005901B2;
loc_005901B0:
    result = 0;
loc_005901B2:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00590190&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00590190[BB_00590190]
  bb_005901A0[BB_005901A0]
  bb_005901A9[BB_005901A9]
  bb_005901B0[BB_005901B0]
  bb_005901B2[BB_005901B2]
  bb_005901B7[BB_005901B7]
  bb_00590190 -->|branch| bb_005901B0
  bb_00590190 -->|fallthrough| bb_005901A0
  bb_005901A0 -->|branch| bb_005901B0
  bb_005901A0 -->|fallthrough| bb_005901A9
  bb_005901A9 -->|branch| bb_005901B2
  bb_005901B0 -->|flow| bb_005901B2
```
