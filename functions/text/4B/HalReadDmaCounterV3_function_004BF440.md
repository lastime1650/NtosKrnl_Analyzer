# HalReadDmaCounterV3

- RVA: `0x004BF440`–`0x004BF46A` (길이 `42` bytes)
- VA: `0x00000001404BF440`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008A618`
- 디코드: `11`개 명령, `42/42` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004BF463` → [HalpDmaControllerReadDmaCounter](HalpDmaControllerReadDmaCounter_function_004BF470.md) (function, `0x004BF470`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004BF440  48 83 EC 28                     sub rsp, 0x28
004BF444  80 B9 B9 01 00 00 00            cmp byte ptr [rcx + 0x1b9], 0
004BF44B  74 09                           je 0x1404bf456
004BF44D  83 C8 FF                        or eax, 0xffffffff
004BF450  48 83 C4 28                     add rsp, 0x28
004BF454  C3                              ret
004BF455  CC                              int3
004BF456  8B 91 7C 01 00 00               mov edx, dword ptr [rcx + 0x17c]
004BF45C  48 8B 89 70 01 00 00            mov rcx, qword ptr [rcx + 0x170]
004BF463  E8 08 00 00 00                  call 0x1404bf470
004BF468  EB E6                           jmp 0x1404bf450
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalReadDmaCounterV3(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if ((*(unsigned __int8 *)(a1 + 441)) == 0) goto loc_004BF456;
    result = (unsigned int)((result) | (0xFFFFFFFFULL));
loc_004BF450:
    v_rsp = (v_rsp) + (40);
    return result;
loc_004BF456:
    result = HalpDmaControllerReadDmaCounter(*(unsigned __int64 *)(a1 + 368), (unsigned int)(*(unsigned int *)(a1 + 380)), a3, a4);
    goto loc_004BF450;
}
```

## 5. (Beta) C Style

```c
int64_t HalReadDmaCounterV3(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if ((*(uint8_t *)(arg1 + 0x1B9)) == 0) goto loc_004BF456;
    result = (uint32_t)((result) | (0xFFFFFFFFULL));
loc_004BF450:
    local_rsp = (local_rsp) + (40);
    return result;
loc_004BF456:
    result = HalpDmaControllerReadDmaCounter(*(uint64_t *)(arg1 + 0x170), (uint32_t)(*(uint32_t *)(arg1 + 0x17C)), a3, a4);
    goto loc_004BF450;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x170` | `64` | `R` |
| `Arg1` | `+ 0x17C` | `32` | `R` |
| `Arg1` | `+ 0x1B9` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004BF440&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004BF440[BB_004BF440]
  bb_004BF44D[BB_004BF44D]
  bb_004BF450[BB_004BF450]
  bb_004BF455[BB_004BF455]
  bb_004BF456[BB_004BF456]
  bb_004BF440 -->|branch| bb_004BF456
  bb_004BF440 -->|fallthrough| bb_004BF44D
  bb_004BF44D -->|flow| bb_004BF450
  bb_004BF455 -->|flow| bb_004BF456
  bb_004BF456 -->|branch| bb_004BF450
```
