# HvcallInitiateHypercall

- RVA: `0x00313630`–`0x00313654` (길이 `36` bytes)
- VA: `0x0000000140313630`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000745AC`
- 디코드: `10`개 명령, `36/36` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **79**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [HvlpSlowSendSyntheticClusterIpiEx](../30/HvlpSlowSendSyntheticClusterIpiEx_function_003034E0.md) at `0x0030369A`
- [HvlRetargetDeviceInterrupt](../30/HvlRetargetDeviceInterrupt_function_003062A0.md) at `0x00306465`
- [HvlGetSparseGpaPagesAccessState](../30/HvlGetSparseGpaPagesAccessState_function_00306A78.md) at `0x00306BB2`
- [HvlDmaMapDeviceLogicalRange](../30/HvlDmaMapDeviceLogicalRange_function_003077D0.md) at `0x00307ABB`
- [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) at `0x0030F47F`
- [sub_00312CF6](Unknown_function_00312CF6.md) at `0x00312E33`
- [HvlSwitchVirtualAddressSpace](../3C/HvlSwitchVirtualAddressSpace_function_003C7C60.md) at `0x003C7C80`
- [HvlMapSparseGpaPages](../42/HvlMapSparseGpaPages_function_0042A160.md) at `0x0042A24C`
- [HvlGetGpaPagesAccessState](../42/HvlGetGpaPagesAccessState_function_0042A3D4.md) at `0x0042A545`
- [HvlpSlowFlushAddressSpaceTb](../44/HvlpSlowFlushAddressSpaceTb_function_004402C4.md) at `0x00440419`
- [HvlInvokeHypervisorDebugger](../44/HvlInvokeHypervisorDebugger_function_0044F32C.md) at `0x0044F368`
- [HvlMapGpaPages](../46/HvlMapGpaPages_function_00462934.md) at `0x00462A37`
- [HvlDmaMapDeviceSparsePages](../47/HvlDmaMapDeviceSparsePages_function_0047A390.md) at `0x0047A552`
- [HvlDmaUnmapDeviceSparsePages](../48/HvlDmaUnmapDeviceSparsePages_function_004844C0.md) at `0x004845DA`
- [HvlLpWriteMultipleMsr](../4A/HvlLpWriteMultipleMsr_function_004A35E0.md) at `0x004A36CF`
- [HvlpSlowFlushListTbEx](../4A/HvlpSlowFlushListTbEx_function_004AFCF8.md) at `0x004AFF99`
- [HvlLpReadMultipleMsr](../4B/HvlLpReadMultipleMsr_function_004BC3B0.md) at `0x004BC50C`
- [HvlpSetPowerProperty](../4C/HvlpSetPowerProperty_function_004C9124.md) at `0x004C923D`
- [HvlSetQpcBias](../4F/HvlSetQpcBias_function_004F8EF0.md) at `0x004F9037`
- [HvlQueryHypervisorTscAdjustment](../58/HvlQueryHypervisorTscAdjustment_function_0058424C.md) at `0x00584317`
- [HvlGetRootVpSharedPages](../58/HvlGetRootVpSharedPages_function_0058466C.md) at `0x00584700`
- [HvlQueryNumaDistance](../58/HvlQueryNumaDistance_function_00584A00.md) at `0x00584AA5`
- [HvlSetupPhysicalFaultNotificationQueue](../58/HvlSetupPhysicalFaultNotificationQueue_function_00584CE0.md) at `0x00584DB3`
- [HvlStartBootLogicalProcessors](../58/HvlStartBootLogicalProcessors_function_00584E18.md) at `0x0058516C`
- [HvlpDepositPages](../58/HvlpDepositPages_function_00585474.md) at `0x00585603`
- [HvlpGetLogicalProcessorProperty](../58/HvlpGetLogicalProcessorProperty_function_00585774.md) at `0x005857F6`
- [HvlpGetVpIndexFromApicId](../58/HvlpGetVpIndexFromApicId_function_00585880.md) at `0x00585912`
- [HvlpMapStatisticsPage](../58/HvlpMapStatisticsPage_function_00585B68.md) at `0x00585C01`
- [HvlpSetupSchedulerAssist](../58/HvlpSetupSchedulerAssist_function_005868F8.md) at `0x00586967`
- [HvlpStartLogicalProcessor](../58/HvlpStartLogicalProcessor_function_00586988.md) at `0x00586A5E`
- [HvlpStartVirtualProcessor](../58/HvlpStartVirtualProcessor_function_00586ADC.md) at `0x00586BA8`
- [HvlpUpdateLpcbIndex](../58/HvlpUpdateLpcbIndex_function_00586BD8.md) at `0x00586C4C`
- [HvlpWithdrawPages](../58/HvlpWithdrawPages_function_00586C90.md) at `0x00586D56`
- [HvlpWithdrawPages](../58/HvlpWithdrawPages_function_00586C90.md) at `0x00586DBC`
- [HvlpQueryHypervisorSchedulerType](../58/HvlpQueryHypervisorSchedulerType_function_00586FB4.md) at `0x0058704C`
- [HvlDmaGetDmaGuardEnabled](../58/HvlDmaGetDmaGuardEnabled_function_00587A50.md) at `0x00587AF3`
- [HvlDmaGetHybridPassthroughReservedRegions](../58/HvlDmaGetHybridPassthroughReservedRegions_function_00587B50.md) at `0x00587C02`
- [HvlEnterSleepState](../58/HvlEnterSleepState_function_00587E50.md) at `0x00587EAC`
- [HvlGetDeviceCapabilities](../58/HvlGetDeviceCapabilities_function_00587EF0.md) at `0x00587FBC`
- [HvlGetSystemPasidCapabilities](../58/HvlGetSystemPasidCapabilities_function_00588520.md) at `0x00588686`
- [HvlHvDebuggerPowerHandler](../58/HvlHvDebuggerPowerHandler_function_00588770.md) at `0x005887CB`
- [HvlLpReadCpuid](../58/HvlLpReadCpuid_function_00588900.md) at `0x00588994`
- [HvlLpWritebackInvalidate](../58/HvlLpWritebackInvalidate_function_00588A00.md) at `0x00588A60`
- [HvlMapDeviceInterrupt](../58/HvlMapDeviceInterrupt_function_00588A90.md) at `0x00588C68`
- [HvlNotifyAllProcessorsStarted](../58/HvlNotifyAllProcessorsStarted_function_00588CF4.md) at `0x00588D45`
- [HvlNotifyDebugDeviceAvailable](../58/HvlNotifyDebugDeviceAvailable_function_00588D80.md) at `0x00588DE4`
- [HvlNotifyHpetEnabled](../58/HvlNotifyHpetEnabled_function_00588E60.md) at `0x00588EBA`
- [HvlNotifyRootCrashdump](../58/HvlNotifyRootCrashdump_function_00588EF8.md) at `0x00588F5B`
- [HvlQueryAssociatedProcessors](../58/HvlQueryAssociatedProcessors_function_00589060.md) at `0x0058910F`
- [HvlRegisterDeviceId](../58/HvlRegisterDeviceId_function_005891C0.md) at `0x005892ED`
- [HvlSetHpetConfig](../58/HvlSetHpetConfig_function_00589560.md) at `0x0058960E`
- [HvlSetHpetConfig](../58/HvlSetHpetConfig_function_00589560.md) at `0x00589696`
- [HvlSetPartitionProperty](../58/HvlSetPartitionProperty_function_005896F8.md) at `0x0058975D`
- [HvlSetSystemMachineCheckProperty](../58/HvlSetSystemMachineCheckProperty_function_005898D0.md) at `0x00589930`
- [HvlSetSystemSleepProperty](../58/HvlSetSystemSleepProperty_function_00589970.md) at `0x005899E1`
- [HvlUnmapDeviceInterrupt](../58/HvlUnmapDeviceInterrupt_function_00589AE0.md) at `0x00589B4E`
- [HvlpDmaSlowFlushDeviceDomainVaList](../58/HvlpDmaSlowFlushDeviceDomainVaList_function_00589CC0.md) at `0x00589D8B`
- [HvlpSlowAcknowledgePageRequest](../58/HvlpSlowAcknowledgePageRequest_function_00589E20.md) at `0x00589EAA`
- [HvlpSlowFlushPasidAddressList](../58/HvlpSlowFlushPasidAddressList_function_00589EE4.md) at `0x00589F98`
- [HvlChangeIsolatedMemoryVisibility](../58/HvlChangeIsolatedMemoryVisibility_function_00589FD0.md) at `0x0058A0B0`
- [HvlMapDmaRanges](../58/HvlMapDmaRanges_function_0058A110.md) at `0x0058A19B`
- [HvlUnmapDmaRanges](../58/HvlUnmapDmaRanges_function_0058A210.md) at `0x0058A2B9`
- [HvlNotifyAcpiReenabled](../58/HvlNotifyAcpiReenabled_function_0058A64C.md) at `0x0058A69A`
- [HvlPrepareForHibernate](../58/HvlPrepareForHibernate_function_0058A6C4.md) at `0x0058A77D`
- [HvlRequestProcessorHalt](../58/HvlRequestProcessorHalt_function_0058A980.md) at `0x0058A9A1`
- [HvlWakeVirtualProcessors](../58/HvlWakeVirtualProcessors_function_0058AA80.md) at `0x0058ABFF`
- [HvlpInitializePowerStatistics](../58/HvlpInitializePowerStatistics_function_0058AC40.md) at `0x0058ACC4`
- [HvlCollectLivedump](../58/HvlCollectLivedump_function_0058B460.md) at `0x0058B597`
- [HvlpCheckTscSync](../58/HvlpCheckTscSync_function_0058C300.md) at `0x0058C39F`
- [HvlpLogGuestStateScrubbingStatus](../58/HvlpLogGuestStateScrubbingStatus_function_0058C48C.md) at `0x0058C52E`
- [HvlpLogIommuInitStatus](../58/HvlpLogIommuInitStatus_function_0058C724.md) at `0x0058C7C7`
- [HvlpDetermineEnlightenments](../58/HvlpDetermineEnlightenments_function_0058CC9C.md) at `0x0058D025`
- [HvlpQueryExtendedCapabilities](../58/HvlpQueryExtendedCapabilities_function_0058D2C8.md) at `0x0058D31F`
- [HvlpApplyIoCachePolicy](../58/HvlpApplyIoCachePolicy_function_0058D45C.md) at `0x0058D4C6`
- [HvlpInvokeGetPageListHypercall](../58/HvlpInvokeGetPageListHypercall_function_0058D7AC.md) at `0x0058D826`
- [HvlpSlowFlushAddressSpaceTbEx](../6A/HvlpSlowFlushAddressSpaceTbEx_function_006A7D48.md) at `0x006A7E23`
- [HvlNotifyPageHeat](../6A/HvlNotifyPageHeat_function_006A7E60.md) at `0x006A8006`
- [sub_006E0708](../6E/Unknown_function_006E0708.md) at `0x006E07AA`
- [HvlpCreateRootVirtualProcessor](../../page/71/HvlpCreateRootVirtualProcessor_function_00718280.md) at `0x0071832E`
- [HvlpLpCpuid](../../page/71/HvlpLpCpuid_function_007183B4.md) at `0x00718487`
- [HvlGetMicrocodeLatency](../../page/71/HvlGetMicrocodeLatency_function_007184E0.md) at `0x00718580`

### Static image references
- `0x0031363C` → RVA `0x00E0A740` (`.data`; read)
- `0x0031364B` → RVA `0x00FC6B14` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00313630  40 53                           push rbx
00313632  41 54                           push r12
00313634  41 56                           push r14
00313636  41 57                           push r15
00313638  48 83 EC 68                     sub rsp, 0x68
0031363C  48 8B 05 FD 70 AF 00            mov rax, qword ptr [rip + 0xaf70fd]
00313643  48 33 C4                        xor rax, rsp
00313646  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
0031364B  8B 05 C3 34 CB 00               mov eax, dword ptr [rip + 0xcb34c3]
00313651  0F 57 C0                        xorps xmm0, xmm0
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HvcallInitiateHypercall(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;

    v_rsp = (v_rsp) - (104);
    result = (*(unsigned __int64 *)(v_rip + 11497725)) ^ (v_rsp);
    v_stack_m48 = result;
    return (unsigned int)(*(unsigned int *)(v_rip + 13317315));
}
```

## 5. (Beta) C Style

```c
void HvcallInitiateHypercall(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m48;

    local_rsp = (local_rsp) - (104);
    result = (*(uint64_t *)(v_rip + 0xAF70FD)) ^ (local_rsp);
    v_stack_m48 = result;
    return (uint32_t)(*(uint32_t *)(v_rip + 0xCB34C3));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00313630&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00313630[BB_00313630]
```
