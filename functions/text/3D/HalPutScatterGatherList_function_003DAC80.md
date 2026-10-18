# HalPutScatterGatherList

- RVA: `0x003DAC80`–`0x003DACA1` (길이 `33` bytes)
- VA: `0x00000001403DAC80`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CEE8`
- 디코드: `10`개 명령, `33/33` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x003DAC8F` → [HalPutScatterGatherListV3](HalPutScatterGatherListV3_function_003DACA8.md) (function, `0x003DACA8`)
- `0x003DAC9A` → [HalPutScatterGatherListV2](HalPutScatterGatherListV2_function_003DE7D0.md) (function, `0x003DE7D0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003DAC80  48 83 EC 28                     sub rsp, 0x28
003DAC84  8B 81 9C 00 00 00               mov eax, dword ptr [rcx + 0x9c]
003DAC8A  83 F8 02                        cmp eax, 2
003DAC8D  74 0B                           je 0x1403dac9a
003DAC8F  E8 14 00 00 00                  call 0x1403daca8
003DAC94  48 83 C4 28                     add rsp, 0x28
003DAC98  C3                              ret
003DAC99  CC                              int3
003DAC9A  E8 31 3B 00 00                  call 0x1403de7d0
003DAC9F  EB F3                           jmp 0x1403dac94
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalPutScatterGatherList(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 156)))) == 2) goto loc_003DAC9A;
    result = HalPutScatterGatherListV3(a1, a2, a3, a4);
loc_003DAC94:
    v_rsp = (v_rsp) + (40);
    return result;
loc_003DAC9A:
    result = HalPutScatterGatherListV2(a1, a2, a3, a4);
    goto loc_003DAC94;
}
```

## 5. (Beta) C Style

```c
int64_t HalPutScatterGatherList(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x9C)))) == 2) goto loc_003DAC9A;
    result = HalPutScatterGatherListV3(Arg1, a2, a3, a4);
loc_003DAC94:
    local_rsp = (local_rsp) + (40);
    return result;
loc_003DAC9A:
    result = HalPutScatterGatherListV2(Arg1, a2, a3, a4);
    goto loc_003DAC94;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x9C` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003DAC80&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003DAC80[BB_003DAC80]
  bb_003DAC8F[BB_003DAC8F]
  bb_003DAC94[BB_003DAC94]
  bb_003DAC99[BB_003DAC99]
  bb_003DAC9A[BB_003DAC9A]
  bb_003DAC80 -->|branch| bb_003DAC9A
  bb_003DAC80 -->|fallthrough| bb_003DAC8F
  bb_003DAC8F -->|flow| bb_003DAC94
  bb_003DAC99 -->|flow| bb_003DAC9A
  bb_003DAC9A -->|branch| bb_003DAC94
```
