# RtlGetHotPatchSize

- RVA: `0x006AA1D0`–`0x006AA1DF` (길이 `15` bytes)
- VA: `0x00000001406AA1D0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `6`개 명령, `15/15` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **7**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [RtlHotPatchSynchronizationRequired](RtlHotPatchSynchronizationRequired_function_006AA21C.md) at `0x006AA255`
- [MiApplyDriverHotPatch](../../page/80/MiApplyDriverHotPatch_function_008018EC.md) at `0x00801BCC`
- [MiPrepareDriverForHotPatch](../../page/80/MiPrepareDriverForHotPatch_function_008066F4.md) at `0x0080670F`
- [RtlCountRequiredHotPatchAddressTableEntries](../../page/84/RtlCountRequiredHotPatchAddressTableEntries_function_00840BF8.md) at `0x00840C2B`
- [RtlEnumerateHotPatchPatches](../../page/84/RtlEnumerateHotPatchPatches_function_00840DE8.md) at `0x00840E0E`
- [RtlValidateHotPatchBase](../../page/84/RtlValidateHotPatchBase_function_008411D0.md) at `0x0084124C`
- [RtlApplyHotPatch](../../pagelk/B7/RtlApplyHotPatch_function_00B7528C.md) at `0x00B7534A`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006AA1D0  83 39 03                        cmp dword ptr [rcx], 3
006AA1D3  B8 02 00 00 00                  mov eax, 2
006AA1D8  72 03                           jb 0x1406aa1dd
006AA1DA  03 41 18                        add eax, dword ptr [rcx + 0x18]
006AA1DD  C3                              ret
006AA1DE  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlGetHotPatchSize(__int64 a1)
{
    __int64 result;

    result = 2;
    if ((*(unsigned int *)(a1)) >= 3) {
        result = (unsigned int)((2) + (*(unsigned int *)(a1 + 24)));
    }
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t RtlGetHotPatchSize(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    result = 2;
    if ((*(uint32_t *)(arg1)) >= 3) {
        result = (uint32_t)((2) + (*(uint32_t *)(arg1 + 0x18)));
    }
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x18` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006AA1D0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006AA1D0[BB_006AA1D0]
  bb_006AA1DA[BB_006AA1DA]
  bb_006AA1DD[BB_006AA1DD]
  bb_006AA1DE[BB_006AA1DE]
  bb_006AA1D0 -->|branch| bb_006AA1DD
  bb_006AA1D0 -->|fallthrough| bb_006AA1DA
  bb_006AA1DA -->|flow| bb_006AA1DD
```
