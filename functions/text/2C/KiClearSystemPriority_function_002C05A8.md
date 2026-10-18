# KiClearSystemPriority

- RVA: `0x002C05A8`–`0x002C0621` (길이 `121` bytes)
- VA: `0x00000001402C05A8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006E5DC`
- 디코드: `30`개 명령, `121/121` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **8**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x002C05C7` → [KiAcquireThreadLockRaiseToDpc](../39/KiAcquireThreadLockRaiseToDpc_function_00396280.md) (function, `0x00396280`)
- `0x002C05EB` → [KiClearPriorityFloor](../39/KiClearPriorityFloor_function_00396314.md) (function, `0x00396314`)
- `0x002C060B` → [KiProcessDeferredReadyList](../25/KiProcessDeferredReadyList_function_00250800.md) (function, `0x00250800`)

### Direct callers
- [PopFxIdleComponent](PopFxIdleComponent_function_002C01D8.md) at `0x002C02EB`
- [KeDisconnectInterrupt](../2D/KeDisconnectInterrupt_function_002D3588.md) at `0x002D3636`
- [KeConnectInterrupt](../2D/KeConnectInterrupt_function_002D3D5C.md) at `0x002D3E13`
- [KeConnectInterrupt](../2D/KeConnectInterrupt_function_002D3D5C.md) at `0x002D3F3A`
- [MiReplenishSlabAllocator](../37/MiReplenishSlabAllocator_function_003788E4.md) at `0x00378AE1`
- [PspUpdateContainerImpersonation](../39/PspUpdateContainerImpersonation_function_003931EC.md) at `0x003933A3`
- [PpmTryAcquireLock](../3B/PpmTryAcquireLock_function_003BEB9C.md) at `0x003BEC19`
- [PpmCheckCustomRun](../3B/PpmCheckCustomRun_function_003BEC2C.md) at `0x003BECF1`
- [MiDemoteSlabEntries](../4D/MiDemoteSlabEntries_function_004D89A0.md) at `0x004D8A08`
- [MiDemoteSlabEntries](../4D/MiDemoteSlabEntries_function_004D89A0.md) at `0x004D8A54`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002C05A8  48 8B C4                        mov rax, rsp
002C05AB  48 89 58 18                     mov qword ptr [rax + 0x18], rbx
002C05AF  57                              push rdi
002C05B0  48 83 EC 20                     sub rsp, 0x20
002C05B4  48 83 60 10 00                  and qword ptr [rax + 0x10], 0
002C05B9  48 8B FA                        mov rdi, rdx
002C05BC  48 8D 50 08                     lea rdx, [rax + 8]
002C05C0  C6 40 08 00                     mov byte ptr [rax + 8], 0
002C05C4  48 8B D9                        mov rbx, rcx
002C05C7  E8 B4 5C 0D 00                  call 0x140396280
002C05CC  48 85 FF                        test rdi, rdi
002C05CF  75 4B                           jne 0x1402c061c
002C05D1  44 0F BE 83 1B 03 00 00         movsx r8d, byte ptr [rbx + 0x31b]
002C05D9  C6 83 1B 03 00 00 20            mov byte ptr [rbx + 0x31b], 0x20
002C05E0  41 B1 01                        mov r9b, 1
002C05E3  48 8D 54 24 38                  lea rdx, [rsp + 0x38]
002C05E8  48 8B CB                        mov rcx, rbx
002C05EB  E8 24 5D 0D 00                  call 0x140396314
002C05F0  48 C7 43 40 00 00 00 00         mov qword ptr [rbx + 0x40], 0
002C05F8  48 8D 54 24 38                  lea rdx, [rsp + 0x38]
002C05FD  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
002C0606  44 8A 44 24 30                  mov r8b, byte ptr [rsp + 0x30]
002C060B  E8 F0 01 F9 FF                  call 0x140250800
002C0610  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
002C0615  48 83 C4 20                     add rsp, 0x20
002C0619  5F                              pop rdi
002C061A  C3                              ret
002C061B  CC                              int3
002C061C  44 8B 07                        mov r8d, dword ptr [rdi]
002C061F  EB BF                           jmp 0x1402c05e0
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiClearSystemPriority(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int8 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 24) = v_rbx;
    v_rsp = (v_rsp) - (32);
    *(unsigned __int8 *)(v_rsp + 8) = 0;
    result = KiAcquireThreadLockRaiseToDpc(a1, v_rsp + 8, a3, a4);
    if (a2 != 0) goto loc_002C061C;
    *(unsigned __int8 *)(a1 + 795) = 32;
loc_002C05E0:
    result = KiClearPriorityFloor(a1, v_stack_p10, (__int8)(*(unsigned __int8 *)(a1 + 795)), 1);
    *(unsigned __int64 *)(a1 + 64) = 0;
    result = KiProcessDeferredReadyList(*(unsigned __int64 *)(gs_base + (0 + 32)), v_stack_p10, v_stack_p8, 1);
    v_rsp = (v_rsp) + (32);
    return result;
loc_002C061C:
    goto loc_002C05E0;
}
```

## 5. (Beta) C Style

```c
int64_t KiClearSystemPriority(void *Arg1, int64_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint8_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x18) = local_rbx;
    local_rsp = (local_rsp) - (32);
    *(uint8_t *)(local_rsp + 0x8) = 0;
    result = KiAcquireThreadLockRaiseToDpc(Arg1, local_rsp + 8, a3, a4);
    if (Arg2 != 0) goto loc_002C061C;
    *(uint8_t *)(arg1 + 0x31B) = 32;
loc_002C05E0:
    result = KiClearPriorityFloor(Arg1, v_stack_p10, (int8_t)(*(uint8_t *)(arg1 + 0x31B)), 1);
    *(uint64_t *)(arg1 + 0x40) = 0;
    result = KiProcessDeferredReadyList(*(uint64_t *)(gs_base + (0 + 0x20)), v_stack_p10, v_stack_p8, 1);
    local_rsp = (local_rsp) + (32);
    return result;
loc_002C061C:
    goto loc_002C05E0;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x40` | `64` | `W` |
| `Arg1` | `+ 0x31B` | `8` | `R` |
| `Arg1` | `+ 0x31B` | `8` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002C05A8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002C05A8[BB_002C05A8]
  bb_002C05D1[BB_002C05D1]
  bb_002C05E0[BB_002C05E0]
  bb_002C061B[BB_002C061B]
  bb_002C061C[BB_002C061C]
  bb_002C05A8 -->|branch| bb_002C061C
  bb_002C05A8 -->|fallthrough| bb_002C05D1
  bb_002C05D1 -->|flow| bb_002C05E0
  bb_002C061B -->|flow| bb_002C061C
  bb_002C061C -->|branch| bb_002C05E0
```
