# HalpDmaIsThinDmarCapable

- RVA: `0x004DC54C`–`0x004DC576` (길이 `42` bytes)
- VA: `0x00000001404DC54C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `14`개 명령, `42/42` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [HalpDmaAllocateChildAdapterV3](../../page/70/HalpDmaAllocateChildAdapterV3_function_007066A0.md) at `0x0070696B`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004DC54C  83 B9 08 02 00 00 03            cmp dword ptr [rcx + 0x208], 3
004DC553  75 1D                           jne 0x1404dc572
004DC555  33 C0                           xor eax, eax
004DC557  38 81 BD 01 00 00               cmp byte ptr [rcx + 0x1bd], al
004DC55D  74 13                           je 0x1404dc572
004DC55F  38 81 B9 01 00 00               cmp byte ptr [rcx + 0x1b9], al
004DC565  74 0B                           je 0x1404dc572
004DC567  38 81 BA 01 00 00               cmp byte ptr [rcx + 0x1ba], al
004DC56D  0F 95 C0                        setne al
004DC570  C3                              ret
004DC571  CC                              int3
004DC572  32 C0                           xor al, al
004DC574  C3                              ret
004DC575  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpDmaIsThinDmarCapable(__int64 a1)
{
    __int64 result;

    if ((*(unsigned int *)(a1 + 520)) != 3) goto loc_004DC572;
    result = 0;
    if ((*(unsigned __int8 *)(a1 + 445)) == 0) goto loc_004DC572;
    if ((*(unsigned __int8 *)(a1 + 441)) == 0) goto loc_004DC572;
    result = ((*(unsigned __int8 *)(a1 + 442)) != 0) ? 1 : 0;
    return result;
loc_004DC572:
    result = 0;
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HalpDmaIsThinDmarCapable(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    if ((*(uint32_t *)(arg1 + 0x208)) != 3) goto loc_004DC572;
    result = 0;
    if ((*(uint8_t *)(arg1 + 0x1BD)) == 0) goto loc_004DC572;
    if ((*(uint8_t *)(arg1 + 0x1B9)) == 0) goto loc_004DC572;
    result = ((*(uint8_t *)(arg1 + 0x1BA)) != 0) ? 1 : 0;
    return result;
loc_004DC572:
    result = 0;
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x1B9` | `8` | `R` |
| `Arg1` | `+ 0x1BA` | `8` | `R` |
| `Arg1` | `+ 0x1BD` | `8` | `R` |
| `Arg1` | `+ 0x208` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004DC54C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004DC54C[BB_004DC54C]
  bb_004DC555[BB_004DC555]
  bb_004DC55F[BB_004DC55F]
  bb_004DC567[BB_004DC567]
  bb_004DC571[BB_004DC571]
  bb_004DC572[BB_004DC572]
  bb_004DC575[BB_004DC575]
  bb_004DC54C -->|branch| bb_004DC572
  bb_004DC54C -->|fallthrough| bb_004DC555
  bb_004DC555 -->|branch| bb_004DC572
  bb_004DC555 -->|fallthrough| bb_004DC55F
  bb_004DC55F -->|branch| bb_004DC572
  bb_004DC55F -->|fallthrough| bb_004DC567
  bb_004DC571 -->|flow| bb_004DC572
```
