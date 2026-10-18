# MiDeleteUltraThreadContext

- RVA: `0x00322C90`–`0x00322C9B` (길이 `11` bytes)
- VA: `0x0000000140322C90`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00075824`
- 디코드: `5`개 명령, `11/11` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **15**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [MiCreateUltraThreadContext](../28/MiCreateUltraThreadContext_function_00288200.md) at `0x00288358`
- [MiCreateUltraThreadContext](../28/MiCreateUltraThreadContext_function_00288200.md) at `0x0028837E`
- [MiFindContiguousPagesEx](../28/MiFindContiguousPagesEx_function_0028BDE0.md) at `0x0028C462`
- [MiFindContiguousPagesEx](../28/MiFindContiguousPagesEx_function_0028BDE0.md) at `0x0028C4E1`
- [MiZeroInParallelWorker](../2C/MiZeroInParallelWorker_function_002C6600.md) at `0x002C6780`
- [MiZeroLargePage](../2C/MiZeroLargePage_function_002C6914.md) at `0x002C6C10`
- [MiInitializeNewUltraHugeContext](../3F/MiInitializeNewUltraHugeContext_function_003FB974.md) at `0x003FBADD`
- [MiInitializeNewUltraHugeContext](../3F/MiInitializeNewUltraHugeContext_function_003FB974.md) at `0x003FBB4C`
- [MiDereferenceHugeContext](../4D/MiDereferenceHugeContext_function_004D9664.md) at `0x004D97D9`
- [MiDeleteZeroThreadContext](../4D/MiDeleteZeroThreadContext_function_004DF788.md) at `0x004DF7AF`
- [MiHugePageOperation](../68/MiHugePageOperation_function_0068C490.md) at `0x0068C63A`
- [MiDefragmentSlabWorker](../68/MiDefragmentSlabWorker_function_0068D730.md) at `0x0068DA03`
- [MiFreeForkMappingPte](../../page/70/MiFreeForkMappingPte_function_00705848.md) at `0x0070586C`
- [MmDeleteProcessor](../../page/7F/MmDeleteProcessor_function_007F8FB4.md) at `0x007F8FEA`
- [MiReleaseScrubPacket](../../page/80/MiReleaseScrubPacket_function_0080ED24.md) at `0x0080ED31`
- [MmRelocatePfnList](../../page/90/MmRelocatePfnList_function_00901E70.md) at `0x009020D6`
- [MiCombineIdenticalPages](../../page/AB/MiCombineIdenticalPages_function_00AB2324.md) at `0x00AB25D5`
- [MmInitializeProcessor](../../pagelk/B7/MmInitializeProcessor_function_00B737F8.md) at `0x00B738DE`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00322C90  40 53                           push rbx
00322C92  56                              push rsi
00322C93  41 55                           push r13
00322C95  41 56                           push r14
00322C97  48 83 EC 28                     sub rsp, 0x28
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall MiDeleteUltraThreadContext(void)
{
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    return;
}
```

## 5. (Beta) C Style

```c
void MiDeleteUltraThreadContext(void)
{
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    return;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00322C90&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00322C90[BB_00322C90]
```
