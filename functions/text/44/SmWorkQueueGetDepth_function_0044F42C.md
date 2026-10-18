# SmWorkQueueGetDepth

- RVA: `0x0044F42C`–`0x0044F44C` (길이 `32` bytes)
- VA: `0x000000014044F42C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `9`개 명령, `32/32` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [ST_STORE&lt;SM_TRAITS&gt;::StDmLazyRegionsWorker](../49/ST_STORE_SM_TRAITS_StDmLazyRegionsWorker_function_0049FE78.md) at `0x004A0032`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0044F42C  44 8B 81 00 1B 00 00            mov r8d, dword ptr [rcx + 0x1b00]
0044F433  44 03 81 08 1D 00 00            add r8d, dword ptr [rcx + 0x1d08]
0044F43A  8B 81 04 1B 00 00               mov eax, dword ptr [rcx + 0x1b04]
0044F440  85 D2                           test edx, edx
0044F442  75 03                           jne 0x14044f447
0044F444  C1 E8 08                        shr eax, 8
0044F447  41 03 C0                        add eax, r8d
0044F44A  C3                              ret
0044F44B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SmWorkQueueGetDepth(__int64 a1, int a2)
{
    __int64 result;

    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 6912))) + (*(unsigned int *)(a1 + 7432)));
    result = (unsigned int)(*(unsigned int *)(a1 + 6916));
    if (a2 == 0) {
        result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 6916))) >> (8));
    }
    result = (unsigned int)((result) + ((unsigned int)(a3)));
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t SmWorkQueueGetDepth(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    a3 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x1B00))) + (*(uint32_t *)(arg1 + 0x1D08)));
    result = (uint32_t)(*(uint32_t *)(arg1 + 0x1B04));
    if (Arg2 == 0) {
        result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x1B04))) >> (8));
    }
    result = (uint32_t)((result) + ((uint32_t)(a3)));
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x1B00` | `32` | `R` |
| `Arg1` | `+ 0x1B04` | `32` | `R` |
| `Arg1` | `+ 0x1D08` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0044F42C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0044F42C[BB_0044F42C]
  bb_0044F444[BB_0044F444]
  bb_0044F447[BB_0044F447]
  bb_0044F44B[BB_0044F44B]
  bb_0044F42C -->|branch| bb_0044F447
  bb_0044F42C -->|fallthrough| bb_0044F444
  bb_0044F444 -->|flow| bb_0044F447
```
