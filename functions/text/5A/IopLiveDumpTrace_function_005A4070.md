# IopLiveDumpTrace

- RVA: `0x005A4070`–`0x005A40AD` (길이 `61` bytes)
- VA: `0x00000001405A4070`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00063458`
- 디코드: `16`개 명령, `61/61` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **26**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x005A4074` → [IopLiveDumpIsTracingEnabled](../4F/IopLiveDumpIsTracingEnabled_function_004FC5AC.md) (function, `0x004FC5AC`)
- `0x005A40A2` → [EtwWriteEx](../25/EtwWriteEx_function_0025F0D0.md) (function, `0x0025F0D0`)

### Direct callers
- [IopLiveDumpTraceEstimatedAndAllocatedPageCount](../3F/IopLiveDumpTraceEstimatedAndAllocatedPageCount_function_003F59B8.md) at `0x003F5AC6`
- [IopLiveDumpAllocateExtraBuffers](../59/IopLiveDumpAllocateExtraBuffers_function_00599A9C.md) at `0x00599BF1`
- [IopLiveDumpAllocateFromVMMemoryPartition](../59/IopLiveDumpAllocateFromVMMemoryPartition_function_0059A2D8.md) at `0x0059A3D4`
- [IopLiveDumpCallRemovePagesCallbacks](../59/IopLiveDumpCallRemovePagesCallbacks_function_0059AC28.md) at `0x0059AD87`
- [IopLiveDumpCallRemovePagesCallbacks](../59/IopLiveDumpCallRemovePagesCallbacks_function_0059AC28.md) at `0x0059AF21`
- [IopLiveDumpCaptureDumpStart](../59/IopLiveDumpCaptureDumpStart_function_0059B02C.md) at `0x0059B082`
- [IopLiveDumpEstimateMemoryPages](../59/IopLiveDumpEstimateMemoryPages_function_0059BA80.md) at `0x0059BC05`
- [IopLiveDumpMarkImportantDumpData](../59/IopLiveDumpMarkImportantDumpData_function_0059CCA4.md) at `0x0059CDBF`
- [IopLiveDumpOpenVMMemoryPartition](../59/IopLiveDumpOpenVMMemoryPartition_function_0059D508.md) at `0x0059D607`
- [IopLiveDumpPolicyChangeWnfCallback](../59/IopLiveDumpPolicyChangeWnfCallback_function_0059D6E0.md) at `0x0059D833`
- [IopLiveDumpPolicyChangeWnfCallback](../59/IopLiveDumpPolicyChangeWnfCallback_function_0059D6E0.md) at `0x0059D917`
- [IopLiveDumpRegisterWnfNotificationCallback](../59/IopLiveDumpRegisterWnfNotificationCallback_function_0059DE08.md) at `0x0059DE89`
- [IopLiveDumpTraceBufferAllocation](../59/IopLiveDumpTraceBufferAllocation_function_0059E290.md) at `0x0059E379`
- [IopLiveDumpTraceBufferEstimation](../59/IopLiveDumpTraceBufferEstimation_function_0059E39C.md) at `0x0059E4EA`
- [IopLiveDumpTraceCaptureGenerateIptSecondaryDataDuration](../59/IopLiveDumpTraceCaptureGenerateIptSecondaryDataDuration_function_0059E50C.md) at `0x0059E57F`
- [IopLiveDumpTraceCaptureMemoryPages](../59/IopLiveDumpTraceCaptureMemoryPages_function_0059E638.md) at `0x0059E6F6`
- [IopLiveDumpTraceCaptureProcessorContextDuration](../59/IopLiveDumpTraceCaptureProcessorContextDuration_function_0059E718.md) at `0x0059E79B`
- [IopLiveDumpTraceCorralProcessorsDuration](../59/IopLiveDumpTraceCorralProcessorsDuration_function_0059E854.md) at `0x0059E910`
- [IopLiveDumpTraceDumpDisabledOnBoot](../59/IopLiveDumpTraceDumpDisabledOnBoot_function_0059EA10.md) at `0x0059EA5B`
- [IopLiveDumpTraceDumpFileWriteEnd](../59/IopLiveDumpTraceDumpFileWriteEnd_function_0059EB00.md) at `0x0059EC02`
- [IopLiveDumpTraceInterfaceEnd](../59/IopLiveDumpTraceInterfaceEnd_function_0059EC24.md) at `0x0059EDE8`
- [IopLiveDumpTraceMarkImportantDumpDataDuration](../59/IopLiveDumpTraceMarkImportantDumpDataDuration_function_0059EE44.md) at `0x0059EEC7`
- [IopLiveDumpTraceMarkRequiredDumpDataDuration](../59/IopLiveDumpTraceMarkRequiredDumpDataDuration_function_0059EF80.md) at `0x0059F003`
- [IopLiveDumpTraceMmDuplicateMemoryFailure](../59/IopLiveDumpTraceMmDuplicateMemoryFailure_function_0059F0BC.md) at `0x0059F137`
- [IopLiveDumpTracePopulateBitmapForDumpDuration](../59/IopLiveDumpTracePopulateBitmapForDumpDuration_function_0059F158.md) at `0x0059F1EB`
- [IopLiveDumpTraceRemovePagesCallbackFailure](../59/IopLiveDumpTraceRemovePagesCallbackFailure_function_0059F2AC.md) at `0x0059F303`
- [IopLiveDumpTraceUncorralProcessorsDuration](../59/IopLiveDumpTraceUncorralProcessorsDuration_function_0059F324.md) at `0x0059F3E0`
- [IopLiveDumpTraceNoArgs](IopLiveDumpTraceNoArgs_function_005A43C0.md) at `0x005A43D2`

