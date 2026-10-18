# PopFxMergeActiveTimeAccounting

- RVA: `0x0043D350`–`0x0043D38D` (길이 `61` bytes)
- VA: `0x000000014043D350`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `15`개 명령, `61/61` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [PopFxPauseDeviceAccounting](PopFxPauseDeviceAccounting_function_0043D0C8.md) at `0x0043D188`
- [PopFxPauseDeviceAccounting](PopFxPauseDeviceAccounting_function_0043D0C8.md) at `0x0043D242`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0043D350  48 8B 81 80 00 00 00            mov rax, qword ptr [rcx + 0x80]
0043D357  BA 05 00 00 00                  mov edx, 5
0043D35C  48 01 41 20                     add qword ptr [rcx + 0x20], rax
0043D360  48 8B 81 88 00 00 00            mov rax, qword ptr [rcx + 0x88]
0043D367  48 01 41 28                     add qword ptr [rcx + 0x28], rax
0043D36B  48 83 C1 30                     add rcx, 0x30
0043D36F  48 8B 41 60                     mov rax, qword ptr [rcx + 0x60]
0043D373  48 01 01                        add qword ptr [rcx], rax
0043D376  48 8B 81 88 00 00 00            mov rax, qword ptr [rcx + 0x88]
0043D37D  48 01 41 28                     add qword ptr [rcx + 0x28], rax
0043D381  48 8D 49 08                     lea rcx, [rcx + 8]
0043D385  48 83 EA 01                     sub rdx, 1
0043D389  75 E4                           jne 0x14043d36f
0043D38B  C3                              ret
0043D38C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopFxMergeActiveTimeAccounting(__int64 a1)
{
    a1 = (a1) + (48);
loc_0043D36F:
    a2 = (5) - (1);
    if (condition_is_not_equal) goto loc_0043D36F;
    return *(unsigned __int64 *)(a1 + 136);
}
```

## 5. (Beta) C Style

```c
int64_t PopFxMergeActiveTimeAccounting(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    Arg1 = (Arg1) + (48);
loc_0043D36F:
    a2 = (5) - (1);
    if (condition_is_not_equal) goto loc_0043D36F;
    return *(uint64_t *)(arg1 + 0x88);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R/W` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R/W` |
| `Arg1` | `+ 0x28` | `64` | `R/W` |
| `Arg1` | `+ 0x60` | `64` | `R` |
| `Arg1` | `+ 0x80` | `64` | `R` |
| `Arg1` | `+ 0x88` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0043D350&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0043D350[BB_0043D350]
  bb_0043D36F[BB_0043D36F]
  bb_0043D38B[BB_0043D38B]
  bb_0043D38C[BB_0043D38C]
  bb_0043D350 -->|flow| bb_0043D36F
  bb_0043D36F -->|branch| bb_0043D36F
  bb_0043D36F -->|fallthrough| bb_0043D38B
```
