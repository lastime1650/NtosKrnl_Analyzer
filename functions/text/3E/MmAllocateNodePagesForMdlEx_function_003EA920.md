# MmAllocateNodePagesForMdlEx

- RVA: `0x003EA920`–`0x003EA950` (길이 `48` bytes)
- VA: `0x00000001403EA920`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00063458`
- 디코드: `12`개 명령, `48/48` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **8**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x003EA945` → [MmAllocatePartitionNodePagesForMdlEx](MmAllocatePartitionNodePagesForMdlEx_function_003EA960.md) (function, `0x003EA960`)

### Direct callers
- [HalpAllocateCommonBufferVectorInternal](HalpAllocateCommonBufferVectorInternal_function_003E848C.md) at `0x003E86B0`
- [HalpAllocateDomainCommonBufferInternal](HalpAllocateDomainCommonBufferInternal_function_003E8B64.md) at `0x003E8E06`
- [HalpAllocateCommonBufferDmarThin](HalpAllocateCommonBufferDmarThin_function_003E8FF0.md) at `0x003E90D7`
- [MmAllocatePagesForMdlEx](MmAllocatePagesForMdlEx_function_003EA8C0.md) at `0x003EA902`
- [HvlpDepositPages](../58/HvlpDepositPages_function_00585474.md) at `0x0058550F`
- [DifMmAllocateNodePagesForMdlExWrapper](../63/DifMmAllocateNodePagesForMdlExWrapper_function_00634560.md) at `0x0063467B`
- [sub_006EABA2](../6E/Unknown_function_006EABA2.md) at `0x006EABD6`
- [KiComputeNumaCosts](../../init/C3/KiComputeNumaCosts_function_00C37AD4.md) at `0x00C37D2C`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003EA920  48 83 EC 48                     sub rsp, 0x48
003EA924  48 83 64 24 38 00               and qword ptr [rsp + 0x38], 0
003EA92A  8B 84 24 80 00 00 00            mov eax, dword ptr [rsp + 0x80]
003EA931  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
003EA935  8B 44 24 78                     mov eax, dword ptr [rsp + 0x78]
003EA939  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
003EA93D  8B 44 24 70                     mov eax, dword ptr [rsp + 0x70]
003EA941  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
003EA945  E8 16 00 00 00                  call 0x1403ea960
003EA94A  48 83 C4 48                     add rsp, 0x48
003EA94E  C3                              ret
003EA94F  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MmAllocateNodePagesForMdlEx(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned int a5, unsigned int a6, unsigned int a7)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned int v_stack_m18;
    unsigned int v_stack_m20;
    unsigned int v_stack_m28;

    v_rsp = (v_rsp) - (72);
    v_stack_m18 = (unsigned int)((unsigned int)(a7));
    v_stack_m20 = (unsigned int)((unsigned int)(a6));
    v_stack_m28 = (unsigned int)((unsigned int)(a5));
    result = MmAllocatePartitionNodePagesForMdlEx(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (72);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MmAllocateNodePagesForMdlEx(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint32_t Arg5, uint32_t Arg6, uint32_t Arg7)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint32_t v_stack_m18;
    uint32_t v_stack_m20;
    uint32_t v_stack_m28;

    local_rsp = (local_rsp) - (72);
    v_stack_m18 = (uint32_t)((uint32_t)(Arg7));
    v_stack_m20 = (uint32_t)((uint32_t)(Arg6));
    v_stack_m28 = (uint32_t)((uint32_t)(Arg5));
    result = MmAllocatePartitionNodePagesForMdlEx(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (72);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003EA920&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003EA920[BB_003EA920]
  bb_003EA94F[BB_003EA94F]
```
