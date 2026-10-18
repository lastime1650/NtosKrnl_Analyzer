# MiInsertTbFlushEntry

- RVA: `0x00293670`–`0x002936A3` (길이 `51` bytes)
- VA: `0x0000000140293670`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00067688`
- 디코드: `15`개 명령, `51/51` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **70**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [MmProtectMdlSystemAddress](../22/MmProtectMdlSystemAddress_function_00227B50.md) at `0x00227CC3`
- [MiCombineWithExisting](../22/MiCombineWithExisting_function_0022B4B8.md) at `0x0022B796`
- [MiCombineInitialInstance](../22/MiCombineInitialInstance_function_0022BC0C.md) at `0x0022C30D`
- [MiBuildForkPte](../22/MiBuildForkPte_function_0022E32C.md) at `0x0022E6A4`
- [sub_00237DE0](../23/Unknown_function_00237DE0.md) at `0x00238471`
- [MiDecommitAddToList](../24/MiDecommitAddToList_function_00242264.md) at `0x002425B3`
- [MmProtectPool](../26/MmProtectPool_function_002697AC.md) at `0x00269A1D`
- [MmProtectPool](../26/MmProtectPool_function_002697AC.md) at `0x00269C7B`
- [MiClearPteAccessed](MiClearPteAccessed_function_00290630.md) at `0x00290755`
- [MiTrimPteWorker](MiTrimPteWorker_function_00292E2C.md) at `0x00292ED1`
- [MiTrimPte](MiTrimPte_function_00292F30.md) at `0x00293127`
- [MiOutPageSingleKernelStack](../2A/MiOutPageSingleKernelStack_function_002A1790.md) at `0x002A1AFF`
- [MiReplaceRotateWithDemandZeroNoCopy](../2A/MiReplaceRotateWithDemandZeroNoCopy_function_002AAB04.md) at `0x002AAC87`
- [MiReplaceRotateWithDemandZeroNoCopy](../2A/MiReplaceRotateWithDemandZeroNoCopy_function_002AAB04.md) at `0x002AACAB`
- [sub_002C1B88](../2C/Unknown_function_002C1B88.md) at `0x002C1CE0`
- [MiInsertRecursiveTbFlushEntries](../2C/MiInsertRecursiveTbFlushEntries_function_002C1F38.md) at `0x002C1F88`
- [sub_002C3A7C](../2C/Unknown_function_002C3A7C.md) at `0x002C41C7`
- [MiRevertValidPte](../2C/MiRevertValidPte_function_002C5160.md) at `0x002C5436`
- [MiDeleteRotateVa](../2C/MiDeleteRotateVa_function_002C79D4.md) at `0x002C7A81`
- [MiTrimSharedPageFromViews](../2E/MiTrimSharedPageFromViews_function_002E16F8.md) at `0x002E1F64`
- [MiTrimSharedPageFromViews](../2E/MiTrimSharedPageFromViews_function_002E16F8.md) at `0x002E2020`
- [MiFlushTbAsNeeded](../31/MiFlushTbAsNeeded_function_00313730.md) at `0x00313A7E`
- [MiSharePages](../31/MiSharePages_function_00315110.md) at `0x003158DE`
- [MiSharePages](../31/MiSharePages_function_00315110.md) at `0x00315999`
- [MiReservePtes](../31/MiReservePtes_function_00318D20.md) at `0x003190FA`
- [MiFillSystemPtes](../31/MiFillSystemPtes_function_00319850.md) at `0x0031A1A2`
- [MiCleanupLazyStampedPageTable](../32/MiCleanupLazyStampedPageTable_function_0032A43C.md) at `0x0032A62A`
- [MiDecommitHardwareEnclavePages](../36/MiDecommitHardwareEnclavePages_function_003688D4.md) at `0x00368C1A`
- [MiInsertLargeTbFlushEntry](../37/MiInsertLargeTbFlushEntry_function_0037827C.md) at `0x003782CB`
- [MiSetSystemCodeProtection](../38/MiSetSystemCodeProtection_function_00384420.md) at `0x00384767`
- [MiUnmapMdlCommon](../3E/MiUnmapMdlCommon_function_003E7DF0.md) at `0x003E80D2`
- [MiUnmapContiguousMemory](../3F/MiUnmapContiguousMemory_function_003F7908.md) at `0x003F7BDA`
- [MiConsumeSystemCacheTbFlushNeededView](../41/MiConsumeSystemCacheTbFlushNeededView_function_004193B4.md) at `0x004194CE`
- [MiQueryVpabAccessedState](../42/MiQueryVpabAccessedState_function_00428E70.md) at `0x00428FBD`
- [MiDeprioritizeVirtualAddresses](../42/MiDeprioritizeVirtualAddresses_function_0042AD1C.md) at `0x0042AFBE`
- [sub_00436E60](../43/Unknown_function_00436E60.md) at `0x00436EA0`
- [sub_0044565B](../44/Unknown_function_0044565B.md) at `0x00445798`
- [MiClearPteAccessedBitRange](../45/MiClearPteAccessedBitRange_function_004520B8.md) at `0x00452198`
- [MiDeleteSystemPageTable](../49/MiDeleteSystemPageTable_function_004916B0.md) at `0x004917C3`
- [MiConvertAndFlushWsleVas](../49/MiConvertAndFlushWsleVas_function_00492CB4.md) at `0x00492E1C`
- [MiMakeVaRangeNoAccess](../4A/MiMakeVaRangeNoAccess_function_004A3CE0.md) at `0x004A3E26`
- [MiMapMemoryDumpMdl](../4A/MiMapMemoryDumpMdl_function_004A619C.md) at `0x004A6375`
- [MiSetPagingOfDriver](../4A/MiSetPagingOfDriver_function_004A76C4.md) at `0x004A78BB`
- [MiUnmapKernelScp](../4A/MiUnmapKernelScp_function_004A82E8.md) at `0x004A8445`
- [MiAdjustSecureDriverStateForIatCapture](../4B/MiAdjustSecureDriverStateForIatCapture_function_004BE864.md) at `0x004BEA24`
- [MiSwitchToTransition](../4C/MiSwitchToTransition_function_004C0F5C.md) at `0x004C1693`
- [MiReadyReservedView](../4C/MiReadyReservedView_function_004CC0D8.md) at `0x004CC194`
- [MiProtectAweRegion](../4C/MiProtectAweRegion_function_004CE62C.md) at `0x004CEC8D`
- [MiMapMdlWithLargePages](../4D/MiMapMdlWithLargePages_function_004D10B8.md) at `0x004D12FB`
- [MiProtectEnclavePages](../4D/MiProtectEnclavePages_function_004D5528.md) at `0x004D59D2`
- [NtUnlockVirtualMemory](../4E/NtUnlockVirtualMemory_function_004EE890.md) at `0x004EECB9`
- [MiDecommitAddTbFlushEntries](../4F/MiDecommitAddTbFlushEntries_function_004FB798.md) at `0x004FB820`
- [MiPageBootRegistry](../66/MiPageBootRegistry_function_0066E82C.md) at `0x0066EA75`
- [MiSetPageProtection](../67/MiSetPageProtection_function_00674BDC.md) at `0x00674DDB`
- [MiStackTheftFreezeProcessors](../67/MiStackTheftFreezeProcessors_function_0067B274.md) at `0x0067B382`
- [MiClearDriverTablePtes](../68/MiClearDriverTablePtes_function_00683024.md) at `0x006831BA`
- [MiFlushEnclaveTb](../68/MiFlushEnclaveTb_function_00686E10.md) at `0x00686E7E`
- [MiInsertAweFlushList](../68/MiInsertAweFlushList_function_00688FEC.md) at `0x00689040`
- [MiUnmapLegacyAwePage](../68/MiUnmapLegacyAwePage_function_0068993C.md) at `0x00689A03`
- [MiClearSystemAccessBits](../68/MiClearSystemAccessBits_function_0068A2A0.md) at `0x0068A396`
- [MiScrubLargeMappedPage](../69/MiScrubLargeMappedPage_function_00693E2C.md) at `0x006940D5`
- [MiCalibrateTbFlush](../69/MiCalibrateTbFlush_function_006955EC.md) at `0x00695699`
- [sub_006D9212](../6D/Unknown_function_006D9212.md) at `0x006D943D`
- [sub_006DB1E0](../6D/Unknown_function_006DB1E0.md) at `0x006DB236`
- [sub_006DB6A6](../6D/Unknown_function_006DB6A6.md) at `0x006DB6EF`
- [sub_006DB77C](../6D/Unknown_function_006DB77C.md) at `0x006DB857`
- [sub_006E362E](../6E/Unknown_function_006E362E.md) at `0x006E368F`
- [sub_006E3CBA](../6E/Unknown_function_006E3CBA.md) at `0x006E3D36`
- [sub_006F25AE](../6F/Unknown_function_006F25AE.md) at `0x006F25B8`
- [sub_006F91FE](../6F/Unknown_function_006F91FE.md) at `0x006F928D`
- [MmDeleteShadowMapping](../../page/80/MmDeleteShadowMapping_function_00807D00.md) at `0x00807DBE`
- [MiEliminateZeroPages](../../page/8C/MiEliminateZeroPages_function_008CF1A0.md) at `0x008CF29B`
- [MmUnmapProtectedKernelPageRange](../../page/AA/MmUnmapProtectedKernelPageRange_function_00AA36DC.md) at `0x00AA377C`
- [MiMarkBootKernelStack](../../init/C6/MiMarkBootKernelStack_function_00C68244.md) at `0x00C683BE`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x0029369D` → [sub_00293812](Unknown_function_00293812.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00293670  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
00293675  48 89 6C 24 18                  mov qword ptr [rsp + 0x18], rbp
0029367A  56                              push rsi
0029367B  57                              push rdi
0029367C  41 56                           push r14
0029367E  48 83 EC 20                     sub rsp, 0x20
00293682  48 8B D9                        mov rbx, rcx
00293685  41 8B F1                        mov esi, r9d
00293688  BF 00 10 00 00                  mov edi, 0x1000
0029368D  49 8B E8                        mov rbp, r8
00293690  4C 8B F2                        mov r14, rdx
00293693  8D 0C F6                        lea ecx, [rsi + rsi*8]
00293696  48 D3 E7                        shl rdi, cl
00293699  83 7B 08 01                     cmp dword ptr [rbx + 8], 1
0029369D  0F 85 6F 01 00 00               jne 0x140293812
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall MiInsertTbFlushEntry(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;

    v_stack_p10 = v_rbx;
    v_stack_p18 = v_rbp;
    v_rsp = (v_rsp) - (32);
    v_rdi = ((unsigned int)(0x1000ULL)) << ((unsigned __int8)((unsigned int)(a4) + (unsigned int)(a4) * 8));
}
```

## 5. (Beta) C Style

```c
void MiInsertTbFlushEntry(void *Arg1, int64_t Arg2, int64_t Arg3, void *Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;

    v_stack_p10 = local_rbx;
    v_stack_p18 = local_rbp;
    local_rsp = (local_rsp) - (32);
    local_rdi = ((uint32_t)(0x1000ULL)) << ((uint8_t)((uint32_t)(Arg4) + (uint32_t)(Arg4) * 8));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `32` | `R` |
| `Arg4` | `+ 0x0 + rsi*8` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00293670&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00293670[BB_00293670]
```
