# PnpReleasePowerRelationsQueueLock

- RVA: `0x004BE70C`–`0x004BE722` (길이 `22` bytes)
- VA: `0x00000001404BE70C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `6`개 명령, `22/22` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x004BE717` → [ExReleaseFastMutex](../25/ExReleaseFastMutex_function_002519C0.md) (function, `0x002519C0`)

### Direct callers
- [PipProcessRebuildPowerRelationsQueue](../../page/A0/PipProcessRebuildPowerRelationsQueue_function_00A06844.md) at `0x00A0687A`
- [PipProcessRebuildPowerRelationsQueue](../../page/A0/PipProcessRebuildPowerRelationsQueue_function_00A06844.md) at `0x00A068F1`
- [PiQueryPowerRelations](../../page/AA/PiQueryPowerRelations_function_00AA3F9C.md) at `0x00AA406E`
- [PiQueryPowerRelations](../../page/AA/PiQueryPowerRelations_function_00AA3F9C.md) at `0x00AA4143`
- [PiQueryPowerDependencyRelations](../../page/AA/PiQueryPowerDependencyRelations_function_00AA4524.md) at `0x00AA4635`
- [PiQueryPowerDependencyRelations](../../page/AA/PiQueryPowerDependencyRelations_function_00AA4524.md) at `0x00AA46B5`
- [PiQueryPowerDependencyRelations](../../page/AA/PiQueryPowerDependencyRelations_function_00AA4524.md) at `0x00AA472B`
- [PiValidatePowerRelations](../../page/AA/PiValidatePowerRelations_function_00AA4768.md) at `0x00AA48D1`

### Static image references
- `0x004BE710` → RVA `0x00F8C3A0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004BE70C  48 83 EC 28                     sub rsp, 0x28
004BE710  48 8D 0D 89 DC AC 00            lea rcx, [rip + 0xacdc89]
004BE717  E8 A4 32 D9 FF                  call 0x1402519c0
004BE71C  48 83 C4 28                     add rsp, 0x28
004BE720  C3                              ret
004BE721  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PnpReleasePowerRelationsQueueLock(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = ExReleaseFastMutex(v_rip + 11328649, a2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void PnpReleasePowerRelationsQueueLock(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = ExReleaseFastMutex(v_rip + 11328649, a2, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004BE70C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004BE70C[BB_004BE70C]
  bb_004BE721[BB_004BE721]
```
