# MiUnlockAwePagesShared

- RVA: `0x004C66C4`–`0x004C66FE` (길이 `58` bytes)
- VA: `0x00000001404C66C4`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `19`개 명령, `58/58` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **7**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004C66D5` → [ExReleaseAutoExpandPushLockShared](../26/ExReleaseAutoExpandPushLockShared_function_00263660.md) (function, `0x00263660`)
- `0x004C66F2` → [KiCheckForKernelApcDelivery](../2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (function, `0x002E2C80`)

### Direct callers
- [MiDeletePagablePteRange](../2A/MiDeletePagablePteRange_function_002A96B4.md) at `0x002A9927`
- [MiProtectAweRegion](MiProtectAweRegion_function_004CE62C.md) at `0x004CE815`
- [MiProtectAweRegion](MiProtectAweRegion_function_004CE62C.md) at `0x004CE848`
- [MiLockAweVadsShared](MiLockAweVadsShared_function_004CEE3C.md) at `0x004CEE70`
- [MiBuildPhysicalPageFreeChain](../68/MiBuildPhysicalPageFreeChain_function_00687C80.md) at `0x00687F70`
- [MiBuildPhysicalPageFreeChain](../68/MiBuildPhysicalPageFreeChain_function_00687C80.md) at `0x00687F7F`
- [MiAllocateUserPhysicalPages](../../page/80/MiAllocateUserPhysicalPages_function_00809828.md) at `0x0080A201`
- [MiAllocateUserPhysicalPages](../../page/80/MiAllocateUserPhysicalPages_function_00809828.md) at `0x0080A2B3`
- [NtMapUserPhysicalPages](../../page/80/NtMapUserPhysicalPages_function_0080B460.md) at `0x0080B6B1`
- [NtMapUserPhysicalPages](../../page/80/NtMapUserPhysicalPages_function_0080B460.md) at `0x0080B6DC`
- [NtMapUserPhysicalPagesScatter](../../page/80/NtMapUserPhysicalPagesScatter_function_0080B750.md) at `0x0080BA39`
- [NtMapUserPhysicalPagesScatter](../../page/80/NtMapUserPhysicalPagesScatter_function_0080B750.md) at `0x0080BAA7`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004C66C4  40 53                           push rbx
004C66C6  48 83 EC 20                     sub rsp, 0x20
004C66CA  48 8B C2                        mov rax, rdx
004C66CD  48 8B D9                        mov rbx, rcx
004C66D0  48 8B C8                        mov rcx, rax
004C66D3  33 D2                           xor edx, edx
004C66D5  E8 86 CF D9 FF                  call 0x140263660
004C66DA  90                              nop
004C66DB  66 83 83 E6 01 00 00 01         add word ptr [rbx + 0x1e6], 1
004C66E3  75 12                           jne 0x1404c66f7
004C66E5  48 8D 83 98 00 00 00            lea rax, [rbx + 0x98]
004C66EC  90                              nop
004C66ED  48 39 00                        cmp qword ptr [rax], rax
004C66F0  74 05                           je 0x1404c66f7
004C66F2  E8 89 C5 E1 FF                  call 0x1402e2c80
004C66F7  48 83 C4 20                     add rsp, 0x20
004C66FB  5B                              pop rbx
004C66FC  C3                              ret
004C66FD  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiUnlockAwePagesShared(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    a2 = 0;
    result = ExReleaseAutoExpandPushLockShared(a2, a2, a3, a4);
    if (condition_is_not_equal) goto loc_004C66F7;
    result = a1 + 152;
    if ((*(unsigned __int64 *)(a1 + 152)) != (a1 + 152)) {
        result = KiCheckForKernelApcDelivery(a2, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiUnlockAwePagesShared(void *Arg1, int64_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    Arg2 = 0;
    result = ExReleaseAutoExpandPushLockShared(Arg2, Arg2, a3, a4);
    if (condition_is_not_equal) goto loc_004C66F7;
    result = Arg1 + 152;
    if ((*(uint64_t *)(arg1 + 0x98)) != (Arg1 + 152)) {
        result = KiCheckForKernelApcDelivery(Arg2, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x98` | `64` | `R` |
| `Arg1` | `+ 0x1E6` | `16` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004C66C4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004C66C4[BB_004C66C4]
  bb_004C66E5[BB_004C66E5]
  bb_004C66F2[BB_004C66F2]
  bb_004C66F7[BB_004C66F7]
  bb_004C66FD[BB_004C66FD]
  bb_004C66C4 -->|branch| bb_004C66F7
  bb_004C66C4 -->|fallthrough| bb_004C66E5
  bb_004C66E5 -->|branch| bb_004C66F7
  bb_004C66E5 -->|fallthrough| bb_004C66F2
  bb_004C66F2 -->|flow| bb_004C66F7
```
