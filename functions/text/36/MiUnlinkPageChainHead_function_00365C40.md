# MiUnlinkPageChainHead

- RVA: `0x00365C40`–`0x00365C5F` (길이 `31` bytes)
- VA: `0x0000000140365C40`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `10`개 명령, `31/31` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **23**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [MiLinkPoolCommitChain](../31/MiLinkPoolCommitChain_function_00313D20.md) at `0x00313F9E`
- [MiReturnPhysicalPoolPages](../32/MiReturnPhysicalPoolPages_function_00328568.md) at `0x003285EF`
- [MiPfPutPagesInTransition](MiPfPutPagesInTransition_function_003640EC.md) at `0x0036448E`
- [MiFreeUnmappedPageTables](MiFreeUnmappedPageTables_function_003678E0.md) at `0x0036794C`
- [MiReleasePrefetchGapPages](MiReleasePrefetchGapPages_function_00367C08.md) at `0x00367C11`
- [MiGetPageForEnclave](MiGetPageForEnclave_function_00367C38.md) at `0x00367C52`
- [MiAllocateEnclavePagesForMdl](../3B/MiAllocateEnclavePagesForMdl_function_003B7B54.md) at `0x003B7BE4`
- [MiFreeLargePageChain](../3B/MiFreeLargePageChain_function_003B8CCC.md) at `0x003B8CE4`
- [MiAllocateEnclavePages](../3B/MiAllocateEnclavePages_function_003BC43C.md) at `0x003BC764`
- [MiUnmapMdlCommon](../3E/MiUnmapMdlCommon_function_003E7DF0.md) at `0x003E834A`
- [MiGetClusterPage](../4D/MiGetClusterPage_function_004DC57C.md) at `0x004DCA07`
- [MiFlushFileOnlyDeleteChain](../4F/MiFlushFileOnlyDeleteChain_function_004F5534.md) at `0x004F5651`
- [MiReturnPfnList](../67/MiReturnPfnList_function_0067FBEC.md) at `0x0067FC05`
- [MiReturnPfnList](../67/MiReturnPfnList_function_0067FBEC.md) at `0x0067FC7B`
- [MiGetDanglingExtent](../68/MiGetDanglingExtent_function_006812C4.md) at `0x006812FC`
- [MiPrepareEnclaveMetadataPage](../68/MiPrepareEnclaveMetadataPage_function_00686EAC.md) at `0x00686F83`
- [MiDemoteValidLargePageOneLevel](../68/MiDemoteValidLargePageOneLevel_function_0068A3F4.md) at `0x0068A567`
- [MiMakeVaRangePhysicallyContiguous](../69/MiMakeVaRangePhysicallyContiguous_function_006936E0.md) at `0x00693844`
- [sub_006E3572](../6E/Unknown_function_006E3572.md) at `0x006E35BA`
- [sub_006E7C8A](../6E/Unknown_function_006E7C8A.md) at `0x006E7CAA`
- [MmCreateShadowMapping](../../page/80/MmCreateShadowMapping_function_00807AB0.md) at `0x00807BA6`
- [MiCreateHardwareEnclave](../../page/80/MiCreateHardwareEnclave_function_00808500.md) at `0x0080871C`
- [MiFreeReadListPages](../../page/93/MiFreeReadListPages_function_0093D600.md) at `0x0093D630`
- [MiFreeReadListPages](../../page/93/MiFreeReadListPages_function_0093D600.md) at `0x0093D667`
- [MiFreeReadListPages](../../page/93/MiFreeReadListPages_function_0093D600.md) at `0x0093D68B`
- [MiFreeReadListPages](../../page/93/MiFreeReadListPages_function_0093D600.md) at `0x0093D6C1`
- [MiReturnReservedEnclavePages](../../pagelk/B7/MiReturnReservedEnclavePages_function_00B74FD0.md) at `0x00B74FE9`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00365C40  48 8B 01                        mov rax, qword ptr [rcx]
00365C43  48 85 C0                        test rax, rax
00365C46  74 15                           je 0x140365c5d
00365C48  48 8B 10                        mov rdx, qword ptr [rax]
00365C4B  48 83 69 10 01                  sub qword ptr [rcx + 0x10], 1
00365C50  48 89 11                        mov qword ptr [rcx], rdx
00365C53  75 08                           jne 0x140365c5d
00365C55  48 C7 41 08 00 00 00 00         mov qword ptr [rcx + 8], 0
00365C5D  C3                              ret
00365C5E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiUnlinkPageChainHead(__int64 a1)
{
    if (*(unsigned __int64 *)(a1) == 0) goto loc_00365C5D;
    *(unsigned __int64 *)(a1) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1));
    if (*(unsigned __int64 *)(a1) == 0) {
        *(unsigned __int64 *)(a1 + 8) = 0;
    }
    return *(unsigned __int64 *)(a1);
}
```

## 5. (Beta) C Style

```c
int64_t MiUnlinkPageChainHead(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    if (*(uint64_t *)(arg1) == 0) goto loc_00365C5D;
    *(uint64_t *)(arg1) = *(uint64_t *)(*(uint64_t *)(arg1));
    if (*(uint64_t *)(arg1) == 0) {
        *(uint64_t *)(arg1 + 0x8) = 0;
    }
    return *(uint64_t *)(arg1);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x0` | `64` | `W` |
| `Arg1` | `+ 0x8` | `64` | `W` |
| `Arg1` | `+ 0x10` | `64` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00365C40&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00365C40[BB_00365C40]
  bb_00365C48[BB_00365C48]
  bb_00365C55[BB_00365C55]
  bb_00365C5D[BB_00365C5D]
  bb_00365C5E[BB_00365C5E]
  bb_00365C40 -->|branch| bb_00365C5D
  bb_00365C40 -->|fallthrough| bb_00365C48
  bb_00365C48 -->|branch| bb_00365C5D
  bb_00365C48 -->|fallthrough| bb_00365C55
  bb_00365C55 -->|flow| bb_00365C5D
```
