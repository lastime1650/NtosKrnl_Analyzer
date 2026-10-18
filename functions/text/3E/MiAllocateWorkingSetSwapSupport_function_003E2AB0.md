# MiAllocateWorkingSetSwapSupport

- RVA: `0x003E2AB0`–`0x003E2AF7` (길이 `71` bytes)
- VA: `0x00000001403E2AB0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008AD5C`
- 디코드: `22`개 명령, `71/71` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x003E2ACF` → [MiAllocatePool](../35/MiAllocatePool_function_0035B540.md) (function, `0x0035B540`)

### Direct callers
- [MmOutSwapWorkingSet](../2A/MmOutSwapWorkingSet_function_002A6BC8.md) at `0x002A6DBE`
- [MmOutSwapWorkingSet](../2A/MmOutSwapWorkingSet_function_002A6BC8.md) at `0x002A702E`
- [MmOutSwapVirtualAddresses](../2A/MmOutSwapVirtualAddresses_function_002A8C30.md) at `0x002A8DC1`
- [MiGetKernelStackSwapSupport](MiGetKernelStackSwapSupport_function_003E2900.md) at `0x003E299B`
- [MiReAllocateWorkingSetSwapSupport](MiReAllocateWorkingSetSwapSupport_function_003E2A58.md) at `0x003E2A69`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003E2AB0  40 53                           push rbx
003E2AB2  48 83 EC 20                     sub rsp, 0x20
003E2AB6  48 8B D1                        mov rdx, rcx
003E2AB9  48 8B D9                        mov rbx, rcx
003E2ABC  48 C1 E2 04                     shl rdx, 4
003E2AC0  B9 40 00 00 00                  mov ecx, 0x40
003E2AC5  48 83 C2 28                     add rdx, 0x28
003E2AC9  41 B8 4D 6D 57 53               mov r8d, 0x53576d4d
003E2ACF  E8 6C 8A F7 FF                  call 0x14035b540
003E2AD4  48 8B D0                        mov rdx, rax
003E2AD7  48 85 C0                        test rax, rax
003E2ADA  74 19                           je 0x1403e2af5
003E2ADC  48 83 C0 2F                     add rax, 0x2f
003E2AE0  48 89 5A 08                     mov qword ptr [rdx + 8], rbx
003E2AE4  48 83 E0 F8                     and rax, 0xfffffffffffffff8
003E2AE8  48 89 02                        mov qword ptr [rdx], rax
003E2AEB  48 8B C2                        mov rax, rdx
003E2AEE  48 83 C4 20                     add rsp, 0x20
003E2AF2  5B                              pop rbx
003E2AF3  C3                              ret
003E2AF4  CC                              int3
003E2AF5  EB F7                           jmp 0x1403e2aee
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiAllocateWorkingSetSwapSupport(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    a2 = (a1) << (4);
    a2 = (a2) + (40);
    result = MiAllocatePool(64, a2, (unsigned int)(0x53576D4DULL), a4);
    if (result == 0) goto loc_003E2AF5;
    result = (result) + (47);
    *(unsigned __int64 *)(result + 8) = a1;
    result = (result) & (-8);
    *(unsigned __int64 *)(result) = result;
loc_003E2AEE:
    v_rsp = (v_rsp) + (32);
    return result;
loc_003E2AF5:
    goto loc_003E2AEE;
}
```

## 5. (Beta) C Style

```c
int64_t MiAllocateWorkingSetSwapSupport(int64_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    a2 = (Arg1) << (4);
    a2 = (a2) + (40);
    result = MiAllocatePool(64, a2, (uint32_t)(0x53576D4DULL), a4);
    if (result == 0) goto loc_003E2AF5;
    result = (result) + (47);
    *(uint64_t *)(result + 0x8) = Arg1;
    result = (result) & (-8);
    *(uint64_t *)(result) = result;
loc_003E2AEE:
    local_rsp = (local_rsp) + (32);
    return result;
loc_003E2AF5:
    goto loc_003E2AEE;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003E2AB0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003E2AB0[BB_003E2AB0]
  bb_003E2ADC[BB_003E2ADC]
  bb_003E2AEE[BB_003E2AEE]
  bb_003E2AF4[BB_003E2AF4]
  bb_003E2AF5[BB_003E2AF5]
  bb_003E2AB0 -->|branch| bb_003E2AF5
  bb_003E2AB0 -->|fallthrough| bb_003E2ADC
  bb_003E2ADC -->|flow| bb_003E2AEE
  bb_003E2AF4 -->|flow| bb_003E2AF5
  bb_003E2AF5 -->|branch| bb_003E2AEE
```
