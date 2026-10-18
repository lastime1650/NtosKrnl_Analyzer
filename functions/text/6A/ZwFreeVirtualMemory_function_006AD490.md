# ZwFreeVirtualMemory

- RVA: `0x006AD490`–`0x006AD4AF` (길이 `31` bytes)
- VA: `0x00000001406AD490`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BFFF8`
- 디코드: `11`개 명령, `31/31` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **20**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [SepRmDispatchDataToLsa](../22/SepRmDispatchDataToLsa_function_0022395C.md) at `0x00223B74`
- [RtlpCreateHeap](../4E/RtlpCreateHeap_function_004E1904.md) at `0x004E2043`
- [RtlpCreateHeap](../4E/RtlpCreateHeap_function_004E1904.md) at `0x004E226F`
- [RtlpDeCommitFreeBlock](../5E/RtlpDeCommitFreeBlock_function_005EA158.md) at `0x005EA36D`
- [RtlpDeCommitFreeBlock](../5E/RtlpDeCommitFreeBlock_function_005EA158.md) at `0x005EA58F`
- [RtlpExtendHeap](../5E/RtlpExtendHeap_function_005EA708.md) at `0x005EA940`
- [RtlpFreeHeap](../5E/RtlpFreeHeap_function_005EABC0.md) at `0x005EB0D5`
- [RtlpHpAllocVirtBlockCommitFirst](../5E/RtlpHpAllocVirtBlockCommitFirst_function_005EB0FC.md) at `0x005EB171`
- [RtlpHpAllocVirtBlockCommitFirst](../5E/RtlpHpAllocVirtBlockCommitFirst_function_005EB0FC.md) at `0x005EB1A4`
- [DifZwFreeVirtualMemoryWrapper](../64/DifZwFreeVirtualMemoryWrapper_function_006424F0.md) at `0x006425E3`
- [VmpUpdateCommitStateMemoryRange](../64/VmpUpdateCommitStateMemoryRange_function_0064D5D0.md) at `0x0064D768`
- [DbgkUserReportWorkRoutine](../../page/71/DbgkUserReportWorkRoutine_function_00710D10.md) at `0x00710FBB`
- [RtlpDestroyHeapSegment](../../page/79/RtlpDestroyHeapSegment_function_00790F88.md) at `0x00790FF5`
- [SepAdtCopyToLsaSharedMemory](../../page/7A/SepAdtCopyToLsaSharedMemory_function_007A37EC.md) at `0x007A3887`
- [EtwpFreeUserBufferSpace](../../page/7C/EtwpFreeUserBufferSpace_function_007C0C08.md) at `0x007C0C79`
- [PspSetupUserStack](../../page/8C/PspSetupUserStack_function_008CD794.md) at `0x008CD8CC`
- [RtlCreateUserStack](../../page/8C/RtlCreateUserStack_function_008CD908.md) at `0x008CDB95`
- [PspExitThread](../../page/90/PspExitThread_function_00905F60.md) at `0x00906352`
- [PspExitThread](../../page/90/PspExitThread_function_00905F60.md) at `0x009063B7`
- [sub_009A0BF0](../../page/9A/Unknown_function_009A0BF0.md) at `0x009A0C86`
- [RtlpWow64CreateUserStack](../../page/9F/RtlpWow64CreateUserStack_function_009F1300.md) at `0x009F15AA`
- [ExRaiseHardError](../../page/A6/ExRaiseHardError_function_00A64520.md) at `0x00A64826`
- [PspDeleteUserStack](../../page/A7/PspDeleteUserStack_function_00A78D18.md) at `0x00A78D80`
- [PspDeleteUserStack](../../page/A7/PspDeleteUserStack_function_00A78D18.md) at `0x00A78DA8`
- [sub_00B4A4E4](../../page/B4/Unknown_function_00B4A4E4.md) at `0x00B4A51B`

### Static image references
- `0x006AD49C` → RVA `0x006B3460` (`KiServiceLinkage`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006AD4A9` → [KiServiceInternal](../6C/KiServiceInternal_function_006C49C0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006AD490  48 8B C4                        mov rax, rsp
006AD493  FA                              cli
006AD494  48 83 EC 10                     sub rsp, 0x10
006AD498  50                              push rax
006AD499  9C                              pushfq
006AD49A  6A 10                           push 0x10
006AD49C  48 8D 05 BD 5F 00 00            lea rax, [rip + 0x5fbd]
006AD4A3  50                              push rax
006AD4A4  B8 1E 00 00 00                  mov eax, 0x1e
006AD4A9  E9 12 75 01 00                  jmp 0x1406c49c0
006AD4AE  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ZwFreeVirtualMemory(void)
{
    __int64 v_rsp;

    v_rsp = (v_rsp) - (16);
}
```

## 5. (Beta) C Style

```c
void ZwFreeVirtualMemory(void)
{
    int64_t local_rsp;

    local_rsp = (local_rsp) - (16);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006AD490&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006AD490[BB_006AD490]
  bb_006AD4AE[BB_006AD4AE]
```
