# ZwAllocateVirtualMemory

- RVA: `0x006AD3D0`–`0x006AD3EF` (길이 `31` bytes)
- VA: `0x00000001406AD3D0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BFFB0`
- 디코드: `11`개 명령, `31/31` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **24**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [PspWow64ThunkProcessParameters](../49/PspWow64ThunkProcessParameters_function_00490424.md) at `0x004904A9`
- [RtlpCreateHeap](../4E/RtlpCreateHeap_function_004E1904.md) at `0x004E1FFE`
- [RtlpCreateHeap](../4E/RtlpCreateHeap_function_004E1904.md) at `0x004E20D0`
- [RtlpStdExtendLowerWatermark](../5E/RtlpStdExtendLowerWatermark_function_005E6664.md) at `0x005E66FA`
- [RtlpStdExtendUpperWatermark](../5E/RtlpStdExtendUpperWatermark_function_005E674C.md) at `0x005E67E7`
- [RtlpExtendHeap](../5E/RtlpExtendHeap_function_005EA708.md) at `0x005EA823`
- [RtlpExtendHeap](../5E/RtlpExtendHeap_function_005EA708.md) at `0x005EA8A1`
- [RtlpFindAndCommitPages](../5E/RtlpFindAndCommitPages_function_005EA95C.md) at `0x005EAA67`
- [RtlpHpAllocVirtBlockCommitFirst](../5E/RtlpHpAllocVirtBlockCommitFirst_function_005EB0FC.md) at `0x005EB151`
- [RtlpInitializeHeapSegment](../5E/RtlpInitializeHeapSegment_function_005EB1DC.md) at `0x005EB2CF`
- [RtlpHpFixedHeapCommitRoutine](../60/RtlpHpFixedHeapCommitRoutine_function_00603870.md) at `0x0060388E`
- [DifZwAllocateVirtualMemoryWrapper](../63/DifZwAllocateVirtualMemoryWrapper_function_0063D8A0.md) at `0x0063D9B5`
- [VmpUpdateCommitStateMemoryRange](../64/VmpUpdateCommitStateMemoryRange_function_0064D5D0.md) at `0x0064D782`
- [DbgkUserReportWorkRoutine](../../page/71/DbgkUserReportWorkRoutine_function_00710D10.md) at `0x00710DF9`
- [SepAdtCopyToLsaSharedMemory](../../page/7A/SepAdtCopyToLsaSharedMemory_function_007A37EC.md) at `0x007A383A`
- [VmCreateMemoryProcess](../../page/7A/VmCreateMemoryProcess_function_007ACFA0.md) at `0x007AD0DC`
- [PspReserveAndCommitUserShadowStack](../../page/88/PspReserveAndCommitUserShadowStack_function_008827A8.md) at `0x00882885`
- [PspReserveAndCommitUserShadowStack](../../page/88/PspReserveAndCommitUserShadowStack_function_008827A8.md) at `0x008828C5`
- [RtlCreateUserStack](../../page/8C/RtlCreateUserStack_function_008CD908.md) at `0x008CDA78`
- [RtlCreateUserStack](../../page/8C/RtlCreateUserStack_function_008CD908.md) at `0x008CDACE`
- [EtwpFindUserBufferSpace](../../page/9B/EtwpFindUserBufferSpace_function_009BFB14.md) at `0x009BFBD9`
- [RtlpWow64CreateUserStack](../../page/9F/RtlpWow64CreateUserStack_function_009F1300.md) at `0x009F14FE`
- [RtlpWow64CreateUserStack](../../page/9F/RtlpWow64CreateUserStack_function_009F1300.md) at `0x009F154D`
- [PspSchedulerSharedDataRegionSlotAllocate](../../page/A2/PspSchedulerSharedDataRegionSlotAllocate_function_00A268C8.md) at `0x00A26B33`
- [MiCheckForUserStackOverflow](../../page/A3/MiCheckForUserStackOverflow_function_00A30854.md) at `0x00A309BA`
- [ExRaiseHardError](../../page/A6/ExRaiseHardError_function_00A64520.md) at `0x00A64686`
- [PspSetupUserProcessAddressSpace](../../page/AE/PspSetupUserProcessAddressSpace_function_00AEBDC8.md) at `0x00AEBF5F`
- [sub_00B39A5E](../../page/B3/Unknown_function_00B39A5E.md) at `0x00B39AC7`
- [sub_00B3D958](../../page/B3/Unknown_function_00B3D958.md) at `0x00B3D9B0`

### Static image references
- `0x006AD3DC` → RVA `0x006B3460` (`KiServiceLinkage`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006AD3E9` → [KiServiceInternal](../6C/KiServiceInternal_function_006C49C0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006AD3D0  48 8B C4                        mov rax, rsp
006AD3D3  FA                              cli
006AD3D4  48 83 EC 10                     sub rsp, 0x10
006AD3D8  50                              push rax
006AD3D9  9C                              pushfq
006AD3DA  6A 10                           push 0x10
006AD3DC  48 8D 05 7D 60 00 00            lea rax, [rip + 0x607d]
006AD3E3  50                              push rax
006AD3E4  B8 18 00 00 00                  mov eax, 0x18
006AD3E9  E9 D2 75 01 00                  jmp 0x1406c49c0
006AD3EE  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ZwAllocateVirtualMemory(void)
{
    __int64 v_rsp;

    v_rsp = (v_rsp) - (16);
}
```

## 5. (Beta) C Style

```c
void ZwAllocateVirtualMemory(void)
{
    int64_t local_rsp;

    local_rsp = (local_rsp) - (16);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006AD3D0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006AD3D0[BB_006AD3D0]
  bb_006AD3EE[BB_006AD3EE]
```
