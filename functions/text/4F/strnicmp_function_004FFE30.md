# strnicmp

- RVA: `0x004FFE30`–`0x004FFE3F` (길이 `15` bytes)
- VA: `0x00000001404FFE30`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `5`개 명령, `15/15` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **6**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004FFE34` → [_ascii_strnicmp](_ascii_strnicmp_function_004FFDCC.md) (function, `0x004FFDCC`)

### Direct callers
- [CmpPreserveSystemHiveData](../../page/7F/CmpPreserveSystemHiveData_function_007F2518.md) at `0x007F2B1F`
- [sub_00B37A8C](../../page/B3/Unknown_function_00B37A8C.md) at `0x00B37A9C`
- [sub_00B37A8C](../../page/B3/Unknown_function_00B37A8C.md) at `0x00B37AB9`
- [EmpInfParseGetValueFromSectionAndKeyName](../../init/C2/EmpInfParseGetValueFromSectionAndKeyName_function_00C264B4.md) at `0x00C26502`
- [CmpAppendSection](../../init/C2/CmpAppendSection_function_00C28158.md) at `0x00C28223`
- [CmpProcessForSimpleStringSub](../../init/C2/CmpProcessForSimpleStringSub_function_00C28C10.md) at `0x00C28C64`
- [IopStoreArcInformation](../../init/C2/IopStoreArcInformation_function_00C2D3C4.md) at `0x00C2D4B4`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004FFE30  48 83 EC 28                     sub rsp, 0x28
004FFE34  E8 93 FF FF FF                  call 0x1404ffdcc
004FFE39  48 83 C4 28                     add rsp, 0x28
004FFE3D  C3                              ret
004FFE3E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall strnicmp(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = _ascii_strnicmp(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void strnicmp(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = _ascii_strnicmp(a1, a2, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004FFE30&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004FFE30[BB_004FFE30]
  bb_004FFE3E[BB_004FFE3E]
```
