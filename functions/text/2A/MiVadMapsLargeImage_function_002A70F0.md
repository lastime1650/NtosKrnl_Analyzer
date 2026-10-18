# MiVadMapsLargeImage

- RVA: `0x002A70F0`–`0x002A7105` (길이 `21` bytes)
- VA: `0x00000001402A70F0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `11`개 명령, `21/21` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **11**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [MiEmptyWorkingSetPrivatePagesByVa](MiEmptyWorkingSetPrivatePagesByVa_function_002A6AC0.md) at `0x002A6B63`
- [MmOutSwapWorkingSet](MmOutSwapWorkingSet_function_002A6BC8.md) at `0x002A6E4D`
- [MiSoftFaultMappedView](../36/MiSoftFaultMappedView_function_00365364.md) at `0x003653D3`
- [MiIsVadEligibleForCommitRelease](../4F/MiIsVadEligibleForCommitRelease_function_004FB6FC.md) at `0x004FB70F`
- [MmProtectVirtualMemory](../../page/88/MmProtectVirtualMemory_function_00881050.md) at `0x0088130C`
- [MiUnmapViewOfSection](../../page/88/MiUnmapViewOfSection_function_0088A4C4.md) at `0x0088A7C1`
- [MmSecureVirtualMemoryAgainstWrites](../../page/89/MmSecureVirtualMemoryAgainstWrites_function_00890164.md) at `0x008902EE`
- [MiMarkPrivateImageCfgBits](../../page/8D/MiMarkPrivateImageCfgBits_function_008D07FC.md) at `0x008D0861`
- [MmEnumerateAddressSpaceAndReferenceImages](../../page/97/MmEnumerateAddressSpaceAndReferenceImages_function_0097DD50.md) at `0x0097DEF5`
- [MiFillMapFileInfo](../../page/97/MiFillMapFileInfo_function_0097E15C.md) at `0x0097E32B`
- [MmQueryVirtualMemory](../../page/9D/MmQueryVirtualMemory_function_009D9280.md) at `0x009D9CA5`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002A70F0  8B 41 30                        mov eax, dword ptr [rcx + 0x30]
002A70F3  24 70                           and al, 0x70
002A70F5  3C 20                           cmp al, 0x20
002A70F7  74 04                           je 0x1402a70fd
002A70F9  33 C0                           xor eax, eax
002A70FB  C3                              ret
002A70FC  CC                              int3
002A70FD  8B 41 40                        mov eax, dword ptr [rcx + 0x40]
002A7100  83 E0 01                        and eax, 1
002A7103  C3                              ret
002A7104  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiVadMapsLargeImage(__int64 a1)
{
    __int64 result;

    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(a1 + 48))) & (112));
    if (((unsigned __int8)(result)) == 32) goto loc_002A70FD;
    result = 0;
    return result;
loc_002A70FD:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 64))) & (1));
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiVadMapsLargeImage(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    result = (uint8_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x30))) & (112));
    if (((uint8_t)(result)) == 32) goto loc_002A70FD;
    result = 0;
    return result;
loc_002A70FD:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x40))) & (1));
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x30` | `32` | `R` |
| `Arg1` | `+ 0x40` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002A70F0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002A70F0[BB_002A70F0]
  bb_002A70F9[BB_002A70F9]
  bb_002A70FC[BB_002A70FC]
  bb_002A70FD[BB_002A70FD]
  bb_002A7104[BB_002A7104]
  bb_002A70F0 -->|branch| bb_002A70FD
  bb_002A70F0 -->|fallthrough| bb_002A70F9
  bb_002A70FC -->|flow| bb_002A70FD
```
