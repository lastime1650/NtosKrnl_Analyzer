# IopOpenRegistryKeyEx

- RVA: `0x00A51B44`–`0x00A51B83` (길이 `63` bytes)
- VA: `0x0000000140A51B44`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CC98`
- 디코드: `16`개 명령, `63/63` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **49**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A51B78` → [ZwOpenKey](../../text/6A/ZwOpenKey_function_006AD310.md) (function, `0x006AD310`)

### Direct callers
- [PnpBootDeviceWait](../../text/5A/PnpBootDeviceWait_function_005A4D68.md) at `0x005A4DCA`
- [IoSetSystemPartition](../71/IoSetSystemPartition_function_0071DF90.md) at `0x0071DFFB`
- [PipCallbackHasDeviceOverrides](../72/PipCallbackHasDeviceOverrides_function_007231D4.md) at `0x00723222`
- [PipCheckComputerSupported](../72/PipCheckComputerSupported_function_007232B0.md) at `0x0072332D`
- [PipGetDriverKsrGuid](../72/PipGetDriverKsrGuid_function_00725100.md) at `0x0072516E`
- [PiGetDeviceRegistryProperty](../72/PiGetDeviceRegistryProperty_function_007280A8.md) at `0x00728174`
- [PipServiceInstanceToDeviceInstance](../72/PipServiceInstanceToDeviceInstance_function_0072C150.md) at `0x0072C1B2`
- [PnpOpenFirstMatchingSubKey](../72/PnpOpenFirstMatchingSubKey_function_0072CA20.md) at `0x0072CA82`
- [PipDmgGetDeviceDmarRegistryValue](../73/PipDmgGetDeviceDmarRegistryValue_function_007307F0.md) at `0x00730861`
- [PipDmgInitReadGroupPolicy](../73/PipDmgInitReadGroupPolicy_function_007309B8.md) at `0x007309F7`
- [PiDcInitUpdateProperties](../73/PiDcInitUpdateProperties_function_00730B3C.md) at `0x00730BD9`
- [PiDcInitUpdateProperties](../73/PiDcInitUpdateProperties_function_00730B3C.md) at `0x00730C54`
- [PiDevCfgOpenDeviceMigrationKey](../73/PiDevCfgOpenDeviceMigrationKey_function_00733EE4.md) at `0x00733F51`
- [PiDevCfgOpenDeviceMigrationKey](../73/PiDevCfgOpenDeviceMigrationKey_function_00733EE4.md) at `0x00733F79`
- [PiDevCfgQueryDriverNode](../73/PiDevCfgQueryDriverNode_function_0073435C.md) at `0x007349D7`
- [PiDevCfgQueryDriverNode](../73/PiDevCfgQueryDriverNode_function_0073435C.md) at `0x00734A01`
- [PiDevCfgQueryMinWhcpVersion](../73/PiDevCfgQueryMinWhcpVersion_function_00735204.md) at `0x00735257`
- [PiDevCfgQueryPolicyStringList](../73/PiDevCfgQueryPolicyStringList_function_00735358.md) at `0x00735412`
- [PiDevCfgReadDriverPolicy](../73/PiDevCfgReadDriverPolicy_function_00735638.md) at `0x007356A1`
- [PiDevCfgResetDeviceKeys](../73/PiDevCfgResetDeviceKeys_function_00735924.md) at `0x0073596B`
- [PpDevCfgProcessDeviceClass](../73/PpDevCfgProcessDeviceClass_function_00736824.md) at `0x00736A8B`
- [PnpProfileUpdateHardwareProfile](../73/PnpProfileUpdateHardwareProfile_function_0073773C.md) at `0x0073778F`
- [PnpProfileUpdateHardwareProfile](../73/PnpProfileUpdateHardwareProfile_function_0073773C.md) at `0x007377BC`
- [NtEnableLastKnownGood](../83/NtEnableLastKnownGood_function_0083C680.md) at `0x0083C756`
- [PiDevCfgInitMigrationContext](../96/PiDevCfgInitMigrationContext_function_009642E0.md) at `0x0096448E`
- [PiDevCfgInitResolveContext](../96/PiDevCfgInitResolveContext_function_00965178.md) at `0x00965275`
- [PiDevCfgResetDeviceDriverSettings](../96/PiDevCfgResetDeviceDriverSettings_function_00966168.md) at `0x0096637C`
- [PiDevCfgConfigureDevice](../97/PiDevCfgConfigureDevice_function_00977BB4.md) at `0x009787E9`
- [IopUpdateSecureDeviceClassState](../9A/IopUpdateSecureDeviceClassState_function_009A2CE8.md) at `0x009A2DFF`
- [PipFindDeviceOverrideEntry](../A2/PipFindDeviceOverrideEntry_function_00A2A694.md) at `0x00A2A919`
- [PiDevCfgEnforceDevicePolicy](../A8/PiDevCfgEnforceDevicePolicy_function_00A89454.md) at `0x00A8955B`
- [PiDevCfgConfigureDeviceKeyCallback](../A9/PiDevCfgConfigureDeviceKeyCallback_function_00A99890.md) at `0x00A99982`
- [PiDevCfgConfigureDeviceLocation](../AA/PiDevCfgConfigureDeviceLocation_function_00AA88C0.md) at `0x00AA898F`
- [PiDevCfgConfigureDeviceLocation](../AA/PiDevCfgConfigureDeviceLocation_function_00AA88C0.md) at `0x00AA8A25`
- [PiDevCfgConfigureDeviceLocation](../AA/PiDevCfgConfigureDeviceLocation_function_00AA88C0.md) at `0x00AA8B20`
- [PiDevCfgConfigureDeviceLocation](../AA/PiDevCfgConfigureDeviceLocation_function_00AA88C0.md) at `0x00AA8B5A`
- [PiDevCfgResolveVariableKeyHandle](../AB/PiDevCfgResolveVariableKeyHandle_function_00AB2A24.md) at `0x00AB2C0C`
- [PiDevCfgResolveVariableKeyHandle](../AB/PiDevCfgResolveVariableKeyHandle_function_00AB2A24.md) at `0x00AB2CBC`
- [PiDevCfgResolveVariableKeyHandle](../AB/PiDevCfgResolveVariableKeyHandle_function_00AB2A24.md) at `0x00AB30F8`
- [sub_00B28306](../B2/Unknown_function_00B28306.md) at `0x00B28330`
- [sub_00B286C8](../B2/Unknown_function_00B286C8.md) at `0x00B28749`
- [sub_00B2D22A](../B2/Unknown_function_00B2D22A.md) at `0x00B2D23D`
- [sub_00B2D22A](../B2/Unknown_function_00B2D22A.md) at `0x00B2D25A`
- [sub_00B2D22A](../B2/Unknown_function_00B2D22A.md) at `0x00B2D287`
- [sub_00B2D22A](../B2/Unknown_function_00B2D22A.md) at `0x00B2D3D3`
- [sub_00B38904](../B3/Unknown_function_00B38904.md) at `0x00B38A77`
- [sub_00B38904](../B3/Unknown_function_00B38904.md) at `0x00B38AE4`
- [sub_00B38B6C](../B3/Unknown_function_00B38B6C.md) at `0x00B38B7A`
- [sub_00B453C2](../B4/Unknown_function_00B453C2.md) at `0x00B453E3`
- [IopStoreSystemPartitionInformation](../../init/C2/IopStoreSystemPartitionInformation_function_00C2D780.md) at `0x00C2D8B5`
- [IopInitializeBootDrivers](../../init/C2/IopInitializeBootDrivers_function_00C2E6F4.md) at `0x00C2E7BB`
- [IopInitializeBootDrivers](../../init/C2/IopInitializeBootDrivers_function_00C2E6F4.md) at `0x00C2E7E4`
- [IopInitializeBootDrivers](../../init/C2/IopInitializeBootDrivers_function_00C2E6F4.md) at `0x00C2EA88`
- [IopInitializePlugPlayServices](../../init/C2/IopInitializePlugPlayServices_function_00C2F298.md) at `0x00C2F7D7`
- [PiInitCacheGroupInformation](../../init/C3/PiInitCacheGroupInformation_function_00C300E8.md) at `0x00C3012D`
- [PipCheckSystemFirmwareUpdated](../../init/C3/PipCheckSystemFirmwareUpdated_function_00C3048C.md) at `0x00C304D0`
- [PipGetDriverTagPriority](../../init/C3/PipGetDriverTagPriority_function_00C30A10.md) at `0x00C30A65`
- [PipInitDeviceOverrideCache](../../init/C3/PipInitDeviceOverrideCache_function_00C312C8.md) at `0x00C31346`
- [VhdAutoAttachVirtualDisks](../../init/C6/VhdAutoAttachVirtualDisks_function_00C6D934.md) at `0x00C6D9AC`
- [VhdAutoAttachVirtualDisks](../../init/C6/VhdAutoAttachVirtualDisks_function_00C6D934.md) at `0x00C6DA3A`
- [CompositefsBootIsEnabled](../../init/C6/CompositefsBootIsEnabled_function_00C6F254.md) at `0x00C6F29A`
- [IopInitializeSystemDrivers](../../init/C7/IopInitializeSystemDrivers_function_00C73590.md) at `0x00C73672`
- [PipInitializeCoreDriversByGroup](../../init/C7/PipInitializeCoreDriversByGroup_function_00C740DC.md) at `0x00C7417D`
- [PipInitializeEarlyLaunchDrivers](../../init/C7/PipInitializeEarlyLaunchDrivers_function_00C74288.md) at `0x00C742FC`
- [IopInitializeBuiltinDriver](../../init/C7/IopInitializeBuiltinDriver_function_00C7625C.md) at `0x00C7657D`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00A51B78` → [ZwOpenKey](../../text/6A/ZwOpenKey_function_006AD310.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A51B44  4C 8B DC                        mov r11, rsp
00A51B47  48 83 EC 58                     sub rsp, 0x58
00A51B4B  49 89 53 D0                     mov qword ptr [r11 - 0x30], rdx
00A51B4F  33 C0                           xor eax, eax
00A51B51  4D 89 43 D8                     mov qword ptr [r11 - 0x28], r8
00A51B55  0F 57 C0                        xorps xmm0, xmm0
00A51B58  49 C7 43 C8 30 00 00 00         mov qword ptr [r11 - 0x38], 0x30
00A51B60  4D 8D 43 C8                     lea r8, [r11 - 0x38]
00A51B64  49 C7 43 E0 40 02 00 00         mov qword ptr [r11 - 0x20], 0x240
00A51B6C  41 8B D1                        mov edx, r9d
00A51B6F  48 89 01                        mov qword ptr [rcx], rax
00A51B72  F3 0F 7F 44 24 40               movdqu xmmword ptr [rsp + 0x40], xmm0
00A51B78  E8 93 B7 C5 FF                  call 0x1406ad310
00A51B7D  48 83 C4 58                     add rsp, 0x58
00A51B81  C3                              ret
00A51B82  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IopOpenRegistryKeyEx(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;

    v_rsp = (v_rsp) - (88);
    *(unsigned __int64 *)(v_rsp - 48) = a2;
    result = 0;
    *(unsigned __int64 *)(v_rsp - 40) = a3;
    *(unsigned __int64 *)(v_rsp - 56) = 48;
    *(unsigned __int64 *)(v_rsp - 32) = 576;
    *(unsigned __int64 *)(a1) = 0;
    v_stack_m18 = v_xmm0;
    result = ZwOpenKey(a1, (unsigned int)(a4), v_rsp - 56, a4);
    v_rsp = (v_rsp) + (88);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t IopOpenRegistryKeyEx(void *Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;

    local_rsp = (local_rsp) - (88);
    *(uint64_t *)(local_rsp - 0x30) = Arg2;
    result = 0;
    *(uint64_t *)(local_rsp - 0x28) = Arg3;
    *(uint64_t *)(local_rsp - 0x38) = 48;
    *(uint64_t *)(local_rsp - 0x20) = 576;
    *(uint64_t *)(arg1) = 0;
    v_stack_m18 = v_xmm0;
    result = ZwOpenKey(Arg1, (uint32_t)(Arg4), local_rsp - 56, Arg4);
    local_rsp = (local_rsp) + (88);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A51B44&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A51B44[BB_00A51B44]
  bb_00A51B82[BB_00A51B82]
```
