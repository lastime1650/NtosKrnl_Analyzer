# ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented

- RVA: `0x002C0F44`–`0x002C0F6B` (길이 `39` bytes)
- VA: `0x00000001402C0F44`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `12`개 명령, `39/39` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **67**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x002C0F60` → [PerfLogSpinLockRelease](../4C/PerfLogSpinLockRelease_function_004CD094.md) (function, `0x004CD094`)

### Direct callers
- [sub_00217146](../21/Unknown_function_00217146.md) at `0x00217175`
- [sub_002219E9](../22/Unknown_function_002219E9.md) at `0x00221B11`
- [sub_002219E9](../22/Unknown_function_002219E9.md) at `0x00221B31`
- [sub_00221B4E](../22/Unknown_function_00221B4E.md) at `0x00221B64`
- [sub_00221B4E](../22/Unknown_function_00221B4E.md) at `0x00221C69`
- [sub_00238CD1](../23/Unknown_function_00238CD1.md) at `0x00238D77`
- [sub_00238CD1](../23/Unknown_function_00238CD1.md) at `0x00238D9A`
- [MiReacquireHigherPageTableLock](../23/MiReacquireHigherPageTableLock_function_00239650.md) at `0x00239CDB`
- [ExReleaseSpinLockRegardlessFromDpcLevel](../23/ExReleaseSpinLockRegardlessFromDpcLevel_function_0023A330.md) at `0x0023A39D`
- [MiReleaseSpinLockExclusive](../24/MiReleaseSpinLockExclusive_function_002482C0.md) at `0x00248322`
- [MiReleaseSpinLockExclusive](../24/MiReleaseSpinLockExclusive_function_002482C0.md) at `0x00248338`
- [sub_0024967C](../24/Unknown_function_0024967C.md) at `0x00249692`
- [ExReleaseSpinLockExclusiveFromDpcLevel](../24/ExReleaseSpinLockExclusiveFromDpcLevel_function_002497E0.md) at `0x00249808`
- [PopPepProcessEvent](../24/PopPepProcessEvent_function_0024B930.md) at `0x0024CBFC`
- [PopPepProcessEvent](../24/PopPepProcessEvent_function_0024B930.md) at `0x0024CC29`
- [PopPepReleaseActivityLink](../24/PopPepReleaseActivityLink_function_0024CC90.md) at `0x0024CD5E`
- [PopPepReleaseActivityLink](../24/PopPepReleaseActivityLink_function_0024CC90.md) at `0x0024CD77`
- [KiAbEntryRemoveFromTree](../26/KiAbEntryRemoveFromTree_function_00262410.md) at `0x00262B66`
- [KiAbEntryRemoveFromTree](../26/KiAbEntryRemoveFromTree_function_00262410.md) at `0x00262B88`
- [KiAbEntryRemoveFromTree](../26/KiAbEntryRemoveFromTree_function_00262410.md) at `0x00262BA8`
- [sub_002648E7](../26/Unknown_function_002648E7.md) at `0x002648FA`
- [sub_002648E7](../26/Unknown_function_002648E7.md) at `0x00264917`
- [MiDeleteVaDirect](../27/MiDeleteVaDirect_function_00277560.md) at `0x0027894F`
- [MiWalkPageTablesRecursively](../27/MiWalkPageTablesRecursively_function_002796C0.md) at `0x0027B6F6`
- [MiReleaseFaultState](../27/MiReleaseFaultState_function_0027D290.md) at `0x0027D65C`
- [sub_0027D95C](../27/Unknown_function_0027D95C.md) at `0x0027DBC5`
- [MiUnlockWorkingSetExclusive](../27/MiUnlockWorkingSetExclusive_function_0027EC70.md) at `0x0027EDDE`
- [MiUnlockWorkingSetExclusive](../27/MiUnlockWorkingSetExclusive_function_0027EC70.md) at `0x0027EE1D`
- [MiUnlockWorkingSetExclusive](../27/MiUnlockWorkingSetExclusive_function_0027EC70.md) at `0x0027EE49`
- [MiCaptureDeleteHierarchy](../27/MiCaptureDeleteHierarchy_function_0027F5F0.md) at `0x0027FD6D`
- [MiMakeSystemAddressValid](../27/MiMakeSystemAddressValid_function_0027FF70.md) at `0x00280C01`
- [MiLockLowestValidPageTableEx](../28/MiLockLowestValidPageTableEx_function_00280D10.md) at `0x002816E3`
- [sub_0028271E](../28/Unknown_function_0028271E.md) at `0x00282734`
- [sub_0028271E](../28/Unknown_function_0028271E.md) at `0x0028279E`
- [MiReleasePageFileInfo](../28/MiReleasePageFileInfo_function_00283FD0.md) at `0x00284530`
- [MiCheckControlArea](../28/MiCheckControlArea_function_002861B0.md) at `0x00286478`
- [MiCheckControlArea](../28/MiCheckControlArea_function_002861B0.md) at `0x00286499`
- [MiAddPageToFlushMdl](../28/MiAddPageToFlushMdl_function_00286930.md) at `0x00286C11`
- [MiRemoveDecayClusterTimer](../28/MiRemoveDecayClusterTimer_function_00288178.md) at `0x002881E6`
- [sub_0028F57A](../28/Unknown_function_0028F57A.md) at `0x0028F594`
- [sub_0028F57A](../28/Unknown_function_0028F57A.md) at `0x0028F5B8`
- [sub_00291D0B](../29/Unknown_function_00291D0B.md) at `0x00291D85`
- [MiUpdateSystemProtoPtesTree](../29/MiUpdateSystemProtoPtesTree_function_00295F0C.md) at `0x002961C7`
- [MiUpdateSystemProtoPtesTree](../29/MiUpdateSystemProtoPtesTree_function_00295F0C.md) at `0x002961EB`
- [MiUnlockVadTree](../29/MiUnlockVadTree_function_00297020.md) at `0x002970FB`
- [MiUnlockVadTree](../29/MiUnlockVadTree_function_00297020.md) at `0x0029715B`
- [MiDecrementModifiedWriteCount](../29/MiDecrementModifiedWriteCount_function_00298184.md) at `0x0029822E`
- [MiRemoveUnusedSubsection](../2A/MiRemoveUnusedSubsection_function_002A6194.md) at `0x002A6202`
- [MiReleasePageListLock](../2B/MiReleasePageListLock_function_002B1050.md) at `0x002B110A`
- [MiCreateDecayPfn](../2B/MiCreateDecayPfn_function_002B8764.md) at `0x002B8AC1`
- [MiInsertDecayClusterTimer](../2B/MiInsertDecayClusterTimer_function_002BADF4.md) at `0x002BAE68`
- [MmDoesFileHaveUserWritableReferences](../2B/MmDoesFileHaveUserWritableReferences_function_002BB690.md) at `0x002BB7B1`
- [MmDoesFileHaveUserWritableReferences](../2B/MmDoesFileHaveUserWritableReferences_function_002BB690.md) at `0x002BB7CE`
- [MmDoesFileHaveUserWritableReferences](../2B/MmDoesFileHaveUserWritableReferences_function_002BB690.md) at `0x002BB7EA`
- [MiComputeFlushRange](../2B/MiComputeFlushRange_function_002BB8D0.md) at `0x002BB9FA`
- [sub_002BBE36](../2B/Unknown_function_002BBE36.md) at `0x002BBE64`
- [MiReferenceControlArea](../2B/MiReferenceControlArea_function_002BC198.md) at `0x002BC3F8`
- [MiLockSectionControlArea](../2B/MiLockSectionControlArea_function_002BC930.md) at `0x002BCB5C`
- [MiLockSectionControlArea](../2B/MiLockSectionControlArea_function_002BC930.md) at `0x002BCB83`
- [MiLockSectionControlArea](../2B/MiLockSectionControlArea_function_002BC930.md) at `0x002BCBA7`
- [PopPepWork](../2B/PopPepWork_function_002BCBC0.md) at `0x002BD0CB`
- [sub_002BE613](../2B/Unknown_function_002BE613.md) at `0x002BE62A`
- [sub_002BE613](../2B/Unknown_function_002BE613.md) at `0x002BE64B`
- [MiUnlockWorkingSetCoreExclusive](MiUnlockWorkingSetCoreExclusive_function_002C0DC4.md) at `0x002C0DFF`
- [ExReleaseSpinLockExclusive](ExReleaseSpinLockExclusive_function_002C0EF0.md) at `0x002C0F37`
- [MiComputeAgingAmount](MiComputeAgingAmount_function_002C2520.md) at `0x002C26DD`
- [sub_002E0B15](../2E/Unknown_function_002E0B15.md) at `0x002E104B`
- [sub_002E0B15](../2E/Unknown_function_002E0B15.md) at `0x002E106E`
- [RtlpHpReleaseQueuedLockExclusive](../2E/RtlpHpReleaseQueuedLockExclusive_function_002E2A70.md) at `0x002E2BFC`
- [sub_002E3438](../2E/Unknown_function_002E3438.md) at `0x002E344F`
- [ExpAddTagForBigPages](../2E/ExpAddTagForBigPages_function_002EF570.md) at `0x002EF89D`
- [MiGetUltraMapping](../32/MiGetUltraMapping_function_00323270.md) at `0x003237CE`
- [MiGetUltraMapping](../32/MiGetUltraMapping_function_00323270.md) at `0x003237F2`
- [sub_0032439E](../32/Unknown_function_0032439E.md) at `0x003243B1`
- [MiAddViewsForSection](../32/MiAddViewsForSection_function_00324990.md) at `0x00324E8F`
- [MiAddViewsForSection](../32/MiAddViewsForSection_function_00324990.md) at `0x00324EB3`
- [MiReferenceActiveSubsection](../32/MiReferenceActiveSubsection_function_00325060.md) at `0x003253E3`
- [MiReferenceActiveSubsection](../32/MiReferenceActiveSubsection_function_00325060.md) at `0x00325402`
- [sub_003354FB](../33/Unknown_function_003354FB.md) at `0x00335EF1`
- [MiUnlinkFreeOrZeroedPage](../33/MiUnlinkFreeOrZeroedPage_function_00336C40.md) at `0x0033765D`
- [MiDecayNodeNowEmpty](../33/MiDecayNodeNowEmpty_function_0033C938.md) at `0x0033CA5F`
- [PfSnGetFileInformation](../34/PfSnGetFileInformation_function_00343210.md) at `0x0034368D`
- [sub_0034CD25](../34/Unknown_function_0034CD25.md) at `0x0034CDB6`
- [sub_0038BBFB](../38/Unknown_function_0038BBFB.md) at `0x0038BCAB`
- [PspUpdateContainerImpersonation](../39/PspUpdateContainerImpersonation_function_003931EC.md) at `0x003933C7`
- [sub_0039410B](../39/Unknown_function_0039410B.md) at `0x00394128`
- [sub_00395529](../39/Unknown_function_00395529.md) at `0x00395546`
- [KiReleaseProcessLockExclusive](../3C/KiReleaseProcessLockExclusive_function_003C2660.md) at `0x003C26AA`
- [sub_00418843](../41/Unknown_function_00418843.md) at `0x00418859`
- [sub_00418843](../41/Unknown_function_00418843.md) at `0x00418879`
- [ExpAddResourceToSystemResourceList](../41/ExpAddResourceToSystemResourceList_function_0041FA30.md) at `0x0041FAC5`
- [sub_004201AA](../42/Unknown_function_004201AA.md) at `0x004204FB`
- [PfSnNameRemove](../43/PfSnNameRemove_function_0043E3C0.md) at `0x0043E4AB`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002C0F44  48 83 EC 28                     sub rsp, 0x28
002C0F48  4C 8B CA                        mov r9, rdx
002C0F4B  0F 31                           rdtsc
002C0F4D  48 C1 E2 20                     shl rdx, 0x20
002C0F51  48 0B C2                        or rax, rdx
002C0F54  C7 01 00 00 00 00               mov dword ptr [rcx], 0
002C0F5A  4C 8B C0                        mov r8, rax
002C0F5D  49 8B D1                        mov rdx, r9
002C0F60  E8 2F C1 20 00                  call 0x1404cd094
002C0F65  48 83 C4 28                     add rsp, 0x28
002C0F69  C3                              ret
002C0F6A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a2 = (a2) << (32);
    result = (result) | (a2);
    *(unsigned int *)(a1) = 0;
    result = PerfLogSpinLockRelease(a1, a2, result, a2);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented(void *Arg1, int64_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    Arg2 = (Arg2) << (32);
    result = (result) | (Arg2);
    *(uint32_t *)(arg1) = 0;
    result = PerfLogSpinLockRelease(Arg1, Arg2, result, Arg2);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002C0F44&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002C0F44[BB_002C0F44]
  bb_002C0F6A[BB_002C0F6A]
```
