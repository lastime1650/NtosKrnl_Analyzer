# MiReleaseProcessorFlushList

- RVA: `0x00313C70`–`0x00313CB1` (길이 `65` bytes)
- VA: `0x0000000140313C70`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `13`개 명령, `65/65` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **61**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [MiHandleForkTransitionPte](../22/MiHandleForkTransitionPte_function_0022D34C.md) at `0x0022DB7D`
- [MiHandleForkTransitionPte](../22/MiHandleForkTransitionPte_function_0022D34C.md) at `0x0022DBFD`
- [MiCloneVads](../22/MiCloneVads_function_0022DC1C.md) at `0x0022E063`
- [MiCloneVads](../22/MiCloneVads_function_0022DC1C.md) at `0x0022E2B7`
- [MiBuildForkPte](../22/MiBuildForkPte_function_0022E32C.md) at `0x0022F18A`
- [MiBuildForkPte](../22/MiBuildForkPte_function_0022E32C.md) at `0x0022F26F`
- [MmSetAddressRangeModifiedEx](../23/MmSetAddressRangeModifiedEx_function_00236F20.md) at `0x002372D7`
- [MiAgeTrimListsTail](../23/MiAgeTrimListsTail_function_00239E90.md) at `0x00239F2B`
- [MiWalkVaRange](../24/MiWalkVaRange_function_00243BF0.md) at `0x00244A06`
- [MiWalkVaRange](../24/MiWalkVaRange_function_00243BF0.md) at `0x00244AB1`
- [MmProtectPool](../26/MmProtectPool_function_002697AC.md) at `0x00269A68`
- [MmProtectPool](../26/MmProtectPool_function_002697AC.md) at `0x00269E02`
- [MmProtectPool](../26/MmProtectPool_function_002697AC.md) at `0x00269F43`
- [MmProtectPool](../26/MmProtectPool_function_002697AC.md) at `0x00269FC7`
- [MiDecommitPagesTail](../27/MiDecommitPagesTail_function_002790FC.md) at `0x00279199`
- [sub_00293C9B](../29/Unknown_function_00293C9B.md) at `0x00293E85`
- [MiSetReadOnlyOnSectionView](../29/MiSetReadOnlyOnSectionView_function_00294538.md) at `0x0029474D`
- [MiSetReadOnlyOnSectionView](../29/MiSetReadOnlyOnSectionView_function_00294538.md) at `0x0029488C`
- [MiSetReadOnlyOnSectionView](../29/MiSetReadOnlyOnSectionView_function_00294538.md) at `0x00294959`
- [NtGetWriteWatch](../2A/NtGetWriteWatch_function_002A7CE0.md) at `0x002A842A`
- [NtGetWriteWatch](../2A/NtGetWriteWatch_function_002A7CE0.md) at `0x002A8527`
- [MiMoveDirtyBitsToPfns](../2A/MiMoveDirtyBitsToPfns_function_002A8624.md) at `0x002A89DF`
- [MiMoveDirtyBitsToPfns](../2A/MiMoveDirtyBitsToPfns_function_002A8624.md) at `0x002A8A3A`
- [MiReplaceRotateWithDemandZeroNoCopy](../2A/MiReplaceRotateWithDemandZeroNoCopy_function_002AAB04.md) at `0x002AAD0F`
- [MiDeleteNonPagedPoolTail](../2C/MiDeleteNonPagedPoolTail_function_002C20F0.md) at `0x002C218D`
- [sub_002C3A7C](../2C/Unknown_function_002C3A7C.md) at `0x002C3DCC`
- [sub_002C3A7C](../2C/Unknown_function_002C3A7C.md) at `0x002C4227`
- [sub_002C3A7C](../2C/Unknown_function_002C3A7C.md) at `0x002C42F8`
- [sub_002C3A7C](../2C/Unknown_function_002C3A7C.md) at `0x002C43C3`
- [sub_002C3A7C](../2C/Unknown_function_002C3A7C.md) at `0x002C44A7`
- [MiProtectPrivateMemory](../2C/MiProtectPrivateMemory_function_002C45B0.md) at `0x002C4ACF`
- [MiProtectPrivateMemory](../2C/MiProtectPrivateMemory_function_002C45B0.md) at `0x002C4B57`
- [MiProtectPrivateMemory](../2C/MiProtectPrivateMemory_function_002C45B0.md) at `0x002C4CDF`
- [MiProtectPrivateMemory](../2C/MiProtectPrivateMemory_function_002C45B0.md) at `0x002C4EED`
- [MiTrimSharedPageFromViews](../2E/MiTrimSharedPageFromViews_function_002E16F8.md) at `0x002E1A91`
- [MiTrimSharedPageFromViews](../2E/MiTrimSharedPageFromViews_function_002E16F8.md) at `0x002E2166`
- [MiFlushTbAsNeeded](MiFlushTbAsNeeded_function_00313730.md) at `0x00313980`
- [MiSharePages](MiSharePages_function_00315110.md) at `0x00315707`
- [MiSharePages](MiSharePages_function_00315110.md) at `0x003158F5`
- [MiFillSystemPtes](MiFillSystemPtes_function_00319850.md) at `0x0031A1AF`
- [MiCleanupLazyStampedPageTable](../32/MiCleanupLazyStampedPageTable_function_0032A43C.md) at `0x0032A513`
- [MiDeleteSystemPageTableTail](../36/MiDeleteSystemPageTableTail_function_00367830.md) at `0x0036786B`
- [MiDecommitHardwareEnclavePages](../36/MiDecommitHardwareEnclavePages_function_003688D4.md) at `0x00368B2A`
- [MiDecommitHardwareEnclavePages](../36/MiDecommitHardwareEnclavePages_function_003688D4.md) at `0x00368B51`
- [MiDecommitHardwareEnclavePages](../36/MiDecommitHardwareEnclavePages_function_003688D4.md) at `0x00368C2C`
- [MiLockCode](../36/MiLockCode_function_0036F91C.md) at `0x00370089`
- [MiLockCode](../36/MiLockCode_function_0036F91C.md) at `0x0037009D`
- [MiLockCode](../36/MiLockCode_function_0036F91C.md) at `0x003700E3`
- [MiLockCode](../36/MiLockCode_function_0036F91C.md) at `0x0037010D`
- [MiLockCode](../36/MiLockCode_function_0036F91C.md) at `0x00370151`
- [MiLockCode](../36/MiLockCode_function_0036F91C.md) at `0x00370165`
- [MiFlushValidPteFromTb](../37/MiFlushValidPteFromTb_function_00376878.md) at `0x003768E4`
- [MiSetSystemCodeProtection](../38/MiSetSystemCodeProtection_function_00384420.md) at `0x003846EA`
- [MiSetSystemCodeProtection](../38/MiSetSystemCodeProtection_function_00384420.md) at `0x00384B53`
- [MiSetSystemCodeProtection](../38/MiSetSystemCodeProtection_function_00384420.md) at `0x00384B68`
- [MiUnmapMdlCommon](../3E/MiUnmapMdlCommon_function_003E7DF0.md) at `0x003E81BA`
- [MiUnmapContiguousMemory](../3F/MiUnmapContiguousMemory_function_003F7908.md) at `0x003F7AC6`
- [MiConsumeSystemCacheTbFlushNeededView](../41/MiConsumeSystemCacheTbFlushNeededView_function_004193B4.md) at `0x00419567`
- [MiUpdateOldWorkingSetPagesTail](../42/MiUpdateOldWorkingSetPagesTail_function_00428C00.md) at `0x00428C75`
- [sub_00428D7A](../42/Unknown_function_00428D7A.md) at `0x00428DAB`
- [MiDeprioritizeVirtualAddresses](../42/MiDeprioritizeVirtualAddresses_function_0042AD1C.md) at `0x0042AFF3`
- [MiDeprioritizeVirtualAddresses](../42/MiDeprioritizeVirtualAddresses_function_0042AD1C.md) at `0x0042B031`
- [sub_0044565B](../44/Unknown_function_0044565B.md) at `0x004457DA`
- [MiCreateSystemPageTable](../45/MiCreateSystemPageTable_function_004518D0.md) at `0x00451BFE`
- [MiClearPteAccessedBitRange](../45/MiClearPteAccessedBitRange_function_004520B8.md) at `0x004521A5`
- [MiEmptyWorkingSetTail](../46/MiEmptyWorkingSetTail_function_0046CC90.md) at `0x0046CCC5`
- [MiCreateSystemPageTableTail](../47/MiCreateSystemPageTableTail_function_0047F890.md) at `0x0047F8B7`
- [MiConvertAndFlushWsleVas](../49/MiConvertAndFlushWsleVas_function_00492CB4.md) at `0x00492E4C`
- [MiRevokeExecuteTail](../49/MiRevokeExecuteTail_function_004949A0.md) at `0x004949C3`
- [MiSetPagingOfDriver](../4A/MiSetPagingOfDriver_function_004A76C4.md) at `0x004A7965`
- [MiSetPagingOfDriver](../4A/MiSetPagingOfDriver_function_004A76C4.md) at `0x004A799F`
- [MiSetPagingOfDriver](../4A/MiSetPagingOfDriver_function_004A76C4.md) at `0x004A79BC`
- [MiUnmapKernelScp](../4A/MiUnmapKernelScp_function_004A82E8.md) at `0x004A84BF`
- [MiUnmapKernelScp](../4A/MiUnmapKernelScp_function_004A82E8.md) at `0x004A852A`
- [MiAdjustSecureDriverStateForIatCapture](../4B/MiAdjustSecureDriverStateForIatCapture_function_004BE864.md) at `0x004BEA9C`
- [MiProtectAweRegion](../4C/MiProtectAweRegion_function_004CE62C.md) at `0x004CE994`
- [MiProtectAweRegion](../4C/MiProtectAweRegion_function_004CE62C.md) at `0x004CEDBC`
- [MiFinishPteChangesInPageTable](../4E/MiFinishPteChangesInPageTable_function_004EE660.md) at `0x004EE687`
- [NtUnlockVirtualMemory](../4E/NtUnlockVirtualMemory_function_004EE890.md) at `0x004EEA32`
- [NtUnlockVirtualMemory](../4E/NtUnlockVirtualMemory_function_004EE890.md) at `0x004EEB42`
- [NtUnlockVirtualMemory](../4E/NtUnlockVirtualMemory_function_004EE890.md) at `0x004EECDB`
- [NtUnlockVirtualMemory](../4E/NtUnlockVirtualMemory_function_004EE890.md) at `0x004EED27`
- [MiPageBootRegistry](../66/MiPageBootRegistry_function_0066E82C.md) at `0x0066E99F`
- [MiPageBootRegistry](../66/MiPageBootRegistry_function_0066E82C.md) at `0x0066EABC`
- [MiSetPageProtection](../67/MiSetPageProtection_function_00674BDC.md) at `0x00674DFF`
- [MiClearDriverTablePtes](../68/MiClearDriverTablePtes_function_00683024.md) at `0x006830F5`
- [MiClearDriverTablePtes](../68/MiClearDriverTablePtes_function_00683024.md) at `0x006833ED`
- [MiFlushEnclaveTb](../68/MiFlushEnclaveTb_function_00686E10.md) at `0x00686E90`
- [MiBuildPhysicalPageFreeChain](../68/MiBuildPhysicalPageFreeChain_function_00687C80.md) at `0x00687E84`
- [MiBuildPhysicalPageFreeChain](../68/MiBuildPhysicalPageFreeChain_function_00687C80.md) at `0x00687F33`
- [MiZeroAndFlushAweLazyPtes](../68/MiZeroAndFlushAweLazyPtes_function_00689B1C.md) at `0x00689C50`
- [MiClearSystemAccessBits](../68/MiClearSystemAccessBits_function_0068A2A0.md) at `0x0068A3C6`
- [MiDemoteValidLargePageOneLevel](../68/MiDemoteValidLargePageOneLevel_function_0068A3F4.md) at `0x0068A937`
- [MiScrubLargeMappedPage](../69/MiScrubLargeMappedPage_function_00693E2C.md) at `0x006940E2`
- [sub_006D9212](../6D/Unknown_function_006D9212.md) at `0x006D9461`
- [sub_006D9212](../6D/Unknown_function_006D9212.md) at `0x006D9480`
- [sub_006DB77C](../6D/Unknown_function_006DB77C.md) at `0x006DB879`
- [sub_006E362E](../6E/Unknown_function_006E362E.md) at `0x006E369C`
- [sub_006E362E](../6E/Unknown_function_006E362E.md) at `0x006E37DB`
- [sub_006E3CBA](../6E/Unknown_function_006E3CBA.md) at `0x006E3CC2`
- [MiProtectLargeKernelHalRange](../../page/7F/MiProtectLargeKernelHalRange_function_007F8D20.md) at `0x007F8DAE`
- [MiProtectLargeKernelHalRange](../../page/7F/MiProtectLargeKernelHalRange_function_007F8D20.md) at `0x007F8E75`
- [MiMarkBootKernelStack](../../init/C6/MiMarkBootKernelStack_function_00C68244.md) at `0x00C682A7`
- [MiMarkBootKernelStack](../../init/C6/MiMarkBootKernelStack_function_00C68244.md) at `0x00C683E2`
- [MiFreeBootDriverPages](../../init/C7/MiFreeBootDriverPages_function_00C7695C.md) at `0x00C76BB1`

