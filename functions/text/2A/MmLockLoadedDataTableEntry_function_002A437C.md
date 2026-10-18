# MmLockLoadedDataTableEntry

- RVA: `0x002A437C`–`0x002A4390` (길이 `20` bytes)
- VA: `0x00000001402A437C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `6`개 명령, `20/20` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x002A4385` → [MiLockLoadedDataTableEntry](MiLockLoadedDataTableEntry_function_002A38F4.md) (function, `0x002A38F4`)

### Direct callers
- [KeSetTracepoint](../../page/74/KeSetTracepoint_function_00747F80.md) at `0x0074818F`
- [MmGetSectionRange](../../page/7F/MmGetSectionRange_function_007F9408.md) at `0x007F942F`
- [MmCompactServiceTable](../../page/80/MmCompactServiceTable_function_0080C7E8.md) at `0x0080C7F2`
- [MiLogPinDriverAddress](../../page/A4/MiLogPinDriverAddress_function_00A442B4.md) at `0x00A442F5`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002A437C  48 83 EC 28                     sub rsp, 0x28
002A4380  BA 01 00 00 00                  mov edx, 1
002A4385  E8 6A F5 FF FF                  call 0x1402a38f4
002A438A  48 83 C4 28                     add rsp, 0x28
002A438E  C3                              ret
002A438F  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MmLockLoadedDataTableEntry(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = MiLockLoadedDataTableEntry(a1, 1, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void MmLockLoadedDataTableEntry(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = MiLockLoadedDataTableEntry(a1, 1, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002A437C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002A437C[BB_002A437C]
  bb_002A438F[BB_002A438F]
```
