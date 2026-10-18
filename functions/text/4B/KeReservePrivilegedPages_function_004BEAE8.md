# KeReservePrivilegedPages

- RVA: `0x004BEAE8`–`0x004BEAF7` (길이 `15` bytes)
- VA: `0x00000001404BEAE8`
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
- `0x004BEAEC` → [VslReserveProtectedPages](../../page/A9/VslReserveProtectedPages_function_00A90ACC.md) (function, `0x00A90ACC`)

### Direct callers
- [MiFreeInitializationCode](../../page/7F/MiFreeInitializationCode_function_007F88A0.md) at `0x007F8A1D`
- [MiFreeInitializationCode](../../page/7F/MiFreeInitializationCode_function_007F88A0.md) at `0x007F8B88`
- [MiReleasePrivilegedPtes](../../page/7F/MiReleasePrivilegedPtes_function_007F9264.md) at `0x007F92A8`
- [MiUnlockDriverPages](../../page/A4/MiUnlockDriverPages_function_00A4BA6C.md) at `0x00A4BB04`
- [MiReservePrivilegedPtes](../../page/A7/MiReservePrivilegedPtes_function_00A75394.md) at `0x00A753E5`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x004BEAEC` → [VslReserveProtectedPages](../../page/A9/VslReserveProtectedPages_function_00A90ACC.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004BEAE8  48 83 EC 28                     sub rsp, 0x28
004BEAEC  E8 DB 1F 5D 00                  call 0x140a90acc
004BEAF1  48 83 C4 28                     add rsp, 0x28
004BEAF5  C3                              ret
004BEAF6  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KeReservePrivilegedPages(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = VslReserveProtectedPages(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void KeReservePrivilegedPages(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = VslReserveProtectedPages(a1, a2, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004BEAE8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004BEAE8[BB_004BEAE8]
  bb_004BEAF6[BB_004BEAF6]
```
