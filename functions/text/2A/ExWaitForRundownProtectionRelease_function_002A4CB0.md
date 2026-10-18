# ExWaitForRundownProtectionRelease

- RVA: `0x002A4CB0`–`0x002A4CD6` (길이 `38` bytes)
- VA: `0x00000001402A4CB0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005F758`
- 디코드: `12`개 명령, `38/38` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **64**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x002A4CCF` → [ExfWaitForRundownProtectionRelease](ExfWaitForRundownProtectionRelease_function_002A4CDC.md) (function, `0x002A4CDC`)

### Direct callers
- [CmpTryToRundownHive](CmpTryToRundownHive_function_002A4A60.md) at `0x002A4ACB`
- [NtShutdownWorkerFactory](NtShutdownWorkerFactory_function_002A4E60.md) at `0x002A4F02`
- [PfSnDeactivateTrace](PfSnDeactivateTrace_function_002A50CC.md) at `0x002A515F`
- [IoStopDiskIoAttributionForContext](IoStopDiskIoAttributionForContext_function_002A5614.md) at `0x002A5658`
- [sub_00342A4A](../34/Unknown_function_00342A4A.md) at `0x00342AC9`
- [KiRundownAvailableCpusWorkItem](../43/KiRundownAvailableCpusWorkItem_function_0043FA78.md) at `0x0043FA85`
- [MiModifiedPageWriter](../47/MiModifiedPageWriter_function_0047E5F0.md) at `0x0047EAB9`
- [HalpIommuCreateDevice](../54/HalpIommuCreateDevice_function_0054ED60.md) at `0x0054F1B2`
- [IommuDeleteAtsDevice](../56/IommuDeleteAtsDevice_function_00564D30.md) at `0x00564D6C`
- [IommuDevicePowerChange](../56/IommuDevicePowerChange_function_00564DB0.md) at `0x00564E05`
- [IommupMapDeviceInternal](../56/IommupMapDeviceInternal_function_00566478.md) at `0x005666AF`
- [IommupUnmapDeviceInternal](../56/IommupUnmapDeviceInternal_function_005667D8.md) at `0x00566963`
- [BgkpDisableConsole](../59/BgkpDisableConsole_function_005911EC.md) at `0x005911F7`
- [PfFbBufferListShutdown](../5C/PfFbBufferListShutdown_function_005CE2CC.md) at `0x005CE2D0`
- [DbgpRemoveDebugPrintCallback](../5E/DbgpRemoveDebugPrintCallback_function_005E59E4.md) at `0x005E5A73`
- [SMKM_STORE_MGR&lt;SM_TRAITS&gt;::SmCompressManagerCleanup](../60/SMKM_STORE_MGR_SM_TRAITS_SmCompressManagerCleanup_function_0060C330.md) at `0x0060C398`
- [VfVolatileClearDifRuleClass](../61/VfVolatileClearDifRuleClass_function_006168E0.md) at `0x00616916`
- [MiDrainCrossPartitionUsage](../69/MiDrainCrossPartitionUsage_function_00690984.md) at `0x00690B0C`
- [CmpWorkItemRundown](../../page/70/CmpWorkItemRundown_function_00705820.md) at `0x0070582D`
- [DbgkLkmdUnregisterCallback](../../page/71/DbgkLkmdUnregisterCallback_function_00711660.md) at `0x007116D2`
- [ObUnRegisterCallbacks](../../page/74/ObUnRegisterCallbacks_function_0074F260.md) at `0x0074F28B`
- [PfpRpShutdown](../../page/75/PfpRpShutdown_function_00751C70.md) at `0x00751C99`
- [PoUnregisterCoalescingCallback](../../page/75/PoUnregisterCoalescingCallback_function_0075C000.md) at `0x0075C05E`
- [PsUnregisterSyscallProvider](../../page/77/PsUnregisterSyscallProvider_function_0077E330.md) at `0x0077E341`
- [SmDeletePartition](../../page/7A/SmDeletePartition_function_007A59C0.md) at `0x007A59F0`
- [SmcProcessCreateRequest](../../page/7A/SmcProcessCreateRequest_function_007A764C.md) at `0x007A7809`
- [SmHwAcceleratorCleanup](../../page/7A/SmHwAcceleratorCleanup_function_007AA3BC.md) at `0x007AA3CD`
- [SmHwAcceleratorPartitionCtxCleanup](../../page/7A/SmHwAcceleratorPartitionCtxCleanup_function_007AB2D8.md) at `0x007AB309`
- [SmcCacheManagerInitialize](../../page/7A/SmcCacheManagerInitialize_function_007AB8CC.md) at `0x007AB8FB`
- [SmcCacheRemove](../../page/7A/SmcCacheRemove_function_007ABB68.md) at `0x007ABBF4`
- [SmcStoreDelete](../../page/7A/SmcStoreDelete_function_007AC214.md) at `0x007AC2F0`
- [VmCleanProcessAddressSpace](../../page/7A/VmCleanProcessAddressSpace_function_007ACD38.md) at `0x007ACDA0`
- [EtwpCoverageSamplerStop](../../page/7C/EtwpCoverageSamplerStop_function_007C2564.md) at `0x007C263E`
- [ExStartStopWorkQueueProvider](../../page/7C/ExStartStopWorkQueueProvider_function_007CF59C.md) at `0x007CF757`
- [ExRegisterHost](../../page/7D/ExRegisterHost_function_007D06CC.md) at `0x007D073E`
- [ExUnregisterExtension](../../page/7D/ExUnregisterExtension_function_007D0870.md) at `0x007D0911`
- [ExpPrivatePoolDestroy](../../page/7D/ExpPrivatePoolDestroy_function_007D61C4.md) at `0x007D61D5`
- [CmpWaitForHiveLoadUnloadRundownRelease](../../page/7F/CmpWaitForHiveLoadUnloadRundownRelease_function_007F133C.md) at `0x007F1347`
- [CmpWaitForShutdownRundownRelease](../../page/7F/CmpWaitForShutdownRundownRelease_function_007F1364.md) at `0x007F136F`
- [MiInitializePartition](../../page/7F/MiInitializePartition_function_007FD3E8.md) at `0x007FD79C`
- [PspExitThread](../../page/90/PspExitThread_function_00905F60.md) at `0x0090603F`
- [PspRundownSingleProcess](../../page/90/PspRundownSingleProcess_function_00906D50.md) at `0x00906DB8`
- [ExpWnfDeleteSubscription](../../page/90/ExpWnfDeleteSubscription_function_00908528.md) at `0x0090877C`
- [ExpWnfDeleteNameInstance](../../page/90/ExpWnfDeleteNameInstance_function_009088C8.md) at `0x00908B84`
- [PspIoRateEntryInitialize](../../page/91/PspIoRateEntryInitialize_function_00917734.md) at `0x00917759`
- [PfSnPowerBoost](../../page/93/PfSnPowerBoost_function_00939C14.md) at `0x00939CD6`
- [CmpPerformUnloadKey](../../page/9A/CmpPerformUnloadKey_function_009AFA28.md) at `0x009AFC82`
- [PspIoRateEntryDeactivate](../../page/9F/PspIoRateEntryDeactivate_function_009F7BD4.md) at `0x009F7BE1`
- [IoDiskIoAttributionAllocate](../../page/9F/IoDiskIoAttributionAllocate_function_009F7F6C.md) at `0x009F7FF6`
- [SmKmStoreDelete](../../page/A6/SmKmStoreDelete_function_00A6D7D0.md) at `0x00A6D8A9`
- [ExpWnfFreeScopeInstance](../../page/A7/ExpWnfFreeScopeInstance_function_00A77614.md) at `0x00A77629`
- [ObDestroyHandleRevocationBlock](../../page/A9/ObDestroyHandleRevocationBlock_function_00A924B8.md) at `0x00A9255D`
- [PsRemoveCreateThreadNotifyRoutine](../../page/AA/PsRemoveCreateThreadNotifyRoutine_function_00AA3870.md) at `0x00AA390F`
- [PsRemoveLoadImageNotifyRoutine](../../page/AC/PsRemoveLoadImageNotifyRoutine_function_00AC30F0.md) at `0x00AC3187`
- [HalpUnregisterPmuNotification](../../page/AC/HalpUnregisterPmuNotification_function_00ACAB7C.md) at `0x00ACACC9`
- [HalpUnregisterPmuNotification](../../page/AC/HalpUnregisterPmuNotification_function_00ACAB7C.md) at `0x00ACADD8`
- [ExWaitForCallBacks](../../page/AC/ExWaitForCallBacks_function_00ACFA04.md) at `0x00ACFA08`
- [sub_00B3C780](../../page/B3/Unknown_function_00B3C780.md) at `0x00B3C798`
- [sub_00B49F04](../../page/B4/Unknown_function_00B49F04.md) at `0x00B49F4F`
- [IoShutdownSystem](../../pagelk/B6/IoShutdownSystem_function_00B63B8C.md) at `0x00B63D18`
- [PfTAccessTracingCleanup](../../pagelk/B6/PfTAccessTracingCleanup_function_00B6B8AC.md) at `0x00B6B90C`
- [MiDeleteAllHardwareEnclaves](../../pagelk/B7/MiDeleteAllHardwareEnclaves_function_00B74CAC.md) at `0x00B74CF6`
- [ViPtPluginUnload](../../pagevrfy/B9/ViPtPluginUnload_function_00B9CA40.md) at `0x00B9CA70`
- [PfInitializeSuperfetch](../../init/C3/PfInitializeSuperfetch_function_00C3CACC.md) at `0x00C3CB7B`
- [PfInitializeSuperfetch](../../init/C3/PfInitializeSuperfetch_function_00C3CACC.md) at `0x00C3CBBC`
- [EtwpInitializeCoverageSampler](../../init/C4/EtwpInitializeCoverageSampler_function_00C4F5D4.md) at `0x00C4F623`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002A4CB0  48 83 EC 28                     sub rsp, 0x28
002A4CB4  BA 01 00 00 00                  mov edx, 1
002A4CB9  33 C0                           xor eax, eax
002A4CBB  F0 48 0F B1 11                  lock cmpxchg qword ptr [rcx], rdx
002A4CC0  48 83 F8 02                     cmp rax, 2
002A4CC4  73 06                           jae 0x1402a4ccc
002A4CC6  48 83 C4 28                     add rsp, 0x28
002A4CCA  C3                              ret
002A4CCB  CC                              int3
002A4CCC  48 8B D0                        mov rdx, rax
002A4CCF  E8 08 00 00 00                  call 0x1402a4cdc
002A4CD4  EB F0                           jmp 0x1402a4cc6
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExWaitForRundownProtectionRelease(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = 0;
    if (0 >= 2) goto loc_002A4CCC;
loc_002A4CC6:
    v_rsp = (v_rsp) + (40);
    return result;
loc_002A4CCC:
    result = ExfWaitForRundownProtectionRelease(a1, 0, a3, a4);
    goto loc_002A4CC6;
}
```

## 5. (Beta) C Style

```c
int64_t ExWaitForRundownProtectionRelease(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = 0;
    if (0 >= 2) goto loc_002A4CCC;
loc_002A4CC6:
    local_rsp = (local_rsp) + (40);
    return result;
loc_002A4CCC:
    result = ExfWaitForRundownProtectionRelease(Arg1, 0, a3, a4);
    goto loc_002A4CC6;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002A4CB0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002A4CB0[BB_002A4CB0]
  bb_002A4CC6[BB_002A4CC6]
  bb_002A4CCB[BB_002A4CCB]
  bb_002A4CCC[BB_002A4CCC]
  bb_002A4CB0 -->|branch| bb_002A4CCC
  bb_002A4CB0 -->|fallthrough| bb_002A4CC6
  bb_002A4CCB -->|flow| bb_002A4CCC
  bb_002A4CCC -->|branch| bb_002A4CC6
```
