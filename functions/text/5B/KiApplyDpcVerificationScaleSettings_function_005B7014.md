# KiApplyDpcVerificationScaleSettings

- RVA: `0x005B7014`–`0x005B707F` (길이 `107` bytes)
- VA: `0x00000001405B7014`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `23`개 명령, `107/107` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **14**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [KeUpdateDpcWatchdogConfiguration](KeUpdateDpcWatchdogConfiguration_function_005B5A34.md) at `0x005B5B9E`
- [KeInitSystem](../../init/C7/KeInitSystem_function_00C71660.md) at `0x00C71857`

### Static image references
- `0x005B7014` → RVA `0x00F04984` (`.data`; read)
- `0x005B701D` → RVA `0x00FC5058` (`ALMOSTRO`; read)
- `0x005B7023` → RVA `0x00FC502C` (`ALMOSTRO`; read)
- `0x005B702C` → RVA `0x00FC502C` (`ALMOSTRO`; write)
- `0x005B7032` → RVA `0x00FC5034` (`ALMOSTRO`; read)
- `0x005B703B` → RVA `0x00FC5034` (`ALMOSTRO`; write)
- `0x005B7041` → RVA `0x00FC5040` (`ALMOSTRO`; read)
- `0x005B704A` → RVA `0x00FC5040` (`ALMOSTRO`; write)
- `0x005B7050` → RVA `0x00FC503C` (`ALMOSTRO`; read)
- `0x005B7059` → RVA `0x00FC503C` (`ALMOSTRO`; write)
- `0x005B705F` → RVA `0x00FC5028` (`ALMOSTRO`; read)
- `0x005B7068` → RVA `0x00FC5028` (`ALMOSTRO`; write)
- `0x005B706E` → RVA `0x00FC5024` (`ALMOSTRO`; read)
- `0x005B7077` → RVA `0x00FC5024` (`ALMOSTRO`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005B7014  83 3D 69 D9 94 00 00            cmp dword ptr [rip + 0x94d969], 0
005B701B  74 60                           je 0x1405b707d
005B701D  8B 0D 35 E0 A0 00               mov ecx, dword ptr [rip + 0xa0e035]
005B7023  8B 05 03 E0 A0 00               mov eax, dword ptr [rip + 0xa0e003]
005B7029  0F AF C1                        imul eax, ecx
005B702C  89 05 FA DF A0 00               mov dword ptr [rip + 0xa0dffa], eax
005B7032  8B 05 FC DF A0 00               mov eax, dword ptr [rip + 0xa0dffc]
005B7038  0F AF C1                        imul eax, ecx
005B703B  89 05 F3 DF A0 00               mov dword ptr [rip + 0xa0dff3], eax
005B7041  8B 05 F9 DF A0 00               mov eax, dword ptr [rip + 0xa0dff9]
005B7047  0F AF C1                        imul eax, ecx
005B704A  89 05 F0 DF A0 00               mov dword ptr [rip + 0xa0dff0], eax
005B7050  8B 05 E6 DF A0 00               mov eax, dword ptr [rip + 0xa0dfe6]
005B7056  0F AF C1                        imul eax, ecx
005B7059  89 05 DD DF A0 00               mov dword ptr [rip + 0xa0dfdd], eax
005B705F  8B 05 C3 DF A0 00               mov eax, dword ptr [rip + 0xa0dfc3]
005B7065  0F AF C1                        imul eax, ecx
005B7068  89 05 BA DF A0 00               mov dword ptr [rip + 0xa0dfba], eax
005B706E  8B 05 B0 DF A0 00               mov eax, dword ptr [rip + 0xa0dfb0]
005B7074  0F AF C1                        imul eax, ecx
005B7077  89 05 A7 DF A0 00               mov dword ptr [rip + 0xa0dfa7], eax
005B707D  C3                              ret
005B707E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiApplyDpcVerificationScaleSettings(void)
{
    __int64 result;

    if ((*(unsigned int *)(v_rip + 9754985)) != 0) {
        a1 = *(unsigned int *)(v_rip + 10543157);
        result = *(unsigned int *)(v_rip + 10543107);
        result = (unsigned int)((result) * ((unsigned int)(a1)));
        *(unsigned int *)(v_rip + 10543098) = (unsigned int)(result);
        result = *(unsigned int *)(v_rip + 10543100);
        result = (unsigned int)((result) * ((unsigned int)(a1)));
        *(unsigned int *)(v_rip + 10543091) = (unsigned int)(result);
        result = *(unsigned int *)(v_rip + 10543097);
        result = (unsigned int)((result) * ((unsigned int)(a1)));
        *(unsigned int *)(v_rip + 10543088) = (unsigned int)(result);
        result = *(unsigned int *)(v_rip + 10543078);
        result = (unsigned int)((result) * ((unsigned int)(a1)));
        *(unsigned int *)(v_rip + 10543069) = (unsigned int)(result);
        result = *(unsigned int *)(v_rip + 10543043);
        result = (unsigned int)((result) * ((unsigned int)(a1)));
        *(unsigned int *)(v_rip + 10543034) = (unsigned int)(result);
        result = *(unsigned int *)(v_rip + 10543024);
        result = (unsigned int)((result) * ((unsigned int)(a1)));
        *(unsigned int *)(v_rip + 10543015) = (unsigned int)(result);
    }
    return result;
}
```

## 5. (Beta) C Style

```c
void KiApplyDpcVerificationScaleSettings(void)
{
    int64_t result;

    if ((*(uint32_t *)(v_rip + 0x94D969)) != 0) {
        a1 = *(uint32_t *)(v_rip + 0xA0E035);
        result = *(uint32_t *)(v_rip + 0xA0E003);
        result = (uint32_t)((result) * ((uint32_t)(a1)));
        *(uint32_t *)(v_rip + 0xA0DFFA) = (uint32_t)(result);
        result = *(uint32_t *)(v_rip + 0xA0DFFC);
        result = (uint32_t)((result) * ((uint32_t)(a1)));
        *(uint32_t *)(v_rip + 0xA0DFF3) = (uint32_t)(result);
        result = *(uint32_t *)(v_rip + 0xA0DFF9);
        result = (uint32_t)((result) * ((uint32_t)(a1)));
        *(uint32_t *)(v_rip + 0xA0DFF0) = (uint32_t)(result);
        result = *(uint32_t *)(v_rip + 0xA0DFE6);
        result = (uint32_t)((result) * ((uint32_t)(a1)));
        *(uint32_t *)(v_rip + 0xA0DFDD) = (uint32_t)(result);
        result = *(uint32_t *)(v_rip + 0xA0DFC3);
        result = (uint32_t)((result) * ((uint32_t)(a1)));
        *(uint32_t *)(v_rip + 0xA0DFBA) = (uint32_t)(result);
        result = *(uint32_t *)(v_rip + 0xA0DFB0);
        result = (uint32_t)((result) * ((uint32_t)(a1)));
        *(uint32_t *)(v_rip + 0xA0DFA7) = (uint32_t)(result);
    }
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005B7014&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005B7014[BB_005B7014]
  bb_005B701D[BB_005B701D]
  bb_005B707D[BB_005B707D]
  bb_005B707E[BB_005B707E]
  bb_005B7014 -->|branch| bb_005B707D
  bb_005B7014 -->|fallthrough| bb_005B701D
  bb_005B701D -->|flow| bb_005B707D
```
