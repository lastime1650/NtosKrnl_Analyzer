# PopPowerAggregatorHandleDirectedDripsIntent

- RVA: `0x007649C0`–`0x007649DB` (길이 `27` bytes)
- VA: `0x00000001407649C0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `10`개 명령, `27/27` bytes 표시
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
007649C0  83 79 10 01                     cmp dword ptr [rcx + 0x10], 1
007649C4  74 07                           je 0x1407649cd
007649C6  B8 03 A0 00 C0                  mov eax, 0xc000a003
007649CB  C3                              ret
007649CC  CC                              int3
007649CD  C7 02 01 00 00 00               mov dword ptr [rdx], 1
007649D3  33 C0                           xor eax, eax
007649D5  C6 42 1A 01                     mov byte ptr [rdx + 0x1a], 1
007649D9  C3                              ret
007649DA  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopPowerAggregatorHandleDirectedDripsIntent(__int64 a1, __int64 a2)
{
    __int64 result;

    if ((*(unsigned int *)(a1 + 16)) == 1) goto loc_007649CD;
    return (unsigned int)(0xC000A003ULL);
loc_007649CD:
    *(unsigned int *)(a2) = 1;
    result = 0;
    *(unsigned __int8 *)(a2 + 26) = 1;
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopPowerAggregatorHandleDirectedDripsIntent(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;

    if ((*(uint32_t *)(arg1 + 0x10)) == 1) goto loc_007649CD;
    return (uint32_t)(0xC000A003ULL);
loc_007649CD:
    *(uint32_t *)(arg2) = 1;
    result = 0;
    *(uint8_t *)(arg2 + 0x1A) = 1;
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x10` | `32` | `R` |
| `Arg2` | `+ 0x0` | `32` | `W` |
| `Arg2` | `+ 0x1A` | `8` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007649C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007649C0[BB_007649C0]
  bb_007649C6[BB_007649C6]
  bb_007649CC[BB_007649CC]
  bb_007649CD[BB_007649CD]
  bb_007649DA[BB_007649DA]
  bb_007649C0 -->|branch| bb_007649CD
  bb_007649C0 -->|fallthrough| bb_007649C6
  bb_007649CC -->|flow| bb_007649CD
```
