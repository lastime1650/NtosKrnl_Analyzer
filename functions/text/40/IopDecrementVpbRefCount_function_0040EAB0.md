# IopDecrementVpbRefCount

- RVA: `0x0040EAB0`–`0x0040EAC1` (길이 `17` bytes)
- VA: `0x000000014040EAB0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009BA20`
- 디코드: `5`개 명령, `17/17` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [sub_00863E45](../../page/86/Unknown_function_00863E45.md) at `0x00863F11`
- [IoVerifyVolume](../../page/AC/IoVerifyVolume_function_00ACF200.md) at `0x00ACF3AC`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x0040EABB` → [sub_0040EC12 + 0x7](Unknown_function_0040EC12.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0040EAB0  40 53                           push rbx
0040EAB2  48 83 EC 20                     sub rsp, 0x20
0040EAB6  48 8B D9                        mov rbx, rcx
0040EAB9  84 D2                           test dl, dl
0040EABB  0F 84 58 01 00 00               je 0x14040ec19
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall IopDecrementVpbRefCount(__int64 a1, unsigned __int8 a2)
{
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
}
```

## 5. (Beta) C Style

```c
void IopDecrementVpbRefCount(int64_t Arg1, uint8_t Arg2)
{
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0040EAB0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0040EAB0[BB_0040EAB0]
```
