# PsSetThreadHardErrorsAreDisabled

- RVA: `0x004C1F90`–`0x004C1FA8` (길이 `24` bytes)
- VA: `0x00000001404C1F90`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `8`개 명령, `24/24` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004C1F90  84 D2                           test dl, dl
004C1F92  75 0A                           jne 0x1404c1f9e
004C1F94  F0 83 A1 A0 05 00 00 EF         lock and dword ptr [rcx + 0x5a0], 0xffffffef
004C1F9C  C3                              ret
004C1F9D  CC                              int3
004C1F9E  F0 83 89 A0 05 00 00 10         lock or dword ptr [rcx + 0x5a0], 0x10
004C1FA6  C3                              ret
004C1FA7  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall PsSetThreadHardErrorsAreDisabled(__int64 a1, unsigned __int8 a2)
{
    if (a2 != 0) goto loc_004C1F9E;
    return;
loc_004C1F9E:
    return;
}
```

## 5. (Beta) C Style

```c
void PsSetThreadHardErrorsAreDisabled(void *Arg1, uint8_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    if (Arg2 != 0) goto loc_004C1F9E;
    return;
loc_004C1F9E:
    return;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x5A0` | `32` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004C1F90&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004C1F90[BB_004C1F90]
  bb_004C1F94[BB_004C1F94]
  bb_004C1F9D[BB_004C1F9D]
  bb_004C1F9E[BB_004C1F9E]
  bb_004C1FA7[BB_004C1FA7]
  bb_004C1F90 -->|branch| bb_004C1F9E
  bb_004C1F90 -->|fallthrough| bb_004C1F94
  bb_004C1F9D -->|flow| bb_004C1F9E
```
