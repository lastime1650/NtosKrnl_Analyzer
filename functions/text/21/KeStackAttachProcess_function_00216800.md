# KeStackAttachProcess

- RVA: `0x00216800`–`0x00216814` (길이 `20` bytes)
- VA: `0x0000000140216800`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `7`개 명령, `20/20` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **53**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00216809` → [KiStackAttachProcess](KiStackAttachProcess_function_00216820.md) (function, `0x00216820`)

### Direct callers
- [SepRmCallLsa](../22/SepRmCallLsa_function_00223630.md) at `0x002236A4`
- [SepAdtLogAuditRecord](../22/SepAdtLogAuditRecord_function_00224B6C.md) at `0x00224D65`
- [MiGetWorkingSetInfoEx](../29/MiGetWorkingSetInfoEx_function_0029E640.md) at `0x0029E700`
- [sub_003AA889](../3A/Unknown_function_003AA889.md) at `0x003AA891`
- [SMKM_STORE&lt;SM_TRAITS&gt;::SmStCleanup](../3B/SMKM_STORE_SM_TRAITS_SmStCleanup_function_003B00E0.md) at `0x003B02AF`
- [SmQuerySystemInformation](../3B/SmQuerySystemInformation_function_003B29F8.md) at `0x003B2A33`
- [MiFlushAllPages](../3B/MiFlushAllPages_function_003BD294.md) at `0x003BD32C`
- [PsQueryProcessCommandLine](../46/PsQueryProcessCommandLine_function_00469810.md) at `0x004698B3`
- [CmSiAcquireProcessLockedPagesCharge](../47/CmSiAcquireProcessLockedPagesCharge_function_0047D714.md) at `0x0047D756`
- [CmSiReleaseProcessLockedPagesCharge](../47/CmSiReleaseProcessLockedPagesCharge_function_0047D81C.md) at `0x0047D858`
- [SMKM_STORE&lt;SM_TRAITS&gt;::SmStSwapStore](../49/SMKM_STORE_SM_TRAITS_SmStSwapStore_function_00496A68.md) at `0x00496AA4`
- [DbgkQueueUserExceptionReport](../../page/71/DbgkQueueUserExceptionReport_function_00710B04.md) at `0x00710C65`
- [DbgkUserReportWorkRoutine](../../page/71/DbgkUserReportWorkRoutine_function_00710D10.md) at `0x00710D9B`
- [IopIsNotNativeDriverImage](../../page/71/IopIsNotNativeDriverImage_function_0071B914.md) at `0x0071BA2F`
- [AlpcpForceUnlinkSecureView](../../page/74/AlpcpForceUnlinkSecureView_function_0074C604.md) at `0x0074C660`
- [PspShutdownCsrProcess](../../page/78/PspShutdownCsrProcess_function_00780214.md) at `0x00780366`
- [PsTerminateMinimalProcess](../../page/78/PsTerminateMinimalProcess_function_007861A8.md) at `0x0078627F`
- [PspCatchCriticalBreak](../../page/78/PspCatchCriticalBreak_function_00786408.md) at `0x0078650B`
- [SmHwAcceleratorPartitionMgrCleanup](../../page/7A/SmHwAcceleratorPartitionMgrCleanup_function_007AB34C.md) at `0x007AB3E3`
- [VmpPrefetchWorker](../../page/7A/VmpPrefetchWorker_function_007ADD20.md) at `0x007ADD53`
- [EtwpUpdateProcessTracingCallback](../../page/7B/EtwpUpdateProcessTracingCallback_function_007B8F40.md) at `0x007B8FAD`
- [CmpAddRemoveContainerToCLFSLog](../../page/7F/CmpAddRemoveContainerToCLFSLog_function_007F69FC.md) at `0x007F6B6B`
- [CmpStartCLFSLog](../../page/7F/CmpStartCLFSLog_function_007F7228.md) at `0x007F735D`
- [MiHotPatchAllProcesses](../../page/80/MiHotPatchAllProcesses_function_00803AC4.md) at `0x00803B1E`
- [MiInSwapSharedWorkingSetWorker](../../page/80/MiInSwapSharedWorkingSetWorker_function_0080C510.md) at `0x0080C561`
- [ObpDecrementHandleCount](../../page/86/ObpDecrementHandleCount_function_008632E0.md) at `0x008633AF`
- [ObCloseHandleTableEntry](../../page/86/ObCloseHandleTableEntry_function_00869E20.md) at `0x0086A122`
- [ObCloseHandleTableEntry](../../page/86/ObCloseHandleTableEntry_function_00869E20.md) at `0x0086A51B`
- [ObpCreateHandle](../../page/86/ObpCreateHandle_function_0086B950.md) at `0x0086D564`
- [ObpIncrementHandleCountEx](../../page/86/ObpIncrementHandleCountEx_function_0086DA10.md) at `0x0086E1EC`
- [MmDeleteTeb](../../page/87/MmDeleteTeb_function_0087FAC0.md) at `0x0087FB07`
- [sub_0088018D](../../page/88/Unknown_function_0088018D.md) at `0x00880200`
- [AlpcpRestoreWriteAccess](../../page/88/AlpcpRestoreWriteAccess_function_00889990.md) at `0x008899EC`
- [AlpcpPrepareViewForDelivery](../../page/88/AlpcpPrepareViewForDelivery_function_00889A44.md) at `0x00889B5D`
- [MiUnmapViewOfSection](../../page/88/MiUnmapViewOfSection_function_0088A4C4.md) at `0x0088A541`
- [MmSecureVirtualMemoryAgainstWrites](../../page/89/MmSecureVirtualMemoryAgainstWrites_function_00890164.md) at `0x00890393`
- [MiMapViewOfSection](../../page/89/MiMapViewOfSection_function_00898F10.md) at `0x00899190`
- [EtwpWriteProcessEvent](../../page/8A/EtwpWriteProcessEvent_function_008A420C.md) at `0x008A43A5`
- [EtwTraceAppStateChange](../../page/8A/EtwTraceAppStateChange_function_008A452C.md) at `0x008A48B7`
- [EtwpProcessEnumCallback](../../page/8A/EtwpProcessEnumCallback_function_008A5F40.md) at `0x008A610B`
- [ObDuplicateObject](../../page/8C/ObDuplicateObject_function_008C4FA0.md) at `0x008C535A`
- [ObDuplicateObject](../../page/8C/ObDuplicateObject_function_008C4FA0.md) at `0x008C5794`
- [ObDuplicateObject](../../page/8C/ObDuplicateObject_function_008C4FA0.md) at `0x008C5A66`
- [ObDuplicateObject](../../page/8C/ObDuplicateObject_function_008C4FA0.md) at `0x008C5EAD`
- [PspWriteTebImpersonationInfo](../../page/8C/PspWriteTebImpersonationInfo_function_008CC7F0.md) at `0x008CC9BB`
- [ExSweepHandleTable](../../page/90/ExSweepHandleTable_function_00904D3C.md) at `0x00904F02`
- [PspRundownSingleProcess](../../page/90/PspRundownSingleProcess_function_00906D50.md) at `0x00906DF4`
- [MmIsFileMapped](../../page/91/MmIsFileMapped_function_0091D8D4.md) at `0x0091D937`
- [MmPrefetchVirtualMemory](../../page/93/MmPrefetchVirtualMemory_function_0093A698.md) at `0x0093A7DB`
- [MiMapImageInSystemSpace](../../page/94/MiMapImageInSystemSpace_function_00941DD8.md) at `0x00942031`
- [MmEnumerateAddressSpaceAndReferenceImages](../../page/97/MmEnumerateAddressSpaceAndReferenceImages_function_0097DD50.md) at `0x0097E0B1`
- [MiCopyVirtualMemory](../../page/9B/MiCopyVirtualMemory_function_009BBB50.md) at `0x009BBCC6`
- [MiCopyVirtualMemory](../../page/9B/MiCopyVirtualMemory_function_009BBB50.md) at `0x009BBFC4`
- [MiInSwapStoreWorker](../../page/A6/MiInSwapStoreWorker_function_00A61C60.md) at `0x00A61C97`
- [SepCleanupLUIDDeviceMapDirectory](../../page/A9/SepCleanupLUIDDeviceMapDirectory_function_00A98F24.md) at `0x00A99155`
- [DbgkpMarkProcessPeb](../../page/AC/DbgkpMarkProcessPeb_function_00AC8D0C.md) at `0x00AC8D6C`
- [sub_00B19294](../../page/B1/Unknown_function_00B19294.md) at `0x00B19326`
- [sub_00B19294](../../page/B1/Unknown_function_00B19294.md) at `0x00B19383`
- [CmpAttachToRegistryProcess](../../pagecmrc/BC/CmpAttachToRegistryProcess_function_00BC98E0.md) at `0x00BC98F3`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00216800  48 83 EC 28                     sub rsp, 0x28
00216804  4C 8B C2                        mov r8, rdx
00216807  33 D2                           xor edx, edx
00216809  E8 12 00 00 00                  call 0x140216820
0021680E  48 83 C4 28                     add rsp, 0x28
00216812  C3                              ret
00216813  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KeStackAttachProcess(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a2 = 0;
    result = KiStackAttachProcess(a1, a2, a2, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KeStackAttachProcess(int64_t Arg1, int64_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    Arg2 = 0;
    result = KiStackAttachProcess(Arg1, Arg2, Arg2, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00216800&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00216800[BB_00216800]
  bb_00216813[BB_00216813]
```
