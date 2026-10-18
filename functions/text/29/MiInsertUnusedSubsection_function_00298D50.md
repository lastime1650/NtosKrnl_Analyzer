# MiInsertUnusedSubsection

- RVA: `0x00298D50`–`0x00298D61` (길이 `17` bytes)
- VA: `0x0000000140298D50`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `6`개 명령, `17/17` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **12**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00298D56` → [MiInsertUnusedSubsectionInternal](../67/MiInsertUnusedSubsectionInternal_function_00677EDC.md) (function, `0x00677EDC`)

### Direct callers
- [sub_00285E76](../28/Unknown_function_00285E76.md) at `0x0028603C`
- [MiFlushRelease](MiFlushRelease_function_002982C0.md) at `0x00298507`
- [MiFlushRelease](MiFlushRelease_function_002982C0.md) at `0x002985E6`
- [MiRemoveViewsFromSectionWithPfn](MiRemoveViewsFromSectionWithPfn_function_002986D4.md) at `0x0029887C`
- [MiRemoveViewsFromSection](MiRemoveViewsFromSection_function_00298960.md) at `0x00298ABC`
- [MiDecrementSubsections](MiDecrementSubsections_function_00298B50.md) at `0x00298CD9`
- [MiDecrementSubsection](MiDecrementSubsection_function_00298D68.md) at `0x00298E3F`
- [MiDereferenceControlAreaPfnList](../2A/MiDereferenceControlAreaPfnList_function_002A45E8.md) at `0x002A46ED`
- [sub_002E0B15](../2E/Unknown_function_002E0B15.md) at `0x002E0EF0`
- [sub_00371EF8](../37/Unknown_function_00371EF8.md) at `0x00371F20`
- [MmPurgeSection](../38/MmPurgeSection_function_0038B450.md) at `0x0038B6DD`
- [MiFlushSection](../40/MiFlushSection_function_004036B0.md) at `0x004044D3`
- [sub_006F4EF0](../6F/Unknown_function_006F4EF0.md) at `0x006F4F07`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00298D50  48 83 EC 28                     sub rsp, 0x28
00298D54  33 D2                           xor edx, edx
00298D56  E8 81 F1 3D 00                  call 0x140677edc
00298D5B  48 83 C4 28                     add rsp, 0x28
00298D5F  C3                              ret
00298D60  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiInsertUnusedSubsection(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a2 = 0;
    result = MiInsertUnusedSubsectionInternal(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiInsertUnusedSubsection(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    Arg2 = 0;
    result = MiInsertUnusedSubsectionInternal(Arg1, Arg2, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00298D50&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00298D50[BB_00298D50]
  bb_00298D60[BB_00298D60]
```
