# MiIsPfnFromChargedSlabAllocation

- RVA: `0x002A2968`–`0x002A29B6` (길이 `78` bytes)
- VA: `0x00000001402A2968`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000685EC`
- 디코드: `19`개 명령, `78/78` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **9**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x002A296F` → [MiGetPfnSlabType](../28/MiGetPfnSlabType_function_0028E2D0.md) (function, `0x0028E2D0`)

### Direct callers
- [MiAllocateKernelStackPages](MiAllocateKernelStackPages_function_002A1BEC.md) at `0x002A218C`
- [MmFreeIndependentPages](MmFreeIndependentPages_function_002A2510.md) at `0x002A25F7`
- [MmAllocateNonChargedSecurePages](../2C/MmAllocateNonChargedSecurePages_function_002C886C.md) at `0x002C898E`
- [MiDeleteShadowStackPtes](../49/MiDeleteShadowStackPtes_function_00493AE4.md) at `0x00493CAC`
- [MmMarkPhysicalMemoryAsBad](../67/MmMarkPhysicalMemoryAsBad_function_0067AA50.md) at `0x0067AD6B`
- [MmAllocateSecureKernelPages](../68/MmAllocateSecureKernelPages_function_0068F394.md) at `0x0068F5D1`
- [MmAllocateIndependentPagesEx](../../page/AA/MmAllocateIndependentPagesEx_function_00AA0CFC.md) at `0x00AA0EDB`
- [MiUpdateBootHpatPagesInUse](../../init/C6/MiUpdateBootHpatPagesInUse_function_00C67548.md) at `0x00C6766B`
- [MiInitializeBootShadowStackPage](../../init/C6/MiInitializeBootShadowStackPage_function_00C67D8C.md) at `0x00C67E1D`

### Static image references
- `0x002A29A0` → RVA `0x00E3D240` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002A2968  48 83 EC 28                     sub rsp, 0x28
002A296C  4C 8B C1                        mov r8, rcx
002A296F  E8 5C B9 FE FF                  call 0x14028e2d0
002A2974  83 F8 09                        cmp eax, 9
002A2977  75 08                           jne 0x1402a2981
002A2979  33 C0                           xor eax, eax
002A297B  48 83 C4 28                     add rsp, 0x28
002A297F  C3                              ret
002A2980  CC                              int3
002A2981  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
002A298B  4C 2B C0                        sub r8, rax
002A298E  48 B8 AB AA AA AA AA AA AA AA   movabs rax, 0xaaaaaaaaaaaaaaab
002A2998  49 C1 F8 04                     sar r8, 4
002A299C  4C 0F AF C0                     imul r8, rax
002A29A0  48 8B 05 99 A8 B9 00            mov rax, qword ptr [rip + 0xb9a899]
002A29A7  49 C1 E8 09                     shr r8, 9
002A29AB  42 0F B6 44 40 01               movzx eax, byte ptr [rax + r8*2 + 1]
002A29B1  C1 E8 07                        shr eax, 7
002A29B4  EB C5                           jmp 0x1402a297b
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiIsPfnFromChargedSlabAllocation(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = MiGetPfnSlabType(a1, a2, a1, a4);
    if (((unsigned int)(result)) != 9) goto loc_002A2981;
    result = 0;
loc_002A297B:
    v_rsp = (v_rsp) + (40);
    return result;
loc_002A2981:
    a3 = (a1) - (0);
    a3 = (a3) >> (4);
    a3 = (a3) * (0);
    a3 = (a3) >> (9);
    result = (unsigned int)((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 12167321) + a3 * 2 + 1)) >> (7));
    goto loc_002A297B;
}
```

## 5. (Beta) C Style

```c
int64_t MiIsPfnFromChargedSlabAllocation(int64_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = MiGetPfnSlabType(Arg1, a2, Arg1, a4);
    if (((uint32_t)(result)) != 9) goto loc_002A2981;
    result = 0;
loc_002A297B:
    local_rsp = (local_rsp) + (40);
    return result;
loc_002A2981:
    a3 = (Arg1) - (0);
    a3 = (a3) >> (4);
    a3 = (a3) * (0);
    a3 = (a3) >> (9);
    result = (uint32_t)((*(uint8_t *)(*(uint64_t *)(v_rip + 0xB9A899) + a3 * 2 + 0x1)) >> (7));
    goto loc_002A297B;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002A2968&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002A2968[BB_002A2968]
  bb_002A2979[BB_002A2979]
  bb_002A297B[BB_002A297B]
  bb_002A2980[BB_002A2980]
  bb_002A2981[BB_002A2981]
  bb_002A2968 -->|branch| bb_002A2981
  bb_002A2968 -->|fallthrough| bb_002A2979
  bb_002A2979 -->|flow| bb_002A297B
  bb_002A2980 -->|flow| bb_002A2981
  bb_002A2981 -->|branch| bb_002A297B
```
