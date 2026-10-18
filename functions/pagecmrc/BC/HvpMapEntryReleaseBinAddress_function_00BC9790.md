# HvpMapEntryReleaseBinAddress

- RVA: `0x00BC9790`–`0x00BC9798` (길이 `8` bytes)
- VA: `0x0000000140BC9790`
- 실행 섹션: `PAGECMRC`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `4`개 명령, `8/8` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **12**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [HvpReleaseCellPaged](../../page/85/HvpReleaseCellPaged_function_00855F40.md) at `0x00855F79`
- [sub_00859517](../../page/85/Unknown_function_00859517.md) at `0x00859697`
- [HvpFindFreeCell](../../page/85/HvpFindFreeCell_function_00859920.md) at `0x00859B9D`
- [HvpFindFreeCell](../../page/85/HvpFindFreeCell_function_00859920.md) at `0x00859C2C`
- [HvCheckHive](../../page/96/HvCheckHive_function_0096D550.md) at `0x0096D64A`
- [HvpFindNextDirtyBlock](../../page/9B/HvpFindNextDirtyBlock_function_009B5540.md) at `0x009B5699`
- [HvpFindNextDirtyBlock](../../page/9B/HvpFindNextDirtyBlock_function_009B5540.md) at `0x009B573C`
- [HvpFindNextDirtyBlock](../../page/9B/HvpFindNextDirtyBlock_function_009B5540.md) at `0x009B5785`
- [HvpSetRangeProtection](../../page/9B/HvpSetRangeProtection_function_009B58C0.md) at `0x009B59B4`
- [HvpDropPagedBins](../../page/9B/HvpDropPagedBins_function_009B7168.md) at `0x009B7277`
- [HvpMapEntryReleaseBlockAddress](../../page/9B/HvpMapEntryReleaseBlockAddress_function_009B73E8.md) at `0x009B73EC`
- [HvpRemapAndEnlistHiveBins](../../page/9B/HvpRemapAndEnlistHiveBins_function_009B8E0C.md) at `0x009B9113`
- [HvpRemapAndEnlistHiveBins](../../page/9B/HvpRemapAndEnlistHiveBins_function_009B8E0C.md) at `0x009B91E5`
- [HvpRemapAndEnlistHiveBins](../../page/9B/HvpRemapAndEnlistHiveBins_function_009B8E0C.md) at `0x009B93CB`
- [HvWriteExternal](../../page/A8/HvWriteExternal_function_00A83C20.md) at `0x00A83CD5`
- [HvWriteExternal](../../page/A8/HvWriteExternal_function_00A83C20.md) at `0x00A83DE9`
- [sub_00B2E0F0](../../page/B2/Unknown_function_00B2E0F0.md) at `0x00B2E245`
- [sub_00B2E0F0](../../page/B2/Unknown_function_00B2E0F0.md) at `0x00B2E2C7`
- [HvSnapshotHiveToOffsetArray](HvSnapshotHiveToOffsetArray_function_00BC9508.md) at `0x00BC957D`
- [HvSnapshotHiveToOffsetArray](HvSnapshotHiveToOffsetArray_function_00BC9508.md) at `0x00BC9631`
- [HvSnapshotHiveToOffsetArray](HvSnapshotHiveToOffsetArray_function_00BC9508.md) at `0x00BC96BB`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BC9790  33 C0                           xor eax, eax
00BC9792  66 41 89 00                     mov word ptr [r8], ax
00BC9796  C3                              ret
00BC9797  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HvpMapEntryReleaseBinAddress(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;

    result = 0;
    *(unsigned __int16 *)(a3) = 0;
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HvpMapEntryReleaseBinAddress(int64_t Arg1, int64_t Arg2, void *Arg3)
{
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;

    result = 0;
    *(uint16_t *)(arg3) = 0;
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x0` | `16` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagecmrc&rva=0x00BC9790&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00BC9790[BB_00BC9790]
  bb_00BC9797[BB_00BC9797]
```
