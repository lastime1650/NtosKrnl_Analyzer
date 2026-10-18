# SymCryptModElementMaskedCopy

- RVA: `0x0052597C`–`0x0052598B` (길이 `15` bytes)
- VA: `0x000000014052597C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `5`개 명령, `15/15` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00525980` → [SymCryptFdefModElementMaskedCopy](../53/SymCryptFdefModElementMaskedCopy_function_00534610.md) (function, `0x00534610`)

### Direct callers
- [SymCryptShortWeierstrassNegate](../53/SymCryptShortWeierstrassNegate_function_00539380.md) at `0x005393EF`
- [SymCryptTwistedEdwardsNegate](../53/SymCryptTwistedEdwardsNegate_function_0053A240.md) at `0x0053A2BB`
- [SymCryptTwistedEdwardsNegate](../53/SymCryptTwistedEdwardsNegate_function_0053A240.md) at `0x0053A2E4`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0052597C  48 83 EC 28                     sub rsp, 0x28
00525980  E8 8B EC 00 00                  call 0x140534610
00525985  48 83 C4 28                     add rsp, 0x28
00525989  C3                              ret
0052598A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SymCryptModElementMaskedCopy(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = SymCryptFdefModElementMaskedCopy(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void SymCryptModElementMaskedCopy(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = SymCryptFdefModElementMaskedCopy(a1, a2, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0052597C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0052597C[BB_0052597C]
  bb_0052598A[BB_0052598A]
```
