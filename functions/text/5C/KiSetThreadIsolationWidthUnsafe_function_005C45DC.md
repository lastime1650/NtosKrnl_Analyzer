# KiSetThreadIsolationWidthUnsafe

- RVA: `0x005C45DC`–`0x005C45F0` (길이 `20` bytes)
- VA: `0x00000001405C45DC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `8`개 명령, `20/20` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [KiAdjustCoreIsolationReasonThread](KiAdjustCoreIsolationReasonThread_function_005C3818.md) at `0x005C3926`
- [KiAdjustCoreIsolationReasonThread](KiAdjustCoreIsolationReasonThread_function_005C3818.md) at `0x005C39D9`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005C45DC  85 D2                           test edx, edx
005C45DE  75 08                           jne 0x1405c45e8
005C45E0  F0 0F BA 71 78 01               lock btr dword ptr [rcx + 0x78], 1
005C45E6  C3                              ret
005C45E7  CC                              int3
005C45E8  F0 0F BA 69 78 01               lock bts dword ptr [rcx + 0x78], 1
005C45EE  C3                              ret
005C45EF  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall KiSetThreadIsolationWidthUnsafe(__int64 a1, int a2)
{
    if (a2 != 0) goto loc_005C45E8;
    return;
loc_005C45E8:
    return;
}
```

## 5. (Beta) C Style

```c
void KiSetThreadIsolationWidthUnsafe(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    if (Arg2 != 0) goto loc_005C45E8;
    return;
loc_005C45E8:
    return;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x78` | `32` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005C45DC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005C45DC[BB_005C45DC]
  bb_005C45E0[BB_005C45E0]
  bb_005C45E7[BB_005C45E7]
  bb_005C45E8[BB_005C45E8]
  bb_005C45EF[BB_005C45EF]
  bb_005C45DC -->|branch| bb_005C45E8
  bb_005C45DC -->|fallthrough| bb_005C45E0
  bb_005C45E7 -->|flow| bb_005C45E8
```
