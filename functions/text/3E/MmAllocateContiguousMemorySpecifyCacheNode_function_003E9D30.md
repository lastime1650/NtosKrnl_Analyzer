# MmAllocateContiguousMemorySpecifyCacheNode

- RVA: `0x003E9D30`–`0x003E9D6F` (길이 `63` bytes)
- VA: `0x00000001403E9D30`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000958CC`
- 디코드: `16`개 명령, `63/63` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x003E9D4E` → [MmAllocateContiguousNodeMemory](MmAllocateContiguousNodeMemory_function_003E9E40.md) (function, `0x003E9E40`)

### Direct callers
- [MmAllocateContiguousMemorySpecifyCache](MmAllocateContiguousMemorySpecifyCache_function_003E9D00.md) at `0x003E9D14`
- [ExtEnvAllocatePhysicalMemory](../56/ExtEnvAllocatePhysicalMemory_function_00561124.md) at `0x0056123F`
- [DifMmAllocateContiguousMemorySpecifyCacheNodeWrapper](../63/DifMmAllocateContiguousMemorySpecifyCacheNodeWrapper_function_00633BE0.md) at `0x00633CF5`
- [DifMmAllocateContiguousMemorySpecifyCacheWrapper](../63/DifMmAllocateContiguousMemorySpecifyCacheWrapper_function_00633D90.md) at `0x00633EA0`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003E9D30  48 83 EC 38                     sub rsp, 0x38
003E9D34  83 7C 24 60 01                  cmp dword ptr [rsp + 0x60], 1
003E9D39  75 1E                           jne 0x1403e9d59
003E9D3B  41 BA 40 00 00 00               mov r10d, 0x40
003E9D41  8B 44 24 68                     mov eax, dword ptr [rsp + 0x68]
003E9D45  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
003E9D49  44 89 54 24 20                  mov dword ptr [rsp + 0x20], r10d
003E9D4E  E8 ED 00 00 00                  call 0x1403e9e40
003E9D53  48 83 C4 38                     add rsp, 0x38
003E9D57  C3                              ret
003E9D58  CC                              int3
003E9D59  83 7C 24 60 02                  cmp dword ptr [rsp + 0x60], 2
003E9D5E  B8 04 04 00 00                  mov eax, 0x404
003E9D63  41 BA 04 02 00 00               mov r10d, 0x204
003E9D69  44 0F 44 D0                     cmove r10d, eax
003E9D6D  EB D2                           jmp 0x1403e9d41
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MmAllocateContiguousMemorySpecifyCacheNode(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned int a5, unsigned int a6)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_rsp;
    unsigned int v_stack_m10;
    unsigned int v_stack_m18;

    v_rsp = (v_rsp) - (56);
    if (a5 != 1) goto loc_003E9D59;
loc_003E9D41:
    v_stack_m10 = (unsigned int)((unsigned int)(a6));
    v_stack_m18 = 64;
    result = MmAllocateContiguousNodeMemory(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (56);
    return result;
loc_003E9D59:
    v_r10 = 516;
    if (a5 == 2) { v_r10 = (unsigned int)((unsigned int)(0x404ULL)); }
    goto loc_003E9D41;
}
```

## 5. (Beta) C Style

```c
int64_t MmAllocateContiguousMemorySpecifyCacheNode(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint32_t Arg5, uint32_t Arg6)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_rsp;
    uint32_t v_stack_m10;
    uint32_t v_stack_m18;

    local_rsp = (local_rsp) - (56);
    if (Arg5 != 1) goto loc_003E9D59;
loc_003E9D41:
    v_stack_m10 = (uint32_t)((uint32_t)(Arg6));
    v_stack_m18 = 64;
    result = MmAllocateContiguousNodeMemory(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (56);
    return result;
loc_003E9D59:
    local_r10 = 516;
    if (Arg5 == 2) { local_r10 = (uint32_t)((uint32_t)(0x404ULL)); }
    goto loc_003E9D41;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003E9D30&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003E9D30[BB_003E9D30]
  bb_003E9D3B[BB_003E9D3B]
  bb_003E9D41[BB_003E9D41]
  bb_003E9D58[BB_003E9D58]
  bb_003E9D59[BB_003E9D59]
  bb_003E9D30 -->|branch| bb_003E9D59
  bb_003E9D30 -->|fallthrough| bb_003E9D3B
  bb_003E9D3B -->|flow| bb_003E9D41
  bb_003E9D58 -->|flow| bb_003E9D59
  bb_003E9D59 -->|branch| bb_003E9D41
```
