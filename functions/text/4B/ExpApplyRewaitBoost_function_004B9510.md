# ExpApplyRewaitBoost

- RVA: `0x004B9510`–`0x004B952D` (길이 `29` bytes)
- VA: `0x00000001404B9510`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `7`개 명령, `29/29` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004B9522` → [ExpApplyPriorityBoost](../21/ExpApplyPriorityBoost_function_00213F10.md) (function, `0x00213F10`)

### Direct callers
- [ExpWaitForResource](../21/ExpWaitForResource_function_002166F0.md) at `0x002167B3`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004B9510  48 83 EC 28                     sub rsp, 0x28
004B9514  65 4C 8B 04 25 88 01 00 00      mov r8, qword ptr gs:[0x188]
004B951D  BA 00 FF 00 00                  mov edx, 0xff00
004B9522  E8 E9 A9 D5 FF                  call 0x140213f10
004B9527  48 83 C4 28                     add rsp, 0x28
004B952B  C3                              ret
004B952C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExpApplyRewaitBoost(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = ExpApplyPriorityBoost(a1, (unsigned int)(0xFF00ULL), *(unsigned __int64 *)(gs_base + (0 + 392)), a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void ExpApplyRewaitBoost(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = ExpApplyPriorityBoost(a1, (uint32_t)(0xFF00ULL), *(uint64_t *)(gs_base + (0 + 0x188)), a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004B9510&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004B9510[BB_004B9510]
  bb_004B952C[BB_004B952C]
```
