# MiGetNextPageTable

- RVA: `0x002C2EE0`–`0x002C2EF5` (길이 `21` bytes)
- VA: `0x00000001402C2EE0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006E92C`
- 디코드: `6`개 명령, `21/21` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **15**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [MiCloneVads](../22/MiCloneVads_function_0022DC1C.md) at `0x0022DF1A`
- [MiMakeHyperRangeAccessible](../27/MiMakeHyperRangeAccessible_function_0027CE10.md) at `0x0027CFD6`
- [MiSplitPrivatePage](../2A/MiSplitPrivatePage_function_002A6210.md) at `0x002A62EC`
- [NtGetWriteWatch](../2A/NtGetWriteWatch_function_002A7CE0.md) at `0x002A811A`
- [MiMoveDirtyBitsToPfns](../2A/MiMoveDirtyBitsToPfns_function_002A8624.md) at `0x002A871B`
- [MiIsCfgBitMapPageShared](MiIsCfgBitMapPageShared_function_002C1200.md) at `0x002C1278`
- [MiCountSharedPages](MiCountSharedPages_function_002C30A4.md) at `0x002C310B`
- [MiComputePageCommitment](MiComputePageCommitment_function_002C5C34.md) at `0x002C5D04`
- [NtLockVirtualMemory](../40/NtLockVirtualMemory_function_004088A0.md) at `0x00408DA7`
- [sub_0044565B](../44/Unknown_function_0044565B.md) at `0x00445689`
- [MiCloneCaptureVadCommit](../4B/MiCloneCaptureVadCommit_function_004B4554.md) at `0x004B465C`
- [MiCheckCommitReleaseFromVad](../66/MiCheckCommitReleaseFromVad_function_0066EB90.md) at `0x0066EC39`
- [MiGetNextNonGapPfnPage](../67/MiGetNextNonGapPfnPage_function_006728D8.md) at `0x006729F0`
- [MiQueryVaPhysicalContiguity](../68/MiQueryVaPhysicalContiguity_function_006875B8.md) at `0x006876C3`
- [MiMakeVaRangePhysicallyContiguous](../69/MiMakeVaRangePhysicallyContiguous_function_006936E0.md) at `0x006937AC`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002C2EE0  48 89 6C 24 18                  mov qword ptr [rsp + 0x18], rbp
002C2EE5  57                              push rdi
002C2EE6  41 56                           push r14
002C2EE8  41 57                           push r15
002C2EEA  48 81 EC F0 00 00 00            sub rsp, 0xf0
002C2EF1  45 0F B6 F0                     movzx r14d, r8b
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall MiGetNextPageTable(__int64 a1, __int64 a2, unsigned __int8 a3)
{
    __int64 v_rsp;
    unsigned __int64 v_stack_p18;

    v_stack_p18 = v_rbp;
    v_rsp = (v_rsp) - (240);
    return;
}
```

## 5. (Beta) C Style

```c
void MiGetNextPageTable(int64_t Arg1, int64_t Arg2, uint8_t Arg3)
{
    int64_t local_rsp;
    uint64_t v_stack_p18;

    v_stack_p18 = local_rbp;
    local_rsp = (local_rsp) - (240);
    return;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002C2EE0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002C2EE0[BB_002C2EE0]
```
