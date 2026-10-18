# HalpAcquireHighLevelLock

- RVA: `0x002D2390`–`0x002D23D2` (길이 `66` bytes)
- VA: `0x00000001402D2390`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060BE4`
- 디코드: `20`개 명령, `66/66` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **51**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x002D23B6` → [KeAcquireSpinLockAtDpcLevel](../20/KeAcquireSpinLockAtDpcLevel_function_00208430.md) (function, `0x00208430`)
- `0x002D23CB` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)

### Direct callers
- [HalpQueryProfileSourceList](HalpQueryProfileSourceList_function_002D1370.md) at `0x002D13AD`
- [IvtFlushDomainTb](IvtFlushDomainTb_function_002D1BD0.md) at `0x002D1BF1`
- [HalpMaskInterrupt](HalpMaskInterrupt_function_002D1DB0.md) at `0x002D1E22`
- [HalpUnmaskInterrupt](HalpUnmaskInterrupt_function_002D1EE0.md) at `0x002D1F81`
- [HalpFindSecondaryIcEntry](HalpFindSecondaryIcEntry_function_002D219C.md) at `0x002D21B4`
- [HalpVpptAcknowledgeInterrupt](HalpVpptAcknowledgeInterrupt_function_002D2230.md) at `0x002D2244`
- [HalpInterruptApplyOverrides](HalpInterruptApplyOverrides_function_002D2CE0.md) at `0x002D2D08`
- [HalpInterruptSetDestination](HalpInterruptSetDestination_function_002D3100.md) at `0x002D31C5`
- [HalpInterruptSetRemappedDestinationHv](HalpInterruptSetRemappedDestinationHv_function_002D3248.md) at `0x002D3337`
- [HalpInterruptEnablePerformanceEvents](HalpInterruptEnablePerformanceEvents_function_002D3420.md) at `0x002D3536`
- [HalDisableInterrupt](HalDisableInterrupt_function_002D39F0.md) at `0x002D3AC1`
- [HalEnableInterrupt](HalEnableInterrupt_function_002D4990.md) at `0x002D4A77`
- [HalpInterruptSetLineState](../48/HalpInterruptSetLineState_function_0048A0C8.md) at `0x0048A13A`
- [ExtEnvSetVpptTarget](../49/ExtEnvSetVpptTarget_function_0049D8FC.md) at `0x0049DA11`
- [HalpInterruptEnableNmi](../4A/HalpInterruptEnableNmi_function_004AD9E0.md) at `0x004ADA47`
- [HalpVpptArmTimer](../4A/HalpVpptArmTimer_function_004AFFE0.md) at `0x004B0010`
- [HalpInterruptLocalErrorService](../4B/HalpInterruptLocalErrorService_function_004B9450.md) at `0x004B946F`
- [HalpQueryProfileSource](../4C/HalpQueryProfileSource_function_004C6DBC.md) at `0x004C6DF1`
- [HalpTimerEnableHypervisorTimer](../4D/HalpTimerEnableHypervisorTimer_function_004D6ECC.md) at `0x004D6FC2`
- [HalpInterruptEnumerateUnmaskedInterrupts](../54/HalpInterruptEnumerateUnmaskedInterrupts_function_00542590.md) at `0x005425E4`
- [HalpInterruptRemapFixedLines](../54/HalpInterruptRemapFixedLines_function_00544210.md) at `0x005443B0`
- [HalpInterruptRequestInterrupt](../54/HalpInterruptRequestInterrupt_function_00544460.md) at `0x00544506`
- [HalpInterruptSetLineSpecificOverride](../54/HalpInterruptSetLineSpecificOverride_function_0054468C.md) at `0x005446F4`
- [HalpInterruptServiceActiveBoth](../54/HalpInterruptServiceActiveBoth_function_00545CFC.md) at `0x00545D58`
- [HalpTimerConfigureInterrupt](../54/HalpTimerConfigureInterrupt_function_00548AB0.md) at `0x00548E7C`
- [HalpVpptInitializePhysicalTimer](../54/HalpVpptInitializePhysicalTimer_function_0054A2F4.md) at `0x0054A301`
- [HalpVpptStop](../54/HalpVpptStop_function_0054A380.md) at `0x0054A390`
- [HalpAcquireSecondaryIcEntryExclusive](../55/HalpAcquireSecondaryIcEntryExclusive_function_00556C28.md) at `0x00556C64`
- [HalpAcquireSecondaryIcEntryExclusive](../55/HalpAcquireSecondaryIcEntryExclusive_function_00556C28.md) at `0x00556C9D`
- [HalpCreateSecondaryIcEntry](../55/HalpCreateSecondaryIcEntry_function_00556D4C.md) at `0x00556E00`
- [HalpInsertSecondarySignalList](../55/HalpInsertSecondarySignalList_function_00556EFC.md) at `0x00556F10`
- [HalpInterruptEnumerateUnmaskedSecondaryInterrupts](../55/HalpInterruptEnumerateUnmaskedSecondaryInterrupts_function_00556F8C.md) at `0x00556FD0`
- [HalpProcessSecondarySignalList](../55/HalpProcessSecondarySignalList_function_00557160.md) at `0x00557171`
- [HalpProcessSecondarySignalList](../55/HalpProcessSecondarySignalList_function_00557160.md) at `0x005571C6`
- [HalpUnregisterSecondaryIcInterface](../55/HalpUnregisterSecondaryIcInterface_function_00557230.md) at `0x00557252`
- [EmonAddProfileSource](../55/EmonAddProfileSource_function_0055BEA0.md) at `0x0055BFF5`
- [EmonEnableMonitoringEnhanced](../55/EmonEnableMonitoringEnhanced_function_0055C8E0.md) at `0x0055C91A`
- [EmonEnableMonitoringOriginal](../55/EmonEnableMonitoringOriginal_function_0055CA40.md) at `0x0055CA7A`
- [EmonRemoveProfileSourceEnhanced](../55/EmonRemoveProfileSourceEnhanced_function_0055F1C0.md) at `0x0055F243`
- [EmonRemoveProfileSourceOriginal](../55/EmonRemoveProfileSourceOriginal_function_0055F2C0.md) at `0x0055F343`
- [EmonSetIntervalEnhanced](../55/EmonSetIntervalEnhanced_function_0055FDB0.md) at `0x0055FDD1`
- [EmonSetIntervalOriginal](../55/EmonSetIntervalOriginal_function_0055FFB0.md) at `0x0055FFD1`
- [Amd64AddProfileSource](../56/Amd64AddProfileSource_function_0056B720.md) at `0x0056B870`
- [Amd64EnableMonitoring](../56/Amd64EnableMonitoring_function_0056C360.md) at `0x0056C39B`
- [Amd64RemoveProfileSource](../56/Amd64RemoveProfileSource_function_0056D900.md) at `0x0056D996`
- [Amd64SetInterval](../56/Amd64SetInterval_function_0056DB50.md) at `0x0056DB71`
- [IvtAttachDeviceDomainInternal](../56/IvtAttachDeviceDomainInternal_function_0056ED90.md) at `0x0056EF33`
- [IvtAttachDeviceDomainInternal](../56/IvtAttachDeviceDomainInternal_function_0056ED90.md) at `0x0056EF81`
- [IvtFreeDomain](../56/IvtFreeDomain_function_0056F8E0.md) at `0x0056F8F9`
- [IvtLegacyAttachDeviceDomainInternal](../57/IvtLegacyAttachDeviceDomainInternal_function_00570EDC.md) at `0x0057102C`
- [IvtLegacyAttachDeviceDomainInternal](../57/IvtLegacyAttachDeviceDomainInternal_function_00570EDC.md) at `0x0057107A`
- [IvtLegacyFlushDomainTb](../57/IvtLegacyFlushDomainTb_function_00571420.md) at `0x00571441`
- [HsaAllocateRemappingTableEntry](../57/HsaAllocateRemappingTableEntry_function_00573820.md) at `0x00573932`
- [HsaAllocateRemappingTableEntry](../57/HsaAllocateRemappingTableEntry_function_00573820.md) at `0x00573A32`
- [HsaFreeRemappingTableEntry](../57/HsaFreeRemappingTableEntry_function_00574140.md) at `0x005741B7`
- [sub_006DD9A0](../6D/Unknown_function_006DD9A0.md) at `0x006DD9F7`

