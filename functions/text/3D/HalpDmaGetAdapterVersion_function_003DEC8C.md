# HalpDmaGetAdapterVersion

- RVA: `0x003DEC8C`–`0x003DECAA` (길이 `30` bytes)
- VA: `0x00000001403DEC8C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `10`개 명령, `30/30` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **15**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [IoMapTransferInternal](IoMapTransferInternal_function_003DC910.md) at `0x003DC943`
- [IoMapTransferInternal](IoMapTransferInternal_function_003DC910.md) at `0x003DC9B6`
- [IopMapTransfer](IopMapTransfer_function_003DCD80.md) at `0x003DCDDD`
- [IopMapTransfer](IopMapTransfer_function_003DCD80.md) at `0x003DCE27`
- [HalpDmaAllocateMapRegisters](HalpDmaAllocateMapRegisters_function_003DDA0C.md) at `0x003DDB0C`
- [HalpDmaAllocateMapRegisters](HalpDmaAllocateMapRegisters_function_003DDA0C.md) at `0x003DDB85`
- [sub_003DDEB6](Unknown_function_003DDEB6.md) at `0x003DDF49`
- [sub_003DDEB6](Unknown_function_003DDEB6.md) at `0x003DDFA9`
- [sub_003DE84B](Unknown_function_003DE84B.md) at `0x003DE955`
- [HalGetScatterGatherList](HalGetScatterGatherList_function_003DFAC0.md) at `0x003DFACD`
- [HalpDmaAllocateContiguousPagesFromContiguousPool](../3E/HalpDmaAllocateContiguousPagesFromContiguousPool_function_003E024C.md) at `0x003E0253`
- [HalJoinDmaDomain](../4E/HalJoinDmaDomain_function_004E3320.md) at `0x004E333D`
- [HalAllocateAdapterChannel](../53/HalAllocateAdapterChannel_function_0053F310.md) at `0x0053F327`
- [HalpDmaAllocateContiguousPagesFromContiguousPoolAtHighLevel](../53/HalpDmaAllocateContiguousPagesFromContiguousPoolAtHighLevel_function_0053F460.md) at `0x0053F467`
- [HalpDmaAllocateScatterPagesFromScatterPoolAtHighLevel](../53/HalpDmaAllocateScatterPagesFromScatterPoolAtHighLevel_function_0053F48C.md) at `0x0053F493`
- [IoFreeMapRegistersThunk](../53/IoFreeMapRegistersThunk_function_0053F550.md) at `0x0053F55A`
- [HalpDmaAllocateMapRegistersAtHighLevel](../55/HalpDmaAllocateMapRegistersAtHighLevel_function_005507A8.md) at `0x005508A5`
- [HalGetAdapterV3](../../page/70/HalGetAdapterV3_function_00709838.md) at `0x00709B72`
- [HalGetAdapterV2](../../page/70/HalGetAdapterV2_function_00709DD8.md) at `0x0070A05E`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003DEC8C  8B 91 9C 00 00 00               mov edx, dword ptr [rcx + 0x9c]
003DEC92  B8 02 00 00 00                  mov eax, 2
003DEC97  3B D0                           cmp edx, eax
003DEC99  74 0D                           je 0x1403deca8
003DEC9B  83 C8 FF                        or eax, 0xffffffff
003DEC9E  B9 03 00 00 00                  mov ecx, 3
003DECA3  3B D1                           cmp edx, ecx
003DECA5  0F 44 C1                        cmove eax, ecx
003DECA8  C3                              ret
003DECA9  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpDmaGetAdapterVersion(__int64 a1)
{
    __int64 result;

    result = 2;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 156)))) != 2) {
        result = (unsigned int)((2) | (0xFFFFFFFFULL));
        a1 = 3;
        if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 156)))) == ((unsigned int)(a1))) { result = (unsigned int)(a1); }
    }
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HalpDmaGetAdapterVersion(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    result = 2;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x9C)))) != 2) {
        result = (uint32_t)((2) | (0xFFFFFFFFULL));
        Arg1 = 3;
        if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x9C)))) == ((uint32_t)(Arg1))) { result = (uint32_t)(Arg1); }
    }
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x9C` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003DEC8C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003DEC8C[BB_003DEC8C]
  bb_003DEC9B[BB_003DEC9B]
  bb_003DECA8[BB_003DECA8]
  bb_003DECA9[BB_003DECA9]
  bb_003DEC8C -->|branch| bb_003DECA8
  bb_003DEC8C -->|fallthrough| bb_003DEC9B
  bb_003DEC9B -->|flow| bb_003DECA8
```
