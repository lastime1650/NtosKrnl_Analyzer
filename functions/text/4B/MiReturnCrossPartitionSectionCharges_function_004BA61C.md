# MiReturnCrossPartitionSectionCharges

- RVA: `0x004BA61C`–`0x004BA670` (길이 `84` bytes)
- VA: `0x00000001404BA61C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00069B08`
- 디코드: `27`개 명령, `84/84` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **29**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004BA63D` → [MiReturnResident](../28/MiReturnResident_function_00286890.md) (function, `0x00286890`)
- `0x004BA64D` → [MiReturnCrossPartitionCharges](../28/MiReturnCrossPartitionCharges_function_002867D0.md) (function, `0x002867D0`)
- `0x004BA669` → [MiReturnCommit](../24/MiReturnCommit_function_00248410.md) (function, `0x00248410`)

### Direct callers
- [sub_0029430C](../29/Unknown_function_0029430C.md) at `0x002943ED`
- [MiCreatePrototypePtes](../29/MiCreatePrototypePtes_function_002950FC.md) at `0x00295578`
- [MiCreatePrototypePtes](../29/MiCreatePrototypePtes_function_002950FC.md) at `0x00295678`
- [MiRemoveMappedPtes](../29/MiRemoveMappedPtes_function_00296A50.md) at `0x00296C64`
- [MiFlushRelease](../29/MiFlushRelease_function_002982C0.md) at `0x002986C2`
- [MiRemoveViewsFromSectionWithPfn](../29/MiRemoveViewsFromSectionWithPfn_function_002986D4.md) at `0x0029891E`
- [MiDecrementSubsection](../29/MiDecrementSubsection_function_00298D68.md) at `0x00298E72`
- [MiDereferenceControlAreaPfnList](../2A/MiDereferenceControlAreaPfnList_function_002A45E8.md) at `0x002A472A`
- [sub_002E10F7](../2E/Unknown_function_002E10F7.md) at `0x002E11DE`
- [MiReferenceActiveSubsection](../32/MiReferenceActiveSubsection_function_00325060.md) at `0x00325371`
- [MiReferenceActiveSubsection](../32/MiReferenceActiveSubsection_function_00325060.md) at `0x00325722`
- [MiDeleteSubsectionPages](../32/MiDeleteSubsectionPages_function_00326340.md) at `0x00326490`
- [MiDeleteControlArea](../36/MiDeleteControlArea_function_003691F4.md) at `0x003693B8`
- [sub_00371F84](../37/Unknown_function_00371F84.md) at `0x00371FB2`
- [MmPurgeSection](../38/MmPurgeSection_function_0038B450.md) at `0x0038B730`
- [MiUpControlAreaRefs](../3B/MiUpControlAreaRefs_function_003B2BF0.md) at `0x003B2EC6`
- [MiFlushSection](../40/MiFlushSection_function_004036B0.md) at `0x00404640`
- [MiUpdateLastSubsectionSize](../45/MiUpdateLastSubsectionSize_function_0045876C.md) at `0x004588DB`
- [MiCleanSection](../46/MiCleanSection_function_00462E1C.md) at `0x00462FA1`
- [MiReleaseFaultCharges](../47/MiReleaseFaultCharges_function_004798C8.md) at `0x00479979`
- [MiAppendSubsectionChain](../48/MiAppendSubsectionChain_function_00480228.md) at `0x004803C4`
- [MiRemoveSystemCacheReferences](../4C/MiRemoveSystemCacheReferences_function_004CFE50.md) at `0x004CFEC9`
- [MiReturnCrossPartitionControlAreaCharges](../4D/MiReturnCrossPartitionControlAreaCharges_function_004D6184.md) at `0x004D61F5`
- [MiSetDeleteOnClose](../4D/MiSetDeleteOnClose_function_004DD8E8.md) at `0x004DD979`
- [MiMakeUnusedSegmentDeleteOnClose](../67/MiMakeUnusedSegmentDeleteOnClose_function_00678078.md) at `0x00678163`
- [MiUpdateActiveSubsection](../67/MiUpdateActiveSubsection_function_0067F034.md) at `0x0067F15A`
- [sub_006E19B0](../6E/Unknown_function_006E19B0.md) at `0x006E1AA2`
- [sub_006E19B0](../6E/Unknown_function_006E19B0.md) at `0x006E1B7A`
- [MiChargeSegmentCommit](../../page/8C/MiChargeSegmentCommit_function_008CEDE4.md) at `0x008CF0FB`
- [MiExtendSection](../../page/98/MiExtendSection_function_00982FDC.md) at `0x0098347F`
- [MiSegmentDelete](../../page/A1/MiSegmentDelete_function_00A1FBB4.md) at `0x00A1FD3E`
- [sub_00B2A916](../../page/B2/Unknown_function_00B2A916.md) at `0x00B2A9A5`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004BA61C  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
004BA621  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
004BA626  57                              push rdi
004BA627  48 83 EC 20                     sub rsp, 0x20
004BA62B  49 8B D8                        mov rbx, r8
004BA62E  8B F2                           mov esi, edx
004BA630  48 8B F9                        mov rdi, rcx
004BA633  85 D2                           test edx, edx
004BA635  75 2C                           jne 0x1404ba663
004BA637  48 8B D3                        mov rdx, rbx
004BA63A  48 8B CF                        mov rcx, rdi
004BA63D  E8 4E C2 DC FF                  call 0x140286890
004BA642  4C 8B CB                        mov r9, rbx
004BA645  44 8B C6                        mov r8d, esi
004BA648  33 D2                           xor edx, edx
004BA64A  48 8B CF                        mov rcx, rdi
004BA64D  E8 7E C1 DC FF                  call 0x1402867d0
004BA652  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
004BA657  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
004BA65C  48 83 C4 20                     add rsp, 0x20
004BA660  5F                              pop rdi
004BA661  C3                              ret
004BA662  CC                              int3
004BA663  45 33 C0                        xor r8d, r8d
004BA666  48 8B D3                        mov rdx, rbx
004BA669  E8 A2 DD D8 FF                  call 0x140248410
004BA66E  EB C7                           jmp 0x1404ba637
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiReturnCrossPartitionSectionCharges(__int64 a1, int a2, __int64 a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_rsp = (v_rsp) - (32);
    if (a2 != 0) goto loc_004BA663;
loc_004BA637:
    result = MiReturnResident(a1, a3, a3, a4);
    a2 = 0;
    result = MiReturnCrossPartitionCharges(a1, a2, (unsigned int)((unsigned int)((unsigned int)(a2))), a3);
    v_rsp = (v_rsp) + (32);
    return result;
loc_004BA663:
    a3 = 0;
    result = MiReturnCommit(a1, v_stack_p8, a3, a3);
    goto loc_004BA637;
}
```

## 5. (Beta) C Style

```c
int64_t MiReturnCrossPartitionSectionCharges(int64_t Arg1, int32_t Arg2, int64_t Arg3)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    local_rsp = (local_rsp) - (32);
    if (Arg2 != 0) goto loc_004BA663;
loc_004BA637:
    result = MiReturnResident(Arg1, Arg3, Arg3, a4);
    Arg2 = 0;
    result = MiReturnCrossPartitionCharges(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3);
    local_rsp = (local_rsp) + (32);
    return result;
loc_004BA663:
    Arg3 = 0;
    result = MiReturnCommit(Arg1, v_stack_p8, Arg3, Arg3);
    goto loc_004BA637;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004BA61C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004BA61C[BB_004BA61C]
  bb_004BA637[BB_004BA637]
  bb_004BA662[BB_004BA662]
  bb_004BA663[BB_004BA663]
  bb_004BA61C -->|branch| bb_004BA663
  bb_004BA61C -->|fallthrough| bb_004BA637
  bb_004BA662 -->|flow| bb_004BA663
  bb_004BA663 -->|branch| bb_004BA637
```
