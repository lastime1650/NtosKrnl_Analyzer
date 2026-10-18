# HalpIommuFlushPhysicalPtesFromCacheSize

- RVA: `0x0030885C`–`0x00308874` (길이 `24` bytes)
- VA: `0x000000014030885C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `7`개 명령, `24/24` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00308869` → [KeInvalidateRangeAllCachesNoIpi](KeInvalidateRangeAllCachesNoIpi_function_00308C50.md) (function, `0x00308C50`)

### Direct callers
- [HalpIommuMapLogical](HalpIommuMapLogical_function_00308290.md) at `0x00308434`
- [HalpIommuMapLogical](HalpIommuMapLogical_function_00308290.md) at `0x00308541`
- [HalpIommuUnmapLogicalRange](HalpIommuUnmapLogicalRange_function_00308660.md) at `0x003087B2`
- [HalpIommuAllocateAndZeroPageTable](../3F/HalpIommuAllocateAndZeroPageTable_function_003F8B30.md) at `0x003F8BC8`
- [HalpIommuInitializeDmarPageTable](../56/HalpIommuInitializeDmarPageTable_function_00568F24.md) at `0x0056909A`
- [HalpIommuMapLogicalRange](../56/HalpIommuMapLogicalRange_function_005690DC.md) at `0x0056925B`
- [HalpIommuMapLogicalRange](../56/HalpIommuMapLogicalRange_function_005690DC.md) at `0x00569342`

### Static image references
- `0x00308860` → RVA `0x00FC1910` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0030885C  48 83 EC 28                     sub rsp, 0x28
00308860  80 3D A9 90 CB 00 00            cmp byte ptr [rip + 0xcb90a9], 0
00308867  75 05                           jne 0x14030886e
00308869  E8 E2 03 00 00                  call 0x140308c50
0030886E  48 83 C4 28                     add rsp, 0x28
00308872  C3                              ret
00308873  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpIommuFlushPhysicalPtesFromCacheSize(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if ((*(unsigned __int8 *)(v_rip + 13340841)) == 0) {
        result = KeInvalidateRangeAllCachesNoIpi(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void HalpIommuFlushPhysicalPtesFromCacheSize(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if ((*(uint8_t *)(v_rip + 0xCB90A9)) == 0) {
        result = KeInvalidateRangeAllCachesNoIpi(a1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0030885C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0030885C[BB_0030885C]
  bb_00308869[BB_00308869]
  bb_0030886E[BB_0030886E]
  bb_00308873[BB_00308873]
  bb_0030885C -->|branch| bb_0030886E
  bb_0030885C -->|fallthrough| bb_00308869
  bb_00308869 -->|flow| bb_0030886E
```
