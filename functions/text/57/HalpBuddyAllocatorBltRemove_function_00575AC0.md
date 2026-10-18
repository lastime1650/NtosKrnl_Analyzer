# HalpBuddyAllocatorBltRemove

- RVA: `0x00575AC0`–`0x00575B00` (길이 `64` bytes)
- VA: `0x0000000140575AC0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CAAC`
- 디코드: `20`개 명령, `64/64` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00575AD4` → [KeAcquireSpinLockRaiseToDpc](../20/KeAcquireSpinLockRaiseToDpc_function_00208470.md) (function, `0x00208470`)
- `0x00575AE4` → [HalpBuddyAllocatorBltRemoveInternal](../46/HalpBuddyAllocatorBltRemoveInternal_function_004675BC.md) (function, `0x004675BC`)
- `0x00575AEF` → [KeReleaseSpinLock](../39/KeReleaseSpinLock_function_00392BA0.md) (function, `0x00392BA0`)

### Direct callers
- [HalpBuddyAllocatorDeleteSubtree](../47/HalpBuddyAllocatorDeleteSubtree_function_0047A890.md) at `0x0047A8D3`
- [HalpBuddyAllocatorReserveLogicalAddress](HalpBuddyAllocatorReserveLogicalAddress_function_00575D00.md) at `0x00575D9B`
- [HalpBuddyAllocatorReserveLogicalAddress](HalpBuddyAllocatorReserveLogicalAddress_function_00575D00.md) at `0x00575E89`
- [HalpBuddyAllocatorReserveLogicalAddress](HalpBuddyAllocatorReserveLogicalAddress_function_00575D00.md) at `0x00575EF1`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00575AC0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00575AC5  57                              push rdi
00575AC6  48 83 EC 20                     sub rsp, 0x20
00575ACA  48 8D 7A 68                     lea rdi, [rdx + 0x68]
00575ACE  48 8B D9                        mov rbx, rcx
00575AD1  48 8B CF                        mov rcx, rdi
00575AD4  E8 97 29 C9 FF                  call 0x140208470
00575AD9  44 8A C0                        mov r8b, al
00575ADC  48 39 1B                        cmp qword ptr [rbx], rbx
00575ADF  74 08                           je 0x140575ae9
00575AE1  48 8B CB                        mov rcx, rbx
00575AE4  E8 D3 1A EF FF                  call 0x1404675bc
00575AE9  41 8A D0                        mov dl, r8b
00575AEC  48 8B CF                        mov rcx, rdi
00575AEF  E8 AC D0 E1 FF                  call 0x140392ba0
00575AF4  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00575AF9  48 83 C4 20                     add rsp, 0x20
00575AFD  5F                              pop rdi
00575AFE  C3                              ret
00575AFF  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpBuddyAllocatorBltRemove(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    result = KeAcquireSpinLockRaiseToDpc(a2 + 104, a2, a3, a4);
    if ((*(unsigned __int64 *)(a1)) != a1) {
        a1 = a1;
        result = HalpBuddyAllocatorBltRemoveInternal(a1, a2, (unsigned __int8)(result), a4);
    }
    result = KeReleaseSpinLock(a2 + 104, (unsigned __int8)((unsigned __int8)(result)), (unsigned __int8)(result), a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HalpBuddyAllocatorBltRemove(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    result = KeAcquireSpinLockRaiseToDpc(Arg2 + 104, Arg2, a3, a4);
    if ((*(uint64_t *)(arg1)) != Arg1) {
        Arg1 = Arg1;
        result = HalpBuddyAllocatorBltRemoveInternal(Arg1, Arg2, (uint8_t)(result), a4);
    }
    result = KeReleaseSpinLock(Arg2 + 104, (uint8_t)((uint8_t)(result)), (uint8_t)(result), a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg2` | `+ 0x68` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00575AC0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00575AC0[BB_00575AC0]
  bb_00575AE1[BB_00575AE1]
  bb_00575AE9[BB_00575AE9]
  bb_00575AFF[BB_00575AFF]
  bb_00575AC0 -->|branch| bb_00575AE9
  bb_00575AC0 -->|fallthrough| bb_00575AE1
  bb_00575AE1 -->|flow| bb_00575AE9
```
