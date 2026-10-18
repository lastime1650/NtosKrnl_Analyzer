# CmDoVirtualTest

- RVA: `0x004AB560`–`0x004AB599` (길이 `57` bytes)
- VA: `0x00000001404AB560`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00069B1C`
- 디코드: `16`개 명령, `57/57` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x004AB585` → [CmpIsSystemEntity](../../page/8B/CmpIsSystemEntity_function_008B4E90.md) (function, `0x008B4E90`)

### Direct callers
- [NtRenameKey](../../page/7E/NtRenameKey_function_007E04B0.md) at `0x007E0739`
- [NtDeleteKey](../../page/84/NtDeleteKey_function_00849920.md) at `0x00849D09`

### Static image references
- `0x004AB564` → RVA `0x00E0ECA0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x004AB585` → [CmpIsSystemEntity](../../page/8B/CmpIsSystemEntity_function_008B4E90.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004AB560  48 83 EC 28                     sub rsp, 0x28
004AB564  80 3D 35 37 96 00 00            cmp byte ptr [rip + 0x963735], 0
004AB56B  48 8B C1                        mov rax, rcx
004AB56E  74 25                           je 0x1404ab595
004AB570  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
004AB579  4C 8B C2                        mov r8, rdx
004AB57C  48 8B D0                        mov rdx, rax
004AB57F  8A 89 32 02 00 00               mov cl, byte ptr [rcx + 0x232]
004AB585  E8 06 99 40 00                  call 0x1408b4e90
004AB58A  84 C0                           test al, al
004AB58C  0F 94 C0                        sete al
004AB58F  48 83 C4 28                     add rsp, 0x28
004AB593  C3                              ret
004AB594  CC                              int3
004AB595  32 C0                           xor al, al
004AB597  EB F6                           jmp 0x1404ab58f
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmDoVirtualTest(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if ((*(unsigned __int8 *)(v_rip + 9844533)) == 0) goto loc_004AB595;
    result = CmpIsSystemEntity(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562), a1, a2, a4);
    result = ((unsigned __int8)(result) == 0) ? 1 : 0;
loc_004AB58F:
    v_rsp = (v_rsp) + (40);
    return result;
loc_004AB595:
    result = 0;
    goto loc_004AB58F;
}
```

## 5. (Beta) C Style

```c
int64_t CmDoVirtualTest(int64_t Arg1, int64_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if ((*(uint8_t *)(v_rip + 0x963735)) == 0) goto loc_004AB595;
    result = CmpIsSystemEntity(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232), Arg1, Arg2, a4);
    result = ((uint8_t)(result) == 0) ? 1 : 0;
loc_004AB58F:
    local_rsp = (local_rsp) + (40);
    return result;
loc_004AB595:
    result = 0;
    goto loc_004AB58F;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004AB560&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004AB560[BB_004AB560]
  bb_004AB570[BB_004AB570]
  bb_004AB58F[BB_004AB58F]
  bb_004AB594[BB_004AB594]
  bb_004AB595[BB_004AB595]
  bb_004AB560 -->|branch| bb_004AB595
  bb_004AB560 -->|fallthrough| bb_004AB570
  bb_004AB570 -->|flow| bb_004AB58F
  bb_004AB594 -->|flow| bb_004AB595
  bb_004AB595 -->|branch| bb_004AB58F
```