### Static image references
- `0x005A409B` → RVA `0x00E66228` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005A4070  48 83 EC 48                     sub rsp, 0x48
005A4074  E8 33 85 F5 FF                  call 0x1404fc5ac
005A4079  84 C0                           test al, al
005A407B  74 2A                           je 0x1405a40a7
005A407D  4C 89 44 24 38                  mov qword ptr [rsp + 0x38], r8
005A4082  45 33 C9                        xor r9d, r9d
005A4085  89 54 24 30                     mov dword ptr [rsp + 0x30], edx
005A4089  45 33 C0                        xor r8d, r8d
005A408C  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
005A4092  48 8B D1                        mov rdx, rcx
005A4095  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
005A409B  48 8B 0D 86 21 8C 00            mov rcx, qword ptr [rip + 0x8c2186]
005A40A2  E8 29 B0 CB FF                  call 0x14025f0d0
005A40A7  48 83 C4 48                     add rsp, 0x48
005A40AB  C3                              ret
005A40AC  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IopLiveDumpTrace(__int64 a1, int a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned int v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;

    v_rsp = (v_rsp) - (72);
    result = IopLiveDumpIsTracingEnabled(a1, a2, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        v_stack_m10 = a3;
        a4 = 0;
        v_stack_m18 = a2;
        a3 = 0;
        a2 = a1;
        a1 = *(unsigned __int64 *)(v_rip + 9183622);
        result = EtwWriteEx(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (72);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t IopLiveDumpTrace(int64_t Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint32_t v_stack_m18;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;

    local_rsp = (local_rsp) - (72);
    result = IopLiveDumpIsTracingEnabled(Arg1, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        v_stack_m10 = Arg3;
        Arg4 = 0;
        v_stack_m18 = Arg2;
        Arg3 = 0;
        Arg2 = Arg1;
        Arg1 = *(uint64_t *)(v_rip + 0x8C2186);
        result = EtwWriteEx(Arg1, Arg2, Arg3, Arg4);
    }
    local_rsp = (local_rsp) + (72);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005A4070&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005A4070[BB_005A4070]
  bb_005A407D[BB_005A407D]
  bb_005A40A7[BB_005A40A7]
  bb_005A40AC[BB_005A40AC]
  bb_005A4070 -->|branch| bb_005A40A7
  bb_005A4070 -->|fallthrough| bb_005A407D
  bb_005A407D -->|flow| bb_005A40A7
```
