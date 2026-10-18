# HalpVpptInitialize

- RVA: `0x0054A2D0`–`0x0054A2EC` (길이 `28` bytes)
- VA: `0x000000014054A2D0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `8`개 명령, `28/28` bytes 표시
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
0054A2D0  83 79 10 FF                     cmp dword ptr [rcx + 0x10], -1
0054A2D4  75 0B                           jne 0x14054a2e1
0054A2D6  65 8B 04 25 A4 01 00 00         mov eax, dword ptr gs:[0x1a4]
0054A2DE  89 41 10                        mov dword ptr [rcx + 0x10], eax
0054A2E1  C7 41 14 01 00 00 00            mov dword ptr [rcx + 0x14], 1
0054A2E8  33 C0                           xor eax, eax
0054A2EA  C3                              ret
0054A2EB  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpVpptInitialize(__int64 a1)
{
    __int64 result;

    if ((*(unsigned int *)(a1 + 16)) == -1) {
        result = *(unsigned int *)(gs_base + (0 + 420));
        *(unsigned int *)(a1 + 16) = (unsigned int)(result);
    }
    *(unsigned int *)(a1 + 20) = 1;
    result = 0;
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HalpVpptInitialize(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    if ((*(uint32_t *)(arg1 + 0x10)) == -1) {
        result = *(uint32_t *)(gs_base + (0 + 0x1A4));
        *(uint32_t *)(arg1 + 0x10) = (uint32_t)(result);
    }
    *(uint32_t *)(arg1 + 0x14) = 1;
    result = 0;
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x10` | `32` | `R` |
| `Arg1` | `+ 0x10` | `32` | `W` |
| `Arg1` | `+ 0x14` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0054A2D0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0054A2D0[BB_0054A2D0]
  bb_0054A2D6[BB_0054A2D6]
  bb_0054A2E1[BB_0054A2E1]
  bb_0054A2EB[BB_0054A2EB]
  bb_0054A2D0 -->|branch| bb_0054A2E1
  bb_0054A2D0 -->|fallthrough| bb_0054A2D6
  bb_0054A2D6 -->|flow| bb_0054A2E1
```
