# VmpProcessContextLockShared

- RVA: `0x00429DB0`–`0x00429DF3` (길이 `67` bytes)
- VA: `0x0000000140429DB0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060BE4`
- 디코드: `20`개 명령, `67/67` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **7**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00429DD6` → [ExAcquireSpinLockSharedAtDpcLevel](../24/ExAcquireSpinLockSharedAtDpcLevel_function_00248E30.md) (function, `0x00248E30`)
- `0x00429DEC` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)

### Direct callers
- [VmpPrefetchVirtualAddresses](VmpPrefetchVirtualAddresses_function_00428844.md) at `0x004288E0`
- [VmpPrefetchVirtualAddresses](VmpPrefetchVirtualAddresses_function_00428844.md) at `0x004289A2`
- [VmpQueryAccessedState](VmpQueryAccessedState_function_004290A8.md) at `0x00429136`
- [VmpAccessFaultBatch](VmpAccessFaultBatch_function_00429398.md) at `0x00429417`
- [VmpSplitMemoryRange](VmpSplitMemoryRange_function_00429754.md) at `0x004297AC`
- [VmColdPagesHint](VmColdPagesHint_function_00429BB0.md) at `0x00429C1E`
- [VmpUpdateCommitStateMemoryRange](../64/VmpUpdateCommitStateMemoryRange_function_0064D5D0.md) at `0x0064D619`
- [sub_006EDFF2](../6E/Unknown_function_006EDFF2.md) at `0x006EE031`

### Static image references
- `0x00429DCA` → RVA `0x00FC6D20` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00429DB0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00429DB5  57                              push rdi
00429DB6  48 83 EC 20                     sub rsp, 0x20
00429DBA  48 8B F9                        mov rdi, rcx
00429DBD  44 0F 20 C3                     mov rbx, cr8
00429DC1  BA 0F 00 00 00                  mov edx, 0xf
00429DC6  44 0F 22 C2                     mov cr8, rdx
00429DCA  83 3D 4F CF B9 00 00            cmp dword ptr [rip + 0xb9cf4f], 0
00429DD1  75 17                           jne 0x140429dea
00429DD3  48 8B CF                        mov rcx, rdi
00429DD6  E8 55 F0 E1 FF                  call 0x140248e30
00429DDB  0F B6 C3                        movzx eax, bl
00429DDE  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00429DE3  48 83 C4 20                     add rsp, 0x20
00429DE7  5F                              pop rdi
00429DE8  C3                              ret
00429DE9  CC                              int3
00429DEA  8A CB                           mov cl, bl
00429DEC  E8 0B B9 0C 00                  call 0x1404f56fc
00429DF1  EB E0                           jmp 0x140429dd3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VmpProcessContextLockShared(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    if ((*(unsigned int *)(v_rip + 12177231)) != 0) goto loc_00429DEA;
loc_00429DD3:
    result = ExAcquireSpinLockSharedAtDpcLevel(a1, 15, a3, a4);
    v_rsp = (v_rsp) + (32);
    return (unsigned __int8)(v_cr8);
loc_00429DEA:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(v_stack_p8), 15, a3, a4);
    goto loc_00429DD3;
}
```

## 5. (Beta) C Style

```c
int64_t VmpProcessContextLockShared(int64_t Arg1)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    if ((*(uint32_t *)(v_rip + 0xB9CF4F)) != 0) goto loc_00429DEA;
loc_00429DD3:
    result = ExAcquireSpinLockSharedAtDpcLevel(Arg1, 15, a3, a4);
    local_rsp = (local_rsp) + (32);
    return (uint8_t)(v_cr8);
loc_00429DEA:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(v_stack_p8), 15, a3, a4);
    goto loc_00429DD3;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00429DB0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00429DB0[BB_00429DB0]
  bb_00429DD3[BB_00429DD3]
  bb_00429DE9[BB_00429DE9]
  bb_00429DEA[BB_00429DEA]
  bb_00429DB0 -->|branch| bb_00429DEA
  bb_00429DB0 -->|fallthrough| bb_00429DD3
  bb_00429DE9 -->|flow| bb_00429DEA
  bb_00429DEA -->|branch| bb_00429DD3
```