### Static image references
- `0x002D23AA` → RVA `0x00FC6D20` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002D2390  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
002D2395  57                              push rdi
002D2396  48 83 EC 20                     sub rsp, 0x20
002D239A  48 8B F9                        mov rdi, rcx
002D239D  44 0F 20 C3                     mov rbx, cr8
002D23A1  BA 0F 00 00 00                  mov edx, 0xf
002D23A6  44 0F 22 C2                     mov cr8, rdx
002D23AA  83 3D 6F 49 CF 00 00            cmp dword ptr [rip + 0xcf496f], 0
002D23B1  75 16                           jne 0x1402d23c9
002D23B3  48 8B CF                        mov rcx, rdi
002D23B6  E8 75 60 F3 FF                  call 0x140208430
002D23BB  8A C3                           mov al, bl
002D23BD  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
002D23C2  48 83 C4 20                     add rsp, 0x20
002D23C6  5F                              pop rdi
002D23C7  C3                              ret
002D23C8  CC                              int3
002D23C9  8A CB                           mov cl, bl
002D23CB  E8 2C 33 22 00                  call 0x1404f56fc
002D23D0  EB E1                           jmp 0x1402d23b3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpAcquireHighLevelLock(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    if ((*(unsigned int *)(v_rip + 13584751)) != 0) goto loc_002D23C9;
loc_002D23B3:
    result = KeAcquireSpinLockAtDpcLevel(a1, 15, a3, a4);
    v_rsp = (v_rsp) + (32);
    return (unsigned __int8)(v_cr8);
loc_002D23C9:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(v_stack_p8), 15, a3, a4);
    goto loc_002D23B3;
}
```

## 5. (Beta) C Style

```c
int64_t HalpAcquireHighLevelLock(int64_t Arg1)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    if ((*(uint32_t *)(v_rip + 0xCF496F)) != 0) goto loc_002D23C9;
loc_002D23B3:
    result = KeAcquireSpinLockAtDpcLevel(Arg1, 15, a3, a4);
    local_rsp = (local_rsp) + (32);
    return (uint8_t)(v_cr8);
loc_002D23C9:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(v_stack_p8), 15, a3, a4);
    goto loc_002D23B3;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002D2390&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002D2390[BB_002D2390]
  bb_002D23B3[BB_002D23B3]
  bb_002D23C8[BB_002D23C8]
  bb_002D23C9[BB_002D23C9]
  bb_002D2390 -->|branch| bb_002D23C9
  bb_002D2390 -->|fallthrough| bb_002D23B3
  bb_002D23C8 -->|flow| bb_002D23C9
  bb_002D23C9 -->|branch| bb_002D23B3
```
