# CmpRemoveHiveFromNamespace

- RVA: `0x0049C4CC`–`0x0049C59B` (길이 `207` bytes)
- VA: `0x000000014049C4CC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00073808`
- 디코드: `54`개 명령, `207/207` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **14**; 고유 호출 대상: **12**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0049C4F1` → [CmpLockHashEntryExclusiveByKcb](../../page/84/CmpLockHashEntryExclusiveByKcb_function_00849780.md) (function, `0x00849780`)
- `0x0049C4F9` → [CmpLockKcbExclusive](../../page/86/CmpLockKcbExclusive_function_00861EB0.md) (function, `0x00861EB0`)
- `0x0049C501` → [CmpLockKcbExclusive](../../page/86/CmpLockKcbExclusive_function_00861EB0.md) (function, `0x00861EB0`)
- `0x0049C50A` → [HvLockHiveFlusherShared](../../page/84/HvLockHiveFlusherShared_function_0084F95C.md) (function, `0x0084F95C`)
- `0x0049C519` → [CmpFreeKeyByCell](../../page/84/CmpFreeKeyByCell_function_0084AD70.md) (function, `0x0084AD70`)
- `0x0049C52B` → [CmpFlushNotifiesOnKeyBodyList](../../page/9B/CmpFlushNotifiesOnKeyBodyList_function_009B3594.md) (function, `0x009B3594`)
- `0x0049C536` → [CmpMarkKeyUnbacked](../../page/9B/CmpMarkKeyUnbacked_function_009B3C4C.md) (function, `0x009B3C4C`)
- `0x0049C53E` → [CmpDiscardKcb](../../page/9B/CmpDiscardKcb_function_009B2F34.md) (function, `0x009B2F34`)
- `0x0049C549` → [CmpRemoveLayerLinkForDiscardedKcb](../../page/9B/CmpRemoveLayerLinkForDiscardedKcb_function_009B3BE0.md) (function, `0x009B3BE0`)
- `0x0049C55E` → [HvUnlockHiveFlusherShared](../../page/84/HvUnlockHiveFlusherShared_function_00848738.md) (function, `0x00848738`)
- `0x0049C566` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (function, `0x00BC92C0`)
- `0x0049C56E` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (function, `0x00BC92C0`)
- `0x0049C576` → [CmpUnlockHashEntryByKcb](../../page/86/CmpUnlockHashEntryByKcb_function_00864370.md) (function, `0x00864370`)
- `0x0049C594` → [CmpLogHiveDestroyEvent](../../page/7E/CmpLogHiveDestroyEvent_function_007E615C.md) (function, `0x007E615C`)

### Direct callers
- [CmpCompleteUnloadKey](../../page/9B/CmpCompleteUnloadKey_function_009B32FC.md) at `0x009B338E`
- [sub_00B17CEE](../../page/B1/Unknown_function_00B17CEE.md) at `0x00B17CFA`

### Static image references
- `0x0049C54E` → RVA `0x00FC6B08` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **14**
  - `0x0049C4F1` → [CmpLockHashEntryExclusiveByKcb](../../page/84/CmpLockHashEntryExclusiveByKcb_function_00849780.md) (`.text` → `PAGE`)
  - `0x0049C4F9` → [CmpLockKcbExclusive](../../page/86/CmpLockKcbExclusive_function_00861EB0.md) (`.text` → `PAGE`)
  - `0x0049C501` → [CmpLockKcbExclusive](../../page/86/CmpLockKcbExclusive_function_00861EB0.md) (`.text` → `PAGE`)
  - `0x0049C50A` → [HvLockHiveFlusherShared](../../page/84/HvLockHiveFlusherShared_function_0084F95C.md) (`.text` → `PAGE`)
  - `0x0049C519` → [CmpFreeKeyByCell](../../page/84/CmpFreeKeyByCell_function_0084AD70.md) (`.text` → `PAGE`)
  - `0x0049C52B` → [CmpFlushNotifiesOnKeyBodyList](../../page/9B/CmpFlushNotifiesOnKeyBodyList_function_009B3594.md) (`.text` → `PAGE`)
  - `0x0049C536` → [CmpMarkKeyUnbacked](../../page/9B/CmpMarkKeyUnbacked_function_009B3C4C.md) (`.text` → `PAGE`)
  - `0x0049C53E` → [CmpDiscardKcb](../../page/9B/CmpDiscardKcb_function_009B2F34.md) (`.text` → `PAGE`)
  - `0x0049C549` → [CmpRemoveLayerLinkForDiscardedKcb](../../page/9B/CmpRemoveLayerLinkForDiscardedKcb_function_009B3BE0.md) (`.text` → `PAGE`)
  - `0x0049C55E` → [HvUnlockHiveFlusherShared](../../page/84/HvUnlockHiveFlusherShared_function_00848738.md) (`.text` → `PAGE`)
  - `0x0049C566` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (`.text` → `PAGECMRC`)
  - `0x0049C56E` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (`.text` → `PAGECMRC`)
  - `0x0049C576` → [CmpUnlockHashEntryByKcb](../../page/86/CmpUnlockHashEntryByKcb_function_00864370.md) (`.text` → `PAGE`)
  - `0x0049C594` → [CmpLogHiveDestroyEvent](../../page/7E/CmpLogHiveDestroyEvent_function_007E615C.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0049C4CC  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0049C4D1  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
0049C4D6  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
0049C4DB  57                              push rdi
0049C4DC  48 83 EC 20                     sub rsp, 0x20
0049C4E0  48 8B 7A 48                     mov rdi, qword ptr [rdx + 0x48]
0049C4E4  48 8B E9                        mov rbp, rcx
0049C4E7  48 8B CF                        mov rcx, rdi
0049C4EA  49 8B D8                        mov rbx, r8
0049C4ED  48 8B 77 48                     mov rsi, qword ptr [rdi + 0x48]
0049C4F1  E8 8A D2 3A 00                  call 0x140849780
0049C4F6  48 8B CE                        mov rcx, rsi
0049C4F9  E8 B2 59 3C 00                  call 0x140861eb0
0049C4FE  48 8B CF                        mov rcx, rdi
0049C501  E8 AA 59 3C 00                  call 0x140861eb0
0049C506  48 8B 4F 20                     mov rcx, qword ptr [rdi + 0x20]
0049C50A  E8 4D 34 3B 00                  call 0x14084f95c
0049C50F  8B 57 28                        mov edx, dword ptr [rdi + 0x28]
0049C512  41 B0 01                        mov r8b, 1
0049C515  48 8B 4F 20                     mov rcx, qword ptr [rdi + 0x20]
0049C519  E8 52 E8 3A 00                  call 0x14084ad70
0049C51E  45 33 C9                        xor r9d, r9d
0049C521  4C 8B C3                        mov r8, rbx
0049C524  48 8B CF                        mov rcx, rdi
0049C527  41 8D 51 01                     lea edx, [r9 + 1]
0049C52B  E8 64 70 51 00                  call 0x1409b3594
0049C530  48 8B D3                        mov rdx, rbx
0049C533  48 8B CF                        mov rcx, rdi
0049C536  E8 11 77 51 00                  call 0x1409b3c4c
0049C53B  48 8B CF                        mov rcx, rdi
0049C53E  E8 F1 69 51 00                  call 0x1409b2f34
0049C543  48 8B D3                        mov rdx, rbx
0049C546  48 8B CF                        mov rcx, rdi
0049C549  E8 92 76 51 00                  call 0x1409b3be0
0049C54E  F7 05 B0 A5 B2 00 00 00 00 01   test dword ptr [rip + 0xb2a5b0], 0x1000000
0049C558  75 37                           jne 0x14049c591
0049C55A  48 8B 4F 20                     mov rcx, qword ptr [rdi + 0x20]
0049C55E  E8 D5 C1 3A 00                  call 0x140848738
0049C563  48 8B CF                        mov rcx, rdi
0049C566  E8 55 CD 72 00                  call 0x140bc92c0
0049C56B  48 8B CE                        mov rcx, rsi
0049C56E  E8 4D CD 72 00                  call 0x140bc92c0
0049C573  48 8B CF                        mov rcx, rdi
0049C576  E8 F5 7D 3C 00                  call 0x140864370
0049C57B  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
0049C580  48 8B 6C 24 38                  mov rbp, qword ptr [rsp + 0x38]
0049C585  48 8B 74 24 40                  mov rsi, qword ptr [rsp + 0x40]
0049C58A  48 83 C4 20                     add rsp, 0x20
0049C58E  5F                              pop rdi
0049C58F  C3                              ret
0049C590  CC                              int3
0049C591  48 8B CD                        mov rcx, rbp
0049C594  E8 C3 9B 34 00                  call 0x1407e615c
0049C599  EB BF                           jmp 0x14049c55a
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpRemoveHiveFromNamespace(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (32);
    result = CmpLockHashEntryExclusiveByKcb(*(unsigned __int64 *)(a2 + 72), a2, a3, a4);
    result = CmpLockKcbExclusive(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 72), a2, a3, a4);
    result = CmpLockKcbExclusive(*(unsigned __int64 *)(a2 + 72), a2, a3, a4);
    result = HvLockHiveFlusherShared(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 32), a2, a3, a4);
    result = CmpFreeKeyByCell(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 32), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 72) + 40)), 1, a4);
    a4 = 0;
    result = CmpFlushNotifiesOnKeyBodyList(*(unsigned __int64 *)(a2 + 72), a4 + 1, a3, a4);
    result = CmpMarkKeyUnbacked(*(unsigned __int64 *)(a2 + 72), a3, a3, a4);
    result = CmpDiscardKcb(*(unsigned __int64 *)(a2 + 72), a3, a3, a4);
    result = CmpRemoveLayerLinkForDiscardedKcb(*(unsigned __int64 *)(a2 + 72), a3, a3, a4);
    if (((*(unsigned int *)(v_rip + 11707824)) & (0x1000000ULL)) != 0) goto loc_0049C591;
loc_0049C55A:
    result = HvUnlockHiveFlusherShared(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 32), a3, a3, a4);
    result = CmpUnlockKcb(*(unsigned __int64 *)(a2 + 72), a3, a3, a4);
    result = CmpUnlockKcb(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 72), a3, a3, a4);
    result = CmpUnlockHashEntryByKcb(*(unsigned __int64 *)(a2 + 72), a3, a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
loc_0049C591:
    result = CmpLogHiveDestroyEvent(v_stack_p10, a3, a3, a4);
    goto loc_0049C55A;
}
```

