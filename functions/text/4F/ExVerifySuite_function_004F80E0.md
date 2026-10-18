# ExVerifySuite

- RVA: `0x004F80E0`–`0x004F80FA` (길이 `26` bytes)
- VA: `0x00000001404F80E0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `10`개 명령, `26/26` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [MmWriteTriageInformation](../67/MmWriteTriageInformation_function_0067DF6C.md) at `0x0067DFB6`
- [MmWriteTriageInformation](../67/MmWriteTriageInformation_function_0067DF6C.md) at `0x0067DFC4`
- [MmWriteTriageInformation](../67/MmWriteTriageInformation_function_0067DF6C.md) at `0x0067DFD2`
- [PsLocateSystemDlls](../../page/77/PsLocateSystemDlls_function_0077ED90.md) at `0x0077EDA4`
- [ExpUpdateProductSuiteTypeInRegistry](../../init/C5/ExpUpdateProductSuiteTypeInRegistry_function_00C51BC0.md) at `0x00C51D06`
- [ExpUpdateProductSuiteTypeInRegistry](../../init/C5/ExpUpdateProductSuiteTypeInRegistry_function_00C51BC0.md) at `0x00C51D50`
- [ExpUpdateProductSuiteTypeInRegistry](../../init/C5/ExpUpdateProductSuiteTypeInRegistry_function_00C51BC0.md) at `0x00C51D93`
- [ExpUpdateProductSuiteTypeInRegistry](../../init/C5/ExpUpdateProductSuiteTypeInRegistry_function_00C51BC0.md) at `0x00C51DD6`
- [ExpUpdateProductSuiteTypeInRegistry](../../init/C5/ExpUpdateProductSuiteTypeInRegistry_function_00C51BC0.md) at `0x00C51E19`
- [ExpUpdateProductSuiteTypeInRegistry](../../init/C5/ExpUpdateProductSuiteTypeInRegistry_function_00C51BC0.md) at `0x00C51E5C`
- [ExpUpdateProductSuiteTypeInRegistry](../../init/C5/ExpUpdateProductSuiteTypeInRegistry_function_00C51BC0.md) at `0x00C51E9F`
- [ExpUpdateProductSuiteTypeInRegistry](../../init/C5/ExpUpdateProductSuiteTypeInRegistry_function_00C51BC0.md) at `0x00C51EE2`
- [ExpUpdateProductSuiteTypeInRegistry](../../init/C5/ExpUpdateProductSuiteTypeInRegistry_function_00C51BC0.md) at `0x00C51F25`
- [ExpUpdateProductSuiteTypeInRegistry](../../init/C5/ExpUpdateProductSuiteTypeInRegistry_function_00C51BC0.md) at `0x00C51F68`
- [ExpUpdateProductSuiteTypeInRegistry](../../init/C5/ExpUpdateProductSuiteTypeInRegistry_function_00C51BC0.md) at `0x00C51FAB`
- [ExpUpdateProductSuiteTypeInRegistry](../../init/C5/ExpUpdateProductSuiteTypeInRegistry_function_00C51BC0.md) at `0x00C51FEE`
- [ExpUpdateProductSuiteTypeInRegistry](../../init/C5/ExpUpdateProductSuiteTypeInRegistry_function_00C51BC0.md) at `0x00C52031`
- [ExpUpdateProductSuiteTypeInRegistry](../../init/C5/ExpUpdateProductSuiteTypeInRegistry_function_00C51BC0.md) at `0x00C52074`
- [ExpUpdateProductSuiteTypeInRegistry](../../init/C5/ExpUpdateProductSuiteTypeInRegistry_function_00C51BC0.md) at `0x00C520B7`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004F80E0  83 F9 12                        cmp ecx, 0x12
004F80E3  7E 04                           jle 0x1404f80e9
004F80E5  32 C0                           xor al, al
004F80E7  C3                              ret
004F80E8  CC                              int3
004F80E9  A1 D0 02 00 00 80 F7 FF FF      movabs eax, dword ptr [0xfffff780000002d0]
004F80F2  0F A3 C8                        bt eax, ecx
004F80F5  0F 92 C0                        setb al
004F80F8  C3                              ret
004F80F9  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExVerifySuite(int a1)
{
    __int64 result;

    if (a1 <= 18) goto loc_004F80E9;
    result = 0;
    return result;
loc_004F80E9:
    result = (condition_is_below) ? 1 : 0;
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ExVerifySuite(int32_t Arg1)
{
    int64_t result;

    if (Arg1 <= 18) goto loc_004F80E9;
    result = 0;
    return result;
loc_004F80E9:
    result = (condition_is_below) ? 1 : 0;
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004F80E0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004F80E0[BB_004F80E0]
  bb_004F80E5[BB_004F80E5]
  bb_004F80E8[BB_004F80E8]
  bb_004F80E9[BB_004F80E9]
  bb_004F80F9[BB_004F80F9]
  bb_004F80E0 -->|branch| bb_004F80E9
  bb_004F80E0 -->|fallthrough| bb_004F80E5
  bb_004F80E8 -->|flow| bb_004F80E9
```
