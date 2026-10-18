# stricmp

- RVA: `0x004FFD80`–`0x004FFD8F` (길이 `15` bytes)
- VA: `0x00000001404FFD80`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `5`개 명령, `15/15` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **7**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004FFD84` → [_ascii_stricmp](_ascii_stricmp_function_004FFD2C.md) (function, `0x004FFD2C`)

### Direct callers
- [HalGetEnvironmentVariable](../54/HalGetEnvironmentVariable_function_005430E0.md) at `0x00543107`
- [HalSetEnvironmentVariable](../54/HalSetEnvironmentVariable_function_00543170.md) at `0x00543193`
- [HalSetEnvironmentVariable](../54/HalSetEnvironmentVariable_function_00543170.md) at `0x005431AA`
- [HalSetEnvironmentVariable](../54/HalSetEnvironmentVariable_function_00543170.md) at `0x005431E0`
- [ViThunkSnapSharedExportByName](../../pagevrfy/BB/ViThunkSnapSharedExportByName_function_00BB65BC.md) at `0x00BB665B`
- [ViThunkSnapSharedExportByName](../../pagevrfy/BB/ViThunkSnapSharedExportByName_function_00BB65BC.md) at `0x00BB666E`
- [ViThunkSnapSharedExportByName](../../pagevrfy/BB/ViThunkSnapSharedExportByName_function_00BB65BC.md) at `0x00BB669E`
- [HdlspBugCheckProcessing](../../pagehdls/BB/HdlspBugCheckProcessing_function_00BBD1F8.md) at `0x00BBD233`
- [HdlspBugCheckProcessing](../../pagehdls/BB/HdlspBugCheckProcessing_function_00BBD1F8.md) at `0x00BBD248`
- [HdlspBugCheckProcessing](../../pagehdls/BB/HdlspBugCheckProcessing_function_00BBD1F8.md) at `0x00BBD25D`
- [HdlspBugCheckProcessing](../../pagehdls/BB/HdlspBugCheckProcessing_function_00BBD1F8.md) at `0x00BBD27E`
- [CmpAppendSection](../../init/C2/CmpAppendSection_function_00C28158.md) at `0x00C2819B`
- [CmpSearchSectionByName](../../init/C2/CmpSearchSectionByName_function_00C28CE0.md) at `0x00C28D19`
- [CmpSearchSectionByName](../../init/C2/CmpSearchSectionByName_function_00C28CE0.md) at `0x00C28D40`
- [CmpSetupConfigurationTree](../../init/C5/CmpSetupConfigurationTree_function_00C5B624.md) at `0x00C5B6B3`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004FFD80  48 83 EC 28                     sub rsp, 0x28
004FFD84  E8 A3 FF FF FF                  call 0x1404ffd2c
004FFD89  48 83 C4 28                     add rsp, 0x28
004FFD8D  C3                              ret
004FFD8E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall stricmp(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = _ascii_stricmp(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void stricmp(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = _ascii_stricmp(a1, a2, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004FFD80&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004FFD80[BB_004FFD80]
  bb_004FFD8E[BB_004FFD8E]
```
