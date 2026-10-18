# AstIsRecording

- RVA: `0x009A55D0`–`0x009A55EA` (길이 `26` bytes)
- VA: `0x00000001409A55D0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `10`개 명령, `26/26` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [AstLogDeviceSDDLUpdated](AstLogDeviceSDDLUpdated_function_009A36A8.md) at `0x009A36DE`
- [AstLogDeviceCreated](AstLogDeviceCreated_function_009A5398.md) at `0x009A53E1`

### Static image references
- `0x009A55D0` → RVA `0x00E06F10` (`.data`; read)
- `0x009A55DD` → RVA `0x00F8D058` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009A55D0  83 3D 39 19 46 00 00            cmp dword ptr [rip + 0x461939], 0
009A55D7  77 04                           ja 0x1409a55dd
009A55D9  32 C0                           xor al, al
009A55DB  C3                              ret
009A55DC  CC                              int3
009A55DD  80 3D 74 7A 5E 00 00            cmp byte ptr [rip + 0x5e7a74], 0
009A55E4  74 F3                           je 0x1409a55d9
009A55E6  B0 01                           mov al, 1
009A55E8  C3                              ret
009A55E9  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall AstIsRecording(void)
{
    __int64 result;

    if ((*(unsigned int *)(v_rip + 4593977)) > 0) goto loc_009A55DD;
loc_009A55D9:
    result = 0;
    return result;
loc_009A55DD:
    if ((*(unsigned __int8 *)(v_rip + 6191732)) == 0) goto loc_009A55D9;
    return 1;
}
```

## 5. (Beta) C Style

```c
void AstIsRecording(void)
{
    int64_t result;

    if ((*(uint32_t *)(v_rip + 0x461939)) > 0) goto loc_009A55DD;
loc_009A55D9:
    result = 0;
    return result;
loc_009A55DD:
    if ((*(uint8_t *)(v_rip + 0x5E7A74)) == 0) goto loc_009A55D9;
    return 1;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009A55D0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_009A55D0[BB_009A55D0]
  bb_009A55D9[BB_009A55D9]
  bb_009A55DC[BB_009A55DC]
  bb_009A55DD[BB_009A55DD]
  bb_009A55E6[BB_009A55E6]
  bb_009A55E9[BB_009A55E9]
  bb_009A55D0 -->|branch| bb_009A55DD
  bb_009A55D0 -->|fallthrough| bb_009A55D9
  bb_009A55DC -->|flow| bb_009A55DD
  bb_009A55DD -->|branch| bb_009A55D9
  bb_009A55DD -->|fallthrough| bb_009A55E6
```
