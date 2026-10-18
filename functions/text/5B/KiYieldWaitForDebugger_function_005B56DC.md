# KiYieldWaitForDebugger

- RVA: `0x005B56DC`–`0x005B56FB` (길이 `31` bytes)
- VA: `0x00000001405B56DC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007E574`
- 디코드: `9`개 명령, `31/31` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x005B56F2` → [KiCheckForFreezeExecution](KiCheckForFreezeExecution_function_005B41E0.md) (function, `0x005B41E0`)

### Direct callers
- [KeBugCheck2](KeBugCheck2_function_005B27D0.md) at `0x005B336A`
- [KiAttemptBugcheckRecovery](../5C/KiAttemptBugcheckRecovery_function_005C6D24.md) at `0x005C7044`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005B56DC  48 83 EC 28                     sub rsp, 0x28
005B56E0  65 66 8B 04 25 26 85 00 00      mov ax, word ptr gs:[0x8526]
005B56E9  66 85 C0                        test ax, ax
005B56EC  74 09                           je 0x1405b56f7
005B56EE  33 D2                           xor edx, edx
005B56F0  33 C9                           xor ecx, ecx
005B56F2  E8 E9 EA FF FF                  call 0x1405b41e0
005B56F7  F3 90                           pause
005B56F9  EB E5                           jmp 0x1405b56e0
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiYieldWaitForDebugger(int a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
loc_005B56E0:
    result = *(unsigned __int16 *)(gs_base + (0 + 34086));
    if ((unsigned __int16)(*(unsigned __int16 *)(gs_base + (0 + 34086))) != 0) {
        a2 = 0;
        a1 = 0;
        result = KiCheckForFreezeExecution(a1, a2, a3, a4);
    }
    goto loc_005B56E0;
}
```

## 5. (Beta) C Style

```c
int64_t KiYieldWaitForDebugger(int32_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
loc_005B56E0:
    result = *(uint16_t *)(gs_base + (0 + 0x8526));
    if ((uint16_t)(*(uint16_t *)(gs_base + (0 + 0x8526))) != 0) {
        Arg2 = 0;
        Arg1 = 0;
        result = KiCheckForFreezeExecution(Arg1, Arg2, a3, a4);
    }
    goto loc_005B56E0;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005B56DC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005B56DC[BB_005B56DC]
  bb_005B56E0[BB_005B56E0]
  bb_005B56EE[BB_005B56EE]
  bb_005B56F7[BB_005B56F7]
  bb_005B56DC -->|flow| bb_005B56E0
  bb_005B56E0 -->|branch| bb_005B56F7
  bb_005B56E0 -->|fallthrough| bb_005B56EE
  bb_005B56EE -->|flow| bb_005B56F7
  bb_005B56F7 -->|branch| bb_005B56E0
```
