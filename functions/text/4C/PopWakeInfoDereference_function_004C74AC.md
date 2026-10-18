# PopWakeInfoDereference

- RVA: `0x004C74AC`–`0x004C74E9` (길이 `61` bytes)
- VA: `0x00000001404C74AC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000841D0`
- 디코드: `17`개 명령, `61/61` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **7**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x004C74E2` → [ExQueueWorkItem](../2F/ExQueueWorkItem_function_002F9520.md) (function, `0x002F9520`)

### Direct callers
- [PopDereferenceWakeInfos](../5D/PopDereferenceWakeInfos_function_005D498C.md) at `0x005D49C9`
- [PopQueryMostRecentWakeSourceInfo](../../page/75/PopQueryMostRecentWakeSourceInfo_function_0075C630.md) at `0x0075C859`
- [PopPowerAggregatorHandleSystemTransitionEndIntent](../../page/76/PopPowerAggregatorHandleSystemTransitionEndIntent_function_00764B30.md) at `0x00764B77`
- [PopPowerAggregatorHandleSystemTransitionEndIntent](../../page/76/PopPowerAggregatorHandleSystemTransitionEndIntent_function_00764B30.md) at `0x00764BB2`
- [PopPotsLogPowerTransitionReliability](../../page/AA/PopPotsLogPowerTransitionReliability_function_00AAE1C4.md) at `0x00AAE2CA`
- [PopQueryMostRecentWakeSourceAttributes](../../page/AB/PopQueryMostRecentWakeSourceAttributes_function_00AB437C.md) at `0x00AB4459`
- [PopNewWakeInfo](../../pagelk/B7/PopNewWakeInfo_function_00B7D220.md) at `0x00B7D2B6`
- [PopIsMostRecentWakeAttended](../../pagelk/B7/PopIsMostRecentWakeAttended_function_00B7D6C8.md) at `0x00B7D6E0`

### Static image references
- `0x004C74CA` → RVA `0x00AB7120` (`PopFreeWakeInfo`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004C74AC  48 83 EC 28                     sub rsp, 0x28
004C74B0  48 8B D1                        mov rdx, rcx
004C74B3  83 C8 FF                        or eax, 0xffffffff
004C74B6  F0 0F C1 41 10                  lock xadd dword ptr [rcx + 0x10], eax
004C74BB  83 F8 01                        cmp eax, 1
004C74BE  74 06                           je 0x1404c74c6
004C74C0  48 83 C4 28                     add rsp, 0x28
004C74C4  C3                              ret
004C74C5  CC                              int3
004C74C6  48 83 C1 30                     add rcx, 0x30
004C74CA  48 8D 05 4F FC 5E 00            lea rax, [rip + 0x5efc4f]
004C74D1  48 89 51 18                     mov qword ptr [rcx + 0x18], rdx
004C74D5  BA 01 00 00 00                  mov edx, 1
004C74DA  48 83 21 00                     and qword ptr [rcx], 0
004C74DE  48 89 41 10                     mov qword ptr [rcx + 0x10], rax
004C74E2  E8 39 20 E3 FF                  call 0x1402f9520
004C74E7  EB D7                           jmp 0x1404c74c0
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopWakeInfoDereference(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = (unsigned int)((result) | (0xFFFFFFFFULL));
    if (((unsigned int)(result)) == 1) goto loc_004C74C6;
loc_004C74C0:
    v_rsp = (v_rsp) + (40);
    return result;
loc_004C74C6:
    a1 = (a1) + (48);
    *(unsigned __int64 *)(a1 + 24) = a1;
    *(unsigned __int64 *)(a1 + 16) = v_rip + 6224975;
    result = ExQueueWorkItem(a1, 1, a3, a4);
    goto loc_004C74C0;
}
```

## 5. (Beta) C Style

```c
int64_t PopWakeInfoDereference(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = (uint32_t)((result) | (0xFFFFFFFFULL));
    if (((uint32_t)(result)) == 1) goto loc_004C74C6;
loc_004C74C0:
    local_rsp = (local_rsp) + (40);
    return result;
loc_004C74C6:
    Arg1 = (Arg1) + (48);
    *(void **)(arg1 + 0x18) = Arg1;
    *(uint64_t *)(arg1 + 0x10) = v_rip + 6224975;
    result = ExQueueWorkItem(Arg1, 1, a3, a4);
    goto loc_004C74C0;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R/W` |
| `Arg1` | `+ 0x10` | `32` | `R/W` |
| `Arg1` | `+ 0x10` | `64` | `W` |
| `Arg1` | `+ 0x18` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004C74AC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004C74AC[BB_004C74AC]
  bb_004C74C0[BB_004C74C0]
  bb_004C74C5[BB_004C74C5]
  bb_004C74C6[BB_004C74C6]
  bb_004C74AC -->|branch| bb_004C74C6
  bb_004C74AC -->|fallthrough| bb_004C74C0
  bb_004C74C5 -->|flow| bb_004C74C6
  bb_004C74C6 -->|branch| bb_004C74C0
```
