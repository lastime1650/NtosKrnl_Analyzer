# ViFilterYieldInitialization

- RVA: `0x00616D80`–`0x00616D92` (길이 `18` bytes)
- VA: `0x0000000140616D80`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `9`개 명령, `18/18` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [ViFilterDispatchGeneric](../../pagevrfy/BA/ViFilterDispatchGeneric_function_00BACFD0.md) at `0x00BACFE6`
- [ViFilterDispatchPnp](../../pagevrfy/BA/ViFilterDispatchPnp_function_00BAD0A0.md) at `0x00BAD0BE`
- [ViFilterDispatchPower](../../pagevrfy/BA/ViFilterDispatchPower_function_00BAD260.md) at `0x00BAD276`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00616D80  8B 41 64                        mov eax, dword ptr [rcx + 0x64]
00616D83  A8 01                           test al, 1
00616D85  75 09                           jne 0x140616d90
00616D87  F3 90                           pause
00616D89  8B 41 64                        mov eax, dword ptr [rcx + 0x64]
00616D8C  A8 01                           test al, 1
00616D8E  74 F7                           je 0x140616d87
00616D90  C3                              ret
00616D91  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ViFilterYieldInitialization(__int64 a1)
{
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 100)))) & (1)) != 0) goto loc_00616D90;
loc_00616D87:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 100)))) & (1)) == 0) goto loc_00616D87;
loc_00616D90:
    return (unsigned int)(*(unsigned int *)(a1 + 100));
}
```

## 5. (Beta) C Style

```c
int64_t ViFilterYieldInitialization(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x64)))) & (1)) != 0) goto loc_00616D90;
loc_00616D87:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x64)))) & (1)) == 0) goto loc_00616D87;
loc_00616D90:
    return (uint32_t)(*(uint32_t *)(arg1 + 0x64));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x64` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00616D80&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00616D80[BB_00616D80]
  bb_00616D87[BB_00616D87]
  bb_00616D90[BB_00616D90]
  bb_00616D91[BB_00616D91]
  bb_00616D80 -->|branch| bb_00616D90
  bb_00616D80 -->|fallthrough| bb_00616D87
  bb_00616D87 -->|branch| bb_00616D87
  bb_00616D87 -->|fallthrough| bb_00616D90
```
