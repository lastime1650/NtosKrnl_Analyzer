# MiDiscardTransitionPteEx

- RVA: `0x00375954`–`0x003759E1` (길이 `141` bytes)
- VA: `0x0000000140375954`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060BC4`
- 디코드: `34`개 명령, `141/141` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **18**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0037598C` → [MiRestoreTransitionPte](../33/MiRestoreTransitionPte_function_0033DD90.md) (function, `0x0033DD90`)
- `0x003759A9` → [MiClearPfnReuseFields](MiClearPfnReuseFields_function_003759F0.md) (function, `0x003759F0`)
- `0x003759CB` → [MiInsertPageInFreeOrZeroedList](../33/MiInsertPageInFreeOrZeroedList_function_00334D20.md) (function, `0x00334D20`)

### Direct callers
- [MiCombineWithStandbyExisting](../22/MiCombineWithStandbyExisting_function_00229E74.md) at `0x0022A103`
- [MiCombineInitialInstance](../22/MiCombineInitialInstance_function_0022BC0C.md) at `0x0022C5B3`
- [MiResolveProtoCombine](../22/MiResolveProtoCombine_function_0022CD00.md) at `0x0022CF82`
- [MiActOnPte](../24/MiActOnPte_function_00244C90.md) at `0x0024594F`
- [sub_00283AFC](../28/Unknown_function_00283AFC.md) at `0x00283BD5`
- [MiUnlinkStandbyPfn](../2C/MiUnlinkStandbyPfn_function_002C3510.md) at `0x002C36EF`
- [MiRemoveLowestPriorityStandbyPage](../33/MiRemoveLowestPriorityStandbyPage_function_00334600.md) at `0x00334A33`
- [MiWalkEntireImage](../36/MiWalkEntireImage_function_00365D70.md) at `0x00366402`
- [MiZeroCfgSystemWideBitmapWorker](../36/MiZeroCfgSystemWideBitmapWorker_function_00367060.md) at `0x003674C5`
- [MiGetRepurposedSlabStandbyPage](MiGetRepurposedSlabStandbyPage_function_003755A8.md) at `0x00375676`
- [MiReservePageFileSpaceForPage](../38/MiReservePageFileSpaceForPage_function_0038377C.md) at `0x00383C88`
- [MiRepurposeStandbySlabPage](../38/MiRepurposeStandbySlabPage_function_00385780.md) at `0x00385944`
- [MiMakeOutswappedPageResident](../43/MiMakeOutswappedPageResident_function_00431AD0.md) at `0x00431F0C`
- [MiHandleSpecialPurposeMemoryCachedFault](../44/MiHandleSpecialPurposeMemoryCachedFault_function_0044C740.md) at `0x0044CA15`
- [MiHandleSpecialPurposeMemoryCachedFault](../44/MiHandleSpecialPurposeMemoryCachedFault_function_0044C740.md) at `0x0044CA5B`
- [MiRelinkTransitionSlabPages](../44/MiRelinkTransitionSlabPages_function_0044D060.md) at `0x0044D100`
- [MiMirrorPerformBrownWrites](../45/MiMirrorPerformBrownWrites_function_0045C560.md) at `0x0045C973`
- [MiPurgeSlabEntry](../48/MiPurgeSlabEntry_function_0048D444.md) at `0x0048D507`
- [MiWalkResetCommitPte](../66/MiWalkResetCommitPte_function_0066FD30.md) at `0x0066FD94`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00375954  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00375959  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
0037595E  57                              push rdi
0037595F  48 83 EC 20                     sub rsp, 0x20
00375963  8B F2                           mov esi, edx
00375965  48 8B D9                        mov rbx, rcx
00375968  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
00375972  48 8B F9                        mov rdi, rcx
00375975  33 D2                           xor edx, edx
00375977  48 2B F8                        sub rdi, rax
0037597A  48 B8 AB AA AA AA AA AA AA AA   movabs rax, 0xaaaaaaaaaaaaaaab
00375984  48 C1 FF 04                     sar rdi, 4
00375988  48 0F AF F8                     imul rdi, rax
0037598C  E8 FF 83 FC FF                  call 0x14033dd90
00375991  48 8B 43 18                     mov rax, qword ptr [rbx + 0x18]
00375995  48 B9 00 00 00 00 00 FF FF FF   movabs rcx, 0xffffff0000000000
0037599F  48 23 C1                        and rax, rcx
003759A2  48 8B CB                        mov rcx, rbx
003759A5  48 89 43 18                     mov qword ptr [rbx + 0x18], rax
003759A9  E8 42 00 00 00                  call 0x1403759f0
003759AE  48 8B 43 18                     mov rax, qword ptr [rbx + 0x18]
003759B2  48 B9 00 00 00 00 00 00 00 40   movabs rcx, 0x4000000000000000
003759BC  48 0B C1                        or rax, rcx
003759BF  83 CE 02                        or esi, 2
003759C2  48 8B CF                        mov rcx, rdi
003759C5  48 89 43 18                     mov qword ptr [rbx + 0x18], rax
003759C9  8B D6                           mov edx, esi
003759CB  E8 50 F3 FB FF                  call 0x140334d20
003759D0  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
003759D5  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
003759DA  48 83 C4 20                     add rsp, 0x20
003759DE  5F                              pop rdi
003759DF  C3                              ret
003759E0  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiDiscardTransitionPteEx(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_rsp = (v_rsp) - (32);
    a2 = 0;
    v_rdi = (a1) - (result);
    v_rdi = (v_rdi) >> (4);
    v_rdi = (v_rdi) * (result);
    result = MiRestoreTransitionPte(a1, a2, a3, a4);
    result = (*(unsigned __int64 *)(a1 + 24)) & (a1);
    *(unsigned __int64 *)(a1 + 24) = result;
    result = MiClearPfnReuseFields(a1, a2, a3, a4);
    result = (*(unsigned __int64 *)(a1 + 24)) | (a1);
    v_rsi = (unsigned int)(((unsigned int)(a2)) | (2));
    *(unsigned __int64 *)(a1 + 24) = result;
    result = MiInsertPageInFreeOrZeroedList(v_rdi, (unsigned int)((unsigned int)(v_rsi)), a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiDiscardTransitionPteEx(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    local_rsp = (local_rsp) - (32);
    Arg2 = 0;
    local_rdi = (Arg1) - (result);
    local_rdi = (local_rdi) >> (4);
    local_rdi = (local_rdi) * (result);
    result = MiRestoreTransitionPte(Arg1, Arg2, a3, a4);
    result = (*(uint64_t *)(arg1 + 0x18)) & (Arg1);
    *(uint64_t *)(arg1 + 0x18) = result;
    result = MiClearPfnReuseFields(Arg1, Arg2, a3, a4);
    result = (*(uint64_t *)(arg1 + 0x18)) | (Arg1);
    local_rsi = (uint32_t)(((uint32_t)(Arg2)) | (2));
    *(uint64_t *)(arg1 + 0x18) = result;
    result = MiInsertPageInFreeOrZeroedList(local_rdi, (uint32_t)((uint32_t)(local_rsi)), a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x18` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00375954&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00375954[BB_00375954]
  bb_003759E0[BB_003759E0]
```
