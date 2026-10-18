# CmpCleanupKcbStack

- RVA: `0x009470A0`–`0x009470B8` (길이 `24` bytes)
- VA: `0x00000001409470A0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `8`개 명령, `24/24` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **15**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x009470AD` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (function, `0x00475D80`)

### Direct callers
- [CmDeleteLayeredKey](../../text/41/CmDeleteLayeredKey_function_0041B598.md) at `0x0041B838`
- [CmDeleteLayeredKey](../../text/41/CmDeleteLayeredKey_function_0041B598.md) at `0x0041B841`
- [CmDeleteLayeredKey](../../text/41/CmDeleteLayeredKey_function_0041B598.md) at `0x0041B8F2`
- [CmDeleteLayeredKey](../../text/41/CmDeleteLayeredKey_function_0041B598.md) at `0x0041B904`
- [CmQueryLayeredKey](../../text/46/CmQueryLayeredKey_function_0046A930.md) at `0x0046AAE4`
- [sub_006ED542](../../text/6E/Unknown_function_006ED542.md) at `0x006ED5AF`
- [sub_006ED542](../../text/6E/Unknown_function_006ED542.md) at `0x006ED5C1`
- [CmSaveKey](../7D/CmSaveKey_function_007DDBDC.md) at `0x007DDFE6`
- [CmRenameKey](../7E/CmRenameKey_function_007E8F48.md) at `0x007E964B`
- [CmRenameKey](../7E/CmRenameKey_function_007E8F48.md) at `0x007E9654`
- [CmRenameKey](../7E/CmRenameKey_function_007E8F48.md) at `0x007E96B3`
- [CmRenameKey](../7E/CmRenameKey_function_007E8F48.md) at `0x007E96BC`
- [CmRenameKey](../7E/CmRenameKey_function_007E8F48.md) at `0x007EA173`
- [CmRenameKey](../7E/CmRenameKey_function_007E8F48.md) at `0x007EA17C`
- [CmRenameKey](../7E/CmRenameKey_function_007E8F48.md) at `0x007EA185`
- [CmpDoBuildVirtualStack](../7E/CmpDoBuildVirtualStack_function_007EB4C4.md) at `0x007EB76E`
- [CmpDoBuildVirtualStack](../7E/CmpDoBuildVirtualStack_function_007EB4C4.md) at `0x007EB777`
- [CmpDoBuildVirtualStack](../7E/CmpDoBuildVirtualStack_function_007EB4C4.md) at `0x007EB7A7`
- [CmpDoBuildVirtualStack](../7E/CmpDoBuildVirtualStack_function_007EB4C4.md) at `0x007EB7B0`
- [CmpAssignKeySecurity](../7E/CmpAssignKeySecurity_function_007EC8B0.md) at `0x007ECA31`
- [CmpPartialPromoteSubkeys](../7F/CmpPartialPromoteSubkeys_function_007F4070.md) at `0x007F4227`
- [CmSetLastWriteTimeKey](../84/CmSetLastWriteTimeKey_function_00843368.md) at `0x008434DE`
- [CmSetLastWriteTimeKey](../84/CmSetLastWriteTimeKey_function_00843368.md) at `0x00843566`
- [CmpPromoteKey](../84/CmpPromoteKey_function_00844388.md) at `0x008444FC`
- [CmpPromoteKey](../84/CmpPromoteKey_function_00844388.md) at `0x00844505`
- [CmDeleteValueKey](../84/CmDeleteValueKey_function_008476E8.md) at `0x008482DB`
- [CmpSubtreeEnumeratorCleanup](CmpSubtreeEnumeratorCleanup_function_00945D98.md) at `0x00945DC7`
- [CmSetKeyFlags](../9A/CmSetKeyFlags_function_009AEEA4.md) at `0x009AF1C3`
- [sub_00B16440](../B1/Unknown_function_00B16440.md) at `0x00B1648B`
- [sub_00B16440](../B1/Unknown_function_00B16440.md) at `0x00B164A7`
- [sub_00B25E36](../B2/Unknown_function_00B25E36.md) at `0x00B25E3B`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x009470AD` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009470A0  48 83 EC 28                     sub rsp, 0x28
009470A4  48 8B 49 18                     mov rcx, qword ptr [rcx + 0x18]
009470A8  48 85 C9                        test rcx, rcx
009470AB  74 05                           je 0x1409470b2
009470AD  E8 CE EC B2 FF                  call 0x140475d80
009470B2  48 83 C4 28                     add rsp, 0x28
009470B6  C3                              ret
009470B7  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpCleanupKcbStack(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (*(unsigned __int64 *)(a1 + 24) != 0) {
        result = CmSiFreeMemory(*(unsigned __int64 *)(a1 + 24), a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CmpCleanupKcbStack(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (*(uint64_t *)(arg1 + 0x18) != 0) {
        result = CmSiFreeMemory(*(uint64_t *)(arg1 + 0x18), a2, a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x18` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009470A0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_009470A0[BB_009470A0]
  bb_009470AD[BB_009470AD]
  bb_009470B2[BB_009470B2]
  bb_009470B7[BB_009470B7]
  bb_009470A0 -->|branch| bb_009470B2
  bb_009470A0 -->|fallthrough| bb_009470AD
  bb_009470AD -->|flow| bb_009470B2
```
