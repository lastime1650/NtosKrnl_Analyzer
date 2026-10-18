# VmpProcessContextLockExclusive

- RVA: `0x003147A4`–`0x003147E7` (길이 `67` bytes)
- VA: `0x00000001403147A4`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060BE4`
- 디코드: `20`개 명령, `67/67` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **12**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x003147CA` → [ExAcquireSpinLockExclusiveAtDpcLevel](../24/ExAcquireSpinLockExclusiveAtDpcLevel_function_00248E80.md) (function, `0x00248E80`)
- `0x003147E0` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)

### Direct callers
- [VmpFlushTb](VmpFlushTb_function_00311BD0.md) at `0x00311C10`
- [VmpFlushTb](VmpFlushTb_function_00311BD0.md) at `0x00311D8A`
- [sub_003142E3](Unknown_function_003142E3.md) at `0x00314303`
- [VmpSplitMemoryRange](../42/VmpSplitMemoryRange_function_00429754.md) at `0x0042983E`
- [VmpRemoveMemoryRange](../48/VmpRemoveMemoryRange_function_00489018.md) at `0x0048906E`
- [VmpInvalidateSlatBatched](../48/VmpInvalidateSlatBatched_function_00489300.md) at `0x00489482`
- [VmpMergeMemoryRanges](../4D/VmpMergeMemoryRanges_function_004D9EDC.md) at `0x004D9F08`
- [VmpMergeMemoryRanges](../4D/VmpMergeMemoryRanges_function_004D9EDC.md) at `0x004DA0C6`
- [VmpInsertMemoryRange](../64/VmpInsertMemoryRange_function_0064C9F0.md) at `0x0064CA20`
- [VmpPinMemoryRange](../64/VmpPinMemoryRange_function_0064CCD0.md) at `0x0064CD75`
- [VmpPinMemoryRange](../64/VmpPinMemoryRange_function_0064CCD0.md) at `0x0064CEC4`
- [VmpPinMemoryRange](../64/VmpPinMemoryRange_function_0064CCD0.md) at `0x0064CF99`
- [VmpPinMemoryRange](../64/VmpPinMemoryRange_function_0064CCD0.md) at `0x0064D0E8`
- [VmpUnpinMemoryRangeHelper](../64/VmpUnpinMemoryRangeHelper_function_0064D370.md) at `0x0064D3B8`
- [VmpUnpinMemoryRangeHelper](../64/VmpUnpinMemoryRangeHelper_function_0064D370.md) at `0x0064D522`
- [sub_006E0EF0](../6E/Unknown_function_006E0EF0.md) at `0x006E0F05`
- [sub_006E0EF0](../6E/Unknown_function_006E0EF0.md) at `0x006E0F51`
- [sub_006E0EF0](../6E/Unknown_function_006E0EF0.md) at `0x006E0F9D`
- [sub_006E123B](../6E/Unknown_function_006E123B.md) at `0x006E1250`
- [sub_006F5CAE](../6F/Unknown_function_006F5CAE.md) at `0x006F5D6A`

### Static image references
- `0x003147BE` → RVA `0x00FC6D20` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003147A4  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
003147A9  57                              push rdi
003147AA  48 83 EC 20                     sub rsp, 0x20
003147AE  48 8B F9                        mov rdi, rcx
003147B1  44 0F 20 C3                     mov rbx, cr8
003147B5  BA 0F 00 00 00                  mov edx, 0xf
003147BA  44 0F 22 C2                     mov cr8, rdx
003147BE  83 3D 5B 25 CB 00 00            cmp dword ptr [rip + 0xcb255b], 0
003147C5  75 17                           jne 0x1403147de
003147C7  48 8B CF                        mov rcx, rdi
003147CA  E8 B1 46 F3 FF                  call 0x140248e80
003147CF  0F B6 C3                        movzx eax, bl
003147D2  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
003147D7  48 83 C4 20                     add rsp, 0x20
003147DB  5F                              pop rdi
003147DC  C3                              ret
003147DD  CC                              int3
003147DE  8A CB                           mov cl, bl
003147E0  E8 17 0F 1E 00                  call 0x1404f56fc
003147E5  EB E0                           jmp 0x1403147c7
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VmpProcessContextLockExclusive(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    if ((*(unsigned int *)(v_rip + 13313371)) != 0) goto loc_003147DE;
loc_003147C7:
    result = ExAcquireSpinLockExclusiveAtDpcLevel(a1, 15, a3, a4);
    v_rsp = (v_rsp) + (32);
    return (unsigned __int8)(v_cr8);
loc_003147DE:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(v_stack_p8), 15, a3, a4);
    goto loc_003147C7;
}
```

## 5. (Beta) C Style

```c
int64_t VmpProcessContextLockExclusive(int64_t Arg1)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    if ((*(uint32_t *)(v_rip + 0xCB255B)) != 0) goto loc_003147DE;
loc_003147C7:
    result = ExAcquireSpinLockExclusiveAtDpcLevel(Arg1, 15, a3, a4);
    local_rsp = (local_rsp) + (32);
    return (uint8_t)(v_cr8);
loc_003147DE:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(v_stack_p8), 15, a3, a4);
    goto loc_003147C7;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003147A4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003147A4[BB_003147A4]
  bb_003147C7[BB_003147C7]
  bb_003147DD[BB_003147DD]
  bb_003147DE[BB_003147DE]
  bb_003147A4 -->|branch| bb_003147DE
  bb_003147A4 -->|fallthrough| bb_003147C7
  bb_003147DD -->|flow| bb_003147DE
  bb_003147DE -->|branch| bb_003147C7
```
