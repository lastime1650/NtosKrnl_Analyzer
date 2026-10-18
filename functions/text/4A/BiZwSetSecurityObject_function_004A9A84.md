# BiZwSetSecurityObject

- RVA: `0x004A9A84`–`0x004A9A98` (길이 `20` bytes)
- VA: `0x00000001404A9A84`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `6`개 명령, `20/20` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004A9A8D` → [ZwSetSecurityObject](../6B/ZwSetSecurityObject_function_006B0810.md) (function, `0x006B0810`)

### Direct callers
- [BiCloseKey](../../page/91/BiCloseKey_function_00916A00.md) at `0x00916A25`
- [BiOpenKey](../../page/A3/BiOpenKey_function_00A3F60C.md) at `0x00A3F6FA`
- [BiCreateKey](../../page/A4/BiCreateKey_function_00A404DC.md) at `0x00A406C2`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004A9A84  48 83 EC 28                     sub rsp, 0x28
004A9A88  BA 04 00 00 00                  mov edx, 4
004A9A8D  E8 7E 6D 20 00                  call 0x1406b0810
004A9A92  48 83 C4 28                     add rsp, 0x28
004A9A96  C3                              ret
004A9A97  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall BiZwSetSecurityObject(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = ZwSetSecurityObject(a1, 4, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void BiZwSetSecurityObject(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = ZwSetSecurityObject(a1, 4, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004A9A84&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004A9A84[BB_004A9A84]
  bb_004A9A97[BB_004A9A97]
```
