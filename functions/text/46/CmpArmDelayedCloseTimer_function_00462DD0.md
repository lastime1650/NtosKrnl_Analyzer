# CmpArmDelayedCloseTimer

- RVA: `0x00462DD0`–`0x00462DF7` (길이 `39` bytes)
- VA: `0x0000000140462DD0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `11`개 명령, `39/39` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00462DEC` → [ExQueueWorkItem](../2F/ExQueueWorkItem_function_002F9520.md) (function, `0x002F9520`)

### Direct callers
- [CmpAddToDelayedClose](../../page/84/CmpAddToDelayedClose_function_0084FBC0.md) at `0x0084FCC9`
- [CmpPerformCompleteKcbCacheLookup](../../page/84/CmpPerformCompleteKcbCacheLookup_function_0084FD20.md) at `0x008506CB`
- [sub_008515D5](../../page/85/Unknown_function_008515D5.md) at `0x008518AA`
- [sub_00862E81](../../page/86/Unknown_function_00862E81.md) at `0x00863001`

### Static image references
- `0x00462DDB` → RVA `0x00EEFC34` (`.data`; read/write)
- `0x00462DE5` → RVA `0x00EF58C0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00462DD0  48 83 EC 28                     sub rsp, 0x28
00462DD4  BA 01 00 00 00                  mov edx, 1
00462DD9  8B C2                           mov eax, edx
00462DDB  87 05 53 CE A8 00               xchg dword ptr [rip + 0xa8ce53], eax
00462DE1  85 C0                           test eax, eax
00462DE3  75 0C                           jne 0x140462df1
00462DE5  48 8D 0D D4 2A A9 00            lea rcx, [rip + 0xa92ad4]
00462DEC  E8 2F 67 E9 FF                  call 0x1402f9520
00462DF1  48 83 C4 28                     add rsp, 0x28
00462DF5  C3                              ret
00462DF6  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpArmDelayedCloseTimer(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = 1;
    if (1 == 0) {
        a1 = v_rip + 11086548;
        result = ExQueueWorkItem(a1, 1, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void CmpArmDelayedCloseTimer(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = 1;
    if (1 == 0) {
        a1 = v_rip + 11086548;
        result = ExQueueWorkItem(a1, 1, a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00462DD0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00462DD0[BB_00462DD0]
  bb_00462DE5[BB_00462DE5]
  bb_00462DF1[BB_00462DF1]
  bb_00462DF6[BB_00462DF6]
  bb_00462DD0 -->|branch| bb_00462DF1
  bb_00462DD0 -->|fallthrough| bb_00462DE5
  bb_00462DE5 -->|flow| bb_00462DF1
```
