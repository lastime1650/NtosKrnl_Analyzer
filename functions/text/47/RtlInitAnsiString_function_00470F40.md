# RtlInitAnsiString

- RVA: `0x00470F40`–`0x00470F7E` (길이 `62` bytes)
- VA: `0x0000000140470F40`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `19`개 명령, `62/62` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **49**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00470F59` → [strlen](../6C/strlen_function_006C70D0.md) (function, `0x006C70D0`)

### Direct callers
- [RtlInitUTF8String](RtlInitUTF8String_function_00470F90.md) at `0x00470F94`
- [IopCreateUnicodeFromAnsiBuffer](../59/IopCreateUnicodeFromAnsiBuffer_function_00596AEC.md) at `0x00596B02`
- [IopCheckDiskName](../59/IopCheckDiskName_function_00597EB8.md) at `0x00597EFD`
- [PopEmModuleAddressMatchCallback](../5D/PopEmModuleAddressMatchCallback_function_005DA3F0.md) at `0x005DA449`
- [PopEmUpdateDeviceConstraintCallback](../5D/PopEmUpdateDeviceConstraintCallback_function_005DC7F0.md) at `0x005DC85B`
- [SepImageHashFromEa](../60/SepImageHashFromEa_function_00608310.md) at `0x0060833B`
- [SepImageHashFromEa](../60/SepImageHashFromEa_function_00608310.md) at `0x00608349`
- [WheaGetCurrentProcessName](../65/WheaGetCurrentProcessName_function_0065F260.md) at `0x0065F29B`
- [CmpInitializeLoadOptions](../66/CmpInitializeLoadOptions_function_0066A228.md) at `0x0066A24D`
- [ScAnsiToUnicodeString](../6A/ScAnsiToUnicodeString_function_006A3FB0.md) at `0x006A3FDD`
- [IopCopyBootLogRegistryToFile](../../page/71/IopCopyBootLogRegistryToFile_function_0071B19C.md) at `0x0071B2B9`
- [KsepGetModuleInfoByName](../../page/74/KsepGetModuleInfoByName_function_0074AA04.md) at `0x0074AA95`
- [SepInitializationPhase1](../../page/79/SepInitializationPhase1_function_0079C580.md) at `0x0079C631`
- [SepInitializationPhase1](../../page/79/SepInitializationPhase1_function_0079C580.md) at `0x0079C75B`
- [WmipCheckSMBiosSysInfoString](../../page/7B/WmipCheckSMBiosSysInfoString_function_007B289C.md) at `0x007B28E0`
- [WmipGetSMBiosString](../../page/7B/WmipGetSMBiosString_function_007B2D30.md) at `0x007B2D8B`
- [WmipQueryWmiRegInfo](../../page/7B/WmipQueryWmiRegInfo_function_007B4B50.md) at `0x007B4B77`
- [EtwWmitraceWorker](../../page/7B/EtwWmitraceWorker_function_007BBD3C.md) at `0x007BBF60`
- [EtwWmitraceWorker](../../page/7B/EtwWmitraceWorker_function_007BBD3C.md) at `0x007BBFC6`
- [NtQuerySystemEnvironmentValue](../../page/7C/NtQuerySystemEnvironmentValue_function_007CDFB0.md) at `0x007CE216`
- [CmpAddProcessorConfigurationEntry](../../page/7E/CmpAddProcessorConfigurationEntry_function_007E4CF8.md) at `0x007E4F7E`
- [CmpAddProcessorConfigurationEntry](../../page/7E/CmpAddProcessorConfigurationEntry_function_007E4CF8.md) at `0x007E4FFA`
- [CmpSetVersionData](../../page/7E/CmpSetVersionData_function_007E7854.md) at `0x007E7B99`
- [CmpSetVersionData](../../page/7E/CmpSetVersionData_function_007E7854.md) at `0x007E7C78`
- [CmpInitializeRegistryNode](../../page/7E/CmpInitializeRegistryNode_function_007EE81C.md) at `0x007EE939`
- [CmpInitializeRegistryNode](../../page/7E/CmpInitializeRegistryNode_function_007EE81C.md) at `0x007EEA3A`
- [CmpAddRemoveContainerToCLFSLog](../../page/7F/CmpAddRemoveContainerToCLFSLog_function_007F69FC.md) at `0x007F6B01`
- [AslStringAnsiToUnicode](../../page/81/AslStringAnsiToUnicode_function_00819824.md) at `0x0081984D`
- [EtwpBuildProcessEvent](../../page/8A/EtwpBuildProcessEvent_function_008A552C.md) at `0x008A5563`
- [MiResolveImageReferences](../../page/A2/MiResolveImageReferences_function_00A23BE4.md) at `0x00A23D09`
- [MiLogFailedDriverLoad](../../page/A2/MiLogFailedDriverLoad_function_00A24ACC.md) at `0x00A24BA3`
- [PopPowerRequestStatsGetIdForRequest](../../page/A2/PopPowerRequestStatsGetIdForRequest_function_00A2D784.md) at `0x00A2D889`
- [PnpLogVetoInformation](../../page/AB/PnpLogVetoInformation_function_00AB6BE8.md) at `0x00AB6C95`
- [sub_00B257D0](../../page/B2/Unknown_function_00B257D0.md) at `0x00B257DD`
- [sub_00B2CEFC](../../page/B2/Unknown_function_00B2CEFC.md) at `0x00B2CF22`
- [sub_00B2EDF4](../../page/B2/Unknown_function_00B2EDF4.md) at `0x00B2EE90`
- [ExpSystemErrorHandler2](../../pagelk/B7/ExpSystemErrorHandler2_function_00B72C30.md) at `0x00B730A4`
- [ExpSystemErrorHandler2](../../pagelk/B7/ExpSystemErrorHandler2_function_00B72C30.md) at `0x00B731E9`
- [KdInitSystem](../../pagekd/B8/KdInitSystem_function_00B85E30.md) at `0x00B8649A`
- [InitBootProcessor](../../init/C1/InitBootProcessor_function_00C1B1C8.md) at `0x00C1BA6F`
- [InitBootProcessor](../../init/C1/InitBootProcessor_function_00C1B1C8.md) at `0x00C1BBDA`
- [InitLoadDebuggerSymbols](../../init/C1/InitLoadDebuggerSymbols_function_00C1BEB0.md) at `0x00C1BF2D`
- [Phase1InitializationDiscard](../../init/C1/Phase1InitializationDiscard_function_00C1C728.md) at `0x00C1D0CF`
- [EmpInfParseGetGuidFromName](../../init/C2/EmpInfParseGetGuidFromName_function_00C263B4.md) at `0x00C2640E`
- [EmpParseEntryTypes](../../init/C2/EmpParseEntryTypes_function_00C267B4.md) at `0x00C26848`
- [IopCreateArcNames](../../init/C2/IopCreateArcNames_function_00C2BF1C.md) at `0x00C2BF77`
- [IopCreateArcNames](../../init/C2/IopCreateArcNames_function_00C2BF1C.md) at `0x00C2BFB4`
- [IopCreateArcNames](../../init/C2/IopCreateArcNames_function_00C2BF1C.md) at `0x00C2C020`
- [IopCreateArcNamesCd](../../init/C2/IopCreateArcNamesCd_function_00C2C060.md) at `0x00C2C2E2`
- [IopCreateArcNamesCd](../../init/C2/IopCreateArcNamesCd_function_00C2C060.md) at `0x00C2C32E`
- [IopCreateArcNamesCd](../../init/C2/IopCreateArcNamesCd_function_00C2C060.md) at `0x00C2C4C2`
- [IopMarkBootPartition](../../init/C2/IopMarkBootPartition_function_00C2CFA0.md) at `0x00C2D033`
- [IopGetBootDiskInformation](../../init/C2/IopGetBootDiskInformation_function_00C2DAAC.md) at `0x00C2DB94`
- [IopGetBootDiskInformation](../../init/C2/IopGetBootDiskInformation_function_00C2DAAC.md) at `0x00C2DBA4`
- [IopGetBootDiskInformation](../../init/C2/IopGetBootDiskInformation_function_00C2DAAC.md) at `0x00C2DBDB`
- [IopGetBootDiskInformation](../../init/C2/IopGetBootDiskInformation_function_00C2DAAC.md) at `0x00C2DE60`
- [IopGetBootDiskInformationLite](../../init/C2/IopGetBootDiskInformationLite_function_00C2DF64.md) at `0x00C2E007`
- [IopGetBootDiskInformationLite](../../init/C2/IopGetBootDiskInformationLite_function_00C2DF64.md) at `0x00C2E01E`
- [IopGetBootDiskInformationLite](../../init/C2/IopGetBootDiskInformationLite_function_00C2DF64.md) at `0x00C2E035`
- [IopGetBootDiskInformationLite](../../init/C2/IopGetBootDiskInformationLite_function_00C2DF64.md) at `0x00C2E0AF`
- [IopApplySystemPartitionProt](../../init/C2/IopApplySystemPartitionProt_function_00C2E398.md) at `0x00C2E517`
- [PipCriticalDeviceWaitCallback](../../init/C3/PipCriticalDeviceWaitCallback_function_00C30890.md) at `0x00C3091E`
- [WmipDriverEntry](../../init/C4/WmipDriverEntry_function_00C4D490.md) at `0x00C4D50B`
- [CmpInitializeDriverStores](../../init/C5/CmpInitializeDriverStores_function_00C57CF0.md) at `0x00C57F13`
- [CmpSetSystemBiosInformation](../../init/C5/CmpSetSystemBiosInformation_function_00C5A5D0.md) at `0x00C5A6D4`
- [CmpSetSystemBiosInformation](../../init/C5/CmpSetSystemBiosInformation_function_00C5A5D0.md) at `0x00C5A7D0`
- [CmpSetSystemBiosInformation](../../init/C5/CmpSetSystemBiosInformation_function_00C5A5D0.md) at `0x00C5A87D`
- [CmpSetVideoBiosInformation](../../init/C5/CmpSetVideoBiosInformation_function_00C5A970.md) at `0x00C5AAED`
- [CmpSetVideoBiosInformation](../../init/C5/CmpSetVideoBiosInformation_function_00C5A970.md) at `0x00C5AB6A`
- [RamdiskCreateSymbolicLink](../../init/C6/RamdiskCreateSymbolicLink_function_00C6EDB8.md) at `0x00C6EE4B`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00470F40  40 53                           push rbx
00470F42  48 83 EC 20                     sub rsp, 0x20
00470F46  48 83 21 00                     and qword ptr [rcx], 0
00470F4A  48 8B D9                        mov rbx, rcx
00470F4D  48 89 51 08                     mov qword ptr [rcx + 8], rdx
00470F51  48 85 D2                        test rdx, rdx
00470F54  74 21                           je 0x140470f77
00470F56  48 8B CA                        mov rcx, rdx
00470F59  E8 72 61 25 00                  call 0x1406c70d0
00470F5E  48 3D FF FF 00 00               cmp rax, 0xffff
00470F64  B9 FE FF 00 00                  mov ecx, 0xfffe
00470F69  48 0F 43 C1                     cmovae rax, rcx
00470F6D  66 89 03                        mov word ptr [rbx], ax
00470F70  66 FF C0                        inc ax
00470F73  66 89 43 02                     mov word ptr [rbx + 2], ax
00470F77  48 83 C4 20                     add rsp, 0x20
00470F7B  5B                              pop rbx
00470F7C  C3                              ret
00470F7D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlInitAnsiString(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    *(unsigned __int64 *)(a1 + 8) = a2;
    if (a2 != 0) {
        a1 = a2;
        result = strlen(a1, a2, a3, a4);
        a1 = 0xFFFEULL;
        if (result >= 0xFFFFULL) { result = a1; }
        *(unsigned __int16 *)(a1) = (unsigned __int16)(result);
        result = (unsigned __int16)((result) + 1);
        *(unsigned __int16 *)(a1 + 2) = (unsigned __int16)(result);
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t RtlInitAnsiString(void *Arg1, int64_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    *(uint64_t *)(arg1 + 0x8) = Arg2;
    if (Arg2 != 0) {
        Arg1 = Arg2;
        result = strlen(Arg1, Arg2, a3, a4);
        Arg1 = 0xFFFEULL;
        if (result >= 0xFFFFULL) { result = Arg1; }
        *(uint16_t *)(arg1) = (uint16_t)(result);
        result = (uint16_t)((result) + 1);
        *(uint16_t *)(arg1 + 0x2) = (uint16_t)(result);
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `16` | `W` |
| `Arg1` | `+ 0x0` | `64` | `R/W` |
| `Arg1` | `+ 0x2` | `16` | `W` |
| `Arg1` | `+ 0x8` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00470F40&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00470F40[BB_00470F40]
  bb_00470F56[BB_00470F56]
  bb_00470F77[BB_00470F77]
  bb_00470F7D[BB_00470F7D]
  bb_00470F40 -->|branch| bb_00470F77
  bb_00470F40 -->|fallthrough| bb_00470F56
  bb_00470F56 -->|flow| bb_00470F77
```
