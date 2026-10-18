# SmAllocEx

- RVA: `0x0034C794`–`0x0034C7E8` (길이 `84` bytes)
- VA: `0x000000014034C794`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00078748`
- 디코드: `22`개 명령, `84/84` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **30**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0034C7A9` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0034C7E1` → [ExAllocatePool3](../../poolcode/B8/ExAllocatePool3_function_00B84270.md) (function, `0x00B84270`)

### Direct callers
- [SMKM_STORE_MGR&lt;SM_TRAITS&gt;::SmPageWrite](SMKM_STORE_MGR_SM_TRAITS_SmPageWrite_function_0034BA54.md) at `0x0034BC79`
- [ST_STORE&lt;SM_TRAITS&gt;::StDmCombineRegion](../3B/ST_STORE_SM_TRAITS_StDmCombineRegion_function_003B0E34.md) at `0x003B0F00`
- [SMKM_STORE_MGR&lt;SM_TRAITS&gt;::SmCompressCtxCreateThreadParams](../3B/SMKM_STORE_MGR_SM_TRAITS_SmCompressCtxCreateThreadParams_function_003B2A84.md) at `0x003B2ADF`
- [SMKM_STORE&lt;SM_TRAITS&gt;::SmStOutSwapStore](../49/SMKM_STORE_SM_TRAITS_SmStOutSwapStore_function_00496C84.md) at `0x00496D22`
- [SmFpPreAllocate](../4C/SmFpPreAllocate_function_004CF32C.md) at `0x004CF3D6`
- [SmFpPreAllocate](../4C/SmFpPreAllocate_function_004CF32C.md) at `0x004CF455`
- [SMKM_STORE_MGR&lt;SM_TRAITS&gt;::SmCompressManagerStart](../60/SMKM_STORE_MGR_SM_TRAITS_SmCompressManagerStart_function_0060C418.md) at `0x0060C455`
- [SMKM_STORE_MGR&lt;SM_TRAITS&gt;::SmCompressManagerStart](../60/SMKM_STORE_MGR_SM_TRAITS_SmCompressManagerStart_function_0060C418.md) at `0x0060C4D3`
- [SMKM_STORE_MGR&lt;SM_TRAITS&gt;::SmCompressManagerStart](../60/SMKM_STORE_MGR_SM_TRAITS_SmCompressManagerStart_function_0060C418.md) at `0x0060C5DC`
- [ST_STORE&lt;SM_TRAITS&gt;::StDeviceIoBuild](../60/ST_STORE_SM_TRAITS_StDeviceIoBuild_function_0060CDEC.md) at `0x0060CE9C`
- [ST_STORE&lt;SM_TRAITS&gt;::StDeviceIoBuild](../60/ST_STORE_SM_TRAITS_StDeviceIoBuild_function_0060CDEC.md) at `0x0060CF1E`
- [SMKM_STORE_MGR&lt;SM_TRAITS&gt;::SmStoreContentsRundown](../61/SMKM_STORE_MGR_SM_TRAITS_SmStoreContentsRundown_function_00610ADC.md) at `0x00610B2D`
- [SMKM_STORE_MGR&lt;SM_TRAITS&gt;::SmStoreTerminate](../61/SMKM_STORE_MGR_SM_TRAITS_SmStoreTerminate_function_00610BD4.md) at `0x00610C06`
- [SmRecordDecompressionFailureDumpPayload](../61/SmRecordDecompressionFailureDumpPayload_function_00611120.md) at `0x00611160`
- [SmRecordDecompressionFailureDumpPayload](../61/SmRecordDecompressionFailureDumpPayload_function_00611120.md) at `0x006111A8`
- [sub_006E708E](../6E/Unknown_function_006E708E.md) at `0x006E709D`
- [sub_006E708E](../6E/Unknown_function_006E708E.md) at `0x006E70C7`
- [SmProcessListRequest](../../page/7A/SmProcessListRequest_function_007A67A8.md) at `0x007A67E6`
- [SmProcessStatsRequest](../../page/7A/SmProcessStatsRequest_function_007A6E68.md) at `0x007A6FE3`
- [SmProcessStatsRequest](../../page/7A/SmProcessStatsRequest_function_007A6E68.md) at `0x007A700D`
- [SmcProcessCreateRequest](../../page/7A/SmcProcessCreateRequest_function_007A764C.md) at `0x007A77BB`
- [SmKmKeyGenNewKey](../../page/7A/SmKmKeyGenNewKey_function_007A8990.md) at `0x007A89E9`
- [SmKmKeyGenStart](../../page/7A/SmKmKeyGenStart_function_007A8BA0.md) at `0x007A8BD6`
- [SmKmStoreFileWriteHeader](../../page/7A/SmKmStoreFileWriteHeader_function_007A9DB4.md) at `0x007A9E20`
- [SmCrEncStart](../../page/7A/SmCrEncStart_function_007AA208.md) at `0x007AA295`
- [SmCrEncStart](../../page/7A/SmCrEncStart_function_007AA208.md) at `0x007AA2DF`
- [SmCrEncStart](../../page/7A/SmCrEncStart_function_007AA208.md) at `0x007AA32D`
- [SmHwAcceleratorCreate](../../page/7A/SmHwAcceleratorCreate_function_007AA40C.md) at `0x007AA480`
- [SmHwAcceleratorCreate](../../page/7A/SmHwAcceleratorCreate_function_007AA40C.md) at `0x007AA580`
- [SmHwAcceleratorMgrAcquireAccelerators](../../page/7A/SmHwAcceleratorMgrAcquireAccelerators_function_007AA628.md) at `0x007AA825`
- [SmHwAcceleratorMgrAcquireAccelerators](../../page/7A/SmHwAcceleratorMgrAcquireAccelerators_function_007AA628.md) at `0x007AA8CE`
- [SmHwAcceleratorParitionCtxCreate](../../page/7A/SmHwAcceleratorParitionCtxCreate_function_007AB0A8.md) at `0x007AB186`
- [SmHwAcceleratorPartitionMgrStart](../../page/7A/SmHwAcceleratorPartitionMgrStart_function_007AB480.md) at `0x007AB4E8`
- [SmcStoreCreate](../../page/7A/SmcStoreCreate_function_007ABFB4.md) at `0x007AC12C`
- [SmcStoreResize](../../page/7A/SmcStoreResize_function_007AC500.md) at `0x007AC58A`
- [SmcStoreSlotReserve](../../page/7A/SmcStoreSlotReserve_function_007AC978.md) at `0x007AC9BC`
- [SmpKeyedStoreCreate](../../page/A5/SmpKeyedStoreCreate_function_00A50B64.md) at `0x00A50C09`
- [SmProcessCreateRequest](../../page/A5/SmProcessCreateRequest_function_00A50DD0.md) at `0x00A51008`
- [SmProcessCreateRequest](../../page/A5/SmProcessCreateRequest_function_00A50DD0.md) at `0x00A5121F`
- [SmKmStoreAdd](../../page/A5/SmKmStoreAdd_function_00A512D0.md) at `0x00A5151B`
- [SmKmFileInfoDuplicate](../../page/AC/SmKmFileInfoDuplicate_function_00AC98FC.md) at `0x00AC99F9`
- [sub_00B3B882](../../page/B3/Unknown_function_00B3B882.md) at `0x00B3B8DE`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x0034C7A9` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
  - `0x0034C7E1` → [ExAllocatePool3](../../poolcode/B8/ExAllocatePool3_function_00B84270.md) (`.text` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0034C794  48 83 EC 48                     sub rsp, 0x48
0034C798  41 83 F8 FF                     cmp r8d, -1
0034C79C  75 16                           jne 0x14034c7b4
0034C79E  44 8B C2                        mov r8d, edx
0034C7A1  48 8B D1                        mov rdx, rcx
0034C7A4  B9 40 00 00 00                  mov ecx, 0x40
0034C7A9  E8 42 59 83 00                  call 0x140b820f0
0034C7AE  48 83 C4 48                     add rsp, 0x48
0034C7B2  C3                              ret
0034C7B3  CC                              int3
0034C7B4  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
0034C7BA  4C 8D 4C 24 30                  lea r9, [rsp + 0x30]
0034C7BF  33 C0                           xor eax, eax
0034C7C1  C6 44 24 30 03                  mov byte ptr [rsp + 0x30], 3
0034C7C6  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0034C7CB  44 89 44 24 38                  mov dword ptr [rsp + 0x38], r8d
0034C7D0  44 8B C2                        mov r8d, edx
0034C7D3  48 8B D1                        mov rdx, rcx
0034C7D6  C7 44 24 20 01 00 00 00         mov dword ptr [rsp + 0x20], 1
0034C7DE  8D 48 40                        lea ecx, [rax + 0x40]
0034C7E1  E8 8A 7A 83 00                  call 0x140b84270
0034C7E6  EB C6                           jmp 0x14034c7ae
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SmAllocEx(__int64 a1, int a2, int a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;

    v_rsp = (v_rsp) - (72);
    if (a3 != -1) goto loc_0034C7B4;
    result = ExAllocatePool2(64, a1, (unsigned int)(a2), a4);
loc_0034C7AE:
    v_rsp = (v_rsp) + (72);
    return result;
loc_0034C7B4:
    result = 0;
    v_stack_p30 = 3;
    v_stack_p38 = 0;
    v_stack_p38 = (unsigned int)((unsigned int)(a2));
    v_stack_p20 = 1;
    result = ExAllocatePool3(result + 64, 64, (unsigned int)((unsigned int)(a1)), v_stack_p30);
    goto loc_0034C7AE;
}
```

## 5. (Beta) C Style

```c
int64_t SmAllocEx(int64_t Arg1, int32_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_p20;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;

    local_rsp = (local_rsp) - (72);
    if (Arg3 != -1) goto loc_0034C7B4;
    result = ExAllocatePool2(64, Arg1, (uint32_t)(Arg2), a4);
loc_0034C7AE:
    local_rsp = (local_rsp) + (72);
    return result;
loc_0034C7B4:
    result = 0;
    v_stack_p30 = 3;
    v_stack_p38 = 0;
    v_stack_p38 = (uint32_t)((uint32_t)(Arg2));
    v_stack_p20 = 1;
    result = ExAllocatePool3(result + 64, 64, (uint32_t)((uint32_t)(Arg1)), v_stack_p30);
    goto loc_0034C7AE;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0034C794&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0034C794[BB_0034C794]
  bb_0034C79E[BB_0034C79E]
  bb_0034C7AE[BB_0034C7AE]
  bb_0034C7B3[BB_0034C7B3]
  bb_0034C7B4[BB_0034C7B4]
  bb_0034C794 -->|branch| bb_0034C7B4
  bb_0034C794 -->|fallthrough| bb_0034C79E
  bb_0034C79E -->|flow| bb_0034C7AE
  bb_0034C7B3 -->|flow| bb_0034C7B4
  bb_0034C7B4 -->|branch| bb_0034C7AE
```
