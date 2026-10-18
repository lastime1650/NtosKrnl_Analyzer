# MiMakeValidPte

- RVA: `0x002C5590`–`0x002C5596` (길이 `6` bytes)
- VA: `0x00000001402C5590`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006EAB0`
- 디코드: `2`개 명령, `6/6` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **84**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [MmProtectMdlSystemAddress](../22/MmProtectMdlSystemAddress_function_00227B50.md) at `0x00227D3C`
- [MiReplacePageTablePage](../22/MiReplacePageTablePage_function_00229184.md) at `0x002292BE`
- [MiMapSinglePage](../22/MiMapSinglePage_function_00229D00.md) at `0x00229D9E`
- [MiMapArbitraryPage](../22/MiMapArbitraryPage_function_0022A44C.md) at `0x0022A52A`
- [MiResolveProtoCombine](../22/MiResolveProtoCombine_function_0022CD00.md) at `0x0022CE96`
- [MmProtectPool](../26/MmProtectPool_function_002697AC.md) at `0x0026996D`
- [MmProtectPool](../26/MmProtectPool_function_002697AC.md) at `0x00269B7E`
- [MiAllocateKernelStackPages](../2A/MiAllocateKernelStackPages_function_002A1BEC.md) at `0x002A1DF2`
- [MiMakeSystemCachePteValid](../2A/MiMakeSystemCachePteValid_function_002A35D8.md) at `0x002A3834`
- [MiInsertPhysicalPteMapping](../2A/MiInsertPhysicalPteMapping_function_002AE26C.md) at `0x002AE35E`
- [MiCreateSharedZeroPages](../2B/MiCreateSharedZeroPages_function_002B6318.md) at `0x002B6552`
- [MiMakePageAvoidRead](../2B/MiMakePageAvoidRead_function_002B7DE0.md) at `0x002B81D2`
- [MiUnlinkStandbyPfn](MiUnlinkStandbyPfn_function_002C3510.md) at `0x002C3613`
- [MiRevertValidPte](MiRevertValidPte_function_002C5160.md) at `0x002C528B`
- [MiCompleteRestrictedImageFault](MiCompleteRestrictedImageFault_function_002C60D4.md) at `0x002C626F`
- [sub_002F6E32](../2F/Unknown_function_002F6E32.md) at `0x002F7120`
- [sub_002F6E32](../2F/Unknown_function_002F6E32.md) at `0x002F72B0`
- [sub_002F6E32](../2F/Unknown_function_002F6E32.md) at `0x002F740E`
- [MiLinkPoolCommitChain](../31/MiLinkPoolCommitChain_function_00313D20.md) at `0x00313FFC`
- [MiFillSystemPtes](../31/MiFillSystemPtes_function_00319850.md) at `0x00319E09`
- [MiFillSystemPtes](../31/MiFillSystemPtes_function_00319850.md) at `0x00319F53`
- [MiComputeCombineHash](../32/MiComputeCombineHash_function_003227C0.md) at `0x003228BB`
- [MiGetUltraMapping](../32/MiGetUltraMapping_function_00323270.md) at `0x00323627`
- [MiGetUltraMapping](../32/MiGetUltraMapping_function_00323270.md) at `0x0032374A`
- [sub_0033284A](../33/Unknown_function_0033284A.md) at `0x00332882`
- [sub_00332A20](../33/Unknown_function_00332A20.md) at `0x00332A98`
- [MiReplacePageOfProtoPool](../36/MiReplacePageOfProtoPool_function_00364BB8.md) at `0x00364CCA`
- [MiAddPagesToEnclave](../36/MiAddPagesToEnclave_function_00367EEC.md) at `0x0036818A`
- [MiDecommitHardwareEnclavePages](../36/MiDecommitHardwareEnclavePages_function_003688D4.md) at `0x00368A60`
- [MiPrivateFixup](../36/MiPrivateFixup_function_003693E8.md) at `0x003696B1`
- [MiSetSystemCodeProtection](../38/MiSetSystemCodeProtection_function_00384420.md) at `0x0038457D`
- [MiMapWithLargePages](../3B/MiMapWithLargePages_function_003B6624.md) at `0x003B6731`
- [MiUnmapMdlCommon](../3E/MiUnmapMdlCommon_function_003E7DF0.md) at `0x003E837D`
- [MiInsertLargeVadMapping](../3F/MiInsertLargeVadMapping_function_003F0498.md) at `0x003F053C`
- [MiScrubPage](../3F/MiScrubPage_function_003F954C.md) at `0x003F9602`
- [MiBuildReservationCluster](../40/MiBuildReservationCluster_function_004071A0.md) at `0x0040739D`
- [MiMakeOutswappedPageResident](../43/MiMakeOutswappedPageResident_function_00431AD0.md) at `0x00431C44`
- [MiInitializeSelfmap](../43/MiInitializeSelfmap_function_0043202C.md) at `0x00432049`
- [MiUpdateImagePfnImportRelocations](../44/MiUpdateImagePfnImportRelocations_function_00449E84.md) at `0x00449F42`
- [MiInitializeSystemPageTable](../45/MiInitializeSystemPageTable_function_00451C88.md) at `0x00451DBC`
- [MiCopyTopLevelMappings](../46/MiCopyTopLevelMappings_function_0046C54C.md) at `0x0046C566`
- [MiMapPageFileHash](../49/MiMapPageFileHash_function_004921E0.md) at `0x004924A5`
- [MiMapMemoryDumpMdl](../4A/MiMapMemoryDumpMdl_function_004A619C.md) at `0x004A6307`
- [MiWriteAwePtes](../4C/MiWriteAwePtes_function_004C51E0.md) at `0x004C535F`
- [MiWriteAwePtes](../4C/MiWriteAwePtes_function_004C51E0.md) at `0x004C5515`
- [MiWriteAwePtes](../4C/MiWriteAwePtes_function_004C51E0.md) at `0x004C55B0`
- [MiProtectAweRegion](../4C/MiProtectAweRegion_function_004CE62C.md) at `0x004CEC15`
- [MiProtectEnclavePages](../4D/MiProtectEnclavePages_function_004D5528.md) at `0x004D574C`
- [MiMapKernelScp](../4D/MiMapKernelScp_function_004DCAD4.md) at `0x004DCC38`
- [MiMakeLargePageTable](../4F/MiMakeLargePageTable_function_004F9198.md) at `0x004F936B`
- [MiInitializeNewPfns](../67/MiInitializeNewPfns_function_00670E94.md) at `0x00671022`
- [MiPfnRangeIsZero](../67/MiPfnRangeIsZero_function_006735C0.md) at `0x0067381F`
- [MiMapMdlCommon](../67/MiMapMdlCommon_function_00674524.md) at `0x00674A84`
- [MiSetPageProtection](../67/MiSetPageProtection_function_00674BDC.md) at `0x00674C50`
- [MiUpdateLargePageSectionPfns](../67/MiUpdateLargePageSectionPfns_function_00678F8C.md) at `0x00678FDA`
- [MiInitializeSlowPte](../67/MiInitializeSlowPte_function_0067E1F8.md) at `0x0067E256`
- [MiInitializeDynamicBitmap](../67/MiInitializeDynamicBitmap_function_0067F5BC.md) at `0x0067F6B0`
- [MiEnableLargeSubsection](../68/MiEnableLargeSubsection_function_00680BC4.md) at `0x00680C10`
- [MiFillPageWithImageExtentContents](../68/MiFillPageWithImageExtentContents_function_00680E44.md) at `0x00680EF6`
- [MiFillPageWithImageExtentContents](../68/MiFillPageWithImageExtentContents_function_00680E44.md) at `0x00680FC1`
- [MmMapDriverTablePage](../68/MmMapDriverTablePage_function_00683EAC.md) at `0x0068409F`
- [MiDbgTranslatePhysicalAddress](../68/MiDbgTranslatePhysicalAddress_function_00685760.md) at `0x00685A84`
- [MmReadProcessPageTables](../68/MmReadProcessPageTables_function_006866C8.md) at `0x006866EB`
- [MiPrepareEnclaveMetadataPage](../68/MiPrepareEnclaveMetadataPage_function_00686EAC.md) at `0x00686FB6`
- [MiDemoteValidLargePageOneLevel](../68/MiDemoteValidLargePageOneLevel_function_0068A3F4.md) at `0x0068A622`
- [MiDemoteValidLargePageOneLevel](../68/MiDemoteValidLargePageOneLevel_function_0068A3F4.md) at `0x0068A707`
- [MiScrubLargePage](../69/MiScrubLargePage_function_006942E8.md) at `0x006945C5`
- [MiCopyMemoryPagefileData](../69/MiCopyMemoryPagefileData_function_00694C04.md) at `0x00694C83`
- [MiCopyMemoryPagefileData](../69/MiCopyMemoryPagefileData_function_00694C04.md) at `0x00694E42`
- [MiCopyMemoryPagefileData](../69/MiCopyMemoryPagefileData_function_00694C04.md) at `0x00694E97`
- [sub_006DC4D4](../6D/Unknown_function_006DC4D4.md) at `0x006DC619`
- [sub_006FA778](../6F/Unknown_function_006FA778.md) at `0x006FA78B`
- [sub_006FB3A8](../6F/Unknown_function_006FB3A8.md) at `0x006FB3BB`
- [MiProtectLargeKernelHalRange](../../page/7F/MiProtectLargeKernelHalRange_function_007F8D20.md) at `0x007F8E0F`
- [MmAllocateNonCachedMemory](../../page/7F/MmAllocateNonCachedMemory_function_007FBB60.md) at `0x007FBC8C`
- [MiInitializeShadowPageTable](../../page/80/MiInitializeShadowPageTable_function_0080778C.md) at `0x008078F2`
- [MiCreateHardwareEnclave](../../page/80/MiCreateHardwareEnclave_function_00808500.md) at `0x00808765`
- [MiCaptureSparsePages](../../page/80/MiCaptureSparsePages_function_0080BAF8.md) at `0x0080BB32`
- [MiValidateImagePfn](../../page/93/MiValidateImagePfn_function_0093EA08.md) at `0x0093EB43`
- [MiRelocateImagePfn](../../page/93/MiRelocateImagePfn_function_0093F2A8.md) at `0x0093F4C1`
- [MiCopyPagesIntoEnclave](../../page/A4/MiCopyPagesIntoEnclave_function_00A472AC.md) at `0x00A47802`
- [MiAllocateProcessShadow](../../page/A5/MiAllocateProcessShadow_function_00A5F1A0.md) at `0x00A5F256`
- [MiUpdateForkMaps](../../page/A7/MiUpdateForkMaps_function_00A7DAF8.md) at `0x00A7DC2B`
- [MmAllocateIndependentPagesEx](../../page/AA/MmAllocateIndependentPagesEx_function_00AA0CFC.md) at `0x00AA0DE0`
- [MmMapProtectedKernelPage](../../page/AB/MmMapProtectedKernelPage_function_00AB6690.md) at `0x00AB66AB`
- [sub_00B42A1A](../../page/B4/Unknown_function_00B42A1A.md) at `0x00B42A81`
- [MiInitializeSharedUserData](../../init/C5/MiInitializeSharedUserData_function_00C5F098.md) at `0x00C5F1A7`
- [MiInitializeDummyPages](../../init/C6/MiInitializeDummyPages_function_00C605CC.md) at `0x00C60707`
- [MiMapDummyPages](../../init/C6/MiMapDummyPages_function_00C60A58.md) at `0x00C60AC7`
- [MiProtectSharedUserPage](../../init/C6/MiProtectSharedUserPage_function_00C60F44.md) at `0x00C6103A`
- [MiProtectSharedUserPage](../../init/C6/MiProtectSharedUserPage_function_00C60F44.md) at `0x00C61101`
- [MxCopyPage](../../init/C6/MxCopyPage_function_00C631F4.md) at `0x00C63244`
- [MxMapVa](../../init/C6/MxMapVa_function_00C63EC4.md) at `0x00C63FB8`
- [MmInitializeImageViewExtensionCfg](../../init/C6/MmInitializeImageViewExtensionCfg_function_00C64FC4.md) at `0x00C65191`
- [MiFillGapPtes](../../init/C6/MiFillGapPtes_function_00C65AC0.md) at `0x00C65B21`
- [MiInitializeTbFlush](../../init/C6/MiInitializeTbFlush_function_00C6B01C.md) at `0x00C6B074`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002C5590  40 57                           push rdi
002C5592  48 83 EC 20                     sub rsp, 0x20
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall MiMakeValidPte(void)
{
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    return;
}
```

## 5. (Beta) C Style

```c
void MiMakeValidPte(void)
{
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    return;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002C5590&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002C5590[BB_002C5590]
```
