# PpvUtilTestStartedPdoStack

- RVA: `0x004BE4D8`–`0x004BE4F2` (길이 `26` bytes)
- VA: `0x00000001404BE4D8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CEE8`
- 디코드: `8`개 명령, `26/26` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x004BE4EB` → [VfMajorTestStartedPdoStack](../../pagevrfy/BA/VfMajorTestStartedPdoStack_function_00BA30B0.md) (function, `0x00BA30B0`)

### Direct callers
- [PipProcessStartPhase3](../../page/8F/PipProcessStartPhase3_function_008FBAF8.md) at `0x008FBBBF`

### Static image references
- `0x004BE4DC` → RVA `0x00E663C8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x004BE4EB` → [VfMajorTestStartedPdoStack](../../pagevrfy/BA/VfMajorTestStartedPdoStack_function_00BA30B0.md) (`.text` → `PAGEVRFY`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004BE4D8  48 83 EC 28                     sub rsp, 0x28
004BE4DC  80 3D E5 7E 9A 00 00            cmp byte ptr [rip + 0x9a7ee5], 0
004BE4E3  75 06                           jne 0x1404be4eb
004BE4E5  48 83 C4 28                     add rsp, 0x28
004BE4E9  C3                              ret
004BE4EA  CC                              int3
004BE4EB  E8 C0 4B 6E 00                  call 0x140ba30b0
004BE4F0  EB F3                           jmp 0x1404be4e5
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PpvUtilTestStartedPdoStack(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if ((*(unsigned __int8 *)(v_rip + 10125029)) != 0) goto loc_004BE4EB;
loc_004BE4E5:
    v_rsp = (v_rsp) + (40);
    return result;
loc_004BE4EB:
    result = VfMajorTestStartedPdoStack(a1, a2, a3, a4);
    goto loc_004BE4E5;
}
```

## 5. (Beta) C Style

```c
void PpvUtilTestStartedPdoStack(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if ((*(uint8_t *)(v_rip + 0x9A7EE5)) != 0) goto loc_004BE4EB;
loc_004BE4E5:
    local_rsp = (local_rsp) + (40);
    return result;
loc_004BE4EB:
    result = VfMajorTestStartedPdoStack(a1, a2, a3, a4);
    goto loc_004BE4E5;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004BE4D8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004BE4D8[BB_004BE4D8]
  bb_004BE4E5[BB_004BE4E5]
  bb_004BE4EA[BB_004BE4EA]
  bb_004BE4EB[BB_004BE4EB]
  bb_004BE4D8 -->|branch| bb_004BE4EB
  bb_004BE4D8 -->|fallthrough| bb_004BE4E5
  bb_004BE4EA -->|flow| bb_004BE4EB
  bb_004BE4EB -->|branch| bb_004BE4E5
```
