# InitializeSListHead

- RVA: `0x00468A90`–`0x00468AB0` (길이 `32` bytes)
- VA: `0x0000000140468A90`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00068784`
- 디코드: `11`개 명령, `32/32` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **35**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00468AAA` → [RtlRaiseStatus](../2F/RtlRaiseStatus_function_002F6A50.md) (function, `0x002F6A50`)

### Direct callers
- [EtwpInitializeApcPool](EtwpInitializeApcPool_function_00467FA0.md) at `0x00467FD0`
- [EtwpInitializeApcPool](EtwpInitializeApcPool_function_00467FA0.md) at `0x00467FD9`
- [ExInitializePagedLookasideListInternal](ExInitializePagedLookasideListInternal_function_00468040.md) at `0x00468065`
- [ST_STORE&lt;SM_TRAITS&gt;::StInitialize](ST_STORE_SM_TRAITS_StInitialize_function_00468158.md) at `0x00468280`
- [ExInitializeNPagedLookasideListInternal](ExInitializeNPagedLookasideListInternal_function_00468720.md) at `0x00468745`
- [ExInitializeLookasideListExInternal](ExInitializeLookasideListExInternal_function_00468890.md) at `0x00468967`
- [EtwpInitializeCompression](../4E/EtwpInitializeCompression_function_004EC774.md) at `0x004EC86C`
- [HvlpSetupCachedHypercallPages](../58/HvlpSetupCachedHypercallPages_function_00586844.md) at `0x00586875`
- [RtlpHpVsSlotCreate](../60/RtlpHpVsSlotCreate_function_006057C0.md) at `0x00605848`
- [SMKM_STORE_MGR&lt;SM_TRAITS&gt;::SmCompressManagerStart](../60/SMKM_STORE_MGR_SM_TRAITS_SmCompressManagerStart_function_0060C418.md) at `0x0060C5FC`
- [SMKM_STORE_MGR&lt;SM_TRAITS&gt;::SmInitialize](../60/SMKM_STORE_MGR_SM_TRAITS_SmInitialize_function_0060C8CC.md) at `0x0060C9C9`
- [MiInitializeNuma](../66/MiInitializeNuma_function_0066E0E0.md) at `0x0066E27C`
- [MiInitializePageFaultResources](../67/MiInitializePageFaultResources_function_0067E490.md) at `0x0067E4CD`
- [MiInitializePageFaultResources](../67/MiInitializePageFaultResources_function_0067E490.md) at `0x0067E4DC`
- [MiPopulateFreeKernelShadowStackCacheEntries](../68/MiPopulateFreeKernelShadowStackCacheEntries_function_006865BC.md) at `0x006865E7`
- [MiAbsorbPossibleEngineChanges](../69/MiAbsorbPossibleEngineChanges_function_006958B4.md) at `0x006958DD`
- [RtlpDynamicLookasideInitialize](../6A/RtlpDynamicLookasideInitialize_function_006A88E8.md) at `0x006A8924`
- [PfTInitialize](../../page/75/PfTInitialize_function_00751554.md) at `0x0075172F`
- [PfFbBufferListInitialize](../../page/75/PfFbBufferListInitialize_function_0075371C.md) at `0x0075375A`
- [PfFbBufferListInitialize](../../page/75/PfFbBufferListInitialize_function_0075371C.md) at `0x00753763`
- [PfFbBufferListInitialize](../../page/75/PfFbBufferListInitialize_function_0075371C.md) at `0x0075376C`
- [RtlStdInitializeStackDatabase](../../page/78/RtlStdInitializeStackDatabase_function_0078C7CC.md) at `0x0078C89D`
- [WdipSemInitializeGlobalState](../../page/7A/WdipSemInitializeGlobalState_function_007AF5FC.md) at `0x007AF67B`
- [WdipSemFreePool](../../page/7B/WdipSemFreePool_function_007B0FC8.md) at `0x007B103E`
- [EtwpCovSampCaptureContextStart](../../page/7C/EtwpCovSampCaptureContextStart_function_007C14AC.md) at `0x007C155C`
- [EtwpCovSampLookasideControlInitialize](../../page/7C/EtwpCovSampLookasideControlInitialize_function_007C1B24.md) at `0x007C1B7E`
- [EtwpCovSampLookasideInitialize](../../page/7C/EtwpCovSampLookasideInitialize_function_007C1BB8.md) at `0x007C1C0A`
- [MiInitializeSections](../../page/7F/MiInitializeSections_function_007FC738.md) at `0x007FC81A`
- [MiInitializePartition](../../page/7F/MiInitializePartition_function_007FD3E8.md) at `0x007FD8EB`
- [MiInitializePartitionFreeZeroLists](../../page/7F/MiInitializePartitionFreeZeroLists_function_007FDA7C.md) at `0x007FDB12`
- [MiCreatePagefile](../../page/7F/MiCreatePagefile_function_007FEC30.md) at `0x007FED29`
- [MmInitializeProcessAddressSpace](../../page/8C/MmInitializeProcessAddressSpace_function_008CF6B0.md) at `0x008CF824`
- [EtwpEnableStackCaching](../../page/A5/EtwpEnableStackCaching_function_00A53C6C.md) at `0x00A53D20`
- [KiInitPrcb](../../pagelk/B6/KiInitPrcb_function_00B66644.md) at `0x00B6679A`
- [PfTAccessTracingInitialize](../../pagelk/B6/PfTAccessTracingInitialize_function_00B6B990.md) at `0x00B6B9CB`
- [ExInitializeSystemLookasideList](../../pagelk/B7/ExInitializeSystemLookasideList_function_00B7E57C.md) at `0x00B7E59B`
- [ViTargetDriversAllocateVerifiedData](../../pagevrfy/B9/ViTargetDriversAllocateVerifiedData_function_00B9B984.md) at `0x00B9B9DF`
- [ViTargetDriversAllocateVerifiedData](../../pagevrfy/B9/ViTargetDriversAllocateVerifiedData_function_00B9B984.md) at `0x00B9B9E8`
- [VfPoolInitPhase1](../../pagevrfy/BA/VfPoolInitPhase1_function_00BAA3E0.md) at `0x00BAA4C5`
- [MiCreateTopLevelUltraMappings](../../init/C6/MiCreateTopLevelUltraMappings_function_00C6CCB0.md) at `0x00C6CDB1`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00468A90  48 83 EC 28                     sub rsp, 0x28
00468A94  F6 C1 0F                        test cl, 0xf
00468A97  75 0C                           jne 0x140468aa5
00468A99  0F 57 C0                        xorps xmm0, xmm0
00468A9C  0F 29 01                        movaps xmmword ptr [rcx], xmm0
00468A9F  48 83 C4 28                     add rsp, 0x28
00468AA3  C3                              ret
00468AA4  CC                              int3
00468AA5  B9 02 00 00 80                  mov ecx, 0x80000002
00468AAA  E8 A1 DF E8 FF                  call 0x1402f6a50
00468AAF  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall InitializeSListHead(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if ((((unsigned __int8)(a1)) & (15)) != 0) goto loc_00468AA5;
    *(unsigned __int64 *)(a1) = v_xmm0;
    v_rsp = (v_rsp) + (40);
    return result;
loc_00468AA5:
    result = RtlRaiseStatus((unsigned int)(0x80000002ULL), a2, a3, a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t InitializeSListHead(int64_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if ((((uint8_t)(Arg1)) & (15)) != 0) goto loc_00468AA5;
    *(uint64_t *)(Arg1) = v_xmm0;
    local_rsp = (local_rsp) + (40);
    return result;
loc_00468AA5:
    result = RtlRaiseStatus((uint32_t)(0x80000002ULL), a2, a3, a4);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00468A90&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00468A90[BB_00468A90]
  bb_00468A99[BB_00468A99]
  bb_00468AA4[BB_00468AA4]
  bb_00468AA5[BB_00468AA5]
  bb_00468A90 -->|branch| bb_00468AA5
  bb_00468A90 -->|fallthrough| bb_00468A99
  bb_00468AA4 -->|flow| bb_00468AA5
```
