# SymCryptSizeofModulusFromDigits

- RVA: `0x00525D54`–`0x00525D63` (길이 `15` bytes)
- VA: `0x0000000140525D54`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `5`개 명령, `15/15` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00525D58` → [SymCryptFdefSizeofModulusFromDigits](../53/SymCryptFdefSizeofModulusFromDigits_function_00535728.md) (function, `0x00535728`)

### Direct callers
- [SymCryptRsakeyCreate](SymCryptRsakeyCreate_function_00523594.md) at `0x00523635`
- [SymCryptRsakeyCreate](SymCryptRsakeyCreate_function_00523594.md) at `0x00523664`
- [SymCryptRsakeyCreateAllObjects](SymCryptRsakeyCreateAllObjects_function_00523720.md) at `0x00523751`
- [SymCryptSizeofRsakeyFromParams](SymCryptSizeofRsakeyFromParams_function_00523FE4.md) at `0x00524014`
- [SymCryptSizeofRsakeyFromParams](SymCryptSizeofRsakeyFromParams_function_00523FE4.md) at `0x0052404B`
- [SymCryptEcurveValidateAndComputeSizes](SymCryptEcurveValidateAndComputeSizes_function_00524814.md) at `0x00524890`
- [SymCryptEcurveValidateAndComputeSizes](SymCryptEcurveValidateAndComputeSizes_function_00524814.md) at `0x0052489B`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00525D54  48 83 EC 28                     sub rsp, 0x28
00525D58  E8 CB F9 00 00                  call 0x140535728
00525D5D  48 83 C4 28                     add rsp, 0x28
00525D61  C3                              ret
00525D62  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SymCryptSizeofModulusFromDigits(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = SymCryptFdefSizeofModulusFromDigits(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void SymCryptSizeofModulusFromDigits(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = SymCryptFdefSizeofModulusFromDigits(a1, a2, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00525D54&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00525D54[BB_00525D54]
  bb_00525D62[BB_00525D62]
```
