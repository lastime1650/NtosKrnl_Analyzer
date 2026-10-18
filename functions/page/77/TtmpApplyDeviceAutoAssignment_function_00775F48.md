# TtmpApplyDeviceAutoAssignment

- RVA: `0x00775F48`–`0x00775F69` (길이 `33` bytes)
- VA: `0x0000000140775F48`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `8`개 명령, `33/33` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [TtmiSessionDeviceListWorker](TtmiSessionDeviceListWorker_function_00775CA0.md) at `0x00775CEB`
- [TtmiSessionDeviceListWorker](TtmiSessionDeviceListWorker_function_00775CA0.md) at `0x00775D0B`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00775F48  F7 41 04 00 08 00 00            test dword ptr [rcx + 4], 0x800
00775F4F  4C 8D 82 58 02 00 00            lea r8, [rdx + 0x258]
00775F56  74 0B                           je 0x140775f63
00775F58  83 A2 54 02 00 00 00            and dword ptr [rdx + 0x254], 0
00775F5F  41 83 08 40                     or dword ptr [r8], 0x40
00775F63  41 83 08 20                     or dword ptr [r8], 0x20
00775F67  C3                              ret
00775F68  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall TtmpApplyDeviceAutoAssignment(__int64 a1, __int64 a2)
{
    if (((*(unsigned int *)(a1 + 4)) & (0x800ULL)) != 0) {
    }
    return;
}
```

## 5. (Beta) C Style

```c
void TtmpApplyDeviceAutoAssignment(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    if (((*(uint32_t *)(arg1 + 0x4)) & (0x800ULL)) != 0) {
    }
    return;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x4` | `32` | `R` |
| `Arg2` | `+ 0x0` | `32` | `R/W` |
| `Arg2` | `+ 0x254` | `32` | `R/W` |
| `Arg2` | `+ 0x258` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00775F48&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00775F48[BB_00775F48]
  bb_00775F58[BB_00775F58]
  bb_00775F63[BB_00775F63]
  bb_00775F68[BB_00775F68]
  bb_00775F48 -->|branch| bb_00775F63
  bb_00775F48 -->|fallthrough| bb_00775F58
  bb_00775F58 -->|flow| bb_00775F63
```