## 5. (Beta) C Style

```c
int64_t CmpRemoveHiveFromNamespace(int64_t Arg1, void *Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (32);
    result = CmpLockHashEntryExclusiveByKcb(*(uint64_t *)(arg2 + 0x48), Arg2, Arg3, Arg4);
    result = CmpLockKcbExclusive(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x48), Arg2, Arg3, Arg4);
    result = CmpLockKcbExclusive(*(uint64_t *)(arg2 + 0x48), Arg2, Arg3, Arg4);
    result = HvLockHiveFlusherShared(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x20), Arg2, Arg3, Arg4);
    result = CmpFreeKeyByCell(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x20), (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x48) + 0x28)), 1, Arg4);
    Arg4 = 0;
    result = CmpFlushNotifiesOnKeyBodyList(*(uint64_t *)(arg2 + 0x48), Arg4 + 1, Arg3, Arg4);
    result = CmpMarkKeyUnbacked(*(uint64_t *)(arg2 + 0x48), Arg3, Arg3, Arg4);
    result = CmpDiscardKcb(*(uint64_t *)(arg2 + 0x48), Arg3, Arg3, Arg4);
    result = CmpRemoveLayerLinkForDiscardedKcb(*(uint64_t *)(arg2 + 0x48), Arg3, Arg3, Arg4);
    if (((*(uint32_t *)(v_rip + 0xB2A5B0)) & (0x1000000ULL)) != 0) goto loc_0049C591;
loc_0049C55A:
    result = HvUnlockHiveFlusherShared(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x20), Arg3, Arg3, Arg4);
    result = CmpUnlockKcb(*(uint64_t *)(arg2 + 0x48), Arg3, Arg3, Arg4);
    result = CmpUnlockKcb(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x48), Arg3, Arg3, Arg4);
    result = CmpUnlockHashEntryByKcb(*(uint64_t *)(arg2 + 0x48), Arg3, Arg3, Arg4);
    local_rsp = (local_rsp) + (32);
    return result;
loc_0049C591:
    result = CmpLogHiveDestroyEvent(v_stack_p10, Arg3, Arg3, Arg4);
    goto loc_0049C55A;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x48` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0049C4CC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0049C4CC[BB_0049C4CC]
  bb_0049C55A[BB_0049C55A]
  bb_0049C590[BB_0049C590]
  bb_0049C591[BB_0049C591]
  bb_0049C4CC -->|branch| bb_0049C591
  bb_0049C4CC -->|fallthrough| bb_0049C55A
  bb_0049C590 -->|flow| bb_0049C591
  bb_0049C591 -->|branch| bb_0049C55A
```
