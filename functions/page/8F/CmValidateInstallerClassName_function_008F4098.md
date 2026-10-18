# CmValidateInstallerClassName

- RVA: `0x008F4098`–`0x008F40B5` (길이 `29` bytes)
- VA: `0x00000001408F4098`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `10`개 명령, `29/29` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x008F409F` → [PnpIsValidGuidString](PnpIsValidGuidString_function_008F37F8.md) (function, `0x008F37F8`)

### Direct callers
- [CmClassSubkeyCallback](../82/CmClassSubkeyCallback_function_0082C830.md) at `0x0082C897`
- [CmClassSubkeyCallback](../82/CmClassSubkeyCallback_function_0082C830.md) at `0x0082C8A6`
- [_PnpDispatchInterfaceClass](../99/_PnpDispatchInterfaceClass_function_00993BD0.md) at `0x00993D26`
- [_PnpDispatchInstallerClass](../9D/_PnpDispatchInstallerClass_function_009D3580.md) at `0x009D3754`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008F4098  48 83 EC 28                     sub rsp, 0x28
008F409C  48 8B CA                        mov rcx, rdx
008F409F  E8 54 F7 FF FF                  call 0x1408f37f8
008F40A4  F6 D8                           neg al
008F40A6  1B C0                           sbb eax, eax
008F40A8  F7 D0                           not eax
008F40AA  25 33 00 00 C0                  and eax, 0xc0000033
008F40AF  48 83 C4 28                     add rsp, 0x28
008F40B3  C3                              ret
008F40B4  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmValidateInstallerClassName(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = PnpIsValidGuidString(a2, a2, a3, a4);
    result = (unsigned __int8)(-(result));
    result = (unsigned int)(~(result));
    result = (unsigned int)((result) & (0xC0000033ULL));
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CmValidateInstallerClassName(int64_t Arg1, int64_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = PnpIsValidGuidString(Arg2, Arg2, a3, a4);
    result = (uint8_t)(-(result));
    result = (uint32_t)(~(result));
    result = (uint32_t)((result) & (0xC0000033ULL));
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008F4098&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_008F4098[BB_008F4098]
  bb_008F40B4[BB_008F40B4]
```