### Static image references
- `0x00313CA8` → RVA `0x0100F4C0` (`INITDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00313C70  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
00313C79  48 8B 80 38 88 00 00            mov rax, qword ptr [rax + 0x8838]
00313C80  48 85 C0                        test rax, rax
00313C83  74 23                           je 0x140313ca8
00313C85  8B 88 5C 01 00 00               mov ecx, dword ptr [rax + 0x15c]
00313C8B  FF C9                           dec ecx
00313C8D  48 69 D1 78 50 00 00            imul rdx, rcx, 0x5078
00313C94  48 C7 84 02 F0 51 00 00 00 00 00 00  mov qword ptr [rdx + rax + 0x51f0], 0
00313CA0  FF 88 5C 01 00 00               dec dword ptr [rax + 0x15c]
00313CA6  C3                              ret
00313CA7  CC                              int3
00313CA8  48 8D 05 11 B8 CF 00            lea rax, [rip + 0xcfb811]
00313CAF  EB D4                           jmp 0x140313c85
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiReleaseProcessorFlushList(void)
{
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34872) == 0) goto loc_00313CA8;
loc_00313C85:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34872) + 348))) - 1);
    a2 = (a2) * (a1);
    *(unsigned __int64 *)(a2 + *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34872) * 1 + 20976) = 0;
    return *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34872);
loc_00313CA8:
    goto loc_00313C85;
}
```

## 5. (Beta) C Style

```c
void MiReleaseProcessorFlushList(void)
{
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8838) == 0) goto loc_00313CA8;
loc_00313C85:
    a1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8838) + 0x15C))) - 1);
    a2 = (a2) * (a1);
    *(uint64_t *)(a2 + *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8838) * 1 + 0x51F0) = 0;
    return *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8838);
loc_00313CA8:
    goto loc_00313C85;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00313C70&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00313C70[BB_00313C70]
  bb_00313C85[BB_00313C85]
  bb_00313CA7[BB_00313CA7]
  bb_00313CA8[BB_00313CA8]
  bb_00313C70 -->|branch| bb_00313CA8
  bb_00313C70 -->|fallthrough| bb_00313C85
  bb_00313CA7 -->|flow| bb_00313CA8
  bb_00313CA8 -->|branch| bb_00313C85
```
