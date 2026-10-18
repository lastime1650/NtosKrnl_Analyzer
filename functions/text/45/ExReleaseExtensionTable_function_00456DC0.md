# ExReleaseExtensionTable

- RVA: `0x00456DC0`–`0x00456DEA` (길이 `42` bytes)
- VA: `0x0000000140456DC0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CEE8`
- 디코드: `13`개 명령, `42/42` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **55**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00456DE3` → [ExfReleaseRundownProtection](../34/ExfReleaseRundownProtection_function_00349EB0.md) (function, `0x00349EB0`)

### Direct callers
- [SepLogonSystemManagedAdmin](../../page/70/SepLogonSystemManagedAdmin_function_00704DA4.md) at `0x00704DF0`
- [PspProcessQosChangeNotificationWorker](../../page/78/PspProcessQosChangeNotificationWorker_function_00781740.md) at `0x007819AD`
- [PspNetRateControlDispatch](../../page/78/PspNetRateControlDispatch_function_007850C4.md) at `0x007850F9`
- [BCryptGenerateSymmetricKey](../../page/79/BCryptGenerateSymmetricKey_function_0079C828.md) at `0x0079C89E`
- [BCryptImportKeyPair](../../page/79/BCryptImportKeyPair_function_0079C8C8.md) at `0x0079C931`
- [BCryptSetProperty](../../page/79/BCryptSetProperty_function_0079C950.md) at `0x0079C9B1`
- [LsaCallAuthenticationPackage](../../page/79/LsaCallAuthenticationPackage_function_0079C9E0.md) at `0x0079CA5A`
- [LsaDeregisterLogonProcess](../../page/79/LsaDeregisterLogonProcess_function_0079CA90.md) at `0x0079CAC8`
- [LsaLogonUser](../../page/79/LsaLogonUser_function_0079CAF0.md) at `0x0079CBD3`
- [LsaLookupAuthenticationPackage](../../page/79/LsaLookupAuthenticationPackage_function_0079CC00.md) at `0x0079CC4E`
- [LsaRegisterLogonProcess](../../page/79/LsaRegisterLogonProcess_function_0079CC80.md) at `0x0079CCCE`
- [VmCleanProcessAddressSpace](../../page/7A/VmCleanProcessAddressSpace_function_007ACD38.md) at `0x007ACD94`
- [EtwpDestructIptData](../../page/7C/EtwpDestructIptData_function_007C10DC.md) at `0x007C1122`
- [NtAcquireCrossVmMutant](../../page/7D/NtAcquireCrossVmMutant_function_007D26C0.md) at `0x007D27AD`
- [ExpCreateCrossVmEvent](../../page/7D/ExpCreateCrossVmEvent_function_007D530C.md) at `0x007D53A8`
- [ExpCreateCrossVmMutant](../../page/7D/ExpCreateCrossVmMutant_function_007D53D0.md) at `0x007D546C`
- [ExpCrossVmIntHostCallback](../../page/7D/ExpCrossVmIntHostCallback_function_007D54A0.md) at `0x007D55A0`
- [ExpCrossVmWnfPull](../../page/7D/ExpCrossVmWnfPull_function_007D55BC.md) at `0x007D5607`
- [ExpObCloseCrossVmEvent](../../page/7D/ExpObCloseCrossVmEvent_function_007D5630.md) at `0x007D567D`
- [ExpObCloseCrossVmMutant](../../page/7D/ExpObCloseCrossVmMutant_function_007D56A0.md) at `0x007D56ED`
- [ExpObDeleteCrossVmEvent](../../page/7D/ExpObDeleteCrossVmEvent_function_007D5710.md) at `0x007D573F`
- [ExpObDeleteCrossVmMutant](../../page/7D/ExpObDeleteCrossVmMutant_function_007D5760.md) at `0x007D578F`
- [ExpPulseCrossVmEvent](../../page/7D/ExpPulseCrossVmEvent_function_007D57A4.md) at `0x007D57E6`
- [ExpReleaseCrossVmMutant](../../page/7D/ExpReleaseCrossVmMutant_function_007D5800.md) at `0x007D5842`
- [ExpResetCrossVmEvent](../../page/7D/ExpResetCrossVmEvent_function_007D585C.md) at `0x007D589E`
- [DbgkForwardException](../../page/8A/DbgkForwardException_function_008A2D60.md) at `0x008A303F`
- [BCryptFinishHash](../../page/8D/BCryptFinishHash_function_008D1BB8.md) at `0x008D1C09`
- [BCryptHashData](../../page/8D/BCryptHashData_function_008D1CB4.md) at `0x008D1D08`
- [BCryptDestroyHash](../../page/8D/BCryptDestroyHash_function_008D1D2C.md) at `0x008D1D64`
- [BCryptCreateHash](../../page/8D/BCryptCreateHash_function_008D1D80.md) at `0x008D1DE8`
- [sub_008D1E14](../../page/8D/Unknown_function_008D1E14.md) at `0x008D1EC6`
- [PspCallProcessNotifyRoutines](../../page/90/PspCallProcessNotifyRoutines_function_00904928.md) at `0x009049F2`
- [PspCallProcessNotifyRoutines](../../page/90/PspCallProcessNotifyRoutines_function_00904928.md) at `0x00904B03`
- [ExpNtUpdateWnfStateData](../../page/90/ExpNtUpdateWnfStateData_function_0090A7A0.md) at `0x0090B210`
- [ExpNtUpdateWnfStateData](../../page/90/ExpNtUpdateWnfStateData_function_0090A7A0.md) at `0x0090B264`
- [ExProcessCounterSetCallback](../../page/91/ExProcessCounterSetCallback_function_0091CDF0.md) at `0x0091D1E9`
- [ExpSetCrossVmEvent](../../page/99/ExpSetCrossVmEvent_function_0099C730.md) at `0x0099C78B`
- [NtQueryInformationProcess](../../page/9A/NtQueryInformationProcess_function_009AA250.md) at `0x009AB4DE`
- [NtQueryInformationProcess](../../page/9A/NtQueryInformationProcess_function_009AA250.md) at `0x009ABC60`
- [ExProcessorCounterSetCallback](../../page/9E/ExProcessorCounterSetCallback_function_009E4880.md) at `0x009E4A49`
- [ExProcessorCounterSetCallback](../../page/9E/ExProcessorCounterSetCallback_function_009E4880.md) at `0x009E4C1A`
- [ExProcessorCounterSetCallback](../../page/9E/ExProcessorCounterSetCallback_function_009E4880.md) at `0x009E50B3`
- [ExProcessorCounterSetCallback](../../page/9E/ExProcessorCounterSetCallback_function_009E4880.md) at `0x009E5240`
- [EtwpEventTracingCounterSetCallback](../../page/A0/EtwpEventTracingCounterSetCallback_function_00A0E0C0.md) at `0x00A0E21F`
- [PcwAddInstance](../../page/A0/PcwAddInstance_function_00A0E530.md) at `0x00A0E589`
- [BCryptGetProperty](../../page/A5/BCryptGetProperty_function_00A56158.md) at `0x00A561C1`
- [KiSynchCounterSetCallback](../../page/A5/KiSynchCounterSetCallback_function_00A5F5B0.md) at `0x00A5F699`
- [PcwCreateInstance](../../page/A6/PcwCreateInstance_function_00A610F0.md) at `0x00A61149`
- [PcwRegister](../../page/A6/PcwRegister_function_00A61180.md) at `0x00A611B8`
- [FsRtlAddDiskIOCounterInstance](../../page/A6/FsRtlAddDiskIOCounterInstance_function_00A615C0.md) at `0x00A61689`
- [PcwCloseInstance](../../page/A7/PcwCloseInstance_function_00A705A0.md) at `0x00A705CD`
- [PsSetProcessFaultInformation](../../page/A7/PsSetProcessFaultInformation_function_00A75400.md) at `0x00A754EF`
- [KiSynchNumaCounterSetCallback](../../page/A7/KiSynchNumaCounterSetCallback_function_00A77BE0.md) at `0x00A77DAD`
- [KiSynchNumaCounterSetCallback](../../page/A7/KiSynchNumaCounterSetCallback_function_00A77BE0.md) at `0x00A78138`
- [ExpCrossVmWnfPush](../../page/A8/ExpCrossVmWnfPush_function_00A85A14.md) at `0x00A85A95`
- [PsSetProcessesWindowState](../../page/A9/PsSetProcessesWindowState_function_00A97C80.md) at `0x00A97CBC`
- [BCryptOpenAlgorithmProvider](../../page/AB/BCryptOpenAlgorithmProvider_function_00ABF200.md) at `0x00ABF25C`
- [LsaFreeReturnBuffer](../../page/AC/LsaFreeReturnBuffer_function_00AC3C60.md) at `0x00AC3C98`
- [PcwUnregister](../../page/AC/PcwUnregister_function_00AC41A0.md) at `0x00AC41CD`
- [ExpQueryCrossVmEvent](../../page/AD/ExpQueryCrossVmEvent_function_00AD4B08.md) at `0x00AD4B6E`
- [NtSetInformationProcess](../../page/AE/NtSetInformationProcess_function_00AE5370.md) at `0x00AE92FC`
- [NtSetInformationProcess](../../page/AE/NtSetInformationProcess_function_00AE5370.md) at `0x00AE9336`
- [PspChangeProcessExecutionState](../../page/AE/PspChangeProcessExecutionState_function_00AEC594.md) at `0x00AEC7B0`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00456DC0  48 83 EC 28                     sub rsp, 0x28
00456DC4  48 83 C1 58                     add rcx, 0x58
00456DC8  0F 0D 09                        prefetchw byte ptr [rcx]
00456DCB  48 8B 01                        mov rax, qword ptr [rcx]
00456DCE  48 83 E0 FE                     and rax, 0xfffffffffffffffe
00456DD2  48 8D 50 FE                     lea rdx, [rax - 2]
00456DD6  F0 48 0F B1 11                  lock cmpxchg qword ptr [rcx], rdx
00456DDB  75 06                           jne 0x140456de3
00456DDD  48 83 C4 28                     add rsp, 0x28
00456DE1  C3                              ret
00456DE2  CC                              int3
00456DE3  E8 C8 30 EF FF                  call 0x140349eb0
00456DE8  EB F3                           jmp 0x140456ddd
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExReleaseExtensionTable(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a1 = (a1) + (88);
    result = (*(unsigned __int64 *)(a1)) & (-2);
    if (condition_is_not_equal) goto loc_00456DE3;
loc_00456DDD:
    v_rsp = (v_rsp) + (40);
    return result;
loc_00456DE3:
    result = ExfReleaseRundownProtection(a1, result - 2, a3, a4);
    goto loc_00456DDD;
}
```

## 5. (Beta) C Style

```c
int64_t ExReleaseExtensionTable(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    Arg1 = (Arg1) + (88);
    result = (*(uint64_t *)(arg1)) & (-2);
    if (condition_is_not_equal) goto loc_00456DE3;
loc_00456DDD:
    local_rsp = (local_rsp) + (40);
    return result;
loc_00456DE3:
    result = ExfReleaseRundownProtection(Arg1, result - 2, a3, a4);
    goto loc_00456DDD;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `8` | `R` |
| `Arg1` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00456DC0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00456DC0[BB_00456DC0]
  bb_00456DDD[BB_00456DDD]
  bb_00456DE2[BB_00456DE2]
  bb_00456DE3[BB_00456DE3]
  bb_00456DC0 -->|branch| bb_00456DE3
  bb_00456DC0 -->|fallthrough| bb_00456DDD
  bb_00456DE2 -->|flow| bb_00456DE3
  bb_00456DE3 -->|branch| bb_00456DDD
```
