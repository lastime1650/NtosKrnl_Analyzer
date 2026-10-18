# KeAcquireQueuedSpinLockRaiseToSynch

- RVA: `0x005BD410`–`0x005BD461` (길이 `81` bytes)
- VA: `0x00000001405BD410`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CAAC`
- 디코드: `22`개 명령, `81/81` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x005BD435` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x005BD44E` → [KxAcquireQueuedSpinLock](../27/KxAcquireQueuedSpinLock_function_00273E20.md) (function, `0x00273E20`)

### Direct callers
- [DifKeAcquireQueuedSpinLockRaiseToSynchWrapper](../62/DifKeAcquireQueuedSpinLockRaiseToSynchWrapper_function_0062E870.md) at `0x0062E93D`

### Static image references
- `0x005BD42A` → RVA `0x00FC6D20` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005BD410  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
005BD415  57                              push rdi
005BD416  48 83 EC 20                     sub rsp, 0x20
005BD41A  48 8B F9                        mov rdi, rcx
005BD41D  44 0F 20 C3                     mov rbx, cr8
005BD421  BA 0C 00 00 00                  mov edx, 0xc
005BD426  44 0F 22 C2                     mov cr8, rdx
005BD42A  83 3D EF 98 A0 00 00            cmp dword ptr [rip + 0xa098ef], 0
005BD431  74 07                           je 0x1405bd43a
005BD433  8A CB                           mov cl, bl
005BD435  E8 C2 82 F3 FF                  call 0x1404f56fc
005BD43A  65 48 8B 0C 25 28 00 00 00      mov rcx, qword ptr gs:[0x28]
005BD443  48 C1 E7 04                     shl rdi, 4
005BD447  48 03 CF                        add rcx, rdi
005BD44A  48 8B 51 08                     mov rdx, qword ptr [rcx + 8]
005BD44E  E8 CD 69 CB FF                  call 0x140273e20
005BD453  8A C3                           mov al, bl
005BD455  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
005BD45A  48 83 C4 20                     add rsp, 0x20
005BD45E  5F                              pop rdi
005BD45F  C3                              ret
005BD460  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KeAcquireQueuedSpinLockRaiseToSynch(__int64 a1)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    if ((*(unsigned int *)(v_rip + 10524911)) != 0) {
        a1 = (unsigned __int8)(v_cr8);
        result = KiRaiseIrqlProcessIrqlFlags(a1, 12, a3, a4);
    }
    v_rdi = (a1) << (4);
    a1 = (*(unsigned __int64 *)(gs_base + (0 + 40))) + (v_rdi);
    result = KxAcquireQueuedSpinLock(a1, *(unsigned __int64 *)(a1 + 8), a3, a4);
    v_rsp = (v_rsp) + (32);
    return (unsigned __int8)(v_cr8);
}
```

## 5. (Beta) C Style

```c
int64_t KeAcquireQueuedSpinLockRaiseToSynch(int64_t Arg1)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    if ((*(uint32_t *)(v_rip + 0xA098EF)) != 0) {
        Arg1 = (uint8_t)(v_cr8);
        result = KiRaiseIrqlProcessIrqlFlags(Arg1, 12, a3, a4);
    }
    local_rdi = (Arg1) << (4);
    Arg1 = (*(uint64_t *)(gs_base + (0 + 0x28))) + (local_rdi);
    result = KxAcquireQueuedSpinLock(Arg1, *(uint64_t *)(Arg1 + 0x8), a3, a4);
    local_rsp = (local_rsp) + (32);
    return (uint8_t)(v_cr8);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005BD410&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005BD410[BB_005BD410]
  bb_005BD433[BB_005BD433]
  bb_005BD43A[BB_005BD43A]
  bb_005BD460[BB_005BD460]
  bb_005BD410 -->|branch| bb_005BD43A
  bb_005BD410 -->|fallthrough| bb_005BD433
  bb_005BD433 -->|flow| bb_005BD43A
```
