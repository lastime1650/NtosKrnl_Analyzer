# KeFindFirstSetRightGroupAffinity

- RVA: `0x002CFB10`–`0x002CFB39` (길이 `41` bytes)
- VA: `0x00000001402CFB10`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `15`개 명령, `41/41` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **11**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [sub_00208DED](../20/Unknown_function_00208DED.md) at `0x00208E34`
- [MiSetIdealProcessorThread](MiSetIdealProcessorThread_function_002C760C.md) at `0x002C7682`
- [HalpTimerConfigureInterrupt](../54/HalpTimerConfigureInterrupt_function_00548AB0.md) at `0x00548B44`
- [HalpIommuConfigureInterrupt](../55/HalpIommuConfigureInterrupt_function_00553464.md) at `0x005534E4`
- [KiGetNextClockOwner](../5B/KiGetNextClockOwner_function_005BB5D4.md) at `0x005BB6B1`
- [KiGetNextClockOwner](../5B/KiGetNextClockOwner_function_005BB5D4.md) at `0x005BB745`
- [MiInitializeZeroEngineCurrentPassDpcAffinity](../69/MiInitializeZeroEngineCurrentPassDpcAffinity_function_00699F04.md) at `0x00699FF8`
- [MiWakeOnlyParticipatingProcessorsFromAssignedNode](../69/MiWakeOnlyParticipatingProcessorsFromAssignedNode_function_0069A314.md) at `0x0069A44E`
- [PpmRegisterPerfStates](../../page/75/PpmRegisterPerfStates_function_0075B084.md) at `0x0075B5D5`
- [MiInitializeZeroingDomains](../../page/81/MiInitializeZeroingDomains_function_00810884.md) at `0x008108E1`
- [MiComputeMemoryNodeProcessorAssignments](../../init/C6/MiComputeMemoryNodeProcessorAssignments_function_00C68F8C.md) at `0x00C690EF`
- [MiFindProcessorsForMemoryOnlyNode](../../init/C6/MiFindProcessorsForMemoryOnlyNode_function_00C692FC.md) at `0x00C6940A`

### Static image references
- `0x002CFB28` → RVA `0x00F231B8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002CFB10  48 8B C1                        mov rax, rcx
002CFB13  48 8B 09                        mov rcx, qword ptr [rcx]
002CFB16  48 85 C9                        test rcx, rcx
002CFB19  74 19                           je 0x1402cfb34
002CFB1B  0F B7 40 08                     movzx eax, word ptr [rax + 8]
002CFB1F  C1 E0 06                        shl eax, 6
002CFB22  48 0F BC C9                     bsf rcx, rcx
002CFB26  03 C8                           add ecx, eax
002CFB28  48 8B 05 89 36 C5 00            mov rax, qword ptr [rip + 0xc53689]
002CFB2F  8B 04 88                        mov eax, dword ptr [rax + rcx*4]
002CFB32  C3                              ret
002CFB33  CC                              int3
002CFB34  83 C8 FF                        or eax, 0xffffffff
002CFB37  C3                              ret
002CFB38  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KeFindFirstSetRightGroupAffinity(__int64 a1)
{
    __int64 result;

    if (*(unsigned __int64 *)(a1) == 0) goto loc_002CFB34;
    result = (unsigned int)((*(unsigned __int16 *)(a1 + 8)) << (6));
    a1 = (unsigned int)((*(unsigned __int64 *)(a1)) + ((unsigned int)(result)));
    return (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12924553) + a1 * 4));
loc_002CFB34:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12924553) + a1 * 4))) | (0xFFFFFFFFULL));
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KeFindFirstSetRightGroupAffinity(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    if (*(uint64_t *)(arg1) == 0) goto loc_002CFB34;
    result = (uint32_t)((*(uint16_t *)(arg1 + 0x8)) << (6));
    Arg1 = (uint32_t)((*(uint64_t *)(arg1)) + ((uint32_t)(result)));
    return (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xC53689) + arg1 * 4));
loc_002CFB34:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xC53689) + arg1 * 4))) | (0xFFFFFFFFULL));
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `16` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002CFB10&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002CFB10[BB_002CFB10]
  bb_002CFB1B[BB_002CFB1B]
  bb_002CFB33[BB_002CFB33]
  bb_002CFB34[BB_002CFB34]
  bb_002CFB38[BB_002CFB38]
  bb_002CFB10 -->|branch| bb_002CFB34
  bb_002CFB10 -->|fallthrough| bb_002CFB1B
  bb_002CFB33 -->|flow| bb_002CFB34
```
