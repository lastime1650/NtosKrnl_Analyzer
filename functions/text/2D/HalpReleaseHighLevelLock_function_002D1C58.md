# HalpReleaseHighLevelLock

- RVA: `0x002D1C58`–`0x002D1C85` (길이 `45` bytes)
- VA: `0x00000001402D1C58`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `14`개 명령, `45/45` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **54**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x002D1C61` → [KxReleaseSpinLock](../20/KxReleaseSpinLock_function_00206670.md) (function, `0x00206670`)
- `0x002D1C75` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)

### Direct callers
- [HalpQueryProfileSourceList](HalpQueryProfileSourceList_function_002D1370.md) at `0x002D1489`
- [IvtFlushDomainTb](IvtFlushDomainTb_function_002D1BD0.md) at `0x002D1C35`
- [HalpInterruptApplyOverrides](HalpInterruptApplyOverrides_function_002D2CE0.md) at `0x002D2D5D`
- [HalpInterruptSetDestination](HalpInterruptSetDestination_function_002D3100.md) at `0x002D31E8`
- [HalpInterruptSetRemappedDestinationHv](HalpInterruptSetRemappedDestinationHv_function_002D3248.md) at `0x002D3359`
- [HalpInterruptEnablePerformanceEvents](HalpInterruptEnablePerformanceEvents_function_002D3420.md) at `0x002D354A`
- [KiDisconnectInterruptCommon](KiDisconnectInterruptCommon_function_002D36A8.md) at `0x002D3895`
- [HalDisableInterrupt](HalDisableInterrupt_function_002D39F0.md) at `0x002D3AF8`
- [KiDisconnectSecondaryInterrupt](KiDisconnectSecondaryInterrupt_function_002D3B88.md) at `0x002D3BE5`
- [KiConnectSecondaryInterrupt](KiConnectSecondaryInterrupt_function_002D4200.md) at `0x002D4292`
- [HalEnableInterrupt](HalEnableInterrupt_function_002D4990.md) at `0x002D4AB6`
- [KiInterruptDispatchCommon](../39/KiInterruptDispatchCommon_function_0039F3D0.md) at `0x0039F6F4`
- [KiInterruptDispatchCommon](../39/KiInterruptDispatchCommon_function_0039F3D0.md) at `0x0039F72A`
- [KiUnmaskSecondaryInterruptInternal](../47/KiUnmaskSecondaryInterruptInternal_function_00479CC8.md) at `0x00479D2D`
- [KiUnmaskSecondaryInterruptInternal](../47/KiUnmaskSecondaryInterruptInternal_function_00479CC8.md) at `0x00479D5B`
- [KiMaskSecondaryInterruptInternal](../47/KiMaskSecondaryInterruptInternal_function_00479D94.md) at `0x00479DE5`
- [KiMaskSecondaryInterruptInternal](../47/KiMaskSecondaryInterruptInternal_function_00479D94.md) at `0x00479E24`
- [HalpInterruptSetLineState](../48/HalpInterruptSetLineState_function_0048A0C8.md) at `0x0048A18D`
- [ExtEnvSetVpptTarget](../49/ExtEnvSetVpptTarget_function_0049D8FC.md) at `0x0049DA63`
- [HalpInterruptEnableNmi](../4A/HalpInterruptEnableNmi_function_004AD9E0.md) at `0x004ADA95`
- [HalpVpptArmTimer](../4A/HalpVpptArmTimer_function_004AFFE0.md) at `0x004B00CD`
- [HalpInterruptLocalErrorService](../4B/HalpInterruptLocalErrorService_function_004B9450.md) at `0x004B94E8`
- [HalpQueryProfileSource](../4C/HalpQueryProfileSource_function_004C6DBC.md) at `0x004C6E14`
- [HalpQueryProfileSource](../4C/HalpQueryProfileSource_function_004C6DBC.md) at `0x004C6E8C`
- [HalpTimerEnableHypervisorTimer](../4D/HalpTimerEnableHypervisorTimer_function_004D6ECC.md) at `0x004D7004`
- [HalpInterruptEnumerateUnmaskedInterrupts](../54/HalpInterruptEnumerateUnmaskedInterrupts_function_00542590.md) at `0x005426AE`
- [HalpInterruptRemapFixedLines](../54/HalpInterruptRemapFixedLines_function_00544210.md) at `0x005443DA`
- [HalpInterruptRequestInterrupt](../54/HalpInterruptRequestInterrupt_function_00544460.md) at `0x0054455A`
- [HalpInterruptSetLineSpecificOverride](../54/HalpInterruptSetLineSpecificOverride_function_0054468C.md) at `0x0054472D`
- [HalpInterruptServiceActiveBoth](../54/HalpInterruptServiceActiveBoth_function_00545CFC.md) at `0x00545DBC`
- [HalpTimerConfigureInterrupt](../54/HalpTimerConfigureInterrupt_function_00548AB0.md) at `0x00548EBF`
- [HalpVpptInitializePhysicalTimer](../54/HalpVpptInitializePhysicalTimer_function_0054A2F4.md) at `0x0054A365`
- [HalpVpptStop](../54/HalpVpptStop_function_0054A380.md) at `0x0054A405`
- [HalpAcquireSecondaryIcEntryExclusive](../55/HalpAcquireSecondaryIcEntryExclusive_function_00556C28.md) at `0x00556C7A`
- [HalpCreateSecondaryIcEntry](../55/HalpCreateSecondaryIcEntry_function_00556D4C.md) at `0x00556E39`
- [HalpDeleteSecondaryIcEntry](../55/HalpDeleteSecondaryIcEntry_function_00556E58.md) at `0x00556EB0`
- [HalpInsertSecondarySignalList](../55/HalpInsertSecondarySignalList_function_00556EFC.md) at `0x00556F75`
- [HalpInterruptEnumerateUnmaskedSecondaryInterrupts](../55/HalpInterruptEnumerateUnmaskedSecondaryInterrupts_function_00556F8C.md) at `0x0055707C`
- [HalpProcessSecondarySignalList](../55/HalpProcessSecondarySignalList_function_00557160.md) at `0x005571AC`
- [HalpProcessSecondarySignalList](../55/HalpProcessSecondarySignalList_function_00557160.md) at `0x005571E2`
- [HalpUnregisterSecondaryIcInterface](../55/HalpUnregisterSecondaryIcInterface_function_00557230.md) at `0x00557294`
- [EmonAddProfileSource](../55/EmonAddProfileSource_function_0055BEA0.md) at `0x0055C02F`
- [EmonAddProfileSource](../55/EmonAddProfileSource_function_0055BEA0.md) at `0x0055C075`
- [EmonEnableMonitoringEnhanced](../55/EmonEnableMonitoringEnhanced_function_0055C8E0.md) at `0x0055CA17`
- [EmonEnableMonitoringOriginal](../55/EmonEnableMonitoringOriginal_function_0055CA40.md) at `0x0055CB77`
- [EmonRemoveProfileSourceEnhanced](../55/EmonRemoveProfileSourceEnhanced_function_0055F1C0.md) at `0x0055F264`
- [EmonRemoveProfileSourceOriginal](../55/EmonRemoveProfileSourceOriginal_function_0055F2C0.md) at `0x0055F364`
- [EmonSetIntervalEnhanced](../55/EmonSetIntervalEnhanced_function_0055FDB0.md) at `0x0055FDF5`
- [EmonSetIntervalEnhanced](../55/EmonSetIntervalEnhanced_function_0055FDB0.md) at `0x0055FE3A`
- [EmonSetIntervalOriginal](../55/EmonSetIntervalOriginal_function_0055FFB0.md) at `0x0055FFF5`
- [EmonSetIntervalOriginal](../55/EmonSetIntervalOriginal_function_0055FFB0.md) at `0x0056003A`
- [Amd64AddProfileSource](../56/Amd64AddProfileSource_function_0056B720.md) at `0x0056B8A9`
- [Amd64AddProfileSource](../56/Amd64AddProfileSource_function_0056B720.md) at `0x0056B8F1`
- [Amd64EnableMonitoring](../56/Amd64EnableMonitoring_function_0056C360.md) at `0x0056C4DB`
- [Amd64RemoveProfileSource](../56/Amd64RemoveProfileSource_function_0056D900.md) at `0x0056D9B7`
- [Amd64SetInterval](../56/Amd64SetInterval_function_0056DB50.md) at `0x0056DB95`
- [Amd64SetInterval](../56/Amd64SetInterval_function_0056DB50.md) at `0x0056DBE1`
- [IvtAttachDeviceDomainInternal](../56/IvtAttachDeviceDomainInternal_function_0056ED90.md) at `0x0056EF6B`
- [IvtAttachDeviceDomainInternal](../56/IvtAttachDeviceDomainInternal_function_0056ED90.md) at `0x0056EFAF`
- [IvtFreeDomain](../56/IvtFreeDomain_function_0056F8E0.md) at `0x0056F924`
- [IvtLegacyAttachDeviceDomainInternal](../57/IvtLegacyAttachDeviceDomainInternal_function_00570EDC.md) at `0x00571064`
- [IvtLegacyAttachDeviceDomainInternal](../57/IvtLegacyAttachDeviceDomainInternal_function_00570EDC.md) at `0x005710A8`
- [IvtLegacyFlushDomainTb](../57/IvtLegacyFlushDomainTb_function_00571420.md) at `0x0057147D`
- [HsaAllocateRemappingTableEntry](../57/HsaAllocateRemappingTableEntry_function_00573820.md) at `0x0057396C`
- [HsaAllocateRemappingTableEntry](../57/HsaAllocateRemappingTableEntry_function_00573820.md) at `0x00573AB5`
- [HsaFreeRemappingTableEntry](../57/HsaFreeRemappingTableEntry_function_00574140.md) at `0x0057421A`
- [sub_006DD9A0](../6D/Unknown_function_006DD9A0.md) at `0x006DDA3A`

### Static image references
- `0x002D1C66` → RVA `0x00FC6D20` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002D1C58  40 53                           push rbx
002D1C5A  48 83 EC 20                     sub rsp, 0x20
002D1C5E  0F B6 DA                        movzx ebx, dl
002D1C61  E8 0A 4A F3 FF                  call 0x140206670
002D1C66  83 3D B3 50 CF 00 00            cmp dword ptr [rip + 0xcf50b3], 0
002D1C6D  74 0B                           je 0x1402d1c7a
002D1C6F  44 0F 20 C1                     mov rcx, cr8
002D1C73  8A D3                           mov dl, bl
002D1C75  E8 1E 3A 22 00                  call 0x1404f5698
002D1C7A  44 0F 22 C3                     mov cr8, rbx
002D1C7E  48 83 C4 20                     add rsp, 0x20
002D1C82  5B                              pop rbx
002D1C83  C3                              ret
002D1C84  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpReleaseHighLevelLock(__int64 a1, unsigned __int8 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = KxReleaseSpinLock(a1, a2, a3, a4);
    if ((*(unsigned int *)(v_rip + 13586611)) != 0) {
        a1 = v_cr8;
        a2 = a2;
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HalpReleaseHighLevelLock(int64_t Arg1, uint8_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = KxReleaseSpinLock(Arg1, Arg2, a3, a4);
    if ((*(uint32_t *)(v_rip + 0xCF50B3)) != 0) {
        Arg1 = v_cr8;
        Arg2 = Arg2;
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002D1C58&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002D1C58[BB_002D1C58]
  bb_002D1C6F[BB_002D1C6F]
  bb_002D1C7A[BB_002D1C7A]
  bb_002D1C84[BB_002D1C84]
  bb_002D1C58 -->|branch| bb_002D1C7A
  bb_002D1C58 -->|fallthrough| bb_002D1C6F
  bb_002D1C6F -->|flow| bb_002D1C7A
```
