# KiDpcWatchdog

- RVA: `0x005C8490`–`0x005C84DE` (길이 `78` bytes)
- VA: `0x00000001405C8490`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `21`개 명령, `78/78` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x005C849E` → [KiDpcWatchdogCounterReset](../39/KiDpcWatchdogCounterReset_function_0039D6A0.md) (function, `0x0039D6A0`)
- `0x005C84D2` → [KiRemoveSystemWorkPriorityKick](../26/KiRemoveSystemWorkPriorityKick_function_002631D0.md) (function, `0x002631D0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005C8490  48 83 EC 28                     sub rsp, 0x28
005C8494  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
005C849D  FA                              cli
005C849E  E8 FD 51 DD FF                  call 0x14039d6a0
005C84A3  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
005C84AC  4C 8B 81 B8 8E 00 00            mov r8, qword ptr [rcx + 0x8eb8]
005C84B3  4D 85 C0                        test r8, r8
005C84B6  74 1F                           je 0x1405c84d7
005C84B8  41 0F 0D 08                     prefetchw byte ptr [r8]
005C84BC  41 8B 00                        mov eax, dword ptr [r8]
005C84BF  8B D0                           mov edx, eax
005C84C1  0F BA F2 15                     btr edx, 0x15
005C84C5  F0 41 0F B1 10                  lock cmpxchg dword ptr [r8], edx
005C84CA  75 F3                           jne 0x1405c84bf
005C84CC  0F BA E0 15                     bt eax, 0x15
005C84D0  73 05                           jae 0x1405c84d7
005C84D2  E8 F9 AC C9 FF                  call 0x1402631d0
005C84D7  FB                              sti
005C84D8  48 83 C4 28                     add rsp, 0x28
005C84DC  C3                              ret
005C84DD  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiDpcWatchdog(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = KiDpcWatchdogCounterReset(*(unsigned __int64 *)(gs_base + (0 + 32)), a2, a3, a4);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536) == 0) goto loc_005C84D7;
loc_005C84BF:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536) != 0) goto loc_005C84BF;
    result = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536)));
    if (!(condition_is_above_or_equal)) {
        result = KiRemoveSystemWorkPriorityKick(*(unsigned __int64 *)(gs_base + (0 + 32)), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536))))), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void KiDpcWatchdog(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = KiDpcWatchdogCounterReset(*(uint64_t *)(gs_base + (0 + 0x20)), a2, a3, a4);
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8) == 0) goto loc_005C84D7;
loc_005C84BF:
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8) != 0) goto loc_005C84BF;
    result = (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8)));
    if (!(condition_is_above_or_equal)) {
        result = KiRemoveSystemWorkPriorityKick(*(uint64_t *)(gs_base + (0 + 0x20)), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8))))), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005C8490&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005C8490[BB_005C8490]
  bb_005C84B8[BB_005C84B8]
  bb_005C84BF[BB_005C84BF]
  bb_005C84CC[BB_005C84CC]
  bb_005C84D2[BB_005C84D2]
  bb_005C84D7[BB_005C84D7]
  bb_005C84DD[BB_005C84DD]
  bb_005C8490 -->|branch| bb_005C84D7
  bb_005C8490 -->|fallthrough| bb_005C84B8
  bb_005C84B8 -->|flow| bb_005C84BF
  bb_005C84BF -->|branch| bb_005C84BF
  bb_005C84BF -->|fallthrough| bb_005C84CC
  bb_005C84CC -->|branch| bb_005C84D7
  bb_005C84CC -->|fallthrough| bb_005C84D2
  bb_005C84D2 -->|flow| bb_005C84D7
```
